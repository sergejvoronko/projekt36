---
title: "BMW E36 M52 to M54 Engine Swap: The Ultimate Guide"
description: "What swapping an M54 into an E36 really involves: the engine's facts, the four problem areas (oil system and fitment, electronic throttle, returnless fuel, DME and immobiliser) and how to plan for them."
pillar: swap
keywords: "E36 M54 swap, M52 to M54 conversion, E36 engine swap wiring, M54 swap parts list, E36 M54 DME adaptation, BMW E36 performance upgrade"
date: "2026-05-25"
hero: "e36-m52-to-m54-engine-swap-guide.webp"
reviewed: "2026-10-03"
sources:
  - title: "Wikipedia: BMW M54 (specifications, electronic throttle, non-return fuel system)"
    url: "https://en.wikipedia.org/wiki/BMW_M54"
  - title: "Wikipedia: BMW M52 (block versions)"
    url: "https://en.wikipedia.org/wiki/BMW_M52"
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998 (E36 fuel system and engine management)"
---

The M54 (2000–2006) is the last of BMW's M5x six-cylinders: an aluminium block with iron liners, double VANOS and Siemens MS43 engine management. Physically it's a close relative of the M52, which is why it gets swapped into E36s. **Electronically it's a generation newer than any E36**, and that is where the work is.

This guide maps out what has to be solved. It is not a wiring how-to: the connection-level detail depends on the exact donor and car, and has to come from both cars' wiring diagrams.

## TL;DR

| | |
| :--- | :--- |
| **What** | An M54B25 or M54B30 in an E36. |
| **Why** | The M54B30 makes 228 hp and 300 Nm. |
| **Hardest parts** | Fully electronic throttle, the non-return fuel system, and making the MS43 DME work (immobiliser included) in a car that was never designed for it. |
| **Difficulty** | 5/5 for the electronics |

---

## The engine

| | M54B22 | M54B25 | M54B30 |
|---|---|---|---|
| Displacement | 2,171 cc | 2,494 cc | 2,979 cc |
| Bore × stroke | 80 × 72 mm | 84 × 75 mm | 84 × 89.6 mm |
| Power | 168 hp | 189 hp | 228 hp |
| Torque | 210 Nm | 245 Nm | 300 Nm |

Common to all: **aluminium block with iron cylinder liners, double VANOS, Siemens MS43**, a **fully electronic throttle with no mechanical back-up**, and a **non-return fuel system**.

For comparison, the E36's own M52 has a single VANOS, Siemens MS41.1 and a mechanical throttle cable. Its block is aluminium in most markets and cast iron in the original US and Canadian cars.

---

## The four problem areas

### 1. Physical fit: oil system, manifolds, ancillaries

The M54 was built for the E46/E39 engine bays. In an E36, expect to adapt:

- the **oil pan, pickup and dipstick** to clear the E36 front subframe and steering
- the **exhaust manifolds** to clear the E36 chassis and steering shaft
- **ancillary brackets:** power steering, A/C and the belt drive

Identify which E36-family parts your donor needs from a documented swap of the same donor engine, not from a generic list.

### 2. Electronic throttle

The M54 has **no throttle cable**: an electronic pedal drives the throttle through the DME. The E36's cable pedal can't be used. The swap needs an electronic accelerator pedal mounted in the E36 footwell, wired to the MS43.

### 3. Fuel system

The **M54 expects the non-return system** it was designed for. The E36 has a **return-type system**: on the M50 the regulator sits on the fuel rail, and on later E36s (M52) it sits under the car at the fuel filter. The fuel supply has to give the M54 rail the pressure it expects. A common approach is a filter-and-regulator unit in the E36's feed line that returns the excess fuel to the tank. Confirm pressures for your setup with a gauge.

### 4. DME, immobiliser and the rest of the car

- **Use the M54's own DME and harness.** Running the M54 on an E36 DME would throw away the double VANOS and the electronic throttle control.
- **Immobiliser:** the MS43 expects to be released by its own immobiliser. Either the donor's matched components come along, or the DME is reprogrammed by a specialist; plan this before buying the DME.
- **Chassis integration:** the E46-era engine electronics also have to supply signals the E36 car expects (rev counter, temperature gauge, fuel pump, oil warning, diagnosis). That needs the wiring diagrams of **both** cars; there's no universal pin table.

---

## Planning advice

1. Pick the donor first, and find a **detailed write-up of the same swap** (M54 into E36) to work from.
2. Buy the donor **complete**: harness, DME, pedal, air flow sensor, and everything the immobiliser needs.
3. Budget for a **specialist** for the DME and immobiliser work.
4. Solve the electronics on paper before the engine goes in.

If the goal is simply more six-cylinder power with far less electronics work, an **M50** (OBD1 cars) or **M52** (OBD2 cars) swap, possibly with the [M50 intake manifold](/guides/bmw-e36-m50-manifold-conversion-guide), stays within the E36's own electronics generation.
