---
title: "BMW E36 M50 Manifold Conversion on M52/S52: Step-by-Step Installation and Vacuum Routing Guide"
description: "Unlock top-end horsepower on your M52 or S52 engine with a complete M50 intake manifold swap. This guide details the exact vacuum routing, required adapter hardware, and tuning adjustments needed for a clean OEM+ installation."
pillar: engine
keywords: "m50 manifold swap e36, m50 intake manifold on m52, e36 m52 intake manifold conversion"
date: "2026-09-25"
hero: "bmw-e36-m50-manifold-conversion-guide.webp"
---

## TL;DR

- **What:** Installing an OBD1 M50B25 intake manifold onto an OBD2 M52 (2.8L) or S52 (3.2L) engine.
- **Why:** Replaces the restrictive OBD2 manifold runners to unlock 15-25 whp above 5,000 RPM, completely changing the high-RPM character of the engine.
- **Cost:** €250 – €450 (Includes used M50 manifold, adapter kit, and fresh OEM gaskets).
- **Time:** 4–6 hours.
- **Difficulty:** 3/5 (Mechanical swap is simple; custom vacuum plumbing requires attention to detail to prevent idle issues).

## The Science Behind the Swap: M50 vs M52 Flow Characteristics

BMW's shift from the OBD1 M50 engine to the OBD2 M52 engine brought a drastic change in intake manifold philosophy. To comply with emissions and improve low-end drivability, BMW choked the M52 (and US-spec S52) with an intake manifold featuring runners that are significantly narrower than their M50 predecessors. 

The cross-sectional area of an M50 intake runner is roughly **400mm²**, while the M52 runner is restricted to **275mm²**. 

While the M52 manifold provides excellent port velocity at low RPMs (resulting in punchy low-end torque), it acts as a restrictor plate above 5,000 RPM. By swapping the M50B25 manifold (found on 1992-1995 325i/525i models) onto your 2.8L or 3.2L block, you dramatically shift the volumetric efficiency (VE) curve to the right. You will lose about 5-10 lb-ft of torque below 3,500 RPM, but in exchange, the engine will breathe freely all the way to a 7,000+ RPM redline, gaining up to 25 wheel horsepower in the process.

## Comprehensive Parts List and Conversion Hardware

While you *can* technically piece together plumbing from a hardware store to make this work, we heavily advise against it. The vacuum leaks inherent in a DIY "Home Depot plumbing" approach will cause erratic idles and lean codes. Buy a dedicated M50 manifold conversion kit (like those from M50Manifold.com, Turner, or Rabid Racing) that includes a CNC-machined throttle body adapter plate and molded silicone vacuum hoses.

Here is what you need for a reliable, OEM+ installation:

| Part / Component | BMW Part Number / Spec | Est. Price (EU) | Notes |
| :--- | :--- | :--- | :--- |
| **M50B25 Intake Manifold** | `11611738722` | €100 - €180 | Sourced used (eBay / local breakers). Avoid M50B20 manifolds; they have smaller runners. |
| **Intake Manifold Gaskets** | `11611740069` (x6) | €30 | Do not reuse old gaskets. Elring or Victor Reinz preferred. |
| **Throttle Body Gasket (M50)** | `11611716174` | €8 | Seals the adapter plate to the M50 manifold. |
| **Throttle Body Gasket (M52)** | `11611436631` | €8 | Seals the M52 throttle body to the adapter plate. |
| **Conversion Kit** | Varies by brand | €120 - €180 | Includes TB adapter plate, fuel rail brackets, CCV/ICV plumbing. |
| **Intake Air Temp (IAT) Adapter** | Custom / M12x1.5 Tap | €15 | M52 IAT is threaded; M50 hole is push-in. See below for modification. |
| **Vacuum Caps** | 3mm and 7mm | €5 | For capping unused vacuum ports on the rear of the manifold. |

## Adapting the Throttle Body and Fuel Rail

The physical bolt patterns between the M50 and M52 components do not match, requiring specific adaptations before the manifold ever enters the engine bay.

### 1. The Throttle Body Adapter
The M52 throttle body has an integrated sealing ring groove, whereas the M50 manifold uses a separate square-profile gasket. If you bolt an M52 throttle body directly to an M50 manifold, you *will* have a massive vacuum leak. 

Your conversion kit will include an aluminum adapter plate. The stack-up should go: **M50 Manifold -> M50 Gasket -> Adapter Plate -> M52 Gasket -> M52 Throttle Body**. Apply a very thin, almost translucent layer of sensor-safe RTV on the adapter plate faces just to guarantee a seal, though high-quality kits seal fine dry.

### 2. Fuel Rail Brackets
The mounting points for the fuel rail on the M50 manifold sit about 15mm lower and at a different angle compared to the M52. Attempting to force the M52 fuel rail down will cause the fuel injectors to seat at a crooked angle, leading to fuel leaks or unmetered air entering the runners. 

Use the flat-bar aluminum brackets provided in your kit to adapt the M52 rail mounting tabs to the M50 manifold posts. When reinstalling your injectors, this is the perfect time to replace the injector O-rings (`13537705604`). Lubricate the new O-rings with a dab of clean engine oil before pressing the rail into the manifold.

### 3. Modifying the IAT Sensor Bung
The OBD2 engine management (Siemens MS41) relies on a threaded Intake Air Temperature (IAT) sensor. The OBD1 manifold has a push-in style IAT port located on the underside of the plenum. You have two options here:
*   **Tap the manifold:** Drill the M50 IAT hole slightly and tap it to M12x1.5 to accept the M52 sensor directly. (Be sure to clean out all plastic shavings).
*   **Use an adapter:** Many high-end kits include a push-in delrin plug that is pre-threaded to M12x1.5. This snaps into the M50 manifold like an OBD1 sensor, and you thread your OBD2 sensor into it.

## The Nightmare Unraveled: Vacuum and CCV Routing

This is where 90% of M50 swaps fail. The M50 manifold was designed for a simpler idle control and crankcase ventilation system. The M52 uses a complex Cyclone Separator (CCV) system. Routing the OBD2 vacuum lines to the OBD1 manifold requires consolidating several ports.

Here is the exact routing breakdown when installing an M52 under an M50 manifold:

### The Rear Manifold Ports
On the rear (firewall side) of the M50 manifold, you will find one large port and two small nipple ports.
*   **Large Port (12mm):** This connects directly to the Brake Booster vacuum line. 
*   **Small Port 1 (3.5mm):** Route this to the Fuel Pressure Regulator (FPR) vacuum line (which runs under the car to the fuel rail on M52s).
*   **Small Port 2 (3.5mm):** If your car still has the Secondary Air Pump (SAP) vacuum solenoid, connect it here. If you have deleted the SAP, cap this port with a high-quality vacuum cap and secure it with a small zip tie.
*   *Note on the Exhaust Flap:* If you still have the factory rear muffler with the vacuum-actuated flap, you will need to T-in a line here. Most E36s running this mod have aftermarket exhausts, so the flap line can be deleted.

### The Underside Plenum Port (ICV & CCV)
The M50 manifold has a single large oval-ish port on the underside of the plenum, designed solely for the OBD1 Idle Control Valve (ICV). Your M52, however, needs to draw vacuum for *both* the ICV and the Cyclone Separator (CCV) from the manifold.

Conversion kits solve this by providing a customized silicone Y-hose or a machined aluminum distribution block that plugs securely into the bottom of the M50 manifold. 
1.  Push the distribution block / main silicone hose into the bottom of the M50 manifold. Ensure the internal retaining clip snaps into place, or it will blow out under backfire.
2.  Route the primary branch to the M52 Idle Control Valve.
3.  Route the secondary branch to the top port of the M52 CCV (Cyclone Separator). 
4.  Ensure the oil drain line from the bottom of the CCV to the dipstick tube is intact and uncracked. (If it's original, replace it now).

*Mechanic's Tip:* On a 25-year-old E36, the plastic CCV housing and its ribbed hoses are extremely brittle. We highly recommend replacing the entire CCV unit (`11151703484`) and the valve cover breather hose (`11151703775`) while the manifold is off. It adds about €60 to the build but saves you from having to pull the manifold again next month.

## Installation and Post-Swap Verification

When physically lowering the assembled M50 manifold onto the engine, take extreme care not to pinch the starter wiring harness or the ICV hose against the engine block. The manifold should sit completely flush against the cylinder head without resistance. If you have to force it, something is trapped underneath. 

Torque the 11mm manifold nuts to **15 Nm (11 lb-ft)**, starting from the center and working your way outward in a crisscross pattern. Over-torquing will crack the plastic flange.

### Mandatory Smoke Testing
Before starting the car, a smoke test is virtually mandatory. Hook a smoke machine up to the intake boot. If you see smoke escaping from under the fuel rail, the adapter plate, or the bottom of the plenum, stop and fix it. An M52 will flat-out refuse to idle correctly if there is even a pinhole leak post-MAF.

## Engine Management and Tuning Requirements

Can you run an M50 manifold on the stock MS41.1 (or MS41.2) ECU tune? Yes. The MAF will read the increased airflow and add fuel accordingly, and the engine will adapt via long-term fuel trims.

*Should* you run it untuned? Absolutely not. 

Running the stock tune leaves at least half the horsepower gains on the table. The factory M52 ignition timing maps are optimized for the torque peak of the narrow-runner manifold. By flashing a dedicated M50 manifold tune (via specialized tuners using tools like RomRaider or MS41 QuickFlash), you achieve three vital things:

1.  **Fuel and Timing Optimization:** The tuner adjusts the VE tables and advances ignition timing past 5,000 RPM, where the new manifold flows best.
2.  **Rev Limiter Increase:** The factory 6,500 RPM redline cuts the fun short right as the M50 manifold is peaking. A proper tune raises the limit to 7,000 RPM (for M52B28) or 7,200 RPM (for S52s with upgraded valve springs), allowing you to utilize the extended powerband.
3.  **Idle Adjustment:** Some tuners will slightly raise the target idle speed (from ~700 to ~800 RPM) to compensate for the larger plenum volume, preventing any minor idle dips when coming to a stop.

## What's Next?

With the M50 manifold swap complete, your M52 or S52 has shed its biggest factory bottleneck. To fully exploit the new high-RPM breathing capability, your next focus should be on the exhaust side. Upgrading to S52/M3 tubular exhaust manifolds (if you have an M52) or fitting a high-flow midsection will ensure the air you're now efficiently pulling in can escape just as quickly.