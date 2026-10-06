---
title: "How to Read the BMW E36 Electrical Troubleshooting Manual (ETM)"
seoTitle: "How to Read the BMW E36 ETM Wiring Diagrams"
description: "How to read E36 wiring diagrams: BMW and Bentley colour codes, terminal numbers (30, 15, 31, 50, 85–87), component and ground numbers, and a step-by-step way to trace any circuit with a multimeter."
pillar: reference
keywords: "bmw e36 etm, e36 wiring diagram, e36 electrical manual, bmw wire colour codes, e36 circuit tracing"
date: "2026-04-13"
hero: "etm.webp"
reviewed: "2026-10-06"
sources:
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998, 600 Electrical System–General (Table a, terminal and circuit numbers; wiring codes), Electrical Wiring Diagrams (ELE), 610 Electrical Component Locations"
---

## TL;DR

- E36 wiring diagrams come in two forms: **BMW's own ETM** (German colour abbreviations such as **SW**, **BR**, **RT**) and the **redrawn diagrams in the Bentley manual** (English abbreviations such as **BLK**, **BRN**, **RED**). Both show the same circuits.
- Learn the **terminal numbers**: **30** (battery, always live), **15** (ignition on), **31** (ground), **50** (starter), **85/86/87** (relays).
- Trace a circuit from **power, through fuse, switch and load, to ground**, then test it with a **digital multimeter** or LED test light, never a bulb test lamp.

---

## What's in the diagrams

Bentley's Electrical Wiring Diagrams section covers the 1992–1998 E36 by system, for example: Power Distribution, Ground Distribution, Starting, Charging System, Engine Management, Exterior Lights, Headlights/Foglights, Instrument Panel, Power Windows, Power Door Locks, Anti-Theft (EWS II), ABS and many more. Many systems have **several versions by model and year**: first find the diagram that matches your car's model, engine and build date.

Fuse, relay and ground **locations** are in a separate part of the manual (610 Electrical Component Locations), not on the diagrams themselves.

---

## Wire colours

A combined code means a coloured wire with a stripe: Bentley's example is **BLU/RED**, a blue wire with a red stripe. BMW's own ETM uses German abbreviations and often adds the cross-section in mm² before the colour (for example **0.75 BL/RT**).

| Colour | BMW (German) | Bentley |
|---|---|---|
| Black | SW (*schwarz*) | BLK |
| Brown | BR (*braun*) | BRN |
| Red | RT (*rot*) | RED |
| Yellow | GE (*gelb*) | YEL |
| Green | GN (*grün*) | GRN |
| Blue | BL (*blau*) | BLU |
| Violet | VI (*violett*) | VIO |
| Grey | GR (*grau*) | GRY |
| White | WS (*weiß*) | WHT |
| Orange | OR (*orange*) | ORG |
| Pink | RS (*rosa*) | PNK |

On BMWs, **brown** wires are normally grounds. Bentley also notes that a wire in the car can be a different colour from the diagram: what matters is that it connects the right terminals.

---

## Terminal numbers (Bentley Table a)

| Terminal | Meaning |
|---|---|
| 1 | Low-voltage switched terminal of the ignition coil |
| 4 | High-voltage centre terminal of the coil |
| 15 | From the ignition switch: live in RUN and START |
| 30 | Battery positive: live whenever the battery is connected, independent of the ignition switch |
| 31 | Ground, battery negative |
| 50 | Starter solenoid feed, START position only |
| 85 | Relay coil, ground side |
| 86 | Relay coil, power-in side |
| 87 | Relay switched contact |
| D+ | Alternator warning light and field energising circuit |

These are the standard German (DIN) terminal designations: you'll see "Kl. 30", "Kl. 15" (*Klemme*, terminal) in German sources.

---

<figure class="p36-diagram">
<div class="p36-diagram-scroll">
<svg viewBox="0 0 760 300" role="img" aria-labelledby="ci-title ci-desc">
<title id="ci-title">A switched circuit and a relay with their terminal numbers</title>
<desc id="ci-desc">Left: battery positive, terminal 30, feeds a fuse, a switch and a load, which returns to ground, terminal 31. Right: a relay. The coil sits between terminal 86, power in, and 85, ground side. When the coil is energised, the contact connects terminal 30 to 87, which feeds the load.</desc>
<text class="d-title" x="30" y="32">Simple circuit</text>
<rect class="d-box" x="30" y="60" width="90" height="44" rx="8"/>
<text class="d-label" x="44" y="80">Battery +</text>
<text class="d-size" x="44" y="96">30</text>
<path class="d-vac" d="M120 82 H160"/>
<rect class="d-box" x="160" y="66" width="60" height="32" rx="6"/>
<text class="d-sub" x="190" y="87" text-anchor="middle">fuse</text>
<path class="d-vac" d="M220 82 H262"/>
<path class="d-vac" d="M262 82 L296 66"/>
<path class="d-vac" d="M300 82 H340"/>
<text class="d-sub" x="281" y="112" text-anchor="middle">switch</text>
<circle class="d-box d-main" cx="372" cy="82" r="28"/>
<text class="d-sub" x="372" y="86" text-anchor="middle">load</text>
<path class="d-vac" d="M372 110 V200"/>
<path class="d-mount" d="M352 200 H392 M358 208 H386 M364 216 H380"/>
<text class="d-label" x="400" y="210">ground</text>
<text class="d-size" x="400" y="226">31</text>
<text class="d-title" x="480" y="32">Relay</text>
<rect class="d-box d-main" x="480" y="50" width="250" height="210" rx="12"/>
<text class="d-sub" x="540" y="78" text-anchor="middle">power in (+)</text>
<text class="d-size" x="540" y="96" text-anchor="middle">86</text>
<rect class="d-box" x="510" y="106" width="60" height="76" rx="6"/>
<text class="d-sub" x="540" y="148" text-anchor="middle">coil</text>
<text class="d-size" x="540" y="204" text-anchor="middle">85</text>
<text class="d-sub" x="540" y="222" text-anchor="middle">ground side</text>
<text class="d-sub" x="660" y="78" text-anchor="middle">supply</text>
<text class="d-size" x="660" y="96" text-anchor="middle">30</text>
<path class="d-vac" d="M660 106 V128 L690 156"/>
<path class="d-vac" d="M694 162 V184"/>
<text class="d-size" x="694" y="204" text-anchor="middle">87</text>
<text class="d-sub" x="694" y="222" text-anchor="middle">to load</text>
<text class="d-note" x="30" y="284">Terminal numbers per Bentley 600, Table a (DIN). 15 is the ignition-switched feed (RUN and START).</text>
</svg>
</div>
<figcaption>How terminal numbers appear in a circuit: 30 always live, through fuse, switch and load to 31 ground. A relay's coil (86, 85) switches the heavy contact from 30 to 87.</figcaption>
</figure>

## Numbers on the diagram

Components, connectors, fuses and **ground points** each have their own identification number, which corresponds to that part throughout the diagrams. Ground points are numbered **G100, G101, G102…**, and their locations are listed in the [ground distribution guide](/guides/e36-ground-distribution-guide). Fuses are numbered as in the [fuse and relay reference](/guides/e36-fuse-relay-reference).

Most component terminals are also numbered on the part and on its connector, so the pin on the diagram is the pin you probe.

---

## Tracing a circuit, step by step

1. **Pick the right diagram** for the system, your model and build date.
2. **Start at the fuse** feeding the circuit: is it fed from 30 (always live) or 15 (ignition on)?
3. **Follow the wire** through switches, relays and connectors to the **load** (bulb, motor, module), noting colours and connector numbers.
4. **Follow it to ground**: which G-number, and where is it in the car?
5. **Test with the circuit live:** voltage at the load's supply, then a **voltage drop** test across switches, connectors and the ground. A good ground side reads close to 0 V.
6. **Test with the circuit dead:** continuity only with the **battery disconnected**.

Bentley's tool rules: use a **digital multimeter with at least 10 MΩ input impedance** or an **LED test light**. A bulb test lamp or an old analogue meter can draw enough current to damage control modules, and an ohmmeter must never be used on solid-state components such as control units.

---

## Safety

- Disconnect the battery before removing electrical components. That can erase stored fault codes, so read them first.
- **Airbag cars:** follow the airbag precautions before any electrical work near the system.
- Connect and disconnect connectors and test leads **only with the ignition off**.
- Use jumper wires with **flat-blade ends of the right size**, so you don't spread the terminals and create a new intermittent fault.
