---
title: "BMW E36 LCM — Light Control Module Explained"
description: "What the LCM does, which E36s have it, how it controls every light circuit, common failure modes, and how to code a replacement for your exact option list."
pillar: reference
keywords: "bmw e36 lcm, e36 light control module, e36 lighting module, lcm failure, e36 headlights"
date: "2026-04-13"
hero: "lcm.webp"
---

## TL;DR

The LCM (Lichtsteuermodul — Light Control Module) is the brain behind every exterior light on later E36s. It replaced simple relay-based lighting with a module that monitors bulb current draw, manages the lighting sequence, and stores fault codes for failed bulbs. When the LCM fails, you lose multiple lights simultaneously. When it's the wrong specification, your lights may behave incorrectly. Coding is required after replacement.

---

## Which E36s Have the LCM

Not all E36s have an LCM. Earlier cars used conventional relay-based lighting:

| Production period | Lighting control |
|---|---|
| 1990–1994 (early E36) | Direct relay control, no LCM |
| 1994–1996 (transition) | LCM introduced progressively by market |
| 1996–1999 (post-facelift) | LCM standard on most markets |

The easiest way to confirm: look in the fuse box area for a sealed module with a large multi-pin connector, or check INPA — if LCM appears as a module in the vehicle list, it's present.

Schema 4 of the ETM (Exterior Lighting) shows whether your car routes lighting through an LCM or directly through relays.

---

## What the LCM Controls

The LCM handles every exterior light output:

- Dipped (low) beams — left and right independently
- Main (high) beams — left and right independently
- Parking/side lights — front and rear
- Tail lights
- Front fog lights (if equipped)
- Rear fog light
- Turn signals — front, rear, side repeaters
- Number plate lights
- Trailer socket (if equipped)

For each output, the LCM:
1. Receives a **command** from the light switch or indicator stalk
2. **Switches the output** via an internal transistor or relay
3. **Monitors current draw** on the circuit
4. **Stores a fault code** if current is abnormal (too low = bulb blown, too high = short circuit)

This is why INPA can tell you "left front turn signal open circuit" even before you check — the LCM measured the fault and logged it.

---

## LCM Variants and Option Coding

The LCM isn't a single part number — different specifications exist for different option combinations:

| Option | Effect on LCM |
|---|---|
| Xenon headlights | Different control circuit; LCM must be coded for Xenon |
| Bi-xenon / AFS | Additional output for leveling motor |
| Fog lights | LCM must know fogs are fitted to activate the output |
| Trailer tow | LCM includes trailer turn signal logic (load detection) |
| US spec (DRL) | Daytime running lights logic differs from European |

A replacement LCM must either:
1. Have the same option specification as the original, or
2. Be recoded with NCS Expert to match your car's options

**Running a Xenon-coded LCM with halogen headlights** (or vice versa) will result in lighting faults, incorrect current monitoring thresholds, and permanent warning lights.

---

## How the LCM Monitors Bulbs

Each output circuit has a measured **expected current range**. For a standard halogen H7 headlight (55W at 12V = ~4.6A), the LCM expects roughly 4–5A. If it measures less than ~2A, it flags an open circuit (blown bulb). If it measures more than 7–8A, it flags a short.

**This makes the LCM sensitive to substitutions:**

- Installing LED bulbs in LCM-controlled circuits without a load resistor will trigger permanent "bulb failure" faults — LEDs draw a fraction of the current of halogens.
- Installing high-wattage aftermarket bulbs (80W vs stock 55W) may trigger overcurrent protection and blow the LCM's internal transistor for that circuit.
- Poor ground connections at the headlight housing change the apparent current draw and cause false fault codes.

---

## Common LCM Failures

### 1. Internal transistor failure (most common)

The LCM switches each output using high-current transistors (or MOSFETs). These fail with age and thermal stress. When one fails:
- That output circuit stops working entirely
- INPA shows a continuous fault for that circuit
- No other symptoms

A failed transistor for the left headlight means only the left headlight is dead. The right works normally.

**Fix:** Replace the LCM. In rare cases, electronics specialists can reflash or replace the transistor on the PCB, but LCM units are inexpensive enough (€30–80 used) that replacement is usually more sensible.

### 2. Corrosion of the connector

The LCM sits in the engine bay and is exposed to moisture. The main connector corrodes — especially the ground pins and output pins. This causes intermittent lighting faults that come and go with temperature.

**Fix:** Remove the connector, clean all pins with electrical contact cleaner, apply dielectric grease, reseat.

### 3. Coding mismatch after replacement

A replacement LCM from a different-spec car (different market, different options) will have different coding. The old coding doesn't transfer automatically. You must use NCS Expert to write the correct coding for your car.

**Symptom of mismatch:** Fog lights that don't activate, DRL behaviour incorrect, turn signal timing wrong, permanent fault codes for equipment that isn't fitted (or should be).

---

## Replacing the LCM

**Location:** Engine bay, driver's side. On the E36 it's typically mounted near the fuse box or on the inner wing, with a large waterproof connector.

### Procedure

1. Disconnect battery negative
2. Locate LCM — trace the main lighting wiring to the module
3. Release connector lock and unplug the large connector
4. Remove mounting bolts (usually 2–3)
5. Install replacement
6. Connect battery
7. **Code the replacement** before testing

### Coding with NCS Expert

1. Connect K-DCAN cable, open NCS Expert
2. Select vehicle: E36, select LCM from module list
3. **Read current coding first** — save the .NCS file as a backup
4. Edit the coding to match your car's options:
   - `XENON` or `HALOGEN` for headlight type
   - `NEBEL_VOR` for front fog (yes/no)
   - `NEBEL_HINT` for rear fog (yes/no)
   - `AHK` for trailer hitch (yes/no)
   - Check market-specific options (US/EUR)
5. Write the coding back to the LCM
6. Test all lights

---

## LCM and Aftermarket Lights

If you're retrofitting non-standard lights (aftermarket projectors, Angel Eyes, LED upgrades), the LCM interaction changes:

**Angel Eye / CCFL rings (halogen cars):** Connect to the parking light circuit. The LCM monitors current on this circuit — if the CCFL draws less current than a standard parking bulb, add a parallel resistor to maintain the expected load.

**LED headlight conversions:** Require either:
- A load resistor on each output to simulate halogen current draw
- An LCM coding change to reduce the current threshold (not always possible)
- An LCM bypass/delete (removes monitoring entirely — not recommended for road use)

**Projector retrofits into original housings:** The LCM doesn't care what's inside the housing as long as current draw is within expected range. H7 projector with H7 bulb = same current = no LCM issues.

---

## Reading LCM Fault Codes

With INPA → LCM:

| INPA Fault | Meaning | First check |
|---|---|---|
| Low beam left open circuit | Left low beam bulb blown or disconnected | Bulb, bulb holder, connector at headlight |
| Low beam right short circuit | Overcurrent on right low beam | Wiring chafing, water in headlight housing |
| Turn signal front right open | Right front turn bulb blown | Bulb, parking light/turn signal combination bulb |
| Tail light left open | Left tail light bulb blown | Bulb in tail cluster |
| Number plate light open | Either number plate bulb blown | Bulb(s), check both if two-bulb setup |

**The LCM stores faults permanently until cleared.** A fault from a bulb that was replaced a week ago may still show in INPA until you clear it. Always clear faults after completing repairs and recheck.

---

## Quick Troubleshooting Table

| Symptom | Likely cause |
|---|---|
| One specific light circuit dead, all others work | LCM transistor failure for that circuit |
| Multiple unrelated lights intermittent | LCM connector corrosion or ground fault at G200 |
| Lights work but INPA shows bulb faults | LED conversion without load resistors |
| All lights dead | LCM fuse blown, LCM power supply fault, or battery issue |
| Turn signals work but LCM logs fault | Incorrect bulb wattage in one socket |
| Lights come on with wrong combination | Coding mismatch on replacement LCM |
