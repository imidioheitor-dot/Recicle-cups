#!/usr/bin/env python3
"""Download the Irish Comeback media into ./assets

Run once:      python3 fetch-assets.py
Then open:     presentation.html
"""
import json, os, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
MANIFEST = os.path.join(ASSETS, "MANIFEST.json")

def main():
    if not os.path.exists(MANIFEST):
        sys.exit("MANIFEST.json not found next to this script.")
    items = json.load(open(MANIFEST))
    os.makedirs(ASSETS, exist_ok=True)
    ok = skip = fail = 0
    for i, it in enumerate(items, 1):
        dest = os.path.join(ASSETS, it["local"])
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            print("[%2d/%d] have   %s" % (i, len(items), it["local"])); skip += 1; continue
        try:
            print("[%2d/%d] get    %s" % (i, len(items), it["local"]), flush=True)
            req = urllib.request.Request(it["url"], headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=90) as r, open(dest, "wb") as f:
                f.write(r.read())
            ok += 1
        except Exception as e:
            print("        FAILED %s -> %s" % (it["local"], e)); fail += 1
    print("\ndone: %d downloaded, %d already present, %d failed" % (ok, skip, fail))
    if fail:
        print("The site still works without them — every image falls back to the CDN.")

if __name__ == "__main__":
    main()
