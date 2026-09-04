#!/usr/bin/env python3
"""One-time, token-free index of a scanned dictionary: OCR every page with the
LATIN (eng) model only and store the text per page, so that headwords given in
Latin transliteration (and Latin-script cognates, Pokorny numbers, etc.) can be
grepped to find the right page, which is then fetched with tools/ref_page.py.

    python3 tools/ref_index_latin.py <pdf> <out_pages.txt> [--dpi 150]
"""
import sys, os, re, subprocess, tempfile

def main(argv):
    pdf, out = argv[0], argv[1]
    dpi = argv[argv.index("--dpi") + 1] if "--dpi" in argv else "150"
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    parts = []
    with tempfile.TemporaryDirectory() as td:
        for p in range(1, n + 1):
            base = os.path.join(td, "p")
            subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", dpi, "-gray", "-png", "-singlefile", pdf, base], check=True)
            r = subprocess.run(["tesseract", base + ".png", "-", "-l", "eng", "--psm", "6"], capture_output=True, text=True)
            parts.append(f"[pdf page {p}]\n" + r.stdout)
            if p % 50 == 0:
                print(f"  {p}/{n}", file=sys.stderr)
    open(out, "w", encoding="utf-8").write("\f".join(parts))
    print(f"{out}: {n} pages")

if __name__ == "__main__":
    main(sys.argv[1:])
