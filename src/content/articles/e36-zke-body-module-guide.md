---
title: "BMW E36 ZKE — Central Body Electronics Explained"
description: "What the ZKE/GM module does, how to diagnose central locking and window faults, what coding does, and what happens when the module fails."
pillar: reference
keywords: "bmw e36 zke, e36 gm module, e36 central locking fault, e36 comfort module, bmw zke coding"
date: "2026-04-13"
hero: "zke.webp"
---

## TL;DR

The ZKE (Zentrale Karosserie-Elektronik — Central Body Electronics) module, also called the GM (Grundmodul — Basic Module), manages central locking, windows, and interior lighting convenience functions on the E36. When the central locking misbehaves, the windows don't respond to the remote, or the interior lights do unexpected things — the ZKE is usually involved. Diagnosis starts with INPA, not guesswork.

---

## What the ZKE Controls

The ZKE handles all body convenience functions:

- **Central locking** — door lock/unlock from key, interior button, and remote
- **Electric windows** — one-touch open/close (comfort function)
- **Interior lighting** — door-triggered illumination and fade-out delay
- **Boot/bonnet** — lock actuation signal routing
- **Remote control (FZV)** — radio key fob signal reception and decoding
- **Global close** — hold-lock on remote to close all windows simultaneously (where fitted)
- **Anti-theft signalling** — activation and deactivation of the alarm system (where fitted)

The ZKE does NOT control the exterior lights (that's the LCM) or the engine management (that's the DME + EWS). It is a comfort/body module only.

---

## Module Location

**Pre-facelift E36 (to ~1995):** The ZKE module is typically located in the boot (trunk), on the right side behind the panel lining, near the battery. Access by removing the boot carpet/panel on the right side.

**Post-facelift E36 (1996–1999):** The module may be repositioned to the interior, often under the rear parcel shelf or behind the driver's side rear kick panel, depending on the body style.

On convertibles, the module may also manage the soft-top hydraulic locking circuit.

Check the ETM (Body Electrical → ZKE) for the exact location for your build date.

---

## How Central Locking Works

The ZKE receives inputs from:

1. **Remote key fob (FZV)** — radio signal via a dedicated receiver aerial
2. **Key switch in door lock** — a switch in the door barrel detects lock/unlock rotation
3. **Interior lock button** — pushbutton in the door card

On receiving a valid unlock signal, the ZKE activates the door lock actuators (motors or solenoids in each door). On the E36, most actuators are cable-driven from a small reversible motor in each door.

**Lock/unlock sequence:**
- Unlock from outside: all doors unlock simultaneously
- Lock from outside: all doors lock simultaneously
- Interior button: typically locks all doors; a second press may unlock (market-dependent)
- Selective unlock (some markets): first remote press unlocks driver door only, second press unlocks all

If your car unlocks only the driver door but should unlock all doors (or vice versa), this is a coding setting in the ZKE, not a fault.

---

## Remote Key (FZV) — How It Works

The E36 uses a rolling-code infrared or RF remote depending on year and market:

| System | Method | Range |
|--------|--------|-------|
| Early IR | Infrared beam | Must point at receiver (low range) |
| Later RF | Radio frequency (433 MHz typically) | 5–10 m, non-directional |

The remote and ZKE share a synchronized rolling code counter. Each button press advances the counter. If the remote is pressed many times out of range (e.g., battery in pocket), the counter can fall out of sync with the ZKE.

**Re-synchronisation:**
With the car locked, stand within range and press the lock button 3–5 times rapidly. The ZKE accepts a window of future counter values and will re-sync if the remote is within that window. If that doesn't work, a full re-learn procedure is needed (requires INPA or the physical coding procedure — ignition cycling sequence described in the ETM).

---

## Comfort Window Function

On E36s with comfort windows (typically post-1995), the ZKE can command the power windows to open or close fully with a single long press on the remote or interior button:

- **Hold remote unlock button:** all windows drop (ventilation function)
- **Hold remote lock button:** all windows close (global close)
- **Hold interior window switch for ~1 second:** window opens/closes to end stop automatically

If the one-touch function stops working but manual window control is fine, the ZKE has lost its learned end-stop positions. Re-learn by manually driving each window to full close, holding the switch for 2 seconds after it reaches the stop. This resets the position memory.

---

## Failure Modes

### 1. Central locking doesn't work at all

**Check first:** Fuse F9 (central locking/ZKE supply). A blown F9 kills all ZKE functions.

If fuse is intact: measure voltage at the ZKE supply pin with ignition on. The ZKE needs a permanent supply (Kl.30) and an ignition supply (Kl.15). Loss of either prevents operation.

**INPA test:** Navigate to ZKE/GM → Actuator tests. You can command each door lock actuator individually from INPA. If the actuators respond to INPA commands but not to the key or remote, the problem is in the input signal chain (switch, remote receiver, wiring to ZKE). If actuators don't respond to INPA either, the ZKE itself or its output circuit is faulty.

### 2. Remote stops working

The most common cause is a flat remote battery (CR2032 or similar). Replace first.

If battery is fresh: perform the re-synchronisation procedure above. If the remote still doesn't work, test whether the ZKE responds to the physical door key switch — if it does, the ZKE is fine and the problem is in the remote receiver or the remote itself.

**Remote receiver test:** The IR or RF receiver is a small module, often near the mirror base or B-pillar. Measure its supply voltage and ground. Some receivers have a signal test via INPA.

### 3. One door doesn't lock/unlock

Usually the door lock actuator motor itself. Test by commanding that specific door from INPA. If INPA commands work: ZKE is fine, wiring and actuator are OK. If the actuator doesn't respond to INPA: check wiring from ZKE to that door actuator, then the actuator itself.

A seized actuator draws high current and can blow the ZKE's internal output transistor for that circuit.

### 4. Central locking activates randomly

A common cause on high-mileage E36s: the door barrel key switch (the microswitch that detects key rotation) is worn and giving false signals. The ZKE sees a "key turn" trigger even with no key in the lock. Replace the door barrel or isolate the switch signal wire to confirm.

Another cause: water ingress into the door lock actuator causing a short that pulses the lock signal.

### 5. Interior light doesn't fade — stays on or won't illuminate

The ZKE controls the lighting delay. A stuck door switch (door pin switch stuck in "open" position) keeps the ZKE in illuminated state. Check all four door switches — a jammed switch is a common E36 issue and is also a parasitic drain source.

---

## Coding the ZKE

The ZKE stores coding data that determines its behaviour. Default coding differs by:
- Market (US/Europe — selective unlock vs all-unlock)
- Body style (coupe, saloon, touring, convertible)
- Option fitment (alarm, sunroof, heated seats signal routing)

After replacing a ZKE, the new unit must be coded to match your car's options. Use **NCS Expert** with a K-DCAN cable:

1. Select E36 → ZKE (or GM depending on NCS Expert version)
2. Read current coding from the new module → save the file
3. Compare with the coding from your original module (if you have an NCS backup from before failure)
4. Alternatively, select options manually:

| Coding parameter | Options |
|-----------------|---------|
| `GLOBAL_CLOSE` | `aktiv` / `nicht_aktiv` |
| `FZV_SELEKTIV` | `aktiv` (driver-only first press) / `nicht_aktiv` (all doors) |
| `COMFORT_OPEN` | `aktiv` / `nicht_aktiv` |
| `ALARM` | `verbaut` (fitted) / `nicht_verbaut` |
| `VERDECK` (convertible) | `verbaut` / `nicht_verbaut` |

5. Write coding → test all functions

---

## Diagnosing with INPA

INPA → Body → ZKE (or GM):

**Status screen:** Shows real-time input states — which door switches are active, which lock outputs are on, remote receiver state. Useful for finding stuck switches without dismantling doors.

**Fault codes:** The ZKE stores faults for:
- Individual actuator open circuits or shorts
- Voltage supply faults
- Communication errors (if ZKE is K-Bus connected)

Clear faults after repair and recheck after 24 hours of normal use.

**Actuator test:** Commands each output individually. Essential for isolating ZKE output faults from wiring and actuator faults.

---

## Quick Troubleshooting

| Symptom | First check |
|---------|-------------|
| Nothing works (no locking, no remote) | Fuse F9, ZKE power supply |
| Remote doesn't work, key switch works | Remote battery, re-sync, RF receiver |
| One door doesn't lock | Actuator in that door (INPA actuator test) |
| Random locking/unlocking | Door barrel switch, water in actuator |
| One-touch windows stopped | Re-learn window end-stops |
| Interior light stays on | Stuck door pin switch (test each door) |
| Central locking after ZKE replacement | NCS Expert coding required |
