---
title: "M43 to M50 Swap, Wiring Differences and What to Reuse"
description: "The electrical side of an E36 M43 to M50 swap: why the M50 harness plugs in, what the M50's DME needs, the EWS question by build date, and the post-swap electrical checks."
pillar: swap
keywords: "m43 m50 swap wiring, e36 engine swap electrics, m50 wiring harness, m43 m50 ecu wiring"
date: "2026-04-13"
hero: "wiring-swap.webp"
reviewed: "2026-10-03"
sources:
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998 (engine management by year, ECM pin tables, sensors, EWS, cooling fans, charging)"
  - title: "Bimmerfest: E36 318is budget build and basic guide to an M50 swap (owner's write-up)"
    url: "https://www.bimmerfest.com/threads/e36-318is-budget-build-and-basic-guide-to-an-m50-swap.811944/"
---

## TL;DR

Use the **complete M50 engine harness and the DME from the donor engine**. Owners who have swapped an M50 into a four-cylinder OBD1 E36 report that the M50 engine harness **plugs into the same chassis connector** the four-cylinder harness used. The body wiring (lights, locks, instruments) stays. The real electrical work is the **immobiliser (EWS)**, if your car has one, plus a careful check of power, grounds and charging after the swap.

---

## What changes with the engine

| | M50 non-VANOS (1992) | M50 VANOS (1993–1995) |
|---|---|---|
| Engine management (Bentley) | Bosch DME M3.1 | Bosch DME M3.3.1 |
| Air flow meter | Hot-wire | Hot-film |
| Knock sensors | **None** (no knock inputs on the M3.1) | Two (cylinders 1–3 and 4–6) |
| Camshaft sensor | Cylinder identification sensor | Hall-effect camshaft position sensor |
| VANOS solenoid | — | Yes |
| Ignition | One coil per cylinder | One coil per cylinder |

Whichever you have, the engine sensors, the DME and the harness belong together. **Don't mix M43 parts or wiring into the M50 system.** The DME, harness and sensors from the donor engine are a matched set.

Sensor locations worth knowing on the M50:

- **Coolant temperature sensor:** left side of the cylinder head, under the intake manifold. It's a dual sensor: one circuit feeds the DME, the other the temperature gauge.
- **Intake air temperature sensor:** in the intake manifold, behind the throttle position sensor.

Pin assignments for both DMEs are in the [DME pinout reference](/guides/e36-dme-connector-pinout-reference), and sensor test values in the [sensor values guide](/guides/e36-obd1-live-data-sensor-reference).

---

## EWS: check your car's build date

Bentley's timeline:

| Built | System |
|---|---|
| Before January 1994 | No immobiliser |
| From January 1994 | **EWS:** a starting-inhibition module that interrupts ignition, fuel injection and the starter; armed and disarmed by the central locking; module under the left side of the dashboard |
| From January 1995 | **EWS II:** coded keys; if the key code doesn't match, the DME and starter are disabled |

**What to do:**

1. **Look for the module** under the left side of the dashboard (on EWS II cars, owners report it under the glovebox area). No module means no EWS work: the donor DME and harness go straight in.
2. **If your car has EWS,** plan the solution before buying the DME. In an owner's write-up of an M50TU going into a 1995 (EWS II) 318is, a **"red label" DME ending in 413** was used, and wiring changes at the EWS module were still needed. Details are in the [EWS guide](/guides/e36-ews-immobilizer-guide).

A swap that is mechanically complete, cranks well and won't start points at the immobiliser first: check it before chasing sensors.

---

## Cooling fans

The M50 keeps the E36's fan arrangement:

- **Belt-driven fan with a viscous clutch** on the water pump: no wiring.
- **Two-speed electric auxiliary fan** in front of the radiator. Bentley: it serves mainly the A/C, but also switches on when the coolant gets hot, through a **dual temperature switch in the radiator**: low speed at **91 °C**, high speed at **99 °C**.

The DME doesn't switch these. Fit the six-cylinder auxiliary fan and make sure the radiator's temperature switch is connected.

---

## Post-swap electrical checks

1. **Grounds:** the engine-to-body ground strap, the battery negative cable and the engine ground points. Test with a voltage-drop test under load. See the [ground guide](/guides/e36-ground-distribution-guide).
2. **DME supplies:** battery voltage at all times (terminal 30), with the key on (terminal 15), and from the main relay. Check at the DME connector following Bentley's safe-testing rules.
3. **Charging:** the alternator's **D+** wire connected; the charge warning light on with the ignition on; **13.5–14.5 V** at the battery with the engine running. See the [charging guide](/guides/e36-charging-system-diagnosis).
4. **Fuel pump:** the DME switches the fuel pump relay only when it sees the crankshaft signal. No pump while cranking points at the crankshaft sensor or its wiring.
5. **Fault codes:** read them with five accelerator presses (ignition on). See the [OBD1 fault code reference](/guides/e36-obd1-fault-code-reference).
