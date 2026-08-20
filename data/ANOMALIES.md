# Source-PDF anomalies

- **PDF page 122 is a byte-identical duplicate of PDF page 121** (both are book
  page 91, root Deru 1). Verified by md5 of 200-DPI renders. Consequence:
  **book page 92 is missing from the PDF** — per the book's own ROOTS index it
  held the charts for roots **Deu 1, Deu 2, Deuk**. The EPUB derives from the
  same scan and lacks them too. If another copy of the book is ever available,
  extract these three roots from it.
- Page-number mapping stays `book = pdf − 30` for all other pages (verified at
  pdf 101→71, 123→93, 129→99, 601→571). Only pdf 122 deviates (footer 91).
- `page-122.json` is intentionally absent from `data/extracted/batch/`.
