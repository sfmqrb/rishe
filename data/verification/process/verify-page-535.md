# Verification process log — verify-page-535


## [2026-10-16T05:13:02.085Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 535 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-535.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-535.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-535.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 535` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:02.149Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:06.157Z] TOOL CALL #1: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md; echo ====; cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-535.txt; echo ====; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-535.json"
}
```


### [2026-10-16T05:13:06.952Z] TOOL RESULT

```
Exit code 1
# Etymology verification task — instructions

You are verifying the etymological derivations from Ali Nourai's *An Etymological
Dictionary of Persian, English and other Indo-European Languages* (1999), which this
repository (`/home/sfmqrb/git/rishe-private`) turned into JSON (`data/extracted/batch/page-<pdf>.json`).
Compact text renderings of the charts are in
`/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-<pdf>.txt`.

Each chart is a tree: a ROOT box, then nodes `#id (parent #p) [Language] refs=… | word «script» : gloss`.
An arrow parent→child in the book means "child derives from parent". `parent #0` = derives from the root.
Redirect entries (`ROOT X -> redirect to Y`) need no verification: skip them (do not include them).

## Your job, per chart (entry)

1. Verify the ROOT itself: is the reconstructed root real, is the language label right,
   is the gloss right? (e.g. PIE *dʰeyǵʰ- "knead, form" — Pokorny 244.)
2. Verify EVERY node (every derivation edge parent→child, and every word in the node):
   - Is the word real, in that language, with that meaning?
   - Does it really descend from (or was borrowed from) the parent as drawn?
   - Give the **derivation explanation**: how, phonetically and historically, the child form
     arises from the parent form. Be concrete: name the sound changes (e.g. "Av. pairi-daēza-
     → MP *pardēz; Greek borrowed it in the 5th c. BCE as paradeisos (Xenophon), Greek
     -ei- rendering Iranian -ē-; Latin paradīsus; Old French paradis; Middle English
     paradis > paradise"), the route of borrowing (which people/era/text), and the
     semantic shift ("walled enclosure" → "royal park" → "Garden of Eden" via the Septuagint).
     For Persian words descend through Old Iranian → Middle Persian → New Persian and name
     the intermediate forms when sources give them (e.g. OP didā- / Av. daēza- → MP diz →
     NP dež/dez). For Arabic loans note the Arabic stem, and for Arabic-mediated round-trips
     (Persian → Arabic → Persian) say so.
3. Give a verdict per node and per root:
   - `confirmed` — independent modern sources agree with the chart (same root, same route).
   - `plausible` — sources give a compatible but not identical picture, or the derivation
     is accepted by some scholars but not all; explain the difference.
   - `disputed` — modern scholarship (Wiktionary with citations, Etymonline, AHD, Cheung,
     Hasandust, Beekes, de Vaan, Kroonen, MacKenzie…) prefers a DIFFERENT origin, or the
     word is unrelated. Explain what the modern view is.
   - `unverified` — you could not find any independent source either way (say what you tried).
   - `transcription_suspect` — the form in the JSON is not what the sources know (a misread
     letter, an impossible form, a wrong Persian script). See "Transcription flags" below:
     you must check the printed page and say whether the book or the extraction is at fault.
4. Record sources as URLs (Wiktionary page, Etymonline page, AHD appendix entry, archive.org
   page of Klein/Horn/Bartholomae, etc.). Also note when Nourai's own cited reference
   (KLN, POK, AHD, BQT, MON, HRN, HUB…) is itself the modern standard for that claim.

## Checking Nourai's OWN cited references (required)

Every node carries `refs=` — Nourai's citations, e.g. `KLN:164; FVQ:75` (abbreviation:page;
`MON5:528` = MON vol. 5 p. 528). The author claims each arrow is supported by those pages.
You must check them:

- The bibliography key (abbreviation → book), where each reference can be read, page
  offsets and lookup hints: `/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json`
  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`, `scans`, `cites`).
- If `local_file` is set, the OCR text of that book is on disk under
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/`: grep it for the headword (try
  several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and, if a page
  offset is given, locate the cited page (pages are separated by form-feeds; `_pages.txt`
  files also carry `[pdf page N]` tags; use `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one
  page). Read the entry and judge whether it actually says what Nourai's arrow says.
- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
  NOT OCR whole books. Fetch only the cited page:
  `python3 /home/sfmqrb/git/rishe-private/tools/ref_page.py BQT:918 --image`
  It renders that one page to PNG, OCRs it (Persian OCR is rough), caches both under
  `data/verification/sources/refs/ocr/`, and prints the text plus the PNG path. If the OCR
  is unreadable, Read the PNG (you can read Persian print directly), and then SAVE what you
  read: write the entry/entries you used (headword, Mo'in's etymological footnote, and any
  surrounding lines you relied on) verbatim to the c

... [8171 characters truncated] ...

ionary** (en.wiktionary.org) — has the best coverage of Persian, Middle Persian,
  Avestan, Old Persian, Sogdian, Arabic etymologies, with citations (Cheung 2007, Hasandust,
  MacKenzie 1971, Bartholomae, Horn, Hübschmann, Nourai himself). Fetch the word's page AND
  the `Reconstruction:Proto-Indo-European/…` / `Reconstruction:Proto-Iranian/…` pages.
  Use URL-encoded Persian/Arabic script for those pages.
- **Etymonline** (etymonline.com/word/<word>) for English/French/Latin/Greek chains.
- **American Heritage Dictionary IE roots** (ahdictionary.com/word/indoeurop.html or
  ahdictionary.com/word/search.html?q=<root>) — Nourai's "AHD" citations refer to the 1975
  appendix; the online appendix is the updated edition of the same list (local: Watkins 1985).
- **Pokorny** — local OCR (POK_01/02/03, POK_full) or indo-european.info / starlingdb.org;
  Nourai's "POK:nnn" is a page number in Pokorny's IEW.
- **Klein**, **Horn**, **Hübschmann**, **MacKenzie**, **Bartholomae**, **Kent**, **Nyberg**,
  **Mann**, **Buck**, **Walde-Pokorny**, **Jeffery**, **Addi Shir**, **Asbaghi**, **Lokotsch**,
  **Gharib**, **Cheung**, **Aryanpur** … are all on disk (see SOURCE_MATRIX.md).
- **Encyclopaedia Iranica** (iranicaonline.org) for historical/cultural routes.
- **Nişanyan Sözlük** (nisanyansozluk.com) for Turkish; **Lisān al-ʿArab** / Wiktionary for Arabic.
- Use WebSearch when you don't know the right page; use WebFetch to read a page.

Do NOT fabricate sources. If a page did not load or didn't help, don't cite it.
If a chain is well known and uncontroversial (e.g. Latin → Old French → English), one good
source covering the chain is enough; spend your effort on the Iranian and Semitic links,
which are where errors are likelier.

## Output — write ONE file per page

Write `/home/sfmqrb/git/rishe-private/data/verification/page-<pdf>.json` (UTF-8, no BOM):

Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.

```json
{
  "pdf_page": 126,
  "book_page": 96,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Dheigh, Dhigha",
      "verdict": "confirmed",
      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
      "nodes": [
        {
          "id": 6,
          "lang": "Avestan",
          "words": "pairi-daeza",
          "verdict": "confirmed",
          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
        }
      ]
    }
  ]
}
```

Rules:
- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
- `words` = the transliterations of the node joined by "; " (copy from the chart).
- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
- Keep `note` on the entry for root-level comments and for anything cross-cutting.
- If a node lists several words, cover each word; if they differ in verdict, use the worst
  verdict for the node and explain per word in `derivation`.
- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
  scholarship takes.
- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
  (array) AND `derivation_fa` (string); every entry has `note_fa`.
- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
  any extraction errors (JSON differs from the printed page) the owner must fix.
  Do not paste the JSON back into your reply.
(eval):1: === not found
```


## [2026-10-16T05:13:08.944Z] TOOL CALL #2: Bash

```json
{
 "command": "sed -n 60,140p /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


## [2026-10-16T05:13:09.780Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-535.txt; echo; echo =====; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-535.json | head -c 6000"
}
```


### [2026-10-16T05:13:10.181Z] TOOL RESULT

```
Exit code 1
=== PDF page 535 (book page 505) ===
--- entry 0 ---
ROOT [Indo-European] Weidh : to separate, divide  (refs POK:1127)
#1 (parent #0) [Avestan] refs=POK:1127 | vidhavâ : separated, widow
  #2 (parent #1) [Persian] refs=BRT:1443 | bîveh «بیوه» : widow
#3 (parent #0) [Germanic] refs=AHD | widewaz : widow
  #4 (parent #3) [English] refs=None | widow
#5 (parent #0) [Latin] refs=AHD | dîvidere : to separate
  #6 (parent #5) [English] refs=None | divide
--- entry 1 ---
ROOT [Indo-European] Weik 1 : to bend, swing  (refs POK:1130)
#1 (parent #0) [Avestan / Old Persian] refs=POK:1130 | waix, waik, waig,vaĕg, vaĕca : to swing ; vyâxa, vyâxman : assembly, collection
  #2 (parent #1) [Persian] refs=BQT:67,333; HRN:14; MON:620 | vîxtan «ویختن» : to sling ; âvîxtan «آویختن (آویز)» : to hang ; âvang «آونگ» : pendulum ; bîxtan «بیختن (بیز ، بیزش)» : to sieve ; parvîzan «پرویزن» : sieve
  #3 (parent #1) [Pahlavi] refs=AEF:169; HRN:30 | han-vĕxt-an : to motivate, excite ☞Sem 1
    #4 (parent #3) [Persian] refs=BQT:178; AEF:169 | angîxtan «انگیختن» : to excite, motivate | extra: انگیزیدن ، انگیزاندن ، انگیزه
#5 (parent #0) [Sogdian] refs=SOD:417 | wye : to stir, shake
#6 (parent #0) [Germanic] refs=AHD | wik : willow twig (soft and bending), wicker ; waikwaz : bent, soft, weak ; wikôn : a turning (of time), week
  #7 (parent #6) [English] refs=None | wicker ; weak ; week
#8 (parent #0) [Latin] refs=AHD | vicis : turn, change, substitute
  #9 (parent #8) [English] refs=AHD | vice-versa ; vice president, viceroy

(eval):1: ==== not found
```


### [2026-10-16T05:13:10.191Z] TOOL RESULT

```
- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
  NOT OCR whole books. Fetch only the cited page:
  `python3 /home/sfmqrb/git/rishe-private/tools/ref_page.py BQT:918 --image`
  It renders that one page to PNG, OCRs it (Persian OCR is rough), caches both under
  `data/verification/sources/refs/ocr/`, and prints the text plus the PNG path. If the OCR
  is unreadable, Read the PNG (you can read Persian print directly), and then SAVE what you
  read: write the entry/entries you used (headword, Mo'in's etymological footnote, and any
  surrounding lines you relied on) verbatim to the companion file
  `data/verification/sources/refs/ocr/<ABBR>/<page>.vision.txt` (the tool prints the exact
  paths). The tool prefers that file next time, so nobody pays for reading the image again.
  If the printed page number on the image is off, re-run with `--pdf-page <n>` adjusted, and
  note the correct pdf page in your ref_check note. Borhan vol. 5 (the addenda, own
  pagination 1–290) is reached only as `BQT5:<page>`; Borhan vols 1–2 exist as OCR text
  files (`BQT_v1_pages.txt`, `BQT_v2_pages.txt`), vols 3–5 as `BQT_v3/4/5_pages.txt` too.
- If `kind` is `website`, use the `lookup_hint` URL pattern with WebFetch (e.g. Mo'in via
  vajehyab.com / abadis.ir).
- Do this for at least ONE cited reference per node (the most authoritative available:
  POK/AHD/KLN for IE roots, HRN/HUB/BRT/KNT/PHD for Iranian, KLN/FVQ/AFM/PLA for Semitic,
  BQT/MON for Persian). If none of a node's references is accessible, say so.

Add to every node a `ref_check` array:

```json
"ref_check": [
  {"ref": "KLN:164", "status": "supports", "note": "Klein p.164 s.v. 'cherub': Heb. kerūbh, prob. rel. to Akkad. karābu 'to bless', metathesis of b-r-k — exactly Nourai's claim."},
  {"ref": "FVQ:75", "status": "not_checked", "note": "no online copy"}
]
```

`status` ∈ `supports` (the page says what the arrow says) · `partial` (the reference has the
word but a different/looser derivation) · `contradicts` (the reference says something else)
· `not_found` (checked the text, could not find the entry/page) · `not_checked` (reference
not accessible online). Quote the key phrase of the reference in `note` when you can, with
the file/leaf/page where you found it.

Also add to each entry a root-level `ref_check` for the root's own refs (e.g. `POK:244`).

## Use EVERY relevant book on disk (required)

Checking only the reference Nourai cites is not enough. For every node, also consult the
other books in the local library that could speak to that claim, and record what each says.
The list of which books cover which kind of node, with file paths, is
`/home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md`. Minimum per node:

- an Indo-European node or root box: Pokorny (POK) AND Walde-Pokorny (WLD) AND Watkins/AHD,
  plus Mann (IEC) or Buck (SYN) when the word is a common noun;
- an Avestan / Old Persian node: Bartholomae (BRT) or Kent (KNT);
- a Pahlavi / Middle Persian node: MacKenzie (PHD) and Nyberg (NYB);
- a New Persian node: Horn (HRN), Hübschmann (HUB), Cheung (CHEUNG, for verbs), Borhan-e
  Qate' with Mo'in's footnotes (BQT), Mo'in (MON), and Aryanpur (ARY);
- a Sogdian node: Gharib (SOD); a Khotanese one: Bailey (ISS_alt_DKS);
- an Arabic node or a Persian/Arabic loan in either direction: Klein (KLN), Jeffery (FVQ),
  Addi Shir (AFM), Asbaghi (PLA), Fraenkel (AFA), Lokotsch (LKT); for French/Spanish
  Arabisms Pihan (PHN), Devic (DEV), Lammens (LAM), Dozy (DOZ);
- an English / Romance node: Klein (KLN), Skeat (SKT), Funk & Wagnalls (FSD), Webster (WEB);
  Anglo-Indian words: Hobson-Jobson (HJB), Whitworth (AID);
- a Turkic node: Vámbéry (TTS), Lokotsch (LKT).

Grep each file for the headword (several spellings; Latin transliteration for the Western
books, Persian script for BQT/MON/ARY, Pahlavi transliteration for PHD/NYB). A grep that
finds nothing is also a result ("silent"). Record everything in a `consulted` array on the
node (separate from `ref_check`, which is only for the references Nourai himself cites):

```json
"consulted": [
  {"src": "HRN", "where": "no. 3, p. 1", "stance": "contradicts", "note": "Horn separates āb 'Glanz' from āb 'water' and derives āftāb from the former"},
  {"src": "PHD", "where": "p. 5 s.v. ābād", "stance": "supports", "note": "'ābād [ʾpʾt] populous, thriving' — no water element"},
  {"src": "WLD", "where": "Bd. I p. 46", "stance": "silent", "note": "root ap- listed, no Persian compound"}
]
```

`stance` ∈ supports / contradicts / partial / silent. Quote the key phrase. Books consulted
via the web (vajehyab for Mo'in, AHD online) go here too, with the URL archived via
fetch_source.py and listed in `sources`. Every node must have at least two `consulted`
entries from different books whenever the matrix lists two or more books for its language.

## Transcription flags: say WHERE the error is (required)

For every node you mark `transcription_suspect`, look at the printed page itself — render it
with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
```


## [2026-10-16T05:13:13.589Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 140,175p /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md; cat /home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md | head -80; ls /home/sfmqrb/git/rishe-private/data/verification/sources/refs/"
}
```


## [2026-10-16T05:13:15.048Z] TOOL CALL #5: Bash

```json
{
 "command": "ls -t /home/sfmqrb/git/rishe-private/data/verification/page-5*.json | head -3; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe-private/data/verification/page-534.json'));print(json.dumps(d['entries'][0]['nodes'][0],ensure_ascii=False,indent=1)[:3000]); print(d.get('book_page'), d.get('verified_by'))\""
}
```


### [2026-10-16T05:13:15.562Z] TOOL RESULT

```
with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
(or open `site/pages/<pdf page>.jpg`) and Read the image — and add to the node:

```json
"error_in": "book",            // "book" = the printed book has the odd form (author's misprint); the extraction is faithful
                               // "extraction" = the book prints the correct form; the JSON misread it
                               // "unknown" = could not decide from the image
"book_prints": "borrāgō",      // what the printed page actually shows
"correct_form": "borrāgō"      // the form that should stand (per the sources)
```

Usually the extraction is faithful and the problem is in the book itself; say so plainly in
`derivation` too ("the book prints X; this is Nourai's misprint for Y"). Only when the JSON
differs from the page is it an extraction error (report those separately in your summary — the
owner fixes the data). Copy the page PNG you relied on to
`data/verification/sources/refs/ocr/BOOK/<pdf page>.png` so the check can be audited.

## Persian explanation (required): `derivation_fa` on every node, `note_fa` on every root

Write the derivation a second time IN PERSIAN, for a Persian reader — not a translation of the
English sentence. Think about how a Persian etymologist (حسن‌دوست، ابوالقاسمی، معین در حواشی
برهان قاطع) would explain it to an educated Persian reader:

- Use the established Persian terminology: هندواروپایی آغازین، ایرانی باستان، اوستایی، پارسی
  باستان، فارسی میانه (پهلوی)، پارتی، سغدی، فارسی نو/دری؛ وام‌واژه، وام‌گیری، دگرگونی آوایی،
  قلب (metathesis)، ابدال، همگونی، پیشوند، پسوند، ریشه، ستاک، تحول معنایی، معرّب، ریشه‌شناسی
  عامیانه (folk etymology)، هم‌ریشه (cognate)، دوگانه (doublet).
- Give the Persian word first in Persian script, then the older forms in Latin transliteration
  as Persian philology does (e.g. «آب» از فارسی میانهٔ āb / āp، از ایرانی باستان *āp-، هم‌ریشه با
  سنسکریت āp-). Persian-script forms for Arabic words; Greek/Latin words in Latin letters.
- Explain the sound changes in the way a Persian reader expects (e.g. «پ ایرانی باستان در میان
  دو واکه در فارسی میانه به ب نرم شده»؛ «ای کشیدهٔ فارسی میانه در فارسی نو به ی بدل شده»).
- Say clearly, in Persian, what the verdict means for the reader: ادعای نورایی درست است / با
  احتیاط پذیرفتنی است / پژوهش امروزی آن را رد می‌کند و به جای آن … می‌گوید / خطای چاپی کتاب /
  خطای خوانش اسکن.
- Keep it 2–5 sentences, formal but readable (نه ترجمهٔ لفظ‌به‌لفظ، نه ماشینی). Numbers in
# Source matrix — which local books to grep for each kind of node

All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.

ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).


## Indo-European roots (any IE node, root boxes)

- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt`
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt`
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LEW_1910.txt`
- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAT.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`

## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD_mackenzie.txt`
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt`
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt`
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt`
- **CHEUNG** — CHEUNG
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/CHEUNG.txt`
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt`
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  incoming
drwxr-xr-x     - sfmqrb 14 Oct 22:19  ocr
drwxr-xr-x     - sfmqrb 14 Oct 22:19  pageimg
drwxr-xr-x     - sfmqrb 14 Oct 22:25  tessdata
.rw-r--r--  600k sfmqrb 14 Oct 22:19  AFA.txt
.rw-r--r--   15M sfmqrb 14 Oct 22:19  AFM.pdf
.rw-r--r--  355k sfmqrb 14 Oct 22:19  AFM.txt
.rw-r--r--  384k sfmqrb 14 Oct 22:19  AFM_alt.txt
.rw-r--r--  342k sfmqrb 14 Oct 22:19  AFM_pages.txt
.rw-r--r--  850k sfmqrb 14 Oct 22:19  AHD_watkins1985.txt
.rw-r--r--  825k sfmqrb 14 Oct 22:19  AHM.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  AID.txt
.rw-r--r--  240k sfmqrb 14 Oct 22:19  AIN.txt
.rw-r--r--  256k sfmqrb 14 Oct 22:19  AKD.txt
.rw-r--r--  285k sfmqrb 14 Oct 22:19  ARB_abdulraheem.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  ARB_mo3rb.txt
.rw-r--r--  744k sfmqrb 14 Oct 22:19  ARP.txt
.rw-r--r--  633k sfmqrb 14 Oct 22:19  AVG.txt
.rw-r--r--  2.6M sfmqrb 14 Oct 22:19  BQT_alt_v1.txt
.rw-r--r--   139 sfmqrb 14 Oct 22:19  BQT_dli_part1.txt
.rw-r--r--  2.6M sfmqrb 14 Oct 22:19  BQT_v1.txt
.rw-r--r--   26M sfmqrb 14 Oct 22:19  BQT_v1_djvu.xml
.rw-r--r--  2.2M sfmqrb 14 Oct 22:19  BQT_v1_pages.txt
.rw-r--r--  2.4M sfmqrb 14 Oct 22:19  BQT_v2.txt
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  BQT_v2_pages.txt
.rw-r--r--  4.8M sfmqrb 14 Oct 22:19  BRT.txt
.rw-r--r--  656k sfmqrb 14 Oct 22:19  BST.txt
.rw-r--r--  1.8M sfmqrb 14 Oct 22:19  CHEUNG.txt
.rw-r--r--  593k sfmqrb 14 Oct 22:19  DEV.txt
.rw-r--r--  144k sfmqrb 14 Oct 22:19  DOZ.txt
.rw-r--r--  1.5M sfmqrb 14 Oct 22:19  DRM.txt
.rw-r--r--  560k sfmqrb 14 Oct 22:19  EAV_studies.txt
.rw-r--r--  891k sfmqrb 14 Oct 22:19  FRS.txt
.rw-r--r--  1.6M sfmqrb 14 Oct 22:19  FRS_pages.txt
.rw-r--r--   16M sfmqrb 14 Oct 22:19  FSD_vol1.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol2.txt
.rw-r--r--   13M sfmqrb 14 Oct 22:19  FSD_vol3.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol4.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  FSF.txt
.rw-r--r--  2.2M sfmqrb 14 Oct 22:19  FSF_pages.txt
.rw-r--r--  650k sfmqrb 14 Oct 22:19  FVQ.txt
.rw-r--r--  628k sfmqrb 14 Oct 22:19  FVQ_pages.txt
.rw-r--r--  573k sfmqrb 14 Oct 22:19  GPL.txt
.rw-r--r--  1.6M sfmqrb 14 Oct 22:19  HENNING_selected_papers.txt
.rw-r--r--  449k sfmqrb 14 Oct 22:19  HID.txt
.rw-r--r--  5.6M sfmqrb 14 Oct 22:19  HJB.txt
.rw-r--r--  688k sfmqrb 14 Oct 22:19  HRN.txt
.rw-r--r--  527k sfmqrb 14 Oct 22:19  HUB.txt
.rw-r--r--  3.3M sfmqrb 14 Oct 22:19  IEC.txt
.rw-r--r--  3.4M sfmqrb 14 Oct 22:19  ISS_alt_DKS.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  KFL.txt
.rw-r--r--   11M sfmqrb 14 Oct 22:19  KLN_1966.txt
.rw-r--r--   10M sfmqrb 14 Oct 22:19  KLN_1971.txt
.rw-r--r--  874k sfmqrb 14 Oct 22:19  KNT.txt
.rw-r--r--  944k sfmqrb 14 Oct 22:19  KNT_full.txt
.rw-r--r--  488k sfmqrb 14 Oct 22:19  LAM.txt
.rw-r--r--  4.6M sfmqrb 14 Oct 22:19  LAT.txt
.rw-r--r--  627k sfmqrb 14 Oct 22:19  LEW_1910.txt
.rw-r--r--  1.1M sfmqrb 14 Oct 22:19  LKT.txt
.rw-r--r--   62k sfmqrb 14 Oct 22:19  LST.txt
.rw-r--r--  4.4M sfmqrb 14 Oct 22:19  MON_part1.txt
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  MON_part2.txt
.rw-r--r--  373k sfmqrb 14 Oct 22:19  MPP.txt
.rw-r--r--  470k sfmqrb 14 Oct 22:19  NAT_2005.txt
.rw-r--r--   139 sfmqrb 14 Oct 22:19  NYB.txt
.rw-r--r--  505k sfmqrb 14 Oct 22:19  NYB_vol1.txt
.rw-r--r--  920k sfmqrb 14 Oct 22:19  NYB_vol2_glossary.txt
.rw-r--r--  664k sfmqrb 14 Oct 22:19  PEI.txt
.rw-r--r--  8.4M sfmqrb 14 Oct 22:19  PHD.pdf
.rw-r--r--  341k sfmqrb 14 Oct 22:19  PHD.txt
.rw-r--r--  8.4M sfmqrb 14 Oct 22:19  PHD_mackenzie.pdf
.rw-r--r--  609k sfmqrb 14 Oct 22:19  PHD_mackenzie.txt
.rw-r--r--  609k sfmqrb 14 Oct 22:19  PHD_pages.txt
.rw-r--r--  604k sfmqrb 14 Oct 22:19  PHN.txt
.rw-r--r--  982k sfmqrb 14 Oct 22:19  POK_01.txt
.rw-r--r--  1.1M sfmqrb 14 Oct 22:19  POK_02.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  POK_03.txt
.rw-r--r--  4.0M sfmqrb 14 Oct 22:19  POK_full.txt
.rw-r--r--  9.8M sfmqrb 14 Oct 22:19  RCH.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  SBK.txt
.rw-r--r--  226k sfmqrb 14 Oct 22:19  SDQ.txt
.rw-r--r--  1.4M sfmqrb 14 Oct 22:19  SIN.txt
.rw-r--r--  2.7M sfmqrb 14 Oct 22:19  SKT.txt
.rw-r--r--  3.0M sfmqrb 14 Oct 22:19  SKT_dli_revised.txt
.rw-r--r--  326k sfmqrb 14 Oct 22:19  SNS.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  SNS_pages.txt
.rw-r--r--  1.8M sfmqrb 14 Oct 22:19  SOD.txt
.rw-r--r--  3.7M sfmqrb 14 Oct 22:19  SOD_pages.txt
.rw-r--r--  466k sfmqrb 14 Oct 22:19  SPG_keilinschriften1881.txt
.rw-r--r--  4.5M sfmqrb 14 Oct 22:19  SYN.txt
.rw-r--r--  152k sfmqrb 14 Oct 22:19  TAD.txt
.rw-r--r--  243k sfmqrb 14 Oct 22:19  TAD_pages.txt
.rw-r--r--  313k sfmqrb 14 Oct 22:19  TLM.txt
.rw-r--r--   89k sfmqrb 14 Oct 22:19  UNV.txt
.rw-r--r--   12M sfmqrb 14 Oct 22:19  WEB_vol1.txt
.rw-r--r--  317k sfmqrb 14 Oct 22:19  WLD_band3.txt
.rw-r--r--  549k sfmqrb 14 Oct 22:19  ZAP.txt
```


### [2026-10-16T05:13:15.791Z] TOOL RESULT

```
Exit code 1
error: invalid value '/home/sfmqrb/git/rishe-private/data/verification/page-500.json' for '--time <FIELD>'
  [possible values: modified, changed, accessed, created]

For more information, try '--help'.
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import json;d=json.load(open('/home/sfmqrb/git/rishe-private/data/verification/page-534.json'));print(json.dumps(d['entries'][0]['nodes'][0],ensure_ascii=False,indent=1)[:3000]); print(d.get('book_page'), d.get('verified_by'))
                            ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/home/sfmqrb/git/rishe-private/data/verification/page-534.json'
```


## [2026-10-16T05:13:18.832Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; /bin/ls page-5*.json | tail -5; python3 -c \"\nimport json;d=json.load(open('page-518.json'));print(d.get('book_page'), d.get('verified_by'), d.get('verified_on'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:4000])\"; sed -n 1,60p /home/sfmqrb/git/rishe-private/tools/verify_check.py"
}
```


### [2026-10-16T05:13:19.354Z] TOOL RESULT

```
page-55.json
page-56.json
page-57.json
page-58.json
page-59.json
488 claude-opus-5.5 2026-10-14
{
 "entry": 0,
 "root": "Umm",
 "verdict": "confirmed",
 "modern_form": "Proto-Semitic *ʔimm- / *ʔumm- 'mother' (< Proto-Afroasiatic *ʔim-)",
 "note": "The Semitic 'mother' word is secure: Arabic umm (dial. imm), Hebrew ʾēm, Aramaic-Syriac ʾem, Ethiopic ʾem, Akkadian ummu, all < Proto-Semitic *ʔimm-/*ʔumm-. Root, label and gloss correct. The weak point of the chart is NOT the root but the Turkic branch (#3-#5): Klein (and Skeat) analyse begum as beg + Arabic umm 'mother of the bey', but Hobson-Jobson, Lokotsch, Webster, Mo'in and modern Wiktionary/AHD/Nişanyan take Eastern Turkic begim/begüm and xanım as beg/xan + Turkic suffix -im/-üm (1st-person possessive 'my lord', used as a feminine title), so the Arabic 'umm' there is a learned folk etymology. The Persian script for ommî's parenthetical is printed '(امّل)' in the book itself (an odd form, probably meant for a plural such as امّیّون/امّیّین); the extraction is faithful.",
 "note_fa": "واژهٔ «اُم» (مادر) از سامی آغازین *ʔimm-/*ʔumm- است و هم‌ریشه با عبری ʾēm، آرامی ʾem و اکدی ummu؛ پس ریشه و معنای آن درست است. اما شاخهٔ ترکی نمودار سست است: کلاین و اسکیت «بیگم» را ترکیبِ beg با «اُم» عربی («مادرِ بیگ») دانسته‌اند، ولی هابسن‌جابسن، لوکوچ، معین و پژوهش امروزی begim/begüm و xanım را از beg/xan با پسوند ترکیِ -im/-üm (ضمیر ملکی «ـَم»: «بیگِ من، خانِ من») می‌دانند و پیوند آن با «اُم» عربی را ریشه‌شناسی عامیانه می‌شمارند. ادعای نورایی دربارهٔ خود ریشه درست است، دربارهٔ بیگم و خانم با پژوهش امروزی سازگار نیست.",
 "sources": [
  "https://en.wiktionary.org/wiki/أم"
 ],
 "ref_check": [
  {
   "ref": "KLN:160",
   "status": "supports",
   "note": "KLN_1966.txt leaf 95 (pp. ~160-161), s.v. begum (line 4670): 'Turk., a hybrid coined fr. beg and Arab. umm, 'mother', ... The second element is rel. to Heb. em, Aram.-Syr. em, Ethiop. em, Akkad. ummu, 'mother''. Also s.v. aunt (line 3982): 'Arab. umm, imm, Ethiop. em, Akkad. ummu, 'mother''. Supports the Semitic root."
  }
 ],
 "consulted": [
  {
   "src": "FVQ",
   "where": "p. 85-86 fn. 3 (FVQ.txt line ~5633, grep 'Ummij')",
   "stance": "partial",
   "note": "Jeffery quotes Horovitz: Muhammad 'wendet öfter das dasselbe besagende Ummī an, welches ... die eigentliche arabische Übertragung von 'Am ha'arez darstellt' — treats umm/umma family as native Arabic; no comment on 'mother' itself."
  },
  {
   "src": "SKT",
   "where": "SKT.txt line 23803, s.v. Begum",
   "stance": "supports",
   "note": "'Pers. begam, a queen, lady of rank; lit. 'mother of the governor.' — Turk. beg, bey, governor; Arab. um, umm, mother.' Confirms umm 'mother'."
  }
 ],
 "nodes": [
  {
   "id": 1,
   "lang": "Arabic",
   "words": "umm; umme-ğîlân",
   "verdict": "confirmed",
   "derivation": "Arabic أُمّ umm 'mother' is the inherited Semitic word (Proto-Semitic *ʔimm-/*ʔumm-, cf. Heb. ʾēm, Akk. ummu). أُمّ غَيْلان umm ghaylān, lit. 'mother of the ghūls' (ghaylān, pl. of ghūl 'desert demon'), is the classical Arabic name of the thorny desert acacia (Vachellia nilotica / gummifera); the name reflects the belief that ghouls haunt such thickets. 'Umm X' is a productive Arabic naming pattern for plants and animals ('possessor/abode of X').",
   "derivation_fa": "«اُمّ» در عربی همان واژهٔ موروثیِ سامی برای «مادر» است (سامی آغازین *ʔimm-، عبری ʾēm). «اُمّ غَیلان» یعنی «مادرِ غول‌ها» (غَیلان جمعِ غول) و نامِ درختچهٔ خاردار بیابانی، گونه‌ای اقاقیا (صمغ عربی)، است؛ عرب‌ها این خاربُن‌ها را جایگاه غولان می‌پنداشتند. الگوی «اُمّ + اسم» در عربی برای نام‌گذاری گیاهان و جانوران رایج است. ادعای نورایی درست است.",
   "sources": [
    "https://en.wiktionary.org/wiki/أم",
    "https://en.wiktionary.org/wiki/أم_غيلان"
   ],
   "ref_check": [
    {
     "ref": "KLN:160",
     "status": "partial",
     "note": "KLN_1966 leaf 95 s.v. begum: 'Arab. umm, 'mother' ... rel. to Heb. em, Aram.-Syr. em, Ethiop. em, Akkad. ummu' — supports umm; Klein has no entry for umm ghaylān (grep 'ghailan|ghaylan' silent)."
    }
   ],
   "consulted": [
    {
     "src": "SKT",
     "where": "line 23803 s.v.
#!/usr/bin/env python3
"""Check data/verification/*.json against data/extracted/batch/*.json.

Reports pages with no verification file, entries/nodes missing from the
verification, invalid verdicts, and a verdict tally.  Exit code 1 if any
verification file is malformed or incomplete.
"""
import glob, json, os, sys, collections

VERDICTS = {"confirmed", "plausible", "disputed", "unverified", "transcription_suspect"}
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "extracted", "batch")
VER = os.environ.get("VERIFY_DIR") or os.path.join(ROOT, "data", "verification")


def page_no(path):
    return int(os.path.basename(path).split("-")[1].split(".")[0])


def main(argv):
    only = set(int(a) for a in argv[1:])
    missing_pages, problems = [], []
    tally = collections.Counter()
    root_tally = collections.Counter()
    ref_tally = collections.Counter()
    con_tally = collections.Counter()
    con_books = collections.Counter()
    nodes_total = nodes_done = 0
    flagged = []
    for src in sorted(glob.glob(os.path.join(SRC, "page-*.json")), key=page_no):
        pg = page_no(src)
        if only and pg not in only:
            continue
        d = json.load(open(src))
        vpath = os.path.join(VER, f"page-{pg}.json")
        entries = [(i, e) for i, e in enumerate(d["entries"]) if not e["root"].get("redirect")]
        need = sum(len(e["nodes"]) for _, e in entries)
        nodes_total += need
        if not os.path.exists(vpath):
            if need:
                missing_pages.append(pg)
            continue
        try:
            v = json.load(open(vpath))
        except Exception as ex:
            problems.append(f"page {pg}: invalid JSON ({ex})")
            continue
        ventries = {ve.get("entry"): ve for ve in v.get("entries", [])}
        for i, e in entries:
            ve = ventries.get(i)
            if ve is None:
                problems.append(f"page {pg}: entry {i} ({e['root']['name']}) missing")
                continue
            rv = ve.get("verdict")
            if rv not in VERDICTS:
                problems.append(f"page {pg}: entry {i} root verdict {rv!r} invalid")
            else:
                root_tally[rv] += 1
                if rv in ("disputed", "transcription_suspect"):
                    flagged.append((pg, e["root"]["name"], "ROOT", rv, ve.get("note", "")))
```


## [2026-10-16T05:13:34.809Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'))\nfor k in ['POK','AHD','BRT','BQT','HRN','MON','AEF','SOD','WLD','CHEUNG','PHD']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\""
}
```


## [2026-10-16T05:13:35.589Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'weidh|weik-|weig-' AHD_watkins1985.txt | head -40"
}
```


### [2026-10-16T05:13:35.948Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
CHEUNG null
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
```


### [2026-10-16T05:13:36.019Z] TOOL RESULT

```
157:The root deme-' denoted both the house (Latin domus) and the household as a social unit. The father of the family (Latin pater familias) was the “master of the house” (Greek despotes) or simply “he of the house” (Latin dominus). A larger unit was the vil- lage, designated by the word weik-'. The
1135:Old English war, seaweed: SEAWARE. 3. Suffixed zero-grade form *wi-ria- in Latin (of Celtic origin) viriae, bracelets: FERRULE. 4. Suffixed form *wei-ti- in Ger- manic *with- willow, in Old English withig, wiry: wITHY. 5. Suffixed zero-grade form *wi-t- in Germanic withj6n- in Old English withthe, supple twig: wITHE. II. Form *weia-, zero-grade *wi- (< *wia-). 1. Suffixed form *wi-ti- in Latin vitis, vine: VISE; VITICULTURE. 2. Suffixed form *wi-td- becoming *wittd in Latin vitta, headband: viTTA. 3. Suffixed form *wi-ri- probably in Greek iris, rainbow, and Iris, rainbow goddess: (IRIDACEOUS), IRIDO-, IRIS, IRIS; (IRIDIUM), (IRISITIS). 4. Suffixed form *wi-n- per- haps in Greek is (genitive inos), sinew: EXINE, INOSITOL, INOTROPIC. [Pok. 1. wei- 1120.] wei-?. To go after something. Suffixed o-grade form in Germanic *wai-thj6-, “pursuit,” with denominative *waithanjan, to hunt, plunder, in Old French gaaignier, gaigner, to obtain: GAIN}; ROWEN. [Pok. 3. wei- 1123.] wei-%. To wither. Extended form *weis- in Germanic *wis- in suffixed form *wis-n-6n in Old English wisnian, to wither, shrivel, shrink: wizEN. [Pok. 2. wei- 1123.] wei-*. Vice, fault, guilt. 1. Suffixed zero-grade form *wi-tio- in Latin vitium, fault, vice: vICE1, vICcIoUs, VITIATE. 2. Suffixed form “wi-tu- in: a. Latin vitiligo, tetter (< “blemish”): vITILIGO; b. Latin vituperdre, to abuse (perhaps formed after Latin recuperdre, to regain; see kap-): VITUPERATE. [Pok. 1. wi- 1175.] weid-. To see. I. Full-grade form *weid-. 1. Germanic *witan, to look after, guard, ascribe to, reproach, in: a. Old English witan, to reproach: Twit; b. Old Proven- gal guida, a guide: GUIDE; c. Germanic derivative noun *witi- in Old English wite, fine, penalty: WITE!. 2. Suf- fixed form *weid-to- in Germanic *wissaz in: a. Old English wis, wise: WISE!; b. Old English wisdém, learn- ing, wisdom (-d6ém, abstract suffix; see dhé-'): WISDOM; c. Old High German wissago, seer, prophet: WISEACRE; d. Germanic *wissdén-, appearance, form, manner, in (i) Old English wise, wis, manner: WISE? (ii) Old French guise, manner: GUISE. 3. Suffixed form *weid-es- in Greek eidos, form, shape: EIDETIC, EIDOLON, IDOL, IDYLL, -OID; IDOCRASE, KALEIDOSCOPE. 4. Perhaps Greek Haidés (also Aidés), the underworld, perhaps “the invisi- ble” (> French Hadés): HADAL, Hangs. II. Zero-grade form *wid-. 1.Germanic *wit- in: a. Old English wit, witt, knowledge, intelligence: wit}; b. Old English wita (genitive plural witena), wise man, councilor: WITENAGE- MOT. 2. Germanic *witan in Old English witan, to know: WIT2; UNWITTING. 3. Suffixed form *wid-to- in Germanic *wissaz, known, in Old English gewis, gewiss, certain, sure: IWIS. 4. Form *wid-é- (with participial form *weid-to-) in Latin vidére (past participle visus), to see, look: VIDE, VIEW, VISA, VISAGE, VISION, VISTA, VOYEUR; ADVICE, (ADVISE), BELVEDERE, CLAIRVOYANCE, ENVY, EVIDENT, INTERVIEW, PREVISE, PROVIDE, REVIEW, SU- PERVISE, SURVEY. 5. Suffixed form *wid-es-ya in Greek idea, appearance, form, idea: IDEA, IDEO-. 6. Suffixed form *wid-tor- in Greek histdr, wise, learned, learned man: HISTORY, (STORY!); POLYHISTOR. 7. Suffixed nasal- ized form *wi-n-d-no- in: a. Irish fionn, white (< “clearly visible”): COLCANNON; b. Welsh gwyn, gwynn, white: PENGUIN. 8. Celtic compound *dru-wid-, ““knower of trees” (*dru-, tree; see deru-). III. Suffixed o-grade form *woid-o- in Sanskrit vedah, knowledge: VEDA; RicG- VepaA. [Pok. 2. ufe)di- 1125.] weidh-. To divide, separate. 1. Suffixed zero-grade form *widh-ewo-, “bereft,” feminine *widh-ewd-, “woman separated (from her husband by death),” in Germanic *widuw6 in Old English widuwe, widow: wiDow. 2. Zero-grade form *widh- in Latin dividere, to separate (dis-, intensive prefix): DEVISE, DIVIDE, POINT-DEVICE. [Pok. weidh- 1127.] weie-. Vital force. Perhaps related to wi-ro-. Zero-grade form *wi- (< *wia-) in Latin vis, force, with irregular
1136:weik-'
1137:derivatives violdre, to treat with force, and violentus, vehement: VIM, VIOLATE, VIOLENT. [In Pok. 3. wei- 1123.] weik-', Clan (social unit above the household). 1. Suf- fixed form *weik-slé in Latin villa, country house, farm: VILLA, VILLAGE, VILLAIN, VILLANELLE, (VILLEIN); (BI- DONVILLE). 2. Suffixed o-grade form *woik-o- in: a. La- tin vicus, quarter or district of a town, neighborhood: (VICINAGE), VICINITY; b. Greek oikos, house, and its derivative oikia, dwelling: ANDROECIUM, AUTOECIOUS, DIOCESE, DIOECIOUS, DIOICOUS, ECESIS, ECOLOGY, ECON- OMY, ECUMENICAL, HETEROECIOUS, MONOECIOUS, PAR- IsH, TRIOECIOUS. 3. Zero-grade form *wik- in Sanskrit vis-, dwelling, house, with derivative vaisyah, settler: Vaisya. [Pok. weik- 1131.] weik-2. In words connected with magic and religious notions (in Germanic and Latin). 1. Germanic suffixed form *wih-l- in Old English wigle, divination, sorcery, akin to the Germanic source of Old French guile, cun- ning, trickery: GUILE. 2. Germanic expressive form *wikk- in: a. Old English wicca, wizard, and wicce, witch: WITCH; b. Old English wiccian, to cast a spell: BEWITCH. 3. Possible suffixed zero-grade form *wik-t- imé in Latin victima, animal used as sacrifice, victim (although this may belong to another root *(a)wek- not otherwise represented in English): vicTiM. [Pok. 1. weik- 1128.] weik-3, To be like. 1. Suffixed variant form ‘*eik-on- in Greek eikdn, likeness, image: ICON, (ICONIC), ICONO-; ANISEIKONIA. 2. Prefixed and suffixed zero-grade form *n-wik-és, not like (*n-, not; see ne), in Greek aikés, unseemly: AECIUM. [Pok. 3. weik- 1129.] weik-4. Also weig-. To bend, wind. I. Form weig-. 1. Ger- manic *wik- in: a. Old English wice, wych elm (having pliant branches): wyCH ELM; b. Swedish viker, willow twig, wand, akin to the Scandinavian source of Middle English wiker, wicker: WICKER; C. Old Norse vikja, to bend, turn, probably akin to the Scandinavian source of Old North French wiket, wicket (< “door that turns”): WICKET. 2. Germanic *waikwaz in: a. Old Norse veikr, pliant: WEAK; b. Dutch week, weak, soft: WEAKFISH. 3. Germanic *wik6n-, “a turning,” series, in Old English wicu, wice, week: WEEK. II. Form *weik-. Zero-grade form *wik- in: a. Latin vix (genitive vicis), turn, situ- ation, change: VICAR, (VICARIOUS), VICE; VICISSITUDE; b. Latin vicia, vetch (< “twining plant”): veTCH. [Pok. 4. ueik- 1130.] weik-5, To fight, conquer. 1. Germanic “wik- in Old Norse vigr, able in battle: WIGHT2. 2. Nasalized zero-grade form *wi-n-k- in Latin vincere (past participle victus), to conquer: VANQUISH, VICTOR, VINCIBLE; CONVINCE, EVICT. [Pok. 2. weik- 1128.] weip-. To turn, vacillate, tremble ecstatically. 1. O-grade form *woip- in Germanic *waif- in Old Norse veif, waving thing, flag, probably akin to the Scandinavian source of Anglo-Norman waif, ownerless property: WAIF!, (WAIVE), (WAIVER). 2. Variant form *weib- in Germanic *wipjan, to move back and forth, in: a. Old English wipian, to wipe: WIPE; b. Old French guiper, to cover with silk: GUIPURE; c. Middle Dutch and Middle Low German wippen, to swing: WHIP. 3. Perhaps suffixed nasalized zero-grade form *wi-m-p-ila- in: a. Old English wimpel, covering for the neck (< “something that winds around”): WIMPLE; b. perhaps Middle Dutch wimmel, auger (< “that which turns in boring”): WIMBLE. 4. Suf- fixed zero-grade variant form *wib-ro- in Latin vibrdre, to vibrate: VIBRATE. [Pok. weip- 1131.] weis-. To flow. I. 1. Germanic *wisdn-, waisén- in Old English wdse, mire, mud: 00ZE?. 2. Taken by many as a derivative of this root, but probably an independent Indo-European word, is the suffixed form *wis-o- in Latin virus, slime, poison: VIRUS. 3. Extended zero-grade form *wisk- possibly in Latin viscum, mistletoe, birdlime: VISCID, VISCOUS. II. Attributed by some to this root, but more likely of obscure origin, are some Germanic words
1217:ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
1246:ANILE an-! ANILINGUS 4no-, leigh- ANIMA ane ANIMADVERT ane- ANIMAL ane- ANIMATE ane ANIMATO ane- ANIMISM ane- ANIMOSITY ane- ANIMUS ane- ANION ei-1 ANISEIKONIA weik-3 ANKLE ank- ANKYLOSIS ank- ANLAGE an}, legh- ANNALS at- ANNEAL aidh- ANNEX ned- ANNIHILATE ne ANNIVERSARY at-, wer-3 ANNOTATE gno- ANNOUNCE neu-! ANNOY od-2 ANNUAL at ANNUITY at- ANNUL ne ANNULAR 4no- ANNULET 4no- ANNULUS 4no- ANODE sed-2 ANODYNE ed- ANOINT ong¥- ANOMALOUS sem-! ANOMIE nem- ANON ol-no- ANONYMOUS né-men- ANOPHELES obhel- ANORECTIC reg-1 ANOREXIA reg-1 ANORTHITE wrddh- ANOSMIA od-! ANSATE ans- ANSERINE ghans- ANSWER swer-1 ANT mai-1
1270:AUSPICE awi-, spek- AUSTERE saus- AUTACOID y@k- AUTARCHY arkhein AUTARKY arek- AUTHOR aug-! AUTHORIZE aug-! AUTOBAHN g*hen-* AUTOCHTHON dhghem- AUTOECIOUS weik-1 AUTOGIRO géu- AUTOMATIC men-1 AUTONOMOUS nem-
1294:BENIGN deu-?, gene- BENTHOS gWadh- BENUMB nem- BEQUEATH gWet-2 BEQUEST gWet-2 BEREAVE reup- BERM bhrem-2 BERRY bha-1 BERSERKER bher-3 BESPEAK spreg- BESPRENT spergh- BEsT bhad- BETOKEN deik- BETRAY d6- BETROTH deru BETTER bhad- BETWEEN dwo- BETWIXT dwo- BEVEL bat- BEVERAGE pO(i)- BEWITCH weik-2 BEZOAR gWhen-1, pa- BHAGAVAD-GITA g@i-2 BI- dwo-
1296:BID bheudh-, ghedh- BIDE bheidh- BIDENTATE dent- BIDONVILLE weik-1 BIENNIUM at-
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
1571:Grus_ gere-2 GUARANTY wer-5 GUARD wer-4 GUERDON lau-, wi- GUERRILLA wers-1 GUESS ghend- GUEST ghos-ti- GUIDE weid- GUILD gheldh- GUILDER ghel-2 GUILE weik-2 GUIPURE weip- GUISE weid- GULAR gWel-3 GULDEN ghel-2 GULES gwWel-3 GULF kwelp- GULLET gWel-3 Gum? ghéu-
1602:HETAERA s(w)e- HETERO- sem-! HETERODOX dek-! HETEROECIOUS weik-1 HETEROGENEOUS gene- HETERONYMOUS no-men- HEURISTIC wera-2 HEW kau-2
1662:ICEBERG bhergh-2 IcH dhgWher- ICHTHYO- dhghi- ICHTHYORNIS  or- ICICLE eis-2, yeg- ICON weik-3
1663:ICONIC weik-3 ICONO- weik-3 ICONOGRAPHY gerbh- ICONOSTASIS  sta- ICOSAHEDRON  wikmti ID I
1882:MOLTO mel-4 MOLY md6(u)lo- MOLYBDENUM plumbum MOMENT meue- MOMENTOUS meue- MOMENTUM meue- MONAD men-4 MONANTHOUS = andh- MONASTERY men-4 MONAXON aks- MonpDay mé-2 MONEY men-! MONGER meng- MONGREL mag- MONILIFORM mon- MONISH men-1 MONITION men-1 MONITOR men-1 MONK men-4 MONO- men-4 MONOCLE oOkw- MONOCLINIC klei- MONOCLINOUS klei- MONOCOQUE kokkos MONODY wed-2 MONOECIOUS weik-! MONOMER (s)mer-2 MOoNOPHYSITE bheue- MONOPODIUM ped-1 MONOPOLY pel-5 MONOTREME tere-1 MONS men-2 MONSTER men-1 MONTAGNARD men-2 MONTANE men-2 MONTE men-2 MONTH mé-2 MONTICULE men-2 MONUMENT men-! MOOCH meug-! MOOD! mé-1 MOOD? med- MOON mé-2
2061:PARGET per, yé- PARHELION sawel- PARI-MUTUEL pere-2 PARISH weik-1 PARITY2 pere-2 PARLAY pere-2 PARLEY gWelg-1 PARLIAMENT gWele-1 PARLOR gWelg-1 PARLOUS per-4 PARODY wed-2 PAROL gWele-1 PAROLE gWele-1_ PARONOMASIA n0-men- PARONYCHIA nogh- PARONYMOUS no-men- PAROTID GLAND ous- -PAROUS pere-) PAROUSIA es- PAROXYSM ak- PARRICIDE paso- PARRY pere-!
2112:POINT peuk- POINT-DEVICE weidh- POINTILLISM peuk- POISE! (s)pen- POISON pO(i)- POKE’ beu-1 PoLack pele-2 POLE! kwel-1
2389:THYME dheu-! -THYMIA dheu-1 THYROID dhwer- TICK? deigh- TICK3 dhé-1 TICKET steig- TIDE! da- TIDE2 da- TIDINGS da- TIE deuk- TIERCE trei- TIFFANY bha-1 TIGER steig- TIGHT tenk-2 TILE (s)teg- TILLER? teks- TILLERS del-3 TILT? del-3 TIMBER deme-1 TIME da- TIMOCRACY kWeig-1 TINCT teng- TINGE teng- TINSEL skeei- TINT teng-
2411:TRIO trei- TRIOECIOUS weik-1 TRIP der-1 TRIPEDAL ped-1 TRIPLE pel-3, trei- TRIPLEX trei- TRIPLOBLASTIC pel-3 TRIREME ere-1 TRISKELION skel-3 TRISMUS | strei- TRISOCTAHEDRON trei- TRITANOPIA ei- TRITE ter * TRITIUM trei- TRITONE trei- TRITURATE tere-1 TRIUMVIR trei-, wi-ro- TRIUNE oi-no- TRIVET ped-1 TRIVIAL wegh- TRIVIUM wegh- TROCAR kwetwer-, trei- TROCHAL dhregh- TROCHANTER dhregh- TROCHE dhregh- TROCHEE dhregh- TROCHLEA dhregh- TROCHOPHORE dhregh- TROGON tere-1 TROIKA trei- TROPE trep-2 TROPHALLAXIS al-1 TROPHIC- threph- TROPHO-  threph- -TROPHY threph-, trep-2 TROPIC trep-2 TROPO- trep-2 -TROPOUS  trep-2 TROT der-1
2445:VAIR wer-1 VaisyA_ weik-1 VALE! wel-3 VALEDICTION deik- VALENCE wal- VALET upo VALETUDINARIAN wal- VALHALLA kel-2, wele-2 VALIANT wal- VALID wal- VALKYRIE wele-2 VALLATION walso- VALLEY wel-3 VALONIA gWele-2 VALOR wal- VALUE wal- VALVE wel-3 VAMOOSE wadh-2 VAMP! ped-1 vaAN3 wet-1 VANADIUM wen-1 VANDAL wendh- VANE pan- VANG pag- VANILLA wag- VANIR wen-! VANISH eu-2 VANITY eu-2 VANQUISH welk-5 VAPID kwép- VAPOR kwép- VAQUERO wak- VARA wa- VARIEGATE wer-1 VARIETY wer-1 VARIOLA wer-! VARIORUM wer-! VARIOUS wer-1 VARIX wer-1 VARLET upo VaRUNA wel-1 VARUS wa- VARVE kwerp-
2451:VESPIARY wopsa VEST wes-4 VESTA wes-3 VETCH weik-4 VETERAN wet-2 VETERINARY wet-2
2452:VIADUCT wegh- VIAND gWei- VIBRATE weip- VICAR weik-4 VICARIOUS wei-4 VICE! wei-4 vIcE3 weik-4 VICENARY wikmti VICENNIAL at- VICEREINE reg-! VICEROY reg-! VICINAGE weik-1
2453:VICINITY weik-1 vicious wei-4 VICISSITUDE weik-4 VICTIM weik-2 vIcTOR weik-5 VICTUAL gWei- VIDE weid- view weid- VIGESIMAL wikmti VIGIL weg-2 VIGILANT weg-2 VIGILANTE weg-2 VIGOR weg-2 VILIPEND (S)pen- VILLA weik-1 VILLAGE weik-! VILLAIN weik-1 VILLANELLE weik-1 VILLEIN weik-1 VILLUS wel-4 vIM weie- VINACEOUS vinum VINCIBLE weik-5 VINDICATE deik- VINE vinum VINEGAR ak-, vinum VINI- vinum VINTAGE em- VIOLATE weia- VIOLENT weie- VIRAGO Wi-ro- VIREO virére VIRESCENT virére
```


## [2026-10-16T05:13:39.588Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^.{0,6}(u̯eidh|ueidh|weidh)' POK_full.txt | head; grep -n -E 'vidav|viδav|viδauu|vidhav|widdewe|viduus' POK_full.txt | head; grep -n -E '(u̯eik|ueik|weik)-.{0,40}(biegen|bend)' POK_full.txt | head"
}
```


### [2026-10-16T05:13:40.202Z] TOOL RESULT

```
89159:in addition (compare the above i/-stem) Old Indie vidhava^ widow', Avestan K/iJauads., 
89161:viduus^ stolen; looted, empty, bare, lacking from etwas'. Old Irish fedb^ widow', corn. 
89371:See also: relationship to ueik-, ue/gh-'bend' etc. is not ausgeschlossen.
```


## [2026-10-16T05:13:42.721Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 89140,89175p POK_full.txt; echo -----; grep -n -E '^Page\\(s\\): 11(27|30|31)|Page\\(s\\)' POK_full.txt | grep -E '112[6-9]|113[01]' | head"
}
```


### [2026-10-16T05:13:43.057Z] TOOL RESULT

```
"wird empty, bare, lacking, has Mangel an etwas', 1//0/7J- "vereinsamf, v/dhura-^ apart, 

separated, remote, distant from, lack, be short of; 1/0/75/" infertile ' i.e. "the empty', 

Sommer MiJnchner Studien z. Sprachwiss. 11 , 20; 



Latin dTvido, -e/"© "separate, divide', Umbrian uef Akk. PI. "partes', i/e/^"dividito' {*vef-tu); 
Lithuanian vidusm. " the interior', vidurysm. " center', Latvian v/dusm. " center, the 
interior, region'; 

Maybe nasalized alb. i/e/7o'" region, place' 

ablaut. Lithuanian i//eo'i/o//s" inside withered tree'; 

Maybe alb. {*vedudlis) vejushe'\N\6o\N' [common alb. -d- > -J^. 

in addition (compare the above i/-stem) Old Indie vidhava^ widow', Avestan K/iJauads., 
gr. r|[F]i0£O(; "Junggeselle', Latin vidua^ widow; geschiedene or unverheiratete Frau', 
viduus^ stolen; looted, empty, bare, lacking from etwas'. Old Irish fedb^ widow', corn. 
guedeu ds., cymr. gweddw^ widower', Gothic widuwo^ widow' (furthermore widuwafrnavn. 
" orphan '), Old English widuwe, wuduwe. Old High German wituwa " widow'. Old Prussian 
widdewu. Old Church Slavic vbdovads.; Indo Germanic * ui6!"euo- M]. "apart, separated', 
in Fem. substantivized " widow'; 

5-present etc. Old High German nvsa/7 "vermeiden', urweisPeri. "subterfugT, Middle 
High German only participle entwisen^ abandon from, empty, bare, lacking from'; Old 
Frisian wesa. Old High German weiso. Modern High German Waise^ orphan '(Germanic 
waisan- < *uoi6'^-son-). 

References: WP. I 239 f., WH. I 359, Trautmann 358; 
See also: compare uiA^u-^\xee\ 
Page(s): 1127-1128 

-----
11308:Page(s): 117-118 
71126:Page(s): 866 
89174:Page(s): 1127-1128 
89344:Page(s): 1125-1127 
89373:Page(s):1128 
89418:Page(s): 1128-1129 
89442:Page(s):1129 
89515:Page(s): 1130-1131 
89562:Page(s):1131 
89904:Page(s): 1131-1132
```


## [2026-10-16T05:13:45.005Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 89120,89135p POK_full.txt; echo ----; sed -n 89443,89562p POK_full.txt"
}
```


### [2026-10-16T05:13:45.322Z] TOOL RESULT

```
Maybe zero grade in alb. {*oxa) ka'ox', {*ox/e) qeP\. "oxen'. 

References: WP. I 248 f., WH. II 815, 849, Mayrhofer 1 , 98. 
Page(s):1118 

Root / lemma: ueib- 
See also: see below ue/p- 
Page(s):1124 

Root/ lemma: ueti'^-, uii'^- 

Meaning: to separate; widow 

Note: probably from *^/- "apart' and t|ho- "place' grown 

Material: Old Indie i//o'/7y5//"durchbohrt' (lengthened grade partly vec/h-, partly vyadh-, 
----

Root / lemma: ueik-4, ueig- 

Meaning: to curve, bend; to go round, to exchange 

Note: (extension from "^©/-"bend'). 

Material: 1. Old Indie vfci-\. " deception, seduction ' (Rv. 10, 10, 6; probably "*Krummheit'); 

with voiced-nonaspirated Old Indie vejate, vijate, participle vikta-, i//g/7a- "vor etwas 
zuriJckfahren, davoneilen', yC>/'a-i/y-"Einsturz threaten', abhi-vij- "umkippen', vega-m. 
"Zittern, intense Bewegung, rush', Avestan vaeg- (vaejd-) "(a projectile) swing', vaeya-m. 
"Anprall, blow, knock, prank', nivixta- "herabgeschwungen, herabgeschleudert', npers. 
vextan^ioss, fling', osset. i/e^^^/? "upset, move', balGcT^^a^ "swing, toss, fling'; Intens. Old 
Indie i/ei/^ya/e "fahrt los'; 

Old Indie v/-vyakt/ ^ufr\iaQ>t', vyacas-n. "further Raum', Avestan vyaxa-, vyaxman- 
"eongregation, meeting' (?); 



gr. sTkoj, Aor. £(F)£i^£ Alkman " recoil, nachstehen, unterliegen', (Boeotian) yT^ai 
(i.e.FsT^ai) xwpnoai Hes.; 

Latin viciat "vetcli': nasalized vincid, -/?e"umwinden, bind', \J'r(\bnaT\ previslatu 
"praevinculato"; 

Gothic waihsta^ angle, point, edge'. Middle High German we/gen 'waver'; Old English 
m'cga'beet\e, chafer'; Middle Low German nnd. w/iche/e '\Ne\6enbautr\' from *wTgele, 
diminutive to Old Saxon *wTga, westfal. tv/aja'Weidenbaum', ablaut. Old Frisian Old 
English wag. Old Saxon weg'\Na\\\ CVo/Zro-'geflochtene wall'); also Middle High German 
gewTge, Modern High German Geweih, 6\a\.Gewicht(eln) 6s. (originally probably 
"*Gezweig'); 

Latvian vTkstu, i//7r/"sich biegen, ductile become', v/ksfs' ductile, soft', vTkne' tendril '; 
Latvian vTcinat'\Naye, tummein', refl. 'sich schwenken, bend make'. 

With Indo Germanic ff. Old Icelandic vJkva, J//ri/a(w-present), vJkj'a, preterit i/e//r"from 
the Stelle move, (sich) bewegen, sich wenden'. Old Saxon wTkan' withdraw' (: sikcjo). Old 
English wTcansiexw V. ' withdraw, crumple ', Old High German w/hhan stem V. 'eine 
Richtung nehmen, withdraw'; Old Icelandic ve/kr{an6 veykr\N\t\r\ -w- after vTkva) 'soft, 
weak'. New Norwegian also "pliable' (compare Old Icelandic i/e/A/5"bend'), Old English 
wac{o\}\. of it Old Icelandic vaki) 'soft, weak, woeful, wretched, miserable ', Old Saxon wee 
"weak'. Old High German n/e/ic/? "soft, weak, timorous'; Old English wicei. "RiJster', Middle 
English ty//re/'"Weidengerte'; Middle Low German wTkm., wTkei. "Entweichen, escape'. 
Middle High German wTcfrm. "groin, flank ', formal = Old Icelandic i//7^ "small bay'. Old 
English wTci., Middle Low German wTk6s.\ Norwegian dial. viku. "small point, edge or 
bend'; Old High German tv/77/7d/7 "spring, dance, jump ', Modern High German Hessian 
wicken'rash, hasty and violent hin and her bewegen', Swedish vicka's\c\\ unstet 
bewegen, wippen'; 

Lithuanian vigrus, v'iglas' xas\\, hasty, adroit', Latvian i//e^/s "light', slov. veg' bent', 
i/ega// "waver', i/eze/7 "gebogen'. 

2. Latin i//ic/s(Gen.), vicem, vice, PI. vices, i//ic/Z?^s "variation, Abwechslung'; perhaps 
Old Irish /^ac/7"mutuum, Geschuldetes, blame'; Old Icelandic ^/a/^-i/ZV/ "exchange of gifts', 
a i/ZV/"kreuzweis' (i/ZV/a"swap, vary, exchange'); Old Saxon weiisai' trade, currency'. Old 
High German weiisai, M/e/7s// "variation, exchange, trade' (Old Saxon wehsion. Middle High 
German Modern High German wechselii); with sicherem Indo Germanic 5^ Gothic by/M"die 
an jemanden kommende order'. Old Icelandic i///r5 "Woche' (originally "*variation'), also 



'Seemeile' ("*variation the oarsman'; also Middle Low German n/e/reses 'Seemeile'), Old 
English wicu, wucu'Woche', Old Saxon w/ka\n cruce-w/ka 'Kreuzwoche', Old High 
German wehha, wohha^\Noc\r\e'; 

unclear is because of Gutturals Old Indie vistf- {*uiR-) 'work, Dienstleistung', tri-visff 
(Instr.), after Wackernagel (KZ 67, 173) "alterant, changeable', after G. Liebert 
(Nominalsuffix -//■ S. 138 f.) though "dreifache Dienstleistung'. 

References: WP. I 233 ff., WH. II 781 f., 791 f., Trautmann 338 f.. Frisk 454. 
Page(s): 1130-1131 

Root / lemma: ueiR-, uiR-, uoiRo-{* duei- ksayatlj 

Meaning: house, settling 

Note: 

Root/ lemma: ueiR-, uiR-, uoiRo-{* duel- ksayati): "house, settling' derived from Root/ 

lemma: Rt^ei-: "to settle' : Root/ lemma: kt^eO)-, kt^aO')-: "to acquire, possess'. 

Material: Old Indie vfs-i. "Wohnsitz, house', PL i//s5/7 "people, citizen', Avestan i//s-(e.g. 

Akk. vTsem, ap. viPam) "house, village. Clan', Old Indie vis-pati-^ householder, 

Gemeindehaupt', vis-patnV housewife', ablaut. Old Indie i/es/77a/7-n., jav. vaesma-m. 

"house, dwelling'. Old Indie vesa-m. "Naehbar' (as Latin vTcTnus); verbal (see below) Old 

Indie i//5a//"tritt ein, geht ein', /7/V/sa//"kehrt ein', Avestan i//s5///"geht ein, tritt ein to etwas'; 

Maybe from Skt. i//5-(RV+) "settlement, community, tribe' derived alb. {*vfs) fis 

"settlement, community, tribe', 1//5 "territory, spot, place ' 

Note: 

Alb. cognate has derived from Sanskrit not from Slavic. 

gr. o\Koc„ FoTko(; "house', oJKia ds., oIkeu) " inhabit ', oiK£Tr|<; "housemate', Tpixa-FiK£(; 
epithet the Dorer "in drei Phylen zerfallend'; alb. k/5 "place', amvise {ame^ rwoihef) " 
housewife'; 

Latin vTcus, dial. Keci/5"Hausergruppe, village, dot, Stadtteil' (= gr. FoTko(;), Umbrian 
uocu-com, Akk. i/^/r^if "aedes'; Latin K/7/a"Landhaus, estate' {*uoik-sla, with Latin suffix- 
sla, or *ueik-s-la\.o es-stem from Gothic weihs); 

Gothic weihsu.. Gen. M'e//7s/s "village, spot'; 

Old Prussian waispattin f\Vk. " housewife', Lithuanian K/espaZ/^^s "master, mister', 
viespati^ v\ob\e wife, woman', verbal Lithuanian vaisinti^ host ', v/eset/"to Gaste sein', 
Latvian v/'es/s' guest'; Old Church Slavic i/6S6 "village'. 



References: WP. I 231, WH. II 782 f., Trautmann 363 f., Vasmer 1, 193. 
Page(s):1131
```


## [2026-10-16T05:13:51.472Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'vi[dδ]ava|viBava|viöava|vi3ava|vidhav|viöauu|viSav' BRT.txt | head; grep -n -i -E 'w[eē]wag|wywk|bēwa|bewa\\b|bēva|bêva|bêwa' PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt HRN.txt HUB.txt | head -20"
}
```


### [2026-10-16T05:13:51.843Z] TOOL RESULT

```
24065:•  j.  viSavä-  f.  'Wittwe',  in  Verbindung mit  vahü-  f.  'Witt&au"':  v^u  °va  F.  2  f.
24604:1473  viSavä-  —  viS.haurva-  1474
24608:•  j,  visavi-  f.  Du.  Name  eines  Bergs  Y.5?.  2;  —  d.iidx  ta  armaiti  'pai  is»m oderGebirgs:  aAma}  haca garays fraoxsyan  '^  (sd.)  maibylca  Y.  -28.  7;  —  ySvaranS  kavä -■  'i>ai':a  Yt.  jp.4.  ,°/j  Y.  ;2.  7;  —  biritams  kava   'pS  Vt.
PHD.txt:651:wénig [wynyk! | M wynyg, N bini] nose. wénO£ [wynwk' | N bunü] lentil. wēš [zoy£ | = M, N béf] more. wé&ag [wysR! | N beta] thicket, wood. --estün [-st?n'] woodland. ~ig [-yk'] silvan. wēwag [wdpk! | N béwa] widow. 1wéxtan, wez- [NSSHWN-tn! < А V nsh; wyhtn', wyc- | P wyxt-, N bextan, béz-] sift, select, choose, separate, cleanse, purify, winnow. ~išn: selection. *wēxtan, wēz- [wyhtn!, wyc-] swing, brandish, throw, pour out. Wīdadafš [wydtpš = Av. wīdašafšū-| the south-western continent of the earth. widang [wtng | P wdng] trouble, distress, constraint. widār [xt' | N gudár] passage, entrance. widarag [wtlg | M wdr, N guàar] path, passage. widardan, wider- [wtitn!, wt(y)l- | M wd(y)r-, N guóar-] pass (by, away), cross, die. : ~išn(īh): passage, crossing, death. ~i$nig : transient. widārdan, widār- [xwt?/-tn! | M wyd’r-, N guóárdan] let pass, transport; endure, suffer. widārīdan [w?lytn'] = widardan. widaštan [wtstn' | N gušaštan] = widardan. widāxtan, widāz- [wt’hin', wtc- | (P wd’c-), N gudaxtan, gudāz-| melt, dissolve. widāzīhistan, widazih- [wt’cyh-stn'] be melted, dissolved. wider- , -išn(-īģ, -ih), v. widardan. widerān [wt(y)?n! | N guóarán) transient, dying. widest [zot(y)st! | N bidast] (hand) span (9 in.). ~ig [-yk'] span-sized, midget. widimās [wtym’s | (M wyd’m’s)] wonder, miracle. ~ig [-уА!] wonderful. ~ih: miracle. widimušt [wtymust | M wd(y)mwšt] astonished. ~ih: astonishment. *widwar [wytwl] contented, resigned, consoled. ~ih: contentment, resignation, consolation. wiftag [wyptk'] passive sodomite. wigrad [zogPt! | N bīdār] awake, alert. wigradan, wigras- [zog tn, wgl’s- | M wygr'd, wygr’s-] awaken, rouse. ~i$n(ih): awakening. wih-, v. wistan. wihan(ag) [zh?n(k)', (b-) | M wl?ng, N bahāna] cause, reason. wihēz- [wyhyc- | M twhyz-] move, progress. wihéz(ag) [wyhyc(k')] movement, progression.
PHD.txt:2880:myriad bēwar.
PHD.txt:5214:wewag wiftag
PHD_mackenzie.txt:5333:wewag [wdpk' IN bewa] widow.
PHD_mackenzie.txt:7983:widow wewag.                           wormwood dramanag.
NYB_vol2_glossary.txt:1467:évak [HDwk'; on coins *ywky] num. one, passim; hàn + ~ Arjäsp A. alone 2416, 2927; ~ ~ one by one 92$; har ~ every- one 1045-%, 10617. 11318; ~~ bēvar ten thou- sand 244; 3 ~ one third 6329-22, 9316, 1025; 4 ~-é [-’y] one fourth 998; 5 ~-é [^y] 10015-17, 10227. 1031-2; — in correspon- dence with dit, ditikar, ane, v. these ws. — Av. ačva-. OP awa- + -ka-, v. s. v. žē; MPrs yk; Paz. yak, iak, NP yak — as against MPrth ‘yw ‘one’, *ywg ‘alone’.
NYB_vol2_glossary.txt:5896:bywr: bēvar
NYB_vol2_glossary.txt:7064:Bēvarasp: Bēvar-asp
```


## [2026-10-16T05:13:56.129Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=23900 && NR<=24070 && /^ *1[0-9]{3} /' BRT.txt | head; sed -n 24063,24068p BRT.txt | cut -c1-400; grep -n -E 'vyäxa|vyaxa|vyäxman|vaeg-|vaēg-' BRT.txt | head"
}
```


### [2026-10-16T05:13:56.465Z] TOOL RESULT

```
•  j.  vi-davay-  Adj.  (auch  mask.)  Tiei von  — ,  sicher  vor  Betrug':  *aöavli'  ttqma ahmt  *'Mj  (NSra.)  nqma  ahmt  Yt /.  14.
Pü.:  yiit  haifrep,  erl.:  ki  man  iSmik /t?/lmi ^at/rißak  bovil.
•  j.  viSavä-  f.  'Wittwe',  in  Verbindung mit  vahü-  f.  'Witt&au"':  v^u  °va  F.  2  f.
Bi.  tiidhioä-  f.3>,  np.  bhia.  —  P&. :  viiaziii.  — ')  S.  No.  a.  —  '}  "Oft  in  Verbindung  mit den  Werler  für  'Weib'",  Db«.  VglS.  /.  421.
•  p,  vidama-  ni.  EN.  eines  Persers;  Heer- fiihrei  Dariui  I.  und  dessen  Genosse  bei der  Magophonie,  TSä^v^f:  -«u*  nama" bagabignahya  pu%''J'  parst^  Bh.4. 18;  — ksram  fräiiayam  . .  °na*  näm<^  pärsa*  . . avamsäm  ma'kiilam  akunavam  Bh.2.6;  6; —  kär^  Aya^  'naliyä  Bh.  2. 6,
Bed.  und  Et.7     Ob  gleich  ai.  vt^dirna-l
5686:•  j.  arä.va£ah-,  g.  «r3§.va£ah-  Adj.  'des Worte,  Sprüche  richtig,  die  rechten  sind, der  die  rechten  Sprüche  kennt':  dirä  vacim baraiti  mthahvacä  z-ä  *'M^>  va  "da  erhebt seine  Stimme  einer,  des  Sprüche  die rechten'',  oder  auch  einer,  des  Sprüche die  falschen  sind"  Y._^/.  12;  —  nsil  °ä('> sarfm  (sd.)  didqs  dnp^iltiJ  Y.49-9;  — mi^nm . .  "catahim  vyäxaimn  Yt.  JO.  7 ;  — mräm  ..  vacS  °(&(VS.)  ahura  maeda  Yt J.2;  —  iianm  asavamm  yS  at?hai  vais 'CS  (NS.)"  V.ji.  2;  —  naire  asaone  arl- manavia  (sd.)  *V<iwAa''  Y. //?,  17.
7912:aifihat  haca  vUat  .  ,  jamyqn  t'  (nämL aivhe  vfsi)  .  .  sfsnta  fravahyö  . .  iäse (sd.)  ..  Y.  6"o.3f.  a)  wesentlich  nur hervorhebend;  a)  hinter  der  Neg.:  näit  i' airyä  daiähitvS  frql  hyäi  haina  Yt&se; —  mäea  ts  i°  *spitama  .  .  P.  40;  — mäiJß  i'  ahurahe  .  .  va^äi  Jasaima  Yt. JO.69.  b)  hinter  Pron. :  hs  i' vyäxman- yeiti\tKis;  15;  —  AäUi'a  i°  .  .  htlu  V> ux'^.vacast3md  paitt.jasät  P.  Sjf.;    —
9367:Igibt,  Gesetze  vorschreibt':  mi^tTm  .  . 'zavAsm  tylxamm  Yt.  /o.  6 1 ;  —  *frazain-' tlm  °sqm  (ASf.)"'  vyäxanam  Y.  ^s.s,  F.5,
13393:•  j.  'dänav-  Adj.,  bezeichnet  einen  den  Ira- niern  feindlichen  i'Srischen  Volksstamm: tala  yöi  taxma  xstüvayS  'nubyS  az)n  p?sana yüz»tn  (näml.  /ravasayj)  tdm  taurvayata v>r?^r?m  'nunqtn  türanqm..t6al^3  'nunam türanqm  .  .  xrBma  asSbis  frasinta  (sd.) "nunqm  baivari.pailinqm  Yt-/J.  37f.;  — yat  baväma  aiwi.vanya  °nav3  (als  AP.) tära  vyäxana  Yt.  J.  73.
18684:—  apqm  napät>m  .  .  yS  nirSus  daha  yO n^rfu/^i  taiasa  Yt/5.  51; — ya>a  nars vay%an?m  "wie  der  Kopf  eines  Menschen" V.ö".a2;Äa3,F.jc,P.j4;  —  narqm  näiri- nqmca  .,  ti  hrmava  mti-viaire  djyammm Visp?m  3  afimät  yat  aSe  narS  "var^/iva anhm  V.2.27C;  —  cvaiti  narqm  ..xaota ratufris  N.  20;  —  yS  narS  kimSgatvS  . . anya  dva  vä  nara  , .  3at  aSsqm  narqm  .. cvat  antari  ^mr^us^'^  V.5.27;  4.i,ä,;- — yä  nara  (NS.)  gätum  baraite  F.^d;  N. 64;  —  paoifTtn  upa  may^m  frä.nasus (sA)  nartm  (statt  NS.)  bavaiti  V.  g. j8.  A)  Gegenüber  einem  attributiven a)  Substsl,  b)  Adj.  oder  c)  Proa  tritt nar-  vielfach  so  zurück ,  dass  wir  es  un- übersetzt  lassen  können;  es  gilt  das  ins- besondre vom  NS,  nä,  der  dabei  meist in  der  Stellung  der  Enklitika  —  hinter  dem ersten  Hochton  des  Satz-  oder  Versteils  — auftritt  a)9>  cvat  na"'^  3%rava  (sd.)  .  , *parayäl  ". ,  (ein  Mann,  der  Priester  ist, sva.)  ein  Priester  .  ."  N,  ^;  —  ydha  na taxmS  ra%a2stä  .  .  kaca  saltät  (sd.)  .  . paiti.ynUa  YtiJ.Sj.  b)  tts  nä  sayeiti (sd.)  vyäxanS  Yt  13.16;  53,  V.5. 40;  — paeiryeheca  na  myatdahe  aZaiit  (sd.)  .  . raius  , .  ratunafm  ayasnXm  (sd.)  daste  A. 3.  7;  8— 12*;  —  daxma  .  .  yahmya  nars irisla  nthayänte  V.3.Q;  Vd.  2',  17,  Vyt 12;  —  kva  narqm  iristanqm  tansm barama  V.  (j.  44;  —  kat  /a'(Sp,  612) nara  iristd  . ,  nasus  upaMvqsaiti  V,  7. 1;
24678:•  j.  *vyäxa-''  m.  'Versammlung':  avai •awm''  hanjamanimca  ..am?ianam  spmta- nqm  G.2.<y'>.
24680:—  Vgl.  vyäxana-,  vyäxman-.  —  ')  So  Mfj, El;  NA.  'xn'.  —  ")  eSt  s.  Y.  J/.  12.  — i)  S.  noch  zu  viyaxna-,  Sp.  1475.
24681:•  j.  vyaxana-  Adj.  (fem.  '«J-)  'in  der Versammlung  sprechend,  ihr  Rat  erteilend, beredt  (ayoySTrijf  und  ßo^k^^ipa?)' ;  a)  von Menschen:  us  nä  saya/i(&d.)  'nS  vysxmsku (sd.)  gasaya/.uxo0  Yt.  13.16;  —  narqm  .. stähyanqm  'nanqm  Ny.j.  10;  YL  l^.  53; —  danavS  türa  'na  Ytj.  73;  —  hulä»- hsm  *''/^m'^  .  .yaha  "urväx/aAe  Az.^;  — ariyeke  'nahe  Yt/J.  108;  —  ß-azainllm karls.räzqm  'nqm  Y.öz.y,  F.j;  —  Jra- santsis  ..  'nayä  Yt.  yj.  134.  b)  von Göttern:  3%rS  urvasUtahe  ..  'nahe  Yt, /J. 85;  —  mi^r)m  .  ,  tpasitn  taxmim  'mm karsB.raiatshim  'mm  Yl/o.öi;  7,  25;  — miknm  . .  ys  'nanqm  °nS  Ytio.  65;  — nairyö.sar»hB  °n5  Y .22.1  y, —  nairya  satiha 'na  V.  22.  7.
24682:Ableit.  —  Vgl.  *vyäxa-.  —  Pü. :  hanjamatük.
24684:•  j.  vyäxainya-  Adj.  'der  Versammlung Rat  erteilend,  sie  beratend':  väc5  ySt  .. iiyra  äs  'aine'l  (NPm.)  Jj  Yt  14.  46.
```


## [2026-10-16T05:14:01.279Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=23000 && NR<=24700 && /^ *14[0-9][0-9] .{0,60}14[0-9][0-9] *$/ {print NR\": \"$0}' BRT.txt; grep -n -E 'vaeg|vaēg|vaig-|vaej' BRT.txt | head"
}
```


### [2026-10-16T05:14:01.720Z] TOOL RESULT

```
23755: 1497  varazyant-  —  vöizda-  1428
24604: 1473  viSavä-  —  viS.haurva-  1474
17781:Komp.  mity>-*. fra-vaej'a-   Adj.
21325:•  j.,  g.  yavae-sü-  Adj.  (auch  mask.)  'immer- während Nutzen,  Vorteil  habend  sva. immer  gedeihend';  yat  karmavqn  frai?m ahBm   .  .  yavaejim    "sum    Yt  /p.  1 1 ;  —
21995:•  j.  vaejant-  Adj,,  PPA.:  s.  vaig-.
21996:•  j.  vaejah-  n.  mit  airyana-  Adj.  Name eines  Landes*':  'nim  °Jö\.i.  1; — paoirim asanhqm^a  , .  vahillfm  fm^wfrpsfm  azim yS  ahurS  mazda  .  .  'nsm  'jS  vavAuya daityayä  (sd.)  ".  .  AV.  der  guten  Däitya" V.  J.  2 ;  —  tarn  yatata  ahurö  mazdä  'yene *jahi  vanhuya  daityayä  Yt5.i7;  104, 15.2; —  yimS  .  .  srüC5  'yene  *'jahe  i'atfhuyil '' daityayä  V.2.20;  20;  —  srätd  'yene 'Ja he^^ tarn  zara>uiira  .  .  Y.5. 14;  *Yt  /.  21.
23764:—  ')  Vgl.  iSt.  y.  2p.  I,  wo  das  Rind  bitlel,  \      Zum  V.  vaig-.    —    Vgl.  vai^n-.    —    iBed.  s.
```


## [2026-10-16T05:14:05.776Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '•  ?j\\.?,?  (vaig|vaēg|vaeg)' BRT.txt | head; grep -n -E 'vaig-  ' BRT.txt | head -5"
}
```


### [2026-10-16T05:14:06.111Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:14:07.827Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'vaig' BRT.txt | head -20 | cut -c1-300"
}
```


### [2026-10-16T05:14:08.140Z] TOOL RESULT

```
21995:•  j.  vaejant-  Adj,,  PPA.:  s.  vaig-.
23296:'weilen,  sich  aufhalten':_yi7/a/flE'a/flra.- irihyeiti  kva  aitqm  (sd.)  xsapamm  havD urva  *varfAaitii''^  H.  2.  i;  —  paoiryqm xfapatum  havS  urva  vaigkaili  hüxte Vyt.  54.
23764:—  ')  Vgl.  iSt.  y.  2p.  I,  wo  das  Rind  bitlel,  \      Zum  V.  vaig-.    —    Vgl.  vai^n-.    —    iBed.  s.
```


## [2026-10-16T05:14:12.606Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^\\*?wa[iy][čcgǰj]|\\*wai[čcgǰ]|\\*waiǰ|\\*waič' CHEUNG.txt | head -20"
}
```


### [2026-10-16T05:14:13.130Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:14:15.921Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'āwēxtan|awextan|āwextan|bēxtan|bextan|angēxtan|hangēxtan|parwēzan|parvīzan|wēxtan|wexta' CHEUNG.txt | head -20"
}
```


### [2026-10-16T05:14:16.252Z] TOOL RESULT

```
26833:Pres.: IND. 3sg. ВМР wycyt /wézéd/, 3р1. BMP wycynd /wézénd/; Inf: BMP wyhtn /wextan/ || (+ *ui-) 
26857:*NWIR: NP bextan/bez- ‘to shake’, Bal. gé(h)t, gétk/géj- ‘to put, swing, turn towards;
```


## [2026-10-16T05:14:17.950Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 26790,26900p CHEUNG.txt"
}
```


### [2026-10-16T05:14:18.392Z] TOOL RESULT

```
(supplet. diay), Fariz. -vin- (supplet. di-), Yar. -vin- (supplet. di-), Gz. ven- (supplet. 
di-), Gur. -in-, (subj.) vin- (supplet. di-), Isfah. venän/ven-, Khuns. vin- (supplet. 
di-), Jow. ai:n- (supplet. bam-di), Meim. a-vin- (supplet. dian), Nn. vin- (supplet. 
di-), Natan. vin- (supplet. -di-), Semn. m-éin- (supplet. -di(&)-), Sang. vin- (supplet. 
-dia), Shamerz. vín- (supplet. bä-dimän), Siv. vin- (supplet. di-), Soi a-ün-, ä-ün- 
(supplet. di(d)-), Sorkh. vin- (supplet. boe-dian), Lasg. vin- (supplet. bae-di-) ‘to see’ 
*NEIR: Oss. I. wynyn/wynd, D. winun/wind, jinun/jind, Pash. win-, Sh. win-/wint, 
Khf. win-/wint, Rosh. wun-/wunt, Sanq. weyn-/wand, Ishk. wen-/wend-, Sangl. 
win-/wind-, Wa. win-/wind-, vin-/vind-, Yi. win- (supplet. lisC-), M. win- (supplet. 
lisk"-) Yghn. wen-/wéta ‘to see’ 

*SANSKRIT: ven- ‘to look for’ (RV+) = EWAia II: 582 

© This Пг. root is nominal in origin, from the noun *uai(H)na- ‘watch, survey(or)’, 
cf. Skt. vená- ‘watch’, YAv. vaena- ‘nose’, cf. Goto 1987: 298 for references. In 
many WIr. forms *uai(H)n is part of a suppletive system with *daiH!. 

«PIE *uei(H;)-no- ‘survey’ => LIV: 668 f., fn. 5 | Pok.: 1123 

*IE COGNATES: Lat. venari ‘to chase, hunt? 

*REFERENCES: КРЕ I: 139b f., 206b f., 245b f.; Ivanow 1926: 420; EVP: 87; KPF II: 199; Christensen, 
Contributions I: 162, 259; IFL II: 262a, 548; Christensen, Contributions II: 55 f. 114 f. 159; 
Abrahamian 1936: 133; Lambton 1938: 42a, 77b; Andreev — PeSéereva: 351b; MacKenzie 1966: 94; 


EVS: 90a; WIM I: 73; WIM II/1: 85; WIM III: 118 £; Abaev, Slovar’ IV: 117 f£; Paul 1998: 319a; 
Steblin-Kamenskij 1999: 389; Cabolov 2001: 199 


*uaij ‘to shake, swing’ 

*AVESTAN: YAv. vij- ‘to shake, swing ?' || (+ *fra-) YAv. frauuaeya- “swinging 
forward’ (Yt 10.96, Yt 10.132) || (+ *ni-) ‘to swing down(wards)’ = Liste: 54 

Partic.: pres. YAv. vaéjant- (? Yt 19.92, ? F 431), perf. pass. YAv. -niuuixta- (Yt 6.5) 

*MIDDLE PERSIAN: BMP wyc- /wéz-/ ‘to swing, fling, sprinkle’ || (+ *ui-) MMP 
whyz-, ВМР wyhyc- /wihéz-/ ‘to move, progress, set out’. 0 On the etymology of 
MMP whyz-, BMP wyhyc- see Nyberg 1974 II: 211b. The older etymology of 


Henning 1933: 178 has been rejected by Nyberg. > DMMPP: 342b 
Pres.: IND. 3sg. ВМР wycyt /wézéd/, 3р1. BMP wycynd /wézénd/; Inf: BMP wyhtn /wextan/ || (+ *ui-) 
Pres.: IND. 3sg. MMP whyzyd, 3р1. BMP wyhycynd /wihezend/ 


*PARTHIAN: (+ *ati-) 'dwyxs- ‘to shake (the head)’ > DMMPP: 25b 


414 *uaij 


(+ *ati-) Pres.: IND. 3pl. 'dwyxsynd {hapax} 

*SOGDIAN: BSogd. wyc, CSogd. wyc ‘to move, shake [intr.]’ || (+ *apa-) BSogd. 
pw’yc- ‘to shake, be agitated’ || (+ *a-) ? BSogd. ’’wys ‘to confuse, disorder’, 
CSogd. ’wyZ ‘to become agitated, angry’ || (+ *pati-) ptw’yc ‘to shake, be agitated’. 
© On CSogd. ’wyz "The etymological possibilities are numerous", Sims-Williams 
1984: 149. 

Pres.: IND. 3sg. BSogd. wyct, 3р1. BSogd. wycnt, CSogd. wycnt, SUBJ. 3sg. BSogd. wyc’t, Partic.: pres. 
BSogd. wyc’y || (+ *apa-) Pres.: SUBJ. 3sg. BSogd. pw’yc’t || (+ *ä-) Impf.: IND. 35р. CSogd. "wyZ 
Partic.: perf. pass. BSogd. "wystk ‘ksubdha’ 

*CHORESMIAN: ? wc- ‘to shake’ (rather from *ua(n)ë ?) = Samadi: 211 

*NWIR: NP bextan/bez- ‘to shake’, Bal. gé(h)t, gétk/géj- ‘to put, swing, turn towards; 
pour into; miscarry, abort’, Zaz. viziyayis/viz(iy)en- ‘to come out, appear’, Yar. 
vast, Isfah. vär-vezän/vär-vez-, Meim. a:-vaft-/a:re-vez-, Mah. wöstän, Natan. är- 
vast ‘to jump, leap’, ? Qohr. vut (pret. stem) “о hang, be suspended’ || (+ *a-) NP 
avextan/avez-, Meim. dar evidz-/dar a-vi:tai- ‘to hang, suspend [intr.]’, Khuns. 
aviz-/aviza ‘to hang on [tr.]’, (inch. ?) ? Kurd. (Kurm.) avasin/awas-, (Sor.) hał- 
awasin/awes- ‘to hang on’ (formally difficult) || 

*NEIR: Oss. I. wigyn/wygd, D. wegun/wigd ‘to shake; wave’, Sh. (Baj.) wuc-t ‘to 
move, stir, go (slowly), rock, swing, shake’, ? (Baj.) wuz-/wuzd ‘to move, stir’ || (+ 
*4-) Oss. I. awynzyn/awygd, D. awinzun/awigd ‘to hang’, ? Sh. avezun ‘to hang’ 
*MISC: ? Arm. (LW) vizem ‘I flow, miscarry’ 

*SANSKRIT: vej ‘to dart up or back, to move up (of a wave), flee, twitch, move 
quickly’ (RV, AV+) = EWAia II: 577 

Q The root is a blend of *yaité and *uaij! according to Nyberg 1974: 210; 
Sims-Williams 1989: 263. It should be noted though that we can distinguish two, 
sharply defined, meanings for an (apparently) single root, viz. ‘to move’ and ‘to 
shake, swing’. This is also found in Germanic: ‘to move’ and ‘to yield, give ground, 
weichen’ respectively. Although, obviously, it is possible that we may still deal with 
one and the same root, it is probably better to reconstruct two different 
(homonymous ?) roots. 

«PIE *ueig- ‘to (start to) swing, shake [vel am IT = LIV: 667 f. | Pok.: 1130 f. 

*IE COGNATES: Gr. eixo ‘I yield, give ground’ (with sec. -к-), OE wican ‘to yield, 
give ground’, ON víkja ‘to move, turn; respond, take action’, OHG wihhön ‘to jump, 
leap’, NHG weichen 

*REFERENCES: Christensen, Contributions I: 156, 255; Abrahamian 1936: 133; Lambton 1938: 40a f.; 


Abaev, Slovar’ I: 87 f., WIM I: 66; EVS: 87b, 96a; Abaev, Slovar’ IV: 108 Ё; Werba 1997: 376 Ё; Paul 
1998: 317b; Cabolov 2001: 98; Lecoq 2002: 656b; Shahbakhsh: s.v. géj- 


*uais 415 


*uaip ‘to swing, shake’ 

*AVESTAN: Y Av. vaep- (vif) ‘to engage in homosexual activities, be a passive’ || (+ 
*ара-) ‘to throw off (?)’ = Liste: 54
```


## [2026-10-16T05:14:22.928Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"sift|sieve|angext|hangext|hngyht|angēz|angez\" CHEUNG.txt | head -20"
}
```


### [2026-10-16T05:14:23.238Z] TOOL RESULT

```
3753:*IE COGNATES: Arm. k‘amem ‘I squeeze out, sieve’, Gr. étepev ‘milked, squeezed 
7275:angextan/angez- ‘to stir up, incite’ 
7280:angezun has a secondarily attached æn- (< (*ham-): if the prefixation was old, it 
7281:would have become I. **zngizyn, D. **angezun. Formally this secondary forma- 
9101:*IE COGNATES: OHG sihan ‘to sift’, OE séon ‘to flow away, to sift’, OCS sscati ‘to 
24288:*SANSKRIT: ? Pkt. chanana ‘sifting’, Khow. chonik ‘to shake down’, Hi. channä ‘to 
25557:*NEIR: ? Oss. I. (rarely) tigyn, D. tegun/tigd ‘to sieve (flour through a sieve)’, ? Wa. 
26452:*yait ‘to sift, select, elect, sort out, separate’ 
26454:*AVESTAN: YAv. vaec- ‘to select, sort out, sift? = Liste: 54 
26458:*MIDDLE PERSIAN: BMP wyc- /wéz-/ ‘to sift, select, elect, choose (etc.); separate’ 
26468:*SOGDIAN: (+ *uz-) CSogd. ZwyZ ‘to sift, winnow’ 
26472:*CHORESMIAN: (+ *pari-) P’rwYCY- ‘to sift (flour) = Samadi: 157 
26479:vitis, Awrom. wetáy/wec-, Abyan. veta/vej-, Gz. vēž-/vēt, Khuns. viz-/viza ‘to sift’, 
26480:Gur. (Kand.) vicä ‘sift !’, Bal. gecin, Kurd. beZing (Ё) ’sieve’, Khor. Боја, vim 
26481:‘weeding’ || (+ *pari-) NP parwez ‘sieve’, Zaz. pirozin (Ё) ‘(big) sieve’ 
26485:Sariq. parwey-/parwid, Yzgh. parwij-/parwoyd ‘to sow, to sift’, Wa. 
26486:porwic-/porwoyd (porwict) ‘to sift’, M. porwiZ-/porwöyd (Zarubin) ‘to sift’ 
26488:*MISC: (+ *pari-) Par. paric- ‘to shake a sieve’, Par. pari&ön, рагіёӣп ‘sieve’ 
26489:*SANSKRIT: vec ‘to sever, separate, winnow, sift? (RV+) = EWAia П: 576 
35225:hngycyn- /hangezen-/,
```


## [2026-10-16T05:14:25.980Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 26452,26500p CHEUNG.txt; echo ------; sed -n 7255,7300p CHEUNG.txt"
}
```


### [2026-10-16T05:14:26.298Z] TOOL RESULT

```
*yait ‘to sift, select, elect, sort out, separate’ 

*AVESTAN: YAv. vaec- ‘to select, sort out, sift? = Liste: 54 

Caus.: pres. IND. 3sg. YAv. *°vaécaiieiti (N 100) 

*MIDDLE PERSIAN: BMP wyc- /wéz-/ ‘to sift, select, elect, choose (etc.); separate’ 
(especially in Dk.) 

Pres.: IND. 3р1. BMP wycynd /wézénd/; Partic.: perf. pass. BMP wyht /wext/; Pass.: pres. IND. 1р1. BMP 
wycyhym /wezihem/ 

*PARTHIAN: wyx- ‘to elect’ = Ghilain: 94 | DMMPP: 360 

Partic.: perf. pass. мухі, "hwyxtg, (pl.) wyxtg’n ‘chosen’ 

*SOGDIAN: (+ *uz-) CSogd. ZwyZ ‘to sift, winnow’ 

Pres.: OPT. 3sg. CSogd. Zw.Zy 

*CHORESMIAN: (+ *pari-) P’rwYCY- ‘to sift (flour) = Samadi: 157 


408 *yaidl 


*NWIR: NP béxtan/béz-, Bal. giht, gitk, getk/gec-, Kurd. (Sor.) bézan/béz(é)-, Zaz. 
vitis, Awrom. wetáy/wec-, Abyan. veta/vej-, Gz. vēž-/vēt, Khuns. viz-/viza ‘to sift’, 
Gur. (Kand.) vicä ‘sift !’, Bal. gecin, Kurd. beZing (Ё) ’sieve’, Khor. Боја, vim 
‘weeding’ || (+ *pari-) NP parwez ‘sieve’, Zaz. pirozin (Ё) ‘(big) sieve’ 

*NEIR: Oss. I. wizyn/wygd, D. wezun/wigd ‘to reap, pick (grain, berries)’, Pash. 
winj- ‘to wash, cleanse’ || (+ *pari-) Sh. parwéj-/parwézd, Rosh. parwij-/parwizd, 
Sariq. parwey-/parwid, Yzgh. parwij-/parwoyd ‘to sow, to sift’, Wa. 
porwic-/porwoyd (porwict) ‘to sift’, M. porwiZ-/porwöyd (Zarubin) ‘to sift’ 

*MISC: (+ *pari-) Par. paric- ‘to shake a sieve’, Par. pari&ön, рагіёӣп ‘sieve’ 
*SANSKRIT: vec ‘to sever, separate, winnow, sift? (RV+) = EWAia П: 576 

9 This Ilr. root has no certain IE cognates. The comparison to the ‘consecration’ 
forms, Hitt. hu-e-ek-mi ‘I slaughter’, Goth. weihan, OHG wihen ‘to dedicate’, Lat. 
victima ‘sacrificial animal’ is semantically not compelling. The Ш. root has no 
particular religious significance and it is highly unlikely that only IIr. would have 
retained the presumably older (more profane) meaning of ‘to separate (from the 
rest), single out, etc.’. 


*PIE — => LIV: 670 | Pok.: 1128 

------
305 f.; EVS: 110a, 96a f., WIM II: 671; DKS: 90b; Vahman — Asatrian 1987: 89; Lecoq 2002: 576b, 
594a, 616b 


*gaiz ? *to disturb, stir, incite, excite ?' 

*MIDDLE PERSIAN: (+ *ni-) BMP nkyc- /nigez-/ ‘to expound’ || (+ *ham-) BMP 
hngyc- /hangéz-/ ‘to arouse, stimulate, stir up’, BMP hngycyn- /hangézén-/ (sec. 
caus.) ‘to resuscitate’ 

(+ *ni-) Pres.: IND. 3sg. BMP nkycyt /nigézéd/; Inf.: BMP nkyhtn /nigextan/ || (+ *ham-) Pres.: IND. 3pl. 
BMP hngycynd /hangézénd/; Caus.: IND. 3sg. BMP hngycynyt /hangézénéd/ 


*SOGDIAN: (+ *ham-) ? BSogd. ’nyyznykh ‘emetic, un (remède) excitant 
(Benveniste, TPS: 232 ad 5). Š This technical term is found in a medical Buddhist 
text twice (P 19.5, P 19.11). 

*NWIR: NP gej, Kurd. gEZ confused, astonished’ (with suff.) Bakht. gez ‘mad’, ? 
Meim. darem gianä/dar a-gizn- ‘to clear, explain, elucidate’ || (+ *ham-) NP 
angextan/angez- ‘to stir up, incite’ 

*NEIR: Oss. І. qyzyn/qyzt, D. gizun/gizt ‘to threaten; to behave hostile, be male- 
volent; to start to rain’ || (+ *ham-) Oss. I. ænqizyn/ænqyzt, D. engezun/engizt ‘to 
be in a state of fermentation; to ferment’ (sec. prefixation). 0 Oss. I. angizyn, D. 
angezun has a secondarily attached æn- (< (*ham-): if the prefixation was old, it 
would have become I. **zngizyn, D. **angezun. Formally this secondary forma- 
tion would derive from the "simplex" I. qyzyn, D. £izun, whose meanings are dif- 
ficult to reconcile with I. engizyn, D. aengezun. The only way to do so would be if 
we start from an older meaning such as *‘to disturb, be stirring’, which could have 
developed into either *‘to cause disturbance, stir up trouble, strife’ (whence ‘to act 
in a hostile, malevolent way’) or it could have referred to the weather, cf. Engl. 
storm (cognate with to stir). 

*PIE ? 0 Apparently quoting from Lidén KZ 61: 1ff., Pokorny, l.c. only mentions the 
Oss. verbs as Ir. cognates, which would go back to an IE root *geig- 'stechen, 
beißen’. Not only is the reconstruction *geig-, with two unaspirated voiced stops, 
phonologically impossible for PIE, also the inclusion of the Oss. forms can be 


98 *gaml 


doubted, if their meanings have risen only secondarily. Considering the other Iranian 
cognates of the Oss. forms, we have to rule out any relationship with the IE forms 
cited by Pokorny as cognates: Arm. kcanem ‘to bite, sting’, kc-u ‘bitter, rancid’,
```


## [2026-10-16T05:14:34.173Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'hangēxt|hangext|hngyhtn|hangēz|hangez' PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head; grep -n -i -E 'āvang|avang|âvang|āwang|ävang|ävextan|äwextan|āvēxtan|avextan|angextan|angextan|ängextan|angexian|bextan|bēxtan|parvezan|parwezan|parvëzan' HRN.txt HUB.txt | head -20"
}
```


### [2026-10-16T05:14:34.698Z] TOOL RESULT

```
PHD.txt:394:handāxtan, handāz- [hnd@htn', hnd?c- | M hnd?c-, № an~] plan, allot, reckon, judge. ~išn: judgement. handāxtār [%nd”%t”[] planner. handāz-, ~išn, v. handaxtan. ~ag [hnd?ck! | N andáza] measure, manner; ~ 1: like. handēmān [hndym’n' | = M] before, in the presence of. ~th: audience, presence. handēmānģar [kndym’ nkl] introducer (into the presence). „lt: introduction. handéSidan, handēš- [Ahndyti-ytn! | M hndy§-, N an~] think, consider, reflect. išn: thought, reflection. handēšīdār [hndyfyt?I] thoughtful. handēxtan, handēz- [hndwhtn', hndwc- | N an~] gain, acquire, amass. „-išn(īh): acquisition. handraxtag [hndl htk! | P ?ndrxt] oppressed. ~ih: oppression, suffering. handüdan, *handāy- [hndwtn' | (M ?nwd), N an~] smear, plaster, anoint. hangad [hngt! | P ?ngd] fortunate, rich. ~ih: fortune, wealth. hangām [hng’m | N ~] time, occasion. ~ig [-yk!] timely. hangarag [hng’lk' | N angara] reckoning. hangardan, hangàr- [hng’l-tn' | M hng^r-, N an~] consider, reckon. ~išn: consideration. hang��xtan, hangéz- [hngyhtn', hngyc- | (M hgjyn-), N an~] arouse, stimulate, stir up. ~išn: arousing. hangirdénidan, hangirdén- [hngityn-ytn'] complete, summarize. hangirdig [kngltyk'] complete, perfect; summary. ~ih: completion, summary. hangdSidag [hngw£ytk! | M ”ngwšydg] way, manner, likeness. ~ 1: like. hanģrāyīdan [hngl’dytn'] lament. hangrüdag [hnglwtk'] lamenting. hanj-, v. hixtan. hanjaftan [hncptn' | P hnjft, (M hnzpt)] be finished. hanjāftan, hanjām- [hnc’tn', hnm- | P hnj ft, hnjm-, (M hnzpt, N anjāmīdan)] finish, complete, carry out. hanjām [kne m | N anjám] end, completion, outcome. hanjaman [hncmn! | (P ?njmn, M hnzmn), N anjuman] gathering, assembly, congregation, community. ~ig [-yk'] (notable) member of the community. hanjīdan [hnc-ytn' | N ~] = hixtan.
PHD.txt:842:arousing hangēzišn.
NYB_vol2_glossary.txt:1906:hangaxtär [hng’ht’l] instigator: anäkeh ~, of Ahriman 679%, — For hangextär
NYB_vol2_glossary.txt:1907:with the change of preconsonantic -éh-, -&x- to -ah-, -ax- often observed in MiPrs, cf s. v. mahmäneh. From hangéxtan hangez- ‘to exite, to provoke, to rouse’ (vat hangēžēt [hngyeyt'] ‘provokes flatulence’ GF II, 31); NP angextan, angézidan; Paz. husazihed wrong transliteration of han- gēžihēt ‘is produced, excited’ (SGV VII, 18. XVI, 32). Hence
PHD_mackenzie.txt:2826:hangextan, hangez- [hngyhtn', hngyc- I (M hgjyn-), Nan......] arouse,
PHD_mackenzie.txt:5957:anger debahr, x~sm.                       arouse guhriiyenidan, hangextan.
PHD_mackenzie.txt:5958:angry x~smen.                             arousing hangezisn.
PHD_mackenzie.txt:7673:spirit menog(ih), wad, waxs; --s       stimulate hangextan.
PHD_mackenzie.txt:7676:    waxSig.                            stir up hangextan.
PHD_mackenzie.txt:11907:awestwar                ~\tf.1t ...        hangextan                  ,,~,...
HUB.txt:248:fiir ahinjidan stehen^) wie avangan der Wb. fiir dvin-
HUB.txt:4792:zu avextan 'hUngen' ; azang Talte* zu cin *Falte' von Wrzl. c7,
HUB.txt:5813:r: avaz 'Stimme', siehe Horn Nr. 54; avextan 'hangen' H.
HUB.txt:5817:H. 262; bSva Wittwe H. 268; parvezan *Sieb' H. 249; paroar
```


## [2026-10-16T05:14:46.957Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'Wittwe|Sieb|hängen|hangen|aufregen|erregen' HRN.txt | head -20; sed -n 5805,5820p HUB.txt"
}
```


### [2026-10-16T05:14:47.293Z] TOOL RESULT

```
926:56. ävey(ten 'hängen, aufhängen', Praes. avez-em^ ät^ezis^
927:vergl. avenffy ävingän 'hängend'^).
928:phlv. ave/fan 'hängen , Mit7']avec (Gemme, ZDMG. 18
930:oss. d. awinjiü}, t. avinjin 'hängen' (6); kurd. hil]avistw,
931:hal]avism (H.-Sch.) aufhängen'.
965:sie gefangen und ai. i^sanj- *hängen* passen nicht, doch
2555:249. hellten sieben', Praes. bez-em^ beziden^) ; perv&zen 'Sieb*.
2557:oder Worfeln aussondern'; päz. veytan sieben'.
2558:kurd. bltin 'sieben', bezink 'Sieb'; bei. gecag sieben',
2559:gecin, n. gesin *Sieb' (112); wa;K. farax-biz, Qar.faraq-
2560:beiz 'Sieb'.
2651:263. beve Wittwe'.
2653:ai. vidhdvä' *Wittwe'; phlv. vepak d. i. vBvak; lat.
2655:oss. t. idäj *Wittwe' (aus *vidüä'j), von Stackel-
6397:aw. l^sraes- , sraesyeiti 'sich an etwas hängen ;
6993:wo es mit menis verbunden ist und 'Übelkeit erregen
8301:anhangen, gerinnen* (Hübschmann, No. 184), sowie
9496:\A098. lieft 'sieben, hefte Woche'.
9497:aw. haptn 'sieben*; phlv. haß; ai. saptd; arm.
9508:l/llOO. heftäd ^siebzig.
arbeit*, vansldan u. s. w., zd. varez- : vireb curvus' = arm.
vrep *torto, perverso'. Unter diesen Worlen mogen alter-
thumliche und dialektische Formen (z. B. vaj, vgl. vaty vat-
gar, vatam^) bei Vullers II, p. 1402) enthalten sein; bei
den iibrigen hat sich das halbvokalische (sonantische) v
unter unbekannten Bedingungen ebenso erhalten wie in den
§ 39, b genannten Wortern das sonantische y.
§ 56. Im Inlaut bleibt ap. v als v nach Vokalen und
r: avaz 'Stimme', siehe Horn Nr. 54; avextan 'hangen' H.
^) Die Wrzl. vac 'sprechen' ist iranisoh-medisoh, nicht persisoh,
8. oben p. 116, Anm. 2.— 165 —
56; bavar *Qlsiuhe\ paz.vdwar^ arm. vaver; 6e/;ar 'zelmtausend'
H. 262; bSva Wittwe H. 268; parvezan *Sieb' H. 249; paroar
*Stair H. 304: parvus: 'Flug' H. 305; parvez *siegreich' H.
307; Pahlav 'Parthien' --=^ ap. Pardava-; fadarv Tasan' H.
379, oben p. 47; tuvan Sermogend' H. 401; javecl Wig
```


## [2026-10-16T05:14:51.465Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 920,940p HRN.txt; echo ---; sed -n 2550,2562p HRN.txt; echo ---; sed -n 2648,2660p HRN.txt; grep -n -E '^1?[0-9]+\\. (ang|eng|hang)' HRN.txt | head; grep -n -i -E 'ang.(x|y)tan|ange?zid' HRN.txt | head"
}
```


### [2026-10-16T05:14:51.885Z] TOOL RESULT

```
>j Mittlerweile auch KZ. 32, 578, No. 3; vergl. auch F. Solmsen ,
KZ. 31, 472.- 14 -
Aussprache : äivtirden), Praes. äwerem^ är-em^ ätrertden ;
jüd.-pers. Bibelübersetzung: pTI2X neben TIIN.
ap. *^+|/6ar-; päz. äwardan, ätvurdan, äivar-am,
beL (LW. ?) ärag, n. aray, awarta (14).
56. ävey(ten 'hängen, aufhängen', Praes. avez-em^ ät^ezis^
vergl. avenffy ävingän 'hängend'^).
phlv. ave/fan 'hängen , Mit7']avec (Gemme, ZDMG. 18
No. 54 (IV) --- Paris, No. 1349).
oss. d. awinjiü}, t. avinjin 'hängen' (6); kurd. hil]avistw,
hal]avism (H.-Sch.) aufhängen'.
Nöldeke (mündliche Mitteilung) meint, dass sich
eine Anknüpfung an ai. V^vij-, vijdte wohl durch eine
anzunehmende Zwischenbedeutung 'bummeln' vermitteln
lasse. Die von Fr. Müller (WZKM. 5, 184) verglichene
altslavische Wurzel stimmt lautlich nicht zu den
iranischen Formen.
57. ähen 'Eisen'; ähemn 'eisern 2).
Semn. ösün; g. vuhen,
phlv. äsm (z. B. vd. 5, 121), ämtm 'eisern*.
---
(vergl. Geldner, KZ. 28, 258, Bartholomae, KZ. 29,
297).
Ob np. hiyähan überhaupt etymologisch ohne Wasser
bedeutet, ist sehr zweifelhaft; Sahn. I, 109 Vers 876
u. ö. wird es ganz allgemein für 'Ebene' gebraucht.
249. hellten sieben', Praes. bez-em^ beziden^) ; perv&zen 'Sieb*.
ai. l/'vec-, vindkti^ vivekti (Imal) 'durch Schwingen
oder Worfeln aussondern'; päz. veytan sieben'.
kurd. bltin 'sieben', bezink 'Sieb'; bei. gecag sieben',
gecin, n. gesin *Sieb' (112); wa;K. farax-biz, Qar.faraq-
beiz 'Sieb'.
250. -öejSJ, ' bezeHp - vez^ -vezen in bädbez 'Fächer'.
(sSv, \/vtfc3r LÄ vijati, vijate 'befächeln', vyajana-
---
262. bever 'tausend'.
äw. ba^vare 'tausend'; phlv. bevar.
oss. d. beurä, t. birä Viel, sehr, lange (61).
263. beve Wittwe'.
Käs. vJgd^ vU (neben bivä^ bwe),
ai. vidhdvä' *Wittwe'; phlv. vepak d. i. vBvak; lat.
oidiia; got. viduvö,
oss. t. idäj *Wittwe' (aus *vidüä'j), von Stackel-
be rg (briefliche Mitteilung).
264. beyoj^beyök 'Braut*, :V2 (Jer. 16, 9).
ai. <^ergl. vadhü- 'Braut' ; kurd. buk.
P.
265. />flcZ 'Schützer, gewaltig ^).
1484:124. engehtn (AM.), enguhln *Honig, vergl. terenguhin,
1524:125. enguM Tinger, Zehe'; vergl. etigustetl 'Ring'^
1536:127. engeiten antreiben', Praes. engez-em,
10086:15. angöSttak *Art und Weise' (Men., Bund., ZPGl.).
1537:phlv. angfytan antreiben', angejet (AV.), vergl.
```


## [2026-10-16T05:14:55.373Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1530,1560p HRN.txt"
}
```


### [2026-10-16T05:14:55.713Z] TOOL RESULT

```
(LW.), t. ängursf (26); af/. güta; wa/. yangl, minj.
augar, §iyn. angast, sar. ingä/t, sangl. ingit.
Dialektisch findet sich Kä§. engxdt, mäz. e)igel^
vergl. skr. atlgün-, angüli- Tinger, Zehe'.
126. efiffist 'Kohle'.
Vergl. skr. angärä- 'Kohle'.
127. engeiten antreiben', Praes. engez-em,
phlv. angfytan antreiben', angejet (AV.), vergl.
ham]vB/t (Geiger, Yätk. Zar., Anni. 52); skr. vgl.
samvignu' 'aufgeregt'.
vergl. oss. d. ve^^nn^ t. viyin erschüttern, bewegen'
(80), bei. gejag n. ge^cig 'schwingen, schleudern,
schlagen' (113).
128. enose 'glücklich, heil!', vergl. hös, nöse, nösin,^)
aw. anaosa- unsterblich'; phlv. anöäak unvergäng-
lich', arm. LW. antcsak, anois,
oss. ämisoriy änusi 'unvergänglich' (119); nicht bei.
anJmy 'Schicksal' (2) (Hübschmann, ZDMG. 44, 555).
129. ö er, jener, Plur. ösän (dialektisch, Lumsden, Per-
sische Grammatik, II, 76 Anm.; vergl. gel. üsüfi,
ühan),
ap. aw. ava- jener'; päz. ö.
Vergl, kurd. ätr, atve jener, er'.
130. o- (Praefix), u-,
aw. ava 'herab, von weg'; phlv. ö; ai. dva.
131. ewam, awam 'Schuld', loam,
phlv. äpäm (PPGL).
bei. LW. warn (288).
^) Aw. *angu8tapäna' (vergl. aw. ranapäna-)'^ oss. d. LW.
ängurstevän.
*) Der Wechsel von st und st ist häufig.
```


## [2026-10-16T05:15:01.160Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for r in BQT:67 BQT:333 BQT:178; do timeout 120 python3 tools/ref_page.py $r 2>&1 | head -c 2500; echo; echo =====; done"
}
```


### [2026-10-16T05:15:01.492Z] TOOL RESULT

```
Exit code 1
no scan of BQT covers printed page 67 (see 'scans' in refs_online.json)

(eval):1: ==== not found
```


## [2026-10-16T05:15:06.053Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'آویختن|آونگ' BQT_v1_pages.txt | head; grep -n -E '^\\[pdf page' BQT_v1_pages.txt | head -3; python3 -c \"\nimport json;print(json.load(open('../refs_online.json'))['BQT'].get('page_offset'))\""
}
```


### [2026-10-16T05:15:06.408Z] TOOL RESULT

```
8554:۰ آگیبیفی - و آکیشبدن بممنی آویختن و پیچیدن . رك : کش .۲ ۰ وا
9028:آون *- بروزن اون ؛ مخخفآونگت
9067:است که از آویختن‌باشد ۸ - چه در فارسی جیم
15160:؟ ركذ : آونگ .
20027:چسبند (۱) ودرهم آویزند ‏ و امر بدر آویختن
23368:باشنك - بروزنآونگ , خوشه کوچكث
24840:کربای » بمه‌نی دز هم آویختن و نلاش کردن
25932:و موافق ساختن باشد - و بمعنی درآویختن -
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
```


## [2026-10-16T05:15:08.951Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 9020,9075p BQT_v1_pages.txt; grep -n 'pdf page' BQT_v1_pages.txt | awk -F: '$1<9075' | tail -2"
}
```


### [2026-10-16T05:15:09.523Z] TOOL RESULT

```
آمده ات ۵
آوده- تح رایع و سکون ها ۰
اودی ح بر وزن باوری . صاحب
یقین و تحفق را" گونند . چه اور دمعتی تحقیق
و شین است ۹ ۰
| و شن س بکسر شین‌قطه داروسکون
نون » کاكوتي را کوبند ۷ و آن کیاهیست
که بعربی«سمتربری» خوانند ۵ .
آون *- بروزن اون ؛ مخخفآونگت
است که آویشنه و آویزان شده باشد .
او ند - بروزن ایند . رسمانی را
گوبند که خوشه های انگور از آن باویزند
کامروز همچوجهل هنرزشت و آوراست
عصری « لفت‌نامه »
الاوارحه ۰ من کب اصحاب الدواوین
۱
آوردن .
آروند و آورند .
۵ رکه :
ندارد بکسکینه وداوری . اپوشکور-
- رکه : آویشن .
سمتراست . «لغت نامه * .
آوشن9
و لنگی و جامه و غیره بر زبرآن اندازند - و
حجت و دلیل و برهاترا بیز کویند ۱ -و بمعنی
سابر ظروف و اوانی باشد همچو کاسه و کوزمو
امثال آن وبعربی «وعا» گوبند ۴ - و تخت‌وهسند
راهم گفته اند ۴ - و بمعنی شطرنج باشد و آن
بازیی است مشپور - و بمعنی اول و نضت هم
هست و باین معنی بکسر ثالث هم گفته اند .
و فدی ه بروزن رامندی , ظرف یکه
شواب درآن کنند .
و فگه ۴ - بسکون تون وکاف فارسی »
بمعتی رسمانی باشد که رخت بر آن انداژنه
و خوشه ای انگور نیز از آن آویزند- و حر
چیز آوشته را نیز گویتد.
آو نگان ۲ بروزن افرمان, آوشتن
و اوشته شده و آووان را گونتد..
٩‏ چنین کنت با پهلوان زال زر
رکه : آبه .
نامه» .
]وه - بنتح اك وطهور حا؛ بمعی ۰
ووای‌وافوس باشد ۵ وباخقای‌ها» نلم شهرست
ترديك بساوه ۱ - و کوره و داش خشت پزیرا
هم کفته اند - و بر آورتده صدا و ندا ماشك ب
و زنجیره را نیز گوبند که نقاشان و دوزندکان
ا وج 2۲ باجم. بروزن و معنی آویز
است که از آویختن‌باشد ۸ - چه در فارسی جیم
ابجد بزای هوز و برعکس تبدبل می‌بابد 4 .9
]ویر گان - با زاو کاف فارسی بر
وزن فالیز بان , خواص - و دلبران و مسشوقان
را گویند .
) و یز گن ‏ بسکون زای حوز و کس
کاف فارسی و نون ساکن . کدای مبرم وابرام
فتتنهترا گونتا .
۴۳ ک ۷ آوشتن واوئد ,
```


## [2026-10-16T05:15:14.073Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 9076,9140p BQT_v1_pages.txt | grep -n -E '[a-z]{3,}|آونگ|آویختن|آویز' | head -30"
}
```


### [2026-10-16T05:15:14.379Z] TOOL RESULT

```
8:فُردوسی * لفت ناعه *.آویزه وروت
```


## [2026-10-16T05:15:17.557Z] TOOL CALL #30: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-16T05:15:17.613Z] TOOL RESULT

```

```


## [2026-10-16T05:15:19.578Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/آونگ",
 "prompt": "Give the Persian etymology section verbatim."
}
```


## [2026-10-16T05:15:20.162Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/انگیختن",
 "prompt": "Give the Persian etymology section verbatim."
}
```


## [2026-10-16T05:15:20.965Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/بیوه",
 "prompt": "Give the Persian etymology section verbatim."
}
```


## [2026-10-16T05:15:21.338Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/آویختن",
 "prompt": "Give the Persian etymology section verbatim."
}
```


### [2026-10-16T05:15:24.046Z] TOOL RESULT

```
Based on the web page content provided, there is no Persian etymology section present. The page contains a "Pronunciation" section and a "Noun" section, but no etymology section is included in the material shared.
```


### [2026-10-16T05:15:24.804Z] TOOL RESULT

```
I've reviewed the webpage content provided, but there is **no Persian etymology section** present in this Wiktionary entry for انگیختن (angēxtan/angixtan).

The page contains:
- Pronunciation information
- Verb definition and meanings
- Extensive conjugation tables for literary Iranian Persian and colloquial Tehrani dialects

However, an etymology section—which would typically explain the word's origin and historical development—is not included in the material you've shared.
```


### [2026-10-16T05:15:25.072Z] TOOL RESULT

```
# Persian Etymology

The etymology section states that بیوه comes "From [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") (wēwag, 'widow'), from [Proto-Iranian](https://en.wikipedia.org/wiki/Proto-Iranian_language "w:Proto-Iranian language") *HwidáwaH, from [Proto-Indo-Iranian](https://en.wikipedia.org/wiki/Proto-Indo-Iranian_language "w:Proto-Indo-Iranian language") *HwidʰáwaH, from [Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language "w:Proto-Indo-European language") *h₁widʰéwh₂."

The word derives from the Proto-Indo-European root meaning "to separate." The section also lists cognates across multiple language families, including Kurdish, Ossetian, Sanskrit, Latin, English (widow), and Old Church Slavonic forms.
```


### [2026-10-16T05:15:25.432Z] TOOL RESULT

```
# Persian Etymology Section

The Persian etymology section states:

"From [Proto-Iranian](https://en.wikipedia.org/wiki/Proto-Iranian_language "w:Proto-Iranian language") _[\*wayǰ-](/w/index.php?title=Reconstruction:Proto-Iranian/way%C7%B0-&action=edit&redlink=1 "Reconstruction:Proto-Iranian/wayǰ- (page does not exist)")_, from [Proto-Indo-European](https://en.wikipedia.org/wiki/Proto-Indo-European_language "w:Proto-Indo-European language") _[\*weyg-](/wiki/Reconstruction:Proto-Indo-European/weyg- "Reconstruction:Proto-Indo-European/weyg-")_."

The word آویختن traces back through Proto-Iranian *wayǰ- to the Proto-Indo-European root *weyg-.
```


## [2026-10-16T05:15:30.402Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/آونگ",
 "prompt": "Quote the Mo'in entry for آونگ verbatim, including any etymology (Pahlavi/Avestan forms) given."
}
```


## [2026-10-16T05:15:31.029Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/بیختن",
 "prompt": "Quote the Mo'in entry for بیختن verbatim, including any etymology (Pahlavi forms) given."
}
```


### [2026-10-16T05:15:34.659Z] TOOL RESULT

```
# Mo'in Dictionary Entry for بیختن

According to the Mo'in Dictionary (Farhang-e Entesharat-e Mo'in), the entry reads:

"(تَ) \[ په . \] (مص م .) 1 - الک کردن ، 2 - غربال کردن ."

This shows the word has a Pahlavi etymology (indicated by په), is a verbal noun (مص م), and carries two meanings: sifting/winnowing and straining/sieving.
```


### [2026-10-16T05:15:37.717Z] TOOL RESULT

```
# Mo'in Dictionary Entry for آونگ

According to the Mo'in Dictionary (Farhang-e Entesharat-e Mo'in) shown on this page, the entry states:

"(وَ) ( اِ.) 1 - ریسمانی که خوشه های انگور و دیگر میوه ها را به آن می بندند و از سقف می آویزند تا فاسد نشود. 2 - هر چیز آویخته ، معلق . 3 - جسم سنگینی که گرد محور ثابتی حرکت کند، مانند پاندول ساعت"

This entry provides three definitions: (1) a rope for hanging grape bunches and other fruits from the ceiling to prevent spoilage; (2) anything suspended or hanging; and (3) a heavy body moving around a fixed axis, like a clock pendulum. However, no Pahlavi or Avestan etymological forms are included in the displayed content.
```


## [2026-10-16T05:15:43.719Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ *(4[01][0-9]|417)\\b' SOD_pages.txt | head -3; grep -n -E '\\bwy[cč]\\b|wyc ' SOD.txt | head -8; grep -n -i -E '^(WIDOW|WICKER|WEEK|WEAK|VICE|DIVIDE)\\b' SKT.txt | head; grep -n -i -E 'widdewa|widhewa|^ *weidh|u̯eidh' IEC.txt | head -5; grep -n -i -E 'vidhava|viduus|widuwo' incoming/WLD/WLD_Bd1_pages.txt | head -5"
}
```


### [2026-10-16T05:15:44.201Z] TOOL RESULT

```
4877:       416; MDii; Frag. Len.; Gersh. Amber. 176;                       az Oy, *y) ©<*a/w-zi; Parth. Wz ©3sg. prct.
4922:                                                                          412 Vyt'y   y Vytk
4925:400 Vt-      B                                        ^Ij.jJ^
13094:864  Jkwyc  =»  'k'we- 
13926:andoxc  ^ntwyc 
15044:1133  ^t'wyc   B  ^"jxl 
15045:andoxc   =>pw  'n^wyc*  mdwxc,  'ntwyc 
15140:1148  >ntwyc   B,  S  ^  «jjul 
15141:andoxc   ©ob.  -y   ^'nt'wyc,  }ntwxc,  >ndwxc 
15172:'nt'wyc 
20677:1981  Vswc  =»  ^swyc 
5206:DIVIDE.
5232:Divide.  (L.>  U  dimiJtrt,  lo  ifiitf% wparate  (pp.  dMUinu).^ls.di-  {f^»\  Sf«t|
18995:weak  verb,  closely  allie*!  to  A.S.
20842:vice-gerent.  (F.  —  L.)  F,  vicegermt, a  deputy;  Cot.  —  I*  uici,  in  place  of; gertni',  stem  of  pres.  pt.  oinrtre.  to  carry un,  rule ;  see  Oesture.  %  So  also  viie- admiral,  vitt-roy  (from  F.  rci,  L.  rtgem, Iting),  vite-regai,
20845:Vice  (I),  a  fault.  (F.  -  L.)  F.  vitt.  - 1*  Milium,  blemuJi.  fault.  D«r.  vic'i-tmi, F.  vicitux,  L.  uitifirus,  faulty;  viti-it/t, from  pp.  of  L.  uitiartt  to  injur«.
20849:Vice-gerent :  sec  Vicar.
21254:Weak.  CScand.>  The  Soud,  U ousted  M.  E.  wock,  A.  S. Weak  is  from  Icel.  tteikr,  Swd weak  ;  Dan.  veg.  pliant.  —  Iccl  rtii,  [« of  vlkja,  to  turn  a»ide ;  coKnale  vilk  A.  S Wiic,  pt.  t.  of  ttr/can,  to  give  vay.  (tei WIK.)    Allied  to  Wiok(i}s»dWlofe«
21290:Week.  (E.)  M.E.  wtkt,  wikt;  A.  S. wiee,  smVu,  a  week.  (There  was  a  later A.  S.  wum,  a  week,  which  became  M.  £. tpoutt,  a  week,  and  ii  obsolete.)  4*  Do. wtik,  Iccl,  vika,  Swed.  vtcka,  O.  H.  G. •UHcha,  TtvAAa  (.mod.  G.  tooche).  We  also once  find  Goth,  wiko,  in  the  sense  of  order or  succession  (Luke  i.  8),  aniiwering  to  L. erdiiu  (not  to  »fW>).  The  orig.  sense Kcems  to  have  been  '  succession,*  series  ;  cf. Icel.  vikja,  to  torn,  return  ;  see  Wook.
21448:Wicker,  made  of  twigs.  (E.  tfr  Scand.) M.  E.  wiktr,  a  pliant  twig,  properly  a  sb. —  A.S.  wic-en,  pp.  of  wuan.  to  give  way, bend,  ply  ;  see  Weak,  -f  Dan.  dial.  z>igref a  phant  lod,  allied  to  Dan.  veg,  pliant, weak ;  Swcd.  dial,  evidnr,  vtAker,  willow, from  Swcd.  vekiL,  to  bend,  ply.  See wit-chelxn  (below).
21453:Widow.  (£.)  H.  E.  vHdewt ;  A.  S. widwt,  •widuwe.  +  Do.  wtditxvt,  G.  toiitwCf Goth,  widuwa.  Further  allied  to  L.  uidua, fern,  of  uiduuj,  bereft  of,  deprived  of;  V>\ gw^iidw,  Kuss.  tfdoTKt,  Skt.  vidhavd,  a widow.  The  root  seems  to  be  WIDH.  as in  Skt.  vidA,  to  lack  (St.  Pctcrsbnrg  Diet, vi.  1070^  %  The  supposed  etymology  of Skt.  tnakavd  (from  vi,  without,  dhava,  a bust>«jid)  it  disproved  by  alt  the  cognate forms.  Sec  Void.  Der.  widow-er,  M.  E. mi^extftr,  coined  from  vndow  by  adding  -tr ; $0  mUq  G.  Ufft/wtr*
22296:heiratete Frau“, viduus „beraubt, leer von etwas“, air. fedb ,.Witwe‘\ corn.
```


## [2026-10-16T05:15:50.073Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ *[0-9]{4,5} +wyc\\b|wyc +B|wyc *[=>]' SOD.txt | head; grep -n -E 'shake|stir' SOD.txt | grep -i -E 'wy' | head -8; grep -n -E 'Vice versa|vice versa' SKT.txt | head -2; grep -n -E 'Page\\(s\\)|^.{0,40}vice versa' incoming/WLD/WLD_Bd1_pages.txt | head -0; grep -n -E 'u̯eig|ueig|vaēg|vaeg' incoming/WLD/WLD_Bd1_pages.txt | head -5"
}
```


### [2026-10-16T05:15:52.015Z] TOOL RESULT

```
13094:864  Jkwyc  =»  'k'we- 
15044:1133  ^t'wyc   B  ^"jxl 
15140:1148  >ntwyc   B,  S  ^  «jjul 
45533:5649  mys  pwyc  =»  mys  Pwyyc 
68392:8959  srywyc  B  >j>^ 
77754:10300  wyc'ytk   B,  M  jUla  <Ub 
77762:10301  wyc'yty   B  =»  wyc>ytk,  wyc'wyt'k 
77771:10303  wyc'wyt^w'k  =4  wyc'wytWk 
77786:10305  wyc'wytNv'k   B  j^^jx^JLi* 
77793:10306  wyc'wytk  *=»  wyc'wyt'k 
4216: auch kuuni zu dra-rgfipco nach Biugmann Festgabe fur Ivaegi 29 ff
9453:Hiervon abgeleitet ist *aiganun altn. eigna, -acla „zueignen“; ags. dgnian
21592:                                                 ueik-      — ueik-, ueig-                                        233
21654:234                                                                                             ueik-, ueig-
21755:                                                                    neik-, ueig-                                                        235
```


## [2026-10-16T05:15:59.619Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 77700,77753p SOD.txt | grep -n -E '^ *[0-9]{5}|shake|stir|move' | head -20; awk 'NR>=21592 && NR<=21760' incoming/WLD/WLD_Bd1_pages.txt | grep -n -E 'vaēg|vaeg|vextan|vēxtan|Woche|weak|veikr|vyāx|vyax|vicis' | head; grep -n -E 'u̯idhéu|uidheu|Witwe' incoming/WLD/WLD_Bd1_pages.txt | head -4"
}
```


### [2026-10-16T05:16:00.208Z] TOOL RESULT

```
11:10296  wy}ws   B  f* 
18:10297  wy>y  =»  >wy(h)1 
20:10298  wye   B,  C 
27:10299  wye-   B,  C    (j^<j^^)^j^vu^jl£j  io>jy>~d& 
32:(to)shake,  (fo)move,  (fo)stir 
9120:„Wit\ve“, ekkill „Witwer“ [nnorw. enkja, ekkja „Wit\ve“, dan. enke usw.],
10334:eccherode „diinn, schwaeh". Doch hat an. ekkja „Witwe“, ekkill „Witwer“
10335:(diin. cnke „Witwe“ usw.:   s. F-T. 194 und 1455j hiermit nichts zu tun
22292:     Dazu (vgl.die obigen «-Stamme) ai. vidhdva „Witwe“. av. vidavd ds.,
```


## [2026-10-16T05:16:04.947Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 21592,21660p incoming/WLD/WLD_Bd1_pages.txt | grep -n -i -E 'av\\.|np\\.|vi[jg]|weich|wicker|vicis' | head -12; sed -n 22285,22300p incoming/WLD/WLD_Bd1_pages.txt; grep -n -E '^ *2(3[89]|40) *$|^ *u̯eidh|ueidh-' incoming/WLD/WLD_Bd1_pages.txt | sed -n 1,5p"
}
```


### [2026-10-16T05:16:05.762Z] TOOL RESULT

```
6:ivijkti       „eintrefFen,        sich    erfiillen,       starker werden", vikrus „munter“.                     Lett.
12:     Arm.        i'fg   „Streit“, vig „Kraft, Starke" (Scheftelowitz                          BB. 2b, 306) kann
52:          um einer Bedrohung, einem Schlage u. dgl. auszuweichen, sich wenden.
53:          weichen.
68:                                                 gall.-lat.              cambiarc „wecliseln‘‘: auch von ,,weichen“ kann



                                               den  beiden Erhijhungen   auf
22, 60 Hinweis auf ai. vidu- m. ,,die zwischen
der Stirn des Elephanten    befindliehe Gegend“       unbelegt     ist nicht—                         —
vorzuziehen).
     Dazu (vgl.die obigen «-Stamme) ai. vidhdva „Witwe“. av. vidavd ds.,
gr.            „Junggeselle‘\ lat. vidua ,/VVitwe: geschiedene oder unver-
          *y[j:](i?£Os

heiratete Frau“, viduus „beraubt, leer von etwas“, air. fedb ,.Witwe‘\ corn.
fjiiedeu ds.. cymr, gwcddu: „Witwer", got. ividuwo „Witwe‘* (
                                                                 widuwcdrna
,,Waise“, s. zum Formans Niedermann IF. 37, 152        gegen  Bechtel Lexil.

22184:                                                                  ueidh-, uidh-                                                        23V
22257:ueidh-, uidh- „trennen“, wohl aus *ui- „auseinamler“ und *dhe- ,,setzen
22281:240
```


## [2026-10-16T05:16:10.390Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^vice versa|vice versa,|^viceroy|^divide,|^wicker,|^week,|^widow,' KLN_1966.txt | head; grep -n -i -E 'vice.versa' SKT.txt | head -3"
}
```


### [2026-10-16T05:16:10.888Z] TOOL RESULT

```
11904:divide,  tr.  and  intr.  v.  —  ME.  deviden,  dividen, fr.  L.  dividere,  'to  force  apart,  separate,  divide’, fr.  di-,  ‘apart’,  and  I.-E.  base  *widh-,  ‘to  separ¬ ate’,  whence  also  L.  vidua ,  Goth,  widuwo,  OE. widewe,  ‘widow'.  See  widow  and  cp.  divisi,  di¬ vision  ;  device,  devise,  individual.  I.-E.  base  *widh- is  probably  compounded  of  base  *wi-.  ‘apart, asunder’,  and  base  *dhe-,  ‘to  place’.  Acc  dingly
```


## [2026-10-16T05:16:13.300Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^(vice|vice-|viceroy|wicker|week|weak|widow)\\b' KLN_1966.txt | head; grep -n -E 'vice versa' KLN_1966.txt | head -3"
}
```


### [2026-10-16T05:16:13.756Z] TOOL RESULT

```
30797:Derivatives:  pseudonym-al,  pseudonym-ic,  adjs., pseudonym-ity,  n.,  pseudonym-ous,  adj.,  pseu- donym-ous-ly,  adv.,  pseudonym-ous-ness,  n. pseudopod,  n.  —  The  same  as  pseudopodium, pseudopodium,  n.,  temporary  extension  of  the protplasm  of  a  cell  serving  for  locomotion.  — ModL.,  compounded  of  pseudo-  and  ModL. -podium,  fr.  Gk.  -mSStov,  fr.  rrdStov,  dimin.  of Tzoiz,  gen.  noSoq,  ‘foot’.  See  podium. Derivatives :  pseudopod-al,  pseudopod-ial,  adjs. pseudoscopc,  n.,  an  optical  instrument  which makes  convex  objects  appear  concave  and  vice versa.  —  Compounded  of  pseudo-  and  Gk. -cncdmov,  fr.  oxotreiv,  ‘to  look  at,  examine’.  See -scope.
```


## [2026-10-16T05:16:22.084Z] TOOL CALL #43: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe-private/site/pages/535.jpg 2>/dev/null || pdftoppm -f 535 -l 535 -r 200 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg535"
}
```


### [2026-10-16T05:16:22.388Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   63k sfmqrb 14 Oct 22:15  /home/sfmqrb/git/rishe-private/site/pages/535.jpg
```


## [2026-10-16T05:16:24.030Z] TOOL CALL #44: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/535.jpg"
}
```


### [2026-10-16T05:16:24.059Z] TOOL RESULT

```

```


## [2026-10-16T05:16:28.597Z] TOOL CALL #45: Bash

```json
{
 "command": "grep -o -i -E '.{30}(att.r|محمود).{60}' /home/sfmqrb/git/rishe-private/data/extracted/batch/page-535.json | head; grep -o -E '\"(widewaz|wye)[^\"]*\"' /home/sfmqrb/git/rishe-private/data/extracted/batch/page-535.json"
}
```


### [2026-10-16T05:16:28.947Z] TOOL RESULT

```
"widewaz"
"wye"
```


## [2026-10-16T05:16:49.922Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'بیختن|پرویزن|انگیختن' BQT_v1_pages.txt | head; grep -n -E 'wēxtan|vēxtan|vextan|wextan|bextan' BQT_v1_pages.txt | head"
}
```


### [2026-10-16T05:16:50.281Z] TOOL RESULT

```
5665:بخشیدن و مشك بیختن و گل ریختن باشد (" .
8675:۲ - مولف منتهی الارب در ترجمةٌ « تمییج » آرد : « برانگیختن نکه را برآلیز . »
10775:انگیختن جنگ و , بر افروختن آتش را نیز
14961:برانگیختن بجنگه و غیره‌باشد - و تقاضانمودن
18131:انگیختن باشد و بعربی اغرا هگویند .
18160:بمعئی بر انگیختن و تحریض ( ۱ )کردن باشد
18728:بمعتی برانگیختن و تحریض نمودن شخصی باشد
19265:بر هیختی ۲ - بر وزن انگیختن حطلق
19286:بروزن شیمن » پرویزن باشد که بعربی غرپال
19305:۱ - رك : برزن و پریزن . ۴ - رك : پرویزن . ۴ ٩‏ بریجن » پهلوی .
```


## [2026-10-16T05:16:52.860Z] TOOL CALL #47: Bash

```json
{
 "command": "sed -n 60,200p /home/sfmqrb/git/rishe-private/tools/verify_check.py | grep -n -E 'problems.append|consulted|ref_check|error_in|sources|png' | head -40"
}
```


### [2026-10-16T05:16:53.203Z] TOOL RESULT

```
6:                    problems.append(f"page {pg}: entry {i} ({e['root']['name']}) node #{n['id']} missing")
10:                    problems.append(f"page {pg}: entry {i} node #{n['id']} verdict {nv!r} invalid")
15:                    problems.append(f"page {pg}: entry {i} node #{n['id']} has no derivation")
18:                for rc in vn.get("ref_check") or []:
20:                for c in vn.get("consulted") or []:
27:    print("books consulted:", dict(con_tally), "| by book:", dict(con_books.most_common(40)))
```


## [2026-10-16T05:16:57.049Z] TOOL CALL #48: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK && cp /home/sfmqrb/git/rishe-private/site/pages/535.jpg /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg535.jpg && python3 -c \"\nfrom PIL import Image; Image.open('/home/sfmqrb/git/rishe-private/site/pages/535.jpg').save('/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/535.png')\" && ls -la /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/535.png"
}
```


### [2026-10-16T05:16:57.526Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image; Image.open('/home/sfmqrb/git/rishe-private/site/pages/535.jpg').save('/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/535.png')
    ^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'PIL'
```


## [2026-10-16T05:16:59.765Z] TOOL CALL #49: Bash

```json
{
 "command": "pdftoppm -f 535 -l 535 -r 200 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/535 && ls -la /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/535.png"
}
```


### [2026-10-16T05:17:00.823Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   71k sfmqrb 16 Oct 01:17  /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/535.png
```


## [2026-10-16T05:17:01.675Z] AGENT

Now writing the verification file.


## [2026-10-16T05:19:20.993Z] TOOL CALL #50: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/page-535.json",
 "content": "{\n  \"pdf_page\": 535,\n  \"book_page\": 505,\n  \"verified_by\": \"claude-opus-5.5\",\n  \"verified_on\": \"2026-10-16\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Weidh\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₁weydʰ- / *weidʰ- 'to separate, divide'; *h₁widʰéwh₂ 'widow'\",\n      \"note\": \"Pokorny 1127-1128 'u̯eidh- to separate; widow'; AHD weidh- 'to divide, separate' (widow, divide, devise). Root, label and gloss correct. The page (book p. 505) was checked against the printed image: extraction faithful. Only weak point: the Germanic form 'widewaz' (#3) is not the standard reconstruction (*widuwō(n)-, feminine).\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *weidʰ- «جدا کردن، بخش کردن» در پوکورنی (ص ۱۱۲۷) و فرهنگ امریکن هریتیج (weidh-) آمده و واژهٔ «بیوه» (زنِ جدا مانده از شوی) از همین ریشه است. ریشه، برچسب زبانی و معنای آن درست است؛ ادعای نورایی درست است. تنها صورت ژرمنی widewaz نادرست چاپ شده و صورت پذیرفته *widuwō است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁weydʰ-\",\n        \"https://en.wiktionary.org/wiki/بیوه\",\n        \"https://www.etymonline.com/word/widow\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1127\", \"status\": \"supports\", \"note\": \"POK_full.txt line ~89130-89174, 'Root/lemma: u̯eidh-, u̯idh- Meaning: to separate; widow ... Old Indic vidhavā widow, Avestan viδavā ds., Latin vidua, Gothic widuwo, Old English widuwe ... Latin dīvido' — Page(s): 1127-1128.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I pp. 239-240 (WLD_Bd1_pages.txt line 22257, 22292)\", \"stance\": \"supports\", \"note\": \"'u̯eidh-, u̯idh- „trennen“ ... ai. vidhavā „Witwe“, av. viδavā ds., lat. vidua, got. widuwo'.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 1135 s.v. weidh-\", \"stance\": \"supports\", \"note\": \"'weidh-. To divide, separate. 1. ... *widh-ewā- ... in Germanic *widuwō in Old English widuwe: WIDOW. 2. ... Latin dividere: DEVISE, DIVIDE. [Pok. weidh- 1127.]'\"},\n        {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 11904 s.v. divide\", \"stance\": \"supports\", \"note\": \"'L. dividere ... fr. di-, apart, and I.-E. base *widh-, to separate, whence also L. vidua, Goth. widuwo, OE. widewe, widow'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"vidhavâ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan viδauuā- (f.) 'widow' (Bartholomae: 'Wittwe', in the phrase vahū- viδavā-) continues Proto-Iranian *widʰawā- < PIE *h₁widʰéwh₂, the zero grade *widʰ- 'separated' + -ewo-/-ewā suffix ('the woman bereft [of her husband]'); exact cognate of Sanskrit vidhávā. Avestan spirantised intervocalic *dʰ > δ. The gloss 'separated' is the etymological sense, 'widow' the attested one.\",\n          \"derivation_fa\": \"اوستایی viδavā- به معنای «بیوه» از ایرانی باستان *widʰawā- و آن از هندواروپایی آغازین *h₁widʰéwh₂ است: ستاکِ تهی *widʰ- «جدا» با پسوند -ewā، یعنی «زنی که از شوی جدا مانده». سنسکریت vidhávā هم‌ریشهٔ دقیق آن است و dʰ میان‌واکه‌ای در اوستایی به δ سایشی بدل شده. معنای «جدا شده» معنای ریشه‌ای است؛ ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁widʰéwh₂\", \"https://en.wiktionary.org/wiki/بیوه\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1127\", \"status\": \"supports\", \"note\": \"POK_full.txt line 89159: 'Old Indic vidhavā widow, Avestan viδavā ds.' under u̯eidh- (pp. 1127-1128).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt line 24065 (col. ~1443)\", \"stance\": \"supports\", \"note\": \"'j. viδavā- f. Wittwe, in Verbindung mit vahū- ... ai. vidhavā- ..., np. bēva'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 240\", \"stance\": \"supports\", \"note\": \"'ai. vidhavā „Witwe“, av. viδavā ds.'\"},\n            {\"src\": \"AHD\", \"where\": \"weidh-\", \"stance\": \"supports\", \"note\": \"*widh-ewā- 'woman separated (from her husband by death)'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"bîveh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP بیوه bēva/bive 'widow' < Middle Persian wēwag [wydwk / wdpk] 'widow' < *widawā-ka- (Av. viδavā- + diminutive/feminine -ka-). Intervocalic *δ was lost and *i + a coalesced into MP ē (wēwag); initial w- > b- in New Persian (as in wēxtan > bēxtan, wēš > bēš), final -ag > -a. Bartholomae himself cites np. bēva under viδavā-.\",\n          \"derivation_fa\": \"«بیوه» در فارسی نو از فارسی میانهٔ wēwag «بیوه» و آن از ایرانی باستان *widawā-ka- (اوستایی viδavā- با پسوند -ka) است. δ میان‌واکه‌ای افتاده و i با a درآمیخته و ē شده؛ w آغازین در فارسی نو به b بدل شده (چنان‌که wēš > بیش) و -ag پایانی به ـه رسیده. بارتولومه خود «بیوه» را زیر viδavā- آورده است؛ ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/بیوه\"],\n          \"ref_check\": [\n            {\"ref\": \"BRT:1443\", \"status\": \"supports\", \"note\": \"BRT.txt line 24065: 'viδavā- f. Wittwe ... np. bēva' (column lies between the running heads 1427-28 and 1473-74, consistent with 1443).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD.txt line 651 / PHD_mackenzie.txt line 5333\", \"stance\": \"supports\", \"note\": \"'wēwag [wdpk' | N bēwa] widow'.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 263 (HRN.txt line 2651)\", \"stance\": \"supports\", \"note\": \"'bēve Wittwe ... ai. vidhávā Wittwe; phlv. vēvak; lat. vidua; got. viduvō'.\"},\n            {\"src\": \"HUB\", \"where\": \"p. 165 §56 (HUB.txt line 5817)\", \"stance\": \"supports\", \"note\": \"'bēva Wittwe H. 263' listed among words with ap. v after vowels.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Germanic\",\n          \"words\": \"widewaz\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The Proto-Germanic word for 'widow' is *widuwō (feminine ō- or n-stem *widuwōn-), < PIE *h₁widʰéwh₂; attested as Gothic widuwo, OE widuwe/wuduwe, OHG wituwa. The book prints 'widewaz', which has a masculine a-stem ending -az that no source reconstructs for this feminine noun; it is Nourai's misprint/misreconstruction for *widuwō (the derivation itself, Germanic 'widow' < weidh-, is correct). The extraction is faithful to the printed page.\",\n          \"derivation_fa\": \"صورت ژرمنی آغازینِ «بیوه» *widuwō (مؤنث) است که در گوتی widuwo و انگلیسی کهن widuwe دیده می‌شود. کتاب widewaz چاپ کرده که پسوند مذکرِ -az دارد و هیچ منبعی آن را برای این اسمِ مؤنث بازسازی نکرده؛ این خطای چاپی/بازسازی خود کتاب است، نه خطای خوانش اسکن. اصل پیوند (ژرمنی «بیوه» از ریشهٔ weidh-) درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/widuwǭ\", \"https://www.etymonline.com/word/widow\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt line 1135: 'in Germanic *widuwō in Old English widuwe, widow' — supports the derivation but gives *widuwō, not widewaz.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1127\", \"stance\": \"partial\", \"note\": \"'Gothic widuwo widow, Old English widuwe, wuduwe, Old High German wituwa' — no form *widewaz.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 21453 s.v. Widow\", \"stance\": \"partial\", \"note\": \"'A.S. widwe, widuwe ... Goth. widuwa'.\"}\n          ],\n          \"error_in\": \"book\",\n          \"book_prints\": \"widewaz\",\n          \"correct_form\": \"*widuwō (*widuwōn-)\"\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"widow\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English widuwe/wuduwe < Proto-Germanic *widuwō; Middle English widewe > Modern English widow (unstressed -uwe reduced to -ow). Inherited, not borrowed.\",\n          \"derivation_fa\": \"انگلیسی widow از انگلیسی کهن widuwe و انگلیسی میانه widewe و آن از ژرمنی آغازین *widuwō است؛ واژه‌ای موروثی است و با «بیوه»ی فارسی هم‌ریشه. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/widow\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference cited by Nourai for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 21453\", \"stance\": \"supports\", \"note\": \"'Widow. (E.) M.E. widewe; A.S. widwe ... Skt. vidhavā'.\"},\n            {\"src\": \"AHD\", \"where\": \"weidh-\", \"stance\": \"supports\", \"note\": \"'Old English widuwe, widow: WIDOW'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"dîvidere\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin dīvidere 'to separate, divide' = dis- 'apart' (with dī- before voiced v) + *-videre < zero-grade *widʰ- (PIE dʰ > Latin medial d), cf. Umbrian vef-, Latin vidua 'widow', viduus 'bereft'.\",\n          \"derivation_fa\": \"لاتین dīvidere «جدا کردن، بخش کردن» از پیشوند dis- «جدا» (پیش از v به dī- کوتاه شده) و ستاکِ تهی *widʰ- است که dʰ هندواروپایی در میان واژه در لاتین d شده. هم‌ریشهٔ vidua «بیوه»ی لاتین است؛ ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/divide\", \"https://en.wiktionary.org/wiki/divido#Latin\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD weidh-: '2. Zero-grade form *widh- in Latin dividere, to separate (dis-, intensive prefix): DEVISE, DIVIDE'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1127\", \"stance\": \"supports\", \"note\": \"'Latin dīvido, -ere separate, divide'.\"},\n            {\"src\": \"KLN\", \"where\": \"line 11904 s.v. divide\", \"stance\": \"supports\", \"note\": \"'fr. di-, apart, and I.-E. base *widh-, to separate'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 239\", \"stance\": \"supports\", \"note\": \"lat. dīvido under u̯eidh- 'trennen'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"divide\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin dīvidere > Middle English deviden/dividen (14th c., learned borrowing, partly via Old French diviser) > Modern English divide.\",\n          \"derivation_fa\": \"انگلیسی divide در سدهٔ چهاردهم از لاتین dīvidere (تا اندازه‌ای از راه فرانسوی کهن) وام گرفته شده و در انگلیسی میانه deviden/dividen بوده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/divide\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference cited by Nourai for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 11904\", \"stance\": \"supports\", \"note\": \"'divide ... ME. deviden, dividen, fr. L. dividere'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 5232 s.v. Divide\", \"stance\": \"supports\", \"note\": \"'Divide. (L.) L. dividere, to separate'.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Weik 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *weik-/*weig- 'to bend, wind; to give way, swing' (Pokorny 4. u̯eik-, u̯eig- 1130-1131; AHD weik-4)\",\n      \"note\": \"Pokorny 1130-1131 lists exactly this material (Av. vaēg- 'swing', vyāxa-/vyāxman- 'assembly' (with ?), NP vēxtan, Lat. vicis, ON veikr, OE wicu). AHD's weik-4 'to bend, wind' gives wicker, weak, week, vice-, vicissitude. Root, label and gloss are therefore right as Pokorny/AHD have them. Modern work (LIV 667f., Cheung 2007: 413f.) separates *weig- 'to swing, shake' (Av. vaēg-, NP āvēxtan, Sogd. wyc) from the 'bend' root and puts NP bēxtan/parvēzan 'sift' under a different Indo-Iranian root *waič 'to sift' (Av. vaēc-, Skt. vec-/vinakti), and angēxtan under *ham-gaiz. The printed page shows also a couplet of 'Attār (یک شبی محمود می‌شد بی‌سپاه / خاک‌بیزی دید سر بر خاک راه, illustrating خاک‌بیز) which the extraction omitted.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی *weik-/*weig- «خم کردن، پیچیدن؛ جنبیدن» در پوکورنی (ص ۱۱۳۰) و امریکن هریتیج (weik-4) آمده و همان داده‌های نورایی را دارد؛ پس ریشه و معنا درست است. اما پژوهش امروزی (چونگ ۲۰۰۷) «آویختن» را از *waiǰ «جنباندن، تاب دادن» و «بیختن، پرویزن» را از ریشهٔ جداگانهٔ *waič «الک کردن» (اوستایی vaēc-، سنسکریت vec-) و «انگیختن» را از *ham-gaiz می‌داند. یک بیت از عطار که در کتاب آمده در داده‌های استخراج‌شده نیامده است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weyg-\",\n        \"https://en.wiktionary.org/wiki/آویختن\",\n        \"https://www.etymonline.com/word/week\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1130\", \"status\": \"supports\", \"note\": \"POK_full.txt lines 89443-89515: 'Root/lemma: u̯eik-4, u̯eig- Meaning: to curve, bend; to go round, to exchange ... Avestan vaēg- (a projectile) swing ... npers. vextan toss, fling ... Avestan vyāxa-, vyāxman- congregation, meeting (?) ... Latin vicis' — Page(s): 1130-1131.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 1137 s.v. weik-4\", \"stance\": \"supports\", \"note\": \"'weik-4. Also weig-. To bend, wind ... WICKER ... *waikwaz ... WEAK ... *wikōn-, a turning, series ... WEEK ... Latin vix (genitive vicis), turn, situation, change: VICAR, VICE ... [Pok. 4. weik- 1130.]'\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. I pp. 233-235 (WLD_Bd1_pages.txt line 21592ff.)\", \"stance\": \"supports\", \"note\": \"'u̯eik-, u̯eig-' — 'auszuweichen, sich wenden; weichen'.\"},\n        {\"src\": \"CHEUNG\", \"where\": \"pp. 413-414 *u̯aiǰ (CHEUNG.txt line ~26820)\", \"stance\": \"partial\", \"note\": \"'*u̯aiǰ to shake, swing ... PIE *u̯eig- to (start to) swing, shake = LIV 667f. | Pok. 1130f.' — but Cheung treats it as probably distinct from the 'yield/bend' root.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"waix, waik, waig,vaĕg, vaĕca; vyâxa, vyâxman\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Avestan vaēg- (pres. vaējaiti-, part. vaējant-, -nivixta-) 'to swing, brandish (a weapon)' is the regular Indo-Iranian reflex *waiǰ- < PIE *weig- (Cheung *u̯aiǰ; Pokorny 1130) — confirmed; 'waix, waik, waig' are root notations, not attested words, and nothing of this verb is attested in Old Persian, so the 'Old Persian' label is unsupported. 'vaēca' belongs to the separate Av. vaēc- 'to sift, select' (Cheung *u̯aič, Skt. vec-), not to 'swing'. vyāxa- 'assembly' and vyāxman-/vyāxana- 'eloquent in the assembly' are real Avestan words (Bartholomae), but Pokorny himself marks their attachment here with '(?)'; they are usually connected with vi- + *Hak-/vac- rather than securely with *weik-.\",\n          \"derivation_fa\": \"اوستایی vaēg- (vaējaiti، vaējant-) «تاب دادن، پرتاب کردن (جنگ‌افزار)» بازتاب منظمِ *waiǰ- هندوایرانی از *weig- هندواروپایی است و درست است؛ اما waix، waik، waig صورت ریشه‌اند نه واژهٔ گواهی‌شده، و در پارسی باستان چنین فعلی دیده نمی‌شود. vaēca از فعل جداگانهٔ vaēc- «بیختن، برگزیدن» (چونگ: *waič) است نه از «تاب دادن». vyāxa- «انجمن» و vyāxman- واژه‌های واقعی اوستایی‌اند، ولی پوکورنی خود پیوند آن‌ها را با این ریشه با نشانهٔ پرسش آورده است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weyg-\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:1130\", \"status\": \"supports\", \"note\": \"POK p. 1130: 'Avestan vaēg- (vaējā-) (a projectile) swing ... nivixta- herabgeschwungen ... Avestan vyāxa-, vyāxman- congregation, meeting (?)' — supports, with Pokorny's own query on vyāxa.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt line 21995 (vaējant- 's. vaig-'); line 24678-24682 (vyāxa-, vyāxana-)\", \"stance\": \"partial\", \"note\": \"'vaējant- Adj., PPA.: s. vaig-'; '*vyāxa- m. Versammlung ... Vgl. vyāxana-, vyāxman-' — words confirmed; Bartholomae keeps vyāxa- apart from vaig-.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"p. 413 *u̯aiǰ; p. 407-408 *u̯aič\", \"stance\": \"partial\", \"note\": \"'*u̯aiǰ to shake, swing: YAv. vij- ... vaējant-, -niuuixta-'; separately '*u̯aič to sift ... YAv. vaēc- to select, sort out, sift ... no certain IE cognates' — so vaēca does not belong here.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 233f.\", \"stance\": \"partial\", \"note\": \"u̯eik-/u̯eig- with Indo-Iranian vij- 'zurückfahren'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"vîxtan; âvîxtan; âvang; bîxtan; parvîzan\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"āvīxtan/āvēxtan (pres. āvēz-) 'to hang' = *ā- + *waiǰ- 'swing' (MP āwēxtan, Oss. awinjyn) — confirmed by Horn 56, Cheung and Wiktionary (< *wayǰ- < PIE *weyg-). vīxtan 'to sling' is the dictionary simplex (MP wēxtan, wēz- 'swing, brandish, throw', MacKenzie) — confirmed. āvang 'rope for hanging fruit; anything suspended; pendulum' (Mo'in) is compared by Horn with āvēxtan (āveng, āvingān 'hanging'), presumably a nasal-present *ā-wi-n-ǰ-/*ā-wang-, as in Oss. awinjyn — plausible but not demonstrated. bīxtan/bēxtan (bēz-) 'to sift' and parvīzan/parwēzan 'sieve' (*pari-waič-ana-) are disputed: MacKenzie separates 1wēxtan 'sift, select' from 2wēxtan 'swing', and Cheung derives them from Indo-Iranian *waič 'to sift' (Av. vaēc-, Skt. vec-/vinakti 'separate, winnow'), a root with no certain IE cognates, not from *weik-/*weig-; Horn 249 likewise compares Skt. vec-. (NP has a homonymous bēxtan 'to shake' that Cheung does put under *u̯aiǰ.)\",\n          \"derivation_fa\": \"«آویختن» (آویز) از پیشوند ā- و ریشهٔ ایرانی *waiǰ- «جنباندن، تاب دادن» است (پهلوی āwēxtan، آسی awinjyn) و درست است؛ «ویختن» نیز همان فعل سادهٔ پهلوی wēxtan «تاب دادن، پرتاب کردن» است. «آونگ» (ریسمانی که خوشهٔ انگور از آن آویزند، و آونگ ساعت) را هورن با «آویختن» سنجیده و پذیرفتنی است، هرچند ساخت آن روشن نیست. اما «بیختن» و «پرویزن» را مکنزی و چونگ از ریشهٔ جداگانهٔ *waič «الک کردن، جدا کردن» (اوستایی vaēc-، سنسکریت vec-) می‌دانند، نه از *weik- «خم کردن»؛ پس این بخش از ادعای نورایی با پژوهش امروزی سازگار نیست.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/آویختن\", \"https://vajehyab.com/moein/آونگ\", \"https://vajehyab.com/moein/بیختن\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:14\", \"status\": \"supports\", \"note\": \"HRN.txt line 926 (p. 14, no. 56): 'āveyten hängen, aufhängen, Praes. āvēz-em ... vergl. āveng, āvingān hängend; phlv. āvēxtan ... oss. awinjin hängen ... Anknüpfung an ai. vij-, vijate'.\"},\n            {\"ref\": \"BQT:67\", \"status\": \"partial\", \"note\": \"BQT_v1_pages.txt lines 9028-9068: entries آون 'مخفف آونگ ... آویخته و آویزان شده'، آونگ 'ریسمانی ... خوشه‌های انگور از آن آویزند'، آویج 'بمعنی آویز است که از آویختن باشد' — headwords confirm meanings; Mo'in's etymological footnotes are not legible in the OCR.\"},\n            {\"ref\": \"BQT:333\", \"status\": \"not_found\", \"note\": \"grep of BQT_v1_pages.txt for بیختن/پرویزن found only incidental uses (line 19286 'پرویزن باشد که بعربی غربال') — the cited headword page could not be located in the noisy OCR.\"},\n            {\"ref\": \"MON:620\", \"status\": \"not_checked\", \"note\": \"printed Mo'in page not accessible; online Mo'in (vajehyab) consulted instead, see consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"pp. 407-408 *u̯aič; pp. 413-414 *u̯aiǰ\", \"stance\": \"partial\", \"note\": \"*u̯aiǰ: 'NP āvextan/āvez- to hang, suspend' and 'NP bextan/bez- to shake' — supports āvīxtan; *u̯aič 'to sift': 'NP bēxtan/bēz- ... (+ *pari-) NP parwēz sieve' — contradicts bīxtan/parvīzan under this root.\"},\n            {\"src\": \"PHD\", \"where\": \"PHD.txt line 651\", \"stance\": \"partial\", \"note\": \"'1wēxtan, wēz- [... N bēxtan, bēz-] sift, select, choose, separate ... 2wēxtan, wēz- swing, brandish, throw, pour out' — two separate verbs.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 249 (HRN.txt line 2555)\", \"stance\": \"partial\", \"note\": \"'bēxten sieben, Praes. bēz-em; pervēzen Sieb. ai. vec-, vinakti, vivekti durch Schwingen oder Worfeln aussondern'.\"},\n            {\"src\": \"HUB\", \"where\": \"p. 165 §56\", \"stance\": \"silent\", \"note\": \"lists 'āvextan hängen H. 56; parvēzan Sieb H. 249' only as phonological examples, no root.\"},\n            {\"src\": \"MON\", \"where\": \"vajehyab s.v. آونگ, بیختن\", \"stance\": \"partial\", \"note\": \"آونگ: 'ریسمانی که خوشه‌های انگور ... از سقف می‌آویزند ... جسم سنگینی که گرد محور ثابتی حرکت کند، مانند پاندول'؛ بیختن: '[په.] الک کردن، غربال کردن' — meanings confirmed, no root given.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"han-vĕxt-an\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Pahlavi verb is hangēxtan, pres. hangēz- [hngyhtn', hngyc-] 'to arouse, stimulate, stir up' (MacKenzie; Nyberg 'to excite, provoke, rouse'). Nourai's 'han-vēxtan' is an analysis, not the attested form: *ham- + *waiǰ- ('swing together, shake up'), with *-mw- > -ng- (Horn 127: 'phlv. angēxtan antreiben ... vergl. ham-vēxt'). Cheung instead files hangēz- under a root *gaiz? 'to disturb, stir, incite' (+ *ham-), comparing Oss. ængizyn, Bal. gēj-; he himself marks that root as uncertain. So the old *ham-waig analysis is possible but not the current standard.\",\n          \"derivation_fa\": \"صورت پهلوی hangēxtan (ستاک حال hangēz-) «برانگیختن، تحریک کردن» است و han-vēxtan نورایی تجزیهٔ اوست نه صورت گواهی‌شده: پیشوند ham- با *waiǰ- «جنباندن» که در آن -mw- به -ng- بدل شده (هورن، شمارهٔ ۱۲۷). چونگ اما این فعل را از ریشهٔ دیگری، *gaiz «آشفتن، برانگیختن» با پیشوند ham-، می‌گیرد و آن ریشه را خود نامطمئن می‌شمارد. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://www.mpcorpus.org/\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:30\", \"status\": \"supports\", \"note\": \"HRN.txt line 1536 (no. 127, p. 30): 'engēxten antreiben, Praes. engēz-em; phlv. angēxtan antreiben ... vergl. ham]vēxt ... skr. vgl. saṃvigna aufgeregt; oss. ve-, bal. gējag schwingen'.\"},\n            {\"ref\": \"AEF:169\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Persian translation of Horn not available locally (catalog entry only); it reproduces Horn no. 127.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD.txt line 394; PHD_mackenzie.txt line 2826\", \"stance\": \"partial\", \"note\": \"'hangēxtan, hangēz- [hngyhtn', hngyc- | (M hgjyn-), N an~] arouse, stimulate, stir up' — form differs from 'han-vēxtan'; no root given.\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 1907 s.v. hangaxtār\", \"stance\": \"partial\", \"note\": \"'From hangēxtan hangēz- to excite, to provoke, to rouse ... NP angēxtan, angēzīdan'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"p. 97-98 *gaiz (CHEUNG.txt line 7258)\", \"stance\": \"contradicts\", \"note\": \"'*gaiz ? to disturb, stir, incite, excite? ... (+ *ham-) BMP hngyc- /hangēz-/ to arouse ... NP angextan/angez- to stir up, incite'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"angîxtan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP angīxtan/angēxtan (pres. angēz-) 'to excite, stir up, motivate' < MP hangēxtan, hangēz- with loss of initial h- before a- (as in hanjaman > anjoman, handāxtan > andāxtan); derivatives angēzīdan, angēzāndan, angēze 'motive' are regular NP formations on the present stem. The NP link to MP is certain; the ultimate root (*ham-waiǰ- per Horn/Nourai vs. *ham-gaiz per Cheung) is uncertain, hence 'plausible'.\",\n          \"derivation_fa\": \"«انگیختن» (ستاک حال: انگیز) از پهلوی hangēxtan/hangēz- است که h آغازین آن در فارسی نو افتاده (چنان‌که hanjaman > انجمن). «انگیزیدن»، «انگیزاندن» و «انگیزه» ساخته‌های منظم فارسی نو بر ستاک حال‌اند. پیوند فارسی نو با پهلوی قطعی است، ولی ریشهٔ دورتر (ham- + *waiǰ- به گفتهٔ هورن و نورایی، یا ham- + *gaiz به گفتهٔ چونگ) روشن نیست؛ پس ادعا با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/انگیختن\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:178\", \"status\": \"not_found\", \"note\": \"BQT_v1_pages.txt has many incidental uses of انگیختن (lines 10775, 14961, 18131 ...) but the headword entry with Mo'in's footnote could not be isolated in the OCR.\"},\n            {\"ref\": \"AEF:169\", \"status\": \"not_checked\", \"note\": \"not available locally (catalog only); reproduces Horn no. 127.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 127\", \"stance\": \"supports\", \"note\": \"'engēxten antreiben ... phlv. angēxtan ... vergl. ham-vēxt'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"p. 97 *gaiz\", \"stance\": \"contradicts\", \"note\": \"'(+ *ham-) NP angextan/angez- to stir up, incite' under *gaiz, not *u̯aiǰ.\"},\n            {\"src\": \"NYB\", \"where\": \"glossary s.v. hangaxtār\", \"stance\": \"supports\", \"note\": \"'NP angextan, angēzīdan' from MP hangēxtan.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Sogdian\",\n          \"words\": \"wye\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The Sogdian verb is wyc- /wēč-/ 'to move, shake, stir' (Buddhist and Christian Sogdian; also apa-/pati- compounds pw'yc-, ptw'yc- 'to be agitated'), the regular reflex of Iranian *waiǰ- (Cheung *u̯aiǰ), so the derivation is right. The book prints 'wye', a misreading of the c of Gharib's transliteration wyc (Gharib entry 10299 'wyc B, C ... to shake, move, stir', on p. 417 of his dictionary); the extraction is faithful to the printed page.\",\n          \"derivation_fa\": \"فعل سغدی wyc- (wēč-) «جنباندن، تکان دادن، به جنبش آوردن» است که بازتاب منظم *waiǰ- ایرانی است؛ پس اصل پیوند درست است. کتاب wye چاپ کرده که خوانش نادرستِ حرف c در آوانگاری قریب (wyc، مدخل ۱۰۲۹۹) است؛ این خطای چاپی کتاب است و استخراج با صفحهٔ چاپی یکی است.\",\n          \"sources\": [\"https://archive.org/details/SogdianDictionary\"],\n          \"ref_check\": [\n            {\"ref\": \"SOD:417\", \"status\": \"supports\", \"note\": \"SOD.txt line ~77720-77732: '10298 wyc B, C / 10299 wyc- B, C ... (to) shake, (to) move, (to) stir' (OCR renders c as e, the same misreading as in Nourai).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"p. 414 *u̯aiǰ\", \"stance\": \"supports\", \"note\": \"'SOGDIAN: BSogd. wyc, CSogd. wyc to move, shake [intr.] || (+ *apa-) BSogd. pw'yc- to shake, be agitated'.\"},\n            {\"src\": \"POK\", \"where\": \"p. 1130\", \"stance\": \"silent\", \"note\": \"no Sogdian form cited.\"}\n          ],\n          \"error_in\": \"book\",\n          \"book_prints\": \"wye\",\n          \"correct_form\": \"wyc (wēč-)\"\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Germanic\",\n          \"words\": \"wik; waikwaz; wikôn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *wīk-/*wik- (zero/full grade of *weig-) in Swedish viker 'willow twig', source of ME wiker 'wicker'; *waikwaz 'pliant, soft' (ON veikr, Dutch week) from o-grade *woig-; *wikōn- 'a turning, succession' (Goth. wiko 'order, turn', OE wicu) — all given by AHD weik-4 and Pokorny 1130-31 with exactly these meanings. Germanic k regularly continues PIE *g (Grimm's law).\",\n          \"derivation_fa\": \"ژرمنی آغازین *wik- (در سوئدی viker «ترکهٔ بید») و *waikwaz «نرم، خم‌پذیر» (نورس کهن veikr) و *wikōn- «گردش، نوبت» (گوتی wiko، انگلیسی کهن wicu «هفته») همه از *weig- «خم کردن، گشتن»اند و k ژرمنی بنا به قانون گریم از g هندواروپایی آمده. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/week\", \"https://www.etymonline.com/word/weak\", \"https://www.etymonline.com/word/wicker\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD weik-4: 'Swedish viker, willow twig ... WICKER ... Germanic *waikwaz ... WEAK ... Germanic *wikōn-, a turning, series, in Old English wicu: WEEK'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"pp. 1130-1131\", \"stance\": \"supports\", \"note\": \"'Old Icelandic veikr soft, weak ... Middle English wiker Weidengerte ... Old Icelandic vika Woche (originally *variation), Old English wicu'.\"},\n            {\"src\": \"SKT\", \"where\": \"lines 21254, 21290, 21448\", \"stance\": \"supports\", \"note\": \"Weak 'from Icel. veikr ... vīkja, to turn aside'; Week 'Goth. wiko ... orig. sense succession'; Wicker 'Swed. dial. vikker, willow, from vika, to bend'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 233ff.\", \"stance\": \"supports\", \"note\": \"Germanic weichen/weak forms under u̯eik-, u̯eig-.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"wicker; weak; week\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"wicker < ME wiker (14th c.) from a Scandinavian source (cf. Sw. viker, Dan. vigre); weak < ME weike, from ON veikr, replacing native OE wāc; week < OE wice/wicu < *wikōn- 'turn, succession'. All three from *weig-.\",\n          \"derivation_fa\": \"wicker از انگلیسی میانه wiker و آن از نورس (سوئدی viker)؛ weak از نورس کهن veikr که جای واژهٔ بومی wāc را گرفت؛ week از انگلیسی کهن wicu «نوبت، گردش». هر سه از ریشهٔ *weig- هستند؛ ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/wicker\", \"https://www.etymonline.com/word/weak\", \"https://www.etymonline.com/word/week\"],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference cited by Nourai for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"SKT.txt lines 21254, 21290, 21448\", \"stance\": \"supports\", \"note\": \"see Weak, Week, Wicker entries.\"},\n            {\"src\": \"AHD\", \"where\": \"weik-4\", \"stance\": \"supports\", \"note\": \"WICKER, WEAK, WEEK listed.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Latin\",\n          \"words\": \"vicis\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin vicis (gen.; nom. not used), acc. vicem, abl. vice 'turn, change, alternation, place/office of another' < zero-grade *wik- of *weik- 'to bend, turn' (AHD weik-4, Pokorny 1130 '2. Latin vicis, vicem, vice, pl. vices variation, Abwechslung'), cognate with Germanic *wikōn- 'week'.\",\n          \"derivation_fa\": \"لاتین vicis «نوبت، دگرگونی، جانشینی» (به حالت مفعولی vicem و حالت ازی vice) از ستاکِ تهی *wik- از ریشهٔ *weik- «گشتن، خم شدن» است و با «هفته»ی ژرمنی (*wikōn-) هم‌ریشه. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/vice-\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD weik-4: 'Zero-grade form *wik- in Latin vix (genitive vicis), turn, situation, change: VICAR, VICE; VICISSITUDE'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1130\", \"stance\": \"supports\", \"note\": \"'2. Latin vicis (Gen.), vicem, vice, Pl. vices, vicibus variation, Abwechslung'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 233ff.\", \"stance\": \"supports\", \"note\": \"lat. vicis under u̯eik-, u̯eig-.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"vice-versa; vice president, viceroy\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin ablative vice 'in place of, in turn' gives the phrase vice versā 'the position being turned' (17th c. in English) and the prefix vice- 'deputy' (ME, via Old French vis-/vice-): vice president, viceroy (French vice-roi, 16th c.). Note these are distinct from vice 'fault' (< vitium, AHD wei-4).\",\n          \"derivation_fa\": \"حالت ازیِ لاتین vice «به جای، به نوبت» در عبارت vice versā «با جابه‌جا شدن» (سدهٔ هفدهم در انگلیسی) و پیشوند vice- «نایب، جانشین» (از راه فرانسوی کهن) در vice president و viceroy (فرانسوی vice-roi) دیده می‌شود. این واژه با vice «گناه، عیب» (از vitium) یکی نیست. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/vice-\", \"https://www.etymonline.com/word/vice%20versa\", \"https://www.etymonline.com/word/viceroy\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD index: 'VICE3 weik-4', 'VICEROY reg-' (second element) — vice- under weik-4; vice1 'fault' under wei-4.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 20842 s.v. vice-gerent\", \"stance\": \"supports\", \"note\": \"'F. vicegerent ... L. uice, in place of ... So also vice-admiral, vice-roy (from F. roi)'.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt (grep 'vice versa')\", \"stance\": \"silent\", \"note\": \"headword not isolable in OCR.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-10-16T05:19:21.040Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe-private/data/verification/page-535.json (file state is current in your context — no need to Read it back)
```


## [2026-10-16T05:19:27.788Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 - <<'EOF'\nimport json\np='page-535.json'; d=json.load(open(p))\nok={\"https://en.wiktionary.org/wiki/بیوه\",\"https://en.wiktionary.org/wiki/آویختن\",\"https://vajehyab.com/moein/آونگ\",\"https://vajehyab.com/moein/بیختن\"}\nalt={\"POK\":\"https://archive.org/details/indogermanisches03pokouoft\",\"AHD\":\"https://archive.org/details/americanheritage00watk\",\"SOD\":\"https://archive.org/details/SogdianDictionary\"}\ndef fix(o):\n    o['sources']=[s for s in o['sources'] if s in ok]\nfor e in d['entries']:\n    fix(e)\n    for n in e['nodes']: fix(n)\nd['entries'][1]['nodes'][4]['sources']=[\"https://archive.org/details/SogdianDictionary\"]\njson.dump(d,open(p,'w'),ensure_ascii=False,indent=2)\nEOF\npython3 -m json.tool page-535.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 535"
}
```


### [2026-10-16T05:19:28.795Z] TOOL RESULT

```
nodes verified: 15/15
node verdicts: {'confirmed': 9, 'transcription_suspect': 2, 'plausible': 3, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 10, 'partial': 2, 'not_checked': 6, 'not_found': 2}
books consulted: {'supports': 24, 'partial': 11, 'silent': 3, 'contradicts': 2} | by book: {'SKT': 6, 'WLD': 5, 'POK': 5, 'CHEUNG': 5, 'AHD': 3, 'PHD': 3, 'HRN': 3, 'KLN': 3, 'BRT': 2, 'HUB': 2, 'NYB': 2, 'MON': 1}
```


## [2026-10-16T05:19:37.612Z] TOOL CALL #52: SubagentHandback

```json
{
 "message": "I verified PDF page 535 (book p. 505) and wrote /home/sfmqrb/git/rishe-private/data/verification/page-535.json. `verify_check.py 535` reports 0 PROBLEM lines, with 15 of 15 nodes verified.\n\n- **Roots:** both confirmed: Weidh (Pokorny 1127, AHD weidh-) and Weik 1 (Pokorny 1130, AHD weik-4).\n- **Nodes:** 9 confirmed, 3 plausible, 1 disputed, 2 transcription_suspect.\n\n**Disputed**\n- Weik 1 #2 (Persian), bîxtan / parvîzan: MacKenzie lists 'sift' wēxtan and 'swing' wēxtan as two separate verbs. Cheung (and Horn no. 249) put bēxtan and parwēzan under a different root, Indo-Iranian *waič 'to sift' (Avestan vaēc-, Sanskrit vec-), not *weik-/*weig-. âvîxtan and vîxtan in the same node are confirmed, and âvang is plausible.\n\n**Transcription_suspect** (both are misprints in the book itself; the extraction matches the printed page)\n- Weidh #3 (Germanic) \"widewaz\": the standard reconstruction is the feminine *widuwō. The -az ending is masculine, and AHD and Pokorny don't give that form.\n- Weik 1 #5 (Sogdian) \"wye\": the Sogdian verb is wyc 'to shake, move, stir' (Gharib entry 10299, Cheung *u̯aiǰ). Nourai misread the c as an e.\n\n**Plausible**\n- Weik 1 #1: Avestan vaēg- 'swing' is confirmed. The \"Old Persian\" label is unsupported, and \"vaĕca\" belongs to vaēc- 'sift'. Pokorny himself queries vyāxa/vyāxman.\n- Weik 1 #3 and #4 (han-vĕxtan → angîxtan): the attested Pahlavi form is hangēxtan. Horn derives it from *ham- + vēxt-, but Cheung puts it under *ham-gaiz.\n\n**Extraction error for the owner to fix:** the printed Persian box of Weik 1 includes an 'Attār couplet (یک شبی محمود می‌شد بی‌سپاه / خاک‌بیزی دید سر بر خاک راه) that is missing from data/extracted/batch/page-535.json.\n\nI saved the page image for audit at /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/535.png."
}
```


### [2026-10-16T05:19:37.878Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
