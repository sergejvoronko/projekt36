---
title: "M43 to M50 Swap — Wiring Differences and What to Reuse"
description: "Electrical differences between the M43 and M50 for an E36 swap: loom strategy, EWS options, and sensor compatibility."
pillar: swap
keywords: "m43 m50 swap wiring, e36 engine swap electrics, m50 wiring harness, m43 m50 ecu wiring"
date: "2026-04-13"
hero: "wiring-swap.webp"
---

## TL;DR

The M43-to-M50 wiring swap is manageable but requires planning. The short version: use the M50 engine loom and DME, keep your E36's body wiring (lights, locks, instruments), bridge the connectors that differ between M43 and M50 body plugs, and handle EWS correctly from the start. Getting EWS wrong is the number one cause of a completed swap that won't start.

---

## What Actually Differs

The E36 body wiring harness (cabin, lights, instruments, ABS) is largely the same regardless of which engine was originally fitted. The differences are in the **engine bay wiring** and **engine management** systems.

| System | M43 | M50 / M50TU |
|---|---|---|
| Engine management | Motronic M1.7 / M1.7.3 | Motronic M3.1 (M50) / M3.3.1 (M50TU) |
| Cylinders / injectors | 4 / 4 | 6 / 6 |
| VANOS | None | None (M50) / Single VANOS (M50TU) |
| EWS interface | EWS 2 (K-Bus) | EWS 2/3 (K-Bus) |
| Oxygen sensors | 1 (pre-cat) | 1–2 depending on spec |
| Coolant temp sensor | 2-pin NTC | 2-pin NTC (compatible) |
| Intake air temp | In airflow meter | Separate sensor on manifold |
| Throttle position | Potentiometer + idle switch | Potentiometer only |
| Engine speed sensor | 60-2 reluctor, same DME logic | 60-2 reluctor, same DME logic |
| Knock sensors | 1 | 2 (M50) or 2 (M50TU) |

The key takeaway: the engine management systems are **not interchangeable** — you cannot run M50 sensors with M43 DME or vice versa. The M50's Motronic has different sensor inputs, different calibration, and different EWS communication requirements.

---

## Strategy: Use the M50 Engine Loom

The cleanest swap approach — and the one that gives the fewest problems — is to use the **complete M50 engine loom** that came with the donor engine. This harness was designed for the M50 DME and has the correct connector types, pinouts, and wire gauges for all M50 sensors.

The M50 engine loom connects to the car's body wiring at a defined set of junction points, primarily:

- The firewall bulkhead connector (large multi-pin connector passing through the firewall)
- The fuse box connections for DME, fuel pump, ignition, and fan relays
- The diagnostic socket (K-Bus for EWS communication)
- Ground points on the engine block and chassis

Your job is to make the M50 loom connect correctly at each of these junction points in your M43 E36's body.

---

## Firewall Connector Differences

The main challenge is that the M43 and M50 E36 use **different firewall connector configurations**. The M43 body has connectors sized and pinned for the M43 engine loom. The M50 engine loom has connectors sized for M50 specification.

### What varies

**The large DME connector (at the firewall):** The M43 firewall has a connector with a specific pin count for the M43 DME's inputs. The M50 DME uses a different connector with more pins (the M50 has more sensors).

### Solutions

**Option 1: Full M50 loom + body loom adapter**  
Many E36 M50 swap specialists sell pre-made adapter harnesses. These bridge the M43 body connector to the M50 loom connectors. You maintain both looms intact (nothing cut), and the adapter handles the translation. Cost: €80–200 depending on supplier.

**Option 2: Full donor body loom**  
If your donor car is also an E36 (just a different engine variant), the donor's complete engine bay loom can come with it. This requires more dismantling of the donor car but gives you all factory connectors.

**Option 3: Pin-by-pin rework**  
With the ETM for both M43 and M50 variants, trace each circuit and re-pin the connectors to match. Time-intensive but requires no adapter harness. Necessary if adapters aren't available for your specific market spec.

---

## Sensor-by-Sensor Compatibility

### Coolant temperature sensor

Both M43 and M50 use a 2-pin NTC (negative temperature coefficient) coolant sensor. The physical connector and thread size are the same on most E36 applications. The sensor from the M50 can be used, or the existing one if it's recently replaced.

**Verify:** The M50TU has two coolant temp sensors (one for DME, one for instrument cluster). The M43 may only have one. If your M50 has two sensor ports, both must be connected.

### Intake air temperature

The M43 has its intake air temperature sensor built into the airflow meter. The M50 has a **separate intake air temperature sensor** on the intake manifold. The M50 loom will have a connector for this sensor — it must be present and connected.

### Knock sensors

The M43 has one knock sensor; the M50 has two. These thread into the block. Both connectors must be used — the M50 DME monitors knock individually per bank. Running with one knock sensor disconnected causes the DME to pull ignition timing aggressively on the assumption knock is occurring.

### Throttle position sensor

Both use a rotary potentiometer. The M50 TPS is on the throttle body and the M50 loom has the correct connector. **Do not swap TPS from M43 body wiring** — the M50 DME has specific calibration for the M50 TPS voltage range.

### Oxygen sensor

**M50 (non-TU):** 3-wire heated oxygen sensor (2 heater wires + 1 signal)  
**M50TU:** Same, or a second post-cat sensor if emissions-equipped  
**M43:** 3-wire heated oxygen sensor

The connector pinout is the same (Bosch standard). If using an M50 into an M43-spec E36 without a catalyst, cap the post-cat sensor port (if present) or connect a sensor — the DME uses its signal to monitor converter efficiency.

### Airflow meter / MAF

The M50 uses a **hot-film MAF sensor** (Siemens/Continental type). This is a critical component — incorrect airflow reading causes major fuelling problems. Always use the airflow meter that came with the M50 loom, and ensure the MAF's connector is from the M50 loom (correct pinout). Generic replacement MAFs must be specification-correct.

---

## EWS — Plan This Before You Start

EWS causes more post-swap no-starts than any other single issue. Read the dedicated EWS guide for full detail; here's the swap-specific summary:

### The problem

Your M43 E36 has an EWS module matched to its original DME and keys. The M50 donor car has an EWS matched to the M50 DME and donor keys. These are not interchangeable without recoding.

### Option A: Use M50 donor EWS + DME + keys as a set

Take the EWS module, M50 DME, and all ignition keys from the donor car. They are already matched. In your E36, connect the M50 DME and donor EWS module in place of the M43 equivalents. Use the donor keys.

**Pros:** No coding required, works immediately  
**Cons:** The EWS is matched to the donor VIN's security information. Adding a key later requires donor car data.

### Option B: Recode EWS to new DME

Keep your original E36 EWS and your existing keys. Have a specialist with INPA/WinKFP sync the EWS to the M50 DME's ISN (Individual Serial Number). The M50 DME's ISN is read-only from the DME itself — you don't need any information from the donor car.

**Pros:** Your existing keys continue to work, your VIN is retained in the EWS  
**Cons:** Requires professional recoding (€50–150 at a competent BMW specialist)

### Option C: EWS delete

Flash the M50 DME with EWS-deleted software. The immobilizer check is removed entirely.

**Pros:** Eliminates all EWS-related complications permanently  
**Cons:** Removes theft protection; requires a reputable tune source for the delete file

### What happens if you ignore EWS

The M50 will crank perfectly. All sensors will show correct values in INPA. The DME receives power, the ignition fires the injectors, everything appears ready — but the fuel injectors receive no pulse. The DME is locked by EWS and won't inject fuel. This is the classic completed-swap symptom: cranks well, smells of fuel briefly, never fires.

**Do not spend time chasing this with sensor testing or compression tests.** If the swap is electrically complete and the engine cranks but won't fire, EWS is the first thing to verify — takes 5 minutes with INPA.

---

## Cooling Fan Circuit

The M50 runs hotter under load than the M43 (more displacement, more heat). The cooling fan relay circuit must be correctly wired:

- The M50 DME activates the cooling fan via the same relay circuit as the M43, but the fan switching thresholds differ
- If using the M50 DME and M50 loom, the fan activation logic is already calibrated correctly
- Verify that the high-speed fan relay (full-speed for coolant temp above ~105°C) is functional — the M50 needs it

---

## What to Check Before First Start

After completing the electrical connections:

- [ ] EWS synchronized to DME (or deleted) — confirmed with INPA
- [ ] Both knock sensors connected
- [ ] MAF sensor connected and from M50 loom
- [ ] All injector connectors seated (6 injectors, all 6 connected)
- [ ] Coolant temp sensor connected
- [ ] Intake air temp sensor connected
- [ ] TPS connected
- [ ] O2 sensor(s) connected
- [ ] Battery ground to engine block (G100) secure
- [ ] Engine-to-chassis ground strap (G101) connected
- [ ] DME main relay in correct position
- [ ] Fuel pump relay in correct position
- [ ] DME fuse (F15, F28) rated correctly
- [ ] Injector fuse (F16) rated for 6-cylinder (15–20A)

With this checklist verified, connect INPA before the first start, navigate to DME, and check for fault codes with ignition on but engine off. Address any pre-start faults before cranking. The M50 should start and run cleanly from the first attempt if the mechanical side is correct.
