[CATALOG WATCHER FEED]
feed_date: 2026-09-25
watcher: manufacturer

```
[FINDING]
category: new_model
detail: Antminer S21e XP Hyd. | 430 TH/s | 5590 W | 13 J/TH | hydro | 2026-Q4
confidence: confirmed
source_url: https://shop.bitmain.com/
date_found: 2026-09-25
watcher_inferred: false
note: Shop listing/API prints 430T/5590W/13J/T, hydro, "Shipping from Q4 2026"; distinct from already-known S21e Hyd (288T, no XP) and S21e XP Hyd 3U (860T, shop code U3S21EXPH).
```

```
[FINDING]
category: new_model
detail: Antminer S19e XP Hyd. | 251 TH/s | 5522 W | 22 J/TH | hydro | unknown
confidence: confirmed
source_url: https://shop.bitmain.com/
date_found: 2026-09-25
watcher_inferred: false
note: Hunted from pending antminer-s19e-xp-hyd (f2pool.com); confirmed on Bitmain's own shop with 251T/5522W/22J/T, hydro; listing shows "Shipping in 10 working days after fully paid", no explicit release month given.
```

```
[FINDING]
category: rumor_model
detail: Bitaxe Gamma 603 | unknown | unknown | unknown | unknown | unknown
confidence: unconfirmed
source_url: https://github.com/bitaxeorg/ESP-Miner/blob/master/main/device_config.h
date_found: 2026-09-25
watcher_inferred: true
note: ESP-Miner firmware repo defines board version 603 (family Gamma, BM1370, power_consumption_target 22W, same target as Gamma 602); no TH/s or W datasheet published; not in KNOWN or PENDING lists.
```

```
[FINDING]
category: rumor_model
detail: Bitaxe Naja Duo | unknown | 60 W | unknown | unknown | unknown
confidence: unconfirmed
source_url: https://github.com/bitaxeorg/ESP-Miner/blob/master/main/device_config.h
date_found: 2026-09-25
watcher_inferred: true
note: New family in ESP-Miner firmware repo (board 1201): dual BM1373 ASICs, max_power=60W per FAMILY_NAJA_DUO config; hashrate/efficiency not published; wholly new device with no matching KNOWN/PENDING entry.
```

```
[FINDING]
category: rumor_model
detail: Bitaxe Supra Hex 702 | unknown | unknown | unknown | unknown | unknown
confidence: unconfirmed
source_url: https://github.com/bitaxeorg/ESP-Miner/blob/master/main/device_config.h
date_found: 2026-09-25
watcher_inferred: true
note: ESP-Miner firmware repo defines board 702 (family SupraHex, BM1368, power_consumption_target 90W, same as known board 701 "Supra Hex 701"); no TH/s or W datasheet. Adjacent to pending "Bitaxe Supra Hex 703" (bt-miners.com) — repo shows 702 not 703, possible numbering error in that rumor.
```
