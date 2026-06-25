---
title: "BMW E36 M50/M52 to S50/S52 Engine Swap: The Definitive Guide"
description: "A complete technical guide for swapping a US-spec S50 or S52 M3 engine into a non-M BMW E36. This article covers part selection, wiring, mechanical installation, and common pitfalls for the experienced DIYer."
pillar: swap
keywords: "E36 S50 swap, E36 S52 swap, M50 to S50 conversion, M52 to S52 conversion, BMW E36 engine swap, S50/S52 wiring, E36 S50 parts list, E36 S52 cooling adaptation"
date: "2026-06-12"
hero: "e36-m50-m52-s50-s52-engine-swap-guide.webp"
---

The US-spec E36 M3 engine is, at its core, a factory-stroked and refined version of the M50/M52 engine found in the 325i and 328i. This shared architecture makes swapping an S50 or S52 into a non-M E36 one of the most popular, cost-effective, and reliable OEM+ power upgrades available. This guide covers the process for a successful swap.

## TL;DR

| Aspect | Summary |
| :--- | :--- |
| **What:** | Swapping a standard E36 M50/M52 for a US-spec S50B30 or S52B32 M3 engine. |
| **Why:** | A reliable, OEM+ power increase from ~190 hp to 240 hp with significant torque gains. |
| **Cost:** | €2,500 - €5,500, depending heavily on the condition and source of the donor engine. |
| **Time:** | 25-40 hours for an experienced home mechanic with parts on hand. |
| **Difficulty:** | 4/5 - Mechanically straightforward, but wiring and component matching require precision. |

---

## Engine selection: S50B30US vs. S52B32US

Your first major decision is choosing between the S50 from the '95 M3 and the S52 from the '96-'99 M3. Both are based on the M50/M52 block and are far simpler to swap than their European counterparts (S50B30/B32). The primary difference is the OBD (On-Board Diagnostics) system they were designed for.

| Feature | S50B30US (1995) | S52B32US (1996-1999) | Notes |
| :--- | :--- | :--- | :--- |
| **Displacement** | 3.0L (2990cc) | 3.2L (3152cc) | S52 has more stroke, resulting in better low-end torque. |
| **Power/Torque** | 240 hp / 305 Nm | 240 hp / 320 Nm | Peak power is identical, but the S52's powerband is broader. |
| **Electronics** | OBD-I | OBD-II | This is the most critical difference affecting the swap. |
| **VANOS** | Single VANOS (M50-based) | Single VANOS (M52-based) | S50 VANOS is generally considered more robust. |
| **Intake Manifold** | High-flow, equal-length runners | Restrictive, lower-cost design | The S50's manifold is a popular upgrade for the S52. |
| **Typical Cost**| €1,500 - €2,500 (used) | €2,000 - €3,500 (used) | S52s are newer and generally command a higher price. |

**Recommendation:**
*   **For an M50-powered car (e.g., 325i):** The S50B30US is a nearly direct, plug-and-play swap. You use the S50 engine harness and the corresponding "Red Label 413" DME.
*   **For an M52-powered car (e.g., 328i):** The S52B32US is the more straightforward choice. It retains your car's native OBD-II system.
*   **The Hybrid (S52 into an M50 car):** This is a very common and effective route. It involves converting the S52 to run on OBD-I electronics, leveraging the M50's simpler, more tuner-friendly system. This is often the best of both worlds: the larger displacement of the S52 with the simplicity of OBD-I.

When sourcing an engine, insist on a compression and leak-down test. A healthy engine should show 180-210 PSI across all cylinders with minimal variation.

## Pre-Installation prep: the "while you're in there" list

An engine on a stand is the easiest engine to work on. Resist the urge to drop it straight in. Addressing these key maintenance items now will save you immense frustration later. On a 25-year-old engine, these are not optional.

| Part | BMW Part Number | Aftermarket Option | Est. Price (€) | Why It's Critical |
| :--- | :--- | :--- | :--- | :--- |
| **Oil Pan Gasket** | 11131437237 | Elring / Victor Reinz | €25 | Guaranteed to leak if you don't replace it. |
| **Rear Main Seal** | 11142249533 | Corteco / Elring | €20 | Prevents oil leaks between engine and transmission. |
| **VANOS Seals** | N/A | Beisan Systems (BS012) | €60 | Restores lost torque and cures the infamous VANOS rattle. |
| **Water Pump** | 11517527799 | Graf / Hepu (metal impeller) | €50 | The original plastic impeller is a notorious failure point. |
| **Thermostat** | 11537511580 (88°C) | Wahler / Mahle | €25 | Replace with the housing (11531722531). |
| **Engine Mounts** | 11812228288/289 | Lemförder / Vibra-Technics | €100-250 | Use E36 M3 specific mounts for proper fitment. |
| **Coolant Hoses** | Kit | Gates / Rein | €120 | Old rubber is a liability. Replace every single hose. |
| **Oil Filter Housing Gasket** | 11421719855 | OEM or Elring | €10 | Common source of major oil leaks onto the belts. |

In our S52 swap build, we also opted to replace the crank position sensor, cam position sensor, and both knock sensors while access was easy. It's cheap insurance against chasing frustrating sensor-related issues post-swap.

## Wiring & DME: the heart of the swap

This is where planning is paramount. Your approach depends entirely on your chassis and donor engine combination.

#### Scenario 1: S50 (obd-i) into M50 chassis (obd-i)
This is the simplest path.
*   **Engine Harness:** Use the complete S50 engine harness. It's physically identical to the M50 harness but pinned for the S50's requirements.
*   **DME:** Use the Bosch DME ending in "413", commonly known as the "Red Label". Part number **12141466000** (Bosch **0 261 200 413**). It's a direct plug-in to your car's body harness.
*   **Sensors:** All sensors are native to the S50 and will work directly. No adaptation is needed.

#### Scenario 2: S52 (obd-ii) into M52 chassis (obd-ii)
This is also straightforward, with one key hurdle.
*   **Engine Harness:** Use the S52 engine harness.
*   **DME:** Use the S52's Siemens MS41.1 DME.
*   **EWS (Immobilizer):** This is the main challenge. The DME, EWS module, and key transponder from the donor car are all paired. You must either:
    1.  Get all three components (DME, EWS box, key chip) from the donor car.
    2.  Have the S52 DME's EWS function "deleted" or aligned to your existing EWS module by a specialist tuner. An EWS delete is often the cleanest solution.

#### Scenario 3: S52 (obd-ii) into M50 chassis (obd-i)
The "OBD-I Conversion" is the enthusiast's choice. You get the bigger S52 engine but run it on the simpler and more easily tunable OBD-I electronics from your original M50.

You will use your original M50 engine harness and adapt it to the S52 engine.

| Component | M50 (OBD-I) Version | S52 (OBD-II) Version | Action Required |
| :--- | :--- | :--- | :--- |
| **Crank Position Sensor** | Mounts on front timing cover | Mounts in the block, reads flywheel | Use the M50 sensor, no change needed. |
| **Cam Position Sensor** | M50-style Siemens sensor | S52-style Siemens sensor | Splice the S52 sensor connector onto your M50 harness. |
| **Knock Sensors** | 2x M50 sensors | 2x S52 sensors | Use S52 sensors. Splice their connectors onto the M50 harness. |
| **Injectors** | High-impedance (e.g., 17#) | High-impedance (21.5# Pink Top) | Use the S52 injectors. They are plug-and-play. |
| **MAF Sensor** | 3" M50 MAF | 3.5" S52/M3 MAF | Use the S52 MAF (**13621747155**) and a tune to scale it. |
| **Throttle Body** | Single-connector TPS | Dual-connector TPS/ASC | Use the S52 throttle body but wire only the primary TPS signal. |
| **DME** | Bosch "413" DME | N/A | Use the M50's 413 DME, but it **must** be custom-tuned for the S52's displacement, injectors, and MAF. A stock 413 tune will run the engine poorly and dangerously lean.

Specialists like TRM, RK-Tunes, or Turner Motorsport offer proven off-the-shelf chips or remote tuning for this exact conversion. Budget around €300-€500 for a proper tune.

## Supporting systems: drivetrain, exhaust, and cooling

Getting the engine in and running is only half the battle. These supporting systems are critical for putting the power down reliably.

#### Drivetrain
Your 325i's Getrag 250G transmission will bolt up, but it's the weak link. The ZF 320Z 5-speed from a 328i or M3 is the correct, robust choice.
*   **Transmission:** ZF S5D 320 Z
*   **Clutch & Flywheel:** Use the complete E36 M3 clutch kit and flywheel. A stock Sachs kit (**21212228289**) is excellent for up to 300 hp.
*   **Driveshaft:** You will need the driveshaft from the car that donated the transmission (e.g., a 328i or M3 driveshaft for a ZF swap).
*   **Differential:** Your stock diff will work, but for best performance, an M3 Limited Slip Differential (LSD) is the ultimate goal. A 3.15 or 3.23 final drive ratio is the sweet spot for a 5-speed S50/S52.

#### Exhaust
You must use M3 exhaust manifolds, as the standard M50/M52 manifolds are highly restrictive and will choke the new engine.
*   **Manifolds:** S50/S52 manifolds are identical. They are a direct fit.
*   **Mid-pipe:** An M3 mid-pipe is the easiest solution. If you're doing an OBD-I conversion, you can use a catalyst-free Euro M3 or aftermarket mid-pipe. For OBD-II cars, you'll need a catted M3 section to keep the post-cat O2 sensors happy.

#### Intake & cooling
*   **M50 Manifold Swap:** If you have an S52, the single most effective power upgrade is swapping its restrictive intake manifold for one from an M50 or S50. This is worth 15-20 hp at the top end. Kits are available from vendors like M50manifold.com to adapt the fuel rail and vacuum lines. Part number for the M50 manifold is **11611735728**.
*   **Cooling System:** The stock 325i/328i radiator is adequate for street use. However, for track days or spirited driving in hot climates, an E36 M3 radiator (**17112227281**) or a quality aluminum upgrade (e.g., Mishimoto) is highly recommended. Ensure you bleed the cooling system properly using the bleed screw on the thermostat housing — air pockets are the enemy of these engines.

## What's next?

The stock 325i/328i brakes are marginal for this kind of power — E36 M3 brakes are the immediate next step. After that, look at suspension: coilovers and reinforced subframe mounts let you actually use what the engine is producing.