# Verification process log — verify-page-531


## [2026-10-16T05:13:01.926Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 531 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-531.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-531.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-531.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 531` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:01.995Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:06.280Z] TOOL CALL #1: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md; echo ====; cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-531.txt; echo ====; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-531.json",
 "description": "Read instructions, chart, and source JSON"
}
```


### [2026-10-16T05:13:06.916Z] TOOL RESULT

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


## [2026-10-16T05:13:10.558Z] TOOL CALL #2: Bash

```json
{
 "command": "sed -n '/Scanned references/,/Wiktionary\\*\\* (en.wiktionary/p' /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md",
 "description": "Read truncated instructions middle"
}
```


## [2026-10-16T05:13:11.504Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-531.txt; echo; echo ======; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-531.json",
 "description": "Read chart text and source JSON"
}
```


### [2026-10-16T05:13:11.895Z] TOOL RESULT

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


### [2026-10-16T05:13:12.062Z] TOOL RESULT

```
Exit code 1
=== PDF page 531 (book page 501) ===
--- entry 0 ---
ROOT [Indo-European] Wegh, Waq, Wag : to go, carry  (refs POK:1119)
#1 (parent #0) [Avestan] refs=POK:1119 | vaz : fly ; vaza 1 : a bird, hawk ; pairi-vaza : fly around ☞Per 1 ; vaza 2, vâzišta : travel ; vazya : load
  #2 (parent #1) [Persian] refs=BQT:217,391,2279; MON:4949 | bâz «باز ۲» : hawk, falcon ; parvâz «پرواز» : flight ; vazîdan «وزیدن» : to blow (wind) | extra: باشه ، واشه
#3 (parent #0) [Avestan] refs=POK:1119 | vašta 2 : curved ; vaštar : load carrying animal ; uždar, uždri : carrier
#4 (parent #0) [Latin] refs=AHD | vehere : to carry ; vectus : carried ; con-vexus : carried to a point, curved
  #5 (parent #4) [English] refs=None | vehicle ; vector ; convection ; convex
#6 (parent #0) [Germanic] refs=AHD | wegaz : course of travel ; wigan : to carry a load
  #7 (parent #6) [English] refs=None | way ; away ; always ; wagon ; wave 2 ; Norway ; weigh ; weight
--- entry 1 ---
ROOT [Indo-European] Wěğo : lizard?  (refs IEC:1499)
#1 (parent #0) [Avestan] refs=IEC:1499 | vazaghâ : lizard, frog
  #2 (parent #1) [Persian] refs=IEC:1499; BQT:2278; HRN:242; MON:5018 | vazağ «وَزَغ» : frog ; vazağeh «وزغه» : a small lizard | extra: وزق ، وزک
--- entry 2 ---
ROOT [Indo-European] Wegw, Ugw, Uks / Uksen : wet / to make wet, inseminate  (refs POK:1118)
#1 (parent #0) [Avestan] refs=POK:1118; KLN:1106; SYN:153 | uxšan : ox, bull, inseminating animal
#2 (parent #0) [Germanic] refs=AHD | uhsôn : ox
  #3 (parent #2) [English] refs=None | ox
#4 (parent #0) [Latin] refs=AHD | hŭmĕre : to be wet
  #5 (parent #4) [English] refs=None | humid ; humor

(eval):1: ===== not found
```


## [2026-10-16T05:13:17.352Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/extracted/batch/page-531.json; ls data/verification/ | tail -5; cat data/verification/sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','BQT','MON','HRN','KLN','SYN','AHD','WLD','BRT','HUB','ARY','SKT','WEB','FSD','KNT','PHD','NYB','CHEUNG']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"",
 "description": "Read source JSON, source matrix, refs info"
}
```


### [2026-10-16T05:13:17.832Z] TOOL RESULT

```
{
  "pdf_page": 531,
  "book_page": 501,
  "entries": [
    {
      "root": {
        "name": "Wegh, Waq, Wag",
        "lang": "Indo-European",
        "refs": "POK:1119",
        "gloss": "to go, carry"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1119",
          "words": [
            {"translit": "vaz", "gloss": "fly", "script": null},
            {"translit": "vaza 1", "gloss": "a bird, hawk", "script": null},
            {"translit": "pairi-vaza", "gloss": "fly around", "script": null, "see": ["Per 1"]},
            {"translit": "vaza 2, vâzišta", "gloss": "travel", "script": null},
            {"translit": "vazya", "gloss": "load", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:217,391,2279; MON:4949",
          "words": [
            {"translit": "bâz", "gloss": "hawk, falcon", "script": "باز ۲"},
            {"translit": "parvâz", "gloss": "flight", "script": "پرواز"},
            {"translit": "vazîdan", "gloss": "to blow (wind)", "script": "وزیدن"}
          ],
          "script_extra": "باشه ، واشه",
          "note": null,
          "quote": {
            "text": "پس اندر دوان هفتصد باز۲ دار - ابا واشه و چرخ و شاهین کار",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1119",
          "words": [
            {"translit": "vašta 2", "gloss": "curved", "script": null},
            {"translit": "vaštar", "gloss": "load carrying animal", "script": null},
            {"translit": "uždar, uždri", "gloss": "carrier", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "vehere", "gloss": "to carry", "script": null},
            {"translit": "vectus", "gloss": "carried", "script": null},
            {"translit": "con-vexus", "gloss": "carried to a point, curved", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "vehicle", "gloss": null, "script": null},
            {"translit": "vector", "gloss": null, "script": null},
            {"translit": "convection", "gloss": null, "script": null},
            {"translit": "convex", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "wegaz", "gloss": "course of travel", "script": null},
            {"translit": "wigan", "gloss": "to carry a load", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "way", "gloss": null, "script": null},
            {"translit": "away", "gloss": null, "script": null},
            {"translit": "always", "gloss": null, "script": null},
            {"translit": "wagon", "gloss": null, "script": null},
            {"translit": "wave 2", "gloss": null, "script": null},
            {"translit": "Norway", "gloss": null, "script": null},
            {"translit": "weigh", "gloss": null, "script": null},
            {"translit": "weight", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Wěğo",
        "lang": "Indo-European",
        "refs": "IEC:1499",
        "gloss": "lizard?"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "IEC:1499",
          "words": [
            {"translit": "vazaghâ", "gloss": "lizard, frog", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "IEC:1499; BQT:2278; HRN:242; MON:5018",
          "words": [
            {"translit": "vazağ", "gloss": "frog", "script": "وَزَغ"},
            {"translit": "vazağeh", "gloss": "a small lizard", "script": "وزغه"}
          ],
          "script_extra": "وزق ، وزک",
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Wegw, Ugw, Uks / Uksen",
        "lang": "Indo-European",
        "refs": "POK:1118",
        "gloss": "wet / to make wet, inseminate"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1118; KLN:1106; SYN:153",
          "words": [
            {"translit": "uxšan", "gloss": "ox, bull, inseminating animal", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "uhsôn", "gloss": "ox", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "ox", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "hŭmĕre", "gloss": "to be wet", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "humid", "gloss": null, "script": null},
            {"translit": "humor", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
.rw-r--r--   40k sfmqrb 14 Oct 22:50  page-514.json
.rw-r--r--   22k sfmqrb 14 Oct 22:47  page-515.json
.rw-r--r--   36k sfmqrb 14 Oct 22:51  page-516.json
.rw-r--r--   32k sfmqrb 14 Oct 22:48  page-517.json
.rw-r--r--   20k sfmqrb 14 Oct 22:48  page-518.json
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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
CHEUNG null
```


## [2026-10-16T05:13:23.356Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','BQT','MON','HRN','KLN','SYN','AHD','BRT','WLD','ARY']:\n  v=d[k]; print(k, {x:v.get(x) for x in ['local_file','page_offset','lookup_hint']})\n\"; python3 -c \"\nimport json;d=json.load(open('data/verification/page-518.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:5000])\"",
 "description": "Show ref lookup hints and example output"
}
```


### [2026-10-16T05:13:23.710Z] TOOL RESULT

```
POK {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt', 'page_offset': 'POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config"}
IEC {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt', 'page_offset': 'TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root."}
BQT {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)"}
MON {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks)."}
HRN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."}
KLN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."}
SYN {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line."}
AHD {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.)."}
BRT {'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt', 'page_offset': 'Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops."}
WLD {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'], 'page_offset': 'Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).', 'lookup_hint': "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP."}
ARY {'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'], 'page_offset': 'printed page = pdf page + 1', 'lookup_hint': "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image"}
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
     "where": "line 23803 s.v. Begum",
     "stance": "supports",
     "note": "'Arab. um, umm, mother'."
    },
    {
     "src": "AFM",
     "where": "AFM.txt grep 'ام غیلان|أم غيلان'",
     "stance": "silent",
     "note": "Addi Shir lists Persian loans into Arabic; umm and umm ghaylān are native Arabic, not listed."
    },
    {
     "src": "MON",
     "where": "vajehyab.com/moein/مغیلان",
     "stance": "supports",
     "note": "'امُ غیلان، درختچهٔ خاردار که در بیابان‌ها می‌روید' [ع.]"
    }
   ]
  },
  {
   "id": 2,
   "lang": "Persian",
   "words": "omm; ommî; moğîlân",
   "verdict": "plausible",
   "derivation": "omm أمّ (pl. ommahât أمّهات) is a learned Arabic loan in Persian, used beside native mâdar (e.g. omm-ol-ketâb). moğîlân مغیلان is Arabic umm ghaylān with the initial vowel lost and the two words fused (umm-ghaylān > mughaylān > Pers. moğîlân, with the Persian î for Arabic ay); Mo'in glosses it 'ام غیلان, a thorny desert shrub' [ع.], and Hafez's 'خار مغیلان' is the classic attestation. ommî أمّی 'il
```


## [2026-10-16T05:13:43.500Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'lemma: (u̯eĝh|ueĝh|u̯eg|ueg|uks|u̯ē̆ĝ)' POK_full.txt | head; grep -n -B2 -A40 'lemma: u̯eĝh-' POK_full.txt | head -120",
 "description": "Find Pokorny entries for weǵh- and related"
}
```


### [2026-10-16T05:13:43.826Z] TOOL RESULT

```
88897:Root / lemma: ueg- 
88931:Root / lemma: uegh- 
89047:Root / lemma: ueg- 
89089:Root / lemma: ueg"- : ug"-, ulcs-
```


## [2026-10-16T05:13:45.822Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 88931,89140p POK_full.txt",
 "description": "Print Pokorny uegh- and uegw- entries"
}
```


### [2026-10-16T05:13:46.118Z] TOOL RESULT

```
Root / lemma: uegh- 

Meaning: to move, carry, drive 

Note: a zero grade ugh- on\Y in Aryan and probably also in Alb. 

Material: Old Indie i/a/7a//" leads, travels, zieht, fijhrt heim, heiratet', also " flows ' and 

"allows flow', Aor. a- i/5/rs-5/77 (participle udha-, in addition neologism Ohati^ pushes, 

wheels, slides, throngs', Leumann IF. 57, 221); common Old Indie -gh- > -ks-: Avestan - 

gh- > -XS-, -z- 

Avestan i/aza///" leads, zieht, flies' (participle vasta-, wherein 5/instead of -zo'- after 

Partizipien from nicht auf Aspirata auslautenden Wzln.); Old Indie i/a/75y5//"er allows 

fijhren', 1/5/75/75- "fiJhrend, fahrend', n. "das FiJhren, Fahren, ship' (zero grade vahana- 

"fijhrend, bearing, carrying', n. " draft animal, cart, ship'), Avestan atra-vazana- 

"Feuerwedel' (compare die Germanic Celtic /7oformations); Old Indie vahftra-v\. "vessel, 

ship' (: Latin vehiculum). Old Indie 1/5/75- "fahrend, fijhrend' (= Slavic i/ozb " cart '), 1/5/75- 

m. "shoulder of Jochtieres', vahat-i. "river, vessel', 1/5/7/5- "zum Fahren suitable ', n. 

"vehicle, Tragsessel, couch, bed, place for resting ', Avestan vazya-u. "load, Tracht' (= Old 



Saxon wiggu. "horse'), Old Indie vodhar- 'fahrend, fijhrend', m. "Zugpferd, Zugochs; 
HeimfiJhrer eines Madchens; Lasttrager', Avestan vastar-' draft animal ' (= Latin vector), 
next to which with zd vazdra-'the vorwarts brings ', say-uzdri- EN actually "dessen female 
Zugtiere dappled, dotted, spotted are' {*uzdni. to *uzdar-)\ Old Indie 1/5/75- 'fiJhrend, 
bearing, carrying', m. ' draft animal, vehicle', Avestan vaza- "fahrend, fliegend', m. "Ziehen, 
pull, draft animal ' (: Gothic wegs). Old Indie vahistha-, Avestan i/az/5/5- "the at best 
vorwartsbringt'; Old Indie vahas- "fahrend' (: £X0(; n.), vahas-n. "vehicle, das die Gotter 
herbeifijhrende laudation ', Avestan i/aza/7- "fahrend, fiJhrend'; 

gr. Exeacpiv apijaaiv Hes., pamphyl. Fexstw "er soil bringen', Cypriot eFe^e "braehte dar', 
oxoq n. " cart ', (6- instead of £- after) oxoc; m. " cart ', oxsw "lead, guide', oxsopai "let me 
bear, carry or drive, reite', aiyi-oxoc; "die Aegis schwingend', Yair|-oxo(; (hom.), yaia-oxoq 
(Doric), YaiaFoxo(;(lak.) "the die Erde heiratet' (Beiw. of Poseidon, Borgeaud KZ 68, 222), 
6x£t6(; m. 'gully, canal, water pipe ', oxsteuu) "leite Wasser in a gully, a canal'; 6xA£U(; " 
lever' (: Old Icelandic i/a^/"Huhnerstange'), oxAsu), oxAi^u) "bewege fort, rolle orwaize 
fort'; 

alb. vjedh 'steaV; zero grade probably alb. udhe'yNay, journey; law - instruction ', 
whereof with formants -ra perhaps also i/Ae "bridge' {*u6^-ra); 

Note: 

Wrong etymology because alb. ura' bridge ' derived from a truncated gr. yscpupa 
{*gephura) " bridge ', Armenian ijunlnLp^ kamourg^ bridge '. Also alb. udhe^\Nay, journey' 
did not derive from Old Indie participle udha- "lead' but from gr. 656i; , n (ou56(; once in 
Hom., Od.17.196): I. "of Place, way, road', 
see Root / lemma: sed- : to sit. 

Latin veho, -ere, vexi{: Old Indie avaksat. Old Church Slavic i/esb Aorist), vectum 
"drive, guide, lead, bear, carry, bring' (in addition probably also con-, de-, sub-vexsus), 
Umbrian arveitu, arsueitu, arueitu^ to conduct, carry, convey, bear, bring, etc., a person 
or thing to a place; and pass., to be carried, to ride, to come to a place upon a horse, in a 
carriage, ship, etc.. ', kuveitu^ he/she shall carry together, collect, store ', Latin vehisi. " 
cart, Fuhre, Fuder', i/e/7e/77e/7s actually "*einherfahrend', hence "violent, stormy, hot 
tempered, stormy', vectis' lever, Hebebaum, crowbar ', originally abstract noun *"das 
Heben, Fortbewegen', vectTgalis "to den tributes an den Staat belonging' (places ein 
*vectis\v\ the meaning "das Herbeibringen, Ablieferung' ahead), i/ec//^5/ "tribute, tax an 
den Staat, Gefalle, tax', Ke/d>r "quick, fast' {*uegh-slo-), i/e/es"Leichtbewaffneter'; veia 
"plaustrum'; 



Old Irish fen 'k\nd of cart ' {*uegh-no-, compare Old Indie vahana-av\6 Old High German 
wagan) = cymr. gwa/n6s., abrit. cc»i///7/7i/5"Sichelwagen', (common Celtic -ns-, -nt- > -nn-), 
cymr. a/77M/5//7"herumfuhren', a/wa//7 'guide, lead', cywa/n'6rwe'; Old Irish fee/?/ 'journey, 
time, mal', mcymr. gweith, ncymr. gwa/fh^\Nork, work, mal', corn, gweth, gwyth^maX, 
acorn. gueid-uur^o'Q\iey!, bret. gwez, gweach ' maV , gall. PN Vectirix, Vecturius, 

(joVc\\c gawigan^moye, shake'. Old Icelandic vega^xwove, swing, heave, life, wiegen'. 
Old High German wegan^s\c\\ bewegen, wiegen (Modern High German bewegen, 
erwagen, wagen, wiegen). Old Saxon wegan'wagen, consider'. Old English n/e^a/? 'bring, 
guide, lead, wagen', Gothic ^an/a^ya/? 'move, shake' (= 6x£U), Slavic voz/tr, lengthened 
grade Old Indie vahayati) = Old High German weggen^move'; iterative Old Icelandic vaga 
'hin - and herbewegen'. Old English wag/an ' s\c\r\ bewegen'. Old High German wagon 
'sich bewegen, vibrate ' (wherefore as post-verbal Old High German n/a^a 'movement' 
Wissmann, Nom. postv. 1, 14); Gothic wigs. Old Icelandic vegr. Old High German Old 
Saxon Old English M/e^'way';Old Icelandic vigg. Old Saxon wigg. Old English wicgu. 
'horse' (= Old Indie vahya-); Old Icelandic vett, vaetti. ' weight ' (= Latin vectis). Old 
English w/Mn. 6s., Middle High German gew/hten. 6s.; 

Old Icelandic vggt ' lever', PI. vagar' sled ', vggur{an6 vagir) f. PI. 'barrow, bier'; Old 
High German Old Saxon waga^ cradle ', Old Icelandic vagga6s.. Old High German wiga^ 
cradle '; Old High German wagan. Old English wsegn. Old Icelandic vagn^ cart ' (ablaut, 
with Irish fen); Old Icelandic vaglxw. 'Hahnenbalken', Norwegian 'HiJhnerstange' 
('*Tragstange', compare formal 6xA-£uc;, -£U)); 

Maybe alb. i//g 'hand-barrow' 

Gothic M/egs'Wogenschlag', PI. 'Wogen', Old Icelandic vagr^sea, Meeresbucht', Old 
High German wag^ surge ', Old Saxon n/ag'hochflutendes water'. Old English waeg^ 
surge '; Old Icelandic vag^ lever. Wage, weight ', Old High German waga'Wage, weight, 
risk ' (Middle Low German Middle High German wagen^\n die Wage lay, place, aufs 
Geratewohl dransetzen, venture, n'sK), Old Saxon waga^\av\x\ Old English w^g, waege 
'Wage, a certain weight '; 

Lithuanian vezu, i/ez// "drive', vezimas^ cart', i/eze'Wagengeleise', p/'ai/eza 
'Wagengeleise'; Old Bulgarian vezg, i/esZ/'vehere', veslo^ ru66er ' {*uegh-s/o-), vozb' 
cart', vozg, i/oz/// "drive, guide, lead'; also Old Russian i/eza 'Wohnwagen, tower'. 

References: WP. I 249 f., WH. II 742 f., 744, Trautmann 356 f., Vasmer 1, 178 f. 
Page(s): 1118-1120 



Root / lemma: ueg- 

Meaning: fresh, strong 

Grammatical information: stative verb uege- 

Material: Old Indie vaja- m. " power, quickness, contest, price of the battle, cut-throat price 

', vaJayati^reQi an, treibt an, lauft urn die Wette'; vajra-m. 'thunderbolt, club, mace, joint' = 

Avestan vazra- 'club, mace, joint'. Old pers. vazrka-, npers. buzurg^b\Q, large', derivative 

from *uazarn.; 

Latin veged, -ere 'bin alert, awake, smart', trans, 'errege', i//g//' watchful, wakeful' and 
'Wache, Wachter' {*vegilis), thereafter vigilare^ awake sein'; vegetus^ strenuous, alert, 
awake, smart'; 

Maybe from Latin ex v/g/7are der'wed Italian svegliare= alb. zgjoj^ wake up' (common alb. 
9l->9J-)- 

Alb. vigjeloj^ guard' a Latin loanword. 

Gothic gawaknan 'wake up, arouse' = Old Icelandic vakna ds., Old English wsecnan 
(preterit woe), waecnian' be born '; Old Icelandic vakinn' awake'; Kaus. Gothic uswakjan' 
awaken ' (besides the abbreviation = Old Indie vajayati) = Old Icelandic vekja, Old High 
German etc. wecchan 'waken, arouse, revive'; Zustandsverbum Germanic *waken\n: 
Gothic wakan. Old Icelandic vaka {schw. Verb) 'watch'. Old English wacian. Old Saxon 
wakon. Old High German wahhon, wahhen 'watch' Old High German wachal' awake'. 
Old English wacol{*wakala-). Old Icelandic vgkull{*wakula-: Latin vigil); Gothic wokainsi. 
'das Wachen'; Old Icelandic i/a/r/". Old English wacor. Old High German wachar, wakar' 
active, fresh, wackei* (formal = Old Indie vajra-, Avestan vazra-); Old Icelandic vaskr'a\ert, 
awake, smart, agile' {*vak-ska-); perhaps also Old High German waiis ' sharp' . 

Tocharian AB wasir' lightning '; 

References: WP. I 246 f., WH. II 741. 

See also: compare aueg- aug- above S. 84 f., from dem ueg- barely to separate is. 

Page(s): 1117-1118 

Root / lemma: ueg"- : ug"-, ulcs- 

Meaning: wet; to irrigate; ox (?) 

Material: Gr. uYp6(; 'humid, wet, fluid'; Latin Jiz/io'^s 'humid, wet, damp' (out of it udus, 

whereof OiTgo'd\e natijrliche dampness of Bodens'), uvor, -oris' dampness, damp ', 



uvesco, -e/"© "humid, wet become, sich betrinken', Ji/e/7s "humid, wet, damp' (place a 
*Ji/c»sfrom *J^"'c»-s ahead); umeo, -eAe "humid, wet sein', umor^ dampness ', umecto 
"befeuchte' (based on auf *ug"'smos)\ Middle Irish fuar urine ' {*uog"-lo-)\ 

Old Icelandic vgkr{f\Vk. vgkuan) "humid, wet', vgkvixw., vgkvat " damp ', wherefore Old 
Icelandic v0kva, i/e/rA/a "(blood) shed, flow let', vgkt {*vakvd) "offene (nasse) place in 
Else', Middle Low German wakei. "hole in Else', Dutch M/a/r"humid, wet, damp', engl. 
(from dem Nord.) bya/re"Kielwasser'; 

5-Erweit.: Old Indie ^/rsa// "befeuchtet, besprengt', Avestan i/A'SKe///"spruht' (of water 
and fire); common Old Indie -gh- > -ks- : Avestan -gh- > -xs- 

in addition (with the same Verhaltn. as Old Indie vrsan- "virile', Latin verres:0\6 Indie 
i/a/'S5-/77"rain', s. uer- "feuchten') Indo Germanic ulcsen-^ buW, Tiermannchen' in: Old Indie 
uksam., Avestan uxsan- "bull' (in addition? fem. *uk"sdr^6\e Besprengte' > Latin uxor 
"wife'); cymr. ych^ox' (= Indo Germanic *uk"sd, urbrit. *uchu> -/" with umlaut yc/?), PI. 
mcymr. ychen, ncymr. ychain, bret. ouhen, oc'hen, corn. 0/75/7 "Ochsen', Middle Irish oss 
"deer'; PN Os-C5/'"hirschliebend', Demin. 0/ss//7"0ssian'; Gothic auhsus {Gen. PI. 
auhsne). Old Icelandic oxi. Old English oxa. Old High German Old Saxon 0/750 "ox'; 
Tocharian B oAso "rother, cattle, bull'. 

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

latter probably previously through imitation from vyath-: 1////7- "waver'); i//o'o'/7a-"durchbohrt, 

durchsehossen', /7/n//O(0'/7a"auseinanderstehend, voneinander apart, separated', vindhate
```


## [2026-10-16T05:13:55.761Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^wegh-|^wegw|^ugw|^wegʷ|^uksen|^ug-' AHD_watkins1985.txt | head; n=$(grep -n -E '^wegh-' AHD_watkins1985.txt | head -1 | cut -d: -f1); sed -n \"${n},$((n+45))p\" AHD_watkins1985.txt",
 "description": "Find AHD Watkins wegh- entry"
}
```


### [2026-10-16T05:13:56.106Z] TOOL RESULT

```
Exit code 1
sed: -e expression #1, char 1: unknown command: ','
```


## [2026-10-16T05:14:01.005Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'wegh|uksen|ugw|wegw' AHD_watkins1985.txt | head -20",
 "description": "Grep AHD for root names"
}
```


### [2026-10-16T05:14:01.396Z] TOOL RESULT

```
173:It was probably not long before the disper- sal of the Proto-Indo-European community that the use of the wheel and wheeled trans- port was adopted. Despite the existence of widespread word families, most terms relat- ing to wheeled vehicles seem to be metaphors formed from already existing words; they are not primitives or primary vocables. So the word for AXLE (aks-) may mean simply “a pivotlike juncture”; the NAVE or hub of the wheel (nobh-) is the same word as NAVEL. This is clearly the case with WHEEL itself, where the widespread *k(e)-k“l-o- is an ex- pressive derivative of a verb (k"el-') meaning “to revolve or go around.” Other words for “wheel” are dialectal and again derivative, like Latin rota from a verbal root ret-, “to run.” A root wegh-, “to go, transport in a vehicle” (WAGON), is attested quite early, though not in Hittite. This evidence for the late appearance of the wheel agrees with archaeological findings that date the distri- bution of the wheel in Europe to the latter
1132:form *weg-slo- in Latin vélum, a sail, curtain, veil: VEIL, VELUM, VEXILLUM, VOILE; REVEAL. [Pok. weg- 1117.] weg-2. To be strong, be lively. 1. Suffixed o-grade form *wog-é- in Germanic *wakén in Old English *wacan, to wake up, arise, and wacian, to be awake: WAKE}. 2. Suf- fixed o-grade form *wog-no- in Germanic *waknan in Old English wecnan, wecnian, to awake: WAKEN. 3. Germanic *wakjan in Old English weccan, to be awake: WATCH. 4. Germanic *wahtwo in Old High Ger- man wahta, watch, vigil, in dialectal German beiwacht, supplementary night watch: BIvouac. 5. Germanic *waht- in: a. Old North French waitier, to watch: WAIT; b. Middle Low German wachten, to watch, guard: WAFT. 6. Suffixed (causative) o-grade form *wog-eyo- in Latin vegére, to be lively: VEGETABLE. 7. Suffixed (stative) form *weg-é- in Latin vigére, to be lively: vicor. 8. Suf- fixed form *weg-eli- in Latin vigil, watchful, awake (> vigilare, to watch, be awake): VEDETTE, VIGIL, (VIGI- LANT), VIGILANTE; REVEILLE, SURVEILLANT. 9. Suffixed form *weg-slo- in Latin véldx, fast, “lively”: VELOCITY. [Pok. weg- 1117.] wegh-. To go, transport in a vehicle. 1. Germanic *wegan in Old English wegan, to carry, balance in a scale: WEIGH}. 2. Germanic lengthened form *wég-6 in Old English wég(e), weight, unit of weight: WEE. 3. Suffixed form *wegh-ti- in Germanic *wihti- in Old English wiht, gewiht, weight: WEIGHT. 4. Germanic *wegaz, course of travel, way, in Old English weg, way: WAY; ALWAYS, (Away). 5. Suffixed form *wogh-no- in Germanic *wag- naz, vehicle, in: a. Old English we(g)n, wagon: WAIN; b. Middle Dutch wagen, wagon: WAGON. 6. Suffixed o-grade form *wogh-lo- in: a. Germanic *waglaz in Old Norse vagl, chicken roost, perch, beam: WALLEYED; b. Greek okhlos, populace, mob (< “moving mass’): OCHLOCRACY, OCHLOPHOBIA. 7. Distantly related to this root are: a. Germanic *wag-, “to move about,” in (i) possibly Middle English waggen, to wag: wac! (ii) Old High German waggo, wacko, boulder rolling on a river- bed (> German Wacke, boulder): GRAYWACKE; b. Ger- manic *wéga-, water in motion, in Old Italian vogare, to row: VOGUE; c. Germanic *wig- in (i) Old English wicga, insect (< “thing that moves quickly”): EARWIG (ii) Middle Dutch and Middle Low German wiggelen, to move back and forth, wag: WIGGLE. 8. Basic form *wegh- in Latin vehere (past participle vectus), to carry: VECTOR, VEHICLE; ADVECTION, CONVECTION, EVECTION, INVEIGH. 9. Suffixed basic form *wegh-yd in Latin via, way, road: FOY, VIA, VOYAGE; CONVEY, DEVIATE, DEVIOUS, (ENVOI), ENVOY!, OBVIOUS, PERVIOUS, PREVIOUS, (TRIVIAL), TRIV- IUM, (vIADUCT). 10. Suffixed form *wegh-s- in Latin vexdre, to agitate (< “to set in motion”): VEX. 11. Prob- ably suffixed form *wegh-so- in Latin convexus, “carried or drawn together (to a point),” convex (com-, together; see kom): CONVEX. [Pok. vegh- 1118.] weg-. Wet. 1. Germanic *wakw-6 in Old Norse vdk, a crack in ice (< “wet spot’): WAKE?. 2. Suffixed zero-grade form *ug’-sm- in: a. Latin (hjiimére, to be wet: HUMECTANT, HUMID; b. Latin (hj)iimor, fluid: HU- mor. 3. Suffixed zero-grade form *ug’-ro- in Greek hugros, wet, liquid: HYGRO-. 4. Regarded by some as an extended form of this root (with the meaning “the impregnator”), but probably a distinct Indo-European word, is *uk”s-en-, bull, ox, in Germanic *uhs6dn- in: a. Old English oxa, ox: 0x; b. Old High German ohso, ox, in German Aurochs, aurochs: AUROCHS. [Pok. uweg#- 1118.] weg”h-, Also eug’h-. To preach, speak solemnly. Suf- fixed o-grade form *wog’h-eyo- in Latin vovére, to pledge, vow: VOTARY, VOTE, (VOTIVE), VOW; DEVOTE, (DEvouT). [Pok. ewegvh- 348.] wei-'. Also weie-. To turn, twist; with derivatives refer- ring to suppleness or binding. I. Form *wei-. 1. Germanic suffixed form *wi-ra-, *wé-ra- in Old English wir, wire: WIRE. 2. Probably suffixed Germanic form *wai-ra- in
1217:ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
1232:ALTER al-1 ALTERCATE al-1 ALTERNATE al-1 ALTHEA al-3 ALTHORN  ker-1 ALTIMETER al-3 ALTITUDE al-3 ALTO al-3 ALTOCUMULUS _al-3 ALTOSTRATUS _al-3 ALTRICIAL al-3 ALTRUISM al-1 ALULA aks- ALUMNUS al-3 ALVEOLUS aulo- ALWAYS wegh- ALYSSUM wikwo- AM es-
1268:AUNT amma AURA wer-2 AURAL! ous- AUREATE aurum AUREOLE aurum AURIC aurum AURICLE ous- AURIFEROUS aurum AURIFORM_ OUuSs- AURIGA 6s- AUROCHS wegW- AURORA aus-! AUSCULTATION oUuS-
1271:AUTOPSY OkW- AUXESIS aug-! AUXILIARY aug-! AUXIN aug-! AVAIL wal- AVAST  kel-3, past- AVATAR auc’, tera-? AVENGE deik- AVENUE gWa- AVER wéro- AVERT wer-3 AVIAN awi- AVIARY awi- AVIATION awi- AVICULTURE awi- AVIFAUNA awi- AVOCATION wekW- AVOID eu-2 AVULSE wel-4 AVUNCULAR awo- AWARE wer-4 AWAY wegh- AWE agh-1 AWKWARD apo- AWN ak-
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
1437:EACH [ik- EAGER! ak- EAR! ous- EAR2 ak- EARLY ayer- EARN! esen- EARNEST! er-! EARTH er-2 EARWIG wegh- EASE yé- EASEL asinus EAST aus-1
1464:ENTO- en ENTOMO- tem- ENTRAILS en ENTRAP der-1 ENTREPRENEUR ghend- ENTRESOL sel-1 ENTROPY trep-2 ENUMERATE nem- ENUNCIATE neu-! ENURESIS wers-2 ENVOI wegh- ENVOY! wegh- ENVY weid- ENZYME yeud- EO- aus-! EQOHIPPUS ekwo- EON aiw-
1479:EUTECTIC ta- EUTHANASIA dhwene- EUTHENICS gWhen-2 EUTROPHIC threph- EUXENITE xenos EVACUATE eu-2 EVADE wadh-2 EVAGINATE wag- EVANESCE eu-2 EVANGEL angelos EVAPORATE kwép- EVECTION wegh- EVENT gWa- EVENTIDE da- EVER aiw-
1536:FOY wegh-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1658:HUM kem-3 HUMAN dhghem- HUMANE dhghem- HUMBLE dhghem- HUMECTANT wegw- HUMERUS omeso- HUMID wegw- HUMILIATE dhghem- HUMILITY dhghem- HUMOR wegw- HUMUS dhghem- HUNDRED dekm HUNGER kenk-2 HUNKER keu-2 HURDLE kert- HUSBAND bheue- HUSSAR kers-2 HUSTINGS tenk-1 HUT (s)keu- HYATHODE sed-2 HYDATHODE wed-1 HYDATID wed-1 Hypra_ wed-! HYDRANT wed-! HYDRANTH andh- HYDRAULIC aulo- HYDRO- wed-1 HYDROCEPHALUS ghebh-el- HYDROMEL melit- HYDROUS wed-1 Hyprus_ wed-! HYENA sil- HYGEIA gWei- HYGIENE gWej- HYGRO- wegw- HYLOZOISM _hulé HYMEN  syil- HYMNODY wed-2 HYOSCINE si- HYPER- uper HYPERBOLA gWele-1 HYPERBOLE gWelg-1 HYPERBOREAN gWere-1 HYPERKINESIA kei-3 HYPERPNEA pneu- HYPHA webh- HYPNAGOGIC ag- HYPNO- swep-! Hypnos swep-! HYPNOSIS swep-1 HYPNOTIC swep-1 HYPO- upo HYPOCHONDRIA ghrendh- HYPOCORISM ker-3 HYPOGEAL gé HYPOPHYSIS bheue- HYPOPNEA pneu- HYPOSTASIS sta- HYPOSTYLE sta- HYPOTAXIS tag- HYPOTENUSE ten- HYPOTHERMIA gWher- HYPOTHESIS dhé-1 HYPROCRISY krei- HYPSO- upo HYSTERESIS ud- HYSTERIC udero- HYSTERO- udero- HYSTERON PROTERON per!, ud-
1683:INTRA- en INTRADOS dorsum, en INTRANSIGENT ag- INTREPID  trep-1 INTRINSIC en, sekw-1 INTRO- en INTRODUCE deuk-, en INTROIT el-1, en INTROMIT en, (s)meit(a)- INTRORSE en, wer-3 INTROSPECT en, spek- INTROVERT wer-3 INTRUDE treud- INTUITION teu- INTUMESCE teue- INTUSSUSCEPTION en, kap- INULIN wel-3 INUNCTION ongw- INUNDATE wed-! INURE op-! INVADE wadh-2 INVAGINATE wag- INVALID! = wal- INVALID2  wal- INVEIGH wegh- INVEIGLE okw- INVENT gWa- INVERT wer-3 INVEST wes-4 INVETERATE wet-2 INVOKE wekw- INVOLVE wel-3 INWARD wer-3 IODOPSIN  okw-
1952:OBEY au-5 OBFUSCATE dheu-1 OBITUARY el-1 OBJECT! yé- OBJURGATE ag-, yewes- OBLAST epi, wal- OBLATE! tele- OBLIGE leig-1 OBLITERATE deph- OBLIVION lel- OBLONG del-1 OBLOQUY tolkw- OBNOXIOUS nek-1 OBOE busk- OBSCURE (s)keu- OBSEQUIOUS sekw-1 OBSERVE ser-! oBsEss sed-1 OBSTACLE sta- OBSTETRIC sta- OBSTINATE sta- OBSTREPEROUS §strep- OBSTRUCT ster-2 OBTAIN ten- OBTECT (s)teg- OBTEST trei- OBTRUDE treud- OBTUND (s)teu- OBVERT wer-3 oBvious wegh- OBVOLUTE wel-3 OCARINA awi- OCCASION kad- occipuT kaput OCCLUDE kleu-3 occuLT kel-2 occupy kap- occur kers-2 OCELLUS okWw- OCHLOCRACY wegh- OCHLOPHOBIA wegh- OCTAD okto(u) OctTans okt6(u) OCTANT oktd(u) OCTAVE okt6d(u) OcTAvO okt6(u) OCTENNIAL at-
2024:ox wegw-
2081:PERQUISITE quaerere PERSE s(w)e- PERSECUTE sekw-1 PERSEVERE wéro- PERSIFLAGE swei-! PERSIST sta- PERSPECTIVE spek- PERSPIRE spirare PERSUADE swad- PERT wer-5 PERTAIN ten- PERTINACIOUS ten- PERTURB twer-1 PERVADE wadh-2 PERVERT wer-3 PERVIOUS wegh- PES ped-!
2129:PRECINCT kenk-! PRECIOUS per-6 PRECIPITATE kaput PRECISE kae-id- PRECLUDE kleu-3 PRECOCIOUS pekw- PRECURSOR kers-2 PREDATORY ghend- PREDECESSOR ked- PREDICATE delk- pRepicT deik- PREDOMINATE deme-1 PREEMPTION em- PREFACE bha-2 PREFECT dhé-1 PREFER bher-1 PREFIGURE dheigh- PREFIX dhig¥- PREGNABLE ghend- PREGNANT! gene- PREGNANT? per-5 PREHENSILE ghend- PREHENSION ghend- PREJUDICE deik-, yewes- PRELAPSARIAN leb-1 PRELATE telo- PRELECT leg-1 PRELIBATION [éi- PRELUDE leld- PREMATURE ma-1 PREMIER per! PREMISE (s)meit(@)- PREMIUM em- PREMONITION men-1 PREMORSE mer-2 PREMUNITION mel-3 PREPARE pere-! PREPENSE (s)pen- PREPONDERATE (S)pen- PREPOSITION apo- PREPOSTEROUS apo- PREPOTENT _poti- PREPUCE pu-! PREROGATIVE reg-1 PRESAGE sag- PRESBYOPIA per! PRESBYTER pert PRESCIENT skel- PRESCIND  skel- PRESCRIBE skribh- PRESENT! es- PRESENT? es- PRESENTIMENT sent- PRESERVE ser-! PRESIDE sed-! PRESS! per-5 PRESSURE per-5 PRESTIGE streig- PRESUME em- PRETEND ten- PRETERIT el-1!, per? PRETERMIT (s)melt(@)- PRETEXT teks- PRETZEL mregh-u- PREVAIL wal- PREVENIENT gWa- PREVENT gWa- PREVIOUS wegh- PREVISE weld- PREY ghend- PRICE per-6
2411:TRIO trei- TRIOECIOUS weik-1 TRIP der-1 TRIPEDAL ped-1 TRIPLE pel-3, trei- TRIPLEX trei- TRIPLOBLASTIC pel-3 TRIREME ere-1 TRISKELION skel-3 TRISMUS | strei- TRISOCTAHEDRON trei- TRITANOPIA ei- TRITE ter * TRITIUM trei- TRITONE trei- TRITURATE tere-1 TRIUMVIR trei-, wi-ro- TRIUNE oi-no- TRIVET ped-1 TRIVIAL wegh- TRIVIUM wegh- TROCAR kwetwer-, trei- TROCHAL dhregh- TROCHANTER dhregh- TROCHE dhregh- TROCHEE dhregh- TROCHLEA dhregh- TROCHOPHORE dhregh- TROGON tere-1 TROIKA trei- TROPE trep-2 TROPHALLAXIS al-1 TROPHIC- threph- TROPHO-  threph- -TROPHY threph-, trep-2 TROPIC trep-2 TROPO- trep-2 -TROPOUS  trep-2 TROT der-1
```


## [2026-10-16T05:14:11.185Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ *(vaz|vaš|vas|uzd|uxš|uxs|vazaγ|vazay|vazag)' BRT.txt | head -60",
 "description": "Grep Bartholomae for Avestan headwords"
}
```


### [2026-10-16T05:14:11.586Z] TOOL RESULT

```
2572:vaslrat.  —  6)  Statt  "/qm  drajim  . .  '/qm  riasJum.
11009:vas?iS  (^ur^masdähe^  mana^a  dä- fD.4.2.  B)imAwr.;  i)die Glieder  sind  nominal'';  a)  sie  folgen  sich unmittelbar:  pita  pu%rasea  .  .  iatarasüi ^■9-5i  —  pu^ra  (ND,)  ..  urvSxsayB k»r>s3spauaY.g.\a\  —  tum  akB  vahistasca ahi  YtJO.  29;  —  kanta  aiwyäxstaca Y.57.  IS  (s.  dagegen  Yt.;o.  103,  Sp.  567  u.);
13208:uzd3tä  äyese  yeHt  V,  22.  i  f.^'*;  _y.  3,  66.
13216:vascTt  :^ahya  ustarum  pairt  7'Tsprr  kujitayB
18045:vasnä  'num  Y. 50.  ii.
23126:vasa^layus  Y.  21.  3  iit  eine  angeichickte
23148:vaz-  2
23170:vaz-  3
23171:vaz-  vaii/m
23227:vazän  aslr  (s.  'arslay-  No.  i).  —  ')  S.  garay- No.  5.
23233:vazi-
23556:vastryä-
23616:vazäite  "der  vom  (stehend)  seinen  Wagen
23916:vas  sui,  vam  in  »am  hat  an,  Zaiti    ",  .  die   den  Kriegern  auch   in  der
24200:vasS  pasca^a  maadayasna  "waäajciV  (NP.) vXmmayanIa  (sd.)  V.  7, 40;  38'.
26575:uxsyeiti  stavanS'^  a%a  (sd.)'  nS  yS  dim staoiti  .  .  Y.  /o.  6 ;  —  yäha  mä  (näml. haotmni)  aparaät  saofyantB  slavqn^'*  Y, g.2;  —  fravasayö  ..  avat  avS  zixSnS- nhimna  (sd.)  ks  «J  stavSp''  kü  yasäite  ks ufyät  Yt. /j.49f.;5.  8;  —  asäunqm  ..fra- vasayS  staomi  sbayemi  ufyemi  Y.  77. 18; —  yS  ahm  staoiti  (s.  i.)  hS  mqm  staoiti yim  akurtm  H. /.  3;  3*;  —  *yavatä  %wa tnazdä  *slaoml*^  u/ya(sd.)cä  'V.43-8;  — at  fravaxsyS  vjspanam  mazishm  (sd.) s'tavas  aiä  yS  kudä  (sd.)ysi  &'«/r(NSni.)5> Y.45.6;  —  aj  vi  yazäi  slavas^  mazäa akuri  hadä  (sd.)  a/ä  Y,  jo.  4;  —  täis  va yasnäis  paitl  stavas^''  ayeni  mazda  asä "mit  diesen  Gebeten  euch  preisend  will ich  wieder  vor  euch  treten,  o  M.  und Äsa"  Y.jo.  9;  —  ycCkä  vi  yaz^mnas/a urväidyä  (sd.)  stavas^''  ayenX  paitl  Y. 34.6.  2)  Tenn.  techn.  fdr  das  Beten des  Asageht\s'''>:  yö  ahm  staoiti  hS..  "wer
```


## [2026-10-16T05:14:13.723Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 23140,23240p BRT.txt | cut -c1-400",
 "description": "Print Bartholomae vaz- section"
}
```


### [2026-10-16T05:14:14.045Z] TOOL RESULT

```
•  j.  vasö.yaoiui-  Adj.  (fem.  *nä-)  'der seine  Heimstätte  nach  Gefallen  hat  sva. der  wo  er  will  sich  ein  Heim  sucht,  be- reitet*: äbyS  dttiAhubyS  sndäA  (nämL  fra- vaiays)  ya%a  .  .  yBz}m  yesnyä  vakmyü 'nä  fra^arähwe  Yt  13.  34.  Verderbt: fsuyanttm  vasltfm  'nät  ttttam  .  .  Yt 10.  60.
•  j.  vasö.yäna-  Adj,  'der  nach  Wunsch, Gefallen,  Gunst  empfängt  oder  erweisf : 'n^m  vasö^aoyaoitim  Yt/o.  6o(?).  Ver- derbte Stelle.
•  ].  nitimanamcil  "vasö.vatam    Vyt  2J.
•  p.  vasiy  Adv.  'multum';  i)  'in  grosser Anzahl,  viel':  v  aniyaiciy  natbam  (sd.) kartam  X./.3;  7.  3,  Bh.d^.S;  —  «israw  (sd.) v  aväjaniy^  Äya*  . .  Bh, /.  13.  a)  mit demV.  i«i-;  a) 'zahlreich  werden':  utätaiy tauma  v  biy^  "und  dein  Geschlecht  möge zahlreich  werden"  Bh,  4- 10,  16.  ß) 'über- handnehmen, sich  ausbreiten':  pasavJ' draugJ'  dahyauvä  V  abavc^  
Zum  V.  vo!-;  eig.  'nach  Wunsch';  s.  Bthu IF.  /.  302  und  zV.  %ai4.\').  -  np.  ias,  nbal. gvas.  —  ')  Anders,  mit  der  Lesung  vasaiy, F0YKZ.jJ.ai,i4.  Falsch  FrMOller  WZKM. 6.  357.  7-  ZS7-
FrW.  g.  a.
"vasta    /td^rqm     kaitya     vaia"
dby  Google
vaz-  2
1386
J.   V
1  Vyt.  3ä,  40 :  liei  vasna,  %.  pauniS.-  1  'j/ata
•  j.  'vastra-  n.  'Kleid,  Gewand,  Kleidungs- stück': bawraitti  'rä  vatahüta  arydvT  Yt 5.  129;  —  spaSa  'rä  var^hatti  spaita Yljo.  136;  —  ?rf%ahm  zaranim  . . 'rSsca ktSh  bämanivä  Yt  i"],  14;  zit.  F.  5  (wo vüHrät  vaca  k°)\  —  'nm  . .  ubdanum V3  Izaimm  vä  V.  <?.  23;  —  sr%nm  'nm st»hrpa^aah»m  Vd.  20;20;  —  yänhuya- nam  ..  °ranam  Vd.2;  *I2;  —  hanhus :far
—  yat  masyS  astahmat  *T3m "'  N.Sj;  — (cvat)  *nä  *mt»ma  'rahe  aiwyästs  ratufris "was  an  Kleidung  muss  man  mindestens anhaben,  um  r.  zu  sein?"  N.  86;  —  *yei •ra  'nm  *aiwyän>Aay~!n/i  N.gj[?);'V.g.$3, , /Ä  1 9 ;  —  asp?nnS  'rahe  .  .  anasp»r»nö 'rahe  N.^r;  g6';  —  ma-^ns  apaspayat  'ra Ytig.56;  V.p.  49,  6.2T;  —  aaf  ..  US tanttm  snayalta  us  *'rä^>  Y.j.  54
—  kat  ta  'ra  yaoidayan  arthfn  V.  7.  1 1 ; Vd.  /2,  20;  —  yim  antar»  'nm  frajasat Csd.)  V.  16.  16;  —  spis  (sd.)  . .  yim  . . nizgaakwti  'ra  i/astrakva  V.  17.  3;F.&
KompE.;  AbUit.  —  Zum  V.  ivoJi-,  —  »i. västra-  n.,  mp.  vasir,  —  Pü. :  vaslrai,  — 0  Gdn.  in  der  NA.  vermulet  väslrim,  vgl. No.  3.  Aber  P6.  vaslrai.  —  »)  Hdl.  västnm, aber  Pü.  vailrak.  —  J)  Hds.  'rät  (ebenso  V. 5-  56)-
•  j.  »vastra-  n.  'Fresse,  Maul,  Rachen': azSis  vilapahe  'r?m  N.  48.
Idg.  *nts-tn>-  *eig.  'womit  man  isst';  vgl.  afad, wiii;  mir./flr  'Essen'").  —  Pü.:  i^ar.  — ')  Vgl.  noch  Leumank  EtWb.  94  No.
•  j.  vastran-  n.  'Aufbewahrungsort  für Kleider,  Kleiderkammcr' :  spis  (sd.) .  .yim . . yaom  yavS.hva  nizgatikttUt  vastra  'rähva (LP.)"  V.77.3.
Ableit  aus  'vattro;  eig.  Adj.  'Kleider  ent- haltend'. Unsicher.  —  Pü.:  vasir  dän.  — <)  AuffülL  Foim;  s.  zu  sfii-  No.
•  j.  vastra'vant-  Adj.  'mit  Kleidern  ver- sehen': kö  nS .  .paiiijanäj  gaomata  tasla
mit  Fleisch  und  Kleider  spenden- der Hand"  Yt  13.  50.
ai.  vasiravarä-  Adj.
•  j.  "vastrvi  a^ravana  (sd.)  Vd.  12. Vgl.  V.  S.  33  und  Bthl.  IF.  //.  125.
•  j-t  g-  vasna-  m.:  s.  unter  vasna-.
•  j.,  g.  vaz-  V.  'fahren'.  Praes.  2  vata-, 2ä(Pass.)  vazya-;  Perf  i  vavas-'^^  waos-; s-\oT.  I  vaS-,  va/-'\  —  PPfP.  vas'/a-''*;  Inf. vazaiöyäi,  vaote;  Absol.  vazfmmm,  vava- zärum.
1)  'fahren';  i)  Irans.;  a)  von  Zugtieren sva.  'ziehen*:  srao&m  ..yim  ..  aurvanlS .. vatmti  Y.57.  37;  Yt.  ;o.  68,  47,  77. 12;  — aurvants  . .  vazimna  yim  vohüm  sraohm Y. 57.29;  —  s.  noch  'vazäna-,  b)  vom Wind;  a'hra  pascaUa  vazaite  vätB  .  . varymca  maiy>mca  fyanhumta  avi  ('hin zu  . .')  asä  . .  YL<y,  33.  c)  vom  Fahrer, sva.  'lenken':  y&  *paourvS  väs
sva. 'einherziehen':  sp^)m..yS  mi  pasill£ vazaite  Yt,  14.  58;  —  aSru  pascalta  vao- zinm  (3PPrPfM.)^'  baohntg  iuhm.."Aort werden  sie  alsdann  einherziehen  .  ,"  Yt iff.6g.  2)  'fahren'  intrans.  von  jeder Art  gleitender  Bewegung  wie  'schweben, fliegen  (usw.)':  ti/trTm  . . yS  avavat  xhiOKifJf vazaite  avi  srayS  .  .  ya'ha  tiyris  ".  .  der so  rasch  dahinfährt  zum
dby  Google
1387
vaz-  3
vaz-  vaii/m
1388
mailim  trayanhü  vouruJiaiahe  "jene  Herr- 1 Uchkeit  .  .,  die  schwebt  inmitten  des Sees  .  ."  Yt5.42;  —  apasi  vazaile  arslis yqm  . .  "zurUclc  fliegt  der  Speer,  den  . ." Yt  10.  ao;  —  arltayasHl  .  .  va%>mna haia  hazubyS  Yt.  lo.  39;  39;  —  kasattrgm isunam  .  .  mainyavasä  vaantt  .  .  pat^nti ' Yt.  io.  119;  —  vlsptm  ä  ahmSl  yai  aHn (näml  tifrii)  paitLa
—  mtrriahe  .  .yS  vataite  MariayamnSfsd.} Yt.  14,  20;  —  päurvö  .  .  yai  dim  usca utdvanayai  (sd.)  . .  'hraitaonO  . .  hs  avaha (sd.)  vaeata  . .  *pailila  nmSmm  Yt.  5.  6 1  f. ;
—  rgnfyS  *vazainte  mats  (Sp.  11 13  u.) Y.  ;o.  19.  3)  'etwas  Jemandem  (Dat) zuflihren,  darbringen':  zaoHrä .  .yh  mävSya pasla  vatinti  (Pass,)"  ".  ,  die  mir  .  .  zu- gerührt werden"  Yt.  5.  95.  4)  'etwas  bei sich  führen,  zu  eigen  haben';  yim  (näml. arrumf)  va!ättte^'>  ahurinhs  valSnW  .  . lfm  val'aia''^  kava  iisa  yim  aspB  arsa baraili  Yt/4. 39.  S)  i)  
fravätai^A)  vasaiteW.^.^i; — yj  nlfi/.. mayä  vaoze  i^SViU.)''^  V.4S{7).  zu  2: nuit  hau  SS  vaote  (Inf.,  sd.)  .  .  lUSii  ahmat vaiata^'  V.48;  — yat..vastär3hs  ahmya (Sp.  398  u.)  nüit  vatyafite  jatSwhS  ahmya rtsit  JanyänU  "wenn  .  .  wenn  die  erfolg- reichen nicht  weiter  (zum  endgiltigen Sieg)  kommen,  die  geschlagenen  keine (endgiltige)  Niederlage  erleiden"  Yt. 
V.iJ.5.
mit  aiwi  intrans.  'herzufahren,  gefahren kommen':  ya'^a  avai  AvanxIaUpm  tarasca haram  .  .  fraia  aiti  aiwi^a  vataiU  Yt. JO.  118.
mit  avi  trans.  'hinfuhren  zu  — '  (Akk.): äptm  .  .  avi  nasBm  vas3hi  tum  yS  ahurS ".  .  das  Wasser  .  .  führst  du  es  hin  zum Leichnam  . ."  V.  j.  r6;  —  ati  nasttnt vasimi  (näml.  aptm)  V.5. 18.
mit  avi  und  us  intrans.  'auf  und  hinzu- fliegen': vayö  vä  Al  kjrifs^arS  avi  uz- vataite  (statt  Plur.)  FrW.  //.
mit  avi  und  Aam  intrans.  'sich  in  der
Fahrt  vereinigen  mit  — ,  einmünden  in  — ' (Akk.):  avi  tfm  avi  Aaniacaiti  (sd.)  avi t?m  avi  Aam.vataite  ifastraca  .  ,  Yt ig.  67.
mit  W^  intrans.  'herzufahren,  herzuge- fahren kommen  zu  — '  (Akk.):  sraohm  .  . yS..imat  iarhiarp  avazäiU'*''  Y.57.31.
mit  a  und  US  intrans.  'auffliegen  hin zu  — '  (Akk.):  3  tai  mtt^im  utvazaiU Aaca  .  .  V.J.  I".
mit  upa  I)  intrans.;  i)  'hinzu,  herzu- gefahren kovamea' : /rava/ayH ..yS  moüf rmmiit  myadinam  ,  .  upavasinU  ",  .  die mittenhinein  unter  die  Opferer  gefahren kommen"  Yty.  64;  —  para  äthi  vpa.- vatamtAa  ">  avi  nmSmm  *airyamanäi  V. 32.7;  —  upa.vazata"^  avi  nmätam  V. 22.  13;  Yt  10. 1 27.  2)  'hinfliegen,  hinge- flogen kommen  zu  — '  (Akk.) :  imrTyim  .  . upa
mit  US  trans.  i)  'nach  oben  fuhren, treiben'  (ohne  Obj.):  afi  utvazaiti"''  ä/s nivazaili  "'  afs  paiti.raScayciti  "das  Wasser treibt  (den  Leichnam)  nach  oben  . .  treibt (ihn)  den  Fluss  hinunter,  .  .  lässt  (ihn  an seichterStelle)!iegen"  V.5. 8.  2) 'heraus- fuhren, -holen,  befreien  aus  — ':  yS  htm (näml.  dainqm)  ,  .  usvazaf  Aaca  Mnüi'wyB (sd.)  Yt.  ;yioo.
mit /!»■/( :  s.  Inf.
mit  para  intrans.  'davon-,  wegfliegCD' : para  kamtrpiA  vazaile  mthrö.dru/qm  Vt. /0.37.
mit  fru  intrans.  i)  'vorwärts,  heran- fahren, hingefahren  kommen';  vom  Fahrer: frsvazaite  mi^rS  ,.  vUhm  srlntn  vavazS- mm  (sd.)  Yt.;o.i24;  —  ya^  mihr5 /ra- vazaite  avi  Aamayä  Yt.  10. 48;  99;  — mi^mm  .  .  y}  väSa  .  .  fravazaite  Aaca karh'an  yat  anzaAi  upa  karsvan  yat x'anirä^fm  Yt.  70,67;  133;  ~-  ^Wähn paskai  pravaz:nte  (näml.  fravasayd)  Yt. ',?■  39j  —
dahinfahren,  schweben,  fliegen':  /hJ  pourvS vSiqm  vazaiti  Yt  &  33 ;  —  liStrlm  .  .  yö . .  fravataitt . .  Yt.  A^.  3  5 ;  —  aat  tg  (näml. Stars)  riBrqm  fravaz^nti  Yty.  58;  — vayaiibya  . .  yB  pannTnS  fravazänte  (statt Du.)  Yt  10. 119.         3)  'sich  dran  machen
dby  Google
1389  vasa-
etwas  zu  tun'  (Inf.):  yat  aüe  ysi  mazda- yasna  bai^azäi  {%A.)  fravazSnte  V.  7. 36.
mit  nt  'nach  unten  führen,  treiben'  (ohne Obj.):  <fß  usvazaiH  (sd.)  . .  mvatatti  V.
5- 8-
ai.  vihati,  ukyäte  (Praet.  37,  Fass.]^  uhl,  vaksai; ; udhäh,  vähadhyai;  mp.  voiSlan  'dahin fahren', , rp.  i'.ijrH'fl« 'wehen',  afj.  po/ii/ 'fliegen' (Praes.  I vuzt],  sbal,  gvcaag,  ZDg.  vailmün  'laufen'.  — Pü. !  vaätan,  vazemlan;  s.  noch  No.  6  ff-  —  ' I)  Nur  im  Abiol.  —  '>  S  W  H;  »■  dagegen  • ai.  üijh^.  —  »  S  /a/  g.  Wertlos  Wilhelm  | Mus.  3.  600. 
•  j.  vaza-  Adj.  i)  'fahrend,  lenkend'  (vom
Fahrer).         a)  'wegführend,  raubend'. KompA.  {vazä.'y,  s.  dazu  unter  barö.iaü%r5-,
•  j.  vazaj^-  m.,  vazaj'a-  f.  'Frosch; Frosch  Weibchen';  ein  iÄiÄ-isches  Tier,  von dem  zwei  Arten  geschieden  werden,  Land- undWasser&Ösche:  °yanqm  dalmainyanqm (sd.)  .  .  'yanqm  ufapanqm  (sd.)  V.  14.  5 ; 'Ä73i  —  -yacT/ (statt  NSm.}  vii.kuskS\ tarS  ySr?  msrM  "ein  vertrockneter  über ein  Jahr  toter  Frosch"  V.5.36; — }q%wS.- tara  ..ydha  v3  °yq/ri  (statt  NSf)  
mp.  (Pü.).  np.  vazai.
•  j.  vazaiüyäi  Inf.  'hinzufliessen  zu  — '(Akk) : /.?«'>  afl  paurva  v  pasca  vUaxti  vafrahe "darauf"'  soll  dann  bei  ber  Schneeschmelze Wasser  in  Massen  fliessen"  V.  2,  24,
mit  paiti  'zurUck-,  nach  Hause  schleifen':
yat  Janani  httaspim  rai^e  *paiti.v'  '>  "dass
ich  den  H.  erschlage,  um  ihn  am  Wagen
nach  Hause  zu  schleifen"  Yt  1$.  28  i'.
Zum  V.  vaz:  —    ai.  vähadkyai.  —    Pu.:   fäi
haf  äp  api  laainih.  —  O  ASn.,  naml.  väilrim
•Weide'.  —    »)  NA.  trennt    —    J)  Vgl.  11.  X
395  ff-
•  j.  vazant-  Adj.,  PPA.:  s.vas-, KompE.
•  p.  '''vazarka-  Adj.  (fem,  'kä-)  'gross': xiaya%iyi^  ahyöyä  bümiya  'kSyS  (GSf.) D.  (*.  2,  H. /.  i;  —  x^aSi''am  tyam  'kam D.J7.  a;  —  xlaya%iy(^    "ia*    "ö  /tej-asl
*vaz5.ra9a-
1390
ßaaiKBV^"  Bh, /.  I,  D.J,  2,  5.1,  6.3,  12, 16,  ig,  X.  /.  a,  2. 3,  3. 3,  4. 3,  5,  a.  Am.  J, 2,  ^,  Ao.J.  a,  2;    —    bagi^    'kt^    <^urc^- matäa    D.  6.  i,  7. 1,  X.  /.  i,  6.  i,  Ao.  /.  i ; —  t^urJ'mazda  'in*  Ti.4.  1. Aus    iran.  *i(as/iia-,   AbleiL  aus    *jiaaar-  n., vgl.  vazärti-  Adj.,  eig.  also  'roichtig'.     iF.  t. ai.  ambAj-tiä-  und  cganä-
•  j.  vazah-  n.  1)  'Vorwärtsbringen, Fördern'.         i)  'Gleiten,  Fliessen*.
KompE.  —  Zum  V.  vaz-.  —  Vgl.  viOäsfa- und  'vätak:
•  j.  vazär«t-  Adj.  (auch  fem.)  'mit Energie,  Kraft,  Macht  sich  aufmachend': fravasayS  .  .  yä  *ts  (NPC)  Vt.  13.  23.
Komp.!  *viaa-  m.  (vgl.  ai.  vi/a-  m-,  wo«l Old£nhekg  ZDMG.  jo.  443,  Uhlenbeck WGSpr,  171 ;    s.  auch   ap.  *T/asatia-  Adj.)+
•  j.  vaz»mna-  Adj,  (fem.  °na-),  PPM.1 s.  vat-.        vaummm  als  AbsoL  sbes.
KompA.,  E.
•  j.  TBz9inn«in  AbsoL'*  'beim  Fahren', intrans.:  yai  aSe  ySi  mazäayasna  päha ayan/pm  (sd.)    vä  .  .  vae'  vä  . .  frajasan
V.^.26;<?.73-
Zum  V.  vas.-.  —  Pü.:  ka  . .  vazSnd  (3  Plur.), ka  .  .  vasän  .  .  rasätid.  —  D  BTHL.  IF. 12.  145,
•  j.  vozemnö-arätay-  m.  'Siegende  Lanze' :
kB  paoiryS . .  °H  (AP.)  ''  därayat . ,  lanaoj kaü  malyeke  V.  20.  i.
Ungewöhnliche    Komp.;    unsicher.    —     Pü. :
vazän  aslr  (s.  'arslay-  No.  i).  —  ')  S.  garay- No.  5.
•  j.  vazö.v^S'wya- ■'  Adj.  'wegführend, raubend  was  zur  Heerde  gehört'  (?) :  gtäiake •yeke  tbalsS  Yt  //.  5.
Pii.:  ramak  fenUär (/)'),  mit  undeulL  ErL3). — I)  Die  Lesung  des  2.  Glieds  ist  unsicher. F 1  bat  väi^raAe ;  richtig  vll.  t/ä%raAe ,  zu vj^ra-  n.  "Besiti,  Schatz',  tum  V.  'van-,  t. No.  3.  —  ')  Ob  väniiärt  Oder  vindUäri  — ä   Sie  scheint  yät  (für  vä%ra')  zu  enthalten,
•  j.  *vazö.ra9'a-  ■'  Adj.  'den  Wagen lenkend,  im  Wagen  fahrend':   ^bar5.aspB
dby  Google
>39'
vazi-
vaStar-
*'%ff  "auf  dem  Ross  reitend,  im  Wagen
fahrend"  li.37.
Pü.:  fetklt;  die  Stelle  iit  Glosae  in  ianrnnö vä  vatimnö  vä.  —  ')  Hds.  getrennt
•  j.  vazi-  fem.  Adj.  'säugend',  von  der Kuh'>:  ^ul paiti  atyä  (sd.)  . .  gJuI  faili . fravaitya  (sd)  vaisssca  . .  yaoiddkB  gsus paili  'zyä  V.g.^Tt  j
Et.?—  Pü.:  transAr.  ~  ')  Anders  Gdn.  KZ., 3/.  254,  DsT.  ZA,  »,  168.  I
■  }.  'vasdaA-  n.  'Beständigkeit;  Aus- dauer*.
```


## [2026-10-16T05:14:18.995Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 23240,23330p BRT.txt | cut -c1-300 | grep -n -i -E 'vaStar|vastar|vazya|vazista|vaz.ista|uzdar|uzdri|vasta|Zugtier|Last|vSzista|vazi' ",
 "description": "Find vaštar, vazya, vazišta in Bartholomae"
}
```


### [2026-10-16T05:14:19.289Z] TOOL RESULT

```
9:•  j.  vazya-  n.  'Last,  Tracht*;  batian "yanqm  alsmanam  V.S4.3,  3;  —  aisma- nqtnht  .  .  •yais''^  sisi//a  staoysbxl  ratSus nmantm  ß-anäiayata  "Trachten  und  noch grössere  Massen  von  Brennholz  sollt üir  zum  Haus  des  R,  herzubringen"  A.
11:KonpA.  —  Zum  V.  vac-,  —  ai.  vahyä-  n. ■TriigseisePi  vgl.  PDs.  vtt  liadaDg,  Last', iross.  ifföi  'Schwere'.  —  Pn. :  fui/at,  Sü. ;  Mä- raiam.  —  ')  Initr,  als  Obj.
12:■  j.  vazyamna-  Adj.  (fem.  'nJ-),  PPM.; s.  vat'  i.
13:•  j.  vazy^stra-  Adj,  'der  Tracht,  Last (nämL  des  Reiteis)  sich  widersetzend', von  Rossen'';  ajpaäi  ySt  miirsMrujqm
15:*ra  (NP.)  bavainti  "and  die  Rosse  . . widersetzen  sich  der  Last"  Yt.70. 30.
16:Komp.:  vatya--\-*tiitra;  »gl,  qita:  —  jEt s.  JN.  JAOS. /.#.  outvi»).  —  i)D.  h.  lie  «ölten sich  die  Last  des  Reiten  nicht  gefallen  lassen und  ihn  abwerfen.  —  >)  Anders  jetit  lo.  54. I  Aber  l)  erwartete  ich  dann  Vaiyajr,  2)  mnss das    Subjekt   zu    apayrinü   -as
29:•  j.  yahmi  ga^e  h^a  vaSta  ^aSu  nara . YL12.8:-?-.
31:•  j.  vaStar-  m.  'Zugtier':  ar3dvlm..ye^he ^a%warS  uara  spalta  vUpa  *hamagaO' näahJT  . .  Yt.5. 13.
```


## [2026-10-16T05:14:24.694Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 23264,23272p BRT.txt | cut -c1-600; grep -n -E 'uzdar|uzdri|uidar|uzdr' BRT.txt | head; grep -n -E 'vazista|vaziSta|väziSta|vSzista|väzista' BRT.txt | head",
 "description": "Check vašta, uzdar, vāzišta in Bartholomae"
}
```


### [2026-10-16T05:14:25.068Z] TOOL RESULT

```
mit  /ra  'anheben   zu   sprechen':   aSa/
uiti  fraiasata    Vfr>%rayn9  Yt  14.54;  IJ.
18,  21. Vgl.  aol-,  mit  dem  es  sich  auf  einer  twei- silbigen  Basis  in  vereinigen  scheint,  ar. *a((o.rJ(A)-'>,  —  sbal,  gvaiag  'sagen',  ZD*. dura  navä!  'ne  mens  pas',  iäii  'dis'  (JA.  9. I.  262);  BthL.  Stnd.  2.23. —  Pü.;  guftan, — ')  Im  Gegens,  lu  dav;  a.  V.  ig.  6,  7.  — »)  GDN.S  Fassung  von  aeSele  V.  iS.  26  in .SPrenssAW.  ig.  426  -  vgl,  IF.  7-  218  -  paist schon  für  V.  18.  51  wenig  gnt
•  J.  vaäan-  m.  —  ?  -,  Plur.  mit  asta Name  eines  Gebirgs:  ahmai  haca  garayS fraoxfyqn  . .  aita  *sanu  paurvata  ". ,  <ks Gebirg  'die  acht  V.'"  Yt/5.3.
•  j.  yahmi  ga^e  h^a  vaSta  ^aSu  nara . YL12.8:-?-.
•  j,  vaäta-  Adj,,  PPfP.:  s.  vas-  (mit No.  3).
•  j.  vaStar-  m.  'Zugtier':  ar3dvlm..ye^he ^a%warS  uara  spalta  vUpa  *hamagaO' näahJT  . .  Yt.5. 13.
Zum  V.   vat-;    J  Jj   IT.    —    ai.   vo^idr-   m., Ht/OT'  m.  —  VgL  läyuldrT-  und  vaÜra-.
ob,Google
7746:•  g.  aras  (,  j.  ar/)  Adv.  'richtig,  recht, wahr':  ärmati^iS uxitäil  fyaoianä  ?r'  daid- yat  (sd.)  Y.  44. 10;  —  beim  V.  vi-kay-: frB  va  fraSxya . .  mrüiteisA)  . .  ä.manat?hä 3f  vlHdysi  (sd.)  Y.  4f).  6;  —  os^ä  hudatthö ir'  vlsystä  nStt  duzdrn^hü  (sd.)  Y._jo.  3; 6;  —  beim  V.  vak-:  tat  %V}ä  p>r3Sä  (sd.) ar'  nwi  vaoc^  aAurJ  Y.44.i~i9"; — 'r° msi  prj-.ücqnt''  vauhSui  va/u/{sd.)  mana- uhS  Y,  48'().
10675:•  j.  xruzdra-  Adj.  'hart'  (vom  Holz): 'äidranain  msmanam  ä^re  frabarüts  \ . lg.  24.  a)  sva.  'schwierig'  (zu  beant- worten) :  'uidranam  (näml.  framanam) Yt.5.82  0.
21245:At/  Aumayalfa  ..  ana%amaide  Vr.J2.4;  — ka  afaa  aSsjtaitÜ  yä  vispim  imat . .  an- /aiti?  ,  ,  y  /raoirisaiti  pairi  dusma- taäbyasca . .  H.  /.  1 6  f.  3)  mit  Opt :  alrnq ß-asapcayaAi{sd,)..y  [va\..ätrpm  uzdarxa (sd.) ..vT/a  bareil..  V.S.j s-  VII)räumUch 'wo'j  nur  b)  im  jAwr.:  iva  aitaAe  nari gätui  atfAal  ..  ?  ..  y  atsAat  aiAAä  B»mS vT.aps.t>mim(sd.)ca  ..  V.j,  15;  10,18;  — a/lfm  nmarigm  y  also  na  para.trikyat  V, 5.41;  —  abda(^d.)ca  iaa  (Sp.  364  u.)  sa- dayät  y-  ioa  pasSus  . .  päiim  vamaiU  V. 2.24; — tä  jäfl(Sp.  364U.)  _)-*  narö  p»n- IfnieYti^.  27.  VIU)  vergleichend 'wie'; a)  im  gA^y.  'so  gut  als',  mit  Opt :  *'AaÜy<>.- dvalsi  (sd.)  hy  isöya  drfgväite  .  .  hyim Y.43.Z.  b)  im  jAw.:  ana  'kwä yama yagane  . .  yas?^^  %wa  yazata  vTitasps  Yt /7. 61;  —  Ay  paourvim  tat  ustfmim(&d.)- ät  Y.56.1,  Vr.().  7.
26200:•  j.  säy'uzdri-  m.  EN.  eines  Gföubigen: aiavazdasca  '^ritas^a  'äröi^''*  pu%ra  "A. und  e,,  die  Söhne  des  S."  Ytj.  73j  — %rilahe  •drOis^'*'^  asaonö  Yt./J.  113.
10189:eayanam  västryehe  fSuyantS  .  .  gaväzista (sd.)  '-izs  (ND.)  \.  14.10.
17822:sae^antätvirshraynaiY.  26. 10; — gSuicä hudätahs  gayehyäcä  mard^nB  .  .  °itm  Y. y-  7;  2j.  a,  26.  S,  Yt  13.  87;  —  «ÄM^ zar^uStrahe  ipitämahe  asaons  -sie  Y.  6S. 22;  3. 2,  4. 23, 16. 2,  23. 2,  24-  S,  7'-  2-  Vr. /ö,  2,  YtÄ  2,  J_J.  87,  Vd.(?;  —  ahe  nars aSaonS  'Jtm  yazamaide  yS  asmffj^ativä nqma  Yt,  /. 30;  13. 95 ff.  (oft),  Y. 23. 2, 26. 5% FrW.  2. 1,  3;  —  hvSuyä  asaonyä  'sim  Yt ''5-^39!  '39f-'*;  —  kanyä  *va}>uis  asaonya [. .]  °slm  Yt  13.  141 ;  141  f.'°;  —  auch  dem AÄM.  und  andern  Gottheiten  wird  eine Fr.  KUgeschrieben**':  vispanqmca  anAqm paoiryanqm  'Sinqm  .  .  °sm  avqm  yqm ahurahe  masda  .  .  °iay5  .  .  ya  ampsanqm spintanqm  .  .  yqmca  ährö  urväzistake  .  . yqmca  sraohhe..yqmca  alnSyqmca  apH.. YtJ^.  80-86;  Y.26.2i.,  V./»?.'4; — äyese yelti  *ä  *fravaM<y)'^  ahurahe  mazdä  am»- sanqm  sparUanqm  . .  Y.  25. 2 ;  —  gaom  (statt Gen.)  agvJS-dätahe  urunB  °Sim  S.2.  I2;i2; —  sogar  den  Fravalay  selber  (!) :  aSäunqm "sinqm  uyranqm  .  .  paoiryjJkaisanqm  'si- nqrrt  nabänazdistanqm  'ünqm  '/ayU  xihaiä ayantu  ahmya  nmaneYt.i3.1s6.  A)/ra- vaHnqm  a)  (näral,  mä)  heisst  der  i .  Monat  im Jahr^:  asäunqm  'sinqmY.i. 11.  ß)(näml, ayar?)  heisst  der  19,  Monatstag:  asäunam 'sinam  uyranam  S.j.  19;  vgl. 2. 19,  Y.10.5. •)*Nach  dem  GrBd.  (s,  DsT.  ZA.  3.  500, Blocket  RHR.J2. 104)  ist  der  Mensch  aus  fünf Bestandteilen lusammengesetit:  ian,yän,  nmän, äiinai  aad /ravakr.  Vom  letzten  heisst  es; y>ti- vahr  an  i  pcs  i  Öhrmazd  i  :^aiäl,  und  über  sein Verhältnis  mm  fiß/ö»  wird  geiagt:  ruvän  S/ra. vakr  pativast,  ku  iän  rm/ä»  marnjcmtan  ne  tiniän. S.  noch  DkB.  269  {218.  6):  io  (fravahr)  haf  lan yut  bavtt  lan  hil  lör  u  aiär  mänri.  Die  Schaffung der  fr.  (bei  West;  "prolotypes,  primary  ideas of  the  good  creations")  ist  nach  Bd.  /.  8, 34.  1 zu  Beginn  des  ersten  Mitleniums  erfolgt;  nach 2.  10  f.  entscheiden  sie  sich,  'lan  tariaiihä'  gegen die  Welt  der  Driig  zu  liämpfen.  Über  ihre,  ins- besondere  kiiegeiischeTäligkeitalsSchutzgeister und  Manen  gibt  das  ihnen  gewidmete  Yt  13 Auskunft.  Ihre  Zahl  wird  Yt.  13.  59  ff.  auf  99  999 eingegeben,  vgl.  jcludra-*)  and  Mx.  4g.  16,  52. 23,  29;  weniger  bestimmt  Yt.  13.  64,  66.  All- jährlich während  der  letzten  fünf  Tage  der sechsten  (letzten)  Jahreszeit  und  der  sich  an- schliessenden fünf  Schalttage  kommen  dieManen, ihre  frühere  Heimat  zu  besuchen  (Yt.  13.  49) und  werden  dann  besonders  gefeiert  (s.  hantas- pa%niae<iaya-)ii).  Vgl.  noch  Cld.  Totenverehrung 48,  BahadoorN.  D.  Khandalawala  Cama  Mem. Vol'  205,  JN.  GIrPh.  2.  643,  SÖDEftBLOM  RHR. 3g.  229,  373,  La  vie  future  7.  Das  Nichtauf- treten  der  fr.  in  den  (eig.)  Gä%äs  (s.  unten  No.  l) ist   bemerkenswert;    zum  Teil   aber   entspricht
```


## [2026-10-16T05:14:35.159Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py --help 2>&1 | head -20",
 "description": "Check fetch_source usage"
}
```


### [2026-10-16T05:14:35.938Z] TOOL RESULT

```
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
```


## [2026-10-16T05:14:44.348Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \\\n'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wéǵʰeti' \\\n'https://en.wiktionary.org/wiki/باز' \\\n'https://en.wiktionary.org/wiki/پرواز' \\\n'https://en.wiktionary.org/wiki/وزیدن' \\\n'https://en.wiktionary.org/wiki/وزغ' \\\n'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/uksḗn' \\\n'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wegʷ-' \\\n'https://www.etymonline.com/word/ox' \\\n'https://www.etymonline.com/word/humid' \\\n'https://www.etymonline.com/word/humor' \\\n'https://www.etymonline.com/word/wave' \\\n'https://www.etymonline.com/word/Norway' \\\n'https://www.etymonline.com/word/way' \\\n'https://www.etymonline.com/word/wagon' \\\n'https://www.etymonline.com/word/weigh' \\\n'https://www.etymonline.com/word/convex' \\\n'https://www.etymonline.com/word/vehicle' \\\n'https://www.etymonline.com/word/vector' \\\n'https://www.etymonline.com/word/convection' \\\n'https://www.etymonline.com/word/always' \\\n'https://www.etymonline.com/word/weight' \\\n'https://www.etymonline.com/word/away' \\\n'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wegaz' \\\n'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/uhsô' \\\n'https://en.wiktionary.org/wiki/umeo' \\\n'https://en.wiktionary.org/wiki/vazaγā' \\\n; do python3 tools/fetch_source.py \"$u\" --note \"page 531: weǵʰ-/wegʷ-/vazaγā- verification\" 2>&1 | tail -1; done",
 "description": "Archive Wiktionary and Etymonline pages",
 "timeout": 400000
}
```


### [2026-10-16T05:14:52.331Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/30d633c185079fa4.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d0da48c969256f25.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/573682d0d82af846.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6a0e509363aae5c4.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/817619fd1faf4d7a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0dc022d8415853d9.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9347ec4d0d8d773a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fc83bfb09dd6ab1e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/dbe1cf65dabfc1ff.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/409f7c08c66c5d75.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2b9d53fa6823679c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7d1490d226903a87.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2ed66dbb90d4afa6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/681b6c5eec078a98.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e46fb4778daa8533.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/098c7a441d4fe1d0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0f21f236f7feaf87.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4d15fc35d87f8991.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0be88b3094271619.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/44f49a57690a62f1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b4e21383414aece3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/19713a1bacb51a62.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b60291d7df32f913.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f99541f0bca9f270.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2b160574e26f2746.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c268d96eefe70985.txt
```


## [2026-10-16T05:14:55.674Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -26 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l); print(d['status'],d['bytes'],d['url'][-40:])\"; for f in d0da48c969256f25 573682d0d82af846 6a0e509363aae5c4 817619fd1faf4d7a; do echo \"## $f\"; grep -n -i -A6 'Etymology' $f.txt | head -30; done",
 "description": "Check fetch status and read Persian etymologies"
}
```


### [2026-10-16T05:14:56.190Z] TOOL RESULT

```
-1 39 https://www.etymonline.com/word/wagon
-1 39 https://www.etymonline.com/word/weigh
-1 39 https://www.etymonline.com/word/convex
-1 39 https://www.etymonline.com/word/vehicle
-1 39 https://www.etymonline.com/word/vector
-1 39 tps://www.etymonline.com/word/convection
-1 39 https://www.etymonline.com/word/always
-1 39 https://www.etymonline.com/word/weight
200 14209 https://en.wiktionary.org/wiki/به
-1 39 https://www.etymonline.com/word/away
200 4244 https://en.wiktionary.org/wiki/پدید
200 4873 wiki/Reconstruction:Proto-Germanic/wegaz
200 9748 https://en.wiktionary.org/wiki/پسند
200 4567 /wiki/Reconstruction:Proto-Germanic/uhsô
200 6178 https://en.wiktionary.org/wiki/باور
200 5971 https://en.wiktionary.org/wiki/umeo
200 3220 https://en.wiktionary.org/wiki/بدرود
-1 39 https://en.wiktionary.org/wiki/vazaγā
200 3950 https://en.wiktionary.org/wiki/پگاه
200 4392 https://en.wiktionary.org/wiki/پنهان
-1 39 https://en.wiktionary.org/wiki/پشکم
200 2344 https://en.wiktionary.org/wiki/سوژه
-1 39 Reconstruction:Proto-Indo-European/h₁upo
-1 39 https://www.etymonline.com/word/evil
-1 39 https://www.etymonline.com/word/open
-1 39 https://www.etymonline.com/word/sub-
## d0da48c969256f25
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
--
91: Etymology 
92-
93- 2.2 
94- Pronunciation 
95-
96- 2.3 
97- Noun 
--
119: Etymology 
120-
121- 4.2 
122- Pronunciation 
123-
124- 4.3 
125- Noun 
--
133: Etymology 1 
134-
135- 5.1.1 
136- Adjective 
137-
138- 5.2 
## 573682d0d82af846
62: Etymology 1 
63-
64- 1.1.1 
65- Noun 
66-
67- 1.1.2 
68- Adjective 
--
77: Etymology 2 
78-
79- 1.2.1 
80- Noun 
81-
82- 1.2.1.1 
83- Descendants 
--
94: Etymology 
95-
96- 2.2 
97- Pronunciation 
98-
99- 2.3 
100- Noun 
--
114: Etymology 
115-
116- 3.2 
117- Pronunciation 
118-
119- 3.3 
## 6a0e509363aae5c4
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
--
144: Etymology
145- [ edit ] 
146-
147- From Middle Persian [Book Pahlavi needed] ( wc-ytn' /⁠wazīdan⁠/ , “ to move; to blow ” ) , from Proto-Iranian *wájati , from Proto-Indo-Iranian *wáȷ́ʰati , from Proto-Indo-European *weǵʰ- ( “ to ride ” ) . Compare Northern Kurdish bezîn ( “ to run ” ) , bazdan ( “ to run ” ) , Avestan 𐬬𐬀𐬰𐬀𐬌𐬙𐬌 ( vaza i ti , “ to move, to drive a chariot ” ) , Sanskrit वहति ( vahati , “ to carry, transport; to blow (of wind) ” ) , Latin vehō ( “ to carry, to transport ” ) , Old Church Slavonic вести ( vesti , “ to carry, to convey ” ) , Old English wegan ( “ to carry, to bear ” ) (whence modern English weigh ). [ 1 ] 
148-
149- Pronunciation
150- [ edit ] 
## 817619fd1faf4d7a
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
88: Etymology 
89-
90- 2.3 
91- Pronunciation 
92-
93- 2.4 
94- Noun 
--
181: Etymology
182- [ edit ] 
183-
184- From Persian وزغ ( vazaġ ) , وزغه ( vazaġe , “ small lizard ” ) .
185-
186- Pronunciation
187- [ edit ] 
--
499: Etymology
500- [ edit ] 
501-
502- From Middle Persian [script needed] ( wzγ /⁠wazaγ⁠/ , “ frog ” ) . Akin to Avestan 𐬬𐬀𐬰𐬀𐬖𐬁 ( vazaγā , “ lizard, frog ” ) , compare وزغه ( vazaġe , “ small lizard ” ) , and to Old Armenian Վազգէն ( Vazgēn ) .
503-
504- Pronunciation
```


## [2026-10-16T05:15:01.844Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in d0da48c969256f25 573682d0d82af846 30d633c185079fa4 0dc022d8415853d9 9347ec4d0d8d773a b60291d7df32f913 f99541f0bca9f270 2b160574e26f2746; do echo \"## $f $(head -3 $f.txt | tr '\\n' ' ' | cut -c1-150)\"; grep -n -E 'From |Proto-|Persian|Avestan' $f.txt | grep -v '^\\S*:\\s*$' | head -25 | cut -c1-500; done",
 "description": "Extract etymology lines from archived pages"
}
```


### [2026-10-16T05:15:02.336Z] TOOL RESULT

```
## d0da48c969256f25 URL: https://en.wiktionary.org/wiki/باز FETCHED: 2026-10-16T05:14:45Z STATUS: 200 
165: Persian 
167: Toggle Persian subsection 
377: From Wiktionary, the free dictionary
396: From Middle Persian 𐭡𐭠𐭰 ( bʾc /⁠bāz⁠/ , “ hawk, falcon ” ) ; cognates with Old Armenian բազէ ( bazē ) , Georgian ბაზი ( bazi ) , Classical Syriac ܒܙܐ ( bāzāʾ ) , and Hebrew בַּז ( baz ) .
763: From Classical Persian باز ( bāz ) , from Middle Persian 𐭡𐭠𐭰 ( bʾc‌ /⁠bāz⁠/ , “ hawk, falcon ” ) .
875: Borrowed from Persian باز ( bâz , “ open ” ) .
891: Borrowed from Persian باز ( bâz , “ again ” ) .
907: Borrowed from Persian باز ( bâz , “ hawk, falcon ” ) .
938: Persian
941: Persian Wikipedia has an article on: باز 
948: ( Classical Persian ) IPA ( key ) : /ˈbaːz/ 
1000: Iranian Persian
1017: In Classical Persian, both باز ( bâz ) and واز ( vâz ) , variants of the same etymon, were in use. The former is now more common in the Iranian standard language and the latter in the Afghani standard, although the contracted وا ( vâ ) is also common in colloquial Iranian speech. Tajik usually uses the unrelated кушода ( kušoda ) , equivalent to Iranian گشوده ( gošude ) , which is now mostly formal or literary both in Iranian and Afghani usage and mainly reserved for poetry.
1036: Inherited from Middle Persian [Book Pahlavi needed] ( LAWHL /⁠abāz⁠/ , “ back, again, re- ” ) , [Book Pahlavi needed] ( ʾp̄ʾc ) , Manichaean Middle Persian 𐫀𐫁𐫀𐫝 ( ʾbʾc ) , from Proto-Iranian *apāča- ( “ back ” ) , derived from Proto-Iranian *apānk- ( “ behind ” ) , from Proto-Iranian *Hápa ( “ off, away ” ) , from Proto-Indo-Iranian *Hápa ( “ off, away ” ) . [ 2 ] 
1038: Less likely, from Proto-Indo-European *bʰe ( instrumental particle ) + *-ǵʰs ( “ out ” ) , and cognate with Sanskrit बहिस् ( bahis , “ out, aside from ” ) . [ 3 ] 
1062: Inherited from Middle Persian 𐭡𐭠𐭰 ( bʾc /⁠bāz⁠/ , “ hawk, falcon ” ) . Related to Sanskrit भास ( bhāsa , “ bird of prey ” ) , as well as Iranian borrowings: Old Armenian բազէ ( bazē ) , Georgian ბაზი ( bazi ) , and Classical Syriac ܒܙܝܩܐ ( bāzīqā ) .
1119: Persian terms suffixed with ـباز 
1137: ^ Nourai, Ali ( 2011 ), An Etymological Dictionary of Persian, English and other Indo-European Languages , page 53 
1145: Borrowed from Classical Persian باز ( bāz ) .
1225: Borrowed from Classical Persian باز ( bāz ) .
1247: Borrowed from Classical Persian باز ( bāz ) .
1259: Borrowed from Classical Persian ـباز ( -bāz ) .
1288: From Pashto باز ( bāz ) .
1299: Categories : Arabic terms borrowed from Middle Persian 
1300: Arabic terms derived from Middle Persian 
## 573682d0d82af846 URL: https://en.wiktionary.org/wiki/پرواز FETCHED: 2026-10-16T05:14:45Z STATUS: 200 
89: Persian 
91: Toggle Persian subsection 
201: From Wiktionary, the free dictionary
211: Borrowed from Persian پرواز ( parvâz ) .
290: Persian
293: Persian Wikipedia has an article on: پرواز 
300: From Middle Persian [script needed] ( plwʾc /⁠parwāz⁠/ ) , from Proto-Iranian *para- + *waj- ( from Proto-Indo-Iranian *waȷ́ʰ- , from Proto-Indo-European *weǵʰ- ) . Compare Central Kurdish دەرباز ( derbaz , “ flight, escape; pass ” ) .
305: ( Classical Persian ) IPA ( key ) : /par.ˈwaːz/ 
378: Borrowed from Classical Persian پَرْوَاز ( parwāz ) . First attested in c. 1611 as Middle Hindi پرواز ( prvaz /⁠parvāz⁠/ ) . [ 1 ] 
449: Categories : Ottoman Turkish terms derived from Persian 
450: Ottoman Turkish terms borrowed from Persian 
454: Persian terms inherited from Middle Persian 
455: Persian terms derived from Middle Persian 
456: Persian terms derived from Proto-Iranian 
457: Persian terms derived from Proto-Indo-Iranian 
458: Persian terms derived from Proto-Indo-European 
459: Persian terms with IPA pronunciation 
460: Rhymes:Persian/aːz 
461: Rhymes:Persian/aːz/2 syllables 
462: Persian lemmas 
463: Persian nouns 
464: Persian terms with usage examples 
465: Urdu terms borrowed from Classical Persian 
466: Urdu terms derived from Classical Persian 
486: Requests for native script for Middle Persian terms 
## 30d633c185079fa4 URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wéǵʰeti FETCHED: 2026-10-16T05:14:44Z STATUS: 200 
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wéǵʰeti
4:TITLE: Reconstruction:Proto-Indo-European/wéǵʰeti - Wiktionary, the free dictionary
6:Reconstruction:Proto-Indo-European/wéǵʰeti - Wiktionary, the free dictionary 
57: Proto-Indo-European 
59: Toggle Proto-Indo-European subsection 
78: Reconstruction:Proto-Indo-European/ wéǵʰeti 
130: From Wiktionary, the free dictionary
132: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
134: Proto-Indo-European
413: Proto-Albanian: *wedza 
416: Proto-Balto-Slavic: *weźtei ( see there for further descendants )
418: Proto-Germanic: *weganą ( see there for further descendants )
420: Proto-Hellenic: *wékʰō ( see there for further descendants )
422: Proto-Indo-Iranian: *wáȷ́ʰati ( see there for further descendants )
424: Proto-Italic: *weɣō ( see there for further descendants )
429: ^ Ringe, Donald ( 2006 ), From Proto-Indo-European to Proto-Germanic (A Linguistic History of English; 1)‎ [1] , 1st edition, Oxford: University Press, →ISBN 
431: Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/wéǵʰeti&oldid=92494553 "
433: Categories : Proto-Indo-European terms suffixed with *-eti 
434: Proto-Indo-European terms belonging to the root *weǵʰ- 
435: Proto-Indo-European lemmas 
436: Proto-Indo-European verbs 
437: Proto-Indo-European imperfective verbs 
439: Proto-Indo-European root thematic verbs 
442: Proto-Indo-European entries with etymon 
475: Reconstruction:Proto-Indo-European/ wéǵʰeti 
## 0dc022d8415853d9 URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/uksḗn FETCHED: 2026-10-16T05:14:47Z STATUS: 200 
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/uksḗn
4:TITLE: Reconstruction:Proto-Indo-European/uksḗn - Wiktionary, the free dictionary
6:Reconstruction:Proto-Indo-European/uksḗn - Wiktionary, the free dictionary 
57: Proto-Indo-European 
59: Toggle Proto-Indo-European subsection 
84: Reconstruction:Proto-Indo-European/ uksḗn 
136: From Wiktionary, the free dictionary
138: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
140: Proto-Indo-European
146: Of uncertain origin; [ 1 ] [ 2 ] possibly from *h₂uks-ḗn , from *h₂weks- ( “ to become strong ” ) [ 3 ] [ 4 ] [ 5 ] +‎ *-ḗn , or perhaps from *ugʷ-s-ḗn ( “ inseminator ” ) , from *wegʷ- ( “ to moisten, make wet ” ) . [ 6 ] Alternatively borrowed from Proto-Kartvelian *usx- ( “ sacrificial bull ” ) with metathesis [ 7 ] [ 8 ] , or a Wanderwort , whence also Proto-Turkic *öküŕ ( “ ox, bull ” ) . [ 9 ] Compare Proto-Nakh *ustu ( “ bull, ox ” ) .
251: Proto-Celtic: *uxsū ( “ ox, stag ” ) ( see there for further descendants )
253: Proto-Germanic: *uhsô ( see there for further descendants )
255: Proto-Tocharian: *wəkʷsó ( “ draft-ox ” ) ( see there for further descendants )
256: → ? Proto-Turkic: *öküŕ ( “ ox, bull ” ) [ 17 ] ( see there for further descendants )
258: → ? Proto-Uralic: *uškɜ ( “ ox, bull ” ) [ 18 ] ( see there for further descendants )
263: Proto-Indo-Iranian: *(H)ukšā́ ( see there for further descendants )
264: → ? Proto-Uralic: *uškɜ ( “ ox, bull ” ) [ 18 ] ( see there for further descendants )
266: → Proto-Kartvelian: *usx- ( “ sacrificial bull ” ) ( perhaps , with metathesis ) [ 7 ] [ 8 ] ( see there for further descendants )
271: ^ Zair, Nicholas ( 2012 ), The reflexes of the Proto-Indo-European laryngeals in Celtic , Leiden: Brill, →ISBN , page 27 
279: ^ Kölligan, Daniel ( 2018 ), “Chapter XX: Proto-Indo-European”, in Klein, Jared S., Joseph, Brian D. , Fritz, Matthias , editors, Handbook of Comparative and Historical Indo-European Linguistics: An International Handbook (Handbücher zur Sprach- und Kommunikationswissenschaft [ Handbooks of Linguistics and Communication Science ] ; 41.2 ), volume 3, Berlin; Boston: De Gruyter Mouton, →ISBN , § The lexicon of Proto-Indo-European, page 2269 
289: ↑ 10.0 10.1 Mallory, J. P. with Adams, D. Q. ( 2006 ), The Oxford Introduction to Proto-Indo-European and the Proto-Indo-European World (Oxford Linguistics), New York: Oxford University Press, →ISBN , page 140 
295: ^ Kölligan, Daniel ( 2018 ), “Chapter XX: Proto-Indo-European”, in Klein, Jared S., Joseph, Brian D. , Fritz, Matthias , editors, Handbook of Comparative and Historical Indo-European Linguistics: An International Handbook (Handbücher zur Sprach- und Kommunikationswissenschaft [ Handbooks of Linguistics and Communication Science ] ; 41.2 ), volume 3, Berlin; Boston: De Gruyter Mouton, →ISBN , § The lexicon of Proto-Indo-European, page 2269 
299: ^ Matasović, Ranko ( 2009 ), “*uxso-, *uxson-”, in Etymological Dictionary of Proto-Celtic (Leiden Indo-European Etymological Dictionary Series; 9), Leiden: Brill , →ISBN , pages 401-402 
307: Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/uksḗn&oldid=92151840 "
309: Categories : Proto-Indo-European terms belonging to the root *h₂weks- 
## 9347ec4d0d8d773a URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wegʷ- FETCHED: 2026-10-16T05:14:47Z STATUS: 200 
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wegʷ-
4:TITLE: Reconstruction:Proto-Indo-European/wegʷ- - Wiktionary, the free dictionary
6:Reconstruction:Proto-Indo-European/wegʷ- - Wiktionary, the free dictionary 
57: Proto-Indo-European 
59: Toggle Proto-Indo-European subsection 
72: Reconstruction:Proto-Indo-European/ wegʷ- 
124: From Wiktionary, the free dictionary
126: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
128: Proto-Indo-European
141: Terms derived from the Proto-Indo-European root *wegʷ- (4 c, 0 e) 
144: Proto-Indo-Iranian: 
145: Proto-Indo-Aryan: 
149: Proto-Germanic: *wakwaz ( see there for further descendants )
152: Proto-Hellenic: *ugrós 
156: Proto-Italic: 
160: Proto-Italic: 
170: ↑ 2.0 2.1 2.2 Kroonen, Guus ( 2013 ), “wakwa-”, in Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [1] , Leiden, Boston: Brill , →ISBN , page 569 
176: Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/wegʷ-&oldid=92151843 "
178: Categories : Proto-Indo-European lemmas 
179: Proto-Indo-European roots 
180: Proto-Indo-European ReC-shaped roots 
183: Proto-Indo-European entries with etymon 
217: Reconstruction:Proto-Indo-European/ wegʷ- 
## b60291d7df32f913 URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wegaz FETCHED: 2026-10-16T05:14:50Z STATUS: 200 
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wegaz
4:TITLE: Reconstruction:Proto-Germanic/wegaz - Wiktionary, the free dictionary
6:Reconstruction:Proto-Germanic/wegaz - Wiktionary, the free dictionary 
57: Proto-Germanic 
59: Toggle Proto-Germanic subsection 
84: Reconstruction:Proto-Germanic/ wegaz 
136: From Wiktionary, the free dictionary
138: This Proto-Germanic entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
140: Proto-Germanic
219: Proto-West Germanic: *weg Old English: weġ Middle English: wæi , wei , wai , wey , way Scots: wey 
258: ↑ 1.0 1.1 Kroonen, Guus ( 2013 ), “*wega-”, in Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [1] , Leiden, Boston: Brill , →ISBN , page 577 
264: Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Germanic/wegaz&oldid=92171145 "
266: Categories : Proto-Germanic terms derived from Proto-Indo-European 
267: Proto-Germanic terms derived from the Proto-Indo-European root *weǵʰ- 
268: Proto-Germanic terms suffixed with *-az (e-grade) 
269: Proto-Germanic terms with IPA pronunciation 
270: Proto-Germanic lemmas 
271: Proto-Germanic nouns 
272: Proto-Germanic masculine nouns 
273: Proto-Germanic a-stem nouns 
276: Proto-Germanic entries with etymon 
309: Reconstruction:Proto-Germanic/ wegaz 
## f99541f0bca9f270 URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/uhsô FETCHED: 2026-10-16T05:14:51Z STATUS: 200 
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/uhsô
4:TITLE: Reconstruction:Proto-Germanic/uhsô - Wiktionary, the free dictionary
6:Reconstruction:Proto-Germanic/uhsô - Wiktionary, the free dictionary 
57: Proto-Germanic 
59: Toggle Proto-Germanic subsection 
81: Reconstruction:Proto-Germanic/ uhsô 
135: From Wiktionary, the free dictionary
137: This Proto-Germanic entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
139: Proto-Germanic
145: From Proto-Indo-European *uksḗn ( “ bull ” ) . [ 1 ] 
209: Proto-West Germanic: *ohsō Old English: oxa Middle English: oxe , hox , nox , occe , ocxe , okse , ox , oxhe , oxse English: ox ( see there for further descendants )
243: → Proto-Sami: *vuoksā ( see there for further descendants )
248: ↑ 1.0 1.1 Kroonen, Guus ( 2013 ), “*uhsan-”, in Etymological Dictionary of Proto-Germanic (Leiden Indo-European Etymological Dictionary Series; 11 )‎ [1] , Leiden, Boston: Brill , →ISBN , page 558 
250: Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Germanic/uhsô&oldid=92150715 "
252: Categories : Proto-Germanic terms derived from Proto-Indo-European 
253: Proto-Germanic terms inherited from Proto-Indo-European 
254: Proto-Germanic terms derived from the Proto-Indo-European word *uksḗn 
255: Proto-Germanic terms with IPA pronunciation 
256: Proto-Germanic lemmas 
257: Proto-Germanic nouns 
258: Proto-Germanic masculine nouns 
259: Proto-Germanic irregular nouns 
260: Proto-Germanic an-stem nouns 
265: Proto-Germanic entries with etymon 
297: Reconstruction:Proto-Germanic/ uhsô 
## 2b160574e26f2746 URL: https://en.wiktionary.org/wiki/umeo FETCHED: 2026-10-16T05:14:51Z STATUS: 200 
160: From Wiktionary, the free dictionary
173: From Proto-Italic *ūmo- ( “ wet ” ) , of uncertain origin.
175: Traditionally derived from Proto-Indo-European *wegʷ- ( “ wet; to irrigate; ox ” ) , and compared with Ancient Greek ὑγρός ( hugrós , “ wet, moist, fluid ” ) , Old Norse vǫkr ( “ moist, damp, wet ” ) , English weaky .
177: However, Weiss and De Vaan are skeptical of this derivation, and instead derive the word from a Proto-Indo-European *uh₁mo- ( “ wet ” ) . Cognates would include Lithuanian umas ( “ quick ” ) , as well as perhaps ūrīna ( “ urine ” ) and Sanskrit वार् ( vār , “ water ” ) . [ 1 ] 
461: Categories : Latin terms derived from Proto-Indo-European 
462: Latin terms derived from the Proto-Indo-European root *wegʷ- 
463: Latin terms derived from Proto-Italic 
464: Latin terms inherited from Proto-Italic 
466: Latin terms inherited from Proto-Indo-European
```


## [2026-10-16T05:15:08.214Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 1055,1070p d0da48c969256f25.txt; sed -n 1128,1140p d0da48c969256f25.txt; grep -n -E 'Etymology|From|Proto' 817619fd1faf4d7a.txt | head; ls /home/sfmqrb/git/rishe-private/site/pages/531.jpg",
 "description": "Read bâz hawk etymology and page image path"
}
```


### [2026-10-16T05:15:08.743Z] TOOL RESULT

```
 باز آمدن ( bāz āmadan  / bâz âmadan , “ to come back ” ) 

 باز داشتن ( bāz dāštan  / bâz dâštan , “ to withhold ” ) 

 Etymology 3
 [ edit ] 

 Inherited from Middle Persian 𐭡𐭠𐭰 ( bʾc /⁠bāz⁠/ , “ hawk, falcon ” ) . Related to Sanskrit भास ( bhāsa , “ bird of prey ” ) , as well as Iranian borrowings: Old Armenian բազէ ( bazē ) , Georgian ბაზი ( bazi ) , and Classical Syriac ܒܙܝܩܐ ( bāzīqā ) .

 Noun
 [ edit ] 

 باز • ( bāz / bâz ) ( plural بازها ( bāz-hā / bâz-hâ ) , or بازان ( bāzān / bâzân ) , Tajik spelling боз ) 

 hawk 

 شطرنج‌باز 

 References
 [ edit ] 

 ^ Rastorgujeva, V. S. ; Edelʹman, D. I. ( 2003 ), Этимологический словарь иранских языков [ Etimologičeskij slovarʹ iranskix jazykov , Etymological Dictionary of Iranian Languages ] (in Russian), volume 2, Moscow: Vostochnaya Literatura, page 146 

 ^ Rastorgujeva, V. S. ; Edelʹman, D. I. ( 2000 ), Этимологический словарь иранских языков [ Etimologičeskij slovarʹ iranskix jazykov , Etymological Dictionary of Iranian Languages ] (in Russian), volume 1, Moscow: Vostochnaya Literatura, page 184 

 ^ Nourai, Ali ( 2011 ), An Etymological Dictionary of Persian, English and other Indo-European Languages , page 53 

 Sindhi
 [ edit ] 
62: Etymology 
88: Etymology 
170: From Wiktionary, the free dictionary
181: Etymology
184: From Persian وزغ ( vazaġ ) , وزغه ( vazaġe , “ small lizard ” ) .
499: Etymology
502: From Middle Persian [script needed] ( wzγ /⁠wazaγ⁠/ , “ frog ” ) . Akin to Avestan 𐬬𐬀𐬰𐬀𐬖𐬁 ( vazaγā , “ lizard, frog ” ) , compare وزغه ( vazaġe , “ small lizard ” ) , and to Old Armenian Վազգէն ( Vazgēn ) .
Permissions Size User   Date Modified Name
.rw-r--r--   72k sfmqrb 14 Oct 22:15  /home/sfmqrb/git/rishe-private/site/pages/531.jpg
```


## [2026-10-16T05:15:12.816Z] TOOL CALL #19: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/531.jpg"
}
```


### [2026-10-16T05:15:12.903Z] TOOL RESULT

```

```


## [2026-10-16T05:15:13.850Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'Falke|Frosch|Eidechse|fliegen|wehen' HRN.txt | head -30",
 "description": "Grep Horn for falcon, frog, fly, blow"
}
```


### [2026-10-16T05:15:14.248Z] TOOL RESULT

```
2855:kurd. per^ zaza pel 'F]ügel\ firin 'fliegen*; wa/. parr.
2940:fliegen , vergl. vazaiti er fliegt*.
5137:572. dem 'Atem, Atemzug', deine^ demulen 'wehen, blas(Mi\
5150:vergl. oss. d. dumun, t. dimin Vauchcn; wehen,
5525:Gehört hierher auch np. ram eilend, fliegend' (Pfeil)
6711:772. sah 'König, Herrscher, sähäne, sälü, sähin 'Falke'-).
9367:1082. vei^ey Frosch', arab. LW. vazayat 'Eidechsenart'.
9368:aw. vazayä' 'Frosch'; phlv. vazay, vazag.
9369:kurd. LW. vizdq 'Frosch' (H.-Sch.).
9372:ai. \/vah-^ väliati 'wehen (dahinfahren vom Winde);
9373:phlv. vajttan wehen'; kurd. LW. vezin, vazdmn
9374:'wehen (H.-Sch.).
10848:155. pasta/n (der Infinitiv kommt nicht vor) 'fliegen , mit
10850:aw. V^paU^ fräpatqn auffliegen' vd. 5, 12, 13;
10851:ai. [/'pat'j pdtati 'fliegen'; gr. Tterofiai 'fliegen.
10853:der Bedeutung 'fliegen* vorkommt und hier noch dazu
11131:(Men. 2, 115)^), oUyitan 'wehen' (AV.).
11143:208. vctjTtan {cäzUan) 'fliegen; fahren, AW.-Kommentar,
11145:aw. {^oaz-^ vazaiti 'fliegen; fahren etc. ; ai. [/^oah-
```


## [2026-10-16T05:15:19.880Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2930,2945p HRN.txt; echo ---; sed -n 9360,9380p HRN.txt; echo; awk 'BEGIN{RS=\"\\f\"} NR==264' HRN.txt | head -5; grep -n -E '^ *[0-9]+\\. *bäz|bäz .Falke|baz .Falke' HRN.txt | head",
 "description": "Read Horn entries for parwāz, vazaγ, vazīdan"
}
```


### [2026-10-16T05:15:20.519Z] TOOL RESULT

```
«) AM., Seite 46. Vergl. auch x^n-i S. (AM. 128 Zeile 6).
5*— 68 —
kurd, per e; af}'. parün; oss. vergl. /ar- (274, 1);
bei. paran- 'darüber hinaus gehend' (284).*
304. pervär *Stair^).
aw. *2)airivära?ia-, vergl. pairi.vära- 'Wall*, 'Stall'
(vd. 2, 26 vielleicht, Bartholomae); phlv. {pä-amün-)
parvär,
eS05. perväi^ 'Flug .
aw. pairi (oder para) — V^vciz-, 'herum- bezw. weg-
fliegen , vergl. vazaiti er fliegt*.
306. jyerwerden ernähren, erziehen*, periveris, perwer'tden,
pari -f- y^hhar-; phlv. partoarfan, partvar(i)sn,
307. pervez 'siegreich*.
phlv. aparvej 'siegreich'; wohl zu «r^i, be.ze (No. 253)?
Dann perwez.
---
versäz {wersäz) ?
1080. very 'Wasserwehr, hery.
skr. vdrga- 'Abwender\ also zu [/^vnrj- , vdrjafi
(Nöldeke, mündliche Mitteilung).
1081. vemste, beziste nur in nnon, nnDTZ (Is. 66, 8;
66, 17).
phlv. v(i)jastak; Pärsenwort, sonst r/ujasfak,
1082. vei^ey Frosch', arab. LW. vazayat 'Eidechsenart'.
aw. vazayä' 'Frosch'; phlv. vazay, vazag.
kurd. LW. vizdq 'Frosch' (H.-Sch.).
V
1083. i^ezlden 'wichen'; bezän (Sahn. I, 284 Anm. 2).
ai. \/vah-^ väliati 'wehen (dahinfahren vom Winde);
phlv. vajttan wehen'; kurd. LW. vezin, vazdmn
'wehen (H.-Sch.).
1084. ve^lr (arab. LW.) 'Vezir; Gelehrter ^), gezJr, gizlr*^),
talm. ns^T»!:.
*) So im indischen Persisch häufig, vergl. z, B. Maä»ir-i Mah-
wiidsähl Fol. 38 (Berliner Handschrift Ms. orient. Fol. 535).
Im modernen Spaniscli ist der Vezir als alguacil, alvazil etc. zum
'Häscher, Polizeidiener* (auch veraltet 'Scharfrichter' und im Schiffs-

— 242 —
1078. vevd/kj 'Wachtel', rerdej, verflj, vertek.
ai. varfikä' ^WachteF; phlv. oartak (Papyrus, Hörn,
ZDMG. 43, 50); gr. oorvh
kurd. verdl, //arnfrr?^ 'Wachtel' (H.-Sch.); af/. vvaraz\
1821:1466. bäzär 'Markt', bazargan, hazergän Kaufmann'.
```


## [2026-10-16T05:15:26.651Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo HUB; grep -n -i -E 'bäz|vazay|parväz|vazTdan|vazidan' HUB.txt | head -15; echo PHD; grep -n -E '^(bāz|wazag|wazay|wazīdan|parwāz|wazidan)' PHD*.txt | head; grep -n -i -E 'falcon|frog|hawk' PHD.txt | head; echo NYB; grep -n -i -E 'falcon|frog|hawk|wazītan|vazitan' NYB_vol2_glossary.txt | head",
 "description": "Grep HUB, PHD, NYB for headwords"
}
```


### [2026-10-16T05:15:27.025Z] TOOL RESULT

```
HUB
5668:zfidan = phi. vaziitan (pr. vazay-) 'to injure' Shk. 272 gehort ;
5801:vazay Trosch* ^^ zd. vazaya-; vantdan 'wehen', skr. vah
6816:paivazidan
7898:vazayGr- u. s. w.
8835:Oel' = zd. raoyna-; vazay *Frosch* = zd. vazaya^\ varg,
PHD
PHD.txt:5190:wazay wazr Saw-! Sudan! nigāh
PHD_mackenzie.txt:5294:wazay [wzyl N -, bazay] frog.
PHD_mackenzie.txt:5298:wazidan, waz- [we-ytn l P wz-, N -] move, blow (of wind).
PHD_mackenzie.txt:10142:wazay                      §.,      windisn
PHD_pages.txt:5294:wazay [wzyl N -, bazay] frog.
PHD_pages.txt:5298:wazidan, waz- [we-ytn l P wz-, N -] move, blow (of wind).
PHD_pages.txt:10142:wazay                      §.,      windisn
256:bayaspānļīh: mission, embassy. ~ig [-yk'] post-(horse). Бах [Pc | N ~] hawk, falcon. bāzā [b’c’y | (N bāzū)] arm. ~banag [-p'nk'] arm-guard, brassard. bazaģ [bck' | М beg, N ~a] sin, evil. —ih: = bazag. bazakkar [bckkl | M bzkr] sinful, sinner. bāzā-zanišnīh [by znfnyh = Av. bázu.jata-] a degree of sin. bazišn [dcšn'] division, part. bazm [bzm | — M, N —] meal, feast. ~-awurd [-zolt! | N ~] a sort of canapé. 1bë [BRA < A br | MP] but; out; ~... (enya), except. ~...enya...né: except... (otherwise)... not. ~ az: without. m 2be [BRA | M P, N bi-] particle with verbs, with 6, of indefinable function. -bed [-pt' | M -byd, N -balilud] suffix, -lord, -master. bēdom [bytwm | M bydwm] furthermost. béganag [byk’nk' | N ~a] strange; stranger. bégar [byk”/ | N ~] corvée, forced labour. béh [byh | N bih] quince. bel [by] | (M. Бу), N ~] spade. bélür [bylwl | M bylwr, N bilür] crystal. bérón [bylwn' | M byrwn, N bérün] outside. bëš [bys] pain, sorrow; harm, hostility. — burdan: bear hostility. bēš-, —i&n, v. bištan. bēšāz [byš(*)z] healing, medicinal. bēšāz(ēn)- [by?z(yn)-, byf?)c(yn)- | M byP?z-] heal, cure. —išnih: healing. bēš-burdār [byšbwlť’[] hostile. bëšidan [bysytn'] = bištan, bēšūmand [byš?*wmnd] sorrowful. béwar [Буш | M bywr, N ~] myriad, ten thousand. P bid [руй | P byd] again. bidaxš [byths] viceroy. *bifagàn [bch'n!] medicinal. bim [bym | = M, N ~] fear, terror. ~gén [-kn'] fearful, terrible. ~génih: fearfulness. --6mand [-'wmnd] fearful. *bistag [bstk! | N busta] hazelnut. biš [byf | N —] aconite. bištan, bé&- [bys-in' | M by$t, bys-] hurt, torment. ~išn: harm, torment. bize&k [dešk! | M bzyšk, N pizišk] doctor, physician.
371:frog [plwk! | N furdy] brilliance, brightness.
372:frogihistan, frógih- [plwkyh-stn'] shine.
605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
1094:brightness, brilliance Һат, brāzišn, frog, payrég, spig.
1870:falcon bāz.
2049:frog wak, wazay.
2227:hawk bāz.
4681:frawahr - PO o parwāngāh 595 ep o parwanagih ^5 e» Ф parwanag 13 ? o frawār, parwāl M o frawār-, parwāl- ANN CH parwālišn e» O frawārdan wed > оу franàm- - PO v franāmišn Irv’ > vo parwāz о» ro franāftan мү оу \ o Farrobag Yo (read pin-) Farróbag | 23 » a) piring E N a palang 3 М оз рагпарап w as» QJ palangmusk VU re N) Q) parwand E R Фу parwand- - 9 i a parron Ў оу frogih- -45?o frogihistan Us 4» оу frog Po parrwar N М P
NYB
448:andar-vāi [’ndlw’y] the atmosphere 8919. 9318, — Paz. andar-waé; SW form < *an- dar-vàd, MPrth ’ndrw’z (S; v. Sogd. 50). From andar + vaz-, v. vazitan.
4062:vazitan [wcytn'] to travel, to ride: tē... ké vazäh [subju. 2nd p. sg. = ind.] pat vài i dérang-x"atà$ thou ... who ridest on the long-dominating Wind 9914-15, — Av. (1386) vaz-; MPrth. pres. wz- ‘to blow’ of the wind’, ‘to move, to go’ (MHC); Ghilain 52.70, cf Verbum 170; Paz.
4065:vazitan [w’cytn'] caus. of the preceding v., to move: 1. trans. catrang — to play at chess 11915, 121%, — 2. intrans. to travel, to ride (= vazitan) 519-14. 6019, — Cf MPrth pdw’z ‘suite, followers’, pres. prw’z- ‘to cause to fly’, Ghilain 70; NP bazidan, büxtan ‘to play; to fly’.
4076:vaz-var [wcwl] safe for traffic: puhl 4 ~ 1147. — V. vazitan,
5432:vaz-: vazitan
7496:vazidan, bazidan: vazitan
```


## [2026-10-16T05:15:31.638Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'vazag|vazay|vazaγ|lizard|frog' IEC.txt | head -20; grep -n -i -E 'uksen|ugws|uqus|uqs.n|ox,' IEC.txt | head",
 "description": "Grep Mann IEC for lizard/frog and ox"
}
```


### [2026-10-16T05:15:31.997Z] TOOL RESULT

```
945:bimbos, å (?) Skt. bimbah, am “disc, mirror, picture; lizard’; bimba ‘red gourg’; It. bimbo, bimba ‘infant’; SEGer. Pimpf 'youngster; LG cf. pimps ‘youngster, midget’; EME cf. pimping “tiny, puny’
3091:dhrieho, ið (?) ‘shake, dash? (The semantic links of the following isophones are obscure). Cf sri8- Alb. (ambig. dridh “cause to tremble’; dridhem, mp. ‘tremble’; dridhë ‘tremor; Ir. driog (*dríog?) (2) ‘pang, nip of cold”; Li. cf. dryžiù, “ti ‘heave, haul beside dryžtu, ti ‘wear, wear out’ beside drýžas ‘striped; stripe’ (also *lizard"); Latv. drīzs ‘quick’ (Li. dryžys, m. = 'weal (Ir. driog, f. also = 'droplet). Obscure.
3185:dhr£h- (2), dhrghos ‘rough, coarse, insolent, boorish’. Cf. dhrágh- (2) Oss. dárzàg (rough, raw’, fr. *dhrghàkos, dim.); Gk. cf. bá-trakhos, m. (frog, lit. *croak- hoarse’, fr. *gua-^); Icel. durgur ‘boor’; Cz. drzý ‘insolent’; OCS drüzü “bold?
3511:ekKskétros, à ‘dragon, sea-monster Tokh. A (?) arsal *poison-snake'; Lat. excetra; Ir. (?) eascar, m. ‘enemy’; OCS jasterü ‘lizard’ beside jesetrü ‘sturgeon’. (Doublets also in OCz ještěr, jeSCer & jeseter; R jàščerica & osëtr); Srb. jesetra ‘sturgeon’; Li. eškētras, erškētras, eršketas & arškētas, m. id.; OPr. esketres, id.
4000:gi20, ið (1) “touch, hit, kick Oss. gezun, pp. gist ‘touch’; Arm. cf. kic, kick, s. Check. fr. *gigsK-); ME kicken (kick. G kicken perh. fr. Eng.); Du. cf. kikker, kik- vors ‘frog’ next, or guiĝ- (?) Arm. kcem, kčem, kcanem ‘prick, sting, burn, bite’; kic, gs kco, s. id.; (OCS go Zigati, beside Zego, žešti “burn, kindle’, fr. *gueg-?). Per. gazam (*burn'. Vocalism ambig.)
5051:ghükos (ghuk-) ‘hoot, whoop’ Skt. ghükah ‘owl; Per. yük ‘frog; R gik ‘whoop’; gikať, v. id.; Cz. (*-u-) hek ‘groan’ beside hykat ‘bray’; cf. R variant zyk (‘dim fr.
6902:kaukos, is, à (kauk-) “a raucous bird’. WP I, 33] Skt. kókah (2) ‘red goose, cuckoo’; Hind. koki ‘crow’; Sind. kok, m. ‘cuckoo; frog’; Per. kabg ‘partridge’; Tokh. A cf. kokafi “an un- identified bird”; Gk. kéux, gs kéukos “a gull’ beside kábéx, kaúēx, id.; Sard. coca ‘goose’ beside Sard. (Campid.) coga (^witch', cf. mngs. of Lat. strix); Ir. cuach ‘cuckoo’; W cawci (jackdaw': Hind. koki); Cz. kavka, Pol. kawka “daw”; Srb. cf. (variant) Cavka, id.; Li. kaukys, m. “a shrill bird’; kiauke ‘daw’; Latv. kaukis *blackcap gull'. (A similar onomat. element is present in Hind. kauwa ‘crow, daw? and in Fr. cahouette, id.)
7833:krekitos, a ‘stridency; strident creature’. Cf. krikət- W cf. creciad ‘chirping’; criciad (‘cricket in- sect, fr. Se or *-1-); Fr. criquet Conicket, fr. Gallo-Lat. unrecorded); OCS krěćetů ‘tree- cricket’; cf. kreksto, krektati ‘croak’; R krèčet ‘gyrfalcon’; Big. cf. kreketùša ‘frog’
7983:krokəlos, krokulos ‘pebble, marble, berry’. Cf. krok- (3) Gk. krokále ‘beach’; Li. krakulai, mpl. “frog- spawn’
9438:lak- (2) ‘kick’. Cf. lakt- (2) Gk. cf. láx (^with the heel". Ambig. cf. lag-); laktízo ‘kick’; Per. cf. lakd, s. ‘kick’; Lat. cf. lacertus “lizard?
9442:laks- (?) jump; lumping horse’ It. lacca “leg, haunch’; cf. Lat. lacertus ‘fore- arm; leg-muscle; lizard, newt? (?); Sw. lägg, m. pl. -ar ‘calf, thigh-bone'; Ukr. cf. loSak, m. ‘colt, foal; loša ‘filly’; Latv. cf. lakstu, -it Sump’.
9460:lako, ið (variant: las-) jump, dance’. Cf. laKosos, laKüs, (lakitio) Skt. cf. (variant) lasāmi (2) ‘dance’; lásayami, id. (and “cause to dance; ply an art'. The se- cond form given also as lasSayami); Oss. lásín (drag, lead; take; weigh". Semantics obscure); Gk. lekáo (‘dance to music’; vulg. ‘coire’); Alb. los, v. (play, fr. lakið); Pol. tasic ‘swirl, twirl; R dial lásit', id.; Li. lóSiu, ti ‘play’; cf. at-si-losti “rear, jump up”. Variants include Romani loSanav man ‘rejoice’ (with -š- for IE *-K-); Latv. lakstit, inf. “jump”; cf. perh. Lat. lacerta ‘lizard’? beside lacri-müusa ‘green li- zard’; Gk. lakáo Churst Cf. G springen in this sense) beside Hes. *lakertizo (misspelt lik- jump?)
12061:oit- (4) “creature, animal Skt. etah, età “hart; hind’; G cf. eid- (in Ei- dechse “lizard'); OE að- in aó-exe, id.; Li. cf. ait- (in ait-vara ‘chimaera, household snake"); Latv. aita, f. ‘sheep’. (Isophonic: ON eiða, f. ‘mother: MHG eide, wf. id.)
12822:popilos, is 'fleeting creature’. WP II, 107. Cf. pipl- (pipol-) Skt. pipiláh, m., -ih, f. rant: Hes. cf. pipalís, f. (-lizard', for (?) *papil-); Lat. cf. papilio, gs: -Onis, m. “butterfly, moth’; W cf. ilir, eilir & eilier, pl. -ion, m. id.; OPr. cf. pipalins, acc.
12905:pingolos ‘lizard’. WP II, 9 Skt. pingaláh, m. id.; adj. ‘tawny’; Hes. píg- galos, m. id.
13615:prusk- (prüsk-) “jump, start, spurt'. Cf. prsk- and next (short vowel in) E to frisk; OE frosc, m. ‘frog’; MHG vrosch, id.; ON froskr id.; cf. Du kik- vors(ch), wd: OCz. prsk, m. “spray, spurt’; (prS&ti, inf. “rain? < *prusk-: *prks-, q. v.); Slo- vene pfsk, m. ‘rut, heat in animals; prskati, inf. ‘rustle; spurt’; (long vowel in) Lat. prūs- cum (an unidentified shrub); Ir. rüisc, s. ‘lash, volley, hail of bullets; OCz. prýščiti, inf. ‘spurt, spray’; cf. Cz. o-prysk-aly, adj. “peeling, blistering’; R pryskat, v. ‘spurt, squirt’; cf. Slovene, Big. prist, m. “swelling, tumour, blister. Variant in OCS prysti, m. ‘sprout; swelling’; prystati se ‘swell, sprout'. (Iso-
14794:roupos (3) ‘rough; roughness’. Cf. (1) and (2) Latv. raupjš, adj. ‘rough, shaggy’. Other iso- phones ambiguously to (1) or (2), but cf. also Li. raupsai, pl. ‘leprosy’; raupežē, f. ‘frog
15487:skard- ‘jump’. Cf. skerio (1) Alb. cf. hardhje, f. ‘lizard’; hardhoj, denom. ‘cast, aim"; MHG cf. scharzen, v. jump, frolic’; scharz, sm. id.; ON skarta, v. ‘swagger’; skart, n. ‘swank, finery’. (NB: a form schérzen oc- curs in MHG, with -&- accdg. to Lexer, but this is uncertain). (Isophone: Br. skarz ‘tiny; neat; pernickety")
15539:skeko, ið (2) “jump, dash’. Cf. skok- Arm. cf. xeé, Let ‘shrimp, prawn’; Gk. cf. (?) skekós, m. ((lizard'", fr. *skēk-?); MHG schéhen, wv. (1) "hurry, hunt’; ON cf. skær, m. (fhorse', if fr. *skekro-); (o-gde in) OCS
18726:LW in) Lat. taxus, id.; EMDu. das, m. “wild cat’; cf. also OS -thassa, and -dehsa (in egi-°, ewi-^ ‘lizard’, lit. running snake’, see oguhis); ' Sw. tàssa, f. “toad'; Li. cf. (adj. form) táksis, gs: -io *'otterhound'; Latv. taksis, id.
480:aluos, ios, io ‘hollow, channel, cavity’. WP I, 26; 92: aulos. Cf. Gk. álox, f.; Cyp. (queried) alwon ((quarry, mune or sim.); Lat. alvus, alveus; ON áll (2. ‘deep channel); Sw. alv ‘podzol’; älv “river”, cf. in-elvor ‘entrails’ (Hell- quist otherwise); (?) Li. alve ont
1100:bhal- (1) “white, pale; white-spotted; pallor, blaze on forehead" ` Skt. bhalah (epithet of sun), bharuh ‘gold’; Arm. bal (i-st. *pallor) Gk. Phalís ‘priestess of Juno', phálos *white, bright'; phálios, id.; Gk. (fr. Phryg. bálios ‘eyeless’; Alb. bal (^white-haired; blazed animal); Gaul. balio- (‘white blaze > Fr: baille, id.); Dacian sub- strate in Rum. bál ‘white blaze’; Br. bai" id. (and “white blazed', adj.): W bal, adj. id. be- side bali ‘blaze’; Go. bala- epithet of horse, LW in LLat. bala, gs balanis ‘white horse’; EME ball ‘white blazed; blaze on animal; Blg. bol ‘smallpox, pockmark’; Li. balas ‘snowdrop’, balai, pl. ʻanemone’; balù, bálti “turn pale’; Latv. bāls (tonal *-a- or long *-a-) ‘pale’. See bhal-. Cf. further Li. bálnas *whit- ish, of cattle’
1398:bhlogos, is, s, à ‘flash, gleam, blaze’. Cf. bhleĝ- and bholg-. WP II, 214 Gk. phlox, gs phlogós; Tokh. (ambig.) A pälk, B pilko ‘look’, (cf. bholg-); G (uml. fr. LG) blecken ‘bare the teeth’; Du. cf. blaken ‘scorch’; Norw. blakk ‘pallid’; Sw. black, id.
3347:dhuskos "dark" Cf. dhus- and cpds. WP I, 846 Lat. fuscus; OE dox, dux ‘fallow’; E cf. dusk; G cf. ver-tuschen, v. *hush up'; Norw. cf.
3458:eĝhis (2) ‘ox, cow'. WP I, 38. (Adjectival: eghnio-, eghino-) Skt. ahih ‘cow’ beside aghnyah ‘bull’, aghnyà ‘cow’; Av. azis, adj. ‘three-year-old’ of cow; Arm. ezn, gs ezin & ezan fox’; OCS cf. jazíno “leather”
3934:geger- (ger-) *wake, rouse, excite; be awake, etc". WP I, 598. Ambig. Skt. jagármi, járe, intr.; Gk. cf. egeíró (ambig. cf. ueger-); Av. jayaurus, act. pt.; G keckeren, v. (of fox, marten ‘screech angrily’), cf. e keckert mich ‘am angry’; OCz. (ambig.) Zehtu, Zehrati (bully; rage; be jealous’. Cf. guhe- guh-); (G jachern 'rush around': Du. jak- keren, id. represent a further variant of type *leger-, equally equatable w. Gk. egeíro. G wacker ‘lively’, etc. represents a type *uogero-)
5339:guóu-eda (-édis, -odà, -dā) ‘ox, cattle, beef, cattle-fodder'. Cf. ed- and guou-sth- Oss. qáwwaz, qwaz, Dig. $àwanz ‘hind, doe: Alb. gjedh “head of cattle"; ON kjot, ds kjotvi ‘flesh’; Sw. kött, Norw. kjótt, Dan. köd, id. (vocalism obscure); OCS govedo "oy: OCz. hovéda, hovedina, f. “beef” beside Cz. havéd ‘vermin’ :
5341:guóuolos (guəuəl-) “head of cattle; bull, ox, buffalo". WP II, 112 Skt. golah ‘bull’; Hind. gaur ‘wild bull, bison’; Oss. gal ‘ox; bull; Gk. boübalos ‘buffalo’; Lat. (LW fr. Gk) bübalus, id., beside It. (from Umbrian) bufolo, id.; MIr. büáaball, id.; W bual, id. (both fr. Lat. but cf. also Ir. bólach, bólacht, bualacht ‘livestock’, fr. *guouol-a$-
5350:guðus “head of cattle, ox, cow. WP I, 696. (Z-gde variant: gii-) Skt. gauh, pl. gāvah “head of cattle’; gávam ‘bull’; gavah ‘ox’; gavih ‘cow’; Av. gáus; Per. gàu, gàv; Oss, qug, gog ‘cow’; Arm. kov, u-st. ‘cow’; Tokh. ko, pl. kowi; B keu ‘cow’; Hitt. .. us ‘head of cattle’; Hiero-Hitt. wawas, id. (for *hwawas); Myc. qou-; Gk. boüs; Lat. bos, gp boum; Umb. bum, acc.; Olr. Ir. bó, pl. ba; W bu, buw; Cor. bow- cpds. ‘cow’; OBr. cf. bou-tig *'cow-house'; OHG kuo, pl. kuo, kuoi, gp kuo; OE cü, pl. cy; LG kau; Fris. kou, pl. kij; Du. koe; OCS cf. gu-mno 'cow-tread', i. e. *threshing-floor', and com. Sl. Cf. min-; Cz. hav-éd' ‘vermin’ beside hov-ézí ‘beef; Latv. govs, gs id., gp govju ‘cow’. Z-gde variants in-
6222:cf. khés-imon “self-easement'; pés-imon “act of falling'; pega-imós 'act of departure'; Alb. het-im (inquiry): Li. skait-ymas reading); Ir. maoidh-eamh, gs -imh ‘telling’; áir-eamh, gs -imh ‘counting’; OCS pisimo “letter, writing; jarímü (fyoke', cf. Pol. ko-jarzyé "mont: Li. pie3-imas, ar-imas, grub-imas, &j-imas *design- ing, plowing, roughening, going’ beside grüd- ymas ‘hardening’; sür-ymas ‘saltwater’, etc. -inā, a generalizing extn. See next Gk. khoir-inë (‘musseľ: khoiros); dotiné (Hes: dos); (melíné ‘millet? in relation to *mel- ‘grind’, q. v. may belong here); Alb. lug- inë ((valley': lug 'trough); rreth-inë ('sur- roundings': rreth 'circle"); Lat. farina (:far); rüpina (:rüpes); haed-ina ('goatsflesh': hae- dus); OS cf. stulina ‘stealing’; lugina ‘lying’; OCS ozina ('anguish': ozükü, cf. Lat. angina); globina (‘depth’: globokü); dolina ('valley': dolü *ditch"). A variant occurs in Li. avíena “mutton”, cf. LLat. ovina, id. As an indicator of a female with a male counterpart, cf. Gk. héroiné (*heroine": héros); Lat. reg-ina (:rex); MHG cf. vühsinne (vixen': vuhs). A truncat- ed formula occurs in Go. managei, obl. -ein- ‘multitude’ and OHG hohi, obl. -1n-. See next -Inos, om (-Inios, om), an adjectival formant > a noun-derivative. Skt. a$v-in (:Lat. equinus); Av. peronin *wing- ed'; hámin- ‘summer’; Per. Sirin (sweet: Sir *milk); éübin (^wooden': éüb); pūstīn (‘fur coat: pūst "pelt: Oss. zàr-in ( golden": zàr); Arm. verf-in (final: verð); het-in, id. (fr. *en-pedinos, cf. Li. j-pedin “close behind”; Í-pédinis *successor"); Gk. pheg-inós (*oaken": phégós, cf. Lat. fàgínus of beech’); earinós (‘of spring": éar, cf. Lat. vernus); Lat. marinus, fibr-inus beside nüc-Ínus, màter-nus, ver-nus, etc.; W derw- in, lledr-in, hef-in ('oaken, leath- ern, summer: derw, lledr, haf); Go. fill-eins (‘of skin": fill, cf. Lat. pell-inus); fadr-ein (“pa- ternity, cf. Lat. paternus); OHG bibir-in, fuhs-in; MHG buech-in; ON gull-inn, OE medr-en, etc. “of beaver, fox, beech, gold, mother’; OCS materinü, materiní ‘maternal’; sestrinü, sestrini ‘sisterly’; krův-ínů (“of blood': krúvi, cf. Li. krùvinas ‘bloody’:kraŭjas “blood”). The variant -inios, where it occurs,
```


## [2026-10-16T05:15:36.110Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 763 764 765; do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' IEC.txt | grep -n -i -E 'u[ĕe]ĝ|ueg|vaza|frog|lizard|1499|1498|1500|uks|uqs' | cut -c1-400; echo \"== $n\"; done",
 "description": "Locate IEC p.1499 entry"
}
```


### [2026-10-16T05:15:36.602Z] TOOL RESULT

```
== 763
== 764
4:teubh- — teukso, ið
17:teukså “girl, young female’. Cf. teuquio. (Norse type: touksàá) Norw. (landmal) taus, def: tausa; Norw. tós, Sw. tös, f. & n. ‘girl, wench’, (o-gde); Slovene Cuba, f. ‘heifer’; Blg. cf. (dim.) čuška, f. *cun- nus”. (Isophonic: Skt. Coksab, à, adj. pure)
18:teukso, ið (1) ‘chatter, twaddle’ W cf. tuch, m. ‘grunt, groan’; Rust, s. “non- sense’; Li. Ciauksti, v. (1) “twitter; stammer”; cf. čiauškalas, m. ‘twittering; twaddle’ beside (o-gde) tauskiu, tauksti, v. ‘twaddle’
19:teuksó, ið (2), see touks-. E-gde in MHG diusen, v. (lug, tousle; get muddled’; Blg. cuslja, v. 'shuck — grain’; Morav. Cz.
== 765
```


## [2026-10-16T05:15:40.899Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'vaza|vazag|vazay' IEC.txt | cut -c1-500 | head; grep -n -E '^u[ĕeē̆][gĝǵ]' IEC.txt | cut -c1-200 | head -30",
 "description": "Search IEC for vaza and ueg headwords"
}
```


### [2026-10-16T05:15:41.241Z] TOOL RESULT

```
19824:uégo- (1), element of the following (?) Av. cf. vazaya, f. ‘lizard’; Per. vazaq, s. ‘frog’; Li. véZys, m. ‘crab, crayfish’; veZlys, m. “tor- toise’; Latv. vēzis, s. ‘crab’. (Oss. isophone (?) wázal, adj. = ‘cool, cold")
19838:ue£hen- (ueghn-) ‘carrier, conveyor, convey- ance; carriage, cartage'. Cf. uegh- Skt. vahanam, n. ‘conveyance’; váhnih, m. *charioteer; steed'; Av. vazanom, n. 'cartage, conveyance’; -vazano, adj. cpds. *-conveying"; Lat. cf. (?) vena, f. (tube, vein’; LLat. also *stream — of tar'; cf. ductus, üs in a similar sense); Gaul. cf. co-vinnus, m. (fchariot'. Cf. W cy-wain, v. *Àconvey?); OIr. fén, Ir. féan, pl. féin, m. ‘wagon’; W gwain, pl. gweiniau, f. (2) ‘support; (3) ‘carriage’; (o-gde in) 
19818:ueg- “twist, weave". WP I, 247. Cf. uig- (1) Alb. vegj, v. ‘weave’; vegjë, f. doom’; Olr. figim, Ir. fighim, v. ‘weave’; -fige, cpds. '*-weav- ing; cf. Ir. feagán, m. ‘flange of spinning- wheel;
19819:uegh- ‘say, utter’ Skt. cf. vāghát, nt-st, m. “official at sacrifice’; Per. güvam, guftan, v. ‘say’; Arm. gogem, aor. 3s. gog, v. ‘say, utter’; Hitt. hwekmi, hwikmi (hweikm:i), 3pl: hukanci, v. 
19823:ueĝer- (uegor-) ‘rouse; lively’. Cf. ueg20, uo- Leið, uoĝeros Hitt. cf. wakariya(mi), wagar-, v. incite’, prob. o-gde); Gk. egeíro, v. id.; cf. Lat. vegeo, ere, v. ‘thrive’; W gwair, adj. “fresh
19826:uegh- “carry, convey, transport; conveyance, roadway, means of transport. WP I, 249. Cf. uogh- Skt. váhami, v. ‘convey, transport'; Av. vazà- mi, v. “lead, conduct, draw’; Per. cf. a-vizam, -vix
19839:ueghidhlom, -tlom, -trom, extn. of type uegh- in Skt. vahitram, n. "boat": Lat. vehiculum, n. *conveyance'; Cz. cf. vozidlo, n. id.
19841:ueghtis “lift, weight, conveyance’
```


## [2026-10-16T05:15:46.798Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 19826,19827p IEC.txt | cut -c1-1500; grep -n -E '^ug|^uks|^uqs|^ug.s' IEC.txt | cut -c1-600 | head",
 "description": "Read IEC uegh- and ox entries"
}
```


### [2026-10-16T05:15:47.172Z] TOOL RESULT

```
uegh- “carry, convey, transport; conveyance, roadway, means of transport. WP I, 249. Cf. uogh- Skt. váhami, v. ‘convey, transport'; Av. vazà- mi, v. “lead, conduct, draw’; Per. cf. a-vizam, -vixtan, v. ‘suspend’; Cypr. Pamph. wékho, aor: éwexe, 3s. “convey, deliver’; Alb. vjedh, aor: vodha, v. ‘steal’; Lat. veho, ére, v. *con- vey’; cf. also (?) traho, ére, v. (draw, if fr. *tro-uegho?) beside incoho, are, v. (begin, if fr. *en-ko-ueghajo); Go. ga-wigan, tr. ‘move’; OHG wégan, sv. 5. id., OE wegan, sv. 5. “bring, bear, wear, weigh’; MHG wégen, SV. 5. *betake oneself; weigh'; ON vega, p. t. vá, sv. 5. "lift, weigh, attack’; OCS vezo, vesti, V. convey’, and com. SL); Li. veZü, véZti, id.; Latv. cf. vezums, m. 'cartage, load’. Nomi- nal types: Skt. vahyah ‘portable’; vahyam, n. *sedan-chair, litter; vahyah, adj. ‘ridden,
ue&er- (uegor-) — ue£htis
19529:ug- (2), suffix-element in bird-names Gk. cf. órt-ux, gs: -ugos ‘quail’; Lat. cf. ves- per-ügo, gs: -üginis, f. (2) *bat'. Tertullian); Ir. cf. truide-og, druide-og beside (simplex) truid & druid, f. ‘starling’; W drud-wy, m. id.; OE cf. heaf-oc & haf-oc ‘hawk’; rudd-uc ro, bin"; E dunn-ock ('sparrow', but for OE tosoc,
19543:ug-, intensive prefix. (Armenian uncertain) Arm. c-agim, v. (“dawn also 'arise); c-agem, v. ‘produce’ (9); OCS vüzü, prp. "against: OCz. vz, id. and vz-, px.; Li. už ‘for; behind; už-, px. Cup, or intensive perfective); cf. also OCS za “for, after, by’: Li. uZüo- “before, with’; uzüot “instead of; Latv. uz, prp. “on, to, to- ward’ beside uz-, px. ‘on~
19551:uksó(n), uksen- *ox'. WP I, 249 Skt. uksán, m. ‘bull’; Av. uxsan- "ox: Tokh. B. okso ‘horned beast; EBr. uchen, ochen, m. ‘ox; W ych, pl. ychain, ychen, id.; Go. aúhsa, id.; OHG ohso, wm.; OE oxa, wm: ON uxi, pl. uxar, yxn & ọxn, id.
19556:uksó(n), uksen- — uper, uperi (upor, upor)
```


## [2026-10-16T05:15:50.615Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ox,|^humid,|^humor,|^convex,|^vehicle,|^way,|^weigh,|^wave,|^Norway' KLN_1966.txt | head; n=$(grep -n -E '^ox,' KLN_1966.txt | head -1 | cut -d: -f1); sed -n \"${n},+6p\" KLN_1966.txt | cut -c1-900",
 "description": "Grep Klein for English headwords"
}
```


### [2026-10-16T05:15:50.950Z] TOOL RESULT

```
18225:humid,  adj.  —  F.  humide,  fr.  L.  {h)i2midus,  ‘moist, wet’,  fr.  {h)umere,  ‘to  be  moist  or  wet’.  See
26833:ox,  n.  —  ME.,  fr.  OE.  oxa,  rel.  to  OS.,  OHG. ohso,  ON.  oxi,  uxi,  OFris.  oxa,  MDu.  osse,  Du. os,  MHG.  ohse,  G.  Ochse,  Goth,  auhsa,  and cogn.  with  W.  ych,  ‘ox’,  Mir.  oss,  ‘stag’,  OI, uksa,  Avestic  uxshan-,  ‘ox,  bull’,  Toch.  B  okso, ‘ox’,  fr.  I.-E.  base  *uksen-,  ‘male  animal’,  lit. ‘besprinkler’,  fr.  base  *uks-, ‘to  sprinkle’,  whence OI.  uksati,  ‘sprinkles’ .  This  base  is  related  to base  *ugw-,  ‘wet,  moist,  to  sprinkle’,  whence  Gk. uyp 8?,  ‘wet,  moist’,  L.  umor  (for  *ugwmbr ), ‘fluid,  moisture’.  See  humor  and  cp.  uxorious. Cp.  also  the  second  element  in  aurochs, oxalate,  n.,  a  salt  of  oxalic  acid  (chem.)  —  F., coined  by  Guyton  de  Morveau  (1737-1816)  fr. L.  oxalis,  "sorrel1.  See  Oxalis  and  chem.  suff; -ate.
ox,  n.  —  ME.,  fr.  OE.  oxa,  rel.  to  OS.,  OHG. ohso,  ON.  oxi,  uxi,  OFris.  oxa,  MDu.  osse,  Du. os,  MHG.  ohse,  G.  Ochse,  Goth,  auhsa,  and cogn.  with  W.  ych,  ‘ox’,  Mir.  oss,  ‘stag’,  OI, uksa,  Avestic  uxshan-,  ‘ox,  bull’,  Toch.  B  okso, ‘ox’,  fr.  I.-E.  base  *uksen-,  ‘male  animal’,  lit. ‘besprinkler’,  fr.  base  *uks-, ‘to  sprinkle’,  whence OI.  uksati,  ‘sprinkles’ .  This  base  is  related  to base  *ugw-,  ‘wet,  moist,  to  sprinkle’,  whence  Gk. uyp 8?,  ‘wet,  moist’,  L.  umor  (for  *ugwmbr ), ‘fluid,  moisture’.  See  humor  and  cp.  uxorious. Cp.  also  the  second  element  in  aurochs, oxalate,  n.,  a  salt  of  oxalic  acid  (chem.)  —  F., coined  by  Guyton  de  Morveau  (1737-1816)  fr. L.  oxalis,  "sorrel1.  See  Oxalis  and  chem.  suff; -ate.
oxalic,  n.,  pertaining  to  the  acid  C2H204  (chem.)
—  F.  oxalique,  fr.  L.  oxalis,  ‘sorrel’ ;  so  called  by the  French  chemist  Antoine-Laurent  Lavoisier (1743-94)  in  1787,  because  it  occurs  in  the  plant
sorrel.  See  Oxalis  and  adj.  suff.  -ic. Oxalidaceae,  n.  pi.,  the  wood  sorrel  family  (bot.)
—  ModL.,  formed  fr.  Oxalis  with  suff.  -aceae. oxalidaceous,  adj.  —  See  prec.  word  and  -aceous. Oxalis,  n.,  a  genus  of  plants,  the  wood  sorrel
(bot.)  —  L.  oxalis,  ‘a  sort  of  sorrel',  fr.  Gk. i'a/ic,  ‘sorrel’,  fr.  6 ;uc,  ‘sharp’,  which  is  rel.  to oxpt;,  ‘peak,  point’,  Homeric  oxptav,  ‘to  make rough  or  rugged’,  dxptxaffxt,  ‘to  be  exasperated’, cogn.  with  L.  ocris,  ‘a  rugged,  stony  mountain’, medi-ocris,  ‘middling,  moderate,  indifferent,  tol¬ erable',  orig.  ‘being  half-way  up  the  height  of  a mountain’.  Limb,  ukar,  ocar,  ‘fortress,  citadel, mountain’,  and  in  gradational  relationship  to  L. acer,  ‘sharp’.  See  acrid  and  cp.  oxy-,  oxytone, paroxysm.  Cp.  also  mediocre.
oxidation,  n.,  the  act  of  oxidizing  or  the  state  of being  oxidized.  —  F.  (now  spelled  oxydation). See  oxide  and  -ation.
```


## [2026-10-16T05:15:56.757Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in humor humour vehicle vector convection convex way away always wagon wave Norway weigh weight; do l=$(grep -n -E \"^$w, \" KLN_1966.txt | head -1); echo \"KLN $w: ${l:0:330}\"; done; echo; for w in humid humour vehicle convex way wagon wave weigh Norway; do l=$(grep -n -i -E \"^$w[, ]\" SKT.txt | head -1); echo \"SKT $w: ${l:0:300}\"; done; awk 'BEGIN{RS=\"\\f\"} /^ox,|\\nox,  n\\./{print NR-1; exit}' KLN_1966.txt",
 "description": "Klein and Skeat lines for English words"
}
```


### [2026-10-16T05:15:57.573Z] TOOL RESULT

```
KLN humor: 
KLN humour: 
KLN vehicle: 
KLN vector: 
KLN convection: 9035:convection,  n.,  transference  of  heat  by  the  move¬ ment  of  the  heated  particles.  —  L.  convectio, gen.  -onis,  ‘a  carrying  together’,  fr.  convectus', pp.  of  convehere,  ‘to  carry  together’,  fr.  con-  and vehere,  ‘to  carry’.  See  vehicle  and  -ion.
KLN convex: 
KLN way: 
KLN away: 4144:away,  adv.  —  ME.  away,  aweie,  fr.  OE.  on  weg, lit.  ‘on  the  way’.  See  a-,  ‘on’,  and  way.
KLN always: 
KLN wagon: 
KLN wave: 
KLN Norway: 
KLN weigh: 
KLN weight: 

(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
SKT humid: 
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
SKT humour: 
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
SKT vehicle: 
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
SKT convex: 
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
SKT way: 
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
SKT wagon: 
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
SKT wave: 
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
SKT weigh: 
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
SKT Norway: 
591
```


## [2026-10-16T05:16:02.203Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nfor fn in ['KLN_1966.txt','SKT.txt']:\n    t=open(fn,encoding='utf-8',errors='ignore').read()\n    pages=t.split('\\f')\n    for w in ['humor','humour','humid','vehicle','vector','convex','way','always','wagon','wave','Norway','weigh','weight','ox']:\n        m=None\n        for i,p in enumerate(pages):\n            mm=re.search(r'(?m)^'+w+r'\\b[,.]?\\s.{0,280}',p, re.I)\n            if mm: m=(i,mm.group(0).replace('\\n',' ')); break\n        print(fn,w,m)\nEOF",
 "description": "Find English headwords in Klein and Skeat"
}
```


### [2026-10-16T05:16:04.699Z] TOOL RESULT

```
KLN_1966.txt humor (403, 'humor. Derivatives:  humid-ly,  adv.,  humid-ness,  n. humidify,  tr.  v.,  to  render  humid.  —  See  humid and  -fy.')
KLN_1966.txt humour None
KLN_1966.txt humid (403, 'humid,  adj.  —  F.  humide,  fr.  L.  {h)i2midus,  ‘moist, wet’,  fr.  {h)umere,  ‘to  be  moist  or  wet’.  See')
KLN_1966.txt vehicle None
KLN_1966.txt vector None
KLN_1966.txt convex None
KLN_1966.txt way None
KLN_1966.txt always None
KLN_1966.txt wagon None
KLN_1966.txt wave None
KLN_1966.txt Norway None
KLN_1966.txt weigh None
KLN_1966.txt weight None
KLN_1966.txt ox (591, 'ox,  n.  —  ME.,  fr.  OE.  oxa,  rel.  to  OS.,  OHG. ohso,  ON.  oxi,  uxi,  OFris.  oxa,  MDu.  osse,  Du. os,  MHG.  ohse,  G.  Ochse,  Goth,  auhsa,  and cogn.  with  W.  ych,  ‘ox’,  Mir.  oss,  ‘stag’,  OI, uksa,  Avestic  uxshan-,  ‘ox,  bull’,  Toch.  B  okso, ‘ox’,  fr.  I.')
SKT.txt humor None
SKT.txt humour (234, 'humour,  orig.  moisture,  (F.  — L.)  See Trench,  Select  Glossary,  and  Study  of Words.  The  four  kumoun,  acconling  to Galen,  caused  the  four  temperaments  of miud,  viz.  choleric,  melancholy,  phlegmatic, and  sanguine.- O.  F.  kt4mor  {i .  Aumeur).')
SKT.txt humid (234, 'Humid,  moist.  iF.-L.)  F.  kumide.^ L.  kumidtts,  better  umiduj,  moist.  —  L. kumere,  umert,  to  be  moist;  cf.  mums, uuidui,  udus,  moist.  Gk.  i^^r,  moist. (VUG,  for  WAG.)')
SKT.txt vehicle None
SKT.txt vector None
SKT.txt convex None
SKT.txt way (582, "Way.  (E.)     U H.U'ey.-way.     A •^Du.  we^,  icel,  r*-^.  Dan.  vet,  S' G.   ttr^,   Golh.   wigs.  +  Lith.    tiVJ track  of  a  carl;  L.  ma ;  Skt.  xvxAd, from  vah,  to  carr^*.     See WAGH.)     Der.  al'ivay,  aJ-wayr^ way-faring,  i.e.  faring  00  the  way, weg'Urend")
SKT.txt always None
SKT.txt wagon (584, 'wagon,   waggon.   (Du)     XM Borrowed  from  Du.  Tt»agrm,  a  wagco;  whii is  cognate  with  wain  vbelowl.')
SKT.txt wave (581, 'Wave  (I),  to  fluctuate.  (E.)  M.  E. xvauen.  A.  S.  wajiafi,  csp.  in  the  sense  to wonder  at  or  waver  in  miod  ;  the  lit.  sense appears  in  the  adj.  tua/rt,  wavering,  rest- less. Cf.  Icel.  va/ra,  va^a,  to  waver ; vaftf  hesitation.  Der.  xuave,  sb.,  from')
SKT.txt Norway None
SKT.txt weigh (584, 'Weigh.    (E.)      M.E.    wgHen.     K.^.\\  "^%Vta.T«-.  sec  WUl  u).')
SKT.txt weight (584, 'weight  — A.S.  wig-,  stem  of  pt.  t')
SKT.txt ox (345, "Ox.  (£.)    M.  E.  cu.  Px*,  pt  oj 0j'(Z,  pi.  tfj:an.-^Du.  0i,  Icel.  aft, Swed.   oxt.   G.  A:4r^,  0r;^/,   Goth. auhsuft  W.  ^A  ;  Skt  uksham,  an (lit    impr^gnater).      The  Skt. derived    frum    Skt,     mJksh^     to (V  WAG.)")
```


## [2026-10-16T05:16:15.336Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \\\n'https://en.wiktionary.org/wiki/wave' \\\n'https://en.wiktionary.org/wiki/Norway' \\\n'https://en.wiktionary.org/wiki/convex' \\\n'https://en.wiktionary.org/wiki/vehicle' \\\n'https://en.wiktionary.org/wiki/humid' \\\n'https://en.wiktionary.org/wiki/humor' \\\n'https://en.wiktionary.org/wiki/weigh' \\\n'https://en.wiktionary.org/wiki/wagon' \\\n'https://en.wiktionary.org/wiki/always' \\\n'https://en.wiktionary.org/wiki/vector' \\\n'https://en.wiktionary.org/wiki/vehō' \\\n'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/weganą' \\\n'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weǵʰ-' \\\n'https://en.wiktionary.org/wiki/𐬎𐬑𐬱𐬀𐬥' \\\n'https://en.wiktionary.org/wiki/باشه' \\\n'https://en.wiktionary.org/wiki/وزغه' \\\n'https://vajehyab.com/moein/باز' \\\n'https://vajehyab.com/moein/وزغ' \\\n'https://vajehyab.com/moein/پرواز' \\\n'https://vajehyab.com/moein/باشه' \\\n; do python3 tools/fetch_source.py \"$u\" --note \"page 531: weǵʰ-/wegʷ-/vazaγā- verification\" >/dev/null 2>&1; done; tail -20 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l); print(d['status'],d['bytes'],d['file'][-25:],d['url'])\"",
 "description": "Archive more Wiktionary and Mo'in pages",
 "timeout": 400000
}
```


### [2026-10-16T05:16:25.675Z] TOOL RESULT

```
200 31979 /web/d5f2df469973d177.txt https://en.wiktionary.org/wiki/humor
200 20075 /web/9dae82fcf5cf623b.txt https://en.wiktionary.org/wiki/weigh
200 38677 /web/6081d0761d9f86e5.txt https://en.wiktionary.org/wiki/wagon
200 29439 /web/a5a527bc351f6740.txt https://en.wiktionary.org/wiki/always
200 26146 /web/cae498c32e121b2c.txt https://en.wiktionary.org/wiki/vector
-1 39 /web/3f412e0e6bee5a3e.txt https://en.wiktionary.org/wiki/vehō
200 330 /web/38c3c12d31703f88.txt https://vajehyab.com/?q=سوبلیمه&d=moein
200 5610 /web/97587e023da5b9d6.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/weganą
200 2182 /web/e720e7fcc61ab291.txt https://vajehyab.com/?q=سوژه&d=moein
200 6035 /web/658014ba821fe763.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weǵʰ-
200 1688 /web/088daaaa118a5dd5.txt https://vajehyab.com/?q=پشکم&d=moein
-1 39 /web/5409ad5dab439566.txt https://en.wiktionary.org/wiki/𐬎𐬑𐬱𐬀𐬥
-1 39 /web/1655249fb605dfcf.txt https://www.etymonline.com/word/sublime
200 4759 /web/d34791161e8bf180.txt https://en.wiktionary.org/wiki/باشه
-1 39 /web/82bac91d2eb44ff1.txt https://en.wiktionary.org/wiki/وزغه
200 909 /web/b74b6f999025d0d1.txt https://vajehyab.com/moein/باز
200 478 /web/6ed0e7d14edece5f.txt https://vajehyab.com/moein/وزغ
200 782 /web/354f64619295b6b9.txt https://vajehyab.com/moein/پرواز
200 619 /web/a0d4534b43fc6930.txt https://vajehyab.com/moein/باشه
200 5247 /web/86af466221981ad2.txt https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weǵ-
```


## [2026-10-16T05:16:30.470Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in b74b6f999025d0d1 6ed0e7d14edece5f 354f64619295b6b9 a0d4534b43fc6930; do echo \"## $f\"; sed -n '6,$p' $f.txt | tr -s ' \\n' ' ' | cut -c1-700; echo; done; grep -n -E 'From|Proto|Etymology' d34791161e8bf180.txt | head -8; for u in wave Norway convex vehicle humid humor weigh wagon always vector; do f=$(grep -F \"\\\"https://en.wiktionary.org/wiki/$u\\\"\" index.jsonl | tail -1 | python3 -c \"import sys,json;print(json.loads(sys.stdin.read())['file'])\"); echo \"## $u\"; grep -m3 -E '^ *(From|Borrowed|Inherited|Alteration|Back-formation|Partly)' $f | cut -c1-500; done",
 "description": "Read Mo'in and Wiktionary etymologies"
}
```


### [2026-10-16T05:16:31.594Z] TOOL RESULT

```
## b74b6f999025d0d1
معنی باز | فرهنگ انتشارات معین | واژه یاب 26 فرهنگ همه دیکشنری مترادف طیفی آزاد + همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه باز فرهنگ انتشارات معین [ فر. ] ( اِ.) اجسامی جامد و سفیدرنگ و بسیار نمگیر که در آب بسیار حل می شوند و در اثر گرما خیلی زود گداخته می گردند. باز در فرهنگ‌های دیگر معنی باز در لغت‌نامه دهخدا معنی باز در فرهنگ فارسی عمید / قربان‌زاده معنی باز در دیکشنری فارسی به عربی معنی باز در دیکشنری فارسی به انگلیسی معنی باز در دیکشنری فارسی به ترکی معنی باز در واژه‌های مصوب فرهنگستان معنی باز در گویش مازنی معنی باز در فرهنگ مترادف و متضاد معنی باز در فرهنگ فارسی طیفی معنی باز در واژه‌نامه آزاد معانی دیگر باز باز (2) باز (3) باز (4) باز (5) باز (6) واژه‌های مشابه باز یافتن باز نم

## 6ed0e7d14edece5f
معنی وزغ | فرهنگ انتشارات معین | واژه یاب 26 فرهنگ همه دیکشنری مترادف طیفی آزاد + همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه وزغ فرهنگ انتشارات معین (وَ زَ) [ په . ] (اِ.) = وزق : قورباغه . وزغ در فرهنگ‌های دیگر معنی وزغ در لغت‌نامه دهخدا معنی وزغ در فرهنگ فارسی عمید / قربان‌زاده معنی وزغ در دیکشنری فارسی به عربی معنی وزغ در دیکشنری فارسی به انگلیسی معنی وزغ در فرهنگ مترادف و متضاد خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره نسخه جدید

## 354f64619295b6b9
معنی پرواز | فرهنگ انتشارات معین | واژه یاب 26 فرهنگ همه دیکشنری مترادف طیفی آزاد + همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه پرواز فرهنگ انتشارات معین (پَ) ( اِ.) 1 - پرش ، پریدن . 2 - تخته های باریکی که روی سقف کنار هم می چینند و حصیر یا پوشال را روی آن می اندازند. پرواز در فرهنگ‌های دیگر معنی پرواز در لغت‌نامه دهخدا معنی پرواز در فرهنگ فارسی عمید / قربان‌زاده معنی پرواز در دیکشنری فارسی به عربی معنی پرواز در دیکشنری فارسی به انگلیسی معنی پرواز در دیکشنری فارسی به ترکی معنی پرواز در گویش مازنی معنی پرواز در فرهنگ مترادف و متضاد معنی پرواز در فرهنگ نام‌ها واژه‌های مشابه پروازه پتواز پدواز پرازده پرداز پردازش چهره پرداز بداهه پرداز دروغ پرداز غزل پرداز خرید اشتراک افزودن واژه افزونه مرو

## a0d4534b43fc6930
معنی باشه | فرهنگ انتشارات معین | واژه یاب 26 فرهنگ همه دیکشنری مترادف طیفی آزاد + همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه باشه فرهنگ انتشارات معین (ش ِ) ( اِ.) یکی از پرندگان شکاری کوچکتر از باز، با چشمانی زرد رنگ ، که رنگ پشتش خاکستری تیره و شکمش سفید با لکه های حنایی است . قرقی ، قوش . باشه در فرهنگ‌های دیگر معنی باشه در لغت‌نامه دهخدا معنی باشه در فرهنگ فارسی عمید / قربان‌زاده معنی باشه در گویش مازنی واژه‌های مشابه بااهمیت باجه باخه باده باده پخته باده پرست باده پرستی باده پیما باده خام باده گسار خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره نسخه جدید

62: Etymology 1 
71: Etymology 2 
82: Etymology 1 
88: Etymology 2 
163: From Wiktionary, the free dictionary
168: Etymology 1
183: Etymology 2
196: Etymology 1
## wave
ugrep: warning: data/verification/sources/web/cf2b22eff0c1f0d6.txt: No such file or directory
## Norway
ugrep: warning: data/verification/sources/web/88e0fff7ea074a99.txt: No such file or directory
## convex
ugrep: warning: data/verification/sources/web/eaa960da4711aa5c.txt: No such file or directory
## vehicle
ugrep: warning: data/verification/sources/web/a05098781fa90bd0.txt: No such file or directory
## humid
ugrep: warning: data/verification/sources/web/6d7ce72e5d1dbbc7.txt: No such file or directory
## humor
ugrep: warning: data/verification/sources/web/d5f2df469973d177.txt: No such file or directory
## weigh
ugrep: warning: data/verification/sources/web/9dae82fcf5cf623b.txt: No such file or directory
## wagon
ugrep: warning: data/verification/sources/web/6081d0761d9f86e5.txt: No such file or directory
## always
ugrep: warning: data/verification/sources/web/a5a527bc351f6740.txt: No such file or directory
## vector
ugrep: warning: data/verification/sources/web/cae498c32e121b2c.txt: No such file or directory
```


## [2026-10-16T05:16:36.535Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in wave Norway convex vehicle humid humor weigh wagon always vector; do f=$(grep -F \"\\\"https://en.wiktionary.org/wiki/$u\\\"\" data/verification/sources/web/index.jsonl | tail -1 | python3 -c \"import sys,json;print(json.loads(sys.stdin.read())['file'])\"); echo \"## $u $f\"; grep -m3 -E '^ *(From|Borrowed|Inherited|Alteration|Back-formation|Partly)' $f | cut -c1-450; done; f=data/verification/sources/web/d34791161e8bf180.txt; sed -n 165,200p $f | grep -v '^\\s*$' | cut -c1-300",
 "description": "Read Wiktionary English etymologies"
}
```


### [2026-10-16T05:16:37.449Z] TOOL RESULT

```
## wave data/verification/sources/web/cf2b22eff0c1f0d6.txt
 From Wiktionary, the free dictionary
 From Middle English waven , from Old English wafian ( “ to wave, fluctuate, waver in mind, wonder ” ) , from Proto-West Germanic *wabōn , from Proto-Germanic *wabōną , *wabjaną ( “ to wander, sway ” ) , from Proto-Indo-European *webʰ- ( “ to move to and from, wander ” ) .
 From Middle English *wave , partially from waven ( “ to fluctuate, wave ” ) (see above) and partially from Middle English wawe , waghe ( “ wave ” ) , from Old English wǣg ( “ a wave, billow, motion, water, flood, sea ” ) , from Proto-Germanic *wēgaz ( “ motion, storm, wave ” ) , from Proto-Indo-European *weǵʰ- ( “ to drag, carry ” ) . 
## Norway data/verification/sources/web/88e0fff7ea074a99.txt
 From Wiktionary, the free dictionary
 From Middle English Norwey , Norweye , Northwey , Norweȝe , Norewæiȝ , Norwæge , from Old English Norþweġ , a calque of Old Norse Norðvegr ( “ north way ” ) , from norðr ( “ north ” ) + vegr ( “ way ” ) , contrasted with suðrvegr ( “ south way ” ) , i.e. , Germany , and austrvegr ( “ east way ” ) , the Baltic lands. Norwegian (1607) is from Medieval Latin Norvegia , with the -w- from Norway . By surface analysis , nor(th) +‎ way .
 Borrowed from English Norway 
## convex data/verification/sources/web/eaa960da4711aa5c.txt
 From Wiktionary, the free dictionary
 Borrowed from Middle French convexe , from Latin convexus ( “ arched ” ) .
 Borrowed from French convexe , from Latin convexus .
## vehicle data/verification/sources/web/a05098781fa90bd0.txt
 From Wiktionary, the free dictionary
 Borrowed from French véhicule , from Latin vehiculum ( “ a carriage, conveyance ” ) , from vehō, vehere ( “ to carry ” ) .
## humid data/verification/sources/web/6d7ce72e5d1dbbc7.txt
 From Wiktionary, the free dictionary
 Borrowed from Old French humide , from Latin humidus ( “ moist ” ) . Via Proto-Indo-European *wegʷ- ( “ wet ” ) related to English weaky .
## humor data/verification/sources/web/d5f2df469973d177.txt
 From Wiktionary, the free dictionary
 Borrowed from Latin hūmor, hūmōrem .
 From Latin (h)ūmor ( “ fluid ” ) . Doublet of humør ( “ spirits, mood ” ) . The modern use of this word for mental processes goes back to Ancient and Medieval theories about the four fluids of the body.
## weigh data/verification/sources/web/9dae82fcf5cf623b.txt
 From Wiktionary, the free dictionary
 From Middle English weyen , from Old English wegan , from Proto-West Germanic *wegan , from Proto-Germanic *weganą ( “ to move, carry, weigh ” ) , from Proto-Indo-European *wéǵʰeti , from *weǵʰ- ( “ to bring, transport ” ) .
## wagon data/verification/sources/web/6081d0761d9f86e5.txt
 From Wiktionary, the free dictionary
 Borrowed from Middle Dutch wagen , [ 1 ] from Old Dutch *wagan , from Proto-West Germanic *wagn , from Proto-Germanic *wagnaz ( “ wagon ” ) , from Proto-Indo-European *weǵʰ- ( “ to transport ” ) . Generally displaced native cognate wain , from Old English wæġn , of which it is a doublet. Related also to way , weigh .
 Borrowed from English waggon , itself from Middle Dutch wagen . Doublet of wagen .
## always data/verification/sources/web/a5a527bc351f6740.txt
 From Wiktionary, the free dictionary
 From Middle English alweyes , alwayes , alweys , a variant of Middle English alwey , alway ( “ always ” ) , from Old English ealneġ , ealne weġ ( “ always, perpetually ” , literally “ all the way, all the while, continuously ” ) , from ealne + weġ ( accusative case ) , equivalent to alway +‎ -s . Cognate with Scots always ( “ always ” ) , Low German allerwegens ( “ very often ” , literally “ all ways' ” ) . More at all , way .
## vector data/verification/sources/web/cae498c32e121b2c.txt
 From Wiktionary, the free dictionary
 From vehō ( “ carry, bear, convey; ride ” ) + -tor .
 Borrowed from French vecteur , Latin vector .
 Ottoman Turkish
 [ edit ] 
 Etymology 1
 [ edit ] 
 Noun
 [ edit ] 
 باشه • ( başa ) 
 alternative form of پاشا 
 References
 [ edit ] 
 Redhouse, James W. ( 1890 ), “ باشه ”, in A Turkish and English Lexicon ‎ [1] , Constantinople: A. H. Boyajian, page 326 
 Etymology 2
 [ edit ] 
 Noun
 [ edit ] 
 باشه • ( başa ) 
 dative singular of باش ( baş ) 
 Persian
 [ edit ] 
 Etymology 1
 [ edit ] 
 From earlier باشد ( bāšad , imperative of بودن , literally “ let it be ” ) .
```


## [2026-10-16T05:16:41.307Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 217 391 2278 2279; do echo \"######## BQT:$p\"; python3 tools/ref_page.py BQT:$p --image 2>&1 | head -80; done",
 "description": "Fetch BQT cited pages OCR",
 "timeout": 300000
}
```


### [2026-10-16T05:16:47.275Z] TOOL RESULT

```
######## BQT:217
no scan of BQT covers printed page 217 (see 'scans' in refs_online.json)
######## BQT:391
no scan of BQT covers printed page 391 (see 'scans' in refs_online.json)
######## BQT:2278
(no exact page map; using offset -1917 -> pdf page 361; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2278.png
REF: BQT:2278  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 361  OCR-lang: fas

ورب -۲۷۸-
وردیب! « بنم اول » بر وزن و معنی ود یز - بکر اول بروزن ستیز» صمغ
ارب است که کج و محرف باشد وبترکی قیقاج | درخت الب (۱) است ؛ وبسنی کوبند افاقیا است
باشد .
بیان نهم
وز ان؟ « بروزن خزان» بممنی جهنده | وواو بهم تبدیل می‌بابند وبمریی عظیم کویند.#
باشد عموماً -وتموج هواراگویند خصوضاً . وزغ۱۹ « بفتح‌اول وئالی وغین نقطه‌داره
ز رانی ۴ اش برد لوعی از چلپاسه ی
وزن مفراشکن , بلفت زند و پازد (۷) نی ۱ است که ریز و۹ .از
۰ ۵ : | وی زهرقاتل‌است, وزغه
وزرگی نم اول وتالی + بر دت | اکن درمیان شراب افتند و بمیرد آن شراب هم
ومعنی بزر که است چه درکلام فارسی بای‌ابجد | زهر قاتل کردد .
)۱( خم۳: آرب. )«( چك : ژد ویاژاد .
۹- ارب (و.م.) - اآوریب (و.م.) آوریو (و.م.) ۶ ورب » کژی باشد برخوهلی
(< کجی) بود اعنی نه راستی نه سنخت بشیب » بوشکور( بلخی ) گفت :
توالی برو کار بدتن فرب که نادان مه راست بیند ویب.ع
2 لغت فری ص۲۹ » ورك: فعرمت ولف ۰
و رك : التفهیم ص ۱۷۹ و مقدمهٌ آن ص قفد . مرحوم بهار نوشته‌اند : ۶ ظ . وراب عربی است
بمعنی اریب پعنی محرف > « سبك شناسی اج ۳ص ۳۶ > درعربی « الوراب ککناب » الاتخراف
(پوند صفت فاعلی). ۴ - هز ۰۷۵2۲۵211۵0 پپلوی 501127 [580450820] بممنی
رفتن « ,ونکن ص۷۷ ».
محر كة . کربه با جانوری است شبیه کربه » سمیت بها لخفتها وسرعة حرکنتها » وزغ بحذف تا
و اوزاغ و وزغان بالکر و وزاغ ککتاب وازغان بکسرالهمزة جمع .> « منتهی‌الارب >.
2 وزغ - بفتح اول و دوم ۳ بزغ « فاب۱ اص ۱۹۹*؛معرب آن وزغه ( اوعی‌چلپاسه )
(«.م.) » اوستا -۷822808-۰۷2228802 (قورباغه) « بارتولمه ۱۳۸۹ » پهلوی ۷22285 ۰
8 کردی ع۷1240 ( قورباغه ) « اسشق ۱۳۸۲ سمنانی ۰۷8۳200 کیلکی802:2؛
(ر4 : وزق) قورباغه » غوك » ضفدع .

######## BQT:2279
(no exact page map; using offset -1917 -> pdf page 362; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2279.png
REF: BQT:2279  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 362  OCR-lang: fas

-۷۷۷۹- وژنگه

ورزق٩‏ ‌- بفتح اول وئالی وسکون‌قاف, وزمه* ‌- بفتح‌اول ومیم وسکون ثالی.
معروف است و اورا فوك خوانند وبمربی شفدغ | آخر فضل زمستان راکوبند چه وزمه باد» بادی
گوبند؟ . باشد که درآخر زمتان وزد .3

وزك - بنتح اول والی وسکون کاف, زیر « با ثالك مجهول بروزن زریس ۰
درخت پده را کویند؟ , وآن درختی است که ۲ زردچوبه را کوبند۹ - وبا ثالك معروف‌درعربی
هرکز بارندهد و بعربی غرب خوانند . کوبند | بمعنی دستورباشد۷ .
اکر شخصی را زلو بگلو رفته باشد آب بر که وزیری* - بروزن امیری » نوعی از
آبراگرفته برحلق او ریزند برآید۴ . انجیرباغد وآن میوه‌است معروف +

بیان دهم

وژن - بفتح اول و ثالی بروزن چمن » وژ نگ < بنم اول بر وزن تفنگه .
کنافت ونجاست را کوبند ‎٩‏ . توژی*۱ باشد جگری رنگ که برپایین تیریعنی

۱- موّلف سراج نوشته : « وزغ , بفتحتین غوك » وبقاف که شهرت گرفته لهجدعراقیان
است و صاحب برهان حرف اصلی پنداشته با آنکه مکرر نوشته که قاف در فارسی لیست .بقل
« فرهنگه نظام ج ۵ ص مب >. : ۴ - رك : وزغ » وزغه ۰ ۴ -رك4 : یده ۰

۴ - « وز4 بوزن و معنی وزغ >« رشیدی >. 8 - *زم» بمعنی سرماست. ر4:
زمتان ؛ ظ. «و» اول زاید وحرف عطف است . ‎٩‏ - مصحف « زربر».

۷ -کلمه معرب است « اسشق ۰۱*۸۶ از ۷101۲ ( با ۷۵17 ) پپلوی ۸« باروچا ۳۳۶
ار اوستایی ۷1178 قتوی دهنده 3 پورداود . خرده اوستا ص ۷۸ ۰5 آرمنی ۷1۳ » لیز آرمنی
7 * فارسی 8121۲ ( دهخدا » ریش‌مفید ده » محصل مالیات ) » -ربانی 862178[/6(ژاندارم)
( 542 .7۶ ,62 .86,0نا۸82 ,11011288 ) در خصوص « وزبر » ر4 : ,878146166
.4 ,53 . 1780 « هوبشمان ۱۶۸۶ * در فارسی 8621۳ , 8121۲ فقط در يك بیت ابوالمعانی
آمده « اسشق شماره ۱۶۸۶4 ۰ ص ۲4:۲ ۲ 4 از: وزبر(ه.م.) ۳ ی(نسیت)

: ‏-قی : وس‎ ٩

از آن ز زرق وربا گشت ظاهرش طاهر که از نفاق درونت (درواه) وژن‌نمیداند.
رضی‌الدین لیشاپوری «رشیدی» « فرهنگه نظام *.

*- در جهانگیری و رشیدی : توز (ه.م.)

وزیدن - بفتح اول و چهارم » از : وز ۳ یدن ( پسوند مصدری ) * پزیدن (ه.م.)»
رشهٌ هندی باستان ۷۵ , ۷۸881 ( وزیدن[ ,اد ]) ۸ اسشق ۱۳۸۳ ؛پهلوی ۷221)]8ءاففانی
[ها۷۵ ( پریدن ) ( ۳ خخص ۷821 ) « هوبشمان ۱۰۸۳ ريشهٌ اوستایی -۷82 ( رفتن )
«بار تولمه ۸۹۸۹ »؛ کردی ۷۱20 ( طنین افکندن » وزیدن د ژایا ی 2۸۳۷ ۰ کیلکی
7 (جت , جهیدن )؛ جنبیدن هوا » حر کت کردن نسیم و باد.
```


## [2026-10-16T05:16:53.885Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='ignore').read().split('\\f')\nimport re\nfor lo,hi,pats in [(425,450,['باشه','واشه','باز']),(600,625,['پرواز','وازیدن','parvaz','parwaz'])]:\n    for i in range(lo,hi):\n        p=t[i]\n        for pat in pats[:2]:\n            for m in re.finditer(pat,p):\n                print(i,pat,repr(p[max(0,m.start()-200):m.start()+300]).replace('\\\\n',' ')[:520]); break\nEOF",
 "description": "Search BQT vol1 for bâše and parvâz"
}
```


### [2026-10-16T05:16:54.437Z] TOOL RESULT

```
438 باشه 'فته\u200cاند. «نداب ۳ : ۳- 4. فرامرزی» ورلك : داگرةالمعارف فرانه . شه ازسفحهة ۲۱۷ همچنان\u200cسنگ یکه اوراسیلکرداند زکوه \u200f کاء زین\u200cسوگاه آ نس وکه فرازوگاه باز کامرهواری\u200cچ و کبك و کامجولان\u200cچونفاب \u200f گاه\u200cبرجستن چوباشه گاءب رکشتن\u200cچوباز. «فرهنک شاهنامه 4۰-۳4» 2 باریدت - پپلوی ۷۵1020 «بندهش۱۳4» مشتق ازمسدر اوستابی۷۵۲ (باریدن)«بارنولمه ۰ استی ۱۷۵۲15 «. است۱۳۸»» کیلکی 1#46600؛ فرودآ مدن قطراتآب ازابر» بارش, آعدن,'
441 باشه 'زن\u200cداستان . گیندو کته و قدیيم و دیرنه را کوبند ۴ و کنابه از دبا و عالم و دهر و گردون هم هست - و بزبان\u200cدری باشامه . تاریخ را کویند که احوال پیتینیان باشد 9 - و بمعتی مجرد هم\u200cبنظر ؛مده که از ترك وتجرید باشه ۷ . پاستان\u200cنامه پانون بالف کشیيده\u200cوميم مفتوح . نام کتابیست از تاریخ فارسیان ۷ . باستی بروزن\u200cراستی ؛ بمعتی\u200cافتاد کی و فروتنی باشد . باسر ۸ - بفتح رای\u200cقرشت وسکون\u200cيم » زمینی را کون دکه بجهت کشت و زراعت کردن آماده و مهیا کرده باشند - و کشت زار را نیز کوشد ۸ پاسر ه \u200c ب
446 واشه ' آید ودرد نمیکندء آنرا بعربی تولول خوانند - و ممعنی آواز حزمن هم آهدم است \u200f با لو اسه بروژن\u200cشاه کاسه ۰ بمعنی\u200cثار باشد که در مقابل بود ی دالوافه - بر وزن آسمانه . مرغکی باشد کوچكوسیاه کدشیر ازبانآ نراهواشه» کوشد. بالوایه - بنتح بای حطی . پرستول باشد و آن برنده است در سقف خانها آشیان کند ۷ . و به\u200cضی گویند پر نده\u200cایست کوچك وراه و کوتاه پاچه که شب و روز در پرواز میباشد مگر درهنگام بجه کردن که بسوراخی رودوا کر برژعن اد زتو اند بر خاست و آ را بعر ی ابایل گوشد. . باوث « نم الت ر سکون واو و دال, ع
603 پرواز 'ازند وپر از ظه کنند - و پیراستن درختان را یز گویند بعنی بربدن خاخهای زبادئیآ ترا تا باندام شو ونم کنند . رخیده - بر وژن فهسده : بىعتی رمز و ایما و اثارت باشد ۴ . رد ه بفتح اول و انی و سکون تال . یعنی پرواز کند؟ - و بسکون ثانی بمعنی لای ونه جامه و کانن باشدچنانکه گویند ملپرد ودو ۱ - مرکب از : پر - اوستا :025 ( پیرامون ) + چن (از : چیدن ) جمعاً یرامون چیده ؛ طبری و ماز ندرانی کتونی 0 دواژه\u200cنامه ۲۱٩۳\u200f » کیلکی یز 0« ۴ یز بممنی شمشیر. رك: لفت\u200cنامه . ۴ - از ساخته\u200cهای دساتیر « غاب ۱ : 4۷ 4 د فرهنکگ دس
615 پرواز 'و قری وییم وباگك٩\u200f -و سروب رکه را نی زکوین و بمعنی داشتن (۱) و فرات - و پرداخت - و پرورش - و پرواز هم آ مده\u200cاست. رواد ۲ « بر وزن خروار » جالوری بائد کهآ نرا در جای خوبی بندلد و خوراك لابق دهند نا فربه شود - وخانهة تابسئانی\u200cوخاناباد گیر دار را نیز گویند بهء\u200cنی اطراف آن ثمام پنجره داشته باشد - و خانه\u200cای را نیز گوبند که\u200cبربالای خالاً ددگر ساخته باشند و اطرافآن بازباشد - و بمعن ی گنجینه هم آمده'
```


## [2026-10-16T05:17:00.203Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='ignore').read().split('\\f')\nfor i in [436,437]:\n    p=t[i]\n    for m in re.finditer(r'باز',p):\n        s=p[max(0,m.start()-60):m.start()+250].replace('\\n',' ')\n        if any(k in s for k in ['شکار','پرنده','اوستا','پهلوی','vaz','۷۵']): print(i,s); print('--')\nfor i in range(605,616):\n    p=t[i]\n    for m in re.finditer(r'پرواز',p):\n        s=p[max(0,m.start()-80):m.start()+300].replace('\\n',' ')\n        if any(k in s for k in ['اوستا','پهلوی','pari','۷۵','پر +','از : پر']): print(i,s); print('--')\nEOF",
 "description": "Locate BQT footnotes for bâz and parvâz"
}
```


### [2026-10-16T05:17:00.570Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:17:04.014Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='ignore').read().split('\\f')\nfor i in range(430,440):\n    if 'شکار' in t[i] and 'باز' in t[i]:\n        for m in re.finditer(r'شکار',t[i]): print(i, t[i][max(0,m.start()-250):m.start()+200].replace('\\n',' ')); print('--')\nEOF",
 "description": "Search BQT vol1 near p217 for hunting bird"
}
```


### [2026-10-16T05:17:04.417Z] TOOL RESULT

```
437 ی - ازاینباره گفتاربسیار گشت. قردوسی‌طوسی. و فاف بواو رسیده و بنون زده ۰ بيونالي‌دوایست که نرا شو کران‌خوانند» وآن نخم بینروهیست» و از تفت که از ولایت بزد است آورند و آنرا دوري تقتی کویند . پا » بر وزن از , پرنده‌ایست مشهور و »مروف که سلاطین و اکابر شکار فرمابند ۷ - و کتادکی میان هر دو دست را نیز گومند چون از هم بکثایند و آنرا نیز بترکی قلاح خوانند و بحربی ماع کوبند ۸ و باین معنی با زای فارسی‌هم آ مدهاست - و شبر و وجب رانیز کفته‌اند و آن مقداری ب
--
439 ا نرکان قزل قوش خوانند ۴ ۰ پاز خمید ‏ بکس میم وسکون‌نحنالی و دال , کیکه بسوان طعنه صدارت کی کند و یکنابه مشن شخصی را یاز نماید کوبند « باز خمید » یمنی بطمنه سخن او را کفت و صدارت او کرد . باردار - بر وزن رازدار ۰ برزیگر و زراعت کننده را گوبند - و میرشکار و صیاد ونگاه دارندث باز را عم کقته‌اند ٩‏ - وشخصی را نیز کوب دکه مردمرا از کاری وازچیزی بازدازد و منم کنه - وامر ببازداشتن و خنم . کردن عم 2 باژ۵اد - بای فارسی بر وزن تانجداره بمعنی بلجبان باشد ب
--
```


## [2026-10-16T05:17:07.902Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='ignore').read().split('\\f')\np=t[437]; i=p.find('۷ -'); \nimport re\nfor m in re.finditer(r'(?m)^\\s*۷\\s*-',p): print(p[m.start():m.start()+600].replace('\\n',' ')); print('==')\nprint(p[-1800:].replace('\\n',' '))\nEOF",
 "description": "Read BQT p217 footnote 7"
}
```


### [2026-10-16T05:17:08.430Z] TOOL RESULT

```
 وحریی‌ابین خوانند ۲- وهر چیز زشت را یز گویند- و بعنی زلف هم هبت- و گله و رمة کاو و گوسفند واسب وامثال آن باشد. و اسپ را یز گوبند که بعربی فری خواند ؟ . بارخ فهم - کنابه از فكك نهم‌است که فكك‌الافلاك باشده و آترا بعربی عرش‌خوانند. بادی ه بر وزن جاری ۰ نامیست از نامهای خدابمالی جل‌جلاله ۴ و کاهی بر ملوه و سلاطین. یز اطلاق کنند - و نام قصبه‌ایست در حندوستان - و دیوار فلعه و حصار شپرباشد ۵ . و از برای تقلبل و انحصار هم هست همچو التصه همچو: یکباری ودو سه باری - و بمعنی گاهی وایامی هم آهده ابت - و کمبتین قلب را نیز گویند و هر چیزیکهپربار وسنگین‌باشد ٩‏ ۶ باد ون -بکس اكب و سکون‌نستانی - ازاینباره گفتاربسیار گشت. قردوسی‌طوسی. و فاف بواو رسیده و بنون زده ۰ بيونالي‌دوایست که نرا شو کران‌خوانند» وآن نخم بینروهیست» و از تفت که از ولایت بزد است آورند و آنرا دوري تقتی کویند . پا » بر وزن از , پرنده‌ایست مشهور و »مروف که سلاطین و اکابر شکار فرمابند ۷ - و کتادکی میان هر دو دست را نیز گومند چون از هم بکثایند و آنرا نیز بترکی قلاح خوانند و بحربی ماع کوبند ۸ و باین معنی با زای فارسی‌هم آ مدهاست - و شبر و وجب رانیز کفته‌اند و آن مقداری باشد از دست صاین ح انگشت کوچك وانکشت‌شمت و دوش و بازو ؛ و مك‌بند انگشت را یز گویند- وبمعنی تکرار و معاودث و دیگرهم هست ٩‏ چنانکه کوشد: «بازیگو» بعنیمکرربگو و«بازچه میگوید؟» ,عنی‌دنگرچه میگوید؟ - و بازنده و بازی کننده را ی زگویند همحو: قمارباز و رسمان‌باز وشب‌باژ و امثالآنب و امر ببازی‌کردن هم آمده است معنی بباز و بازی کن - و بمعنی کشاده هم هست که دد «قابل بسته باشد- وشیب رائیز کوبند *۱ که ؟ -_ پپلوی02۲2](مر کوب): ۵ - رك:پارو وبار.. ٩‏ - ر:بار. ۳ 7 «قاب ۱ بش نگار. فرخی. آمدت نوروز و آعد جشن نوروزی فراز شاخ کل‌شطرنج‌سیمین وعقیقین گشتهاست ای خداو ندی که تا تو ازعدم «ىدا شدی آفرین زآن مر کبی کو بشنود در تیم‌شب کامگارا !کار کیتی نازه از س رکیر باز وفت شبگیران بنطع سبز برشطرنج باز بته‌شد درهای‌بد, خما تلا گت باز بانگه پای مورچه در زبر چاه‌شست باز بقه در سفحهٌ ۲۱۸
```


## [2026-10-16T05:17:13.564Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='ignore').read().split('\\f')\np=t[438]; i=p.find('بقیه'); i2=p.find('شه ازسفحه')\nprint(p[-2200:].replace('\\n',' '))\nEOF",
 "description": "Read BQT p218 footnote continuation"
}
```


### [2026-10-16T05:17:13.873Z] TOOL RESULT

```
با ۱ - ۷۱۸ - و باع و قلاح راکوند . وآن مقداری باشد از سرانگشت میانین دست راست ناسر انگشت‌میافین دست چپ وقترکهرستهاراازهم بگشایند ۴ - وجمعنی دوشو بازوویك‌بندانگشت‌هم‌همت ۴ -وخاموشيی باشد که فان در وفت بدن شستن وچیزی‌خوردن بعد از زمزمه آختبار کنند ۴ ونام فربه ابست از قرای طوی ومعرب آن فاز است . گویند تولد ۱ حکیم فردوسی از ] تجاست . پاد اه با زای بالف کشیده . نود استیی باشدبموجب‌قرارداد زراشت‌بهرام ۵, وهراسنیری چهارمتفال است -٩‏ وبممنی دیگر ییا هم هست یمنی بازیا . *# باز آزردن. کابه از فابدث خاط خواه کردن باشد ۷ . ۱ باز ار خاك - بکررای‌بی‌هطه وخای قض فراز باشد - وبازماندن و واماندن بمعنی طرمیدن هم هست- و بمعنی تمیز کردن وغرقه لمودن میان درچیز باشد - و پمعتی جداه‌عت _که بربی فصل کوبند - و بمعنی عکس و قلب نیزآمده است - وشراب راهم میگوبند که‌بعریی خمر خواشد - و سوی و طرف و جالب را یز کنته اند - و پیعتی گذر کاه سل هم آمده است - وباج وخراج‌را لیز کویند, و باینمعنی بازای فارسی هم‌درست ات باز س بنزای فارسی » بروزن و «حنی‌باج و خراج باشد. و آن زرست که زبر دستان از زبردسان گپررند بمنی پادشاهان یزركك ازیادشاهان کوچك‌سنانند ؟ ؛ومالیکه حکام از رعابا وراهدار از سودااگر گرند - و جزبه را نز گفته اید» وآن زری باشد که ملمانان ازکافران‌یگ ود - ن‌ بازار - در پهلوی و [در: هوحتان واچار ‌ سوق‌الاحواز ۰ رك 0 خوزستان ] ( یز 02227 .م ) » فریزندی ویریی 2286 , نطنزی 9202۲ «ه . ۱ص ۲۹۰ > , ممنانی ۲ منگری ۷۵28۲ , سرخه ؛ لاسگردی و شهمیرزادی 08226 « د . ۲ ص ۱۸۸ استی 08226 ده . استی 6۱۱4 ؛ محل خرید و فروش‌کالا وخوراك وبوشالك. لغت فرانة 27هت . از پرقالی کرفته شده و پرتفالیان یز از ابرانیان گرفته‌اند. «نداب ۳ : ۳- 4. فرامرزی» ورلك : داگرةالمعارف فرانه . شه ازسفحهة ۲۱۷ همچنان‌سنگ یکه اوراسیلکرداند زکوه ‏ کاء زین‌سوگاه آ نس وکه فرازوگاه باز کامرهواری‌چ و کبك و کامجولان‌چونفاب ‏ گاه‌برجستن چوباشه گاءب رکشتن‌چوباز. «فرهنک شاهنامه 4۰-۳4» 2 باریدت - پپلوی ۷۵1020 «بندهش۱۳4» مشتق ازمسدر اوستابی۷۵۲ (باریدن)«بارنولمه ۰ استی ۱۷۵۲15 «. است۱۳۸»» کیلکی 1#46600؛ فرودآ مدن قطراتآب ازابر» بارش, آعدن,
```


## [2026-10-16T05:17:19.771Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='ignore').read().split('\\f')\nfor i in range(600,625):\n    p=t[i]\n    hdr=p[:60].replace('\\n',' ')\n    for m in re.finditer(r'پرواز\\s*[-ـ«]',p):\n        print(i,hdr,'|',p[m.start():m.start()+300].replace('\\n',' '))\n    for m in re.finditer(r'parv|pairi|para.?v',p): print(i,'LATIN',p[max(0,m.start()-150):m.start()+150].replace('\\n',' '))\nEOF",
 "description": "Locate BQT parvâz entry around p391"
}
```


### [2026-10-16T05:17:20.236Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:17:24.038Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='ignore').read().split('\\f')\nfor i in range(590,640):\n    p=t[i]\n    if re.search(r'پرواز',p):\n        c=len(re.findall('پرواز',p)); print(i, c, re.findall(r'[-–]\\s*[۰-۹]{3}\\s*[-–]',p[:200]), p[:80].replace('\\n',' '))\nEOF",
 "description": "List BQT leaves mentioning parvâz"
}
```


### [2026-10-16T05:17:24.397Z] TOOL RESULT

```
592 1 [] پتفوز ود « بافا بروزن سردوز" کردا کرد دهان + منفارمرغان باشد ۱ و کردا کرد کلاهوا
597 1 [] مت ۳۱۲ فد ۱۵ - بروزن‌فرسود؛ بمععنی‌سلامت باشد - و بمعنی وداع فیزآمده است - لف‌4۵
603 1 [] پر یی ۱ ۰ بر وژن پروین ؛ حساری باشد که از خاروخللاشه وشاخ درختان بر دورباغ وفالی
615 2 [] و قری وییم وباگك٩‏ -و سروب رکه را نی زکوین و بمعنی داشتن (۱) و فرات - و پرداخت -
628 1 [] سا نیدن- بروزن «سانیدن, آب دادن باغ وزراعت را کویند ۱ . بی‌او کند . با واوه بروز
```


## [2026-10-16T05:17:34.367Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '\\*?ṷ?waz|\\*waz-|\\*vaz' CHEUNG.txt | head -8; sed -n 5798,5803p HUB.txt; python3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='ignore').read()\npages=t.split('\\f')\nfor w in ['وزیدن','پرواز','وزغ','باز ']:\n    for i,p in enumerate(pages):\n        for m in re.finditer(w,p):\n            s=p[max(0,m.start()-100):m.start()+300].replace('\\n',' ')\n            if re.search(r'wegh|weg|uegh|vaz|waz|POK|پوکورنی',s,re.I):\n                tag=re.search(r'\\[pdf page (\\d+)\\]',p); print(w,i,tag.group(1) if tag else '',s[:400]); break\nEOF",
 "description": "Grep Cheung, Hübschmann, Aryanpur"
}
```


### [2026-10-16T05:17:34.841Z] TOOL RESULT

```
13562:*NEIR: Oss. I. wazyn/wagd, D. wazun/wagd ‘to leave behind, abandon; throw’ 
15136:*аџа-) Orm. uZnaw-/uZnawok, wazn-/wazyok ‘to kill’ 
18817:roll, turn’. In fact it should rather be read as the very common verbal form /wazend/ 
26178:*MIDDLE PERSIAN: MMP w’c, w z, ВМР w'c /waz/ ‘word, speech’ || (+ *abi-) BMP 
26179:’yw’c, ’dw’c /ewaz/ ‘word, utterance’ || (+ *a-) MMP ’w’c- ‘to call’, MMP ’’w’g 
26180:‘voice, speech’, BMP ’p’c /awaz/ ‘sound, voice, language’ || (+ *pati-) MMP 
26181:pyw’c-, BMP ptw’c- /paywaz-/ ‘to answer’ || (+ *ni-) MMP nw’cysn ‘kind 
26238:nowaz-/nowext ‘to swear, curse’ (< NP Tadj.) || (+ *4-) Sariq. awuj ‘voice, sound’ (< 
270, zd. "^vaxsahara- ; varj 'Grosse, Wiirde' = phi. varc Guj.
Abal. 73, skr. vdrcas- ; vardij ^Wachtel', skr. vdrtika-, var-
taka^; vary = bary *Wasserwehr, skr. varga- 'Abwehrer ;
vazay Trosch* ^^ zd. vazaya-; vantdan 'wehen', skr. vah
'dahinfahren , wehen*; vaztr 'Vezir', aus dem Arabischen
zuriickentlehnt, vgl. Horn Nr. 1084, oben p. 105; vtr'Vei'
```


## [2026-10-16T05:17:38.649Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^\\*?wa[jz]\\b|\\*waj-|\\*u̯aj|wajH|\\*waǰ' CHEUNG.txt | head; grep -n -i 'wazidan\\|wazīdan\\|parwāz\\|parwaz' CHEUNG.txt | head; ls incoming/ARY/ | head; grep -c . incoming/ARY/ARY_pages.txt",
 "description": "Locate Cheung *waj- entry and ARY files"
}
```


### [2026-10-16T05:17:39.120Z] TOOL RESULT

```
27903:waz- ‘to swim’, Sh. wöX-/wäxt, Rosh. wext, Sariq. wux-/wuxt, Yzgh. wöx-/weXt ‘to 
48151:waz-/wixt, 431 
48451:waz-/wixt, 431 
49860:waz-/wast-, 431 
50183:waz-, 431 
50191:waz-/wayd, 434 
27832:/parwaz-/ (caus.) ‘to fly off (LW) || (+ *ham-) ? BMP ’mws- /amwas-/ (pret. stem) 
27837:BMP plw’cyt /parwazéd/, SUBJ. 3pl. MMP “prwz’nd; Partic.: pres. MMP prwz’g || (+ *ham-) Partic.: 
28006:Partic.: perf. pass. BMP w’cyt/wazid/; Inf.: BMP w'cytn /wazidan/ 
35459:plw'c- /parwaz-/, 430 
Permissions Size User   Date Modified Name
.rw-r--r--  8.1M sfmqrb 14 Oct 22:19  ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
.rw-r--r--  586k sfmqrb 14 Oct 22:19  ARY_latin_index_pages.txt
.rw-r--r--  960k sfmqrb 14 Oct 22:19  ARY_pages.txt
15706
```


## [2026-10-16T05:17:42.162Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 27815,27840p CHEUNG.txt; grep -n -E 'VAZ|PARV|BAZ\\b|VAZAQ|VAZAGH|VAZIDAN' incoming/ARY/ARY_latin_index_pages.txt | head",
 "description": "Read Cheung *waz- and ARY index"
}
```


### [2026-10-16T05:17:42.651Z] TOOL RESULT

```
430 *yaz 


YAv. vazäite (Yt 5.11, Yt 8.6), YAv. frauuazäite (Yt 8.35), 3pl. med. YAv. vazante (Yt 10.125), IMPV. 
med. 2sg. YAv. upa.vazayg'ha (22.7); Aor. them. s-: INJ. 35р. ? YAv. uzuuaZat (Yt 13.100); Perf.: IND. 
3sg. med. YAv. vaoze (P 48), OPT. 3pl. med. YAv. vaoziram (Yt 19.69); Partic.: pres. YAv. vazant- (Yt 
10.20, Yt 13.26), med. YAv. vazomna-, YAv. frauuazamna- (Yt 13.26), perf. YAv. vauuazäna- (Yt 
10.124), perf. pass. ? Y Av. vasta- (Yt 12.8); Inf.: pres. YAv. vazaiöiläi ‘to flow’ (Yt 15.28, V 2.24), YAv. 
paiti.vazaidiiai (Yt 15.28); Pass.: pres. SUBJ. 3р1. YAv. vaziiante (Yt 14.43). © The interpretation of 
Y Av. "uuaZat as a sigmatic aor., corresponding to Skt. (RV) vaksat, is from Narten 1964: 140. This is 
declined by Kellens 1984: 368, fn. 1. || Final "^om of the YAv. ending vaozirom is the result of sandhi 
(Leumann 1952: 91), which must Бе Ріг. Further evidence is provided by Khot. mu (SGS: 203) and 
possibly Ossetic (Cheung 2002: 139). 

*MIDDLE PERSIAN: 1. MMP wy- ‘to move along’ || 2. BMP wc- /waz-/ ‘to move 
[intr.], blow [of wind]’ (LW) || (+ *para-) MMP prwz- ‘to fly’, BMP plw’c- 
/parwaz-/ (caus.) ‘to fly off (LW) || (+ *ham-) ? BMP ’mws- /amwas-/ (pret. stem) 
‘to collect, gather ?’ (< Pth. ?, cf. MacKenzie, Pahlavi: 8) = DMMPP: 350b, 281b 

1. Pres.: IND. 3pl. MMP wyynd, SUBJ. 3р1. MMP wy’nd; Partic.: perf. pass. II wy’d {in Pth. writing} || 
2. Pres.: IND. 3sg. BMP weyt /wazéd/; Partic.: perf. pass. BMP weyt /wazid/ || (+ *para-) Pres.: IND. 35р. 
BMP plw’cyt /parwazéd/, SUBJ. 3pl. MMP “prwz’nd; Partic.: pres. MMP prwz’g || (+ *ham-) Partic.: 
perf. pass. BMP ’mwst /amwast/ 

*PARTHIAN: wz- ‘to blow (of the wind); to move, go, fly’ || (+ *pati-) pdw’z 
3047:BALGS GOTHIC) Si BAZ AOSSETIC) ga)
3648:WACAN, (OLD ENGLISH) oS lS} VAZRA AVESTAN) glee!
3649:WECCAN VAZRAKA, :(OLD PERSIAN) oles p+,
3650:WAKE ENGLISH) SS} VAZARKA
4608:ie; WPARV (SWEDISH) (S45 yo PELESHTUK:(OLD PERSIAN) j\o«\, oj
4660:SANSKRIT) = Sle PAIRI-VAZAITI, PARA-VAZ
4678:Cog’ ee 4) VAZ- & VAZAITI ~¥ Cy, ila” CLSM ep 4 PARA | PAIRI-
4682:PREPELICA (SLOVENE) gy ge PARVANAK PAHLAVI) 5 3h |
4692:PARVARTAN s(PAHLAV]) 5 hy A(AVESTAN) bos!
4693:PARVARITAN, PARWARDAN PITUSH, -PITHWAy PITU-°
```


## [2026-10-16T05:17:48.652Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; python3 - <<'EOF'\nimport re\nt=open('ARY_latin_index_pages.txt',encoding='utf-8',errors='ignore').read()\nfor key in ['PAIRI-VAZAITI','VAZ- & VAZAITI','VAZAGH','VAZAQ','UXSHAN','UKSAN']:\n    i=t.find(key)\n    if i<0: print(key,'none'); continue\n    tags=[m for m in re.finditer(r'\\[pdf page (\\d+)\\]',t[:i])]\n    print(key,'pdf page',tags[-1].group(1) if tags else '?', t[max(0,i-300):i+300].replace('\\n',' | ')[:600]); print('---')\nEOF",
 "description": "Find ARY pages for parvâz, vazidan"
}
```


### [2026-10-16T05:17:49.071Z] TOOL RESULT

```
PAIRI-VAZAITI pdf page 162  glT | BUCK!” 1264-1266 FORSCON, FRAHEN, FRAGA | SKEAT: © (PREK) 757 FRAGEN, FRAGE (GERMAN) gulT | AMINDAROV: (ASK) 187 FRIGNAN (OLD ENGLISH) oS iS! | MALLORY & ADAMS: PERK SPORGE (DANISH) jails | rAd seb oly FRAGA SWEDISH) 528 y- | SPORRE NORWEGIAN) 533 | “ | PARWAZ HAFGHAND (54) lil AVESTAN) gly) | SANSKRIT) = Sle PAIRI-VAZAITI, PARA-VAZ | vVAHATI, VAHANA, VAHAYATI, VAHA- (KURDISH) 63 | ECHESTHIN (GREEK) gli y FIR, PIRIN, FIRIN, FIRKIRIN | VEHO, VEHERE LATIN) 33‘Y PERWAZ HBALUCHT) gx gh | ee | [pdf page 163] | 1 | | | | | ayy [| \PT \ | WEGAN (OLD ENGLISH) oS lS wees GOTHIC) 5 | UDHI ALBANI
---
VAZ- & VAZAITI pdf page 163  | | | ayy [| \PT \ | WEGAN (OLD ENGLISH) oS lS wees GOTHIC) 5 | UDHI ALBANIAN) git OLD SCANDINAVIAN) 45 Soh) | ms VEGA | ee FT aka HOLD HIGH GERMAN) oS gat | POKORNY. —~—«ald, 1N18119 VEGAN | ray gay BEWEGEN (GERMAN) galt | ieetloah | sgboay)) PERI: \ PER =) scant od Ce oat 9 in Sets 99 SI Cora cal tal dla | Cog’ ee 4) VAZ- & VAZAITI ~¥ Cy, ila” CLSM ep 4 PARA | PAIRI- | . 02S phe jin 1 Seale Lj 2 Sy al | 2S J 6a SV Ob5 29 3a cal | Deke Hgta5 GUDL; 2259 Cal | PREPELICA (SLOVENE) gy ge PARVANAK PAHLAVI) 5 3h | | “TPETELISHKE (LITHUANIAN) is) FEPULE, PERWANE :(KURDISH) 5,5 | 7 PATANG AFGHANI) (
---
VAZAGH none
VAZAQ none
UXSHAN none
UKSAN none
```


## [2026-10-16T05:17:55.043Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='ignore').read().split('\\f')\nimport re\nfor i in range(254,262):\n    p=t[i]\n    for k in ['uegh','u̯eĝh','vazaiti','uksan','ukṣ','umeo','ūmeo','vehō','veho']:\n        j=p.find(k)\n        if j>=0: print(i+1,k,'|',p[:40].replace('\\n',' '),'|',p[max(0,j-100):j+200].replace('\\n',' ')); \nEOF",
 "description": "Check Walde-Pokorny Bd I pp. 248-249"
}
```


### [2026-10-16T05:17:55.563Z] TOOL RESULT

```
255 uegh |                                          | ssig“. sabrexus „sehrag aufsteigend“ hierherzustellen, wenn auch die Zugehorigkeit zu lat. reho (s. uegh -) nach Thurneysen GGA. 1907, 806 moglich ist. Ygl. Yf. LEWb. 2 89 f.                          1     ueqti- ..Sache, Ding”.    Got. waihts f. ,.Saehe“. aisl. rittr, veetv, ritr f. ,.lebendes Wese
258 uegh | pi.    mcymr. ychen. ncymr. y chain      |  kaum als die „von den Feuchtigkeit aussondernden Driisen nasse" anzureilien. sondern Schallwort.   uegh- „bewegen, zielien, fahren u. dgl.“: eine Sehwundstufe                                                 idjh-    nur im     Ar. und wohl auch im Alb.        Ai.   v uhati             „fiihrt, heim
258 vazaiti | pi.    mcymr. ychen. ncymr. y chain      | heiratet" (Ptc. udha-), av.                                            fahrt,    zieht,     fiihrt  vazaiti          ,,   fiihrt,    zieht,   worin It statt -zd- nach Partizi-                                            fliegt“   (Ptc. vrnta-, pien von nicht auf Aspirata auslautenden Wzln.), ai. vcfl
259 uegh | 250                                      | 250                                                               uegh-      Lat. who,              -ere,  vvxi (: ai. uvulcsat, abg. tvjsa Aorist), vedum „fahren, fiihren, tragen,             bringen“ (dazu wo hi auch con-, de-. sub-vexsus s. Yf. LEWb. 2 189f.),
```


## [2026-10-16T05:18:00.115Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==178' SYN.txt | grep -n -i -E 'uk|uxs|ox|bull|wet|sprinkl|153' | head -20 | cut -c1-300",
 "description": "Check Buck SYN p.153 ox discussion"
}
```


### [2026-10-16T05:18:00.586Z] TOOL RESULT

```
22:CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
```


## [2026-10-16T05:18:03.219Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'uksan|ukşan|ukṣan|uxšan|uxsan|auhsa' SYN.txt | head | cut -c1-400",
 "description": "Grep Buck for ox words"
}
```


### [2026-10-16T05:18:03.526Z] TOOL RESULT

```
4111:~- ‘pull’, etc., disputed but probable roe 5 21). Walde-P. 2.609. Feist 454. cs Goth. auhsus, auhsa, ON oxi (uxt), OE ona, etc., the general Gme. word for ‘ox’, W. yoh ‘ox’, Br. oc’hen ‘oxen ; me Ose ‘stag’, Skt. wksan-, Av. uasan- bull, prob. : Skt. uks-‘sprinkle, emit Beat sole sypos ‘moist’, etc. Cf. Skt. uraarr. male, bull, stallion’, Lat. verrés ‘boar’ : Skt. vys- ‘rain’, ete. Walde-P. 1
4138:4. Skt. ukgan-, Av. uxdan-: Goth. auhsa ‘ox’, etc. (above, p. 153).
4997:ate a :W. ych, Goth. auhsa ‘ox’ : alde-P, 1.248 £, Peden:
```


## [2026-10-16T05:18:08.341Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^•? *j\\. *u[xz]san|uxian-|uxsan-  m' BRT.txt | head -5 | cut -c1-300; grep -n -E \"uxsan|uxSan|uxian\" BRT.txt | head -5 | cut -c1-250",
 "description": "Grep Bartholomae for uxšan"
}
```


### [2026-10-16T05:18:08.800Z] TOOL RESULT

```
5986:kada  mazda  yöi  uxsand  "snam  . .  /rärmtg
7759:•  g.  «razuxSan-  Adj.  'wahr  gesprochenes (Wort)  habend'  sva,  'sein  Wort  wahr  ge- sprochen machend,  es  erfüllend,  haltend': katuntl  (sd.)  ■  .  yi  U  akmai  ■'oil  (NS.)  IUI däiie  ".  .  dem  Mann,  der  es  (das  Ver- sprocJien
9588:Komp.:  »^kiriia-Aruxsan- ,  eig.  'des  Stiere  Stets  mit  Gen.  part.",  in  auffällig  freier mager  sind'.  syntaktischer  Verwendung'';  a)  als  Subj.:
12415:•  j.  daenav-  f.  'femina',  von  (vierftissigen) Tieren  (im  Gegensatz  zu  arsan-,  uxsan- und  varsnqy-),  in  Verbindung  mit  dem Tiernamen":   ka'iwa   'nu  (IS.)   ,  ,  gava
12779:—  tanam  yaoedai^lta  pascaSa  'im  S.bao- 'itayalta  \.g.-^\i.;  —  lanüm  . .  yahsil  'im ..  avaxanqa  lOia  ..V.6.  4$;  —  '  a*ura*- masda  yai^ä  avainJ'  imäm  bumim  .  . passvel^dim  mann  fräbarc^  D.  Ö'.  4;  — aOaiia  . .  uxian
```


## [2026-10-16T05:18:39.319Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; mkdir -p data/verification/sources/refs/ocr/BOOK; ls data/verification/sources/refs/ocr/BOOK/531.png 2>/dev/null || pdftoppm -f 531 -l 531 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf data/verification/sources/refs/ocr/BOOK/531; ls -la data/verification/sources/refs/ocr/BOOK/531.png; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"ox,  n.\")) {print NR-1; exit}}' data/verification/sources/refs/KLN_1966.txt",
 "description": "Render book page PNG for audit"
}
```


### [2026-10-16T05:18:40.918Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   78k sfmqrb 16 Oct 01:18  data/verification/sources/refs/ocr/BOOK/531.png
112
```


## [2026-10-16T05:21:28.775Z] TOOL CALL #50: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-531.py <<'PYEOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nPOK_WEGH={\"ref\":\"POK:1119\",\"status\":\"supports\",\"note\":\"POK_full.txt 'Root / lemma: uegh- ... Meaning: to move, carry, drive ... Page(s): 1118-1120': 'Avestan vazaiti leads, zieht, flies (participle vašta-)', 'Avestan vazya- n. load, Tracht', 'Avestan vaštar- draft animal (= Latin vector)', 'say-uzdri- ... (*uzdri- to *uzdar-)', 'Avestan vaza- fahrend, fliegend', 'Avestan vazišta-'.\"}\nWLD_WEGH={\"src\":\"WLD\",\"where\":\"Bd. I p. 249 (WLD_Bd1_pages.txt leaf 258)\",\"stance\":\"supports\",\"note\":\"'uegh- „bewegen, ziehen, fahren u. dgl.“ ... av. vazaiti „fährt, zieht, fliegt“ (Ptc. vašta-)'; p. 250 'Lat. veho, -ere, vexi, vectum ... (dazu wohl auch con-, de-, sub-vexus)'.\"}\nAHD_WEGH={\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt line 1132, s.v. wegh-\",\"stance\":\"supports\",\"note\":\"'wegh-. To go, transport in a vehicle. 1. Germanic *wegan in Old English wegan ...: WEIGH ... 3. *wegh-ti- ... WEIGHT. 4. Germanic *wegaz, course of travel, way ...: WAY; ALWAYS, (AWAY). 5. ... *wagnaz ... Middle Dutch wagen: WAGON ... 8. Latin vehere (past participle vectus): VECTOR, VEHICLE; ... CONVECTION ... 11. Probably ... *wegh-so- in Latin convexus ...: CONVEX. [Pok. wegh- 1118.]'\"}\nIEC_WEGH={\"src\":\"IEC\",\"where\":\"IEC.txt line 19826, s.v. uegh-\",\"stance\":\"supports\",\"note\":\"'uegh- carry, convey, transport ... WP I, 249 ... Av. vazāmi lead, conduct, draw ... Lat. veho ... Go. ga-wigan move; OHG wegan ... OE wegan bring, bear, weigh'.\"}\nPOK_WET={\"ref\":\"POK:1118\",\"status\":\"supports\",\"note\":\"POK_full.txt 'Root / lemma: uegʷ- : ugʷ-, uks- ; Meaning: wet; to irrigate; ox (?) ... Latin ūmeo, -ēre humid, wet sein, ūmor dampness ... Indo Germanic uksen- bull, Tiermännchen in: Old Indie ukṣan-, Avestan uxšan- bull ... Gothic auhsus ... Old English oxa ... Page(s): 1118'. Pokorny himself puts a query on the 'ox' meaning.\"}\nAHD_WET={\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt line 1132, s.v. wegw-\",\"stance\":\"partial\",\"note\":\"'wegʷ-. Wet ... 2. *ugʷ-sm- in: a. Latin (h)ūmēre, to be wet: HUMECTANT, HUMID; b. Latin (h)ūmor, fluid: HUMOR ... 4. Regarded by some as an extended form of this root (with the meaning \\\"the impregnator\\\"), but probably a distinct Indo-European word, is *ukʷs-en-, bull, ox, in Germanic *uhsōn- in: a. Old English oxa, ox: OX'.\"}\nWLD_WET={\"src\":\"WLD\",\"where\":\"Bd. I pp. 248-249 (WLD_Bd1_pages.txt leaf 258)\",\"stance\":\"supports\",\"note\":\"Leaf 258 opens with the end of the ueg-/uks-en entry ('mcymr. ychen, ncymr. ychain' = W. 'oxen'), which Walde-Pokorny treat under 'feucht, befeuchten' exactly as POK 1118 (whose entry cites 'WP. I 248 f.').\"}\nSYN_OX={\"src\":\"SYN\",\"where\":\"§3.2x OX, p. 153 (SYN.txt line 4111)\",\"stance\":\"partial\",\"note\":\"'Goth. auhsus, auhsa, ON oxi, OE oxa ... W. ych ... Skt. ukṣan-, Av. uxšan- bull, prob. : Skt. ukṣ- sprinkle, emit seed, Grk. ὑγρός moist' — Buck calls the 'sprinkler' link only 'prob.'\"}\n\nentries=[]\n# ---------------- entry 0\ne0={\"entry\":0,\"root\":\"Wegh, Waq, Wag\",\"verdict\":\"confirmed\",\n\"modern_form\":\"PIE *weǵʰ- 'to convey, transport (in a vehicle), ride' (LIV *u̯eǵʰ-; Pokorny 1118-1120 uegh-; AHD wegh-)\",\n\"note\":\"The root is one of the best-established PIE verbs: Skt. vahati, Av. vazaiti, Lat. vehō, Gk. (Pamph.) wekhetō, Goth. ga-wigan, OE wegan, OCS vezǫ, Lith. vežù. Nourai's gloss 'to go, carry' matches Watkins ('to go, transport in a vehicle'); the alternants 'Waq, Wag' are Nourai's own shorthand for the Iranian/Germanic outcomes, not separate PIE roots. The Latin, Germanic and English branches are textbook; the weak points are on the Iranian side: (a) Nourai's Avestan glosses 'vaza 1: a bird, hawk' and 'vašta 2: curved' are not supported by Bartholomae or Cheung (vaza- is an adjective 'driving, flying'; vašta- is only the past participle 'conveyed'); (b) NP bâz 'hawk' is traditionally connected with vaz- 'fly' (*vāza- 'flier') but Wiktionary instead compares Skt. bhāsa- 'bird of prey', so that link is uncertain; (c) English wave (n.) is only partly from this root (ME wawe < OE wǣg), its modern shape coming from the verb wave < OE wafian (PIE *webʰ-).\",\n\"note_fa\":\"ریشهٔ هندواروپایی آغازین *weǵʰ- «بردن، با گردونه رفتن، کشیدن» از استوارترین ریشه‌هاست: سنسکریت vahati، اوستایی vazaiti، لاتین vehō، گوتی ga-wigan، انگلیسی کهن wegan و اسلاوی کهن vezǫ همه از آن‌اند (پوکورنی ۱۱۱۸–۱۱۲۰، واتکینز). معنای «رفتن، بردن» که نورایی داده درست است و صورت‌های Waq و Wag تنها نشانهٔ بازتاب‌های ایرانی و ژرمنی‌اند. شاخه‌های لاتینی، ژرمنی و انگلیسی بی‌گمان درست‌اند؛ اما در شاخهٔ ایرانی معنای «باز (پرندهٔ شکاری)» برای اوستایی vaza- و «خمیده» برای vašta- در بارتولومه و چونگ نیامده، و پیوند «باز» با vaz- «پریدن» تنها یکی از دو نظر است. ادعای نورایی دربارهٔ خود ریشه درست است.\",\n\"sources\":[W+\"Reconstruction:Proto-Indo-European/weǵʰ-\",W+\"Reconstruction:Proto-Indo-European/wéǵʰeti\"],\n\"ref_check\":[POK_WEGH],\n\"consulted\":[WLD_WEGH,AHD_WEGH,IEC_WEGH],\n\"nodes\":[\n{\"id\":1,\"lang\":\"Avestan\",\"words\":\"vaz; vaza 1; pairi-vaza; vaza 2, vâzišta; vazya\",\"verdict\":\"plausible\",\n\"derivation\":\"Av. vaz- (pres. vazaiti) < Proto-Iranian *u̯az- < PIE *weǵʰ- (palatal *ǵʰ > Iranian z) means 'drive, convey', and intransitively 'glide, fly' (Bartholomae col. 1386-88: 'schweben, fliegen'), so 'vaz: fly' is right; vazya- n. 'load, burden' (col. 1391, = Skt. vahya-) is right; vāzišta- is a superlative 'best-conveying' (Pokorny: 'der am besten vorwärtsbringt', an epithet of a fire), loosely glossed 'travel'. vaza- is attested only as an adjective 'driving, carrying off; flying' (Bartholomae 1389, Pokorny 'fahrend, fliegend'): the sense 'a bird, hawk' (vaza 1) is not attested and is Nourai's back-projection from NP bâz. pairi-vaza is not an attested Avestan word but a reconstruction (*pari-/*para-vaz-) behind MP parwāz (Horn §305: 'aw. pairi (oder para) + vaz-, herum- bzw. wegfliegen'; Cheung: MMP prwz- 'to fly').\",\n\"derivation_fa\":\"ریشهٔ اوستایی vaz- (vazaiti) از ایرانی باستان *u̯az- و هندواروپایی *weǵʰ- است (ǵʰ کامی در ایرانی به z بدل شده) و به معنای «راندن، بردن» و در کاربرد ناگذرا «لغزیدن، پرواز کردن» است؛ پس «vaz: پریدن» و vazya- «بار» و vāzišta- «بهترین برنده» درست‌اند. اما vaza- در اوستا تنها صفت «رونده، پرنده (پروازکننده)» است و معنای «باز، پرندهٔ شکاری» در بارتولومه نیامده؛ این معنا را نورایی از «باز» فارسی به عقب برده است. pairi-vaza نیز واژهٔ گواهی‌شده نیست و بازسازیِ ریشهٔ «پرواز» است (هرن ۳۰۵). ادعای نورایی با احتیاط پذیرفتنی است.\",\n\"sources\":[W+\"Reconstruction:Proto-Indo-European/weǵʰ-\"],\n\"ref_check\":[POK_WEGH],\n\"consulted\":[\n {\"src\":\"BRT\",\"where\":\"cols. 1386-1389, 1391 (BRT.txt lines ~23170-23270)\",\"stance\":\"partial\",\"note\":\"'vaz- V. fahren ... 2) intrans. von jeder Art gleitender Bewegung wie schweben, fliegen'; 'vazya- n. Last, Tracht'; 'vaza- Adj. 1) fahrend, lenkend 2) wegführend, raubend' — no noun 'bird/hawk'; mp. vazītan, np. vazīdan 'wehen', afγ. vuzal 'fliegen'.\"},\n {\"src\":\"CHEUNG\",\"where\":\"p. 430 s.v. *u̯az- (CHEUNG.txt lines 27815-27840)\",\"stance\":\"partial\",\"note\":\"YAv. vazāite, frauuazāite ... perf. pass. ? YAv. vašta- (Yt 12.8) ... MMP prwz- 'to fly', BMP plwʾc- /parwaz-/ 'to fly off' — confirms vaz-/parwāz, has no *pairi-vaza- noun.\"},\n WLD_WEGH,\n {\"src\":\"KNT\",\"where\":\"lexicon (grep vaz-)\",\"stance\":\"silent\",\"note\":\"Old Persian has vazarka- 'great' (from a different root *u̯eǵ-), no vaz- 'drive'; not relevant to Avestan forms.\"}]},\n{\"id\":2,\"lang\":\"Persian\",\"words\":\"bâz; parvâz; vazîdan\",\"verdict\":\"plausible\",\n\"derivation\":\"vazīdan 'to blow (of wind)' < MP wazīdan (wc-ytn') 'move, blow' < Av./Proto-Ir. *u̯az- 'drive, glide' — confirmed (PHD, NYB, Horn §1083, Mo'in BQT 2279, Wiktionary). parvâz 'flight' < MP parwāz (MMP prwz- 'to fly', BMP plwʾc-) < *pari-/*para-vāza-, with the Av. preverb pari 'around' or para 'away' + vaz- — confirmed (Horn §305, Cheung 430, Aryanpur). bâz 'hawk, falcon' < MP bāz (bʾc), and the variants bâše/vâše 'sparrowhawk' (Mo'in: 'a bird of prey smaller than the bâz') show the b-/v- alternation typical of old initial *w- (cf. vād/bād): Nourai derives it from *vāza- 'flier' < vaz-; this is phonetically regular but is not the only view — Wiktionary (after Rastorgueva-Edelman) instead relates bāz to Skt. bhāsa- 'bird of prey', and Horn and Bartholomae give no Iranian etymology. Arabic bāz, Armenian bazē, Georgian bazi are loans from the Iranian word. Ferdowsi's verse pairs bāz with vâše 'sparrowhawk'.\",\n\"derivation_fa\":\"«وزیدن» از فارسی میانهٔ wazīdan «جنبیدن، وزیدن» و از ریشهٔ ایرانی باستان *u̯az- است؛ «پرواز» از فارسی میانهٔ parwāz (فارسی میانهٔ مانوی prwz- «پریدن») و از پیشوند pari/para + vaz- ساخته شده است؛ این دو درست‌اند (هرن، مکنزی، نیبرگ، چونگ، معین در حاشیهٔ برهان). «باز» (پرندهٔ شکاری) از فارسی میانهٔ bāz است و «باشه/واشه» گونه‌های همان واژه‌اند که ابدال ب/و را نشان می‌دهند. نورایی آن را از *vāza- «پرنده، پروازکننده» می‌داند که از نظر آوایی درست است، ولی ویکی‌واژه آن را با سنسکریت bhāsa- «پرندهٔ شکاری» می‌سنجد و هرن ریشه‌ای برایش نمی‌دهد؛ پس این بخش با احتیاط پذیرفتنی است. «باز» عربی و ارمنی bazē از فارسی وام گرفته شده‌اند.\",\n\"sources\":[W+\"باز\",W+\"پرواز\",W+\"وزیدن\",\"https://vajehyab.com/moein/باشه\",\"https://vajehyab.com/moein/پرواز\"],\n\"ref_check\":[\n {\"ref\":\"BQT:2279\",\"status\":\"supports\",\"note\":\"ref_page.py BQT:2279 (vol 4 pdf p. 362), Mo'in's footnote to وزیدن: 'از: وز + یدن (پسوند مصدری) ... ریشهٔ هندی باستان vah (وزیدن) ... پهلوی vazītan، افغانی vuzal (پریدن) «هوبشمان ۱۰۸۳» ریشهٔ اوستایی vaz- (رفتن) «بارتولمه ۱۳۸۶»'.\"},\n {\"ref\":\"BQT:217\",\"status\":\"partial\",\"note\":\"BQT_v1_pages.txt leaf 437: headword باز 'پرنده‌ایست مشهور و معروف که سلاطین و اکابر شکار فرمایند' (footnote 7); the footnote's continuation on p. 218 (leaf 438) quotes the Shahnameh 'گاه برجستن چو باشه گاه برگشتن چو باز' but its etymological part is not legible in the OCR — no confirmation of the vaz- etymology.\"},\n {\"ref\":\"BQT:391\",\"status\":\"not_found\",\"note\":\"BQT_v1_pages.txt leaves 600-625 searched for پرواز; the OCR shows the word only inside other entries (leaf 615), the headword and Mo'in's note for p. 391 are not legible; no scan for vol 1 via ref_page.py.\"},\n {\"ref\":\"MON:4949\",\"status\":\"partial\",\"note\":\"Printed page not mappable online; vajehyab Mo'in: 'باشه ... یکی از پرندگان شکاری کوچکتر از باز'; 'پرواز ... پرش، پریدن' — confirms meanings, no etymology online.\"}],\n\"consulted\":[\n {\"src\":\"PHD\",\"where\":\"PHD_mackenzie.txt line 5298; PHD.txt line 256\",\"stance\":\"supports\",\"note\":\"'wazīdan, waz- [wc-ytn' | P wz-, N ~] move, blow (of wind)'; '¹wāzīdan, wāz- [wʾc-ytn'] move, carry away; fly. ~išn: flight'; 'bāz [bʾc | N ~] hawk, falcon' (no etymology).\"},\n {\"src\":\"NYB\",\"where\":\"vol 2 glossary lines 4062-4065\",\"stance\":\"supports\",\"note\":\"'vazītan [wcytn'] to travel, to ride ... Av. (1386) vaz-; MPrth. pres. wz- to blow of the wind, to move, to go'; 'vāzītan ... Cf MPrth ... prwʾz- to cause to fly'.\"},\n {\"src\":\"HRN\",\"where\":\"§305 p. 67-68 (HRN.txt line 2938); §1083 p. 242\",\"stance\":\"supports\",\"note\":\"'305. perwāz Flug. aw. pairi (oder para) — √vaz-, herum- bezw. weg-fliegen, vergl. vazaiti er fliegt'; '1083. vezīden wehen ... ai. √vah- vahati wehen; phlv. vazītan wehen'. Horn has no entry deriving bāz 'falcon'.\"},\n {\"src\":\"HUB\",\"where\":\"HUB.txt line 5801\",\"stance\":\"supports\",\"note\":\"'vazīdan wehen, skr. vah dahinfahren, wehen'.\"},\n {\"src\":\"CHEUNG\",\"where\":\"p. 430 *u̯az-\",\"stance\":\"supports\",\"note\":\"'BMP wc- /waz-/ to move, blow [of wind] ... (+ *para-) MMP prwz- to fly, BMP plwʾc- /parwaz-/ (caus.) to fly off'.\"},\n {\"src\":\"ARY\",\"where\":\"pdf pp. 162-163 (printed 163-164), entry پرواز\",\"stance\":\"supports\",\"note\":\"ARY_latin_index_pages.txt: 'PARWAZ ... AVESTAN PAIRI-VAZAITI, PARA-VAZ ... SANSKRIT VAHATI ... LATIN VEHO, VEHERE ... OLD ENGLISH WEGAN ... POKORNY 1118-1119'.\"}]},\n{\"id\":3,\"lang\":\"Avestan\",\"words\":\"vašta 2; vaštar; uždar, uždri\",\"verdict\":\"plausible\",\n\"derivation\":\"vaštar- m. 'draught animal' (Bartholomae: 'Zugtier', Yt 5.13) = Skt. voḍhar-, Lat. vector, < *weǵʰ-tor- — confirmed. uždar/uždri: Pokorny posits *uzdar-/*uzdri- (zero grade *uǵʰ-dʰr-) only from the personal name sāy-uždri- 'whose female draught animals are dappled' (Bartholomae: 'säy-uzdri- m. EN eines Gläubigen'); 'carrier' is therefore a reconstructed meaning, not an attested word. vašta- is the perfect passive participle of vaz- 'conveyed' (Pokorny, Cheung: '? YAv. vašta- (Yt 12.8)'), with -št- for expected *-žd- by analogy; no Avestan source gives it the meaning 'curved' — that gloss seems carried over from Latin convexus and is unsupported.\",\n\"derivation_fa\":\"vaštar- «جانور بارکش، چارپای کشنده» (بارتولومه: Zugtier) هم‌ریشه با لاتین vector و سنسکریت voḍhar- است و درست است. uždar/uždri واژهٔ مستقلی در اوستا نیست و پوکورنی آن را تنها از نام خاص sāy-uždri- («آن‌که چارپایان بارکشش خال‌دارند») بازسازی کرده است. vašta- تنها صفت مفعولی گذشتهٔ vaz- به معنای «برده‌شده» است و معنای «خمیده» که نورایی داده در هیچ منبعی نیامده و گویا از لاتین convexus گرفته شده است. پس این گره با احتیاط پذیرفتنی است و معنای «خمیده» نادرست است.\",\n\"sources\":[W+\"Reconstruction:Proto-Indo-European/weǵʰ-\"],\n\"ref_check\":[POK_WEGH],\n\"consulted\":[\n {\"src\":\"BRT\",\"where\":\"col. ~1391 (BRT.txt lines 23268-23271); col. ~1556 (line 26200)\",\"stance\":\"partial\",\"note\":\"'vašta- Adj., PPfP.: s. vaz-'; 'vaštar- m. Zugtier ... Zum V. vaz-; ai. voḍhar-'; 'sāy-uzdri- m. EN. eines Gläubigen' — no 'curved' sense, uzdar only in the name.\"},\n {\"src\":\"CHEUNG\",\"where\":\"p. 430 *u̯az-\",\"stance\":\"partial\",\"note\":\"'perf. pass. ? YAv. vašta- (Yt 12.8)' — participle, meaning 'conveyed', uncertain.\"},\n WLD_WEGH]},\n{\"id\":4,\"lang\":\"Latin\",\"words\":\"vehere; vectus; con-vexus\",\"verdict\":\"confirmed\",\n\"derivation\":\"Latin vehō, vehere, vexī, vectum 'to carry, convey' continues PIE *wéǵʰeti (Proto-Italic *weɣō; *ǵʰ > Latin h between vowels), past participle vectus < *weǵʰ-to-. convexus 'vaulted, arched, sloping to a point' is con- 'together' + *vexus (< *weǵʰ-so-), 'drawn together (to a point)'; Watkins marks this 'probably', and Walde-Pokorny/Walde-Hofmann likewise include con-, de-, sub-vexus under vehō.\",\n\"derivation_fa\":\"لاتین vehō, vehere «بردن، حمل کردن» با صفت مفعولی vectus بازماندهٔ *wéǵʰeti هندواروپایی است (ǵʰ میان دو واکه در لاتین به h بدل شده). convexus «برآمده، خمیده به سوی یک نقطه» از con- «با هم» + *vexus (از *weǵʰ-so-) به معنای «به یک نقطه کشیده‌شده» است؛ واتکینز این را «به احتمال زیاد» می‌داند. ادعای نورایی درست است.\",\n\"sources\":[W+\"Reconstruction:Proto-Indo-European/wéǵʰeti\",W+\"convex\",W+\"vehicle\"],\n\"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985 s.v. wegh-: '8. Basic form *wegh- in Latin vehere (past participle vectus), to carry: VECTOR, VEHICLE ... 11. Probably suffixed form *wegh-so- in Latin convexus, \\\"carried or drawn together (to a point),\\\" convex'.\"}],\n\"consulted\":[{\"src\":\"POK\",\"where\":\"p. 1119\",\"stance\":\"supports\",\"note\":\"'Latin veho, -ere, vexi, vectum drive, guide, lead, bear, carry, bring (in addition probably also con-, de-, sub-vexsus)'.\"},\n WLD_WEGH,\n {\"src\":\"KLN\",\"where\":\"KLN_1966.txt line 9035 s.v. convection\",\"stance\":\"supports\",\"note\":\"'L. convectio ... fr. convectus, pp. of convehere, to carry together, fr. con- and vehere, to carry. See vehicle'.\"}]},\n{\"id\":5,\"lang\":\"English\",\"words\":\"vehicle; vector; convection; convex\",\"verdict\":\"confirmed\",\n\"derivation\":\"vehicle (17th c.) < French véhicule < Latin vehiculum 'carriage' (vehere + instrumental -iculum); vector (18th c., first in astronomy/medicine 'carrier') < Latin vector 'carrier, bearer' (vehere + -tor); convection (17th c., physics sense 19th c.) < Late Latin convectio 'a carrying together' < convehere; convex (16th c.) < Middle French convexe < Latin convexus 'arched'. All are learned borrowings from the Latin verb of node #4.\",\n\"derivation_fa\":\"vehicle از فرانسوی véhicule و لاتین vehiculum «گردونه»؛ vector از لاتین vector «برنده، حامل»؛ convection از لاتین convectio «باهم بردن» و convex از فرانسوی میانه convexe و لاتین convexus «برآمده». همه وام‌واژه‌های دانشی از فعل لاتین vehere هستند. ادعای نورایی درست است.\",\n\"sources\":[W+\"vehicle\",W+\"vector\",W+\"convex\"],\n\"ref_check\":[{\"ref\":\"(none)\",\"status\":\"not_checked\",\"note\":\"Node has no reference of its own; AHD wegh- (above) lists VECTOR, VEHICLE, CONVECTION, CONVEX.\"}],\n\"consulted\":[{\"src\":\"KLN\",\"where\":\"line 9035 s.v. convection\",\"stance\":\"supports\",\"note\":\"'L. convectio ... fr. convehere ... See vehicle'.\"},\n {\"src\":\"AHD\",\"where\":\"s.v. wegh- §8, §11\",\"stance\":\"supports\",\"note\":\"'VECTOR, VEHICLE; ADVECTION, CONVECTION ... CONVEX'.\"}]},\n{\"id\":6,\"lang\":\"Germanic\",\"words\":\"wegaz; wigan\",\"verdict\":\"confirmed\",\n\"derivation\":\"Proto-Germanic *wegaz 'way, course of travel' (Kroonen *wega-) is the o-stem noun from *weǵʰ- (Verner-free *ǵʰ > *g), giving OE weg, ON vegr, Goth. wigs. *weganą 'to move, carry, weigh' continues the thematic present *wéǵʰeti (OE wegan, OHG wegan, ON vega); Nourai's 'wigan' is the Gothic form (ga-wigan 'to move, shake', with Gothic i for e), glossed by the OE sense 'carry, weigh'.\",\n\"derivation_fa\":\"ژرمنی آغازین *wegaz «راه» و *weganą «جنباندن، بردن، وزن کردن» هر دو از *weǵʰ- هستند (انگلیسی کهن weg و wegan، گوتی wigs و ga-wigan). صورت wigan در نمودار همان صورت گوتی است. ادعای نورایی درست است.\",\n\"sources\":[W+\"Reconstruction:Proto-Germanic/wegaz\",W+\"Reconstruction:Proto-Germanic/weganą\"],\n\"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985 s.v. wegh-: '1. Germanic *wegan in Old English wegan, to carry, balance in a scale: WEIGH ... 4. Germanic *wegaz, course of travel, way'.\"}],\n\"consulted\":[{\"src\":\"POK\",\"where\":\"p. 1119\",\"stance\":\"supports\",\"note\":\"'Gothic gawigan move, shake ... Old English wegan bring, guide, lead ... Gothic wigs, Old Icelandic vegr, Old High German Old Saxon Old English weg way'.\"},\n IEC_WEGH, WLD_WEGH]},\n{\"id\":7,\"lang\":\"English\",\"words\":\"way; away; always; wagon; wave 2; Norway; weigh; weight\",\"verdict\":\"plausible\",\n\"derivation\":\"way < OE weg < *wegaz; away < OE on weg 'on (the) way'; always < ME alwey(e)s < OE ealne weg 'all the way'; wagon < Middle Dutch wagen < *wagnaz (doublet of native wain < OE wæġn); weigh < OE wegan 'carry, weigh' < *weganą; weight < OE wiht/gewiht < *wihtiz (*weǵʰ-ti-); Norway < OE Norþweg, calque of ON Norðvegr 'the north way' (vegr < *wegaz). wave (n.) is only partly from this root: ME wawe < OE wǣg 'billow' < *wēgaz (lengthened grade) merged with the noun from the verb wave < OE wafian (PIE *webʰ- 'move to and fro'), which gives the modern form — so 'wave 2' is a hybrid, while the other seven words are confirmed.\",\n\"derivation_fa\":\"way از انگلیسی کهن weg، away از on weg «در راه»، always از ealne weg «همهٔ راه»، wagon از هلندی میانه wagen، weigh از wegan و weight از wiht/gewiht، و Norway از Norþweg که ترجمهٔ نوردیک کهن Norðvegr «راه شمال» است؛ همه از *weǵʰ- هستند. اما wave (موج) دورگه است: wawe انگلیسی میانه از wǣg انگلیسی کهن (از همین ریشه) با فعل wave از wafian (از ریشهٔ دیگر *webʰ-) درآمیخته و صورت امروزی از دومی است. پس این گره با احتیاط پذیرفتنی است و جز wave بقیه درست‌اند.\",\n\"sources\":[W+\"wave\",W+\"Norway\",W+\"always\",W+\"wagon\",W+\"weigh\"],\n\"ref_check\":[{\"ref\":\"(none)\",\"status\":\"not_checked\",\"note\":\"Node has no reference of its own; AHD wegh- lists WAY, ALWAYS, (AWAY), WAGON, WEIGH, WEIGHT but not WAVE or NORWAY.\"}],\n\"consulted\":[AHD_WEGH,\n {\"src\":\"SKT\",\"where\":\"SKT.txt leaf 581-584 s.v. Wave (1), Way, Weigh, wagon\",\"stance\":\"partial\",\"note\":\"'Way. (E.) ... Goth. wigs ... Skt. vahá, from vah, to carry. Der. al-way, al-ways'; 'Wave (1), to fluctuate. M.E. wauen. A.S. wafian ... Der. wave, sb.' — Skeat derives the noun wave from wafian, not from wegh-; 'wagon ... Borrowed from Du. wagen ... cognate with wain'.\"},\n {\"src\":\"KLN\",\"where\":\"KLN_1966.txt line 4144 s.v. away\",\"stance\":\"supports\",\"note\":\"'away, adv. — ME. away, aweie, fr. OE. on weg, lit. on the way'.\"}]}\n]}\nentries.append(e0)\n\n# ---------------- entry 1\nIEC_LIZ={\"ref\":\"IEC:1499\",\"status\":\"supports\",\"note\":\"IEC.txt line 19824: 'uĕĝo- (1), element of the following (?) Av. cf. vazaγa, f. lizard; Per. vazaq, s. frog; Li. vėžys, m. crab, crayfish; vėžlys, m. tortoise; Latv. vēzis crab.' — Mann's own entry, with his query.\"}\ne1={\"entry\":1,\"root\":\"Wěğo\",\"verdict\":\"plausible\",\n\"modern_form\":\"Mann's *u̯ĕǵo- (queried); modern handbooks give no PIE etymology for Av. vazaγā- / NP vazaγ\",\"note\":\"The 'root' is taken from Mann (IEC 1499), who himself marks it with '(?)' and links Av. vazaγā-, NP vazaγ with Lith. vėžys 'crayfish', vėžlys 'tortoise', Latv. vēzis 'crab'. It is not in Pokorny, LIV or Watkins; Wiktionary only says the NP word is 'akin to Avestan vazaγā'. The Iranian chain Av. vazaγā- → MP wazaγ → NP vazaγ is secure; the IE root is speculative, as Nourai's own '?' signals.\",\n\"note_fa\":\"این ریشه را تنها مان (IEC ۱۴۹۹) با علامت پرسش آورده و اوستایی vazaγā- و فارسی «وزغ» را با لیتوانیایی vėžys «خرچنگ» سنجیده است؛ پوکورنی و واتکینز چنین ریشه‌ای ندارند. زنجیرهٔ ایرانی (اوستایی vazaγā- ← پهلوی wazaγ ← فارسی «وزغ») استوار است، ولی ریشهٔ هندواروپایی آن گمانی است، چنان‌که خود نورایی هم علامت پرسش گذاشته است. با احتیاط پذیرفتنی است.\",\n\"sources\":[W+\"وزغ\"],\n\"ref_check\":[IEC_LIZ],\n\"consulted\":[{\"src\":\"POK\",\"where\":\"POK_full.txt grep 'vazaγ|vazag|Frosch'\",\"stance\":\"silent\",\"note\":\"No Pokorny entry contains Av. vazaγā-; the Baltic 'crab' words are under other roots.\"},\n {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt\",\"stance\":\"silent\",\"note\":\"No root for 'lizard/frog' of this shape.\"},\n {\"src\":\"WLD\",\"where\":\"Band 3 index / Bd. I\",\"stance\":\"silent\",\"note\":\"Not found (grep vazaγ).\"}],\n\"nodes\":[\n{\"id\":1,\"lang\":\"Avestan\",\"words\":\"vazaghâ\",\"verdict\":\"confirmed\",\n\"derivation\":\"Av. vazaγā- (m./f.) is attested in the Vidēvdād (V 5.36; V 14.5) as an ahrimanic creature, 'frog; female frog', of which land- and water-varieties are distinguished (Bartholomae col. 1389: 'Frosch; Froschweibchen ... Land- und Wasserfrösche'); Mann's 'lizard' is a looser gloss. It continues into MP wazaγ and NP vazaγ (Bartholomae: 'mp. (Pü.), np. vazaγ').\",\n\"derivation_fa\":\"اوستایی vazaγā- در وندیداد (۵.۳۶؛ ۱۴.۵) به معنای «قورباغه» آمده و از آفریده‌های اهریمنی شمرده شده و دو گونهٔ خشکی و آبی آن جدا شده‌اند (بارتولومه ستون ۱۳۸۹). معنای «مارمولک» را مان افزوده است. این واژه به پهلوی wazaγ و فارسی «وزغ» رسیده است. ادعای نورایی درست است.\",\n\"sources\":[W+\"وزغ\"],\n\"ref_check\":[IEC_LIZ],\n\"consulted\":[{\"src\":\"BRT\",\"where\":\"col. 1389 (BRT.txt ~line 23190)\",\"stance\":\"supports\",\"note\":\"'vazaγ- m., vazaγā- f. Frosch; Froschweibchen; ein ahrimanisches Tier, von dem zwei Arten geschieden werden, Land- und Wasserfrösche ... mp. (Pü.), np. vazaγ'.\"},\n {\"src\":\"HRN\",\"where\":\"§1082 p. 242\",\"stance\":\"supports\",\"note\":\"'aw. vazaγā Frosch; phlv. vazaγ, vazag'.\"}]},\n{\"id\":2,\"lang\":\"Persian\",\"words\":\"vazağ; vazağeh\",\"verdict\":\"confirmed\",\n\"derivation\":\"NP vazaγ وزغ 'frog' < MP wazaγ (wzγ, PHD 'frog') < Av. vazaγā-; the variants vazaq وزق and vazak وزک (Borhan) show the usual γ/q/k spelling alternation (Mo'in, after the Farhang-e Nezam, notes the -q spelling is the Iraqi dialect form). vazaγe وزغه 'small lizard, gecko' is the Arabic form wazagha (Horn: 'arab. LW. vazaγat Eidechsenart'), i.e. the Persian word borrowed into Arabic with a shift to 'gecko' and re-borrowed — a Persian → Arabic → Persian round trip.\",\n\"derivation_fa\":\"«وزغ» (قورباغه) از پهلوی wazaγ و اوستایی vazaγā- است؛ «وزق» و «وزک» گونه‌های نوشتاری همان واژه‌اند (به گفتهٔ معین، صورت با ق لهجهٔ عراقیان است). «وزغه» (مارمولک کوچک، چلپاسه) صورت عربیِ وَزَغة است که خود از فارسی وام گرفته شده و معنایش به «چلپاسه» گشته و دوباره به فارسی بازگشته است (هرن ۱۰۸۲). ادعای نورایی درست است.\",\n\"sources\":[W+\"وزغ\",\"https://vajehyab.com/moein/وزغ\"],\n\"ref_check\":[\n {\"ref\":\"BQT:2278\",\"status\":\"supports\",\"note\":\"ref_page.py BQT:2278 (vol 4 pdf p. 361), Mo'in's footnote to وزغ: 'بفتح اول و دوم ... معرب آن وزغه (نوعی چلپاسه) ... اوستا vazaγā (قورباغه) «بارتولمه ۱۳۸۹» پهلوی vazaγ، کردی (قورباغه) ... سمنانی ... گیلکی ...'.\"},\n {\"ref\":\"HRN:242\",\"status\":\"supports\",\"note\":\"HRN.txt line 9367, p. 242: '1082. vezeγ Frosch, arab. LW. vazaγat Eidechsenart. aw. vazaγā Frosch; phlv. vazaγ, vazag. kurd. LW. vizāq Frosch'.\"},\n IEC_LIZ,\n {\"ref\":\"MON:5018\",\"status\":\"partial\",\"note\":\"Page not mappable online; vajehyab Mo'in: 'وزغ (وَ زَ) [په.] (اِ.) = وزق: قورباغه' — confirms Pahlavi origin and meaning.\"}],\n\"consulted\":[{\"src\":\"PHD\",\"where\":\"PHD_mackenzie.txt line 5294\",\"stance\":\"supports\",\"note\":\"'wazaγ [wzγ | N ~, bazaγ] frog'.\"},\n {\"src\":\"HUB\",\"where\":\"HUB.txt line 5801\",\"stance\":\"supports\",\"note\":\"'vazaγ Frosch = zd. vazaγa-'.\"},\n {\"src\":\"BQT\",\"where\":\"p. 2279 fn. 1 (vol 4 pdf 362)\",\"stance\":\"supports\",\"note\":\"'مؤلف سراج نوشته: «وزغ، بفتحتین غوک» وبقاف که شهرت گرفته لهجهٔ عراقیان است' — on the وزق variant.\"}]}\n]}\nentries.append(e1)\n\n# ---------------- entry 2\ne2={\"entry\":2,\"root\":\"Wegw, Ugw, Uks / Uksen\",\"verdict\":\"plausible\",\n\"modern_form\":\"PIE *wegʷ- 'wet' (Pokorny 1118 uegʷ-; Kroonen *wakwa-) and the separate noun *uksḗn 'bull, ox' (origin uncertain)\",\n\"note\":\"Two different things are combined, following Pokorny 1118 ('uegʷ-: ugʷ-, uks- wet; to irrigate; ox (?)') and Klein ('*uksen- male animal, lit. besprinkler'). *wegʷ- 'wet' is accepted (Gk. hugrós, ON vǫkr, E. wake 'track in water'), but the Latin ūmeō branch is now doubted (de Vaan and Weiss derive it from *uh₁mo-). *uksḗn 'bull' itself is certain (Skt. ukṣán-, Av. uxšan-, Goth. auhsa, W. ych, Toch. B okso), but its link to 'wet / sprinkle, inseminate' is only one hypothesis: Watkins calls it 'probably a distinct Indo-European word', and Wiktionary also lists *h₂weks- 'grow strong' and a Kartvelian loan. So the root box is a defensible traditional view, not a consensus.\",\n\"note_fa\":\"نورایی به پیروی از پوکورنی (۱۱۱۸) و کلاین دو چیز را در یک ریشه گرد آورده است: *wegʷ- «تر، خیس» و *uksḗn «نرگاو». ریشهٔ «تر» پذیرفته است (یونانی hugrós، نوردیک کهن vǫkr)، و واژهٔ *uksḗn (سنسکریت ukṣán-، اوستایی uxšan-، گوتی auhsa) نیز قطعی است، ولی پیوند «گاو نر» با «تر کردن، بارور کردن» تنها یک فرضیه است: واتکینز آن را «احتمالاً واژه‌ای جدا» می‌داند و ویکی‌واژه ریشهٔ *h₂weks- «نیرومند شدن» یا وام از کارتولی را هم آورده است. پس ریشه با احتیاط پذیرفتنی است.\",\n\"sources\":[W+\"Reconstruction:Proto-Indo-European/wegʷ-\",W+\"Reconstruction:Proto-Indo-European/uksḗn\"],\n\"ref_check\":[POK_WET],\n\"consulted\":[AHD_WET, WLD_WET,\n {\"src\":\"IEC\",\"where\":\"IEC.txt line 19551 s.v. uksó(n)\",\"stance\":\"partial\",\"note\":\"Mann lists 'uksó(n), uksen- ox. WP I, 249 Skt. ukṣán, Av. uxšan-, Tokh. B okso, W ych, Go. aúhsa ...' as an independent headword, not under 'wet'.\"}],\n\"nodes\":[\n{\"id\":1,\"lang\":\"Avestan\",\"words\":\"uxšan\",\"verdict\":\"plausible\",\n\"derivation\":\"Av. uxšan- m. 'bull, ox' (Bartholomae lists it with aršan- and varšni- as words for male animals) = Skt. ukṣán- < Proto-Indo-Iranian *(H)ukšā́ < PIE *uksḗn (Iranian *-ks- > -xš-). The word and its cognates are certain; Nourai's gloss 'inseminating animal' follows Pokorny/Klein, who connect it with Skt. ukṣ- 'sprinkle' and *ugʷ- 'wet', a link Buck calls 'prob.' and Watkins doubts; alternatives are *h₂weks- 'grow' or a Wanderwort (cf. Kartvelian *usx-).\",\n\"derivation_fa\":\"اوستایی uxšan- «نرگاو» هم‌ریشه با سنسکریت ukṣán- است و از هندوایرانی *(H)ukšā́ و هندواروپایی *uksḗn می‌آید (ks در ایرانی به xš بدل شده). خود واژه قطعی است، ولی معنای «جانور بارورکننده» و پیوند آن با سنسکریت ukṣ- «پاشیدن» و ریشهٔ «تر» تنها نظر پوکورنی و کلاین است؛ واتکینز در آن تردید دارد و برخی آن را از *h₂weks- «بالیدن» یا وام‌واژه‌ای کهن می‌دانند. با احتیاط پذیرفتنی است.\",\n\"sources\":[W+\"Reconstruction:Proto-Indo-European/uksḗn\"],\n\"ref_check\":[POK_WET,\n {\"ref\":\"KLN:1106\",\"status\":\"supports\",\"note\":\"KLN_1966.txt line 26833 (leaf 591) s.v. ox: '... OI. ukṣā, Avestic uxshan-, ox, bull, Toch. B okso, ox, fr. I.-E. base *uksen-, male animal, lit. besprinkler, fr. base *uks-, to sprinkle, whence OI. ukṣati, sprinkles. This base is related to base *ugʷ-, wet, moist ... L. ūmor'.\"},\n {\"ref\":\"SYN:153\",\"status\":\"partial\",\"note\":\"SYN.txt line 4111: 'Skt. ukṣan-, Av. uxšan- bull, prob. : Skt. ukṣ- sprinkle, emit seed, Grk. ὑγρός moist' — 'prob.' only.\"}],\n\"consulted\":[{\"src\":\"BRT\",\"where\":\"BRT.txt line 12415 s.v. daēnav-\",\"stance\":\"supports\",\"note\":\"'daēnav- f. femina, von (vierfüssigen) Tieren (im Gegensatz zu aršan-, uxšan- und varšnay-)' — confirms uxšan- as the male animal word.\"},\n {\"src\":\"IEC\",\"where\":\"line 19551\",\"stance\":\"partial\",\"note\":\"'uksó(n), uksen- ox ... Av. uxšan-' as an independent root.\"},\n AHD_WET]},\n{\"id\":2,\"lang\":\"Germanic\",\"words\":\"uhsôn\",\"verdict\":\"plausible\",\n\"derivation\":\"Proto-Germanic *uhsô (n-stem, oblique *uhsan-, Kroonen p. 558) < PIE *uksḗn with Grimm's law *k > *h before s; it gives Goth. auhsa, ON oxi/uxi, OHG ohso, OE oxa. The Germanic form is secure; its descent from the 'wet' root is the same uncertain step as in node #1.\",\n\"derivation_fa\":\"ژرمنی آغازین *uhsô (با k → h بنا بر قانون گریم) از *uksḗn است و گوتی auhsa، آلمانی کهن ohso و انگلیسی کهن oxa از آن آمده‌اند. خود صورت ژرمنی قطعی است، ولی پیوندش با ریشهٔ «تر» همان فرضیهٔ نامطمئن است. با احتیاط پذیرفتنی است.\",\n\"sources\":[W+\"Reconstruction:Proto-Germanic/uhsô\"],\n\"ref_check\":[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"AHD_watkins1985 s.v. wegʷ-: '*ukʷs-en-, bull, ox, in Germanic *uhsōn- in Old English oxa' — but 'probably a distinct Indo-European word'.\"}],\n\"consulted\":[{\"src\":\"POK\",\"where\":\"p. 1118\",\"stance\":\"supports\",\"note\":\"'Gothic auhsus (Gen. Pl. auhsne), Old Icelandic oxi, Old English oxa, Old High German ohso ox' under uegʷ-.\"},\n {\"src\":\"KLN\",\"where\":\"line 26833 s.v. ox\",\"stance\":\"supports\",\"note\":\"'OE. oxa, rel. to OS., OHG. ohso, ON. oxi, uxi ... Goth. auhsa'.\"}, SYN_OX]},\n{\"id\":3,\"lang\":\"English\",\"words\":\"ox\",\"verdict\":\"confirmed\",\n\"derivation\":\"English ox < ME oxe < OE oxa (pl. oxan, hence oxen) < Proto-West Germanic *ohsō < Proto-Germanic *uhsô (u > o before a in the next syllable). The Germanic → English step is undisputed.\",\n\"derivation_fa\":\"انگلیسی ox از انگلیسی میانه oxe و انگلیسی کهن oxa (جمع oxan، از این رو oxen) و ژرمنی آغازین *uhsô است. این گام قطعی است. ادعای نورایی درست است.\",\n\"sources\":[W+\"Reconstruction:Proto-Germanic/uhsô\"],\n\"ref_check\":[{\"ref\":\"(none)\",\"status\":\"not_checked\",\"note\":\"Node has no reference of its own; AHD wegʷ- §4 lists OX.\"}],\n\"consulted\":[{\"src\":\"KLN\",\"where\":\"line 26833\",\"stance\":\"supports\",\"note\":\"'ox, n. — ME., fr. OE. oxa'.\"},\n {\"src\":\"SKT\",\"where\":\"SKT.txt leaf 345 s.v. Ox\",\"stance\":\"supports\",\"note\":\"'Ox. (E.) M.E. ox, pl. oxen ... Goth. auhsa ... Skt. ukshan, an ox (lit. impregnator)'.\"}]},\n{\"id\":4,\"lang\":\"Latin\",\"words\":\"hŭmĕre\",\"verdict\":\"transcription_suspect\",\n\"error_in\":\"book\",\"book_prints\":\"hŭmĕre\",\"correct_form\":\"(h)ūmēre\",\n\"derivation\":\"The book prints 'hŭmĕre' with breves, but the Latin verb is ūmeō, ūmēre (2nd conjugation, long ū and long ē; the h- spelling is a secondary one, by association with humus) — a misprint in the book, faithfully extracted. Pokorny, Watkins and Klein derive it from *ugʷ-smo- (zero grade of *wegʷ- 'wet'), comparing Gk. hugrós and ON vǫkr; de Vaan and Weiss doubt this and reconstruct *uh₁mo- 'wet' instead, so the derivation itself is the traditional but contested view.\",\n\"derivation_fa\":\"کتاب این واژه را hŭmĕre با نشانهٔ کوتاهی چاپ کرده، حال آن‌که صورت درست لاتین ūmeō, ūmēre (با ū و ē بلند) است و h- آغازین بعدها به قیاس با humus افزوده شده؛ این خطای چاپی کتاب است نه خطای خوانش. پوکورنی، واتکینز و کلاین آن را از *ugʷ-smo- (درجهٔ صفرِ *wegʷ- «تر») و هم‌ریشه با یونانی hugrós می‌دانند، ولی دو وان و وایس در این تردید دارند و *uh₁mo- را پیشنهاد می‌کنند. پس اشتقاق با احتیاط پذیرفتنی است و صورت چاپی نادرست.\",\n\"sources\":[W+\"umeo\",W+\"Reconstruction:Proto-Indo-European/wegʷ-\"],\n\"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985 s.v. wegʷ-: '2. Suffixed zero-grade form *ugʷ-sm- in: a. Latin (h)ūmēre, to be wet: HUMECTANT, HUMID; b. Latin (h)ūmor, fluid: HUMOR'.\"}],\n\"consulted\":[{\"src\":\"POK\",\"where\":\"p. 1118\",\"stance\":\"supports\",\"note\":\"'umeo, -ēre humid, wet sein, umor dampness, umecto befeuchte (based on *ugʷsmos)'.\"},\n {\"src\":\"KLN\",\"where\":\"KLN_1966.txt leaf 403 s.v. humid\",\"stance\":\"supports\",\"note\":\"'humid, adj. — F. humide, fr. L. (h)ūmidus, moist, wet, fr. (h)ūmere, to be moist or wet'.\"},\n {\"src\":\"SKT\",\"where\":\"leaf 234 s.v. Humid\",\"stance\":\"supports\",\"note\":\"'L. humidus, better umidus, moist. — L. humere, umere, to be moist; cf. uuidus, udus ... Gk. ὑγρός'.\"}]},\n{\"id\":5,\"lang\":\"English\",\"words\":\"humid; humor\",\"verdict\":\"confirmed\",\n\"derivation\":\"humid (15th c.) < Old French humide < Latin (h)ūmidus 'moist' < ūmēre; humor/humour (14th c.) < Anglo-French/Old French humour < Latin (h)ūmor 'fluid, moisture', the medieval medical sense 'bodily fluid' (the four humours) giving 'temperament, mood' and from the 16th-17th c. 'amusing quality'.\",\n\"derivation_fa\":\"humid از فرانسوی کهن humide و لاتین (h)ūmidus «نمناک» است و humor از فرانسوی کهن humour و لاتین (h)ūmor «مایع، رطوبت»؛ معنای «خلط بدن» در پزشکی قرون وسطا به «خوی، حال» و سپس «شوخ‌طبعی» گشته است. ادعای نورایی درست است.\",\n\"sources\":[W+\"humid\",W+\"humor\"],\n\"ref_check\":[{\"ref\":\"(none)\",\"status\":\"not_checked\",\"note\":\"Node has no reference of its own; AHD wegʷ- §2 lists HUMID, HUMOR.\"}],\n\"consulted\":[{\"src\":\"KLN\",\"where\":\"leaf 403 s.v. humid; line 26833 s.v. ox ('L. ūmor ... See humor')\",\"stance\":\"supports\",\"note\":\"'humid ... fr. L. (h)ūmidus ... fr. (h)ūmere'.\"},\n {\"src\":\"SKT\",\"where\":\"leaf 234 s.v. humour\",\"stance\":\"supports\",\"note\":\"'humour, orig. moisture, (F.-L.) ... The four humours, according to Galen ... O.F. humor'.\"}]}\n]}\nentries.append(e2)\n\nout={\"pdf_page\":531,\"book_page\":501,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-16\",\"entries\":entries}\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-531.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-531.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-531.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 531",
 "description": "Build page-531 JSON and run checker"
}
```


### [2026-10-16T05:21:29.786Z] TOOL RESULT

```
nodes verified: 14/14
node verdicts: {'plausible': 6, 'confirmed': 7, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1, 'plausible': 2}
ref checks: {'supports': 12, 'partial': 5, 'not_found': 1, 'not_checked': 4}
books consulted: {'partial': 8, 'supports': 33, 'silent': 1} | by book: {'KLN': 7, 'BRT': 4, 'WLD': 4, 'POK': 4, 'SKT': 4, 'CHEUNG': 3, 'AHD': 3, 'PHD': 2, 'HRN': 2, 'HUB': 2, 'IEC': 2, 'KNT': 1, 'NYB': 1, 'ARY': 1, 'BQT': 1, 'SYN': 1}
```


## [2026-10-16T05:21:43.222Z] TOOL CALL #51: SubagentHandback

```json
{
 "message": "I've finished verifying page 531 (book page 501). The results are in `/home/sfmqrb/git/rishe-private/data/verification/page-531.json`, and `verify_check.py 531` reports 0 PROBLEM lines, with all 14 nodes verified.\n\n**Verdict counts**\n- **Roots:** 1 confirmed (Wegh), 2 plausible (Wěğo and Wegw/Uksen).\n- **Nodes:** 7 confirmed, 6 plausible, 1 transcription_suspect, 0 disputed.\n\n**Transcription flag**\n- **Wegw, Latin \"hŭmĕre\":** the book prints breves, but the Latin verb is (h)ūmēre, with long ū and long ē. This is the author's misprint, and the extraction matches the page (`error_in: book`). The page image is saved at `data/verification/sources/refs/ocr/BOOK/531.png`. The derivation from *wegʷ- is the traditional view; de Vaan and Weiss instead reconstruct *uh₁mo-.\n\n**Notable plausible items (no outright disputes)**\n- **Wegh, Avestan \"vaza 1: a bird, hawk\":** Bartholomae, Pokorny and Cheung know vaza- only as an adjective meaning \"driving, flying\". \"pairi-vaza\" is not attested; it is a reconstruction behind parvâz.\n- **Wegh, Avestan \"vašta 2: curved\":** vašta- is only the past participle \"conveyed\". No source gives the sense \"curved\".\n- **Wegh, Avestan \"uždar, uždri\":** the form is reconstructed from a personal name only.\n- **Wegh, Persian \"bâz\" (hawk):** the derivation from vaz- \"fly\" is not supported by Horn or Bartholomae, and Wiktionary compares Sanskrit bhāsa- instead. parvâz and vazîdan are confirmed by Horn, MacKenzie, Nyberg, Cheung and Mo'in's notes in Borhan-e Qate' (BQT 2279).\n- **Wegh, English \"wave 2\":** this is a hybrid. One source is Middle English wawe from Old English wǣg, which goes back to *weǵʰ-. The other is the verb wave from Old English wafian, from a different root (*webʰ-). Skeat derives the noun from the verb.\n- **Uksen (ox):** the Pokorny/Klein link of ox to the root meaning \"wet / inseminate\" is only one hypothesis; Watkins says \"probably a distinct Indo-European word\". This affects the root, Avestan uxšan and Germanic uhsôn.\n- **Wěğo:** this root comes from Mann (IEC 1499) only, and he marks it \"(?)\". The Iranian chain from Avestan vazaγā- to vazaγ is secure (Bartholomae col. 1389, Horn 242, BQT 2278).\n\n**Extraction errors:** none. The JSON matches the printed page.\n\n**References I could not verify:**\n- **BQT:391 (parvâz):** I couldn't find the entry in the scanned text.\n- **BQT:217 (bâz):** the hawk headword is there, but Mo'in's etymology note can't be read in the scan.\n- **MON (Mo'in) page numbers:** these can't be matched to the online entries, so I checked meanings only via vajehyab.\n- **Etymonline:** none of its pages could be fetched, so I used Wiktionary instead."
}
```


### [2026-10-16T05:21:43.551Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
