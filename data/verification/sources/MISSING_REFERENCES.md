# Nourai references: second-pass search for the items not on archive.org

Date: 2026-09-04. Scope: every reference in Ali Nourai's *Etymological Dictionary of Persian, English and other Indo-European Languages* (1999) that the first pass could not find on archive.org. Platforms searched: archive.org (advancedsearch + Digital Library of India items), Google Books (`viewapi` endpoint; the JSON API was quota-limited), HathiTrust (Bib API only: `catalog.hathitrust.org/Search` and `babel.hathitrust.org` are Cloudflare/IP-blocked from this host, so full-view items are noted but must be downloaded in a browser), Open Library / Internet Archive lending, noorlib, lib.eshia, ghbook, ketabpedia (connection refused), pdf.tarikhema (broken TLS), opac.nlai.ir (connection refused), ketabnak, parsianjoman, fidibo/taaghche, gisoom/iketab/adinehbook, academia.edu, DiVA, Wikisource/Commons, TITUS, and Persian/German/English web search. Pirate shadow libraries were not used.

Downloads are in `data/verification/sources/refs/incoming/<ABBR>/`. Machine-readable details (URLs, local files, page offsets, lookup hints) are merged into the session table `refs_online.json` (scratchpad).

"Grey" below means: the file is freely downloadable from a general file host or a free-PDF site (picofile, asmaneketab/eliteraturebook, a user upload on archive.org), not from a library or the publisher, and the book is still in copyright. They were used because the task allowed any non-shadow-library platform; the owner may prefer to buy the print edition for citation purposes.

Access levels: **OPEN** = full text downloaded locally; **OPEN (browser)** = full view on HathiTrust, not downloadable from this host; **PREVIEW** = Google Books partial view; **BORROW** = Internet Archive controlled lending (free account, 1 h / 14 d); **LOGIN** = free registration on an Iranian site; **PURCHASE** = only for sale (print or ebook); **CATALOG** = bibliographic record only; **NOTHING** = no trace online.

## Summary

| Result | Items |
|---|---|
| OPEN, downloaded and text-searchable | BQT vols 3-5 (OCR), PLA, WLD Bde I-II, BLY, ZAW, TTS, FFD (OCR), IRN (OCR), VIE (OCR) |
| OPEN (browser only, HathiTrust public domain) | SHP (1945), TYL (1933) |
| PREVIEW only | ISS (CUP 2009 reprint), KGW |
| BORROW only (archive.org lending) | OEW, PRT, AHD New College Ed., MAG, OXF, DVS, ROE, FWE |
| LOGIN (ketabnak free account) | MMF, ARM |
| PURCHASE only | MON 6-vol (print), SAP (Fidibo ebook), ZMA, DZA, AKM, FNI, IRT, ETM, AEF |
| CATALOG / NOTHING | FVA, VOP, CEL, FAF, ARK, ZFS, VSF, SNB, NFI, MFL (5-page fragment only) |

## Priority items

### 1. BQT — برهان قاطع, ed. محمد معین, vols 3-5 — OPEN (grey), OCRed
- Found on the file host picofile.com (links from farhangoadabeirani.blogsky.com, post 482); the identical scans sit behind a login on ketabnak.com (books 55304-55307, 58249).
  - vol 3 (ش–ل), Ibn Sina 2nd ed. 1342, 721 pp: https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html
  - vol 4 (م–ی), same printing, 553 pp: https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html
  - vol 5 (تعلیقات), Amir Kabir 5th pr. 1376, 293 pp: https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html
- Verified as Mo'in's edition (title pages; Latin-script Pahlavi/Avestan footnotes present).
- Local: `refs/incoming/BQT/BQT_v{3,4,5}_picofile.pdf` (image-only) + `BQT_v{3,4,5}_pages.txt` (tesseract `fas`) + `BQT_v{3,4,5}_pages_faseng.txt` (tesseract `fas+eng`, better for the Latin etyma).
- Printed-page offsets: vol 3 printed ≈ PDF page + 1209 (start) / +1207 (middle, PDF 300 = p. 1507) / +1203 (end); the scan has a few duplicated or mis-ordered leaves and reportedly lacks pp. 1291-1294, so confirm with the running-head numeral. vol 4 printed = PDF page + 1917 throughout (PDF 300 = p. 2217). vol 5 printed ≈ PDF page − 5 (PDF 150 = p. 145); the تعلیقات are keyed to main-volume page numbers.
- Not found: archive.org (only vols 1-2), Google Books (IBX2zAEACAAJ etc. = no preview), HathiTrust (only the Ottoman translation), noorlib 10294 and ghbook 12267 (other, non-Mo'in one-volume editions).

### 2. MON — فرهنگ فارسی معین, 6 vols — PURCHASE (print); only the 2-vol condensation is open
- No scan of the 6-vol Amir Kabir edition (vol 4 ترکیبات خارجی, vols 5-6 اعلام) on any platform; ketabnak's Mo'in author page (persons/6040) lists 34 titles, none of them these volumes.
- Open: the 2-vol Adena/Alizadeh condensation (1381): https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 and `_02_20171226` (downloaded to `refs/incoming/MON/`; `_text.pdf` variants with OCR layer remain on archive.org). It drops the Latin etyma and has no اعلام.
- Buy the 6-vol set (in print): iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100.

### 3. FVA — نحوی، فرهنگ واژه‌های عربی در فارسی — CATALOG
- Open Library https://openlibrary.org/works/OL4602367W (Intisharat-i Islami 1368, 582 pp). Catalogued under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)». No scan, no ebook. Second-hand purchase only.

### 4. PLA — Asbaghi, Persische Lehnwörter im Arabischen (1988) — OPEN (grey)
- https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted).
- Local: `refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf`, `PLA_pages.txt` (301 leaves; printed = leaf − 15).
- Publisher copy for purchase: harrassowitz-verlag.de. No Google/HathiTrust preview.

### 5. FFD — ابوالقاسمی، فعل‌های فارسی دری — OPEN (grey), OCRed
- Real title: «ماده‌های فعل‌های فارسی دری», Qoqnus, ISBN 964-311-015-X; 2nd printing 1385, 115 pp.
- https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ (file at dl.eliteraturebook.com).
- Local: `refs/incoming/FFD/FFD_asmaneketab.pdf` + `FFD_pages.txt` / `FFD_pages_faseng.txt` (115 leaves; printed page = PDF page − 5). Purchase: iranketab.ir/book/154409, adinehbook 964311015X.

### 6. ETM — ابوالقاسمی، ریشه‌شناسی (اتیمولوژی) — CATALOG / PURCHASE
- ketabnak.com/book/107170 (explicitly no download), ketab.ir record, adinehbook 9643110451 (print). Nothing digitised.

### 7. VOP — مشیری، فرهنگ واژه‌های اروپایی در فارسی (البرز 1371) — NOTHING
- No record with a scan and no ebook anywhere. Beware decoys: ketabnak 132354 (Zomorrodian's dictionary), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997). Second-hand only.

### 8. AEF — خالقی مطلق، اساس اشتقاق فارسی ج ۱ — CATALOG / PURCHASE
- Open Library OL38785552W (1356). The 2015 complete edition «فرهنگ ریشه‌شناسی فارسی» (publisher مهرافروز) is print-only (gisoom 11154690, digikala dkp-3058984). Proxy: Horn's German original https://archive.org/details/grundrissderneu00horngoog (already local as HRN).

### 9. ISS — Bailey, Indo-Scythian Studies: Khotanese Texts VI (1967) — PREVIEW
- Google Books https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview — usable for spot checks). HathiTrust mdp.39015034317936 search-only. archive.org has only vols I-III (khotanesetexts0103bail, lending). Purchase: Cambridge.

### 10. OEW — Shipley, The Origins of English Words (JHU 1984) — BORROW
- https://archive.org/details/originsofenglish0000ship and originsofenglish00jose (lending). HathiTrust search-only; Google no view.

### 11. PRT — Partridge, Origins — BORROW
- https://archive.org/details/originsshortetym00part (1958 1st ed., matches Nourai's pagination), originsetymologi0000part_j9t3 (4th ed. 1966), originsetymologi0000part (2009) — all lending; 8 copies in total, none open.

### 12. SAP — سیاح، فرهنگ بزرگ جامع نوین — PURCHASE (ebook)
- Fidibo PDF: https://fidibo.com/book/142427 (vol. 1, 1152 pp) and https://fidibo.com/book/142430 (vol. 2, 1206 pp), about 300,000 toman each, free sample. Google Books records 4yQPAQAAMAAJ / NoplAAAAMAAJ / HcGipwAACAAJ (no view).

### 13. IRN — فره‌وشی، ایرانویج — OPEN (grey), OCRed
- https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ (file at dl.eliteraturebook.com); 6th printing 1382, 222 pp, same setting as 1368.
- Local: `refs/incoming/IRN/IRN_eliteraturebook.pdf` + `IRN_pages.txt` (222 leaves; printed page = PDF page − 11). Google Books kP8bAAAAIAAJ (1368 ed., no view).

### 14. WLD — Walde & Pokorny, Bände I-II — OPEN
- Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled "Vwrgleichendes", which is why it was missed; duplicate in.gov.ignca.20337). Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624.
- Local: `refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf` + `WLD_Bd1_pages.txt` (887 leaves, printed = leaf − 9); `WLD_Bd2_1927_dli_106624_text.pdf` + `WLD_Bd2_pages.txt` (720 leaves, printed = leaf − 5). Band III was already local.
- HathiTrust also has both as pdus full view (mdp.39015066210405, mdp.39015066210397) for a browser.

### 15. AHD — American Heritage Dictionary, New College Edition — BORROW
- New College Edition scans with the IE appendix (1610 pp): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — lending. Avoid the ~840-pp Dell abridgements. HathiTrust mdp.39015031593562 search-only. Local proxy stays `AHD_watkins1985.txt`.

### 16. BLY — Bailey, "Hvatanica II", BSOS 9.1 (1937) — OPEN
- Contained in Robert Bedrosian's open compilation https://archive.org/details/bailey-studies-1930-1993 (PDF pp. 313-322).
- Local: `refs/incoming/BLY/BLY_Hvatanica_II_BSOS9_1937_pp69-78.pdf` + `BLY_pages.txt` (printed = leaf + 67); the full compilation (80 Bailey articles, incl. Hvatanica I, III, IV) is kept alongside.

### 17. MAG — Widengren, Muhammad the Apostle of God (1955) — BORROW
- https://archive.org/details/muhammadapostled0000geow (lending). Not in DiVA; HathiTrust pst.000011130420 search-only; Google no view.

### 18. CEL — Gupta, Comparative Etymologic Lexicon — CATALOG
- HathiTrust holds the 8-vol 1986- edition search-only (mdp.39015021572337 ...); Open Library records; the 1997 printing is not digitised. HathiTrust full-text search (in a browser) can at least confirm whether a word occurs.

### 19. KGW — Ibrahim, Kulturgeschichtliche Wortforschung (1991) — PREVIEW
- Google Books https://books.google.com/books?id=OUtZZNSUi3cC (partial preview). HathiTrust uc1.b3624504 search-only. No PDF on jamshid-ibrahim.net. Purchase: Harrassowitz.

### 20. ZAW — Bartholomae, Zum altiranischen Wörterbuch (1906) — OPEN
- Google Books https://books.google.com/books?id=agDP0HdEssEC is full view; PDF downloaded (also full view: 8q0zAQAAMAAJ; HathiTrust coo.31924026891675).
- Local: `refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf` + `ZAW_pages.txt` (306 leaves; printed = leaf − 24).

## Lower-priority items

| Abbr | Work | Result | Where |
|---|---|---|---|
| ZMA | جنیدی، زندگی و مهاجرت آریاییان | PURCHASE | in print (Balkh/Bonyad-e Neyshabur), gisoom/iketab |
| FAF | دانشگر، فرهنگ اعلام فارسی | NOTHING | no record found; check opac.nlai.ir manually |
| ARK | رکن‌زاده آدمیت، ارکان سخن | CATALOG | biographical mentions only; not digitised, not on sale |
| VFO | (unresolved abbreviation, probably = VOP) | skipped | — |
| DZA | راشد محصل، درآمدی بر دستور زبان اوستایی | PURCHASE | revised edition as ebook on taaghche.com; 1364 ed. not digitised |
| VIE | سجادیه، واژه‌های ایرانی در زبان انگلیسی | OPEN, OCRed | https://parsianjoman.org/?p=5160 (253-page scan); local `refs/incoming/VIE/VIE_sajjadieh1364_parsianjoman.pdf` + `VIE_pages.txt` (253 leaves; printed = PDF page − 6) |
| AKM | اعلم، فرهنگ اعلام کتاب مقدس | PURCHASE | in print (Niloofar 1388) |
| ZFS | ابوالقاسمی، زبان فارسی و سرگذشت آن | CATALOG | not digitised (other Abolghasemi titles are open on archive.org/parsianjoman) |
| FNI | دانایی، فرهنگ نام‌های ایرانی | PURCHASE | in print (Negah); same-title free PDFs online are unrelated |
| VSF | مهراوند، واژه‌سازی در زبان فارسی (راستی 1349) | NOTHING | zero hits; check opac.nlai.ir |
| MFL | ارانسکی، مقدمهٔ فقه‌اللغهٔ ایرانی (tr. کشاورز) | fragment | https://archive.org/details/galaxy_ub2007_yahoo_201511 (5 pages only); local `refs/incoming/MFL/` |
| IRT | سجادیه، پژوهشی در تبار مشترک ایرانیان و تورانیان | PURCHASE | gisoom/iketab |
| SNB | کوثر، سنگ‌نبشته‌ها سخن می‌گویند | NOTHING | no trace online |
| NFI | جنیدی، نامهٔ فرهنگ ایران | CATALOG | no digitised issue; ask Bonyad-e Neyshabur / parsianjoman |
| MMF | خلیلی، فرهنگ مشتقات مصادر فارسی | LOGIN | ketabnak.com/book/127793 (v1), 127795 (v2), 127796 (v4); tebyan reader |
| ARM | آریان، فرهنگ واژه‌های همانند ج ۱ | LOGIN | ketabnak.com/book/132355 |
| SHP | Shipley, Dictionary of Word Origins (1945) | OPEN (browser) | HathiTrust uc1.32106001576476 = public-domain full view (record 001441050); archive.org copies are lending only |
| OXF | Speake, Oxford Dict. of Foreign Words and Phrases (1997) | BORROW | archive.org oxforddictionary00spea, isbn_9780965016070; Google preview only for the 2008 2nd ed. |
| DVS | Davies, Roots (1981) | BORROW | archive.org rootsfamilyhisto0000davi |
| TYL | Taylor, Arabic Words in English (S.P.E. Tract XXXVIII, 1933) | OPEN (browser) | HathiTrust uc1.b4089843 (Tracts 31-40, pdus full view). Only a related 1934 Leeds article was downloadable here (`refs/incoming/TYL/`), not the tract |
| TTS | Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen (1878) | OPEN | https://archive.org/details/etymologischesw00vmuoft; local `refs/incoming/TTS/TTS_pages.txt` (printed N = leaf N + 30); OCR rough |
| ROE | Claiborne, The Roots of English (1989) | BORROW | archive.org rootsofenglish00clai, rootsofenglishre0000robe |
| FWE | Bliss, Dictionary of Foreign Words and Phrases (1966) | BORROW | archive.org dictionaryoffore00blis and 8 others |

## What to buy / borrow / fetch in a browser

- Browser (free, public domain): SHP 1945 and TYL 1933 from HathiTrust; WLD I-II are also there if the DLI scans prove insufficient.
- Borrow (free Internet Archive account): OEW, PRT (1958 copy), AHD New College Edition, MAG, OXF, DVS, ROE, FWE.
- Free registration: ketabnak.com for MMF and ARM (and the BQT/MON mirrors).
- Buy: MON 6-vol print set (needed for vols 5-6 اعلام and the Latin etyma), SAP on Fidibo (ebook), PLA/KGW from Harrassowitz, ISS from Cambridge, and the Persian print titles ETM, AEF (2015 ed.), ZMA, DZA, AKM, FNI, IRT.
- Unobtainable online (second-hand only): FVA, VOP, CEL 1997, FAF, ARK, ZFS, VSF, SNB, NFI, MFL.

## OCR notes
Image-only Persian scans (BQT 3-5, FFD, IRN, VIE) were OCRed with tesseract 5.3.4 using `fas.traineddata` from the official tesseract-ocr/tessdata_fast repository (stored in `refs/incoming/_tessdata/`; not installed system-wide). `*_pages.txt` = `fas` model; for BQT and FFD there is also `*_pages_faseng.txt` = `fas+eng` (reads the Latin-script etyma better, mangles some Persian); IRN and VIE got the `fas` pass only. Pages are separated by form-feeds; the N-th block (0-based) = PDF page N+1. Expect character errors: search for short substrings.
