---
title: "BMW E36 OBD1 Fault Codes, Complete Reference: Every Code, What It Means, and What to Check First"
seoTitle: "BMW E36 OBD1 Fault Codes: Full Reference List"
description: "Every BMW E36 OBD1 (1992-1995) DME blink code from the Bentley manual, what it means, what to check first, and how to read and erase codes with just the accelerator pedal."
pillar: reference
keywords: "BMW E36 OBD1 fault codes, E36 DME fault code list, BMW E36 diagnostic codes M50"
date: "2026-04-30"
hero: "e36-obd1-fault-code-reference.webp"
reviewed: "2026-10-03"
sources:
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998, 100 Engine–General, Table d: OBD I Fault (Blink) Codes"
---

## TL;DR

- **What:** The complete list of OBD1 fault codes for the E36's Bosch DME, from the Bentley manual, with what to check first for each.
- **Which cars:** **1992–1995** E36s use OBD1. From 1996 the cars use **OBD2**, which needs an OBD2 scan tool and uses completely different codes.
- **No tools needed to read them:** with the ignition on, press the accelerator pedal fully **five times within five seconds**, and the Check Engine light blinks the codes out.

---

## Reading the codes with the accelerator pedal

1. Turn the ignition **on** (engine off).
2. Press the accelerator pedal **fully to the floor five times within five seconds**.
3. The Check Engine light stays **on for 5 seconds**, goes off, then comes on for **2.5 seconds** and off again for 2.5 seconds. Then the codes start.
4. Each code is **four digits**, flashed as groups of blinks. Code 1221 is one blink, a pause, two blinks, a pause, two blinks, a pause, one blink. Codes are separated by a **2.5-second pause**.
5. After the last code there is a **0.5-second flash** and the light stays off.

To read them again, switch the ignition off and on, and repeat the five pedal presses.

### Erasing the memory

1. Read the codes until you get **1000** (a short blink, then the light stays off for a long time), meaning the end of the output.
2. Then hold the accelerator pedal **fully down for at least 10 seconds**.
3. Read the codes again and check for **1444**: no faults stored.

Fix the cause before erasing: a code that comes back proves the fault is still there.

---

## OBD1 fault codes (Bentley Table d)

"M3.3.1 only" codes exist only on the VANOS M50 (1993–1995). The 1992 non-VANOS M50 uses DME M3.1. See the [DME pinout reference](/guides/e36-dme-connector-pinout-reference) to tell them apart and to trace the wiring.

| Code | Meaning | What to check first |
|---|---|---|
| **1211** | DME control module | The module failed its self-test. Check the module's inputs (power, grounds) before suspecting the module itself. |
| **1215** | Mass air flow sensor | The air flow sensor and its wiring to the DME |
| **1216** | Throttle potentiometer | Throttle position sensor resistance and wiring |
| **1218** | Output stage, group 1 (M3.3.1 only) | DME inputs and outputs |
| **1219** | Output stage, group 2 (M3.3.1 only) | DME inputs and outputs |
| **1221** | Oxygen sensor 1 | The sensor's output signal to the DME |
| **1222** | Oxygen sensor lean/rich control limit | Intake air leaks, or causes of a rich mixture |
| **1223** | Coolant temperature sensor | Test the coolant temperature sensor |
| **1224** | Intake air temperature sensor | Test the intake air temperature sensor |
| **1225** | Knock sensor 1 (M3.3.1 only) | Knock sensor and its wiring |
| **1226** | Knock sensor 2 (M3.3.1 only) | Knock sensor and its wiring |
| **1231** | Battery voltage monitor | Battery voltage, charging system and starter |
| **1234** | Speed signal (M3.3.1 only) | Wiring between the instrument cluster and the DME |
| **1237** | A/C compressor cut-off (M3.3.1 only) | DME inputs and outputs to the A/C system |
| **1242** | A/C compressor signal (M3.3.1 only) | DME inputs and outputs to the A/C system |
| **1243** | Crankshaft position sensor (M3.3.1 only) | Crankshaft position / rpm sensor and its wiring to the DME |
| **1244** | Camshaft position sensor (M3.3.1 only) | Camshaft position sensor and its wiring to the DME |
| **1245** | Transmission control intervention (M3.3.1 only) | Wiring between the DME and the automatic transmission module |
| **1247** | Ignition secondary monitor (M3.3.1 only) | Secondary voltage to the ignition coils and the coil wiring |
| **1251** | Injector 1 (M3.1 and M3.3.1) | Injector operation and the signal reaching it |
| **1252** | Injector 2 | As above |
| **1253** | Injector 3 | As above |
| **1254** | Injector 4 | As above |
| **1255** | Injector 5 | As above |
| **1256** | Injector 6 | As above |
| **1261** | Fuel pump control | Fuel pump relay and the pump circuit |
| **1262** | Idle speed control | Idle control valve and its signal |
| **1263** | Evaporative (EVAP) system | The EVAP purge valve |
| **1264** | Oxygen sensor heater | Oxygen sensor heater and its relay |
| **1265** | Check Engine lamp (M3.3.1 only) | The bulb and its wiring |
| **1266** | VANOS (M3.3.1 only) | The VANOS solenoid and the signal to it. See the [M50TU VANOS guide](/guides/m50tu-vanos-guide) |
| **1267** | Air pump relay control (M3.3.1 only) | Air pump relay and wiring, where fitted |
| **1271** | Ignition coil 1 (M3.3.1 only) | The coil and its wiring |
| **1272** | Ignition coil 2 (M3.3.1 only) | As above |
| **1273** | Ignition coil 3 (M3.3.1 only) | As above |
| **1274** | Ignition coil 4 (M3.3.1 only) | As above |
| **1275** | Ignition coil 5 (M3.3.1 only) | As above |
| **1276** | Ignition coil 6 (M3.3.1 only) | As above |
| **1281** | DME memory supply (M3.3.1 only) | The constant battery supply to the DME |
| **1282** | Fault code memory (M3.3.1 only) | DME inputs and outputs; the module may be faulty |
| **1283** | Injector output stage (M3.3.1 only) | DME inputs and outputs; the module may be faulty |
| **1286** | Knock control test pulse (M3.3.1 only) | DME inputs and outputs; the module may be faulty |
| **1000** | End of code output | Nothing to fix: all stored codes have been shown |
| **1444** | No faults stored | Nothing to fix; this code must be present before the memory can be erased |

---

## Before chasing a code

Bentley's basic checks for any driveability fault, worth doing before replacing parts:

1. **Intake leaks:** cracked, loose or disconnected hoses and ducts, and loose clamps. Unmetered air causes lean running and sets the Check Engine light. A classic one is a split in the intake boot between the air flow sensor and the throttle body; a smoke test finds it quickly.
2. **Battery and grounds:** battery in good condition, cables tight and clean at both ends, ground points tight and corrosion-free, harness connectors undamaged. See the [ground distribution guide](/guides/e36-ground-distribution-guide).
3. **Power and ground at the DME,** including its main grounds.
4. **Fuses, and enough fuel in the tank.** After running out of fuel, pressure takes a moment to build again.
5. **Spark:** if the tachometer needle bounces while cranking, the ignition is probably working.

Idle speed, idle mixture and ignition timing **are not adjustable** on these engines. The DME adapts automatically within limits; when those limits are exceeded, it turns on the Check Engine light.

---

## Tools

The pedal method shows the stored codes. For **live data** (sensor values while the engine runs), you need a BMW-capable diagnostic tool connected to the round 20-pin diagnostic connector under the bonnet. See the [OBD1 diagnostic setup guide](/guides/e36-obd1-diagnostic-setup).

Standard OBD2 code readers don't work on OBD1 cars.
