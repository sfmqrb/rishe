#!/usr/bin/env python3
"""Token-free tesseract OCR of a scanned reference into one form-feed-paginated
text file, so headwords can be grepped (the 'table of contents' of a dictionary).

    python3 tools/ref_ocr_book.py <pdf> <out_pages.txt> [--lang fas+eng] [--dpi 200] [--jobs 4]
Pages are tagged [pdf page N]. Resumable: existing per-page files are reused.
"""
import sys, os, re, subprocess
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESSDATA = os.path.join(ROOT, "data", "verification", "sources", "refs", "tessdata")

def ocr_page(pdf, p, lang, dpi, wd):
    base = os.path.join(wd, f"{p:05d}")
    txt = base + ".txt"
    if os.path.exists(txt):
        return
    subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", str(dpi), "-gray", "-png", "-singlefile", pdf, base], check=True)
    env = dict(os.environ, TESSDATA_PREFIX=TESSDATA, OMP_THREAD_LIMIT="1")
    r = subprocess.run(["tesseract", base + ".png", "-", "-l", lang, "--psm", "6"], capture_output=True, text=True, env=env)
    open(txt, "w", encoding="utf-8").write(r.stdout)
    os.remove(base + ".png")

def main(argv):
    pdf, out = argv[0], argv[1]
    lang = argv[argv.index("--lang") + 1] if "--lang" in argv else "fas+eng"
    dpi = argv[argv.index("--dpi") + 1] if "--dpi" in argv else "200"
    jobs = int(argv[argv.index("--jobs") + 1]) if "--jobs" in argv else 4
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    wd = out + ".pages"
    os.makedirs(wd, exist_ok=True)
    with ThreadPoolExecutor(jobs) as ex:
        for i, _ in enumerate(ex.map(lambda p: ocr_page(pdf, p, lang, dpi, wd), range(1, n + 1)), 1):
            if i % 25 == 0:
                print(f"  {i}/{n}", file=sys.stderr)
    parts = [f"[pdf page {p}]\n" + open(os.path.join(wd, f"{p:05d}.txt"), encoding="utf-8").read() for p in range(1, n + 1)]
    open(out, "w", encoding="utf-8").write("\f".join(parts))
    print(f"{out}: {n} pages, lang {lang}")

if __name__ == "__main__":
    main(sys.argv[1:])
