---
title: "BMW M50 Oil System Guide: Pump, Sump, Pickup Tube, and Pressure Diagnosis"
description: "A complete technical breakdown of the M50 oil system covering pump replacement, sump and pickup tube selection, and low oil pressure diagnosis. Written for E36 builders and M50 swap owners who need real specs, part numbers, and pricing."
pillar: engine
keywords: "BMW M50 oil pressure, M50 oil pump replacement, E36 low oil pressure diagnosis"
date: "2026-05-04"
hero: "e36-m50-oil-system-guide.webp"
---

## TL;DR

- **What:** Full guide to the M50 oil system — pump, sump, pickup tube, pressure specs, and fault diagnosis
- **Why:** Low oil pressure on the M50 is a common and engine-destroying problem if ignored; most cases trace back to a worn pump or collapsed pickup tube
- **Cost:** €40–€220 depending on pump brand and whether you're replacing the sump
- **Time:** 3–5 hours with the engine in the car; shorter on a bench
- **Difficulty:** 3/5

---

## How the M50 oil system works

The M50 (and its VANOS-equipped sibling, the M50B25TU/M50B20TU) uses a conventional gear-type oil pump driven off the front of the crankshaft. Oil is drawn from the sump through a pickup tube with a mesh strainer, pushed through the pump, past the oil pressure relief valve, through the filter, and then distributed to the main and rod bearings, camshaft journals, and — on TU variants — the VANOS solenoid system.

The system is deceptively simple, but a few weak points make it worth understanding in detail:

1. **The pickup tube O-ring** dries out and cracks with age, allowing the pump to draw air instead of oil under load.
2. **The pump itself** wears on high-mileage engines (200,000+ km), especially if oil changes were infrequent.
3. **The oil pressure relief valve** can stick open on neglected engines, causing chronically low pressure even with a new pump.
4. **Sump baffling** is marginal from the factory — relevant for any car that sees track or aggressive road use.

---

## Oil pressure specs and what "low" actually means

Before condemning a pump, verify actual pressure with a mechanical gauge. The M50's idiot light triggers at around **0.3 bar**, which is dangerously low. The sensor threads into the block at the front-left (M10×1.0), and a mechanical gauge adapter fits the same port.

| Condition | Minimum Acceptable Pressure |
|---|---|
| Hot idle (90°C oil temp, 900 RPM) | 1.5 bar |
| Cruising (2,500 RPM, hot) | 3.0–4.5 bar |
| High RPM (6,000+ RPM) | 5.0–6.5 bar |
| Cold start (ambient temp) | Up to 7.5 bar (relief valve opens) |

On a 25-year-old E36 that's been running 15W-40 since the factory fill, seeing 1.0–1.2 bar at hot idle is not unusual — and it means the bottom end is on borrowed time. Don't add thicker oil as a fix. Replace the pump and inspect the pickup tube first.

**Symptom checklist for low oil pressure:**
- Oil pressure warning light flickering at idle when hot
- Pressure light on during hard cornering (pickup uncovering — check sump baffling)
- Ticking from the top end at startup that clears slowly (VANOS or camshaft journals starved)
- Knocking at idle when hot (main or rod bearings worn, compounding the pressure loss)

---

## Oil pump: part numbers, brands, and what to buy

The M50B20 and M50B25 share the same oil pump housing, driven via the crankshaft nose — no separate drive shaft. The pump is accessible after removing the front timing cover.

**BMW OEM Pump**
- Part number: **11 41 1 742 993** (fits M50B20, M50B25, M50B25TU, M50B20TU)
- Supplier price (Germany/Austria): **€115–€145** (ECS Tuning DE, Schmiedmann, or local BMW dealer)

**Aftermarket Options**

| Brand | Part Number | Price (€) | Notes |
|---|---|---|---|
| Febi Bilstein | 24415 | €42–€55 | Budget option, acceptable for street use |
| Glyco / Federal-Mogul | — | €65–€85 | OE-quality, used by independent workshops |
| Wahler / ITM | — | €50–€70 | Common in Eastern European market |
| BMW OEM (Genuine) | 11 41 1 742 993 | €115–€145 | Recommended for any performance or track use |

For a street M50 with 200,000 km, Febi or Glyco is a reasonable choice. For an M50 swap build running the engine hard, spend the extra €60 and fit the genuine BMW pump. The tolerances matter when you're at 6,500 RPM on track.

**Installation note:** Always replace the pump O-ring (BMW 11 41 1 744 001, ~€3) and the front main seal while the cover is off. There is no reason not to.

---

## Pickup tube and o-ring: the most overlooked failure point

The pickup tube on the M50 runs from the oil pump body down into the sump and terminates in a mesh strainer. It seals to the pump body via a rubber O-ring — **BMW part 11 41 1 716 344**, roughly **€4–€8**.

This O-ring is the single most common cause of intermittent low oil pressure on M50 engines over 150,000 km. When it fails partially, the pump draws a mixture of air and oil under high-demand conditions (hard acceleration, high RPM), and pressure drops dramatically. The engine may show normal pressure at idle and in light cruising, making it easy to misdiagnose as a worn pump.

**How to check it without removing the pump:**
1. Drop the sump (see below).
2. Wiggle the pickup tube. Any movement at the pump body indicates O-ring failure or complete seal loss.
3. Inspect the O-ring visually — cracking, flattening, or hardening means replace it.

The pickup tube itself (BMW 11 41 1 716 343, ~€25–€35 OEM) rarely needs replacing unless it's physically damaged or the strainer mesh is clogged with sludge. If you find heavy sludge in the sump or on the strainer, the engine's service history is suspect — do a full inspection of bearing clearances before trusting it further.

---

## Sump options: OEM, baffled, and dry sump considerations

The stock M50 sump holds approximately **5.5 litres** with filter. It is an unmodified stamped-steel pan with no windage tray and minimal baffling. For most street applications this is fine. For track use or a dedicated M50 swap into a lightweight chassis, oil starvation during sustained cornering or hard braking is a real risk.

**Stock sump:**
- BMW 11 13 1 740 452 (M50B25) — ~€85–€110 OEM, or ~€35–€55 Febi/aftermarket
- Adequate for street use; replace the sump gasket (cork/rubber composite) whenever the pan is dropped

**Baffled sump upgrades:**

| Option | Price (€) | Notes |
|---|---|---|
| Mosselman Turbosystems baffled sump | €280–€340 | Best-known option, bolt-on, includes trap doors |
| Custom fabricated baffled pan (local fab shop) | €150–€250 | Variable quality; bring a template |
| Accusump accumulator system | €200–€350 | Stores pressurised oil; releases on pressure drop — works with stock sump |

In our M50 swap build running a B25TU in an E30 shell, we fitted the Mosselman baffled sump with an updated Febi pickup tube and OEM pump. Oil pressure at hot idle sits at 2.0 bar, and we've seen no pressure anomalies at Hockenheim GP through fast chicanes where the car pulls hard lateral G.

**Sump gasket:** Always replace with a new gasket (BMW 11 13 1 740 045 or Elring equivalent, ~€8–€15). Do not reuse the old one. Clean both mating surfaces thoroughly and use no additional sealant on the standard gasket.

---

## Oil pressure relief valve and filter housing checks

The pressure relief valve is integral to the oil pump body on most M50 units — it is not a separately serviceable item. If you're fitting a new pump, this is handled automatically. However, on the M50TU (VANOS variants), there is an additional **VANOS oil pressure control valve** integrated into the front of the cylinder head that can stick or fail, causing erratic VANOS behaviour and apparent oil pressure faults.

**Oil filter housing:**
The M50 uses a spin-off filter (BMW 11 42 1 726 372 or Mann W 940/25 equivalent, ~€6–€10). The filter housing itself can develop a weeping leak at the base gasket (BMW 11 42 1 718 519, ~€5). Replace this whenever you have the front of the engine apart. A leaking filter housing gasket drops external oil onto the block, generates the perpetual burning oil smell, and creates an apparent sump loss that's easy to misread as consumption.

Also check the oil pressure sender (BMW 12 61 1 730 081, ~€15–€25 Hella or Bosch equivalent). These fail regularly on E36-era engines and generate false low-pressure warnings. Substituting a mechanical gauge is always the correct first diagnostic step before replacing any components.

---

## What's next

If your M50 is showing low pressure at hot idle and you've confirmed it with a mechanical gauge, start with the pickup tube O-ring and sump inspection — it's a two-hour job and costs under €15. If that checks out, fit a new pump (budget for OEM if the engine is going to be worked hard) and replace the front main seal and timing cover O-rings while you're in there. For any car that will see track days or spirited mountain driving, a baffled sump is a worthwhile investment that eliminates one more variable.

For related reading, see our guides on M50 timing chain service and VANOS rebuild procedures, both of which share significant disassembly steps with the oil pump replacement outlined here.