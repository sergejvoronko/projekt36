#!/usr/bin/env python3
"""Fetch a Wikimedia Commons image for an article, with its credit attached.

    python3 scripts/commons-image.py "File:BMW M50 1995.JPG" [--width 1200] [--alt "..."]

Downloads a resized copy, converts it to webp in public/images/commons/, records
author, licence and source in src/data/commons-credits.json, and prints the
<figure> HTML to paste into the article. CC BY / BY-SA require that credit next
to the image, so the credit is generated from Commons' own metadata rather than
typed by hand. Files without a machine-readable author, or under a licence we
cannot reuse commercially, are refused.
"""
import argparse, html, json, re, subprocess, sys, tempfile
from pathlib import Path
from urllib import parse, request

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / 'public' / 'images' / 'commons'
CREDITS = ROOT / 'src' / 'data' / 'commons-credits.json'
API = 'https://commons.wikimedia.org/w/api.php'
# Wikimedia asks API clients for a descriptive UA with contact details.
UA = 'projekt36-commons/1.0 (https://projekt36.com; airbrushden@gmail.com)'

# Licences that allow commercial reuse. NC and ND variants are deliberately absent.
OK = re.compile(r'^(CC0|Public domain|PD.*|CC BY(-SA)? [1-4]\.0.*)$', re.I)


def get(url):
    with request.urlopen(request.Request(url, headers={'User-Agent': UA}), timeout=30) as r:
        return r.read()


def strip(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s or '')).strip()


def metadata(title, width):
    q = parse.urlencode({
        'action': 'query', 'titles': title, 'prop': 'imageinfo', 'format': 'json',
        'iiprop': 'url|extmetadata', 'iiurlwidth': width,
        'iiextmetadatafilter': 'LicenseShortName|LicenseUrl|Artist|Credit|AttributionRequired',
    })
    page = next(iter(json.loads(get(f'{API}?{q}'))['query']['pages'].values()))
    if 'imageinfo' not in page:
        sys.exit(f'not found on Commons: {title}')
    info = page['imageinfo'][0]
    m = {k: v.get('value', '') for k, v in info.get('extmetadata', {}).items()}
    return {
        'title': page['title'],
        'thumb': info.get('thumburl') or info['url'],
        'page': info['descriptionurl'],
        'license': strip(m.get('LicenseShortName')),
        'license_url': m.get('LicenseUrl', ''),
        'author': strip(m.get('Artist')),
        'attribution_required': m.get('AttributionRequired', 'true') != 'false',
    }


def slugify(title):
    stem = Path(title.split(':', 1)[1]).stem
    return re.sub(r'[^a-z0-9]+', '-', stem.lower()).strip('-')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('title', help='Commons file title, e.g. "File:BMW M50 1995.JPG"')
    ap.add_argument('--width', type=int, default=1200)
    ap.add_argument('--alt', default='')
    a = ap.parse_args()
    title = a.title if a.title.startswith('File:') else f'File:{a.title}'

    m = metadata(title, a.width)
    if not OK.match(m['license']):
        sys.exit(f'licence not reusable here: {m["license"] or "unknown"}')
    # Commons fills Artist with this phrase when the uploader left no author field.
    if m['author'].lower().startswith('no machine-readable author'):
        m['author'] = ''
    if m['attribution_required'] and not m['author']:
        sys.exit('no machine-readable author: check the file page by hand before using it')

    slug = slugify(m['title'])
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f'{slug}.webp'
    with tempfile.NamedTemporaryFile(suffix=Path(m['thumb']).suffix) as tmp:
        tmp.write(get(m['thumb']))
        tmp.flush()
        subprocess.run(['cwebp', '-quiet', '-q', '80', tmp.name, '-o', str(out)], check=True)

    credits = json.loads(CREDITS.read_text()) if CREDITS.exists() else {}
    credits[slug] = {k: m[k] for k in ('title', 'page', 'license', 'license_url', 'author')}
    CREDITS.write_text(json.dumps(credits, indent=2, ensure_ascii=False) + '\n')

    lic = (f'<a href="{m["license_url"]}" rel="license noopener" target="_blank">{html.escape(m["license"])}</a>'
           if m['license_url'] else html.escape(m['license']))
    who = f'{html.escape(m["author"])}, ' if m['author'] else ''
    print(f'''<figure class="p36-photo">
<img src="/images/commons/{slug}.webp" alt="{html.escape(a.alt)}" loading="lazy" decoding="async">
<figcaption><span class="p36-credit">Photo: {who}{lic}, via <a href="{m["page"]}" rel="noopener" target="_blank">Wikimedia Commons</a></span></figcaption>
</figure>''')
    print(f'\nsaved {out.relative_to(ROOT)} ({out.stat().st_size // 1024} KB)', file=sys.stderr)


if __name__ == '__main__':
    main()
