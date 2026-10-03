---
title: "BMW M52 Engine Rebuild: A Complete Guide from Block to Head"
description: "Rebuilding the E36 M52: why the block type (Nikasil aluminium or iron) decides the machine work, what to inspect, the assembly order and only specs confirmed by Bentley or two independent sources."
pillar: engine
keywords: "BMW M52 rebuild, M52 engine guide, E36 M52 engine, M52 block rebuild, M52 head rebuild, M52 torque specs, E36 engine restoration"
date: "2026-06-22"
hero: "bmw-m52-engine-rebuild-guide.webp"
reviewed: "2026-10-03"
sources:
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998, 113, 116, 117, 119 (head, timing, lubrication torque values)"
  - title: "Wikipedia: BMW M52 (block versions, Nikasil, bore and stroke, single VANOS)"
    url: "https://en.wikipedia.org/wiki/BMW_M52"
  - title: "engine-specs.net and Brentford Racing: M5x connecting rod bolt procedure and rod bearing clearance"
    url: "https://brentfordracing.com/2020/08/21/bmw-e36-m50-s50-m52-s52-connecting-rod-bearing-replacement-upgrade/"
  - title: "Beisan Systems: single VANOS seal procedure"
    url: "https://beisansystems.com/single-vanos-6-cyl-e36-e34-e39/"
---

The M52 (E36 328i and 323i from 1995/96) is the M50's successor, and much of a rebuild is the same job. See the [M50 rebuild guide](/guides/bmw-m50-engine-rebuild-guide) for the general order of work. The big difference is the **block**, and it decides what machine work is even possible. This guide covers the M52-specific points.

**Specs policy:** Bentley's E36 manual covers the head, timing and lubrication, but not the crankshaft, bearings and pistons. Internal values not confirmed by two independent sources are marked **"check the workshop manual"**.

## TL;DR

| | |
| :--- | :--- |
| **What:** | Rebuilding an M52B25 or M52B28 long block. |
| **Why:** | Oil consumption, low compression, or a sound base for a swap. |
| **First step:** | Find out **which block you have**: Nikasil-lined aluminium or cast iron. |
| **Difficulty:** | 5/5 |

---

## Which block do you have?

| Version | Block |
|---|---|
| Most markets (early M52) | **Aluminium**, with **Nikasil**-coated bores |
| From 1998 | Aluminium with **cast-iron cylinder sleeves** (BMW's fix for the Nikasil problem) |
| Original US and Canadian cars (except the Z3) | **Cast iron**, carried over from the M50 |

| | M52B25 | M52B28 |
|---|---|---|
| Bore × stroke | 84 × 75 mm | 84 × 84 mm |
| VANOS | Single (intake) | Single (intake) |

**The Nikasil problem:** sulphur in fuel attacks the Nikasil coating. Many early M52s, and the V8 M60s with the same coating, suffered premature bore wear in markets with high-sulphur fuel. On a Nikasil block that is losing compression, the bores are the first suspect.

**Why it matters for the rebuild:** Nikasil is a thin hard coating on the aluminium, not an iron bore. It can't simply be bored to the next oversize like the M50's iron block. Before any machine work:

- establish which bore surface your block has
- go to a machine shop that works with coated bores
- if the coating is damaged, expect a re-coat, sleeves or a replacement block, not a quick hone

---

## Before teardown: diagnose

A **compression test and a leak-down test** before the engine comes out tell you what you are rebuilding for:

- low compression everywhere, with air escaping into the crankcase: rings or bores
- one or two low cylinders, with air at the intake, exhaust or coolant: valves or head gasket

Also inspect the usual M52 age items as you strip it: brittle cooling-system plastics, the crankcase vent valve and its hoses, the VANOS, and oil leaks around the oil filter housing.

---

## Bottom end

Machine-shop basics, as for the M50: chemical clean, crack inspection, deck check, bores measured. **On a Nikasil block, the bores decide the plan:** see above.

- **Rod bearing clearance:** 0.020–0.055 mm.
- **Main bearing clearance:** check the workshop manual.
- **New piston rings,** end gaps checked in their bores against the ring maker's specification.
- **Connecting rod bolts are stretch bolts:** fit new ones and tighten them as follows (threads and seats lightly oiled):

  | Stage | Value |
  |---|---|
  | 1 | 5 Nm |
  | 2 | 20 Nm |
  | 3 | +70° |

- **Main cap bolts:** torque plus angle. Check the workshop manual for the values and sequence.

**Oil pump and pan (Bentley):**

| Fastener | Torque |
|---|---|
| Oil pump to block (M8) | 22 Nm |
| Oil pump sprocket nut (M10×1, **left-hand thread**) | 25 Nm |
| Oil pan, M6 grade 8.8 / 10.9 | 10 / 12 Nm |

---

## Cylinder head and VANOS

- Pressure-test the head for cracks and check it for warpage. Bentley's limits: no more than **0.3 mm** may be removed, minimum height **139.7 mm** (140.0 new). A machined head needs the **0.3 mm thicker gasket**.
- A valve job, with new valve stem seals, is the norm.
- The M52 has **hydraulic lifters**. If the camshafts are removed, observe Bentley's waiting time before turning the engine: **10 minutes at 20 °C or above, 30 minutes at 10–20 °C, 75 minutes at 0–10 °C**.
- **Reseal the single VANOS** while the head is on the bench: Beisan's **BS011** kit. See the [M52 single VANOS guide](/guides/bmw-e36-m52-single-vanos-guide).

---

## Head, timing and front of the engine (Bentley)

| Item | Value |
|---|---|
| Head gasket | New, with **"OBEN"** facing up |
| Cylinder head bolts (new Torx stretch bolts, lightly oiled) | 30 Nm, +90°, +90°, in BMW's sequence |
| Head to lower timing cover | 10 Nm |
| Camshaft bearing caps (M7) | 15 Nm |
| Exhaust camshaft sprocket bolts (M7 Torx) | 5 Nm, then 22 Nm |
| Primary chain tensioner (M52) | 40 Nm |
| Crankshaft hub (new stretch bolt) | 410 ± 20 Nm |
| Flywheel (new bolts) | 105 Nm |

Timing is set with the crankshaft locking pin **11 2 300** and camshaft locking tool **11 3 240**. There are no reassembly marks on the camshafts. Confirm the timing by turning the engine through two full revolutions and refitting the tools. See the [timing chain guide](/guides/e36-m50-timing-chain-guide) for the critical points; the M52 procedure follows the same logic.

---

## First start

- **Prime the oil system** before the first start, so the bearings don't run dry.
- Fill with BMW-approved coolant, 50/50 with distilled water, and bleed the system (see the [cooling system guide](/guides/e36-cooling-system-overhaul)).
- Expect some valvetrain noise for the first moments while the hydraulic lifters and VANOS fill with oil. Watch oil pressure, temperature and leaks closely, and follow your ring maker's break-in advice.
