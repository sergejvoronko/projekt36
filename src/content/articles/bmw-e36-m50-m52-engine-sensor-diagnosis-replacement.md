---
title: "BMW E36 M50/M52 Engine Sensor Diagnosis & Replacement: The Definitive Guide"
seoTitle: "BMW E36 M50/M52 Sensor Diagnosis and Replacement"
description: "Which engine sensors the E36 M50 and M52 actually have (by DME), what each one does, the symptoms of failure, where they sit and how to replace them, with Bentley values."
pillar: engine
keywords: "E36 engine sensors, M50 sensor diagnosis, M52 sensor replacement, crankshaft position sensor E36, camshaft position sensor E36, MAF sensor testing, O2 sensor E36, throttle position sensor E36, engine coolant temperature sensor E36"
date: "2026-06-21"
hero: "bmw-e36-m50-m52-engine-sensor-diagnosis-replacement.webp"
reviewed: "2026-10-03"
sources:
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998, 120 Ignition System, 130 Fuel Injection, 117 Camshaft Timing Chain"
---

Failing sensors cause a large share of running problems on a 25-year-old M50 or M52. The fastest way to the cause is to know **which sensors your engine actually has**, read the fault memory, then test the suspect against its factory values before buying parts.

For the test values (resistances, voltages), see the [M50 sensor values guide](/guides/e36-obd1-live-data-sensor-reference).

## TL;DR

| | |
| :--- | :--- |
| **What:** | The M50/M52 engine sensors: what they do, how they fail, where they are and how to replace them. |
| **First step:** | Read the fault codes. OBD1 cars (1992–1995): five accelerator presses. OBD2 cars (1996 on): an OBD2 scan tool. |
| **Difficulty:** | 2/5 for most sensors; 4/5 for the knock sensors (intake manifold off). |

---

## Which sensors your engine has

| Sensor | M50, 1992 (DME M3.1) | M50 VANOS, 1993–95 (DME M3.3.1) | M52, 1996–98 (MS41.1) |
|---|---|---|---|
| Crankshaft position / rpm sensor | Yes | Yes | Yes |
| Camshaft sensor | Cylinder identification sensor | Hall-effect camshaft position sensor | Yes |
| Knock sensors | **None** | Two | Two |
| Air flow meter | Hot-wire | Hot-film | Hot-film |
| Coolant temperature (ECT) | Yes (dual: DME and gauge) | Yes | Yes |
| Intake air temperature (IAT) | Yes | Yes | Yes |
| Throttle position (TPS) | Yes | Yes | Yes |
| Oxygen sensor(s) | Yes | Yes | Yes (OBD2 adds monitoring sensors) |

Bentley states it plainly: every engine in the manual except the **1992 M50** has knock sensors.

---

## Crankshaft and camshaft sensors: no-start and cut-out

- The **crankshaft position / rpm sensor** tells the DME engine speed and crank position. Without its signal, the DME sets no ignition point **and doesn't switch the fuel pump relay**, so the engine cranks but won't start. A tachometer that doesn't move while cranking is a clue. On the 1992–1995 M50, the sensor is on the **timing cover**.
- The **camshaft sensor** tells the DME which cylinder is on its firing stroke.
- **OBD1 codes:** 1243 (crankshaft sensor) and 1244 (camshaft sensor) are stored by M3.3.1 only. See the [fault code reference](/guides/e36-obd1-fault-code-reference).

**Replacing the camshaft position sensor (six-cylinder with VANOS, Bentley):**

1. Remove the plastic cover above the injectors.
2. Disconnect and unscrew the **VANOS solenoid**, and remove the **VANOS oil supply line**.
3. Remove the sensor from the **left front of the cylinder head**, next to the top of the oil filter housing. Disconnect its harness under the intake manifold.
4. Fit it with a **new O-ring** and route the wiring exactly as before.

| Fastener | Torque |
|---|---|
| Camshaft position sensor to head | 5 Nm |
| VANOS oil supply line | 32 Nm |
| VANOS solenoid | 30 Nm |

---

## Air flow meter and oxygen sensor: mixture problems

- A faulty **air flow meter** causes hesitation, poor running and mixture faults. If it fails completely, the DME runs a limp-home mode: the car still drives, but badly. The air flow meter **can't be adjusted or repaired**. On the 1992 M50's hot-wire meter, the four-second burn-off after switch-off is a useful test.
- The **oxygen sensor** signal should swing between about **0.2 and 0.8 V** at idle on a warm engine. A sensor that stays flat, or a faulty heater, upsets the mixture control.
- Before condemning either one, look for **intake air leaks** after the air flow meter. Unmetered air causes the same symptoms, and the intake boot is a classic place for a split.

The oxygen sensor is tightened to **55 Nm** with anti-seize on the thread.

---

## Throttle position and coolant temperature: drivability

- **TPS:** a worn track gives erratic idle and stumbles. Its resistance should change smoothly, with no interruption, as the throttle opens. It is **not adjustable**: replace it if it fails.
- **ECT:** a sensor that reads cold all the time makes the engine run rich and start badly. Check it against the temperature table.
- **Location of the M50 ECT:** left side of the cylinder head, under the intake manifold. Replace it only with the engine **cold**, using a new copper sealing washer, tightened to **13 Nm**.

---

## Knock sensors (M3.3.1 and M52 only)

The knock sensors are bolted to the **left side of the cylinder block** and reached by removing the **intake manifold**. If the DME detects knock it retards the ignition, and a faulty sensor sets a fault code (1225/1226 on OBD1 M3.3.1).

- **Clean the contact surface** on the block before fitting.
- Tighten to **20 Nm**.
- On the M52, a single harness connects both sensors; the **shorter lead goes to the sensor for cylinders 4–6**.

Since the intake manifold has to come off, combine knock sensor work with other jobs under the manifold.

---

## Buying sensors

Look up part numbers by **VIN** on [RealOEM](https://www.realoem.com/): sensors differ between M3.1, M3.3.1 and MS41.1 engines. Prefer the original manufacturer's parts (Bosch or Siemens/VDO, depending on the engine).
