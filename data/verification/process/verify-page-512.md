# Verification process log — verify-page-512


## [2026-10-15T02:44:16.516Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 512 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-512.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-512.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-512.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 512` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.587Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:20.120Z] TOOL CALL #1: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md; echo ====; cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-512.txt; echo ====; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-512.json",
 "description": "Read instructions, chart text, and source JSON"
}
```


### [2026-10-15T02:44:20.644Z] TOOL RESULT

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


## [2026-10-15T02:44:22.416Z] TOOL CALL #2: Bash

```json
{
 "command": "sed -n '/SAVE what you/,/Wiktionary\\*\\* (en.wiktionary/p' /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md",
 "description": "Read truncated middle of instructions"
}
```


### [2026-10-15T02:44:22.851Z] TOOL RESULT

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


## [2026-10-15T02:44:24.890Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/agent/charts/page-512.txt; echo =====; head -c 3000 data/extracted/batch/page-512.json; echo; cat data/verification/sources/SOURCE_MATRIX.md | head -80; ls data/verification/page-51*.json",
 "description": "Read chart text, JSON head, source matrix"
}
```


### [2026-10-15T02:44:25.331Z] TOOL RESULT

```
Exit code 1
=== PDF page 512 (book page 482) ===
--- entry 0 ---
ROOT [Indo-European] Trenk, Tronkus : to push; pressed, oppressed  (refs POK:1093)
#1 (parent #0) [Avestan] refs=POK:1093; KLN:1612 | traxtanam : pressed together
  #2 (parent #1) [‼UNCLEAR] refs=None |  | NOTE: Box printed with double border (matching this book's style for Persian boxes) but with no header text or word content visible in the source scan.
#3 (parent #0) [Germanic] refs=KLN:1612 | dringan : to press on, oppress
  #4 (parent #3) [English] refs=None | throng
#5 (parent #0) [Latin] refs=POK:1093; KLN:1660 | trancus : tree stem | NOTE: AHD:1546 derives this word from the Indo-European root "Ter 1:to overcome".
  #6 (parent #5) [English] refs=None | trunk, truncate, trench
--- entry 1 ---
ROOT [Indo-European] Trep 1 : to tremble, be restless  (refs POK:1094)
#1 (parent #0) [Old Iranian] refs=BQT:1083 | thrapu : restless, quick
  #2 (parent #1) [Old Persian] refs=BQT:1083 | čapu-ka : restless, quick
    #3 (parent #2) [Pahlavi] refs=BQT:607, 1083 | čâpŭk : swift ; sapŭk : light, swift
      #4 (parent #3) [Persian] refs=BQT:607, 1083 | čâbok «چابک» : swift ; sabok «سبک» : light, fast
#5 (parent #0) [Sanskrit] refs=POK:1094; BQT:1083; KLN:1646 | trprâh : hasty
#6 (parent #0) [Latin] refs=POK:1094 | trepidus : agitated, alarmed
  #7 (parent #6) [English] refs=None | trepid
--- entry 2 ---
ROOT Trep 2 -> redirect to Terp
(eval):1: ==== not found
```


## [2026-10-15T02:44:27.485Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/extracted/batch/page-512.json | head -c 2500; echo; echo \"----\"; cat data/verification/sources/SOURCE_MATRIX.md | head -90; ls data/verification/ | tail -20",
 "description": "Read JSON and source matrix"
}
```


### [2026-10-15T02:44:28.255Z] TOOL RESULT

```
{
  "pdf_page": 512,
  "book_page": 482,
  "entries": [
    {
      "root": {
        "name": "Trenk, Tronkus",
        "lang": "Indo-European",
        "refs": "POK:1093",
        "gloss": "to push; pressed, oppressed"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1093; KLN:1612",
          "words": [
            {"translit": "traxtanam", "gloss": "pressed together", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "‼UNCLEAR",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": "Box printed with double border (matching this book's style for Persian boxes) but with no header text or word content visible in the source scan.",
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "KLN:1612",
          "words": [
            {"translit": "dringan", "gloss": "to press on, oppress", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "throng", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:1093; KLN:1660",
          "words": [
            {"translit": "trancus", "gloss": "tree stem", "script": null}
          ],
          "script_extra": null,
          "note": "AHD:1546 derives this word from the Indo-European root \"Ter 1:to overcome\".",
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "trunk, truncate, trench", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Trep 1",
        "lang": "Indo-European",
        "refs": "POK:1094",
        "gloss": "to tremble, be restless",
        "note": "May be related to the root \"Tres:to tremble\""
    
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
.rw-r--r--   57k sfmqrb 14 Oct 22:14  page-480.json
.rw-r--r--   43k sfmqrb 14 Oct 22:14  page-481.json
.rw-r--r--   75k sfmqrb 14 Oct 22:14  page-482.json
.rw-r--r--   27k sfmqrb 14 Oct 22:14  page-483.json
.rw-r--r--   67k sfmqrb 14 Oct 22:14  page-484.json
.rw-r--r--   49k sfmqrb 14 Oct 22:14  page-485.json
.rw-r--r--   63k sfmqrb 14 Oct 22:14  page-486.json
.rw-r--r--   72k sfmqrb 14 Oct 22:14  page-487.json
.rw-r--r--   55k sfmqrb 14 Oct 22:14  page-488.json
.rw-r--r--   60k sfmqrb 14 Oct 22:14  page-489.json
.rw-r--r--   64k sfmqrb 14 Oct 22:14  page-490.json
.rw-r--r--   55k sfmqrb 14 Oct 22:14  page-491.json
.rw-r--r--   70k sfmqrb 14 Oct 22:14  page-492.json
.rw-r--r--   68k sfmqrb 14 Oct 22:14  page-493.json
.rw-r--r--   62k sfmqrb 14 Oct 22:14  page-494.json
.rw-r--r--   60k sfmqrb 14 Oct 22:14  page-495.json
.rw-r--r--   66k sfmqrb 14 Oct 22:14  page-496.json
.rw-r--r--   35k sfmqrb 14 Oct 22:14  page-497.json
.rw-r--r--   64k sfmqrb 14 Oct 22:14  page-498.json
.rw-r--r--   49k sfmqrb 14 Oct 22:33  page-499.json
```


## [2026-10-15T02:44:31.632Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/512.jpg; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; pdftoppm -f 512 -l 512 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg512; ls $S/pg512*; sed -n 1,200p tools/verify_check.py | grep -n -i 'problem' | head -40",
 "description": "Render page image and inspect check script"
}
```


### [2026-10-15T02:44:32.566Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   54k sfmqrb 14 Oct 22:15  site/pages/512.jpg
Permissions Size User   Date Modified Name
.rw-r--r--   59k sfmqrb 14 Oct 22:44  /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg512.png
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


## [2026-10-15T02:44:34.116Z] TOOL CALL #6: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg512.png"
}
```


### [2026-10-15T02:44:34.485Z] TOOL RESULT

```

```


## [2026-10-15T02:44:34.477Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-15T02:44:55.392Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'trenk' POK_full.txt | head -20; echo \"----\"; grep -n -i \"trep-\" POK_full.txt | head -20; echo \"----\"; cat ../refs_online.json | python3 -c \"import json,sys; d=json.load(sys.stdin); [print(k, {x:d[k].get(x) for x in ('kind','local_file','page_offset','lookup_hint')}) for k in ('POK','KLN','BQT','AHD')]\"",
 "description": "Grep Pokorny for trenk and trep; show refs info"
}
```


### [2026-10-15T02:44:55.959Z] TOOL RESULT

```
82024:anstrengen', strenk- 'straff 
82136:as nasalized form strenk-, streng-, see there. 
83167:Root / lemma: strenk-, streng- 
83212:Latvian strenka/s ' e\n piece verharteten Auswurfs' (perhaps ' stiff, rigid'). 
87272:Root / lemma: trenk-1 
87318:Old Icelandic t^rgngi); trenku, tr/nkt/'wasW (see also *trenk-'\Nas\r\'), trinkiu, -e//"din, 
87329:Root / lemma: trenk-2 
87335:balneare' (-c/7- probably from -nk-s-); about Lithuanian trenku, tr/nkt/'\Nas\r\' see above. 
----
82268:strep-: 
83217:Root / lemma: (s)trep- (s)treb- 
85949:See also: extensions: trem-, //les- (Kombinationsform *trems-), trep-. 
86134:4. terp-, trep-{ov\\y Balto Slavic): Latvian farps^\Nom\' ('the Zerbohrende'), Lithuanian 
86305:Root / lemma: terp- trep- 
87233:Note: (contaminated with tres-), the same double meaning by trep- 
87343:Root / lemma: trep-1 
87365:feststampfen' (besides probably through hybridization with Germanic *trep-, *tremp-, see 
87369:Lithuanian trepsetH^. Pers. trepsi, old trepsti) "with den Fijften trampein', trep-{l)enti6s., 
87381:Root / lemma: trep-2 
87400:See also: Indo Germanic trep- " turn ' extension from /e/'-J"rub, drehend reiben, turn'? 
87404:Root / lemma: trep-3, treb- 
87408:See also: see above S. 1037 under (s)trep-. 
----
POK {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"}
KLN {'kind': 'archive_djvu', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."}
BQT {'kind': 'archive_djvu+local_scan_ocr', 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"}
AHD {'kind': 'archive_djvu+website+archive_restricted', 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."}
```


## [2026-10-15T02:44:57.720Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 87265,87410p POK_full.txt",
 "description": "Print Pokorny trenk/trep entries"
}
```


### [2026-10-15T02:44:58.106Z] TOOL RESULT

```
Tocharian A tram-"in rage, fury geraten', B trem/'rage, fury'. 

References: WP. I 758, WH. II 701, Trautmann 329 f., Vasmer 3, 144, 146 f. 
See also: compare ter-f wriggle ', worfrom *trem- and *tres- extended are. 
Page(s): 1092-1093 

Root / lemma: trenk-1 

Meaning: to push; to oppress 

Note: s. also //•e/7Ar-'wash, bathe' 

Material: Avestan ^raxtan^m Gen. PI. "zusammengedrangf (in the meaning to Germanic 

stimmend); 

Latin truncus'tree truck, trunk'. Adj. 'mutilated, the Aste or Glieder stolen; looted ', 
trunco, -are^ mutilate '; gall, trincos^a kind of Gladiatoren' (Vendryes RC. 39, 404 f.); 
perhaps ("es drangt myself) Old Irish di-fo-thracc-^yN\s\\\ verbal noun duthracht, probably 
(as "abgedrangt become') Old Irish Middle Irish treicim^ leave, retreat', cymr. trengi^ wilt, 
wither, die', tranc, PI. trangaum. "Abschied, death, end'; 

maybe alb. trung ' stump' , alb. Geg {*truncus) truni^{*a dolt, blockhead), brain, head' from 
Latin truncus -a -um "maimed, mutilated, cut short. M. as subst. truncus -i, a lopped tree, 
the trunk of a tree; the trunk of a human body. Transf. a dolt, blockhead', also alb. trqgull, 
trangu//' cucumber, a dolt, blockhead'. 

Gothic f^re/han' urge, press, push' (from Proto German *l=>renxd, *l=>ri"xo, through ablaut 
derailment t^raih, t^rafhans, faihu-t^raihna {Dai. Sg.) " richness '; also Old Saxon thregian. 
Middle Low German Dutch o'/'e/ge/? "threaten'? Ein West Germanic *A'/777-= Gothic t^reih- 
certainly in Middle High German o'/777e"Stecknadel, Handgerat of Flechtens and Webens'; 
with gramm. variation Old Icelandic l=>ryngja, -va, /=>rgng' press, urge, press, push, press' 
(for *A'/7/7^a probably after dem Adj. f^rgngr' r\arro\N' from *t^rangu-). Old Saxon thringan. 
Old English dr/ngan stem V., Old High German dr/ngan ds. (Middle High Germar\ dr/ngen 
also "flax, wattle, braid, to weave', see above dnhe ar\d compare above *terk- ^turr\'); Kaus. 
Old Icelandic I=>r0ngja^ urge, press, push, constrain, oblige, in die clamp bringen'. Middle 
High German drengen 'urge, press, push\ Old Icelandic l=>rgngr^v\arro\N' (= 
Lithuanian//'a/7/r^s), Middle High German drange, gedrange Mn . "narrow'; Old Icelandic 
l=>rgng. Gen. -vari. "crush, narrowness'. Old Englisho'/'5/7^m. "crush, gedrangte troop, 
multitude, crowd'. Middle High German dranc 'Drang', Old High German drangon' urge, 
press, push (= Lithuanian trankali); 



Old Icelandic l=>rseta, /=>rcetta 'quarre\, sich quarrel, squabble, bestreiten' {*t^ranxatjan); 
Old English t^rseir farmhand, Unfreier' etc. {*t^ranhilaz)\ 

ngr. 5poOYYOc;, late Latin drungus an6 Old Irish drong 'troop, multitude, crowd' are 
genuine Celtic {*6^rungho) and keine Germanic loanword; wrongly above S. 255; 

Lithuanian //'e/7/r//"drohnend bump, poke'. Frequent, trankau, -yti{= Old High German 
drangon), tranksmas' crush, resonance ', trankus' bumpy ' (actually 'pushing, thrusting ' = 
Old Icelandic t^rgngi); trenku, tr/nkt/'wasW (see also *trenk-'\Nas\r\'), trinkiu, -e//"din, 
drone'; Latvian triecu, tr'iekV grind, crush, squeeze hard, squash; wegjagen'; triecinat 
'upset', truoksn/s'6\n, fuss, noise, Gepolter'; Old Prussian pertr/nktan \erstockt'; russ. 
trutyth' press, bump, poke', serb. //x/c/'Z/'schmeiften'; 

Aniautdublette in slov. drgkaf/ "bump, poke, stomp, squeeze'. Old Church Slavic udrgciti 
'niederdriJcken, torment, smite'?. 

References: WP. I 758 f., WH. II 710 f., Trautmann 328 f., Vasmer 3, 144, 145. 
Page(s): 1 093 

Root / lemma: trenk-2 

Meaning: to wash, bathe 

Material: Irish fothrucud'ba\he', bret. gozronquetds. {*tronk-), cymr. //-c»c/7/'mergere, 

balneare' (-c/7- probably from -nk-s-); about Lithuanian trenku, tr/nkt/'\Nas\r\' see above. 

References: WP. I 759; 

See also: probably identical with //'e/7/r-/;compare above S. 819 about Lithuanian pert/. 

Page(s): 1 094 

Root / lemma: trep-1 

Meaning: to trample, tread 

Material: Old Indie trpra-, trpa/a-' hasty, unstet'? (probably from 'trippeind'); afghan. drabs/ 

'jiggle, shake, herabdriJcken'; gr. Tponsu) 'keltere' ('trete die Trauben from'), arpanoc;, 

hom. aTapn6(; 'Fuftsteig' (a- 'copulativum', actually 'ausgetretenerway'), rponsovTO 

erraTouv Hes., Oivorponoi 'Gottheiten of Weinbaues'; alb. *tr/p= gr. rpan- in sh-t/p, sh-typ 

'zertrete, grind, crush, zerquetsche', per-t(r)yp' chew ', sh-trip, zdryp'stexqe herab'; 

Latin trepidus' anxiously umherlaufend', trepido, -are' walk on tiptoe; trip, from 
Geschaftigkeit or fear'; 



Old English draf/an' press, urge, press, push, drive, push; rebuke, reproach'; engl. dial. 
thrave, fhreave ^ dr\ft, trailing, herd'. Old Saxon thra5dn' trot', Middle High German draben 
ds. (= russ. tropatb), Swedish /Aai/'festgefahrener Schnee auf Wegen', trav/a ^{sr\ow) 
feststampfen' (besides probably through hybridization with Germanic *trep-, *tremp-, see 
below der-^rur\\ Middle Low German o'/'5/r7/7e/7 "trample'. East Frisian Dutch drempel. Low 
German drumper threshold'. Middle Low German dorper threshold'); 

Lithuanian trepsetH^. Pers. trepsi, old trepsti) "with den Fijften trampein', trep-{l)enti6s., 
trypset/6s., ablaut, tryp/'u, trypt/"trarc\p\e' {ior * trip-); trapineti^Wxth den Fijften bump, poke', 
Old Prussian trapt'tread', ertreppa' sie ijbertreten '; 

Old Church Slavic //'e/0e/b"das Zittern, Beben', //'eyoe/5//"tremble', //'(9y05//"palpare', 
Bulgarian tropam^ stamp, trample, trapple', tropotm. "Getrampel', russ. tropatb^ stomp, 
trample, with den Fijften treten', tropai. " path, track; Fahrte'. 

References: WP. I 756, WH. II 701 f., Trautmann 329, Vasrner 3, 136, 140 f. 
See also: As trem- and tres- probably extension from ter-1 " wriggle '. 
Page(s): 1 094 

Root / lemma: trep-2 

Meaning: to turn; to bow the head (of shame) 

Material: Old Indie trapate^ scharut sich, wird verlegen', trapa\. "the genitals, Verlegenheit'; 

gr. Tpsnu), Doric Ionian rpanw "wende', rponn " reversal ', Tp6no(; " turn ', tpottk; "keel, 
Grundbalken of Schiffes' (actually "Wender'), TpooTrau) "wende, verandere', Med. " turn, 
twist, rotate myself um, kehre um', sv-TpsTTopai "wende myself jemandem to, schame 
myself vorjemandem', £UTpan£Ao(; "movable, nimble';T£pTTiKepauvo(; in spite of TspncbpsGa 
TpsncbpisGa Hes. not "fulmina torquens', but to TsprrEiv, -eaOai as "the Blitzfrohe'; 

Latin trepit ^yert\t'; turpis {* trpis) "ugly, nasty ' ("*wovor man sich abwenden muft', 
formation as Gothic it'/'J/rs "usable'), -ur- instead of -o/"- dialect. 

Maybe alb. {* turpis) turp^ shame' 

References: WP. I 756 f., WH. II 702, 719, Mayrhofer 530. 

See also: Indo Germanic trep- " turn ' extension from /e/'-J"rub, drehend reiben, turn'? 

Page(s): 1 094 

Root / lemma: trep-3, treb- 



See also: see above S. 1037 under (s)trep-. 
Page(s): 1 095
```


## [2026-10-15T02:45:03.560Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'raxtan\\|raxta-\\|θraxt\\|draxta' BRT.txt | head; echo \"-- KLN\"; grep -n -i '^throng\\|^trunk\\|^truncate\\|^trench,\\|^trepid' KLN_1966.txt | head -20; echo \"-- AHD\"; grep -n -i '^trenk\\|^ter-\\|^trep\\|^terə\\|^ter(ə)' AHD_watkins1985.txt | head; grep -n -i 'TRUNK\\|THRONG\\|TREPID' AHD_watkins1985.txt | head",
 "description": "Grep BRT, KLN, AHD for headwords"
}
```


### [2026-10-15T02:45:03.984Z] TOOL RESULT

```
<persisted-output>
Output too large (35.6KB). Full output saved to: /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/bbfslxx2q.txt

Preview (first 2KB):
14069:a  drynja-,  7  dadrang-''>,  16  (Des.)  dh drayia-*'*,  i^drfnjaya-.  — PPfP.  •draxta-^''. 'festigen,  kräftigen,  bestärken':  änräm aSal^qm  axlinam  fqtiayö  dnnjatH  (statt Plur.)  "ein  Drittel  dieser  Krankheiten  be- stärken die  Menscher"  V.  7. 59  Gl.  Un- klar: tun^ö  hs  dqdrqxtii>  V.  4. 10  PüZ. mit  a  i)  'etwas  befestigen  an  — '  (AbL): äjir»njaySiS  aom  srum  paurva.naimäj (sd.)    aAe    gravaAe  V.5.  14.  2)  'fest-
14493:•  j.  ^Oraxta-')  Adj.  'zusammengedrängt, eng  aufgeschlossen':  'ianam  rasmanqm "phalangum  stipatarura"  Yt.  14-  63-
20954:paiti-ayatahs {^^  Yt  /j.  7;  —  *'iraxtanqm (sd.)  rasmanqm  yüxtanqm  ssi%ranqm ".  .  der  verbündeten  Länder"  Yt.  i4- 63.  b)  mit  Angabe  des  womit?  durch b)  Instr.:  kyat  daina  . .  yüpn  (sd.,  bei4) , . tt^ä  yuxiä  y.4<).  9.  ß)  Dat:  kS  vätai
25219:j  49;    —    *%raxtanam  (sÄ)    'rnanam    Yt
29379:•  j.  han-draxta-  Adj.,  PPfP.:  s.  'drang-.
-- KLN
39152:throng,  n.,  crowd.  —  ME.  throng,  fr.  OE.  prang, geprang,  ‘crowd,  tumult’,  rel.  to  ON.  prong,  Du. drang,  G.  Drang,  Gedrange,  ‘crowd,  throng’, OE. pringan, OS.  thringan,  ON. pryngva,  ‘to  press on,  crowd’,  Du.  dringen^to  push’,  OHG.  dringan, MHG.,  G.  dringen,  ‘to  press  on,  crowd’,  MHG. dringen,  ‘to  press  round  a  prince  at  court’,  Goth. preihan  (for  *prinhan),  ‘to  oppress’,  and  cogn. with  Avestic  draxtanam  (gen.  pi.),  ‘of  those pressed  together’,  Lith.  trenkiu,  trehkti,  ‘to  push, jolt’.
39994:trench,  tr.  and  intr.  v.,  to  cut.  —  MF.  trenchier (F.  trancher)  ‘to  cut’,  fr.  L.  trunedre,  ‘to  cut  off (whence  also  It.  troncare ).  See  truncate  and  cp. trinket.  In  some  senses  the  verb  trench  derives fr.  trench,  n.
39995:trench,  n.,  a  ditch.  —  ME.  trenche,  fr.  MF., trenche  (F.  tranche),  fr.  trenchier.  See  trench,  v., and  cp.  entrench.
...
</persisted-output>
```


## [2026-10-15T02:45:06.733Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^trunk,\\|^truncate,\\|^trepid\\|^trepidation' KLN_1966.txt | cut -c1-900; echo \"-- AHD\"; grep -n -a -i '^trenk\\|^ter-\\|^trep\\|^ter[0-9]\\|^terə' AHD_watkins1985.txt | head; grep -n -a 'TRUNK\\|THRONG\\|TREPID' AHD_watkins1985.txt | cut -c1-300 | head",
 "description": "KLN trunk/trepid and AHD lookups"
}
```


### [2026-10-15T02:45:07.120Z] TOOL RESULT

```
40006:trepidation,  n.,  alarm.  —  L.  trepidatio,  gen.  -onis, ‘state  of  alarm,  agitation,  consternation',  fr. trepiddt-(um),  pp.  stem  of  trepidare,  ‘to  bustle about  anxiously',  fr.  trepidus,  ‘agitated,  alarmed, restless,  anxious,  solicitous'  (see.trepid),  which stands  for  *trepodos,  and  is  cogn.  with  Ol.  trpriih, trpdlah,  ‘hasty’,  Gk.  xpxreEiv,  ‘to  tread  (grapes)’, OPruss.  trapt,  "to  tread’,  Lith.  trepseti,  ‘to  stamp with  one’s  feet’,  OSlav.  trepetati,'\o  tremble".  All these  words  derive  fr.  I.-E.  *tre-p-,  ‘to  shake, tremble’.  See  tremble  and  -ation.
40356:trunk,  n.,  1)  stem  of  a  tree;  2)  body.  —  ME. tronke,  trunke,  fr.  MF.  (=  F.)  tronc,  fr.  L.  tr  un¬ cus,  ‘the  stem,  bole  or  trunk  of  a  tree’,  prop,  ‘the stem  with  the  boughs  lopped  off’,  from  the  ad¬ jective  truncus,  ‘lopped  off,  broken  off;  maim¬ ed,  mutilated’,  which  prob.  stands  for  *troncos, fr.’  I.-E.  base  *trank-,  ‘to  press’,  whence  also Lith.  trenkiu,  trehkti,  ‘to  shake,  jolt’,  trahksmas, ‘turmoil,  tumult’,  W.  trwch,  ‘maimed’;  prob. not  cogn.  with  E.  throng.  Cp.  truncate,  trun¬ cheon,  trunnion,  trench.  Cp.  also  bronco. Derivatives:  trunk,  adj.  and  tr.  v.,  trunk-ed,  adj. trunk,  n.,  proboscis  of  the  elephant.  —  From  a confusion  of  prec.  word  with  trump,  ‘trumpet , which  was  earlier  used  also  in  the  sense  of  ‘pro¬ boscis’,  fr.  F.  trompe,  ‘trumpet;  proboscis’, trunnion
-- AHD
2407:TREPONEME (s)né-, trep-2
1083:thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old 
1096:5. Greek trias, the number three: TRIAD. 6. Greek trikha, in three parts: TRICHOTOMY. 7. Greek compound triérés, galley with three banks of oars, trireme (-érés, oar; see era-'): TRIERARCH. 8. Suffixed form “*tri-to- in Greek tritos, third: TRITIUM; TRITANOPIA. 9. Compound form *tri-pl-, “three
1683:INTRA- en INTRADOS dorsum, en INTRANSIGENT ag- INTREPID  trep-1 INTRINSIC en, sekw-1 INTRO- en INTRODUCE deuk-, en INTROIT el-1, en INTROMIT en, (s)meit(a)- INTRORSE en, wer-3 INTROSPECT en, spek- INTROVERT wer-3 INTRUDE treud- INTUITION teu- INTUMESCE teue- INTUSSUSCEPTION en, kap- INULIN wel-
2406:TRAPUNTO peuk- TRAUMA tera-1 TRAVAIL pag- TRAVE treb- TRAVEL pag- TRAVESTY wes-4 TRAY deru TREACLE ghwer- TREAD der-1 TREADLE der-1 TREASON d6- TREAT tragh- TREBUCHET beu-1 TRECENTO dekm, trei- TREE deru TREFOIL bhel-3 TREMATODE tere-! TREMENDOUS trem- TREMOR trem- TREMULOUS trem- TRENCH tera-2
2412:TROTH deru TROUBLE twer-1 TROUGH deru TROVER trep-2 TROW deru TRUANT tere-1 TRUCE deru TRUCK! dhregh- TRUCKLE dhregh- TRUCULENT tera-2 TRUE deru TRUFFLE teua- TRUNCATE tere-2 TRUNK tera-2 TRUST deru
```


## [2026-10-15T02:45:10.749Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -o '.\\{0,10\\}THRONG [^ ]*\\|TREPID[A-Z]* [^ ]*\\|TRENCHANT [^ ]*' AHD_watkins1985.txt | head; grep -n -a 'trenk\\|trunk\\|trep-1' AHD_watkins1985.txt | cut -c1-600 | head",
 "description": "AHD index for throng, trepid"
}
```


### [2026-10-15T02:45:11.414Z] TOOL RESULT

```
1683:TREPID 
2406:TREPID trep-1
321:yawn, gape: BAY2, BEVEL; ABASH, ABEYANCE. 2. Possibly Vulgar Latin *abbaidre (> Old French (a)baiier), to bay: BAY‘*.] [battuere. To beat. Latin verb of unknown origin. (BATE?), BATTER!, (BATTER’), (BATTERY), BATTLE; ABATE, COMBAT, DEBATE, (RABBET), (REBATE?), (RE- BATO).] bel-. Strong. 1. Suffixed o-grade form *bol-iyo- in Russian bol’shoi, large: BOLSHEVIK. 2. Prefixed form *dé-bel-i- (dé-, privative prefix; see de-), “without strength,” in Latin débilis, weak: DEBILITATE, DEBILITY. [Pok. 2. bel- 96.] bend-. Protruding point. 1. Germanic *pannja-, “struc- ture of stakes,” in Old English 
328:bheidh-. To persuade, compel, confide. 1. Probably Ger- manic *bidan, to await (< “to await trustingly, expect, trust”), in Old English bidan, to wait, stay: BIDE; ABIDE, (ABODE). 2. Latin fidere, to trust, confide, and fidus, faithful: FIANCE, FIDUCIAL, (FIDUCIARY); AFFIANCE, (AFFIANT), (AFFIDAVIT), (CONFIDANT), CONFIDE, (CONFI- DENT), (DEFIANCE), DEFY, DIFFIDENT. 3. Suffixed o-grade form *bhoidh-es- in Latin foedus (stem foeder-), treaty, league: FEDERAL, FEDERATE; CONFEDERATE. 4. Zero-grade form *bhidh- in Latin fidés, faith, trust: FAITH, FEALTY, FIDELITY; INFIDEL, PERFIDY. [Pok. bheid
730:tive masculus, male, manly: MACHO, MALE, MASCULINE; EMASCULATE.] mat-. A kind of tool. Old English mattuc, mattock (prob- ably borrowed from Vulgar Latin *mattea): MATTOCK. [Pok. 2. mat- 700.] mater-. Mother. Based ultimately on the baby-talk form ma-2, with the kinship term suffix -fer-. 1. Germanic *méthar- in Old English mddor, mother: MOTHER}. 2. Latin mater, mother: MATER, MATERNAL, MATERNITY, (MATRICULATE), MATRIX, MATRON; MADREPORE, MATRI- MONY. 3. Greek métér, mother: METRO-; METROPOLIS. 4, Latin mdteriés, materia, tree trunk (< “matrix,” the tree’s source of growth), hence hard ti
938:skep-. Also kep-. Base of words with various technical meanings such as “to cut,” “to scrape,” “to hack.” 1. Germanic *skap- in: a. Old English gesceap (ge-, collective prefix; see kom), form, creation (< “cutting”): SHAPE; b. Old English -scipe, state, condition (collective suffix): -sHIP; c. Dutch -schap, “-ship,” condition (collec- tive suffix): LANDSCAPE. 2. Germanic ablaut variant *skOpo-, “thing cut out,” container, in Middle Dutch and Middle Low German schdépe, bucket for bailing water: scoop. 3. Germanic *skaftaz in Old English sceaft, rod of a spear: SHAFT! 4, Germanic expressive 
997:sta-. To stand; with derivatives meaning “place or thing that is standing.” Contracted from *stag-. I. Basic form *std-. 1. Extended form *stddh- in: a. Germanic *stéd- J6n- in Old English stéda, stallion, studhorse ( < “place for breeding horses”): STEED; b. Germanic *st6d6 in Old English stéd, establishment for breeding horses: sTuD2. 2. Suffixed form *std-lo- in Germanic *stdlaz in: a. Old English st6/, stool: sTooL; b. compound *faldistélaz (see pel-3). 3. Latin stdre (third person singular present subjunctive séet), to stand, with its past participle status (< “sta-to-) and derivative
1013:STICKLE. 3. Suffixed form *stigh-o- in Greek stikhos, row, line, line of verse: STICH; ACROSTIC, CADASTER, DISTICH, HEMISTICH, ORTHOSTICHOUS, STICHOMETRY, STICHO- MYTHIA. III. O-grade form *stoigh-. 1. Suffixed form *stoigh-ri- in Germanic *staigri in Old English stéger, stair, step: STAIR. 2. Greek stoikheion, shadow line, element: STOICHIOMETRY. [Pok. steigh- 1017.] steip-. To stick, compress. 1. Germanic *séifaz in: a. Old English séff, rigid, stiff: stirF; b. Dutch stip, tip, point: STIPPLE. 2. Latin stipes, post, tree trunk: STIPE, STIPES. 3. Suffixed form *steip-d- in Latin stipdre,
1026:Middle Dutch stuyver, stiver: STIVER. II. Extended form *steud-. 1. Nasalized form *stu-n-t- in Germanic *stunt- jan in Old English styntan, to dull: stinT!. 2. Germanic *staut- in: a. Old High German stézan, to push: sTOss; b. Middle Low German and Middle Dutch stéten, to force, akin to the source of Middle English stutten, to stutter: sTUTTER. III. Extended form *steug-. 1. Ger- manic *stukkaz in: a. Old English stocc, tree trunk: stock; b. Old High German stoc (> German Stock), staff: ALPENSTOCK; Cc. Old French estoc, rapier, sword point: TUCK’, 2. Germanic *stukkjam in: a. Old High Ge
1029:strei-. To hiss, buzz. Imitative root. 1. Extended form *strid- in Latin stridére, to make a harsh sound: sTRI- DENT. 2. Extended variant form *trig- in Greek trismos, trigmus, a scream: TRISMUS. [Pok. 3. streig- 1036.] streig-. To stroke, rub, press. I. Basic form *streig-. 1. Germanic *strikan in Old English strican, to stroke: STRIKE. 2. Germanic diminutive *strik-ila- in Old Eng- lish stricel, implement for leveling grain: STRICKLE. 3. Germanic *strikén- in Old English strica, stroke, line: STREAK. II. O-grade form “stroig- in Germanic *straik- in Middle English stroke, stroke: STROKE
1031:b. Greek stranx, drop (< “that which is squeezed out”): STRANGURY. [Pok. strenk-, streng- 1036.]
1083:thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old English therscan, to thresh: (THRASH), THRESH; b. Old English therscold, threscold, sill of a door (over which one treads; second element obscure): THRESHOLD. II. O-grade form *tor(a)-. 1. Greek toreus, a boring tool: TOREUTICS. 2. Suffixed form *tor(e)-mo-, hole, in Germanic *tharma in Old High Ger
```


## [2026-10-15T02:45:14.245Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -o 'tera-2\\. .\\{0,900\\}\\|terə-2\\. .\\{0,900\\}\\|tere-2\\. .\\{0,900\\}' AHD_watkins1985.txt | head -3; grep -n -a -o 'trep-1\\. .\\{0,500\\}' AHD_watkins1985.txt; grep -n -a -o 'THRONG [a-z0-9-]*' AHD_watkins1985.txt",
 "description": "AHD terə-2 and trep-1 entries"
}
```


### [2026-10-15T02:45:14.600Z] TOOL RESULT

```
1083:tera-2. To cross over, pass through, overcome. Variant *trd-, contracted from “traa-. I. Zero-grade form “*tr()-. 1. Germanic suffixed form *thur-ila- in Old English thyr(e)l, thyrel, a hole (< “a boring through”): THRILL; NOSTRIL. 2. Suffixed form *tra-kve in Germanic *thurh in Old English thurh, thuruh, through: THOROUGH, THROUGH. 3. Greek nek-tar, overcoming death ‘(see nek-'). 4, Zero-grade form *tre- and full-grade form *ter(a)- in Sanskrit tirati, tarati, he crosses over: AVATAR. Il. Variant form ‘*trd-. 1. Latin trans, across, over, be- yond, through (perhaps originally the present participle of a verb *trdre, to cross over): TRANS-, TRANSIENT, (TRANSOM). 2. Suffixed form *trd-yo- in Iranian thrdaya-, to protect, in Middle Persian srdyidhan, to protect, in Persian sardi, inn: CARAVANSARY. III. Extended form *tru-. 1. Suffixed form *tru-k- in Latin trux (stem truc-), savage, fierce, grim (
```


## [2026-10-15T02:45:17.158Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -o 'Extended form \\*tru-\\. .\\{0,700\\}' AHD_watkins1985.txt | head -2; grep -n -a -o 'trep-1\\..\\{0,500\\}' AHD_watkins1985.txt; grep -n -a -o '.\\{80\\}THRONG.\\{80\\}' AHD_watkins1985.txt",
 "description": "AHD extended tru- and trep-1"
}
```


### [2026-10-15T02:45:18.259Z] TOOL RESULT

```
1083:Extended form *tru-. 1. Suffixed form *tru-k- in Latin trux (stem truc-), savage, fierce, grim (< “overcoming,” “powerful,” “pene- trating”): TRUCULENT. 2. Suffixed nasalized form *tru-n-k-o- in Latin truncus, deprived of branches or limbs, mutilated, hence trunk (? < “overcome, maimed”): TRENCH, TRUNCATE, TRUNK. [Pok. 5. ter- 1075.] terkw-. To twist. Extension of tera-'. 1. Possible variant form *twjerk- in Germanic *thwerh-, twisted, oblique, in Old Norse thverr, transverse: THWART. 2. Suffixed (caus- ative) o-grade form *tork’-eyo- in Latin torquére, to twist: TORCH, TORMENT, TORQUE}, TORQUE?, TORSADE, TORT, TORTUOUS; CONTORT, DISTORT, EXTORT, NASTUR- TIUM, RETORT!, TORTICOLLIS. [Pok. terk- 1077.] terp-. To s
```


## [2026-10-15T02:45:21.456Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -o 'trep-.\\{0,10\\}To tremble.\\{0,500\\}\\|trep-.\\{0,4\\}To .\\{0,400\\}' AHD_watkins1985.txt | head; grep -c . AHD_watkins1985.txt; grep -n -a -o 'tre[nm]k-.\\{0,300\\}' AHD_watkins1985.txt|head -3",
 "description": "AHD trep root text"
}
```


### [2026-10-15T02:45:22.022Z] TOOL RESULT

```
1032:trep-. To make a noise. Imitative root. Latin strepere, to make noise: OBSTREPEROUS. [Pok. (s)trep- 1037.]
1096:trep-'. To tremble. Possibly related to trem- and tres- through a hypothetical base *ter-. Latin trepidus, agi- tated, alarmed: TREPID; INTREPID. [Pok. 1. trep- 1094.] trep-2. To turn. 1. Greek trepein, to turn: -TROPOUS; APOTROPAIC, TREPONEME. 2. O-grade form *trop- in: a. suffixed form *trop-o- in Greek tropos, a turn, way, manner: TROPE, TROPO-, TROVER; CONTRIVE, (RE- TRIEVE); b. suffixed form *trop-d- in Greek tropé, a turning, change: TROPHY, TROPIC; ENTROPY. [Pok. 2. trep- 1094.] tres-. To tremble. Possibly
2463
1029:trenk-. Tight, narrow. Possible root. 1. O-grade form *stronk- in: a. Germanic “strangi- in Old English streng, string: STRING; b. Germanic *strangaz in Old English strang, strong, powerful, strict: STRONG; c. Germanic *strangithé in Old English strengthu, strength, strict- ness: STRENGTH. 2. Variant *str
1031:trenk-, streng- 1036.]
2319:trenk- STRANGLEs  strenk- STRANGULATE _ strenk- STRANGURY strenk- STRATAGEM ag-, ster-2 STRATH ster-2 STRATOCRACY  ster-2 STRATUS  ster-2 STRAW ster-2 STREAK streig- STREAM sreu- STREET  ster-2 STRENGTH  strenk- STREPTO-  streb(h)- STREPTOMYCES meug-2 STREPTOMYCIN meug-2 STREPTOTHRICIN  thrix STREUSEL ste
```


## [2026-10-15T02:45:24.849Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -o 'THROE.\\{0,200\\}' AHD_watkins1985.txt | head -3; grep -n -a -i 'throng\\|thringan' SKT.txt | head -5; grep -n -a -i '^trunk\\|^trench\\|^trepid' SKT.txt | cut -c1-400 | head",
 "description": "AHD index for throng; Skeat lookups"
}
```


### [2026-10-15T02:45:25.191Z] TOOL RESULT

```
4428:Crowd  (i)>  to  pash,  throng.  (%) <nUM*.   pff.  t-  mdif,   to  {Mih 1 1  Mil  gKrod.  ft  crowd,  throng.
8789:bcmHy.-Glt  ifuXct,  a  throng. j*^f.  like,  same,  together, 8*n3e ;  atiU  IX17.  ttArj,  a .lu  MAiiK,  to  compress,  shut  in. .) irvoTUL^hv      r,\(_)    Englished  from -s  in  feeling  or  con- like;  waeiiy,  aorist of  ««M'x««*'.  u*  kufTer.    See  8*md  And kthoft     And  Ke  Homllr. HOQ)0^   (£.)     AS.    ^Jrt,  a  hone,  (with _     from  d  lo  long  e,  as  iii  d^rin,  bone).
11487:diameter,    the    line    measuring breadth  across  or  thickness  throngh.
11488:-  L.  -  Gk.)     O.  F.  diametrt,  '  a  d Cot.  «-L-  diatne/roi.  ^C\i.  dtafurpot d«d,  throngh :    titrpii^,    to   measure,  b liirpor.  a  measure.
16628:ahoal  (1),  a  multituHe  of  fishes,  a  troop, crowd,  (L.)  Spelt  shoU  in  Spenser;  M.  £. scoU,  a  school,  hence,  a  troop,  throng, crowd  ;  sec  above.  %  Tbe  sailor's  phrase 'a  sckffoi  of  fish'  exhibits  the  same  word; it  aUo  appears  as  scull,  Trotl.  v.  5.  3  3.
20261:Trunk,  stem  of  a  Irec.&c.  (F--Li trofUf  trunk.  —  L.  irufu-utn,  aoc.  of trunk,  stem,  bit  cut  off,  -  L  trmmutt cut  off,   maimed.     Prob    from twist,  hence  to  twist  off;  cf. press.     Her.  trunJk' hose,  i.e Knee* breeches,  breeches  cut  short.
20265:Trunk  (j),  of  an  elephant.    jK.- Comipliun  of  F.  trompt ,  tee  Trxun^  0
21911:Trunk  (2),  of  an  elephant.  Comipted from  F.  trompe.  'a  irump;  also,  the  snowt of  an  elephant;*  Cotgrave.
```


## [2026-10-15T02:45:27.964Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; grep -n -a -i 'raxtan\\|truncus' WLD_Bd1_pages.txt | cut -c1-300 | head; grep -n -a -i 'tṛpr\\|trpr\\|trepidus' WLD_Bd1_pages.txt | cut -c1-300 | head",
 "description": "Grep Walde-Pokorny for trenk, trep"
}
```


### [2026-10-15T02:45:28.365Z] TOOL RESULT

```
38974:m. „truncus"', mhd. ron(r) m. f. „umgestiirzter oder abgehauener Baum‘-
71876:     Av. draxtanqm g. pi. „der zsgedrangten, enggeschlossenen [Schlacht-
71881:  Lat. truncus „(abgestoGener) Baumstamm ohne Aste, Rumpf“, Adj. (nach
71889:niederhauen ££ (verfehlt iiber truncus v. Bradke ZdmG. 40, 352 und Sutter-
71956:         Ygl. Zup. G. 70f. m. Lit., Yf. LEWb.                               u.   truncus    ,
71623:     Ai. trpra-h, trpdla-h „hastig“ (wohl aus „trippelnd ') ; gr. tqolji eco „keltere"
71637:                                                     lat. trepidus ,,trippelnd (vor       ;
71689:III 4 191, Yf. LEWb. 2 u. trepidus , Trautmann Apr. 450, BslWb. 329.
```


## [2026-10-15T02:45:31.444Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:607 2>&1 | head -80",
 "description": "Fetch BQT page 607"
}
```


### [2026-10-15T02:45:32.295Z] TOOL RESULT

```
no scan of BQT covers printed page 607 (see 'scans' in refs_online.json)
```


## [2026-10-15T02:45:34.964Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for L in 62 63 64 65 66; do echo \"== leaf $L\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | grep -a -n 'چابک\\|chābuk\\|čābuk\\|cabuk\\|۶۰' | head -5; done",
 "description": "Locate chabok entry in BQT vol 2"
}
```


### [2026-10-15T02:45:35.742Z] TOOL RESULT

```
== leaf 62
== leaf 63
== leaf 64
== leaf 65
35: ‫چابکی ؟ ‪ -‬بمعنی جلدی وچالاکی‬                      ‫جابانی » با بای فارسی و نای‬
== leaf 66
```


## [2026-10-15T02:45:37.906Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==66' BQT_v2_pages.txt | head -80; grep -a -n 'چابک' BQT_v2_pages.txt | head",
 "description": "Print BQT vol2 leaf 65"
}
```


### [2026-10-15T02:45:38.378Z] TOOL RESULT

```
                                  ‫گفتار ششم‬

     ‫تبجی‬            ‫رب‬
                   ‫واف‬   ‫از کاب پرهان قاطع درحرف جیم فار‬
                       ‫حسی‬
        ‫هبتتی بربيست و دو بیان و محتوی بر ششصد و سیزده‬
                                                 ‫لف‬
                                            ‫کتنوات‬
                                            ‫بیان اول‬

                 ‫در جیم فارسی باالف مشتمل بر نود و هفت لفت و کنات‬

‫قرشت (‪ )۱‬بروزن آبادی ‪ ۰‬بان فطیر نازك باشد‬          ‫‪ #‬چاه مروف است ومشهور بجای‪۰ ۷‬‬
‫اتزپپنند وبرروی تابه‬
                   ‫سدس‬
                     ‫که خمیرآ را با‬                ‫وآن برکی است که از چين وخطا آورند و در‬
                                           ‫پر لد‬    ‫آب جوشانده مانند قهوه خورند‪ ,‬وخاصت آن‬
 ‫چا بك ‪ = ۲‬بصم بای ابجد و سکون‬                     ‫روت شراب رادف عکند ‪ .‬گوبند‬    ‫ضست‬
                                                                                   ‫مار ا‬
                                                                                       ‫بسب‬
    ‫ت‬
    ‫چو‬‫چفافبوك است که جلد‬
                       ‫کاف » مخ‬                    ‫مردم تبت ببب آنکه شراب بيار میخورند‬
‫تازبانه همآمده‬      ‫ع‪-‬‬
                   ‫نی‬ ‫ماشد‬
                         ‫یب‬‫وردف‬
                              ‫ولاك وظ‬
                                    ‫ا‬              ‫وعرب آن صا ‪۴‬‬ ‫ند م‬     ‫رشك‬
                                                                           ‫خت م‬
                                                                              ‫یقیم‬
                                                                                 ‫مرا ب‬
                                                                                     ‫آن‬
                                           ‫ات‬                                         ‫باشد ‪.‬‬

 ‫چابکی ؟ ‪ -‬بمعنی جلدی وچالاکی‬                      ‫جابانی » با بای فارسی و نای‬
                                             ‫‪aaa‬‬



                                                                    ‫‪ :‬و ٿا‪.‬‬   ‫(‪)۱‬چك‬



  ‫٭‪(- €#‬ج بکس » جیم فارسی) حرف هفتم از الفبای فارسی است ‪ .‬در زبان عرب‬
  ‫دارند ‪ .‬وآن‌گاه به ”ش‪٣‬‏ و گاه به « ز >‬     ‫وجودندارد ودر حاب جمل ماد جم آبرا سه مصوب‬

   ‫به «» » ودرتعریب ب«هص» و «ش» تبدبل کردد‬          ‫)ه‬
                                                     ‫گا‬‫ولف‬
                                                         ‫بدل شود ( رك ‪ :‬ص بح دبباچة مۇ‬
                                                              ‫مانند چغانی » صغانی و شفالی ‪.‬‬
          ‫‪ - ۴‬معرب چای «صای» و «شای» امت ‪ .‬رك ‪ :‬چای ‪.‬‬     ‫رك‪ :‬چای ‪.‬‬  ‫‪۱‬‬

   ‫؟ ‪ -‬پهلوی ‪ 60۳86‬ابرانی‌باستان‪ ۵ 26-1۳26-‬ارمنی ‪ ۰‬ع کلقا‪(8‬قابل‌انستاء‬
   ‫نرم » زرنگك) ‏ دیز ارمنیع ‪( ۳60‬شتاب) «ییبرك ‪۲٤٩‬‏ « مسینا ‪ « ۷۳۱۷‬افا ‪ ۱ :۱‬ص‪ ۹۷۲‬؛ ‪۷‬‬
  ‫ص ‪ ۱۸۱‬ورك‪ :‬چابوکه ‪« :‬منافم سفر ‪ ...‬يطناجیفه راست ‪ :‬لضتین بازر گانیکه باوجود‬
       ‫نعمت و مکنت غلامان کونیزکان دارد دلاویز وشاکردان چابك ‪« ».‬کلتان ‪. ۳۱۱-۸۱‬‬
                                   ‫‪ . ۴‬ازچ‪:‬ايك (هم‪ + ).‬ی (مصدری) ‪.‬‬

3677: ‫چابکی ؟ ‪ -‬بمعنی جلدی وچالاکی‬                      ‫جابانی » با بای فارسی و نای‬
18764:‫وحلقه زدن مردمان و جانوران باشد ابستاده با‬                      ‫ویمعنی فتح وفیروزی ‪ -‬و چابکدستی‌وفره وبازی‬
37941:                                                                         ‫چابکی چرب دست ش‬
```


## [2026-10-15T02:45:42.639Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"import json; d=json.load(open('data/verification/sources/refs_online.json'))['BQT']; print(d.get('url')); print(d.get('scans')); print(d.get('cites'))\" | head -30; ls data/verification/sources/refs/ocr/BQT/ | head -50",
 "description": "BQT url, scans, existing OCR cache"
}
```


### [2026-10-15T02:45:43.139Z] TOOL RESULT

```
https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.
[{'volume': '3', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]
page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material
Permissions Size User   Date Modified Name
.rw-r--r--  368k sfmqrb 14 Oct 22:19  0001.png
.rw-r--r--  1.7k sfmqrb 14 Oct 22:19  0001.txt
.rw-r--r--  534k sfmqrb 14 Oct 22:19  0049.png
.rw-r--r--  2.7k sfmqrb 14 Oct 22:19  0049.txt
.rw-r--r--  190k sfmqrb 14 Oct 22:30  0143.jpg
.rw-r--r--   576 sfmqrb 14 Oct 22:30  0143.vision.txt
.rw-r--r--  472k sfmqrb 14 Oct 22:45  0339.jpg
.rw-r--r--   849 sfmqrb 14 Oct 22:45  0339.vision.txt
.rw-r--r--  202k sfmqrb 14 Oct 22:30  0479.jpg
.rw-r--r--   444 sfmqrb 14 Oct 22:30  0479.vision.txt
.rw-r--r--  205k sfmqrb 14 Oct 22:30  0480.jpg
.rw-r--r--   849 sfmqrb 14 Oct 22:30  0480.vision.txt
.rw-r--r--  2.6k sfmqrb 14 Oct 22:19  31.vision.txt
.rw-r--r--  1.5k sfmqrb 14 Oct 22:19  58.vision.txt
.rw-r--r--  1.9k sfmqrb 14 Oct 22:19  70.vision.txt
.rw-r--r--  257k sfmqrb 14 Oct 22:19  71.png
.rw-r--r--  1.5k sfmqrb 14 Oct 22:19  71.vision.txt
.rw-r--r--  1.6k sfmqrb 14 Oct 22:19  72.vision.txt
.rw-r--r--  1.1k sfmqrb 14 Oct 22:19  103.vision.txt
.rw-r--r--  521k sfmqrb 14 Oct 22:19  171.png
.rw-r--r--   806 sfmqrb 14 Oct 22:19  171.vision.txt
.rw-r--r--  527k sfmqrb 14 Oct 22:19  172.png
.rw-r--r--  1.3k sfmqrb 14 Oct 22:19  172.vision.txt
.rw-r--r--  482k sfmqrb 14 Oct 22:19  180.png
.rw-r--r--  1.3k sfmqrb 14 Oct 22:19  180.vision.txt
.rw-r--r--  510k sfmqrb 14 Oct 22:19  181.png
.rw-r--r--  1.2k sfmqrb 14 Oct 22:19  181.vision.txt
.rw-r--r--  538k sfmqrb 14 Oct 22:19  216.png
.rw-r--r--  1.1k sfmqrb 14 Oct 22:19  216.vision.txt
.rw-r--r--  1.1k sfmqrb 14 Oct 22:19  220.vision.txt
.rw-r--r--  512k sfmqrb 14 Oct 22:19  333.png
.rw-r--r--  1.3k sfmqrb 14 Oct 22:19  333.vision.txt
.rw-r--r--  528k sfmqrb 14 Oct 22:19  436.png
.rw-r--r--  1.4k sfmqrb 14 Oct 22:19  436.vision.txt
.rw-r--r--   865 sfmqrb 14 Oct 22:19  460.vision.txt
.rw-r--r--  2.0k sfmqrb 14 Oct 22:19  509.vision.txt
.rw-r--r--  669k sfmqrb 14 Oct 22:19  733.png
.rw-r--r--  1.2k sfmqrb 14 Oct 22:19  733.vision.txt
.rw-r--r--  1.5k sfmqrb 14 Oct 22:19  794.vision.txt
.rw-r--r--  727k sfmqrb 14 Oct 22:19  829.png
.rw-r--r--   981 sfmqrb 14 Oct 22:19  829.vision.txt
.rw-r--r--  625k sfmqrb 14 Oct 22:19  902.png
.rw-r--r--  1.7k sfmqrb 14 Oct 22:19  902.vision.txt
.rw-r--r--  620k sfmqrb 14 Oct 22:19  1024.png
.rw-r--r--  1.7k sfmqrb 14 Oct 22:19  1024.vision.txt
.rw-r--r--  1.3k sfmqrb 14 Oct 22:19  1074.vision.txt
.rw-r--r--  584k sfmqrb 14 Oct 22:19  1085.png
.rw-r--r--  1.1k sfmqrb 14 Oct 22:19  1085.vision.txt
.rw-r--r--  330k sfmqrb 14 Oct 22:19  1092.jpg
```


## [2026-10-15T02:45:47.507Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -a -n 'سبك\\|سبک' BQT_v2_pages.txt | head; awk 'BEGIN{RS=\"\\f\"} {if ($0 ~ /سبك ‪|سبک ‪|سبك =|سبک =/) print NR-1}' BQT_v2_pages.txt | head",
 "description": "Locate sabok entry in BQT vol 2"
}
```


### [2026-10-15T02:45:48.193Z] TOOL RESULT

```
3464:‫بدادی ب‪-‬هست جهان یهلوان ( سام )‪.‬‬                             ‫کرفتش سبك دست شاه جهان (فربدون)‬
6488:          ‫بشهربار رساند سبك چکامشمن ‪.‬‬              ‫چکوردد آکه خواجه زحال امه(زکارامثامن‬
8247:                                         ‫عربی است ‪۸‬‬        ‫حر دون ‪ °‬سبکر اول وسکون ثالی‬
10507:                                                                                 ‫«سبك شناسی‪ .‬بہار ج ‪۲‬ص ‪: ۳۳۱‬‬
12461:  ‫گیلکی بنوعی‌شیربنی که‬             ‫‪2‬‬                  ‫«ترجمة تاریخ طبری بنقل سبك شناسی ج ‪ ۲‬ص ‪ ۹-۰۱‬؟‪.‬‬
16261:      ‫‪ ۴‬کیلکی ‪( 2100۱80‬کسبکه دربازی تقلب کند ‪.‬جر‬                                           ‫رك‪ :‬داغنه‪۰ ‎‬‬   ‫‪۳ ١‬‬
17154:  ‫کاری گفتن » یا پس انداختن‌کار » « سبك شناسیج ‪ ۲‬ص ‪ * 6۱۲‬ونيز بمعنی چشم پوشیدن‪,‬بدور‬
22588:‫بل د بکراول وسکون بای ابجد ‪۴‬‬                                 ‫* ذاقنو بداس ‪ ۱‬سبکرفان ونون‬
26403: ‫ریحان تاتادی سبکرنون‪ .‬بمعنی‬
32044:                                                                              ‫اس‬‫‪ ۷‬کجسبکه‬
545
644
```


## [2026-10-15T02:45:50.606Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==546' BQT_v2_pages.txt | grep -a -n -B3 -A12 'سبك\\|سبک\\|sapuk\\|sabuk' | head -80",
 "description": "Print sabok entry in BQT leaf 545"
}
```


### [2026-10-15T02:45:51.329Z] TOOL RESULT

```
18-                             ‫و زود خىز باشد‪.‬‬          ‫که بش ازکار کردن بمزدور دهند ‪ - ۷‬وضم‌اول‬
19-‫سبگدست ‪ -‬کنابه ازشتاب و جلدی‬                                            ‫دراز قد کوشیده بالا گرواشد‪.‬‬
20-‫باشد در کارهابی کهبادست کنند ‪ -‬وشخص یکه‬
21:                                                      ‫سبك ‪ -‬بفتح اول وضم الیو سکون‬
22-          ‫درکارها سرعت و جلدی بکار برد ® ‪.‬‬            ‫»عروف است که در مقابل سنگن باشد‬
23-                                                                                    ‫کاف م‬
24: ‫‪-‬برنتشم‌تر‪.‬ایبمعتیسبکیای‬
25-                        ‫سیگر و ف‬                       ‫وابه‌ازمردم بی‌وفارونی‌ته‌بود ‪ -‬وبمعنی‌چست‬
26-                                                                                                ‫‪ -‬کن‬
27- ‫اکسرتیکهزپای و تند و نیز براه رونده وجله‬             ‫جرد و بی‬
28-                                                             ‫و شوتاهب‌‪-‬‬              ‫یل‬
29-                                                                                      ‫عكم‪۴‬ج و‬
30-                                                                                            ‫تچاي‬
31-                                                                                               ‫و‬
32-                        ‫رفتار وشتاب رو باشد ‪.‬‬         ‫ولکر ثافی‌بمعنی‬
33-                                                                    ‫آمده است ‪ -‬وضم او‬
34-                                                                                    ‫تعلق ح‬
35- ‫سبگکروح کدنابه از مردم بی‌تکلف‬                        ‫ست وسستی‌باشد ‪ -‬وبکسراول وثالی؛پرنده‌است‬
36-      ‫ایشد‪.‬‬
--
55-          ‫ب‪-‬ب‬
56-            ‫س‪-‬و‬ ‫وقار وشتاب زده باشد ‪۷‬‬                 ‫سپکاد ‪-‬باکاف بر وزن بنداد »بمعنی‬
57-
58:  ‫‪ - ۴‬پهلوی ‪( 610035‬سبك ‪,‬چابك) ‪ .‬پارسی باستان‬                    ‫‪۱‬‬   ‫*بعاله»‬   ‫ظ‪.‬عصحف‬    ‫‪۱‬‬
59-
60-
61-  ‫‪5۳‬‬      ‫در ساسکریت ‪ , 2۲۳۳ -‬افغالی‪‎‬‬            ‫‪ = ٥ ۷02 - ak‬ابرانی باستان ‪۵ )010427-0‬‬
62-  ‫یی« هکر ‪۰ ۰۲۰۱‬یکلیک ‪500‬انع اهمیدرد( )‪ , >5۱0000‬یدنزیرف الأع ‪‎ , 80۷‬ییرب )‪. 85۷0‬‬
63-  ‫‪‎‬یب‌هخرس ‪.„savik‬‬   ‫‪‎‬یکتا ‪۰ saevûk‬‬           ‫‪subuk‬‬      ‫‪۰۲۹۲‬ص‪ ۱‬؛ ‪‎‬یلانمس‬       ‫‪4.‬‬      ‫یزنطن ‪۷۳۵‬‬
64-                                     ‫یدرگسا ‪ » 51‬ىرازرىمېش ‪. « 58۷6‬ك‪‎ 4‬س‪. ۱۹۲ ۲‬‬
65:            ‫‪.‬‬   ‫سبك وار هبرسجتایایمت‬                           ‫مت‬
66-                                                                ‫یکار‬
67-                                                                   ‫اتا‬
68-                                                                     ‫مباش‬
69-                                                                        ‫ربك‬
70-                                                                          ‫ف‪ -‬س‬
71-                                                                             ‫‪۴‬‬
72-  ‫| منطفی ‪ « .‬لقت فر ‪. > ۵۰۳‬‬            ‫‪۰‬‬   ‫‪ :‬سیکاد‬   ‫توت جکاد (ه‪ -‬م‪ ).‬ورك‬       ‫سکاد‬   ‫مصحف‬      ‫‪۴‬‬
73-
74:           ‫عروی صبح را زیور بهم بت ‪.‬‬                  ‫ازمشرق سبکدست‬       ‫بر آمد دزدی‬   ‫‪- ۵‬‬
75-
76-  ‫‪.‬‬    ‫«‪۳۸۰‬‬
77-          ‫نه‬‫یوی‬
78-              ‫جنج‬
79-                ‫ن ک‬
80-                  ‫کامی‬
81-                     ‫نظ‬
82:          ‫(ه‪.‬م‪ ).‬لغة بمعنى سرسيك » مردخفیف وسبك ‪.‬‬              ‫ر)‬
83-                                                                ‫سار‬
84-                                                                  ‫(ك ‪+‬‬
85-                                                                     ‫‪ - ۱‬از ‪ :‬سب‬
86-                                                            ‫‪ - ۷‬سکار شادی‌لمادد تضت‬
87-  ‫فردوسی طوسی‪«.‬فرهنکه فظام» ‪.‬‬
88-
```


## [2026-10-15T02:45:54.866Z] TOOL CALL #23: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl512; cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl512; for L in 65 545; do curl -sL -o bqt512_n$L.jpg \"https://archive.org/download/borhan-ghate-v2/page/n${L}_w1400.jpg\"; done; file *",
 "description": "Download BQT vol2 leaf images"
}
```


### [2026-10-15T02:46:00.854Z] TOOL RESULT

```
bqt512_n545.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2569x3970, components 1
bqt512_n65.jpg:  JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2569x3970, components 1
```


## [2026-10-15T02:46:04.474Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl512; magick bqt512_n65.jpg -crop 2569x1300+0+2500 -resize 60% c65.jpg && magick bqt512_n545.jpg -crop 2569x1500+0+2300 -resize 60% c545.jpg; magick bqt512_n545.jpg -crop 2569x700+0+0 -resize 50% h545.jpg; ls",
 "description": "Crop footnote regions"
}
```


### [2026-10-15T02:46:05.466Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:46:07.491Z] TOOL CALL #25: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl512/c65.jpg"
}
```


### [2026-10-15T02:46:07.509Z] TOOL RESULT

```

```


## [2026-10-15T02:46:08.123Z] TOOL CALL #26: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl512/c545.jpg"
}
```


### [2026-10-15T02:46:08.154Z] TOOL RESULT

```

```


## [2026-10-15T02:46:15.036Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl512; magick bqt512_n65.jpg -crop 2569x300+0+0 -resize 40% t65.jpg; magick bqt512_n545.jpg -crop 2569x300+0+0 -resize 40% t545.jpg; magick t65.jpg t545.jpg -append t512.jpg",
 "description": "Crop page headers"
}
```


## [2026-10-15T02:46:16.257Z] TOOL CALL #28: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl512/t512.jpg"
}
```


### [2026-10-15T02:46:16.856Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-10-15T02:46:16.894Z] TOOL RESULT

```

```


## [2026-10-15T02:46:19.846Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; ls | grep -E '^(0?607|1083)\\.' ; cat 1085.vision.txt | head -5",
 "description": "Check existing BQT vision files"
}
```


### [2026-10-15T02:46:20.547Z] TOOL RESULT

```
[Borhan-e Qate', ed. Mo'in, printed p. 1085 (running head «-۱۰۸۵-») = archive.org
borhan-ghate-v2 leaf n547; read from the page image by the verification agent,
page 469 task, 2026-09-13]

Headword: «سپار = به ضم اول بر وزن دچار، آهنِ جفت را گویند و آن آهنی باشد سرتیز که زمین
```


## [2026-10-15T02:46:31.889Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; D=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl512; cp $D/c65.jpg 607.jpg; cp $D/c545.jpg 1083.jpg\ncat > 607.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed p. 607 = archive.org borhan-ghate-v2 leaf n65\n(offset leaf+542, consistent with leaf n547 = p.1085); footnote area read from the page image\nby the verification agent, page 512 task, 2026-10-14]\n\nHeadword (OCR + image): «چابك = بضم بای ابجد و سکون کاف، معروف است که جلد و چالاک باشد ...»\nFootnote ۳ (Mo'in):\n«۳ ـ پهلوی câpûk، ایرانی‌باستان câpu-ka- * ارمنی، ع capuk (قابل‌انحناء، نرم، زرنگ)، نیز ارمنی ع cep (شتاب) «نیبرگ ۴۲» «مینا ۱۳۲» «اسفا ۱: ۱ ص۲۷۹؛ ۲ ص ۱۸۶» ورك: چابوك: «منافع سفر ... پنج طایفه راست: نخستین بازرگانی که با وجود نعمت و مکنت غلامان و کنیزکان دارد دلاویز و شاگردان چابك.» «گلستان ۱۱۳-۱۴».»\nFootnote ۴: «از: چابك (ه.م.) + ی (مصدری).»\nEOF\ncat > 1083.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, printed p. 1083 = archive.org borhan-ghate-v2 leaf n545\n(leaf n547 = p.1085 per running head); footnote area read from the page image by the\nverification agent, page 512 task, 2026-10-14]\n\nHeadword (OCR): «سبك ـ بفتح اول و ضم ثانی و سکون کاف، معروف است که در مقابل سنگین باشد ... و بمعنی چست و چالاک ...»\nFootnote ۲ (Mo'in):\n«۲ ـ پهلوی sapûk (سبك، چابك). پارسی باستان çapu-ka* = ایرانی باستان thrapu-* در سانسکریت trpra، افغانی spuk «نیبرگ ۲۰۱»، گیلکی sobuk (subûk دردیه‌ها)، فریزندی sovuk، یرنی sävok، نطنزی sävuk «ک. ۱ ص۲۹۲»؛ سمنانی subuk، سنگسری saevúk، سرخه‌یی savík، لاسگردی söúk، شهمیرزادی savék «ک. ۲ ص ۱۹۲».»\nFootnote ۳: «سبك باش تا کار فرمایمت / سبك وار هر جای بستایمت.»\nEOF\nls 607* 1083*",
 "description": "Save BQT vision transcriptions"
}
```


### [2026-10-15T02:46:34.976Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   86k sfmqrb 14 Oct 22:46  607.jpg
.rw-r--r--   968 sfmqrb 14 Oct 22:46  607.vision.txt
.rw-r--r--  112k sfmqrb 14 Oct 22:46  1083.jpg
.rw-r--r--   986 sfmqrb 14 Oct 22:46  1083.vision.txt
```


## [2026-10-15T02:46:41.692Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -i 'sabuk\\|sapuk\\|čābuk\\|cābuk\\|cabuk\\|capuk' PHD.txt PHD_mackenzie.txt | head; echo \"-- NYB\"; grep -n -a -i 'sapuk\\|sapuk\\|capuk\\|čāpuk\\|cāpuk\\|spwk\\|cpwk' NYB_vol2_glossary.txt | head; echo \"-- HRN\"; grep -n -a -i 'sabuk\\|cabuk\\|čābuk\\|cäbuk\\|sapuk\\|thrapu\\|Orapu' HRN.txt | head; echo \"-- HUB\"; grep -n -a -i 'sabuk\\|cabuk\\|čābuk\\|sapuk\\|capuk' HUB.txt | head",
 "description": "Grep PHD, NYB, HRN, HUB for sabuk/chabuk"
}
```


### [2026-10-15T02:46:42.190Z] TOOL RESULT

```
PHD.txt:296:čābuk [c’Swk! | N ~] agile, nimble; excellent. ~th: agility. čādur [c?twl | N ~] sheet, veil. éagad [ck*t! | (N ¿ahad), J ¿eyad] peak, summit. сабаг [cki] wife (of the second degree). саһ [ол | N ~] pit, well. čahār [ALBA < A?rb‘; ch?l | M с, N ~] four. ~dah [cl’ldh | N ~] fourteen. ~-рау [cb Ip d | N ~ > čārwā] quadruped. čakēk [ckwk | N ~, cakáwak] lark. čakuč [cktwc | N čakuš] hammer. čambar [cmbl | N ~] circle, hoop. čamišn [cmšn! | M cmbyšn (?)] urination; lavatory. ` бапа [спа | = M, N ~] how many, much?; so many, much; some, a few. ~ih: amount, quantity. čandal [cndl | N ~] sandalwood. čandīdan, čand- [cnd-ytn! | (M cn-ystn)] tremble, quake. ~išn: trembling, movement. čang [eng | M bung, N ~] harp. ~-sray [-sPd] harpist. са�� [c7] = Carag. багар [clk' | M erg] pasture, grazing; flock. čārag [c?]k! | N ~a] means, remedy. ~garih [-glyh] ability, savoir faire. Carb [с/р | P crb, N ~] mild, gentle; fatty, oily. ~ih: gentleness; fattiness. ~išn [-sn'] fat, oil. ~і&потапа [-šrwmnd) oleaginous. Carm [с/т | M crm, N ~] skin, hide, leather. čārūģ [c wk! | N čārū] lime, mortar. „ēn [-yn!] limy. Carz [сіх | N ~] bustard. čāšīdan [c'$-ytn!] = čāštan. čašm [A YNE < A ‘ynh; ст | = M, N ~] eye. léaSmag [cfmk! | М cšmg, N ~a] spring, source. tčašmaģ [cfmk!] renowned. čašmaģāh [cšmk?s | M csmg’h] obvious, public, notorious. ~ih: notoriety, condemnation. čašm-arešk [cém ?ly$k!] envious. ^h: envy. čašm-dīd [cšm dyt'] visible, obvious. čāšnīg [c nyk! | M спус, N čāšnī] taste.
PHD.txt:562:sabuk [spwk! | N ~] light, easy. sabz [spz, sbz | N —] green, fresh. sad [roo | M sd, N ~] hundred. Sadwés [stwys | M sdwys] a star (Fomalhaut ?). ваб [KLBA < A klb | N ~] dog. Zeag [sk!] stone. sag [PR | P g] number. sagén [skyn! | M sygyn] stony. sagr [sg] | N sēr] sated, satiate. «ЛЬ: satiety. sahig [shyk' | M shyg, N sahi] worthy. ~th : worthiness. sahistan, sah- [MDMEN-stn' = A mdmh, V dmh | (M shyd, s‘y-)] seem; seem proper. ~išn: satisfaction. sahm [skm | = M, N ~] terror. ~gin [-k(y)n! | N —gin] terrible. ~genith : terribleness. sahög [shwk'] hare. sāk [s | (N sdw)] tribute. sal [SN T < A fnt | (M sr), N <] year. -sálag [SN TA, oli | N -sala] . . . -years-old. ~ih: age (of... years). salar [srd?] | M ffr, s’r’r, N ~] leader, master. ^h : authority. salwar Leikofl perennial. sāmān [?mn! | = M, N ~] limit, boundary. —Óómand [-’wmnd | M -wmnd] bounded. samór [smzl | N ~] sable (marten). sàn [?л! | N ~] kind, manner.
PHD.txt:753:ageless azarman. aggression hénih. aggressive mustabarmand. agile čābuk.
PHD.txt:754:agility čābukīh.
PHD.txt:1072:brave čēr, dilēr, marčābuk, mardān- ag, nēw.
PHD.txt:1073:bravery čērīh, gurdih, marcabukih, mardānagīh.
PHD.txt:1729:easy asan, sabuk, xwār.
PHD.txt:1827:excellent čābuk, pāhlom, pāšom.
PHD.txt:2620:light (a.) rēšn; (weight) sabuk, xwār.
PHD.txt:2919:nimble čābuk, šēbāg.
-- NYB
3391:sapük [spwk'] light, brisk; unsteady, shallow, comp. ~-tar 90%, — < OP *capu-ka- < Olr *0rapu-ka-, from IE *trep-, Gr retro ‘to turn’, Lat trepidus
3394:sapukiha swiftly, rapidly 274. 11922,
3476:spannik  [spn'k]. ménoi 65°, spénak [spyn’k] ménoi 106° spénài [spyn’y] ménói 10215-17, 10312: the Effective, Good Spirit, the creative power of the world, as opposed to ganāk menör (g.v.). — The Phl rendering of Av. (1137 sqq.) sponta- mainyu-; spwk may be spannak < *spanta- enlarged with the suff. -āk and with -nt- > -nn-, or spanäk with the same suff. from the abstr. (1612) spanah-; spénük with the same suff.
-- HRN
-- HUB
6259:phi. sr(u)p; sabuk 'leicht' = paz. sabuk Min. 61. 180 — 181,
8760:sabuk leicht', afgh. spuk^ paz. saiuk Min. Gl. 180,
8761:phi. sapuk Phi. Min. 63, Z. 15, Yatk. i. Zar. 65; tanuk
```


## [2026-10-15T02:46:46.241Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3388,3393p NYB_vol2_glossary.txt; grep -n -a -i \"c'pwk\\|cʾpwk\\|capuk\\|câpûk\\|cāpūk\" NYB_vol2_glossary.txt | head -5; sed -n 8755,8765p HUB.txt; grep -n -a -i 'subuk\\|sapuk\\|ćabuk\\|cäbuk\\|cābuk' HRN.txt | head",
 "description": "More NYB, HUB, HRN context"
}
```


### [2026-10-15T02:46:46.623Z] TOOL RESULT

```
simanak [s’m’nk'] limit 10415, — MPrs s’m’nwmnd ‘limited’, ’s®’m’n ‘unlimited’ NP saman; Arm. lw. (Prth) sahman.
sāmānihā [s’m’nyh’] adv.: tuvān ~ in proportion to their powers, or capacity 8115, — sāmān (v. the preceding w.) also ‘measure, proportion’. Paz. tuq sämä- naihä, Skr. v. šakta-anurupatayč.
Samarkand [smlknd] 113".
sapük [spwk'] light, brisk; unsteady, shallow, comp. ~-tar 90%, — < OP *capu-ka- < Olr *0rapu-ka-, from IE *trep-, Gr retro ‘to turn’, Lat trepidus
sargun
‘agitated, anxious’, cf Skr ¢rpra- id.; Paz. NP sabuk.
1100:cāpūk [c'pwk'], comp. ~-tar, quick, brisk 8%; busy, active 178. — NP cābuk. cāpūkēh quickness of wit, nimble wit 223, 42, 141°. 1518,
Hinterbeinen = np. jufta; kddak 'Kind', phi. kotak, arm.
kotak (oben p. 89); r^ak 'Kind' = fihl. retak (siehe p. 244)?,
pusak = pOsak 'Katze' (dial.) H. 322 ? Dieses k bleibt auch
im Plural: hindtwakariy Vullers Wb. II, 1478.
b) in dem Suffix uk:
sabuk leicht', afgh. spuk^ paz. saiuk Min. Gl. 180,
phi. sapuk Phi. Min. 63, Z. 15, Yatk. i. Zar. 65; tanuk
*diinn, zart, fein, osset. fdndg^ skr. tanuka' Miinn'; cdhuk
schnell, flink, behend, geschickt', arm. JapwA?; nSewi zart,
zierlich, fein' zu ndz 'Zierlichkeit' u. s. w. ; tanhah u. s. w.
'tympanum*, lies tunbuk? — arm. fmbuk (= phi. Hunbuk)
```


## [2026-10-15T02:46:49.147Z] TOOL CALL #33: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-15T02:46:49.157Z] TOOL RESULT

```

```


## [2026-10-15T02:46:51.336Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/سبک",
 "prompt": "Give the full Persian etymology section(s) for the word meaning 'light (weight)', verbatim."
}
```


## [2026-10-15T02:46:51.753Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/چابک",
 "prompt": "Give the full Persian etymology section verbatim."
}
```


## [2026-10-15T02:46:52.363Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/truncus",
 "prompt": "Give the Latin etymology section verbatim."
}
```


## [2026-10-15T02:46:53.524Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/throng",
 "prompt": "Give the English etymology section(s) verbatim, including the Proto-Germanic and PIE forms."
}
```


## [2026-10-15T02:46:53.610Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/trepidus",
 "prompt": "Give the Latin etymology section verbatim."
}
```


### [2026-10-15T02:46:55.513Z] TOOL RESULT

```
# Latin Etymology Section

From Proto-Indo-European *\*trep-* ("to tremble") + *-idus*. Cognate with Russian *трепа́ть* (trepátʹ).
```


### [2026-10-15T02:46:57.622Z] TOOL RESULT

```
# Latin Etymology Section

The Latin etymology section states:

"Unknown origin,[[1]](#cite_note-1) but possibly from Proto-Indo-European *[\*twerḱ-](/wiki/Reconstruction:Proto-Indo-European/twer%E1%B8%B1- "Reconstruction:Proto-Indo-European/twerḱ-")* ("to cut")."

It further notes cognates with Ancient Greek *σάρξ* (sárx), Old Irish *tru* and *troich* ("fated to die"), Latin *trux*, and Proto-Slavic *\*strǫkъ*.
```


### [2026-10-15T02:46:58.771Z] TOOL RESULT

```
# Persian Etymology for "Light (Weight)"

The word سبک (sabuk/sabok) meaning "light" in weight has the following etymology:

**Etymology 2** states it derives "From [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") \[Book Pahlavi needed\] (spwk' /⁠sabuk⁠/, "light, easy"), from [Proto-Iranian](https://en.wikipedia.org/wiki/Proto-Iranian_language "w:Proto-Iranian language")" sources, ultimately tracing to Proto-Indo-European *trep- ("to tremble").

The entry notes cognates include "Latin _[trepidus](/wiki/trepidus#Latin "trepidus")_ ("nervous, perilous") and [Russian](https://en.wikipedia.org/wiki/Russian_language "w:Russian language") _[трепа́ть](/wiki/%D1%82%D1%80%D0%B5%D0%BF%D0%B0%D1%82%D1%8C#Russian "трепать")_" along with Iranian borrowings in Syriac, Georgian, and Laz languages.
```


### [2026-10-15T02:46:59.181Z] TOOL RESULT

```
# Etymology of "Throng"

The etymology section states that "throng" comes "From Middle English _throng_, _thrang_, from Old English _þrang_, _ġeþrang_ ("crowd, press, tumult"), from Proto-Germanic _\*þrangwą_, _\*þrangwō_ ("throng"), from _\*þrangwaz_ ("pressing, narrow"), from _\*þrinhwaną_ ("to press, to push; to force"), from Proto-Indo-European _\*trenkʷ-_ ("to beat; pound; hew; press")."

The document notes cognates in Dutch (_drang_) and German (_Drang_), and compares the German word _Gedränge_ ("throng").
```


### [2026-10-15T02:46:59.496Z] TOOL RESULT

```
# Persian Etymology Section

The etymology states that چابک comes "From [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") \[Book Pahlavi needed\] (cʾp̄wk' /⁠čābuk⁠/, "agile, nimble; excellent")," with a suffix from an unattested root borrowed as "Old Armenian _[ճեպ](/w/index.php?title=%D5%B3%D5%A5%D5%BA&action=edit&redlink=1 "ճեպ (page does not exist)")_ (čep, "haste")."

The entry notes the word is "Akin to" related terms in Old Armenian _čapuk_, Old Georgian forms, and describes these as "Middle Iranian borrowings."
```


## [2026-10-15T02:47:02.910Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þrinhaną",
 "prompt": "Give the etymology (PIE root and any cognates, esp. Avestan, Lithuanian) and descendants (Old English, Gothic, OHG) verbatim."
}
```


## [2026-10-15T02:47:03.521Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/trench",
 "prompt": "Give the etymology of trench verbatim."
}
```


## [2026-10-15T02:47:04.104Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/trunk",
 "prompt": "Give the etymology of trunk (n.) verbatim, including the Latin truncus origin and PIE root."
}
```


## [2026-10-15T02:47:04.664Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/तृप्र",
 "prompt": "Give the Sanskrit etymology and meaning verbatim."
}
```


### [2026-10-15T02:47:05.187Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:47:05.192Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:47:05.200Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-15T02:47:05.205Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-10-15T02:47:07.282Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/trench",
 "prompt": "Give the English etymology verbatim (Old French trenchier, Vulgar Latin, Latin truncare)."
}
```


## [2026-10-15T02:47:07.863Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þrinhwaną",
 "prompt": "Give the etymology (PIE root, cognates incl. Avestan, Lithuanian) and descendants verbatim."
}
```


## [2026-10-15T02:47:08.611Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/trunk",
 "prompt": "Give the English etymology for trunk (tree stem/torso) verbatim."
}
```


### [2026-10-15T02:47:13.188Z] TOOL RESULT

```
# Etymology and Descendants of Proto-Germanic *þrinhwaną

**Etymology:**
The word derives from "Proto-Indo-European *trenkʷ- ('to beat, hew, press')."

**Descendants:**
The word produced extensive reflexes across Germanic languages, including Old English þringan, Old Saxon thringan, Old Dutch thringan, Old High German dringan, and Old Norse þryngva. Modern descendants encompass German dringen, Dutch dringen, Icelandic þryngva, and English thring. Additional modern forms include Luxembourgish dréngen, Yiddish דרינגען (dringen), and Afrikaans dring.

**Note:** The webpage does not provide Avestan or Lithuanian cognates, only the PIE root and Germanic language family descendants.
```


### [2026-10-15T02:47:13.323Z] TOOL RESULT

```
# English Etymology of "Trench"

Based on the Wiktionary content provided, here is the etymology:

The word "trench" was "Borrowed into Middle English from Old French _trenche_." The entry notes it is a "Doublet of _tranche_ and _traunch_" and lists a "Possible doublet of English: truncate."

The etymological chain suggests connections to Old French and ultimately to Latin roots related to cutting or dividing, though the specific Vulgar Latin or classical Latin etymons are not explicitly detailed in this dictionary entry.
```


### [2026-10-15T02:47:18.370Z] TOOL RESULT

```
# Etymology of "Trunk" (Tree Stem/Torso)

According to the Wiktionary entry, the etymology is:

"From Middle English _tronke_, _trunke_, from Old French _tronc_ ("alms box, tree trunk, headless body"), from Latin _truncus_ ("a stock, lopped tree trunk"), from _truncus_ ("cut off, maimed, mutilated")."

The entry also notes that for the verb form, one should "compare French _tronquer_" and see the entry for "truncate." Additionally, it identifies "trunk" as a doublet of both "_truncus_" and "_tronk_" in English.

[WebFetch note: this page's text is 113869 characters long and the answer above covers only characters 0 to 100000; the final 13869 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


## [2026-10-15T02:47:24.676Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F=tools/fetch_source.py\npython3 $F 'https://en.wiktionary.org/wiki/سبک' --note 'page 512, root Trep 1: sabuk < MP sabuk < PIr *θrapu- < PIE *trep-' \npython3 $F 'https://en.wiktionary.org/wiki/چابک' --note 'page 512, root Trep 1: čābuk < MP čābuk, root akin to Arm. čep haste; no *trep- link'\npython3 $F 'https://en.wiktionary.org/wiki/truncus' --note 'page 512, root Trenk: Latin truncus, unknown origin / *twerḱ-'\npython3 $F 'https://en.wiktionary.org/wiki/throng' --note 'page 512, root Trenk: throng < OE geþrang < PGmc *þrinhwaną < PIE *trenkʷ-'\npython3 $F 'https://en.wiktionary.org/wiki/trepidus' --note 'page 512, root Trep 1: trepidus < PIE *trep-'\npython3 $F 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þrinhwaną' --note 'page 512, root Trenk: OE þringan, OHG dringan < PIE *trenkʷ-'\npython3 $F 'https://en.wiktionary.org/wiki/trench' --note 'page 512, root Trenk: trench < OF trenche, possible doublet of truncate'\npython3 $F 'https://en.wiktionary.org/wiki/trunk' --note 'page 512, root Trenk: trunk < OF tronc < Latin truncus'",
 "description": "Archive fetched web sources"
}
```


### [2026-10-15T02:47:27.420Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6c2f07d70307fe34.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/aa71da26f7cdd02a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ae75bf9be5f0ec4c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0d3f8e0b5a74d2a6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/78153874ea5603b0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b7bbdd7a53881c71.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6e645bb0732e356c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/993bcf2fda364439.txt
```


## [2026-10-15T02:47:29.933Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -a -n -i -A3 'etymology' aa71da26f7cdd02a.txt | head -20; grep -a -n -i 'trep\\|thrap\\|θrap\\|Proto-Iranian' 6c2f07d70307fe34.txt | head",
 "description": "Inspect archived Wiktionary etymologies"
}
```


### [2026-10-15T02:47:30.252Z] TOOL RESULT

```
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
--
94: Etymology 
95-
96- 2.2 
97- Noun 
--
177: Etymology
178- [ edit ] 
179-
180- From Middle Persian [Book Pahlavi needed] ( cʾp̄wk' /⁠čābuk⁠/ , “ agile, nimble; excellent ” ) , Northern Luri چںڤوک ( çəvok ) , suffixed from an unattested root borrowed as Old Armenian ճեպ ( čep , “ haste ” ) . Akin to Old Armenian ճապուկ ( čapuk ) , Old Georgian ჭაპუკი ( č̣aṗuḳi ) , ჭაბუკი ( č̣abuḳi ) , Middle Iranian borrowings.
--
307: Etymology
308- [ edit ] 
309-
310- Borrowed from Classical Persian چابک ( čābuk ) .
--
261: From Middle Persian [Book Pahlavi needed] ( spwk' /⁠sabuk⁠/ , “ light, easy ” ) , from Proto-Iranian *θrapuka- , from Proto-Iranian *θrap- ( “ to be unsteady ” ) , Northern Luri سۏوک ( söwk ) , perhaps from Proto-Indo-European *trep- ( “ to tremble ” ) ; if so, then cognate with Latin trepidus ( “ nervous, perilous ” ) and Russian трепа́ть ( trepátʹ , “ to scutch; to flutter ” ) . [ 2 ] Akin to the Iranian borrowings: Classical Syriac ܐܣܦܘܟܐ ( espukā , “ post-man, courier ” ) , Old Georgian სუბუქი ( subuki ) , მსუბუქი ( msubuki ) , Laz სუბუქი ( subuki , “ lightweight ” ) .
350: Persian terms inherited from Proto-Iranian 
351: Persian terms derived from Proto-Iranian
```


## [2026-10-15T02:47:34.908Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -a -i 'trenk\\|trepid\\|truncus' IEC.txt | cut -c1-300 | head; grep -n -a -i 'tṛpr\\|trpra\\|trprah' KLN_1966.txt | cut -c1-200 | head -3; grep -n -a '^trepid,' KLN_1966.txt | cut -c1-300; grep -n -a '^truncate,' KLN_1966.txt | cut -c1-300",
 "description": "Grep Mann IEC and KLN more"
}
```


### [2026-10-15T02:47:35.353Z] TOOL RESULT

```
18883:(treik- ‘force, crush’. Cf. trenk- and trik-. Ambig. in Li. tréikiu, -ti ‘rage’ Go. breihan, v. ‘press, squeeze’; Latv. triecu, triekt, v. ‘batter, crush’. For Go. faíhu-praibns *riches' see trika-. Latv. ambig. cf. troik-)
18893:(treK- ‘rot’, etc. Cf. trenK- and tronk-. Thus only in Li. trešiù, eti, id. & tre&ti, inf. id.)
18898:trenko, ið “force, browbeat, bully’. Cf. WP I, 735 & 759. Cf. tronk- MHG dringen, sv. 3. (2) ‘squeeze, press’; OE bringan, sv. id.; Li. trenkiü, trefikti, v. “bang, beat? beside trenkü, trifükti, v. ‘shampoo’; Latv. trencu, trenkt, v. “drive, persecute? be- side triecu, triekt, v. "batter, cru
18907:cf. treik-; thus also for Go. preihan, v. ‘squash’, rather than to type trenk-)
18908:trenKó, ið ‘soil, defile’. Cf. tronK-. (Variant *treK- only in Li.) Br. trenka, tr. & intr. ‘sour; become sour’; trenk, adj. “sour, acrid, severe’; Cz. cf. třísnit, inf. ‘defile’; (o-gde in) trous, m. ‘manure’; Li. trestü, trésti (sic), intr. ‘rot, decay? beside Des, trësti, tr. ‘manure’; (o-g
18909:trepito (trepido, trepero, ið) ‘flutter, flicker, tremble'. Cf. WP I, 756 Lat. trepido, are, v. id.; Br. trida, v. ‘tremble, quake’; Ir. cf. triath, f. queried: ‘surge’; R trepetàt', Cz. tfepetat, inf. ‘flutter, tremble’, cf. also R trépet, Cz. tfepet, & tfepot, m. id.; Srb. trepcem, treptati,
19006:tronk- (tronkos, ios) “bump, jostle, tumult, crowd'. Cf. trenk- & WP I, 759 OHG ge-drengi, n. id.; OE prang, n. ‘crowd, tumult; MHG dranc, gs: dranges, sm. *pres- sure, oppression, throng’; prange, adj. ‘close’; ON brongr, acc. sg: prongvan, adj. ‘tight, com- pact’; Sw. tráng, adj. id.; Li. tr
19007:tronKos, å, us ‘nauseous; vileness, filth’. Variant troK-. Cf. trenKo, ið and WP II, 642 Tokh. tranko, s. ‘sin, wrong’; W trwnc, m. (“' urine”, fr. *tronKus); OE proh, adj. ‘rancid’ beside Fris. trang, id.; Cz. trus, m. 'réfuse, dung, dross’ beside trousit, R trusit and OCS po-trositi, v. ‘sca
19082:trük- (1) “break down, fail, collapse, die’. Cf. trunk- and trük- (2) Olr. Ir. trú, gs: troch, m. 'outlaw, wretch’; troch, m. id.; adj. *wretched'; trochaim, v. “pine away, decay’; OBr. cf. in-troc, adv. ‘foul- ly’; Br. troc, adj. ‘wretched’; Cor. troc, m. as Ir. trú, troch; Lat. cf. truncus, 
19104:trunk- (?). Cf. trük- (1). (Semantics obscure) Lat. truncus, adj. “maimed, docked'; MHG cf. drüch, gs: drühes, sm. ‘trap’; Li. cf. trunku, inf: trukti, v. ‘trail, drag-out, dally’. (Isopho- nic: OE brüh, mfn. “pipe; trough; chest, cof- fin". Not to G Truhe)
```


## [2026-10-15T02:47:52.773Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; sed -n 71870,71900p WLD_Bd1_pages.txt; echo ----; sed -n 71615,71640p WLD_Bd1_pages.txt",
 "description": "Print WLD trenk and trep passages"
}
```


### [2026-10-15T02:47:53.567Z] TOOL RESULT

```
*tres- erweitert sind. Trautmann Bsl. Wb. 329 f.

1.    trenq- „stoBen (auch drohnend), zusammendrangen, bedrangen                                              ££
                                                                                                                   ,
                                                                                                                       s.   auch
        trenq- „waschen, baden“.
     Av. draxtanqm g. pi. „der zsgedrangten, enggeschlossenen [Schlacht-
            (in der Bed. engstens zum Germ, stimmend, Btbl. ZfdWtf. 4, 252,
         ££
reihen]
Wb. 801).
  Lat. truncus „(abgestoGener) Baumstamm ohne Aste, Rumpf“, Adj. (nach
Niedermann Y Jb 1912, 1 330 erst durch Riickbildung aus truncaret) „ver-
                          .




stummelt. der Aste oder Glieder beraubt", trunco, - are „verstummeln, ab-,
niederhauen ££ (verfehlt iiber truncus v. Bradke ZdmG. 40, 352 und Sutter-
                                              ££
lin IF. 27, 127); cymr. trwch „verstummelt       (Stokes Arch. Cambr. 1873, 11;
IF. 2, 172, Fick II 4 136 unter einer Gdf. *trolrno-, die nur bei Diss. aus
*tronk-no- ertraglich ware; wohl aus '*tronk-so- und ein Parallelfall zu
cymr. troclii „baden“ (wohl aus *tronks-, s. * trenq- „waschen ££ ); vielleicht
(„es drangt mich ,£ ) air. di-fo-tracc- „wiinschen ££ (z. B. d-a-du-th raccar „ich
wiinsche es ££ , Inf. d fit hr add; Lautbestimmung unklar, s. Pedersen KG. II
 653 f.); wahrscheinlich (als „abgedrangt werden ££ ) air. mir. treicim „ver-
 Iasse, weiche“ (z. B. 1. sg. Fut. noco-trecmb. Inf. trecud), cymr. trenq „ver-
                               ;                                                                                -           ,

----
stufig *pruhtu- in aisl. prottr m. „Kraft,                                          Ausdauer                    ags. proht           m. „An-
                                                                       £
strengung, Miihsal", proht ,,bedriickend '.
  Ygl. Zup. G. 21 7, Pick III 4 189, Palk-Torp u. idrcet, Persson Beitr. 432.                                                                —
In der Bed. ferner liegt Endzelin’s KZ. 44, 57 Yergleick der kelt. Sippe
mit lett. treJcus ,,feist, gemastet".

1.    trep- „trippeln, trampeln, treten".
     Ai. trpra-h, trpdla-h „hastig“ (wohl aus „trippelnd ') ; gr. tqolji eco „keltere"
                                                                                                   £




(„trete die             Trauben aus“), arganog, hom. maonog „FuBsteig                                                 £:
                                                                                                                               (a-       „copu-
lativum“,              eig. ,,ausgetretener     Weg     ££
                                                             ),       tqojieovto'             Inmovv Hes., Oivorgonoi
(Fick    BB. 28, 1 06 f.) „Gottheiten des Weinbaues"; alb. (Jokl SBAkWien
 168 I 85f.) *trip = gr. rgan- in s-tip, s-tiip „zertrete, zerstoBe, zerquetsche •,
per-t(j)up ,.kaue“, s-trip, zdrilp „steige herab
                                                                                      -
                                                     lat. trepidus ,,trippelnd (vor       ;


Geschaftigkeit oder Furcht), hastig, unruhig, angstlich", trepido, -are
```


## [2026-10-15T02:47:57.181Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 -c \"\nimport json;d=json.load(open('page-499.json'));print({k:v for k,v in d.items() if k!='entries'}); e=d['entries'][0]; print(list(e.keys())); print(list(e['nodes'][0].keys()))\"; python3 -c \"\nimport json;d=json.load(open('../extracted/batch/page-512.json'));[print(n['id'],n.get('quote'),n.get('script_extra')) for n in d['entries'][1]['nodes']]\"",
 "description": "Inspect prior output format and source quotes"
}
```


### [2026-10-15T02:47:57.700Z] TOOL RESULT

```
{'pdf_page': 499, 'book_page': 469, 'verified_by': 'claude-opus-5', 'verified_on': '2026-10-14'}
['entry', 'root', 'verdict', 'modern_form', 'note', 'note_fa', 'sources', 'ref_check', 'consulted', 'nodes']
['id', 'lang', 'words', 'verdict', 'derivation', 'derivation_fa', 'sources', 'ref_check', 'consulted']
1 None None
2 None None
3 None None
4 {'text': 'چو آمد به نزدیکی بارگاه - سبک نزد شاهش گشادند راه', 'poet': 'Ferdowsî'} None
5 None None
6 None None
7 None None
```


## [2026-10-15T02:48:00.825Z] TOOL CALL #51: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg512.png /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/512.png",
 "description": "Copy book page image for audit"
}
```


### [2026-10-15T02:48:01.212Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:50:12.908Z] TOOL CALL #52: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-512.py",
 "content": "import json\n\nW = \"https://en.wiktionary.org/wiki/\"\nS_SABUK = W + \"سبک\"\nS_CABUK = W + \"چابک\"\nS_TRUNCUS = W + \"truncus\"\nS_THRONG = W + \"throng\"\nS_TREPIDUS = W + \"trepidus\"\nS_THRINH = W + \"Reconstruction:Proto-Germanic/þrinhwaną\"\nS_TRENCH = W + \"trench\"\nS_TRUNK = W + \"trunk\"\n\nPOK_TRENK = {\"ref\": \"POK:1093\", \"status\": \"supports\", \"note\": \"POK_full.txt 'Root / lemma: trenk-1 / Meaning: to push; to oppress / Material: Avestan θraxtanąm Gen. Pl. \\\"zusammengedrängt\\\" ... Latin truncus ... Old English þringan, Old High German dringan ... Old English geþrang' (Page(s): 1093).\"}\nWLD_TRENK = {\"src\": \"WLD\", \"where\": \"Bd. I 758-759, 1. trenq- (WLD_Bd1_pages.txt l.71872 ff.)\", \"stance\": \"supports\", \"note\": \"'1. trenq- „stoßen (auch dröhnend), zusammendrängen, bedrängen“. Av. θraxtanąm g. pl. „der zsgedrängten, enggeschlossenen [Schlachtreihen]“ ... Lat. truncus „(abgestoßener) Baumstamm ohne Äste, Rumpf“'.\"}\nAHD_NOTRENK = {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt)\", \"stance\": \"silent\", \"note\": \"No root *trenk- 'push' in Watkins; grep '^trenk' finds only 'strenk-. Tight, narrow'; THRONG is not indexed.\"}\nIEC_TRENK = {\"src\": \"IEC\", \"where\": \"IEC.txt l.18898, 19006\", \"stance\": \"supports\", \"note\": \"'trenko ‘force, browbeat, bully’ ... MHG dringen ... OE þringan ... Li. trenkiù'; 'tronk- (tronkos) ‘bump, jostle, tumult, crowd’ ... OE þrang, n. ‘crowd, tumult’'.\"}\n\nentries = []\n\n# ---------------- entry 0: Trenk ----------------\ne0_nodes = [\n    {\n        \"id\": 1, \"lang\": \"Avestan\", \"words\": \"traxtanam\", \"verdict\": \"confirmed\",\n        \"derivation\": \"Av. θraxtanąm is the gen. pl. of the adjective/participle θraxta- 'pressed together, closely packed' (Yt 14.63, of battle-lines: θraxtanąm rasmanąm 'of the serried ranks'), from zero-/e-grade *trenk- with the regular Iranian change *t > θ before r and *k > x before t (*trnk-to- / *trenk-to- > *θraxta-). Pokorny, Walde-Pokorny, Bartholomae and Klein all set it beside Germanic *þrinhwan- 'to press'. Nourai's 'traxtanam' simply writes initial θ as t and drops the nasal-vowel mark of -ąm; the form is recognisable and not a misreading.\",\n        \"derivation_fa\": \"واژهٔ اوستایی θraxtanąm حالت اضافی جمعِ صفت θraxta- «به‌هم‌فشرده، تنگ‌بسته» است که در یشت ۱۴ بند ۶۳ برای «صف‌های فشردهٔ سپاه» آمده؛ از ریشهٔ هندواروپایی *trenk- «فشردن» با دگرگونی آوایی t به θ پیش از r و k به x پیش از t. پوکورنی، والده‌ـ‌پوکورنی، بارتولومه و کلاین همه آن را با فعل ژرمنی «فشردن» هم‌ریشه می‌دانند. نورایی θ را t نوشته و نشانهٔ خیشومی پایانی را انداخته، ولی صورت درست شناخته می‌شود؛ ادعای نورایی درست است.\",\n        \"sources\": [],\n        \"ref_check\": [\n            POK_TRENK,\n            {\"ref\": \"KLN:1612\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.39152 s.v. throng: '... Goth. þreihan (for *þrinhan), ‘to oppress’, and cogn. with Avestic θraxtanam (gen. pl.), ‘of those pressed together’, Lith. trenkiu, trenkti, ‘to push, jolt’.'\"}\n        ],\n        \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. ~801 s.v. θraxta- (BRT.txt l.14493, 20954, 25219)\", \"stance\": \"supports\", \"note\": \"'θraxta- Adj. ‘zusammengedrängt, eng aufgeschlossen’: θraxtanąm rasmanąm \\\"phalangum stipatarum\\\" Yt. 14.63'.\"},\n            WLD_TRENK\n        ]\n    },\n    {\n        \"id\": 2, \"lang\": \"‼UNCLEAR\", \"words\": \"\", \"verdict\": \"unverified\",\n        \"derivation\": \"The printed page (pdf 512, checked on the page image) shows an empty double-bordered box to the right of the Avestan box, connected by an arrow, with no language header and no word: Nourai evidently intended a Persian descendant of θraxta- but left it blank. No New Persian or Middle Persian reflex of Av. θraxta- is known in Bartholomae, Horn, MacKenzie or Wiktionary, so there is nothing to verify; the extraction is faithful.\",\n        \"derivation_fa\": \"در صفحهٔ چاپی کتاب، کنار خانهٔ اوستایی یک خانهٔ دوخطیِ خالی (بی‌نام زبان و بی‌واژه) با پیکان آمده است؛ گویا نورایی می‌خواسته بازماندهٔ فارسیِ θraxta- را بیاورد ولی آن را ننوشته. در بارتولومه، هرن، مکنزی و ویکی‌واژه بازمانده‌ای در فارسی میانه یا فارسی نو برای این واژه یافت نشد؛ پس چیزی برای سنجش نیست و استخراج داده با کتاب یکی است.\",\n        \"sources\": [],\n        \"ref_check\": [{\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"Box carries no references and no content.\"}],\n        \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"s.v. θraxta-\", \"stance\": \"silent\", \"note\": \"Bartholomae gives no Middle/New Persian continuant for θraxta-.\"},\n            {\"src\": \"PHD\", \"where\": \"grep 'traxt', 'saxt'\", \"stance\": \"silent\", \"note\": \"No Pahlavi word from *θraxta- found in MacKenzie.\"}\n        ]\n    },\n    {\n        \"id\": 3, \"lang\": \"Germanic\", \"words\": \"dringan\", \"verdict\": \"confirmed\",\n        \"derivation\": \"OHG dringan / OS thringan / OE þringan 'to press, crowd, throng' continue Proto-Germanic *þrinhwaną (strong verb III), from PIE *trenk(ʷ)- 'to press, push'; Grimm's law turned *t > þ (OHG d) and *k(ʷ) > *h(w), and the nasal before h was later restored analogically or kept as -ng- via Verner variants (*þrungw-). Gothic þreihan 'to oppress' shows the same root with loss of n before h. 'dringan' is the Old High German form, labelled generically 'Germanic' by Nourai.\",\n        \"derivation_fa\": \"فعل dringan در آلمانی علیای کهن (و thringan در ساکسونی کهن، þringan در انگلیسی کهن) به معنی «فشار آوردن، ازدحام کردن» از ژرمنی آغازین *þrinhwaną و آن از ریشهٔ هندواروپایی *trenk- «فشردن، راندن» است؛ بنا بر قانون گریم t به þ (در آلمانی d) و k به h بدل شده است. گوتی þreihan «ستم کردن» نیز هم‌ریشه است. ادعای نورایی درست است.\",\n        \"sources\": [S_THRINH],\n        \"ref_check\": [{\"ref\": \"KLN:1612\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.39152 s.v. throng: 'OE. þringan, OS. thringan, ON. þryngva, ‘to press on, crowd’ ... OHG. dringan, MHG., G. dringen, ‘to press on, crowd’ ... Goth. þreihan (for *þrinhan), ‘to oppress’'.\"}],\n        \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 1093 trenk-1\", \"stance\": \"supports\", \"note\": \"'Old English þringan stem V., Old High German dringan ds.'\"},\n            WLD_TRENK,\n            IEC_TRENK,\n            AHD_NOTRENK\n        ]\n    },\n    {\n        \"id\": 4, \"lang\": \"English\", \"words\": \"throng\", \"verdict\": \"confirmed\",\n        \"derivation\": \"English throng (ME throng, thrang) is from OE geþrang / þrang 'crowd, tumult', the o-grade noun (PGmc *þrangwą) to the verb *þrinhwaną (OE þringan), cf. ON þröng, Du. drang, G. Gedränge; semantically 'a pressing' > 'a crowd'.\",\n        \"derivation_fa\": \"واژهٔ انگلیسی throng «انبوه مردم» از انگلیسی میانهٔ throng و انگلیسی کهن geþrang / þrang «ازدحام، غوغا» است که اسمِ ساخته‌شده با درجهٔ o از همان فعل þringan «فشردن» است؛ تحول معنایی «فشار» به «جمعیتِ به‌هم‌فشرده». ادعای نورایی درست است.\",\n        \"sources\": [S_THRONG],\n        \"ref_check\": [{\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"Node carries no reference; parent's KLN:1612 s.v. throng covers it: 'ME. throng, fr. OE. þrang, geþrang, ‘crowd, tumult’'.\"}],\n        \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 1612 s.v. throng (KLN_1966.txt l.39152)\", \"stance\": \"supports\", \"note\": \"'throng, n., crowd. — ME. throng, fr. OE. þrang, geþrang, ‘crowd, tumult’, rel. to ON. þrong, Du. drang, G. Drang, Gedränge'.\"},\n            {\"src\": \"POK\", \"where\": \"p. 1093 trenk-1\", \"stance\": \"supports\", \"note\": \"'Old English geþrang n. \\\"crush, gedrängte troop, multitude, crowd\\\"'.\"},\n            IEC_TRENK,\n            {\"src\": \"SKT\", \"where\": \"SKT.txt\", \"stance\": \"silent\", \"note\": \"grep 'throng' gives only incidental uses; the headword is illegible in the OCR.\"}\n        ]\n    },\n    {\n        \"id\": 5, \"lang\": \"Latin\", \"words\": \"trancus\", \"verdict\": \"transcription_suspect\",\n        \"derivation\": \"The Latin word is truncus 'trunk of a tree, lopped stem' (orig. adj. 'maimed, cut off'); 'trancus' does not exist. The page image shows 'trancus' printed, so this is Nourai's misprint and the extraction is faithful. On the root: Pokorny 1093, Walde-Pokorny and Klein put truncus under *trenk- 'press' (*tronk-o- > truncus with -on- > -un- before velar), but Watkins/AHD (as Nourai's own note says) derive it from terə-2 'overcome' via *tru-n-k-o-, Mann sets up a separate trunk-, and Wiktionary calls it of unknown origin, possibly *twerḱ- 'cut'; the *trenk- connection is thus one view among several.\",\n        \"derivation_fa\": \"واژهٔ لاتینی درست truncus «تنهٔ درختِ شاخه‌زده» (در اصل صفت «بریده، ناقص‌شده») است و «trancus» در لاتینی وجود ندارد؛ کتاب همین «trancus» را چاپ کرده، پس خطای چاپی کتاب است، نه خطای خوانش. دربارهٔ ریشه: پوکورنی، والده‌ـ‌پوکورنی و کلاین آن را از *trenk- «فشردن» می‌دانند، ولی واتکینز (فرهنگ امریکن هریتیج) آن را از terə- «چیره شدن» با صورت *tru-n-k-o- می‌گیرد و ویکی‌واژه آن را ناروشن (شاید از *twerḱ- «بریدن») می‌داند؛ پس پیوند با *trenk- تنها یکی از دیدگاه‌هاست.\",\n        \"error_in\": \"book\",\n        \"book_prints\": \"trancus\",\n        \"correct_form\": \"truncus\",\n        \"sources\": [S_TRUNCUS],\n        \"ref_check\": [\n            {\"ref\": \"POK:1093\", \"status\": \"supports\", \"note\": \"Pokorny trenk-1: 'Latin truncus \\\"tree trunk\\\", Adj. \\\"mutilated\\\" ... trunco, -are \\\"mutilate\\\"' — Pokorny has truncus, not 'trancus'.\"},\n            {\"ref\": \"KLN:1660\", \"status\": \"partial\", \"note\": \"KLN_1966.txt l.40356 s.v. trunk: 'fr. L. truncus ... which prob. stands for *troncos, fr. I.-E. base *trank-, ‘to press’, whence also Lith. trenkiu ... prob. not cogn. with E. throng.' Klein supports the root but explicitly doubts the throng (Germanic) link drawn in the same chart.\"}\n        ],\n        \"consulted\": [\n            WLD_TRENK,\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, terə-2 (AHD_watkins1985.txt l.1083)\", \"stance\": \"contradicts\", \"note\": \"'Suffixed nasalized form *tru-n-k-o- in Latin truncus, deprived of branches or limbs, mutilated, hence trunk (? < \\\"overcome, maimed\\\"): TRENCH, TRUNCATE, TRUNK. [Pok. 5. ter- 1075.]' — matches Nourai's note citing AHD:1546.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt l.19104\", \"stance\": \"contradicts\", \"note\": \"'trunk- (?). Cf. trūk- (1). (Semantics obscure) Lat. truncus, adj. \\\"maimed, docked\\\"' — Mann keeps truncus apart from trenk-.\"},\n            {\"src\": \"LEW\", \"where\": \"LEW_1910.txt\", \"stance\": \"silent\", \"note\": \"not separately quoted; WLD (by Walde) gives the trenq- view.\"}\n        ]\n    },\n    {\n        \"id\": 6, \"lang\": \"English\", \"words\": \"trunk, truncate, trench\", \"verdict\": \"plausible\",\n        \"derivation\": \"trunk: ME tronke < OF tronc < Lat. truncus (confirmed). truncate: 15th c. from Lat. truncātus, pp. of truncāre 'to lop off', denominative from truncus (confirmed). trench: ME trenche < OF trenche / trenchier 'to cut' (F. trancher), usually traced to VL *trincāre, an alteration of Lat. truncāre (Klein, Watkins); the vowel change is unexplained and an alternative *trinicāre 'cut in three' has been proposed, so for trench the link to truncus is probable rather than certain. The Latin-to-English edges are sound; whether truncus itself belongs to *trenk- is the question discussed at node 5.\",\n        \"derivation_fa\": \"trunk «تنهٔ درخت» از انگلیسی میانهٔ tronke و فرانسوی کهن tronc از لاتینی truncus است؛ truncate «بریدن، کوتاه کردن» از truncātus، صفت مفعولیِ truncāre «شاخه زدن» است. trench «خندق» از فرانسوی کهن trenche / trenchier «بریدن» است که معمولاً آن را از لاتینی عامیانهٔ *trincāre، دگرگون‌شدهٔ truncāre، می‌دانند، ولی دگرگونی واکه روشن نیست. پس پیوند این سه با truncus پذیرفتنی است (برای trench با احتیاط)، و پرسشِ اصلی دربارهٔ ریشهٔ خودِ truncus است.\",\n        \"sources\": [S_TRUNK, S_TRENCH],\n        \"ref_check\": [{\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"Node carries no reference; KLN (parent's KLN:1660) s.v. trunk: 'Cp. truncate, truncheon, trunnion, trench'.\"}],\n        \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. trench (KLN_1966.txt l.39994) and trunk (l.40356)\", \"stance\": \"supports\", \"note\": \"'trench, tr. and intr. v., to cut. — MF. trenchier (F. trancher) ‘to cut’, fr. L. truncare, ‘to cut off’ (whence also It. troncare). See truncate'; 'trunk ... ME. tronke, trunke, fr. MF. (= F.) tronc, fr. L. truncus'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 terə-2\", \"stance\": \"supports\", \"note\": \"'Latin truncus ...: TRENCH, TRUNCATE, TRUNK' (same three words, root aside).\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt l.20261\", \"stance\": \"supports\", \"note\": \"'Trunk, stem of a tree ... (F. — L.) F. tronc, trunk. — L. truncum, acc. of truncus ... cut off, maimed' (OCR noisy).\"}\n        ]\n    }\n]\n\nentries.append({\n    \"entry\": 0,\n    \"root\": \"Trenk, Tronkus\",\n    \"verdict\": \"confirmed\",\n    \"modern_form\": \"PIE *trenk- (Wiktionary *trenkʷ-) 'to press, push, oppress'; o-grade *tronk-\",\n    \"note\": \"Pokorny 1093 trenk-1 'to push; to oppress' (= Nourai's gloss); Walde-Pokorny I 758 trenq-; Wiktionary *trenkʷ- 'beat, press'. 'Tronkus' is not a separate root but the o-grade nominal *tronko- that Pokorny/Klein posit behind Lat. truncus. The Avestan and Germanic branches are uncontroversial; the Latin branch (truncus) is disputed — Watkins/AHD put it under terə-2, Wiktionary calls it obscure — and the book misprints truncus as 'trancus'. Klein notes truncus is 'prob. not cogn. with E. throng'. Watkins 1985 has no *trenk- root at all.\",\n    \"note_fa\": \"ریشهٔ هندواروپایی آغازین *trenk- (در ویکی‌واژه *trenkʷ-) «فشردن، راندن، ستم کردن» در پوکورنی (ص ۱۰۹۳) و والده‌ـ‌پوکورنی آمده و معنای نورایی درست است؛ «Tronkus» ریشهٔ جداگانه نیست، بلکه صورت درجهٔ o (*tronko-) است که پوکورنی و کلاین پشت لاتینی truncus می‌نهند. شاخهٔ اوستایی (θraxta-) و ژرمنی (dringan، throng) پذیرفته است، ولی پیوند truncus با این ریشه مورد اختلاف است (واتکینز آن را از terə- و ویکی‌واژه ناروشن می‌داند)، و کتاب truncus را به خطا «trancus» چاپ کرده است.\",\n    \"sources\": [S_THRINH, S_THRONG, S_TRUNCUS],\n    \"ref_check\": [POK_TRENK],\n    \"consulted\": [WLD_TRENK, AHD_NOTRENK, IEC_TRENK],\n    \"nodes\": e0_nodes\n})\n\n# ---------------- entry 1: Trep 1 ----------------\nPOK_TREP = {\"ref\": \"POK:1094\", \"status\": \"supports\", \"note\": \"POK_full.txt 'Root / lemma: trep-1 / Meaning: to trample, tread / Material: Old Indic tṛprá-, tṛpála- \\\"hasty, unstet\\\"? (probably from \\\"trippelnd\\\") ... Latin trepidus \\\"anxiously umherlaufend\\\" ... Old Church Slavic trepetъ \\\"das Zittern, Beben\\\"' (Page(s): 1094).\"}\nWLD_TREP = {\"src\": \"WLD\", \"where\": \"Bd. I 756, 1. trep- (WLD_Bd1_pages.txt l.71621 ff.)\", \"stance\": \"supports\", \"note\": \"'1. trep- „trippeln, trampeln, treten“. Ai. tṛprá-h, tṛpála-h „hastig“ (wohl aus „trippelnd“) ... lat. trepidus „trippelnd (vor Geschäftigkeit oder Furcht), hastig, unruhig, ängstlich“'.\"}\nAHD_TREP = {\"src\": \"AHD\", \"where\": \"Watkins 1985 trep-1 (AHD_watkins1985.txt l.1096)\", \"stance\": \"supports\", \"note\": \"'trep-1. To tremble. Possibly related to trem- and tres- ... Latin trepidus, agitated, alarmed: TREPID; INTREPID. [Pok. 1. trep- 1094.]'\"}\nIEC_TREP = {\"src\": \"IEC\", \"where\": \"IEC.txt l.18909\", \"stance\": \"supports\", \"note\": \"'trepito (trepido ...) ‘flutter, flicker, tremble’. Cf. WP I, 756 Lat. trepido, -are ... R trepetát'.\"}\nNYB_SAPUK = {\"src\": \"NYB\", \"where\": \"vol. 2 glossary p. ~173 s.v. sapūk (NYB_vol2_glossary.txt l.3391)\", \"stance\": \"supports\", \"note\": \"'sapūk [spwk'] light, brisk; unsteady, shallow ... — < OP *çapu-ka- < OIr *θrapu-ka-, from IE *trep-, Gr τρέπω ‘to turn’, Lat trepidus ‘agitated, anxious’, cf Skr tṛprá- id.; Paz. NP sabuk.'\"}\nBQT1083 = {\"ref\": \"BQT:1083\", \"status\": \"supports\", \"note\": \"Mo'in's footnote 2 s.v. سبك (archive.org borhan-ghate-v2 leaf n545; transcribed in ocr/BQT/1083.vision.txt): 'پهلوی sapûk (سبك، چابك). پارسی باستان *çapu-ka = ایرانی باستان *thrapu- در سانسکریت trpra، افغانی spuk «نیبرگ ۲۰۱»' — supports thrapu-/sapûk/sabok; note Mo'in writes OP ç, not č.\"}\nBQT607 = {\"ref\": \"BQT:607\", \"status\": \"contradicts\", \"note\": \"Mo'in's footnote 3 s.v. چابك (archive.org borhan-ghate-v2 leaf n65; ocr/BQT/607.vision.txt): 'پهلوی câpûk، ایرانی‌باستان *câpu-ka- ارمنی capuk (قابل‌انحناء، نرم، زرنگ)، نیز ارمنی cep (شتاب)' — Mo'in derives čābok from OIr *čāpu-ka- (with č), not from *thrapu-; he only glosses Pahl. sapûk as 'سبك، چابك'.\"}\n\ne1_nodes = [\n    {\n        \"id\": 1, \"lang\": \"Old Iranian\", \"words\": \"thrapu\", \"verdict\": \"plausible\",\n        \"derivation\": \"Proto-Iranian *θrapu-(ka-) 'unsteady, quick, light' is a reconstruction (Mo'in *thrapu-, Nyberg *θrapu-ka-, Wiktionary *θrapuka- from *θrap- 'to be unsteady'), built on MP sapūk / NP sabok, Pashto spuk 'light' and the Indic match tṛprá- 'hasty'; PIE *t > Iranian θ before r. The Iranian form is well founded; the link to PIE *trep- is accepted by Nyberg and Mo'in but flagged 'perhaps' by Wiktionary.\",\n        \"derivation_fa\": \"صورت ایرانی باستانِ *θrapu-(ka-) «ناپایدار، چابک، سبک» بازسازی است (معین *thrapu-، نیبرگ *θrapu-ka-، ویکی‌واژه *θrapuka- از ستاک *θrap- «لرزان بودن») و بر پایهٔ فارسی میانهٔ sapūk، فارسی نو «سبک» و پشتوی spuk و هم‌ریشهٔ سنسکریت tṛprá- «شتابان» ساخته شده؛ t هندواروپایی پیش از r در ایرانی به θ بدل شده است. صورت ایرانی استوار است و پیوندش با *trep- را نیبرگ و معین پذیرفته‌اند، ولی ویکی‌واژه آن را با «شاید» آورده؛ پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n        \"sources\": [S_SABUK],\n        \"ref_check\": [BQT1083],\n        \"consulted\": [\n            NYB_SAPUK,\n            {\"src\": \"BRT\", \"where\": \"grep 'θrap', 'Orapu'\", \"stance\": \"silent\", \"note\": \"No Avestan *θrapu- attested; the form is a reconstruction.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt l.8760\", \"stance\": \"partial\", \"note\": \"'sabuk leicht, afgh. spuk, paz. sabuk ... phl. sapuk' — Pahlavi/Pashto equation, no Old Iranian form given.\"}\n        ]\n    },\n    {\n        \"id\": 2, \"lang\": \"Old Persian\", \"words\": \"čapu-ka\", \"verdict\": \"transcription_suspect\",\n        \"derivation\": \"Unattested Old Persian *çapu-ka-: in Old Persian Proto-Iranian *θr regularly became the sibilant written ç (cf. puça- 'son' vs Av. puθra-), which gives MP s- in sapūk/sabuk; this is exactly what Mo'in (BQT 1083: 'پارسی باستان çapu-ka') and Nyberg ('< OP *çapu-ka- < OIr *θrapu-ka-') write. The book prints 'čapu-ka' with č (háček), which is a different sound and would not yield MP s-; it appears to blend Mo'in's *çapu-ka (for sabok) with his separate *čāpu-ka- (for čābok, BQT 607). The extraction matches the page; the error is the book's, and the asterisk marking a reconstruction is also missing.\",\n        \"derivation_fa\": \"صورت پارسی باستانِ ناگواهیده *çapu-ka- است: در پارسی باستان θr ایرانی باستان به صامتی بدل می‌شود که با ç نوشته می‌شود (مانند puça- «پسر» در برابر اوستایی puθra-)، و همین ç در فارسی میانه به s می‌رسد (sapūk ← «سبک»). معین در حاشیهٔ برهان (ص ۱۰۸۳) و نیبرگ هر دو *çapu-ka نوشته‌اند. کتاب «čapu-ka» با چ چاپ کرده که آوای دیگری است و به s فارسی میانه نمی‌انجامد؛ گویا با *čāpu-ka- که معین برای «چابک» آورده درآمیخته است. این خطای چاپی (یا آمیختگی) کتاب است، نه خطای خوانش، و نشانهٔ ستاره (بازسازی) نیز افتاده است.\",\n        \"error_in\": \"book\",\n        \"book_prints\": \"čapu-ka\",\n        \"correct_form\": \"*çapu-ka-\",\n        \"sources\": [S_SABUK],\n        \"ref_check\": [BQT1083],\n        \"consulted\": [\n            NYB_SAPUK,\n            {\"src\": \"KNT\", \"where\": \"grep 'çapu', 'capuka'\", \"stance\": \"silent\", \"note\": \"Kent's lexicon has no such word; it is unattested in Old Persian inscriptions (Kent §: OP ç < IIr. *tr/θr confirmed by puça-).\"}\n        ]\n    },\n    {\n        \"id\": 3, \"lang\": \"Pahlavi\", \"words\": \"čâpŭk; sapŭk\", \"verdict\": \"disputed\",\n        \"derivation\": \"sapūk: Book Pahlavi spwk' sabuk/sapūk 'light, easy; brisk' (MacKenzie, Nyberg) continues OP *çapu-ka- < OIr *θrapu-ka- with OP ç > MP s — confirmed. čāpūk: Pahlavi c'pwk' čābuk 'agile, nimble; excellent' is a real word (MacKenzie, Nyberg), but no source derives it from *θrapu-: initial č cannot come from *θr. Mo'in (BQT 607) gives it a separate OIr *čāpu-ka-, and Wiktionary derives it from an unattested root borrowed as Old Armenian čep 'haste' (cf. Arm. čapuk). Nourai has placed čāpūk in the sapūk chain because Mo'in glosses sapûk as 'سبك، چابك' (light, swift); the čāpūk part is not supported.\",\n        \"derivation_fa\": \"واژهٔ پهلوی sapūk / sabuk (spwk') «سبک، آسان، چالاک» به گواهی مکنزی و نیبرگ از پارسی باستان *çapu-ka- و ایرانی باستان *θrapu-ka- است (ç پارسی باستان در فارسی میانه s می‌شود) و درست است. ولی čāpūk / čābuk (c'pwk') «چابک، چالاک» گرچه واژه‌ای واقعی است، از *θrapu- نمی‌آید، چون چ آغازین از θr پدید نمی‌آید؛ معین (برهان، ص ۶۰۷) آن را از *čāpu-ka- جداگانه می‌داند و ویکی‌واژه آن را با ارمنی čep «شتاب» و čapuk مرتبط می‌کند. نورایی چون معین sapûk را «سبک، چابک» معنی کرده، چابک را هم در این شاخه آورده است؛ این بخش را پژوهش امروزی تأیید نمی‌کند.\",\n        \"sources\": [S_SABUK, S_CABUK],\n        \"ref_check\": [BQT607, BQT1083],\n        \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 21 s.v. čābuk; p. 72 s.v. sabuk (PHD.txt l.296, 562)\", \"stance\": \"partial\", \"note\": \"'čābuk [cʾpwk | N ~] agile, nimble; excellent'; 'sabuk [spwk | N ~] light, easy' — two separate words, no etymology.\"},\n            {\"src\": \"NYB\", \"where\": \"glossary s.v. sapūk (l.3391) and čāpūk (l.1100)\", \"stance\": \"partial\", \"note\": \"sapūk '< OP *çapu-ka- < OIr *θrapu-ka-, from IE *trep-'; but 'čāpūk [c'pwk'] quick, brisk; busy, active — NP čābuk' with no derivation from *θrapu-.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt l.8760-8763\", \"stance\": \"partial\", \"note\": \"'sabuk leicht, afgh. spuk ... phl. sapuk'; separately 'čābuk schnell, flink, behend, geschickt, arm. čapuk' — Hübschmann keeps them apart.\"}\n        ]\n    },\n    {\n        \"id\": 4, \"lang\": \"Persian\", \"words\": \"čâbok «چابک»; sabok «سبک»\", \"verdict\": \"disputed\",\n        \"derivation\": \"sabok «سبک» 'light (in weight), quick' < MP sabuk (spwk') < OP *çapu-ka- < OIr *θrapu-ka-, with intervocalic p > b in New Persian; cf. Pashto spuk and many dialect forms (Gilaki sobuk, Semnani subuk) listed by Mo'in — confirmed, and the Ferdowsi line quoted (سبک نزد شاهش گشادند راه) uses sabok as 'quickly'. čābok «چابک» 'agile, swift' < MP čābuk (c'pwk') with the same p > b, but its source is not *θrapu-: Mo'in (BQT 607) gives OIr *čāpu-ka- and Wiktionary an unattested root seen in Old Armenian čep 'haste' (Arm. čapuk, Georgian č̣abuḳi are Middle Iranian loans). So sabok is correctly placed, čābok is not.\",\n        \"derivation_fa\": \"«سبک» از فارسی میانهٔ sabuk (spwk')، از پارسی باستان *çapu-ka- و ایرانی باستان *θrapu-ka- است؛ p میان دو واکه در فارسی نو به ب نرم شده، و هم‌ریشه با پشتوی spuk و گویش‌های گیلکی sobuk و سمنانی subuk است (معین، برهان ص ۱۰۸۳)؛ بیت فردوسی «سبک نزد شاهش گشادند راه» نیز «سبک» را به معنی «شتابان» دارد. اما «چابک» از فارسی میانهٔ čābuk است و به گفتهٔ معین (برهان ص ۶۰۷) از *čāpu-ka- و به گفتهٔ ویکی‌واژه از ریشه‌ای که در ارمنی čep «شتاب» دیده می‌شود؛ پس پیوند «سبک» با *trep- پذیرفتنی است ولی «چابک» را پژوهش امروزی به این ریشه نمی‌برد.\",\n        \"sources\": [S_SABUK, S_CABUK],\n        \"ref_check\": [BQT607, BQT1083],\n        \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"HRN.txt grep 'sabuk', 'čābuk', 'cabuk'\", \"stance\": \"silent\", \"note\": \"Neither word found in Horn's Grundriss (OCR).\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt l.6259, 8760\", \"stance\": \"partial\", \"note\": \"'sabuk leicht = paz. sabuk' and 'čābuk schnell, flink ... arm. čapuk' — separate entries.\"},\n            NYB_SAPUK,\n            {\"src\": \"MON\", \"where\": \"via BQT footnotes (Mo'in)\", \"stance\": \"partial\", \"note\": \"Mo'in's own notes (BQT 607/1083) separate *čāpu-ka- (چابک) from *çapu-ka/*thrapu- (سبک).\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt grep 'سبک', 'چابک'\", \"stance\": \"silent\", \"note\": \"No usable hit in the OCR.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt grep 'θrap'\", \"stance\": \"silent\", \"note\": \"No verbal root *θrap- in Cheung (adjectives only).\"}\n        ]\n    },\n    {\n        \"id\": 5, \"lang\": \"Sanskrit\", \"words\": \"trprâh\", \"verdict\": \"confirmed\",\n        \"derivation\": \"Vedic tṛprá- 'hasty, restless' (also tṛpála-) is the zero-grade *tr̥p-ró- of *trep-, with syllabic *r̥ > Skt ṛ; Pokorny (with a query), Walde-Pokorny, Klein, Nyberg and Mo'in all set it beside Lat. trepidus and Ir. *θrapu-. Nourai's 'trprâh' is the nominative tṛpráḥ with diacritics simplified.\",\n        \"derivation_fa\": \"واژهٔ ودایی tṛprá- «شتابان، ناآرام» (و tṛpála-) از درجهٔ صفرِ ریشهٔ *trep- (*tr̥p-ró-) است که در آن r هجایی هندواروپایی در سنسکریت به ṛ رسیده؛ پوکورنی (با تردید)، والده‌ـ‌پوکورنی، کلاین، نیبرگ و معین آن را هم‌ریشهٔ لاتینی trepidus و ایرانی *θrapu- می‌دانند. «trprâh» نورایی همان حالت فاعلی tṛpráḥ است؛ ادعای نورایی درست است.\",\n        \"sources\": [],\n        \"ref_check\": [\n            POK_TREP,\n            BQT1083,\n            {\"ref\": \"KLN:1646\", \"status\": \"supports\", \"note\": \"KLN_1966.txt l.40006 s.v. trepidation: 'trepidus ... cogn. with OI. tṛpráḥ, tṛpálaḥ, ‘hasty’, Gk. τραπεῖν ‘to tread (grapes)’ ... All these words derive fr. I.-E. *tre-p-, ‘to shake, tremble’.'\"}\n        ],\n        \"consulted\": [WLD_TREP, NYB_SAPUK]\n    },\n    {\n        \"id\": 6, \"lang\": \"Latin\", \"words\": \"trepidus\", \"verdict\": \"confirmed\",\n        \"derivation\": \"Lat. trepidus 'agitated, alarmed, anxious' = *trep- + adjectival -idus (cf. trepidāre 'to bustle, tremble'); cognate with OCS trepetъ 'trembling', Russ. trepát'. Pokorny, Walde-Pokorny, Watkins, Klein and Wiktionary agree.\",\n        \"derivation_fa\": \"صفت لاتینی trepidus «پریشان، هراسان، ناآرام» از ریشهٔ *trep- با پسوند صفت‌ساز -idus ساخته شده (فعل trepidāre «شتابیدن، لرزیدن») و هم‌ریشهٔ اسلاوی کلیسایی کهن trepetъ «لرزش» و روسی trepát' است. پوکورنی، واتکینز، کلاین و ویکی‌واژه همه هم‌داستان‌اند؛ ادعای نورایی درست است.\",\n        \"sources\": [S_TREPIDUS],\n        \"ref_check\": [POK_TREP],\n        \"consulted\": [WLD_TREP, AHD_TREP, IEC_TREP,\n                      {\"src\": \"KLN\", \"where\": \"p. 1646 s.v. trepidation (l.40006)\", \"stance\": \"supports\", \"note\": \"'trepidus, ‘agitated, alarmed, restless, anxious, solicitous’ (see trepid), which stands for *trepodos'.\"}]\n    },\n    {\n        \"id\": 7, \"lang\": \"English\", \"words\": \"trepid\", \"verdict\": \"confirmed\",\n        \"derivation\": \"English trepid 'timid, trembling' (17th c., rare) is a direct learned borrowing of Lat. trepidus; the commoner intrepid (Lat. intrepidus) and trepidation (Lat. trepidātiō) belong to the same family.\",\n        \"derivation_fa\": \"واژهٔ انگلیسی trepid «ترسان، لرزان» (سدهٔ هفدهم، کم‌کاربرد) وام‌واژهٔ مستقیم و ادبی از لاتینی trepidus است؛ intrepid «بی‌باک» و trepidation «دلهره» نیز از همین خانواده‌اند. ادعای نورایی درست است.\",\n        \"sources\": [S_TREPIDUS],\n        \"ref_check\": [{\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"Node carries no reference; KLN s.v. trepidation refers to 'trepid'.\"}],\n        \"consulted\": [\n            AHD_TREP,\n            {\"src\": \"KLN\", \"where\": \"p. 1646 (l.40006)\", \"stance\": \"supports\", \"note\": \"'trepidus ... (see trepid)'.\"}\n        ]\n    }\n]\n\nentries.append({\n    \"entry\": 1,\n    \"root\": \"Trep 1\",\n    \"verdict\": \"confirmed\",\n    \"modern_form\": \"PIE *trep- 'to tremble; to trample, tread' (Pokorny 1. trep- 1094; Watkins trep-1 'to tremble')\",\n    \"note\": \"Root, number and gloss match Watkins/AHD trep-1 'to tremble' (Pokorny glosses 'trippeln, trampeln'); the box note 'may be related to Tres' echoes Watkins ('Possibly related to trem- and tres-'). Indic tṛprá-, Latin trepidus and Iranian *θrapu- > sabok are accepted (the Iranian link by Nyberg, Mo'in; Wiktionary says 'perhaps'). Problems: (1) Old Persian is *çapu-ka- (ç < θr), printed as 'čapu-ka'; (2) čābok/čāpūk does not belong here — Mo'in (BQT 607) and Wiktionary give it a separate origin (*čāpu-ka- / Arm. čep 'haste'); Nourai merged two of Mo'in's notes.\",\n    \"note_fa\": \"ریشهٔ هندواروپایی آغازین *trep- «لرزیدن؛ پا کوبیدن، گام برداشتن» (پوکورنی ص ۱۰۹۴؛ واتکینز trep-1 «لرزیدن») با معنای نورایی می‌خواند و یادداشتِ «شاید با tres- مرتبط باشد» نیز در واتکینز هست. سنسکریت tṛprá-، لاتینی trepidus و «سبک» فارسی (از *θrapu-) را نیبرگ و معین پذیرفته‌اند. ولی صورت پارسی باستان *çapu-ka- است نه «čapu-ka»، و «چابک» به این ریشه تعلق ندارد: معین در برهان (ص ۶۰۷) و ویکی‌واژه برای آن خاستگاه جداگانه‌ای می‌آورند؛ نورایی دو یادداشت معین را درآمیخته است.\",\n    \"sources\": [S_TREPIDUS, S_SABUK],\n    \"ref_check\": [POK_TREP],\n    \"consulted\": [WLD_TREP, AHD_TREP, IEC_TREP],\n    \"nodes\": e1_nodes\n})\n\nout = {\"pdf_page\": 512, \"book_page\": 482, \"verified_by\": \"claude-opus-5\", \"verified_on\": \"2026-10-14\", \"entries\": entries}\nwith open(\"/home/sfmqrb/git/rishe-private/data/verification/page-512.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\n"
}
```


### [2026-10-15T02:50:12.930Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-512.py (file state is current in your context — no need to Read it back)
```


## [2026-10-15T02:50:17.630Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo KNT; grep -a -c -i 'çapu\\|capuka\\|capu-ka' KNT_full.txt; grep -a -n 'puça' KNT_full.txt | head -2; echo PHD; grep -a -c -i 'traxt' PHD.txt; echo HRN; grep -a -c -i 'sabuk\\|čābuk\\|cabuk\\|cäbuk' HRN.txt; echo ARY; grep -a -n 'سبک\\|چابک' incoming/ARY/ARY_pages.txt | head -3; grep -a -n -i 'SABOK\\|CHABOK\\|SABUK' incoming/ARY/ARY_latin_index_pages.txt | head; echo CHEUNG; grep -a -c 'θrap\\|Orap' CHEUNG.txt; echo BRT; grep -a -c -i 'θrapu\\|Orapu' BRT.txt",
 "description": "Run the remaining claimed greps"
}
```


### [2026-10-15T02:50:18.047Z] TOOL RESULT

```
KNT
0
2050:puça : Haxámanisya : puça : Haxdémanisiya : 
3055:DB 2.15f, 2.81); Nabunaitahyd puça DB 3.81, 
PHD
0
HRN
0
ARY
653:ارابه‌ی مجهز به چرخهای پره‌دار (سبکك و سریع) و زندگانی شبانی و کوچگری (یادآور ایل‌های
699:زبانهای قفقاز و گورهای سبکك کورگان (1180۸) در شمال آذربایجان مسیر کوچ این اقوام
CHEUNG
2
BRT
0
```


## [2026-10-15T02:50:19.753Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -a -n -B2 -A3 'θrap\\|Orap' CHEUNG.txt | cut -c1-300",
 "description": "Check Cheung hits for θrap"
}
```


### [2026-10-15T02:50:20.172Z] TOOL RESULT

```
25734-
25735-
25736:396 *Orap/tarp 
25737-
25738-
25739-(+ *abi-) Pres.: IND. 3sg. BSogd. Btr’ynct, BSogd. Btr’ynctt, SUBJ. 3sg. BSogd. Btr'ync't; Impf.: IND. 
--
25759-
25760-
25761:*Orap/tarp ‘to be unsteady, move unsteadily’ 
25762-
25763-*MIDDLE PERSIAN: BMP spwk /sabuk/ ‘light, unsteady, shallow’ ( *0rap°) 
25764-
```


## [2026-10-15T02:50:21.748Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 25761,25800p CHEUNG.txt | cut -c1-400",
 "description": "Read Cheung *θrap entry"
}
```


### [2026-10-15T02:50:22.112Z] TOOL RESULT

```
*Orap/tarp ‘to be unsteady, move unsteadily’ 

*MIDDLE PERSIAN: BMP spwk /sabuk/ ‘light, unsteady, shallow’ ( *0rap°) 

*PARTHIAN: sbwk ‘light, easy’ (< MP) = DMMPP: 306a 

*NWIR: Kurd. terpin ‘to stumble’, NP sabuk ‘light(footed); unsteady; haste, 
despatch’, widely borrowed into: Abz. söbök, Nn. suvok, Qohr. sövök, Tr. sobok 
‘light’, etc. 

*NEIR: Oss. I. tælfyn/tælft (tælfyd), D. talfun/telft ‘to move to a place, to move 
[intr]; to fidget; to twitch [intr.], shake, be in trepidation’ (*trf-ia-), Sariq. turf-/turft 
‘to stumble, slip’, Pash. drabal ‘to shake, press down’ (LW ?), trap ‘leap, jump’ (< 
Indo-Aryan) 

*SANSKRIT: ? trap (med.) ‘to be ashamed, become shy’ (Ep.+). © Also in modern 
Indo-Aryan: Lah. trapp ‘leap, jump’, Khetr. trap, Hi. tarap ‘jump, throb’. = EWAia 
II: 674f. 

«PIE *trep- ‘to be in trepidation’ ? = LIV: 650 | Pok.: 1094 

*IE COGNATES: Gr. tpaneo ‘I press grapes’, Lat. trepido (denomin.) ‘I act in haste, 
scurry, trepidation; I feel anxious, apprehensive’, Lat. trepidus ‘apprehensive, 
anxious, behaving in an excited or agitated manner’, OCS trepets ‘trembling’, Lith. 
trapus ‘fragile, delicate’ 

*REFERENCES: EVP: 83, 22; EVS: 81a; Abaev, Slovar’ III: 255 f.; Hoffmann, Aufsätze II: 397; Werba 
1997: 415; Lecoq 2002: 602a, 637a, 654a (passim) 


*OrauH ? ‘to oppress’ 
*KHOTANESE: thurs- ‘to be oppressed’ || (+ *abi- or *ui-) ? LKh. buhurs- ‘to be 
afflicted, oppressed’ (SVK II: 54 ff.) © SGS: 43 


*Quai ? 397 


*CHORESMIAN: Swy- ‘to tyrannize, oppress’. > A different etymology was proposed 
for Chor. swy- by Henning 1958: 111, who derived it from a denom. *srausa-, Y Av.
```


## [2026-10-15T02:50:34.034Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 - <<'EOF'\np='build-512.py'; s=open(p).read()\nold='''            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt grep 'θrap'\", \"stance\": \"silent\", \"note\": \"No verbal root *θrap- in Cheung (adjectives only).\"}'''\nnew='''            CHEUNG_THRAP'''\nassert old in s; s=s.replace(old,new)\ns=s.replace('''e1_nodes = [''','''CHEUNG_THRAP = {\"src\": \"CHEUNG\", \"where\": \"p. 396 *θrap/tarp (CHEUNG.txt l.25761)\", \"stance\": \"supports\", \"note\": \"'*θrap/tarp ‘to be unsteady, move unsteadily’ — MIDDLE PERSIAN: BMP spwk /sabuk/ ‘light, unsteady, shallow’ ... NP sabuk ‘light(footed); unsteady; haste’ ... PIE *trep- ‘to be in trepidation’ ? Pok.: 1094' — sabuk only; čābuk not listed.\"}\ne1_nodes = [''',1)\nold2='''{\"src\": \"KNT\", \"where\": \"grep 'çapu', 'capuka'\", \"stance\": \"silent\", \"note\": \"Kent's lexicon has no such word; it is unattested in Old Persian inscriptions (Kent §: OP ç < IIr. *tr/θr confirmed by puça-).\"}'''\nnew2='''{\"src\": \"KNT\", \"where\": \"KNT_full.txt grep 'çapu', 'capuka'; l.2050 puça\", \"stance\": \"silent\", \"note\": \"No such word in Kent (unattested in the inscriptions); Kent's texts show OP puça 'son' (= Av. puθra-), illustrating OP ç < OIr θr.\"}'''\nassert old2 in s; s=s.replace(old2,new2)\n# add Cheung to node 1 and node 3 consulted\ns=s.replace('''\"ref_check\": [BQT1083],\n        \"consulted\": [\n            NYB_SAPUK,\n            {\"src\": \"BRT\"''','''\"ref_check\": [BQT1083],\n        \"consulted\": [\n            NYB_SAPUK,\n            CHEUNG_THRAP,\n            {\"src\": \"BRT\"''')\ns=s.replace('''\"note\": \"'čābuk [cʾpwk | N ~] agile''','''\"note\": \"'čābuk [cʾpwk | N ~] agile''')\ns=s.replace('''\"note\": \"'sabuk leicht, afgh. spuk ... phl. sapuk'; separately''','''\"note\": \"'sabuk leicht, afgh. spuk ... phl. sapuk'; separately''')\ns=s.replace('''Hübschmann keeps them apart.\"}\n        ]\n    },\n    {\n        \"id\": 4''','''Hübschmann keeps them apart.\"},\n            CHEUNG_THRAP\n        ]\n    },\n    {\n        \"id\": 4''')\nopen(p,'w').write(s)\nEOF\npython3 build-512.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-512.json >/dev/null && echo OK; grep -c CHEUNG_THRAP build-512.py; python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 512",
 "description": "Patch script, build JSON, validate, run check"
}
```


### [2026-10-15T02:50:35.185Z] TOOL RESULT

```
OK
4
nodes verified: 13/13
node verdicts: {'confirmed': 6, 'unverified': 1, 'transcription_suspect': 2, 'plausible': 2, 'disputed': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 12, 'not_checked': 4, 'partial': 1, 'contradicts': 2}
books consulted: {'supports': 26, 'silent': 9, 'contradicts': 2, 'partial': 6} | by book: {'WLD': 5, 'AHD': 5, 'NYB': 5, 'IEC': 4, 'KLN': 4, 'BRT': 3, 'CHEUNG': 3, 'HUB': 3, 'PHD': 2, 'POK': 2, 'SKT': 2, 'LEW': 1, 'KNT': 1, 'HRN': 1, 'MON': 1, 'ARY': 1}
```


## [2026-10-15T02:50:37.839Z] TOOL CALL #57: Bash

```json
{
 "command": "grep -a -n -i 'truncus' /home/sfmqrb/git/rishe-private/data/verification/sources/refs/LEW_1910.txt | head -3 | cut -c1-300",
 "description": "Grep Walde LEW for truncus"
}
```


### [2026-10-15T02:50:38.172Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:50:42.304Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 - <<'EOF'\np='build-512.py'; s=open(p).read()\nold='''\"where\": \"LEW_1910.txt\", \"stance\": \"silent\", \"note\": \"not separately quoted; WLD (by Walde) gives the trenq- view.\"}'''\nnew='''\"where\": \"LEW_1910.txt grep 'truncus'\", \"stance\": \"silent\", \"note\": \"No hit in the OCR text; WLD (Walde's comparative dictionary) gives the trenq- view.\"}'''\nassert old in s; open(p,'w').write(s.replace(old,new))\nEOF\npython3 build-512.py && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 512 | grep -c PROBLEM",
 "description": "Fix LEW note, rebuild, recheck"
}
```


### [2026-10-15T02:50:43.074Z] TOOL RESULT

```
0
```


## [2026-10-15T02:50:52.061Z] TOOL CALL #59: SubagentHandback

```json
{
 "message": "I wrote the page 512 file at /home/sfmqrb/git/rishe-private/data/verification/page-512.json. `verify_check.py 512` reports 0 PROBLEM lines and 13 of 13 nodes verified. Entry 2 (Trep 2 → Terp) is a redirect, so I skipped it.\n\n- **Roots:** 2 confirmed (Trenk/Tronkus = Pokorny trenk-1, page 1093; Trep 1 = Pokorny 1. trep-, page 1094).\n- **Nodes:** 6 confirmed, 2 plausible, 2 disputed, 2 transcription_suspect, 1 unverified.\n\n**Disputed:**\n- **Trep 1, Pahlavi node, čâpŭk; sapŭk:** sapūk (from Old Iranian *θrapu-ka-) is correct. čāpūk can't come from *θr-. Mo'in's footnote at Borhan p. 607 derives it from a separate Old Iranian *čāpu-ka-, and Wiktionary links it to Old Armenian čep \"haste\". Nourai merged two of Mo'in's footnotes.\n- **Trep 1, Persian node, čâbok / sabok:** the same problem one step later. sabok is correct (Nyberg, Cheung *θrap-, Mo'in p. 1083), but čābok does not belong to this root.\n\n**Transcription suspect (both are misprints in the book; the JSON matches the printed page):**\n- **Trenk, Latin node, \"trancus\":** the Latin word is truncus. Separately, Watkins/AHD puts truncus under terə-2 (as Nourai's own note says), Mann keeps it apart and Wiktionary calls it obscure.\n- **Trep 1, Old Persian node, \"čapu-ka\":** Mo'in and Nyberg both write *çapu-ka- (ç is the Old Persian outcome of θr, which gives Middle Persian s-). The book uses č and drops the asterisk that marks it as a reconstruction.\n\n**Extraction errors:** none. The empty double-bordered box in the Trenk chart (node #2, ‼UNCLEAR) really is blank on the printed page. I marked it unverified because no Persian descendant of Avestan θraxta- is known.\n\n**Files added for audit:**\n- Mo'in footnotes read from the page images: data/verification/sources/refs/ocr/BQT/607.vision.txt and 1083.vision.txt, each with a cropped .jpg beside it.\n- The book page image: data/verification/sources/refs/ocr/BOOK/512.png.\n- 8 archived Wiktionary pages, saved with fetch_source.py."
}
```


### [2026-10-15T02:50:52.371Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
