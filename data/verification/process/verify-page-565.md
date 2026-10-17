# Verification process log — verify-page-565


## [2026-10-17T00:30:14.336Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 565 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-565.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-565.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-565.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 565` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:30:14.394Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:30:22.587Z] TOOL CALL #1: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md; echo ====; cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-565.txt; echo ====; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-565.json",
 "description": "Read instructions, chart text, and source JSON"
}
```


### [2026-10-17T00:30:23.166Z] TOOL RESULT

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

... [8324 characters truncated] ...

ung 2007, Hasandust,
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

In the shell, `ls` is aliased to `eza`, which can hang without a terminal and leave your
command stuck. List files with `command ls` or `find` instead.

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


## [2026-10-17T00:30:40.088Z] TOOL CALL #2: Bash

```json
{
 "command": "sed -n '/SAVE what you/,/Wiktionary/p' /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md",
 "description": "Read the truncated middle of instructions"
}
```


## [2026-10-17T00:30:40.995Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-565.txt; echo; echo ====; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-565.json",
 "description": "Read chart text and source JSON"
}
```


### [2026-10-17T00:30:41.433Z] TOOL RESULT

```
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
  Persian digits are fine. Mention the key sources by their Persian-usable names (پوکورنی،
  بارتولومه، هرن، هوبشمان، مکنزی، نیبرگ، چونگ، معین، برهان قاطع، ویکی‌واژه).

Field names: `derivation_fa` (node) and `note_fa` (root entry). Both required.

## Process documentation (required)

The owner wants to be able to audit every step later. Therefore:

- **Every web page you rely on must be archived**: after you read a page (WebFetch or
  curl), run
  `python3 /home/sfmqrb/git/rishe-private/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
  This stores the page as text under `data/verification/sources/web/` and indexes it. Only
  URLs that were archived this way may appear in a `sources` array. (Batch several calls in
  one Bash command to save time.)
- **Every lookup in a local reference text must be quoted**: in `ref_check[].note` and
  `consulted[].note` include the exact phrase(s) you found (with the grep pattern or page you
  used), so the finding can be re-run.
- Your full transcript (every tool call and result) is exported automatically by the
  coordinator; nothing else needed for that.

## Sources to use (in roughly this order)

- **Wiktionary** (en.wiktionary.org) — has the best coverage of Persian, Middle Persian,
```


### [2026-10-17T00:30:41.493Z] TOOL RESULT

```
Exit code 1
=== PDF page 565 (book page 535) ===
--- entry 0 ---
ROOT [Indo-European] Yeu 1, Yeug : to join  (refs POK:509)
#1 (parent #0) [Avestan] refs=BQT:577,1228,2458; POK:509 | yaoj, yuj : I harnessed ; yuxta : harnessed, joined
  #2 (parent #1) [Persian] refs=None | yŭğ «یوغ» : yoke ; joft «جفت» : pair (union)
#3 (parent #0) [Greek] refs=POK:509; AHD; VDQ:346 | zugon, zygos, sextarious : yoke, arm of a pair of balances, scale
  #4 (parent #3) [Arabic] refs=VDQ:239 | zawj : yoke, pair, couple, spouse | NOTE: This apparently reached Arabic through another language.
    #5 (parent #4) [Persian] refs=FVA:180 | zowj «زوج» : pair, even, spouse, couple | extra: زوجه ، تزویج ، ازدواج ، مزدوج
  #6 (parent #3) [Arabic] refs=VDQ:346 | qest : balance, scale, justice
    #7 (parent #6) [Persian] refs=MON:2674 | qest «قسط» : justice, loan payment ; qestâs «قسطاس» : balance, scale | extra: اقساط
#8 (parent #0) [Germanic] refs=AHD | yukam
  #9 (parent #8) [English] refs=None | yoke
#10 (parent #0) [Sanskrit] refs=AHD | yuga : yoke ; yoga : union
  #11 (parent #10) [English] refs=None | yoga
#12 (parent #0) [Latin] refs=AHD | jungere : to join ; jugum : yoke ; yugista : nearby
  #13 (parent #12) [English] refs=None | join ; conjugate ; adjust
--- entry 1 ---
ROOT [Indo-European] Yeu 2, Yuwn, Yuwnkos, Ieu : young  (refs POK:510)
#1 (parent #0) [Avestan] refs=POK:510; KLN:1764; HRN | yuvan, yvan : young
  #2 (parent #1) [Persian] refs=BQT | javân «جوان» : young
#3 (parent #0) [Sanskrit] refs=KLN:1764 | yavan : young ; yuvasah : youth
#4 (parent #0) [Germanic] refs=AHD; KLN | juncaz, jungaz
  #5 (parent #4) [English] refs=None | young, youth, youngster
#6 (parent #0) [Latin] refs=AHD; KLN | juvenis : young ; juvencus : young man ; juvenca : young woman
  #7 (parent #6) [English] refs=None | junior, juvenile

(eval):1: === not found
```


## [2026-10-17T00:30:44.584Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/extracted/batch/page-565.json | head -c 6000; echo; echo '----'; cat data/verification/sources/SOURCE_MATRIX.md | head -120",
 "description": "Read source JSON and source matrix"
}
```


### [2026-10-17T00:30:44.994Z] TOOL RESULT

```
{
  "pdf_page": 565,
  "book_page": 535,
  "entries": [
    {
      "root": {
        "name": "Yeu 1, Yeug",
        "lang": "Indo-European",
        "refs": "POK:509",
        "gloss": "to join"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:577,1228,2458; POK:509",
          "words": [
            {"translit": "yaoj, yuj", "gloss": "I harnessed", "script": null},
            {"translit": "yuxta", "gloss": "harnessed, joined", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "yŭğ", "gloss": "yoke", "script": "یوغ"},
            {"translit": "joft", "gloss": "pair (union)", "script": "جفت"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:509; AHD; VDQ:346",
          "words": [
            {"translit": "zugon, zygos, sextarious", "gloss": "yoke, arm of a pair of balances, scale", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "VDQ:239",
          "words": [
            {"translit": "zawj", "gloss": "yoke, pair, couple, spouse", "script": null}
          ],
          "note": "This apparently reached Arabic through another language.",
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "FVA:180",
          "words": [
            {"translit": "zowj", "gloss": "pair, even, spouse, couple", "script": "زوج"}
          ],
          "script_extra": "زوجه ، تزویج ، ازدواج ، مزدوج",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "Arabic",
          "refs": "VDQ:346",
          "words": [
            {"translit": "qest", "gloss": "balance, scale, justice", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:2674",
          "words": [
            {"translit": "qest", "gloss": "justice, loan payment", "script": "قسط"},
            {"translit": "qestâs", "gloss": "balance, scale", "script": "قسطاس"}
          ],
          "script_extra": "اقساط",
          "note": null,
          "quote": {"text": "بقسطاسی بسنجم راز موبد - که چو سنگش بود قسطای لوقا", "poet": "Khâqânî"}
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "yukam", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "yoke", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "AHD",
          "words": [
            {"translit": "yuga", "gloss": "yoke", "script": null},
            {"translit": "yoga", "gloss": "union", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "yoga", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "jungere", "gloss": "to join", "script": null},
            {"translit": "jugum", "gloss": "yoke", "script": null},
            {"translit": "yugista", "gloss": "nearby", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "join", "gloss": null, "script": null},
            {"translit": "conjugate", "gloss": null, "script": null},
            {"translit": "adjust", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Yeu 2, Yuwn, Yuwnkos, Ieu",
        "lang": "Indo-European",
        "refs": "POK:510",
        "gloss": "young",
        "note": "Compare with root \"Aiw: vitality\""
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:510; KLN:1764; HRN",
          "words": [
            {"translit": "yuvan, yvan", "gloss": "young", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT",
          "words": [
            {"translit": "javân", "gloss": "young", "script": "جوان"}
          ],
          "note": null,
          "quote": {"text": "جوانی شمع ره کردم که جویم زندگانی را - نجستم زندگانی را و گم کردم جوانی را", "poet": "Shahrîyâr"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "KLN:1764",
          "words": [
            {"translit": "yavan", "gloss": "young", "script": null},
            {"translit": "yuvasah", "gloss": "youth", 
----
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
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS_pages.txt`
- **FSF** — Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF_pages.txt`
- **HENNING** — HENNING
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HENNING_selected_papers.txt`
- **EAV** — J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/EAV_studies.txt`
- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ISS_alt_DKS.txt`
- **AHM** — I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHM.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_pages.txt`
- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_pages.txt`
- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AVG.txt`
- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HID.txt`
- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt`
- **TLM** — H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Seri
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TLM.txt`
- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/UNV.txt`
```


## [2026-10-17T00:30:48.805Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n '120,400p' data/verification/sources/SOURCE_MATRIX.md | grep -E '^\\- \\*\\*|^#' ; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['VDQ','FVA','MON','BQT','KLN','HRN','AHD','POK']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:700]); print()\n\"",
 "description": "List remaining matrix books and ref details"
}
```


### [2026-10-17T00:30:49.351Z] TOOL RESULT

```
- **SBK** — M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
## Semitic / Arabic loans in either direction
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
- **PLA** — A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
- **AFA** — S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)
- **TAD** — Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-huru
- **ARB** — al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edi
- **KFL** — Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
- **LAM** — H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890
- **DOZ** — R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeu
- **AKD** — H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
- **SIN** — B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
## English / Romance / Germanic
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
- **WEB** — Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
- **RCH** — J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
- **NAT** — C. Berlitz, Native Tongues, New York 1982
- **PEI** — M. Pei, The Families of Words, New York 1962
## Turkic / Mongolian
- **TTS** — H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
- **VIE** — M.A. Sajjadiyyeh, Vazheha-ye Irani dar Zaban-e Engelisi, Bonyad-e Neyshabur 1364/1985
## Sanskrit / Hindustani
- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Not on archive.org. Also on ghaemiyeh (ghboo

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966:

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or g

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based lea
```


## [2026-10-17T00:31:07.572Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-558.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:5000])\"; command ls site/pages/565.jpg; sed -n '1,80p' tools/verify_check.py | head -80",
 "description": "View example output and checker"
}
```


### [2026-10-17T00:31:07.929Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Xac 1",
 "verdict": "plausible",
 "modern_form": "Skt. khac- 'shine through' (?) (Buck, after Uhlenbeck); modern view: Skt. kāca- probably a Nuristani loan, cognate with Skt. kāś- 'to shine'",
 "note": "The book files this chart under X because Nourai writes Skt. kh as X ('Xac' = Skt. khac-). The root and gloss come straight from Buck SYN 620, who gives it with a question mark: 'Skt. kāca- : khac- shine through (?). Uhlenbeck 51.' Wiktionary (after Mayrhofer) calls kāca- 'likely borrowed from a Nuristani language (*kāt's'a), cognate with Sanskrit kāś- to shine brightly'. Either way, a 'shining' root sits behind the glass word, so the chart is defensible, but the specific root khac- is uncertain. The extraction matches the printed page.",
 "note_fa": "نورایی ریشه را سنسکریت khac- «از درون درخشیدن» می‌گیرد (او kh سنسکریت را X می‌نویسد، از همین رو این مدخل زیر حرف X آمده). این ریشه را باک (SYN ص ۶۲۰) به پیروی از اولنبک، و خودش با علامت پرسش، آورده است. ویکی‌واژه به نقل از مایرهوفر سنسکریت kāca- «شیشه» را احتمالاً وام‌واژه‌ای از زبان‌های نورستانی (*kāt's'a) و هم‌ریشه با kāś- «درخشیدن» می‌داند. پس پیوند «شیشه» با ریشه‌ای به معنای درخشیدن پذیرفتنی است، اما خودِ ریشهٔ khac- قطعی نیست و ادعای نورایی را باید با احتیاط پذیرفت.",
 "sources": [
  "https://en.wiktionary.org/wiki/काच"
 ],
 "ref_check": [
  {
   "ref": "SYN:620",
   "status": "supports",
   "note": "SYN.txt (printed p. 620, section 9.74 GLASS), para 7: 'Skt. kāca- : khac- shine through (?). Uhlenbeck 51.' This is exactly Nourai's root and gloss, including Buck's hesitation."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "POK_full.txt grep 'kāca|kāś-|kāçat'",
   "stance": "silent",
   "note": "no Pokorny entry for Skt. kāca- or kāś-."
  },
  {
   "src": "WLD",
   "where": "WLD_Bd1/Bd2_pages.txt, WLD_band3.txt grep 'kāca'",
   "stance": "silent",
   "note": "no hit."
  },
  {
   "src": "AHD",
   "where": "AHD_watkins1985.txt",
   "stance": "silent",
   "note": "no IE root for Skt. kāca- (an Indo-Aryan word with no European cognates)."
  }
 ],
 "nodes": [
  {
   "id": 1,
   "lang": "Sanskrit",
   "words": "kâca",
   "verdict": "confirmed",
   "derivation": "Skt. kāca- m. 'glass, crystal, quartz' (classical, post-Vedic). Buck lists it as the Sanskrit word for GLASS and tentatively links it to khac- 'shine through'. Wiktionary instead suggests a Nuristani loan cognate with kāś- 'shine'. It continues in Pali kāca, Hindi kā̃c, Bengali kāc, Malay kaca. The gloss 'pearl' comes from Mo'in's BQT footnote, which cites Monier-Williams for 'شیشه، آبگینه، مروارید' (glass bead). The word and its sense 'glass' are secure.",
   "derivation_fa": "سنسکریت kāca- به معنای «شیشه، بلور، کوارتز» در سنسکریت کلاسیک به‌خوبی گواهی شده و در پالی kāca و هندی kā̃c (کانچ) و بنگالی kāc بازمانده است. باک آن را با تردید به ریشهٔ khac- «درخشیدن» می‌پیوندد و ویکی‌واژه آن را وامی از نورستانی می‌داند. معنای «مروارید» را معین در حاشیهٔ برهان قاطع به نقل از فرهنگ مونیر-ویلیامز آورده است (مهرهٔ شیشه‌ای). وجود واژه و معنای «شیشه» درست است.",
   "sources": [
    "https://en.wiktionary.org/wiki/काच"
   ],
   "ref_check": [
    {
     "ref": "SYN:620",
     "status": "supports",
     "note": "SYN p.620 GLASS table: 'Skt. kāca-'; para 7 'Skt. kāca- : khac- shine through (?)'."
    },
    {
     "ref": "BQT:1556",
     "status": "supports",
     "note": "BQT vol 3 p.1556 (pdf 349; vision file ocr/BQT/1556.vision.txt), footnote 9 to کاچ: 'قس: سانسکریت kâcá (شیشه، آبگینه، مروارید) «ویلیامز ۲:۲۶۸»'. Mo'in gives the Sanskrit word with these meanings."
    }
   ],
   "consulted": [
    {
     "src": "POK",
     "where": "POK_full.txt grep 'kāca'",
     "stance": "silent",
     "note": "not in Pokorny."
    },
    {
     "src": "WLD",
     "where": "WLD Bd1/Bd2 grep 'kāca'",
     "stance": "silent",
     "note": "not in Walde-Pokorny."
    },
    {
     "src": "SYN",
     "where": "p.620 §9.74",
     "stance": "supports",
     "note": "'Skt. kāca-' as the Sanskrit word for 'glass'."
    }
   ]
  },
  {
   "id": 2,
   "lang": "Persian",
   "words": "kâč; kâčî",
   "verdict": "plausible",
   "derivation": "NP kāč 'glass, ground glass' is a lexicographers' word. Jahangiri, quoted by Mo'in at BQT 1556, has 'کاچ آبگینه را گویند', and Borhan glosses it 'شیشهٔ صلایه کرده' (ground glass rubbed on pottery). Mo'in only compares it with Skt. kāca (قس), and Wiktionary treats the variant kāš 'glass' as 'likely borrowed from an Indo-Aryan language, probably Hindustani kā̃c, ultimately from Sanskrit kāca'. So kāč is a loan from Indic (with Indic c > Persian č), not an inherited word. kāčī 'thin glazed tile' (Jahangiri: 'brick or clay vessel on which glass has been poured') is equated by Mo'in with kāšī (Farhang: 'کاشی: کاچی، آجر لعاب‌دار'), and Wiktionary says kāšī is 'related to kāš glass'. The more usual explanation derives kāšī 'tile' from the city of Kāšān (Arabicised qāšānī; Mo'in's note at BQT 1568, after Qazvini). The book itself puts کاشی in parentheses beside kāčī, so the kāčī/kā
site/pages/565.jpg
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
            vnodes = {vn.get("id"): vn for vn in ve.get("nodes", [])}
            for n in e["nodes"]:
                vn = vnodes.get(n["id"])
                if vn is None:
                    problems.append(f"page {pg}: entry {i} ({e['root']['name']}) node #{n['id']} missing")
                    continue
                nv = vn.get("verdict")
                if nv not in VERDICTS:
                    problems.append(f"page {pg}: entry {i} node #{n['id']} verdict {nv!r} invalid")
                    continue
                nodes_done += 1
                tally[nv] += 1
                if not vn.get("derivation"):
                    problems.append(f"page {pg}: entry {i} node #{n['id']} has no derivation")
                if nv in ("disputed", "transcription_suspect"):
                    flagged.append((pg, e["root"]["name"], f"#{n['id']} {vn.get('words','')}", nv, vn.get("derivation", "")))
                for rc in vn.get("ref_check") or []:
                    ref_tally[rc.get("status")] += 1
                for c in vn.get("consulted") or []:
                    con_tally[c.get("stance")] += 1
```


## [2026-10-17T00:31:11.438Z] AGENT

Let me look at the printed page.


## [2026-10-17T00:31:11.782Z] TOOL CALL #7: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/565.jpg"
}
```


### [2026-10-17T00:31:11.816Z] TOOL RESULT

```

```


## [2026-10-17T00:31:19.666Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; \necho '## POK yeug'; grep -n -i -E '^ *(\\d+ *)?ieu-g|i̯eu-g|ieug-|i̯eug' POK_full.txt | head; grep -n -E 'iugum|yugá|yuga-' POK_full.txt | head -5\necho '## POK young'; grep -n -E 'iuu̯en|i̯uu̯en|iuven|yúvan|juvenis' POK_full.txt | head -8\necho '## AHD'; grep -n -i -E '^ *yeug|^ *yeu-|yeu-\\.|yeu-$|yewon|yuwen' AHD_watkins1985.txt | head -20",
 "description": "Grep Pokorny and AHD for roots"
}
```


### [2026-10-17T00:31:20.191Z] TOOL RESULT

```
## POK yeug
7318:from Latin iugum -/n. "a yoke' - a constellation in the southern night skies, see Root/ 
21033:awnord. driugr^ withstanding, strong, full', driugum^yery\ aschw. drygher^ respectable, 
## POK young
## AHD
274:aiw-. Vital force, life, long life, eternity; also “endowed with the acme of vital force, young.” 1. Extended form in Germanic *aiwi in: a. Old English a, ever: No}; b. Ger- manic *aiwi + *wihti, “ever a thing, anything” (*wihii-, thing; see wekti-), in Old English Gwiht, duht, anything, “ever a creature”: AUGHT!; c. Old English &fre (second element obscure), ever: EVER; EVERY, NEVER; d. Old Norse ei, ever: AYE?; NAY. 2. Suffixed form *ai-wo- in: a. Latin aevum, age, eternity: COEVAL, LONGEVITY, ME- DIEVAL, PRIMEVAL; b. suffixed form *aiwo-tdt- in Latin aetds (stem aetdt-), age: AGE; COETANEOUS; C. suffixed form *aiwo-terno- in Latin aeternus, eternal: ETERNAL; SEMPITERNAL. 3. Suffixed form *aiw-en- in Greek aidn, age, vital force: EON. See also *yuwwen- under yeu-. [Pok. aiu- 17.]
557:gyeu-. Also geu-. To chew. Germanic *kewwan in Old English céowan, to chew: CHEW. [Pok. g(iJeu- 400.]
993:spyeu-. Also speu. To spew, spit. Expressive root. 1. Germanic *spitjan in Old English spittan, to spit:
1195:yeu-. Vital force, youthful vigor. Earliest form *ayeu-; variant of aiw-. Suffixed zero-grade form *yuwen- (< *yu-sen-), “possessing youthful vigor,” young. 1. Further suffixed form *yuwn-ti- in Germanic *jugunthi-, *jugun- tha- in Old English geoguth, youth: YOUTH. 2. Further suffixed form *yuwn-ko- in: a. Germanic *juwungaz becoming *jungaz in (i) Old English geong, young: YOUNG (ii) Old High German jung, young: JUNKER (iii) compound *jung-fréw6-, young lady (see per’); b. Old Irish 6ac, Irish Gaelic 6g, in oglach, soldier: GALLOW- GLASS. 3. Latin iuvenis, young: JUNIOR, JUVENILE; JUVE- NOCRACY, REJUVENATE. [Pok. 3. ieu- 510.]
1198:yeug-. To join. I. Zero-grade form *yug-. 1. Suffixed form *yug-o- in: a. Germanic *yukam in Old English geoc, yoke: YOKE; b. Latin jugum, yoke: JUGATE, JUGULAR, JUGUM; CONJUGATE, SUBJUGATE; C. Greek zugon, yoke, and zugoun, to join: ZYGO-, ZYGOMA, -ZYGOUS; (AZY- GOUS), SYZYGY; d. Sanskrit yugam, yoke: YuGA. 2. Suf- fixed (superlative) form *yug-istos in Latin *jugistd (vid), “on a nearby (road),” contracted to juxtd, close by: JOUST; ADJUST, JUXTAPOSE, (JUXTAPOSITION). 3. Nasal- ized form *yu-n-g- in Latin jungere, to join: JOIN, JUNC- TION, JUNCTURE, JUNTA; ADJOIN, CONJOIN, (CONJUGAL), (CONJUNCT), ENJOIN, INJUNCTION, SUBJOIN. II. Suffixed form *yeug-mn in Greek zeugma, a bond: ZEUGMA. III. Suffixed o-grade form *youg-o- in Sanskrit yogah, union: YoGA. [Pok. 2. ieu- 508.]
```


## [2026-10-17T00:31:24.952Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 165 166 167; do echo \"### leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_02.txt | grep -n -i -E 'ieu|yug|iug|zug|juv|iuv|yuv|yaog|jung|joch|jugum|zeug|yoga|jung' | head -30; done",
 "description": "Locate Pokorny pages 508-510"
}
```


### [2026-10-17T00:31:25.295Z] TOOL RESULT

```
### leaf 165
13:I.  ieu-  , vermengen,  bei  der  Speisezubereitung'  {:  ieu-,  iö[u\-]   iu-,iü-]  letz- teres auf  Grund  der  Dehnstufen  oder  von  einer  schweren  Basis  *ieud-), ursprünglich  wohl  ,in  Bewegung  setzen';   s.  ieu-dh-, Ai.  yäuti,  yuvdti  ,vermengt',  ud-ä-yäuti  , rührt  auf^,  pra-yäuti  ,rührt  um', yUt
### leaf 166
12:.  ieu-,   ieuQ-,   ieu-g-  ^verbinden' ;    m-ti-   , Verbindung^,   ieugos-  n.  ,Ge,
13:spannS   ieug-ter-  ,Anschirrer^,  -iug-  ^geschirrt,  Gefährte^-   iu^o-zzj
14:n.  ,JocbS  iug-men-  ,Paarung,  Joch',  iug-ti-s  ^Anschirren',  i'ug'-W-
15:,angespannV ;  wohl  wie  1.  ieu-  ,vermengen'  aus  ,in  Bewegung  setzen'
16:entwickelt;   s.  auch  ieu-dh-  und  ieu-ni-.
17:Ai.  ydutij  yuvdti  ,bindet  an,  schirrt  an'  (auch  ,vermengt'),  Partiz.  yutd.^
### leaf 167
1: heit', geocian  ,bewahren,  retten'  vereinbar  ist;   s.  unten  4.  ieu-.
2:Specht  (KZ.  65,  207  f.,  68,  52  ff.)  stellt  juvare  zu  ai.  dvati^  worüber ölen  S.  77;  dagegen  M.  Leumann  Gl.  29,  173  f.
3:iu-go-m  ,Joch*:
4:ai.  yugd-  n.  ,Joch;  Paar'  (auch  ,Geschlecht,  Generation')  =
5:gr.  ^vyöv  ,Joch'  =
6:lat.  jugum  ds.  (siehe  auch  WH.  I  728  f.  über  umbr.  Iguvium)  ==
7:got.  asächs.  juk  n.,  ags.  geocj  anord.  ok  ,Joch',  ahd.  juch^  joch  ,Joch; auch  so  viel  Land,  als  man  mit  einem  Ochsengespann  an  einem  Tage pflügen  kann';
8:lit.  (mit  n  nach  jüngiu)  jüngas  ,  Joch' ;
9:aksl.  igo  (Gen.  iga)  ,Joch'  (es-St.),  Öech.  jho  ds.  (slav.  *jhgo  aus  "^ßgo, siehe  auch  Berneker  421  f.;  dazu  aruss.  ohbza  ,ein  Landmaß;  so  viel,  als ein  Mann  mit  einem  Pferde  pflügt'  aus  *ob-pgjä,  heute  obza  und  ohga- d.  j.  *oh-pga-  ,Deichselarme  des  Hakenpflugs';  ksl.  PL  izesa,  sloven.  Gen. i£^sa  mit  Nachwirkung  des  idg.  St.  Heugos-,  s.  unten);
10:cymr.  iau  f.,  acymr.  iom,  acorn.  ieu,  bret.  ieo,  geo  ,Joch',  kazelye,  kazelgi ,Knechtschaft' =  mcymr.  kesseyl-yeu  ,axillary  yoke'  (Loth  RC  40,  153 f.);
12:o-all.  PN  Ver-mgo-dumnus]  siehe  auch  Pedersen  KG.  I  98;  Thurneysen  lA. 26;  2Q  zweifelt,  an  der  Zugehörigkeit  des  ir.  und  Urverwandtschaft  des brit.  Wortes ;  unsicher  ist  auch  die  Beurteilung  von  ir.  cuing  , Joch' ;  nach Hessen  ZceltPh.  9,  39  vielleicht  aus  "^uing  {*iungis)  durch  Einfluß  der präpos.   com-]   dazu  mcjmr.  kyn-iwng  ,Vereinigung'   (Loth  RC  38,  160);
13:arm.  lue  ^JocV  zeugt,  nicht  für  ursprüngl.  Anlaut  1%-  der  Wz. ;  Einfluß von  lucanem  , spanne  aus^;
14:hitt.  i-ü-ga-an  (yugan)  ,Joch';
16:Ohne  geschichtlichen  Zusammenhang  untereinander  sind  ai.  yugald- n.  ,Paar';  lat.  jugulum  (Demin.)  ^Jochbein,  Schlüsselbein',  jugulae  , Stern- gürtel des  Orion',  und  gr.  ^evylTj  , Schlinge  im  Joch';  mit  hitt.  yugas ,jährig',  däyugas  ^zweijährige  vgl.  lit.  dveigys  ^zweijährige  {treigys  ,drei- jährig',  usw.),  oben  S.  229,  230.
17:ieu-gos-  es-St.:
18:gr.  rd  Csvyog  , Gespann',  PL  ^svysa  =  lat.  jügera  {^*iougesa),  wozu  ein neuer  Sg.  jügerum  ,ein  Morgen  Landes'  =  mhd.  jiuch  n.  ,Morgen  Landes', vgl.  auch  oben  ksl.  izesa,  ferner  vielleicht  (das  freilich  späte)  difyyrig  ,un- verhunden,  unvermählt',  sowie  lat.  iouxmenta,  iümentum  (s.  S.  510) ;  tief- stufig (wie  ätvyvjg,  das  aber  von  ^vyöv  aus  neugebildet  sein  kann)  wahr- scheinlich got.  juhuzi  f.  ,Joch,  Knechtschaft',  gegenüber  ags.  gycer  ,Joch' (*jukizi'),  mit  w  der  2.  Silbe  durch  Assimilation?
19:Verbalstamm  ieu-g-: •  ai.  yundkti  (3.  PL  yunjdnti  =  lat.  jungunt)^  yunjati  , schirrt  an,   spannt an,
```


## [2026-10-17T00:31:29.393Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==168' POK_02.txt | head -40; echo '### 169'; awk 'BEGIN{RS=\"\\f\"} NR==169' POK_02.txt | grep -n -i -E 'ieu|iuu|juv|yuv|jung|young|juh|yvan|yuvan|av\\.|jiwān' | head -20",
 "description": "Read Pokorny 509-510 pages"
}
```


### [2026-10-17T00:31:29.791Z] TOOL RESULT

```
 verbindet',  vgl.  vollstufig  yöjayati  (*jeugeieti)  ,fügt  zusammen';  av.  yaoj-^ yuj-  ,anspannen,  anschirren;  womit  vertraut  machen,  einer  Sache  teilhaftig machen' ;
gr.  ^svyWjXL  , schirre  an,  verbinde',  ^sv^ai  ^vyfjvac,
lat.  jungöj  -ere,  -nxi^  -nctus  ,verbinden';
vollstufig  ahd.  untar-jauhta  ,subjugavi';
lit.  jüngiuj  jüngti  ,verbinden,  ins  Joch  spannen';  Partiz.  ai.  yuktd-j  av yuxta-,  mit  dem  präs.  -n-  lat.  junctus,  ags.  geoht^  iukt  n.  ,Joch',  \ii.  jüngtas, mit  der  (wie  im  Präs.  aus  ^sr^at,  ^svyitrJQ  usw.  stammenden)  Hochstufe ^£i;xT(5s ;
Wurzelnomen  iug-  in:
ai.  yüj'  , Gefährte,  Genosse;  geschirrt,  bespannt  mit',  ayüj-  ,ohne  Ge- nossen, nicht  paarweise'  ==  gr.  ä'^v?  ,nicht  gejocht',  av^v^  ,zusammen- gekoppelt,  vereint^,  lat.  conjux . , Gatte,  Gattin' ;  Superl.  Hugistos  in  lat. juxtä  jdicht  daneben'  (*jugistä,  seil,  viä  ,auf  dem  nächst  verbindenden Wege') ;  in  den  starken  Kas.  analogisches  ai.  junj-,  lat.  conjunx.
510  f
Weitere  Ableitungen  in:
ai.  yöga-  m.  ,das  Anschirren,  Verbindung';  yögya-  m.  ,Zugtier',  vgl. anord.  eykr  ,Zugtier,  Pferd'  (germ.  *jaukiz,  vgl.  auch  Kaus.  "^jaukian' ^anschirren'  vorausgesetzt  durch  anord.  eykt  f.  ^Arbeitszeit  zwischen  den Mahlzeiten'  aus  *jaukipö)  =  lB.t  jügis  ^immerwährend ;  beständig  fließend' (daneben  iüges,  -itis  ,angespanntO;  ai.  yöjana-  n.  ,ein  Wegmaß',  av.  ywjas^i- f.  ds. ;  ai.  yukti-  f.  ,das  Anschirren',  gr.  tev^ig  ,das  Anschirren,  Verbinden', lat.  juncti-m,  juncti-ö,  vgl.  vom  es-St.  av.  yaöxUi-  ,Fertigkeit,  Fähigkeit, . Gewandtheit';  ai.  yöktdr-  ,Anschirrer',  yöktra-  n.  ,Strang,  Gurt',  av.  yaoocg^ dra-  n.  ,kriegerische  Anspannung,  Unternehmung,  Angriff',  gr.  ^sv7.TfJQsg , Jochriemen',  lat.  junctor,  junctüra-^  ai.  T/it^Tnan- , gepaart',  gr.  tevy^a  ,Zu- sammenjochung,  Joch',  lat.  jug{u)mentu7n  ,Pfosten,  Querbalken',  auf  Grund des  es-St.  dazu  alat.  iouxmenta,  klass.  iümentum  , Gespann'.
Vielleicht  mit  ieu-  verwandt  sind  auch  die  Sippen  iew(e)s- , Satzung' als ,Verbindlichkeit,  Bindung,  Fug'  und  ws-  ,gürten'  als  *iö[u}s-.
WP.  I  201  f.,  WH.  I
### 169
2:5.  ieu-  ,jung'.  Positiv  iuuen-  (:  iün-),  Kompar.  ieu-ios.
3:Ai.  yüvan-  (yuvä,  Gen.  yünah)  ,jung;  Jüngling',  f.  yünly  Komp.  Sup. ydviyas-,  ydvista-h ;  av.  yvan-,  yavan-  (beides  für  yuvan-  geschrieben),  Gen. yünö  ,Jüngling';
4:Isit.  juvenis  ,jung;  Jüngling,  Jungfrau'  (zu  -ven-  statt  -vin-  vgl.  EM^  509) statt  *iuud  auf  Grund  der  alten  kons.  Kasus  Gen.  juven-is.  Dat.  -z,  Akk.  -em usw.;  jürii-x  ,junge  Kuh'  lat.  -c-Erw.  neben  ai.  yünlj  dagegen  Komp. junior  mit  jungem  jün-  (durch  lat.  Entw.  aus  *juvemos) ;  umbr.  louies ,juvenibus,  militibus',  Akk.  PI.  jovie  (ein  vom  Komp.  rückgebildetes  *jovie-8 ,Schar  der  juniores'?);
5:air.  öa  Jünger',  öam  ,jüngst',  mcjmr.  ieu  (ncymr.  iau)  ,jünger*,  ieuaf (so  auch  ncymr.)  ,jüngst',  bret.  iaou  .jünger',  woneben  der  Positiv  air. öac  (arch.  oec),  mir.  öc,  cymr.  ieuanc,  bret.  iaouank^  acorn.  iouenCy  mcorn. yowynk  ,jung',  gall.  Jovinc-iUus,  -a  (idg.  *iuunkösj  s.  unten),  nach  dem Komp.-Sup.  zu  kelt.  *if'U-,  *iounko-  umvokalisiert ;
6:lit.  jdunas,  lett.  jaüns;  abg.  jum  ,jung'  (-«o-St.  statt -n-St.  nach  *seno-8 ,alt';  iuueno-  nach  dem  Kompar.  umgestellt  zu  *ieueno-j  bsl.  *iöunO').
7:Ableitungen  vom  St.  *  iuuen-:
8:i^li^^^'^'  ^i-  yuvaSd-h,  yuvakd-h  ,jugendlich',  lat.  juvencuSj  -a  ,junger Stier,  junge  Kuh,  Junges',  umbr.  iveka,  iuenga  ,juvenca',  got.  juggSj  aisl. ungvj  ahd.  jung,  ags.  geong  ,jung'  (urg.  *jüngaz  aus  *juwungdz ;  dazu  ein   ^ neuer  Komp.  *jünh{zan-  in:)  got.  jükiza,  aisl.  ere  ,jünger'  (vgl.  auch  aisl. eska  , Jugend'  aus  *jii[n]Äi5Äön-).
10:iuuent-,  iuunt-:  ai.  yüvant-j  i.  yuvati-lj,  ,jung;  Jungfrau';  shdi.  jugundj as.  jugud,  ags.  geogud  (g  statt  w  nach  *duzunpi-  ^Tugendj  Tüchtigkeit'), got.  junda  ^Jugend'  (*iuunta) ;  lat.  Juventus,  -tütis  , Jugend'  (jüventa  =  got. junda?)  =  air.  öetiu,  öitiu,  Gen.  -ted  ^Jugend'  {^iountüt-Sj  umgebildet  aus iuui}tüt-j  s.  oben  zu  öac).
11:Eine  s-Erw.  wahrscheinlich  in  ai.  yösä,  Gen.  *yösndh,  N.  PI.  yösüh,  yö?andh junges,  zum  Liebesgenuß  geeignetes  Weib,  Gattin';  für  lat.  Jünö,  w
```


## [2026-10-17T00:31:35.759Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'yuvaś|yuvas|yuvan|yavan' KLN_1966.txt | head; echo ---; grep -n -E '^young|^yoke|^yoga|^join|^juvenile|^junior|^adjust|^conjugate|^zygo' KLN_1966.txt | head -20",
 "description": "Grep Klein for young and yoke entries"
}
```


### [2026-10-17T00:31:36.197Z] TOOL RESULT

```
19864:Ionian,  adj.  and  n.  —  Formed  with  suff.  -an  fr. L.  Ionius,  fr.  Gk.’Idmoi;,  ‘Ionian’,  fr.’Tcav  (gen. Tcovoe),  contraction  of  Titov  (gen.  Taovo^), ‘Ionian’,  fr.  orig.  *TiFtov,  whence  Heb.  Yawdn, Akkad.  Iamanu,  Idvanu,  Egypt.  Yfvana,  Y*- vanna,  ‘Greek’.  Cp.  also  OI.  Yavanah,  OPers. Yauna,  ‘Greek’,  OI.  yavanika,  ‘Greek  woman’; ‘curtain  (in  the  theater)’,  lit.  ‘Greek  (partition)’. Ionic,  adj.  —  L.  lonicus,  fr.  Gk.  Ttov.xic,  ‘Ionic’, fr.  Tov.  See  prec.  word  and  -ic. ionium,  n.,  a  radioactive  element  pertaining  to the  uranium  group  (chem)  —  ModL.,  formed fr.  ion  with  suff.  -ium;  so  called  in  allusion  to its  ionizing  power.
---
1646:adjust,  tr.  v.,  1)  to  settle,  arrange;  2)  to  fit  exact¬ ly.  —  Fr.  earlier  F.  adjuster  (corresponding  to  F. ajuster),  fr.  ML.  adjustare,  fr.  Late  L.  adjuxtdre, ‘to  bring  near’,  fr.  ad-  and  L.  juxta,  ‘near’.  See joust,  v.,  and  cp.  juxta-.
8756:conjugate,  tr.  and  intr.  v.  —  L.  conjugatus,  pp.  of conjugdre,  ‘to  join  together,  unite’,  fr.  con-  and jugare,  ‘to  join;  to  yoke;  to  marry’,  which  is rel.  to  jugum,  ‘yoke’ ,  jungere,  ‘to  join’.  See  join and  verbal  suff.  -ate  and  cp.  jugate.  Cp.  also conjoin.
8757:conjugate,  adj.  —  L.  conjugatus,  pp.  of  conjugdre. See  conjugate,  v.
20317:joint
20345:join,  tr.  and  intr.  v.  —  ME.  joinen,  fr.  OF. (=  F.)  join-,  joign-,  stem  of  joindre,  ‘to join’,  fr.  L.  jungere,  ‘to  join,  unite’,  which  is cogn.  with  OI.  yundkti,  ‘he  harnesses’,  yuktdh, ‘harnessed’,  Gk.  ^euyvuvai,  ‘to  yoke,  har¬ ness’,  Avestic  yaoj-,  yuj-,  ‘I  harness’,  yuxta-, ‘harnessed’,  Lith.  jiingiu,  jungti,  ‘to  yoke’.  All these  words  are  dervatives  of  I.-E.  base  *yeug-, ‘to  join,  unite’,  enlargement  of  base  *yeu-,  of s.m.,  whence  OI.  yduti,  yuvdti,  ‘he  harnesses’. See  yoke  and  cp.  adjoin,  adjunct,  conjoin,  con¬ joint,  conjugal,  conjugate,  conjugation,  conjunct, disjoin,  disjoint,  disjunct,  injunction,  jostle,  joust, Jugatinus,  jugular,  jugulate,  junction,  juncture, junta,  junto,  juxta-,  rejoin,  rejoinder,  subjoin, subjugate,  subjunctive,  and  the  second  element in  quadriga.  For  a  special  jse  of  base  *yeu-  in the  sense  ‘to  mix’,  see  juice  and  cp.  jube. Derivatives:  join-ing,  verbal  n.,  and  adj.,  join¬ ing -ly,  adv.
20346:joinder,  n.,  the  act  of  joining  (taw).  —  F.  joindre, ‘to  join’  (fr.  L.  jungere),  used  as  a  noun;  see join.  For  the  subst.  use  of  infinitives  in  law terms  see  attainder.  Cp.  rejoinder, joiner,  n.  ME.  joynour,  fr.  OF.  joigneor,  fr. joigner  (F.  joindre),  ‘to  join'.  See  join  and  agen¬ tial  suff.  -er.
20348:joint,  n.  —  OF.  (=  F.)  joint,  ‘a  joint’,  fr.  joint, pp.  of  joindre.  See  joint,  adj.
20350:joint
20351:joint,  adj.  —  OF.  (=  F.),  ‘joined’,  fr.  F.junctus, po.  of  jungere,  ‘to  join’.  See  join  and  cp.  prec. word.
20508:juvenile,  adj.,  young,  youthful.  —  F.  juvenile, ‘youthful’,  fr.  L.  juvenilis ,  ‘youthful’,  fr.  juvenis , ‘young  man’.  See  young  and  -lie  and  cp.  Juven- tas,  rejuvenate.  Cp.  also  junior,  Juno,  Evan. Derivatives:  juvenile-ly,  adv.,  juvenile-ness ,  n., juvenil-ity,  n.
20510:join  and  cp.  next  word.  Cp.  also  jostle,  joust, adjust.
```


## [2026-10-17T00:31:40.445Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^(young|yoke|yoga|junior|youth),? ' KLN_1966.txt | head; grep -n -E 'yuva|yuvan' KLN_1966.txt KLN_1971.txt | head",
 "description": "Grep Klein young/yoke/yoga"
}
```


### [2026-10-17T00:31:40.815Z] TOOL RESULT

```
20775:youth,  servant’,  MHG.,  G.  knabe,  ‘boy,  lad’,  assembly’).
KLN_1971.txt:17429:8 eixt6 ^, verbal adj. of AmaScixyuvaL, ‘to show 
KLN_1971.txt:107788:apartment’, prop. neut. of the adjective yuvat- 
KLN_1971.txt:107790:minine,’ used as a noun, fr. yuvir], gen. yuvaixos;, 
KLN_1971.txt:107797:Gk. yuvavSpot;, ‘of doubtful sex’, fr. yuvT), 
KLN_1971.txt:107809:meaning ‘woman’. — Gk. yuvaixo-, yuvaix-, 
KLN_1971.txt:107819:woman or women. — Gk. yuvat.xoxpaT(a, com- 
KLN_1971.txt:119758:yuvaixeltx (female genitals), possibly also with 
KLN_1971.txt:270057:OI. yuvasdh, ‘youthful; young man, youth’, OIr. 
KLN_1971.txt:270061:*yeu-, ‘young’, whence OI. yuva, yuvan-, ‘young ; 
KLN_1966.txt:16936:—  L.  gynaeceum,  fr.  Gk.  yovatxEtov,  ‘women’s apartment’,  prop.  neut.  of  the  adjective  yuvat- xciop,  ‘pertaining  to  a  woman;  womanly,  fe¬ minine,’  used  as  a  noun,  fr.  yuvi rj,  gen.  yuvatxo?, ‘woman’.  See  gyneco-.
```


## [2026-10-17T00:31:45.413Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '270040,270075p' KLN_1971.txt; grep -n -E '^yoke|^yoga' KLN_1971.txt | head",
 "description": "Read Klein 1971 young entry"
}
```


### [2026-10-17T00:31:45.927Z] TOOL RESULT

```
(used as dat. and acc. of gi, ge, ‘ye’), OFris. 
iuwe, iwe (used as dat. and acc. of gi, ‘ye’), MDu. 
u (used as dat. and acc. of gi, ge, ‘ye’), Du. u 
(used as dat. and acc. of gij, ‘ye’), OHG., MHG. 
iu (used as dat. of ir , ‘ye’), OHG. iuwih, MHG. 
iuwich, iuch (used as acc. of ir, ‘ye’), G. euch 
(used as dat. and acc. of ihr, ‘ye’), Goth, izwis 
(used as dat. and acc. of jus, ‘ye’). See ye, pron., 
and cp. your. 

young, adj. — ME. yung , yong, fr. OE. geong, rel. 
to OS., OFris. jung, ON. ungr, Dan., Swed. ung, 
MDu. jonc, Du. jong, OHG. jung, MHG. junc, 
G. jung, Goth, juggs, ‘yong’, and cogn. with L. 
juvencus, ‘a young bullock ; a young man 5 , ju- 
venca, ‘a young cow; a young woman’, Umbr. 
iveka [corresponding to L . ju(v)e(n)ca\, ‘herfer, 
OI. yuvasdh, ‘youthful; young man, youth’, OIr. 
oac, Mir. oc, W. ieuanc, Co. iouenc, iunc, Bret. 
yaouank , ‘young’; fr. I.-E. *yuwnkos, a deriva- 
tive of *yuwn-, which is an enlargement of base 
*yeu-, ‘young’, whence OI. yuva, yuvan-, ‘young ; 
young man, youth’, Avestic yvan- (gen. yun-d), 
‘young man’, L. juvenis, ‘young; young man’, 
OIr. da, dam, ‘younger, youngest’, MW. ieu , 
Bret., iaou, ‘younger’, W. ieuaf, ‘youngest’, 
OSlav, junu, Lith. jaunas , Lett, jauns , ‘young’. 
Cp. youngster, younker, youth, the first element 



in euphroe and the second element in galloglass. 
Cp. also juvenile and words there referred 
to. 

Derivatives: young, n., young-ish, adj. 
235332:yoke and cp. jugate. 
269907:yoga, n. (Hindu philos.) — OI. ydga-, ‘a yoking, 
269909:yoke and cp. Yuga. 
269930:yoke, n. — ME. yok, fr. OE. geoc , rel. to OS. juk , 
269947:yokel, n., rustic, countryman. — Of uncertain
```


## [2026-10-17T00:31:55.809Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 577 1228 2458; do echo \"######## BQT:$p\"; python3 tools/ref_page.py BQT:$p 2>&1 | head -80; done",
 "description": "Fetch BQT cited pages",
 "timeout": 300000
}
```


### [2026-10-17T00:32:07.459Z] TOOL RESULT

```
######## BQT:577
no scan of BQT covers printed page 577 (see 'scans' in refs_online.json)
######## BQT:1228
REF: BQT:1228  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 19  OCR-lang: fas

شاکمونی -۱۲۲۸-
خوانند - بجهت طلبی که از دیگری دارد بگیرند - و بر
شا کمونی ۱ با میم‌بواو رسیدم‌ونون ۳ داروصان خاطران و پیاده وان را یز
بتحتان ی کشیده » باعتقاد کفرء هند پیغمبرصاحب ۹ و کلیمی‌رانیز گفته‌اند که درزیرفرشها
ند ۰
کتاب است وعیچ کس بر اسرار او واقف یات ۱ "1۶ ی 0
و در ولادت و وجود ارو خرق عادات و خرافات لنگی ۳ بفتح ثالث بر وزان
ببارگویند وکتاب او را نیزا کموبی خواد, | نازنگی » رسمان تابنده و موتاب راکوبندوآن
۰ ۰ .. امه ۰ ۰
ری گوبند پیغمبر احل خطاست. ۸ شخصی باش د که ججهت یمه : آن رسمان
۲1۸ بتابد و آلرا بعریی لواف خوانند ۷ .
ل هم » مدیراگوش که از به
نقطه دار (۱) پر فبتان بن ارفخشد پن سام برد ص ۳
۲ هه اس * ث ) بز مالند نه از پشم کوسفند .
۰ ع ۰ رعا ۰
لوح است وعابریر اوست, وعبری آزعایرمشنق
است . شالهنگ - بنتم ثالث و ها بر وزن
پالهنگه ۰ بمعة گان باشد و آنرا
شالده ۴ (۲) - بسکرن لام وافتح ۹ پعمتی کرو و کرو ن باشد و لو
بعربی رهن و مرهون خوانند - و بمعنی زبادتی
کوبند ۴ . ومکر وفریب وحیله را نیز کوبند.
(۷) چك : وسکون خا . ()چك » چش : شال ده. (۳)خم۱ : شالنکی.

. ‏حساکیامونی . شهرستانی در ملل وتحل (س۸*۰؟۲) نام او را «شاکیمن»ضبط کرده‎ ٩
‏ر4: بودا - ۴ <- علح (یکراول وفتح دوم) ات 66 : *سام بعداز تولید نمودنش‎
‏چاپ‌لندن ۱۸۹۹م. سفرنکوین آیه‌های ۱۲-۱۱ .۰ ۴ - درزبان کنونی «شالوده»‎

فرهنگه شیرازی. «فرهنکه نظام» .

6 قی : فشگه . ‎٩‏ - رد4 : عال .

غضایری رازی. «جهانگیری» . ۰ بمعلی‌س رکش «جهانگیری» ([غاهد درح۷آمده).

* شال-از فارسی وارد عری‌شده *شال» «تفی» و ازعربی وارد فرانوی 216]لاروس

زآن مثل حال من بگشت و بتات که کسی شال جت ودیبا یاف >.

« لغت فرص ۰.6۳۱۷

- نیز پارچه‌ا ی که دورکمر با کردن پیچند .

######## BQT:2458
(no exact page map; using offset -1917 -> pdf page 541; check the printed number and re-run with --pdf-page if off)
REF: BQT:2458  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 541  OCR-lang: fas

توسف زرین رسن مخ
یوسف زرین دسن - بممنی‌پوسف | وغین نقطد دار . چوبی باشد که برکردن کاو
روز است که کنایه ازآفتاب عالمتاب باشد. زرامت و کاو کردون رم ۱
و گذارند . 5 رو سای
یوسف زییق نقاب - کنای+ از | روووم ۹
پوسف‌گ رک ی ۱ اولوسکون‌تای دکاف»
هست ‌- ۰ ار ۰
و | سیخ آهنی را کوبند بوغ
شاهد ومحبوب ومطلوب باشد . که بر بالای تنور نهند و بربالرا برآن سیخ
کردن باشد . چیزی باشد ماد گرد بالشی از لئه دوخته که
ارة درود کربر| کوبند . ۳ بواد
۸ بو گان؟ « با کاف فارسی بالف. کشنده
بوش؟ * باانی مجهول بروزن‌موش, :. 4 1 0
: بروزن بونان, بجه‌دان ومديمه آدمی وحیوانات
تفحص ونج ی کردن وجتجولمودن باشد . دیگر باشد - و رودة پاك نکردء کوسفند را نیز
پوع؟ - بنم اول وسکون‌انی مجهول | کویند .
‎٩‏ - بیوسه ببرند چوب سکند
که تا (کزان) پای خولی درآرد (چوبین درآید) به اد .
اسدی طوسی«لغت فرس ص۵۰۶ «رشیدی».
۴ سبوز (هم.) ۴ <جوغ (۸م.) ۳ جغ ۳ جوه* جوخ ۳ جو , اففانی ع
ناژ (بوغ کاوآهن) «هوبشمان 4۲۳»؛ سانکریت- 9888 ۰ بلوچی 0812[ «هوبدمان‌ش 4۱۰۷
ازربشه اوستایی 3808 (اسب را بگردونه بتن) «یارتوامه ۲۹-۱۲۲۸:
همی گفت با اوکزاف و دروغ مگر کاندرآرد سرش را بیوغ.
بوشکور بلخی «لغت فری‌س ۲۲۹
«آعنی باشد که برزبر تنورنپند وبربان را ازآن آویزند وآنرا بلك نی ز کویند. » «جهانگیری»
ورك: رشیدی . 8 _- درلغت فرس مصحح اقبال ص۳۵۹ آمده : ‎٩‏ بوکان ( با باه موحده )
رحم بود بعنی زهدان. کسائی (مروزی) کوبد:
وزین هم ه که بگنتم اصیب روزبزر که غدود وزهره وس ر کین وخون بوکا ن کن.
ابوالعبای کوید :
رش چون بوکانا سبلت چون سوهانی سر بینیش چو بورای باننگانا .>
(با باو فارسی)؛ زهدان ,مای رحم . درنشةٌ نی : پوکان ( با بای مثناة تحتانی ) زهدان باشد
وبتازی رحم کوبند» وبپارسی رودء کوسفند که سر کین درش باشد . ( لغت فرس مصحح اقبال ص
```


## [2026-10-17T00:32:13.584Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls data/verification/sources/refs/ocr/BQT/ | grep -E '^(2458|1228)'",
 "description": "Find cached BQT page images"
}
```


### [2026-10-17T00:32:14.067Z] TOOL RESULT

```
1228.png
1228.txt
2458.png
2458.txt
```


## [2026-10-17T00:32:16.499Z] TOOL CALL #16: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2458.png"
}
```


### [2026-10-17T00:32:17.013Z] TOOL RESULT

```

```


## [2026-10-17T00:32:17.009Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-17T00:32:27.035Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; cat > 2458.vision.txt <<'EOF'\n[BQT p. 2458, vol 4 pdf page 541 — read from the page image by claude-opus-5.5 for page-565 verification]\nیوغ ۳ - بضم اول و سکون ثانی مجهول و غین نقطه دار، چوبی باشد که برگردن گاو زراعت و گاو گردون گذارند.\nFootnote 3: ۳ - = جوغ (هـ.م.) = جغ = جوه = جوخ = جو ، افغانی jugh (یوغ گاوآهن) «هوبشمان ۴۲۳»؛ سانسکریت yôga (sic) ، بلوچی jôgh «هوبشمان ص۱۰۷» ازریشهٔ اوستایی yaog (اسب را بگردونه بستن) «بارتولمه ۱۲۲۸-۲۹»:\nهمی گفت با او گزاف و دروغ - مگر کاندرآرد سرش را بیوغ. بوشکور بلخی «لغت فرس ص۲۲۹».\nEOF\ncd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'جفت' BQT_v1_pages.txt BQT_v2_pages.txt | head -5; grep -n 'جغ' BQT_v2_pages.txt | head -5",
 "description": "Save vision file; grep BQT for joft"
}
```


### [2026-10-17T00:32:27.378Z] TOOL RESULT

```
BQT_v1_pages.txt:3242:۱ موّلف کلمةه چاو» را که چینی‌امت نام«جفتای» باد کرده است. ‏ ۷- راد: ص‌شش
BQT_v1_pages.txt:3627:حرنر کی ۰ است. جفتابی 6۲4۱ . ركك: مثن برهان: تومن.
BQT_v1_pages.txt:4467:مأخذ اروپایی (-جفتایی).
BQT_v1_pages.txt:4608:(جفتایی ) ۰ ۷6۱006016( .وزعدظ
BQT_v1_pages.txt:8363:را بدان میخوانده « لفث جفتابی و تر کی عثمانی جح ۱ ص ۱۶ > « عاث اللفات » و ححنی
47: ‫علوی (محمدحن)؛ دبیرتاریخ وجغرافیای دبیرستانهای تهران ( لغات کازرونی‬
138: ‫اببهرء جغرافیابی ستاد ارتش(ابران)‪.‬تپران‬
568:  ‫بار وله‬        ‫‪2‬‬        ‫اوت ‪-‬‬     ‫شيخ جام است ‪ « .‬جغرافیای سیاسی ‪ .‬کنهان ‪٩ ۹۹۱ ۰۰‬‏ ‪۴ ۰‬‬
1032: ‫بتقدیم غین بر حرف الی هم هت که جغبوت‬
1434:   ‫‏‪« - ٩‬فشافوبه» دراوحی باره دبه است‪ :‬کوشك و علیاباد کویلین و جرم ‪ « »...‬جغرافیای‬
```


## [2026-10-17T00:32:32.692Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'juxt|yuxt|ĵuxt|jaft|jo\\b' BQT_v1.txt BQT_v2.txt BQT_v2_pages.txt | head -10; grep -n -i -E 'yuxta|yaog|yuj' BRT.txt | head -10",
 "description": "Grep BQT and Bartholomae for joft/yaog"
}
```


### [2026-10-17T00:32:33.101Z] TOOL RESULT

```
BQT_v2_pages.txt:6127: ‫از‏‪۲:۱ lal» (caftan?)jaftan .caftîdhan:‬‬           ‫‪۵‬‬          ‫کوسفندان‌است‪ .‬رکد‪ :‬ج ‪. ۲‬‬
BQT_v2.txt:2878:بگردونه بتن). بهلوی)] لا (انحاد, زوح)» ارمنی ع juxtak‏ (زوج)»هندی باستان_ 4 )نال. 
BQT_v2.txt:9788:lal» (caftan?)jaftan .caftîdhan :‏ ۲:۱ 
2909:I      Zum  ai.V.  H^aft' 'er rückt' I).  —  'S ^. paifyaog^t.
3372:ainim  ag^rapaitiot  (sd.)  üpshöit  '>a  >. Um  aivdi:a  tüirim  T^.ii; — yujyastis  haca *nmanat    "'ha    \daniuil]     visal     Aa'ir»m *zaiUao]  *'%a  •>   *daMaot  N.  8;  ioS\  Yt. JT.3; —  dvaiibya  Aaca  mnbya  dva  nara
4208:•  j.  ana,  p.  anä  Praen. 'über  — hin';  i)  mit Akk.,  a)  'über—  hin':  yat  vlspanqm  yuxta- nqm  az>m  fratsmsm  "^anjaymi  (sd.)  "</ *car>tqm  yqm  daryyqm  ". .  über  die  lange Rennbahn  hin"  Yt5.so'>.  b)  'entlang, längs';  "a  til  vai'Am{&i..)  ayii  °a  bititn  °a 'iritXm  V.  5.  5.         c)  'auf',  auf  die  Frage
4575:•  j.  'an'tara-  Adj.  'der  innere,  innen  be- findlich': 'r^m  ür^Mfii  nmanahe  "ins  Innere des  Hauses"  V.6'.43;  —  'rat  W.  2.^0 PüZ.  a)  'rat  naimax  'innerhalb',  mit folg.  1)  Gen.,  z)  Lok.,  3)  Instr.,  4)  Akk., uzw.  a)  räumlich,  b)  zeitlich:"  1  a)  a'  n- hsirake  N.  Go;  104';  —  *a'  n°  *yujyastHs N.  -ji  T'*j  —  a'  W  aEi3.drajahyehe  N. Ii()',  —  a'  n°  '^rigämyt/ie  N. 65.  1  b)  a- II'  tiava.xsaparahe  V.  5. 43.  !  a)  a'  11° barj''irisi'a  y.^.^i.  3  a)  a'  n'  brrat.- byqm  V.  Ä41,  42,  g.  15,  16.  4  a)  a' tr  aSe  pa>a  "auf  diesen  Wegen"  V.  8. 104.  4b)  a°  11°  triilzär.ljaAlm'V.^.^y, —  a-  n' yanJräßV.O.a,  3,  7.77.  Tai fialinät  N.^.^3).  Ta  N.JOi(?);  —  'nm N.pj(?).
4836:•  Ji  g-  '^Y'  subst  Fron,  dem.,  nur  enkL Akk.  mask.  und  neutr.'*,  'ihn,  es;  sie', hinter  dem  ersten  (hochtonigen)  Wort  des Satz-  und  Versteils'*;  i)  zurückweisend, a)  auf  ein  Nomen:  atjhiuS  ,  ,  yS  im  dät Y.45.4;  —  mq>r)7n  ..ya^ä  Tm  mlnätHä vaocacä  Y. 43.3;  —  yastat  .  .  yi  .  .  ku tSin . .  *maimS  atihal  paouruyi  vTdvä  avatn yn  im  anhat  ap^mii  (sA.)  Y. 44.1g;  — yS,.dasdi  *a!na»iAi  tiöit  ahyä .. paityaogit (sd.)  ta  akmai  JasSit  . .  ya  im  pmySl  Y. 46,%;  5/.12  (valpys),  46.^{ayaiit^m),  ig. i2f.J  (a/iurym)i  —  vahistim  %wa..yäs3 . .  f»rala6str3i  maibyacd  yaiibyas^ä  J?  ri- aha^m  Y.2ÄS;  4j.  10  {ahm),  J5.6} {vohs);  —  nä  zil  ^almainX  vyädamtm vatfhSuS  mainySus  iyao^anahyä  tixfiahyScS "denn  nun  will  ich  es  (xla'i:r?m)  mit  dem Auge  erschauen,  (das  Reich)  des  guten Gedankens,  Werks  undWotts"  Y.4$.Z^^; —  aya  nStt  3r?s  vlsyätä  daivännä  hyat if  ä.dfbaoma  {sä.)  ..  ups.jasat  Y.jo.6; 31.1&  idr?gvatS),  32.1$  (maraxtJrff),  44, 4  {drggvasa),  46.  12  {naptyai^ü),  31.  14 {karapans),  ^.8  {duivarMai^hö),  33.9 {duivar?näi/)i   —    slU^fnf  . .  mraeml . .
5724:•  j-t  E-  (.  P-)  asan-iaj«-,  j.,  p.  asman-  m." i)  'Stein':  *ja«s(alsAP.)  äi/i{sd.)  maya  äiti darSii"V.g.  11;  —  'sSnaShia'^ ..  vtHiaeh-a' . .  tBiuxha  (sd.)  V,  6. 5 1,  a)  als  Amulet: °samm  *siyaire.ci^rim  (sd.)  abars  *aAurö.- puirS  (sd.)  Yl;4.59-  b)  als  Waffe, 'Schleuderstein,  Steingeschoss':  Uavasca  . . •sanas(a  . .  (NP.)  fraäaxlaitya  V.  Z7.9;  — karjtS  .  .  vazrö .  .  'sänS  atymSJütä  Yt.  JJ. 72;  /.18;  —  jainti  mqm  ahuna  vairya avavata  snai^isa  ya'^a  'sma  iatS.masa (sd.)  Yt/7.20;  —  'sanS  (als  AP.)  tasia drazimnS  katä-masatiks  Aynti  V,  117.43); —  yahmai  .  .  aurvan/a  *yuxta  vJsa %an/asante  (sd.)  .  .  asUnas/a  (als  AP.) vispeMvia  "dem  .  .  die  Renner  am  ge- schirrten Wagen   ziehen  -  .  und  die  all-
6064:I  (sd.)  didqs  dngväta  hyat  dalnh  vahiÜi ^yüjsn  (sd.)  mxMi  'sd  yuxta  (sd.)  Y.^^. 9;  —  yä  masyä  acista  datUS  .  .  var?hSus '  slsdyamna  (sd.)  manat>AS  masda  ahu- '  r&hyä  xralius  tiasyantö  (sd.)  'iSatcä  Y. 32./^;  —  tkalsS  drjguä  ..  'sät  ramsH (sd.) Y.  4ff.  2 ;  —  ayi  *niainivä  varatil  (sd.) yS  drfgvä  aciltä  vmzyS  'i>m  mainyui' spini/ts  Y.30.  5;  —  tSng . .  ySng  'lahyä vazdrSng..  Y.46.4;  —  roAü  AvS  xs'a^rit '/im.,  hapn  (sd.)  Y.jr.  2z;  —  hvö  cistf uxlai/  /yadiianS  daSta  'hm  spSnvat  (sd.) Y.JJ.  21;  — yä  'iai  ha/äjvamaAl  (%d)Y.
6396:•  j.  a^samnö.gan-   Adj.   'das  Ziel  nicht  den  ganzen  M.   in   sich  fassende  As3m~ treffend":    karptaUt    altqm    hufräyuxta  ..Gebet  bekannt  wurde"  Yt. /^.  91.
6980:•  j.  a-x*asta-  Adj.  *nicht  gedroschen':  *!i  stllY.43.z\ — yakmya  3p5..^waxs3iite altavat  ifastaiiqm  (sd.)  aSavat  'tanqm  *3  iskafymT^  pouruttm^a  Yt/O.  14;  — {yavanqm)  V.  7,35.  paityaogit  (sd.)  ta  akmai  jassit . .  iaurSui
7035:yeü,  ß)  vorausgehendem  yen  'Svenn  aber, wenn  jedoch",  kondiz.:  a)  *yujyastis  hala *nmä>tat  . .  a°  yat  he  aoxte  .  .  dka  *hä *x!ayae  .  .  haxtöit{%A.)  N.A'f.;  V.7.3 äat  (s.  ?•)  yg  .  .  upairi  hunarain  (sd.)  maiiü barst  .  .  J'  yaj  .  .  faiti  barät  aat  (s.  z) yat  .  .  ava  baraite  "wer  .  .  aber  wenn  er .  .    und    wenn    er    .  ."    P.^jjf.;    —  yezi
```


## [2026-10-17T00:32:38.045Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '2870,2885p' BQT_v2.txt; echo; grep -n -E '^ *[•.]? *j?\\.? *yaog-|yaog- *V|^.{0,10}yaog' BRT.txt | head -5; grep -n -E 'yvan|yavan-|yuvan' BRT.txt | head -5",
 "description": "Read BQT joft footnote and BRT entries"
}
```


### [2026-10-17T00:32:39.322Z] TOOL RESULT

```
بگردونه بتن). بهلوی)] لا (انحاد, زوح)» ارمنی ع juxtak‏ (زوج)»هندی باستان_ 4 )نال. 


کردی 0154 . 46[ ( عاربه ازجفت) "افتانی؟؟نلا (نمام.درست) » بلوچی ع ]لا «اسشق 


.44 2 


20927:yaog-
21838:Zum  V.  yaog-,  —  ai.  vgl-  yuktay-  f.  —  Pü-  (lu F.):  äyBosn,  (luY.);  mä  bav/ arvandän  Sydxlär (lies  'xtan).  —  ')  Vgl.  zKonstr,  Bthl.  IF.  io, iSg  und  joii^  K.
21849:Zum  V.  yaog-  (FPfP.  mit  iha-,  %  sog.  8).  — Npfl.  r  äyüxtäi;  erl. :  ßs  raflär.  —  1)  Gdn.  3Yt. 65;  'kampfbereit',  Dst.  ZA.  2.  566:  'rapide'.
21006:Pü.  1  j*.!/  äySlär,  erl. :  »"fl/  ayu/Jr/A  und  lorait'i JaVil;  Tgl.  'j-iK*-  No.  1.  —  ')  Denkbar  wäre auch  yaoiiö^aal'  (vgl.  mmaj^anl-  nnd  raßnö.- Hya^  Ableit  aus  'yaanah-.  Die  Bedeutung bleibt  auch  so  dunkel. j.  yaenüya:  s.  yavan-
21340:•  j.  yavan-  -.yaon-  o,    i)  'Getreidefeld':
21800:Superl.  zu  yvan-  m.;  »r.  *iuu3tha-;  BthL.  IF, tt.  137.  —  Vgl.  'yiÜla-  EN.(?).  —  Pü.:  k<u*\ (zu  a):  euai  lälak.  —  i)  Sva.  niama-;  vgL  zu MidiSla-  und  zum  tu,  Kom^vX.yäTiiyas:  —  >)  Zu N,  mit_^adda  geschrieben/_IF.  11.  137.^
21911:•  j.  yvan-,  yavan-"';  ySn-  m.  'Jüngling': 'vänjtn  humananAsm  Vr.j.  3;  —  'Otts AumanavAs  11.2.1$;  36;  —  •Unat  hal^a .-  humananhal  P.JJ;  —  yum  (VS.)*' Aumans  H.  2.  11,  13.  a)  bes.  'junger Held,  Held':  yat  nmSnS.paitlm  vindätna •vanS  (GS.)  J'  sralsilo.kthrpa  Yt  /J.  40;  — ktrssäspasca  .  .  'ava  gatatH  gaZavarS  Y. 5. 10;   —   srüohtit  . .  'Bnam  aojist?m  Y.
27214:•  j.  sraeStö.kahtp-  f.  'die  schönste  Ge- stall': yat  nmStiS.paittm  vindama  yvanS 'pa  (IS.)  Yt  15. 40.
```


## [2026-10-17T00:32:45.768Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '2855,2870p' BQT_v2.txt | cut -c1-300; grep -n -E '\\bjuxt|\\bjuγ|\\bjug\\b|\\bjuwān|\\bjuwan|\\bjawān' PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head",
 "description": "BQT joft context; grep PHD/NYB"
}
```


### [2026-10-17T00:32:46.038Z] TOOL RESULT

```
جفت فلك هه کنابه از آفتاب و ماه 


جفتاك = م اول بروزن اردگ » 
نام مرغی است ت که بر و ماد آن هر کدام بك 
بال دارند و بجای بال دیگر بررا قلابی ومادمرا 
حلقه ات از استخوان چون پرواز کنند 
ار قلاب را بر 
کنند و چون بدانه خوردن مشغول 9 از 
یکدیگر جدا شوند و ترديك بهم چرا کنند 
واینپا را بعرمی‌لابنفك خوانند ۷ - و بفتح اول 
کاروانك را گونند . 


؟ ‏ اوستا _ ۷۱۲4۵ (بهم بیوستن» چاریا 

NYB_vol2_glossary.txt:4482:yuxt [ywht'] a pair: č-yurt [HN? ~, v. 8. v. e] for év-yuxt, a bahuvrihi: having, implying one pair (playing a game) = a game 1187. 119%, 1201. — Av. (1301) ydata- ‘a team of horses’; NP juft < *juxt ‘a yoke, a couple, a pair’, from yaog-, V.S. v. apiyuat.
PHD.txt:414:jawédan [LOLMN < А l-Imn; ywyt?n' | (P y'wyd?n, M Pyn), N ~] eternally, always. ~ag [-k! | (P -g), N ~a] eternal, perpetual. jawén [S£yn! | № jawin] made of barley. jeh [yh, yyh = Av. jahi-] the Whore, female arch-demon. fiw [суш!, yyw! = Av. fiwya-] (consecrated) milk. *jomā [ywm’y] together with; both. jorda [ywilt’y, 2k | (P yw?rd?w), J *jwrd?r] corn, grain. jo(y) [ywd, ywb! | N ~] stream, channel. Jóy-, -išn, v. Jadan. jud [ywdt' | M jwd] separate, different; anti-. ~ az [N juz] except, apart from. judàg [ywd? h! | N juda] separate, different. ~ih: separation, difference. Jūdan, jóy- [ywtn!, ywd- | M jwwdn, (jw-), (N jawruan)] chew; devour (daevic). „išn: eating (daevic). jud-|-bēš [ywdt bys] harmless, antidote. ~-dadestan [-D YN A] disagreeable, opposing. ~-déw [-ŠD YA) anti-demonic. ---này [-> d] a fathom (6 ft.). jud-ristag [yzodt lystk!] schismatic, heretic. ~th: heresy. Juy [усе | N ~] yoke. Jumbāģīh [ywmb’kyh] motion. jumbénidan, jumbén- [ywmbyn-yin'] (cause to) move. jumbidan, jumb- [ywmb-yin' | N ~] move. ~išn: motion, movement. jumbihistan, jumbīh- [ywmbyh-stn'] be moved. juttar [ywdtl | M jwtr] different, otherwise. --īh: opposite, reverse. Juwān [ywb?n! | (P ywn), N jawàn] young; a youth. ~th: youth. juxt [ywht! | (P ywxt), N juft!] pair, couple.
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD.txt:1420:couple juxt.
PHD.txt:3034:pair juxt.
PHD.txt:4377:youth Juwan; juwānīh.
PHD.txt:5474:ə dandán, juwan
PHD_mackenzie.txt:5583:xumb [hwmb' I M xwmb, N --] jug, pitcher.
PHD_mackenzie.txt:6904: interpret wizardan.                       jug xumb.
PHD_mackenzie.txt:8004:wrong abaron, zefiin.                   youth Juwan; juwanih.
```


## [2026-10-17T00:32:54.531Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'juwān|yuvān|ywb.n|ywān|juvān' NYB_vol2_glossary.txt | head -3; echo HRN; grep -n -E 'juft|jafl|ǰuft|yūγ|yugh|jüγ|ǰuγ|juγ|javän|ǰavān|jawān|javān' HRN.txt | head -10; echo HUB; grep -n -E 'juft|ǰuγ|juγ|jugh|yōγ|ǰavān|javān|jüγ' HUB.txt | head -10; echo CHEUNG; grep -n -E '^\\*?yau[gǰ]|\\*yaug' CHEUNG.txt | head -5",
 "description": "Grep NYB, Horn, Hübschmann, Cheung"
}
```


### [2026-10-17T00:32:54.909Z] TOOL RESULT

```
4458:yuvan [ywd'n', for ywb'n' with a b joined to the left] youth, a young man 135. 744; 12000 mart ~ 12028. — Av. (1305) yvan-, yavan- ; Ps. abstr. ywb’nyhy, MPrth yw’ngft (S), Paz. jugnī (Aog). — NP javān.
5468:yaz-: yaštan, izišn yazata-: yazčt Yima: Yam yujyasti-: yujiyast yüxta-: yuxt yūšmāka-: šmāh yvan-, yavan-: yuvān
6670:juanī: yuvān judtar: yuvat jumē: yumē
HRN
3983:niäz. javän.
3987:LW. kurd. juvän; afy. javän; bei. javan (111).
6793:*) An ursprüngliches ^sila^ten (vergl. jjuft aus jf*x^) darf man
18517:m. javän 429.
HUB
1715:noch juftdk *das Ausschlagen, der Tritt rait beiden
1716:Hinterbeinen = np. jufta, \m Balufi kommt auch
1717:jiixt gleich' (von Zahlen, Dames p. 65) neben juft
5395:'Weber ; jfuxtak ein Paar' (Turteltauben, 5. Jhd.), np. juft
8748:'soviel* etc. (Vullers, Gram. p. 233). Dazu auch juftak
8754:(Turteltauben), afgh. LW. juftak *das Ausschlagen mit beiden
8755:Hinterbeinen = np. jufta; kddak 'Kind', phi. kotak, arm.
8960:giessen H. 638 u. s. w. Ap. xt wird im Np. zu ft in juft
CHEUNG
```


## [2026-10-17T00:32:58.970Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '3975,3990p' HRN.txt; grep -n -E '^ *4[0-9]{2}\\. *(juft|ju)' HRN.txt | head; grep -n -i 'yaug' CHEUNG.txt | head -5; sed -n '5390,5397p' HUB.txt",
 "description": "Read Horn javān entry, Cheung yaug, HUB juft"
}
```


### [2026-10-17T00:32:59.387Z] TOOL RESULT

```
Studien II, IH Anm. 2.— 96 —
428. jev (AM.), jo *6erste*, jevm.
Käs. ye, ya,
SiW.yava- *6etreide'; phlv. jav bezw. yav; ai. yäva-.
knrd, je, jau, yö (H.-Sch.); oss. yau, yäu, yeu *Hirse'
(147); bei. /ö, jav, n. jau 'Gei-ste' (179); si/n. yavoj,
sar. yaugjy yögj, 'MehY (aus ^yavaka^).
429. Jevän, juvän 'Jüngling .
niäz. javän.
aw. ytivan- {yvan-) 'Jüngling; phlv. yuvän (päz.
falsch jüdän)^), arm. LW. yavanak, yovanak 'Junges
eines Vierfüsslers'; ai. yüvan-,
LW. kurd. juvän; afy. javän; bei. javan (111).
430. jösTden *koehen, sieden, jös{pere), jösäk, jösänldtn,
Ka§. vöyösnaä, böyösad (Qohrüd).
ai. yüs-, yüsdn- 'Brühe*.
ayatkar (?) Gl. and Ind. p. 23.
Dagegen / in: jatagov Tertheidiger* (5. Jhd.) = paz.
jada(n)gDf phi. jatagDw^ geschrieben yatakgob^ ap. "^yata-
gauba- (ZDMG. 46, 325); Jatuk 'Zauberer (5. Jhd.) = np.
Jadu^ zd. ydtU' ; julhak Weber (modern) = np. Jolahj Jdldha
'Weber ; jfuxtak ein Paar' (Turteltauben, 5. Jhd.), np. juft
Taar , zd. yuxta- 'Gespann ; javitean-xosrov (Sebeos 68)
*) Im Ap. steht yad fflr yaz^ vgl. ayadana- 'Tempel*. Also yaz-
```


## [2026-10-17T00:33:05.588Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'yau.?[gǰj]-|yuxta|yuj-' CHEUNG.txt | head -5; sed -n '6788,6795p' HRN.txt; echo IEC; grep -n -i -E '^ *i?y[uū]gom|yugom|^ *yuwen|yuu̯en|yuwn' IEC.txt | head -5; echo SYN; grep -n -E 'yuga-|yuvan-' SYN.txt | head -5",
 "description": "Grep Cheung, IEC, SYN"
}
```


### [2026-10-17T00:33:06.007Z] TOOL RESULT

```
14583:*NEIR: Yi. yuxs-/yuxt-, M. yuxs-/yuxt- (inch.) ‘to learn’, Yghn. yuxs-/yuxta- ‘to get 
14617:Partic.: perf. pass. YAv. yuxta- (Y 49.9, Yt 5.50, Yt 9.2), YAv. apaiiüxta- (V 18.30), Y Av. fra.yuxta- (Yt 
14618:10.125); Inf.: YAv. yuxta (Y 11.2) 
kurd. FD. LW. sest; afy. speta,
782. susten Vaschen', Praes. söy-em^),
phlv. sustan, söyBnd^ söy(i)sn; kurd. LW. sustin
'waschen' (vergl. g. sustinUu neben sustmün) ; bei.
*) Pfiz. qastäftun^ qastäwidan (Men.) ist Unsinn.
*) An ursprüngliches ^sila^ten (vergl. jjuft aus jf*x^) darf man
wegen Praes. siiäb-em natürlich nicht denken.
^) Bartholomae, Ar. Forsch. III, 33 liest staitc.
IEC
SYN
4144:2. Lith. jautis : Lett. jutis ‘joint’, Skt. go-yuti- ‘yoke of cattle’, yu- ‘bind, yoke, harness’, yuga- ‘yoke’, Grk. tuyév, Lat. wugum ‘yoke’, Lat. di&mentum ‘draught-animal’, etc., hence orig. ‘yoke animal’, Walde-P. 1.201.
18354:10.78 YOKE Grk. tuys Goth. jukuzi Lith. jungas NG tuys ON ok Lett. jugs Lat.  iugum Dan. aag ChSl. 290, jartmis It. giogo Sw. ok SCr. jaram Ty. joug OE geoc, gioc Boh, jafmo, jho Sp. yugo ME joke, yocke Pol. jarzmo Rum. jug NE yoke Russ. jarmo Ir. cuing Du. juk Skt. yuga- NIr.  cuing OHG joh, juh AVE Fae 5 W. tau MHG joch Br. yeo NHG joch
18359:Gme.; Lith. jungas (-n- fr. junkti), Lett, jugs; ChSl. igo (*jigo fr. *jtigo), Boh. jho (Pol. zgo- in place-names; Russ. igo now only fig.); Skt. yuga-m (Av. form not quotable, but NPers. juy, etc.); Hitt. yugan, yukan.
24421:6a 14.14 YOUNG NG. id Goth. juggs Lith. jaunas Lat, hee ON ungr Lett. jauns io Dan. ung ChSl. junit hr, he Sw. ung SCr. mlad 8p, Hote OE —geong Ha ria Rum, : ME yong ‘ol.  mlody h Ag in, june NE young Russ. molodoj, junyj NI, ig Du. jong Skt.  yuvan-, kanina- uf teuane OHG jung Av. yuvan- = Fs Mo jung
24428:due to Fr. influence); Lith. jaunas, Lett. jauns, ChSI. junit (positive not in Gospels, but junéji = 6 vedrepos, Lk. 15.12), Russ. junyj, Bulg., Slov. jun; Skt., Av. yuvan-, ytin- (Av. quotable only as sb. ‘young man’); b) Ir. dac, dc, Nit. 69, W. iewanc, Br. yaouank; Goth. juggs, ON ungr, etc., general Gmc.; cf. Lat. iuvencus, -a ‘steer, heifer’, Umbr. tuenga ‘iuvencas’, Skt. yuvaca- ‘youth- ful’,
```


## [2026-10-17T00:33:10.185Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '14600,14616p' CHEUNG.txt | cut -c1-250; sed -n '14619,14640p' CHEUNG.txt | grep -n -i -E 'NP|Pers|juft|MP|yōg' | head",
 "description": "Read Cheung entry header"
}
```


### [2026-10-17T00:33:10.518Z] TOOL RESULT

```
*IE COGNATES: Arm. usanim ‘I learn, am adapted to’, OCS vyknoti ‘to become 
accustomed to’, OCS učiti ‘to learn’, Lith. junkti ‘to become accustomed to’, Goth. 


bi-uhts (ppp.) ‘accustomed’ 
*REFERENCES: IIFL П: 274, 555b; Andreev — PeSéereva: 366b; EVS: 79; DKS: 194b Ё; Werba 1997: 337; 
Steblin-Kamenskij 1999: 434 


*jauj ‘to harness, yoke, employ’ 

*AVESTAN: yüj- ‘to harness’ || (+ *apa-) ‘to yoke off, lay down’ || (+ *fra-) ‘to 
harness’ = Liste: 47 

Pres. {1} n- IND. 3р1. *yunjinti (F 252, cf. Kellens 1984: 165f.); Pres. {2} 1а-: IND. 35р. YAv. yujiieiti 
(Yt 10.52); Aor. athem.: INJ. 3sg. OAv. yaogot (Y 44.4), 1р1. med. YAv. fra(-ca) yaoxmaide (Yt 4.1), 
3pl. OAv. yüjan (Y 46.11, Y 49.9), SUBJ. 1sg. OAv. yaoja (Y 50.7), med. 3р1. OAv. yaojante (Y 30.10); 
3:*MIDDLE PERSIAN: (+ *à-) BMP ’ywe- /ay6z-/ ‘to join; yoke; drive’ || (+ *upa-) BMP 
4:"pywc- /abyöz-/ ‘to join, mix’ || (+ *pari-) MMP pyrwz, BMP pylwc /peroz/ *victor- 
5:ious, victor’. Ф The Persian forms of ‘victory’ were thought to derive from *pari- 
8:=> DMMPP: 290a 
10:(+ *a-) Pres.: SUBJ. 3sg. BMP ’ywe’t /ayozad/; Partic.: perf. pass. BMP ’ywht /ayuxt/ || (+ *upa-) Pres.: 
11:IND. 3р1. BMP ’pyweynd /abyozend/; Partic.: perf. pass. BMP "pywht /abyuxt/ 
14:‘victory’ => Ghilain: 63 | DMMPP: 283a
```


## [2026-10-17T00:33:16.566Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; grep -A6 -E '^\\- \\*\\*(FVQ|AFA|AFM|PLA|LKT)\\*\\*' SOURCE_MATRIX.md | grep -E '^\\-|refs/' | head -20",
 "description": "Get Semitic source file paths"
}
```


### [2026-10-17T00:33:16.856Z] TOOL RESULT

```
- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt`
- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt`
- **PLA** — A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt`
- **AFA** — S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFA.txt`
- **TAD** — Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-huru
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TAD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TAD_pages.txt`
- **ARB** — al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edi
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ARB_abdulraheem.txt`
--
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt`
```


## [2026-10-17T00:33:20.893Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'Zauj|Zawj|zauj|Qist|Qisṭ|Qistās|Qisṭās|ζε[υü]γος|ξέστης|xestes|sextarius|Sextarius|δικαστ' FVQ.txt | head -20",
 "description": "Grep Jeffery for zawj and qist"
}
```


### [2026-10-17T00:33:21.281Z] TOOL RESULT

```
9782:(Zawj). 
14812:(Qist). 
14865:(Qistds). 
14918:would derive it from ^e'or?;? from the Lat. sextarius used as a measure 
21712:sextarius 239
```


## [2026-10-17T00:33:24.521Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '9775,9815p' FVQ.txt; echo ----; sed -n '14805,14935p' FVQ.txt",
 "description": "Read Jeffery zawj, qist, qistas entries"
}
```


### [2026-10-17T00:33:24.836Z] TOOL RESULT

```
singiv&ra, from which comes the Gk. Qyyi&tpis? There can be 
little doubt that the word passed into Arabic from Syr. and was 
thence borrowed back into Persian in Islamic times. 6 It occurs in the 
early poetry 7 and so was evidently an early borrowing. 



(Zawj). 

Occurs frequently in many forms, cf. ii, 33. 
A pair, species, kind, sex, couple, companion, spouse. 
It is a very early loan-word in Arabic from Gk. {eDyoy through 

1 So Vullers, Lex, ii, 148, and cf. Pnhlttri Texts, ed. Jamasp Ar-una, p. 31. 

2 Hubschmann, Arm. (Jramm, i, 238. 

3 From which was then derived the form X"TJ' 1 ?, Levy, Worterbucfi, i, 345. 

1 Yule (vide Yule and Burnell, Uobson Jtjbton', cd. Cooke, 1003, p. 374) thought 

that the Skt. ^J^F^T was a made-up word, and that as the home of the plant is in 
the Malabar district, we should look for the origin of the word in the Malayalam 
gnnnf| inchi, meaning root (cf. Tamil j$<&\ inji; Sinhalese gQO^fQ 
inguru), but there is the equal probability that these are all derived from the 
Skt. ^JIF a horn. Sec, however, Laufcr, ftino-Iranica, 54fi, 583. 

5 This then beoame ytyyt'jStpis and through the Lat. gingibvr became the Middle 
English gingevir and our ginger. IVorn fyytj3c/M? came the Syr. ^2)Q.kj] and 
other forms (Low, Aramainche Pfanzcnnarnen, p. 138). ^ 

6 Fracnkel, Vocab, 11 ; Pautz, Offenbarung, 213 ; Horovitz, 1'aradie*, 11; Addai 
Sher, 80. 

7 See Geyer, Zwei Gedichte, i, 57 ; ii, 83 ; Jacob, Beduinenleben, 258. 



FOREIGN VOCABULARY OF THK QUR^AN 155 

** 
----
to do with fish of any kind. Noldeke suggests with much more 
probability that it is a shortened form of the Gk. Kap^aplaf, 5 a word 
which is used for a kind of small shark with pointed teeth, and which 
Nicander the Colophonian 6 said was used also for a lamia or a squill. 



(Qist). 

iii, 16, 20 ; iv, 126, 134 ; v, 11, 46 ; vi, 153 ; vii, 28 ; x, 4, 48, 55 ; 
xi, 86 ; xxi, 48 ; Iv, 8 ; Ivii, 25. 
Justice, equity. 

.x* ^- 

It would seem on the surface to be a derivative from ,L..*J5 
which occurs in iv, 3 ; Ix, 8 ; xlix, 9, and of which other derivatives 

are found in ii, 282 ; xxxiii, 5 ; Ixxii, 14, 15. This ,Lu-J, however, 
may be a denominative and as-Suyuti, Itq, 323 ; Mutaw, 49, tells us 

1 Or sword-fish (Margoliouth, Mohammed, 9). Ihn Faqih (ed. do Goeje, p. 290) 
describes it aa <jdM /^* /v^l ^*- 

2 Tabari, Annalw, i, 1 104 ; Damm, Hayaiwn, ii, 291 ff. ; vide also Khizana, i, 98. 

3 Zaologie der Talmud, Frankfurt, 1858, p. 271. This is accepted by Levy, Wnrter- 
biich, ii, 416, and Goldschmidt, Der Jtabyloniftc.he Talmud, vi, 1136 ; though Jastrow, 
Diet. Talmud, i, 667, gives it as meaning probably the shark. 

* Bartholomae, AIW, 1848; cf. Yasht, x, 118; v, 90. 

5 Cf. also Hess in ZS, ii, 220. 

a In his Book on Dialects quoted by Athenaeus, vii, 76. 



238 FOREIGN VOCABULARY OF THE QUR'AN 



that some early authorities thought JU^.S was a borrowing from 

Greek. 1 

The root D2?p is widely used in Aramaic but occurs elsewhere 
apparently as a loan-word. Thus Blttfp ; KBEftp, like Syr. ]A*ap, 
means truth, right 2 ; Hand. tDtf p is to be true, and Palm. ZDttfp 
to succeed, while in the Christian-Palestinian dialect we find f^D 
true. 3 The Heb. ?2?p is an Aramaizing, as Toy pointed out in his 
Commentary on Proverbs, and Fraenkel is doubtless correct in taking 




the Ar. la.*~A as also of Aram., probably of Christian Aram, origin. 4 



(Qistds). 

xvii, 37 ; xxvi, 182. 

A balance. 

There was practical agreement among the early authorities that 
the word means primarily a balance, and then metaphorically justice 
(cf. Raghib, Mufraddt, 413 ; LA, viii, 59). It was also very generally 
recognized as a loan-word. Some considered it as a genuine Arabic 

word, a variant of Ja.*Jf, 5 but the weight of the authorities as we 

see from as-Suyutl, Itq, 323 ; Muzhir, i, 130; al-Jawaliqi, Mu ( arrab, 114; 
ath-Tha'alabi, Fiqh, 318, and as-Sijistam, 257, was in favour of its being 
taken as a borrowing from Greek. 6 Its foreign nature is indeed indicated 
by the variety of spellings we find. 7 

It was evidently an early borrowing, for it occurs in verses of 



1 This may be a reminiscence of the Lat. iusticia, though Sprenger, Leben, ii, 219, 
thinks that it may be the Lat. nextarivs. 

2 Notice also the XIOBTO =- honesty (with 3), of the incantation texts ; cf. 
Montgomery, Aramaic, Incantation, Texts, Glossary, p. 292. 

3 Schwally, I (Hot won, 86 ; Schulthess, Lex, 185. 

4 Frrmdw, 205; Noldeke, SHAW, Berlin (1882), liv, 5, thinks the noun is an 
Arabicizing of l^S&A l)ut ^voiak, Fremdw, 76, 78, would regard it as an Arabic 
word taken as foreign through its similarity in sound with ^IL^J. 

5 See Zam. on xxvi, 182, and the remarks in TA, iv, 218. 

6 See also as-Suyuti,^/?/^>, i, 137; Ibn Qutaiba (Adab al-Katib), 527 ; al-KhafajI, 
156 ; as-Suyuti, Mutaw, 49. 

7 al-Jawaliql notes ^Ik.J ; ^IWljj ; jlkJ ; to which we may add from 
TA. rlk^a* and 



FOREIGN VOCABULARY OF THE QUR*AN 239 

'Adi b. Zaid, an-Nabigha, 1 and others. The origin of the word, how- 
ever, is not easy to settle. Sachau in his notes to the Mu'arrab, p. 51, 
quotes Fleischer as suggesting that it goes back to the Lat. conslans 
as used of the libra* Fraenkel, Fremdw, 282, suggests a hypothetical 
*KOVCTTCO$ as a possible origin, and in WZKM, vi, 261, would interpret 
it from fyyoo-racria- Vullors, Ley, ii, 725, thought that it was probably 
a mangling ..of the Gk. ^Oyor a yoke, and Dvorak, Fremdw, 77 ft'., 
would derive it from ^e'or?;? from the Lat. sextarius used as a measure 
of fluid and dry materials. 

All these suggestions seem to be under the influence of the theory 
of the philologers that the word is of Greek origin. It would seem 
much more hopeful to start from the Aram. NtDOp ; NJDO'p ; 
fcttDOIp meaning measure, or the Syr. l4 CQjD - The final s 
here, however, presents a difficulty, and Vollers, ZDMG, 1, 633, 3 
suggests that it is from the Gk. St/cacrr^y a judge, which in Syr. is 
tfiDQ^ttO.!? (BB, in PSm, 891), and with the > taken as the genitive 
particle, would give us JBQ^mo. This, influenced by the similar 



also = dLKaaTrj?, would give us ^la^Ji. This is very 
ingenious and may be true, but Mingana, Syriac Influence, 89, thinks 
it simpler to take it from I&CQO representing ^to-rrjs in some form 
in which the final tt) had survived.
```


## [2026-10-17T00:33:35.083Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '9815,9835p' FVQ.txt; echo AFA; grep -n -E 'zaug|Zaug|ζεῦγος|zûg|zuga|zûgâ' AFA.txt | head -5; grep -n -E 'قسطاس|قسط' AFA.txt AFM.txt TAD.txt | head -5; echo LKT; grep -n -i -E 'zaud|zauǧ|zawǧ|kistās|qisṭās' LKT.txt | head",
 "description": "Read rest of zawj; grep Fraenkel, Addi Shir, Lokotsch"
}
```


### [2026-10-17T00:33:35.419Z] TOOL RESULT

```
** 

the Aram. The verbal forms ir j j, etc., with this meaning are clearly 

denominative, the primitive root 77 ij meaning "to sow discord 

*> *'. 
between". In the Qur'an we have many forms *r Jj to many, to 

^ ^ x 

couple with, ^ 3j plu. 77 ijjl a wife or husband (human) ; <r 3 j kind, 



, 
species ; O^Jj ft joair ; 7^ J j s?#. 

No Muslim authority, as Fraenkel notes (Frewdw, 107), has any 
suspicion that the word is other than genuine Arabic, but no derivation 
of the word is possible from Semitic material, and there can be no 
AFA
4070:wohl auch Ton den Aramäemals zaug Dillm. 1061 ange-
TAD.txt:1432:سقسطة - بوناني 923 معنا » المغا لطة 
AFM.txt:5059:(الشَان) القسطاس 3 توزن بها الاشياء. القند تعريب كبآن وبقال فين 0 
AFM.txt:5133:قال الاب لامنس في كتاب الفروق:« القسطار هو الصيرف وقيل التاجر. ومن اغرب 
AFM.txt:5145:ما قيل قول ܐܕܐ في المعرب : القسطار هو 5( ¢ 3 1 لاذي :ܸܛ 
AFM.txt:5146:امور القر ® وَسُووم, | قسطار وهو راح بع الى معنى الممزان اه وهو ܐܐܐ بحض نين 
LKT
```


## [2026-10-17T00:33:39.584Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '4062,4074p' AFA.txt; sed -n '5055,5062p' AFM.txt; grep -n 'قسطاس' AFM.txt | head -3; grep -n -E 'Qisṭās|qistas|Qistas|قسطاس' PLA_pages.txt incoming/PLA/PLA_pages.txt 2>/dev/null | head -3",
 "description": "Read Fraenkel zawj and Addi Shir qistas"
}
```


### [2026-10-17T00:33:39.931Z] TOOL RESULT

```
^vyo^ in's Arab. übei^egangen ist. Auch im Arabischen107
hat es noch den ursprünglichen Begriff des zusammenge-
spannten Paares ^Antara 21, 31, aus welchem sich dann
»Paar'* überhaupt mit allen Denominatiyen entwickelt. Kei-
nem Araber ist je ein Zweifel gekommen , dass dies Wort
echt seL Es muss aus sehr alter Zeit stammen, auch die
Abessynier haben es schon in ihrer frühesten Litteraturpe-
rioile — es kommt schon in der Bibelübersetzung Tor —
wohl auch Ton den Aramäemals zaug Dillm. 1061 ange-
nommen. Einige Schwierigkeit macht Vi »die Satteldecke**
(belegt mit einem Verse Lebid*s bei Gauh.); wenn man nicht
annehmen will, dass sie einfach »Paar** genannt wird, weil
sie aus zwei Theilen besteht, so wird man es zu K2T »sich


و يرادفة اليوناللي ܟܫܘ« ( راجع اا ) 

(الشَان) القسطاس 3 توزن بها الاشياء. القند تعريب كبآن وبقال فين 0 
اي وَزَنَهُ 6 0 أظن 5 قول الاب لامنس الذي قال ان كيان ( 3 ` 
00 مغ 621222112 بالرومية ومعناها اكرس 37 على !ܡܐ ܝ ايض 

5059:(الشَان) القسطاس 3 توزن بها الاشياء. القند تعريب كبآن وبقال فين 0
```


## [2026-10-17T00:33:49.869Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yewg-' 'https://en.wiktionary.org/wiki/%D8%B2%D9%88%D8%AC' 'https://en.wiktionary.org/wiki/%D9%82%D8%B3%D8%B7%D8%A7%D8%B3' 'https://en.wiktionary.org/wiki/%D9%82%D8%B3%D8%B7' 'https://en.wiktionary.org/wiki/%DB%8C%D9%88%D8%BA' 'https://en.wiktionary.org/wiki/%D8%AC%D9%81%D8%AA' 'https://en.wiktionary.org/wiki/%D8%AC%D9%88%D8%A7%D9%86' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82y%C3%A9wHn%CC%A5' 'https://en.wiktionary.org/wiki/iuxta' 'https://en.wiktionary.org/wiki/sextarius' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/jung%C4%85' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/jungaz' 'https://www.etymonline.com/word/adjust' 'https://www.etymonline.com/word/yoga' 'https://en.wiktionary.org/wiki/%E0%A4%AF%E0%A5%81%E0%A4%B5%E0%A4%A8%E0%A5%8D'; do echo \"=== $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 565, roots Yeu 1/Yeu 2\" 2>&1 | tail -3; done",
 "description": "Archive relevant web sources",
 "timeout": 400000
}
```


### [2026-10-17T00:34:00.171Z] TOOL RESULT

```
=== https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yewg-
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d9427871c0b0071d.txt
=== https://en.wiktionary.org/wiki/%D8%B2%D9%88%D8%AC
/home/sfmqrb/git/rishe-private/data/verification/sources/web/49c956950f087b83.txt
=== https://en.wiktionary.org/wiki/%D9%82%D8%B3%D8%B7%D8%A7%D8%B3
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7afb5ee6935dafd5.txt
=== https://en.wiktionary.org/wiki/%D9%82%D8%B3%D8%B7
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3e2095b394d840f4.txt
=== https://en.wiktionary.org/wiki/%DB%8C%D9%88%D8%BA
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8f44d46d788a8f32.txt
=== https://en.wiktionary.org/wiki/%D8%AC%D9%81%D8%AA
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8b09e18abd1c6143.txt
=== https://en.wiktionary.org/wiki/%D8%AC%D9%88%D8%A7%D9%86
/home/sfmqrb/git/rishe-private/data/verification/sources/web/900d781faf524e22.txt
=== https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82y%C3%A9wHn%CC%A5
/home/sfmqrb/git/rishe-private/data/verification/sources/web/cd01ea5ab84a2bd5.txt
=== https://en.wiktionary.org/wiki/iuxta
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f30f54a4276cd6b8.txt
=== https://en.wiktionary.org/wiki/sextarius
/home/sfmqrb/git/rishe-private/data/verification/sources/web/dfcb4fbb8f988226.txt
=== https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/jung%C4%85
/home/sfmqrb/git/rishe-private/data/verification/sources/web/80748b8ecd0117d2.txt
=== https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/jungaz
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4dc76ac604bf1194.txt
=== https://www.etymonline.com/word/adjust
/home/sfmqrb/git/rishe-private/data/verification/sources/web/52a32ce0672ff004.txt
=== https://www.etymonline.com/word/yoga
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ffe3035ddbdd0a93.txt
=== https://en.wiktionary.org/wiki/%E0%A4%AF%E0%A5%81%E0%A4%B5%E0%A4%A8%E0%A5%8D
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a470f0ffbc5b6039.txt
```


## [2026-10-17T00:34:04.692Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 49c956950f087b83 7afb5ee6935dafd5 3e2095b394d840f4 8f44d46d788a8f32 8b09e18abd1c6143 900d781faf524e22; do echo \"##### $f\"; wc -c < $f.txt; grep -n -i -A4 '^Etymology' $f.txt | head -40; done",
 "description": "Read etymology sections of archived pages"
}
```


### [2026-10-17T00:34:05.051Z] TOOL RESULT

```
##### 49c956950f087b83
26247
##### 7afb5ee6935dafd5
10704
##### 3e2095b394d840f4
27725
##### 8f44d46d788a8f32
8872
##### 8b09e18abd1c6143
17304
##### 900d781faf524e22
20648
```


## [2026-10-17T00:34:09.572Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 49c956950f087b83 7afb5ee6935dafd5 3e2095b394d840f4 8f44d46d788a8f32 8b09e18abd1c6143 900d781faf524e22; do echo \"##### $f\"; grep -n -i -E 'borrowed|from (Middle|Old|Proto|Ancient|Classical|Aramaic|Syriac|Greek)|inherited|cognate' $f.txt | head -12 | cut -c1-400; done",
 "description": "Grep etymology statements"
}
```


### [2026-10-17T00:34:09.942Z] TOOL RESULT

```
##### 49c956950f087b83
276: From Aramaic זוגא ( zawgā , “ yoke, pair ” ) , from Ancient Greek ζεῦγος ( zeûgos , “ yoke ” ) which was used in Greek for the yoke of marriage – now it forms a root ز و ج ( z w j ) .
1150: Inherited from Arabic زَوْج ( zawj ) .
1168: Inherited from Arabic زَوَّجَ ( zawwaja ) .
1266: Borrowed from Arabic زَوْج ( zawj , “ one of a pair ” ) .
1315: Borrowed from Arabic زَوْج ( zawj ) . Doublet of یوغ ( joġ, juġ , “ yoke ” ) , also related to جُفت ( joft ) . 
1395: Inherited from Arabic زَوَّجَ ( zawwaja ) .
1541: Arabic terms derived from Proto-Indo-European 
1543: Arabic terms borrowed from Aramaic 
1544: Arabic terms derived from Aramaic 
1545: Arabic terms derived from Ancient Greek 
1570: Hijazi Arabic terms inherited from Arabic 
1581: Ottoman Turkish terms borrowed from Arabic 
##### 7afb5ee6935dafd5
155: Via an Aramaic  term retained in Classical Syriac ܣܓܘܣܛܪܐ ( səgosṭārā ) and other Syriac spellings from Ancient Greek ζυγοστάτης ( zugostátēs , “ weigher ” ) , which also passed into  Latin zygostatēs . For the stem ending in ـس ( -s ) , maybe also denoting the occupation after ζυγοστασία ( zugostasía ) , ζυγοστάτησις ( zugostátēsis , “ weighing ” ) . Influenced by قِسْط ( qisṭ , “ share ” ) 
368: Categories : Arabic terms borrowed from Aramaic 
369: Arabic terms derived from Aramaic 
370: Arabic terms borrowed from Ancient Greek 
371: Arabic terms derived from Ancient Greek 
383: Arabic terms borrowed from Latin 
##### 3e2095b394d840f4
286: If the noun goes so far as to mean justice , it is perhaps a semantic loan from Classical Syriac ܩܘܼܫܬܿܵܐ ( qūštā , “ truth, rectitude, justice ” ) , while others go even so far as to consider a borrowing from Latin iūstitia , whereas the use for a measure is Aramaic קִיסְטָא / ܩܸܣܛܵܐ ( qesṭā ) from Medieval Greek ξέστης ( xéstēs ) from Latin sextārius ( “ a cubic measure ” ) . The presence o
1117: Borrowed from Ancient Greek κόστος ( kóstos ) .
1209: Inherited from Arabic قَسَّطَ ( qassaṭa ) .
1303: Inherited from Arabic قِسْطْ ( qisṭ ) .
1323: Borrowed from Arabic قِسْط ( qisṭ , “ equity; lot, portion, share ” ) .
1376: Borrowed from Arabic قُسْط ( qusṭ , “ costus ” ) , ultimately from Sanskrit कुष्ठ ( kuṣṭha , “ crepe ginger ” ) .
1408: Borrowed from Arabic قِسْط ( qisṭ ) .
1482: Borrowed from Classical Persian قِسْط ( qist ) , borrowed from Arabic قِسْط ( qisṭ ) .
1550: Arabic semantic loans from Classical Syriac 
1551: Arabic terms derived from Classical Syriac 
1552: Arabic terms borrowed from Latin 
1554: Arabic terms borrowed from Aramaic 
##### 8f44d46d788a8f32
218: Inherited from Proto-Turkic *yōg . Cognate with Old Turkic 𐰖𐰆𐰍 ( y¹wg¹ ) .
258: Borrowed from Persian یوغ ( yuġ ) .
294: From earlier جغ ( joġ ) , from Middle Persian ywg ( juğ , “ yoke ” ) , from Proto-Iranian *yugám , from Proto-Indo-Iranian *yugám , from Proto-Indo-European *yugóm . From the same root are جفت ( joft ) and, via Greek and Arabic, زُوج ( zowj ) , both meaning “pair, couple; partner; even number”. Cognate with English yoke .
372: Borrowed from Classical Persian یوغ ( yōġ , “ yoke ” ) . 
374: Cognate with Pashto جغ ( źëǧ , “ yoke ” ) , Torwali یو ( yū , “ yoke ” ) , and Kalasha جو ( ǰu , “ yoke ” ) . 
417: Categories : Karakhanid terms inherited from Proto-Turkic 
418: Karakhanid terms derived from Proto-Turkic 
424: Ottoman Turkish terms borrowed from Persian 
429: Persian terms derived from Proto-Indo-European 
431: Persian terms inherited from Middle Persian 
432: Persian terms derived from Middle Persian 
433: Persian terms inherited from Proto-Iranian 
##### 8b09e18abd1c6143
240: Borrowed from Classical Persian جفت ( jaft ) .
323: From Palestinian dialects, borrowed from Aramaic גיפתא ( gip̄tā ) .
413: From Egyptian dialects, borrowed from Ottoman Turkish چفت ( çift ) .
667: From Middle Persian [Book Pahlavi needed] ( ywht /⁠ǰuxt⁠/ ) , from Proto-Iranian *yuxtáh , from Proto-Indo-Iranian *yuktás , from Proto-Indo-European *yugtós . Doublet of یوغ ( yuġ ) and زوج ( zowj ) .
783: Uncertain. Regard Sanskrit चाप ( cāpa , “ bow; arc ” ) , Persian چپ ( čap , “ left ” ) , چپه ( čape , “ topped over ” ) , Old Armenian ճապուկ ( čapuk , “ supple ” ) , Sangisari , Semnani , Lasgerdi , Sorkhrudi Mazanderani چفت ( čeft , “ sheepfold ” ) , Shahmirzadi چفت ( čoft , “ sheepfold ” ) , Shughni чаг̌ ( čaɣ̌ , “ reed ” ) , Chagatai چیغ ( çığ , “ reed, any stiff steppe grass; a mat or sc
865: Categories : Arabic terms derived from Classical Persian 
866: Arabic terms borrowed from Classical Persian 
875: Arabic terms borrowed from Aramaic 
876: Arabic terms derived from Aramaic 
877: Arabic terms derived from Middle Persian 
878: Arabic terms derived from Proto-Iranian 
879: Arabic terms derived from Proto-Indo-Iranian 
##### 900d781faf524e22
373: From Proto-Iranian *HyúHā , from Proto-Indo-Iranian *HyúHā , from Proto-Indo-European *h₂yéwHō .
393: From Proto-Iranian *HyúHā , from Proto-Indo-Iranian *HyúHā , from Proto-Indo-European *h₂yéwHō .
395: Cognate with Persian جوان ( jawān  / javân ) , Pashto ځوان ( źwān ) , Sanskrit युवन् ( yúvan ) , Latin iuvenis ( Italian giovane ), Latvian jauns , Old English ġeong ( English young ).
457: Borrowed from French joint .
494: From Classical Persian جَوَان ( jawān ) , from Middle Persian [script needed] ( yw'n /⁠ǰuwān⁠/ ) , from Proto-Iranian *HyúHā , from Proto-Indo-Iranian *HyúHā , from Proto-Indo-European *h₂yéwHō .
496: Cognate with Northern Kurdish ciwan , Pashto ځوان ( źwān ) , Sanskrit युवन् ( yúvan ) , Latin iuvenis Italian giovane , French jeune , Spanish joven , Latvian jauns , English young ).
553: Inherited from Middle Persian [script needed] ( yw'n /⁠ǰuwān⁠/ ) , from Proto-Iranian *HyúHā , from Proto-Indo-Iranian *HyúHā , from Proto-Indo-European *h₂yéwHō , from *h₂óyu + *-Hō .
555: Cognate with Northern Kurdish ciwan , Northern Luri جڤۆ ( jevø ) , Pashto ځوان ( źwān ) , Sanskrit युवन् ( yúvan ) , Latin iuvenis ( Italian giovane , French jeune , or Spanish joven ), Latvian jauns , Old English ġeong ( English young ).
740: a male given name , Javan , from Middle Persian 
742: a surname , Javan , from Middle Persian 
752: Borrowed from Classical Persian جوان ( jawān ) .
795: Borrowed from French juin .
```


## [2026-10-17T00:34:20.728Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n '150,160p' 7afb5ee6935dafd5.txt | cut -c1-1200; for f in d9427871c0b0071d cd01ea5ab84a2bd5 4dc76ac604bf1194 80748b8ecd0117d2 f30f54a4276cd6b8 dfcb4fbb8f988226 a470f0ffbc5b6039 52a32ce0672ff004 ffe3035ddbdd0a93; do echo \"##### $f\"; head -3 $f.txt | cut -c1-200; grep -n -i -E 'from Proto|from Latin|from Old French|Sanskrit|Iranian|Avestan|reconstruct|superlative|\\*h₂|youthful|young' $f.txt | head -8 | cut -c1-350; done",
 "description": "Read remaining archived pages"
}
```


### [2026-10-17T00:34:21.196Z] TOOL RESULT

```
 قِسْطَار ( qisṭār ) , قُسْطَار ( qusṭār ) , قَسْطَرِيّ ( qasṭariyy ) , *سِقِسْطَار ( *siqisṭār ) , سِقِنْطَار ( siqinṭār ) , سِنِقْطَار ( siniqṭār ) , سِقْطِرِيّ ( siqṭiriyy ) 

 Etymology
 [ edit ] 

 Via an Aramaic  term retained in Classical Syriac ܣܓܘܣܛܪܐ ( səgosṭārā ) and other Syriac spellings from Ancient Greek ζυγοστάτης ( zugostátēs , “ weigher ” ) , which also passed into  Latin zygostatēs . For the stem ending in ـس ( -s ) , maybe also denoting the occupation after ζυγοστασία ( zugostasía ) , ζυγοστάτησις ( zugostátēsis , “ weighing ” ) . Influenced by قِسْط ( qisṭ , “ share ” ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /qis.tˤaːs/ , /qus.tˤaːs/ 
##### d9427871c0b0071d
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yewg-
FETCHED: 2026-10-17T00:33:51Z
STATUS: 200
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/yewg-
4:TITLE: Reconstruction:Proto-Indo-European/yewg- - Wiktionary, the free dictionary
6:Reconstruction:Proto-Indo-European/yewg- - Wiktionary, the free dictionary 
75: Reconstruction:Proto-Indo-European/ yewg- 
79: Reconstruction 
129: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
137: Possibly an extension of *yew- (as in Sanskrit यु ( yu , “ to unite ” ) ). [ 1 ] [ 2 ] 
152: Proto-Indo-Iranian: 
##### cd01ea5ab84a2bd5
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82y%C3%A9wHn%CC%A5
FETCHED: 2026-10-17T00:33:54Z
STATUS: -1
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82y%C3%A9wHn%CC%A5
##### 4dc76ac604bf1194
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/jungaz
FETCHED: 2026-10-17T00:33:56Z
STATUS: 200
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/jungaz
4:TITLE: Reconstruction:Proto-Germanic/jungaz - Wiktionary, the free dictionary
6:Reconstruction:Proto-Germanic/jungaz - Wiktionary, the free dictionary 
90: Reconstruction:Proto-Germanic/ jungaz 
97: Reconstruction 
147: This Proto-Germanic entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
155: From earlier *yunhós (from which /h/ > /g/ due to Verner's law ), from Proto-Indo-European *h₂yuHn̥ḱós ( “ young ” ) , from *h₂yuh₁en- ( “ young ” ) . [ 1 ] The shortening of the vowel from earlier *-uHun- is due to Osthoff's law .
165: *jungaz ( comparative *junhizô , superlative *junhistaz ) 
##### 80748b8ecd0117d2
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/jung%C4%85
FETCHED: 2026-10-17T00:33:56Z
STATUS: -1
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/jung%C4%85
##### f30f54a4276cd6b8
URL: https://en.wiktionary.org/wiki/iuxta
FETCHED: 2026-10-17T00:33:55Z
STATUS: 200
166: from Proto-Italic *jougestos ( “ yoked ” ) , from *jougos ( “ team of yoke animals ” ) (whence Latin iūgera   pl ), from Proto-Indo-European *(H)yewg-es- , from *(H)yewg- ( “ join together ” ) ;
168: from Proto-Italic *jugistos ( “ closest ” ) , equivalent to *(H)yug- +‎ *-istHos ( “ superlative suffix ” ) ; however, this suffix is otherwise not found in Latin.
268: Categories : Latin terms derived from Proto-Indo-European 
270: Latin terms inherited from Proto-Italic 
271: Latin terms derived from Proto-Italic 
##### dfcb4fbb8f988226
URL: https://en.wiktionary.org/wiki/sextarius
FETCHED: 2026-10-17T00:33:55Z
STATUS: 200
170: From Latin sextārius ( “ one-sixth ” ) , from sextus ( “ sixth ” ) + -ārius ( “ -ary ” , forming adjectives ) . Doublet of sextary .
316: Categories : English terms borrowed from Latin 
317: English terms derived from Latin 
##### a470f0ffbc5b6039
URL: https://en.wiktionary.org/wiki/%E0%A4%AF%E0%A5%81%E0%A4%B5%E0%A4%A8%E0%A5%8D
FETCHED: 2026-10-17T00:34:00Z
STATUS: 200
80: Sanskrit 
82: Toggle Sanskrit subsection 
198: Devanagari script form of yuvan ( “ young ” ) 
235: Devanagari script form of yuvan ( “ young man ” ) 
242: Sanskrit
286: From Proto-Indo-Iranian *HyúHan , from Proto-Indo-European *h₂yéwHō ( “ young ” ) .
288: Cognate with Avestan 𐬫𐬀𐬎𐬎𐬀𐬥 ( yauuan ) , Persian جوان ( jawān  / javân ) , Latin iuvenis , Lithuanian jaunas , Old English ġeong (whence English young )).
295: ( Classical Sanskrit ) IPA ( key ) : /ju.ʋɐn̪/ 
##### 52a32ce0672ff004
URL: https://www.etymonline.com/word/adjust
FETCHED: 2026-10-17T00:33:57Z
STATUS: -1
##### ffe3035ddbdd0a93
URL: https://www.etymonline.com/word/yoga
FETCHED: 2026-10-17T00:33:57Z
STATUS: -1
```


## [2026-10-17T00:34:35.266Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in https://en.wiktionary.org/wiki/yoga https://en.wiktionary.org/wiki/adjust https://en.wiktionary.org/wiki/young https://en.wiktionary.org/wiki/yoke https://en.wiktionary.org/wiki/iuvenis https://en.wiktionary.org/wiki/iugum https://en.wiktionary.org/wiki/%CE%B6%CF%85%CE%B3%CF%8C%CE%BD https://en.wiktionary.org/wiki/iuvencus; do echo \"=== $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 565, roots Yeu 1/Yeu 2\" 2>&1 | tail -1 | tee /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/f565.txt; f=$(cat /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/f565.txt); sed -n 3p $f; grep -n -i -E '^ *(From|Borrowed|Inherited)' $f | head -4 | cut -c1-350; done",
 "description": "Archive more Wiktionary pages and show etymologies",
 "timeout": 300000
}
```


### [2026-10-17T00:34:45.672Z] TOOL RESULT

```
=== https://en.wiktionary.org/wiki/yoga
/home/sfmqrb/git/rishe-private/data/verification/sources/web/267da0d488a3bd50.txt
STATUS: 200
457: From Wiktionary, the free dictionary
483: Borrowed from Sanskrit योग ( yóga , “ yoking, union ” ) , from Proto-Indo-Aryan *yáwgas , from Proto-Indo-Iranian *yáwgas , from Proto-Indo-European *yéwg-o-s , from *yewg- ( “ to join ” ) (whence also yoke ).
730: Borrowed from Chamorro yoga .
757: Borrowed from Sanskrit योग ( yóga , “ yoking, union ” ) , from Proto-Indo-Aryan *yáwgas , from Proto-Indo-Iranian *yáwgas , from Proto-Indo-European *yéwg-o-s , from *yewg- ( “ to join ” ) .
=== https://en.wiktionary.org/wiki/adjust
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bbdfead8786cad16.txt
STATUS: 200
200: From Wiktionary, the free dictionary
208: From Middle English ajusten , borrowed from Middle French adjuster , or Old French , from Latin ad ( “ to, up to, towards ” ) + iustus ( “ correct, proper, exact ” ) ; Equivalent to ad- +‎ just . Probably influenced in sense by Old French ajouster (cf. modern ajouter ), from Vulgar Latin *adiuxtāre , from Latin iuxta . The Middle English origi
=== https://en.wiktionary.org/wiki/young
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0136bb8aa31f635b.txt
STATUS: 200
234: From Wiktionary, the free dictionary
248: Inherited from Middle English yong , yonge , from Old English ġeong , from Proto-West Germanic *jung , from Proto-Germanic *jungaz , from Proto-Indo-European *h₂yuHn̥ḱós , from *h₂yuh₁en- ( “ young ” ) .
=== https://en.wiktionary.org/wiki/yoke
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7ad334747df8b007.txt
STATUS: 200
224: From Wiktionary, the free dictionary
263: From Middle English iuc , jok , yok , yoke , ȝok , ȝook [ 1 ] , from Old English ġeoc , ġioc , ioc ( “ yoke ” ) , from Proto-West Germanic *juk , from Proto-Germanic *juką ( “ yoke ” ) , from Proto-Indo-European *yugóm ( “ yoke ” ) , from *yewg- ( “ to join, yoke ” ) . [ 2 ] Doublet of yuga , jugum , yoga and possibly yogh .
904: From Middle English yoken , yoke , ȝoken ( “ to put a harness or yoke on a draught animal or pair of such animals, to yoke; to attach (an animal to a cart, plough, etc.) with a yoke; to lock (arms) in wrestling; to bind (oneself or someone) to something ” )   [ and other forms ] , [ 3 ] from Old English ġeocian , iucian , from Old English ġeoc
=== https://en.wiktionary.org/wiki/iuvenis
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1dbd4e47d5a4c70c.txt
STATUS: 200
177: From Wiktionary, the free dictionary
210: Inherited from Proto-Italic *juwō , from Proto-Indo-European *h₂yéwHō ( “ young ” ) . [ 1 ] Cognate with Sanskrit युवन् ( yúvan ) , Persian جوان ( jawān  / javân ) , Old Irish óc (early OIr: óac ), Old English ġeong (whence English young ). The Latin nominative singular form iuvenis is an innovation replacing expected *iuvō (compare Sanskrit य
=== https://en.wiktionary.org/wiki/iugum
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5f14697617ba51f1.txt
STATUS: 200
173: From Wiktionary, the free dictionary
194: From Proto-Italic *jugom , from Proto-Indo-European *yugóm , from *yewg- ( “ to yoke, harness, join ” ) + *-óm . [ 1 ] Cognate with Sanskrit युग ( yuga ) , Ancient Greek ζῠγόν ( zŭgón ) , and Gothic 𐌾𐌿𐌺 ( juk ) . Equivalent to a substantivization of the adjective iugus ( “ belonging together ” ) .
=== https://en.wiktionary.org/wiki/%CE%B6%CF%85%CE%B3%CF%8C%CE%BD
/home/sfmqrb/git/rishe-private/data/verification/sources/web/80d2983cbe3dcaf2.txt
STATUS: 200
161: From Wiktionary, the free dictionary
174: Inherited from Proto-Hellenic *dzugón , from Proto-Indo-European *yugóm . [ 1 ] 
=== https://en.wiktionary.org/wiki/iuvencus
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8ceb2a7077107674.txt
STATUS: 200
151: From Wiktionary, the free dictionary
159: From Proto-Italic *juwenkos , from Proto-Indo-European *h₂yuHn̥ḱós , equivalent to iuvenis +‎ -cus . De Vaan suggests that Latin -enc- instead of -inc- is explainable either as a Sabellicism or as the result of analogical remodeling after iuvenis or iuventus . [ 1 ]
```


## [2026-10-17T00:34:52.131Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'iugo-m|iugom|iu-go-m|ieu-g|juvenis|iuu̯en|iuven' incoming/WLD/WLD_Bd1_pages.txt | head -8; echo SKT; grep -n -E '^(Yoke|Young|Yoga|Join|Adjust|Junior|Juvenile|Conjugate|Youth|Youngster)\\b' SKT.txt | head -12",
 "description": "Grep Walde-Pokorny and Skeat"
}
```


### [2026-10-17T00:34:52.444Z] TOOL RESULT

```
18310:gen. yiino „Jiingling“; lat. juvenis ..jung; Jiingling, Jungfrau" (zu -ven-
18311:statt -vin- hier                         wie           in    iuvencus richtig Juret Dominance et resistance 204)
SKT
370:Adjust;  sec  Just.  %  Not  from ajostir,  mod.  F.  ajeuttr.
21798:Yoke.  sb.  (E)  M.  E^a^i.  A.S.  ^wv^ ^/w,  toe,  a  yoke  for  OKcn.-#-Du.  /uk,  Icel, oi.  Dan.  aa^.  Swed.  oi,  Goth,  jui,  G  /a-*!, W,  iau,  L.  iug'um,  Russ.  i]^'tf.  Lith./«/fiw/. Gk,  Cn^°''i  '^'^t*  y**ff'*>  ^  yoke,  a  couple. Lit.  '  thai  which  joins ; '  all  from  ^YUG, to  ioin.     See  Join.     Vet.yoJte,  verb.
21804:Young.  (E.)  M.  E  yong,  yteng.  A.  S. gt<*^S,  gi**rtg.  rung,  )oung.  +  Dn,  j^g, Icel.  ungr,  jungr.  Dan  Swed.  ung,  u. junt^,  Goth,  juggs  (written  for  jungs*\. p,  T htw  forms  answer  to  Lat  iuHttttus.  a young  animal,  heifer,  W.  iettanc^  yoang; ol  her  forms(withont  the  final  galluran occur in  L.  iuuenUt  Lith.  jaunas,  Skt.  yux>an, youn)^,  Uuss.  iunuH,  young.  "D^x.yQung- ting.  youngster :  also  youn-ker,  borrowed from  Vvi.  Jffnker^  Jonkheer,  i.e.  young  sir. compounded  of  Jong,  young,  and  A/rr,  sir^ a  lord.
```


## [2026-10-17T00:34:57.212Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'jugum|yugá-|„Joch' incoming/WLD/WLD_Bd1_pages.txt | head -5; awk 'NR<18310 && /\\[pdf page/ {p=$0} END{}; NR==18310{print p}' incoming/WLD/WLD_Bd1_pages.txt; grep -n -E '^(Join|Junior|Juvenile|Conjugate)' SKT.txt | head",
 "description": "Locate WLD yoke and page tags; Skeat join"
}
```


### [2026-10-17T00:34:57.562Z] TOOL RESULT

```
6640:jermen „Jochriemen, Riemen“ mit Anlautdehnung nach Pedersen KZ. 3S,
18463:   Ai. yugd- n. „Joch; Paar 44 = gr. jvyov „Joch (zum 'Q- siehe Sommer                                                           44
18468:umbr. Igucium), got. as. juk n., ags. geoc anord. ok „Joch      ahd. juh,                                      ,
18497:                                    acorn, ieu, bret. ieo, geo „Joch“ (aber nir.
18519:leitungen ai. yugald- n. „Paar 44 lat. jugidum (Demin.) „Jochbein, Schliissel-
```


## [2026-10-17T00:35:03.624Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for w in قسطاس قسط زوج یوغ جفت جوان; do u=\"https://vajehyab.com/moein/$w\"; f=$(python3 tools/fetch_source.py \"$u\" --note \"page 565 Mo'in entry $w\" 2>&1 | tail -1); echo \"=== $w $f\"; sed -n 3p $f; grep -n -E '\\[(ع|په|یو|تر|سر)' $f | head -3 | cut -c1-300; done",
 "description": "Fetch Mo'in entries from vajehyab",
 "timeout": 300000
}
```


### [2026-10-17T00:35:06.608Z] TOOL RESULT

```
=== قسطاس /home/sfmqrb/git/rishe-private/data/verification/sources/web/21de309107d0c392.txt
STATUS: 200
=== قسط /home/sfmqrb/git/rishe-private/data/verification/sources/web/214e0d580c724152.txt
STATUS: 200
=== زوج /home/sfmqrb/git/rishe-private/data/verification/sources/web/a577d4d75416ad01.txt
STATUS: 200
=== یوغ /home/sfmqrb/git/rishe-private/data/verification/sources/web/06ad723b8aac302c.txt
STATUS: 200
=== جفت /home/sfmqrb/git/rishe-private/data/verification/sources/web/5f2ca8f3272aa221.txt
STATUS: 200
=== جوان /home/sfmqrb/git/rishe-private/data/verification/sources/web/cd7e7d95f6bef5cb.txt
STATUS: 200
```


## [2026-10-17T00:35:10.902Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 21de309107d0c392 214e0d580c724152 a577d4d75416ad01 06ad723b8aac302c 5f2ca8f3272aa221 cd7e7d95f6bef5cb; do echo \"##### $f\"; grep -n -E 'معین|\\(اِ\\.|\\(ص\\.|ع\\.\\]|په\\.\\]|\\[ ?ع|\\[ ?په' $f.txt | head -4 | cut -c1-300; done",
 "description": "Extract Mo'in entry lines"
}
```


### [2026-10-17T00:35:11.248Z] TOOL RESULT

```
##### 21de309107d0c392
4:TITLE: معنی قسطاس | فرهنگ انتشارات معین | واژه یاب
6:معنی قسطاس | فرهنگ انتشارات معین | واژه یاب 
16: فرهنگ انتشارات معین
17: (قُ یا قِ) [ ع . ] (اِ.) ترازو، ترازوی بزرگ .
##### 214e0d580c724152
4:TITLE: معنی قسط | فرهنگ انتشارات معین | واژه یاب
6:معنی قسط | فرهنگ انتشارات معین | واژه یاب 
16: فرهنگ انتشارات معین
17: (قِ) [ ع . ] (اِ.) 1 - عدل و داد. 2 - بهره ، نصیب . 3 - قسمتی از یک کل که در فاصله های مساوی با کمیت های مساوی دریافت یا پرداخت می شود.
##### a577d4d75416ad01
4:TITLE: معنی زوج | فرهنگ انتشارات معین | واژه یاب
6:معنی زوج | فرهنگ انتشارات معین | واژه یاب 
16: فرهنگ انتشارات معین
17: (زُ) [ ع . ] (اِ.) 1 - شوهر. 2 - عددی که بر 2 بخش پذیر باشد.
##### 06ad723b8aac302c
4:TITLE: معنی یوغ | فرهنگ انتشارات معین | واژه یاب
6:معنی یوغ | فرهنگ انتشارات معین | واژه یاب 
16: فرهنگ انتشارات معین
17: (اِ.) چوبی که هنگام شخم زدن زمین بر گردن گاو می گذارند.
##### 5f2ca8f3272aa221
4:TITLE: معنی جفت | فرهنگ انتشارات معین | واژه یاب
6:معنی جفت | فرهنگ انتشارات معین | واژه یاب 
16: فرهنگ انتشارات معین
17: ( ~.) [ په . ] (اِ.) 1 - زوج ، دو عدد از یک چیز. 2 - زن و شوهر، همسر. 3 - همتا، همانند. 4 - همراه ، همدم .
##### cd7e7d95f6bef5cb
4:TITLE: معنی جوان | فرهنگ انتشارات معین | واژه یاب
6:معنی جوان | فرهنگ انتشارات معین | واژه یاب 
16: فرهنگ انتشارات معین
17: (جَ) [ په . ] (ص . اِ.) هر چیز کم سن . مق پیر.
```


## [2026-10-17T00:35:15.643Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n -E 'یوغ|جوان|جفت' ARY_pages.txt | head -8 | cut -c1-250; grep -n -E '\\b(YUGH|YUQ|JOFT|JAVAN|JAVĀN|YOUGH)\\b' ARY_latin_index_pages.txt | head -5",
 "description": "Grep Aryanpur for the Persian words"
}
```


### [2026-10-17T00:35:16.204Z] TOOL RESULT

```
1089:ابدی بود. آنان با پیروی از آرمان‌های ی که در صدر آن جوانمردی و مروت و شجاعت قرار داشت در
1394:واجریشه‌یابی این واژه‌ها و صدها واژه‌ی دیگر را به پژوهشگران جوانتر واگذار می‌کنم.
1933:آلیز آلیزیدن» آلیختن(به چم *جفتک انداختن») / ۶۹
3646:۶ برّنا (بة چم "جوان* و "نرچه")
5639:چم این واژه در زبان‌های اوستایی و سانسکریت: جوان)تر و تازه.
5756:آلمانی کهن ((05794۸ 107 صان): ایرلندی کهن (نزولم! صاه). جفتاتمهی7 ۱
6353:| جوانگلیس سواژی ناش ری ۱38
6171:UNG (NORWEGIAN) 8335 JAVAN X(BALUCHI) gz sh
6172:JONG DUTCH) gala = ZWAN, JAVAN. (AFGHAND) (+4) gsi
```


## [2026-10-17T00:35:20.610Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n '6160,6175p' ARY_latin_index_pages.txt | cut -c1-200; awk 'NR<=6171 && /\\[pdf page/ {p=$0} NR==6171{print p; exit}' ARY_latin_index_pages.txt; grep -n -E 'YUGA|YOKE|JUGUM|YUJ' ARY_latin_index_pages.txt | head -5",
 "description": "Read Aryanpur index around JAVAN"
}
```


### [2026-10-17T00:35:20.987Z] TOOL RESULT

```
BUCK: 516 JECZMIEN POLISH) glo)
‘MALLORY & ADAMS: JEvOS ‘OVIN, JEVIN (RUSSIAN) .o9,
ow seb day JACHMEN (SLOVAK), $1 jlet
cetlool
waytg: OWI OSE F gba 4 alia! He hdl) Ha PU or!
Sa a REGS Rte rm a so
JUVAN, YUVAN = (PAHLAVI) 5h, YUVAN, YONO = {AVESTAN) p=!
[pdf page 214]
os
| NNO | tse het ye
| UNG (SWEDISH) 5-8 y= JIWAN, JUVAN (KURDISH) 62,5
UNG (NORWEGIAN) 8335 JAVAN X(BALUCHI) gz sh
JONG DUTCH) gala = ZWAN, JAVAN. (AFGHAND) (+4) gsi
:(OLD CHURCH SLAVIC) 34S 5.33! yuvas, (SANSKRIT) <4 Site
JUNT YUVASAS, YUVAN, YONAS, JUVACAS
JUNYJ (RUSSIAN) 53 ARMENIAN) gs,
[pdf page 214]
15788:YUGA, YUGAM, YUNAKTI YAOG 4AVESTAN) gle!
15791:JUGUM, JUNGERE = (LATIN) gs JUGH HAPGHANI) (24) gil
15802:YUKAN, YUGAN (HITTITE) cea JOH (OLD HIGH GERMAN) oS glST
15806:BARNHART: (YOKE) 1254 YOKE HENGLISH) ood&3t
15808:MACKENZIE: (YOKE) 141 OK (SWEDISH) 28 y
```


## [2026-10-17T00:35:24.784Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n '15780,15800p' ARY_latin_index_pages.txt | cut -c1-160; awk 'NR<=15788 && /\\[pdf page/ {p=$0} NR==15788{print p; exit}' ARY_latin_index_pages.txt",
 "description": "Read Aryanpur yoke entry"
}
```


### [2026-10-17T00:35:25.259Z] TOOL RESULT

```
DELAMARRE: (UN) 209 EEN DUTCH) «sacha
MACKENZIE: (ONE) 125 (OLD CHURCH SLAVIC) 55 y3ee\
BUCK: 937-939 IND, JEDAN
ONIONS: (ONE) 627 JEDEN POLISH) ging)
SKEAT: (ONE) 411] © RUSSIAN) gay)
rrr. 1ebb olny ODIN, JEDNA, JEDNO
aes
j
YUGA, YUGAM, YUNAKTI YAOG 4AVESTAN) gle!
ZOUYK, ZOUKEL (ARMENIAN) JHUGH, AYOXTAN :(PAHLAVD sy
ZYGON, ZEUGNYNAI (GREEK) Jy JOGH ABALUCHD) gh
JUGUM, JUNGERE = (LATIN) gs JUGH HAPGHANI) (24) gil
JouG (FRENCH) 4.315 YOKAM s(TOKHARIAN A) A 15 )\o5
YUGO SPANISH) glial SANSKRIT) 4 Sail
[pdf page 541]
forse | ony
JUNGAS, JUNGTL (LITHUANIAN) gly) GI0Go A(ITALIAN) gids
jues (LATVIAN) (33) gis) JUG :(RUMANIAN) ley)
conc (oLpytisfy aS sl! JUGO, JUNTA (PORTUGUESE) Js
a H(GAULISH) JS JUK GOTHIC) 53,
TAU (WELSH) «$39 OK :(OLD SCANDINAVIAN) oS tte!
[pdf page 540]
```


## [2026-10-17T00:35:47.754Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; mkdir -p data/verification/sources/refs/ocr/BOOK; pdftoppm -f 565 -l 565 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf data/verification/sources/refs/ocr/BOOK/565 && command ls -la data/verification/sources/refs/ocr/BOOK/565.png",
 "description": "Render printed page 565 to PNG for audit"
}
```


### [2026-10-17T00:35:48.922Z] TOOL RESULT

```
-rw-r--r-- 1 sfmqrb sfmqrb 82767 Oct 16 20:35 data/verification/sources/refs/ocr/BOOK/565.png
```


## [2026-10-17T00:38:59.756Z] TOOL CALL #43: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-565.py",
 "content": "import json\nW = \"https://en.wiktionary.org/wiki/\"\nU_YEWG = W + \"Reconstruction:Proto-Indo-European/yewg-\"\nU_ZAWJ = W + \"%D8%B2%D9%88%D8%AC\"\nU_QISTAS = W + \"%D9%82%D8%B3%D8%B7%D8%A7%D8%B3\"\nU_QIST = W + \"%D9%82%D8%B3%D8%B7\"\nU_YUG = W + \"%DB%8C%D9%88%D8%BA\"\nU_JOFT = W + \"%D8%AC%D9%81%D8%AA\"\nU_JAVAN = W + \"%D8%AC%D9%88%D8%A7%D9%86\"\nU_IUXTA = W + \"iuxta\"\nU_SEXT = W + \"sextarius\"\nU_JUNGAZ = W + \"Reconstruction:Proto-Germanic/jungaz\"\nU_YUVAN = W + \"%E0%A4%AF%E0%A5%81%E0%A4%B5%E0%A4%A8%E0%A5%8D\"\nU_YOGA = W + \"yoga\"\nU_ADJUST = W + \"adjust\"\nU_YOUNG = W + \"young\"\nU_YOKE = W + \"yoke\"\nU_IUVENIS = W + \"iuvenis\"\nU_IUGUM = W + \"iugum\"\nU_ZUGON = W + \"%CE%B6%CF%85%CE%B3%CF%8C%CE%BD\"\nU_IUVENCUS = W + \"iuvencus\"\nM = \"https://vajehyab.com/moein/\"\nM_QISTAS, M_QIST, M_ZAWJ, M_YUG, M_JOFT, M_JAVAN = (M + w for w in [\"قسطاس\", \"قسط\", \"زوج\", \"یوغ\", \"جفت\", \"جوان\"])\n\nPOK509 = {\"ref\": \"POK:509\", \"status\": \"supports\", \"note\": \"POK_02.txt leaves 166-168 (pp. 508-510), '2. ieu-, ieu-g- \\\"verbinden\\\"': 'iu-go-m \\\"Joch\\\": ai. yugá- ... gr. ζυγόν ... lat. jugum ... got. juk'; 'av. yaoj-, yuj- \\\"anspannen, anschirren\\\"'; 'Partiz. ai. yuktá-, av. yuxta-'; 'lat. jungō'; 'Superl. *iugistos in lat. juxtā (*jugistā, scil. viā)'; 'ai. yóga- m. \\\"das Anschirren, Verbindung\\\"'.\"}\nPOK_C = {\"src\": \"POK\", \"where\": \"pp. 508-510 (POK_02.txt leaves 166-168)\", \"stance\": \"supports\", \"note\": \"'2. ieu-, ieu-g- \\\"verbinden\\\"' with yugá-, ζυγόν, jugum, juk, av. yaoj-/yuj-, yuxta-, juxtā < *jugistā, yóga-.\"}\nWLD_C = {\"src\": \"WLD\", \"where\": \"Bd. I, s.v. 2. i̯eu-g- (WLD_Bd1_pages.txt l. 18463 ff.)\", \"stance\": \"supports\", \"note\": \"'Ai. yugá- n. \\\"Joch; Paar\\\" = gr. ζυγόν \\\"Joch\\\" ... umbr. Iguvium), got. as. juk n., ags. geoc anord. ok \\\"Joch\\\", ahd. juh'.\"}\nAHD_C = {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. yeug- (l. 1198)\", \"stance\": \"supports\", \"note\": \"'yeug-. To join. ... *yug-o- in: a. Germanic *yukam in Old English geoc, yoke: YOKE; b. Latin jugum ...; c. Greek zugon, yoke ...; d. Sanskrit yugam ... 2. Suffixed (superlative) form *yug-istos in Latin *jugistā (via), \\\"on a nearby (road),\\\" contracted to juxtā, close by: JOUST; ADJUST ... 3. Nasalized form *yu-n-g- in Latin jungere, to join: JOIN ... III. *youg-o- in Sanskrit yogah, union: YOGA. [Pok. 2. ieu- 508.]'\"}\nAHD_R = {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l. 1198 s.v. yeug-: 'Germanic *yukam in Old English geoc ... Latin jugum ... Greek zugon ... Sanskrit yugam ... Latin *jugistā (via) ... juxtā ... Latin jungere, to join: JOIN ... CONJUGATE ... ADJUST ... Sanskrit yogah, union: YOGA'.\"}\nSYN_YOKE = {\"src\": \"SYN\", \"where\": \"§10.78 YOKE (SYN.txt l. 18354-18359)\", \"stance\": \"supports\", \"note\": \"'Skt. yuga-m (Av. form not quotable, but NPers. juy, etc.); Hitt. yugan' — one IE word for 'yoke'.\"}\nKLN_JOIN = {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. join (l. 20345)\", \"stance\": \"supports\", \"note\": \"'L. jungere ... cogn. with OI. yunákti ... Gk. ζευγνύναι ... Avestic yaoj-, yuj-, \\\"I harness\\\", yuxta-, \\\"harnessed\\\" ... I.-E. base *yeug-, \\\"to join, unite\\\"'.\"}\nKLN_YOUNG = {\"src\": \"KLN\", \"where\": \"KLN_1971.txt s.v. young (l. 270049 ff.)\", \"stance\": \"supports\", \"note\": \"'OE. geong ... Goth. juggs ... cogn. with L. juvencus, \\\"a young bullock; a young man\\\", juvenca, \\\"a young cow; a young woman\\\" ... OI. yuvaśáh, \\\"youthful; young man, youth\\\" ... fr. I.-E. *yuwnkos, a derivative of *yuwn-, ... base *yeu-, \\\"young\\\", whence OI. yuvā, yuvan-, ... Avestic yvan- (gen. yūn-ō) ... L. juvenis'.\"}\nPOK510 = {\"ref\": \"POK:510\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 169 (p. 510), '5. ieu- \\\"jung\\\". Positiv iuuen- (: iūn-)': 'Ai. yúvan- ... av. yvan-, yavan- (beides für yuvan- geschrieben), Gen. yūnō \\\"Jüngling\\\"; lat. juvenis'; derivatives 'ai. yuvaśá-h ... lat. juvencus, -a \\\"junger Stier, junge Kuh\\\" ... got. juggs ... (urg. *jungaz aus *juwungáz)'.\"}\nPOK510_C = {\"src\": \"POK\", \"where\": \"p. 510 (POK_02.txt leaf 169)\", \"stance\": \"supports\", \"note\": \"'5. ieu- \\\"jung\\\"': yúvan-, av. yvan-/yavan-, juvenis, yuvaśá-, juvencus, urg. *jungaz aus *juwungáz.\"}\nWLD_Y = {\"src\": \"WLD\", \"where\": \"Bd. I s.v. i̯eu- 'jung' (WLD_Bd1_pages.txt l. 18310)\", \"stance\": \"supports\", \"note\": \"'... gen. yūno \\\"Jüngling\\\"; lat. juvenis \\\"jung; Jüngling, Jungfrau\\\" (zu -ven- statt -vin- ... wie in iuvencus'.\"}\nAHD_Y = {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. yeu- (l. 1195)\", \"stance\": \"supports\", \"note\": \"'yeu-. Vital force, youthful vigor ... variant of aiw-. Suffixed zero-grade form *yuwen- ... *yuwn-ti- in Germanic *jugunthi- ... OE geoguth: YOUTH ... *yuwn-ko- in Germanic *juwungaz becoming *jungaz in OE geong: YOUNG ... Latin iuvenis, young: JUNIOR, JUVENILE. [Pok. 3. ieu- 510.]'\"}\nSYN_Y = {\"src\": \"SYN\", \"where\": \"§14.14 YOUNG (SYN.txt l. 24421-24428)\", \"stance\": \"supports\", \"note\": \"'Skt., Av. yuvan-, yūn- (Av. quotable only as sb. \\\"young man\\\") ... Goth. juggs ... cf. Lat. iuvencus, -a \\\"steer, heifer\\\", ... Skt. yuvaśa- \\\"youthful\\\"'.\"}\nSKT_YOKE = {\"src\": \"SKT\", \"where\": \"SKT.txt s.v. Yoke (l. 21798)\", \"stance\": \"supports\", \"note\": \"'Yoke ... A.S. geoc ... L. iugum ... Gk. ζυγόν ... all from √YUG, to join. See Join.'\"}\nSKT_YOUNG = {\"src\": \"SKT\", \"where\": \"SKT.txt s.v. Young (l. 21804)\", \"stance\": \"supports\", \"note\": \"'Young ... A.S. geong ... Goth. juggs ... answer to Lat. iuuencus ... L. iuuenis, Lith. jaunas, Skt. yuvan, young ... youngster'.\"}\nPHD_JUG = {\"src\": \"PHD\", \"where\": \"PHD.txt l. 414\", \"stance\": \"supports\", \"note\": \"'jug [ywg | N ~] yoke' and 'juxt [ywht | (P ywxt), N juft] pair, couple'.\"}\nNYB_YUXT = {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt l. 4482\", \"stance\": \"supports\", \"note\": \"'yuxt [ywht] a pair ... Av. yuxta- \\\"a team of horses\\\"; NP juft < *juxt \\\"a yoke, a couple, a pair\\\", from yaog-'.\"}\n\ndef node(id, lang, words, verdict, der, der_fa, sources, ref_check, consulted, **extra):\n    d = {\"id\": id, \"lang\": lang, \"words\": words, \"verdict\": verdict, \"derivation\": der, \"derivation_fa\": der_fa,\n         \"sources\": sources, \"ref_check\": ref_check, \"consulted\": consulted}\n    d.update(extra)\n    return d\n\ne0_nodes = [\n node(1, \"Avestan\", \"yaoj, yuj; yuxta\", \"confirmed\",\n  \"Av. yaoj-/yuj- 'to yoke, harness' (Cheung *i̯au̯ǰ: OAv. aor. yaogət, subj. yaojā; YAv. pres. yujiieiti) is the regular Iranian continuant of PIE *yewg-/*yug- (PIE *y- kept, *g after *u > Av. j by Iranian palatalization in the present stem). The past participle yuxta- 'yoked, harnessed' < Proto-Iranian *yuxta- < PIE *yug-tó- (Bartholomae's Law does not apply; *g before t > x in Iranian), = Skt. yuktá-, Lat. iunctus. Nourai's gloss 'I harnessed' is taken verbatim from Klein, who glosses the root as 'Avestic yaoj-, yuj-, \\\"I harness\\\"' (i.e. a citation-form translation, not a 1st-person form).\",\n  \"اوستایی yaoj- / yuj- «بستن ستور به گردونه، یوغ کردن» بازماندهٔ منظم ریشهٔ هندواروپایی آغازین *yewg- / *yug- است و صفت مفعولی آن yuxta- «به یوغ بسته، جفت‌شده» از ایرانی باستان *yuxta- (گ پیش از ت در ایرانی به خ بدل شده) است، هم‌ریشه با سنسکریت yuktá- و لاتین iunctus. بارتولومه (ستون ۱۲۲۸) و چونگ همین را می‌گویند. معنای «مهار کردم» که نورایی آورده از کلاین گرفته شده که ریشه را با «I harness» ترجمه کرده است. ادعای نورایی درست است.\",\n  [U_YEWG],\n  [POK509,\n   {\"ref\": \"BQT:577\", \"status\": \"supports\", \"note\": \"No page scan covers printed p. 577 (ref_page.py: 'no scan of BQT covers printed page 577'), but the OCR text BQT_v2.txt l. 2878 (Mo'in's footnote to جفت, the entry Nourai cites) reads: '... (بگردونه بستن). پهلوی juxt (اتحاد، زوج)، ارمنی juxtak (زوج)، هندی باستان yukta ...' — i.e. joft from the Avestan root 'to yoke a horse to a chariot'. Page number not verifiable from the OCR.\"},\n   {\"ref\": \"BQT:1228\", \"status\": \"not_found\", \"note\": \"BQT p. 1228 (vol 3 pdf p. 19, ocr/BQT/1228.txt) carries شاکمونی – شالده – شالهنگ, nothing on yoke. '1228' is in fact Bartholomae's column number cited inside Mo'in's footnote at BQT 2458 ('ازریشهٔ اوستایی yaog (اسب را بگردونه بستن) «بارتولومه ۱۲۲۸-۲۹»'); Nourai copied it as a BQT page.\"},\n   {\"ref\": \"BQT:2458\", \"status\": \"supports\", \"note\": \"BQT p. 2458 (vol 4 pdf p. 541; read from the image, saved as ocr/BQT/2458.vision.txt), footnote 3 to یوغ: '= جوغ = جغ = جوه = جوخ = جو، افغانی jugh (یوغ گاوآهن) «هوبشمان ۴۲۳»؛ سانسکریت yôga، بلوچی jôgh ... ازریشهٔ اوستایی yaog (اسب را بگردونه بستن) «بارتولومه ۱۲۲۸-۲۹»'.\"}],\n  [{\"src\": \"BRT\", \"where\": \"BRT.txt l. 20927 s.v. yaog-; yuxta- passim (e.g. l. 5724 'aurvanta yuxta')\", \"stance\": \"supports\", \"note\": \"headword 'yaog-' (col. 1228 f.); yuxta- 'geschirrt' in Yt 5.50 etc.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt l. 14610 ff. s.v. *i̯au̯ǰ\", \"stance\": \"supports\", \"note\": \"'*i̯au̯ǰ \\\"to harness, yoke, employ\\\" *AVESTAN: yūj- \\\"to harness\\\" ... OAv. yaogət ... Partic.: perf. pass. YAv. yuxta- (Y 49.9, Yt 5.50, Yt 9.2)'; MP (+ā-) ayōz-, ayuxt.\"},\n   KLN_JOIN, POK_C, WLD_C, AHD_C]),\n node(2, \"Persian\", \"yŭğ; joft\", \"confirmed\",\n  \"NP yuġ/yōġ 'yoke' is a variant of juġ/joġ (Borhan: = جوغ = جغ = جوه = جوخ = جو) < MP jug [ywg] 'yoke' < Proto-Iranian *yugám < PIE *yugóm (= Skt. yugá-, Gk. zugón, Lat. iugum). Initial Old Iranian *y- regularly becomes MP/NP j-; the y- of یوغ is a learned/dialectal by-form (Wiktionary: 'from earlier joġ'). NP joft 'pair' < MP juxt [ywht] 'pair, couple' (Parthian ywxt) < Av. yuxta- 'yoked' (PIE *yug-tó-), with the regular NP change xt > ft (cf. Hübschmann: 'Ap. xt wird im Np. zu ft in juft'); Armenian borrowed the MP word as zoyg/juxtak 'pair'. Semantic shift 'yoked (team)' > 'pair'.\",\n  \"«یوغ» (و گونه‌های جغ، جوغ، جوه، جوخ) از فارسی میانهٔ jug «یوغ»، از ایرانی باستان *yugam و هندواروپایی آغازین *yugóm است، هم‌ریشه با سنسکریت yuga و یونانی zugon و لاتین iugum؛ ی آغازی ایرانی باستان در فارسی میانه و نو به ج بدل می‌شود و صورت «یوغ» گونه‌ای کتابی یا گویشی است. «جفت» از فارسی میانهٔ juxt «جفت، زوج»، از اوستایی yuxta- «به یوغ بسته» است و خت فارسی میانه در فارسی نو به فت بدل شده است. مکنزی، نیبرگ، هوبشمان، معین در حاشیهٔ برهان قاطع و ویکی‌واژه همه همین را می‌گویند؛ ادعای نورایی درست است.\",\n  [U_YUG, U_JOFT, M_YUG, M_JOFT],\n  [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own; the parent's BQT:2458 (یوغ) and BQT:577 (جفت) footnotes cover it (see node 1).\"}],\n  [PHD_JUG, NYB_YUXT,\n   {\"src\": \"HUB\", \"where\": \"HUB.txt l. 5395, l. 8960\", \"stance\": \"supports\", \"note\": \"'juxtak ein Paar (Turteltauben, 5. Jhd.), np. juft \\\"Paar\\\", zd. yuxta- \\\"Gespann\\\"'; 'Ap. xt wird im Np. zu ft in juft'.\"},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt l. 6793 (footnote)\", \"stance\": \"partial\", \"note\": \"only in passing: 'vergl. juft aus *juxt'; no separate Horn paragraph for juġ found by grep.\"},\n   {\"src\": \"BQT\", \"where\": \"p. 2458 footnote 3 (ocr/BQT/2458.vision.txt)\", \"stance\": \"supports\", \"note\": \"'یوغ ... = جوغ = جغ ... ازریشهٔ اوستایی yaog'.\"},\n   {\"src\": \"MON\", \"where\": M_YUG + \" ; \" + M_JOFT, \"stance\": \"supports\", \"note\": \"یوغ: '(اِ.) چوبی که هنگام شخم زدن زمین بر گردن گاو می گذارند'; جفت: '[په.] (اِ.) ۱- زوج، دو عدد از یک چیز' — Pahlavi origin.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt l. 15788 ff. ([pdf page 540-541], یوغ)\", \"stance\": \"supports\", \"note\": \"'YUGA, YUGAM, YUNAKTI (SANSKRIT); YAOG (AVESTAN); JHUGH, AYOXTAN (PAHLAVI); JOGH (BALUCHI); JUGH (AFGHANI); ZYGON (GREEK); JUGUM (LATIN)'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *i̯au̯ǰ (l. 14619 ff.)\", \"stance\": \"partial\", \"note\": \"gives MP ayōz-/ayuxt, abyōz- from the verb; the nouns juġ/joft are not treated.\"}]),\n node(3, \"Greek\", \"zugon, zygos, sextarious\", \"disputed\",\n  \"Gk. zugón / zugós 'yoke; cross-beam of a balance, (pair of) scales' < Proto-Hellenic *dzugón < PIE *yugóm (PIE *y- > Gk. z- in this word): confirmed. 'zygos' is only a second romanization of the same ζυγός. But 'sextarious' (sic; correctly Latin sextārius) is neither Greek nor from *yewg-: it is the Latin measure 'one-sixth (of a congius)', from sextus 'sixth' + -ārius (PIE *swéks 'six'), which Greek borrowed as ξέστης. Nourai has merged Dvořák's proposal (qisṭās < ξέστης < sextarius, reported by Jeffery FVQ 239) with Vullers' (qisṭās < ζυγός) into one Greek node. Verdict for zugon/zygos: confirmed; for sextarious: disputed (unrelated root, wrong language label, misspelled).\",\n  \"یونانی zugon / zugos «یوغ؛ شاهینِ ترازو، ترازو» از یونانی آغازین *dzugón و هندواروپایی آغازین *yugóm است و درست است (zygos فقط آوانویسی دیگری از همان واژه است). اما sextarious (درستش لاتین sextārius) نه یونانی است و نه از ریشهٔ *yewg-؛ این واژه نام پیمانه‌ای رومی به معنای «یک‌ششم» است، از sextus «ششم» (ریشهٔ هندواروپایی *swéks «شش»)، که یونانی آن را به صورت xestēs وام گرفته است. نورایی دو پیشنهاد متفاوت برای ریشهٔ «قسطاس» را که جفری (ص ۲۳۹) نقل کرده، یعنی از zygos (فولرس) و از xestēs < sextarius (دووراک)، در یک خانه آورده است. پس zugon درست است ولی sextarius به این ریشه ربطی ندارد.\",\n  [U_ZUGON, U_SEXT],\n  [POK509, AHD_R,\n   {\"ref\": \"VDQ:346\", \"status\": \"partial\", \"note\": \"VDQ (Persian translation of Jeffery) not accessible (noorlib viewer JS-only); checked the original FVQ pp. 238-239 s.v. Qisṭās: 'Vullers ... thought that it was probably a mangling of the Gk. ζυγός a yoke, and Dvořák ... would derive it from ξέστης from the Lat. sextarius used as a measure' — Jeffery reports both as the philologers' Greek theory and prefers an Aramaic/Syriac source. So the page gives Nourai his three forms but does not support deriving sextarius from *yewg-.\"}],\n  [POK_C, WLD_C, AHD_C,\n   {\"src\": \"FVQ\", \"where\": \"pp. 238-239 s.v. Qisṭās (FVQ.txt l. 14865-14935)\", \"stance\": \"partial\", \"note\": \"zygos and xestēs/sextarius are two separate proposals for qisṭās; sextarius is a Latin measure.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. Yoke (l. 21798)\", \"stance\": \"supports\", \"note\": \"'Gk. ζυγόν ... all from √YUG, to join' (zugon only).\"}]),\n node(4, \"Arabic\", \"zawj\", \"confirmed\",\n  \"Ar. zawj 'one of a pair, mate, spouse; pair, kind' is an early loan (pre-Islamic poetry, Qur'an ii 33 etc.) from Aramaic zūgā/zawgā 'yoke, pair', itself from Gk. zeûgos 'yoke of beasts, pair' (PIE *yewg-es-, the e-grade s-stem, not zugón); Ethiopic also has it. Arabic then built a triliteral root z-w-j (zawwaja 'to marry', tazwīj, izdiwāj, muzdawij) from the noun. Fraenkel (AFA 107) and Jeffery (FVQ 154-155) say exactly this; Nourai's note 'reached Arabic through another language' = Aramaic is correct. Strictly the Greek source is ζεῦγος, a sister form of the ζυγόν in node 3.\",\n  \"عربی «زَوج» «یکی از جفت، همسر، جفت» وام‌واژه‌ای بسیار کهن (در شعر جاهلی و قرآن) از آرامی zawgā / zūgā «یوغ، جفت» است که خود از یونانی zeugos «جفت ستوران زیر یوغ، جفت» (از *yewg-es- هندواروپایی) گرفته شده است. عرب‌ها از این اسم ریشهٔ سه‌حرفی ز-و-ج ساختند و تزویج و ازدواج و مزدوج از آن برآمد. فرانکل و جفری همین را می‌گویند و یادداشت نورایی که واژه «از راه زبانی دیگر» به عربی رسیده (یعنی آرامی) درست است؛ فقط صورت یونانیِ دقیق zeugos است نه zugon.\",\n  [U_ZAWJ],\n  [{\"ref\": \"VDQ:239\", \"status\": \"supports\", \"note\": \"VDQ not accessible online (JS-only noorlib viewer); verified through the original FVQ pp. 154-155 s.v. Zawj: 'It is a very early loan-word in Arabic from Gk. ζεῦγος through the Aram. The verbal forms ... are clearly denominative ... no derivation of the word is possible from Semitic material'.\"}],\n  [{\"src\": \"FVQ\", \"where\": \"pp. 154-155 (FVQ.txt l. 9782 ff.)\", \"stance\": \"supports\", \"note\": \"'a very early loan-word in Arabic from Gk. ζεῦγος through the Aram.'\"},\n   {\"src\": \"AFA\", \"where\": \"p. 107 (AFA.txt l. 4062-4070)\", \"stance\": \"supports\", \"note\": \"'... ζεῦγος in's Arab. übergegangen ist ... Keinem Araber ist je ein Zweifel gekommen, dass dies Wort echt sei. Es muss aus sehr alter Zeit stammen ... wohl auch von den Aramäern als zaug ... angenommen'.\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt grep 'zawj|zauj'\", \"stance\": \"silent\", \"note\": \"no entry for the Arabic word.\"},\n   {\"src\": \"AFM\", \"where\": \"AFM.txt grep 'زوج'\", \"stance\": \"silent\", \"note\": \"Addi Shir (Persian loans in Arabic) has no زوج entry — consistent with a non-Persian source.\"}]),\n node(5, \"Persian\", \"zowj\", \"confirmed\",\n  \"NP zowj (classical zawj) 'pair; even number; husband, spouse', with zowje 'wife', tazvij, ezdevāj, mozdavej, is the Arabic word (node 4) taken into Persian in the Islamic period together with its root derivatives (Mo'in tags it [ع.]). It is thus an Aramaic-Greek word re-entering Iran via Arabic, while inherited Persian joft and juġ (node 2) are its native cognates from the same PIE root (Wiktionary: 'Doublet of یوغ, also related to جفت').\",\n  \"«زوج» (زَوج / زُوج) با زوجه، تزویج، ازدواج و مزدوج وام‌واژه‌ای عربی است که در دورهٔ اسلامی به فارسی آمده (معین آن را [ع.] نشان می‌زند). این واژه از آرامی و در اصل از یونانی zeugos است و بدین‌سان با «جفت» و «یوغ» فارسی، که بازماندهٔ مستقیم همان ریشهٔ هندواروپایی‌اند، هم‌ریشه است؛ ویکی‌واژه هم آن را دوگانهٔ «یوغ» می‌داند. ادعای نورایی درست است.\",\n  [U_ZAWJ, M_ZAWJ],\n  [{\"ref\": \"FVA:180\", \"status\": \"not_checked\", \"note\": \"Nahvi's Farhang-e Vazheha-ye Arabi: no digital copy (refs_online.json: 'Catalogue record only').\"}],\n  [{\"src\": \"MON\", \"where\": M_ZAWJ, \"stance\": \"supports\", \"note\": \"'(زُ) [ع.] (اِ.) ۱- شوهر. ۲- عددی که بر ۲ بخش پذیر باشد' — Arabic loan.\"},\n   {\"src\": \"FVQ\", \"where\": \"pp. 154-155\", \"stance\": \"supports\", \"note\": \"the Arabic word itself from Gk. ζεῦγος via Aramaic.\"},\n   {\"src\": \"AFA\", \"where\": \"p. 107\", \"stance\": \"supports\", \"note\": \"zawj from ζεῦγος via Aramaic zaug.\"},\n   {\"src\": \"PLA\", \"where\": \"PLA_pages.txt grep 'zauǧ|زوج'\", \"stance\": \"silent\", \"note\": \"not among Asbaghi's Persian loans in Arabic (correctly: the direction is Arabic > Persian).\"}]),\n node(6, \"Arabic\", \"qest\", \"disputed\",\n  \"Ar. qisṭ 'justice, equity; share, portion; instalment' (Qur'an iii 18, iv 135, lv 9 etc.) is not from Greek zugón. Jeffery (FVQ 237-238), following Fraenkel (Fremdw. 205), takes it from Christian Aramaic: the Semitic root q-š-ṭ 'true, right' (Syriac qūštā 'truth, rectitude', Jewish Aram. qušṭā), which Arabic received as a loan. Wiktionary adds that the measure sense comes separately from Aramaic qesṭā < Medieval Greek xéstēs < Latin sextārius ('six'), so even that strand is unrelated to *yewg-. Its link to qisṭās (node 7) is a later Arabic association, not common descent from ζυγός. Modern view: unrelated to this root.\",\n  \"عربی «قِسط» «داد، انصاف؛ بهره، سهم؛ پاره‌ای از وام» از یونانی zugon نیست. جفری (ص ۲۳۷-۲۳۸) به پیروی از فرانکل آن را از آرامیِ مسیحی و ریشهٔ سامی ق-ش-ط «راست، درست» (سریانی qūštā «راستی، داد») می‌داند. ویکی‌واژه افزون بر این، معنای «پیمانه» را از آرامی qesṭā < یونانی میانه xestēs < لاتین sextārius می‌داند که آن هم به ریشهٔ *yewg- ربطی ندارد. پس پژوهش امروزی پیوند «قسط» با این ریشه را رد می‌کند.\",\n  [U_QIST],\n  [{\"ref\": \"VDQ:346\", \"status\": \"contradicts\", \"note\": \"VDQ itself not accessible; the original FVQ pp. 237-238 s.v. Qisṭ: 'The root קשט is widely used in Aramaic ... means truth, right ... Fraenkel is doubtless correct in taking the Ar. قسط as also of Aram., probably of Christian Aram. origin' — no Greek ζυγός.\"}],\n  [{\"src\": \"FVQ\", \"where\": \"pp. 237-238 s.v. Qisṭ (FVQ.txt l. 14812 ff.)\", \"stance\": \"contradicts\", \"note\": \"Aramaic q-š-ṭ 'truth, right'; a footnote mentions Latin iustitia or sextarius as other guesses.\"},\n   {\"src\": \"AFA\", \"where\": \"AFA.txt grep 'قسط|qisṭ'\", \"stance\": \"silent\", \"note\": \"the OCR yields no readable hit (Jeffery cites Fraenkel Fremdw. 205 for Aramaic origin).\"},\n   {\"src\": \"AFM\", \"where\": \"AFM.txt l. 5059\", \"stance\": \"silent\", \"note\": \"Addi Shir mentions القسطاس only as a gloss for the balance (s.v. قبّان); no Persian origin for قسط claimed.\"},\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt grep 'qist'\", \"stance\": \"silent\", \"note\": \"no entry.\"}]),\n node(7, \"Persian\", \"qest; qestâs\", \"disputed\",\n  \"NP qest 'justice; instalment (aqsāṭ)' and qestās 'balance, great scales' are Arabic loans (Mo'in: both [ع.]). qest: see node 6, from Aramaic q-š-ṭ, not *yewg- (disputed). qestās: Wiktionary derives Ar. qisṭās via Aramaic/Classical Syriac səgosṭārā from Gk. zugostátēs 'weigher' (zugón 'beam of the balance' + -statēs), influenced by qisṭ; that would make qestās ultimately a *yewg- word, as Nourai implies. Jeffery (FVQ 238-239) lists Vullers' ζυγός, Dvořák's ξέστης < sextarius and Vollers' δικαστής, and himself prefers Aramaic qisṭā 'measure'. qestās is therefore only plausible. The Khāqāni line (بقسطاسی بسنجم ...) illustrates the 'balance' sense. Node verdict = worst of the two words.\",\n  \"«قسط» (جمع: اقساط) و «قسطاس» «ترازو، ترازوی بزرگ» هر دو از عربی به فارسی آمده‌اند (معین: [ع.]). «قسط» چنان‌که در خانهٔ پیشین گفته شد از ریشهٔ آرامی ق-ش-ط است و به *yewg- ربطی ندارد. اما برای «قسطاس» ویکی‌واژه ریشه‌ای از راه سریانی səgosṭārā از یونانی zugostatēs «ترازودار، وزن‌کننده» (از zugon «شاهین ترازو») پیشنهاد می‌کند که اگر درست باشد قسطاس سرانجام به همین ریشه می‌رسد. جفری اما پیشنهادهای گوناگون (zygos، xestēs < sextarius، dikastēs) را می‌آورد و خود آرامی qisṭā «پیمانه» را ترجیح می‌دهد. پس «قسطاس» با احتیاط پذیرفتنی است ولی «قسط» را پژوهش امروزی از این ریشه نمی‌داند.\",\n  [U_QIST, U_QISTAS, M_QIST, M_QISTAS],\n  [{\"ref\": \"MON:2674\", \"status\": \"partial\", \"note\": \"printed page not mappable online (refs_online.json); vajehyab Mo'in text: قسط '(قِ) [ع.] (اِ.) ۱- عدل و داد. ۲- بهره، نصیب. ۳- قسمتی از یک کل که در فاصله‌های مساوی ... پرداخت می‌شود'; قسطاس '(قُ یا قِ) [ع.] (اِ.) ترازو، ترازوی بزرگ'. Supports the meanings and the Arabic origin only; says nothing of Greek.\"}],\n  [{\"src\": \"MON\", \"where\": M_QIST + \" ; \" + M_QISTAS, \"stance\": \"partial\", \"note\": \"both tagged [ع.], no further etymology.\"},\n   {\"src\": \"FVQ\", \"where\": \"pp. 238-239 s.v. Qisṭās\", \"stance\": \"partial\", \"note\": \"'Vullers ... a mangling of the Gk. ζυγός a yoke ... Dvořák ... from ξέστης from the Lat. sextarius ... much more hopeful to start from the Aram. qisṭā meaning measure ... Vollers ... from the Gk. δικαστής a judge'.\"},\n   {\"src\": \"AFM\", \"where\": \"AFM.txt l. 5059\", \"stance\": \"silent\", \"note\": \"القسطاس named only as the thing weighed with (s.v. قبّان); no etymology.\"},\n   {\"src\": \"TAD\", \"where\": \"TAD.txt grep 'قسطاس'\", \"stance\": \"silent\", \"note\": \"no readable hit.\"}]),\n node(8, \"Germanic\", \"yukam\", \"confirmed\",\n  \"Proto-Germanic *juką 'yoke' (AHD 1975 writes it *yukam) < PIE *yugóm, with Grimm's Law *g > *k and *-om > *-ą: Gothic juk, OS juk, OHG joh, ON ok, OE ġeoc. The chart's form is AHD's notation, not a misprint.\",\n  \"ژرمنی آغازین *juką «یوغ» (هریتیج آمریکن آن را *yukam می‌نویسد) از هندواروپایی آغازین *yugóm است؛ بنا بر قانون گریم g هندواروپایی در ژرمنی به k بدل شده است. گوتی juk، آلمانی کهن joh، نوردی کهن ok و انگلیسی کهن geoc بازماندهٔ آن‌اند. ادعای نورایی درست است.\",\n  [U_YOKE],\n  [AHD_R],\n  [AHD_C, POK_C, WLD_C, SYN_YOKE]),\n node(9, \"English\", \"yoke\", \"confirmed\",\n  \"English yoke < ME yok, ȝok < OE ġeoc, ġioc < Proto-West Germanic *juk < PGmc *juką (node 8); OE palatal ġ- [j] continues Gmc *j-.\",\n  \"انگلیسی yoke از انگلیسی میانهٔ yok و انگلیسی کهن geoc، از ژرمنی آغازین *juką است و هم‌ریشه با «یوغ» و «جفت» فارسی. ادعای نورایی درست است.\",\n  [U_YOKE],\n  [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on the node; parent's AHD s.v. yeug- covers 'Old English geoc, yoke: YOKE'.\"}],\n  [SKT_YOKE,\n   {\"src\": \"KLN\", \"where\": \"KLN_1971.txt s.v. yoke (l. 269930)\", \"stance\": \"supports\", \"note\": \"'yoke, n. — ME. yok, fr. OE. geoc, rel. to OS. juk ...'.\"},\n   AHD_C]),\n node(10, \"Sanskrit\", \"yuga; yoga\", \"confirmed\",\n  \"Skt. yugá- n. 'yoke; pair; generation, world-age' < PIE *yugóm (zero grade, thematic), exactly = Gk. zugón, Lat. iugum. Skt. yóga- m. 'yoking, harnessing; union, application, (later) the yoga discipline' < Proto-Indo-Iranian *yáwgas < PIE *yéwg-o-s (o-grade action noun), with IIr. *aw > Skt. o.\",\n  \"سنسکریت yuga «یوغ، جفت، دوران» از هندواروپایی آغازین *yugóm است، درست برابر با یونانی zugon و لاتین iugum. سنسکریت yoga «به یوغ بستن، پیوستن، و سپس ریاضت یوگا» از هندوایرانی آغازین *yáwgas و هندواروپایی *yéwg-o-s است و au هندوایرانی در سنسکریت به o بدل شده است. پوکورنی و هریتیج آمریکن هر دو را آورده‌اند؛ ادعای نورایی درست است.\",\n  [U_YOGA, U_IUGUM],\n  [AHD_R],\n  [POK_C, WLD_C, AHD_C, SYN_YOKE]),\n node(11, \"English\", \"yoga\", \"confirmed\",\n  \"English yoga (first attested 1820s, in British-Indian writing on Hindu philosophy) is a direct borrowing of Skt. yóga- 'union, yoking (of the self to the divine)'; the physical-exercise sense is 20th century.\",\n  \"انگلیسی yoga در سدهٔ نوزدهم، از راه نوشته‌های انگلیسی‌ها در هند دربارهٔ فلسفهٔ هندو، مستقیم از سنسکریت yoga «پیوستن، یوغ» وام گرفته شده است. ادعای نورایی درست است.\",\n  [U_YOGA],\n  [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on the node; AHD s.v. yeug- 'Sanskrit yogah, union: YOGA' covers it.\"}],\n  [{\"src\": \"KLN\", \"where\": \"KLN_1971.txt s.v. yoga (l. 269907)\", \"stance\": \"supports\", \"note\": \"'yoga, n. (Hindu philos.) — OI. yóga-, \\\"a yoking, union\\\" ... See yoke'.\"},\n   AHD_C,\n   {\"src\": \"SKT\", \"where\": \"SKT.txt grep '^Yoga'\", \"stance\": \"silent\", \"note\": \"no entry in Skeat's Concise dictionary.\"}]),\n node(12, \"Latin\", \"jungere; jugum; yugista\", \"plausible\",\n  \"Lat. iungere 'to join' < PIE nasal present *yu-n-g- (= Skt. yunákti) and iugum 'yoke' < PIE *yugóm are certain. 'yugista' is not a Latin word: it is AHD's reconstructed pre-form *jugistā (viā) 'by the nearest (road)', a superlative *yug-istos, contracted to attested iuxtā 'close by, nearby' (Pokorny 509: '*iugistos in lat. juxtā (*jugistā, scil. viā)'; Wiktionary gives this or Proto-Italic *jougestos 'yoked'). The gloss 'nearby' belongs to iuxtā. So the derivation is right but the chart presents a starred reconstruction as an attested Latin word.\",\n  \"لاتین iungere «پیوستن» از صورت خیشومی‌دار هندواروپایی *yu-n-g- (برابر سنسکریت yunakti) و iugum «یوغ» از *yugóm است و هر دو قطعی‌اند. اما yugista واژه‌ای لاتینی نیست؛ صورت بازسازی‌شدهٔ *jugistā (viā) «از نزدیک‌ترین راه» در هریتیج آمریکن و پوکورنی است که به لاتین iuxtā «نزدیک، کنار» کوتاه شده است، و معنای «نزدیک» از آنِ iuxtā است. پس ریشه‌شناسی درست است ولی کتاب صورتی فرضی را چون واژه‌ای گواهی‌شده آورده است؛ با احتیاط پذیرفتنی است.\",\n  [U_IUGUM, U_IUXTA],\n  [AHD_R],\n  [POK_C, AHD_C, WLD_C,\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. join, conjugate\", \"stance\": \"supports\", \"note\": \"'L. jungere ... jugum, \\\"yoke\\\"'; 'jugare ... rel. to jugum, jungere'.\"}]),\n node(13, \"English\", \"join; conjugate; adjust\", \"plausible\",\n  \"join < ME joinen < OF joindre (stem join-/joign-) < Lat. iungere (confirmed). conjugate < Lat. coniugātus, pp. of coniugāre 'to yoke together' (con- + iugāre, from iugum; confirmed). adjust: AHD and Klein derive it from OF ajuster < Late Lat. *adiuxtāre 'bring near' < iuxtā (*jugistā); Wiktionary derives it from ad + iustus 'just, exact', only influenced in sense by OF ajouster < *adiuxtāre. adjust is therefore only partly from this root (plausible).\",\n  \"join از انگلیسی میانهٔ joinen و فرانسوی کهن joindre، از لاتین iungere است و conjugate از لاتین coniugātus «به هم یوغ‌شده» (از iugum) است؛ هر دو درست‌اند. adjust را هریتیج آمریکن و کلاین از فرانسوی کهن ajuster و لاتین متأخر *adiuxtāre «نزدیک کردن» (از iuxtā) می‌دانند، ولی ویکی‌واژه آن را از ad + iustus «درست، دقیق» می‌گیرد که تنها در معنا از ajouster < iuxtā اثر پذیرفته است. پس adjust با احتیاط پذیرفتنی است.\",\n  [U_ADJUST],\n  [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on the node; parent's AHD s.v. yeug- lists 'JOIN ... CONJUGATE ... ADJUST'.\"}],\n  [KLN_JOIN,\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. adjust (l. 1646), conjugate (l. 8756)\", \"stance\": \"supports\", \"note\": \"'adjust ... fr. ML. adjustare, fr. Late L. adjuxtāre, \\\"to bring near\\\", fr. ad- and L. juxta, \\\"near\\\"'; 'conjugate ... L. conjugatus ... jugare ... rel. to jugum'.\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt l. 370 s.v. Adjust\", \"stance\": \"contradicts\", \"note\": \"'Adjust; see Just.' — Skeat puts it under just (Lat. iustus).\"},\n   AHD_C]),\n]\n\ne1_nodes = [\n node(1, \"Avestan\", \"yuvan, yvan\", \"confirmed\",\n  \"Av. yuuan-/yauuan- (Bartholomae 'yvan-, yavan-', both spellings for yuvan-; gen. yūnō) 'young man, (young) hero' < Proto-Iranian *HyúHā < PIE *h₂yéwHō / *h₂yuh₁en- 'young' (Pokorny 510 '5. ieu- jung'), = Skt. yúvan-.\",\n  \"اوستایی yuvan- / yvan- (در نوشتار yauuan-، حالت اضافی yūnō) «جوان، پهلوان جوان» از ایرانی باستان *HyúHā و هندواروپایی آغازین *h₂yuh₁en- «جوان» است، هم‌ریشه با سنسکریت yuvan. بارتولومه، پوکورنی و کلاین همین را آورده‌اند؛ ادعای نورایی درست است.\",\n  [U_YUVAN, U_JAVAN],\n  [POK510,\n   {\"ref\": \"KLN:1764\", \"status\": \"supports\", \"note\": \"KLN_1971.txt s.v. young (1966 ed. p. 1764): 'Avestic yvan- (gen. yūn-ō), \\\"young man\\\"'.\"},\n   {\"ref\": \"HRN\", \"status\": \"supports\", \"note\": \"HRN no. 429 (HRN.txt l. 3983 ff.): 'javān, juvān \\\"Jüngling\\\" ... aw. yuvan- (yvan-) \\\"Jüngling\\\"; phlv. yuvān ... ai. yúvan-'.\"}],\n  [{\"src\": \"BRT\", \"where\": \"BRT.txt l. 21911 (col. ~1305)\", \"stance\": \"supports\", \"note\": \"'yvan-, yavan-; yūn- m. \\\"Jüngling\\\" ... bes. \\\"junger Held, Held\\\"'.\"},\n   POK510_C, WLD_Y, AHD_Y, SYN_Y]),\n node(2, \"Persian\", \"javân\", \"confirmed\",\n  \"NP javān 'young' < MP juwān [ywb'n, Pahl. also ywn] 'young; a youth' < Av. yuuan- / Old Iranian *yuwan- < PIE *h₂yuh₁en-. Old Iranian initial *y- > MP j-, and the vowel of the first syllable was later lowered (juwān > javān; Horn gives both jevān and juvān). Kurdish ciwan, Pashto źwān, Balochi javan are cognates or loans; Armenian borrowed yovanak.\",\n  \"«جوان» از فارسی میانهٔ juwān «جوان، برنا»، از اوستایی yuvan- و ایرانی باستان *yuwan- و هندواروپایی آغازین *h₂yuh₁en- است. ی آغازی ایرانی باستان در فارسی میانه به ج بدل شده و واکهٔ هجای نخست در فارسی نو باز شده است (juwān > javān؛ هرن هر دو صورت را می‌آورد). مکنزی، نیبرگ، هرن و معین ([په.]) همه همین را می‌گویند؛ ادعای نورایی درست است.\",\n  [U_JAVAN, M_JAVAN],\n  [{\"ref\": \"BQT\", \"status\": \"not_checked\", \"note\": \"no page number given; the جوان entry lies in BQT vol. 2 whose OCR (BQT_v2_pages.txt) gives no readable footnote on grep 'جوان'.\"}],\n  [{\"src\": \"PHD\", \"where\": \"PHD.txt l. 414\", \"stance\": \"supports\", \"note\": \"'juwān [ywb'n | (P ywn), N jawān] young; a youth. ~īh: youth'.\"},\n   {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt l. 4458\", \"stance\": \"supports\", \"note\": \"'yuvān [ywb'n] youth, a young man ... Av. yvan-, yavan-; ... — NP javān'.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 429 (HRN.txt l. 3983)\", \"stance\": \"supports\", \"note\": \"'javān, juvān \\\"Jüngling\\\" ... aw. yuvan- ... phlv. yuvān'.\"},\n   {\"src\": \"MON\", \"where\": M_JAVAN, \"stance\": \"supports\", \"note\": \"'(جَ) [په.] (ص. اِ.) هر چیز کم سن. مق پیر' — Pahlavi origin.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt l. 6165-6175 [pdf page 214]\", \"stance\": \"supports\", \"note\": \"'JUVAN, YUVAN (PAHLAVI); YUVAN, YONO (AVESTAN); JIWAN, JUVAN (KURDISH); JAVAN (BALUCHI); ZWAN, JAVAN (AFGHANI); YUVASAS, YUVAN ... (SANSKRIT)'.\"},\n   {\"src\": \"HUB\", \"where\": \"HUB.txt grep 'javān'\", \"stance\": \"silent\", \"note\": \"no readable hit.\"}]),\n node(3, \"Sanskrit\", \"yavan; yuvasah\", \"transcription_suspect\",\n  \"Skt. yúvan- (nom. yúvā, gen. yū́naḥ) 'young; youth' < PIE *h₂yéwHō; yuvaśá- 'youthful' (nom. yuvaśáḥ, Nourai's 'yuvasah') is a derivative = Lat. iuvencus, Gmc. *jungaz. The book prints 'yavan', which is not the Sanskrit form: Klein (Nourai's KLN:1764) has 'OI. yuvā, yuvan-', and 'yavan-' is the Avestan spelling variant (Pokorny: 'av. yvan-, yavan- (beides für yuvan- geschrieben)'). This is Nourai's misprint/conflation; the extraction reproduces the page faithfully. yuvasah is correct.\",\n  \"سنسکریت yuvan «جوان» (حالت فاعلی yuvā) از هندواروپایی آغازین *h₂yéwHō است و yuvaśa «جوان‌وار، نوجوان» (yuvasah نورایی) از آن ساخته شده و برابر لاتین iuvencus است. اما کتاب «yavan» چاپ کرده که صورت سنسکریت نیست؛ کلاین که نورایی به او ارجاع می‌دهد yuvan- دارد و yavan- املای دیگرِ اوستایی است (پوکورنی). پس این خطای چاپی یا آمیختگی در خود کتاب است و استخراج درست است؛ صورت درست yuvan است.\",\n  [U_YUVAN],\n  [{\"ref\": \"KLN:1764\", \"status\": \"partial\", \"note\": \"KLN_1971.txt s.v. young: 'OI. yuvaśáh, \\\"youthful; young man, youth\\\" ... OI. yuvā, yuvan-, \\\"young; young man, youth\\\"' — supports yuvasah and the root, but gives yuvan, not yavan.\"}],\n  [POK510_C, SYN_Y, AHD_Y, WLD_Y],\n  error_in=\"book\", book_prints=\"yavan\", correct_form=\"yuvan\"),\n node(4, \"Germanic\", \"juncaz, jungaz\", \"transcription_suspect\",\n  \"Proto-Germanic *jungaz 'young' (Goth. juggs, OHG jung, ON ungr, OE ġeong) < earlier *juwungaz < PIE *h₂yuHn̥ḱós (*yuwn̥-kó-), the -k- suffixed derivative of *h₂yuh₁en-; Verner's law turned pre-Gmc *-nh- (from *-nk-) into *-ng-. *jungaz is confirmed (AHD: '*juwungaz becoming *jungaz'). 'juncaz' is not a form found in any source: it looks like a hybrid of Klein's PIE *yuwnkos with the Germanic ending, or a misprint for *junhaz/*juwungaz. The book prints 'juncaz, jungaz' (extraction faithful).\",\n  \"ژرمنی آغازین *jungaz «جوان» (گوتی juggs، آلمانی کهن jung، انگلیسی کهن geong) از *juwungaz پیشین و از هندواروپایی آغازین *h₂yuHn̥ḱós (صورت پسونددار با -k- از *h₂yuh₁en-) است و این بخش درست است. اما «juncaz» در هیچ منبعی نیست و به نظر می‌رسد آمیزه‌ای از صورت هندواروپایی *yuwnkos کلاین با پایانهٔ ژرمنی یا خطای چاپی باشد. کتاب همین «juncaz, jungaz» را چاپ کرده و استخراج درست است.\",\n  [U_JUNGAZ, U_YOUNG],\n  [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l. 1195 s.v. yeu-: '*yuwn-ko- in: a. Germanic *juwungaz becoming *jungaz in (i) Old English geong, young' — supports jungaz, not juncaz.\"},\n   {\"ref\": \"KLN\", \"status\": \"partial\", \"note\": \"KLN_1971.txt s.v. young: 'Goth. juggs ... fr. I.-E. *yuwnkos' — no Germanic *juncaz.\"}],\n  [POK510_C, AHD_Y, SYN_Y, SKT_YOUNG],\n  error_in=\"book\", book_prints=\"juncaz, jungaz\", correct_form=\"*jungaz (< *juwungaz)\"),\n node(5, \"English\", \"young, youth, youngster\", \"confirmed\",\n  \"young < ME yong < OE ġeong < PWGmc *jung < PGmc *jungaz. youth < OE ġeoguþ < PGmc *jugunþiz (PIE *yuwn̥-ti-, with g for w after duguþ 'virtue'). youngster = young + -ster (16th c.). All three go back to *h₂yuh₁en-.\",\n  \"انگلیسی young از انگلیسی کهن geong و ژرمنی آغازین *jungaz است؛ youth از انگلیسی کهن geoguþ و ژرمنی *jugunþiz (هندواروپایی *yuwn̥-ti-)، و youngster از young با پسوند -ster (سدهٔ شانزدهم) ساخته شده است. همه به ریشهٔ *h₂yuh₁en- «جوان» می‌رسند و هم‌ریشهٔ «جوان» فارسی‌اند. ادعای نورایی درست است.\",\n  [U_YOUNG],\n  [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on the node; AHD s.v. yeu- 'OE geoguth, youth: YOUTH ... OE geong, young: YOUNG' covers it.\"}],\n  [KLN_YOUNG, SKT_YOUNG, AHD_Y]),\n node(6, \"Latin\", \"juvenis; juvencus; juvenca\", \"confirmed\",\n  \"Lat. iuvenis 'young; young man/woman' < Proto-Italic *juwō < PIE *h₂yéwHō (nom. -is an innovation from the oblique stem iuven-). iuvencus 'young bull, bullock; (poetic) young man' and iuvenca 'heifer; (poetic) girl' < Proto-Italic *juwenkos < PIE *h₂yuHn̥ḱós, the same -k- derivative as Gmc. *jungaz and Skt. yuvaśá-. Nourai's glosses 'young man / young woman' are the secondary senses quoted by Klein.\",\n  \"لاتین iuvenis «جوان» از ایتالیک آغازین *juwō و هندواروپایی آغازین *h₂yéwHō است. iuvencus «گوسالهٔ نر جوان، و در شعر مرد جوان» و iuvenca «گوسالهٔ ماده، و در شعر دختر جوان» از *juwenkos و هندواروپایی *h₂yuHn̥ḱós اند، همان صورتی که young انگلیسی و yuvaśa سنسکریت از آن آمده‌اند. معناهای «مرد جوان / زن جوان» نورایی معناهای ثانوی است که کلاین آورده است. ادعای نورایی درست است.\",\n  [U_IUVENIS, U_IUVENCUS],\n  [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l. 1195: '3. Latin iuvenis, young: JUNIOR, JUVENILE'.\"},\n   {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1971.txt s.v. young: 'L. juvencus, \\\"a young bullock; a young man\\\", juvenca, \\\"a young cow; a young woman\\\" ... L. juvenis, \\\"young; young man\\\"'.\"}],\n  [POK510_C, WLD_Y, AHD_Y, SYN_Y]),\n node(7, \"English\", \"junior, juvenile\", \"confirmed\",\n  \"junior < Lat. iūnior 'younger', the comparative (*iuwen-yos > *iouniōs > iūnior) of iuvenis. juvenile < Fr. juvénile < Lat. iuvenīlis 'youthful', from iuvenis + -īlis. Both learned borrowings (14th-17th c.).\",\n  \"انگلیسی junior از لاتین iūnior «جوان‌تر»، صفت برتر iuvenis، و juvenile از فرانسوی juvénile و لاتین iuvenīlis «جوانانه» است؛ هر دو وام‌واژه‌های کتابی‌اند. ادعای نورایی درست است.\",\n  [U_IUVENIS],\n  [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on the node; AHD s.v. yeu- 'Latin iuvenis, young: JUNIOR, JUVENILE' covers it.\"}],\n  [{\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. juvenile (l. 20508)\", \"stance\": \"supports\", \"note\": \"'juvenile ... F. juvénile, fr. L. juvenīlis, \\\"youthful\\\", fr. juvenis, \\\"young man\\\". See young ... Cp. also junior'.\"},\n   AHD_Y,\n   {\"src\": \"SKT\", \"where\": \"SKT.txt grep '^Junior|^Juvenile'\", \"stance\": \"silent\", \"note\": \"no separate hit in the OCR.\"}]),\n]\n\nout = {\n \"pdf_page\": 565, \"book_page\": 535, \"verified_by\": \"claude-opus-5.5\", \"verified_on\": \"2026-10-16\",\n \"entries\": [\n  {\"entry\": 0, \"root\": \"Yeu 1, Yeug\", \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *yewg- (*(H)yewg-) 'to join, yoke'\",\n   \"note\": \"Pokorny 508-510 '2. ieu-, ieu-g- \\\"verbinden\\\"' (Nourai's POK:509 is the right page); AHD yeug- 'To join'. Root, label and gloss correct. Problems on the page: (1) the Greek node mixes zugon/zygos with 'sextarious' = Latin sextarius 'one-sixth', a different root (*swéks); (2) Arabic qisṭ 'justice' is from Aramaic q-š-ṭ, not from ζυγός; qisṭās is disputed (Wiktionary: via Syriac from Gk. zugostatēs 'weigher', which would be a *yewg- word; Jeffery prefers Aramaic qisṭā). (3) Latin 'yugista' is AHD's reconstructed *jugistā, the source of iuxtā, not an attested word. (4) 'BQT:1228' is actually Bartholomae col. 1228 cited in Mo'in's footnote at BQT 2458. The extraction matches the printed page.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *yewg- «پیوستن، به یوغ بستن» (پوکورنی ۵۰۸-۵۱۰؛ هریتیج آمریکن yeug-) درست است و یوغ، جفت، زوج، yoke، yoga، join و iugum همه از آن‌اند. اما در این نمودار چند خطا هست: sextarius لاتین «یک‌ششم» از ریشهٔ «شش» است و به این ریشه ربطی ندارد؛ «قسط» عربی از ریشهٔ آرامی ق-ش-ط «راستی، داد» است؛ دربارهٔ «قسطاس» اختلاف هست (ویکی‌واژه آن را از یونانی zugostatēs «ترازودار» می‌داند و جفری از آرامی qisṭā)؛ و yugista صورتی بازسازی‌شده است که لاتین iuxtā «نزدیک» از آن آمده است. ارجاع «برهان ۱۲۲۸» نورایی در واقع ستون ۱۲۲۸ بارتولومه است که معین در حاشیهٔ «یوغ» (ص ۲۴۵۸) آورده است.\",\n   \"sources\": [U_YEWG, U_IUGUM],\n   \"ref_check\": [POK509],\n   \"consulted\": [POK_C, WLD_C, AHD_C,\n                 {\"src\": \"IEC\", \"where\": \"IEC.txt grep 'yugom|i̯ugom'\", \"stance\": \"silent\", \"note\": \"no readable hit in the OCR.\"},\n                 SYN_YOKE],\n   \"nodes\": e0_nodes},\n  {\"entry\": 1, \"root\": \"Yeu 2, Yuwn, Yuwnkos, Ieu\", \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₂yuh₁en- / *h₂yéwHō 'young' (Watkins: yeu- 'vital force, youthful vigor', variant of aiw-); *h₂yuHn̥ḱós 'young' (Klein *yuwnkos)\",\n   \"note\": \"Pokorny 510 '5. ieu- \\\"jung\\\"' (Nourai's POK:510 is right); AHD yeu- 'Vital force, youthful vigor ... variant of aiw-', which supports Nourai's 'Compare with root Aiw'. The labels Yuwn and Yuwnkos are Klein's *yuwn-, *yuwnkos. Problems: Sanskrit 'yavan' should be yuvan- (yavan- is an Avestan spelling); Germanic 'juncaz' is not a known form (only *jungaz < *juwungaz). Both are in the printed book; the extraction is faithful.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₂yuh₁en- «جوان» (پوکورنی ۵۱۰؛ هریتیج آمریکن yeu- «نیروی زندگی، توان جوانی» که گونه‌ای از aiw- است) درست است و «جوان» فارسی، yuvan سنسکریت، iuvenis لاتین و young انگلیسی همه از آن‌اند؛ اشارهٔ نورایی به ریشهٔ Aiw هم با هریتیج آمریکن سازگار است. تنها دو خطای چاپی در کتاب هست: سنسکریت yavan باید yuvan باشد و ژرمنی juncaz صورتی ناشناخته است (درستش *jungaz).\",\n   \"sources\": [U_YUVAN, U_IUVENIS, U_YOUNG],\n   \"ref_check\": [POK510],\n   \"consulted\": [POK510_C, WLD_Y, AHD_Y, SYN_Y, KLN_YOUNG],\n   \"nodes\": e1_nodes},\n ]}\njson.dump(out, open(\"/home/sfmqrb/git/rishe-private/data/verification/page-565.json\", \"w\"), ensure_ascii=False, indent=1)\n"
}
```


### [2026-10-17T00:38:59.780Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-565.py (file state is current in your context — no need to Read it back)
```


## [2026-10-17T00:39:11.238Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-565.py && python3 -m json.tool data/verification/page-565.json >/dev/null && echo JSON-OK; python3 tools/verify_check.py 565",
 "description": "Build JSON, validate, and run checker"
}
```


### [2026-10-17T00:39:11.916Z] TOOL RESULT

```
JSON-OK
nodes verified: 20/20
node verdicts: {'confirmed': 13, 'disputed': 3, 'plausible': 2, 'transcription_suspect': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 15, 'not_found': 1, 'not_checked': 8, 'partial': 4, 'contradicts': 1}
books consulted: {'supports': 68, 'partial': 5, 'silent': 11, 'contradicts': 2} | by book: {'AHD': 14, 'KLN': 10, 'POK': 9, 'WLD': 8, 'SKT': 7, 'SYN': 6, 'FVQ': 5, 'MON': 4, 'AFA': 3, 'AFM': 3, 'BRT': 2, 'CHEUNG': 2, 'PHD': 2, 'NYB': 2, 'HUB': 2, 'HRN': 2, 'ARY': 2, 'BQT': 1, 'PLA': 1, 'TAD': 1}
```


## [2026-10-17T00:39:14.922Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/verify_check.py 565 2>&1 | grep -c PROBLEM",
 "description": "Count PROBLEM lines"
}
```


### [2026-10-17T00:39:15.448Z] TOOL RESULT

```
0
```


## [2026-10-17T00:39:25.515Z] TOOL CALL #46: SubagentHandback

```json
{
 "message": "Page 565 (book page 535) is verified. I wrote /home/sfmqrb/git/rishe-private/data/verification/page-565.json, and `verify_check.py 565` reports 0 PROBLEM lines.\n\nAll 20 nodes are covered, plus both roots.\n- **Roots (Yeu 1 / Yeug; Yeu 2):** both confirmed (Pokorny pp. 508–510, AHD yeug- and yeu-).\n- **Nodes:** 13 confirmed, 2 plausible, 3 disputed, 2 transcription_suspect.\n\nDisputed:\n- **Yeu 1 #3 Greek \"sextarious\":** this is Latin sextārius \"one-sixth\", from the word for \"six\", not from *yewg-, and not Greek. zugon/zygos are fine. Nourai merged two separate proposals for the origin of qisṭās that Jeffery (FVQ p. 239) reports, one from ζυγός (Vullers) and one from ξέστης < sextarius (Dvořák).\n- **Yeu 1 #6 Arabic qest:** qisṭ comes from Aramaic q-š-ṭ \"truth, right\" (Jeffery, Fraenkel), not from ζυγός.\n- **Yeu 1 #7 Persian qest; qestâs:** qest is disputed for the same reason. qestâs is only plausible: Wiktionary derives it through Syriac from Greek zugostatēs \"weigher\", which would make it a *yewg- word, but Jeffery prefers Aramaic qisṭā \"measure\".\n\nTranscription_suspect (in both cases the book prints the odd form and the extraction copies it faithfully):\n- **Yeu 2 #3 Sanskrit \"yavan\":** should be yuvan-. yavan- is an Avestan spelling, and Klein, the source Nourai cites, has yuvan.\n- **Yeu 2 #4 Germanic \"juncaz\":** no source has this form. Only *jungaz (from earlier *juwungaz) is attested.\n\nPlausible: Latin \"yugista\" is AHD's reconstructed *jugistā (the source of iuxtā \"nearby\"), shown as if it were a real Latin word. English \"adjust\" has a disputed origin: Klein and AHD derive it from iuxta, Wiktionary from ad + iustus.\n\nReference problem: Nourai's \"BQT:1228\" is really Bartholomae column 1228. Mo'in cites it in his footnote to یوغ at BQT p. 2458, while BQT p. 1228 has nothing on yoke. I saved my reading of the BQT p. 2458 footnote to `data/verification/sources/refs/ocr/BQT/2458.vision.txt`.\n\nExtraction errors: none. The JSON matches the printed page; the rendered page is at `data/verification/sources/refs/ocr/BOOK/565.png`."
}
```


### [2026-10-17T00:39:25.942Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
