#!/usr/bin/env python3
"""Replace schemas 4, 6, 8, 10 with professional BMW ETM-style English SVGs."""
import re, sys

with open('public/schemas/e36-wiring.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─── SCHEMA 4: EXTERIOR LIGHTING ─────────────────────────────────────────────
S4_SVG = '''<svg viewBox="0 0 1200 700" xmlns="http://www.w3.org/2000/svg" font-family="'IBM Plex Mono',monospace" font-size="9">
<defs>
  <pattern id="grid4" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40,0 L0,0 0,40" fill="none" stroke="rgba(255,255,255,.025)" stroke-width=".5"/>
  </pattern>
  <symbol id="gnd4" viewBox="0 0 14 12">
    <line x1="7" y1="0" x2="7" y2="4" stroke="#6b5a3a" stroke-width="1.5"/>
    <line x1="0" y1="4" x2="14" y2="4" stroke="#6b5a3a" stroke-width="2"/>
    <line x1="2" y1="7" x2="12" y2="7" stroke="#6b5a3a" stroke-width="1.5"/>
    <line x1="4" y1="10" x2="10" y2="10" stroke="#6b5a3a" stroke-width="1"/>
  </symbol>
  <symbol id="jct4"><circle r="3" fill="#d4952a"/></symbol>
  <symbol id="bulb" viewBox="0 0 16 16">
    <circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-width="1.2"/>
    <line x1="5" y1="5" x2="11" y2="11" stroke="currentColor" stroke-width="1"/>
    <line x1="11" y1="5" x2="5" y2="11" stroke="currentColor" stroke-width="1"/>
  </symbol>
</defs>
<!-- Background -->
<rect width="1200" height="700" fill="#131720"/>
<rect width="1200" height="700" fill="url(#grid4)"/>
<!-- HEADER -->
<rect x="0" y="0" width="1200" height="26" fill="#1a1f2b"/>
<rect x="0" y="25" width="1200" height="1" fill="#d4952a" opacity=".4"/>
<text x="12" y="17" fill="#d4952a" font-size="9" font-weight="600" letter-spacing="2">SCHEMA 4</text>
<text x="84" y="17" fill="#84817a" font-size="9">EXTERIOR LIGHTING · LCM · HEADLIGHTS · TURN SIGNALS · BRAKE &amp; TAIL</text>
<text x="1188" y="17" fill="#58564f" font-size="8" text-anchor="end">BMW E36 ETM · projekt36.com</text>

<!-- ═══════════════════════════════════════════════
     POWER &amp; LCM SECTION
═══════════════════════════════════════════════ -->
<rect x="8" y="34" width="290" height="290" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="8" y="34" width="130" height="13" fill="rgba(212,149,42,.07)"/>
<text x="14" y="44" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">POWER &amp; LCM</text>

<!-- Battery -->
<rect x="22" y="58" width="62" height="28" fill="#1d2330" stroke="#6abf69" stroke-width="1.5"/>
<text x="28" y="72" fill="#6abf69" font-size="8" font-weight="600">[1] BAT</text>
<text x="28" y="82" fill="#58564f" font-size="6">12 V lead-acid</text>

<!-- Main fusible link F108 -->
<rect x="22" y="100" width="80" height="18" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="27" y="113" fill="#cc3333" font-size="7.5">F108  200A</text>

<!-- wire bat → F108 -->
<line x1="53" y1="86" x2="53" y2="100" stroke="#cc3333" stroke-width="1.2"/>
<text x="56" y="95" fill="#84817a" font-size="6">6.0 Rt</text>

<!-- Vertical main power rail -->
<line x1="62" y1="118" x2="62" y2="150" stroke="#cc3333" stroke-width="1.5"/>

<!-- F106 50A  F107 50A -->
<rect x="22" y="150" width="55" height="18" fill="#1d2330" stroke="#cc3333"/>
<text x="26" y="162" fill="#cc3333" font-size="7">F106  50A</text>
<rect x="85" y="150" width="55" height="18" fill="#1d2330" stroke="#cc3333"/>
<text x="89" y="162" fill="#cc3333" font-size="7">F107  50A</text>
<use href="#jct4" x="62" y="150"/>
<line x1="62" y1="150" x2="50" y2="150" stroke="#cc3333" stroke-width="1"/>
<line x1="62" y1="150" x2="113" y2="150" stroke="#cc3333" stroke-width="1"/>

<!-- F32 5A  F9 5A (ignition fuses) -->
<rect x="22" y="186" width="50" height="16" fill="#1d2330" stroke="#ee8833"/>
<text x="26" y="197" fill="#ee8833" font-size="7">F32  5A</text>
<rect x="80" y="186" width="50" height="16" fill="#1d2330" stroke="#ee8833"/>
<text x="84" y="197" fill="#ee8833" font-size="7">F9  5A</text>
<text x="22" y="214" fill="#58564f" font-size="6">Ign. supply via F32/F9</text>

<!-- LCM [37] -->
<rect x="130" y="58" width="155" height="55" fill="#1d2330" stroke="#5488cc" stroke-width="1.5"/>
<text x="148" y="76" fill="#5488cc" font-size="10" font-weight="700">[37] LCM</text>
<text x="148" y="89" fill="#84817a" font-size="7">Light Control Module</text>
<text x="148" y="100" fill="#58564f" font-size="6">Connector X37 · 36-pin</text>

<!-- wire F106 → LCM power -->
<line x1="50" y1="168" x2="50" y2="185" stroke="#cc3333" stroke-width="1"/>
<line x1="50" y1="175" x2="130" y2="80" stroke="#cc3333" stroke-width="1" stroke-dasharray="3 2"/>
<text x="60" y="172" fill="#cc3333" font-size="5.5">4.0 Rt/Ws</text>

<!-- Stalk switch [43] -->
<rect x="130" y="130" width="155" height="28" fill="#1d2330" stroke="#ee8833"/>
<text x="145" y="148" fill="#ecebe6" font-size="7.5">[43] Stalk switch</text>
<text x="145" y="158" fill="#58564f" font-size="6">Low beam · Turn signal</text>
<line x1="207" y1="113" x2="207" y2="130" stroke="#ee8833" stroke-width="1"/>

<!-- Hazard / CL switch [41] -->
<rect x="130" y="170" width="155" height="28" fill="#1d2330" stroke="#ee8833"/>
<text x="145" y="188" fill="#ecebe6" font-size="7.5">[41] Hazard / CL switch</text>
<text x="145" y="198" fill="#58564f" font-size="6">Hazard flash · Interior light</text>

<!-- K-bus note -->
<rect x="22" y="235" width="263" height="30" fill="rgba(212,149,42,.04)" stroke="rgba(212,149,42,.2)"/>
<text x="30" y="249" fill="#84817a" font-size="7">K-bus serial line:  0.5 Br/Sw</text>
<text x="30" y="260" fill="#58564f" font-size="6">LCM ↔ Cluster ↔ ZKE IV ↔ Radio</text>

<!-- Ground cluster at bottom of LCM section -->
<text x="22" y="285" fill="#58564f" font-size="6">Grounds: X6001 engine bay  ·  X6002 body</text>
<use href="#gnd4" x="150" y="285" width="14" height="12" color="#6b5a3a"/>
<use href="#gnd4" x="220" y="285" width="14" height="12" color="#6b5a3a"/>

<!-- ═══════════════════════════════════════════════
     FRONT LIGHTS
═══════════════════════════════════════════════ -->
<rect x="308" y="34" width="360" height="290" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="308" y="34" width="100" height="13" fill="rgba(212,149,42,.07)"/>
<text x="314" y="44" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">FRONT LIGHTS</text>

<!-- Left column labels -->
<text x="314" y="62" fill="#84817a" font-size="7" font-weight="600">LEFT</text>
<text x="474" y="62" fill="#84817a" font-size="7" font-weight="600">RIGHT</text>

<!-- Parking [44] [45] -->
<rect x="314" y="68" width="140" height="22" fill="#1d2330" stroke="#cccc33"/>
<use href="#bulb" x="318" y="72" width="16" height="16" color="#cccc33"/>
<text x="340" y="83" fill="#ecebe6" font-size="7.5">[44] Parking light</text>
<rect x="474" y="68" width="140" height="22" fill="#1d2330" stroke="#cccc33"/>
<use href="#bulb" x="478" y="72" width="16" height="16" color="#cccc33"/>
<text x="500" y="83" fill="#ecebe6" font-size="7.5">[45] Parking light</text>
<text x="314" y="59" fill="#58564f" font-size="5.5">0.5 Ge/Sw</text>
<text x="474" y="59" fill="#58564f" font-size="5.5">0.5 Ge/Sw</text>

<!-- Low beam [46] [47] -->
<rect x="314" y="100" width="140" height="22" fill="#1d2330" stroke="#5488cc"/>
<use href="#bulb" x="318" y="104" width="16" height="16" color="#5488cc"/>
<text x="340" y="115" fill="#ecebe6" font-size="7.5">[46] Low beam  H7</text>
<rect x="474" y="100" width="140" height="22" fill="#1d2330" stroke="#5488cc"/>
<use href="#bulb" x="478" y="104" width="16" height="16" color="#5488cc"/>
<text x="500" y="115" fill="#ecebe6" font-size="7.5">[47] Low beam  H7</text>
<text x="314" y="96" fill="#58564f" font-size="5.5">1.5 Ge/Gn</text>
<text x="474" y="96" fill="#58564f" font-size="5.5">1.5 Ge/Gn</text>

<!-- High beam [48] [49] -->
<rect x="314" y="132" width="140" height="22" fill="#1d2330" stroke="#aa44aa"/>
<use href="#bulb" x="318" y="136" width="16" height="16" color="#aa44aa"/>
<text x="340" y="147" fill="#ecebe6" font-size="7.5">[48] High beam  H1</text>
<rect x="474" y="132" width="140" height="22" fill="#1d2330" stroke="#aa44aa"/>
<use href="#bulb" x="478" y="136" width="16" height="16" color="#aa44aa"/>
<text x="500" y="147" fill="#ecebe6" font-size="7.5">[49] High beam  H1</text>
<text x="314" y="128" fill="#58564f" font-size="5.5">1.5 Ge/Vi</text>
<text x="474" y="128" fill="#58564f" font-size="5.5">1.5 Ge/Vi</text>

<!-- Front turn [50] [52] -->
<rect x="314" y="164" width="140" height="22" fill="#1d2330" stroke="#33aa33"/>
<use href="#bulb" x="318" y="168" width="16" height="16" color="#33aa33"/>
<text x="340" y="179" fill="#ecebe6" font-size="7.5">[50] Front turn</text>
<rect x="474" y="164" width="140" height="22" fill="#1d2330" stroke="#33aa33"/>
<use href="#bulb" x="478" y="168" width="16" height="16" color="#33aa33"/>
<text x="500" y="179" fill="#ecebe6" font-size="7.5">[52] Front turn</text>
<text x="314" y="160" fill="#58564f" font-size="5.5">1.0 Gn/Sw  1.0 Gn/Ge</text>

<!-- Side repeaters [51] [53] -->
<rect x="314" y="196" width="140" height="20" fill="#1d2330" stroke="#33aa33" stroke-dasharray="3 2"/>
<text x="322" y="210" fill="#ecebe6" font-size="7">[51] Side repeater</text>
<rect x="474" y="196" width="140" height="20" fill="#1d2330" stroke="#33aa33" stroke-dasharray="3 2"/>
<text x="482" y="210" fill="#ecebe6" font-size="7">[53] Side repeater</text>

<!-- License plate [42] -->
<rect x="314" y="228" width="300" height="22" fill="#1d2330" stroke="#cccc33"/>
<use href="#bulb" x="318" y="232" width="16" height="16" color="#cccc33"/>
<text x="340" y="243" fill="#ecebe6" font-size="7.5">[42] License plate lights (×2)  ·  trunk lid switch</text>
<text x="314" y="224" fill="#58564f" font-size="5.5">0.5 Ge/Sw  · from LCM pin 12</text>

<!-- Leveling [38] [39] [40] -->
<rect x="314" y="264" width="350" height="52" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="4 2"/>
<rect x="314" y="264" width="120" height="12" fill="rgba(212,149,42,.05)"/>
<text x="320" y="273" fill="#d4952a" font-size="7.5" font-weight="600">HEADLIGHT LEVELING</text>
<rect x="322" y="278" width="110" height="20" fill="#1d2330" stroke="#84817a"/>
<text x="330" y="292" fill="#ecebe6" font-size="7">[38] Axle load sensor</text>
<rect x="450" y="278" width="60" height="20" fill="#1d2330" stroke="#5488cc"/>
<circle cx="465" cy="288" r="7" fill="none" stroke="#5488cc" stroke-width="1.2"/>
<text x="461" y="291" fill="#5488cc" font-size="7">M</text>
<text x="448" y="275" fill="#58564f" font-size="5.5">[39] L motor</text>
<rect x="528" y="278" width="60" height="20" fill="#1d2330" stroke="#5488cc"/>
<circle cx="543" cy="288" r="7" fill="none" stroke="#5488cc" stroke-width="1.2"/>
<text x="539" y="291" fill="#5488cc" font-size="7">M</text>
<text x="526" y="275" fill="#58564f" font-size="5.5">[40] R motor</text>
<line x1="432" y1="288" x2="450" y2="288" stroke="#5488cc" stroke-width="1"/>
<line x1="510" y1="288" x2="528" y2="288" stroke="#5488cc" stroke-width="1"/>

<!-- Wire from LCM to front lights area (horizontal bus) -->
<line x1="298" y1="80" x2="314" y2="80" stroke="#d4952a" stroke-width="1" stroke-dasharray="4 2"/>
<text x="300" y="77" fill="#d4952a" font-size="5.5">→ LCM</text>

<!-- ═══════════════════════════════════════════════
     REAR LIGHTS
═══════════════════════════════════════════════ -->
<rect x="680" y="34" width="360" height="290" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="680" y="34" width="95" height="13" fill="rgba(212,149,42,.07)"/>
<text x="686" y="44" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">REAR LIGHTS</text>

<text x="686" y="62" fill="#84817a" font-size="7" font-weight="600">LEFT</text>
<text x="846" y="62" fill="#84817a" font-size="7" font-weight="600">RIGHT</text>

<!-- Rear turn [54] / Rear fog [55] -->
<rect x="686" y="68" width="140" height="22" fill="#1d2330" stroke="#33aa33"/>
<use href="#bulb" x="690" y="72" width="16" height="16" color="#33aa33"/>
<text x="712" y="83" fill="#ecebe6" font-size="7.5">[54] Rear turn</text>
<rect x="846" y="68" width="140" height="22" fill="#1d2330" stroke="#ee5555"/>
<use href="#bulb" x="850" y="72" width="16" height="16" color="#ee5555"/>
<text x="872" y="83" fill="#ecebe6" font-size="7.5">[55] Rear fog</text>
<text x="686" y="59" fill="#58564f" font-size="5.5">1.0 Gn/Sw</text>
<text x="846" y="59" fill="#58564f" font-size="5.5">1.0 Br/Ge  (from F20)</text>

<!-- Brake [56] [57] -->
<rect x="686" y="100" width="140" height="22" fill="#1d2330" stroke="#cc3333"/>
<use href="#bulb" x="690" y="104" width="16" height="16" color="#cc3333"/>
<text x="712" y="115" fill="#ecebe6" font-size="7.5">[57] Brake light</text>
<rect x="846" y="100" width="140" height="22" fill="#1d2330" stroke="#cc3333"/>
<use href="#bulb" x="850" y="104" width="16" height="16" color="#cc3333"/>
<text x="872" y="115" fill="#ecebe6" font-size="7.5">[56] Brake light</text>
<text x="686" y="96" fill="#58564f" font-size="5.5">1.5 Rt/Ge  via brake SW [34]</text>

<!-- 3rd brake light -->
<rect x="686" y="132" width="300" height="18" fill="#1d2330" stroke="#cc3333" stroke-dasharray="3 2"/>
<use href="#bulb" x="690" y="136" width="16" height="14" color="#cc3333"/>
<text x="712" y="145" fill="#ecebe6" font-size="7">[61] 3rd brake light  ·  centre high-mount</text>

<!-- Tail [58] [59] -->
<rect x="686" y="160" width="140" height="22" fill="#1d2330" stroke="#84817a"/>
<use href="#bulb" x="690" y="164" width="16" height="16" color="#84817a"/>
<text x="712" y="175" fill="#ecebe6" font-size="7.5">[59] Tail light</text>
<rect x="846" y="160" width="140" height="22" fill="#1d2330" stroke="#84817a"/>
<use href="#bulb" x="850" y="164" width="16" height="16" color="#84817a"/>
<text x="872" y="175" fill="#ecebe6" font-size="7.5">[58] Tail light</text>
<text x="686" y="156" fill="#58564f" font-size="5.5">1.0 Ge/Sw  from LCM pin 7</text>

<!-- Rear marker [59][60] -->
<rect x="686" y="192" width="140" height="18" fill="#1d2330" stroke="#84817a" stroke-dasharray="3 2"/>
<text x="694" y="205" fill="#ecebe6" font-size="7">[59] Marker</text>
<rect x="846" y="192" width="140" height="18" fill="#1d2330" stroke="#84817a" stroke-dasharray="3 2"/>
<text x="854" y="205" fill="#ecebe6" font-size="7">[60] Marker</text>

<!-- Variant note -->
<rect x="686" y="220" width="300" height="26" fill="rgba(84,136,204,.07)" stroke="rgba(84,136,204,.25)"/>
<text x="694" y="232" fill="#5488cc" font-size="7">Sedan / Coupe / Touring rear loom differs</text>
<text x="694" y="242" fill="#58564f" font-size="6">Touring: additional rear wiper harness</text>

<!-- Brake switch [34] -->
<rect x="686" y="258" width="145" height="28" fill="#1d2330" stroke="#ee8833"/>
<text x="694" y="270" fill="#ecebe6" font-size="7.5">[34] Brake light switch</text>
<text x="694" y="281" fill="#58564f" font-size="6">NC type · adjust gap: 1–1.5 mm</text>
<line x1="686" y1="111" x2="686" y2="258" stroke="#cc3333" stroke-width=".8" stroke-dasharray="3 3"/>

<!-- ═══════════════════════════════════════════════
     BOTTOM: WIRE COLOURS &amp; COMPONENT INDEX
═══════════════════════════════════════════════ -->
<rect x="8" y="336" width="1184" height="118" fill="#181d28" stroke="rgba(212,149,42,.15)"/>
<text x="20" y="354" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1.5">COMPONENT INDEX</text>

<g font-size="7">
  <text x="20" y="370" fill="#b8b5ae">[1]  Battery</text>
  <text x="20" y="382" fill="#b8b5ae">[34] Brake light switch</text>
  <text x="20" y="394" fill="#b8b5ae">[37] Light Control Module (LCM)</text>
  <text x="20" y="406" fill="#b8b5ae">[38] Axle load sensor (leveling)</text>
  <text x="20" y="418" fill="#b8b5ae">[39] L headlight leveling motor</text>
  <text x="20" y="430" fill="#b8b5ae">[40] R headlight leveling motor</text>

  <text x="220" y="370" fill="#b8b5ae">[41] Hazard / central lock switch</text>
  <text x="220" y="382" fill="#b8b5ae">[42] License plate lights</text>
  <text x="220" y="394" fill="#b8b5ae">[43] Column stalk switch</text>
  <text x="220" y="406" fill="#b8b5ae">[44] L parking light</text>
  <text x="220" y="418" fill="#b8b5ae">[45] R parking light</text>
  <text x="220" y="430" fill="#b8b5ae">[46] L low beam (H7)</text>

  <text x="420" y="370" fill="#b8b5ae">[47] R low beam (H7)</text>
  <text x="420" y="382" fill="#b8b5ae">[48] L high beam (H1)</text>
  <text x="420" y="394" fill="#b8b5ae">[49] R high beam (H1)</text>
  <text x="420" y="406" fill="#b8b5ae">[50] L front turn signal</text>
  <text x="420" y="418" fill="#b8b5ae">[51] L side repeater</text>
  <text x="420" y="430" fill="#b8b5ae">[52] R front turn signal</text>

  <text x="620" y="370" fill="#b8b5ae">[53] R side repeater</text>
  <text x="620" y="382" fill="#b8b5ae">[54] L rear turn signal</text>
  <text x="620" y="394" fill="#b8b5ae">[55] Rear fog light (R)</text>
  <text x="620" y="406" fill="#b8b5ae">[56] R brake light</text>
  <text x="620" y="418" fill="#b8b5ae">[57] L brake light</text>
  <text x="620" y="430" fill="#b8b5ae">[58] R tail light</text>

  <text x="820" y="370" fill="#b8b5ae">[59] L tail / marker</text>
  <text x="820" y="382" fill="#b8b5ae">[60] R marker</text>
  <text x="820" y="394" fill="#b8b5ae">[61] 3rd brake light (high-mount)</text>
  <text x="820" y="406" fill="#58564f">F106/F107 50A — LCM main power</text>
  <text x="820" y="418" fill="#58564f">F32/F9 5A — ignition supply</text>
  <text x="820" y="430" fill="#58564f">Grounds: X6001 / X6002  (brown Br)</text>
</g>
</svg>'''

# ─── SCHEMA 6: INTERIOR LIGHTING ─────────────────────────────────────────────
S6_SVG = '''<svg viewBox="0 0 1200 650" xmlns="http://www.w3.org/2000/svg" font-family="'IBM Plex Mono',monospace" font-size="9">
<defs>
  <pattern id="grid6" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40,0 L0,0 0,40" fill="none" stroke="rgba(255,255,255,.025)" stroke-width=".5"/>
  </pattern>
  <symbol id="gnd6" viewBox="0 0 14 12">
    <line x1="7" y1="0" x2="7" y2="4" stroke="#6b5a3a" stroke-width="1.5"/>
    <line x1="0" y1="4" x2="14" y2="4" stroke="#6b5a3a" stroke-width="2"/>
    <line x1="2" y1="7" x2="12" y2="7" stroke="#6b5a3a" stroke-width="1.5"/>
    <line x1="4" y1="10" x2="10" y2="10" stroke="#6b5a3a" stroke-width="1"/>
  </symbol>
  <symbol id="bulb6" viewBox="0 0 14 14">
    <circle cx="7" cy="7" r="5.5" fill="none" stroke="currentColor" stroke-width="1.2"/>
    <line x1="4.5" y1="4.5" x2="9.5" y2="9.5" stroke="currentColor" stroke-width="1"/>
    <line x1="9.5" y1="4.5" x2="4.5" y2="9.5" stroke="currentColor" stroke-width="1"/>
  </symbol>
</defs>
<rect width="1200" height="650" fill="#131720"/>
<rect width="1200" height="650" fill="url(#grid6)"/>
<!-- HEADER -->
<rect x="0" y="0" width="1200" height="26" fill="#1a1f2b"/>
<rect x="0" y="25" width="1200" height="1" fill="#d4952a" opacity=".4"/>
<text x="12" y="17" fill="#d4952a" font-size="9" font-weight="600" letter-spacing="2">SCHEMA 6</text>
<text x="84" y="17" fill="#84817a" font-size="9">INTERIOR LIGHTING · ZKE IV · DOME · FOOTWELL · VANITY MIRRORS · LIGHTER</text>
<text x="1188" y="17" fill="#58564f" font-size="8" text-anchor="end">BMW E36 ETM · projekt36.com</text>

<!-- ═══ POWER SUPPLY &amp; ZKE IV ═══ -->
<rect x="8" y="34" width="350" height="220" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="8" y="34" width="160" height="13" fill="rgba(212,149,42,.07)"/>
<text x="14" y="44" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">POWER SUPPLY</text>

<!-- Fuse box -->
<rect x="22" y="56" width="65" height="18" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="26" y="68" fill="#cc3333" font-size="7.5">F52  30A</text>
<rect x="22" y="80" width="65" height="18" fill="#1d2330" stroke="#cc3333"/>
<text x="26" y="92" fill="#cc3333" font-size="7">F108  200A</text>
<text x="22" y="111" fill="#58564f" font-size="6">Permanent  + KL30</text>

<!-- F6 5A ignition -->
<rect x="22" y="118" width="65" height="18" fill="#1d2330" stroke="#ee8833"/>
<text x="26" y="130" fill="#ee8833" font-size="7.5">F6  5A</text>
<text x="22" y="150" fill="#58564f" font-size="6">Ign. +KL15  (vanity mirrors)</text>

<!-- ZKE IV / General Module [77] -->
<rect x="120" y="56" width="220" height="55" fill="#1d2330" stroke="#5488cc" stroke-width="2"/>
<text x="145" y="76" fill="#5488cc" font-size="11" font-weight="700">[77] ZKE IV</text>
<text x="145" y="90" fill="#84817a" font-size="7">General Module (GM4)</text>
<text x="145" y="101" fill="#58564f" font-size="6">Controls interior lamps, power windows, CL</text>

<!-- wire F52 → ZKE -->
<line x1="87" y1="65" x2="120" y2="75" stroke="#cc3333" stroke-width="1.2"/>
<text x="88" y="68" fill="#84817a" font-size="6">2.5 Rt/Sw</text>

<!-- Door switch inputs to ZKE -->
<rect x="22" y="165" width="130" height="22" fill="#1d2330" stroke="#84817a"/>
<text x="30" y="180" fill="#ecebe6" font-size="7">[75][76] Door switches</text>
<rect x="22" y="195" width="130" height="22" fill="#1d2330" stroke="#84817a"/>
<text x="30" y="210" fill="#ecebe6" font-size="7">[96] Trunk lid switch</text>
<line x1="87" y1="176" x2="120" y2="110" stroke="#84817a" stroke-width=".8" stroke-dasharray="3 2"/>
<line x1="87" y1="206" x2="120" y2="110" stroke="#84817a" stroke-width=".8" stroke-dasharray="3 2"/>
<text x="22" y="234" fill="#58564f" font-size="6">Door open signal → ZKE activates interior lamps</text>

<!-- ═══ INTERIOR LIGHTS DISTRIBUTION ═══ -->
<rect x="370" y="34" width="810" height="165" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="370" y="34" width="185" height="13" fill="rgba(212,149,42,.07)"/>
<text x="376" y="44" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">INTERIOR LIGHTS — ZKE OUTPUT</text>

<!-- Horizontal distribution bus from ZKE -->
<line x1="340" y1="84" x2="1174" y2="84" stroke="#cccc33" stroke-width="1.2" stroke-dasharray="5 3"/>
<text x="356" y="81" fill="#cccc33" font-size="6">0.5 Ge/Sw  interior lamp bus</text>

<!-- Dome / Map light [78] -->
<rect x="376" y="92" width="110" height="35" fill="#1d2330" stroke="#cccc33" stroke-width="1.5"/>
<use href="#bulb6" x="380" y="96" width="14" height="14" color="#cccc33"/>
<text x="398" y="108" fill="#ecebe6" font-size="8" font-weight="600">[78] Dome</text>
<text x="398" y="120" fill="#84817a" font-size="6">Map light incl.</text>
<line x1="431" y1="84" x2="431" y2="92" stroke="#cccc33" stroke-width="1"/>

<!-- Trunk lights [82] [83] -->
<rect x="500" y="92" width="120" height="35" fill="#1d2330" stroke="#cccc33"/>
<use href="#bulb6" x="504" y="96" width="14" height="14" color="#cccc33"/>
<text x="522" y="108" fill="#ecebe6" font-size="7.5">[82][83] Trunk</text>
<text x="522" y="120" fill="#84817a" font-size="6">2× bulb · lid switch</text>
<line x1="560" y1="84" x2="560" y2="92" stroke="#cccc33" stroke-width="1"/>

<!-- Glove box [84] -->
<rect x="634" y="92" width="100" height="35" fill="#1d2330" stroke="#cccc33"/>
<use href="#bulb6" x="638" y="96" width="14" height="14" color="#cccc33"/>
<text x="656" y="108" fill="#ecebe6" font-size="7.5">[84] Glove box</text>
<text x="656" y="120" fill="#84817a" font-size="6">Lid switch</text>
<line x1="684" y1="84" x2="684" y2="92" stroke="#cccc33" stroke-width="1"/>

<!-- Rear interior lights [80] [81] -->
<rect x="748" y="92" width="120" height="35" fill="#1d2330" stroke="#cccc33"/>
<use href="#bulb6" x="752" y="96" width="14" height="14" color="#cccc33"/>
<text x="770" y="108" fill="#ecebe6" font-size="7.5">[80][81] Rear</text>
<text x="770" y="120" fill="#84817a" font-size="6">L + R rear ceiling</text>
<line x1="808" y1="84" x2="808" y2="92" stroke="#cccc33" stroke-width="1"/>

<!-- Footwell lights [85] [86] -->
<rect x="882" y="92" width="125" height="35" fill="#1d2330" stroke="#cccc33"/>
<use href="#bulb6" x="886" y="96" width="14" height="14" color="#cccc33"/>
<text x="904" y="108" fill="#ecebe6" font-size="7.5">[85][86] Footwell</text>
<text x="904" y="120" fill="#84817a" font-size="6">Driver + Pass.</text>
<line x1="944" y1="84" x2="944" y2="92" stroke="#cccc33" stroke-width="1"/>

<!-- Lighter illumination [87] [88] -->
<rect x="1020" y="92" width="145" height="35" fill="#1d2330" stroke="#cccc33" stroke-dasharray="3 2"/>
<use href="#bulb6" x="1024" y="96" width="14" height="14" color="#cccc33"/>
<text x="1042" y="108" fill="#ecebe6" font-size="7.5">[87][88] Lighter illum.</text>
<text x="1042" y="120" fill="#84817a" font-size="6">Panel illumination</text>
<line x1="1092" y1="84" x2="1092" y2="92" stroke="#cccc33" stroke-width="1"/>

<!-- Grounds below lamps -->
<use href="#gnd6" x="431" y="127" width="14" height="12"/>
<use href="#gnd6" x="560" y="127" width="14" height="12"/>
<use href="#gnd6" x="684" y="127" width="14" height="12"/>
<use href="#gnd6" x="808" y="127" width="14" height="12"/>
<use href="#gnd6" x="944" y="127" width="14" height="12"/>
<use href="#gnd6" x="1092" y="127" width="14" height="12"/>
<text x="376" y="155" fill="#58564f" font-size="6">Grounds: X6002 (body · brown Br)  ·  All interior lights: 0.35 – 0.5 mm² Ge wire</text>

<!-- ═══ VANITY MIRRORS ═══ -->
<rect x="8" y="270" width="370" height="200" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="8" y="270" width="130" height="13" fill="rgba(212,149,42,.07)"/>
<text x="14" y="280" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">VANITY MIRRORS</text>

<!-- F6 5A supply (already shown, reference) -->
<text x="22" y="296" fill="#58564f" font-size="6">+KL15 via F6 5A</text>

<!-- Driver vanity [91] + switch [92] -->
<rect x="22" y="302" width="90" height="22" fill="#1d2330" stroke="#ee8833"/>
<text x="30" y="317" fill="#ecebe6" font-size="7">[92] Driver switch</text>
<rect x="22" y="334" width="90" height="22" fill="#1d2330" stroke="#cccc33"/>
<use href="#bulb6" x="26" y="338" width="14" height="14" color="#cccc33"/>
<text x="44" y="349" fill="#ecebe6" font-size="7">[91] Driver mirror</text>
<line x1="67" y1="324" x2="67" y2="334" stroke="#ee8833" stroke-width="1"/>

<!-- Passenger vanity [93] + switch [94] -->
<rect x="140" y="302" width="90" height="22" fill="#1d2330" stroke="#ee8833"/>
<text x="148" y="317" fill="#ecebe6" font-size="7">[94] Pass. switch</text>
<rect x="140" y="334" width="90" height="22" fill="#1d2330" stroke="#cccc33"/>
<use href="#bulb6" x="144" y="338" width="14" height="14" color="#cccc33"/>
<text x="162" y="349" fill="#ecebe6" font-size="7">[93] Pass. mirror</text>
<line x1="185" y1="324" x2="185" y2="334" stroke="#ee8833" stroke-width="1"/>

<!-- Trunk vanity [89] [90] -->
<rect x="22" y="374" width="130" height="22" fill="#1d2330" stroke="#cccc33"/>
<use href="#bulb6" x="26" y="378" width="14" height="14" color="#cccc33"/>
<text x="44" y="390" fill="#ecebe6" font-size="7">[89][90] Trunk vanity</text>

<text x="22" y="420" fill="#58564f" font-size="6">All vanity: 0.35 Ge/Ws  ·  Mirror covers also act as switches</text>
<text x="22" y="432" fill="#58564f" font-size="6">+KL15 supply: lights on only with ignition ON</text>

<!-- ═══ LIGHTER / SOCKET ═══ -->
<rect x="390" y="270" width="350" height="200" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="390" y="270" width="175" height="13" fill="rgba(212,149,42,.07)"/>
<text x="396" y="280" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">LIGHTER &amp; POWER SOCKET</text>

<!-- F47 20A -->
<rect x="406" y="294" width="60" height="18" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="410" y="306" fill="#cc3333" font-size="7.5">F47  20A</text>

<!-- Cigarette lighter [95] -->
<rect x="406" y="326" width="100" height="30" fill="#1d2330" stroke="#ee8833" stroke-width="1.5"/>
<text x="415" y="340" fill="#ecebe6" font-size="8" font-weight="600">[95] LIGHTER</text>
<text x="415" y="350" fill="#84817a" font-size="6">12 V · heating element</text>
<line x1="436" y1="312" x2="436" y2="326" stroke="#cc3333" stroke-width="1.2"/>
<text x="440" y="323" fill="#cc3333" font-size="5.5">2.5 Rt/Sw</text>

<!-- Power socket [96] -->
<rect x="520" y="326" width="120" height="30" fill="#1d2330" stroke="#ee8833"/>
<text x="528" y="340" fill="#ecebe6" font-size="8" font-weight="600">[96] PWR SOCKET</text>
<text x="528" y="350" fill="#84817a" font-size="6">Accessory · 120W max</text>
<line x1="436" y1="312" x2="580" y2="312" stroke="#cc3333" stroke-width="1"/>
<line x1="580" y1="312" x2="580" y2="326" stroke="#cc3333" stroke-width="1"/>

<use href="#gnd6" x="436" y="358" width="14" height="12"/>
<use href="#gnd6" x="580" y="358" width="14" height="12"/>

<text x="406" y="396" fill="#58564f" font-size="6">Both on +KL30 permanent  ·  active even ignition OFF</text>
<text x="406" y="407" fill="#58564f" font-size="6">F47 20A from main fuse box · 2.5 Rt/Sw wire</text>
<text x="406" y="432" fill="#84817a" font-size="7">Lighter pull: ~100 W  →  8 A steady state</text>

<!-- ═══ COMPONENT INDEX ═══ -->
<rect x="8" y="482" width="1184" height="148" fill="#181d28" stroke="rgba(212,149,42,.15)"/>
<text x="20" y="500" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1.5">COMPONENT INDEX</text>
<g font-size="7">
  <text x="20" y="516" fill="#b8b5ae">[75] Driver door switch</text>
  <text x="20" y="528" fill="#b8b5ae">[76] Passenger door switch</text>
  <text x="20" y="540" fill="#b8b5ae">[77] ZKE IV General Module</text>
  <text x="20" y="552" fill="#b8b5ae">[78] Dome / map light</text>
  <text x="20" y="564" fill="#b8b5ae">[80] L rear interior light</text>
  <text x="20" y="576" fill="#b8b5ae">[81] R rear interior light</text>
  <text x="20" y="588" fill="#b8b5ae">[82] Trunk light (L)</text>
  <text x="20" y="600" fill="#b8b5ae">[83] Trunk light (R)</text>
  <text x="20" y="612" fill="#b8b5ae">[84] Glove box light</text>

  <text x="220" y="516" fill="#b8b5ae">[85] L footwell light</text>
  <text x="220" y="528" fill="#b8b5ae">[86] R footwell light</text>
  <text x="220" y="540" fill="#b8b5ae">[87] L lighter illumination</text>
  <text x="220" y="552" fill="#b8b5ae">[88] R lighter illumination</text>
  <text x="220" y="564" fill="#b8b5ae">[89] Trunk vanity (L)</text>
  <text x="220" y="576" fill="#b8b5ae">[90] Trunk vanity (R)</text>
  <text x="220" y="588" fill="#b8b5ae">[91] Driver visor mirror</text>
  <text x="220" y="600" fill="#b8b5ae">[92] Driver mirror switch</text>
  <text x="220" y="612" fill="#b8b5ae">[93] Passenger visor mirror</text>

  <text x="420" y="516" fill="#b8b5ae">[94] Passenger mirror switch</text>
  <text x="420" y="528" fill="#b8b5ae">[95] Cigarette lighter</text>
  <text x="420" y="540" fill="#b8b5ae">[96] Power socket (trunk)</text>
  <text x="420" y="552" fill="#58564f">F6 5A — vanity mirrors (+KL15)</text>
  <text x="420" y="564" fill="#58564f">F47 20A — lighter / socket (+KL30)</text>
  <text x="420" y="576" fill="#58564f">F52 30A — ZKE IV supply (+KL30)</text>
  <text x="420" y="588" fill="#58564f">Interior lamp bus: 0.5 Ge/Sw</text>
  <text x="420" y="600" fill="#58564f">All grounds: brown Br → X6002</text>

  <text x="680" y="516" fill="#5488cc" font-weight="600">ZKE IV controls:</text>
  <text x="680" y="528" fill="#84817a">· Interior lights (door / trunk trigger)</text>
  <text x="680" y="540" fill="#84817a">· Illuminated entry delay (~30 s)</text>
  <text x="680" y="552" fill="#84817a">· Power windows (Sch.10)</text>
  <text x="680" y="564" fill="#84817a">· Central locking (Sch.10)</text>
  <text x="680" y="576" fill="#84817a">· K-bus: 0.5 Br/Sw  IKE · LCM · Radio</text>
  <text x="680" y="588" fill="#58564f">Module location: right side of footwell</text>
  <text x="680" y="600" fill="#58564f">behind glove box on early cars,</text>
  <text x="680" y="612" fill="#58564f">passenger kick panel on late E36</text>
</g>
</svg>'''

# ─── SCHEMA 8: HORN, WIPERS, HEATER ──────────────────────────────────────────
S8_SVG = '''<svg viewBox="0 0 1200 700" xmlns="http://www.w3.org/2000/svg" font-family="'IBM Plex Mono',monospace" font-size="9">
<defs>
  <pattern id="grid8" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40,0 L0,0 0,40" fill="none" stroke="rgba(255,255,255,.025)" stroke-width=".5"/>
  </pattern>
  <symbol id="gnd8" viewBox="0 0 14 12">
    <line x1="7" y1="0" x2="7" y2="4" stroke="#6b5a3a" stroke-width="1.5"/>
    <line x1="0" y1="4" x2="14" y2="4" stroke="#6b5a3a" stroke-width="2"/>
    <line x1="2" y1="7" x2="12" y2="7" stroke="#6b5a3a" stroke-width="1.5"/>
    <line x1="4" y1="10" x2="10" y2="10" stroke="#6b5a3a" stroke-width="1"/>
  </symbol>
  <symbol id="motor8" viewBox="0 0 20 20">
    <circle cx="10" cy="10" r="8" fill="#1d2330" stroke="currentColor" stroke-width="1.5"/>
    <text x="10" y="14" fill="currentColor" font-size="9" font-weight="700" text-anchor="middle">M</text>
  </symbol>
  <symbol id="relay8" viewBox="0 0 30 22">
    <rect x="0" y="0" width="30" height="22" fill="#1d2330" stroke="currentColor" stroke-width="1" rx="1" stroke-dasharray="3 1"/>
    <line x1="5" y1="8" x2="10" y2="8" stroke="currentColor" stroke-width="1"/>
    <ellipse cx="13" cy="8" rx="3" ry="3" fill="none" stroke="currentColor" stroke-width="1"/>
    <line x1="20" y1="8" x2="25" y2="8" stroke="currentColor" stroke-width="1"/>
    <line x1="5" y1="14" x2="25" y2="14" stroke="currentColor" stroke-width=".8"/>
  </symbol>
</defs>
<rect width="1200" height="700" fill="#131720"/>
<rect width="1200" height="700" fill="url(#grid8)"/>
<!-- HEADER -->
<rect x="0" y="0" width="1200" height="26" fill="#1a1f2b"/>
<rect x="0" y="25" width="1200" height="1" fill="#d4952a" opacity=".4"/>
<text x="12" y="17" fill="#d4952a" font-size="9" font-weight="600" letter-spacing="2">SCHEMA 8</text>
<text x="84" y="17" fill="#84817a" font-size="9">HORN · WASHER JET HEATERS · HEADLIGHT WASHERS · BLOWER · WIPERS · REAR WIPER</text>
<text x="1188" y="17" fill="#58564f" font-size="8" text-anchor="end">BMW E36 ETM · projekt36.com</text>

<!-- ═══ HORN CIRCUIT ═══ -->
<rect x="8" y="34" width="240" height="240" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="8" y="34" width="80" height="13" fill="rgba(212,149,42,.07)"/>
<text x="14" y="44" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">HORN</text>

<!-- F55 15A  F5 5A -->
<rect x="22" y="56" width="65" height="18" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="26" y="68" fill="#cc3333" font-size="7.5">F55  15A</text>
<rect x="22" y="80" width="65" height="18" fill="#1d2330" stroke="#ee8833"/>
<text x="26" y="92" fill="#ee8833" font-size="7.5">F5  5A</text>
<text x="22" y="112" fill="#58564f" font-size="6">F55 = horn power (+KL30)</text>
<text x="22" y="122" fill="#58564f" font-size="6">F5 = ZKE / button signal</text>

<!-- ZKE IV horn control [118] -->
<rect x="22" y="133" width="120" height="26" fill="#1d2330" stroke="#5488cc"/>
<text x="30" y="148" fill="#5488cc" font-size="7.5">[118] ZKE IV  horn</text>
<text x="30" y="158" fill="#58564f" font-size="6">Relay K14 inside ZKE</text>

<!-- Clock spring [120] -->
<rect x="22" y="170" width="100" height="24" fill="#1d2330" stroke="#ee8833"/>
<text x="30" y="182" fill="#ecebe6" font-size="7.5">[120] Clock spring</text>
<text x="30" y="191" fill="#58564f" font-size="6">Steering wheel slip ring</text>

<!-- Horn button [121] -->
<rect x="22" y="204" width="100" height="22" fill="#1d2330" stroke="#ee8833"/>
<text x="30" y="219" fill="#ecebe6" font-size="7.5">[121] Horn button</text>
<line x1="72" y1="204" x2="72" y2="194" stroke="#ee8833" stroke-width="1"/>

<!-- Horn [119] -->
<rect x="145" y="170" width="90" height="40" fill="#1d2330" stroke="#cccc33" stroke-width="1.5"/>
<text x="155" y="189" fill="#cccc33" font-size="9" font-weight="700">[119]</text>
<text x="155" y="203" fill="#cccc33" font-size="8" font-weight="700">HORN</text>
<line x1="122" y1="182" x2="145" y2="182" stroke="#cc3333" stroke-width="1.2"/>
<text x="124" y="179" fill="#cc3333" font-size="5.5">1.5 Rt</text>
<line x1="87" y1="194" x2="87" y2="182" stroke="#ee8833" stroke-width="1"/>
<line x1="87" y1="182" x2="145" y2="182" stroke="#ee8833" stroke-width=".8" stroke-dasharray="3 2"/>
<use href="#gnd8" x="175" y="212" width="14" height="12"/>

<!-- ═══ WASHER JET HEATERS ═══ -->
<rect x="260" y="34" width="230" height="160" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="260" y="34" width="170" height="13" fill="rgba(212,149,42,.07)"/>
<text x="266" y="44" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">WASHER JET HEATERS</text>

<!-- F25 5A  F106 50A -->
<rect x="276" y="56" width="60" height="18" fill="#1d2330" stroke="#cc3333"/>
<text x="280" y="68" fill="#cc3333" font-size="7">F25  5A</text>
<rect x="276" y="80" width="70" height="18" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="280" y="92" fill="#cc3333" font-size="7">F106  50A</text>

<!-- Jet heater element [122] -->
<rect x="276" y="112" width="100" height="28" fill="#1d2330" stroke="#ee8833" stroke-width="1.5"/>
<text x="284" y="124" fill="#ecebe6" font-size="7.5">[122] Jet heaters</text>
<text x="284" y="135" fill="#84817a" font-size="6">Washer nozzle elements</text>

<!-- Thermal cut-out [123] -->
<rect x="390" y="112" width="90" height="28" fill="#1d2330" stroke="#84817a"/>
<text x="398" y="124" fill="#ecebe6" font-size="7.5">[123] Thermo</text>
<text x="398" y="135" fill="#84817a" font-size="6">cut-out safety</text>
<line x1="376" y1="126" x2="390" y2="126" stroke="#ee8833" stroke-width="1"/>

<text x="276" y="158" fill="#58564f" font-size="6">Auto-heats washer nozzles in sub-zero temps</text>
<text x="276" y="169" fill="#58564f" font-size="6">Thermostat opens circuit at +3 °C</text>
<use href="#gnd8" x="310" y="143" width="14" height="12"/>

<!-- ═══ HEADLIGHT WASHERS ═══ -->
<rect x="500" y="34" width="230" height="160" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="500" y="34" width="170" height="13" fill="rgba(212,149,42,.07)"/>
<text x="506" y="44" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">HEADLIGHT WASHERS</text>

<!-- F51 30A -->
<rect x="516" y="56" width="65" height="18" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="520" y="68" fill="#cc3333" font-size="7.5">F51  30A</text>

<!-- Relay [124] -->
<use href="#relay8" x="516" y="90" width="30" height="22" color="#a878d0"/>
<rect x="516" y="88" width="80" height="24" fill="#1d2330" stroke="#a878d0"/>
<text x="524" y="100" fill="#a878d0" font-size="7.5">[124] Relay</text>
<text x="524" y="110" fill="#58564f" font-size="6">Washer relay K25</text>
<line x1="549" y1="74" x2="549" y2="88" stroke="#cc3333" stroke-width="1.2"/>

<!-- Pump motor [125] -->
<rect x="620" y="88" width="90" height="40" fill="#1d2330" stroke="#5488cc" stroke-width="1.5"/>
<circle cx="650" cy="108" r="10" fill="none" stroke="#5488cc" stroke-width="1.5"/>
<text x="646" y="112" fill="#5488cc" font-size="8" font-weight="700">M</text>
<text x="668" y="104" fill="#84817a" font-size="6">[125]</text>
<text x="668" y="114" fill="#58564f" font-size="6">Pump motor</text>
<line x1="596" y1="100" x2="620" y2="100" stroke="#5488cc" stroke-width="1.2"/>
<text x="598" y="97" fill="#84817a" font-size="6">1.5 Sw/Bl</text>
<use href="#gnd8" x="650" y="130" width="14" height="12"/>

<text x="516" y="160" fill="#58564f" font-size="6">Headlight washer: present on M-Tech / Sport variants</text>
<text x="516" y="171" fill="#58564f" font-size="6">Check bumper for nozzle holes  ·  F51 30A from KL30</text>

<!-- ═══ HEATER BLOWER ═══ -->
<rect x="8" y="290" width="350" height="230" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="8" y="290" width="120" height="13" fill="rgba(212,149,42,.07)"/>
<text x="14" y="300" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">HEATER BLOWER</text>

<!-- F50 40A -->
<rect x="22" y="314" width="65" height="18" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="26" y="326" fill="#cc3333" font-size="7.5">F50  40A</text>

<!-- HVAC / heater control unit [129] -->
<rect x="22" y="346" width="130" height="30" fill="#1d2330" stroke="#a878d0" stroke-width="1.5"/>
<text x="30" y="361" fill="#a878d0" font-size="8" font-weight="600">[129] HVAC ctrl</text>
<text x="30" y="373" fill="#58564f" font-size="6">Heater head unit</text>

<!-- Blower resistor / final stage [126] -->
<rect x="22" y="392" width="130" height="35" fill="#1d2330" stroke="#ee8833"/>
<text x="30" y="406" fill="#ecebe6" font-size="7.5">[126] Blower resistor</text>
<text x="30" y="418" fill="#84817a" font-size="6">Wire wound  (heating only)</text>
<text x="30" y="427" fill="#58564f" font-size="6">IHKA: PWM final stage unit</text>
<line x1="87" y1="376" x2="87" y2="392" stroke="#ee8833" stroke-width="1"/>

<!-- Blower motor [127] -->
<rect x="200" y="378" width="90" height="40" fill="#1d2330" stroke="#5488cc" stroke-width="1.5"/>
<circle cx="230" cy="398" r="12" fill="none" stroke="#5488cc" stroke-width="2"/>
<text x="225" y="403" fill="#5488cc" font-size="9" font-weight="700">M</text>
<text x="250" y="395" fill="#84817a" font-size="6">[127]</text>
<text x="250" y="405" fill="#58564f" font-size="6">Blower</text>
<line x1="152" y1="404" x2="200" y2="398" stroke="#5488cc" stroke-width="1.2"/>
<text x="155" y="401" fill="#84817a" font-size="6">1.5 Sw/Ge</text>
<use href="#gnd8" x="230" y="420" width="14" height="12"/>

<!-- IHKA vs heater-only warning -->
<rect x="22" y="448" width="328" height="60" fill="rgba(204,51,51,.06)" stroke="rgba(204,51,51,.4)"/>
<text x="32" y="464" fill="#cc3333" font-size="8" font-weight="700">IHKA vs HEATING-ONLY DIFFERENCE</text>
<text x="32" y="478" fill="#b8b5ae" font-size="7">Heating-only: wire-wound resistor [126] in blower duct</text>
<text x="32" y="490" fill="#b8b5ae" font-size="7">IHKA (A/C): electronic PWM final stage unit — NOT interchangeable!</text>
<text x="32" y="502" fill="#58564f" font-size="6">Identify: check if 7-pin or 10-pin connector on heater head</text>

<!-- ═══ WINDSHIELD WIPER / WASHER ═══ -->
<rect x="370" y="200" width="380" height="240" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="370" y="200" width="210" height="13" fill="rgba(212,149,42,.07)"/>
<text x="376" y="210" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">WINDSHIELD WIPER / WASHER</text>

<!-- ZKE IV wiper control [77] -->
<rect x="386" y="224" width="130" height="30" fill="#1d2330" stroke="#5488cc" stroke-width="1.5"/>
<text x="395" y="239" fill="#5488cc" font-size="8" font-weight="600">[77] ZKE IV</text>
<text x="395" y="250" fill="#58564f" font-size="6">Wiper relay R12/R13</text>

<!-- Wiper stalk [128] -->
<rect x="386" y="266" width="130" height="28" fill="#1d2330" stroke="#ee8833"/>
<text x="394" y="280" fill="#ecebe6" font-size="7.5">[128] Wiper stalk</text>
<text x="394" y="290" fill="#58564f" font-size="6">Speed: off / int / slow / fast</text>
<line x1="451" y1="254" x2="451" y2="266" stroke="#ee8833" stroke-width="1"/>

<!-- Wiper motor [130] -->
<rect x="570" y="224" width="90" height="42" fill="#1d2330" stroke="#5488cc" stroke-width="1.5"/>
<circle cx="600" cy="245" r="12" fill="none" stroke="#5488cc" stroke-width="2"/>
<text x="595" y="250" fill="#5488cc" font-size="9" font-weight="700">M</text>
<text x="622" y="241" fill="#84817a" font-size="6">[130]</text>
<text x="622" y="251" fill="#58564f" font-size="6">Wiper</text>
<line x1="516" y1="239" x2="570" y2="239" stroke="#5488cc" stroke-width="1.2"/>
<text x="520" y="236" fill="#84817a" font-size="6">1.5 Gn/Ge</text>
<use href="#gnd8" x="600" y="268" width="14" height="12"/>

<!-- Washer pump [131] -->
<rect x="570" y="284" width="90" height="40" fill="#1d2330" stroke="#33aa33" stroke-width="1.5"/>
<circle cx="600" cy="304" r="10" fill="none" stroke="#33aa33" stroke-width="1.5"/>
<text x="595" y="308" fill="#33aa33" font-size="8" font-weight="700">M</text>
<text x="622" y="300" fill="#84817a" font-size="6">[131]</text>
<text x="622" y="310" fill="#58564f" font-size="6">Washer</text>
<text x="386" y="315" fill="#58564f" font-size="6">Washer→wiper interlock via ZKE</text>
<text x="386" y="326" fill="#58564f" font-size="6">Wiper runs 3× after washer pulse</text>
<use href="#gnd8" x="600" y="326" width="14" height="12"/>

<!-- Interval relay / timer -->
<rect x="386" y="344" width="250" height="22" fill="#181d28" stroke="rgba(84,136,204,.2)"/>
<text x="394" y="358" fill="#5488cc" font-size="7">Interval: ZKE R12 · delay: 2–30 s · LIN input [128]</text>
<text x="386" y="404" fill="#58564f" font-size="6">Park position: motor internal limit switch</text>
<text x="386" y="415" fill="#58564f" font-size="6">Always parks at bottom before next cycle</text>

<!-- ═══ REAR WIPER / WASHER ═══ -->
<rect x="760" y="200" width="420" height="200" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="760" y="200" width="180" height="13" fill="rgba(212,149,42,.07)"/>
<text x="766" y="210" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">REAR WIPER / WASHER</text>
<text x="920" y="210" fill="#58564f" font-size="7">Touring / Compact only</text>

<!-- Rear wiper control [132] -->
<rect x="776" y="224" width="130" height="28" fill="#1d2330" stroke="#a878d0"/>
<text x="784" y="238" fill="#a878d0" font-size="7.5">[132] Rear ctrl</text>
<text x="784" y="249" fill="#58564f" font-size="6">Relay module (boot)</text>

<!-- Trunk lid switch [133] -->
<rect x="776" y="264" width="130" height="26" fill="#1d2330" stroke="#84817a"/>
<text x="784" y="276" fill="#ecebe6" font-size="7.5">[133] Trunk SW</text>
<text x="784" y="287" fill="#58564f" font-size="6">Disables wiper when open</text>
<line x1="841" y1="252" x2="841" y2="264" stroke="#84817a" stroke-width="1"/>

<!-- Rear wiper motor [134] -->
<rect x="970" y="224" width="90" height="40" fill="#1d2330" stroke="#33aa33" stroke-width="1.5"/>
<circle cx="1000" cy="244" r="12" fill="none" stroke="#33aa33" stroke-width="2"/>
<text x="995" y="249" fill="#33aa33" font-size="9" font-weight="700">M</text>
<text x="1022" y="240" fill="#84817a" font-size="6">[134]</text>
<text x="1022" y="250" fill="#58564f" font-size="6">Rear</text>
<text x="1022" y="260" fill="#58564f" font-size="6">wiper</text>
<line x1="906" y1="238" x2="970" y2="238" stroke="#33aa33" stroke-width="1.2"/>
<text x="910" y="235" fill="#84817a" font-size="6">1.0 Gn/Sw</text>
<use href="#gnd8" x="1000" y="267" width="14" height="12"/>

<!-- Rear washer pump [135] -->
<rect x="970" y="284" width="90" height="35" fill="#1d2330" stroke="#33aa33"/>
<circle cx="1000" cy="301" r="9" fill="none" stroke="#33aa33" stroke-width="1.5"/>
<text x="996" y="305" fill="#33aa33" font-size="8" font-weight="700">M</text>
<text x="1022" y="297" fill="#84817a" font-size="6">[135]</text>
<text x="1022" y="307" fill="#58564f" font-size="6">Washer</text>
<use href="#gnd8" x="1000" y="322" width="14" height="12"/>

<text x="776" y="322" fill="#58564f" font-size="6">Sedan = no rear wiper  ·  Coupe = rear wiper standard</text>
<text x="776" y="333" fill="#58564f" font-size="6">Touring: heated rear washer nozzle optional</text>

<!-- ═══ COMPONENT INDEX ═══ -->
<rect x="8" y="534" width="1184" height="148" fill="#181d28" stroke="rgba(212,149,42,.15)"/>
<text x="20" y="552" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1.5">COMPONENT INDEX</text>
<g font-size="7">
  <text x="20" y="568" fill="#b8b5ae">[118] ZKE IV horn relay</text>
  <text x="20" y="580" fill="#b8b5ae">[119] Horn (single/dual)</text>
  <text x="20" y="592" fill="#b8b5ae">[120] Clock spring (slip ring)</text>
  <text x="20" y="604" fill="#b8b5ae">[121] Horn button (wheel)</text>
  <text x="20" y="616" fill="#b8b5ae">[122] Washer jet heaters</text>
  <text x="20" y="628" fill="#b8b5ae">[123] Thermal cut-out</text>
  <text x="20" y="640" fill="#b8b5ae">[124] Headlight washer relay</text>
  <text x="20" y="652" fill="#b8b5ae">[125] Headlight washer pump</text>

  <text x="220" y="568" fill="#b8b5ae">[126] Blower resistor/final stage</text>
  <text x="220" y="580" fill="#b8b5ae">[127] Blower motor</text>
  <text x="220" y="592" fill="#b8b5ae">[128] Wiper stalk switch</text>
  <text x="220" y="604" fill="#b8b5ae">[129] HVAC control unit</text>
  <text x="220" y="616" fill="#b8b5ae">[130] Windshield wiper motor</text>
  <text x="220" y="628" fill="#b8b5ae">[131] Windshield washer pump</text>
  <text x="220" y="640" fill="#b8b5ae">[132] Rear wiper relay</text>
  <text x="220" y="652" fill="#b8b5ae">[133] Trunk lid switch</text>

  <text x="440" y="568" fill="#b8b5ae">[134] Rear wiper motor</text>
  <text x="440" y="580" fill="#b8b5ae">[135] Rear washer pump</text>
  <text x="440" y="592" fill="#58564f">F5 5A — horn signal/ZKE</text>
  <text x="440" y="604" fill="#58564f">F25 5A — jet heater supply</text>
  <text x="440" y="616" fill="#58564f">F50 40A — blower motor</text>
  <text x="440" y="628" fill="#58564f">F51 30A — headlight washers</text>
  <text x="440" y="640" fill="#58564f">F55 15A — horn power</text>
  <text x="440" y="652" fill="#58564f">F106 50A — jet heater main</text>

  <text x="680" y="568" fill="#84817a">Wire sizes (typical):</text>
  <text x="680" y="580" fill="#84817a">Horn: 1.5 Rt  ·  signal: 0.5 Ws/Sw</text>
  <text x="680" y="592" fill="#84817a">Blower: 1.5 – 2.5 Sw/Ge / Sw/Bl</text>
  <text x="680" y="604" fill="#84817a">Wiper: 1.5 Gn/Ge  ·  washer: 1.0 Sw</text>
  <text x="680" y="616" fill="#84817a">Rear wiper: 1.0 Gn/Sw</text>
  <text x="680" y="628" fill="#58564f">Grounds: brown Br → X6001/X6002</text>
  <text x="680" y="640" fill="#58564f">Wiper park: internal motor limit switch</text>
</g>
</svg>'''

# ─── SCHEMA 10: WINDOWS, MIRRORS, LOCKS, SEATS ────────────────────────────────
S10_SVG = '''<svg viewBox="0 0 1200 730" xmlns="http://www.w3.org/2000/svg" font-family="'IBM Plex Mono',monospace" font-size="9">
<defs>
  <pattern id="grid10" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40,0 L0,0 0,40" fill="none" stroke="rgba(255,255,255,.025)" stroke-width=".5"/>
  </pattern>
  <symbol id="gnd10" viewBox="0 0 14 12">
    <line x1="7" y1="0" x2="7" y2="4" stroke="#6b5a3a" stroke-width="1.5"/>
    <line x1="0" y1="4" x2="14" y2="4" stroke="#6b5a3a" stroke-width="2"/>
    <line x1="2" y1="7" x2="12" y2="7" stroke="#6b5a3a" stroke-width="1.5"/>
    <line x1="4" y1="10" x2="10" y2="10" stroke="#6b5a3a" stroke-width="1"/>
  </symbol>
  <symbol id="motor10" viewBox="0 0 20 20">
    <circle cx="10" cy="10" r="8" fill="#1d2330" stroke="currentColor" stroke-width="1.5"/>
    <text x="10" y="14" fill="currentColor" font-size="9" font-weight="700" text-anchor="middle">M</text>
  </symbol>
</defs>
<rect width="1200" height="730" fill="#131720"/>
<rect width="1200" height="730" fill="url(#grid10)"/>
<!-- HEADER -->
<rect x="0" y="0" width="1200" height="26" fill="#1a1f2b"/>
<rect x="0" y="25" width="1200" height="1" fill="#d4952a" opacity=".4"/>
<text x="12" y="17" fill="#d4952a" font-size="9" font-weight="600" letter-spacing="2">SCHEMA 10</text>
<text x="96" y="17" fill="#84817a" font-size="9">POWER WINDOWS · ELECTRIC MIRRORS · CENTRAL LOCKING · HEATED SEATS</text>
<text x="1188" y="17" fill="#58564f" font-size="8" text-anchor="end">BMW E36 ETM · projekt36.com</text>

<!-- ═══ ZKE IV CENTRAL HUB ═══ -->
<rect x="390" y="34" width="420" height="55" fill="#1d2330" stroke="#5488cc" stroke-width="2"/>
<text x="460" y="57" fill="#5488cc" font-size="14" font-weight="700">[77] ZKE IV  —  GENERAL MODULE</text>
<text x="460" y="73" fill="#84817a" font-size="7.5">Controls: power windows · central locking · interior lights (Sch.6) · K-bus interface</text>

<!-- K-bus line from ZKE -->
<line x1="600" y1="89" x2="600" y2="105" stroke="#5488cc" stroke-width="1" stroke-dasharray="4 2"/>
<text x="604" y="98" fill="#58564f" font-size="6">K-bus  0.5 Br/Sw</text>

<!-- ═══ POWER WINDOWS ═══ -->
<rect x="8" y="120" width="1184" height="175" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="8" y="120" width="130" height="13" fill="rgba(212,149,42,.07)"/>
<text x="14" y="130" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">POWER WINDOWS</text>

<!-- F60 25A -->
<rect x="22" y="144" width="70" height="18" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="26" y="156" fill="#cc3333" font-size="7.5">F60  25A</text>
<text x="100" y="156" fill="#58564f" font-size="6">+KL30 permanent</text>

<!-- Horizontal power bus for windows -->
<line x1="57" y1="162" x2="57" y2="175" stroke="#cc3333" stroke-width="1.5"/>
<line x1="57" y1="175" x2="1175" y2="175" stroke="#cc3333" stroke-width="1.2"/>
<text x="22" y="186" fill="#58564f" font-size="6">2.5 Rt/Sw  →  all door modules via ZKE</text>

<!-- Driver door [151] - two motors -->
<rect x="140" y="195" width="220" height="60" fill="#1d2330" stroke="#ee8833" stroke-width="1.5"/>
<text x="152" y="212" fill="#ecebe6" font-size="7.5" font-weight="600">[151] Driver door</text>
<!-- window motor -->
<circle cx="175" cy="235" r="11" fill="none" stroke="#ee8833" stroke-width="1.5"/>
<text x="170" y="239" fill="#ee8833" font-size="8" font-weight="700">M</text>
<text x="188" y="232" fill="#84817a" font-size="6">Window</text>
<text x="188" y="241" fill="#58564f" font-size="6">regulator</text>
<!-- lock motor -->
<circle cx="275" cy="235" r="11" fill="none" stroke="#ee8833" stroke-width="1.5"/>
<text x="270" y="239" fill="#ee8833" font-size="8" font-weight="700">M</text>
<text x="288" y="232" fill="#84817a" font-size="6">Lock</text>
<text x="288" y="241" fill="#58564f" font-size="6">actuator</text>
<use href="#gnd10" x="225" y="248" width="14" height="12"/>
<text x="152" y="258" fill="#58564f" font-size="6">1.5 Gn/Ge · Gn/Rt per direction</text>
<line x1="225" y1="175" x2="225" y2="195" stroke="#cc3333" stroke-width="1"/>

<!-- Passenger door [152] -->
<rect x="380" y="195" width="220" height="60" fill="#1d2330" stroke="#33aa33" stroke-width="1.5"/>
<text x="392" y="212" fill="#ecebe6" font-size="7.5" font-weight="600">[152] Passenger door</text>
<circle cx="415" cy="235" r="11" fill="none" stroke="#33aa33" stroke-width="1.5"/>
<text x="410" y="239" fill="#33aa33" font-size="8" font-weight="700">M</text>
<text x="428" y="232" fill="#84817a" font-size="6">Window</text>
<circle cx="515" cy="235" r="11" fill="none" stroke="#33aa33" stroke-width="1.5"/>
<text x="510" y="239" fill="#33aa33" font-size="8" font-weight="700">M</text>
<text x="528" y="232" fill="#84817a" font-size="6">Lock</text>
<use href="#gnd10" x="465" y="248" width="14" height="12"/>
<text x="392" y="258" fill="#58564f" font-size="6">1.5 Gn/Sw · Gn/Vi per direction</text>
<line x1="465" y1="175" x2="465" y2="195" stroke="#cc3333" stroke-width="1"/>

<!-- Rear L [153] -->
<rect x="620" y="195" width="220" height="60" fill="#1d2330" stroke="#5488cc" stroke-width="1.5"/>
<text x="632" y="212" fill="#ecebe6" font-size="7.5" font-weight="600">[153] Rear L door</text>
<circle cx="655" cy="235" r="11" fill="none" stroke="#5488cc" stroke-width="1.5"/>
<text x="650" y="239" fill="#5488cc" font-size="8" font-weight="700">M</text>
<text x="668" y="232" fill="#84817a" font-size="6">Window</text>
<circle cx="755" cy="235" r="11" fill="none" stroke="#5488cc" stroke-width="1.5"/>
<text x="750" y="239" fill="#5488cc" font-size="8" font-weight="700">M</text>
<text x="768" y="232" fill="#84817a" font-size="6">Lock</text>
<use href="#gnd10" x="705" y="248" width="14" height="12"/>
<text x="632" y="258" fill="#58564f" font-size="6">Coupe rear = no window motor</text>
<line x1="705" y1="175" x2="705" y2="195" stroke="#cc3333" stroke-width="1"/>

<!-- Rear R [154] -->
<rect x="860" y="195" width="220" height="60" fill="#1d2330" stroke="#5488cc" stroke-width="1.5"/>
<text x="872" y="212" fill="#ecebe6" font-size="7.5" font-weight="600">[154] Rear R door</text>
<circle cx="895" cy="235" r="11" fill="none" stroke="#5488cc" stroke-width="1.5"/>
<text x="890" y="239" fill="#5488cc" font-size="8" font-weight="700">M</text>
<text x="908" y="232" fill="#84817a" font-size="6">Window</text>
<circle cx="995" cy="235" r="11" fill="none" stroke="#5488cc" stroke-width="1.5"/>
<text x="990" y="239" fill="#5488cc" font-size="8" font-weight="700">M</text>
<text x="1008" y="232" fill="#84817a" font-size="6">Lock</text>
<use href="#gnd10" x="945" y="248" width="14" height="12"/>
<text x="872" y="258" fill="#58564f" font-size="6">Sedan/Touring only</text>
<line x1="945" y1="175" x2="945" y2="195" stroke="#cc3333" stroke-width="1"/>

<!-- One-touch / anti-pinch note -->
<rect x="1100" y="195" width="82" height="60" fill="rgba(84,136,204,.06)" stroke="rgba(84,136,204,.3)"/>
<text x="1108" y="212" fill="#5488cc" font-size="7">One-touch:</text>
<text x="1108" y="224" fill="#84817a" font-size="6">ZKE IV only</text>
<text x="1108" y="236" fill="#84817a" font-size="6">316i base =</text>
<text x="1108" y="248" fill="#84817a" font-size="6">no ZKE →</text>
<text x="1108" y="260" fill="#84817a" font-size="6">relay retrofit</text>

<!-- ═══ ELECTRIC MIRRORS ═══ -->
<rect x="8" y="310" width="430" height="190" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="8" y="310" width="130" height="13" fill="rgba(212,149,42,.07)"/>
<text x="14" y="320" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">ELECTRIC MIRRORS</text>

<!-- F31 5A  F25 5A -->
<rect x="22" y="334" width="60" height="18" fill="#1d2330" stroke="#cc3333"/>
<text x="26" y="346" fill="#cc3333" font-size="7">F31  5A</text>
<rect x="88" y="334" width="60" height="18" fill="#1d2330" stroke="#cc3333"/>
<text x="92" y="346" fill="#cc3333" font-size="7">F25  5A</text>
<text x="155" y="346" fill="#58564f" font-size="6">+KL15</text>

<!-- Mirror selector / switch [155] -->
<rect x="22" y="366" width="130" height="30" fill="#1d2330" stroke="#33aa33" stroke-width="1.5"/>
<text x="30" y="380" fill="#ecebe6" font-size="7.5">[155] Mirror switch</text>
<text x="30" y="391" fill="#58564f" font-size="6">L / R select + direction</text>
<line x1="52" y1="352" x2="52" y2="366" stroke="#cc3333" stroke-width="1"/>

<!-- Driver mirror [156] - 2 motors -->
<rect x="22" y="408" width="160" height="45" fill="#1d2330" stroke="#33aa33" stroke-width="1.5"/>
<text x="32" y="422" fill="#ecebe6" font-size="7.5">[156] Driver mirror</text>
<circle cx="55" cy="440" r="9" fill="none" stroke="#33aa33" stroke-width="1.5"/>
<text x="51" y="444" fill="#33aa33" font-size="8">M</text>
<text x="66" y="437" fill="#84817a" font-size="6">H/V</text>
<text x="66" y="446" fill="#58564f" font-size="5.5">adjust</text>
<!-- heated element -->
<rect x="115" y="430" width="55" height="20" fill="#1d2330" stroke="#cc3333" stroke-dasharray="2 1"/>
<text x="120" y="443" fill="#cc3333" font-size="6.5">Heated</text>
<use href="#gnd10" x="75" y="450" width="14" height="12"/>
<line x1="87" y1="396" x2="87" y2="408" stroke="#33aa33" stroke-width="1"/>

<!-- Passenger mirror [157] - 3 motors (H, V, fold) -->
<rect x="200" y="408" width="220" height="45" fill="#1d2330" stroke="#33aa33" stroke-width="1.5"/>
<text x="210" y="422" fill="#ecebe6" font-size="7.5">[157] Passenger mirror</text>
<circle cx="230" cy="440" r="9" fill="none" stroke="#33aa33" stroke-width="1.5"/>
<text x="226" y="444" fill="#33aa33" font-size="8">M</text>
<text x="241" y="437" fill="#84817a" font-size="6">H/V</text>
<circle cx="300" cy="440" r="9" fill="none" stroke="#33aa33" stroke-width="1.5"/>
<text x="296" y="444" fill="#33aa33" font-size="8">M</text>
<text x="311" y="437" fill="#84817a" font-size="6">Fold</text>
<rect x="360" y="430" width="50" height="20" fill="#1d2330" stroke="#cc3333" stroke-dasharray="2 1"/>
<text x="365" y="443" fill="#cc3333" font-size="6.5">Heated</text>
<use href="#gnd10" x="265" y="450" width="14" height="12"/>
<text x="210" y="491" fill="#58564f" font-size="6">Pass. mirror: 3rd motor for folding (M-Sport / optional)</text>
<line x1="87" y1="396" x2="265" y2="408" stroke="#33aa33" stroke-width=".8" stroke-dasharray="3 2"/>

<!-- Heated mirror supply -->
<text x="22" y="490" fill="#58564f" font-size="6">Mirror heat: +KL58 (ignition) ·  1.0 Rt/Bl  · both mirrors in parallel</text>

<!-- ═══ CENTRAL LOCKING ═══ -->
<rect x="450" y="310" width="380" height="190" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="450" y="310" width="145" height="13" fill="rgba(212,149,42,.07)"/>
<text x="456" y="320" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">CENTRAL LOCKING</text>

<!-- F42 30A -->
<rect x="466" y="334" width="70" height="18" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="470" y="346" fill="#cc3333" font-size="7.5">F42  30A</text>

<!-- CL relay module [158] -->
<rect x="466" y="366" width="145" height="35" fill="#1d2330" stroke="#a878d0" stroke-width="1.5"/>
<text x="476" y="381" fill="#a878d0" font-size="8" font-weight="600">[158] CL Module</text>
<text x="476" y="393" fill="#58564f" font-size="6">Relay board in fusebox area</text>
<line x1="501" y1="352" x2="501" y2="366" stroke="#cc3333" stroke-width="1.2"/>

<!-- Door lock actuators connected to CL module -->
<text x="466" y="418" fill="#84817a" font-size="7">Output: lock actuators in all 4 doors</text>
<text x="466" y="430" fill="#58564f" font-size="6">2.5 Gn/Vi = lock  ·  2.5 Gn/Gn = unlock</text>
<text x="466" y="442" fill="#58564f" font-size="6">ZKE IV K-bus triggers CL relay</text>
<text x="466" y="454" fill="#58564f" font-size="6">Key cylinder: driver door direct input</text>
<text x="466" y="466" fill="#58564f" font-size="6">Remote: 315/433 MHz via radio module</text>

<!-- K-bus interface note -->
<rect x="630" y="366" width="185" height="60" fill="rgba(84,136,204,.06)" stroke="rgba(84,136,204,.3)"/>
<text x="640" y="382" fill="#5488cc" font-size="7">K-bus  0.35 Ws/Rt/Ge</text>
<text x="640" y="394" fill="#84817a" font-size="6">ZKE ↔ CL ↔ alarm · RF</text>
<text x="640" y="406" fill="#84817a" font-size="6">Speed-dependent auto-lock</text>
<text x="640" y="417" fill="#58564f" font-size="6">via INPA: close-not-locked fault</text>

<!-- ═══ HEATED SEATS ═══ -->
<rect x="843" y="310" width="349" height="190" fill="none" stroke="rgba(212,149,42,.12)" stroke-dasharray="5 3"/>
<rect x="843" y="310" width="115" height="13" fill="rgba(212,149,42,.07)"/>
<text x="849" y="320" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1">HEATED SEATS</text>

<!-- F12 7.5A -->
<rect x="859" y="334" width="70" height="18" fill="#1d2330" stroke="#cc3333"/>
<text x="863" y="346" fill="#cc3333" font-size="7.5">F12  7.5A</text>
<text x="937" y="346" fill="#58564f" font-size="6">+KL15</text>

<!-- Seat heat switch [158] -->
<rect x="859" y="366" width="120" height="26" fill="#1d2330" stroke="#ee8833"/>
<text x="867" y="378" fill="#ecebe6" font-size="7.5">[158] Seat switch</text>
<text x="867" y="388" fill="#58564f" font-size="6">2-stage: low / high</text>
<line x1="894" y1="352" x2="894" y2="366" stroke="#cc3333" stroke-width="1"/>

<!-- Driver cushion [159] + backrest [160] -->
<rect x="859" y="404" width="145" height="42" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="867" y="418" fill="#ecebe6" font-size="7.5">[159] Driver cushion</text>
<text x="867" y="430" fill="#84817a" font-size="6">Heating element ~ 35 W</text>
<rect x="867" y="435" width="115" height="8" fill="#1d2330" stroke="#cc3333" stroke-dasharray="2 1"/>
<text x="877" y="442" fill="#84817a" font-size="6">[160] backrest element</text>
<use href="#gnd10" x="900" y="447" width="14" height="12"/>
<line x1="919" y1="392" x2="919" y2="404" stroke="#cc3333" stroke-width="1"/>

<!-- Pass. cushion [162] + backrest [161] -->
<rect x="1020" y="404" width="155" height="42" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="1028" y="418" fill="#ecebe6" font-size="7.5">[162] Pass. cushion</text>
<text x="1028" y="430" fill="#84817a" font-size="6">Heating element ~ 35 W</text>
<rect x="1028" y="435" width="115" height="8" fill="#1d2330" stroke="#cc3333" stroke-dasharray="2 1"/>
<text x="1038" y="442" fill="#84817a" font-size="6">[161] backrest element</text>
<use href="#gnd10" x="1060" y="447" width="14" height="12"/>

<text x="859" y="468" fill="#58564f" font-size="6">1.5 Gn/Vi feed  ·  1.5 Br / 2.5 Br ground</text>
<text x="859" y="478" fill="#58564f" font-size="6">Bi-metal thermo-sensor in cushion: ~50 °C cut-off</text>

<!-- ═══ RETROFIT NOTE ═══ -->
<rect x="8" y="514" width="1184" height="70" fill="rgba(212,149,42,.04)" stroke="rgba(212,149,42,.2)"/>
<text x="20" y="532" fill="#d4952a" font-size="8" font-weight="700">POWER WINDOW RETROFIT (base 316i with manual cranks)</text>
<g font-size="7">
  <text x="20" y="548" fill="#b8b5ae">Parts needed: electric regulators × 4 · motors × 4 · door harnesses × 4 · switch panels × 4 · ZKE IV module · wiring plugs</text>
  <text x="20" y="560" fill="#b8b5ae">Without ZKE IV: wire via relays only (basic up/down, NO one-touch, NO speed-lock)</text>
  <text x="20" y="572" fill="#cc3333">Initialization after install: fully open → fully close → hold UP switch 5 s → system learns end-stops</text>
</g>

<!-- ═══ COMPONENT INDEX ═══ -->
<rect x="8" y="596" width="1184" height="120" fill="#181d28" stroke="rgba(212,149,42,.15)"/>
<text x="20" y="614" fill="#d4952a" font-size="8" font-weight="600" letter-spacing="1.5">COMPONENT INDEX</text>
<g font-size="7">
  <text x="20" y="630" fill="#b8b5ae">[77] ZKE IV General Module</text>
  <text x="20" y="642" fill="#b8b5ae">[151] Driver door (window + lock)</text>
  <text x="20" y="654" fill="#b8b5ae">[152] Passenger door (window + lock)</text>
  <text x="20" y="666" fill="#b8b5ae">[153] Rear L door (window + lock)</text>
  <text x="20" y="678" fill="#b8b5ae">[154] Rear R door (window + lock)</text>
  <text x="20" y="690" fill="#b8b5ae">[155] Mirror select switch</text>
  <text x="20" y="702" fill="#b8b5ae">[156] Driver mirror (2 motors)</text>

  <text x="250" y="630" fill="#b8b5ae">[157] Passenger mirror (2–3 motors)</text>
  <text x="250" y="642" fill="#b8b5ae">[158] CL relay module / seat switch</text>
  <text x="250" y="654" fill="#b8b5ae">[159] Driver seat cushion heater</text>
  <text x="250" y="666" fill="#b8b5ae">[160] Driver seat backrest heater</text>
  <text x="250" y="678" fill="#b8b5ae">[161] Pass. seat backrest heater</text>
  <text x="250" y="690" fill="#b8b5ae">[162] Pass. seat cushion heater</text>
  <text x="250" y="702" fill="#58564f">F12 7.5A · F25/F31 5A · F42 30A · F60 25A</text>

  <text x="560" y="630" fill="#84817a">Window wire: 1.5 Gn/Ge · Gn/Rt · Gn/Sw</text>
  <text x="560" y="642" fill="#84817a">Lock wire: 2.5 Gn/Vi (lock) · Gn/Gn (unlock)</text>
  <text x="560" y="654" fill="#84817a">Mirror: 0.35 Ws/Rt × 4 per mirror</text>
  <text x="560" y="666" fill="#84817a">Mirror heat: 1.0 Rt/Bl both mirrors</text>
  <text x="560" y="678" fill="#84817a">Seat heat: 1.5 Gn/Vi supply · 1.5 Br GND</text>
  <text x="560" y="690" fill="#58564f">All grounds: brown Br → X6002 body</text>
  <text x="560" y="702" fill="#58564f">K-bus: 0.5 Br/Sw (ZKE ↔ CL ↔ dash)</text>
</g>
</svg>'''

# ─── PERFORM REPLACEMENTS ─────────────────────────────────────────────────────

def replace_svg(html, schema_id, new_svg):
    """Replace everything between <div id="sN-simple"> and </div> with new SVG."""
    pattern = rf'(<div class="svg-frame" id="s{schema_id}-simple">).*?(</div>)'
    replacement = rf'\g<1>\n    {new_svg}\n  \g<2>'
    updated, n = re.subn(pattern, replacement, html, count=1, flags=re.DOTALL)
    if n == 0:
        print(f'WARNING: s{schema_id}-simple div not found!', file=sys.stderr)
    else:
        print(f'OK: replaced schema {schema_id} SVG')
    return updated

html = replace_svg(html, 4, S4_SVG)
html = replace_svg(html, 6, S6_SVG)
html = replace_svg(html, 8, S8_SVG)
html = replace_svg(html, 10, S10_SVG)

with open('public/schemas/e36-wiring.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Done — new file size: {len(html)} chars')
