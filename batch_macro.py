#!/usr/bin/env python3
"""Batch macro hero generator for projekt36-astro, driven by hero_prompts_macro.txt.

Writes N variants per scene to OUT/<name>/vK.webp (1344x768). Nothing in
public/heroes is touched; pick the best variant and copy it over by hand.

usage: batch_macro.py [--variants 3] [--only name.webp ...] [--out DIR]
"""
import argparse, signal, base64, io, json, os, re, sys, time, urllib.error, urllib.request
from pathlib import Path
from PIL import Image

KEY = os.environ.get("GOOGLE_AI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
if not KEY:
    sys.exit("Set GOOGLE_AI_API_KEY")
MODEL = "gemini-3.1-flash-image-preview"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
SRC = Path(__file__).with_name("hero_prompts_macro.txt")


def parse():
    text = SRC.read_text()
    style = re.search(r"STYLE BLOCK.*?\n-+\n(.*?)\n\n\nNEGATIVES", text, re.S).group(1).strip()
    neg = re.search(r"NEGATIVES.*?\n-+\n(.*?)\n\n\n", text, re.S).group(1).strip()
    scenes = []
    for m in re.finditer(r"^# (\S+\.webp)\n(SCENE:.*?)(?=\n\n|\n#|\Z)", text, re.S | re.M):
        scenes.append((m.group(1), " ".join(m.group(2).split())))
    return " ".join(style.split()), " ".join(neg.split()), scenes


def generate(prompt):
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE"],
                             "imageConfig": {"aspectRatio": "16:9", "imageSize": "2K"}},
    }).encode()
    for attempt in range(4):
        req = urllib.request.Request(URL, data=body, method="POST",
                                     headers={"Content-Type": "application/json", "x-goog-api-key": KEY})
        try:
            signal.alarm(200)  # hard cap: urlopen's timeout doesn't cover a stalled proxy
            try:
                with urllib.request.urlopen(req, timeout=120) as r:
                    res = json.loads(r.read())
            finally:
                signal.alarm(0)
            break
        except TimeoutError:
            if attempt < 3:
                continue
            raise RuntimeError("timeout")
        except urllib.error.HTTPError as e:
            msg = e.read().decode()[:300]
            if e.code in (429, 500, 503) and attempt < 3:
                time.sleep(2 ** (attempt + 3)); continue
            raise RuntimeError(f"HTTP {e.code}: {msg}")
    for c in res.get("candidates", []):
        for p in c.get("content", {}).get("parts", []):
            if "inlineData" in p:
                return base64.b64decode(p["inlineData"]["data"])
    raise RuntimeError(f"no image: {str(res)[:300]}")


def _alarm(*_):
    raise TimeoutError()


def main():
    signal.signal(signal.SIGALRM, _alarm)
    ap = argparse.ArgumentParser()
    ap.add_argument("--variants", type=int, default=3)
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--out", default="macro_out")
    a = ap.parse_args()
    style, neg, scenes = parse()
    if a.only:
        scenes = [s for s in scenes if s[0] in a.only]
    out = Path(a.out)
    fails = 0
    for i, (name, scene) in enumerate(scenes, 1):
        d = out / name
        d.mkdir(parents=True, exist_ok=True)
        for k in range(1, a.variants + 1):
            f = d / f"v{k}.webp"
            if f.exists():
                continue
            print(f"[{i}/{len(scenes)}] {name} v{k}", flush=True)
            try:
                img = Image.open(io.BytesIO(generate(f"{style} {scene} {neg}"))).convert("RGB")
                img.resize((1344, 768), Image.LANCZOS).save(f, "WEBP", quality=85)
            except Exception as e:
                fails += 1
                print(f"  ERROR: {e}", flush=True)
            time.sleep(3)
    print(f"Done. failures={fails}")


if __name__ == "__main__":
    main()
