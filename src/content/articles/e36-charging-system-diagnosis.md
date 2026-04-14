---
title: "BMW E36 Charging System — Diagnosis from Scratch"
description: "Step-by-step E36 charging system diagnosis: alternator, voltage regulator, belt, and the D+ circuit. Avoid the expensive misdiagnosis."
pillar: reference
keywords: "bmw e36 alternator, e36 charging fault, e36 battery light, e36 bosch alternator, e36 voltage regulator"
date: "2026-04-13"
hero: "charging.webp"
---

## TL;DR

The most expensive E36 charging diagnosis mistake is replacing the alternator when the problem is a bad ground, a loose belt, or a €12 voltage regulator. The E36's charging system is straightforward: alternator → voltage regulator → battery → chassis. Test in order, replace the cheapest part first. Most faults are the regulator, a corroded connection, or the drive belt — not the alternator itself.

---

## How the E36 Charging System Works

The alternator is belt-driven from the crankshaft. Inside the alternator:

1. **Rotor** — spins with the belt pulley; creates a magnetic field when the exciter circuit energizes it
2. **Stator** — fixed windings that generate AC current as the magnetic field rotates
3. **Rectifier diodes** — convert AC to DC
4. **Voltage regulator** — controls rotor excitation to maintain ~14.2V output regardless of RPM or load

The regulator is the key component. It's a separate unit attached to the back of the alternator. It contains the brushes (which contact the rotor slip rings) and the voltage-sensing/control circuit. This is the most commonly replaced component — and on the E36, it's a bolt-on unit that costs €10–25.

### The charging warning light

The dashboard warning light connects between ignition positive and the alternator's warning light terminal (terminal D+). When the engine is off, both sides of the bulb are at the same potential, so it doesn't light. When the engine runs and the alternator charges, the D+ terminal is pulled high — again, equal potential, light off. When the alternator isn't charging, D+ stays low while the ignition side is high — current flows, light illuminates.

This means: **charging warning light on = alternator output is below ignition supply voltage.** It doesn't necessarily mean the alternator is dead — just that it's not producing enough voltage.

---

## Diagnostic Order (Cheap to Expensive)

### Step 1: Check the drive belt

Belt slipping or broken = alternator not spinning = no charge. Obvious but skipped often.

- Belt present and taut? Should deflect 8–12 mm under firm thumb pressure
- Belt surface cracked, glazed, or frayed? Replace it
- Tensioner pulley wobbles? Replace tensioner

A slipping belt charges intermittently — battery warning light flickers at idle, goes out above 2000 RPM when belt bite improves. The smell of burning rubber under the bonnet confirms it.

### Step 2: Visual inspection and connections

- Battery terminals: corrosion, loose clamps
- Main cable from alternator B+ terminal to battery: check both ends for corrosion
- Ground cable from battery to engine block: check both ends
- Engine-to-chassis ground strap: present and tight?
- Alternator mounting bolts: loose alternator vibrates, wears brushes prematurely

### Step 3: Battery voltage test

Test with a multimeter, engine off:
- **12.6–12.8 V** = fully charged
- **12.4 V** = partially discharged
- **Under 12.0 V** = discharged or failing battery

A battery under 12.0 V may not be able to power the exciter circuit adequately — the alternator won't charge from a deeply discharged battery until the battery is partially recovered (jump start and run for 10 minutes first).

### Step 4: Charging voltage test

Engine running, multimeter at battery terminals:
- **13.8–14.4 V** = normal charging
- **12.6–13.5 V** = undercharging (regulator or connection issue)
- **14.8 V+** = overcharging (regulator failure — replace immediately, will destroy battery)
- **Same as Step 3 reading** = alternator not charging at all

Test at idle and at 2000 RPM. A good alternator shows 13.8–14.2 V by 1200 RPM and maintains it through the rev range.

### Step 5: Load test the charging system

Turn on: headlights, rear demister, blower on max, A/C if equipped. This represents near-maximum electrical load.

Voltage at battery should stay above 13.5 V. If it drops to 12.8 V or below under load, the alternator is undersized for load, failing, or the regulator is limiting output.

### Step 6: Test the voltage regulator

Remove the regulator from the back of the alternator (3–4 screws, easy access with the alternator in-car). Visually inspect:
- Brush length: brushes should extend at least 5 mm from the regulator body. Worn brushes = intermittent or no charging
- Brush contact: if brushes are worn to the backing plate, the rotor slip rings have no contact

A worn regulator produces the classic E36 symptom: charges fine when cold, warning light comes on after 20–30 minutes as the regulator heats up and internal resistance changes.

**Replacement:** Bosch F00M145200 or equivalent (check your alternator part number for the correct regulator). The regulator is a 10-minute swap and typically cures 60–70% of E36 charging complaints.

### Step 7: Test the alternator independently

If the regulator is new and correct voltage still isn't achieved, the alternator itself may be failing. Tests:

**AC ripple test:** With engine running, set multimeter to AC voltage, test at battery terminals. Should read under 0.5 V AC. Higher than 0.5 V = diode failure in the rectifier pack (alternator rebuilding or replacement needed).

**Diode test:** An alternator with a failed diode will show excess AC ripple and may also drain the battery when the car is parked (diodes should block reverse current flow — failed diode allows battery drain through the stator).

**Bench test:** Remove the alternator, take it to a parts supplier with a bench tester. Most test alternators for free. A 10-minute drive saves a lot of guesswork.

---

## Alternator Specifications

| Engine | Stock alternator | Output |
|---|---|---|
| M43B18 | Bosch 90A or 120A | 90–120A depending on spec |
| M50B20 | Bosch 120A | 120A |
| M50B25 | Bosch 120A or 140A | 120–140A |
| M52B28 | Bosch 140A | 140A |

The stock alternator is adequate for standard electrical loads. If you've added: high-power audio, electric fans, heated seats that weren't original, or other high-draw accessories, consider upgrading to a higher-output alternator (typically from a later E36 variant or equivalent Bosch unit with same mounting).

---

## Regulator and Alternator Part Numbers

| Alternator | Regulator | Output |
|---|---|---|
| Bosch 0 123 510 068 | F00M145200 | 90A |
| Bosch 0 123 515 025 | F00M145200 | 120A |
| Bosch 0 123 520 024 | F00M145201 | 140A |

Always verify against your alternator's stamped number. Aftermarket alternatives (Valeo, Hella) use equivalent regulators — cross-reference by alternator output and frame size.

---

## Common Misdiagnosis Situations

### "New alternator, still not charging"

Almost always one of:
1. The new alternator is also defective (not unknown with cheap pattern parts)
2. The D+ (exciter) wire to the alternator is broken — without exciter voltage, the alternator can't self-excite and produce output
3. Bad ground — the charging return path has high resistance; the alternator output appears low because the voltage is being dropped across a corroded ground

Test the D+ wire: at the alternator connector, check for ~12V on the D+ pin with ignition on, engine off. If 0 V, trace back through the charge warning light circuit.

### "Battery flat after sitting two days"

This is parasitic drain, not a charging fault. A healthy charging system fills the battery during driving but can't overcome a constant drain. Diagnose with a multimeter in series with the battery negative — measure current draw with everything off (target: under 30 mA). Then pull fuses one by one until current drops — that fuse's circuit is the drain.

Common E36 parasitic drain sources: aftermarket radio (check it has a proper ignition feed), ZKE module with a stuck relay, boot light switch jammed on, phone charger left plugged in.

### "Charging warning light on but voltage reads 14.2 V"

The warning light circuit itself has a fault — not the charging system. The light illuminates when D+ terminal voltage is below ignition supply. This can happen if:
- The D+ wire has extra resistance (but alternator is charging fine)
- The warning light PCB has a fault
- A diode in the alternator monitoring circuit has failed

Use INPA → DME → live data → battery voltage: if it reads 14.2 V, the alternator is fine. The warning light circuit needs investigation separately.

---

## After a Swap (M43 → M50)

The M50's alternator is physically different from the M43 unit and mounts in a different position. When swapping:

- Use the M50 alternator, bracket, and tensioner as a complete assembly
- Route the B+ cable from M50 alternator to battery — may need extension or rerouting
- The D+ exciter circuit connects at the firewall connector; verify the M50 loom's D+ wire reaches the alternator connector
- Engine ground (G100) to M50 block must be secure — alternator output returns through this path

After first start, measure charging voltage immediately. Catching an issue at first start is far easier than diagnosing it after 50 km.
