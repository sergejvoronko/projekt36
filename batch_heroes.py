#!/usr/bin/env python3
"""Batch hero image generator for projekt36-astro using garage reference lock."""

import base64
import json
import mimetypes
import os
import sys
import time
import urllib.request
from pathlib import Path

try:
    from PIL import Image
    import io
except ImportError:
    print("Need Pillow: pip install pillow")
    sys.exit(1)

API_KEY = os.environ.get("GOOGLE_AI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
if not API_KEY:
    print("Set GOOGLE_AI_API_KEY env")
    sys.exit(1)

MODEL = "gemini-3.1-flash-image-preview"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

REF = Path("/home/sergej/Downloads/projekt36-astro/reference_img")
OUT = Path("/home/sergej/Downloads/projekt36-astro/public/heroes")

GARAGE_IMGS = [REF / "garage" / f for f in ["IMG_0778.jpeg", "IMG_0779.jpeg", "IMG_0780.jpeg", "IMG_0781.jpeg"]]
E36_IMGS = [REF / "e36" / f for f in ["IMG_0784.jpeg", "IMG_0785.jpeg", "IMG_0786.jpeg"]]
ENGINE_IMGS = [
    REF / "engine" / "M50.jpg",
    REF / "engine" / "complete m50 one side.jpg",
    REF / "engine" / "complete m50 other side.jpg",
    REF / "engine" / "bmw-m52-engine-04-830x528.jpg",
]

GARAGE_LOCK = (
    "REFERENCE LOCK: Reproduce the exact garage from the reference photos — "
    "white painted walls, two small windows in the back wall letting in natural daylight, "
    "fluorescent strip light on ceiling, left wall with cluttered workbench, cables, tools "
    "and yellow extension cord, right side with wooden wardrobe and parts shelving, gray "
    "concrete floor with drain. "
)
CAR_LOCK = (
    "The dark navy blue BMW E36 sedan from the reference photos is parked inside — "
    "same paint color, same angel-eye projector headlights, same M front bumper lip, "
    "same steel wheels. "
)
NO_CAR = "No car inside the garage. "
STYLE = (
    "STYLE: Photorealistic automotive photography. Professional DSLR photography. "
    "Natural workshop lighting. Ultra realistic materials. No CGI look. No concept art. "
    "No text. No watermark. No people. Shot with 35mm lens. Shallow depth of field. "
    "High dynamic range. Authentic BMW enthusiast workshop."
)

ARTICLES = [
    # (hero_filename, pillar, scene)
    ("bmw-e36-m50-m52-engine-sensor-diagnosis-replacement.webp", "engine",
     "BMW M50 inline-6 engine mounted on red engine stand in the garage, angled front-left view "
     "showing the intake manifold side with MAF sensor housing and wiring harness connectors along "
     "the top of the engine, fluorescent strip light overhead"),

    ("bmw-e36-m52-double-vanos-guide.webp", "engine",
     "BMW M52 inline-6 engine on red engine stand in the garage, front of engine facing camera "
     "showing the dual VANOS housing with its actuator body mounted at the front of the cylinder head, "
     "timing chain cover removed, fluorescent light overhead"),

    ("bmw-m50-engine-rebuild-guide.webp", "engine",
     "BMW M50 inline-6 engine block on red engine stand in the garage viewed from the exhaust side "
     "showing the full length of the long cast-iron block, cylinder head removed and resting on the "
     "workbench beside it, head gasket laid flat on the bench, workshop tools visible in background"),

    ("bmw-m52-engine-rebuild-guide.webp", "engine",
     "BMW M52 inline-6 engine block on red engine stand in the garage viewed from the side, "
     "aluminium block showing the full long engine profile, cylinder head separated and resting on "
     "the workbench to the right, natural light from back windows"),

    ("cooling.webp", "engine",
     "BMW M50 inline-6 engine on red engine stand in the garage, cooling components on the workbench "
     "to the left — plastic expansion tank, thermostat housing, and fresh coolant hose set on the bench surface, "
     "fluorescent strip light overhead"),

    ("e36-m50-head-gasket-replacement.webp", "engine",
     "BMW M50 inline-6 engine block on red engine stand in the garage with cylinder head removed and "
     "set beside the stand, bare block deck exposed showing the head stud pattern, multi-layer steel "
     "head gasket lying flat on the workbench beside the stand"),

    ("e36-m50-oil-system-guide.webp", "engine",
     "BMW M50 oil sump pan and oil pump assembly on a blue shop rag on the workbench in the garage, "
     "pickup tube attached to the pump, oil filter housing and new filter set beside them, natural "
     "daylight from the back windows"),

    ("e36-m50-timing-chain-guide.webp", "engine",
     "BMW M50 inline-6 engine on red engine stand in the garage with timing chain cover removed, "
     "front of engine showing the timing chain, sprocket and tensioner guide rail assembly exposed "
     "under the fluorescent workshop light"),

    ("m50-failures.webp", "engine",
     "BMW M50 inline-6 engine on red engine stand in the center of the garage viewed from the exhaust side, "
     "long engine profile showing oil seepage at the cam cover gasket edge and valve cover surface, "
     "workshop fluorescent strip light overhead"),

    ("engine-compare-v2.webp", "engine",
     "Two BMW inline-6 cylinder heads on the workbench in the garage side by side — one M50 non-TU "
     "head and one M52 aluminium head — natural daylight from the back windows illuminating the "
     "casting differences between the two"),

    ("vanos.webp", "engine",
     "BMW VANOS variable valve timing actuator unit disassembled on a blue shop rag on the workbench "
     "in the garage, helical gear internals and seal ring set visible, VANOS solenoid and adjustment "
     "collar beside it, natural daylight from the back windows"),

    # SWAP pillar - garage only
    ("gearbox.webp", "swap",
     "BMW ZF S5D gearbox lying on a padded mat on the garage floor, bellhousing end facing camera "
     "showing the input shaft and clutch fork pivot, workshop tools on the floor beside it, "
     "fluorescent overhead light"),

    ("e36-m50-m52-s50-s52-engine-swap-guide.webp", "swap",
     "BMW S50 inline-6 engine suspended on chain hoist chains in the center of the garage, long "
     "engine profile hanging level above the concrete floor, fluorescent strip light overhead, "
     "engine stand and swap tools visible below"),

    ("e36-m52-to-m54-engine-swap-guide.webp", "swap",
     "BMW M54 inline-6 engine hanging from chain hoist in the center of the garage, freshly prepared "
     "with new gaskets and hoses fitted, long valve cover profile visible, garage workbench and "
     "parts shelves in background"),

    ("parts-list.webp", "swap",
     "BMW M50 inline-6 engine on red engine stand beside the workbench in the garage, workbench surface "
     "covered with engine swap components — wiring harness coiled at the back, engine mounts and "
     "coolant hoses arranged in rows, fluorescent light overhead"),

    ("wiring-swap.webp", "swap",
     "Two BMW engine wiring harnesses laid flat on the workbench in the garage side by side — one shorter "
     "M43 harness and one longer M50 harness — connectors and plugs visible along both lengths, "
     "natural daylight from the back windows"),

    ("m50-swap-cooling-adaptation.webp", "swap",
     "BMW M50 cooling adaptation components on the workbench in the garage — radiator expansion tank, "
     "aluminium thermostat housing, and fresh silicone hose set coiled beside them, all laid out "
     "for a swap installation, fluorescent strip light overhead"),

    # BODY pillar - with E36
    ("bmw-e36-paint-preparation-diy-respray-guide.webp", "body",
     "Dark navy blue BMW E36 sedan inside the garage, driver's front door and fender area masked "
     "with paper and tape, body panels showing sanded surface with guide coat applied, garage "
     "workbench visible to the left in the background"),

    ("rust-map.webp", "body",
     "Dark navy blue BMW E36 sedan inside the garage, rear wheel arch showing exposed bare metal "
     "with surface rust after panel trim removal, angle grinder and wire wheel brush on the "
     "garage floor beside the wheel arch"),

    ("ppf.webp", "body",
     "Dark navy blue BMW E36 sedan inside the garage viewed from the front three-quarter angle, "
     "clear paint protection film being applied to the hood and front bumper lip, squeegee tool "
     "resting on the bonnet surface"),

    # INTERIOR pillar - with E36
    ("sound-deadening.webp", "interior",
     "Interior of the dark navy blue BMW E36 inside the garage, driver door panel removed exposing "
     "bare metal sheet, roll of Dynamat sound deadening material on the floor beside the open door, "
     "roller tool resting inside the door cavity"),

    # SUSPENSION pillar - with E36
    ("air-suspension.webp", "suspension",
     "Dark navy blue BMW E36 sedan inside the garage with front driver wheel removed, front "
     "MacPherson strut and spring seat area exposed, air compressor unit and stainless air fittings "
     "laid on the floor beside the wheel arch"),

    # REFERENCE pillar - with E36
    ("charging.webp", "reference",
     "Dark navy blue BMW E36 sedan with hood open inside the garage, digital multimeter with probes "
     "connected to the battery terminals, alternator and belt visible in engine bay, natural daylight "
     "from the back windows"),

    ("e36-dme-connector-pinout-reference.webp", "reference",
     "BMW E36 DME control unit (black ECU box) on the workbench in the garage with the large "
     "wiring harness connector unplugged and spread beside it, printed pinout wiring diagram "
     "flat on the bench under the connector"),

    ("ews.webp", "reference",
     "BMW EWS immobilizer control module (small grey rectangular unit) on the workbench in the "
     "garage beside the E36 ignition key with transponder ring, garage tools visible on the "
     "left wall"),

    ("fuel-system.webp", "reference",
     "Dark navy blue BMW E36 inside the garage with rear seat base lifted, fuel pump access cover "
     "open showing the in-tank pump assembly, fuel filter and pressure test gauge on the workbench nearby"),

    ("fuse-relay.webp", "reference",
     "BMW E36 main fuse and relay box with cover removed set on the workbench in the garage, "
     "relay and fuse layout exposed, test light probe and relay test socket lying beside the box, "
     "natural light from back windows"),

    ("grounds.webp", "reference",
     "Dark navy blue BMW E36 with hood open inside the garage, focus on the engine bay firewall "
     "showing chassis ground strap connection points and braided earth leads at their bolted "
     "anchor positions, natural daylight from the back windows"),

    ("etm.webp", "reference",
     "Dark navy blue BMW E36 with hood open in the garage, printed BMW E36 ETM electrical wiring "
     "diagram pages spread open on the workbench beside the car, highlighter and pencil resting "
     "on the open diagram page"),

    ("inpa.webp", "reference",
     "Laptop computer on the workbench in the garage displaying INPA BMW diagnostic software "
     "interface with live sensor data on screen, OBD1 round 20-pin diagnostic cable coiled beside "
     "it, dark navy blue BMW E36 partially visible in the background"),

    ("lcm.webp", "reference",
     "BMW E36 LCM light control module (small black rectangular unit) on the workbench in the "
     "garage with wiring connector unplugged beside it, turn-signal relay and bulb socket test "
     "adapter resting on the bench surface"),

    ("torque-specs.webp", "reference",
     "Dark navy blue BMW E36 with hood open in the garage, click torque wrench resting across "
     "the M50 engine valve cover, folded printed torque specification reference sheet on the "
     "engine beside it, natural window light"),

    ("obd1-diag-v2.webp", "reference",
     "Dark navy blue BMW E36 sedan inside the garage, center console area showing the round OBD1 "
     "20-pin diagnostic connector port under the dash, diagnostic cable plugged in, laptop "
     "computer open on the passenger seat, fluorescent light overhead"),

    ("e36-obd1-fault-code-reference.webp", "reference",
     "Dark navy blue BMW E36 with hood open inside the garage, OBD1 round connector cable plugged "
     "into the under-hood diagnostic port, fault code reader on the workbench showing a code "
     "display, fluorescent strip light overhead"),

    ("e36-obd1-live-data-sensor-reference.webp", "reference",
     "Dark navy blue BMW E36 with hood open inside the garage, laptop on the workbench showing "
     "live INPA sensor data readout, OBD1 diagnostic cable connected, natural light from the "
     "back windows"),

    ("parts-sourcing.webp", "reference",
     "Dark navy blue BMW E36 hood open in the garage, workbench beside the car with BMW OEM "
     "parts in plastic packaging — gasket set, filter kit, and seal rings — and a BMW parts "
     "catalog open flat on the bench surface"),

    ("sunroof-drain.webp", "reference",
     "Dark navy blue BMW E36 sedan in the garage with sunroof glass slid fully open, overhead view "
     "into the sunroof drain channel and gutter seal, thin wire drain cleaning tool coiled beside "
     "the open sunroof frame"),

    ("suspension.webp", "reference",
     "Dark navy blue BMW E36 in the garage with front driver wheel removed, MacPherson strut and "
     "hub assembly exposed, new suspension bushings and wishbone arm on the floor beside the "
     "wheel arch"),

    ("zke.webp", "reference",
     "BMW E36 ZKE central body electronics module (small rectangular control unit) on the "
     "workbench in the garage, wiring connector pulled apart beside it, door lock relay and "
     "window lift relay on a clean shop rag beside the module"),
]

CAR_PILLARS = {"body", "suspension", "interior", "reference"}


def load_part(path: Path):
    mime = mimetypes.guess_type(str(path))[0] or "image/jpeg"
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return {"inlineData": {"mimeType": mime, "data": data}}


def call_gemini(parts: list) -> bytes:
    body = {
        "contents": [{"parts": parts}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": "16:9", "imageSize": "2K"},
        },
    }
    data = json.dumps(body).encode()
    req = urllib.request.Request(
        API_URL, data=data,
        headers={"Content-Type": "application/json"}, method="POST"
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                result = json.loads(resp.read())
            break
        except urllib.error.HTTPError as e:
            body_err = e.read().decode()
            if e.code == 429 and attempt < 2:
                wait = 2 ** (attempt + 2)
                print(f"  rate limited, wait {wait}s")
                time.sleep(wait)
                req = urllib.request.Request(
                    API_URL, data=data,
                    headers={"Content-Type": "application/json"}, method="POST"
                )
                continue
            raise RuntimeError(f"HTTP {e.code}: {body_err[:200]}")

    candidates = result.get("candidates", [])
    if not candidates:
        raise RuntimeError(f"No candidates: {result}")
    for p in candidates[0]["content"]["parts"]:
        if "inlineData" in p:
            return base64.b64decode(p["inlineData"]["data"])
    raise RuntimeError(f"No image in response")


def generate_hero(hero_file: str, pillar: str, scene: str, idx: int, total: int):
    out_path = OUT / hero_file
    print(f"[{idx}/{total}] {hero_file} ({pillar})")

    with_car = pillar in CAR_PILLARS
    ref_imgs = list(GARAGE_IMGS)
    if with_car:
        ref_imgs.extend(E36_IMGS)
    else:
        ref_imgs.extend(ENGINE_IMGS)

    ref_imgs = [p for p in ref_imgs if p.exists()]

    car_text = CAR_LOCK if with_car else NO_CAR
    prompt = GARAGE_LOCK + car_text + "SCENE: " + scene + " " + STYLE

    parts = [load_part(p) for p in ref_imgs]
    parts.append({"text": prompt})

    png_data = call_gemini(parts)

    img = Image.open(io.BytesIO(png_data))
    img = img.convert("RGB")
    img_resized = img.resize((1344, 768), Image.LANCZOS)
    img_resized.save(str(out_path), "WEBP", quality=85)
    print(f"  → saved {out_path} ({out_path.stat().st_size // 1024}KB)")


def main():
    start_idx = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    total = len(ARTICLES)

    for i, (hero_file, pillar, scene) in enumerate(ARTICLES):
        if i < start_idx:
            continue
        try:
            generate_hero(hero_file, pillar, scene, i + 1, total)
        except Exception as e:
            print(f"  ERROR: {e}")
            print(f"  Skipping, continuing...")
        if i < total - 1:
            time.sleep(8)

    print("Done.")


if __name__ == "__main__":
    main()
