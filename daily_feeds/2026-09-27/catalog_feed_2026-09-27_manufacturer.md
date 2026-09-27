[CATALOG WATCHER FEED]
feed_date: 2026-09-27
watcher: manufacturer

```
[FINDING]
category: new_model
detail: WhatsMiner M7AS | 500-552 TH/s | 7200 W | 13.5 J/T | hydro | unknown
confidence: confirmed
source_url: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM7AS_1778123572892.pdf
date_found: 2026-09-27
watcher_inferred: false
note: Product manual (dated April 2026) prints 500-552 TH/s at 13.5 J/T +-5%, 7200W +-10% normal mode (10kW +-10% high-performance mode also listed); hydro, outlet up to 70C. Neither known nor pending baseline has bare M7AS (M7AS+ is known); still not in either baseline as of today's snapshot, so re-flagged from 2026-09-26.
```

```
[FINDING]
category: new_model
detail: Bitaxe Naja Duo | unknown | 60 W | unknown | unknown | unknown
confidence: likely
source_url: https://github.com/bitaxeorg/ESP-Miner/blob/c75aa99dc867db6ed1f38c7add113c452f263633/main/device_config.h
date_found: 2026-09-27
watcher_inferred: true
note: Board family FAMILY_NAJA_DUO (board_version 1201) in ESP-Miner firmware; dual BM1373 ASIC, 60W is a firmware power-consumption target not a confirmed rated spec. No hashrate or J/TH published. Not in known or pending baselines; still absent as of today's snapshot, so re-flagged from 2026-09-26.
```

