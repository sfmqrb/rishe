#!/usr/bin/env python3
"""Build an exact printed-page -> pdf-page map for a scanned reference by OCRing
only the header strip (top 12%) of every page at low resolution.

    python3 tools/ref_index_pages.py <pdf> <out.json> [--lang fas] [--band 0.12]

Output: {"pdf_pages": N, "map": {"<printed>": <pdf page>, ...}, "unmapped": [...]}.
Persian/Arabic digits are normalised to ASCII. Pages whose header does not OCR to a
plausible number are interpolated from their neighbours when unambiguous.
"""
import sys, os, json, re, subprocess, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESSDATA = os.path.join(ROOT, "data", "verification", "sources", "refs", "tessdata")
DIGITS = {ord(c): str(i) for i, c in enumerate("۰۱۲۳۴۵۶۷۸۹")}
DIGITS.update({ord(c): str(i) for i, c in enumerate("٠١٢٣٤٥٦٧٨٩")})


def main(argv):
    pdf, out = argv[0], argv[1]
    lang = argv[argv.index("--lang") + 1] if "--lang" in argv else "fas"
    band = float(argv[argv.index("--band") + 1]) if "--band" in argv else 0.12
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
    raw = {}
    with tempfile.TemporaryDirectory() as td:
        for p in range(1, n + 1):
            base = os.path.join(td, "p")
            png = base + ".png"
            # render only the top band (pdftoppm crop), no full-page render
            subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", "100", "-gray", "-png", "-singlefile",
                            "-x", "0", "-y", "0", "-W", "2000", "-H", str(int(1100 * band)), pdf, base], check=True)
            r = subprocess.run(["tesseract", png, "-", "-l", lang, "--psm", "6"], capture_output=True, text=True, env=env)
            txt = r.stdout.translate(DIGITS)
            nums = [int(x) for x in re.findall(r"(?<!\d)(\d{1,4})(?!\d)", txt)]
            raw[p] = nums
            if p % 50 == 0:
                print(f"  {p}/{n}", file=sys.stderr)
    # choose, per pdf page, the number consistent with a roughly constant offset
    cand = {}
    for p, nums in raw.items():
        for v in nums:
            cand.setdefault(p, []).append(v)
    # estimate offset as the most common (v - p) over all candidates
    from collections import Counter
    offs = Counter(v - p for p, vs in cand.items() for v in vs)
    best_off = offs.most_common(1)[0][0] if offs else 0
    mapping, unmapped = {}, []
    for p in range(1, n + 1):
        vs = [v for v in cand.get(p, []) if abs((v - p) - best_off) <= 12]
        if vs:
            mapping[vs[0]] = p
        else:
            unmapped.append(p)
    # interpolate: a pdf page between two mapped pages with consecutive numbers
    inv = {v: k for k, v in mapping.items()}
    for p in list(unmapped):
        lo, hi = p - 1, p + 1
        if lo in inv and hi in inv and inv[hi] - inv[lo] == 2:
            mapping[inv[lo] + 1] = p
            unmapped.remove(p)
    json.dump({"pdf": os.path.relpath(pdf, ROOT), "pdf_pages": n, "offset_mode": best_off,
               "map": {str(k): v for k, v in sorted(mapping.items())}, "unmapped": unmapped},
              open(out, "w"), indent=0)
    print(f"{out}: {len(mapping)} printed pages mapped, {len(unmapped)} pdf pages unmapped, modal offset {best_off}")


if __name__ == "__main__":
    main(sys.argv[1:])
