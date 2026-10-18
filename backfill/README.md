# backfill/

One-off, curated feed files: findings from `daily_feeds/` that were written but never ingested, because the laptop read the Google Sheet until the 2026-10-19 cutover.

- Every `[FINDING]` block is copied **verbatim** from the daily feed named in the PR that added it. Nothing is re-typed or edited.
- The daily job (`run_catalog_daily.sh`) never reads this folder. Its catch-up only scans `daily_feeds/<date>/catalog_feed_<date>_<watcher>.md`.
- Ingest happens once, by hand, with the same ceremony as any catalog write: dry-run, then operator GO, then `--execute`, then verify row counts. The origin is `git`, so `source_tool` reads `claude_watcher_<watcher>_<feed_date>`.
- Design and decision trail: Mining Guardian project doc `claude/RUNNING_FINDINGS_2026-10-18.md`.
