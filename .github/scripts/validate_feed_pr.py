#!/usr/bin/env python3
"""Gate for auto-merging watcher feed PRs (mg-catalog-feeds).

A PR is auto-mergeable only if it is a pure APPEND of daily feed files:
  * every changed path is an ADDED file (no modify / delete / rename),
  * every path is daily_feeds/<date>/catalog_feed_<date>_<watcher>.md,
  * the file's header agrees with its path (feed_date, watcher),
  * the body is either the single line [NO NEW FINDINGS] or >=1 fenced
    [FINDING] block whose keys are exactly the seven the intake expects,
    in order.
Anything else exits 1 with the reasons on stdout, and the PR is left for a
human. This is the repo's append-only rule, enforced by a machine instead
of by trust.

Usage: validate_feed_pr.py <name-status-file> [repo-root]
  <name-status-file> is the output of `git diff --name-status <base>...<head>`.
"""
import re
import sys
from pathlib import Path

WATCHERS = ("manufacturer", "aggregator", "community", "firmware")
PATH_RE = re.compile(
    r"^daily_feeds/(\d{4}-\d{2}-\d{2})/catalog_feed_(\d{4}-\d{2}-\d{2})_(%s)\.md$"
    % "|".join(WATCHERS)
)
KEYS = ("category", "detail", "confidence", "source_url", "date_found",
        "watcher_inferred", "note")
# Mirrors standing_feed_intake.py MODEL_CATS | ALIAS_CATS | FIRMWARE_CATS | HELD_CATS
CATEGORIES = {"new_model", "rumor_model", "alias", "firmware",
              "spec_correction", "issue", "field_report", "industry"}
CONFIDENCE = {"confirmed", "likely", "unconfirmed"}
MAX_FILES = len(WATCHERS)


def check_body(text: str, date: str, watcher: str) -> list[str]:
    errs: list[str] = []
    lines = text.splitlines()
    if len(lines) < 4:
        return ["file too short"]
    if lines[0].strip() != "[CATALOG WATCHER FEED]":
        errs.append("line 1 must be [CATALOG WATCHER FEED]")
    if lines[1].strip() != f"feed_date: {date}":
        errs.append(f"line 2 must be 'feed_date: {date}' (path/header mismatch)")
    if lines[2].strip() != f"watcher: {watcher}":
        errs.append(f"line 3 must be 'watcher: {watcher}' (path/header mismatch)")
    rest = [l for l in lines[3:] if l.strip()]
    if rest == ["[NO NEW FINDINGS]"]:
        return errs
    if "[NO NEW FINDINGS]" in rest:
        errs.append("[NO NEW FINDINGS] must be the only body line")
        return errs
    # fenced blocks
    blocks, cur, inside = [], [], False
    for l in lines[3:]:
        s = l.rstrip()
        if s.startswith("```"):
            if inside:
                blocks.append(cur)
                cur = []
            inside = not inside
            continue
        if inside:
            cur.append(s)
        elif s.strip():
            errs.append(f"text outside a fenced block: {s[:60]!r}")
    if inside:
        errs.append("unterminated fenced block")
    if not blocks:
        errs.append("no [FINDING] blocks and no [NO NEW FINDINGS]")
    for i, b in enumerate(blocks, 1):
        if not b or b[0].strip() != "[FINDING]":
            errs.append(f"block {i}: first line must be [FINDING]")
            continue
        body = b[1:]
        keys = [l.split(":", 1)[0].strip() for l in body]
        if tuple(keys) != KEYS:
            errs.append(f"block {i}: keys must be exactly {list(KEYS)}, got {keys}")
            continue
        kv = {l.split(":", 1)[0].strip(): l.split(":", 1)[1].strip() for l in body}
        if kv["category"] not in CATEGORIES:
            errs.append(f"block {i}: bad category {kv['category']!r}")
        if kv["confidence"] not in CONFIDENCE:
            errs.append(f"block {i}: bad confidence {kv['confidence']!r}")
        if kv["watcher_inferred"] not in ("true", "false"):
            errs.append(f"block {i}: watcher_inferred must be true/false")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", kv["date_found"]):
            errs.append(f"block {i}: date_found not YYYY-MM-DD")
        if not re.match(r"^https?://", kv["source_url"]):
            errs.append(f"block {i}: source_url must be http(s)")
        if kv["category"] in ("new_model", "rumor_model") and kv["detail"].count("|") != 5:
            errs.append(f"block {i}: model detail needs 6 '|'-separated fields")
    return errs


def main() -> int:
    ns_file = Path(sys.argv[1])
    root = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(".")
    errs: list[str] = []
    entries = [l.split("\t") for l in ns_file.read_text().splitlines() if l.strip()]
    if not entries:
        errs.append("PR changes no files")
    if len(entries) > MAX_FILES:
        errs.append(f"PR changes {len(entries)} files (max {MAX_FILES})")
    seen = set()
    for e in entries:
        status, path = e[0], e[-1]
        if status != "A":
            errs.append(f"{path}: status {status} (only added files are auto-merged)")
            continue
        m = PATH_RE.match(path)
        if not m or m.group(1) != m.group(2):
            errs.append(f"{path}: not daily_feeds/<date>/catalog_feed_<date>_<watcher>.md")
            continue
        date, watcher = m.group(1), m.group(3)
        if (date, watcher) in seen:
            errs.append(f"{path}: duplicate date/watcher in one PR")
        seen.add((date, watcher))
        try:
            text = (root / path).read_text(encoding="utf-8")
        except Exception as ex:  # noqa: BLE001
            errs.append(f"{path}: unreadable ({ex})")
            continue
        errs += [f"{path}: {x}" for x in check_body(text, date, watcher)]
    if errs:
        print("NOT auto-mergeable:")
        for x in errs:
            print(f"  - {x}")
        return 1
    print(f"auto-mergeable: {len(entries)} appended feed file(s): "
          + ", ".join(e[-1] for e in entries))
    return 0


if __name__ == "__main__":
    sys.exit(main())
