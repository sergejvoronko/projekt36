---
title: "BMW E36 M50 Sensor Values: Live Data and Multimeter Checks for Every Engine Sensor"
seoTitle: "BMW E36 M50 Sensor Values and Checks (OBD1)"
description: "Bentley test values for the E36 M50's engine sensors on Bosch DME M3.1 and M3.3.1: coolant and air temperature, throttle position, air flow meter, idle valve and oxygen sensor, and how to use them with live data."
pillar: reference
keywords: "BMW E36 OBD1 live data, INPA sensor values E36, BMW M50 sensor readings explained"
date: "2026-05-14"
hero: "e36-obd1-live-data-sensor-reference.webp"
reviewed: "2026-10-03"
sources:
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998, 130 Fuel Injection (Bosch DME M3.1 and M3.3.1 component tests)"
---

## TL;DR

- **What:** The factory test values for the M50's engine sensors (1992–1995, Bosch DME M3.1 and M3.3.1) and how to check each one, from the Bentley manual.
- **Why:** Live data from a scan tool tells you what the DME *thinks* it sees. A multimeter check against the factory value tells you whether the sensor and its wiring are telling the truth.
- **Rule of thumb:** compare a suspicious live-data value with a direct measurement at the sensor before replacing anything.

---

## Which system do you have?

| Engine | Engine management | Air flow meter |
|---|---|---|
| M50, 1992 | Bosch DME M3.1 | Hot-wire mass air flow sensor |
| M50 with VANOS, 1993–1995 | Bosch DME M3.3.1 | Hot-film mass air flow sensor |

The M52 (1996 on) uses Siemens MS41.1 with OBD2, and is not covered here. Many pin assignments also differ between M3.1 and M3.3.1. See the [DME pinout reference](/guides/e36-dme-connector-pinout-reference).

**Measurement rule:** use a **digital** multimeter. Bentley warns that an analog meter can damage the air flow sensor and that a bulb test light can damage the ECM.

---

## Coolant temperature (ECT) and intake air temperature (IAT) sensors

**Where they are on the M50:**

- **ECT sensor:** left side of the cylinder head, under the intake manifold. It is a **dual sensor**: one circuit for the DME and one for the temperature gauge.
- **IAT sensor:** in the intake manifold, behind the throttle position sensor.

Both are NTC sensors: resistance falls as temperature rises. Bentley's test values for DME M3.1 and M3.3.1 (Table f) are the same for both sensors:

| Temperature | Resistance |
|---|---|
| −10 °C | 7–11.6 kΩ |
| 20 °C | 2.1–2.9 kΩ |
| 80 °C | 0.27–0.40 kΩ |

**How to check:**

1. Unplug the sensor, switch the ignition on and check for about **5 V** reference between the supply wire in the harness connector and ground. (On the M50, the IAT supply is the **grey** wire.) No voltage means a wiring or ECM output problem.
2. Ignition off: measure the resistance across the sensor terminals and compare it with the table. The three points are just samples: the resistance should change smoothly as the temperature changes.

**With live data:** a cold engine's coolant and air temperature readings should both be close to the outside temperature. A coolant reading that doesn't match a known engine temperature means checking the sensor against the table.

The ECT sensor is tightened to **13 Nm** with a new copper sealing washer. Replace it only on a **cold** engine: hot coolant scalds.

---

## Throttle position sensor (TPS)

The TPS is a potentiometer on the side of the throttle housing, turned directly by the throttle shaft. It is **not adjustable**: if it fails the tests, replace it.

| Test (Bentley Table g, DME M3.1/M3.3.1) | Terminals | Value |
|---|---|---|
| Connector unplugged, ignition on: supply in the harness connector | Supply to ground | About 5 V |
| Connector unplugged, ignition off | Sensor terminals 1 and 3 | About 4 kΩ |
| Throttle turned from idle to full | Sensor terminals 1 and 2 | Varies about 1–4 kΩ **without interruption** |

A dead spot or jump while you sweep the throttle shows up as hesitation or idle trouble. On cars with traction control, don't confuse the main throttle body's TPS with the switch on the secondary throttle body.

---

## Idle speed control valve

The idle speed is controlled entirely by the DME and **cannot be adjusted**. Before testing the valve, make sure the throttle position sensor is OK.

1. **Engine running:** the valve should be **buzzing**.
2. **Load the engine:** switch on the A/C, or select Drive on an automatic. The idle should stay steady or rise slightly.
3. **If it doesn't buzz, or the idle drops:** stop the engine, unplug the valve and measure its coils. Tap the valve lightly while measuring if you suspect an intermittent fault.

| Terminals (M50) | Resistance |
|---|---|
| 1 and 2 | 20 ± 5 Ω |
| 2 and 3 | 20 ± 5 Ω |
| 1 and 3 | 40 ± 5 Ω |

These are electrical checks only. A valve can pass them and still stick mechanically; swapping in a known-good valve is the surest test. After fitting a new valve, the idle may be poor for about **10 minutes of driving** while the DME adapts.

---

## Mass air flow sensor

The air flow sensor is **not adjustable** and can't be serviced. If it fails or gives no output, the DME switches to a limp-home mode: the car usually still starts and drives.

**Hot-wire sensor (DME M3.1) checks:**

1. **Burn-off test:** take the sensor off the air cleaner but leave the harness connected. Rev the engine to at least 2,500 rpm and switch it off. About **four seconds** later the wire should **glow** for about one second; the DME burns contamination off it.
2. **Burn-off signal:** with a digital voltmeter at the back of the connector, terminals **1 and 4**, repeat the test. About four seconds after shut-off, the voltage should rise to **about 4 V for about one second**. Voltage present but no glow means the sensor is faulty.
3. **Supply:** with the ignition on, there should be **ground at pin 4** and **battery voltage at pin 2**.
4. **Resistance (M3.1):** with the ignition off and the connector unplugged, sensor terminals **5 and 6** should read **3–4 Ω**.

**With live data:** an air-flow reading that seems too low, together with lean running, also points at **unmetered air**: a split intake boot between the sensor and the throttle body, or a loose clamp.

---

## Oxygen sensor

The oxygen sensor's signal at idle should **fluctuate between about 0.2 and 0.8 V** once the engine is warm. The DME ignores it until the engine and sensor are warm enough.

- **Stuck low** (lean) or **stuck high** (rich): suspect the mixture first, such as an air leak, fuel pressure or an injector. Then the sensor.
- **No fluctuation at all:** check the sensor heater (its relay and the heater element) and the sensor itself.

Bentley's trick to check the sensor's response: create a small air leak (lean), or pull the vacuum hose off the fuel pressure regulator to raise fuel pressure (rich), and watch the signal follow.

---

## Fuel pressure and battery voltage

Two values every live-data session should be checked against:

| Value | Specification (Bentley) |
|---|---|
| Fuel pressure, M50 (pump running, no vacuum) | 3.0 ± 0.2 bar; 0.4–0.7 bar lower at idle |
| Charging voltage, engine running | 13.5–14.5 V |

See the [fuel system guide](/guides/e36-fuel-system-guide) and the [charging system guide](/guides/e36-charging-system-diagnosis) for the full tests.

---

## Reading live data

Live data needs a BMW-capable diagnostic tool on the round **20-pin diagnostic connector** under the bonnet. See the [OBD1 diagnostic setup guide](/guides/e36-obd1-diagnostic-setup). Labels and units differ between tools, so the most reliable baseline is a **recording from your own car when it runs well**: log idle, part throttle and a few full-throttle runs, and compare later readings with that.

For stored fault codes, no tool is needed at all: see the [OBD1 fault code reference](/guides/e36-obd1-fault-code-reference).
