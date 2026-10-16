# Verification process log — verify-page-520


## [2026-10-16T05:13:01.562Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 520 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-520.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-520.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-520.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 520` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:01.590Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:06.057Z] TOOL CALL #1: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md; echo ----; cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-520.txt; echo ----; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-520.json"
}
```


### [2026-10-16T05:13:07.112Z] TOOL RESULT

```
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
----
=== PDF page 520 (book page 490) ===
--- entry 0 ---
ROOT [Indo-European] Upo : to, from below  (refs POK:1106; KLN:1105)  PART 2
#1 (parent #0) [Indo-European] refs=POK:1105; KLN:1105 | Uper : over, above, beyond
  #2 (parent #1) [Avestan] refs=POK:1105; KLN:1105 | upairi : above, over, beyond
    #3 (parent #2) [Pahlavi] refs=HRN | apar : on, over, more than
      #4 (parent #3) [Persian] refs=BQT:79 | abar «ابر» : super ; bar 2 «بر٢» : over ☞Bhergh | extra: ابرمرد ، ابرقدرت ؛ برتر ، برترین ، برین | NOTE: See root "Bhergh" for another possible derivation.
  #5 (parent #1) [Latin] refs=AHD | super : over
    #6 (parent #5) [French] refs=None | 
      #7 (parent #6) [Persian] refs=AMD:1242; VOP:220 | sŭper «سوپر» : super | extra: سوپرمارکت
    #8 (parent #5) [English] refs=AHD | super, supreme, superior, sirloin
  #9 (parent #1) [Latin] refs=KLN | s-upper-mo, summus : peak
    #10 (parent #9) [English] refs=None | sum, summit
  #11 (parent #1) [Greek] refs=AHD | huper : over
    #12 (parent #11) [English] refs=None | hyper
  #13 (parent #1) [Germanic] refs=AHD | uberi : over
    #14 (parent #13) [English] refs=AHD | over
--- entry 1 ---
ROOT Urdu -> redirect to Urmak
--- entry 2 ---
ROOT [Indo-European] Urigh : rice  (refs IEC:1681)
#1 (parent #0) [Sanskrit] refs=AHD:1116 | Vrihi : rice
  #2 (parent #1) [Avestan / Old Persian] refs=KLN:1346 | brîzi, vriz, urvinj : rice
    #3 (parent #2) [Persian] refs=BQT:265; MON:198,5014; IEC:1681 | oroz «ارز» : rice ; varîzeh «وریزه» : rice ; berenj 2 «برنج٢» : rice
    #4 (parent #2) [Greek] refs=SYN:519; AHD:1116 | oruza : rice
      #5 (parent #4) [Latin] refs=None | oryza
        #6 (parent #5) [Italian] refs=None | riso
          #7 (parent #6) [French] refs=None | ris, riz
            #8 (parent #7) [English] refs=AHD:1116 | rice
----
{
  "pdf_page": 520,
  "book_page": 490,
  "entries": [
    {
      "root": {
        "name": "Upo",
        "lang": "Indo-European",
        "refs": "POK:1106; KLN:1105",
        "gloss": "to, from below"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "POK:1105; KLN:1105",
          "words": [
            {
              "translit": "Uper",
              "gloss": "over, above, beyond",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "POK:1105; KLN:1105",
          "words": [
            {
              "translit": "upairi",
              "gloss": "above, over, beyond",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Pahlavi",
          "refs": "HRN",
          "words": [
            {
              "translit": "apar",
              "gloss": "on, over, more than",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:79",
          "words": [
            {
              "translit": "abar",
              "gloss": "super",
              "script": "ابر"
            },
            {
              "translit": "bar 2",
              "gloss": "over",
              "script": "بر٢",
              "see": [
                "Bhergh"
              ]
            }
          ],
          "script_extra": "ابرمرد ، ابرقدرت ؛ برتر ، برترین ، برین",
          "note": "See root \"Bhergh\" for another possible derivation.",
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {
              "translit": "super",
              "gloss": "over",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "AMD:1242; VOP:220",
          "words": [
            {
              "translit": "sŭper",
              "gloss": "super",
              "script": "سوپر"
            }
          ],
          "script_extra": "سوپرمارکت",
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "super, supreme, superior, sirloin",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 1,
          "lang": "Latin",
          "refs": "KLN",
          "words": [
            {
              "translit": "s-upper-mo, summus",
              "gloss": "peak",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "sum, summit",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 1,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {
              "translit": "huper",
              "gloss": "over",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "hyper",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 1,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {
              "translit": "uberi",
              "gloss": "over",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "over",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Urdu",
        "redirect": "Urmak"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Urigh",
        "lang": "Indo-European",
        "refs": "IEC:1681",
        "gloss": "rice"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "AHD:1116",
          "words": [
            {
              "translit": "Vrihi",
              "gloss": "rice",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan / Old Persian",
          "refs": "KLN:1346",
          "words": [
            {
              "translit": "brîzi, vriz, urvinj",
              "gloss": "rice",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:265; MON:198,5014; IEC:1681",
          "words": [
            {
              "translit": "oroz",
              "gloss": "rice",
              "script": "ارز"
            },
            {
              "translit": "varîzeh",
              "gloss": "rice",
              "script": "وریزه"
            },
            {
              "translit": "berenj 2",
              "gloss": "rice",
              "script": "برنج٢"
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "Greek",
          "refs": "SYN:519; AHD:1116",
          "words": [
            {
              "translit": "oruza",
              "gloss": "rice",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": null,
          "words": [
            {
              "translit": "oryza",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Italian",
          "refs": null,
          "words": [
            {
              "translit": "riso",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": null,
          "words": [
            {
              "translit": "ris, riz",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "AHD:1116",
          "words": [
            {
              "translit": "rice",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-10-16T05:13:14.393Z] TOOL CALL #2: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; ls data/verification/sources/refs/ | head -100; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','HRN','BQT','AHD','AMD','VOP','IEC','SYN','MON','WLD','PHD','NYB','BRT','KNT','HUB','SKT','ARY']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-10-16T05:13:14.780Z] TOOL RESULT

```
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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
AMD {"title": "Hasan Amid, Farhang-e Farsi-ye Amid, 2 vols, Amir Kabir 1369/1990", "kind": "website", "url": "https://vajehyab.com/?q=<word>&d=amid ; https://abadis.ir/fatofa/<word>/ (فرهنگ عمید) ; scan on noorlib: https://noorlib.ir/book/view/28973?pageNumber=<N>&viewType=pdf", "lookup_hint": "Entry text online with origin tags ([پهلوی], [عربی]...); page numbers of the 2-vol 1369 print not mappable."
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09:
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root,
```


## [2026-10-16T05:13:38.674Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls data/verification/ | tail -5; python3 -c \"\nimport json;d=json.load(open('data/verification/page-518.json'))\ne=d['entries'][0]; print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:3000]); print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\n\"; sed -n 1,200p tools/verify_check.py | grep -n -i 'problem' | head -40"
}
```


### [2026-10-16T05:13:39.102Z] TOOL RESULT

```
.rw-r--r--   40k sfmqrb 14 Oct 22:50  page-514.json
.rw-r--r--   22k sfmqrb 14 Oct 22:47  page-515.json
.rw-r--r--   36k sfmqrb 14 Oct 22:51  page-516.json
.rw-r--r--   32k sfmqrb 14 Oct 22:48  page-517.json
.rw-r--r--   20k sfmqrb 14 Oct 22:48  page-518.json
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
 ]
}
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
}
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


## [2026-10-16T05:13:59.391Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/520.jpg; mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; R=data/verification/sources/refs; grep -n -i 'oryza\\|vrīhi\\|vrihi\\|brizi\\|vriz' $R/KLN_1966.txt | head -20; echo ---IEC; grep -n -i 'urīĝh\\|urigh\\|vrīhi\\|vrihí\\|oryza\\|óryza' $R/IEC.txt | head; echo --SYN; grep -n -i 'oryza\\|ὄρυζα\\|vrīhi' $R/SYN.txt | head"
}
```


### [2026-10-16T05:13:59.886Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   66k sfmqrb 14 Oct 22:15  site/pages/520.jpg
4288:bahuvrihi,  n.,  name  of  a  class  of  compounds (Old  Indian  gram.)  —  OI.  bahuvrihih,  ‘having much  rice’,  compounded  of  bahuh,  ‘much, numerous,  abundant’,  and  vriltih,  ‘rice’.  The first  element  is  rel.  to  Avestic  bazah-,  ‘height, depth’,  and  cogn.  with  Gk.  -ay;)?,  ‘thick’;  see pachy-.  For  the  second  element  see  rice, baignoire,  n.,  box  at  a  theatre.  —  F.,  ‘bath,  bath¬ tub;  box  at  a  theatre’,  fr.  baigner,  ‘to  bathe’,  fr. bain,  ‘bath’,  fr.  L.  balneum.  See  balneal  and  cp. bagnio.
9334:Coryphodon,  n.,  a  genus  of  extinct  mammals (palconrol.)  —  ModL.,  compounded  ofxrjp’j^r,, ‘head,  top,  summit',  and  o8e!>v,  gen.  o86vto?, tooth’.  Sec  coryphaeus  and  odonto-. coryza,  n.,  nasal  catarrh  (tiled.)  —  L.  coryza,  fr. Gk.  xcp’j^a,  ‘a  cold  in  the  head,  nasal  catarrh’, which  is  prob.  cogn.  with  OE.  hrot,  ‘thick  fluid, scum’,  OHG.  hroz,  roz,  ‘nasal  mucus’,  MHG., G.  rot:,  ‘nasal  mucus’,  OE.  hrutan ,  ‘to  snore; to  resound',  ON.  hrjota,  OS.  hrutan,  ON. hrjola,  OHG.  hrujjan,  ‘to  rattle  in  one's  throat’, cos,  cos  lettuce,  n.  Prop,  ‘lettuce  introduced from  Cos',  fr.  L.  Cos,  fr.  Gk.  KCjz,  one  of  the Aegean  islands,  now  called  Stanchio.  Cp.  Coan. cos,  n.  —  Abbresialion  of  cosine, cosecant,  n.,  the  secant  of  the  complement  of  an angle  (trigon.)  —  Formed  on  analogy  of  cosine and  cotangent  fr.  ModL.  complement i  secans. See  co-  and  secant.
26645:Oryza,  n.,  a  genus  of  cereal  grasses  ( bot .)  —  L., ‘rice’,  fr.  Gk.  8pu£a,  See  rice.
26882:—  Gk.  ■za.yo-,  fr.  r.oc/ui,  ‘thick,  dense',  for  I.-E. *bhnghus,  whence  also  OI.  bahiih,  ‘much,  nu¬ merous’;  cogn.  with  Avestic  bazah-,  ‘height, depth’  (for  *bhenghos),  Hitt,  pankush,  ‘large’, ON.  bingr,  ‘heap’,  OHG.  bungo,  ‘a  bulb’,  Lith. bless  (for  *bhenghus),  ‘thick’.  Cp.  the  first  ele¬ ment  in  bahuvrihi.
32853:rice,  n.  —  ME.  rys,  ris,  fr.  OF.  ris  (F.  riz),  fr.  It. riso,  fr.  VL.  *oryzum,  fr.  L.  oryza,  fr.  Gk. oputa,  fr.  OPers.  brizi,  fr.  Afghan  vrize,  ult.  fr.
32854:OI.  vrihih,  ‘rice’.  Cp.  Oryza,  risotto  and  the  sec¬ ond  element  in  bahuvrihi.
---IEC
--SYN
```


## [2026-10-16T05:14:03.209Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; grep -n -i 'rice' $R/IEC.txt | head -20; echo --SYN; grep -n -i '\\brice\\b' $R/SYN.txt | head -20; echo --AHD; grep -n -i 'rice\\|uper\\b\\|upo\\b' $R/AHD_watkins1985.txt | head -30"
}
```


### [2026-10-16T05:14:03.766Z] TOOL RESULT

```
<persisted-output>
Output too large (81.8KB). Full output saved to: /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/b5z5k9htc.txt

Preview (first 2KB):
1154:bhask- ‘tangle, network, bond WP II, 136. Cf. WP II, 106. Cf. bhaks- Phryg. báskioi (ffetters'. Hes.); báskein (Hes: légein); Gk. pháskos (f(bundle; tree-moss'. Hes.) beside phaskís ‘bundle’; Alb. (LW fr. Thrac. or Mac. ? bashkë ‘together’; *fleece"); Lat. fascis; MIr. basc ‘necklace, neckband'; W basg *basketry'; cf. MIr. bascaim ‘shackle, oppress’. (Note: ‘Scythian seers foretold the future by bundles of twigs’. Talbot-Rice: Scythians, p. 85)
1656:bhrik- ‘bristle, spike’. Cf. WP II, 201 Gk. phrix, beside phrike; OBr. cf. bricer ‘tuft, crest; W brig, m. “crown of tree; hair
2817:dhermos, à, io (dhermn-, dherom-) “firm, fixed; fixture, pact, order'. See dher- (2) and cf. WP I, 856 Skt. dhármah, dhárman; Tokh. (?) sarm ‘reason’; Arm. cf. darum (fend, term’, fr. *dherom-); Lat. firmus; LLat. firma “fixed payment; farm’; Umb. cf. ferime ‘firmly’; Ir. darmna (‘price-fixing or sim.); MHG térme,
3666:er$- (r-) (1) ‘right, proper, genuine’. Skt. (z-gde) rjuh ‘right, straight’; Av. orozus (id. & mue Per. arz ‘price, value; Go. -aírkns ‘genuine’; OHG &rchan, id.; OE eor- can-stáàn ‘genuine stone, gem’; ON jarkna- steinn, id.
3779:ombros, is (omber-) in Skt. àmbaram 'firma- ment’; Lat. imber beside imbrex 'roof-gutter' and ambrices ‘rafters’; Gk. ómbros (vocalism of ónoma). (A simplex may be present in Skt. ámbu *water' & Arm. amp 'cloud', but a
4268:gragos, is ‘harshness, roughness; horror, monster” Arm. arkack “mishap, evil' arkacim “suffer evil. Wrongly associated with arkk “evil”, see urg-); W grae ‘harshness’, graen “grief; grievous, severe’; LG krack ‘nag, jade’; Norw. krake ‘wizened creature, gnarled tree; EME cratch ‘scab, mange in horse’s leg’; Sw. kräk ‘reptile’, kräka, v. ‘creep’; OCS groza ‘horror’, grozavü ‘fouľ; R grozà ‘thunderstorm, threat’; Latv. graži, mpl. ‘temper, caprice’. (Isophonic are: MHG krachen, Du. kraken, OE cracian “crack, resound’; ON krak-ligr ‘frail’; Sw. krak ‘plunder’; ON kraki ‘barge-pole, boathook’, all without further connexions)
...
</persisted-output>
```


## [2026-10-16T05:14:07.008Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; grep -n -i \"'rice'\\|‘rice\\|oryz\\|óruza\\|vrih\" $R/IEC.txt | head -10; echo --SYN; grep -n -i 'rice' $R/SYN.txt | grep -i 'oryz\\|vrih\\|19\\.\\|518\\|519' | head -10; echo --AHD; grep -n -i 'oryza\\|^uper\\|^upo\\|\\buper\\b' $R/AHD_watkins1985.txt | head -30"
}
```


### [2026-10-16T05:14:07.400Z] TOOL RESULT

```
5863:(ruis, cf. geru-, geur-. Skt. jirvib, jívrih *de- crepit")
7485:ko-, px. ‘together’; intensive px. ‘very’. WP I, 458. Cf. kom Gk. cf. ko-nnéo (C(know', cf. noéo, noüs); ko-lophón ('peak,, cf. lóphos); kó-labos (*mor- sel”, cf. láb&); kokheuo (lift, fr. *ko-ue$h-?); koinós, adj. (common, cf. oinos "one: Lat. cf. c-0g0, co-actum; Olr. cf. cuman ‘he remem- bered'; cu-ing ‘yoke’; W cy-, cpds.; Blg. cf. kå (before a consonant); kám (before a vowel) ‘to’. (For Gk. kóruza ‘running cold”, cf. Kor-
--SYN
8025:Sp. cansado, pple. of cansar ‘tire’ (now trans.; refl. ‘get tired’), this (not : Fr. casser ‘break’ ifr. Lat. quassare ‘shake’, as Diez 91, REW 6939, but) = It. cansare ‘avoid’, fr. Lat. campsdre ‘turn aside from’, fr. Grk. xaépyar aor. Of kaurrw ‘bend’ (9.14). So Korting, Menéndez Pidal, C. C. Rice, Language 13.18 f., 19.154, Leo Spitzer, Language 14.205 f., Wartburg 2.156. Lat. campsdare occurs in Ennius in the nautical sense of doub- ling a headland (frequent in Grk.), then only in late Latin in more general sense of ‘turn aside from’ e.g. ut de via cam- semus Pereprinatio 10.8 and in many Blosses, The semantic development in Spanish was prob. (otherwise Rice) oan > ‘cease’ > ‘get hired INe ra as ie > es atl oie re 4 € association is there, ‘get tired? ae cho Russ. ustavat! 0 Slensich » ustate get tired, cease’ =
13094:RICE Lith. rysat Lett. risz ChSl. aes SCr. __riza, oriz Boh. ryze Pol. ryz Russ. ris Skt. vriht- Av.
20875:Goth. kaupén ‘carry on business’ (rpayparebecba, Lk. 19.3), ON kaupa ‘bargain, trade, buy’, sb. kaup ‘bargain, pay’, Dan. kjgbe, Sw. képa ‘buy’, OF céapan ‘trade, bargain’, rarely ‘buy’, sb. céap ‘bargain, trade, market, price’ (NE
24183:The proportional sense is also ex- pressed by the instr. sg. of ~ica derivs. of the coll. numerals (Leskien, Gram. 120), e.g. Celvericejg = rerpardoty Lk. 19.8, stitoricejq (so Zogr., etc.; stitokraticeja Mar.) = éxarovrardactova Lk. 8.8.
--AHD
340:bheue-. Also bheu-. To be, exist, grow. I. Extended forms *bhwiy(o)-, *bhwi-. 1. Germanic *biju in Old Eng- lish béon, to be: BE. 2. Latin fieri, to become (third person singular present subjunctive fiat): FIAT. 3. Possi- bly suffixed form *bhwi-lyo- in Latin filius, son; but this is possibly from dhé(i)-. II. Lengthened o-grade form *bhéw- in Germanic *béwan in: a. Old Norse bia, to live, prepare (present participle bondi); BONDAGE, BOUND‘; HUSBAND; b. Middle Dutch bouwen, to cultivate: BOW- ERY; C. Old Danish bdth, dwelling, stall, akin to the Scandinavian source of Middle English bothe, market stall: BooTH. III. Zero-grade form *bhu-. 1. Germanic *buthia in: a. Old English bold, dwelling, house, hence byldan, to build: BUILD; b. alternate Germanic form *béthla in Middle Dutch bédel, riches, property: BOoo- DLE. 2. Greek phuein, to bring forth, make grow, phutos, a plant, and phusis, growth, nature: PHYSIC, PHYSIO-, PHYSIQUE, -PHYTE, PHYTO-, PHYTON; DIAPHYSIS, DIPHY- ODONT, EPIPHYSIS, HYPOPHYSIS, IMP, MONOPHYSITE, NEOPHYTE, PERIPHYTON, SYMPHYSIS, TRACHEOPHYTE. 3. Suffixed form *bhu-td- in Welsh bod, to be: EISTEDD- FOD. 4, Suffixed form *bhu-tu- in Latin futirus, “that is to be,” future: FUTURE. IV. Zero-grade form *bhii- (< *bhua-). 1. Germanic *biiram, dweller, especially farmer, in: a. Old English bir, “dwelling space,” bower, room: BOWER}; b. Old English gebir, dweller (ge-, collective prefix; see kom): NEIGHBOR; Cc. Middle Dutch gheboer, ghebuer, peasant: BorR, Boor. 2. Germanic *birjam, dwelling, in Old English byre, stall, hut: BYRE. 3. Suf- fixed form *bhi-lo- in Greek phulon, tribe, class, race, and phulé, tribe, clan: PHYLE, PHYLETIC, PHYLUM; PHY- LOGENY. V. Suffixal forms in Latin. 1. *du-bhw-io-, “being two,” in Latin dubius, doubtful, and dubitdre, to doubt (see dwo-). 2. *pro-bhw-o-, “growing well or straightforward” (see per'). 3. *super-bhw-o-, “being above,” in Latin superbus, superior, proud (see uper). VI. Possibly Germanic *baumaz (and *bagmaz), tree (? < “growing thing”), in: a. Old English béam, tree, beam: uel b. Middle Dutch boom, tree: BooMm?. [Pok. bheu- 146. bheug-'. To flee. 1. Zero-grade form *bhug- in Latin fugere, to flee: FUGACIOUS, FUGITIVE; CENTRIFUGAL, FEVERFEW, REFUGE, SUBTERFUGE. 2. Extended form *bhuga in: a. Latin fuga, flight (> fugdre, to drive away): -FUGE, FUGUE; FEBRIFUGE; b. Greek phugé, flight: APOPHYGE. [Pok. 1. bheug- 152.] bheug-2. To enjoy. Nasalized zero-grade form *bhu-n-g- in Latin fungi, to discharge, perform: FUNCTION, FUNGI- BLE; DEFUNCT, PERFUNCTORY. [Pok. 4. bheug- 153.] bheug-*. To bend; with derivatives referring to bent, pliable, or curved objects. 1. Germanic *baugaz in: a. Old English béag, a ring: BEE?; b. Old High German boug, a ring: BAGEL. 2. Germanic *bugon- in: a. Old English boga, a bow, arch: Bow’; b. compound *alino- bugén-, “bend of the forearm,” elbow (*alino-, forearm; see el-'), 3. Germanic biégan in Old English bigan, to bend: Bow?, BUXxOM. 4. Germanic causative form *baug- Jan in Old Norse beyla, a swelling, akin to the probable Scandinavian source of Middle English baile, baill, a handle: Barn’. 5. Germanic *buhtiz in Old English byht, a bend, angle: BIGHT. 6. Celtic *buggo-, “flexible, mallea- ble,” in Scottish and Irish Gaelic bog, soft: BoG. [Pok. 3. bheug- 152.] bhilo-. Dear, familiar. Possible source of Greek philos, dear, loving (> philein, to love): -PHILE, -PHILIA, PHILO-, -PHILOUS, PHILTER; PAM. [Pok. bhili- 153,] bhiad-. To worship. Suffixed form *bhildd-(s)men- in Latin flamen, priest (of a particular deity): FLAMEN. [In Pok. bhlag-men- 154.] bhlag-. To strike. 1. Germanic *blak-, perhaps in the probable Scandinavian source of Middle English bakke, bat: BAT?. 2. Latin flagrum, a whip (> flagellum, little whip): FLAGELLATE, FLAGELLUM, FLAIL, FLOG. 3. Latin
542:shape): DELPHINIUM, DOLPHIN. 2. Prefixed and suffixed form *sm-gvelbh-o-, “born of one womb” (*sm-, one; see sem-'), in Greek adelphos, brother: -ADELPHOUS. [Pok. gtelbh- 473.] gvele-1. To throw, reach. Variant *g/é-, contracted from *guleg-, 1. Suffixed zero-grade form *g/-n-o- in: a. Greek ballein, to throw (with o-grade *bol- and variant *b/é-): BALLISTA; AMPHIBOLE, ASTROBLEME, CATABOLISM, DEVIL, (DIABOLIC), (EBLIS), ECBOLIC, EMBLEM, EPIBOLY, (HYPERBOLA), HYPERBOLE, METABOLISM, (PALAVER), PARABLE, (PARABOLA), (PARLEY), (PARLIAMENT), (PAR- LOR), (PAROL), (PAROLE), PROBLEM, SYMBOL; b. Greek ballizein, to dance: BALL?, (BALLAD), (BALLET), BAYA- DERE. 2. Suffixed o-grade form *gvols-d in Greek bolé, beam, ray: BOLOMETER. 3. Suffixed o-grade form *gwolo-sdé in Greek boulé, determination, will (< “throw- ing forward of the mind”), council: BOULE!; ABULIA. 4. Suffixed variant zero-grade form *gvele-mno- in Greek belemnos, dart, javelin: BELEMNITE. [Pok. 2. g¥el- 471.] gwela-2, An acorn. 1. Suffixed zero-grade form *g¥/o-nd- in Latin gldns (stem gland-), an acorn: GLAND, GLAN- DERS, (GLANDULAR), GLANS. 2. Suffixed zero-grade form *gulg-no- in Greek balanos, acorn, date: VALONIA; MYRO- BALAN. [Pok. 3. gvel- 472.] gven-. Woman. 1. Suffixed form *gven-d- in: a. Germanic *kwen6n- in Old English cwene, woman, prostitute, wife: QUEAN; b. Old Irish ben (> Irish Gaelic bean), woman: BANSHEE; C. Persian zan, woman: ZENANA. 2. Suffixed lengthened-grade form *gvén-i- in Germanic *kwéniz, woman, wife, queen, in Old English cwén, woman, wife, queen: QUEEN. 3. Suffixed zero-grade form *g“n-d- in Greek guné, woman: GYNO-, -GYNOUS, -GYNY; GYNAE- CEUM, GYNECOCRACY, (GYNECOLOGY), POLYGYNY. [Pok. gvend 473.) g”ere-'. Mountain. Possibly o-grade form *gvors- in: a. Greek boreios, “coming from the north” (? < “coming from the mountains of Thrace, north of Greece”), whence Boreas, the north wind: Boras; b. Greek Huperboreioi, Huperboreoi, name of a people living in the far north, variously explained as “they who live beyond the north wind” and “they who live beyond the mountains” (hu- per-, beyond; see uper): HYPERBOREAN. [Pok. 3. gver- 477.) gvere-2. Heavy. I. Zero-grade form *gra-. 1. Suffixed form “g“ra-u-i- in Latin gravis, heavy, weighty: GRAVE?, GRAVID, (GRIEF), GRIEVE; AGGRAVATE, AGGRIEVE. 2. Suffixed form “gro-u- in: a. Greek barus, heavy: BARITE, BARITONE, (BARIUM), BARYON, (BARYSPHERE), BARYTA; b. Sanskrit guru-, heavy, venerable: GURU. 3. Suffixed form *gro-es- in Greek baros, weight: BAR?, BARO-; CENTROBARIC, ISALLOBAR, ISOBAR. 4. Possibly *guri- in Greek bri- in compound *u(d)-bri- (see ud-). II. Suffixed extended form *g-rii-to- in Latin britus, heavy, unwieldy, dull, stupid, brutish: BRUT, BRUTE. III. Suffixed extended form *g»ri-g- in: a. Celtic *brig-o-, strength, in Italian brio, vigor: BRIO; b. Germanic *krig- in Old High German krég, chrég, stubbornness (> Ger- man Krieg, war): BLITZKRIEG, SITZKRIEG. IV. Suffixed full-grade form *gvero-nd-, millstone, in Old English cweorn, quern: QUERN. [Pok. 2. g¥er- 476.] gvere-*. To praise (aloud). 1. Suffixed zero-grade form *gvra-to- in Latin grdtus, pleasing, beloved, agreeable, favorable, thankful: GRACE, GRATEFUL, GRATIFY, GRATIS, GRATITUDE, GRATUITY; AGREE, CONGRATULATE, IN- GRATE, INGRATIATE. 2. Suffixed zero-grade form *gwro-do-, “he who praises,” in Celtic bardo-, bard, in Welsh bardd and Scottish and Irish Gaelic bard, bard: BARD}. [Pok. 4. gver(a)- 478.] gvere-4. To swallow. 1. Possibly suffixed extended form *gro-gh- in Germanic *krag-, throat, in: a. Old English *craga, throat, possible source of Middle English crawe, craw: CRAW; b. Middle Dutch craghe, throat: scrac. 2. Suffixed o-grade form *gvor-d- in Latin vordre, to swallow up: VORACIOUS, -VOROUS; DEVOUR. 3. Expres-
1097:upo
1105:uper. Over. 1. Extended form *uperi in Germanic *uberi in: a. Old English ofer, over: OVER; b. Middle Dutch over, over: ORLOP. 2. Variant form *(sjuper in: a. Latin super, super-, above, over: SOUBRETTE, SOVEREIGN, SUPER-, SUPERABLE, SUPERIOR, SUPREME, (SUPREMO), SUR-; SIRLOIN; b. suffixed form *(s)uper-no- in Latin supernus, above, upper, top: SUPERNAL,; C. suffixed form *super-bhw-o-, “being above” (*bhw-o-, being; see bheue-), in Latin superbus, superior, excellent, arrogant: SUPERB; d. suffixed (superlative) reduced form *sup-mo- in Latin summus, highest, topmost: SUM, SUMMIT; @. var- iant form *(s)juprd in Latin supra, above, beyond: (so- PRANINO), SOPRANO, SUPRA-; SOMERSAULT. 3. Basic form *uper in Greek huper, over: HYPER-. [Pok. uper 1105.]
1106:upo. Under, up from under, over. 1. Germanic *upp-, up, in: a. Old English up, uppe, up: uP; b. Old English up-, upp-, up=: UP-; C. Middle Dutch op, up: UPROAR. 2. Ger- manic *upanaz, “put or set up,” open, in Old English open, open: OPEN. 3. Germanic *ufana, “on, above,” in Old English bifan, above, over: ABOVE. 4. Possibly suffixed form *up-t- in Germanic *ufta, frequently, in Old English oft, oft: OFT, OFTEN. 5. Extended form *upes- in Germanic *ubasw6, *ubizwé6, vestibule, porch, eaves (< “that which is above or in front’), in: a. Old English efes,
1658:HUM kem-3 HUMAN dhghem- HUMANE dhghem- HUMBLE dhghem- HUMECTANT wegw- HUMERUS omeso- HUMID wegw- HUMILIATE dhghem- HUMILITY dhghem- HUMOR wegw- HUMUS dhghem- HUNDRED dekm HUNGER kenk-2 HUNKER keu-2 HURDLE kert- HUSBAND bheue- HUSSAR kers-2 HUSTINGS tenk-1 HUT (s)keu- HYATHODE sed-2 HYDATHODE wed-1 HYDATID wed-1 Hypra_ wed-! HYDRANT wed-! HYDRANTH andh- HYDRAULIC aulo- HYDRO- wed-1 HYDROCEPHALUS ghebh-el- HYDROMEL melit- HYDROUS wed-1 Hyprus_ wed-! HYENA sil- HYGEIA gWei- HYGIENE gWej- HYGRO- wegw- HYLOZOISM _hulé HYMEN  syil- HYMNODY wed-2 HYOSCINE si- HYPER- uper HYPERBOLA gWele-1 HYPERBOLE gWelg-1 HYPERBOREAN gWere-1 HYPERKINESIA kei-3 HYPERPNEA pneu- HYPHA webh- HYPNAGOGIC ag- HYPNO- swep-! Hypnos swep-! HYPNOSIS swep-1 HYPNOTIC swep-1 HYPO- upo HYPOCHONDRIA ghrendh- HYPOCORISM ker-3 HYPOGEAL gé HYPOPHYSIS bheue- HYPOPNEA pneu- HYPOSTASIS sta- HYPOSTYLE sta- HYPOTAXIS tag- HYPOTENUSE ten- HYPOTHERMIA gWher- HYPOTHESIS dhé-1 HYPROCRISY krei- HYPSO- upo HYSTERESIS ud- HYSTERIC udero- HYSTERO- udero- HYSTERON PROTERON per!, ud-
1997:ORGAN werg- ORGANOLEPTIC (s)lag¥- ORGANON werg- ORGASM wrdg- ORGEAT ghers- ORGY werg- ORIENT er-1 ORIFICE 6s- ORIFLAMME aurum ORIGIN er-1 ORIGINAL er-! ORINASAL 6S- ORIOLE aurum ORLOP klou-, uper OrMaAzD ansu-, men-1 ORMER mori-, ous- ORMOLU aurum, mele- ORNAMENT ar- ORNATE ar- ORNITHO- oF OROIDE aurum OROTUND 6s- ORPHAN orbh- ORPHREY aurum ORPIMENT aurum ORT ed-, ud- ORTHO- wrddh- ORTHODOX dek-1 ORTHOGONAL genu-1 ORTHOPEDICS pau- ORTHOSTICHOUS _steigh- ORTHOTICS wrddh- ORTOLAN gher-! os! Os-
2015:OVER uper
2264:SIREN twer-2 SIRLOIN lendh-1, uper SIRVENTE servus SISTER swesor- SISTRUM twei- sit sed-1
2276:SoL sdwel- SOLACE sel-2 SOLANINE sAwel- SOLAR sawel- SOLARIUM sawel- SOLE! sel-1 SOLE? s(w)e- SOLEMN sol- SOLICITOUS_ kei-3, sol- SOLID sol- SOLILOQUY s(wW)es, tolkw- SOLIPSISM s(w)e- SOLITARY s(w)e- SOLITUDE s(w)e- SOLO s(w)e- SOLSTICE sawel- SOLUBLE leu-1 SOLUM sel-1 SOLUTE leu-1 SOLVE leu-! SOMA teue- SOMATO- teua- SOME sem-! -SOME! sem-1 -SOME2  teue- SOMERSAULT sel-4, uper SOMNI swep-! SOMNOLENT swep-! SON seue-! SONANT swen- SONATA swen- SONE swen- SONG sengWh- SONIC swen- SONNET swen- SONOROUS swen- sooT sed-1 SOOTH es- SOOTHE es-
2277:SOP seue-2 SOPOR swep-1 SOPORIFIC swep-1 SOPRANINO uper SOPRANO uper SORCERER ser-3 SORDID swordo- SORDINO swer-2 SORE sai- SORITES teue- SORORAL swesor- SORORITY swesor- SORREL! siiro- SORREL? saus- SORROW swergh- SORRY Sai- SORT ser-3 SORTILEGE leg-1, ser-3 SORUS teue- SOTERIOLOGY teue- SOUBRETTE uper SOUFFLE bhlé-2 SOUGH (s)wagh- SOUND! swen- SOUND2 swento- SOUND3 swem- SOUND4 swem- SOUP seue-2 sOUR siiro- SOURDINE swer-2 SOUSE sal-1 SOUTANE upo SOUTH sawel- SOUTHERN sawel- SOUVENIR gWa- SOVEREIGN uper SOVIET sem-! sow! sé-1
2325:SUE sekw-1 SUFFER bher-1 SUFFICE dhé-1 SUFFICIENT dhé-1 SUFFIX dhig’- SUFFRAGAN bhreg- SUFFRAGE bhreg- SUFFUSE gheu- SUGGEST gerere SUICIDE s(w)e- SUINT sweid-2 SUITOR sekw-1 SULCATE selk- SULCUS selk- SULLEN s(w)e- SULTRY swel-2 SUM uper SUMMER! sem-2 SUMMIT uper
2327:suP2 seue-2 SUPER- uper SUPERABLE uper SUPERANNUATED at- SUPERB uper SUPERCILIOUS kel-2 SUPERCILIUM kel-2 SUPEREROGATE reg-' SUPERFETATE dh@(i)- SUPERFLUOUS bhieu- SUPERIOR uper SUPERJACENT yé- SUPERLATIVE tele- SUPERNAL uper SUPERNATANT sna- SUPERNUMERARY _nem- SUPERSCRIBE skribh- SUPERSEDE sed-1 SUPERSTITION sta- SUPERVENE gWa- SUPERVISE weid- SUPINE! upo SUPINE? upo SUPPLANT plat- SUPPLE plek-, upo SUPPLICATE plek- SUPPLY pele-1 SUPPORT per-2 SUPPOSE apo- SUPPRESS per-5 SUPPURATE pu-2 SUPRA- uper SUPRALAPSARIAN leb-1 SUPREME uper SUPREMO uper SUR- uper SURCULOSE swer-3 SURD swer-2
```


## [2026-10-16T05:14:11.512Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; grep -n 'upairi\\|uparí\\|upari' $R/POK_full.txt | head; grep -n -i 'upo\\b' $R/POK_full.txt | head -5; echo --WLD; grep -n -i 'upairi\\|uper\\b\\|úper' $R/WLD_band3.txt | head; grep -n -i 'upairi' $R/incoming/WLD/WLD_Bd1_pages.txt | head; grep -n 'upairi' $R/incoming/WLD/WLD_Bd2_pages.txt | head -3"
}
```


### [2026-10-16T05:14:11.993Z] TOOL RESULT

```
63184:"under', neologism after Indo Germanic *upeh{0\d Indie uparieio. "above'); 
6162:absorption from Indo Germanic *upo, and for Slavic po\x\ meaning ' behind, after ' m. Lok. 
6540:zero grade Lithuanian ore^ ploughing time ', compare gr. noAunpoq noAuapoupo(; Hes.), 
7579:ff.; 5£0t£ is formed in addition to 5£upo; also ouToq, aurn, touto most probably from 6, a, to 
7613:5£upo " here, well, all right, well then (an obsolete interjection meaning "come now") ' 
7617:(5£upaj after oniaaoj , inschr. SsOps after ays) from *5£-upo (5s " here ' + aupo " here '), 
--WLD
688:super umbr. 192. vopefe umbr. 431°.
```


## [2026-10-16T05:14:14.838Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; grep -n -i 'lemma: uper\\|lemma: upo\\|^uper\\|^upo' $R/POK_full.txt | head; grep -n -i 'upairi\\|upairi' $R/POK_03.txt | head; grep -n -c . $R/POK_03.txt"
}
```


### [2026-10-16T05:14:15.169Z] TOOL RESULT

```
1690:upon, appeal to '), cymr. add-, gall, ao'- prefix (e.g., MN Ad-iantu. cymr. ao'o'/a/?/" longing', 
31030:upon itself '), Latvian gnauzt'grasp with the hand, press' (Latvian znaugt' strangle, 
88131:Root / lemma: uper, uperi 
88137:Centum languages prove that Root/ lemma: uper, uperi: "over, above' derived from an 
88141:What becomes clear is the common gr.- celt, -kw- > -p-. Therefore Root/ lemma: uper, 
88143:uperi: "over, above' derived from the same root as the cognates for horse. This root 
88192:upo). 
88197:Root / lemma: upo, up, eup, (e)up-s- 
5975
```


## [2026-10-16T05:14:18.215Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; sed -n 88131,88240p $R/POK_full.txt"
}
```


### [2026-10-16T05:14:18.643Z] TOOL RESULT

```
Root / lemma: uper, uperi 

Meaning: over, above 

Note 

Centum languages prove that Root/ lemma: uper, uperi: "over, above' derived from an 

older Root/ lemma: *hukwer, *hukweri\ "over, above', later the old laryngeal was lost. 

What becomes clear is the common gr.- celt, -kw- > -p-. Therefore Root/ lemma: uper, 

uperi: "over, above' derived from the same root as the cognates for horse. This root 

developed from the concept of climbing a horse: Root/ lemma: eRuo-s: "horse'. The sky 

above was seemly called according to the horse goddess : gall. Epona' The Celtic horse 

goddess whose authority extended even beyond death, accompanying the soul on its final 

journey'. 

Note: related with upos. d. 

Material: 1 . Old Indie uparl, Avestan upalri, ap. uparly^ dbowi, about - toward, about - out 

(Akk.); about - toward (Instr); about (Gen.)'; Armenian probably / i/e/'"hinauf, above' 

(probably *uper, besides from Kasusformen from *upero-\) I veroy^M, oberhalb', / veray 

"above, darauf (these as preposition beim Gen. "about, auf); 

gr. uTTsp, proverb "about, about - out' and preposition "about - toward, oberhalb, about - 
out (Akk.); about' also in sense from Latin de; "zum protection, zum Besten (m. real Gen.; 
Arcadian with Dat.-Lok.)'; Latin Umbrian super{to s- see below upd) proverb "about, 
driJber' and preposition "about, about - toward, about - out (Akk.); about' ('Abl.' = Lok.); Old 
Irish for-, forpreverb "about, auf and preposition "about, about - toward, about - out (Akk); 
about auf ("Dat.' = Instr. or Lok.)', cymr. gor-, gwar-, corn, gor-, bret. gour-, gall, uer-tragus 
"a kind of schnellfuftiger Hunde', PN Ver-clngefo-r/x {das insel Celtic-o after Irish fo-, brit. 
gwo-); 

Celtic *vertamo-'the hochste' in VN Vertamo-corl(J), changing through ablaut cymr. 
gwar-thafheii^hi' {*vortamos); keltiber. ^e/'5/77c»s "summus' {*uperemos); 



Gothic ufar, Old \ce\av\6\c yfir {* uperi); Old High German uber{*uperi), with in Satzinlaut 
preserved /■ Old High German ubari, ub/n preverb "about' and preposition "about, about - 
toward, about = out (Akk.); about' ("Dat.' = Instr. or Lok). 

2. Old Indie upara-^\he untere, nahere' = Avestan upara-'t\r\e obere'; gr. uTTspoq 
"Morserkeule', unspa " upper rope, band' (unEpcoa " palate', unepcbiov " upper chamber ' 
are unclear); 

Latin super, superus' that is above, upper, higher ', Oscan supruis^ that is above, upper, 
higher' (therefrom Latin supra' Adv. over, on the top; of time, before, previously; in writing, 
above; of amount, etc.. over, more, beyond; Prep, with ace. above, over; of time, before; of 
amount, more than, above, beyond', super/or, supremus, Umbrian subra' above', supru 
Adv. "above'; Latin supernus' that is above, celestial, supernal ', Umbrian supernexu. Akk. 
" over, above, upon, on '); Gothic ufardf\6\. "about, above'. Old High German obaro Ad\. " 
that is above, upper, higher'. Old English yferra ds. {*uber/za, Superl. yfemestsee below 
upo). 

References: WP. I 192, WH. II 613 ff., Schwyzer Gr. Gr. 2, 518 ff. Mayrhofer 1, 105 f. 
Page(s): 1105-1106 

Root / lemma: upo, up, eup, (e)up-s- 

Meaning: under, from under, etc.. 

Note: from the meaning "from under hinauf die meaning "hinauf, about', die partly here, 

esp. but in related *uper(i){see d.), as well as in the group u4JnA6(; etc. ausgepragt is; Indo 

Germanic upo\s proverb (e.g. Old Indie upa-i-, gr. un-£ipi, Latin sub-ed) and preposition by 

variant case. 

Material: /. Old Indie ^pa proverb and preposition " toward - to (Akk.); an, by, to (Lok.); in 

Laufe from, gemaft, with in sense the accompaniment (Instr.)', Avestan upa, ap. upa 

proverb and preposition " toward - to, in, auf (Akk.); by, in (Lok.)'; 

gr. uno proverb and preposition "under an etwas heran, under etwas (Akk.); under an, 
under ("dative ', actually Lok. and partly perhaps Instr.); under; of Urheber beim Passiv 
(Gen. of Bereiehes); from under away, under - hervor (Abl.)'; 

Latin 5^i6'(s-from *[e]ks-, compare gr. s^unspGEv; -it* from -pas in ab= gr. airo), proverb 
and preposition "under an etwas heran, under etwas' (Akk.; also temporal, e.g. sub 
noctem); under an, under("Abl.', actually Lok.), as Oscan aun psSiKiai (partly perhaps 
Instr., as Umbrian su maronato' sub *maronatu'), besides subs- (as abs) in sustineo and 
in susque deque /fe/'d "aequo animo fero' (Gell.), compare also under die group from uijji. 



Umbrian sub-, su-, Oscan aun; Old Irish /opreverb and preposition "under' (Akk., "Dat.' = 
Lok. or partly perhaps Instr.), acymr. guo-, gu-, gua-, ncymr. go-, gwa-, corn, go-, gu-, bret. 
gou- proverb and in compound gall, vo- ( Voretus), ve- (gr. -Celtic-Latin parave-redus 
"Extrapostpferd', from which Modern High German Pferd); 

maybe alb. {*subeo, subito) shpejt 'sudden, fast'. 

perhaps cymr. gorau 'besi' from *uper-esu{= gr. UTT£p-£u "very good', L.-P. S. 186) or 
from * uper-gousom {compare S. 399) after Binchy J. C. stem 1, 148 ff.; das ofrom Celtic 
I/O-; with Old Indie upa-sthana-m ^Bed'\enung', upa-sti-, upa-stf-rc\. " subordinate, servant' 
compare Middle Irish /bss "servant' {*upo-sto-), cymr. bret. gwas, corn, guas ds., gall. PN 
Vasso-nxeic, Middle Latin vassus, vassallus, samtlich zur root sta-S. 1005, 1008, as also 
Old Irish /fc»//7 "replacement, equivalent' {fo+ ta) but Middle Irish fothae' foundation, origin, 
source, beginning; an ancestor ' from fo + suide (see 885);
```


## [2026-10-16T05:14:23.279Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; awk 'NR>88240 && NR<88330' $R/POK_full.txt | grep -n -i 'summus\\|super\\|Page(s)\\|ufan\\|up,' | head; echo ---KLN; grep -n -i '^summit\\|^sum,\\|^summa\\b\\|^super,\\|^super-\\|^supreme\\|^superior\\|^sirloin\\|^hyper-\\|^over,\\|^over\\b' data/verification/sources/refs/KLN_1966.txt | head -20"
}
```


### [2026-10-16T05:14:23.607Z] TOOL RESULT

```
4:Old Icelandic orabout, an, in'. Old English ufe-{*upo). Old High German uf{ufan) "auf (to 
15:Latin summus {*supmos) "the hochste' = Umbrian 50/770 "summum', compare also gr. 
22:alb. shume {* summus) [adv] " considerably, greatly, very ' 
51:Page(s): 1106-1107 
73:Page(s): 1 1 09 
---KLN
35351:sirloin,  n.,  the  loin  of  beef,  or  a  part  of  it.  —  A var.  spelling  of  surloin,  lit.  ‘the  upper  part  of  the loin’,  fr.  OF.  surlogne,  surlonge  (F.  surlonge), from  sur,  ‘above’,  and  logne,  longe  (F.  longe), ‘loin’.  See  sur-  and  loin.
37473:super-,  pref.  meaning  ‘above,  over’.  —  L.  super-, fr.  super,  ‘over,  above,  on  the  top  of;  beyond’, rel.  to  supra,  of  s.m.,  and  cogn.  with  OI.  updri, Gk.  trnsp,  ‘over,  above,  beyond’,  fr.  I.-E.  base *uper-,  *uperi-,  ‘over,  above,  beyond’,  which  is prop,  a  comparative  from  base  *upo-,  ‘from  be¬ low;  turning  upward,  upward;  up,  over,  be¬ yond’,  whence  also  L.  sub,  ‘under’.  See  over  and cp.  sub-.  Cp.  also  supra-,  soprano,  soubrette, sovereign,  superable,  superb.  Cp.  also  pref.  sur-, representing  OF.,  F.  sur. superable,  adj.,  surmountable.  —  L.  superabilis, ‘that  may  be  surmounted,  superable’,  fr.  supe- rdre,  ‘to  surmount’,  fr.  super,  ‘over,  above’.  See super-  and  -able.
37554:supreme,  adj.,  highest;  greatest.  —  L.  supremus, superlative  of  superus,  ‘that  which  is  above; higher’,  fr.  super,  ‘above’.  See  super-  and  cp. superior.
```


## [2026-10-16T05:14:27.009Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; grep -n -i 'summus' $R/KLN_1966.txt | head -5; grep -n -i '^over,\\|^over  *adv\\|^hyper-' $R/KLN_1966.txt | head; grep -n -i 'over,  *adv\\|^over\\b' $R/KLN_1966.txt | head -3"
}
```


## [2026-10-16T05:14:27.346Z] TOOL CALL #12: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/520.jpg"
}
```


### [2026-10-16T05:14:27.472Z] TOOL RESULT

```
8906:consultant,  n.  —  L.  consultans,  gen.  -antis,  pres, part,  of  consultare.  See  consult  and  -ant. consultation,  n.  —  L.  cdnsultatid,  gen.  -onis (either  directly  or  through  the  medium  of  F. consultation),  fr.  cdnsultatus,  pp.  of  consultare. See  consult,  v.,  and  -ation. consume,  tr.  and  intr.  v.  —  OF.  consumer,  fr.  L. consumere,  ‘to  take  entirely,  eat,  devour,  con¬ sume,  destroy’,  fr.  con-  and  sumere,  ‘to  take  up’, which  is  compounded  of  sub-  and  emere,  ‘to take’.  See  assume  and  cp.  words  there  referred  to. Derivatives:  consum-able,  adj.  and  n.,  consum- ed-Iy,  adv.,  consum-er,  n.,  consum-ing ,  adj.,  con- sum-ing-ly,  adv.,  consum-ing-ness,  n. consummate,  adj.,  consummated ;  complete,  per¬ fect.  —  L.  consummatus,  pp.  of  consummare, ‘to  accomplish,  finish,  complete’,  fr.  con-  and summus,  ‘the  highest,  topmost’.  See  summit  and adj.  suff.  -ate  and  cp.  consomme.
37429:sultana,  n.,  a  sultan’s  wife,  mother,  daughter  or sister.  —  It.,  fem.  of  sultano,  fr.  Arab,  sultan, ‘sultan’.  See  prec.  word, sultry,  adj.,  oppressively  hot.  —  Formed  from  the obsolete  verb  to  suiter,  a  var.  of  swelter. Derivatives:  sultri-ly,  adv.,  sultri-ness,  n. sum,  n.  —  ME.  summe,  somme,  fr.  OF.  summe, somme  (F.  somme),  fr.  L.  summa,  ‘top,  summit; chief  point;  amount’,  prop.  fem.  of  the  adj. summus,  ‘highest’,  used  as  a  noun.  Summus stands  for  *sup-mos  and  is  rel.  to  L.  super, ‘above’,  sub,  ‘under’.  See  sub-,  super-,  and  cp. summary,  summit,  consummate.  Cp.  also  OI. upamdh,  ‘the  highest,  uppermost’,  OE.  ufema,  of s.m.,  Gk.  tixazot;  (dissimilated  fr.  *ujrap.oi;),  of s.m.,  which  are  all  cogn.  with  L.  summus,  ‘high¬ est’.  For  the  sense  development  of  L.  summa, ‘sum’,  lit.  ‘the  highest’,  one  should  bear  in  mind that  the  Romans  used  to  write  the  sum  over  the addends  (in  contradistinction  to  our  own  habit of  putting  the  sum  under  the  addends). Derivatives:  sum-less,  adj.,  sum-less-ness,  n. sum,  tr.  v.  —  ME.  summen,  sommen,  fr.  OF.  sum¬ mer,  sommer  (F.  sommer),  fr.  ML.  summare,  fr. L.  summa.  See  sum,  n.
37441:OF. ,  fem.  of  somet,  dimin.  of  som,  ‘summit’,  fr. L.  summum,  prop,  the  neut.  of  summus,  ‘highest’, used  as  a  noun.  See  sum,  n.,  and  -et  and  cp. consummate.
24404:moreover,  adv.  - —  Compounded  of  more  and over.
26789:(for  *weqwnos,  ‘oven’.  Hence  oven  orig¬ inally  meant  'a  pot,  a  fire-pot’  (cp.  OE.  ofnet,  ‘a small  vessel').  Cp.  olio  and  olla  podrida. over,  adv.  and  prep.  —  ME.,  fr.  OE.  ofer,  ‘over, above',  rel.  to  OS.  obar,  ubar,  OFris.  over,  ur, ON.  yfir  (adv.  and  prep.),  Dan.  over  (prep.), Swed.  over  (prep,  and  adv.),  Norw.  yver  (prep, and  adv.),  OHG.  ubar,  ubir  (adv.  and  prep.), ubari,  ubiri  (adv.),  MHG.,  G.  iiber  (prep,  and adv.),  Goth,  ufar,  ‘over,  above’,  and  cogn.  with OI.  upari,  Avestic  upairi,  ‘over,  above,  beyond’ (adv.  and  prep.),  Arm.  i  ver,  ‘up,  above’,  Gk. U7r£p  (adv.  and  prep.),  L.  super,  ‘over,  above,  be¬ yond’  (adv.  and  prep.),  Gaul,  ver-  in  ver-tragus, ver-tagus,  ‘greyhound’,  and  in  PN’s  (as  in  Ver- cingetorix,  etc.),  OIr.  for  (for  *upor),  ‘above,  be¬ yond’.  All  these  words  derive  fr.  I.-E.  *uper, *uperi,  ‘over,  above,  beyond’,  which  is  prop, comparative  of  *upo,  ‘from  below;  turning  up¬ ward,  upward;  up,  over,  beyond’.  See  up,  adv., and  cp.  words  there  referred  to.  Cp.  also  hypo-, hyper- ;  sub-,  super-.
26790:Derivatives:  over,  adj.  (q.v.),  over,  tr.  v.,  to  get over  (rare)',  intr.  v.,  to  go  over  (rare);  over,  n., surplus,  excess;  also  a  term  of  cricket, over,  adj.  —  ME.,  fr.  uvere,  ‘upper,  higher’,  fr. OE.  uferra,  of  s.m.,  compar.  of  ofer,  adv.;  see over,  adv.  The  change  of  ME.  uvere  to  over  is due  to  the  influence  of  over,  adv.  Cp.  OHG. obaro,  MHG.  obere,  G.  ober,  ‘upper,  higher’, overanxious,  adj.  —  A  hybrid  coined  by  the English  novelist  Samuel  Richardson  (1689-1761) fr.  over,  adv.,  and  anxious,  which  is  of  Latin origin.
```


### [2026-10-16T05:14:27.559Z] TOOL RESULT

```

```


## [2026-10-16T05:14:36.153Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; grep -n -i 'urig\\|urīg\\|uri\\^\\|uriĝ\\|brinj\\|berenj\\|virinj\\|urvinj' $R/IEC.txt | head; tail -c 6000 $R/IEC.txt | head -80"
}
```


### [2026-10-16T05:14:36.959Z] TOOL RESULT

```
1731:bhrün- (bhreun-, bhrun-) ‘edge, top, crest, brow’. WP H, 196 & 207. Cf. bhrüs (1) Alb. bri, gs bm “tip, top, horn?” beside ` EMAIb. brinjë ‘rib, side, cliff, wall; Olr. cf. brú and Ir. bruinne “edge, shore, verge’; Cor. bron, pl. bronnow & bronyow *hill (all ambig. in view of homonymic brú, etc. ‘breast’, see bhrondh-); ON brún, pl. brýnn ‘cliff-edge, brow’ beside brýni ‘whetstone’; Dan.Sw. bryn ‘brim, edge, brow’, beside Sw. bryna ‘whetstone’; Li. (short vowel) bruns ‘brow’, beside brune ‘back of knife’; (*-eu- in) briaunà “edge, back of knife, keel. A possible link may exist (qua “acute, keen’) between Lat. frunitus ‘clever, in-frunitus ‘silly and ON brýnn “sharp, prompt'; brýna *sharpen, egg on'
14620:rigom, iom ‘thong, band, bond’. WP II, 347. Variant: uri- (?), q.v. Lat. cf. cor-rigium, -rigia, nf. ‘strap’; Mir cf. rigim, v. ‘tie, fetter, bond’; Cor. row, pl. -ow, f. “bond; strop’; MHG ric, gs: rickes, sm. id.; (Gisophone: G & LG Rick, sn. ‘stake, paling’). Variant of type *urig- in Sw. vrick, m. 'key- wind’; E wrick ‘sprain’
16012:skur- (skurð, io) (2) ‘thrust, poke Arm. rem. v. tr. id.; MHG schurn, schorn, v. ‘poke; jolt beside OHG scurigen, MHG schürgen, v. id. (and “incite'); OE scorian, v. (2) jut’; Du. schoren, v. “prop up, shore up’; schoor, m. "prop, stay, strut'; ON skora, v. (2) ‘urge, challenge’ beside skor-óa, f. ‘stay, prop’; Cz. cf. skeřit zuby, v. ‘bare the teeth’; skeřit se ‘grin’
16986:spur- (sphur-) (3) ‘spur, spike, shoot, sprout’. Cf. sphur- Gk. spurós, m. ‘spring corn’; Li. spurai, mpl. ‘fringe’; spürenos, fpl. s. ‘Hnt; Latv. spuras, fpl. ‘fibres, floss’; spurigs, adj. ‘bristly’. (In sense of ‘spur, heel’, see sphur-)
Gk. lóphos, m. ‘neck, mane, tuft, crest, peak'; lophía, f. id.; Maced, cf. otto-lobus ('eight- hill, a place-name); cf. also Gk. ko-lophón, m. (top, peak, if fr. *Kor-ulobhon, cf. Kor-, Kor-) (hardly Tokh. A lap “head? as V. Windekens)
ulod- “evil, harmful, poisonous; harm, poi- son. (Lat. ambig.)
ulon- — ulg-
20
25
30
35
40
45
1552
Skt. cf. a-vrade, mp. ‘grow soft’; Lat. cf. lolium, n. ‘tare’; lol-igo, gs: -1ginis, f. (“cuttlefish”, lit. *ink-creature); MLG wlete, s. "injury; (MHG lez, letze, adj. “bad, wrong' ambig. since OE lettan, v. "harm, oppress': EME let, s. & vb.: Go. ga-latjan, v. ‘hinder’ do not derive from a type *ulod-)
(ulong-, see Supt: U)
uldh- (1) ‘grow strong, thrive". Skt. ambig. Cf. ueldho, but also uordh- (2) Skt. vrdhah adj. & s. ‘cheerful; cheerer'; Av. voroÓ-, v. ‘promote’ (Here: R. Kent); Per. gurd, s. (hero'. Here Justi); Arm. cf. bat, i, iv, adj. (strong, grand, vast’, fr. *epi-uldht-); also cf. h-ayt'em, v. ‘conquer’; Gk. álthomai, v. ‘grow, get strong, recover’; álthos, n. fre- medy’; cf. am-áltheia, f. ((cornucopia', fr. *sm-^); ep-althéo, v. ‘cure’; epalthés (‘cura- tive: Arm. hayt); OE wuldor, n. Cëlorg, praise, thanks, heaven': Gk. álthos, eos, but not: Go. wulpus, see ultos, us); MHG cf. wulst, sm., wulste, sf. (“bulge, bustle', fr. *uldht-); G cf. wulstig, adj. 'blubberlipped'; Wulst, mf. pl. -ü- ‘hump, boss, pinnacle
uldh- (2) “mild, lukewarm' W gwlydd, adj. ‘mild, soft, tender, gentle’; s. pl. -ion ‘greenery’; Li. vildau, yti, v. ‘make tepid'
(ule-, cf. uelaio. Zero-gde perh. in Gk. aleé, f. “flight, avoidance’; Fr. vol, It. volo, m. ‘flight’)
ulëið (@ul-, uol-, *uol-) “be strong’. See ual- (2) and cf. uel- (6)
ulg- *wet, damp; dampen'. WP I, 306. Cf. uelg-, (variant uolg-) Alb. lag, v. (^wet', via a type *ulog-, cf. valë ‘wave’ and i parë 'first); W glaw (occasionally gwlaw), m. ‘rain’; Cor. glaw, m., Br. glað, m. id.; MHG cf. wolken, wulken, s & wf. “cloud, welkin'; cf. wolkern, wulkern, sf. ‘cloudy urine’; Du. wolk, f. ‘cloud’; OE wolcen, m & n. (2), id.; Fris. wolk, wolke, wolken & wolkem, id.; Norw. ulka, ulke, f. ‘slime’; cf. OCS vlügü- kú, adj. (^wet, fr. *ulguko-); Cz. vlhký, id.; Pol. cf. wilgnac, intr. ‘grow damp’; Ukr. vox- kyj, adj. “wet, damp”; Li. cf. vilgstu, vilgti, intr. grow damp’ beside vilgau, yti, tr. *dam- pen’. (O-gde in OCS, R vlága, Cz. vláha, f.
1553
‘moisture’; OCS vlaZinú, Cz. vlahý and vlažný ‘damp’, fr. *uolg-. Variant of type ulog- in OE wlzec E wlacu, adj. 'tepid) Lusatian wloha ‘moisture’ confirms o-gde, as Latv. velgs, adj., velgt, v. beside valgs, valgt ‘moist; become moist. Skt. vrjánam, n., vrjanih ‘sky; cloud? is isolated
ulgh- ‘tepid’. Variant of ulg- (?). Cf. uolgh- Arm. gayğ, Let id.; Icel. volgur, id.
ulguó, v., ulguos, us, s. ‘surge’. Variant in ON ulguh-? but cf. uluos, uluió Gk. cf. (?) kas-albás, gs: -albádos, f. (harlot', if for *kmt-, q. v. and *ulgu-); Lat. vulgus, gs: -i, m. & n. ‘crowd, rabble’ beside volgiolum, n. ‘roller’; volgi-vagus ‘wandering, strolling’; Icel. cf. volk, n. ‘billowing; toil’ (beside ylgja, f. ‘swell, surge’ fr. (?) *ulguhiə. Lat. vulba ‘bag, budget, late Lat. bulga is ambig. Skt. várgā ‘sect, class’ seems to be unrelated)
(ulio (1) ‘wind, wrap’, see uluið; (2) ‘boil’, see ulāið)
ulksuos, à (ul'suos, à) (?) ‘sorcerer, prophet Gk. cf. (?) álsos, n. ‘sacred grove’; ON cf. volva ‘prophetess’; OCS vlüxvü, m. ‘prophet’; vlüxvij, adj. *magical'; Blg. vláxva, m. *high- wayman'; LW in Finn. velho ('sorcerer', vocal- ism of Finn. verho “top”, cf. urks- (4))
ulm- ‘surge, billow; wide mouth, gulf’. WP I, 298. Gk. ambig. & uncertain Skt. ürmíb, mf. ‘wave, billow’; Gk. cf. lámos, m. ‘gulf; lámia, f. ‘monster, wide-mouthed fish’; cf. lamurós ‘deep, awful; riotous’; Arm. cf. aymuk, gs: aymki, ab. s. aymkav, s. *up- roar’; OE wylm, m. ‘surge, billow, boiling’; G (7) Wolm, m. ‘archway, porch, curved ba- nister’; ON olmr, adj. ‘wild, boisterous’. (Iso- phone: Li. vilminti, inf. ‘cheat’)
uln- (1) (ulna, ulon-) ‘wool’. WP I, 206. (Var- iant initial in Oss.) Skt. urna, f. id.; Av. cf. una, f. “lock, curl’; Oss. cf. qun, Dig. gun, s. ‘wool, hair’; Hitt. cf. hulana-, Luvian hulani- (queried: *wool"); Lat. lana, f. id.; Ir. olann, gs: olna & olla, f. id.; W gwlan, OBr. gulan, Breton gloan, m. id.; OHG wolla, f. id.; Go. wulla, f. id.; OE wull, wll f. id.; ON ull, ds: ullu, f. id.; OCS vlüna, Cz. vina, Pol. wełna, Big. vlána, id.; Li. vilna, Latv. vilna, id.
ulgh- — ulquos, is
20
25
30
35
40
45
1554
uln- (2) (ulnis, à) ‘surge, wave’. WP I, 302- 3. (Gk. ambig.) Oss. wlän ‘wave’; Arm. cf. alik, gen. aleaç, abl. aleawk, id.; Gk. cf. alés, halés, adj. ‘surg- ing’; but Gk. hális, adv. (“in a mass’ equally fr. a type *uluit-, see uluió and extns.); Alb. valë, pl. id., f. ‘wave’; OE wll m. ‘fountain’; OCS vlüna, Cz. vina, f. (2) ‘wave’; Li. vilnis, i&s, f. id.; Latv. vilnis, id.
(ulnio (1) see uluið; (2) see ulaið) (1) only in Skt. ürnómi, v. ‘envelop’; (2) only in Gmc. cf. Go. wulan and OE wylian 'seethe? beside wyllan, v. id. (fr. *ulnio)
ulquátis, os *tearer, devourer, killer’. Cf. ul- quos (1) Skt. vrkátih, m. ‘robber, murderer’; Slovene volkác ‘Alsatian dog’; Li. vilkátas, m. *wer- wolf; Late vilkatis, vilkacs, id.
ulquio ‘she-wolf’. Cf. ulquos (1) Skt. vrkih, id.; OE welt id. MHG (Upper Ger) wülpe, id.; ON ylgr, ds: ylgi, id.; Li. vilke, id.
ulquó, ið (ambiguous consonantism, unless related to type ulquos, etc. see next). Skt. varke, mp. ((seize', but cf. type *uelk-) beside vrkah (2) '(plough'; Srb. vučem, v. ‘drag’; cf. OCS (hapax) vlüci, s. (Ccaltrop? or sim.); Li. vilkiu, eti, v. ‘wear — a garment’; cf. vilktas, m. (tech. *priming); L
```


## [2026-10-16T05:14:40.835Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; grep -n -i \"oruz\\|óryz\\|‘rice’\\|'rice'\\|(rice\\|brinj\\|vrī\" $R/IEC.txt | head; grep -n '^168[01]$\\|^1679$\\|^1682$' $R/IEC.txt | head; sed -n 13090,13100p $R/SYN.txt"
}
```


### [2026-10-16T05:14:41.269Z] TOOL RESULT

```
1731:bhrün- (bhreun-, bhrun-) ‘edge, top, crest, brow’. WP H, 196 & 207. Cf. bhrüs (1) Alb. bri, gs bm “tip, top, horn?” beside ` EMAIb. brinjë ‘rib, side, cliff, wall; Olr. cf. brú and Ir. bruinne “edge, shore, verge’; Cor. bron, pl. bronnow & bronyow *hill (all ambig. in view of homonymic brú, etc. ‘breast’, see bhrondh-); ON brún, pl. brýnn ‘cliff-edge, brow’ beside brýni ‘whetstone’; Dan.Sw. bryn ‘brim, edge, brow’, beside Sw. bryna ‘whetstone’; Li. (short vowel) bruns ‘brow’, beside brune ‘back of knife’; (*-eu- in) briaunà “edge, back of knife, keel. A possible link may exist (qua “acute, keen’) between Lat. frunitus ‘clever, in-frunitus ‘silly and ON brýnn “sharp, prompt'; brýna *sharpen, egg on'
11166:mormolos (mormoros) ‘murmur; humming creature, murmurer. Cf. murmur-, etc. Skt. marmarah ‘murmur, rustle’; Gk. cf. mor- moruzo ('frighten'. A formal equivalent, re- dup. to moros, q.v); Li. marmalas ‘gadfly’; cf. marmu, eti, v. ‘murmur’. WP II, 307
igitized by Arya Samaj Foundation Chennai and eGangotri
519
Meyer-Liibke, Arch. sl. Ph. 36.591, after Weigand). In It. dial. colwmbine, used of the white popping corn, the associa- tion with doves is more obvious.
5. SCr. kukuruz, etc., general Slavic, whence also the Lith. and Lett. terms, prob. not loanword fr. Turkish (as in Miklosich, Tiirk. Elem. 1.334, Lokotsch 1230), perh. related to certain Slavic plant names, but uncertain. Berneker 640. Briickner 280.
RICE Lith. rysat Lett. risz ChSl. aes SCr. __riza, oriz Boh. ryze Pol. ryz Russ. ris Skt. vriht- Av.
of the word seen in Skt. vrihi- (AV-+), Afghan vrizé, etc. Boisacq 712. Schra- der, Reallex. 2.230.
8.51 GRASS ba, xbpros Goth. hawi Lith. Zolé Ses 3 ON gras Lett.  zale ae, aroier Dan. gras ChSl.  trava herbe Sw. gras SCr.  trava hierba or gr@s, gars Boh.  irdva . tarba ME gras Pol. trawa fer NE grass Russ. trava fear Bua gras Skt. trna- pp, glaswellt MHG a ae Av. (vasira-) Words f, paiey off ‘ or ‘ ass’ tons as ‘green, prowine from such no- Grk. xépros, orig. ‘enclosure’, esp. 'D part also from fodde fat blade’, but | ‘feeding place for cattle’, whence ‘fodder, &t Was Usually grasg er’, since the fod- | grass, hay’ : Lat. hortus ‘garden’ (8.13), «tk. xb, Ton ia D Ir. gort ‘field’ (8.12), etc. Walde-P. Toy fot? 7 Vor. rota, fr. | 1.603. Hence NG xoprépt.
“ , Lith. péva ‘meadow’, 14, ' V+ Pivah- ‘fat?, ete. Walde-
2. Lat. herba (> It. erba, Fr. herbe, Sp. hierba, yerba, Rum. iarbé), etym.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
520
```


## [2026-10-16T05:14:43.222Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; grep -n -B3 \"Afghan vriz\" $R/SYN.txt | head -20; grep -n \"8.43\\|RICE\" $R/SYN.txt | sed -n 1,10p | cut -c1-200"
}
```


### [2026-10-16T05:14:43.539Z] TOOL RESULT

```
13092-Meyer-Liibke, Arch. sl. Ph. 36.591, after Weigand). In It. dial. colwmbine, used of the white popping corn, the associa- tion with doves is more obvious.
13093-5. SCr. kukuruz, etc., general Slavic, whence also the Lith. and Lett. terms, prob. not loanword fr. Turkish (as in Miklosich, Tiirk. Elem. 1.334, Lokotsch 1230), perh. related to certain Slavic plant names, but uncertain. Berneker 640. Briickner 280.
13094-RICE Lith. rysat Lett. risz ChSl. aes SCr. __riza, oriz Boh. ryze Pol. ryz Russ. ris Skt. vriht- Av.
13095:of the word seen in Skt. vrihi- (AV-+), Afghan vrizé, etc. Boisacq 712. Schra- der, Reallex. 2.230.
7604:REW 8543 Puscariu 1713. ;
12925:Of ¢ which a several grains the names of Scussed in 8.43-8.48 wheat
12959:8. ChS]. Zito (in Gospels once = ye- vnpara ‘fruits of the field’; as ‘grain’ in derivs. Zitinica ‘granary, barn’, etc.; reg. pisenica for otros, but here prob. under- stood as ‘wheat’, cf. 8.43
13077:rell, old. ed.) gwenith India (gwenith ‘wheat’, 8.43) or now (Spurrell-Anwy!) indrawn (abbr. ind- + grawn ‘grain’); later in U.S. simply corn at the expense of its old generic use.
13094:RICE Lith. rysat Lett. risz ChSl. aes SCr. __riza, oriz Boh. ryze Pol. ryz Russ. ris Skt. vriht- Av.
21043:the th nch along 11.87 PRICE oth. wairp, andawairpt Lith. kaina
31430:18.41 Cau (vb. = Summon) 18.42 Catt (vb. = Name) 18.43 ANNOUNCE
32271:Lat. vovére ‘vow’, Skt. vdghat- ‘sacrificer’, Av. aoj- ‘say solemnly’ (18.43). Walde- P, 1.110. Boisacq 300. Ernout-M. 1135.
```


## [2026-10-16T05:14:48.555Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; echo HRN; grep -n -i 'abar\\b\\|upairi\\|birinj\\|birin\\b\\|brinj' $R/HRN.txt | head -15; echo HUB; grep -n -i 'abar\\b\\|upairi\\|birinj\\|brinj\\|\\bbar\\b' $R/HUB.txt | head -15"
}
```


### [2026-10-16T05:14:49.156Z] TOOL RESULT

```
HRN
2081:ap. upariy 'über; aw. upairi; phlv. apar, päz. awar,
2122:kurd. birin ^tragen, bringen', Praes. berum; af/. wral;
2209:Wort; vergl. arm. brinj; kurd. birinj; oss. brinj
2210:(Hübschmann, S. 121); bei. brinj (35); wa/.
2214:208^»« {2)birin) 'Kupfer .
2218:birinj, bei. LW. brinj (34) ^).
2225:aw. *upairivara- oder wohl besser ^upairivärana- ;
2243:kurd. birin 'schneiden; bei. buray , n. buray (43);
3534:374. teber, tewer 'Beil', arab. LW. tabar,
3710:*Krone* elamitischen Ursprungs wäre, ebenso wie taka- in takabarä, so
14515:upairi 191.
22792:, ahd. zabar 69.
23168:tabar 374-
HUB
115:lautete, wie mir No Id eke aus Reimen (mit bar-e, mar-e
204:auch * dvar dan *nehmen zu skr. apa-bhar, zd. apa-bar^)
205:wegnehmen' zu ziehen, aber kann ap. *apa'bar- ^^ phi.
216:*auferre* = pSz. apurdan = phi. apavurtan = ap. apa-bar^ zu dem
335:Noldeke belegt mir np. araS im Reim mit bar-aS.
338:envy' etc.) wie abar zu bar auf etc. und geht laut-
860:'rosten, backen', np. phi. bar^jan 'Backofen, 61. and
884:208. Die meisten iran. Formen fiir birinj = gurinj 'Reis*
891:ihr stimmt kurd. pirinjok = birinj *bronze' (Justi-
893:') Vullers giebt biranj neben birinj an, aber auoh die Lehn-
894:worter zeugen fiir birinj.— 28 —
900:210. Np. harvdr =^ zd. *upairivara' (nicht *upairivarana-,
922:*) Arm. plinj : np. birinj — arm. hrinj 'Reis' : np. birinjf.
1515:bar, vgl. zd. paiti-dl 'hinsehen*, paitidaya- *Aufseher,
1878:477. Dazu kurd. vird, Mrs, hire 'Bar ZDMG. 38, 93.
```


## [2026-10-16T05:14:51.542Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; sed -n 2076,2086p $R/HRN.txt; echo ...; sed -n 2200,2220p $R/HRN.txt; echo HUB; sed -n 330,340p $R/HUB.txt; sed -n 880,895p $R/HUB.txt; sed -n 918,924p $R/HUB.txt"
}
```


### [2026-10-16T05:14:52.009Z] TOOL RESULT

```
kurd. LW.(?) ier; bei. gvar (135).
191. {2)ber, eber, auf, über, nahe bei' etc.; "ibN Is. 1, 1;
vergl. berm 'höchster 2).
*) Mohl übersetzt falsch durcli *mieux*.
2) Phlv. barin 'höchster*.— 45 —
ap. upariy 'über; aw. upairi; phlv. apar, päz. awar,
apartar, apartum; ai. upäri.
kurd. her; af/. pre- (LW. bar); oss. d. uol, t. 0/ *das
Obere*, välä Postpos. auf, über* (253) ; bei. par n. par
(283), resp. gvar (136); wa/. sar. war,
Geiger, Etymol. des Balü^i s. v. gvar (136), macht
...
vergl. arab. LW. burnäj, barnaj, eine Dattelart (de
Goeje, Bibl. geogr. arab. IV, 189).
aw. aperenäyuka^ * Knabe*; phlv. apurnäyak.
afy. wör 'klein , wörkai, wörukai 'Kind*; bei. LW.
Warna jung, Jüngling (285).
208. (i)&fr«tijf, gurinj (AM.) 'Reis'.
Semn. varinj; (Käs. nur berSnj).
aw. ^verenja-; skr. vergl. vrthi- *ßeis'.
Vielfach entlehntes , gewiss ursprünglich arisches
Wort; vergl. arm. brinj; kurd. birinj; oss. brinj
(Hübschmann, S. 121); bei. brinj (35); wa/.
gurunj etc.
af/. vrize geht auf die Form ohne Nasal zurück,
wie gr. o()v£a, /J^(>«fa, ostt. uruz, urz, AM. eruz),
208^»« {2)birin) 'Kupfer .
Zusammenhang mit aw. berejya^ (in parö.berejya-)
ist durchaus unsicher; vergl. Schrader, Sprach-
vergleichung und Urgeschichte \ 273, 274, kurd. LW.
birinj, bei. LW. brinj (34) ^).
209. bemT 'Gefäss* (unbelegt).
aw. vergl. urunya- 'Schüssel* (vd. 14, 8); de Lagarde,
HUB
Vgl. F r e i t a g , arab. Wb. a. v. rasas.
^) Die Var. dristya- hat G e 1 d n e r nicht in den Text auf-
genommen. Ihr wiirde np. *drist entsprechen.— 13 —
steht nicht fest. Im Balu^i wird altes rs zu s, vgl. kasag^),
kisag^ musag, also bal. hars aus haris =^ *haras?
Noldeke belegt mir np. araS im Reim mit bar-aS.
71. Np. arask 'Neid* {baraSk Fird. 1, 15, 23 mit Praef, ba-)
ist die altere Form zu raSk (afgh. LW. rask malice,
envy' etc.) wie abar zu bar auf etc. und geht laut-
gesetzlich durch paz. arask (Min. 61. p. 16 als Var.),
phi. arask (Gl. and Ind. p. 20: arashih) auf ap. ^araska"
Etymologie rich tig, falls gustuvan aus kuStuvan *Wei-
chen-schiitzer' entstanden ware. Arm. kstapanak stimmt
lautlich gut dazu, aber nicht in der Bedeutung, da es
das ntpids^iav der Septuag. wiedergiebt.
208. Die meisten iran. Formen fiir birinj = gurinj 'Reis*
haben i-Vokal,*) daher ap. *vrinji-^ iranisch *vrinji',
^vriSi-? (afgh. mi^ pi. fem., vri^a 'Keiskorn, vgl.
auch skr. vrthi-) anzusetzen.
2ogbi8. jfp lyipifij *Kupfer fMessing' nach Rosen, Neup.
Sprachfiihrer p. 35) ist nach Vullers die (jungere)
Nebenform zu piring, die Horn nicht erwahnt. Zu
ihr stimmt kurd. pirinjok = birinj *bronze' (Justi-
^) Dazu phi. kuataktar 'ftussere* ZDMG. 43, 37.
') Vullers giebt biranj neben birinj an, aber auoh die Lehn-
worter zeugen fiir birinj.— 28 —
Jaba Wb.) und arm. plinj^) *Kiipfer, Kiipfergeld, Munze,
(-= skr. chinna) Min. cap. 27, 10, Shk. 237. Vgl.
Bartholomae, Studien zur idg. Sprachgeschichte,
II, 107, Anm. 4, und 180—181 ; Joh. Schmidt im Fest-
gruss an R. von Roth p. 186.
*) Arm. plinj : np. birinj — arm. hrinj 'Reis' : np. birinjf.
*J Aber gesiohert durch arab. hamiyya (No Id eke).
3) Dazu das Abstractum hurts *sectio' (Tom Praesensstamm ge-
```


## [2026-10-16T05:14:58.326Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; echo PHD; grep -n -i '^abar\\b\\|^abar \\|brinj\\|^apar' $R/PHD_mackenzie.txt | head; grep -n -i 'brinj\\|^abar' $R/PHD.txt | head -5; echo NYB; grep -n -i '^abar\\|^apar\\|brinj\\|\\bapar\\b' $R/NYB_vol2_glossary.txt | head -10; echo BRT; grep -n 'upairi' $R/BRT.txt | head -5; echo KNT; grep -n -i 'upariy' $R/KNT_full.txt | head -8"
}
```


### [2026-10-16T05:14:58.767Z] TOOL RESULT

```
PHD
257:abar; otherwise it is replaced by K), E, and O. E stands for the
693:abar~ar [)plgi] god, divinity.
702:abar-meniin ['Plmjmfn ] proud, haughty.
706:abar-oz ['pl'wc] stronger.
708:abar-tan ['Pltn l ] arrogant.
1582:bob                             19                           brinj
1633:brinj                             20                              buz
1634:2brinj [blnc I (M bryng), N birinJ] bronze, brass.
6112:brass brinj, roy-.                     burn (vi.) waxsidan.
6118:brazen brinJen, royen.                   tabisn.
163:abarmün i 2 abd sahistan
164:abarmān [5/mn'] in charge. abarmānd ['pín?nd] inheritance, privilege. abarmānīģ [%n?nyk!] noble. abar-menišn Pf/myn$n'!] proud, haughty. abarón Pf*/xwn! | N wárün] contrary, wrong, sinful. ~ih: sin. abar-6z PóPeoc] stronger. ~ih: mastery. abar-tan [Pltn'] arrogant. ~th: arrogance. abarwēz Pfltvyc | (M *bruyj, N parwéz)] triumphant, victorious. ~ih: triumph, victory. abarzén, v. zmašk, abaxs [hš] repentant; regret. ~ЛЬ : repentance. abaxšāwand [5hP^wnd] regretful. abaxšāyīdan, abaxšāy- [5APd-ytn! | М ?bxPy-, N baxšūdan, baxšāy-) forgive, have mercy on. ~išn: mercy, forgiveness. ~i&nig : forgiving, merciful. labāxtar [*5?*4tl | M 7b’xtr] planet. žabāxtar [PP’htl | (N bāxtar ‘west’)] north. abaydag Pyrťk', v. paydag | M ?byd?g] invisible. ~th: invisibility. abày- : abayéd ['yt' | M Maud, N bāyad] it is necessary, fitting; must (+ infinitive). ~ist Pf?dst' | N bāyist] it was necessary. ~istan [?P?dstn!] be necessary, fitting; desire, want. ~išn: necessity. ~išnīg : necessary, fitting, seemly. abāz [L AWHL < A lI2(w)hr;?Pc | М Рс, N baz, wa] back, again, re-. ~ айдап б: attribute, ascribe to. 7 appoint t= ~ dāštan: withhold, restrain, prevent. ~ ēstādan az: abandon, desist from. — kardan: open. — kardan az: disengage from, wean. ~ mándan: remain behind. ~ pádan: remain, stay. — raftan : issue, go forth. ~ waštan O: turn into, become. ~ wirāstan: rearrange. abāzsār [LAWHLs'I] rebellious. ~ih: rebellion. āb-čihrag [$ cyhlk'] holding the seed, essence of water. abd [>24 | М "Gd J ?bd-] wonderful. ~ sahistan: seem wonderful (to) > marvel.
257:bób 19 brinj
290:lbrinj [binc | N birinj] rice.
291:brinj 20 buz
NYB
314:ahräm- [’hl’m-] pres., to raise, to lift up, to lead upwards; pres. pass. dd p. sg. ahrāmiyēt ['hPmydyt']: fratom gam pat humat ... apar ~ at the first step he is lead up to (the stage called) Good Thought 7326-27, but Paz. ārāmed, Skr. v. nivesayati (West: ‘he rests the first footstep on Humat’). — Ps. pret. ’hl’pty, pres. ’hl’m-, pt. 'hlwpty ‘elevated’; MPrs hr'ptn, ’hr’m-; MPrth pt. ’hr’m’d; Paz. aharām- išni, Skr. v. ākarsgana, aharämihed, Skr. v. krsyate SGV XVI, 22. 26, treat- ing of Manichean theology. Etymological attempts HP II, 5; Verbum 190; Ghilain 73; Ps. Gloss. As to -m-: -ft- cf ayinaftan, hanžaftan. Cf also Gxrdm-.
394:of; o pattākēh ~ to appear 513, 1081; 6 patirak ~ to meet 8%. 731.20-21, ete.; 6 en kustak rón towards this district 715; — with hac: from 184 ete. [hac ... be 6 ... ~ to be converted from... to... PR 945]; hac ... ywvatük away from 747-8, 7667; — with pat: on (a path) ibd. ; — with prev.: andar — to come forth, to appear 87?5; to be handed down 10818-19; — apāc ~ to become again 104?*; apdc 6 to return to 5) (v. bälist). 818-19, 914, 12]9-10; hac ... apāc ~ to return from 991; — apar ~ to shoot up 9573-4; to be allotted to 98*; apértar apar āyēt ku surpas- ses 641%; — hac varten beron be ämat got off the chariot 20?3; (coursers) ke pat róc-6 70  frasang bē āyēnd- (h)b who are always riding a dis- tance of 70 parasangs in one day 6! (v.s.v. h-); hān<i>druž (be) āyēt the space which the Drug will cover 96?3, 9818; bé + the pres. of ~ regularly denotes the fut.: 24"; if the vb. takes the prep. 6 the order is always be 6: 9725, 985-6, 9912-13, 1046-7; — fröt ~ to come down, to descend (hac...6...) 104°; — ul ~ to rise 86°; šuhr pat post ul āmat the sperm rose to the skin 547°. — āmatan < *ā-gmatanai from à + Av. (493 sqq.) OP gam-, cf OP (par)ägmata- ‘gone forth’; äy- < à + Av. (147 sqq.) OP ay-; MPrs ’mdn ”y-; Paz. NP dmadan dy-. This vb. is characteristic of the SW dialects, as against NW āgatan,
441:andar [BYN] in: 1. adv. a) referring to a preceding encl. pron. (ef apäk, apar, avis, haciš, patiš): zäyak-e ke-š murvēcak ~ an egg in which there is a chicken 92%; api-§ ... must" (g. v.) u drog ~ nest F:7; without a preceding encl. pron.: Sugud i haft janakan ~ in which there are seven j. (q.v.) 11318-14; haft x"ataidan ~ būt 11314-95; — b) prev., esp. with vbs. of
445:motion: šutan, dväristan, opastan, ete., and with ēstātan and nisastan (also ~ 6). — 2. prep. in, local, temporal and figura- tive: ~ Pārs; ~ im xünak P1:6; ~ miyàn i in the middle of 865; ~ han hangam at the time 613; ~ ham zamān at the same time 127°; ~ zamān in due time 221, etc.; ~ sap in the night 529, 614; ~ hàsr for a single moment 663; ~ hàn in the meantime 5615-17; — xtatäyeh + Xösrör 1184; ~ Vistasp šāh kisvarikan when V. was the emperor of the world 365; — freftür ~ : concerning 3419-20, 10923; spasdārēh ~ , an-ispās ~ : to, against; with other substantives, v. these separately ; — together with another prep.: ~ 6 into, on to, up to: ~ 6 nun 404; with apakandan, burtan, guméxtan (also without 6), hištan, kartan (v.s.v. kar); apar ~ 402, — Av. (131 sq.) antara, antarš, OP antar (better read antara^); MPrthPrs ’ndr; Paz. NP andar; v. also niyandar.
491:?apak [LWTH] 1. a) adv. together: (ka- nicak virtual dat.) andar ham Sap ~ bit in that same night he was together with the girl 16!-?; referring back to an encl. pron.: sih (restore the reading “30”, v. 28th) 4-$ ~ pat asp which was with him on the horse 8? (v.s.v. i and ef andar); Sih-& ... —-aš pat asp nišast estat 89: as prepositions do not govern an encl. pron. ~ must be the adv., and -aš refer to the following pat asp or to the whole sentence. — b) prep. together with, with, in all its senses, passim; in spite of 118; ~ man 5?*; ~ amäh 19, ~ smäh 1918, ~ disin 82; ēvak ~ dit with each other 7818. 799. 1071, — 2. adj. prostrate, knocked down, lying on one’s back: čvak apar, ~ dit, apar ēstūt hend o en kar they set about this act (making coition), the one above, the other lying on her back 4314-4; ka Ahriman ~ A. being knocked down (lying senseless) 914 (the enel. -4 after ~ belongs to the following, taking up the preceding subj. Ohurmazd which begins the period), a wordplay — not understood by the Pazandist — with — hämöden yazdan u amahraspandän |. 5—6, the first
497:apākēh [’p’kyh] 1. company; pat ~ together 5712, — 2. backward movement: pat ~ back 418; v. pat-apākēnītan. — 3. help, assistance 5919-20, 729-26 (opp. ha- mēstārēh). — V. lapāk and ?apäk. Paz. āvāgī. V. also apar-apākēh.
505:lapar [’pl; MDM, v. 2apar] adj. situated above, lying above: évak ~, apäk dit, v.s.v. žapāk (2); — heavenly, often in compounds: apar-apükeh etc., v. below; comp. ~-tar [’pltl] higher 5426, 581°, highest 1097; sup. ~-tom highest 415. 102°; v. also apartaréh; — adv. empha- sizing an adj.: highly, extremely: apar- aržānīk, v. aržānīk. — Av. (393) upara-, adv. upara (instr.), uparam; MPrth ’br adj. and adv. (MHC), comp. ’brdr, sup. ’brdwm; Ps. ?pldl; Paz. awartar, awardar (SGV); NP bar ‘height, top, summit’, bartar ‘higher’. ?apar [MDM, erroneous reading of OAram QDM] 1. adv. above: (3 päs) i-m guft ~ of which I spoke above 65°; či nümak" cé hac ~ nipišt" éstat the inscription that had been written here above P2:3, cf hacapar; — prev. over, on, upon, up, or simply expressing the initiation of the action, with varying vbs., cf esp. (@)ma- tan, burtan, grätan, raftan, rasitan ; follow- ed by enclitics: apar-p-im ravišn I must needs ascend 4076, v.s.v. -p(i); — refer- ring back to an encl. pron.: api-š Vidrafš . ~ mšast and V. got on it (the horse) 25W5; cē-t avdom margéh ~ raset for at the end Death will come upon thee 726-7; (martömän) tāi-šān āmēcišn ~ nē barend as long as one does not impart instruction to them 801. — 2. prep. a) local: over, on, on to, down on: Krisäsp ~ én damik raset K. is roaming all over this earth 3318; ~ giyāk on the spot 3", 102; ~ ki Zartuxst bé dahém where we shall deposit Z. 3957; ~ pad ēstāt rose to his feet 1821; asp ... — rahy vartét harness the horse! 5418-14; srišk ~ srišk drop after drop 214
506:apar-gar
507:(cf 41?" and 89%); ~ fravartak in the letter 1822; — combined with another prep.: ~ 6 pad estat 28%. 1189. 11917 (cf above 1871); ~ 6 ax“ i astomand 401; m andar äyiyänak 409; ~ tdi sdxdn 401; ~ pat óstak 48% (ete.). — b) temporal: ~ sal 2 mazdesn bag’ Šāhpuhr” in the year 2 of the Mazdayasnian Divine Sh. Pl:l; ~ sal "68 in the year 68 P2:1; ~ pat han jamān ka at the time when 41%, adak ~ pat jamän at that time 619; 4214; 3 sap td three nights ago 512-3, — c) figurative: on, about (esp. in headings and book titles), concerning; (reigning) over, (merciful) to, (hostile) to- wards; (means) for; ete.; — with an inf. or a v.n.: in order to 3714-15, 4515; 1185 (continued by inf. + rād, l. 6). - ~ does not govern encl. pronouns; single excep- tion apar-aš 54° (late passage). — Av. (394 sq.) upati, OP upariy; MPrthPrs br; Paz. awar; NP bar. Cf aper. — On MDM 43" v. hàreftan.
508:apar-apakčh [MDM ’p’kyh] heavenly, di- vine help 591°.
BRT
2533:*'te  *yffi'^  fracarinti  , .  aiialiqm  .  .  N.  ,paiqn  ,  ,  'na  ,  ,  triltm  k>hrp}m  hvan.- ^.  III)  In  folgenden  Fallen  brauchen  i  t/arwr« -f?rv«aii/V.  5. 13,  3)  'dann'  im wir  den  Sing,  mit  'ein'  (unbestimmter  Ar- !  Sinn  von  'in  der  Folge'  und  'in  Folge tikel),  den  Plur.  artikellos  (vgl.  ^aisa- 111}  j  dessen',  einen  Zwischensatz  hinter  einem yesica  .  .  upairi  'l^m  iristim  .  .  Ajr^zy^lf '  SaU  mit  yai  einleitend:  y^i  ndii  nidan- yaia  .  ,  "und  wenn  (man)  .  .  auf  einem  sayilnte  —  ''ja  kl  alte  sünö  vä  .  .  fraja- Toten  ..  liegen  lässt  .  ."  V.5.61;  — yö\s,yi>  —  kä  Af  asU  äiaX.ö.^T,  —  yaii'a vastnm  upaiiharizatti  upatri  °t»m  tristem  |  vaoeäp  aiSö  m7  Aanqm  .  .  p3r>saKuAa  — "wenn  einer  ein  Gewandstück  auf  einem '  "'la  ae^a  y<J  kaine  hanqm  . .  p?nsaili  , .  — Toten  liegen  lässt"  V.Äaj;  —  bei  rela- 1 'ort  assa  yS  kaine  altahmat  puir.lt  *mi- tivisch  angeschlossenem  Nomen:  yat  "te^  manxlstti  —  '^Aapanta  .  .  vfri^qn  .  . yöi  tnazdayasna  . ,  taci.apaya  nasSum  fra-  [  V.  /J.  1 3  f. ;  —  yeii  mit  Aari^nm  baraili jasqn  "wenn  Mazday.  auf  einen  Leich-  -  "da  aisa  yö  afirinüyakö  adJityö.an- nam  in  fliessendem  Wasser  stossen"  V.  6.  Aarj^nin  (sd.)  iri^ät  —  ^'>para  A!  iri- 26;  <y.73,  7-36.  \sittt5  rais?m  cikayat  .,  V.7j.i6.
2550:äJffj  ti  'take  paiti  ..  V.22.2f.;  —  Da.'  aoAvo  (Stvetx.)  yal  as/tainti  Y.i^.6  \isw.; in  Verbindung  mit  anya-  Du.  (s.  i  b):  —  'tagsam  sünam  ..yimpasuiJiaurvamca.. asUm^mastrrfttqm  vispacayö*>nastr?inqm  i  V./^J.S;  —  'farahqm  urvaranqm  yat  ätri.- amqsta  fsd.)  ''i^arö.cikaya  *°le  anye  cika- ■  ciirranqm  V,4',75;  —  'ttm  ratümca  .. yatö  "wenn  einer  ,  .  und  wenn  einer  ,  .  \yim  maiaydhanmaim  A.j.3(?).  b)  sub- vcrletzt,  so  sollen  sie  dies  und  jenes  . ."  stasA\v\&c\\- 'ta(^T>.)äb3r3ta*sraosiivariza F,_jc  b)  adjektivisch:  j'iT/fl/ire'a/ara.-  vicarayaDm  "die  beiden,  der  .^.  und  der iri^yeiti  kva  "tarn  xsapan»m  . .  *vanAaiti  Sr.  .  ."  N.  jcf ;  —  cval  'te  (ADn.)  stai- "wenn  ein  Gläubiger  stirbt,  wo  weilt  asi\tiüa  bar>iis^a  ..  nasus  .,  fräsnaoiti dem  Tä^  (des  Todes)  . ."  H.  2.  i;  — yö  "..  die  beiden,  das  Bett  und  das  Polster .." . .  upairi  kunanm  (sdL)  manö  baräi  i-up^m  V.  7.9;  — ■  azim  °ta  (APn.)  zaota  zlsJi  (sd.) 'tfm  paiti  zmämm  aUariin  uri'a  kllayäi  ..  /rasrao^r?mca  /ragl>r>mca  . .  Vr._j.7; (sd.)  "wenn  einer  . .,  so  . .  während  der  —  't^m  nitamim  As'>rjm  '^rivacahim  (sd.) ganzen  Zelt  (seiner  Cberhebung)  .  ."P.  "id  minimum  Aj^/um:  triverbe"  F.  27b; J7.  a)  wo    wir   'solch'   brauchen:  yö  —  haomü  kutö  .  .  ava    'te  ahuta  .  .  "ge-
2561:'''tt  *yöP^  fracarmii  . .  aitaSsqm  .  .  N.  patan  .  .  'oa  .  .  agtJm  k>hrp>m  hvar».- ij.  III)  In  folgenden  Fällen  brauchen  j  i/awjrjw  fo/vwuc/ V.  5. 1 3.  3)  'dann'  im mir  den  Sing,  mit  'ein'  (unbestimmter  Ar- 1  Sinn  von  'in  der  Folge'  und  'in  Folge tikel),  den  Flur,  artikellos  {vgl,  ^aila-  III) '  dessen',  einen  Zwischensatz  hinter  einem jcsVJ  .  .  upairi  'tim  iristim  .  .  k>r>zyllt.  Satz  mit  ytzi  einleitend:  ye:i  mit  mdart- ya>a  .  .  "und  wenn  (man)  .  .  auf  einem  l  sayanfe  —  'ca  he  alte  sünS  vä  .  .  fraja- Toten  . .  liegen  lässt  .  ."  V.  5. 6 1 ;  —  /^ ,  JiW^  —  kä  hl  asti  Wia  V.  6".  47 ;  —  yesila vastnm  upaifharizaiti  upairi  ^tfm  iristtm  ^  vaocät  aSsö  nä  hanqm  .  .  p>r?sat3uha  — "wenn  einer  ein  Gewandstiick  auf  einem  .  '<,a  aSsa  y.J  kaine  hanqm  ..p^nsititi  . .  — Toten  liegen  lässt"  V.  ^'.23;  —  bei  rela-,°ö(J  a^ia  yä  kaine  aetakmut  puir-at  *mi- tivisch  angeschlossenem  Nomen:  yat  °te\mar?x^iliti  —  '^hat<anta  .  .  7>)r?zyqn  .  . yei  mazdayasna  . .  taH.apaya  nasHum  fra- '  V.  /5. 1 3  f ;  —  yai  nöii  har^'^nm  baraiti jasqn  "wenn  Mazday.  auf  einen  Leich-  —  °ofl  aila  yS  ap^rinlyükö  adaityo.at3- nam  in  fliessendem  Wasser  stossen"  V.  6. '  harsirim  (sd.)  iriiyäi  —  ^para  he  iri- 26;  ^.73,  7-36-  \Hntö  raSsim  cikayat  ..  V./j.iö.
3000:jf. ;  —  hyal  ds  fyao^anl  mTsdavan  (sd.) '  ivam:a  (sd.)  simqmia  simötirqm^a  dprtta . .  'iim  (ASf.)  .  .  °^,Ji  vanuAim  aslm  '  huk>r3ta  upairispatä  °ka  (IS.)  bastqm  Yt vaKAatrvi  \.43.^;    —    aübyö  masdä  'kä   ;o.i25.
3260:•  j.  aSairi.dahyav-  Adj.  (auch  mask.)  'der unter  dem  Land  ist* :  mi'kr?m  upairi^ahyOm ..  'yam  (ASm.)  Yt. /O.144.
KNT
6736:(from *wpa-dyam) ‘I arrived’, upariy-dyam ‘I 
11237:kanam, nij-dyam (ulpayam upariy-dlyalm, aor. niy- 
12708:upariy mam niyasaya ulá-di$ alávayam bartanaty 
12745:upariy, prep. W, асс.; pref. w. verbs. 
12806:upariy ‘over’, with slight idea of motion, shading 
14176:IV. The postpositions are upariy ($269; only 
14498:upariy nipistà ayauda ‘there is (= ‘was’, $285) 
18139:04 iy : zürakara : &ham : поту : adam : поталу : tauma : upariy pev omis ~
```


## [2026-10-16T05:15:02.451Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; grep -n -o '.\\{0,60\\}upairi  *Adv[^.]*.\\{0,200\\}' $R/BRT.txt | head -3; grep -n -o '.\\{0,40\\}upari.  *Präp.\\{0,200\\}' $R/BRT.txt | head -3; sed -n 12745,12750p $R/KNT_full.txt; grep -n -o '.\\{0,100\\}upairi.\\{0,100\\}' $R/incoming/WLD/WLD_Bd1_pages.txt | head -5"
}
```


### [2026-10-16T05:15:11.671Z] TOOL RESULT

```
ugrep: error: error at position 391
][\x80-\xbf])*(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
                      exceeds complexity limits___/


ugrep: error: error at position 120
[\x80-\xbf]*){0,200}
                    \___exceeds complexity limits


upariy, prep. W, асс.; pref. w. verbs. 
lara, prep. w. acc. 
ni-, prep. W. loc. in phrasal adv.; pref. w. verbs, 
nij-, pref. w. verbs. 
nipadày, prep. W. ace. T 
patiy, prep. ж. асе.; postp. у. acc, inst, loe; .^ 
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,100}
                        \___exceeds complexity limits
```


## [2026-10-16T05:15:16.076Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; python3 - <<'EOF'\nimport re\nR='data/verification/sources/refs/'\nt=open(R+'BRT.txt',errors='ignore').read()\nfor m in re.finditer(r'upairi  ?(Adv|Präp|Praev)',t):\n    print('BRT',m.start(), t[m.start()-80:m.start()+300].replace('\\n',' ')); break\nfor f in ['incoming/WLD/WLD_Bd1_pages.txt','incoming/WLD/WLD_Bd2_pages.txt']:\n    t=open(R+f,errors='ignore').read()\n    for m in re.finditer(r'upairi|uperi',t):\n        s=t.rfind('[pdf page',0,m.start()); print(f, t[s:s+16], t[m.start()-200:m.start()+200].replace('\\n',' ')); print('==')\nt=open(R+'KNT_full.txt',errors='ignore').read()\ni=t.find(\"upariy ‘over’\"); print(t[i-200:i+400])\nEOF"
}
```


### [2026-10-16T05:15:16.616Z] TOOL RESULT

```
incoming/WLD/WLD_Bd1_pages.txt   lo-, brit. gwo-, aber                                     kaum            lautlicli;        s.   Brugmann aaO. und Pedersen KG. I 35);    got. ufar, ahd. nbir, aisl. yfir (letztere beide sicher aus *uperi                                                         mit im                                                                                                                                :   
==
incoming/WLD/WLD_Bd1_pages.txt                                               am ebesten von einem nach avco gebildeten  vne oo>)      ;    lat.     super,   superus „der obere". osk                                         supruis „superis“           (davon lat.supra „oberhalb, fiber*', superior. supr?mus umbr. sobra „supra“, suprii                      ,    Adv. .,supra“; lat. supernits „der obere**, umbr. supn ne m. Acc. .,9upe
==
incoming/WLD/WLD_Bd1_pages.txt  von einem nach avco gebildeten  vne oo>)      ;    lat.     super,   superus „der obere". osk                                         supruis „superis“           (davon lat.supra „oberhalb, fiber*', superior. supr?mus umbr. sobra „supra“, suprii                      ,    Adv. .,supra“; lat. supernits „der obere**, umbr. supn ne m. Acc. .,9uper“j got. ufaio Adv.    fiber, darfiher*'. ahd. obaro Adj
==
d ‘under’, always of a person, in figurative 
uses: ‘was under me, under my command, with 
me’ (DB 2.18, 3.30); ‘under Artaxerxes, in the 
time of A.’ (Аа 4); ‘made under me, in my 
time (А?Ра 23). 

upariy ‘over’, with slight idea of motion, shading 
down to ‘according to’ (DB 4.64); once placed 
as second word after its object (DNb 49, vari- 
ant of 46). 

fara ‘through’, with motion. 

nipadiy ‘close after’, see §270.1V. 

patiš ‘against’, governing a person as goal. 

para ‘beyond’, of place where. 

para ‘along’, of motion; enclitic postposition. 

pariy ‘about = concerning = against’, of
```


## [2026-10-16T05:15:20.843Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 - <<'EOF'\nimport re\nR='data/verification/sources/refs/'\nt=open(R+'incoming/WLD/WLD_Bd1_pages.txt',errors='ignore').read()\ni=t.find('superus „der obere'); \nprint(re.findall(r'\\[pdf page \\d+\\]',t[:i])[-1:], t.count('\\f',0,i))\ni2=t.find('ufar, ahd'); print(t[i2-600:i2+100])\nt=open(R+'BRT.txt',errors='ignore').read()\nfor m in re.finditer(r'upairi',t):\n    seg=t[m.start():m.start()+120]\n    if 'über' in seg or 'Adv' in seg: print(m.start(), t[m.start()-50:m.start()+250].replace('\\n',' ')); print('--')\nEOF"
}
```


### [2026-10-16T05:15:21.463Z] TOOL RESULT

```
[] 200
                                                  —
hin, fiber          —
                hinaus (Acc.); fiber („Abl.“ = Loc.): air. for-, for Praeverb
..fiber, auf“ und Praep. „fiber, fiber    — hin, fiber — hinaus (Acc.) fiber auf                                           ;



(,,Dat.“       = Instr. oder Loe.)“, cymr. yor-, givar-, corn. gor-. bret. gour-.
gall, uer-tragus „eine ArtsehnellffiSiger Hunde“ Ver-cingeto-rij- (das inselkelt.
-o- nach ir. lo-, brit. gwo-, aber                                     kaum            lautlicli;        s.   Brugmann aaO. und
Pedersen KG. I 35);
   got. ufar, ahd. nbir, aisl. yfir (letztere beide sicher aus *uperi                                       
1055400  mayä  pärmdti  'zff  (VS.) dby  Google 393 upara upairi  2 394 •  j.  upara  Adv, :  s.  upara-. •  j.  upara-  Adj.  i)  'der  obere,  höhere; oben  befindlich;  überlegen':  "^^F.jg;  — fratanmat  . .  'r^mcil  U  Aavatipm  (sd.)  Y. 10. 3 ;  — yö  daii^kaom  . .  'rät  amai  dahaid "der  dem  La
--
1058825 iniän  hend  u anSnri  vimSn  ape  kunend, •  j.  upairi,  p,  upariy  i)  Adv,  'supetne'; a)  'oben':  °ri  pusqm  (sd,)  bandayata  Yt. 5.128.  b)  'von  oben  her':  fravasayS .. ya  'ri  ^hamarmat  (sd.)  .  .  bazül  slanda- yeiti  Yt.  13. 31.  2)  ftaen.  mit  Akk.  und Instr.;  a)  'oben  ü
--
1061737 rs  Gdn.  KZ. 2S.  188,  DsT.  ZA.  /.  9. •  j.  upairi.dahyav-  Adj.  (auch  mask.) 'der  über  dem  Land  ist':  mür^m  °yüm  .. aoairij/a/iyBm  (ASm.)  YLjo.  144. Npü,:  iti  bälä  i  sahr  Ott. •  j.  upairi.5pita-  Adj-,  PPfP.:  s.  'spä-. •  j.  upairi.z^ma-  Adj.  'oberhalb,  oben auf  der
--
4035969 matsi^  (Sp.  337  o.) t>mff  Hca  V.J.  35. mit  upairi  'oben  drauf  legen,  darüber- slecken':  Jo/  tl  (nämL  aurvantg)  . .  frä.- yxixta  *hqm.h>qmi^A.)ia , .  d^nta  hukarita *upairi.s'paia-l  aka  YLro.us. wxpara  'fortschleudern' :/ara  kamfr^aa spayäti  .  .  para  kam^r^ha  voiaite  mi^
--
```


## [2026-10-16T05:15:26.284Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['BQT','MON','ARY']: print(k, d[k].get('page_offset'), d[k].get('lookup_hint')[:600]); print()\n\"; head -c 600 $R/BQT_v1_pages.txt; grep -n 'pdf page' $R/BQT_v1_pages.txt | head -3"
}
```


### [2026-10-16T05:15:26.892Z] TOOL RESULT

```
BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=deh

MON None Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded a

ARY printed page = pdf page + 1 Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image

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
```


## [2026-10-16T05:15:29.422Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py BQT:79 2>&1 | head -80"
}
```


### [2026-10-16T05:15:30.050Z] TOOL RESULT

```
no scan of BQT covers printed page 79 (see 'scans' in refs_online.json)
```


## [2026-10-16T05:15:33.016Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 - <<'EOF'\nt=open('data/verification/sources/refs/BQT_v1_pages.txt',errors='ignore').read().split('\\f')\nimport re\nfor n in range(285,294):\n    p=t[n]\n    if 'upairi' in p or 'apar' in p or 'ابر' in p[:3000]:\n        hits=[m.start() for m in re.finditer('upairi|apar|abar',p)]\n        print('leaf',n,len(p),hits[:5])\nEOF"
}
```


### [2026-10-16T05:15:33.392Z] TOOL RESULT

```
leaf 286 1536 []
leaf 287 2406 []
leaf 289 2495 []
leaf 290 2199 []
leaf 291 2402 []
leaf 292 2267 []
```


## [2026-10-16T05:15:36.890Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 - <<'EOF'\nimport re\nfor f in ['BQT_v1_pages.txt','BQT_v1.txt','BQT_alt_v1.txt']:\n    t=open('data/verification/sources/refs/'+f,errors='ignore').read().split('\\f')\n    for n,p in enumerate(t):\n        for m in re.finditer(r'upairi|upari|brinj|vrīhi|vrihi|oryza|aruzz|uruz',p,re.I):\n            print(f,'leaf',n, p[max(0,m.start()-150):m.start()+150].replace('\\n',' ')); print('--')\nEOF"
}
```


### [2026-10-16T05:15:38.055Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:15:40.951Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 - <<'EOF'\nt=open('data/verification/sources/refs/BQT_v1_pages.txt',errors='ignore').read().split('\\f')\nfor n in [288,289,290]:\n    print('=====',n); print(t[n][:1500])\nEOF"
}
```


### [2026-10-16T05:15:41.298Z] TOOL RESULT

```
===== 288
ابحل ی
)بحل « بنتح اول و ضم حای بی نفطه و«شتکار» نیز گفته‌اند » لقری را نافع است .
و سکون ثانی و لام » نام یادشاه جایلسا باشد » و
آن شهپرست در مقابل جابلفا وهردو درعالم مثال
اند ؛ و بعضی جایرسا گفته اند که بجای لام .
رای قرشت باشد .
) بحاد - باخای نقطه داربر وزن‌اهواز.
تلم ولانتی است ازتر کستان مشهوریظلم:. گویند
مردم آنجا یشتر ترساو آتش پرستند و درآنجا
دبرست سار تسم ۱ .
ایحوسا ۴ - باسین بی نقطه بر وزن
محمودا . بزبان سربانی دوائی است که ب رکه
آن ساه برخی مابل باشد و آنرا« اپوخلما »
آیدا۵ - با دار ابجد بر وزن بد تام
بمعتی چم است که در مقابل جوهر باشد ۴ .
ابف‌آن - بر وزن افغان , بمعنی دودمان
و خاندان باشد - و بمعنی سزاوار و حستحق حم
آمده است ؛ و در موّبد الفضلاء با ذال نقطه دار
نوشته اند * .
ایدرم * ه بکس اول بروزن اسپرم .
نام کتلب شاکمونی ۷ و او باعتفاد کف ند
پیغمس صاحب کتاب است » و معنی این لفت
باعتفاد او اول و آخر کتابها باشد .
اير - یسکون ثانی بروزن صبر » حص‌ون
البلدان) ۸۵25 و ۸۵216 « لت نامه *. ۴ - مصحف کلب « انشوسا » و < انشا »
صت ۸ لغت ناهد *. ات مو ندالفتلاء حم همسن حعتی آورده , شاهدی برای‌آن د نده‌نشد.
محتملاست ممحف «ندام» باشد. «لفت نامه». ۴ ت هردوصورت اند شواهدمحتاح است.
«لفت نامه». ۵ - درسانکربت ۸۵0۵۲۳۵ ودرپالی20101018۲۳۳12. «د کرراجا».
۱ - ۷۵0 ۹2۷۷2 (-اکنی زاهد) وآن نامیاست که اغلب بدان 5002۳1۳8
2 موّسس آیین بودایی را مینامند . پدر او ۹۷0000202 رئی فبله 522
بود و سا کیامونی درنیمة قرن ششم متولد شده .
بشه از صفحهٌ ۷۷
شکی نیست که اصل الفبای عرب . عبرانی - آرامی‌است معهذا ۰ عرب که ازدبگرلفات
سامی آ کاهی نداشته است واز وی دیگر بعات استفراق تام درسنن خوش وبسیب تعصب قومی»
===== 289
- ۷ - ایکا کبا
و سکون الث و ها و رای قرشت ؛ نام اصلی
نیشابور است و ممدن فیروزه آلجاست ٩‏ .
ابر قباك ع من فان . نام ولایتی است
از توابم اره جان ۱ که میان اهواز و فاری
واقم است و آباد کرد قباد شهربار است ؛ و با
زای قطه دار هم کفته اند ۲ . #
ا پر کاد - باکاف‌بروزن‌اتکبار » بمعنی
متحیر و حیران و س رکردان باند ۸ .
ایکا کیا هیفتح اول وانی‌و کسرکاف
دوم تحتانی بال فکشیده , ننیده و تارعنکبوت را
کویند. اکر بر جراحت نهند خون را باز دارد
انت و بمربی «سحاب» گود ٩‏ - و بمعنی هرد
(۱) هم آمده است که دره‌قابل زن‌باشد, و بفنح
ثانی‌بلفت زند ویازید (۲)لت تناسل را گوید ۳
- و «بر » را نیز گفته الد که بمرمی « علی »
خوانند ۴ و بمعنی بر و آغوش هم هت  .‏
آ برش ع بنتح اول و تال ۰ بر وزن
مهوش ؛رنگه سرخ و سفید در هم امیخته را
گوبند . - و اسبی که نقطه های مخالف رنگه
او پر او باشد ۴  .‏
] پر ش خور شیف کنابه‌ازآسمانت.
ابر شهر - فتح اول و انی و رابع
(۱) چك : مردم ! )۱( چك : ژند و باژند ..
۱ - انسکرت 2080۴4 (با 200068 مرکب از0۳۵ - ۵0 بمعنی برنده وحامل
آب ) « وبلیامز ۳:۷۹ > اومتا 3072 بارتولمه ۹۵ بهلوی 27 « دهارله ۱۷۹ » « عنلی
۶ > ۸ نب رک ٩۱‏ . اففانی ۵۲2 . بلوچی 8۷1۲ (باران) « بارتولمه ۹۵ » , کردی ]اقلا .
اورامانی ۷۴۲ : 4 . اورآمان ۱۲۲ * .گلکی ۳9 دزفولی ۳۷ . ۳ 32602۲
حزواری است بمعنی ره » آلت رجولیت « بندهش ۱۱۲ ۰ ۶ یوستی » بندهش ص۵۱ * . اشتباه
نشود ا.« ابر » که در عربی بمعنی نره و فرزند فررینه است و 26779)2(8 هزوارش پمعنی آلت
رجولت « بوتکر ٩۳‏ ۰ . ۴ - اوتا ۱۳۵17 و ۱۳02۲ بمعنی بالا ۰ عالی»
سال‌کریت ۱1۳8۲1 « بارتولمه ۳۹۶ - ٩۵‏ ۰. پهاوی 8087 < منای ۲۹۹ < اونوالا ۳۳۵ ۰
«نب رکه ن 9
۴ - از آن ایرش وبور وختگك وسیاه 
===== 290
و نگذارد که جراحت ورم کند . وااگر بلس رکه
بردمل. وخيارك نهند ب رکرداند ۱ » وابرک کیاپ "
یز بنض آمده است که در آخرش بای ابجد
باشد . ٩‏
ابر که ین کاف » نم شهزیست از
عراق عجم . و چون‌آن شهر بر زمیتی که درته
آن کوه است واقم شده باين نام موسوم ماختند
ومعوب آن ابر قوه است ۴ حرایین زمان بتعریب
ار هر گنه - بکر ثاك و خم میم »
بمعنی ابی‌کپن است که اسفنج الب باشد ۴ .
ابر نجن - بفتح جیم‌بروزن ب رکندن»
حلقه ای باشد از طلا و نقره و امثال آن که
زان در دست و بای (۱) کنند ۴ و آنه در(۷)
دست کنند دست ابر نج و آنراکه در (۲) بای
کنند پای ابرنجن خوانند .
اتتهار دارد . ابر ن<سن - بر وزن فروردین ؛ بمعنی
اب رگن - بکس تاك و انوم ابر‌تجن است . وان حلقه‌ای باشد از طلا و نقره
که در (۲) دست و پای کنند ۴ .
ایرو ددن - کتابه از دا دادن
واشاره کردن باشد ۵ .
ها و سکون نون . چیزی است مانند مد کرم
خورده » چون بی آب گذارند اب را بخود کشد
واسفنج الیسر حمانت ۴ .
۱ - دلیل توایری است یوشای حق بیستی است همچون ابرکا کبا
لطيفي پنقل شموری. ومحتاح اید شواهد است «افت‌نامه».
۳ < ابرفوه » , حبط ابوسمد وبضی دیکر ۶ اپرقوبه » نوشته اند واحل فاري آن را
« ورکوه » نامند ومعنی آن « بالای کوه » است. و آن شهرست مشهور بارس از کورة اسطضر
ترديك بزد. « ممجم‌البلدان »؛ ساب ناحیه‌ای آباد ومهم‌بوده. وهوای آنکرمیرواراضی‌حاصلخیز
وقابل زراعت دارد . درخت سرو بیار کهنی درآنجا هست , اراضی آن از قنواتی حشروب میشود
که.بستی از آنها بیار طوبل است . محصول عمد آن تربالك وینبه وتتبا کو وقلات » شتجی ۱
بافنن کربای . کلردگ ورونای درآن بسیار بعمل آبد ۰« کبهان . جفرافبای سیاسی*44*.
۴ . رك : اسفنج . ۴ - آورنجن , خلخال . ٩9‏ رضا نمودن با اشارت
ابرو . دستوری دا
```


## [2026-10-16T05:15:46.020Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 - <<'EOF'\nt=open('data/verification/sources/refs/BQT_v1_pages.txt',errors='ignore').read().split('\\f')\nfor n in range(470,495):\n    p=t[n]\n    if 'برنج' in p or 'رنج ' in p:\n        i=p.find('برنج'); print('=====',n, p[:60].replace('\\n',' | ')); print(p[max(0,i-300):i+500]); \nEOF"
}
```


### [2026-10-16T05:15:46.388Z] TOOL RESULT

```
===== 485 ۱۲ حسه برد | ی ۰ | این شممها که در دل بسحق بر فروخت | از رهگذار نو
۱۲ حسه برد
ی ۰
این شممها که در دل بسحق بر فروخت
از رهگذار نور(۱) برنج شماله بود ۴ .
مخقف بر نج‌زار است که شالی‌زار باشد ۰
بر نجاسب بکسر اول وثالی وسکون
کشیده و بسین بر نج کابلی - نغمی است دواییو آن
می نقطه و بای کوچك وبز رک میباشد و کوچك آن بپتراست»
باشد ٩‏ کهآ نرا کرم و خشك است . مفاصل را نافم است .
بوی مادران ۱ بر نج مثاك بروزن ومعنی‌فلنج‌عشك
کوند و بعربی است که بالنگوی خودروی باشد ۴ . بواسیر را
حبق الراعی تافع است .
خانه بگسترندجمیم گزندکان بگریزند ؛ وباین
معنی‌بجای حرف آخر تای قرشت هم آمده‌است .
پر نحاسف ه با فا . بر وزن و ععنی
برنجاسپ است که کباه بوی‌ماد
===== 486 برنداف | بر ناف س بفتح اولو انی و سکون‌ثالث | و رامع بالف کشیده 
س کنابه ازسوارشدن‌باشد ۴.
بر نگ - بفتح اول وثانی بروزن‌خدنگ»
بمعتی جچری و درای و لق‌درخانه باشد - وکید
را نیز گویند که عربان مفتاح‌خوانند ؛ وبایشععنی
بش
با زای قطددار هم آمده است - و بضم اولوئانی
بمه‌نی اندوخثه و ذخیره و پی‌انداز باشد -. ونم
ولایتی است که قطب جنوبی آنجا دیده میشود -
و بکر اول و انی برنج کابلی را کویند » وآن
بر و بر وزن بدخو ۰ دبای تنك
بر و س ‏ بفتم اول بر وزن افوی »
کی از مچددقان نت۵ کی ولیک
را نیز گومشد , و باینمعنی با شین تقطه‌داربروزن
بر ورن « بر وزن آفیون » بمعنی برنو
باشد که دبای تنك و حریر نازك است » و باين
ممنی در مود الفضلا بجای نون اول بای ابجد
و بای حطی هر دو آمدم است .
بر فی » بقتح اول و سکون انی و ثالث
شحتانی رسده » مرطبان کوچك را گودند .
بر نیس بکسراول‌بروزن‌آدرس ؛نوعی
از بلوط باشد ۷ .
بر یش بضم اول وسکون ثانی‌و کسر
اك بتحتانی مجهول وشین نقطهدار زده ؛ پیچش
باش
```


## [2026-10-16T05:15:48.354Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 - <<'EOF'\nt=open('data/verification/sources/refs/BQT_v1_pages.txt',errors='ignore').read().split('\\f')\nfor n in [484,485]:\n    p=t[n]; print('=====',n); print(p)\nEOF"
}
```


### [2026-10-16T05:15:48.772Z] TOOL RESULT

```
===== 484
برحه
بر هه ۱ « بروزن کرعه: مثفب‌درود گری
باش که بدان چوب و نخته سوراخ کنند .
برن ‏ بروزن چمن . ام فصبه‌است در
فر فا ۴ ع بنتح اوز و سکون ثانی و نون
بالف کشیده . جوان و نوچة اول عمر و ظریف
را گونند - و بمعتی خوب و نيك هم هست -
و حنا را نیز کون دکه بردست و پا بندنده وضم
اول هم آمده است .
بر فاخی الستادن » کنابد از اطات
کردن و بلدب ایستادن باشد .
بر فاص ۴ - بروزن کربای, بمعنی‌غافل
و عادان - و غافلی و ناداتی باشد .
بر ناك ۴ « چختح اول بر وزن غمناله ۰
بمعنی برنا است که جوان و نوچةٌ اول عمر باشد
ور حنای دلت و بارا نیز گفته‌اند. و خ‌اوژهم
۱ رك : برماه.
1 نو ای
یعنی آدجه برس رکتابتهار نامها نویستد » وسسربی
القاب و عنوان گویند۷ .
بر ناه » بروزن حمراه » جوان و نوچة
اول عمر را گویشدب وحنای دست و پارا نیز
بر نایشتی - یکر بای حطیو سکون
شین فرشت و فوفانی‌بتحتانی رسیده ۰ بمعنی پشتی
و تعصب باشد چه برنایشتی کردن بمعنی پشتی
کردن و تسب نمودن است . #*
بر فج - فتح اول و انی و سکون نون
و جیم » آن‌باشد اکه سیب کوری‌با بجهت‌ناریکی
دست خور را مر دبوار با جابی بمالند تا وک
بیدا کاند ۷ ْ
پر فاد - بکس اود بر وزنکرفتار .
جوان اراده کنند . ناصر خسرو بلخی کوید :
داسفا ۱ : ۲ س ٩۹۳‏ . اه
۵ مرکب‌از: پیشوند بر (بار) ۳ نامه, ۷2۲-۲۵103
« اسفا ۱ : ۲ص ۱۹۰ . 1 - آمروز نمی دستورعملبکار
رود. ععرب آن «یر نامج». «رزی>.
غله‌است (3201۷3 ۳۷2۵()) که درمازندران. کلان » استراباد.
خوزستان؛ اسفهان وبرخی‌تقاط دیگر ابران ودر هندوسثان شرفی
و ژاين و چن میروید . « فرهنکگ روستابی ۲۶۵ » « کل کلاب
===== 485
۱۲ حسه برد
ی ۰
این شممها که در دل بسحق بر فروخت
از رهگذار نور(۱) برنج شماله بود ۴ .
مخقف بر نج‌زار است که شالی‌زار باشد ۰
بر نجاسب بکسر اول وثالی وسکون
کشیده و بسین بر نج کابلی - نغمی است دواییو آن
می نقطه و بای کوچك وبز رک میباشد و کوچك آن بپتراست»
باشد ٩‏ کهآ نرا کرم و خشك است . مفاصل را نافم است .
بوی مادران ۱ بر نج مثاك بروزن ومعنی‌فلنج‌عشك
کوند و بعربی است که بالنگوی خودروی باشد ۴ . بواسیر را
حبق الراعی تافع است .
خانه بگسترندجمیم گزندکان بگریزند ؛ وباین
معنی‌بجای حرف آخر تای قرشت هم آمده‌است .
پر نحاسف ه با فا . بر وزن و ععنی
برنجاسپ است که کباه بوی‌مادران باشد .
بر نج شماله - بنتح شین نقطهدارومیم
بالف کشیده و لام مفنوح » بممنی مزعفر است ۰
و آن طعامی‌باشد معروق . گوبند درشیرازطباخی
بود که پیوسته شبها برسرراهی تشستیو زردپلاوی
با پرنج درشتی پختی و درپیش خود فانوسی‌داشتی
رگاهی دوسه مشمل افروختی و فرباد کرد ی که
*یا به برنج شماله» و این بیت را نیز خواندی:
از طلا و نقره و امثال آن که زنان در دست‌ویای
7 آنسه وروت کتلت دست برنجن وآنچه
دریای کنند پای برنجن خوالند .
بر فجین ه بفتح اول بر وزن تبرزین »
بسعنی برنجن است که حلقَةٌ طلا و نفرء بلش د که
زئان در دست و با کنند .
یر فف « بنم اول بروزن خجند ؛ وبفتح
اول بروزن سمند ؛ هر دوآعده است بمعنی تیغ
و کمقی کر و آبدار و جوهردار ؛ و باین‌منی
با بای فارسی هم گفته‌اند ۴ - و بفتح اول بمعنی
مراد هم آهده است که حرریر ساده باشد ٩‏ .
۱0( چنن است درنشخ » در دبوان اطعمه: بوی.
۰ - و۲معآ۷۵ ۸۲۱۵۲1512 دک لکلاب::۲» «لك ۱ س ۲۰۵*.
؟ - دبوان‌بحق اطعمه. چاپ‌استانبول ص۵۸. ۴ ۸۷۲۱۸۵5 «لك ۱ص ۲۱*.
۴ راك ؛ فرند . سفق
بقبه ازصفحةٌ ۲۹۶ ۵ در پپلوی ۷۲۱1 «ناوادیا ۰۱۹۷
درفارسی‌نیز ثرنج, اوستابی [۱۵۲۷1۳ #» بونانی ۵۳۱۵201 ,افقانی ۷۲12118 «اسفا۱: ۱ص۱۷۷*.
از مآأخذ قدیم‌میتوان دانست که درروز کار هخامنشیان‌براج درایران بوده» شك‌نیست که این گیاءاز
سرزمین هند بابران رسیده» نام آن درسانکربت] ۷۲۸19 است که در بونانی 0۲2۷22 (درعرمی:ارز)
شده « فاب ۱ : ۳۳۵ » گیلکی [06۲6۳ , فریبزندی [۷26۲۵68 , برتي [06۲26۳ ۰ نطلنزی
۷6۲6۳ < 4 . ۱ ص ۰۲۸۱ ۰ سمنانی ۷۵۲8 ۰ سرخه ۷۵6۲46 , لاسکردی [۷6۲۵6۳ .
شهمیرزادی [۵۳۵60 «۲.۵ص۱۸۲*: ک_دی0۱۳۱0(0. ارمنی(0۲10 و۳110« اسفا۷:۱ص۱۸*.
۸ یز فلز مخصوص (0۲0026) را گویند .
۵ ار ای - منم‌اول, درپهلوی 8۳016083111 «اونوالا ۳۳۹ ب»؛ جوانی. رگ : برن.
```


## [2026-10-16T05:15:55.544Z] TOOL CALL #29: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-10-16T05:15:55.550Z] TOOL RESULT

```


```


## [2026-10-16T05:15:57.856Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/برنج",
 "prompt": "Give the Persian etymology section(s) for برنج 'rice' verbatim: Middle Persian form, Proto-Iranian form, Sanskrit cognate, origin (substrate?), and relation to Greek oryza."
}
```


## [2026-10-16T05:15:58.557Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ὄρυζα",
 "prompt": "Give the etymology section verbatim."
}
```


## [2026-10-16T05:15:59.207Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/rice",
 "prompt": "Give the etymology of rice verbatim."
}
```


## [2026-10-16T05:16:00.257Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/أرز",
 "prompt": "Give the Arabic etymology of أَرُزّ / أُرْز 'rice' verbatim, and any Persian ارز entry."
}
```


### [2026-10-16T05:16:00.907Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-10-16T05:16:03.743Z] TOOL RESULT

```
# Etymology Section

The etymology indicates that ὄρυζα is "A borrowing from an Eastern Iranian language, from Proto-Iranian *wrinǰiš or *wriHǰíš." The entry references Pashto وريژې (wriže) as a comparison and directs readers to Old Persian *vrinjiš for additional related forms.

The word ultimately traces back through "Proto-Iranian" to "Proto-Indo-Iranian" origins, with the etymological chain documented in the source material showing how this grain term traveled across language families.
```


### [2026-10-16T05:16:03.791Z] TOOL RESULT

```
# Arabic Etymology of أَرُزّ/أُرُزّ (Rice)

Based on the Wiktionary entry provided, the etymology section for أَرُزّ/أُرُزّ states:

**"alternative form of رُزّ (ruzz)"**

The entry does not provide a deeper etymological explanation for the rice term itself beyond this reference to رُزّ as the primary form.

## Persian Entry

The web page content provided contains only English Wiktionary material for the Arabic word أَرْز. There is no Persian ارز entry included in this document. To obtain Persian etymological information, you would need to consult the Persian Wiktionary or another lexicographic source.
```


### [2026-10-16T05:16:05.785Z] TOOL RESULT

```
# Persian Etymology for برنج (Rice)

Based on the Wiktionary entry, here's the Persian etymology section verbatim:

**Middle Persian form:** "blnc" (/⁠brinǰ⁠/)

**Proto-Iranian form:** Not explicitly listed for the rice meaning. The etymology states it is "Inherited from Middle Persian blnc (/⁠brinǰ⁠/)."

**Sanskrit cognate:** The entry does not provide a Sanskrit cognate for the rice sense. However, under Arabic Etymology 1, it mentions Sanskrit _विडङ्ग_ (viḍaṅga) and _विडङ्गा_ (viḍaṅgā) as sources for the false black pepper meaning.

**Origin:** The entry provides no specific information about substrate origins for the rice term.

**Relation to Greek oryza:** The document contains no mention of Greek oryza or its relationship to برنج.

The Persian section emphasizes that برنج meaning "rice" descends directly from Middle Persian with no further etymological details provided regarding earlier Indo-European connections.
```


## [2026-10-16T05:16:07.856Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Old_Persian/vrinjiš",
 "prompt": "Give the full etymology and descendants verbatim (Proto-Iranian, Indo-Iranian, origin; descendants incl. Middle Persian, Persian, Greek, Arabic)."
}
```


## [2026-10-16T05:16:08.919Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/rice",
 "prompt": "Give the English etymology section of 'rice' verbatim, including the ultimate origin (substrate, Proto-Indo-Iranian etc.)."
}
```


## [2026-10-16T05:16:09.759Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/رز",
 "prompt": "Give the Arabic etymology of رُزّ 'rice' verbatim (source language)."
}
```


## [2026-10-16T05:16:10.711Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/व्रीहि",
 "prompt": "Give the Sanskrit etymology section verbatim (Proto-Indo-Iranian form, substrate origin)."
}
```


### [2026-10-16T05:16:14.733Z] TOOL RESULT

```
# Arabic Etymology of رُزّ (Rice)

Based on the Wiktionary entry, the Arabic word رُزّ (ruzz, "rice") was **borrowed from Aramaic** אֲרוּזָא (ʔăruzzā) / ܐܘܪܘܙܐ (ʔuruzzā) and ܪܘܙܐ (rūzā).

The entry notes this term is a "doublet of برِنْج (birinj)" and traces back further through Proto-Iranian origins to Ancient Greek ὄρυζα (óruza).
```


### [2026-10-16T05:16:15.832Z] TOOL RESULT

```
# Sanskrit Etymology of व्रीहि

The Wiktionary entry does not provide a Proto-Indo-Iranian form for this word. Instead, it describes the etymology as follows:

According to the source, व्रीहि is "A Wanderwort of unclear ultimate origin, though likely from a language southeast of Indo-Iranian." The word is either borrowed from Dravidian languages or, per scholar Michael Witzel, from an unknown South Asian source, possibly Austroasiatic, such as Proto-Austroasiatic *ɓa(ː)ʔ meaning "paddy rice." Related words exist in Iranian, Ancient Greek, and Semitic languages, with the Middle Persian blnc ("rice") cited as a comparative example.

The entry does not identify a Proto-Indo-Iranian etymological root for this Sanskrit term.
```


### [2026-10-16T05:16:16.738Z] TOOL RESULT

```
# Etymology and Descendants of Old Persian *vrinjiš

## Etymology

The term derives from **Proto-Iranian *wrinǰiš**, which itself comes from **Proto-Indo-Iranian *wriHǰʰíš**. This is "unexplained nasalized variant of *wriHǰíš."

Cognates include Sanskrit vrīhí (rice), Sogdian forms, Pashto wriže, and various other Iranian language equivalents across the family.

An intriguing cross-linguistic connection exists: the word is "possibly related to Proto-Dravidian *wariñci (rice)," suggesting ancient trade or contact between Indo-Iranian and Dravidian speakers.

## Descendants

The word's evolution produced a rich descendant family:

**Middle Persian** forms include /brinǰ/ in multiple scripts, which developed into:

- **Classical Persian**: برنج (birinj)
- **Tajik**: биринҷ (birinj)  
- **Dari**: برنج (birinj)
- **Kurdish** varieties: birinc
- **Ottoman Turkish**: برنج (birinǰ), پرنج (pirinç)
- **Baluchi, Zazaki, Uyghur**: Various adapted forms

Additionally, the word entered non-Iranian languages:
- **Old Armenian**: բրինձ (brinj)
- **Georgian**: ბრინჯი (brinǯi)
- **Classical Syriac**: ܒܪܢܓ (brng)
- **Elamite**: cuneiform attestations

This demonstrates significant medieval trade language influence across the Near East and Central Asia.
```


### [2026-10-16T05:16:17.366Z] TOOL RESULT

```
# English Etymology of 'Rice'

From Middle English *rys*, from Old French *ris*, from Old Italian *riso*/*risi*, from Medieval Greek *ὄρυζα* (óruza). This derives from an Eastern Iranian language related to Middle Persian *blnc* (*brinǰ), Northern Kurdish *riz*, and Zazaki *riz*.

The term is theorized to have come to Iranian languages from Sanskrit *व्रीहि* (vrīhi). Prior to Sanskrit, it may have been borrowed from either Dravidian languages (compare Proto-Dravidian *wariñci*, meaning "rice") or Austroasiatic languages further east.

An alternative theory proposes Medieval Greek *ὄρυζα* derives from Hebrew *אורז* (órez), from South Arabian *areez*, ultimately from Old Tamil *𑀅𑀭𑀺𑀘𑀺* (arici).

The word is a doublet of *arroz*.

[WebFetch note: this page's text is 172387 characters long and the answer above covers only characters 0 to 100000; the final 72387 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```


## [2026-10-16T05:16:20.353Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=وریزه",
 "prompt": "Quote verbatim all dictionary definitions of وریزه (Dehkhoda, Moin, Amid, etc.), especially any meaning 'rice' and its source."
}
```


## [2026-10-16T05:16:21.438Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=ارز&d=moein",
 "prompt": "Quote verbatim Moin's entries for اُرُز / ارز meaning rice, including origin tag ([ع.] etc.)."
}
```


## [2026-10-16T05:16:22.299Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=سوپر",
 "prompt": "Quote verbatim definitions of سوپر and سوپرمارکت with origin tags (فر. / انگ.), from Amid, Moin, Dehkhoda etc."
}
```


## [2026-10-16T05:16:23.151Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=ابر&d=moein",
 "prompt": "Quote verbatim Moin's entry for اَبَر meaning 'above, over, super' (prefix/preposition), with origin tag (په.)."
}
```


### [2026-10-16T05:16:24.004Z] TOOL RESULT

```
Command failed with no output
```


### [2026-10-16T05:16:26.465Z] TOOL RESULT

```
# Moin's Entry for اَبَر (Prefix/Preposition)

According to Moin's dictionary, the entry for اَبَر with the preposition/prefix sense includes:

"(اَ بَ) [ په . ] (اِ.) بالا، مق پایین"

This indicates the term carries meanings relating to spatial position, with etymology marked as پشتو (Pashto origin). The entry associates it with concepts of "above" and directional relationships, functioning as a preposition or prefix in Persian.
```


### [2026-10-16T05:16:26.477Z] TOOL RESULT

```
# Dictionary Definitions of وریزه

Based on the content provided, here is the definition found:

**Dehkhoda Dictionary:**
"رگی است که از معده تا جگر رود" (a vessel/vein that runs from the stomach to the liver), sourced from Montahal-arab, Aqrab al-Mawarid, Anandraj, and Nazem al-Atebba.

**Note:** The search results shown do not include any definition of وریزه meaning "rice." The primary meaning presented is anatomical—referring to a duct or vessel in the body.
```


### [2026-10-16T05:16:27.394Z] TOOL RESULT

```
I've reviewed the Persian dictionary page content provided, but I don't find entries for اُرُز or ارز meaning "rice" in this material.

The entries shown define **ارز** as:
- Foreign currency/exchange
- Banking documents valued in foreign currency
- Archaic terms for value, price, or worth

The page displays synonyms, homophones, and related terms, but none of the visible Moin dictionary entries document a rice definition with origin tags ([ع.] or otherwise).

To locate Moin's entry for rice (اُرُز), you would likely need to search that term directly in the dictionary rather than reviewing this particular results page for ارز.
```


## [2026-10-16T05:16:29.960Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/ارز/",
 "prompt": "Quote verbatim any entries (Moin, Dehkhoda, Amid) for اُرُز / اَرُز / ارز meaning rice (برنج), with origin tags."
}
```


## [2026-10-16T05:16:30.905Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/وریزه/",
 "prompt": "Quote verbatim any entries for وریزه, especially meaning rice (برنج), with sources (Borhan, Dehkhoda, Moin)."
}
```


## [2026-10-16T05:16:31.699Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/سوپر/",
 "prompt": "Quote verbatim the entries for سوپر (Amid, Moin) with origin tags (فرانسوی/انگلیسی)."
}
```


### [2026-10-16T05:16:36.424Z] TOOL RESULT

```
Based on the provided web page content, I can only find one entry for وریزه:

**From Dehkhoda Dictionary:**
"وریزه. [ وَ زَ / زِ ] ( ع اِ ) رگی است که از معده تا جگر رود."

Translation: A vessel/duct that runs from the stomach to the liver.

**Important note:** The web page does not contain any entries defining وریزه as rice (برنج). The single definition provided refers to an anatomical structure. No entries from Borhan or Moin dictionaries appear on this page—only the Dehkhoda Dictionary entry is displayed.
```


### [2026-10-16T05:16:38.138Z] TOOL RESULT

```
# Dictionary Entries for سوپر

**Amid Dictionary Entry:**
"۱. عالی ، برتر. ۲ - بزرگ . ۳ - (اِصت . ) ویژگی هر نوع وسیلة نقلیة مسافربری که بزرگ تر و دارای امکانات بهتر و رفاه بیشتر است . ۴ - سکسی" [English origin: انگ.]

**Moin Dictionary Entry:**
"سوپرمارکت" and "اتوبوسی که اتاق آن راحت تر و تعداد صندلی هایش از اتوبوس های دیگر کمتر است" [English origin]

**Etymology Note:**
According to user suggestions, the word derives from the French term for "superior/higher" and ultimately traces back to Latin "superior" and Sanskrit "āpar" (higher).
```


### [2026-10-16T05:16:38.226Z] TOOL RESULT

```
# ارز (Rice Meaning)

Based on the dictionary entries provided, here are the verbatim citations for the rice definition:

**Dehkhoda Dictionary:**
"( آرز )… ( ع اِ ) اَرُزّ. رُزّ. برنج ( یکی از حبوب )."

**Amid Dictionary:**
"= برنج۱"

**Moein Dictionary:**
The entry does not explicitly list rice as a primary definition in the excerpt provided.

All three historical Persian lexicons confirm that اُرُز/اَرُز represents an older or variant form referring to rice (برنج), classified as one of the grains. The Dehkhoda and Amid entries note this as a classical or dialectal usage.
```


## [2026-10-16T05:16:42.591Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; for f in incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt BQT_v1_pages.txt MON_part1.txt MON_part2.txt; do echo \"== $f\"; grep -n 'وریزه\\|وريزه\\|ورىزه' $R/$f | head -5; done"
}
```


### [2026-10-16T05:16:42.920Z] TOOL RESULT

```
== incoming/BQT/BQT_v4_pages.txt
== incoming/BQT/BQT_v5_pages.txt
== BQT_v1_pages.txt
28191:بمعتی پارم پاره وریزه ریزه و ره ذره‌باشد۸ ,
29077:بمعنی نملین و عصاباشد9 - وریزه و خرد؛ هر
== MON_part1.txt
28221:پاستوریزه: 6( (مص‌م.) گرم کردن 
== MON_part2.txt
```


## [2026-10-16T05:16:46.166Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; head -c 400 $R/MON_part1.txt; echo; grep -n 'برنج' $R/MON_part1.txt | head -8; grep -n 'اُرُز\\|ارز.*برنج\\|ارز:' $R/MON_part1.txt | head -8; grep -n 'وریز' $R/MON_part2.txt | head"
}
```


### [2026-10-16T05:16:46.511Z] TOOL RESULT

```
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع 

مه مر وه ود 

3 ور 133131313 


هم مشب جج جب بیج چم �
1342:برنج که با آب کار کند؛ دنگی که به نیروی 
1343:آب حرکت کند و بدان شلتوک برنج 
1345:پوسته از برنج (به اصطلاح شلت و کث) (بیشتر 
2651:بدست آید. آرد گندم؛ آرد جو آرد برنج. 
4025:نو برنج» | کوله. 
4355:می‌بر ند و آن نیم‌دایره‌ای است که از برنج یا 
5248:اورنجن: صحلیه‌عة [ - آبرنجن - بر نجن ] 
5249:(امر.) دست بنده دست آبرنجن» دست 
9839:ارز: 2 () بهاء قیمت» ارزش, ارج» نرخ. 
9845:ارز: »۵ (ع. ارز] (.) (گسسسیا.) درخت
```


## [2026-10-16T05:16:48.553Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; sed -n 9835,9860p $R/MON_part1.txt; grep -n '^برنج\\|برنج: ' $R/MON_part1.txt | head"
}
```


### [2026-10-16T05:16:48.940Z] TOOL RESULT

```
اردل: امه [ع.] (ص‌تفضد. رذالت) 
ردیل تر» خوارتر» زبون‌تر» پست‌تر» اخس؛ 
دون تر» فرومایه تر» نا کس تر 

ارز: 2 () بهاء قیمت» ارزش, ارج» نرخ. 
قدر» ر تبه» مر تمه» درجه چاه مقام. حرمت» 
احترام» عرت» و بهر ۵» فایده» سود. کام 
ابرو. (ص.) ارجمند» ارزنده» بر قیمت؛ مق. 
ناارز» بی‌ارز. (ا.) سندهای تجاری که ارزش 
آنها به پول‌های بیگانه معین شده باشد؛ سعر. 
ارز: »۵ (ع. ارز] (.) (گسسسیا.) درخت 
سلیمان‌نوعی عرعر. سرو. درخت انار. 
ارزاق: 2« [ع.] ج. رزق. روزی‌هسا 
خواروبار. جیر ه) جیرة سپاهیان. ادارة 
خواروبار» سازمان تهیه و پبخش ارزاق و 
خواروبار. 

ارزان: «هه (ص.) آنچه ارزنده باشد به 
بهای وقت» چیزی که به قیمتش می‌ارزد» 
ارزش‌دار. کم‌بها؛ رخیص؛ مق. گران. لایق؛ 
شایسته» درخورء سزاوار. فرومایه. 

ارزانی: -2۳20 (ص نسه.) ارزنده. درخوره 
لایسق» سزاوار» مستحق. دروش» بی‌توا؛ 
نادار. صالح (مق. طالح)» سزا (مق. ناسزا)» 
اهل. پیشکش. (حامص.) کسم بهائی؛ کسم 
1342:برنج که با آب کار کند؛ دنگی که به نیروی 
5250:برنجن. خلخال» پای آور نجن. 
23750:برنج و یا نقره که بر صندوق زنند خصوصا. 
32560:برنج جوشیده شده در آب تهیه کنند و با 
61670:برنجن. ساعدیند آهنین که در روز جنگ در 
83124:برنج کاشته باشند) کشتزار برنج. 
87925:شیربرنج: لجه:»0-.5 (امر.) خوراکیی که با
```


## [2026-10-16T05:16:52.395Z] TOOL CALL #48: WebSearch

```json
{
 "query": "\"وریزه\" برنج",
 "mode": "standard"
}
```


### [2026-10-16T05:16:58.430Z] TOOL RESULT

```
Web search results for query: ""وریزه" برنج"

Links: [{"title":"Shir Berenj","url":"https://en.wikipedia.org/wiki/Shir_Berenj"},{"title":"Nan-e berenji","url":"https://en.wikipedia.org/wiki/Nan-e_berenji"},{"title":"چطور میزان آرسنیک برنج را کاهش دهیم 1","url":"https://whc.iums.ac.ir/uploads/59/2022/Oct/15/چطور میزان آرسنیک برنج را کاهش دهیم_1.pdf"},{"title":"rice (Q5090)","url":"https://www.wikidata.org/wiki/Q5090"},{"title":"اتیمولوژی برنج و rice","url":"https://myth.tarikhema.org/?p=7404"},{"title":"wild rice","url":"https://abadis.ir/entofa/wild-rice/"},{"title":"abadis.ir","url":"https://abadis.ir/fatofa/برنج/"},{"title":"globalsymbols.com","url":"https://globalsymbols.com/symbolsets/arasaac/symbols/44865?locale=de"},{"title":"whatsapp.com","url":"https://whatsapp.com/channel/0029VbABYB4AzNbmdL8TNo0B"}]

Based on the search results, I found information about the term "وریزه برنج" (vriže berenj):

The term "وریزه" (vriže) relates to the etymology of rice, with the word appearing in Persian as a form related to Sanskrit vrihi, meaning rice. The word وریهی-انگه in Sanskrit and Avestan means "rice product".

The search results show that "وریزه" comes from the Avestan وَرِسَ-ی, meaning "fine-haired" or "resembling white hair", which refers to the appearance of rice grains.

Additionally, برنج (berenj) means rice and can also refer to a brass alloy made of copper, zinc, and lead, though in this context "وریزه برنج" appears to refer to rice or rice-related products.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-10-16T05:17:06.798Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/upér",
 "prompt": "Summarize etymology (relation to *h₁upó) and list descendants verbatim for: Avestan, Old Persian, Middle Persian, Persian; Latin super/summus; Greek hypér; Proto-Germanic *uber/*uberi and English over."
}
```


## [2026-10-16T05:17:07.462Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/summus",
 "prompt": "Give Latin etymology of summus verbatim."
}
```


## [2026-10-16T05:17:08.103Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/sirloin",
 "prompt": "Give English etymology of sirloin verbatim."
}
```


## [2026-10-16T05:17:09.199Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ابر",
 "prompt": "Give the Persian etymology section(s) verbatim for ابر meaning 'above, super-' (abar), incl. Middle Persian and Old Persian forms, and relation to بر 'on, over'."
}
```


### [2026-10-16T05:17:11.652Z] TOOL RESULT

```
# Etymology of Sirloin

According to the Wiktionary entry, sirloin's etymology is:

"From Middle English *surloine*, from Old French *surlonge*, from *sur la longe* (literally 'above the loin')."

The term's origin traces back through these linguistic layers, with the Old French phrase literally meaning "above the loin," which accurately describes the anatomical location of this beef cut on the animal.
```


### [2026-10-16T05:17:13.049Z] TOOL RESULT

```
# Proto-Indo-European *upér: Etymology and Descendants

## Etymology
The root derives from "*úp" (above) plus the locative adverbial suffix "*-er". It shares the same root as "*up-ó" (up), forming spatial adverbs with comparable suffixes.

## Key Descendants

**Iranian Branch:**
- Younger Avestan: upara
- Proto-Iranian: *úparah

**Romance:**
- Latin: super (also basis for summus)

**Greek:**
- Ancient Greek: ῠ̔πέρ (hŭpér)

**Germanic:**
- Proto-Germanic: *uber, *uberi
- English: over (descended from *uber)

The word "above, over" maintained consistent semantic meaning across Indo-European languages, appearing as a preposition or adverbial modifier denoting spatial position or superiority across Romance, Greek, and Germanic branches.
```


### [2026-10-16T05:17:13.128Z] TOOL RESULT

```
# Latin Etymology of *summus*

According to the Wiktionary entry, *summus* derives from Proto-Italic *\*supemos*, which itself comes from Proto-Indo-European *(s)úp-m̥mo-s*. 

The source explains: "from *\*upó* + *\*-m̥mo-*." The term is cognate with Proto-Germanic *\*ufumô* and Sanskrit *उपम* (upamá, "uppermost").

The entry also notes relationships to related Latin terms *suprēmus* and the suffix *-issimus*.
```


### [2026-10-16T05:17:13.174Z] TOOL RESULT

```
# Persian Etymology for ابر (abar) - "Above/Super-"

## Etymology 2

The entry states it was "Inherited from Middle Persian ـ𐭠𐭯𐭫 (ʾp̄l /⁠abar⁠/)" which also produced بر (bar). This derives from Proto-Iranian *upári, which comes from Proto-Indo-Iranian *upári and ultimately Proto-Indo-European *upér.

The relationship to بر is direct: both modern Persian forms descend from the same Middle Persian root 𐭠𐭯𐭫.

Cognates include English "over," Latin "super," Ancient Greek ὑπέρ (hupér), and German "über," demonstrating the ancient Indo-European lineage of this preposition meaning "above" or "over."
```


## [2026-10-16T05:17:18.493Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; grep -n -o 'abar \\[[^]]*\\][^.]*\\.' $R/PHD.txt | head -3; grep -n -i '^rice\\|^summit\\|^sum,\\|^over,\\|^super\\b\\|^hyper\\|^sirloin' $R/SKT.txt | head; grep -n 'برنج\\|اَبَر\\|ابر' $R/incoming/ARY/ARY_pages.txt | head -8; grep -n -i 'BERENJ\\|BIRINJ\\|ABAR\\b' $R/incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-10-16T05:17:18.847Z] TOOL RESULT

```
161:abar [ODM < А дат; bl | M "be, N bar] up; on, over.
225:abar [hcpl | M?c?br, № zabar] above.
9019:Hyper-,  prefix,  denoting  excc».   (L.«      ■ Gk.)     h.  Aypcr-,  for  Gk.  vwip,  above,  be-     1 yood,   alliert   to   L.  su/tr.      lience  Ayper» b<uon,  a  transposition  of  words  from  natural order,  lit.  'x  going  beyond'  (from  ^Vfir, to  go)  ;    Ayp<r^bortan,    extreme    norlhcm (from  ^o^tat,  north  wind!  ;  kyptr-boU,  ex-      ^ aggeralion.  Gk.  iiM*^oKii   (from  f}dAA<iv,      fl to  throw,  cast).  1
10797:Sirloin,  surioin.  (F. - L.)  M.E. snr^ hyn\  XV  cent.  —  O.  F.  surhngt  U4th cent.),  the  surluiu. * F.  jMr,  upon,  above; iongty  loin  (above).  %  TTie  story  abont taming  the  tain  into  sir-ioim  by  knighting it  is  mere  trash.
17322:Sirloin,  for  Surloin  ;  see  Lumbar.
87:معتقد بودند که گهواره‌ی آریایی‌های ابرنژاد شمال باختری اروپا بوده و از آنجا به سرزمین‌های دیگر
113:ارتش و فناوری وگسترش از راه کوچگری را میسر نمود. بنابراین دیدمان (17733083) مردمان این
291:همریشه‌اند می‌توان نتیجه گرفت که آنان در رام کردن اسب و استفاده از ترابرهای چرخدار پیشگام
292:بوده‌اند و تحرکك و تفوقی که سوارکاری و ترابری به آنها داده عامل بزرگی در گسترش آنها بوده
431:اروپایی به ویژه زبان‌های کهن اروپایی وجود دارد. کمی بعد که به بررسی نوشتارهای کهن ابراني (به
544:باید به طور علمی و سامانمند بررسی و اثبات گردد. مثلاً آوای یونانی 2۳3 برابر است با آوای ژرمنی
560:واژه‌ی بنیادین را احیاکرد. مثلاً پس از تعبین برابرهای واژه‌ی «زمین» (سانسکریت: 4۵7۸8 یونانی؛ . ,
917:۱-برابری و اخوت.۲- رفتار نیمه جنونآمیز و سرمستانه هنگام نبرد یا تهاجم یا مراسم وابسته به
2091:‘APAR, ABAR, ABRAG,(PAHLAVD) «5 4 UPARA., UPARIY. (AVESTAN) glo, |
3107:OLD SAXON) pS p-S WABAR, VAVAR, VAR
```


## [2026-10-16T05:17:21.465Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs/incoming/ARY; python3 - <<'EOF'\nimport re\nR='data/verification/sources/refs/incoming/ARY/'\nt=open(R+'ARY_latin_index_pages.txt',errors='ignore').read()\ni=t.find('APAR, ABAR'); print(re.findall(r'\\[pdf page \\d+\\]',t[:i])[-1:]); print(t[i-1200:i+600])\nEOF"
}
```


### [2026-10-16T05:17:21.792Z] TOOL RESULT

```
['[pdf page 74]']
 EISARN GOTHIC) Sa,
“POKORNY ———~—~=~=«89-300, 1S | © «(OLD SCANDINAVIAN) Sigh!
BARNHART: (RON) 544 TSARN, EIR, JARN
MACKENZIE: 6, (IRON) 120 ISARN HOLD SAXON) of J y-S\s
‘BUCK: 613 . OLD HIGH GERMAN) pS galT
ONIONS: (IRON) 485 TSARN, ER
SKEAT: (IRON) 308 EISEN, ERZ GERMAN) glulT
AMINDAROV: rat ISERN, (OLD ENGLISH) pS pS:
MALLORY 1a IREN
ve 1gbG olay TRON ENGLISH) SS
JERN (DANISH) jails
Ne
[pdf page 74]
i, |
vO | saul ule ale
leetlooy
Bree Sab abs 2 dls aol
Bad Y bh 23 Sls cal
OLD CHURCH SLAVIC) gS §3%\ , -YRINT, AEITI, HMAVESTAN) gt 3}
16, IDI, 171 ANTI, :
EITI, EI-ME, ©. (LITHUANIAN) gi} AITIY HOLD PERSIAN) seas. oo
EUNT, EIMI AY.. : PAHLAVE hy
mT (OLD PRUSSIAN) oS go. YMAS (TOKHARIAN A} A 5, j\55
EIMU, IET MLATVIAN) (93) og YAM A(TOKHARIAN B) B «s,\55
. ACHITTITE) coca YAN, AYA TE, :(SANSKRIT) he
LIT, E-HU, PA-IMI, IM- YANTI, EMI, ETI
; EMI (GREEK) «gy
REFERENCES eehay IRE, EO LATIN) (45\) 53
POKORNY ——=SSs*~*~*«~*«iS IRAI (FRENCH) 31
BARNHART: (wEnD) 1228 IR (SPANISH) Pray
‘DELAMARRE: (ALLER) 254 IRE : HITALIAN) ‘ga!
‘MACKENZIE: 14, (COME) 107 IR (PORTUGUESE) it 5
SKEAT: . (Ely 256 IDDJA GOTHIC) WSs
ver sla abcd BODE . (OLD ENGLISH) yy pS
u s
: je datisal “4
oO gaT yes,” veh
‘APAR, ABAR, ABRAG,(PAHLAVD) «5 4 UPARA., UPARIY. (AVESTAN) glo, |
ABARAGAN, ABARIGAN UPAIRI i
UPARI, UPARA :(SANSKRIT) 2» Sit. UPARIY — (OLD PERSIAN) sul, 4 |
[pdf page 75]
(COLL sees’ 4) oh LVF
OVER (NORWEGIAN) 5533 VER ARMENIAN) 24,
OVER (DUTCH) «sacle HUPER, HYPER GREEK) gly
FOR- | HOLD IRISH) oS 5 SUPER LATIN) 3
'eVERTAMO- CELTIC) (gS) UFAR, UFARO AGOTHIC) S35
VER- GAULISH) SS (OLD SCANDINAVIAN) p652hes}
. YFIR
‘REFERENCES cathy HOLD SAXON) ff gipS le
POKORNY, —=~=~S~S*«wLOS 1106, UBAR, UVER
BARNHART: (OVER) 742 UVER, OVER :(OLD FRISIAN) 4S 53.3
DELAMARRE: (SUR, AU-DESSUS) 303 {OLD HIGH G
```


## [2026-10-16T05:17:26.007Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; grep -n -i 'VRIHI\\|BRINJ\\|ORYZA\\|ORUZA' $R/incoming/ARY/ARY_latin_index_pages.txt | head; grep -n -i '^Rice\\|^Summit\\|^Sum,\\|^Over,\\|^Super' $R/SKT.txt | head; grep -n -i 'rice' $R/LKT.txt | head -5; grep -n -i 'aruzz\\|óryza\\|oryza' $R/FVQ.txt $R/AFA.txt $R/AFM.txt | head"
}
```


### [2026-10-16T05:17:26.324Z] TOOL RESULT

```
201:superl. — SQperlatire.
6196:superficicB.  (L.)  L.  xu/erjida,  sur- face, outer  face.  — L.  tu/tr,Mho\c;/attej, fate.
6837:superfluous.  (L.)  'L.n4perJiMus,oitx- flowiug.  —  L  mftr,  over ;  jCutrt^  to  flow.
11529:superlative,  on  the  model  of  afier'ftutst^ foremost.
12511:superntunerary.  (F.— L.)  F.  nr/Vr- nttnuraire  (Col.).  —  L.  sv/er-nu/turariui^ cxcvssive  in  number.
16702:superscription.   (F.  — L.)     f. schption'.   Cot.  — L.  ace  neperteripli
18716:superstructure   (L.")    FrtmU aho^e;   nr>d  Struoture. Strugrgle,  vb.  (Scand.)  M-R. a  weakened  iovm  of  stroJUixm  *.  not
18865:Supercargo ;  »cc  Car.
18866:Supercilious,  disdainful.  (L.)  From L.'  suptrcili-Hfti,  (i)  an  e)-e-l>row,  (i) haughtiness,  as  expressed  by  raising  the eye-brows.  — L.  supcr^  abo\-e;  n'/iuw,  eye- lid, lit.  'covering*  of  the  eye.  Cf.  L. ctlare,  to  hide;  sec  Ooll.
18867:Supererogation ;  see  Bog&tion.
479:'Eine  Fichtenart,  pinus  cedrus'.  Hieraus mit  dem  ar.  Art.  sp.  alerce  'Lärche'; siz.  arzanu  'Tanne'.  Auffallend  ist  die Ähnlichkeit  mit  lat.  lärix,  laricem,  wor- aus it.  larice,  pg.  larico;  dtsch.  Lärche. [GrSVociSic  227.    ML  635.    DE  98.
720:'Segen  (nämlich  Gottes)',  ebenso  tk. bereket  'dass.,  Fruchtbarkeit';  hieraus rum.  berechet  'Fülle,  Fruchtbarkeit'; bulg.  bereket  'Überfluß',  serb.  bericet 'Glück,  Überfluß'.  [Sain  47.  Bern SlEtWb  49.
2889:'Mais,  Zea  Mais';  hieraus  dtsch.  Kuku- rutz;  russ.  kuhiruza,  serb.  ktikuruz, üech.  kukurice,  poln.  kukurydza  'Mais'.
3718:'Stück,  Teil'  [Horn  Np  EtS.  62,  Nr.  271], ebenso  tk.  para  'Stück,  Geldstück,  '/^<> tk.  Piaster';  hieraus  bulg.  para  'der Para',  serb.  pari  'Geld',  besparicen  'un- entgeltlich'; rum.  para  'Geldstück,  Para'; vom  Adj.  paralij  'reich'  kommt  rum. paraleü  'reich'  [Gi^ä  POP  hat  in  seinem Wörterbuch  S.  325  paraleü  'mächtiger Löwe'];  A&m.pärälu^ä  'Gänseblümchen'. [Löbel  EITAP  74,    Mikl  SIEtWb  232.
7097:labarda  823 /rtc-c«  1295 /accÄe  2130 /a/ia  siz.  24 lambiccare  79 lambiccio  79 lanibicco  79 /an/"«  1535 laparderi  siz.  823 laparduni  siz.  823 /a^is  lazzuli  1311 larice  114 lazzaretto  1310 lazzarone  1310 lazzeruola  2ii06 lazzuli(lapis)  1311 Ze/ffli  siz.  1313 libeccio  1313 i?7ac  1319 Hmbiccio  79 limone  1322 limuni  siz.  1322 Usciardo  1581 K«rfo  2127 «M<o  2127 1329
```


## [2026-10-16T05:17:29.189Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; R=data/verification/sources/refs; grep -n 'Rice,\\|Summit,\\|Sum,  \\|Over,  \\|Super-,' $R/SKT.txt | head -8; grep -n -i \"oryza\\|riso\" $R/LAT.txt | head -3; grep -n -i 'summus' $R/LAT.txt | head -3"
}
```


### [2026-10-16T05:17:29.533Z] TOOL RESULT

```
12948:''^'*  ^^^-  **S^'  ^-  5^>  Goth,  au^fw. (The  common  base  is  l/tlNA.) Over,  above,  across.  (E.)  M.E.  ffudr {=»OTrri.  A.S.  o/ir.  +  Du.  ovtr,  \(x\. y^r, Dan.  ovtr,  Swcd.  o/c^r,  G.  iib^r,  Goth, •i/ar,  Gk.  imip,  L.  S'up<r\  Skt.  upari, above.  The  Aryan  form  is  UPARl,  loca- tive case  of  UPARA.  upper  (Skt.  tt/ara, L.  s-upems,  A.  S.  y/cra).  This  is  a  compa- rative ibnn  from  Aryan  UFA  (Skt.  w/a, near,  on,  under ;  Gk.  vw6^  L.  s-u&,  Goth,  m/, under;  E.  <rve  in  tUjovc).  Closely  allied to  Up.  ^Thc  senses  '  over '  and  '  under  * arc  curiously  mixed.)  ^T  Hence  a  large number  of  compounds  beginning  with  nvr, which  present  no  difficulty.
22152:see  Bnb-. tpT' ;  sec  Super-, ■uge ;  see  £xtr^. :ct ;  see  Bub-.
1844:aerisonus \ixXx6xxvnoC . Cf. aussi pent-etre aestumo, que L.Havet, MSL
4957:Pline), souvent corroapue, en agrisonia, M.L.995a , acrimonia, argi-
7744:1307. A separer de briso, -as qu'on trouve dans le scol.de Perse, 1,76,
7783:*breuimus, cf. pour le suffixe tuus, summus, etc.
16243:Demum est peut-etre un superlatif form 4 sur de, comme summus est forme
16899:summus, impudicus, infamis, etc.), quartus ( anularis, honestus, medi¬
```


## [2026-10-16T05:17:41.444Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; F=\"python3 tools/fetch_source.py\"; \n$F 'https://en.wiktionary.org/wiki/برنج' --note 'page 520, root Urigh, Persian berenj < MP brinj' ;\n$F 'https://en.wiktionary.org/wiki/ὄρυζα' --note 'page 520, root Urigh, Greek oryza borrowed from Eastern Iranian' ;\n$F 'https://en.wiktionary.org/wiki/Reconstruction:Old_Persian/vrinjiš' --note 'page 520, root Urigh, OP *vrinjiš, PIIr *wriHjhis, Dravidian link' ;\n$F 'https://en.wiktionary.org/wiki/rice' --note 'page 520, root Urigh, English rice chain and Wanderwort origin' ;\n$F 'https://en.wiktionary.org/wiki/رز' --note 'page 520, root Urigh, Arabic ruzz < Aramaic aruzza' ;\n$F 'https://en.wiktionary.org/wiki/व्रीहि' --note 'page 520, root Urigh, Sanskrit vrihi Wanderwort' ;\n$F 'https://abadis.ir/fatofa/ارز/' --note 'page 520, root Urigh, Dehkhoda/Amid arozz = rice' ;\n$F 'https://abadis.ir/fatofa/وریزه/' --note 'page 520, root Urigh, varizeh not found as rice' ;\n$F 'https://abadis.ir/fatofa/سوپر/' --note 'page 520, root Upo, Persian super loanword (Amid tag)' ;\n$F 'https://vajehyab.com/?q=ابر&d=moein' --note 'page 520, root Upo, Moin abar [Pahlavi] bala' ;\n$F 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/upér' --note 'page 520, root Upo, PIE uper descendants' ;\n$F 'https://en.wiktionary.org/wiki/summus' --note 'page 520, root Upo, Latin summus < *sup-mo-' ;\n$F 'https://en.wiktionary.org/wiki/sirloin' --note 'page 520, root Upo, sirloin < OF surlonge' ;\n$F 'https://en.wiktionary.org/wiki/ابر' --note 'page 520, root Upo, Persian abar/bar < MP abar < PIr *upari' 2>&1 | tail -3\npdftoppm -f 520 -l 520 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg520 && mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg520.png data/verification/sources/refs/ocr/BOOK/520.png && echo ok"
}
```


### [2026-10-16T05:17:43.118Z] TOOL RESULT

```
(eval):2: no such file or directory: python3 tools/fetch_source.py
(eval):3: no such file or directory: python3 tools/fetch_source.py
(eval):4: no such file or directory: python3 tools/fetch_source.py
(eval):5: no such file or directory: python3 tools/fetch_source.py
(eval):6: no such file or directory: python3 tools/fetch_source.py
(eval):7: no such file or directory: python3 tools/fetch_source.py
(eval):8: no such file or directory: python3 tools/fetch_source.py
(eval):9: no such file or directory: python3 tools/fetch_source.py
(eval):10: no such file or directory: python3 tools/fetch_source.py
(eval):11: no such file or directory: python3 tools/fetch_source.py
(eval):12: no such file or directory: python3 tools/fetch_source.py
(eval):13: no such file or directory: python3 tools/fetch_source.py
(eval):14: no such file or directory: python3 tools/fetch_source.py
(eval):15: no such file or directory: python3 tools/fetch_source.py
ok
```


## [2026-10-16T05:17:44.266Z] AGENT

zsh does not word-split the variable, so I'll call the script directly.


## [2026-10-16T05:17:49.522Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; while IFS='|' read -r u n; do python3 tools/fetch_source.py \"$u\" --note \"$n\" 2>&1 | tail -1; done <<'EOF'\nhttps://en.wiktionary.org/wiki/برنج|page 520, root Urigh, Persian berenj < MP brinj\nhttps://en.wiktionary.org/wiki/ὄρυζα|page 520, root Urigh, Greek oryza borrowed from Eastern Iranian\nhttps://en.wiktionary.org/wiki/Reconstruction:Old_Persian/vrinjiš|page 520, root Urigh, OP *vrinjiš, PIIr *wriHjhis, Dravidian link\nhttps://en.wiktionary.org/wiki/rice|page 520, root Urigh, English rice chain and Wanderwort origin\nhttps://en.wiktionary.org/wiki/رز|page 520, root Urigh, Arabic ruzz < Aramaic aruzza\nhttps://en.wiktionary.org/wiki/व्रीहि|page 520, root Urigh, Sanskrit vrihi Wanderwort\nhttps://abadis.ir/fatofa/ارز/|page 520, root Urigh, Dehkhoda/Amid arozz = rice\nhttps://abadis.ir/fatofa/وریزه/|page 520, root Urigh, varizeh not found as rice\nhttps://abadis.ir/fatofa/سوپر/|page 520, root Upo, Persian super loanword (Amid tag)\nhttps://vajehyab.com/?q=ابر&d=moein|page 520, root Upo, Moin abar [Pahlavi] bala\nhttps://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/upér|page 520, root Upo, PIE uper descendants\nhttps://en.wiktionary.org/wiki/summus|page 520, root Upo, Latin summus < *sup-mo-\nhttps://en.wiktionary.org/wiki/sirloin|page 520, root Upo, sirloin < OF surlonge\nhttps://en.wiktionary.org/wiki/ابر|page 520, root Upo, Persian abar/bar < MP abar < PIr *upari\nEOF"
}
```


### [2026-10-16T05:17:57.503Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/082c4af70edb954b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/99893527cfcfce42.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a6223b1b8b6517f1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6aed4f367e9efe24.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7034861c740439c1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e09b8e0bbcbfeb8a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ba486b8f64252411.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/048546ffd32405bc.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/cfa888bdbb0efc5b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/17c999f120abc6c7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3f81616a129e0888.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3463dd5c553e37d1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/851c27e7037c5d27.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fa1886882bc88396.txt
```


## [2026-10-16T05:20:41.272Z] TOOL CALL #59: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-520.py <<'PYEOF'\nimport json\nW='https://en.wiktionary.org/wiki/'\nUPER=W+'Reconstruction:Proto-Indo-European/upér'\nPOK1105={\"ref\":\"POK:1105\",\"status\":\"supports\",\"note\":\"POK_full.txt line 88131 'Root / lemma: uper, uperi ... over, above' ... 'Old Indie uparí, Avestan upairi, ap. upariy' ... 'gr. ὑπέρ' ... 'Latin Umbrian super' ... 'Gothic ufar ... Old High German ubar(*uperi)'; Page(s): 1105-1106.\"}\nKLN1105={\"ref\":\"KLN:1105\",\"status\":\"supports\",\"note\":\"KLN_1966.txt line 26789 s.v. over: 'OE. ofer ... OHG. ubar ... Goth. ufar ... cogn. with OI. upari, Avestic upairi, ‘over, above, beyond’ ... Gk. hyper ... L. super ... All these words derive fr. I.-E. *uper, *uperi, ‘over, above, beyond’, which is prop. comparative of *upo, ‘from below; turning upward’'.\"}\nAHDu={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. uper (AHD_watkins1985.txt line 1105)\",\"stance\":\"supports\",\"note\":\"'uper. Over. 1. Extended form *uperi in Germanic *uberi in: a. Old English ofer, over: OVER ... 2. Variant form *(s)uper in: a. Latin super ... SUPERIOR, SUPREME ... SIRLOIN ... d. suffixed (superlative) reduced form *sup-mo- in Latin summus, highest: SUM, SUMMIT ... 3. Basic form *uper in Greek huper, over: HYPER-. [Pok. uper 1105.]'\"}\nWLDu={\"src\":\"WLD\",\"where\":\"Bd. I p. 192 (WLD_Bd1_pages.txt, ~200th page block)\",\"stance\":\"supports\",\"note\":\"'got. ufar, ahd. ubir, aisl. yfir (letztere beide sicher aus *uperi)' ... 'lat. super, superus „der obere“ ... (davon lat. supra „oberhalb“, superior, suprēmus)'.\"}\nPOKu_d={\"src\":\"POK\",\"where\":\"p. 1105-1106 s.v. uper (POK_full.txt l. 88131 ff.)\",\"stance\":\"supports\",\"note\":\"'Material: 1. Old Indie uparí, Avestan upairi, ap. upariy'; 'Latin super ... superior, supremus'; 'Gothic ufar, ... Old High German ubar (*uperi)'.\"}\nKLNsum={\"src\":\"KLN\",\"where\":\"KLN_1966.txt line 37429 s.v. sum\",\"stance\":\"supports\",\"note\":\"'L. summa ... prop. fem. of the adj. summus, ‘highest’ ... Summus stands for *sup-mos and is rel. to L. super, ‘above’, sub, ‘under’ ... OI. upamáh, ‘the highest’'.\"}\nSKTover={\"src\":\"SKT\",\"where\":\"SKT.txt line 12948 s.v. Over\",\"stance\":\"supports\",\"note\":\"'A.S. ofer ... G. über, Goth. ufar, Gk. ὑπέρ, L. s-uper, Skt. upari, above. The Aryan form is UPARI ... comparative form from Aryan UPA' — Skeat's hyphenated 's-uper' notation is the model for Nourai's 's-upper-mo'.\"}\nNOTCH=lambda r,why: {\"ref\":r,\"status\":\"not_checked\",\"note\":why}\n\ne0_nodes=[\n {\"id\":1,\"lang\":\"Indo-European\",\"words\":\"Uper\",\"verdict\":\"confirmed\",\n  \"derivation\":\"PIE *upér / *upéri 'over, above' is the comparative-locative formation (*up- + adverbial/locative *-er(i)) built on the same base as *upo 'under, up from under', so the arrow root→node (upo → uper) is the standard analysis (Pokorny 1105 and 1106 cross-refer the two; Klein calls *uper 'prop. comparative of *upo'). The two meanings 'under' and 'over' both stem from the notion 'from below upward'.\",\n  \"derivation_fa\":\"ریشهٔ هندواروپایی آغازین *uper / *uperi «بالای، فراز، فراتر از» صورت تفضیلی‑مکانیِ همان پایهٔ *upo «زیر، از زیر به بالا» است؛ پوکورنی (۱۱۰۵–۱۱۰۶)، کلاین و واتکینز هر دو را از یک بن می‌دانند. معنای «زیر» و «زبر» هر دو از مفهوم «از پایین رو به بالا» برخاسته است. ادعای نورایی درست است.\",\n  \"sources\":[UPER],\n  \"ref_check\":[POK1105,KLN1105],\n  \"consulted\":[AHDu,WLDu,{\"src\":\"IEC\",\"where\":\"IEC.txt grep 'uper'\",\"stance\":\"silent\",\"note\":\"Mann's uper- entry not reached in the OCR text (grep for the lemma returns only unrelated compounds).\"},SKTover]},\n {\"id\":2,\"lang\":\"Avestan\",\"words\":\"upairi\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Avestan upairi 'above, over, beyond' (adv., prep. with acc./instr.) = OP upariy, Skt. upári, < Proto-Iranian *upári < PIIr *upári < PIE *upéri; Avestan -ai- is the regular epenthesis before -ri (vowel i anticipated). Bartholomae col. 394 lists it with OP upariy.\",\n  \"derivation_fa\":\"اوستایی upairi «بالای، بر، فراتر از» برابر پارسی باستان upariy و سنسکریت upári است و از ایرانی باستان *upári و هندواروپایی *uperi آمده؛ -ai- در اوستایی از پیش‌آیی (اپنتز) i پیش از -ri پدید آمده است. بارتولومه (ستون ۳۹۴) و کنت آن را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n  \"sources\":[W+'ابر'],\n  \"ref_check\":[POK1105,KLN1105],\n  \"consulted\":[{\"src\":\"BRT\",\"where\":\"col. 394 (BRT.txt offset ~1058825)\",\"stance\":\"supports\",\"note\":\"'upairi, p. upariy 1) Adv. 'superne'; a) 'oben' ... 2) Praep. mit Akk. und Instr.; a) 'oben über'...'\"},\n               {\"src\":\"KNT\",\"where\":\"Lexicon/§269 (KNT_full.txt l. 12745, 12806)\",\"stance\":\"supports\",\"note\":\"'upariy, prep. w. acc.; pref. w. verbs' ; 'upariy ‘over’, with slight idea of motion'.\"},\n               WLDu,AHDu]},\n {\"id\":3,\"lang\":\"Pahlavi\",\"words\":\"apar\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Middle Persian abar (Book Pahlavi written with the Aramaic ideogram QDM, ʾpl; Manichaean ʾbr) 'on, over, upon; above, more than' < OP upariy / Proto-Iranian *upári: initial u- > a- before the labial, intervocalic -p- lenited to -b-/-w- (Pazand awar), final -i lost. 'apar' is Nyberg's older transcription of the same word that MacKenzie writes abar.\",\n  \"derivation_fa\":\"فارسی میانهٔ abar (در خط پهلوی با هزوارش QDM نوشته می‌شد؛ مانوی ʾbr) «بر، روی، بالای، بیش از» از پارسی باستان upariy / ایرانی باستان *upári است: u- آغازی به a- بدل شده، پ میان دو واکه به ب (و در پازند به w: awar) نرم شده و -i پایانی افتاده است. apar خوانش کهن‌ترِ نیبرگ از همین واژه است. هرن، مکنزی و نیبرگ آن را تأیید می‌کنند.\",\n  \"sources\":[W+'ابر'],\n  \"ref_check\":[{\"ref\":\"HRN\",\"status\":\"supports\",\"note\":\"HRN.txt l. 2076-2081, no. 191 '(2)ber, eber, auf, über' ... 'ap. upariy über; aw. upairi; phlv. apar, päz. awar, apartar, apartum; ai. upári'.\"}],\n  \"consulted\":[{\"src\":\"PHD\",\"where\":\"p. 4 (PHD.txt l. 161)\",\"stance\":\"supports\",\"note\":\"'abar [QDM < Aram. qdm; ʾpl | M ʾbr, N bar] up; on, over.'\"},\n               {\"src\":\"NYB\",\"where\":\"Glossary s.v. apar (NYB_vol2_glossary.txt l. 505-507)\",\"stance\":\"supports\",\"note\":\"'²apar [MDM, erroneous reading of OAram QDM] 1. adv. above ... 2. prep. a) local: over, on ... — Av. upairi, OP upariy; MPrthPrs ʾbr; Paz. awar; NP bar.'\"},\n               {\"src\":\"ARY\",\"where\":\"pdf p. 74-75 (printed 75-76), entry ابر/بر\",\"stance\":\"supports\",\"note\":\"Latin index: 'APAR, ABAR, ABRAG (PAHLAVI) ... UPAIRI, UPARA (AVESTAN) ... UPARIY (OLD PERSIAN) ... UPARI (SANSKRIT)'; references 'POKORNY 1105, 1106'.\"}]},\n {\"id\":4,\"lang\":\"Persian\",\"words\":\"abar; bar 2\",\"verdict\":\"confirmed\",\n  \"derivation\":\"NP abar 'above, super-' (now revived as a prefix: abar-mard 'superman', abar-qodrat 'superpower') continues MP abar unchanged; NP bar 'on, upon, over' (and bartar 'higher, better', bartarin, barin 'highest, supreme') is the same MP abar with loss of the unstressed initial a- (aphaeresis), exactly as Hübschmann notes for arašk : rašk 'wie abar zu bar'. Nourai's cross-reference to Bhergh ('high') reflects the old alternative derivation of bar/barin from *bʰerǵʰ- (cf. Av. barəz-); for the preposition bar 'on' modern sources (MacKenzie, Nyberg, Wiktionary) take only the *upári line, though barz/bālā belong to *bʰerǵʰ-.\",\n  \"derivation_fa\":\"«اَبَر» در فارسی نو (و پیشوند تازه‌ساختِ ابرمرد، ابرقدرت) همان فارسی میانهٔ abar است و «بَر» (و برتر، برترین، برین) نیز از همان abar با افتادن a- آغازیِ بی‌تکیه پدید آمده؛ هوبشمان این را «مانند abar به bar» می‌خواند. معین در حاشیهٔ برهان قاطع (ص ۷۹) «بر» را از اوستایی upairi «بالا، عالی» و پهلوی apar می‌داند. اشارهٔ نورایی به ریشهٔ Bhergh («بلند») برای «بر» پذیرفته نیست؛ پژوهش امروزی «بر» را تنها از *upari می‌داند. ادعای اصلی نورایی درست است.\",\n  \"sources\":[W+'ابر','https://vajehyab.com/?q=ابر&d=moein'],\n  \"ref_check\":[{\"ref\":\"BQT:79\",\"status\":\"supports\",\"note\":\"BQT_v1_pages.txt leaf 289 (= printed p. 79), s.v. ابر: 'و «بر» را نیز گفته‌اند که بعربی «علی» خوانند ۴'; footnote ۴: 'اوستا upairi ... بمعنی بالا، عالی، سانسکریت upari «بارتولمه ۳۹۶-۳۹۵» پهلوی apar' (Latin forms garbled in OCR, Persian frame legible).\"}],\n  \"consulted\":[{\"src\":\"HRN\",\"where\":\"no. 191, p. 44-45\",\"stance\":\"supports\",\"note\":\"'(2)ber, eber, auf, über' < 'ap. upariy; aw. upairi; phlv. apar, päz. awar'.\"},\n               {\"src\":\"HUB\",\"where\":\"no. 71, p. 13 (HUB.txt l. 335-338)\",\"stance\":\"supports\",\"note\":\"'Np. arašk ... ist die ältere Form zu rašk ... wie abar zu bar auf etc.'\"},\n               {\"src\":\"MON\",\"where\":\"vajehyab.com/?q=ابر&d=moein\",\"stance\":\"supports\",\"note\":\"'(اَ بَ) [په.] (اِ.) بالا، مق پایین' — tagged Pahlavi.\"},\n               {\"src\":\"ARY\",\"where\":\"pdf p. 74-75\",\"stance\":\"supports\",\"note\":\"entry lists Pahlavi APAR, ABAR < Av. UPAIRI, OP UPARIY, Pokorny 1105-1106.\"},\n               {\"src\":\"PHD\",\"where\":\"p. 4\",\"stance\":\"supports\",\"note\":\"'abar ... N bar' — MacKenzie gives NP bar as descendant.\"}]},\n {\"id\":5,\"lang\":\"Latin\",\"words\":\"super\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Latin super 'over, above, beyond' (adv., prep., prefix) < Proto-Italic *super < PIE *(s)uper, the variant with 's-mobile' (or with the s- of *eks/*ups-, as Pokorny suggests) of *uper; superus, superior, suprēmus are derivatives.\",\n  \"derivation_fa\":\"لاتین super «بالای، بر، فراتر از» از ایتالیکی آغازین *super و هندواروپایی *(s)uper، گونهٔ s-دار *uper است؛ superus، superior و suprēmus از آن ساخته شده‌اند. پوکورنی، کلاین و واتکینز همگی آن را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n  \"sources\":[UPER],\n  \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. uper: '2. Variant form *(s)uper in: a. Latin super, super-, above, over: ... SUPER-, SUPERIOR, SUPREME ... SIRLOIN'.\"}],\n  \"consulted\":[POKu_d,WLDu,{\"src\":\"KLN\",\"where\":\"KLN_1966.txt l. 37473 s.v. super-\",\"stance\":\"supports\",\"note\":\"'L. super-, fr. super, ‘over, above, on the top of; beyond’ ... cogn. with OI. upári, Gk. hyper ... fr. I.-E. base *uper-, *uperi-'.\"},SKTover]},\n {\"id\":6,\"lang\":\"French\",\"words\":\"\",\"verdict\":\"plausible\",\n  \"derivation\":\"Empty pass-through node: French super (prefix and colloquial adjective 'super', supermarché) < Latin super. Persian dictionaries (Amid) tag سوپر as English rather than French; for the 20th-century Persian loan 'super(market)' both French and English are possible donors, so the French intermediary is possible but not certain.\",\n  \"derivation_fa\":\"گرهٔ میانجی بی‌واژه: فرانسوی super (پیشوند و صفت گفتاری) از لاتین super است. فرهنگ عمید «سوپر» را انگلیسی می‌داند، پس میانجی‌گری فرانسوی ممکن است ولی قطعی نیست؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\":['https://abadis.ir/fatofa/سوپر/'],\n  \"ref_check\":[NOTCH(\"None\",\"node carries no reference\")],\n  \"consulted\":[{\"src\":\"KLN\",\"where\":\"s.v. super- (l. 37473)\",\"stance\":\"partial\",\"note\":\"'Cp. also pref. sur-, representing OF., F. sur' — Klein notes French inherited sur- (< super); learned super- is a Latinism.\"},\n               {\"src\":\"SKT\",\"where\":\"l. 22152 index 'see Super-'\",\"stance\":\"silent\",\"note\":\"no French-specific entry for super.\"}]},\n {\"id\":7,\"lang\":\"Persian\",\"words\":\"sŭper\",\"verdict\":\"plausible\",\n  \"derivation\":\"Persian سوپر sūper 'super, superior' and سوپرمارکت 'supermarket' are 20th-century European loans (Latin super via a Western language). Nourai routes it through French; Amid tags سوپر as English (انگ.), and سوپرمارکت is clearly the English compound supermarket (French uses supermarché). Real loanword, route partly debatable.\",\n  \"derivation_fa\":\"«سوپر» و «سوپرمارکت» وام‌واژه‌های سدهٔ بیستم از زبان‌های اروپایی‌اند و در نهایت به لاتین super می‌رسند. نورایی آن را از راه فرانسوی می‌داند، ولی فرهنگ عمید آن را انگلیسی (انگ.) نشان داده و «سوپرمارکت» آشکارا از انگلیسی supermarket است (فرانسوی supermarché می‌گوید). وام‌گیری درست است، اما مسیر فرانسوی با احتیاط پذیرفتنی است.\",\n  \"sources\":['https://abadis.ir/fatofa/سوپر/'],\n  \"ref_check\":[{\"ref\":\"AMD:1242\",\"status\":\"partial\",\"note\":\"Amid online (abadis.ir/fatofa/سوپر): '۱. عالی، برتر. ۲. بزرگ ...' tagged English (انگ.), not French; print page 1242 not mappable.\"},NOTCH(\"VOP:220\",\"Moshiri's Farhang-e Vazheha-ye Orupayi not available online (refs_online.json)\")],\n  \"consulted\":[{\"src\":\"MON\",\"where\":\"abadis.ir/fatofa/سوپر (Mo'in section)\",\"stance\":\"partial\",\"note\":\"Mo'in lists 'سوپرمارکت' and 'اتوبوسی که اتاق آن راحت‌تر ...' as a European loan; online text gives no French tag.\"},\n               {\"src\":\"ARY\",\"where\":\"ARY_latin_index_pages.txt pdf p. 75\",\"stance\":\"silent\",\"note\":\"entry ابر/بر lists 'SUPER (LATIN)' only as a cognate; no Persian سوپر.\"}]},\n {\"id\":8,\"lang\":\"English\",\"words\":\"super, supreme, superior, sirloin\",\"verdict\":\"confirmed\",\n  \"derivation\":\"English super (adj./prefix, from Latin super-), supreme (16th c., < MFr. suprême < L. suprēmus, superl. of superus), superior (ME, < OF superiour < L. superior, compar. of superus) and sirloin (ME surloine < OF surlonge 'above the loin', sur < L. super + longe 'loin'; the 'sir-' spelling is a later folk-etymological respelling, the knighting story is 'mere trash' per Skeat) all go back to Latin super.\",\n  \"derivation_fa\":\"انگلیسی super (از پیشوند لاتین super-)، supreme (از فرانسوی میانه suprême، از لاتین suprēmus صفت عالیِ superus)، superior (از فرانسوی کهن superiour، از لاتین superior) و sirloin (از فرانسوی کهن surlonge «بالای کمر»: sur از لاتین super + longe «کمر»؛ املای sir- ریشه‌شناسی عامیانه است) همه به لاتین super بازمی‌گردند. ادعای نورایی درست است.\",\n  \"sources\":[W+'sirloin',UPER],\n  \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. uper: 'Latin super ... SUPER-, SUPERABLE, SUPERIOR, SUPREME, (SUPREMO), SUR-; SIRLOIN'.\"}],\n  \"consulted\":[{\"src\":\"KLN\",\"where\":\"l. 35351 s.v. sirloin; l. 37554 s.v. supreme\",\"stance\":\"supports\",\"note\":\"'sirloin ... var. spelling of surloin ... fr. OF. surlogne, surlonge ... from sur, ‘above’, and logne'; 'supreme ... L. supremus, superlative of superus ... fr. super'.\"},\n               {\"src\":\"SKT\",\"where\":\"l. 10797 s.v. Sirloin\",\"stance\":\"supports\",\"note\":\"'O. F. surlonge ... F. sur, upon, above; longe, loin ... The story about turning the loin into sir-loin by knighting it is mere trash.'\"}]},\n {\"id\":9,\"lang\":\"Latin\",\"words\":\"s-upper-mo, summus\",\"verdict\":\"transcription_suspect\",\n  \"derivation\":\"Latin summus 'highest, topmost' (n. summum/summa 'top, peak') < *sup-mos < PIE *(s)up-mo- (superlative of *upo/*uper, cf. Skt. upamá- 'uppermost', OE ufemest), with -pm- > -mm- assimilation. The book prints 's-upper-mo': a Skeat-style hyphenated reconstruction (*s-up-mo-) in which the double 'pp' is Nourai's misprint/conflation with English 'upper'; the extraction is faithful. Correct pre-form is *sup-mos.\",\n  \"derivation_fa\":\"لاتین summus «بالاترین، فرازترین» (و summum/summa «قله، سر») از *sup-mos و هندواروپایی *(s)up-mo- صفت عالیِ *upo/*uper است (هم‌ریشه با سنسکریت upamá- «بالاترین»)؛ -pm- به -mm- همگون شده است. کتاب «s-upper-mo» چاپ کرده که خطای چاپیِ نورایی (آمیختگی با upper انگلیسی) برای *s-up-mo- است؛ استخراج درست است. ریشه‌شناسی درست، صورتِ بازسازی‌شده نادرست چاپ شده است.\",\n  \"error_in\":\"book\",\"book_prints\":\"s-upper-mo, summus\",\"correct_form\":\"*sup-mos (< PIE *(s)up-mo-), summus\",\n  \"sources\":[W+'summus'],\n  \"ref_check\":[{\"ref\":\"KLN\",\"status\":\"supports\",\"note\":\"KLN_1966.txt l. 37429 s.v. sum: 'Summus stands for *sup-mos and is rel. to L. super, ‘above’, sub, ‘under’' — Klein's form is *sup-mos, not 's-upper-mo'.\"}],\n  \"consulted\":[{\"src\":\"POK\",\"where\":\"p. 1106 s.v. upo (POK_full.txt ~l. 88255)\",\"stance\":\"supports\",\"note\":\"'Latin summus (*supmos) \\\"the höchste\\\"'.\"},AHDu,SKTover,\n               {\"src\":\"LAT\",\"where\":\"LAT.txt l. 16243\",\"stance\":\"partial\",\"note\":\"Ernout-Meillet: 'comme summus est formé sur ...' — treats summus as superlative formation.\"}]},\n {\"id\":10,\"lang\":\"English\",\"words\":\"sum, summit\",\"verdict\":\"confirmed\",\n  \"derivation\":\"sum (ME summe < OF summe/somme < L. summa 'top; chief point; total', fem. of summus — Romans wrote the total above the addends) and summit (ME somete < OF sommet, dim. of som 'top' < L. summum, neut. of summus).\",\n  \"derivation_fa\":\"انگلیسی sum از فرانسوی کهن summe/somme و لاتین summa «سر، جمع کل» (مؤنثِ summus؛ رومیان حاصل جمع را بالای اعداد می‌نوشتند) و summit از فرانسوی کهن sommet، مصغّرِ som «قله»، از لاتین summum است. ادعای نورایی درست است.\",\n  \"sources\":[W+'summus'],\n  \"ref_check\":[NOTCH(\"None\",\"node carries no reference\")],\n  \"consulted\":[KLNsum,{\"src\":\"KLN\",\"where\":\"l. 37441 s.v. summit\",\"stance\":\"supports\",\"note\":\"'OF., fem. of somet, dimin. of som, ‘summit’, fr. L. summum, prop. the neut. of summus, ‘highest’'.\"},AHDu]},\n {\"id\":11,\"lang\":\"Greek\",\"words\":\"huper\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Ancient Greek ὑπέρ hypér 'over, above, beyond, on behalf of' < PIE *upér with the regular Greek initial *u- > hu- (psilosis absent in Attic), exact match of Skt. upári, Av. upairi.\",\n  \"derivation_fa\":\"یونانی باستان ὑπέρ (hypér) «بالای، فراتر از» از هندواروپایی *uper است؛ u- آغازی در یونانی به hu- (با دمش) بدل شده. هم‌ریشهٔ مستقیم اوستایی upairi و سنسکریت upári است؛ ادعای نورایی درست است.\",\n  \"sources\":[UPER],\n  \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. uper: '3. Basic form *uper in Greek huper, over: HYPER-'.\"}],\n  \"consulted\":[POKu_d,KLN1105|{\"src\":\"KLN\",\"where\":\"s.v. over (l. 26789)\",\"stance\":\"supports\"} if False else {\"src\":\"KLN\",\"where\":\"s.v. over (l. 26789)\",\"stance\":\"supports\",\"note\":\"'Gk. ὑπέρ (adv. and prep.) ... All these words derive fr. I.-E. *uper'.\"},SKTover]},\n {\"id\":12,\"lang\":\"English\",\"words\":\"hyper\",\"verdict\":\"confirmed\",\n  \"derivation\":\"English hyper- (prefix, and colloquial adj. 'hyper' since the 1940s, clipped from hyperactive) < Latin hyper- < Greek ὑπέρ.\",\n  \"derivation_fa\":\"انگلیسی hyper- (پیشوند، و صفت گفتاری hyper کوتاه‌شدهٔ hyperactive) از لاتین hyper- و یونانی ὑπέρ آمده است. ادعای نورایی درست است.\",\n  \"sources\":[UPER],\n  \"ref_check\":[NOTCH(\"None\",\"node carries no reference\")],\n  \"consulted\":[{\"src\":\"SKT\",\"where\":\"l. 9019 s.v. Hyper-\",\"stance\":\"supports\",\"note\":\"'Hyper-, prefix, denoting excess. (L. — Gk.) L. hyper-, for Gk. ὑπέρ, above, beyond, allied to L. super'.\"},AHDu]},\n {\"id\":13,\"lang\":\"Germanic\",\"words\":\"uberi\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Proto-Germanic *uberi / *ubar 'over' < PIE *upéri / *upér by Grimm's law (*p > *f) and Verner's law (*f > *b after unaccented syllable since PIE accent was on the second syllable). Gothic ufar, OHG ubar/ubiri, ON yfir, OE ofer.\",\n  \"derivation_fa\":\"ژرمنی آغازین *uberi / *ubar «بالای» از هندواروپایی *uperi است: p به f (قانون گریم) و سپس، چون تکیه روی هجای دوم بود، f به b (قانون ورنر) بدل شده؛ گوتی ufar، آلمانی کهن ubar، انگلیسی کهن ofer. ادعای نورایی درست است.\",\n  \"sources\":[UPER],\n  \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. uper: '1. Extended form *uperi in Germanic *uberi in: a. Old English ofer, over'.\"}],\n  \"consulted\":[POKu_d,WLDu,{\"src\":\"KLN\",\"where\":\"s.v. over (l. 26789)\",\"stance\":\"supports\",\"note\":\"'OHG. ubar, ubir ... ubari, ubiri (adv.) ... Goth. ufar'.\"}]},\n {\"id\":14,\"lang\":\"English\",\"words\":\"over\",\"verdict\":\"confirmed\",\n  \"derivation\":\"English over < ME over < OE ofer 'over, above' < Proto-Germanic *uber(i); OE f between vowels was voiced [v].\",\n  \"derivation_fa\":\"انگلیسی over از انگلیسی میانه over و انگلیسی کهن ofer (با f میان‌واکه‌ای که v تلفظ می‌شد) و ژرمنی آغازین *uber(i) است. ادعای نورایی درست است.\",\n  \"sources\":[UPER],\n  \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. uper: 'Old English ofer, over: OVER'.\"}],\n  \"consulted\":[{\"src\":\"KLN\",\"where\":\"l. 26789 s.v. over\",\"stance\":\"supports\",\"note\":\"'over, adv. and prep. — ME., fr. OE. ofer, ‘over, above’ ...'.\"},SKTover]},\n]\n\nKLNrice={\"src\":\"KLN\",\"where\":\"KLN_1966.txt l. 32853 s.v. rice\",\"stance\":\"supports\",\"note\":\"'rice — ME. rys, ris, fr. OF. ris (F. riz), fr. It. riso, fr. VL. *oryzum, fr. L. oryza, fr. Gk. oryza, fr. OPers. brizi, fr. Afghan vrize, ult. fr. OI. vrihih, ‘rice’'.\"}\nSYNrice={\"src\":\"SYN\",\"where\":\"§8.46 RICE, p. 519 (SYN.txt l. 13094-13095)\",\"stance\":\"partial\",\"note\":\"Table 'RICE ... Skt. vrīhi- Av. —'; text: '... of the word seen in Skt. vrīhi- (AV+), Afghan vrīzē, etc. Boisacq 712' — Buck gives no Avestan word and no IE etymology.\"}\nHRNrice={\"src\":\"HRN\",\"where\":\"no. 208, p. 47 (HRN.txt l. 2208-2213)\",\"stance\":\"supports\",\"note\":\"'birinj, gurinj 'Reis'. Semn. varinj ... aw. *verenja-; skr. vergl. vrīhi- ... Vielfach entlehntes, gewiss ursprünglich arisches Wort ... afγ. vrize geht auf die Form ohne Nasal zurück, wie gr. ὄρυζα ... osst. uruz, arab. eruz'.\"}\nHUBrice={\"src\":\"HUB\",\"where\":\"no. 208, p. 27 (HUB.txt l. 884-886)\",\"stance\":\"supports\",\"note\":\"'Die meisten iran. Formen für birinj = gurinj 'Reis' haben i-Vokal, daher ap. *vrinji-, iranisch *vrinji-, *vriži-? (afgh. wriže ...)'.\"}\nBQTrice={\"ref\":\"BQT:265\",\"status\":\"supports\",\"note\":\"BQT_v1_pages.txt leaf 485 (printed p. 265), continuation of the برنج footnote: 'در پهلوی brinj ... اوستایی [*...] یونانی oryza، افغانی vrīže ... از مآخذ قدیم می‌توان دانست که در روزگار هخامنشیان برنج در ایران بوده؛ شک نیست که این گیاه از سرزمین هند به ایران رسیده، نام آن در سانسکریت vrīhi است که در یونانی oryza (در عربی: ارز) شده ... سمنانی ...' (Latin forms garbled in OCR).\"}\n\ne2_nodes=[\n {\"id\":1,\"lang\":\"Sanskrit\",\"words\":\"Vrihi\",\"verdict\":\"plausible\",\n  \"derivation\":\"Sanskrit vrīhí- 'rice' (Atharvaveda onward) is real and correct in meaning. But it is not inherited from a PIE root: it is a Wanderwort shared with Iranian (*wriHǰi-/*wrinǰi-) and probably borrowed from a South/Southeast Asian language (Proto-Dravidian *wariñci, or an Austroasiatic source per Witzel). As a node it is fine; the arrow from an 'Indo-European root' is not.\",\n  \"derivation_fa\":\"سنسکریت vrīhí- «برنج» (از اَتهَروَوِدا به بعد) واژه‌ای واقعی است، اما از ریشهٔ هندواروپایی نیامده؛ واژه‌ای سرگردان (Wanderwort) است که از زبانی جنوبی یا جنوب‌شرقیِ آسیا (دراویدی *wariñci یا آسترو‌آسیایی، به گفتهٔ ویتسل) وام گرفته شده. خود واژه درست است، ولی پیوند آن با ریشهٔ هندواروپایی پذیرفته نیست.\",\n  \"sources\":[W+'व्रीहि',W+'Reconstruction:Old_Persian/vrinjiš'],\n  \"ref_check\":[NOTCH(\"AHD:1116\",\"AHD 1975 main-dictionary page 1116 (s.v. rice) not available; the Watkins IE-roots appendix (AHD_watkins1985.txt) has no rice entry (grep 'rice|oryza' silent)\")],\n  \"consulted\":[SYNrice,KLNrice,{\"src\":\"POK\",\"where\":\"POK_full.txt grep 'vrīhi|oryza'\",\"stance\":\"silent\",\"note\":\"Pokorny has no root for 'rice' (no hits) — consistent with a non-IE loanword.\"},{\"src\":\"IEC\",\"where\":\"IEC.txt grep 'vrīh|oryz|rice'\",\"stance\":\"silent\",\"note\":\"no hit in the OCR text.\"}]},\n {\"id\":2,\"lang\":\"Avestan / Old Persian\",\"words\":\"brîzi, vriz, urvinj\",\"verdict\":\"plausible\",\n  \"derivation\":\"No word for rice is attested in Avestan or Old Persian; these are reconstructions. Modern reconstruction: Proto-Iranian *wrinǰi- (nasalised) beside *wriHǰi- (cf. Pashto wriže, OP *vrinjiš per Wiktionary/Hübschmann). Klein's 'OPers. brizi' and Horn's 'aw. *verenja-' are hypothetical forms; 'urvinj' matches no cited form (perhaps from Semnani varinj). The derivation from the Sanskrit node is also not a descent: Iranian and Indic share the loanword in parallel. Acceptable as 'Old Iranian reconstructed form', not as attested Avestan/OP.\",\n  \"derivation_fa\":\"در اوستایی و پارسی باستان واژه‌ای برای برنج گواهی نشده و این صورت‌ها بازسازی‌اند. پژوهش امروزی ایرانی باستان *wrinǰi- (با خیشومی) در کنار *wriHǰi- را بازسازی می‌کند (پشتو wriže؛ پارسی باستان *vrinjiš). «brizi» کلاین و «*verenja-» هرن فرضی‌اند و «urvinj» با هیچ منبعی نمی‌خواند (شاید از سمنانی varinj). وانگهی ایرانی آن را از سنسکریت نگرفته، بلکه هر دو شاخه این وام‌واژه را جداگانه دارند. با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+'Reconstruction:Old_Persian/vrinjiš',W+'ὄρυζα'],\n  \"ref_check\":[{\"ref\":\"KLN:1346\",\"status\":\"supports\",\"note\":\"KLN_1966.txt l. 32853 s.v. rice: '... fr. Gk. oryza, fr. OPers. brizi, fr. Afghan vrize, ult. fr. OI. vrihih' — the source of Nourai's 'brîzi'; Klein's form is hypothetical.\"}],\n  \"consulted\":[HUBrice,HRNrice,{\"src\":\"BRT\",\"where\":\"BRT.txt grep 'vrīz|vrinj|brinj'\",\"stance\":\"silent\",\"note\":\"Bartholomae has no Avestan word for rice.\"},{\"src\":\"KNT\",\"where\":\"KNT_full.txt grep 'vrinj|briz'\",\"stance\":\"silent\",\"note\":\"No Old Persian word for rice.\"}]},\n {\"id\":3,\"lang\":\"Persian\",\"words\":\"oroz; varîzeh; berenj 2\",\"verdict\":\"unverified\",\n  \"derivation\":\"berenj برنج 'rice' < MP brinj [blnc] < Proto-Iranian *wrinǰi- — confirmed (MacKenzie, Horn 208, Hübschmann 208, Mo'in). oroz/aroz اُرُز is not inherited Persian but a loan from Arabic أَرُزّ/رُزّ (aruzz, ruzz), itself < Aramaic ʾaruzzā < Greek óruza < Eastern Iranian — so it reaches the Iranian form only via a Greek/Aramaic/Arabic round-trip (plausible as cognate, wrong as direct descent). varîzeh وریزه 'rice' could not be found in Dehkhoda, Mo'in, Amid or Borhan (vajehyab/abadis give only an anatomical Arabic وریزه 'vessel from stomach to liver'); it looks like the Pashto wriže written in Persian script — unverified as a Persian word.\",\n  \"derivation_fa\":\"«برنج» از فارسی میانهٔ brinj و ایرانی باستان *wrinǰi- است و این بخش درست است (مکنزی، هرن، هوبشمان، معین). «اُرُز» واژهٔ موروثی فارسی نیست، بلکه معرّب است: عربی أَرُزّ/رُزّ از آرامی ʾaruzzā، از یونانی óruza و آن از یک زبان ایرانی شرقی؛ پس پیوند آن با صورت ایرانی از راه یونانی و آرامی و عربی است، نه مستقیم. «وریزه» به معنای برنج در دهخدا، معین، عمید و برهان یافت نشد و به نظر می‌رسد همان پشتوی wriže باشد؛ ادعای نورایی دربارهٔ آن تأیید نشد.\",\n  \"sources\":[W+'برنج',W+'رز','https://abadis.ir/fatofa/ارز/','https://abadis.ir/fatofa/وریزه/'],\n  \"ref_check\":[BQTrice,{\"ref\":\"MON:198,5014\",\"status\":\"not_checked\",\"note\":\"6-vol Mo'in print pages not accessible; local 2-vol abridgement (MON_part1.txt l. 9839-9846) has ارز only as 'ارزش' and '[ع. ارز] درخت سلیمان، نوعی عرعر، سرو' — no rice sense; وریزه absent (grep silent).\"},{\"ref\":\"IEC:1681\",\"status\":\"not_found\",\"note\":\"IEC.txt OCR ends in the u- section; no hit for 'urīĝh|vrīhi|oryza|rice' as headword.\"}],\n  \"consulted\":[{\"src\":\"PHD\",\"where\":\"p. 20 (PHD.txt l. 290)\",\"stance\":\"supports\",\"note\":\"'¹brinj [blnc | N birinj] rice.'\"},HRNrice,HUBrice,\n               {\"src\":\"MON\",\"where\":\"abadis.ir/fatofa/ارز (Dehkhoda/Amid sections)\",\"stance\":\"partial\",\"note\":\"Dehkhoda: '(ع اِ) اَرُزّ. رُزّ. برنج (یکی از حبوب)' — tagged Arabic; Amid: '= برنج'.\"},\n               {\"src\":\"FVQ\",\"where\":\"FVQ.txt/AFM.txt/AFA.txt grep 'aruzz|oryza'\",\"stance\":\"silent\",\"note\":\"no entry for Arabic aruzz.\"},\n               {\"src\":\"ARY\",\"where\":\"ARY_latin_index_pages.txt grep 'VRIHI|BRINJ|ORYZA'\",\"stance\":\"silent\",\"note\":\"Aryanpur has no entry for برنج — consistent with its not being an IE word.\"}]},\n {\"id\":4,\"lang\":\"Greek\",\"words\":\"oruza\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Ancient Greek ὄρυζα óruza 'rice' (first after Alexander's campaigns; Theophrastus, Megasthenes) is a borrowing from an Eastern Iranian (Bactrian-type) form of *wriHǰi- (cf. Pashto wriže), with prothetic o- and -uza rendering Iranian -iz-/-iž-. Mo'in, Klein, Horn and Wiktionary agree on the Iranian intermediary.\",\n  \"derivation_fa\":\"یونانی باستان ὄρυζα (óruza) «برنج» (از روزگار لشکرکشی اسکندر، نزد تئوفراستوس و مگاستنس) از یک زبان ایرانی شرقی (هم‌خانوادهٔ پشتو wriže) وام گرفته شده و o- آغازین در یونانی افزوده شده است. کلاین، هرن، معین و ویکی‌واژه این میانجیِ ایرانی را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n  \"sources\":[W+'ὄρυζα'],\n  \"ref_check\":[{\"ref\":\"SYN:519\",\"status\":\"partial\",\"note\":\"SYN.txt l. 13095 (§8.46, p. 519): '... of the word seen in Skt. vrīhi- (AV+), Afghan vrīzē, etc. Boisacq 712' — Buck links Gk. oryza to the Indo-Iranian word, but the OCR of his exact route is truncated.\"},NOTCH(\"AHD:1116\",\"AHD 1975 main dictionary p. 1116 not available\")],\n  \"consulted\":[KLNrice,HRNrice,{\"src\":\"BQT\",\"where\":\"leaf 485 (p. 265) footnote\",\"stance\":\"supports\",\"note\":\"'نام آن در سانسکریت vrīhi است که در یونانی oryza (در عربی: ارز) شده'.\"}]},\n {\"id\":5,\"lang\":\"Latin\",\"words\":\"oryza\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Latin oryza (Horace, Pliny) is a direct learned loan of Greek ὄρυζα; Vulgar Latin *orizum/*oriza.\",\n  \"derivation_fa\":\"لاتین oryza (نزد هوراس و پلینی) وام مستقیم از یونانی ὄρυζα است. ادعای نورایی درست است.\",\n  \"sources\":[W+'rice'],\n  \"ref_check\":[NOTCH(\"None\",\"node carries no reference\")],\n  \"consulted\":[{\"src\":\"KLN\",\"where\":\"l. 26645 s.v. Oryza\",\"stance\":\"supports\",\"note\":\"'Oryza ... L., ‘rice’, fr. Gk. oryza. See rice.'\"},KLNrice]},\n {\"id\":6,\"lang\":\"Italian\",\"words\":\"riso\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Italian riso (Old Italian riso/risi) < VL *orizum with aphaeresis of the initial unstressed o-.\",\n  \"derivation_fa\":\"ایتالیایی riso از لاتین عامیانه *orizum با افتادن o- آغازین بی‌تکیه پدید آمده است. ادعای نورایی درست است.\",\n  \"sources\":[W+'rice'],\n  \"ref_check\":[NOTCH(\"None\",\"node carries no reference\")],\n  \"consulted\":[KLNrice,{\"src\":\"LKT\",\"where\":\"LKT.txt grep 'riso'\",\"stance\":\"silent\",\"note\":\"not treated (non-Oriental intermediate).\"}]},\n {\"id\":7,\"lang\":\"French\",\"words\":\"ris, riz\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Old French ris (13th c.), Modern French riz, borrowed from Italian riso (rice reached France via Italian trade).\",\n  \"derivation_fa\":\"فرانسوی کهن ris (سدهٔ سیزدهم) و فرانسوی نو riz از ایتالیایی riso وام گرفته شده‌اند. ادعای نورایی درست است.\",\n  \"sources\":[W+'rice'],\n  \"ref_check\":[NOTCH(\"None\",\"node carries no reference\")],\n  \"consulted\":[KLNrice,{\"src\":\"SKT\",\"where\":\"SKT.txt grep 'Rice'\",\"stance\":\"silent\",\"note\":\"headword not located in OCR.\"}]},\n {\"id\":8,\"lang\":\"English\",\"words\":\"rice\",\"verdict\":\"confirmed\",\n  \"derivation\":\"English rice < ME rys, ris (13th c.) < Old French ris.\",\n  \"derivation_fa\":\"انگلیسی rice از انگلیسی میانه rys/ris و فرانسوی کهن ris است. ادعای نورایی درست است.\",\n  \"sources\":[W+'rice'],\n  \"ref_check\":[NOTCH(\"AHD:1116\",\"AHD 1975 main-dictionary page not available; content matches Klein s.v. rice\")],\n  \"consulted\":[KLNrice,{\"src\":\"SYN\",\"where\":\"§8.46 p. 519\",\"stance\":\"partial\",\"note\":\"Buck lists the European rice words as loans from Gk./Lat. oryza.\"}]},\n]\n\nout={\"pdf_page\":520,\"book_page\":490,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-16\",\"entries\":[\n {\"entry\":0,\"root\":\"Upo\",\"verdict\":\"confirmed\",\n  \"modern_form\":\"PIE *upo 'under, up from under' (Pokorny 1106) with comparative *uper(i) 'over' (Pokorny 1105)\",\n  \"note\":\"Pokorny 1106 upo 'unter, von unten an etwas heran' and AHD upo 'under, up from under, over'; Klein *upo 'from below; turning upward'. Root, label and gloss correct. Whole chart sound; only blemish is the misprinted Latin pre-form 's-upper-mo' (#9, book error, should be *sup-mos) and the uncertain French intermediary for Persian سوپر (#6-#7, Amid tags it English).\",\n  \"note_fa\":\"ریشهٔ هندواروپایی آغازین *upo «زیر، از زیر به بالا» (پوکورنی ۱۱۰۶؛ کلاین: «از پایین، رو به بالا») و صورت تفضیلی آن *uper «بر، بالای» (پوکورنی ۱۱۰۵) درست‌اند. شاخه‌های اوستایی upairi، پهلوی abar و فارسی «ابر» و «بر»، لاتین super، یونانی hyper و ژرمنی *uberi همه تأیید می‌شوند. تنها ایراد، صورت چاپیِ نادرست «s-upper-mo» به جای *sup-mos (خطای چاپی کتاب) و تردید در میانجی‌گری فرانسوی برای «سوپر» است. ادعای نورایی درست است.\",\n  \"sources\":[UPER],\n  \"ref_check\":[{\"ref\":\"POK:1106\",\"status\":\"supports\",\"note\":\"POK_full.txt l. 88197 ff.: 'Root / lemma: upo, up, eup, (e)up-s-; Meaning: under, from under, etc.; Note: from the meaning \\\"from under hinauf\\\" die meaning \\\"hinauf, über\\\" ... esp. in related *uper(i)'; Page(s): 1106-1107.\"},\n               {\"ref\":\"KLN:1105\",\"status\":\"supports\",\"note\":\"KLN_1966.txt l. 26789 s.v. over: '*uper, *uperi ... prop. comparative of *upo, ‘from below; turning upward, upward; up, over, beyond’'.\"}],\n  \"consulted\":[{\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. upo (l. 1106)\",\"stance\":\"supports\",\"note\":\"'upo. Under, up from under, over. 1. Germanic *upp-, up ...'.\"},\n               {\"src\":\"WLD\",\"where\":\"Bd. I p. 192 (uper) \",\"stance\":\"supports\",\"note\":\"WLD treats uper(i) beside upo; Latin super, superus listed.\"},\n               {\"src\":\"SKT\",\"where\":\"s.v. Over\",\"stance\":\"supports\",\"note\":\"'comparative form from Aryan UPA (Skt. upa, near, on, under; Gk. ὑπό, L. s-ub)'.\"}],\n  \"nodes\":e0_nodes},\n {\"entry\":2,\"root\":\"Urigh\",\"verdict\":\"disputed\",\n  \"modern_form\":\"No PIE root. Indo-Iranian Wanderwort: Skt. vrīhí-, Proto-Iranian *wriHǰi-/*wrinǰi-, probably from a South Asian (Dravidian *wariñci or Austroasiatic) source\",\n  \"note\":\"Mann (IEC 1681) posits an IE 'urīĝh-' for rice, but Pokorny, Walde-Pokorny, Watkins and Buck have no such root, and modern scholarship (Mayrhofer EWAia, Witzel; Wiktionary) treats Skt. vrīhí- and Iranian *wrinǰi- as a non-IE loanword shared in parallel by Indic and Iranian; Mo'in (BQT 265) likewise says the plant and name came to Iran from India. The individual chains are largely right (Iranian → Greek óruza → Latin → Italian → French → English rice; MP brinj → NP berenj), but: the Iranian forms are not attested Avestan/OP (#2); اُرُز is an Arabic loan (via Aramaic/Greek), not a direct descendant (#3); varîzeh is unattested as Persian (#3).\",\n  \"note_fa\":\"برای «برنج» ریشهٔ هندواروپایی وجود ندارد. تنها مان (IEC) ریشهٔ *urīĝh- را پیشنهاد کرده، ولی پوکورنی، والده‑پوکورنی، واتکینز و باک چنین ریشه‌ای ندارند و پژوهش امروزی (مایرهوفر، ویتسل، ویکی‌واژه) سنسکریت vrīhí و ایرانی *wrinǰi- را واژه‌ای سرگردان می‌داند که از زبانی دراویدی یا آسترو‌آسیایی وارد هندوایرانی شده است؛ معین نیز در حاشیهٔ برهان می‌گوید این گیاه از هند به ایران آمده. زنجیرهٔ یونانی ← لاتین ← ایتالیایی ← فرانسوی ← انگلیسی و پهلوی brinj ← «برنج» درست است، ولی «اُرُز» معرّب است و «وریزه» در فارسی یافت نشد. ادعای هندواروپایی بودن ریشه را پژوهش امروزی رد می‌کند.\",\n  \"sources\":[W+'व्रीहि',W+'rice',W+'Reconstruction:Old_Persian/vrinjiš'],\n  \"ref_check\":[{\"ref\":\"IEC:1681\",\"status\":\"not_found\",\"note\":\"IEC.txt OCR covers the u- section only up to ~p. 1554 (ulquos); page 1681 (addenda) not in the local text; grep 'urīĝh|urigh|vrīh|oryz' silent.\"}],\n  \"consulted\":[{\"src\":\"POK\",\"where\":\"POK_full.txt grep 'vrīhi|oryza|Reis'\",\"stance\":\"contradicts\",\"note\":\"no root for rice in Pokorny — implicitly not IE.\"},\n               {\"src\":\"WLD\",\"where\":\"WLD_Bd1/2 grep 'vrīhi|oryza'\",\"stance\":\"silent\",\"note\":\"no entry.\"},\n               {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt grep 'rice|oryza'\",\"stance\":\"silent\",\"note\":\"no IE root for rice in Watkins' appendix.\"},\n               SYNrice,KLNrice,\n               {\"src\":\"BQT\",\"where\":\"leaf 485 (p. 265)\",\"stance\":\"contradicts\",\"note\":\"Mo'in: 'شک نیست که این گیاه از سرزمین هند به ایران رسیده' — loan, not inherited.\"}],\n  \"nodes\":e2_nodes}\n]}\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-520.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)\nPYEOF\ncd /home/sfmqrb/git/rishe-private && python3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-520.py && python3 -m json.tool data/verification/page-520.json >/dev/null && python3 tools/verify_check.py 520"
}
```


### [2026-10-16T05:20:41.888Z] TOOL RESULT

```
nodes verified: 22/22
node verdicts: {'confirmed': 16, 'plausible': 4, 'transcription_suspect': 1, 'unverified': 1}
root verdicts: {'confirmed': 1, 'disputed': 1}
ref checks: {'supports': 14, 'not_checked': 11, 'partial': 2, 'not_found': 1}
books consulted: {'supports': 51, 'silent': 11, 'partial': 6} | by book: {'KLN': 15, 'SKT': 9, 'AHD': 5, 'POK': 5, 'WLD': 4, 'ARY': 4, 'HRN': 4, 'PHD': 3, 'HUB': 3, 'MON': 3, 'IEC': 2, 'BRT': 2, 'KNT': 2, 'SYN': 2, 'NYB': 1, 'LAT': 1, 'FVQ': 1, 'BQT': 1, 'LKT': 1}
```


## [2026-10-16T05:20:51.429Z] TOOL CALL #60: SubagentHandback

```json
{
 "message": "I verified page 520 (book page 490) and wrote `/home/sfmqrb/git/rishe-private/data/verification/page-520.json`. It passes `python3 -m json.tool`, and `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 520` shows 0 PROBLEM lines, with all 22 nodes verified.\n\n**Verdict counts**\n- **Roots:** 1 confirmed (Upo), 1 disputed (Urigh). The Urdu entry is a redirect and was skipped.\n- **Nodes:** 16 confirmed, 4 plausible, 1 transcription_suspect, 1 unverified.\n\n**Disputed**\n- **Root Urigh \"rice\":** this is not an Indo-European root. Only Mann (IEC) proposes one. Pokorny, Walde-Pokorny, Watkins and Buck have no such root. Modern sources (Mayrhofer, Witzel, Wiktionary) treat Sanskrit vrīhí- and Iranian *wrinǰi- as a borrowed word of probably Dravidian or Austroasiatic origin. Mo'in's note in Borhan p. 265 also says rice came to Iran from India. The chain from Iranian to Greek óruza and on to English \"rice\" is correct.\n\n**Transcription_suspect**\n- **Upo #9, Latin \"s-upper-mo\":** the book itself prints \"s-upper-mo\"; the JSON copies it faithfully. It is Nourai's misprint for *sup-mos (< PIE *(s)up-mo-), the form Klein, Pokorny and Watkins give. I copied the page image to `data/verification/sources/refs/ocr/BOOK/520.png`.\n\n**Other weak points**\n- **Urigh #3, Persian (unverified):** berenj is confirmed (Middle Persian brinj). oroz/aroz is a loan from Arabic aruzz, which came via Aramaic and Greek, so it is not a direct Persian descendant. I could not find varîzeh meaning \"rice\" in Dehkhoda, Mo'in, Amid or Borhan; it looks like Pashto wriže written in Persian script.\n- **Urigh #2 (plausible):** brîzi, vriz and urvinj are reconstructions, not attested Avestan or Old Persian words.\n- **Upo #6–#7, French route for Persian سوپر (plausible):** Amid tags سوپر as English, and سوپرمارکت is the English word \"supermarket\", so the French step is uncertain.\n\n**Extraction errors for you to fix:** none. The JSON matches the printed page throughout."
}
```


### [2026-10-16T05:20:51.710Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
