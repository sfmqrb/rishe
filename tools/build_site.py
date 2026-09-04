#!/usr/bin/env python3
"""Merge extracted page JSONs into the site template.

Usage: build_site.py <extracted-dir> [more dirs...] -o <out.html>
Pages are deduplicated by pdf_page (later dirs win)."""
import json, sys, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "site" / "template.html"
FA_TRANSLATIONS = ROOT / "data" / "translations" / "fa.json"
VERIFICATION = ROOT / "data" / "verification"
REFS_TABLE = VERIFICATION / "sources" / "refs_online.json"

VERDICTS = ("confirmed", "plausible", "disputed", "unverified", "transcription_suspect")


def attach_verification(pg, summary):
    """Attach data/verification/page-<pdf>.json (per-arrow verdicts, derivation
    explanations, sources, reference checks) to the page's entries as e["verif"]."""
    vf = VERIFICATION / f"page-{pg['pdf_page']}.json"
    if not vf.exists():
        return
    try:
        v = json.loads(vf.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"  ! skipping {vf}: {e}", file=sys.stderr)
        return
    ventries = {ve.get("entry"): ve for ve in v.get("entries", [])}
    for i, e in enumerate(pg.get("entries", [])):
        ve = ventries.get(i)
        if not ve or e.get("root", {}).get("redirect"):
            continue
        nodes = {}
        for vn in ve.get("nodes", []):
            nodes[str(vn.get("id"))] = {k: vn.get(k) for k in ("verdict", "derivation", "sources", "ref_check", "consulted") if vn.get(k)}
            summary["nodes"][vn.get("verdict")] = summary["nodes"].get(vn.get("verdict"), 0) + 1
            for rc in vn.get("ref_check") or []:
                summary["refs"][rc.get("status")] = summary["refs"].get(rc.get("status"), 0) + 1
        e["verif"] = {k: ve.get(k) for k in ("verdict", "modern_form", "note", "sources", "ref_check", "consulted") if ve.get(k)}
        e["verif"]["nodes"] = nodes
        e["verif"]["on"] = v.get("verified_on")
        summary["roots"][ve.get("verdict")] = summary["roots"].get(ve.get("verdict"), 0) + 1
        summary["pages"].add(pg["pdf_page"])


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


def load_pages(dirs, summary=None):
    pages = {}
    for d in dirs:
        for f in sorted(Path(d).glob("page-*.json")):
            try:
                pg = json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                print(f"  ! skipping {f}: {e}", file=sys.stderr)
                continue
            if summary is not None:
                attach_verification(pg, summary)
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
    summary = {"nodes": {}, "roots": {}, "refs": {}, "pages": set()}
    pages = load_pages(dirs, summary)
    n_entries = sum(len(p.get("entries", [])) for p in pages)
    n_nodes = sum(len(e.get("nodes", [])) for p in pages for e in p.get("entries", []))
    summary["pages"] = len(summary["pages"])
    summary["total_pages"] = len(pages)
    summary["total_nodes"] = n_nodes
    refs = {}
    if REFS_TABLE.exists():
        for ab, r in json.loads(REFS_TABLE.read_text(encoding="utf-8")).items():
            refs[ab] = {"title": r.get("title") or "", "url": r.get("url") or "", "kind": r.get("kind") or "",
                        "cites": r.get("cites") or "page number", "hint": (r.get("lookup_hint") or "")[:400],
                        "notes": (r.get("notes") or "")[:400], "offset": r.get("page_offset") or ""}
    data = json.dumps({"pages": pages, "verif_summary": summary, "refs": refs}, ensure_ascii=False, separators=(",", ":"))
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
    ganjoor = ROOT / "data" / "research" / "ganjoor.json"
    assert html.count("/*__GANJOOR__*/null;") == 1, "ganjoor placeholder not found in template"
    if ganjoor.exists():
        gj = json.loads(ganjoor.read_text(encoding="utf-8"))
        html = html.replace("/*__GANJOOR__*/null;",
                            json.dumps(gj, ensure_ascii=False, separators=(",", ":")) + ";", 1)
    out.write_text(html, encoding="utf-8")
    nv = sum(summary["nodes"].values())
    print(f"{out}: {len(pages)} pages, {n_entries} entries, {n_fa} fa strings, "
          f"{nv}/{n_nodes} nodes verified on {summary['pages']} pages, {out.stat().st_size/1024:.0f} KB")


if __name__ == "__main__":
    main(sys.argv[1:])
