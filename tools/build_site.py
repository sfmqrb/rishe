#!/usr/bin/env python3
"""Merge extracted page JSONs into the site template.

Usage: build_site.py <extracted-dir> [more dirs...] -o <out.html>
Pages are deduplicated by pdf_page (later dirs win)."""
import json, sys, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "site" / "template.html"
FA_TRANSLATIONS = ROOT / "data" / "translations" / "fa.json"


def splice_empty(entry):
    """Remove content-free connector nodes, reparenting their children."""
    nodes = entry.get("nodes", [])
    empty = {n["id"]: n.get("parent", 0) for n in nodes
             if not n.get("lang") and not n.get("words") and not n.get("quote")
             and not n.get("note") and not n.get("script_extra")}
    if not empty:
        return
    entry["nodes"] = [n for n in nodes if n["id"] not in empty]
    for n in entry["nodes"]:
        p = n.get("parent", 0)
        while p in empty:
            p = empty[p]
        n["parent"] = p


def load_pages(dirs):
    pages = {}
    for d in dirs:
        for f in sorted(Path(d).glob("page-*.json")):
            try:
                pg = json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                print(f"  ! skipping {f}: {e}", file=sys.stderr)
                continue
            for e in pg.get("entries", []):
                splice_empty(e)
            pages[pg["pdf_page"]] = pg
    return [pages[k] for k in sorted(pages)]


def main(argv):
    if "-o" in argv:
        i = argv.index("-o")
        out = Path(argv[i + 1])
        dirs = argv[:i]
    else:
        out = ROOT / "site" / "risheh.html"
        dirs = argv
    if not dirs:
        dirs = [ROOT / "data" / "extracted"]
    pages = load_pages(dirs)
    n_entries = sum(len(p.get("entries", [])) for p in pages)
    data = json.dumps({"pages": pages}, ensure_ascii=False, separators=(",", ":"))
    html = TEMPLATE.read_text(encoding="utf-8")
    assert html.count("/*__DATA__*/;") == 1, "data placeholder not found in template"
    html = html.replace("/*__DATA__*/;", data + ";", 1)
    assert html.count("/*__I18N__*/{};") == 1, "i18n placeholder not found in template"
    n_fa = 0
    if FA_TRANSLATIONS.exists():
        fa = json.loads(FA_TRANSLATIONS.read_text(encoding="utf-8"))
        n_fa = len(fa)
        html = html.replace("/*__I18N__*/{};",
                            json.dumps(fa, ensure_ascii=False, separators=(",", ":")) + ";", 1)
    research = ROOT / "data" / "research" / "research.json"
    assert html.count("/*__RESEARCH__*/null;") == 1, "research placeholder not found in template"
    if research.exists():
        html = html.replace("/*__RESEARCH__*/null;",
                            research.read_text(encoding="utf-8").strip() + ";", 1)
    out.write_text(html, encoding="utf-8")
    print(f"{out}: {len(pages)} pages, {n_entries} entries, {n_fa} fa strings, {out.stat().st_size/1024:.0f} KB")


if __name__ == "__main__":
    main(sys.argv[1:])
