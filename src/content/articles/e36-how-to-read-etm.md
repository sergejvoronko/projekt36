---
title: "How to Read the BMW E36 Electrical Troubleshooting Manual (ETM)"
description: "How to navigate the BMW E36 ETM: wire colour codes, component numbers, fuse assignments, and tracing any circuit."
pillar: reference
keywords: "bmw e36 etm, e36 wiring diagram, e36 electrical manual, bmw wire colour codes, e36 circuit tracing"
date: "2026-04-13"
hero: "etm.webp"
---

## TL;DR

The BMW ETM (Electrical Troubleshooting Manual) is the complete wiring reference for the E36. Most people open it, see a tangle of lines and abbreviations, and close it immediately. This guide teaches you to navigate it systematically — find any component, trace any circuit, understand what every abbreviation means, and diagnose a fault from the manual alone.

---

## What the ETM Contains

The E36 ETM is organized into numbered schemas (circuit diagrams). Each schema covers a functional system:

| Schema | System |
|--------|--------|
| 1 | Power supply, fuses, relays, grounds |
| 2 | Starting & charging, EWS, cooling fan |
| 3 | Engine management (DME) |
| 4 | Exterior lighting (LCM, headlights, turn signals, brake/tail) |
| 5 | Instrument cluster, warning lights |
| 6 | Interior lighting, ZKE, vanity mirrors, lighter |
| 7 | ABS, traction control, DSC |
| 8 | Wipers, washers, horn, HVAC |
| 9 | Radio, amplifier, speakers |
| 10 | Power windows, central locking, mirrors, heated seats |
| 11 | Airbags, seat belt tensioners |

The numbering varies slightly between model years (318i vs 325i, pre- vs post-facelift). Always confirm which schema covers the system you're tracing before you start.

---

## The Header Box — Read This First

Every schema page starts with a header box in the top left. This is the key to the whole page:

### Wire Colours

The colour legend lists the abbreviation codes used on every wire in that schema. BMW uses German-origin abbreviations:

| Code | Colour | German |
|------|--------|--------|
| Bl   | Blue   | Blau |
| Br   | Brown  | Braun |
| Ge   | Yellow | Gelb |
| Gn   | Green  | Grün |
| Gr   | Grey   | Grau |
| Or   | Orange | Orange |
| Rt   | Red    | Rot |
| Sw   | Black  | Schwarz |
| Vi   | Violet | Violett |
| Ws   | White  | Weiß |

Wire codes on the diagram use these abbreviations combined with a gauge number and sometimes a tracer colour. For example:

- **0.35 Bl/Rt** — 0.35 mm² wire, Blue with Red tracer
- **1.5 Br** — 1.5 mm² wire, solid Brown
- **6.0 Rt/Ws** — 6.0 mm² wire, Red with White tracer

The number before the colour is the cross-sectional area in mm². Larger = more current capacity. Ground wires are almost always Brown (Br). Battery positive mains are almost always Red (Rt).

### Diagram Symbols

The symbols list identifies the numbered components shown in the schema. Each component has a number (e.g., "7 — ABS / traction control module") that appears in a dashed rectangle on the diagram. When you see a dashed box with a number, look it up in the header symbols list to know what it represents.

---

## Anatomy of a Circuit

Every circuit in the ETM runs from **battery positive** at the top of the page, through protection (fuse), through load (component), to **chassis ground** at the bottom. Understanding this top-to-bottom flow is the single most important thing to grasp.

### Power distribution

Power enters the diagram at the top. You'll see:
- **Thick red lines** — battery positive, unfused (before fuse box)
- **Kl. 30** — permanent battery positive (terminal 30, always live)
- **Kl. 15** — ignition-switched positive (only live with ignition on)
- **Kl. 58** — parking/tail light feed

These terminal designations (Kl. = Klemme = terminal) are DIN standards used across all European vehicles of this era.

### Ground paths

Grounds (Br wire, usually terminating at a chassis ground point) run along the bottom of the diagram. E36 has multiple ground points — G100, G101, G201, etc. — documented in the ground distribution section. A bad ground is one of the most common causes of electrical faults. More on this in the dedicated ground distribution guide.

### Connectors and pin numbers

Every connector in the diagram shows:
- A connector identifier (e.g., **X60** or **C211**)
- Pin numbers inside the connector symbol

The connector identifier lets you find the physical connector in the car using the connector location drawings (usually in a separate section of the ETM). Pin numbers match the physical pin numbers moulded into the connector housing.

---

## Following a Circuit — Step by Step

Let's trace the brake light circuit as an example.

**Goal:** Understand why the left rear brake light doesn't work but the right does.

1. **Find the relevant schema** — brake lights are in Schema 4 (Exterior Lighting).

2. **Locate the component** — look in the Diagram Symbols list for "brake light" or "tail light." Find its component number. Locate the dashed box with that number on the diagram.

3. **Trace back to fuse** — follow the wire from the brake light bulb upward through the circuit. You'll pass through connectors and eventually reach a fuse. Note the fuse number.

4. **Check fuse assignment** — Schema 1 (Power Distribution) shows what each fuse protects. Confirm the fuse number matches the brake circuit.

5. **Find the branch point** — the left and right brake lights are wired in parallel. Find where the circuit splits. Everything before the split is common to both lights; everything after is individual.

6. **Check the connectors between split and fault** — the fault is isolated to the left side, so check every connector between the branch point and the left bulb. Each connector symbol in the diagram is a potential fault point.

7. **Verify the ground** — trace the ground wire from the left bulb downward to the ground point. A corroded ground causes exactly this symptom (one side works, other doesn't) when they share a circuit but have individual ground paths.

---

## Cross-Schema References

Components often appear on multiple schemas. When you see:

> **See diagram 11: ABS / traction control module**

…it means that component's full circuit detail is shown on another schema. This is a cross-reference. The current schema only shows the wires relevant to its own system; the full pinout of the component is on the referenced schema.

This matters when you're chasing an intermittent fault that involves multiple systems — for example, a speed sensor that feeds both ABS (Schema 7) and the instrument cluster (Schema 5).

---

## Reading Wire Gauge Sizes

Wire gauge affects diagnostic decisions:

| Gauge | Typical use |
|-------|-------------|
| 0.35 mm² | Signal wires, sensor inputs, K-Bus |
| 0.5 mm²  | Low-current outputs, lamp feeds |
| 1.0 mm²  | Medium loads, solenoids |
| 1.5 mm²  | Higher loads, motor feeds |
| 2.5 mm²  | Fused feeds, main lighting circuits |
| 4.0 mm²  | High-current loads, starter signal |
| 16–25 mm²| Battery main cables, alternator |

When you find a burnt wire, the gauge tells you if the original fuse rating was appropriate. A 0.35 mm² wire on a 15A fuse is a fire waiting to happen.

---

## Common Abbreviations in the ETM

| Abbreviation | Meaning |
|---|---|
| Kl. 30 | Battery + (permanent) |
| Kl. 15 | Ignition + (switched) |
| Kl. 31 | Ground |
| Kl. 50 | Starter activation |
| Kl. 58 | Parking/tail light |
| DME | Digital Motor Electronics (engine ECU) |
| EWS | Wegfahrsperre (immobilizer) |
| ZKE | Central Body Electronics (comfort module) |
| LCM | Light Control Module |
| GM | Grundmodul (basic module) |
| K-Bus | Diagnostic / body bus |
| CAN | Controller Area Network (later E36s) |

---

## Practical Tips

**Print the schema you're working with.** The ETM as a PDF is designed for paper. On screen it's tiny; printed A3 (or A4 with magnification) you can trace circuits with a pencil.

**Start with the fuse, not the component.** If something doesn't work, find the fuse first. A blown fuse tells you there's a short somewhere in that circuit. A good fuse with no output tells you power isn't reaching the fuse.

**The connector is usually the fault.** In a 30-year-old car, corroded or backed-out connector pins cause 80% of electrical faults. Once you trace a circuit, physically clean and reseat every connector in that path before replacing components.

**Ground points are suspects.** Brown wires going to chassis ground points (G100, G101, etc.) corrode. A bad ground causes bizarre symptoms — a light on one circuit affecting another, sensors reading wrong, modules behaving erratically. The ground distribution guide lists every E36 ground point with its chassis location.

**Use the ETM alongside live diagnostics.** INPA fault codes tell you *what* failed; the ETM tells you *where* and *why*. Use both together.
