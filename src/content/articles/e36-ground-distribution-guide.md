---
title: "BMW E36 Ground Distribution, Every Ground Point Located"
description: "Where the E36's ground points really are, from the Bentley component-location table, how to test them with a voltage-drop test, and how to restore them."
pillar: reference
keywords: "bmw e36 grounds, e36 ground points, e36 electrical gremlins, e36 chassis ground, G100 G101 G201"
date: "2026-04-13"
hero: "grounds.webp"
reviewed: "2026-10-03"
sources:
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998, 600 Electrical System–General and 610 Electrical Component Locations"
---

## TL;DR

Bad grounds cause a large share of electrical faults on old cars: flickering lights, odd instrument readings, modules misbehaving, starting and charging trouble. The E36 returns current to the battery through numbered **ground points** bolted to the body and the engine. On a 25–30-year-old car, corrosion at those points is a prime suspect whenever several unrelated electrical problems appear together. The reliable test is a **voltage-drop test** under load.

---

## Why grounds fail

A ground point is a ring terminal (often several, stacked) clamped to the body or engine by a bolt. Over decades three things go wrong:

- **Corrosion between terminal and body:** an oxide layer forms where the terminal meets the metal, especially where water collects.
- **Corroded terminals:** green or white deposits on the ring terminal itself.
- **Damaged wires:** stubs near the ground point chafed or broken, especially on the engine, where vibration works on them.

Because several circuits often share one ground point, one bad ground can cause several apparently unrelated faults at once. That pattern is the clue.

---

## E36 ground point locations (Bentley)

BMW numbers each ground point; the same numbers appear in the electrical wiring diagrams (ETM). The table lists every ground in Bentley's E36 component-location table:

| Ground | Years | Location |
|---|---|---|
| G100 | 1995–1998 | Front of left front fender (headlights) |
| G101 | 1992–1998 | Front of right front fender |
| G102 | 1992–1998 | Left front strut tower |
| G103 | 1992–1998 | Right front strut tower |
| G110 | 1992–1998 | Left front of engine |
| G111 | 1992–1998 | Near battery |
| G117 | 1992–1998 | Right rear of engine |
| G119 | 1992–1998 | Right front of engine |
| G123 | 1992–1998 | Right side of safety wall (bulkhead) |
| G200 | 1992–1998 | Left kick panel |
| G201 | 1992–1998 | Right side of instrument panel |
| G202 | 1992–1998 | Left side of instrument panel |
| G203 | 1992–1998 | Right kick panel |
| G230 | 1992–1998 | Right kick panel |
| G301 | 1992–1998 | Below right front seat |
| G302 | 1992–1998 | Below centre console |
| G303 | 1992–1998 | Below right rear seat |
| G310 | 1992–1998 | Behind right rear seat |
| G312 | 1992–1998 | Behind left rear seat |
| G313 | 1992–1998 | Right side of rear shelf |
| G314 | 1992–1998 | Left side of rear shelf |
| G400 | 1992–1998 | Left front side of boot |
| G404 | 1992–1998 | Left rear side of boot |

**Which circuits use which ground:** look up the circuit in the wiring diagrams for your car. Each diagram shows the ground number the component returns to. See [How to read the E36 ETM](/guides/e36-how-to-read-etm).

Besides these points, the **battery negative cable to the body** and the **ground strap between engine and body** carry the heavy currents for starting and charging. Bentley lists a loose or dirty body ground strap as a cause of both slow cranking and charging problems.

---

## Testing: voltage drop, not resistance

A resistance check is not much use here. The resistances involved are too small for most ohmmeters to read, yet they still matter. Bentley's example: just 0.02 Ω in a 150 A starter circuit drops 3 V.

Measure **voltage drop with current flowing** instead:

1. Switch on the circuit you are testing (headlights, blower, cranking the starter) so current flows.
2. Put a digital multimeter's leads on the two ends of the connection you're testing. For a ground, that means the component's ground terminal (or the ground point) and the **battery negative terminal**.
3. Read the voltage: that's the loss across the ground path.

**Maximum voltage drops** (SAE figures, quoted by Bentley):

| Connection | Maximum drop |
|---|---|
| Small wire connections | 0 V |
| High-current connections | 0.1 V |
| High-current cables | 0.2 V |
| Switch or solenoid contacts | 0.3 V |
| Any connector or short cable | 0.5 V |

On long wires the drop may be slightly higher, but **more than 1.0 V usually means a problem**.

---

## Restoring a ground point

1. **Disconnect the battery** (negative terminal, in the boot) first.
2. Remove the ground bolt and note the order of the stacked ring terminals.
3. Clean the contact pad on the body to **bare metal** and clean each ring terminal on both faces.
4. Check the wires at each terminal for breaks or chafing, and repair any you find.
5. Refit the terminals in their original order and tighten the bolt firmly, without stripping the thin sheet metal.
6. Protect the joint against moisture once it's tight. A coat of paint or wax over the finished joint works.
7. Reconnect the battery and repeat the voltage-drop test under load.

Pay special attention to grounds in places where water collects, such as the **kick panels** and **under the seats**, and to the **engine grounds** near heat and vibration.

---

## After an engine swap

On an M43 → M50 swap, check before diagnosing sensors or the DME:

- the **engine-to-body ground strap** is fitted and tight (it's easily forgotten when the engine goes in)
- the engine-side ground points (G110, G117, G119) are connected to the new engine's harness
- the **battery negative cable** is sound at both ends

A freshly swapped engine that cranks but won't start, or runs badly, deserves a full voltage-drop check of its grounds first.

---

## Quick fault-tracing guide

| Symptom | Where to start |
|---|---|
| Slow cranking, or charging faults with a good alternator | Battery negative cable, engine-to-body ground strap |
| Several faults in the engine compartment at once | Engine grounds G110 / G117 / G119, strut tower grounds G102 / G103 |
| Headlight problems | Fender grounds G100 / G101 |
| Dashboard and interior faults together | Kick-panel and instrument-panel grounds G200–G203, G230 |
| Faults under or behind the seats, or at the rear | G301–G314 |
| Boot and rear lighting faults | G400 / G404 |
| Not sure | Find the circuit in the wiring diagram and test its ground with a voltage-drop test |
