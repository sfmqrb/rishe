#!/bin/bash
id="$1"
f=$(curl -s "https://archive.org/metadata/$id" | python3 -c '
import json,sys,urllib.parse
d=json.load(sys.stdin)
for f in d.get("files",[]):
    if f["name"].endswith("_djvu.txt"): print(urllib.parse.quote(f["name"]), f.get("size"))
')
echo "$id -> $f"
name=$(echo "$f" | head -1 | cut -d" " -f1)
[ -n "$name" ] && echo "  https://archive.org/download/$id/$name" && curl -sIL "https://archive.org/download/$id/$name" | grep -i '^HTTP' | tail -1
