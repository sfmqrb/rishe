# Verification process log — verify-page-562


## [2026-10-17T00:30:14.252Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 562 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-562.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-562.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-562.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 562` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:30:14.296Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:30:18.604Z] TOOL CALL #1: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md; echo ====; cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-562.txt; echo ====; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-562.json",
 "description": "Read instructions, chart text, and source JSON"
}
```


### [2026-10-17T00:30:18.962Z] TOOL RESULT

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


## [2026-10-17T00:30:22.330Z] TOOL CALL #2: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/agent; awk 'NR>=50 && NR<=140' AGENT_INSTRUCTIONS.md",
 "description": "Read truncated middle of instructions"
}
```


## [2026-10-17T00:30:23.103Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-562.txt; echo; echo =====; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-562.json",
 "description": "Read chart text and source JSON"
}
```


### [2026-10-17T00:30:23.625Z] TOOL RESULT

```
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


### [2026-10-17T00:30:23.775Z] TOOL RESULT

```
Exit code 1
=== PDF page 562 (book page 532) ===
--- entry 0 ---
ROOT [Semitic / Hebrew] Yârâh : he threw, cast  (refs KLN:828)
#1 (parent #0) [Hebrew] refs=KLN:828 | yârah, yerŭ : foundation, base, city ; yerŭ-šâla'yim : city of peace ☞S.l.m
  #2 (parent #1) [Persian] refs=MON5:195; IRN:28 | Ûršalîm «اورشليم» : "city of peace", Jerusalem ; Ûrmîyeh «اورمیه» : "city of water", a city north of Iran
#3 (parent #0) [Arabic] refs=ARB:32 | al-avâra : place, location
  #4 (parent #1) [English] refs=KLN:828 | Jerusalem
--- entry 1 ---
ROOT [Hebrew] Yâšfa, Yâšfeh : an opaque variety of quartz  (refs BQT:2434; KLN:826)
#1 (parent #0) [Arabic] refs=BQT:2434 | yašb : a kind of quartz
  #2 (parent #1) [Persian] refs=BQT:2434 | yašm «یشم» : a grayish green quartz | extra: یشپ ، یشمی
#3 (parent #0) [Greek] refs=KLN:826 | iaspis
  #4 (parent #3) [Latin] refs=KLN:826 | iaspis
    #5 (parent #4) [Old French] refs=KLN:826 | jaspe, jaspre
      #6 (parent #5) [Middle English] refs=KLN:826 | iaspre, jaspre
        #7 (parent #6) [English] refs=KLN:826 | jasper 2 : a kind of quartz
--- entry 2 ---
ROOT Yâšfeh -> redirect to Yâšfa
--- entry 3 ---
ROOT [Indo-Schythian] Yau, Gyŭna : Yau: move, movement; Gyŭna: gait (of a lion or horse)  (refs ISS:91)
#1 (parent #0) [Old Persian] refs=ISS:91; KNT:204 | yauviya : channel (to move water)
  #2 (parent #1) [Pahlavi] refs=BQT:602 | yôî, jôî : stream
    #3 (parent #2) [Persian] refs=ISS:91; BQT:602 | jŭ «جو۱ ، جوی۱ ، جوب» : stream ; jŭy-bâr «جویبار» : river bank ☞Per 2
#4 (parent #0) [Avestan] refs=ISS:91 | yaona : movement
  #5 (parent #4) [Sogdian] refs=SOD:450 | ywn : place
--- entry 4 ---
ROOT [Avestan] Yâvarenâ : a stone or tool for beating and crushing grains  (refs HRN:252)
#1 (parent #0) [Persian] refs=BQT:2422 | yâvar «یاور» : stone or other objects used for crushing grains

(eval):1: ==== not found
```


## [2026-10-17T00:30:29.301Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/agent; awk 'NR>=140 && NR<=175' AGENT_INSTRUCTIONS.md; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-562.json; cat /home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md | head -80",
 "description": "Read rest of instructions, JSON, source matrix"
}
```


### [2026-10-17T00:30:29.583Z] TOOL RESULT

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
{
  "pdf_page": 562,
  "book_page": 532,
  "entries": [
    {
      "root": {
        "name": "Yârâh",
        "lang": "Semitic / Hebrew",
        "refs": "KLN:828",
        "gloss": "he threw, cast"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:828",
          "words": [
            {"translit": "yârah, yerŭ", "gloss": "foundation, base, city", "script": null},
            {"translit": "yerŭ-šâla'yim", "gloss": "city of peace", "script": null, "see": ["S.l.m"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON5:195; IRN:28",
          "words": [
            {"translit": "Ûršalîm", "gloss": "\"city of peace\", Jerusalem", "script": "اورشليم"},
            {"translit": "Ûrmîyeh", "gloss": "\"city of water\", a city north of Iran", "script": "اورمیه"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Arabic",
          "refs": "ARB:32",
          "words": [
            {"translit": "al-avâra", "gloss": "place, location", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "English",
          "refs": "KLN:828",
          "words": [
            {"translit": "Jerusalem", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Yâšfa, Yâšfeh",
        "lang": "Hebrew",
        "refs": "BQT:2434; KLN:826",
        "gloss": "an opaque variety of quartz"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "BQT:2434",
          "words": [
            {"translit": "yašb", "gloss": "a kind of quartz", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2434",
          "words": [
            {"translit": "yašm", "gloss": "a grayish green quartz", "script": "یشم"}
          ],
          "script_extra": "یشپ ، یشمی",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:826",
          "words": [
            {"translit": "iaspis", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Latin",
          "refs": "KLN:826",
          "words": [
            {"translit": "iaspis", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Old French",
          "refs": "KLN:826",
          "words": [
            {"translit": "jaspe, jaspre", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Middle English",
          "refs": "KLN:826",
          "words": [
            {"translit": "iaspre, jaspre", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "KLN:826",
          "words": [
            {"translit": "jasper 2", "gloss": "a kind of quartz", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Yâšfeh",
        "redirect": "Yâšfa"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Yau, Gyŭna",
        "lang": "Indo-Schythian",
        "refs": "ISS:91",
        "gloss": "Yau: move, movement; Gyŭna: gait (of a lion or horse)"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "ISS:91; KNT:204",
          "words": [
            {"translit": "yauviya", "gloss": "channel (to move water)", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:602",
          "words": [
            {"translit": "yôî, jôî", "gloss": "stream", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "ISS:91; BQT:602",
          "words": [
            {"translit": "jŭ", "gloss": "stream", "script": "جو۱ ، جوی۱ ، جوب"},
            {"translit": "jŭy-bâr", "gloss": "river bank", "script": "جویبار", "see": ["Per 2"]}
          ],
          "note": null,
          "quote": {"text": "بوی جوی مولیان آید همی - یاد یار مهربان آید همی", "poet": "Rŭdakî"}
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "ISS:91",
          "words": [
            {"translit": "yaona", "gloss": "movement", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Sogdian",
          "refs": "SOD:450",
          "words": [
            {"translit": "ywn", "gloss": "place", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Yâvarenâ",
        "lang": "Avestan",
        "refs": "HRN:252",
        "gloss": "a stone or tool for beating and crushing grains"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:2422",
          "words": [
            {"translit": "yâvar", "gloss": "stone or other objects used for crushing grains", "script": "یاور"}
          ],
          "note": null,
          "quote": {"text": "قدر از سر گرز او ساخت یاور - قضا ازسر خصم او کرد هاون", "poet": "Nazârî Qahestânî"}
        }
      ]
    }
  ]
}
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
```


## [2026-10-17T00:30:32.552Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; awk 'NR>=175' agent/AGENT_INSTRUCTIONS.md | head -40; sed -n 80,200p sources/SOURCE_MATRIX.md; command ls page-55*.json; python3 -c \"\nimport json;d=json.load(open('page-558.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:5000])\"",
 "description": "Read remaining instructions, matrix, sample output"
}
```


### [2026-10-17T00:30:33.069Z] TOOL RESULT

```
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
- **SBK** — M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SBK.txt`

## Semitic / Arabic loans in either direction

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
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
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ARB_mo3rb.txt`
- **KFL** — Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KFL.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DEV.txt`
- **LAM** — H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAM.txt`
- **DOZ** — R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeu
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DOZ.txt`
- **AKD** — H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AKD.txt`
- **SIN** — B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SIN.txt`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
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

## English / Romance / Germanic

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol4.txt`
- **WEB** — Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
page-550.json
page-551.json
page-552.json
page-553.json
page-554.json
page-555.json
page-556.json
page-557.json
page-558.json
page-55.json
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
```


## [2026-10-17T00:30:39.759Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls site/pages/562.jpg; sed -n 1,200p tools/verify_check.py | grep -n -i 'problem' | head -40",
 "description": "Check page image and checker rules"
}
```


### [2026-10-17T00:30:40.205Z] TOOL RESULT

```
site/pages/562.jpg
22:    missing_pages, problems = [], []
46:            problems.append(f"page {pg}: invalid JSON ({ex})")
52:                problems.append(f"page {pg}: entry {i} ({e['root']['name']}) missing")
56:                problems.append(f"page {pg}: entry {i} root verdict {rv!r} invalid")
65:                    problems.append(f"page {pg}: entry {i} ({e['root']['name']}) node #{n['id']} missing")
69:                    problems.append(f"page {pg}: entry {i} node #{n['id']} verdict {nv!r} invalid")
74:                    problems.append(f"page {pg}: entry {i} node #{n['id']} has no derivation")
89:    for p in problems:
90:        print("PROBLEM:", p)
94:    return 1 if problems else 0
```


## [2026-10-17T00:30:42.106Z] TOOL CALL #7: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/562.jpg"
}
```


### [2026-10-17T00:30:42.159Z] TOOL RESULT

```

```


## [2026-10-17T00:31:04.141Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['KLN','MON5','MON','IRN','ARB','BQT','ISS','KNT','SOD','HRN']:\n  v=d.get(k); print(k, json.dumps(v,ensure_ascii=False)[:600] if v else None)\"",
 "description": "Look up reference metadata"
}
```


### [2026-10-17T00:31:04.486Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
MON5 None
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe-privat
ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "lo
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local fil
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "
```


## [2026-10-17T00:31:08.618Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['KLN','HRN','ISS','SOD','MON','BQT']:\n  v=d.get(k); print(k, v.get('local_file'), v.get('page_offset'), v.get('lookup_hint','')[:500]);print()\"",
 "description": "Get offsets for key references"
}
```


### [2026-10-17T00:31:08.953Z] TOOL RESULT

```
KLN /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

HRN /home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

ISS None DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Khotanese Texts VI itself is not online. Nourai's ISS page numbers cannot be checked directly; the Dictionary of Khotan Saka (headword at line start, Khotanese in transliteration, with 'Pok.' refs) covers the same etymological material and can verify the substance of a claim.

SOD ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt'] printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get serv

MON ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] None Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Aden

BQT ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf imag
```


## [2026-10-17T00:31:11.268Z] AGENT

Now Klein pages 826 and 828.


## [2026-10-17T00:31:12.599Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E '^(Jerusalem|jasper)' KLN_1966.txt | head; grep -n -i -A8 '^Jerusalem' KLN_1966.txt | head -30; grep -n -i -A12 '^jasper' KLN_1966.txt | head -30",
 "description": "Grep Klein for Jerusalem and jasper"
}
```


### [2026-10-17T00:31:13.134Z] TOOL RESULT

```
20185:jasper,  n.,  an  opaque  variety  of  quartz.  —  ME. iaspre,  fr.  OF.  jaspe,  jaspre,  fr.  L.  iaspis,  fr.  Gk. lacm ?,  ‘jasper’,  which  is  of  Sent,  origin.  Cp. Heb.  yashephih,  Akkad,  yashupu,  ashpu,  ‘jasper’. Jasper,  masc.  PN.  —  A  name  of  Persian  origin. Jas-per  lit.  means  ‘treasure  holder’.  The  first element  of  this  compound  name  is  traceable  to Pers .ganj,  ‘treasure’.  See  genizah  and  cp.  Gaspar. Jataka,  n.,  a  birth  story  of  Gautama  Buddha.  — OI.  jatakah,  ‘begotten  by;  birth’,  fr.  jatah, bom;  son',  which  is  cogn.  with  L .gnatus,  ‘bom’, Gk,  -yviQToi;  (in  compounds),  ‘bom’,  fr.  I.-E. base  gen-,  ‘to  beget,  bear,  bring  forth,  produce’, whence  also  L.  gignere,  ‘to  beget,  bear,  bring forth’,  genus,  ‘birth,  descent,  origin’.  See  genus and  cp.  words  there  referred  to.
20245:Jerusalem,  n.  —  Gk.  'IspouaaXfip.,  fr.  Heb.  Y*rQ- shaldyim,  lit.  ‘foundation  of  peace’,  fr.  base  of yardh,  ‘he  threw,  cast’,  and  shaldm,  ‘peace’.
20247:Jerusalem  artichoke.  —  Folk  etymological  alter¬ ation  of  It.  girasole,  ‘sun  flower’.  See  girasol. Jeshurun,  n.,  poetic  name  of  Israel.  —  Heb. Ylshurdn,  prop,  ‘the  righteous  people’,  deno¬ minated  fr.  yashdr  =  yashdr,  ‘straight,  right, upright’,  which  derives  fr.  yashdr,  ‘was  smooth, straight,  right’,  whence  also  ydsher,  ‘straight¬ ness,  uprightness’,  meshdr,  ‘evenness,  upright¬ ness,  equity’,  mishSr,  ‘uprightness,  level  place, plains’;  rel.  to  Aram,  meshrd,  ‘level  place’, Arab,  yasara,  ‘was  gentle,  tractable,  easy’, ydsar,  ‘tractable,  easy’,  Akkad,  esheru,  ‘to  be straight  or  right,’  mesharu,  ‘justice’;  cp.  Sharon. The  defective  writing  of  the  first  u  in  Y*shurun (with  qubbutz  inst.  of  with  shureq)  does  not affect  its  quantity,  and  is  due  to  the  tendency to  avoid  the  scriptio  plena  in  two  successive syllables.
20245:Jerusalem,  n.  —  Gk.  'IspouaaXfip.,  fr.  Heb.  Y*rQ- shaldyim,  lit.  ‘foundation  of  peace’,  fr.  base  of yardh,  ‘he  threw,  cast’,  and  shaldm,  ‘peace’.
20246-Heb.  yardh  in  the  above  sense  is  rel.  to  Ethiop. warawa,  ‘he  threw’,  ModArab.  warra,  of  s.m. For  sense  development  cp.  Akkad,  nadu  ushshe, Gk.  (3aXXecrSm  L.  fundamenta  jacere,  ‘to lay  the  foundations’.  Cp.  Shaldm ,  the  ancient Heb.  name  of  Jerusalem.  Cp.  also  Aram.  Yeru- shHdm ,  Akkad.  Ursalimmu  .(in  the  Tell  El- Amama  Tablets:  Urusalim),  Arab.  Onshalam, Gk.  ‘IepoaAXupux,  ‘Jerusalem’  (see  Hierosolyma). For  the  second  element  in  Heb.  Ylriishdldyim see  shalom.
20247:Jerusalem  artichoke.  —  Folk  etymological  alter¬ ation  of  It.  girasole,  ‘sun  flower’.  See  girasol. Jeshurun,  n.,  poetic  name  of  Israel.  —  Heb. Ylshurdn,  prop,  ‘the  righteous  people’,  deno¬ minated  fr.  yashdr  =  yashdr,  ‘straight,  right, upright’,  which  derives  fr.  yashdr,  ‘was  smooth, straight,  right’,  whence  also  ydsher,  ‘straight¬ ness,  uprightness’,  meshdr,  ‘evenness,  upright¬ ness,  equity’,  mishSr,  ‘uprightness,  level  place, plains’;  rel.  to  Aram,  meshrd,  ‘level  place’, Arab,  yasara,  ‘was  gentle,  tractable,  easy’, ydsar,  ‘tractable,  easy’,  Akkad,  esheru,  ‘to  be straight  or  right,’  mesharu,  ‘justice’;  cp.  Sharon. The  defective  writing  of  the  first  u  in  Y*shurun (with  qubbutz  inst.  of  with  shureq)  does  not affect  its  quantity,  and  is  due  to  the  tendency to  avoid  the  scriptio  plena  in  two  successive syllables.
20248-jess,  n.,  a  short  strap  fastened  round  the  leg  of a  hawk  (falconry)  —  ME.  ges,  fr.  OF.  ges,  gies, pi.  of  get,  giet  (F.  jet),  ‘a  throwing’,  lit.  ‘that which  is  thrown’,  fr.  L.  jactus,  pp.  of  jacere,  ‘to throw’.  See  jet,  ‘to  spirt  forth’.
20249-Derivative :  jess,  tr.  v.
20250-jessamine,  n.,  jasmine.  —  MF.  jassemin;  a  var. of  jasmine  (q.v.)
20251-Jesse,  1)  masc.  PN.;  2)  in  the  Bible,  father  of David.  —  L.,  fr.  Gk.  Teoaotl,  fr.  Heb.  Yishdy, which  is  of  uncertain  etymology.
20252-Jessica,  fern.  PN.  —  Late  L.  Jesca  (Gen.  1 1 : 29), fr.  Gk.  Tetr/a  (Septuagint  l.c.),  fr.  Heb.  Yiskdh, name  of  a  daughter  of  Haran.
20253-jest,  n.  —  Lit.  ‘a  deed,  exploit’,  fr.  ME.  geste, jeste,  fr.  OF.  geste,  ‘a  deed,  exploit’,  fr.  L.  gesta, ‘deeds,  acts’,  neut.  pi.  of  gestus,  pp.  of  gerere, ‘to  bear,  carry,  produce,  perform,  do’,  used  as  a noun.  See  gerent  and  cp.  gest,  gestation,  gesti¬ culate,  gesture,  register.
20254-Derivatives:  jest,  intr.  v.,  jest-ee,  n.,  jest-er,  n., jest-ing,  n.  and  adj.,  jest-ing-ly,  adv.
20255-Jesuit,  n.  —  ModL,  Jesuita,  formed  fr.  Jesus with  suff.  -ite.
20185:jasper,  n.,  an  opaque  variety  of  quartz.  —  ME. iaspre,  fr.  OF.  jaspe,  jaspre,  fr.  L.  iaspis,  fr.  Gk. lacm ?,  ‘jasper’,  which  is  of  Sent,  origin.  Cp. Heb.  yashephih,  Akkad,  yashupu,  ashpu,  ‘jasper’. Jasper,  masc.  PN.  —  A  name  of  Persian  origin. Jas-per  lit.  means  ‘treasure  holder’.  The  first element  of  this  compound  name  is  traceable  to Pers .ganj,  ‘treasure’.  See  genizah  and  cp.  Gaspar. Jataka,  n.,  a  birth  story  of  Gautama  Buddha.  — OI.  jatakah,  ‘begotten  by;  birth’,  fr.  jatah, bom;  son',  which  is  cogn.  with  L .gnatus,  ‘bom’, Gk,  -yviQToi;  (in  compounds),  ‘bom’,  fr.  I.-E. base  gen-,  ‘to  beget,  bear,  bring  forth,  produce’, whence  also  L.  gignere,  ‘to  beget,  bear,  bring forth’,  genus,  ‘birth,  descent,  origin’.  See  genus and  cp.  words  there  referred  to.
20186-Jatropha,  n.,  a  genus  of  plants  of  the  spurge family  (bot.)  —  ModL.,  inaccurately  formed  by the  Swedish  botanist  Carolus  Linnaeus  (1717-
20187-826
20188-83)  fr.  Gk.  iarpo;,  ‘healer,  physician’  (see  iatric), and  Tpo<py|,  ‘food,  nutrition’  (see  trophic), jaun,  n.,  a  small  palankin.  —  Bengali  jan,  yan,  j.
20189-fr.  OI.  ydnah  (masc.),  ‘path’,  (neut.),  ‘a  going’.
20190-See  janitor  and  cp.  the  second  element  in  Ratha- yatra.  Jl
20191-jaundice,  n.  —  Formed  with  intrusive  d  fr.  OF. jaunice,  jaunisse  (F.  jaunisse),  fr.  jaune,  ‘yellow’, fr.  L.  galbinus,  ‘greenish  yellow’,  which  is  rel. to  galbanus,  ‘yellow’,  prop,  ‘having  the  color  of galbanum’,  fr.  galbanum,  name  of  a  yellowish gum  resin.  See  galbanum  and  suff.  -ice  (repre¬ senting  L.  -itia).  For  the  so-called  inorganic  d in  jaundice  cp.  gender,  sound,  ‘noise’,  thunder. Derivative:  jaundice,  tr.  v. jaunt,  intr.  v,,  to  make  a  short  pleasure  journey; n.,  a  short  pleasure  journey.  —  Of  uncertain origin.
20192-jaunty,  adj.,  careless,  sprightly.  —  Earlier  jantee, janty,  fr.  F.  gentil.  See  gentle.
20193-Derivatives:  jaunti-ly,  adv.,  jaunti-ness,  n. jaup,  intr.  and  tr.  v.,  to  splash  (Scot,  and  N.  of England).  —  Of  imitative  origin, javali,  n.,  the  collared  peccary.  —  Amer.  Sp. javali,  fr.  Sp.  jabali,  ‘wild  boar’,  fr.  Arab,  jabalt, ‘pertaining  to  the  mountains,  inhabitant  of mountains’,  adj.,  formed  fr.  jabal,  ‘mountain’, which  is  rel.  to  Heb.  g(bhul,  ‘frontier,  bound¬ ary’,  orig.  ‘earth  wall  or  mountain  serving  as boundary’.  Cp.  Bible  and  the  first  element  in Gibraltar.
20194-javelin,  n.,  a  light  spear.  —  F.  javeline,  of  Gaul, origin.  Cp.  OIr.  gabul,  W.  gafl,  ‘fork’,  W.  gaf- lach,  ‘feathered  spear’,  and  see  gable.
20195-Derivative :  javelin,  tr.  v.
20196-jaw,  n.  — ■  ME.  jawe,  jowe,  fr.  OF.  (=  F.)  joue,
20197-‘cheek,  jaw’,  fr.  VL.  *gauta ,  which  is  prob.  a contraction  of  *gavita,  fr.  *gabita,  fr.  pre-Latin *gaba,  ‘gorge,  jaw,  goiter’,  whence  also  F.  gaver,
```


## [2026-10-17T00:31:17.151Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for f in ARB_mo3rb.txt ARB_abdulraheem.txt; do echo \"## $f\"; grep -n -E 'أوري|اوري|أورى|الأوارى|أوارى|شلم' $f | head -20; done",
 "description": "Grep al-Jawaliqi for Jerusalem forms"
}
```


### [2026-10-17T00:31:17.533Z] TOOL RESULT

```
## ARB_mo3rb.txt
4199:و كن ٠‏ ذلك 1 لبيت المقدس “أورى شل 6 قال الامش 
4239:وقد طفت للمأل أفاقه 2# عمان خمص فأورى شم 
4243:قال أبوفييدة 5 غك تأورى شل » بكسر اللام ٠‏ وقال : هو عبرانىي مدر نبا 6 
4537:برد (ص* من طبعة أورية وص4 من طبعة الى » ١‏ : لاه من شرح المرصتى ) وفى اللسان 
4945:(1) فى م ه شرما الإستار» وهو مالف لسائر النسخ ولنقائض ( ص 4 مم طبعة أورية ) . 
8644:إجماع الناس أنه لعيد الر-من بن حسان © وهوق بت معاورية بن ألى سفيان » ٠‏ وأ نظار طبققات الشعراء 
11975:الفرس ” أدره” و العرب 01 عليه وو من جشلما » وحم يفعلون ذلك 6 
12968:اوري 
19754:6 افتتاح قصيدة فى ديرانه رص 5 *ا ١‏ طبعة أورية ) وأوله 
24556:قال القتل » ٠‏ رما لحان بسر تيطع راق اوري ناج وأنظر نحفة الأحوذى(م ران 
25541:الخطوطة لكاب الكامل ليرد ( ص وباد طبعة أورية ) 
31758:الارأورى ١١5نم‏ ؛ +70:؟ 
34271:أورى شل (وانظار ”بيت المقدس“'و”” ابابا ") 
34465:بيت ادس (وانظر””أورى شل“ و ””إيلياء“* 
36711:جا دروأ اقافة اللريياق 0 1 ايت معاورية ٠‏ طبعة مد أده سنة ١ 05.1١‏ 
## ARB_abdulraheem.txt
```


## [2026-10-17T00:31:20.328Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4190,4250p ARB_mo3rb.txt",
 "description": "Read al-Jawaliqi Urishalam entry"
}
```


### [2026-10-17T00:31:20.886Z] TOOL RESULT

```
وقالوا ع ”ا أبيل ٠“‏ قال : 
كاي ا 2 
وما الى عل جا 2# بناه وصلب فيه وصارا 0 ك 


قل أبو 2 : 2 َس « صاحب 2 أضل » ومن عصا الناقوس ٠‏ 
1 )19 مني 


و كن ٠‏ ذلك 1 لبيت المقدس “أورى شل 6 قال الامش 


ع 
)00 رواية الأساث : « وما قدّس الرهران فى كل هيكل » ٠‏ وثال : «و””ما““ فى قوله ””وما ؤدس»* 
ا مصدرية 6 أى : وتسبيح الره بان أبيل الأبيلين »> ٠‏ وروأية اللهاية ٠‏ «وما سيم الرهبا بان فى كل بلدة © 
وزواية الازانة وق كل 10> * والوذاح يضا فى معجم البلدان (جمص 5) مع آخرين ٠‏ منسوابة ١٠‏ 
إل خطل 6 وروايته « وما سبح الرحن » ٠‏ 
(0) نسبه فى ابججهرة للد “عشى 6 وأوله < فإفى ورب الساجدين عشسية » والظاهى من كلام صاحب 
للها" أنه يرى أن الكلمة عر بية © لأنه شرح الأثرج كان عيسى عليه السلام يسمى أبيل الأبيلين» فقال : 
« الأبيل يوزن الأسير : الراهب » سى به لتأبله عن النساء وترك غشيا نين ٠والفعل‏ مه أبل يأبل أباله : 
إذا تنسك وترهب» ٠‏ (+) فى هذا الحرف روايات أولفات » فالذى هنا يمتح المزة وكير 1 
الباء الموحدة » وهذا الضبط رواه أيضا صاحب القاءوس ٠‏ والروايات الأخر ى «أبيل » بفتم اطمزة 
وتقدم اليا المثناة سا كنة وبتأخير الباء الموحدة مع مها أو فتيحها أو كسرها ٠‏ كاف القاموس » واقتصر 
صاحب اللسان على رواية خم الباء فط » وقال : « الراهب »6 فإما أن يكون أعحميا » وإما أن يكون 
قد غيرته ياء الإضافة » وإما أن يكون من باب انقحل» ٠‏ (4) هكذأ هو هنا فى النسخ » والذى 
فى اللسان وشرح القاموس «أبيل » بتقدم الياء مع غم الباء ء» وقسيا البيت للا عثى » وقال الزبيدى : «قيل # 
أراه ””أبيل' فليا اضعار قدم الياء م قالوا ””أينق**» والأصل * 'أنوق“"» 22٠‏ (ه) بنذم المزة 
ركسر الراء وفتح الشين وكسر اللام ٠‏ ونقل ياقوت أله يروى بفتح اللام أيضا » وقال : « هو اسم 
للبيت المقدس بالعبرانية » إلا أنهم سكنون اللام» ٠‏ وف الأسان : « المثهورأررى شل بالتشديد 
لفففه للضرورة > يعنى الأعثى فى البيت الآتى ٠‏ (1) فى ى « قال الأسمعى » وهو خطأ ٠‏ 
والييت ذكه فى اللسان ( :ة و ١8:16‏ ؟ ) وياقوت وبعه أنر ( 105:1 ٠)‏ م 


1 
05 
ار 


مساج 
مك[ أ 


”0 غواس ل جلاليت 


مم ياب الألف 


وى تير 0 ا و مه 1 سام 
وقد طفت للمأل أفاقه 2# عمان خمص فأورى شم 
53 


قال أبوفييدة 5 غك تأورى شل » بكسر اللام ٠‏ وقال : هو عبرانىي مدر نبا 6 
00 


0 معن + سر 
والشمر اها وعاء نور فوا القافك الرمع ل الاو وده فلع
```


## [2026-10-17T00:31:30.979Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py IRN:28 --image 2>&1 | tail -60",
 "description": "Render and OCR Iranvij page 28"
}
```


### [2026-10-17T00:31:34.919Z] TOOL RESULT

```
(no exact page map; using offset 11 -> pdf page 39; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/IRN/0028.png
REF: IRN:28  PDF: data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf page 39  OCR-lang: fas

۳۸ ایرانویج

این‌دو تیرة بزرگك با همه طایفه‌های خود که نام برده شد» بسوی نواحی
حاصلخیز پیرامون دریاچه رضائیه (اورمیه-شهرآب) فرودآمدند. تیرة مادی در
نواحی جنوب شرقی دریاچه بین همدان وتبریز جای گرفت ویعدها تا اصفهان پیش
رفت وقبیله‌های پارسی درمغرب وقسمت‌های جنوب غربی دریاچه» درناحیه اردلان
کنونی جای گرفت . واه اردلان را میتوان بصورت کهن آن ۸۳130 بازسازی
کرده 0 - 27۲ ومعی‌آن «ایران مقدس» است .

این‌قبیله‌ها با یکدیگر باصلح وآرامش زندگی م ی کردند و به دامداری و
تربیت اس بکه یکی از مهمترین پیشه‌های آنها بود می‌پرداختند. یکی از علل
برتری آنها نیز در دوران تاریخی داشتن اسب‌های تربیت شدهٌ خوب بودکه در
جنگها عامل مهم پیروزی بشمار میرفت .

اینان » نخست به خدمت امیران بومی درآمدند وسپس خود سالار و سرور
روستا ها گشتند .
قبیله‌ای از مهاجران هند و اروپائی که در پی‌یافتن سرزمین ها و چراگاه‌های جدید مهاجرت
می‌کنند (نقل ا زکتاب 6سصده1:77)
ی
```


## [2026-10-17T00:31:38.123Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py IRN:28 --image --pdf-page 29 2>&1 | tail -60",
 "description": "Re-render Iranvij at corrected pdf page"
}
```


### [2026-10-17T00:31:38.474Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/IRN/0028.png
REF: IRN:28  PDF: data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf page 39  OCR-lang: fas

۳۸ ایرانویج

این‌دو تیرة بزرگك با همه طایفه‌های خود که نام برده شد» بسوی نواحی
حاصلخیز پیرامون دریاچه رضائیه (اورمیه-شهرآب) فرودآمدند. تیرة مادی در
نواحی جنوب شرقی دریاچه بین همدان وتبریز جای گرفت ویعدها تا اصفهان پیش
رفت وقبیله‌های پارسی درمغرب وقسمت‌های جنوب غربی دریاچه» درناحیه اردلان
کنونی جای گرفت . واه اردلان را میتوان بصورت کهن آن ۸۳130 بازسازی
کرده 0 - 27۲ ومعی‌آن «ایران مقدس» است .

این‌قبیله‌ها با یکدیگر باصلح وآرامش زندگی م ی کردند و به دامداری و
تربیت اس بکه یکی از مهمترین پیشه‌های آنها بود می‌پرداختند. یکی از علل
برتری آنها نیز در دوران تاریخی داشتن اسب‌های تربیت شدهٌ خوب بودکه در
جنگها عامل مهم پیروزی بشمار میرفت .

اینان » نخست به خدمت امیران بومی درآمدند وسپس خود سالار و سرور
روستا ها گشتند .
قبیله‌ای از مهاجران هند و اروپائی که در پی‌یافتن سرزمین ها و چراگاه‌های جدید مهاجرت
می‌کنند (نقل ا زکتاب 6سصده1:77)
ی
```


## [2026-10-17T00:31:43.588Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'اورمیه|ارومیه|شهرآب|شهر آب|اورشلیم' incoming/IRN/IRN_pages.txt | head; grep -c . incoming/IRN/IRN_pages.txt",
 "description": "Search Iranvij OCR for Urmia mentions"
}
```


### [2026-10-17T00:31:43.922Z] TOOL RESULT

```
547:ونیریز و زره سیستان وغیره خشک شدند و درياچهٌ رضائیه (ارومیه) نی زکه در زمان
767:(اورمیه) که پهنه‌ای بیش از امروز داشت ودارای دشتهای سرسبز وخرم بود
875:حاصلخیز پیرامون درياچهُ رضائیه (اورمیه-شهرآب) فرودآمدند, یره مادی در
1622:طولانی اورشلیم پرداخت وآنجا راگرفت و هزاران نفر از بزرگان وصنعتگران یهود
1624:دیگر با مصر متحد گشتند . «ناب وکدنصر» این بار اورشلیم راگرفت وآنجا را ویران
1743:خانةٌ پادشاه داده شود ونیز ظروف طلا و نقرهٌ خانةٌ خدا را که از هیکل اورشلیم
4721:دریاچه چی‌چست ( ارومیه ) فاصله دارد . ولی هر دوروایت جای آن را درشیز
6181:ارومیه ده۱- ۱۱۱-۱ استخری (ابواسحق ابراهیم) ۹ ۱۱- ۱۱۷
6227:اکباتان پارس ۱۸۱ اورشلیم رد .وه باه
6063
```


## [2026-10-17T00:31:48.264Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{p=0} /\\f/{p++} NR==767||NR==875{print NR, \"block\", p}' incoming/IRN/IRN_pages.txt; sed -n 760,770p incoming/IRN/IRN_pages.txt; grep -n 'pdf page' incoming/IRN/IRN_pages.txt | awk -F: '$1<880' | tail -4",
 "description": "Locate pages for Urmia mentions in Iranvij"
}
```


### [2026-10-17T00:31:48.667Z] TOOL RESULT

```
767 block 35
875 block 38
ایران «73ع برخاسته‌اند ونمودار آنن د که روزگاری ایرانی نژادان در آنجا ساکن
بوده‌اند.

برخی از تاریخ نویسان دورا نکهن این اقوام مهاجررا ازطوایف سکائی و
سرمتی میدانند! .

این دوقوم بتدریج از دربندهای قفقازگذشتند و درپیرامون درياچةٌ رضائیه
(اورمیه) که پهنه‌ای بیش از امروز داشت ودارای دشتهای سرسبز وخرم بود
ساکن شدند وب ه کار دامداری وکشاورزی وتربیت اسب پرداختند .

مورخان یونانی نام قبایل پارسی‌را چنین نوشته‌اند:
747:[pdf page 36]
775:[pdf page 37]
806:[pdf page 38]
871:[pdf page 39]
```


## [2026-10-17T00:31:53.833Z] TOOL CALL #17: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-10-17T00:31:53.842Z] TOOL RESULT

```


```


## [2026-10-17T00:31:57.748Z] TOOL CALL #18: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Jerusalem",
 "prompt": "Give the English etymology section of Jerusalem verbatim (Hebrew form, Amarna Urusalim, meaning of elements, Shalem deity)."
}
```


## [2026-10-17T00:31:58.496Z] TOOL CALL #19: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/jasper",
 "prompt": "Give the etymology section of English jasper (the stone) verbatim."
}
```


## [2026-10-17T00:31:59.447Z] TOOL CALL #20: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DB%8C%D8%B4%D9%85",
 "prompt": "Give the Persian etymology section for یشم verbatim, and any Arabic section with etymology."
}
```


## [2026-10-17T00:32:00.429Z] TOOL CALL #21: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D9%88%DB%8C",
 "prompt": "Give the Persian etymology section(s) for جوی (stream) verbatim, including Middle Persian, Old Persian, Proto-Iranian forms."
}
```


### [2026-10-17T00:32:02.928Z] TOOL RESULT

```
# Etymology of English Jasper (the stone)

From Middle English *jasper* and *jaspre*, from Old French *jaspre* (a variant of *jaspe*), from Latin *iaspis*, from Ancient Greek *ἴασπις* (íaspis).
```


### [2026-10-17T00:32:03.142Z] TOOL RESULT

```
# Persian Etymology for جوی

Based on the Wiktionary entry, here is the etymology section:

The word derives from Middle Persian (ǰōy), which came from Old Persian (yauviya). It is cognate with Northern Kurdish *co* and Sanskrit *यव्या* (yavyā).

The entry notes that native scripts are needed for the Middle Persian and Old Persian forms, as they are not displayed in the current version.
```


### [2026-10-17T00:32:03.916Z] TOOL RESULT

```
# Persian Etymology for یشم

The Persian etymology section states:

"(This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium.)"

There is no Arabic section present on this Wiktionary page for یشم. The entry only contains a Persian language section with noun definition, pronunciation, and derived terms.
```


### [2026-10-17T00:32:06.924Z] TOOL RESULT

```
# English Etymology of Jerusalem

Based on the Wiktionary content provided, here is the English etymology section:

The entry traces Jerusalem through multiple linguistic layers: "From [Old English](https://en.wikipedia.org/wiki/Old_English "w:Old English") _[Hierusalem](/wiki/Hierusalem#Old_English "Hierusalem")_ or [Old French](https://en.wikipedia.org/wiki/Old_French "w:Old French") _[Jherusalem](/wiki/Jherusalem#Old_French "Jherusalem")_ or [Late Latin](https://en.wikipedia.org/wiki/Late_Latin "w:Late Latin") _[Ierusalem](/wiki/Ierusalem#Latin "Ierusalem")_, _[Hierusalem](/wiki/Hierusalem#Latin "Hierusalem")_, from Latin _[Hierosolyma](/wiki/Hierosolyma#Latin "Hierosolyma")_, from [Ancient Greek](https://en.wikipedia.org/wiki/Ancient_Greek "w:Ancient Greek") _[Ἰερουσαλήμ](/wiki/%E1%BC%B8%CE%B5%CF%81%CE%BF%CF%85%CF%83%CE%B1%CE%BB%CE%AE%CE%BC#Ancient_Greek "Ἰερουσαλήμ")_ (Ierousalḗm), from [Biblical Hebrew](https://en.wikipedia.org/wiki/Biblical_Hebrew "w:Biblical_Hebrew") _[יְרוּשָׁלַיִם](/wiki/%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D#Hebrew "ירושלים")_ (Yərūšālayim)."

The document does not provide information about Amarna Urusalim, individual element meanings, or the Shalem deity.

[WebFetch note: this page's text is 121118 characters long and the answer above covers only characters 0 to 100000; the final 21118 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


## [2026-10-17T00:32:10.383Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D",
 "prompt": "Give the Hebrew etymology section verbatim (Amarna Urusalim, yrw found, Shalem, folk etymology \"city of peace\" if any)."
}
```


## [2026-10-17T00:32:11.681Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%B4%CE%B1%CF%83%CF%80%CE%B9%CF%82",
 "prompt": "Give the Ancient Greek etymology section verbatim (Semitic source, Hebrew yāšp̄ē, Akkadian, Persian yašm?)."
}
```


## [2026-10-17T00:32:12.723Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Urmia",
 "prompt": "Quote verbatim the Etymology/name section: what is the origin of the name Urmia (Syriac 'city of water' folk etymology, Urartian, etc.)?"
}
```


### [2026-10-17T00:32:17.564Z] TOOL RESULT

```
# Etymology of Urmia

Based on the Wikipedia article, there are several proposed origins for the name Urmia:

**Urartian Origin:**
"Richard Nelson Frye suggested Urartian origin for the name"

**Indo-Iranian Origin:**
"T. Burrow connected the origin of the name Urmia to Indo-Iranian urmi- 'wave' and urmya- 'undulating, wavy'."

**Syriac Derivation:**
The name could derive from combining Assyrian Aramaic words: "Ur" (meaning "city") and "Mia" (meaning "water"), resulting in "City of Water" referring to Lake Urmia nearby.

The article notes these various etymologies reflect the city's linguistic and cultural diversity throughout history.

[WebFetch note: this page's text is 192837 characters long and the answer above covers only characters 0 to 100000; the final 92837 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


### [2026-10-17T00:32:17.711Z] TOOL RESULT

```
# Ancient Greek Etymology of ἴασπις

According to the Wiktionary entry, the word has "a loanword of unclear source, but possibly Egyptian in origin."

The entry identifies several related forms across languages:

**Semitic cognates:**
- Biblical Hebrew: יָשְׁפֵה (yāšəfēh, "jasper")
- Akkadian: /⁠yašpû⁠/ ("name of a stone")
- Classical Syriac: ܝܫܦܐ (jaʃpɑ(ʔ), "jasper")

**Other related forms:**
- Persian: یشپ (yašp), noted as deriving "from the same source"

The etymology section concludes these terms share a common origin, though the ultimate source remains unclear despite the apparent Egyptian connection suggested by the loanword classification.
```


### [2026-10-17T00:32:18.913Z] TOOL RESULT

```
# Hebrew Etymology of ירושלים

According to the Wiktionary entry, the etymology is **disputed**. Here are the key proposed origins:

**Western Semitic Form**: The word derives from "a Western Semitic form attested in Ancient Egyptian as ꜣwšꜣmm" (the hieroglyphic representation is shown in the source).

**Possible Compound Origin**: One theory suggests it combines "יָרוּ (yarú, 'he lays down')" with "שָׁלֵם (Shalém, 'the Canaanite god Shalem')."

**Folk Etymology**: A popular but likely inaccurate explanation proposes "יִרְאֶה (yir'é, 'he sees')" plus "שָׁלוֹם (shalóm, 'peace')"—essentially meaning "city of peace."

**Cognates**: The entry notes related forms in Akkadian (Urušalim) and Classical Syriac (ʾŪrišlēm), suggesting a shared Semitic heritage rather than Hebrew invention.

The source emphasizes the etymology remains uncertain, with multiple competing theories rather than consensus.
```


## [2026-10-17T00:32:23.519Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for r in BQT:2434 BQT:2422 BQT:602; do timeout 300 python3 tools/ref_page.py $r --image 2>&1 | head -80; echo \"-----\"; done",
 "description": "Render and OCR three Borhan pages",
 "timeout": 600000
}
```


### [2026-10-17T00:32:37.216Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 517; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2434.png
REF: BQT:2434  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 517  OCR-lang: fas

پشپ! < بفتح اول وسکون ثانی و بای پشت؟ - بروزن هشت. ام سکی باشد

قارسی» بمعتی یشم است وآن‌سنگی باشدمعروف | ازکتاب زند بعتی قمی ازاقام کتاب زند, چه
کوید: از عبرانی « بشفه » ( بفتح اول وکسر سوم ) است بمعنی مصقول » و آن مشتق است از
(شفه) بمعنی‌سیقلی شد. این‌کلمه بیودانی‌منتقل گردید: 125015. واز آن بدیگرزبانهای ارویا رفته
(احهی) (قی:انگلیی185007. فراسوی188806) رك: لیدل واسکات. فرهنگه بونانی-انگلیسی:
1396 ورك : دزی جاص۸۵۱؛ ور4: بشم - ۲ - 32501 . دراوستایی 181111 همريشة
بستا(ه.م.)8582ل[اوستابی و8[88«ساسکربت و72215108 وبشتن‌بهلوی بمعنی‌پرستش وستایش
کردن وجشن (خود اين‌کلمهٌ پارسی آزریِشهٌ مذکور است) . ( ر4؛ بشتن ) . بشت بمعنی نبایش

ز بهر روان هر که فرمود بشت پشیمان شد . از گفت خود با زگشت.
«زرنشت بهرام پژدو. زرایعت نامه؟.
بشتها بخشی ازینج جزه اوستا را تشکیل دهند وآن شامل‌ستایش آفرید کار ولیایش امشاسپندان
وایزدان است. بشتهایی که | کنون دردست است؛ اگرچه تر کیب شمری نداردء ولی هنوزهم کلام
آن موزون وبا طرزی شاعرانه, با عبارات بلند وتخیلات عالی سروده شده‌است . اصلا هم بشتیا
منظوم ودارای وزن هجائی ومانند کاتها منم بقطعات وبیتها وشماره هجا های آن ۸ وگاهی۱۰
و۷ بوده‌است. بهدها بواسطهةٌ تصرفانی که درآنپا شده وبعلت تفیر- که بتدریج جزوهتن گردیده-
تر کیب شعری آن بهم خورده‌است . باوجود این اوزان آنها بخوبی معلوم ومیتوان دوباره آنهارا
بشکل اصلی درآورد . برخی ازیشتها بسیار قدیمی بنظرمیرسند. اکنون بیست ويك پشت موجود
است که بعی ازآنها کوتاه وبسنی دیگر بسیار بلند است. اسامی پشتها بقرار ذیل است :
۱- هرمزد بشت. ۲ هفت‌امناسپند بشت. ۳- اردیبهشت بشت. ‏ ۶- خردادیشت.
آبان بشت.  ‎-٩‏ خورشید بشت. ۷- ماه پشت. ۸- تیربفت ۰ ٩-کوش‏ بشت .
+ مهربشت. ۱۱- سروش بشت. ۱۲ رشن بشت. ۱۳- فروردین بشت . ۱۶- بهرام
بشت. ۱۵-رام بشت. ۱۹-دین بشت. ۱۷ آردبشت. ۱۸ اشتاد بشت. ۱۹-زامیاد
بشت. *۲- هوم بشت. ۲۱- ونند بشی.
از این میان مخصوماً ,بشتپای بتک رخسمت بهی :۵ بمیار قدیمند 2 مزدستا بقلم
نکارنده ۱۳۱-۳۰ ورق پورداود. پشتها ۱ مقدمه ۲ بیعد.
(رهای قاطع۷م۴ )

-----
(no exact page map; using offset -1917 -> pdf page 505; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2422.png
REF: BQT:2422  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 505  OCR-lang: fas

بانه <<
کشف خواند ‎٩‏ - و بتر کی طرف و جاب را یابد است که از پافتن باشد چه در فارسی بای
میگوبند - وامر بسوختن هم هت . ابجد بواو تبدیل می‌باید و همچنین برعکی .
بانه- بفتح نون, بممنی هاون‌باشدمطلقاً یاور بروژن‌ساغر» بمعنی باری‌دهنده
و آن ظرفی است که چیزها در آن کوبند ۲ - | وهددکار باشده - و دستَهٌ هاونرا نی زکویند۹؟ -
و بمعتی بزرك هم هت وآن تخمیت که روغن | ونم روز دهم‌است از هرماء۷ .
از آن کیرند وبعربی کتان خوانند۴ . یاو گی۸ - بنتح وار و کاف فارسی
یاود؟ < بفتح واو بروزن آمد. بمعنی | بتختانی کشیده , بممنی گم شدلی وناپدی دکشتنی
۹ - هرن نوبسد: بان (وحیآسمانی, سورت) [اسطلاح عرفانی]. پارمی‌باستان -288لل
(«دیه. تحفه, بخشش) » اوستا 9282 پپلوی 328 «اسشدق 019۱۱۲4۶» هوبشمان گوید: معالی
مذ کور باهم متناسب نیستند. رك: هوبشمان ۱۱۲4 019.
۴ - همجو پاور شده سر کرزت تا چو بانه کند سر دشمن .
فتاحی نیشابوری «جهانگیری» «رشیدی».
۳ - رك: رشیدی. ی - رشیدی بهمین معنی آورده. ر: باوند» بافتن.
8 *پارور (ازبار ۳۲ ور [پسوند نسبت واتصاف ] ( «اسشق 4۱۱۲۱:
چو پاور نبودش (دارا را) زازديك ودور یکی نامه بنوشت نزديك فور -
فزدوسی طوسی «شاهنامهٌ بخ ج٩‏ ۰۱۷۹۹
‎٩‏ - اوستا - 78۷87682 ( دستةٌ هاون) ( 50 ,1 500060 ,0610861) ۶ اسشق
۵ ور4: هوبشمان ۱۱۲۵ :
قدر از سر کرز او ساخت یاور قضا از سر خسم او کرد هاون -
ازاری قهستانی «جهانگیری» .
ورك: شاهد امه زگ روز دهم هرماه «آبان»( م.)است .کلمهٌفوق گوبا مسحف «دی] بآذر»است
که نام روزهشتم هرماه شمی‌است. ر4: روزشماری بقلم نگارنده ۲۱-۹ موژلف همین‌کلمه
را صورت «یادر» (ه م.) آورده بمعنی روز دوازدهم از تیرماه (۱)
۸ - از: باره (باوکه) ی (حاصل مصدرء اسم همنی) ۳ بافگی. (علاوه برممانی‌متن):
درفصل سیزدهم از کتاب سیاست‌نامه منسوب بخواجه نظام الملك درز کر داستان مربوط بامیر -
عضدالدولةٌ دیلمی با یکی ازقاضیان عهد اززبان دادخواهی چنین آمده: «دیگرباره میان با وگیان
آمدم وخدمت کردم ایشالرا چندان که نفقات بدست آوردم...» ازقرائن‌دراین جمله وعباراتی نظیر
آن که در کتب دیگرآن ایام مثل راحة الصدور و غیره دیده میشود » چنین مستفاد میگردد که
با وگیان گروعی ازسپاهیان ولشکربان بوده اند. و بهمین علت بعضی آنرا «ناوکیان» خوانده اند
بمعنی تیراندازان , لیکن این تصور صحیح لیست, و باوگیان جمع باوکی‌است منسوب به یاوه»
وآن چنالکه ازاستعمال قدما برمیآ.د بمعنی کسانی‌بوده است که بدون سروسردار ونظم وترتیبی
همین بجنگه میرفته‌اند . لشکر باوه یعنی لشکر بله و سرخود... (ر4: باوه) . با وگیان کسالی
بوده اند که در سلك چاین لشکری درمی آمده‌اند. خاقانی گوبد :
داد نیب صبا عرض سهاه بهار کز دوگروعهی بدید یاوگیان خزان.
همچنین درین بیت که درتاریخ وصاف آمده :
بقیه در حاشیةٌ صفحهٌ رد

-----
no scan of BQT covers printed page 602 (see 'scans' in refs_online.json)
-----
```


## [2026-10-17T00:32:41.506Z] TOOL CALL #26: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2434.png"
}
```


### [2026-10-17T00:32:42.015Z] TOOL RESULT

```

```


## [2026-10-17T00:32:42.010Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-17T00:32:50.733Z] TOOL CALL #27: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2422.png"
}
```


### [2026-10-17T00:32:51.289Z] TOOL RESULT

```

```


## [2026-10-17T00:32:51.283Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-17T00:33:04.021Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; mkdir -p ocr/BQT; cat > ocr/BQT/2434.vision.txt <<'EOF'\n[BQT p.2434 (vol 4, pdf 517), read from image by vision]\nیشپ ۱ - بفتح اول وسکون ثانی و بای فارسی، بمعنی یشم است وآن سنگی باشد معروف و خاصیت‌مند .\n۱ - در عربی یشب ، یشف (ه.م.)، یشم (ه.م.)، یسب، یصف ویصیب آمده . مؤلف نفس گوید: از عبرانی « یشفه » ( بفتح اول وکسر سوم ) است بمعنی مصقول ، و آن مشتق است از (شفه) بمعنی صیقلی شد. این کلمه بیونانی منتقل گردید: iaspis، وازآن بدیگر زبانهای اروپا رفته (انتهی) (قس: انگلیسی jasper، فرانسوی jaspe) رك: لیدل واسکات. فرهنگ یونانی-انگلیسی: iaspis ورك : دزی ج۲ ص۸۵۱؛ ورك: یشم .\nEOF\ncat > ocr/BQT/2422.vision.txt <<'EOF'\n[BQT p.2422 (vol 4, pdf 505), read from image by vision]\nیاور - بروزن ساغر، بمعنی یاری‌دهنده ومددکار باشد۵ - و دستهٔ هاونرا نیز گویند۶ - ونام روز دهم است از هرماه۷ .\n۵ - یارور (ازبار+ور [پسوند نسبت واتصاف] ) «اسشق ۱۱۲۱»\n۶ - اوستا - yâvarena ( دستهٔ هاون) (Geldner, Studien 1, 50) «اسشق ۱۱۲۵» ورك: هوبشمان ۱۱۲۵ :\nقدر از سر گرز او ساخت یاور  قضا از سر خصم او کرد هاون . نزاری قهستانی «جهانگیری» .\nEOF\ngrep -n -i -E 'y[aā]var|yâvar|yāwar' HRN.txt HUB.txt BRT.txt | head -20",
 "description": "Save Borhan vision text; grep Horn/Hübschmann/Bartholomae for yavar"
}
```


### [2026-10-17T00:33:04.557Z] TOOL RESULT

```
HUB.txt:3784:1125. Darmesteter iibersetzt yavarena- durch moulin a
HUB.txt:5297:b) Ap. y im Anlaut = np. y in: yavar, yar ^Stfissel'
HUB.txt:5298:= zd. yavarena-; yOz 'Jagdleopard' = arm. yovaz^ yavaz;
HUB.txt:5333:syavarsan-; mayazd (besser miyazd) *6elage' (parsisch) =
HUB.txt:5830:havan *M5rser* H. 1089; yavar 'Stossel* H. 1125 u. s. w.
HUB.txt:5949:yavar^ vgl. mand. adyaura, siehe
HUB.txt:5952:neben yavar H. 1125.
HUB.txt:9342:Syavarsan-, phi. paz. SiyavaxS West, PT. 4,|28, Min. 61.
BRT.txt:6259:—  antar)  i^ädamaü  'iiionis"  (IP.)  Vr.  21. 3.  'P-S^i  —  °Ai<JW  (VS.)  pu%ra  kava vJstaspa  ^y\-53',  45  (wo  'säum);  —  ratui 'iava  V.ö.ii;  Vr.5.6;  —  'laonB  aiahe raiwü  rafufritlm  Y.  22.3,  71. 3;  — yqmca bipaitistänqm  '/aonim  Y.  13,1;  —  °/at»ti- nqm  ärmaiti.paoiryanqmY .21.2; — Jiaisa- nqm  . ,  sasnSgüsqm  . .  'iaonqm  '/aoninqmca ..  nabänazdistanqm  ..  -saonqm  'iaoninamia .  .  af&rapaitinqm  'iaonqm  .  .  ai'i:ryanqm 'iaonqm  .  .  naram  'iaonqm  .  .  näirinqm 'saoninqm  Y.  26. 4— 8;  gf.^,  Vr, /.  3';  — ä'irai'antm  'iavamm  ,.  rdialitär^m  °iara- mm  .  .  västrXm  fiuyant^m  'iavanjm  .  . nmänS.paitlm  °!avan»m  .  .  nmänB.pa'inUn 'iavanjm  (statt  fem.)*>  aiaAe  raiüm  Q.4 7  f.;  7—9";  —  zaotanm  'savamm  ,- sraoiävar3zim  'iavafum  G.  J.  5;  5*;  — Aai^yavarxsqm  'iaonqm  haOiyavamtnqm -saoninqm  V.17.14;  14*,  G.J.7';  —  saoi- yantqm  'iaonqm  Y.  ;4-i.  *i~-li  Vr-5-i. 22,1,  Ytii,i7;  —  äsna?a  mana  'iaonqm äsna/a  mana  saoiyantqm  Vr.  /i.  3 ;  — fravasays  .  .  yamca  staoyB  (sd.)  'iävaoyj {DP.)YU3.88(f);~ädaAyunqm/a  'iaonqm .  ,  uzdaAyunqmca  'saonqm  Vr.  16.  z;  — irtrüuiqm  'iaonqm  .  .  Jvantqm  'saonqtn Y,  24. 5 ;  —  vup>m  'Savamm  h3iit»mca bavantimia  bü^anipmca  Y.  2^4,  Vr, /Äs;
BRT.txt:6639:3$,  14.5g',    f-7>    —  yavar^nS  as  sara- lYt  13.12g.         Ungrammatisch:  taEJa  ySi
BRT.txt:10116:•  j.  *gav-  m.  'Hand',  uzw.  dariA&chtr Wesen " :  am  aus  'va  (AD.)  paiii  apa.- gmrvayal  Yt.jp. 50;  11. z,  F.2i''>;  —  Aqm •va^^  nidar^zayatAü^m  Yl.j.27(?);  —  ma abara^alibya  fraluyh  mS  'vaeifya*''  aiwi.- tütuya  ¥.5,29;  —  d^ra  ..  mihröMru/am aptts  'vSiAP.)  darfzayeiti  Yt.  10. 48,  [n. 18:  lies  gavästryavar>i\
BRT.txt:10164:-  gavaestryavarStaara-  510
BRT.txt:10183:•  j.  gavästryavarä't«ma-  Adj.   'der  die
BRT.txt:13147:Mraiui'lre . .  ustaiwm  dadaifJ . .  masdäi  Y. J^J.  14;  —  ai  toi  myatä>m  ahura  imnanhä asäicä  dämä  "wir  wollen  dir,  o  Ah.,  in Ehrfurcht  das  Opfer  weihen  und  dem  Aia" Y._J4.3;  —  stütS  gard  vaAmSng . .  ahuriii dadimahicd  cTsmah'tcä  . .  Y.  4^.  1 ;  _J5.  j ;  — mitenkl.Dat(-Gen.)desPron.pers.:^aJil  tu l  mlnghäc/i .  .  düä  töi  dadsmahi  a%ä  As- mahl..  \.3ij. 4.  a  n)  im  jAw. a)  ohne Obj.  'schenken  sva,  ein  Geschenk  geben, eine  Gabe  reichen':  hs  daoS  as»m  upa.- rao'iayeUe  (sd.)  yS  drvaite  ^datäiti  P.  50; - —  yat  bä  paiti  .  .  naire  asaone  v»r}syät ("für  seine  Arbeit")  asaya  daoaiti  V,_y,  34 35;  —  yB  hs  *gaväslryavar)l {sA.)  *daidlt aSahmäi  ti.iS.  b)  mit  Obj,:  v^htksi hisvqm  dahäiti  yö  .  .  N.  77;  —  yai  nä kasvikqmcit  .  .  avartianqm  naire  asaone ajasta  ..  daoäi/i  V.iÄ'.37;  34;  —  tUtnm ,  .  yS  daoaiti  .  .  ayaptä  Jaioyanisi  Yt,  8. 49;  Ny.^.  II*';  —  da'iai  aHbyasnt  tat  avat äyapt?m   ar>dvt  YL5.  74;  »9,  9-  5.  '5-4;
BRT.txt:18016:•  j.  fraSaotoa-,  g.  f«raS°  m.  EN.  eines Gläubigen,  Schwiegervaters  Zara%ustras, 'SnAa^Jamaspas,  aus  der  HvB.gva-'Sasai\ic : hnxham  mSi  'rS  hvs^gvs  daBiBi/t  (sd) kfhrpim..  Y.5J.17;  —  -ra  (VS.)  .. AvS^a  Y.46. 16;  —  "ru^tf  hvSvake  alaotUS YLij.  103;  —  atcä  hsi  icantü  .  .  xlnüm .  .  kavacS  vistäspU  tarä^u/tri!  spitämS 'riucäY.^3.2;  —  vahiäsm  'hii;a..yäsa(s±) väunm  narSi  °räi  maibyäca  Y.  2Ä8;  40- 8;  —  yavaranä  *'ra  (ND.)''  Jamasfä  . . tu  vaf7n3^  (sd.)  ..  Y. /2. 7;  —  'ralibya jsmaspaxibya  Vyt//; — '"Aaurvö.pass{sA^ °rS  ^tuUmS.päkwa  sardkuitrS  N.  64;  — p3r3sat  'rS  asava  . .  xara^ustr^m  Y.  7/.1; —  pik^ra  'ra  Vyt.  //,  54,  55-
BRT.txt:20783:—  alibyS  ..ydi  asäi  dadtn  zastayö  *dru- ßm  Y.^.8;  31.1,  ^5.6;  —  aSibys ..yöi gSul  mSrmdfn  .  .  jyBtüm  yäis  ^grShma (sd.)  asat  varaiä  Y.^2.12; —  qstSngi^A..) ahmäi  y!  na  astai  daiditä  Y.^tf.  18;  — S.  noch  Y.  43.  I  im  Anhang.  ß)  adjek- tivisch; nur  NSm.  mit  «a  (s.  Sp.  izoo  o.); zu  3):  atcTt  ahmäi  ..  asa  (Sp.2340.) atfhaitx  yS  «J  .  .  vandaya^ä  (sd.)  Y.50. 3.  b)  im  jAw,;  das  Relativ  ist  o)  sub- stantivisch: usia  buyät  ahmäi  naire  yas» &JPÖ  ../räyazäite  Y.  62.  i ;  10. 12,  ö^.Tt.", Yx.13.  24,  41 ;  —  anyS  ahmäi  y^  ^^  V"" väslryavarp^i^A.);  daidlt  ahmäi  N.I<?;  V, 5-  34;  —  aitihä  damaya  yä  (NSf.)  ähBtriS tara%ultris  Y.  Ä  7;  —  aya  aibijarsta yä  amxanqm  spxntanqm  Vr.  22.  i ;  — alibyö  mrahyS  .  .  ySi  vS  . .  n^it  . .  äwärO'
BRT.txt:21590:yavarana-
BRT.txt:22959:und  Lehre"  Y.  i(5.  2 ;  —    yavaranS  kascll  raiwya  °na  ", .  oder  wie  die  der  Jahres-
BRT.txt:23550:•  j.,  g.  västra-  n.  'Weide';  i)  'was  das Vieh  weidet,  Gras,  Futter':  pars  *wmS  .. *da>ihsui  aaÄaj  dfrptj(sd.)  *r>m  V.2. 34; —  gSmia  "roAeca  YLjj.  100',  ig.  SA;  — I  Hat  .  .  ahe  nmänake  frapObwS  gaui  .  . \frapiiiwS  'nm  V.J.  3;  — gavsi  .  .  fral^- yamaht  räma^  °r?tncä  dazdyai  (sd.)  Y, J5.  4;  —  ahurahyi ..yasramila  vahm^mlä .  .  gsulca  'rsm  Y.JJ.  7;  —  gavSi  .  .  hyat htm  data  .  .  hads  'rS  gaodaya  %waxilT (sd.)  Y.  2g.  3;  —  'r>m  btnttm  (sd.)  gtrue ..gaodäyüm  nanm  Vr.z,  11;  —  :^ar>h»mca naire  .  .  'nmca  gave  huhhnhe  V.5.30;  — ■ \yavö  mi  maiys  ^arat  'rym  gave  Au^anhe I  V.5.30; —  yavaca  'raca  V.7.32;  —  yat !  bä  paiti  fraiit>m  kärayätt  .  .  yavanamca '  'ranqm(als  Obj.)/a  urvaranqmca  i^arihs.- bairyanqm  ".  .  Getreide  und  Gräser '  lind  Pflanzen  mit  essbaren  Früchten" iV.  J.  4;  g.  53;  —  as.danunqm(sd.)ca ,yavariqm  kasu.dänunqmca  °nanqm  Yt  S. \  39.  2)    'wo  das  Vieh  weidet,  Weide-
BRT.txt:23593:västryavar^z-
```


## [2026-10-17T00:33:09.423Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3780,3792p HUB.txt; sed -n 5945,5953p HUB.txt; sed -n 21585,21596p BRT.txt; grep -n -E '^ *1125\\.' HRN.txt; grep -n -i 'Stössel\\|Stossel\\|St.ssel' HRN.txt | head",
 "description": "Read Hübschmann/Bartholomae/Horn entries for yavar"
}
```


### [2026-10-17T00:33:09.739Z] TOOL RESULT

```
Wb. hat auch ein unbelegtes ydn 'iumentum, vehi-
culum' = skr. yana- 'Wagen, Vehikel' (Vullers) =
afgh. yun gait, movement, carriage, habit, custom*
(Geiger)?
1125. Darmesteter iibersetzt yavarena- durch moulin a
ble* nach der Tradition , deren jurtak drd ('Getreide-
Mehl') aber auf schlechter Etymologie beruht.
1129. Np. yd» *Jagdleopard' = arm. yovaz kann nicht zu
arm. yoiz-k 'Suchen* etc. (vgl, np. razmyoz Kampf-
suchend*) geh5ren.
Das hier fehlende np. y6y *Joch' (= skr. y^ga-^
bal. j(iy) siehe unter juy Nr. 423.VERLORENES SPRAOHGDT.
Dieses Kapitel von Horn's Grundriss habe ich
siyah *schwarz', phi. siyClk aus *5yfl-
vaka-? (neben arm. seav = zd.
syava-) ;
ydr *Freund* (= paz. ayar) neben
yavar^ vgl. mand. adyaura, siehe
oben p. 106.
Jiinger ist arad *bringt* = paz. dwared; yar ^Stossel'
neben yavar H. 1125.
Dagegen blieb dva^ in havan 'Morser*, bavar 'Glaube*,
\g\.  yjtumani:   —   Ti.:  ySlükih.  —   0  Them.
•  j.    yätu'mant-    Adj.    (fem.    'maitr-)
dby  Google
128s
yatumast^ina
yavarana-
1286
i)  'Zauberei  treibend,  hexend':  y5  a/a-^ pq/a  ys  •tnä\. 6^.8;  Yt  1^.56;  —  'maifi (VS.)/aM  V.2/.17;  Ytj.9,  13,16';  —  I jahikayäi  'maityäi  Y.^. 32  j — tanäa  -mmta  \ ^-  '^-  SSi  F.  20;  ^  hamUtayalca  sandamca  ; 'matqmla  Y.  Ö7.  3;  — yäiuUa  °matqm  Yt  1 //.6(?);  — 'ffwWjw  V.J.14GI.  z)  'von'
Zauberern  umgeben,  der  es  mit  Zauberern  j hält,  Zauberergenosse':  wf  rfuft/a»/ (näml.  j sanm  mruyt)  vi  dofuavatbis  vi  yatus  vi  \ 'maßli  Y.  72,  4.  [V,  20.  I :  lies  ySta- '
matqmi\
Ableit.  —  at.  yriluiaänt-  Adj.  'hexend'.  —  Vgl. yäluman-,  ~  Pü.:  yiiül!,  (m  Y.  I2)\  api  hat yälüiän  martän  u  ianäri')  -  Sü.:  /"fr  fäifa- leiiyai  fU  räi}asiiAyah  -,  (lu  V.  7);  yä/üHi. —  >)  Enlsprechend  such  zu  Vt.  ir.  6.
•  j.  yatumas'tama-  Adj.  'der  am  meisten Zauberei  treibt,  hext':  aüa  hmti  'hma  V, f.  14  Gl.
9721:Li 125. yaver, ydr-) 'Stössel (des Mörsers)*.
```


## [2026-10-17T00:33:13.871Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 9718,9730p HRN.txt; awk 'BEGIN{p=0} /\\f/{p++} NR==9721{print \"leaf\",p}' HRN.txt; grep -n -E 'y[aā]var[əe]n|yāvar' BRT.txt | head",
 "description": "Read Horn 1125 and its leaf"
}
```


### [2026-10-17T00:33:14.438Z] TOOL RESULT

```
t. t., den ich nicht zu belegen vermag).
ap. f/ana- *6abe, Gnadengabe' ^) ; aw. yäna; phlv.
yün (Hörn).
Li 125. yaver, ydr-) 'Stössel (des Mörsers)*.
^(;^\j^'^ aw. f/avarenii' ^StösseF (Geldner, Studien I, 50).
\ii26. i/^x *Eis' i/e/ce *Hagel\
i aw. af/a- *Eis', (de Lagard e, Beitr. z. altb. Lex.
i 4"^)), oder Trost* (Bartholomae, Studien II, 55);
päz. yah (L 19)^).
kurd. aty. LW. ye/; oss. d. ye/, t. Jx Eis, Hagel'
^ (148); wa/. yi/.
'il27, yexdan 'Gott*.
,J^o. ^ aw. yazatanqm; phlv. yaztün, yazdän , yaz<i\d\n
leaf 266
```


## [2026-10-17T00:33:21.659Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'st.ssel|m.rserkeule' BRT.txt | head; grep -n -E 'yaon[aä]-|yaon-|ywn' BRT.txt | head -5; grep -n -i -E 'yauviy' KNT_full.txt BRT.txt TLM.txt | head",
 "description": "Search Bartholomae and Kent for pestle, yaona, yauviya"
}
```


### [2026-10-17T00:33:22.133Z] TOOL RESULT

```
4164:•  j.  a-»havana-m. 'Stösscl,  Mörserkeule': hävananO  yat  . .  'tumia  ^vlmanUt  (sd.) N.72.
4930:ai.  nyo'gra-  m.  'Mörserkeule'.  —  Pü.:  ianlir apäi  30  an  i  äseiÜM  sar.
19859:Stössel  in  Bewegung  setzt"  N.  72.
21630:•  j.  y^varvna-  n.  'Stössel'  (des  Mörsers): yai^qm  zayanqm  vastrytke  fsityantU  . .  °mm zgfTfsnö.va-fiarum  ". .  ein  StÖssel  mit  rund- lichem Kop&tUck"  V. /4. 10.
29564:•  j.  havana-  m.  ('Auspresser,  Kelterer') Name  für  die  beiden  Teile  des  loi  Haoma- bereitung  verwendeten  Geräts,  spez.  beim ffaemamÖTsti  des  Trogs  und  Stössels*': fraiarfm{&A.)(it  tl  °»?m  . .  upa.staotni  . .  yö qsui * hanglurvayete  upanmat''  U  °n»m.. yahmi  niyne  nars  aojanha  "das  erstere (untere)  Stuck  deines  (des  Haoma-)bAÖt- sers  . .,  das  die  (.ff<zii/nii-)Zweige  aufnimmt, und  das  obere  , .,  womit  ich  hineinstampfe mit  Manneskraft"  Y.  lo.a; — ^d3ityö*ainyS havanS  *däityS  *ainyS  ya%a  *va  *däifys hita  "der  Vorschrift  entsprechend  sei  das eine  Stück  des  (Äiiowa-) Mörsers  und  der Vorschrifl  entsprechend  das  andre,  auf dass  beide  der  Vorschrift  entsprechen,  wenn sie  verbunden  sind"    N.  J07,  a)    Du,
29567:KompE.  —  Zum  V.  'hav-.  —  ai.  vgl.  aähifä- vaifa-  Adj.  'lut  Somab ereil ung  dienend',  n. Du.  '  Somapressc'.  Vgl.  GON.  KZ,  tS-  526, Bthl.  IF.  5.  370.  —  Pü.j  kävan,  /riltum Aävan  -  aparlum'-'i  hävait  oder  afiar')  Aä^art (vgl.  PüErl.  zu  N.  /o/).  —  ■)  Vgl.  gr.  Ztipt; ■Mörserkeule'.
29869:•  j.  hivana-  m..  Du.  Name  des  zur  Aus- pressung von  Früchten  usw.  dienenden, aus  zwei  Teilen,  dem  Trog  und  dem  Reibel oder  Stössel  bestehenden  Geräts,  'Kelter- pressc':^aitfaOT  zayanam  västryehe fhtyaJÜS .  .  aimana  'na  ".  ,  eine  steinerne  Keltcr- pressc"  '^■14-  10"-  a)  insbes.  von  der ÄäöMapresse,  dem  JlaomaiBÖTsei  (vgl havatia-)'.  'naca  taSlaca  V.i<).g;  —  Aoa- ma/a  'naca  V.  5,  39115.9;  —  asmano 'na  ayanhama  'na  fraoirinmna  Jraisva- yamna  Vr.  J2.  5;  17.2',  Y.  22.  2';  —  fra- snataiibya  'naHbya  A.  ^.  5;  Vr.  10.  z, *N.  A'>;  —  *'nalibya^1  ratujris  ^aya- nhamalibya  *Z3mafnaHlya  N.  loy;  — cvatbya  *nä  nittmaiibya  'nalibya  *rafufni "wie  gross  muss  der  Mörser  mindestens sein,  damit  man  sich  den  R.  genehm mache?"  N.  108*'^.  a)  Du.  als  sing, fem.  J-Stamm^':  'nayäsca  kaoma  hun- vaintyä  asaya  frasätayh  fralSvayamnayä
5412:•  j.  araja^aspa-  m.  EN.  eines  Hyaona- Fürsten":  mairyehe  hyaonahe  "pake  \'tf/. 30;  —  drfantptn^a  'piin  Yt.5.  109;  — tum  yazata    vandar^mainis  (sd.)    'ps  Vt.
6365:•  j.  aSä-yaona-  Adj.  'wo  die  Heimat  des A.  ist' :  garS  nmätum . .  ravSAu  -n^m  Yt_j.  4.
13321:•  j,  *däitya.yaona-''  Adj.  'der  der  ge- hörigen, angemessenen  Beschäftigung  ob- liegt': yäi  -im  ^'torsnla  (Sp.  449  u.)  N.52,
14564:•  j,  flräya'van-  :  'yaon-  Adj.  —  ?  — ,  Bei- wort des  a'^ravan-:  hwam  (nämL  anävim) ' ..ähravanS  °_j'rti>flj  (NP.)  mastlm  jaiöySnte Yt5. 86; —  aS^m  tnq%r^m  mä  fradalsa- ySU ainyat  fihre  vä.,  ähravanäi  vä  'yaone (DS.)  Yt'i4-46.
16122:.  ,.  par»aTi.yaona-  Ad,   (fem. '«3-)  'der  ,^^^^„„^^^  v.2.8;  9; - unslnnhch:'««^
KNT_full.txt:3534:yauviyü DZe 8f, 10; cf. Skt. yavyà. 
KNT_full.txt:20561:10 iy : draya : tya : haeá : Рагва : aitiy : pasdva : iyam : yauviya : akaniya : 
KNT_full.txt:20563:12 уй : tara : imam : yauviyim : abiy : Pársam : араба : yatà : mim : Ката : dha 
KNT_full.txt:28431:ay-/i-/yà- ‘go’ (JAOS 62.271). yauviyd nsf. DZe
```


## [2026-10-17T00:33:28.253Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 28428,28434p KNT_full.txt; grep -n -E '^\\S*\\s*j\\.\\s*yaona-|j\\.  yaona-|yaona-  n' BRT.txt | head; grep -n -i 'Heimat' BRT.txt | grep -i yaon | head -5",
 "description": "Read Kent yauviya entry and find Bartholomae yaona"
}
```


### [2026-10-17T00:33:28.577Z] TOOL RESULT

```
уашлуй- sb. ‘canal’ (§48): NPers. Joi ^water- 
course, canal’, cf. perhaps Skt. (Vedic) yavyd isf. 
‘stream, river’; perhaps deriv. (§144.V) of root 
ay-/i-/yà- ‘go’ (JAOS 62.271). yauviyd nsf. DZe 
10. yaunydm asf. Оле 8f, 12. 


6365:•  j.  aSä-yaona-  Adj.  'wo  die  Heimat  des A.  ist' :  garS  nmätum . .  ravSAu  -n^m  Yt_j.  4.
```


## [2026-10-17T00:33:34.842Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'yaona-  ?n|yaona-  m|j\\.  yaona|yaon-  n' BRT.txt | head; grep -n -o -E '.{60}yaona-.{200}' BRT.txt | grep -v -E 'hyaona|aS.-yaona|da.itya|par' | head -5",
 "description": "Find Bartholomae yaona headword"
}
```


### [2026-10-17T00:33:35.223Z] TOOL RESULT

```
20980:•  j.  'yaona-  m.  '(bestimmte,  fest  zuge- I  wiesene)  Statt,  Satte">:  tistrtm  .  .  yS  . . \ffavazäii€  düralurvalsim  paiti  pantqm ' bcr}3.baxt3m  paiti  -mm  Yt.Ä35;  /J.  S4i I  56,  V.  21.  5;  —  usihista  hqnt.yaUSnhs  (sd.) !  'ntm^a*  avi  zqm . .  usihista  p3iri.haBianuha yehe  tq'ha^ca  vaxSaSca  'ntm  dahät  ahurS masda  ". ,  (du),  dem  bei  (sva.  für)  Geburt
```


## [2026-10-17T00:33:38.786Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 20980,20986p BRT.txt | cut -c1-1500",
 "description": "Read full Bartholomae yaona entry"
}
```


### [2026-10-17T00:33:39.081Z] TOOL RESULT

```
•  j.  'yaona-  m.  '(bestimmte,  fest  zuge- I  wiesene)  Statt,  Satte">:  tistrtm  .  .  yS  . . \ffavazäii€  düralurvalsim  paiti  pantqm ' bcr}3.baxt3m  paiti  -mm  Yt.Ä35;  /J.  S4i I  56,  V.  21.  5;  —  usihista  hqnt.yaUSnhs  (sd.) !  'ntm^a*  avi  zqm . .  usihista  p3iri.haBianuha yehe  tq'ha^ca  vaxSaSca  'ntm  dahät  ahurS masda  ". ,  (du),  dem  bei  (sva.  für)  Geburt
dby  Google
I33I  *yaona-  —  '''yaoidana-  1333
und  Wachstum  AAM.  eine  feste  Stätte  zu- '  geraten  sah,  da  hat  er  sie  mir  fibergeben"
gewiesen  hat"  V.  21. 4.       a)  insbes.  'Heim-  D.  6. 4.        a)  Kaus.  'in  Aufregung  bringen,
Stätte,  Heimat"*  (nur  Komp.).  erregen':    xsttütaheHt   a^itähe   .  .  mand
K«inpA.{?],  E.  —    w.  »gL  yfnaj/-  m.  —   Pü.  yaozaydti  Yt  10.  111.  2)   'in   Unruhe,
```


## [2026-10-17T00:33:45.471Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^(gyūna|gyuna|gyün|yau-|yaun|gyaun)' ISS_alt_DKS.txt | head; grep -n -E 'gy[uū]na|yaona|yauviy' ISS_alt_DKS.txt | head -20",
 "description": "Search Dictionary of Khotan Saka for gyūna, yaona"
}
```


### [2026-10-17T00:33:45.746Z] TOOL RESULT

```
2309:gyüna-, jūna- ‘movement, gait’, and ‘times’, Z 247221 sarvai māñite gyūnu ' resembles the gait of a Поп’, parallel BS süha-vikranti-gümm-; JS 1572 gara ttüjd хара bihīsadā-jūna ' mountain rivers descending with extensive movements’; K 4, 140УІ Aseivareddrsd küla sate ysare gyiima ‘36 ten-million hundred-thousand times', Tib. lan bye-ba khrag-khrig brgya ston phrag sum-£u-réa; 17:120 ysüra jüna; SuvP. 65v2 fau jīna 'once', BS eka-velam; її 21, 15b2 dur jūna, п 92:119 dva drai jüna ' two or three
752:ajum- чо bring', v 110, 32v3 (1 plural) haysgamiyai üjumamá (BS omits) ‘we bring troubles upon it’; rv 410 (ртуйаћа äjumi ' bring a letter’; tr 381775 тата ajumyard padāmdara ‘bring here first’; IV g3bz sur ysai mara hamgrrima üjuma ‘early in the morning bring here into the lampgrama-market'. Later üjdm- п 34:56 khu và spata budarmá para vaysnà ājäme; ājim-, ijimm-, ajemm-, V 64:41 Ājimīdä "they bring, lead (a life)’, п 11374 сй va sika visğna phara ci và üjimi ' as to what is good (and) bad talk who would bring it here...'; ї1 rr4rog phari và ајітӣт 'I bring the talk here’; п 15, 3a2 stūra ajimyarü "bring (2 plur.) the horses'; SDTV 78:812 kira ajemim ‘I bring the küra-(berries ?)'. Preterite ajimda-, тїї 72:161 hia ajindamdi ‘they brought the troop’, H 95:50 ajidauda, v зто, vii r3 ájidamdd. See also pim- “to bring’. Base pa(ti)- with jum- later jäm-, jim-, jem, from уаи-:уи- ‘поче, with increment -т- in јит-, and j- kept in the compound. To Zor.P. yumb-, yumbenitan ‘0 move', N.Pers. Junb- from yu-m- and yu-mb-- (either secondary -mb-, as in Oss. D. dumäg чай’, N.Pers. dunb, Zor.P. dumb, Av. duma-; or increment -m-b-). Base pim- tto bring’ from pa(ti)-yum- through pi-yim-. Av. yaona- ‘place of movement’ is from yau-na-, see куйпа- 'going'. An alternative proposal is to connect with gam, jam- (> fum- due to labial -m-) and so with Yazg. а-јат- ‘send’, Sangleči imu-, 1®йп-:буо8, Lfum-:dyad ‘bring’, Waxi wüzem- 'bring, M.Parth.T. j'm *šam- ‘conduct’, participle jm'd ( =), һиў'т- ‘achieve’, M.Pers.T. дрі tsent’, z^m- ‘lead’, causative z'myn-. But this jam- would not suit Khotan Saka pīm-.
2312:times', v 42, 87v3 drrai jüna, V 59, 129v2 hoda gyüna, v 42, 87v5 hasta jüna, V 40, 63bt nau jüna, їп 93:207 hauda hastá jum, Sid. татуз sim hun ‘once’, Tib. čig rgya; и 3871373 dau јар, ibid. fau jū; п 94723 drai team jū, V 40, 63b3 tcahaulsd jüna '4o times’; second component Z 22-125 daso-gyünau 'tenfold' (quoted s.v. sala ‘year’, gen. sing. salye). From *yauna- ' movement; place, time of movement’, Av. yaona-, O.Pers. yauviyā- ‘channel’, Zor.P. ушай, Pahlavi Psalter yad, N.Pers. jay ‘stream’. To O.Ind. yoni-, Possibly i-eu- from ei-:i- 'to move’ by increment -eu-; not to IE Pok. 507, 308, 511. See also teira-, rrayd.
4498:pim- ‘bring’, participle pīda-, Sid. 14115 2 và pari vi ana dvāsą hausá uskyagtà, pimánq u ttekye ushütta bendnd ‘ог from the knee twelve fingers upwards it is to be brought up and it is to be split above that’, BS Artvà, Tib. уап-па rtin-pa-nas sor bču-gñis-kyi gov-du byin-pa dral-te; v 65, 2дато puni desana тайа ‘І would now bring the pro- fession’; ші i24:87 pimq, BS minaya (not identified; 'bring'?); v 3003 ttye ййтїла pima pu(stakd?) ‘bring with the teacher (BS acarya-) his book(?)'; preterite, v 222/2072 ci và hambata pide ' because he has brought the amounts’, For -in-:-nda-, note also dam-:danda- ' to tame’, Base *рї-уит-> *biydm-- ріт-, with  ajum-, üjdm-, ajim-: ajimda- ' to bring’. 'T'o Zor.P. yunb-, yunbén-, N.Pers. fumb-, jumban- (m~ mb). Possibly to IE Pok. sos iem- ‘hold’, Av. yam-:yata-, see above Jama, with secondary meaning ‘hold towards’, Otherwise a base yau-:yu- tto move’ with increment -m (see isum-, khūm-), in Av. yaona-, above gyiina-, jüna- ‘рай’, O.Ind. yóni-.
7084:title baga-, п 82, 58 vvitvayau drüpadq = п 79:12 vilvayum drüpadà “ће royal (princess) Drüpadi'. Hence *baga- Yauna- ‘of royal origin’ with the Indian name replacing "dropadi- (Epic Sanskrit Draupadi) with Prakrit -adi <-ай (as O.Ind. RV nadd- "reed', RV, AV nadd-, later nada- and BS лаја-; and *argada- 'enclosing Баг! > атрафа-, argala-), Ах. yaona- 'place of movement’, O.Ind. yoni- (s.v. gyūna- ' way"). For baga- O.Pers. baga- (glossed by Akkad. ilu ' god!) is Av. baya- ‘distributor’, Parsi-Sanskrit vibitaktar-, Bogd. Bud. fy- rendering BS deva-, plur. By yit, gen. plur. By'u, By'ystn ‘paradise’, ByBn'k 'altar', Byp'wr 'prince', M.Parth.T. bg, plur. bg'n, adjective bg'nyg, abstract bgyft; bgpwhr,'son of a god’; M.Pers.T. by, plur. В", adjective by'nyg, Zor.P. bg, DEM 413:9 im bay ‘this god! = his present majesty’; "Turkish Iw bág, with suffix bdgrák, as proper name (of the
7671:sira- ‘content, happy, satisfied', v 118, бугу sira-, BS tusfa-; K 1431054 sira samdustá (dyadic, = BS samtusfa-); K 4643 sira sadustd; К. бї, ҷоуг-2 harbeia-m sira samdusta hamya ‘all became content, satisfied'; SuvO. 68r7 bist зға hámáta gyasta dīvate ‘all the deities (BS devatü-) became content’, ВЗ prahargitah хаги babhüvu devatüh; 11 132b3 iyd sird hámáte 'then he was con- tented’; sra-, K 74:62-3 сӣ và sa sira ушії ‘І who have made content'; K 90:754 sira himya ‘were content’. With -váti- (from either -dati- or -tati-), v 99:6 muditta (BS mudita-) siravatà ‘јоу, content’ dyadic; 2 3102 siravátd; Z 5-24. siravete jsa; Manj. 417 sīravā byauddda mesta ' they got great joy’; Manj. 188 siravàá varáse ‘she enjoys content’; K. 30:220 sirada-dasta ' rich in content- ment' (if correctly interpreted, supporting the second component dāti-); adjective, SuvO. 36:6 avamātäna siravátinaina suhána (BS sukha-) иухӣпа рарһайййа ће self must be seated with immeasurable happy joy’; BS acintyaya аішуауа prityacatmanam ѕатіаграуйаоуат; SuvO. 36r6—7 siravatinaina suhäna, BS priti-sukhena. With -oía- sirofa- 'joy', 1 167, 8315 tväñi sirausi hauva paduni ‘strengthens, makes happiness, strength’, BS brmhana-, hargana-, bala-; adjective -avanta-, JS тту iirofüdd sau jambor harbiéd satva 'all the beings of all Jambudvipa were contented’. Compound, SuvO. 56r2-3 ciyd uysano paphandu yanimád u pajsamui yudu yanīmä u sirustanvai padamdu yanimá ' when I can delight myself and I can do it honour and can content it’, BS aimanaq ca samtarpayitvā pratimünayitva samprahargayiteü (to read the last word v 119, бту (syi(rusjayna, BS 1483 jrahrsja-); 1 254, 198vz sirustand, BS pramudita-; Мал). 208-9 буе sirüsjana büima 'gets to the bhümi-stage of content’, see ug/ana- ‘state’, From base sag- to *sagra-, M.Pers.T. sgr *sayr, Pahlavi Psalter sgly ‘satisfied’, giving also the older form of Zor.P. sel, syr *ser, Balöčī sër, N.Pers, sēr, sir. To O.Ind. (RV) fagind- glossed by sukhakara- ' making happy’ from base sag- (not sak- ‘Бе able’), see Indo-Iranian Journal п, 1958, 149-52, hence IE лер-. Three other bases for 'satisfy' are in Waxi зај 'satisfied', Oss. D. dfsadun ‘to satisfy, nourish’, dfsdst, dfsddun ‘be satisfied’, I. afsadyn, dfsádyn, dfsdst; and IE Pok. 876 sü-:s2-, see Indo-Celtica (dedicated to А. Sommerfelt) 18-28 on Ау, hyaona-, O.Ind. (RV) syond-; and sar- in dsada- 'satisfied, fed’, to TE Pok. 577 her-. Here -ira- has replaced -agra- as in tcirau (*éagrüva-) above; sira- is clearly nearer in meaning to M.Pers.T. sayr than to dsada-, though *sarya- would also result in *sira-, see Rira- ‘act’. For West Iranian ér«-agra- note Zor.P. anēr, Av. апауга-, der ‘long’, O.Pers. darga-.
8329:hayüna ‘friend’, SuvP. 63v2 hayunëm, BS mitra, Z 24'449 ysanyau hīssädyau hayünyau jsa ‘with kinsmen, relatives, friends’; v 58, 128v1 odä balysüste yanindd kye hayünu (acc. sing. to -/- stem) ‘up to bodhi-knowledge who make the friend’; v 147, 127b3 asádda (BS asiddha-) hayta *bad friends’; Іп 130, 1b4.ysaiiau -Лауййаи -* with kin, with friends'; v 262, 124 Лауйта idi bisi ' all are friends’; ш 127723 mastam hayinau hiya ' of great friends’, instr. sing. JS 35v4 hayumna; with -ka-, 111 59:17 hayünakyau jsa. Abstract, Bcd 49r4 hayumdausti jsa ' with kindness’, BS mitrā; v 118, 67r2 dätä hayünaustä ісега ' service must be made to the dharma-doctrine', BS dharmiknn janayet sevām; adjective to abstract, SuvO. sr6 Aayiümaustmei aysmi ‘kindly mind’, BS maitri-ciliap; v 106, 2913 hayünaustinai-y-ü aysmiü, BS maitri-citia-. From *ha- yauna- ' of the same place! to AV. yaona- ‘place’, but it would be possible to consider kai- ‘ќо bind’, Av. hiña- ‘companion (?)'. Note also Oss. D. xádzard, І. xádzar ‘house’ from *Ла-ёата-.
```


## [2026-10-17T00:33:54.467Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '(^| )ywn( |$)|ywn[^a-z]' SOD_pages.txt | head -20; grep -n -E '^ *450[0-9]? ' SOD_pages.txt | head",
 "description": "Search Sogdian dictionary for ywn"
}
```


### [2026-10-17T00:33:54.958Z] TOOL RESULT

```
1680:Ill 3jj> j3 JUL* . ju^> oLiy ^r/' n>f A) j         *frywn £sjy-*<i                                                         -^
3107:  /afriwanV *frywn               blessing
3926: 24 "prywn B                           jijl <uk^                  TPS 1966, If
3927:    afriwan ('prywnh) =»*prywn, "frywn
3938:  26 "prywnh       S =* »prywn                                  a8ec(u) =**8c(w)
4006:  53 »«wh B                                                        70 »frywn M                                                            -
4007:                                            <Sj* J. iJ^' ia^^         afriwan ©Av. afrivana         =»»prywn, »prywn,
4445:221 »prywn    B, S                        *jj><J->J*>*<jlJ'i
4446:    afriwan =»*Prywn, 8frywn                                                  Perikhanian, SI 1988, 138
4706:322 "wsywn'k =* 'wsxwn'y
4710:    aw-saxwanc, o-saxune ? ('wsywn'k) ©pi. -/
5399:564 »py»tr B                                    j^>         577 }pywn- =* Py}wn-
5402:       Py»tr                                                      frywn ©pi. -f =»bywny
5642:         habitual                                                  674 'frywn     M, C                                 CjtJ^J^
5643:          BSTii 910.52; C2, 61V22; Bcnv. Et. 1, 318, JA                afriwan =»*Prywn, *frywn, *prywn      ji J * 'J^
5786:                                                              726 'Ys'ywn      B                                o^
5788:                                                                   (3)xsewan Cysywn) ^'Ysy'wn, xsywn
5793:                                                              727 'ys'ywn'k     B                                   ,li
5796:714 >YS,w,n)h   B, S                              o^^U               -ty -^'xsywnCy), xsywny(y), ^sywn'k, MLK(,)
5865:         Frag. 2a. 11            ?                            750 'ysywn =» ^sy'wn, 'ys^ywn
5050:                                                              450 >b C
16556:                                                              4502 Ywyrsny B, S                         ^UaT ^^L <j^
16570:  4503 ywys- B                          o>/is^'o>/3S
16579:  4504 ywyst    S(MD) ** ywycst
16581:  4505 ywyst'k B, S              ^j^a i(jU* <*j&>J t^j            TSP 5.107, 13.13; BSTBL, Dhy. 40, 74, 145; Frag
16593:  4506 ywystk ==» ywyst'k                                         GMS 375, 1230
16594:  4507 ywystr B, S        (J>> y-t-x j->)j^jj* «>j;l>J t^j   4518 yy C                                             ^%$
16607:  4508 ywyz- B                    (oy>y^^)^j^                     xyaryak
16619:  4509 ywyz- =* ywyz-                                        4522 yygpp     S ^ yy5rp
```


## [2026-10-17T00:33:59.112Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '44[89][0-9] +ywn|ywn +[BSMC]' SOD_pages.txt | head; grep -n -i -E 'yon\\b|yun\\b' SOD_pages.txt | sed -n 1,10p",
 "description": "Find Sogdian ywn entry by number"
}
```


### [2026-10-17T00:33:59.403Z] TOOL RESULT

```
3926: 24 "prywn B                           jijl <uk^                  TPS 1966, If
4006:  53 »«wh B                                                        70 »frywn M                                                            -
4445:221 »prywn    B, S                        *jj><J->J*>*<jlJ'i
5642:         habitual                                                  674 'frywn     M, C                                 CjtJ^J^
5786:                                                              726 'Ys'ywn      B                                o^
6279:879 'm'ywn      M
6705:       Dhy. 324; KG 563; 'nVtch, MSP bl03; Hen.                   1035 >nywn     M, S                           -u^.jujU
8323:1575 >skw,yny S                                ^^          1587 ^nVnywn B                            *>£ jU*7 i^J~S\
9225:1897 Vjystyy M                                   .;U/^           1908 Vnglywn      M, C                                J^l
9810:                                                                    2085 'xs'ywn     S                                        \^ Loy^
3096:  /yon/         ^wn              kind          Av. gaona                     For instance, fiyst- (past stem of Pynd-, to bind)
4653:299 »tr xwrndy(y) M                                                         oyon ? auyon ?
6280:    (o)mayon        =>m>Ywny                                   891 >mh =» >m>
6706:       Giants. 70; }nYttc, STii 575                                    anyon     ©*hama-gauna-, MP; Parth. hangon
8325:     dweller                                                    osman-yon
9226:     ozyastc ©pp.                                                     ewangelyon   ©ob. -y
10762:         ew-mayon
11012:                                                                 .J>         piyon, piwan, pewan ? ©<*abiwaina-
11108:      Payan-anyon
12224:     Pyon, Piwan ? OPywn-) ®<*abi-waina\ Parth.              2980 py8,y- B              j-uf j^ijjJ^cJ^hjltjjJ^j*
```


## [2026-10-17T00:34:03.562Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for L in 514 515 516 517 518; do awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' SOD_pages.txt | grep -n -E 'ywn|yawan|yon|place' | head -8; echo \"--$L\"; done",
 "description": "Check SOD leaves near printed page 450 for ywn"
}
```


### [2026-10-17T00:34:03.922Z] TOOL RESULT

```
12:10978 yksy ywn'y B                           J^y.^               10992 ynch S
15:      yakse-yone                                                       inc =^ync                                    fr<±A
--514
64:11017 yswymsyh* -» yswcmsyh}                                         ywnts, ywp*t, ywsmbd
--515
--516
5: 11051 ywk       B, M      {oy y^> j*)^^ i*€ i*j> i*x5& i*A*z     11062 ywntsmyq       C                                    it
11:         C2 p236; ywk\ ywleh, SCE 59; VJ 28b n p92;               11063 ywntsnw C
17:11052 ywq      C => ywk                                           11064 ywny C, S
21:                                                                         STi 39.5, 52.12; C2 gloss. p236; ywny. . . rtw,
24:                                                                          yone
27:11055 YWM()) S                                        (>)j.              yone5/8 (ywnyd/0, ywny56) ©<Av. yaona+
31:                                                                           }yd ^ywn'yS
35:11056 ywn      M, C, S
--517
5:        C2, 57R13: BSTii 903.13                                          =»yxwn-, xwrn-, wyrn-(h), yywn(w),
25:        yutar, ew-tar =»cywtr                                            ptz'ny, yywnk
45:          ©*aiva-dasa-(a)nam       -^ywntsnw, ywnts
49:        ywntsnw                                                       GMS 417
--518
```


## [2026-10-17T00:34:07.558Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==518' SOD_pages.txt | sed -n 15,60p",
 "description": "Print SOD leaf 517 around ywn entry"
}
```


### [2026-10-17T00:34:07.859Z] TOOL RESULT

```
         C2, 52V11, 68V15                                                Sund. AoFi 1974, 9R 3 p244               J>>^ <(->y
                                                                                                                                 (^i
11052 ywq      C => ywk                                           11064 ywny C, S
11053 ywk'Ps'k          S => ywk fs>k
                                                  JU»JLj i^Jy^S          immediately
11054 ywk fs'k M
                                                                         STi 39.5, 52.12; C2 gloss. p236; ywny. . . rtw,
      yok-fsak (ywk'fJs'k)
      teachings                                                           "as soon as" MSP b26; Frag. Len. 68.11
                                                                          yone
      GMS 1635
                                                                  1 1065 y wny8 B, M, C             ^k->> i^o^ *'jy
11055 YWM()) S                                        (>)j.              yone5/8 (ywnyd/0, ywny56) ©<Av. yaona+
      day ©Idg.
      me9
                                                           JJJ
                                                                           }yd ^ywn'yS
                                                                         immediately, at once, on the spot
       Anc. Lett. 1.2, 3.23, 6.2                                         GMS 23, 1109, 142a, VJ 1266; TSP 13ii 3, 4;
                                                                           BSTBL, Padm. 55; SCE 215; STii 7.10; BBB
11056 ywn      M, C, S
                                      (^^r>> <U- < jl£*                   f45> Frag. Len. 84a6; MDii p215; KG 446,
       yon ©<Av. yaona =»ywny5
                                                                          467; MSP b89; Hen. Tales. 472; STi 84.8;
       place, on the spot
                                                                          Lentz. STii 5.26 p601; C2 p236; ywnyyS, Hen.
       GMS 1109A 1420; MDii, Nov. 4R 14 p22; BSTi
                                                                          JRAS 19
         111, 152; Frag. Len. 68.11
                                                                  11066 ywnySS      M =* ywny5
11057 ywn>k B, S                               ^1
      yone ?, yune ? (ywn*y, ywny(y)) ©demons.                    11067 ywnyd/8      C =» ywnyS
         pron. m. & f.
      this                                                        11068 ywny(y) M, B ** ywn>k
                                                                  11069 ywp'i M, C                                    jUX
       GMS 1492-5; VJ pl23; TSP p278; SCE p75;
                                                                        yu-pat, ew-pat
         BSTBL pl45-6; STii 7.40, 35, 10.15; Frag.                      once
         Len. pi 12; Anc. Lett. 3.6, KG 327; Hen. Tales.                STii 3.50; BBB pi 02 f6, 1; p\ GMS 1327
         466.3, 18; ywn>kwy MDii A-19R7; ywn}x, S W,
         IIJ 1976, Frag. 5.4                                      11070 ywp'tqy     C                   ^jf^jj ^      "J^±

11058 ywn'y      B =» ywn>k                                             all at once, altogether
11059 ywn>y8 B, S                          hj<d;±J>                      yupat
                                                                        STi      ? GMS 984, C2, 83V4 n pl63; Sogd.
                                                                             70.11;
```


## [2026-10-17T00:34:12.998Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'yôî|yoî|yôi|y[oō]y\\b|jôî|yauviy|ýauvi' BQT_v2_pages.txt | head; ",
 "description": "Grep Borhan vol 2 for jôy/yauviya"
}
```


### [2026-10-17T00:34:13.402Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:34:18.345Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {if ($0 ~ /جوی/ ) print NR-1\": \"substr($0,1,80)}' BQT_v2_pages.txt | head -20",
 "description": "Find Borhan vol 2 leaves containing جوی"
}
```


### [2026-10-17T00:34:18.696Z] TOOL RESULT

```
2:                    ‫م‬ ‫و‬
‫نآکو سخنیم بیاموزد مرا‬
                       ‫د‬ ‫
10:          ‫س‬
         ‫و ی‬                                                     
16:  ‫سین وس‬                                                                       
20:  ‫¬=“‬                                                                          
23:                                           ‫بیان چهارم‬
                     ‫درج
25:                                                         ‫بیان ششم‬
             
27:   ‫جره‬                                                                         
28:     ‫وبا وت‬                                                                    
33:                                              ‫بیان بدارهم‬

               ‫در ج
34:     ‫‪۷۹‬‬                                                                      
35:                                          ‫بیان دوازدهم‬

                    ‫و
```


## [2026-10-17T00:34:30.449Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 57 58 59 60 61; do echo \"== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | grep -o -E '[A-Za-zâîûôêāīūōē]{3,}[^‫]{0,40}' | head -15; done",
 "description": "Look at Latin strings in Borhan vol 2 leaves near page 602"
}
```


### [2026-10-17T00:34:32.092Z] TOOL RESULT

```
== leaf 57
natnubesoj .‬‏‬         
== leaf 58
nidrevhsû‬ز‏ ‪nin .‬‏ ‪hsû‬ز‏ ‪ .‬بلرچی ‪ ( [8206
== leaf 59
== leaf 60
dzubãr‬کربرسن ‪: ۸۷۰‬‬
== leaf 61
```


## [2026-10-17T00:34:38.503Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==60' BQT_v2_pages.txt | tr -d '‫‬‏‎' | sed 's/ \\{3,\\}/  /g' | head -80",
 "description": "Print Borhan vol 2 leaf 59"
}
```


### [2026-10-17T00:34:38.975Z] TOOL RESULT

```
  �ولیدن  ات  =




  �۱  ات  گنستك
�و لقی * = بروزن و ی �ولخی
 است که قلندرشال پوش�باشد " وختح اول کوسر
  �ول � -بورزن غول � .غلیوا� را
  �ال� هم امده است �.  گونند �. ۴
�و له � -بضم اول و قتح �ال� و ظهور  �و لاه � -بورزن روباه � ۰بافنده را
ها » مخفف �ولاه است که بافنده � -و عنکیوت  را نز کفته اندکه عربان  و عنکبوت  گونند 

باشد � -وبخفای ها» تیردان وئ رکش را گوبنهب  دلدل خواننن �۴

و بمعنی کیش و قربان همآهده است » و آن  �و لاهك � = ۴بر وزن روباهك �.
  عونی
  بدم�-
  �ابی باشد که کمان را در آن هن  عنکموت را گوند � -وتصذیر �ولاه نزهت که
زده شده همآمده است آعم از یشمو پنبه وغیر
  بافئده باشد �.
 آن � -و خاریشت بزرکه را یکزفته اند س
 وبهندی *�٩علتی است کهآ نراسربی�فالخوانند  مر�-وف است که بافند�.
  �لواهه �°
باشدکهآدرامرغ  سعییاززه
  وبا واو م�پول نو  باشد � -و عذکیوت را نیز گوند �.
  و فریز گوبند �.  �و لخ ۔ باانیم�هول بروزن دوزخ؛
 �وله گاه � -با �انی م�هول بورزن  نوعی از بافتهةٌپشمینه باشد که ازآن خر�ین
 بوسه گاه » بمعنی �وله زارباشد که آنرا مرغزار  وردم فقیر ودروش وقلندران هم
  سازند ع
 کوبند� .ومرغ علفی�است که حیوانات نرابرغ�ت  پوشند �٩ �۱


  تمام خورند �.  د بروزن دوزخی � .قلندر  �و لتی
 و ها� .مخنف  لحت
  اتلوهه �-
  �  �.  ناد
  نرووش
  گل ی
  شا
  �ولاحه است که بافنده � -و عنکبوت ماشد�.
  �و لق » باقاف � .بروزن ومعنی �ولخ
  لیدن
  ژوی
  �و لیدن � -بورزن و  است که بافتهٌ پشمینه باشد » و بفتح اول وکر

  است که از همرفتن وپربشان شدن باشد �٩۷ �.  ال� همکونند �. ۸


  � - ۱رك � :چفك � ,چنوك � ,چکك� ,چکوك� .چگك �.
  درطبری �1ز � ,چالقان (مرغ شکاری) است � صاب طبری� »۰۷۲ت�حفةٌ حکیم موّمن  �۴
  چلقان را اسم ترکی حداة دادته کهغلیوا� است�� .واژه نامه �.»۰۷۲
  نهکویوت آمده است  عفند
  �-� ۴یوشیده نماند که لفظ �ولاه و�وله باظهار ها بمع�ی با
  و�وله باخفای ها بمعنی خاریشت و غیرآن� .چنان�ه صاحب برهان وفرهنك �هانگیری وغیرها
 تصریح نموده آند و دادل سمتین درعربی بمعنی خاریشت بزرك آهده له بمعنی عنکیوت » لیکن
  چون لفظ �وله مخفف �ولاه هم آمده و آن�صورت خطی بلفظ �وله باخفای هاکه بمعتی�خاریشت
 آمده مشابپت دارد صاحب برهان را اشتباه وافع شده رگفته عنکبوت را یز گویند که ری دلدل
  � - ۴صورت قدیم � :�ولاحه �.  �.  �۹ص�6�ِ۰ة
  خوانند» �چك حاش
  رك� :�ولق » �والق �.  �۱  � _ ۵رك � :حولاحك �.
  رك � :�ولخ »  �۵  ینبت) � .رك � :�ولقی �.
  � - ۷از � :�ولخ (ه�.م ) �( +
  � - ٩از � :�ولق (ھ�.م� 4 (.ی (لست)� .رك� :�ولهی�.  �والق �.
  طولخم ظفلتلا �.دتیوگاپب »
  �- ۰حندی [� ( 0012یتس � � ).یدنهرد هلوپ�اب می�
  � - ۱كر � :ندیلرژ �.  � كچ � .ةشاح �۲4۹ص �.
```


## [2026-10-17T00:34:44.936Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 60 61 62 63; do echo \"== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | tr -d '‫‬‏‎' | grep -n -E 'وی|yu|yo|jo|ju|اوستا|پهلوی|بهلوی' | head -20; done",
 "description": "Search next leaves for جوی entry and footnote"
}
```


### [2026-10-17T00:34:45.512Z] TOOL RESULT

```
== leaf 60
14:�وهر کویند � -و �ابی را یزگفته اندکه در
15:                آن �وی آب روان بار باشد �.                  �دانشده�باشدیگر دا نندنا غله�از کاه حدا شود � ۳ے
22: �هوی � ۰بروزن کوهی ؛ نگالمی است                            کشده بورزن احان » بلفت زند و پازند (�)۲
25:�یویار �١ با بای حطی ونای اب�د                             وان چومی�باشد که بر گردن گاو زراعت اهند �۴
28: بر وزن کوهار * کنار �وی آب راگوبند �-                      �وهز ده بفتح اول بر وزن کوئر �
29: و �ایی که دران �وی آب بسیارباشد � -و�وی                    معرب کوهر باشد که مروارید است � -و یمه�تی
39:   � 38را�م بطربقة بدست آوردن سعادت د وبلیامز �� »۷۵۸:۲د کتررا �ا» بنابرین کتاب م�وی
52:   � . [08۷11 - ۴قرائتی ازکلمة �,هلوی �( 03۷۷۷�وان) رك � :�وان و رك� :بونگر �۸۷۰
54:   � - ۱از ت:وی � -۳بار (پسوندمکان) اشکاشمی                      است کوچك خوشبو برنك سفید مابل�بزرد�.
56:   � #�وی � -یارسی باستان � . 8۷۱۷۷2۷-پهلوی � [10با ل[ » هندى باستان �2۷۷712۷
59:           رود کی سمرقندی�.            باد بار مهربان آبدهمی�.       بوی �وق مولان آبدهمی
60:                                            �#�ویدی � -بفتح اول و چهارم ؛ رك � :�اوبدن �.
== leaf 61
14:                  �ها نيدده کن                       را نیز گویند » و بکراول هم�امده است� -ومال
15:                                دننده باشد �.                        و اسباب دلیوی را هممیگویند�.
17:                                       � :باو    �ك    ))          چك� :زند ویاژند �.    ()
23:    � - ۱پپلوی �( [18زن بدکار) �مناس�۲٩ :۷۷۲ �نییر ک� ۹۱۱»۰دراومتا �� 13بلرتولمه
25:� - ۴پهلوی �( 020168عالم) * اوستا � 200638بب رکے� � »۸۰استق� .*۹ر گبهان�.
28:    � - ۴بهر دومعنی » حانظ دربارٌ امیر مبارزالدیین محمد ومیل کشیدن چشمان وی بامر
== leaf 62
12:                                                  کویند که ماسوی الله است و عرب عالم کبیر
32:              �-ر �دامدات�تمك» ونيز �بندهش بزرکگف» دو اصطلاح پهلوی ذیل آمده �:
39:   مهین» ب�ای ک�یپان کزرك» پهلویو�ما کرس کسمس» بونانی� ,و��هان کین� ب�ای< کیانکودك»
42:    �۶ص �.*۷۳۳     �م�نوی چاپ�میرزامحه�ود �۲۰۳
43:   �پلوی � . 6720اوستا � ۰ 4۲×4هندی باستانی �8761۵0-
== leaf 63
4:وآن چیزی بود ازکندم وآرد و نان وام�ال آن               صفاهان را گویند عموما � -وبلوکی از بلوکات
5:          که ب�پت غلام و لوکرمقرر کنند �.                آنرا خصوصا � - ۱ویفتح اول دهی است ازولات
6:�یز �نگ � _ .با�یم وزای�هوزبروزن                        بز�-بان زد وپازند(� )۲بمعنی پاكویاکیزه
17:                                   بر                      پابای فارسی همآمده است که بکرویزینا
21:    سوکون �الیویون کواف » ناکمر�ای                      وزن دیگر» بمعنی فرادیس بودکه�مم فردوی
35:       (� )۳چس� :خیز زنگه�.               (� )۲چك� :ژد ویاژند �.                 )� ۱چش � :هده
39:   � - ۱پپلوی ل�� 3شپرستانهای ابران � .مارکوارت� .چاپ مینا ص � ۱۲و�»4*۱ورك�:
```


## [2026-10-17T00:34:50.420Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==61' BQT_v2_pages.txt | tr -d '‫‬‏‎' | sed -n '1,4p;20,32p;50,60p'",
 "description": "Print relevant lines of Borhan leaf 60"
}
```


### [2026-10-17T00:34:50.814Z] TOOL RESULT

```
  � ۵ ۲ات
                                                                                                  �ومت

هورك از سنگهای نفسه همچو المای وباقوت                    � = ۱بفتح اول وسکون �انی         �ومت

                      فروش را نگیوزبند �.                  چووان � ۲ه کر اول و واو بالف
 �هوی � ۰بروزن کوهی ؛ نگالمی است                            کشده بورزن احان » بلفت زند و پازند (�)۲
در هندوستان وا نرا�وئی� 6یز گوبند که ب�ای                            بیضا بشید �.بمعنی �وان است که نق
                         ها بای حطی باشد �4 .               �و�٥ بروزن کوه » بمعنی��وغ است »
�یویار �١ با بای حطی ونای اب�د                             وان چومی�باشد که بر گردن گاو زراعت اهند �۴


 بر وزن کوهار * کنار �وی آب راگوبند �-                      �وهز ده بفتح اول بر وزن کوئر �
 و �ایی که دران �وی آب بسیارباشد � -و�وی                    معرب کوهر باشد که مروارید است � -و یمه�تی
بزرگی را نیزکوبند که از �وبهای کو�ك بهم                    وحودمطلق ومو�ود لافی موضوع وموصع بود
                              �¥   �.    باشد   ه   رسد      دز را نز گوشب      نز نزاد � -وماد هر      دص

  � -اکنون در اصفپان آنرا � 01116کوبند �فرهنك�نظام»» دراراك                         مزدیتا �. 1۸4-۰1
                  (سلطان آباد) � 006وعمل خرمنکوبی را �چن کردن» کوبند � ( .مکی نژاد)�.
   � . [08۷11 - ۴قرائتی ازکلمة �,هلوی �( 03۷۷۷�وان) رك � :�وان و رك� :بونگر �۸۷۰
 �-۵شکل قدیم دنراار�,دو لافلا � ,و آن کلی                           رك � :�وغ » � » بوغ �.         �۴
   � - ۱از ت:وی � -۳بار (پسوندمکان) اشکاشمی                      است کوچك خوشبو برنك سفید مابل�بزرد�.
                                                                              � * dzubãrکربرسن �: ۸۷۰
   � #�وی � -یارسی باستان � . 8۷۱۷۷2۷-پهلوی � [10با ل[ » هندى باستان �2۷۷712۷
   کردی ع از � .افغانی � . [2۷0بلوچی �( [۵ب�1رو » آبراهه) *اسشق� ۱۳46ورك" هوبشمان�۱۳4؛
                   رود کوچك » م�رایی که آب را از آن �هت مشروب کردن ی عبور دهند �:
           رود کی سمرقندی�.            باد بار مهربان آبدهمی�.       بوی �وق مولان آبدهمی
                                            �#�ویدی � -بفتح اول و چهارم ؛ رك � :�اوبدن �.
```


## [2026-10-17T00:34:59.023Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ *423\\.' HRN.txt HUB.txt | head; grep -n -A4 -E '423\\. *j' HRN.txt | head -12; grep -n -B1 -A3 -E '^ *423\\.' HUB.txt | head -12; grep -n -E \"\\bjōy\\b|jōy |jwy\" PHD_mackenzie.txt PHD.txt | head -5; grep -n -i -E \"y[oō]y\\b|jōy\" NYB_vol2_glossary.txt | head -5",
 "description": "Look up jōy in Horn, Hübschmann, MacKenzie, Nyberg"
}
```


### [2026-10-17T00:34:59.433Z] TOOL RESULT

```
HUB.txt:1713:423. Dazu afgh. LW. juy 'the yoke of a plough'.
HRN.txt:3943:423. Juy *Joch', vergl. yöy.
1712-*springen' = 'sieden') unsicher.
1713:423. Dazu afgh. LW. juy 'the yoke of a plough'.
1714-424. Tax afgh. LW. jiift genau, richtig, Paar gehort
1715-noch juftdk *das Ausschlagen, der Tritt rait beiden
1716-Hinterbeinen = np. jufta, \m Balufi kommt auch
PHD.txt:125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
PHD_mackenzie.txt:562:       Jiidan      I M jwwdn, jwy- ...
311:*ähöyenitan, pt. = pret. pass. *ahdyénit ['hwkynyt'!] "to insist on (pat) 383. — Meaning approximately clear; reading hypothetical. I take it as the caus. *ayöden- of OP yaud- ‘to be in commo- tion’, Av. (1231 sq.) yaoz-, v.s.v. āyēz. This *äyöden- having developed into *ayoyén- io SW, the first -y- was dropped and -h- inserted to fill the hiatus, ac- cording to the cominon rule; -k- is only graphic, as often after a w to assure its reading as -0- — if -k- is not simply (by no means uncommon) the defective form of the old letter d (cf the Ps.): *hwdyn-. — Commonly the spelling *hwkynytn' stands
```


## [2026-10-17T00:35:04.685Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'yauviy|Kanal|Bach\\b' HRN.txt HUB.txt | head; grep -n -i -E 'stream|canal|brook' PHD_mackenzie.txt | head -8; grep -n -i -E 'canal|stream|brook' NYB_vol2_glossary.txt | head -8",
 "description": "Search Horn, Hübschmann, MacKenzie, Nyberg for stream/canal"
}
```


### [2026-10-17T00:35:04.962Z] TOOL RESULT

```
HUB.txt:1315:ner erschliesst sie aus np. pars *Bach*, das Horn
HUB.txt:5294:Joi, Jo 'Kanal' = ap. yauviyd-; Jam = Jammed = zd. yima
HRN.txt:2912:301. pers 'Bach, Quell'.
HRN.txt:3994:ap. yauviyä'^); phlv. jöi bezw. yöl; ai. yavyd'.
HRN.txt:3995:LW. kurd. /i?; Sity,jova; bei. /ö * Wasserlauf, Kanal*
HRN.txt:6778:Etym. d. Bai. unter No. 66; bei. ö[ur 'Giessbach'
HRN.txt:7563:vergl. auch feryen neu gegrabener Wasserkanal' neben
HRN.txt:8886:1024. näv Wasserkanal; Schiffchen', nävdän.
HRN.txt:14316:yauviyä' 431.
3080:jo(y) [ywd, ywb ' I N --] stream, channel.
7692:stream joey).                              sulphurous gogirdomand.
3307:rēcišn [lyešn'] the act of flowing, stream- ing 85??. 867. — V. rextan.
4240:vitartan [wtltn'], viturtan [wtwltn'], vi- taštan [wtštn'], vitir- [wtyl-] to pass: andar dašt bē vitart passed over the plain 318; pat kustak + deh vitart passed outside the village 619-17; to pass by 7!1.15.22; bē vitast drove ahead 71’; to cross a bridge 7225.27; to go through a stream 101%. 10323; kë vitīrēndv the passers-by 12815; — pt. vitart, viturt deceased: vitart coll. the deceased 837. 8413; viturtān martūmān 10517. — Av. (640) vi-tar- = OP; MPrth w(y)drdn w(y)dr- (S, MHC); MPrs pres. wdyr- (S); Ps. pt. wilty, pres. wtyl-, wtl-; Paz. vadardan vadirdan, pres. vadar-, va- der-, vadir-; NP guöastan guóar-. Verbum 206, Ghilain 57.
4772:Pap. Kraeling — The Brooklyn Museum Aramaic Papyri. New Documents of the Fifth Century B.C. from the Jewish Colony at Elephantine. Edited ... by Emil G. Kraeling. New Haven 1953.
```


## [2026-10-17T00:35:08.737Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3990,3996p HRN.txt; awk 'BEGIN{p=0} /\\f/{p++} NR==3994{print \"leaf\",p}' HRN.txt; sed -n 5292,5296p HUB.txt",
 "description": "Read Horn's jōy entry"
}
```


### [2026-10-17T00:35:09.210Z] TOOL RESULT

```
ai. yüs-, yüsdn- 'Brühe*.
LW.(?) kurd, jüSverdin, jüsdnin; hei, jösenag 'kochen,
sieden; aufbrausen, zürnen' (181).
431. jöf, jö *Kanar.
ap. yauviyä'^); phlv. jöi bezw. yöl; ai. yavyd'.
LW. kurd. /i?; Sity,jova; bei. /ö * Wasserlauf, Kanal*
(117).
leaf 110
zd. yakare ; Jau *6erste' = zd. yava- ; javan, juvan 'Jung-
ling' = skr. yuvan'\ jOsTdan *kochen, sieden', Wzl. Iran. yaus\
Joi, Jo 'Kanal' = ap. yauviyd-; Jam = Jammed = zd. yima
— xsofta-. Dazu das LW. Jahud, JuhUd^ afgh. Jahud, phi.
yahut Phi. Min. p. 32, Z. 1, arab. yahud, hebr. ''TlH^
```


## [2026-10-17T00:35:14.220Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=%D8%A7%D9%88%D8%B1%D8%B4%D9%84%DB%8C%D9%85",
 "prompt": "Quote verbatim any Mo'in (معین) entry for اورشلیم, including etymology (عبری etc.), and Dehkhoda's etymology if present."
}
```


## [2026-10-17T00:35:15.257Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=%DB%8C%D8%B4%D9%85",
 "prompt": "Quote verbatim Mo'in (معین) and Dehkhoda entries for یشم including origin tags (e.g. [ع.], [تر.], یشب)."
}
```


### [2026-10-17T00:35:19.405Z] TOOL RESULT

```
# یشم (Jade)

## Definition
According to the Amid Dictionary, یشم is "a stone resembling agate or chrysolite in various colors: white, blue, and dark green."

## Dictionary Entries

**Mo'in Dictionary:**
"(یَ) (اِ.) یشپ; a precious mineral stone in dark green and blue colors."

**Dehkhoda Dictionary:**
The term refers to "a valuable precious stone brought from China or India," traditionally believed to protect bearers from lightning strikes.

## English Equivalents
- Jade
- Opal
- Jasper

## Related Terms
- **یشمی** (yašmi): adjective meaning jade-colored; a deep green shade
- **یشم اعلی**: jadeite (gemology term)
- **یشم سان**: opalescent quality
```


### [2026-10-17T00:35:19.424Z] TOOL RESULT

```
# اورشلیم - معنی و تعریف

Based on the Persian dictionary content provided, here's what I found:

## Main Entry

According to **Dehkhoda Dictionary**, the entry states: "اورشلیم . [ ش َ ] (اِخ ) رجوع به قدس شود" - indicating that one should refer to the entry for "قدس" (Qods/Quds) for the complete definition.

## Related Translations

The page shows several dictionary matches:

- **English-to-Persian**: "Jerusalem" translates to "اورشلیم، بیت المقدس" (Jerusalem, Bait al-Maqdis)
- **Persian-to-English**: "اورشلیم (شهر)" renders as "Jerusalem, Zion"

The dictionary also lists various compound terms containing this word, such as "Jerusalem artichoke" and "Wailing Wall" (دیوار ندبه در شهر اورشلیم).

Note: The source content does not provide detailed etymology from Mo'in dictionary or extended etymological information beyond the cross-reference to "قدس."
```


## [2026-10-17T00:35:25.138Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%8A%D8%B4%D8%A8",
 "prompt": "Quote the Arabic etymology and meaning for يَشْب (yašb) verbatim, if any."
}
```


## [2026-10-17T00:35:25.788Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/jasper",
 "prompt": "Quote the etymology of jasper verbatim."
}
```


## [2026-10-17T00:35:26.669Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DB%8C%D8%B4%D9%BE",
 "prompt": "Quote Persian etymology of یشپ (yašp) verbatim."
}
```


### [2026-10-17T00:35:27.101Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-17T00:35:27.345Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-17T00:35:30.751Z] TOOL RESULT

```
# Arabic Etymology and Meaning for يَشْب (yašb)

**Etymology:** The word is "Cognate to Hebrew ישפה; probably ultimately from Persian یشپ (yašp)."

**Meaning:** يَشْب (yašb) is a masculine noun with two primary meanings:
1. Jasper (a semi-precious stone)
2. Jade (another semi-precious stone)
```


## [2026-10-17T00:35:39.032Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo AFM; grep -n -E 'يشب|اليشم|يشم' AFM.txt | head -5; echo LKT; grep -n -i -E 'jaspis|jasper|ja[sš]p' LKT.txt | head -5; echo SKT; grep -n -i -A3 '^jasper' SKT.txt | head -8; echo SKTJ; grep -n -i 'jerusalem' SKT.txt | head -3; echo TAD; grep -n -E 'يشب|يشم' TAD.txt | head -3; echo FSD; grep -n -i -E '^jasper' FSD_vol*.txt | head -3; echo WEB; grep -n -i -E '^jasper' WEB_vol1.txt | head",
 "description": "Grep Semitic and English references for jasper/yashb"
}
```


### [2026-10-17T00:35:39.484Z] TOOL RESULT

```
AFM
461:وقال !)ܝܣ : هو دواء هندي يشبه المندق الاان فيه ;; ,80 قليلا الى الغسبرة ما هو 
735:( البربط ) العود تعريب برت واصل معناه صدر ܐܠ( لاله يشبهة ٠‏ ومنة 
918:بز فمن يون أي يشبه البز ٠‏ ويون لغة في كون بالفارسية 
1375:0 0 معناه فارة السسش وهو حيوان يشبه الفارة يسكن في اصل !+ ٠‏ وفي 
2030:ابيض يشبه الصوف وورقها كورق التين ماثل | 
LKT
2260:'Grüner  Jaspis' ;  hieraus  über  tk.  jesem russ.  serb.  Jasma  'dass.'.
SKT
SKTJ
TAD
523:نفس يوئاني 09كاوم وهو شجر يشبه الاآس خشيه صاب 
849:جلبان وفي الفارسية 2 جَنايان © وهو حب يشبه الماش 
1266:يشبه السلق 
FSD
FSD_vol1.txt:42750:Jasper   
WEB
```


## [2026-10-17T00:35:43.896Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2255,2262p LKT.txt; grep -n -i -E 'jasper' SKT.txt | head -3; sed -n 42750,42762p FSD_vol1.txt | head -14",
 "description": "Read Lokotsch yašm and Skeat/FSD jasper"
}
```


### [2026-10-17T00:35:44.224Z] TOOL RESULT

```
939.  Tk.  jasak:
'Gesetz,  Verordnung;  Verbot'  [Kelekian Kämüs  1338  und  1352;  vom  Stamme jas  'Reihe,  Regel,  Gesetz'  Vämbery TktEtWb  S.  123,  Nr.  134.  Die  Ansicht von  Bern  SlEtWb  448,  das  Wort  sei ar.,  ist  ein  Irrtum;  umgekehrt  ist  das tk.  Wort  mit  dem  Suffix  des  Berufes als  jasäkgl,  jasakgi  ins  Arabische  über- gegangen: äg.  Dialekt  jasäkgl  'Kawaß' ZDMG  LL  310  und  Dialekt  von  Damas- kus jasäkgl  'Türhüter,  Schließer'  Halim Dammüs,  Kämas  al-'awwäm.  Damaskus 1923.  S.  3Ö9];  hieraus  h\x\%.  jasak,  jesak 'Verbot,  Wache',  serb.  jasak  'Verbot', russ.  jasak  'Tribut,  den  die  Stämme Sibiriens  in  Form  von  Pelzwerk  abzu- liefern haben'.
940.  Tk.  jazdyk:
'Kissen'  [vom  Stamme  jat,  jas  'liegen, ausstrecken,  flach'  Vämbery  TktEtWb S.  126,  Nr.  138];  hieraus  bulg.  >s<iit 'Kopfkissen',  serb.  jastuk  'Kissen,  Pol- ster'.   [Bern  SlEtWb  449.
941.  Ar.  jasm:
'Grüner  Jaspis' ;  hieraus  über  tk.  jesem russ.  serb.  Jasma  'dass.'.
942.  Pers.  jäsämln:
'Jasmin'  [at.  jäsamün,  gr.  idcr|ur|];  hier- aus mit  Anlehnung  an  gelso  'Maulbeer- baum' it.  gehomino,  gesmino,  mlat.  gel- seminum,  jesminium,  prov.  jaussemin, jensemil,  frz.  sp.  jasmin,  pg.  jasmim, kat.  gessami,  rum.  iasmin,  iasomie,  as- monie  [letztere  Formen  über  ngr.  fia- aou|u{] ;  dtsch.  Gelsemin,  Jelsomin,  jas- min, Schasmin,  engl,  jasmin,  jasmine, ndl.  jasmijn;  russ.  bulg.  serb.  jasmin, ßech.  jasmin,  poln.  jasmin.  [DE  291. Eguilaz  432.  Devic  DEt  145.  ML  4577. Kluge  218.
9437:^Littr^),  an  occa- i  jasper.  —  1-  ioj' Gk.  lOOirir.'Arab. tM,   JA<>(«r ;    whence    Ven. jttpef.     CX  Heb.  ydjkpkth,
Jasper   
.   .   .March.
Chrysolite  
.September.
Sapphire.  ...
...  .April.
Aquamarine  or
Chalcedony, Car-
Beryl  
.   October.
nellan.orAgate.Mar.
Topaz  
.   November.
```


## [2026-10-17T00:35:56.144Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'أوار|اوار|آري|الآرى|آرى' ARB_mo3rb.txt | head -10; grep -n -E 'أوار|آري|أوري' ARB_abdulraheem.txt | head",
 "description": "Search al-Jawaliqi for awārī/ārī"
}
```


### [2026-10-17T00:35:56.447Z] TOOL RESULT

```
3907:اوارسيا من تغلب انة وائل اه جاه يمن نسم أشائب 
4256:وقالوا ق أدم الموضع » أوارة » ٠‏ قال #>روبن ملقط الطانىي : 
4258:هأ !1 . خحرة أمه ي* بالسقح اسفل من أواره 
4878:لما لم هده ظنه «عيدى بن عاتك أو ابن فاتك اتخطى » وهو أحد شعراء الاوارج 6 ذكره المر ز بانى 
17491:(3) < الوعوع »> و« الوعواع » دو ابن آرى ٠.‏ 2 
20679:فراسم ©» قل فأ د فافع بن الأزرق رئيس الأوارج 6 فى دقعه ينبم وبين أهل
```


## [2026-10-17T00:36:00.078Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4243,4275p ARB_mo3rb.txt",
 "description": "Read al-Jawaliqi entry for Uwāra"
}
```


### [2026-10-17T00:36:00.562Z] TOOL RESULT

```
قال أبوفييدة 5 غك تأورى شل » بكسر اللام ٠‏ وقال : هو عبرانىي مدر نبا 6 
00 


0 معن + سر 
والشمر اها وعاء نور فوا القافك الرمع ل الاو وده فلع 





زفق 
1 0 00 31 2 
وقالوا ق أدم الموضع » أوارة » ٠‏ قال #>روبن ملقط الطانىي : 
2 اج سسا َه 1 2ه 00 لير 
هأ !1 . خحرة أمه ي* بالسقح اسفل من أواره 
لكر و 03 2 52 
5 و نأء» ٠‏ شت الممقدس [أيضا ]| 0 وهو معرب 03 قال الفرزدق 3 
ه11 ل را عرو يم و هس سا سكل تر 
و يتان بنتث الله حكن ولابه #* واطلت باعل إباياء مشرف 
و : 0 5-8 3 فق 3 الوق 0 
واطمزة فيه فاء» والكمة ماعحقة د« مطرمساء » و« جاععطاء © وى الأرض 
)9 تك 0 
سو قر 
اد زر 5 كل 
)0( يذكر اءم جرير فى 2 (؟) فى © زيادة نصها « ونسبته للاأعثى »> وأملها 


استدراك من بعض الناسغين ه وقد ذ ىر ياقوت اليت فى موضعين مذو با الاأعثى ( وم ام) 
ولكن ابن دريد فى الاشتقاق (ص . م7) ذكره فى أبيات أخر عند الكلام على «عمرو بن ماقط »>ونسها 
إليه يخاطب الك عمرو بن دند .وهو الصواب () كلام ألى عييدة اختصره اماف » وذكه ياقوت 
مطولا (1: 5لا - م0 م) ٠‏ (4) « إيلياء» بكسر اطهمزة فى أمله ثم ياءثم لام مكسوره ثم ياء 
وألف مدودة . قال فى القادوس : «ر يقر و شدد قهما » و إلياء بياء واحدة » و يقصر » . وهو اسم
```


## [2026-10-17T00:36:20.325Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'yavy|yauviy|yaona' POK_full.txt | head -5; grep -n -i -E 'yavy|yauviy' WLD_band3.txt incoming/WLD/WLD_Bd1_pages.txt | head -3; grep -n -i -E 'Jerusalem|jasper' AHD_watkins1985.txt | head -3",
 "description": "Grep Pokorny/WLD/AHD for yavyā and related"
}
```


### [2026-10-17T00:36:20.759Z] TOOL RESULT

```
41602:Avestan yav- "occupy oneself with sth. ' (present yavayeiti, Inf. yuto, yuta), yaona-n. 
41885:npers.yai/" barley' (= Lithuanian yai/a/); Old \n6\c yavya-m. " fruit supply ' (: Lithuanian ya^ya 
incoming/WLD/WLD_Bd1_pages.txt:18615: „Gerste“ (= lit. jaral)               ;   ai.       yavya- m. „Fruchtvorrat" (: lit jduja ,,Scheune“);
```


## [2026-10-17T00:36:24.325Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 41594,41606p POK_full.txt",
 "description": "Read Pokorny passage on Avestan yaona"
}
```


### [2026-10-17T00:36:24.762Z] TOOL RESULT

```
labialized laryngeal PIE h™- > 0u-, 0u-, 0y-, 0i- West Germanic = y-, j- Old Indie = j- East 
Germanic, Slavic, Old Latin, Old Albanian = w-, f- Old Celtic = v- Old Slavic = g'^- 
Armenian, Celtic, lllyrian = z- Greek, Baltic, Slavic = gj- Albanian Geg, gl- Albanian Tosc. 
Old \n6\c yaut/, yuvat/"ban6s, joins together, harnesses, places a harness on a draft 
animal ' (also " mixed '), participle yuta-, yutf-i. "connection' (and " mixture '), ni-yut-i. 
"row, yoke, pair of harnessed oxen ', yutha-m. " association, troop, multitude, crowd', 
yotra-u. "rope, band', yuna- n. 'band, strap, cord', avayava-m. "limb, member, part'; 
Avestan yav- "occupy oneself with sth. ' (present yavayeiti, Inf. yuto, yuta), yaona-n. 
"occupation ', yav- (yu-) Adj. " holding, standing by somebody ' = Old Indie yu- " 
journeyman, fellow ' (see Bartholomae Airan. Wb. 1264 f., where also about yav- 
"duration'); 
Note:
```


## [2026-10-17T00:36:33.350Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; P=tools/fetch_source.py; \npython3 $P 'https://en.wiktionary.org/wiki/ירושלים' --note 'page 562, root Yârâh: Hebrew etymology of Jerusalem (Shalem, yrw, folk \"city of peace\", Akkadian Urušalim, Syriac Ūrišlem)';\npython3 $P 'https://en.wiktionary.org/wiki/Jerusalem' --note 'page 562, root Yârâh: English Jerusalem chain via Greek/Latin';\npython3 $P 'https://en.wikipedia.org/wiki/Urmia' --note 'page 562, root Yârâh: origin of the name Urmia (Urartian, Indo-Iranian urmi-, Syriac ur+mia folk etymology)';\npython3 $P 'https://en.wiktionary.org/wiki/ἴασπις' --note 'page 562, root Yâšfa: Greek iaspis, Semitic cognates, Persian yašp';\npython3 $P 'https://en.wiktionary.org/wiki/jasper' --note 'page 562, root Yâšfa: English jasper chain';\npython3 $P 'https://en.wiktionary.org/wiki/يشب' --note 'page 562, root Yâšfa: Arabic yašb, probably from Persian yašp';\npython3 $P 'https://vajehyab.com/?q=یشم' --note 'page 562, root Yâšfa: Mo in entry یشم = یشپ';\npython3 $P 'https://en.wiktionary.org/wiki/جوی' --note 'page 562, root Yau: Persian jōy < MP jōy < OP yauviyā, cognate Skt yavyā' 2>&1 | tail -3",
 "description": "Archive the web sources used",
 "timeout": 300000
}
```


### [2026-10-17T00:36:36.630Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/62daaf0abc862004.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d0346ac75bbdfe90.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7f6974433c178f1e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/be4fa43f4b3acc1a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/86de770968091120.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e6d196a989dae5f7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f0c2b9d36af7bf22.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f9baf704f24aca88.txt
```


## [2026-10-17T00:36:40.742Z] TOOL CALL #61: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad",
 "description": "Ensure scratchpad exists"
}
```


### [2026-10-17T00:36:41.040Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:39:29.495Z] TOOL CALL #62: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-562.py",
 "content": "import json\n\nW = \"https://en.wiktionary.org/wiki/\"\nJER_HE = W + \"ירושלים\"\nJER_EN = W + \"Jerusalem\"\nURMIA = \"https://en.wikipedia.org/wiki/Urmia\"\nIASPIS = W + \"ἴασπις\"\nJASPER = W + \"jasper\"\nYASHB = W + \"يشب\"\nVJ_YASHM = \"https://vajehyab.com/?q=یشم\"\nJUY = W + \"جوی\"\n\nKLN828 = {\"ref\": \"KLN:828\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 20245 (grep '^Jerusalem'): 'Jerusalem, n. — Gk. Ierousalēm, fr. Heb. Yerūshālayim, lit. ‘foundation of peace’, fr. base of yārāh, ‘he threw, cast’, and shālōm, ‘peace’. Heb. yārāh in the above sense is rel. to Ethiop. warawa ‘he threw’ ... For sense development cp. ... L. fundamenta jacere, ‘to lay the foundations’. Cp. Shālēm, the ancient Heb. name of Jerusalem. Cp. also Aram. Yerushlem, Akkad. Ursalimmu (in the Tell El-Amarna Tablets: Urusalim), Arab. Ūrishalam'. Exactly Nourai's root and gloss.\"}\nKLN826 = {\"ref\": \"KLN:826\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 20185 (grep '^jasper', page marker 826 follows): 'jasper, n., an opaque variety of quartz. — ME. iaspre, fr. OF. jaspe, jaspre, fr. L. iaspis, fr. Gk. iaspis, ‘jasper’, which is of Sem. origin. Cp. Heb. yāshephēh, Akkad. yashupu, ashpu, ‘jasper’.' Nourai's chain and gloss are copied from this entry.\"}\nBQT2434 = {\"ref\": \"BQT:2434\", \"status\": \"supports\", \"note\": \"BQT vol 4 p.2434 (pdf 517; vision file ocr/BQT/2434.vision.txt), s.v. یشپ 'بمعنی یشم است'; footnote 1: 'در عربی یشب، یشف (ه.م.)، یشم (ه.م.)، یسب، یصف ویصیب آمده. مؤلف نفس گوید: از عبرانی «یشفه» ... است بمعنی مصقول ... این کلمه بیونانی منتقل گردید: iaspis، وازآن بدیگر زبانهای اروپا رفته (قس: انگلیسی jasper، فرانسوی jaspe)'. Mo'in gives the Hebrew > Arabic/Greek picture Nourai draws.\"}\n\ndef c(src, where, stance, note):\n    return {\"src\": src, \"where\": where, \"stance\": stance, \"note\": note}\n\nSKT_J = c(\"SKT\", \"SKT.txt line 9437 grep 'jasper'\", \"supports\", \"Skeat s.v. jasper: '... Gk. iaspis; Arab. yashb ... Cf. Heb. yāshpheh' (OCR noisy) — Semitic source, Greek > Latin > French > English.\")\nLKT_Y = c(\"LKT\", \"LKT.txt no. 941\", \"partial\", \"'Ar. jašm: Grüner Jaspis; hieraus über tk. ješem russ. serb. jašma' — Lokotsch treats yašm as Arabic (passed on to Turkish), not Persian.\")\n\nentries = []\n\n# ---------------- entry 0 ----------------\ne0_nodes = [\n {\"id\": 1, \"lang\": \"Hebrew\", \"words\": \"yârah, yerŭ; yerŭ-šâla'yim\", \"verdict\": \"plausible\",\n  \"derivation\": \"Biblical Hebrew Yərūšālayim (older spelling Yərūšālēm) is attested as Urusalim in the 14th-c. BCE Amarna letters (Akkadian Urušalim), so the name is pre-Israelite Canaanite. The usual scholarly analysis is West Semitic *yrw 'to found, lay (a cornerstone)' (the same verb as Heb. yārāh 'throw, cast; lay', cf. Job 38:6) + Šalem, the Canaanite god of dusk: 'foundation of Shalem'. Klein's reading 'foundation of peace' (šālōm) and the gloss 'city of peace' are later popular interpretations; Wiktionary calls the yir'eh + šālōm 'city of peace' etymology a folk etymology and says the whole etymology is disputed. yārāh is a real verb, but 'yerŭ' meaning 'city/base' is an inferred element, not an independent Hebrew noun.\",\n  \"derivation_fa\": \"نام عبری «یروشالیم» (Yərūšālayim) در نامه‌های تل‌العمارنه (سدهٔ چهاردهم پیش از میلاد) به صورت Urusalim آمده و پیش از بنی‌اسرائیل کنعانی است. پژوهشگران آن را معمولاً از ریشهٔ سامی غربی yrw «بنیاد نهادن، افکندن (سنگ بنا)» (همان yārāh عبری «افکندن») و نام خدای کنعانی «شالِم» می‌دانند: «بنیادِ شالِم». معنای «شهر صلح» ریشه‌شناسی عامیانه است و ویکی‌واژه اصل نام را مورد اختلاف می‌داند. پیوند با yārāh پذیرفتنی است، ولی تفسیر «شهر صلح» را باید با احتیاط پذیرفت.\",\n  \"sources\": [JER_HE],\n  \"ref_check\": [KLN828],\n  \"consulted\": [\n    c(\"KLN\", \"KLN_1966.txt l.20245-20246\", \"supports\", \"'fr. base of yārāh, he threw, cast, and shālōm, peace ... Akkad. Ursalimmu (Tell El-Amarna: Urusalim)'.\"),\n    c(\"AFA\", \"AFA.txt grep 'شلم|Jerusalem'\", \"silent\", \"Fraenkel does not treat the name.\"),\n    c(\"ARB\", \"ARB_mo3rb.txt l.4199-4243\", \"partial\", \"al-Jawaliqi s.v. أورى شلم: 'لبيت المقدس ... قال أبو عبيدة: أوري شلم بكسر اللام، وقال: هو عبراني معرب' — Hebrew origin of the Arabic name, no analysis of the elements.\")]},\n {\"id\": 2, \"lang\": \"Persian\", \"words\": \"Ûršalîm; Ûrmîyeh\", \"verdict\": \"disputed\",\n  \"derivation\": \"Ûršalîm (اورشلیم): Persian took the biblical name through the Aramaic/Syriac and Arabic form (Syriac ʾŪrišlem, Arabic Ūrīšalam/Ūrišalam, which al-Jawaliqi calls 'Hebrew, Arabicised'); the initial Ūr- reflects the Aramaic/Akkadian Ur(u)- spelling, not Hebrew Yərū-. The descent from the Hebrew name is correct, but the gloss 'city of peace' is the popular interpretation (see #1). Ûrmîyeh (اورمیه, Urmia): the analysis Syriac ūr 'city' + mayyā 'water' = 'city of water' is a popular etymology; Wikipedia records rival views (R. N. Frye: Urartian; T. Burrow: Indo-Iranian ūrmi- 'wave'), and Farahvashi (Iranvij p.38) gives 'اورمیه-شهرآب'. In either case Urmia has nothing to do with Heb. yārāh; Nourai seems to link the two only through the shared 'ur(u)-' element, and that 'uru' 'city' (if real) is not the Hebrew verb. Ûršalîm: plausible; Ûrmîyeh: disputed.\",\n  \"derivation_fa\": \"«اورشلیم» از راه آرامی/سریانی (ʾŪrišlem) و عربی «أوری شَلَم» به فارسی رسیده است و آغاز -Ūr آن صورت آرامی و اکدی است، نه yərū- عبری. پس پیوندش با نام عبری درست است، اما معنای «شهر صلح» ریشه‌شناسی عامیانه است. «اورمیه» را به سریانی ūr «شهر» + mayyā «آب» یعنی «شهر آب» معنی کرده‌اند (فره‌وشی در ایرانویج: «اورمیه-شهرآب»)، ولی این نیز ریشه‌شناسی عامیانه است. فرای آن را اورارتویی و بارو آن را از هندوایرانی ūrmi- «موج» دانسته‌اند. در هر حال «اورمیه» هیچ پیوندی با فعل عبری yārāh ندارد و این بخش از نمودار نورایی پذیرفتنی نیست.\",\n  \"sources\": [JER_HE, URMIA],\n  \"ref_check\": [\n    {\"ref\": \"MON5:195\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 5 (a'lam) not on disk or online; vajehyab gives only Dehkhoda 'اورشلیم ... رجوع به قدس شود'.\"},\n    {\"ref\": \"IRN:28\", \"status\": \"partial\", \"note\": \"Iranvij (ref_page.py IRN:28 -> pdf 39, printed p.38; IRN_pages.txt l.875): 'پیرامون دریاچهٔ رضائیه (اورمیه-شهرآب) فرودآمدند' — gives the 'city of water' gloss for Urmia, without etymology and without any link to Jerusalem. Printed page is 38, not 28.\"}],\n  \"consulted\": [\n    c(\"ARB\", \"ARB_mo3rb.txt l.4199, 4243\", \"supports\", \"'أورى شلم ... بيت المقدس ... هو عبراني معرب' — the Arabic form behind Persian Ūršalīm.\"),\n    c(\"IRN\", \"IRN_pages.txt l.767, 875\", \"partial\", \"'(اورمیه) ... ' and '(اورمیه-شهرآب)' — gloss only.\"),\n    c(\"HRN\", \"HRN.txt grep 'Urmi|Jerusalem'\", \"silent\", \"Horn has neither name.\"),\n    c(\"BQT\", \"BQT_v1_pages.txt grep 'اورشلیم|اورمیه'\", \"silent\", \"no headword found in the OCR of vol. 1.\")]},\n {\"id\": 3, \"lang\": \"Arabic\", \"words\": \"al-avâra\", \"verdict\": \"disputed\",\n  \"derivation\": \"No Arabic word al-awāra 'place, location' derived from Heb. yārāh exists. Nourai's source, al-Jawaliqi's al-Muʿarrab, right after Ūrī-šalam (Jerusalem) says 'وقالوا في اسم الموضع «أُوارة»' ('and they said, as the name of the place, Uwāra'), quoting a verse by ʿAmr b. Milqaṭ al-Ṭāʾī ('... بالسفح أسفل من أُوارة'). Uwāra is a place name (a site in Arabia, known from the pre-Islamic 'Day of Uwāra'), so Nourai seems to have read 'اسم الموضع' (name of a place) as the meaning of the word. The Arabic root ʾ-w-r / w-r-y is not Hebrew y-r-h, so the arrow from the root is not supported.\",\n  \"derivation_fa\": \"واژه‌ای عربی به صورت «الأوارة» به معنای «جای، مکان» که از yārāh عبری آمده باشد شناخته نیست. جوالیقی در «المعرّب» پس از «أوری شَلَم» (اورشلیم) می‌نویسد «وقالوا في اسم الموضع أُوارة» و بیتی از عمرو بن ملقط طائی می‌آورد. «أُوارة» نام جایی در عربستان است (یوم أوارة). پیداست نورایی عبارت «اسم الموضع» را معنای واژه پنداشته است. این پیوند پذیرفتنی نیست.\",\n  \"sources\": [],\n  \"ref_check\": [{\"ref\": \"ARB:32\", \"status\": \"partial\", \"note\": \"ARB_mo3rb.txt l.4256-4258 (Shakir ed., same article as أورى شلم; page number not legible in the OCR): 'وقالوا في اسم الموضع «أوارة». قال عمرو بن ملقط الطائي: ... بالسفح أسفل من أواره'. The word is there, but as a place name (Uwāra), not a common noun 'place', and with no derivation from Hebrew.\"}],\n  \"consulted\": [\n    c(\"KLN\", \"KLN_1966.txt l.20246\", \"silent\", \"Klein lists only Arab. Ūrishalam, nothing like awāra.\"),\n    c(\"AFA\", \"AFA.txt grep 'أوار'\", \"silent\", \"no hit.\"),\n    c(\"AFM\", \"AFM.txt grep 'أوار'\", \"silent\", \"no hit.\")]},\n {\"id\": 4, \"lang\": \"English\", \"words\": \"Jerusalem\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English Jerusalem goes back through Old English Hierusalem / Old French Jherusalem and Late Latin Ierusalem/Hierusalem to Greek Ierousalēm (Septuagint), a transcription of Biblical Hebrew Yərūšālēm/Yərūšālayim. The chart's direct arrow from Hebrew to English leaves out the Greek and Latin links, but the descent is correct.\",\n  \"derivation_fa\": \"واژهٔ انگلیسی Jerusalem از انگلیسی باستان Hierusalem و فرانسوی کهن Jherusalem، از لاتین متأخر Ierusalem/Hierusalem و یونانی Ierousalēm (ترجمهٔ هفتادی) آمده است. این صورت یونانی برگردان عبری Yərūšālayim است. نمودار پیوندهای یونانی و لاتین را نیاورده، ولی ادعای نورایی در اصل درست است.\",\n  \"sources\": [JER_EN],\n  \"ref_check\": [KLN828],\n  \"consulted\": [\n    c(\"KLN\", \"l.20245\", \"supports\", \"'Jerusalem, n. — Gk. Ierousalēm, fr. Heb. Yerūshālayim'.\"),\n    c(\"SKT\", \"SKT.txt grep 'jerusalem'\", \"silent\", \"no entry.\"),\n    c(\"FSD\", \"FSD_vol1-4 grep '^Jerusalem'\", \"silent\", \"no etymological entry found.\")]},\n]\nentries.append({\n \"entry\": 0, \"root\": \"Yârâh\", \"verdict\": \"plausible\",\n \"modern_form\": \"Biblical Hebrew yārāh 'to throw, cast; lay (a foundation)'; Yərūšālayim < Canaanite *Yrw-Šalem 'foundation of (the god) Shalem', Amarna Urusalim\",\n \"note\": \"The root, its Semitic/Hebrew label and the gloss 'he threw, cast' are taken from Klein s.v. Jerusalem, and Heb. yārāh is a real verb. That it underlies the first element of Jerusalem is the common view ('foundation of Shalem'). Klein's 'foundation of peace' and the chart's 'city of peace' are popular interpretations. Two nodes go wrong: Urmia ('city of water') is unrelated to yārāh and its Syriac etymology is itself popular, and the Arabic 'al-avâra' is the place name Uwāra in al-Jawaliqi, misread as a noun meaning 'place'. The extraction matches the printed page, including the arrow from #1 (not #3) to English.\",\n \"note_fa\": \"ریشهٔ عبری yārāh «افکندن، انداختن» و برچسب سامی/عبری آن از فرهنگ کلاین (ذیل Jerusalem) گرفته شده و درست است. جزء نخست نام «یروشالیم» را بیشتر پژوهشگران از همین فعل به معنای «بنیاد نهادن» می‌دانند («بنیاد شالِم»)، ولی «شهر صلح» تفسیری عامیانه است. «اورمیه» با این ریشه پیوندی ندارد. «الأوارة» عربی هم نام جایی است به نام «أُوارة» که نورایی آن را واژه‌ای به معنای «مکان» گرفته است. پس ریشه پذیرفتنی است، اما دو شاخهٔ نمودار نادرست است.\",\n \"sources\": [JER_HE],\n \"ref_check\": [KLN828],\n \"consulted\": [\n   c(\"AFA\", \"AFA.txt grep 'يرى|أورى'\", \"silent\", \"no treatment of yrh/Jerusalem.\"),\n   c(\"ARB\", \"ARB_mo3rb.txt l.4199-4243\", \"partial\", \"Ūrī-šalam = Bayt al-Maqdis, 'Hebrew, Arabicised' (Abu ʿUbayda); no root analysis.\"),\n   c(\"FVQ\", \"FVQ.txt grep 'Jerusalem'\", \"silent\", \"Jeffery has no entry for the name (it is not Qur'anic).\")],\n \"nodes\": e0_nodes})\n\n# ---------------- entry 1 ----------------\ngk_chain = [\n (3, \"Greek\", \"iaspis\", \"Greek íaspis (fem., from Plato and the Septuagint on) 'jasper'. Klein calls it 'of Sem. origin' (cf. Heb. yāšəfēh, Akkad. yašpû). Wiktionary says it is a loanword of unclear source, possibly Egyptian, with Hebrew yāšəfēh, Akkadian yašpû, Syriac yašpā and Persian yašp all 'from the same source'. That Greek borrowed it from the Semitic Levant is the traditional view; that Hebrew is the direct source is less certain.\", \"یونانی íaspis «یشم، جاسپر» به گفتهٔ کلاین از زبانی سامی گرفته شده است (عبری yāšəfēh، اکدی yašpû). ویکی‌واژه آن را وام‌واژه‌ای با خاستگاه نامعلوم (شاید مصری) می‌داند که با عبری و اکدی و سریانی yašpā و فارسی «یشپ» از یک سرچشمه است. پس وام‌گیری از جهان سامی پذیرفتنی است، ولی منبعِ مستقیم بودن عبری قطعی نیست.\", \"plausible\", [IASPIS]),\n (4, \"Latin\", \"iaspis\", \"Latin iaspis, -idis (Pliny, Vulgate) is a direct borrowing of Greek íaspis, keeping the Greek form and gender.\", \"لاتین iaspis مستقیماً از یونانی íaspis گرفته شده و همان ساخت و جنس دستوری را نگه داشته است. ادعای نورایی درست است.\", \"confirmed\", [JASPER]),\n (5, \"Old French\", \"jaspe, jaspre\", \"Old French jaspe continues Latin iaspis (Vulgar Latin *iaspidem, with Latin initial i- > j- [dʒ]). The variant jaspre has an intrusive -r-. Both are 12th-13th c.\", \"فرانسوی کهن jaspe از لاتین iaspis آمده است (i- آغازی لاتین در فرانسوی به j- بدل شده). صورت jaspre یک r افزوده دارد. ادعای نورایی درست است.\", \"confirmed\", [JASPER]),\n (6, \"Middle English\", \"iaspre, jaspre\", \"Middle English jaspre/iaspre (14th c., Chaucer) was borrowed from Old French jaspre. i and j were one letter in ME script, so iaspre and jaspre are the same word.\", \"انگلیسی میانه jaspre/iaspre (سدهٔ چهاردهم، چاسر) از فرانسوی کهن jaspre گرفته شده است. i و j در خط انگلیسی میانه یک حرف بودند. ادعای نورایی درست است.\", \"confirmed\", [JASPER]),\n (7, \"English\", \"jasper 2\", \"Modern English jasper 'opaque (red, yellow, brown or green) variety of quartz/chalcedony' continues ME jaspre with the final -re > -er spelling. The '2' only separates it from the personal name Jasper, which Klein treats separately.\", \"انگلیسی امروزی jasper «گونه‌ای کوارتز کدر» دنبالهٔ jaspre انگلیسی میانه است (‎-re به ‎-er بدل شده). شمارهٔ ۲ برای جدا کردن آن از نام کسانِ Jasper است. ادعای نورایی درست است.\", \"confirmed\", [JASPER]),\n]\ne1_nodes = [\n {\"id\": 1, \"lang\": \"Arabic\", \"words\": \"yašb\", \"verdict\": \"plausible\",\n  \"derivation\": \"Arabic yašb (also yašf, yašm, yasb, according to Mo'in's footnote) 'jasper; jade' is a real word. Mo'in, after the author of 'Nafs', derives it from Hebrew yāšəfēh. Wiktionary instead calls it 'cognate to Hebrew ישפה; probably ultimately from Persian یشپ (yašp)'. The Semitic-Iranian word moved in more than one direction, and Arabic may have it from Persian rather than from Hebrew, so the arrow root > Arabic is possible but not certain.\",\n  \"derivation_fa\": \"عربی «یَشْب» (و به گفتهٔ معین یشف، یشم، یسب) به معنای «یشم، جاسپر» واژه‌ای واقعی است. معین در حاشیهٔ برهان، به نقل از مؤلف «نفس»، آن را از عبری «یشفه» می‌داند، ولی ویکی‌واژه آن را هم‌ریشه با عبری و «احتمالاً در اصل از فارسی یشپ» می‌شمارد. پس اشتقاق از عبری ممکن است، ولی قطعی نیست و باید با احتیاط پذیرفت.\",\n  \"sources\": [YASHB],\n  \"ref_check\": [BQT2434],\n  \"consulted\": [\n    c(\"BQT\", \"p.2434 fn.1\", \"supports\", \"'در عربی یشب، یشف، یشم ... از عبرانی «یشفه» ... بمعنی مصقول'.\"),\n    c(\"KLN\", \"l.20185\", \"partial\", \"Klein cites Heb. and Akkad. cognates of iaspis but not Arabic yašb.\"),\n    c(\"AFM\", \"AFM.txt grep 'يشب|يشم'\", \"silent\", \"Addi Shir has no entry (hits are only يشبه).\"),\n    c(\"LKT\", \"no. 941\", \"partial\", \"lists Ar. jašm 'grüner Jaspis', the m-variant, as Arabic.\")]},\n {\"id\": 2, \"lang\": \"Persian\", \"words\": \"yašm\", \"verdict\": \"plausible\",\n  \"derivation\": \"NP yašm (یشم) 'jade, jasper', with variants yašp (یشپ) and the adjective yašmī 'jade-green', is well attested. Borhan glosses یشپ 'بمعنی یشم است'. Mo'in's dictionary has 'یشم ... یشپ', and Wiktionary lists Persian yašp as 'from the same source' as Greek iaspis. The -p/-b/-m alternation (yašp ~ yašb ~ yašm) is common in such Wanderwörter, and Turkish yeşim comes from the Persian/Arabic form. Whether Persian took the word from Arabic yašb, as drawn, or Arabic took it from Persian yašp (Wiktionary's view) is undecided, so the arrow direction is uncertain.\",\n  \"derivation_fa\": \"«یشم» فارسی (با گونهٔ «یشپ» و صفت «یشمی») به معنای سنگ سبز یشم است. برهان قاطع «یشپ» را «بمعنی یشم» آورده و معین نیز «یشم» را برابر «یشپ» می‌نهد. ویکی‌واژه «یشپ» فارسی را با یونانی iaspis از یک سرچشمه می‌داند. ابدال پ/ب/م در این واژهٔ کوچنده (یشپ، یشب، یشم) رایج است. اینکه فارسی آن را از عربی «یشب» گرفته (چنانکه نورایی کشیده) یا عربی از فارسی، روشن نیست. پس پیوند پذیرفتنی است، ولی جهت وام‌گیری قطعی نیست.\",\n  \"sources\": [VJ_YASHM, IASPIS],\n  \"ref_check\": [dict(BQT2434, note=\"BQT vol 4 p.2434 (pdf 517; ocr/BQT/2434.vision.txt): 'یشپ - بفتح اول وسکون ثانی و بای فارسی، بمعنی یشم است وآن سنگی باشد معروف و خاصیت‌مند'; fn.1 lists Arabic یشب/یشم and Hebrew یشفه. Confirms yašm = yašp and the Hebrew/Arabic background, without saying Persian took it from Arabic.\")],\n  \"consulted\": [\n    c(\"BQT\", \"p.2434\", \"supports\", \"'یشپ ... بمعنی یشم است'.\"),\n    c(\"MON\", \"vajehyab.com s.v. یشم\", \"supports\", \"Mo'in: 'یشم (یَ) (اِ.) یشپ؛ سنگی معدنی ... به رنگهای سبز تیره و آبی'.\"),\n    c(\"HRN\", \"HRN.txt grep 'yašm|yašp|jašm'\", \"silent\", \"not in Horn.\"),\n    c(\"ARY\", \"ARY_pages.txt grep 'یشم'\", \"silent\", \"not an Indo-European word; no hit.\"),\n    LKT_Y]},\n] + [\n {\"id\": i, \"lang\": lg, \"words\": w, \"verdict\": v, \"derivation\": d, \"derivation_fa\": dfa, \"sources\": s,\n  \"ref_check\": [KLN826],\n  \"consulted\": [c(\"KLN\", \"l.20185\", \"supports\", \"'ME. iaspre, fr. OF. jaspe, jaspre, fr. L. iaspis, fr. Gk. iaspis ... of Sem. origin'.\"), SKT_J,\n                c(\"FSD\", \"FSD_vol1.txt l.42750\", \"silent\", \"the hit is only a birthstone table ('Jasper ... March'), no etymology.\")]}\n for (i, lg, w, d, dfa, v, s) in gk_chain]\nentries.append({\n \"entry\": 1, \"root\": \"Yâšfa, Yâšfeh\", \"verdict\": \"plausible\",\n \"modern_form\": \"Biblical Hebrew yāšəfēh 'jasper' (Ex. 28:20); a Wanderwort of unclear (possibly Egyptian) origin shared with Akkadian yašpû, Syriac yašpā, Greek íaspis, Persian yašp/yašm, Arabic yašb\",\n \"note\": \"Hebrew yāšəfēh 'jasper' is real (one of the stones of the high priest's breastplate), and the gloss 'an opaque variety of quartz' is Klein's definition of jasper. The Greek-Latin-French-English chain is standard. Modern sources do not treat Hebrew as the ultimate source: Wiktionary calls Greek íaspis a loanword of unclear, possibly Egyptian, origin and groups Hebrew, Akkadian, Syriac and Persian yašp as cognate borrowings 'from the same source'. It also derives Arabic yašb probably from Persian yašp, the reverse of the chart's Arabic > Persian arrow. Hence plausible rather than confirmed. Entry 2 (Yâšfeh) is a redirect and is skipped. The extraction matches the printed page.\",\n \"note_fa\": \"عبری yāšəfēh «یشم، جاسپر» واژه‌ای واقعی است (یکی از سنگهای سینه‌بند کاهن بزرگ)، و تعریف «گونه‌ای کوارتز کدر» تعریف کلاین از jasper است. زنجیرهٔ یونانی، لاتین، فرانسوی و انگلیسی درست است. ولی پژوهش امروزی عبری را سرچشمهٔ نهایی نمی‌داند و واژه را وام‌واژه‌ای کوچنده با خاستگاه نامعلوم (شاید مصری) می‌شمارد که در اکدی، سریانی، یونانی و فارسی (یشپ) هم آمده است. ویکی‌واژه حتی عربی «یشب» را از فارسی «یشپ» می‌داند، یعنی وارونهٔ جهت نمودار. پس ادعای نورایی را باید با احتیاط پذیرفت.\",\n \"sources\": [IASPIS, YASHB],\n \"ref_check\": [BQT2434, KLN826],\n \"consulted\": [\n   c(\"AKD\", \"AKD.txt grep 'jašp|ašpû|jaspis'\", \"silent\", \"Zimmern does not list it among Akkadian loanwords in this OCR.\"),\n   SKT_J, LKT_Y],\n \"nodes\": e1_nodes})\n\n# ---------------- entry 3 ----------------\nDKS_G = c(\"ISS_alt_DKS\", \"DKS s.v. gyūna-, jūna- (ISS_alt_DKS.txt l.2309-2312)\", \"supports\", \"'gyūna-, jūna- ‘movement, gait’ ... Z 24.221 sarvai māñaṃte gyūnu ‘resembles the gait of a lion’ ... From *yauna- ‘movement; place, time of movement’, Av. yaona-, O.Pers. yauviyā- ‘channel’, Zor.P. yōy, Pahlavi Psalter yōd, N.Pers. jōy ‘stream’. To O.Ind. yoni-. Possibly i-eu- from ei-:i- ‘to move’ ...; not to IE Pok. 507, 508, 511.' This is Nourai's whole chart.\")\ne3_nodes = [\n {\"id\": 1, \"lang\": \"Old Persian\", \"words\": \"yauviya\", \"verdict\": \"confirmed\",\n  \"derivation\": \"OP yauviyā- f. 'canal' occurs in Darius's Suez inscription (DZc 8-12: 'this canal (yauviyā) was dug ... from the river Nile to the sea that goes from Persia'). Kent glosses it 'canal', compares Vedic yavyā 'stream, river' and calls it 'perhaps deriv. of root ay-/i-/yā- ‘go’'. Bailey derives it from *yau- 'move'. The word and meaning are secure, and the gloss 'channel (to move water)' is Bailey's interpretation of it.\",\n  \"derivation_fa\": \"پارسی باستان yauviyā- «آبراهه، کانال» در کتیبهٔ داریوش در سوئز آمده است: «این آبراهه کنده شد از رود نیل تا دریایی که از پارس می‌آید». کنت آن را «کانال» معنی می‌کند و با ودایی yavyā «رود» می‌سنجد. او آن را شاید از ریشهٔ ay-/i- «رفتن» می‌داند، ولی بیلی آن را از *yau- «جنبیدن» می‌گیرد. خود واژه و معنایش استوار است و ادعای نورایی درست است.\",\n  \"sources\": [JUY],\n  \"ref_check\": [\n    {\"ref\": \"KNT:204\", \"status\": \"supports\", \"note\": \"KNT_full.txt l.28428-28432 (lexicon s.v.): 'yauviyā- sb. ‘canal’ (§48): NPers. jōi ‘water-course, canal’, cf. perhaps Skt. (Vedic) yavyā ‘stream, river’; perhaps deriv. of root ay-/i-/yā- ‘go’. yauviyā nsf. DZc 10; yauviyām asf. DZc 8f, 12.'\"},\n    {\"ref\": \"ISS:91\", \"status\": \"not_checked\", \"note\": \"Khotanese Texts VI not online; substance checked in Bailey's Dictionary of Khotan Saka s.v. gyūna- (see consulted).\"}],\n  \"consulted\": [\n    c(\"KNT\", \"KNT_full.txt l.3534\", \"supports\", \"'yauviyā DZc 8f, 10; cf. Skt. yavyā'.\"),\n    c(\"BRT\", \"BRT.txt grep 'yauviy'\", \"silent\", \"Bartholomae has no separate entry in this OCR.\"),\n    DKS_G,\n    c(\"HRN\", \"HRN no. 431 (leaf 110)\", \"supports\", \"'jōī, jō ‘Kanal’. ap. yauviyā; phlv. jōi bezw. yōī; ai. yavyā'.\")]},\n {\"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"yôî, jôî\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Middle Persian jōy 'stream, channel' (MacKenzie: jō(y) [ywd, ywb]) continues OP yauviyā- regularly: *yauvyā > *yōy (OIr. au > MP ō, loss of the final syllable). Initial y- became j- in Middle Persian (cf. yava- > jaw 'barley', yuvan- > jawān). The older y- spelling survives in the Pahlavi Psalter yōd/yōy (Bailey), Horn's 'phlv. jōi bezw. yōī'.\",\n  \"derivation_fa\": \"فارسی میانهٔ jōy «جوی، آبراهه» (مکنزی: jō(y)) دنبالهٔ منظم پارسی باستان yauviyā- است: au ایرانی باستان در فارسی میانه به ō بدل شده و هجای پایانی افتاده است. y- آغازی نیز در فارسی میانه به j- (ج) بدل شده، چنانکه yava- به «جو» و yuvan- به «جوان» رسیده است. صورت کهن‌تر yōy در زبور پهلوی بازمانده است. ادعای نورایی درست است.\",\n  \"sources\": [JUY],\n  \"ref_check\": [{\"ref\": \"BQT:602\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 60 (= printed p.602 by the leaf+543 rule; OCR reversed/noisy), footnote to جوی: 'جوی - پارسی باستان yauviyā، پهلوی ... هندی باستان yavyā ... کردی ... بلوچی (آبراهه) «اسشق ۴۳۱» ورک هوبشمان ...' — the Latin forms are garbled in the OCR, but the OP > Pahlavi > NP chain and the Rudaki verse 'بوی جوی مولیان آید همی' are legible.\"}],\n  \"consulted\": [\n    c(\"PHD\", \"PHD_mackenzie.txt l.3080\", \"supports\", \"'jō(y) [ywd, ywb | N ~] stream, channel'.\"),\n    c(\"NYB\", \"NYB_vol2_glossary.txt grep 'jōy|yōy|stream'\", \"silent\", \"no glossary entry for jōy found.\"),\n    c(\"HRN\", \"no. 431\", \"supports\", \"'phlv. jōi bezw. yōī'.\"),\n    DKS_G]},\n {\"id\": 3, \"lang\": \"Persian\", \"words\": \"jŭ; jŭy-bâr\", \"verdict\": \"confirmed\",\n  \"derivation\": \"NP jōy/jūy (جوی), jū (جو), also jōb (جوب) 'stream, brook' < MP jōy < OP yauviyā- (Horn 431, Hübschmann: 'Joi, Jo ‘Kanal’ = ap. yauviyā-'). The final -y drops in jū, and -b in jōb is a dialect variant. jūybār (جویبار) = jūy + the place suffix -bār (as in rūdbār, daryābār), 'streamside; place with many streams'. Borhan: 'کنار جوی آب راگویند و جایی که در آن جوی آب بسیار باشد'. The Rudaki line 'بوی جوی مولیان آید همی' is quoted by Mo'in under جوی.\",\n  \"derivation_fa\": \"«جوی، جو» (و گونهٔ «جوب») در فارسی نو از فارسی میانهٔ jōy و پارسی باستان yauviyā- آمده است (هرن ش ۴۳۱، هوبشمان). «جویبار» از «جوی» و پسوند مکان «-بار» (چون رودبار) ساخته شده و برهان آن را «کنار جوی آب و جایی که در آن جوی آب بسیار باشد» معنی کرده است. بیت رودکی «بوی جوی مولیان آید همی» را معین نیز در حاشیهٔ برهان آورده است. ادعای نورایی درست است.\",\n  \"sources\": [JUY],\n  \"ref_check\": [\n    {\"ref\": \"BQT:602\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 60: 'جویبار - ... بر وزن کوهسار، کنار جوی آب را گویند و جایی که دران جوی آب بسیار باشد و جوی بزرگی را نیز گویند که از جویهای کوچک بهم رسد'; footnote 'از: جوی + بار (پسوند مکان)'; footnote to جوی with OP yauviyā and Rudaki's verse.\"},\n    {\"ref\": \"ISS:91\", \"status\": \"not_checked\", \"note\": \"Khotanese Texts VI not online; DKS s.v. gyūna- gives 'N.Pers. jōy ‘stream’' from *yauna-/yauviyā-.\"}],\n  \"consulted\": [\n    c(\"HRN\", \"HRN.txt l.3993-3996 (no. 431, leaf 110 = p.89)\", \"supports\", \"'431. jōī, jō ‘Kanal’. ap. yauviyā; phlv. jōi bezw. yōī; ai. yavyā. LW. kurd. jō ...; bel. jō ‘Wasserlauf, Kanal’'.\"),\n    c(\"HUB\", \"HUB.txt l.5294\", \"supports\", \"'Joi, Jo ‘Kanal’ = ap. yauviyā-'.\"),\n    c(\"BQT\", \"vol 2 leaf 60\", \"supports\", \"جوی / جویبار entries as above.\"),\n    c(\"CHEUNG\", \"CHEUNG.txt\", \"silent\", \"Cheung treats verbs only; no noun jōy.\"),\n    c(\"ARY\", \"ARY_pages.txt grep 'جوی'\", \"silent\", \"no clear entry in the OCR.\")]},\n {\"id\": 4, \"lang\": \"Avestan\", \"words\": \"yaona\", \"verdict\": \"plausible\",\n  \"derivation\": \"Avestan yaona- exists, but Bartholomae (col. 1231) glosses it 'm. ‘(bestimmte, fest zugewiesene) Statt, Stätte’; insbes. ‘Heimstätte, Heimat’' (assigned place, home), as in aša-yaona- 'whose home is Aša'. Pokorny (under *i̯eu- 'bind', p.508) gives 'yaona- n. ‘occupation’'. Only Bailey interprets it as 'place of movement', from *yau- 'move', which yields Nourai's 'movement'. The word is real and its link to Khotanese gyūna- and Sogdian ywn is accepted, but the gloss 'movement' is Bailey's etymological reading, not the attested sense ('place').\",\n  \"derivation_fa\": \"اوستایی yaona- واژه‌ای واقعی است، ولی بارتولومه آن را «جای معین، جایگاه، میهن» معنی می‌کند (مانند aša-yaona- «که میهنش اشه است») و پوکورنی «اشتغال». تنها بیلی آن را «جای جنبش» و از *yau- «جنبیدن» می‌داند و معنای «جنبش» در نمودار نورایی از اوست. پیوند واژه با سغدی و ختنی پذیرفتنی است، اما معنای «حرکت» درست نیست و معنای گواهی‌شده «جای» است.\",\n  \"sources\": [],\n  \"ref_check\": [{\"ref\": \"ISS:91\", \"status\": \"not_checked\", \"note\": \"Khotanese Texts VI not online; DKS s.v. jum-/pīm-: 'Av. yaona- ‘place of movement’ is from yau-na-'; s.v. hayūna-: 'AV. yaona- ‘place’' — Bailey himself glosses it 'place'.\"}],\n  \"consulted\": [\n    c(\"BRT\", \"BRT.txt l.20980 (col. 1231)\", \"contradicts\", \"'yaona- m. ‘(bestimmte, fest zugewiesene) Statt, Stätte’ ... a) insbes. ‘Heimstätte, Heimat’' — place, not movement.\"),\n    c(\"POK\", \"POK_full.txt l.41602 (i̯eu- 'bind')\", \"contradicts\", \"'Avestan yav- ‘occupy oneself with sth.’ ..., yaona- n. ‘occupation’'.\"),\n    c(\"WLD\", \"WLD Bd1 grep 'yaona'\", \"silent\", \"no hit.\"),\n    DKS_G]},\n {\"id\": 5, \"lang\": \"Sogdian\", \"words\": \"ywn\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Sogdian ywn /yōn/ 'place; on the spot' (Gharib no. 11056: 'yon < Av. yaona, place, on the spot', with the derived adverb ywnyδ 'immediately, at once') is the regular continuation of OIr. *yauna- = Av. yaona- (au > ō). The meaning 'place' agrees with Bartholomae's gloss of the Avestan word, not with 'movement'.\",\n  \"derivation_fa\": \"سغدی ywn (yōn) «جای؛ در جا» (قریب ش ۱۱۰۵۶: «yon از اوستایی yaona، جای») دنبالهٔ منظم ایرانی باستان *yauna- (اوستایی yaona-) است و au به ō بدل شده است. معنای «جای» با معنایی که بارتولومه برای واژهٔ اوستایی آورده می‌خواند. ادعای نورایی درست است.\",\n  \"sources\": [],\n  \"ref_check\": [{\"ref\": \"SOD:450\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf 517 (≈ printed p.451; Nourai's 450 is close): '11056 ywn M, C, S — yon ©<Av. yaona =»ywnyδ — place, on the spot — GMS 1109A 1420; MDii ...'.\"}],\n  \"consulted\": [\n    c(\"SOD\", \"entry 11056\", \"supports\", \"'yon < Av. yaona ... place, on the spot'.\"),\n    c(\"ISS_alt_DKS\", \"s.v. hayūna-\", \"supports\", \"'From *ha-yauna- ‘of the same place’ to Av. yaona- ‘place’'.\"),\n    c(\"BRT\", \"col. 1231\", \"supports\", \"Av. yaona- 'Stätte, Heimat' — same sense as the Sogdian.\")]},\n]\nentries.append({\n \"entry\": 3, \"root\": \"Yau, Gyŭna\", \"verdict\": \"plausible\",\n \"modern_form\": \"Khotanese gyūna-/jūna- 'movement, gait; time(s)' < *yauna-; Bailey's Iranian base *yau-/yu- 'to move' (not in Pokorny)\",\n \"note\": \"'Indo-Scythian' is Bailey's term for Khotanese Saka. Gyūna is a real Khotanese word ('gait of a lion', Book of Zambasta 24.221), and Nourai copies Bailey's whole etymological complex from Khotanese Texts VI p.91: *yauna- 'movement; place of movement' > Av. yaona-, Sogd. ywn, OP yauviyā- 'channel', NP jōy. The base 'yau- move' is Bailey's own. Kent instead suggests root ay-/i- 'go' for yauviyā-, Bartholomae glosses Av. yaona- 'place, home', and Pokorny puts yaona- under *i̯eu- 'bind' ('occupation'). The OP > MP > NP jōy chain is secure. Grouping it with yaona-/gyūna- under 'move' rests on one scholar. The extraction matches the printed page.\",\n \"note_fa\": \"«هندوسکایی» اصطلاح بیلی برای زبان سکایی ختنی است. gyūna- «رفتار، گام (شیر یا اسب)» واژهٔ ختنی واقعی است. نورایی همهٔ این نمودار را از بیلی گرفته است: *yauna- «جنبش، جای جنبش» که به اوستایی yaona-، سغدی ywn، پارسی باستان yauviyā- «آبراهه» و فارسی «جوی» رسیده است. ریشهٔ yau- «جنبیدن» پیشنهاد خود بیلی است. کنت yauviyā- را از ریشهٔ «رفتن» می‌داند، بارتولومه yaona- را «جایگاه، میهن» معنی می‌کند و پوکورنی آن را زیر ریشهٔ «بستن» می‌آورد. زنجیرهٔ پارسی باستان، پهلوی و فارسی «جوی» استوار است، ولی گردآوردن همهٔ اینها زیر یک ریشهٔ «جنبیدن» تنها نظر بیلی است و باید با احتیاط پذیرفت.\",\n \"sources\": [JUY],\n \"ref_check\": [{\"ref\": \"ISS:91\", \"status\": \"not_checked\", \"note\": \"Khotanese Texts VI not online. Bailey's Dictionary of Khotan Saka s.v. gyūna- (ISS_alt_DKS.txt l.2309-2312) gives the same material: 'gyūna-, jūna- ‘movement, gait’ ... From *yauna- ‘movement; place, time of movement’, Av. yaona-, O.Pers. yauviyā- ‘channel’ ... N.Pers. jōy ‘stream’ ... Possibly ... from ei-:i- ‘to move’ by increment -eu-; not to IE Pok. 507, 508, 511' — supports Nourai in substance.\"}],\n \"consulted\": [\n   c(\"POK\", \"POK_full.txt l.41594-41606\", \"contradicts\", \"Pokorny files Av. yaona- under *i̯eu- 'bind, harness' ('occupation'), not under a root 'move'.\"),\n   c(\"WLD\", \"WLD_Bd1_pages.txt grep 'yaona|yavy'\", \"silent\", \"only ai. yavya- 'Fruchtvorrat' under *i̯eu̯o- 'grain', unrelated.\"),\n   c(\"AHD\", \"AHD_watkins1985.txt grep 'yau|yaona'\", \"silent\", \"no root for this group.\"),\n   DKS_G,\n   c(\"KNT\", \"lexicon s.v. yauviyā-\", \"partial\", \"'perhaps deriv. of root ay-/i-/yā- ‘go’' — a 'going' root too, but a different one.\")],\n \"nodes\": e3_nodes})\n\n# ---------------- entry 4 ----------------\nBRT_Y = c(\"BRT\", \"BRT.txt l.21630 (col. 1286)\", \"supports\", \"'yāvarəna- n. ‘Stössel’ (des Mörsers): ... °nəm zgərəðnō.vaγðanəm ‘ein Stössel mit rundlichem Kopfstück’ V.14.10'.\")\nHRN_Y = c(\"HRN\", \"HRN.txt l.9721-9722 (no. 1125, leaf 266 = printed p.245)\", \"supports\", \"'1125. yāvar, yār- ‘Stössel (des Mörsers)’. aw. yāvarənā- ‘Stössel’ (Geldner, Studien I, 50)'.\")\nHUB_Y = c(\"HUB\", \"HUB.txt l.3784, 5297-5298, 5952\", \"supports\", \"'1125. Darmesteter übersetzt yāvarəna- durch moulin à blé nach der Tradition ... beruht aber auf schlechter Etymologie'; 'Ap. y im Anlaut = np. y in: yāvar, yār ‘Stössel’ = zd. yāvarəna-'.\")\nHRN252 = {\"ref\": \"HRN:252\", \"status\": \"supports\", \"note\": \"Horn no. 1125 (HRN.txt l.9721, leaf 266 = printed p.245, not 252): 'yāvar, yār- ‘Stössel (des Mörsers)’. aw. yāvarənā- ‘Stössel’ (Geldner, Studien I, 50)'. Content matches; page number differs.\"}\nBQT2422 = {\"ref\": \"BQT:2422\", \"status\": \"supports\", \"note\": \"BQT vol 4 p.2422 (pdf 505; ocr/BQT/2422.vision.txt): 'یاور - بروزن ساغر، بمعنی یاری‌دهنده ومددکار باشد - و دستهٔ هاونرا نیز گویند'; fn.6: 'اوستا yâvarena (دستهٔ هاون) (Geldner, Studien 1, 50) «اسشق ۱۱۲۵» ورک: هوبشمان ۱۱۲۵', quoting Nezari Qohestani 'قدر از سر گرز او ساخت یاور ...'.\"}\nentries.append({\n \"entry\": 4, \"root\": \"Yâvarenâ\", \"verdict\": \"confirmed\",\n \"modern_form\": \"Avestan yāvarəna- n. 'pestle (of a mortar)' (Vd. 14.10)\",\n \"note\": \"Avestan yāvarəna- 'pestle' is attested in Vīdēvdād 14.10 (a stone pestle with a rounded head). Bartholomae, Horn (no. 1125, after Geldner) and Hübschmann agree, and Hübschmann rejects the traditional rendering 'mill'. Nourai's gloss 'a stone or tool for beating and crushing grains' is a loose paraphrase of 'pestle'. The citation HRN:252 points to Horn no. 1125, which is on printed p.245 of the 1893 edition. The extraction matches the printed page.\",\n \"note_fa\": \"اوستایی yāvarəna- «دستهٔ هاون» در وندیداد ۱۴:۱۰ آمده است (دستهٔ هاون سنگی با سر گرد). بارتولومه، هرن (ش ۱۱۲۵، به پیروی از گلدنر) و هوبشمان همین معنا را می‌دهند و هوبشمان معنای سنتی «آسیاب» را رد می‌کند. معنای «سنگ یا ابزار کوبیدن غله» در نمودار گزارشی آزاد از همان «دستهٔ هاون» است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [HRN252],\n \"consulted\": [BRT_Y, HUB_Y,\n   c(\"POK\", \"POK_full.txt grep 'yāvar|yavar'\", \"silent\", \"not in Pokorny.\"),\n   c(\"WLD\", \"WLD Bd1/Bd2 grep 'yāvar'\", \"silent\", \"no hit.\"),\n   c(\"AHD\", \"AHD_watkins1985.txt\", \"silent\", \"no IE root given for yāvarəna-.\")],\n \"nodes\": [\n  {\"id\": 1, \"lang\": \"Persian\", \"words\": \"yâvar\", \"verdict\": \"confirmed\",\n   \"derivation\": \"NP yāvar (یاور) 'pestle', with the contracted form yār, continues Av. yāvarəna- (through an unattested MP *yāwar). The suffix -əna- drops, and initial OIr. y- is kept here instead of becoming j- (Hübschmann: 'Ap. y im Anlaut = np. y in yāvar, yār'). This yāvar is a different word from yāvar 'helper' (< yār + -var). Borhan lists both and quotes Nezari Qohestani's line 'قدر از سر گرز او ساخت یاور، قضا از سر خصم او کرد هاون', where yāvar pairs with hāvan 'mortar'. Nourai's gloss 'stone or other objects used for crushing grains' paraphrases Borhan's 'دستهٔ هاون'.\",\n   \"derivation_fa\": \"«یاور» به معنای «دستهٔ هاون» (و صورت کوتاه‌شدهٔ «یار») دنبالهٔ اوستایی yāvarəna- است. پسوند -əna- افتاده و y- آغازی ایرانی باستان این‌بار به ج بدل نشده و مانده است (هوبشمان). این «یاور» با «یاور» به معنای «یاری‌دهنده» (از یار + ور) یکی نیست. برهان قاطع هر دو را آورده و بیت نزاری قهستانی «قدر از سر گرز او ساخت یاور / قضا از سر خصم او کرد هاون» را گواه می‌آورد که «یاور» را در کنار «هاون» نشانده است. ادعای نورایی درست است.\",\n   \"sources\": [],\n   \"ref_check\": [BQT2422],\n   \"consulted\": [HRN_Y, HUB_Y,\n     c(\"BQT\", \"p.2422 fn.6\", \"supports\", \"'اوستا yâvarena (دستهٔ هاون) ... ورک: هوبشمان ۱۱۲۵'.\"),\n     c(\"MON\", \"vajehyab not fetched\", \"silent\", \"not consulted online; Mo'in's view is the BQT footnote above.\"),\n     c(\"ARY\", \"ARY_pages.txt grep 'یاور'\", \"silent\", \"no hit for the 'pestle' sense in the OCR.\")]}]})\n\nout = {\"pdf_page\": 562, \"book_page\": 532, \"verified_by\": \"claude-opus-5.5\", \"verified_on\": \"2026-10-16\", \"entries\": entries}\njson.dump(out, open(\"/home/sfmqrb/git/rishe-private/data/verification/page-562.json\", \"w\", encoding=\"utf-8\"), ensure_ascii=False, indent=1)\nprint(\"ok\")\n"
}
```


### [2026-10-17T00:39:29.521Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-562.py (file state is current in your context — no need to Read it back)
```


## [2026-10-17T00:39:45.764Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; g(){ printf '%s: ' \"$1\"; shift; grep -c -i -E \"$@\" 2>/dev/null | tr '\\n' ' '; echo; }\ng AFA_shlm 'شلم|Jerusalem' AFA.txt\ng AFA_awar 'أوار' AFA.txt\ng AFM_awar 'أوار' AFM.txt\ng FVQ_jer 'Jerusalem' FVQ.txt\ng AKD 'jašp|ašp[uû]|jaspis|jaspu' AKD.txt\ng NYB 'jōy|yōy|jōd' NYB_vol2_glossary.txt\ng ARY_juy 'جوی' incoming/ARY/ARY_pages.txt\ng ARY_yashm 'یشم' incoming/ARY/ARY_pages.txt\ng ARY_yavar 'یاور' incoming/ARY/ARY_pages.txt\ng CHEUNG 'jōy|yauviy' CHEUNG.txt\ng FSD_jer '^Jerusalem' FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt\ng BQT1 'اورشلیم|اورمیه' BQT_v1_pages.txt\ng HRN_urm 'Urmi|Jerusalem' HRN.txt\ng WLD_yaona 'yaona' incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt WLD_band3.txt\ng WLD_yavar 'y[aā]var' incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt WLD_band3.txt\ng POK_yavar 'y[aā]var[əe]n' POK_full.txt\ng AHD 'yaona|yavar|yauviy' AHD_watkins1985.txt\ng HRN_yashm 'ya[sš][mp]|ja[sš][mp]' HRN.txt\ng KLN_yashb 'yashb|yashm' KLN_1966.txt",
 "description": "Run the claimed silent greps across references"
}
```


### [2026-10-17T00:39:46.174Z] TOOL RESULT

```
Exit code 1
(eval):1: defining function based on alias `g'
(eval):1: parse error near `()'
```


## [2026-10-17T00:39:53.777Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; while IFS='|' read -r name pat files; do printf '%s: ' \"$name\"; grep -c -i -E \"$pat\" $files 2>&1 | tr '\\n' ' '; echo; done <<'EOF'\nAFA_shlm|شلم|Jerusalem|AFA.txt\nAFA_awar|أوار|AFA.txt\nAFM_awar|أوار|AFM.txt\nFVQ_jer|Jerusalem|FVQ.txt\nAKD|jašp|ašp[uû]|jaspis|jaspu|AKD.txt\nNYB|jōy|yōy|jōd|NYB_vol2_glossary.txt\nARY_juy|جوی|incoming/ARY/ARY_pages.txt\nARY_yashm|یشم|incoming/ARY/ARY_pages.txt\nARY_yavar|یاور|incoming/ARY/ARY_pages.txt\nCHEUNG|jōy|yauviy|CHEUNG.txt\nFSD_jer|^Jerusalem|FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt\nBQT1|اورشلیم|اورمیه|BQT_v1_pages.txt\nHRN_urm|Urmi|Jerusalem|HRN.txt\nWLD_yaona|yaona|incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt WLD_band3.txt\nWLD_yavar|y[aā]var|incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt WLD_band3.txt\nPOK_yavar|y[aā]var[əe]n|POK_full.txt\nAHD|yaona|yavar|yauviy|AHD_watkins1985.txt\nHRN_yashm|ya[sš][mp]|ja[sš][mp]|HRN.txt\nEOF",
 "description": "Run the claimed silent greps across references"
}
```


### [2026-10-17T00:39:54.216Z] TOOL RESULT

```
AFA_shlm: ugrep: warning: Jerusalem|AFA.txt: No such file or directory 
AFA_awar: 0 
AFM_awar: 1 
FVQ_jer: 5 
AKD: ugrep: warning: ašp[uû]|jaspis|jaspu|AKD.txt: No such file or directory 
NYB: ugrep: warning: yōy|jōd|NYB_vol2_glossary.txt: No such file or directory 
ARY_juy: 5 
ARY_yashm: 0 
ARY_yavar: 2 
CHEUNG: ugrep: warning: yauviy|CHEUNG.txt: No such file or directory 
FSD_jer: ugrep: warning: FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt: No such file or directory 
BQT1: ugrep: warning: اورمیه|BQT_v1_pages.txt: No such file or directory 
HRN_urm: ugrep: warning: Jerusalem|HRN.txt: No such file or directory 
WLD_yaona: ugrep: warning: incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt WLD_band3.txt: No such file or directory 
WLD_yavar: ugrep: warning: incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt WLD_band3.txt: No such file or directory 
POK_yavar: 0 
AHD: ugrep: warning: yavar|yauviy|AHD_watkins1985.txt: No such file or directory 
HRN_yashm: ugrep: warning: ja[sš][mp]|HRN.txt: No such file or directory
```


## [2026-10-17T00:40:01.297Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; while IFS=';' read -r name pat files; do printf '%s: ' \"$name\"; grep -c -i -E \"$pat\" $files 2>&1 | tr '\\n' ' '; echo; done <<'EOF'\nAFA_shlm;شلم|Jerusalem;AFA.txt\nAKD;jašp|ašp[uû]|jaspis|jaspu;AKD.txt\nNYB;jōy|yōy|jōd;NYB_vol2_glossary.txt\nCHEUNG;jōy|yauviy;CHEUNG.txt\nFSD_jer;^Jerusalem;FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt\nBQT1;اورشلیم|اورمیه;BQT_v1_pages.txt\nHRN_urm;Urmi|Jerusalem;HRN.txt\nWLD_yaona;yaona;incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt WLD_band3.txt\nWLD_yavar;y[aā]var;incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt WLD_band3.txt\nAHD;yaona|yavar|yauviy;AHD_watkins1985.txt\nHRN_yashm;ya[sš][mp]|ja[sš][mp];HRN.txt\nEOF\ngrep -n -i 'Jerusalem' FVQ.txt | head -5; grep -n 'أوار' AFM.txt; grep -n -E 'جوی|یاور' incoming/ARY/ARY_pages.txt | head",
 "description": "Re-run greps with safe separator and inspect hits"
}
```


### [2026-10-17T00:40:01.767Z] TOOL RESULT

```
AFA_shlm: 4 
AKD: 1 
NYB: 0 
CHEUNG: 0 
FSD_jer: ugrep: warning: FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt: No such file or directory 
BQT1: 0 
HRN_urm: 1 
WLD_yaona: ugrep: warning: incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt WLD_band3.txt: No such file or directory 
WLD_yavar: ugrep: warning: incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt WLD_band3.txt: No such file or directory 
AHD: 0 
HRN_yashm: 1 
333:Horovitz, J. Das koranische Paradies. Jerusalem, 1923. 
1993:frequently suggested that the destruction of Jerusalem in A.D. 70 
12727:sometimes used for idols, as in the Jerusalem Talmud, Sank, x, 28 d , 
15026:6 That lO3?p as used in the Mishnah and Jerusalem Talmud is but a form of hntflDp, 
16485:at Jerusalem (xvii, 1), of the Church built over the Seven Sleepers 
330:الأوارجة ) 5755 جسات الدخل والخرح يدون 3 )ا 1 
887:بیاوروی ۳ب ایساندن
914:(88 0۳ 8۸ 2مت 5- 070-7100 ۳3) هسند. مثلاً ویژگی‌های جنگجویان هند و
916:ویژگی‌های این جنگجویان از هند باستان گرفته تا آلمان» یونان و روم کهن چنین بوده است.
1077:‎٩‏ رزمجویی: ویژگی دیگر هند و اروپائیان جنگاوری بود..مردمی که طی چند سده از
1079:را اشغال کردند نه تنها از پرتری فنی (اسب و ارابه) برخوردار بودند بلکه از نظر جنگجویی و
6337:۶ / جویدن, جاویدن
10871:وجججججج و ییاور
```


## [2026-10-17T00:40:07.641Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'شلم|Jerusalem' AFA.txt | head; grep -n -i -E 'jašp|ašp[uû]|jaspis|jaspu' AKD.txt; grep -n -i -E 'Urmi|Jerusalem' HRN.txt; grep -n -i -E 'ya[sš][mp]|ja[sš][mp]' HRN.txt; for f in FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt; do grep -c -i '^Jerusalem' $f; done; for f in incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt WLD_band3.txt; do grep -c -i -E 'yaona|y[aā]var' $f; done",
 "description": "Inspect remaining grep hits"
}
```


### [2026-10-17T00:40:08.015Z] TOOL RESULT

```
Exit code 1
9331:zum Pfingstfest in Jerusalem versammelten Juden, die dann
9453:12. Man hat darin zu Unrecht einen Jerusalem walliahrer
9455:"npsn ri*3» woraus später ^lVÄ^ für Jerusalem gewor-
9457:»her sind in jenen Zeiten schwerlich nach Jerusalem ge-
968:[akk.  aJpü,  auch  jasupü  und  jos^m  eine  Steinart,  viell.  Magnesit  (s. S.  59  Anm.  1)  :  dazu  wohl  späthebr.  jclspe  ein  Steinname,  und  doch  wohl auch  griech.  Xaam?  usw.,  Jaspis^  [akk.  algnmisu  eine  Steinart,  auch  im
368:(S. 25), tischaq neben eschaq (S. 28), turmis neben termus
1119:(4); wa;K. yas, minj. ydsap, yasp,
0
1
6
3
2
1
0
```


## [2026-10-17T00:40:13.644Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1115,1120p HRN.txt; grep -n -i -E 'yaona|y[aā]var' incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt WLD_band3.txt | cut -c1-300; grep -n -i -A2 '^Jerusalem' FSD_vol2.txt | head -8",
 "description": "Inspect Horn, WLD and FSD hits"
}
```


### [2026-10-17T00:40:14.015Z] TOOL RESULT

```
ap. Aspa[cana-, uv]aspa- fschöne Pferde habend');
aw. aspa- 'Pferd'; phlv. asp; ai. dgva-,
kurd. hasp; af>'. fls, aspa (fem.) 'Pferd, Stute'; oss.
d. äfsä, t. yäfs 'Stute' (41); bei. aps, haps (LW. asp)
(4); wa;K. yas, minj. ydsap, yasp,
ap. asa[hara' und np. es[^^r (No. 86) stützen sich
incoming/WLD/WLD_Bd2_pages.txt:34042:   ^su- ist Tiefstufe zu                               ^'77-, z. B. hva-yaona-
incoming/WLD/WLD_Bd1_pages.txt:18418:tigen 44 (Praes. yavayeiti Inf. ydto, yuta), yaona- n. „Besehaftigung 44 yav-
incoming/WLD/WLD_Bd1_pages.txt:20346:der Spreu, beutle“, parai nsginxlaai Hes. (iiberliefert yavar Tteginxiaar.
45485:Jerusalem:  an  ancient  spelling;  in  the  1811  edition. hle'«8py",  n.  Same  as  I«spy. hl"fa-lu'tln,  a.  &   n.  See  highfalutin.
45486-HIg'den.lhig'den;  2   Mg'dEn,  Eanulph  orEalph  (I299?-Vij 1364).  An  English  Benedictine  monk  and  chronicler, hig'don,  1   hig'dsn;  2   hlg'don,  n.  [Local,  XT.  S.l  A   mixed pickle  made  of  green  tomatoes.  „   ,
45487-Blg-ga'lon,  1   hi-gS'yen;  2   hl-ga'y6n,  n.  Bib.  Fs.  1/.  18- Hig'gin-son,  l hlg'm-san;  2 hig'ln-son,  n.  1.  Francis  (1587- Ve  1630),  an  English  divine  and  writer.  2,  John(  V6l616- 1   Vs  1708),  an  American  pastor;  son  of  Francis.  3.  Ihonias Wentworth  C‘V23lS23-Vsl91T).  American  author  and soldier:  colonel  of  the  first  colored  regiment  in  the  Civil  War. Hlg'glns-vllle,  1   hlg'mz-vil;  2   hia'lns-vll,  n.  A   village  in Lafayette  county.  Mo.  .   ,   ,   ,   ,   -   m
```


## [2026-10-17T00:40:34.325Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 - <<'EOF'\np='build-562.py'; s=open(p).read()\nrep=[\n('c(\"AFA\", \"AFA.txt grep \\'شلم|Jerusalem\\'\", \"silent\", \"Fraenkel does not treat the name.\"),',\n 'c(\"AFA\", \"AFA.txt grep \\'شلم|Jerusalem\\' (l.9331-9457)\", \"silent\", \"Fraenkel mentions Jerusalem only in passing (Pentecost, pilgrims); no etymology of the name.\"),'),\n('c(\"AFA\", \"AFA.txt grep \\'يرى|أورى\\'\", \"silent\", \"no treatment of yrh/Jerusalem.\"),',\n 'c(\"AFA\", \"AFA.txt grep \\'شلم|Jerusalem\\' (l.9331-9457)\", \"silent\", \"only incidental mentions of Jerusalem; no treatment of yrh or of the name.\"),'),\n('c(\"FVQ\", \"FVQ.txt grep \\'Jerusalem\\'\", \"silent\", \"Jeffery has no entry for the name (it is not Qur\\'anic).\")',\n 'c(\"FVQ\", \"FVQ.txt grep \\'Jerusalem\\' (5 hits)\", \"silent\", \"only incidental mentions (bibliography, Talmud Yerushalmi); no entry for the name, which is not Qur\\'anic.\")'),\n('c(\"AKD\", \"AKD.txt grep \\'jašp|ašpû|jaspis\\'\", \"silent\", \"Zimmern does not list it among Akkadian loanwords in this OCR.\"),',\n 'c(\"AKD\", \"AKD.txt l.968\", \"partial\", \"Zimmern: \\'akk. ašpû, auch jašupû und jošpû eine Steinart, viell. Magnesit: dazu wohl späthebr. jāšpe ein Steinname, und doch wohl auch griech. iaspis usw., Jaspis\\' — makes Akkadian, not Hebrew, the oldest attested form.\"),'),\n('c(\"WLD\", \"WLD Bd1 grep \\'yaona\\'\", \"silent\", \"no hit.\"),',\n 'c(\"WLD\", \"WLD_Bd1_pages.txt l.18418\", \"contradicts\", \"\\'yaona- n. Beschäftigung\\' (under i̯eu- \\'bind\\') — same as Pokorny.\"),'),\n('c(\"WLD\", \"WLD_Bd1_pages.txt grep \\'yaona|yavy\\'\", \"silent\", \"only ai. yavya- \\'Fruchtvorrat\\' under *i̯eu̯o- \\'grain\\', unrelated.\"),',\n 'c(\"WLD\", \"WLD_Bd1_pages.txt l.18418, 18615\", \"contradicts\", \"Av. yaona- n. \\'Beschäftigung\\' under i̯eu- \\'bind\\'; ai. yavya- \\'Fruchtvorrat\\' under i̯eu̯o- \\'grain\\' — no root \\'move\\'.\"),'),\n('c(\"ARY\", \"ARY_pages.txt grep \\'جوی\\'\", \"silent\", \"no clear entry in the OCR.\")',\n 'c(\"ARY\", \"ARY_pages.txt grep \\'جوی\\'\", \"silent\", \"5 hits, all in unrelated words (جنگجویی, جویدن); no entry for jōy.\")'),\n('c(\"ARY\", \"ARY_pages.txt grep \\'یاور\\'\", \"silent\", \"no hit for the \\'pestle\\' sense in the OCR.\")',\n 'c(\"ARY\", \"ARY_pages.txt grep \\'یاور\\'\", \"silent\", \"2 hits, both noise (بیاوروی, ییاور); no entry for yāvar \\'pestle\\'.\")'),\n('c(\"AFM\", \"AFM.txt grep \\'أوار\\'\", \"silent\", \"no hit.\"),',\n 'c(\"AFM\", \"AFM.txt grep \\'أوار\\'\", \"silent\", \"only الأوارجة (account book), unrelated.\"),'),\n]\nfor a,b in rep:\n    assert a in s, a[:60]; s=s.replace(a,b)\nopen(p,'w').write(s)\nEOF\npython3 build-562.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-562.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 562",
 "description": "Patch notes, build JSON, validate and run checker"
}
```


### [2026-10-17T00:40:34.947Z] TOOL RESULT

```
Traceback (most recent call last):
  File "<stdin>", line 23, in <module>
AssertionError: c("AFM", "AFM.txt grep 'أوار'", "silent", "no hit."),
ok
nodes verified: 17/17
node verdicts: {'plausible': 5, 'disputed': 2, 'confirmed': 10}
root verdicts: {'plausible': 3, 'confirmed': 1}
ref checks: {'supports': 14, 'not_checked': 4, 'partial': 2}
books consulted: {'supports': 32, 'silent': 23, 'partial': 5, 'contradicts': 2} | by book: {'KLN': 9, 'HRN': 6, 'SKT': 6, 'FSD': 6, 'BQT': 5, 'ISS_alt_DKS': 4, 'ARY': 3, 'BRT': 3, 'AFA': 2, 'ARB': 2, 'AFM': 2, 'LKT': 2, 'MON': 2, 'HUB': 2, 'IRN': 1, 'KNT': 1, 'PHD': 1, 'NYB': 1, 'CHEUNG': 1, 'POK': 1, 'WLD': 1, 'SOD': 1}
```


## [2026-10-17T00:40:41.041Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; grep -n \"AFM.txt grep 'أوار'\" build-562.py",
 "description": "Find the AFM line in build script"
}
```


### [2026-10-17T00:40:41.433Z] TOOL RESULT

```
56:    c("AFM", "AFM.txt grep 'أوار'", "silent", "no hit.")]},
```


## [2026-10-17T00:40:55.880Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 - <<'EOF'\np='build-562.py'; s=open(p).read()\nrep=[\n('c(\"AFA\", \"AFA.txt grep \\'شلم|Jerusalem\\'\", \"silent\", \"Fraenkel does not treat the name.\"),',\n 'c(\"AFA\", \"AFA.txt grep \\'شلم|Jerusalem\\' (l.9331-9457)\", \"silent\", \"Fraenkel mentions Jerusalem only in passing (Pentecost, pilgrims); no etymology of the name.\"),'),\n('c(\"AFA\", \"AFA.txt grep \\'يرى|أورى\\'\", \"silent\", \"no treatment of yrh/Jerusalem.\"),',\n 'c(\"AFA\", \"AFA.txt grep \\'شلم|Jerusalem\\' (l.9331-9457)\", \"silent\", \"only incidental mentions of Jerusalem; no treatment of yrh or of the name.\"),'),\n('c(\"FVQ\", \"FVQ.txt grep \\'Jerusalem\\'\", \"silent\", \"Jeffery has no entry for the name (it is not Qur\\'anic).\")',\n 'c(\"FVQ\", \"FVQ.txt grep \\'Jerusalem\\' (5 hits)\", \"silent\", \"only incidental mentions (bibliography, Talmud Yerushalmi); no entry for the name, which is not Qur\\'anic.\")'),\n('c(\"AKD\", \"AKD.txt grep \\'jašp|ašpû|jaspis\\'\", \"silent\", \"Zimmern does not list it among Akkadian loanwords in this OCR.\"),',\n 'c(\"AKD\", \"AKD.txt l.968\", \"partial\", \"Zimmern: \\'akk. ašpû, auch jašupû und jošpû eine Steinart, viell. Magnesit: dazu wohl späthebr. jāšpe ein Steinname, und doch wohl auch griech. iaspis usw., Jaspis\\' — makes Akkadian, not Hebrew, the oldest attested form.\"),'),\n('c(\"WLD\", \"WLD Bd1 grep \\'yaona\\'\", \"silent\", \"no hit.\"),',\n 'c(\"WLD\", \"WLD_Bd1_pages.txt l.18418\", \"contradicts\", \"\\'yaona- n. Beschäftigung\\' (under i̯eu- \\'bind\\') — same as Pokorny.\"),'),\n('c(\"WLD\", \"WLD_Bd1_pages.txt grep \\'yaona|yavy\\'\", \"silent\", \"only ai. yavya- \\'Fruchtvorrat\\' under *i̯eu̯o- \\'grain\\', unrelated.\"),',\n 'c(\"WLD\", \"WLD_Bd1_pages.txt l.18418, 18615\", \"contradicts\", \"Av. yaona- n. \\'Beschäftigung\\' under i̯eu- \\'bind\\'; ai. yavya- \\'Fruchtvorrat\\' under i̯eu̯o- \\'grain\\' — no root \\'move\\'.\"),'),\n('c(\"ARY\", \"ARY_pages.txt grep \\'جوی\\'\", \"silent\", \"no clear entry in the OCR.\")',\n 'c(\"ARY\", \"ARY_pages.txt grep \\'جوی\\'\", \"silent\", \"5 hits, all in unrelated words (جنگجویی, جویدن); no entry for jōy.\")'),\n('c(\"ARY\", \"ARY_pages.txt grep \\'یاور\\'\", \"silent\", \"no hit for the \\'pestle\\' sense in the OCR.\")',\n 'c(\"ARY\", \"ARY_pages.txt grep \\'یاور\\'\", \"silent\", \"2 hits, both noise (بیاوروی, ییاور); no entry for yāvar \\'pestle\\'.\")'),\n('c(\"AFM\", \"AFM.txt grep \\'أوار\\'\", \"silent\", \"no hit.\")',\n 'c(\"AFM\", \"AFM.txt grep \\'أوار\\'\", \"silent\", \"only الأوارجة (account book), unrelated.\")'),\n]\nfor a,b in rep:\n    assert a in s, a[:60]; s=s.replace(a,b)\nopen(p,'w').write(s)\nEOF\npython3 build-562.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-562.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 562 | grep -E 'PROBLEM|verdicts|ref checks|consulted'",
 "description": "Apply patches, rebuild JSON, run checker"
}
```


### [2026-10-17T00:40:56.454Z] TOOL RESULT

```
ok
node verdicts: {'plausible': 5, 'disputed': 2, 'confirmed': 10}
root verdicts: {'plausible': 3, 'confirmed': 1}
ref checks: {'supports': 14, 'not_checked': 4, 'partial': 2}
books consulted: {'supports': 32, 'silent': 22, 'partial': 5, 'contradicts': 3} | by book: {'KLN': 9, 'HRN': 6, 'SKT': 6, 'FSD': 6, 'BQT': 5, 'ISS_alt_DKS': 4, 'ARY': 3, 'BRT': 3, 'AFA': 2, 'ARB': 2, 'AFM': 2, 'LKT': 2, 'MON': 2, 'HUB': 2, 'IRN': 1, 'KNT': 1, 'PHD': 1, 'NYB': 1, 'CHEUNG': 1, 'POK': 1, 'WLD': 1, 'SOD': 1}
```


## [2026-10-17T00:41:09.134Z] TOOL CALL #71: SubagentHandback

```json
{
 "message": "Page 562 (book page 532) is verified and written to `/home/sfmqrb/git/rishe-private/data/verification/page-562.json`. It is valid JSON and `verify_check.py 562` reports 0 PROBLEM lines, with all 17 nodes covered. Entry 2 (Yâšfeh) is a redirect and was skipped.\n\n**Verdicts**\n- **Roots:** 3 plausible (Yârâh, Yâšfa, Yau/Gyŭna), 1 confirmed (Yâvarenâ).\n- **Nodes:** 10 confirmed, 5 plausible, 2 disputed, 0 transcription_suspect.\n- **Nourai's own references:** 14 support the arrow, 2 partly support it, 4 could not be checked (MON5:195, and ISS:91 three times; Bailey's Dictionary of Khotan Saka was used in place of ISS and supports him in substance).\n\n**Disputed**\n- **Yârâh / Persian Ûrmîyeh (\"city of water\"):** Urmia has nothing to do with Hebrew yārāh. The Syriac reading ur + mia is itself a popular etymology; other scholars propose an Urartian origin (Frye) or Indo-Iranian ūrmi- \"wave\" (Burrow). In the same node, Ûršalîm comes from the Hebrew name through Syriac and Arabic, which is fine, but \"city of peace\" is a folk etymology.\n- **Yârâh / Arabic al-avâra (\"place, location\"):** There is no such Arabic noun from yārāh. al-Jawaliqi (ARB) writes \"وقالوا في اسم الموضع «أُوارة»\", which names the place Uwāra in Arabia. Nourai seems to have read \"اسم الموضع\" (name of a place) as the meaning of the word.\n\n**Other notable findings**\n- **Avestan yaona:** the attested sense is \"place, home\" (Bartholomae; Sogdian ywn \"place\"). Pokorny and Walde-Pokorny give \"occupation\". The chart's \"movement\" is Bailey's interpretation alone, so the node is plausible, not confirmed.\n- **Yâšfa:** modern sources treat jasper as a borrowed stone-name of unclear, possibly Egyptian, origin, not one that starts in Hebrew. Wiktionary derives Arabic yašb from Persian yašp, the opposite of the chart's Arabic → Persian arrow.\n- **Cited pages that are off:** HRN:252 is Horn no. 1125, which is on printed p.245. IRN:28 is actually printed p.38 (pdf 39).\n\n**Extraction errors:** none. The JSON matches the printed page.\n\nI also saved the two Borhan pages I read from the scans as `data/verification/sources/refs/ocr/BQT/2434.vision.txt` and `2422.vision.txt`, and archived 8 web sources with `fetch_source.py`."
}
```


### [2026-10-17T00:41:09.420Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
