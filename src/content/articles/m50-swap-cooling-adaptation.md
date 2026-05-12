---
title: "M50 Swap Cooling Adaptation: Radiator, Thermostat Housing, and Expansion Tank Explained"
description: "A hands-on guide to adapting the cooling system when swapping an M50 into an E36 M43 chassis. Covers radiator fitment, thermostat housing differences, expansion tank routing, and the parts you'll actually need."
pillar: swap
keywords: "M50 swap cooling system, E36 M50 radiator fitment, M43 to M50 cooling adaptation"
date: "2026-05-11"
hero: "m50-swap-cooling-adaptation.webp"
---

## TL;DR

- **What:** Cooling system adaptation required when swapping an M50 into an E36 originally fitted with an M43
- **Why:** The M50 runs higher coolant volume, different thermostat housing geometry, and incompatible expansion tank routing versus M43
- **Cost:** €180–€420 depending on whether you reuse the original radiator
- **Time:** 4–8 hours alongside the engine swap
- **Difficulty:** 3/5

---

## Why the M43 Cooling Setup Doesn't Just Bolt Over

The M43 is a compact four-cylinder with modest cooling demands. BMW specced the E36 318i/316i cooling system accordingly — smaller radiator cross-section, a single-row plastic-tank aluminium core on most 1993–1998 examples, and an expansion tank mounted high on the passenger-side strut tower with a relatively simple overflow circuit.

The M50 (and its VANOS-equipped sibling, the M50B25TU) is a 2.5-litre inline-six producing significantly more heat. It also runs a different thermostat housing — a larger, more complex casting that points the main coolant outlet toward the driver's side and incorporates a bleed port that the M43 system simply doesn't account for. If you bolt an M50 into an M43 E36 and connect whatever coolant hoses reach, you'll likely end up with chronic air pockets, thermostat confusion, and a car that runs hot within 20 minutes.

The three problem areas are: radiator capacity and fitment, thermostat housing outlet geometry, and expansion tank location and bleed line routing. Each one is solvable, and none of them require fabrication if you source the right donor parts.

---

## Radiator: What Fits, What Works, What to Buy

The E36 325i/328i radiator is the direct bolt-in solution. It uses the same mounting points as the 318i unit, fits within the same core support dimensions, but has a larger core — typically 53 mm depth versus 32 mm on the M43 application — and higher flow capacity appropriate for the M50.

**BMW OEM part numbers (for reference):**

| Application | OEM Part Number | Core Size | Notes |
|---|---|---|---|
| E36 318i (M43) | 17111723469 | 540×322×32 mm | Original fitment, undersized for M50 |
| E36 325i/328i (M50/M52) | 17111723470 | 540×322×53 mm | Correct swap fitment |
| E36 M3 (S50/S52) | 17111723833 | 540×322×60 mm | Overkill but fits cleanly |

Aftermarket aluminium replacements from Nissens (ref. **60673A**, ~€95–€115 from Autodoc or GSF) or Mahle (ref. **CR 253 000P**, ~€105–€130) are reliable and often better long-term value than OEM on a 25-year-old car. Both are direct fitments for the 325i/328i and will accept the M50 top and bottom hoses without modification.

In our M50 swap build, we used a Nissens 60673A sourced from Autodoc for €98. It arrived with both plastic tanks pre-fitted and needed only a transfer of the original drain plug from the M43 unit. Install time was under 30 minutes once the engine was in.

**One watch-out:** Check the lower radiator hose outlet diameter. The M43 radiator uses a 38 mm outlet; the M50/M52 radiator uses a 40 mm outlet. The lower hose from the M50 engine (BMW 11531709851 or equivalent) is sized for the 40 mm outlet, so if you're mixing parts from different donors, verify this before you clamp anything.

---

## Thermostat Housing: The Geometry Problem

This is where most first-time M50 swappers get caught out. The M43 thermostat housing is a simple casting on the front of the head, outlet pointing roughly upward toward the top radiator hose. The M50 thermostat housing (BMW part **11531740478** for the B25 non-VANOS, **11531743229** for the M50TU/VANOS) is a more involved piece — larger, with the main outlet rotated toward the driver's side of the engine bay, and with a dedicated bleed nipple on the upper face.

If you're doing a clean swap and pulling the complete engine ancillaries from an E36 325i donor, you likely have all of this already. The problem arises when the engine comes from an E34 or E30 donor, or when someone has mixed housings trying to make things fit. E34 M50 thermostat housings are dimensionally similar but the hose connections route differently for the longer engine bay, and the bleed port location changes.

**Always use the E36 M50 thermostat housing, not the E34 version.** They're not interchangeable without hose rerouting, and the E34 unit typically lacks the upper bleed nipple that the E36 system relies on to purge air from the heater circuit.

Thermostat spec: BMW specifies a **88°C opening thermostat** for the M50 in standard road use. Part number **11531740478** includes the housing; the thermostat element alone is **11531721003** (Wahler or Mahle OE-equivalent ~€12–€18). Don't fit a 92°C thermostat — it's common advice on forums and it's wrong for street use. The M50's VANOS solenoid on the TU variant is coolant-temperature-dependent and needs the ECU to see a proper warm-up curve.

---

## Expansion Tank: Location, Routing, and the Bleed Line

This is the detail that gets skipped and causes the most post-swap headaches. The M43 expansion tank is mounted on the passenger-side strut tower brace area, slightly aft. The M50 system requires the expansion tank to be mounted **higher** — specifically, it must be the highest point in the cooling circuit to allow passive air purging. In an E36 M50 shell, BMW positioned it at the correct height; in an M43 shell, the stock tank mounting point is marginally lower than ideal.

The practical fix: use the E36 325i/328i expansion tank (BMW **17137787039**, ~€28–€45 OEM, or a Febi/Bilstein equivalent at ~€14–€22) and relocate it to use the upper mounting position on the strut tower. On most E36 M43 chassis, there are pre-drilled mounting points or sufficient flat surface to mount the tank 40–60 mm higher than the M43 original position. If the holes aren't there, two M6 bolts into the strut tower brace plate is a half-hour job with a drill.

**The bleed line is non-negotiable.** The M50 thermostat housing has a 6 mm bleed nipple on its upper face. This connects via a small-bore hose directly to the expansion tank cap neck — not to the main coolant circuit, but to the overflow/bleed port on the tank cap. If this line is missing or blocked, you will trap air in the top of the engine and the car will overheat on the motorway regardless of how good your radiator is.

| Connection Point | Hose ID | Route |
|---|---|---|
| Thermostat housing bleed nipple | 6 mm | Forward to expansion tank bleed port |
| Top radiator hose | 40 mm | Thermostat housing main outlet → radiator top |
| Bottom radiator hose | 40 mm | Radiator outlet → water pump inlet |
| Heater return | 19 mm | Rear of head → heater valve → firewall |
| Expansion tank main feed | 19 mm | Radiator header tank → expansion tank lower |

Hose sets from ECS Tuning or Turner Motorsport come pre-cut for E36 M50 fitment and cost €45–€85 for a full set. Alternatively, Gates or Dayco bulk hose cut to length works fine — just confirm ID sizes before ordering.

---

## Heater Circuit and Rear Head Bleed

One more detail worth covering: the M50 has a heater return port at the rear of the cylinder head, and a second small bleed nipple near the intake manifold area depending on variant. Neither of these exists on the M43, so if you're building the cooling circuit from scratch, don't overlook them.

The rear head port feeds coolant through the heater core and back to the water pump inlet via the heater control valve (BMW **64118375443** or equivalent, ~€25–€40). If this circuit isn't connected, you'll have a heater that blows cold in winter — obvious — but more importantly, you'll have a dead-end pocket at the rear of the head that won't purge and will give you false overheating symptoms.

On a 25-year-old E36, if the heater valve is original, replace it during the swap. They're a £25 part and a €200 job if they fail with a freshly installed M50.

---

## Bleeding the System After Fill

Once everything is plumbed, filling and bleeding the M50 system correctly takes about 45 minutes. Use BMW coolant (blue, **82141467704**) at 50/50 concentration with distilled water — do not use universal green antifreeze, it's incompatible with the aluminium castings and VANOS seals.

Procedure:
1. Fill from expansion tank slowly until coolant reaches the MIN mark
2. Crack the bleed nipple on the thermostat housing — leave open until bubble-free coolant flows
3. Close nipple, top up tank to MAX
4. Start engine, run to operating temp with heater set to max heat
5. Watch for bubbles returning to expansion tank — normal for 5–10 minutes
6. Once thermostat opens (temp gauge settles), recheck level and bleed nipple
7. Allow to cool fully, recheck cold level

If the car runs hot or the gauge spikes before the thermostat opens, there's an air lock — most likely the bleed nipple hose isn't connected or is kinked.

---

## What's Next

With cooling sorted, the next system to address in a thorough M50 E36 swap is the intake and throttle body adaptation — particularly if you're running an M43 airbox location or if the E34-sourced engine has a different MAF diameter. We'll cover that in the next swap guide, including the AFM to MAF conversion for Motronic 3.3 versus 3.1 variants.

If you're cross-referencing this with our E36 M50 swap master guide, cooling is Step 6 — once this is signed off, you're clear to do a first-start coolant fill and begin the engine management commissioning phase.