# Verification process log — verify-page-524


## [2026-10-16T05:13:01.644Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 524 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-524.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-524.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-524.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 524` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:01.690Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:06.420Z] TOOL CALL #1: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md; echo ====; cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-524.txt; echo ====; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-524.json",
 "description": "Read instructions, chart text, and source JSON"
}
```


### [2026-10-16T05:13:07.197Z] TOOL RESULT

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


## [2026-10-16T05:13:11.729Z] TOOL CALL #2: Bash

```json
{
 "command": "sed -n 40,120p /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md",
 "description": "Read the truncated middle of the instructions"
}
```


## [2026-10-16T05:13:12.322Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-524.txt",
 "description": "Read page 524 chart text"
}
```


### [2026-10-16T05:13:12.643Z] TOOL RESULT

```
=== PDF page 524 (book page 494) ===
--- entry 0 ---
ROOT [Sanskrit] Velŭr, Bĕlŭr
Vaidŭrya, Veluryia : a city in southern India (from a Dravidian root)
a crystal "from Velŭr".  (refs KLN:166; AHD:126)
#1 (parent #0) [Greek] refs=AHD:126; KLN:166 | beryllos, bĕrullos : the beryl crystal
  #2 (parent #1) [Arabic] refs=MON:575 | bolŭr : crystal ; tabalvor ; motebalver
    #3 (parent #2) [Persian] refs=MON:575 | bolŭr «بُلور» : crystal, clear | extra: تبلور ، متبلور
  #4 (parent #1) [Latin] refs=AHD:126 | beryllus : beryl
    #5 (parent #4) [French] refs=AHD:126,166 | beryl, brillat
      #6 (parent #5) [Persian] refs=MON:511 | berelyân «برلیان» : cut diamond
      #7 (parent #5) [English] refs=AHD:126,166; KLN:200 | beryl, beryllium, brilliant
--- entry 1 ---
ROOT Veluryia -> redirect to Velŭr
--- entry 2 ---
ROOT Věno -> redirect to Wes 5
--- entry 3 ---
ROOT Vesno -> redirect to Wes 5
--- entry 4 ---
ROOT Veso -> redirect to Wes 5
--- entry 5 ---
ROOT [Old Persian] Vrsa, Vrsna : hunger  (refs BQT:1794)
#1 (parent #0) [Pahlavi] refs=BQT:1794 | gursak : hungry ; gursakîh : hunger ; gursîtan : to be hungry
  #2 (parent #1) [Persian] refs=BQT:1794; HUB:92 | gors 1 «گرس ۱» : hunger ; goresneh «گرسنه» : hungry | extra: گورس ، گرسنگی ، گشنگی ، گشنه
#3 (parent #0) [Sogdian] refs=SOD:79,414 | wš`y : to be hungry ; wšn, `wšnty : hungry
--- entry 6 ---
ROOT Vrsna -> redirect to Vrsa
```


### [2026-10-16T05:13:12.648Z] TOOL RESULT

```
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
```


## [2026-10-16T05:13:15.680Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 120,175p /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-524.json | head -c 6000; ls /home/sfmqrb/git/rishe-private/data/verification/ | head; cat /home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md | head -80",
 "description": "Read rest of instructions, JSON, source matrix"
}
```


### [2026-10-16T05:13:16.025Z] TOOL RESULT

```
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
{
  "pdf_page": 524,
  "book_page": 494,
  "entries": [
    {
      "root": {
        "name": "Velŭr, Bĕlŭr\nVaidŭrya, Veluryia",
        "lang": "Sanskrit",
        "refs": "KLN:166; AHD:126",
        "gloss": "a city in southern India (from a Dravidian root)\na crystal \"from Velŭr\"."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:126; KLN:166",
          "words": [
            {"translit": "beryllos, bĕrullos", "gloss": "the beryl crystal", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "MON:575",
          "words": [
            {"translit": "bolŭr", "gloss": "crystal", "script": null},
            {"translit": "tabalvor", "gloss": null, "script": null},
            {"translit": "motebalver", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:575",
          "words": [
            {"translit": "bolŭr", "gloss": "crystal, clear", "script": "بُلور"}
          ],
          "script_extra": "تبلور ، متبلور",
          "note": null,
          "quote": {
            "text": "بی تو بی جان تنی است جام بلور - تن پاکیزه جام را جان باش",
            "poet": "Mas`ŭd Sa`d Salmân"
          }
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Latin",
          "refs": "AHD:126",
          "words": [
            {"translit": "beryllus", "gloss": "beryl", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": "AHD:126,166",
          "words": [
            {"translit": "beryl, brillat", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:511",
          "words": [
            {"translit": "berelyân", "gloss": "cut diamond", "script": "برلیان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "English",
          "refs": "AHD:126,166; KLN:200",
          "words": [
            {"translit": "beryl, beryllium, brilliant", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Veluryia",
        "redirect": "Velŭr"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Věno",
        "redirect": "Wes 5"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Vesno",
        "redirect": "Wes 5"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Veso",
        "redirect": "Wes 5"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Vrsa, Vrsna",
        "lang": "Old Persian",
        "refs": "BQT:1794",
        "gloss": "hunger"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT:1794",
          "words": [
            {"translit": "gursak", "gloss": "hungry", "script": null},
            {"translit": "gursakîh", "gloss": "hunger", "script": null},
            {"translit": "gursîtan", "gloss": "to be hungry", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1794; HUB:92",
          "words": [
            {"translit": "gors 1", "gloss": "hunger", "script": "گرس ۱"},
            {"translit": "goresneh", "gloss": "hungry", "script": "گرسنه"}
          ],
          "script_extra": "گورس ، گرسنگی ، گشنگی ، گشنه",
          "note": null,
          "quote": {
            "text": "گرس از دلم ببرد غم زلف و خال دوست - جان با خیال رشته فتاد از خیال دوست",
            "poet": "Bes-hâq"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:79,414",
          "words": [
            {"translit": "wš`y", "gloss": "to be hungry", "script": null},
            {"translit": "wšn, `wšnty", "gloss": "hungry", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Vrsna",
        "redirect": "Vrsa"
      },
      "nodes": []
    }
  ]
}
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


## [2026-10-16T05:13:20.888Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 175,200p /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md; sed -n 80,200p /home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md; cat /home/sfmqrb/git/rishe-private/tools/verify_check.py | head -150",
 "description": "Read rest of instructions, matrix, and checker"
}
```


### [2026-10-16T05:13:21.292Z] TOOL RESULT

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
                    con_books[c.get("src")] += 1
    print(f"nodes verified: {nodes_done}/{nodes_total}")
    print("node verdicts:", dict(tally))
    print("root verdicts:", dict(root_tally))
    print("ref checks:", dict(ref_tally))
    print("books consulted:", dict(con_tally), "| by book:", dict(con_books.most_common(40)))
    if missing_pages:
        print(f"pages without verification ({len(missing_pages)}):", " ".join(map(str, missing_pages)))
    for p in problems:
        print("PROBLEM:", p)
    if "--flagged" in os.environ.get("VERIFY_OPTS", "") or os.environ.get("FLAGGED"):
        for f in flagged:
            print("FLAG:", *f[:4], "|", f[4][:200])
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```


## [2026-10-16T05:13:24.599Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['KLN','AHD','MON','BQT','HUB','SOD','HRN','PHD','NYB']:\n  e=d.get(k,{}); print(k, {x:e.get(x) for x in ['kind','url','lookup_hint','local_file','page_offset','scans']})\n\"",
 "description": "Look up reference metadata"
}
```


### [2026-10-16T05:13:25.013Z] TOOL RESULT

```
KLN {'kind': 'archive_djvu', 'url': 'https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None}
AHD {'kind': 'archive_djvu+website+archive_restricted', 'url': 'https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only', 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).", 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'scans': None}
MON {'kind': 'website+archive_djvu', 'url': 'https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)', 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'scans': None}
BQT {'kind': 'archive_djvu+local_scan_ocr', 'url': "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", 'lookup_hint': "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'], 'page_offset': "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').", 'scans': [{'volume': '3', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]}
HUB {'kind': 'archive_djvu', 'url': 'https://archive.org/details/persischestudie00hbgoog', 'lookup_hint': "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt', 'page_offset': 'leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None}
SOD {'kind': 'archive_djvu', 'url': 'https://archive.org/details/SogdianDictionary', 'lookup_hint': "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt'], 'page_offset': 'printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)', 'scans': None}
HRN {'kind': 'archive_djvu', 'url': 'https://archive.org/details/grundrissderneu00horngoog', 'lookup_hint': "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None}
PHD {'kind': 'archive_djvu', 'url': 'https://archive.org/details/a-concise-pahlavi-dictionary', 'lookup_hint': "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).", 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt', 'page_offset': 'leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None}
NYB {'kind': 'archive_djvu', 'url': 'https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg', 'lookup_hint': "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", 'local_file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt', 'page_offset': 'Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'scans': None}
```


## [2026-10-16T05:13:36.161Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/524.* 2>/dev/null; mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p524; pdftoppm -f 524 -l 524 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p524/pg524 && ls /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p524",
 "description": "Render printed page 524 to PNG"
}
```


### [2026-10-16T05:13:37.061Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   62k sfmqrb 14 Oct 22:15  site/pages/524.jpg
Permissions Size User   Date Modified Name
.rw-r--r--   69k sfmqrb 16 Oct 01:13  pg524.png
```


## [2026-10-16T05:13:39.414Z] TOOL CALL #8: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p524/pg524.png"
}
```


### [2026-10-16T05:13:39.943Z] TOOL RESULT

```

```


## [2026-10-16T05:13:39.854Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-16T05:13:44.748Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^beryl' KLN_1966.txt | head; grep -n -i '^brilliant\\|^brill,\\|^brilliance' KLN_1966.txt | head; grep -n -i 'beryl' AHD_watkins1985.txt SKT.txt LKT.txt POK_full.txt IEC.txt 2>/dev/null | head -20; grep -n -i '^brilliant\\|^BRILLIANT\\|^beryl\\|^BERYL' SKT.txt | head",
 "description": "Grep beryl/brilliant in Klein, AHD, Skeat, Lokotsch"
}
```


### [2026-10-16T05:13:45.200Z] TOOL RESULT

```
5652:brilliance,  brilliancy,  n.  - —  Formed  fr.  next  word with  suff.  -ce,  resp.  -cy.
5653:brilliant,  adj.  —  F.  brillant,  lit.  ‘shining’,  pres, part,  of  briller,  ‘to  shine’,  fr.  VL.  *beryllare,  ‘to shine  like  a  beryl’,  fr.  L.  beryllus,  fr.  Gk.  pf;- pukko;,  ‘beryl’.  See  beryl  and  -ant.
5655:brilliantine,  n.,  an  oily  liquid  used  to  make  the hair  glossy.  —  F.  brillantine,  fr.  brillant,  ‘shin¬ ing’.  See  prec.  word.
9882:brilliant;  2)  armor  covering  the  hinder  part  of the  body.  —  F.,  dimin.  of  cul,  ‘backside,  poste¬ rior,  bottom’,  fr.  L.  cuius,  ‘posterior,  fundament’, which  is  cogn.  with  OIr.  cul,  W.  cil,  ‘back’.  Cp. culot,  culotte,  bascule,  recoil  and  the  first  ele¬ ment  in  cul-de-sac.  For  the  ending  see  suff.  -et. Culex,  n.,  a  genus  of  mosquitoes.  —  L.  culex, ‘gnat’,  cogn.  with  OIr.  cuil  (for  *ku-li)  ‘gnat’, W.  cylionen,  ‘gnat,  fly’,  Co.  kelionen,  ‘fly’  and prob.  also  with  OI.  sula-,  ‘spear,  spit’.  These words  possibly  derive  fr.  I.-E.  *kul-,  enlargement of  base  *kd-,  ‘pointed’,  whence  also  L.  caucus, ‘wedge’.  See  coin.
SKT.txt:1733:Beryl.   (L.-Ck.-Skt.)    M.E. L.    beryllus.  —  Gk.    ^/j^t/AAot ; hilhiur,  cr^'stal,  beryl.  —  SV '      ■  -  ' lai'ii  l.-culi,  brnuj^ht  from
SKT.txt:1734:brilliantjshininf;.  (,F  - F.  brillaui,  prei.  pait.  o' cf,    Ital.  brillare,   to  s|  ^i Ken^e    was    to   sparkle  aii    a    bwii bery/lHj.   a   beryl;    whence    a!*© btrilluSf  an  eye-glaw,  O.  ^ri/Ah
SKT.txt:2310:Brilliant,  shining:  sec  Beryl- Brim.    (E.)      M.E.  *rj'w,      A.S.  *n*«, surf,  burgc  nn  the  shore.  +  Jcel.  brim,  surf, G.  br<\m4,  border,  M.  H.  G.  brtm,  border; Ski.  bkrimi,  a  whirl-pool,  from  bhram,  loj whirl.     The  brim  of  Uie  sea  is  its  maigiit,, where  the  surf  is  heard  to  roar;  cf.   L,j frtmtn.   \^  BHkAM.)
SKT.txt:23632:French  from  iMtn  from  Greek  from Sanskrit;  beryl,  briUioiit,  ginger,  mace (a),  saccharine.
1733:Beryl.   (L.-Ck.-Skt.)    M.E. L.    beryllus.  —  Gk.    ^/j^t/AAot ; hilhiur,  cr^'stal,  beryl.  —  SV '      ■  -  ' lai'ii  l.-culi,  brnuj^ht  from
1734:brilliantjshininf;.  (,F  - F.  brillaui,  prei.  pait.  o' cf,    Ital.  brillare,   to  s|  ^i Ken^e    was    to   sparkle  aii    a    bwii bery/lHj.   a   beryl;    whence    a!*© btrilluSf  an  eye-glaw,  O.  ^ri/Ah
2310:Brilliant,  shining:  sec  Beryl- Brim.    (E.)      M.E.  *rj'w,      A.S.  *n*«, surf,  burgc  nn  the  shore.  +  Jcel.  brim,  surf, G.  br<\m4,  border,  M.  H.  G.  brtm,  border; Ski.  bkrimi,  a  whirl-pool,  from  bhram,  loj whirl.     The  brim  of  Uie  sea  is  its  maigiit,, where  the  surf  is  heard  to  roar;  cf.   L,j frtmtn.   \^  BHkAM.)
```


## [2026-10-16T05:13:48.846Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'beryl,\\|^beryl' KLN_1966.txt | head -5; grep -n -i 'beryl' KLN_1966.txt | head -8; grep -n -i 'beryl' LKT.txt FSD_vol1.txt WEB_vol1.txt HJB*.txt 2>/dev/null| head -12; grep -n 'بلور\\|billaur\\|bill[aā]wr\\|bul[uū]r' AFM.txt LKT.txt FVQ.txt PLA*.txt incoming/PLA/PLA_pages.txt 2>/dev/null | head",
 "description": "Grep beryl entry in Klein, Lokotsch, others"
}
```


### [2026-10-16T05:13:49.275Z] TOOL RESULT

```
4810:Berula,  n.,  a  genus  of  plants  of  the  parsley  family (bot.)  —  L.  berula,  ‘water  cress’,  dissimilated  fr. *beruva,  a  word  of  Celtic  origin.  Cp.  W.  berwr, Mir.  biror,  bilor,  ‘water  cress’, beryl,  n.  —  ME.,  fr.  OF.  beryl  (F.  beryl),  fr.  L. beryllus,  fr.  Gk.  (Jtjp'jXXos,  fr.  Prakrit  veruliya, transposed  fr.  vi/uriya  (whence  Ol.  vaidiirya-), which  prob.  derives  from  the  name  of  the  city Velur  (now  called  Belur).  Cp.  G.  Brille,  ‘spec¬ tacles’,  from  the  pi.  of  MHG.  bril,  of  s.m.,  which derives  fr.  MHG.  berille,  ‘beryl’,  fr.  L.  beryl- las  (the  first  spectacles  were  made  from  beryl). Cp.  also  brilliant,  the  first  element  in  besiclo- meter  and  the  second  element  in  chrysoberyl. beryllium,  n.,  a  metallic  element,  called  also ghteinum  ( chem .)  —  ModL.,  fr.  L.  beryllus  (see beryl);  so  called  because  it  was  first  obtained through  isolation  from  beryl  (by  the  French chemist  Nicolas-Louis  Vauquelin  in  1797).  For the  ending  see  suff.  -ium.
7614:Chrysemys,  n.,  a  genus  of  American  turtles  (zool.) —  ModL.,  compounded  of  chrys-  and  Gk.  cpu;, ‘fresh  water  turtle’.  See  Emys. chryso-,  before  a  vowel  chrys-,  combining  form meaning  ‘gold,  golden,  golden  yellow’.  —  Gk. Xpono-,  xpu or-,  fr. /putt6;,  ‘gold’.  See  chrysalis, cbrysoberyl,  n.,  a  semi-precious  stone  (mineral.) — •  L.  chrysoberyllus,  fr.  Gk.  / poco  |3  f] poXXo ; , which  is  compounded  of  /poao ;,  ‘gold’,  and pfjpuXXo;,  ‘beryl’.  See  chrysalis  and  beryl. Chrysochloris,  n.,  a  genus  of  moles  (zool.) ModL.,  lit.  ‘golden  yellow’,  compounded  ofGk. Z_pu <r6;,  ‘gold’,  and  /Xiopo;,  ‘greenish  yellow  , See  chrysalis  and  chlorine, chrysolite,  n.,  a  magnesium  iron  silicate.  —  ME. crisolite  (F.  chrysolithe),  fr.  L.  chrysolithus ,  fr. Gk.  /pucAXiffo;,  which  is  compounded  of Xpucjo;,  ‘gold’,  and  Xifloc,  ‘stone’.  See  chrysalis and  -lite.
2158:alevin,  n.,  a  young  fish.  —  F.,  ‘fry,  young  fish’, fr.  OF.  alevain,  fr.  VL.  *allevdmen,  fr.  L.  alle- vdre,  ‘to  lift  up,  lighten,  alleviate’,  in  VL.  also ‘to  bring  up,  rear’,  fr.  ad-  and  levare,  ‘to  raise, lift  up’.  See  lever  and  cp.  elevate.  The  French form  alevin  (fr.  OF.  alevain)  is  due  to  the  change of  suff.  -ain  (fr.  L.  -amen)  to  suff.  -in  (fr.  L.  -inus). Alexander,  masc.  PN.  —  L.  Alexander,  fr.  Gk. ’AXl^otvSpoi;,  lit., ‘defender  of  men’,  fr.  d&iijeiv, ‘to  ward  off,  keep  off,  turn  away,  defend,  pro¬ tect,  and  avfjp,  gen.  avSpO!;,  ‘man’.  ’AXeijeiv  is desiderative  of  (xXexeiv,  ‘to  ward  off’,  which  is related  to  aXxir),  ‘protection,  help,  strength, power,  courage’,  #Xxi|jlo9,  ‘strong’,  and  cogn. with  OI.  raksati,  ‘protects’,  OE.  ealgian,  ‘to  de¬ fend’,  and  possibly  also  with  OE.  ealh,  OS. alah,  Goth,  alhs,  ‘temple’,  OLith.  elkas,  alkas, ‘sacred  wood’,  Lett,  elks,  ‘idol’.  Cp.  Alcmene, alexin,  alexipharmic,  Alexis,  Alexius,  Alcestis, analcite.  Cp.  also  lac,  ‘one  hundred  thousand’. For  the  2nd  element  in  Alexander  see  andro-. alexanders,  the  meadow  parsnip.  —  Lit.  ‘the flower  of  Alexander  (the  Great)’;  so  called  for its  brilliant  color  suggesting  royalty. Alexandrine,  n.,  a  verse  of  six  iambic  feet,  having the  caesura  after  the  third.  —  F.  alexandrin;  so called  because  first  used  by  the  French  poet Alexandre  de  Paris  (de  Bernai)  in  a  poem  on Alexander  the  Great,  dating  from  the  13th  cent, alexandrite,  n.,  a  dark  green  variety  of  chryso- beryl  (mineral.)  —  Named  after  Alexander  II of  Russia.  For  the  ending  see  subst.  suff.  -ite. alexia,  n.,  inability  to  read  (med.)  —  Medical  L., formed  fr.  priv.  pref.  a-  and  Gk.  ‘speech’, from  the  stem  of  XsyEiv,  to  tell,  say,  speak’ (see  lexicon),  but  confused  in  meaning  with  L. legere,  ‘to  read’.  For  the  ending  see  suff.  -ia. alexin,  n.,  a  substance  which  destroys  bacteria (immunology).  — Coined  by  the  German  bacteri¬ ologist  Hans  Buchner  (1850-1902)  in  1888,  fr. Gk.  (xXeEeiv,  ‘to  ward  off.  keep  off.  protect’. See  Alexander  and  chem.  suff.  -in. alexipharmic,  adj.  counteracting  poison,  anti¬ dotal.  —  Gk.  dtXE^i^aptxaxoi;,  ‘acting  as  an  anti¬ dote’,  fr.  aXs^eiv,  ‘to  ward  off,  keep  off,  pro¬ tect’,  and  tpappiaxov,  ‘drug,  poison’.  See  Al¬ exander,  pharmacy  and  -ic.
3261:aquamarine,  n.,  a  transparent  bluish-green  variety of  beryl  (mineral.)— U  aqua  marina,  ‘sea  water’, fr.  aqua,  ‘water’,  and  marina,  fern,  of  marinus, ‘of  the  sea’.  See  aqua  and  marine, aqua  regia,  mixture  of  concentrated  nitric  and hydrochloric  acid  (chem.)  —  L.,  lit.  ‘royal water’ ;  so  called  from  its  power  to  dissolve  gold, ‘the  king  of  metals’.  See  aquatic  and  regal, aquarelle,  n.,  a  water  color  painting.  —  F.,  fr.  It. acquerella,  ‘water  color’,  dimin.  of  acqua,  ‘wa¬ ter’,  fr.  L.  aqua.  See  aquatic.
4809:Bertram,  masc.  PN.  —  OHG.  Bcrahtram,  lit.  ‘a bright  raven’,  fr.  beraht,  ‘bright’,  and  hram,  a collateral  form  of  hraban,  ‘raven’.  See  bright  and raven  and  cp.  the  second  element  in  Ingram, bertrandite,  n.,  a  beryllium  silicate  (mineral.)  — Named  after  the  French  mineralogist  E.  Ber¬ trand,  who  first  analyzed  it.  For  the  ending  see subst.  suff.  -ite.
4810:Berula,  n.,  a  genus  of  plants  of  the  parsley  family (bot.)  —  L.  berula,  ‘water  cress’,  dissimilated  fr. *beruva,  a  word  of  Celtic  origin.  Cp.  W.  berwr, Mir.  biror,  bilor,  ‘water  cress’, beryl,  n.  —  ME.,  fr.  OF.  beryl  (F.  beryl),  fr.  L. beryllus,  fr.  Gk.  (Jtjp'jXXos,  fr.  Prakrit  veruliya, transposed  fr.  vi/uriya  (whence  Ol.  vaidiirya-), which  prob.  derives  from  the  name  of  the  city Velur  (now  called  Belur).  Cp.  G.  Brille,  ‘spec¬ tacles’,  from  the  pi.  of  MHG.  bril,  of  s.m.,  which derives  fr.  MHG.  berille,  ‘beryl’,  fr.  L.  beryl- las  (the  first  spectacles  were  made  from  beryl). Cp.  also  brilliant,  the  first  element  in  besiclo- meter  and  the  second  element  in  chrysoberyl. beryllium,  n.,  a  metallic  element,  called  also ghteinum  ( chem .)  —  ModL.,  fr.  L.  beryllus  (see beryl);  so  called  because  it  was  first  obtained through  isolation  from  beryl  (by  the  French chemist  Nicolas-Louis  Vauquelin  in  1797).  For the  ending  see  suff.  -ium.
4816:besiclometer,  n.,  an  instrument  for  measuring the  forehead  to  establish  the  exact  size  of  the spectacles.  —  A  hybrid  coined  fr.  F.  besides (pi.),  ‘spectacles’,  and  Gk.  jx^Tpov,  ‘measure’. The  first  element  is  an  alteration  of  OF.  bericle, fr.  L.  beryllus,  ‘beryl’.  The  ending  of  OF.  bericle was  prob.  suggested  by  the  synonym  escarboucle, ‘carbuncle’;  see  beryl.  For  the  second  element see  meter,  ‘poetical  rhythm’, beside,  prep.  —  ME.  besiden,  beside,  fr.  OE.  be sidan,  ‘by  the  side’,  fr.  be,  ‘by’,  and  dative  of side,  ‘side’.  See  by  and  side, besides,  adv.  —  Formed  fr.  prec.  word  with  the adv.  gen.  sufif.  -s.
5653:brilliant,  adj.  —  F.  brillant,  lit.  ‘shining’,  pres, part,  of  briller,  ‘to  shine’,  fr.  VL.  *beryllare,  ‘to shine  like  a  beryl’,  fr.  L.  beryllus,  fr.  Gk.  pf;- pukko;,  ‘beryl’.  See  beryl  and  -ant.
7614:Chrysemys,  n.,  a  genus  of  American  turtles  (zool.) —  ModL.,  compounded  of  chrys-  and  Gk.  cpu;, ‘fresh  water  turtle’.  See  Emys. chryso-,  before  a  vowel  chrys-,  combining  form meaning  ‘gold,  golden,  golden  yellow’.  —  Gk. Xpono-,  xpu or-,  fr. /putt6;,  ‘gold’.  See  chrysalis, cbrysoberyl,  n.,  a  semi-precious  stone  (mineral.) — •  L.  chrysoberyllus,  fr.  Gk.  / poco  |3  f] poXXo ; , which  is  compounded  of  /poao ;,  ‘gold’,  and pfjpuXXo;,  ‘beryl’.  See  chrysalis  and  beryl. Chrysochloris,  n.,  a  genus  of  moles  (zool.) ModL.,  lit.  ‘golden  yellow’,  compounded  ofGk. Z_pu <r6;,  ‘gold’,  and  /Xiopo;,  ‘greenish  yellow  , See  chrysalis  and  chlorine, chrysolite,  n.,  a  magnesium  iron  silicate.  —  ME. crisolite  (F.  chrysolithe),  fr.  L.  chrysolithus ,  fr. Gk.  /pucAXiffo;,  which  is  compounded  of Xpucjo;,  ‘gold’,  and  Xifloc,  ‘stone’.  See  chrysalis and  -lite.
10096:cymophane,  n.,  a  wavy  variety  of  chrysoberyl {mineral)  —  Compounded  of  Gk.  xupa,  ‘wave’, and  the  stem  of  ipalvsiv,  ‘to  show’,  (paivcoOat, ‘to  appear’.  See  cyma  and  phantasm, cymoscope,  n.,  a  device  for  detecting  electric waves.  —  Compounded  of  Gk.  xupia,  ‘wave’, and  -onimov,  fr.  oxotteiv,  ‘to  look  at,  examine’. See  cyma  and  -scope.
HJB.txt:143:The  words  with  which  we  have  to  do,  taking  the  most  extensive  view  of the  field,  are  in  fact  organic  remains  deposited  under  the  various  currents of  external  influence  that  have  washed  the  shores  of  India  during  twenty centuries  and  more.  Rejecting  that  derivation  of  elephant*  which  would connect  it  with  the  Ophir  trade  of  Solomon,  we  find  no  existing  Western term  traceable  to  that  episode  of  communication  ;  but  the  Greek  and  Roman commerce  of  the  later  centuries  has  left  its  fossils  on  both  sides,  testifying to  the  intercourse  that  once  subsisted.  Agallochum,  carba^us,  camphor, sandal,  musk,  nard,  pepper  (Wire/w,  from  Skt.  pippali,  *long  pepper'),  ginger (^tyyi^pis,  see  under  Ginger),  lac,  costus,  opal,  malabathrum  or  folium  indicum, beryl,  sugar  {adjcxap,  from  Skt.  sarkara,  Prak.  saJdcara),  rice  (Upvia,  but  see  s.v.), were  products  or  names,  introduced  from  India  to  the  Greek  and  Roman world,  to  which  may  be  added  a  few  terms  of  a  different  character,  such  as Bpax/taret,  ^apfidyes  {sramanas,  or  Buddhist  ascetics),  ^;Xa  ffayaXLpa  koI  <r<urafi[va (logs  of  teak  and  shisham),  the  ffdyycLpa  (rafts)  of  the  Periplus  (see  Jangar in  Gloss.)  ;  whilst  dindra,  dramma,  perhaps  kastira  (*  tin,'  Kaafflrepos),  kasturl (*musk,'  Koardpiov,  properly  a  different,  though  analogous  animal  product), and  a  very  few  more,  have  remained  in  Indian  literature  as  testimony  to  the same  intercourse.t
HJB.txt:3437:BERYL.
HJB.txt:3461:the  West,  it  having  heen  supposed  that its  origin  was  the  Skt.  vaimryOy  Prak. vel^wij  whence  [Malay  haiduri  and hiduri\,  P.  biUaur,  and  Greek  pifpvXkos. Bochart  points  out  the  probable identity  of  the  twro  last  words  by  the transpofiition  of  I  and  r.  Another  trans- position appears  to  have  given  Ptolemy his  'OpoH^ta  6fni  (for  the  Western Ohats),  representing  probably  the native  Vaidurya  mountains.  In Ezekiel  xxvii.  13,  the  Sept.  has fiffp^XXLw,  where  the  Hebrew  now  has ictnh4^  [another  word  with  probably the  same  meaning  being  trnksm  (see Professor  Ridgeway  in  EncycL  BibL S.V.  Beryl)!  Professor  Max  Midler has  treated  of  the  nossible  relation between  vaidHrya  ana  viddUiy  'a  cat,' And  in  connection  with  this  observes that  ^we  should,  at  all  events,  have learnt  the  useful  lesson  that  the •chapter  of  accidents  is  sometimes larger  than  we  suppose." — {India^  What <an  U  Teach  tw^^'^p.  267).  This  is  a lesson  which  many  articles  in  our book  suggest;  and  in  dealing  with the  same  words,  it  may  be  indicated that  the  resemblance  between  the Greek  afXov/m,  hildur^  a  common  H. word  for  a  cat,  and  the  P.  biUaur, *  beryl,'  are  at  least  additional  illustra- tions of  the  remark  quoted.
HJB.txt:3462:c.  A.i>.  70.— "Beryls  .  .  .  from  India thev  oome  as  from  tiieir  native  place,  for seldom  are  they  to  be  found  elsewhere.  .  .  . Those  are  best  aooonnted  of  which  carrie  a «ea-water  greene."— P/tn^,  Bk.  XXXVII. «ap.  20  (in  P.  Holland,  ii.  613).
HJB.txt:24007:Beryl,  886 Besermani,  604a
WEB_vol1.txt:5429:of Al-ex-an‘drine, a. of an Alexandrine or Alex- andrines. Ss, al-ex-an/drite, n. [named after Alexander II, 'h- Czar of Russia.] a variety of chrysoberyl, emerald-green by daylight and deep red by in- artificial light. ch a-lex/i-a, n. [L., from Gr. a priv., and lexis, speech, from legein, to speak.] inability to SS, read, caused by lesions of the brain; word blindness. as a-lex/in, n. [Gr. alexein, to ward off.] a sub- stance found in the blood, capable of destroy- ly. ing bacteria. k; ht- a-lex-i-phar’mic, ålexiphär’mac, a. [L., from Gr. alexipharmdkon; alexein, to ward off, Ing and pharmakon, poison.] expelling or resist- ts. ing poison; antidotal, ted alex-i-phar’mic, a-lex-i-phar’mac, n. an old antidote. q 5 a-lex-i-phar’mic-al, a-lex-i-phir’/mac-Al, a. ind same as alexipharmic.
WEB_vol1.txt:5549:al’/ka-li-fi’a-ble, a. that may be alkalified, or converted into an alkali. al/ka-li-fy, v.t.; alkalified, pt., pp.; alkalifying, ppr. to form or to convert into an alkali. al’/ka-li-fy, v.i. to become an alkali. al-ka-lig’e-nous, a. [alkali, and -genous; Gr. genés, producing.] producing an alkali. al’ka-li land, an arid region, particularly in the western United States, where the soil is strongly impregnated with alkalis which are destructive to vegetation. : alkáli” met’Al, any metal, such as sodium, potassium, or lithium, whose hydroxide is an alkali. al-kà-lim’e-tēr, n. [alkali, and Gr. melron, measure.] an instrument for measuring the quantity of alkali in any solution or mixture. al’/ka li-met’ric, al’/ka-li-met’/ric-Al, a. per- taining to alkalimetry. sea al-ka-lim/e-try, n. the process of determining the strength of alkalis or the amount 0 alkali present in any mixture. y al’kå-līne (or -lin), a. pertaining to an alkali; having the properties of or containing an alkali. al’/ka-line-éarth’ met’ălş, the group of chem- ical elements comprising calcium, strontium, barium, and sometimes, beryllium, magne- sium, and radium. š al’ka-line čarths, the oxides of the alkaline- earth metals. ; al-ka-lin/i-ty, n. the quality or state of being alkaline. ; al-ka/li-ous, a. alkaline. [Obs.] al’/ka-li-zate, a. alkaline. [Obs.] X al/ka-li-za’tion, n. the act of making alkaline; the process of converting into alkali. al’/ka-lize, v.t.; alkalized, pt., pp.; alkalizing, per: to make alkaline. b alkå:loid, n. any of a class of organic com- pounds found in living plants, usually 1m combination with organic acids and having
WEB_vol1.txt:10035:1. a variety of beryl: so called because o its pale, bluish-green color.
WEB_vol1.txt:16260:ba-ry-t6-cal’cite, n. [LL. baryta, barium, from Gr. berylés, weight, and L. calx, calcis, lime.} a compound of carbonate of lime and carbon- ate of barium, of a dark or light gray color, occurring massive or crystallized.
WEB_vol1.txt:16978:Be, in chemistry, beryllium.
WEB_vol1.txt:18610:ry, n. [L._ beryllus; Gr. béryllos, a gem, ber $ beryllium aluminum silicate, Be;Alr
WEB_vol1.txt:18612:ee of beryllium: emerald and aquama-
(eval):1: no matches found: PLA*.txt
```


## [2026-10-16T05:13:54.746Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for ln in 4810 5653; do head -n $ln KLN_1966.txt | tr -cd '\\f' | wc -c; done; grep -n 'بلور' AFM.txt AFM_pages.txt TAD.txt ARB_mo3rb.txt incoming/PLA/PLA_pages.txt MON_part1.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -20; grep -n -i 'bill[aā]u\\?r\\|billaur\\|ballūr\\|bulur\\|ballor\\|billōr' LKT.txt FVQ.txt AFA.txt incoming/PLA/PLA_pages.txt HRN.txt HUB.txt 2>/dev/null | head",
 "description": "Locate Klein pages and grep billaur in Arabic loan sources"
}
```


### [2026-10-16T05:13:55.128Z] TOOL RESULT

```
99
116
MON_part1.txt:785:یک شيشة بلوری که در آب فرر ه۲ 
MON_part1.txt:1060:آ کم بلور. بح. . ژاله» شبنم. تگرگک. 
MON_part1.txt:1204:آبگینه. بلور. 
MON_part1.txt:1234:بلورین که با آن آب خورند آبخوره. 
MON_part1.txt:1622:منجمد. نش . بلور. . شمشیر. حنحر . 
MON_part1.txt:1777:منسوب به شهر شام: آبکینه مخروط: بلور 
MON_part1.txt:4253:رود (غعفص.): آهن آلات؛ بلورالات؛ 
MON_part1.txt:4471:الومینیوم که در طبیعت بصورت بلورین 
MON_part1.txt:5334:گلاویز. (.) منشور و غیر آن از بلور و مانند 
MON_part1.txt:12318:بلوری استوانه شکل نسبهٌباریکک ۱ 
MON_part1.txt:22512:بصورت بلورهایی به شکل منشور مسدس 
MON_part1.txt:22513:القاعده متبلور می‌ گردد و در فصل سرما از 
MON_part1.txt:22695:تبلور الساس را تبعیت می‌کنند (روش 
MON_part1.txt:22699:شکل‌های مسختلفی که بلور الماس در 
MON_part1.txt:25100:بلور: ۲ ,0:۱۳ (۱.) قسمی ششه که از 
MON_part1.txt:26433:نوعی بلور کبود شفاف و کم قیمت. (گیا.) 
MON_part1.txt:26438:نیکک‌بخت. (امر.) (زه.) نوعی بلور کبود و 
MON_part1.txt:27921:آبخوری سر گشاد سفالین یا بلورین و یا 
MON_part1.txt:30939:رنگ بلورهای بش تبرة آن بر اثرانعکاس 
MON_part1.txt:33898:غیر قابل تبلور بنام گلوکوکینین که بنام 
LKT.txt:3212:139U.  Tk.  uiaiidar: 'Lukeiiiiegel,  Drehkreuz'  |Kel6kian  Kä- mtls  1095  b];   hieraus  rum.  mandanea 'Billardbande'  [Löbel  EITAP  61].
```


## [2026-10-16T05:13:59.527Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==100' KLN_1966.txt | head -c 600; echo; echo ---; awk 'BEGIN{RS=\"\\f\"} NR==117' KLN_1966.txt | head -c 400; echo; sed -n 25095,25106p MON_part1.txt; grep -n 'برلیان\\|بریلیان\\|برلیانت' MON_part1.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt | head",
 "description": "Check Klein page numbers and Mo'in entries"
}
```


### [2026-10-16T05:14:00.087Z] TOOL RESULT

```
 vaidiirya-), which  prob.  derives  from  the  name  of  the  city Velur  (now  called  Belur).  Cp.  G.  Brille,  ‘spec¬ tacles’,  from  the  pi.  of  MHG.  bril,  of  s.m.,  which derives  fr.  MHG.  berille,  ‘beryl’,  fr.  L.  beryl- las  (the  first  spectacles  were  made  from  beryl). Cp.  also  brilliant,  the  first  element  in  besiclo- meter  and  the  second  element  in  chrysoberyl. beryllium,  n.,  a  metallic  element,  called  also ghteinum  ( chem .)  —  ModL.,  fr.  L.  beryllus  (see beryl);  so  called  because  it  was  first  obtained through  isolation  fr
---
axo<;),  ‘well,  spring’  Thracian Gk.  PpOxoc  (fjpouxoi;  in  Hesychius),  ppuxov.
199
‘fermented  liquor  made  from  barley,  beer’,  L. defrutum,  ‘must  boiled  down’,  fervere  or  fervere, ‘to  boil,  glow,  foam’,  Alb.  brum,  brume,  ‘leaven’, Russ,  bruja,  ‘current’,  bruit',  ‘to  stream  with force’,  OIr.  bruth,  ‘heat’,  Mir.  berbaim,  ‘I  boil,
را قرار دهند و آن به سهولت گردش می‌کند 
و معبر باد را نشان می‌دهد. پارچ؛ گوشتی که 
۳ ختنه کاه زنان می‌باشد و بریدن او سنت 
است. 

بلور: ۲ ,0:۱۳ (۱.) قسمی ششه که از 
تکیت سیلیکات دو پتاسیم و سیلیکات دو 
پلمب ساخته شود آنکینة صاف و شفاف. 
۱ ۸ (.) سفر ه 4 بزرگ. 

بلوز: 52اه" () جامةٌ نیم‌تتةٌ کرکی يا 

incoming/MON/MON_2vol_Adena_v1_djvu.txt:22691:برلیان: 0 (.) (زم.) الماس تراش 
MON_part1.txt:22691:برلیان: 0 (.) (زم.) الماس تراش
```


## [2026-10-16T05:14:03.831Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==100' KLN_1966.txt | grep -o '\\b1[67][0-9]\\b' | head; awk 'BEGIN{RS=\"\\f\"} NR==117' KLN_1966.txt | grep -o 'brilliant[^.]*' | head -3; sed -n 22688,22693p MON_part1.txt; grep -n -i 'gursag\\|gursak\\|gurs' PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt HRN.txt HUB.txt CHEUNG.txt | head -20",
 "description": "Klein page numbers, Mo'in berelyan, grep gursag"
}
```


### [2026-10-16T05:14:04.502Z] TOOL RESULT

```
166
167
brilliant,  adj
brilliant,  n
brilliant-ly,  adv
خشکک کرده» ب رگة زردالو. کشتهٌ زردالو 
که فسات کال 6 موز کف ان که و 
نو یسند. 
برلیان: 0 (.) (زم.) الماس تراش 
داده شده س تمام جهات به منظور زیبابی و 
تلاو به بیشتر و عرضهة به بازار. در تراش الماس 
PHD_mackenzie.txt:2629:gursag [gwlsk] I N gurusna !] hungry.
PHD_mackenzie.txt:6814:hollowness gabrih.                             hunger gursagih, suy, suy.
PHD_mackenzie.txt:6815:holy abezag, pak, spenag, yoJdahr;             hungry gursag, gusnag.
PHD_mackenzie.txt:10718:gursagih            AU~t'          gonag                        ,oS U·
PHD_mackenzie.txt:10719:gursag
HRN.txt:1530:(LW.), t. ängursf (26); af/. güta; wa/. yangl, minj.
HRN.txt:1559:ängurstevän.
HRN.txt:7870:907. {\)gtir8 'Hunger, gursene, gursenegt; gtcsne, n22/}^
HRN.txt:7873:phlv. gursak (AV.), gursakth (Men.), gursUan (vd.
HRN.txt:10529:Np. gurs ist unbelegt (vergl. oben No. 908).
HRN.txt:12441:gursenetß 907.
HRN.txt:20982:d, iittgurstfviht 125
NYB_vol2_glossary.txt:1742:gurisnak [gwlysnk'] hungry 92°. — Paz. abstr. gursnai, guršnaī (Mx); NP gur(z)s- nah, gura/u/snah.
NYB_vol2_glossary.txt:1743:gursakeh [gwlskyh, gwlskyh] hunger 1422. 895, 9414, — Paz. gursaa ‘hungry’ (SGV); NP gurs ‘hunger’.
NYB_vol2_glossary.txt:3980:vars [wls] hair 26°”. — Av. (1374) varasa-; Paz. vars (SGV); Arm. lw. vars-k* (pl.); NP gurs ‘curled hair’.
NYB_vol2_glossary.txt:6623:gursaa: gursakéh
NYB_vol2_glossary.txt:6624:gursnai
NYB_vol2_glossary.txt:6625:gursnai
NYB_vol2_glossary.txt:7177:gurs: gursakéh
NYB_vol2_glossary.txt:7178:gurs: vars
```


## [2026-10-16T05:14:07.450Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 7866,7885p HRN.txt; grep -n -i 'gurs\\|907' HUB.txt | head -20; grep -n -i 'hunger\\|gurs' CHEUNG.txt | head; grep -n -i 'v[r]s\\|varš\\|vərš\\|hunger' KNT_full.txt | head",
 "description": "Read Horn 907 and grep Hübschmann, Cheung, Kent"
}
```


### [2026-10-16T05:14:07.804Z] TOOL RESULT

```
V
aw. garö demmia-^ garö nmäna- (S alemann, SF,
pag. 99»; dann auch Fr. Müller, WZKM. 5, 187, der
arm. LW. gerezman 'Grab' Gruft, Friedhof dazu stellt).
907. {\)gtir8 'Hunger, gursene, gursenegt; gtcsne, n22/}^
(Js. 8, 4), ^r:i'^i: (Js. 5, 13).
g. vasne, vasnegi; Kä§. ves, vesd, vesS, vesegl.
phlv. gursak (AV.), gursakth (Men.), gursUan (vd.
9 (132) GL); kurd. vürsl, vürsigt, vdsa (H.-Sch.).
LW. bei. gusnag, n. gumag (120); siyn. gusna.
Wegen g. vasne etc. muss der Anlaut ursprüng-
lich ein V gewesen sein, also ist bei. gusnag entlehnt.
908. {2)gur8 Xockenhaar (unbelegt).
aw. varesa- 'Haar; phlv. vars, arm. LW. vars;
ksl. vlasu,
909. yiriften 'ergreifen*, Praes. glr-etn,
g. gereftmün,
ap. [/^grab-, agarbayam ergreifen'; aw. [/^grab-,
gerewnäiti; phlv. graftan; ai. l^grabh^, gfbhndti,
kurd. girtin 'ergreifen ; bei. girag , n. giray (106);
182:ruk; gurSy Tlucht' neben gurextan^ Wrzl. rik. Die
3260:907. Die Nebenform gusna *hungrig' ist durch Anlehnung
3266:gurs, besser gars im alteren Neupersisch vorhanden
5053:veretka-f choras. kurd. bulk ZDMG. 38, 53; gurs^) 'Hunger',
5054:gursina 'hungrig aus "^vrsa-, *vrsna-; gurg *Wolf = zd.
5063:') Ueber gurs *Lockenhaar* (fiir gars) s. oben p. 92.- 145 —
5157:gursa 'hungry', gursnai 'hunger , gurda 'kidney* — dil 'heart',
5180:p. 275, gursakih 'hunger p. 275, guSn *a male' p. 280,
5505:zd. veredka-^ veretka-; gurs 'Hunger*, gursina^ gusna, gusna
5506:'hungrig', paz. gursnal 'Hunger Min. Gl. 94, phi. gursak
5508:vgl. Horn Nr. 907, dazu afgh. vaMi'hungrig, also gurs =
5537:gurs Xocken' (unbelegt), besser gars = phi. gars, vars, zd.
5677:zd. hqmvareti'\ 13) gursak 'hungrig Gl. and Ind. 275 = ap.
5694:gumdn, gumext, gurbak (?), gurt, gursak, gurg, gurtak, gusn,
5699:vf {gurt, gursak, gurg^), gurtak, gusn), danach in der An-
5717:gurda, giirg, gursa, guman, gumexta, gumardan Shk. 246—
7581:zd. varesa-; Pctrs =^ ap. Pdrsa-; gurs ^Hunger, gursina
7813:‘hunger’ 
12440:möwzi, Sariq. morz ‘hunger’, Wa. mərz ‘hungry’ || (+ *uz-) ? Pash. ‘“zmogalay 
27412:*MIDDLE PERSIAN: ? MMP gwrsgyh ‘hunger’? > DMMPP: 167b 
27414:*PARTHIAN: wsynd, wsyynd ‘hungry; hunger > DMMPP: 348a 
27420:*CHORESMIAN: m[w$y- ‘to be(come) hungry’, ’wsyk ‘hunger’ (477.5), ’wsynd 
27428:wusi(y)aday ‘hungry’, Yi. wúšřyo ‘hunger, hungry’ 
30704:*CHORESMIAN: (+ *upa-) ? b’Z’w- ‘he writhed with hunger [= Arab. ç ,>Jl s sl ?, 
30705:‘he cried out of hunger [= Pers. SS 5I 2 15] ?’. © Samadi compares the Chor. 
14218:1The only exception is A'Hc 14f Vrslaspahyá пата 
24689:lar, Gk. Kva£ápys. From u- ‘good’ + varštra- 
29078:this ptc. would be OP *vrsasta- or the equivalent
```


## [2026-10-16T05:14:10.051Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 27395,27432p CHEUNG.txt; sed -n 3258,3268p HUB.txt; sed -n 5050,5056p HUB.txt; head -n 3260 HUB.txt | tr -cd '\\f' | wc -c",
 "description": "Read Cheung entry and Hübschmann on gurs"
}
```


### [2026-10-16T05:14:10.402Z] TOOL RESULT

```
*NWIR: Abz. varz ‘fertiliser, dung’ || (+ *pari-) NP parvardan/parvar- ‘to nourish, 
feed’, parvardegar ‘Creator, Provider’ 

*NEIR: Oss. I. warzyn/warzt, D. warzun/warzt ‘to love’ (< *‘to take care of, foster’) 
*SANSKRIT: ürj- (f.) ‘nourishment, refreshment, strength” > EWAia I: 242 f. 

«PIE *uerH)g- ‘to be filled, nourished, brimming with life (energy)’. > A laryngeal is 
reconstructed on account of the long vowel in Skt. ürj-. => LIV: — | Pok.: 1169 

*IE COGNATES: Hitt. /uarkant-/ ‘fat, fattened’, Gr. opge ‘I am getting ready to bear, 
growing ripe; I swell with lust’, оруй ‘natural impulse, temperament, disposition’ 
*REFERENCES: Henning 1965: 176, fn. 38; Abaev, Slovar’ IV: 53 f.; Lecoq 2002: 604a; NEVP: 92 


*yarS ‘to be hungry’ 

*MIDDLE PERSIAN: ? MMP gwrsgyh ‘hunger’? > DMMPP: 167b 

*PARTHIAN: wsynd, wsyynd ‘hungry; hunger > DMMPP: 348a 

*SOGDIAN: BSogd. ws’y-, CSogd. wš- ‘to be hungry’ 

Pres.: IND. 3sg. BSogd. ws’yt (SCE 29) 

*CHORESMIAN: m[w$y- ‘to be(come) hungry’, ’wsyk ‘hunger’ (477.5), ’wsynd 
‘hungry’ (412.7) = Samadi: 222 f. 

*NWIR: NP gusnah, Bal. gusnag (< NP), Gz. vässe, vesse, visse, Jow. vefa ‘hungry’, 
Abyan. vasa, Abz. veša, Anar. vase, Ard. veSe, Nn. vassa, Qohr. veša ‘who is 
hungry’ 

*NEIR: М. (w)usay-/(w)usyad- ‘to become hungry’ (Zarubin), Pash. wogay, Yi. 
wusi(y)aday ‘hungry’, Yi. wúšřyo ‘hunger, hungry’ 

*MISC: Par. yurcá ‘hungry’ 

© The root *uars/S- appears to be a kind of "Reimbildung" after *tar$ ‘to be thirsty’ 
gerezman 'Grab* nichts zu thun. Vgl. Fr. Muller,
WZKM. 5, 187.
907. Die Nebenform gusna *hungrig' ist durch Anlehnung
an tisna 'durstig entstanden, wie afgh. va^ai 'hungrig'
von ta^ai *durstig' beeinflusst ist. Fiir das Altpers.
ist *vrsa^y *vrsna- anzusetzen.
908. Die Nummer will Horn streiehen (Einleitung p. IX,
Anm.), wohl weil np. guvs unsicher ist. Doch muss
gurs, besser gars im alteren Neupersisch vorhanden
gewesen sein, da die jiingere Form gars auch im Phi.
(vgl. Horn p. 278 Nr. 90) neben alterem phi. paz. vars
dazu auch np. slmury *Vogel Greif = zd. sa^no -\- mereyo ;
mw/'Wein, skr. wrdv«A^*Weintraube'; grwrd 'Held' aus */;rto-,
\^. zi. hqmvareti' *Tapferkeit* ; gurda Niere' = zd. t?«r«<)A;flf-,
veretka-f choras. kurd. bulk ZDMG. 38, 53; gurs^) 'Hunger',
gursina 'hungrig aus "^vrsa-, *vrsna-; gurg *Wolf = zd.
vehrka^; Gurgdn *ein Land' = zd. vehrkdna-, ap. vrkCLna-;
*) Np. mu§tan ist der regelreohte Infinitiv zum Praesens m&lam^
102
```


## [2026-10-16T05:14:15.555Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'hungry\\|hunger' SOD_pages.txt | head -20",
 "description": "Grep hunger in Sogdian dictionary"
}
```


### [2026-10-16T05:14:15.973Z] TOOL RESULT

```
5589:     hunger
5598:    died of hunger
8976:       ^'sy', sy>                                                    star vedihunger -dead)
9537:     hungry                              =»ws>y-, ws'nt'y
13798:      TSP 2.259, 324, 730, 3.16; W-Li, ii; BBB                       hunger                                        =>>SPz>
13807:        3.256; Hen. Cosm. 312, 121; C2, 25R 16                      died of hunger
23881:                                                                           hungry ghost
30803:                                                                              hungry ?
33277:      hungry
33294:                                                                           hungryM                                      a^J
33303:      (to)be hungry                                                          7l3n 5
37702:beard   8657                           (to )be confused  360                   (to)bt hungry   10218
38057:descendent      4977, 9568             died of hunger      640, 3525             disintegration 8254
38578:    hunger       639, 3523                     illicit 1260, 6770
38579:i   hunger-dead     1810                       illness 230, 1068, 1320, 1661,
38584:    hungry   2001, 9391, 10213, 10228,            1678, 3946, 4527, 4816, 7178,         incense   2878, 2890
38586:    hungry ghost       7029                      9347, 10713, 10717                     incited   1189
```


## [2026-10-16T05:14:18.351Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for ln in 9537 33277 33303; do echo \"== $ln leaf $(head -n $ln SOD_pages.txt | tr -cd '\\f' | wc -c)\"; sed -n \"$((ln-8)),$((ln+6))p\" SOD_pages.txt; done",
 "description": "Read Sogdian hungry entries with leaf numbers"
}
```


### [2026-10-16T05:14:18.786Z] TOOL RESULT

```
== 9537 leaf 144
                                                                                                                      -J<jL
      STii 3.36; Benv. Notesiii 223; Mack. BSOAS                            Sund. AoFi 244; STi 53.3; S W, C2, 17V5; inf.
         1970, 116; S W, BSOAS 1981, 236; }wsq>r                              Vft, C2, 31V21
         cmqy\ STii p577                                              2011 >wsty- =» >wst»y-
2000 Svsqyrd             C =» wysqyrd-                                2012 >wsty>mnty C
2001 >wsnty C                                         (^if)w/               ostay-amande
                                                                            standing            -^wst'mntyy
     usande ©<*vrs+andaka
     hungry                              =»ws>y-, ws'nt'y
                                                                            GMS 558; C2, 61V19
      STi 24.6, 27.8 & etc.; GMS 10, 1068
                                                                     2013 Nvstyt =* 'wst'y-
                                                                     2014 'wstyty C
2002 'wst-1          ^->)(uJLi <u->_y 'j^ J»* ^f)^h^€      to&~>\
                                                                           standing
== 33277 leaf 481
         piece                                                              SCE 247; GMS 218; Gersh. Sogd. Cpds. 152n;
         wsw, TSP 3.66; }yw wsyy "alone" GMS 1317;
           Sogdica. 24.9; GMS 299                                             S W, C2 p7422
                                                                     10223 wsk^rt'y B                         (^j^f^)^
10213 ws'n^y S                               ^/
                                                                           wiskerte =»wysqyr-, wysk'yr^y
      wisande, usande (ws'nty) ©pi. -t ^wsnty,
        wsn, wswq                                                          open(<?/ eyes)
      hungry
                                                                            BSTBL, Dhy. 33, 102; GMS 219
         Frag. 18.3 apud. S W, IIJ 1976, 63; GMS 210,                10224 wskpn =» wskwpn
           1068
                                                                     10225 wskwpn B                      0jl5 <l5&l>- ij^ j
10214 ws'nty =$ ws'nt'y                                                    w(i)skupan, uskupan ? (wskpn) ©wsk-
                                                                             <*huska ©ace. -nw =»sqwpn
== 33303 leaf 481
         wisus, wsus, usus ? (wsws) ©pi. -yf =#*ws-                        w(i)san, usan, wisn ? ^ws'y-, ws'n^y
         individually ?
         BSTBL, Dhu. 22; Gersh. Sogd. Cpds. 143.4,                         GMS 386
           145.2; Sogdica. 25n9
                                                                     10229 wsn- B                                    jiS \j
10218 ws'y- B, C                                  Crj*-*/                  wasn,w(i)sn ©Av. vardsna% Skt. vrsan
      wsay, us(ay) ? (ws-) ©<*wrs-          =»wswq,                        male
        ws'nt'y, wsn-, >wsnty                                              GMS 147; TSP 19.2a, wsny 'spy, Hen. Texts.
      (to)be hungry                                                          7l3n 5
      SCE 29; wpyt, 3sg. pres. BSTi 65
                                                                     10230 wsn'm M                          J^y,-.,...*,
10219 wsyn     M         (^j^yl*     Jk^ J J^-fi)^.                        wisnam, usnam ©*wi-sndma-, Arm. osnan
415                                                                                                                  wx'scn
                                                         x,^
                                                                10243 wswsyt S                                       OjSV
```


## [2026-10-16T05:14:23.801Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:1794 --image 2>&1 | tail -60",
 "description": "Fetch Borhan page 1794 OCR and image"
}
```


### [2026-10-16T05:14:31.956Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 589; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1794.png
REF: BQT:1794  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 589  OCR-lang: fas

کردن نهادن : اهنجمنه
گردن نهادن - کدایه از فروتنی - و بالش کرد را نیز گفته‌اند - و بمعنی همه
کردن - وفرمانبرداری‌واطاعت نمودن (۱)نمودن | ومجموع هم هست- ویمعتی نگاه نیز (۲) آهده
باغد ‎٩‏ . رز امت - و بفتح اول ۸ خاکهٌ نقاشان باشد وآن
گرد نی کردن > کنانه از سر کی زغال سوده اس ت که در پارچه معه‌اند و برکاغد
ونافرمانی کردن باشد . های سوزن زده طراحی کرده مالند یا از آن‌طرح
گردو ۳ بکر اول وتات بواو و نقش بجای دیگر نشیند - وآن‌کاغذ سوزن‌زده
کشیده , کردکان را گوبند .9# را نی ز کوبند ‎٩‏ .
گردون سرشت - کندایه از مردم گرده آ الق - بنم اول . بمعنی آلو
صاحب عجب و تکبر و با وقار و تمکین و کاهل | کرد باشد » وآن میوه‌است شبیه پزردآ لو .
وتاموافق باشد ۴ گرده‌ بات - بابای‌ابجد بروزن‌اسفهان.
گردون مینا < کنابه از آسان بمعنی‌نگاهبان‌باشد چه گرده بمعنی‌نگاه هم‌آمده
: گرده پکسر اد رد کح نا ً کردم چرخ - کناها زآتاب‌است-
نوعی از بان غیر تنك باشد 6 - و «رچیز مدور
و گرد راگویند عموماً - وپارچهٌ زرد.مدوریرا که وماه را نیز کویند .
ازملمانان خصوصاً وآنرا بعربی‌غیار٩؟‏ خوانند ۷ | است که کنایه ازآفتاب وماء باشد .4

(۱) چش: - واطاعت. (۷) خم۱ :۳+ بنظر -

۱ -رك : رشیدی - وحاضر شدن برای کشته شدن «* فرهنگه نظام > -

۴ - از :کرد ( بکسر )+ و ( پسوند تصفیر , سازندة اسم از صفت ) » رك: کردکان .
درختی است ( 1181288 ) از دسَهٌ غان‌ها » باجوب محکم وبرگهای مرک ب که مغز آن روغن
بیاردارد. «کل کلاب ص ۲۷۸ 4 ۴ -رك : رشیدی . ۴ - از: گرد (بکر)+
شود . پهلوی 81718۷ * » ارمنی 871216 » معرب جردقه « هوبشمان ۹*۹ ۰

۹ - رك : غیار .

۷ -کرده پبردوش راهب دیرم حلقه درکوش ناجد لاتم . نزاری فهستانی «رشیدی»-

۸ - از :کرد ( بفتح )۰ ( دبت ) . ‎٩‏ - بم اول . بمعنی‌کلیه (ع) امت.
اوستا - ۷۵۲۵۵۵ ۰ -۷6۲۵1۵8 (کلیتین) » پپلوی 8۳1816 » هندی - پرا کربت -۷۲4
(کلیه) . کردی 870216 ۰ بلوچی 81111810 . وخی ]۷۵ ۶ اسشق ۹*۵ .

گردون - بفتح اول . از: کرد (کردیدن)+-ون ( پسوند فاعلی ) ۳ کردان.یپلوی
0 . 382۳1۵0 با 0۷27108 3۷27108 ۶ هوبشمان ۹*۶ ۰ ورك : اسشق ۹*۶ .
گردنده » چرخ - ارابه » کالسکه - آسمان , فلك . ۱

۲ گردیدن - بفتح اول و پنجم < گشتن . پپلوی 827111827 « بندهشنه۹ زو ها
00 اوستا - ۶۷2۳61 بارتولمه ۱۳۹۸ * » هندی‌باستان ۷2۳1216 « نیب رکه ص۲۳۹
نیز هندی باستان ۷8۳ [ گردیدن ۰ چرخیدن | ) « اسفا ۱: ۲ ص 6۹۹ کردی [ا ت۰1
( کرش کردن » گردیدن ) « ژابا ص ۳۹۱ ؛ دور زدن » چرخیدن - شدن ,گشتن - برکشتن,
تغبی رکردن - سرنگون شدن - سیر کردن »کردش کردن .
```


## [2026-10-16T05:14:34.812Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 592 593 594; do python3 tools/ref_page.py BQT:1794 --pdf-page $p --image 2>&1 | grep -n 'IMAGE\\|گرس\\|گرسنه\\|گشنه' | head -8; echo ----; done",
 "description": "Search nearby Borhan pages for gors entry"
}
```


### [2026-10-16T05:14:35.566Z] TOOL RESULT

```
1:IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1794.png
----
1:IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1794.png
----
1:IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1794.png
----
```


## [2026-10-16T05:14:38.803Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; grep -n 'گرسن\\|گرس \\|گرس-\\|گرس ۱\\|گرسنگی' BQT_v3_pages.txt | head -20; grep -n '\\[pdf page 59[0-9]\\]' BQT_v3_pages.txt",
 "description": "Grep gors in Borhan vol 3 OCR text"
}
```


### [2026-10-16T05:14:39.159Z] TOOL RESULT

```
6377:‏وشمانید. ‎pales‏ ازتعنگی ودمادم از گرسنگی؛ وغربووغرنگ»وغرن» «لفت‌فرس*#۱۲ومرادآ ست که
10027:۵ - ضرم ‎ci)‏ اول و دوم) (عر) سخت گرسنه گردیدن « تاج
18380:‏گرسنافه - بک اول و قح ‎pl‏ که
34644:‏۵ خشکا رگرسنه راکللبه است
43320:‏گرس . ‎em‏ اول و سکون ‎gt‏ وسین
43351:‎٩‏ هه کوری , رگ : گرسنه » کشنه » کاشانی
43355:پارسی باستان - 0۷۳58, 0۷۲5۵2«هویشمان ‎٩۰۷‏ > رك : «گرسنه » (هم.) ورك : رشیدی و
43381:گرسنه چشم - بت ول تا ناه
43386:گرسنه چشمان کنعان - کنایه
43429:‏ب سگرسنه خفت وکس ندانت که کیست بس جان بلب آمدکه بروکس نگرست.
43501:‎SS‏ جاب‌آن ده ‎1G‏ نکند وا گرس رک رکه
43528:وانان نیز بهتگام گرسنگی حمله ميکند.
43547:علف نخورد هرچند کرسنه باشد وا گرس کین اورا
45146:‏مخقف گرسنگی بود .
47993:۱ کری (هم) و رك : گرسنه .
43223:[pdf page 590]
43276:[pdf page 591]
43362:[pdf page 592]
43432:[pdf page 593]
43484:[pdf page 594]
43551:[pdf page 595]
43640:[pdf page 596]
43702:[pdf page 597]
43778:[pdf page 598]
43874:[pdf page 599]
```


## [2026-10-16T05:14:41.510Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT; sed -n 43276,43290p BQT_v3_pages.txt; echo ...; sed -n 43315,43361p BQT_v3_pages.txt; sed -n 43362,43395p BQT_v3_pages.txt",
 "description": "Read Borhan pdf page 591-592 OCR"
}
```


### [2026-10-16T05:14:41.916Z] TOOL RESULT

```
[pdf page 591]
گرزه
و پیمانه بز رکه را گونند ۱

‎OIF‏ © بنتح اول بروزن هرزه »لوعی
ازمار استء وبعض یکوبند ماری باشد سر بز رکه
و پر خط وخال وزهر او ‎asks‏ از مارهای ‎Kee‏
‏است وهیج ترباقی برزهر او مقاومت نکند ۴ -
ودر بعضی از ولایت دارالمرز ۴ موش راکرزء ۴
‎any‏ - و بضم اول. هم یمعنی اولوهم‌بمعنی
کرز باشدکه عربان‌عمود کویند ۵ .

‏گرد گاو پیکر ۷ » ‎oma‏
‏راگوبند چه آنرا بپیأت سر کاومیش از فولاد
ساخته ‎Woy‏ .
...
تاج کیانیرا گوبند و آنرا مرصع ساخته از بالای
تخت محازی‌سرایشان باز اجیر طلاآ ویشته‌بوده‌اند
- ویمعتی زبیل ‎col le‏ - و ‎ps‏ پیکان‌دار
را 5 گفته‌الد ۱

‏گرس . ‎em‏ اول و سکون ‎gt‏ وسین
بی‌نقطه » کرسنگی راکویند که در مقابل سپری
است ‎٩‏ - و ‎gine‏ چرك وزیم جامه و بدن هم
آمده است - وموی پیچیده وموی پیچه را لیز

‏کفته‌اند که موباف زان باشد ‎NO‏

‏۱ -قی :کرزن « دزی ج ۲ ص ‎boo‏ ۰۰ ورگ : هرمزدنامه ص ۸-۳۰۷ ۶ نیم‌تاجی
بود از دیبا بافند بزرو ‎pS‏ مفرق کرده » و کوبند ناجی بود ‎Sg‏ وزین پرجواهر ومئوك ‎PB‏

‏تخت ‎gating Lb,‏ . بوسف عروضی گوید :

‏ار عیر بیکوان جهانت و یکوبی

‏۴ - بدی مار کرزه است » از او دورباش

‏۴ مراد گیلان است.
‎Coa) in ®‏
رك : کرزدن » ۸ - ره :038 .

‏تاجت وسال وماه مر اورا چ وکرزنت .»

‏« لت فری ۰۳0۹ .
که بد بدتر از مار گرزه کزد .
« ناصرخرو بلخی . دبوان ص ۱۱۲ *.

‏۴ - درلاهیجان وحوالی ‎OT‏ 88628 (موش) «میررفتی»

‎. Kas: ‏رك‎ ۱

‏۷ - مسحف «گزربدن »< گزردن
‎٩‏ هه کوری , رگ : گرسنه » کشنه » کاشانی

‎.veshegi , ۷۵۵۳۵ . ۷6:۵۵ .vesh‏ پهلری ‎gursitan .gursakib .gursak‏ ؛ کردی
‎vursigt . vurst‏ . ۷۵52 بلوچی ‎gushnage‏ تننی ‎gushna‏ > استق ۹۰۷ ۰ ۰ شکل
پارسی باستان - 0۷۳58, 0۷۲5۵2«هویشمان ‎٩۰۷‏ > رك : «گرسنه » (هم.) ورك : رشیدی و
فرهنگه نظام . جهانگیری و فرهنگه نظام این بست شاهد آورده‌اند :
کر ازدلم برد نم زلف وخال ‎cays‏ جان باخیال رشته فتاد ازخیال‌دوست. بسحاق اطعمه,
اما در دیوان بحاق چاپ قطنطنیه ص ۳۸ بجای کرس > جوع © وبجای خیال اول در مصراع
دوم > حبال » آمده است . ۰ ر : اسشق - هوبشمان ‎٩۰۸‏ .

‏(برهان فاطهه۴۳)
[pdf page 592]
۱۷۹7

گرست « بفتح اول و ابی و سکون
ثالث و ‎sigh‏ بمعنی سیاه همست باشد وبعریی
طافع گویند ۱ - و بزبان علمی هند فرو بردن
لقمه و امثال ‎OT‏ باشد و عربان ‎ab‏ خوانند.

گرسقن ۴ - بکر اول وانی :مخف
کربستن است که کربه کردن باشد .

گر ستودن ۴ بفتح‌اول وئالی‌بروزن
تیغرودن » بمعنی ‎OS‏ است وآن ترازو مانندی
است که بستها و تنگهای ‎gh‏ را بدان سنجند .

گرستون ۴ © بفتح اول وئالی بروزن
شف ق کون + بمعت ی گرستودن است که ‎methods‏
‏وبه‌عنی کیل ‎Ulan‏ بزر که همآمده است‌ومعرب

گرسنه چشم - بت ول تا ناه
از ‎Ste‏ و ممسك ‎ath‏ - و مردم ‎ad‏ وکدا را
‎e‏ میگویند ۵ - وکنابه از مردمی‌هم هست که
از قحط وغلا برآمده پاشتد .

گرسنه چشمان کنعان - کنایه
از برادران ‎Gey‏ علیه‌اللام است .

گرسیان - با بای ونون وحرکت
غیرمملوم « نوعی‌ازسنگه باشد ‎OT;‏ درهتدوستان
‎re‏ میرسد ودر صثمت کیمیا ‎ale‏ 1

‎Sg F‏ = بتادرستا مود
بروزن بخنی‌پز » نام برادر افراسیاب است ؛ وبا
کاف تازی هم بنظ رآمده است .
```


## [2026-10-16T05:14:47.431Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls -la data/verification/sources/refs/ocr/BQT/ | grep 179; python3 tools/ref_page.py BQT:1796 --pdf-page 591 --image 2>&1 | head -3",
 "description": "Cache Borhan printed page 1796 image"
}
```


### [2026-10-16T05:14:55.279Z] TOOL RESULT

```
.rw-r--r--  179k sfmqrb 14 Oct 22:19  1499.png
.rw-r--r--  433k sfmqrb 16 Oct 01:14  1794.png
.rw-r--r--  3.8k sfmqrb 16 Oct 01:14  1794.txt
.rw-r--r--  431k sfmqrb 14 Oct 22:19  1795.png
.rw-r--r--  4.0k sfmqrb 14 Oct 22:19  1795.txt
.rw-r--r--  179k sfmqrb 14 Oct 22:19  2396.png
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1796.png
REF: BQT:1796  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 591  OCR-lang: fas
```


## [2026-10-16T05:15:02.692Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^گرس\\|^گرسنه\\|^بلور\\|^تبلور\\|^متبلور' MON_part1.txt MON_part2.txt | head; grep -n 'گرسنه\\|گرس ' incoming/ARY/ARY_pages.txt | head -5; grep -n -i 'GORESNE\\|GOROSNE\\|GORS\\b\\|BOLUR\\|BOLOUR' incoming/ARY/ARY_latin_index_pages.txt | head",
 "description": "Grep Mo'in and Aryanpur for gorosneh, bolur"
}
```


### [2026-10-16T05:15:03.033Z] TOOL RESULT

```
MON_part2.txt:8804:بلورین با ۳ آن چای یا قهوه 
MON_part2.txt:18844:بلورها کمی مشکل است ولی به سهولت 
MON_part2.txt:18853:بلورهایش در سطح آب قرار می‌گیرد و 
MON_part2.txt:21312:متبلور می‌شود و در آب کاملاً محلول است 
MON_part2.txt:29386:بلورهایش بیتر شکل ۸ وجهی را دارند. در 
MON_part2.txt:29974:تبلورش را از دست بدهد و بصورت گچ 
MON_part2.txt:31398:گرسنه چشم: 6(0)-.بو (ص‌مر.) ( کد.) 
MON_part2.txt:32932:گرسنه» ج گشنگان. 
MON_part2.txt:34735:بلورهایش به شکل قلم مو یا دسته جارو 
MON_part2.txt:38578:گرسنگی. لباس راهب: (کد.) جامهٌ سیاه (چه 
695:از میلاد در سرزمین‌های شمال کوه‌های زاگرس نشیمند شده بودند. گیرشمن (078877۸/1۸37 .) و
12744:1/۳۰ گرسنه گشنه» گرسنگی» گشنگی
12495:GOROSNE, GOSHNE, GOROSNEGI, GOSHNEGI
```


## [2026-10-16T05:15:05.374Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 12735,12760p incoming/ARY/ARY_pages.txt; grep -n '\\[pdf page' incoming/ARY/ARY_pages.txt | awk -F: '$1<12744' | tail -1; sed -n 31390,31400p MON_part2.txt",
 "description": "Read Aryanpur gorosne entry and Mo'in nearby"
}
```


### [2026-10-16T05:15:05.713Z] TOOL RESULT

```
انگلیسی کهن (تلکلا8(/0 ۰:02 ۷1.011 برهان قاطع : ۱۷۹۴
اسلاوی کهن (۲16اهاة #04( صا0): لغث‌نامه دهخدا: ۱۹۸۲
۷۸۲۵۲۰ ,۷۸۷۵ فرهنگ معین : ۳۳۵۸
یادداشت:
اوه بازگت به: ویر
۲ چم این وُژه در دْقزیان‌های این فهرست: نخ پشمی» ریسمان (از الیاف گیاهی).
۳ واژه‌های انگلیسی .۷001 و آلمانی ۷۷0178 و سانسکریت 18۸1۸ (همه به چم "پشم!) نیز از همین
واجربشه‌اند (1139 :۳۵101۹/۷۷)
[pdf page 429]
1/۳۰ گرسنه گشنه» گرسنگی» گشنگی
۱ فارسی (88514(0: گرسته, گشنه, گرسنگی, گشنگی
1 603082807 ,00510 رد0020
ا
پارسی باستان (28781۸4 صان): سوئدی (5[78:01317): ان ۱۱ شش
۸ ۹۷5۸ نروژی (07فا07۳۶0/): 1
پهلوی (۱/مااقمه): هلندی (بلع07): " دی
06 6188۸67 ,خاهقانان اسلاوی کهن (ع7/اماد نات صاه).
کردی (4)(801520). اد لونی ری تآهساه
بلوچی (/8۸007): 6۸6 لهستانی (0۵1/58: 01007 ,ماه
اففانی (پشتو) (/4701۸7): روسی (لفا55ن): 60100۲۷ ,01۵02
: ۸ ,1۸5۲۸ چکه 28071 5 ,فآ
سانسکریت (5۸5777): ان ان صربی (/ل4ا5888): شاه ,تشاج
که ,تکفا ,13013۸7 برهمی (/ل80/751114): 00۷5شآ1 ,0ش ]11
یونانی (0828۴): ۰ ۳8016818 ,۵۲7 اسلوا کی (51014): 3۲5هن11 رتش
گریک (00771): نراد ان لیترانی (/لغاللفتا 77 :هاش ,13113
ایسلندی کهن ((0۸۷۸ا0یی5 صزه): َ
12743:[pdf page 429]
موی مجعد. موی‌باف زنان؛ موی پیچه. 
گسرسنگی: آ-(۵-) 130۲۵۵۵ (حاأمص.) 
گر سنه بو دن» احتیاح به خوردن داشتن؛ 
سیگ 

گر سثه (ع)هم ب(30۲۵۵0۸)6 [- کسنه 
< کشنه] (ص.) آنکه احساس احتیاج به 
خوردن عد| کند) جایع؛ ج. گرسنگان. 
گرسنه چشم: 6(0)-.بو (ص‌مر.) ( کد.) 
حریص» آزمند. (کد.) بخیل» ممسککك. ( کذ.) 
کداء فقبر . گس سثه چشمان کنعان: ( کن.)
```


## [2026-10-16T05:15:10.583Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | grep -v '^import'",
 "description": "Read fetch_source.py usage"
}
```


### [2026-10-16T05:15:11.150Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
"""

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "data", "verification", "sources", "web")
INDEX = os.path.join(WEB, "index.jsonl")
UA = "rishe-verification/1.0 (+https://github.com/sfmqrb/rishe; etymology source archiving)"


def html_to_text(s):
    s = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>|</tr>|</h[1-6]>", "\n", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    return s.strip()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    note = ""
    if "--note" in sys.argv:
        note = sys.argv[sys.argv.index("--note") + 1]
        args = [a for a in args if a != note]
    if not args:
        print(__doc__); return 2
    url = args[0]
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]
    # IRI -> URI: percent-encode non-ASCII path/query characters so urllib accepts them
    parts = urllib.parse.urlsplit(url)
```


## [2026-10-16T05:15:15.158Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F=tools/fetch_source.py; for u in 'https://en.wiktionary.org/wiki/beryl' 'https://en.wiktionary.org/wiki/βήρυλλος' 'https://en.wiktionary.org/wiki/بلور' 'https://en.wiktionary.org/wiki/برلیان' 'https://en.wiktionary.org/wiki/گرسنه' 'https://en.wiktionary.org/wiki/brilliant' 'https://en.wiktionary.org/wiki/briller' 'https://en.wiktionary.org/wiki/beryllium' 'https://www.etymonline.com/word/beryl' 'https://www.etymonline.com/word/brilliant' 'https://en.wiktionary.org/wiki/वैडूर्य' 'https://en.wiktionary.org/wiki/beryllus' 'https://en.wiktionary.org/wiki/گرس'; do python3 $F \"$u\" --note \"page 524, root Velur/Vrsa\" 2>&1 | tail -1; done",
 "description": "Fetch and archive web sources",
 "timeout": 300000
}
```


### [2026-10-16T05:15:21.070Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/52dfc1a2527c6a2c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/75e90ed2cc6689c6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/cd40e1f887231397.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d29e7b21487a492b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/488202d7845f14fa.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2a5914d0424ad150.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/37e727ed4792981d.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/22ec466211a97720.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f77c408569c8a875.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1cc80a3bd71c8bcc.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/975a15ed4554a3cd.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a9c2a01a4884718f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/049e3975f1470529.txt
```


## [2026-10-16T05:15:24.145Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 52dfc1a2527c6a2c 75e90ed2cc6689c6 cd40e1f887231397 d29e7b21487a492b 488202d7845f14fa 37e727ed4792981d 975a15ed4554a3cd 049e3975f1470529 f77c408569c8a875 1cc80a3bd71c8bcc; do echo \"=== $f $(wc -c <$f.txt)\"; grep -i -A6 '^Etymology' $f.txt | head -14; done",
 "description": "Extract etymology sections from fetched pages"
}
```


### [2026-10-16T05:15:24.680Z] TOOL RESULT

```
=== 52dfc1a2527c6a2c 22829
=== 75e90ed2cc6689c6 9870
=== cd40e1f887231397 19109
=== d29e7b21487a492b 138
=== 488202d7845f14fa 4490
=== 37e727ed4792981d 10158
=== 975a15ed4554a3cd 9739
=== 049e3975f1470529 3454
=== f77c408569c8a875 132
=== 1cc80a3bd71c8bcc 136
```


## [2026-10-16T05:15:28.482Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -i -m3 -A3 'etymology' 52dfc1a2527c6a2c.txt | head -20; echo ==; grep -i -m2 -A4 'etymology' 75e90ed2cc6689c6.txt|head; echo ==; grep -i -A5 'etymology' cd40e1f887231397.txt | head -30; echo ==; cat d29e7b21487a492b.txt f77c408569c8a875.txt; echo ==; grep -i -A5 'etymology' 488202d7845f14fa.txt | head; echo ==; grep -i -A4 'etymology' 37e727ed4792981d.txt | head; echo ==;  grep -i -A5 'etymology' 975a15ed4554a3cd.txt | head; echo ==; grep -i -A5 'etymology' 049e3975f1470529.txt | head",
 "description": "Show etymology text from pages"
}
```


### [2026-10-16T05:15:28.847Z] TOOL RESULT

```
Exit code 1
 Etymology 

 1.2 
 Pronunciation 
--
 Etymology 

 6.3 
 Pronunciation 
--
 Etymology 

 7.2 
 Pronunciation 
(eval):1: = not found
```


## [2026-10-16T05:15:31.557Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 52dfc1a2527c6a2c 75e90ed2cc6689c6 cd40e1f887231397 488202d7845f14fa 37e727ed4792981d 975a15ed4554a3cd 049e3975f1470529; do echo \"######## $f\"; grep -n -i 'from \\|borrowed\\|inherited' $f.txt | head -12; done; head -c 300 d29e7b21487a492b.txt; head -c 300 f77c408569c8a875.txt",
 "description": "Show derivation lines from pages"
}
```


### [2026-10-16T05:15:31.930Z] TOOL RESULT

```
######## 52dfc1a2527c6a2c
339: From Wiktionary, the free dictionary
378: Inherited from Middle English beryl , from Old French beril , from Latin bērillus , bēryllus , from Ancient Greek βήρυλλος ( bḗrullos , “ beryl ” ) , in turn borrowed from Middle Indic forms like Pali veḷuriya or Prakrit 𑀯𑁂𑀭𑀼𑀮𑀺𑀅 ( verulia ) , from Dravidian , probably named after Velur (modern day Belur ) in southern India. [ 1 ] 
397: 2012 March, Lee A. Groat, “Gemstones”, in American Scientist ‎ [2] , volume 100 , number 2, archived from the original on 14 June 2012 , page 128 : Although there are dozens of different types of gems, among the best known and most important are diamond, ruby and sapphire, emerald and other gem forms of the mineral beryl , chrysoberyl, tanzanite, tsavorite, topaz and jade. 
406: 1922 , E[ric] R[ücker] Eddison , The Worm Ouroboros: A Romance , London: Jonathan Cape   [ … ] , →OCLC , page 5 : His buskins were laced with gold, and from his belt hung a sword, narrow of blade and keen, the hilt rough with beryls and black diamonds. 
841: Borrowed from Old French beril , from Latin bērillus , bēryllus ( “ beryl ” ) , from Ancient Greek βήρυλλος ( bḗrullos ) .
873: Borrowed from Middle French béryl . [ 1 ] [ 2 ] First attested in 1472.
925: Inherited from Old Polish beryl .
1089: Retrieved from " https://en.wiktionary.org/w/index.php?title=beryl&oldid=92520279 "
1091: Categories : English terms derived from Prakrit 
1092: English terms derived from Pali 
1093: English terms derived from Dravidian languages 
1094: English terms derived from Proto-Indo-European 
######## 75e90ed2cc6689c6
167: From Wiktionary, the free dictionary
195: Borrowed from Middle Indic forms like Pali veḷuriya or Prakrit 𑀯𑁂𑀭𑀼𑀮𑀺𑀅 ( verulia ) , from Dravidian , probably named after a city (modern day Bēlūr ) in southern India in which the mineral was mined. [ 1 ] 
381: From Ancient Greek βήρυλλος ( bḗrullos , “ beryl ” ) .
418: Retrieved from " https://en.wiktionary.org/w/index.php?title=βήρυλλος&oldid=93344954 "
420: Categories : Ancient Greek terms derived from Proto-Indo-Iranian 
421: Ancient Greek terms derived from Proto-Dravidian 
422: Ancient Greek terms derived from Prakrit 
423: Ancient Greek terms derived from Proto-Indo-European 
424: Ancient Greek terms borrowed from Prakrit 
425: Ancient Greek terms derived from Sanskrit 
426: Ancient Greek terms borrowed from Pali 
427: Ancient Greek terms derived from Pali 
######## cd40e1f887231397
196: From Wiktionary, the free dictionary
221: Borrowed from Classical Persian بِلّور ( billōr ) , from Middle Persian bylwl ( /⁠*bēlūr⁠/ ) , borrowed from Pali veḷuriya , from Proto-Dravidian *weḷ-ūr ( name of a city ) + Pali -iya .
1087: From Middle Persian [script needed] ( bylwl /⁠*bēlūr⁠/ , “ crystal ” ) , from Pali veḷuriya . Compare Parthian [Term?] ( byrwl /⁠*bērūl⁠/ , “ crystal ” ) and Ancient Greek βήρυλλος ( bḗrullos , “ beryl ” ) .
1181: Retrieved from " https://en.wiktionary.org/w/index.php?title=بلور&oldid=92739728 "
1183: Categories : Arabic terms derived from Pali 
1184: Arabic terms borrowed from Classical Persian 
1185: Arabic terms derived from Middle Persian 
1186: Arabic terms derived from Proto-Dravidian 
1187: Arabic terms derived from Classical Persian 
1212: Persian terms inherited from Middle Persian 
1213: Persian terms derived from Proto-Dravidian 
1214: Persian terms derived from Middle Persian 
######## 488202d7845f14fa
145: From Wiktionary, the free dictionary
153: Seemingly inherited from Middle Persian [script needed] ( gwlsk /⁠gursag⁠/ , “ hungry ” ) , but the correspondence is irregular. [ 1 ] Apparently influenced by (and probably from the same origin as) the synonym Middle Persian [Book Pahlavi needed] ( gwšnk' /⁠gušnag⁠/ , “ hungry ” ) , which is the source for the regular modern colloquial word گشنه ( gošne , “ hungry ” ) .
218: گشنه ( gošne ) , which is actually from a different Middle Persian word, is used colloquially in both Iran and Afghanistan. However, گشنه ( gošne ) is usually considered the colloquial form of گرسنه ( gorosne ) rather than a different word.
230: Retrieved from " https://en.wiktionary.org/w/index.php?title=گرسنه&oldid=92259622 "
232: Categories : Persian terms inherited from Middle Persian 
233: Persian terms derived from Middle Persian 
######## 37e727ed4792981d
208: From Wiktionary, the free dictionary
226: From bril +‎ -er .
278: Borrowed from Italian brillare .
655: Retrieved from " https://en.wiktionary.org/w/index.php?title=briller&oldid=91560841 "
669: French terms derived from Proto-Indo-European 
670: French terms derived from Sanskrit 
671: French terms derived from Prakrit 
672: French terms derived from Ancient Greek 
673: French terms borrowed from Italian 
674: French terms derived from Proto-Dravidian 
675: French terms derived from Latin 
676: French terms derived from Italian 
######## 975a15ed4554a3cd
144: From Wiktionary, the free dictionary
190: Sanskritization of Pali वेळुरिय ( veḷuriya , “ beryl ” ) or Prakrit वेलुरिअ ( veluria ) , derived from the name of a Dravidian mining town. See there for more.
366: → Malay: baiduri , biduri , waiduri ( nonstandard ) > Indonesian: baiduri ( inherited ) 
385: Retrieved from " https://en.wiktionary.org/w/index.php?title=वैडूर्य&oldid=92443258 "
387: Categories : Sanskrit terms derived from Pali 
388: Sanskrit terms derived from Proto-Dravidian 
389: Sanskrit terms borrowed from Pali 
390: Sanskrit terms derived from Middle Indo-Aryan by Sanskritization 
391: Sanskrit terms borrowed from Prakrit 
392: Sanskrit terms derived from Prakrit 
393: Sanskrit terms derived from Dravidian languages 
######## 049e3975f1470529
134: From Wiktionary, the free dictionary
147: From Middle Persian [Book Pahlavi needed] ( wls /⁠wars⁠/ , “ hair ” ) , from Proto-Iranian *wálśah , cognate with Avestan 𐬬𐬀𐬭𐬆𐬯𐬀 ( var ə sa , “ hair (on the head) ” ) , Sogdian 𐼴𐽀𐼼 ( wrs /⁠wars⁠/ , “ hair ” ) and Northern Kurdish pirç ( pirč , “ hair on the head ” ) ; from Proto-Indo-Iranian *wálćas , cognate with Sanskrit वल्श ( válśa , “ twig, sprout ” ) ; from Proto-Indo-European *wólḱ-o-s , cognate with Proto-Slavic *volsъ ( “ hair ” ) . Akin to Old Armenian վարս ( vars , “ hair ” ) and վարշամակ ( varšamak , “ handkerchief; headband ” ) , which are Iranian borrowings.
163: Retrieved from " https://en.wiktionary.org/w/index.php?title=گرس&oldid=85722985 "
165: Categories : Persian terms derived from Middle Persian 
166: Persian terms inherited from Proto-Iranian 
167: Persian terms derived from Proto-Iranian 
168: Persian terms inherited from Proto-Indo-Iranian 
169: Persian terms derived from Proto-Indo-Iranian 
170: Persian terms inherited from Proto-Indo-European 
171: Persian terms derived from Proto-Indo-European 
URL: https://en.wiktionary.org/wiki/برلیان
FETCHED: 2026-10-16T05:15:17Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not FoundURL: https://www.etymonline.com/word/beryl
FETCHED: 2026-10-16T05:15:19Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden
```


## [2026-10-16T05:15:39.846Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 215,225p cd40e1f887231397.txt; sed -n 1080,1092p cd40e1f887231397.txt; grep -n -i 'from \\|borrowed' 2a5914d0424ad150.txt | head -5; sed -n 270,285p 37e727ed4792981d.txt; grep -n -i 'from \\|borrowed\\|coined' 22ec466211a97720.txt a9c2a01a4884718f.txt | head -6",
 "description": "Read more etymology details"
}
```


### [2026-10-16T05:15:40.244Z] TOOL RESULT

```
 Pali veḷuriya bor. 
 Middle Persian bylwl ( /⁠*bēlūr⁠/ ) 
 Classical Persian بِلّور ( billōr ) bor. 
 Arabic بلور 

 Borrowed from Classical Persian بِلّور ( billōr ) , from Middle Persian bylwl ( /⁠*bēlūr⁠/ ) , borrowed from Pali veḷuriya , from Proto-Dravidian *weḷ-ūr ( name of a city ) + Pali -iya .

 Pronunciation
 [ edit ] 


 Pali -iya 

 Pali veḷuriya bor. 
 Middle Persian bylwl ( /⁠*bēlūr⁠/ ) 
 Persian بلور 

 From Middle Persian [script needed] ( bylwl /⁠*bēlūr⁠/ , “ crystal ” ) , from Pali veḷuriya . Compare Parthian [Term?] ( byrwl /⁠*bērūl⁠/ , “ crystal ” ) and Ancient Greek βήρυλλος ( bḗrullos , “ beryl ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /bi.ˈloːr/ , /bal.ˈloːr/ , /bil.ˈlawr/ , /bu.ˈluːr/ 
214: From Wiktionary, the free dictionary
249: Borrowed from French brillant (late 17th century), present participle of the verb briller , from Italian brillare , possibly from Latin berillus , beryllus ( “ a beryl, gem, eyeglass ” ) , from Ancient Greek βήρυλλος ( bḗrullos , “ beryl ” ) . By surface analysis , French brill(er) +‎ -i- +‎ -ant .
605: 1742 , Henry Fielding , “The History of Leonora, or the Unfortunate Jilt”, in The History of the Adventures of Joseph Andrews, and of His Friend Mr. Abraham Adams.   [ … ] , volume I, London: [ … ] A [ ndrew ] Millar ,   [ … ] , →OCLC , book II, page 183 : [ … ] Bellarmine vvhen he breakfaſted vvith her and her Niece, had complimented her vvith a Brilliant from his Finger, [ … ] 
607: 1834 , L[etitia] E[lizabeth] L[andon] , chapter XXII, in Francesca Carrara.   [ … ] , volume I, London: Richard Bentley ,   [ … ] , (successor to Henry Colburn ), →OCLC , page 257 : On the one, a plain massive band which matched the collar; on the other, a serpent; the tail reached nearly to the elbow, and the head rose a little from the wrist; the tongue of a ruby, the eyes of large brilliants . 
724: Borrowed from French brillant .
 Prakrit -इय ( -iya ) 

 Prakrit वेरुलिअ ( vērulia ) bor. 
 Ancient Greek βήρυλλος ( bḗrullos ) bor. 
 Latin bēryllus der. 
 Italian brillare bor. 
 French briller 

 Borrowed from Italian brillare .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /bʁi.je/ 

 Audio ( France ) : ( file ) 
a9c2a01a4884718f.txt:150: From Wiktionary, the free dictionary
a9c2a01a4884718f.txt:184: Borrowed from Ancient Greek βήρυλλος ( bḗrullos ) , borrowed from Prakrit वेरुलिअ ( vērulia ) , from Proto-Dravidian *weḷ-ūr ( name of a city ) + Prakrit -इय ( -iya ) .
a9c2a01a4884718f.txt:325: Retrieved from " https://en.wiktionary.org/w/index.php?title=beryllus&oldid=91361285 "
a9c2a01a4884718f.txt:327: Categories : Latin terms derived from Sanskrit 
a9c2a01a4884718f.txt:328: Latin terms derived from Ancient Greek 
a9c2a01a4884718f.txt:329: Latin terms derived from Proto-Dravidian
```


## [2026-10-16T05:15:45.136Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; head -c 200 22ec466211a97720.txt; grep -n -i 'beryl' 22ec466211a97720.txt | head -5; head -c 200 1cc80a3bd71c8bcc.txt; cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/beryllium' --note 'page 524 Velur beryllium' | tail -1; python3 tools/fetch_source.py 'https://vajehyab.com/moein/برلیان' --note 'page 524 Velur berelyan Moin' | tail -1;  python3 tools/fetch_source.py 'https://vajehyab.com/moein/بلور' --note 'page 524 Velur bolur Moin' | tail -1",
 "description": "Check beryllium page; fetch Mo'in online"
}
```


### [2026-10-16T05:15:46.490Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/beryllium
FETCHED: 2026-10-16T05:15:19Z
STATUS: 200
TITLE: beryllium - Wiktionary, the free dictionary

beryllium - Wiktionary, the free dictionary 

 Jump to conte1:URL: https://en.wiktionary.org/wiki/beryllium
4:TITLE: beryllium - Wiktionary, the free dictionary
6:beryllium - Wiktionary, the free dictionary 
246: beryllium 
351: See also: Beryllium and béryllium 
URL: https://www.etymonline.com/word/brilliant
FETCHED: 2026-10-16T05:15:19Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden/home/sfmqrb/git/rishe-private/data/verification/sources/web/22ec466211a97720.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a094991cc6741808.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8cfc1567f0ea1f6f.txt
```


## [2026-10-16T05:15:49.036Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 352,362p 22ec466211a97720.txt; grep -n 'برلیان' a094991cc6741808.txt | head -5; grep -n -A2 'معین' a094991cc6741808.txt | head -12; grep -n -A3 'بلور' 8cfc1567f0ea1f6f.txt | head -20",
 "description": "Read beryllium etymology and Mo'in online"
}
```


### [2026-10-16T05:15:49.327Z] TOOL RESULT

```
 English
 [ edit ] 

 Chemical element ( edit ) 

 Be 
 Atomic number 4 
 beryllium 

 Classification data
1:URL: https://vajehyab.com/moein/برلیان
4:TITLE: معنی برلیان | فرهنگ انتشارات معین | واژه یاب
6:معنی برلیان | فرهنگ انتشارات معین | واژه یاب 
14: برلیان
18: برلیان در فرهنگ‌های دیگر
4:TITLE: معنی برلیان | فرهنگ انتشارات معین | واژه یاب
5-
6:معنی برلیان | فرهنگ انتشارات معین | واژه یاب 
7-
8- 26 فرهنگ 
--
16: فرهنگ انتشارات معین
17- (بِ رِ) [ فر. ] ( اِ.) الماس تراش داده شده .
18- برلیان در فرهنگ‌های دیگر
1:URL: https://vajehyab.com/moein/بلور
2-FETCHED: 2026-10-16T05:15:46Z
3-STATUS: 200
4:TITLE: معنی بلور | فرهنگ انتشارات معین | واژه یاب
5-
6:معنی بلور | فرهنگ انتشارات معین | واژه یاب 
7-
8- 26 فرهنگ 
9-
--
14: بلور
15-
16- فرهنگ انتشارات معین
17- (بُ یا بَ) [ معر. ] ( اِ.) 1 - نوعی شیشه که از ترکیب سیلیکات دوپتاسیم و سیلیکات دوپلمب ساخته شود. 2 - کنایه از: شفاف .
18: بلور در فرهنگ‌های دیگر
19: معنی بلور در لغت‌نامه دهخدا 
20: معنی بلور در فرهنگ فارسی عمید / قربان‌زاده 
21: معنی بلور در دیکشنری عربی به فارسی 
22: معنی بلور در دیکشنری فارسی به عربی 
23: معنی بلور در دیکشنری فارسی به انگلیسی
```


## [2026-10-16T05:15:55.914Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'beryll\\|berill\\|bill[oö]r' LKT.txt DEV.txt PHN.txt | head -8; grep -n 'بلّور\\|البلور\\|بلور' AFM.txt TAD.txt ARB_mo3rb.txt ARB_abdulraheem.txt KFL.txt | head -8; grep -n -i 'bill[aaw]*r\\|ballūr\\|bulūr\\|billaur' incoming/PLA/PLA_pages.txt SIN.txt | head -8",
 "description": "Grep Arabic-loan sources for billaur"
}
```


### [2026-10-16T05:15:56.239Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:15:59.031Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; ls | head -80; grep -c . LKT.txt AFM.txt; grep -n 'لور' AFM.txt | head -5; grep -n -i 'beryl\\|ballor\\|bellor\\|bal[lI]ur' LKT.txt SIN.txt FVQ.txt | head",
 "description": "Check files and broader grep"
}
```


### [2026-10-16T05:15:59.313Z] TOOL RESULT

```
AFM.txt:6949
LKT.txt:10115
1017:وقيل معر بة عن ܨܠ امم بيج ومعناها اللوم والورقة والرسالة‎ ٠» $ حمائك ܐ‎ 
1027:لامنس 3 نغر نب 30 الورقة والرسالة .قلت وعندىي 0 معر بة عن 
1123:با ܠ « قولغان ܕܨ ¢ وهو نماث 0 الارض أخر 80 ܝ كالورق 
1583:+ ( )ܥ ) عريب ند وهو زهر الرمآن والورد < 0 ايضا على 
1683:لور مر وغيره وقيل جريال ܐܶܟ ܐܕܐ شيل ܝ ܀ الغلئل انما
```


## [2026-10-16T05:16:04.626Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'gursit\\|gursīt\\|gursid\\|gursag' PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt SNS.txt UNV.txt | head; for ln in 2629; do head -n $ln PHD_mackenzie.txt | tr -cd '\\f' | wc -c; done; head -n 1742 NYB_vol2_glossary.txt | tr -cd '\\f' | wc -c",
 "description": "Grep Pahlavi gursitan and page numbers"
}
```


### [2026-10-16T05:16:05.017Z] TOOL RESULT

```
PHD.txt:384:ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gursag [ewlsk] | N gurusna !] hungry. «ЛЬ: hunger. Suën [gvfn! | N ~] male. gusnag [gwšnk! | J gušna] hungry. Gušnasp [gwšn(*)sf] the second major Fire of Sasanian Eran, that of warriors. £yà$ [gyw'k! | M gy'g, N jay] place.
PHD.txt:2339:hunger gursagih, suy, Suy.
PHD.txt:2340:hungry gursag, gušnag.
PHD.txt:5444:gurgānīg gursagih gursag durgar jorda jorda 1-2gurdih gurd gurdwar gurdag dum, 1021 joma jomā gumānīh gumānīgīh gumānīg gumān gumāngar gumār- gumārdan gumārdag jumb- dumbēmand jumbāgīh jumbīh-
PHD_mackenzie.txt:2629:gursag [gwlsk] I N gurusna !] hungry.
PHD_mackenzie.txt:6814:hollowness gabrih.                             hunger gursagih, suy, suy.
PHD_mackenzie.txt:6815:holy abezag, pak, spenag, yoJdahr;             hungry gursag, gusnag.
PHD_mackenzie.txt:10718:gursagih            AU~t'          gonag                        ,oS U·
PHD_mackenzie.txt:10719:gursag
SNS.txt:18347:gursag: 5-cVW ^Av^ oL^ 1 ^ «*^-j*:gursnag: 3*^-'* 
59
98
```


## [2026-10-16T05:16:21.577Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'bylwl\\|bēlūr\\|belur\\|byrwl\\|crystal' PHD.txt NYB_vol2_glossary.txt HRN.txt HUB.txt | head -10; grep -n -i 'bill[oōaù]r\\|bulur\\|bulūr\\|ballur' HRN.txt HUB.txt CHEUNG.txt | head",
 "description": "Grep Pahlavi/Horn for belur crystal"
}
```


### [2026-10-16T05:16:21.944Z] TOOL RESULT

```
PHD.txt:169:abgar- [5%'I-] provide, promote. Ж abgénag Dfkynk!, M Y Akynk! | N ábgina] crystal, glass. Boyd "ebe, c-én[-yn!] crystalline. kat v3 abig Pfyk! | N abi] aquatic, watery. rea
PHD.txt:256:bayaspānļīh: mission, embassy. ~ig [-yk'] post-(horse). Бах [Pc | N ~] hawk, falcon. bāzā [b’c’y | (N bāzū)] arm. ~banag [-p'nk'] arm-guard, brassard. bazaģ [bck' | М beg, N ~a] sin, evil. —ih: = bazag. bazakkar [bckkl | M bzkr] sinful, sinner. bāzā-zanišnīh [by znfnyh = Av. bázu.jata-] a degree of sin. bazišn [dcšn'] division, part. bazm [bzm | — M, N —] meal, feast. ~-awurd [-zolt! | N ~] a sort of canapé. 1bë [BRA < A br | MP] but; out; ~... (enya), except. ~...enya...né: except... (otherwise)... not. ~ az: without. m 2be [BRA | M P, N bi-] particle with verbs, with 6, of indefinable function. -bed [-pt' | M -byd, N -balilud] suffix, -lord, -master. bēdom [bytwm | M bydwm] furthermost. béganag [byk’nk' | N ~a] strange; stranger. bégar [byk”/ | N ~] corvée, forced labour. béh [byh | N bih] quince. bel [by] | (M. Бу), N ~] spade. bélür [bylwl | M bylwr, N bilür] crystal. bérón [bylwn' | M byrwn, N bérün] outside. bëš [bys] pain, sorrow; harm, hostility. — burdan: bear hostility. bēš-, —i&n, v. bištan. bēšāz [byš(*)z] healing, medicinal. bēšāz(ēn)- [by?z(yn)-, byf?)c(yn)- | M byP?z-] heal, cure. —išnih: healing. bēš-burdār [byšbwlť’[] hostile. bëšidan [bysytn'] = bištan, bēšūmand [byš?*wmnd] sorrowful. béwar [Буш | M bywr, N ~] myriad, ten thousand. P bid [руй | P byd] again. bidaxš [byths] viceroy. *bifagàn [bch'n!] medicinal. bim [bym | = M, N ~] fear, terror. ~gén [-kn'] fearful, terrible. ~génih: fearfulness. --6mand [-'wmnd] fearful. *bistag [bstk! | N busta] hazelnut. biš [byf | N —] aconite. bištan, bé&- [bys-in' | M by$t, bys-] hurt, torment. ~išn: harm, torment. bize&k [dešk! | M bzyšk, N pizišk] doctor, physician.
PHD.txt:1454:crystal abgénag, bélür.
PHD.txt:1455:crystalline abgénagén.
NYB_vol2_glossary.txt:2419:Phl mānēnak ‘belonging to the sphere man’, 1. e. ‘rain-bearing’, or, as a subst., the rain itself. Paz. substitutes āvgīna, based on a reading MY?-kynk': apakénak, Skr v. ratnäkrti ‘of jewel form’; accepted by Bailey, ZP 131 (‘crystal’), but not preferable. — I withdraw my reading *mānēvak given in the Index.
```


## [2026-10-16T05:16:29.777Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -n 256 PHD.txt | tr -cd '\\f' | wc -c; head -n 384 PHD.txt | tr -cd '\\f' | wc -c; mkdir -p ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p524/pg524.png ocr/BOOK/524.png; head -n 1733 SKT.txt | tr -cd '\\f' | wc -c; head -n 3437 HJB.txt | tr -cd '\\f' | wc -c",
 "description": "Compute leaf numbers and copy book page image"
}
```


### [2026-10-16T05:16:30.133Z] TOOL RESULT

```
41
62
57
139
```


## [2026-10-16T05:18:17.042Z] TOOL CALL #38: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-524.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nU_beryl=W+\"beryl\"; U_gr=W+\"βήρυλλος\"; U_bol=W+\"بلور\"; U_gor=W+\"گرسنه\"; U_bril=W+\"brilliant\"; U_brl=W+\"briller\"; U_vai=W+\"वैडूर्य\"; U_lat=W+\"beryllus\"; U_gors=W+\"گرس\"\nU_mbol=\"https://vajehyab.com/moein/بلور\"; U_mbrl=\"https://vajehyab.com/moein/برلیان\"\nnc=lambda r,why=\"no online or local copy of the 1975 AHD main-dictionary page (local AHD is only Watkins' 1985 IE-root appendix, which has no beryl entry)\": {\"ref\":r,\"status\":\"not_checked\",\"note\":why}\nKLN166={\"ref\":\"KLN:166\",\"status\":\"supports\",\"note\":\"KLN_1966.txt leaf 99 (p.166), s.v. beryl: 'ME., fr. OF. beryl (F. beryl), fr. L. beryllus, fr. Gk. beryllos, fr. Prakrit veruliya, transposed fr. viluriya (whence OI. vaidurya-), which prob. derives from the name of the city Velur (now called Belur).'\"}\ne0_nodes=[\n {\"id\":1,\"lang\":\"Greek\",\"words\":\"beryllos, bĕrullos\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Ancient Greek bḗryllos (βήρυλλος) 'beryl, sea-green gem' was borrowed (Hellenistic period, via the Indian gem trade; Pliny says the best beryls came from India) from Middle Indic Prakrit verulia / Pali veḷuriya, with the l...r of veḷuriya transposed to r...l (Klein: 'transposed fr. viluriya'). Both spellings in the chart (beryllos, bērullos) render the same word; the root of the chain is the Dravidian town-name, not an IE root.\",\n  \"derivation_fa\":\"یونانی bḗryllos «زبرجد، سنگ سبزِ دریایی» وام‌واژه‌ای است از پراکریت verulia / پالی veḷuriya که در تجارت گوهر با هند به یونانی رسید؛ در این وام‌گیری جای l و r قلب شده است. کلاین و ویکی‌واژه همین را می‌گویند و ادعای نورایی درست است.\",\n  \"sources\":[U_gr,U_beryl],\n  \"ref_check\":[nc(\"AHD:126\"),KLN166],\n  \"consulted\":[{\"src\":\"SKT\",\"where\":\"SKT.txt leaf 57, s.v. Beryl\",\"stance\":\"supports\",\"note\":\"'Beryl. (L.-Gk.-Skt.) M.E. ... L. beryllus. — Gk. beryllos' (OCR garbled, Skt. vaidurya cited).\"},\n              {\"src\":\"HJB\",\"where\":\"HJB.txt leaf 139, s.v. BERYL\",\"stance\":\"supports\",\"note\":\"'its origin was the Skt. vaidurya, Prak. veluriya, whence [Malay baiduri], P. billaur, and Greek beryllos. Bochart points out the probable identity of the two last words by the transposition of l and r.'\"},\n              {\"src\":\"POK\",\"where\":\"POK_full.txt grep 'beryl'\",\"stance\":\"silent\",\"note\":\"no hit; non-IE (Dravidian/Indic) loanword, outside Pokorny's scope\"}]},\n {\"id\":2,\"lang\":\"Arabic\",\"words\":\"bolŭr; tabalvor; motebalver\",\"verdict\":\"disputed\",\n  \"derivation\":\"Arabic billawr / ballūr 'crystal' (Persianised reading bolur) is real, as are its tafaʿʿul derivatives tabalwur 'crystallization' and mutabalwir 'crystallized' (quadriliteral b-l-w-r). But the chart's arrow Greek → Arabic is not the modern view: Wiktionary (s.v. بلور) derives Arabic billawr from Classical Persian billōr, from Middle Persian bēlūr (bylwl), itself borrowed from Pali veḷuriya — i.e. an Iranian, not Greek, intermediary; MacKenzie confirms MP bēlūr 'crystal'. Greek bḗryllos is a parallel (cousin) borrowing from the same Indic word, not the source.\",\n  \"derivation_fa\":\"«بلّور / بِلَّور» در عربی واژه‌ای واقعی است و «تبلور» و «متبلور» ساخته‌های عربی (باب تفعّل) از ستاک چهارحرفی ب‌ل‌و‌ر هستند. اما پژوهش امروزی (ویکی‌واژه، مکنزی) آن را از یونانی نمی‌داند: عربی آن را از فارسی billōr گرفته که از فارسی میانهٔ bēlūr و آن خود از پالی veḷuriya است؛ یونانی bḗryllos هم‌ریشه‌ای موازی است نه منشأ. پس پیکان یونانی ← عربی در نمودار نورایی پذیرفته نیست.\",\n  \"sources\":[U_bol,U_mbol],\n  \"ref_check\":[{\"ref\":\"MON:575\",\"status\":\"partial\",\"note\":\"Mo'in online (vajehyab, s.v. بلور): '(بُ یا بَ) [معر.] (اِ.) ۱ - نوعی شیشه...' — Mo'in tags it 'Arabicized' but gives no Greek source; local MON_part1.txt l.25100 same entry. Page 575 of the 6-vol ed. not mappable.\"}],\n  \"consulted\":[{\"src\":\"PHD\",\"where\":\"PHD.txt leaf 41 (p.20), s.v. bēlūr\",\"stance\":\"contradicts\",\"note\":\"'bēlūr [bylwl | M bylwr, N bilūr] crystal' — the word is already Middle Persian, so Arabic need not have it from Greek\"},\n               {\"src\":\"HJB\",\"where\":\"HJB.txt leaf 139, s.v. BERYL\",\"stance\":\"partial\",\"note\":\"'Prak. veluriya, whence ... P. billaur, and Greek beryllos' — Persian and Greek as parallel borrowings\"},\n               {\"src\":\"AFM\",\"where\":\"AFM.txt grep 'بلور'\",\"stance\":\"silent\",\"note\":\"no hit (OCR)\"},\n               {\"src\":\"LKT\",\"where\":\"LKT.txt grep 'beryl|billor|ballur'\",\"stance\":\"silent\",\"note\":\"no hit\"}]},\n {\"id\":3,\"lang\":\"Persian\",\"words\":\"bolŭr\",\"verdict\":\"disputed\",\n  \"derivation\":\"Persian bolur / bellur / bilur 'crystal; clear' (quoted from Mas'ud-e Sa'd-e Salman) is genuine, but it is inherited, not borrowed from Arabic: MP bēlūr (Book Pahlavi bylwl, Manichaean bylwr; Parthian byrwl) < Pali/Prakrit veḷuriya, verulia; the MP long ē > NP i/e and the doublets bolur/bellur arise in New Persian (MacKenzie: 'N bilūr'). The extras tabalvor, motebalver are Arabic-pattern formations borrowed back into Persian, so only those reflect an Arabic route (a Persian → Arabic → Persian round-trip). Nourai's chain follows Mo'in's tag [معر.]; modern scholarship (MacKenzie, Wiktionary) treats bolur as native from MP.\",\n  \"derivation_fa\":\"«بُلور» (بِلور، بَلّور) در فارسی میراث فارسی میانهٔ bēlūr (پهلوی bylwl، مانوی bylwr، پارتی byrwl) است که خود از پالی veḷuriya وام گرفته شده؛ پس معرّب نیست و از عربی به فارسی نیامده است. تنها «تبلور» و «متبلور» ساخت‌های عربی‌اند که از «بلّورِ» عربیِ برگرفته از فارسی ساخته شده و دوباره به فارسی بازگشته‌اند (رفت‌وبرگشت فارسی ← عربی ← فارسی). معین آن را «معرّب» دانسته و نورایی از او پیروی کرده، ولی مکنزی و ویکی‌واژه این را نمی‌پذیرند.\",\n  \"sources\":[U_bol,U_mbol],\n  \"ref_check\":[{\"ref\":\"MON:575\",\"status\":\"supports\",\"note\":\"Mo'in (vajehyab): 'بلور (بُ یا بَ) [معر.] نوعی شیشه... ۲ - کنایه از: شفاف' — supports Nourai's Arabic-mediated arrow (and the gloss 'clear'), though modern sources reject it\"}],\n  \"consulted\":[{\"src\":\"PHD\",\"where\":\"PHD.txt leaf 41 (p.20)\",\"stance\":\"contradicts\",\"note\":\"'bēlūr [bylwl | M bylwr, N bilūr] crystal' — NP word continues MP\"},\n               {\"src\":\"HJB\",\"where\":\"HJB.txt leaf 139\",\"stance\":\"contradicts\",\"note\":\"'Prak. veluriya, whence ... P. billaur' — Persian directly from Indic\"},\n               {\"src\":\"HRN\",\"where\":\"HRN.txt grep 'bill?r|bulur'\",\"stance\":\"silent\",\"note\":\"no entry\"},\n               {\"src\":\"MON\",\"where\":\"MON_part1.txt l.25100\",\"stance\":\"supports\",\"note\":\"'بلور ... قسمی شیشه که از ترکیب سیلیکات دو پتاسیم و سیلیکات دو پلمب ساخته شود' (local OCR; online version has [معر.])\"}]},\n {\"id\":4,\"lang\":\"Latin\",\"words\":\"beryllus\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Latin bēryllus (also bērillus) 'beryl', borrowed from Greek bḗryllos (Pliny, NH 37.20 already describes Indian beryls). From Latin it passed to Old French beril and, via a Vulgar Latin verb *beryllare / Italian brillare 'to sparkle (like a beryl)', to French briller.\",\n  \"derivation_fa\":\"لاتین bēryllus «زبرجد» وام‌واژه از یونانی bḗryllos است (پلینی از زبرجدهای هندی یاد می‌کند). از همین واژه فرانسوی کهن beril و نیز فعل ایتالیایی brillare «درخشیدن» و فرانسوی briller پدید آمده است. ادعای نورایی درست است.\",\n  \"sources\":[U_lat,U_beryl],\n  \"ref_check\":[nc(\"AHD:126\")],\n  \"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt leaf 99 (p.166), s.v. beryl\",\"stance\":\"supports\",\"note\":\"'fr. L. beryllus, fr. Gk. beryllos'\"},\n               {\"src\":\"SKT\",\"where\":\"SKT.txt leaf 57, s.v. Beryl\",\"stance\":\"supports\",\"note\":\"'M.E. ... L. beryllus. — Gk. beryllos'\"},\n               {\"src\":\"WEB\",\"where\":\"WEB_vol1.txt l.18610, s.v. beryl\",\"stance\":\"supports\",\"note\":\"'[L. beryllus; Gr. béryllos, a gem ...]'\"}]},\n {\"id\":5,\"lang\":\"French\",\"words\":\"beryl, brillat\",\"verdict\":\"transcription_suspect\",\n  \"derivation\":\"French béryl (OF beril, from L. beryllus) is correct. 'brillat' is not a French word: the intended form is brillant 'shining; cut diamond', present participle of briller 'to shine', from Italian brillare, ultimately from L. beryllus (VL *beryllare 'to shine like a beryl', Klein). The book prints 'brillat'; this is Nourai's misprint for brillant, faithfully extracted.\",\n  \"derivation_fa\":\"فرانسوی béryl از فرانسوی کهن beril و لاتین beryllus است و درست است. اما «brillat» در فرانسوی وجود ندارد و صورت درست brillant «درخشان؛ الماس تراش‌خورده» است، صفت فاعلی از briller «درخشیدن» که از ایتالیایی brillare و در نهایت از لاتین beryllus («مانند زبرجد درخشیدن») آمده است. کتاب «brillat» چاپ کرده و این خطای چاپی کتاب است، نه خطای خوانش اسکن.\",\n  \"error_in\":\"book\",\"book_prints\":\"beryl, brillat\",\"correct_form\":\"béryl, brillant\",\n  \"sources\":[U_brl,U_bril],\n  \"ref_check\":[nc(\"AHD:126\"),{\"ref\":\"AHD:166\",\"status\":\"not_checked\",\"note\":\"1975 AHD main-dictionary page (presumably s.v. brilliant) not available; Klein p.199 covers the same claim (see node 7)\"}],\n  \"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt leaf 116 (p.199), s.v. brilliant\",\"stance\":\"supports\",\"note\":\"'F. brillant, lit. shining, pres. part. of briller, to shine, fr. VL. *beryllare, to shine like a beryl, fr. L. beryllus'\"},\n               {\"src\":\"SKT\",\"where\":\"SKT.txt leaf 57, s.v. Beryl\",\"stance\":\"supports\",\"note\":\"'brilliant, shining. (F.-Ital.) F. brillant, pres. part. of briller; cf. Ital. brillare, to sparkle ... beryllus, a beryl' (OCR garbled)\"}]},\n {\"id\":6,\"lang\":\"Persian\",\"words\":\"berelyân\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Persian berelyân / berliyân 'brilliant-cut diamond' is a modern (Qajar-era) loan from French brillant (nasal -ant rendered -ân, the cluster br- broken by an epenthetic vowel and the palatal ll /j/ written -ly-). Mo'in marks it [فر.] 'French' and glosses it 'الماس تراش داده شده'.\",\n  \"derivation_fa\":\"«برلیان» وام‌واژه‌ای نو (از دورهٔ قاجار) از فرانسوی brillant «الماس تراش‌خورده» است؛ خوشهٔ آغازین br- با واکهٔ میانجی شکسته و پایانهٔ -ant به «-ان» بدل شده است. معین آن را [فر.] و «الماس تراش داده شده» آورده و ادعای نورایی درست است.\",\n  \"sources\":[U_mbrl],\n  \"ref_check\":[{\"ref\":\"MON:511\",\"status\":\"supports\",\"note\":\"Mo'in online (vajehyab, s.v. برلیان): '(بِ رِ) [فر.] (اِ.) الماس تراش داده شده.'; also local MON_part1.txt l.22691 'برلیان ... (زم.) الماس تراش داده شده از تمام جهات'\"}],\n  \"consulted\":[{\"src\":\"MON\",\"where\":\"MON_part1.txt l.22691\",\"stance\":\"supports\",\"note\":\"'برلیان: (زم.) الماس تراش داده شده ... به منظور زیبایی و تلألو بیشتر'\"},\n               {\"src\":\"KLN\",\"where\":\"KLN_1966.txt leaf 116 (p.199), s.v. brilliant\",\"stance\":\"supports\",\"note\":\"French source word brillant 'shining' confirmed\"},\n               {\"src\":\"ARY\",\"where\":\"ARY_latin_index_pages.txt grep 'BERELIAN|BERLIAN'\",\"stance\":\"silent\",\"note\":\"no hit (non-IE loan)\"}]},\n {\"id\":7,\"lang\":\"English\",\"words\":\"beryl, beryllium, brilliant\",\"verdict\":\"confirmed\",\n  \"derivation\":\"English beryl (ME beril, 13th c.) < OF beril < L. beryllus; beryllium is a Modern Latin coinage (19th c.) for the element first isolated from beryl (Vauquelin identified the earth in 1797-8); brilliant (late 17th c.) < F. brillant 'shining', pres. part. of briller. Strictly beryllium is a learned coinage from Latin, not from French, but the chart's grouping under the French node is harmless.\",\n  \"derivation_fa\":\"انگلیسی beryl از انگلیسی میانه beril و فرانسوی کهن beril و لاتین beryllus است؛ beryllium نام عنصری است که در سدهٔ نوزدهم به لاتین نو از روی beryl ساخته شد (چون نخست از زبرجد جدا شد)؛ brilliant در اواخر سدهٔ هفدهم از فرانسوی brillant «درخشان» گرفته شد. ادعای نورایی درست است، جز آن‌که beryllium مستقیماً از لاتین علمی ساخته شده نه از فرانسوی.\",\n  \"sources\":[U_beryl,U_bril],\n  \"ref_check\":[nc(\"AHD:126\"),{\"ref\":\"AHD:166\",\"status\":\"not_checked\",\"note\":\"1975 AHD page not available\"},\n               {\"ref\":\"KLN:200\",\"status\":\"supports\",\"note\":\"KLN_1966.txt leaf 116 (pp.199-200), s.v. brilliant: 'F. brillant ... pres. part. of briller ... fr. L. beryllus ... See beryl'\"}],\n  \"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt leaf 99 (p.166), s.v. beryl, beryllium\",\"stance\":\"supports\",\"note\":\"'beryl, n. — ME., fr. OF. beryl'; 'beryllium ... ModL., fr. L. beryllus ... first obtained through isolation from beryl (by the French chemist Nicolas-Louis Vauquelin in 1797)'\"},\n               {\"src\":\"SKT\",\"where\":\"SKT.txt leaf 57\",\"stance\":\"supports\",\"note\":\"'Beryl. (L.-Gk.-Skt.)'; 'Brilliant, shining: see Beryl'\"},\n               {\"src\":\"WEB\",\"where\":\"WEB_vol1.txt l.18610\",\"stance\":\"supports\",\"note\":\"beryl '[L. beryllus; Gr. béryllos]'; l.16978 'Be ... beryllium'\"}]}\n]\ne5_nodes=[\n {\"id\":1,\"lang\":\"Pahlavi\",\"words\":\"gursak; gursakîh; gursîtan\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Book Pahlavi gursag [gwlsk] 'hungry', abstract gursagīh 'hunger', and the verb gursīdan (Horn: phlv. gursītan in the Vendidad gloss) 'to be hungry' continue Old Iranian *wṛša- 'hunger' (root *warš- 'be hungry'): initial *wṛ- > MP gur- (as in gurg 'wolf' < *wṛka-, gurdag 'kidney' < *wṛtka-), Hübschmann's regular rule. Nyberg also has the -n- form gurisnak 'hungry'.\",\n  \"derivation_fa\":\"پهلوی gursag «گرسنه»، gursagīh «گرسنگی» و gursīdan «گرسنه بودن» از ایرانی باستان *wṛša- «گرسنگی» آمده‌اند؛ آغازهٔ *wṛ- در فارسی میانه به gur- بدل می‌شود، چنان‌که در gurg «گرگ» از *wṛka- و gurdag «گرده، کلیه». مکنزی، نیبرگ، هرن و هوبشمان همین را می‌گویند و ادعای نورایی درست است.\",\n  \"sources\":[U_gor],\n  \"ref_check\":[{\"ref\":\"BQT:1794\",\"status\":\"supports\",\"note\":\"The gors entry is actually on printed p.1796 (BQT_v3 pdf 591; printed p.1794 = pdf 589 has گردن/گرده). Mo'in's footnote (OCR): 'پهلوی gursak، gursakih، gursitan؛ کردی vurs، vursigi ... بلوچی gushnag ... پارسی باستان *vrsa, *vrsna «هوبشمان ۹۰۷»'\"}],\n  \"consulted\":[{\"src\":\"PHD\",\"where\":\"PHD.txt leaf 62, s.v. gursag\",\"stance\":\"supports\",\"note\":\"'gursag [gwlsk | N gurusna] hungry. ~ih: hunger.' — also lists separately 'gušnag [gwšnk | J gušna] hungry'\"},\n               {\"src\":\"NYB\",\"where\":\"NYB_vol2_glossary.txt leaf 98 (p.90)\",\"stance\":\"supports\",\"note\":\"'gurisnak [gwlysnk'] hungry ... NP gur(z)snah'; 'gursakēh [gwlskyh] hunger ... Paz. gursaa hungry; NP gurs hunger'\"},\n               {\"src\":\"HRN\",\"where\":\"HRN.txt no. 907\",\"stance\":\"supports\",\"note\":\"'907. gurs Hunger, gursene, gursenegi ... phlv. gursak (AV.), gursakīh (Men.), gursītan (Vd.)'\"}]},\n {\"id\":2,\"lang\":\"Persian\",\"words\":\"gors 1; goresneh\",\"verdict\":\"confirmed\",\n  \"derivation\":\"NP gors 'hunger' (rare, lexicographic; Borhan cites Bes-hâq's verse, noting the printed divan reads جوع instead) < MP gursag/gursagīh, and gorosne/gorsne 'hungry' < *wṛšna- (-na- adjective), MP Nyberg gurisnak, Pazand gursnai. Wiktionary calls the MP→NP correspondence 'irregular' but accepts inheritance. The extras گشنه / گشنگی are colloquial: MacKenzie and Wiktionary derive gošne from a separate MP gušnag 'hungry', while Hübschmann explains gušna as gursna reshaped after tišna 'thirsty' — so their grouping here is acceptable but debated. Note gors 1 must be kept apart from gors 2 'curled hair' < MP wars < Av. varəsa- (Horn 908).\",\n  \"derivation_fa\":\"«گُرس» به معنی «گرسنگی» (واژه‌ای کم‌کاربرد که برهان با بیت بسحاق اطعمه آورده) و «گرسنه» از پهلوی gursag / gurisnak و ایرانی باستان *wṛša-، *wṛšna- آمده‌اند. ویکی‌واژه تحول را «نامنظم» ولی موروثی می‌داند. «گشنه» را مکنزی و ویکی‌واژه از واژهٔ جداگانهٔ پهلوی gušnag می‌دانند، ولی هوبشمان آن را صورتی از «گرسنه» می‌داند که به قیاس «تشنه» دگرگون شده است. «گرس» به معنی «موی پیچیده» (گرس ۲) هم‌ریشه نیست و از پهلوی wars و اوستایی varəsa- است. ادعای نورایی درست است.\",\n  \"sources\":[U_gor,U_gors],\n  \"ref_check\":[{\"ref\":\"BQT:1794\",\"status\":\"supports\",\"note\":\"Entry found on printed p.1796 (BQT_v3 pdf 591, cached as ocr/BQT/1796.png): 'گرس - بضم اول و سکون ثانی و سین بی‌نقطه، گرسنگی را گویند که در مقابل سیری است - و بمعنی چرک ... و موی پیچیده' with footnote 'رک: گرسنه، گشنه ... پارسی باستان *vrsa, *vrsna (هوبشمان ۹۰۷)' and the verse 'گرس از دلم ببرد غم زلف و خال دوست... بسحاق اطعمه'\"},\n               {\"ref\":\"HUB:92\",\"status\":\"supports\",\"note\":\"HUB.txt leaf 102 (p.92), note to Horn 907: 'Die Nebenform gusna hungrig ist durch Anlehnung an tisna durstig entstanden ... Für das Altpers. ist *vrsa-, *vrsna- anzusetzen.'\"}],\n  \"consulted\":[{\"src\":\"HRN\",\"where\":\"HRN.txt no. 907\",\"stance\":\"supports\",\"note\":\"'gurs Hunger, gursene, gursenegi; gusne ... phlv. gursak ... Wegen g. vasne etc. muss der Anlaut ursprünglich ein v gewesen sein'\"},\n               {\"src\":\"CHEUNG\",\"where\":\"CHEUNG.txt s.v. *u̯arš 'to be hungry'\",\"stance\":\"supports\",\"note\":\"'MMP gwrsgyh hunger? ... NWIR: NP gusnah ... The root *uarš appears to be a kind of Reimbildung after *tarš to be thirsty'\"},\n               {\"src\":\"MON\",\"where\":\"MON_part2.txt l.31390-31397\",\"stance\":\"supports\",\"note\":\"'گرسنگی ... گرسنه [= گسنه = گشنه] (ص.) آنکه احساس احتیاج به خوردن کند'\"},\n               {\"src\":\"ARY\",\"where\":\"ARY_pages.txt pdf p.429\",\"stance\":\"partial\",\"note\":\"entry 'گرسنه، گشنه، گرسنگی، گشنگی' with Pahlavi, Kurdish, Baluchi, Pashto and Old Persian forms (Latin OCR illegible); also lists European words, cites 'برهان قاطع: ۱۷۹۴'\"}]},\n {\"id\":3,\"lang\":\"Sogdian\",\"words\":\"wš`y; wšn, `wšnty\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Buddhist Sogdian wš'y- (wšay-) 'to be hungry' < *wṛš- (*warš-), with the regular Sogdian loss of r before š; 'wšnty / wš'nty (usande) 'hungry' < *wṛš-anta-ka-, with variants wšn. These are true cognates of MP gursag, not descendants of the Persian forms, which the chart correctly draws as a separate branch from the root.\",\n  \"derivation_fa\":\"سغدی wš'y- «گرسنه بودن» از ریشهٔ ایرانی *warš- / *wṛš- است و ’wšnty «گرسنه» از *wṛš-anta-ka- ساخته شده؛ این‌ها هم‌ریشهٔ پهلوی gursag و فارسی «گرسنه» هستند. فرهنگ سغدی قریب و چونگ همین را می‌گویند و ادعای نورایی درست است.\",\n  \"sources\":[],\n  \"ref_check\":[{\"ref\":\"SOD:79\",\"status\":\"supports\",\"note\":\"SOD_pages.txt leaf 144 (p.78/79), entry 2001: \\\"'wsnty C usande <*vrs+andaka hungry =>ws'y-, ws'nt'y\\\"\"},\n               {\"ref\":\"SOD:414\",\"status\":\"supports\",\"note\":\"SOD_pages.txt leaf 481 (p.414/415), entry 10218: \\\"ws'y- B, C wsay <*wrs- =>wswq, ws'nt'y, wsn-, 'wsnty (to) be hungry SCE 29\\\"; entry 10213 \\\"ws'nty S wisande, usande ... pl. -t 'wsnty, wsn, wswq hungry\\\"\"}],\n  \"consulted\":[{\"src\":\"SOD\",\"where\":\"entries 2001, 10213, 10218\",\"stance\":\"supports\",\"note\":\"as in ref_check\"},\n               {\"src\":\"CHEUNG\",\"where\":\"CHEUNG.txt s.v. *u̯arš\",\"stance\":\"supports\",\"note\":\"'SOGDIAN: BSogd. ws'y-, CSogd. wš- to be hungry. Pres.: IND. 3sg. BSogd. ws'yt (SCE 29)'; Parthian wsynd 'hungry'\"}]}\n]\nout={\"pdf_page\":524,\"book_page\":494,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-16\",\"entries\":[\n {\"entry\":0,\"root\":\"Velŭr, Bĕlŭr / Vaidŭrya, Veluryia\",\"verdict\":\"confirmed\",\n  \"modern_form\":\"Dravidian place-name Vēḷūr (modern Belur), Prakrit verulia / Pali veḷuriya 'beryl', Sanskritised vaiḍūrya\",\n  \"note\":\"Klein p.166 (Nourai's own reference), Wiktionary and Hobson-Jobson all derive beryl via Prakrit veruliya/Pali veḷuriya from the name of a South Indian town Velur/Belur (Dravidian). Language label 'Sanskrit' is loose: vaiḍūrya is a Sanskritisation of the Middle Indic form and the town name is Dravidian, as the chart's gloss itself says. Non-IE root, so POK/WLD/AHD are silent. Cross-cutting: the Arabic/Persian branch (bolur) is drawn Greek → Arabic → Persian; modern sources derive it Pali → MP bēlūr → Persian → Arabic. French 'brillat' is a book misprint for brillant.\",\n  \"note_fa\":\"ریشه نام شهری دراویدی در جنوب هند (Vēḷūr، امروز Belur) است؛ از آن پراکریت verulia و پالی veḷuriya «زبرجد» و صورت سنسکریت‌شدهٔ vaiḍūrya پدید آمده. کلاین، ویکی‌واژه و هابسن-جابسن همین را می‌گویند و ادعای نورایی درست است، جز آن‌که برچسب «سنسکریت» دقیق نیست. شاخهٔ «بلور» را امروز از فارسی میانهٔ bēlūr می‌دانند نه از یونانی و عربی؛ و «brillat» خطای چاپی کتاب برای brillant است.\",\n  \"sources\":[U_beryl,U_vai,U_gr],\n  \"ref_check\":[KLN166,nc(\"AHD:126\")],\n  \"consulted\":[{\"src\":\"HJB\",\"where\":\"HJB.txt leaf 139, s.v. BERYL\",\"stance\":\"supports\",\"note\":\"'its origin was the Skt. vaidurya, Prak. veluriya'\"},\n               {\"src\":\"POK\",\"where\":\"POK_full.txt grep 'beryl'\",\"stance\":\"silent\",\"note\":\"no hit (non-IE)\"},\n               {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt grep 'beryl'\",\"stance\":\"silent\",\"note\":\"no hit (non-IE)\"}],\n  \"nodes\":e0_nodes},\n {\"entry\":5,\"root\":\"Vrsa, Vrsna\",\"verdict\":\"plausible\",\n  \"modern_form\":\"Proto-Iranian *u̯arš- / *wṛš- 'to be hungry' (Cheung); OP *vṛša-, *vṛšna- is Hübschmann's unattested reconstruction\",\n  \"note\":\"The root is not attested in Old Persian: Hübschmann (p.92, Nourai's HUB:92, followed by Mo'in in Borhan) posits OP *vṛša-, *vṛšna-; the chart omits the asterisk. Cheung reconstructs Ir. *u̯arš 'to be hungry', with Sogdian, Parthian, Choresmian and Pashto cognates, possibly a rhyme-formation after *tarš 'to be thirsty'; no secure PIE etymology. Gloss 'hunger' correct. BQT:1794 should be 1796 (the gors entry is two pages later).\",\n  \"note_fa\":\"این ریشه در پارسی باستان گواهی نشده و صورت *vṛša-، *vṛšna- بازسازی هوبشمان است (که معین در حاشیهٔ برهان از او آورده)؛ نورایی نشانهٔ ستاره را انداخته است. چونگ ریشهٔ ایرانی *warš- «گرسنه بودن» را با هم‌ریشه‌های سغدی، پارتی، خوارزمی و پشتو آورده و آن را شاید ساختی هم‌قافیه با *tarš- «تشنه بودن» می‌داند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\":[U_gor],\n  \"ref_check\":[{\"ref\":\"BQT:1794\",\"status\":\"supports\",\"note\":\"actually printed p.1796 (pdf 591): Mo'in's footnote to گرس: 'شکل پارسی باستان *vrsa, *vrsna «هوبشمان ۹۰۷»'\"}],\n  \"consulted\":[{\"src\":\"HUB\",\"where\":\"HUB.txt leaf 102 (p.92)\",\"stance\":\"supports\",\"note\":\"'Für das Altpers. ist *vrsa-, *vrsna- anzusetzen' (reconstruction); also p.~145 'gurs Hunger, gursina hungrig aus *vrsa-, *vrsna-'\"},\n               {\"src\":\"CHEUNG\",\"where\":\"CHEUNG.txt s.v. *u̯arš\",\"stance\":\"partial\",\"note\":\"Iranian root *uarš 'to be hungry', 'a kind of Reimbildung after *tarš'; MP form only '? MMP gwrsgyh'\"},\n               {\"src\":\"KNT\",\"where\":\"KNT_full.txt grep 'vrs|hunger'\",\"stance\":\"silent\",\"note\":\"no OP word for hunger attested\"},\n               {\"src\":\"POK\",\"where\":\"POK_full.txt\",\"stance\":\"silent\",\"note\":\"no Iranian hunger-word under *wers-; no IE root proposed\"}],\n  \"nodes\":e5_nodes}\n]}\njson.dump(out,open(\"/home/sfmqrb/git/rishe-private/data/verification/page-524.json\",\"w\",encoding=\"utf-8\"),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-524.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-524.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 524",
 "description": "Build page-524 verification JSON and run checker"
}
```


### [2026-10-16T05:18:17.614Z] TOOL RESULT

```
nodes verified: 10/10
node verdicts: {'confirmed': 7, 'disputed': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'not_checked': 6, 'supports': 9, 'partial': 1}
books consulted: {'supports': 21, 'silent': 5, 'contradicts': 3, 'partial': 2} | by book: {'SKT': 4, 'KLN': 4, 'HJB': 3, 'PHD': 3, 'HRN': 3, 'MON': 3, 'WEB': 2, 'ARY': 2, 'CHEUNG': 2, 'POK': 1, 'AFM': 1, 'LKT': 1, 'NYB': 1, 'SOD': 1}
```


## [2026-10-16T05:18:27.723Z] TOOL CALL #39: SubagentHandback

```json
{
 "message": "I wrote the page 524 (book p. 494) verification file and ran `verify_check.py 524`: 10/10 nodes verified and 0 PROBLEM lines. There are two non-redirect entries, Velŭr (entry 0) and Vrsa/Vrsna (entry 5).\n\n**Verdicts**\n- **Nodes:** 7 confirmed, 2 disputed, 1 transcription_suspect.\n- **Roots:** Velŭr confirmed, Vrsa/Vrsna plausible.\n- **Root note on Vrsa/Vrsna:** \"Old Persian *vṛša-, *vṛšna-\" is not attested. It is Hübschmann's reconstruction (HUB:92), which Mo'in repeats in his notes to Borhan. The chart leaves out the asterisk. Cheung reconstructs an Iranian root *u̯arš- \"to be hungry\".\n- **Reference checks:** 9 supports, 1 partial, 6 not_checked. The not_checked ones are all AHD:126/166: those are pages of the 1975 AHD main dictionary, which isn't available locally or online.\n\n**Disputed**\n- **Velŭr #2, Arabic bolŭr; tabalvor; motebalver:** the chart draws Greek beryllos → Arabic. MacKenzie (MP bēlūr, written bylwl, \"crystal\") and Wiktionary instead give Pali veḷuriya → Middle Persian bēlūr → Persian billōr → Arabic billawr. Greek is a parallel borrowing from the same Indic word, not the source.\n- **Velŭr #3, Persian bolŭr:** this is inherited from Middle Persian bēlūr, not taken from Arabic. Nourai follows Mo'in's [معر.] (\"Arabicized\") label, and MON:575 does support the arrow. Only تبلور and متبلور are Arabic formations that came back into Persian.\n\n**Transcription suspect**\n- **Velŭr #5, French \"beryl, brillat\":** the printed page really does say \"brillat\". It is the book's misprint for French *brillant*; the extraction is faithful (error_in: book). I copied the page image to `data/verification/sources/refs/ocr/BOOK/524.png`.\n\n**Extraction errors:** none. The JSON matches the printed page.\n\n**Citation correction for the owner:** Nourai's BQT:1794 for the gors entry is really printed p. 1796 (vol. 3 PDF p. 591). It's cached as `ocr/BQT/1796.png`. The `ocr/BQT/1794.png` cache now holds printed p. 1794 itself, which is the گردن/گرده page.\n\nFile: /home/sfmqrb/git/rishe-private/data/verification/page-524.json"
}
```


### [2026-10-16T05:18:28.074Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
