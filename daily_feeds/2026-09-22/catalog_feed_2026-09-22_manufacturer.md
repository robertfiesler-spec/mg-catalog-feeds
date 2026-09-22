[CATALOG WATCHER FEED]
feed_date: 2026-09-22
watcher: manufacturer
```
[FINDING]
category: new_model
detail: Antminer S19e XP Hyd. | 251 TH/s | 5522 W | 22 J/TH | hydro | unknown
confidence: confirmed
source_url: https://shop.bitmain.com/product/detail?pid=00020240522173522667K739304605B3
date_found: 2026-09-22
watcher_inferred: false
note: Bitmain shop product page prints "251T 5522W 22J/T", hydro-cooled, power efficiency on wall @35C 22 J/TH; listed Sold Out, no release date on page. Confirms pending line antminer-s19e-xp-hyd hunted from aggregator host www.f2pool.com.
```
```
[FINDING]
category: new_model
detail: WhatsMiner M7AS | 500-552 TH/s | 7200 W | 13.5 J/TH | hydro | unknown
confidence: confirmed
source_url: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM7AS_1778123572892.pdf
date_found: 2026-09-22
watcher_inferred: false
note: Official MicroBT datasheet (Chinese, linked from whatsminer.com product_manual page, file id 85, created 2026-05-07) prints hashrate 500T~552T +/-10%, power 7200 W +/-10% normal mode (10 kW high-performance mode), 13.5 J/T +/-5%, hydro-cooled with 70C outlet; document dated 2026-04, product release date not stated. Not in KNOWN (only M7AS+ is) and not in PENDING.
```
```
[FINDING]
category: rumor_model
detail: Bitaxe Naja Duo | unknown | unknown | unknown | unknown | unknown
confidence: unconfirmed
source_url: https://github.com/bitaxeorg/ESP-Miner/blob/master/main/device_config.h
date_found: 2026-09-22
watcher_inferred: true
note: ESP-Miner master (commit 0c798de, 2026-09-18) defines FAMILY_NAJA_DUO, board version 1201 (configs/config-1201.csv, devicemodel NajaDuo, asicmodel BM1373, 2 ASICs); the repo prints no rated hashrate, power or efficiency (max_power=60 is a firmware limit, not a rating) and bitaxe.org shows no specs. New family not in KNOWN or PENDING.
```
```
[FINDING]
category: industry
detail: Bitmain launches ANTRACK AR30 and AR31 47U modular hydro-cooling cabinets (20x S23e U2H per module, up to 200 kW, 380-480 V input); on sale since 2026-09-10, AR30 $16,000 and AR31 $20,000 per set, shipping 45 business days after payment
confidence: confirmed
source_url: https://www.bitmain.com/news-detail/antrack-ar30--ar31-modular-hydro-cooling-cabinets-designed-for-antminer-465
date_found: 2026-09-22
watcher_inferred: false
note: Bitmain news post dated 2026-09-22; infrastructure for hydro Antminers, not a miner model; AR31 integrates a dry cooler with 50C outlet and heat recovery, AR30 connects to existing cooling.
```
