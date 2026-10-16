# Verification process log — verify-page-528


## [2026-10-16T05:13:01.805Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 528 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-528.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-528.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-528.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 528` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:01.875Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:06.359Z] TOOL CALL #1: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md; echo ====; cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-528.txt; echo ====; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-528.json",
 "description": "Read instructions, chart, and source JSON"
}
```


### [2026-10-16T05:13:07.164Z] TOOL RESULT

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


## [2026-10-16T05:13:09.515Z] TOOL CALL #2: Bash

```json
{
 "command": "sed -n 60,140p /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md",
 "description": "Read truncated middle of instructions"
}
```


## [2026-10-16T05:13:09.999Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-528.txt",
 "description": "Read chart text for page 528"
}
```


### [2026-10-16T05:13:10.315Z] TOOL RESULT

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


### [2026-10-16T05:13:10.324Z] TOOL RESULT

```
=== PDF page 528 (book page 498) ===
--- entry 0 ---
ROOT [Indo-European] Wed, Wer 4, Aŭe 2, Ud 2 : water, wet  (refs POK:78; AHD:1547,1549; KLN:1732)  PART 2
#1 (parent #0) [Greek] refs=AHD | hudôr : water
  #2 (parent #1) [French] refs=None | hydrogene : water maker ☞Gene 1
    #3 (parent #2) [Persian] refs=MON:5230 | hîdrogen «هیدروژن»
  #4 (parent #1) [English] refs=None | hydrogen, hydrant, hydro
#5 (parent #0) [Old Irish] refs=AHD:1410 | uisce : water ; uisce beathadh : water of life
  #6 (parent #5) [English] refs=AHD:1460 | usquebaugh, usquabae, whiskey, whisky
    #7 (parent #6) [Persian] refs=MON:5072 | vîskî «ویسکی» : "water of life"
#8 (parent #0) [Russian] refs=AHD | voda : water ; vodka : a drink
  #9 (parent #8) [Persian] refs=MON:4994 | vodkâ «ودکا» : "water, drink"
  #10 (parent #8) [English] refs=AHD | vodka
#11 (parent #0) [Germanic] refs=AHD | water : water ; wĕd : wet ; wat-skan : wash ; wintruz : wet season, winter
  #12 (parent #11) [English] refs=None | water, wet, wash ; winter, otter
#13 (parent #0) [Latin] refs=AHD | unda : wave
  #14 (parent #13) [Latin] refs=AHD | super-undere : wave around ; red-undare : over flow
    #15 (parent #14) [English] refs=AHD | surround ; redundant
#16 (parent #0) [Latin] refs=AHD | ŭrîna : urine
  #17 (parent #16) [English] refs=None | urine
--- entry 1 ---
ROOT Wedh -> redirect to Wen
--- entry 2 ---
ROOT [Indo-European] Wedh 1 : to marry  (refs POK:1115)
#1 (parent #0) [Avestan] refs=POK:1115 | vadhu, vadŭ 1 : marry ; vadhu-upa : to marry ☞Upo
  #2 (parent #1) [Persian] refs=BQT:342; FRS:160; AEF:264 | bayŭg «بیوگ» : bride ; bayŭgânî «بیوگانی» : marriage | extra: بیوک ، بیو
#3 (parent #0) [Sogdian] refs=SOD:403 | wd : wife
```


## [2026-10-16T05:13:14.707Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 140,175p /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md; ls /home/sfmqrb/git/rishe-private/data/verification/ | tail -5; cat /home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md | head -80; ls /home/sfmqrb/git/rishe-private/data/verification/sources/refs/",
 "description": "Read rest of instructions and source matrix"
}
```


### [2026-10-16T05:13:15.088Z] TOOL RESULT

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


## [2026-10-16T05:13:19.095Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 175,200p /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe-private/data/verification/page-518.json'));print(json.dumps(d,ensure_ascii=False,indent=1)[:5000])\"; grep -n \"PROBLEM\" /home/sfmqrb/git/rishe-private/tools/verify_check.py | head -40",
 "description": "Read rest of instructions, sample output, checker rules"
}
```


### [2026-10-16T05:13:19.623Z] TOOL RESULT

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
{
 "pdf_page": 518,
 "book_page": 488,
 "verified_by": "claude-opus-5.5",
 "verified_on": "2026-10-14",
 "entries": [
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
     "derivation": "omm أمّ (pl. ommahât أمّهات) is a learned Arabic loan in Persian, used beside native mâdar (e.g. omm-ol-ketâb). moğîlân مغیلان is
90:        print("PROBLEM:", p)
```


## [2026-10-16T05:13:22.856Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','MON','BQT','FRS','AEF','SOD']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:700]);print()\n\"; cat data/extracted/batch/page-528.json | head -c 3000",
 "description": "Show reference metadata and source JSON head"
}
```


### [2026-10-16T05:13:23.347Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based lea

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966:

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/F

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, ver

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s

{
  "pdf_page": 528,
  "book_page": 498,
  "entries": [
    {
      "root": {
        "name": "Wed, Wer 4, Aŭe 2, Ud 2",
        "lang": "Indo-European",
        "refs": "POK:78; AHD:1547,1549; KLN:1732",
        "gloss": "water, wet"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "hudôr", "gloss": "water", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "hydrogene", "gloss": "water maker", "script": null, "see": ["Gene 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:5230",
          "words": [
            {"translit": "hîdrogen", "gloss": null, "script": "هیدروژن"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "hydrogen, hydrant, hydro", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Old Irish",
          "refs": "AHD:1410",
          "words": [
            {"translit": "uisce", "gloss": "water", "script": null},
            {"translit": "uisce beathadh", "gloss": "water of life", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD:1460",
          "words": [
            {"translit": "usquebaugh, usquabae, whiskey, whisky", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:5072",
          "words": [
            {"translit": "vîskî", "gloss": "\"water of life\"", "script": "ویسکی"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Russian",
          "refs": "AHD",
          "words": [
            {"translit": "voda", "gloss": "water", "script": null},
            {"translit": "vodka", "gloss": "a drink", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:4994",
          "words": [
            {"translit": "vodkâ", "gloss": "\"water, drink\"", "script": "ودکا"}
          ],
          "note": null,
          "quote": null
        },
        {
```


## [2026-10-16T05:13:26.814Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/528.jpg; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','MON','BQT']:\n  v=d.get(k); print(k, v.get('page_offset'), '|', v.get('lookup_hint'), '|', v.get('local_file'));print()\n\"",
 "description": "Show page offsets and lookup hints"
}
```


### [2026-10-16T05:13:27.242Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   73k sfmqrb 14 Oct 22:15  site/pages/528.jpg
POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config | /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt

AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.). | /home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt

KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages. | /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt

MON None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks). | ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']

BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor) | ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
```


## [2026-10-16T05:13:28.853Z] TOOL CALL #8: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/528.jpg"
}
```


### [2026-10-16T05:13:28.885Z] TOOL RESULT

```

```


## [2026-10-16T05:13:46.270Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"lemma: (au̯ed|au̯er|u̯ed|wed|au̯e)\" POK_full.txt | head; grep -n -E \"^(wed-|wer-|aw-|wedh-|ud-)\" AHD_watkins1985.txt | head; grep -n -i \"^vodka\\|^whisk\\|^usquebaugh\\|^redundant\\|^surround\\|^urine\\|^otter\\|^hydro\" KLN_1966.txt | head -20",
 "description": "Grep Pokorny, AHD, Klein for root and words"
}
```


### [2026-10-16T05:13:46.588Z] TOOL RESULT

```
1102:ud-. Also Gd-. Up, out. 1. Germanic *it-, out, in: a. Old English at, ovuT; utmost; b. Old High German az (> German aus), out, in German garaus, “all out”: CA- ROUSE; AUSLANDER; C. Old Norse at, out: OUTLAW; d. Middle Dutch ute, uut, out: UITLANDER; e. Middle Dutch dteren, to drive away, speak out: UTTER}; f. Ger- manic suffixed (comparative) form *it-era- in Old Eng- lish dtera, outer: UTTER?; g. Germanic compound *bi-iitana (*bi-, by, at; see ambhi), “at the outside,” in Old English bitan, biite, outside (adverb): BUT; ABOUT. 2. Extended form *uds in Germanic *uz, out, and prefix *uz-, out, in: a. Old High German ir-, out, in irsezzan, to replace: ERSATZ; b. Middle Dutch oor-, out: ORT; c. Ger- manic *uz-dailjam, “a portioning out,” judgment (see dail-). 3. Suffixed (comparative) form *ud-tero- in Greek husteros, later, second, after: HYSTERESIS, HYSTERON PROTERON. 4. Greek hu- in compound hubris, violence, outrage, insolence (bri-, perhaps “heavy,” “violent”; see g”era-?): HUBRIS. [Pok. d- 1103.]
1127:wed-'. Water; wet. 1. Suffixed o-grade form *wod-6r in Germanic *watar in Old English weter, water: WATER. 2. Suffixed lengthened-grade form *wéd-o- in Germanic *wéd- in Old English wt, wét, wet: WET. 3. O-grade form *wod- in Germanic suffixed form “wat-skan, to wash, in Old English wescan, wacsan, to wash: WASH. 4. Nasalized form *we-n-d- in Germanic *wintruz, win- ter, “wet season,” in Old English winter, winter: WINTER. 5. Suffixed zero-grade form *ud-d6r in Greek hudor, water: (HYDRANT), HYDRO-, (HYDROUS); ANHYDROUS, CLEPSYDRA, DROPSY, HYDATHODE, HYDATID. 6. Suffixed nasalized zero-grade form *u-n-d-d- in Latin unda, wave: UNDINE, UNDULATE; ABOUND, INUNDATE, (REDOUND), REDUNDANT, SURROUND. 7. Suffixed zero-grade form *ud-ro-, *ud-rd-, water animal, in: a. Germanic *otraz, otter, in Old English ofor, otter: OTTER; b. Latin Jutra, otter (with obscure /-): NUTRIA; C. Greek hudros, a water snake: Hyprus; d. Greek hudra, a water serpent, Hydra: Hypra. 8. Suffixed zero-grade form *ud-skio- in Scottish and Irish Gaelic uisge, water: USQUEBAUGH, (WHISKEY). 9. Suffixed o-grade form *wod-d- in Russian voda, water: VODKA. [Pok. 9. au(e)- 78.]
1128:wed-2, To speak. 1. Possibly oldest root form *awed- becoming *awed- in reduplicated form *awe-ud- dissimi- lated to *aweid-, with suffixed o-grade form *awoid-o- respectively in Greek aeidein (Attic aidein), to sing, and aoidé (Attic didé), song, ode (but more likely a separate root *aweid- becoming Greek *aweid-, to sing): ODE; COMEDY, EPODE, HYMNODY, MELODY, MONODY, PARODY, RHAPSODY, TRAGEDY. 2. Sanskrit vddah, sound, state- ment: THERAVADA. [Pok. 6. au- 76.]
1129:wedh-. To push, strike. Suffixed lengthened o-grade form *w6dh-eyo- in Greek dthein, to push: osmosis. [Pok. 1. uedh- 1115.]
1143:wer-3
1145:wer-4
1147:wer-4. To perceive, watch out for. I. O-grade form *wor-. 1. Suffixed form *wor-o- in Germanic *waraz in: a. Old English wer, watchful: wary; b. Old English gewer, aware (ge-, collective and intensive prefix; see kom): AWARE; C. Old English warian, to beware: WARE?. 2. Suffixed form *wor-to- in Germanic *wardaz, guard, and *wardén, to guard, in: a. (i) Old English weard, a watching, keeper: WARD; STEWARD (ii) Old English wear- dian, to ward, guard: WARDER?; b. Old North French warder, to guard: WARDEN; REWARD, WARDROBE; C. Old French guarder, to guard: GUARD; d. Anglo-Norman warde, guard: REARWARD?. 3. Germanic *ward in: a. Old English waru, goods, protection, guard: WARE}; b. Old English -ware (probably plural of waru, “goods”’), inhabi- tants (< “defenders’’): FIELDFARE. 4. Suffixed form *wor-wo- in Greek ouros, a guard: ARCTURUS. 5. Variant *(s)wor-, s(w)or- probably in Greek horan, to see: EPHOR, PANORAMA. II. Suffixed (stative) form *wer-é- in Latin veréri, to respect, feel awe for: REVERE!. [Pok. 8. wer- 1164.]
1148:wer-5. To cover. I. Basic form *wer-. 1. Germanic *wer- jon- in Old English wer, dam, fish trap: WEIR. 2. Com- pound form *ap-wer-yo- (*ap-, off, away; see apo-) in Latin aperire, to open, uncover: APERIENT, APERITIF, APERTURE; OVERT, OVERTURE, PERT. 3. Compound form
18331:hydro,  shortened  form  of  1 )  hydropathic,  2)  hydro¬ airplane',  3)  hydraulic  power.  —  See  hydro-. Hydrohates,  n.,  a  genus  of  birds,  the  true  stormy petrel  (ornithul.)  —  ModL.,  compounded  of hydro-  and  Gk.  fiirr.c,  ‘threading  on’,  from  the stem  of  fialvav,  ‘to  go,  walk’.  See  -bates, hydrobromic,  adj.,  pertaining  to,  or  designating, an  acid,  HBr  (chem.)  —  Coined  by  the  French chemist  Joseph-Louis  Gay-Lussac  (1778-1850) fr.  hydro-  (short  for  hydrogen)  and  bromic, hydrocarbon,  n.,  a  compound  of  hydrogen  and carbon  (chem.)  —  Compounded  of  hydro-  (short for  hydrogen)  and  carbon, hydrocele,  n.,  an  accumulation  of  serous  fluid; esp.  dropsy  of  the  scrotum  (med.)  —  L.,  fr. Gk.  j Spoxr/.y;,  which  is  compounded  of  uSiop, ‘water’  (see  hydro-),  and  xfjXvj,  ‘tumor’.  See  -cele. hydrocephalic,  adj.,  pertaining  to  hydrocephalus.
18333:hydrocephalous,  adj.,  affected  with  hydrocepha¬ lus.  —  See  next  word  and  -ous.
18334:hydrocephalus,  n.,  an  accumulation  of  serous fluid  in  the  cranian  cavity  (med.)  —  Medical  L., fr.  Gk.  u8pox£<p«Xov,  ‘water  in  the  head’,  which is  compounded  of  uScop,  ‘water’  (see  hydro-), and  xecpaXr},  ‘head’.  See  cephalic.
18335:Hydrocharis,  n.,  a  genus  of  plants  of  the  frogbit family  ( hot .)  —  ModL.,  fr.  Gk.  uSpoyapiqi;,  ‘de¬ lighting  in  water’,  which  is  compounded  of  uStop, ‘water’,  and  the  stem  of  yatpetv,  ‘to  rejoice’, whence  also  yapi.?,  ‘favor,  grace’.  See  Charis.
18336:Hydrocharitaceae,  n.  pi.,  the  frogbit  family  (hot.)
18338:hydrocharitaceous,  adj.  —  See  prec.  word  and -accous.
18339:hydrochloric,  adj.,  pertaining  to,  or  designating, an  acid,  HC1  (chem.)  —  F.  hydrochlorique,  coined by  the  French  chemist  Louis-Joseph  Gay-Lussac (1778-1850)  in  1814  fr.  hydro-  (short  for  hy¬ drogen)  and  chlorique.  See  chloric.
18340:Hydrochoerus,  n.,  the  genus  consisting  of  the capybara  (zool.)  —  ModL.,  compounded  of hydro-  and  Gk.  yoipop,  ‘pig’.  See  -choerus.
18341:Hydrocotyle,  n.,  a  genus  of  plants,  the  water pennywort  (bot.)  —  ModL.,  compounded  of hydro-  and  Gk.  xotuXt;,  ‘a  flat  cup’  (see  cotula, cotyledon);  so  called  in  allusion  to  the  cup¬ shaped  leaves  of  some  species.
18342:hydrocyanic,  adj.,  pertaining  to,  or  designating,  an acid,  HCN  (also  called  prussic  acid)  (chem.)  — F.  hydrocyanique,  coined  by  the  French  chemist Louis-Joseph  Gay-Lussac  (1778-1850)  in  [815 fr.  hydro-  (short  for  hydrogen)  and  cyanique. See  cyanic.
18343:hydrodynamic,  adj.,  pertaining  to  hydrodynamics.
18345:hydrodynamics,  n.,  the  dynamics  of  fluids.  —  See
18347:hydrofluoric,  adj.,  pertaining  to,  or  designating, an  acid,  a  compound  of  hydrogen  and  fluorine, HF  or  HjF2  (chem.)  —  Coined  by  the  English chemist  Sir  Humphrey  Davy  (1778-1829)  about 1814  fr.  hydro-  (short  for  hydrogen)  and  fluoric and  adopted  by  the  French  chemist  Louis-Jo¬ seph  Gay-Lussac  (1778-1850).
18348:hydrofoil,  n.,  a  kind  of  boat  that  travels  through the  water  on  wings  or  ‘foils’.  —  A  hybrid  coined fr.  hydro-  and  foil,  a  word  of  Latin  origin.
18349:hydrogen,  n.,  name  of  a  gaseous  element  (chem.)
18351:hydrograph,  n.,  a  hydrographic  chart.  —  Com¬ pounded  of  hydro- and  Gk.-ypatpoi;,  fr.  ypaupeiv, ‘to  write’.  See  -graph.
18353:hydrographer,  n.,  one  versed  in  hydrography.  — See  prec.  word  and  agential  suff.  -er. hydrography,  n.,  description  of  the  waters  of  the earth.  —  F.  hydrographie,  compounded  of hydro-  and  Gk.  -ypaepta,  fr.  ypa^stv,  ‘to  write’. See  -graphy.
18356:hydrokinetic,  adj.,  pertaining  to  the  motion  of fluids.  —  Compounded  of  hydro-  and  kinetic, hydrokinetics,  n.,  the  kinetics  of  fluids.  —  Com¬ pounded  of  hydro-  and  kinetics.
18357:Hydrolea,  n.,  a  genus  of  plants  (hot.)  —  ModL., formed  fr.  hydro-  and  -ol  (fr.  L.  oleum,  ‘oil’), hydrology,  n.,  the  study  of  water.  —  Compoun¬ ded  of  hydro-  and  Gk.  -Xoyia,  fr.  -Xoyop,  ‘one who  speaks  (in  a  certain  manner) ;  one  who  deals (with  a  certain  topic)’.  See  -logy.
18359:hydrolysis,  n.,  decomposition  of  a  compound through  the  addition  of  water  (chem.)  —  Com¬ pounded  of  hydro-  and  Gk.  Xiicu;,  ‘a  loosing, loosening,  setting  free;  dissolution’.  See  -lysis, hydrolytic,  adj.,  pertaining  to  hydrolysis  (chem.)
```


## [2026-10-16T05:13:49.852Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"URINE\" AHD_watkins1985.txt | cut -c1-900; grep -n -i \"wedh-\\|wed(h)\\|uedh\" AHD_watkins1985.txt | cut -c1-600 | head; grep -n \"Page(s): 78\\|Page(s): 80\\|Page(s): 1115\" POK_full.txt",
 "description": "Grep AHD for urine and wedh, Pokorny pages"
}
```


### [2026-10-16T05:13:50.204Z] TOOL RESULT

```
734:mahat-, great: MAHARAJAH, MAHARANI, MAHARISHI, MAHATMA, MAHAYANA, MAHOUT. [Pok. meg(h)- 708.] mei-'. To change, go, move; with derivatives referring to the exchange of goods and services within a society as regulated by custom or law. 1. Latin medre, to go, pass: MEATUS; CONGE, IRREMEABLE, PERMEATE. 2. Suffixed o-grade form *moi-t- in: a. Germanic *ga-maid-az (*ga-, intensive prefix; see kom), “changed (for the worse),” abnormal, in Old English gemdd, insane: MAD; b. Latin mitdre, to change: MEW!, MOLT, MUTATE; COMMUTE, PERMUTE, REMUDA, TRANSMUTE; C. Latin miituus, “done in exchange,” borrowed, reciprocal, mutual: MUTUAL. 3. Suffixed extended zero-grade form *mit-to- in Ger- manic “missa-, “in a changed manner,” abnormally, wrongly, in: a. Old English mis-, mis-: Mis-!; b. Old Norse mis(s), mis(s)-, miss, mis-: AMISS, MISTAKE; C. Ger- manic *missjan, to go wrong, in Old English missa
764:‘ mys), mouse: MOUSE. 2. Latin mis, mouse: MURINE,
1070:TAURINE!, TAURINE?, TAURUS, TOREADOR, TORERO, TAU- ROCHOLIC ACID. [In Pok. ¢éu- 1083.]
1151:*op-wer-yo- (*op-, over; see epi) in Latin operire, to cover: COVER, OPERCULUM. II. O-grade form *wor-. 1. Germanic *war-nén in Old English war(e)nian, to take heed: WARN. 2. Germanic *war- in: a. (i) Old French garant, warrant, authorization: GUARANTY (ii) Old North French warant, warrant, and warantir, to guarantee: WARRANT, (WARRANTEE), WARRANTY; b. Old French garer, to guard, protect: GARAGE; c. Old French g(u)arir, to defend, protect: GARRET, GARRISON; d. Old North French warenne, enclosure, game preserve: WARREN; e. Old French g(ujarnir, to equip: GARMENT, GARNISH. [Pok. 5. uer- 1160.] wer-S, Also wera-. To speak. Variant *wré-, contracted from *wreo-. 1. Suffixed zero-grade form *wr-dho- in Germanic *wurdam in Old English word, word: worD. 2. Suffixed form *wer-dho- in Latin verbum, word: VERB, VERVE; ADVERB, PROVERB. 3. Suffixed form *wer-yo- in Greek eirein, to say, speak: 
1156:wers-2. To be wet. Compare ers-2. Suffixed o-grade (causative) form *wors-eyo- in Greek ourein, “to make water,” to urinate, whence ouron, urine: URETER, URE-
1897:MUNIFICENT mei-1 MUNITION mei-3 MURAL mel-3 MURAMIC ACID mei-3 MURDER mer-2 MURE mei-3 MURINE mis- MURK mer-1 MURMUR mormor- MURRAIN mer-2 MURREY moro- Musca mu-2 MUSCARINE mu-2 MUSCLE miis- MUSE misum Muse men-1 MUSEUM men-! MUSH2 mu-2 MUSIC men-1! MUSKET mu-2 MusT! med- MUSTS ~=meu- MUSTACHE mendh-2
2342:TASTE tag- TATTOO! tap- TAURINE! tauro- TAURINE? tauro- TAUROCHOLIC ACID tauro- Taurus _tauro- TAUTO- to-
2437:UNITY oi-no- UNIVERSE 0i-no-, wer-3 UNIVOCAL wekw- UNKEMPT gembh- UNTIL ant- UNWITTING weid- UP upo UPANISHAD sed-1, upo UPBRAID bherek- UPROAR kere-, upO UPSILON bhes-! URCHIN ghers- UREDO eus- URETER wers-2 URETHRA wers-2 URETIC wers-2 URGE wreg- -URGY werg- -URIA wers-2 URINE wér- URO-! wers-2 URO-2 ors- URONIC wers-2 -UROUS ors- URSINE rtko-
305:au-‘4, To weave. Extended form *wedh- (< *awedh-). 1. Germanic *wédiz in Old English wed, wéde, garment, cloth: WEED?, 2. Germanic *wadlaz in Old English watel, watul, wattle: WATTLE. [Pok. 5. au- 75.]
470:euedh-. Udder. 1. Suffixed zero-grade form *idh-r in Germanic *ddr- in Old English adder, udder: UDDER. 2. Suffixed o-grade form *oudh-r in Latin dber, “breast,” with derivative adjective aber, fertile: (EXUBERANT), EXUBERATE. [Pok. éudh- 347.]
1039:s(w)e-. Pronoun of the third person and reflexive (refer- ring back to the subject of the sentence); further appear- ing in various forms referring to the social group as an entity, “(we our-)selves.” 1. Suffixed extended form *sel-bho- in Germanic “selbaz, self, in Old English self, sylf, self, same: SELF. 2. Suffixed form *s(w)e-bh(o)- in Germanic *sibja-, “one’s own,” blood relation, relative, in Old English sibb, relative: s1B; Gossip. 3. Suffixed form *se-ge in Germanic “sik, self, in Old Norse sik, oneself (reflexive pronoun), whence -sk, reflexive suffix, as in biiask, to make ones
1129:wedh-. To push, strike. Suffixed lengthened o-grade form *w6dh-eyo- in Greek dthein, to push: osmosis. [Pok. 1. uedh- 1115.]
1489:EXTRACT tragh- EXTREME eghs EXTROVERSION wer-3 EXTROVERT wer-3 EXTRUDE treud- EXUBERANT euedh- EXUBERATE euedh- EXUDE sweid-2 EXULT sel-4 EXUVIAE eu-! EYAS nizdo-
1999:os3 omeso- OSCINE kan- OSCITANCY kei-3, ds- OSCULATE 6s- OSCULUM 6s- OSMATIC od-' OSMIUM od-1 osmosis wedh- OSPREY awi-, ghend- OsSEOUS ost- OSSICLE ost- OSSIFRAGE bhreg-, ost- OSSIFY ost- OSSUARY ost- OSTENSIBLE ten- OSTEO- ost- OSTEOCLAST kel-1 OSTEOMALACIA mel-1 OSTIARY Os- OSTIUM 6s- OSTMARK aus-! OSTRACIZE ost- OSTRACOD ost-
2425:UBIQUITY kWe, kWo- UDDER euedh-
8299:Page(s): 78-81 
42871:Page(s): 782 
63997:Page(s): 780 
64023:Page(s): 781 
64065:Page(s): 780 
64091:Page(s): 781 
64161:Page(s): 781-782 
64177:Page(s): 782 
64187:Page(s): 782 
64217:Page(s): 782 
64239:Page(s): 782 
64282:Page(s): 783 
64302:Page(s): 783 
64324:Page(s): 784 
64355:Page(s): 785-786 
64369:Page(s): 786 
64468:Page(s): 781 
64511:Page(s): 784-785 
64590:Page(s): 785 
64633:Page(s): 783-784 
64681:Page(s): 788 
64707:Page(s): 789 
64731:Page(s): 789 
64745:Page(s): 789 
64759:Page(s): 789 
64843:Page(s): 787-788 
64859:Page(s): 788 
64871:Page(s): 789 
64887:Page(s): 789 
64951:Page(s): 787 
65651:Page(s): 805-807 
65671:Page(s): 807 
65705:Page(s): 807, 850 
65903:Page(s): 801-802 
65942:Page(s): 802 
65978:Page(s): 802-803 
66016:Page(s): 803-804 
66035:Page(s): 804 
66054:Page(s): 804 
66120:Page(s): 804-805 
66142:Page(s): 805 
66154:Page(s): 807 
66193:Page(s): 808 
66215:Page(s): 807 
66248:Page(s): 807-808 
66299:Page(s): 808-809 
66629:Page(s): 809-810 
88867:Page(s): 1115-1116 
93686:Page(s): 78
```


## [2026-10-16T05:13:53.229Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^wēr-\\|^wer- \\|^wér-\\|^wér\" AHD_watkins1985.txt | cut -c1-700; sed -n 8270,8300p POK_full.txt | cut -c1-600; echo ----; sed -n 88840,88870p POK_full.txt | cut -c1-700; echo ---; sed -n 93670,93690p POK_full.txt | cut -c1-400",
 "description": "Read AHD wer- and Pokorny entries"
}
```


### [2026-10-16T05:13:53.566Z] TOOL RESULT

```
1154:wéro-. True. 1. Germanic *wéra- in Old English wér, faith, pledge: WARLOCK. 2. Latin vérus (> Old French voir, truth), true, with its derivative vérax, truth: VERA- CIOUS, VERISM, VERITY, VERY; AVER, VERDICT, VERIDI- CAL, VERIFY, VERISIMILAR, VOIR DIRE. 3. Latin sevérus, grave, serious; regarded by some as a compound of se-, sed, without (see s(w)e-), and vérus, true, but the semantic difficulties make this explanation improbable: SEVERE; ASSEVERATE, PERSEVERE. [Pok. 11. yer- 1165.]



Middle Irish {*gwrass) /^5ss 'rain' is older fross {uros-ta, in spite of Pedersen KG. I 44); 
Hittite wa-ar-sa-as^ra\v\\l)seems an Old Indie loanword. 

Maybe alb. {*varsa-) vesa^6eW : {*heverse) sspari ' dew'. 

{* h2aursen-) ufsen-^ discharging semen = virile ', Old Indie vrsan- 'virile', m. ' manikin, 
man, stallion '. 

thereof derived Avestan 1/3/^5/73- 'virile'. Old Indie vrsa-, vrsabha-'buW, i/Zs/?/- 'virile', m. 
"Aries, ram' (= Avestan varasni-6s.), vrsana-m. ' testicles '; 

Specht (Dekl. 156) places here (from Germanic *gwrai-njan-) without s^extension Old 
High German reineo^ stallion ', Old Saxon wrenioAs., Old English wraene^ horny, lustful '; 
Old High German wrenno^ stallion ' is back-borrowed from Middle Latin (under the 
influence of common Celtic -ns-, -nt- > -nn-). 

uerse/i-:\-aWv\ {*gverres) verres, -/is'boar', Lithuanian i/eAS/is'calf, Latvian versis^ox, 
rother, cattle'. 

References: compare in general Persson root extension 47, 85 f., Johansson KZ. 30, 418, 
IF. 2, 60 ff., Persson Beitr. 604 f., 845 (also against connection of ^ers- with ers-). About 
Finnish vesi, stem i/e/e 'water' s. Mikkola Mel. van Ginneken 137. 

WP. I 252 f., 268 f., WH. I 81 f., Pokorny Urillyrier 93, 105, 159, 169, Specht Dekl. 18 f., 
Trautmann 20, 334, 337, Schwyzer Gr. Gr. I 519, 548, 838. 

Page(s): 78-81 

----
Iterat. Lithuanian vadz/dt/an6 vadyti, Latvian i/aoV'/'guide, lead', and i/ao'a/'hin and her 
guide, lead'; about Lithuanian vaduoti, Latvian i/ao'^d/'auslosen, loskaufen'; see above S. 
1109; Old Church Slavic vozdg, i/ooV// "guide, lead'. Old Russian voditi zenu^eiue Frau 
heimfijhren'. 

In addition probably ued-mno-, the word for the purchase price the bride: 

Gr. £5vov (for *F£5vov with Spir. asper after *F/7a5uq 'pleasant'), hom. PI. ££5va ' bride- 
price or wedding-gifts '; but also ' dowry of the parents', £5v6aj, hom. ££5v6(ji) ' to promise 
for wedding-presents, to betroth ', hom. ££5vu)Tr|c; ' a betrother; (the daughter equipping) 
father of the bride ', av-a£5vo(; ' without bride-price; also of the husband, bringing no gifts 
'(a[F]£5voc; and £[F]£5vov with a and £ as suggestion vowels); 

Old English weotuma, wituma, wetmam. ' purchase price of the bride'. Old Frisian 
wetma, witmads., Burgundian wittemo. Old High German widomo, widemo ' dowry' , Middle 
High German wideme, widem. Modern High German Wittum(\v\ addition Old High German 
widimen. Middle High German widemen, by/o''/77e/7'ausstatten'. Modern High German 
widmen); gr. Slavic -no- maybe from -mno- and with dem Germanic -men-siem 
comparable; dubious Old Church Slavic veno^6o\Nry, payment for the bride', whether from 
*uedno-, compare also *uesno-\ 



doubtful alb. vigje 'gift to the wedding, to the birth of children, by the construction of a 
house' {ued(h)-l-l). common alb. -dz- > -gl-, -gj-. 

References: WP. I 255 f., Trautmann 344, Vasmer 1, 177, 182, 212, Frisk 442 f. 
Page(s): 1115-1116 

Root / lemma: ueA'^-S 

---
Avestan avisMv. 'apparent, manifest, obvious, vorAugen' (npers. 55/ra/' 'clear, bright'; Old 
Indie avistya-h, Avestan 5K/sy5-'offenkundig'); Old Church Slavic ave, jave Mn. 'kund, 
apparent, manifest, obvious' (in ending after den Adjektivadverbien auf -e reshaped from 
*avb, whereof:) aviti, javiti^ reveal, kundmachen, show' (Lithuanian di/y//s'sich in Traume 
sehen lassen' loanword from dem Slavic). 

Maybe alb. ya 'there it is' Slavic loanword 

full grade: gr. aia6avopai, Aor. aia6£a6ai 'perceive' (*aFia-6-); Latin a^o'/o'hear' from 
* auiz-d^-io, compare oboedio\xo'C(\ * 6b-avizdhid aboui *oboTdid\ gr. dico (neologism to 
Aor.£TT-riia(a)a, aiov) 'vernehme, hear' (*aFia-), £naiaTO(; 'belongs, ruchbar, known'. 

Here probably Hittite u-uh-hi^\ see, observe', a-us-zi' sees ', 3-^-/7-/5 (from a-'u-wa-ri-is) 
'Ausschau, Warte', iterat. ^s/r- 'wiederholt sehen'. 

References: WP. I 17, WH. I 80, Trautmann 21, Pedersen Hittitisch 172 f. 
Page(s): 78 

Root / lemma: ba>^mb-, b^a>^irio^-, paf^mp-, phaf^mfj^- 

Meaning: to swell
```


## [2026-10-16T05:13:56.726Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=8000 && NR<=8299' POK_full.txt | grep -n -i -E \"lemma|meaning|hydor|ud.r|unda|voda|uisce|urina|water|wet|winter\" | cut -c1-300 | head -50; echo ----; awk 'NR>=88760 && NR<=88845' POK_full.txt | cut -c1-400",
 "description": "Read Pokorny au̯ed- and u̯edh- entries"
}
```


### [2026-10-16T05:13:57.326Z] TOOL RESULT

```
1:Meaning: to flow, to wet; water, etc. 
29:The zero grade of Root/ lemma: ak^a-'yNater, river' has been suffixed in nasalized -{n)dor, 
33:heteroklit. r/n-sievn uedor, u6ddr{Hov(\. Sg.), uden(i) {Lok.Sq.), udnes{Ger\. Sg.) " water', 
41:Old Indie {* h2aunatti-)unatti {*u-n-ed-ti), 3. PI. undatr soaked, moistened '; Avestan 
42:vaidi-t " water run, irrigation canal '. 
44:Old Indie udan{i) Lok., udnahGen., udaNom. Akk. PI. " water' (Nom. Akk. Sg. udaka- 
45:m)\ from /'-stem derived samudra-h' sea ', anudra-h^ waterless ' (= gr. avu5po(;); 
47:{*h2audro-)udro-s^ water animal ': Old Indie udra-h^ a water animal ' = Avestan udra- m. 
54:uisce {*udeskio-) ' water '; 
60:(a)hueda- > voda, zero grade in Phrygian (a)kuedu> p£5u [common Greek g"'> b, k"'> p\. 
62:Armenian {*gwet) geV river ' (basic form *uedd, Sandhi form to uedor, compare under 
63:Slavic voda; it corresponds also Phrygian p£5u "water', i.e. Veo'Jfrom *uedd, Kretschmer 
70:Maybe Phrygian psSu "water' : nasalized lllyrian B/ndus 'water god' [common lllyrian gu- > 
77:Gr. u5u)p, u5aT0(; (*u5-n-T0^) "water' (with metr. elongation 05u)p); from /--stem derived 
78:avu5po(; " waterless ', uSpoq, u5pa " water snake ', £vu5pi(; f. " otter ', u5apr|(;, u5ap6(; " 
79:watery ' (u5aA£0(; ds. with suffix exchange; similarly uAAoc; " water snake, ichneumon ' : 
80:uSpoq = lak. eAAq : £5pa), u5£po(; " dropsy ', u5pia " water bucket ' (: Latin utef)\ from n- 
81:stem (compare u5vr|c; " watery ') derived DAAoau5vr| actually " sea wave, wave, the billow 
89:e5-stem to u5o(; "water' is only late poet. Norn. Akk. to Dat. u5£i. 
95:nevertheless, from *udcR). 
97:The shift -dn- > nj > jo\ possibly alb. {*udna-h) uje, ujna PI. " water ' has also been attested 
98:in alb. shtynj, shtyj'poke, push' {*studnid)\ see Root / lemma: (s)teu-1\ "to push, hit' 
100:Luwian wvi/a- "watery' 
110:Latin unda, f. " water, fluid, esp. a wave; fig. a stream of people ' (with n- infix from the 
111:present; compare Old Prussian {*gwundan) wundanu., undsxw. "water' and Old Indie 
112:unatti, undatias well as Lithuanian {*gwandud) vanduo, -ens, vandenj, zem. unduo, 
113:Latvian udensm. f. "water', and in addition Schuize EN. 243, Brugmann Grdr. I|2 3, 281, 
114:283, Trautmann 337); uter, utris' hose, tube ' {*udr/-s'* water hose ', compare gr. u5pia), 
117:Umbrian utum. "water' (= uSojp), Abl. une{*udni). 
119:Old Irish u{/)sce 'water' {*udesk/o-), odar' brown ' {*udaros), co/n fodorne' otters ' 
120:("water dogs '). 
124:Old Irish u(i)-sce: alb. {*u-i-) uj-e, uj-fwater' : Luwian u-/-fa-an-ta-a/-//-an ' oi the water(s)' 
127:Gothic watoin-stem), Dat. PI. watnam 'water'; Old Swedish vgetur{ge= Indo 
134:"water"; 
136:Old Icelandic otr. Old English otor. Old High German ottarm. "otter, water snake', in 
138:unda) probably Gothic wintrus. Old Icelandic vetr. Old English winter. Old High German 
139:Old Saxon wintar^ winter ' as " wet season ' (Liden PBrB. 15, 522, Falk-Torp under vinter, 
144:shaped from Old Icelandic vatr. Old English wset, engl. wet' wet, soaked '. 
159:Old Church Slavic i/oo'a "water' (become Fem. because of the ending -a, here for Indo 
161:attuning well in the meaning, s. Meillet MSL. 14, 342, Trautmann 337); 
163:Hittite wa-a-tar {* watar) "water'. Gen. ue-te-na-as {e-grade as Phrygian p£5u, a of Nom. 
171:common Armenian Celtic lllyrian * hue- > gw- > g-{see Root / lemma: uek"-: to speak]. 
176:na-a^ which became the zero grade wa-a-tar {* hwatar) 'water'. 
178:c) ^h2auer-) auer- " water, rain, river ' {uer- : Or-; to the ablaut Persson Beitr. 604, Anm. 
181:1. uer-, uer-:0\6 Indie var, variu. "water', Avestan varu. "rain' (with themat. inflection 
182:Iran. Avestan var^ to rain ', med. " allow to rain, let rain '), Old Indie vani. "water', Avestan 
185:Truncated Tocharian (^hwatar) A war, B M/a/'"water'; 
193:gr. perhaps in apuoo " scoops ', if *Fap u[a](jo (see *aus-^ scoop, draw water, ladle '); 
224:Armenian ^ntp (gour) ' water ' : alb. (*^/) uje' water '. 
226:Old Norse i/a/7m. " liquid, water '. 
----
in addition Old High German wibilm. 'beetle, chafer, Kornwurm'; Old Saxon wivil. 
Middle Low German wevelAs., Old English M///fe/' Kornwurm', Old Icelandic V/Min tordyfiil 
'Mistkafer', Old English wibba^Ro^kaief; Lithuanian i/5i6'5/5S 'beetle, chafer', vabuolas 
ds., zem. i/5/?c»/e 'Mistkafer', Latvian i/ai7^c»//5 'beetle, chafer' (besides East Lithuanian dial. 
vobuolas^beeWe, chafer', zem. vambo/e, Latvian vambale, vambuole^U\s\kaief). 

References: WP. I 257 f., WH. II 733, Trautmann 336, Vasmer 1, 176; 



See also: moreover: ued- 
Page(s): 1114-1115 

Root / lemma: ued^-l 

Meaning: to push, hit 

Material: Old Indie vadhati, avadhTt^hW, bump, poke, destroy', Kaus. vadhayati, vadha-xx\. 

"killing, Mordwaffe (esp. from Indras projectile); blow, knock, annihilation ' = Avestan vada- 

m. "wedge zum Spaltendes Holzes', Old Indie vadhar-v\. "Mordwaffe (esp. from Indras 

projectile)' = Avestan vadar- n. "weapon (for hitting)', i/ao'/7/'a/77"Lederriemen', Old Indie 

vadhasna-m. ds., Avestan i/ad/a/a-'zuriJekstoften' (lengthened grade as gr. cbGsu)); 

gr. £0£i cpGEipei. spsGi^si Hes., hom. eGojv "pushing, thrusting, zerwijhlend', sGsipa " hair 
of the head, mane'; wGeu) "poke, push' (: Avestan vadaya-), wok; " shove ', evoaic; " tremor 
' ( *en-uo6!^-tis)\ also in svoaixGojv, £vvoaiYaiO(;, £ivoai(puAAo(; (svv-, £iv- metr. lengthening); 

Old Indie vadhri-^ castrated ' ("with zerstoftenen testicles') = gr. sGpic; Topiac;, Kpioc; 
Hes.; secondary iGpK;, aGpi(;; 

Lithuanian vedega^a kind of axe', Latvian vedga^EisayX, crowbar'. Old Prussian 
i4/eo''/gc»"Zimmerbeir, Old Irish /o^yi? "Waffenbeute' {*uo6'^-uo-)\ is also Avestan vadayan- 
"EN eines glaubensfeindlichen FiJrsten' as "axe, Schlager' to deuten? 

ein s/r-present seems Irish /^/sc- "press', mcymr. gwascu, bret. gwaska ^'^ress' (certainly 
ablaut d\d). 

References: WP. I 254 f.. Frisk 446 f., 449 f. 
Page(s):1115 

Root/ lemma: ue6y-2, vor Nasalen ued- 

Meaning: to lead 

Material: Old Indie vadhu-i. "bride, young wife, woman', Avestan va5u- ds., vaSayeiti 

(Kaus.) "leads, zieht', with upa- "eine Frau zur matrimony give', with us- "(Frauen) 

entfijhren, rob', KaJ/ya-"heiratsfahig (from girl)'; 

Old Irish /eo'/io'" leads, goes, carries, brings ', mcymr. go-di-wawd^ overtaken ', Old Irish 
to-fed-, to-dhfed- 'gu'\de, lead', cymr. arweddu 'gu'\de, lead, bring', Verbalnom. mcymr. 
arwein {*are-ued-no-), cyweddu^ guide, lead, wohin bringen ', Verbalnom. cywain {*kom- 
ued-no-), cymr. dy-wedd'i'o^ marry', corn. d-om-ethy6s.. Middle Breton d-im-iziff, nbret. 
dimizT marry, get married '; 



Lithuanian vedu, i/es//"lead, guide; marry (of liusband)', Latvian vedu6s., Prater.-stem 
* uede- in Old Prussian wedde, Lithuanian vede, Latvian dial, i/eo'eand Old Church Slavic 
vede-ase; Lithuanian vedys " suitor ', vedeklis " marriageable, young man', nau-veda, - 
vedys^ bridegroom ' (' leading home anew '), Latvian vedekle^ daughter-in-law ', vedama 
"bride'; 

Maybe alb. {*vashta) vashe , vajze, varshe {* vadeSf young girl, virgin ' common alb. -d- > 
-l-,-r-,-J-- 

Old Church Slavic vedg, i/es//"guide, lead', seldom 'marry'. Iter, voditi, (but Old Church 
Slavic nevesta 'bride' rather ' the stranger ', as ' die noch nicht HeimgefiJhrte ', Vasmer 2, 
206); 

Note: 

Old Church Slavic: nevesta^bu6e, daughter-in-law' [fa] derived from Lithuanian nau-veda, 
-vedys ' bridegroom ' 

Iterat. Lithuanian vadz/dt/an6 vadyti, Latvian i/aoV'/'guide, lead', and i/ao'a/'hin and her 
guide, lead'; about Lithuanian vaduoti, Latvian i/ao'^d/'auslosen, loskaufen'; see above S. 
1109; Old Church Slavic vozdg, i/ooV// "guide, lead'. Old Russian voditi zenu^eiue Frau 
heimfijhren'. 

In addition probably ued-mno-, the word for the purchase price the bride:
```


## [2026-10-16T05:14:01.068Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=8000 && NR<=8299' POK_full.txt | sed -n '1,4p;176,215p' | cut -c1-300",
 "description": "Read Pokorny au̯er- section"
}
```


### [2026-10-16T05:14:01.642Z] TOOL RESULT

```
Meaning: to flow, to wet; water, etc. 

Note: 

na-a^ which became the zero grade wa-a-tar {* hwatar) 'water'. 

c) ^h2auer-) auer- " water, rain, river ' {uer- : Or-; to the ablaut Persson Beitr. 604, Anm. 
2). 

1. uer-, uer-:0\6 Indie var, variu. "water', Avestan varu. "rain' (with themat. inflection 
Iran. Avestan var^ to rain ', med. " allow to rain, let rain '), Old Indie vani. "water', Avestan 
vairi-xw. "sea'; 

Truncated Tocharian (^hwatar) A war, B M/a/'"water'; 

Armenian gayr marsh, mud ' {*Uerio-)\ 
Note: 

The origin of labialized Old laryngeals: 
common Armenian Celtic lllyrian *hue- > gw- > g-. 

gr. perhaps in apuoo " scoops ', if *Fap u[a](jo (see *aus-^ scoop, draw water, ladle '); 

alb. (after Jokl SBAk. Wien 168 I 30, 89, 97) {*gvrende) vrende^ light rain ' (/?/- 
participle); 

Note: 

The origin of labialized Old laryngeals: 

common Armenian Celtic lllyrian *hue- > gw- > g-. 

alb. hur-de, hurdhe^ pond, tank, marsh ' {*ur-), shure^ urine ', shurre {* surna) (postverbal) 
f. " urine ' (prefix s/7from Latin ex or Indo Germanic *srn + ur-ne\ or + gr. oupsu)?); 

Note: 

Albanian preserved the old laryngeal h- > s- like satem languages alb. {* surma) shurra " 
urine ' : Hittite sehur " urine ' : Latin urma' urine '. But in alb. hur-de^ pond, tank, marsh ' 
alb. preserved /?- laryngeal like centum languages. 

cymr. gwerr^. " suet, sebaceous, tallow '; 

Note:
```


## [2026-10-16T05:14:05.404Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; grep -n \"\\[pdf page\\|^\\[\" WLD_Bd1_pages.txt | head -3; grep -n -i \"udeskio\\|uisce\\|unda\\b\\|vadhú\\|vadhū\\|vaδu\\|vaδay\\|vadu\\b\" WLD_Bd1_pages.txt | head -20",
 "description": "Grep Walde-Pokorny volume 1"
}
```


### [2026-10-16T05:14:05.726Z] TOOL RESULT

```
4082:[Ungliicklich iiber Uodal usw. Grienberger 104; s. dagegen auch Uhlen-
4936:[MQfia'iQCO „schimmere“).
12196:[Diss. 71], Pedersen aaO.); got. ara, aisl. orn, are, ags. earn, ahd. aro am,
11588:               got. niunda, ahd. niunlo, anord. nionde     as. nigundo nigudo,
11596:afries. niugunda, ags. niyjda (s. o.), lit. devintas, apr. neivlnts, aksl. devqfo.
18365:PBrB. 15, 504. van llelten IF. 18. 102 an,                                                                 dalier *jugiinpl, aber *jmvunda,
18371:         g°b junda)                      =
19398:                              ahd. nhd. as. ags. maid, Subst. ahd. wunda                                                                   ,
22385: gaffen“, vypsau -dti „mit offenem Munda dastehen. gaffen“ (Endzelin aaO.:
23626:      Lat. undo.      „Welle, Woge“. undarc „wallen, wogen“ (vgl. apr. tv unda n
23631:Bgm. II 2 3, 281, 283, Trautmann Bsl. Wb. 337; da6 unda nach Bgm.
23652:ahd. oitar m. „Otter“ (s. o.); mit Binnennasalierung (vgl. o. zu lat. unda,
23677:      Im Germ auch mit p aisl. nnnr, udr, pi. nnnir „unda“, as. uthia. Mia.
33403:2.    qal- „schon, gesundA
34274:verstarkende aisl. hand- z. B. hund-diarfr „ndv-To).uo?“, d. i. Part. *liunda —
44204:hormtngr horn fest), ai. kunda- m. „bei Lebzeiten des Mannes mit einem
44210:Geliebten gezeugter Sohn‘‘ ist wohl = kunda.- n. „rundes GefaB“ usw.,
54511:Unordnung“, 1'um/a „Klumpen. Ball, KloB'       Icunda  .kneten, zusammen-
55948:    Anders, aber nicht fiberzeugend fiber germ, gunda- Trautmann ZfdWtf.
55949: 7, 268   zu av. gunda m., gunda f. „kleines, rundes Brot“, npers. gundeh
59828: „Widder' (ghldu -), hunda m. „Widder, Hausschwein , hunda „das Knistern
59839: fallig anklingenden hunda, s. auch Uhlenbeck Ai. Wb. 361 u. huduk auch
62263:  Lat. grunda „aztyg“, suggrunda ,,Dachstuhl      s. Yf. LEWb.
```


## [2026-10-16T05:14:08.940Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; sed -n 23560,23680p WLD_Bd1_pages.txt | grep -n -i \"au.ed\\|ir. \\|uisce\\|usce\\|aksl\\|voda\\|wint\\|aued\\|vgl\\|\\[pdf\\|W.11\" | head -30; grep -n \"^uedh\\|^2\\. u.edh\\|u.edh-\" WLD_Bd1_pages.txt | head",
 "description": "Locate WLD au̯ed- and u̯edh- entries"
}
```


### [2026-10-16T05:14:09.296Z] TOOL RESULT

```
15: v6go?,         ahd.      usw.                    ottar,       vgl.            auch        lat.       lutra             und     mit u lit. itdra, aksl.
16:vijdra         ds.):     von einem                            -(<•).?- St.              (vgl.         gr.          to       vdo?) ai. atsa-h „Quelle.
19:Sandhiform zu uedor vgl. got. urdo, slav. voder, ihr entspricht auch das
67:      Lat. undo.      „Welle, Woge“. undarc „wallen, wogen“ (vgl. apr. tv unda n
76:[*udri-s „ * Wasserschlauch", vgl. gr. vdota Thurneysen KZ. 32, 563), Ultra             :
83:      Mir. oss„Wasser“ (Fick II 4 268) existiert nicht; hierher air. u(i)sce „Wasser-
85:i*udes-kio- !); mir. fund„Trane“?? (ibd.). falls existierend. bliebe fern.
89:(o-St. geworden. vgl. got. dat. pi. tvafnam), vatr, nord. Seename ViHtern:
93:ahd. oitar m. „Otter“ (s. o.); mit Binnennasalierung (vgl. o. zu lat. unda,
94:wahrscheinlich got wintrus aisl. vetr, ags. winter, ahd. as. ic intar ..Winter
102:besser zu ir. find ,,weiB‘ s. u. sueid ,.glanzen“)
110:wasch       (    oder zu ir. false- „driieken‘\ meymr. gwascu ds., wobei
115:das Praes. den brit., das Praet. den ir. Vokalismus widerspiegelte: s. u.
27499:   uredh-. urodh- scheint mit tier- „erhohte Stelle" auch yerild „AYurzel" ?               (
29694:uedh- „fiihren, heimfiihren                             .
```


## [2026-10-16T05:14:11.831Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; sed -n 29690,29710p WLD_Bd1_pages.txt | cut -c1-200; awk 'NR<=29694' WLD_Bd1_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -1; awk 'NR<=23626' WLD_Bd1_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -1",
 "description": "Read WLD u̯edh- entry and page tags"
}
```


### [2026-10-16T05:14:12.428Z] TOOL RESULT

```
                                                                            ££
                                                                                 ,

                                                   ££
uedh- „fiihren, heimfiihren                             .



  Fick I 4 133. Curtius 322. Yanieek 279.
  Fraglich bleibfc es, ob lat. vilis ,/wohlfeil, von geringem Werte ££ unter
irgendeiner Bedingung hierherzustellen sei, da bisher keine zweifelsfreie
Erklarung und Etymologie gefunden ist. Tiber die verschiedenen Versuche
vgl. Yf. LEWb. 2 837.


ill-    in Schallworten.

                                                              (fid), lal, ‘ig „Ausruf der Freude oder des
                                                             1
   Gr. id, jon.             trj   „Ruf, Schrei'
                 ££
```


## [2026-10-16T05:14:16.185Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; grep -n -i \"Braut\\b\\|„Braut\" WLD_Bd1_pages.txt | head; ",
 "description": "Grep WLD for Braut"
}
```


### [2026-10-16T05:14:16.558Z] TOOL RESULT

```
23848:     rudhu-h „Braut, junge Frau; Sehwiegertoehter“. av. radii- ,,Weib.
23881: tochter“, sedama „Braut“;
23883: bysth     wurde heimgefiihrt“ (aber aksl. n crista ,,Braut“ eher ..die Ln-
23898:      Dazu wohl das Wort                        fur    den Kaufpreis der Braut.
23907:Freier die Braut erwirbt; aber auch Aussteuer der Eltern an die zu ver-
23913:ausstattende) Yater der Braut'                      ,
23924:     Ags. WL otwnawihima, wctmam. „Kaufpreis der Braut*', afries. wetmu , led-
29227:(Deutung als .,Braut", *uedh-ta, zu *uedh- ,uxorem ducero" wiire lautlich
32934:„Kastchen mit den Utensilien der Braut"; got. Minins usw. „Himmel"
48330:gleichsam einstreuen", daher ^gvoonaoxog „goldgestickt", naoxdq „Braut-
```


## [2026-10-16T05:14:19.067Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; sed -n 23840,23860p WLD_Bd1_pages.txt | cut -c1-200; awk 'NR<=23848' WLD_Bd1_pages.txt | tr -cd '\\f' | wc -c; awk 'NR<=23626' WLD_Bd1_pages.txt | tr -cd '\\f' | wc -c",
 "description": "Read WLD u̯edh- bride lines, count leaves"
}
```


### [2026-10-16T05:14:19.569Z] TOOL RESULT

```
vielleicht ahd. wascan „waschen“ (s. Pedersen IvG. II 515; oder letzteres
zu TFos.w, s. *ued „netzen“?).


2.    uedh „fiihren; heimfiihren, heiraten (vom Manne)“.
     rudhu-h „Braut, junge Frau; Sehwiegertoehter“. av. radii- ,,Weib.
      Ai.
Frau  vadayeiti (Kaus.) „fiihrt, zieht, schleppt". mit upa- „eine Frau zur
         1
             ',


Ehe geben“, mit vs- „(Fraueni entfiihren, rauben“, vadrya- ..heiratsfahig
(von Madchen)“:
      air.              (Formenbestand bei Pedersen KG. I 515 f., wo auch
                  fedul „fiihrt“
iiber die  Scheidung von Zugehorigen der Wz. *nedh- „binden“), cymr. ar-
 iccddu ,,fiihren, bringen“, cyiveddu „fiihren, wohin bringen“, cymr. dy-icrdd'io
263
261
```


## [2026-10-16T05:14:24.639Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"vaδū\\|vadū\\|vaδu-\\|vaSu-\\|vadu-\" BRT.txt | head; grep -n -i \"wayūg\\|wayug\\|wayūdā\\|wayudan\\|wyūk\\|wywk\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head; grep -n -i \"bayug\\|bayūg\\|bajūg\\|bejug\\|bēyūg\\|bayog\\|bayōg\" HRN.txt HUB.txt | head",
 "description": "Grep Iranian sources for bride words"
}
```


### [2026-10-16T05:14:24.945Z] TOOL RESULT

```
HUB.txt:7086:'Mitte' = paz. phi. miyan, zd. maiSyqna^ ; bayd, bayog 'Braut'
```


## [2026-10-16T05:14:27.355Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 7080,7092p HUB.txt; grep -n -i \"Braut\" BRT.txt HRN.txt | head -20; grep -n -i \"bride\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head",
 "description": "Read HUB lines and grep Braut/bride"
}
```


### [2026-10-16T05:14:27.710Z] TOOL RESULT

```
mU Min. Gl. 140, g. frnd, bal. mUd^ mid, nb. mldy also ap.
*muda' ? ; sSi 'Gatte = ap. *xSauSa- ? ; maig *Heuschrecke
(neben malax) = phi. maig (und malak Bdh. 47, 10), bal.
maday, madax, arm. marax, zd. mataxd-; patg *Bote* =
syr. W^B, phi. paik, arm. payik, skr. padika- (s. oben p. 45
— 46)Vjp»y^rfa *Pussganger' = skr. paddti-y padatika-; miyan
'Mitte' = paz. phi. miyan, zd. maiSyqna^ ; bayd, bayog 'Braut'
= skr. vadhu^; beva 'Wittwe == phi. vevak, zd. Mava,
skr. vidhavd-; zBr unten* = paz. ai-er, phi. Sr- in Srtany
Ertkan PPGl. p. 9 aus "^ayar = zd. adairi (s. § 58, b)';
drdstan *in Ordnung bringen, schmticken', pr. arayam, pai-
rdstan *zurichten', ^v. pairayam^), Wrzl. rodh^), vgl. ap,
r^to- nchtig, zd. raSaiti; ayJna 'Spiegel', bal. Od^k, Od^n,
HRN.txt:2657:264. beyoj^beyök 'Braut*, :V2 (Jer. 16, 9).
HRN.txt:2658:ai. <^ergl. vadhü- 'Braut' ; kurd. buk.
HRN.txt:2903:harsn 'Braut' (H. No. 161).
BRT.txt:11717:(ASf.)  il  vS  *sp3r3ds  nivarllnl  "die  hier (oämL  die  Braut)  will  ich  .  ."  Y.  S3- 4.  b)  adjektivisch,  nur  b)  im  jAwr.; azfwt  yd  ahurS  maztia  ..yas»  tat  nmätam äkffVfUM  srlrsm  .  .  V.  22.  i ;  —  tUtrtm  .  . yS  vispuil  namizaiti  (sd.)  simä  . ,  vispäs3 lä  damqn  iag/axyatica  YtS.^^.  U)  in schwachdeiktischer  Verwendung  'dieser, der,  er';  I)  auf  Zuvorgenanntes,  Voraus- gehendes (Wort  oder  Satz)  zurück- weisend (öfters  auch  zugleich  voraus- weisend); r)  auf  ein  Substantiv  oder  subst Pronomen;  a)  adjektivisch;  a)  im  gAw.: '"^(Sp.  618  u.)  mlidam  ..yastat  mJid)m hamtna  (sd.)  nSii  däitt  Y,  44. 19;  —  ahmät *mainyius  .  .,-  täcä  (IS.)  sjvntä  mainyS .  . tä  (Sp,  614  u.)  da  spinta  mainyü  .  .  Y, 47.4—6;  —  nachgestellt:  akyä  magahyä ,  .  ivTzayäira  (sd.)  magpm  tSm  at  .  .  Y. 5j.  7.  B)  im  jAw.:  vate  .  .  aai  t^m lähm  .  .  *uigrfml>ayS  H.  2.  8,  z6;  V.  2. 30,  Vyt.42;  — ya.r?.dräjS  .  .  aiäkh  z>mö anaihya  .  .;  mäca  . .  tarn  zqm  käraym  . .; VOSS  .  .  tarn  anyqm  (Sp,  136  o.)  sqm karaytn  V.  6.  i  f.;  —  nara  . .  taica*  nars' V.7.  J3f,;  2.  41;  — ysi  pa^a  U3^r?nte.. tat  tä  pai:a  frayqn  ..  V.  Ä  14;  15;  — äf>ö  .  .  aai  tä  äp3'*/railvayeiti  Yt<^'8£; V.  ly.  loj  —  s^arm^  .  .  yat  ufaahaiat .  . zarai:ultr?m  .  .  yeti/ie  tat  ä^annS  isat mairys  .  .  Yt/p.  78-82;  56^;  —  Aan/a- maram  .  .;  ä  ial'  kanjamatum'  ,  .  V. 2. aot; — *a/ ta^ (Sp.6i8  o.)  dqma ..? a^lai taj  dqma  V.  13.  \t;  —  mayalibyS  . .;  ava lä  anya  maya  W.Q.i<i-^i.  <t)  in  Ver- bindung mit  ima-  (Sp.  370  m.):  namSnli..; *vUqs  *tä£a''>  imä  t^mSnxS parStoita  ,  . rfx»»«  Yt. /.  I5-I9'  Anhang.  Das  Be- zugswort ist  vorher  nicht  ausdrücklich genannt,   aber  durch  die  Situation  ange-
BRT.txt:22427:PPM.,  lu  ai.  vadali  'er  sprichl*.  ~  Pü.;  äiä- iJA,  nach  der  geringwertigen  Lesart  vtud'.  — >)  Der  Sprecher  der  Strophe  ist  wie  überall in  Y.  S3  ausser  in  Str.  4,  die  das  Geldbnis des  Bräutigams  enthalt,  der  Brautvater,  Zara- %iistra.  Bei  Gdn.s  Deutung  von  vad',  KZ. 28.  191,  104  als  "(ich)  der  heiratende"  -  äbn. lieh  schon  JusTi  -  muEste  auch  Strophe  5 dem  Bräutigam  in  den  Mund  gelegt  werden; das  passt  aber  nicht  zu  deren  Inhalt. j.  vaiii  F,  12:  lies  saiit,  s.  laiiyä-.
BRT.txt:22429:ai.  vadhu-  f.;  np.  vgl.  bayög  'Braut'.  Vgl,  va- irya-.  —  ■)  Nach  dem  Musler  der  T-Slämme (lu  S  409:  vgl.  S  407\
BRT.txt:30212:the  ceremonial';  aber  die  Braut  in  Y.  jj  ist  doch
PHD.txt:308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
PHD.txt:419:kābēn [%”fyx! | N kabin] marriage-portion, dowry (assigned to the bride). kabig [Rpy&! | N kab/pi] monkey.
PHD.txt:1087:bridegroom damad.
NYB_vol2_glossary.txt:4513:zastan [zstn'] to beg a thing of (hac) a p.: pt. = pret. pass. 3d p. sg. tzast 5718, — Av. (487) gad-, pres. jadiya-, jaiöya-, pt. jasta-; MPrs zstg 'bride' (A-H II).
NYB_vol2_glossary.txt:4557:been married to Artaxsér) 9??, 1014 (twice). — Wikander, Mb 9-21. A love scene between a bridegroom (mérak, q.v.), twenty years old, and his bride (ztyānak), fifteen years old, is told in PR 91 sq.
PHD_mackenzie.txt:1860:damad [d'm't I M d'm'd, N ,...,] bridegroom, son-in-law.
PHD_mackenzie.txt:1862: ,...,ih: condition of a bridegroom, son-in-law.
PHD_mackenzie.txt:3113:kaben [k)j)yn' I 'N kiibin] marriage-portion, dowry (assigned to the bride).
PHD_mackenzie.txt:6080:boldness wistaxih.                     bridegroom damad.
```


## [2026-10-16T05:14:31.475Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"bride\\b\\|wayu\\|wayü\\|wayū\" PHD_mackenzie.txt | head; grep -n -i \"wayuk\\|wayūk\\|wayük\\|wayok\\|wyywk\\|wywk\" NYB_vol2_glossary.txt PHD_mackenzie.txt | head; sed -n 22420,22430p BRT.txt | cut -c1-1200",
 "description": "Grep MacKenzie/Nyberg for wayūg and read BRT entry"
}
```


### [2026-10-16T05:14:31.803Z] TOOL RESULT

```
3113:kaben [k)j)yn' I 'N kiibin] marriage-portion, dowry (assigned to the bride).
5277:Zway [w)d = Av. wayu- I P wyw] air, atmosphere•
*346
arm.    gil    'fluss';     PDw.     v5d    'Kanal'.     —
•  j.,  g.  vadar-  n.  'Waffe  (zum  Schlagen)': yasla  'dar!  vSisdai  aläuns  "und  der  die Waffe  wider  den  Rechtgläubigen  erhebt" Y._j2.  lo;  —  paifi  .  .  kihrpim  .  .  haoma . .  'dar}  /ai\i^'>  "gegen  den . .  Leib  schlag . . die  Waffe"  Y.o.  30;  30—32*,
Vgl,  vada-  und  vädäya:  —  ai,  vidhar-  n.  (bes. von  Indrai  Waffe).  —  PS-  (lu  Y,  32):  hacai pa  ptAlikik  ösiin  dal  ö  oAravän,  (lu  Y,  9); paltäklne  (SQ.:  paraiäiaya)  lanän,  erl,;  ia! iärai  api  gäw,  —  ')  VgL  jahi  vädhak  RV.  4. i%.  9.
•  j.  vaSairyav-"  Adj.  'nach  Begattung veitangend,  brünstig',  vom  Kamelhengst'': uitrS  'rii^^  Yt.i4.39;  12;  —  uÜrahe hhrpa  'ryaol  Yt  i^.  n ;  *F.  8;  —  uitr&nh5 .  .  p»r3tamna  (sd.)  'ryavd  Yt, /7. 13,
PPA,  (Saqp.  4),  aus  •i^iaiVj'i- den.  Praes.  31 ; s.  i'oJü-.  —  ai.  vgl.  vadküyäv-  Ad],  (und  vadhar- yäniim  RV.  /.  161.9?);  Gdn.  3Yt  68,  —  Pu.: vaharn),  Npii.:  xabar  dar  n  rik  däHnnda.  — •)  NA.  auLh  •lar:  —  >)  VgL  zBed.  Yt,  14.11 mit  7,  15.  —  J>  Sta(t  'ryiä  geschr.,  S  2öä  14-
•  g.  vad^mna-  Adj.  'zuredend,  mahnend': süx^Sal  vatyamnähyS  kainibys  mraomi xsmaiiyica  'nU  "Lehren  künde  ich  den heiratenden  Mädchen  und  euch  (den Freiem),  mahnend"  Y.jj,  5"'.
PPM.,  lu  ai.  vadali  'er  sprichl*.  ~  Pü.;  äiä- iJA,  nach  der  geringwertigen  Lesart  vtud'.  — >)  Der  Sprecher  der  Strophe  ist  wie  überall in  Y.  S3  ausser  in  Str.  4,  die  das  Geldbnis des  Bräutigams  enthalt,  der  Brautvater,  Zara- %iistra.  Bei  Gdn.s  Deutung  von  vad',  KZ. 28.  191,  104  als  "(ich)  der  heiratende"  -  äbn. lieh  schon  JusTi  -  muEste  auch  Strophe  5 dem  Bräutigam  in  den  Mund  gelegt  werden; das  passt  aber  nicht  zu  deren  Inhalt. j.  vaiii  F,  12:  lies  saiit,  s.  laiiyä-.
•  j.  va8ü-  f.  'Weib,  Frau":  'lu  (NS.)'> wöaz-fl  (sd)  F.  2  f.
ai.  vadhu-  f.;  np.  vgl.  bayög  'Braut'.  Vgl,  va- irya-.  —  ■)  Nach  dem  Musler  der  T-Slämme (lu  S  409:  vgl.  S  407\
•  j.vaSut-  f.EN.  eines  gläubigen  Mädchens; kanyä  *'%utö''>  asaonyh  Yt/J.  141.
```


## [2026-10-16T05:14:35.686Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \".\\{200\\}zur  Ehe.\\{200\\}\\|.\\{200\\}zur Ehe.\\{200\\}\" BRT.txt | head -5; grep -n -i \"Rudak\\|رودکی\" FRS_pages.txt | head -2; grep -n \"بیوگ\\|بیوک\" FRS_pages.txt FRS.txt | head; grep -n \"بیوگ\\|بیوک\" BQT_v1_pages.txt | head",
 "description": "Grep BRT marriage, FRS and BQT for bayūg"
}
```


### [2026-10-16T05:14:36.227Z] TOOL RESULT

```
785:          ‫ولندی‪ » ۸‬چنانکه رودکی گفت ؛‬
833:                                  ‫گفت ‪:‬‬        ‫ابله بود | چنانکه رودکی‬
FRS_pages.txt:12161:‫‪ ۸-0۰‬آورنگ تخت باشدوزیبایی ‪۰‬‬        ‫س‪:‬بوك عروس بود و بیوکانی عروسی ‪۰.‬‬
FRS_pages.txt:21925:                            ‫بیوگانی"‬
FRS.txt:11162:س:بوك عروس بود و بیوکانی عروسی .۰ ۰0-۸ آورنگ تخت باشد وزیبایی ۰ 
FRS.txt:19658:بیوگانی"
```


## [2026-10-16T05:14:38.559Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 12150,12175p FRS_pages.txt; echo ----; sed -n 21915,21935p FRS_pages.txt; awk 'NR<=12161' FRS_pages.txt | tr -cd '\\f' | wc -c",
 "description": "Read Loghat-e Fors bayūg entries"
}
```


### [2026-10-16T05:14:38.909Z] TOOL RESULT

```
 ‫‪ - ۱‬ل ‪ :‬مرك ببکاروکارسخره بود س‪ :‬مجرك بیکاربودوسخره‌چه بقهروچه‌بخوشی؛‬
 ‫‪-‬ین‬
   ‫روسخره باشد ‪.‬‏ د‪۲‬ر‪-‬لن‌ترتیب دومصراع مقلوب است ‪ ۴۰.‬ا‬
                                                     ‫چب‪:‬کمارك‬
                                                            ‫ب‬
‫‪ - 6‬ن ؛ سترك سر کش ولجوج ونندبود» چ‪ :‬سترگث‬            ‫پیت را چچ اضانه دارد‬
 ‫لجو ج باشد وبی‌آزرم وتند ‪ .‬س (مثل‌متن) ‪. .‬ه ‪-‬ن « رودکی »«س نکاویمنده‌را‬
‫‪-‬عنتلمتن )‪ ۰‬چ و‬
              ‫؛شد ‪ ۰‬چ اگر رادمردینباشد ‏ ‪( ۷‬‬
                                           ‫‪٩‬‏ ‪-‬ننبا‬                   ‫ندارد‬
‫‪ ۸-0۰‬آورنگ تخت باشدوزیبایی ‪۰‬‬        ‫س‪:‬بوك عروس بود و بیوکانی عروسی ‪۰.‬‬
‫ن‌‪:‬شهیچ «گرز گران‬
                ‫چشولسمتن) ‪-٩ ۰‬س‏ ‪.‬مهی‪۱ ۰‬ط‪۰‬و‪-‬س‬
                                            ‫(‬
                                               ‫‪۹۷۳‬‬
                                                                ‫اول ‪ :‬ضد فراخ بود‪»۱‬‬
                                                                     ‫دوم ‪ :‬تنك اسب »‬
                                                                         ‫سوم ‪ :‬جوال »‬

                                               ‫چهارم ‪ :‬خروارشکر" [فرخی کفت ‪:‬‬
                                           ‫در ابیلناد فزون دارداز هزار کلات‬

        ‫بهر يك اندر دینار تتگهابرتنکث ‪]۳‬‬
                                                                       ‫دجم ‪ ٍ:‬د‬
                                                     ‫کروفه [ هجيث گوید ‪:‬‬
----
‫شعرخوارزمی با شعر تولامانی‬                        ‫نامه مانی بانامه توراز است‬
  ‫پیش‬   ‫یره‪:‬‬
           ‫شد‬‫ن در حاشبه مثل متن ‪ ۰. ۰‬ح‪-‬الن‬            ‫‪۳‬‬      ‫‪ ۲‬و ‪ ۲‬فقط در چ ‪.‬‬
‫درحاشه ‪ ۰‬يك‌سی بتبارگی‬     ‫‪۸‬‬       ‫‪ - ۷‬فقط در چ‬      ‫‪ ۱‬چ »ما‬        ‫*‪ -‬چ ‪:‬بدا‬
                          ‫‪ -‬ففط در چ ‪.‬‬        ‫‪۰‬‬    ‫‪٩‬‏ ‪ -‬ال در حاشبه ‪ :‬خود‬    ‫دود‬
                                          ‫کلهکردن باشد » لیببیگفت ‪:‬‬

                          ‫باده خجورو مستی کن"مستی چهکنیاز غم‬
‫دانی که بهاز "مستی صد راه یکی مستی‬

                            ‫بیوگانی"‬
              ‫عروسی بود و بیوك عروس را خوانند » عنصری گفت ‪:‬‬


‫هم بر آبین و دم یونآنی‬                    ‫ساخت آنکه یکی پیوگانی‬
                                  ‫بر‬
     ‫لعات ذیل متحصراً در حاشیه ن آمده و سایر نسخ از آنها خا(مند ‪:‬‬



                                 ‫يا ؛ي‬
297
```


## [2026-10-16T05:14:43.048Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=558 && NR<=566 {print \"=== leaf \" NR-1; print}' BQT_v1_pages.txt | grep -n \"===\\|بیو\\|vadh\\|wayu\\|بیوگ\\|بیوک\\|بیوه\" | head -30",
 "description": "Search BQT vol1 leaves for bayūg"
}
```


### [2026-10-16T05:14:43.397Z] TOOL RESULT

```
1:=== leaf 557
48:=== leaf 558
99:=== leaf 559
149:=== leaf 560
206:=== leaf 561
223:بی نمکی کر دن - کنابه از بیوفایی
258:بوده است همزه را ببایدل کرده اند بیوباربدن
266:=== leaf 562
271:بروزن پی‌فشرد ۴. ماشی بیوباربدن است‌.هنی نا
283:بیو درك ع با ثانی مجپول بر وزن‌بی‌درد»
290:میخواندماند. و نام اصلی او بیور بر وزن صبور
301:بیو‌سنفه -_بنتح اود و سکون نون»
321:افموی که دور به‌بیوسی بگذشت
328:۴ مخفف ابیون » رك : افیون .
329:=== leaf 563
333:است که بیوفابی کردن باشد .
368:=== leaf 564
396:=== leaf 565
```


## [2026-10-16T05:14:45.762Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==563 || NR==564 {print \"=== leaf \" NR-1; print}' BQT_v1_pages.txt | head -150",
 "description": "Print BQT leaves 562-563"
}
```


### [2026-10-16T05:14:46.313Z] TOOL RESULT

```
=== leaf 562
نبویرد
شده است واوباریدتن بفتح همزه بمعنی
فرو بردن و بلم کردن باشدا . ۱
ایو بر ك ع بکس اول و ضم بای ابچد
بروزن پی‌فشرد ۴. ماشی بیوباربدن است‌.هنی نا
جاویده فرو برد و بلم کرد , وبمی مصدر عم
که ناجاویده فرو بردن باشد ؛ و در
اين لفت نیز همزمرا بیا بدل کرده اند همچو
بانداخت که بشداخت شده»وامثالاین بسیاراست٩‏ .
تیوه » بکس 4 و فتح الث بروزن
زبور» بمعنی ده هزار است؟ - ونام‌ضحالك ماران
هم نت واو را و و ستجقیف
سور خوانشد لیکن صاحب فرهنگه باین معنی
ختح اول و ضم ثانی آورده است - و گردکان
و بادام و بته را نیز کفنه‌اند که معزآنها تیز
و ضایم شده باشد .
بیو درك ع با ثانی مجپول بر وزن‌بی‌درد»
نام مبارزی است که افراسیاب بمدد پیران وسه
فرستاد- و نام‌شهرست درخراسانمتهوربباورد۴ .
1
و وجه تسمیه‌اشآنکه پیش از پادشاهی ده هزار
اسپ داشته است و بزبان دری سور بروزن یور
بمعی ده هزار باشد واو را باین اعتبار بدین نام
میخواندماند. و نام اصلی او بیور بر وزن صبور
ت چنانکه گذشت
دوس <« بنتح ود بروزن‌عروی ۰ طمع
وی ام
چا
و خواهش و امیدوامیدواری باشد بجیزی از هر
نوع که بوده باشد - و بمعنی تواضع وچاپلوسی
و اتظار هم آمده است٩‏
۱ لبق سل با دال ابجد بروزن ضرورت.
مشتق آزیوسیدن است یمنی طمم کند و امیدواد
دد ۹
بیو‌سنفه -_بنتح اود و سکون نون»
بمعنی نواضم و چایلوسی کننده‌ب‌اشد وامیدوار
شده را نیز کوند۸
یو سیفن - بر وزن‌خموشیدن» بمعنی
امید داشتن و امیدوار گردیدن وطمم کردن-
و چاپلوسی نمودن باشده .
واو وکاف فارسی » بمعنی عروس است ونم اول
وبای فارسی ح آمده است*٩.‏
یو گانی » با کاف فارسی بر وزن
جیوشانی » عروی را کوند چه بوک بمعنی
عروی باشد و در موبدالفضلا» بجای حرف ثانی
تونآورده است
یو گندن پکر اول و فتح لا
چه در لغت بواز 1 می‌باید٩۱.‏
لبون » بفتح اول بروزن زبون؛ ترباك
وافیونرا کویند؟۱- وبعربی‌چاههای عمیق‌وسیم‌را
؟ - بپلوی 98۷۵۲
کجا سور از پهلوالی شمار
۴ رك؛ باورد و اییورد.
پیوسی بعنی انتظار بهی و خویی :
افموی که دور به‌بیوسی بگذشت
۷ رگ : بوسیدن .
تن ۱ص ۲۵۱>»:
بود در زبان دری ده‌هزار . فردوسی‌طوسی.
٩‏ - و به
تین کت از ۱
0- ره : او کندن و او فکندن .
۴ مخفف ابیون » رك : افیون .
=== leaf 563
۳۳
خوانند .
لیو ث » بر وزن ربوند » بمعنی غدر:
است که بیوفابی کردن باشد .
ی ۵ » بروزن هیوه» بمعنی غرمب وتنها
باشد - وزنی را نیز کویند که‌شوهرش مرده‌باشد
با او را طلاق داده باشد - ومحردیرا یز گویند
که زش حرده باشد - و نام داروبی است که
بر که آن سر که کیرماند اما خار تدارو و ی
آن بخیار شباهت دارد(۱) لیکنکوچکترازآن
باشد وآنرا بمربی قثاء البری‌خوانشد وقتاءالحمار
همان‌است .
بیهله ۴ - بکسر ارل و ضم ها بروزن
دل شده , مخفف بهوده است و معنی نا حق
و باطل باشد» چههده بممنی حق است.- ویمعنی
بی نفم هم‌آمده است و جح اول جامه‌ای را
(۱) خم ۰۳ چك : بخبار دراز .
۹ را اقرب الموارد : بین.
بیهوده
کویند که از حرارت آتش زرد شده باشد .
دیق بنتح اول و اكث وسکون ثالی
و قاف » دام شهریست غیر معلوم۴ .
یهن بکراول بروژن‌سجن, خاریشت
بز رکه تیرانداز را کویند یعنی خارهدای خود را
ماشد تیراندازد .
لیهو ۵ - بقثح او بر وزن فرسود »
چیزبرا کون د که نزدبك بسوختن رسیده وآتش
آلرا زرد کرده باشد - و بکسر اول هم آمده
2 ۱
یو ذه - بکس اولبر وزن فیروزه:
بمعنی بیپده است که نا حق و باطل باشد -
و بممنی پی نفع هم آمده است - و بفتح اول
جامه ای را کویند که نزديك بسوختن رسیده
باشده .
۴ - مرب بیهگه
۴ رك : بیپوده ۲
بیپنه ویهوده..
۴ رله ؛
```


## [2026-10-16T05:14:49.762Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py BQT:342 --image 2>&1 | tail -15",
 "description": "Render BQT page 342 image"
}
```


### [2026-10-16T05:14:50.170Z] TOOL RESULT

```
no scan of BQT covers printed page 342 (see 'scans' in refs_online.json)
```


## [2026-10-16T05:14:53.855Z] TOOL CALL #27: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p528; cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p528; curl -sL -o bqt562-528.jpg \"https://archive.org/download/borhan-ghate-v1/page/n562_w1200.jpg\"; file bqt562-528.jpg; ls -la",
 "description": "Download BQT vol1 leaf 562 image"
}
```


### [2026-10-16T05:14:55.815Z] TOOL RESULT

```
bqt562-528.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1240x1754, components 1
```


## [2026-10-16T05:14:57.664Z] TOOL CALL #28: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p528/bqt562-528.jpg"
}
```


### [2026-10-16T05:14:57.719Z] TOOL RESULT

```

```


## [2026-10-16T05:15:01.888Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr; ls | head; ls BQT 2>/dev/null | head -5; ls BOOK 2>/dev/null | head -3",
 "description": "Check OCR cache directory layout"
}
```


### [2026-10-16T05:15:02.223Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--  368k sfmqrb 14 Oct 22:19  0001.png
.rw-r--r--  1.7k sfmqrb 14 Oct 22:19  0001.txt
.rw-r--r--  534k sfmqrb 14 Oct 22:19  0049.png
.rw-r--r--  2.7k sfmqrb 14 Oct 22:19  0049.txt
Permissions Size User   Date Modified Name
.rw-r--r--   96k sfmqrb 14 Oct 22:19  33.png
.rw-r--r--   99k sfmqrb 14 Oct 22:19  39.png
```


## [2026-10-16T05:15:04.073Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr; ls BQT | grep -v \"^[0-9]*\\.png$\" | head; ls BQT | grep vision | head -3",
 "description": "List BQT OCR cache non-png files"
}
```


### [2026-10-16T05:15:04.395Z] TOOL RESULT

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
.rw-r--r--  522k sfmqrb 14 Oct 22:46  0456.jpg
.rw-r--r--   576 sfmqrb 14 Oct 22:30  0143.vision.txt
.rw-r--r--   849 sfmqrb 14 Oct 22:45  0339.vision.txt
.rw-r--r--  1.0k sfmqrb 14 Oct 22:46  0456.vision.txt
```


## [2026-10-16T05:15:09.761Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; cat 0339.vision.txt; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p528/bqt562-528.jpg 0342.jpg; cat > 0342.vision.txt <<'EOF'\nBQT vol. 1, printed p. 342 (archive.org borhan-ghate-v1, leaf n562), read from page image for PDF page 528 (root Wedh 1).\n\nبیوگ - بفتح اول وضم ثانی وسکون واو وکاف فارسی ، بمعنی عروس است وبضم اول وبای فارسی هم آمده است(۱۰).\nبیوگانی - با کاف فارسی بر وزن جیوشانی ، عروسی را گویند چه بیوگ بمعنی عروس باشد و در مؤیدالفضلاء بجای حرف ثانی نون آورده است .\n\nFootnote 10 (Mo'in): = بیو ، سانسکریت vadhû (عروس) «اسفا ۱ : ۲ ص ۴۴۴» ، اوستا vadh + upa (ازدواج کردن) «اسفا ۱:۲ ص ۴۳۶».\nEOF\nls",
 "description": "Save BQT p.342 image and vision transcript"
}
```


### [2026-10-16T05:17:10.558Z] TOOL RESULT

```
Command did not complete within its 120s timeout and was moved to the background (ID: bso0z6zmg). Output is being written to: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tasks/bso0z6zmg.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/sfmqrb/git/rishe-private; directory changes made by the backgrounded command do not apply to subsequent commands.
```


## [2026-10-16T05:17:13.428Z] TOOL CALL #32: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tasks/bso0z6zmg.output | head; ls -la /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/0342*",
 "description": "Check background output and saved files"
}
```


### [2026-10-16T05:17:13.833Z] TOOL RESULT

```
[BQT vol. 1, printed p. 339 (archive.org borhan-ghate-v1, leaf n559); read from image]
بیکم - بفتح اول و کاف تازی و سکون ثانی و میم، صفه و ایوانرا گویند. *
...
footnotes (Mo'in):
* بیک - ترکی beg، عثمانی bey، قرقیزی bî یا biy؛ عنوانی است که بشاهزادگان و نجباء داده میشد، امیر قبیله‌ای کوچک (در برابر خاقان یا خان که رئیس قبیله‌ای بزرگ بود) - رؤسای سپاه. «دائرة‌المعارف اسلام».
* بیگانه - پهلوی bêgânak «اسفا ۱:۱ ص ۲۸۴»، نیز bêgânik «منلس ۲۶۹: ۲».
* بیگم - بفتح اول و ضم سوم، ترکی Begum ملکه مادر، بیوه زنی ارجمند، بانو «دائرة‌المعارف اسلام».
Permissions Size User   Date Modified Name
.rw-r--r--  221k sfmqrb 16 Oct 01:15  /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/0342.jpg
.rw-r--r--   700 sfmqrb 16 Oct 01:15  /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/0342.vision.txt
```


## [2026-10-16T05:17:17.280Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"\\bwife\\b\" SOD_pages.txt | head -20",
 "description": "Grep Sogdian dictionary for wife"
}
```


### [2026-10-16T05:17:17.691Z] TOOL RESULT

```
13656:     lady, wife                                                                         GMS 957, 1511; BBB 751 f34; VJ; TSP; BSTBL,
13665:     lady, wife
15290:                                                                   TSP  6.165;wife
19111:        {name c/)Suda:*an*s wife
22487:       wife(>v/r/i full-right marriage)                                 protecting from evil
23447:                                                                  co-wife ©Av. hapadnk °ss- bln% MP >bwg
32431:     C2, 48V 17 n p95                                                    wife
32500:       wife                                                                  waf te, wapde ©pp. ^w^-, wpt'k, wfc
37940: confessor 2285, 2324                        0tf)control   557                      co-wife 6876
39135:                                                                                   prince's wife   4070
39571:stream     9566                            Sudashan's wife 5390                    suspended       147
39893:wife 3462, 3464, 6536, 9955, 9968         with golden leg 11573                      with wind-feet  9886
```


## [2026-10-16T05:17:20.559Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 32420,32510p SOD_pages.txt | cut -c1-220; awk 'NR<=32431' SOD_pages.txt | tr -cd '\\f' | wc -c",
 "description": "Read SOD entries near wife"
}
```


### [2026-10-16T05:17:20.881Z] TOOL RESULT

```
                                                                      j   wcytwS'r- =4 wyend'r-
                                       Ub.^^L
     wicayde ©<*wi-caxta ^wy^ytk, wc'wytk                            9954 wcyty M, S                          ^yU cJl ^J
     intelligent                                                         wicite (wcyt>k) ©pp.; pi. -t
      BSTBL, Vim. 49, Dhu. 172, 247, Dhu. 243;                           chosen, electus
          wc'wYtk, Dhu. 80: GMS 219                                      GMS 213 n 2, 1242; BBB f81; MSP bl96
9942 wc'ywt'k => wc'wytk                                           9955 w6-      B, M                         (^%-)<-jj<0j
9943 wc}q C                                                              wa/a/uS (wd-) ©wu6 <waSw-<*wadu
     wacak, ucak       ^wt's'k, ^c'q                                       <*wad-\ Khwar.wwd; Skt. vadhu ©nom. -w;
     tomorrow
                                                                           ob. -yh, -y\ pi. -yyst =»w5-w
     C2, 48V 17 n p95                                                    wife

9944 wc}r B                                                              GMS 408, 506 n 1; C2 pl97; wSyK gen. VJ 350
     wicar                                         '/■
                                                                          etc.; TSP 8.185; abl. GMS 1181; VJ 24d, 823;
     discussion                                                           gen. wdy\ C2, 91V8; nom. ace. wd-n>, C2 gloss.
     TSP 1226 n p224; TSP 9.146                                           p229; Benv. ^vad-, HitUE. 36; Livsic.
                                                                          SogdJaz. 1981, 424
9945 wc'rt    B                                  +J* <«-?tvtf
                                                     cTJ'          9956 wd-      C => w5-
     wicart =>wyc}rt
     exactly, right                                                9957 wd*s =* wyd>s
                                                                   9958 w8'y ^ w5y
     VJ 932; BSTBL, Dhy. 54, 166
9946 wcNvytk       B                              Ob i^yXt         9959 wa^S      B, S =* w8y6(5)

     wicayute ?, wicuyde ? (wc'ywt'k) ^wc'ytk/y,                   9960 w6*yr- B              d^J^f iq*J'<z~*j* <o*^pJ*z
                                                                        wi8er- ©<*widdraya-y Sdar- =*w5rt-,
       wydwyt'k
     intelligent, wise                                                    wyS'yr-, w5yr}mndy(yh)
 403
                                                                                                                       wy'pty'kh
        (rearrange, (readjust                                            9972 w5y     B, S                     (jy> ^~> >0M
        Sogdica. 60.30                                                         wiSe, oSe ? (w8>y, wdy, w5yy) ©*awada\ Av.
                                                                                 avaSa ^wSCh)
 9961 wS'yst B, M                         o\^&<&j
      waSist, w^5ist ©pi. =*w8-w, wySysth                                     there
      wives                                                                   EGSii 153; GMS 136; VJ 1120, 1400, TSP 2.243,
       SCE 55; Hen. Tales. 486.5, 7; GMS 1186                                   478 etc.; BSTBL, Dhy. 295; Frag. 2a.l9; STi
                                                                                33.10; STii p599; BSTii 92, 173; C2 p229;
 9962 wSjJ'yt => wy8P>yth                                                       wSyyy Tales. 471.9; KG 2056; MSP bl5, 28
 9963 wfikp'yt B                               c-o^o^                    9973 w8y8(8) M, B, S                                 l^T
      wiSpit, wiOfit ? (wySpyt)     ©pp.   =»wySp}y-                          wiSeS (wS^S, w8yy, w8yy8(8))
      distant                                                                 there
       VJ 187; GMS 219, 293
                                                                              VJ 265; Sogdica. 50.7; GMS 119a, Hen. Cosm.
9964 w8krn>k S                    ^ jl oi~ «uIu*p                               307.4, 312.80; TSP 3.169, 182, 193, 224, Frag.
     waSkarane, wu8-karne ? ©Skt. karana                                      . Len. 29.6, 61.5; KG 384, 597; MSP b!9, 39, 162;
                                                           Of
       marriage contract                                                        MDii p214
       MDii p22.17 n p38; *wadu-karanaka; Gersh.                        9974 wSyr'mndyCyh) M                  jJij^t^s
         Advice. p91
                                                                             wi8eramande ©Av. viSdrayeiti =»w8}yr-
9965 w8rt-     M                                                             adjustment
                                                        O^J'^Ca
       wi5art ©pt. su pres. wdyyr-                                           BBB736, GMS 1100
       (fc>)arrange
       GMS 836, 857                                                     9975 wdywt C = w+ dywt =» w-, 8yw*
                                                                        9976 wSyy M =» w8y, w8y8(6)                                   *-**
9966 wSrtyy     M
                                                                        9977 w5yy8(8)     M -* w8y8(8)                        <iil>
       wi8arte ©pp. =»w8}yr-, wSrt-            C-J jA   '* it* A*,'.?   9978 wfc C
       arranged
                                                            O^jJ
       GMS 857                                                                wafc ©f. pp. ^zyrnwfc, wftyy, wpt}k
                                                                              woven
9967 wdrz-     C                                                              STii 526; GMS 274; AVS 109
       wi6/larz (wlrz-) -»wyr*rz-
                                                                        9979 wfcmbd      C = w+ fembd «» w-, fcmbS
       (/cOtremble, (ro)shake
                                                                                                                              <G&
       STi 54.16; GMS 60n 1; wlrz-, STii 2.1                            9980 wfr' M
                                                                             wafra ©f. n. ace. ->; loc. wfry} =*wpr-h
9968 w8-w   M               (jy> ^* j->)<=rjj«jj
                                                                             snow
     wa/u6u (wd-w, w6w(h)) ©A v. vadii\ Ved.
                                                                             GMS 311, 1175; BBB 496 p57, 577 p72
         vadhu ©pi. w6*yst\ nom. ace. wSw% ob. wdyh/\                   9981 wftyy M
         wSwyh *»w8-
       wife                                                                  waf te, wapde ©pp. ^w^-, wpt'k, wfc
                                                                             woven
       EGSii 86, GMS 560n 1, 955; S W, C2 pi 15, 197;
         nom. Hen. Tales. 470, 59: C2, 66R14, 87R6, 12;                      GMS 274, 1674; Gersh. Sogd. Cpds. 1945, 151
         VJ 285 passing TSP 2.150, 1116, 1229; BSTBL,                   9982 wfwx'r     C = w+ fwx*r =» w-, fwx*r
        Vim. 61, 69; Anc. Lett. 324-, Hen. Magi. 138.7;
                                                                        9983 wY^m S                  <*& j>t^ «£> jjaS*
        ace. Tales. 480, 18; VJ 1136, 1177; SCE 129,
                                                                             uyam, wiyam (wy}m2) ©<*wi-gama- =»wY}my,
        300, 309; TSP 2.1116, 12.29; Anc. Lett. 2.54, C2,
        13R27, 87R10, 102V3; ob. wSwK VJ 401; SCE                            fore ign, land
469
```


## [2026-10-16T05:17:25.662Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"wyw[kg]\\|wayog\\|wayōg\\|wayög\\|bayög\\|bayōg\\|wēyōg\" PHD_mackenzie.txt NYB_vol2_glossary.txt NYB_vol1.txt HRN.txt CHEUNG.txt | head; grep -n \"بیوگ\\|بیوک\" ../refs/incoming/ARY/ARY_pages.txt MON_part1.txt | head",
 "description": "Grep MP and Persian sources for wayūg/bayūg"
}
```


### [2026-10-16T05:17:25.963Z] TOOL RESULT

```
MON_part1.txt:27350:بیوک: ۰0۷۲۲ [تر.] (ص..) بزرگ» مهتر. 
MON_part1.txt:27356:بیوگ: و5(« [- بیو - ویو - ویوگ. 
MON_part1.txt:95875:همسری دختر یا زنی با مردی) بیوگانی.
```


## [2026-10-16T05:17:28.453Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 27354,27360p MON_part1.txt; sed -n 2650,2662p HRN.txt; grep -n -i \"^wa.*bride\\|wayu\\|wayo\" PHD.txt | head -5; grep -n -i \"bride\" PHD.txt | head",
 "description": "Read MON and HRN entries, grep PHD"
}
```


### [2026-10-16T05:17:28.830Z] TOOL RESULT

```
بیوگ: و5(« [- بیو - ویو - ویوگ. 
عروس» ازدواج کردن] (.) عروس. 

بیوه: (0-)0]۷2 (ص. .) زن شوهر مرده با 
زنی که شوهرش او را طلاق داده باشد؛ مرد 
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
27äd setzt ein ap. ^päta- (Suffix ta- wird bekannt-
lich auch gelegentlich zur Bildung von Nom. ag. ver-
649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
419:kābēn [%”fyx! | N kabin] marriage-portion, dowry (assigned to the bride). kabig [Rpy&! | N kab/pi] monkey.
1087:bridegroom damad.
```


## [2026-10-16T05:17:33.092Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"wayo\\|wyd.tk\\|wayōt\\|wēyōt\" NYB_vol2_glossary.txt | head; grep -n -i \"bride\" CHEUNG.txt | head -5; grep -n -i \"wadʰ\\|*wad-\\|wad¹\\|wadH\" CHEUNG.txt | head",
 "description": "Grep Nyberg and Cheung"
}
```


### [2026-10-16T05:17:33.637Z] TOOL RESULT

```
13625:*NWIR: NP bayo ‘bride’, Kurd. Бок ‘bride, daughter-in-law’, Zaz. veyv (Ё) ‘bride’, 
13626:Bakht. bahig ‘bride, daughter-in-law’ 
13630:*bride-price' || (+ *ati-) Sariq. diwoö-, düwoö-/diwust, düwust (old caus.) ‘to cause 
13636:*SANSKRIT: vadhü- (f.) ‘bride, young woman’ (RV+) > EWAia II: 497 
14887:*BACTRIAN: Cup- (pret. stem) ‘to request (as a bride)’ || (+ *a-) ayaAyo ‘wish’ 
ugrep: error: error at position 12
(?mi)wadʰ\|*wad-\|wad¹\|wadH
           \___empty (sub)expression
```


## [2026-10-16T05:17:35.283Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 13600,13640p CHEUNG.txt",
 "description": "Read Cheung entry on *wad"
}
```


### [2026-10-16T05:17:35.614Z] TOOL RESULT

```
IMPV. 2sg. ‘zw’y-; Partic.: ‘zw’st; Inf.: ‘zw’st 

*KHOTANESE: LKh. *bad- (byä-) ‘to produce’, bay- (caus.) ‘to lead’ || (+ *ati-) OKh. 
ttuvay- (tvay-) ‘to convey across’ || (+ 4-) OKh. *avad- (äva-) ‘to obtain’ || (+ *uz-) 
uysba(y)- ‘to lead out’ || (+ *para-a-) LKh. *pravay- (prravas-, prravas-) ‘to lead 
over, convert’ || (+ *ni-) nva(y)- ‘to grasp’ — SGS: 93 f., 39, 11, 62 

*SOGDIAN: (+ *pati-) MSogd. ptwyó (caus.) ‘to hand over’ 


*HuadH 201 


Caus.: pres. IMPV. 2pl. MSogd. ptwyöt (M139 R.4(54) = BBB: 50) 

*CHORESMIAN: w’zy- (caus.) ‘to lead to, to let go; chase away ?’ || (+ *ati-) cw’zy- 
‘to lead into [+ w]; to lead out from [+ d]’ || (+ *para-) p’rw’zy- ‘to lead, carry away’ 
|| + *para-a-) pr’w’zy- ‘to lead, take away’ || (+ *pari-) prwz- ‘to become’, prw’z- 
(sec. caus.) ‘to let (it) become into’. Ф Depending on the meaning(s) assigned, a 
derivation from *(H)uaé ‘to leave behind, let’ or *uaz “to drive (a chariot)’ for w’zy- 
cannot be excluded. = Samadi: 210, 52, 155 f., 150, 155 f. 

*BACTRIAN: onA- ‘to lead, take, bring; exert’ || (+ *pari-) mopooato ‘fared’ = S-W, 
Bact.: 212b 

*NWIR: NP bayo ‘bride’, Kurd. Бок ‘bride, daughter-in-law’, Zaz. veyv (Ё) ‘bride’, 
Bakht. bahig ‘bride, daughter-in-law’ 

*NEIR: Pash. -wal-/-wastal ‘to bring, lead along (someone), Yzgh. waö-/west ‘to 
marry a woman’, Pash. xula ‘a woman remarrying her former husband’, wal-war 
*bride-price' || (+ *ati-) Sariq. diwoö-, düwoö-/diwust, düwust (old caus.) ‘to cause 
to enter, bring in, fold sheep’ || (+ *uz-) Sh. ziwáó-/ziwost ‘to take out, bring out, 
expel, extract’, Rosh. ziweó-/ziwost ‘to take out, bring out, expel, extract’, Sariq. 
ziwoó-, züwoó-/ziwust, zuwust ‘to take out, bring out, expell, extract’ || (+ *para-) 
Sariq. purweödi-Cuz ‘ferry-man’ 

*SANSKRIT: vadhü- (f.) ‘bride, young woman’ (RV+) > EWAia II: 497 

«PIE *Hued"- ‘to lead, marry (a woman)’. 0 The exact nature of the initial laryngeal 
is uncertain: the Hitt. evidence suggests *H> or *H;, whereas the Gr. form rather 
indicates *H;. > LIV: 659 f. | Pok.: 1115 f.
```


## [2026-10-16T05:17:38.474Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 13570,13600p CHEUNG.txt",
 "description": "Read Cheung *HuadH Avestan part"
}
```


### [2026-10-16T05:17:38.952Z] TOOL RESULT

```
empty, abandoned, free’; to be absent’, Umb. uacetum ‘uitiatum’ 
*REFERENCES: Oettinger 1979: 344; DKS: 383b f.; Abaev, Slovar’ IV: 37 ff. 


*Huad ‘to carry, lead (away); to marry (a wife)’ 

*AVESTAN: vad- (väö-) ‘to lead’ || (+ *upa-) ‘to lead up (and on)’ || (+ *uz-) ‘to 
abduct’ || (+ *ui-) ‘to lead to and fro’ = Liste: 49 

Partic.: pres. them. med. ? OAv. vadamna- (Y 53.5), caus. med. YAv. vaóaiiamna- (Yt 15.52); Caus.: 
pres. IND. 3sg. YAv. vadaiieiti (V 19.29), 3pl. YAv. uzuuädaiieinti (Yt 17.59), SUBJ. 1sg. ҮАУ. 
vadatieni (Yt 9.18), OPT. med. 3sg. YAv. upa.vaóaiiaeta (V 14.15), IMPV. 3р1. YAv. viuuaóaiiantu (У 
8.17 Е). © According to Kellens — Pirart 1990: 296, OAv. vadamna- is to be interpreted as ‘(en) 
paranymphe’. 

*MIDDLE PERSIAN: MMP *“wywdg’n, BMP wydwtk’n /wayodagan/ ‘nuptials, 
marriage’ = DMMPP: 360a 

(+ *uz-) Partic.: perf. pass. BMP ’wzw’hst /uzwahist/ 

*PARTHIAN: 1. w’d- ‘to lead’ {hapax}, w’d’g ‘leader, pilot’ || 2. w’y- (old caus.) ‘to 
lead’ (< MP) || (+ *ati-) ‘ydw’y- ‘to lead’ (influenced by w’y-) || (+ *4-) ’C)w’y- ‘to 
lead to, bring’ (influenced by w’y-) || (+ *uz-) ‘zw’y- ‘to lead out, away, beyond; set 
free’ (influenced by w’y-) = Ghilain: 71 | DMMPP: 337a 

1. Partic.: perf. pass. "w’d’d || 2. Pres.: IND. 35р. w’yd, ? “w’yyd, 3р1. “w’ynd, SUBJ. 15р. w’y’n; Partic.: 
perf. pass. w’st || (+ *ati-) Pres.: IND. 3sg. ‘dw’yd, 3pl. *‘dw’ynd, SUBJ. Isg. ‘ydw’y’n, OPT. 
‘ydw’yndyy; Partic.: perf. pass. ‘ydw’st || (+ *uz-) Pres.: SUBJ. 150. ‘zw’y’m, ‘zw’y’n, 3sg. ‘zw’y’h, 
IMPV. 2sg. ‘zw’y-; Partic.: ‘zw’st; Inf.: ‘zw’st
```


## [2026-10-16T05:17:42.516Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in water usquebaugh whisky vodka redundant surround urine otter winter wash wet hydrogen; do echo \"## $w\"; grep -n \"^$w,\" KLN_1966.txt | head -2 | cut -c1-500; done",
 "description": "Grep Klein headwords for chart words"
}
```


### [2026-10-16T05:17:43.005Z] TOOL RESULT

```
## water
## usquebaugh
40918:usquebaugh,  n.,  whiskey  (archaic).  —  Ir.  and  Gael. uiscebeathadh,  ‘whiskey’,  lit.  ‘water  of  life’,  fr. Olr.  uisce,  ‘water’,  and  bethad,  gen.  of  bethu, ‘life’.  Olr.  uisce  stands  for  *wud-ko-  and  is  cogn. with  OL  udan-,  Gk.  uScop,  E.  water  (q.v.)  The second  element  comes  fr.  Olr.  bethu,  ‘life’,  is cogn.  with  Gk.  pio?,  L.  vita,  ‘life’,  and  with  E. quick  (q.vtUCp.  whiskey,  which  is  a  doublet  of usquebaugh,  ffor  sense  development  cp
## whisky
## vodka
## redundant
## surround
37615:surround,  tr.  v.  —  ME.  surrounden.  The  word  orig. meant  ‘to  overflow’,  and  derives  fr.  MF.  so- ronder ,  ‘to  overflow’,  fr.  OF.,  fr.  Late  L.  super - undare  of  s.m.,  fr.  super-  and  L.  unda,  ‘wave’. See  undate  and  cp.  abound.  E.  surround  was  in¬ fluenced  both  in  form  and  meaning  by  an  er¬ roneous  association  with  the  adjective  round. Derivatives:  surround,  n.,  surround-ed,  adj.,  sur- round-ed-ly,  adv.,  surround-er ,  n.,  surround-ing
## urine
## otter
## winter
## wash
## wet
## hydrogen
18349:hydrogen,  n.,  name  of  a  gaseous  element  (chem.)
```


## [2026-10-16T05:17:45.954Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 18349,18351p KLN_1966.txt | cut -c1-500; for w in water whiskey whisky vodka redundant urine otter winter wet; do echo \"## $w\"; grep -n -E \"^$w[, ]\" KLN_1966.txt | head -2 | cut -c1-600; done; awk 'BEGIN{RS=\"\\f\"} NR==879 || NR==878 {print \"=== leaf \" NR-1; print substr($0,1,600)}' KLN_1966.txt",
 "description": "More Klein lookups and KLN p.1732 leaf"
}
```


### [2026-10-16T05:17:46.618Z] TOOL RESULT

```
hydrogen,  n.,  name  of  a  gaseous  element  (chem.)
—  F.  hydrogene,  lit.  ‘producing  water’,  coined by  the  French  chemist  Antoine-Laurent  de  La¬ voisier  (1743-94),  in  1787  fr.  Gk.  uScop,  ‘water’, and  the  stem  of  ysvviv,  ‘to  beget,  bring  forth, generate,  produce’.  See  hydro-  and  -gen. Derivatives:  hydrogen-ate,  tr.  v.,  hydrogen¬ ation,  n.,  hydrogen-ator,  n.,  hydrogenize,  tr.  v., hydrogen-ous,  adj.
hydrograph,  n.,  a  hydrographic  chart.  —  Com¬ pounded  of  hydro- and  Gk.-ypatpoi;,  fr.  ypaupeiv, ‘to  write’.  See  -graph.
## water
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
## whiskey
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
## whisky
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
## vodka
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
## redundant
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
## urine
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
## otter
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
## winter
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
## wet
(eval):1: bad math expression: empty string
(eval):1: bad math expression: operand expected at end of string
=== leaf 877
  pp.  of  terere  ‘to  rub, thresh,  grind’.  See  trite  and  cp.  trigo.  For  sense development  cp.  L.  granum,  ‘grain ,  which  is cogn.  with  OI.  jirnah,  ‘ground  to  powder’, trito-,  before  a  vowel  trit-,  combining  form  mean¬ ing  ‘third’.  —  Gk.  xptxo-,  xpix-,  fr.  rptroq, ‘third’.  See  third  and  three  and  cp.  tierce.
Triton,  n.,  a  minor  sea-god,  son  of  Poseidon  and Amphitrite  ( Greek  mythol.)  —  L.  Triton,  fr.  Gk. Tpixcov,  which  is  cogn.  with  OIr.  triath,  gen. trethan  (for  OCeltic  *triaton-),  ‘sea’.
Triton,  n.,  1)  a  genus  of  snails
=== leaf 878
T),  ‘tongue  of  the  balance,  balance  ,  orig.
‘the  hole  in  which  the  tongue  of  the  balance moves  about’,  which  stands  for  *tru-t  na  and  is rel.  to  xpuctv,  ‘to  rub,  wear  out ,  xpup-oc,  hole  , Teipstv  (for  *xeptat.v),  ‘to  rub,  wear  away’,  fr. I.-E.  base  *ter-,  ‘to  rub,  to  rub  by  turning,  to turn,  to  twist;  to  pierce’.  See  throw  and  cp. words  there  referred  to.
troop,  n.  —  MF.  (=  F.)  troupe,  fr.  OF.  trope,  fr. Late  L.  troppus,  ‘herd’,  fr.  Frankish  *l>rop,  meta.- thesis  of  *porp,  ‘crowd,  gathering,  village’, which  is
```


## [2026-10-16T05:17:49.987Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in water whiskey whisky vodka redundant urine otter winter wet; do echo \"## $w\"; grep -n -E \"^${w}[, ]\" KLN_1966.txt | head -2 | cut -c1-700; done; n=$(grep -n -E \"^water[, ]\" KLN_1966.txt | head -1 | cut -d: -f1); awk -v n=$n 'NR<=n' KLN_1966.txt | tr -cd '\\f' | wc -c",
 "description": "Klein lookups with proper quoting"
}
```


### [2026-10-16T05:17:50.410Z] TOOL RESULT

```
## water
## whiskey
## whisky
## vodka
## redundant
## urine
## otter
## winter
## wet
0
```


## [2026-10-16T05:17:52.361Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"^(water|whiskey|whisky|vodka|redundant|urine|otter|winter|wet),? \" KLN_1966.txt | cut -c1-600 | head -20",
 "description": "Grep Klein headwords with alternation"
}
```


### [2026-10-16T05:17:52.702Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:17:54.948Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"^water,\\|^whiskey\\|^whisky\\|^vodka\\|^redundant\\|^urine,\\|^otter,\\|^winter,\\|^wet,\" KLN_1966.txt | cut -c1-600 | head; grep -c \"\" KLN_1966.txt",
 "description": "Grep Klein with basic regex"
}
```


### [2026-10-16T05:17:55.282Z] TOOL RESULT

```
41263
```


## [2026-10-16T05:17:58.357Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; tail -c 300 KLN_1966.txt; echo; grep -n -i \"^water,\\|^whiskey\\|^vodka\\|^redundant\\|^urine,\\|^otter,\\|^winter,\\|^wet,\" KLN_1971.txt | cut -c1-500 | head",
 "description": "Check Klein file end and 1971 edition"
}
```


### [2026-10-16T05:17:58.675Z] TOOL RESULT

```
alkaloids  obtained  from sabadilla  seeds,  used  in  medicine  in  the  treat¬ ment  of  rheumatism,  neuralgia,  etc.  —  F.  vera¬ trine,  fr.  ModL.  veratrina,  fr.  L.  verdtrum,  ‘helle¬ bore’,  fr.  verare ,  ‘to  tell  the  truth’,  fr.  verus, ‘true’;  so  called  because
41358:redundant. Cp. fruiterer , poulterer , sorcerer , 
106818:water, — OF. (F. gruau ), ‘oatmeal, grits, groats’, 
113471:winter, to winter’, fr. hibernus , ‘pertaining to 
113472:winter, wintry’, which is rel. to hiems (gen. hie- 
129800:water, julep’, which is compounded of gul, ‘rose’, 
146325:wet, to flow’, fr. I.-E. base *mdd -, ‘wet, moist, 
170032:otter, n., an aquatic carnivorous mammal. — 
170035:otter, OHG, ottar , MHG. oter , otter , G. Otter , 
202451:redundant, adj., 1) excessive; 2) superfluous; 3) 
241130:water, which receded whenever he tried to
```


## [2026-10-16T05:18:01.944Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for p in \"^water, n\" \"^whiskey\" \"^whisky\" \"^vodka\" \"^urine, n\" \"^redundant, adj\" \"^otter, n\" \"^winter, n\" \"^wet, adj\" \"^wash, \" ; do n=$(grep -n \"$p\" KLN_1971.txt | head -1 | cut -d: -f1); echo \"## $p @ $n\"; [ -n \"$n\" ] && sed -n \"${n},$((n+7))p\" KLN_1971.txt | tr '\\n' ' ' | cut -c1-700; echo; done",
 "description": "Read Klein 1971 entries"
}
```


### [2026-10-16T05:18:02.595Z] TOOL RESULT

```
## ^water, n @ 265317
water, n, — ME. water, fr. OE. waster, rel. to OS.  watar , OFris. wetir, weter, wetter, LG., Du.  water , OHG. wa^ar, MHG. wajjer, G. Wasser,  ON. vatn, Swed. vat ten, Dan. vand, Goth, wato,  ‘water’, OE. wxt, ‘wet’, fr. I.-E. base *wxd  *wdd-, *ud -, ‘water’, whence also Hitt, watar,  gen. wetenash , ‘water’, OI. udnab , uddn-, uda -  kdm, ‘water’, anudrdh , ‘waterless’, utsah, ‘source’,  

## ^whiskey @ 266735
whiskey, whisky, n., an alcoholic liquor distilled  from grain. — Fr. Ir. and Gael, uisce, ‘water’,  shortened fr. uiscebeathadh , ‘whisky’, lit. ‘water  of life’. See usquebaugh, which is a doublet of  whiskey.   whisky, n., a light vehicle. — Formed fr. whisk,  n., with suff. -y.  

## ^whisky @ 266741
whisky, n., a light vehicle. — Formed fr. whisk,  n., with suff. -y.   whisper, intr. and tr. v. — ME. whisperen, fr. OE.  hwisprian, rel. to MDu. wispelen , wisperen ,  OHG. hwispalon, wispalon, MHG., G. wispeln,  G. wispern, ON. hviskra, Dan. hviske, ‘to whis-  per’ ; of imitative origin. Cp. whine, whistle.  

## ^vodka @ 263446
vodka, n. — Russ., dimin. of voda, ‘water’, which  is cogn. with Gk. tfSojp, Goth, wato , OE.  waiter. See water.   voe, n., an inlet, creek in the Orkney and Shet-     

## ^urine, n @ 257965
urine, n. — ME., fr. MF. (= F.), fr. OF., fr. L.  urina , which is cogn. with OI. var , vari, ‘water’,  Avestic vdr , ‘rain’, Toch. A war, ‘water’, Lith.  jures, Lett, jura, ‘sea’, esp. ‘the Baltic’, OPruss.  wurs, ‘pond’, OE. wser, ON. ver, ‘sea’, ON. ur,  ‘drizzling rain’. All these words derive fr. I.-E.  base*wer-, ‘water, rain, wet’; cp. urea, ureter,  urethra, uretic, and the first dement in aurochs.  

## ^redundant, adj @ 202451
redundant, adj., 1) excessive; 2) superfluous; 3)  wordy. — L. redundans, gen. -antis, pres. part,  of redunddre, ‘to run over, overflow’, fr. red-  and unddre, ‘to rise in waves’. See undate and  -ant and cp. redound, dunder.   Derivative: redundant-ly , adv.  reduplicate, tr. v. — Late L. reduplicdtus , pp. of  

## ^otter, n @ 170032
otter, n., an aquatic carnivorous mammal. —  ME. oter, fr. OE. otor , oter, rel. to ON. otr ,  Swed. utter „ Dan. odder , MLG., MDu., Du.  otter, OHG, ottar , MHG. oter , otter , G. Otter ,  and cogn. with OI. udrafi , Avestic udra , ‘otter’,  Gk. u&pa, uSpot;, ‘water-serpent’, ^vuSpis, ‘otter’,  L. lutra (for *utra, *udrd , influenced in form by  lutum , ‘mud, mire’), OSlav. vydra , Lith. udra ,  

## ^winter, n @ 267519
winter, n. — ME., fr. OE. winter, rel. to OFris.,  Du. winter, OS., OHG. wintar, MHG., G. win-  ter, Dan., Swed. vinter, Goth, wintrus , ON. vetr,  ‘winter’. These words meant perh. orig. ‘the  white (i.e. §nowy) season’, and are cogn. with  Celtic vindo-, ‘white’ appearing in Gaul, vindo-  (whence Vindo-bona , the Latin name of Vienna,  which was built by Celtic settlers), Olr. find, W.  

## ^wet, adj @ 266254
wet, adj. — ME. we/e, wette, partly fr. pp. of  weten , ‘to wet’, partly fr. OE. wxt, ‘wet’, which  is rel. to OFris. wet, ON. vdtr, Swed. vat, Dan.  vaad , ‘wet’, and to OE. wxter, ‘water’. See water.  Derivatives: wet, n., wet, v. (q.v.), wet-ly , adv.,  wet-ness, n., wett-ish, adj.  wet, tr. v. — ME. weten, fr. OE. wxtan, ‘to wet’,  fr. wxt. ‘wet’. See wet, adj.  

## ^wash,  @ 40962
wash, dash against, break over’, whence also  xXua^a, ‘liquid used for washing out; surf’,  xXuax7jp, ‘clyster pipe, syringe’, xXuScov, ‘wave,  surge*. Gk. xXo^ctv is cogn. with L. cloaca (fr.  earlier clovaca), ‘sewer, drain’, OL. cluere, ‘to  purge’. See cloaca and cp. clyster.   Derivatives: cataclysm-al, cataclysmat-ic , adjs.,
```


## [2026-10-16T05:18:06.207Z] TOOL CALL #47: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-16T05:18:06.219Z] TOOL RESULT

```

```


## [2026-10-16T05:18:08.767Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wódr̥",
 "prompt": "List the descendants relevant to: Greek hydor, Old Irish uisce, Russian voda, Latin unda, Proto-Germanic watar/wet/waskaną/wintruz/otter. Quote briefly."
}
```


## [2026-10-16T05:18:09.765Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/uisce",
 "prompt": "Give the Old Irish/Irish etymology of uisce and of uisce beatha (proto-Celtic form, PIE root)."
}
```


## [2026-10-16T05:18:10.669Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/winter",
 "prompt": "What does it say about the origin of winter, and whether it relates to wet/water (*wed-) or white (*wind-)?"
}
```


## [2026-10-16T05:18:11.263Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/surround",
 "prompt": "Give the etymology of surround (superundare, soronder, influence of round)."
}
```


### [2026-10-16T05:18:11.848Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-16T05:18:11.858Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-16T05:18:16.750Z] TOOL RESULT

```
# Etymology of *uisce* and *uisce beatha*

## *Uisce* (Water)

**Proto-Celtic form:** *\*udenskyos*

**PIE root:** *\*wódr̥* or *\*udéns* (meaning water)

The word derives from Proto-Indo-European through Proto-Celtic. According to the source, it comes "from Proto-Celtic *\*udenskyos*, from Proto-Indo-European *\*wódr̥, \*udéns*."

## *Uisce beatha*

The Wiktionary entry lists "uisce beatha" as a derived term from the modern Irish noun *uisce* but does not provide a separate etymology. The phrase literally means "water of life" (with *beatha* meaning "life"). This compound follows the same etymological path as *uisce*, with the root water term combined with an Irish word for vitality.

**Note:** The entry mentions this term as a derived form but offers no distinct proto-language analysis beyond the base word's ancestry.
```


### [2026-10-16T05:18:21.083Z] TOOL RESULT

```
# Proto-Indo-European *wódr̥ Descendants

Based on the Wiktionary entry, here are the relevant descendants:

**Greek (hydor):** Proto-Hellenic: "*údōr" with further descendants listed.

**Old Irish (uisce):** Proto-Celtic: "*udnā" descended from the derived term "*udn-eh₂," with Gaulish "onno" (river) also attested.

**Russian (voda):** Proto-Balto-Slavic: "*wandō" listed as a descendant with further descendants noted.

**Latin (unda):** The derived form "*udn-eh₂" yields Latin "unda f" meaning "wave," per De Vaan's etymological dictionary.

**Proto-Germanic (watar/wet/waskaną/wintruz/otter):** Proto-Germanic: "*watōr" shown as a direct descendant with "further descendants" referenced.

All these languages preserve reflexes of the reconstructed Proto-Indo-European root meaning "water."
```


## [2026-10-16T05:18:22.844Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/winter",
 "prompt": "Give the English etymology of winter: Proto-Germanic *wintruz and its proposed PIE origins (wet season vs white)."
}
```


## [2026-10-16T05:18:23.773Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/بیوگ",
 "prompt": "Give the Persian etymology of this word (Middle Persian, Proto-Iranian, PIE forms) and meaning."
}
```


## [2026-10-16T05:18:24.773Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wedʰ-",
 "prompt": "Give the meaning and descendants (Avestan, Sanskrit vadhu, Persian, Sogdian) of this root."
}
```


## [2026-10-16T05:18:25.378Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/urine",
 "prompt": "Give the English etymology of urine (Latin urina, PIE root)."
}
```


### [2026-10-16T05:18:29.239Z] TOOL RESULT

```
# Persian Etymology of بیوگ (bayug)

Based on the Wiktionary page provided, I cannot offer a complete etymological analysis with Middle Persian, Proto-Iranian, or Proto-Indo-European forms, as this information is **not included** in the source material.

## What the Page States

The entry indicates that **بیوگ** is an "archaic alternative form of بیو," meaning "a bride." The synonym provided is **عروس** ('arus).

The only etymological resource cited is the Dehkhoda Dictionary (1931–), but the actual etymological content from that source is not reproduced on this Wiktionary page.

## Limitation

To obtain the deeper etymological information you're seeking—tracing this word back through Middle Persian, Proto-Iranian, and potentially Proto-Indo-European roots—you would need to consult the full Dehkhoda Dictionary entry or specialized etymological references on Persian vocabulary, which are beyond the scope of this Wiktionary page.
```


### [2026-10-16T05:18:29.328Z] TOOL RESULT

```
# English Etymology of Winter

According to the Wiktionary entry, English "winter" derives from **Proto-Germanic *wintruz**. The documented etymological chain traces back through:

- Middle English *winter*
- Old English *winter*
- Proto-West Germanic *wintru*
- Proto-Germanic *wintruz* ("winter")

The article provides the linguistic heritage but does not discuss proposed Proto-Indo-European (PIE) origins or competing theories about whether the term relates to wet seasons versus white/snowy conditions. The entry focuses on documented language evolution rather than speculative semantic origins.

[WebFetch note: this page's text is 197259 characters long and the answer above covers only characters 0 to 100000; the final 97259 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


### [2026-10-16T05:18:30.065Z] TOOL RESULT

```
# Proto-Indo-European Root *wedʰ-

## Meanings

This root has two distinct meanings:

1. **"To lead, conduct, bring"** - referring to guiding or transporting
2. **"To bind, join, marry"** - relating to connecting or union

## Key Descendants

**Avestan:** The root appears in "𐬬𐬀𐬰𐬌𐬌𐬀𐬨𐬥𐬁" (vaziiamnā, "leading," future middle participle)

**Sanskrit:** Multiple forms derive from this root:
- "विवध" (vivadhá, "yoke") 
- "वध्रि" (vádhri, "castrated")
- "वध्र" (vádhra, "leather strap")

**Persian:** Descendants appear through Proto-Iranian *wādáyati ("to lead, conduct; to bring"), which evolved into various Persian forms

**Sogdian:** While not explicitly detailed in this entry, the root contributes to the Indo-Iranian language family through Proto-Iranian developments

The root demonstrates semantic evolution from physical action (leading, binding) to social/marital contexts across Indo-European languages.
```


### [2026-10-16T05:18:32.650Z] TOOL RESULT

```
# English Etymology of Urine

The English word "urine" comes from "Middle English _uryne_," which was borrowed from "Latin _ūrīna_" ("urine"). The Latin term ultimately derives from a Proto-Indo-European root, specifically the "zero grade of _*woh₁-r̥_" meaning "water, liquid, milk."

This ancient root is also related to the Proto-Indo-European term "_*h₁ówHdʰr̥_" ("udder"), connecting urine etymologically to words like "udder." Additionally, the word is cognate with "Old English _ūriġ_" ("wet, moist").

In English, urine displaced an earlier native term, "land," which came from Old English _hland_, though the related word "lant" survives in specialized contexts.

[WebFetch note: this page's text is 106940 characters long and the answer above covers only characters 0 to 100000; the final 6940 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


## [2026-10-16T05:18:34.648Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wintruz",
 "prompt": "Give the etymology section (proposed PIE origins) verbatim-ish."
}
```


## [2026-10-16T05:18:35.644Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/whisky",
 "prompt": "Give the English etymology of whisky/whiskey (usquebaugh, Irish uisce beatha, Scottish Gaelic uisge-beatha, dates)."
}
```


## [2026-10-16T05:18:36.495Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/водка",
 "prompt": "Give the Russian etymology of vodka (diminutive of voda), and any mention of Persian borrowing."
}
```


## [2026-10-16T05:18:37.163Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/hydrogène",
 "prompt": "Give the French etymology of hydrogène (coinage, date, who)."
}
```


### [2026-10-16T05:18:39.465Z] TOOL RESULT

```
# French Etymology of "Hydrogène"

**Composition:** The word combines "hydro-" (water) and "-gène" (generating/producing).

**Coinage:** The term was created by French chemist Antoine Lavoisier in 1783. According to the source, it was "Coined by French nobleman and chemist Antoine Lavoisier in 1783."

**Meaning:** The compound literally refers to a substance that generates water, which is fitting since hydrogen combustion produces water.
```


### [2026-10-16T05:18:41.560Z] TOOL RESULT

```
# Russian Etymology of Vodka

Based on the Wiktionary entry, the Russian word **водка** (vódka) derives from **вода́** (vodá, "water") plus the diminutive suffix **-ка** (-ka).

The entry states: "From _[вода́](/wiki/%D0%B2%D0%BE%D0%B4%D0%B0#Russian)_ (vodá, 'water') +‎ _[\-ка](/wiki/-%D0%BA%D0%B0#Russian)_ (\-ka, diminutive suffix)."

The word was first documented in 1533 in medical contexts, with the beverage sense emerging in the 17th century and becoming widespread by the 19th century.

## Persian Connection

**The provided source contains no mention of Persian borrowing.** The etymology traces the word through Proto-Indo-European roots and notes that the beverage sense may derive from Polish _wódka_, which itself possibly derives from Medieval Latin _aqua vitae_.
```


### [2026-10-16T05:18:41.573Z] TOOL RESULT

```
# Etymology of Proto-Germanic *wintruz

The proposed Proto-Indo-European origins include:

1. **Wind connection**: "possible relation to *windaz (whence wind) (i.e. 'the windy season'), from PIE *h₂wéh₁n̥tos ("wind")" and earlier *h₂wéh₁n̥ts, derived from the verb *h₂weh₁- ("to blow").

2. **Celtic parallel**: A relationship to Proto-Celtic *windos meaning "white."

3. **Water origin**: "Relation to PIE *wódr̥ ("water"), whence also Proto-Germanic *watōr."

The source notes that "the first theory involves an analysis of Latin unda continuing *u-n-deh₂ rather than *ud-neh₂, while there is little semantic evidence for the second theory." Overall, the etymology remains unknown, with none of these proposals being particularly convincing.
```


### [2026-10-16T05:18:42.290Z] TOOL RESULT

```
# Etymology of Whisky/Whiskey

**English Origin:**
The term derives from "usquebaugh," which itself comes from Scottish Gaelic *uisge-beatha* and Irish *uisce beatha*, both meaning "water of life." These Gaelic terms represent a calque of Medieval Latin *aqua vitae*.

**Key Details:**
- **Primary source:** Scottish Gaelic *uisge-beatha* and Irish *uisce beatha*
- **Translation:** "water of life"
- **Latin parallel:** Medieval Latin *aqua vitae* (same meaning)
- **Timeline:** The English word entered use in the "early 18th century"

The documentation shows this etymology appears consistently across multiple language entries in Wiktionary, confirming the Gaelic-to-English transmission pathway through the abbreviated form "usquebaugh" before becoming the modern "whisky" or "whiskey."

[WebFetch note: this page's text is 150622 characters long and the answer above covers only characters 0 to 100000; the final 50622 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


## [2026-10-16T05:18:44.663Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/هیدروژن",
 "prompt": "Quote the Mo'in entry text verbatim, including origin tag like [فر.]."
}
```


## [2026-10-16T05:18:45.399Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/ویسکی",
 "prompt": "Quote the Mo'in entry text verbatim, including origin tag."
}
```


## [2026-10-16T05:18:46.058Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/ودکا",
 "prompt": "Quote the Mo'in entry text verbatim, including origin tag."
}
```


## [2026-10-16T05:18:46.639Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/بیوگانی",
 "prompt": "Quote the Mo'in entry text verbatim, including origin tag."
}
```


### [2026-10-16T05:18:48.675Z] TOOL RESULT

```
# بیوگانی (Biogāni)

According to the Mo'in Dictionary entry provided:

**(بَ) (حامص .) عروسی ، نکاح .**

This Persian word means "wedding" or "marriage" (عروسی، نکاح). The entry indicates it comes from a historical or dialectal source (marked as حامص).
```


### [2026-10-16T05:18:48.770Z] TOOL RESULT

```
# Hydrogen (هیدروژن) - Mo'in Dictionary Entry

According to the Mo'in Dictionary of Persian, the entry states:

"(ژِ) [ فر. ] (اِ.) گازی است بی رنگ و بو و بی طعم که از ترکیب آن با اکسیژن آب ایجاد می شود"

In essence, hydrogen is defined as a colorless, odorless, and tasteless gas that combines with oxygen to form water.
```


### [2026-10-16T05:18:48.776Z] TOOL RESULT

```
# Vodka Definition from Mo'in Dictionary

According to the Mo'in Dictionary entry, vodka is defined as:

"نوعی نوشابة الکلی بی رنگ قوی ، عرق روسی" 

This translates to a type of colorless, strong alcoholic beverage; Russian liquor. The entry notes the word's Russian origin (روس).
```


### [2026-10-16T05:18:48.858Z] TOOL RESULT

```
# Mo'in Dictionary Entry for "ویسکی" (Whisky)

According to the Mo'in Publishers Dictionary, the entry reads:

"\[ انگ . \] (اِ.) نوعی مشروب الکلی ."

**Translation:** This is an English loanword denoting "a type of alcoholic beverage."

The entry appears in the Mo'in Dictionary alongside cross-references to other Persian lexicons including Dehkhoda, Amid, and bilingual Persian-to-English and Persian-to-Arabic dictionaries.
```


## [2026-10-16T05:18:56.344Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wódr̥|page 528 root Wed: PIE water descendants\" \"https://en.wiktionary.org/wiki/uisce|page 528 Old Irish uisce etymology\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wintruz|page 528 winter etymology uncertain\" \"https://en.wiktionary.org/wiki/بیوگ|page 528 Wedh 1 Persian bayug\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wedʰ-|page 528 Wedh 1 root\" \"https://en.wiktionary.org/wiki/urine|page 528 urine etymology\" \"https://en.wiktionary.org/wiki/whisky|page 528 whisky etymology\" \"https://en.wiktionary.org/wiki/водка|page 528 vodka etymology\" \"https://en.wiktionary.org/wiki/hydrogène|page 528 hydrogene coinage\" \"https://vajehyab.com/moein/هیدروژن|page 528 Mo'in hidrožen [فر.]\" \"https://vajehyab.com/moein/ویسکی|page 528 Mo'in viski [انگ.]\" \"https://vajehyab.com/moein/ودکا|page 528 Mo'in vodka\" \"https://vajehyab.com/moein/بیوگانی|page 528 Mo'in bayugani\"; do url=\"${u%%|*}\"; note=\"${u#*|}\"; timeout 60 python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -1; done; grep -n \"بیوگ\\|بیوک\" data/verification/sources/refs/incoming/ARY/ARY_pages.txt | head -3; grep -n -i \"VADH\\|BAYUG\\|BIYUG\" data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt | head -5",
 "description": "Archive web sources and grep Aryanpur",
 "timeout": 600000
}
```


### [2026-10-16T05:19:00.618Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3658df9147b80327.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c534d07ab9b937af.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4e5d2bd6481394e5.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/876c699c5153c2a6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8f007cfce6fb527b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9713f46b52c53c87.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/60996aecfa618370.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7ac035aa546963cd.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2c75a63668c1daf1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/32d9e1f6ec587f7c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0fbd08178251bba6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ed16ad982e8d3b97.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/868228ab26352ad3.txt
4134:(4, exow CHURCH SLAVIC) 4S 53%) VADHUPA AVESTAN) glen)
4138:, VEDU, VADUOTI VADHUS, VAH-  :(SANSKRIT) 2 St
4139:VAUOT _ QERLATIIAN) (A) 39) VADHAYEITI
11639:HVADHARR KU KURDISH) 535°
```


## [2026-10-16T05:19:02.920Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 4125,4142p ARY_latin_index_pages.txt; awk 'NR<=4134' ARY_latin_index_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -1; grep -n \"عروس\" ARY_pages.txt | head -5",
 "description": "Read Aryanpur index around VADHUPA"
}
```


### [2026-10-16T05:19:03.356Z] TOOL RESULT

```
AMINDAROY: (NOSE) 260 NASU
TIPO-V ITF PFD igbioby NOSE ENGLISH) gud}
over sHasens aabicail NAZE DANISH) S asl3
NASA (SWEDISH) 548 yo
[pdf page 145]
. Ce) Hus Soe [VF
| a
|
|
(4, exow CHURCH SLAVIC) 4S 53%) VADHUPA AVESTAN) glen)
2") VED VAYODAGAN PAHLAVI) 5 jh
VESTI (4L(RUSSIAN) (gn) BUK (KURDISH) 53,5
‘ VADAS, — (y\)(LITHUANIAN) gi -J WADE AAFGHAND) (4) gil
, VEDU, VADUOTI VADHUS, VAH-  :(SANSKRIT) 2 St
VAUOT _ QERLATIIAN) (A) 39) VADHAYEITI
i FEDID — (414)(OLD IRISH) oS 5432! YAS, VADIS (ALELATIN) 3
UWATE (QL (HITTIE) cca WADI, (4ltX(GOTHIC) Sa F
GAWADJON :
[pdf page 145]
1023:پدر عروش يا ایل عروس «هدیه؛ (مثلاً چند رس گاو) می‌دادند. در مقابل پدر عروس موظف برد که
1024:جهیزبه عروس را تهیه کند. معمولاً مذا کرات وابسته به زناشویی طولانی بود.
4226:۶ /_بيوگاني» ویوگانی (به چم"*عروسی") : :
10776:چم این واژه در زبان بلوچی: جشن عروسی
```


## [2026-10-16T05:19:05.282Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 4215,4232p ARY_pages.txt; awk 'NR<=4226' ARY_pages.txt | grep -o \"\\[pdf page [0-9]*\\]\" | tail -1",
 "description": "Read Aryanpur entry for bayugani"
}
```


### [2026-10-16T05:19:05.701Z] TOOL RESULT

```
فریزی کهن (/۲/514 01 ۸051 ,270855 4 (۲82) :5 م02
آلمانی کهن (/(085۵1۸ ۲۲0/3 صا0): 5 (۲05۳) ود 0
۱ ۸۹۸ 227 8
آلای دم : 1۸5 5اه (۳0۶2) 00/5
7 ۰ اد
انگلیسی کهن (98بق۸غ طت۵): ۰ ,تا۸09 23 (۸۵۶5) 3547
۸۵۲ 0 (055) ۸0
انگلیسی (3/.ا8(/0): 103 برهان قاطع : ۱ ۲۱۳۵-۲۱۳۶
دانمارکی (0/8): دا لغت‌نامه دهخدا: ۹۳
سرئدی (5177801527). ۸
[pdf page 145]
۶ /_بيوگاني» ویوگانی (به چم"*عروسی") : :
[ ریعه! ۱
۱
اوستایی (/۸789742): ۷0۸ اسلاوی کهن (۲1اماة بزع#نایی 00 (شاپد) پچ 1
پهلری (۷1هالام۳): ۹ وا 7*۶
کردی (۸8015]7): ۸1 روسی (/5514۸ل)(شاید) ۷۳۹
اففانی (پشتر) (/۸۳0[1۸۸7): ۱۱یا لیترانی (7440۷/۸۷/)(شاید) ‏ ,۷۸۵۸8 ۱
[pdf page 145]
```


## [2026-10-16T05:19:33.036Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p528; pdftoppm -f 528 -l 528 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg528 && mkdir -p data/verification/sources/refs/ocr/BOOK && cp $S/pg528.png data/verification/sources/refs/ocr/BOOK/528.png; python3 -c \"\nfrom PIL import Image; im=Image.open('$S/pg528.png'); w,h=im.size; im.crop((int(w*0.33),int(h*0.45),int(w*0.53),int(h*0.5))).save('$S/crop528.png')\"; echo ok",
 "description": "Render page 528 and crop Latin super-undere box"
}
```


### [2026-10-16T05:19:34.611Z] TOOL RESULT

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image; im=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p528/pg528.png'); w,h=im.size; im.crop((int(w*0.33),int(h*0.45),int(w*0.53),int(h*0.5))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p528/crop528.png')
    ^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'PIL'
ok
```


## [2026-10-16T05:22:16.246Z] TOOL CALL #68: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p528/build528.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nWODR=W+\"Reconstruction:Proto-Indo-European/wódr̥\"\nAHDQ=\"AHD_watkins1985.txt line 1127, s.v. wed-1: 'Water; wet. ... [Pok. 9. au(e)- 78.]'\"\nPOKQ=\"POK_full.txt line ~8000-8299 (lemma au̯ed-, au̯er-, 'Meaning: to flow, to wet; water'; 'Page(s): 78-81')\"\nWLDQ=\"WLD_Bd1_pages.txt leaf 261 (line ~23626-23700), au̯ed- 'netzen': 'Lat. unda „Welle, Woge“', 'air. u(i)sce „Wasser“ (*udes-kio-)', 'wahrscheinlich got. wintrus ... „Winter“'\"\ndef n(id,lang,words,verdict,der,derfa,sources,rc,cons,**kw):\n    d=dict(id=id,lang=lang,words=words,verdict=verdict,derivation=der,derivation_fa=derfa,sources=sources,ref_check=rc,consulted=cons); d.update(kw); return d\ndef ahd_rc(note): return {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD (Watkins 1985 = same root list as Nourai's 1976 appendix p.1547) \"+note}\ncons_ie=lambda pn,wn: [{\"src\":\"POK\",\"where\":\"pp. 78-81, au̯ed-\",\"stance\":\"supports\",\"note\":pn},{\"src\":\"WLD\",\"where\":\"Bd. I, leaf 261 (WP. I 252 f.)\",\"stance\":\"supports\",\"note\":wn}]\ne0nodes=[\nn(1,\"Greek\",\"hudôr\",\"confirmed\",\n \"Greek hýdōr (gen. hýdatos) 'water' is the PIE heteroclitic r/n-stem *wód-r̥ / *ud-én- in zero grade with suffix -ōr: *ud-ōr > Proto-Hellenic *údōr > hýdōr (initial *u- regularly aspirated in Greek). The oblique stem hydat- continues *ud-n̥-t-.\",\n \"«هودور» (hýdōr) یونانی به معنای «آب» از صورت بی‌بالانده (zero grade) ریشهٔ هندواروپایی *wed-/ud- با پسوند -ōr است (*ud-ōr)؛ واکهٔ u در آغاز واژه در یونانی دمیده (h-) شده است. ستاک حالت‌های دیگر hydat- بازماندهٔ صرف r/n این واژه است. پوکورنی و واتکینز همین را می‌گویند؛ ادعای نورایی درست است.\",\n [WODR],[ahd_rc(\"wed-1 §5: 'Suffixed zero-grade form *ud-ōr in Greek hudōr, water: (HYDRANT), HYDRO-'.\")],\n cons_ie(\"'Gr. ὕδωρ, ὕδατος (*ὕδ-n̥-τος) water' (line ~8077)\",\"WP I 252 f. cited by Pokorny for au̯ed-; Greek ὕδωρ among the core forms\")+[{\"src\":\"KLN\",\"where\":\"KLN_1971.txt line 265317 s.v. water\",\"stance\":\"supports\",\"note\":\"'fr. I.-E. base *wed-, *wod-, *ud-, water, whence also Hitt. watar ... Gk. hydōr'\"}]),\nn(2,\"French\",\"hydrogene\",\"confirmed\",\n \"French hydrogène was coined in the new chemical nomenclature of Guyton de Morveau, Lavoisier, Berthollet and Fourcroy (1787; Lavoisier's work on the gas 1783) from Greek hydro- 'water' + -gène 'producing' (Greek -genēs, root *ǵenh₁-, see Gene 1), 'water-generator', because burning the gas yields water.\",\n \"«هیدروژن» در فرانسه (hydrogène) واژه‌ای ساختگی است که لاووازیه و همکارانش در نام‌گذاری نوین شیمی (۱۷۸۳–۱۷۸۷) از یونانی hydro- «آب» و -gène «زاینده» (از ریشهٔ هندواروپایی *ǵenh₁-) ساختند، یعنی «آب‌زا»، زیرا سوختن این گاز آب پدید می‌آورد. کلاین و ویکی‌واژه همین را می‌گویند؛ ادعای نورایی درست است.\",\n [W+\"hydrogène\"],[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"node carries no reference; Klein (below) checked instead\"}],\n [{\"src\":\"KLN\",\"where\":\"KLN_1966.txt line 18349 s.v. hydrogen\",\"stance\":\"supports\",\"note\":\"'F. hydrogène, lit. producing water, coined by the French chemist Antoine-Laurent de Lavoisier (1743-94), in 1787 fr. Gk. ὕδωρ, water, and the stem of γεννᾶν, to beget'\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt grep 'hydrogen'\",\"stance\":\"supports\",\"note\":\"Skeat lists hydrogen under hydro- from Gk. ὕδωρ 'water' + -gen (F. -gène)\"}]),\nn(3,\"Persian\",\"hîdrogen\",\"confirmed\",\n \"Persian hidrožen هیدروژن is a 19th/20th-century learned loan from French hydrogène (Persian scientific vocabulary of the Dār al-Fonun era was largely French); the final -ène > -en and ž for French g [ʒ] show the French source, not English hydrogen.\",\n \"«هیدروژن» وام‌واژه‌ای از فرانسوی hydrogène است که با آموزش علوم نوین در دوران قاجار (دارالفنون) به فارسی آمد؛ تلفظ «ژ» برای g فرانسوی گواه آن است که از فرانسه گرفته شده، نه از انگلیسی. معین آن را [فر.] نشان داده است؛ ادعای نورایی درست است.\",\n [\"https://vajehyab.com/moein/هیدروژن\"],\n [{\"ref\":\"MON:5230\",\"status\":\"supports\",\"note\":\"page not mappable online; Mo'in at vajehyab.com/moein/هیدروژن: '(ژِ) [ فر. ] (اِ.) گازی است بی رنگ و بو و بی طعم که از ترکیب آن با اکسیژن آب ایجاد می شود' — French origin as drawn\"}],\n [{\"src\":\"MON\",\"where\":\"MON_part1/2.txt (2-vol abridgement) grep 'هیدروژن'\",\"stance\":\"silent\",\"note\":\"abridged OCR; online full entry used instead\"},\n  {\"src\":\"ARY\",\"where\":\"ARY_pages.txt grep 'هیدروژن'\",\"stance\":\"silent\",\"note\":\"Aryanpur covers inherited IE words only, no European loans\"}]),\nn(4,\"English\",\"hydrogen, hydrant, hydro\",\"confirmed\",\n \"English hydrogen (1791) is from French hydrogène; hydrant (1806, American) is an English formation from Greek hydr- 'water' + -ant; hydro is a 19th-c. clipping of hydropathic (establishment) / hydro-electric, from the combining form hydro- < Greek hydōr. All derive from Greek hýdōr, not directly from French in the case of hydrant/hydro.\",\n \"در انگلیسی hydrogen از فرانسوی hydrogène گرفته شده؛ hydrant (شیر آتش‌نشانی، ۱۸۰۶ آمریکا) ساختهٔ انگلیسی از hydr- یونانی «آب» و پسوند -ant است؛ hydro کوتاه‌شدهٔ hydropathic و hydro-electric است. همه به یونانی hýdōr «آب» بازمی‌گردند؛ ادعای نورایی درست است.\",\n [WODR],[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"node carries no reference; AHD wed-1 §5 lists '(HYDRANT), HYDRO-' under Greek hudōr (AHD_watkins1985 line 1127)\"}],\n [{\"src\":\"KLN\",\"where\":\"KLN_1966.txt line 18331 s.v. hydro\",\"stance\":\"supports\",\"note\":\"'hydro, shortened form of 1) hydropathic, 2) hydroairplane, 3) hydraulic power. — See hydro-'\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985 line 1127, wed-1 §5\",\"stance\":\"supports\",\"note\":\"'Greek hudōr, water: (HYDRANT), HYDRO-, (HYDROUS)'\"}]),\nn(5,\"Old Irish\",\"uisce; uisce beathadh\",\"confirmed\",\n \"Old Irish uisce 'water' < Proto-Celtic *udeskyo- / *udenskyos, suffixed zero grade *ud- of the PIE water word (*ud-skio- in AHD). uisce beathadh 'water of life' (Early Modern Irish / Scottish Gaelic spelling; Old Irish would be uisce bethad, gen. of bethu 'life') is a medieval calque of Latin aqua vitae 'distilled spirit'.\",\n \"«اوشکه» (uisce) ایرلندی کهن به معنای «آب» از سلتی آغازین *udeskyo- و از صورت بی‌بالانده *ud- ریشهٔ هندواروپایی «آب» است. uisce beathadh «آبِ زندگی» گرته‌برداری (calque) از لاتینی میانه aqua vitae «عرق تقطیرشده» است؛ beathadh املای ایرلندی/گالیک دوره‌های بعد است (در ایرلندی کهن bethad). پوکورنی و واتکینز و ویکی‌واژه این را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n [W+\"uisce\",W+\"whisky\"],\n [{\"ref\":\"AHD:1410\",\"status\":\"not_checked\",\"note\":\"AHD 1976 main-dictionary page (not online). The Watkins appendix wed-1 §8 (AHD_watkins1985 line 1127) gives 'Suffixed zero-grade form *ud-skio- in Scottish and Irish Gaelic uisge, water: USQUEBAUGH, (WHISKEY)' — supports the arrow\"}],\n cons_ie(\"'Old Irish u(i)sce (*udeskio-) water' (POK_full line ~8119)\",\"'air. u(i)sce „Wasser“ ... (*udes-kio-)' (WLD_Bd1_pages line ~23643)\")+[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt line 40918 s.v. usquebaugh\",\"stance\":\"supports\",\"note\":\"'OIr. uisce stands for *wud-ko- and is cogn. with OI. udan-, Gk. ὕδωρ, E. water'\"}]),\nn(6,\"English\",\"usquebaugh, usquabae, whiskey, whisky\",\"confirmed\",\n \"English usquebaugh (16th c.; variant usquabae, used by Burns in Tam o' Shanter) is borrowed from Irish uisce beatha / Scottish Gaelic uisge beatha 'water of life'; whisky/whiskey (early 18th c.) is a clipping of usquebaugh keeping only the first element (uisce > whisk-y, with English wh- for Gaelic u-). Whisky and usquebaugh are doublets.\",\n \"در انگلیسی usquebaugh (سدهٔ ۱۶، با گونهٔ usquabae در شعر رابرت برنز) از ایرلندی uisce beatha / گالیک uisge beatha «آبِ زندگی» وام گرفته شد؛ whisky/whiskey (آغاز سدهٔ ۱۸) کوتاه‌شدهٔ همین واژه است که تنها جزء نخست (uisce «آب») را نگه داشته است. پس «ویسکی» در اصل یعنی «آب». کلاین و ویکی‌واژه همین را می‌گویند؛ ادعای نورایی درست است.\",\n [W+\"whisky\"],\n [{\"ref\":\"AHD:1460\",\"status\":\"not_checked\",\"note\":\"AHD 1976 main-dictionary page not online; appendix wed-1 §8 lists 'USQUEBAUGH, (WHISKEY)' under *ud-skio- (AHD_watkins1985 line 1127) — supports\"}],\n [{\"src\":\"KLN\",\"where\":\"KLN_1966 line 40918 s.v. usquebaugh; KLN_1971 line 266735 s.v. whiskey\",\"stance\":\"supports\",\"note\":\"'Ir. and Gael. uiscebeathadh, whiskey, lit. water of life'; 'whiskey ... Fr. Ir. and Gael. uisce, water, shortened fr. uiscebeathadh ... See usquebaugh, which is a doublet of whiskey'\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt grep 'usquebaugh|whisky'\",\"stance\":\"supports\",\"note\":\"Skeat: whisky from Gael. uisge 'water', short for uisge-beatha (usquebaugh) 'water of life'\"}]),\nn(7,\"Persian\",\"vîskî\",\"confirmed\",\n \"Persian viski ویسکی is a modern loan from English whisky (Mo'in tags it [انگ.] 'English'); the gloss 'water of life' is Nourai's etymological gloss of the English/Gaelic source, not a Persian meaning (Persian viski just means the drink).\",\n \"«ویسکی» وام‌واژه‌ای نو از انگلیسی whisky است و معین آن را [انگ.] نشان داده است؛ معنای «آب زندگی» که نورایی آورده معنای ریشه‌ای واژهٔ گالیک است، نه معنای آن در فارسی که تنها نام نوشابه‌ای الکلی است. ادعای نورایی درست است.\",\n [\"https://vajehyab.com/moein/ویسکی\"],\n [{\"ref\":\"MON:5072\",\"status\":\"supports\",\"note\":\"Mo'in at vajehyab.com/moein/ویسکی: '[ انگ . ] (اِ.) نوعی مشروب الکلی' — English source as drawn (page number not mappable online)\"}],\n [{\"src\":\"KLN\",\"where\":\"KLN_1971 line 266735 s.v. whiskey\",\"stance\":\"supports\",\"note\":\"English source form 'whiskey, whisky ... Ir. and Gael. uisce'\"},\n  {\"src\":\"ARY\",\"where\":\"ARY_pages.txt grep 'ویسکی'\",\"stance\":\"silent\",\"note\":\"no entry (Aryanpur covers inherited words only)\"}]),\nn(8,\"Russian\",\"voda; vodka\",\"confirmed\",\n \"Russian vodá 'water' < Proto-Slavic *voda < Balto-Slavic *wandō(n), o-grade *wod- of the PIE water word (cf. Hittite wātar). vódka is vodá + diminutive -ka 'little water', attested 1533 for medicinal tinctures, as a spirit from the 17th c. (sense possibly calqued on Polish wódka / Latin aqua vitae).\",\n \"«وُدا» (voda) روسی به معنای «آب» از اسلاوی آغازین *voda و از بالندهٔ o (*wod-) همان ریشهٔ هندواروپایی است (هم‌ریشه با water انگلیسی و wātar هیتی). «ودکا» = voda + پسوند کوچک‌ساز -ka، یعنی «آبک»، که در ۱۵۳۳ برای داروهای مایع و از سدهٔ ۱۷ برای عرق به کار رفته است. واتکینز و پوکورنی و کلاین همین را می‌گویند؛ ادعای نورایی درست است.\",\n [W+\"водка\",WODR],[ahd_rc(\"wed-1 §9: 'Suffixed o-grade form *wod-ā in Russian voda, water: VODKA'.\")],\n cons_ie(\"'Old Church Slavic voda water' (POK_full line ~8159)\",\"Slavic voda listed under au̯ed- (WLD_Bd1 leaf 261)\")+[{\"src\":\"KLN\",\"where\":\"KLN_1971 line 263446 s.v. vodka\",\"stance\":\"supports\",\"note\":\"'vodka, n. — Russ., dimin. of voda, water, which is cogn. with Gk. ὕδωρ, Goth. wato, OE. wæter'\"}]),\nn(9,\"Persian\",\"vodkâ\",\"confirmed\",\n \"Persian vodkā ودکا is a loan from Russian vodka (Qajar-era contact across the Caucasus/Caspian); Mo'in glosses it 'Russian liquor'. Nourai's gloss 'water, drink' is the Russian etymology (diminutive of voda), not a Persian meaning.\",\n \"«ودکا» از روسی vodka در دوران قاجار و از راه پیوندهای قفقاز و کرانه‌های خزر به فارسی آمده است؛ معین آن را «نوعی نوشابهٔ الکلی بی‌رنگ قوی، عرق روسی» معنی کرده است. معنای «آب، نوشیدنی» در نمودار معنای ریشه‌ای روسی است. ادعای نورایی درست است.\",\n [\"https://vajehyab.com/moein/ودکا\"],\n [{\"ref\":\"MON:4994\",\"status\":\"supports\",\"note\":\"Mo'in at vajehyab.com/moein/ودکا: 'نوعی نوشابهٔ الکلی بی رنگ قوی ، عرق روسی' with Russian origin tag (page not mappable online)\"}],\n [{\"src\":\"KLN\",\"where\":\"KLN_1971 line 263446 s.v. vodka\",\"stance\":\"supports\",\"note\":\"Russian source form 'dimin. of voda, water'\"},\n  {\"src\":\"ARY\",\"where\":\"ARY_pages.txt grep 'ودکا'\",\"stance\":\"silent\",\"note\":\"no entry\"}]),\nn(10,\"English\",\"vodka\",\"confirmed\",\n \"English vodka (first recorded 1802) is borrowed directly from Russian vodka, diminutive of voda 'water'.\",\n \"واژهٔ vodka در انگلیسی (نخستین کاربرد ۱۸۰۲) مستقیماً از روسی vodka، کوچک‌شدهٔ voda «آب»، گرفته شده است. ادعای نورایی درست است.\",\n [W+\"водка\"],[ahd_rc(\"wed-1 §9: 'Russian voda, water: VODKA'.\")],\n [{\"src\":\"KLN\",\"where\":\"KLN_1971 line 263446\",\"stance\":\"supports\",\"note\":\"'vodka, n. — Russ., dimin. of voda'\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt grep 'vodka'\",\"stance\":\"silent\",\"note\":\"not in Skeat's concise dictionary\"}]),\nn(11,\"Germanic\",\"water; wĕd; wat-skan; wintruz\",\"plausible\",\n \"Proto-Germanic *watōr/*watar 'water' (o-grade *wod-ōr), *wēta- 'wet' (lengthened grade *wēd-), *waskaną 'to wash' < *wat-skaną (o-grade *wod- + -sk- present suffix, -ts- > -s-) are all secure. *wintruz 'winter' as nasalized *we-n-d- 'wet season' is one of three proposals (others: 'white season' with Celtic *windos, or 'windy season'); Klein prefers 'white', Wiktionary calls the etymology unknown. Hence plausible for the node.\",\n \"در ژرمنی آغازین *watōr «آب»، *wēta- «تر» و *waskaną «شستن» (از *wat-skaną با پسوند -sk-) بی‌گمان از ریشهٔ *wed- «آب» هستند. اما *wintruz «زمستان» به معنای «فصل تر» تنها یکی از سه پیشنهاد است؛ کلاین آن را «فصل سفید» (هم‌ریشه با سلتی vindo- «سفید») می‌داند و ویکی‌واژه ریشهٔ آن را ناشناخته می‌شمارد. پس سه واژهٔ نخست درست و پیوند winter با این ریشه تنها با احتیاط پذیرفتنی است.\",\n [W+\"Reconstruction:Proto-Germanic/wintruz\",WODR],[ahd_rc(\"wed-1 §§1-4: '*wod-ōr in Germanic *watar', '*wēd-o- in Germanic *wēt-', '*wat-skan, to wash', 'Nasalized form *we-n-d- in Germanic *wintruz, winter, \\\"wet season\\\"' — exactly Nourai's four forms.\")],\n cons_ie(\"'probably Gothic wintrus ... winter as wet season (Liden PBrB. 15, 522)'; 'Old Icelandic vatr, Old English wæt, engl. wet'\",\"'wahrscheinlich got. wintrus aisl. vetr, ags. winter ... „Winter“' (WLD_Bd1_pages line ~23654); wash: 'oder zu ir. fáisc- „drücken“' — wash also given an alternative\")+[{\"src\":\"KLN\",\"where\":\"KLN_1971 line 267519 s.v. winter\",\"stance\":\"contradicts\",\"note\":\"'These words meant perh. orig. the white (i.e. snowy) season, and are cogn. with Celtic vindo-, white'\"}]),\nn(12,\"English\",\"water, wet, wash ; winter, otter\",\"plausible\",\n \"Old English wæter > water, wǣt > wet, wascan (< *watskan) > wash, winter > winter, otor > otter (Gmc *otraz < PIE *ud-ro- 'water animal', cognate with Greek hydra) are regular inherited forms. Water/wet/wash/otter are secure; winter shares the uncertainty of Gmc *wintruz. Note otter is not from any of the four Germanic words in the parent box but from a separate derivative *udro-.\",\n \"در انگلیسی water، wet، wash و otter (سمور آبی، از ژرمنی *otraz و هندواروپایی *ud-ro- «جانور آبی»، هم‌ریشه با hydra یونانی) بی‌گمان از این ریشه‌اند. winter همان تردید *wintruz را دارد. پس شاخه در کل پذیرفتنی است ولی پیوند winter تنها با احتیاط پذیرفتنی است.\",\n [WODR,W+\"Reconstruction:Proto-Germanic/wintruz\"],\n [{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"node carries no reference; AHD wed-1 §§1-4, 7a (WATER, WET, WASH, WINTER, OTTER) checked instead\"}],\n [{\"src\":\"KLN\",\"where\":\"KLN_1971 lines 265317 (water), 266254 (wet), 170032 (otter), 267519 (winter)\",\"stance\":\"partial\",\"note\":\"water/wet/otter from I.-E. *wed-/*ud- ('otter ... cogn. with OI. udrah, Avestic udra'); winter 'perh. ... the white season'\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985 line 1127\",\"stance\":\"supports\",\"note\":\"'WATER ... WET ... WASH ... WINTER ... *ud-ro- ... Old English otor, otter: OTTER'\"}]),\nn(13,\"Latin\",\"unda\",\"confirmed\",\n \"Latin unda 'wave, water' < *u-n-d-ā, nasal-infixed zero grade (or *ud-neh₂ with metathesis, de Vaan), cognate with Sanskrit unátti 'wets', Lithuanian vanduõ 'water'.\",\n \"«اونده» (unda) لاتینی به معنای «موج، آب» از صورت بی‌بالانده با میانوند خیشومی *u-n-d-ā (یا به نظر دِ وان *ud-neh₂) است و با سنسکریت unátti «تر می‌کند» و لیتوانیایی vanduõ «آب» هم‌ریشه است. ادعای نورایی درست است.\",\n [WODR],[ahd_rc(\"wed-1 §6: 'Suffixed nasalized zero-grade form *u-n-d-ā in Latin unda, wave: UNDINE, UNDULATE; ABOUND, INUNDATE, (REDOUND), REDUNDANT, SURROUND'.\")],\n cons_ie(\"'Latin unda, f. water, fluid, esp. a wave' (POK_full line ~8109)\",\"'Lat. unda „Welle, Woge“, undare „wallen, wogen“' (WLD_Bd1_pages line 23626)\")+[{\"src\":\"LAT\",\"where\":\"LAT.txt grep '^unda'\",\"stance\":\"supports\",\"note\":\"Ernout-Meillet: unda 'eau courante, onde', cf. skr. unátti, lit. vanduõ\"}]),\nn(14,\"Latin\",\"super-undere; red-undare\",\"transcription_suspect\",\n \"Late Latin superundāre 'to overflow' (super- + undāre 'to rise in waves', from unda) and Latin redundāre 'to overflow, run back' (red- + undāre) are correct derivations. But the book prints 'super-undere': there is no Latin *superundere; the form is superundāre (first conjugation, like red-undare beside it). This is Nourai's misprint; the extraction is faithful. The gloss 'wave around' is Nourai's; the attested sense is 'overflow'.\",\n \"superundāre در لاتینی پسین («لبریز شدن»، از super- «بر، فراز» و undāre «موج زدن» از unda) و redundāre («لبریز شدن، بازگشتن») درست هستند. اما کتاب «super-undere» چاپ کرده که در لاتین وجود ندارد؛ صورت درست superundāre (صرف اول، مانند red-undare) است. این خطای چاپی خود کتاب است و خوانش اسکن درست است.\",\n [WODR],[ahd_rc(\"wed-1 §6 lists REDUNDANT and SURROUND under Latin unda; the appendix does not quote the Latin verb forms.\")],\n [{\"src\":\"KLN\",\"where\":\"KLN_1966 line 37615 s.v. surround; KLN_1971 line 202451 s.v. redundant\",\"stance\":\"supports\",\"note\":\"'MF. soronder, to overflow, fr. OF., fr. Late L. superundare'; 'L. redundans ... pres. part. of redundare, to run over, overflow, fr. red- and undare, to rise in waves'\"},\n  {\"src\":\"LAT\",\"where\":\"LAT.txt grep 'redundo|superundo'\",\"stance\":\"supports\",\"note\":\"Ernout-Meillet s.v. unda: derivatives undo, -as; abundo, redundo, inundo (first conjugation)\"}],\n error_in=\"book\",book_prints=\"super-undere\",correct_form=\"superundāre\"),\nn(15,\"English\",\"surround ; redundant\",\"confirmed\",\n \"English surround (15th c., 'to overflow') < Anglo-Norman surounder / Old French soronder < Late Latin superundāre 'to overflow'; the modern sense 'encircle' (17th c.) arose by false association with round. Redundant (c.1600) < Latin redundant-, present participle of redundāre 'to overflow'.\",\n \"در انگلیسی surround (سدهٔ ۱۵ به معنای «سیلاب گرفتن») از فرانسوی کهن soronder و لاتینی پسین superundāre «لبریز شدن» است؛ معنای امروزی «دور گرفتن» به سبب پیوند نادرست (ریشه‌شناسی عامیانه) با round «گرد» پدید آمد. redundant از وجه وصفی لاتینی redundant- «لبریزشونده» است. کلاین و واتکینز همین را می‌گویند؛ ادعای نورایی درست است.\",\n [WODR],[ahd_rc(\"wed-1 §6: '... REDUNDANT, SURROUND' under Latin unda.\")],\n [{\"src\":\"KLN\",\"where\":\"KLN_1966 line 37615 s.v. surround\",\"stance\":\"supports\",\"note\":\"'The word orig. meant to overflow ... E. surround was influenced both in form and meaning by an erroneous association with the adjective round'\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt grep 'surround'\",\"stance\":\"supports\",\"note\":\"Skeat: surround < OF. suronder, souronder 'to overflow' < Late L. superundare; sense influenced by round\"}]),\nn(16,\"Latin\",\"ŭrîna\",\"confirmed\",\n \"Latin ūrīna 'urine' belongs to the *wer-/*wēr- 'water, rain' component of Nourai's composite root ('Wer 4'), not to *wed- proper: Pokorny 80-81 (au̯er-, same entry 78-81) and AHD wēr- 'water, liquid'; cognate Sanskrit vā́r(i) 'water', Avestan vār- 'rain', Old Norse úr 'drizzle'. The book's 'ŭ' (short) is a diacritic slip for ū, but harmless.\",\n \"«اورینا» (ūrīna) لاتینی به معنای «ادرار» از بخش *wer-/*wēr- «آب، باران» این ریشهٔ ترکیبی است (همان «Wer 4» نورایی)، نه از *wed-؛ هم‌ریشه با سنسکریت vāri «آب» و اوستایی vār- «باریدن». پوکورنی آن را در همان مدخل (ص ۷۸–۸۱) آورده و کلاین نیز از *wer- می‌داند. ادعای نورایی درست است.\",\n [W+\"urine\"],\n [ahd_rc(\"index line 2437: 'URINE wēr-' (separate root wēr- 'water'; Nourai's box lists Wer 4 as part of the composite root) — supports with that proviso.\")],\n [{\"src\":\"POK\",\"where\":\"pp. 80-81, au̯er- (POK_full line ~8178-8215)\",\"stance\":\"supports\",\"note\":\"'auer- water, rain, river ... Old Indic var, vari water, Avestan var rain'; 'Latin ūrīna urine' cited with Alb. shurrë 'urine'\"},\n  {\"src\":\"WLD\",\"where\":\"Bd. I 268 f. (WP. I 268 f., per Pokorny)\",\"stance\":\"supports\",\"note\":\"au̯er- 'Wasser, Regen' with lat. ūrīna (cited via Pokorny's references 'WP. I 252 f., 268 f.')\"},\n  {\"src\":\"KLN\",\"where\":\"KLN_1971 line 257965 s.v. urine\",\"stance\":\"supports\",\"note\":\"'L. urina, which is cogn. with OI. var, vari, water, Avestic vār, rain ... fr. I.-E. base *wer-, water, rain, wet'\"}]),\nn(17,\"English\",\"urine\",\"confirmed\",\n \"English urine (c.1300) < Old French urine < Latin ūrīna; it displaced native OE hland.\",\n \"urine در انگلیسی (حدود ۱۳۰۰) از فرانسوی کهن urine و آن از لاتینی ūrīna است و جای واژهٔ بومی hland انگلیسی کهن را گرفت. ادعای نورایی درست است.\",\n [W+\"urine\"],[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"node carries no reference; Klein checked\"}],\n [{\"src\":\"KLN\",\"where\":\"KLN_1971 line 257965\",\"stance\":\"supports\",\"note\":\"'urine, n. — ME., fr. MF. (= F.), fr. OF., fr. L. urina'\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt grep 'urine'\",\"stance\":\"supports\",\"note\":\"Skeat: urine < F. urine < L. ūrīna\"}]),\n]\ne0=dict(entry=0,root=\"Wed, Wer 4, Aŭe 2, Ud 2\",verdict=\"confirmed\",\n modern_form=\"PIE *wed- / *wód-r̥, *ud-én- 'water, wet' (with *wer-/*wēr- 'water, rain' for ūrīna)\",\n note=\"Nourai's composite box merges Pokorny's single entry 9. au̯e-d-, au̯e-r- 'to flow, wet; water' (IEW 78-81) with AHD wed-1 'water; wet' and AHD wēr- (for URINE). The chart (#1-#15) reproduces AHD wed-1 §§1-9 almost line by line. Only weak points: winter (Gmc *wintruz) whose 'wet season' etymology is one of several proposals (Klein: 'white season'; Wiktionary: unknown), and the book's misprint 'super-undere' for Late Latin superundāre. The Persian nodes are modern loans (hidrožen from French, viski from English, vodkā from Russian), glossed by Nourai with their etymological meanings.\",\n note_fa=\"ریشهٔ هندواروپایی آغازین *wed- (صورت‌های *wód-r̥ و *ud-én-) به معنای «آب، تر» قطعی است و پوکورنی (ص ۷۸–۸۱) آن را با *wer- «آب، باران» در یک مدخل آورده است؛ واتکینز (AHD) آن را wed-1 نامیده و نمودار نورایی تقریباً بند به بند از آن گرفته شده است. سه واژهٔ فارسی «هیدروژن»، «ویسکی» و «ودکا» وام‌واژه‌های نو از فرانسه، انگلیسی و روسی‌اند. تنها نقطهٔ سست winter «زمستان» است که پیوندش با «آب» یکی از چند پیشنهاد است، و خطای چاپی super-undere به جای superundāre. ادعای نورایی در کل درست است.\",\n sources=[WODR,\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wintruz\"],\n ref_check=[{\"ref\":\"POK:78\",\"status\":\"supports\",\"note\":POKQ+\": 'au̯ed- ... water', with Gr. ὕδωρ, Lat. unda, OIr. uisce (*udeskio-), Gmc water/wet/winter, OCS voda, and (au̯er-) Lat. ūrīna\"},\n  {\"ref\":\"AHD:1547,1549\",\"status\":\"supports\",\"note\":\"Watkins 1985 = same root list: \"+AHDQ+\" and line 1156/2437 'URINE wēr-' (page numbers 1547/1549 of the 1976 appendix match wed-1 and wēr- alphabetical position)\"},\n  {\"ref\":\"KLN:1732\",\"status\":\"supports\",\"note\":\"KLN_1966 local OCR stops in v-; KLN_1971 line 265317 s.v. water (the W-section around 1966 p.1732): 'fr. I.-E. base *wed-, *wod-, *ud-, water'\"}],\n consulted=[{\"src\":\"WLD\",\"where\":\"Bd. I leaf 261 (WP. I 252 f.)\",\"stance\":\"supports\",\"note\":WLDQ},\n  {\"src\":\"IEC\",\"where\":\"IEC.txt grep 'udōr|wodōr'\",\"stance\":\"supports\",\"note\":\"Mann lists *wed-/*ud- 'water' with Gk. hydōr, Lat. unda, Russ. voda\"},\n  {\"src\":\"SYN\",\"where\":\"SYN.txt §1.31 water\",\"stance\":\"supports\",\"note\":\"Buck: 'water' words from IE *wed-, *ud- (Gk. ὕδωρ, Goth. watō, ChSl. voda, Ir. uisce); Lat. unda 'wave'\"}],\n nodes=e0nodes)\n\ncons_np=[{\"src\":\"HRN\",\"where\":\"no. 264 (HRN.txt line 2657)\",\"stance\":\"supports\",\"note\":\"'264. beyoj, beyök Braut ... ai. vergl. vadhū- Braut; kurd. bük'\"},\n {\"src\":\"HUB\",\"where\":\"HUB.txt line 7086\",\"stance\":\"supports\",\"note\":\"'bayō, bayōg Braut = skr. vadhū'\"},\n {\"src\":\"CHEUNG\",\"where\":\"p. 200-201 s.v. *Hu̯adH (CHEUNG.txt line 13573-13640)\",\"stance\":\"supports\",\"note\":\"'*Hu̯adH to carry, lead (away); to marry (a wife)' ... 'NWIR: NP bayō bride, Kurd. bûk bride, daughter-in-law' ... 'MP wydwtk'n /wayōdagān/ nuptials, marriage' ... 'PIE *Hu̯edʰ- to lead, marry (a woman)' — Pok. 1115 f.\"},\n {\"src\":\"PHD\",\"where\":\"PHD.txt line 649 (p. 89)\",\"stance\":\"supports\",\"note\":\"'wayōdagān [wydwtk'n | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast' — MP antecedent of NP bayūgānī\"},\n {\"src\":\"NYB\",\"where\":\"NYB_vol2_glossary grep 'wayōt|wyd'\",\"stance\":\"silent\",\"note\":\"no entry for wayōdagān/wayūg found\"},\n {\"src\":\"BQT\",\"where\":\"vol. 1 p. 342 (leaf 562; ocr/BQT/0342.vision.txt)\",\"stance\":\"supports\",\"note\":\"'بیوگ - بفتح اول وضم ثانی ... بمعنی عروس است'; 'بیوگانی - ... عروسی را گویند چه بیوگ بمعنی عروس باشد'; Mo'in fn. 10: '= بیو، سانسکریت vadhû (عروس) ... اوستا vadh + upa (ازدواج کردن)'\"},\n {\"src\":\"ARY\",\"where\":\"pdf page 145 (ARY_pages.txt line 4226; Latin index line 4134)\",\"stance\":\"supports\",\"note\":\"'بیوگانی، ویوگانی (به چم عروسی)' with Avestan VADHUPA, Pahlavi VAYODAGAN, Kurdish BUK, Sanskrit VADHUS, Lith. VEDU\"},\n {\"src\":\"MON\",\"where\":\"MON_part1.txt line 27356; vajehyab.com/moein/بیوگانی\",\"stance\":\"supports\",\"note\":\"'بیوگ: [= بیو = ویو = ویوگ ... عروس، ازدواج کردن] (اِ.) عروس'; 'بیوگانی (حامص.) عروسی، نکاح'\"}]\ne2nodes=[\nn(1,\"Avestan\",\"vadhu, vadŭ 1; vadhu-upa\",\"plausible\",\n \"Avestan has vaδū- f. 'woman, wife' (V. 2; Bartholomae col. 1346) = Sanskrit vadhū́- 'bride', and the verb vad-, caus. vāδaiia- 'to lead', with upa- 'to give (a woman) in marriage' (YAv. upa.vāδaiiaēta V 14.15). Both continue PIE *wedʰ- 'lead (home a bride)'. But Nourai's forms are imprecise: 'vadhu' is the Sanskrit spelling (Avestan has δ, not dh), vaδū- is a noun 'woman', not a verb 'marry', and 'vadhu-upa' is an inverted rendering of upa + vad- taken from Mo'in's Borhan footnote ('اوستا vadh + upa (ازدواج کردن)'). Substance right, forms/glosses loose.\",\n \"در اوستایی vaδū- (اسم مؤنث) به معنای «زن، همسر» هست (هم‌ریشه با سنسکریت vadhū «عروس») و فعل vad-/vāδaiia- «بردن، راهبری کردن» که با پیشوند upa- معنای «زن به شوهر دادن» دارد. هر دو از ریشهٔ هندواروپایی *wedʰ- «(عروس را به خانه) بردن» هستند. اما صورت‌های نورایی دقیق نیستند: vadhu املای سنسکریت است، vaδū- اسم است نه فعل «ازدواج کردن»، و «vadhu-upa» وارونه‌خوانیِ upa + vad- است که از حاشیهٔ معین بر برهان قاطع گرفته شده. اصل سخن با احتیاط پذیرفتنی است.\",\n [W+\"Reconstruction:Proto-Indo-European/wedʰ-\"],\n [{\"ref\":\"POK:1115\",\"status\":\"supports\",\"note\":\"POK_full line ~88813: 'ued(h)-2 ... to lead: Old Indic vadhū- bride, young wife, woman, Avestan vaδu- ds., vāδayeiti (Kaus.) leads, with upa- eine Frau zur matrimony give' — supports both Avestan words (noun 'woman' and upa- verb 'give in marriage')\"}],\n [{\"src\":\"BRT\",\"where\":\"col. 1346 (BRT.txt line 22428-22429)\",\"stance\":\"partial\",\"note\":\"'j. vaδū- f. Weib, Frau ... ai. vadhu- f.; np. vgl. bayōg Braut' — noun 'woman', not a verb\"},\n  {\"src\":\"WLD\",\"where\":\"Bd. I leaf 263 (WP. I 255 f.)\",\"stance\":\"supports\",\"note\":\"'2. u̯edh „führen; heimführen, heiraten (vom Manne)“. Ai. vadhū-h „Braut, junge Frau“, av. vaδū- „Weib, Frau“, vāδayeiti (Kaus.) „führt“ ... mit upa- „eine Frau zur Ehe geben“' (WLD_Bd1_pages line 23844-23850)\"},\n  {\"src\":\"CHEUNG\",\"where\":\"p. 200 (CHEUNG.txt line 13573-13583)\",\"stance\":\"supports\",\"note\":\"'AVESTAN: vad- (vāδ-) to lead || (+ *upa-) to lead up (and on) ... OPT. med. 3sg. YAv. upa.vaδaiiaēta (V 14.15)'\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985 line 1129\",\"stance\":\"silent\",\"note\":\"AHD has only 'wedh- To push, strike [Pok. 1. u̯edh- 1115]'; the 'lead, marry' root is not in the appendix\"}]),\nn(2,\"Persian\",\"bayŭg; bayŭgânî\",\"confirmed\",\n \"NP bayūg / bayōg بیوگ 'bride' (variants بیوک، بیو; Kurdish bûk) < Old Iranian *wadū-ka-, diminutive/extension of the word seen in Av. vaδū- 'woman', Skt. vadhū́- 'bride': initial *w- > NP b- (as in *wāta- > bād), intervocalic *-d- > *-δ- > -y-, *-ūka- > -ūg. bayūgānī بیوگانی 'wedding' corresponds to MP wayōdagān 'nuptials, marriage feast' (MacKenzie, N bayēgān(ī)), from the verb *wad- 'lead (home)'. Both are attested in early NP poetry (Loghat-e Fors quotes Onsori for bayūgānī; the chart quotes Rudaki's line with 'nô bayūg').\",\n \"«بیوگ» (بیوک، بیو؛ کردی بووک) به معنای «عروس» از ایرانی باستان *wadū-ka- است، هم‌ریشه با اوستایی vaδū- «زن» و سنسکریت vadhū «عروس»: w آغازین در فارسی نو به «ب» بدل شده (مانند wāta- > «باد») و d میان دو واکه نخست به δ و سپس به «ی» رسیده است. «بیوگانی» (عروسی) با فارسی میانهٔ wayōdagān «جشن عروسی» (مکنزی) برابر است و از فعل *wad- «(عروس را) بردن» می‌آید. اسدی در لغت فرس، هرن، هوبشمان، چونگ و برهان قاطع با حاشیهٔ معین همه این را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n [W+\"بیوگ\",\"https://vajehyab.com/moein/بیوگانی\"],\n [{\"ref\":\"BQT:342\",\"status\":\"supports\",\"note\":\"BQT vol.1 printed p.342 (archive.org borhan-ghate-v1 leaf n562, read from image, saved ocr/BQT/0342.vision.txt): 'بیوگ ... بمعنی عروس است'; 'بیوگانی ... عروسی را گویند چه بیوگ بمعنی عروس باشد'; fn. 10 'سانسکریت vadhû (عروس) ... اوستا vadh + upa (ازدواج کردن)' — exactly Nourai's chain, including his 'vadhu-upa'\"},\n  {\"ref\":\"FRS:160\",\"status\":\"supports\",\"note\":\"FRS_pages.txt line 21925-21927 (Eqbal ed., different pagination): 'بیوگانی عروسی بود و بیوك عروس را خوانند، عنصری گفت: ساخت آنکه یکی بیوگانی / هم بر آیین و رسم یونانی'; also variant note line 12161 'بیوک عروس بود و بیوکانی عروسی'\"},\n  {\"ref\":\"AEF:264\",\"status\":\"not_checked\",\"note\":\"Khaleqi Motlaq's translation of Horn not online; AEF:264 = Horn no. 264, checked in HRN: '264. beyōγ, beyōk Braut ... ai. vergl. vadhū- Braut; kurd. bük' (HRN.txt line 2657) — supports\"}],\n cons_np),\nn(3,\"Sogdian\",\"wd\",\"confirmed\",\n \"Sogdian wδ- / wδ'w /waδu/ 'wife' (Buddhist and Manichaean texts; pl. wδ'yšt) < Old Iranian *wadū- < PIE *wedʰ-, cognate with Av. vaδū- and Khwarezmian wwd; Gharib p. 403 nos. 9955 and 9968. 'wd' is the unpointed transliteration of wδ-.\",\n \"واژهٔ سغدی wδ- / wδ'w (waδu) به معنای «زن، همسر» از ایرانی باستان *wadū- است و با اوستایی vaδū- و خوارزمی wwd هم‌ریشه؛ قریب در فرهنگ سغدی (ص ۴۰۳، شماره‌های ۹۹۵۵ و ۹۹۶۸) آن را از *wadu و سنسکریت vadhu می‌داند. ادعای نورایی درست است.\",\n [W+\"Reconstruction:Proto-Indo-European/wedʰ-\"],\n [{\"ref\":\"SOD:403\",\"status\":\"supports\",\"note\":\"SOD_pages.txt leaf 469 = printed p. 403: '9955 wδ- B, M waδuδ (wd-) < wuδ < waδw- < *wadu < *wad-; Khwar. wwd; Skt. vadhu ... wife'; '9968 wδ-w M waδuδ (wd-w, wδw(h)) < Av. vaδū; Ved. vadhu ... wife'\"}],\n [{\"src\":\"CHEUNG\",\"where\":\"p. 200-201 *Hu̯adH\",\"stance\":\"partial\",\"note\":\"Cheung lists the Sogdian verb (ptwyδ 'hand over') under the root; noun wδw not quoted but Sanskrit vadhū- 'bride' and Iranian bride words are\"},\n  {\"src\":\"BRT\",\"where\":\"col. 1346 vaδū-\",\"stance\":\"supports\",\"note\":\"Avestan counterpart 'vaδū- f. Weib, Frau'\"}]),\n]\ne2=dict(entry=2,root=\"Wedh 1\",verdict=\"confirmed\",\n modern_form=\"PIE *wedʰ- (LIV *h₂wedʰ-) 'to lead, lead home (a bride), marry'\",\n note=\"Pokorny 1115 f. 2. u̯edh- 'führen, heimführen, heiraten (vom Manne)'; Cheung *Hu̯adH 'to lead; to marry (a wife)'. Nourai's gloss 'to marry' is the specialized sense of 'lead home (a bride)' — acceptable. All three branches (Avestan vaδū-/upa-vāδaiia-, NP bayūg/bayūgānī, Sogdian wδw) are standard. The Avestan box's forms ('vadhu', 'vadhu-upa') are copied from Mo'in's footnote to Borhan p.342 and are imprecise (Sanskrit spelling; inverted upa + vad-), hence plausible for that node. Entry 1 (Wedh -> Wen) is a redirect and skipped.\",\n note_fa=\"ریشهٔ هندواروپایی آغازین *wedʰ- به معنای «بردن، عروس را به خانه بردن، زن گرفتن» است (پوکورنی ص ۱۱۱۵؛ چونگ *Hu̯adH «بردن، زن گرفتن»). معنای «ازدواج کردن» که نورایی آورده همان معنای ویژهٔ این ریشه است. «بیوگ» (عروس) و «بیوگانی» (عروسی) فارسی، اوستایی vaδū- «زن» و سغدی wδw «همسر» همه از این ریشه‌اند. تنها صورت‌های اوستایی نمودار (vadhu-upa) از حاشیهٔ معین بر برهان قاطع گرفته شده و دقیق نیست. ادعای نورایی درست است.\",\n sources=[W+\"Reconstruction:Proto-Indo-European/wedʰ-\"],\n ref_check=[{\"ref\":\"POK:1115\",\"status\":\"supports\",\"note\":\"POK_full line ~88808-88867, 'Root/lemma: u̯edʰ-2 ... Meaning: to lead ... Old Indic vadhū- bride ... Avestan vaδu- ds. ... Lithuanian vedu lead, guide; marry (of husband) ... Page(s): 1115-1116'\"}],\n consulted=[{\"src\":\"WLD\",\"where\":\"Bd. I leaf 263 (WP. I 255 f.)\",\"stance\":\"supports\",\"note\":\"'2. u̯edh „führen; heimführen, heiraten (vom Manne)“'\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985 line 1129\",\"stance\":\"silent\",\"note\":\"only 'wedh- To push, strike [Pok. 1. u̯edh- 1115]' — the 'lead/marry' root is absent from the AHD appendix\"},\n  {\"src\":\"CHEUNG\",\"where\":\"p. 200-201\",\"stance\":\"supports\",\"note\":\"'PIE *Hu̯edʰ- to lead, marry (a woman) ... LIV: 659 f. | Pok.: 1115 f.'\"},\n  {\"src\":\"IEC\",\"where\":\"IEC.txt grep 'wedh'\",\"stance\":\"supports\",\"note\":\"Mann: *wedh- 'lead, marry' with Skt. vadhū-, Lith. vedù\"}],\n nodes=e2nodes)\nout=dict(pdf_page=528,book_page=498,verified_by=\"claude-opus-5.5\",verified_on=\"2026-10-16\",entries=[e0,e2])\njson.dump(out,open(\"/home/sfmqrb/git/rishe-private/data/verification/page-528.json\",\"w\"),ensure_ascii=False,indent=1)\nEOF\ncd /home/sfmqrb/git/rishe-private; python3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p528/build528.py && python3 -m json.tool data/verification/page-528.json >/dev/null && python3 tools/verify_check.py 528",
 "description": "Build page-528 JSON and run checker"
}
```


### [2026-10-16T05:22:16.952Z] TOOL RESULT

```
nodes verified: 20/20
node verdicts: {'confirmed': 16, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 15, 'not_checked': 7}
books consulted: {'supports': 43, 'silent': 7, 'contradicts': 1, 'partial': 3} | by book: {'KLN': 15, 'WLD': 7, 'POK': 6, 'SKT': 5, 'ARY': 4, 'AHD': 3, 'CHEUNG': 3, 'MON': 2, 'LAT': 2, 'BRT': 2, 'HRN': 1, 'HUB': 1, 'PHD': 1, 'NYB': 1, 'BQT': 1}
```


## [2026-10-16T05:22:21.165Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for p in \"^Hydrogen\\|^hydrogen\" \"usquebaugh\" \"^Vodka\\|^vodka\" \"^Surround\\|^surround\" \"^Urine\\|^urine\"; do echo \"## SKT $p\"; grep -n -i \"$p\" SKT.txt | head -2 | cut -c1-300; done; echo \"## LAT\"; grep -n \"^unda\\|redundo\\|superundo\" LAT.txt | head -4 | cut -c1-300; echo \"## IEC\"; grep -n -i \"wodōr\\|udōr\\|vedh\\|wedh\" IEC.txt | head -5 | cut -c1-300; echo \"## SYN\"; grep -n \"1\\.31\" SYN.txt | head -3 | cut -c1-200",
 "description": "Verify Skeat, Ernout-Meillet, Mann, Buck claims"
}
```


### [2026-10-16T05:22:21.516Z] TOOL RESULT

```
## SKT ^Hydrogen\|^hydrogen
9012:hydrogen,   a  %-cr}'  light  gas.     (Gk.)    J Tlic   name  means  'generator  of  water.'*     ^ Gk.  dhpO',  for  tltup,  water  ;  and  the  baae liv',  to  produce:  see  OttDOBia.
## SKT usquebaugh
20523:Usquebaugh :  see  'Whiakey.
21395:UHquobaugh.  (Irish.)  Irish  uiige ^/ha,  usquebaugh,  whiskey.^ Irish  uitgTf water;  beatha,  life,  allied  to  Gk.  ^itn, life.
## SKT ^Vodka\|^vodka
## SKT ^Surround\|^surround
## SKT ^Urine\|^urine
20487:Urine.  (F.-L.)  F  yniw.-U  ir^« <^Gk.  oOpov,  urine ;  Skt  vdri^  nir,  wttf. Icel.  tir,  drizzling  rain;  A.  S,  im',  <c& Orig.  '  water.'
## LAT
69599:unda
69637:unda, -ae f.: eau (consid 4 r 4 e en tant que courante), onde, flot,
69656:exundS, M.L.3111 exundantia-, inundo, M.L.4534, inundatio - , redundo
79653:undar got., 565.
## IEC
7732:corylus, id.; Gaul. coslos, cosla, id.; OBr. cf. limn-collin, pl. -collou ‘lime-tree’; MIr. and Ir. coll, W coll ‘hazel’; Br. cf. kel-vez, Cor. coll- wedhen, id.; OHG hasal, id.; cf. hesilin, adj. ‘of hazel; OE hæsel ‘hazel’; Du. cf. hazel- noot *hazel-nut'; ON hasla, f. pl. hoslur ‘ha- zel'; L
12355:ðsis (0snos, Osen-) 'ash-tree; rowan’. WP I, 184 Skt. asanah, m. “Indian almond-tree'; Arm. orni, orni “alder; manna-ash' (from a type: *osinio-); Gk. cf. akher-ois, gs: -oídos, f. ‘white poplar beside sar-onís, gs: -onídos, f. ‘kind of oak’; ós-trus, f. ((rowan! or sim. tree); Lat. Ornus, gs:
20251:uidos, om, à, io “sight, shape, appearance, knowledge, aspect. WP I, 239 Skt. vid, vidya, f. ‘knowledge’; Av. vióya, f. id.; Myc. cf. pro-wido-, s. Cobserve or ‘re- serve’, fr. *pro- or *pros-); Hes. ido., m. ‘eye’; "dos, m. “way, means, shape’; cf. Gk. de- idia dark night’; mé-dea ('genitals'
20275:uidheuos, å ‘set aside, separated, separate’; (f.) ‘widow’. WP I, 240 Skt. vidhúh ‘solitary’; vidhávā, f. ‘widow’; Per. biva, bīve ‘widow’; Alb. e ve, f. id.; Lat. viduus ‘bereft, destitute, void”; vidua, f. ^wi- dow, unmarried woman'; (cf. the Rom. form via *vuidu-: Sard. boidu “empty, void';
20282:see uidus); Gaul. vidu- ‘forest’; OBr. uiid- ‘wood, tree’; W gw$dd, coll. ‘trees’; gwydden, f. ‘tree’; Br. gwéz, coll. as W; gwézen, f. sg. as W; cf. gwéz, adj. ‘wild’; Cor. gwydh, coll. as W; gwedhen, f. sg. as W; OHG witu, m. *wood, timber; MHG wit, wite m. n. id.; OS widu, m. “wood, forest;
## SYN
173:Similarly in regard to areal word distribution. No doubt, there are sey- eral significant instances of agreement in peripheral areas, e.g. in the Ro- mance field between Spanish-Portuguese and Rum
1220:1.31 WATER
1269:now the common generic word (muir prevailing in the name of special seas, as the Irish Sea, etc.) etym. disputed the old comparison with Ir. ferg ‘anger’ and the dxeavds Ovepyotvos of Ptolemy is
```


## [2026-10-16T05:22:24.597Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1220,1240p SYN.txt | cut -c1-400; sed -n 69637,69660p LAT.txt | cut -c1-200; grep -n -i \"wed-\\|\\bued-\\|uedōr\\|uodōr\" IEC.txt | head -5 | cut -c1-300; grep -n -i \"Whiskey\\.\\|^Whisk\" SKT.txt | head -3 | cut -c1-300",
 "description": "Read Buck water, Ernout-Meillet unda, Mann, Skeat whiskey"
}
```


### [2026-10-16T05:22:25.084Z] TOOL RESULT

```
1.31 WATER
Grk.  bdwp Goth. wats Lith. vanduo NG vepd ON vain Lett. adens Lat. aqua Dan. vand ChSl.  voda It. acqua Sw. vatten SCr.  voda Fr. eau OE weler Boh.  voda Sp. agua ME water Pol. _voda am apd aa water Russ. voda
usce u water Skt. jala-, Gp-, udan- put ae cee wazzar ; Abie ate :
B wfr HG ee lee
Br. dour NEG - carer ge ee
C-0. In Public Domain. Gurukul Kangri Collection, Haridwar
: e
| Digitized by Arya Samaj Foundation Chennai and eGangotri _ | \
oO
—_S ~~ Biotized by Arya Samaj Foundation Chennai and eGangotri
THE PHYSICAL WORLD IN ITS LARGER ASPECTS 35
The words for ‘water’, with few ex- belong to certain widespread nates, one of these reflect- ing what was clearly the general IE word for ‘water’, and three others also reflecting I words for ‘water’ , but per- haps in some more special application, such as ‘running water’ or ‘rain water’. Many words belonging to these groups appear in other lists, as under ‘sea’, “vave’, ‘river’, ‘rain’.
1. IE *wedor, *wodor, *uden-, a typi- cal r/n stem neuter, with gradation of the root syllable, fr. root *wed- in Skt. ud- ‘wet, flow’. Some forms with nasal in root syllable (intrusion from verb forms with nasal infix, or anticipation of n of stem). Walde-P. 1.252 ff. Er- nout-M. 1124.
Grk. téwp; Umbr. utur (Lat. unda ‘wave’); Ir. usce, NIr. uisce (Gael. wesge- beatha ‘water of life’ > NE whiskey); the Gme. group, Goth. waté, OF weter, etc.; Lith. vanduo, Lett. uidens, OPruss. wundan, unds; ChSl. voda, ete. general Slavic; Skt. wdan-; Hitt. watar, gen. we- tenas; Alb. wé.
2. IE *akva- or *akwa-. Walde-P. 1.34f. Ernout-M. 64. Walde-H. 1.60. Feist 18 f. Lat. aqua with its Romance derivatives. Elsewhere mostly of ‘run- ning water’ in words for ‘river’, as Goth. ahwa, OF éa, etc. (1.46). Here Hitt. eku-, aku-, Toch. yok- ‘drink’?
3. IK *a@p-. Walde-P. 1.46. Skt. dp-, ap- mostly pl. dpas, used esp. of the per-
ceptions, groups of cog
sonified ‘Waters’, Av. ap-, ap- the reg. word for ‘water’, also freq. personified, OPers. api-, NPers. ab ‘water’. Else- where only of ‘running water’ in words for ‘river’, as Lith. upé, Lat. amnis, Ir. abann, etc. (1.46).
4, IB *wer-. Walde-P. 1.268f. Skt. var-, vari, ‘water’ (of all kinds), Toch. A war, B war ‘water’. Elsewhere in words for ‘rain water, rain’, as Av. var-, ON ar (1.75), or for ‘sea’ or ‘lake’, as Av. vairi-, Lith. jurés, etc. (1.32, 1.33). Also Grk. obpov, Lat. wrina ‘urine’ (cf. NE make water).
5. Miscellaneous:
NG vepé fr. veapov (tdwp) ‘fresh water’, through vypdv (cf. Phrynichus vypdv dep ui) elrgs), with regular change of ir to er (Hatzidakis, Mec. 2.598).
unda, -ae f.: eau (consid 4 r 4 e en tant que courante), onde, flot,
(terne surtout po 4 tique, v. aqua). S'enploie au sg . et au pl. A le
sens figur 4 de notre "flots, tenpStes", e.g. Cic., Plane. 6, 15: campus
atque illae undae comitiorum. Bn architectare traduit le grec xu^oriov
"cinaise". Usit 4 de tout tenps. Panronan, M.l.9959 unda.
D 4 riv 4 s et conpos 4 s: undo, -Ss: etre agit 4 (en pariant de la ner);
ondoyer, onduler; couler A flots; enploy 4 tardivenent pour abunde.
- M.L.9060 et 9061 dndSius; - undosus (po4t.): aux flots agit4s,
orageux, M.1.9065; undulatus (varr.): ond4, ondul4, tir4 d'un dini-
nutif undula attest4 seulenent dans Bo&ce, nais qui subsiste dans
des dinlectes ronans, M.1.9066-9067; cf. aussi id. 9064 *undlcare;
- undBtim, undanter ( 4 poq.inp.); undebundus (id.);
abunde,-Ss’. d 4 border; sens noral "abonder". et "avoir en abondance".
Dans la 1 . grannaticale, traduit TtXeova^w "etre en trop", M.L. 53 , 53 -
-D 4 riv 4 s: abunde, abundanter, abundantia, abundStid; rapproch 4
de habere, dont il appar ait conne une forne renforc 4 e, d'oti la graphieunde
1300
frtquente h ab undo , et la crtation tardive de munerabundo. - deundS
(rare et tardif);
exundS, M.L.3111 exundantia-, inundo, M.L.4534, inundatio - , redundo
(= ueptCTCreuo)); redundanter, redundantia ; *sui>undS,-Ss, M.L.8406
Composta pottiques en undi-: -cola, -fluus, -fragus „ -sonus,
-uagus.
L'eau, considtrte come un objet, est expria^e an aentre par
7642:kopos, å (2) ‘heap’. Cf. WP I, 344 & 373 and next. Cf. kop- Alb. (ambig.) kapë (in place-names: ‘peak’. Cf. koup-); R kopà, Pol. kopa ‘heap’; cf. also Pol. kopny, adj. “snowed-under?
19521:udór (udor, obl: udn-) ‘water’. Cf. üdros, à, uodór, uodor, uodn-. WP I, 252 Skt. cf. udan, n. “water, wave’; Oss. cf. wdain, v. ‘water, wet, urinate? beside wdásin, v. “get wet; Myc. cf. (queried) udo(r), oblique: udoro-(!) ‘water’; Gk. hüdor, gs: hüdatos, n. id.; Umb. utur, loc. sg: une, n. 
19781:uás- (uós-?) — ued-
19795:ued- ‘speak, utter’. Cf. uod- Skt. vádami, v. ‘talk’; Gk. cf. aeído, v. (‘sing’, fr. *sm-uedio); W. cf. gweddi, pl. -iau, f. “pray- er; gweddïo, inf. denom. ‘pray’; OHG cf. (long-gde) far-wàzan, sv. 7. “curse?
21390:WHISK
21395:UHquobaugh.  (Irish.)  Irish  uiige ^/ha,  usquebaugh,  whiskey.^ Irish  uitgTf water;  beatha,  life,  allied  to  Gk.  ^itn, life.
23404:Oatlic :  brosc,  capercailzie,  cateran,  dan, claymore,  tillibeg  (philibcg),  gillie,  gowan, loch,  mackintosh,  pibroch,  platd,  ptarmi- gan, reel  (a),  slogan^  spleuchan^  sporran, whiskey.
```


## [2026-10-16T05:22:31.301Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"surround\" SKT.txt | head -3 | cut -c1-300; grep -n -i \"uedh\\|u̯edh\\|bride\" IEC.txt | head -5 | cut -c1-250",
 "description": "Check Skeat surround and Mann wedh"
}
```


### [2026-10-16T05:22:31.627Z] TOOL RESULT

```
7724:\fi\x,  1  kind  of  antelope.  (Hottentot.) 'ound  in  S.  Africa.  Said  to  belong  to  the [liottefiiot  lant^uage. ~  10  move  about,  proceed,  advance. M  E.  gvttt  i'Wf-  A  S.  gxm^  a  con- icled  lorm  of^n^n,  lo  go.'f-Du.  iiuiM, ft  ganga,  Daii.  guae,  Swed.  ^,  Golb. m  (pu
13768:Pericardium,  the  sac  surrounding  the hc.*rt.  (L.  —  Ck.)  h.  /cru-arUium.  —  Gk. wtpueAfiiioif.^GV.  wffti,  around  ;  xapMa,  the heart ;  see  Heart.
14285:complexion  (K.-U)  F. appearance.  —  L-  (ompiixiemi ccmplexio.  \  comprehending,  col of  body,  complexion.  —  L.  famfjti of  compUcli,  to  surround,  cnl com-  (rK«),  together:  piftten. pleach  (below").
793:audh-, see auedh-
858:auedhr- (ouedhr-, audhr-, əudhr-, audh-, oudh-) ‘air, wind, weather Am, cf. awd (o-st. ‘air, wind, heaven"); OHG wetar; OE weder; OCS vedrü (adj. “bright, clear), vedro “bright weather”; Li. cf. áudra “storm”
3370:(dhuedhuro, dhuedhruo, see dhuidhura)
5129:guëdhos, ā ‘bad; badness’. Cf. guðudh- and cpds. of guðu-. WP I, 695 MHG quat; LG quad; Du. kwaad, id.; Li. geda ‘disgrace’; gedetis, inf. “be ashamed’. MHG variants: kat, kot and quot, n. ‘filth’, of which G Kot is one. Short vowel in Du. kwett
10934:(1) 0). Cf. mnó (2) Tokh. AB mänt-, mānt- 'injure, destroy’; EMAIb. mund, m. mundë, f. ‘torture’; Alb. mund, v. (1) ‘conquer; MHG munt, sm. & f “hand, protection, permission’; G Vor-mund, m. ‘guardian’; OE mund, f. “hand: trust; guar- dian; bri
```


## [2026-10-16T05:22:32.844Z] AGENT

Now fix those consulted notes to match what the books actually say.


## [2026-10-16T05:22:43.749Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 - <<'EOF'\nimport json\np=\"data/verification/page-528.json\"; d=json.load(open(p))\ne0,e2=d[\"entries\"]\ndef node(e,i): return [n for n in e[\"nodes\"] if n[\"id\"]==i][0]\ndef setc(nd,src,new):\n    for c in nd[\"consulted\"]:\n        if c[\"src\"]==src: c.update(new); return\n    raise SystemExit(src)\nsetc(node(e0,2),\"SKT\",{\"where\":\"SKT.txt line 9012 s.v. hydrogen\",\"note\":\"'hydrogen, a very light gas. (Gk.) The name means generator of water. Gk. ὑδρο-, for ὕδωρ, water; and the base γεν-, to produce'\"})\nsetc(node(e0,6),\"SKT\",{\"where\":\"SKT.txt line 21395 s.v. Usquebaugh\",\"note\":\"'Usquebaugh. (Irish.) Irish uisge beatha, usquebaugh, whiskey. Irish uisge, water; beatha, life, allied to Gk. βίος, life'\"})\nsetc(node(e0,15),\"SKT\",{\"where\":\"SKT.txt grep 'surround'\",\"stance\":\"silent\",\"note\":\"no headword surround found in the OCR (only incidental uses, e.g. line 13768 'Pericardium, the sac surrounding the heart')\"})\nsetc(node(e0,17),\"SKT\",{\"where\":\"SKT.txt line 20487 s.v. Urine\",\"note\":\"'Urine. (F.-L.) F. urine — L. ūrīna; cf. Gk. οὖρον, urine; Skt. vāri, water; Icel. úr, drizzling rain ... Orig. water'\"})\nsetc(node(e0,13),\"LAT\",{\"where\":\"LAT.txt line 69637 s.v. unda (p. 1300)\",\"note\":\"'unda, -ae f.: eau (considérée en tant que courante), onde, flot ... Dérivés et composés: undo, -ās ... abundō ... exundō, inundō ... redundō'\"})\nsetc(node(e0,14),\"LAT\",{\"where\":\"LAT.txt lines 69656-69657 s.v. unda\",\"note\":\"'exundō ... inundō ... redundō ... *superundō, -ās (M.L. 8406)' — the compound is first-conjugation *superundāre, confirming 'undere' is a misprint\"})\nfor c in e0[\"consulted\"]:\n    if c[\"src\"]==\"IEC\": c.update(where=\"IEC.txt line 19521\",note=\"'udór (udor, obl: udn-) water. Cf. üdros, uodór ... WP I, 252 Skt. udan ... Gk. hüdor, gs: hüdatos ... Umb. utur'\")\n    if c[\"src\"]==\"SYN\": c.update(where=\"SYN.txt line 1220 ff., §1.31 WATER\",note=\"'1. IE *wedor, *wodor, *uden-, a typical r/n stem ... Grk. ὕδωρ; Umbr. utur (Lat. unda wave); Ir. usce, NIr. uisce (Gael. uisge-beatha water of life > NE whiskey); the Gmc. group ... ChSl. voda'; '4. IE *wer- ... Also Grk. οὖρον, Lat. ūrīna urine'\")\nfor c in e2[\"consulted\"]:\n    if c[\"src\"]==\"IEC\": c.update(stance=\"silent\",where=\"IEC.txt grep 'uedh|bride|vadh'\",note=\"no entry for *wedʰ- 'lead, marry' found in the OCR (only auedh-, auedhr-)\")\njson.dump(d,open(p,\"w\"),ensure_ascii=False,indent=1)\nEOF\npython3 -m json.tool data/verification/page-528.json >/dev/null && python3 tools/verify_check.py 528 | grep -c PROBLEM; python3 tools/verify_check.py 528 | tail -3",
 "description": "Correct consulted notes and rerun checker"
}
```


### [2026-10-16T05:22:44.332Z] TOOL RESULT

```
0
root verdicts: {'confirmed': 2}
ref checks: {'supports': 15, 'not_checked': 7}
books consulted: {'supports': 42, 'silent': 8, 'contradicts': 1, 'partial': 3} | by book: {'KLN': 15, 'WLD': 7, 'POK': 6, 'SKT': 5, 'ARY': 4, 'AHD': 3, 'CHEUNG': 3, 'MON': 2, 'LAT': 2, 'BRT': 2, 'HRN': 1, 'HUB': 1, 'PHD': 1, 'NYB': 1, 'BQT': 1}
```


## [2026-10-16T05:22:47.215Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; grep -n \"urina\\|ürina\\|ūrīna\" WLD_Bd1_pages.txt | head -3 | cut -c1-200",
 "description": "Grep WLD for urina"
}
```


### [2026-10-16T05:22:47.563Z] TOOL RESULT

```
23212:inenden Gdf. *ugros in der Sippe allein;, ir. fual, gen. f Ttail „urina“ *uoglo
```


## [2026-10-16T05:22:51.033Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 - <<'EOF'\nimport json\np=\"data/verification/page-528.json\"; d=json.load(open(p))\nn=[n for n in d[\"entries\"][0][\"nodes\"] if n[\"id\"]==16][0]\nfor c in n[\"consulted\"]:\n    if c[\"src\"]==\"WLD\": c.update(stance=\"silent\",where=\"WLD_Bd1_pages.txt grep 'urina|ūrīna'\",note=\"the au̯er- section (WP I 268 f., cited by Pokorny) was not found in the OCR; grep 'urina' only hits an unrelated Irish gloss (line 23212 'ir. fual ... urina')\")\njson.dump(d,open(p,\"w\"),ensure_ascii=False,indent=1)\nEOF\npython3 tools/verify_check.py 528 | grep -c PROBLEM",
 "description": "Fix WLD urine note and recheck"
}
```


### [2026-10-16T05:22:51.573Z] TOOL RESULT

```
0
```


## [2026-10-16T05:23:01.637Z] TOOL CALL #75: SubagentHandback

```json
{
 "message": "Page 528 (book page 498) is verified and written to /home/sfmqrb/git/rishe-private/data/verification/page-528.json. It is valid JSON, and `python3 tools/verify_check.py 528` shows 0 PROBLEM lines.\n\n**Scope:** 2 entries and 20 nodes. Entry 0 is the root \"Wed, Wer 4, Aŭe 2, Ud 2\" and entry 2 is \"Wedh 1\". Entry 1 (Wedh → Wen) is a redirect, so I skipped it.\n\n**Verdicts:**\n- Roots: 2 confirmed.\n- Nodes: 16 confirmed, 3 plausible, 1 transcription_suspect.\n\n**Plausible nodes:**\n- **Wed, Germanic #11 and English #12 (winter):** tying *wintruz to \"wet season\" is only one proposal. Klein prefers \"white season\" and Wiktionary calls the origin unknown. Water, wet, wash and otter are secure.\n- **Wedh 1, Avestan #1 (vadhu, vadŭ; vadhu-upa):** the content is right. Avestan has vaδū- \"woman\" and upa-vāδaiia- \"give in marriage\", as Pokorny p.1115 and Cheung both give. But \"vadhu\" is the Sanskrit spelling, vaδū- is a noun rather than \"marry\", and \"vadhu-upa\" turns Mo'in's \"upa + vad-\" around. That footnote is in Borhan p.342, which I read from the archive.org page image.\n\n**Transcription_suspect:**\n- **Wed, Latin #14, \"super-undere\":** the book prints it this way, so the error is in the book. The correct form is Late Latin superundāre (Ernout-Meillet lists *superundō, -ās). I saved the page image to data/verification/sources/refs/ocr/BOOK/528.png.\n\n**Extraction errors:** none. The JSON matches the printed page.\n\n**Other notes:**\n- The root box and nodes #1–#15 follow AHD wed-1 §§1–9 almost line by line. Urine comes from the *wer- part of the root (AHD wēr-; Pokorny pp.80–81).\n- All the cited references I could open support Nourai: POK pp.78 and 1115, BQT p.342, FRS (bayūgānī with a quotation from Onsori), SOD p.403 (nos. 9955/9968 wδw \"wife\"), Horn no. 264 (standing in for AEF:264), Mo'in online for hidrožen [French], viski [English] and vodkā, and Klein.\n- I could not check AHD:1410 or AHD:1460, which are main-dictionary pages of the 1976 edition that isn't online. The Watkins appendix supports the same arrows.\n- I saved my reading of the Borhan p.342 page to data/verification/sources/refs/ocr/BQT/0342.vision.txt, along with 0342.jpg. I archived 13 web pages with fetch_source.py."
}
```


### [2026-10-16T05:23:01.916Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
