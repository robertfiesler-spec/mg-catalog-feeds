# mg-catalog-feeds

Daily watcher feed files for the Mining Guardian catalog intake.

- Writers: four Claude scheduled tasks (manufacturer, aggregator, firmware, community), one commit per run.
- Reader: the laptop's 13:00 CDT `run_catalog_daily.sh` (`git pull --ff-only`, then `run_standing_pipe_daily.sh` with catch-up).
- Layout: `daily_feeds/<YYYY-MM-DD>/catalog_feed_<YYYY-MM-DD>_<watcher>.md`
- Format: `[CATALOG WATCHER FEED]` header (`feed_date:`, `watcher:`) then either `[NO NEW FINDINGS]` or fenced `[FINDING]` blocks
  (`category`, `detail`, `confidence`, `source_url`, `date_found`, `watcher_inferred`, `note`) — identical to what
  `sheet_to_feed.py` produced from the Google Sheet, so the intake is unchanged.
- Rules: append-only; never rewrite a past day's file (the intake hashes finding-blocks and logs `monitoring.standing_feed_runs`
  by (feed_date, watcher, sha256)). A correction is a new finding in a later day's file, citing the earlier one.
- Design: Mining-Guardian repo `claude/26_WATCHER_MIGRATION_DESIGN.md`.
