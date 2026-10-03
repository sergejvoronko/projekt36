---
title: "BMW E36 Charging System, Diagnosis from Scratch"
description: "Diagnosing an E36 charging fault in the right order with the Bentley test values: battery state, regulated voltage, the D+ warning-light circuit, regulator brushes and parasitic drain."
pillar: reference
keywords: "bmw e36 alternator, e36 charging fault, e36 battery light, e36 bosch alternator, e36 voltage regulator"
date: "2026-04-13"
hero: "charging.webp"
reviewed: "2026-10-03"
sources:
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998, 121 Battery, Starter, Alternator"
---

## TL;DR

The expensive mistake with an E36 charging fault is replacing the alternator when the real problem is a dead battery, a bad ground, a slipping belt or worn regulator brushes. Test in order from cheapest to most expensive. Bentley's figures: a healthy system regulates at **13.5–14.5 V**, and more than **14.8 V** points at the voltage regulator.

---

## How the system fits together

- The **alternator** is belt-driven. Its **voltage regulator**, which carries the brushes, bolts onto the back of the alternator and can be replaced on its own.
- Terminal **B+** at the back of the alternator is connected directly to the battery.
- Terminal **D+** gets battery voltage **through the charge warning bulb** when the ignition is on or the engine is running. That small current excites the alternator. If the bulb circuit is broken, the alternator may not start charging.
- On the E36 the **battery is in the boot**, on the right-hand side.

So the warning light does two jobs: it tells you whether the alternator is producing current, and it is part of the excitation circuit. That is why Bentley's first check is the bulb.

---

## Diagnostic order

### 1. Belt, cables and grounds

- **Drive belt:** check its condition and that the automatic tensioner holds it properly. A slipping belt can make the warning light flicker at idle.
- **Battery cables:** clean and tight at both ends.
- **Grounds:** check the cable from the battery negative terminal to the body, and the ground strap from the engine to the body.

### 2. Battery state of charge

Load the battery with about 15 A for one minute (headlights on, engine off). Then disconnect the negative cable and measure the **open-circuit voltage** with a digital voltmeter:

| Open-circuit voltage | State of charge |
|---|---|
| 12.6 V or more | Fully charged |
| 12.4 V | 75 % |
| 12.2 V | 50 % |
| 12.0 V | 25 % |
| 11.7 V or less | Discharged |

Below 12.4 V, recharge the battery and test again before blaming the alternator. If the voltage is fine but the battery still won't start the car, have it **load tested**. Under a 200 A load for 15 seconds it must stay above **9.6 V at 27 °C** (9.3 V at 4 °C, 8.5 V at −18 °C).

Charge at **6 A or less**, never above 16.5 V at the battery, and keep sparks and flames away: the gas is explosive.

### 3. Charging system check

1. **Ignition on, engine off:** the charge warning light must come on. If it doesn't, fix the bulb or its wiring first; otherwise the alternator may not excite.
2. **At the back of the alternator:** check for battery voltage between B+ and ground. With the ignition on, check for voltage between D+ and ground. If either is missing, the fault is in the wiring.
3. **Engine running:** measure at the battery. **13.5–14.5 V** is normal. **Above 14.8 V** means the regulator is most likely faulty.
4. **Output under load:** ideally with a load tester. Without one, run the engine at about **2,000 rpm** and switch on every big load: lights, fans, rear window heater, wipers. Battery voltage should stay **above 12.0 V**.

**Never disconnect the battery with the engine running.** It can damage the alternator and the engine electronics.

### 4. Regulator and brushes

The regulator comes off the back of the alternator with a few screws. Check the **brush protrusion: minimum 5 mm**. Clean the brush contact surfaces and check the slip rings for wear. BMW doesn't sell the brushes separately, but aftermarket brushes exist and are soldered in. A complete aftermarket regulator is the simpler fix.

### 5. The alternator itself

If the wiring, battery, belt and regulator are all good and output is still low, the alternator is the likely culprit. Many parts suppliers can bench-test it, including the rectifier diodes. A replacement should have **the same rating as the original**; the maker and ampere rating are marked on the housing.

---

## Battery goes flat when parked

That is a parasitic drain, not a charging fault. To measure it:

1. Switch everything off and close the doors.
2. Connect a digital ammeter between the battery negative post and the negative cable.
3. Wait at least one minute for the reading to settle.

Bentley's figures: **0–100 mA** is normal, depending on how many systems need constant power; **400 mA or more** points to a problem. To find it, pull fuses one at a time until the current drops; that circuit holds the drain.

---

## Torque values (Bentley)

| Fastener | Torque |
|---|---|
| D+ wire to alternator (M6 nut) | 7 Nm |
| B+ wire to alternator (M8 nut) | 13 Nm |
| Alternator pulley (M16 nut) | 60 Nm |
| Alternator to bracket | 43 Nm |

To remove the six-cylinder alternator, release the belt tensioner by prying off its cover and levering it **clockwise**. Mark the belt's direction of rotation if you are going to reuse it.

---

## After an M43 → M50 swap

The M50 uses its own alternator, bracket and belt drive, so fit them as a set from the donor engine. Check that the B+ cable reaches the alternator and that the **D+ wire** from the warning-light circuit is connected to it. Make sure the engine-to-body ground strap is fitted and tight. Measure the charging voltage on the very first start.
