[CATALOG WATCHER FEED]
feed_date: 2026-10-04
watcher: manufacturer
```
[FINDING]
category: new_model
detail: WhatsMiner M7AS | 500-552 TH/s | 7200 W | 13.5 J/TH | hydro | unknown
confidence: confirmed
source_url: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/WhatsMinerM7AS_1778123567731.pdf
date_found: 2026-10-04
watcher_inferred: false
note: MicroBT product manual (dated April 2026, no release date printed) prints 500 T-552 T +/-10%, 13.5 J/T +/-5%, 7200 W +/-10% normal mode (10 kW high performance), hydro; still absent from KNOWN and PENDING (also reported 2026-10-03); adjacent to known M7AS+ and pending whatsminer-m7a.
```
```
[FINDING]
category: rumor_model
detail: Bitaxe Naja Duo | unknown | unknown | unknown | unknown | unknown
confidence: unconfirmed
source_url: https://github.com/bitaxeorg/ESP-Miner/blob/master/main/device_config.h
date_found: 2026-10-04
watcher_inferred: true
note: ESP-Miner master (2026-10-03) defines FAMILY_NAJA_DUO, board 1201 (configs/config-1201.csv, devicemodel NajaDuo, BM1373, 2 ASICs); repo prints no rated hashrate/power/efficiency (max_power=60 is a firmware limit, not a rating); still absent from KNOWN and PENDING (reported since 2026-09-22).
```
```
[FINDING]
category: new_model
detail: NerdQAxe+ | 2.5 TH/s | 55 W | 22 J/TH | unknown | unknown
confidence: likely
source_url: https://github.com/shufps/qaxe/blob/be1a4a071def733a601a62b4fda3f3c5558c332e/README.md
date_found: 2026-10-04
watcher_inferred: false
note: Maker repo README prints "~2.5TH/s at ~55 W (~22 J/TH)" (approximate figures, hence likely); KNOWN has only NerdQaxePlus Hydro and NerdQaxePlusPlus variants, not plain NerdQAxe+; cooling and release date not stated.
```
