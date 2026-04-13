#!/usr/bin/env python3
"""Redesign Schema 2 as a vertical stack.
- Each sub-circuit is full 1200px wide, sections stack top-to-bottom
- No empty areas = no background bleed / tan bug
- Larger fonts, more readable
- Based on original Russian ETM scan layout (002.webp)
"""
import re

with open('public/schemas/e36-wiring.html', 'r', encoding='utf-8') as f:
    html = f.read()

NEW_S2 = '''<svg viewBox="0 0 1200 1660" xmlns="http://www.w3.org/2000/svg"
     font-family="'IBM Plex Mono',monospace" style="background:#131720;display:block">
<defs>
  <symbol id="gnd2v" viewBox="0 0 16 14">
    <line x1="8" y1="0" x2="8" y2="5" stroke="#8a7050" stroke-width="2"/>
    <line x1="0" y1="5" x2="16" y2="5" stroke="#8a7050" stroke-width="2.5"/>
    <line x1="3" y1="9"  x2="13" y2="9"  stroke="#8a7050" stroke-width="2"/>
    <line x1="6" y1="13" x2="10" y2="13" stroke="#8a7050" stroke-width="1.5"/>
  </symbol>
  <symbol id="fuse2" viewBox="0 0 48 20">
    <rect x="0" y="4" width="48" height="12" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
    <line x1="12" y1="4" x2="12" y2="16" stroke="#cc3333" stroke-width="1"/>
    <line x1="36" y1="4" x2="36" y2="16" stroke="#cc3333" stroke-width="1"/>
  </symbol>
  <symbol id="motor2" viewBox="0 0 28 28">
    <circle cx="14" cy="14" r="12" fill="#1a1f2b" stroke="currentColor" stroke-width="2"/>
    <text x="14" y="19" fill="currentColor" font-size="12" font-weight="700" text-anchor="middle">M</text>
  </symbol>
  <symbol id="gen2" viewBox="0 0 28 28">
    <circle cx="14" cy="14" r="12" fill="#1a1f2b" stroke="currentColor" stroke-width="2"/>
    <text x="14" y="19" fill="currentColor" font-size="12" font-weight="700" text-anchor="middle">G</text>
  </symbol>
  <symbol id="jct2"><circle r="4" fill="#d4952a"/></symbol>
</defs>

<!-- ═══════ PAGE BACKGROUND ═══════ -->
<rect width="1200" height="1660" fill="#131720" x="0" y="0"/>

<!-- ═══════ HEADER BAR ═══════ -->
<rect x="0" y="0" width="1200" height="30" fill="#191e2b"/>
<rect x="0" y="29" width="1200" height="2" fill="#d4952a" opacity=".5"/>
<text x="14" y="20" fill="#d4952a" font-size="11" font-weight="600" letter-spacing="2">STARTING &amp; CHARGING</text>
<text x="310" y="20" fill="#84817a" font-size="11">· COOLING FAN · EWS IMMOBILIZER · DIAGNOSTIC CONNECTORS</text>
<text x="1186" y="20" fill="#58564f" font-size="9" text-anchor="end">BMW E36 ETM · projekt36.com</text>

<!-- ════════════════════════════════════════════════════════════
     SECTION 1: STARTING & CHARGING
════════════════════════════════════════════════════════════ -->
<rect x="0" y="36" width="1200" height="16" fill="rgba(212,149,42,.08)"/>
<text x="14" y="49" fill="#d4952a" font-size="11" font-weight="600" letter-spacing="1.5">STARTING &amp; CHARGING</text>

<!-- ── FUSES (left column) ── -->

<!-- F108 200A fusible link -->
<rect x="20" y="64" width="80" height="24" fill="#1d2330" stroke="#cc3333" stroke-width="2"/>
<text x="26" y="80" fill="#cc3333" font-size="11" font-weight="600">F108  200A</text>
<text x="108" y="80" fill="#84817a" font-size="10">Fusible link (main)</text>

<!-- F106 50A -->
<rect x="20" y="96" width="80" height="22" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="26" y="111" fill="#cc3333" font-size="10.5">F106  50A</text>
<text x="108" y="111" fill="#84817a" font-size="10">Engine main fuse</text>

<!-- F101 50A -->
<rect x="20" y="126" width="80" height="22" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="26" y="141" fill="#cc3333" font-size="10.5">F101  50A</text>
<text x="108" y="141" fill="#84817a" font-size="10">Fan / accessories</text>

<!-- F37 50A -->
<rect x="20" y="156" width="80" height="22" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="26" y="171" fill="#cc3333" font-size="10.5">F37   50A</text>
<text x="108" y="171" fill="#84817a" font-size="10">Fan / accessories 2</text>

<!-- F34 30A -->
<rect x="20" y="186" width="80" height="22" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="26" y="201" fill="#cc3333" font-size="10.5">F34   30A</text>
<text x="108" y="201" fill="#84817a" font-size="10">Alternator excitation</text>

<!-- F30 7.5A -->
<rect x="20" y="216" width="80" height="22" fill="#1d2330" stroke="#ee8833" stroke-width="1.5"/>
<text x="26" y="231" fill="#ee8833" font-size="10.5">F30  7.5A</text>
<text x="108" y="231" fill="#84817a" font-size="10">OBD-II  +12V  (pin 16)</text>

<!-- F1 7.5A -->
<rect x="20" y="246" width="80" height="22" fill="#1d2330" stroke="#ee8833" stroke-width="1.5"/>
<text x="26" y="261" fill="#ee8833" font-size="10.5">F1   7.5A</text>
<text x="108" y="261" fill="#84817a" font-size="10">EWS + ignition relay</text>

<!-- F14 5A -->
<rect x="20" y="276" width="80" height="22" fill="#1d2330" stroke="#ee8833" stroke-width="1.5"/>
<text x="26" y="291" fill="#ee8833" font-size="10.5">F14   5A</text>
<text x="108" y="291" fill="#84817a" font-size="10">EWS module supply</text>

<!-- Main power rail (vertical red line) -->
<line x1="60" y1="88" x2="60" y2="310" stroke="#cc3333" stroke-width="2"/>
<use href="#jct2" transform="translate(60,97)"/>
<use href="#jct2" transform="translate(60,127)"/>
<use href="#jct2" transform="translate(60,157)"/>
<use href="#jct2" transform="translate(60,187)"/>

<!-- ── BATTERY [1] ── -->
<rect x="240" y="64" width="130" height="50" fill="#1d2330" stroke="#6abf69" stroke-width="2.5"/>
<text x="255" y="82" fill="#84817a" font-size="10">[1]</text>
<text x="275" y="82" fill="#6abf69" font-size="13" font-weight="700">BATTERY</text>
<text x="255" y="100" fill="#ecebe6" font-size="10">＋12 V  ·  −  (trunk)</text>
<text x="255" y="113" fill="#58564f" font-size="9">Lead-acid 70 Ah typ.</text>

<!-- Battery → F108 wire -->
<line x1="305" y1="64" x2="305" y2="52" stroke="#cc3333" stroke-width="2.5"/>
<line x1="305" y1="52" x2="60"  y2="52" stroke="#cc3333" stroke-width="2.5"/>
<line x1="60"  y1="52" x2="60"  y2="64" stroke="#cc3333" stroke-width="2.5"/>
<text x="170" y="48" fill="#cc3333" font-size="9">35.0 Rt  (battery main)</text>

<!-- ── IGNITION SWITCH [2] ── -->
<rect x="240" y="140" width="130" height="70" fill="#1d2330" stroke="#ee8833" stroke-width="1.8"/>
<text x="255" y="158" fill="#84817a" font-size="10">[2]</text>
<text x="275" y="158" fill="#ecebe6" font-size="12" font-weight="600">IGN SWITCH</text>
<text x="255" y="175" fill="#ee8833" font-size="10">0 = Off</text>
<text x="320" y="175" fill="#ee8833" font-size="10">I = Accessories</text>
<text x="255" y="190" fill="#ee8833" font-size="10">II = On (+KL15)</text>
<text x="320" y="190" fill="#ee8833" font-size="10">III = Start</text>
<text x="255" y="205" fill="#58564f" font-size="9">Connector X2 · 6-pin</text>

<!-- IGN → battery wire -->
<line x1="305" y1="140" x2="305" y2="114" stroke="#cc3333" stroke-width="2"/>
<text x="310" y="130" fill="#cc3333" font-size="9">4.0 Rt/Gn</text>

<!-- ── STARTER MOTOR [3] ── -->
<rect x="430" y="130" width="150" height="80" fill="#1d2330" stroke="#cc3333" stroke-width="2"/>
<text x="445" y="150" fill="#84817a" font-size="10">[3]</text>
<use href="#motor2" x="500" y="142" width="28" height="28" color="#cc3333"/>
<text x="445" y="180" fill="#ecebe6" font-size="12" font-weight="600">STARTER</text>
<text x="445" y="196" fill="#84817a" font-size="10">30 pin = B+  50 pin = KL50</text>
<text x="445" y="208" fill="#58564f" font-size="9">Bosch 1.1 kW (6-cyl)</text>

<!-- IGN III → starter (orange = KL50) -->
<line x1="370" y1="165" x2="430" y2="165" stroke="#ee8833" stroke-width="1.5"/>
<text x="373" y="160" fill="#ee8833" font-size="9">4.0 Rt/Ws  KL50</text>
<!-- Battery → starter B+ (thick black) -->
<line x1="305" y1="114" x2="305" y2="100" stroke="#cc3333" stroke-width="1.5"/>
<line x1="305" y1="100" x2="430" y2="100" stroke="#333" stroke-width="3"/>
<line x1="430" y1="100" x2="430" y2="150" stroke="#333" stroke-width="3"/>
<text x="350" y="96" fill="#555" font-size="9">25.0 Sw  (B+)</text>

<!-- ── ALTERNATOR [4] ── -->
<rect x="430" y="64" width="150" height="58" fill="#1d2330" stroke="#5488cc" stroke-width="2"/>
<text x="445" y="82" fill="#84817a" font-size="10">[4]</text>
<use href="#gen2" x="500" y="68" width="28" height="28" color="#5488cc"/>
<text x="445" y="106" fill="#ecebe6" font-size="12" font-weight="600">ALTERNATOR</text>
<text x="445" y="120" fill="#84817a" font-size="10">B+ · D+ · DF  Bosch</text>

<!-- Alt → battery (charge wire) -->
<line x1="430" y1="82" x2="390" y2="82" stroke="#cc3333" stroke-width="2"/>
<line x1="390" y1="82" x2="390" y2="89" stroke="#cc3333" stroke-width="2"/>
<text x="335" y="78" fill="#cc3333" font-size="9">6.0 Rt  (B+)</text>

<!-- ── DME / ECU [5] ── -->
<rect x="640" y="64" width="200" height="100" fill="#1d2330" stroke="#a878d0" stroke-width="2.5"/>
<text x="656" y="82" fill="#84817a" font-size="10">[5]</text>
<text x="680" y="82" fill="#a878d0" font-size="13" font-weight="700">DME / ECU</text>
<text x="656" y="100" fill="#84817a" font-size="10">Motronic M1.7 / 1.8 / 3.3.1</text>
<text x="656" y="114" fill="#ecebe6" font-size="10">B5 · B3 · B2  starter relay ctrl</text>
<text x="656" y="127" fill="#ecebe6" font-size="10">D1 · D2  charge sense / K-line</text>
<text x="656" y="140" fill="#ecebe6" font-size="10">Pin 7 OBD-II ← K-line (diag.)</text>
<text x="656" y="155" fill="#58564f" font-size="9">Location: E-box right of firewall</text>

<!-- IGN → DME -->
<line x1="580" y1="175" x2="640" y2="110" stroke="#a878d0" stroke-width="1.2" stroke-dasharray="4 2"/>
<text x="585" y="155" fill="#a878d0" font-size="9">+KL15 signal</text>

<!-- ── INSTRUMENT CLUSTER [6] ── -->
<rect x="640" y="176" width="200" height="75" fill="#1d2330" stroke="#6abf69" stroke-width="1.8"/>
<text x="656" y="194" fill="#84817a" font-size="10">[6]</text>
<text x="680" y="194" fill="#6abf69" font-size="12" font-weight="600">CLUSTER / IKE</text>
<text x="656" y="212" fill="#ecebe6" font-size="10">Charge warn · Rev counter</text>
<text x="656" y="227" fill="#ecebe6" font-size="10">D+ feed from alternator</text>
<text x="656" y="241" fill="#58564f" font-size="9">K-bus: 0.5 Br/Sw  ←→ DME</text>

<!-- Alt D+ → cluster -->
<line x1="580" y1="95" x2="640" y2="205" stroke="#6abf69" stroke-width="1" stroke-dasharray="3 2"/>
<text x="598" y="140" fill="#6abf69" font-size="9">D+  0.35 Gn/Ws</text>

<!-- ── WIRE COLOUR REFERENCE PANEL ── -->
<rect x="880" y="64" width="300" height="260" fill="#181d28" stroke="rgba(212,149,42,.2)"/>
<text x="896" y="84" fill="#d4952a" font-size="11" font-weight="600" letter-spacing="1">WIRE REFERENCE</text>
<g font-size="10" fill="#b8b5ae">
  <text x="896" y="104">35.0 Rt          — Battery positive main</text>
  <text x="896" y="119">25.0 Sw          — Starter B+ (thick black)</text>
  <text x="896" y="134">6.0 Rt            — Alternator output</text>
  <text x="896" y="149">4.0 Rt/Gn      — Ignition switch to bat.</text>
  <text x="896" y="164">4.0 Rt/Ws      — KL50 start signal</text>
  <text x="896" y="179">0.35 Gn/Ws   — Alternator D+ charge</text>
  <text x="896" y="194">0.5 Br/Sw       — K-bus serial line</text>
  <text x="896" y="209">0.35 Ws/Vi     — K-line OBD pin 7</text>
  <text x="896" y="224">Br                   — Ground (always brown)</text>
</g>
<text x="896" y="250" fill="#d4952a" font-size="10" font-weight="600">FUSE BOX (engine bay)</text>
<text x="896" y="265" fill="#58564f" font-size="9">F108 = fusible link (red)</text>
<text x="896" y="278" fill="#58564f" font-size="9">F106, F101, F37 = 50A bolt-on</text>
<text x="896" y="291" fill="#58564f" font-size="9">F30, F1, F14 = blade fuse box</text>
<text x="896" y="308" fill="#58564f" font-size="9">X6001 = engine bay ground point</text>
<text x="896" y="320" fill="#58564f" font-size="9">X6002 = body ground (firewall)</text>

<!-- Ground symbols -->
<use href="#gnd2v" x="300" y="305" width="16" height="14"/>
<text x="318" y="320" fill="#8a7050" font-size="9">X6001 engine bay</text>
<use href="#gnd2v" x="460" y="305" width="16" height="14"/>
<text x="478" y="320" fill="#8a7050" font-size="9">X6001</text>
<use href="#gnd2v" x="650" y="305" width="16" height="14"/>
<text x="668" y="320" fill="#8a7050" font-size="9">X6002</text>

<!-- Section border -->
<rect x="8" y="52" width="1184" height="290" fill="none" stroke="rgba(212,149,42,.15)" stroke-dasharray="6 3"/>

<!-- ════════════════════════════════════════════════════════════
     SECTION 2: COOLING FAN
════════════════════════════════════════════════════════════ -->
<rect x="0" y="360" width="1200" height="16" fill="rgba(84,136,204,.07)"/>
<text x="14" y="373" fill="#5488cc" font-size="11" font-weight="600" letter-spacing="1.5">COOLING FAN</text>
<rect x="8" y="380" width="1184" height="190" fill="none" stroke="rgba(84,136,204,.15)" stroke-dasharray="6 3"/>

<!-- F101 50A -->
<rect x="30" y="396" width="80" height="22" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="36" y="411" fill="#cc3333" font-size="10.5">F101  50A</text>
<!-- F37 50A -->
<rect x="30" y="426" width="80" height="22" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="36" y="441" fill="#cc3333" font-size="10.5">F37   50A</text>

<!-- power rail down -->
<line x1="70" y1="418" x2="70" y2="540" stroke="#cc3333" stroke-width="1.8"/>
<use href="#jct2" transform="translate(70,418)"/>
<use href="#jct2" transform="translate(70,448)"/>

<!-- Fan relay K -->
<rect x="180" y="390" width="140" height="50" fill="#1d2330" stroke="#ee8833" stroke-width="1.8"/>
<text x="194" y="409" fill="#ee8833" font-size="11" font-weight="600">K  FAN RELAY</text>
<rect x="194" y="415" width="28" height="18" fill="none" stroke="#ee8833" stroke-dasharray="3 2"/>
<text x="194" y="435" fill="#84817a" font-size="10">Coil: +KL15 trigger</text>

<!-- Thermal switch [10] -->
<rect x="380" y="390" width="160" height="50" fill="#1d2330" stroke="#ee8833" stroke-width="1.8"/>
<text x="395" y="408" fill="#84817a" font-size="10">[10]</text>
<text x="420" y="408" fill="#ecebe6" font-size="11" font-weight="600">THERMO SW</text>
<text x="395" y="425" fill="#ecebe6" font-size="10">92 °C  on  /  87 °C  off</text>
<text x="395" y="437" fill="#58564f" font-size="9">Coolant pipe, rear engine</text>

<!-- wire relay → thermo -->
<line x1="320" y1="415" x2="380" y2="415" stroke="#33aa33" stroke-width="1.2"/>
<text x="325" y="411" fill="#33aa33" font-size="9">0.35 Sw/Gr</text>

<!-- Fan motor [9] -->
<rect x="600" y="385" width="160" height="65" fill="#1d2330" stroke="#5488cc" stroke-width="2"/>
<text x="616" y="403" fill="#84817a" font-size="10">[9]</text>
<use href="#motor2" x="658" y="392" width="28" height="28" color="#5488cc"/>
<text x="616" y="437" fill="#ecebe6" font-size="12" font-weight="600">AUX FAN MOTOR</text>
<text x="616" y="450" fill="#58564f" font-size="9">Pusher type · 400W</text>

<!-- relay → motor -->
<line x1="540" y1="415" x2="600" y2="418" stroke="#cc3333" stroke-width="1.8"/>
<text x="547" y="411" fill="#cc3333" font-size="9">6.0 Rt/Bl  (+)</text>

<!-- ground fan motor -->
<use href="#gnd2v" x="670" y="453" width="16" height="14"/>
<text x="688" y="468" fill="#8a7050" font-size="9">X6001</text>

<!-- power to relay -->
<line x1="70" y1="448" x2="180" y2="415" stroke="#cc3333" stroke-width="1.8"/>
<text x="100" y="437" fill="#cc3333" font-size="9">6.0 Rt/Bl</text>

<!-- Notes -->
<rect x="880" y="390" width="300" height="140" fill="#181d28" stroke="rgba(84,136,204,.2)"/>
<text x="896" y="408" fill="#5488cc" font-size="11" font-weight="600">SWAP NOTE: M43 → M50</text>
<text x="896" y="425" fill="#b8b5ae" font-size="10">M43 fan assembly is smaller.</text>
<text x="896" y="440" fill="#b8b5ae" font-size="10">Swap to 6-cyl. fan + shroud.</text>
<text x="896" y="455" fill="#b8b5ae" font-size="10">Thermal switch [10] stays same.</text>
<text x="896" y="470" fill="#cc3333" font-size="10">E36 M50 runs HOT without</text>
<text x="896" y="483" fill="#cc3333" font-size="10">correct fan — check before drive.</text>
<text x="896" y="498" fill="#58564f" font-size="9">Aux fan relay: behind headlight L</text>
<text x="896" y="511" fill="#58564f" font-size="9">Thermal switch: rear coolant line</text>

<!-- ════════════════════════════════════════════════════════════
     SECTION 3: EWS IMMOBILIZER
════════════════════════════════════════════════════════════ -->
<rect x="0" y="590" width="1200" height="16" fill="rgba(168,120,208,.07)"/>
<text x="14" y="603" fill="#a878d0" font-size="11" font-weight="600" letter-spacing="1.5">EWS IMMOBILIZER</text>
<rect x="8" y="610" width="1184" height="200" fill="none" stroke="rgba(168,120,208,.15)" stroke-dasharray="6 3"/>

<!-- Fuses -->
<rect x="30" y="626" width="80" height="22" fill="#1d2330" stroke="#ee8833" stroke-width="1.5"/>
<text x="36" y="641" fill="#ee8833" font-size="10.5">F14   5A</text>
<rect x="30" y="656" width="80" height="22" fill="#1d2330" stroke="#ee8833" stroke-width="1.5"/>
<text x="36" y="671" fill="#ee8833" font-size="10.5">F1   7.5A</text>

<!-- EWS module [11] -->
<rect x="180" y="616" width="230" height="80" fill="#1d2330" stroke="#a878d0" stroke-width="2.5"/>
<text x="196" y="636" fill="#84817a" font-size="10">[11]</text>
<text x="225" y="636" fill="#a878d0" font-size="13" font-weight="700">EWS MODULE</text>
<text x="196" y="654" fill="#84817a" font-size="10">Location: behind glove box</text>
<text x="196" y="669" fill="#84817a" font-size="10">Versions: EWS-I  ·  EWS-II  ·  EWS-III</text>
<text x="196" y="684" fill="#58564f" font-size="9">Connector X11 · 12-pin</text>

<!-- wire supply to EWS -->
<line x1="110" y1="637" x2="180" y2="637" stroke="#ee8833" stroke-width="1.5"/>
<text x="118" y="633" fill="#ee8833" font-size="9">1.0 Rt/Gn</text>

<!-- EWS Function 1: DME signal -->
<rect x="470" y="616" width="280" height="60" fill="#1d2330" stroke="#cc3333" stroke-width="1.5" stroke-dasharray="4 2"/>
<text x="486" y="636" fill="#cc3333" font-size="11" font-weight="600">① DME RELEASE SIGNAL</text>
<text x="486" y="652" fill="#b8b5ae" font-size="10">Pin 7 · green wire · X20 connector</text>
<text x="486" y="666" fill="#58564f" font-size="9">EWS codes engine: DME checks code every start</text>

<!-- EWS Function 2: Starter lockout -->
<rect x="470" y="686" width="280" height="60" fill="#1d2330" stroke="#cc3333" stroke-width="1.5" stroke-dasharray="4 2"/>
<text x="486" y="706" fill="#cc3333" font-size="11" font-weight="600">② STARTER LOCKOUT</text>
<text x="486" y="722" fill="#b8b5ae" font-size="10">2× thick wires · relay in starter circuit</text>
<text x="486" y="736" fill="#58564f" font-size="9">EWS relay cuts starter signal if code mismatch</text>

<!-- EWS → functions arrows -->
<line x1="410" y1="650" x2="470" y2="646" stroke="#a878d0" stroke-width="1.2"/>
<line x1="410" y1="650" x2="410" y2="716" stroke="#a878d0" stroke-width="1.2"/>
<line x1="410" y1="716" x2="470" y2="716" stroke="#a878d0" stroke-width="1.2"/>

<!-- Bypass warning box -->
<rect x="800" y="616" width="380" height="170" fill="rgba(204,51,51,.07)" stroke="#cc3333" stroke-width="1.5"/>
<text x="816" y="636" fill="#cc3333" font-size="12" font-weight="700">⚠  SWAP CRITICAL — EWS</text>
<text x="816" y="656" fill="#b8b5ae" font-size="10">Must bypass BOTH functions.</text>
<text x="816" y="672" fill="#b8b5ae" font-size="10">Missing ① = no spark, engine cranks but</text>
<text x="816" y="687" fill="#b8b5ae" font-size="10">          does not fire.</text>
<text x="816" y="703" fill="#b8b5ae" font-size="10">Missing ② = starter will not crank at all.</text>
<text x="816" y="725" fill="#5488cc" font-size="10" font-weight="600">Best solution:</text>
<text x="816" y="741" fill="#5488cc" font-size="10">OBD1 M50TU  413 red-label ECU = no EWS</text>
<text x="816" y="757" fill="#58564f" font-size="9">M52: always EWS — needs delete chip (~€60)</text>
<text x="816" y="771" fill="#58564f" font-size="9">EWS-I / II delete: simpler. EWS-III: harder.</text>

<!-- ════════════════════════════════════════════════════════════
     SECTION 4: DIAGNOSTIC CONNECTORS
════════════════════════════════════════════════════════════ -->
<rect x="0" y="830" width="1200" height="16" fill="rgba(100,191,105,.07)"/>
<text x="14" y="843" fill="#6abf69" font-size="11" font-weight="600" letter-spacing="1.5">DIAGNOSTIC CONNECTORS</text>
<rect x="8" y="850" width="1184" height="310" fill="none" stroke="rgba(100,191,105,.15)" stroke-dasharray="6 3"/>

<!-- ── OBD-II 16-PIN [7] ── -->
<rect x="20" y="866" width="560" height="280" fill="none" stroke="rgba(100,191,105,.2)" stroke-dasharray="4 2"/>
<text x="36" y="884" fill="#6abf69" font-size="11" font-weight="600" letter-spacing="1">16-PIN OBD-II DIAGNOSTIC PORT  [7]</text>
<text x="36" y="898" fill="#58564f" font-size="9">Location: passenger footwell, left of centre console</text>

<!-- Connector shape -->
<rect x="36" y="906" width="180" height="65" fill="#1d2330" stroke="#6abf69" stroke-width="2.5" rx="4"/>
<text x="96" y="929" fill="#6abf69" font-size="14" font-weight="700" text-anchor="middle">OBD-II</text>
<text x="96" y="946" fill="#84817a" font-size="10" text-anchor="middle">16-pin D-sub</text>
<text x="36" y="975" fill="#58564f" font-size="9">Upper row: 1–8  ·  Lower row: 9–16</text>

<!-- Pin assignments OBD-II -->
<g font-size="10" fill="#b8b5ae">
  <text x="235" y="920">Pin 4   — Chassis GND          2.5 Br</text>
  <text x="235" y="935">Pin 5   — Signal GND           0.75 Gn/Br</text>
  <text x="235" y="950">Pin 7   — K-line to DME         0.35 Ws/Vi</text>
  <text x="235" y="965">Pin 8   — K-line 2 / ADS bridge</text>
  <text x="235" y="980">Pin 14  — CAN Low                0.5 Rt/Ge/Ws</text>
  <text x="235" y="995">Pin 15  — CAN High</text>
  <text x="235" y="1010">Pin 16  — +12V permanent       F30 7.5A · 2.5 Rt/Bl</text>
</g>

<!-- Modules connected -->
<text x="36" y="1010" fill="#d4952a" font-size="10" font-weight="600">Connected modules:</text>
<rect x="36" y="1018" width="160" height="20" fill="#1d2330" stroke="#a878d0"/>
<text x="44" y="1032" fill="#a878d0" font-size="9">→ DME engine ECU (K-line)</text>
<rect x="36" y="1042" width="160" height="20" fill="#1d2330" stroke="#5488cc"/>
<text x="44" y="1056" fill="#5488cc" font-size="9">→ ABS / ASC module</text>
<rect x="36" y="1066" width="160" height="20" fill="#1d2330" stroke="#ee8833"/>
<text x="44" y="1080" fill="#ee8833" font-size="9">→ Instrument cluster</text>
<rect x="36" y="1090" width="160" height="20" fill="#1d2330" stroke="#6abf69"/>
<text x="44" y="1104" fill="#6abf69" font-size="9">→ EWS module</text>
<rect x="36" y="1114" width="160" height="20" fill="#1d2330" stroke="#84817a"/>
<text x="44" y="1128" fill="#84817a" font-size="9">→ Airbag SRS module</text>

<!-- ── ADS 20-PIN [8] ── -->
<rect x="620" y="866" width="560" height="280" fill="none" stroke="rgba(238,136,51,.2)" stroke-dasharray="4 2"/>
<text x="636" y="884" fill="#ee8833" font-size="11" font-weight="600" letter-spacing="1">20-PIN ADS CONNECTOR  [8]</text>
<text x="636" y="898" fill="#58564f" font-size="9">Location: under bonnet, left side near firewall (round connector)</text>

<!-- ADS connector shape (round) -->
<ellipse cx="740" cy="940" rx="55" ry="42" fill="#1d2330" stroke="#ee8833" stroke-width="2.5"/>
<text x="740" y="938" fill="#ee8833" font-size="14" font-weight="700" text-anchor="middle">ADS</text>
<text x="740" y="956" fill="#84817a" font-size="9" text-anchor="middle">Round · 20 pins</text>

<!-- Pin assignments ADS -->
<g font-size="10" fill="#b8b5ae">
  <text x="812" y="916">Pin 1   — TXD serial transmit     0.35 Ws/Gn</text>
  <text x="812" y="931">Pin 7   — K-line (OBD1 only)</text>
  <text x="812" y="946">Pin 14  — Chassis ground           2.5 Br</text>
  <text x="812" y="961">Pin 17  — TXD data                  0.35 Ws/Gn</text>
  <text x="812" y="976">Pin 19  — +12V battery supply</text>
  <text x="812" y="991">Pin 20  — +12V ignition supply     +KL15</text>
</g>

<!-- OBD1 vs OBD2 note -->
<rect x="636" y="1008" width="530" height="70" fill="rgba(84,136,204,.07)" stroke="rgba(84,136,204,.3)"/>
<text x="650" y="1026" fill="#5488cc" font-size="11" font-weight="600">OBD1 vs OBD2</text>
<text x="650" y="1043" fill="#b8b5ae" font-size="10">Pre-Jan 1996:  ADS connector (serial) · use ADS cable, NOT K+DCAN</text>
<text x="650" y="1059" fill="#b8b5ae" font-size="10">Post-Jan 1996: OBD-II 16-pin · use K+DCAN USB cable with INPA</text>
<text x="650" y="1073" fill="#58564f" font-size="9">Pin 8 OBD-II bridges to ADS pin 7 — required for INPA on OBD1</text>

<!-- ════════════════════════════════════════════════════════════
     COMPONENT INDEX
════════════════════════════════════════════════════════════ -->
<rect x="0" y="1180" width="1200" height="16" fill="rgba(212,149,42,.06)"/>
<text x="14" y="1193" fill="#d4952a" font-size="11" font-weight="600" letter-spacing="1.5">COMPONENT INDEX</text>
<rect x="8" y="1200" width="1184" height="180" fill="#181d28" stroke="rgba(212,149,42,.15)"/>

<g font-size="10" fill="#b8b5ae">
  <!-- col 1 -->
  <text x="24" y="1220">[1]  Battery (trunk-mounted)</text>
  <text x="24" y="1236">[2]  Ignition switch</text>
  <text x="24" y="1252">[3]  Starter motor</text>
  <text x="24" y="1268">[4]  Alternator</text>
  <text x="24" y="1284">[5]  DME / Engine ECU</text>
  <text x="24" y="1300">[6]  Instrument cluster (IKE)</text>
  <text x="24" y="1316">[7]  16-pin OBD-II port</text>
  <text x="24" y="1332">[8]  20-pin ADS connector</text>
  <text x="24" y="1348">[9]  Aux cooling fan motor</text>
  <text x="24" y="1364">[10] Thermal switch (fan)</text>
  <text x="24" y="1380">[11] EWS immobilizer module</text>
  <!-- col 2 -->
  <text x="340" y="1220">F1    7.5A  — EWS / ign relay supply</text>
  <text x="340" y="1236">F14   5A    — EWS module</text>
  <text x="340" y="1252">F30   7.5A  — OBD-II +12V (pin 16)</text>
  <text x="340" y="1268">F34   30A  — Alternator excitation</text>
  <text x="340" y="1284">F37   50A  — Fan / accessories</text>
  <text x="340" y="1300">F101  50A  — Fan / accessories</text>
  <text x="340" y="1316">F106  50A  — Engine main</text>
  <text x="340" y="1332">F108  200A — Fusible link</text>
  <text x="340" y="1348">K          — Aux fan relay</text>
  <text x="340" y="1364">G101       — Engine bay ground</text>
  <text x="340" y="1380">G102       — Chassis ground</text>
  <!-- col 3 wire legend -->
  <text x="700" y="1220" fill="#84817a">Wire gauge / colour legend:</text>
  <text x="700" y="1236">Rt = Red      Sw = Black    Br = Brown</text>
  <text x="700" y="1252">Ws = White    Bl = Blue     Gn = Green</text>
  <text x="700" y="1268">Ge = Yellow   Gr = Grey     Or = Orange</text>
  <text x="700" y="1284">Vi = Violet   e.g.  4.0 Rt/Gn = 4mm² Red+Green</text>
  <text x="700" y="1316" fill="#84817a">Colour-coded sections in this diagram:</text>
  <rect x="700" y="1322" width="12" height="10" fill="#cc3333"/>
  <text x="716" y="1331">Red      — Power / fuses / battery</text>
  <rect x="700" y="1338" width="12" height="10" fill="#ee8833"/>
  <text x="716" y="1347">Orange — Ignition / switched power</text>
  <rect x="700" y="1354" width="12" height="10" fill="#5488cc"/>
  <text x="716" y="1363">Blue     — Alternator / charge circuit</text>
  <rect x="700" y="1370" width="12" height="10" fill="#a878d0"/>
  <text x="716" y="1379">Purple  — DME / ECU</text>
  <rect x="700" y="1386" width="12" height="10" fill="#8a7050"/>
  <text x="716" y="1395">Brown — Ground connections</text>
</g>

<!-- Footer note -->
<rect x="8" y="1400" width="1184" height="40" fill="#16192a"/>
<text x="24" y="1416" fill="#58564f" font-size="9">Translated from BMW E36 Electrical Diagrams (Электрические схемы) · H32734. Cross-referenced with BMW E36 ETM (Electrical Troubleshooting Manual).</text>
<text x="24" y="1430" fill="#58564f" font-size="9">Wire specifications reproduced from original. All values are nominal — verify against your specific variant (M43 / M50 / M50TU / M52) and production date.</text>

</svg>'''

# Replace s2-simple content
pattern = r'(<div class="svg-frame" id="s2-simple">)\s*<svg[\s\S]*?</svg>\s*(</div>)'
replacement = r'\g<1>\n    ' + NEW_S2 + r'\n  \g<2>'
updated, n = re.subn(pattern, replacement, html, count=1)
if n == 0:
    print('ERROR: s2-simple div not found!', file=sys.stderr)
else:
    print(f'OK: replaced Schema 2 Overview SVG ({len(NEW_S2)} chars)')

with open('public/schemas/e36-wiring.html', 'w', encoding='utf-8') as f:
    f.write(updated)

print(f'Done — file size: {len(updated)} chars')
