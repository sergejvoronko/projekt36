#!/usr/bin/env python3
"""Preprocess BMW E36 wiring diagram scans.

Operations per image:
  1. Detect skew angle and deskew
  2. Normalise background to clean white (preserves dark ink/lines)
  3. Mild sharpening pass
  4. Save as high-quality PNG ready for Gemini editing

Output: /tmp/e36_scans_preprocessed/002.png  (etc.)
"""

import os
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter, ImageOps
from deskew import determine_skew

SCANS_DIR = Path("public/schemas")
OUT_DIR   = Path("/tmp/e36_scans_preprocessed")
OUT_DIR.mkdir(parents=True, exist_ok=True)

SCAN_FILES = sorted(SCANS_DIR.glob("0*.webp"))

def whiten_background(img: Image.Image, bg_threshold: int = 210) -> Image.Image:
    """Lift every pixel brighter than bg_threshold toward pure white.

    The paper background of these scans sits around RGB 215-235 with a
    cream / yellowish cast.  We map that range to 255 (white) while leaving
    the dark ink lines, coloured wires and component text untouched.
    """
    arr = np.array(img, dtype=np.float32)
    # Determine which pixels are "background" (all channels bright)
    bg_mask = np.all(arr >= bg_threshold, axis=2)

    # Smooth the mask slightly so edges don't get harsh
    # (just expand the mask by treating mid-grey as near-background)
    scale = np.clip((arr - bg_threshold) / (255 - bg_threshold), 0.0, 1.0)
    # Per-channel: blend pixel toward 255 where it's in background range
    for c in range(3):
        arr[:, :, c] = np.where(
            bg_mask,
            255.0,
            arr[:, :, c] + scale[:, :, c] * (255.0 - arr[:, :, c]) * 0.6,
        )
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

def process_scan(path: Path) -> Path:
    print(f"\n── Processing {path.name} ──")
    img = Image.open(path).convert("RGB")
    print(f"   Original size: {img.size}")

    # 1. Detect skew on a greyscale version
    grey_arr = np.array(img.convert("L"))
    angle = determine_skew(grey_arr)
    print(f"   Detected skew: {angle:.2f}°")

    # 2. Rotate to correct skew (expand=True keeps all content)
    if abs(angle) > 0.2:          # skip if negligibly small
        img = img.rotate(angle, resample=Image.BICUBIC, expand=True, fillcolor=(255, 255, 255))
        print(f"   Rotated by {angle:.2f}°")
    else:
        print("   Skew negligible — skip rotation")

    # 3. Whiten background
    img = whiten_background(img, bg_threshold=210)
    print("   Background whitened")

    # 4. Mild unsharp mask to restore sharpness lost in rotation
    img = img.filter(ImageFilter.UnsharpMask(radius=0.8, percent=120, threshold=3))
    print("   Sharpening applied")

    # 5. Save
    out_path = OUT_DIR / (path.stem + ".png")
    img.save(out_path, "PNG", optimize=False)
    print(f"   Saved → {out_path}  ({out_path.stat().st_size // 1024} KB)")
    return out_path

if __name__ == "__main__":
    if not SCAN_FILES:
        print("ERROR: no 0*.webp files found in", SCANS_DIR)
        sys.exit(1)

    results = []
    for f in SCAN_FILES:
        results.append(process_scan(f))

    print("\n✓ All done:")
    for r in results:
        print(f"  {r}")
