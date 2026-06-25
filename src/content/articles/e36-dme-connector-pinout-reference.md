---
title: "BMW E36 OBD1 Wiring Pinout Reference: DME Connector, Sensor Wires, and Diagnostic Port Explained"
description: "A complete pinout reference for the BMW E36 DME connector covering OBD1 M50/M52 sensor wiring, diagnostic port signals, and common fault traces. Written for mechanics and builders doing E36 engine swaps, harness repairs, or standalone ECU work."
pillar: reference
keywords: "BMW E36 DME pinout, M50 ECU connector wiring, E36 OBD1 sensor wiring reference"
date: "2026-05-18"
hero: "e36-dme-connector-pinout-reference.webp"
---

## TL;DR

- **What:** Full pin-level wiring reference for the BMW E36 OBD1 DME (Motronic M3.1 / M3.3) 88-pin connector and the 20-pin OBD1 diagnostic port
- **Why:** Factory ETK diagrams are scattered, out of print, or trapped behind paywalls — this consolidates what you actually need for diagnostics and harness work
- **Cost:** N/A (reference article)
- **Time:** N/A
- **Difficulty:** 3/5 — straightforward to read, but harness work on a 25-year-old E36 demands patience and a quality multimeter

---

## Background: which DME are we talking about?

The E36 ran two generations of Bosch Motronic on the six-cylinder cars before the swap to OBD2:

| Engine | DME Version | ECU Part Number (example) | Production Years |
|---|---|---|---|
| M50B20 / M50B25 (non-VANOS) | Motronic M3.1 | 0 261 200 557 | 1990–1992 |
| M50B20TU / M50B25TU (VANOS) | Motronic M3.3 | 0 261 203 220 | 1992–1995 |
| M52B20 / M52B28 (early) | Motronic M5.2 | 0 261 204 402 | 1995–1998 |

This article focuses on **M3.1 and M3.3** — the OBD1 units used in the 1990–1995 cars. The 88-pin Bosch connector is physically identical across both; pin assignments are essentially the same with M3.3 adding VANOS solenoid control on a previously unused pin. M5.2 moves to a different connector scheme and is covered separately.

The harness plug itself is BMW part **61 12 1 393 443** (female housing, 88-pin, grey). Replacement terminals are sold individually as **61 13 0 005 198** — expect to pay €0.80–€1.50 per terminal from a BMW dealer or around €0.40 each via APA or Hella trade accounts.

---

## The 88-pin DME connector: full pinout

The connector is keyed and reads left-to-right, top row first, when viewed from the wire side (ECU unplugged, looking into the harness plug). Rows are 32 / 32 / 24 pins.

### Power and ground (rows a & b, selected pins)

| Pin | Signal | Wire Colour (factory) | Notes |
|---|---|---|---|
| 1 | Main relay switched B+ | Red/White | 12V after main relay closes |
| 2 | Main relay switched B+ | Red/White | Redundant feed; both must be present |
| 3 | Ground — ECU logic | Brown | Direct to body earth stud |
| 4 | Ground — ECU logic | Brown | Redundant ground; both must measure <0.1Ω to chassis |
| 5 | Ignition switch terminal 15 | Red/Yellow | ECU wake-up; 12V with key on |
| 6 | Ground — power stage | Brown/Black | Injector return ground; keep separate from logic ground |
| 19 | Fuel pump relay trigger | Brown/Green | ECU pulls low to energise relay |
| 20 | Main relay trigger | Brown/Yellow | ECU pulls low; relay closes ~1s after key-on |

**On a 25-year-old E36:** Pins 3 and 4 are the single most common source of intermittent misfires and false fault codes. Both grounds run through the same loom section that passes over the back of the cylinder head — heat cycling cracks the insulation. Measure resistance to chassis with the connector unplugged and probing the pin directly; anything above 0.2Ω warrants a replacement ground wire.

### Sensor inputs

| Pin | Signal | Expected Value (key on, engine cold) | Notes |
|---|---|---|---|
| 18 | Coolant temp sensor (NTC) | 2.2–2.8V at 20°C | Dual-pin sensor; return on Pin 17 |
| 17 | Coolant temp sensor ground | 0V (signal ground) | Not chassis ground — isolated inside ECU |
| 26 | Intake air temp sensor | 2.2–2.8V at 20°C | Same NTC curve as coolant sensor |
| 25 | Air temp sensor ground | 0V (signal ground) | |
| 27 | Throttle position sensor (TPS) — wiper | 0.4–0.6V at idle | Linear pot; 4.5V at WOT |
| 28 | TPS reference voltage | 5.0V | ECU-supplied; probe to verify 5V rail intact |
| 29 | TPS ground | 0V (signal ground) | |
| 7 | Mass air flow sensor — signal | 1.0–1.2V at idle | Bosch hot-film MAF; frequency output on M3.1, voltage on M3.3 |
| 8 | MAF ground | 0V | |
| 9 | MAF supply voltage | 12V | |
| 10 | Crankshaft position sensor (CKP) — signal + | AC waveform | 60-2 trigger wheel; ~0.5V AC at 200 RPM |
| 11 | CKP signal − | AC waveform return | Differential pair — do not ground |
| 16 | Camshaft position sensor (CMP) | 5V square wave | Hall effect on VANOS cars; single wire + ground |
| 15 | CMP ground | 0V | |
| 30 | Knock sensor 1 | AC signal ~0–5V | Piezo; wiring must be shielded, shield to Pin 31 |
| 31 | Knock sensor 1 shield | 0V | |
| 32 | Knock sensor 2 | AC signal ~0–5V | Rear bank |

**Tip for swap builds:** In our M50B25TU swap into a Z3 shell, the CMP sensor wiring had been extended by a previous owner using unshielded speaker wire. The result was intermittent cam signal dropout above 5,000 RPM. Always use twisted shielded pair (Belden 8761 equivalent, ~€1.20/m) for the CMP and CKP extensions.

### Injector and actuator outputs

| Pin | Signal | Notes |
|---|---|---|
| 33 | Injector 1 | ECU low-side switch; B+ supplied by injector wiring at top |
| 34 | Injector 2 | |
| 35 | Injector 3 | |
| 36 | Injector 4 | |
| 37 | Injector 5 | |
| 38 | Injector 6 | |
| 45 | Idle control valve (ICV) — coil A | PWM output; 100–200 Hz at idle |
| 46 | ICV — coil B | |
| 47 | VANOS solenoid | M3.3 only; B+ switched, ECU grounds to activate |
| 55 | Purge valve (EVAP) | PWM; ECU low-side |

### Ignition outputs

| Pin | Signal | Notes |
|---|---|---|
| 48 | Ignition coil 1 (cyl 1 & 6) | ECU triggers power stage module |
| 49 | Ignition coil 2 (cyl 2 & 5) | |
| 50 | Ignition coil 3 (cyl 3 & 4) | |

The coil trigger wires go to the **external power stage (ZAE)** module — BMW part **12 14 1 742 185** (Bosch 0 227 400 128), current replacement approximately €65–€90 from ECP or TRW. Do not probe these outputs with a standard test light; use a 10MΩ probe only or a dedicated ignition scope lead.

---

## The OBD1 diagnostic port (round 20-pin)

The E36 OBD1 diagnostic port is a round 20-pin circular connector located in the engine bay near the fusebox. It is **not** OBD2-compatible. Communication is via BMW's proprietary DS2 protocol at 9,600 baud on a single K-line wire.

| Pin | Signal |
|---|---|
| 1 | Ground |
| 2 | K-line (DME) |
| 3 | K-line (ABS/ASC) |
| 7 | Battery voltage (for tester power) |
| 11 | K-line (EWS / immobiliser) |

To communicate with the DME using a modern interface, you need a **K+DCAN USB cable** (commonly sold as INPA cable, ~€15–€25 on Amazon.de) plus **INPA/Ediabas** or **NCSExpert** on Windows. The BMW-specific cable uses the round-to-OBD2 adapter that ships with the cable — the adapter is not electrically OBD2, just physically convenient.

**Fault code reading via LED blink (emergency method):** With no scan tool, bridge Pin 7 to Pin 20 and cycle ignition. The MIL will blink fault codes in a 3+1 digit pattern. This only works for DME codes — ABS and EWS have separate K-lines.

---

## Common wiring faults and how to trace them

These are the failure modes we see repeatedly on E36 harnesses that are 25–30 years old:

**1. High resistance injector returns**
Injectors share a common B+ rail through a single fusible link (10A, green, in the fusebox). If that link shows more than 0.3V drop under cranking, replace it. The link is available as **61 13 1 378 144** (~€3).

**2. MAF signal drift**
The MAF connector (3-pin AMP Junior Power Timer) corrodes and introduces resistance on the signal wire. Clean with DeoxIT D5 or replace the connector. The female connector housing is **61 13 0 007 867**; terminals are **61 13 0 005 198** (same as DME terminals).

**3. Coolant sensor ground contamination**
Because the coolant sensor shares a signal ground plane with the TPS and IAT inside the ECU, a leaking sensor that introduces coolant into the connector contaminates all three sensor readings simultaneously. If you get simultaneous TPS, IAT, and CLT faults, inspect the coolant sensor plug first. Replacement sensor (Wahler or Febi): **13 62 1 433 077**, approximately €8–€12.

**4. EWS / DME synchronisation loss**
On 1995+ cars with EWS2, the EWS module communicates with the DME over a separate CAN-style wire (not the K-line). Fault code 82 (EWS tamper) after a battery replacement means the synchronisation has been interrupted. Re-sync using NCSExpert or a dealer scan tool — not fixable with a code reader alone.

---

## Using this reference for standalone ECU work

If you're deleting the factory harness in favour of a standalone ECU (Speeduino, MegaSquirt MS3, or Haltech Nexus R5), this pinout gives you the signal source locations. Key points:

- The **CKP sensor output is differential AC** — most standalone ECUs expect this on a dedicated differential input. Do not convert to single-ended without a proper differential buffer (e.g., LM1815 circuit).
- The **MAF is unnecessary** on a MAP-based standalone tune. The MAF wiring can be repurposed for a wideband lambda signal if the routing is convenient.
- The **VANOS solenoid (Pin 47)** is a simple on/off solenoid, not a PWM device on M3.3. It opens at a fixed RPM/load threshold. Any standalone ECU with a spare switched output can drive it via a flyback diode.
- Factory **coil packs are wasted-spark** — pairs 1/6, 2/5, 3/4. Keep this pairing if reusing the factory coils with a standalone ignition driver.

Bosch connector tool set for 88-pin DME service (extraction and insertion): look for the **Bosch 1 684 463 281** terminal removal tool, sold by specialist tool suppliers for approximately €18–€25.

---

## What's next

If you're here because you're chasing a specific fault code, cross-reference the pin assignments above with the BMW ISTA fault code definitions — codes 0x012A (coolant sensor) and 0x0158 (CKP signal) account for a large proportion of E36 no-start calls. For harness repair beyond terminal-level work, see our E36 engine harness refresh guide, which covers full loom re-pinning with OEM-spec GXL wire and correct gauge selection by circuit type.