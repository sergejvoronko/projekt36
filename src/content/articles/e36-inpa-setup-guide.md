---
title: "INPA on BMW E36 — Cable, Software, and What You Can Actually Do With It"
description: "INPA on the BMW E36: which cable to buy, how to install the software, what each module shows, and the tests that save time."
pillar: reference
keywords: "bmw e36 inpa, e36 diagnostics, k-dcan cable, inpa setup, bmw obd diagnostic, e36 fault codes"
date: "2026-04-13"
hero: "inpa.webp"
---

## TL;DR

INPA is BMW's factory diagnostic software from the 1990s–2000s. On the E36 it gives you live sensor data, fault code reading/clearing, actuator tests, EWS key coding, and module-level diagnostics that a generic OBD2 scanner can't touch. You need a K-DCAN USB cable (~€20), a Windows laptop, and about an hour to set it up. Once working, it's the most useful tool you own for an E36.

---

## What INPA Does That Generic Scanners Don't

A standard OBD2 Bluetooth dongle reads emission-related fault codes from the DME. That's it. INPA gives you:

- **All module fault codes** — DME, EWS, ABS, instrument cluster, ZKE, airbags, IHKA (climate), LCM, everything
- **Live data streams** — coolant temp, oil temp, throttle position, lambda values, ignition timing, battery voltage, actual vs requested values
- **Actuator tests** — activate the fuel pump relay, idle actuator, cooling fan, individual injectors, and others from the software
- **EWS functions** — read authorization status, code new keys, sync EWS to DME
- **Adaptation reset** — reset throttle body adaptation, idle adaptation after cleaning or replacing components
- **Module identification** — read hardware/software versions, part numbers, VINs stored in modules

This is the difference between knowing a fault code exists and understanding why.

---

## What You Need

### 1. The cable

You need a **K-DCAN USB cable** (also called a PA Soft cable or just INPA cable). This interfaces between your laptop's USB port and the car's OBD2 port.

**What to buy:** FTDI chip-based K-DCAN cable with the switch (or software-switchable). The switch selects between K-line and D-CAN mode — E36 uses K-line.

**What to avoid:** Cheap cables with CH340 or PL2303 chips cause connection issues. FTDI-based cables cost a few euros more but work reliably. Search for "K-DCAN FTDI cable BMW" — budget €15–25.

The E36's OBD port (under the bonnet, near the battery on earlier models, or in the footwell on later models) is a round BMW-specific connector — not the standard OBD2 trapezoid. Later E36s (1996+) have both. The K-DCAN cable for E36 comes with a round BMW adapter, or you can get an adapter separately.

### 2. The laptop

Windows only. The software was written for Windows 98/XP but runs fine on Windows 10/11 in compatibility mode. Requirements:
- **USB port** (for the cable)
- **Minimum 1 GB RAM** (INPA itself is very lightweight)
- **.NET 3.5** (required for some companion tools)
- **Windows 7/10/11** — all work; avoid 64-bit Windows for the oldest INPA versions, but modern INPA 5.0.2 works on 64-bit

A cheap €50 ThinkPad from eBay is ideal — dedicate it to car diagnostics, keep it offline, and it'll outlast the car.

### 3. The software package

The typical INPA package contains:
- **INPA** — the main diagnostic interface
- **NCS Expert** — module coding (change parameters, code retrofits)
- **WinKFP** — ECU flashing and programming
- **Tool32** — low-level module communication (advanced use)
- **EDIABAS** — the communication backend (required by all above)

These tools are widely available in the BMW enthusiast community. A Google search for "BMW INPA 5.0.2 download" will find the package. It's not sold commercially; BMW dealerships use the newer ISTA software, but INPA remains the go-to for older BMWs.

---

## Installation

### Step 1: Install EDIABAS first

EDIABAS is the communication layer everything else depends on. Run the EDIABAS installer, accept defaults. After install, edit `C:\EDIABAS\BIN\EDIABAS.INI`:

```
Interface=EDIC
Port=COM3       ; or whatever COM port your cable appears on
Baud=9600
```

Check the actual COM port number in Windows Device Manager after plugging in the cable.

### Step 2: Install INPA

Run the INPA installer. It installs to `C:\EDIABAS\ECU\` by default. The installer asks for paths — accept defaults.

After installing, navigate to `C:\EDIABAS\INPA\` and check that `.IPO` files exist for your car's modules. The E36-specific files include `DME.IPO`, `EWS.IPO`, `ABS.IPO`, etc.

### Step 3: Configure the COM port

Open **INPA** → **Settings** → **COM Port** — set to match your cable's COM port. Test with the cable plugged in and ignition on: click **Connect** — you should see the E36 model selection.

### Step 4: Install FTDI drivers

If Windows didn't auto-install them, download FTDI drivers from the FTDI website and install. The cable must appear as a COM port in Device Manager under **Ports (COM & LPT)**. If it appears as an unknown device, the driver isn't installed.

---

## Connecting to the Car

1. Plug cable into laptop USB
2. Plug cable into car OBD port (ignition off is fine for connecting)
3. Turn ignition to **position 2** (accessories on, engine off) — this powers the modules
4. Open INPA
5. Select vehicle: **E36 / 3 Series** → select year/engine
6. Select module from the list

The module list shows everything: DME, EWS, ABS, instrument cluster (KOMBI), ZKE body module, airbags (MRS), climate control (IHKA or A/C), LCM, etc.

---

## Module-by-Module: What to Check

### DME (Engine ECU)

Navigate to DME. This is where you spend the most time.

**Fault codes:** The DME stores codes for sensor faults, misfire detection, fuel trim faults. Unlike OBD2, INPA shows BMW-specific codes with full descriptions — not just a P-code lookup.

**Live data:** Select **Messwerte** (measured values). Key channels:
- Coolant temperature (actual vs sensor reading)
- Throttle position (%)
- Lambda / O2 sensor voltage (0.1–0.9 V cycling = sensor working)
- Fuel trim short-term and long-term (ideally ±5%; anything above ±15% indicates a fuelling issue)
- Ignition timing (advance in degrees, varies with load and temp)
- Battery voltage (should be 13.8–14.4 V running)
- Idle speed (target vs actual)

**Adaptation reset:** After cleaning the throttle body or idle control valve, reset adaptations here so the DME relearns from a clean baseline.

### EWS (Immobilizer)

**Fault codes:** "Key not authorized," "communication fault," etc.  
**Key status:** See which key slots are programmed  
**Sync status:** Confirm EWS and DME are synchronized  
**Key teaching:** Program a new transponder key (see the EWS guide)

### ABS

**Fault codes:** Wheel sensor faults, pump motor faults, valve faults  
**Live data:** Wheel speeds (all four, individually) — critical for diagnosing intermittent ABS warning lights. Drive slowly and watch for a wheel speed reading of 0 while the others register correctly. That wheel's sensor or ring is faulty.  
**Actuator test:** Cycle the ABS pump — you'll hear it run briefly

### Instrument Cluster (KOMBI)

**Live data:** Odometer, service interval counter, coolant temp (as received by cluster — useful to compare against DME's reading to find cluster vs sensor issues)  
**Fault codes:** Illumination faults, CAN faults on later models

### ZKE (Central Body Module)

Controls central locking, windows, interior lights, deadlocking, soft-close. Fault codes here cover window regulator faults, lock faults, and switch faults. On a car with window or locking issues, check ZKE before touching any motors.

### LCM (Light Control Module)

**Fault codes:** Bulb failure codes (LCM monitors current draw for each bulb — if current is wrong, it stores a fault even if the bulb appears to work). Useful for tracing which bulb is intermittent.  
**Actuator test:** Turn on individual lights from software — useful when physically checking continuity without a helper.

---

## Practical Examples

### Example 1: Rough idle, no OBD2 code

OBD2 scanner shows nothing. Open INPA → DME → live data. Watch:
- Long-term fuel trim: if it's at +20%, the engine is running lean permanently. Cause: air leak (intake boot crack, loose hose) or weak fuel pump.
- Lambda sensor voltage: if it's stuck at 0.45 V (not cycling), the sensor is dead.
- Coolant temp at idle: if it reads 50°C but the engine feels hot, the sensor is faulty and causing rich fuelling.

### Example 2: ABS light on, no obvious cause

Generic scanner says "wheel speed sensor fault — front left." But which side? INPA live data while driving at 15 km/h shows three wheels at normal speed; one reads 0. That's the failed sensor or corroded tone ring. Saves pulling all four wheels to check.

### Example 3: Post-swap, won't start

After an M50 swap, car cranks but doesn't fire. INPA → EWS shows "key not authorized" fault. The EWS from the donor car isn't matched to the ignition key you're using. Either use the donor key set, or recode EWS to the new key. See the EWS guide.

### Example 4: Charging fault light, alternator tests fine

INPA → DME live data → battery voltage while revving: should climb to 14.2–14.4 V. If it stays at 12.1 V with the engine running, the alternator isn't charging. If it reads 13.8 V at idle but INPA shows a charging fault code, check the voltage regulator separately from the alternator.

---

## NCS Expert — Coding Modules

NCS Expert is a step above INPA — it reads and writes module coding data. On the E36 this is less critical than on later BMWs, but useful for:

- Coding a replacement LCM to match your options (xenons, fog lights, trailer hitch)
- Enabling/disabling ZKE comfort functions (auto-lock while driving, auto-window close with key)
- Coding a replacement instrument cluster to your VIN

NCS Expert is not beginner-friendly. Before changing any coding, **read and save the current coding first** (Profile → Read). This creates a backup you can restore if something goes wrong.

---

## Keeping INPA Reliable

- Use the cable only for diagnostics — don't leave it plugged in with ignition off for extended periods (parasitic drain)
- Keep the laptop dedicated and offline — Windows Update breaking COM port drivers on a car-specific laptop is a real problem
- Back up your `C:\EDIABAS\` folder after a working installation
- INPA is not live-safe — don't use it while driving. Actuator tests are for stationary use only.
