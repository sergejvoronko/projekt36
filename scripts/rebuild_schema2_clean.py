#!/usr/bin/env python3
"""Replace Schema 2 (Starting & Charging) SVG with clean BMW ETM-style layout.

Design rules enforced in this SVG:
  • All wires are horizontal or vertical only — ZERO diagonal lines
  • Wires connect at box EDGES, never pass through box interiors
  • Text inside every box padded ≥12 px from all edges
  • Each sub-circuit is a self-contained bordered region
  • Wire labels sit above horizontal wire segments in clear space
  • No rotated text for wire labels
"""

import re

NEW_SVG = '''\
<svg viewBox="0 0 1200 1430" xmlns="http://www.w3.org/2000/svg"
     font-family="'IBM Plex Mono',monospace" style="background:#131720;display:block">

<!-- PAGE BACKGROUND -->
<rect width="1200" height="1430" fill="#131720"/>

<!-- HEADER BAR -->
<rect x="0" y="0" width="1200" height="30" fill="#191e2b"/>
<rect x="0" y="29" width="1200" height="2" fill="#d4952a" opacity=".45"/>
<text x="14" y="20" fill="#d4952a" font-size="11" font-weight="600" letter-spacing="2">STARTING &amp; CHARGING</text>
<text x="236" y="20" fill="#84817a" font-size="10">· COOLING FAN · EWS IMMOBILIZER · DIAGNOSTIC CONNECTORS</text>
<text x="1186" y="20" fill="#58564f" font-size="9" text-anchor="end">BMW E36 ETM · projekt36.com</text>

<!-- ══════════════════════════════════════════════════════════════
     SECTION 1 · STARTING SYSTEM
     Components: BATTERY → F108 → STARTER MOTOR
                 IGNITION SWITCH KL50 → STARTER pin50
     ══════════════════════════════════════════════════════════════ -->
<rect x="10" y="38" width="1180" height="226" fill="rgba(212,149,42,.03)"
      stroke="rgba(212,149,42,.2)" stroke-width="1" stroke-dasharray="6 3"/>
<rect x="10" y="38" width="1180" height="16" fill="rgba(212,149,42,.07)"/>
<text x="22" y="51" fill="#d4952a" font-size="10" font-weight="600" letter-spacing="1.5">STARTING SYSTEM</text>

<!-- BATTERY [1] — x=20,y=62,w=148,h=68 -->
<rect x="20" y="62" width="148" height="68" fill="#1d2330" stroke="#6abf69" stroke-width="2"/>
<text x="32" y="80"  fill="#84817a"  font-size="9">[1]</text>
<text x="50" y="80"  fill="#6abf69"  font-size="11" font-weight="700">BATTERY</text>
<text x="32" y="96"  fill="#ecebe6"  font-size="9">+12V · GND (trunk)</text>
<text x="32" y="110" fill="#84817a"  font-size="9">Lead-acid 70 Ah typ.</text>
<text x="32" y="122" fill="#58564f"  font-size="8">Location: boot</text>

<!-- F108 200A fusible link — x=212,y=80,w=126,h=38  cy=99 -->
<rect x="212" y="80" width="126" height="38" fill="#1d2330" stroke="#cc3333" stroke-width="2"/>
<text x="224" y="97"  fill="#cc3333" font-size="10.5" font-weight="600">F108  200A</text>
<text x="224" y="110" fill="#58564f" font-size="8">Fusible link · engine bay</text>

<!-- STARTER MOTOR [3] — x=386,y=62,w=176,h=68  cy=96 -->
<rect x="386" y="62" width="176" height="68" fill="#1d2330" stroke="#cc3333" stroke-width="2"/>
<text x="398" y="80"  fill="#84817a"  font-size="9">[3]</text>
<circle cx="544" cy="82" r="13" fill="#1a2030" stroke="#cc3333" stroke-width="1.5"/>
<text x="544" y="87" fill="#cc3333" font-size="11" font-weight="700" text-anchor="middle">M</text>
<text x="398" y="102" fill="#ecebe6" font-size="11" font-weight="600">STARTER MOTOR</text>
<text x="398" y="116" fill="#84817a" font-size="9">pin 30 = B+  ·  pin 50 = KL50</text>
<text x="398" y="126" fill="#58564f" font-size="8">Bosch 1.1 kW (6-cyl)</text>

<!-- Wire: BAT right(168,96) → F108 left(212,96)  straight H at cy=96 -->
<line x1="168" y1="96" x2="212" y2="96" stroke="#cc3333" stroke-width="2"/>
<text x="180" y="92" fill="#cc3333" font-size="8">35.0 Rt</text>

<!-- Wire: F108 right(338,96) → STARTER left(386,96)  straight H -->
<line x1="338" y1="96" x2="386" y2="96" stroke="#cc3333" stroke-width="2.5"/>
<text x="348" y="92" fill="#cc3333" font-size="8">35.0 Rt  (B+)</text>

<!-- BAT negative ground symbol — centred x=94, from STARTER bottom y=130 -->
<line x1="94" y1="130" x2="94" y2="143" stroke="#8a7050" stroke-width="1.5"/>
<line x1="80" y1="143" x2="108" y2="143" stroke="#8a7050" stroke-width="2.5"/>
<line x1="84" y1="148" x2="104" y2="148" stroke="#8a7050" stroke-width="2"/>
<line x1="88" y1="153" x2="100" y2="153" stroke="#8a7050" stroke-width="1.5"/>
<text x="94" y="164" fill="#8a7050" font-size="8" text-anchor="middle">GND</text>

<!-- STARTER motor ground — x=474, from STARTER bottom y=130 -->
<line x1="474" y1="130" x2="474" y2="143" stroke="#8a7050" stroke-width="1.5"/>
<line x1="460" y1="143" x2="488" y2="143" stroke="#8a7050" stroke-width="2.5"/>
<line x1="464" y1="148" x2="484" y2="148" stroke="#8a7050" stroke-width="2"/>
<line x1="468" y1="153" x2="480" y2="153" stroke="#8a7050" stroke-width="1.5"/>
<text x="474" y="164" fill="#8a7050" font-size="8" text-anchor="middle">X6001</text>

<!-- IGNITION SWITCH [2] — x=212,y=172,w=156,h=74  right=368 cy=209 -->
<rect x="212" y="172" width="156" height="74" fill="#1d2330" stroke="#ee8833" stroke-width="2"/>
<text x="224" y="190" fill="#84817a"  font-size="9">[2]</text>
<text x="244" y="190" fill="#ecebe6"  font-size="11" font-weight="600">IGN SWITCH</text>
<text x="224" y="208" fill="#ee8833"  font-size="9">KL30=B+  KL15=+On</text>
<text x="224" y="222" fill="#ee8833"  font-size="9">KL50=Start (pos. III)</text>
<text x="224" y="236" fill="#58564f"  font-size="8">Connector X2 · 6-pin</text>

<!-- Wire: BAT KL30 supply to IGN — exit BAT right(168,96), turn down to IGN left(212,209)
     Path: H right to x=184, V down to y=209, H right to x=212
     x=184 is clear: BAT right=168, F108 left=212, nothing between them -->
<polyline points="168,96 184,96 184,209 212,209"
          fill="none" stroke="#cc3333" stroke-width="1.5"/>

<!-- Wire: IGN KL50 → STARTER pin50
     Exit IGN right(368,209), go right to x=574 (outside STARTER right=562),
     then V up to y=96, then H left to STARTER right edge at (562,96) -->
<polyline points="368,209 574,209 574,96 562,96"
          fill="none" stroke="#ee8833" stroke-width="1.5"/>
<text x="410" y="204" fill="#ee8833" font-size="8">4.0 Rt/Ws  KL50</text>

<!-- ══════════════════════════════════════════════════════════════
     SECTION 2 · CHARGING SYSTEM
     Components: ALTERNATOR → F34 → to battery bus
                 ALT D+ → CLUSTER charge warning → DME K-bus
     ══════════════════════════════════════════════════════════════ -->
<rect x="10" y="274" width="1180" height="184" fill="rgba(84,136,204,.03)"
      stroke="rgba(84,136,204,.2)" stroke-width="1" stroke-dasharray="6 3"/>
<rect x="10" y="274" width="1180" height="16" fill="rgba(84,136,204,.07)"/>
<text x="22" y="287" fill="#5488cc" font-size="10" font-weight="600" letter-spacing="1.5">CHARGING SYSTEM</text>

<!-- ALTERNATOR [4] — x=20,y=298,w=164,h=76  cy=336 -->
<rect x="20" y="298" width="164" height="76" fill="#1d2330" stroke="#5488cc" stroke-width="2"/>
<text x="32" y="316"  fill="#84817a"  font-size="9">[4]</text>
<circle cx="162" cy="316" r="13" fill="#1a2030" stroke="#5488cc" stroke-width="1.5"/>
<text x="162" y="321" fill="#5488cc" font-size="11" font-weight="700" text-anchor="middle">G</text>
<text x="32" y="336"  fill="#ecebe6" font-size="11" font-weight="600">ALTERNATOR</text>
<text x="32" y="350"  fill="#84817a" font-size="9">B+ · D+ · DF  Bosch</text>
<text x="32" y="362"  fill="#58564f" font-size="8">~80A · 14.4V regulated</text>

<!-- F34 30A — x=234,y=317,w=108,h=36  cy=335 -->
<rect x="234" y="317" width="108" height="36" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="246" y="333" fill="#cc3333" font-size="10.5" font-weight="600">F34  30A</text>
<text x="246" y="345" fill="#58564f" font-size="8">Alt excitation / B+</text>

<!-- Wire: ALT B+ right(184,326) → F34 left(234,326) -->
<line x1="184" y1="326" x2="234" y2="326" stroke="#cc3333" stroke-width="2"/>
<text x="198" y="321" fill="#cc3333" font-size="8">6.0 Rt  B+</text>

<!-- Wire: F34 right(342,326) → label "→ BATTERY BUS" -->
<line x1="342" y1="326" x2="390" y2="326" stroke="#cc3333" stroke-width="1.5"/>
<text x="350" y="321" fill="#cc3333" font-size="8">→ BAT BUS</text>

<!-- CLUSTER / IKE [6] — x=406,y=298,w=186,h=76  cy=336 -->
<rect x="406" y="298" width="186" height="76" fill="#1d2330" stroke="#6abf69" stroke-width="1.8"/>
<text x="418" y="316" fill="#84817a"  font-size="9">[6]</text>
<text x="438" y="316" fill="#6abf69"  font-size="11" font-weight="600">CLUSTER / IKE</text>
<text x="418" y="332" fill="#ecebe6"  font-size="9">Charge warning lamp (D+)</text>
<text x="418" y="346" fill="#ecebe6"  font-size="9">Rev counter · K-bus</text>
<text x="418" y="358" fill="#58564f"  font-size="8">K-bus: 0.5 Br/Sw</text>

<!-- Wire: ALT D+ → CLUSTER
     ALT D+ exits at right edge y=350 (lower than B+ at y=326).
     Route: H right to x=220, V down to y=372, H right to CLUSTER left(406,372).
     Then V up from (406,372) to CLUSTER bottom at (406,374).
     Wait — CLUSTER bottom is y=374. So entry is at y=374 bottom edge.
     Check clear path: x=220,y=350→372 is between ALT(right=184) and F34(left=234) → x=220 is INSIDE F34 range!
     F34 is x=234-342. x=220 < 234. So x=220 is LEFT of F34. ✓ Clear.
     Then y=372 path: F34 bottom=353. So y=372 is below F34. ✓
     Then (220,372)→(406,372): at y=372. Nothing between x=220 and x=406 at y=372 (F34 bottom=353, CLUSTER top=298). ✓ -->
<polyline points="184,350 220,350 220,372 406,372"
          fill="none" stroke="#6abf69" stroke-width="1.2"/>
<text x="256" y="381" fill="#6abf69" font-size="8">0.35 Gn/Ws  D+</text>

<!-- DME [5] — x=652,y=294,w=208,h=110  cy=349 -->
<rect x="652" y="294" width="208" height="110" fill="#1d2330" stroke="#a878d0" stroke-width="2"/>
<text x="664" y="312" fill="#84817a"  font-size="9">[5]</text>
<text x="684" y="312" fill="#a878d0"  font-size="12" font-weight="700">DME / ECU</text>
<text x="664" y="330" fill="#84817a"  font-size="9">Motronic M1.7 / 1.8 / 3.3.1</text>
<text x="664" y="346" fill="#ecebe6"  font-size="9">Charge sense (D+) input</text>
<text x="664" y="360" fill="#ecebe6"  font-size="9">+KL15 · +KL30 supply pins</text>
<text x="664" y="374" fill="#ecebe6"  font-size="9">K-line output → OBD-II pin 7</text>
<text x="664" y="388" fill="#58564f"  font-size="8">Location: E-box right of firewall</text>

<!-- Wire: CLUSTER → DME K-bus (right=592 → DME left=652) -->
<line x1="592" y1="336" x2="652" y2="336" stroke="#84817a" stroke-width="1" stroke-dasharray="3 2"/>
<text x="606" y="330" fill="#84817a" font-size="8">K-bus</text>

<!-- ALT ground -->
<line x1="102" y1="374" x2="102" y2="387" stroke="#8a7050" stroke-width="1.5"/>
<line x1="88"  y1="387" x2="116" y2="387" stroke="#8a7050" stroke-width="2.5"/>
<line x1="92"  y1="392" x2="112" y2="392" stroke="#8a7050" stroke-width="2"/>
<line x1="96"  y1="397" x2="108" y2="397" stroke="#8a7050" stroke-width="1.5"/>
<text x="102" y="408" fill="#8a7050" font-size="8" text-anchor="middle">X6001</text>

<!-- ══════════════════════════════════════════════════════════════
     SECTION 3 · COOLING FAN
     Power: BAT → F101 → FAN RELAY pin87 → FAN MOTOR → GND
     Control: +KL15 → relay coil · THERMO SW in coil ground path
     ══════════════════════════════════════════════════════════════ -->
<rect x="10" y="468" width="1180" height="206" fill="rgba(84,136,204,.03)"
      stroke="rgba(84,136,204,.15)" stroke-width="1" stroke-dasharray="6 3"/>
<rect x="10" y="468" width="1180" height="16" fill="rgba(84,136,204,.07)"/>
<text x="22" y="481" fill="#5488cc" font-size="10" font-weight="600" letter-spacing="1.5">COOLING FAN</text>

<!-- BATTERY [1] repeated — x=20,y=492,w=130,h=56  cy=520 -->
<rect x="20" y="492" width="130" height="56" fill="#1d2330" stroke="#6abf69" stroke-width="1.5"/>
<text x="32" y="508" fill="#84817a"  font-size="9">[1]</text>
<text x="50" y="508" fill="#6abf69"  font-size="10" font-weight="600">BATTERY</text>
<text x="32" y="522" fill="#84817a"  font-size="9">+12V</text>
<text x="32" y="534" fill="#58564f"  font-size="8">via F101 / F37</text>

<!-- F101 50A — x=200,y=502,w=110,h=36  cy=520 -->
<rect x="200" y="502" width="110" height="36" fill="#1d2330" stroke="#cc3333" stroke-width="1.5"/>
<text x="212" y="518" fill="#cc3333" font-size="10" font-weight="600">F101  50A</text>
<text x="212" y="530" fill="#58564f" font-size="8">Fan / accessories</text>

<!-- FAN RELAY K — x=362,y=492,w=154,h=66  cy=525 -->
<rect x="362" y="492" width="154" height="66" fill="#1d2330" stroke="#ee8833" stroke-width="1.8"/>
<text x="374" y="510" fill="#ee8833" font-size="11" font-weight="600">FAN RELAY  K</text>
<text x="374" y="526" fill="#84817a" font-size="9">Coil: +KL15 trigger</text>
<text x="374" y="540" fill="#84817a" font-size="9">30 → 87 = power path</text>
<text x="374" y="552" fill="#58564f" font-size="8">Behind left headlight</text>

<!-- THERMAL SWITCH [10] — x=574,y=492,w=162,h=66  cy=525 -->
<rect x="574" y="492" width="162" height="66" fill="#1d2330" stroke="#ee8833" stroke-width="1.8"/>
<text x="586" y="510" fill="#84817a"  font-size="9">[10]</text>
<text x="610" y="510" fill="#ecebe6"  font-size="10" font-weight="600">THERMO SW</text>
<text x="586" y="526" fill="#ecebe6"  font-size="9">ON  at 92 °C</text>
<text x="586" y="540" fill="#ecebe6"  font-size="9">OFF at 87 °C</text>
<text x="586" y="552" fill="#58564f"  font-size="8">Rear coolant pipe</text>

<!-- AUX FAN MOTOR [9] — x=792,y=488,w=162,h=70  cy=523 -->
<rect x="792" y="488" width="162" height="70" fill="#1d2330" stroke="#5488cc" stroke-width="2"/>
<text x="804" y="506" fill="#84817a"  font-size="9">[9]</text>
<circle cx="934" cy="506" r="13" fill="#1a2030" stroke="#5488cc" stroke-width="1.5"/>
<text x="934" y="511" fill="#5488cc" font-size="11" font-weight="700" text-anchor="middle">M</text>
<text x="804" y="526" fill="#ecebe6" font-size="11" font-weight="600">AUX FAN</text>
<text x="804" y="540" fill="#84817a" font-size="9">Pusher · 400W</text>
<text x="804" y="552" fill="#58564f" font-size="8">Radiator front</text>

<!-- Wire: BAT right(150,520) → F101 left(200,520) -->
<line x1="150" y1="520" x2="200" y2="520" stroke="#cc3333" stroke-width="1.8"/>
<text x="162" y="515" fill="#cc3333" font-size="8">6.0 Rt/Bl</text>

<!-- Wire: F101 right(310,520) → FAN RELAY left(362,520) -->
<line x1="310" y1="520" x2="362" y2="520" stroke="#cc3333" stroke-width="1.8"/>
<text x="322" y="515" fill="#cc3333" font-size="8">6.0 Rt/Bl</text>

<!-- Wire: FAN RELAY right(516,520) → FAN MOTOR left(792,520)
     Path goes over THERMO SW. THERMO SW is x=574-736, y=492-558.
     The wire at y=520 passes THROUGH the thermo switch box! Need to route around it.
     Route: H to x=556 (left of thermo sw), V down to y=578, H right to x=808, V up to y=558 (motor bottom).
     Wait, fan motor: x=792-954, y=488-558. Entry from left at y=520 would enter fan motor.
     Better: go BELOW both thermo sw and fan motor:
     (516,520) → H to x=556 → V down to y=578 → H right to x=808 → V up to y=558 → H right to fan motor left(792).
     But fan motor left IS at x=792. Let me just enter fan motor at bottom edge.
     (516,520) → (556,520) → (556,578) → (873,578) → (873,558)
     Fan motor bottom is at y=558. x=873 is within fan motor (x=792-954). This wire enters bottom of fan motor. ✓
     Thermo SW bottom is at y=558. The segment (556,578)→(873,578) at y=578 is BELOW thermo sw. ✓
     The vertical (556,520)→(556,578): x=556 is LEFT of thermo sw (left=574). ✓ -->
<polyline points="516,520 556,520 556,578 873,578 873,558"
          fill="none" stroke="#cc3333" stroke-width="1.8"/>
<text x="660" y="574" fill="#cc3333" font-size="8">6.0 Rt/Bl  (power to motor)</text>

<!-- Control wire: +KL15 enters relay coil from top
     Small vertical tick on relay top edge at x=420 -->
<line x1="420" y1="484" x2="420" y2="492" stroke="#ee8833" stroke-width="1.2"/>
<text x="424" y="490" fill="#ee8833" font-size="8">+KL15</text>

<!-- Control wire: relay coil(−) → THERMO SW → GND
     Show as dashed line below, from relay bottom to thermo sw bottom -->
<polyline points="430,558 430,602 655,602 655,558"
          fill="none" stroke="#33aa33" stroke-width="1.2" stroke-dasharray="4 2"/>
<text x="510" y="616" fill="#33aa33" font-size="8">0.35 Sw/Gr  coil ctl</text>

<!-- FAN MOTOR ground — below motor bottom at y=558 -->
<line x1="873" y1="558" x2="873" y2="626" stroke="#8a7050" stroke-width="1.5"/>
<line x1="859" y1="626" x2="887" y2="626" stroke="#8a7050" stroke-width="2.5"/>
<line x1="863" y1="631" x2="883" y2="631" stroke="#8a7050" stroke-width="2"/>
<line x1="867" y1="636" x2="879" y2="636" stroke="#8a7050" stroke-width="1.5"/>
<text x="873" y="648" fill="#8a7050" font-size="8" text-anchor="middle">X6001</text>

<!-- SWAP NOTE box — x=966,y=492 -->
<rect x="966" y="492" width="214" height="172" fill="#181d28" stroke="rgba(84,136,204,.25)"/>
<text x="978" y="510" fill="#5488cc" font-size="10" font-weight="600">SWAP: M43 → M50</text>
<text x="978" y="526" fill="#b8b5ae" font-size="9">M43 fan assembly is</text>
<text x="978" y="540" fill="#b8b5ae" font-size="9">smaller. Must swap to</text>
<text x="978" y="554" fill="#b8b5ae" font-size="9">6-cyl fan + shroud.</text>
<text x="978" y="568" fill="#b8b5ae" font-size="9">Thermo switch stays.</text>
<text x="978" y="586" fill="#cc3333" font-size="9">M50 runs HOT without</text>
<text x="978" y="600" fill="#cc3333" font-size="9">correct fan. Check</text>
<text x="978" y="614" fill="#cc3333" font-size="9">before first drive!</text>
<text x="978" y="634" fill="#58564f" font-size="8">Relay: behind L headlight</text>
<text x="978" y="648" fill="#58564f" font-size="8">Thermo: rear coolant pipe</text>

<!-- ══════════════════════════════════════════════════════════════
     SECTION 4 · EWS IMMOBILIZER
     Components: BATTERY → F14 → EWS MODULE → DME (coded signal)
                 KEY RING ANTENNA → EWS
     ══════════════════════════════════════════════════════════════ -->
<rect x="10" y="662" width="1180" height="220" fill="rgba(168,120,208,.03)"
      stroke="rgba(168,120,208,.2)" stroke-width="1" stroke-dasharray="6 3"/>
<rect x="10" y="662" width="1180" height="16" fill="rgba(168,120,208,.07)"/>
<text x="22" y="675" fill="#a878d0" font-size="10" font-weight="600" letter-spacing="1.5">EWS IMMOBILIZER</text>

<!-- BATTERY [1] repeated — x=20,y=688,w=130,h=56  cy=716 -->
<rect x="20" y="688" width="130" height="56" fill="#1d2330" stroke="#6abf69" stroke-width="1.5"/>
<text x="32" y="704" fill="#84817a"  font-size="9">[1]</text>
<text x="50" y="704" fill="#6abf69"  font-size="10" font-weight="600">BATTERY</text>
<text x="32" y="718" fill="#84817a"  font-size="9">+12V permanent</text>
<text x="32" y="730" fill="#58564f"  font-size="8">via F14 5A</text>

<!-- F14 5A — x=200,y=698,w=108,h=36  cy=716 -->
<rect x="200" y="698" width="108" height="36" fill="#1d2330" stroke="#ee8833" stroke-width="1.5"/>
<text x="212" y="714" fill="#ee8833" font-size="10" font-weight="600">F14  5A</text>
<text x="212" y="726" fill="#58564f" font-size="8">EWS module supply</text>

<!-- EWS MODULE [11] — x=364,y=676,w=210,h=98  right=574 cy=725 -->
<rect x="364" y="676" width="210" height="98" fill="#1d2330" stroke="#a878d0" stroke-width="2.5"/>
<text x="376" y="694" fill="#84817a"  font-size="9">[11]</text>
<text x="402" y="694" fill="#a878d0"  font-size="12" font-weight="700">EWS MODULE</text>
<text x="376" y="712" fill="#84817a"  font-size="9">Versions: I · II · III</text>
<text x="376" y="726" fill="#ecebe6"  font-size="9">Behind glove box · X11 12-pin</text>
<text x="376" y="740" fill="#ecebe6"  font-size="9">Ring antenna → key transponder</text>
<text x="376" y="754" fill="#58564f"  font-size="8">Coded start required each cycle</text>
<text x="376" y="765" fill="#58564f"  font-size="8">No code = no spark / no crank</text>

<!-- DME [5] repeated — x=638,y=676,w=210,h=98  cy=725 -->
<rect x="638" y="676" width="210" height="98" fill="#1d2330" stroke="#a878d0" stroke-width="2"/>
<text x="650" y="694" fill="#84817a"  font-size="9">[5]</text>
<text x="670" y="694" fill="#a878d0"  font-size="11" font-weight="600">DME / ECU</text>
<text x="650" y="712" fill="#ecebe6"  font-size="9">Receives coded start signal</text>
<text x="650" y="726" fill="#ecebe6"  font-size="9">from EWS on each key cycle.</text>
<text x="650" y="740" fill="#ecebe6"  font-size="9">Pin 7 = EWS serial wire</text>
<text x="650" y="754" fill="#58564f"  font-size="8">No valid code → no fuel/spark</text>
<text x="650" y="765" fill="#58564f"  font-size="8">Engine cranks but won't fire</text>

<!-- Wire: BAT right(150,716) → F14 left(200,716) -->
<line x1="150" y1="716" x2="200" y2="716" stroke="#ee8833" stroke-width="1.5"/>
<text x="162" y="711" fill="#ee8833" font-size="8">1.0 Rt/Gn</text>

<!-- Wire: F14 right(308,716) → EWS left(364,716) -->
<line x1="308" y1="716" x2="364" y2="716" stroke="#ee8833" stroke-width="1.5"/>
<text x="320" y="711" fill="#ee8833" font-size="8">1.0 Rt/Gn</text>

<!-- Wire: EWS right(574,716) → DME left(638,716) -->
<line x1="574" y1="716" x2="638" y2="716" stroke="#a878d0" stroke-width="1.5"/>
<text x="586" y="711" fill="#a878d0" font-size="8">coded signal</text>

<!-- Wire: EWS → DME starter lockout (second signal, below) -->
<line x1="574" y1="748" x2="638" y2="748" stroke="#cc3333" stroke-width="1.2" stroke-dasharray="3 2"/>
<text x="586" y="743" fill="#cc3333" font-size="8">starter inhibit</text>

<!-- EWS BYPASS WARNING BOX — x=870,y=676 -->
<rect x="870" y="676" width="310" height="200" fill="rgba(204,51,51,.06)" stroke="#cc3333" stroke-width="1.5"/>
<text x="882" y="694" fill="#cc3333" font-size="11" font-weight="700">⚠  SWAP: EWS BYPASS</text>
<text x="882" y="712" fill="#b8b5ae" font-size="9">Must bypass BOTH functions:</text>
<line x1="882" y1="718" x2="1170" y2="718" stroke="rgba(204,51,51,.2)" stroke-width="1"/>
<text x="882" y="732" fill="#cc3333" font-size="9" font-weight="600">① DME coded signal</text>
<text x="882" y="746" fill="#b8b5ae" font-size="9">EWS serial → DME pin 7</text>
<text x="882" y="758" fill="#58564f" font-size="8">Missing: cranks, no fire</text>
<line x1="882" y1="766" x2="1170" y2="766" stroke="rgba(204,51,51,.2)" stroke-width="1"/>
<text x="882" y="780" fill="#cc3333" font-size="9" font-weight="600">② Starter lockout relay</text>
<text x="882" y="794" fill="#b8b5ae" font-size="9">Thick wires in starter circuit</text>
<text x="882" y="806" fill="#58564f" font-size="8">Missing: won't crank at all</text>
<line x1="882" y1="814" x2="1170" y2="814" stroke="rgba(84,136,204,.3)" stroke-width="1"/>
<text x="882" y="828" fill="#5488cc" font-size="9" font-weight="600">Best: OBD1 M50TU 413 red ECU</text>
<text x="882" y="842" fill="#5488cc" font-size="9">= no EWS, plug-and-play</text>
<text x="882" y="856" fill="#58564f" font-size="8">M52: delete chip ~€60</text>
<text x="882" y="868" fill="#58564f" font-size="8">EWS-III: most difficult</text>

<!-- ══════════════════════════════════════════════════════════════
     SECTION 5 · DIAGNOSTIC CONNECTORS
     ══════════════════════════════════════════════════════════════ -->
<rect x="10" y="906" width="1180" height="258" fill="rgba(100,191,105,.03)"
      stroke="rgba(100,191,105,.15)" stroke-width="1" stroke-dasharray="6 3"/>
<rect x="10" y="906" width="1180" height="16" fill="rgba(100,191,105,.07)"/>
<text x="22" y="919" fill="#6abf69" font-size="10" font-weight="600" letter-spacing="1.5">DIAGNOSTIC CONNECTORS</text>

<!-- OBD-II 16-pin [7] — left half -->
<rect x="20" y="928" width="570" height="226" fill="none"
      stroke="rgba(100,191,105,.25)" stroke-dasharray="4 2"/>
<text x="34"  y="946" fill="#6abf69" font-size="10" font-weight="600">16-PIN OBD-II  [7]</text>
<text x="34"  y="960" fill="#58564f" font-size="8">Passenger footwell · left of centre console</text>
<!-- OBD connector shape -->
<rect x="34" y="966" width="162" height="58" fill="#1d2330" stroke="#6abf69" stroke-width="2" rx="4"/>
<text x="115" y="992" fill="#6abf69" font-size="13" font-weight="700" text-anchor="middle">OBD-II</text>
<text x="115" y="1008" fill="#84817a" font-size="9" text-anchor="middle">16-pin D-sub</text>
<!-- Pin assignments -->
<g font-size="9" fill="#b8b5ae">
  <text x="210" y="980">Pin  4  — Chassis GND          2.5 Br</text>
  <text x="210" y="994">Pin  5  — Signal GND           0.75 Gn/Br</text>
  <text x="210" y="1008">Pin  7  — K-line to DME         0.35 Ws/Vi</text>
  <text x="210" y="1022">Pin  8  — K-line 2 / ADS bridge</text>
  <text x="210" y="1036">Pin 14  — CAN Low               0.5 Rt/Ge/Ws</text>
  <text x="210" y="1050">Pin 16  — +12V permanent        F30 7.5A</text>
</g>
<text x="34" y="1072" fill="#d4952a" font-size="9" font-weight="600">Connected modules:</text>
<text x="34" y="1088" fill="#a878d0" font-size="8">→ DME (K-line)  · ABS/ASC  · Cluster  · EWS  · Airbag SRS</text>
<text x="34" y="1104" fill="#58564f" font-size="8">Use K+DCAN USB with INPA / NCS Expert (post Jan 1996)</text>
<text x="34" y="1118" fill="#58564f" font-size="8">Pin 8 bridges to ADS pin 7 for OBD1 compatibility</text>
<text x="34" y="1132" fill="#58564f" font-size="8">F30 7.5A · F1 7.5A supply permanent +12V to port</text>

<!-- ADS 20-pin [8] — right half -->
<rect x="610" y="928" width="570" height="226" fill="none"
      stroke="rgba(238,136,51,.2)" stroke-dasharray="4 2"/>
<text x="624" y="946" fill="#ee8833" font-size="10" font-weight="600">20-PIN ADS CONNECTOR  [8]</text>
<text x="624" y="960" fill="#58564f" font-size="8">Under bonnet · left near firewall · round connector</text>
<!-- ADS connector shape (round) -->
<ellipse cx="730" cy="998" rx="54" ry="40" fill="#1d2330" stroke="#ee8833" stroke-width="2"/>
<text x="730" y="996" fill="#ee8833" font-size="13" font-weight="700" text-anchor="middle">ADS</text>
<text x="730" y="1012" fill="#84817a" font-size="8" text-anchor="middle">Round · 20 pins</text>
<!-- Pin assignments -->
<g font-size="9" fill="#b8b5ae">
  <text x="800" y="976">Pin  1  — TXD serial transmit   0.35 Ws/Gn</text>
  <text x="800" y="990">Pin  7  — K-line (OBD1 only)</text>
  <text x="800" y="1004">Pin 14  — Chassis ground         2.5 Br</text>
  <text x="800" y="1018">Pin 17  — TXD data               0.35 Ws/Gn</text>
  <text x="800" y="1032">Pin 19  — +12V battery supply</text>
  <text x="800" y="1046">Pin 20  — +12V ignition supply   +KL15</text>
</g>
<!-- OBD1 vs OBD2 note -->
<rect x="624" y="1068" width="542" height="76" fill="rgba(84,136,204,.06)"
      stroke="rgba(84,136,204,.25)"/>
<text x="638" y="1086" fill="#5488cc" font-size="10" font-weight="600">OBD1 vs OBD2</text>
<text x="638" y="1102" fill="#b8b5ae" font-size="9">Pre  Jan 1996: ADS connector · use ADS cable, NOT K+DCAN</text>
<text x="638" y="1116" fill="#b8b5ae" font-size="9">Post Jan 1996: OBD-II 16-pin · use K+DCAN USB with INPA</text>
<text x="638" y="1130" fill="#58564f" font-size="8">Pin 8 OBD-II ↔ ADS pin 7 — required for INPA on OBD1</text>

<!-- ══════════════════════════════════════════════════════════════
     WIRE COLOUR REFERENCE  (left)  +  COMPONENT INDEX  (right)
     ══════════════════════════════════════════════════════════════ -->
<rect x="10" y="1176" width="580" height="244" fill="#181d28"
      stroke="rgba(212,149,42,.2)" stroke-width="1"/>
<text x="22" y="1194" fill="#d4952a" font-size="10" font-weight="600" letter-spacing="1.5">WIRE COLOUR REFERENCE</text>
<g font-size="9" fill="#b8b5ae">
  <text x="22" y="1212">35.0 Rt           — Battery positive main (fusible link)</text>
  <text x="22" y="1228">25.0 Sw           — Starter B+ direct  (thick black)</text>
  <text x="22" y="1244">6.0 Rt             — Alternator B+ output / fan power</text>
  <text x="22" y="1260">4.0 Rt/Gn       — Ignition switch to battery (KL30)</text>
  <text x="22" y="1276">4.0 Rt/Ws       — KL50 start signal to starter pin50</text>
  <text x="22" y="1292">1.0 Rt/Gn       — EWS module permanent supply</text>
  <text x="22" y="1308">0.35 Gn/Ws    — Alternator D+ charge signal</text>
  <text x="22" y="1324">0.5 Br/Sw        — K-bus serial communication</text>
  <text x="22" y="1340">0.35 Ws/Vi      — K-line to OBD-II pin 7</text>
  <text x="22" y="1356">Br  (brown)       — All chassis / body grounds</text>
  <text x="22" y="1378" fill="#84817a" font-size="8">X6001 = engine bay ground  ·  X6002 = body / firewall</text>
  <text x="22" y="1392" fill="#84817a" font-size="8">F30 7.5A = OBD +12V  ·  F1 7.5A = EWS + ign relay</text>
</g>

<rect x="610" y="1176" width="580" height="244" fill="#181d28"
      stroke="rgba(212,149,42,.2)" stroke-width="1"/>
<text x="622" y="1194" fill="#d4952a" font-size="10" font-weight="600" letter-spacing="1.5">COMPONENT INDEX</text>
<g font-size="9" fill="#b8b5ae">
  <text x="622" y="1212">[1]   Battery — trunk-mounted · lead-acid 70 Ah</text>
  <text x="622" y="1228">[2]   Ignition switch — X2 6-pin · steering column</text>
  <text x="622" y="1244">[3]   Starter motor — Bosch 1.1 kW (6-cylinder)</text>
  <text x="622" y="1260">[4]   Alternator — Bosch ~80 A · 14.4 V regulated</text>
  <text x="622" y="1276">[5]   DME / ECU — Motronic M1.7 / 1.8 / 3.3.1</text>
  <text x="622" y="1292">[6]   Instrument cluster (IKE)</text>
  <text x="622" y="1308">[7]   OBD-II 16-pin diagnostic port</text>
  <text x="622" y="1324">[8]   20-pin ADS connector (OBD1 only)</text>
  <text x="622" y="1340">[9]   Auxiliary cooling fan motor · 400 W</text>
  <text x="622" y="1356">[10]  Thermal switch — ON 92 °C / OFF 87 °C</text>
  <text x="622" y="1372">[11]  EWS immobilizer module</text>
  <text x="622" y="1392" fill="#84817a" font-size="8">Wire spec: gauge (mm²) + BMW colour codes (e.g. 4.0 Rt/Gn)</text>
  <text x="622" y="1406" fill="#84817a" font-size="8">Verify against your variant (M43/M50/M50TU/M52) and date</text>
</g>

</svg>'''

HTML_FILE = 'public/schemas/e36-wiring.html'

with open(HTML_FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace everything inside the s2-simple div (from opening tag to closing </div>)
# The s2-simple div contains the SVG; we replace just the inner SVG
pattern = r'(<div class="svg-frame" id="s2-simple">)\s*<svg[\s\S]*?</svg>\s*(</div>)'
replacement = r'\g<1>\n    ' + NEW_SVG.replace('\\', '\\\\') + r'\n  \g<2>'

html_new, n = re.subn(pattern, replacement, html)
if n == 0:
    print('ERROR: s2-simple div not found in HTML file', flush=True)
    raise SystemExit(1)

with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(html_new)

print(f'Done — replaced Schema 2 SVG (file is now {len(html_new):,} chars)')
