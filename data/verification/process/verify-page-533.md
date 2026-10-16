# Verification process log — verify-page-533


## [2026-10-16T05:13:02.008Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 533 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-533.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-533.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-533.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 533` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:02.073Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:06.842Z] TOOL CALL #1: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md; echo ====; cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-533.txt; echo ====; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-533.json",
 "description": "Read instructions, chart, and source JSON"
}
```


### [2026-10-16T05:13:07.436Z] TOOL RESULT

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


## [2026-10-16T05:13:09.906Z] TOOL CALL #2: Bash

```json
{
 "command": "sed -n '/Scanned references/,/Wiktionary\\*\\* (en/p' /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md",
 "description": "Read truncated middle of instructions"
}
```


## [2026-10-16T05:13:10.859Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-533.txt; echo; echo =====; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-533.json",
 "description": "Read chart text and source JSON"
}
```


### [2026-10-16T05:13:11.276Z] TOOL RESULT

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


### [2026-10-16T05:13:11.330Z] TOOL RESULT

```
Exit code 1
=== PDF page 533 (book page 503) ===
--- entry 0 ---
ROOT [Indo-European] Wei 2, Wiros : vital force; man  (refs POK:1123,1177; KLN:1714)
#1 (parent #0) [Avestan] refs=POK:1177; KLN:1714 | vîra : man, (his mind)
  #2 (parent #1) [Pahlavi] refs=BQT:334; ZAP:159 | vîr : awareness ; varm 2 : memory ; varm kartan : to memorize
    #3 (parent #2) [Persian] refs=MON:489; BQT:2298; ZAP:159; BQT:262 | vîr «ویر (بیر)» : memory, intelligence ; bar 1 «بَر ۱ (بَرم)» : memory
#4 (parent #0) [Avestan] refs=POK:1123 | vôi, vây 2, vîvâiti, vayeiti 2 : to chase ; vyâna 1 : followed ; vâtay : persecution ; vîtar 1 : persecutor ; vôi-thwa : chased
#5 (parent #0) [Germanic] refs=AHD | weraldh : man's world
  #6 (parent #5) [English] refs=None | world
#7 (parent #0) [Latin] refs=AHD; POK:1123,1177 | vir : man ; violere : treat with force
  #8 (parent #7) [English] refs=None | virtue ; violent
--- entry 1 ---
ROOT Weib -> redirect to Weip

(eval):1: ==== not found
```


## [2026-10-16T05:13:14.923Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-533.json; echo '-----'; cat /home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md | head -80; ls /home/sfmqrb/git/rishe-private/data/verification/sources/refs/; ls /home/sfmqrb/git/rishe-private/data/verification/ | head; ls /home/sfmqrb/git/rishe-private/data/verification/page-5*.json | tail -3",
 "description": "Read JSON, source matrix, refs dir"
}
```


### [2026-10-16T05:13:15.246Z] TOOL RESULT

```
{
  "pdf_page": 533,
  "book_page": 503,
  "entries": [
    {
      "root": {
        "name": "Wei 2, Wiros",
        "lang": "Indo-European",
        "refs": "POK:1123,1177; KLN:1714",
        "gloss": "vital force; man"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1177; KLN:1714",
          "words": [
            {"translit": "vîra", "gloss": "man, (his mind)", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:334; ZAP:159",
          "words": [
            {"translit": "vîr", "gloss": "awareness", "script": null},
            {"translit": "varm 2", "gloss": "memory", "script": null},
            {"translit": "varm kartan", "gloss": "to memorize", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:489; BQT:2298; ZAP:159; BQT:262",
          "words": [
            {"translit": "vîr", "gloss": "memory, intelligence", "script": "ویر (بیر)"},
            {"translit": "bar 1", "gloss": "memory", "script": "بَر ۱ (بَرم)"}
          ],
          "note": null,
          "quote": {
            "text": "بپرسید نامش ز فرّخ هجیر - بدوگفت نامش ندانم به ویر",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1123",
          "words": [
            {"translit": "vôi, vây 2, vîvâiti, vayeiti 2", "gloss": "to chase", "script": null},
            {"translit": "vyâna 1", "gloss": "followed", "script": null},
            {"translit": "vâtay", "gloss": "persecution", "script": null},
            {"translit": "vîtar 1", "gloss": "persecutor", "script": null},
            {"translit": "vôi-thwa", "gloss": "chased", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "weraldh", "gloss": "man's world", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "world", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; POK:1123,1177",
          "words": [
            {"translit": "vir", "gloss": "man", "script": null},
            {"translit": "violere", "gloss": "treat with force", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "virtue", "gloss": null, "script": null},
            {"translit": "violent", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Weib",
        "redirect": "Weip"
      },
      "nodes": []
    }
  ]
}
-----
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
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  agent
drwxr-xr-x     - sfmqrb 14 Oct 22:57  process
drwxr-xr-x     - sfmqrb 14 Oct 22:19  sources
.rw-r--r--  9.7k sfmqrb 14 Oct 22:19  COORDINATOR.md
.rw-r--r--   89k sfmqrb 14 Oct 22:14  page-31.json
.rw-r--r--   33k sfmqrb 14 Oct 22:14  page-32.json
.rw-r--r--   64k sfmqrb 14 Oct 22:14  page-33.json
.rw-r--r--   85k sfmqrb 14 Oct 22:14  page-34.json
.rw-r--r--   87k sfmqrb 14 Oct 22:14  page-35.json
.rw-r--r--   36k sfmqrb 14 Oct 22:51  /home/sfmqrb/git/rishe-private/data/verification/page-516.json
.rw-r--r--   32k sfmqrb 14 Oct 22:48  /home/sfmqrb/git/rishe-private/data/verification/page-517.json
.rw-r--r--   20k sfmqrb 14 Oct 22:48  /home/sfmqrb/git/rishe-private/data/verification/page-518.json
```


## [2026-10-16T05:13:36.679Z] TOOL CALL #5: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe-private/site/pages/533.jpg; cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','BQT','ZAP','MON','AHD']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:700])\n\"",
 "description": "Check page image and ref metadata"
}
```


### [2026-10-16T05:13:37.092Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   44k sfmqrb 14 Oct 22:15  /home/sfmqrb/git/rishe-private/site/pages/533.jpg
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based lea
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966:
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
ZAP {"title": "H. W. Bailey, Zoroastrian Problems in the Ninth-Century Books, Oxford 1943 (repr. 1971)", "edition_found": "1943/1971 (scan without hocr; page detection weak)", "kind": "archive_djvu", "url": "https://archive.org/details/BaileyH.W.ZoroastrianProblemsInTheNinthCenturyBooksk", "identifier": "BaileyH.W.ZoroastrianProblemsInTheNinthCenturyBooksk", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ZAP.txt", "page_offset": "not reliably detected (121 leaves, apparently two pages per leaf); grep the word. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
```


## [2026-10-16T05:13:38.643Z] TOOL CALL #6: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/533.jpg"
}
```


### [2026-10-16T05:13:38.672Z] TOOL RESULT

```

```


## [2026-10-16T05:13:42.587Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'u̯ei-3\\|wei-3\\|u̯ī-ro-\\|wī-ro\\|u̯īro' POK_full.txt | head -20; grep -n 'Page(s): 1123\\|Page(s): 1177\\|^Page.*1123\\|1177' POK_full.txt | head",
 "description": "Grep Pokorny for root entries"
}
```


### [2026-10-16T05:13:42.895Z] TOOL RESULT

```
89752:Page(s):1123 
89840:Page(s): 1123-1124 
92892:Page(s):1177 
92910:Page(s):1177 
92939:Page(s):1177 
92950:Page(s):1177 
93050:Page(s): 1177-1178
```


## [2026-10-16T05:13:44.717Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '89730,89845p;92880,92960p' POK_full.txt",
 "description": "Print Pokorny entries pages 1123 and 1177"
}
```


### [2026-10-16T05:13:45.162Z] TOOL RESULT

```
Maybe alb. Geg vyshk-et, Tosc f/shk 'mther' a Latin loanword. 

Old Irish feugudg\. "marcor' has derived from feo^ wilted; faded, flaccid, withered ' {*u/- 
yo-) = cymr. gwyw6s.; 

Old Icelandic visinn^ wilted; faded, flaccid, withered ', participle oVwisan, whereof 
Germanic *wis-n-dn, -en\n Old Icelandic visna. Old English w/sn/an and (with gramm. 
variation) weornian. Old High German M/e55/7e/7 "wither, wilt' (also Modern High German 
verwesen be\ongs as Old English forweoren \eoj\/est' shows, originally here); Middle High 
German wese/^weak, faint, languid', engl. dial, weasel, weazen^Vnin, lean ', Old Icelandic 
vesair woeful, wretched, miserable ', vesligrds., Norwegian i//5a"weak person', Swedish 
i/esa "exhaust'; 



Lithuanian i/ysZ/'witlier, wilt' (preterit vytau), vytinu, pa-va/t/nu' make wilt ', Latvian 
v/etet, vTtet6s. 

References: WP. I 227 f., WH. II 787 f.; 

See also: relationship to ueis-^ deliquesce ' is probable. 

Page(s):1123 

Root / lemma: uei-3, ueia- : uT- 

Meaning: to reach towards smth., to pursue or wish smth.; to be strong 

Material: Old Indie veti, 3. PI. vyanti, also i/aya//"verfolgt, strives, leads (the weapons), 

drives, lenkt', also "enjoys", participle i//?a-" pursued, liked, beloved, fancied ', Adj. " 

straight, in a straight line ', K/?a"row', vTthi-, vTthTi. 'row, way', pravayana-^zuvn Antreiben 

helpful', m. "Stachelstock', pravetar-^ charioteer', vTti- 'horse' ("*pursuer, follower'?); 

pada-vTi. " way, path, track ', padavaya-^ signpost, leader ' (lengthened grade); with the 

meaning " strive - have gladly '; i//?a-" liked, beloved, fancied, gladly genossen', vTtf- " eat, 

drink; relish, enjoy, enjoyment, meal', deva-vT-^ the pleased gods ', deva-vTti- 'enjoyment, 

feast for the gods'; 

Avestan i/o/lnf. 'to cheer, to gefallen'; vay- {vayeiti, vTvaitr chases away ', 3. PI. vyeinti) 
' pursue, hunt, chase', vyana-'\he victim of persecution ', vo/^wa- Ad'\. 'to hunt, chase, 
jagend to pursue ', v/tar- ' pursuer ', vatay- ' pursuit '; 

with the meaning 'fly' Old Indie ved. ve v/yate IWes' and Avestan a-vaye/nf/' they fly up '; 
Old Indie venat/" longs ', vena- ' yearning, longing '; 

gr.lepai 'bewege myself vorwarts, hurry, strive, lust, desire', (reshuffling of a *R-iopai; 
Asper after the Medium from Tr|Mi),"i£|J£vo(; 'cupidus', £iaaTo(F-), £[F]£iaaTO ' walked loose', 
oijjoq ' gait, way, pathway', (*FoT[joq), hom.lojKr) ' pursuit ' (F-), Akk.lwKO ds.,1u)x|j6(; (T 
metr. lengthening) 'Schlachtgetummel', naXiw^K;, naAi-iw^K; 'WiederzuriJckdrangen in 
Kampfe', korinth. Fiojkei 'verfolgt' (compare 5iu)k-u) : Sispai); i£p6(; (FT£po(;), Doric FTap6(; 
(6pvi(;) 'nimble, quick, fast' (Tmetr. lengthening), besides *R-po(;, assumed through ep. 
lonianlpn^, -r\Koq ' hawk' (the schnelle), Attic (through engeren connection an i£p6(;) lipa^, 
-aKO(; ' hawk'; 

'iq ' power ' (= Latin v/s, vim), yi(; iaxu(; Hes., icpi 'with power ' (Instr. in -b^/), whereof 
icpioq; about io, 'sinew' see above S. 1121 ; 

Latin viai. 'way'. Oscan viu, Umbrian ablative vea, via 6s., Oscan amvian{n)ud 
'Straftenviertel, road' {*ueja); Latin i//s'du willst' {*uei-si= Old Indie vesi), vTs, vim' power. 



force, might' (= gr.l(; ds.), PI. K/?es(from an 5-stem); invTtare^ host, invite ', with in- "ein'- 
compared with verneinendem //7-'un'- in //7i//?i/5 "wider Willen' (: Old Indie vTta- " liked, 
beloved, fancied '); whether i///7o'eA'"Burge, avenger' as "Bestimmerthe atonement ' to Old 
Church Slavic i//77a "blame'? 

(about Old Irish ffad^WM, ffadach^ hunt' etc. see below *ui6!^u-^\xee')\ 

mcymr. gwit^6\s\\, food', mel-wiV honey ' (: Old Indie i//?/- "enjoyment, meal'), Ifor 
Williams BBCS. 11, 143; 

Old Icelandic veidr^ hunt ', Old English wad^ hunt, journey' = Old High German weida 
"food, Weide, hunt (Waidwerk), Fischerei', also "Fahrt, journey'. Middle High German 
anderweide^zum zweitenmal'. Modern High German anderweit. Middle High Germano'/> 
weide^z\}xr\ drittenmal'. Old Icelandic veida. Old English wsedan^ hunt, chase, 
umherstreifen'. Old High German we/ddn^\r\unt, chase; food seek ': Indo Germanic *uof-ta 
"das Drauflosgehen, Jagen'; Old Saxon wnn PN l/VF-r/ic, Ger-wJ(. Latin 1//5); 

Lithuanian vefu, i/y//"hunt, chase, pursue ', i/y/as(= Old Indie vTta-) "verfolgf, vaJ6-ju, -ti 
"mehrfach nachjagen', yC>5i/yj7s"Strecke Wegs', Latvian vajat^ pursue ', a/-i/eya/"Ruckfalle 
from Krankheiten', at-veja^may ("*gait ', compare Middle High German anderweide^zum 
zweitenmal'); o-grade Lithuanian pa i/Q^i/s "danger', pai/oy^s "dangerous'; Old Church Slavic 
i/oyi. "warrior', vojbna^\Nar, fight', ablaut. Old Church S\av\c pov/ngt/^ subject, subdue', 
i/bzi///^e "profit, gain' ("*Erjagtes'); with the meaning "Verfolgung eines Ubeltaters' probably 
Old Church Slavic i///7a "blame, punishment', ablaut. Latvian i/a/775 "blame', Lithuanian 
i/a//7d// "vilify, scold, scold, chide'. Old Prussiane/M//>7j/"entschuldigen'; 

Czech etc. i///a// "greet' reminds an Latin invitare; unclear is the relationship to russ. 
v/fatb etc. "stay, dwell', and to Lithuanian v/efa, Latvian i//e/a "place' {*ueita), Trautmann 
345, Vasmerl, 205; 

maybe nazalized alb. (^vieta) KeA7o' 'place' 

e5-stem, respectively s-extension: Old Indie vayas-v\. " vitality, youth strength, 
Jugendalter', i//o'5ya//(*^/-z-o'-) "makes strong, tight, firm', k/o'Z/- "tight, firm', vivesti, vesati 
"is active, wirkt, brings zustande, richtet from', Latin vT-r-es{see o). 

References: WP. I 228 ff., WH. I 713 f., II 749 f., 800 f., Trautmann 345 f., Vasmer 1, 201, 

215; 

See also: compare also ufro-s "man'. 

Page(s): 1123-1124 



Root / lemma: ueip- ueib- 

"separate, divide' and then formal = Old Indie vidh'u- "vereinsamf, Lithuanian vidus^ 
center, the interior'; compare above S. 707 Lithuanian medzias^iree"; 

connection with Irish ffad^wM, fladach' hunt', cymr. gwydd'wM', acorn. gu/t-f/71era', 
bret. ^c»^ez"wild' would be the meaning after through Latin s/'/vat/cus'wM : s/7va, 
Lithuanian med/n/s^wM', medz/dk/e' hunt' : med/s'tree' to prop, support, yet bliebe dabei 
die lengthened grade e/ compared with dem Grundworte Irish /^icy difficult, hard; es is hence 
fladirom f/dto separate and auf eine besides *ue/-t- in Old High German weida. Old 
English wad. Old Icelandic veidr^ hunt, fishing' (: *uei-3) liegende root form *uei-c^h)- to 
beziehen. 

References: WP. I 314, 228 ff. 
Page(s):1177 

Root / lemma: u/ng- and ue/g-{u/g-7) {*hueik-) 
Meaning: elm 

Material: With nasalization Balto Slavic group Lithuanian vinksna, Latvian v/'ksna ds. (also 
Old Prussian w/m/no'e\r(\', lies wincsnd) from *u/ng-sna {Suii. as in Lithuanian g/uosna' 
willow '); 

nasalized Old English w/ic, wTce, engl. witch. Low German W77re"elm'; 

likewise uing- as uig- can be in alb. vith. Gen. i//o'/7"elm' and in Kurdish K/z"a kind of 
elm'; the relationship of the nasalized against unnasalized form is still to be cleared, 
(common alb. Celtic -k > -th, -g > -dh > Slavic Iranian z-) 

Serb. Kez(Gen. i/eza), russ. vjaz-b, poln. M//^z"Ulmus campestris' (proto Slavic. V^zb); 
References: WP. I 314, Specht Indo Germanic Dekl. 59 f., Trautmann 360, Vasmer 1, 244, 
Petersson Heteroklisie 56 f. 
Page(s):1177 

Root / lemma: ujeth-, uith- {*haueith-^ 
Meaning: to shake 



Material: Old Indie vyathate' sways, taumelt, geht schief, kommt to Falle, shrugs, jerks, 

weicht', vithura-^ fluctuating, mangelhaft'; Gothic wiPon^ shake' \ relationship to *uei-1 

"turn' is probably, da in Kreise this root words for 'waver, hin and her bewegen' right 

frequent, often are. 

Maybe alb. vithe " buttocks, hips '. 

References: WP. I 318, Kuiper Nasalpras. 53, Wackernagel-Debrunner II 2, 487. 

Page(s):1178 

Root / lemma: uTks- {*hauiks^ 

Meaning: ' mistletoe and other glue delivering trees ' 

Note: {u7sk-l) 

See also: s. S. 1134 (ue/s-). 

Page(s):1177 

Root / lemma: uT-Rnrit-T{* hauT-RrQt-J) 
Meaning: twenty 

Note: actually Dual "two decades ' (to Indo Germanic oT-'two' and dRrpt- above S. 192) 
Material: Old Indie viifisatf-, Avestan vTsaiti, osset. insai, Armenian k'san, gr. eiKoai, Doric 
FiKQTi, hom. EsiKOGi for £(F)lKoai, alb. zet, Latin vTginti{see above S. 192), Old Irish fiche. 
Gen. fichet {*uiRmt-s, -os), acymr. i/ce//?/ (instead of *gwyca/ntirorr\ the compound *dou- 
viceint, cymr. deugaint^AQ" abstracted), corn, ugans, Tocharian A wiki, B ik9. 
References: WP. I 313, Wackernagel-Debrunner 3, 366 f., WH. II 788 f.. Frisk 453 f. 
Page(s):1177 

Root / lemma: u7-1 {*hauV) 
Meaning: separate from; both, two 
Note: (see uT-Rixit-fj 

Material: Old Indie k/- 'apart', Avestan i/7- 'apart; abseits, apart, separated from; entgegen; 
through and through ' (also vis-: v/s-pat-^go away, pass over'); Old Indie i//si/- 'after variant 
Seiten' in i//si//7a- 'verschiedenartig', iz/siz-zt/pa- 'verschiedengestaltig' , v/suva-n. 
'aequinoctium', visuvant- 'in the middle situated, after beiden Seiten gleich', visv-anc- 
'afterbeiden (all) Seiten gewandt, auseinandergehend'. Old Indie i//5i/5-o'/y5/7/r'uberallhin
```


## [2026-10-16T05:13:48.361Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '93030,93080p' POK_full.txt; grep -n -i 'violare\\|vir, viri\\|virtus' POK_full.txt | head",
 "description": "Print Pokorny wiro-s entry"
}
```


### [2026-10-16T05:13:48.823Z] TOOL RESULT

```
mancipia ', Volscan Abl. Sg. couehr/u ^*coy\n6, contione ', Lithuanian vyras, Latvian mrs, 

Old Prussian w/jrs^man'; skyth. oiop ' av5pa ' (Herod. 4, 110), more properly oipo- = v/ro-, 

Old Indie v/rapsa-irom * vTra-psv-a- {: Avestan pasu vTra) 'people and cattle', compare 

Umbrian ueiro pequo6,s. 

With / Latin iz/^'man', in the old language also the unique word for " husband ', 
wherefore K/Aa^d'mannhafte virgin, Heldin', virtus^ manfulness, skillfulness, virtue, 
uprightness, integrity ', Old Irish /fe^'man', cymr. etc. gwr, PI. gwyr{{o which the Sg. gwr 
analogically is formed additionally). 

Gothic wafr. Old Icelandic verr. Old High German Old Saxon Old English wer^rc\av\\ 
Tocharian A wir^ young '; Modern High German Werwolf, probably to Latin vTs " power ' 
etc., "Vez-'auf etwas losgehen', s. d. 

References: WP. I 314 f., WH. II 796 f., Trautmann 360, W. Schuize Kl. Schr. 398, 
Untermann, IF. 62, 127. 
Page(s): 1177-1178 

Root / lemma: uiek-, yfk- {*haiilk^ 

Meaning: to shine; fiery 

Note: 

It derived from Root/ lemma: se-\ "reflexive pronoun' + /e/r'shape, apparition'. 

Material: 

perhaps to gr. {*haiilk-) aFAa^ apAa^ " bright, brilliant, radiant ' (whether (*FAapnpaJ(;) 

Aaijnpux; Hes. 'bright, brilliant, radiant '); incredible nAEKTwp 'gleaming, sun', pAEKipov ' 

mixture of gold and silver, amber '; 

Old Indie ulka, u/kusr meteor', 

Tocharian AB {*vlek) /e/r 'shape, apparition'. 

References: WP. I 321, J. B. Hofmann Etymol. gr. Wb. 106, Frisk 629, Mayrhofer 1, 112. 

Page(s):1178 

Root/ lemma: y/k'^-os {* hau/k''-) 
Meaning: wolf 



93040:wherefore K/Aa^d'mannhafte virgin, Heldin', virtus^ manfulness, skillfulness, virtue,
```


## [2026-10-16T05:13:51.382Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '93018,93031p' POK_full.txt; echo ----AHD; grep -n -i -B2 -A25 '^wei-2\\|wei-2\\.\\|wei-2 ' AHD_watkins1985.txt | head -60",
 "description": "Pokorny wiro-s head; AHD wei-2"
}
```


### [2026-10-16T05:13:51.694Z] TOOL RESULT

```
<persisted-output>
Output too large (36.9KB). Full output saved to: /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/bg9rpp5jd.txt

Preview (first 2KB):
Page(s):1176 



Root / lemma: uTro-s {*haueir-) 

Meaning: man; warrior 

Material: With f. Old Indie vTra-, Avestan vTra- "man, hero ', Umbrian Akk. PI. n. u(e)iro^ 

mancipia ', Volscan Abl. Sg. couehr/u ^*coy\n6, contione ', Lithuanian vyras, Latvian mrs, 
----AHD
648-English hréowan, to distress, grieve: RUE!, RUTH. 2. Ex- tended o-grade form *krous- in Greek krouein, to strike: ANACRUSIS. [Pok. 3. kreu- 622.] kreup-. Scab; to become encrusted. 1. Germanic *hrub- in: a. Middle Low German ruffelen, to crumple, akin to the Germanic source of Middle English ruffelen, to ruffle, roughen: RUFFLE}; b. Germanic compound *ga-hrub- (*ga-, intensive prefix; see kom) in Middle Dutch grof, harsh: GRuFF. 2. Suffixed o-grade form *kroup-d in Serbo-Croatian krupa, groats (perhaps > German Graupe, barley): GRAUPEL. [Pok. kreup- 623.] kreus-. To begin to freeze, form a crust. 1. Suffixed zero-grade form *krus-to- in: a. Latin crusta, crust: CROUTON, CRUST, CRUSTACEAN, CRUSTACEOUS, CRUS- TOSE; b. Greek krustallos, ice: CRYSTAL, CRYSTALLINE, CRYSTALLO-. 2. Suffixed zero-grade form *krus-es- in Greek kruos, icy cold, frost: cryo-. [Pok. 1. B. kreu- 621.] kreut-. Also kreudh-. Reed. Germanic *hreuda- in Old English hréod, reed: REED. [Pok. kreut- 623.] kropo-. Roof. Germanic *hréfam in Old English hrdf, roof: ROOF. [Pok. krdpo- 616.] krut-. Musical instrument. 1. Germanic *Arut- in Old French rote, a stringed instrument: ROTE3, 2. Geminated form *krutté in Welsh crwth, an ancient Celtic instru- ment: CROwD?. [Pok. krut- 624.] ksero-. Dry. 1. Lengthened-grade form *kséro- in Greek xéros, dry: XERO-; ELIXIR, PHYLLOXERA, XEROPHTHAL- MIA. 2. Perhaps suffixed variant form “kseres-no- in Latin serénus, serene, bright, clear: SERENE. [Pok. ksero- 625.] ksun. Preposition and preverb meaning “with.” 1. Greek sun, xun, together, with: syN-. 2. Russian so-, s-, with, in sputnik, fellow traveler (see pent-): SPUTNIK. [In Pok. 2. sem- 902.] ku-. Hypothetical base of a variety of conceivably rel
...
</persisted-output>
```


## [2026-10-16T05:13:54.204Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o -i 'wei(ə)-.\\{0,900\\}' AHD_watkins1985.txt | head -3; grep -o 'wi-ro-.\\{0,600\\}' AHD_watkins1985.txt | head -3; grep -o -i 'Vital force.\\{0,800\\}' AHD_watkins1985.txt | head",
 "description": "Find AHD wei-2 / wi-ro entry"
}
```


### [2026-10-16T05:13:54.532Z] TOOL RESULT

```
wi-ro- (VIRILE) and *g”end- from g’en- (GYNECOLOGY). For man as a human being, the oldest word was apparently *manu- (man-'), as preserved in English MAN and in Slavic and Sanskrit. In other dialects we find interesting metaphori- cal expressions, which attest a set of religious concepts opposing the gods as immortal and celestial to mankind as mortal and terres- trial. Man is either *mortos, “mortal” (mer-2, “to die’), or *dhghomyo-, ‘“‘earthling”’ (dhghem-, “earth”).
wi-ro- peku).
wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. 
vital force,” whence “long life, the eternal recreation of life, eter- nity” (EON). It is noteworthy that the idea of “holy” is intimately bound up with that of “whole, healthy” in a number of forms: kailo- (WHOLE and HOLY), swento- (SOUND?), and sole-, whence Latin salvus (SALVATION). An ancient root relating solely to religion is sak- (SACRED).
Vital force, life, long life, eternity; also “endowed with the acme of vital force, young.” 1. Extended form in Germanic *aiwi in: a. Old English a, ever: No}; b. Ger- manic *aiwi + *wihti, “ever a thing, anything” (*wihii-, thing; see wekti-), in Old English Gwiht, duht, anything, “ever a creature”: AUGHT!; c. Old English &fre (second element obscure), ever: EVER; EVERY, NEVER; d. Old Norse ei, ever: AYE?; NAY. 2. Suffixed form *ai-wo- in: a. Latin aevum, age, eternity: COEVAL, LONGEVITY, ME- DIEVAL, PRIMEVAL; b. suffixed form *aiwo-tdt- in Latin aetds (stem aetdt-), age: AGE; COETANEOUS; C. suffixed form *aiwo-terno- in Latin aeternus, eternal: ETERNAL; SEMPITERNAL. 3. Suffixed form *aiw-en- in Greek aidn, age, vital force: EON. See also *yuwwen- under yeu-. [Pok. aiu- 17.]
Vital force. Perhaps related to wi-ro-. Zero-grade form *wi- (< *wia-) in Latin vis, force, with irregular
Vital force, youthful vigor. Earliest form *ayeu-; variant of aiw-. Suffixed zero-grade form *yuwen- (< *yu-sen-), “possessing youthful vigor,” young. 1. Further suffixed form *yuwn-ti- in Germanic *jugunthi-, *jugun- tha- in Old English geoguth, youth: YOUTH. 2. Further suffixed form *yuwn-ko- in: a. Germanic *juwungaz becoming *jungaz in (i) Old English geong, young: YOUNG (ii) Old High German jung, young: JUNKER (iii) compound *jung-fréw6-, young lady (see per’); b. Old Irish 6ac, Irish Gaelic 6g, in oglach, soldier: GALLOW- GLASS. 3. Latin iuvenis, young: JUNIOR, JUVENILE; JUVE- NOCRACY, REJUVENATE. [Pok. 3. ieu- 510.]
```


## [2026-10-16T05:13:56.802Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o -i 'Vital force. Perhaps related to wi-ro-.\\{0,500\\}' AHD_watkins1985.txt; echo; grep -o -i '.\\{30\\}wi-ro-\\. Man\\..\\{0,700\\}' AHD_watkins1985.txt",
 "description": "Full AHD wei-2 and wi-ro entries"
}
```


### [2026-10-16T05:13:57.225Z] TOOL RESULT

```
Vital force. Perhaps related to wi-ro-. Zero-grade form *wi- (< *wia-) in Latin vis, force, with irregular
```


## [2026-10-16T05:13:59.738Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; n=$(grep -n 'Vital force. Perhaps related to wi-ro-' AHD_watkins1985.txt | cut -d: -f1); sed -n \"$((n-2)),$((n+4))p\" AHD_watkins1985.txt; grep -n 'wi-ro-\\.' AHD_watkins1985.txt | head; grep -n 'WORLD' AHD_watkins1985.txt|head -3",
 "description": "AHD context lines"
}
```


### [2026-10-16T05:14:00.255Z] TOOL RESULT

```
74
weia-
Old English war, seaweed: SEAWARE. 3. Suffixed zero-grade form *wi-ria- in Latin (of Celtic origin) viriae, bracelets: FERRULE. 4. Suffixed form *wei-ti- in Ger- manic *with- willow, in Old English withig, wiry: wITHY. 5. Suffixed zero-grade form *wi-t- in Germanic withj6n- in Old English withthe, supple twig: wITHE. II. Form *weia-, zero-grade *wi- (< *wia-). 1. Suffixed form *wi-ti- in Latin vitis, vine: VISE; VITICULTURE. 2. Suffixed form *wi-td- becoming *wittd in Latin vitta, headband: viTTA. 3. Suffixed form *wi-ri- probably in Greek iris, rainbow, and Iris, rainbow goddess: (IRIDACEOUS), IRIDO-, IRIS, IRIS; (IRIDIUM), (IRISITIS). 4. Suffixed form *wi-n- per- haps in Greek is (genitive inos), sinew: EXINE, INOSITOL, INOTROPIC. [Pok. 1. wei- 1120.] wei-?. To go after something. Suffixed o-grade form in Germanic *wai-thj6-, “pursuit,” with denominative *waithanjan, to hunt, plunder, in Old French gaaignier, gaigner, to obtain: GAIN}; ROWEN. [Pok. 3. wei- 1123.] wei-%. To wither. Extended form *weis- in Germanic *wis- in suffixed form *wis-n-6n in Old English wisnian, to wither, shrivel, shrink: wizEN. [Pok. 2. wei- 1123.] wei-*. Vice, fault, guilt. 1. Suffixed zero-grade form *wi-tio- in Latin vitium, fault, vice: vICE1, vICcIoUs, VITIATE. 2. Suffixed form “wi-tu- in: a. Latin vitiligo, tetter (< “blemish”): vITILIGO; b. Latin vituperdre, to abuse (perhaps formed after Latin recuperdre, to regain; see kap-): VITUPERATE. [Pok. 1. wi- 1175.] weid-. To see. I. Full-grade form *weid-. 1. Germanic *witan, to look after, guard, ascribe to, reproach, in: a. Old English witan, to reproach: Twit; b. Old Proven- gal guida, a guide: GUIDE; c. Germanic derivative noun *witi- in Old English wite, fine, penalty: WITE!. 2. Suf- fixed form *weid-to- in Germanic *wissaz in: a. Old English wis, wise: WISE!; b. Old English wisdém, learn- ing, wisdom (-d6ém, abstract suffix; see dhé-'): WISDOM; c. Old High German wissago, seer, prophet: WISEACRE; d. Germanic *wissdén-, appearance, form, manner, in (i) Old English wise, wis, manner: WISE? (ii) Old French guise, manner: GUISE. 3. Suffixed form *weid-es- in Greek eidos, form, shape: EIDETIC, EIDOLON, IDOL, IDYLL, -OID; IDOCRASE, KALEIDOSCOPE. 4. Perhaps Greek Haidés (also Aidés), the underworld, perhaps “the invisi- ble” (> French Hadés): HADAL, Hangs. II. Zero-grade form *wid-. 1.Germanic *wit- in: a. Old English wit, witt, knowledge, intelligence: wit}; b. Old English wita (genitive plural witena), wise man, councilor: WITENAGE- MOT. 2. Germanic *witan in Old English witan, to know: WIT2; UNWITTING. 3. Suffixed form *wid-to- in Germanic *wissaz, known, in Old English gewis, gewiss, certain, sure: IWIS. 4. Form *wid-é- (with participial form *weid-to-) in Latin vidére (past participle visus), to see, look: VIDE, VIEW, VISA, VISAGE, VISION, VISTA, VOYEUR; ADVICE, (ADVISE), BELVEDERE, CLAIRVOYANCE, ENVY, EVIDENT, INTERVIEW, PREVISE, PROVIDE, REVIEW, SU- PERVISE, SURVEY. 5. Suffixed form *wid-es-ya in Greek idea, appearance, form, idea: IDEA, IDEO-. 6. Suffixed form *wid-tor- in Greek histdr, wise, learned, learned man: HISTORY, (STORY!); POLYHISTOR. 7. Suffixed nasal- ized form *wi-n-d-no- in: a. Irish fionn, white (< “clearly visible”): COLCANNON; b. Welsh gwyn, gwynn, white: PENGUIN. 8. Celtic compound *dru-wid-, ““knower of trees” (*dru-, tree; see deru-). III. Suffixed o-grade form *woid-o- in Sanskrit vedah, knowledge: VEDA; RicG- VepaA. [Pok. 2. ufe)di- 1125.] weidh-. To divide, separate. 1. Suffixed zero-grade form *widh-ewo-, “bereft,” feminine *widh-ewd-, “woman separated (from her husband by death),” in Germanic *widuw6 in Old English widuwe, widow: wiDow. 2. Zero-grade form *widh- in Latin dividere, to separate (dis-, intensive prefix): DEVISE, DIVIDE, POINT-DEVICE. [Pok. weidh- 1127.] weie-. Vital force. Perhaps related to wi-ro-. Zero-grade form *wi- (< *wia-) in Latin vis, force, with irregular
weik-'
derivatives violdre, to treat with force, and violentus, vehement: VIM, VIOLATE, VIOLENT. [In Pok. 3. wei- 1123.] weik-', Clan (social unit above the household). 1. Suf- fixed form *weik-slé in Latin villa, country house, farm: VILLA, VILLAGE, VILLAIN, VILLANELLE, (VILLEIN); (BI- DONVILLE). 2. Suffixed o-grade form *woik-o- in: a. La- tin vicus, quarter or district of a town, neighborhood: (VICINAGE), VICINITY; b. Greek oikos, house, and its derivative oikia, dwelling: ANDROECIUM, AUTOECIOUS, DIOCESE, DIOECIOUS, DIOICOUS, ECESIS, ECOLOGY, ECON- OMY, ECUMENICAL, HETEROECIOUS, MONOECIOUS, PAR- IsH, TRIOECIOUS. 3. Zero-grade form *wik- in Sanskrit vis-, dwelling, house, with derivative vaisyah, settler: Vaisya. [Pok. weik- 1131.] weik-2. In words connected with magic and religious notions (in Germanic and Latin). 1. Germanic suffixed form *wih-l- in Old English wigle, divination, sorcery, akin to the Germanic source of Old French guile, cun- ning, trickery: GUILE. 2. Germanic expressive form *wikk- in: a. Old English wicca, wizard, and wicce, witch: WITCH; b. Old English wiccian, to cast a spell: BEWITCH. 3. Possible suffixed zero-grade form *wik-t- imé in Latin victima, animal used as sacrifice, victim (although this may belong to another root *(a)wek- not otherwise represented in English): vicTiM. [Pok. 1. weik- 1128.] weik-3, To be like. 1. Suffixed variant form ‘*eik-on- in Greek eikdn, likeness, image: ICON, (ICONIC), ICONO-; ANISEIKONIA. 2. Prefixed and suffixed zero-grade form *n-wik-és, not like (*n-, not; see ne), in Greek aikés, unseemly: AECIUM. [Pok. 3. weik- 1129.] weik-4. Also weig-. To bend, wind. I. Form weig-. 1. Ger- manic *wik- in: a. Old English wice, wych elm (having pliant branches): wyCH ELM; b. Swedish viker, willow twig, wand, akin to the Scandinavian source of Middle English wiker, wicker: WICKER; C. Old Norse vikja, to bend, turn, probably akin to the Scandinavian source of Old North French wiket, wicket (< “door that turns”): WICKET. 2. Germanic *waikwaz in: a. Old Norse veikr, pliant: WEAK; b. Dutch week, weak, soft: WEAKFISH. 3. Germanic *wik6n-, “a turning,” series, in Old English wicu, wice, week: WEEK. II. Form *weik-. Zero-grade form *wik- in: a. Latin vix (genitive vicis), turn, situ- ation, change: VICAR, (VICARIOUS), VICE; VICISSITUDE; b. Latin vicia, vetch (< “twining plant”): veTCH. [Pok. 4. ueik- 1130.] weik-5, To fight, conquer. 1. Germanic “wik- in Old Norse vigr, able in battle: WIGHT2. 2. Nasalized zero-grade form *wi-n-k- in Latin vincere (past participle victus), to conquer: VANQUISH, VICTOR, VINCIBLE; CONVINCE, EVICT. [Pok. 2. weik- 1128.] weip-. To turn, vacillate, tremble ecstatically. 1. O-grade form *woip- in Germanic *waif- in Old Norse veif, waving thing, flag, probably akin to the Scandinavian source of Anglo-Norman waif, ownerless property: WAIF!, (WAIVE), (WAIVER). 2. Variant form *weib- in Germanic *wipjan, to move back and forth, in: a. Old English wipian, to wipe: WIPE; b. Old French guiper, to cover with silk: GUIPURE; c. Middle Dutch and Middle Low German wippen, to swing: WHIP. 3. Perhaps suffixed nasalized zero-grade form *wi-m-p-ila- in: a. Old English wimpel, covering for the neck (< “something that winds around”): WIMPLE; b. perhaps Middle Dutch wimmel, auger (< “that which turns in boring”): WIMBLE. 4. Suf- fixed zero-grade variant form *wib-ro- in Latin vibrdre, to vibrate: VIBRATE. [Pok. weip- 1131.] weis-. To flow. I. 1. Germanic *wisdn-, waisén- in Old English wdse, mire, mud: 00ZE?. 2. Taken by many as a derivative of this root, but probably an independent Indo-European word, is the suffixed form *wis-o- in Latin virus, slime, poison: VIRUS. 3. Extended zero-grade form *wisk- possibly in Latin viscum, mistletoe, birdlime: VISCID, VISCOUS. II. Attributed by some to this root, but more likely of obscure origin, are some Germanic words
75
wel-3
1135:Old English war, seaweed: SEAWARE. 3. Suffixed zero-grade form *wi-ria- in Latin (of Celtic origin) viriae, bracelets: FERRULE. 4. Suffixed form *wei-ti- in Ger- manic *with- willow, in Old English withig, wiry: wITHY. 5. Suffixed zero-grade form *wi-t- in Germanic withj6n- in Old English withthe, supple twig: wITHE. II. Form *weia-, zero-grade *wi- (< *wia-). 1. Suffixed form *wi-ti- in Latin vitis, vine: VISE; VITICULTURE. 2. Suffixed form *wi-td- becoming *wittd in Latin vitta, headband: viTTA. 3. Suffixed form *wi-ri- probably in Greek iris, rainbow, and Iris, rainbow goddess: (IRIDACEOUS), IRIDO-, IRIS, IRIS; (IRIDIUM), (IRISITIS). 4. Suffixed form *wi-n- per- haps in Greek is (genitive inos), sinew: EXINE, INOSITOL, INOTROPIC. [Pok. 1. wei- 1120.] wei-?. To go after something. Suffixed o-grade form in Germanic *wai-thj6-, “pursuit,” with denominative *waithanjan, to hunt, plunder, in Old French gaaignier, gaigner, to obtain: GAIN}; ROWEN. [Pok. 3. wei- 1123.] wei-%. To wither. Extended form *weis- in Germanic *wis- in suffixed form *wis-n-6n in Old English wisnian, to wither, shrivel, shrink: wizEN. [Pok. 2. wei- 1123.] wei-*. Vice, fault, guilt. 1. Suffixed zero-grade form *wi-tio- in Latin vitium, fault, vice: vICE1, vICcIoUs, VITIATE. 2. Suffixed form “wi-tu- in: a. Latin vitiligo, tetter (< “blemish”): vITILIGO; b. Latin vituperdre, to abuse (perhaps formed after Latin recuperdre, to regain; see kap-): VITUPERATE. [Pok. 1. wi- 1175.] weid-. To see. I. Full-grade form *weid-. 1. Germanic *witan, to look after, guard, ascribe to, reproach, in: a. Old English witan, to reproach: Twit; b. Old Proven- gal guida, a guide: GUIDE; c. Germanic derivative noun *witi- in Old English wite, fine, penalty: WITE!. 2. Suf- fixed form *weid-to- in Germanic *wissaz in: a. Old English wis, wise: WISE!; b. Old English wisdém, learn- ing, wisdom (-d6ém, abstract suffix; see dhé-'): WISDOM; c. Old High German wissago, seer, prophet: WISEACRE; d. Germanic *wissdén-, appearance, form, manner, in (i) Old English wise, wis, manner: WISE? (ii) Old French guise, manner: GUISE. 3. Suffixed form *weid-es- in Greek eidos, form, shape: EIDETIC, EIDOLON, IDOL, IDYLL, -OID; IDOCRASE, KALEIDOSCOPE. 4. Perhaps Greek Haidés (also Aidés), the underworld, perhaps “the invisi- ble” (> French Hadés): HADAL, Hangs. II. Zero-grade form *wid-. 1.Germanic *wit- in: a. Old English wit, witt, knowledge, intelligence: wit}; b. Old English wita (genitive plural witena), wise man, councilor: WITENAGE- MOT. 2. Germanic *witan in Old English witan, to know: WIT2; UNWITTING. 3. Suffixed form *wid-to- in Germanic *wissaz, known, in Old English gewis, gewiss, certain, sure: IWIS. 4. Form *wid-é- (with participial form *weid-to-) in Latin vidére (past participle visus), to see, look: VIDE, VIEW, VISA, VISAGE, VISION, VISTA, VOYEUR; ADVICE, (ADVISE), BELVEDERE, CLAIRVOYANCE, ENVY, EVIDENT, INTERVIEW, PREVISE, PROVIDE, REVIEW, SU- PERVISE, SURVEY. 5. Suffixed form *wid-es-ya in Greek idea, appearance, form, idea: IDEA, IDEO-. 6. Suffixed form *wid-tor- in Greek histdr, wise, learned, learned man: HISTORY, (STORY!); POLYHISTOR. 7. Suffixed nasal- ized form *wi-n-d-no- in: a. Irish fionn, white (< “clearly visible”): COLCANNON; b. Welsh gwyn, gwynn, white: PENGUIN. 8. Celtic compound *dru-wid-, ““knower of trees” (*dru-, tree; see deru-). III. Suffixed o-grade form *woid-o- in Sanskrit vedah, knowledge: VEDA; RicG- VepaA. [Pok. 2. ufe)di- 1125.] weidh-. To divide, separate. 1. Suffixed zero-grade form *widh-ewo-, “bereft,” feminine *widh-ewd-, “woman separated (from her husband by death),” in Germanic *widuw6 in Old English widuwe, widow: wiDow. 2. Zero-grade form *widh- in Latin dividere, to separate (dis-, intensive prefix): DEVISE, DIVIDE, POINT-DEVICE. [Pok. weidh- 1127.] weie-. Vital force. Perhaps related to wi-ro-. Zero-grade form *wi- (< *wia-) in Latin vis, force, with irregular
1170:wi-ro-. Man. Derivative of weie-?. 1. Germanic shortened from *wiraz becoming *weraz in: a. Old English wer, man: WEREWOLF, WERGELD; b. Germanic compound
```


## [2026-10-16T05:14:01.928Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '1170p' AHD_watkins1985.txt | cut -c1-900",
 "description": "AHD wi-ro entry"
}
```


### [2026-10-16T05:14:02.324Z] TOOL RESULT

```
wi-ro-. Man. Derivative of weie-?. 1. Germanic shortened from *wiraz becoming *weraz in: a. Old English wer, man: WEREWOLF, WERGELD; b. Germanic compound
```


## [2026-10-16T05:14:04.094Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '1171,1174p' AHD_watkins1985.txt | cut -c1-900",
 "description": "AHD wi-ro continuation"
}
```


### [2026-10-16T05:14:04.777Z] TOOL RESULT

```
wrod-
*wer-ald., “life or age of man” (*-ald-, age; see al-3), in Old English weorold, world: woRLD; c. Frankish *wer- wulf, “man-wolf” (*wulf, wolf; see wikvo-), in French garou, werewolf: LOUP-GAROU. 2. Latin vir, man: VI- RAGO, VIRILE, VIRTUE, (VIRTUOSA), (VIRTUOSO); DECEM- VIR, DUUMVIR, TRIUMVIR. 3. Possibly Latin ciria, curia, court, if regarded as from *co-vir, “men together” (co-, together; see kom): CURIA. [Pok. uiro-s 1177.] wleik-. To flow, run. Zero-grade form *wlik-. 1. Adjective *wlik-u-, wet, in: a. suffixed form *wlik-w-d- in Latin liquare, to dissolve: LIQUATE; b. suffixed form *wlik-w-é- in Latin liquére, to be liquid: LIQUESCENT, LIQUID, LIQUOR; DELIQUESCE, LIQUEFY. 2. Suffixed form *wlik-s- in: a. Latin lixa, lye: LIXIVIATE; b. Latin prélixus, poured forth, stretched out in front, extended (pro-, forth; see per’): PROLIX. [In Pok. leiku- 669.] wlkwo-. Wolf. 1. Germanic *wulf
wrdd-
ROSE}, 3. Zero-grade form *wrd- in Iranian *wrd in Persian gul, rose: JULEP.]
```


## [2026-10-16T05:14:09.058Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'wīr\\b\\|wir \\|wyl\\b\\|warm\\b\\|wlm\\b' PHD_mackenzie.txt | head -20; echo ---NYB; grep -n -i 'wīr\\b\\|wlm\\|warm\\b' NYB_vol2_glossary.txt | head -20",
 "description": "Grep MacKenzie and Nyberg for wir/warm"
}
```


### [2026-10-16T05:14:09.458Z] TOOL RESULT

```
506:        aswir [PR/LSYA < A prsy'; ...
539:       duAwir [dwsw'll (M dwjw'r), ...
608:add sirwir [s'lw'l] helmet.
1312:aweran ['wyl'n l , )pyl'n l I N weran] desolate, ruined.
1321:awMan [OLEI)n, v. oy I M )wyl'n, N €fan] they, those.
2142:duAmen [dwlm(y)n l I = M, N dulman] enemy.
2155:dus-I-wir [dwl-wyl] evil-minded.
2468:garm [glm I M grm, N ......] warm, hot.
2472:garmog [glmwk l] warm, ardent, fervent.
2474:garmser [glmsyl IN.......,] warm region, lowlands.
2974:huram [hwlm I N xurram !] happy.
4675:star-Oimir, -oimur [stl'wlm)l, -'w!mwl] astrologer.
5208:lwarm [wlm I N barm] memory.
5210:lIwarm [wlm I N barm] pool, reservoir.
5329:weA [wyl I = M, N bel] more.
5399:lwir [wyl I M wyyr] man, hero.
5400:lIwir [wyll M wyr-, N bir] memory, mind.
5401:3wir [wyll N bir] thunderbolt.
5402:wirastan, wiray-, (P wiraz-) [wyPstn', wyl)d-, (wPe-) I M wyr)st,
5566:xorIYla [Tg < A tmryn; hwlm)k l IN . . . . ] date.
---NYB
563:apa-zón [’pzwn'] increase, addition 11217; tan pat-~ kunéh increase thy physical well being 21%, cf s. v. ?pat (11); increase of spiritual blessings 50%. — MPrs ’bzwn (A-H IT); Paz. awazün; NP afzün ‘more, greater’; < *abi-Zavana-, in which api- was substituted for abi-, v.s. v. apa-; from apa-zūtan, q.v. Wikander, Orbis XXXI, 1972, 183—184, prefers the read- ing Ppzn'] = äp-zan ‘a bath(ing vessel)’, NP abzan referring to the corresponding passage of Sn: bi- garmäbah šau ‘go to the warm bath!’
1636:garm [glm], garmök [glmwk'] hot, warm 1420, 41?9, 10122. — Av. (515) garoma-, (516) garomu- ‘heat; MPrs grm’g ‘heat’ (A-H I); NP garm. l
2070:hu-ram [hwlm] cheerful, glad 67%; bliss- ful, of Paradise, comp. ~-tar 66’. — Paz. cüram; NP xurram; in some way or other to be connected with Av. (1511) ram- ‘to rest, to repose’. Cf the next w. and huraméh.
2072:hu-ramak [hwlmk'] having good herds of cattle 5076, with the gl. ku ramak 4 apdrik veh dānēt dästan ‘that is: it knows how to breed other cattle [than sheep, ete.] in the best way’. — V. ramak. Paz. hurama; translates Av. (1857) hvq0wa-.
2802:dātār ~, passim; ~ apazonik (q. v.); ~ + x"atài 1222, 745. 75%. "7922, 85H. 894. 12015; ~ bag 2117. 22%; rēc + ~ the first day of the month 95%. — 2. the star of Jupiter 510-12, 77, — 3. n. pr. of human beings: a) the king ~ son of Shapuhr 165—179. 11618; ~ son of Artaxsér 11617; b) a Mobad 1104. — Av. (285 sqq.) Ahura- Mazdāh- in two separate ws.; inser. Prth 'hwrmzd; Prs ^whrmzdy, but as n. pr. of an ordinary man hwlmzdy (KZ); MPrth Prs ^whrmyzd (*whrmzdbg ‘the primordial man’); Paz. Hormezd (Hurmazda and other forms); NP Hurmuzd, Ormuz(d).
3041:patiš [pts] adv. 1. before (= pēš), with hac: ~ hac zāyišn i ... before the birth of ... 365. — 2. used instead of pat if it refers back to an encl. pron. in the be- ginning of the sentence: cē-m anākēh vas ~ kunēnd (BYDWN-x;) for they will do much harm to me 954; i ka-t anākēh ~ kuném for we shall do. harm to thee 76°; api-š dēvān apasós ~ kunénd and the devs sneer at him 7576-2"; api-ščin ~ nē virroyam and I do not believe in them 64%; cigan ka-šān Sir i garm ~ andar dösend as if warm milk were milked upon them 10121-22; 4228; 8024-26; 9825-26, . 3, as a substitute for the prep. pat + the encl. pron. of the 3d p. sg. -$: on, to, at (etc.) him, her, it 4?6. 3212, 4726, 559.16, 6311.16, 6420.24 6614, 801, 8615.
4341:x"arm [hwlm] sleep 3215. — < a¥amr through metathesis, MPrth xwmr (S, MHC), < z"amn (g.v.) through dissi- milation of -n- > -r after -m-.
6301:hmky: hamak hwlmzdy: Öhurmazd hwslwb: Xösröi
6443:awīr, avīr: apēr
```


## [2026-10-16T05:14:12.801Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^vīr\\|^vir \\|^varm\\|^vīr \\|^vīrāy\\|vīr \\[' NYB_vol2_glossary.txt | head; grep -n -i 'varm\\b' NYB_vol2_glossary.txt|head -5",
 "description": "Grep Nyberg for vir/varm"
}
```


### [2026-10-16T05:14:13.325Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:14:15.516Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '\\[wyl\\]\\|\\[wlm\\]\\|\\[vyl\\]' NYB_vol2_glossary.txt | head; grep -n -i 'memory' NYB_vol2_glossary.txt | head",
 "description": "Grep Nyberg by Pahlavi spelling"
}
```


### [2026-10-16T05:14:15.852Z] TOOL RESULT

```
4171:1yir [wyl] man, pl. eas. obl. ~-dn: gös- pandan virün cattle and men 41%, the
4175:2vir [wyl] a mental faculty, reason, in- tellect 39%, 551. — Av. (1454) ®vira-; Paz. (Mx, SGV) vir, Skr. v. smrti.
858:ayyāt [’dyb’t'] memory 11". 124; andar ~ dästan to keep in memory 71°. — Ps. ’by’t; MPrth ’by’d, ’n-’by’d ‘not remem- bering’; MPrs ’y’d (BBB, Sogd. 2126); Paz. ayäd, NP ydd. Verbum 224.
```


## [2026-10-16T05:14:18.665Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '4171,4180p' NYB_vol2_glossary.txt; echo ---BRT; grep -n 'vīra-\\|vīrō\\b\\|^ *vīra' BRT.txt | head; grep -n '2vīra\\|²vīra\\|vīra- m\\.' BRT.txt | head",
 "description": "Nyberg vir entries; Bartholomae vira"
}
```


### [2026-10-16T05:14:18.968Z] TOOL RESULT

```
1yir [wyl] man, pl. eas. obl. ~-dn: gös- pandan virün cattle and men 41%, the
213
Viröi-pahr
Phl rendering of Av. pasu vira; pat hän i virdn gobišn 58°. — Av. (1453) vira-; MPrs wyr, v. Sogd. 52.
2vir [wyl] a mental faculty, reason, in- tellect 39%, 551. — Av. (1454) ®vira-; Paz. (Mx, SGV) vir, Skr. v. smrti.
virästak [wyl’stk'] curried, tanned 107°.
virästan [wyl'stn'] vērāy- [wyl’d-] to prepare, to arrange, to adorn: apāc ~ to restore, to renew 711%; pt. viräst well executed 12027; — 10622 read with the MSS vīnārēnd instead of virdyénd. — Av. (1514) raz- and (1520) rad- have inter- mingled in SW where raz- > rad-. MPrth wyr sin wyrz- (S, A-H III), cf viräz-; MPrs wyr’stn wyry-, cf Arm. lw. varsa- viray ‘hair-dresser’ (DkM 7573 wlswyl'd); Ps. wyl’sty, wyl’d-, cf ärastan, patrčistak, räyenitan. Verbum 187; Ghilain 52. 69.
Viraz [wyl’c'] n. pr. 107. — Av. (1454) Vīrāz-, more correct Virdza-. In BP traditionally read Vīrāf, which is now generally regarded as a misreading; de- fended by de Menasce, JA 237, 1949, 3—6.
viräz- [wl’c-] pres., to arrange, to bring about, opt. 2nd p. sg. virdzés in an inter- rogative clause 358. — Probably identical with NW wyr?štn wyr’z- (v. s. v. virüstan) in spite of w- instead of wy-.
virēk [wlyk'] flight 1°. 821, from
---BRT
```


## [2026-10-16T05:14:21.883Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'vira-\\|vlra-' BRT.txt | head -30",
 "description": "Grep Bartholomae for vira"
}
```


### [2026-10-16T05:14:22.198Z] TOOL RESULT

```
5851:•  j.  aspa.vira-gan-  Adj.  'auf  Roes  und
14245:•  j.  drvö.vira-  Adj.  'der  gesunde  Männer, Leute  besitzt':  dadimahl  .  .  dmafsavB  'rä (NP.)  Y.5Ä6;  —  mag%anake{^)  paiU .  .  drvaßaos  'rahe  Y.  16.  10.
15031:•  j.  paiti.vira-  Adj.  'sammt  den  Männern, Menschen'  *':    karsvan    yat    ^amra%fm
15856:•  j.,  g.  pasav-  -.ßav-  m.  'Vieh,  domestizirtes vierfüssigcs  Tier,  Haustier',  Sing,  auch  kolL : azsm  .  .  tJ  nipayanl .  .  ya^a  'sßm  pasa.- vastr?m  (sd.)  Vtj.  89;  —  ki  mH  'sSui ^ mS  nä  >rat3  vists  .  .  axdä  (sd.)  .  .  Y. 50.1;  — /su  F.5(?)";  —  im  Gegensatz 2U  nar-  oder  vira-:  'svamca  naramca  Y. 4-  S  i  —  y^  "^J  'P^  •  ■  °fli»t  vä  narim vä  raiiyät  W. 13.^1;  32;  —  västryehys •sSui  vTräatiä  (sd.)  Y.  JJ.  1 5 ;  —  va/  virpt^ ahmäksng  frada^ai  (sd.)  J  Y.  4:5.  9;  — pairT  'sUs  pain  vlrSng  dadtmahl  Y.  JÄ 6.  a)  in  Dual  Verbindung  mit  vJra-  (sd., audi  fdSt):  -j*  vlra  *Yt.  y.  iz  usw.;  — 'Tirä  Wrayi  Vr.7.3usw,;  —  'subya  vTraäbya V.6.^2.  A)  insbes.  vom  Kleinvieh,  den Schafen  und  Ziegen,  im  Gegensatz  zu staora-  (sdj:  -svamca  staoranameä  masyl- nqmca  sünqmla  vayqmca  V.  2.8;  10,  Äiz, 13;  —  °vasca  (als  NP.)  staoräea . .  masyäca bmngra  Yt.5.89;  Äs,  V.2.8,  9,  11,5.5, 6,  15;  —  °sv5  (AP.)  staeräca  V.  p.  39=;  — •subya  staoralibya  vayafibya  patantaäbya (sd,)  YL  /o.  119;  —  's}ul*g?ribui  ysistahe (sd.)  A.J.  3;  — -pania-dasa  °svs  sraoni.masa F. 25b(?); —  *hvBiSa^a{&A.)  'sus./iva^'> N.  5>V;  —  mit  anumaya-  (sd.):  ustrahe  . . aspahe  .  .  gSuI .  .  mtfnumat  ap?r3näyBk»in yaoida^S  °sSul  ^g^nbus  anumayeke  V.  9. 38 ; 2.  24;  —  bis  hapta  "vö  (AP.)  anumaya  . . fiissrinuyäi  V,  i4- 16.  a)  spez.  als  Opfer- tier: zadhrä  hE ushärayfti .,'sum  hl pacaym
16110:Ei.j~Pi.:  m»/^  In  i^mii  pur  /rä^iamMAl'  i-  p9M*vira- Adj.  (fem.  'rä-)  'desEin-
17692:fra-ßav-  Adj.  'des  Haustiere  voran  sind,  der treffliche  Haustiere  besitzt'.  —  Pü.;  /rät ramak.  —  ')  Abgekürzt  täi  fra/hila  ftävira- läca;  E.  zu  (z'?r>a'}srinAra-.
17734:•  j.  framan.narö.vira-  Adj.  'der  die  Ein- sicht der  Männer  —  ?— ':  usätakam  .  .fra- mmjtarqm  (sd.)  'rqm  G.  5.  5  ;  Vr.  7.  3,
17852:•  j.  fra-vira-  m.  'Befestigungswerk,  Bastei (oder  dgl.)':  Aa%ra  timänä  avastaya  .  .fra- skpml>pmi^a(^&A.)'rfmca  pairi.vanm^a\  ,2.i6.
18151:•  j.  frädatvira-  m.  Name  einer  Gottheit,
18251:'ftä-vira-  Adj.  'de»  Leute  voran  sind,  der treffliche  Leute  hat'.  —  Ki.-.  fräk  vir.  — >)  NA./rflM>a  fäia;  s.  die  Var.
19305:j.  Hmöi  N.  8-,  lid  nmänäl •  j,nrnäna-,g.,j.''dflniana-'',j.'V;'«ff»a- n.  'Behausung,  Haus',  von  jedem  zum Aufenthalt  für  Menschen  (Götter)  und Haustiere  dienenden  Bauwerk,  sowie  auch von  dem  zu  einem  Anwesen  gehörigen Gebäudekomplex;  I)  von  Wohnungen  fUr Menschen  (und  Götter):  yanyS buyä  'nshu ma^yäkanqm  Y.  6i.\;  —  ahmi  *ne  ya^ m!^ayasnBi^{Stve.Tz.)  V.5.45;  —  vasö.. mazdayasna  ahe  'nahe  myasd>m  äaihyäril V,  &22J  —  ätacäni  sünm  'mm  drvatS Yt-5'  3S;  —  <Mi  'tarn  yim  ^alpaihjm Yt5.63;  62;  —  ha%ra  'ni  avastaya  ka~ t>mca  /raslamb>m{s,ü.)Si  ..  V.  2. 26;  — yat  bä  paiti  nä  a/ava  'mm  uedasta  ä%ra- vai  gaomavat  nsirivat  ..  V.J.  2;  15.  ai; —  mürnm  . .  ylF  stunä  v^ärayeiti  iirtsi- mitahe  'nahe  Yt /O.  28;  30;  —  tBm..°na inasilä  ..  dahähi  YtJO.30; —  sraohm .. yS  driyaolca  . .  amava£  'mm  hüm.täsH  Y. $'j.  10;  —  as>m  yS  ahurB  masda  . .  yas> tat  'npm  ahnmm  srirtm  raoximm  frs- d^rirsrym  V.  22.1^;  \.Sy.2i;  —  iaiiihe ka^he  apayisire  'mm  htitaite  hi^ättm  Yt. 5.  loi;  —  aliqm  "nä  hvihätä  .  .  hUhfUe Vti7.  8;  V./j.  4g;  —  hubaotUl  ba^aite °mm  yeAhe  'ne  asis  varmhi  . .  psta  mda- ^aite  Yt.ij.6;  ij.107;  —  iha  ml  tum (nämL./4/fl)  hamJaranuha  *antary.ar^?m •nahe  srJrahe  Ytzj.öo;  jj.  147, 156';  — alU  . .  ramyai  i%a  upa  tmai  °mm  yat ahüiri  Y./O.i;  6'o.2,  Yt  14.41; — vainti ahmi  'ne  sraesS  Y.  tfo.  5;  Yt7j.  52,  FrD. /3;  —  vUfa  'na  sraoiö.psta  yazamaide  Y. 57-34)  —  damt  ha^a  ahmüt 'nät  ..rhyeja ■  •  ^'yeyenti  yejihe  *'?ya*'  sraoh  . .  astf paiti^ants  Y.57. 14;  /o.  7;  —  mä  yave imat  'mm  i^'annS  frazakXi  Y.60.  7;  Vyt 5;  —  xihsii  äfrlnstttu  {jis-viA.  fravas<rfS) ahmya  'ne  vattuhim  asim  . .  xsnüiä  para- yantu  haca  ahmst  'nät . .  msüm  gtnzänä pärayantu  haca  ahmst  'nät  ahmSkfm^a mazdayasnanqm  Yt  13. 157;  Y.  2j.  3;  — aai  ahmSi  'näi  dähäiti  gluica  vqhwa  vlra- nqm/a  Yt.!0.  a8;  —  äat  ..  ahe  'nahe/ra- pi^iws  gäu^  .  -  Y.  j.  3 ;  —  t^it  ahmi  'ne *sänaite  ä^rava . .  äat  ahmi  'ne  Sayhnte  da- hahaca..Y.ii,6;  — /raddhsi  ahe'naheY. 52.4;  4.5,  Vr./J.  13*;  —  'n?m  hS  manyaita paraJa%B  V.  ;*.  28;  ■ —  (8«  miknäi  daiva *aipi.jaiti  'ne  aiAhai  gundayai  (sd.)  V,  3.
22868:J3S  .AbdulkädLn^Lex.äabn.  /.|3i  SWienAW.  ,  .   yar^tö.vira-  Adj.  'wo  die  Menschen
24276:•  j-,  e-'viT&-,vira-  m.'tAami':  nart  iiArfia ..tala  ayao/(sd.)  yäia  pauirJm  'nm  avi ya  bavaiti  YtS.  I3f.;  14.  2;  —  hasanrai bartina  (sd.)  'ranqm  YL5.  96 'J;  —  insbes. der  wehrhafte,  wafleniragende,  'Kriegs- mann': °rahe  k>hrpa  raSimtS  srJrahf  Yt I4.^^'''■,  —  haüaiti  dtm  •rohe  ao/d  Yl /^.  68;  —  a.  noch  a,  a)  im  Gegen- satz zu  aspa-^:  4d . .  galam  (sd.)  nijainti aspagca  'raica  ". .  auf  Ross  und  (Kriegs-) Mann"  Yt./o.  iqi;  —  aspailu  -raEht  Yt ^5-  S3i  —  s.  noch  No.  3.  b)  im  Gegen- satz zu  ^gav-%  gfuica  va^wa  *ranamca\ "Heerden  von  Vieh  und  Männern"  Yt. , ;o.  a8,  13.  $x;  —  gSus  vifhwa  (sd.)  ..j 'ranqm  *-pouruJäs  Y.  62.  i'o.  c)  im  | Gegensatz  zu  pasav-;  a)  'Manne,  Zuge- liöriger;  Leute':  västryehyä . . pasSus  'räatcä "an  des  Bauern  Tieren  und  Leuten"  Y. _?j,  15;  — pasüs  'rSng  ahmakSng frada^äi (sd.)    a   Y.  45-  9 ;  —  p<i'rT  pasas  . .  'ring
24281:•  j.  'vira-  a.  'Verstand,  Einsicht'*. KompE.    —    np,  vir;    DsT.  6tlr.  3.  183.    — ')    iBed.   t.    SWienAW.    6/.    850.  231    vlrTA
24282:•  j.  vira-gan-  .^dj.  'Männer,  Krieger tötend':  daiäAupaiti/  nsit  sahm  jainti 'raja  Yt/4-37;  —  asH..vJraak^S  °raja Aog.  7Ä
24284:■  j.  vira-Dhad-  Adj.  'Männer,  Krieger an-,  überfallend':  aiiS  asparaAätö  'ahohs (NS.)  Aog.  7*.
24289:Komp.:  'vlra--\-aspa;  eig.  'Männer  (als  Rosse d.  i.)  lUm  Gespann  habend' >).  —  Dp.  vgl. vlrS   (JusTI   NB.  371)?   -    ')    iBed.    vgl.  ai.
25944:•  j.  satö.vira-  Adj.  'hundert  Männer  hoch, tier:  'rim  vaOnim  (sd.)  V.4.$a.
29741:•  j.  hazaDro.vira-Adj.(fem.'ra-)'tausend
30485:•  j.  huvira-  Adj.  (fem.  'rä-):  s.  unter 'livira:
```


## [2026-10-16T05:14:30.669Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '24276,24281p' BRT.txt | cut -c1-300; grep -n -i 'vay-\\|vayeiti\\|vyäna\\|vyana-\\|vltar\\|vitar-\\|vätay\\|vatay-\\|vöiöwa\\|voiÖwa\\|voi9wa' BRT.txt | head -20",
 "description": "Bartholomae vay- family"
}
```


### [2026-10-16T05:14:31.048Z] TOOL RESULT

```
•  j-,  e-'viT&-,vira-  m.'tAami':  nart  iiArfia ..tala  ayao/(sd.)  yäia  pauirJm  'nm  avi ya  bavaiti  YtS.  I3f.;  14.  2;  —  hasanrai bartina  (sd.)  'ranqm  YL5.  96 'J;  —  insbes. der  wehrhafte,  wafleniragende,  'Kriegs- mann': °rahe  k>hrpa  raSimtS  srJrahf  Yt I4.^^'''■,  —  haüaiti  
. .  dadfmahl  Y.  56".  6.  P)  'Mensch',  in Dualverbindung  damit:  pasu  'ra  "Tiere und  Menschen"^*  Yt.  to.  112,  *if.  izs>, /*).3z,  Y.il.4,  *V.yo.r8*>,  DkB.131;  — "irä^räi  pasvS  'rayä  Yt. /J.  10;  Vr.  7.3; —  aß . ,  aiuiii'.x^arf^a  fasubya  'raiibya V.  6. 32.
KompA.,  E.;  Ableit.j  s.  noch  No.  3.  —  vX. virä-  m.;  mp.  vir,  PDy.  vir.  —  Pü.!  vh-,  (im Komp.  aoch);  mari.  —  ")  Der  Mann  als  Mass- einheit; s.  Komp.  und  V.  4.  52.  —  ')  S.  da- gegen Yt.   14.   17;  nari  kihtfa  panca.dasaahS.
—  3)  S.  auch  aspa,vitcif;att;  mil  Dualverbin- dung im   1.  Glied.  —  4)  Vgl.  peciidi:sque  vitos-
^uc,  Ovii)  Met.  /.  286.  —  5)  NA,  paiV,  s.  aber Var.  —  6)  Na,  pam.vlra.
•  j.  'vira-  a.  'Verstand,  Einsicht'*. KompE.    —    np,  vir;    DsT.  6tlr.  3.  183.    — ')    iBed.   t.    SWienAW.    6/.    850.  231    vlrTA
3242:•  j.  a-8avay-  Adj.  (auch  mask.)  'der  keinen Trug  übt,  nicht  trügt,  betrügt':  *''T'r/(NSm.) nama  aAmt  *vtöavl/  nqtna  ahmt  Yt.  /.  14; —  n^mö  voku  °vim  (ASm.  statt  n.)  aibai- hm  Vr. 21. 3,  Yt  luz;  —  yeiihe  vähm Äangryuinäili  "vil  (NSf.)  paoirls  (sd.)  .  . i4ä  *dämya  (sd.)  xlaztäi  Yt.  iO,  143.
4650:äahtmm  gä'^anqm  sraohrät  pairistaytili  N.^'<>;  —  mmS  ahuräi  mazdai  mmö N.4^;45^*fH.2.i3; — yd  'nyehe  dahmahe  amisaiibys spintaHbyS mmS'nyagsqm  asao- bansma  *frast»r3nfe  ii.104;  lOi;  —  bsöalnqm  V.i^. 25:32;  —  »üi/  xsnSvayeiti  ahu- iia  hislahe  ..  'nyehe  dvan  (sd)  srayatül  r?m  mazdam  tUSit  °nye  (als  AP.)  amisO. V.j.zg;  N.6',7; —  hvSiits  vä  ySiitö  (i'3)  |  ¥1,70.139;'  '39;  —  hapta  hanti  *käva- yim  vä  'inim  *hais^aeTia  (sd.)  .  .  cayqn ,  iiayS  ratavS  .  .  aai  'nyahu  ralu/risü  N. N./;  — ]avada  'niyam  md^ifia/fi  . .  Bh.  102.  a)  mit  ciV'' :  saoiyanlqm  vfn'üra- 5.  4(?);  —  "nyqmca  suttm  ..  N.ff2(,?);  — jamm  Uta  "nyasHt  (als  APn.)  haxayS  Yt. ^rayS 'nya  (als  APm.)  maya  nihwirgsöU  /p.S9'*'.  NSm.  "/yJ,  ASm.'fiim,  ASn.
4758:nqm  Yt.  J7.2;  —  yö  . .  yazata  ahunm mazdqm  yazata  -/J  spmts  Yt.  J".  1 8,  Y.57.Z ; 2/.2,'Vr./j.  1, 18.1,  ig.i,  23.1,  V.  ig.  19, N,  70;  —  aAur?m  mazdqm  .  .  'sit  sp^ntit yazamaidl  Y.jj.i;  2.2,  25.4,  77.4;  — ii^mS  afturäi  mazdäi . .  'salibyff  spantaAbyS V./p.2s;Ny./.  i,Yt<?.3s,  io.  89. /^.  157, J5.44,  S, /.  i;  —  nsit  xsnävayeiti  ahunm mazdqm  tßit  anye  °^a  sp?nta  Yt.  10. 139; 139;— ^i7/'J  nmätttm  mathantm  ahurahe mazdh  ..  'sanqm  spuntanam  V.  79.32;  32, Y.y.i,  4.7,  22.1.  29.2,  27.2,  Vr.9,6, A.  2. 1 ;  — bsrijayat  ahurd  mazdä  bgry/ay^n sp?ntfi  Yt. /o.  90;  —  yazaite  ahurtm 'IS  sputts  .  .  haom  urvänim Yx.6.\;  —  ahuräi  mazdai  ..  'laAbyS spmtaMyS  .  ,  aiwyS  vanuhibyS  Vr.  Ii.  i ; —  ahurahe  mazdl  .  .  "sanqm  sp>ntanqm sraofahe  asythe  . .  ähr5  Y.  22, 4;  —  ahu- rsica  mazdsi  sraosäica  .  .  rasnvaica  . . mi^räica  .  .  '/aeibyasca  sp>ntaHbyS  . .  Vr. II.  6 ;  Y.  4. 2;  —  ahurahe  mazda  . .  'Sanqm spmlanam  mü-rahe . ,  rUmanasca  ^ästrahe Y.22.23;  (JÄ22,  Yt.7.1.  b)  von  ein- zelnen Göltern:  ahm  at  vahiStfm  . .  hyat sra!st?m  hyat  sp>nt}m  'hm  Y.J7.4;  — astm  vahÜt)m  sra!st?m  °hm  sppnt>m  Yt. j.  18*;  S.  2. 3;  —  ahre  ..  ya^ustsmäi 'Sanqm  spinlanqm  "dem  Ä.,  dem  geschäf- tigsten der  ASp."  Y.I.2;  —  vahu  manS 'hm  sp3nt}m  S.  2.  2;  —  xlfdrtm  vairjm 'hm  sp^trm  S.  2.4;  —  haurvatätim  'hm spintam  S.2.6;  YX. 4-\<i' -j^ amgrsfatätim 'hm  spuntsm  S.  2.7.  ['s'a  spunta  Yt.Ä 38  ist  Einschiebsel,  s.  an-  No.  3.]
5014:•  ').  a-vadö.urvatay-  Adj.  'der  einen  Ver- trag durch  das  (blosse)  Wort  abzuschliessen nicht  quaÜfizirt  ist' "';  myazdava  ratus amyaxdavatum  ratunafm  'vaitlm  aaste antarf  masdayasnäii  ".  .  macht  (erklärt) der  Ä. . .  den  . .  Laien  für  unfähig,  durch das  (blosse)  Wort  einen  Vertrag  abzu- schliessen" A.J.8.
5141:•  j.  ava.urvatay-  f.  'Vertragsbruch'  (?) : ' vi  ha'a  datvayasHaiibys  'vaiti (IS.)  '•  apa.-  ' bar>j  fsd.)  *qya  ratu/rii  ". .  wegen  Ver- tragsbruch .  ."  N.  $4.
5308:•  j.  a-ratu'fri-  Adj.  'der  nicht  r.  ist,  die Ratav  nicht  befriedigt,  es  ihnen  nicht  zu Dank  macht,  gegen  ihren  Willen  ver- stösst':  äahms  zaota  dahmS  upa.sraolärü vispe  ratu/ryö  tanupirii^ö  zaota  tarnt- p>r3%5  upü.sraotltrS  vupe  '/ryüti.^i);  — yai  ig  däiti  dalätH  ^rafufrÜ . .  yesi  aal hSnDit  däiti  daoäiti  '/ris'ü.io^;  wo,  loi'^, S03, 104,55,  *55  ■';  — yi  ^ri/*Aa>räricS yätayeinle  ratufryS  yai  Hat  (ä-ri/)  nSii *Aa>r.'rtci>  yataytinti  'fryO  N.  S8;  gj,  gi, 9-',  93>  95;  —  y^i  •  ■  »o  ratu/ryö  yezi *aai  .  .  uva  -/ryJ  (ND.)  ü.$4;  —  yai arastnm  (sd.)  .  .  pairi.iioa  .  .  °/rya  pasca vä  pars  vä  pairi.ä6a  °/ryS  ii.32;  —  yä yastam  *yazfnti..  nva  *ratu/rya  Aam.srul.- väcayala  (sd.)  ^yax^nti  *«va  *'fiya  (ND.)'' N.  24',  — yö  aiwyänhayäiti  kar>tSsca  °/ryS pasca  aiitiySstim  nitaohydti  ratufrys  N. tV^.  a)  mit  Gen.  dessen,  wodurch  (und wofür)  man  ar.  ist  oder  wird:  yasnahe advakt  (sd.)  ratu/ris  'frii gä'iianqm  N.22; —  kaithqm  ml  gä'^anqm  srutanqm  °/rii3 yä  ^maizö  vä  . .  *srävayeiti  aetaesqm  vacqm "fris  "mit  welchen  aufgesagten  G.  verstbsst
6797:-  .  .  'nasca  vairyan /rasravayeiti\i.50;.f''^-''""''  ''"'^'  r*'«"'  "y^"  ■  -  ^'^  ='  "^^ —zaola{sA.)..zaolarsgatava*'n^mvairTm  °'"'':1  ,  '"^-^  '■''^'««'■''''  >^  '"5«'-^" Aa^rJ^.Tyj«/  N.&;  —  ^vaiti  naram  ..  """'f^^  den,  der  emen  ^/5s  und  Äo/aj/ ■laota  ifA.)  ratufni 'tum  vairim  frasrao-  besitzt,...  Der  nämlich  besiut  emen -4-4fi ^ehe  N.  20;  -   'n?mca  vairtm  srSvayeni  '^^  ^"^""Ik  «^^  '  ■"  ^J"  "-^V,       ,-
8472:brauchten Pflanze :  *h<ata  nS  rnhma  bans- mana  ratu/risi  ^ris.uri'ara  (sd.)  cyävaitis aäaya  'rayti  (NP.)  anhsnl  ".  .  wie  gross sollen  die  Pflanzenstengel  sein?"  N.i^o;  — yezi  *paitila  (sd.)  °varh  upa-doo^litt  ratu- /ri/H.ioi.  S.  auch  3.  a)  oft  neben Feuer,  Wasser,  Rind,  Himmel,  Erde  usw. : xshiivayeiti  ätrmt  .  .  ap^m  .  .  gqm  .  .  °rqin V.f).4Z;  33,  i/.  I,  2,  6,  9;  —  haca  a^rat .  .  Opal  .  .  z^mat  .  .  gaot  .  .  "rayiJf  V. ;/. 10;  —  aHiS  .  ,  apas^a  ttmasca  'rayhsca Ytij.jS;  aS.  86,  Y.ytj.a,  8;  —  asnäalca apäatca  z»mäatca  'rayüatca  Vr.  7. 4;  — hs  äp?m  staoiti  .  ,  zqm  .  .  gqm  .  .  'rqm H.  7.3;  —  ys  gqmcä  ahmcä  dät  apascä 'räsctl  vat^kli  y.  3-^.1 ;  —  yS  gqm  tasö (sd.)  apaslS  °rasca  Y.si-T,  —  vlspä  bal- iazä  apqmca  gavqmea  'ranqmca  Y,52.  a; J2. 7 ;  —  nasuspaim  .  .  äsirysnie  .  ,  apasca Zimasca  'rayäsca  V.  6.y,  /.j,  2/.3,  Y.  j.  16, 2.16,  Vr./Ö.3,  G.2.6;  —  ntzbayemi  zqm .  .  äppm  .  .  'rqm  asaonim  V,  ;p.35;-  — imat  vö  sps  jaiüyemi  . .  tfmO  . .  'rä  Y.
8522:•)  Der  iiiijak  des  RV.;  s.  Brrgaigne  Rel. v*d.  r.  57;  dazu  IIauq  Eäsaysi  289,  Bthu  BB. 8.  2x7,  KZ.  2Ä  II  und  unter  dti^'ani-  mit No.  3  und  ^tavay-;  ferner  SBE.  47.  143.
8663:•  g.  uz«ina-  (,  j.  asma-)  Adj.  'ehrerbietig gegen  — '  (Dat.):  ks  'mSm  cör)i  vyänayä puinm  pfkre  "wer  machte  mit  Weisheit den  Sohn  ehrerbietig  gegen  den  Vater?" Y-44.r-
8949:j.  kanynm :  s.  ^kavay-.
9127:'kavay-
9130:KompA.;  AUntl.  {s.  k.i.-ya-,  ij:-r\  —  Vgl. tiavay-  EN.  —  ai.  Air-.if-  m.  (IIB.  S.  227).  — P6.!  (kdk,  voM.)  tiiyii-,  s.  iinttt  <.ic-f/.iK- mit No.  —  ">  iKI.  s.  C1.0.  KZ.  fj.  300  und  No.  2, 3,  S-  -  ^)  S  i'"''-  3  ai  vgl.  No.  5.  --  3)  IF. /.  191,  193  No. ;  S  ^<>S.  I  b,  MeILLeT  bei Bgm.  Grdr.'  /.  1091.  —  t)  Doch  s.  auch  Komp. \Ln:i').  —  i>  Stven.  nnter  dem  EN.  —  <•)  -f statt  -va,  S  3Ö1V.  31,  Abi;esehcn  von  11  ftjr -0,  formell  gleieli  /'Jrvyi/j-Äi.
9131:•  j,  'kavay-  m,  EN.  eines  Gläubigen: 'j'eis  asaom  Vt.7j.119;  — garslahe  "vöU asaonS  "des  G.,  Sohns  des  A'.  . ."  Vt.  /  J. 123;  —  pouruslöis  'vöis  asaonö  "des  F., , Sohns  des  K.  .  ."  Vt.  y.  114.
9672:Vgl.  Modi  Twö  Amuleis  of  ancient  Persia (Joura.  Anthrop.  Soc.  Bombay  igozi  1 1  ff.,  wo- nach der  Text  besagen  soll:  "May  we,  who perform  tbe  Yasna  in  the  proper  way,  be relieved  (from  the  evil  inSuence  of]  the wretched  Aum,  JCuro,  Tareuiani  aiiA  Karapait." Ich  kann  das  nicht  herauslesen,  iura  soll np.  iür  'blind'  sein  und  synonym  mit  tiavay- Bed.  a!
9971:nstr.  {'mittelst') :  yö  adniim "iiila  vlxrBmmtim  x'arim 2)  '(den  Vertrag)  ver- ' :  mi'hnm  mä  janya  Yt. 'das  Wasser)  treffen'  sva. iniessbar  machen' :yV^  ap>m t/rävayeiti  V.5.37. chlagenauf— ,  erschlagen': aipi.janyh  mi^ra  Yt  10. i:  lies  aipi.jaiti,  Inf.] lieder-,  erschlagen,  töten'; upäk?m  janaita'''  ava  kl ; — yS  frasiiim  usayanqm 't  y,  105;  ~  sraoiö  asyö anyät  'V.iff.41; —  masda- ■ivanaHbil  (sd.)  avajamm udrahe  avayiulnS  ha!c5 51.  a)  bes.  vom  Töten ■e;  ban'arg  aiinqm  ..  ava.- Sf.';  —  xraßlnm  ava.- Im  .  .  V.  16.12;  —  Äakyä- vanijm  xra/stranqm  ava.- ;  JÄ73J.  2)  'anfallen,
10315:•  j.  ^^  gä%ä  srävayeiti  aps  vä  paitts.- ^aine  (sd.)  .  .  "gäi^aI^,m  vä  väsyan- ianam"  ". .  ein  Getöse  . .  (hervorgerufen) durch  .."  N. 36'*.
10322:—  '%a  *sravayD  yasmm  yaz>ntim  paitisiaiii (sd.)  ..-%anqm  *sravayamnanqm  paitisti . . N.22;  —  'hih/a  iravayS  apas.'a  ..yaamnS H.  2. 1 3 ;  V.  jÄ  9 ;  —  zara'^uslrpui  , .  °%asfa srävayatitsm  Y. g.i;  N. 48;  —  '%anqmca srao^nm  Y.^,4,  d-i.  22.3;  —  frasrüifi •'ianqm  V.  12.  2;  —  ia/  asti  .  .  'hanqm kank^riitis  Y.~i.i;  N.22;  —  yö  °%anqm anumaiti  (sd.)  va  *anumainyeie  N,  2j;  — y5..anyS  va  kl  dahmö  sruik  '%h  daiaiti *ralu/ris  atruta  (sd.) ..  N.  2^;  —  aiwyäita (sd.)  mazdayasna  '"iä  sr-lvayat  nsil  anaiw- yasta  N.(?5;  —  yS  '>a  srävayeiti  apö  va paitisj^aiiie{%A.)  . .  N.  26;  32;  —  iauAqm na  'ianqtn  srutanqm  aratu/ris  {sA.)i  *ya *maixS  va  ..  srävayeiti  N._37;  22',38,3q;
10324:—  yj  °iä(f  asravayö  *qsta  (sd.)  va  ,  . N.  4i\  4^—45^'^\'^y^*  *alte  maiXyanqm (sd.)  pars  x''arftöil  *°IJaJ'  nöif  srävayeiti N.  25;  —  yS  .  .  *aimm  dahm>m  '%anqm *sraoi!rat  pairistayeiti  N.  44.  A)  für die  einzelnen  Tagesabschnitte  {asnya-)  war das  Beten  bestimmter  Grf^^stücke  vorge- schrieben: .(■aiOTJi'  kaca  ulaAinanqm  "^a- nqin . .  * Aavaiiinqm  °'ianqm  . .  *rapi^wina' nqm  ''ianqm  .  .  uzayairinqm  '"hanqm  . . aiwi.srO^rimanqm  'ianqm  ratu/rii  fra- jasaitil  N.46—S1.
10581:erschrecken':  yö  g^wqm  .  .  janaiti  vil vayeiti  vä  xraosyäti  vä  pazdayäti  (sd.)  vä
```


## [2026-10-16T05:14:34.367Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"'verfolgen\\|Verfolger'\\|Verfolgung'\" BRT.txt | head; ",
 "description": "Bartholomae verfolgen glosses"
}
```


### [2026-10-16T05:14:34.843Z] TOOL RESULT

```
22699:Eig.Bed.?    Etwa 'Verfolger'  lum  V.oä(^)-?0.
23436:mit  aipi  'verfolgen,  heijagen  hinter  — ' (Akk.) :  mihr»m  .,yS.,  avarvhi  Alf  api- vaHi^i  bafvart  ypnqnä  nisirinaoiti  "der., hinter  ihnen,  den  wehrlosen  herjagt,  zehn- tausend Sch^ge  austeilt"  Ytio.  37.
23462:•  j.  vätay-  f.  'Verfolgung',  Bezeichnung eines  strafbaren  Delikts :  väiti  F.  25  a.
23978:•  j.  'vitar-  m.  i)  'der  nachjagt,  Verfolger' (mit  Akk.) :  'tartm  paskäi  hamirik»m  Jan- 1 iar?m  (sd.)  parö  dusmainyäm  "der  den Gegner  von  hinten  her  verfolgt .  ."  Yt  17. , la;  —  °ta  nama  ahmi  Yt /.  13.  j
```


## [2026-10-16T05:14:36.719Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '23425,23436p' BRT.txt | cut -c1-400",
 "description": "Bartholomae vay- head"
}
```


### [2026-10-16T05:14:37.085Z] TOOL RESULT

```
V^dd  V.  S.  37.  I
bL  vgl.  vSyati;  1.  noch  PQ.  —  Pü.:  frdySaii'''i  '
(■OB  'jrojiai'),  in  V.  S  erl.:  afii  aftäritan.  —  I
>)  V.  *  weht  p  ra  k  >t  Kalt  p  rn  d  at    VgL  lu
fravätay-  No.  1.
•  j.  HS-  V,,  Pass.  Meficere'.     Praes.  a? (Pass.)  uya:  —  PPfP.  Üna-.
i)  PPM.  'nicht  ausreichend,  ungenügend, mangelhaft' :'V^r^i7/ami;'ii  ita  vohti  västrya (sd.)  uyamna  anuyamnäii  daste  ". .  damit was  mangelhaft  ist,  vollkommen  gemacht werde"  Vr.  15.  i'\  2)  PPfP.;  a)  'unge- nügend': ä/riii  yä  ünsm  pintam  ksr»- naoiti  p^nrumat  viyiarayäti  (sd.)  ". .  die was  ungenügend  (gefUllt)  ist,  voU  macht, . ." V.25.5.  b> 'geringfügig,  kärg
■i.  ünä-  Adj.  (Gegens.  püri/ä-)\  a.  dazu  BB. 32.  1S9.  —  Pü.  (zn  Vr.):  bavandaläh  {i)  ä  i abavaKdaA  däl,  (in  F.,  V.J:  *am,  (lu  Y.):  nn- deuüich,  —  ■)  Vgl.  zu  dasU,  Sp.  701  f.  — »J  Vgl.  DsT.  ZA.  /.  105,  Mnis  ZDMG.  56. ISO;  doi  Wort  beginnt  ofleabar  mit  ann  •= un\  s.  zu  unä-;  MiLLS'  beide  Letungen  sind
•  j-  vä(y)-  V.  'jagen'.     Praes.  i  va^yY: vy-,  3  vaya-,  'vya-'K  —  PFP.  *vSi^wa:
'jagen,  jagend  verfolgen' :^ff^a8a'a»i_j'^»t apu%ram  Janaiti  vIt  vayäti  va  xraosyäti vä  patdayeiti  (sd.)  vä  V.  75. 5 ;  —  ysi  vlsps U  apayeinti  yq  *aoe  paskät  vyeinii  ". ,  denen sie  von  hinten  her  verfolgend  nachjagen" ¥.57.29;  —  y&  *ava  ^xbayats  avaähe vyqsca  vyanasca  apatse  (sd.)  zbayeitt vyqs  apagaße  vyänS  "welche  beide  um Hilfe  rufen  der  Verfolger  un
mit  apa  'wegjagen  von  — '  {haca  mit Abi) :  apa  dlm  adäi  vyeiti  trayaahal  hala vourukasät  Yt.  Ä  23.
mit  aipi  'verfolgen,  heijagen  hinter  — ' (Akk.) :  mihr»m  .,yS.,  avarvhi  Alf  api- vaHi^i  bafvart  ypnqnä  nisirinaoiti  "der., hinter  ihnen,  den  wehrlosen  herjagt,  zehn- tausend Sch^ge  austeilt"  Ytio.  37.
```


## [2026-10-16T05:14:40.721Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(d['KLN']['page_offset']); print(d['KLN'].get('lookup_hint','')[:400]); print(json.dumps(d['BQT'],ensure_ascii=False)[700:2500]); print(json.dumps(d['ZAP'],ensure_ascii=False)[700:1200])\"",
 "description": "KLN, BQT, ZAP offsets"
}
```


### [2026-10-16T05:14:41.030Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
om (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)", "/home/sfmqrb/
 "lookup_hint": "Chapters on Pahlavi words (e.g. 'Iranian Studies' terms); footnotes numbered per page.", "notes": "Built from djvu.xml."}
```


## [2026-10-16T05:14:43.248Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^virile,\\|^virtue,\\|^violent,\\|^violate,\\|^world,\\|^vim,' KLN_1966.txt | head; ",
 "description": "Klein headwords"
}
```


### [2026-10-16T05:14:43.567Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:14:45.798Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^ *virile\\|^ *virtue\\|^ *violent\\b\\|^ *violate\\|^ *world\\b\\|^ *vim\\b' KLN_1966.txt | head -20",
 "description": "Klein headwords looser"
}
```


### [2026-10-16T05:14:46.171Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:14:48.945Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'virile\\|virtus' KLN_1966.txt | head -10; grep -c . KLN_1966.txt; awk 'BEGIN{RS=\"\\f\"} NR>=868 && NR<=871 {print NR\": \"substr($0,1,200)}' KLN_1966.txt",
 "description": "Locate Klein virile and page 1714 leaf"
}
```


### [2026-10-16T05:14:49.543Z] TOOL RESULT

```
2713:andro-,  before  a  vowel  andr-,  combining  form meaning  ‘man’.  —  Gk.  avSpo-,  avSp-,  fr.  avfjp, gen.  avSpfS?,  ‘man’,  which  is  cogn.  with  OI. ndram  (acc.),  ‘man’,  naryah,  ‘virile’,  Arm.  ayr, gen.-dat.  arn,  ‘man’,  Alb.  n'er,  ‘man’,  Umbr. nerus  (pi.  acc.),  ‘men’,  Sabine-L.  Nerd,  PN.,  lit. ‘strong’,  W.  ner,  ‘hero’,  OIr.  nert,  W.,  Co.  nerth, ‘virility’.  Cp.  Andrew,  Andrias,  andron,  dandy, ‘a  fop’,  and  the  second  element  in  Alexander, Ardhanari,  Dianira,  Leander,  philander,  sundari. Cp.  also  the  first  element  in  anthropo-. androcracy,  n.,  rule  or  supremacy  of  men.  — Compounded  of  andro-  and  -xpaxla,  fr.  xpdxoc;, ‘strength,  power,  rule’.  See  -cracy. androecium,  n.,  the  stamens  of  a  flower  taken collectively  (hot.)  ■ —  ModL.,  compounded  of andro-  and  Gk.  oExtov,  dimin.  of  olxog,  ‘house’. See  economy.
6984:centumvir,  n.,  one  of  a  court  of  one  hundred  jud¬ ges  or  jurors  (Roman  hist.)  —  L.,  compounded of  centum,  ‘a  hundred’,  and  v/r,  ‘man’.  See  cent, ‘a  hundred’,  and  virile.
9961:curia,  n.,  i)  the  Roman  senate;  2)  a  court;  3)  the papal  court.  —  L.  curia,  ‘one  of  the  thirty  parts, into  which  the  Roman  people  was  divided  (ten for  each  of  the  three  tribes);  the  senate  house; the  senate’,  in  ML.,  ‘court’,  prob.  for  *co-'ciria, hence  literally  meaning  ‘community  of  men’,  fr. co-  and  vi'r,  ‘men’.  See  virile  and  cp.  Quirites,cry. curial,  adj.,  pertaining  to  a  curia.  —  L.  curialis, ‘pertaining  to  a  curia’,  fr.  curia.  See  curia  and adj.  suff.  -al.
10486:December,  n.  — •  L.  December,  ‘the  tenth  month’, fr.  decern,  ‘ten’  (see  decern-);  so  called  because the  Roman  year  began  with  March. Derivatives:  December-ish,  adj.,  December-ly, adj.,  Decembr-ist,  n.  (Russ,  hist.) decemvir,  n.,  i)  a  member  of  a  council  of  ten  men (Roman  hist.) ;  2)  a  member  of  an  authoritative body  of  ten  men.  —  L.,  back  formation  fr.  the pi.  decern  viri,  ‘ten  men.’  See  decern-  and  virile and  cp.  duumvir,  triumvir,  centumvir. decemviral,  adj.  —  L.  decemviralis,  ‘pertaining  to the  decemvir(s)’,  fr.  decern  viri.  See  prec.  word and  adj.  suff.  -al.
12488:Derivatives:  dutiable  (q.v.),  duti-ful,  adj.,  duti- ful-ly,  adv.,  duti-ful-ness,  n. duumvir,  n.,  one  of  two  officials  having  the  same public  function.  —  L.,  name  of  various  magis¬ trates;  back  formation  from  the  archaic  gen. pi.  duum  virum,  ‘(one)  of  the  two  men’.  See  dual and  virile  and  cp.  triumvir,  decemvir, duumviral,  adj.  —  L.  duumviralis,  ‘pertaining  to the  duumvirs’,  formed  fr.  prec.  word  with  suff. -alis  (see  adj.  suff.  -al).
13894:evirate,  tr.  v.,  to  castrate.  —  L.  eviratus,  pp.  of evi 'rare,  ‘to  deprive  of  manhood’,  fr.  e-  and  vir, ‘man’.  See  virile  and  verbal  suff.  -ate. eviration,  n.,  castration.  —  L.  evirdtio,  gen.  -onis,
14577:with  L.  vir ,  ‘man’ ;  see  virile.  The  second  element derives  fr.  Celtic  *gustu-,  ‘choice’,  fr.  I.-E.  base *geus-,  *gus-,  ‘to  taste’;  see  choose, fergusonite,  n.,  a  niobate  and  tantalate  of  yt¬ trium,  erbium  etc.  {mineral.)  —  Named  after Robert  Ferguson  (1799-1865),  of  Raith  (Scot¬ land).  For  the  ending  see  subst.  suff.  -ite. feria,  n.  (pi.  feriae),  1)  pl„  feast  days,  holidays ; 2)  {eccles.)  a  weekday.  —  Late  L.  feriae  (pi.), ‘days  of  rest,  holidays,  festivals’,  fr.  OL.  fesiae (see  rhotacism),  rel.  to  festus,  ‘solemn,  festive, festal’,  fanum,  ‘temple’.  See  fair,  n.,  and  cp. words  there  referred  to.
31455:—  Curis,  a  name  which  possibly  derives  from  the contraction  of  *co-w iriom,  ‘the  whole  of  citi¬ zens’,  fr.  co-,  ‘together’,  and  vir,  gen.  viri,  ‘man’. See  co-  and  virile  and  cp.  Quirinal,  Quirinus.  Cp. also  cry.
34622:septemvir,  n.,  one  of  seven  men  associated  in  some office  or  authority  ( Roman  hist.)  —  L.  septem- viri  (pi.),  compounded  of  septem-  and  viri,  pi.  of vir,  ‘man’.  See  virile.
37460:sundari,  n.,  name  of  an  East  Indian  tree  ( Heritiera fomes)  —  OI.  sundari,  lit.  ‘beautiful’,  fern,  of sundarah,  a  later  form  corresponding  to  Vedic siinarah,  ‘of  full  vitality’  (cp.  Avestic  hunara-,  of s.m.),  formed  fr.  I.-E.  pref.  *su-,  ‘well,  good, beautiful',  and  base  *ner-,  ‘vital  energy,  vigor'. I.-E.  *su-  appears  also  in  Gk.  u-  in  u-Yir,c, ‘healthy’;  see  hygiene.  I.-E.  *ner-  occurs  also  in OI.  naryab,  ‘virile’,  Gk.  a-vv)p,  ‘man’;  see andro-.
41263
868:  Compounded  of  trachelo-  and  Gk. -xopia,  ‘a  cutting  of’,  fr.  xoprj,  ‘a  cutting’.  See -tomy.
tracheo-,  before  a  vowel  trache-,  combining  form denoting  the  trachea.  —  See  trachea.
869: ain. Cp.  also  trail.
Derivatives:  train,  n.  (q.v.),  train-age,  n.,  train¬ ed,  adj.,  train-ing,  n.  and  adj. train,  n.,  procession,  cortege,  etc.;  a  series,  a  line of  connected  ra
870: L.  transfor- matus,  pp.  of  transformdre.  See  prec.  word  and -ation.
Derivative:  transformation-al,  adj., transformative,  adj.  —  ML.  transformations,  fr. L.  transformatus,  pp.  of  tra
871: ,  v.,  and  -ation  and cp.  L.  transportatio,  gen.  -dnis,  ‘migration’. Derivatives:  transportation-al,  adj. transposal,  n.,  transposition.  —  See  next  word and  subst  suff.  -al.
transpo
```


## [2026-10-16T05:14:52.708Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for i in 868 869 870 871 872 873 874; do awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | grep -o -i 'virile,  adj.\\{0,900\\}\\|violent,  adj.\\{0,500\\}\\|virtue,  n.\\{0,500\\}\\|world,  n.\\{0,600\\}' | sed \"s/^/leaf$i: /\"; done",
 "description": "Find Klein entries near p.1714"
}
```


### [2026-10-16T05:14:53.395Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:14:56.452Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /virile,|virile, *adj/ {print NR}' KLN_1966.txt | head; grep -n -o 'virile,  adj.\\{0,1200\\}' KLN_1966.txt | head -3; grep -n -o 'violent,  adj.\\{0,500\\}' KLN_1966.txt|head -2; grep -n -o 'virtue,  n.\\{0,400\\}' KLN_1966.txt|head -2; grep -n -o 'world,  n.\\{0,700\\}' KLN_1966.txt|head -2",
 "description": "Klein virile/violent/virtue/world"
}
```


### [2026-10-16T05:14:56.942Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:14:59.612Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o 'virile, .\\{0,1000\\}' KLN_1966.txt | head -3; grep -n -o 'violent, .\\{0,400\\}' KLN_1966.txt|head -2; grep -n -o 'virtue, .\\{0,400\\}' KLN_1966.txt|head -2; grep -n -o '^world, .\\{0,700\\}\\| world, n.\\{0,700\\}' KLN_1966.txt|head -2",
 "description": "Klein entries different spacing"
}
```


### [2026-10-16T05:14:59.978Z] TOOL RESULT

```
5615:violent,  passionate’.  Arm. albeur  (gen.  aiber),  ‘source’,  Gk.  <pop6veiv, tpopuoaew,  ‘to  knead  together,  soil,  bespatter’, <pp(ap  (gen.  <ppeaxo<;),  ‘well,  spring’  Thracian Gk.  PpOxoc  (fjpouxoi;  in  Hesychius),  ppuxov.
15361:violent,  impetuous,  bold’, whence  also  W.  rhewidd  (for  *pragio-),  ‘lasci¬ viousness’,  Pol.  pragnqc,  ‘to  crave  for’.  Cp. fresh,  obtrusive’.
12150:virtue,  happiness’,  OHG.  tu- gundi,  ‘ability’,  MHG.  tugent,  ‘skill,  worthiness, virtue’,  G.  Tugend,  ‘virtue’,  and  cogn.  with  Gk. xeuyeiv,  ‘to  make  ready’,  -ruyyavstv,  ‘to  hap¬ pen,  be  at  a  place’,  teO/ch;,  ‘tool,  implement’, later  ‘book’,  Tuyy,  ‘fortune,  fate,  providence’, Hitt,  tukka-,  ‘to  fall  to  a  person’s  share’,  Ir. dual  (for  *dhughlo-),  ‘becoming,  fit’,
```


## [2026-10-16T05:15:04.540Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} END{print NR}' KLN_1966.txt; awk 'BEGIN{RS=\"\\f\"} {if ($0 ~ /virile/) print NR}' KLN_1966.txt | tail -3; grep -n -o 'virile, adj.\\{0,1000\\}' KLN_1971.txt | head -2; grep -n -o 'violent, adj.\\{0,500\\}' KLN_1971.txt | head -2; grep -n -o 'virtue, n.\\{0,400\\}' KLN_1971.txt|head -2; grep -n -o 'world, n.\\{0,700\\}' KLN_1971.txt|head -2",
 "description": "Check Klein files coverage"
}
```


### [2026-10-16T05:15:05.063Z] TOOL RESULT

```
903
819
878
888
262655:virile, adj., manly; masculine. F. viril, fr. L. 
262468:violent, adj. — ME., fr. MF. ( = F.), fr. L. violen- 
262712:virtue, n. — ME. vertu, virtu , fr. OF. (= F.) vertu, 
268320:world, n. — ME. weoreld, weorld, fr. OE. weo-
```


## [2026-10-16T05:15:07.656Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '262455,262480p;262655,262680p;262712,262720p;268320,268335p' KLN_1971.txt; awk 'BEGIN{RS=\"\\f\"} NR==879' KLN_1966.txt | grep -o '.\\{200\\}virile.\\{600\\}' | head -2",
 "description": "Read Klein 1971 entries"
}
```


### [2026-10-16T05:15:08.543Z] TOOL RESULT

```
Derivatives: violation (q.v.), violat-ive , adj., 
violator (q.v.) 

violation, n. — ME. violacion, fr. L. violdtio, gen. 
-onis, fr. violates, pp. of violare. See prec. word 
and -ion. 

Derivative: violation-al, adj. 
violator, n. — L. violator , fr. violate, pp. of vio- 
lare. See violate and agential suff. -or. 
violence, n. — ME., fr. OF. (= F.), fr. L. violen- 
tia , fr. violentus. See next word and suff. -ce. 
violent, adj. — ME., fr. MF. ( = F.), fr. L. violen- 
tus, ‘forcible, vehement, violent’, which is rel. to 
violare, ‘to treat with violence’. See violate. 
Derivatives: violently, adv., violent-ness, n. 
violescent, adj., tending to a violet color. — 



Formed fr. viola with suff. -escent. 
violet, n. — ME., fr. MF. violete (F. violette ), fr. 
OF., dimin. of viole, fr. L. viola , which is prob. 
a Mediterranean loan word; cp. Viola. Cp. also 
iolite. For the ending see suff. -et. 
virile, adj., manly; masculine. F. viril, fr. L. 
virilis, ‘pertaining to a man, masculine, manly, 
vigorous, spirited’, which is rel. to Umbr. viro , 
veiro, ‘the men’ (acc.), and cogn. with 01. virdh, 
Avestic vira-y Toch. wir, Lith. vfras, Lett, vtrs, 
OPruss. wars, Goth, wair, OHG., OS. wer, ON. 
verr t OE. wer, OIr. fer , W. gwr, ‘man’. These 
words prob, meant orig. ‘the strong one’, and 
derive fr. I.-E. base *wi-ro-, enlargement of base 
*wei-, ‘to be strong’, whence L. vis, ‘strength, 
force, vigor’. See vis and -ile and cp. duumvir, 
triumvir, septemvir, decemvir, centumvir, cry, 
curia, evirate, Fergus, Quirites, virtue, werewolf, 
world. 

virilescence, n. — Formed from next word with 
suff. -ce. 

virilescent, adj., tending to acquire characters of 
the male. — Formed fr. L. virilis (see virile) with 
suff. -escent. 

virility, n., the age of manhood; masculinity. — 
F. vir Hite, fr. L. virilitatem, acc. of virilitds, ‘the 
age of manhood’, fr. virilis. See virile and -ity. 
virology, n., that branch of science which deals 
virtue, n. — ME. vertu, virtu , fr. OF. (= F.) vertu, 
fr. L. virtutem , acc. of virtus, ‘virtue’, lit. ‘man- 
liness, manhood’, fr. vir. See virile, 
virtuosity, n. — Formed fr. virtuoso with suff. 
-ity. 

virtuoso, n., a person skilled in one of the fine arts, 
esp. in music. — It., fr. Late L. virtuosus. See 
next word. 
world, n. — ME. weoreld, weorld, fr. OE. weo- 
ruld, woruld, ‘world, age’, related to OS. werold, 
ON. verold, Swed. verld, Dan. verden, OFris. 
war Id, wrald , Du. wereld , OHG. weralt, worolt , 
MHG. werelt , werlt, welt, G. Welt. The first 
element of these compound words is rel. to OE. 
wer, etc., ‘man’; see virile. The second element 
is rel. to ON. old, ‘mankind’, aldr , ‘age’, OE. 
ieldu, Goth, aids, ‘age’, and to OE. aid, ‘old’ ; see 
old. Accordingly OE. weoruld, etc., lit. mean ‘the 
age of man’. 

Derivatives; world-ish , adj., world-ling, n., 
world-ly, adj. 

worm, n. — ME. werm, worm , wurm, fr. OE.
```


## [2026-10-16T05:15:12.711Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==879' KLN_1966.txt | head -c 600; echo; awk 'BEGIN{RS=\"\\f\"} NR==879' KLN_1966.txt | grep -o '1[67][0-9][0-9]' | head",
 "description": "Klein 1966 leaf with virile"
}
```


### [2026-10-16T05:15:13.124Z] TOOL RESULT

```
T),  ‘tongue  of  the  balance,  balance  ,  orig.
‘the  hole  in  which  the  tongue  of  the  balance moves  about’,  which  stands  for  *tru-t  na  and  is rel.  to  xpuctv,  ‘to  rub,  wear  out ,  xpup-oc,  hole  , Teipstv  (for  *xeptat.v),  ‘to  rub,  wear  away’,  fr. I.-E.  base  *ter-,  ‘to  rub,  to  rub  by  turning,  to turn,  to  twist;  to  pierce’.  See  throw  and  cp. words  there  referred  to.
troop,  n.  —  MF.  (=  F.)  troupe,  fr.  OF.  trope,  fr. Late  L.  troppus,  ‘herd’,  fr.  Frankish  *l>rop,  meta.- thesis  of  *porp,  ‘crowd,  gathering
1707
1657
```


## [2026-10-16T05:15:17.727Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in BQT:262 BQT:334 BQT:2298; do echo \"=== $p\"; timeout 300 python3 tools/ref_page.py $p --image 2>&1 | head -80; done",
 "description": "Fetch cited Borhan pages via ref_page tool",
 "timeout": 600000
}
```


### [2026-10-16T05:15:25.323Z] TOOL RESULT

```
=== BQT:262
no scan of BQT covers printed page 262 (see 'scans' in refs_online.json)
=== BQT:334
no scan of BQT covers printed page 334 (see 'scans' in refs_online.json)
=== BQT:2298
(no exact page map; using offset -1917 -> pdf page 381; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2298.png
REF: BQT:2298  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 381  OCR-lang: fas

وبدايك -م۷۹۸-<
وهویدا وظاهرهم آمده است ‎٩‏ - ودرد والم‌وآ زار وعلاج کردن باشد ؛ و بفتح اول هم‌آمده است.
را نیز کویند ؛ و باین معنی بقتح اول‌هم کمته‌اند ویده ؟۴ - بنتم‌اول بروزن‌میده. بعمنی
و اسح این است . چاره جسته و چاره جوبنده باشد ؛ ویکسراولهم

وبدانك ه با اول بثالی مجهول‌رسشده آمده است.

و دال بالف کشیده وفتح نون وسکون‌کاف,بمعنی وید یدن « بنتح اول بروزن کردیدن,
کاری و چیزی بهم ناپیوسته باشد و آنرا بعری بممنی گم شدن وناپدید گشتن ونقصان کردن* -
طفره و درهندوستان باغه کوبند . وچاره وعلاج جتن باشد ‎٩‏ .

و پدستر ؟ -« با تای قرغت بروزن بی ور ۷ » بکراول بروزن میر ؛ بهعنی
لشکر . نام حیوانی است بحری و در خشکی‌هم | از بر است که ازحفظ کردن و بخاطرنگاهداغتن
میباشد وخصبهٌ او راآش بچگان کوبند . باشد ۸ - و بمه‌نی‌فهم وهوش و ادرادعم‌هت۹-

ویدن ۴ بروزن دیدن , چاره جتن | و نله و فرباد را نیز کویند *۱- و نام دجی‌است

۱ -فی : هوبدا. ۴ *<بیدستر (ه.م.) وارك : رشیدی .
۴ -ر4 : وبدیدن . ۴ - ر4 : ویدن» وبدیدن ۰
8 - رك : وید , وندا. ۹« ویدیدن ( بفتح واو و سکون هردو با ) چاره
جستن » وبدیده چاره جستّه .» ۸ رشیدی» « موْبدالفسلاء » و رك : ویدن » ویده .۰
۷ *بیر (هم.) * بر(ه.م.) » قن : وبرا (۸.م.) اوستایی -5۷178 (هوش) «دارمتش.
تبعات ج ۲ ص ۱۸۳ ؛ پپلوی ۷1۲ ۰ ۷۸72۴ (وبرا ) »کردی 1۳ظ ( حافظه ) » بلوچی 817۲
( حافظه , تذکار ) * اسدق ۱۶۸۹ . رك : بیر.- ولف *وبر» را درشاهنامه بمعمنی هوش وحافظه
آورده: اورامانی۷۷1۳ (باد . حافظه) «ک4 . اورامان. ۶۱۲۷ » دراراك (-لطان؟ باد)8154 ۷1۳-02
( نظرم لیست » فراموش کرده‌ام ) « مکی‌نژاد > .
۸ - چه افتاد ای عزیزان مر شما را که شد یکبارتان پاد من از ور.
مجد همگر « رشیدی >.
‎٩‏ کی راکه کمتر بدی خط و ون نرفتی بدبوان شاه اردشین .
فردوسی طوسی « شاهنامةٌ بخ ج ۷ص ۰۱۹۸۲
زین بدکنش حذر کن وزین پس دروغ او
منیوش اگر بهوش و صیری وتیزویر .
2 ناصرخرو بلخی . دبوان ص ۱۵۷ *.
۰ اسم صوت : « با وبلنا اناکنا ظالمین ۰ أی وای و وبرما » ما بودیم ستمکاران که
فرمان خدای لکردیم .» « تفسی ر کمبریج ورق ۳۷ 8 ۰ ]. ۲۱؛ سورة ]2536 آية 4۸ > لیز ورق
۹ ۹3 رك : براون . تفسیرص4۹۲ وقس: تهرانی۷1۳ ۵ 1۳[ (داد وفرپاد) :
ای جوان زیر چرخ پیر مباش یا ز دورانش در زحیر مباش
با برون شوزچرح چون «ردان ورنه با وای وای و ویر مباش.
سنائی غزلوی « جهانگیری >.
رشیدی : و رنه با وا ووی و ویر مپائي ؛ فرهنگه نظام : ورنه با ای وای و ویر مباش .
(پرهاي فاطع ۲۹۰)
```


## [2026-10-16T05:15:32.408Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -c 600 BQT_v1_pages.txt; echo; grep -n 'pdf page' BQT_v1_pages.txt | head -3; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(d['BQT'].get('page_offset'))\"",
 "description": "Inspect BQT vol1 page file format"
}
```


### [2026-10-16T05:15:32.744Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
م و اس مر هر وه او
7 رین خلت ریز یتایب بره ات
لف‌بال ۶۲ .یرک
ا اند کل داي رشب , رمع
فان تا تا
رن 9 3
کرحم تن
اد شش مرا
مو رم | مر
وک رهب اه نات مج
لش
وان روکد ور
۱ و
طراول ؛ | ع اس
چاپ دوم فروردین ۱۳۴۳
با تجدید نظر کامل
بسرمایه کنابفروشی ابن سینا - تپر اناداره کل دک زون.
شماره ۷9 9 ۳
بر
5
‌ ۰ م�
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
```


## [2026-10-16T05:15:35.592Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 481 482 483 553 554 555 556; do echo \"=== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | grep -n 'برم\\|بیر\\|vīr\\|vir\\|varm\\|warm\\|حافظ\\|ویر' | head -12; done",
 "description": "Search Borhan vol1 leaves near pp.262 and 334"
}
```


### [2026-10-16T05:15:36.402Z] TOOL RESULT

```
=== leaf 481
=== leaf 482
20:رما کردن - بمتیبرمال زدناست
22:برمالیدن بروزن سرخار دن».سنی
25:برماه بر وذن درگاه » افزارست
30:برمایون ۱ - بکر اول بایای حطی
34:بمعنی برمایون است و آن‌گاوی بود که‌فریدون
60:۴ لکلرك‌برم‌را ۱۷:0۵0966
62:۸ - رك : برهوز وبرمو.
=== leaf 483
15:فرمود تا او را از مجلس بیرون بردند . خواص
26:آنکه در هنگام شدت‌الم برمکم. لهنا او مرك
27:و اولاد او ببرمکی ملقب و مشهور شدتد .
41:بودابی بوده و برمکیان تولیت آن ممبد و در اراشی وسیم وموقوفات بیار متعلق بدیر » رماست
47:8 میباشد . واضح است که امتممال کلمهٌ سانسکربت ۳۲2101118112 مربوط ببرمك
52:«البرموك . سادن‌النوبهار (درهتن مزبور : البوبپار (مکرر) » ؛ ركث مزدسنا ص ۳۷۵.
53:۴ رك: برمز. ۴ - و نیز برمونه در د اثیر بممنی شینی است «فرهنشکه دساثیر ۰۲۳۹
=== leaf 553
=== leaf 554
36:ثبر ان « بروزن ومعنی ویران باش دکه
38:یر انه « بروزن ومعنی ویرانه است که
63:ف .2۲ (: - شش ( چاه) . و۲ و فان : ۵ د رظ : ویرالد .
=== leaf 555
11:بیر گند ب یفتح کاف فارسی بروزن
17:بیرون است که تقض اندرون باشد 8
43:۵ رك: بیرون.
46:برای شهر بیرجند آب تهیه
48:چونکه بیرنگی اسیر رنگگ شد
=== leaf 556
1:بیرونآحدن
2:بیرون آ هلان - سسروف است که
```


## [2026-10-16T05:15:40.361Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==483' BQT_v1_pages.txt | sed -n '1,20p;50,70p'; echo =====; awk 'BEGIN{RS=\"\\f\"} NR==554' BQT_v1_pages.txt | grep -n 'بیر\\|حافظه\\|هوش' | head",
 "description": "Print Borhan leaf ~p.262"
}
```


### [2026-10-16T05:15:40.707Z] TOOL RESULT

```
Exit code 1
باقاف فارسی هم آمده است- و بکر انی‌طایفه‌ای
بر لنگار دن ع کنابهاز کریختن‌باشد.
بر ۵ - بفتح اول و ثانی بر وزن عجم .
چوب بندیر! کوبند که ناك انگور و بیارهٌ کدو
وخیار و امثالآن بربالایش اندازند ۱ - وعربی
بمعتی ملول شدن وبستوهآمدن باشد -و کیکه
در مجلی قمفر نشیند و بازی نکند - و میوه
درخت خاردار را کویند عموما . و بعضی گویند
شکوفه و بهار درخت مفیلان است و آن‌درقوت
و منففت مانند بد مك است ؟ - و سکون
و لاب واستخر و چشمةٌ آب را نیز کوبند ۴ -
و بمعنی اتظار هم آمده است - و مرغ را نیز
۱
و اه و وست کی بائد ۴ .
بر ماسیدن عبمعنی وین
مالیدن و سودن عنوی باشد برعضو دیگر .
بر مال - دروزت ابدال 1 سینه وسرابالای
کوه و بنخه باشد - و گوز را نز گویند که از
مخت ات و آهر حر گرختن ح هست هنی
رما کردن - بمتیبرمال زدناست
باشد - و امیدوار شدترا نیز کویند - و به‌عنی
زنور عل هم‌آهده است۸ ۰
بر مقار - با غن نقطه‌دار بروزن چمحد
ماز » 2 کردانه را گویند ۲ اه زر اصت انداله
که بمد از اجرت استاد برسم انعام‌بشا گرد دهند.
بر مغازه - بنتحزای‌هوز, بمعنی مر مغاز
اس ت که شا گردانه باشد .
داتیته * لك ۱ص 4۲۱ ۳
ی نت رل : عبر ماسدن .
*یوستی .بندهشص ٩۸۷‏ .
۴ لکلرك‌برم‌را ۱۷:0۵0966
ب پپلوی 9۲602/۷18
۸ - رك : برهوز وبرمو.
(eval):1: ==== not found
```


## [2026-10-16T05:15:46.496Z] TOOL CALL #38: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p533; cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p533; for n in 482 553 554; do curl -sL -o bqt533-n$n.jpg \"https://archive.org/download/borhan-ghate-v1/page/n${n}_w1200.jpg\"; done; file bqt533-*",
 "description": "Download Borhan vol1 leaf images"
}
```


### [2026-10-16T05:15:50.593Z] TOOL RESULT

```
bqt533-n482.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1240x1754, components 1
bqt533-n553.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1240x1754, components 1
bqt533-n554.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1240x1754, components 1
```


## [2026-10-16T05:15:52.592Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p533/bqt533-n482.jpg"
}
```


### [2026-10-16T05:15:52.608Z] TOOL RESULT

```

```


## [2026-10-16T05:15:57.247Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p533/bqt533-n554.jpg"
}
```


### [2026-10-16T05:15:57.335Z] TOOL RESULT

```

```


## [2026-10-16T05:16:02.688Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; ls ocr/BQT | head; grep -n -i 'varm\\|warm\\b\\|vīr\\b\\|vir\\b\\|wīr' ZAP.txt | head -20",
 "description": "Grep Bailey ZAP for vir/varm"
}
```


### [2026-10-16T05:16:03.102Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--  368k sfmqrb 14 Oct 22:19  0001.png
.rw-r--r--  1.7k sfmqrb 14 Oct 22:19  0001.txt
.rw-r--r--  534k sfmqrb 14 Oct 22:19  0049.png
.rw-r--r--  2.7k sfmqrb 14 Oct 22:19  0049.txt
.rw-r--r--  190k sfmqrb 14 Oct 22:30  0143.jpg
.rw-r--r--   576 sfmqrb 14 Oct 22:30  0143.vision.txt
.rw-r--r--  472k sfmqrb 14 Oct 22:45  0339.jpg
.rw-r--r--   849 sfmqrb 14 Oct 22:45  0339.vision.txt
.rw-r--r--  221k sfmqrb 16 Oct 01:15  0342.jpg
778:aSd varmte tat -j^aQYam mananho
802:gaosurabyo •tfar.md pairi .varma- the good things with wealth in
1071:or great prosperity', and mx Varm °' da-, x v ar9nazda- used of Mithra
4285:warm to the joy of cattle and
4853:adunnica vir hos x ar ^ ddnasni boi
4884:vir, os, and yrat with the statement of their activity vlr nerok
4912:u vir ix v dstdr aflaspdrddr
4926:2 Dd 2. 13 vir i ayapak, but SGV 5. 82 ddnaZni i ayafid.
4928:Cf. GrBd 190. 13 f. 0/ ut vir ut marisn ut handeHsn ddniSn ut usvdriht.
4939:(DkM 50. 8). Cf. also SGV 5. 5 hos i agunast u vir i tafaa u
4982:to derive varom from *varma- to the base var- 'choose' as ddrmak from dar-
4985:ut vir ut torn manist andar tan cegon 'What is the place of man's
7703:4 The physician, too, who is varm-rtipek, has his books by heart, is commended
7708:vdcakthd [vdcihd] varm-naskihd
7735:ut zand varm 'one who had memorized the whole Apastdk and
7737:apastak apdk zand varm. Of the sisters of Artay Viraz, devout
7738:Zoroastrians (AVn 2. 3), it is said ut-san den varm utyast kart estdt
7754:venisn varm apastdk ut vicltdr
7757:Similarly in the Pahlavi Rivayat p. 50, 1. 1 1 ke-sgdsan ne varm kart
7758:'who has not memorized the gathas', and p. 43, 1. 11 zand varm
```


## [2026-10-16T05:16:05.153Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '4970,4995p;7695,7712p' ZAP.txt",
 "description": "Read Bailey ZAP on vir and varm"
}
```


### [2026-10-16T05:16:05.454Z] TOOL RESULT

```
the brain. First the mind is
mixed with the marrow of the
finger of man's hands and its
seat and position is in the heart
and its abode is in the whole
body as the form of the foot is
within the shoe.
1 So in DkM 25. ii, 19; 348. 14; Pahl. Texts, p. 130, § 13; Pahl- R^- Dd >
p. 135. 28, ZKA 259. 8. In Pahl. Texts, p. 144, § 4, we have gukdret hen andar
varom f^e/'he digests vengeance in his mind'. It does not occur in the Bunda-
hisn. Pagliaro, Rivista indo-greco-italica, 1929, 63 ff., considers it as taken from
Av. vdrzma 'at will', as Bartholomae, ZAIW 222, had done. But it is preferable
to derive varom from *varma- to the base var- 'choose' as ddrmak from dar-
as proposed in JRAS, 1934, 511.104 MARTOM
This is the answer to the question asked in 47. 2 martoman 6s
ut vir ut torn manist andar tan cegon 'What is the place of man's
memory, mind, and seed in the body V It is probably some error
of reading which has given in the Pazand rua manastan (copied in
Skt. atmanasca sannivaso) in place of ut-as manist. The ruvan
does not belong to the question.
The second further statement is that in GrBd 196. 2 f., where
it is taught that each member of the body is presided over by
Ohrmazd and the Amahraspands. Ohrmazd is president of the jan:
jan (ut) hart) rosnth apdk jan os ut
boh ut apdrik hot en mar ohrmazd
x v es
first incorruptibility,
second niceness in thoughts, words,
and deeds,
third to hold as a dastafiar him
1 DkM 857. 18 = SBE 37. 278.
3 DkM 653. 13 = SBE 47. 88.
3 See A. Christensen, Ulran sous les Sassanides, 410 ff., and 'Om den his-
toriske romanlitteratur paa Pehlevi' in Studier tilegnede Fronts Buhl, 1925.
4 The physician, too, who is varm-rtipek, has his books by heart, is commended
in DkM 161. 9.
idanaktar i rdst-gofSisntar ke den-
dkdsihd dmd\tet ut rdstthd dmocet
Zaharom yazisn i yazddn rdst-
vdcakthd [vdcihd] varm-naskihd
pat nirang yastan
pancom rocdn sapdn sndyismhd
andar yfeskdrih estdtan apdk
X v eS hamestdr ko-^sisn kartan zi~
```


## [2026-10-16T05:16:10.467Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '4878,4890p;4920,4945p' ZAP.txt",
 "description": "Bailey vir context"
}
```


### [2026-10-16T05:16:10.765Z] TOOL RESULT

```
'senses' in DkM 48. 21 venisn asnavisn casish hanboSisn ut ptr-
mayim 1 'sight, hearing, taste, smell, touch', admitting only five
senses as Aristotle had done {^repl faxi* A 2 A b). The instruments
are dil casm gos uzvan dast pad 'heart, eye, ear, tongue, hand,
foot'.
In reference to the mind we have in the Denkart 48. 10 ff. bo8,
vir, os, and yrat with the statement of their activity vlr nerok
X v astar ut aydftdr 2 os oz dastar ut *pdtdr, xrat 3 zor nikiritar viclnkar
ut karlkenltdr hast I danisn 'the power of the vlr is to seek and
acquire, of the os to maintain and protect, of the xrat to observe
and decide and set in motion, that is knowledge'. These are the
three faculties of mind recognized by Aristotle avd}ivT)uis 'recol-
lection', fivTjfiT] 'memory', and vovs 'understanding*.
treasurer and watcher, and the
DkM 586. 11 hanboSisn, 162. 18 hanboUsnth 'smell' to baud-, cf. Mid.Parth.
ptc. 'mbwy'd 'kissed, embraced', Armenian hamboyr 'kiss* (Ghilain, Essai sur la
langue parthe, p. 65). Of ifi}*»4^0 ptrmdyisn the reading is uncertain: the
Pazand (SGV) has padarmdisni. Zatspram 30. 25 has venakih ut asna<^)akih
ut kanbdSdkih ut cas\a)kih which are andar mazg <f> sar 'in the brain'.
2 Dd 2. 13 vir i ayapak, but SGV 5. 82 ddnaZni i ayafid.
3 Dd 36, 19 an i vicingar -xrat.
Cf. GrBd 190. 13 f. 0/ ut vir ut marisn ut handeHsn ddniSn ut usvdriht.
W:
I * v .
MARTOM 103
u boi iy v at vindi i rvq boZ which is itself the vision of
frava! i x"*$ & har ddltdr i tan the ruvan and the fravahr which
ninth iaf&kaa is the cihr-maintainer of the
M afiarv mainyvq. i tan-d&tar body, and the ax v undefiled and
the other invisible agents main-
taining the body.
These are the janlk ut tanik afizar 'instruments of jan and body*
(DkM 50. 8). Cf. also SGV 5. 5 hos i agunast u vir i tafaa u
xard i vazlndd 'with pure memory, keen recollection, and dis-
criminating understanding' (in the Sanskrit smrtya anavilayd
caitanyena ca ttvratarena buddhyd ca viviktayd).
We need here only mention the varom 1 'mind' and dsn xrat and
gososrut xrat, the two last from the Avesta.
Two further opinions have still to be noticed. The place of the
```


## [2026-10-16T05:16:14.837Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /tmp; for t in 'ویر' 'بر' 'Reconstruction:Proto-Indo-European/wiHrós' 'Reconstruction:Proto-Indo-European/weyh₁-' 'violo' 'world' 'virtus' 'vīra' 'Reconstruction:Proto-Iranian/wiHráh'; do echo \"=== $t\"; curl -s -G 'https://en.wiktionary.org/w/index.php' --data-urlencode \"title=$t\" --data-urlencode action=raw | grep -A6 -i '===Etymology' | head -40; done 2>&1 | head -200",
 "description": "Fetch Wiktionary etymology sections"
}
```


### [2026-10-16T05:16:16.962Z] TOOL RESULT

```
=== ویر
===Etymology===
From {{inh|bqi|pal|tr=wyl|ts=wīr|sc=Phlv}}, from {{inh|bqi|ira-pro|*wiHr̥Háh|t=noun}}.

===Pronunciation===
* {{IPA|bqi|/vir/}}

===Noun===
--
===Etymology===
{{dercat|inh=3|ks|inc-pro|iir-pro|ine-pro}}
{{inh+|ks|sa|वीर|tr=vīrá}}.

===Noun===
{{ks-noun|ویٖر|g=m}}

--
===Etymology 1===
From {{inh|fa|pal|tr=wyl|ts=wīr|sc=Phlv}}, from {{inh|fa|ira-pro|*wiHr̥Háh|t=memory, mind}}.

====Noun====
{{fa-noun|cls=وِیر}}

# {{lb|fa|obsolete}} [[memory]]
--
===Etymology 2===
From earlier {{fa-l|وِیل|t=desire}}.

====Noun====
{{fa-noun|cls=وِیر}}

# {{lb|fa|somewhat|colloquial}} [[whim]]
--
===Etymology 1===
{{root|pa|sa|वीर}}
{{inh+|pa|pra|𑀯𑁂𑀭}}, from {{inh|pa|sa|वैर|tr=váira}}.{{ref|{{R:CDIAL|vaíra|12142|703}}}}

====Pronunciation====
* {{IPA|pa|[ʋɛːɾᵊ]|a=pa}}

--
=== بر
===Etymology 1===
{{ety|ar|:inh|sem-pro:*barr-|text=+}} 
{{ar-rootbox|ب ر ر}}

====Pronunciation 1====
{{ar-pr|بَرّ}}

--
===Etymology 2===

====Pronunciation====
{{ar-pr|بَرَّ}}

====Verb====
{{ar-verb form|+بار<I>}}
--
===Etymology 3===
[[File:Triticum turgidum L. Bajuwarenhof Kirchheim 2012-08-05.jpg|thumb|right|{{lang|ar|بُرّ}}|upright=1.25]]
Probably one of the words Yemenite expatriates picked up in the {{w|Byzantine Empire}}, from {{bor|ar|grc|πυρός}}, similar to {{m|ar|فِرْسِك|t=peach}}, if it is correct that one has to posit for {{der|ar|ine-pro|*péh₂wr̥}} a meaning “spelt”. Another word for spelt or dinkel wheat is borrowed from Ancient Greek: {{m|ar|خندريس|خَنْدَرُوس}}.

The similar {{cog|he|בָּר|tr=bār|t=grain, corn}} may be instead from the same derivation as the etymon of {{m|ar|بَزْر|t=seed}}. The similarity to {{cog|sla-pro|*bъrъ|t=foxtail millet}} is also likely a coincidence.

====Pronunciation====
--
===Etymology===
From {{inh|xbo|trk-pro|*bar-}}.

===Verb===
{{head|xbo|verb|tr=bar|head=بَر}}

# {{lb|xbo|Volga Bulgar}} to [[go]]
--
===Etymology===
{{bor+|gwt|fa|بر}}.

===Adverb===
{{head|gwt|adverb|g=|tr=bar}}

# [[without]] [[delay]], [[promptly]]
--
=== Reconstruction:Proto-Indo-European/wiHrós
===Etymology===
{{etymon|ine-pro|id=man|*weyh₁-<unc>|pos=word}}
Various theories have been posited:
* According to some, {{m|ine-pro|*wiHrós}} is derived from the verb {{m|ine-pro|*weyh₁-||to hunt}} (cf. Sanskrit {{m|sa|वेति|tr=véti}}, Lithuanian {{m|lt|výti}} etc.), which would render the reconstruction as {{m|ine-pro||*wih₁rós}} and the original meaning of "hunter".
* Also often derived from {{m|ine-pro|*wéyHs|t=force, strength}}.
* Perhaps related to {{m|ine-pro|*h₂weyd-}} (whence {{m|ine-pro|*h₂wéydr̥}}) via the Kortlandt effect, a proposed sound law whereby {{m|ine-pro||*d}} sometimes becomes {{m|ine-pro||*h₁}}. This theory nessecitates a reconstruction of {{m|ine-pro||*h₂wih₁rós}}.<ref name=Matasović>{{cite-book|editors=Alwin Kloekhorst and Tijmen Pronk|author=Matasović, Ranko|chapter=The Glottalic Theory and the “Kortlandt Effect”|page=110|title=The Reconstruction of Indo-European Stop Systems: From the Traditional Model to Glottalic Theories|date=2026-02-02|publisher=Brill|url=https://brill.com/view/title/73615|isbn=978-90-04-75044-9|doi=10.1163/9789004750449_014|passage=*h₂wih₁ro-}}</ref>

=== Reconstruction:Proto-Indo-European/weyh₁-
=== violo
===Etymology===
Borrowed from {{bor|eo|it|viola}}, {{bor|eo|en|violet}}, {{bor|eo|fr|violette}} and {{bor|eo|pl|fiołek}}.

===Pronunciation===
{{eo-pr|a=LL-Q143 (epo)-Lepticed7-violo.wav;LL-Q143 (epo)-Robin van der Vliet-violo.wav}}

===Noun===
--
===Etymology 1===

====Pronunciation====
{{it-pr|vi.òlo<r:DiPI><r:Olivetti:VIOLO100,alt#violo>}}

====Noun====
{{it-noun|m}} {{tlb|it|regional|Tuscan}}
--
===Etymology 2===

====Pronunciation====
{{it-pr|vi.òlo<r:Olivetti:VIOLO200,alt#violo>}}

====Noun====
{{it-noun|m}} {{tlb|it|regional|Venetian}}
--
===Etymology 3===

====Pronunciation====
{{it-pr|vìolo}}

====Verb====
{{head|it|verb form}}
--
===Etymology===
{{etymon|la|:from|vīs}}
Traditionally derived from {{m|la|vīs|t=strength}}, as if from some diminutive {{m|la||*viola}}. De Vaan prefers to derive the word instead from a deverbal adjective, which he reconstructs as {{inh|la|ine-pro||*weyh₁-elos}}. Either way, from {{der|la|ine-pro|*weyh₁-|t=to chase, strive after}}.<ref>{{R:itc:EDL|page=680}}</ref>

===Pronunciation===
* {{la-IPA|violō}}

=== world
===Etymology===
{{etymon|en|id=Q2|:inh|enm:world<id:Q2>|tree=1}}
From {{inh|en|enm|world}}, from {{inh|en|ang|weorold|t=world}}, from {{inh|en|gmw-pro|*weraldi}}, from {{inh|en|gem-pro|*weraldiz|t=lifetime, human existence, world|lit=age/era of man}}, equivalent to {{com|ang|wer|t1=man|eld|t2=age|nocat=1}}. Eclipsed non-native {{ncog|enm|mounde|t=world}}, from {{ncog|fro|monde}}, {{m|fro|munde|t=world}}. 
{{col-top|2|cog}}
Cognate with {{cog|sco|warld|t=world}}, {{cog|frr|Wārel}}, {{m|frr|wäält}}, {{m|frr|wråål|t=world}}, {{cog|stq|Waareld|t=world}}, {{cog|fy|wrâld|t=world}}, {{cog|af|wêreld|t=world}}, {{cog|bar|Wöd|t=world}}, {{cog|nl|wereld|t=world}}, {{cog|de|-}}, {{cog|lb|Welt|t=world}}, {{cog|nds-de|Wereld}}, {{m|nds|Werld|t=world}}, {{cog|wym|wełt|t=world}}, {{cog|yi|וועלט|t=world}}, {{cog|da|verden|t=world}}, {{cog|ovd|wärd|t=world}}, {{cog|fo|verð}}, {{m|fo|verøld|t=world}}, {{cog|is|veröld|t=world}}, {{cog|nrn|vrildan|t=the earth}}, {{cog|nb|verd}}, {{m|nb|verden|t=(the) world}}, {{cog|nn|verd|t=world}}, {{cog|sv|värld|t=world}}.
{{col-bottom}}

--
===Etymology===
{{etymon|enm|id=Q2|:inh|ang:weorold<id:world>|tree=1}}
{{inh+|enm|ang|weorold}}, from {{inh|enm|gmw-pro|*weraldi}}, from {{inh|enm|gem-pro|*weraldiz}}.<ref>{{R:MED Online|entry=world |pos=n|id=MED53430 |accessdate=2018-03-20}}</ref>

===Pronunciation===
* {{IPA|enm|/wurld/|/wɔrld/|ref2={{R:en:Dobson:1957|II|90|582}}}}
* {{IPA|enm|/wɛrld/|q2=late|/warld/|aa=especially Northern or Norfolk|ref2={{R:enm:eLALME}}<<name:LALME>>}}
=== virtus
===Etymology===
{{etymon|la|title=virtūs|:af|vir<t:man, male>|-tūs<id:abstract noun><pos:abstract noun-forming suffix>|tree=1|text=+}}

===Pronunciation===
* {{la-IPA|virtūs}}

===Noun===
=== vīra
===Etymology===
From {{der|pi|sa|वीर}}.

===Adjective===
{{pi-adj}}

# brave; heroic
=== Reconstruction:Proto-Iranian/wiHráh
===Etymology===
From {{inh|ira-pro|iir-pro|*wiHrás}}.

===Noun===
{{head|ira-pro|noun}}

# [[man]]
```


## [2026-10-16T05:16:20.615Z] TOOL CALL #45: Bash

```json
{
 "command": "for t in 'Reconstruction:Proto-Iranian/wiHr̥Háh' 'Reconstruction:Proto-Indo-European/wéyHs' 'violentus' 'Reconstruction:Proto-Iranian/wayHati' 'از بر' 'برم'; do echo \"=== $t\"; curl -s -G 'https://en.wiktionary.org/w/index.php' --data-urlencode \"title=$t\" --data-urlencode action=raw | head -40; done",
 "description": "Fetch more Wiktionary pages"
}
```


### [2026-10-16T05:16:21.892Z] TOOL RESULT

```
=== Reconstruction:Proto-Iranian/wiHr̥Háh
{{reconstruction}}
==Proto-Iranian==

===Etymology===
{{unk|ira-pro}}; possibly from {{af|ira-pro|*wi-|pos1=intensifier prefix||alt2=*Hr̥Háh}}, from {{der|ira-pro|iir-pro||*Hr̥Hás}}, from {{der|ira-pro|ine-pro||*h₂réh₁-s ~ *h₂r̥h₁-és}}, from {{suf|ine-pro|*h₂reh₁-|t1=to think|*-s|nocat=1}}.

===Adjective===
{{head|ira-pro|adjective}}

# {{senseid|ira-pro|adjective}} [[intelligent]]

====Derived terms====
* {{l|ira-pro|*awiHr̥Hakah}}
** {{desc|ps|ورک|tr=vrëk, vuruk|t=forgotten}}
* {{l|ira-pro|*awiHr̥Hyáh|t=forgotten}}<ref>{{R:ps:EVP|page=30|passage=*a-wairya-}}</ref>
** {{desc|kmr|bîr}}
** {{desc|ps|هېر|tr1=her|alts=1}}
** {{desc|zza|ڤیرا|tr=vîra}}
* {{l|ira-pro|*HhuwiHr̥Háh|t=intelligent}}
** {{desc|ae-yng|𐬵𐬎𐬬𐬍𐬭𐬀|𐬵𐬬𐬍𐬭𐬀}}
** {{desc|pal|tr=hwwyl|ts=huwīr|sc=Phlv}}<ref>{{R:kho:Bailey|vira|387|From base vai-: vi- ‘be keen’}}</ref> {{q|ghost word?}}

====Related terms====
* {{l|ira-pro|*wiHráHwah}}
** {{desc|sog|𐼱𐽀𐼰𐼴|ts=frāw|t=memory, recollection}}

====Descendants====
* {{desc|kho|tr=vira}}

===Noun===
{{head|ira-pro|noun}}<ref>{{R:xme:Asatrian:2011|vīr|421|*wīra-}}</ref>

# {{senseid|ira-pro|noun}} [[memory]]
# [[mind]]

====Inflection====
{{ira-decl-noun-auto}}

====Descendants====
{{top2}}
=== Reconstruction:Proto-Indo-European/wéyHs
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Please set a proper user-agent and respect our robot policy https://w.wiki/4wJS. See also https://phabricator.wikimedia.org/T400119</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1103 cp1103, Varnish XID 960906524<br>Upstream caches: cp1103 int<br>Error: 429, Please set a proper user-agent and respect our robot policy https://w.wiki/4wJS. See also https://phabricator.wikimedia.org/T400119 at Fri, 16 Oct 2026 05:16:21 GMT<br><details><summary>Sensitive client information</summary>IP address: 128.100.1.23</details></code></p>
</div>
=== violentus
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Please set a proper user-agent and respect our robot policy https://w.wiki/4wJS. See also https://phabricator.wikimedia.org/T400119</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1103 cp1103, Varnish XID 955247144<br>Upstream caches: cp1103 int<br>Error: 429, Please set a proper user-agent and respect our robot policy https://w.wiki/4wJS. See also https://phabricator.wikimedia.org/T400119 at Fri, 16 Oct 2026 05:16:21 GMT<br><details><summary>Sensitive client information</summary>IP address: 128.100.1.23</details></code></p>
</div>
=== Reconstruction:Proto-Iranian/wayHati
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Please set a proper user-agent and respect our robot policy https://w.wiki/4wJS. See also https://phabricator.wikimedia.org/T400119</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1103 cp1103, Varnish XID 984975625<br>Upstream caches: cp1103 int<br>Error: 429, Please set a proper user-agent and respect our robot policy https://w.wiki/4wJS. See also https://phabricator.wikimedia.org/T400119 at Fri, 16 Oct 2026 05:16:21 GMT<br><details><summary>Sensitive client information</summary>IP address: 128.100.1.23</details></code></p>
</div>
=== از بر
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Please set a proper user-agent and respect our robot policy https://w.wiki/4wJS. See also https://phabricator.wikimedia.org/T400119</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1103 cp1103, Varnish XID 981435999<br>Upstream caches: cp1103 int<br>Error: 429, Please set a proper user-agent and respect our robot policy https://w.wiki/4wJS. See also https://phabricator.wikimedia.org/T400119 at Fri, 16 Oct 2026 05:16:21 GMT<br><details><summary>Sensitive client information</summary>IP address: 128.100.1.23</details></code></p>
</div>
=== برم
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Please set a proper user-agent and respect our robot policy https://w.wiki/4wJS. See also https://phabricator.wikimedia.org/T400119</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1103 cp1103, Varnish XID 967753029<br>Upstream caches: cp1103 int<br>Error: 429, Please set a proper user-agent and respect our robot policy https://w.wiki/4wJS. See also https://phabricator.wikimedia.org/T400119 at Fri, 16 Oct 2026 05:16:21 GMT<br><details><summary>Sensitive client information</summary>IP address: 128.100.1.23</details></code></p>
</div>
```


## [2026-10-16T05:16:24.643Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py --help 2>&1 | head -15",
 "description": "Show fetch_source usage"
}
```


### [2026-10-16T05:16:25.059Z] TOOL RESULT

```
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
```


## [2026-10-16T05:16:29.056Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/ویر' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wiHr̥Háh' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wiHrós' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wiHráh' 'https://en.wiktionary.org/wiki/violo' 'https://en.wiktionary.org/wiki/world' 'https://en.wiktionary.org/wiki/virtus' 'https://www.etymonline.com/word/violent' 'https://www.etymonline.com/word/virtue' 'https://www.etymonline.com/word/world'; do python3 tools/fetch_source.py \"$u\" --note \"page 533, root Wei 2/Wiros: etymology check\" 2>&1 | tail -1; sleep 2; done",
 "description": "Archive web sources used",
 "timeout": 300000
}
```


### [2026-10-16T05:16:54.551Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/854616af8d32cf9d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/154add4e073b2ade.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/de529c4b22286a9b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a8fd80b2d4d4b2c8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5bc2e8f34ad3645d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/acaa34a02b4ebf0d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fc1548d1d9928657.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/207c43bde2e111ea.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/46649e7c687c84bd.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/20d9873d2b41a1ad.txt
```


## [2026-10-16T05:16:57.775Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 854616af8d32cf9d 207c43bde2e111ea 46649e7c687c84bd 5bc2e8f34ad3645d; do echo \"== $f $(wc -c <$f.txt)\"; grep -i -m3 'error\\|from Latin violentus\\|virtus\\|from Middle Persian\\|vīs' $f.txt | cut -c1-300; done; tail -10 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin: d=json.loads(l); print(d['status'],d['bytes'],d['url'][:70])\"",
 "description": "Check archived pages loaded correctly"
}
```


### [2026-10-16T05:16:58.142Z] TOOL RESULT

```
== 854616af8d32cf9d 10977
 From Middle Persian [Book Pahlavi needed] ( wyl /⁠wīr⁠/ ) , from Proto-Iranian *wiHr̥Háh ( “ noun ” ) .
 From Middle Persian [Book Pahlavi needed] ( wyl /⁠wīr⁠/ ) , from Proto-Iranian *wiHr̥Háh ( “ memory, mind ” ) .
 Categories : Bakhtiari terms inherited from Middle Persian 
== 207c43bde2e111ea 134
FETCH FAILED: HTTP Error 403: Forbidden
== 46649e7c687c84bd 133
FETCH FAILED: HTTP Error 403: Forbidden
== 5bc2e8f34ad3645d 15587
 Traditionally derived from vīs ( “ strength ” ) , as if from some diminutive *viola . De Vaan prefers to derive the word instead from a deverbal adjective, which he reconstructs as Proto-Indo-European *weyh₁-elos . Either way, from Proto-Indo-European *weyh₁- ( “ to chase, strive after ” ) . [ 1 ] 
200 851 https://vajehyab.com/moein/باران
200 7401 https://abadis.ir/fatofa/اسمز/
-1 39 https://vajehyab.com/moein/بارگین
200 3743 https://en.wiktionary.org/wiki/Wichse
200 7186 https://en.wiktionary.org/wiki/vegeo
200 7288 https://en.wiktionary.org/wiki/vigeo
200 29486 https://en.wiktionary.org/wiki/wait
200 46310 https://en.wiktionary.org/wiki/watch
200 12563 https://en.wiktionary.org/wiki/vegetable
200 5519 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/wáȷ́r
```


## [2026-10-16T05:17:02.014Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; wc -c 154add4e073b2ade.txt de529c4b22286a9b.txt a8fd80b2d4d4b2c8.txt acaa34a02b4ebf0d.txt fc1548d1d9928657.txt 20d9873d2b41a1ad.txt; head -c 300 154add4e073b2ade.txt; cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py 'https://vajehyab.com/moein/ویر' --note 'page 533 Mo’in vir' | tail -1; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/ویر/' --note 'page 533 Mo’in vir (abadis)' | tail -1",
 "description": "Verify archives; fetch Mo'in entry"
}
```


### [2026-10-16T05:17:04.216Z] TOOL RESULT

```
 6259 154add4e073b2ade.txt
 6047 de529c4b22286a9b.txt
 3716 a8fd80b2d4d4b2c8.txt
63547 acaa34a02b4ebf0d.txt
 7991 fc1548d1d9928657.txt
  132 20d9873d2b41a1ad.txt
87692 total
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wiHr̥Háh
FETCHED: 2026-10-16T05:16:32Z
STATUS: 200
TITLE: Reconstruction:Proto-Iranian/wiHr̥Háh - Wiktionary, the free dictionary

Reconstruction:Proto-Iranian/wiHr̥Háh - Wiktionary, the free dictionary 

 Jump to content 

 Main/home/sfmqrb/git/rishe-private/data/verification/sources/web/8992d29fd02b71f3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9d9e3f141e0d77cc.txt
```


## [2026-10-16T05:17:06.461Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; wc -c 8992d29fd02b71f3.txt 9d9e3f141e0d77cc.txt; grep -o '.\\{0,100\\}حافظه.\\{0,200\\}' 9d9e3f141e0d77cc.txt 8992d29fd02b71f3.txt | head -5",
 "description": "Check Mo'in archive content"
}
```


### [2026-10-16T05:17:09.889Z] TOOL RESULT

```
 1418 8992d29fd02b71f3.txt
21754 9d9e3f141e0d77cc.txt
23172 total
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,200}
                            \___exceeds complexity limits
```


## [2026-10-16T05:17:12.343Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; python3 -c \"\nimport re\nfor f in ['9d9e3f141e0d77cc.txt','8992d29fd02b71f3.txt']:\n  t=open(f).read()\n  for m in re.finditer('معین|په\\.|حافظه',t):\n    print(f, t[max(0,m.start()-150):m.start()+250].replace('\\n',' ')); print('--')\n\" | head -30",
 "description": "Extract Mo'in text from archive"
}
```


### [2026-10-16T05:17:12.686Z] TOOL RESULT

```
<string>:5: SyntaxWarning: "\." is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\."? A raw string is also an option.
9d9e3f141e0d77cc.txt نری آبادیس  ویر - معنی در دیکشنری آبادیس    دیکشنری مترجم بپرس    ویر  /vir/   مترادف ویر : فریاد، ناله، ادراک، استنباط، درک، فهم، هوش، به خاطرسپاری، حافظه، یادگیری، میل، ویار، هوس  دنبال کنید    لغت نامه دهخدا   ویر. ( اِ ) بیر. بر. از ویر؛ یعنی ازحفظ کردن و به خاطر نگاه داشتن. ( برهان ). || حفظ. حافظه. ( یادداشت مرحوم دهخدا ) :  بپرسید نامش ز فرخ هجیر بگفتا که نامش ندارم به ویر. فردوسی. چه افتاد
--
9d9e3f141e0d77cc.txt  حافظه، یادگیری، میل، ویار، هوس  دنبال کنید    لغت نامه دهخدا   ویر. ( اِ ) بیر. بر. از ویر؛ یعنی ازحفظ کردن و به خاطر نگاه داشتن. ( برهان ). || حفظ. حافظه. ( یادداشت مرحوم دهخدا ) :  بپرسید نامش ز فرخ هجیر بگفتا که نامش ندارم به ویر. فردوسی. چه افتاد ای عزیزان مر شما را که شد یکبارتان یاد من از ویر؟ ؟ - از ویر شدن ؛ از یاد رفتن.  || فهم و هوش و ادراک. ( ناظم الاطباء ) :  دو مرد خردمند بسیارویر به
--
9d9e3f141e0d77cc.txt   یا برون شو ز چرخ چون مردان  ورنه با وای وای و ویر مباش. سنایی ( از حاشیه برهان ). - جیر و ویر ؛ داد و فریاد ( در تداول تهرانی ها ). ( حاشیه برهان چ معین ). || ( ص ) ویر با ثانی مجهول ، بی عقل و احمق. ( برهان ). و رجوع به رشیدی شود. ( حاشیه برهان چ معین ). || در تداول ، شیت. بی نمک. ( یادداشت مرحوم دهخدا ). سفید. سخت سفید که مطبوع نباشد. ( یادداشت مرحوم دهخدا ). || ( اِ ) میل مفرط. هوس شدید. ویار
--
9d9e3f141e0d77cc.txt د و فریاد ( در تداول تهرانی ها ). ( حاشیه برهان چ معین ). || ( ص ) ویر با ثانی مجهول ، بی عقل و احمق. ( برهان ). و رجوع به رشیدی شود. ( حاشیه برهان چ معین ). || در تداول ، شیت. بی نمک. ( یادداشت مرحوم دهخدا ). سفید. سخت سفید که مطبوع نباشد. ( یادداشت مرحوم دهخدا ). || ( اِ ) میل مفرط. هوس شدید. ویار. هوس کاری : ویرش گرفته. ویرش آمده. || جاذبه و کششی که در پاره ای از کارها هست که عامل از آن به آسان
--
9d9e3f141e0d77cc.txt بدان منسوب است احمدبن محمدبن ابی عمروبن ابی بکر ویری. ( حاشیه برهان قاطع از معجم البلدان ). بیشتر بخوانید ...    فرهنگ فارسی   ویل، وای، ناله، فریاد، حافظه، فهم، ادراک، هوش ( مهمل ( هیر ) )    فرهنگ معین   [ په . ] (اِ. ) ۱ - هوش ، فهم . ۲ - یاد، ذهن .  (اِ. ) ناله ، فریاد.  (اِ. ) (عا. ) میل و هوس شدید به چیزی .    فرهنگ عمید   ۱. حافظه: بپرسید نامش ز فرخ هجیر / بگفتا که نامش ندارم ز ویر (فردوسی:
--
9d9e3f141e0d77cc.txt یری. ( حاشیه برهان قاطع از معجم البلدان ). بیشتر بخوانید ...    فرهنگ فارسی   ویل، وای، ناله، فریاد، حافظه، فهم، ادراک، هوش ( مهمل ( هیر ) )    فرهنگ معین   [ په . ] (اِ. ) ۱ - هوش ، فهم . ۲ - یاد، ذهن .  (اِ. ) ناله ، فریاد.  (اِ. ) (عا. ) میل و هوس شدید به چیزی .    فرهنگ عمید   ۱. حافظه: بپرسید نامش ز فرخ هجیر / بگفتا که نامش ندارم ز ویر (فردوسی: ۲/۱۶۱ ). ۲. فهم، ادراک، هوش: یکی تیزویری ست و بس
--
9d9e3f141e0d77cc.txt ر ) )    فرهنگ معین   [ په . ] (اِ. ) ۱ - هوش ، فهم . ۲ - یاد، ذهن .  (اِ. ) ناله ، فریاد.  (اِ. ) (عا. ) میل و هوس شدید به چیزی .    فرهنگ عمید   ۱. حافظه: بپرسید نامش ز فرخ هجیر / بگفتا که نامش ندارم ز ویر (فردوسی: ۲/۱۶۱ ). ۲. فهم، ادراک، هوش: یکی تیزویری ست و بسیاردان / کز او نیست احوال گیتی نهان (لبیبی: شاعران بی دیوان: ۴۸۸ ). ۳. بهره: نه گهواره دیدم نه پستان نه شیر / نه از هیچ خوشی مرا بود وی
--
9d9e3f141e0d77cc.txt یت دارد.   wiki: ویر (هلند)    این نوشته برگرفته از سایت ویکی پدیا می باشد، اگر نادرست یا توهین آمیز است، لطفا گزارش دهید: گزارش تخلف    جدول کلمات   حافظه, فهم, ادراک, هوش    پیشنهاد کاربران   "ویر" در پارسی میانه به مینه ی "مرد" نیز بوده است. در اوستایی "ویرَ:vira" بوده است. ما آن را بیشتر در واژگانِ آمیغی داشته ایم.  نمونه: ویرزَدار ( پارسیِ میانه ) / ویرَ - گَن ( اوستایی ) /ویرآسپَ ( اوستایی )
--
9d9e3f141e0d77cc.txt یشتر در واژگانِ آمیغی داشته ایم.  نمونه: ویرزَدار ( پارسیِ میانه ) / ویرَ - گَن ( اوستایی ) /ویرآسپَ ( اوستایی ) و. . . .   وسوسه   ویراختن: حفظ کردن حافظه: ویرازه ویریدن: حس کردن برابر sense سهیدن: feel سهستن: demonstrate ایاسیدن، ایاشتن: به خاطر سپردن   در زبان لکی بسته بود نوع تلفظ معنایش فرق می کند.  VIR یعنی یاد و هوش. مثل: هامه ویرت یعنی به یادت هستم.  VIAR به فتح یاء یعنی برف. مثل: چنین ویر
--
9d9e3f141e0d77cc.txt ۱۳۴۹. ( مصحح در پایان جلد اول شرح مفصل و سودمندی از فهرست لغات�ترکی�و�مغولی�رایج در متون فارسی از سده هفتم به بعد را نوشته است )  • فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵ • غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶ • فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹   در لری علاوه بر حافظه و یاد و خاطر و
--
9d9e3f141e0d77cc.txt شگاهی، تهران، ۱۳۸۶ • فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹   در لری علاوه بر حافظه و یاد و خاطر و حواس معنی توجه هم می دهد مثلا میگیم به درس ویر واکن یعنی به درس توجه کن یا حواست به درس باشه   ویر به گویش بختیاری یعنی خاطره و ذهن، حافظه مثال تو ز ویرم نیری یعنی از یاد و خاطرم پاک نمی شوی   وِ یر در زبان لکی به معنی ۱. برف می 
--
9d9e3f141e0d77cc.txt ه و یاد و خاطر و حواس معنی توجه هم می دهد مثلا میگیم به درس ویر واکن یعنی به درس توجه کن یا حواست به درس باشه   ویر به گویش بختیاری یعنی خاطره و ذهن، حافظه مثال تو ز ویرم نیری یعنی از یاد و خاطرم پاک نمی شوی   وِ یر در زبان لکی به معنی ۱. برف می باشد ۲. ویر گویچ گویچ یعنی گوله های برف برف و بوران   ویر =فیر=فکر درزبان لکی هنوز به هرسه صورت بالا تلفظ می شود و به معنای = یاد ، هوش و اتعداد ذهنی برای
--
9d9e3f141e0d77cc.txt ست .  ویرا =باهوش و تیزهوش ، دارنده هوش قوی وتیز  ویر =یاد و ا=پسوند دارندگی   ویر در پشتو اندوه و مویه است   ویر : ویر در زبان لری به معنی یاد، ذهن، حافظه، خاطر، هوش .  هیر : هیر در زبان لری به معنی یاد، ذهن، حافظه، خاطر، هوش .   ویر به چم پهلوان هم هست ویرو   ویر ( Vir ) در زبان سانسکریت به معنی جنگاور، قهرمان و شجاع است   بنده به خاطر دارم که در زمان های قبل در زبان محاوره ی محلی ما دقیقا به مع
--
9d9e3f141e0d77cc.txt  ا=پسوند دارندگی   ویر در پشتو اندوه و مویه است   ویر : ویر در زبان لری به معنی یاد، ذهن، حافظه، خاطر، هوش .  هیر : هیر در زبان لری به معنی یاد، ذهن، حافظه، خاطر، هوش .   ویر به چم پهلوان هم هست ویرو   ویر ( Vir ) در زبان سانسکریت به معنی جنگاور، قهرمان و شجاع است   بنده به خاطر دارم که در زمان های قبل در زبان محاوره ی محلی ما دقیقا به معنای یاد و خاطره کاربرد داشت.  مثلا "از یادم رفت" به زبان محل
--
9d9e3f141e0d77cc.txt حیر مباش یا برون شو ز چرخ چون مردان ورنه با وای وای و ویر مباش.  سنایی || ( ص ) ویر ، بی عقل و احمق. ( برهان ) . و رجوع به رشیدی شود. ( حاشیه برهان چ معین ) . || در تداول ، شیت. بی نمک. ( یادداشت مرحوم دهخدا ) . سفید. سخت سفید که مطبوع نباشد. ( یادداشت مرحوم دهخدا ) . || ( اِ ) میل مفرط. هوس شدید. ویار. هوس کاری : ویرش گرفته. ویرش آمده. || جاذبه و کششی که در پاره ای از کارها هست که عامل از آن به آ
--
```


## [2026-10-16T05:17:17.714Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f=$(python3 tools/fetch_source.py 'https://abadis.ir/fatofa/برم/' --note 'page 533 Mo’in barm/bar memory' | tail -1); wc -c $f; python3 -c \"\nimport re,sys\nt=open('$f').read()\ni=t.find('فرهنگ معین')\nprint(t[i:i+700])\nfor m in re.finditer('حفظ',t): print('>>',t[max(0,m.start()-200):m.start()+150].replace('\\n',' '))\n\" | head -30",
 "description": "Fetch Mo'in barm entry"
}
```


### [2026-10-16T05:17:19.543Z] TOOL RESULT

```
18506 /home/sfmqrb/git/rishe-private/data/verification/sources/web/b24784ea838a62cc.txt
فرهنگ معین

 (بَ ) [ په . ] ( اِ. ) آبگیر، استخر، برکة آب .
 (بَ رَ ) (اِ. ) ۱ - چوبی که پارچه ای ملون بر بالای آن بندند و در میدان نصب کنند برای آگاه کردن مردم از کشتی پهلوانان . ۲ - چوب بندی را گویند که تاک انگور و بیارة کدو و خیار و غیره را بالای آن گذارند، داربست . 

 فرهنگ عمید

 حفظ، حافظه.
۱. برغ.
۲. چشمه: چون تن خود به برم پاک بشست / از مسامش تمام، لؤلؤ رُست (شهیدبلخی: شاعران بی دیوان: ۲۸ ).
۳. تالاب.
۴. گودالی که در آن آب جمع شده.
چوب بندی که شاخه های تاک یا بیارۀ کدو، ومانندِ آن را روی آن می اندازند، چوب بست، داربست.
عنصری غیر فلزی، فرّار، مایع، سنگین، و به رنگ سرخ که در داروسازی، رنگ سازی، و ساخت مواد شیمیایی عکاسی به کار می رود. 

 فرهنگستان زبان و ادب

 {carr} [مهندسی منابع طبیع
>> دیس    دیکشنری مترجم بپرس    برم  /borom/   مترادف برم : آبگیر، استخر، برکه، تالاب، غدیر، بند، سد کوچک  معنی انگلیسی : bromine , memory , trellis    دنبال کنید    لغت نامه دهخدا   برم. [ ب َ ] ( اِ ) حفظ و از بر کردن و بیاد نگاه داشتن. ( برهان ). حفظ که آنرا از بر گویند. ( آنندراج ) . بَر. - از برم داشتن ؛ از حفظ داشتن. از بر داشتن. ( یادداشت دهخدا
>> ادف برم : آبگیر، استخر، برکه، تالاب، غدیر، بند، سد کوچک  معنی انگلیسی : bromine , memory , trellis    دنبال کنید    لغت نامه دهخدا   برم. [ ب َ ] ( اِ ) حفظ و از بر کردن و بیاد نگاه داشتن. ( برهان ). حفظ که آنرا از بر گویند. ( آنندراج ) . بَر. - از برم داشتن ؛ از حفظ داشتن. از بر داشتن. ( یادداشت دهخدا ) :  از مصحف تندی و درشتی نه همانا یک سوره برآ
>> گلیسی : bromine , memory , trellis    دنبال کنید    لغت نامه دهخدا   برم. [ ب َ ] ( اِ ) حفظ و از بر کردن و بیاد نگاه داشتن. ( برهان ). حفظ که آنرا از بر گویند. ( آنندراج ) . بَر. - از برم داشتن ؛ از حفظ داشتن. از بر داشتن. ( یادداشت دهخدا ) :  از مصحف تندی و درشتی نه همانا یک سوره برآید که تو از برم نداری. فتوحی مروزی.  || تالاب و استخر و چشمه آب.
>> ه برمة شود. || ( اِخ ) نام ناقه ای. ( منتهی الارب ). بیشتر بخوانید ...    فرهنگ فارسی   شهری در آلمان واقع در ساحل وسر ۷۵٠/۵٠٠ سکنه انبار محصولات خارجه کشتی سازی صنایع مکانیکی شیمیایی و غذایی نساجی . حفظ، حافظه ( اسم ) مایعی است قهوه یی رنگ و سنگین وزن مخصوص آن ۳ و بسیار فرار است . در ۶۳ درجه بجوش میاید و در ۷ درجه یخ میزند. در آب حل میشود و محلول 
>> که پارچه ای ملون بر بالای آن بندند و در میدان نصب کنند برای آگاه کردن مردم از کشتی پهلوانان . ۲ - چوب بندی را گویند که تاک انگور و بیارة کدو و خیار و غیره را بالای آن گذارند، داربست .    فرهنگ عمید   حفظ، حافظه. ۱. برغ. ۲. چشمه: چون تن خود به برم پاک بشست / از مسامش تمام، لؤلؤ رُست (شهیدبلخی: شاعران بی دیوان: ۲۸ ). ۳. تالاب. ۴. گودالی که در آن آب ج
>>    چوب بستی که انگور بر ان اندازند ترم و تارم است است و نه برم  ترم یا همان تارم زنجان که انرا به نادرست طارم مینویسند ترم است پس چه شد جستان وهسودان و ترم دیلمان   غلت عقب   Roll bag    بَرم [barm]: حفظ، خافظه، از برم کردن/شدن/بودن.  در انگلیسی memory گویند.   برم : [اصطلاح راه سازی] ایجاد پله در ترانشه هایی که معمولا از 8 متر بیشتر باشند برای جلو
```


## [2026-10-16T05:17:24.851Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo HRN; grep -n -i 'vīr\\b\\|vir\\b\\|barm\\b' HRN.txt | head -8; echo HUB; grep -n -i 'vīr\\b\\| vir \\|barm\\b' HUB.txt | head -8; echo CHEUNG; grep -n -i 'u̯aiH\\|\\*vaiH\\|\\*u̯ai-\\|vaya-\\|vayeiti' CHEUNG.txt | head -8; echo ARY; grep -n 'ویر\\b\\|ویر ' incoming/ARY/ARY_pages.txt | head -5; grep -n -i '^VIR\\b\\|\\bVIR\\b' incoming/ARY/ARY_latin_index_pages.txt | head -5",
 "description": "Grep Horn, Hubschmann, Cheung, Aryanpur"
}
```


### [2026-10-16T05:17:25.177Z] TOOL RESULT

```
HRN
588:vir äst an,
589:2) Vgl. auch phlv. vlrästav^ viräyOßn ; hamrästcni.5 -
1645:emä Vir (jüd.-pers.) s. ma (No. 955).
2074:mäz. var; Käs. ver, ver ö vir.
4880:wa/. bär^ sar. divir, §iyn. dive, divSr, minj. labra,
9403:1086. vir Sinn, Verstand; Gedächtniss'-), hir, her (8,
9405:g. vir därtmün 'erinnern', vtr svdmün Vergessen'.
9407:Et. ir. II, 183); phlv. vir, vlräk im Gedächtniss
HUB
3122:kund Vir strenuus* zu trennen, vgl. kunda^ kundavar,
CHEUNG
11622:*ud-avaya-, the dental ought to have disappeared, becoming either -y- or -h-. 
ARY
616:قبر و روی گنجانه‌های سفالین. وجود گورهای برجسته (1)1180۸) و آثار ویرانی ساختمان‌ها و
629:می‌شود. نوشتارهای هند و آریایی کامل‌ترین و پیشین ترین تصویر را از یک زبان کهن هند و اروپایی
744:05880 بل8510۸شا)) برمی‌خوریم. این منون تصویر کاملی از زبان و فرهنگك و ساختار
935:تصویر کلی فرهنگ و جامعهی هند و اروپایی حدود شش هزار سال پیش را به تقریب ترسیم کنند.
936:طبق این تصویر هند و اروپائیان برخی در یک محل ساکن بودند (به دلیل همریشگی واژه‌های وابسته
1946:VIR (U4) (PORTUGUESE) (65 : ASANSKRIT) Si Sila
5950:vir dlasaas dabei TAUTO — (OLD PRUSSIAN) pS 53.
6824:vir (abaya veo seb olny (REF - ERE
15313:BUCK: 81 VIR LATIN) oa
```


## [2026-10-16T05:17:27.751Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '9400,9412p' HRN.txt; echo; sed -n '3118,3124p' HUB.txt; echo ARY; grep -n 'pdf page' incoming/ARY/ARY_latin_index_pages.txt | awk -F: '$1<15313' | tail -1; sed -n '15300,15320p' incoming/ARY/ARY_latin_index_pages.txt",
 "description": "Read Horn vir, Hubschmann, Aryanpur"
}
```


### [2026-10-16T05:17:28.016Z] TOOL RESULT

```
gehören scheint. Nachträglich sehe ich auch Toma-
schek zu sar. vanao 'Leerheit, Eitelkeit, Müssiggang,
Faulheit'.
1086. vir Sinn, Verstand; Gedächtniss'-), hir, her (8,
Vullers), Viru 'im Gedächtniss habend'.
g. vir därtmün 'erinnern', vtr svdmün Vergessen'.
aw. *nra' 'Einsicht' in livtra- etc. (Darmesteter,
Et. ir. II, 183); phlv. vir, vlräk im Gedächtniss
habend* (Bund.).
kurd. Mr 'Gedächtniss*; bei. glr 'Gedächtniss, Er-
innerung' (110).
1087. werän, werane wüst', heran.
phlv. aperän 'wüst' (M6n.), aperämh (Ganj-T äayakän,

kamra 'Gewolbe, Stalf (N 6 1 d e k e , Pers. Stud. H, p. 40)
ist mir unklar.
868. Np. kund *stumpf = bal. kunt *stumpf, grob, einfaltig*
(Geiger) = skr. (prakr.) kunthar- 'stumpf. Davon
kund Vir strenuus* zu trennen, vgl. kunda^ kundavar,
869. Horn bemerkt mit Recht, dass auf paz. xandan
(= kandan) nichts zu geben ist. Das angefiihrte
ARY
15304:[pdf page 524]
nr sebG olny VINCI, VICIA (LATIN) 3
over slaseas aabcid WAIHSTA GOTHIC) Si
i HOLD ENGLISH) oS gS
Z |
[pdf page 524]
OND 1 (ead ale” Oot ya" 6) eos
WURS (OLD PRUSSIAN) 5 gus 9 Vika, VIRO HAVESTAN) glen)
FER (OLD IRISH) oS 5 p\ WIR, WIROMANDIH :(PAHLAVI) «5. he
BIR KURDISH) 53,5
REFERENCES: beth GIR s(BALUCHI) gx gy
POKORNY, SSS*CAATTAAATR WIR TOKHARIAN A) A «5 Jos
MACKENZIE: VIRA SANSKRIT) xy Sule
(MEMORY) 123, (MIND) 124 «yikos (GREEK) gh»
BUCK: 81 VIR LATIN) oa
RAMAT: 46 WAIRS AGOTHIC) S56
TY4A g ITF sabi aby WER. (OLD ENGLISH) ef galSii
rrver Mesens abi! VYRAS (LITHUANIAN) gl 3
wiks LATVIAN) (3) 393
leedhoal
"ad Cass gk get ap” yale" ye press cal slg 2
AVE :(PORTUGUESE) Jlis VISH, VAZ HAVESTAN) glo 31
```


## [2026-10-16T05:17:34.582Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo IEC; grep -n -i 'wīros\\|wiros\\|wīrós' IEC.txt | head -5; echo SYN; grep -n 'Lat. vir\\b\\|L. vir,\\|Av. vīra\\|vīra-' SYN.txt | head -5; echo WLD; grep -n -i 'vīra-\\|vira-' incoming/WLD/WLD_Bd1_pages.txt | head -8",
 "description": "Grep Mann, Buck, Walde-Pokorny"
}
```


### [2026-10-16T05:17:35.040Z] TOOL RESULT

```
IEC
SYN
2281:2.21 MAN? (vs. Woman) , Goth. wair (guma, manna) Lith.  vyras Gr Fes ON karl, karlmadr Lett. _virs Lat. vir Dan. mand ChSl. mazt It. uomo Sw. man SCr.  Covjek, muSkarac Fr, homme OE wer (wépnedman, Boh. muz Sp. hombre, varén ceorl, man) Pol. maz, meszczyzna Rum. bdrbat, om ME — man (were) Russ. mu3éina ifs fer NE man Skt. —_nar-, nara-, vira-, Nir. fear Du. man pumaiis- W. guwr OHG man, gomman (wer, Ay. nar-, virad~, OPers. Br. gwaz karl) martiya- MHG man NHG mann
2583:Grk. — avip (xéars) NG ayrpas, obfuyos Lat. vir, marilus (coniux)
2634:1. From words for ‘man’ and ‘wom- an’, which have already been discussed in 2.21, 2.22, Probably in every IE language the words for ‘man” and ‘wom- an’ may be used for ‘husband’ and ‘wife’, at least in colloquial or vulgar speech, as is true even in NE my man, my woman. Here are listed only those that are the usual terms. (So NG yuvaixa for ‘wife’ is not vulgar, like NE woman in this sense, but is used in the best circles, where cifvyos would be felt as super- refined, almost like NE spouse; Dan. kone is now in the best usage, more usu- al than hustru; NHG weib for ‘wife’, vul- gar in the north, is usual in southern Germany). While many of these retain also their earlier use, as Grk. dvp, yuri, Lat. vir, Fr. femme, NHG mann, ChSI. mgzt, Zena, etc., others have come to be used prevailingly or exclusively for ‘hus- band’, ‘wife’, as ON verr ‘husband’, Goth. géns ‘wife’, NE wife, Br. gwreg ‘wife’, Lith. Zmona, Pol. zona ‘wife’, Russ. muz, Zena ‘husband, wife’. All such relations are shown by a compari- son of the lists 2.21, 2.22 and 2.31, 2.32.
29050:Skt. vzra-, also ‘heroic, powerful, ex- cellent’, lit. ‘manly’ : vira- ‘man, hero’, Lat. vir ‘man’, etc. (2.21).
WLD
44123: BB. 19, 282) AnschluB an keu- ^ehwellen" entw. im Sinne von ai. cavira-
```


## [2026-10-16T05:17:39.149Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -A12 '^2.21 MAN' SYN.txt | grep -i -m5 'vir\\|wiro'; sed -n '2290,2320p' SYN.txt | grep -i 'vir\\|IE \\*\\|wi-ro\\|wīro' | head; echo WLD; grep -n -i 'u̯īro\\|uiro-\\|ulro-\\|vir \"Mann\\|vir ,Mann\\|vir „Mann' incoming/WLD/WLD_Bd1_pages.txt | head; echo IEC2; grep -n -i 'vir \\|wiros\\|uiros' IEC.txt | head -5",
 "description": "More Buck, Walde-Pokorny, Mann"
}
```


### [2026-10-16T05:17:39.726Z] TOOL RESULT

```
2281:2.21 MAN? (vs. Woman) , Goth. wair (guma, manna) Lith.  vyras Gr Fes ON karl, karlmadr Lett. _virs Lat. vir Dan. mand ChSl. mazt It. uomo Sw. man SCr.  Covjek, muSkarac Fr, homme OE wer (wépnedman, Boh. muz Sp. hombre, varén ceorl, man) Pol. maz, meszczyzna Rum. bdrbat, om ME — man (were) Russ. mu3éina ifs fer NE man Skt. —_nar-, nara-, vira-, Nir. fear Du. man pumaiis- W. guwr OHG man, gomman (wer, Ay. nar-, virad~, OPers. Br. gwaz karl) martiya- MHG man NHG mann
2284-1. TE *wiro-, that is, *wt-ro- : Lat. vis, Skt. vayas, ete. ‘strength’. Walde- ot ff. Ernout-M. 1112 f.
2285-at. vir, Umbr. uiro (ace. pl.): Ir. Jer, Nir. fear, W. gur, Nie nas Ge ae with neg. for ‘no one’); Goth. wair Gat Chee OE wer, ete. (old : ) Dut now obs. except in epds.,
2287-» Ay, vira-,
2289-Lith. vyras, Lett. virs;
1. IE *gvena-, *gveni-, etc., with gra- dation of the root syllable. Without known root connection, unless at some remote period, before differentiation of the gutturals (?), with IE *gen- ‘beget’ and ‘bear’ of Lat. gignere, ete. Walde- P. 1.681.
3. Ir. frace ‘woman’, W. gwrach ‘old woman, witch’, gwraig ‘woman, wife’, Br. gwreg ‘wife’, prob. fem. derivs. of Ir. Jer, W. gwr, etc. ‘man’? (Pedersen, 1.159 dub.). Cf. Lat. viragd ‘manlike female’, virgo ‘maiden’, fr. vir, W. dynes ‘woman’ (cf. Morris Jones 223) fr. dyn ‘man”, and Skt. nar7- ‘woman’ fr. nar- ‘man”,
WLD
IEC2
5900:$£uhen- (guhon-, guhn-) ‘sound; resound’. See next & ĝuenghõ, &uhon- Skt. jhanarni, v. id.; Alb. zâ, gs záni (T: zë, gs zëri) ‘voice, sound’; cf. pé-zàj, bzáj ‘bawl’; për- zâj (2), id.; Lat. (o-gde) honos, honor beside hones-tus (*&uhonos, -es-; OCS zvonů “sound, bel; Pol. dzwon, id. beside OCS (z-gde in i-basis) zvínjo, -čti ‘resound’ and zví- nú, pl. zvir évy ‘noise’; Latv. zvans "bell" WP I, 642
6904:käng, ið (kou-, kāu-, kü-) (1) “strike, hew’. WP I, 330. Gk. etc. ambig. Cf. Káu- Av. cf. fra-kava ‘fight’; apa-kavo ‘warrior’; Per. kavam, inf. kavidan and kaftan ‘dig’; Tokh. A ko-, B kau- 'strike, kil; Pelasg? cf. Ká- beiroi (/émetalworkers of Vulcan! fr. *kau-uiroi (?), see uiros); Gk. cf. kaunós “lot, fate’; Ir. cf. caibe 'spade-blade, blade of hoe’; Br. cf. kawad, f. 'surprise-attack'; W cawod ‘shower’: Cor. cowas ‘gust, squal; OHG houwan, OE
14074:quiros, us ‘pert’. See Supt: quíquor- W pyr, adv. & adj. id.; Li. cf. j-kirüs, -kyrüs, adj. ‘importunate’
20374:uir- (3), see uiros and next
20375:uirátos (uirotos) «team of men, troop’. Cf. uiros Skt. cf. viráta, f. ‘manliness’; Lat. cf. duum-, trium-viratus, gs: -us, m. beside -viritim, adv. *man-by-man'; OS Ob werod, m. n. ‘troop’
```


## [2026-10-16T05:17:42.615Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^uiros\\|^uīros\\|^uiros ' IEC.txt | head; n=$(grep -n '^uiros' IEC.txt | head -1 | cut -d: -f1); [ -n \"$n\" ] && sed -n \"${n},$((n+3))p\" IEC.txt | cut -c1-700; grep -n '^uejō\\|^uei- \\|^ueiō\\|^uiēti\\|^uis \\|^uīs' IEC.txt | head",
 "description": "Mann uiros entry"
}
```


### [2026-10-16T05:17:42.936Z] TOOL RESULT

```
20378:uiros “man, husband, hero’. WP I, 314 Skt. viráh “man, hero’; Av. viro ‘man’; Tokh. A wir, id.; Gk. (Pelasgian ?) cf. Ka-beiroi (*metal-workers' if fr. *káu-uiroi, cf. káuo (1), kàuos (1)); Lat. vir, gs: -i, m. ‘man’; Umb. veiro, viro, neut. pl. ‘slaves’; Lat. cf. also cüria, Volscian co-uehriu (fr. *ko-uirio *council); Ir. fear ‘man’; Gaul. ver-, W gwr, pl: gwyr, Br. gur, pl. gwir, OBr. gur; Cor. gour, id.; Go. wair, OE wer, MHG wér- (in wolt -gelt); ON vert, m. “man, husband’; OCS cf. (?) vrüsti, vrüsta Or vrísti, vrísta “age of man; Li. vyras, Lat- vian virs “man, husband?
uiros “man, husband, hero’. WP I, 314 Skt. viráh “man, hero’; Av. viro ‘man’; Tokh. A wir, id.; Gk. (Pelasgian ?) cf. Ka-beiroi (*metal-workers' if fr. *káu-uiroi, cf. káuo (1), kàuos (1)); Lat. vir, gs: -i, m. ‘man’; Umb. veiro, viro, neut. pl. ‘slaves’; Lat. cf. also cüria, Volscian co-uehriu (fr. *ko-uirio *council); Ir. fear ‘man’; Gaul. ver-, W gwr, pl: gwyr, Br. gur, pl. gwir, OBr. gur; Cor. gour, id.; Go. wair, OE wer, MHG wér- (in wolt -gelt); ON vert, m. “man, husband’; OCS cf. (?) vrüsti, vrüsta Or vrísti, vrísta “age of man; Li. vyras, Lat- vian virs “man, husband?
uiruos, is, io ‘twist, twine, gut, string, spiral. Cf. uir- (2), ueru- (2) and WP II, 499. (Variant of type wir- in Per. Tokh. Arm. See uir- (2). Gk. ambig.). Cf. uiior- Per. cf. girah *knot; Tokh. cf. wiralom (?) 'zedoary'; Arm. cf. gir, gs: gro, ab. s. grov
1545
‘written character’; Gk. cf. iris, dial. wiris, gs; -idos, f. ‘rainbow, iris’; Ir. cf. fearb, f. ‘stripe’; Mir, ferbán ( potentilla", ambig. cf. ueru-: Gk. dial. berbínia *pot-hook"); R (ambig.) verév- ka, f. ‘rope’. Cf. uru- below
20382:uis (1) “strength, youth'. Cf. guis, uis- (5) and uisàaió, eio. WP I, 229 (667) Gk. cf. í-phi, d. inst. pl. ‘by strength’; cf. also í-oulous, -onthos ‘youthful down": i-khór ‘lifeblood’; hi-drüo, v. ‘fix; an-ía ‘sorrow’; Lat. (acc.) vim, f. Å
20388:uis — uisg-
```


## [2026-10-16T05:17:46.305Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'vīrá-\\|virá-\\|vlra-\\|vira-, av\\|vir, viri' incoming/WLD/WLD_Bd1_pages.txt | head; grep -n -i 'violare\\|violäre\\|violo' incoming/WLD/WLD_Bd1_pages.txt | head -5",
 "description": "Grep Walde-Pokorny Bd1"
}
```


### [2026-10-16T05:17:46.727Z] TOOL RESULT

```
34100:Ubermacht", qdvlra- „stark, maehtig" (j wohl sekundar fur 7, so da6 = gall.
34176:(„*die starke", abl. mit ai. gavlra-. gall, xauaoog)        a-xvQog „ungiltig"    ;
28716:Eingeweide“), ags. tce'.o loc, weolc, ivioloc „Trompeterschnecke", ndl. uvik , loulk
63157:844); lat. ns, violare (Yaniiek 2 85, Fick I 4 38, 197  nicht mehr KZ. 44,         —
```


## [2026-10-16T05:17:49.638Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '63150,63160p' incoming/WLD/WLD_Bd1_pages.txt; grep -n 'pdf page' incoming/WLD/WLD_Bd1_pages.txt | awk -F: '$1<63157' | tail -1; grep -n -i 'u̯īro-\\|uīro-\\|ulro-\\|u\\?iro-s\\|Mann, Held' incoming/WLD/WLD_Bd1_pages.txt | head",
 "description": "Walde-Pokorny violare context"
}
```


### [2026-10-16T05:17:49.967Z] TOOL RESULT

```
benim „schlage“?); lat. vitium (Brugmann IF. 17, 367, Gdr. II 2 1, 186; sei
„Yergewaltigung, Schandung, Fehlgriff, Fehler“ und in der Bildung zuniichst
mit ai. ciji-jitya „Sieg im WettlauP, auch ji-ti-h „Sieg“, -jit „ersiegend,
erbeutend" zu vergleichen; wahrscheinlichere Deutungen bei Yf. LEWb. 2
844); lat. ns, violare (Yaniiek 2 85, Fick I 4 38, 197  nicht mehr KZ. 44,         —
329     — Prellwitz 2 77 zw., Brugmann-Thumb GrGr. 4 134; siehe aber Yf.
            ,

5877:                                             angiro-s         — anti, anta                                             65
5927:angiro-s „Bote“ ?
29872:    314                                                                     nidhu            niro-s
29977:niro-s „Mann“.
32842:                                            qabeiro-s   — qam- (qem-?)                                           349
32869:qabeiro-s „chthonische Gottergestalt".
42235:*halep-un, -mis?) in ags. hcelep „Mann, Held", as. heliih ds., ahd. Jielid
```


## [2026-10-16T05:17:55.833Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '63120,63150p' incoming/WLD/WLD_Bd1_pages.txt | cut -c1-120",
 "description": "More WLD context"
}
```


### [2026-10-16T05:17:56.173Z] TOOL RESULT

```
her (wobei /Itveiv von einem Ptc. *f5l-v6-g = ai. Jfi-na-, Gramm., abzuleiten
ware), sondern nack Liden IF. 19, 328 mit np. gCiyad „futuit“ von einer
Wz. *g ‘ai oder (?)
            l
                            die nnr bei letzterem Ansatz mit cfiei- als Dehn-
stufe der o-Abtonung allenfalls theoretiscb vereinbar ware, iibrigens auch
von *g ‘u- „gehn“ zu scheiden ist is. if'eni-); ob dazu nach Liden auch
            l



aisl.hugr „Jungstier“, ulga ,.junge Kub vom ersten Hervortreten der
                                          /,


Brunst bis zum 1. Kalben"? ig'it-qo-, -go- ,,coitui maturus, -a“?) Yon B.
bei Fick II 4 165, Zup. G. 88 nicht besser mit air. hutch „penis“ verbunden,
das freilich auch nicht nach Johansson KZ. 36, 381         S3 mit der grm.             —
Sippe von aisl. pile „Stacheh‘ zusammengehort, womit Fick III 4 218                                           y


Falk-Torp u. pig, pege, peis II auch andere Worte mit germ. Anl. pi- in
der Bed. „spitz“, und Petersson KZ. 47, 278 auch arm. picak „oxfly, wasp“
unter idg. *bdg- vermitteln will, was nicht tiberzeugt.
  Unverwandt ist mir. bine „Zerst6rung, Yerbreclien‘‘ (Fick II 4 eher zu                      ;
```


## [2026-10-16T05:18:01.100Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'uiolō\\|violo, -as\\|uiolo\\|uiolentus' LAT.txt | head -5; grep -n -i 'violo\\b\\|violare' LEW_1910.txt | head -5; echo SKT; grep -n -i '^violate\\|^violent\\|^virtue\\|^world' SKT.txt | head",
 "description": "Grep Ernout-Meillet, Walde LEW, Skeat"
}
```


### [2026-10-16T05:18:01.522Z] TOOL RESULT

```
68855:uiolo: -r.uis.
69083:A uts se rattachent: uiolentusi violent. Ancien et nsuel, avec
69085:uehenSns, uehenentiory d’oii uiolenter (ancien), uiolentia f.; inuiolentus
69087:uiolo,-Ss : violer, faire violence a, outrager. Ancien; classique.
69101:La formation de uiolentus rappelle celle de opulentus, et uiolare
SKT
20918:Violate.  (L.)  From  pp.  of  L,  uielart,  lo treat  with  force,  violate.  Formed  a«  If from  an  ailj.  uioiux*,  dne  lo  ui-s,  force.
20919:violent     (K.  -  L)      F.  violent.  -  L. uh!mtHs,  full   of  might.       Fonned  as  if Srvrn  an  adj.  uiolm  •  laboveV Violet,  a  flower.
20929:virtue.  (F.  -  U)     M.E. verfu.'^h.  uirtuttm,  acc.  of  uirtHt, excellence.  —  L,  uir.  a  man.
```


## [2026-10-16T05:18:03.682Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '69075,69105p' LAT.txt; grep -n -i '^world\\|^World' SKT.txt | head -3",
 "description": "Ernout-Meillet uis/violo text"
}
```


### [2026-10-16T05:18:04.005Z] TOOL RESULT

```
mais sans doute en raison de son caractbre monosyllabique n'a pas
surv^cu dans les 1. romanes, sauf dans le juxtapose uts maior > fr.
vimaire, terme technique du vocabulaire des eaux et forets.I 3®9
ulscus
D^riv^s en uir-, rares et tardifs ponr la plupart; uiriculae (Apul.);
uiriVsus: violent, uiridsZ (Apul., Tert., Gloss.); uirdcius dansVarr^,
ap.Non.187,is, uir uiracius, glose nagnarun uiriun. Ponr euirio,
-ri&tio, r.SuirS, sous uir.
A uts se rattachent: uiolentusi violent. Ancien et nsuel, avec
un doublet poetique 1 ii olens (Hor., Pera.) fait sur uiolentior d'aprbs
uehenSns, uehenentiory d’oii uiolenter (ancien), uiolentia f.; inuiolentus
(Cassiod. Not. Tir.).
uiolo,-Ss : violer, faire violence a, outrager. Ancien; classique.
D'o4 uioldtor, -tio (tona deux d'epoq.imp.), -trix (tardif); uiolabilis
(po^s.imp. ) et inuioldbilis (depnis Lncr. d'aprbs apiaoroc)» inuiola-
bilitds (l.Agl.); inuiolatus (class.) "invioie" et "inviolable"
(cf . inuictus), inuiolSte.
An sena de "force", la langae hom^rique a lea formes correspon-
dantes k uts: (F)Xc k ilis, (F)lv’ (devant voyelle; en r<§alit<? FXv,
an sg. ) k uin, et la forme adverbiale (F)Xcpi. (d'ob (F)Xcpi.£x en face
de ut-. Ponr F, noter la glose ytc (c.-A-d. F15), tcr^ufi.
II n'y a paa lien de considerer ici (F)tvcx "tendon", (F)uvec
"tendons". - Le sena de akr .vdyalf (thbme en -S-) «at: "force vitale,
force jeune"; ce rapprochement explique l*r de uirSs; le type utr-
n 1 existe qu'an plnriel; cf .spes, et speres. La parenti avec uir est
vraisemblable.
La formation de uiolentus rappelle celle de opulentus, et uiolare
a l'air d'nne formation expressive comme ustulare,■ sorbillare, etc.
uls: 3« p. sg. de uolo, iasne de *uei—s (i). Vts a*est introdnit
dans la conjngaiaon de uolo, parce que la ai e peraonne normale uel-si
abontissait soit k *uelle, et ae confondait avec 1'infinitif pr^sent,
```


## [2026-10-16T05:18:07.823Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; ls | grep -E '2298|0262|0334|262|334'; cat 0143.vision.txt | head -5; ls ../ | head; ls ../BOOK 2>/dev/null | tail -3",
 "description": "Check OCR cache naming"
}
```


### [2026-10-16T05:18:08.155Z] TOOL RESULT

```
[BQT vol.1 printed p.143 = archive.org borhan-ghate-v1 leaf n359; read from the page image]
Mo'in's added entry (marked ☼) in the footnote zone:
☼ اطلس - از تازی، از یونانی Atlas (نام ربّ‌النوع حامل کرهٔ زمین) «نفس». کتاب شامل نقشه‌های جغرافی - جامهٔ ابریشمی پرز دار.
(Column text above, for context: اصطرلاب - معروف است و آن آلتی باشد از برنج ... و این لغت یونانی است بمعنی ترازوی آفتاب چه اصطر ترازو ...)
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  AFM
drwxr-xr-x     - sfmqrb 14 Oct 22:47  ARY
drwxr-xr-x     - sfmqrb 14 Oct 22:19  BLY
drwxr-xr-x     - sfmqrb 16 Oct 01:17  BOOK
drwxr-xr-x     - sfmqrb 16 Oct 01:18  BQT
drwxr-xr-x     - sfmqrb 14 Oct 22:48  FFD
drwxr-xr-x     - sfmqrb 14 Oct 22:19  HRN
drwxr-xr-x     - sfmqrb 14 Oct 22:19  IRN
drwxr-xr-x     - sfmqrb 14 Oct 22:27  PLA
.rw-r--r--   45k sfmqrb 14 Oct 22:19  532.png
.rw-r--r--   61k sfmqrb 16 Oct 01:16  534.png
.rw-r--r--   71k sfmqrb 16 Oct 01:17  535.png
```


## [2026-10-16T05:18:10.973Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; /bin/ls | grep -E '2298|262|334'; /bin/ls | wc -l",
 "description": "List BQT OCR cache files"
}
```


### [2026-10-16T05:18:11.354Z] TOOL RESULT

```
2262.png
2262.txt
2262.vision.txt
2298.png
2298.txt
586
```


## [2026-10-16T05:18:13.513Z] TOOL CALL #65: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2298.png"
}
```


### [2026-10-16T05:18:14.004Z] TOOL RESULT

```

```


## [2026-10-16T05:18:14.000Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-16T05:18:32.712Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p533; pdftoppm -f 533 -l 533 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg533 && cp $S/pg533.png data/verification/sources/refs/ocr/BOOK/533.png; R=data/verification/sources/refs/ocr/BQT; cp $S/bqt533-n482.jpg $R/0262.jpg; cp $S/bqt533-n554.jpg $R/0334.jpg\ncat > $R/0262.vision.txt <<'EOF'\n[BQT vol.1 printed p.262 = archive.org borhan-ghate-v1 leaf n482; read from the page image]\nبرم - بفتح اول و ثانی بر وزن عجم ، چوب بندیرا گویند که تاک انگور و بیارهٔ کدو و خیار و امثال آن بربالایش اندازند ۱ ... و بسکون ثانی بمعنی حفظ و ازبر کردن و بیاد نگاه داشتن باشد ۳ - و تالاب و استخر و چشمهٔ آب را نیز گویند ...\nfootnote ۳ - باین معنی در پهلوی varm «اوادیا ۱۶۶».\nEOF\ncat > $R/0334.vision.txt <<'EOF'\n[BQT vol.1 printed p.334 = archive.org borhan-ghate-v1 leaf n554; read from the page image]\nبیر - بکسر اول و سکون ثانی و رای قرشت ، جامهٔ خواب را گویند ... و صاعقه و طوفان را نیز گفته اند - و بمعنی حفظ و از بر کردن هم آمده است ۲ ...\nfootnote ۲ - = ویر (حفظ ، فهم ، حافظه) ، پهلوی vîr ، vîrâk ، اوستایی ²vîra (اطلاع) «اسفا ۱: ۲ ص۲۶» درپهلوی vîrîh بمعنی خردمندی وهشیاری است . کردی wîr ومکری bîr ، fêr (آموخته و یادگرفته) . رك : ارداویرافنامه بقلم نگارنده ص ۲-۴ .\nEOF\ncat > $R/2298.vision.txt <<'EOF'\n[BQT vol.4 printed p.2298 = BQT_v4_picofile.pdf page 381; read from the page image]\nویر ۷ - بکسر اول بروزن میر ، بمعنی از بر است که ازحفظ کردن و بخاطر نگاهداشتن باشد ۸ - و بمعنی فهم وهوش و ادراک هم هست ۹ - و ناله و فریاد را نیز گویند ۱۰ ...\nfootnote ۷ - = بیر (ه.م.) = بر (ه.م.) ، قس : ویرا (ه.م.) اوستایی ²vîra (هوش) «دارمستتر. تتبعات ج ۲ ص ۱۸۳» ؛ پهلوی vîr ، vîrâk (ویرا) ، کردی bîr (حافظه) ، بلوچی gîr (حافظه ، تذکار) «اسشق ۱۰۸۶» . رك : بیر . - ولف «ویر» را درشاهنامه بمعنی هوش وحافظه آورده: اورامانی wîr (یاد ، حافظه) ... دراراك (سلطان آباد) vîr-om nîst (نظرم نیست ، فراموش کرده ام).\nEOF\nls -la data/verification/sources/refs/ocr/BOOK/533.png",
 "description": "Save page images and vision transcripts"
}
```


### [2026-10-16T05:18:34.976Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   35k sfmqrb 16 Oct 01:18  data/verification/sources/refs/ocr/BOOK/533.png
```


## [2026-10-16T05:20:08.162Z] TOOL CALL #67: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p533/build533.py <<'PYEOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nU_vir=W+\"ویر\"; U_pir=W+\"Reconstruction:Proto-Iranian/wiHr̥Háh\"; U_pie=W+\"Reconstruction:Proto-Indo-European/wiHrós\"\nU_pirm=W+\"Reconstruction:Proto-Iranian/wiHráh\"; U_violo=W+\"violo\"; U_world=W+\"world\"; U_virtus=W+\"virtus\"\nU_abv=\"https://abadis.ir/fatofa/ویر/\"; U_abb=\"https://abadis.ir/fatofa/برم/\"\nPOK1123={\"ref\":\"POK:1123\",\"status\":\"supports\",\"note\":\"POK_full.txt 'Page(s): 1123-1124', root 'uei-3, ueiə- : uī-' 'to reach towards smth., to pursue or wish smth.; to be strong': 'Avestan ... vay- (vayeiti, vīvāiti chases away, 3. Pl. vyeinti) pursue, hunt, chase, vyāna- the victim of persecution, vōiϑwa- ... vītar- pursuer, vātay- pursuit'; also 'Latin ... vīs, vim power, force'; ends 'compare also uīro-s man'.\"}\nPOK1177={\"ref\":\"POK:1177\",\"status\":\"supports\",\"note\":\"POK_full.txt 'Page(s): 1177-1178', 'uīro-s man; warrior': 'Old Indic vīra-, Avestan vīra- man, hero ... Latin vir man ..., virtus manfulness ... virtue ... Old English wer man ... probably to Latin vīs power etc., *ueiə- auf etwas losgehen'.\"}\nAHDw={\"src\":\"AHD\",\"where\":\"Watkins 1985 p.74-75 s.v. weiə- and wi-ro-\",\"stance\":\"supports\",\"note\":\"'weiə-. Vital force. Perhaps related to wi-ro-. Zero-grade form *wi- in Latin vīs, force, with irregular derivatives violāre, to treat with force, and violentus ... [In Pok. 3. wei- 1123.]'; 'wi-ro-. Man. Derivative of weiə-? ... *wer-ald- \\\"life or age of man\\\" in Old English weorold, world ... Latin vir, man: ... VIRTUE ... [Pok. wiro-s 1177.]'\"}\nKLNv={\"ref\":\"KLN:1714\",\"status\":\"supports\",\"note\":\"KLN_1971.txt s.v. virile (1966 two-vol. leaf for p.1714 not cleanly OCR'd): 'cogn. with OI. vīrāḥ, Avestic vīra-, ... OE. wer ... man. These words prob. meant orig. \\\"the strong one\\\", and derive fr. I.-E. base *wi-ro-, enlargement of base *wei-, \\\"to be strong\\\", whence L. vīs ... cp. ... virtue, werewolf, world.'\"}\nnodes=[]\nnodes.append(dict(id=1,lang=\"Avestan\",words=\"vîra\",verdict=\"plausible\",\n derivation=\"Av. vīra- m. 'man, (warrior) hero' (Bartholomae col. 1453 ¹vīra-) < Proto-Iranian *wiHráh < PIIr. *wiHrás < PIE *wiHrós 'man', cognate with Skt. vīrá-, Lat. vir, Lith. výras, OE wer: the word and its root are correct. But the gloss '(his mind)' conflates it with a homonym: Bartholomae (col. 1454) lists a separate ²vīra- 'Verstand, Einsicht' (→ NP vīr), which modern work (Wiktionary, after Asatrian/Bailey) reconstructs as PIr. *wiHr̥Háh 'memory, mind' (perhaps *wi- + *Hr̥Ha- 'thinking'), unrelated to *wiHráh 'man'. So vīra 'man' is confirmed under this root; vīra 'mind' is not.\",\n derivation_fa=\"اوستایی vīra- «مرد، دلاور» از ایرانی باستان *wiHra- و هندواروپایی آغازین *wiHrós است و با سنسکریت vīra- و لاتین vir هم‌ریشه است؛ این بخش ادعای نورایی درست است. اما افزودن معنای «اندیشه/هوش» در پرانتز آمیختن دو واژهٔ هم‌آوا است: بارتولومه در ستون ۱۴۵۴ واژهٔ جداگانهٔ ²vīra- «فهم، دریافت» را آورده که «ویر» فارسی از آن است و پژوهش امروزی آن را از *wiHr̥Ha- «یاد، ذهن» می‌داند، نه از «مرد». پس این گره با احتیاط پذیرفتنی است.\",\n sources=[U_pirm,U_pie,U_pir],\n ref_check=[dict(POK1177),{\"ref\":\"KLN:1714\",\"status\":\"supports\",\"note\":\"KLN_1971 s.v. virile lists 'Avestic vīra-' among cognates of L. vir 'man' (base *wi-ro-); says nothing about a 'mind' sense.\"}],\n consulted=[{\"src\":\"BRT\",\"where\":\"col. 1453-1454 (BRT.txt l.24276-24281)\",\"stance\":\"partial\",\"note\":\"¹vīra- m. 'Mann' ('mp. vīr, np. vīr' in sense 'man' in compounds) and separately '²vīra- n. Verstand, Einsicht ... np. vīr; Dst. Étr. 2.183' — two distinct words.\"},\n  {\"src\":\"IEC\",\"where\":\"l.20378 s.v. uiros\",\"stance\":\"supports\",\"note\":\"'uiros man, husband, hero. WP I, 314 Skt. vīráh man, hero; Av. vīrō man; ... Lat. vir'\"},\n  {\"src\":\"SYN\",\"where\":\"2.21 MAN (SYN.txt l.2281-2289)\",\"stance\":\"supports\",\"note\":\"'IE *wiro-, that is, *wī-ro- : Lat. vīs, Skt. vayas ... strength' with 'Av. vīra-'\"},\n  dict(AHDw)]))\nnodes.append(dict(id=2,lang=\"Pahlavi\",words=\"vîr; varm 2; varm kartan\",verdict=\"disputed\",\n derivation=\"MP wīr [wyl] 'memory, mind, reason' is real (MacKenzie: ²wīr 'memory, mind', N bīr; Nyberg: ²vīr 'a mental faculty, reason, intellect — Av. ²vīra-') and continues Av. ²vīra- 'understanding', PIr. *wiHr̥Háh; it is a homonym of ¹wīr 'man, hero' and not derived from *wiHrós 'man', so the placement under root Wei 2/Wiros is disputed. MP warm [wlm] 'memory' (MacKenzie, N barm), warm kardan 'to learn by heart' (Bailey ZAP: 'zand varm', 'varm kart' = memorized) is a different word altogether: Bailey derives it from *varma- to the base var- 'choose' (Pagliaro/Bartholomae from Av. vārəzma); it cannot come from vīra- (no w-ī-r → w-a-r-m development).\",\n derivation_fa=\"پهلوی wīr «یاد، هوش، خرد» واژه‌ای درست است (مکنزی، نیبرگ) و از اوستایی ²vīra- «فهم» می‌آید، ولی این واژه با wīr «مرد، پهلوان» تنها هم‌آواست و از ریشهٔ «مرد» نیست. پهلوی warm «حافظه» و warm kardan «از بر کردن» واژه‌ای جداگانه است که بیلی (همان منبع نورایی) آن را از *warma- از ریشهٔ var- «برگزیدن» می‌داند؛ پیوند آن با vīra ناممکن است. پس پژوهش امروزی ادعای نورایی را در این گره رد می‌کند.\",\n sources=[U_pir,U_vir],\n ref_check=[{\"ref\":\"BQT:334\",\"status\":\"partial\",\"note\":\"BQT vol.1 p.334 (leaf n554, ocr/BQT/0334.vision.txt) s.v. بیر 'بمعنی حفظ و از بر کردن'; Mo'in fn.2: '= ویر ... پهلوی vîr، vîrâk، اوستایی ²vîra (اطلاع) ... درپهلوی vîrîh بمعنی خردمندی' — supports Pahlavi vīr from Av. ²vīra (the 'mind' word), not from vīra 'man'; says nothing of varm.\"},\n  {\"ref\":\"ZAP:159\",\"status\":\"contradicts\",\"note\":\"ZAP.txt l.4978-4982 (Bailey, Zoroastrian Problems): 'varom ... Pagliaro ... considers it as taken from Av. vārəzma \\\"at will\\\", as Bartholomae ... had done. But it is preferable to derive varom from *varma- to the base var- \\\"choose\\\"'; l.7735-7758 'zand varm', 'ne varm kart \\\"who has not memorized the gathas\\\"'. Confirms the words, contradicts a vīra origin for varm.\"}],\n consulted=[{\"src\":\"PHD\",\"where\":\"PHD_mackenzie.txt l.5208, 5399-5400\",\"stance\":\"partial\",\"note\":\"'¹warm [wlm | N barm] memory'; '¹wīr [wyl] man, hero'; '²wīr [wyl | M wyr-, N bīr] memory, mind' — memory-wīr kept separate from man-wīr.\"},\n  {\"src\":\"NYB\",\"where\":\"vol.2 glossary p.213, l.4171-4175\",\"stance\":\"partial\",\"note\":\"'¹vīr [wyl] man ... Av. (1453) vīra-'; '²vīr [wyl] a mental faculty, reason, intellect ... Av. (1454) ²vīra-'.\"},\n  {\"src\":\"BRT\",\"where\":\"col. 1454\",\"stance\":\"partial\",\"note\":\"'²vīra- n. Verstand, Einsicht ... np. vīr'\"}]))\nnodes.append(dict(id=3,lang=\"Persian\",words=\"vîr; bar 1\",verdict=\"disputed\",\n derivation=\"NP vīr ویر (also bīr بیر) 'memory, understanding' (Ferdowsi: 'bigoft nāmaš nadānam be vīr') < MP wīr < Av. ²vīra- / PIr. *wiHr̥Háh 'memory, mind' (Horn no.1086, Mo'in, Wiktionary): the Pahlavi→Persian step is correct, but the word is not from *wiHrós 'man', so its place under this root is disputed. NP bar/barm بر/برم 'by heart' (az bar kardan 'to memorize') < MP warm 'memory' with regular initial w- > b- (cf. warf > barf) and loss of final -m in bar; it is unrelated to vīr (see node 2).\",\n derivation_fa=\"«ویر» (بیر) فارسی به معنی «یاد، هوش» از پهلوی wīr و آن از اوستایی ²vīra- «فهم» است (هرن شمارهٔ ۱۰۸۶، معین، ویکی‌واژه)؛ این گام درست است ولی واژه از ریشهٔ «مرد» (*wiHrós) نیست. «بر/برم» در «از بر کردن» از پهلوی warm «حافظه» است که در آن w آغازین به b بدل شده (مانند warf → برف)؛ این واژه با «ویر» هم‌ریشه نیست. پس جای دادن این دو در زیر ریشهٔ Wei/Wiros را پژوهش امروزی رد می‌کند.\",\n sources=[U_vir,U_pir,U_abv,U_abb],\n ref_check=[{\"ref\":\"BQT:2298\",\"status\":\"partial\",\"note\":\"BQT vol.4 p.2298 (ocr/BQT/2298.vision.txt) ویر 'بمعنی از بر است که ازحفظ کردن و بخاطر نگاهداشتن باشد - و بمعنی فهم وهوش و ادراک'; Mo'in fn.7: '= بیر = بر ... اوستایی ²vîra (هوش) دارمستتر ... پهلوی vîr، vîrâk، کردی bîr ... بلوچی gîr' — supports vīr < Av. ²vīra 'intelligence' (not 'man'); Mo'in equates بر with ویر, which Nourai follows.\"},\n  {\"ref\":\"BQT:262\",\"status\":\"partial\",\"note\":\"BQT vol.1 p.262 (leaf n482, ocr/BQT/0262.vision.txt) برم 'و بسکون ثانی بمعنی حفظ و ازبر کردن و بیاد نگاه داشتن'; fn.3 'باین معنی در پهلوی varm' — supports barm < Pahlavi varm, nothing about vīra.\"},\n  {\"ref\":\"MON:489\",\"status\":\"partial\",\"note\":\"Mo'in, Farhang-e Farsi via abadis.ir (page not mappable): ویر '[په.] ۱- هوش، فهم. ۲- یاد، ذهن'; برم entry gives Dehkhoda 'حفظ و از بر کردن' — confirms meanings and Pahlavi origin, no root claim.\"},\n  {\"ref\":\"ZAP:159\",\"status\":\"contradicts\",\"note\":\"Bailey derives varm (> NP barm/bar) from *varma-, base var- 'choose' (ZAP.txt l.4982), not from vīra.\"}],\n consulted=[{\"src\":\"HRN\",\"where\":\"no. 1086 (HRN.txt l.9403-9410)\",\"stance\":\"partial\",\"note\":\"'vīr Sinn, Verstand; Gedächtniss ... aw. *vīra- \\\"Einsicht\\\" (Darmesteter, Et. ir. II, 183); phlv. vīr, vīrāk ... kurd. bīr; bal. gīr' — separate from vīra 'man'.\"},\n  {\"src\":\"ARY\",\"where\":\"ARY_latin_index_pages.txt [pdf page 524]\",\"stance\":\"supports\",\"note\":\"Aryanpur lists under the 'man' root 'VIRA (AVESTAN)', 'WIR, WIROMANDIH (PAHLAVI)', 'BIR (KURDISH)', 'GIR (BALUCHI)', 'MACKENZIE: (MEMORY) 123, (MIND) 124' — same conflation as Nourai.\"},\n  {\"src\":\"HUB\",\"where\":\"HUB.txt grep vīr/barm\",\"stance\":\"silent\",\"note\":\"no entry for vīr or barm found.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"CHEUNG.txt\",\"stance\":\"silent\",\"note\":\"nouns, not verbs; no entry.\"}]))\nnodes.append(dict(id=4,lang=\"Avestan\",words=\"vôi, vây 2, vîvâiti, vayeiti 2; vyâna 1; vâtay; vîtar 1; vôi-thwa\",verdict=\"confirmed\",\n derivation=\"Av. vay- 'to hunt, chase, pursue' (pres. vaiieiti, reduplicated vīuuāiti, 3pl. vīieinti; inf. vōi) < PIr. *waj(H)- < PIE *weyh₁- 'go after, pursue' (Skt. véti, Lith. výti, Lat. invītāre); derivatives vyāna- 'the pursued, persecuted one', vātay- f. 'pursuit, persecution' (a punishable offence), vītar- 'pursuer', vōiϑwa- gerundive 'to be chased'. All forms and glosses match Bartholomae and Pokorny's u̯ei-3. The chart shows no Persian descendant (empty box).\",\n derivation_fa=\"فعل اوستایی vay- «دنبال کردن، شکار کردن» (vaiieiti، vīvāiti) از هندواروپایی آغازین *weyh₁- «به دنبال چیزی رفتن» است و با سنسکریت véti و لیتوانیایی výti هم‌ریشه است؛ vyāna- «تعقیب‌شده»، vātay- «تعقیب، آزار»، vītar- «تعقیب‌کننده» و vōiϑwa- «تعقیب‌شدنی» مشتقات آن‌اند. بارتولومه و پوکورنی همه را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n sources=[U_violo],\n ref_check=[dict(POK1123)],\n consulted=[{\"src\":\"BRT\",\"where\":\"BRT.txt l.23432-23436, 23462, 23978\",\"stance\":\"supports\",\"note\":\"'vā(y)- V. \\\"jagen\\\". Praes. vaya-, vya- — PFP. vōiϑwa: \\\"jagen, jagend verfolgen\\\" ... vyqsca vyānasca'; 'vātay- f. \\\"Verfolgung\\\", Bezeichnung eines strafbaren Delikts'; 'vītar- m. \\\"der nachjagt, Verfolger\\\"'.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wei-² 'To go after something' [Pok. 3. wei- 1123]\",\"stance\":\"supports\",\"note\":\"same Pokorny root; Germanic *waithanjan 'to hunt'.\"},\n  {\"src\":\"IEC\",\"where\":\"IEC.txt s.v. uis (1)\",\"stance\":\"partial\",\"note\":\"'uis (1) strength, youth ... Lat. (acc.) vim' — Mann treats the 'strength' word, no Avestan vay-.\"}]))\nnodes.append(dict(id=5,lang=\"Germanic\",words=\"weraldh\",verdict=\"confirmed\",\n derivation=\"Proto-Germanic *weraldiz 'age/lifetime of man, world', compound of *weraz 'man' (< PIE *wiHrós, Germanic e from i before r) + *aldiz 'age' (cf. OE ield, ON ǫld); AHD writes it *wer-ald- 'life or age of man'. Nourai's 'weraldh' is a loose notation of this compound.\",\n derivation_fa=\"ژرمنی آغازین *weraldiz «روزگار آدمی، جهان» ترکیبی است از *weraz «مرد» (از *wiHrós) و *aldiz «عمر، دوران»؛ واتکینز (AHD) آن را *wer-ald- «زندگی یا روزگار مرد» می‌نویسد. ادعای نورایی درست است.\",\n sources=[U_world],\n ref_check=[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. wi-ro-: 'Germanic compound *wer-ald-, \\\"life or age of man\\\" (*-ald-, age; see al-3), in Old English weorold, world: WORLD'.\"}],\n consulted=[{\"src\":\"KLN\",\"where\":\"KLN_1971 s.v. world\",\"stance\":\"supports\",\"note\":\"'The first element ... is rel. to OE. wer ... man; see virile. The second element is rel. to ON. old, mankind, aldr, age ... OE. weoruld lit. mean \\\"the age of man\\\"'.\"},\n  {\"src\":\"POK\",\"where\":\"p.1177-1178\",\"stance\":\"supports\",\"note\":\"'Old English wer man' under uīro-s.\"},\n  {\"src\":\"IEC\",\"where\":\"s.v. uiros\",\"stance\":\"supports\",\"note\":\"'Go. wair, OE wer ... ON verr'\"}]))\nnodes.append(dict(id=6,lang=\"English\",words=\"world\",verdict=\"confirmed\",\n derivation=\"English world < ME world, weoreld < OE weorold, woruld 'world, age, mankind' < PWGmc *weraldi < PGmc *weraldiz 'age of man' (node 5); the OE sense shift 'human lifespan/age' → 'human existence' → 'the earth and its people' parallels Latin saeculum.\",\n derivation_fa=\"انگلیسی world از انگلیسی میانه weoreld و انگلیسی کهن weorold «روزگار، جهان» و آن از ژرمنی *weraldiz «روزگار آدمی» است؛ معنا از «عمر آدمی» به «جهان مردمان» گسترش یافته است. ادعای نورایی درست است.\",\n sources=[U_world],\n ref_check=[{\"ref\":\"(none)\",\"status\":\"not_checked\",\"note\":\"node has no refs; checked via parent AHD and Klein.\"}],\n consulted=[{\"src\":\"KLN\",\"where\":\"KLN_1971 s.v. world\",\"stance\":\"supports\",\"note\":\"'world, n. — ME. weoreld, weorld, fr. OE. weoruld, woruld, \\\"world, age\\\"'\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt grep '^world'\",\"stance\":\"silent\",\"note\":\"headword not found in OCR.\"}]))\nnodes.append(dict(id=7,lang=\"Latin\",words=\"vir; violere\",verdict=\"transcription_suspect\",\n derivation=\"Lat. vir 'man' < PIE *wiHrós (Pokorny 1177, AHD wi-ro-): confirmed. The second form is printed 'violere' in the book; the Latin verb is violāre (1st conj., violō, -āre) 'to treat with force, violate', derived from vīs 'force' (traditionally via an adj. *violus; de Vaan from *weyh₁-elos), with violentus 'forcible'. The book misprints the infinitive ending; the extraction is faithful. Ernout-Meillet judge the kinship of vīs with vir 'vraisemblable', so grouping both under one root follows AHD/Klein but is not certain.\",\n derivation_fa=\"لاتین vir «مرد» از *wiHrós است و درست است. صورت دوم در کتاب «violere» چاپ شده، ولی فعل لاتین violāre «به زور رفتار کردن، تجاوز کردن» است که از vīs «زور» ساخته شده؛ این خطای چاپی کتاب است و استخراج درست انجام شده. ارنو و میه خویشاوندی vīs و vir را «محتمل» می‌دانند، پس گروه‌بندی نورایی با احتیاط پذیرفتنی است.\",\n error_in=\"book\",book_prints=\"violere\",correct_form=\"violāre\",\n sources=[U_violo,U_virtus,U_pie],\n ref_check=[dict(AHDw,ref=\"AHD\",status=\"supports\") if False else {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985: 'Latin vīs, force, with irregular derivatives violāre, to treat with force, and violentus' (weiə-); 'Latin vir, man' (wi-ro-).\"},\n  {\"ref\":\"POK:1123,1177\",\"status\":\"supports\",\"note\":\"p.1123 'Latin ... vīs, vim power, force'; p.1177 'Latin vir man ... virtus'. violāre itself not named in the OCR.\"}],\n consulted=[{\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. uīs (LAT.txt l.69083-69101)\",\"stance\":\"supports\",\"note\":\"'A uīs se rattachent: uiolentus violent ...; uiolo, -ās: violer, faire violence à ... La parenté avec uir est vraisemblable.'\"},\n  {\"src\":\"WLD\",\"where\":\"Bd. I (WLD_Bd1_pages.txt l.63157)\",\"stance\":\"partial\",\"note\":\"cites 'lat. vīs, violāre' (referring to Walde LEW) as unrelated to the root under discussion; main u̯ei- entry not located in OCR.\"},\n  {\"src\":\"IEC\",\"where\":\"s.v. uiros, uis (1)\",\"stance\":\"supports\",\"note\":\"'Lat. vir, gs. -i, m. man'; 'Lat. (acc.) vim'\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt l.20918\",\"stance\":\"supports\",\"note\":\"'Violate. From pp. of L. uiolāre, to treat with force ... Formed as if from an adj. uiolus*, due to uī-s, force.'\"}]))\nnodes.append(dict(id=8,lang=\"English\",words=\"virtue; violent\",verdict=\"confirmed\",\n derivation=\"virtue < ME vertu < OF vertu < Lat. virtūtem, acc. of virtūs 'manliness, valour, excellence' (vir + abstract suffix -tūs); the moral sense developed in Latin and Christian usage. violent < ME < OF violent < Lat. violentus 'forcible, vehement', related to violāre / vīs 'force'.\",\n derivation_fa=\"virtue از فرانسهٔ کهن vertu و لاتین virtūs «مردانگی، دلیری، فضیلت» (از vir «مرد» + پسوند -tūs) است؛ violent از لاتین violentus «زورمند، تند» و هم‌خانواده با violāre و vīs «زور» است. ادعای نورایی درست است.\",\n sources=[U_virtus],\n ref_check=[{\"ref\":\"(none)\",\"status\":\"not_checked\",\"note\":\"node has no refs; checked via parent AHD/Klein.\"}],\n consulted=[{\"src\":\"KLN\",\"where\":\"KLN_1971 s.v. virtue, violent\",\"stance\":\"supports\",\"note\":\"'virtue ... fr. L. virtūtem, acc. of virtūs, \\\"virtue\\\", lit. \\\"manliness, manhood\\\", fr. vir'; 'violent ... fr. L. violentus, \\\"forcible, vehement, violent\\\", which is rel. to violāre'\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt l.20919, 20929\",\"stance\":\"supports\",\"note\":\"'violent (F.-L.) F. violent - L. violentus, full of might'; 'virtue ... L. uirtūtem ... L. uir, a man'\"}]))\nentry=dict(entry=0,root=\"Wei 2, Wiros\",verdict=\"plausible\",\n modern_form=\"PIE *wiHrós 'man' (Pok. uīro-s 1177); PIE *weyh₁- 'go after, pursue; be strong' / *wéyHs 'force' (Pok. u̯ei-3 1123; AHD weiə- 'vital force')\",\n note=\"The box merges two Pokorny roots, as Watkins does (weiə- 'vital force' with *wi-ro- 'man' as 'derivative of weiə-?'); Pokorny himself only says uīro-s is 'probably' related to vīs. Modern opinion (Wiktionary) lists several theories for *wiHrós (from *weyh₁- 'hunt', from *wéyHs 'force', or other), so the merger is plausible but not certain. The Latin, Germanic, English and Avestan vay- branches are sound. The Iranian 'memory' branch (Pahlavi wīr, varm; NP vīr, bar/barm) is wrong for this root: vīr 'memory' continues Av. ²vīra- 'understanding' (Bartholomae, Horn, Mo'in), a homonym of vīra 'man', and varm/barm is a separate word (Bailey: *varma-, base var- 'choose'). Book misprints Latin violāre as 'violere'.\",\n note_fa=\"ریشهٔ هندواروپایی آغازین *wiHrós «مرد» (پوکورنی ۱۱۷۷) و *weyh₁- «به دنبال رفتن، نیرومند بودن» (پوکورنی ۱۱۲۳) را نورایی مانند واتکینز یکی گرفته است؛ پوکورنی تنها پیوند آن دو را «محتمل» می‌داند و ویکی‌واژه چند نظریه برمی‌شمارد، پس ریشه با احتیاط پذیرفتنی است. شاخه‌های لاتین، ژرمنی، انگلیسی و فعل اوستایی vay- درست‌اند، ولی «ویر» فارسی (یاد، هوش) از اوستایی ²vīra- «فهم» است که با vīra «مرد» تنها هم‌آواست، و «بر/برم» (از بر کردن) از پهلوی warm است که بیلی آن را از ریشهٔ var- «برگزیدن» می‌داند؛ پژوهش امروزی این شاخه را رد می‌کند. «violere» در کتاب خطای چاپی برای violāre است.\",\n sources=[U_pie,U_pirm,U_pir,U_violo],\n ref_check=[dict(POK1123),dict(POK1177),dict(KLNv)],\n consulted=[dict(AHDw),{\"src\":\"IEC\",\"where\":\"l.20378 uiros; l.20382 uis (1)\",\"stance\":\"supports\",\"note\":\"'uiros man, husband, hero. WP I, 314'; 'uis (1) strength, youth ... WP I, 229'\"},\n  {\"src\":\"SYN\",\"where\":\"2.21 MAN\",\"stance\":\"supports\",\"note\":\"'IE *wiro-, that is, *wī-ro- : Lat. vīs, Skt. vayas ... strength. Walde-P. 1.(228) ff.'\"},\n  {\"src\":\"WLD\",\"where\":\"Bd. I 228 ff., 314 (cited by POK/SYN)\",\"stance\":\"silent\",\"note\":\"entries not located in the noisy OCR of WLD_Bd1_pages.txt.\"},\n  {\"src\":\"LAT\",\"where\":\"s.v. uīs\",\"stance\":\"partial\",\"note\":\"'La parenté avec uir est vraisemblable.'\"}],\n nodes=nodes)\nout=dict(pdf_page=533,book_page=503,verified_by=\"claude-opus-5\",verified_on=\"2026-10-16\",entries=[entry])\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-533.json','w'),ensure_ascii=False,indent=1)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p533/build533.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-533.json >/dev/null && cd /home/sfmqrb/git/rishe-private && python3 tools/verify_check.py 533",
 "description": "Build page-533 JSON and run checker"
}
```


### [2026-10-16T05:20:08.782Z] TOOL RESULT

```
nodes verified: 8/8
node verdicts: {'plausible': 1, 'disputed': 2, 'confirmed': 4, 'transcription_suspect': 1}
root verdicts: {'plausible': 1}
ref checks: {'supports': 6, 'partial': 4, 'contradicts': 2, 'not_checked': 2}
books consulted: {'partial': 7, 'supports': 15, 'silent': 3} | by book: {'IEC': 4, 'BRT': 3, 'KLN': 3, 'SKT': 3, 'AHD': 2, 'SYN': 1, 'PHD': 1, 'NYB': 1, 'HRN': 1, 'ARY': 1, 'HUB': 1, 'CHEUNG': 1, 'POK': 1, 'LAT': 1, 'WLD': 1}
```


## [2026-10-16T05:20:18.029Z] TOOL CALL #68: SubagentHandback

```json
{
 "message": "Page 533 (book p.503) is verified and written to /home/sfmqrb/git/rishe-private/data/verification/page-533.json. `verify_check.py 533` reports 0 PROBLEM lines and all 8 of 8 nodes verified.\n\nVerdicts for the one real entry, Wei 2 / Wiros (the \"Weib\" entry is only a redirect to Weip and was skipped):\n- **Root:** plausible. The chart treats PIE *wiHrós \"man\" (Pokorny 1177) and *weyh₁- \"go after; vital force\" (Pokorny 1123) as one root, as Watkins/AHD does. Pokorny and Ernout-Meillet only call the link \"probable\", and Wiktionary lists rival theories.\n- **Nodes:** 4 confirmed (Avestan vay- family, Germanic *weraldiz, English world, English virtue/violent), 1 plausible, 2 disputed, 1 transcription_suspect.\n- **Plausible, #1 Avestan vīra:** the word \"man\" is correct, but the gloss \"(his mind)\" mixes in a different word that only sounds the same. Bartholomae lists it separately as ²vīra- \"Verstand\", col. 1454.\n\nDisputed:\n- **#2 Pahlavi vīr; varm; varm kartan.** Pahlavi wīr \"memory, mind\" comes from Avestan ²vīra- \"understanding\" (Proto-Iranian *wiHr̥Háh), not from vīra \"man\"; MacKenzie and Nyberg keep the two apart. varm \"memory\" is a separate word: Bailey, whom Nourai himself cites (ZAP), derives it from *varma- (base var- \"choose\"). That source contradicts the chart.\n- **#3 Persian vīr «ویر», bar/barm «بر/برم».** The step from Pahlavi to Persian is correct (Horn no. 1086, Mo'in's notes in Borhan pp. 334 and 2298), but vīr \"memory\" does not belong under this root. bar/barm comes from Pahlavi warm and is unrelated to vīr.\n\nTranscription_suspect:\n- **#7 Latin \"violere\".** The fault is in the book, which prints \"violere\"; the correct form is violāre. Latin vir is confirmed.\n\nNo extraction errors: the JSON matches the printed page.\n\nAlso saved: Mo'in's footnotes, read from the page images, at `data/verification/sources/refs/ocr/BQT/0262.vision.txt`, `0334.vision.txt` and `2298.vision.txt` (with the page images). The book page image is at `ocr/BOOK/533.png`. Etymonline returned 403 and is not cited."
}
```


### [2026-10-16T05:20:18.334Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
