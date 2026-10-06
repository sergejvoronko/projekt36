---
title: "BMW E36 ZKE, Central Body Electronics Explained"
description: "ZVM (1992–93) and ZKE IV (from 9/1993 production) on the E36: what each module controls, where it is, how the locks and comfort closing work, and how to diagnose central locking and window faults."
pillar: reference
keywords: "bmw e36 zke, e36 zke iv, e36 zvm, e36 central locking fault, e36 comfort closing"
date: "2026-04-13"
hero: "zke.webp"
reviewed: "2026-10-06"
sources:
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998, 400 Body–General, 515 Central Locking and Anti-Theft, 610 Electrical Component Locations"
---

## TL;DR

- E36s use **two generations** of body electronics. **1992–1993 models** have the **central locking module (ZVM)**. Cars **built from 9/1993 (model year 1994)** have **Central Body Electronics, ZKE IV**.
- **ZKE IV** adds one-touch windows, closing the windows and sunroof from the door lock, and locking or unlocking from the boot lock.
- The control module sits **behind or in front of the glove compartment**, not in the boot.
- The system is **self-diagnostic**: fault codes are read through the diagnostic connector in the engine compartment.

---

## Which one does your car have?

| | ZVM | ZKE IV |
|---|---|---|
| Fitted to | 1992–1993 models | Built from 9/1993 (1994 model year) to 1998 |
| Module location (Bentley) | Behind the glove compartment | Behind the glove compartment (described in 515 as mounted in front of it) |
| Interior lighting | ✓ | ✓ |
| Central locking with double lock | ✓ | ✓ |
| Power window and sunroof relays | ✓ | ✓ |
| One-touch window up/down | | ✓ |
| Close windows and sunroof from the door lock | | ✓ |
| Lock and unlock from the boot lock | | ✓ |

On ZKE IV cars, a remote key pad was available on some 1994 and later cars.

**Projekt 36** is a January 1994 build, so it should have ZKE IV, the same month the first **EWS** immobiliser arrived. See the [EWS guide](/guides/e36-ews-immobilizer-guide).

---

## How the locks work

When you turn the key in a front door lock, **microswitches** in the lock cylinder tell the module what to do. It then drives the electric actuators at each door, the boot lid and the fuel flap.

**ZKE IV (two microswitches per front door):**

- **About 45° one way (position 1):** locks and arms the alarm. **Holding the key there closes the open windows and the sunroof.**
- **About 45° the other way (position 2):** unlocks and disarms the alarm.

**ZVM (three microswitches per front door):** about 45° locks, about 90° **double locks**, and about 45° the other way unlocks.

<figure class="p36-diagram">
<div class="p36-diagram-scroll">
<svg viewBox="0 0 760 270" role="img" aria-labelledby="zk-title zk-desc">
<title id="zk-title">ZKE IV door lock key positions</title>
<desc id="zk-desc">Driver's door lock cylinder, key vertical at position 0. Turned about 45 degrees one way, position 1: locks and arms the alarm; holding the key there closes open windows and the sunroof. Turned about 45 degrees the other way, position 2: unlocks and disarms the alarm.</desc>
<circle class="d-box d-main" cx="380" cy="150" r="70"/>
<path class="d-vac d-thick" d="M380 150 V82"/>
<text class="d-size" x="380" y="72" text-anchor="middle">0</text>
<path class="d-vac" d="M380 150 L334 104" stroke-dasharray="6 5"/>
<path class="d-vac" d="M380 150 L426 104" stroke-dasharray="6 5"/>
<text class="d-size" x="318" y="96" text-anchor="middle">1</text>
<text class="d-size" x="442" y="96" text-anchor="middle">2</text>
<circle class="d-port" cx="380" cy="150" r="7"/>
<rect class="d-box" x="40" y="70" width="230" height="98" rx="8"/>
<text class="d-label" x="54" y="92">Position 1 (≈45°)</text>
<text class="d-sub" x="54" y="112">locks, arms the alarm</text>
<text class="d-sub" x="54" y="130">hold the key here: windows</text>
<text class="d-sub" x="54" y="146">and sunroof close</text>
<rect class="d-box" x="490" y="70" width="230" height="64" rx="8"/>
<text class="d-label" x="504" y="92">Position 2 (≈45°)</text>
<text class="d-sub" x="504" y="112">unlocks, disarms the alarm</text>
<text class="d-note" x="40" y="250">Which way is 1 and which is 2 depends on the door; check on your car. Positions per Bentley 515, Fig. 20.</text>
</svg>
</div>
<figcaption>ZKE IV key positions in the front door locks. ZVM cars (1992–93) have a third switch position at about 90° for double locking.</figcaption>
</figure>

**Double locking:** Bentley warns not to double lock with passengers in the car unless the master key is at hand: the doors then can't be opened from inside or outside without it. With a flat battery the car can still be locked and unlocked with the key.

---

## Fuses (Bentley, front power distribution box)

| Fuse | Rating | Circuits |
|---|---|---|
| 7 | — | Central body electronics (convertible), central locking, convertible roof |
| 33 | 10A | Central body electronics, interior lights, licence plate and boot lights, park/taillights |
| 35 | 25A | Central locking, convertible roof, roll-over protection |
| 43 | 5A | Anti-theft system, airbag, central body electronics |

The full table is in the [fuse and relay reference](/guides/e36-fuse-relay-reference).

---

## Diagnosing faults

**Nothing locks at all:** check fuses 35 and 43, then the module's power and grounds. If the module isn't powered, nothing works.

**One door doesn't lock or unlock:** the problem is at that door: the actuator, or the wiring in the **rubber boot between the door and the body**, where wires break after years of opening and closing. Listen for the actuator; measure for voltage at its connector when you lock and unlock.

**Locking from one door works, from the other doesn't:** suspect that door's lock cylinder microswitches or their wiring.

**Windows won't close with the key (ZKE IV):** check that the windows work from their switches first; then check the microswitch in the driver's lock.

**Read the fault memory.** The module stores fault codes, readable through the round diagnostic connector in the engine compartment with a suitable tool (see the [INPA setup guide](/guides/e36-inpa-setup-guide)). Clear the codes, test, and read them again.

The wiring for your exact car is in the ETM. See [how to read the ETM](/guides/e36-how-to-read-etm).
