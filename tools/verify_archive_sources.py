#!/usr/bin/env python3
"""Archive every URL cited in data/verification/page-*.json that is not yet in
data/verification/sources/web/index.jsonl (post-pass, so no cited source is lost
even if an agent forgot to archive it).  Usage: verify_archive_sources.py [pages...]
"""
import sys, os, glob, json, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = os.path.join(ROOT, "data", "verification")
INDEX = os.path.join(VER, "sources", "web", "index.jsonl")

def indexed():
    s = set()
    if os.path.exists(INDEX):
        for line in open(INDEX, encoding="utf-8"):
            try:
                d = json.loads(line)
                if d.get("status") == 200:
                    s.add(d["url"])
            except Exception:
                pass
    return s

def main(argv):
    only = set(argv[1:])
    have = indexed()
    todo = {}
    for f in sorted(glob.glob(os.path.join(VER, "page-*.json"))):
        pg = os.path.basename(f)[5:-5]
        if only and pg not in only:
            continue
        d = json.load(open(f, encoding="utf-8"))
        for e in d.get("entries", []):
            for u in e.get("sources") or []:
                todo.setdefault(u, f"page {pg}, root {e.get('root')} (root-level)")
            for n in e.get("nodes", []):
                for u in n.get("sources") or []:
                    todo.setdefault(u, f"page {pg}, root {e.get('root')}, node #{n.get('id')} {n.get('words','')}")
    missing = [u for u in todo if u not in have]
    print(f"{len(todo)} cited URLs, {len(missing)} not yet archived")
    fails = 0
    for u in missing:
        r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "fetch_source.py"), u, "--note", "post-pass: " + todo[u]],
                           capture_output=True, text=True)
        if r.returncode != 0:
            fails += 1
            print("FAILED", u)
    print(f"archived {len(missing) - fails}, failed {fails}")

if __name__ == "__main__":
    main(sys.argv)
