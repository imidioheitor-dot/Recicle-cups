#!/usr/bin/env bash
# Download the Irish Comeback media into ./assets
set -u
cd "$(dirname "$0")"
mkdir -p assets
python3 - <<'PY'
import json,os,urllib.request
items=json.load(open("assets/MANIFEST.json"))
for i,it in enumerate(items,1):
    d=os.path.join("assets",it["local"])
    if os.path.exists(d) and os.path.getsize(d)>0:
        print("have  ",it["local"]); continue
    try:
        print("get   ",it["local"],flush=True)
        req=urllib.request.Request(it["url"],headers={"User-Agent":"Mozilla/5.0"})
        open(d,"wb").write(urllib.request.urlopen(req,timeout=90).read())
    except Exception as e:
        print("FAILED",it["local"],e)
PY
