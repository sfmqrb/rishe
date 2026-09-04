#!/bin/bash
# usage: ia.sh "<query>" [rows]
q="$1"; rows="${2:-15}"
curl -s -G 'https://archive.org/advancedsearch.php' --data-urlencode "q=$q" --data-urlencode 'fl[]=identifier' --data-urlencode 'fl[]=title' --data-urlencode 'fl[]=year' --data-urlencode 'fl[]=access-restricted-item' --data-urlencode "rows=$rows" --data-urlencode 'output=json' | python3 -c '
import json,sys
d=json.load(sys.stdin)
for r in d["response"]["docs"]:
    print(r.get("identifier"),"|",r.get("year"),"|",r.get("access-restricted-item"),"|",str(r.get("title"))[:90])
'
