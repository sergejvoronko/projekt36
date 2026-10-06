---
title: "BMW M50 Common Failure Points & How to Prevent Them"
description: "Where an old BMW M50 actually fails, how each problem shows itself, and what to replace during a rebuild or swap, checked against the Bentley manual."
pillar: engine
keywords: "m50 reliability, m50 problems, m50 common issues, bmw m50 failure points, m50 engine problems"
date: "2026-03-16"
hero: "m50-failures.webp"
reviewed: "2026-10-06"
sources:
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998 (cooling, timing chains, VANOS, head gasket, idle control, air flow sensor, maintenance)"
---

## TL;DR

The M50 is a durable engine; what lets it down on a 30-year-old car is the **ageing around it**. In rough order of how often it bites:

1. **the cooling system**, mostly plastic parts and old hoses;
2. **oil leaks** from hardened gaskets and seals;
3. **timing chain** tensioners and guides;
4. on VANOS engines, the **VANOS piston seals**;
5. **idle control and air flow problems**.

The head gasket rarely fails on its own; it fails after overheating. Prevent the first problem and you prevent the worst one.

---

## 1. Cooling system

**What fails:** the plastic expansion tank and radiator tanks crack, the thermostat sticks, hoses perish. Old water pumps with plastic impellers are a known weak point. Bentley recommends replacing the cooling hoses **every four years** as a preventive measure.

**Symptoms:** the temperature gauge reading higher than usual, coolant smell, residue on the tank seams, a falling coolant level, or steam (by then the damage may be done).

**Prevention:** replace the water pump (metal impeller), thermostat, expansion tank and cap, hoses and clamps, and the radiator if it's old. Pressure-test the system: it should hold within **0.1 bar for two minutes**. Full details: [cooling system overhaul](/guides/e36-cooling-system-overhaul).

---

## 2. Oil leaks

**What fails:** after decades of heat, gaskets and seals harden and shrink. The usual spots:

- **cylinder head cover** gasket: oil onto the hot exhaust side means smoke and smell
- **oil filter housing** gasket
- **oil pan** gasket
- **front crankshaft seal** in the lower timing cover
- **rear main seal**: oil here can contaminate the clutch
- **camshaft sensor O-ring** (VANOS engines): Bentley calls for a new O-ring whenever the sensor is removed
- **VANOS oil line** (VANOS engines): new sealing washers whenever it's undone

**Prevention:** with the engine out, reseal it completely. In the car, start with the cylinder head cover and oil filter housing gaskets.

---

## 3. Timing chains, guides and tensioners

The six-cylinder uses **two chains** (primary and secondary), each with a **hydraulic tensioner**. Bentley: a worn chain and sprockets cause noise and erratic valve timing, and a faulty tensioner can also cause chain noise.

**Symptoms:** rattle from the front of the engine, especially at start-up; persistent rattle when warm; pieces of plastic guide in the oil pan.

**Prevention:** inspect during any major work, and replace the tensioners and guides if in doubt. Chain removal on the six-cylinder means taking the **oil pan** off and using the BMW **locking tools**. See the [timing chain guide](/guides/e36-m50-timing-chain-guide).

---

## 4. VANOS seals (M50TU only)

This doesn't apply to the non-VANOS M50 (built up to 8/1992).

**What fails:** the VANOS piston's O-ring hardens and the piston can't hold oil pressure, so the intake camshaft doesn't advance fully.

**Symptoms:** flat response at lower revs, rough idle, a stored VANOS fault.

**Fix:** reseal the unit with an aftermarket kit. See the [M50TU VANOS guide](/guides/m50tu-vanos-guide) for the BMW test, which needs at least 8.5 mm of travel, and the repair.

---

## 5. Head gasket: a consequence, not a cause

Head gaskets on these engines usually fail after an **overheating** event. Signs: white exhaust smoke that doesn't clear, coolant loss with no visible leak, milky residue under the oil cap, combustion gas in the coolant. Confirm with a block (combustion leak) tester and a compression test. Repair: [head gasket guide](/guides/e36-m50-head-gasket-replacement).

---

## 6. Idle control valve

**What fails:** deposits make the valve stick or respond slowly; its coils can also fail.

**Symptoms:** hunting or unstable idle, stalling when coming to a stop, idle too high.

**Checks (Bentley):** with the engine running the valve should **buzz**; switching on the A/C or selecting Drive should keep the idle steady or raise it slightly. Coil resistance on the M50: **20 ± 5 Ω** across terminals 1–2 and 2–3, **40 ± 5 Ω** across 1–3. These electrical checks don't prove the valve moves freely: a known-good substitute is the surest test. After a new valve, the idle may be poor for about 10 minutes of driving while the DME adapts.

---

## 7. Air flow meter

**What fails:** the sensing element gets contaminated or fails; the meter can't be adjusted or repaired. If it fails completely, the DME switches to limp-home mode.

**Symptoms:** hesitation, poor running, mixture faults.

**Checks:** on the 1992 M50's hot-wire meter, the wire should glow about four seconds after a 2,500 rpm shutdown (the burn-off). Rule out **air leaks** after the meter before blaming it. See the [sensor values guide](/guides/e36-obd1-live-data-sensor-reference).

---

## Before installation (engine out, e.g. a swap)

- full reseal: all gaskets and seals
- complete cooling system
- timing chains, guides and tensioners inspected, and replaced if in doubt
- spark plugs (tightened to 23–25 Nm)
- idle control valve checked
- drive belt and tensioner
- clutch and flywheel if their history is unknown

**No valve adjustment needed:** the M50 has **hydraulic lifters**, non-VANOS and VANOS alike.

---

## Maintenance after installation

Follow BMW's service schedule for your car as a minimum. On an old engine of unknown history, shorter oil change intervals and a coolant change every two years are cheap insurance.

---

*This guide is part of the Projekt 36 M50 Engine series. Our M50B25 NV is getting a complete reseal and preventive replacement of all wear items before installation.*

*→ Related: [M50 vs M50TU vs M52 Comparison](/guides/m50-vs-m50tu-vs-m52-comparison) | [Cooling System Overhaul](/guides/e36-cooling-system-overhaul) | [M50 Torque Specifications](/guides/e36-m50-torque-specifications)*
