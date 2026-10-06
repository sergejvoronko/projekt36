---
title: "BMW M50 vs M50TU vs M52: The Complete Comparison Guide"
description: "BMW M50 vs M50TU vs M52 for an E36 build: years, power, block material, VANOS, engine management and the internal differences, from Bentley, Wikipedia and engine-builder sources."
pillar: engine
keywords: "m50 vs m52, m50tu differences, m50 vs m50tu, bmw m50 engine guide"
date: "2026-03-16"
hero: "engine-compare-v2.webp"
reviewed: "2026-10-06"
sources:
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998 (engine management by year, VANOS, knock sensors)"
  - title: "Wikipedia: BMW M50"
    url: "https://en.wikipedia.org/wiki/BMW_M50"
  - title: "Wikipedia: BMW M52"
    url: "https://en.wikipedia.org/wiki/BMW_M52"
  - title: "Bimmerfest: M50B25 NV or TU engine for a stroker with M52B28 internals (rod length, valve stems, springs)"
    url: "https://www.bimmerfest.com/threads/m50b25-nv-or-tu-engine-for-stroker-with-m52b28-internals.1405005/"
  - title: "R3VLimited: M50/S50 and M52/S52 engine questions"
    url: "https://www.r3vlimited.com/board/forum/e30-technical-forums/general-technical/3232-m50-s50-m52-s52-engine-questions"
---

## TL;DR

| | M50B25 (non-VANOS) | M50B25TU (VANOS) | M52B25 / M52B28 |
|---|---|---|---|
| **Built** | 1990–1992 (E36: up to 8/1992) | 1992–1996 | 1995–2000 |
| **Power** | 192 PS | 192 PS | 170 PS / 193 PS |
| **Torque** | 245 Nm @ 4,700 rpm | 250 Nm @ 4,200 rpm | 245 Nm / 280 Nm @ 3,950 rpm |
| **Block** | Cast iron | Cast iron | Aluminium in most markets (Nikasil, later iron sleeves); cast iron in original US/Canadian cars |
| **VANOS** | None | Single (intake, up to 12.5°) | Single (intake) |
| **Engine management (Bentley)** | Bosch DME M3.1 (OBD1) | Bosch DME M3.3.1 (OBD1) | Siemens MS41.1 (OBD2, 1996 on) |
| **Knock sensors** | None | Two | Two |
| **Connecting rods** | 135 mm | 140 mm | 135 mm |
| **Valve stems** | 7 mm | 6 mm | 6 mm |
| **Valve springs** | Double | Single | Single |

---

## M50 non-VANOS: the original

Built 1990–1992 (E34 525i and the earliest E36 325i). In E36s, Bentley dates the change to VANOS engines to cars built after August 1992.

- **No VANOS** to maintain or reseal, and simpler timing work.
- **Bosch DME M3.1**, which has **no knock sensors**: Bentley lists the 1992 M50 as the only engine in the E36 range without them.
- **Internals:** engine builders note **double valve springs**, **7 mm valve stems** and **135 mm connecting rods**. That's why the non-VANOS head and rods are popular for high-rpm and boosted builds. The other side of it: no knock control.
- **The trade-off:** peak torque comes later (245 Nm at 4,700 rpm) and the engine feels softer in everyday driving.

## M50TU: VANOS arrives

Built 1992–1996. A **VANOS unit** on the front of the cylinder head varies the intake camshaft timing, by up to **12.5°** (Bentley), giving **250 Nm at 4,200 rpm**.

- **Bosch DME M3.3.1** with **two knock sensors** and a Hall-effect camshaft sensor.
- **Internals change:** single valve springs, 6 mm valve stems and 140 mm rods, so **head and valvetrain parts are not interchangeable** with the non-VANOS engine.
- The VANOS piston seals age and need resealing: see the [M50TU VANOS guide](/guides/m50tu-vanos-guide).

## M52: the aluminium generation

Built 1995–2000, in the E36 323i/328i from 1996 (OBD2).

- **Block:** aluminium in most markets. The early **Nikasil** bores wore prematurely on high-sulphur fuel; **iron sleeves** followed from 1998. Original US and Canadian cars kept a **cast-iron** block (except the Z3).
- **Siemens MS41.1** with OBD2, and single VANOS.
- **M52B28:** 193 PS and 280 Nm, at 3,950 rpm. The most torque of the three for a naturally aspirated road car.
- **Buying in Europe:** know which bore surface the block has. Compression and leak-down tests tell you its condition. See the [M52 rebuild guide](/guides/bmw-m52-engine-rebuild-guide).

The later **M52TU** (1998 on) has double VANOS and different electronics: a different engine for swap purposes. See the [double VANOS guide](/guides/bmw-e36-m52-double-vanos-guide).

---

## Which one for which build?

| Goal | Engine | Why |
|---|---|---|
| Simplest swap into an OBD1 car | M50 non-VANOS | No VANOS; OBD1 like the car |
| Best everyday response on OBD1 | M50TU | VANOS torque; knock control |
| Most NA torque, OBD2 car | M52B28 | 2.8 litres, 280 Nm |
| High-rpm or boosted build | M50 non-VANOS internals are popular | Double springs, 7 mm stems, but no knock sensors: plan the engine management accordingly |

---

## Identifying an engine

1. **Front of the cylinder head:** a **VANOS unit** at the front means M50TU or M52; no VANOS unit means the non-VANOS M50.
2. **Block:** a magnet sticks firmly to cast iron, not to aluminium. An aluminium block means a non-US M52.
3. **DME label:** Bosch M3.1 = non-VANOS M50; Bosch M3.3.1 = M50TU (or US S50); Siemens MS41.1 = M52.
4. **Engine code** stamped on the block confirms it.

---

*This guide is part of the Projekt 36 M50 Engine series. Our build uses the M50B25 Non-VANOS in an E36 316i sedan swap.*

*→ Related: [M43 to M50 parts list](/guides/m43-to-m50-complete-parts-list) | [M50 torque specifications](/guides/e36-m50-torque-specifications) | [Cooling system overhaul](/guides/e36-cooling-system-overhaul)*
