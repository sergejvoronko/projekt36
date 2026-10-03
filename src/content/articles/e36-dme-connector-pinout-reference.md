---
title: "BMW E36 M50 DME Pinout Reference: Bosch M3.1 and M3.3.1 ECM Connector"
seoTitle: "BMW E36 M50 DME Pinout: Bosch M3.1 and M3.3.1"
description: "Pin-by-pin ECM connector assignments for the E36 M50: Bosch DME M3.1 (1992) and M3.3.1 (VANOS, 1993-95), from the Bentley manual, with the safe way to test at the connector."
pillar: reference
keywords: "BMW E36 DME pinout, M50 ECU connector wiring, E36 OBD1 sensor wiring reference"
date: "2026-05-18"
hero: "e36-dme-connector-pinout-reference.webp"
reviewed: "2026-10-03"
sources:
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998, 130 Fuel Injection, Tables i and j (ECM pin assignments) and Table b (engine management systems)"
---

## TL;DR

- **What:** The pin assignments of the 88-pin engine control module (ECM, "DME") connector on the E36 M50, for both versions: **Bosch DME M3.1** (non-VANOS, 1992) and **Bosch DME M3.3.1** (VANOS, 1993–1995).
- **Why:** When a sensor or actuator misbehaves, checking the signal and the wiring at the ECM connector tells you whether the fault is the part, the wiring or the ECM.
- **Important:** The two versions use **different pins** for many functions, injectors and ignition coils included. Use the table for your DME.

---

## Which DME do you have?

| Engine | Engine management (Bentley) |
|---|---|
| M50, 1992 | Bosch DME M3.1 |
| M50 with VANOS, 1993–1995 | Bosch DME M3.3.1 |
| S50US (US M3), 1995 | Bosch DME M3.3.1 |
| M52 and S52US, 1996–1998 | Siemens MS41.1 (OBD2): a different system and connector, not covered here |

Both M50 systems have **distributorless ignition**: one coil per cylinder, each driven by its own ECM output.

---

## Before you probe the connector

Bentley's rules, there to protect the ECM:

- **Wait at least 40 seconds** after switching the ignition off before unplugging the ECM. Residual power in the system relay can damage the module if you unplug it sooner.
- Connect and disconnect the ECM connector and your meter probes **with the ignition off**.
- Use a **breakout box** where possible, so you can measure with the ECM connected and without spreading the small terminals. The alternative is to separate the connector housing and measure **from the back** of the connector.
- Test with a **digital multimeter or an LED tester only**: an analog meter or a bulb test light can damage the ECM.
- A replacement ECM must be **coded** for the car (engine, transmission and so on) before it is fitted.

**Where it is:** the ECM sits in a compartment at the **right rear of the engine compartment**, by the bulkhead. The cover is held by four captive screws; the connector releases with a fastener and pivots up off the module.

Bentley's advice on reading the results: no voltage or no continuity usually means a wiring or connector problem. A wrong value doesn't automatically mean the component is faulty, so check for loose, broken or corroded connections before replacing parts.

---

## Bosch DME M3.1 (M50, 1992)

Vacant pins are left out.

| Pin | Type | Function |
|---|---|---|
| 1 | Output | Fuel pump relay control (needs the crankshaft position signal to switch) |
| 2 | Output | Idle speed control valve, close signal (pulsed ground) |
| 3 | Output | Injector, cylinder 1 |
| 4 | Output | Injector, cylinder 3 |
| 5 | Output | Injector, cylinder 2 |
| 6 | Ground | Ground for the injector output stages |
| 8 | Output | Check Engine lamp |
| 11 | Output | Throttle position (load) signal to the transmission control module |
| 12 | Input | Throttle position sensor signal |
| 13 | Output | Mass air flow sensor hot-wire burn-off (for 0.5 s after shutdown) |
| 14 | Ground | Mass air flow sensor ground |
| 16 | Input | Cylinder identification sensor (AC pulse between pins 16 and 44) |
| 17 | Output | Fuel consumption signal to the instrument cluster |
| 23 | Output | Ignition coil, cylinder 2 |
| 24 | Output | Ignition coil, cylinder 3 |
| 25 | Output | Ignition coil, cylinder 1 |
| 26 | Input | Battery voltage at all times (terminal 30) |
| 27 | Output | Main relay control (to relay terminal 85) |
| 28 | Ground | Ground for the ECM and sensor shielding |
| 29 | Output | Idle speed control valve, open signal (pulsed ground) |
| 31 | Output | Injector, cylinder 5 |
| 32 | Output | Injector, cylinder 6 |
| 33 | Output | Injector, cylinder 4 |
| 34 | Ground | Ground for the output stages |
| 36 | Output | Evaporative purge valve |
| 37 | Output | Oxygen sensor heater relay control |
| 41 | Input | Mass air flow sensor signal |
| 43 | Ground | Ground for the temperature sensors and throttle position sensor |
| 44 | Input | Cylinder identification sensor (pair with pin 16) |
| 48 | Output | A/C compressor control |
| 50 | Output | Ignition coil, cylinder 4 |
| 51 | Output | Ignition coil, cylinder 6 |
| 52 | Output | Ignition coil, cylinder 5 |
| 54 | Input | Battery voltage from the main relay (terminal 87) |
| 55 | Ground | Ground for ignition control |
| 56 | Input | Battery voltage with key on or engine running (terminal 15) |
| 59 | Output | Throttle position sensor supply (5 V) |
| 60 | Input | Programming voltage, from the data link connector |
| 64 | Input | Ignition timing intervention from the A/T control module (during gearshifts) |
| 65 | Input | A/T range switch: park/neutral signal |
| 67 | Input | Crankshaft position / rpm sensor (AC voltage between pins 67 and 68) |
| 68 | Input | Crankshaft position / rpm sensor (pair with pin 67) |
| 70 | Input | Oxygen sensor signal (0–1 V, fluctuating when running) |
| 71 | Ground | Oxygen sensor signal ground |
| 73 | Input | Road speed signal from the instrument cluster |
| 74 | Output | Engine speed (TD) signal to the instrument cluster |
| 77 | Input | Intake air temperature sensor (0–5 V, varies with temperature) |
| 78 | Input | Coolant temperature sensor (0–5 V, varies with temperature) |
| 81 | Input | Drive-away protection enable, from the on-board computer |
| 85 | Input | A/C pressure switch signal, from the climate control module |
| 86 | Input | A/C compressor on request, from the climate control module |
| 87 | Input | Diagnostic RxD, to pin 15 of the data link connector |
| 88 | In/out | Diagnostic TxD, to pin 20 of the data link connector |

---

## Bosch DME M3.3.1 (M50 VANOS, 1993–1995)

Vacant pins are left out. Note how many functions moved compared with M3.1.

| Pin | Type | Function |
|---|---|---|
| 1 | Output | Fuel pump relay control (needs the crankshaft position signal to switch) |
| 2 | Output | Idle speed control valve, close signal (pulsed ground) |
| 3 | Output | Injector, cylinder 5 |
| 4 | Output | Injector, cylinder 6 |
| 5 | Output | Injector, cylinder 4 |
| 6 | Ground | Ground for the injector output stage |
| 7 | Output | VANOS solenoid (camshaft actuator) |
| 8 | Output | Check Engine lamp |
| 11 | Output | Throttle angle signal to the A/T control module |
| 13 | Input | Oxygen sensor signal (0–1 V, fluctuating when running) |
| 14 | Input | Mass air flow sensor |
| 15 | Ground | Ground |
| 16 | Input | Crankshaft position / rpm sensor (AC voltage between pins 16 and 43) |
| 17 | Input | Camshaft position sensor (Hall effect) |
| 23 | Output | Ignition coil, cylinder 4 |
| 24 | Output | Ignition coil, cylinder 6 |
| 25 | Output | Ignition coil, cylinder 5 |
| 26 | Input | Battery voltage at all times (terminal 30) |
| 27 | — | Main relay activation (relay terminal 85) |
| 28 | Ground | Ground for the ECM and sensor shielding |
| 29 | Output | Idle speed control valve, open signal (pulsed ground) |
| 31 | Output | Injector, cylinder 3 |
| 32 | Output | Injector, cylinder 2 |
| 33 | Output | Injector, cylinder 1 |
| 34 | Ground | Ground for the remaining output stages |
| 36 | Output | Evaporative purge valve |
| 38 | Output | Oxygen sensor heater relay control |
| 40 | Ground | Oxygen sensor signal ground |
| 41 | Input | Mass air flow sensor voltage signal |
| 42 | Input | Vehicle speed signal from the instrument cluster |
| 43 | Input | Crankshaft position / rpm sensor (pair with pin 16) |
| 44 | Ground | Ground for the intake air and coolant temperature sensors and the throttle position sensor |
| 45 | Ground | Ignition circuit shield |
| 46 | Output | Fuel consumption signal to the instrument cluster |
| 47 | Output | Engine speed (TD) signal to the instrument cluster |
| 48 | Output | A/C compressor relay control |
| 50 | Output | Ignition coil, cylinder 1 |
| 51 | Output | Ignition coil, cylinder 2 |
| 52 | Output | Ignition coil, cylinder 3 |
| 54 | Input | Battery voltage from the main relay |
| 55 | Ground | Ground for ignition control |
| 56 | Input | Battery voltage with key on or engine running (terminal 15) |
| 57 | Input | Ignition timing intervention from the A/T control module |
| 59 | Output | Throttle position sensor supply (5 V) |
| 60 | Input | Programming voltage, from the data link connector |
| 64 | Input | A/C on signal, from the climate control module |
| 65 | Input | A/C pressure signal, from the climate control module via the pressure switch |
| 66 | Input | Drive-away protection enable (starter immobilization relay) |
| 69 | Input | Knock sensor 2 (cylinders 4, 5, 6) |
| 70 | Input | Knock sensor 1 (cylinders 1, 2, 3) |
| 71 | Ground | Ground for the knock sensors and shields |
| 73 | Input | Throttle position sensor signal |
| 77 | Input | Intake air temperature sensor (0–5 V) |
| 78 | Input | Coolant temperature sensor (0–5 V) |
| 81 | Input | A/T park/neutral position signal |
| 87 | Input | Diagnostic RxD, to pin 15 of the data link connector |
| 88 | In/out | Diagnostic TxD, to pin 20 of the data link connector |

---

## Using the tables

- **Injector or coil complaints:** find the cylinder in the table for your DME, then test from that pin to the component. The pin for "cylinder 1" differs between M3.1 and M3.3.1.
- **Sensor readings:** the temperature sensors give 0–5 V that changes with temperature. The oxygen sensor fluctuates between 0 and 1 V with the engine running. The crankshaft sensor produces an AC voltage across its two pins while cranking.
- **Power and grounds first:** before condemning a sensor, check the ECM's supplies (terminal 30, terminal 15, main relay feed) and its ground pins with a voltage-drop test. See the [ground distribution guide](/guides/e36-ground-distribution-guide).
- **Full circuits:** for wire colours and everything between the ECM and each component, use the electrical wiring diagrams. See [How to read the E36 ETM](/guides/e36-how-to-read-etm).
