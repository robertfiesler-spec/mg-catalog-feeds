[CATALOG WATCHER FEED]
feed_date: 2026-09-23
watcher: manufacturer
```
[FINDING]
category: new_model
detail: Antminer S21e XP Hyd. | 430 TH/s | 5590 W | 13 J/TH | hydro | 2026-Q4
confidence: confirmed
source_url: https://shop.bitmain.com/product/detail?pid=000202608101645025339zMWHzD70684
date_found: 2026-09-23
watcher_inferred: false
note: Bitmain shop product-detail API (shop-product-service.bitmain.com/api/product/getDetail) prints hashRate "430T", powerConsumption "5590W", unitPower "13J/T", coolingFlag hydro, shipInfo "Shipping from Q4 2026". This is the single-unit SKU, distinct from the already-known 3U rack version Antminer S21e XP Hyd 3U (Bitmain shop code U3S21EXPH, listed alongside it at 860T/11180W/13J/T for two units = same per-unit numbers x2). Not in KNOWN or PENDING as a standalone SKU.
```
```
[FINDING]
category: new_model
detail: WhatsMiner M7BS | 500-552 TH/s | 7200 W (10kW high-performance mode) | 13.5 J/TH | hydro | unknown
confidence: confirmed
source_url: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM7BS_1778138155435.pdf
date_found: 2026-09-23
watcher_inferred: false
note: Official MicroBT datasheet (Chinese, linked from whatsminer.com product_manual page via /renren-fast/app/v2/presales/getFileProductList + downloadFile API, file id 90, created 2026-05-07) prints hashrate 500T~552T +/-10%, power 7200W+/-10% normal mode (10kW+/-10% high-performance mode), 13.5J/T+/-5%, hydro-cooled with 90C outlet; doc dated Feb 2026, no product release date stated. Differs from pending line whatsminer-m7bs (WhatsMiner M7BS+) only by the "+" suffix, so per the +/++ rule this is a distinct SKU, not that pending line — adjacent to it.
```
```
[FINDING]
category: new_model
detail: WhatsMiner M6BS+ | 390-450 TH/s | 7200 W (10kW high-performance mode) | 17 J/TH | hydro | unknown
confidence: confirmed
source_url: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM6BS%2B_1778135746133.pdf
date_found: 2026-09-23
watcher_inferred: false
note: Official MicroBT datasheet (file id 87, created 2026-05-07, doc dated Feb 2026) prints hashrate 390T~450T +/-10%, power 7200W+/-10% normal mode (10kW+/-10% high-performance mode), 17J/T+/-5%, hydro-cooled with 90C outlet, no release date stated. Differs from pending line whatsminer-m6bs (WhatsMiner M6BS++) only by "+" vs "++", so per the +/++ rule this is a distinct SKU, not that pending line — adjacent to it.
```
```
[FINDING]
category: new_model
detail: WhatsMiner M6AS+ | 390-450 TH/s | 10 kW (input) | 17 J/TH | hydro | unknown
confidence: likely
source_url: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM6AS%2B_1778122976176.pdf
date_found: 2026-09-23
watcher_inferred: false
note: Official MicroBT datasheet (file id 82, created 2026-05-07, doc dated Apr 2026) prints hashrate 390T~450T +/-10%, 17J/T+/-5% power ratio, hydro-cooled with 70C outlet (lower than the M6BS+/M7BS siblings' 90C). Power is marked "likely" because the only wattage figure printed on this page is "Input 10kW" — unlike the sibling M6BS+/M7BS docs it does not separately state a normal-mode wall-power figure, so it is unclear if 10kW is the rated consumption or an input-capacity spec; reported as printed. Differs from pending line whatsminer-m6as (WhatsMiner M6AS++) only by "+" vs "++", so per the +/++ rule this is a distinct SKU, not that pending line — adjacent to it.
```
