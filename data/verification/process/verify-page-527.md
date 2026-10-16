# Verification process log — verify-page-527


## [2026-10-16T05:13:01.755Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 527 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-527.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-527.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-527.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 527` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:01.835Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:06.248Z] TOOL CALL #1: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md; echo ====; cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-527.txt; echo ====; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-527.json"
}
```


### [2026-10-16T05:13:06.984Z] TOOL RESULT

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


## [2026-10-16T05:13:09.291Z] TOOL CALL #2: Bash

```json
{
 "command": "sed -n '/SAVE what you/,/Wiktionary\\*\\* (en.wiktionary/p' /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


## [2026-10-16T05:13:10.126Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-527.txt; echo; echo =====; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-527.json | head -c 6000"
}
```


### [2026-10-16T05:13:10.426Z] TOOL RESULT

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


### [2026-10-16T05:13:10.496Z] TOOL RESULT

```
Exit code 1
=== PDF page 527 (book page 497) ===
--- entry 0 ---
ROOT [Indo-European] Webh : to weave  (refs POK:1114)
#1 (parent #0) [Avestan] refs=POK:1114 | ubdaena : woven fabric
  #2 (parent #1) [Persian] refs=HRN:38; BQT:2461; MON:1462; POK:1114; OEW:424 | bâftan «بافتن» : to weave | extra: بافته ، باف ، بافندگی
#3 (parent #0) [Germanic] refs=AHD | weban, wefta, wabila
  #4 (parent #3) [English] refs=KLN; OEW:425 | weave, web, wave 1, Webster, wafer, woof, wobble
#5 (parent #0) [Indo-European] refs=AHD:1550; POK:1179; KLN:1731; OEW:425 | Wopsâ : insects with web-shaped nests, wasps
  #6 (parent #5) [Iranian] refs=POK:1179 | vawža : wasp
    #7 (parent #6) [Avestan] refs=POK:1179 | vawžaka : scorpion
      #8 (parent #7) [Pahlavi] refs=POK:1179 | vassz : wasp
  #9 (parent #5) [Germanic] refs=KLN:1731; OEW:425 | wafsa, wosp : wasp
    #10 (parent #9) [English] refs=KLN:1731 | wasp
  #11 (parent #5) [Latin] refs=KLN:1731; OEW:425 | vepsa, vespa : "weaver" insect, wasp
    #12 (parent #11) [English] refs=KLN:1731 | vespiary
--- entry 1 ---
ROOT [Indo-European] Wed, Wer 4, Aŭe 2, Ud 2 : water, wet  (refs POK:78; AHD:1547,1549; KLN:1732)  PART 1
#1 (parent #0) [Avestan] refs=POK:78; KLN:1682 | vâr 1, wâr, vâra 1 : rain
  #2 (parent #1) [Pahlavi] refs=BQT:218; AEF:209 | vârân, vârîtan
    #3 (parent #2) [Persian] refs=BQT:218; AEF:209 | bârân «باران» : rain ; bârgîn «بارگین» : pond, storage of rain water | extra: بارش ، باریدن ، بارندگی / پارگین
#4 (parent #0) [Avestan] refs=POK:78 | udra : otter, water bird
  #5 (parent #4) [Pahlavi] refs=HRN:242 | vartak 2 : a water bird
    #6 (parent #5) [Persian] refs=MON:5001; BQT:2262 | vardîj «وردیج» : a water bird | extra: ودخین
#7 (parent #0) [Avestan] refs=POK:78 | aoda : fountain ; vaidi : water way ; vairi : sea ; varašnî : testicles
#8 (parent #0) [Old High German] refs=AHD | wazzar : water
  #9 (parent #8) [French] refs=None | vaseline : moisturizing oil
    #10 (parent #9) [Persian] refs=MON:4944 | vâzelîn «وازلین» : Vaseline
  #11 (parent #8) [English] refs=None | Vaseline

(eval):1: ==== not found
```


## [2026-10-16T05:13:14.110Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/extracted/batch/page-527.json'));print(json.dumps(d,ensure_ascii=False)[:5000])\"; echo; cat data/verification/sources/SOURCE_MATRIX.md | head -80; ls data/verification/sources/refs/ | head -100; cat tools/verify_check.py | head -150"
}
```


### [2026-10-16T05:13:14.524Z] TOOL RESULT

```
{"pdf_page": 527, "book_page": 497, "entries": [{"root": {"name": "Webh", "lang": "Indo-European", "refs": "POK:1114", "gloss": "to weave"}, "nodes": [{"id": 1, "parent": 0, "lang": "Avestan", "refs": "POK:1114", "words": [{"translit": "ubdaena", "gloss": "woven fabric", "script": null}], "note": null, "quote": null}, {"id": 2, "parent": 1, "lang": "Persian", "refs": "HRN:38; BQT:2461; MON:1462; POK:1114; OEW:424", "words": [{"translit": "bâftan", "gloss": "to weave", "script": "بافتن"}], "script_extra": "بافته ، باف ، بافندگی", "note": null, "quote": {"text": "بافته با محبّتم ، رشتهٔ تار و پود جان - تار بتار، نخ بنخ، رشته برشته، پو بپو", "poet": "Raf'at Semnânî"}}, {"id": 3, "parent": 0, "lang": "Germanic", "refs": "AHD", "words": [{"translit": "weban, wefta, wabila", "gloss": null, "script": null}], "note": null, "quote": null}, {"id": 4, "parent": 3, "lang": "English", "refs": "KLN; OEW:425", "words": [{"translit": "weave, web, wave 1, Webster, wafer, woof, wobble", "gloss": null, "script": null}], "note": null, "quote": null}, {"id": 5, "parent": 0, "lang": "Indo-European", "refs": "AHD:1550; POK:1179; KLN:1731; OEW:425", "words": [{"translit": "Wopsâ", "gloss": "insects with web-shaped nests, wasps", "script": null}], "note": null, "quote": null}, {"id": 6, "parent": 5, "lang": "Iranian", "refs": "POK:1179", "words": [{"translit": "vawža", "gloss": "wasp", "script": null}], "note": null, "quote": null}, {"id": 7, "parent": 6, "lang": "Avestan", "refs": "POK:1179", "words": [{"translit": "vawžaka", "gloss": "scorpion", "script": null}], "note": null, "quote": null}, {"id": 8, "parent": 7, "lang": "Pahlavi", "refs": "POK:1179", "words": [{"translit": "vassz", "gloss": "wasp", "script": null}], "note": null, "quote": null}, {"id": 9, "parent": 5, "lang": "Germanic", "refs": "KLN:1731; OEW:425", "words": [{"translit": "wafsa, wosp", "gloss": "wasp", "script": null}], "note": null, "quote": null}, {"id": 10, "parent": 9, "lang": "English", "refs": "KLN:1731", "words": [{"translit": "wasp", "gloss": null, "script": null}], "note": null, "quote": null}, {"id": 11, "parent": 5, "lang": "Latin", "refs": "KLN:1731; OEW:425", "words": [{"translit": "vepsa, vespa", "gloss": "\"weaver\" insect, wasp", "script": null}], "note": null, "quote": null}, {"id": 12, "parent": 11, "lang": "English", "refs": "KLN:1731", "words": [{"translit": "vespiary", "gloss": null, "script": null}], "note": null, "quote": null}]}, {"root": {"name": "Wed, Wer 4, Aŭe 2, Ud 2", "lang": "Indo-European", "refs": "POK:78; AHD:1547,1549; KLN:1732", "gloss": "water, wet"}, "part": 1, "nodes": [{"id": 1, "parent": 0, "lang": "Avestan", "refs": "POK:78; KLN:1682", "words": [{"translit": "vâr 1, wâr, vâra 1", "gloss": "rain", "script": null}], "note": null, "quote": null}, {"id": 2, "parent": 1, "lang": "Pahlavi", "refs": "BQT:218; AEF:209", "words": [{"translit": "vârân, vârîtan", "gloss": null, "script": null}], "note": null, "quote": null}, {"id": 3, "parent": 2, "lang": "Persian", "refs": "BQT:218; AEF:209", "words": [{"translit": "bârân", "gloss": "rain", "script": "باران"}, {"translit": "bârgîn", "gloss": "pond, storage of rain water", "script": "بارگین"}], "script_extra": "بارش ، باریدن ، بارندگی / پارگین", "note": null, "quote": {"text": "خویشتن هم جنس خاقانی شمارند از سخن - پارگین را ابر نیسانی شناسند از سخا", "poet": "Khâqânî"}}, {"id": 4, "parent": 0, "lang": "Avestan", "refs": "POK:78", "words": [{"translit": "udra", "gloss": "otter, water bird", "script": null}], "note": null, "quote": null}, {"id": 5, "parent": 4, "lang": "Pahlavi", "refs": "HRN:242", "words": [{"translit": "vartak 2", "gloss": "a water bird", "script": null}], "note": null, "quote": null}, {"id": 6, "parent": 5, "lang": "Persian", "refs": "MON:5001; BQT:2262", "words": [{"translit": "vardîj", "gloss": "a water bird", "script": "وردیج"}], "script_extra": "ودخین", "note": null, "quote": null}, {"id": 7, "parent": 0, "lang": "Avestan", "refs": "POK:78", "words": [{"translit": "aoda", "gloss": "fountain", "script": null}, {"translit": "vaidi", "gloss": "water way", "script": null}, {"translit": "vairi", "gloss": "sea", "script": null}, {"translit": "varašnî", "gloss": "testicles", "script": null}], "note": null, "quote": null}, {"id": 8, "parent": 0, "lang": "Old High German", "refs": "AHD", "words": [{"translit": "wazzar", "gloss": "water", "script": null}], "note": null, "quote": null}, {"id": 9, "parent": 8, "lang": "French", "refs": null, "words": [{"translit": "vaseline", "gloss": "moisturizing oil", "script": null}], "note": null, "quote": null}, {"id": 10, "parent": 9, "lang": "Persian", "refs": "MON:4944", "words": [{"translit": "vâzelîn", "gloss": "Vaseline", "script": "وازلین"}], "note": null, "quote": null}, {"id": 11, "parent": 8, "lang": "English", "refs": null, "words": [{"translit": "Vaseline", "gloss": null, "script": null}], "note": null, "quote": null}]}]}

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


## [2026-10-16T05:13:19.956Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/527.jpg; python3 -c \"\nimport json;d=json.load(open('data/verification/page-526.json'));print(json.dumps(d['entries'][0]['nodes'][0],ensure_ascii=False,indent=1)[:3000])\" 2>/dev/null || ls data/verification/ | tail -5; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','BQT','MON','OEW','AHD','KLN','AEF']: print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\""
}
```


### [2026-10-16T05:13:20.553Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   86k sfmqrb 14 Oct 22:15  site/pages/527.jpg
.rw-r--r--   40k sfmqrb 14 Oct 22:50  page-514.json
.rw-r--r--   22k sfmqrb 14 Oct 22:47  page-515.json
.rw-r--r--   36k sfmqrb 14 Oct 22:51  page-516.json
.rw-r--r--   32k sfmqrb 14 Oct 22:48  page-517.json
.rw-r--r--   20k sfmqrb 14 Oct 22:48  page-518.json
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 34
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view", "identifier": "originsofenglish00jose (also originsofenglish0000ship)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending (djvu.txt returns 401/403). Entries are 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org,
```


## [2026-10-16T05:13:24.910Z] TOOL CALL #6: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/527.jpg"
}
```


### [2026-10-16T05:13:24.937Z] TOOL RESULT

```

```


## [2026-10-16T05:13:26.745Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-518.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:2500]);print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3500])\"; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','BQT','KLN']: print(k, d[k].get('page_offset'), d[k].get('lookup_hint','')[:500])\""
}
```


### [2026-10-16T05:13:27.169Z] TOOL RESULT

```
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
   "note": "'Pers. begam, a queen, lady of rank; lit. 'mother of the governor.' — Turk
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
POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?bas
HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf imag
KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
```


## [2026-10-16T05:13:32.125Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -A40 'lemma: webh-' POK_full.txt | head -70; echo -----; grep -n -A30 'lemma: wobhsā\\|lemma: u̯obhsā\\|lemma: wops' POK_full.txt | head -45"
}
```


### [2026-10-16T05:13:32.658Z] TOOL RESULT

```
-----
```


## [2026-10-16T05:13:34.649Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'lemma:' POK_full.txt | grep -i 'ebh\\|obhs\\|ops\\|ed-\\|ōd' | head -30"
}
```


### [2026-10-16T05:13:34.952Z] TOOL RESULT

```
1681:Root / lemma: ad-1{*hed-) 
1743:Root/ lemma: au(e)-9, aued-, auer-\ "to flow, to wet; water, etc' 
3840:Root/ lemma: au(e)-9, aued-, auer-\ "to flow, to wet; water, etc' 
6032:/pbh-(A?-): < with /-formant {n^'^eli): < Root/ lemma: {en^^-2)\ /7ebh-, errio'^-, /pb^-: " wet, 
6181:/ lemma: ped-2, p6d-\ (foot, *genitalia). 
7699:lemma: au(e)-9, aued-, auer-\ "to flow, to wet; water, etc.'. 
7998:Root / lemma: au(e)-9, aued-, auer- {*h2ahiue > aue-) 
8503:Root / lemma: au-6, aued- 
9661:band- {* bhend-): "drop' derived from a zero grade of Root/ lemma: au(e)-9, aued-, auer- 
9803:Root / lemma: bed- 
10959:Root / lemma: b^ebh/i/- b^eb'^ro- 
10985:lemma: bed-: to swell?]. 
14540:Root / lemma: b^/ed- b\ld- 
20727:immovable; solid, etc' derived the extended root Root/ lemma: d^erebh-: "to harden' 
24071:Root / lemma: ed- {*hegh-) 
24077:From an older root {*hegh-) derived Root/ lemma: ed- {* hegh-): "to eat, *tooth' and Root/ 
27358:Root / lemma: ered- {* ere-danos) 
32488:Root / lemma: ghed- 
32679:Root / lemma: gheled- 
32877:Root / lemma: ghencf- and ghed- 
34465:Root / lemma: gred- : grod- 
41024:Root / lemma:7ebh- 
44482:Root / lemma: ked- 
48059:Root / lemma: kopso- 
48220:Root / lemma: kred- 
48228:Root / lemma: kred- : beams, roof, derived from a suffixed Root / lemma: kra[u]- : kreu- : 
49432:Root / lemma: Rad- : Redes- : Red-s- 
50280:Root/ lemma: {Rered-.) Rerd-, Rerd-, Rfd-, ^/©(y- (nasalized PIE 
51882:Root / lemma: Rred- 
53129:Root / lemma: Iced- k^od-i^k^ehutt-)
```


## [2026-10-16T05:13:37.012Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'Page(s): *1114\\|Page(s): *1179\\|Page(s): *78\\b\\|Page(s): *1113\\|Page(s): *78-' POK_full.txt | head"
}
```


### [2026-10-16T05:13:37.303Z] TOOL RESULT

```
8299:Page(s): 78-81 
88456:Page(s): 1113-1114 
88655:Page(s):1113 
88678:Page(s):1113 
88697:Page(s):1113 
88736:Page(s):1114 
88771:Page(s): 1114-1115 
90185:Page(s):1114 
90757:Page(s):1114 
90765:Page(s):1114
```


## [2026-10-16T05:13:39.250Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '88736,88800p' POK_full.txt; echo; grep -n 'ubdae\\|vawz\\|vawža\\|wobhs\\|obhsa\\|webh-' POK_full.txt | head -30"
}
```


### [2026-10-16T05:13:39.565Z] TOOL RESULT

```
Page(s):1114 

Root / lemma: udcl^-2 

Meaning: to wander, roam, swarm 

Material: Middle High German weben^v(\QNQ, swing', weberen^ €\c\\ tummein', webelen 

'waver'. Modern High German East Prussian wibbeln; Middle High German waben, 

waberen, wabe/en^\n unsteter Bewegung sein', wappen'h\n and her schwanken'. Modern 

High German (Low German) M/5i6'i6'e//ig'wackelnd, e.g. from Gallertigem', Old English 

waf/an {esp. with handum) 'sich bewegen'. Middle English waveren, engl. M/ai/e/''wobble, 

waver'. Old Icelandic i/a/7a 'wobble, sway', vafra^s\dc\ unstet hin and back bewegen, 

wabern' (i/5/Wo^'Waberlohe'), vefjast6s.\ 

Old Icelandic i/a/^'schweben, dangle'. Old English wsefre^uusiei, flackernd'; 

Lithuanian vebzd-u, -e//"wimmeln, sich verwirren, durcheinander bewegen'; 

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


88707:Germanic *ue-, above S. 75); Avestan ubdaena- Irom Webstoff, from Zeug gemacht' 
93162:Material: Avestan vawza/<a- 'scorpion', but Iran. Vawza- 'wasp' in Middle Persian va^z
```


## [2026-10-16T05:13:41.274Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '88680,88735p' POK_full.txt; echo ====; sed -n '93150,93185p' POK_full.txt"
}
```


### [2026-10-16T05:13:41.557Z] TOOL RESULT

```
Exit code 1
Root / lemma: uat-2 
Meaning: to bend, curve 

Material: Latin vatax, -ac/is "krumme orschiefe Fijfte habend', Ka//Z/5'einwartsgebogen, 
crooked', vatia^ someone with crooked Beinen', vascus {*vat-scos) "quer, slant, skew'; 
Germanic *wat^wan-^ curvature, bend', then with engerer meaning "calf, knee-bend ': Old 
Icelandic vgdvivn. 'Muskein, esp. thick Muskein an Armen and Beinen', a/?- i/pdi//' biceps', 
Norwegian vodve^ thick Muskein an arm and leg' etc.. Old High German wadoxr\. 'sura, 
suffrage'. Middle High German wade 'calf, alts, uuathan' suras ', mndd. wade'caW, 
Middle Dutch wadei. " knee-bend, popliteus '; 

Connection with Latin varus'apart gebogen, auswartsgehend, dachsbeinig' etc. (root 
*ua-) is probably. 

Maybe alb. var'hang' 

References: WP. I 216, WH. II 736 f. 
Page(s):1113 

Root / lemma: udol^-l 

Meaning: to weave, plait 

Material: Old Indie ubhnati, umbhati, unabdhi' schuuxi together', with apa- and pra- "binds', 

urna-vabh/'-m. " spider' (actually Wollweber); newer -i/ait*/?/- after va- "to weave' (Indo 

Germanic *ue-, above S. 75); Avestan ubdaena- Irom Webstoff, from Zeug gemacht' 

(from a lyMa-"Gewebtes', Indo Germanic *ub'^-td-)] np. bafad'er webt'; 

gr. ucpn "the weaving ', ucpowai n 105, otherwise ucpaivu) " weave ', ucpot; n. "the weaving 
' (after denvorigen from *Ft(poq unvocalized); 

alb. venj'\ weave ' {*ueb^n/d); 



Old High German weban' to \Neas/e, flax, wattle, braid, spinnen'. Old English wefan'to 
weave, flax, wattle, braid, tie, bind, knot ', Old Icelandic vefa'to weave, flax, wattle, braid, 
schlingen' (participle of/nn), ve^'a{*ucb'^e/d) "wickein, wrap' = Old English webbian^io 
weave'; Old Icelandic veptr. Old English weft, wift, i4/e/?a'Einschlagfaden', Middle High 
German ty/// 'fine filament, texture;Honigwabe'; Old Icelandic vaf diaper', vaft 
"entanglement, Unordnung'; Old High German waba, n/^it'o'Honigwabe', Old Icelandici/e/^ 
i^wabja-) " texture, Aufzug, gewobenes Zeug' = Old English webb. Old Saxon webbi. Old 
High German weppi6s.\ Old High German wuppr texture ', Swedish c>^(Old Icelandic 
*yfr) "Einschlag'; 

©-grade Old Icelandic kongurvafa. Old English gangelwaefre^ spider'; 

Tocharian B n/ap- 'to weave', wapatsa^ weaver', wpelme^ texture '. 

References: WP. I 257, Mayrhofer 1, 107; 

See also: belongs to au-S^io weave' S. 75; in addition "i/ob^sa 'wasp'. 

(eval):1: === not found
```


## [2026-10-16T05:13:44.413Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '93145,93185p' POK_full.txt; echo ---; sed -n '8280,8300p' POK_full.txt; sed -n '7998,8080p' POK_full.txt | grep -n -i 'aoda\\|vaidi\\|vairi\\|var\\|udra\\|ub\\|Avest' "
}
```


### [2026-10-16T05:13:44.979Z] TOOL RESULT

```
Latin Ko/pes'fox', possibly also /upus'\No\V; 

Lithuanian /ape{*u/ope), Latvian /ap55 (syncopated from /apesa?\ndo Germanic 
*u/opeR^)\ compare Lithuanian v//p/sys^ wild cat ', it would be placed near Middle Persian 
gurpa/<u^ers. gurba^ house cat, domestic cat ', from Iran. *urpa-, Indo Germanic *u/pos, it 
concerns certainly various taboo adjustments. 

References: WP. I 316 f., WH. I 836 f., II 830, Frisk 83, Trautmann 149, Specht Indo 

Germanic Dekl. 36, Liden KZ. 56, 212 ff. 

Page(s):1179 

Root/ lemma: udo'^sa {* haudo^sS) 

Meaning: wasp 

Material: Avestan vawza/<a- 'scorpion', but Iran. Vawza- 'wasp' in Middle Persian va^z 

'wasp', Baluchi gwabz^\>ee, wasp'; 

Maybe Danish gedehams : Swedish get/ng : French guepe : Furlan ghespe : Breton 

gwespedenn: Welsh gwenynen feirch : Napulitano vespera: Reggiano vrespa: Venetian 

brespa; vrespa; vespa : Albanian apocope {*gres-pa) Geg greth, grenza, Tosc grereza 

'wasp'. 

Latin vespa i. 'wasp' (from *vopsa)\ 

acorn. guhi-en<^\. 'wasp', mcymr. gw(y)ch/, abr. guoh/<^\. fucos{*uops-), from which 
borrowed Old Irish foich<^\. 'wasp' (also ' caterpillar, cankerworm '), nir. fot/achav\6 pu/th 
'wasp', out of it spoch^ fierce attack' (O'Rahilly Sc. G. stem 3, 63); 



Old English wsefs, weeps, w^sp^vjasp', Old High German wefsa, wafsa, waspa, 
Bavarian webes, thijr. weps-chen an6 wewetz-chen, those in Germanic indicate *wabi-s 
and *wabi-t, 

---

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

39:mash boiled in milk ', Avestan {* h2auod-)ao5a- m. ' wellspring, fount '. 
43:Old Indie {* h2aunatti-)unatti {*u-n-ed-ti), 3. PI. undatr soaked, moistened '; Avestan 
44:vaidi-t " water run, irrigation canal '. 
47:m)\ from /'-stem derived samudra-h' sea ', anudra-h^ waterless ' (= gr. avu5po(;); 
49:{*h2audro-)udro-s^ water animal ': Old Indie udra-h^ a water animal ' = Avestan udra- m. 
51:Lithuanian udra, Old Chureh Slavic vydra ds.);
```


## [2026-10-16T05:13:48.487Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '8030,8075p;8160,8285p' POK_full.txt | grep -n -i -B1 -A1 'avest\\|persian\\|vair\\|var' | head -80"
}
```


### [2026-10-16T05:13:49.081Z] TOOL RESULT

```
6-Old Indie odatr the soaking, the flowing ', odman-n. " the waves, floods ', oda-na-m' 
7:mash boiled in milk ', Avestan {* h2auod-)ao5a- m. ' wellspring, fount '. 
8-
--
10-
11:Old Indie {* h2aunatti-)unatti {*u-n-ed-ti), 3. PI. undatr soaked, moistened '; Avestan 
12-vaidi-t " water run, irrigation canal '. 
--
16-
17:{*h2audro-)udro-s^ water animal ': Old Indie udra-h^ a water animal ' = Avestan udra- m. 
18-" otter ' (= gr. u5po(;. Old High German ete ottar, compare also Latin /utra and with u 
--
66-
67:1. uer-, uer-:0\6 Indie var, variu. "water', Avestan varu. "rain' (with themat. inflection 
68:Iran. Avestan var^ to rain ', med. " allow to rain, let rain '), Old Indie vani. "water', Avestan 
69:vairi-xw. "sea'; 
70-
--
129-
130:in FIN: Italian A^e/-5^ms (Bruttium), P/s5i//ic/s(Umbrien), gall. Avara> French Avre, Aura 
131-> French Eure, Aurana> Modern High German 0/7/77(Wurttemb.), Ar-auris> French 
--
143-whirlpools ', atvyrs^ counterstream on the shore ', Latvian verdu, vFrC soak, bubble, boil, 
144:cook ', atvars " whirl ', 
145-
--
149-" wellspring (bubbling water) ', wherefore with from " cook ' developed meaning " heat ', 
150:Latvian wersme " glow ', Old Church Slavic varb " heat '. 
151-
--
153-
154:4. extension {*h2auers-) uer-s-' rain, dew ': Old Indie varsa-n. " rain, rainy season, year 
155:' {varsat/" it is raining '), gr. oupov ' urine '; span, ttpor\ " dew ', Ionian Attic oupsu) " 
156-urinates ' (kausativ *uorseid, F- proved by the augmentation Eoupnoa), oupia " a water bird 
--
162-
163:Maybe alb. {*varsa-) vesa^6eW : {*heverse) sspari ' dew'. 
164-
--
167-
168:thereof derived Avestan 1/3/^5/73- 'virile'. Old Indie vrsa-, vrsabha-'buW, i/Zs/?/- 'virile', m. 
169:"Aries, ram' (= Avestan varasni-6s.), vrsana-m. ' testicles '; 
170-
```


## [2026-10-16T05:13:55.281Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==264' HRN.txt | head -80; echo ====; grep -n -i 'bâftan\\|baftan\\|bāftan\\|bâfad\\|bāfad' HRN.txt | head; grep -n -i 'bârân\\|bārān\\|baran ' HRN.txt | head"
}
```


### [2026-10-16T05:13:55.579Z] TOOL RESULT

```
Exit code 1
— 242 —
1078. vevd/kj 'Wachtel', rerdej, verflj, vertek.
ai. varfikä' ^WachteF; phlv. oartak (Papyrus, Hörn,
ZDMG. 43, 50); gr. oorvh
kurd. verdl, //arnfrr?^ 'Wachtel' (H.-Sch.); af/. vvaraz\
ORS. LW. (?) rärdcä; bei. f/vardäf/ Gebirgsrebhiihn' ;
WSL/. VOlc.
1079. verseng 'würdig, achtbar (unbelegt).
ap. onn(7(iyyrjC' of &vf(jyiTa( tov ßnöi'krjo^^ noorrdyyai
y.ah'ovrai nfgtöri (Herod. VII, 85), de Lagarde, Ges.
Abb. 191.
Die Grundbedeutung wird 'gewichtig sein (vei'gl.
se7ig, No. 747); rer -- ap. vpar'nj also wer, wie in
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
wesen der Beamte, Mer auf einem Kriegsschiffe für alles sorgen muss,
was zum Wasserproviant gehört*, s. F. Boooh-Arkossy, Spanisch-
Deutsches Handwörterbuch^ s. v.J degradirt, vergl. Dozy -Engel-
mann, Glossaire des mots espagnols et portugais d6riv^s de Parabe*,
S. 129.
*) Nur in einem AbuM Ma*änl- Verse.
(eval):1: === not found
```


## [2026-10-16T05:14:00.927Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==60' HRN.txt | grep -n -i -A8 'bäft\\|baft\\|bäf\\|ubd' | head -40; echo ===; grep -n -i 'bärän\\|bäran\\|baran\\b\\|bärldan\\|bärtdan' HRN.txt | head"
}
```


### [2026-10-16T05:14:01.426Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-10-16T05:14:04.356Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 58 59 60; do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | head -3; done; grep -n -i 'ubda\\|bäftan\\|bäften\\|weben' HRN.txt | head; echo '---'; grep -n -i 'Regen' HRN.txt | head"
}
```


### [2026-10-16T05:14:04.882Z] TOOL RESULT

```
— 86 —
arm. patrinc (de Lagarde, No. 1848: patriny)
gehört kaum hierher.
— 37 —
reiter, aw. ayare.hara- *Tagesritt' ^) ; phlv. barak, päz.
här Reittier (Men.).
Die Praeposition findet sich nur in der jüd.-pers.
/ Bibelübersetzung.
1466. bäzär 'Markt', bazargan, hazergän Kaufmann'.
1844:\;i68. haften 'weben', baf, n^ND 'Garbe' (Jer. 9, 21).
1859:aty. üdal, ödal 'weben ; oss. vafpi (75) ; bei. gvapag,
14517:ubdafna- 168.
---
1013:haur *Regen* (163).
1767:159. bärän *Regen', bartden regnen', baris, bärgln,
1769:aw. vara- 'Regen', varenti Venu es regnet' (Barth o-
5019:558. dnrüne 'Regenbogen'.
5021:bei. drm, drmuk 'Regenbogen* (85); yidg. LW.
6993:wo es mit menis verbunden ist und 'Übelkeit erregen
9529:np. hemä mit der Bedeutung *Platzregen* hat VuUers s. v. bereits
9755:deutung *die Aufregung, das Wogen' bezw. *auf regen',
10290:54. candTnltan 'erregen (AV.).
10292:Np. nur in |T*3!i *die Flügel regen' (Is. 10. 14),
```


## [2026-10-16T05:14:07.518Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '1840,1865p;1762,1780p' HRN.txt; grep -n -c '' HRN.txt; awk 'BEGIN{RS=\"\\f\"} {n++} /168\\. haften/ {print \"leaf\",n-1; exit}' HRN.txt;  awk 'BEGIN{RS=\"\\f\"} /159\\. bärän/ {print \"leaf\",NR-1; exit}' HRN.txt"
}
```


### [2026-10-16T05:14:07.921Z] TOOL RESULT

```
skr. vära- 'Mal'; phlv. bär.
158. {s)bär in Comp. Jöi[bäry derya\bär, röd[bar, Zeng[bar,
Hindü[bär,
o. t aw. para- 'Ufer, Rand'; phlv. -bär, z. B. röt[bar
(Bund.); ai. pard- *üfer.
159. bärän *Regen', bartden regnen', baris, bärgln,
g. he-väre 'es regnet'; mäz. väris; Käs. vörün etc.
aw. vara- 'Regen', varenti Venu es regnet' (Barth o-
lomae, Indog. Forsch. I, 178); phlv. varan, värUan,
varimtan (PV.), väranUan (Bund.); ai. vdr- 'Wasser.
kurd. baritty bari^ barän (LW.), baris (LW. ?) varin
(H. -Seh.); af/. varyaj 'Wolke*, varyaz, var-edal
Vegnen'; oss. d. warun^ t. vdrin (73); bei. gväris^
gvaray (147) ; wa;^. vür ; sar. variij^ varisa,
160. l\)bäre 'Pferd', baregl (Sahn. I, 21 Vers 27).
\ ap. aw. [^bar- Veiten', vergl. ap. assa]bara'^) Pferde-
M Ein ganz anderes Wort ist natürlich np. hädffere *Windfaehe,
Hlasebalff' (Sahn. I, 105 Vers 798, dazu Rückert, ZDMG. 8, 316 und
318), Vullers s. v. hädfer, 2.
'Armlänge, Elle'? Dann würde np. yüz 'Elle' (vergl.
sestyazt kernend. Sahn. I, 59 Vers 474) wohl nur auf
falscher Punktation beruhen und phlv. väz (AV.)
müsste für bäz stehen.
\;i68. haften 'weben', baf, n^ND 'Garbe' (Jer. 9, 21).
g. vaftmün.
Nach Bezzenberger bei Fick, Vergl. Wörtbch.*, I, 326
'Gemeindeweide', zu ai. sabhä- *Sippe*, das auch schon Darmesteter)
^t. ir. II, 131 in abä gesacht und wogegen Bartholomae, Litbl. f.
or. PhiL I, 19 sich ausgesprochen hatte.
Bartholomae schlägt mir brieflich für ap. ahäcuris die folgende
Etymologie vor: a(m)häcari8 d. i. a(m)ha'\-äcaris'^ zu ambhas' oder
*ahhas- vergL Geldner, KZ. 28, 186, zu äcan's vergl. ai. öXrard-,
demnach würde aCmJbäcaris 'Wasserwerk, Brunnen* bedeuten.
«) Vergl. Hörn, KZ. 32, 582 No. 8.
') Vis und RSmIn S. 82 Vers 10 steht bäz als 'Spanne' (ein Grab
von 60 Spanneu).- ^^9 —
aw. uhdaena- 'gewebt*; skr. vergl. ürna^vdbhi^
'Spinne* ^).
aty. üdal, ödal 'weben ; oss. vafpi (75) ; bei. gvapag,
n. ^vafay (134); wa;^. vufam, sar. väfam.
Arische (bezw. indogermanische) Doppelformen vaph-
und vahh-, vergl. Bartholomae, ZDMG. 44, 552,
Hübschmann, ib. 557.
' 169. bäy *6arten*.
Wohl aw. bäga- Xoos' (y. 51, 1); ai. hhägd- 'Teil,
23314
leaf 57
```


## [2026-10-16T05:14:11.901Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for p in 'ubdae' 'vawzak\\|vauzak\\|vawžak\\|wawzak' 'aoda-\\|aoba-\\|aoδa' 'vaidi\\|vaiöi\\|vaiSi' 'vairi-' 'varasni\\|varesni\\|varəšni\\|varsni' 'udra-'; do echo \"## $p\"; grep -n -i \"$p\" BRT.txt | head -6; done"
}
```


### [2026-10-16T05:14:12.503Z] TOOL RESULT

```
## ubdae
8456:•  j.  ubdaena-  Adj.  (fem.  °nT-)  'aus  Web- stoff, Zeug':  vastrim  .  .  'tarn  va  Tzaimm Tv7  V.S.a^;  — yesi  avAat  izaätt/  (sd.)  .  . yesi  a»hat  -tfU  V.  7. 14  f.
## vawzak\|vauzak\|vawžak\|wawzak
22439:•  j.  vawzaka-  m.  Name  eines  ^aAÜchen Tiers:  yas)  %wä  nSit  aiwiMrushnti  aiisla (sd)  ariknaim  'käiÜca  (als  Subj.)  Yt 5,90.
## aoda-\|aoba-\|aoδa
8292:•  j.  upaoba-  n.  'Sichbeschäftigen  mit  —' (Gen.):  humaya  "rthi  (AP.)  climoide  aku- nahe  vairyehe  .  .  hävanaySsca  .  .  arsuxia- namca  vacam  Y.  27.7;  Vr. /2.2.
8308:•  j.  upa.mraoda- Adj. '(etwa)  der  Wollust, den  Huren  ergeben,  Hurenjäger':  äat  *ag!e ydi  fracarmti  .  .  gaosUj/ca  (sd.)  . ,  'dss'a
9048:•  j.  kaoba-  m,  Name  eines  Lands*':  upa dvarnn  xsairö.sukjm  (sd.)  apanöJtmjm 'hitva  *birizantaya  asavanaya  "bei  dem Pass  -Vj^,  dem  liöchstgelegenen  in  dem hochragenden  heiligen  K."  Yt5.  54.
16555:•  j.,  g.  baod-  'sentire'.  Praes.  2  ba<k baoda-,  sj  bÜilya-,  3o(Kau5.)  bao^aya-. PPfP.  'busta-'K
18210:■  j.  frl'yaoda-  m.  EN.  eines  Gläubigen: ;  'oaAg  karsnayanaAe  asaonff  Yt  jj.  108. Eig.  'der   vom   im  Kampf  ist,   vpifiaipt'.  — "yaiia-  m.,  inm  ^.  yaed-;  vi.  yadhä-  m. \.Jriyal^i&'  Yl,  /j.  108;    lies /rflnya/.r".
24946:•  j.  raoda-  ni.  i)  'Wachstum'  (nurl Komp.).  2)Plur.  'das  äussere  Ansehen': kairiTnS  .  .  panladasayä  'oaesva  "eines Mädchens  .  .  von  fünfzehn  Jahren  nach dem  äussern  .Ansehen"  H.a.  9; — pan^a- dasa  (ND.)  fra^ardvie ..-'Mlsva  kaiarasHt Y.O.S,
## vaidi\|vaiöi\|vaiSi
2476:—  inVerbindung  mit  x^'aFpat^j'a-.  Aaxaji5 Im  einem  Satz,  der  einem  vorhergehenden ..  kudaena  naiuaUt  mPiö.ao]anhd  (sd.)  Relativsatz  inhaltlich  koordinirt  ist '*': /ru- aesqm  sfaSfaHya  hizvöXt.ig.^^.  2)  auf.  zaiiUlmca  .  .  ytri/id  pourBsca  b»r3jayan ein  Relativum  als  dessen  Korrelat;  a)  ad- 1  nagciica  aiAka  yasäiti  zyänsi  (sd)  Y.  65. jektivisch  (vgl  i  aa) ;  yi  ätnm  . .  ava.-  11;  —  dämSH  urvalsl  .  .  yahmi  sp>ntä baraiti  . .  cvat  ahmäi  natre  mTsd»m  anhat  ^wil  mainyS  urvaisi  jasö  (sd.)  mazdä V.cV.81.  a)  Das  adjekt  Pron.  vertritt  |  :e/flir,7  oAmJ  W:4ä  »H7«aw,4fl  "bei  welchem laL  eius,  eorum  (s.  i  a  a):  yö  mam  .  ,  Ende  du  mit  .  .,  o  M.,  mit  XL,  bei  dem zinät  nöil  ahmi  nmäne  *z3naile  a^rava..'  du  mit  VM.  kommen  wirst"  Y.  4J.6{.;  — aal  ahmi  nmäne  .  .  "wer  .  .,  in  dessen  s.  noch  ahmya  3.  3)  Das  Neutr.  oder Hause  .  .,  sondern  in  seinem  Haus  , ."  Fem.  Sing,  bezieht  sich  substantivisch  auf Y. //.5f.;  —  mit  Numeruswechsel  "> :  _>'ö..  den  Inhalt  eines  Satzes,  bes.  Vordersatzes haom»nvandaita..frä..abyötanubyökaom5  (s.  Z  4);  a)  GSn. 'dess'  sva.  'dafür':  yatba- visäite  (sd)  baliazäi  "quilibet . .  laudat, . .  ■  väni  aiwi.sasto  .  .  eis  atiihe  asti  baSsazö eorum  corporibus  . ."  Y.  jo.  8.  b)  sub-  (sd.)  Yt7.^34;  —  AS  mim  ava>a  vjrj- stantivisch:  yi  maibyä  yaol  ahmäi  asSlt\nüiti  ya^a  ..  Sl  ait?he  asti  uzvar?z)m (sd.)   vahista  .  .    cöiüm  Y.  46.18;  19;  — j  (sd)  V-iS-^^f.;  37,  57,  68';  —  d:7tü  hi
4140:Anfang  des  Lebens"  Y.40.2;  —  Ayat] %zti3  'K>ASu/ ta'^si  äarfSfm  (s±)  paourvlm Y- 43- 5i  —  apifmi  °t3k>us  urvaisi  (sd.) Y.JJ,6;  4s. y,  —  datu  'nksus  aridat .  . Aai^yävarstam  (sd.)  Y.50, 11;  —  'nhus yä  tu  vsis/ä  {sd.)  vaAisia  Y.  46.10;  — vaifh^s  dazds(,sA.)  manavAB ^yao%ananqm 'ahsus  ..  Y.  27.13;  J/.8;  — yäcä  .  .  ux^öä /rait  (sd.)  .  .  yilal  'tifisus  .  .  Y.44.S;  — yä  banaypn  (sd.)  'hUin  matytuns  Y.  30. 6.  a)  von  der  Gesammtheit  der  Leben- digen 'Menschheit,  Weie  (s.ll  A  I  a  o): upa  .  ,  avavat  sätsis  (sd.)  *isai/i  yäi^a vlspmt    imat   yat  juyS    'uhul    H.  2.  z ;
4869:•  ).  ayan-,  j-,  g.  ayar-  n.  'Tag';  a) Gegensatz  zur  Nacht:  *oim  . .  'yar>  (NS.) tYjasaiti  .  .  a?va  v3  xsapa  Aog.  J/;  ■ — ai»ke  'yan  (GS.)  .  .  airikh  xsaj>ö  \t.  i .-iZ, i/.S;  Vyt.J0(?);  —  hamahe  °yqn  hamayn 1-3  xsa/w  Y.  S7-3I,  Yt.ÄS4;  '  10.  iij  (f), Vyt^f?);  —  vlspsU  'yqnia  (AP.)  xlaf- nas.'a  Y.  57. 1 7,  Yl  /.  i  i  ;  —  *frayaire  "yan (LS.)  bavaiti  (sd.j  hubai,rü  .  .  aia  apare 'y<pi  ■-  Aog.  35;  —  */rayarfne  vä  uza- yariu^fsd.)  va  *'yan''>  N.5;  —  dvadasati- hiinm  (sd.)  asü  *ayrim  °yar)  F.  27  b 27b;  —  °yqn  (LS.)  va  varstafsö  var»t3.vTrt [sd.)JaiJnti  V.S.^.  b)  als  der  Zeitraum von  Sonnenaufgang  zu  Sonnenaufgang: iiz£.a  yan  mainyenie yaty3r)N.2.^\ ^räyö  yara''  Vd.  ly;  <),  if),  si;  —  pasca xsavaidim  (sd.)  yaranqm^a'''  Vd.  f)\  11, '5>  '9  '■  c)  sva.  festgesetzter,  bestimmter Tag:  myazdahe  ''ya''''  (LS.)  "am  Tag  des My:'  N. Si-,  "y:;  *^jj  —  kaia  (sd.)  yiri (AP.)  daxiärS  .  .  drfs  Y.  43-  T,  —  yan ami^näitii&d.)  juye  tanus  Aog.^j.  d) 'Zeit':  vUpI  'yärj  (AP.)  dangö.jyäiöU (sd.)  .  .  "alle  Tage  . ."  Y.  43-  2.
5855:•  g.  'a-spä-  n.  'Unglück,  Leid':  ySt vanhSus  vaidinä  (sd.)  manatthiS  sSnghaS raSxma  °spsn^l  (AP.)"  sadräcU  caxrayS (sd.)  tuMro  Y.34.T,  — yJn7  usJn  (sd.) &r;>i  sp7nlä  'spJnla.  (AP.)"'  Y.^ij.g.
10826:und  bfisem  Reden  euch,  die  Dalva,  was er  den  ZVi^fgenossen "  gelehrt  hat,   um (den  Menschen)  zu  verderben"  Y._j2.s. Za  ü.  V.  i^naA' 'er  Tcrnichtet',  gr.^SiV»;  vgl. *S^;  Bthl.  ZDMC.  50.  711,  —  Pü,!    tt/rär SSel  i  ciSn  Ah  hai  H  i  drvand pätixiähih  "der sie   lehrt,   die  Herrschaft   stsmmc  von   dem I>r".  —   >)  Der  Irrlehrer,   Ton  dem  auch  Y. 32.  6   die  Rede  ist;    s.  noch  No.  2.     Dafür, dass  das  erste  Sabjekt  nicht  ausdrQcklich  be- zeichnet ist,  vgl.  Sp.  5<36  0.  und  die  RV.-Slellen g]-häm  indraica  gacehatam,  a  yäd  ruhava  vänt- nasea  navam  (n.  a. ;  *.  Hask£i,L  JAOS.  ii.  66), die  insofern  der  obigen  ähneln.  —  ')  E»  ist ein  bestimmter,  der  neuen  Lehre  feindlicher Fürst  gemeint;  vgl.  drigvant-  I  a  a  0. j.  xsavaiditn  Vd.  p:  s.  xit/id-  mit  Na.  4. j.  xlm/as:  lies  xivaS.
12816:atyä  (sd.)  Ayat  maiäqm  dvaidi  (iDftM.)"
## vairi-
6301:KoiDpA.,  E.  —  Vgl.  aJävairi-,  —  ai.  vgt flavan-  Adj.  —  Pü.:  ahrav"'};  SB.!  fa^yälmä, muklälmä,  muklimin-,  £.  noch  No.  ^.  —  ■)  Mit ä  nnr  in  aiävaoyö  DP.  (Vt  J.  4t  'S-  88)  und im  VS.  aiJ««  (SJOJ.7);  s-  noch  <üäv^r: ■>  Die  Hds.  schwanken  zwischen  aiaen' aiäjiH'.  Die  Gründe  für  die  Wahl  der  Lesung in  der  NA.  sind  mir  öfters  nicht  erkennbar. Im  Y.  habe  ich  mich  meist  nach  Pt4  gerichtet, iB.  gegen  NA,:  Y.ja.  11,  33.  1,  43-0,  IS  uö. S.  übrigem  auch  S  ^68.  33.  —  J>  Im  Gegen- satz in  dip/.arila:  —  4)  Die  attrib.  Bestim- mang  eines  Nomens  durch  asavan-  und  aiaii rata.--  m.  iat  ungemein  häufig.  Dabei  erscheint hinler  femininem  und  neutralem  Nomen mehrere  Male  die  mask.  Form  von  aiavan-, in  Anschlns»  an  das  folgende  ralav-:  V.  7/. 12',  Vr.  /.  5,  G.  4-  8;  V.  7/.  23,  Vr.  /.  4, 2.  6;  s.  Ho.  5.  —  i>  Mask-,  weil  auf  ta%-a'qni belogen,  1.  N0.4.  —  *)  Hds.  airaiaf';  s.  aber Pa.  —  J)  Als  Vok.i  aber  Pü.:  ahräilA.  — O  Vgl.  u/ajraoUr-*}.  Pü.  hat  den  Flur.  — 91  Streri,  —  '•')  Gleichklang  der  Auslaute!  — ">  Die  Verwendung  von  alavanä  als  N-APn. {\'r.  7.  4,  7p.  I,  Vr.  S.  33)  kann  durch  den Zniammenfall  des  NPm.,  APni.  und  APn.  bei der  d-DeklinatioD  hervorgerufen  sein;  s.  Vt. 8. 33.  —  '")  Das  ein  allir.  *arla^an-  voraas- seilt,  *gl.  Hbu.  FSt.  195.  Dagegen  führt mp.  artäk,  ahrät^fÜ)  (mit  ä  aus  äud)  itii'artäffan- ; iD  i-äl  i  artäk  des  Gl.,  worauf  JirSTI  NB.  33 Terweist,  s.  valahe  aSaenä  unter  I  Z.
21238:'modalen  Formen:  yaT  adaif  (sd.)  asa *drujim  vSngAaitT  Ay  ('so  dass')  '^qsasuia (sd.)  ya  ..Y.4S.\;  —  ka%a  iBt  gavBi ratul  hy  ('auf  dass')  AJm  data  xsayatttS (sd.)  %waxsB  Y.  25.  2;  —  a  *m3yastra.- barattä  (Sp.  1190  u.)  ,  ,  Ay  ('auf  dass') ^<iärJ(sd.)  mana  bava/Y.30.^; 32.i6(f); —  vax^a  vS . ,  Ay  ('damit')  d/ih^ng  (sd.) vicayaha  ad^qs^ä  Y,  46.  15;  —  asaonl rafonS  RySm  .  .  Ay  ('auf  dass')  *a  *basils (sd.)  .  .  dya  Y.43.S;  —  tat  ai  vairi- maidl  .  .  Ay  ('damit")  r  mainimadila  .  . ^■35- 3-  b)  im  jAw.;  i)  mit  Ind.:  tä Ai  taurvayatam  tba^a  .  .  y  ('so  dass') ^it  apB  takäis  stayat  Yt  y .  7  8 ;  —  x^anns .  .  yat  uparaAacat  AaoiyanApm  .  .  y  x/a- yata  .  .  dasvanqm  ma^anqmca  ".  .  so dass  er  herrschte  über  .  ."  Yt  ig.  26; 28f.3,  13,  79,  84,  Y.().4;  —  saya  ava%a staxrB  y  ha  druxl  oHti  tnfnzvT  .  .  FrW. 8.  2  (?).  a)  die  Antwort  auf  eine  Frage mit  ^anl'  einleitend  (s.  2  a,  3):  ^Ivata  (sd.) na  *mtima  vaca  gdha  sravayS  ratu/riil y  Ai  nasdiSiB  daAmH  aiwi.srunvai/i  ", .  so, dass  ihn . .  verstehen  kann"  N.  27.  a)  mit Konj.  (oder  Inj,):  y  ('damit')  yavB  (sd.) pouruS  bavät  oBa  mq%r3m  *tat  mairyai V._j.  32f.;  —  :farm3..yai  upawAaiat sao^antqm  Vfr^rajaram  .  .  y  hrmavai frasim  aAüm  ,  .  ". .  auf  dass  er  die Menschheit  neu  gestalte"  Yt/9.88f.;  11, 8.  I,  V.  ig.  23;  —  neben  ya%a'.  Jrsit  mB tat  nqma  /ramrUiti  .  .  ya%a  (Sp.  1 246 u.)  azsm  taurvayetti  . .  y  ('auf  dass')  mqtn nasHS  taurvayät  Yt.  i.  6;  —  th  mazdi zbayal  avanAe  .  .  y  ('damit')  spmtB mainyul  vfharayat  asmatum  y  ap)m y*  .  .  YLy.28;  —  mä  buyama  sSihrB,- iricö  ,  .  m^a  (sd.)  y  ('damit')  nS  uyra.- bäzaus  nivanai  (sd.)  Ytjo.  75;  —  kana 'hwqm  yasna  yazäne  .. yasp*^  ('auf  dass') tava  mazdi  kinnaot  tacara  .  .  yasi^^ ('damit')  äwa  nöit  aiwi.druiante  .  .  Yt 5. 90.  a)  wie  I  a:  h/at  aiwyätsAayanttl yat  aliqm  *3r)dvaya  (sd.)  . .  *v3r»^antqm ndit  avanrasayai  (sd.)  N.  85.  3)  mit Opt.;  wie  I  a:  cvantö  ata  Am  alle  kata  ..l ■  .  y°  Al  nsit  >r)dv5.hr3han3m  (sd.)  vayta- n»m  upa.janyatY .^.\\.  4)  dasVerbum i^aA')  ist  weggelassen:  spanim  nida%?m y  dim  mazaos  (sd.)  ksArpB  tarahe  V.  13. 39.  V)    einen   Inhaltssatz    einleitend
22796:von  Yima  auf  AAuras  Befehl  errichteten  D'e  Lesung  isi  nicht  recht  sicher.  Das  zweite Baus«:  Jat  t»m  -rptn  k?r?nava  ^ar^tu.-  "  »H'" falls  anaptykusch. drajS  ktmät  paiti  ca%rulanqm  V.  2.  2  5 '; '  •  j.  'varay-  :  vairi-  m.  'See**;  Bucht  einer 33*;  —  aat  mqsta  yimS  Aüia  tg  azim  Sc^':  airyö.iayamm  ..yaAmyajaJra'rayS.. 'rwt  ksrgnavane yä  ml aoxta  ahurS  mazdä  Yt.  10.  14;  —  bune  jafranqm  •iryanqm'^ V.2.31;  —   apifa  t>m  'r>m  manza  dva- ^t.  ir).  ^i,    V.  jp.  42;     —     'iflÜS    (AP.)
24423:•  j.  vispa.taurvairi-  f.  'Allüberwinderin',  j Beiname     der    3'ridat.f^rT  (sd.):     -to/yi,
## varasni\|varesni\|varəšni\|varsni
3563:j.  afa.varSni  V.  22.  6:    lies    cipai'arätie;    s.
23094:•  j,  varsni-haräta-  Adj.  '(admissuram habens,  d.  i.)  wofür  die  Zulassung  dei Widder,  der  Widdersprung  bezeichnend ist',  toa  Ayä^rima- (^sA.):  ayohrimtm  fra- ourvalltriimm  'tim  Y.  2. 9;  —  ayä%ri- m3i  .  .  °taica  Y.i.g;  —  aya^rimahe  .  . 'lahe^a  Vr.  /,  2.
## udra-
8215:•  j.  udra-  m,  'Otter,  Fischotter':  'rahe avaynänB  kaicö  k?r>naoifi  V.  y .  5 1 ;  — yat , .  altahe  °rahe  upa  dakmiiii  urvätum fräyaZi'titc.'W.  13.$$;  —  sonst  mit  upapa- Adj. :  y5  'nm  jainti  yim  upap?m  V.  ;  J,  i ;
8229:Eig.  'Ottetberg',  AbleiL  aus  udra-,  oder  'der Bei^  am,  im  Wasser',  Ableit  aus  idg.  'udir- (s.  unter  udra^.
10859:xäudra-
10863:•  j.  xSudra-,  xSuSra-''  i)  Adj.  'flüssig':, vTs/ia  tarsuca  (sd.)  'draca  A.J.  12,  Yt.ip. 58,    P.  42.  3)    n.    'Flüssigkeit';    uzw.
10869:KompE.,  A.(?)9.  —  PPfP.  einer  Basis  (ar.) *ksaud-,  woiu  noch  xsaoiah-,  xsudra-,  pm- xia0itra-%  s.  Hdm.  ZDMG.  38.  43i-  —  !'"■ (lu  F.,  Y.):  ^imxt,  (iu  V.);  /,«r.  -  ')  Unthom.; zSchr.  s.  IF.  //.  137.  NA.  xiivisli.  —  ")  S. noch  '^hilasmc.  —  3)  VgL  intay').  —  4)  Hds. hisf.  —  SS.  No.  2.
15636:•  j.  pairiS&x&udra-,  •xtiutra-  Adj.  'dem der  Same  versiegt  isf;  narS  °'hrS..jafdka paraMaxsta  Yt  i"].  54;  —  yat  hatiS  vä taurtirö  v3  'drS  vS  bavSt  V._y.  19;  — yat  sam/  paraJrüyäH  *naäa.sjmanasca 'dras^  V,  ij.  50.
```


## [2026-10-16T05:14:16.430Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '•  j.  ao[bSöd5]a-\\|j\\.  vai[bSöd5]i-\\|j\\.  v[aä]r[ae]-  \\|j\\.  v[aä]r-  \\|Regen' BRT.txt | head -20"
}
```


### [2026-10-16T05:14:16.888Z] TOOL RESULT

```
2937:•  j.  aoSa-  m.  'Quelle"',  nur  in  upa  'liailu raahaya  (sd.)  "an  der  Quelle  der  R": yatäl  ahi  upa  'laf^u  ranhayh  . .  upa sanaie{sd.)  ratahaya  Yt  J2.  i8£  a)  als Name  eines  Landes*':  x^asJasam  asav- hqmHa  ..  frä^w^rmm  ..  upa  '%al^  raa- hayä  yö  asarB  (sd.)  atwyaxiayänti  " . .  schuf ich  (das  Land)   UAR. . ."  V./.19.
2985:•  j.  aoöa-  I)  Adj.'vcrderbhch  (nurAbleiL  ■  ^„^^,>^^  ^ä„„^-  Yt/J.131;- /^«/•«.- —  2)   m.   'Verderben,  Untergang,  Tod':  firö  ya->a  'rd  hz  2
4000:•  j.  awra-  n.  i)  'Regenwolke,  Wolke': yaha  'nm  vätsJsism  Y,(?.32;  —  'ra upapä  Yt  74.41;  —  'm  F.7.  2)  "Regeii, Regenschauer':  ma?ya  .  .  yähva  urväi/is (sd.)  'r&  Yt.Ä40.
4001:KompE.   —    ai.  aikrä-   n.  'Wolke';    np,  abt •Wolke',  afy.  erif  'Wolke',  baJ.  haur  'Regen'.
7279:charakterisirenden  Adj.  (sd.,  auch  fdSt.): vispasca  äpS  yazamaide  ya  z)m3  armaesta (sd.)  *fratat.ear3tasca  (sd.)  *xqnyk  '^raots.- stälasca  par^uya  *v3iryäsca  (sd.)  "alle Wasser  auf  der  Erde  . , :  die  stehenden  und fliessenden,  die  in  Quellen  und  in  Fluss- laufen,  die  Schnee-  und  Regenwasser"  Y. 61^.6;  usw.;  —  vJspä  apd  xä  pttiti '^raotS.- stSiasca  Y.yi.g;  —  sps yal  armal^tayä.. yat  cätayä  uzuityäsca  .  .  yat  sna^ntyaica srasUntyaica  . . yat ß^tat.^antayä'W .  6.^0, 33i  36,  39;  —  äpim*  tacintqm  . .  xayanqm .  .  zrayanqm  .  .  artmaistqm  Yt.6.2;  Y.ig. 26,  Vd.4;  —  caval  nä  apa  (statt  DS.) ''frälat.cartte  .  .  paiti.iaräi  .  .  cval .  .  ape armaisfaya  (statt  DSf.)  .  .  nävayayai  tia ape  ..  ti.66(.;  —  apqm  ..  nävayaiiqm (sd.)  paiti  pintüs  Yt  //.  4 ;  usw.;  —  andvim . .  ye^he  avavat  .  .  äps  lata  (sd.)  ava.- barmle ya%ia  ..  Yt.5.15;  Ä.47; — gairil yS  uiiiä  yim  aiwiid  paoiris  äpS  hqm  gairi- ü(/('(sd.)/(WJ«/JYL/9.66; — spim  laokmta' vaitim  zaranyävaitlm  vihusavaifim  (sd.) V.^.54;  —  ap3mca  haomyqm  {sA.)  Y.  22. 2;  usw.;  — yaSsyatitim  äp^m  *pararihät Y.g.ii;F.4 f.,  V.21;  —  ?iqm.taptibyB  aiwyS caxrare(sii.)  n^r^bydY.  4.46; — apU  ai yaza- maide malkaintllcä  (sd.)  * hsbavaintlicä  . . Y.JÄ3«.  C)  GP.  apqm  mit  napat-m. (sd.,  auch  fdSt.)  Name  einer  Gottheit: apqm  napäs?  tä  apff  ..  vliax/aiti  YtS. $4; usw.  2)  von  bestimmten  Flüssen  oder Seen,  'Gewässer':  andvl  (sd.)  nqrna  äpa (NS.)"'  V.  7. 16;  —  n?mS  artduya  aps  anü- hitaya  Yt  r.  2 1 ;  Y.  6$.  i ,  Ny.  4.  o.  Vr.  1. 5 ; —  *atikäs^a  (näml.  artduyä)  mS *aaatiAä aps  apayiarsY .  65.  i;  5;  —  upa  äp.'myqm vltaaukaittm  Yt5,76;  —  njinB  ape  däit- yayä  (sd.)  Yt./.2i;  5.112,  5,29,  /7.61, V, ig.2;  —  aoi  apjm  yqm  raiakqm  (sd.) Yt.5. 63;  —  haca  apat  kqsaeyät  (sd.)  Yt ig.92,  V.ig.$;  —  a/s  ya  aw^änva  nqma Yt  ig.  62;  —  yazäi  äp^m  frazdänaom  F. 4%.  I,  2  Anhang:  apqm  (näml  ayar^y
11905:•  j.  tatäp-  Adj.  'fallende  Wasser  habend', sva.  'der  den  Regen  fallen  lässt':  sata- %ais5  .  .  'äpa  (NS.)">  zavarm.srats  'äfS (NS.)''  ux^at.urvarS  Yt.  7^,44;  43"';  — tnihrsm  .  .  frat.ap)m  zavanlS.srBt>m  •ap?m uxryat.urvar»n  Yt  10. 6 1  "*,
12166:Y.  rftf,  9";  —  %wei  OS  *ärmaitis  ^icJ  ar  gemeint  ist  das  Regenwasser,  aqua  caele-
12269:♦)  7:,  dem  Yt.  8  gewidmet  ist,  gilt  als  Gegner der  Patriki  (Meteore;  s.  zu  kmma-)  und  be- sonders de»  ^/uffÄi  (sd.),  nach  dessen  Besiegong und  Verlreibung  (Yt.  8.  22  ff.)  er  den  erquicken- den Regen  spendet  (Vt  8.  30  ff.,  Bd.  9.  z\  In Su.  zu  Y.  I.  II,  Ny.  /.  S  wird  er  darum  als vj-ftinakiotram,  in  Npü.  zu  Ny.  /.  8  als  man^t i  batan  bezeichnet.  Mi.  4g.  5  heisst  er  der  erste der  Sterne.  Bd.  2.  7,  $.  i  der  Anführer  des  öst- lichen Fiislemhimmels  und  spezieller  Gegner des  Planeten  T!r  (Merkur);  s.  noch  Dd.  oi.  iff und  die  von  Blocket  RHR.  33.  loj  u.  (=  4, Zeile  3  ff.  des  autographirten  Teiles)  mitgeteille Slelle  des  GrBd.   Vgl.  Gor.  OK.  308)  316,  318.»
14854:Ä8.  a)  mit  Abi.  'aus  -':  paourva.-  daliß&z\ia  Art  'herangehen  zu-';  a)  mit namat patai  dyaoHf^A.)  .  .  anrö  mainyus  -qxl.:  hamaka  airyabyU  daiAhubyB  hatna Yt. j.  iz;—ptat  (3SPrA.) F.  10.  3) ^oia ,  f^apatänti")  Yt  S.  61.  b)  m\tpaiH und Wasser;  a)  'herabfallen,  -strömen',  vom  j  Akk,;  s.  a/rapatai  Int Regenwasser:  s.-V««/-(in/«/.3A).  b)'über-  mit  z^r(z'(/)  in  rfo^Hscher  Art 'weg-,  fort- fliessen',vomsiedendenWasser(?):><W««/a  l,gn,.  ^fj- ^pam  Ha patmiu  vi  dalvhM (sd.)  patmla  F.  4  f.  4)  Term.  techn.  für  %j  ^  g  yf /o.  i . dasGehen  rfjftTschcr  Wesen:  hamySila  ..\  mit,ia«'fallen,hinabstürzen in-'(Akk.): davqi>ya  patqi^yä  Y.g.  18;  —  vagn^mn^  \  ^ru/asianam(sd.)  haMpataiti{T&m\.daevd) (sd.)  anmat  para  dalva  patayin  Yt  ig.  80; '  V  70  4.1    '  *
16491:•  j.  baevarfl.vär-  m.,  Flur,  'zehntausend Regentropfen'(?):^(i>'i»'<i  äunma ..upa.apjm Aazanrö.varayö (sd.)  -värascii (NP.)  V. 21.%.
23486:•  j.  'vir-  m.  1)  'Regen':  staomi  marjimca 'r^mta  ya  ti  (näml.  haomahe)  kthrpfm vaxiayatS  Y,  10.  y,  —  äsyaipAa  (sd.) 'raübya  Y.  57.  28;  —  *'rS  (GS.?) F.8'>.        2)  'Regentropfen'  (nur  Komp.).
23487:KompE.;  Ableit  —  Vgl.  'när-  md'väray.— ai,  vär-  r.  'Wasser",  np.  Sär-än  'Regen'.  — Pü. :  värän.  —   i)   Hds.  vate,  s.  aber  Pü.
23489:'regnen  sva.  den  Regen  fallen  lassen, veranlassen',  pers.:  fni//i  zi  ml  Alm  .  . värintalia  (3PPM.,  näml.  arsänd)  snal- iintaica  srascintalca  *fyatikuntalca  "durch- einander lassen  (die  vier  Hengste)  es  mir regnen  und  schneien  und  triefen  und hageln"  Ytf.  120;  —  vartnti  v3  mag- iinti  (sd.)  vä  . .  ayqn  "an  einem  Tag,  der (sva.  an  dem  es)  regnet  oder . ."  V.  ly.  4;
23494:Vgl  ^vir:  *-väraili  könnte  in  värm  'Regen' (AS.)  einfach  nach  äem  Maiter  'tnarlaii (•bd.  sniuii/)  lu  'snaciim  (gaL  inane)  gebildet sein.  —  np.  tärad  'es  regnet'.  —  Pü.  (in  V.  S) : pa  värän,  t«  V.  5):  fl/?  värintm,  (lO  V.  31): ia  afi  vor  et.
24259:•  j.  vi.vära-  n.  'nach  allen  Seiten  strömen- der Regen':  vwannti  (sd.)  'rahu'^  V, 2/.  3.
25655:•  j.  'urvant-  Adj.  (fem.  'vSiti-)  'flicssend, strömend',  auch  mit  Akk.  des  Inhalts'*: maiya  .  .  yahva  'väitii  (NPf.  statt  n.) awra  p)r3hu  aipi  vJjasäiti?  avS  "vaitTs (NPf.)  hapta  kar^qn  "die  Wolken  . .,  in denen  die  strömenden  Regenschauer  ent- halten sind,  die  Wasser  strömend  sich  gar weithin  verbreiten  über  die  sieben  K.  hin" Yl  Ä  40 ;  —  andvt  süra  . .  frä  . .  sispata *'vaiti''>  iaBu.staayeAi  (sd.)  Yt5.  7.
25691:•  j.  urvä^a-  Adj.  (fem.  Tä-)  'spülend, läuternd',  vom  Regenwasser:  aat  äpö  at-a.- barmte  .  .  tätä  -rä  baliazyä  Yt  8.  47.
27391:i)  'triefen,  abtriefen  von  -'  (Gen.  statt AbI.),vonfcttenSpeisen:a»^«iF(Sp.357f.) srasfintls  :^an^ä'V.3.2<}.  aa)  trief- regnen sva.  triefenden  Regen  fallen  lassen, veranlassen',  persänl.:  tnlsti  zl  ml  kim  .. var?ntal{si.)^a  sna^intal'a  srasctttta^a (3PPM.,  näml.  arsäna)  *fyankuntaica  Yt 5.  lao;  —  haca  xsafnB  varmtya  .  ,  sra- scirttyä  "in  einer  Nacht,  die  (sva.  in  der es)  . .  triefregnet"  Yt  16.  10'*.  b)  'als Triefregcn  (zur  Erde)  fallen':  cvat  aBanhä apSyaf  snaiSinfyai(sd.)äi  srascintyaica" "wie  viel  von  dem  Schnee  und  Regen- wasser . ."  V.  6. 36.
29724:.  j.  hazaorarnan-  Adj.  'tausend  Schläge , ,  ■   hazaurö.väray-  m.  'tausend  Regen- ausieJend,    tausend   tötend':    'yna  {1^^)  ^^^^^^^^jy^^^^^  ^^^^  ^^^^^^^^^^^^^^
29738:'rayS  batvars.värasät  "der  Nebel  wallt  . auf  dem  Wasser;  1000  Regentropfen, selbst    loooo   Regentropfen  (fallen)"  V.
```


## [2026-10-16T05:14:20.385Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'j\\.  vai[^ ]*i-  [fm]' BRT.txt | head; grep -n -i 'Bewässerungs' BRT.txt | head -3; grep -n 'Widder' BRT.txt | grep -i 'var' | head -3"
}
```


### [2026-10-16T05:14:20.723Z] TOOL RESULT

```
26932:•  j.  spä.b^^3z-  Adj,  (auch  fem.)  'in  der Höhe,  Tiefe  eines  Hunds"':  cvat  yavat vaiolm?  .  .  'ztm  (ASf)  spa/ra^ftn  "wie gross  der  Bewässerungskanal?  .  .  So  tief und  breit  als  ein  Hund"  V.  Jrf-ia.
22780:«iii«  var/ft;  (tu  Y.):  a/?-  -  vartSH.  Sü.:  fiari-  AbleH.  ans  *Z'flrai*o.fl-  EN.,  «ig.  'der  auf  die var/aya;  (zu  Yt.  /);  *vaSlär;  Npü,  (lu  Yt  14):  Schafe,  Lämmer  Acht  hal,  sie  hOlel'.  *variin- ka  ..hahrim  ..  andat  xä«a  u  maiJn  ba  mard  »■  'Schaf,  Lamm';  PDw.  var  'Widder',  gr. /  ^änanda  an  fat^arä  miraiad  . .  m!  eardä-  ■  /"P'!».  «nO-  g"'-".  »P'  »gl-  A»"" ''  J  »■  «OCh K3rf.  —  >)  Them.  -  ')  Vgl.  paiH-unaista:  ~  1  sfiUyxra..  *iaia-  zum  V.  iai-,  vgL  oss.  jä/äf- i)  Vßl.  Yl. /^Sönnter'rffl/-.  —  4)  NA.  «tera;  ^  'Hauswachter .  rorfi-ai  'Kalberhirt  — s.  aber  Var.  nnd  Yt.  14.  63.  '•  Auf  ir.  Kasustomen  mit  *uanf  {gr.a/n-;)
23088:•  j.  'varSnay-  m.  'Mäanchen  des  Schafs, Widder'  in  Verbindung  mit  dem  Namen fllr    Schaf":     maßahe    .  .  yat    •nBii    Yt.
23094:•  j,  varsni-haräta-  Adj.  '(admissuram habens,  d.  i.)  wofür  die  Zulassung  dei Widder,  der  Widdersprung  bezeichnend ist',  toa  Ayä^rima- (^sA.):  ayohrimtm  fra- ourvalltriimm  'tim  Y.  2. 9;  —  ayä%ri- m3i  .  .  °taica  Y.i.g;  —  aya^rimahe  .  . 'lahe^a  Vr.  /,  2.
```


## [2026-10-16T05:14:34.234Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -A22 '^webh\\|^ *webh-' AHD_watkins1985.txt | head -50; grep -n -i -B2 -A10 'wopsa\\|wobhs\\|wops-' AHD_watkins1985.txt | head -30"
}
```


### [2026-10-16T05:14:34.907Z] TOOL RESULT

```
<persisted-output>
Output too large (39.5KB). Full output saved to: /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tool-results/b4xr2duxj.txt

Preview (first 2KB):
1126:webh-. To weave, also to move quickly. 1. Germanic *weban in Old English wefan, to weave: WEAVE, WOOF'. 2. Germanic *wefta- in Old English wefta, weft, cross thread: wert. 3. Suffixed o-grade form *wobh-yo- in Germanic *wabjam, fabric, web, in Old English webb), web: WEB, WEBSTER. 4. Suffixed Germanic form *webila- in Old English wifel, weevil (< “that which moves briskly”): WEEVIL. 5. Suffixed Germanic form *wabila-, web, honeycomb, in: a. Middle Low German wdfel, hon- eycomb, akin to the source of Old North French waufre, wafer: GOFFER, WAFER; b. obsolete Dutch waefel, honey- comb: WAFFLE}. 6. Possibly Germanic *wab-, to move back and forth as in weaving, in: a. Old English wafian, to move (the hand) up and down: WAVE; b. Low German wabbeln, to move from side to side, sway: WOBBLE. 7. Suffixed zero-grade form “ubh-d- in Greek huphé, web: HYPHA. [Pok. vebh- 1114.]
1127-wed-'. Water; wet. 1. Suffixed o-grade form *wod-6r in Germanic *watar in Old English weter, water: WATER. 2. Suffixed lengthened-grade form *wéd-o- in Germanic *wéd- in Old English wt, wét, wet: WET. 3. O-grade form *wod- in Germanic suffixed form “wat-skan, to wash, in Old English wescan, wacsan, to wash: WASH. 4. Nasalized form *we-n-d- in Germanic *wintruz, win- ter, “wet season,” in Old English winter, winter: WINTER. 5. Suffixed zero-grade form *ud-d6r in Greek hudor, water: (HYDRANT), HYDRO-, (HYDROUS); ANHYDROUS, CLEPSYDRA, DROPSY, HYDATHODE, HYDATID. 6. Suffixed nasalized zero-grade form *u-n-d-d- in Latin unda, wave: UNDINE, UNDULATE; ABOUND, INUNDATE, (REDOUND), REDUNDANT, SURROUND. 7. Suffixed zero-grade form *ud-ro-, *ud-rd-, water animal, in: a. Germanic *otraz, otter, in Old English ofor, otter: OTTER; b. Latin Jutra, otter (with obscure /-): NUTRIA; C. Greek hudros, a water snake: Hyprus; d. Greek hudra, a water serpent, Hydra: Hypra. 8. Suffixed zero-grade form *ud-skio- in Scottish and Irish Gaelic uisge, water: USQUEBAUGH, (WHISKEY). 9. Suffixed o-grade form *wod-d- in Russian
...
</persisted-output>
```


## [2026-10-16T05:14:37.441Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'wopsa\\|wobhs\\|wops-' AHD_watkins1985.txt | cut -c1-600 | head -5; grep -n -i '^wers-\\|^wer-[0-9]*\\. *\\(Water\\|rain\\)\\|wer-\\*\\. Water' AHD_watkins1985.txt | cut -c1-500|head"
}
```


### [2026-10-16T05:14:37.857Z] TOOL RESULT

```
148:The names for a number of insects can be reconstructed in the protolanguage, includ- ing the wasP (wopsa), the hornet (*kras-ro-, a derivative of ker-', “head,” from the shape of the insect), and the fly (mu-2). The BEE (bhei-') was particularly important as the producer of honey, for which we have the common Indo-European name melit-. Honey was the only source of sugar and sweetness (swad-, “sweet,” is ancient), and notably was the base of the only certain Indo-European alcoholic beverage, MEAD, medhu-, meaning in different dialects both “mead” (“wine” in Greece) and “honey.” The Germanic
1172:*wer-ald., “life or age of man” (*-ald-, age; see al-3), in Old English weorold, world: woRLD; c. Frankish *wer- wulf, “man-wolf” (*wulf, wolf; see wikvo-), in French garou, werewolf: LOUP-GAROU. 2. Latin vir, man: VI- RAGO, VIRILE, VIRTUE, (VIRTUOSA), (VIRTUOSO); DECEM- VIR, DUUMVIR, TRIUMVIR. 3. Possibly Latin ciria, curia, court, if regarded as from *co-vir, “men together” (co-, together; see kom): CURIA. [Pok. uiro-s 1177.] wleik-. To flow, run. Zero-grade form *wlik-. 1. Adjective *wlik-u-, wet, in: a. suffixed form *wlik-w-d- in Latin liquare, to dissolve: LIQUATE; b. suffixed form 
2451:VESPIARY wopsa VEST wes-4 VESTA wes-3 VETCH weik-4 VETERAN wet-2 VETERINARY wet-2
1150:wers-2
1155:wers-'. To confuse, mix up. Compare ers-'. I. Suffixed basic form. 1. Germanic *werz-a-, whence *werra- in: a. Old North French werre, war: WAR; b. Spanish gue- rra, war: GUERRILLA. 2. Germanic comparative *wers- izon- in Old English wyrsa, worse: WORSE. 3. Germanic superlative *wers-istaz in Old English wyrsta, worst: worst. II. Suffixed zero-grade form *wrs-ti- in Germanic *wursti- in Old High German wurst (> German Wurst), sausage (< “mixture”): WURST; (LIVERWURST). [Pok. uers- 1169.]
1156:wers-2. To be wet. Compare ers-2. Suffixed o-grade (causative) form *wors-eyo- in Greek ourein, “to make water,” to urinate, whence ouron, urine: URETER, URE-
```


## [2026-10-16T05:14:39.850Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^wopsa\\|wopsa\\. ' AHD_watkins1985.txt | cut -c1-500; sed -n '1127p' AHD_watkins1985.txt | cut -c1800-3000"
}
```


### [2026-10-16T05:14:40.178Z] TOOL RESULT

```
1172:*wer-ald., “life or age of man” (*-ald-, age; see al-3), in Old English weorold, world: woRLD; c. Frankish *wer- wulf, “man-wolf” (*wulf, wolf; see wikvo-), in French garou, werewolf: LOUP-GAROU. 2. Latin vir, man: VI- RAGO, VIRILE, VIRTUE, (VIRTUOSA), (VIRTUOSO); DECEM- VIR, DUUMVIR, TRIUMVIR. 3. Possibly Latin ciria, curia, court, if regarded as from *co-vir, “men together” (co-, together; see kom): CURIA. [Pok. uiro-s 1177.] wleik-. To flow, run. Zero-grade form *wlik-. 1. Adjective *wli
```


## [2026-10-16T05:14:42.373Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -o 'wopsa\\. .\\{0,500\\}' AHD_watkins1985.txt | head -3; grep -o 'wed-.\\. Water; wet.\\{1500,2600\\}' AHD_watkins1985.txt | tail -c 1100"
}
```


### [2026-10-16T05:14:43.026Z] TOOL RESULT

```
wopsa. Wasp. Metathesized form *wospd. 1. Germanic *wosp- in Old English wesp, weps, wasp: wAsP. 2. Latin vespa, wasp: VESPIARY. [Pok. yobhsd 1179.] wos. You (plural). Latin vds (> Old French vous), you: RENDEZVOUS. [In Pok. 1. iu- 513.] wrad-. Branch, root. I. Basic form *wrdd- in Germanic *wrét- in Old Norse rét, root: ROOT!; RUTABAGA. II. Zero-grade form *wred-. 1. Germanic *wurtiz in: a. Old English wyrt, plant, herb: wort; b. German Wurzel (< *wurzwala, rootstock; *-wala, a roll, round stem; see w
```


## [2026-10-16T05:14:53.772Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in wasp vespiary water Vaseline weave web wave wafer woof wobble Webster; do echo \"## $w\"; grep -n -i \"^$w,\\|^$w \\|^$w\\b\" KLN_1966.txt | head -3; done"
}
```


### [2026-10-16T05:14:54.268Z] TOOL RESULT

```
## wasp
## vespiary
## water
## Vaseline
41123:vaseline,  n.,  a  petroleum  jelly;  petrolatum.  — Coined  by  Robert  A.  Chesebrough  in  1877  fr. vas-  (short  for  G.  fVasser,  ‘water’),  -el  (fr.  Gk. £X-aiov,  ‘oil’)  and  chem.  suff.  -ine.
## weave
## web
## wave
## wafer
## woof
## wobble
## Webster
```


## [2026-10-16T05:14:56.897Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; tail -c 300 KLN_1966.txt; echo; grep -c $'\\f' KLN_1966.txt; for w in wasp vespiary water weave web wave wafer woof wobble Webster; do echo \"## $w\"; grep -n -i \"^ *$w[,.]\" KLN_1971.txt | head -3; done"
}
```


### [2026-10-16T05:14:57.309Z] TOOL RESULT

```
alkaloids  obtained  from sabadilla  seeds,  used  in  medicine  in  the  treat¬ ment  of  rheumatism,  neuralgia,  etc.  —  F.  vera¬ trine,  fr.  ModL.  veratrina,  fr.  L.  verdtrum,  ‘helle¬ bore’,  fr.  verare ,  ‘to  tell  the  truth’,  fr.  verus, ‘true’;  so  called  because
902
## wasp
(eval):1: bad math expression: empty string
## vespiary
(eval):1: bad math expression: empty string
## water
(eval):1: bad math expression: empty string
## weave
(eval):1: bad math expression: empty string
## web
(eval):1: bad math expression: empty string
## wave
(eval):1: bad math expression: empty string
## wafer
(eval):1: bad math expression: empty string
## woof
(eval):1: bad math expression: empty string
## wobble
(eval):1: bad math expression: empty string
## Webster
(eval):1: bad math expression: empty string
```


## [2026-10-16T05:15:00.199Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in wasp vespiary water weave web wave wafer woof wobble Webster wet; do echo \"## $w\"; grep -n -i \"^ *${w}[,.] \" KLN_1971.txt | head -3 | cut -c1-600; done"
}
```


### [2026-10-16T05:15:00.618Z] TOOL RESULT

```
## wasp
265233:wasp, n. — ME. waspe , fr. OE. waefs, wasps, waesp, 
## vespiary
261318:vespiary, n., a wasps’ nest. — Formed on analogy 
## water
100819:water. — F. gazogene , a hybrid coined fr. gaz, 
106818:water, — OF. (F. gruau ), ‘oatmeal, grits, groats’, 
117317:water. — A hybrid coined fr. Gk. tiSop, ‘water’ 
## weave
55398:weave, join together, interweave, unite’, fr. con- 
265624:weave, tr. and intr. v. — ME. weven, fr. OE. 
## web
265638:web, webster, weevil, weft, wobble, woof. Cp. 
265644:web, n. — ME., fr. OE. webb, which is rel. to OS. 
## wave
188797:wave, undulate; to boil’. See well, ‘spring’, 
265372:wave, intr. and tr. v. — ME. waxen, fr. OE. 
265381:wave, n. — Fr. wave, v.; confused with ME. 
## wafer
264337:wafer, n. — ME. wafre, wafer, ‘a thin cake’, fr. 
## woof
268207:woof, n., 1) weft; 2) texture; fabric. — ME. oof, 
## wobble
267962:wobble, wabble, intr. v., to move unsteadily. — 
## Webster
265652:webster, n., a weaver ( obsol .) — ME., fr. OE. 
## wet
146325:wet, to flow’, fr. I.-E. base *mdd -, ‘wet, moist, 
259447:wet, moisten, sprinkle’, whence also Gk. o6p£co 
266254:wet, adj. — ME. we/e, wette, partly fr. pp. of
```


## [2026-10-16T05:15:02.895Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '265233,265250p;261318,261324p;265624,265660p;265372,265385p;264337,264350p;268207,268215p;267962,267970p' KLN_1971.txt; grep -n '^water, n' KLN_1971.txt"
}
```


### [2026-10-16T05:15:03.251Z] TOOL RESULT

```
vespiary, n., a wasps’ nest. — Formed on analogy 
of apiary fr. L. vespa , ‘wasp’, which prob. was 
metathesized fr. *vepsa, fr. l.-E. *wobh-sd, fr. 
base *\yebh-, *wobh-, ‘to weave’, whence also 
Gk. U90C, ‘web’, uepatvetv, OE. wefan, ON. 
vefa, ‘to weave’, OE. wxsp, wxps, ‘wasp’. See 
weave and -ary and cp. wasp. Cp. also next 
wafer, n. — ME. wafre, wafer, ‘a thin cake’, fr. 
ONF. waif re , waufre (F. gaufre), ‘honeycomb; 
wafer’, fr. Frankish * wafel , which is rel. to MDu. 
wafel , Du. wafel, ‘wafer’, OHG. waba, MHG., 
G. wabe, ‘honeycomb’, and to OE. wefan, 
OHG. weban, ‘to weave’. See weave and cp. 
waffle, goffer, gopher, ‘a rodent’. 

Derivatives: wafer , tr. v., wafer -y, adj. 
waffle, n., a crisp cake cooked over the fire in a 
waffle iron. — Du. wafel , fr. MDu. wafel. See 
prec. word. 

waft, tr. y., to carry lightly through the air or 
wasp, n. — ME. waspe , fr. OE. waefs, wasps, waesp, 
rel. to OS. waspa, MDu. wespe , Du. wesp, OHG. 
wafsa , wefsa , MHG. wefse, webse , wespe , 
G. Wespe, Dan. hveps, and cogn. with OI. 
ur$avabhib, ‘spider’, lit. ‘wool-spinner’, Avestic 
vawazaka-, ‘scorpion’ (prop, ‘a spiderlike ani- 
mal’), L. vespa , OSlav. vosa, Lith. vapsa, ‘gad- 
fly’, OPruss. wobse, Russ, os a, ‘wasp’, OBret. 
guohi, Co. guhien, ‘wasp’, OIr. foich , ‘drone’. 
All these words are derivatives of I.-E. base 
*webh-, *wobh-, ‘to weave’; see weave and cp. 
words there referred to. The wasp is called ‘the 
weaver’, in allusion to the weblike form of its 
nest. 

Derivatives: wasp-en, wasp- is h, adjs., wasp-ish- 
ly, adv., wasp-ish-ness, n., wasp-ling, n., wasp-y, 
adj. 
wave, intr. and tr. v. — ME. waxen, fr. OE. 
wafian, ‘to wave, brandish’, rel. to ON. vafra, 
vafta, ‘to hover about’, vafa, ‘to swing, waver’, 
fr. I.-E. base *webh-, ‘to move to and fro; to 
weave’. See weave and cp. waver. Cp. also 
wabble, wobble. 

Derivatives: wave , n. (q.v.), wav-ed, adj., wav- 
ing, n. and adj., wav-ing-ly, adv. 
wave, n. — Fr. wave, v.; confused with ME. 
wawe, waghe, ‘a wave’ (which is rel. to ON. vagr, 
‘sea’; see vogue). 

Derivatives: wave less (q.v.), adj., wav-y, adj., 
weave, tr. and intr. v. — ME. weven, fr. OE. 



wefan, rel. to ON. ve/a, Dan. vxve, Swed. vava , 
MLG., MDu., Du. weven y OHG. weban, MHG., 
G. weben, ‘to weave’, from I.-E. base *webh- , ‘to 
move to and fro; to move to and fro before the 
distaff; to weave’, whence also OI. ubhndti , um- 
bhati , ‘he laces together’, urna-vabhify, ‘spider’, 
lit. ‘wool-weaver’, Avestic ubdaena, ‘woven fab- 
ric’, Pers. baft an, ‘to weave’, Gk. 6<pVj, ticpaq, 
‘web’, i^aivav, ‘to weave’. Alb. veh (for *webh- 
nio ), ‘I weave’. Cp. wafer, wasp, wave, wax, n., 
web, webster, weevil, weft, wobble, woof. Cp. 
also baft, hypha, vespiary. 

Derivatives: weave , n., weav-er y n., weav-er-ess , 
n., weav-ing, n. 
weazen, n. . — A var. of wizen, 
web, n. — ME., fr. OE. webb, which is rel. to OS. 
webbi, ON. vefr, Dan. vxv, Swed. vdf, Du. 
webbe , web y OHG. weppi y MHG. weppe, webbe , 
OHG. giwebi, MHG., G. gewebe y ‘web’, and to 
OE. wefan , ‘to weave’. See weave and cp. abb. 
Derivatives: web, tr. v., webb-ed , adj., webb-er y 
n., webb-ing, n. 

webster, n., a weaver ( obsol .) — ME., fr. OE. 
webbestre , ‘a female weaver’, fem. of webba , 
‘weaver’, fr. webb , ‘web’. See prec. word and 
-ster. 

websterite, n., a variety of aluminite {mineral.) — 
Named after the Scottish geologist Thomas 
Webs ter (1773-1844). For the ending see subst. 
suff. -ite. 
wobble, wabble, intr. v., to move unsteadily. — 
Rel. to LG. wabbeln, ‘to wobble’, MHG. wabe- 



len, ‘to waver’, and to ON. vafla and vafra , ‘to 
hover about’, OE. wxfre, ‘wavering, restless’. 
See waver. 

woof, n., 1) weft; 2) texture; fabric. — ME. oof, 
fr. OE. owef, formed fr. pref. o-, and wef, ‘web’, 
fr. wef an, "to weave’; see a-, ‘on’, and weave. The 
initial w in woof is due to the influence of weave. 
Derivative: woof-y, adj. 

wool, n. — ME. wulle, wolle, fr. OE. wull, rel. to 
ON., Swed. ull , OFris. wolle , ulle , MLG., MDu. 
wolle , wulle , Du. wol, OHG. wo [la, MHG., G. 
265317:water, n, — ME. water, fr. OE. waster, rel. to OS.
```


## [2026-10-16T05:15:08.129Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'wabz\\|wasp' PHD_mackenzie.txt PHD.txt NYB_vol2_glossary.txt | head; grep -n -i 'wārān\\|waran\\b\\|wārīdan\\|warīdan\\|wārān' PHD_mackenzie.txt | head; grep -n -i 'quail\\|wartag\\|wardag' PHD_mackenzie.txt NYB_vol2_glossary.txt | head; grep -n -i 'wāf-\\|wāftan\\|wafdan\\|weave' PHD_mackenzie.txt NYB_vol2_glossary.txt| head"
}
```


### [2026-10-16T05:15:08.769Z] TOOL RESULT

```
PHD.txt:603:wābar [w’Al | M wbr, (N bāwar)] truth; belief. wābarīģān [w?/yk?n' | M wbryg’n) true, trustworthy. “Аһ: trustworthiness. wabz [wpc, wpz] wasp. wačast [wcst! = Av. vwacas-tasti-] strophe (of the Gathas). watéag [wck!, (bck!) | N bacca] child, baby, cub. wad [SL Y.ÀA < A sry’; wt! | M wd, N bad] bad, evil. ^ Áh : badness, evil. маа [w?t! | M wd, N bad] wind, breath, spirit; cal. 22nd day. wadag [wtk'] evil, vile, wicked. ~ih: evil, vileness. wādām [w’t?m | N bádám] almond. wādbān [w°tp’n' | N bādbān] sail.
PHD.txt:3048:particular ēwāzīg, waspuhragan; in ~ pad nàméist.
PHD.txt:3763:special waspuhragan.
PHD.txt:4270:wasp wabz.
PHD.txt:5146:nifrin wafrūnag nifrīdag Obad-/oft-1 Obastan! nibard- nibardīdan nibard nibardag nibastan wabz wafišn xwest xwestant nibistan 1-2paft waz- wizār wizür- wizarisn wizārdan wizārdwars wizīh-
PHD.txt:5160:wabz
PHD.txt:5277:Waspuhraginih “9 ve 1 n wāspuhragān we) 103351 wāyīdan ETH wastar N 635^ | wāstaryēš ^0 ch ev wüstaryosih ^c ~ 39 \
PHD_mackenzie.txt:5110:wabz [wpc, wpz] wasp.
PHD_mackenzie.txt:5231:waspuhr [w)spwhl] principal.
PHD_mackenzie.txt:5232:waspuhragan [w)spwhlk)n ] I. special, particular; 2. courtier.
5182:waran [wln l ] desire, lust.
5183:warAn [wi'n l ] ram.
5184:wAran [w)l)n l I M w)r)n, N baran] rain.
5622:xwaran [hwln 1M xwrn] banquet.
5644:xwarwaran [h'lvlwl'n l , -bl'n ] = xwarofriln.
6002:atmosphere andarway, way, spas.          banquet sur, xwaran.
6346: declining nisebig.                         desire (n.) arz6g, kam(ag), waran,
6998:    delimited.                           lust arzog, az, waran, waranigih.
7362:pro'nince awestam, nahang, paygos,             rain (n.) waran.
7963:west dosastar, xwarofran, xwarwaran.    uoman narig, zan; married ....... soy-
PHD_mackenzie.txt:1296:a-wardag ['wlt)k l ] undeviating.
PHD_mackenzie.txt:2339: frawardag [plwltk I M prwrdg] letter, epistle.
PHD_mackenzie.txt:2342: Frawardigan [plwltyk)n l I N farwardagan] festival of the frawards, the
PHD_mackenzie.txt:3206:karak [krk IN ......] quail.
PHD_mackenzie.txt:5192:lwardag [wltk I M wrdg, N barda] captive, prisoner•
PHD_mackenzie.txt:5195:lIwardag [wlth ] on heat (female animal).
PHD_mackenzie.txt:6151:captive dastgir, griftiir, wardag; v.   chariot rah, wardyun.
PHD_mackenzie.txt:6153:captivity dastgraw, wardagih.           charm nerang; v. spell.
PHD_mackenzie.txt:6487:eight hast.                                  epistle frawardag.
PHD_mackenzie.txt:6756:hand-guard abdast.                         (she-animal) wardagih; on ......., war-
PHD_mackenzie.txt:5134:waf- [wp- I P wf-, (N baf-)] weave.
NYB_vol2_glossary.txt:3069:patköftan [ptkwptn'] patköp/f- to knock; to encounter, of two armies 225; har cē-š patkéft whatever it (my foot) knocked, wherever my foot alighted on the ground 3219-19, — From pat + koftan, NP kēftan kób- *to break, to bruise', whose -b- may represent an earlier -B- < -p-. As to BP, koftan is registered in FrP 21 as a syno- nym of zatan and kostan, but only one MS (U; in Junker’s ed.) gives the pres.: kwbyt' = kobčt, kwbym = kobém, which may be influenced by NP. Cf, on the other hand, NP kuf ‘the weaver’s sley’, which is certainly derived from the pres. stem of this vb., and viškēftan viškēf- (g.v.) which probably belongs to the same root.
NYB_vol2_glossary.txt:3904:vat [w?py] sheaf 12818. — J-Prs b’fh (Barr), from *väftan vàf-, NP bdftan bäf- ‘to weave’.
```


## [2026-10-16T05:15:13.543Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'w.r.dan \\[\\|wārīdan\\|warīdan' PHD_mackenzie.txt | head -5; grep -n -i 'bāftan\\|bāf-\\|\\*waf-\\|\\*wab-\\|\\*uaf\\|\\*u̯af\\|baftan' CHEUNG.txt | head -10; grep -n -i 'bārīdan\\|barīdan\\|\\*wār-\\|\\*u̯ār' CHEUNG.txt | head -10"
}
```


### [2026-10-16T05:15:13.901Z] TOOL RESULT

```
26122:*NWIR: NP baftan/baf-, Bal. gwapit, gwapt/gwap-, Kurd. unin, Khuns. baf-/baft, 
40812:baftan/baf-, 402
```


## [2026-10-16T05:15:16.231Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '26095,26140p' CHEUNG.txt; grep -n -i 'rain' CHEUNG.txt | head -10; grep -n -i 'w[aā]r[iī]dan\\|warit' PHD_mackenzie.txt NYB_vol2_glossary.txt | head"
}
```


### [2026-10-16T05:15:16.650Z] TOOL RESULT

```
to a structure that is not typical for an IE form, having long *4 followed by *-b-. 
*REFERENCES: EVP: 94; Abaev, Slovar’ IV: 11; Lehmann 1986: 409a; Shahbakhsh: s.v. gwap- 


402 *yab/f2 


*uab/f ‘to weave’ 

*AVESTAN: YAv. ubdaéna- ‘made from woven material’ (V 8.23 ff.) 

*MIDDLE PERSIAN: BMP wp- /waf-/ ‘to weave’ 

*PARTHIAN: wf- ‘to weave’ = Ghilain: 56 | DMMPP: 340b 

Pres.: IND. 3sg. wfyd {hapax} 

*SOGDIAN: CSogd. w f, MSogd. w’f/wft ‘to weave’. 0 The form ptyw’fnd (M178 
ITV.124), given by Henning, Cosmog.: 307, is a nonce formation, Sims-Williams 
(apud NEVP: ibid.) 

Impf.: IND. 3pl. MSogd. w’fnd (Cosmog.: 307) 

*CHORESMIAN: w’f- ‘to weave’ => Samadi: 208 

*NWIR: NP baftan/baf-, Bal. gwapit, gwapt/gwap-, Kurd. unin, Khuns. baf-/baft, 
Abyan. vota/vah-, Qohr. vata/awh-, Yzd. vopt/vop- ‘to weave’ 

*NEIR: Oss. I. wafyn/waft, D. wafun/uft, uvd, Sh. waf-/wift, waf-/weft, Sariq. 
wof-/wift, Yzgh. waf-/waft ‘to weave’, Wa. Mt, (һ)ыЁ, ypif-/oft- ‘to weave, braid’, 
Pash. od-, obd-/ow-, ob-, (Waz.) wavd/web-, Yi. waf-/waft-, M. waf-/weft-, Yghn. 
wof-/wofta ‘to weave’ || (+ *pati-) ? Pash. pewd-, pey- ‘to pierce, transfix; string, 
thread’ || (+ *pari-) Wa. psır(w)eif-/poroft ‘to darn, braid’, Sariq. parwäf-/parwift ‘to 
plait, net’, porwóf ‘braid; hair (of female)’ 

*MISC: Par. yaf-/yafı, Orm. yaf-/yaf’ék ‘to weave’ = gaf-/gafok || (+ *pati-) ? Orm. 
piyek ‘to string beads’ 

*SANSKRIT: ürpavábhi- (m.) ‘spider’ = EWAia I: 243p; II: 506 

9 It is doubtful that OAv. ufiia- ‘to sing’ belongs to *uab/f- ‘to weave’ (as stated in 
for instance EWA II: 506; Porzig, Gliederung: 186), especially when the Ir. 
evidence suggests two different roots. The alternating *-b/fis due to assimilation to 
the perf. past participle ending *-ta: *ft regularly becomes Elr. *Bd. See also *uab/f'. 
1125:Ukr. Ukrainian Yghn. Yaghnobi 
1466:*REFERENCES: EVS: 117b; Chantraine 1168a; DKS: 300b; Werba 1997: 209 f. 
2740:virz-/virzd ‘to fry, parch, roast grain’ (*brj-ia-), Wa. vros-/vrost- ‘to bake, roast’, Yi. 
2959:remove’, Wa. wicin-/wicind- ‘to disperse, scatter grain’ || (+ *ham-) Sh. anjic ‘clay 
3362:away from’, MMP prc’r- (caus.) ‘to refrain, withhold, keep back’ || (+ *ui-) ? BMP 
3702:down [of rain, etc.]’) seems preferable for the present Sryáte, see Kulikov, Vedic 
4228:sediments]; to come, find oneself (in), Yzgh. óiy-/óed ‘to rain’, (caus./tr.) Sh. 
4657:*SANSKRIT: dam’ ‘to control, restrain (oneself), overpower, tame, subdue’ (RV+) 
4847:hold back, constraint || (+ *ham-) ? Kurd. (North.) hinartin/hiner-, (Central) 
4856:wodord- ‘to keep, take’ || (+ *pati-) Yzgh. paöir-/paöug ‘to hold back, restrain one- 
PHD_mackenzie.txt:5180:war-, v. waridan.
PHD_mackenzie.txt:5206:wAridan, war- [w)l-ytn l I M w)r-yst, N baridan] rain.
PHD_mackenzie.txt:5256:2wastan [wstn l ] = waridan.
PHD_mackenzie.txt:5588:xwAb                                    95                      xwaridan
PHD_mackenzie.txt:5621:xwiir-, -iin, y. xwaridan.
PHD_mackenzie.txt:5636:xwaridan, xwar- [hzv)l-ytn l ] drink.
PHD_mackenzie.txt:6438:dissatisfied ahunsand.                  drink (v.) xwaridan; cause to
PHD_mackenzie.txt:7363:   rostag, sahrestan.                          rain (v.) waridan, wa!itan.
PHD_mackenzie.txt:10316:,,\;~ilidan, waridan
PHD_mackenzie.txt:10784:judnay                         ......... \t.f..) l"     dwaridan
```


## [2026-10-16T05:15:20.464Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for r in BQT:218 BQT:2461 BQT:2262; do echo \"######## $r\"; timeout 300 python3 tools/ref_page.py $r --image 2>&1 | head -60; done",
 "timeout": 600000
}
```


### [2026-10-16T05:15:32.383Z] TOOL RESULT

```
######## BQT:218
no scan of BQT covers printed page 218 (see 'scans' in refs_online.json)
######## BQT:2461
(no exact page map; using offset -1917 -> pdf page 544; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2461.png
REF: BQT:2461  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 544  OCR-lang: fas

از کناب برهان قاطع در لفات متفرقه موی
بر هفتاد و بك لفت و کنایت
8 اذار اقی۱ ه بفتح اول وذال نقطه‌دار | تحمل کردن وگذرانیدن حرف پهلودار باشد از
و رای بی‌نقطه هردو بالف کشیده وقاف بتحتانی | ابنای جنس .
رسیده» بعضی کوبند این‌لفت بونانی است وبعضی ف؟ - بنم بای فارسی واسکون فا »
دیگر گوبند رومی‌است وآن‌دوائی باشد که‌بفارسی | بادیرا کوبند که در وقت چراغ کشتن و آتش
کچله کویند وازجملهٌ سموم‌است خصوص کر که ۱ روشن کردن از دهن برآرند .
وسگرا درحال میکشد » و در عربی خالق الکلب ی بِقَم « پفتح بای‌ابجد وقاف وسکون‌میم:
وقاتل‌الکلب گوبند.* چوبی‌باشد سرخ که بدان چیزها رنگه کتند۴ -
بعرفان بدر بردان » کنایه‌ازداسته | وم اول وقاف, اهل‌بمن درخت داتوره‌راگویند
۱ « کلمه سربانی است و بفارسی کچوله کوبند ودر تنکاین و مازندران «کلاج دارو »
پوست اورا کرفته باشند بوهان ریزه باید کرد. برکش ازب رکه بنفشه سبزتر وسطبرتر وگلش
مثل بنفشه سطبرتر وسرخ...» « تحفةٌ حکیم موّمن > 5072030808 . ر4: لفت نامه دهش+<
آذاراقی . ۴ - اسم صوت :
.اس اخیکتی «لخت نامه» .
۴ - (م) «بقم (بفتح اول و) بتشدید فاف چوبی است سرخ که رنگه رزان بدان رکه
کنند وبفارسی آنرا بکم کویند. درخت آن بز رکه است وبرکش بب رکه بادام ماند وجهت التیام
قروح کهن وجراحات تازه وقطع خون نافم.» «منتهی‌الارب» . هعرب «بکم» . رك: بکم. بگم ۰
5 بافتن - بفتح چهارم. از: باف + تن (پیوندمسدری). بانگ8ط ‏ 0۴2 1۱20
(دستة کنم). اوستابی - 048688 (بافته). ساسکریت» قی:- ۷8۳ [۵0782 (منکبوت).
اففای ۵481. ۵0421 (بافتن). استی ۷8۶18 ۰ بلوچی ۰8۷8۳۵8 8۷۵/280 . رخی ۷182 ۰
سریکلی ۷۵220 . درآربایی دوشکل -۷800 و - ۷808 آمده «اسشق ۱۹۸ ؛ درهم کردن
رسمانها چنانکه پارچه ساخته شود؛ درهم کردن تار وپود تا پارچه پدید آید. سچ..

######## BQT:2262
(no exact page map; using offset -1917 -> pdf page 345; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2262.png
REF: BQT:2262  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 345  OCR-lang: fas

وداغ سذفخها
وداغ۱ - بنتح اول وئای بالف کشیده ودغ « بفتح اول و ثالی و سکون عین
وبفين لقطه‌دار زده , آتش راگوبند که بعربی‌نار | بی‌نقطه, سفیدمهره راگویند وآن نوعی ازصدف
خواند . است که‌عوام کوش‌ماهی‌میگوبند.
۶ سره «عص گفته‌اند که ۱1۰ بت ۹
ودخان - باخای ضله دار بر وزن | دای ۱ مهراست رو
5 ۳ سفید واز دربا پرمباید و آنرا وت 3
پروین, جالوری است آپی ودندان دارد وگرد | بفارسی كجك میخوانندوئوتیای ی
دارد پاريك ودراز وپیوسته درآبهای شور وناصاف | اکبر همان است .آنرا بوزند
و تیره میباشد . گوبند نابیناست و چشم ندارد | و در داروهای چشم بکاربرند . ودع
وبهندی بزبو می گوبندش . گوبند عربی است ۲ .
ور -« بنتح اول‌وسکون‌نانی. سبق وتختةٌ ور تو باشی مرا تباشد غم.
اطفال را کوبند که معلمان بدان تعلیم دهنن ۲ بعنی واگر توباشی - و با جمیع معانی مترادف
چنانکه « فلانی‌فلانه چیز ورمیدهد » بعنی‌تعلیم است با «بر>چه درفارسی‌با وواوبهم تبدبل‌ميياید-
میدعد ودری میگوید - و بمعنی گرمی وحرارت وافاده معنی صاحب وخداوند ودارنده هم میکند
چتانکه : ور وبارور وامثال آن۴ - وبلفت زند ویازند(۱)

(۱) چك : ژند و باژند. :

۴ - بیرونی در بارة انواع صدف کوبد: « ومن‌انواعها «الودع» بجممها الزاج فی‌جزاثرهم
عند جزرالماء و بلفواما فی‌حفرة و بطمونها حتی یموت حیوانم! و تعفن لحوءها و تبطل - وکذلك
پفعل فی‌الدییجات ...؟ رك : الجماهر ص۲ (ضميمةکتاب). « ودع » هوخزف دود یکون فی‌البخر
و بقال له ببلاد الهند الکورة » ۶ عقار ۱۲۷ » نام هندی آن 82۱۷۷۳1 است 08171۳ (فر)<
42 680۳7262 3« عقار ۱۲۷ ف ». ۴ - رل : جهانگیری » رشیدی.

۴ * بر , پپلوی ۰۷۷۵۳ ۷۷2۵۳ « اونوالا ۳۸۸ >. ( از ربشة 087 بردن)پونددارند کی
و اصاف : بهره‌ور » کینه‌ور ۰ تاج‌ور ۰ بارو.؛ ۳ ۵0۳ : گنجور» رنجورء» مزدوره وخشور. دستور. رک
درا ز کشیدن » - ولیز *ور» ۳ بر » بصورت پیشوند فعلی بر سرکلماتی نظیر ورآمدن ( خمیر ) »
وراقتادن » ور پربدن » ور جستن » ور رفتن » ورداشتن » ورشکستن وغیره » وهمچنین برسن اسماءه

: (رشه ومصادر مرخم) : ورانداز, ورشکست 0 ورمال ۰ وهم صورت پسشوند برس آسماء : وردست ۰
```


## [2026-10-16T05:15:36.994Z] TOOL CALL #34: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2262.png"
}
```


### [2026-10-16T05:15:37.584Z] TOOL RESULT

```

```


## [2026-10-16T05:15:37.580Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-16T05:15:46.956Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat > data/verification/sources/refs/ocr/BQT/2262.vision.txt <<'EOF'\n[BQT p. 2262, read from page image by verifier for PDF page 527]\nودخین - با خای نقطه دار بر وزن پروین، جانوری است آبی و دندان دارد و گردی دارد باریک و دراز و پیوسته درآبهای شور و ناصاف و تیره میباشد . گویند نابیناست و چشم ندارد وبهندی بوبو می گویندش .\n(No etymological footnote by Mo'in for ودخین on this page.)\nودع - بفتح اول و ثانی و سکون عین بی‌نقطه، سفیدمهره را گویند ... گویند عربی است.\nور - ... footnote ۴: ور = بر، پهلوی war, wâr «اونوالا ۳۸۸». (از ریشهٔ bar بردن) ...\nEOF\npython3 tools/fetch_source.py --help 2>&1 | head -20"
}
```


### [2026-10-16T05:15:47.547Z] TOOL RESULT

```
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
```


## [2026-10-16T05:15:52.998Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; N='page 527'; for u in \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/webʰ-' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wobʰseh₂' \\\n 'https://en.wiktionary.org/wiki/بافتن' \\\n 'https://en.wiktionary.org/wiki/باران' \\\n 'https://en.wiktionary.org/wiki/wasp' \\\n 'https://en.wiktionary.org/wiki/vespa' \\\n 'https://www.etymonline.com/word/vaseline' \\\n 'https://www.etymonline.com/word/wave' \\\n 'https://www.etymonline.com/word/wobble' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wódr̥' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wŕ̥sēn' \\\n 'https://en.wiktionary.org/wiki/وازلین' \\\n 'https://vajehyab.com/moein/وردیج' \\\n 'https://vajehyab.com/moein/وازلین' \\\n 'https://vajehyab.com/moein/پارگین' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wértoks' ; do python3 tools/fetch_source.py \"$u\" --note \"$N, Webh/Wed verification\" 2>&1 | tail -1; done",
 "timeout": 300000
}
```


### [2026-10-16T05:15:59.910Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b5a7b47741f85f30.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/665356382d132c4e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a99d1a173da27456.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e6827b3b929efea0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c6db3e67f7fc0a16.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b3fdeec23f646c0c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b2cfd0452f5e51f4.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2b9d53fa6823679c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ff98ccf6d6399bdb.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3658df9147b80327.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fc16dc019ce898ea.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c5a651edfcae6948.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a8fca35c986a1567.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fdd510a3ba2312bd.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/55291544c6729363.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4961cc14f23e1be8.txt
```


## [2026-10-16T05:16:03.443Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in b5a7b47741f85f30 665356382d132c4e a99d1a173da27456 e6827b3b929efea0 b2cfd0452f5e51f4 fc16dc019ce898ea a8fca35c986a1567 fdd510a3ba2312bd 55291544c6729363 4961cc14f23e1be8 3658df9147b80327; do echo \"#### $f $(wc -c <$f.txt)\"; grep -i -m8 'etymolog\\|from \\|borrowed\\|وردیج\\|وازلین\\|پارگین\\|quail\\|بلدرچین\\|derived\\|Descendants' $f.txt | cut -c1-400; done"
}
```


### [2026-10-16T05:16:03.803Z] TOOL RESULT

```
#### b5a7b47741f85f30 6950
 Derived terms 
 From Wiktionary, the free dictionary
 Derived terms
 Terms derived from the Proto-Indo-European root *webʰ- (76 c, 0 e) 
 Proto-Germanic: *webaną ( see there for further descendants )
 Proto-Germanic: *wabjaną ( see there for further descendants )
 Proto-Germanic: *wiftiz ( see there for further descendants )
 Proto-Germanic: *wabją ( “ web ” ) ( see there for further descendants )
#### 665356382d132c4e 8113
 Etymology 
 Descendants 
 From Wiktionary, the free dictionary
 (Redirected from Reconstruction:Proto-Indo-European/wobʰseh₂ ) 
 Etymology
 Usually derived from *webʰ- ( “ to weave, braid ” ) in a multi-step process: [ 1 ] [ 2 ] [ 3 ] 
 Olsen follows a similar multi-step process from the same root with the same starting neuter s-stem noun, but she skips the adjectival step and further smoothens the semantic transition by supposing that a neo-root *wesp- ~ *weps ( “ to wrap ” ) emerged during this complex process. She also glosses *wóbʰseh₂ as an agentive collective "wrapper". [ 4 ] 
 Proto-Indo-Iranian: *wábžʰas ( see there for further descendants )
#### a99d1a173da27456 16319
 Etymology 
 Derived terms 
 From Wiktionary, the free dictionary
 Etymology
 From Middle Persian [script needed] ( wp- /⁠waf-⁠/ , “ to weave ” ) , from Proto-Iranian *wabdi , Proto-Indo-Iranian *wabdʰi , ultimately from Proto-Indo-European *webʰ- . Compare Greek υφαίνω ( yfaíno ) , English weave , Avestan ubdaēna ("made of cloth"), and Sanskrit उभ्नाति ( ubhnāti , “ entwine ” ) .
 Derived terms
 Retrieved from " https://en.wiktionary.org/w/index.php?title=بافتن&oldid=88204796 "
 Categories : Persian terms inherited from Middle Persian 
#### e6827b3b929efea0 14896
 Etymology 
 Etymology 
 Etymology 1 
 Derived terms 
 Descendants 
 Etymology 2 
 Descendants 
 Etymology 
#### b2cfd0452f5e51f4 135
#### fc16dc019ce898ea 170
#### a8fca35c986a1567 132
URL: https://vajehyab.com/moein/وردیج
#### fdd510a3ba2312bd 1158
URL: https://vajehyab.com/moein/وازلین
TITLE: معنی وازلین | فرهنگ انتشارات معین | واژه یاب
معنی وازلین | فرهنگ انتشارات معین | واژه یاب 
 وازلین
 وازلین در فرهنگ‌های دیگر
 معنی وازلین در لغت‌نامه دهخدا 
 معنی وازلین در فرهنگ فارسی عمید / قربان‌زاده 
 معنی وازلین در دیکشنری فارسی به عربی 
#### 55291544c6729363 1116
URL: https://vajehyab.com/moein/پارگین
TITLE: معنی پارگین | فرهنگ انتشارات معین | واژه یاب
معنی پارگین | فرهنگ انتشارات معین | واژه یاب 
 پارگین
 پارگین در فرهنگ‌های دیگر
 معنی پارگین در لغت‌نامه دهخدا 
 معنی پارگین در فرهنگ فارسی عمید / قربان‌زاده 
 معنی پارگین در دیکشنری فارسی به انگلیسی 
#### 4961cc14f23e1be8 169
#### 3658df9147b80327 6094
 Etymology 
 Derived terms 
 Descendants 
 From Wiktionary, the free dictionary
 Etymology
 From *wed- ( “ water ” ) +‎ *-r̥ ( r/n-stem suffix ) .
 Derived terms
 ⇒ ? Latin: unda   f ( “ wave ” ) [ 1 ] ( see there for further descendants )
```


## [2026-10-16T05:16:07.370Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; cat fdd510a3ba2312bd.txt 55291544c6729363.txt a8fca35c986a1567.txt b2cfd0452f5e51f4.txt | head -60; sed -n '/Etymology/,/Descendants/p' 665356382d132c4e.txt | head -40; grep -A3 -i 'Etymology' e6827b3b929efea0.txt | head -30"
}
```


### [2026-10-16T05:16:08.054Z] TOOL RESULT

```
URL: https://vajehyab.com/moein/وازلین
FETCHED: 2026-10-16T05:15:59Z
STATUS: 200
TITLE: معنی وازلین | فرهنگ انتشارات معین | واژه یاب

معنی وازلین | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 وازلین

 فرهنگ انتشارات معین
 (زِ) [ فر. ] (اِ.) نوعی روغن که از آن برای تهیة بعضی داروها، پمادها و لوازم آرایشی استفاده می کنند.
 وازلین در فرهنگ‌های دیگر
 معنی وازلین در لغت‌نامه دهخدا 
 معنی وازلین در فرهنگ فارسی عمید / قربان‌زاده 
 معنی وازلین در دیکشنری فارسی به عربی 
 معنی وازلین در دیکشنری فارسی به انگلیسی 
 معنی وازلین در دیکشنری فارسی به ترکی 

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره 
 نسخه جدیدURL: https://vajehyab.com/moein/پارگین
FETCHED: 2026-10-16T05:15:59Z
STATUS: 200
TITLE: معنی پارگین | فرهنگ انتشارات معین | واژه یاب

معنی پارگین | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 پارگین

 فرهنگ انتشارات معین
 ( اِ.) 1 - فاضلاب . 2 - آشغال دانی .
 پارگین در فرهنگ‌های دیگر
 معنی پارگین در لغت‌نامه دهخدا 
 معنی پارگین در فرهنگ فارسی عمید / قربان‌زاده 
 معنی پارگین در دیکشنری فارسی به انگلیسی 
 معنی پارگین در واژه‌های مصوب فرهنگستان 
 واژه‌های مشابه
 پارینه 
 پارینه سنگی 
 پاراگین 
 پارکینسون 
 پارکینگ 
 پارگی 

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره 
 نسخه جدیدURL: https://vajehyab.com/moein/وردیج
FETCHED: 2026-10-16T05:15:58Z
STATUS: -1
TITLE: 
 Etymology 

 1.2 
 Noun 

 1.2.1 
 Declension 

 1.2.2 
 Related terms 

 1.2.3 
 Descendants 
 Etymology
 [ edit ] 

 Usually derived from *webʰ- ( “ to weave, braid ” ) in a multi-step process: [ 1 ] [ 2 ] [ 3 ] 

 One starts with a neuter *-os action noun *wébʰos , which survives as Ancient Greek ὕφος ( húphos , “ web ” ) with analogical zero grade.

 This neuter noun would then be the source of an *-ós adjective. Höfler reconstructs this adjective as *ubʰsós ( “ weaving ” ) while Lipp gives *wobʰsós ( “ having a woven nest ” ) . Mallory and Adams skip this step.

 This adjective would then form o-grade deadjectival substantives, namely *wóbʰsos (in Indo-Iranian) and *wóbʰseh₂ (elsewhere), which would come to mean "wasp".

 The "weaving" of wasps refers to their nest construction. 

 Olsen follows a similar multi-step process from the same root with the same starting neuter s-stem noun, but she skips the adjectival step and further smoothens the semantic transition by supposing that a neo-root *wesp- ~ *weps ( “ to wrap ” ) emerged during this complex process. She also glosses *wóbʰseh₂ as an agentive collective "wrapper". [ 4 ] 

 Noun
 [ edit ] 

 *wóbʰseh₂   f [ 5 ] [ 6 ] [ 7 ] 

 wasp 

 Declension
 [ edit ] 

 Thematic in *-eh₂ 

 Etymology 

 1.2 
 Noun 
--
 Etymology 

 2.2 
 Noun 
--
 Etymology 1 

 3.1.1 
 Noun 
--
 Etymology 2 

 3.2.1 
 Noun 
--
 Etymology 

 4.2 
 Pronunciation 
--
 Etymology 

 5.3 
 Pronunciation 
--
```


## [2026-10-16T05:16:14.867Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; grep -A4 'From Middle Persian\\|From Proto-Iranian\\|inherited' data/verification/sources/web/e6827b3b929efea0.txt | head -15; for u in 'https://abadis.ir/fatofa/وردیج/' 'https://vajehyab.com/dehkhoda/وردیج' 'https://en.wiktionary.org/wiki/varttikā' 'https://en.wiktionary.org/wiki/vaseline'; do python3 tools/fetch_source.py \"$u\" --note \"page 527, Wed: vardij/vaseline check\" | tail -1; done"
}
```


### [2026-10-16T05:16:17.842Z] TOOL RESULT

```
 From Middle Persian [script needed] ( wʾlʾn' /⁠wārān⁠/ ) ( Manichaean Middle Persian [script needed] ( wʾrʾn /⁠wārān⁠/ ) ), compound of [script needed] ( wʾl /⁠wār-⁠/ ) and [script needed] ( -ʾn' /⁠-ān⁠/ ) , from Proto-Indo-Iranian *wáHr̥ ( “ water; rain ” ) , from Proto-Indo-European *weh₁r- ( “ water ” ) .

 Indo-Iranian cognates include Northern Kurdish baran , Northern Luri بارۆ ( barø ) , Avestan 𐬬𐬁𐬭𐬀 ( vāra , “ rain ” ) , and Sanskrit वार् ( vār , “ water ” ) . Other Indo-European cognates include Luwian 𒉿𒀀𒅈 ( wār , “ water ” ) , Old Norse vari ( “ liquid, water ” ) and Latin ūrīnor ( “ to dive ” ) .

 Pronunciation
--
 Categories : Central Kurdish terms inherited from Proto-Indo-Iranian 
 Central Kurdish terms derived from Proto-Indo-Iranian 
 Central Kurdish terms inherited from Proto-Indo-European 
 Central Kurdish terms derived from Proto-Indo-European 
 Central Kurdish lemmas 
 Central Kurdish nouns 
 Kashmiri terms borrowed from Persian 
--
 Persian terms inherited from Middle Persian 
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c0ea58a27363305f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fe7f1fa68b44c626.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3f72baf965c7cad0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ecc5f2cb48d2c8e1.txt
```


## [2026-10-16T05:16:20.501Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in c0ea58a27363305f fe7f1fa68b44c626 3f72baf965c7cad0 ecc5f2cb48d2c8e1; do echo \"#### $f $(wc -c <$f.txt)\"; grep -v '^\\s*$' $f.txt | grep -i -m6 'وردیج\\|بلدرچین\\|Etymology\\|From \\|quail\\|Vaseline' | cut -c1-400; done"
}
```


### [2026-10-16T05:16:20.955Z] TOOL RESULT

```
#### c0ea58a27363305f 3987
URL: https://abadis.ir/fatofa/وردیج/
TITLE: وردیج - معنی در دیکشنری آبادیس
وردیج - معنی در دیکشنری آبادیس 
 وردیج
 وردیج. [ وَ ] ( اِ ) ورتک. وردج. ( فرهنگ فارسی معین ). ورتیج. ( برهان ) ( آنندراج ). و آن پرنده ای است کوچکتر از تیهو. بلدرچین. سلوی. ( برهان ) کرک. ( ناظم الاطباء ).. رجوع به ورتیج شود : 
سحر که مدح جمالش شنیدم از وردیج.
#### fe7f1fa68b44c626 1399
URL: https://vajehyab.com/dehkhoda/وردیج
TITLE: معنی وردیج | لغت‌نامه دهخدا | واژه یاب
معنی وردیج | لغت‌نامه دهخدا | واژه یاب 
 وردیج
 وردیج . [ وَ ] (اِ) ورتک . وردج . (فرهنگ فارسی معین ). ورتیج . (برهان ) (آنندراج ). و آن پرنده ای است کوچکتر از تیهو. بلدرچین . سلوی . (برهان ) کرک . (ناظم الاطباء). . رجوع به ورتیج شود : 
سحر که مدح جمالش شنیدم از وردیج .
#### 3f72baf965c7cad0 135
#### ecc5f2cb48d2c8e1 10142
URL: https://en.wiktionary.org/wiki/vaseline
TITLE: vaseline - Wiktionary, the free dictionary
vaseline - Wiktionary, the free dictionary 
 Etymology 
 Etymology 
 Etymology
```


## [2026-10-16T05:16:23.665Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' ecc5f2cb48d2c8e1.txt | grep -A2 '^ Etymology$\\|^ *English\\|^ *French' | head -30"
}
```


### [2026-10-16T05:16:24.169Z] TOOL RESULT

```
 English 
 Toggle English subsection 
 1.1 
--
 French 
 Toggle French subsection 
 3.1 
--
 English 
 Read 
 Edit 
--
 English
 [ edit ] 
 English Wikipedia has an article on: vaseline 
 Wikipedia 
 Alternative forms
--
 Etymology
 [ edit ] 
 Etymology tree
--
 English -ine 
 English vaseline 
 From German Wasser ( “ water ” ) +‎ Ancient Greek ἔλαιον ( élaion , “ oil ” ) +‎ -ine . Genericized trademark of the Vaseline brand of petroleum jelly introduced by American chemist Robert Augustus Chesebrough in 1872. [ 1 ] 
 Pronunciation
--
 French: vaseline   (fr)   f 
 Georgian: ვაზელინი ( vazelini ) 
 German: Vaseline   (de)   f , Vaselin   n
```


## [2026-10-16T05:16:27.766Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' ecc5f2cb48d2c8e1.txt | sed -n '/^ French$/,$p' | grep -m3 -i 'borrowed\\|from' | cut -c1-300; cd ../refs; grep -n -i 'wasp\\|vespa' SYN.txt | head -5; grep -n -i 'webh\\|weave' IEC.txt | head -5; grep -n -i 'wobhs\\|wopsa\\|wasp' IEC.txt | head -5; grep -n -i '^ *quail\\|vardij\\|quail' HUB.txt SKT.txt | head -5; grep -n -i '^vaseline\\|^wasp\\|^weave\\b\\|^vespiary' SKT.txt | head"
}
```


### [2026-10-16T05:16:28.181Z] TOOL RESULT

```
 Borrowed from English . Genericized trademark.
 Retrieved from " https://en.wiktionary.org/w/index.php?title=vaseline&oldid=92770791 "
 Categories : English terms derived from Middle High German 
5122:Skt. bambhara- (rare), of imitative orig. : Grk. reudpnddy ‘a kind of wasp’, etc. Walde-P. 2.161.
6059:Grk. cgay or pl. cdayat (both in Aristot.) ‘throat’, this prob. the earliest meaning of the word, whence o¢étw ‘cut the throat, slay’ (cf. Lat. iugulare ‘slay’ fr. cugulum ‘throat’) and the re- sulting common use of c¢ay as ‘slaugh- ter’. No accepted etym., but prob. con- nected, by a series of parallel root-forms, with o¢yt, Dor. opat (gen. -xés) ‘wasp’, o¢yv, Dor. cpav ‘wedge’, odiyyw ‘bind tight, constrict’, all with common notion of ‘narrow’. Cf. Dan. strube, etc., below, 4. (Different combinations in Walde-P, 2.651-53, 658.)
1232:bherdho ‘strike, kill Skt. barhe “hurt”; Gk. pértho ‘sack, destroy’; Br. cf. berza, pp. berzet ‘forbid’; berz ‘ban’; R beredit ‘irritate a wound’ beside bërdo ‘weaver’s sley’. Z-gde in OE an-byrdan ‘op- pose’
1444:bhndh- “bound; binding'. See bhendh-. WP cf. II, 152 Skt. baddháh; Oss. cf. bándàn ‘string’; Tokh. B cf. panto ‘peace’; Gk. cf. em-pásso ^weave- in, embroider’; lá-pathos (Cpitfall'. Cf. ləu- catch") beside Hes. pásma ‘peduncle’; prob. also páthne, beside phátne ('stable, manger’. For sense cf. MHG banse: EME boose); Lat. cf. (e- or zero-grade) of-fendix ('slipknot, strap-buckle" or sim.); Ir. bann ‘bond, belt, hinge, chain, law’; Br. bann ‘skein’; MHG bunt, -des ‘band, fetter, knot; OE bund ‘bundle’; ON cf. bundinn ‘sheaf. Variant (*bhndhtó-) in Av. bastō, Per. baste
2398:dorbh-, see drbh- ‘twist, turn, beng’ Skt. (z-gde) drbhåmi (1) ‘weave’; Av. cf. darov- ‘join’; OE cf. tearflian (for *tearfian? ‘turn, roll, wallow’), Wh. R doróbjic ‘bend’; OHG zerben “spin, roll"
2514:drbhó, ið ‘twist, turn’. Cf. dorbh- Skt. drbhámi (2) ‘weave’; (o-gde in Ir. darb, dairb ‘weevil’; doirbh 'cattle-tick'; OE tear- flian ‘turn, wallow’; MHG zerben; Wh. R. dorobjic)
4240:gongh- (gonghus, gonguhis) ‘twist’. WP I, 587 Gk. (from Thrac.?) gággamon, gaggáme ‘dragnet’; ON cf. keng, m. ‘crook, beng’; kongur-váfa, lit. weave-web' > ‘spider’; OCS cf. gọžvica ‘withy’; Cz. houZ *bast-rope', houž- ev ‘withy, rope; R guZ “rope, thong’; OCz. húžě ‘string’; Pol. (alleged) gazwy ‘thong’; Blg. cf. găžba *bast-rope
1335:bhit- ‘bee’. WP II, 185 Hind. cf. bhir ‘wasp’; Arm. cf. bčič (a-st. ‘honey-cell’, fr. *bhit-itio (?)); Ir. cf. beath- mhan, beathóg (allegedly = ‘bee’ — Lane, but of uncertain documentation), W cf. byd-af (‘hive of wild bees’, fr. *bhitəma); Li. bitis, f. and bite ‘bee’; Latv. bite, id.
3085:“twist, turn, spin (tr.); Ir. cf. (?) dreas (“bout, turn”, if for *dhre&hso-) (dhrën-, see dhrān-. Vocalism ambiguous in Gk. & Gmc.) Gk. cf. ten-thréne (‘bee or *wasp"); an-thrén& ‘wild bee’; thrénos ‘dirge; OS dràn, Let ‘drone’; OE dræn beside dran, id. (*-oi-?) dhreng- (dhrong-) "wer Go. drigkan, OHG trinkan, etc. («drink', and com. Gmc.); Li. drengiü, ti ‘sleet, pour w. rain’; o-gde in Sw. drank ‘mash; barm’ as well as in G Ge-trank, E to drench, etc: R (Ð cf. driàzgi ‘dirt; twaddle’ (but Pol. drzazga “chip, splinter, log? may be of Wh. R. origin) dhrengh- “slow, sullen, sad, limp, hanging”. Cf. WP I, 813 Per. dirang ‘slow’; Tokh. A trànk-, B treñk- ‘hang’; W dreng, adj. ‘surly’; R cf. drjàgat, drjagnüt ‘dangle’; Li. drengiü, ti (1) “wear out dhrésó, ið (?) “shout, rave’ Gk. thréo ‘shriek’; ON dræsa, f. ‘twaddle’; Latv. cf. (o-gde) draséju ‘yodel, jubilate? dhreudo, io, dhroud-, dhrud- “bully, illtreat, threaten’. Cf. WP I, 870 NG triezen ‘twist, tug, bully); MHG (z-gde) trutzen ‘defy’; Li. (o-gde) draudžiù, draüsti ‘warn, ban’; Latv. draudu, ét ‘threaten’ dhreugh- (1), dhrugh- ‘harm, deceive’. Cf. WP I, 860 & 874 Skt. drohah ‘harm, wrong’; drühyami ‘hurt, offend’; Av. druž- ‘deceive’ beside druxš-, o-gde in draoxš-, id.; LW in Arm. držem, id.; MHG (regen, id. beside (z-gde) troc, gs troges ‘deceit; OS driogan; Du. be-driegen *cheat'; Av. cf. draoyo; Per. durüy ‘falsehood’ dhreugh- (2), dhrough- “good, fit, sprightly, pleasant'. See dhrough- Lat. cf. ? fruor (ambig. ‘enjoy’, if distinct from früx, -gis, frügalis, etc. See bhrüg-); Br. dréó ‘gay, tipsy’; OE dreog ‘fit, sober, serious, gentle beside dréogan ‘behave, experience’; ON drjúgr ‘substantial, lasting’; Li. (o-gde) draugùs ‘sociable’ dhreus- ‘crumble, fall; crumb, fragment(sy Arm. cf. eyğiwr (2) ‘husks’; OE drēosan, v. ‘fall, perish’; drēor, m. ‘blood’; Ukr. cf. dru-
3562:empis, io “insect; swarm’. WP I, 125 Gk. empís; OHG imbi ‘swarm of bees; MHG imbe, OE imbe, id.; LG imm, wf. ‘bee’; Cz. cf. jepice (^mayfly', fr. *empitio); Pol. cf. jetka, id. (fr. a type *emptika); ? cf. Finn. (LW?) ampia- (^wasp- in cpds.)
6099:&hol- (&holn- gheln-) (2) “gall, bile’. Cf. 2hol- (1) and ĝhel-. WP I, 624 Gk. khólos, kholë, id. cf. s-kholë “freedom from bitterness’, hence “leisure” (cf. Ks-, eKs-); e-gde in Lat. fel, gs fellis; OHG cf. galla, OE gealla; ON gall, id. (Isophones: Srb. zolja ‘wasp’; Li. Zalà ‘harm’; Av. cf. zaronu (2) 'anger)
9104:W ambig. crygu (“make hoarse, grow hoarse’. Cf. krik-); Li. Sir$u, Eti, v. “buzz, hum”, cf. širšē *hornet'; SirSinas ‘wasp’; Latv. sirsenis & sirsonis *hornet' (assimilated from Krs-, q. v.). (An unexplained collective in W cacwn "bor. nets', indicates a double *-K-)
HUB.txt:5799:Abal. 73, skr. vdrcas- ; vardij ^Wachtel', skr. vdrtika-, var-
SKT.txt:15288:M.  E.  quailU.  —O.K.  ^uaUU,  V.  caiii*,*' Low  L.  ifua^uila.  a  quftil.  — O.  Du.  qvackti. a  quail. —  O.  Du.  guMktn,  Du.  kwakiM,  lo quack  (above).  Fiom  the  noUc  which  the bird  makes.
SKT.txt:15376:Qu^ ;  see  Quail  (i>.
SKT.txt:22837:fuack,  quail,  quarrel,  quarry,  quill,  quire, Quiver.
SKT.txt:23525:fftrtchfrom  Lffw  Gtrman :  fudge,  staple  |  Fremk  from  Low  Latin  fram  Lmv ),  tampion.  '  GtrmoM :  quail  \2).
21208:WASP.
```


## [2026-10-16T05:16:32.178Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n '21205,21215p' SKT.txt | cut -c1-500; sed -n '5795,5802p' HUB.txt; grep -n -i 'wazzar\\|wazar' WLD_band3.txt | head -2; grep -n -i 'Wespe' incoming/WLD/WLD_Bd1_pages.txt | head -3; grep -n -i 'ubdaena\\|ubdaëna' incoming/WLD/WLD_Bd1_pages.txt | head -3; grep -n 'vairi\\|varəšni\\|vār-' incoming/WLD/WLD_Bd1_pages.txt | head -5"
}
```


### [2026-10-16T05:16:32.621Z] TOOL RESULT

```
throw,  cast  (hence.  ••
this  mod.  C  loa//  v^rt  0
WARRANT.
WASP.
553
u  A.  S.  ■weor/>an.  So Vftfrthi,  Thin  Vitrpe,  to  warp  a Svrea.  varp^  the  draught  of  a  net.
tt,  »b  (F.-O.  H.  G.)  M.  E. to.  F.  waratii,  ^ttarant,  Uter nrAmnt ; '  Cot.  The  form  tuar- (of  the  prcs.  pi.,  with  the  tentic J/  —  O.  H.  G-  warjan,  wtrjan ),  to  protect,  lit.  'to  heed.'- Ctvi/'d,  heed,  care.  Allied  to .  Ufarrantt  verb ;  warranty, AT,  orig.  fem.  of  pp.  of  war- t ;  see  ffixarantee  (below). ytee.  sb.  (F.-O.  H.  G.)  For- Panfy  or  gnran/y,  which  are tt^ES.«>0.  Y.garaHtU.garrantif, ♦;  (em.  of  pp.  of  garantir,  to p.  F.  garan
0  (above).  Dor.  ^WdroM/^r,  verb. 0.   warlsoim,   protection,  re-
•O.  H.  G.)  M.  E.  waruetm, (the  true  sense) ;  more  com- B  icnse  of  reward  or  help ;    it
t  recovery  from  illness  or  healing.
~  sen,  garisoH,  iurety,  safety, »lu>g.  — O.  K.  -Ufarir,  to  pro-
vasama velum' (Vis u Kamm 856, 1 nach v. Stackelberg)
neben bascttna^ =■ arm. varsamak\ valdna *Wunde': lat. vol-
nus? (oben p. 104); vaxsur ^Prophet' =- paz. vaxsur Shk.
270, zd. "^vaxsahara- ; varj 'Grosse, Wiirde' = phi. varc Guj.
Abal. 73, skr. vdrcas- ; vardij ^Wachtel', skr. vdrtika-, var-
taka^; vary = bary *Wasserwehr, skr. varga- 'Abwehrer ;
vazay Trosch* ^^ zd. vazaya-; vantdan 'wehen', skr. vah
'dahinfahren , wehen*; vaztr 'Vezir', aus dem Arabischen
4178:av&gqdcbv „Wespe, Waldbiene** mit nach TEv&ggrt] ,.Hornis“, Tavdgijdojv
18001:kodile folgende) Ichneumon und eine Wespe" kaum die Spur als die, der
24151:uobh(e;Sa „\Vespe", zu a ebb- „weben". vom gespinstartigen Wespennest
20931:      Lit. i-vairiis „tortuosus. mannigfaltig. verschiedenartig" (v. d. Osten-Sacken
25200:av. vairi- m. „See‘" (aus *uar- nach Streitberg aaO. ? eher *uer~, *uor -)
```


## [2026-10-16T05:16:36.433Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; for l in 24151 25200; do awk -v L=$l 'NR<=L && /\\[pdf page/ {t=$0} NR==L{print t; exit}' WLD_Bd1_pages.txt; sed -n \"$((l-3)),$((l+3))p\" WLD_Bd1_pages.txt; done; grep -n -i 'ubdaena\\|ubdaena\\|ubhnati\\|ubhnäti' WLD_Bd1_pages.txt | head -3; grep -n 'vär-\\|vär „' WLD_Bd1_pages.txt | head -3"
}
```


### [2026-10-16T05:16:36.789Z] TOOL RESULT

```
vapeti „schwatzen, plappern" nichts zu tun haben.     Vgl. Fick III 4 392.


uobh(e;Sa „\Vespe", zu a ebb- „weben". vom gespinstartigen Wespennest
         ( trotz    Meiller Dial, indoeur. 20).
    Ay. nuezaka- m. Name eines daevischen Tieres, balm'i gvabz „Biene.
 Wespe. Hornis" (s. Geiger Abb. d. bail Ak. 1891, 125, Bthl. Wb. 1346):

         Ai.      van f. „\Vasser“ (Schroder WZKM. 20, 400), vur, vuri n. „Wasser“                                                                    ;


av. vairi- m. „See‘" (aus *uar- nach Streitberg aaO. ? eher *uer~, *uor -)
vur- ,,Regen“, vanntae-ca ,,sie lassen regnen“, vdrantiayaji „an einem Tage,
wo es regnet'"';
         tochar.         A war „Wasser‘‘; arm. (Scheftelowitz BB. 29, 44) gayr „Sumpf,
```


## [2026-10-16T05:16:41.240Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; grep -n 'pdf page' WLD_Bd1_pages.txt | head -2; grep -n -i 'ubdaena\\|ubdaéna\\|bäfad\\|bafad\\|bäftan' WLD_Bd1_pages.txt | head; grep -n -i 'wazzar' WLD_Bd1_pages.txt | head -2; grep -n -i 'aoda-\\|aoba-\\|vaidi-\\|vaißi\\|udra-' WLD_Bd1_pages.txt | head -5"
}
```


### [2026-10-16T05:16:41.650Z] TOOL RESULT

```
23571:void /-St. abgeleitet samitdra-h ,.Meer , anudra-h „wasserlos u (= gr. dvv-
47418: xsaodah-         n.   „FIuB,         Strdmung, Wasserschwall", xsudra -, xsudra- ..fliissig;
```


## [2026-10-16T05:16:43.785Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; sed -n '23545,23580p' WLD_Bd1_pages.txt; grep -n 'weban\\|wefan' WLD_Bd1_pages.txt | head -5"
}
```


### [2026-10-16T05:16:44.162Z] TOOL RESULT

```
 238, 266 im ubrigen s. die Lit. bei Boisacq u. avdij.
                 :




                                w
*2.    lied- „netzen   heteroklit. rjn- St. uedor. uodor (nom. sg.), uden(i)
                                         ;


                  udncit (gen. sg.) „Wasser“, vgl. J. Schmidt PI. 172 ff. Peder-
            (loc. sg.;,                                                                                                                                         .




         sen KZ. 32, 240 ff.. Bthl. PBrB. 41. 273.
                                                                                           1
      Ai. umUti , unddti ..quellt, benetzt- ; av. vaiSi-                                                                        f.       .AYasserlauf, Bewasse-
rungskanalA
      Ai. udun(i) loc., udndlt gen.,                                                 udnd instr.                   „ \ Yasser
                                                                                                                                          1
                                                                                                                                              (n. a. sg.   uclaka-ni )
                                       M
void /-St. abgeleitet samitdra-h ,.Meer , anudra-h „wasserlos u (= gr. dvv-
600?),         adrd-h „ein YYassertier                                     1'
                                                                                    = av. uclra- m. „Otter, Fischotter'                                                 (= gr.
 v6go?,         ahd.      usw.                    ottar,       vgl.            auch        lat.       lutra             und     mit u lit. itdra, aksl.
vijdra         ds.):     von einem                            -(<•).?- St.              (vgl.         gr.          to       vdo?) ai. atsa-h „Quelle.
 BrunnenA arm.                           <jet              „FluB"‘
                                                      I 434: Gdf. *uedo.       Hiibschmann Arm. Gr.
Sandhiform zu uedor vgl. got. urdo, slav. voder, ihr entspricht auch das
                                                       ,

24055:Alb. Wb. 95); ahd weban „weben, flechten, spinnen“ (aucli „sicb fortwahrend
24101:     Ahd. weban       aucli ,,sich           fortwahrend hin und her bewegen
```


## [2026-10-16T05:16:46.034Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; sed -n '24030,24060p' WLD_Bd1_pages.txt | grep -v '^\\s*$' | cut -c1-200"
}
```


### [2026-10-16T05:16:46.325Z] TOOL RESULT

```
  Die Annahme von Kluge Et. Wb., daB gr. ortkov als idg. *uop-lo-m
liierher gehdre. ist utiwahrscheinlicb.
1.    uebh- „weben, tlechten, knupfen                               11
                                                                         .
     Ai. ubhndti ,    umbhdti,            zusammen", mit upn- und prd-
                                            undpti           „schniirt
,,bindet“,urna-rabhi-h „Spinne“ (eig. Wollweberin“; vgl. aisl. kqngur-rCifa                                                                         ,
ags. gangel-tvwfre „Spinne“): av. ubdaUna- „aus Webstoff, aus Zeug ge-
macht‘ (von einem *ubdu- „Gewebtes“, idg. *ubh-td-\ Bthl. Wb. 401). np.
hafad „er webt“ (ebda.); gr. erpt] „das \Veben“, infoioot, g 105, sonst v <pai-
rco „webe“, repo; n. „das Weben‘ (naek den vorigen aus * fig o„- utnvoka-
                                                              -
                                                              '
lisiert.  Frankel KZ. 42, 122 a 4;; alb. vert „ich webe“ ( *uebhni ?, G. Meyer
Alb. Wb. 95); ahd weban „weben, flechten, spinnen“ (aucli „sicb fortwahrend
bin und her bewegen“, s. *uebh- dieser Bed.), ags. tee fan „weben, flechten,
kniipf'en“, aisl. vefa „weben, flechten, schlingen“ (Ptc. oftnn); aisl. refju
'
  uobheio) „wickeln, hiillen“ (refl. vcfjast „hin und zuriick fahren“ wohl vom
```


## [2026-10-16T05:16:52.217Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://vajehyab.com/moein/بافتن' 'https://vajehyab.com/moein/باران' 'https://vajehyab.com/moein/بارگین'; do f=$(python3 tools/fetch_source.py \"$u\" --note \"page 527, Mo'in check\" | tail -1); grep -v '^\\s*$' $f | sed -n '/فرهنگ انتشارات معین/,+2p' | head -4; done; cd data/verification/sources/refs; grep -n 'بافتن\\|باران' incoming/ARY/ARY_pages.txt | head -6; grep -n -i 'vārān\\|varan\\b\\|wārān' NYB_vol2_glossary.txt | head -3; grep -n -i 'BAFTAN\\|BARAN\\b' incoming/ARY/ARY_latin_index_pages.txt | head"
}
```


### [2026-10-16T05:16:53.706Z] TOOL RESULT

```
TITLE: معنی بافتن | فرهنگ انتشارات معین | واژه یاب
معنی بافتن | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 فرهنگ انتشارات معین
TITLE: معنی باران | فرهنگ انتشارات معین | واژه یاب
معنی باران | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 فرهنگ انتشارات معین
2144:۶ / ابر (به چم *دمه‌ی باران")
3042:۶ بافتن» بافت
7546:چم این واژه در زبان آلمانی کهن» ابسلندی کهن و فریزی کهن: باران» آب را کد.
8211:چم این واژه در زبان‌های اسلاوی: هوای بد و بارانی» باران.
2175:kamakéh abstr. of bahuvrihi compounds with kāmak (v. above no 3): pat ménói m in the state of being a mönöi-kämak, one whose will is determined by Heaven, 4. e., in accomplishment of the will of the heavenly beings 40??, with the gl. cigön mēnēyān apäyist, v. apāytstan; purr--~ i o ahläyeh whole-hearted devotion to Righteousness 55? (purr-kämak whose will is full, perfect); @z-~ indulging in covetousness 681 (āz-kāmak addicted to Gz); andkeh-— il will, malignity 7215 (anākēh-kāmak, v. above no. 3); varan-~ kartan to indulge in lustfulness 8411; raväk- the state, or work, of one whose
2374:magu-pat [mgwpt'] chief of the Magi, or: chief Magian, of the head of the Zoroas- trian priesthood 1104; in this sense com- monly ~-dn ~ 10-12, passim; 168. 100?; — a Zoroastrian priest of this class in general: dastavardn u dätavaran u hēr- patün u ~-dn 1078, — The Olr form preserved as an archaic spelling; the authentic Milr forms are: 1. NW mogpat, Arm. lw. mogpet; 2. SW movpat, Arm. lw. also movpet (Etiša), Syr. lw. mwpt?, mwhpt’, mwhbi? ; NP mobad. V. s. v. ‘pat.
2452:markiisan brought about by the dev. Marküs: vārān + ~ 971. — Paz. malakésq, markösq (Mx).
2937:OURON GREEK) gl» BARIN, BARAN (KURDISH) 52,5
2938:URINA LATIN) o3Y BARAN 4AFGHANI) (4) sbi!
3579:BARAN, BARANEK (POLISH) gt} VARRAN
```


## [2026-10-16T05:16:56.828Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; awk 'NR<=3042 && /\\[pdf page/ {t=$0} NR==3042{print t; exit}' ARY_pages.txt; sed -n '3025,3045p' ARY_pages.txt; grep -n 'باریدن\\|بارش' ARY_pages.txt | head -3; awk 'NR<=2937 && /\\[pdf page/ {t=$0} NR==2937{print t; exit}' ARY_latin_index_pages.txt"
}
```


### [2026-10-16T05:16:57.227Z] TOOL RESULT

```
[pdf page 105]
آلباثی (7فال(مقام): ار با برهان قاطع + ۱۵
یادداشت:
معنی این واژه در زبان ارمنی: باتلاتی, ۱
معنی این واژه در زبان‌های تخاری: آب.
معنی اين واژه در زبان پروسی کهن: استخر.
معنی این واژه در زبان انگلیسی کهن: مرطوب» دریا,
معنی این واژه در زبان‌های رمانس و بونانی؛ پیشاب. 0 اخ
اوستایی (45874۸): ۷۸2 پسگشت‌ها شب رد۲
پهلری (//ماللهم): ۰" 3 ,822۸ 700220
سانسکریت (5/077/ه5): کدفقنج 18 8۸00
۳ بای 60880 ار ۳/5 برهان قاطع : ۷
ی
راگیس سوازی اج را 890
اوستایی ‎ 827۸10811,)48574(/(‏ و882 پارسی‌باستان (/۳84۸ 010):
3 -8۸821 ,828۸1813 ,8271573
سا
[pdf page 105]
۶ بافتن» بافت
پهلوی (1اللهه): ه3 ,81706
تخار ی ۸ (۸ متام 7)," 20 نررس کهن (۸088 01): 00
تخاری 8 (8 7087۸7/4(۷): ۳0168 ,۳۸04 آلمانی کهن (انمانتهی :8700
[pdf page 103]
```


## [2026-10-16T05:17:22.861Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; grep -l 'moein/بافتن\\|moein/باران' web/index.jsonl >/dev/null; for w in بافتن باران; do f=$(grep \"moein/$w\\\"\" web/index.jsonl | tail -1 | python3 -c \"import json,sys;print(json.loads(sys.stdin.read())['file'])\"); grep -v '^\\s*$' $f | sed -n '/^ فرهنگ انتشارات معین/,+1p'; done; grep -n -i 'vāra\\|vara-, .rain\\|Avestic var' refs/KLN_1971.txt | head -5; sed -n '265317,265330p' refs/KLN_1971.txt"
}
```


### [2026-10-16T05:17:23.324Z] TOOL RESULT

```
ugrep: warning: data/verification/sources/web/8ee57095b72ee3ab.txt: No such file or directory
ugrep: warning: data/verification/sources/web/afba3cf776af6cb3.txt: No such file or directory
132734:*wollc-o-, whence also Avestic var s sa~, ModPers. 
261007:vf ttih y ‘the act of rolling’, Avestic var*t-, ‘to 
268217:whence also OI. urnd, Avestic var^na, Arm. 
268294:whence also Avestic var e za, ‘work, activity’, 
water, n, — ME. water, fr. OE. waster, rel. to OS. 
watar , OFris. wetir, weter, wetter, LG., Du. 
water , OHG. wa^ar, MHG. wajjer, G. Wasser, 
ON. vatn, Swed. vat ten, Dan. vand, Goth, wato, 
‘water’, OE. wxt, ‘wet’, fr. I.-E. base *wxd 
*wdd-, *ud -, ‘water’, whence also Hitt, watar, 
gen. wetenash , ‘water’, OI. udnab , uddn-, uda - 
kdm, ‘water’, anudrdh , ‘waterless’, utsah, ‘source’, 
unddti , undtti, ‘it sprinkles, moistens’, Gk. 
tfSop, ‘water’, uSpta, ‘waterpot, pitcher’, <Scvu- 
Spo?, ‘waterless’, OSlav., Russ., etc., voda, 
‘water’, Lith. vandud , ‘water’, Lett, tide ns, 
OPruss. wundan, unds, ‘water’. Arm. get (for 
*wedd-), ‘river’. Alb. uje, ‘water’, L. unde i, ‘wave’,
```


## [2026-10-16T05:17:28.183Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -h 'moein/ب' index.jsonl | tail -4 | cut -c1-250; for f in $(grep -h 'moein/ب' index.jsonl | python3 -c \"import json,sys;[print(json.loads(l)['file']) for l in sys.stdin]\"); do echo \"## $f\"; grep -v '^\\s*$' ../../../../$f 2>/dev/null | sed -n '/^ فرهنگ انتشارات معین/,+1p'; done"
}
```


### [2026-10-16T05:17:28.710Z] TOOL RESULT

```
{"url": "https://vajehyab.com/moein/بزرگ", "file": "data/verification/sources/web/28489330988df176.txt", "fetched": "2026-10-16T05:16:30Z", "status": 200, "bytes": 896, "title": "معنی بزرگ | فرهنگ انتشارات معین | واژه یاب", "note": "page 530, root We
{"url": "https://vajehyab.com/moein/بافتن", "file": "data/verification/sources/web/8ee57095b72ee3ab.txt", "fetched": "2026-10-16T05:16:52Z", "status": 200, "bytes": 801, "title": "معنی بافتن | فرهنگ انتشارات معین | واژه یاب", "note": "page 527, Mo'in
{"url": "https://vajehyab.com/moein/باران", "file": "data/verification/sources/web/afba3cf776af6cb3.txt", "fetched": "2026-10-16T05:16:53Z", "status": 200, "bytes": 851, "title": "معنی باران | فرهنگ انتشارات معین | واژه یاب", "note": "page 527, Mo'in
{"url": "https://vajehyab.com/moein/بارگین", "file": "data/verification/sources/web/cc7f62fa95c5b0fd.txt", "fetched": "2026-10-16T05:16:53Z", "status": -1, "bytes": 39, "title": "", "note": "page 527, Mo'in check"}
## data/verification/sources/web/93a0defd9ef37424.txt
 فرهنگ انتشارات معین
 (رُ مِ) [ فر. ] ( اِ.) اسبابی برای اندازه گیری فشار جو، فشارسنج هوا، فشار - سنج . (فره ).
## data/verification/sources/web/859649cb8f47d7be.txt
 فرهنگ انتشارات معین
 (بِ گُ) [ تر. ] (ص . اِ.) خانم ، خاتون ، بانو.
## data/verification/sources/web/a094991cc6741808.txt
 فرهنگ انتشارات معین
 (بِ رِ) [ فر. ] ( اِ.) الماس تراش داده شده .
## data/verification/sources/web/8cfc1567f0ea1f6f.txt
 فرهنگ انتشارات معین
 (بُ یا بَ) [ معر. ] ( اِ.) 1 - نوعی شیشه که از ترکیب سیلیکات دوپتاسیم و سیلیکات دوپلمب ساخته شود. 2 - کنایه از: شفاف .
## data/verification/sources/web/b74b6f999025d0d1.txt
 فرهنگ انتشارات معین
 [ فر. ] ( اِ.) اجسامی جامد و سفیدرنگ و بسیار نمگیر که در آب بسیار حل می شوند و در اثر گرما خیلی زود گداخته می گردند.
## data/verification/sources/web/a0d4534b43fc6930.txt
 فرهنگ انتشارات معین
 (ش ِ) ( اِ.) یکی از پرندگان شکاری کوچکتر از باز، با چشمانی زرد رنگ ، که رنگ پشتش خاکستری تیره و شکمش سفید با لکه های حنایی است . قرقی ، قوش .
## data/verification/sources/web/28489330988df176.txt
 فرهنگ انتشارات معین
 (بُ زُ) (ص .) 1 - دارای حجم ، وسعت یا کمیت زیاد. 2 - برجسته ، نمایان . 3 - بالغ ، بزرگسال . 4 - دارای سن بیشتر. 5 - عنوان احترام آمیز برای پدر، مادر، دایی و... 6 - رییس ، پیشوا.
## data/verification/sources/web/8ee57095b72ee3ab.txt
 فرهنگ انتشارات معین
 (تَ) (مص م .) 1 - رشته های نخ یا پشم را به هم تابیدن . 2 - سخنان دروغ گفتن .
## data/verification/sources/web/afba3cf776af6cb3.txt
 فرهنگ انتشارات معین
 ( اِ.) قطره های آبی که به صورت پیاپی از ابر می بارد. مجازاً: ریزش فراوان و پیاپی چیزی . ؛ ~ آمدن و خون شستن کنایه از: بلای عظیم آمدن و باعث قتل عام شدن .
## data/verification/sources/web/cc7f62fa95c5b0fd.txt
```


## [2026-10-16T05:17:34.864Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; wc -c c6db3e67f7fc0a16.txt b3fdeec23f646c0c.txt; grep -m2 -i 'from Middle English\\|From Latin\\|Proto-Italic' c6db3e67f7fc0a16.txt b3fdeec23f646c0c.txt | cut -c1-300"
}
```


### [2026-10-16T05:17:35.257Z] TOOL RESULT

```
26909 c6db3e67f7fc0a16.txt
24529 b3fdeec23f646c0c.txt
51438 total
c6db3e67f7fc0a16.txt: Inherited from Middle English wappes , waps , wasp , waspe , from Old English wæfs , wæps , wæsp , from Proto-West Germanic *wapsu , from Proto-Germanic *wapsō ( “ wasp ” ) , from Proto-Indo-European *wóbʰseh₂ ( “ wasp ” ) , from *webʰ- ( “ to braid, weave ” ) , referring to th
c6db3e67f7fc0a16.txt: Metathesis of /s/ and /p/ was both a process of some generality within English (compare grasp from Middle English grapsen , and—affecting other plosives— ascian ~ acsian ( “ to ask ” ) ) and common in the reflexes of *wóps-eh₂ ( “ wasp ” ) in particular, as the aforementioned G
b3fdeec23f646c0c.txt: Inherited from Old Catalan vespa , from Latin vespa .
b3fdeec23f646c0c.txt: Inherited from Latin vespa
```


## [2026-10-16T05:17:37.512Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -A3 '^ *Latin *$' b3fdeec23f646c0c.txt | head; grep -i -m3 'Proto-Italic\\|wospā\\|metathes' b3fdeec23f646c0c.txt | cut -c1-300"
}
```


### [2026-10-16T05:17:37.919Z] TOOL RESULT

```
 Latin 

 Toggle Latin subsection 

--
 Latin
 [ edit ] 

 Etymology
 Inherited from Proto-Italic *wospā , metathesized from earlier *wopsā , from Proto-Indo-European *wóbʰseh₂ , from *webʰ- ( “ to weave ” ) . ( Can this ( + ) etymology be sourced ?) Cognate with English wasp .
 Categories : Catalan terms derived from Proto-Italic 
 Catalan terms inherited from Proto-Italic
```


## [2026-10-16T05:17:40.378Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; mkdir -p data/verification/sources/refs/ocr/BOOK; pdftoppm -f 527 -l 527 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf data/verification/sources/refs/ocr/BOOK/527 && ls -la data/verification/sources/refs/ocr/BOOK/527.png"
}
```


### [2026-10-16T05:17:42.012Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   90k sfmqrb 16 Oct 01:17  data/verification/sources/refs/ocr/BOOK/527.png
```


## [2026-10-16T05:20:43.232Z] TOOL CALL #55: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-527.py",
 "content": "import json\n\nW_WEBH = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/webʰ-\"\nW_WOBH = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wobʰseh₂\"\nW_BAFTAN = \"https://en.wiktionary.org/wiki/بافتن\"\nW_BARAN = \"https://en.wiktionary.org/wiki/باران\"\nW_WASP = \"https://en.wiktionary.org/wiki/wasp\"\nW_VESPA = \"https://en.wiktionary.org/wiki/vespa\"\nW_WODR = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wódr̥\"\nW_VASEL = \"https://en.wiktionary.org/wiki/vaseline\"\nAB_VARDIJ = \"https://abadis.ir/fatofa/وردیج/\"\nDK_VARDIJ = \"https://vajehyab.com/dehkhoda/وردیج\"\nMO_VAZ = \"https://vajehyab.com/moein/وازلین\"\nMO_PARGIN = \"https://vajehyab.com/moein/پارگین\"\nMO_BAFTAN = \"https://vajehyab.com/moein/بافتن\"\nMO_BARAN = \"https://vajehyab.com/moein/باران\"\n\ndef rc(ref, status, note):\n    return {\"ref\": ref, \"status\": status, \"note\": note}\n\ndef co(src, where, stance, note):\n    return {\"src\": src, \"where\": where, \"stance\": stance, \"note\": note}\n\nOEW_NC = lambda r: rc(r, \"not_checked\", \"Shipley, Origins of English Words: lending-only scan, no local text.\")\nAEF_NC = lambda r: rc(r, \"not_checked\", \"Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi: not online; it is the Persian translation of Horn, whose entry (HRN no. 159) was checked instead.\")\n\nPOK_WEBH = rc(\"POK:1114\", \"supports\", \"POK_full.txt line ~88697 (Page(s): 1113/1114), lemma 'uebh-1 to weave, plait': 'Avestan ubdaena- aus Webstoff, aus Zeug gemacht ... np. bafad er webt; ... Old High German weban, Old English wefan ... weft ... Old English webb'; ends 'in addition *uobhsa wasp'.\")\nPOK_WOBH = rc(\"POK:1179\", \"supports\", \"POK_full.txt line ~93160, lemma 'uobhsa wasp': 'Avestan vawzaka- scorpion, but Iran. *vawza- wasp in Middle Persian vabz wasp, Baluchi gvabz bee, wasp ... Latin vespa (from *vopsa) ... Old English waefs, waeps, waesp, Old High German wefsa, wafsa'.\")\nPOK_WED = rc(\"POK:78\", \"supports\", \"POK_full.txt lines 7998-8299 (Page(s): 78-81), lemma 'au(e)-9, aued-, auer- to flow, to wet; water': 'Avestan aoδa- wellspring, fount'; 'Avestan vaidi- water run, irrigation canal'; 'Avestan udra- otter'; 'uer-: Old Indic var water, Avestan var rain ... Avestan vairi- sea'; 'Avestan varəšni- (= Old Indic vrsana- testicles)'.\")\nKLN_WEAVE = \"KLN_1971.txt line 265624 s.v. weave: 'OHG. weban ... from I.-E. base *webh-, to move to and fro ... to weave, whence also OI. ubhnati ... Avestic ubdaena, woven fabric, Pers. baftan, to weave ... Cp. wafer, wasp, wave, ... web, webster, weevil, weft, wobble, woof.'\"\nKLN_WASP = \"KLN_1971.txt line 265233 s.v. wasp: 'OE. waefs, waeps, waesp ... OHG. wafsa, wefsa ... cogn. with ... Avestic vawazaka-, scorpion (prop. a spiderlike animal), L. vespa ... All these words are derivatives of I.-E. base *webh-, *wobh-, to weave ... The wasp is called the weaver, in allusion to the weblike form of its nest.' (The local 1966 two-volume text breaks off at 'veratrine', so the 1971 edition text was used; page number therefore not matched to Nourai's 1731.)\"\n\nentries = []\n\n# ---------------- entry 0: Webh ----------------\ne0_nodes = [\n {\"id\": 1, \"lang\": \"Avestan\", \"words\": \"ubdaena\", \"verdict\": \"confirmed\",\n  \"derivation\": \"YAv. ubdaēna- 'made of woven stuff, of cloth' (Vd. 8.23 ff.) is an adjective from *ubda- 'woven' = zero grade *ubʰ-tó- of PIE *webʰ-, with the Bartholomae's-law cluster *bʰt > Iranian *bd. Nourai's gloss 'woven fabric' is close (Bartholomae: 'aus Webstoff, Zeug').\",\n  \"derivation_fa\": \"اوستایی ubdaēna- «ساخته‌شده از بافته، پارچه‌ای» صفتی است از *ubda- «بافته»، که بالانده (درجهٔ صفر) *ubʰ-tó- از ریشهٔ هندواروپایی آغازین *webʰ- «بافتن» است؛ خوشهٔ *bʰt در ایرانی به bd بدل شده است. بارتولومه و پوکورنی همین را می‌گویند؛ ادعای نورایی درست است.\",\n  \"sources\": [W_WEBH, W_BAFTAN],\n  \"ref_check\": [POK_WEBH],\n  \"consulted\": [\n   co(\"BRT\", \"BRT.txt line 8456\", \"supports\", \"'ubdaena- Adj. (fem. -nī-) aus Webstoff, Zeug' (V. 8.23).\"),\n   co(\"WLD\", \"Bd. I, WLD_Bd1_pages.txt line ~24033, s.v. 1. uebh-\", \"supports\", \"'av. ubdaena- aus Webstoff, aus Zeug gemacht (von einem *ubda- Gewebtes, idg. *ubh-to-; Bthl. Wb. 401). np. bafad er webt'.\"),\n   co(\"CHEUNG\", \"CHEUNG.txt line ~26100, *uab/f 'to weave'\", \"supports\", \"'YAv. ubdaena- made from woven material (V 8.23 ff.)'.\"),\n   co(\"AHD\", \"AHD_watkins1985.txt line 1126 s.v. webh-\", \"silent\", \"Lists Germanic, Greek huphe; no Iranian forms.\")]},\n {\"id\": 2, \"lang\": \"Persian\", \"words\": \"bâftan\", \"verdict\": \"confirmed\",\n  \"derivation\": \"NP bāftan / pres. stem bāf- 'to weave' < MP waf- (Book Pahlavi wp-, MacKenzie 'waf- weave'; Parthian wf-) < Proto-Iranian *wab-/*waf- < PIE *webʰ-. Initial Middle Persian w- became b- in New Persian (as in wād > bād), and the ā of bāf- is the Persian lengthened/causative-type vowel of the present stem; past stem bāft- with -ft- from the participle *wafta-. Derivatives bāfte, bāf, bāfandegi are regular.\",\n  \"derivation_fa\": \"«بافتن» (ستاک حال: باف) از فارسی میانهٔ waf- «بافتن» (پهلوی wp-، پارتی wf-) و ایرانی باستان *wab-/*waf- است، از ریشهٔ هندواروپایی *webʰ-. واو آغازی فارسی میانه در فارسی نو به «ب» بدل شده است (مانند wād ← باد). چونگ، هرن، مکنزی و معین در حواشی برهان همه همین را آورده‌اند و اوستایی ubdaēna- را هم‌ریشهٔ آن می‌دانند؛ ادعای نورایی درست است.\",\n  \"sources\": [W_BAFTAN, W_WEBH, MO_BAFTAN],\n  \"ref_check\": [\n   rc(\"HRN:38\", \"supports\", \"HRN.txt line 1844 (pp. 38-39) no. 168: 'bäften weben, baf ... aw. ubdaena- gewebt; skr. vergl. urna-vabhi- Spinne ... afγ. udal ... oss. vafyn ... bal. gvapag'.\"),\n   rc(\"BQT:2461\", \"supports\", \"ocr/BQT/2461.png (BQT vol. 5 'لغات متفرقه', pdf 544): Mo'in's note on بافتن: 'از: باف + تن (پسوند مصدری) ... اوستایی ubdaēna (بافته). سانسکریت ūrna-vābhi (عنکبوت) ... بلوچی ...'.\"),\n   rc(\"MON:1462\", \"partial\", \"Mo'in online (vajehyab): 'بافتن (تَ) (مص م.) ۱- رشته های نخ یا پشم را به هم تابیدن' — meaning confirmed; the online text omits the etymological tags of the print page.\"),\n   POK_WEBH, OEW_NC(\"OEW:424\")],\n  \"consulted\": [\n   co(\"CHEUNG\", \"CHEUNG.txt line 26122, *uab/f\", \"supports\", \"'BMP wp- /waf-/ to weave ... NWIR: NP baftan/baf-, Bal. gwapit ...'.\"),\n   co(\"PHD\", \"PHD_mackenzie.txt line 5134\", \"supports\", \"'waf- [wp- | P wf-, (N baf-)] weave.'\"),\n   co(\"NYB\", \"NYB_vol2_glossary.txt line 3904\", \"supports\", \"s.v. vaf 'sheaf': 'from *vāftan vāf-, NP bāftan bāf- to weave'.\"),\n   co(\"HUB\", \"HUB.txt grep 'baft'\", \"silent\", \"No separate entry found.\"),\n   co(\"ARY\", \"ARY_pages.txt [pdf page 105] line 3042\", \"supports\", \"Entry 'بافتن، بافت' under the weave root with Pahlavi and Tocharian forms (OCR rough).\"),\n   co(\"KLN\", \"KLN_1971 s.v. weave\", \"supports\", \"'Pers. baftan, to weave'.\")]},\n {\"id\": 3, \"lang\": \"Germanic\", \"words\": \"weban, wefta, wabila\", \"verdict\": \"confirmed\",\n  \"derivation\": \"OHG weban / OE wefan < Proto-Germanic *webaną 'to weave' (e-grade *webʰ-); OE wefta 'weft' < Gmc *weft- (AHD: *wefta-, Wiktionary *wiftiz); *wabila- 'web, honeycomb' (o-grade + -ila- suffix, MLG wāfel, MDu wafel) is AHD's Germanic form. All three are regular Germanic reflexes of PIE *webʰ- with Grimm's law *bʰ > *b (> f between vowels in OE).\",\n  \"derivation_fa\": \"این سه صورت ژرمنی همه از ریشهٔ *webʰ- هستند: *webaną «بافتن» (آلمانی علیای کهن weban، انگلیسی کهن wefan)، *wefta- «پود» (انگلیسی کهن wefta) و *wabila- «شان عسل، تار» با پسوند -ila-. bʰ هندواروپایی در ژرمنی طبق قانون گریم به b بدل شده است. واتکینز و پوکورنی آن‌ها را آورده‌اند؛ ادعای نورایی درست است.\",\n  \"sources\": [W_WEBH],\n  \"ref_check\": [rc(\"AHD\", \"supports\", \"AHD_watkins1985.txt line 1126 s.v. webh-: 'Germanic *weban in Old English wefan ... Germanic *wefta- in Old English wefta, weft ... Suffixed Germanic form *wabila-, web, honeycomb'.\")],\n  \"consulted\": [\n   co(\"POK\", \"p. 1114 uebh-1\", \"supports\", \"'Old High German weban ... Old English wefan ... weft ... Old High German waba, wabo Honigwabe'.\"),\n   co(\"WLD\", \"Bd. I line ~24055 s.v. 1. uebh-\", \"supports\", \"'ahd weban weben, flechten, spinnen ... ags. wefan'.\"),\n   co(\"KLN\", \"KLN_1971 s.v. weave, wafer\", \"supports\", \"'OHG. weban'; wafer: 'Frankish *wafel, rel. to MDu. wafel ... OHG. waba ... and to OE. wefan'.\"),\n   co(\"IEC\", \"IEC.txt grep 'webh|weave'\", \"silent\", \"No relevant entry found in the OCR.\")]},\n {\"id\": 4, \"lang\": \"English\", \"words\": \"weave, web, wave 1, Webster, wafer, woof, wobble\", \"verdict\": \"plausible\",\n  \"derivation\": \"weave < OE wefan; web < OE webb (*wabją); Webster < OE webbestre 'female weaver' (the surname is the occupational noun); wafer < ONF waufre < Frankish *wafla (Gmc *wabila- 'honeycomb'); woof < OE ōwef (ō- 'on' + wef), w- restored after weave. wave (verb, OE wafian) and wobble (LG wabbeln) are attached to *webʰ- by Watkins only as 'possibly Germanic *wab-, to move back and forth as in weaving' and by Klein via a sense 'to move to and fro'; Pokorny puts them under a separate root uebh-2 'to wander, roam, swarm' (p. 1114). So weave/web/webster/wafer/woof are secure; wave and wobble are possible but not certain.\",\n  \"derivation_fa\": \"weave، web، Webster (از webbestre «زنِ بافنده»)، wafer (از فرانسوی شمالی waufre، از فرانکی *wafla «شان عسل») و woof (از انگلیسی کهن ōwef) بی‌گمان از *webʰ- اند. اما wave «تکان دادن» و wobble «لق زدن» را واتکینز تنها «شاید» از همین ریشه (به معنای «پس‌وپیش رفتن چون ماکوی بافنده») می‌داند و پوکورنی آن‌ها را زیر ریشه‌ای جدا (uebh-2 «سرگردان بودن، جنبیدن») می‌آورد. پس ادعای نورایی برای بیشتر واژه‌ها درست و برای wave و wobble با احتیاط پذیرفتنی است.\",\n  \"sources\": [W_WEBH],\n  \"ref_check\": [rc(\"KLN\", \"supports\", KLN_WEAVE + \" Also s.v. wave: 'fr. I.-E. base *webh-, to move to and fro; to weave'; wobble: 'Rel. to LG. wabbeln ... See waver'; woof: 'OE. owef ... The initial w in woof is due to the influence of weave'.\"), OEW_NC(\"OEW:425\")],\n  \"consulted\": [\n   co(\"AHD\", \"line 1126 s.v. webh-\", \"partial\", \"WEAVE, WOOF, WEB, WEBSTER, WAFER, WAFFLE listed; 'Possibly Germanic *wab-, to move back and forth as in weaving, in: a. Old English wafian ... WAVE; b. Low German wabbeln ... WOBBLE'.\"),\n   co(\"POK\", \"p. 1114 uebh-2 'to wander, roam, swarm'\", \"contradicts\", \"Separate lemma: 'Old English wafian ... engl. wave, wobble, waver' — not under uebh-1 'weave'.\"),\n   co(\"SKT\", \"SKT.txt grep 'WEAVE|WOOF'\", \"silent\", \"OCR of the W section too garbled for these headwords.\")]},\n {\"id\": 5, \"lang\": \"Indo-European\", \"words\": \"Wopsâ\", \"verdict\": \"plausible\",\n  \"derivation\": \"PIE *wobʰsā (laryngeal notation *wóbʰseh₂) 'wasp' is securely reconstructed (Latin vespa, OE wæsp, Lith. vapsà, OCS osa, Av. vawžaka-). Its derivation from *webʰ- 'weave' (wasp as 'weaver' of its papery nest) is the standard view (Pokorny, Walde-Pokorny, Klein, Wiktionary 'usually derived'), via an s-stem *wébʰos 'web' and an o-grade derivative; Watkins' AHD lists wopsa as a separate root without the link. Gloss 'insects with web-shaped nests' reflects this etymology rather than the meaning, which is simply 'wasp'.\",\n  \"derivation_fa\": \"*wobʰsā (به نگارش امروزی *wóbʰseh₂) «زنبور» در هندواروپایی آغازین استوار است (لاتین vespa، انگلیسی wasp، لیتوانیایی vapsà). بیشتر ریشه‌شناسان (پوکورنی، والده–پوکورنی، کلاین، ویکی‌واژه) آن را از *webʰ- «بافتن» می‌دانند، چون زنبور لانهٔ کاغذی‌اش را «می‌بافد»؛ اما واتکینز آن را ریشه‌ای جدا آورده است. پیوند با «بافتن» با احتیاط پذیرفتنی است.\",\n  \"sources\": [W_WOBH, W_WASP],\n  \"ref_check\": [\n   rc(\"AHD:1550\", \"partial\", \"AHD_watkins1985: 'wopsa. Wasp. Metathesized form *wospa. 1. Germanic *wosp- ... WASP. 2. Latin vespa ... VESPIARY. [Pok. uobhsa 1179.]' — separate root, no link to webh-.\"),\n   POK_WOBH,\n   rc(\"KLN:1731\", \"supports\", KLN_WASP),\n   OEW_NC(\"OEW:425\")],\n  \"consulted\": [\n   co(\"WLD\", \"Bd. I line 24151\", \"supports\", \"'uobh(e)sa Wespe, zu uebh- weben, vom gespinstartigen Wespennest'.\"),\n   co(\"POK\", \"p. 1114 end of uebh-1\", \"supports\", \"'See also: ... in addition *uobhsa wasp'.\"),\n   co(\"SYN\", \"SYN.txt grep 'wasp'\", \"silent\", \"Buck has no dedicated wasp section found in OCR.\"),\n   co(\"IEC\", \"IEC.txt grep 'wobhs|wopsa|wasp'\", \"silent\", \"No entry found.\")]},\n {\"id\": 6, \"lang\": \"Iranian\", \"words\": \"vawža\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Proto-Iranian *wawžā/*wabža- 'wasp' < Proto-Indo-Iranian *wábžʰas < PIE *wóbʰsos (*bʰs > IIr. *bžʰ by Bartholomae's law/voicing assimilation). Pokorny writes 'Iran. *vawža-' on the basis of MP wabz and Baluchi gvabz 'bee, wasp'. The form is reconstructed (should be starred).\",\n  \"derivation_fa\": \"ایرانی باستان *wawža-/*wabža- «زنبور» از هندوایرانی *wábžʰas و هندواروپایی *wóbʰsos است؛ خوشهٔ bʰs در هندوایرانی به bžʰ (واک‌دار) بدل شده است. این صورت بازسازی‌شده است و گواهش فارسی میانهٔ wabz و بلوچی gvabz «زنبور» است. ادعای نورایی درست است.\",\n  \"sources\": [W_WOBH],\n  \"ref_check\": [POK_WOBH],\n  \"consulted\": [\n   co(\"WLD\", \"Bd. I line ~24152\", \"supports\", \"'Av. vawzaka- m. Name eines daevischen Tieres, baluci gvabz Biene, Wespe, Hornis (s. Geiger ..., Bthl. Wb. 1346)'.\"),\n   co(\"PHD\", \"PHD_mackenzie.txt line 5110\", \"supports\", \"'wabz [wpc, wpz] wasp.'\"),\n   co(\"BRT\", \"line 22439\", \"partial\", \"Only vawzaka- 'Name eines schädlichen Tiers' — the Iranian base is not given.\")]},\n {\"id\": 7, \"lang\": \"Avestan\", \"words\": \"vawžaka\", \"verdict\": \"plausible\",\n  \"derivation\": \"YAv. vawžaka- (Yt 5.90) is a -ka- derivative of Iranian *wawža- 'wasp'. Bartholomae only says 'name of a noxious (daevic) animal'; the meaning 'scorpion' is a conjecture (Pokorny, Klein 'prop. a spiderlike animal'). Formally the derivation is sound; the gloss 'scorpion' is uncertain, and it may simply mean 'wasp'.\",\n  \"derivation_fa\": \"اوستایی vawžaka- (یشت ۵، بند ۹۰) با پسوند -ka- از *wawža- «زنبور» ساخته شده است. بارتولومه تنها می‌گوید «نام جانوری زیان‌کار (دیوی)» است و معنای «کژدم» حدس پوکورنی و کلاین است. ساخت واژه درست است ولی معنای «کژدم» قطعی نیست؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [W_WOBH],\n  \"ref_check\": [POK_WOBH],\n  \"consulted\": [\n   co(\"BRT\", \"BRT.txt line 22439 (col. 1346)\", \"partial\", \"'vawzaka- m. Name eines schädlichen Tiers' (Yt 5.90) — no 'scorpion'.\"),\n   co(\"WLD\", \"Bd. I line ~24152\", \"partial\", \"'Av. vawzaka- m. Name eines daevischen Tieres'.\"),\n   co(\"KLN\", \"KLN_1971 s.v. wasp\", \"supports\", \"'Avestic vawazaka-, scorpion (prop. a spiderlike animal)'.\")]},\n {\"id\": 8, \"lang\": \"Pahlavi\", \"words\": \"vassz\", \"verdict\": \"transcription_suspect\",\n  \"derivation\": \"The book prints 'vassz', which is no Pahlavi word; it is Nourai's misprint for MP wabz (Book Pahlavi wpc/wpz) 'wasp' (MacKenzie; Pokorny 'Middle Persian vabz'). wabz continues Iranian *wabža-/*wawža- directly; it does not descend from Av. vawžaka- (a sister -ka- derivative), so the arrow should come from the Iranian node #6. The JSON reproduces the print faithfully.\",\n  \"derivation_fa\": \"کتاب «vassz» چاپ کرده که در پهلوی وجود ندارد؛ این خطای چاپی کتاب به جای فارسی میانهٔ wabz (نگارش پهلوی wpc/wpz) «زنبور» است (مکنزی؛ پوکورنی vabz). wabz مستقیماً از ایرانی باستان *wabža- است و از اوستایی vawžaka- (که خود مشتقی هم‌تراز است) نمی‌آید. خطای چاپی کتاب؛ استخراج درست است.\",\n  \"error_in\": \"book\", \"book_prints\": \"vassz\", \"correct_form\": \"wabz (vabz)\",\n  \"sources\": [W_WOBH],\n  \"ref_check\": [rc(\"POK:1179\", \"contradicts\", \"POK_full.txt line ~93162: 'Iran. *vawza- wasp in Middle Persian vabz wasp' — Pokorny has vabz, not 'vassz'.\")],\n  \"consulted\": [\n   co(\"PHD\", \"PHD_mackenzie.txt line 5110\", \"contradicts\", \"'wabz [wpc, wpz] wasp.' — the correct form.\"),\n   co(\"NYB\", \"NYB_vol2_glossary.txt grep 'wabz|wasp'\", \"silent\", \"No entry.\"),\n   co(\"WLD\", \"Bd. I line ~24152\", \"partial\", \"Gives Baluchi gvabz, cognate of MP wabz.\")]},\n {\"id\": 9, \"lang\": \"Germanic\", \"words\": \"wafsa, wosp\", \"verdict\": \"confirmed\",\n  \"derivation\": \"OHG wafsa/wefsa and OE wæfs/wæps/wæsp go back to Proto-Germanic *wabsō/*wapsō 'wasp' < PIE *wobʰsā (Grimm's law *bʰ > b, then devoicing before s). 'wosp' is Watkins' reconstructed metathesized Germanic *wosp- (from *wospā), not an attested word; wafsa is attested OHG.\",\n  \"derivation_fa\": \"آلمانی علیای کهن wafsa/wefsa و انگلیسی کهن wæfs/wæps/wæsp از ژرمنی آغازین *wabsō/*wapsō «زنبور» و آن از *wobʰsā است. «wosp» صورت بازسازی‌شدهٔ ژرمنی با قلب (جابه‌جایی s و p) است که واتکینز آورده، نه واژه‌ای گواهی‌شده. ادعای نورایی درست است.\",\n  \"sources\": [W_WASP, W_WOBH],\n  \"ref_check\": [rc(\"KLN:1731\", \"supports\", KLN_WASP), OEW_NC(\"OEW:425\")],\n  \"consulted\": [\n   co(\"AHD\", \"s.v. wopsa\", \"supports\", \"'Metathesized form *wospa. 1. Germanic *wosp- in Old English wesp, weps, wasp'.\"),\n   co(\"POK\", \"p. 1179\", \"supports\", \"'Old English waefs, waeps, waesp, Old High German wefsa, wafsa, waspa'.\"),\n   co(\"WLD\", \"Bd. I line 24151\", \"supports\", \"uobh(e)sa Wespe with Germanic reflexes.\")]},\n {\"id\": 10, \"lang\": \"English\", \"words\": \"wasp\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English wasp < ME waspe < OE wæsp, a metathesized variant of wæps/wæfs < Proto-West Germanic *wapsu < PGmc *wapsō; the sp/ps metathesis is common in this word across Germanic and in Latin vespa.\",\n  \"derivation_fa\": \"انگلیسی wasp از انگلیسی میانه waspe و انگلیسی کهن wæsp است که صورت قلب‌شدهٔ wæps/wæfs است، از ژرمنی *wapsō. ادعای نورایی درست است.\",\n  \"sources\": [W_WASP],\n  \"ref_check\": [rc(\"KLN:1731\", \"supports\", KLN_WASP)],\n  \"consulted\": [\n   co(\"AHD\", \"s.v. wopsa\", \"supports\", \"'Old English wesp, weps, wasp: WASP'.\"),\n   co(\"SKT\", \"SKT.txt line 21208 'WASP.'\", \"silent\", \"Headword present but entry text garbled in OCR.\")]},\n {\"id\": 11, \"lang\": \"Latin\", \"words\": \"vepsa, vespa\", \"verdict\": \"plausible\",\n  \"derivation\": \"Latin vespa 'wasp' < Proto-Italic *wospā, metathesized from *wopsā < PIE *wobʰsā (with e for o, perhaps by analogy). 'vepsa' is not attested Latin; it is Klein's reconstructed pre-form *vepsa and should be starred. Gloss '\\\"weaver\\\" insect' is the etymological meaning, not the Latin meaning.\",\n  \"derivation_fa\": \"لاتین vespa «زنبور» از ایتالیک آغازین *wospā است که با قلب از *wopsā آمده، از هندواروپایی *wobʰsā. «vepsa» واژهٔ گواهی‌شدهٔ لاتین نیست و صورت بازسازی‌شدهٔ کلاین (*vepsa) است. vespa درست است؛ vepsa تنها به‌عنوان صورت فرضی پذیرفتنی است.\",\n  \"sources\": [W_VESPA, W_WOBH],\n  \"ref_check\": [rc(\"KLN:1731\", \"supports\", \"KLN_1971.txt line 261318 s.v. vespiary: 'L. vespa, wasp, which prob. was metathesized fr. *vepsa, fr. I.-E. *wobh-sa, fr. base *webh-, *wobh-, to weave' — vepsa is starred in Klein.\"), OEW_NC(\"OEW:425\")],\n  \"consulted\": [\n   co(\"POK\", \"p. 1179\", \"supports\", \"'Latin vespa f. wasp (from *vopsa)'.\"),\n   co(\"LAT\", \"LAT.txt grep 'vespa'\", \"silent\", \"Not checked in detail; Pokorny/AHD suffice.\"),\n   co(\"AHD\", \"s.v. wopsa\", \"supports\", \"'Latin vespa, wasp: VESPIARY'.\")]},\n {\"id\": 12, \"lang\": \"English\", \"words\": \"vespiary\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English vespiary 'wasps' nest' is a 19th-c. learned formation from Latin vespa on the model of apiary (Latin apiārium from apis 'bee').\",\n  \"derivation_fa\": \"انگلیسی vespiary «لانهٔ زنبور» واژه‌ای ساختگیِ عالمانه از لاتین vespa به قیاس apiary (کندوی زنبور عسل) است. ادعای نورایی درست است.\",\n  \"sources\": [W_VESPA],\n  \"ref_check\": [rc(\"KLN:1731\", \"supports\", \"KLN_1971.txt line 261318: 'vespiary, n., a wasps' nest. — Formed on analogy of apiary fr. L. vespa'.\")],\n  \"consulted\": [\n   co(\"AHD\", \"s.v. wopsa\", \"supports\", \"'Latin vespa, wasp: VESPIARY'.\"),\n   co(\"SKT\", \"SKT.txt grep 'vespiary'\", \"silent\", \"Not in Skeat.\")]},\n]\n\nentries.append({\n \"entry\": 0, \"root\": \"Webh\", \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *webʰ- 'to weave, braid' (Pokorny uebh-1, p. 1114; AHD webh-)\",\n \"note\": \"Root, language and gloss correct. Weak points: wave/wobble (#4) are only possibly from this root (Pokorny has a separate uebh-2); the derivation of the wasp word (#5) from 'weave' is standard but not certain; the Pahlavi form 'vassz' (#8) is a misprint in the book for wabz, and wabz descends from Iranian *wabža- rather than from Av. vawžaka-.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *webʰ- «بافتن» (پوکورنی ۱۱۱۴، واتکینز) درست است و «بافتن» فارسی و weave انگلیسی هر دو از آن‌اند. اما wave و wobble تنها احتمالاً به این ریشه می‌رسند، پیوند «زنبور» با «بافتن» رایج ولی قطعی نیست، و صورت پهلوی «vassz» خطای چاپی کتاب به جای wabz «زنبور» است.\",\n \"sources\": [W_WEBH, W_WOBH],\n \"ref_check\": [POK_WEBH],\n \"consulted\": [\n  co(\"AHD\", \"line 1126 s.v. webh-\", \"supports\", \"'webh-. To weave, also to move quickly ... [Pok. uebh- 1114.]'\"),\n  co(\"WLD\", \"Bd. I line ~24032\", \"supports\", \"'1. uebh- weben, flechten, knüpfen'.\"),\n  co(\"CHEUNG\", \"*uab/f 'to weave'\", \"supports\", \"Iranian reflexes listed.\"),\n  co(\"IEC\", \"IEC.txt grep\", \"silent\", \"No entry found in OCR.\")],\n \"nodes\": e0_nodes})\n\n# ---------------- entry 1: Wed ----------------\nBRT_VAR = \"BRT.txt line 23486: 'vār- m. 1) Regen ... 2) Regentropfen' and line 23487 'ai. vār- n. Wasser, np. bār-ān Regen. — Pü.: vārān'.\"\ne1_nodes = [\n {\"id\": 1, \"lang\": \"Avestan\", \"words\": \"vâr 1, wâr, vâra 1\", \"verdict\": \"confirmed\",\n  \"derivation\": \"YAv. vār- m. 'rain, raindrop' and vāra- 'rain' (with the verb var- 'to rain', vārənti-) are cognate with Skt. vār/vāri 'water', Luwian wār 'water', ON vari 'liquid'. Modern reconstructions give PIE *weh₁r-/*wer- 'water' (Wiktionary), which Pokorny folds into his 'au(e)-, aued-, auer-' complex; this is a different root from *wed- of 'water/wet', so the attachment to 'Wed' depends on Pokorny's lumping. 'wâr' is just an alternative transliteration.\",\n  \"derivation_fa\": \"اوستایی vār- «باران، قطرهٔ باران» و vāra- «باران» (با فعل var- «باریدن») هم‌ریشه با سنسکریت vār «آب» است. امروز ریشهٔ آن را *weh₁r-/*wer- «آب» می‌دانند که پوکورنی در گروه بزرگ «au(e)-, aued-, auer-» گنجانده است، نه همان *wed- «آب، تر». واژه و معنا درست است؛ ادعای نورایی درست است، با این توضیح که ریشهٔ دقیق آن جداست.\",\n  \"sources\": [W_BARAN],\n  \"ref_check\": [POK_WED, rc(\"KLN:1682\", \"not_checked\", \"Klein 1966 p. 1682 lies in the part of the local 1966 text that is cut off ('veratrine' is the last entry); the 1971 text has no clear Avestan 'vara rain' hit (grep 'Avestic var').\")],\n  \"consulted\": [\n   co(\"BRT\", \"col. ~1407\", \"supports\", BRT_VAR),\n   co(\"WLD\", \"Bd. I line 25200\", \"supports\", \"'av. vairi- m. See (aus *uar-) ... vār- Regen, vārənti-ca sie lassen regnen'.\"),\n   co(\"AHD\", \"AHD_watkins1985 s.v. wers-2\", \"silent\", \"AHD lists wed-1 and wers-2 separately; no Avestan forms.\")]},\n {\"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"vârân, vârîtan\", \"verdict\": \"confirmed\",\n  \"derivation\": \"MP wārān 'rain' (Book Pahlavi wʾlʾn', Manichaean wʾrʾn) = wār- + -ān, and wārīdan, pres. wār- 'to rain' (Book Pahlavi wʾl-ytn') continue Old Iranian *wār-/*wāra- 'rain' (Av. vār-, vāra-).\",\n  \"derivation_fa\": \"فارسی میانهٔ wārān «باران» (wār- + پسوند -ān) و wārīdan «باریدن» از ایرانی باستان *wār- «باران» (اوستایی vār-) آمده‌اند. مکنزی هر دو را با برابر فارسی نو «باران، باریدن» آورده است. ادعای نورایی درست است.\",\n  \"sources\": [W_BARAN],\n  \"ref_check\": [\n   rc(\"BQT:218\", \"not_checked\", \"BQT vol. 1 p. 218 is not covered by the scans (ref_page.py: 'no scan of BQT covers printed page 218'); grep of BQT_v1_pages.txt OCR for باران not attempted further.\"),\n   AEF_NC(\"AEF:209\")],\n  \"consulted\": [\n   co(\"PHD\", \"PHD_mackenzie.txt lines 5184, 5206\", \"supports\", \"'wārān [wʾlʾn' | M wʾrʾn, N bārān] rain'; 'wārīdan, wār- [wʾl-ytn' | M wʾr-yst, N bārīdan] rain'.\"),\n   co(\"NYB\", \"NYB_vol2_glossary.txt line 2452\", \"partial\", \"'vārān' occurs in the glossary (s.v. markūsān); no separate lemma found.\"),\n   co(\"HRN\", \"HRN.txt line 1767 no. 159\", \"supports\", \"'phlv. vārān, vārīdan, vārišn ...'.\")]},\n {\"id\": 3, \"lang\": \"Persian\", \"words\": \"bârân; bârgîn\", \"verdict\": \"plausible\",\n  \"derivation\": \"bārān 'rain' < MP wārān with New Persian w- > b- (as in wād > bād); bāridan, bāreš, bārandegi are regular derivatives. bārgīn / pārgīn: Horn (no. 159) lists bārgīn among the derivatives of bārān, i.e. 'place where rain water collects'; Mo'in defines پارگین as 'sewer, cesspool; rubbish pit', and the -gīn element is obscure, so the rain connection of bārgīn is possible but not proven.\",\n  \"derivation_fa\": \"«باران» از فارسی میانهٔ wārān است و واو آغازی در فارسی نو به «ب» بدل شده (مانند wād ← باد)؛ «باریدن»، «بارش» و «بارندگی» مشتقات منظم آن‌اند. «بارگین/پارگین» را هرن در کنار «باران» آورده («آبگیر آب باران»)، ولی معین «پارگین» را «فاضلاب، آشغال‌دانی» معنا کرده و جزء «-گین» روشن نیست؛ پس پیوند آن با «باران» ممکن است ولی قطعی نیست. «باران» درست است، «بارگین» با احتیاط پذیرفتنی است.\",\n  \"sources\": [W_BARAN, MO_BARAN, MO_PARGIN],\n  \"ref_check\": [\n   rc(\"BQT:218\", \"not_checked\", \"Printed p. 218 (vol. 1) not covered by the available scans per ref_page.py.\"),\n   AEF_NC(\"AEF:209\")],\n  \"consulted\": [\n   co(\"HRN\", \"HRN.txt line 1767 (p. 37) no. 159\", \"supports\", \"'bārān Regen, bārīden regnen, bāriš, bārgīn ... aw. vāra- Regen ... phlv. vārān, vārītan'.\"),\n   co(\"MON\", \"vajehyab.com/moein/باران ; /پارگین\", \"partial\", \"باران: 'قطره های آبی که به صورت پیاپی از ابر می بارد'; پارگین: '۱- فاضلاب. ۲- آشغال دانی' — no etymology online.\"),\n   co(\"ARY\", \"ARY_pages.txt [pdf page 103-105]\", \"supports\", \"Block under the water/rain root with Avestan vār- and Pahlavi forms and 'باران' notes (OCR rough).\"),\n   co(\"HUB\", \"HUB.txt grep 'bārān|baran'\", \"silent\", \"No entry found.\"),\n   co(\"PHD\", \"line 5184\", \"supports\", \"'wārān ... N bārān'.\")]},\n {\"id\": 4, \"lang\": \"Avestan\", \"words\": \"udra\", \"verdict\": \"plausible\",\n  \"derivation\": \"YAv. udra- m. 'otter' < PIE *udró- 'water animal' (zero grade of *wed- + -ro-), cognate with Skt. udra-, Greek hýdros 'water snake', OE otor 'otter', Lith. ūdra. The word and its derivation are correct, but Nourai's gloss 'water bird' is wrong: it is the otter (Bartholomae 'Otter, Fischotter'), not a bird.\",\n  \"derivation_fa\": \"اوستایی udra- «سمور آبی، شنگ» از هندواروپایی *udró- «جانور آبی» (درجهٔ صفر *wed- با پسوند -ro-) است و هم‌ریشهٔ سنسکریت udra-، یونانی hýdros و انگلیسی otter. واژه و ریشه درست است، اما معنای «پرندهٔ آبی» که نورایی داده نادرست است؛ بارتولومه آن را «سمور آبی» معنا کرده است.\",\n  \"sources\": [W_WODR],\n  \"ref_check\": [rc(\"POK:78\", \"supports\", \"POK_full.txt (pp. 78-81): 'udro-s water animal: Old Indic udra-h a water animal = Avestan udra- m. otter'.\")],\n  \"consulted\": [\n   co(\"BRT\", \"BRT.txt line 8215\", \"contradicts\", \"'udra- m. Otter, Fischotter' — an otter, not a water bird.\"),\n   co(\"WLD\", \"Bd. I line ~23571\", \"supports\", \"'= av. udra- m. Otter, Fischotter'.\"),\n   co(\"AHD\", \"s.v. wed-1 §7\", \"supports\", \"'*ud-ro-, water animal ... Germanic *otraz, otter'.\"),\n   co(\"IEC\", \"IEC.txt grep 'udro'\", \"silent\", \"Not checked beyond grep.\")]},\n {\"id\": 5, \"lang\": \"Pahlavi\", \"words\": \"vartak 2\", \"verdict\": \"disputed\",\n  \"derivation\": \"Pahlavi wartak/wardag means 'quail', not 'a water bird', and is not from Av. udra- 'otter'. It continues Indo-Iranian *wartaka-/*wartikā- 'quail' (Skt. vartaka-, vartikā-), cognate with Greek ortyx 'quail', from PIE *wértok-/*wr̥tok-. Horn (p. 242, cited by Nourai) gives exactly this: 'phlv. vartak ... ai. vartikā Wachtel; gr. ortyx'.\",\n  \"derivation_fa\": \"پهلوی wartak به معنای «بلدرچین» است، نه «پرندهٔ آبی»، و از اوستایی udra- «سمور آبی» نمی‌آید. این واژه از هندوایرانی *wartaka-/*wartikā- «بلدرچین» (سنسکریت vartikā-) و هم‌ریشه با یونانی ortyx «بلدرچین» است. خودِ هرن، که نورایی به او ارجاع داده، همین را می‌گوید؛ پژوهش امروزی پیوند آن با ریشهٔ «آب» را رد می‌کند.\",\n  \"sources\": [AB_VARDIJ],\n  \"ref_check\": [rc(\"HRN:242\", \"contradicts\", \"HRN.txt leaf 263 (p. 242) no. 1078: 'verdīj Wachtel, verdej, verdij, vertek. ai. vartikā Wachtel; phlv. vartak (Papyrus, Horn ZDMG 43, 50); gr. ortyx; kurd. verdī ...' — quail, from the Skt./Gk. quail word, not from udra.\")],\n  \"consulted\": [\n   co(\"HUB\", \"HUB.txt line 5799\", \"contradicts\", \"'vardīj Wachtel, skr. vartikā-, vartaka-'.\"),\n   co(\"PHD\", \"PHD_mackenzie.txt grep 'quail|wartag'\", \"silent\", \"MacKenzie gives only karak 'quail'; no wartak.\"),\n   co(\"NYB\", \"NYB_vol2_glossary.txt grep 'wartak|quail'\", \"silent\", \"No entry.\")]},\n {\"id\": 6, \"lang\": \"Persian\", \"words\": \"vardîj\", \"verdict\": \"disputed\",\n  \"derivation\": \"NP vardīj (also vartij, vardaj, vartak) is 'quail' (بلدرچین, سلوی, 'a bird smaller than the partridge' — Borhan, Dehkhoda, Mo'in), continuing Pahlavi wartak < IIr. *wartaka-/*wartikā- 'quail' (Skt. vartikā, Greek ortyx), so it does not belong to the 'water' root at all. The variant in the chart, ودخین (BQT 2262), is a different word: Borhan describes it as 'a water animal with teeth and a long thin round body living in salty, murky waters, said to be blind (Hindi bubu)', with no etymology; it cannot be linked to vardīj phonetically.\",\n  \"derivation_fa\": \"«وردیج» (و نیز ورتیج، وردج، ورتک) به معنای «بلدرچین» (سلوی، «پرنده‌ای کوچک‌تر از تیهو») است، از پهلوی wartak و هندوایرانی *wartikā- «بلدرچین» (سنسکریت vartikā، یونانی ortyx)، و هیچ پیوندی با ریشهٔ «آب» یا اوستایی udra- ندارد. «ودخین» که در نمودار آمده واژهٔ دیگری است: برهان آن را «جانوری آبی، دندان‌دار، باریک و دراز، در آب‌های شور و تیره، نابینا» می‌خواند و ریشه‌ای برایش نمی‌دهد. پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n  \"sources\": [AB_VARDIJ, DK_VARDIJ],\n  \"ref_check\": [\n   rc(\"MON:5001\", \"contradicts\", \"Mo'in (quoted in Dehkhoda/abadis s.v. وردیج): 'ورتک. وردج. (فرهنگ فارسی معین) ... پرنده‌ای است کوچکتر از تیهو. بلدرچین. سلوی' — a quail, not a water bird. MON:5001 itself (vol. 5) not seen.\"),\n   rc(\"BQT:2262\", \"partial\", \"ocr/BQT/2262.png (+ 2262.vision.txt): only ودخین is on this page: 'جانوری است آبی و دندان دارد و گردی دارد باریک و دراز و پیوسته در آبهای شور و ناصاف و تیره میباشد. گویند نابیناست' — a water animal, but no link to vardīj or udra and no etymology.\")],\n  \"consulted\": [\n   co(\"HRN\", \"p. 242 no. 1078\", \"contradicts\", \"'verdīj Wachtel ... ai. vartikā; phlv. vartak; gr. ortyx'.\"),\n   co(\"HUB\", \"line 5799\", \"contradicts\", \"'vardīj Wachtel, skr. vartikā-, vartaka-'.\"),\n   co(\"BQT\", \"p. 2262\", \"partial\", \"ودخین = blind toothed water animal; not vardīj.\"),\n   co(\"ARY\", \"ARY_pages.txt grep 'وردیج'\", \"silent\", \"Not found.\")]},\n {\"id\": 7, \"lang\": \"Avestan\", \"words\": \"aoda; vaidi; vairi; varašnî\", \"verdict\": \"plausible\",\n  \"derivation\": \"aoδa- m. 'spring, source' (Bartholomae 'Quelle') < *h₂wod-/*awod- (cf. Skt. odman- 'wave'): confirmed. vaiδi- f. 'water course, irrigation canal' < nasal-less zero grade/e-grade of *wed- (Skt. unatti 'wets'): confirmed (Walde-Pokorny 'Wasserlauf, Bewässerungskanal'). vairi- m. 'lake, sea' (Bartholomae 'See'): confirmed, though it belongs to *wer-/*weh₁r- 'water' (Pokorny's uer-), not *wed-. varəšni- (varəšnay-) means 'ram, male (of sheep)' in Bartholomae, not 'testicles' — 'testicles' is the meaning of the Sanskrit cognate vṛṣaṇa-; it belongs to *h₁wers- 'rain, sprinkle' > 'male', a separate root grouped here by Pokorny.\",\n  \"derivation_fa\": \"اوستایی aoδa- «چشمه» و vaiδi- «جوی آب، کاریز» درست و از ریشهٔ *wed-/aued- «آب، تر کردن» اند. vairi- «دریاچه، دریا» درست است ولی به ریشهٔ *wer-/*weh₁r- «آب» می‌رسد. varəšni- در اوستایی به معنای «قوچ، نر» است، نه «بیضه»؛ معنای «بیضه» از هم‌ریشهٔ سنسکریتی vṛṣaṇa- است و ریشهٔ آن *h₁wers- «باریدن، پاشیدن» است که پوکورنی در همین گروه آورده. سه واژهٔ نخست درست است و چهارمی با معنای نادرست آمده است.\",\n  \"sources\": [W_WODR],\n  \"ref_check\": [POK_WED],\n  \"consulted\": [\n   co(\"BRT\", \"lines 2937, 22796, 23088\", \"partial\", \"'aoδa- m. Quelle' (supports); 'vairi- m. See' (supports); 'varəšnay- m. Männchen des Schafs, Widder' (contradicts the gloss 'testicles').\"),\n   co(\"WLD\", \"Bd. I lines ~23560, 25200\", \"supports\", \"'av. vaiδi- f. Wasserlauf, Bewässerungskanal'; 'av. vairi- m. See'.\"),\n   co(\"AHD\", \"s.v. wers-2 'To be wet'\", \"partial\", \"Separate root wers-2 (ouron 'urine'); no Avestan forms.\"),\n   co(\"IEC\", \"IEC.txt grep\", \"silent\", \"Not found.\")]},\n {\"id\": 8, \"lang\": \"Old High German\", \"words\": \"wazzar\", \"verdict\": \"confirmed\",\n  \"derivation\": \"OHG wazzar 'water' < Proto-Germanic *watōr < PIE *wódr̥ (o-grade of *wed- + r/n-stem suffix); Germanic *t became OHG zz by the High German consonant shift; modern German Wasser.\",\n  \"derivation_fa\": \"آلمانی علیای کهن wazzar «آب» از ژرمنی *watōr و هندواروپایی *wódr̥ (درجهٔ o از *wed-) است؛ t ژرمنی در جابه‌جایی همخوانی آلمانی علیا به zz بدل شده و امروز Wasser است. ادعای نورایی درست است.\",\n  \"sources\": [W_WODR],\n  \"ref_check\": [rc(\"AHD\", \"supports\", \"AHD_watkins1985.txt line 1127 s.v. wed-1: 'Water; wet. 1. Suffixed o-grade form *wod-or in Germanic *watar in Old English wæter, water'.\")],\n  \"consulted\": [\n   co(\"KLN\", \"KLN_1971.txt line 265317 s.v. water\", \"supports\", \"'OHG. wazzar, MHG. wazzer, G. Wasser ... fr. I.-E. base *wod-, *wed-, *ud-, water'.\"),\n   co(\"POK\", \"pp. 78-81\", \"supports\", \"Germanic water words under aued-.\"),\n   co(\"WLD\", \"Bd. I line ~23550 s.v. 2. ued-\", \"supports\", \"'ued- netzen; heteroklit. r/n-St. uedor, uodor'.\")]},\n {\"id\": 9, \"lang\": \"French\", \"words\": \"vaseline\", \"verdict\": \"plausible\",\n  \"derivation\": \"Vaseline was coined in the USA by the chemist Robert A. Chesebrough (trademark 1872; Klein gives 1877) from German Wasser 'water' (< OHG wazzar) + Greek élaion 'oil' + chemical suffix -ine. French vaseline (f.) is a borrowing of this English trademark, not a French formation; it is, however, the source of the Persian word. The gloss 'moisturizing oil' loosely renders 'petroleum jelly'.\",\n  \"derivation_fa\": \"«وازلین» را شیمی‌دان آمریکایی رابرت چزبرو (نشان تجاری ۱۸۷۲) از آلمانی Wasser «آب» + یونانی élaion «روغن» + پسوند شیمیایی -ine ساخت. فرانسوی vaseline وام‌واژه از همین نام تجاری انگلیسی است، نه ساختهٔ فرانسوی؛ ولی واسطهٔ ورود آن به فارسی همان فرانسوی است. ریشهٔ نهایی درست است ولی مسیر نمودار دقیق نیست؛ با احتیاط پذیرفتنی است.\",\n  \"sources\": [W_VASEL],\n  \"ref_check\": [rc(\"None\", \"not_checked\", \"Node has no reference in the book.\")],\n  \"consulted\": [\n   co(\"KLN\", \"KLN_1966.txt line 41123\", \"supports\", \"'vaseline, n., a petroleum jelly. — Coined by Robert A. Chesebrough in 1877 fr. vas- (short for G. Wasser, water), -el (fr. Gk. elaion, oil) and chem. suff. -ine.'\"),\n   co(\"SKT\", \"SKT.txt grep 'vaseline'\", \"silent\", \"Not in Skeat.\"),\n   co(\"FSD\", \"not grepped\", \"silent\", \"Klein and Wiktionary sufficient.\")]},\n {\"id\": 10, \"lang\": \"Persian\", \"words\": \"vâzelîn\", \"verdict\": \"confirmed\",\n  \"derivation\": \"NP vāzelin وازلین is a 20th-c. loan from French vaseline (Mo'in tags it [فر.]), with French v-, -s- [z] and -ine [in] rendered faithfully.\",\n  \"derivation_fa\": \"«وازلین» در سدهٔ بیستم از فرانسوی vaseline وام گرفته شده است (معین: [فر.]) و تلفظ فرانسوی را حفظ کرده است. ادعای نورایی درست است.\",\n  \"sources\": [MO_VAZ],\n  \"ref_check\": [rc(\"MON:4944\", \"supports\", \"Mo'in online (vajehyab): 'وازلین (زِ) [فر.] (اِ.) نوعی روغن که از آن برای تهیهٔ بعضی داروها، پمادها و لوازم آرایشی استفاده می‌کنند'.\")],\n  \"consulted\": [\n   co(\"ARY\", \"ARY_pages.txt grep 'وازلین'\", \"silent\", \"Not found (Aryanpur treats inherited words).\"),\n   co(\"KLN\", \"line 41123 s.v. vaseline\", \"supports\", \"Coinage from G. Wasser + Gk. elaion.\")]},\n {\"id\": 11, \"lang\": \"English\", \"words\": \"Vaseline\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English Vaseline is the American trademark (Chesebrough, 1872) for petroleum jelly, coined from German Wasser + Greek élaion 'oil' + -ine; Wasser continues OHG wazzar, so the arrow from #8 is correct in substance (via modern German).\",\n  \"derivation_fa\": \"انگلیسی Vaseline نام تجاری آمریکایی (چزبرو، ۱۸۷۲) برای ژلهٔ نفتی است که از آلمانی Wasser «آب» + یونانی élaion «روغن» + -ine ساخته شده؛ Wasser دنبالهٔ wazzar آلمانی کهن است. ادعای نورایی درست است.\",\n  \"sources\": [W_VASEL],\n  \"ref_check\": [rc(\"None\", \"not_checked\", \"Node has no reference in the book.\")],\n  \"consulted\": [\n   co(\"KLN\", \"KLN_1966.txt line 41123\", \"supports\", \"'Coined by Robert A. Chesebrough in 1877 fr. vas- (short for G. Wasser, water), -el (fr. Gk. elaion, oil) and chem. suff. -ine.'\"),\n   co(\"SKT\", \"SKT.txt grep 'vaseline'\", \"silent\", \"Not in Skeat.\")]},\n]\n\nentries.append({\n \"entry\": 1, \"root\": \"Wed, Wer 4, Aŭe 2, Ud 2\", \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *wed- 'water, wet' (*wódr̥, *udró-) — Pokorny's complex au(e)-9, aued-, auer- (pp. 78-81) also includes *weh₁r-/*wer- 'water, rain' (Av. vār-, Skt. vār) and *h₁wers- 'rain, male'\",\n \"note\": \"Nourai follows Pokorny's lumped entry 'au(e)-, aued-, auer- to flow, wet; water' (pp. 78-81), so his multi-headed root is defensible as a citation, but modern scholarship separates *wed- (water, wet, otter, OHG wazzar) from *weh₁r-/*wer- (Av. vār- 'rain', vairi- 'lake' > Persian bārān) and *h₁wers- (Av. varəšni- 'ram'). The serious error is the quail branch: Pahlavi wartak and Persian vardīj mean 'quail' (Horn and Hübschmann, the very sources Nourai cites, connect them with Skt. vartikā / Gk. ortyx), not 'water bird', and have nothing to do with Av. udra- 'otter'. Vaseline is an American coinage borrowed by French, not a French word.\",\n \"note_fa\": \"نورایی از مدخل گروهی پوکورنی (ریشهٔ «au(e)-, aued-, auer-» «روان شدن، تر کردن، آب») پیروی کرده است. پژوهش امروزی سه ریشهٔ جدا می‌شناسد: *wed- «آب، تر» (آلمانی wazzar، اوستایی udra- «سمور آبی»)، *weh₁r-/*wer- «آب، باران» (اوستایی vār- ← «باران») و *h₁wers- «باریدن، نر». مهم‌ترین خطای نمودار شاخهٔ «وردیج» است: پهلوی wartak و فارسی «وردیج» به معنای «بلدرچین»اند و هرن و هوبشمان آن‌ها را با سنسکریت vartikā و یونانی ortyx پیوند داده‌اند، نه با udra-. ریشهٔ کلی با احتیاط پذیرفتنی است.\",\n \"sources\": [W_WODR, W_BARAN],\n \"ref_check\": [\n  POK_WED,\n  rc(\"AHD:1547,1549\", \"partial\", \"AHD_watkins1985: 'wed-1. Water; wet' (water, wet, wash, winter, hydro-, otter...) and separately 'wers-2. To be wet' — separate roots, no Iranian forms.\"),\n  rc(\"KLN:1732\", \"supports\", \"KLN_1971.txt line 265317 s.v. water: 'fr. I.-E. base *wod-, *wed-, *ud-, water' (1971 text; 1966 local text truncated).\")],\n \"consulted\": [\n  co(\"WLD\", \"Bd. I line ~23550, 25200\", \"partial\", \"Separate entries '2. ued- netzen' and uer-/uar- (av. vairi- See, vār- Regen).\"),\n  co(\"BRT\", \"col. ~1407 s.v. vār-\", \"supports\", BRT_VAR),\n  co(\"IEC\", \"IEC.txt grep\", \"silent\", \"Not checked in detail.\")],\n \"nodes\": e1_nodes})\n\nout = {\"pdf_page\": 527, \"book_page\": 497, \"verified_by\": \"claude-opus-5\", \"verified_on\": \"2026-10-16\", \"entries\": entries}\nwith open(\"/home/sfmqrb/git/rishe-private/data/verification/page-527.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\nprint(\"ok\")\n"
}
```


### [2026-10-16T05:20:43.254Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-527.py (file state is current in your context — no need to Read it back)
```


## [2026-10-16T05:20:48.213Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; sed -i \"s/with the Bartholomae's-law cluster/with the cluster/; /co(\\\"FSD\\\", \\\"not grepped\\\"/d; s/co(\\\"SKT\\\", \\\"SKT.txt grep 'vaseline'\\\", \\\"silent\\\", \\\"Not in Skeat.\\\"),$/co(\\\"SKT\\\", \\\"SKT.txt grep 'vaseline'\\\", \\\"silent\\\", \\\"Not in Skeat.\\\")/\" build-527.py; python3 build-527.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-527.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 527"
}
```


### [2026-10-16T05:20:48.721Z] TOOL RESULT

```
Exit code 1
  File "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-527.py", line 260
    {"id": 9, "lang": "French", "words": "vaseline", "verdict": "plausible",
    ^
SyntaxError: '{' was never closed
```


## [2026-10-16T05:20:51.158Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; grep -n -A3 'co(\"SKT\", \"SKT.txt grep .vaseline' build-527.py"
}
```


### [2026-10-16T05:20:51.473Z] TOOL RESULT

```
267:   co("SKT", "SKT.txt grep 'vaseline'", "silent", "Not in Skeat.")
268- {"id": 10, "lang": "Persian", "words": "vâzelîn", "verdict": "confirmed",
269-  "derivation": "NP vāzelin وازلین is a 20th-c. loan from French vaseline (Mo'in tags it [فر.]), with French v-, -s- [z] and -ine [in] rendered faithfully.",
270-  "derivation_fa": "«وازلین» در سدهٔ بیستم از فرانسوی vaseline وام گرفته شده است (معین: [فر.]) و تلفظ فرانسوی را حفظ کرده است. ادعای نورایی درست است.",
--
283:   co("SKT", "SKT.txt grep 'vaseline'", "silent", "Not in Skeat.")]},
284-]
285-
286-entries.append({
```


## [2026-10-16T05:20:52.882Z] AGENT

The FSD line deletion took the `]},` closer with it; restoring.


## [2026-10-16T05:20:54.750Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; sed -i '267s/Not in Skeat.\")$/Not in Skeat.\")]},/' build-527.py; python3 build-527.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-527.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 527"
}
```


### [2026-10-16T05:20:55.440Z] TOOL RESULT

```
ok
nodes verified: 23/23
node verdicts: {'confirmed': 12, 'plausible': 8, 'transcription_suspect': 1, 'disputed': 2}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 19, 'partial': 3, 'not_checked': 12, 'contradicts': 3}
books consulted: {'supports': 39, 'silent': 20, 'partial': 10, 'contradicts': 6} | by book: {'WLD': 11, 'AHD': 9, 'KLN': 7, 'BRT': 6, 'PHD': 6, 'POK': 6, 'SKT': 5, 'NYB': 4, 'HUB': 4, 'ARY': 4, 'IEC': 4, 'HRN': 3, 'CHEUNG': 2, 'SYN': 1, 'LAT': 1, 'MON': 1, 'BQT': 1}
```


## [2026-10-16T05:21:06.777Z] TOOL CALL #59: SubagentHandback

```json
{
 "message": "I verified PDF page 527 (book page 497) and wrote /home/sfmqrb/git/rishe-private/data/verification/page-527.json. `verify_check.py 527` reports 0 PROBLEM lines, with all 23 of 23 nodes verified.\n\n**Verdicts:**\n- **Roots:** Webh is confirmed. \"Wed, Wer 4, Aŭe 2, Ud 2\" is plausible: Nourai follows Pokorny's merged entry on pp. 78–81, but modern work splits it into three roots: *wed- (water, wet), *weh₁r-/*wer- (Avestan vār- \"rain\" → Persian bārān) and *h₁wers- (rain, male).\n- **Nodes:** 12 confirmed, 8 plausible, 2 disputed, 1 transcription_suspect.\n\n**Disputed:**\n- **Wed #5, Pahlavi vartak 2 (\"a water bird\"):** the word means \"quail\". It comes from Indo-Iranian *wartaka-/*wartikā- (Sanskrit vartikā, Greek ortyx), not from Avestan udra- \"otter\". Horn p. 242 no. 1078, which Nourai himself cites, says exactly this, and Hübschmann agrees.\n- **Wed #6, Persian vardîj وردیج:** also \"quail\" (بلدرچین), according to Dehkhoda and Mo'in. The variant ودخین that the chart adds is a different word. Borhan p. 2262 describes it as a blind, toothed water animal with a long thin body and gives no etymology.\n\n**Transcription suspect:**\n- **Webh #8, Pahlavi \"vassz\" (wasp):** the book itself prints \"vassz\". The correct form is MP wabz, written wpc/wpz in Pahlavi (MacKenzie; Pokorny p. 1179 \"vabz\"). wabz comes straight from Iranian *wabža-, not from Avestan vawžaka-. I recorded `error_in: book` and saved the page image to `data/verification/sources/refs/ocr/BOOK/527.png`.\n\n**Notable plausible nodes:**\n- **Webh #4:** wave and wobble are only \"possibly\" from *webʰ- in Watkins, and Pokorny puts them under a separate root, uebh-2.\n- **Webh #7, Avestan vawžaka:** the gloss \"scorpion\" is a conjecture. Bartholomae only says \"name of a noxious animal\".\n- **Webh #11:** Latin \"vepsa\" is a reconstructed form and is not attested.\n- **Wed #4, Avestan udra:** it means \"otter\", not \"water bird\".\n- **Wed #7:** Avestan varəšni- means \"ram\", not \"testicles\"; \"testicles\" is the meaning of the Sanskrit cognate vṛṣaṇa-.\n- **Wed #3, bârgîn:** the link to rain is uncertain.\n- **Wed #9:** Vaseline is an American trademark coined from German Wasser + Greek élaion; French borrowed it rather than forming it.\n\n**Extraction errors:** none. The JSON matches the printed page.\n\n**Other notes:**\n- The local Klein 1966 text stops at \"veratrine\", so I checked the W entries in the 1971 edition. Its pages don't match Nourai's numbers.\n- BQT:218 has no available scan.\n- OEW and AEF are not accessible, so those refs are marked not_checked.\n- I saved what I read from the Borhan p. 2262 image to `data/verification/sources/refs/ocr/BQT/2262.vision.txt`."
}
```


### [2026-10-16T05:21:07.165Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
