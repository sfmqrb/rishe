#!/usr/bin/env python3
"""Structural validation of extracted page JSONs.

Usage: validate.py <dir> [dir...]
Checks: parseable, page numbers consistent with filename, node ids unique,
parents resolve, words well-formed, Persian fields contain Arabic-script text.
"""
import json, re, sys
from pathlib import Path

AR = re.compile(r"[؀-ۿ]")


def check(f):
    errs, warns = [], []
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"JSON parse error: {e}"], []
    m = re.match(r"page-(\d+)", f.stem)
    if m and d.get("pdf_page") != int(m.group(1)):
        errs.append(f"pdf_page {d.get('pdf_page')} != filename {m.group(1)}")
    if d.get("book_page") != d.get("pdf_page", 0) - 30:
        errs.append(f"book_page {d.get('book_page')} != pdf_page-30")
    for ei, e in enumerate(d.get("entries", [])):
        tag = f"entry[{ei}] {e.get('root', {}).get('name', '?')}"
        root = e.get("root")
        if not root or not root.get("name"):
            errs.append(f"{tag}: missing root/name")
            continue
        if root.get("redirect"):
            continue
        nodes = e.get("nodes", [])
        if not nodes and not root.get("redirect"):
            warns.append(f"{tag}: no nodes")
        ids = [n.get("id") for n in nodes]
        if len(ids) != len(set(ids)):
            errs.append(f"{tag}: duplicate node ids")
        idset = set(ids)
        for n in nodes:
            p = n.get("parent", 0)
            if p != 0 and p not in idset:
                errs.append(f"{tag}: node {n.get('id')} parent {p} unresolved")
            if p == n.get("id"):
                errs.append(f"{tag}: node {n.get('id')} is its own parent")
            if not n.get("lang"):
                warns.append(f"{tag}: node {n.get('id')} has no lang")
            for w in n.get("words", []):
                if not w.get("translit") and not w.get("script"):
                    warns.append(f"{tag}: node {n.get('id')} word with no translit/script")
                s = w.get("script")
                if s and not AR.search(s):
                    errs.append(f"{tag}: node {n.get('id')} script has no Arabic chars: {s!r}")
                if "UNCLEAR" in str(w):
                    warns.append(f"{tag}: node {n.get('id')} has UNCLEAR marker")
            q = n.get("quote")
            if q and q.get("text") and not AR.search(q["text"]):
                errs.append(f"{tag}: node {n.get('id')} quote not Arabic-script")
            x = n.get("script_extra")
            if x and not AR.search(x):
                errs.append(f"{tag}: node {n.get('id')} script_extra not Arabic-script")
    return errs, warns


def main(dirs):
    files = sorted(f for d in dirs for f in Path(d).glob("page-*.json"))
    n_err = 0
    tot_e = tot_n = tot_w = tot_fa = 0
    for f in files:
        errs, warns = check(f)
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
            es = d.get("entries", [])
            tot_e += len(es)
            for e in es:
                ns = e.get("nodes", [])
                tot_n += len(ns)
                for n in ns:
                    tot_w += len(n.get("words", []))
                    tot_fa += sum(1 for w in n.get("words", []) if w.get("script"))
        except Exception:
            pass
        for e in errs:
            print(f"ERROR {f.name}: {e}")
            n_err += 1
        for w in warns:
            print(f"  warn {f.name}: {w}")
    print(f"\n{len(files)} files, {tot_e} entries, {tot_n} nodes, {tot_w} words "
          f"({tot_fa} with Persian script), {n_err} errors")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["data/extracted/batch"]))
