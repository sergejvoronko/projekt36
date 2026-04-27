---
title: "M50TU VANOS Rebuild Guide: Diagnosis, Teardown, and Seals Replacement with Part Numbers"
description: "A complete hands-on guide to diagnosing, tearing down, and rebuilding the M50TU single VANOS unit with OEM and aftermarket part numbers, EU pricing, and real torque specs. Written for E36 and E34 owners doing the job themselves."
pillar: engine
keywords: "M50TU VANOS rebuild, BMW VANOS seal replacement, E36 VANOS rattle fix"
date: "2026-04-27"
hero: "m50tu-vanos-rebuild-seals-replacement-guide.webp"
---

## TL;DR

- **What:** Full rebuild of the single VANOS unit fitted to the M50TU (and M52) engine, covering seals, o-rings, and the piston
- **Why:** Failed Teflon seals cause cold-start rattle, loss of low-end torque, and sluggish throttle response above 3,500 rpm
- **Cost:** €30–€80 DIY depending on kit choice; dealer assembly ~€400–€600 labour included
- **Time:** 4–6 hours first time; 2–3 hours if you've done it before
- **Difficulty:** 3/5 — patience-intensive but no specialist tools required beyond a spanner set and a seal driver or suitable socket

---

## What Is the M50TU VANOS and Why It Fails

The M50TU introduced BMW's first production VANOS (Variable Nockenwellen Steuerung) system in 1992. Unlike the later dual VANOS on the S50B32 or M54, this is a **single-cam, intake-only** system. A hydraulically actuated piston advances the intake camshaft up to 14° depending on oil pressure and engine load, improving low-end torque and idle quality without sacrificing top-end power.

The unit bolts onto the front of the cylinder head and is driven directly off the oil feed from the main gallery. It uses a helical-splined sleeve to translate axial piston movement into cam rotation — elegant, but entirely dependent on a set of Teflon sealing rings maintaining oil pressure across the piston lands.

**The failure mode is predictable.** The Teflon piston rings harden and shrink with heat cycling over 25+ years. Once they lose their interference fit against the bore, oil bypasses the piston and the system can no longer build or hold actuation pressure. You'll notice:

- A distinct metallic rattle on cold start that clears within 30–60 seconds (the classic VANOS rattle — oil pressure eventually forces partial sealing)
- Flat, lazy throttle response between 1,500–3,500 rpm
- A noticeable power step or surge above 4,000 rpm as you're now effectively running a fixed-cam profile at all times
- Occasional rough idle that smooths once the engine warms

On our project E36 328i with a late M50TU (built November 1993, 247,000 km), the rattle had been present for roughly two years before we addressed it. Compression and leakdown were fine — this was a pure VANOS issue.

---

## Parts, Kits, and What to Buy

You have three realistic options for the seal kit:

| Supplier | Part / Kit | Approx. Price (EU) | Notes |
|---|---|---|---|
| BMW OEM (seals only) | 11 36 1 440 142 (seal ring set) | €45–€60 | Teflon rings, o-rings, filter screen |
| Beisan Systems | BS003 | €55–€70 shipped | US-based, excellent quality, machined Teflon rings with tighter tolerance |
| Corteco / Elring | Various (ask by VIN) | €25–€35 | Lower quality Teflon, adequate for street use |

We used the **Beisan BS003 kit** on our build. The machined Teflon rings have a noticeably better surface finish than OEM, and the instructions are thorough. If you're sourcing locally in Germany or Austria, the OEM kit through a dealer parts counter is a perfectly respectable choice.

**Additional parts to have on hand:**

| Part | BMW Part Number | Price |
|---|---|---|
| Valve cover gasket set | 11 12 1 730 229 | €18–€25 |
| VANOS solenoid o-ring | 11 36 1 437 741 | €3–€5 |
| Intake cam sprocket bolt (stretch bolt — replace if removing) | 11 31 1 745 052 | €8–€12 |
| Copper crush washer (oil feed banjo) | 07 11 9 963 200 | €2 |

The cam sprocket centre bolt is technically a torque-to-yield fastener. BMW's official position is to replace it. In practice, many experienced builders reuse it if it's undamaged and they're not removing the sprocket from the cam — your call, but we replaced ours at €10.

---

## Teardown Procedure

Park the car with the engine cold — you need the oil to have drained back down and you do not want to burn yourself on the head.

**1. Remove the valve cover.** Ten M6 bolts, standard 10mm socket. The gasket on a car this age will likely stick; pry gently around the perimeter. Set it aside — if it tears, you have a new one ready.

**2. Position the engine at TDC on cylinder 1.** Rotate the crank clockwise (viewed from the front) using a 27mm socket on the crank bolt until the TDC mark on the crank pulley aligns with the pointer on the timing cover. Confirm by checking that both cam lobes on cylinder 1 are pointing upward and away from the followers (base circle contact). This step is non-negotiable — losing cam timing on reassembly means re-doing the whole job.

**3. Secure the camshafts.** BMW has a TDC alignment tool (BMW Special Tool 11 2 240) that locks both cams simultaneously. A good substitute is a pair of flat-bar timing locks cut to 24mm width from 3mm steel plate — dimensions are well-documented online. Do not skip locking the cams.

**4. Disconnect the VANOS oil lines.** There's a banjo fitting on the top of the VANOS body (14mm) and a hardline running to the solenoid. Have a rag ready — residual oil will drain.

**5. Unbolt the VANOS from the head.** Four M8 bolts on the mounting flange, 13mm. The unit comes forward as a complete assembly once the bolts are out. Note the alignment pin — don't lose it.

**6. Remove the intake cam sprocket bolt.** Counter-hold the cam using the timing lock (this is why you installed it). The bolt is right-hand thread. With the bolt out, the helical sleeve and piston assembly slide out of the VANOS body.

**7. Disassemble the piston.** The Beisan instructions walk through this clearly. The piston has a circlip retaining the inner sleeve — a pair of circlip pliers and patience. Once apart, the three Teflon rings and their expander o-rings are visible in their grooves.

---

## Seal Replacement and Inspection

With the piston disassembled on the bench, inspect the bore of the VANOS housing with a torch. You're looking for scoring or wear marks. Light haze is fine; deep scoring means the unit is worn beyond what seals alone will fix (rare, but it happens on high-mileage, oil-starved engines).

**Removing the old Teflon rings:** They're fragile and hardened — they'll often snap rather than stretch off. That's fine; you're replacing them. Clear the grooves completely and clean out any debris.

**Installing new Teflon rings:** This is the fiddly part. The rings need to be slightly compressed to fit into the bore. The Beisan kit includes a sizing sleeve — you seat the ring in the groove, then use the sleeve to compress it uniformly. Work one ring at a time. Let each ring relax for 5–10 minutes before installing the next. Trying to rush this causes the rings to seat unevenly, which replicates the original failure.

Replace all o-rings (inner piston o-ring, external body o-rings) with the new ones from the kit. The solenoid o-ring is tiny but important — a failed one here causes an oil leak at the solenoid boss and can contribute to inconsistent actuation.

**Lubrication:** Use clean engine oil on all o-rings and the piston bore before reassembly. No grease, no assembly lube — this system lives in engine oil.

---

## Reassembly and Torque Specs

Reassembly is the reverse of teardown with a few critical checkpoints:

| Fastener | Torque |
|---|---|
| Intake cam sprocket centre bolt | 20 Nm + 90° (angle tighten) |
| VANOS body to head (M8) | 22 Nm |
| Banjo bolt (oil feed) | 25 Nm |
| Valve cover bolts (M6) | 10 Nm |

**Before installing the VANOS back on the head**, manually cycle the piston through its full stroke by hand. It should move smoothly with moderate resistance from the new seals — not freely (that would indicate a seal isn't seated), and not so tight it requires force (check ring sizing).

Reinstall the helical sleeve onto the camshaft nose, engage the VANOS body, and start the four mounting bolts finger-tight. Confirm the alignment pin is seated before torquing down.

Reinstall the cam sprocket centre bolt. Apply a small amount of thread-locking compound (Loctite 243 or equivalent) to the first few threads. Torque to 20 Nm, then angle-tighten 90°. Remove the cam timing locks, confirm the crank is still at TDC, and rotate the engine two full turns by hand to check for binding before reinstalling the valve cover.

---

## First Start and Verification

Fill oil if needed, reconnect the battery, and start the engine **cold**. The critical test:

- **Cold start rattle:** Should be gone immediately or within the first two seconds of startup. If it persists beyond 5 seconds, the piston seals aren't holding — pull it and recheck ring seating.
- **Idle quality:** Should be smooth and stable from cold. The VANOS advances timing at idle to improve combustion stability; you'll notice a crisper idle if the system was badly degraded before.
- **Mid-range throttle response:** Take the car for a drive once at operating temperature. The flat spot between 1,500–3,500 rpm should be gone. On our E36 the difference was immediate and significant — noticeably stronger pull through the mid-range and a smoother power delivery to redline.

Check for oil leaks at the banjo fitting and solenoid o-ring after the first heat cycle.

---

## What's Next

A VANOS rebuild is often the first step in a broader top-end refresh. With the valve cover already off, it's worth checking bucket-style tappet clearances (M50TU spec: intake 0.25mm, exhaust 0.30mm cold) and inspecting the cam lobes for pitting. If you're chasing further performance on the M50TU, the next logical step is a camshaft upgrade — the Schrick 264° intake cam is a well-documented fitment that works well with the stock VANOS system and opens up noticeable gains above 4,500 rpm without sacrificing street manners.