---
title: "BMW E36 M43 to M50 Engine Conversion: The Complete Step-by-Step Guide"
description: "A comprehensive guide to swapping the M43 four-cylinder engine for the legendary M50 six-cylinder in your BMW E36. This article covers parts, wiring, cooling, and common pitfalls for a successful conversion."
pillar: swap
keywords: "M43 to M50 swap, E36 engine conversion, M50 swap guide, engine swap wiring, E36 cooling upgrade"
date: "2026-08-17"
hero: "bmw-e36-m43-to-m50-complete-engine-conversion-guide.webp"
---

The four-cylinder E36 models, the 316i and 318i, are lightweight, balanced, and plentiful. Their biggest drawback? The M43 engine. While reliable, its ~115 hp leaves much to be desired. The solution is one of the most classic and rewarding swaps in the E36 world: replacing the M43 with the iconic M50 inline-six.

This guide provides a comprehensive, no-nonsense walkthrough of the entire M43 to M50 conversion process. We'll cover sourcing the right donor package, mechanical installation, wiring, and the essential supporting upgrades you can't afford to skip.

## TL;DR

| Aspect | Summary |
| :--- | :--- |
| **What:** | Swapping the 1.6L/1.8L M43 4-cylinder for a 2.0L/2.5L M50 6-cylinder. |
| **Why:** | A massive power increase (from ~115 hp to 150-192 hp) and the legendary E36 inline-six soundtrack. |
| **Cost:** | €1,500 - €3,500, depending on donor engine condition and "while-you're-in-there" upgrades. |
| **Time:** | 40-60 hours. A packed weekend for an experienced mechanic, a week for the meticulous DIYer. |
| **Difficulty:** | 4/5. Requires solid mechanical skill, wiring competence, and patience for troubleshooting. |

## Sourcing Your Donor Package: The Heart of the Swap

The success of your swap hinges on sourcing a complete and healthy donor package. Your primary choice is between the M50B20 (from a 320i) and the M50B25 (from a 325i). While the swap process is nearly identical, the performance difference is significant.

| Engine | Displacement | Power (hp) | Torque (Nm) | Typical Cost (Used) |
| :--- | :--- | :--- | :--- | :--- |
| **M50B20** | 1991 cc | 150 | 190 | €400 - €700 |
| **M50B25** | 2494 cc | 192 | 245 | €700 - €1,200 |

For the effort involved, we strongly recommend holding out for an M50B25. The extra 42 hp and 55 Nm of torque completely transform the car.

Regardless of your choice, you need a *complete* package. Scouring scrapyards for individual parts will quickly become a logistical and financial nightmare. Aim to get all of the following from a single donor car:

*   **Complete Engine:** With intake and exhaust manifolds, alternator, power steering pump, starter, and all sensors.
*   **Engine Wiring Harness:** Uncut and in good condition.
*   **DME (ECU):** The correct one for the engine (e.g., Bosch Motronic M3.1 for the M50B25). Crucially, know if it has EWS (immobiliser).
*   **Transmission:** A Getrag 250G (common) or the stronger ZF 310G/320Z.
*   **Driveshaft:** From the corresponding 6-cylinder model. Your 4-cylinder shaft will not fit.
*   **Engine Mounting Arms:** Specific to the 6-cylinder E36 chassis.
*   **Full Exhaust System:** From the manifolds back to the muffler.
*   **Cooling System:** Radiator, expansion tank, fan shroud, and all hoses.
*   **Instrument Cluster:** A 6-cylinder cluster is needed for an accurate tachometer.

## Mechanical Installation: The Heavy Lifting

With the M43 removed, it's time to prepare the engine bay for its new heart. The core of the mechanical swap involves fitting the engine, transmission, and driveshaft.

### Engine Mounts and Arms

The M50 engine will not bolt to the M43's mounting points. You must use the cast aluminum engine mounting arms from a 6-cylinder E36.

*   **Left Engine Arm:** BMW `11811141137`
*   **Right Engine Arm:** BMW `11811141138`

While you're there, install new engine mounts. Aged rubber mounts will compromise the feel of your new engine.

| Mount Type | Part Number (Example) | Approx. Cost (Pair) | Notes |
| :--- | :--- | :--- | :--- |
| **OEM Rubber** | Lemförder `1052201` | €50 - €70 | Best for comfort and daily driving. |
| **Polyurethane** | Powerflex PFF5-306 | €90 - €120 | Stiffer, more engine feedback. Ideal for track/fast road use. |

### Transmission, Driveshaft, and Differential

The M50 bolts up to a 5-speed manual gearbox, typically the Getrag 250G found in the 320i and 325i. This is a direct fit. You will also need the corresponding 6-cylinder transmission cross-member (`22311141132`) and new gearbox mounts (`22316799331`).

Your 4-cylinder driveshaft is the wrong length. You must use a driveshaft from a manual 320i, 323i, 325i, or 328i. Ensure its center support bearing (`26121226723`) and flex disc (guibo, `26117511454`) are in good condition or replace them.

The stock differential from your 316i/318i (likely a 3.38 or 3.45 ratio) will technically work, but the gearing will be extremely short. You'll be hitting the rev limiter constantly. A highly recommended upgrade is to swap in a medium case (188mm) differential from a 325i, which has a much more suitable **3.15** final drive ratio.

## Wiring: Demystifying the X20 Connector

This is the most intimidating part of the swap for many, but it's straightforward if you're systematic. On E36s from ~1993 onwards, the engine harness connects to the main chassis harness at a large, round plug on the firewall called the **X20 connector**. Your job is to ensure the pins from the M50 engine harness correctly line up with the functions on your M43 chassis-side connector.

Fortunately, BMW kept the pin functions largely consistent. For most post-1994 cars, it's nearly plug-and-play. Below are the most critical pins you need to verify.

| X20 Pin | M50 Function | M43 Chassis Wire Colour | Notes |
| :--- | :--- | :--- | :--- |
| 1 | Alternator Charge Indicator | Blue | Should match directly. |
| 12 | Tachometer Signal | Black | Essential for a working rev counter. |
| 13 | Fuel Consumption Signal | White/Violet | For the MPG gauge. |
| 15 | Starter Signal | Black/Green | From ignition switch to starter solenoid. |
| 18 | Ignition Power (Run/Start) | Black/Yellow | Powers the DME when key is on. |
| 21 | DME Power (from Main Relay) | Green | Constant power supply for the DME. |
| 23 | Oil Pressure Switch | Brown/Green | For the oil pressure warning light. |
| 25 | Main Relay Power (Unswitched) | Red/White | Constant battery power. |

**The EWS Problem:** The biggest electrical hurdle is the factory immobiliser (EWS).
*   **Your Car:** An M43-powered E36 from 1995 or later will have EWS-II.
*   **Your Donor Engine:** An early M50 (pre-1995) may have no EWS or the simpler EWS-I.

You have three main solutions:
1.  **The "Red Label 413" DME:** The easiest path. Source a Bosch DME with part number `0 261 200 413`. This DME is from early M50B25TU engines and has no EWS. It's plug-and-play. Expect to pay €150 - €250 for this coveted piece.
2.  **Matched EWS Set:** Use the DME, EWS-II module, and the ignition key transponder chip from your donor car. This requires integrating the donor EWS module into your car's wiring. It's more complex but cheaper if the parts come with your engine.
3.  **EWS Delete Service:** Send your M50's DME to a specialist who can digitally remove the EWS function from its software. This service typically costs €100 - €150 and is a clean, reliable solution.

## Fuel, Cooling, and Exhaust Systems

With the engine in and wired up, you need to handle the supporting systems.

### Fuel System

The good news is that the stock M43 fuel pump provides sufficient flow and pressure for a standard M50. You don't need to upgrade it. You will, however, need to connect your chassis fuel lines (feed and return) to the M50 fuel rail. The connections are in a slightly different location. This can usually be accomplished by carefully bending the hard lines or using a short section of high-pressure, ethanol-safe fuel hose (8mm inner diameter) and proper fuel injection clamps.

### Cooling System: A Non-Negotiable Upgrade

The 4-cylinder radiator is completely inadequate for cooling a 6-cylinder engine. You *must* upgrade to the larger radiator from a 6-cylinder E36. Overheating is the fastest way to kill your new M50.

| Component | Recommended Part (New) | BMW Part Number | Approx. Cost (New) |
| :--- | :--- | :--- | :--- |
| Radiator | Behr/Hella 8MK376712-281 | `17111728907` | €120 - €180 |
| Expansion Tank | Meyle HD `3142230002` | `17111723520` | €40 - €70 |
| Water Pump | Graf PA539 (Metal Impeller) | `11517527799` | €50 - €70 |
| Thermostat | Wahler 4264.88D (88°C) | `11531740437` | €25 - €40 |
| Fan Clutch | Sachs `2100010031` | `11527505302` | €70 - €90 |
| Hose Kit | Full 6-cyl kit (e.g., Gates) | Varies (Kit) | €80 - €120 |

In our M50 swap build, we found that a complete cooling system overhaul is cheap insurance. On a 25-year-old E36, the plastic components are brittle and guaranteed to fail at the worst possible moment. Replace everything.

### Exhaust System

You need the entire exhaust system from a 320i or 325i. The dual-pipe M50 exhaust manifolds will not connect to the single-pipe M43 system. The entire system is a direct bolt-on to the E36 chassis, using the existing hanger locations. Sourcing a good-condition used system is the most economical route (€200 - €400).

## Final Steps: Brakes and Suspension

You've nearly doubled your car's horsepower and added about 60 kg over the front axle. Your stock M43 brakes and suspension are no longer up to the task.

**Brakes:** A 316i or 318i typically has small, solid front brake discs and often rear drum brakes. At a minimum, you must upgrade to the vented front discs and callipers from a 320i/325i. A full 325i brake conversion (front and rear) is highly recommended for safe, repeatable stopping power.

**Suspension:** The front springs from your M43 car are rated for a much lighter engine. With the M50 installed, the front end will sag, ruining the car's handling balance and causing poor ride quality. You must install front springs and dampers designed for a 6-cylinder E36. This is the perfect excuse to upgrade to a matched set of performance springs and shocks or a complete coilover kit from brands like Bilstein, H&R, or KW.

## What's Next?

Completing an M43 to M50 swap is a rite of passage for any serious E36 enthusiast. You've taken a modest chassis and given it the engine it always deserved. The result is a car that is dramatically faster, sounds incredible, and provides immense satisfaction every time you turn the key.

Take the time to shake down the car, fix any minor leaks or issues, and get a proper wheel alignment. Once settled, your new 325i-spec E36 is a fantastic platform for further modification, whether you're heading to the track or just enjoying a perfect back-road companion.