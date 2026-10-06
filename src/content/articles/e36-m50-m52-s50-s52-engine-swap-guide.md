---
title: "BMW E36 M50/M52 to S50/S52 Engine Swap: The Definitive Guide"
description: "Swapping a US-spec E36 M3 engine (S50B30US or S52B32) into a 325i or 328i: what the engines are, which DME and gearbox belong to each, and the decisions that decide how hard the swap is."
pillar: swap
keywords: "E36 S50 swap, E36 S52 swap, M50 to S50 conversion, M52 to S52 conversion, BMW E36 engine swap, S50/S52 wiring, E36 S50 parts list, E36 S52 cooling adaptation"
date: "2026-06-12"
hero: "e36-m50-m52-s50-s52-engine-swap-guide.webp"
reviewed: "2026-10-03"
sources:
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998 (engine management and transmission applications)"
  - title: "Wikipedia: BMW S50 (S50B30US)"
    url: "https://en.wikipedia.org/wiki/BMW_S50"
  - title: "Wikipedia: BMW S52"
    url: "https://en.wikipedia.org/wiki/BMW_S52"
---

The North American E36 M3 engines, the **S50B30US** and **S52B32**, are close relatives of the M50 and M52 in the 325i and 328i. That shared base is what makes them popular swaps into non-M E36s. This guide covers what they are and the decisions that decide how hard the swap is.

## TL;DR

| | |
| :--- | :--- |
| **What:** | Putting a US-spec M3 engine into a 325i or 328i. |
| **Why:** | 240 hp from a six-cylinder that shares most of its architecture with the M50/M52. |
| **The big decision:** | Matching the engine's electronics generation (OBD1 or OBD2) to the car's. |
| **Difficulty:** | 4/5 |

---

<figure class="p36-photo">
<img src="/images/commons/bmw-s50b32-vanos.webp" alt="BMW S50B32 engine with its double-VANOS unit at the front of the cylinder head" loading="lazy" decoding="async">
<figcaption>The S50B32 from the later E36 M3, with its double-VANOS unit on the front of the cylinder head.<span class="p36-credit">Photo: Buschtrommler, <a href="https://creativecommons.org/licenses/by-sa/4.0" rel="license noopener" target="_blank">CC BY-SA 4.0</a>, via <a href="https://commons.wikimedia.org/wiki/File:BMW_S50B32_Vanos.jpg" rel="noopener" target="_blank">Wikimedia Commons</a></span></figcaption>
</figure>

## The engines

| | S50B30US | S52B32 |
|---|---|---|
| Displacement | 2,990 cc | 3,152 cc |
| Bore × stroke | 86.0 × 85.8 mm | 86.4 × 89.6 mm |
| Power | 240 hp | 240 hp |
| Torque | 305 Nm | 320 Nm |
| Block | Cast iron | Cast iron |
| Years | 1994–1995 | 1996–2000 |
| Closest relative | M50 | M52 (single VANOS) |
| Engine management (Bentley) | Bosch DME M3.3.1 (OBD1) | Siemens MS41.1 (OBD2) |
| Manual gearbox in the M3 (Bentley) | ZF S5D 310Z | ZF S5D 320Z |

These **US engines** are different from the European S50B30/S50B32, which are far more complex engines and a different swap altogether.

---

## Match the electronics generation

| Swap | What it means |
|---|---|
| **S50B30US into an OBD1 325i (M50)** | Same electronics generation and the same DME family as an M50TU (Bosch M3.3.1). The closest to a like-for-like swap: use the S50's own engine harness and DME. |
| **S52B32 into an OBD2 328i (M52)** | Same generation: Siemens MS41.1 on both. Use the S52's harness and DME. The immobiliser (EWS) pairing between DME, module and keys has to be dealt with. |
| **S52B32 into an OBD1 car** | Mixing generations. Running an S52 on OBD1 electronics is a known enthusiast route, but it needs adapted sensors and wiring and, above all, a **DME tune made for the engine**. Follow a supplier's documented conversion and tune rather than improvising. |

Whatever the combination, treat the immobiliser first. See the [EWS guide](/guides/e36-ews-immobilizer-guide).

---

## Before it goes in

The donor engine is 25-plus years old. While it's on a stand:

- **Compression and leak-down test** before buying, or at least before installing
- reseal it: oil pan, rear main seal, oil filter housing, valve cover
- **reseal the VANOS** (S52: Beisan's single-VANOS kit; see the [M52 single VANOS guide](/guides/bmw-e36-m52-single-vanos-guide))
- refresh the cooling system: see the [cooling system overhaul](/guides/e36-cooling-system-overhaul)
- consider new crankshaft and camshaft sensors while they are easy to reach

Part numbers: look them up by the **donor engine's** VIN on [RealOEM](https://www.realoem.com/).

---

## Drivetrain

- **Gearbox:** the M3s used ZF five-speeds (S5D 310Z with the S50US, S5D 320Z with the S52). A 325i's Getrag S5D 250G bolts to the engine, since the bolt pattern is shared, but it was never paired with this torque at the factory. See the [gearbox guide](/guides/e36-gearbox-selection-swap).
- **Driveshaft:** the front section must match the gearbox make (Getrag or ZF).
- **Clutch and flywheel:** use parts matched to the engine and gearbox you end up with.

---

## Exhaust, intake, cooling

- Use the **M3's exhaust manifolds** and a matching downpipe and mid-pipe. On OBD2 cars, keep every oxygen sensor the system expects.
- The S52 accepts the same **M50 intake manifold** upgrade as the M52. See the [M50 manifold guide](/guides/bmw-e36-m50-manifold-conversion-guide).
- The cooling system needs to be in perfect condition; the radiator suitable for the car's engine bay and the use.

---

## After the swap

With roughly 50 hp more than a 325i, the **brakes** and **suspension** should match the engine. The registration inspection may also expect it.
