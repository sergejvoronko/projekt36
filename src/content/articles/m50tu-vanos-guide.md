---
title: "M50TU VANOS, How It Works, What Fails, and How to Fix It"
description: "How the M50TU single VANOS works, how to test it the BMW way, why the piston seals fail and what the seal repair involves, with Bentley torque values."
pillar: engine
keywords: "m50tu vanos, bmw vanos repair, vanos rattle, vanos seals, m50 vanos rebuild, bmw e36 vanos"
date: "2026-04-13"
hero: "vanos.webp"
reviewed: "2026-10-03"
sources:
  - title: "Bentley Publishers: BMW 3 Series (E36) Service Manual 1992–1998, 117 Camshaft Timing Chain (VANOS)"
  - title: "Beisan Systems: 6-cylinder single VANOS seal repair procedure (E36, E34, E39)"
    url: "https://beisansystems.com/single-vanos-6-cyl-e36-e34-e39/"
  - title: "Wikipedia: BMW M52 (single vs double VANOS)"
    url: "https://en.wikipedia.org/wiki/BMW_M52"
---

## TL;DR

VANOS (*variable Nockenwellensteuerung*, variable camshaft timing) on the M50TU varies the **intake** camshaft timing, advancing it by up to **12.5°**. It is hydraulic: engine oil pressure moves a piston, and a DME-controlled solenoid decides when. The classic failure is the **piston seals**: the original O-ring hardens and shrinks with age, the piston stops holding pressure, and the engine loses mid-range response. Aftermarket seal kits fix it, but the VANOS unit has to come off the engine, with the crankshaft and camshafts locked at TDC.

---

## Which engines have which VANOS

| Engine | VANOS |
|---|---|
| M50 (built up to 8/1992) | None |
| M50TU (1993 on) | Single VANOS, intake camshaft |
| M52 (E36 328i/323i up to 1998) | Single VANOS, intake camshaft |
| M52TU (1998 on) | Double VANOS, intake and exhaust |
| S50B30 (European M3, 1992–95) | Single VANOS |
| S50B32 (European M3, 1995 on) | Double VANOS |

Most E36 325i have the M50TU. The non-VANOS M50 is mainly found in cars built up to 1992. If you are buying an M50 for a swap, check which you are getting: the non-VANOS engine is simpler, and the TU has better mid-range response.

---

## How it works

The main parts are the **VANOS control unit** at the front of the cylinder head (piston housing with an integral spool valve, plus the solenoid) and a **modified intake camshaft**. The intake sprocket drives the camshaft through helical splines, so when the piston pushes the gear cup forward, the camshaft rotates slightly relative to its sprocket.

- With the engine running, the piston housing is supplied with pressurized engine oil.
- **At idle**, the solenoid is off and the valve timing stays in its normal position.
- **When the DME energizes the solenoid**, oil pushes the piston forward and the intake camshaft advances, by a maximum of 12.5°.

The DME decides when to advance based on engine load, engine speed and engine temperature.

---

## Failure modes

### Piston seal failure (most common)

The VANOS piston is sealed by an O-ring and a Teflon ring. With age the original O-ring hardens, shrinks and develops flat spots, so oil leaks past the piston and the camshaft no longer advances fully. Typical symptoms:

- flat or hesitant response below about 3,000 rpm
- rough idle
- a VANOS fault stored in the DME

### Solenoid or control unit faults

The solenoid is available as a separate part. If the **control unit's own plunger** sticks, BMW's answer is a complete control unit.

### Incorrect installation

Bentley points out a cause that is easy to overlook: if the VANOS doesn't advance and no other fault is found, the control unit may have been installed incorrectly, especially if the camshaft sprockets were removed during earlier work. Reinstalling it correctly is the fix.

### Base timing

The VANOS works from the camshaft's base timing. If the timing chain is worn or the timing was set wrongly, the VANOS starts from the wrong point, and the symptoms overlap with seal failure.

---

## Testing the VANOS (the BMW method)

Bentley's test needs three special tools: electrical test lead **12 6 410**, air-line fitting **11 3 450** and crankshaft TDC locking tool **11 2 300**. In outline:

1. Set the engine to TDC on cylinder 1 and lock the crankshaft.
2. Replace the VANOS oil line fitting with the air-line fitting and apply **compressed air at 30–115 psi**.
3. Measure the distance between the trigger plate edge and the side of the secondary chain tensioner.
4. Energize the solenoid with the test lead. It should click audibly and the intake camshaft should advance. Measure again.
5. The difference between the two measurements must be **at least 8.5 mm**. Less points to the solenoid, the control unit or its installation.

**Polarity matters:** connecting the test lead the wrong way round destroys the solenoid's internal diode. The solenoid still works, but the DME may store a fault. Bentley describes how to confirm the polarity first.

---

## The seal repair

BMW does not sell the piston seals separately, only complete or rebuilt control units. Aftermarket kits (Beisan Systems is the best known) contain an upgraded O-ring and a new Teflon ring for the M50TU and M52 single VANOS.

**What the job involves:**

- The **engine must be cold.** Lock the crankshaft at TDC (11 2 300) and the camshafts (11 3 240). Lock the secondary chain tensioner down (11 3 292 or a stiff wire).
- Remove the fan (left-hand thread), the cylinder head cover and the oil baffle. Then the two **access plugs** on the control unit, so the exhaust sprocket bolts can be loosened.
- Disconnect the solenoid and oil line, remove the control unit's nuts and bolt and take the unit off the head.
- On the bench, take the piston out, cut away the old O-ring and Teflon ring, and fit the new O-ring and then the new Teflon ring. The kit instructions explain how to warm and seat the Teflon ring.
- Refit the unit so the helical splines engage correctly and the shaft is fully seated. Retighten everything to the values below, refit the access plugs and check the timing with the locking tools before starting.

Allow most of a day the first time. Follow the kit maker's instructions alongside Bentley.

---

## Torque values (Bentley)

| Fastener | Torque |
|---|---|
| VANOS control unit to cylinder head, M6 nut | 10 Nm |
| VANOS control unit to cylinder head, M8 bolt | 22 Nm |
| VANOS oil supply line banjo bolt | 32 Nm |
| VANOS solenoid to control unit | 30 Nm |
| Access plugs in the control unit | 50 Nm |
| Exhaust camshaft sprocket bolts (M7 Torx) | 5 Nm, then 22 Nm |
| Cylinder head cover | 10 Nm |

---

## Non-VANOS or TU for a swap?

**M50 non-VANOS:** no VANOS unit to maintain, simpler timing work, but harder to find, since it was built only up to 1992.

**M50TU:** better mid-range response, and far more common in E36 325i. The VANOS is reliable once the seals have been renewed.

Neither is a bad choice. The non-VANOS removes one system to maintain; the TU drives better at everyday engine speeds.
