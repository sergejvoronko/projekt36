---
title: "BMW E36 Light Check Module (LKM) Explained"
description: "What the E36 light check module does, how it detects failed bulbs, why LED conversions trigger warnings, and how to diagnose lighting faults. Not the same as the E46's LCM."
pillar: reference
keywords: "bmw e36 lcm, e36 light check module, e36 lkm, e36 bulb failure warning, e36 led headlights"
date: "2026-04-13"
hero: "lcm.webp"
reviewed: "2026-10-06"
sources:
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998, 610 Electrical Component Locations, 630 Lights"
  - title: "ShiftBMW: E36 modification of the light control module for LED headlights"
    url: "https://www.shiftbmw.com/model/e36/e36-modification-of-light-control-module-for-led-headlights/"
---

## TL;DR

- The E36's **light check module (LKM, *Lichtkontrollmodul*)** watches the lighting circuits and reports failed bulbs to the instrument cluster or the check control display.
- It is **not** the E46/E39-style **LCM** that switches every light with transistors and is coded with NCS Expert. Much of what you read online about "the LCM" (xenon coding, per-output transistors, option coding) belongs to those later cars.
- The module checks for a **minimum current draw** from each monitored bulb. That's why **LED bulbs** and failed bulbs both trigger a warning.

---

## What it does

The headlight switch and stalks switch the lights through the normal relays and fuses. The light check module sits in those circuits and monitors whether the bulbs draw current when they're switched on. If a monitored bulb draws too little, the module flags it, and the warning appears in the instrument cluster, or as a text message on cars with **check control**.

Bentley's component location table places the **check control module** (where fitted) **below the left side of the dash**. Owners describe the light check module itself as a small black box mounted up under the driver's side of the dash, hard to reach. Use the electrical troubleshooting manual (ETM) for your car's build date to confirm its position and connector.

---

## Why LED bulbs cause warnings

An owner who modified the module for LED headlights found two separate problems:

1. **Current too low:** LEDs draw less current than the halogen bulb, below the module's "good" range.
2. **Too slow to start:** an LED's driver electronics need a moment to power up, while the module checks for current almost immediately.

Solutions are a correctly sized **load resistor** across the LED (which gets hot and needs mounting on metal), LED bulbs designed to be "CANbus" or warning-free for older BMWs, or a modification of the module itself. Before fitting LED headlight bulbs on the road, check whether they're legal in your country: in Slovakia, as in much of the EU, retrofitted LED bulbs in halogen headlights are often not type-approved.

---

## Diagnosing lighting faults

1. **Check the bulb first**, then its socket for corrosion or burnt contacts.
2. **Check the fuse and relay.** The fuse and relay positions are in the [fuse and relay reference](/guides/e36-fuse-relay-reference).
3. **Check the ground.** Lighting faults on an old car are often a corroded ground point. See the [ground distribution guide](/guides/e36-ground-distribution-guide).
4. **Measure at the bulb** with the light switched on: battery voltage at the supply, good ground on the other side.
5. **If one warning won't go away** with a good bulb and wiring, suspect the module. A common fault on these modules is **cracked solder joints**, often around the relays soldered to the circuit board. A careful resolder can fix it; otherwise, replace the module with one listed for your car on [RealOEM](https://www.realoem.com/).

To follow any circuit through the module, see [how to read the ETM](/guides/e36-how-to-read-etm).
