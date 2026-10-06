---
title: "BMW E36 Fuse & Relay Reference, Complete Box Guide"
description: "Where the E36's fuses and relays are, the 1994 fuse positions and the front-box relay layout from the Bentley manual, and how to find a blown fuse safely."
pillar: reference
keywords: "bmw e36 fuse box, e36 fuse chart, e36 relay guide, e36 fuse locations, bmw e36 fuse diagram"
date: "2026-04-13"
hero: "fuse-relay.webp"
reviewed: "2026-10-06"
sources:
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998, 610 Electrical Component Locations (fuse tables 1992–1998, relay positions)"
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998, 130 Fuel Injection (ECM pin tables: fuel pump relay control)"
---

## TL;DR

- **Main fuse box:** the **front power distribution box** in the engine compartment holds **46 fuses and 15 relays** (Bentley).
- **More fuses and relays:** the **auxiliary relay panel** under the left side of the dashboard, the left and right **splice panels**, and on later cars a fuse in the right side of the luggage compartment.
- **Fuse assignments changed every model year** and depend on equipment and market. Bentley prints a separate table for each year from 1992 to 1998. **The chart in your fuse box lid, or the wiring diagrams for your car, is the authority.**
- **Always replace a fuse with the same rating.** A bigger fuse can cause circuit damage or a fire.

---

## Where everything is

| Location | What's there (Bentley) |
|---|---|
| Front power distribution box, engine compartment | Fuses 1–46 and relay positions 1–15 |
| Auxiliary relay panel, under the left side of the dashboard | Comfort relay (where fitted), crash control module, park ventilation relay; on cars from January 1995 the EWS II transmitter/receiver module; fuse 48 |
| Left splice panel | Fuses 47 and 50 (later cars) |
| Right side of the luggage compartment | Fuse 49 (later cars) |

---

## Relays in the front power distribution box (Bentley)

| Position | Relay |
|---|---|
| 1 | Fuel pump relay |
| 2 | System (main) relay |
| 3 | Oxygen sensor heater relay |
| 4 | Horn relay |
| 5 | Taillight / foglight relay |
| 6 | Low beam relay |
| 7 | High beam relay |
| 8 | Emergency flasher relay |
| 9 | Heater / A/C blower relay |
| 10 | Rear defogger relay |
| 11 | ABS system relay |
| 12 | ABS pump relay |
| 13 | High-speed radiator fan relay |
| 14 | A/C compressor relay |
| 15 | Low-speed radiator fan relay |

Relay positions can vary from car to car. Bentley's tip: verify a relay by comparing the wire colours at its socket with the wiring diagram.

### The fuel pump relay and the "priming hum"

On the M50's Bosch DME M3.1 and M3.3.1, Bentley's pin tables state that the DME switches the fuel pump relay **only while the engine is cranking or running**: the crankshaft position signal must be present. So **no pump noise with the ignition just switched on is normal** on these cars, not a fault. To test the pump on its own, Bentley bridges the relay socket's terminals **30 and 87 with a fused jumper**. See the [fuel system guide](/guides/e36-fuel-system-guide).

---

## 1994 fuse positions (Bentley Table d, front power distribution box)

Main circuit per fuse; many fuses feed several circuits. This is Bentley's **US-market 1994** table: European cars and other years differ, so **check your own car's chart**.

| Fuse | Rating | Main circuit(s) |
|---|---|---|
| 1 | 30A | Power sunroof |
| 2 | 15A | Not used |
| 3 | 30A | Headlight washer |
| 4 | 15A | Heated seats |
| 5 | 30A | Power seats |
| 6 | 20A | Rear window defogger / blower |
| 7 | — | Central body electronics (convertible), central locking, convertible roof |
| 8 | 15A | Horn |
| 9 | 20A | Sound system |
| 10 | 30A | ABS / traction control |
| 11, 12 | 7.5A | Headlights / foglights, on-board computer |
| 13 | 5A | Not used |
| 14 | 30A | Front power windows |
| 15 | 15A | Headlights / foglights |
| 16 | 5A | Engine control module; heating and A/C |
| 17 | 10A | Not used |
| 18 | 15A | **Fuel pump** |
| 19 | 30A | Rear power windows |
| 20 | 30A | Blower motor |
| 21 | 5A | ABS / traction control |
| 22 | 5A | Instrument illumination, park/taillights |
| 23 | 5A | Headlights/foglights, heated seats, instrument cluster, turn signals and others |
| 24 | 10A | Power mirrors |
| 25 | 5A | Headlights/foglights, instrument illumination |
| 26 | 10A | Back-up lights; automatic transmission control |
| 27 | 5A | Instrument cluster, on-board computer |
| 28 | 5A | Cruise control, **engine control module**, starting system |
| 29, 30 | 7.5A | Headlights / foglights |
| 31 | 5A | Clock, heating and A/C, instrument cluster |
| 32 | 30A | Cigar lighter / ashtray lights |
| 33 | 10A | Central body electronics, interior lights, licence plate and luggage compartment lights, park/taillights |
| 34 | 15A | Crash control module, turn signals / hazard lights |
| 35 | 25A | Central locking, convertible roof, roll-over protection |
| 36 | 30A | Wiper / washer |
| 37 | 10A | Engine compartment light, instrument illumination, lights and others |
| 38 | 30A | ABS / traction control |
| 39 | 7.5A | Heating and A/C |
| 40 | 30A | Power seats |
| 41 | 30A | Heating and A/C, **radiator auxiliary fan** |
| 42 | 7.5A | Airbag (SRS), roll-over protection |
| 43 | 5A | Anti-theft system, airbag, central body electronics |
| 44 | 15A | Glove compartment light and others |
| 46 | 15A | ABS, **brake lights**, cruise control, instrument cluster and others |

---

## Finding a blown fuse

1. **List what stopped working.** Several unrelated items at once suggest a shared fuse, or a bad ground (see the [ground guide](/guides/e36-ground-distribution-guide)).
2. **Find the fuse** for that circuit on your lid chart or in the wiring diagrams.
3. **Ignition off** before pulling fuses or relays. For any other electrical work, also disconnect the battery negative cable (in the boot), observing your car's battery-disconnection cautions. On cars with airbags, follow the airbag precautions first.
4. **Check it properly:** a hairline crack can hide in the element. Better than looking: measure voltage on **both** sides of the fuse with the circuit switched on.
5. **Find the cause.** A new fuse that blows at once means a hard short; one that blows later points to an intermittent short or an overloaded circuit.

**Never fit a fuse of a higher rating** to stop one from blowing.

### Blade fuse colours

| Colour | Rating |
|---|---|
| Tan | 5A |
| Brown | 7.5A |
| Red | 10A |
| Blue | 15A |
| Yellow | 20A |
| Clear / natural | 25A |
| Green | 30A |

---

## After an M43 → M50 swap

- The M50 engine harness plugs into the same chassis connector, and the engine-management fuses and relays (**system relay**, **fuel pump relay**, **oxygen sensor heater relay**) are already in the front box.
- **No fuel pump priming hum is normal** on an M3.1/M3.3.1 car; the pump runs while cranking.
- The **six-cylinder auxiliary fan** relies on its relays and fuse in the front box and on the radiator's temperature switch. Check the fan works after the swap.
