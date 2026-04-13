#!/usr/bin/env python3
"""Fix two problems in e36-wiring.html:
1. Grid pattern fill="url(#gridN)" causes tan/white rendering in many browsers.
   Fix: remove the problematic grid overlay rects.
2. "Schema 2, 4, 6…" naming implies missing schemas 1,3,5…
   Fix: rename everything to descriptive English titles.
"""
import re, sys

with open('public/schemas/e36-wiring.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─── 1. FIX GRID PATTERN OVERLAY RECTS ──────────────────────────────────────
# Remove lines like:  <rect width="1200" height="NNN" fill="url(#gridN)"/>
# Keep the dark background rect and the defs block, just kill the overlay rect.
html = re.sub(
    r'\s*<rect width="1200" height="\d+" fill="url\(#grid\d+\)"/>\n?',
    '\n',
    html
)
print('Fixed: removed grid pattern overlay rects')

# ─── 2. RENAME NAV BUTTONS ───────────────────────────────────────────────────
# The nav is a div.schema-nav with buttons. Each button calls showSchema(N).
nav_renames = {
    r'onclick="showSchema\(2\)">[^<]*Schema 2[^<]*</button>':
        'onclick="showSchema(2)">Starting &amp; Charging</button>',
    r'onclick="showSchema\(4\)">[^<]*Schema 4[^<]*</button>':
        'onclick="showSchema(4)">Exterior Lighting</button>',
    r'onclick="showSchema\(6\)">[^<]*Schema 6[^<]*</button>':
        'onclick="showSchema(6)">Interior Lighting</button>',
    r'onclick="showSchema\(8\)">[^<]*Schema 8[^<]*</button>':
        'onclick="showSchema(8)">Wipers &amp; Horn</button>',
    r'onclick="showSchema\(10\)">[^<]*Schema 10[^<]*</button>':
        'onclick="showSchema(10)">Windows &amp; Locks</button>',
}
for pat, rep in nav_renames.items():
    html, n = re.subn(pat, rep, html)
    if n == 0:
        print(f'  WARNING: nav pattern not matched: {pat[:60]}', file=sys.stderr)
print('Fixed: renamed nav buttons')

# ─── 3. RENAME H2 HEADINGS ───────────────────────────────────────────────────
h2_renames = [
    # Schema 2
    (r'<h2>Schema 2 —[^<]*<span>[^<]*</span></h2>',
     '<h2>Starting &amp; Charging</h2>'),
    # Schema 4
    (r'<h2>Schema 4 —[^<]*<span>[^<]*</span></h2>',
     '<h2>Exterior Lighting</h2>'),
    # Schema 6
    (r'<h2>Schema 6 —[^<]*<span>[^<]*</span></h2>',
     '<h2>Interior Lighting</h2>'),
    # Schema 8
    (r'<h2>Schema 8 —[^<]*<span>[^<]*</span></h2>',
     '<h2>Wipers, Horn &amp; HVAC</h2>'),
    # Schema 10
    (r'<h2>Schema 10 —[^<]*<span>[^<]*</span></h2>',
     '<h2>Windows, Locks &amp; Mirrors</h2>'),
]
for pat, rep in h2_renames:
    html, n = re.subn(pat, rep, html)
    if n == 0:
        print(f'  WARNING: h2 pattern not matched: {pat[:60]}', file=sys.stderr)
print('Fixed: renamed h2 headings')

# ─── 4. FIX INTERNAL SVG HEADER TEXT (SCHEMA N → descriptive) ───────────────
svg_header_renames = [
    (r'<text[^>]*>SCHEMA 2</text>',
     '<text x="12" y="17" fill="#d4952a" font-size="9" font-weight="600" letter-spacing="2">STARTING &amp; CHARGING</text>'),
    (r'<text[^>]*>SCHEMA 4</text>',
     '<text x="12" y="17" fill="#d4952a" font-size="9" font-weight="600" letter-spacing="2">EXTERIOR LIGHTING</text>'),
    (r'<text[^>]*>SCHEMA 6</text>',
     '<text x="12" y="17" fill="#d4952a" font-size="9" font-weight="600" letter-spacing="2">INTERIOR LIGHTING</text>'),
    (r'<text[^>]*>SCHEMA 8</text>',
     '<text x="12" y="17" fill="#d4952a" font-size="9" font-weight="600" letter-spacing="2">WIPERS, HORN &amp; HVAC</text>'),
    (r'<text[^>]*>SCHEMA 10</text>',
     '<text x="12" y="17" fill="#d4952a" font-size="9" font-weight="600" letter-spacing="2">WINDOWS, LOCKS &amp; MIRRORS</text>'),
]
for pat, rep in svg_header_renames:
    html, n = re.subn(pat, rep, html)
    if n == 0:
        print(f'  WARNING: SVG header pattern not matched: {pat[:60]}', file=sys.stderr)
print('Fixed: renamed SVG internal headers')

# ─── 5. FIX SVG SUBTITLE TEXT (Schema N — ...) ───────────────────────────────
html = html.replace(
    '>STARTING · CHARGING · COOLING FAN · EWS · DIAGNOSTICS<',
    '>STARTING · CHARGING · COOLING FAN · EWS · DIAGNOSTICS<'
)  # keep the subtitle, just clean up

# ─── 6. UPDATE JS SCAN_TITLES ────────────────────────────────────────────────
old_titles = """const SCAN_TITLES = {
  2:'Schema 2 — Starting, Charging, Cooling Fan, EWS, Diagnostic Connectors',
  4:'Schema 4 — Lighting Control, External Lights, Fog Lights',
  6:'Schema 6 — Interior Lighting, Vanity Mirrors, Cigarette Lighter',
  8:'Schema 8 — Horn, Washer Heaters, Headlight Washers, Cooling Fan, Wipers',
  10:'Schema 10 — Door Locks, Electric Mirrors, Heated Seats'
};"""
new_titles = """const SCAN_TITLES = {
  2:'Starting & Charging — Starter, Alternator, Cooling Fan, EWS, Diagnostics',
  4:'Exterior Lighting — LCM, Headlights, Turn Signals, Brake & Tail',
  6:'Interior Lighting — ZKE IV, Dome, Footwell, Vanity Mirrors, Lighter',
  8:'Wipers, Horn & HVAC — Washer Heaters, Headlight Washers, Blower, Wipers',
  10:'Windows, Locks & Mirrors — Power Windows, Central Locking, Heated Seats'
};"""
if old_titles in html:
    html = html.replace(old_titles, new_titles)
    print('Fixed: updated JS SCAN_TITLES')
else:
    print('WARNING: JS SCAN_TITLES block not found — may already be updated', file=sys.stderr)

# ─── 7. UPDATE SCHEMA-META subtitles ─────────────────────────────────────────
# Also update the page header description
html = html.replace(
    'Toggle between a simplified SVG overview and the original service manual scan.',
    'Clean English SVG diagrams based on original BMW E36 service manual. Toggle to view the original Russian scan for reference.'
)

# Fix the "M43 → M50 SWAP NOTES  —  SCHEMA 2" text inside SVG bottom bar
html = html.replace(
    'M43 → M50 SWAP NOTES  —  SCHEMA 2',
    'M43 → M50 SWAP NOTES  —  STARTING &amp; CHARGING'
)
# Fix COMPONENT INDEX — SCHEMA 2
html = html.replace(
    'COMPONENT INDEX — SCHEMA 2',
    'COMPONENT INDEX'
)

# ─── 8. SCHEMA-SIMPLIFIED labels inside old SVGs (Schema 4 had these) ────────
html = html.replace('SCHEMA 4 — SIMPLIFIED', 'EXTERIOR LIGHTING')
html = html.replace('SCHEMA 6 — SIMPLIFIED', 'INTERIOR LIGHTING')
html = html.replace('SCHEMA 8 — SIMPLIFIED', 'WIPERS, HORN &amp; HVAC')
html = html.replace('SCHEMA 10 — SIMPLIFIED', 'WINDOWS, LOCKS &amp; MIRRORS')

# ─── WRITE OUTPUT ─────────────────────────────────────────────────────────────
with open('public/schemas/e36-wiring.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nDone — new file size: {len(html)} chars')
