[CATALOG WATCHER FEED]
feed_date: 2026-09-24
watcher: manufacturer
```
[FINDING]
category: new_model
detail: Bitaxe Naja Duo | unknown | 60 W | unknown | unknown | unknown
confidence: likely
source_url: https://github.com/bitaxeorg/ESP-Miner/blob/0c798deddf1e4e103c072b23c31e96f9e57c27ee/main/device_config.h
date_found: 2026-09-24
watcher_inferred: false
note: ESP-Miner firmware (bitaxeorg, commit 0c798de, main/device_config.h) defines FAMILY_NAJA_DUO: BM1373 ASIC x2, max_power=60W, nominal 12V, board_version 1201; main/images/README.md confirms the product name "Naja Duo" with a 320x170 ST7789 display. No hashrate, J/TH, cooling type, or release date found on bitaxe.org or in the repo; not in KNOWN or PENDING.
```
```
[FINDING]
category: new_model
detail: NerdQAxe+ | 2.5 TH/s | 55 W | 22 J/TH | unknown | unknown
confidence: likely
source_url: https://github.com/shufps/qaxe/blob/be1a4a071def733a601a62b4fda3f3c5558c332e/README.md
date_found: 2026-09-24
watcher_inferred: false
note: qaxe repo README (shufps, commit be1a4a0) lists NerdQAxe+ as current design, 4x BM1368 ASICs, "~2.5TH/s at ~55 W (~22 J/TH)", hardware revision 5.0. KNOWN only has nerdqaxeplus-hydro (NerdQaxePlus Hydro); this SKU is not named as hydro anywhere on the page, so per the cooling-word rule it is a distinct product from that known line — adjacent to it. No release date stated.
```
```
[FINDING]
category: rumor_model
detail: WhatsMiner M7AS | unknown | unknown | unknown | unknown | unknown
confidence: unconfirmed
source_url: https://www.whatsminer.com/renren-fast/app/v2/presales/getFileProductList
date_found: 2026-09-24
watcher_inferred: true
note: WhatsMiner's own product-manual API (backing https://www.whatsminer.com/src/views/product_manual.html) lists a datasheet "WhatsMinerM7AS.pdf" (id 85, created 2026-05-07) alongside the already-known M7AS+ (id 86). The site's downloadFile endpoint errored for every id tried, so no figures were readable. KNOWN has whatsminer-m7as-plus (M7AS+) only; per the +/++ rule bare M7AS is a distinct SKU — adjacent to that known line.
```
