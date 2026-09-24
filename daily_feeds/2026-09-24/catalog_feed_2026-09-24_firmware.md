[CATALOG WATCHER FEED]
feed_date: 2026-09-24
watcher: firmware
```
[FINDING]
category: firmware
detail: LuxOS | S21++ / S19 XP Hydro | 2026-09-21 | Added S21++ and S19 XP Hydro hashboard support; raised S21+ temperature limits to 75C hot / 80C panic; fixed chip health attribution and metrics temperature-drop bugs; improved power target ramp stability
confidence: confirmed
source_url: https://docs.luxor.tech/firmware/changelog
date_found: 2026-09-24
watcher_inferred: false
note: LuxOS versions this changelog by release date; not present in baseline (latest luxos entry there is 2026-05-12) or in any past daily_feeds firmware file.
```
```
[FINDING]
category: firmware
detail: LuxOS | S21 XP / S21 Pro / S21 Pro+ / S21+ | 2026-08-11 | Fixed BM1370 miners rebooting at startup by ensuring chips reach hashing frequency before the health check engages
confidence: confirmed
source_url: https://docs.luxor.tech/firmware/changelog
date_found: 2026-09-24
watcher_inferred: false
note: Distinct dated entry on the same changelog page, between the 2026-07-31 and 2026-09-21 releases; not present in baseline or any past feed file.
```
```
[FINDING]
category: firmware
detail: LuxOS | S21 Hydro | 2026-07-31 | Introduced configurable ramp speed with new API commands; enhanced hashboard recovery with temperature-aware power targeting; added recovery-related events; improved tuner performance on miners with fewer hashboards; increased S21 Hydro hashrate ceiling
confidence: confirmed
source_url: https://docs.luxor.tech/firmware/changelog
date_found: 2026-09-24
watcher_inferred: false
note: Not present in baseline or any past feed file; page states an increased hashrate ceiling specifically for S21 Hydro.
```
```
[FINDING]
category: firmware
detail: LuxOS | S21 XP (A3HB70502 hashboard) | 2026-07-03 | Added S21 XP A3HB70502 hashboard support; fixed configuration partition recreation and installer mount handling issues
confidence: confirmed
source_url: https://docs.luxor.tech/firmware/changelog
date_found: 2026-09-24
watcher_inferred: false
note: Not present in baseline or any past feed file.
```
```
[FINDING]
category: firmware
detail: LuxOS | S21 Pro+ / S21+ / S21 Hydro / S19 XP Hydro | 2026-06-02 | Added S21 Pro+ and S21+ hashboard support; included S21 Hydro and S19 XP Hydro in the autotuner; raised hydro maximum voltage to 22.0V; improved autotuner cleanup phase; added Antminer PSU diagnostics
confidence: confirmed
source_url: https://docs.luxor.tech/firmware/changelog
date_found: 2026-09-24
watcher_inferred: false
note: Oldest of five new dated releases found on this page; not present in baseline (latest luxos entry there is 2026-05-12) or any past feed file.
```
```
[FINDING]
category: firmware
detail: Braiins OS | models not stated on this page | 2026-09-11-0-7a758742-26.09-plus | changelog text not accessible this session; version, "26.09" folder name and Sept 16 2026 release date read from the downloads directory listing only
confidence: likely
source_url: https://downloads.braiins.com/braiins-os/
date_found: 2026-09-24
watcher_inferred: true
note: Directory listing shows folder "26.09" (identifier 2026-09-11-0-7a758742-26.09-plus, dated Sept 16 2026) as newest, above 26.08.1/26.08/26.07; baseline's latest braiins_os entry is 2026-05-07-0-e6eaa788-26.05-plus (2026-05-13), so this supersedes it. academy.braiins.com/en/braiins-os/changelog/, /braiins-os-plus/changelog/, /en/braiins-os/ and braiins.com/os/release-notes all returned 404, so supported models and changelog text could not be confirmed.
```
```
[FINDING]
category: firmware
detail: ePIC | Whatsminer M3x / M5x | V0.26.0 | no changelog text printed on this page; version, model and March 2024 date shown only in the firmware-download table
confidence: confirmed
source_url: https://epicblockchain.io/support/firmware-download/
date_found: 2026-09-24
watcher_inferred: false
note: Separate "UMC Firmware" table row from the Antminer S19x/S21x/T21 V1.24.0 row already reported in the 2026-09-23 feed; not present in baseline or any past feed file. Table's own date (March 2024) is older than today, but the page lists it in the "Latest Version" column for these models.
```
```
[FINDING]
category: firmware
detail: ePIC | BlockMiner 520i | V0.23.2 | no changelog text printed on this page; version, model and September 2023 date shown only in the firmware-download table
confidence: confirmed
source_url: https://epicblockchain.io/support/firmware-download/
date_found: 2026-09-24
watcher_inferred: false
note: "UMC Firmware" table row on ePIC's own firmware-download page; not present in baseline or any past feed file. Table's own date (September 2023) is older than today, but the page lists it in the "Latest Version" column for this model.
```
human should look at:
- Baseline KNOWN lines `stock_canaan|A15PROA15XPA15A15SE_A15x-K210-A3197S-Temp70_25112501_25462b2_40c74c6.zip||` and `stock_canaan|A15PROA15XPA15A15SE_A15x-K230_release_OTA_2025081201_131780c.zip||` are K210/K230 AI control-board builds filed under the stock_canaan (SHA-256 firmware) family; this watcher's mandate is to ignore K210/K230 AI builds, so these two lines look mis-filed.
- Baseline line `other|closed beta (no version); example shows VNish 1.2.6 detected||` has descriptive text in the version field rather than an actual version string; looks malformed.
