---
title: "BMW E36 OBD1 Fault Codes — Complete Reference: Every Code, What It Means, and What to Check First"
description: "A complete, no-fluff reference for every BMW E36 OBD1 DME fault code — what each code means, which sensors and circuits to test first, and what they look like in real-world diagnostics. Written for E36 owners and builders who already know their way around a wrench."
pillar: reference
keywords: "BMW E36 OBD1 fault codes, E36 DME fault code list, BMW E36 diagnostic codes M50"
date: "2026-04-30"
hero: "e36-obd1-fault-code-reference.webp"
---

## TL;DR

- **What:** Complete fault code reference for BMW E36 OBD1 DME systems (M50, M52, S50, M44, M43)
- **Why:** OBD1 codes won't read on a standard ELM327 — you need to know what you're looking at with a 20-pin adapter or blinking LED method
- **Cost:** €15–€80 for a basic OBD1 scan tool or ADS adapter; component testing is mostly free with a multimeter
- **Time:** 30–90 minutes for a full read and component check
- **Difficulty:** 2/5

---

## How E36 OBD1 Diagnostics Actually Work

Every E36 built before late 1995 (and many up to 1996, depending on market and engine code) runs BMW's proprietary OBD1 protocol over a 20-pin diagnostic connector located in the engine bay, usually on the driver's side strut tower or firewall. This is **not** compatible with standard OBD2 scanners. Your ELM327 dongle will do nothing here.

You have three realistic options:

1. **BMW ADS/GT1 compatible tool** — an older BMW dealer tool or clone. Genuine used units run €50–€200; clones can be had for €30–€80 from the usual Eastern European suppliers. Reliable brands for clones include Autophix and some Carsoft units.
2. **Peake Research R5/FCX-3** — a dedicated BMW OBD1 code reader, €40–€70 used. Plug-and-play, reads and clears codes. No live data.
3. **20-pin LED blink method** — free. Jump pins 7 and 19 on the 20-pin connector with a test light or LED across the battery. The DME will blink out codes in groups. This is old-school but it works on every E36 OBD1 system.

The 20-pin connector pinout you need:
- **Pin 7:** K-line (diagnostic signal)
- **Pin 19:** Ground
- **Pin 20:** +12V

For live data, INPA running on a laptop with a genuine or quality clone K+DCAN cable (€15–€40) is the gold standard. It reads M50/M52/S50 DMEs natively and gives you actual sensor values, not just codes.

---

## Complete E36 OBD1 Fault Code Table

The following codes apply to the Siemens MS41 / MS42, Bosch Motronic M3.1, M3.3, and M5.2 DMEs fitted across E36 variants. Not all codes are active on all DMEs — engine-specific notes are included where relevant.

| Code | Description | Likely Cause | First Check |
|------|-------------|--------------|-------------|
| **1000** | No faults stored | — | — |
| **1010** | Idle air control valve (ICV/ISV) — signal fault | Dirty or seized ICV, wiring | Resistance across ICV: 8–16 Ω. Part: BMW 13411436149 |
| **1020** | Coolant temperature sensor — open/short circuit | Failed CTS, corroded connector | Resistance at 20°C: ~2.5 kΩ; at 80°C: ~300 Ω. Part: BMW 13621703862 |
| **1030** | Coolant temperature sensor — implausible signal | Sensor reading stuck or inconsistent | Compare ICV correction % in INPA — if idle control is maxed, CTS is suspect |
| **1040** | Intake air temperature sensor — signal fault | Failed IAT in airflow meter (M50B25/S50B30) | IAT is integral to AFM on M50 — AFM replacement needed if IAT fails. Part: BMW 13621703259 |
| **1050** | Throttle position sensor — idle switch open | Failed TPS, misadjusted switch | Check 0 Ω across idle switch with throttle fully closed |
| **1060** | Throttle position sensor — WOT switch open | Failed TPS, wiring | Check switch closes at ~85% throttle travel |
| **1070** | Oxygen sensor — signal absent (bank 1) | Failed O2 sensor, wiring, exhaust leak | NTK or Bosch OEM replacement: BMW 11781742050, ~€35–€55 |
| **1080** | Oxygen sensor — rich/lean adaptation at limit | Fueling issue, injector leak or vacuum leak | Check short-term and long-term fuel trims in INPA |
| **1085** | Oxygen sensor — adaptation at lower limit (lean) | Vacuum leak, lean injector, low fuel pressure | Smoke test or carb cleaner, fuel pressure spec: 3.0 bar (M50) |
| **1090** | Airflow meter — signal implausible | Dirty or failing AFM (hot film or hot wire) | Spray AFM cleaner (CRC 05110) into AFM element, recheck. Replacement AFM: Bosch 0280217114, ~€80–€140 used |
| **1100** | Fuel injector — cylinder 1 | Failed injector, wiring | Resistance: 14–17 Ω (high impedance, M50). Part: BMW 13641734776 |
| **1101** | Fuel injector — cylinder 2 | As above | |
| **1102** | Fuel injector — cylinder 3 | As above | |
| **1103** | Fuel injector — cylinder 4 | As above | |
| **1104** | Fuel injector — cylinder 5 | As above | |
| **1105** | Fuel injector — cylinder 6 | As above | |
| **1110** | Knock sensor 1 — signal fault | Failed knock sensor, wiring, loose torque | Torque spec: 20 Nm. Part: BMW 12141741534, ~€25–€40 |
| **1120** | Knock sensor 2 — signal fault (M50/S50 6-cyl) | As above | Second sensor on rear of block |
| **1130** | Camshaft position sensor — no signal | Failed CPS, reluctor ring, wiring | Part: BMW 12141703221, ~€30–€50 |
| **1140** | Crankshaft position sensor — no signal | Failed CKP, wiring, ring damaged | Engine will not start. Part: BMW 12141703221 (shared on some variants) |
| **1150** | VANOS — mechanical fault (M50TU, M52, S50B32) | VANOS solenoid, oil pressure, chain wear | Check VANOS solenoid: 18–22 Ω. Rebuild kit: ~€80–€150 |
| **1160** | VANOS solenoid — electrical fault | Solenoid wiring, failed solenoid | Same as above — isolate electrical first |
| **1170** | EWS/immobiliser — no signal or mismatch | EWS module, ring antenna, or DME mismatch | EWS3 antenna failure is common on 1996–1999 builds |
| **1180** | Fuel pump relay — circuit fault | Failed relay, wiring | Relay part: BMW 13901433073 or generic Hella 4RD960388 |
| **1190** | EVAP purge valve — electrical fault | Failed purge solenoid, wiring | Resistance: ~20–30 Ω. Part: BMW 16131180380 |
| **1200** | Secondary air injection — pump or valve fault | Pump seized, valve stuck, wiring | Common failure on high-mileage M50. Pump: ~€60–€90 aftermarket |
| **1210** | Idle speed too high after warm-up | Vacuum leak, ICV stuck open | ICV cleaning often resolves: socket head cap screws, Torx T20 |
| **1220** | Idle speed too low | ICV dirty, vacuum leak on intake side | Check brake booster hose — common split point on E36 |
| **1230** | Mixture adaptation — rich limit reached | Injector leak, MAF overcounting | Long-term trim in INPA: healthy range ±10% |
| **1240** | Mixture adaptation — lean limit reached | Vacuum leak, low fuel pressure, MAF undercounting | Fuel pressure regulator: BMW 13531720133, ~€25–€45 |

---

## M50 vs M52 vs S50 — Code Differences That Catch People Out

The M50B25 (non-TU) runs Bosch M3.1 and **does not have VANOS** — ignore any VANOS-related codes if you're on a pre-TU engine. The M50TU and all M52 engines run MS41/MS41.1 with single VANOS. The S50B32 (Euro) runs MS41 with double VANOS and has a different knock sensor layout.

Key differences that affect code interpretation:

- **M50 (non-TU, 1990–1992):** No VANOS codes (1150/1160). AFM is hot-film type, more sensitive to contamination.
- **M50TU (1992–1995):** Single VANOS, codes 1150/1160 active. CPS signal is shared with VANOS timing.
- **M52 (1995–1999):** MS41.1 or MS42, OBD2 from late 1996 onward depending on VIN and market. If your connector has a 16-pin OBD2 port *and* a 20-pin, it's a transitional build.
- **S50B32 (Euro M3):** Double VANOS, both solenoids monitored. Fault codes 1150 and 1160 can refer to either intake or exhaust cam actuator depending on DME revision.
- **M43/M44 (4-cyl):** Single knock sensor only, no code 1120. ICV is a rotary type, different resistance spec (~22 Ω).

On our M50B25TU swap build, we chased a persistent 1090 (AFM implausible) for weeks before finding a hairline crack in the intake boot between AFM and throttle body — classic unmetered air. Smoke test found it in under two minutes.

---

## Clearing Codes and When Not To

You can clear OBD1 fault codes by disconnecting the DME relay (under the glovebox on the passenger side, relay number 9 in the carrier) for 30 seconds, or through a scan tool. **Do not clear codes before photographing or recording them.** The DME stores adaptive values alongside fault codes — clearing them resets fuel trims, idle adaptations, and VANOS timing corrections. On a high-mileage M52 with worn injectors, this can make the car run noticeably rougher until the DME relearns.

Also: a code that returns within one drive cycle after clearing is an active, present fault. A code that doesn't return after 3–5 drive cycles was likely a transient event — loose connector, brief sensor dropout, or a one-time over-temp condition.

---

## Tools and Adapters Worth Having

| Tool | Use | Price (EU) |
|------|-----|------------|
| INPA + K+DCAN cable (clone) | Full live data, code read/clear | €15–€40 |
| Peake R5/FCX-3 | Standalone code reader, no laptop needed | €40–€70 used |
| Fluke 87V or equivalent | Sensor resistance and voltage testing | €80–€200 |
| CRC 05110 MAF cleaner | AFM element cleaning | €8–€12 |
| Smoke machine or DIY vacuum pump | Finding vacuum leaks | €0–€150 |
| Bosch fuel pressure test kit | FPR and rail pressure | €30–€60 rental/own |

If you're deep into an E36 build or running a fleet of them, a second-hand genuine BMW GT1 or DIS unit (€80–€200 at German parts auctions) is worth it for the ECU flashing and VANOS calibration functions alone.

---

## What's Next

With codes read and documented, the next step depends on what you found. VANOS-related codes (1150/1160) lead directly to our VANOS rebuild guide. Fueling codes in the 1080–1090 range almost always warrant a full fuel system pressure test before throwing parts. Persistent oxygen sensor faults on a car with fresh sensors point upstream — exhaust leaks, misfires, or coolant intrusion.

The E36 OBD1 DME is a robust unit that rarely fails outright. In most cases, the code is pointing at a sensor, a connector, or a mechanical condition — not the DME itself. Work methodically, verify with live data where possible, and don't clear until you've fixed.