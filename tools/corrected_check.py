#!/usr/bin/env python3
"""Check data/corrected/page-<pdf>.json (the modern trees) against the extraction.

usage: python3 tools/corrected_check.py [N ...]     (no args: every corrected page)
Prints one summary line per page and a PROBLEM line for each defect.
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXTR = ROOT / "data" / "extracted" / "batch"
CORR = ROOT / "data" / "corrected"
CHANGES = {"kept", "corrected", "moved", "split", "added", "uncertain"}
ROOT_CHANGES = {"kept", "corrected", "replaced"}


def check(n):
    probs = []
    cf, ef = CORR / f"page-{n}.json", EXTR / f"page-{n}.json"
    if not cf.exists():
        return [f"page {n}: no corrected file"], None
    try:
        c = json.loads(cf.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"page {n}: invalid JSON: {e}"], None
    ex = json.loads(ef.read_text(encoding="utf-8"))
    want = {i for i, e in enumerate(ex["entries"]) if not e.get("root", {}).get("redirect") and e.get("nodes")}
    got = {}
    tally = {}
    for ce in c.get("entries", []):
        i = ce.get("entry")
        if i in got:
            probs.append(f"entry {i}: listed twice")
        got[i] = ce
    for i in sorted(want - set(got)):
        probs.append(f"entry {i}: missing")
    for i in sorted(set(got) - want):
        probs.append(f"entry {i}: not a chart entry in the extraction")
    for i, ce in sorted(got.items()):
        if i not in want:
            continue
        en = {x["id"]: x for x in ex["entries"][i]["nodes"]}
        r = ce.get("root") or {}
        if r.get("change") not in ROOT_CHANGES:
            probs.append(f"entry {i}: root.change {r.get('change')!r}")
        if not r.get("name"):
            probs.append(f"entry {i}: root.name empty")
        if r.get("change") in ("corrected", "replaced") and not (r.get("why") and r.get("why_fa")):
            probs.append(f"entry {i}: root changed without why/why_fa")
        if not (ce.get("summary") and ce.get("summary_fa")):
            probs.append(f"entry {i}: summary/summary_fa missing")
        nodes = ce.get("nodes") or []
        ids = [x.get("id") for x in nodes]
        if len(ids) != len(set(ids)):
            probs.append(f"entry {i}: duplicate node ids")
        idset = set(ids)
        seen = {}
        for x in nodes:
            nid = x.get("id")
            ch = x.get("change")
            tally[ch] = tally.get(ch, 0) + 1
            if ch not in CHANGES:
                probs.append(f"entry {i} node {nid}: change {ch!r}")
            p = x.get("parent")
            if p != 0 and p not in idset:
                probs.append(f"entry {i} node {nid}: parent {p} not in tree")
            fn = x.get("from_node")
            if ch == "added":
                if fn is not None:
                    probs.append(f"entry {i} node {nid}: added node has from_node")
                if not isinstance(nid, int) or nid < 101:
                    probs.append(f"entry {i} node {nid}: added node id must be >= 101")
            else:
                if fn not in en:
                    probs.append(f"entry {i} node {nid}: from_node {fn} not a Nourai node")
                elif nid != fn:
                    probs.append(f"entry {i} node {nid}: id differs from from_node {fn}")
                else:
                    seen[fn] = seen.get(fn, 0) + 1
            if ch != "kept" and not (x.get("why") and x.get("why_fa")):
                probs.append(f"entry {i} node {nid}: change {ch} without why/why_fa")
            if not isinstance(x.get("words"), list):
                probs.append(f"entry {i} node {nid}: words must be a list")
            if not x.get("lang"):
                probs.append(f"entry {i} node {nid}: lang empty")
        # cycles
        par = {x.get("id"): x.get("parent") for x in nodes}
        for nid in par:
            k, hops = nid, 0
            while k != 0 and k in par and hops <= len(par):
                k, hops = par[k], hops + 1
            if hops > len(par):
                probs.append(f"entry {i} node {nid}: cycle")
                break
        det = ce.get("detached") or []
        tally["detached"] = tally.get("detached", 0) + len(det)
        for d in det:
            fn = d.get("from_node")
            if fn not in en:
                probs.append(f"entry {i}: detached from_node {fn} not a Nourai node")
            if not (d.get("words") and d.get("belongs_to") and d.get("why") and d.get("why_fa")):
                probs.append(f"entry {i}: detached {fn} needs words, belongs_to, why, why_fa")
        det_ids = {d.get("from_node") for d in det}
        for d in det:
            u = d.get("under")
            if u is not None and (u not in det_ids or u == d.get("from_node")):
                probs.append(f"entry {i}: detached {d.get('from_node')} under {u}, which is not another detached item")
        split_ids = {x.get("id") for x in nodes if x.get("change") == "split"}
        dropped = set(ce.get("dropped_empty") or [])
        for d in dropped:
            if d in en and en[d].get("words"):
                probs.append(f"entry {i}: dropped_empty {d} has words")
        for nid in en:
            in_tree = seen.get(nid, 0)
            if in_tree > 1:
                probs.append(f"entry {i}: Nourai node {nid} used {in_tree} times")
            if not in_tree and nid not in det_ids and nid not in dropped:
                probs.append(f"entry {i}: Nourai node {nid} not accounted for")
            if in_tree and nid in det_ids and nid not in split_ids:
                probs.append(f"entry {i}: Nourai node {nid} both in tree and detached (mark it split)")
    return probs, tally


def main(argv):
    pages = [int(a) for a in argv] or sorted(int(p.stem.split("-")[1]) for p in CORR.glob("page-*.json"))
    bad = 0
    for n in pages:
        probs, tally = check(n)
        for p in probs:
            print(f"PROBLEM page {n}: {p}")
        bad += len(probs)
        if tally is not None:
            print(f"page {n}: " + ", ".join(f"{k} {v}" for k, v in sorted(tally.items(), key=lambda kv: str(kv[0]))) + ("" if probs else " - ok"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
