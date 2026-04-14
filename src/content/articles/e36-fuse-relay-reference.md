---
title: "BMW E36 Fuse & Relay Reference — Complete Box Guide"
description: "Complete BMW E36 fuse box map: every position, amperage rating, and circuit — plus how to find an unlabelled blown fuse."
pillar: reference
keywords: "bmw e36 fuse box, e36 fuse chart, e36 relay guide, e36 fuse locations, bmw e36 fuse diagram"
date: "2026-04-13"
hero: "fuse-relay.webp"
---

## TL;DR

The E36 fuse box is on the left side of the engine bay, under a cover. There's a secondary fuse strip in the boot for trailer/audio circuits, and individual high-current fuses near the battery. The lid of the fuse box has a basic diagram, but it's faded and cryptic on any 30-year-old car. This guide gives you the complete map.

---

## Fuse Box Location

**Main fuse box:** Engine bay, driver's side (left), against the firewall. Lift the plastic cover. The box contains a mix of blade fuses (ATO/ATC type) and relays.

**Secondary fuses:** Some circuits have inline fuses or standalone fuse holders near the battery or in the boot. The fuel pump circuit often has an inline fuse. Audio amplifier installations frequently add their own fused feed here.

**High-current fuses:** Next to the battery, there may be a maxi-fuse or fusible link for the main feed to the fuse box. On some E36s this is a 60A or 80A fusible link — if this blows, nothing works.

---

## Fuse Layout Reference

Fuse positions vary slightly between production years (pre-facelift 1993–1995 vs post-facelift 1996–1999) and market specifications. The table below covers the most common 1993–1999 E36 layout. Always cross-reference with the ETM Schema 1 for your specific build date.

<img src="/images/e36-fuse-box-diagram.svg" alt="BMW E36 fuse box diagram with color-coded fuse positions" style="width:100%;max-width:760px;display:block;margin:1.5rem 0" />

### Blade Fuses — Main Box

| Position | Rating | Circuit |
|----------|--------|---------|
| F1  | 5A  | Instrument cluster, warning lights |
| F2  | 5A  | Radio, clock |
| F3  | 10A | Interior lighting, dome light, boot light |
| F4  | 10A | Cigarette lighter, 12V socket |
| F5  | 15A | Wiper motor (front) |
| F6  | 10A | Horn |
| F7  | 10A | Heated rear window (switching circuit — the actual load is fused separately) |
| F8  | 20A | Heated seats (if equipped) |
| F9  | 10A | Central locking, ZKE module supply |
| F10 | 15A | Front windows (driver + passenger) |
| F11 | 15A | Rear windows (if equipped) |
| F12 | 10A | Rear wiper (Touring/Compact only) |
| F13 | 20A | HVAC blower motor |
| F14 | 10A | ABS control module |
| F15 | 5A  | DME (engine ECU) ignition-switched supply |
| F16 | 15A | Fuel injectors, DME output stage |
| F17 | 10A | Oxygen sensor heater |
| F18 | 10A | Idle control valve, throttle position sensor |
| F19 | 30A | Main lighting feed (via LCM on later cars) |
| F20 | 10A | Brake lights, stop lamp switch |
| F21 | 10A | Turn signals, hazard flasher |
| F22 | 10A | Reverse lights, reversing sensor (if equipped) |
| F23 | 15A | Power mirrors |
| F24 | 10A | EWS module, antenna ring |
| F25 | 30A | Cooling fan (secondary speed) |
| F26 | 40A | Cooling fan (primary/high speed) |
| F27 | 30A | Fuel pump relay output |
| F28 | 10A | DME permanent supply (Kl. 30) |
| F29 | 5A  | Diagnostic socket (K-Bus, OBD) |
| F30 | 5A  | Airbag module (MRS) |

> **Note:** Some positions are shared or split across model variants. Convertibles have additional fuses for the roof mechanism. The E36 M3 has different assignments for some engine management circuits.

---

## Relay Reference

Relays are the larger square or rectangular components in the fuse box. They switch high-current circuits using a low-current control signal. On the E36:

| Position | Relay | Function |
|----------|-------|---------|
| R1  | Main relay | DME main relay — powers the DME, injectors, and sensors when ignition is turned on |
| R2  | Fuel pump relay | Activates fuel pump; energized by DME when starting/running |
| R3  | Cooling fan relay (slow) | Runs radiator fan at low speed via resistor |
| R4  | Cooling fan relay (fast) | Runs radiator fan at full speed (triggered by coolant temp or A/C) |
| R5  | A/C compressor relay | Clutch engagement for air conditioning compressor |
| R6  | Heated rear window relay | High-current switch for the rear demister element |
| R7  | Starter relay | Activates starter motor; signal from ignition switch Kl. 50 |
| R8  | Rear wiper relay (Touring) | — |
| R9  | Wiper park relay | Ensures wipers park correctly after switch-off |
| R10 | Flasher relay | Controls turn signal timing (click-click speed) |

### The DME Main Relay — Most Commonly Replaced

The DME main relay (R1) is the single most replaced relay on the E36. When it fails, the engine either won't start (relay fails open — DME doesn't power up) or cuts out while driving (relay fails intermittently — DME drops power under vibration or heat).

**Symptom:** Car starts fine when cold, cuts out after getting warm and won't restart until cooled down → DME main relay failing. The relay contacts arc and weld slightly, then separate when thermal expansion changes the contact geometry.

**Fix:** Replace with a genuine Bosch relay or equivalent quality. The relay is a standard automotive 4-pin type (87a contact, 30 amp rated). Cost: €5–15. Worth replacing preventively on any high-mileage E36.

### The Fuel Pump Relay

Controls the fuel pump. The DME activates it at startup and keeps it active while the engine runs. The relay also has a safety cut: if the DME stops receiving RPM signal (engine stalled), it de-energizes the relay within ~1 second, cutting fuel.

**Symptom of failure:** No fuel pump prime sound when ignition is turned on (listen for the ~2-second hum before cranking), won't start, starts briefly then cuts out.

**Test:** With ignition on (engine off), measure voltage at the fuel pump connector. Should be battery voltage for ~2 seconds then drop to 0. If 0 immediately, fuel pump relay or its control circuit is faulty.

---

## How to Find a Blown Fuse Fast

The fuse box lid diagram fades over decades, and swapped-in fuses of the wrong rating are common on older cars. Systematic approach:

### 1. Identify what stopped working

Make a list. Multiple unrelated items failing simultaneously points to a shared fuse (or a ground fault — check grounds first). A single item failing usually means its dedicated fuse.

### 2. Use the ETM cross-reference

Schema 1 of the ETM shows every fuse, its rating, and every circuit it feeds. Look up the failed circuit in the relevant schema, trace the wire back to the fuse, and note the fuse number.

### 3. Visual check under load

A blown fuse is obvious when held up to light — the element is visibly broken. However, some fuses blow with the element still partially intact but with a hairline crack that's invisible in poor lighting. Use a fuse tester (€2 tool) or multimeter in continuity mode across the fuse.

### 4. Check fuse current flow, not just continuity

A fuse can be intact but the circuit still doesn't work because power isn't reaching the fuse at all. Test both sides: voltage on the input side + voltage on the output side with the load connected = circuit is OK. Voltage on input but none on output = blown fuse or broken fuse holder clip.

### 5. Never replace without finding the cause

A blown fuse tells you there was an overcurrent event. Replace the fuse with the **correct amperage**, watch if it blows immediately (hard short) or eventually (intermittent short). A fuse that blows immediately means there's a bare wire grounding somewhere. A fuse that blows after days means an intermittent short — harder to find, usually in a connector that flexes.

**Never fit a higher-amperage fuse to stop a fuse from blowing.** This bypasses the only protection between a short circuit and a fire.

---

## Fuse Amperage — What the Colors Mean

Standard ATO/ATC blade fuses use universal colors. If the label is unreadable, the color identifies the rating:

| Color | Amperage |
|-------|---------|
| Black | 1A |
| Grey  | 2A |
| Violet| 3A |
| Pink  | 4A |
| Tan/Beige | 5A |
| Brown | 7.5A |
| Red   | 10A |
| Blue  | 15A |
| Yellow| 20A |
| Clear/White | 25A |
| Green | 30A |
| Orange| 40A |
| Red (large) | 50A |

---

## High-Current Fuses Near the Battery

The main feed from the battery to the fuse box is protected by a high-current fuse or fusible link mounted near the battery:

**E36 typical:** A 60A maxi-fuse in a black holder near the battery positive terminal, or a fusible link (a short, thick wire with a lower-current element embedded) in line with the main cable.

If this fuse blows — and it sometimes does from a dead short during electrical work — **nothing in the car works at all**. This is often mistaken for a dead battery. Test: measure voltage at the fuse box input terminal with ignition off. If 0 V despite a charged battery, the main fuse is blown.

Replacements are readily available; ensure the replacement rating matches the original.

---

## Post-Swap Fuse Considerations (M43 → M50)

When swapping from M43 to M50:

- **F16 (injectors):** M50 has 6 injectors vs M43's 4. The injector fuse rating needs to match M50 peak draw — 15–20A is standard.
- **F25/F26 (cooling fan):** The M50's cooling fan arrangement may differ from M43. Verify fan relay wiring matches.
- **DME main relay and fuel pump relay:** If using the M50 wiring loom, the relay positions may be in a different fuse box section. Plan the routing before starting.
- **EWS fuse (F24):** Must be retained and functional. EWS without power won't authorize the DME regardless of all other circuits being correct.
