# Verification process log — verify-page-522


## [2026-10-16T05:13:01.600Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 522 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-522.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-522.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-522.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 522` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:01.636Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:07.342Z] TOOL CALL #1: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md; echo ====; cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-522.txt; echo ====; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-522.json",
 "description": "Read instructions, chart text, and source JSON"
}
```


### [2026-10-16T05:13:07.921Z] TOOL RESULT

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


## [2026-10-16T05:13:10.520Z] TOOL CALL #2: Bash

```json
{
 "command": "sed -n '/SAVE what you/,/Wiktionary\\*\\* (en/p' /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md",
 "description": "Read truncated middle part of instructions"
}
```


## [2026-10-16T05:13:11.448Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-522.txt; echo; echo =====; cat /home/sfmqrb/git/rishe-private/data/extracted/batch/page-522.json",
 "description": "Read chart text and source JSON"
}
```


### [2026-10-16T05:13:11.792Z] TOOL RESULT

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


### [2026-10-16T05:13:12.031Z] TOOL RESULT

```
Exit code 1
=== PDF page 522 (book page 492) ===
--- entry 0 ---
ROOT [Avestan] Vaenâ 1, Vaěnâ 1 : nose  (refs AEF:323)
#1 (parent #0) [Pahlavi] refs=AEF:323 | věnîk, běnîk : nose
  #2 (parent #1) [Persian] refs=BQT:341 | bînî «بینی» : nose
--- entry 1 ---
ROOT Vaěnâ 1 -> redirect to Vaenâ 1
--- entry 2 ---
ROOT Vaidŭrya -> redirect to Velŭr
--- entry 3 ---
ROOT [Indo-Schythian] Var : to cover, enclose  (refs ISS:234)
#1 (parent #0) [Pahlavi] refs=ISS:234 | varm 1 : container, reservoir
  #2 (parent #1) [Persian] refs=ISS:234; MON:511 | barm «بَرم» : reservoir, pool
--- entry 4 ---
ROOT Varaka -> redirect to Varekahe
--- entry 5 ---
ROOT [Avestan] Varâza : boar (animal)  (refs BQT:1779)
#1 (parent #0) [Pahlavi] refs=MON:3212 | varâz : boar
  #2 (parent #1) [Persian] refs=MON; HRN:200; BQT:1780,2263 | vorâz «وُراز» : boar ; gorâz «گراز» : boar, also a bold and strong person
--- entry 6 ---
ROOT [Avestan] Varekahe, Varaka : leaf  (refs SNS:281; SYN:525; EAV:86)
#1 (parent #0) [Pahlavi] refs=BQT:260; AEF:259 | varg, valg
  #2 (parent #1) [Persian] refs=MON:571; AEF:259 | barg «برگ» : leaf, page, sustenance | extra: بلگ ، بلگه ، برگه

(eval):1: ==== not found
```


## [2026-10-16T05:13:16.620Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/extracted/batch/page-522.json | head -c 6000; echo; echo '---'; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AEF','BQT','ISS','MON','HRN','SNS','SYN','EAV','PHD','NYB','BRT','POK','WLD','AHD','ISS_alt_DKS','HUB','CHEUNG','ARY','KNT','IEC']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"; ls data/verification/page-52*.json; ls data/verification/sources/refs | head -80",
 "description": "Read JSON, ref key, list local refs"
}
```


### [2026-10-16T05:13:17.131Z] TOOL RESULT

```
{
  "pdf_page": 522,
  "book_page": 492,
  "entries": [
    {
      "root": {
        "name": "Vaenâ 1, Vaěnâ 1",
        "lang": "Avestan",
        "refs": "AEF:323",
        "gloss": "nose"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "AEF:323",
          "words": [
            {
              "translit": "věnîk, běnîk",
              "gloss": "nose",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:341",
          "words": [
            {
              "translit": "bînî",
              "gloss": "nose",
              "script": "بینی"
            }
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Vaěnâ 1",
        "redirect": "Vaenâ 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Vaidŭrya",
        "redirect": "Velŭr"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Var",
        "lang": "Indo-Schythian",
        "refs": "ISS:234",
        "gloss": "to cover, enclose"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "ISS:234",
          "words": [
            {
              "translit": "varm 1",
              "gloss": "container, reservoir",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "ISS:234; MON:511",
          "words": [
            {
              "translit": "barm",
              "gloss": "reservoir, pool",
              "script": "بَرم"
            }
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Varaka",
        "redirect": "Varekahe"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Varâza",
        "lang": "Avestan",
        "refs": "BQT:1779",
        "gloss": "boar (animal)",
        "note": "Cognate with Sanskrit \"varâha\""
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "MON:3212",
          "words": [
            {
              "translit": "varâz",
              "gloss": "boar",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON; HRN:200; BQT:1780,2263",
          "words": [
            {
              "translit": "vorâz",
              "gloss": "boar",
              "script": "وُراز"
            },
            {
              "translit": "gorâz",
              "gloss": "boar, also a bold and strong person",
              "script": "گراز"
            }
          ],
          "note": null,
          "quote": {
            "text": "دور سپهر مثل تو هرگز نیاورد - از هفت پشت پهلو شیرافکن و گراز",
            "poet": "Amîd Lobakî"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Varekahe, Varaka",
        "lang": "Avestan",
        "refs": "SNS:281; SYN:525; EAV:86",
        "gloss": "leaf"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT:260; AEF:259",
          "words": [
            {
              "translit": "varg, valg",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:571; AEF:259",
          "words": [
            {
              "translit": "barg",
              "gloss": "leaf, page, sustenance",
              "script": "برگ"
            }
          ],
          "script_extra": "بلگ ، بلگه ، برگه",
          "note": null,
          "quote": {
            "text": "ژیغ ژیغ تلخ آن درهای مرگ - نشنود گوش حریص از حرص برگ",
            "poet": "Molavî"
          }
        }
      ]
    }
  ]
}
---
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
EAV {"title": "J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869", "edition_found": "JSTOR offprint collected in an IA item 'Studies by Jacques Duchesne-Guillemin'", "kind": "archive_djvu", "url": "https://archive.org/details/duchesne-guillemin-studies", "identifier": "duchesne-guillemin-studies", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
ISS_alt_DKS null
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
Permissions Size User   Date Modified Name
.rw-r--r--   50k sfmqrb 14 Oct 22:14  data/verification/page-52.json
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
```


## [2026-10-16T05:13:21.707Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls data/verification/sources/refs | tail -40; python3 -c \"\nimport json;d=json.load(open('data/verification/page-511.json'));print(json.dumps(d,ensure_ascii=False,indent=1)[:5000])\"; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AEF','BQT','ISS','MON','HRN','SNS','EAV','PHD','NYB','BRT','HUB','ARY','SYN']:\n  v=d.get(k); print(k, v.get('local_file'), v.get('page_offset'), '|', (v.get('lookup_hint') or '')[:300])\n\"",
 "description": "Look at sample output and ref details"
}
```


### [2026-10-16T05:13:22.118Z] TOOL RESULT

```
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
{
 "pdf_page": 511,
 "book_page": 481,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-10-14",
 "entries": [
  {
   "entry": 0,
   "root": "Tôkei, Tôgei",
   "verdict": "plausible",
   "modern_form": "Tamil tōkai (தோகை) 'peacock's tail; peacock' - a proposed, not proven, eastern source of Greek ταώς",
   "note": "Tamil tōkai 'tail of a peacock; peacock' is a real word (Wiktionary தோகை), and Klein (KLN:1143) and Skeat (SKT:378) both name 'Tamil tokei, tōgei' as the ultimate source of the peacock words, so Nourai's root box faithfully reports his references; Wiktionary today calls Greek ταώς 'of Pre-Greek origin; possibly ... perhaps from Dravidian (compare Tamil tōkai)', i.e. only a possibility. The internal chart, however, is wrong in its routing: (1) there is no Sanskrit intermediary (Sanskrit has mayūra-, śikhin-); (2) Arabic ṭāwūs comes from Aramaic ṭawsā, which comes from Greek ταώς, not from Sanskrit; (3) Greek ταώς (5th c. BCE) and Latin pāvō cannot derive from medieval Persian ṭāvūs - the arrows from the Persian box to Greek and Latin reproduce Skeat's 1911 chain and are reversed. Persian ṭāvūs < Arabic, OE pēa < Latin pāvō and English peacock are correct. The book's root note prints 'Tanil' for Tamil (misprint in the book, faithfully extracted). No extraction errors: JSON matches the printed page.",
   "note_fa": "تامیلی tōkai «دم طاووس؛ طاووس» واژه‌ای واقعی است و کلاین (۱۱۴۳) و اسکیت (۳۷۸) هر دو «tokei/tōgei» تامیلی را سرچشمهٔ نهایی نام طاووس در زبان‌های اروپایی دانسته‌اند؛ ویکی‌واژهٔ امروز یونانی ταώς را پیش‌یونانی و تنها «شاید» از دراویدی می‌داند. پس ریشه با احتیاط پذیرفتنی است. اما مسیرهای درون نمودار نادرست است: گذر از سنسکریت گواهی ندارد؛ «طاووس» عربی از آرامی ṭawsā و آن از یونانی ταώς است؛ و یونانی ταώς و لاتین pāvō که بسیار کهن‌ترند نمی‌توانند از «طاووس» فارسی (که خود معرّب است) آمده باشند - پیکان‌ها وارونه‌اند و از اسکیت (۱۹۱۱) گرفته شده‌اند. «طاووس» فارسی از عربی، pēa انگلیسی کهن از لاتین و peacock انگلیسی درست است. «Tanil» در یادداشت کتاب خطای چاپی به جای Tamil است؛ خطای استخراج دیده نشد.",
   "sources": [
    "https://en.wiktionary.org/wiki/தோகை",
    "https://en.wiktionary.org/wiki/ταώς",
    "https://en.wiktionary.org/wiki/طاووس",
    "https://en.wiktionary.org/wiki/pavo",
    "https://en.wiktionary.org/wiki/peacock"
   ],
   "ref_check": [
    {
     "ref": "KLN:1143",
     "status": "partial",
     "note": "Klein 1966 s.v. peacock (KLN_1966.txt line 27770): 'OE. pāwa, pēa ... fr. L. pāvo, gen. pāvonis, 'peacock' ... which, together with Gk. ταώς, prob. comes ult. fr. Tamil tokei, tōgei (whence also Heb. tukkiyyim, 'peacocks'). The initial p- in L. pavo is due to imitative influence'. Klein supports the Tamil root and the Latin/OE/English chain, but routes Latin and Greek directly from the eastern source, not through Persian/Arabic, and has no Sanskrit link."
    },
    {
     "ref": "SKT:378",
     "status": "supports",
     "note": "Skeat, Concise Etym. Dict. s.v. Peacock (SKT_dli_revised.txt line 55507): '(L. - Pers. - Tamil; and E.) M.E. pecok ... AS. pea, pāwa; all from L. pāuo ... The same as Gk. ταώς, for ταϝώς, a peacock; the change from τ to p being due to the fact that the word was foreign both to L. and Gk. - Pers. tāwus, tāus, a peacock. - Tamil tōkei, tōgei, a peacock'. This is exactly Nourai's chain (Tamil > Persian > Greek/Latin > OE > E.); it is Skeat's 1911 view, now abandoned."
    }
   ],
   "consulted": [
    {
     "src": "MON",
     "where": "vol.2 s.v. طاوس (MON_part1.txt line 91933)",
     "stance": "supports",
     "note": "'[دراویدی هندی]' - Mo'in also gives a Dravidian/Indian origin."
    },
    {
     "src": "BQT",
     "where": "p.1346, Mo'in fn. s.v. طاوس (ocr/BQT/1346.vision.txt)",
     "stance": "partial",
     "note": "'(عر) معرب آن طویس، یونانی Taôs، آرامی طاوسا tausâ ... اصل کلمه از زبان دراویدی وارد سانسکریت شده و از آنجا بزبانهای دیگر رفته' (after Pourdavoud)."
    },
    {
     "src": "HJB",
     "where": "grep tokei/togai/tukki",
     "stance": "silent",
     "note": "Hobson-Jobson OCR yields no Tamil peacock entry."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Sanskrit",
     "words": "",
     "verdict": "disputed",
     "derivation": "Empty pass-through box: Nourai (following Pourdavoud via Mo'in's Borhan footnote) routes the Tamil word through Sanskrit before it reaches Aramaic and Arabic. No Sanskrit form of the tōkai/ṭāwūs type is attested: the Sanskrit words for 'peacock' are mayūra-, śikhin-, barhin-, kalāpin-. Modern scholarship (Wiktionary s.v. ταώς, Klein s.v. peacock) derives the Mediterranean/Semitic words either from Pre-Greek ταώς or directly from a Dravidian (Tamil tōkai) or other eastern source by sea trade, with no Sanskrit intermediary.",
     "derivation_fa": "این خانهٔ خالی «سنسکریت» را نورایی به پیروی از پورداوود (در حاشیهٔ معین بر برهان قاطع) میان تامیلی و آرامی/عربی گذاشته است. اما در سنسکریت واژه‌ای از گونهٔ tōkai یا ṭāwūs برای طاووس دیده نمی‌شود؛ نام‌های سنسکریت طاووس mayūra، śikhin و barhin است. پژو
AEF None None | Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015
BQT ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
ISS None DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Khotanese Texts VI itself is not online. Nourai's ISS page numbers cannot be checked directly; the Dictionary of Khotan Saka (headword at line start, Khotanese in transliteration, with 'Pok.' refs) covers the same etymological material and can verify the substance of a claim.
MON ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
HRN /home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
SNS ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt'] 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image | grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
EAV /home/sfmqrb/git/rishe-private/data/verification/sources/refs/EAV_studies.txt The article keeps its BSOAS page numbers 861-869: leaf = printed - 702 (e.g. leaf 169 = p.871), i.e. pp. 861-869 are at leaves ~159-167. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | grep -n 'Etymologies Avestiques' EAV_studies.txt; numbered etymologies with Avestan headwords.
PHD /home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
NYB /home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
BRT /home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
HUB /home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
ARY ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] printed page = pdf page + 1 | Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
SYN /home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
```


## [2026-10-16T05:13:26.999Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/522.jpg 2>/dev/null; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; mkdir -p $S; pdftoppm -f 522 -l 522 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg522 && ls $S",
 "description": "Render printed page 522"
}
```


### [2026-10-16T05:13:27.870Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   63k sfmqrb 14 Oct 22:15  site/pages/522.jpg
Permissions Size User   Date Modified Name
.rw-r--r--   440 sfmqrb 16 Oct 01:13  agents.txt
.rw-r--r--   48k sfmqrb 16 Oct 01:13  pg522.png
```


## [2026-10-16T05:13:30.112Z] TOOL CALL #7: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg522.png"
}
```


### [2026-10-16T05:13:30.140Z] TOOL RESULT

```

```


## [2026-10-16T05:13:40.455Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo '## PHD'; grep -n -i -E '^(wēnīg|wenig|wēnīk|warm|warāz|waraz|warg|barm|wāraz)\\b' PHD.txt PHD_mackenzie.txt | head -30; echo '## NYB'; grep -n -i -E '^(vēnīk|venik|varm|varāz|varaz|varg|warg|wēnīk)' NYB_vol2_glossary.txt | head; echo '## HRN'; grep -n -E '^ *[0-9]+\\. *(bīnī|bini|gurāz|guraz|barg|barm|warāz)' HRN.txt | head; grep -n -i -E 'bīnī|gurāz|barg |varg' HRN.txt | head -20",
 "description": "Grep MacKenzie, Nyberg, Horn for headwords"
}
```


### [2026-10-16T05:13:40.824Z] TOOL RESULT

```
## PHD
PHD.txt:4264:warm garm(6g); ~ region garmsér,
PHD_mackenzie.txt:5189:warAz [wPc I N guraz] boar.
PHD_mackenzie.txt:5205:warg [wlg IN barg] leaf.
PHD_mackenzie.txt:5326:wenig [wynyk 1M wynyg, N bilti] nose.
PHD_mackenzie.txt:10078:waraz                      ~I        nakkira
PHD_mackenzie.txt:10081:warg                         ~,      nigeridan            "~,,
## NYB
3955:Varazin patron. of n. pr. Varaz: P1:7.
3968:varg [wlg] leaf 957+. MPrth wrgr (Sogd. 4); barg.
6858:varg-: ~
## HRN
2172:aw. varekah^ (ZP61.); phlv. varg 'Blatt',
2236:(137); wa;K. vurk, siyn. varg, sar. barka,
7888:Käs. var, varg, mrg\ mäz. vurg.— 203 —
7891:kurd. varg *Wolf'; afy. lüg] oss. d. beräyj t. biräy
18790:K. varg 910.
```


## [2026-10-16T05:13:44.294Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5185,5210p PHD_mackenzie.txt; sed -n 5320,5330p PHD_mackenzie.txt; grep -n -E '^warm|^wām|^wa[rl]m ' PHD_mackenzie.txt | head; echo '## HRN'; sed -n 2165,2180p HRN.txt; grep -n -E 'guräz|gurdz|gurâz|varäza|varāza|varaza' HRN.txt | head; grep -n -E 'binl|bīnī|blni|vaena|vaeiia|vaēnā' HRN.txt | head",
 "description": "Read PHD entries and grep Horn"
}
```


### [2026-10-16T05:13:44.950Z] TOOL RESULT

```
waranig [wlnyk l ] greedy.
  ......ih: greed, lust.
wArAnig [w)Pnyk I N barani] rain(y).
                        '
warAz [wPc I N guraz] boar.
war-~aim [wlclm] with eye(s) in the breast.
ward-, v. lwaitan.
lwardag [wltk I M wrdg, N barda] captive, prisoner•
                    '
 ......ih: captivity.
lIwardag [wlth ] on heat (female animal).
                 '
 ......ih: heat.
·wardAnAg [wlt)n)k l I N gardana] (roasting) spit.
wardenidan, warden- [wltyn-ytn l I (N gardanidan)] cause to turn;
  change, alter.
wardlin [wlt!n' I M wrdy!n, N gardif] turning, change, metamorphosis•
 ......ig [-yk l ] transient, changeable.
 ......(ig)ih: transience, mutability.
wardyun [wltywn l I P wrdywn, N gardun] vehicle, carriage, chariot.
warg [wlg IN barg] leaf.
wAridan, war- [w)l-ytn l I M w)r-yst, N baridan] rain.
warlin [wlIn ' ] conduct, behaviour.
lwarm [wlm I N barm] memory.
 ...... kardan: learn by heart, memorize.
lIwarm [wlm I N barm] pool, reservoir.
wenAb [w)m)p I N binab] vision.
 ......dig [-d)k l , -t)k ] visible.
                         '
wenag [wyn~kJ I M wyn)g, N bind] seeing.
  ......ih: seeing, sight.
                                                             wihez(all)
wenig [wynyk 1M wynyg, N bilti] nose.
                 '
wenog [wynwk' I N bunu] lentil.
weA [wyl I = M, N bel] more.
wMag [wylk' I N bela] thicket, wood.
## HRN
aw. vafra- 'Schnee'; phlv. vafr.
kurd. vafr (H.-Sch.), befir, bafer, berf (LW.); af>.
vävra 'Schneeflocke*, Plur. 'Schnee'; bei. LW. harpi
sangl. varf, min], värfa,
203. hery 'Blatt'.
g. niaz. varak; gel. velg, valk; Käö. valg^ velg\ (vergl.
buchär. :^3, Ps. 1, 3).
aw. varekah^ (ZP61.); phlv. varg 'Blatt',
kurd. LW. (?) valg (H.-Sch.), belk, balg (Guranl, Rieu
Catalogue II, 729 a).
204. bevf/er 'Glück'.
SiW.*uparö.kara- {wergl.uparö.kairga-), deLagarde,
Beitr. z. altbaktr. Lex. 71, von Geldner, 3 Yasht 12,
gebilligt.
205. bergustuwän 'Panzer, Pferdepanzer'.
Etwa *uparö,kustapäna'; phlv. vergl. kustak \Seite'.
7787:896. guräz *Eber .
7788:aw. varäza- 'Eber ; phlv. varOz (geschrieben varoc),
2615:58. blni 'Furcht'.
```


## [2026-10-16T05:13:48.936Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 7785,7800p HRN.txt; grep -n -i -E 'Nase' HRN.txt | head; awk 'BEGIN{RS=\"\\f\"} NR==222' HRN.txt | head -5; grep -c . HRN.txt; python3 - <<'E'\nt=open('HRN.txt').read().split('\\f')\nfor i,p in enumerate(t):\n  if '896. gur' in p or '203. ber' in p: print('leaf',i, 'printed', i-21)\nE",
 "description": "Read Horn guraz and find nose entry"
}
```


### [2026-10-16T05:13:49.365Z] TOOL RESULT

```
Krätze' (69) ; vergl. nslov. gar je *Krätze', garjaOj garat
^kratzen' (Miklosich, Denkschr. WAW. Band 37, 40).
896. guräz *Eber .
aw. varäza- 'Eber ; phlv. varOz (geschrieben varoc),
arm. LW. varaz, vgl. Varazdat, Baoa^rj^, OvuQoiCfjg
(Armenier); ai. varähd- *Eber'.
kurd. heräz,
V
np. veraz *Eber' wird im FS (Vullers) durch einen
V
angeblichen Sähnämevers belegt, der aber des Metrums
halber kein solcher sein kann.
897. geräziden 'schreiten .
ai. V^vra}', vrdjati schreiten, gehen, fortgehen'
(Rückert, ZDMG. 10, 165).
898. girun 'schwer.
1306:'in die Nase einführen, einfüllen* u. ö. (mit und ohne
2639:261. Mm 'Nase.
2641:aw. va^nä' Nase' (Y. 9, 11 (35), Darmesteter, Et.
2643:kurd. hen *Nase, Geruch' (H.-Sch.); bei. gin *Atem,
3172:335. poz 'Partie um die Nase* 2).
3174:kurd. püZj pöz; bei. pöz, pönz, n. pönz 'Nase (310);
3176:oss. d. finje, t. fing 'Nase' (286), arm. pinj (pinS)
3177:'Nasenloch* will Hübschmann hiervon trennen ;
3189:vergl. deutsch *seine Nase in etwas hineinstecken'. F J citirt noch Verse
10766:139. näl {nak?) 'Nase, nur vd. 8 (46), 9 (158).
— 200 —
895. ger, gerr (AM. 28 Zeile 4) ^Krätze.
aw. garenu' *Krätze' vd. 7, 58 (145), yt. 13, 131
(Darmesteter, ebenso Jackson, der Amer. or. Soc.
Proc. 1889, XXV und Avesta Grammar § 806 ai.
23314
leaf 221 printed 200
```


## [2026-10-16T05:13:52.816Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2636,2650p HRN.txt; echo '## HUB'; grep -n -E '^ *(261|896|203)\\.|guräz|blnl|bini|barg' HUB.txt | head -20; echo '## NYB'; sed -n 3955,3970p NYB_vol2_glossary.txt; grep -n -i -E '^v[eē]n[iī]k|^varm|^va?raz' NYB_vol2_glossary.txt | head",
 "description": "Horn bini, Hübschmann, Nyberg lookups"
}
```


### [2026-10-16T05:13:53.182Z] TOOL RESULT

```
af/. vm-am; oss. d. mmin, t. ünin (82); wa;^. §iyn.
viti-am, sar. veln-am.
*) Gul. (Sprenger) S. 26 Zeile 8 reimt es ausnahmsweise auf piL— 60 —
261. Mm 'Nase.
Semn. vlm; mäz. v^it,
aw. va^nä' Nase' (Y. 9, 11 (35), Darmesteter, Et.
ir. I 57); phlv. venik (Bund., AV.), bEmk (AV.).
kurd. hen *Nase, Geruch' (H.-Sch.); bei. gin *Atem,
Leben (109) (?).
Fr. Müller (WZKM. 5, 260) stellt dazu phlv. mi,
(ZP61. 8, 3) 'Hauch* und nimmt als dessen Grundform
*vayana' an.
262. bever 'tausend'.
äw. ba^vare 'tausend'; phlv. bevar.
oss. d. beurä, t. birä Viel, sehr, lange (61).
## HUB
1149:261. Dazu auch paz. vtni *nose, nostrils Shk. 273.
1185:(bei Vullers auch bargm^ was falsch ist) erwahnt
3892:203. Eher uf!de3 etc. zu leseu, vgl. Phi. Min. p. 10, Z. 1
4845:bargar {^), bargustuvan {?), barvar^), varvdra Horn Nr. 204,
5260:barg *Blatt', bevar zehntausend', parr Teder, Fliigel', dar
5457:61. 204, zd. vafra-; barg *Blatt' = zd. vareka-; barra 'Lamm'
8446:46, 139) = ap. mad^ista- ; bargustuvan 'Pferdepanzer H. 205,
10315:bargar 27.
## NYB
Varazin patron. of n. pr. Varaz: P1:7.
vare [wlc'] a supernatural power given |
to man by the gods 90%; varc-é given by the gods to the bull of Käyös 45°; men- tioned together with z"arrah, amävandeh
203
Var-kaš
and pērēzgarēh 11938; almost a synonym of avarrah 4%. — Av. (1367) !earocah-; MPrth. wre (S, A-H III); MPrs wre, wrz; Paz. (Gsmqn-)varz (SGV); NP varj.
vareak heavenly brightness: ~ % hac
asmän àyet 120%,
varcävand possessing supernatural pow- er: of ätur farröbäg 974; of ātaxš Varhran 1139-21; of ātaxš i Karköi 1164; — subst. a man endowed with supernatural power, of Zartuxšt 36%; mart i vazurg x"arrah 4 Yam u an-ic ~ 44°; pl. cas. obl. ~-an 455, — MPrs wrc'wynd (S).
varcāvandihā in a supernatural, mira-
culous way 38?.
vare-kartik [~-krtyk] miracle 381. — ""Supernational power realized in work”. vard- (Ps.) [wld-] vart-, v. vastan; subju. 3d p. pl. vardänd [wld’ndy] apä- ron may they turn backward 128.
— Av. (1367) varaka- ; Paz. varg; NP
varg [wlg] leaf 957+. MPrth wrgr (Sogd. 4); barg.
Varhran [wlhl’n'], Varhräm [wlhPm] 1.
the god: ätaxs V-n 1277, 958-10, 1045. 1139-21, ätaxs i V-m 82°, the fire found in every fire-temple, v. Christensen,
3955:Varazin patron. of n. pr. Varaz: P1:7.
```


## [2026-10-16T05:13:56.657Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"'Nase'|Nase\\b\" BRT.txt | head; grep -n -E \"'Blatt'|Eber\" BRT.txt | head; grep -n -E \"^ *(1316|1317|1367|1368|1374|1375|1376)$\" BRT.txt | head -20",
 "description": "Grep Bartholomae for nose, leaf, boar"
}
```


### [2026-10-16T05:13:57.254Z] TOOL RESULT

```
8669:•  j.  uzyazcUüia-  m.  ein  Teil  der  Nase: 'na  F._jd.
10943:°paya  vainaya  bar^sna  "am  Hintern,  an der  Nase,  in  der  Höhe"  Y.5. 11  PUZ. (,  Yt/5.40)".
14496:•  j.  9-raDh-  n.  'Mund':  -arg  (NS.)'>  F. 23.  a)  Du.  'die  Mundwinkel' :  nazdyd  . . ya^a  *näaha  haca  *gaosalibya  yaha vä  gaosa  haca  ^'anhibya'^  "näher .. als  die Nase  von  den  Ohren  oder  als  die  Ohren von    den   Mundwinkeln   (entfernt    sind)"
14953:•  j,  paiti.däna-  m.  'Vortuch,  Schutztuch'; a)  auf  der  Brust  (unter  demPanzer)  getragen, 'Brusttuch':  yalsqm  zayanqm  ra^BtlH  . . naumö  'nS'V.j4.g;  —  taranafrum  °ram  .  . histaile  draiimns  (statt  fem,)  artdvX  Yt 5.133.  b)  insbes.  Name  des  von  den Priestern  über  Nase  und  Mund  getragenen Tuchs  *^  das  bestimmt  war,  das  Feuer  vor der  Berührung  durch  den  Atem  zu  be- wahren**': yagsqm  zayanqm  a%aurune astra  gaoihi  'nD  V.14.8;  —  'rum  *ainm iarai/i  anaiwyäs/ff  dalnqm  V.  lÜ.  i;  — wird  dem  Toten  mitgegeben  (s.  *'):  avi h?  iristanqm  tanüm  .  ./rada%eiiti  , ,  xa/fvl 'nahe  Vd.  12.
15890:lich 'darauf,  alsdann':  äat  mqm  narS  p' vaz^iiU  ahtirsm  masdam  dariyS ya¥t>mh . . H.  2. 14.  a)  mit  voranstehendem  enkl. Gen.  neutr.  h?  Avt.:  apa  hl p°  */raoirisyeiti .  .  aisa  drux¥  yl  nasul  nfnhanat  haca "alsdann  kommt  die  Dr.  wieder  zum  Vor- schein von  der  Nase  her"  V,^.  40.
18941:•  j.,  p.  nah-  m.  'Nase',  Sing,  und  Du.: Waäamsaiy  uta  nüham  utä  gausa  fraja- nam  Bh.  2. 14;  13;  —  yim  yava  vatim närahabya  hubaoüitim^m  ßgaurva  H. 2.8;  26;  —  t^m  vahm  ninhaya  (LS.)'> *uzgnmiiiysil.2.8;  a6;  —  «Jw^a  (ND.)'' F.jd; — yaha  *nänhai''  Aaca  *gaoSaäbya ydha  vä  gaosa  Aaca  *^raaAiiya  (sd.)  P.  28.
19100:.  j.  nanhan-  m.  'Nase'  des  Menschen:!  ..^- ^^.^„^„  ^^,^  .,,■  „,.^^_^^^„  ,.
22129:•  j.  vaenä-  f,  'Nase:  xhaipaya  (sd.)  'naya bansna  Y.ß.  11  PüZ.,  Yt.  ;p.  40.  |
22130:kuid.  beit  'Nase,  Geruch' ;  mp.  ven,  nbal.  gtn  | •Atem'i  np.  vgl.  blni  'Nase'.  Vgl  DsT.  £tlr.  ] /,  57,  HoBN  NpEt.  60.  I
24750:mit  para  dnwS. :  iiä  tat  para. iri^y eilt  \  den  Lebenden  eindringt"  V.  10.  i  ^\  — V,5. 1 ;  J2, 1  ff,;  — yat  asava  para.irikyeiti  ^yesi  sl  baräi  a^'S yat  iristim  upa  vä  nasus .  .  yat  drva  *ava.miryete  H.  2. 1  und  19;  l  ralhwat  natshanat  haca  ".  .  so  dringt  die —  yat  also  nä  para.iri'hya^  Y .  5. /^i  ■,YA.\  J^.  (in  ihn)  ein  durch  die  Nase  .  ."  V. 2    (wo  pairi  siM.  para);    —   yat    ssn}s\j.i4.
2060:Meinen  Schlilem,  Herrn  Dr.  Otto  Keller  aus  Eberstadt,  der  mir  bei  der Koirektur,  von  Bogen  10  an,  und  Herrn  Frttz  Wolff  aus  Berlin,  der  mir  bei  der Korrektur,  von  Bogen  45  an,  und  insbesondere  bei  der  Ausarbeitung  der  Indices geholfen  hat,  spreche  ich  auch  an  dieser  Stelle  meinen  besten  Dank  aus.
4495:Ebers,    der    ergrimmt   unnahbar   ist"  Yt.
4868:•  j.  ayanhö.zasta-  Adj.  'mit  nietallenen (eisernen)  Klauen';  varäzahe  ('eines Ebers'; ayüahs^äiahe  'saslahe  Yt.  ro.  70.
9029:?:t.?0.  —  Pü.:  fehlt;  Kyo.:  kF«ü.  ei\.:  n.i kiMii  li.iti  ,/,ijl  kitnad.  —  ')  Man  setit  wegen np.  kiihijsl  'Koloquinle'  die  Bedeutung  'Gift' oder  'plante  vüni'neuse'  an,  was  mir  nicht  lu passen  scheint.  Eber  ka-/<a'Uiy-  (s.  unter t,-nu,A„-y,  vgl.  lat.  A^/«.
16037:Ableit(mit^J-fl'fl'.Sj(S)aos*/oi>'-''™i-m, 'Herum-, Überfahren',  zum  V.  via-;  ai.  pariväha-  m. 'Überfluten',  -a^.  pamäi  'Flug'.  —  Npü.: /«r ra/lär,  erl.s  Üsyär  raoanda.  —  0  Der  Eber sucht  seinen  Gegner  zu  übertennen;  s.Biuaiu Tierleben.
21035:mit  /ra  'vollkommen  machen':  frä  U k}hrp3mca  t^ihmca  yaoidaiiäni  V.21.6. Komp.:  *yai>J-  n.+^iiä:  —  ti,  yii-  n.  (nur  in Verbindung  mit  iäm-\  \i.t./Hi;  s.  dazu  BcM. Grdr.»  /,  30l(?)S).  —  Vi.:  yHdäsreiülan,  yii- djirik  dätan,  eH.  (zuV.i).  l):  päk  karlan,  (zu V.  5.  31)!  kacvinäs  päk  däUan;  (fiir  PHP.): yHdäsr,  tiV:  päk  fai  niitrü;  Sü.  (tu  Y.  g): pjvayilum,  (lU  Y.  44);  favilTayilum).  ^  ")  Nur im  \tA.  yaoidayqn.  —  ')  Zur  Trennung  ».  unter 'sra:i/ä-.  Das  zyreilcyofli  ist  nach  dem  Metrum zu  streichen.  Jn.s  Auffassung  derStelle,  GlrPh. 3.  626  verstehe  ich  nicht  —  J)  Them.  — 1)  Ungmmmatische  Stellen.  —  s)  Ar.  'fiuij- soll  aus  "if^iis-  hervorgegangen  sein.  Eber dürfte  es  Kompoiittonsform  neben  *ifl^iS-  (mit
22823:Eber',
24292:allenthalben  gebietend',  vi-rät-;  aL  viraj-  m. 'Herrscher',  auchEN. ,  np.  fariaEN.»);  oder aber:  'Qber  Männer  gebietend',  haplol.  aus »viTa-räz-l).  —  ')  Them.  —  •)  Der  jedenfalls nicht  notwendig  'Eber'  bedeuten  muss.  — 3)  Statt  ar4äi  viTäfi^KVÜ)  ist  vielmehr  artak [Sp.  353  No.l2)i/i>-ä.3u  lesen.
28008:—  pä\aiibya  .  .  -toiibya  V.  5.  1 1 ;  — palnubya  ..  'taiibya  V.  2.  31;  ö".  29,  4".  40, s8.  19,  A.  4-  5.  Yd,  72;  —  Äiiz'fl  mrBihi hsxtim  . .  *°tagibya  variza  kvarltjm  Syao- 'kmm  Aog.  söf.;  —  manaahasca  *humaiti hisvasca  *häxii  'iayas{LS.)'Va  *hvarsii P.  2c?.  a)  gAw.  ID.  sva.  'durch  Handeln, Tun' 3':  at  yJ  aktm  dngvSitl  vacankä  vü ai  vä  manatskä  'tsibyä  va  vanlaitl  "wer aber  dem  Zlrv^enossen  mit  Worten  oder mit  Gedanken  oder  mit  seiner  Hände Werk  Übles  tut"  Y.  jj.  2.  et)  in  Ver- bindung mit  Syaö^ana-.  vahistim  hisvä uxiäi/. .  Sfdnä  . .  'tSibyä  syaö^anä  vimyat (Sp.  1377  0.)  Y.47-  2.  b)  Pv  gAw.  Lok! (Sg.  oder  Du.)  mit  V.  da-  oder  'kar-  'alicui (Dat,  Gen.)  in  manu  ponere':  'pasavJ'- di/  a*ura''rnasdä  manS  'tays  (LS.)''  aku- naui  "dann  gab  sie  AM.  in  meine  Hand" Bh.  4.  4;  —  kdka  asäi  drupm  dyam  "tayd (LD.)  "ob  ich  wohl  dem  A.  (dem  Reich der  Wahrheit)  die  Dr.  (das  Reich  der Lüge)  in  dieHände  liefern  kann?"  \.4.4. 1 4; jo.  85'.  2)  übertr.,  von  den  Klauen des  Ebers  (nur  Komp.).  1
30138:•  j.  hQ-  'Schwein,  Sau':  ahmai  . .  ajasai vinhrafnS  hü  (GS.)'^  kthrpa  varätahe (sd.)  .  .  arins  ".  .  in  der  Gestalt  eines Ebers  .  ."  Yt./rf.  15.
21393:1374
21413:1376
```


## [2026-10-16T05:14:00.606Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=22100 && NR<=22135 && /^ *1[0-9]{3} *$/' BRT.txt; grep -n -E '^ *13[0-9]{2} *$' BRT.txt | awk -F: '$1>21900 && $1<22900'; sed -n 22818,22830p BRT.txt; grep -n -E \"Blatt\" BRT.txt | head",
 "description": "Find BRT column numbers and entries"
}
```


### [2026-10-16T05:14:01.045Z] TOOL RESULT

```
21901:1306
21929:1308
21945:1309
22021:1318
22150:1337
22153:1328
22245:1333
22248:1334
22271:1336
22300:1338
22323:1340
22372:1343
22417:1345
22447:1347
22450:1348
22506:1349
22509:1350
22798:1365
22883:1369
22886:1370
-  Vgl.  :
■i  V.  a
.  6:    lit:
'iar-,  Sp.  936  U
'varäza-  m.  'Männchen  des  Schweins, Verbindung  mit  dem  Namen  für
Eber',
Schwein"':  As(sd.)  k»hrpa  'zähe , .  arÜnS*''
hakirH.janS  'räzahe  Yt  1.^.15. 1  Vgl.~»iwfläa.  EN.  —  ai.  wflj-ä-ia- m.,  np.fNpO.) guräi.  —  ')  R.  zu  tarian-  No.  3  und  oaai [  KÖieptm  E  783.  —  ')  Zur  Verbindung  von 1  varäta-  mit  arlan-  s.  vfiabkir  varähäih  RV. I       TO.  67.  7.
•  j.  »varäza-   m.  EN.   eines  Gläubigen: iivatö  'zahe  asacnS  Yt.  y.  96.
I  Vgl.  ^varäia-.     —    ai.   varähA-    m.    EN.,    np.
!  baräa  EN.
I  j.  varl  N.  ff:  s.  "/röU.vari.
I  j.  var>ana  F.  S:  lies  vartna%  s.  Vttr>nä-.
191:Ich  würde  bei  solcher  Sachlage  sinnloser  Raumvergeudung  geziehen  werden müssen,  hätte  ich  bei  jedem  Wort  die  ganze  Reihe  der  gleichen  oder  ähnlichen Fundatellen  aufgeführt  Wohl  aber  muss  man  gegebenen  Falls  in  der  Lage  sein, aUe  Belege  eines  Worts  bequem  einzusehen.  Diesem  Zweck  soll  die  nachstehende Konkordanz  dienen,  in  der  ich  nur  jene  Stellen  nicht  berücksichtigt  habe,  die sich  deutlich  als  Anführungen  aus  anderen  bekannten  Avestatexten  ■ —  insbesondere den  ^aSischen  —  kennzeichnen;  z.B.  Y.7.a4f.  -von  yehya  bis  _)'(i7'?(=  Y.  4:5.  7a und  41.  ${.),  N.  71  (Blatt  147,  Z.  14 ff.)  von  am>sa  sp»nta  bis  jasaiti  (=  Y.  Ä3f.); wo  es  nötig  schien,  habe  ich  das  Sigel  Z.  (Zitat)  verwendet  —  Das  Zeichen  :  soll
1993:48  (Blatt  /oa  5)  :  FrW.  /.  a 50  :  N-  46.
16105:•  j.  'parafrv-araätay-  Adj.  'des  Speer breit  ist  (d.  L  ein  breites  Blatt  hat)':  °lf''> ttqma  ahmt  'lis  nqma  ahmt  Yt.  i§.  48.
16994:*>  Über  die  Pflanien,  von  denen  die  Zweige geschnitten  werden  dürfen,  bieten  die  älteren Texte  keine  genaueren  Mitteilungen;  N.  90 PüErl.  (Blatt  16/.  ig)  ist  nicht  recht  deutlich. In  Indien  braucht  man  jetzt  ans  Metall  herge- stellte Zweige.  Die  Mindestzahl  wird  N.  po  auf drei  angegeben;  Y.  57.  6  werden  die  Zahlen 3>  S>  7>  9  genannt.  Als  Höchstzahl  etscheint N.  90  PüErl.  (Blatt  t6S.  1)  551.  Für  gewöhn- lich schwankt  die  Zahl  zwischen  5  und  33,  der Zahl  dcT  ra/rij'ö f airi!,Aä-!i/iHayB  (sd.).  Ober  Grösse und  Stärke  der  Zweige  s.  Y.  J/.  6,  N.  yo,  po, V.  /p.  19.  Die  Zusammenfassung  der  Zweige  zu einem  Bündel  geschieht  mittelst  des  aiwyio- ^nna-'Cürter  (Sp.  98  m.),  wozu  man  heutzutage ein  Datlelblalt  verwendet.  Die  gebündelten Zweige  ruhen  auf  dem  Gerätetisch  (aräVoi^) vor  dem  ZaMar.  Weiteres  bei  Hauo  Essays» 396  f.,  West  SBE.  5.  »84,  '8.  142.  3y-  162. DsT.  ZA.  /.  LXJüiL  Der  Terra,  techn.  für  das Bündeln  des  B.%  ist  ^slar-  'stemere'.  Dies  sowie die  Etymologie  von  b'  weisen  darauf  bin,  das« der  Gebrauch  des  B.  sich  aus  dem  'Spreiten der  Opferstreu'  (ai.  barhifah  slärimä)  entwickelt hat;  %.  datn  OuiENSEiic  Rel.  des  Veda  343.
21319:—  Pü.:  iurtäi.  —  ')  Die  beiden  in  der  NA- getrennten  Sätzchen  gehören  zusammen  und stehen  auch  zusammen  auf  dem  ersten  Blatt von  K  1 8  (mit  Npu. :  :*/  yaltaA  tisyär  täSad  laän mäita  an  himSr  iardan).  —  "I  Pü.  erl. :  mai.
22044:ai.  ävidat,  vividat,  vindäti,  vtdäyali;  vhi/da; viiläh;  my.viiidi/an"i,  %'b3\.gindag  'itheW  'Sl; Ur.  finnaim  'ich  linde'.  —  Pü. :  vindilan,  (zu Y.  49,  N.  16):  däaislan,  (lu  Y.  3t,  44)'  •«■'- linltaH,  (lU  Yt  6):  ditan,  (lU  Y.  30):  dälan. —  >)  S.  daiu  Bthl.  BB.  /o.  170,  WkIPli. iSff3.  396  (mit  JScHMU)T  Krilik  43).  —  *)  In visle,  mit  1  Blatt  /';  s.  No.  4.  —  3)  So  alle Hd>.,  Eva.  vindSt  (als  PraeL,  %  104.  I  No.  2) +fcm,  S  368.  49.   —    4)  Hds.  UU,  aber  Fa.:
22848:•  j.  vanka-  m.  "Blatt  (der  Ffianzen)': , ,  j.  'varffta-  1)  m.  a)  'locus  versandi,  Auf- 'kahe  F.  8.  ,  cntbaltsort'  (nur  Komp.).       b)  'BaU,  KJos' :
```


## [2026-10-16T05:14:06.795Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:341 2>&1 | head -60",
 "description": "Fetch Borhan page 341"
}
```


### [2026-10-16T05:14:07.241Z] TOOL RESULT

```
no scan of BQT covers printed page 341 (see 'scans' in refs_online.json)
```


## [2026-10-16T05:14:09.988Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nt=open('BQT_v1_pages.txt').read().split('\\f')\nimport re\nfor i,p in enumerate(t):\n  for kw in ['venik','vēnīk','vênîk','wēnīk','vaēnā','vaena','vaênâ']:\n    if kw in p.lower():\n      j=p.lower().find(kw); print('leaf',i,kw,repr(p[max(0,j-400):j+300])); break\nE",
 "description": "Search Borhan vol1 for venik"
}
```


### [2026-10-16T05:14:10.554Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:14:13.347Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nt=open('BQT_v1_pages.txt').read().split('\\f')\nprint(len(t))\nfor leaf in range(553,566):\n  p=t[leaf]\n  if 'بینی' in p or 'بيني' in p or 'بینى' in p:\n    print('== leaf',leaf); \n    for m in __import__('re').finditer('بینی|بيني|بینى',p):\n      print('   ',repr(p[max(0,m.start()-150):m.start()+250]))\nE",
 "description": "Look for bini in Borhan vol1 around p.341"
}
```


### [2026-10-16T05:14:13.971Z] TOOL RESULT

```
777
```


## [2026-10-16T05:14:16.912Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nt=open('BQT_v1_pages.txt').read().split('\\f')\nimport re\nfor leaf in range(540,580):\n  p=t[leaf]\n  nums=re.findall(r'\\b(3[3-5]\\d)\\b',p[:300])\n  hits=[m.start() for m in re.finditer('بینی|بيني|بینى|بینیست|بینی',p)]\n  print(leaf, nums[:3], len(hits), p[:80].replace('\\n',' '))\nE",
 "description": "Map Borhan leaves near printed p.341"
}
```


### [2026-10-16T05:14:17.284Z] TOOL RESULT

```
540 [] 0 بو عادران باینمهنی عربی است - و زمین شیار نکرده رانیز گفته اند - و جاو مقام و من
541 [] 0 بو همان - بسکون‌ناكث بروزن‌دودمانه پمعنی رحم است که زهدان و بچه وان باشد - و از 
542 [] 0 9 بکر اول وسکون ال تاتی‌سمعنی خوب وتيك‌باشد ۱ - از 4 - بکر اولر انی بالف کشیده. 
543 [] 0 قدید گویندش . # لها - بکس اول و ثانی بالف کشیده و بزای نقطه دار زده » اسب اصلی ز
544 [] 0 بهزا است ۱- ودر عربی بمعنی عجب ازتعجب_ وحلااه ازهللا کت باشد . لور آح بر وزن صحر
545 [] 0 ی ۳۹ ده بهر ام تل - هی مر فج توح کتک هر اهج -_بنتح میم و سکون جيم . عمرب بیرامه 
546 [] 0 له ره بر - بنتح بای‌ابجدبروزن رخده | فرشت . تم میوا حرختی است که سمخ آنر! مفل کر
547 [] 0 ون مت کاف فارسی وسکون‌نون و کاف‌دیگر؛ دارالملك نحاك در شهر بابل ساخته نود . بهشت
548 [] 0 غشب را فرو نشاند ۰ و او موکل است ب رگلوان و گومقندان , اکثر چهار پابان ؛ و تدییر
549 [] 0 ۳۷۹ - پمنحه 2 با جیم ونون بروزن‌دد و عجمان در ين روز عید کنند و جشن سازند » با ب
550 [] 0 یم - بر وزن فهیم : تلم یکی آزرابان و بزرگان هند ات۳٩‏ گزنشد ‏ لین ۰ بکس ۳ وزن نگ
551 [] 0 بجوم آب با بخون ۱ . باآب یا بخون ۱ . نی خساند و ق م کرد - و آحیخت و سرشت آب و با
552 [] 0 که پس رکیوین کودرز باشد . یحو هر - کنابه از مردم بی هنرویی عفل و هیچمکاره باشد .
553 [] 0 ابثان کتاب آسمانی است ت - و ممعنی حوش وشمور هم بنظرآعده است و در مویدالّلاء موش‌
554 [] 0 بید کیا بید گیا - بکر کاف فارسی و نحتانی بالف کشیده . نوعی از حرشف است که کنگی ب
555 [] 0 - ۳۳ 7 یر دک بنتم رابع بر وزن نك بی » بمعئی برژه انته ات صمفی‌باشف منتو, که‌بارز
556 [] 0 بیرونآحدن بیرون آ هلان - سسروف است که نفیض درون رفتن باشد- و کنابه از ترك اطاعت 
557 [] 0 پیمما -- لیستون ۱- نام کوهی است مشپور که فرهاد بفرمودة شیرین آنرا مبکند و کنابه 
558 [] 0 از "1 رن اه لیشه » بر وزن ربشه جنگل و نستانرا گونند و بعربی اجم خوانند؟ - وسازی 
559 [] 0 ۳۹۳6 سد بیقاد ه بنتح اولبروزن نیزار , سرزنش وطعنه باشد. بیغاره بر وزن گهواره » ب
560 [] 0 بنم ثانث مر وزث میگفت اه ستارژ زهره را گوبند . بیلقان ‏ بنتح اول و و بر وزن نهرو
561 [] 0 ۳:۱ ماه است که بعربی شه ر گوبندا . که مردمرا در حالت ماشفه دیده میشوده وآنرا مرب
562 [] 0 نبویرد شده است واوباریدتن بفتح همزه بمعنی فرو بردن و بلم کردن باشدا . ۱ ایو بر ك
563 [] 0 ۳۳ خوانند . لیو ث » بر وزن ربوند » بمعنی غدر: است که بیوفابی کردن باشد . ی ۵ » ب
564 [] 0 گفتار 3 از کاب برهان قاطم درحرف بای فارسی با حروف نبجی مبتتی بربیست و يك بیان و 
565 [] 0 با آ هو - بالف بسدکشيده و های بواو رسیده » باصطلاح بنایان خانةٌ شش بهلو باشد وآن
566 [] 0 باتو ك‌ ثالت بواو رسده: خانه ومنزل و عفرب باشدا - و ظرفی را نیز کوبند که از گنل 
567 [] 0 او نیز گویند . ۱ پاچیله » بر وزن پانیله . کنش و پا افزار باشد . پاخره ‏ بفتح خای
568 [] 0 بممنی سیه (۱) باشد , و آن خربنن چیزیست امرو که فردا مت ندهند ٩‏ , باذشاه ۴ نامی 
569 [] 0 4و۳ بادم۱ بروزن ساده ,که خرو کاورا کوبند - و چراگاه اسبان و شتران و کاوان را بز 
570 [] 0 ۳9 ۱ با نگ - بسکون الت بی وزن آپرنگ » به‌نی امک ات و آن چیزی باشد که در يك که تر
571 [] 0 
572 [] 0 ۲۶ ۵ ما > > 15 )-6( > ۶2 ۵ تا ور 0 > ی و سس (۵-) هط - ۵0 >> -< (و-وه-) ۵ ۳ (و-رع
573 [] 0 - وس باد گی ه بسکون ات و کاف فارسی بتحتانی رسیده . قحبگی راکوبند ۷. پاد گین - با
574 [] 0 داریلب ْ ۱ 4 ۲و بمعنی جزئی باشد که دربرابر کنی استوپاز تاربان بمعنی جزئیات؟ . یا
575 [] 0 کتاب زردشت است ؛ و برعکس اینهم کفته اند یعنی زند(۱) تفسیر پاژند(۲) است. وبعضی وگ
576 [] 0 بر ون دلدگار » بیعتی سار است که فگد باشد؟ _ ولگد کوب راه مگفتماند - و بضم ثالت د
577 [] 0 ۳66 77 و همال پاش ۷ - . . باشنك - بروزنآونگ , خوشه کوچكث انگور را کویند - و خیار
578 [] 0 .و شخصبکه اسباب خود را نمام بباژد - و زاهد و مجرد و عاشقی که‌بنظر پاك بممشوق نگر
579 [] 0 ایا پا کنك - بروزن پازند . مطلق باقوتر) کوبند اعم از زرد و سفید و سرخ » و باین >
```


## [2026-10-16T05:14:21.845Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nt=open('BQT_v1_pages.txt').read().split('\\f')\nimport re\nfor leaf in (561,562,563):\n  p=t[leaf]\n  for m in re.finditer(r'بین|بين',p):\n    s=p[max(0,m.start()-60):m.start()+200].replace('\\n',' ')\n    if 'nose' in s.lower() or 'Nase' in s or 'vin' in s.lower() or 'دماغ' in s or 'ven' in s.lower() or 'پهلوی' in s: print(leaf,'::',s); print()\nE",
 "description": "Find bini entry text in Borhan leaves"
}
```


### [2026-10-16T05:14:22.298Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:14:25.494Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nt=open('BQT_v1_pages.txt').read().split('\\f')\nimport re\nfor leaf in range(559,564):\n  p=t[leaf]\n  for m in re.finditer(r'دماغ|vê|vē|vi?n[iî]k|bîn|bīn|Nase|nez',p):\n    print(leaf,'::',p[max(0,m.start()-250):m.start()+250].replace('\\n',' ')); print()\nE",
 "description": "Broader search for bini entry"
}
```


### [2026-10-16T05:14:26.056Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:14:29.362Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E '.{0,200}(v[eêē]n[iîī]k|vaênâ|vaēnā|vaena).{0,200}' BQT_v1.txt BQT_alt_v1.txt BQT_v2.txt | head; grep -n -o -E '.{0,100}b[iîī]n[iîī].{0,100}' BQT_alt_v1.txt | head",
 "description": "Grep raw Borhan OCR for venik"
}
```


### [2026-10-16T05:14:34.756Z] TOOL RESULT

```
ugrep: error: error at position 151
vaēnā|vaena)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
                    exceeds complexity limits___/


ugrep: error: error at position 126
-\xbf][\x80-\xbf]*){0,100}
                          \___exceeds complexity limits
```


## [2026-10-16T05:14:37.379Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for f in BQT_v1.txt BQT_alt_v1.txt; do python3 - \"$f\" <<'E'\nimport sys,re\nt=open(sys.argv[1]).read()\nfor m in re.finditer(r'v[eêē]n[iîī]k|vaênâ|vaēnā|vaena|b[iîī]n[iîī]\\b',t):\n  print(sys.argv[1],'::',t[max(0,m.start()-300):m.start()+200].replace('\\n',' ')); print()\nE\ndone | head -40",
 "description": "Python search raw Borhan OCR for venik"
}
```


### [2026-10-16T05:14:37.886Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:14:42.634Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; ls pageimg ocr ocr/BQT 2>/dev/null | head -30; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; curl -sL -o $S/bqt522-n562.jpg 'https://archive.org/download/borhan-ghate-v1/page/n562_w800.jpg' -w '%{http_code} %{size_download}\\n'",
 "description": "Check cached pages and fetch Borhan leaf image"
}
```


### [2026-10-16T05:14:45.900Z] TOOL RESULT

```
pageimg:
Permissions Size User   Date Modified Name
.rw-r--r--   60k sfmqrb 14 Oct 22:19  bqt_v3_p150-150.png
.rw-r--r--   51k sfmqrb 14 Oct 22:19  bqt_v3_p600-600.png
.rw-r--r--   75k sfmqrb 14 Oct 22:19  bqt_v4_p150-150.png
.rw-r--r--   41k sfmqrb 14 Oct 22:19  bqt_v4_p500-500.png
.rw-r--r--   55k sfmqrb 14 Oct 22:19  bqt_v5_p8-008.png
.rw-r--r--   42k sfmqrb 14 Oct 22:19  bqt_v5_p30-030.png
.rw-r--r--   49k sfmqrb 14 Oct 22:19  bqt_v5_p150-150.png
.rw-r--r--   44k sfmqrb 14 Oct 22:19  bqt_v5_p250-250.png
.rw-r--r--   79k sfmqrb 14 Oct 22:19  irn_p100-100.png
.rw-r--r--   52k sfmqrb 14 Oct 22:19  irn_p101-101.png
.rw-r--r--  5.5k sfmqrb 14 Oct 22:19  unknown_p3-003.png
.rw-r--r--   48k sfmqrb 14 Oct 22:19  unknown_p40-040.png
.rw-r--r--  267k sfmqrb 14 Oct 22:19  userbook_p1.png
.rw-r--r--   59k sfmqrb 14 Oct 22:19  userbook_p2.png
.rw-r--r--   59k sfmqrb 14 Oct 22:19  userbook_p200.png
.rw-r--r--   70k sfmqrb 14 Oct 22:19  userbook_p300.png

ocr:
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  AFM
drwxr-xr-x     - sfmqrb 14 Oct 22:47  ARY
drwxr-xr-x     - sfmqrb 14 Oct 22:19  BLY
drwxr-xr-x     - sfmqrb 14 Oct 22:50  BOOK
drwxr-xr-x     - sfmqrb 16 Oct 01:14  BQT
drwxr-xr-x     - sfmqrb 14 Oct 22:48  FFD
drwxr-xr-x     - sfmqrb 14 Oct 22:19  HRN
drwxr-xr-x     - sfmqrb 14 Oct 22:19  IRN
drwxr-xr-x     - sfmqrb 14 Oct 22:27  PLA
200 221215
```


## [2026-10-16T05:14:48.044Z] TOOL CALL #23: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt522-n562.jpg"
}
```


### [2026-10-16T05:14:48.070Z] TOOL RESULT

```

```


## [2026-10-16T05:14:51.443Z] TOOL CALL #24: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; curl -sL -o $S/bqt522-n561.jpg 'https://archive.org/download/borhan-ghate-v1/page/n561_w1000.jpg' -w '%{http_code}\\n'",
 "description": "Fetch Borhan leaf 561 image"
}
```


### [2026-10-16T05:14:53.340Z] TOOL RESULT

```
200
```


## [2026-10-16T05:14:55.409Z] TOOL CALL #25: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt522-n561.jpg"
}
```


### [2026-10-16T05:14:55.430Z] TOOL RESULT

```

```


## [2026-10-16T05:15:02.229Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; mkdir -p data/verification/sources/refs/ocr/BQT; cat > data/verification/sources/refs/ocr/BQT/341.vision.txt <<'E'\n[BQT vol.1 p.341 = archive.org borhan-ghate-v1 leaf n561; read from page image by claude (page-522 verification)]\nMo'in footnote (asterisked, to headword بینی at foot of page):\n* بینی - سمنانی vînî ، مازندرانی vênî ، « اسفا ۱ : ۲ ص ۴۹ » ، پهلوی vênik ،\nاوستایی vaênâ « اسفا ۱ : ۲ ص ۷۶ » ، بری bînî « ك . ۱ ص ۲۸۸ » ، سمنانی väni ؛\nسرخهٔ ven ، لاسگردی vinî ، شهمیرزادی vinî « ك . ۲ ص ۱۸۵ » ؛ جزء برآمدهٔ صورت که عموماً\nبین پیشانی و دهان قرار دارد و قوهٔ شامه در جوف آنست .\nE\nfor p in 1779 1780 2263; do echo \"#### $p\"; python3 tools/ref_page.py BQT:$p --image 2>&1 | tail -40; done",
 "description": "Save Borhan 341 vision text and fetch other Borhan pages",
 "timeout": 300000
}
```


### [2026-10-16T05:15:24.021Z] TOOL RESULT

```
#### 1779
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1779.png
REF: BQT:1779  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 576  OCR-lang: fas

بیان نهم
در کاف فارسی با رای بی‌نقطه مشتمل بر دویست و سی و يك لغت و کنایت
گر < بفتح اول وسکون ثالی»مخقف! کر و آهنی پهن باشد دسته دار و در دو طرف آن
باشد که كلمةٌ شرطه است9 - ونام جوشعی‌است | دیسمان بندند یکی دستةٌ آنرا بگیرد و دیگوی
مشهو رکه بعربی جرب کوبند ؟ - ویمعنی مراد | ریسمانرا بکشد تا زمین شیارکردة ناموار را
ومقصود باشد ۴ - و بمه‌نی کننده و سازنده هم بدان هموار کنند وآ ترایعربی ملفه‌ومواط(۱)
هت ۴ همچو کوزه کر وکاسه گر وامثال آن , | خوانند ۸ .
ومر‌ادف گارباشد همجو آموزکار وآموز کر که گر آد بکر اول بروزن فتاد» جامهٌ
ازهر دومعنی فاعلیت مفهوم میگردد وقتی که با | کهنه راکوبند .
کلمدٌدیگن ترکیب‌شود - ویتم‌اول دام رودخانه - گرادون- با رای قرشت بر وزن
است در سرحد ملك غزان » وباین معنی باکاف | فلاطون » نام جوششی است کهآ ترا داد خواتند
تاری مشهور است * . وبعربی قوباکویند ‎٩‏ -
گرا - بفتح اول‌وئانی مشددبالف کشیده. گر ان « بنم اول بروز ن گداز , بممنی
بمعنی بنده باشد که در مقابل آزاد اسمت ‎٩‏ - | خول نرباشد که جفت خو ماده است*۱-وخرام
وحجام وسرتراش ودلا را نیز کوبند۷ »وکاهی | ورفتاری که از روی ناز وتکبر وتبختر باشد۱۱ »
این لفظ را بطریق :دشنام هم بزبان آورند- | و بسنی کوبند بمعمنی خرام و رفتار از روی ناز
(۱) خم : منقه ومتواط -
۱ رد: اکر؛ کردی16۳ع (اکر) ابا ۰.۳۵۷ ۴ - مرضی‌است که‌دانه‌هاي کوچك
پربدن انان‌وجانوران پدید آرد وخارش کند ومرٍض راگرکین» (مغفف آن : کر کن) کویند.
اوستا - 827671 (جرب) کردی 81۳ (جرب) » بلوچی 827 (پییسی » جرب) «* اسشق ۲۸۹۵
و رك : هوبشمان » اساً ؛ پهلوی 82۳ (جرب) « دارمستتر » تبعات اج ٩ص‏ ۴۹۵ ۰
۴ -رك :کر . ۴ - اوستا - ۷2۵۳۵8 - (ساخته) » پپلوی 1۳2۲ - :887-.هندی
باستان - 8۳2 - « اسشق ۸۹۶ »کردی 56۲ - (ویرانکر [ویران کننده]) « ژایا س4۳۹ »۰
8 ر4 :کر .
‎٩‏ -کفت‌این گرای خاین را ببین ماکمان برده که باشد او امین .
مثنوی مولوی هرشیدی» .
۷ - شيعهٌ پر خو نکه‌کرا می مکد بر آمید نفع دل خوش میکند .
مثنوی مولوی «رشیدی» .
۸ ظ . مصحف «گراز» (ه.م.) ‎٩‏ - رك : رشیدی .
* - اوستا - ۷8۳۵22 (کراز) » پهلوی ۷8737 (لوشته میشود ۷8726) ۰ آرمنی‌ع
2 فهندی باستان - ۷2۳2046 (گراز) »کردی ۳۵۲82 « اسشق ۰۸۹۹
۱- مصدر آن «گرازبدن» است .

#### 1780
هم (۱) میگویند که بدان زهین را ب
و بسی گودند بیلی باشد بز رکه که دو حلقةٌ گر اذ ات - بر وزن خراسان . بممنی
آهنین بردوطرف‌آن تعبیه کرده باشند وربسمانی | جلوه‌کنان وخرامان باشد ۷ - وجمع کراز هم
برآن بندند و مزارعان زمین شیار کرده را بدان | اهمت ۸ .

زگ خم۱:-هم .- ۱

۹ - ر4: ح ۱۱صفحهٌ قبل. ۴ - اسم قاعل مرخم . ۱

۴ - بفرمود تا کارگر با گراز بیارند چندی ز راه دراز

فرود آمد از امپ شاه بلند شراعی زدند از بر کشتمند

«فردوسی . شاهنامة بخ ج۷س ۱۹ ۰
ورك : فهرست ولف ۰ قی : مازندرانی «کرواز» (بیل کم پهنا و دراز) «فرهنگه نظام» »کیلکی
2 (بعمن معنی) . ۴ - این لفت «کراز» است و عربی است . «کراز کغراب .
شیشه وکوزهٌ سرتنگه .«کرزان بالکر جمع» « منتهی الارب » و رك : رشیدی - در لفت فرس

«گرلز» آمده بهمین هعنی واین بیت را شاهد آورده : 1

با نعمت تمام پد رگاهت آمدم امروز با کراز وچوبی‌همی‌روم: ‏ فاخر«لغت‌فرس4۱۹۸.

8 - مصحف «کواز» (ه.م.) «رشیدی» . ‎٩‏ - بمناسبت قوت جانورمز بور(گراز).
در بهرام بت (اوستا) » بهرام » فرشتةٌ پیروزی ده ترکیب جممانی بخودکرفت وخودراپزرتشت
تمود ؛ از هريك ازین ترکیبهای مختلف که اسب وشتر و ورزاو وغیره باشد يك قم قوتی اراده
شده است . دربند ۱۵ بدت مذکور بهرام صورت کرازی جلوه میکند . بهمین مناسبت فوت‌این
جالور است که ورازه ۷۵7222 ام اغضخاس آمده از حمله درد ‎٩٩‏ فروردین بشت . در میان
نامداران وشاهزادگان ابران قدیم وممالك همایه مثل ارمنتان والبانی‌اوغیر» بگروهی برهیخوریم
که ام آنان با «ورازه» تر کیب بافته است هثل ورازبنده , ورازدات » ورازدخت » ورازسورن,
وراز پیروز» ورازمهر» ورازلرسی‌وغیره . « پور داود . بشتها ج اص 20۹ح۳ ورك : یوستی. نام
نامه . درین بیت بمعنی شجاع وپعلوان آمده :

دور سپهرمثل توهر کز تیاورد ازهفت پشت پهلوشیرافکن وکراز.

عمید لوبکی «رشیدی» .

۷ - صفت فاعلی از «گرازسن» . ۸ - فردوسی بهر دو معنی آورده :

کرازا نگرازان . نه آگاه ازین که بیژن نهادست بر بور زین. «رشیدی».

#### 2263
(no exact page map; using offset -1917 -> pdf page 346; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/2263.png
REF: BQT:2263  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 346  OCR-lang: fas

۹۳۳ وراغ
سینه راکوبتد ۱ که عربان صدر خوانند. وراز؟.- جنم اول» بروزن ومعنی کراز
ورا؟ « بروزن سرا . مغفف اورا باشی | است که خوترباشد؛ وبفتح اول وتشدید ثانی‌هم
چنانکه گوبند « ورایین که با ما چپا میکند » | باین معنی گفته اند.
بمنی اوراً به‌بین » و« ورا بده » پمنی اورا بده . وراروده* « بفتح اول وهمزه بر وزن
ور ار ود؟ - بارای بی‌نقطه‌رواومجپول | دمك سود » بمعنی ورارود است که ماوراء الثهر
بروزن غم‌آلود » ترجمهٌ ماوراء النهراست, وآن | باش ‏ ,
ملکی‌است مشهور . وراغ ۱ - بنتح اول و ناك بالف
۹ - پهلوی ۷8۲ (سینه » کمر) «اوتوالا 4۸ > ؛ رك :بل +
۴ - از : و (* آو , وی )+ را ( علامت مفعول صربح ) : « ورا » وی را بود.منجيك
(ترمذی) گفت :
نداند مشعیذ ورا باد چون نداند مهندی ورا درز (دور.دهشدا) چند.»
« لفت فری مصحح اقبال ص۱۵ . و درلفت فری چاپ هرن : درد چند .
۴ - اسدی کوید : « ورارود » ماوراءالثهر است. فردوسی (طوسی) کوید :
اگر پهلوانی ندانی زبان ورارود را ماوراالنهرخوان.» «لفت فری ۱*۰۹ ۰
ورك : صحاح‌الفری « طاعتی ». جهانگیری آرد : « ورارود با اول مفتوح و رای ثالی مضموم وواو
مجهول و « وراز رود » با اول مفتوح بشانی زده والف هفتوح بزای منقوطه زده و « ورز رود » با
اول مفتوح بثانی زده و زای منقوطهٌ مکسور و رای مضموم » دام ماوراءالشهر است » حکم
فردوس ی گفته :
اکر پپلوانی ندانی زبان ورا رود را ماوراالنپرخوان.»
در صحاح الفری فیز آمده : * ورارود ماوراء‌النهر است » ۶ فرهنگه تظام » در فهرست‌ولف مستقلا
« ورارود » نیامده » اما « ورز رود ؟ را بمعنی (سر زمین ماوراءالنهر) آورده و بفرهنکه عبدالقادر
شمارء ۲۹۶4 ارجاع کرده است؛ ولی بیت مزبور را درشاهنامه‌های مأخذ خودٌ لیافته است رشیدی
گوید : « آزا رود و وزارود » ماوراوالنهر . فخری کوید :
يك موی مباد ازسر او کم که جهانرا آن موی به از جمله سمرقند و ازارود.
و رودکی ( چندن است گوید :
اکر پپلوانی ندانی زبان وزا رود را ماورا الثهردان.
و گاهی‌بند الف وغیرمد وحذف کلمهٌ رودئیز آید چنالچه گوبند «سیب آزا» یمنی‌سیب‌ماوراءالثهر.»
موْلف سراج « ازارود» ( بالکس و بفتح یز ) بدین معنی مخفف ( ازان روی رود ) و * ازرود»
بحذق الف دوم مخفف آن » وآزا رود بمد وآزا ننها بمد و بغیر مد غیر ابیت » و « ورارود (ثانی
رای مهمله ) غلط وصحیف « ازا رود » چه ورا بمهنی1 نطرف عربی‌است نه پپلوی » وتبدیل الف
بواو جائز «حاشيةٌ فرهنگه رشیدی : آزارود » ولی وجه اشتقاق سراج درست نمی‌نماید.«ورازود»
هم که برهان آورده» تصحیف است. ۴ << کراز («م.) » طبری ۷87۵7 (کراز) « واژه
نامه ۷۸۷ *. ۰ - رك : ورارود . ۹ <ورغ (.م.)
```


## [2026-10-16T05:15:30.110Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nt=open('BQT_v1_pages.txt').read().split('\\f')\nimport re\nfor leaf in range(470,490):\n  p=t[leaf]\n  print(leaf, p[:70].replace('\\n',' '), '| varg' if re.search(r'varg|valg|varek|vareka',p) else '')\nE",
 "description": "Locate Borhan p.260 leaf"
}
```


### [2026-10-16T05:15:30.513Z] TOOL RESULT

```
470 بر جوسیوی ۳ بر توسوسن سین اول مک ور وتحتانی بواو دسیده و بسین دوم زده» 
471 <- ٩ کرده باشند برجاس گوبند» وانرا که در زمین نمانه کنند حدف خوانند .  
472 برخقد سر کردن بر خلد‌سر کرش - اجه اتیابداری همیشگی و جاودالی‌بانتن باش 
473 ۳و۷ بر دفتر افگندن - کنابه از نوشتن باشف . 0 بر دلگ« بروزن‌مرداه . اضا 
474 برزستد ۱ 3 ۰ ج ووات بنابان را نیز کفته‌اند . بر ددن - بر وزن‌ک رکدن .  
475 ی ۷ سس و بکسر اول تابه باشدکه از کل سازند و نان بر بالای آن پزند ٩‏ سك 
476 " بر‌سان « بنتح اول می وزن نرسان : دوشاب میاء رنگه خوشبوی را گویند - و 
477 ده نسکهای عشهور زند )۱( آست سی و پنج برسم بدست گیرید ؛ و بجهت نك بشت ٩ 
478 می شیر آن" زین نهادن سرخ‌مرد گوبند و بعربی عصا الراعی خوانندا ۰ بر شیر 
479 -- ۷6 سس بیشتراوفات‌بخر وکاو دهند» وبخورند وبسنی‌دمگر گفته‌اند ترمایست 
480 بر فشا ندن‌ذست ه کنابه ازرقصدن بر قنجاك » بنتح او و سکون ثالی و فتح ثا 
481 ۳ بر گ ید - معروفست - و نوعی از پیکان تیر هم هست که آنرا بهیشت بر کك ب 
482 باقاف فارسی هم آمده است- و بکر انی‌طایفه‌ای بر لنگار دن ع کنابهاز کریخ 
483 5 رما ۱ ه بر وزن نتزك ؛ دام جابی و مقامی و ولایتی است - و لقب جعفر پدر 
484 برحه بر هه ۱ « بروزن کرعه: مثفب‌درود گری باش که بدان چوب و نخته سوراخ  
485 ۱۲ حسه برد ی ۰ این شممها که در دل بسحق بر فروخت از رهگذار نور(۱) برنج  
486 برنداف بر ناف س بفتح اولو انی و سکون‌ثالث و رامع بالف کشیده و فا زده » 
487 سای هس و بفتح او وسکون ائی‌نام ماه - و ستارمشتری باشد ۱ - و بفتح اول و 
488 بردث لر ون ه بکراول بروزن فون,»مخنف بیرون است ٩‏ - و بممنی برای وبجهت  
489 است درحضرموت. کویت. درآنجا چاهی امت که ارواح کفار و عنافین آنجا جمم شو
```


## [2026-10-16T05:15:33.467Z] TOOL CALL #28: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; curl -sL -o $S/bqt522-n481.jpg 'https://archive.org/download/borhan-ghate-v1/page/n481_w1000.jpg' -w '%{http_code}\\n'",
 "description": "Fetch Borhan leaf 481 image"
}
```


### [2026-10-16T05:15:34.926Z] TOOL RESULT

```
200
```


## [2026-10-16T05:15:37.187Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt522-n481.jpg"
}
```


### [2026-10-16T05:15:37.233Z] TOOL RESULT

```

```


## [2026-10-16T05:15:38.421Z] AGENT

This is p.261; I need p.260 (leaf 480).


## [2026-10-16T05:15:40.558Z] TOOL CALL #30: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; curl -sL -o $S/bqt522-n480.jpg 'https://archive.org/download/borhan-ghate-v1/page/n480_w1000.jpg' -w '%{http_code}\\n'",
 "description": "Fetch Borhan leaf 480 image"
}
```


### [2026-10-16T05:15:42.204Z] TOOL RESULT

```
200
```


## [2026-10-16T05:15:44.498Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt522-n480.jpg"
}
```


### [2026-10-16T05:15:44.515Z] TOOL RESULT

```

```


## [2026-10-16T05:15:55.403Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; cat > ocr/BQT/260.vision.txt <<'E'\n[BQT vol.1 p.260 = archive.org borhan-ghate-v1 leaf n480; read from page image by claude (page-522 verification)]\nHeadword (left col.): ... بفتح اول و سکون ثانی و کاف فارسی ، برگ درخت باشد که بعربی ورق گویند - و بمعنی ساز و نوا و اسباب و جمعیت و دستگاه و سامان و سرانجام باشد عموماً و سامان و سرانجام مهمانی را گویند خصوصاً ...\nMo'in footnote:\n* برگ - بفتح اول در پهلوی valg ، اوستا varəka «بارتولمه ۱۳۶۷» «نیبرگ ۲۳۲»\nو نیز در پهلوی vark «تاوادیا ۱۶۶» ، گیلکی balg ، فریزندی ، برنی و نطنزی valg\n«ك . ۱ ص ۲۸۶» ، سمنانی varg ، سنگسری و لاسگردی valg ، شهمیرزادی barg «ك . ۲ ص\n۱۸۱» ، اشکاشمی barg ، وخی palc ، سریکلی pork ، شغنی pårg ، یودغا panuk «گریرسن\n۷۵» خوانساری valg «سالنامهٔ گلپایگان ۴۷» ؛ جزوی از گیاهان که نازک و پهن است و از کنار\nهای ساقه یا شاخه ها میروید ، ورق .\nE\nfor f in MON_part1.txt MON_part2.txt; do python3 - $f <<'E'\nimport sys,re\nt=open(sys.argv[1]).read()\nfor kw in ['بَرم','برم ','بَرگ','برگ ','گُراز','گراز','وُراز','وراز','بینی']:\n  for m in list(re.finditer(r'\\n[^\\n]{0,4}'+kw,t))[:3]:\n    s=t[m.start():m.start()+260].replace('\\n',' ')\n    if '[' in s[:60] or '(اِ' in s[:60]: print(sys.argv[1],kw,'::',s)\nE\ndone",
 "description": "Save Borhan 260 vision text; grep Mo'in"
}
```


### [2026-10-16T05:15:56.528Z] TOOL RESULT

```
MON_part1.txt برم  ::  برم می‌دهد.   برماسیدن: 0۸۲83-۲ [- بر ماسیدن]  (مسصمع.) (س‌ ماسید» بر ماسد؛ خواهد  برماسید» بیرماس؛ برماسنده؛ بر ماسیده)  سودن دست بر جبزی» لمتن کردن: سودن  عضوی بر عضو دیگر.   برمالیدن: ۸۲-21-00 (مص‌ل.) نور  دیدن» طی کردن. بالا کردن آستین و باچة  تشان: [ کند
MON_part1.txt وراز ::  زورازما(ی): (0ةص(ه)۳22: [-  زورآزماینده| (ص‌فا.) آنکه زور و نیروی  یار ۷۱ معرض آزمایش در آورد؛ کسی  که با دیکری دست و پنجه نرم کند. پهلوان.    ۱ زورازسایی: -22)6(00217-.2 (حامص.)    نشان دادن زور و نبرو» دست و پنجه نرم  کردن. بهلوانی   زوراور: 222 (- زورآورند
MON_part2.txt گراز ::  گرازشی: ۵022۲5 [ - گزارشن | (امسص.)  انجام دادن (غم.) پرداخت. تادبه (غم.)  تبلیغ (بیغام» پیغمیر ی و غبره). سان» اظهار.  شرح و تفصیل» تفسیر. ترجمه. و  خرج. . طرح (نقاشی). تشتکین؛ هد به.  راپرت (فره. ) گزارش خواب: وی  کر 7ج (ص‌فا.) بیان کننده.    7    کز فرهنگ 
MON_part2.txt وراز ::  اهورازدا فروهری دارد.   فروهشتن :100165 [- فنروهلیدن]  (مص‌م.) پایین گذاشتن؛ بر زمین نهادن.  آویزان کردن. (مص‌ل.) بابین افتادن. سست  گشتن. آویزان شدن.   فروهشته: (108000.] (ص‌مف.) پایین  گذاشته. سست. آوایزن کرده» آويخته. موی  ( گیسوی) فروهشته: موی (گیسوی) آوی
MON_part2.txt بینی ::  بینیش غالاً فرو ریزد.   فینه: (0-)102] [- فینو] (.) کلاهی پشمی  سرخ (غالبا)» سفید یا به رنگ دیگر که  مصر بان و بعض هندیان (و سابقاً تسرکان    مات )مدش کذار ند   فیور: 1۷57 (.) (فز.) سیمی فلزی که در  مسیر جریان الکتر یک تعبیه کنند. اگر جریان  برق بسیار قوی و خ
```


## [2026-10-16T05:16:00.995Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for w in برم گراز وراز برگ بینی; do echo \"### $w\"; curl -sL \"https://vajehyab.com/moein/$(python3 -c \"import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))\" $w)\" | python3 -c \"\nimport sys,re,html\nt=sys.stdin.read()\nt=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)\nt=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\\s+',' ',t)\ni=t.find('معین'); print(t[:0]); \nfor m in re.finditer(r'\\[ ?په|\\(اِ\\.\\)|\\(اِ\\)',t): print('  ..',t[max(0,m.start()-80):m.start()+250]); \n\" | head -12; done",
 "description": "Fetch Mo'in entries from vajehyab"
}
```


### [2026-10-16T05:16:02.930Z] TOOL RESULT

```
### برم

  ..  همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه برم فرهنگ انتشارات معین (بَ رَ) (اِ.) 1 - چوبی که پارچه ای ملون بر بالای آن بندند و در میدان نصب کنند برای آگاه کردن مردم از کشتی پهلوانان . 2 - چوب بندی را گویند که تاک انگور و بیارة کدو و خیار و غیره را بالای آن گذارند؛ داربست . برم در فرهنگ‌های دیگر معنی برم در لغت‌نامه دهخدا مع
### گراز

  ..  + همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه گراز فرهنگ انتشارات معین (گُ) [ په . ] (اِ.) 1 - خوک نر. 2 - بیل . گراز در فرهنگ‌های دیگر معنی گراز در لغت‌نامه دهخدا معنی گراز در فرهنگ فارسی عمید / قربان‌زاده معنی گراز در دیکشنری فارسی به عربی معنی گراز در دیکشنری فارسی به انگلیسی معنی گراز در گویش اصفهانی معنی گراز در گویش کر
  .. یق مترادف متضاد مشابه آوا متن آغاز قافیه گراز فرهنگ انتشارات معین (گُ) [ په . ] (اِ.) 1 - خوک نر. 2 - بیل . گراز در فرهنگ‌های دیگر معنی گراز در لغت‌نامه دهخدا معنی گراز در فرهنگ فارسی عمید / قربان‌زاده معنی گراز در دیکشنری فارسی به عربی معنی گراز در دیکشنری فارسی به انگلیسی معنی گراز در گویش اصفهانی معنی گراز در گویش کرمانشاه مع
### وراز

  ..  + همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه وراز فرهنگ انتشارات معین (وُ) (اِ.) گراز، خوک نر. وراز در فرهنگ‌های دیگر معنی وراز در لغت‌نامه دهخدا معنی وراز در فرهنگ فارسی عمید / قربان‌زاده معنی وراز در گویش مازنی واژه‌های مشابه وازدن وازده وازر وازع وازلین وازدگی واز پس وازنک ولنگ و واز خرید اشتراک افزودن واژه افزونه مرورگر
### برگ

### بینی
```


## [2026-10-16T05:16:08.903Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://vajehyab.com/moein/%D8%A8%D8%B1%DA%AF\" \"https://vajehyab.com/moein/%D8%A8%DB%8C%D9%86%DB%8C\" \"https://vajehyab.com/dehkhoda/%D8%A8%D8%B1%D9%85\" \"https://abadis.ir/fatofa/%D8%A8%D8%B1%D9%85/\"; do echo \"### $u\"; curl -sL \"$u\" | python3 -c \"\nimport sys,re,html\nt=sys.stdin.read()\nt=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)\nt=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\\s+',' ',t)\nfor kw in ['فرهنگ انتشارات معین','آبگیر','حوض','بینی (','لغت‌نامه دهخدا برم']:\n  for m in list(re.finditer(kw,t))[:3]: print('  ..',t[max(0,m.start()-100):m.start()+400])\n\"; done",
 "description": "Fetch more Mo'in and Dehkhoda entries"
}
```


### [2026-10-16T05:16:12.234Z] TOOL RESULT

```
Exit code 1
### https://vajehyab.com/moein/%D8%A8%D8%B1%DA%AF
Traceback (most recent call last):
  File "<string>", line 7, in <module>
    for m in list(re.finditer(kw,t))[:3]: print('  ..',t[max(0,m.start()-100):m.start()+400])
                  ~~~~~~~~~~~^^^^^^
  File "/usr/lib/python3.14/re/__init__.py", line 285, in finditer
    return _compile(pattern, flags).finditer(string)
           ~~~~~~~~^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/re/__init__.py", line 350, in _compile
    p = _compiler.compile(pattern, flags)
  File "/usr/lib/python3.14/re/_compiler.py", line 762, in compile
    p = _parser.parse(p, flags)
  File "/usr/lib/python3.14/re/_parser.py", line 973, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "/usr/lib/python3.14/re/_parser.py", line 460, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
                ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                       not nested and not items))
                       ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/re/_parser.py", line 858, in _parse
    raise source.error("missing ), unterminated subpattern",
                       source.tell() - start)
re.PatternError: missing ), unterminated subpattern at position 5
  ..  معنی برگ | فرهنگ انتشارات معین | واژه یاب 26 فرهنگ همه دیکشنری مترادف طیفی آزاد + همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه برگ فرهنگ انتشارات معین (بَ) ( اِ.) 1 - توشه ، آذوقه . 2 - اسباب و اثاثیة زندگی . 3 - میل ، آرزو. 4 - اسباب و سامان . برگ در فرهنگ‌های دیگر معنی برگ در لغت‌نامه دهخدا معنی برگ در فرهنگ فارسی عمید / قربان‌زاده معنی برگ در دیکشنری فارسی به عربی معنی برگ در دیکشنری فارسی به انگلیسی مع
  .. واژه یاب 26 فرهنگ همه دیکشنری مترادف طیفی آزاد + همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه برگ فرهنگ انتشارات معین (بَ) ( اِ.) 1 - توشه ، آذوقه . 2 - اسباب و اثاثیة زندگی . 3 - میل ، آرزو. 4 - اسباب و سامان . برگ در فرهنگ‌های دیگر معنی برگ در لغت‌نامه دهخدا معنی برگ در فرهنگ فارسی عمید / قربان‌زاده معنی برگ در دیکشنری فارسی به عربی معنی برگ در دیکشنری فارسی به انگلیسی معنی برگ در دیکشنری فارسی به ترکی معنی برگ در واژه‌های مصوب فرهنگستان معنی برگ در گویش اصفهانی معنی برگ در گویش کرمانشاه معن
### https://vajehyab.com/moein/%D8%A8%DB%8C%D9%86%DB%8C
Traceback (most recent call last):
  File "<string>", line 7, in <module>
    for m in list(re.finditer(kw,t))[:3]: print('  ..',t[max(0,m.start()-100):m.start()+400])
                  ~~~~~~~~~~~^^^^^^
  File "/usr/lib/python3.14/re/__init__.py", line 285, in finditer
    return _compile(pattern, flags).finditer(string)
           ~~~~~~~~^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/re/__init__.py", line 350, in _compile
    p = _compiler.compile(pattern, flags)
  File "/usr/lib/python3.14/re/_compiler.py", line 762, in compile
    p = _parser.parse(p, flags)
  File "/usr/lib/python3.14/re/_parser.py", line 973, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "/usr/lib/python3.14/re/_parser.py", line 460, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
                ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                       not nested and not items))
                       ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/re/_parser.py", line 858, in _parse
    raise source.error("missing ), unterminated subpattern",
                       source.tell() - start)
re.PatternError: missing ), unterminated subpattern at position 5
### https://vajehyab.com/dehkhoda/%D8%A8%D8%B1%D9%85
Traceback (most recent call last):
  File "<string>", line 7, in <module>
    for m in list(re.finditer(kw,t))[:3]: print('  ..',t[max(0,m.start()-100):m.start()+400])
                  ~~~~~~~~~~~^^^^^^
  File "/usr/lib/python3.14/re/__init__.py", line 285, in finditer
    return _compile(pattern, flags).finditer(string)
           ~~~~~~~~^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/re/__init__.py", line 350, in _compile
    p = _compiler.compile(pattern, flags)
  File "/usr/lib/python3.14/re/_compiler.py", line 762, in compile
    p = _parser.parse(p, flags)
  File "/usr/lib/python3.14/re/_parser.py", line 973, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "/usr/lib/python3.14/re/_parser.py", line 460, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
                ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                       not nested and not items))
                       ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/re/_parser.py", line 858, in _parse
    raise source.error("missing ), unterminated subpattern",
                       source.tell() - start)
re.PatternError: missing ), unterminated subpattern at position 5
  .. برم . [ ب ُ رَ ](اِخ ) روستایی است در سمرقند. (از معجم البلدان ). برم در فرهنگ‌های دیگر معنی برم در فرهنگ انتشارات معین معنی برم در فرهنگ فارسی عمید / قربان‌زاده معنی برم در دیکشنری فارسی به انگلیسی معنی برم در گویش مازنی معنی برم در فرهنگ مترادف و متضاد معنی برم در واژه‌نامه آزاد معانی دیگر برم برم (2) برم (3) برم (4) برم (5) برم (6) برم (7) برم (8) برم (9) برم (10) برم (11) واژه‌های مشابه برم سیاه برم شور بالا برم دلک برم سبز برم شور پائین برم صاد برم کوه برم مرغابی برمهیون برمال خرید اشتراک ا
### https://abadis.ir/fatofa/%D8%A8%D8%B1%D9%85/
Traceback (most recent call last):
  File "<string>", line 7, in <module>
    for m in list(re.finditer(kw,t))[:3]: print('  ..',t[max(0,m.start()-100):m.start()+400])
                  ~~~~~~~~~~~^^^^^^
  File "/usr/lib/python3.14/re/__init__.py", line 285, in finditer
    return _compile(pattern, flags).finditer(string)
           ~~~~~~~~^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/re/__init__.py", line 350, in _compile
    p = _compiler.compile(pattern, flags)
  File "/usr/lib/python3.14/re/_compiler.py", line 762, in compile
    p = _parser.parse(p, flags)
  File "/usr/lib/python3.14/re/_parser.py", line 973, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "/usr/lib/python3.14/re/_parser.py", line 460, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
                ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                       not nested and not items))
                       ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/re/_parser.py", line 858, in _parse
    raise source.error("missing ), unterminated subpattern",
                       source.tell() - start)
re.PatternError: missing ), unterminated subpattern at position 5
  ..  برم - معنی در دیکشنری آبادیس دیکشنری مترجم بپرس برم /borom/ مترادف برم : آبگیر، استخر، برکه، تالاب، غدیر، بند، سد کوچک معنی انگلیسی : bromine , memory , trellis دنبال کنید لغت نامه دهخدا برم. [ ب َ ] ( اِ ) حفظ و از بر کردن و بیاد نگاه داشتن. ( برهان ). حفظ که آنرا از بر گویند. ( آنندراج ) . بَر. - از برم داشتن ؛ از حفظ داشتن. از بر داشتن. ( یادداشت دهخدا ) : از مصحف تندی و درشتی نه همانا یک سوره برآید که تو از برم نداری. فتوحی مروزی. || تالاب و استخر و چشمه آب. ( برها
  .. میدهد . آشکارا و ظاهر و هویدا بطور آشکار و بی پرده و در نظر همه . فرهنگ معین (بَ ) [ په . ] ( اِ. ) آبگیر، استخر، برکة آب . (بَ رَ ) (اِ. ) ۱ - چوبی که پارچه ای ملون بر بالای آن بندند و در میدان نصب کنند برای آگاه کردن مردم از کشتی پهلوانان . ۲ - چوب بندی را گویند که تاک انگور و بیارة کدو و خیار و غیره را بالای آن گذارند، داربست . فرهنگ عمید حفظ، حافظه. ۱. برغ. ۲. چشمه: چون تن خود به برم پاک بشست / از مسامش تمام، لؤلؤ رُست (شهیدبلخی: شاعران بی دیوان: ۲۸ ). ۳. تالاب. ۴. گودالی که در آن آب جمع شده
  .. یک سوره برآید که تو از برم نداری. فتوحی مروزی. || تالاب و استخر و چشمه آب. ( برهان ). گوی باشد بزرگ حوض مانند که آب باران در آن جمع شود و آنرا تالاب خوانند. ( آنندراج ) : چون تن خود به برم پاک بشست از مسامش تمام لؤلؤ رست. شهید بلخی. طریقهاش چو برم آبهای سیل از گل نباتهاش چو دندانهای اره ز خار. فرخی. || مرغ ، که سبزه کنار جوی باشد. ( برهان ). || یک قسم مرغ آبی. ( ناظم الاطباء ). || انتظار. ( برهان ). برم. [ ب َ ] ( ع مص ) استوار کردن. ( از منتهی الارب ). محکم کردن. ( از اقرب الموارد ). || ریسما
```


## [2026-10-16T05:16:17.482Z] TOOL CALL #35: Bash

```json
{
 "command": "for p in \"بینی\" \"گراز\" \"برگ\" \"برم\" \"wēnīg\" \"warāz\" \"warg\" \"Reconstruction:Proto-Iranian/warāȷ́ʰás\" \"Reconstruction:Proto-Iranian/wárkah\" \"Reconstruction:Proto-Iranian/wáyHnaH\" \"Reconstruction:Proto-Indo-European/wer-\" ; do echo \"##### $p\"; curl -sG 'https://en.wiktionary.org/w/index.php' --data-urlencode \"title=$p\" --data-urlencode action=raw | grep -v '^\\s*$' | grep -i -E -A8 'Etymology|Descendants' | head -30; done 2>&1 | head -250",
 "description": "Fetch Wiktionary wikitext for key words"
}
```


### [2026-10-16T05:16:19.444Z] TOOL RESULT

```
##### بینی
===Etymology 1===
{{inh+|trk-oat|trk-pro|*bẹńi|gloss=brain}}; {{cog|kk|ми||brain}}, {{cog|ky|мээ||brain}}, {{cog|tt|ми||brain}}, {{cog|tk|beýni}}, {{cog|ug|مىڭە||brain}}, {{cog|uz|miya||brain}} and {{cog|sah|мэйии||brain}}.
====Noun====
{{head|trk-oat|noun|tr=bäyni}}
# [[brain]]
#* {{quote-book|trk-oat|title=Dresden Manuscript: Kitāb-ı Dedem Ḳorḳud Alā Lisān-ı Tāife-i Oġuzān
|author=anonymous
|2=14th Century
|text=غافل باشك اغریسن '''بيني''' بلور
--
=====Descendants=====
* {{desctree|az|beyin}}
* {{desc|gag|beyni}}
* {{desctree|ota|بینی|tr=beyni}}
====Further reading====
* {{R:trk-oat:Kanar|page=112|beyni}}
* {{R:ota:TS|beyni}}
* {{R:tr:Nişanyan|beyin}}
===Etymology 2===
{{bor+|trk-oat|fa-cls|بینی|tr=bīnī}}
====Noun====
{{head|trk-oat|noun|tr=bīnī}}
# [[nose]]
#: {{syn|trk-oat|بورون<tr:burun>}}
=====Derived terms=====
{{col3|trk-oat|بینی دوتمق<tr:bīnī dutmaq><t:to close one's nose>}}
====Further reading====
--
===Etymology 1===
{{inh+|ota|trk-oat|بینی|tr=bäyni}}, from {{inh|ota|trk-pro|*bẹńi|gloss=brain}}; cognate with {{cog|az|beyin}}, {{cog|kk|ми||brain}}, {{cog|ky|мээ||brain}}, {{cog|tt|ми||brain}}, {{cog|tk|beýni}}, {{cog|ug|مىڭە||brain}}, {{cog|uz|miya||brain}} and {{cog|sah|мэйии||brain}}.
##### گراز
===Etymology===
From {{inh|fa|pal|tr=[[wlʾc]]|ts=warāz|t=boar}}, from {{uder|fa|ira-old|-}}, from {{uder|fa|ira-pro|*warājáh}}, from {{uder|fa|iir-pro|*warāȷ́ʰás||boar}}. Cognate with {{cog|ckb|بەراز}}, {{cog|kmr|beraz}}, {{cog|sdh|وەراز}}, {{cog|mzn|وراز|tr=verâz}}, {{m|mzn|براز|tr=berâz||boar}}, {{cog|ae|𐬬𐬀𐬭𐬁𐬰𐬀||boar}}, and {{cog|sa|वराह||boar}}. Akin to {{cog|xcl|վարազ||wild boar}} and {{cog|syc|ܘܪܙܐ|tr=warzāʾ}}, Iranian borrowings.
===Pronunciation===
{{fa-IPA|guˈrāz}}
===Noun===
{{fa-regional|گراز|گراز|гуроз}}
{{fa-noun|tr=gorâz|pl=گرازها}}
# [[boar]]
## [[wild boar]], [[wild pig]] {{gloss|{{taxfmt|Sus scrofa|species}}, a species of swine}}
##### برگ
##### برم
##### wēnīg
##### warāz
##### warg
##### Reconstruction:Proto-Iranian/warāȷ́ʰás
##### Reconstruction:Proto-Iranian/wárkah
##### Reconstruction:Proto-Iranian/wáyHnaH
##### Reconstruction:Proto-Indo-European/wer-
```


## [2026-10-16T05:16:23.474Z] TOOL CALL #36: Bash

```json
{
 "command": "for p in \"بینی\" \"برگ\" \"برم\"; do echo \"##### $p\"; curl -sG 'https://en.wiktionary.org/w/index.php' --data-urlencode \"title=$p\" --data-urlencode action=raw | sed -n '/==Persian==/,/^==[^=]/p' | head -40; done; curl -s 'https://en.wiktionary.org/w/api.php?action=query&list=search&srsearch=warāz%20boar%20Middle%20Persian&format=json&srnamespace=0|118' | head -c 1500",
 "description": "Get Persian sections of Wiktionary pages"
}
```


### [2026-10-16T05:16:24.490Z] TOOL RESULT

```
##### بینی
==Persian==
{{wp|fa:}}
{{fa-regional|بینی|دماغ|бинӣ|q=in normal speech|nose}}
{{Wiktionary:Picture dictionary/fa:head}}

===Etymology 1===
{{inh+|fa|pal|𐭥𐭩𐭭𐭩𐭪|ts=wēnīg}}, traditionally derived from {{der|fa|ine-pro|*weyd-|t=to see}} and related to {{m|fa|بین|tr={{fa-xlit|بِین}}|pos=form of {{m|fa|دیدن|tr={{fa-xlit|دِیدَن}}}}}}.

However, {{w|Ilya_Gershevitch|Gershevitch}} rejects this etymology, transcribing the Middle Persian term as ''wīnīg'' instead, and deriving it from {{der|fa|ira-pro|*wí|t=apart}} + an Iranian formation descended from {{der|fa|ine-pro|*h₂enh₁-|t=to breathe}}. The prefix is from {{inh|fa|iir-pro|*wí}}, from {{inh|fa|ine-pro|*wí|t=apart}}.<ref>{{cite-web
|last=Korn
|first=Agnes
|title= review of: Desmond Durkin-Meisterernst 2004: Dictionary of Manichaean Middle Persian and Parthian [Corpus Fontum Manichaeorum: Dictionary of Manichaean Texts III: Texts from Central Asia and China 1]. Turnhout: Brepols
|url=https://hal.science/hal-01340887v1/document |archiveurl=https://web.archive.org/web/20231227051414/https://hal.science/hal-01340887v1/document
|archivedate=2023-12-27
|work=Orientalia Suecana 54
|publisher=Turnhout: Brepols
|year=2005
|page=206-212}}
</ref>

Connection with {{cog|kmr|bêvil|t=nose}} is uncertain.

====Pronunciation====
{{fa-IPA|bī`nī}}

====Noun====
{{fa-noun|cls=بِینِی}}

# [[nose]]
#: {{syn|fa|{{fa-l|دِمَاغ//دَمَاغ}}}}

=====Descendants=====
* {{desc|jdt|vini}}
* {{desc|trk-oat|بینی|tr=bīnī|bor=1}}
** {{desc|ota|بینی|tr=bini}}
* {{desc|gu|બીની|bor=1}}

===Etymology 2===
{{nonlemma}}

##### برگ
==Persian==

===Pronunciation===
{{fa-IPA|barg}}
* {{audio|fa|Fa-برگ.ogg|a=Iran}}

===Etymology 1===
{{ety|fa|id=leaf|:inh|pal:<tr:wlg><ety:inh<iir-pro:*walkás>>|tree=1}}
{{inh+|fa|pal|tr=wlg|ts=warg|t=leaf|sc=Phlv}} (whence {{cog|fa-ear|بلگ|tr=balg}}), from {{inh|fa|iir-pro|*walkás|*warkás ~ *walkás}}. Cognate with {{cog|ae-yng|𐬬𐬀𐬭𐬆𐬐𐬀}}, {{cog|sa|वल्क||bark of a tree}}, {{cog|mzn|ولگ|tr=valg}}.

====Alternative forms====
* {{alt|fa|بلگ|tr=balg||archaic|dialectal}}
* {{alt|fa|بلک|tr=balk||Hazaragi}}

====Noun====
{{fa-regional|برگ|برگ|барг}}
{{fa-noun|cls=بَرْگ|pl=برگ‌ها}}

# [[leaf]]
#: {{ux|fa|'''برگ''' زرد و خراب|tr='''barg'''-e zard va xarâb|t=yellow, wilted '''leaf'''}}
#: {{ux|fa|'''برگ''' سبزی است تحفه درویش.|tr='''barg'''-e sabzi ast tohfe-ye darviš.|t=A green '''leaf''' is a poor man's gift.|footer=(Persian proverb about poverty)}}
#* {{quote-book|fa|title=fa:شاهنامه|trans-title={{w|Shahnameh|Book of Kings}}
|year=c. 1011
|author={{w|Ferdowsi|Abu'l-Qāsim Firdawsī}}
|chapter=The tale of Kay Qubād
|url=https://ganjoor.net/ferdousi/shahname/kqobad/sh5
|text=چو دانست کامد به نزدیک مرگ<br>بپژمرد خواهد همی سبز '''برگ'''
|tr=čū dānist k-āmad ba nazdīk marg<br>bipižmurd xwāhad hamē sabz '''barg'''
|t=When it knows that death has come near,<br>The green '''leaf''' will wither away.
}}
# [[petal]]
#: {{coa|fa|'''برگ''' گل رز|tr='''barg'''-e gol-e roz|t=rose '''petal'''}}
# [[sheet]], [[folio]]

=====Derived terms=====
{{col|fa
|برگه<tr:barge>
|خمیربرگ<tr:xamir-barg>
|برگی<tr:bargi>
|برگچه<tr:bargče>
##### برم
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

<p>Please set a prope
```


## [2026-10-16T05:16:31.375Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'barm|warm\\b|varma' ISS_alt_DKS.txt | head -20; grep -n -i -E '^ *var- |^ *vär-' ISS_alt_DKS.txt | head",
 "description": "Grep Bailey Khotan Saka dictionary for var/barm"
}
```


### [2026-10-16T05:16:31.777Z] TOOL RESULT

```
44:References to Khotanese Texts are by Roman numeral 1-V1 with page and line and to Khotanese Buddhist Texts by К and page and line; but by name Bed Bhadra-caryà-desanà; Manj. Manjusri-nairátmya-avatüra-sütra; Sid. Siddhasara; SuvO. КТ r 232-41 Suvarma- bhása; SuvP. KT 1 242-9; Z, The Book of Zambasta, ed. E. Leumann and R. E. Emmerick.
1395:kavürma 'safe place( ?)', 11 18, 8b tt và kavārma tsvümdi ‘they went to the keep’, after a list of names, as elsewhere spasaña tsue "he went on guard duty’, following names. Possibly from base kap- ‘то hold, imprison’, and var- ‘to surround, enclose', hence "Aapa-varma- *kavvürma-, dyadic compound. For kap- see khapa, kava; Armen. Iw kaparan ��bond, detention, prison’ from Iranian *hapadüna-.
1644:khattaviha ‘laughing (?)', ш 106:28-30 tta tta baismás- varmat Süste à kaumadeva hamaiyq strriyanyau bvaijsya byauda khattavihà brriyq khū dye ' so Vi$vakarman created her, or Kümadeva himself, possessed of woman's virtues; in love when he saw her laughing (?)'. From *xandáta- ka- with suffix -ulhaa-, to base khan- ' laugh ', For -viya-, -vilha- also K 19:235 adapuraviya strriye ‘women of the inner chambers’, =K 27:156 attapüraviye strive, = 1. 36102 ayitta-püri strriye; and II 49717 pisaravilid: ' dis- gusting’, K 41098 paravi, =K {1'8: pifaravi. See AION 1, 1959, 116-8.
1828:gahvardama 'pipe-blower, flautist’, пі 38:36 pyatsa тїй pau gahvardama grrüsidá 'they sing in front; then they call upon them, the pipers’, = tt 47:55 pvatsa ñada, pau gahvardama grrausida, =111 35:37 pyatsa ñada pā gahva- dama grrausida, with variant HI 4012-3 pyamtsd йай [pam] pau gahveradránd g(rjüsīdä. Compound gahvara- and dama- 'blower', from ga- < ava- and hvar- ‘to sound’. To IE Pok. 1049-50 suer- : sur- ' to sound’, O.Ind. sudrati 'to sound’ (зйғті, sürmi- 'pipe' (also with $-)); Lit. surmá ‘flute, pipe’, O.Slav. svirati 'to pipe’, Russ. svireli ‘flute, pipe’, svirati ‘play flute', O.Norse svarmr ‘noise’, O.Engl. swearm ‘swarm’, Lat. susurrus ' whisper'. With ava-, note RV 8:68:9 dva svaráti gdrgaro godhá pári sanisvanat ‘let the gargara-instrument sound, let the gauntlets(?) ring'.
2007:gráma- ‘hot’, N. 76:2 luksd grámá ‘rough, hot’, BS 179-14 rukga-ugna; Z 20:2 ysamassamdya grümu hámátu ‘in the world it has become hot’; Sid. туг? си krrimgä hiya gūstä şi tcárba u garkha и grüma ste ‘as to the flesh of fowl, it is fat and heavy and hot’, BS ugmo...suigdho guru-..., Tib. bya-gag-gi ta ni, suum-3in lči-la drod che-ba yin-te; Sid. 16r3 masc. grām, Tib. drod che-ste; п 79:5 grau aysmi јѕа ' with warm mind’; Ш 109:1-2 gra aysmū jsa; I 153, 63vs grrüma иса; see compound grümücd ‘hot water’. With -ka-, Sid. 153r5 grümaka-' tepid’, BS kosna-, Tib. dron-po. Comparative H 112:57 grümyera; abstract, Sid. Sr grauttà' heat! (*gramatàtá), BS anala- ' fire", Tib. mehi drod; Мап). 28 grrüttà. Compound, 1 18:22 grümiücá thot water’. See also garma- in the compound garma- mágtaa-, and gala ' sparks(?)'. From garma-, Ау. garama-, O.Pers. garma-, Sogd. угт, Yayn. yarm, Zor.P., N.Pers. garm, Sangl. убгт, Sarikolt urm, Oss. D. yar, І. gárm. ТЕ Pok. 493 O-Ind. gharmd-, Greek 8&puós, Lat. formus, Armen. jerm, O.Pruss. gorme ‘heat’, Let. garme ‘heat’,
2469:dausvera 'covering (?)', п 11019-20 kaucahara à fau hatca dausvera jsa 'one covering (?) together with dausvera covering'. Uncertain, possibly dausa- from *drafía- to base drap- 'put on, wear’, beside Av. draffa- ‘banner’, draffaka- 'fringe, streamer of dress’ (used of a pusá- 'crown"), Zor.P. drap- ‘to wear’, gloss to Av. vah- ‘to wear’, Опа. dräpi- ' mantel, clothes’; and *vārya- from var- ‘to cover’, Av. varma- 'cloak', Zor.P. wl *varr, Armen. lw vař 'mantle'; hence a dyadic 'garment' or part of a garment’, Neither Chinese nor Tibetan seems to have such а word. For d- from *r8- from dr-, note medial -d- from older -rt- as krta- in kádágana- ‘act’.
3033:Pamir dialects, see s.v. padaji-. IE Рок. 240-1 dheg*h- ‘burn’, O.Ind. dihati, dagdhá-, daha-s, nidágha-s, Greek тёрра 'ashes', Lat. foueo, fauilla 'ash', febris ‘fever’; Celtic Mid.Ir. daig, gen. dega ‘бге’, Got. dags ‘day’, Lit. degit, dégti ' burn, warm’.
3422:naysda- ‘near’, Z 223515 maysdd naysdä ‘very near’, parallel Pali Anāgata-vamsa 38 асс-йзаппа- (= BS aty- üsanna-); Sid. ra6rr bvastyi virastd naysdd hame 'he is near to understanding’, Tib. ses-ñen (ñen 'near'), Ш qz154-5 naysdä laga-pürd kamthe 'near to Lankäpura city’, K 8, svr hàysa. . .navsdä 'far. ..near’; П S148 naysdi grām ауғтӣ уза ' with near warm mind', I 114214 naysda grrau brrivausta jühünai aysmū jsa 'with near warm loving joyful тіпа’; K 109:316 baysüiti navsdaka bvüiia ‘іє must be known to be near bodhi-knowledge', Z 13:62 naysdd atë balysüste ' he has come near to bodhi- knowledge’; Z 23:166 ku balysd naysdakä йїй ' where the Buddha came near’, Z 17:21 naysdá ggarinu ' near to the mountains’, Compound saysda-varga, v 115, 64v3-4 йтаӣса rrundi naysda-varna Нуе rrundi Кута adatya “ће ministers (BS amütya- 'intimate'), the courtiers of the king in the king's country (become) irreligious', BS amütyüh pargadas сайа bhavanty asyüpy adharmiküh. Here naysda-varna- renders BS parsadas ' those who sit around’, hence zaysda- 'near' and var- 'to surround’, *oarana- > varna-. Base mazda-, Av. nazdyü 'nearer', nazdišta- 'nearest' (to āna- 'near", Zor.P. nazdik, nazdiktar, nazdist, N.Pers. паха, nazdik, M.Pers.T. nzd, Balàé&t nasīk, nazi, Pašto nazde, nid, nəzdë (*nazdyah-), Sarikoli шай, Kurd лёзій. IE Pok. 886 sed-, O.Ind. nédiyas-, nédistha- to üsanna-; from *ne-sd-,
4165:parremá ‘ап ornament’, Z 13:137 svarma-süttára kalsta уйе радиа parremá kádai pharu nväsa yidándi 'they made very much noise for him, gold-threaded stuffs, kalsta- ornaments, citü-ornaments, finger-rings, parrema-orna- ments’; K 63, 78v3 hara kaiyūra kaista maula paraima
4267:pasa ‘messenger’, pasa, райа, paisa, п ii7'12 khu pasa ka(j)e (та): ma kamacū ávüm ‘when as messenger in the month Kaja (second spring month) I came here (та=тага) to Kam-cü (Kan-tsou)'; п 872 khu và Hasá bisd pgsa...parau nütem 'when I, the humble servant, as messenger. . . received the command'; v 198, боат amàci pasa pastai ‘the amatya-minister commanded the messenger’; ibid. a4 (amayc(1) pasa; п 95:63—4 khu và 11а pasa hasta khu ttyai Һуд và pā phara na ra hista ‘when he returned, the messenger considered how no longer does a report o£ his come’; u g8«r47 ғасби) bsa hada tsoayda paisq hamdyaja татай 'the envoys іп Sa-cü (Sa-tsou) went as messengers in the month Hamdyaja', = п 95:6т $асп bia hada isvümda paisa hadyaja masta; (first summer month). Parallel context in H 119172 üfgrya gühsà hada ñua Һе teachers (BS ücürya-), householders (BS grhastha-) came as mes- sengers'. From *palsa- (as halsa-, balsa-) (with usual changes -gs-, -ais-) to base pars- ‘to send out’, derivative like Lat. mittere, emissarius, Engl. envoy. Possibly ТЕ Pok. pel- ‘drive’ with increment pel-k- to Lat. pello, pepuli, pultare, Greek пеАбзсо ‘approach’. To Armen. lw jarsem ‘issue, send out’ (of swarm of bees ог sling- stones), T'okhara B parso, parsaut, A. párs ‘missive’, Tib. par-śa, see Indo-Iranica, Mélanges Morgenstierne 11—12; SD'TV 67. Below цп 71:5 pastña, adjective ‘of the pasa- . messengers (?)'.
4557:pisai ‘teacher’, Z ir-42 Киза? pisai parstä ‘where the teacher ordered it'; Іп 124'72 phe айй, BS upadhyaya-, u r15:19 pisai аў beside K 143, rr4 риат üsiri; Z 12:22 itu rro piso viri 'also to the teacher’. Tumšuq Saka pese asri (BS arya- beside acarya-) For йй see KT VI 9, from Prakrit; BS йғуа-. Plural pisa, v 63:29 pisa Ralyana-mittra acc. plur., 111 128-16 pisa kalyaui-maittri byehümine ‘тау we get teachers, good friends’; K. 65, 83v4 pisa byehīme hvastá ' may I get best teachers”: ; inst. plur, K 148:55 різаи kalyana-maittrau jsa. The title jpisai occurs after proper names п 115'19 filavarma prsai ай, V 220, буаз vinai pisa; and before, v 216rr ays isa ѕетаіп pīsai vasádattá ризй (‘I greet’), gen. plur., K. 482:6 mera-pyard pisám vira ‘towards parents, teachers’, abstract, v 84, 2515 pisaittetu vátàá ‘in position of teacher’.
5185:278. bar-— barman-
5195:bàrman- ‘enclosure’ whence r. ‘prison’, 2. ' reservoir', ш 2, 714 and ш 0, 17v4 ttäña bārmaña kastüm ' I came into this prison’; v 126br sayitsárinp barmina (not barmamna, unless by error) ‘from prison of migration’, parallel Samghata-sütra G 37, 78b2 samsara-bhava-bandhanat ‘from bondage of life in migration’; ш 6, 12v4 (and 7, 14V4) samitsürinaina Ьйгтпазпта t from prison of migration’; ‘reservoir’, Z 17:18 ggaryau nuvalysde kho ju barmafii jsa samu ‘pours down from the mountains as from a reser- voir’, From base var- 'to enclose, shut’, Zor.P. varm, N.Pers. barm ‘reservoir’; Oss. D. #ërmá, I. dorm, orm ‘hole, pit’. IE Pok. 1160 пег-. See above s.v. Рајла-; and below vara ‘court’.
5287:bima- ‘rock’, 11 80:24 vasti [bt] bimi haiysgá padá anvastá 'continuously rock is obstructive, the road difficult’; u 81:38 bimvà ttará baysgá ca Па Па strathá: ‘among rocks vegetation is thick, which is so stiff’; rit 80:26—7 bnnia phastadä харӣ ‘тоску moving stones'. From *vaima-, Av. тағта- ‘rock, cleft’; M.Parth. (Hajjiabad insc. 6:12) шут *uëm, М.Регз.Т'. шут ty warg *vemn т vaxarg ' great rock’, Armen. lw оёт, vimac' ‘stone, rock’, Zor.P. оёт; guardian yaksa-goblin vemacitrat ca pahlave 'Vemacitra in the Pahlava-land' ('rock-born'?) see S. Lévi, JA 1915, І, 56. Note also Z 2:105 bimacátri aysuri 'the demon Vemacitra', BS varmacitra asura- rüjanam (А.Е. К. Hoernle, Manuscript Remains of Buddhist Literature found in E. Turkestan, 10519), Pali vepacitta-. Base of *vaima- may be vai- ‘to cut’, Av. vinaoiti, vinuya? glossed by kustan ‘ву, kill’, Armen. lw 081 'incision', see Henning Memorial Volume 25. For bi та with bt at end of line repeated next line, note also ibid. rr 89-19-20 Ji picà. Suffix -ila- as in їп 80:30 utcála kauysá ‘water pot’.
5845:hunter’, —E 2485-6 Нала astada тапа lümdrrai pana, =K 16-131 ttanai üstana brraima lümdrrai pana (translation BSOAS 29, 1966, 508 but pana taken as panatá ' he arose); preterite, v 332, 2416 (bryaundaimá І wept’, BS G 37, 21b2 asrūni ca pramuncümi, Tib. méhi-ma šor-to (héhor Во”); v 1591193, туз braunde вуахій balysü Нете jsa ро ‘ће wept, with forehead he (touched) the feet of the Buddha'. From bram-, Av. bram- in brasat ‘he wept', Yašt 19:34 brüsat yimō 'Yama wept’ (W. B. Henning, BSOAS то, 1938, 509), M. Parth. T. brm'd, noun and adjective brmg; Zor.P. (AVn. 42:2) blnnnd *bramand, Мх 1165 bi'myt *bramët, Pazand varámzó, Aflyütkar i Zarérün 107 brāmēnd, Јатаѕр-патак Бтатёї; Yazdi bremidwun, Naini bremb-: breft, Müzandarani barm- ‘ќо weep’, Sangisari be- bürmiten, bürma ‘weeping’, дебе berme, 2228 berman, with O.Engl. bërmen, barmen. ТЕ, Рок. 132 bher-, bhrem- ‘well up, seethe’ may have been applied to tears; in the sense ‘wander about’, O.Ind. bhrdmati, Khotan Saka Z $26 vibram- ' wander', ui vibramīndä ' wits are wander- ing' (possibly a loan-word).
6182:mür- ' to swarm, teem’, Z 20:41 kye pära jsahera mürindi ‘in whose belly worms swarm’; Ш 76:244 huiyasā agapya йаа bidä ѕатитагӣ khu mürīmdä sam 'as unclean con- temptible human-like beasts swarm just upon the great sea’ (BS maha-samudra-). See mvir- ‘to move', K 109:314. mvara ‘movement’, possibly base mau- mu- thence *mvar-:mūr-, beside mvir- < *mvar-y-.
6344:ysara-güna- ' gold-coloured', SuvP. 6ov2 ysaragünd tcargu kūsä ' beautiful gold-coloured drum’, BS dundubhi rucira, SuvP. 68v2 ysaragüna sam khu sumirá 'gold-coloured like Sumeru’, BS suvarma-varna-giri-bhásita-meru-tulya- ; SuvP. бога ysaragüna sphülye mañamdau 'like gold- coloured crystal’, BS rajata-sphattka- ' silver-crystalled'; SuvP. 69v2 uysdva-chata ysarapüna...amga ‘limbs of polished skin gold-coloured', BS «yavabhasita-anga- suvarga-varua-; К. 34777 ysaraguná, =K 26:126 da-gune, = K 18:193 daá-giná ' fire-coloured' ; JS 38rz ysaregum che jsa '(the godha-lizard) with gold-coloured skin’; with уза, її 103:68-9 ysa-günya chai jsa ' with gold-coloured skin’, See s.v. ysar-; Av. axairi.gaona-, Sogd. Bud. zryunc'h s'yh 'ground for vegetables’; srywnč-mwd (in Uigur lw) glossed by Pers. palang-mušk ‘basil’ (with purple tinge), Zor.P. xargón, N.Pers. zargón, zaryon, zxarjón 'fiery-cred; anemone’, ML.Pers T.  Awargm, M.Parth.T. srgtong, Агаш. srgwn ‘vine’.
6424:sumi; Z 17-4 ysdmünd bora byaridte ttrmhkhe g(gare) ' the winter snow covers the mountain peaks'; Z 22:155 ysämānu sparíüána grüma ' warm to the touch in winter’ {BS sparía-j with -u-, Sid. 3vg ysumām u hamam * winter and summer’, BS sitogna- . . .himosna-, Tib. gran- bahi dus dan, éha-bahi dus-su (‘in cold season and in warm season"), Sid. 3v3 nastya ysumüm hisa rva ' the season at the end of winter’, Adjective, ysumaiia-, Sid. 3r5 ysumaña тоа ‘the winter period’, Sid. 3v5 узитайй u hamām ‘of winter and summer’; п 9:143 ysümauñai bairai ' winter clothes’. Compound, п 76x2 ysumāña-vrrahau ‘for winter dress’ to prahona-, v 2:2:2 ysumāña-vrrahaunajām аштап ' of winter-clothes, types of cloth’. See ysumi.
6641:rükyüm ‘оћсіа title', gen. plur, п 776 Оппа їй u rükyam va $š “ог the biruka-officials one and for the rükya-officials one’. The title birüka- is Turkish buirug. The association of the two titles гпАуа- (from older *raukya-) and Turkish buirug may indicate identical bases. Turkish buyur- ‘ёо command’ can be set beside Khotan Saka rau-:ru- ‘о command’ (see sv. parau, parsta- and rre, rrund-) from the base vrau-z rau-. Note also rautcü variant to rrund- ‘ruler’, In form rükya- is from "*(v)rauka- with adjective suffix -ya-, of agent, rather than gen. plural -уйт. Since the Saka title kara- lranga, kanürang and barmak (Saka from BS pramukha- ‘prior of a monastery") are found in the Persian Islamic sources, this title r2kya- may be traced in the title тш!
7326:S$au 'one!, fem. isa, acc. sing. ifau, inflexion, fSiye, ssye, sye, se, $i, inst. sdna, sina, sena, loc, ssiñi, siie, па, sina, miña (-йп-==-е-), fem. $a, fai, iio, sona; acc. sing. K 34/65 # jasta ‘опе goddess’; п 60:55 fà їй; Sid. 12v4 48... 48... ; HL 21, 523 fau halai mi nasta ' they sat at one side', BS eka-ante nyasidan; Sid. ro1r1 deyam am sau ‘one from two', Tib. gnis-las; 11 127:35 ë dvi sili ' one or two years', Sid. 151v4 sā dva baga ‘опе or two parts’ (BS bhaga- or dialectal, keeping -g-); Sid. r47r4 fo $e; Sid. 7r1 fau salä oi bure, BS varsa-, Tib. lo gétg-gi bar-du; V 333, 2716 fau sau, BS G 37, 2427 eka-ekam. Compounds sa- (see s.v. fa-), fa- (see s.v. fa-), stm-jum, si-jum ‘at one time’, here sau- 'sole, universal’, v 62:8 fau-karünum jsa hvamdä drriinà himare ' thereby (-um jsa) may the men of the whole Rarüna-region become healthy’; K 32:28-9 fau-ksiri satvà upajiva 'livelihood of beings of the whole land’ (BS upajiva-), Sid. т bis rr yudamdá śau-kşīrä krra 'they made treatment of the whole land'; K. 63, 79v3 Sau-giinasthünyau spyau jsa ' with flowers of all colours’; v 252:845 Лауя naysdi fau-güttirà livarakyam brrataram jsa hambrrihüm “І share with sisters (and) brothers of the one family far and near’ (BS gotra-); п 19, 933 sau- hadajsya ‘of опе day'; v 68:16 (#уац-паиАйпа aysinüna ' with concentrated mind’; Z 2:180 pūru ffau-ysütu ' only- born son’; Ir 7:110a #аи-узй pūra māñada 'like an only- born son’ (= 7:114); Manj. 3 fau-raysa 'having one taste’, parallel BS eka-rasa-; V 217, 234 fau masi ‘only one', Manj. so fau mase; Manj. 347 fà ye hama ‘уаз one (and) the same’; Manj. 325 #2 Лата prrara ‘опе (and) the same nature’; Мап). 331 #й hama Manj. 346 sā aysmua hama tone (and) the same mind’; 2 924 ffo баи balysi, =Manj. 403 їй $z baysd; v 62-7 $ü-bisa Toaindá ‘men of one house’; K 46:25 fau hada salya ‘опе day a year; K 68:217 cu fau piysindi (-in-—-e-) 'who recognizes (that it is) one'; H 116:39-40 fau-v-a айа Рапа;[а ‘опе horse of theirs (-am) lost’; K 45‹20-2 fau ümn...u $e др... the one. ..and the other’; ш 6749 Sau. . sera jsëm ' the one. . .the other’; compounds with fü-, Sid. 132r3 ja-salum hvadam hhastá jsa ‘with food (and) drink for one year’, Tib. lo géig chun-éhad lon-pa ni kha-zas dan; JS 37v3 fa-thüra ‘of one subject’ (BS sthàna-); п 89:53 Sa-mastawsye ‘for one month’; v 215702 fü-salvamjsa ' far one year’, above v 6277 fa-bisa hvamdä ‘men of one house’; Manj. 153 fa-nà/ia aysmva ‘mind on one point’; Manj. 322 sā-najsada bvüma ‘knowledge of one kind’; with fauva-, п 104772 sauva- hamara aika-raysa ' having the one taste’, BS eka-rasa-, dyadic; see also first component ďa- above. Before numbers 20-90 sfivare-, Z 13102 fsüvarmautamá ' 91st! ;
```


## [2026-10-16T05:16:40.125Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'var[əe]ka|varǝka|valka-' POK_full.txt | head; grep -n -E 'varāza|varäza|varāha|varaha' POK_full.txt | head; grep -n -E 'vaēnā|vaena' POK_full.txt | head; grep -n -E '^(1160|1161)|wer-.*(bedecken|schützen)' POK_full.txt | head",
 "description": "Grep Pokorny for Avestan words"
}
```


### [2026-10-16T05:16:40.456Z] TOOL RESULT

```
90388:Old Indie valka-m. "bast, splint', i/5//r5/5-"Bastgewand', vrkala-v\. "Bastgewand; a 
18566:dravb); Avestan drvaena- " wooden ', Old Indie druvaya-h' wooden vessel, box made of 
90989:vaenask^ boast ', Old Saxon wanian e\.c.; zero grade Old Icelandic osk {* wunsko) 'wish'.
```


## [2026-10-16T05:16:43.541Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 90370,90395p POK_full.txt; grep -n -i -E 'Page\\(s\\): 116[01]|^Root / lemma: \\*?wer-' POK_full.txt | head; grep -n -i -E 'boar|Eber' POK_full.txt | grep -i -E 'iran|avest|indic' | head",
 "description": "Read Pokorny valka and wer- entries"
}
```


### [2026-10-16T05:16:43.892Z] TOOL RESULT

```
Material: A. Old Indie urnai. (compare Old Indie urna-vabhi- ' spider ', above S. 1114) 
'wool', Avestan varana6s., gr. Anvoc;, Doric Aavoc; n. 'wool', Latin lana ds., lanugo' fluff, 
underfurof Bartes, Milchhaare', Gothic wulla, Old High German wolla etc. 'Wolle = wool', 
Lithuanian i////7a 'Wollfaser', PI. 'wool', Latvian i//Za5 'wool'. Old Prussian wllna'Rock', r.- 
Church Slavic vibna, serb. vuna'\Noo\'; schwachere Ablautform *ulana\n cymr. gwlan, 
corn, gluan, bret. gloan{bn{. loanword is Middle Irish olann) 'wool'; 

other vowel gradation in Latin vellus, -e/75 'fleece' (i///A/s'das zottige, wollige Haarthe 
animal') = Old English m///-/77c»o''coIus' (i.e. 'Wollstange', as wul-mod), probably also 
Armenian gelmn'woo\, fleece'; relationship to Latin vellere {uel-8) from *uel-s-d\\es near; 



*ul6- in gr. Awpa n. "hem, Gespint', Germanic V/c»/7a- (under B) and Indo Germanic *ul6- 
ro-{uel-7)S. 1143. 

B. guttural extensions: 

Old Indie valka-m. "bast, splint', i/5//r5/5-"Bastgewand', vrkala-v\. "Bastgewand; a 
certain intestine, entrails '; isl. /of., Danish /^"Tuchflocke, das Rauhe an Kleidern', Old 
English Old Saxon wloh^ fibre, filament, fringe, Flocke' (Germanic *wldha-)\ Old Icelandic 
lagdr^ tuft of Wolle or Haar' ( *wlagat^a-)\ Old Church Slavic vlakno, russ. volokno " fibre, 
filament '; with Indo Germanic ^.Old Indie valsa-m. "sprout, twig, branch' (these point at 
auf " flexible rod') and Avestan varasa-, npers. gurs= Old Church Slavic vlasi^, russ. volos 
"hair'; to a from beiden root form belongs gr. Aaxvr) f. "krauses hair' ( *ulksna), Kayyoc, m. 
"wool'; 
92096:Page(s): 1160-1162 
68923:teuerst', whereupon Kompar. preyas- 'lieber' for older *prayas-\ Avestan fray- ' satisfy ', 
84550:Material: Avestan /7j(Gen. Sg. for *huvd) "swine'; gr. ho,, doc,, Akk. uv m. "boar', f. "sow' 
85762:tasat^puW, with Gewalt set in motion ', /asa/a-zr? 'Weberschiffchen', v/tast/'-m.; Avestan
```


## [2026-10-16T05:16:47.597Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 92085,92125p POK_full.txt; grep -n -E '^ *wer-' AHD_watkins1985.txt | head; grep -n -i -E 'wer-.*cover' AHD_watkins1985.txt | head",
 "description": "Read Pokorny wer- cover and AHD"
}
```


### [2026-10-16T05:16:47.990Z] TOOL RESULT

```
Old English weord, wordn. m. " courtyard, household ' {*uer-to-, *ur-to-). Old Saxon 
wurtht "gestampfter odergepflasterter Platz' (= Old Indie vrti-). Middle Low German wurt, 
wort, wurde, wordei. "erhohter place, Hofstatte; garden, FeldstiJck', Old Icelandic urdi. 
"heap from Felsblocken'; 

compare alb. vathe^ paddock, Hof um das Haus, hurdle, sheepfold ' {*uor-ta), tochar. B 
warto, warfffjo' garden, wood, forest', Irish fert'bur\a\ mound'; in the meaning also Old 
Church Slavic i/c»/'5"saepimentum'. 

References: WP. I 280 ff.. Frisk 568 f., 593 f., 643 f.; 
See also: in addition uergh-1. 
Page(s): 1160-1162 

Root / lemma: uer-6{^huer-6) 

Meaning: to talk, speak 

Note: also uere-, ure- 

Material: Avestan urvata-n. " determination, command ' (= phtov), next to which from the 

light basis *uere-: Avestan urvata- n. " determination ' = Old Indie vrata-n. " command, 

statute, profession, declaration ', and Old Church Slavic rota^oaVn'; ablaut. Old Prussian 

wertemmaT we schworen'; 

gr. £ipu) "say' (*F£pju)), Fut ep. Ionian spsu), Attic spw. Pass. Aor. Ionian dpsOnv 
(*£Fp£0r|v), Attic sppnOnv (*£Fpn0r|v), Perf. £ipr|-Ka, -|jai diss, from *F£Fpr|-, compare 
geneuertes = renamed, has changed?? arg. F£Fpr|M£va; phtoc; "verabredet = festgesetzt', 
PHToop, Aeolic Fpniajp "Redner', pnrpa, el. Fparpa f. " saying, pact, covenant', diss, to 



Cypriot Fpnra, whereof £uFpr|TaaaTU "pact, covenant, law ', pnija "word", pf\a\(; " discourse 
', £ipu)v ' someone, the sich verstellt' (*F£pju)v), eipwvEia "Verstellung"; 

russ. vru{*vbrg), vratb'We, maunder, drivel ', with /r-suffix {*uorka): russ. ura/ra "empty 
gossip'. Old Church Slavic vracb ( *uorkios) 'physician, medicine man (*sayer of a magic 
spell), magician, sorcerer'; 

1143:wer-3
1145:wer-4
1147:wer-4. To perceive, watch out for. I. O-grade form *wor-. 1. Suffixed form *wor-o- in Germanic *waraz in: a. Old English wer, watchful: wary; b. Old English gewer, aware (ge-, collective and intensive prefix; see kom): AWARE; C. Old English warian, to beware: WARE?. 2. Suffixed form *wor-to- in Germanic *wardaz, guard, and *wardén, to guard, in: a. (i) Old English weard, a watching, keeper: WARD; STEWARD (ii) Old English wear- dian, to ward, guard: WARDER?; b. Old North French warder, to guard: WARDEN; REWARD, WARDROBE; C. Old French guarder, to guard: GUARD; d. Anglo-Norman warde, guard: REARWARD?. 3. Germanic *ward in: a. Old English waru, goods, protection, guard: WARE}; b. Old English -ware (probably plural of waru, “goods”’), inhabi- tants (< “defenders’’): FIELDFARE. 4. Suffixed form *wor-wo- in Greek ouros, a guard: ARCTURUS. 5. Variant *(s)wor-, s(w)or- probably in Greek horan, to see: EPHOR, PANORAMA. II. Suffixed (stative) form *wer-é- in Latin veréri, to respect, feel awe for: REVERE!. [Pok. 8. wer- 1164.]
1148:wer-5. To cover. I. Basic form *wer-. 1. Germanic *wer- jon- in Old English wer, dam, fish trap: WEIR. 2. Com- pound form *ap-wer-yo- (*ap-, off, away; see apo-) in Latin aperire, to open, uncover: APERIENT, APERITIF, APERTURE; OVERT, OVERTURE, PERT. 3. Compound form
446:epi. Also opi. Near, at, against. 1. Latin ob, ob-, before, to, against: OB-. 2. Greek epi, on, over, at: EPI-. 3. Greek opisthen, behind, at the back: OPISTHOBRANCH, OPIS- THOGNATHOUS. 4, Zero-grade “pi-, on, in Greek piezein, to press tight (see sed-1). 5. Old Church Slavonic ob, on, in Russian oblast’, oblast: OBLAST. 6. Prefix *op- in *op-wer-yo-, to cover over (see wer-5). [Pok. epi 323.]
1148:wer-5. To cover. I. Basic form *wer-. 1. Germanic *wer- jon- in Old English wer, dam, fish trap: WEIR. 2. Com- pound form *ap-wer-yo- (*ap-, off, away; see apo-) in Latin aperire, to open, uncover: APERIENT, APERITIF, APERTURE; OVERT, OVERTURE, PERT. 3. Compound form
1151:*op-wer-yo- (*op-, over; see epi) in Latin operire, to cover: COVER, OPERCULUM. II. O-grade form *wor-. 1. Germanic *war-nén in Old English war(e)nian, to take heed: WARN. 2. Germanic *war- in: a. (i) Old French garant, warrant, authorization: GUARANTY (ii) Old North French warant, warrant, and warantir, to guarantee: WARRANT, (WARRANTEE), WARRANTY; b. Old French garer, to guard, protect: GARAGE; c. Old French g(u)arir, to defend, protect: GARRET, GARRISON; d. Old North French warenne, enclosure, game preserve: WARREN; e. Old French g(ujarnir, to equip: GARMENT, GARNISH. [Pok. 5. uer- 1160.] wer-S, Also wera-. To speak. Variant *wré-, contracted from *wreo-. 1. Suffixed zero-grade form *wr-dho- in Germanic *wurdam in Old English word, word: worD. 2. Suffixed form *wer-dho- in Latin verbum, word: VERB, VERVE; ADVERB, PROVERB. 3. Suffixed form *wer-yo- in Greek eirein, to say, speak: IRONY. 4. Variant form *wré- in suffixed form *wré-tor- in Greek rhétér, public speaker: RHETOR. [Pok. 6. wer- 1162.] wer-7. To burn. Suffixed lengthened o-grade (causative) form *w6r-yo- in Russian varit’, to boil: saMovarR. [Pok. 12. wer- 1166.] wer-®, Squirrel. Reduplicated expressive form *wi-wer(r)- in Latin viverra, a ferret: VIVERRINE. [Pok. 13. uer- 1166.] wér-. Water. Suffixed zero-grade form *dr-ind- in Latin irina, urine: URINE. [In Pok. 9. au(e)- 78.] were-', Wide, broad. Suffixed form *wer(a)-u- metathe- sized in Greek eurus, wide: EURY-; ANEURYSM, EURYD- IcE. [Pok. 8. wer- 1165.] were-2, To find. Variant *wré-, contracted from *wrea-. Reduplicated form *we-wré- in Greek heuriskein (first person singular perfect indicative active heuréka), to find: EUREKA, HEURISTIC. [Pok. 4. ver- 1160.] werg-. To do. I. Suffixed form *werg-o-. 1. Germanic *werkam, work, in: a. Old English weorc, werc, work: work; b. Old High German werc, work: (BOULEVARD),
```


## [2026-10-16T05:16:51.745Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'Root / lemma: uer-5' POK_full.txt; L=$(grep -n -E 'Root / lemma: uer-5' POK_full.txt | head -1 | cut -d: -f1); sed -n \"$L,$((L+25))p\" POK_full.txt | grep -n -i -E 'avest|npers|persian|var' ",
 "description": "Read Pokorny wer-5 Avestan material"
}
```


### [2026-10-16T05:16:52.259Z] TOOL RESULT

```
91991:Root / lemma: uer-5 {* huer-5) 
15:derivatives: *uortom\n Nom. PI. Lithuanian vartai, Latvian i/a/Y/'gate, door'. Old Prussian 
21:Slavic ot-voriti, compare also Old Indie Kaus. varayati) as 'das gate open, um das Vieh
```


## [2026-10-16T05:16:54.065Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 91991,92010p POK_full.txt",
 "description": "Read start of Pokorny wer-5"
}
```


### [2026-10-16T05:16:54.349Z] TOOL RESULT

```
Root / lemma: uer-5 {* huer-5) 

Meaning: to close, cover; to guard, save 

Material: A. With Prafixen: 'shut' and 'open'; 'door'; uortom' gate'. 

Old Indie ap/-vrndt/\ersc\r\\\eQ>t, bedeckt', apa-vrnot/^ off net'; also Latin operio 
'bedecke', aper/'o ^ off ne' (from *op{/)- and *ap(o)-uerid)\ Oscan i/e/i/'portam', Umbrian 
verof-e^\n portam', Oscan vereiasQen. Sg. 'Jungmannerbund' (originally 'Torwache', 
VetterGI. 29, 240); 

Lithuanian uzveriu, -i/e/^^/'shut', afverf/'open' (from which previously without proverb 
ver/u, vert/'open', and 'shut'; Old Church Slavic (za)/vbrQ, K/ieZ/'shut', Iter, ot-voriti^ open'; 

derivatives: *uortom\n Nom. PI. Lithuanian vartai, Latvian i/a/Y/'gate, door'. Old Prussian 
warto ^Uaustuxe'; Old Church Slavic vrata, russ. vorota^gate, luxe'; also to 3. uer- could 
belong Old Church Slavic vereja and z5-i/c>/7>'Hebebaum', russ. i/e/'eya'Torflugel', zavor 
'gesperrter passage '; 

perhaps here Lithuanian i/a/y// "drive, push' (formal = Germanic warjan. Old Church
```


## [2026-10-16T05:16:58.437Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; ls; python3 - <<'E'\nimport re\nt=open('ARY_pages.txt').read().split('\\f')\nfor kw in ['برگ','گراز','بینی','برم']:\n  for i,p in enumerate(t):\n    for m in re.finditer(r'(^|\\n)\\s*'+kw+r'\\s*[\\n:(]',p):\n      print(kw,'pdf',i+1,repr(p[m.start():m.start()+300])); break\nE",
 "description": "Search Aryanpur OCR for headwords"
}
```


### [2026-10-16T05:18:59.582Z] TOOL RESULT

```
Command did not complete within its 120s timeout and was moved to the background (ID: bpcs3zdkr). Output is being written to: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tasks/bpcs3zdkr.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/sfmqrb/git/rishe-private; directory changes made by the backgrounded command do not apply to subsequent commands.
```


## [2026-10-16T05:19:02.256Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; ls -la | head; ls ../../ocr/ARY | head",
 "description": "List Aryanpur files"
}
```


### [2026-10-16T05:19:02.573Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--  329k sfmqrb 14 Oct 22:19  0051.png
.rw-r--r--  1.6k sfmqrb 14 Oct 22:19  0051.txt
.rw-r--r--  1.0k sfmqrb 14 Oct 22:19  0051.vision.txt
.rw-r--r--  361k sfmqrb 14 Oct 22:19  0136.png
.rw-r--r--  2.0k sfmqrb 14 Oct 22:19  0136.txt
.rw-r--r--  2.1k sfmqrb 14 Oct 22:19  0136.vision.txt
.rw-r--r--  387k sfmqrb 14 Oct 22:19  0153.png
.rw-r--r--  1.7k sfmqrb 14 Oct 22:19  0153.txt
.rw-r--r--  2.0k sfmqrb 14 Oct 22:19  0153.vision.txt
```


## [2026-10-16T05:19:04.591Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; ls -la; wc -c *.txt *.json 2>/dev/null",
 "description": "List Aryanpur incoming dir"
}
```


### [2026-10-16T05:19:04.893Z] TOOL RESULT

```
Exit code 1
(eval):1: no matches found: *.json
```


## [2026-10-16T05:19:06.510Z] TOOL CALL #46: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ | head -30",
 "description": "List Aryanpur dir"
}
```


### [2026-10-16T05:19:07.066Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--  8.1M sfmqrb 14 Oct 22:19  ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
.rw-r--r--  586k sfmqrb 14 Oct 22:19  ARY_latin_index_pages.txt
.rw-r--r--  960k sfmqrb 14 Oct 22:19  ARY_pages.txt
```


## [2026-10-16T05:19:10.705Z] TOOL CALL #47: Bash

```json
{
 "command": "sleep 1; cat /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tasks/bpcs3zdkr.output; cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n -c $'\\f' ARY_pages.txt; grep -n -E '^\\s*(برگ|گراز|بینی|برم)\\b' ARY_pages.txt | head",
 "description": "Check background output and grep ARY"
}
```


### [2026-10-16T05:19:12.025Z] TOOL RESULT

```
544
4197:بینی / ۱۴۵
12611:گراز )۲۷۵
```


## [2026-10-16T05:19:14.824Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 4190,4215p ARY_pages.txt; echo ----; sed -n 12605,12630p ARY_pages.txt; grep -n -E 'برگ' ARY_pages.txt | head -5; grep -n -i -E 'warg|varəka|varaka|wēnīg|wenig|warāz|varāza' ARY_pages.txt ARY_latin_index_pages.txt | head",
 "description": "Read Aryanpur bini and guraz entries"
}
```


### [2026-10-16T05:19:15.244Z] TOOL RESULT

```
انگلیسی کهن (37ا8۸۷0 012): 85077۸0 1153 8
اسلاوی کهن (۷72ما5 بل#تابن صال): برهان قاطع + ۱ ۳۴۰
0 8۸7۸7 807۸1 ,85055 :
یادداشت:
بازگشت به: باک
[pdf page 144]
نج
بینی / ۱۴۵
یکره دض
اوستایی (/4887۸4۸): ۷۸۲۰ ,۷۸5۸ نروژی (/۸/07775014): 5(
پارسی باستان (۲8۴۶۶4۸۷ ۰)010 ۰ ۲۸7۸۵۲ هلدی (017۳[4): ناد لا
پهلری (۲7مابتهط): ال ند ریا اسلاوی کهن (0/ها5 077867 ضا0):
کردی (ل70137): الا -88 ,نآ208
سغدی (50077014(7): 8 ,۸8 لهستانی (داماه۳): 05
سانسکریت (۸۸/۹/7: ۰ ۸۵۹۰ ب۸۸8 روسی (75514ا): 05
یونانی (07280)(شاید) انا چک 7ل22): 05
لاتین (4710ا): 88 ,کنآهم۸< صربی (887/14۸4): 085
فرانسه (73ح/۳2۸): 12 برهمی (/80/782411): 05
اسپانیایی (52۸(۷184): 2 اسلواکی 51.07420): 05
ایتالیایی (/۸الم7): ۹0 لینوانی (/7270۸0/1۸/): 015
رومانی (۸1۸/4۷تا): ند ند پروسی کهن (۲/35۸ دا0): 02
[ پرتغالی (۳077010535): 7
۱ ابسلند یکهن (9۷ 52/0107 صا۵): پسگشت‌ها دهد ات۲
085 زن رس
نورس کهن (۸0782 010): ۸ 0 (0۹5) دما ان
فریزی کهن (/۲/514 01 ۸051 ,270855 4 (۲82) :5 م02
----
دانمارکی (7ل18م0): 0 34 تا ان
سوئدی (87۷50[57): 0 5 (لباتا) ک آدند 0۱
نروژی (07(501۸7/): رد برهان قاطع : ۱۷/۸۶۸۶
هلندی (7ل0070), 0
9
[pdf page 424]
گراز )۲۷۵
اوستایی (لل4۲7:87): ۷۸ رومانی (8117142): ۷
پهلری (ماتم۸: ۰ ۷۸۸۵2 ,۷۸۵2 لنرنی (لنی) (/7742ت): دید دبا
کردی (۸/7۵]51): 32 پروسی کهن (/(354تا۶۸ ۰:۵۵ ۷18885
سانسکریت (54۸/97077): ۷۸۸
ارمتی (4/8۸/18۸): ۷۸۸ پسگشت‌ها 5
لائین (7/0ل): ۷5 104 0۸0 102228
فراسه (7ل۳۳7): ۷۸ 1014 [ سا
اسپانیایی (50۸18): ۷0 2 (80۸3) ۸247/00
ایتالیایی (4ل74)): ۷ برهان قاطع : ۱۷۷۹
یادداشت:
رابطه‌ی واژه‌های ایرانی و سانمکریت و ارمنی اين فهرست با واجریشه‌ی هند و اروپایی و دیگر واژه‌های این
فهرست احتمالی است و بهمین دلیل در جلر واجریشه‌ی هند و اروپایی (شاید) آورده‌ام.
اوستایی (4۲23744): پرتغای (۳0770178538): هه
+6۸۸۲ +0۸30 +6۸8 انگلیسی (8(70/877)(از فرانسه) 01۸68
پهلری ۰:۷ اسلاوی کهن (51476 0۶0074 صات):
قسی بانقه6۸ ا4نقق0۸ ,کآننقه0 دناد
مش . 0 قلاانقهه لیترانی (/40/(متا 7 7ل):
سانسکریت (۸/58/7شگا: ۲ کفعتاه ,6133۱ ,ات617
ما0 ,080۸ ,کفقاه ,ق0158 نرنی (لنی) (/71۸ا): اند ای ما
1095:افتخار ابدی خواهم داشت. از سوی دیگر» اگر به مهن خود برگردم عمر طولانی خواهم داشت ولی
1191:اخص توسط دانشمندان برونمرزی (بارتولومه» یونگر» هنینگه» نیبرگ) در چند دهه قبل آغاز شد.
1213:زبان‌های هند و اروپایی نمود. بخشی از پژوهش‌های او تحت عنوان «برگزیده‌ای از زبان‌های آریایی»
1860:این واژه برگرفته شده‌اند. :
3451:"درخشیدن" است. حتی معنی برگرفته‌های پهلوی این واژه(81۵210۸۷ 8۸62 دارای چم" درخشیدن"
ARY_latin_index_pages.txt:3508:BLAD DANISH) Sails WARG, VALG PAHLAVD) 5 shay
ARY_latin_index_pages.txt:4106:s(OLD CHURCH SLAVIC) oS 53%! WENIG (PAHLAVI) 5 Jha
```


## [2026-10-16T05:19:21.522Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 - <<'E'\nt=open('data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt').read()\nimport re\nfor kw in ['WARG, VALG','WENIG (PAHLAVI)','WARAZ','VARM']:\n  i=t.find(kw)\n  if i<0: print(kw,'none'); continue\n  pre=t[:i]; m=list(re.finditer(r'\\[pdf page (\\d+)\\]',pre)); print(kw, m[-1].group(1) if m else None)\nE\nfor p in 145 275; do python3 tools/ref_page.py ARY:$p --image 2>&1 | head -3; done",
 "description": "Locate ARY pages and render images",
 "timeout": 200000
}
```


### [2026-10-16T05:19:35.140Z] TOOL RESULT

```
WARG, VALG 123
WENIG (PAHLAVI) 144
WARAZ 424
VARM 125
(no exact page map; using offset -1 -> pdf page 144; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/ARY/0145.png
REF: ARY:145  PDF: data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf page 144  OCR-lang: fas+eng
(no exact page map; using offset -1 -> pdf page 274; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/ARY/0275.png
REF: ARY:275  PDF: data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf page 274  OCR-lang: fas+eng
```


## [2026-10-16T05:19:38.502Z] TOOL CALL #50: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/ARY/0275.png"
}
```


### [2026-10-16T05:19:38.935Z] TOOL RESULT

```

```


## [2026-10-16T05:19:38.932Z] INPUT

[Image: original 1500x2400, displayed at 1250x2000. Multiply coordinates by 1.20 to map to original image.]


## [2026-10-16T05:19:41.997Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; rm -f data/verification/sources/refs/ocr/ARY/0275.png data/verification/sources/refs/ocr/ARY/0275.txt; python3 tools/ref_page.py ARY:425 --pdf-page 424 --image 2>&1 | head -3",
 "description": "Render Aryanpur pdf page 424",
 "timeout": 200000
}
```


### [2026-10-16T05:19:48.808Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/ARY/0425.png
REF: ARY:425  PDF: data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf page 424  OCR-lang: fas+eng
```


## [2026-10-16T05:19:50.283Z] TOOL CALL #52: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/ARY/0425.png"
}
```


### [2026-10-16T05:19:50.803Z] TOOL RESULT

```

```


## [2026-10-16T05:19:50.798Z] INPUT

[Image: original 1500x2400, displayed at 1250x2000. Multiply coordinates by 1.20 to map to original image.]


## [2026-10-16T05:19:56.482Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/ARY; cat > 0425.vision.txt <<'E'\n[ARY printed p.425 = pdf page 424; read from image by claude (page-522 verification)]\nفارسی (PERSIAN): گراز GORĀZ — چم انگلیسی: BOAR — هند و اروپایی (INDO-EUROPEAN) (شاید): *WER-, *WEROS\nاوستایی VARĀZA; پهلوی VARĀZ, WARĀZ; کردی BERĀZ; سانسکریت VARĀHA; ارمنی VARAZ; لاتین VERRĒS; فرانسه VERRAT; اسپانیایی VERRACO; ایتالیایی VERRO; رومانی VIER; لتونی VERVEX; پروسی کهن VIRSES\nREFERENCES: MACKENZIE (BOAR) 104; BUCK 160-164; AMINDAROV (BOAR) 192; برهان قاطع ۱۷۷۹\nیادداشت: رابطه‌ی واژه‌های ایرانی و سانسکریت و ارمنی این فهرست با واجریشه‌ی هند و اروپایی و دیگر واژه‌های این فهرست احتمالی است و بهمین دلیل در جلو واجریشه‌ی هند و اروپایی (شاید) آورده‌ام.\nE\nls",
 "description": "Save Aryanpur vision text"
}
```


### [2026-10-16T05:21:57.090Z] TOOL RESULT

```
Command did not complete within its 120s timeout and was moved to the background (ID: bj5plyu18). Output is being written to: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tasks/bj5plyu18.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/sfmqrb/git/rishe-private; directory changes made by the backgrounded command do not apply to subsequent commands.
```


## [2026-10-16T05:21:59.728Z] TOOL CALL #54: Bash

```json
{
 "command": "head -2 /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/ARY/0425.vision.txt; ls /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/ARY/ | grep -E '014|042'",
 "description": "Verify vision file saved"
}
```


### [2026-10-16T05:22:00.037Z] TOOL RESULT

```
[ARY printed p.425 = pdf page 424; read from image by claude (page-522 verification)]
فارسی (PERSIAN): گراز GORĀZ — چم انگلیسی: BOAR — هند و اروپایی (INDO-EUROPEAN) (شاید): *WER-, *WEROS
.rw-r--r--  348k sfmqrb 16 Oct 01:19  0145.png
.rw-r--r--  1.8k sfmqrb 16 Oct 01:19  0145.txt
.rw-r--r--  375k sfmqrb 16 Oct 01:19  0425.png
.rw-r--r--  1.9k sfmqrb 16 Oct 01:19  0425.txt
.rw-r--r--   939 sfmqrb 16 Oct 01:19  0425.vision.txt
```


## [2026-10-16T05:22:01.439Z] TOOL CALL #55: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/ARY/0145.png"
}
```


### [2026-10-16T05:22:01.807Z] TOOL RESULT

```

```


## [2026-10-16T05:22:01.803Z] INPUT

[Image: original 1500x2400, displayed at 1250x2000. Multiply coordinates by 1.20 to map to original image.]


## [2026-10-16T05:22:09.061Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat > data/verification/sources/refs/ocr/ARY/0145.vision.txt <<'E'\n[ARY printed p.145 = pdf page 144; read from image by claude (page-522 verification)]\nفارسی (PERSIAN): بینی BĒNĒ — NOSE — هند و اروپایی: *NAS-, *NĀS-, *NES-\nاوستایی VAĒNĀ, NĀH-; پارسی باستان NĀHAM; پهلوی WĒNĪG; کردی BIHNI; سغدی NS, NŌS; سانسکریت NĀSĀ, NĀS-; یونانی (شاید) BHĪNÓS; لاتین NASŪS, NĀRIS; ... انگلیسی NOSE ...\nREFERENCES: POKORNY 755; BARNHART (NOSE) 710; DELAMARRE (NEZ) 104; MACKENZIE (NOSE) 125; BUCK 227; ONIONS (NOSE) 615; SKEAT (NOSE) 403; AMINDAROV (NOSE) 260; برهان قاطع ۳۴۱ و ۲۱۳۵-۲۱۳۶; لغت‌نامه دهخدا ۵۲۹۳\nE\ntimeout 100 python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/بینی' --note 'page 522, root Vaenâ 1: Persian bīnī < MP wēnīg; *weyd- vs Gershevitch wi-+*h2enh1-' 2>&1 | tail -2",
 "description": "Save ARY vision; archive first web source",
 "timeout": 120000
}
```


### [2026-10-16T05:22:10.254Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4b67b7b9a402e742.txt
```


## [2026-10-16T05:22:15.812Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f(){ timeout 100 python3 tools/fetch_source.py \"$1\" --note \"$2\" 2>&1 | tail -1; }\nf 'https://en.wiktionary.org/wiki/گراز' 'page 522, root Varâza: NP gorâz < MP warāz < PIr *warājáh < PIIr *warāȷ́ʰás; cognates Av. varāza-, Skt varāha-' \nf 'https://en.wiktionary.org/wiki/برگ' 'page 522, root Varekahe: NP barg < MP warg < PIIr *warkás~*walkás; Av. varəka-, Skt valka-'\nf 'https://abadis.ir/fatofa/برم/' 'page 522, root Var: Moin barm [په.] آبگیر استخر برکه; Dehkhoda/Borhan تالاب و استخر'\nf 'https://vajehyab.com/moein/گراز' 'page 522, root Varâza: Moin gorâz [په.] خوک نر'\nf 'https://vajehyab.com/moein/وراز' 'page 522, root Varâza: Moin vorâz گراز، خوک نر'\nf 'https://en.wiktionary.org/wiki/برم' 'page 522, root Var: Persian barm'",
 "description": "Archive remaining web sources",
 "timeout": 600000
}
```


### [2026-10-16T05:22:18.696Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/77106ffd3904ddec.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9095549fdeb95716.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b24784ea838a62cc.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3ada9353d190fa99.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fa88801c57bacdf6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3d231667f4e25842.txt
```


## [2026-10-16T05:22:21.326Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -i -E 'pool|reservoir|Etymology|Middle Persian' 3d231667f4e25842.txt | head; wc -c 3d231667f4e25842.txt; grep -o -E 'Persian.{0,300}' 4b67b7b9a402e742.txt | head -3 | cut -c1-200",
 "description": "Check archived Wiktionary barm content"
}
```


### [2026-10-16T05:22:21.737Z] TOOL RESULT

```
 Etymology 
 Etymology 1 
 Etymology 2 
 Etymology
 (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 
 Etymology 1
 From Middle Persian wlm ( warm ) , from Proto-Iranian [Term?] , ultimately from Proto-Indo-European *wer- ( “ to heed, be wary, watch, guard ” ) . Cognates include Ancient Greek ὁράω ( horáō , “ to see, watch ” ) , Latin vereor ( “ to revere , fear ” ) , and Old English warnian ( “ to warn , be wary ” ) . ( Can this ( + ) etymology be sourced ?) Alternatively from Proto-Iranian *wār- ( “ to choose; to convince, believe ” ) , from Proto-Indo-European *welh₁- .
 Etymology 2
 Persian terms inherited from Middle Persian 
 Persian terms derived from Middle Persian 
15944 3d231667f4e25842.txt
Persian 
Persian subsection 
Persian بینی ( bīnī )
```


## [2026-10-16T05:22:23.897Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -A6 -E '^ Etymology 2$' 3d231667f4e25842.txt | head -20; grep -n -i -E 'memory|pond|pool' 3d231667f4e25842.txt | head",
 "description": "Read Wiktionary barm etymology 2"
}
```


### [2026-10-16T05:22:24.228Z] TOOL RESULT

```
 Etymology 2
 [ edit ] 

 Chemical element ( edit ) 

 Br 
 Atomic number 35 
1356: memory
```


## [2026-10-16T05:22:30.604Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E '\\bwarg\\b|\\bvarg\\b|valg' SNS.txt SNS_pages.txt | head -5; grep -n -i -E 'var[əe]ka|varǝk|vareka' EAV_studies.txt | head -5; python3 - <<'E'\nt=open('SYN.txt').read().split('\\f')\np=t[525+24]\nimport re\ni=p.find('LEAF'); print(p[:100]); \nfor m in re.finditer(r'Av\\.|Pers|NPers|varak|barg',p): print(p[max(0,m.start()-150):m.start()+200].replace('\\n',' ')); print('--')\nE",
 "description": "Check SNS, EAV, Buck refs for leaf"
}
```


### [2026-10-16T05:22:30.989Z] TOOL RESULT

```
SNS.txt:31130:varg 281/12 
SNS_pages.txt:15792:                                                              vijratC?) 289/1           varg 281/12
 sapd ‘hoe’, MLat. sappa (8.25).
3. Ir. claidim (NIr. claidhim ‘ex- cavate’, W. claddu ‘bury’, old ‘
e ; yy i ME spade Pol. _—rydel Tipe ee lai NE spade Russ, zastup, lopata oe rame, laige Du. spade Skt. khanitra- Tr, ramhan, laighe OHG - sciwvala(?) Av. kastra- Me pal, rhaw MHG grabeschit ; r. pal NHG  spaten (grabscheit) CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar Digitized by Arya Samaj Foundation Chennai and eGangotri SELECTED 
--
, etc., general Slavic : Lith. raultt ‘tear out’, ON rgja ‘tear out wool’, Skt. ru- ‘break to pieces’, etc., IE *reu-. Walde-P. 1.352. 7. Skt. khan-, Av., OPers. kan-, with- out certain Hur. connections. Walde-P. 1.399. AGRI t names of dig- y the Greek, it certainly be- and some form of ‘hoe’. ‘spade’ and ‘shovel ) s not a are a their similar shape
--
, general Slavic : Lith. raultt ‘tear out’, ON rgja ‘tear out wool’, Skt. ru- ‘break to pieces’, etc., IE *reu-. Walde-P. 1.352. 7. Skt. khan-, Av., OPers. kan-, with- out certain Hur. connections. Walde-P. 1.399. AGRI t names of dig- y the Greek, it certainly be- and some form of ‘hoe’. ‘spade’ and ‘shovel ) s not a are a their similar shape sleme
--
```


## [2026-10-16T05:22:34.528Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '8\\.57 LEAF|LEAF$|^ ?LEAF' SYN.txt | head; grep -n -i -E 'varak|NPers\\. barg|Pahl\\. varg' SYN.txt | head; grep -n -i -E 'NPers\\. (gurāz|guräz)|varāza|BOAR' SYN.txt | head -5; grep -n -i -E 'NPers\\. b[iī]n[iī]|vaenā|vaēnā' SYN.txt | head -5",
 "description": "Grep Buck for leaf, boar, nose"
}
```


### [2026-10-16T05:22:34.865Z] TOOL RESULT

```
13242:8.56 LEAF
13246:. frunzd (foate) NE leaf Russ. list duille Du. . blad (loof) Skt. parna-, patira- duilleog, bileog OHG  blat, loub Av. varaka- deilen, dalen MHG Dlat, loup
13271:Av. varaka-, cf. MPers. varg, NPers, barg. etym.? Barth. 1367,
14471:Lith. vilkti (now ‘drag’, but once ‘draw’ whence refl. or vilkéti ‘put on clothes, wear’), Lett. vilkt, ChSI, vest; vlékq (in Gospels pri-vléti), SCr. vués (‘draw’ or ‘drag’; but Boh. vleci, Pol, wleé, Russ. voloé’, volocit! ‘drag’) : Grk. avAatE (*ardak-) ‘furrow’, Ay, varak- ‘draw’ in cpds. (Barth. 1366), all fr, *welk-. (cf. *selk- in Grk. a&kw, ete, above, 1). Walde-P. 1.306.
174:Ace as ae been carried on with the kindly co-operation of colleagues gine e help of paid assistance, provided for out of the research grant € General Education Board to the University of Chicago. Sir William
351:BBCS Bulletin of Board of Celtic Studies,
1161:Grk. rapadia (yf expressed or under- stood) ‘seacoast, seaboard’, fr. TapaAtos ‘by the sea’.
2449:Sw. gosse : Norw. gosse ‘strong fellow’ and ‘boar’, NE dial. gussze ‘swine, pig’, etc., a collog. word of the most diverse applications. Bjérkman, IF 30.252 ff. Hellquist 294.
3744:CHAPTER 3 ANIMALS 3.45 Foau, Cott gal eANo 3.46 Ass, DonKEY 3.12 Mate (adj.) 3.47 Mute gia ene 3.51 Hen, Catcxen (Generic) Blan CASTE 3.52 Cock Blo ESTO 3.53 CAPON 3.16 PasTuRE (vb.) aa ee ON chaaeh Pe, 3.55 CHICKEN 3.18 HerDSMAN aA Goan 3.19 STABLE, STALL ne Duue 3.20 CATTLE (Bovine Species) et at ae se 3.612 Purry a oe 3.62 Car 3 4 CALF 3.63 Mouse eed tae AM ; eS a 3.66 FISHERMAN 3.28 Ews 3.71 Wo.ur | 3.29 Lams 3.72 Lion 3.31 Swint 3.73 BEAR 3.32 Boar 3.74 Fox | 3.33 Barrow 3.75 DEER i 3.34 Sow 8.76 MonxkEY 3.35 Pie 3.77 ELEPHANT 3.36 Goat 3.78 CAMEL | 3.37 Hu-coar 3.79 Hunt (vb.) 3.38 Kip 3.81 InsEctT 3.41 Horse (Generic) 3.82 BEE 3.42 Srantion 3.83 Fy : 3.43 GrLpine 3.84 Worm 344 Mare 3.85 SNAKE
```


## [2026-10-16T05:22:38.953Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^3\\.32 BOAR|3\\.32 BOAR' SYN.txt | head -3; L=$(grep -n -E '3\\.32 BOAR' SYN.txt | tail -1 | cut -d: -f1); sed -n \"$L,$((L+25))p\" SYN.txt | grep -i -E 'Av\\.|NPers|varāz|varaz' | head; grep -n -E '4\\.(21|22) NOSE|NOSE' SYN.txt | head -3; grep -n -i -E 'NPers\\. b[iī]n' SYN.txt | head",
 "description": "Grep Buck boar and nose sections"
}
```


### [2026-10-16T05:22:39.276Z] TOOL RESULT

```
4310:3.32 BOAR
5912:gprs OF T 4.23 NOSE Lith. nosis Goth. .--- pis ON nasar Lett. deguns Gre im Dan. nase Chsl. nosit nasus Sw. nisa SCr. nos naso OE nosu Boh. nos nez ME _~ nose Pol. nos nariz NE nose Russ. os Rum. nas Du. neus Skt. nas-, ghrana- sron OHG nasa Av. nah- sron MHG nase i NHG nase Tl Most of the words for ‘nose’ belong to | then orig. a vulgar epithet, displacing Mo:
```


## [2026-10-16T05:22:41.716Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4310,4340p SYN.txt | grep -n -i -E 'Av|Pers|var' | head; sed -n 5912,5935p SYN.txt | grep -i -o -E '.{0,120}(vaen|Pers|bini|bīnī).{0,150}' | head",
 "description": "Read Buck boar and nose Iranian material"
}
```


### [2026-10-16T05:22:44.009Z] TOOL RESULT

```
10:eber, bér eber (bdr) kuilys kuilis nerast kanec kiernoz kaban varadha- vardza-
31:brav
ugrep: error: error at position 128
80-\xbf][\x80-\xbf]*){0,150}
                            \___exceeds complexity limits
```


## [2026-10-16T05:22:47.474Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4310,4380p SYN.txt | python3 -c \"\nimport sys,re;t=sys.stdin.read()\nfor m in re.finditer(r'var[aā]h|Av\\. v',t): print(t[max(0,m.start()-200):m.start()+250].replace('\\n',' '));print('--')\" | head -20; sed -n 5912,5960p SYN.txt | python3 -c \"\nimport sys,re;t=sys.stdin.read()\nfor m in re.finditer(r'vaen|NPers|Pers\\.',t): print(t[max(0,m.start()-200):m.start()+250].replace('\\n',' '));print('--')\" | head -20",
 "description": "Python search in Buck sections"
}
```


### [2026-10-16T05:22:47.865Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:24:44.770Z] TOOL CALL #65: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build522.py <<'EOF'\nimport json\nWK_BINI=\"https://en.wiktionary.org/wiki/بینی\"\nWK_GORAZ=\"https://en.wiktionary.org/wiki/گراز\"\nWK_BARG=\"https://en.wiktionary.org/wiki/برگ\"\nAB_BARM=\"https://abadis.ir/fatofa/برم/\"\nVJ_GORAZ=\"https://vajehyab.com/moein/گراز\"\nVJ_VORAZ=\"https://vajehyab.com/moein/وراز\"\nAEF_NC={\"ref\":\"AEF:323\",\"status\":\"not_checked\",\"note\":\"Khaleqi Motlaq's Persian translation of Horn is not online; its content checked through the original Horn (HRN no. 261, p. 60), see consulted.\"}\nE=[]\n# entry 0\nE.append({\n \"entry\":0,\"root\":\"Vaenâ 1, Vaěnâ 1\",\"verdict\":\"confirmed\",\n \"modern_form\":\"Avestan vaēnā- f. 'nose' (Y 9.11, Yt 19.40)\",\n \"note\":\"Avestan vaēnā- 'Nase' is a real word (Bartholomae col. ~1320: 'vaēnā- f. Nase ... mp. vēn, np. vgl. bīnī Nase'), and Horn no. 261 bīnī derives the Persian word from it via Pahlavi vēnīk / bēnīk. MacKenzie: wēnīg [wynyk] 'nose' > N bīnī. The deeper etymology is open: Wiktionary gives the traditional link with *weyd- 'see' (cf. bīn-, wēn- 'see') and Gershevitch's alternative *wi- + *h2enh1- 'breathe'; this does not affect Nourai's chain Av. -> MP -> NP. Aryanpur (ARY p.145) wrongly files bīnī under PIE *nas- (that root belongs to Av. nāh-, OP nāham, not to vaēnā-). The '1' marks a homograph; the redirect 'Vaěnâ 1' is skipped. JSON matches the printed page.\",\n \"note_fa\":\"«وَئِنا» (vaēnā-) در اوستا به معنی «بینی» گواهی دارد (یسنه ۹ بند ۱۱ و یشت ۱۹ بند ۴۰) و بارتولومه، هرن (شمارهٔ ۲۶۱) و معین در حاشیهٔ برهان قاطع (ص ۳۴۱) «بینی» فارسی را از همین واژه از راه پهلوی vēnīk می‌دانند. پس ادعای نورایی درست است. ریشهٔ دورتر این واژه روشن نیست: برخی آن را از ریشهٔ «دیدن» (wēn-/bīn-) و گرشویچ آن را از vi- + ریشهٔ «دم زدن» می‌دانند. آریان‌پور «بینی» را به ریشهٔ هندواروپایی *nas- برده که نادرست است؛ آن ریشه به اوستایی nāh- و پارسی باستان nāham مربوط است.\",\n \"sources\":[WK_BINI],\n \"ref_check\":[{\"ref\":\"AEF:323\",\"status\":\"not_checked\",\"note\":\"AEF (Persian translation of Horn's Grundriss) not online; the corresponding Horn entry no. 261 (HRN.txt line 2639: '261. bīnī Nase. ... aw. vaēnā Nase (Y. 9, 11 ...); phlv. vēnik (Bund., AV.), bēnik (AV.)') supports the root.\"}],\n \"consulted\":[\n  {\"src\":\"BRT\",\"where\":\"col. ~1320 (BRT.txt line 22129)\",\"stance\":\"supports\",\"note\":\"'vaēnā- f. Nase: ... Y.9.11 PüZ., Yt.19.40 | kurd. bēn Nase, Geruch; mp. vēn, nbal. gīn Atem; np. vgl. bīnī Nase'.\"},\n  {\"src\":\"POK\",\"where\":\"grep vaēnā/vaena in POK_full.txt\",\"stance\":\"silent\",\"note\":\"Pokorny does not list Av. vaēnā-; his *nas- 'nose' (755) covers Av. nāh- only.\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt, nas-\",\"stance\":\"silent\",\"note\":\"Watkins' nas- 'nose' has no Iranian vaēnā- form.\"},\n  {\"src\":\"WLD\",\"where\":\"only Band 3 (index) on disk\",\"stance\":\"silent\",\"note\":\"no entry for vaēnā- in the register volume.\"},\n  {\"src\":\"SYN\",\"where\":\"4.23 NOSE (SYN.txt line 5912)\",\"stance\":\"silent\",\"note\":\"Buck's table gives Av. nah- only; vaēnā- not discussed.\"},\n  {\"src\":\"ARY\",\"where\":\"p.145 (ocr/ARY/0145.vision.txt)\",\"stance\":\"partial\",\"note\":\"'بینی BĒNĒ NOSE ... *NAS-, *NĀS-, *NES- ... اوستایی VAĒNĀ, NĀH- ... پهلوی WĒNĪG' - lists vaēnā and wēnīg but under the wrong PIE root *nas-.\"}\n ],\n \"nodes\":[\n  {\"id\":1,\"lang\":\"Pahlavi\",\"words\":\"věnîk, běnîk\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Zoroastrian MP wēnīg [wynyk] 'nose' (MacKenzie; Manichaean wynyg) = Av. vaēnā- + the MP suffix -īg (< OIr. *-ika-); Old Iranian diphthong ai > MP ē. The variant bēnīk (Horn: 'bēnik (AV.)', Ardā Wirāz) shows the MP/early NP shift of initial w- > b-, the bridge to NP bīnī. Gershevitch reads the word wīnīg; the reading does not change the derivation.\",\n   \"derivation_fa\":\"پهلوی wēnīg (نوشته wynyk) «بینی» از اوستایی vaēnā- با پسوند -īg ساخته شده است؛ واکهٔ مرکب ai ایرانی باستان در فارسی میانه به ē (یای مجهول) بدل شده است. گونهٔ bēnīk که هرن از ارداویراف‌نامه آورده دگرگونی w- آغازی به b- را نشان می‌دهد که در فارسی نو هم دیده می‌شود. ادعای نورایی درست است.\",\n   \"sources\":[WK_BINI],\n   \"ref_check\":[{\"ref\":\"AEF:323\",\"status\":\"not_checked\",\"note\":\"AEF not online; Horn no. 261 (HRN.txt line 2641-2642: 'phlv. vēnik (Bund., AV.), bēnik (AV.)') - the source AEF translates - has exactly Nourai's two forms.\"}],\n   \"consulted\":[\n    {\"src\":\"PHD\",\"where\":\"p. 90 s.v. wēnīg (PHD_mackenzie.txt line 5326)\",\"stance\":\"supports\",\"note\":\"'wenig [wynyk | M wynyg, N bīnī] nose.'\"},\n    {\"src\":\"NYB\",\"where\":\"glossary, grep vēnīk/wēnīk\",\"stance\":\"silent\",\"note\":\"no entry found in the OCR of Nyberg's glossary.\"},\n    {\"src\":\"HRN\",\"where\":\"no. 261, p. 60\",\"stance\":\"supports\",\"note\":\"'phlv. vēnik (Bund., AV.), bēnik (AV.)'.\"}\n   ]},\n  {\"id\":2,\"lang\":\"Persian\",\"words\":\"bînî\",\"verdict\":\"confirmed\",\n   \"derivation\":\"NP bīnī 'nose' < MP wēnīg: initial w- > b- (as warg > barg, wārān > bārān), MP majhūl ē > ī in modern Persian, and loss of final -g after a long vowel (-īg > -ī). Dialect forms quoted by Mo'in (Semnani vīnī, Mazandarani vēnī, Sorkhe ven) keep the old v-.\",\n   \"derivation_fa\":\"«بینی» فارسی از پهلوی wēnīg آمده است: w آغازی به b بدل شده (چنان‌که در «برگ» از warg و «باران» از wārān)، یای مجهول ē به ی معروف رسیده و g پایانی پس از واکهٔ بلند افتاده است. گونه‌های گویشی سمنانی vīnī و مازندرانی vēnī که معین آورده v کهن را نگه داشته‌اند. ادعای نورایی درست است.\",\n   \"sources\":[WK_BINI],\n   \"ref_check\":[{\"ref\":\"BQT:341\",\"status\":\"supports\",\"note\":\"Borhan vol.1 p.341 (archive.org borhan-ghate-v1 leaf n561; ocr/BQT/341.vision.txt), Mo'in's footnote to بینی: 'سمنانی vînî ، مازندرانی vênî ... پهلوی vênik ، اوستایی vaênâ ... بری bînî'.\"}],\n   \"consulted\":[\n    {\"src\":\"HRN\",\"where\":\"no. 261, p. 60 (HRN.txt line 2639)\",\"stance\":\"supports\",\"note\":\"'261. bīnī Nase ... aw. vaēnā Nase ... phlv. vēnik'.\"},\n    {\"src\":\"HUB\",\"where\":\"note to Horn 261 (HUB.txt line 1149)\",\"stance\":\"supports\",\"note\":\"'261. Dazu auch paz. vīnī nose, nostrils Shk. 273' - adds Pazand vīnī, no objection.\"},\n    {\"src\":\"BQT\",\"where\":\"p.341 fn.\",\"stance\":\"supports\",\"note\":\"see ref_check.\"},\n    {\"src\":\"ARY\",\"where\":\"p.145\",\"stance\":\"partial\",\"note\":\"lists Av. VAĒNĀ, Pahl. WĒNĪG but puts bīnī under PIE *nas-.\"},\n    {\"src\":\"CHEUNG\",\"where\":\"not a verb\",\"stance\":\"silent\",\"note\":\"Cheung covers verbs; no entry.\"}\n   ]}\n ]})\n# entry 3 Var\nDKS=\"ISS_alt_DKS.txt line 5195 (Dictionary of Khotan Saka p.278 s.v. bārman-)\"\nE.append({\n \"entry\":3,\"root\":\"Var\",\"verdict\":\"plausible\",\n \"modern_form\":\"Iranian base *var- 'to cover, enclose' (Av. var-, Khotanese var-), PIE *wer- 'to cover' (Pokorny 5. wer-, p.1160; AHD wer-5)\",\n \"note\":\"The root and gloss are right: Bailey (whose Indo-Scythian Studies Nourai cites; checked through his Dictionary of Khotan Saka, which repeats the material) derives Khotanese bārman- 'enclosure, prison, reservoir' 'from base var- to enclose, shut, Zor.P. varm, N.Pers. barm reservoir ... IE Pok. 1160 wer-'. The language label 'Indo-Schythian' (sic, the book's spelling) is misleading: var- is a common Iranian (and Indo-Iranian, Skt. vṛ-) base, attested in Avestan; Khotanese is only one witness, and the Pahlavi/Persian words cannot descend from Khotanese. MacKenzie has the needed homonym: 2warm 'pool, reservoir' > NP barm, distinct from 1warm 'memory' (Nourai's 'varm 1' numbering does not match MacKenzie's). The derivation *var-ma- 'enclosed (water)' is Bailey's and is not widely discussed elsewhere, hence 'plausible'. JSON matches the page.\",\n \"note_fa\":\"ریشهٔ var- «پوشاندن، در میان گرفتن» درست است و با ریشهٔ هندواروپایی *wer- «پوشاندن» (پوکورنی ۱۱۶۰) پیوند دارد. بیلی در فرهنگ ختنی، «برم» فارسی و warm پهلوی را به معنی «آبگیر» از همین ریشه دانسته (یعنی «جای محصور آب»). اما برچسب «هندوسکایی» (ختنی) گمراه‌کننده است: این ریشه در همهٔ زبان‌های ایرانی، از جمله اوستایی، هست و واژهٔ پهلوی و فارسی نمی‌تواند از ختنی آمده باشد. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\":[],\n \"ref_check\":[{\"ref\":\"ISS:234\",\"status\":\"not_checked\",\"note\":\"Khotanese Texts VI not online; Bailey's Dictionary of Khotan Saka p.278 s.v. bārman- (%s): 'From base var- to enclose, shut, Zor.P. varm, N.Pers. barm reservoir; Oss. D. wærmæ ... IE Pok. 1160 wer-' gives the same claim.\"%DKS}],\n \"consulted\":[\n  {\"src\":\"POK\",\"where\":\"5. wer- p.1160 (POK_full.txt line 91991)\",\"stance\":\"supports\",\"note\":\"'uer-5: to close, cover; to guard, save' - Iranian not cited, Old Indic apa-vṛṇoti etc.\"},\n  {\"src\":\"AHD\",\"where\":\"wer-5 (AHD_watkins1985.txt line 1148)\",\"stance\":\"supports\",\"note\":\"'wer-5. To cover ... [Pok. 5. wer- 1160.]'.\"},\n  {\"src\":\"WLD\",\"where\":\"only Band 3 on disk\",\"stance\":\"silent\",\"note\":\"index volume only.\"},\n  {\"src\":\"ISS_alt_DKS\",\"where\":\"p.278 bārman-; also s.v. dausvera (line 2469)\",\"stance\":\"supports\",\"note\":\"'var- to cover, Av. varma- cloak' and 'bārman- enclosure ... reservoir, from base var- to enclose'.\"}\n ],\n \"nodes\":[\n  {\"id\":1,\"lang\":\"Pahlavi\",\"words\":\"varm 1\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Zoroastrian MP warm [wlm] 'pool, reservoir' (MacKenzie's 2warm, > N barm) is a real word, homonymous with 1warm 'memory'. Bailey explains it as *var-ma- 'enclosure' from the base var- 'to enclose', with the same suffix -ma- as Av. varma- 'cloak' and Khotanese bārman- 'enclosure, reservoir'.\",\n   \"derivation_fa\":\"پهلوی warm (نوشته wlm) به معنی «آبگیر، مخزن آب» در فرهنگ مکنزی آمده و با warm دیگر به معنی «یاد، حافظه» هم‌آواست. بیلی آن را از *var-ma- «جای محصور» از ریشهٔ var- «در میان گرفتن» می‌داند، با همان پسوند -ma- که در ختنی bārman- «حصار، آبگیر» دیده می‌شود. ادعای نورایی درست است.\",\n   \"sources\":[],\n   \"ref_check\":[{\"ref\":\"ISS:234\",\"status\":\"not_checked\",\"note\":\"not online; DKS p.278 bārman- has 'Zor.P. varm' in exactly this sense.\"}],\n   \"consulted\":[\n    {\"src\":\"PHD\",\"where\":\"p. 89 (PHD_mackenzie.txt line 5207-5209)\",\"stance\":\"supports\",\"note\":\"'1warm [wlm | N barm] memory ... 2warm [wlm | N barm] pool, reservoir.'\"},\n    {\"src\":\"NYB\",\"where\":\"glossary grep '^varm'\",\"stance\":\"silent\",\"note\":\"no entry for varm in Nyberg's glossary OCR.\"},\n    {\"src\":\"ISS_alt_DKS\",\"where\":\"p.278\",\"stance\":\"supports\",\"note\":\"'Zor.P. varm, N.Pers. barm reservoir'.\"}\n   ]},\n  {\"id\":2,\"lang\":\"Persian\",\"words\":\"barm\",\"verdict\":\"confirmed\",\n   \"derivation\":\"NP barm 'pool, pond, reservoir' (Borhan: 'تالاب و استخر و چشمهٔ آب'; Shahid Balkhi, Farrokhi) < MP warm with the regular initial w- > b-. Mo'in tags it [په.] (Pahlavi). It must be kept apart from barm 'memory' (< 1warm) and borm 'pole, trellis'.\",\n   \"derivation_fa\":\"«بَرم» به معنی «آبگیر، استخر، برکه» (برهان: «تالاب و استخر و چشمهٔ آب»؛ شاهد از شهید بلخی و فرخی) از پهلوی warm است با دگرگونی منظم w آغازی به b. معین آن را پهلوی [په.] نشان داده است. این واژه از «برم» به معنی «از بر، حافظه» (از warm دیگر) و «بُرم» به معنی «داربست» جداست. ادعای نورایی درست است.\",\n   \"sources\":[AB_BARM],\n   \"ref_check\":[\n    {\"ref\":\"ISS:234\",\"status\":\"not_checked\",\"note\":\"not online; DKS p.278 'N.Pers. barm reservoir' supports.\"},\n    {\"ref\":\"MON:511\",\"status\":\"supports\",\"note\":\"Mo'in via abadis.ir: 'فرهنگ معین (بَ) [په.] (اِ.) آبگیر، استخر، برکهٔ آب' (page number not verifiable online; local MON OCR too poor).\"}],\n   \"consulted\":[\n    {\"src\":\"MON\",\"where\":\"abadis.ir s.v. برم\",\"stance\":\"supports\",\"note\":\"'(بَ) [په.] آبگیر، استخر، برکة آب'; Dehkhoda: 'تالاب و استخر و چشمه آب (برهان)'.\"},\n    {\"src\":\"PHD\",\"where\":\"2warm\",\"stance\":\"supports\",\"note\":\"'2warm ... N barm pool, reservoir'.\"},\n    {\"src\":\"HRN\",\"where\":\"grep barm\",\"stance\":\"silent\",\"note\":\"Horn has no entry barm.\"},\n    {\"src\":\"HUB\",\"where\":\"grep barm\",\"stance\":\"silent\",\"note\":\"no entry.\"}\n   ]}\n ]})\n# entry 5 Varaza\nE.append({\n \"entry\":5,\"root\":\"Varâza\",\"verdict\":\"confirmed\",\n \"modern_form\":\"Avestan varāza- m. 'boar' < Proto-Iranian *warājáh < Proto-Indo-Iranian *warāȷ́ʰás; cognate Sanskrit varāhá-\",\n \"note\":\"Av. varāza- 'Männchen des Schweins, Eber' (Bartholomae col. ~1368, Yt 14.15) is secure, and the root note 'cognate with Sanskrit varāha' is right (Wiktionary, Horn no. 896, Bartholomae). Any PIE connection (Aryanpur's '*wer-, *weros (شاید)', Latin verrēs) is uncertain, as Aryanpur himself says; Nourai sensibly stops at Avestan. Armenian varaz and Syriac warzā are Iranian loans. JSON matches the page (including the Amid Lobaki verse).\",\n \"note_fa\":\"اوستایی varāza- «گراز نر» (بارتولومه، یشت ۱۴ بند ۱۵) واژه‌ای استوار است و هم‌ریشگی آن با سنسکریت varāha- که نورایی در یادداشت آورده درست است. پیوند آن با ریشه‌ای هندواروپایی و لاتین verrēs «خوک نر» قطعی نیست (آریان‌پور هم «شاید» نوشته). ارمنی varaz وام‌واژه‌ای ایرانی است. ادعای نورایی درست است.\",\n \"sources\":[WK_GORAZ],\n \"ref_check\":[{\"ref\":\"BQT:1779\",\"status\":\"supports\",\"note\":\"Borhan vol.3 p.1779 (ocr/BQT/1779.png, OCR), Mo'in's asterisked footnote to گراز: 'اوستا varâza (گراز)، پهلوی varâz (نوشته میشود varâč)، ارمنی ... هندی باستان varâha (گراز)، کردی berâz «اسشق ۸۹۶»'.\"}],\n \"consulted\":[\n  {\"src\":\"BRT\",\"where\":\"col. ~1368 (BRT.txt line 22818-22826)\",\"stance\":\"supports\",\"note\":\"'varāza- m. Männchen des Schweins, Eber ... ai. varāha- m., np. (Npü.) gurāz'.\"},\n  {\"src\":\"POK\",\"where\":\"grep varāza/varāha\",\"stance\":\"silent\",\"note\":\"Pokorny has no entry (no accepted PIE etymology).\"},\n  {\"src\":\"AHD\",\"where\":\"grep boar\",\"stance\":\"silent\",\"note\":\"no root for this word.\"},\n  {\"src\":\"WLD\",\"where\":\"Band 3 only\",\"stance\":\"silent\",\"note\":\"index volume only.\"},\n  {\"src\":\"SYN\",\"where\":\"3.32 BOAR (SYN.txt line 4310)\",\"stance\":\"supports\",\"note\":\"table lists Skt. varāha-, Av. varāza-.\"},\n  {\"src\":\"ARY\",\"where\":\"p.425 (ocr/ARY/0425.vision.txt)\",\"stance\":\"supports\",\"note\":\"'اوستایی VARĀZA; پهلوی VARĀZ, WARĀZ; ... سانسکریت VARĀHA' with PIE *wer-, *weros marked (شاید).\"}\n ],\n \"nodes\":[\n  {\"id\":1,\"lang\":\"Pahlavi\",\"words\":\"varâz\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Zoroastrian MP warāz [wlʾc] 'boar' (MacKenzie; written with final -c = -z) continues Av./OIr. *varāza- with loss of the final vowel; Old Iranian -z- is kept. The word is common in Sasanian personal names (Warāz, Warāzdād, Warāz-Bandag), and Armenian borrowed it as varaz.\",\n   \"derivation_fa\":\"پهلوی warāz (نوشته wlʾc) «گراز» دنبالهٔ اوستایی varāza- است که واکهٔ پایانی‌اش افتاده است. این واژه در نام‌های ساسانی مانند وراز، ورازداد و ورازبنده فراوان است و ارمنی هم آن را به صورت varaz وام گرفته است. ادعای نورایی درست است.\",\n   \"sources\":[WK_GORAZ],\n   \"ref_check\":[{\"ref\":\"MON:3212\",\"status\":\"supports\",\"note\":\"Mo'in (vajehyab.com/moein/گراز): 'گراز (گُ) [په.] (اِ.) ۱- خوک نر. ۲- بیل' - tags the word as Pahlavi; Pahlavi form itself not shown online, page not verifiable.\"}],\n   \"consulted\":[\n    {\"src\":\"PHD\",\"where\":\"p. 89 (PHD_mackenzie.txt line 5189)\",\"stance\":\"supports\",\"note\":\"'warāz [wlʾc | N gurāz] boar.'\"},\n    {\"src\":\"NYB\",\"where\":\"glossary line 3955\",\"stance\":\"partial\",\"note\":\"only 'Varāzīn patron. of n. pr. Varāz' - the name, not the common noun.\"},\n    {\"src\":\"HRN\",\"where\":\"no. 896, p.200\",\"stance\":\"supports\",\"note\":\"'phlv. varāz (geschrieben varāc)'.\"}\n   ]},\n  {\"id\":2,\"lang\":\"Persian\",\"words\":\"vorâz; gorâz\",\"verdict\":\"confirmed\",\n   \"derivation\":\"gorāz 'boar' < MP warāz with the regular NP change of initial wa-/wu- > gu- (cf. MP wišād > gušād, wurg > gurg 'wolf'), plus vowel rounding wa- > wu- > gu-; the figurative sense 'brave, strong man' (Amid Lobaki's verse in Borhan p.1780: 'درین بیت بمعنی شجاع و پهلوان آمده') comes from the boar as symbol of strength (Verethraghna appears as a boar in Yt 14.15). vorāz is the variant keeping the initial w- (cf. Mazandarani/Tabari varāz); Mo'in lists it as 'گراز، خوک نر', though Horn notes the Shahnameh verse cited for it in Vullers is spurious.\",\n   \"derivation_fa\":\"«گُراز» از پهلوی warāz است با دگرگونی منظم w آغازی (پیش از واکهٔ گرد) به g در فارسی نو، چنان‌که در «گرگ» از wurg و «گشاد» از wišād. معنای مجازی «دلیر و پهلوان» در بیت عمید لوبکی (برهان، ص ۱۷۸۰) از نیرومندی گراز است که در بهرام‌یشت ایزد پیروزی به پیکر آن درمی‌آید. «وُراز» گونه‌ای است که w کهن را نگه داشته (مانند طبری varāz)؛ معین آن را «گراز، خوک نر» معنی کرده است. ادعای نورایی درست است.\",\n   \"sources\":[WK_GORAZ,VJ_GORAZ,VJ_VORAZ],\n   \"ref_check\":[\n    {\"ref\":\"MON\",\"status\":\"supports\",\"note\":\"vajehyab Mo'in: 'گراز (گُ) [په.] ... خوک نر' and 'وراز (وُ) (اِ.) گراز، خوک نر'.\"},\n    {\"ref\":\"HRN:200\",\"status\":\"supports\",\"note\":\"Horn p.200 no. 896 (HRN.txt line 7787): '896. gurāz Eber. aw. varāza- Eber; phlv. varāz ... ai. varāha- Eber ... np. verāz Eber wird im FS (Vullers) durch einen angeblichen Šāhnāmevers belegt, der aber des Metrums halber kein solcher sein kann.'\"},\n    {\"ref\":\"BQT:1780\",\"status\":\"supports\",\"note\":\"Borhan vol.3 p.1780 (ocr/BQT/1780 OCR): Mo'in's note on Bahram Yasht boar symbolism and 'درین بیت بمعنی شجاع وپهلوان آمده: دور سپهر مثل تو هرگز نیاورد از هفت پشت پهلو شیرافکن و گراز. عمید لوبکی «رشیدی»' - the very verse quoted by Nourai.\"},\n    {\"ref\":\"BQT:2263\",\"status\":\"supports\",\"note\":\"Borhan vol.4 p.2263 (ocr/BQT/2263.png, pdf p.346; OCR): 'وراز - بضم اول، بروزن و معنی گراز است که خوک نر باشد'; fn. 'گراز (ه.م.) ، طبری varâz (گراز)'.\"}],\n   \"consulted\":[\n    {\"src\":\"HRN\",\"where\":\"no. 896\",\"stance\":\"supports\",\"note\":\"see ref_check.\"},\n    {\"src\":\"HUB\",\"where\":\"grep 896/gurāz\",\"stance\":\"silent\",\"note\":\"no comment found in HUB OCR.\"},\n    {\"src\":\"BQT\",\"where\":\"pp.1779, 1780, 2263\",\"stance\":\"supports\",\"note\":\"see ref_check.\"},\n    {\"src\":\"ARY\",\"where\":\"p.425\",\"stance\":\"supports\",\"note\":\"'GORĀZ ... پهلوی VARĀZ, WARĀZ'.\"},\n    {\"src\":\"MON\",\"where\":\"vajehyab\",\"stance\":\"supports\",\"note\":\"[په.] tag.\"}\n   ]}\n ]})\n# entry 6 Varekahe\nE.append({\n \"entry\":6,\"root\":\"Varekahe, Varaka\",\"verdict\":\"confirmed\",\n \"modern_form\":\"Young Avestan varəka- n. 'leaf' (gen. sg. varəkahe, Frahang-i Oim) < Proto-Indo-Iranian *warkás ~ *walkás; cf. Sanskrit valka- 'bark'\",\n \"note\":\"Av. varəka- 'Blatt (der Pflanzen)' is in Bartholomae col. 1367; the form 'varekahe' Nourai uses as headword is its genitive singular varəkahe as attested in the Frahang-i Oīm (Bartholomae '°kahe F. 8'), and 'Varaka' is a simplified spelling of the stem - neither is an error, though the citation form should be varəka-. Buck 8.56 LEAF: 'Av. varəka-, cf. MPers. varg, NPers. barg. etym.? Barth. 1367'; Wiktionary links it to Skt. valka- 'bark' (PIIr *warkás ~ *walkás). JSON matches the page (script_extra بلگ، بلگه، برگه).\",\n \"note_fa\":\"اوستایی varəka- «برگ» (بارتولومه ستون ۱۳۶۷) واژه‌ای گواهی‌شده است؛ «varəkahe» که نورایی سرواژه کرده حالت اضافی (genitive) همین واژه در فرهنگ اویم است و «varaka» شکل ساده‌شدهٔ ستاک آن. باک و ویکی‌واژه آن را با پهلوی warg و فارسی «برگ» یکی می‌دانند و ویکی‌واژه آن را هم‌ریشه با سنسکریت valka «پوست درخت» می‌داند. ادعای نورایی درست است.\",\n \"sources\":[WK_BARG],\n \"ref_check\":[\n  {\"ref\":\"SNS:281\",\"status\":\"partial\",\"note\":\"Tavoosi's Shayast-ne-Shayast glossary index (SNS.txt line 31130) has 'varg 281/12' - the Pahlavi word on p.281, not the Avestan root itself.\"},\n  {\"ref\":\"SYN:525\",\"status\":\"supports\",\"note\":\"Buck 8.56 LEAF (SYN.txt line 13242-13271): 'Av. varəka-, cf. MPers. varg, NPers. barg. etym.? Barth. 1367'.\"},\n  {\"ref\":\"EAV:86\",\"status\":\"not_found\",\"note\":\"grep varəka/vareka in EAV_studies.txt found nothing; the article covers pp. 861-869, so '86' is probably a truncated page number.\"}],\n \"consulted\":[\n  {\"src\":\"BRT\",\"where\":\"col. 1367 (BRT.txt line 22848)\",\"stance\":\"supports\",\"note\":\"'varəka- m. Blatt (der Pflanzen): ... °kahe F. 8'.\"},\n  {\"src\":\"POK\",\"where\":\"1139 wel- (POK_full.txt line 90388)\",\"stance\":\"partial\",\"note\":\"lists Old Indic valka- 'bast' under wel- 'hair, wool' (guttural extension) without Iranian varəka-.\"},\n  {\"src\":\"AHD\",\"where\":\"grep leaf\",\"stance\":\"silent\",\"note\":\"no root for this word.\"},\n  {\"src\":\"WLD\",\"where\":\"Band 3 only\",\"stance\":\"silent\",\"note\":\"index volume only.\"},\n  {\"src\":\"SYN\",\"where\":\"8.56 LEAF\",\"stance\":\"supports\",\"note\":\"see ref_check.\"}\n ],\n \"nodes\":[\n  {\"id\":1,\"lang\":\"Pahlavi\",\"words\":\"varg, valg\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Zoroastrian MP warg 'leaf', written [wlg] (Pahlavi l for r, hence Mo'in's reading valg), continues Av./OIr. *varəka- with syncope of the medial vowel and loss of the final vowel (*varka- > warg, k > g after r). Parthian has wrgr; the dialects (Gilaki balg, Natanzi valg) and Early NP balg show the l-variant that Wiktionary traces to PIIr *walkás.\",\n   \"derivation_fa\":\"پهلوی warg «برگ» (نوشته wlg، که معین آن را valg خوانده) دنبالهٔ اوستایی varəka- است: واکهٔ میانی و پایانی افتاده و k پس از r به g نرم شده است. گونه‌های دارای l مانند گیلکی balg و نطنزی valg و «بلگ» فارسی کهن نشان می‌دهند که در ایرانی دو گونهٔ *warka- و *walka- بوده است. ادعای نورایی درست است.\",\n   \"sources\":[WK_BARG],\n   \"ref_check\":[\n    {\"ref\":\"BQT:260\",\"status\":\"supports\",\"note\":\"Borhan vol.1 p.260 (archive.org borhan-ghate-v1 leaf n480; ocr/BQT/260.vision.txt), Mo'in fn.: 'برگ - بفتح اول در پهلوی valg ، اوستا varəka «بارتولمه ۱۳۶۷» «نیبرگ ۲۳۲» و نیز در پهلوی vark ... گیلکی balg'.\"},\n    {\"ref\":\"AEF:259\",\"status\":\"not_checked\",\"note\":\"AEF not online; Horn no. 203 (HRN p.~60, line 2165-2173): 'barg Blatt ... aw. varəkah (ZPGl.); phlv. varg Blatt' supports.\"}],\n   \"consulted\":[\n    {\"src\":\"PHD\",\"where\":\"p. 89 (PHD_mackenzie.txt line 5205)\",\"stance\":\"supports\",\"note\":\"'warg [wlg | N barg] leaf.'\"},\n    {\"src\":\"NYB\",\"where\":\"glossary p.~203 (NYB_vol2_glossary.txt line 3968)\",\"stance\":\"supports\",\"note\":\"'varg [wlg] leaf ... MPrth wrgr ... — Av. (1367) varəka-; Paz. varg; NP barg'.\"}\n   ]},\n  {\"id\":2,\"lang\":\"Persian\",\"words\":\"barg\",\"verdict\":\"confirmed\",\n   \"derivation\":\"NP barg 'leaf' < MP warg with the regular initial w- > b- (cf. wārān > bārān); the variants balg, balge in the book's bracket continue the l-form (MP/dialect valg). The senses 'page, sheet' (barg-e kāğaz) and 'provisions, sustenance; equipment' (Mo'in: 'توشه، آذوقه ... اسباب و سامان'; Rumi's 'حرص برگ') are listed by Borhan under the same headword; Mo'in treats the 'provisions' sense as a separate homograph, so the semantic link leaf -> sustenance is traditional rather than proven.\",\n   \"derivation_fa\":\"«برگ» فارسی از پهلوی warg است با دگرگونی منظم w آغازی به b (مانند «باران» از wārān)؛ «بلگ» و «بلگه» که در کمانک کتاب آمده دنبالهٔ گونهٔ l‌دار (valg) است. معنی‌های «ورق» و «توشه، ساز و سامان» (حرص برگ در بیت مولوی) را برهان زیر همین سرواژه آورده، ولی معین معنی «توشه» را جدا آورده است؛ پس پیوند معنایی «برگ درخت» و «توشه» سنتی است و اثبات‌نشده. ادعای اصلی نورایی درست است.\",\n   \"sources\":[WK_BARG],\n   \"ref_check\":[\n    {\"ref\":\"MON:571\",\"status\":\"partial\",\"note\":\"Mo'in online (vajehyab) shows برگ (بَ) 'توشه، آذوقه، اسباب و اثاثیهٔ زندگی، میل، آرزو' - the 'sustenance' homograph; the leaf entry with etymology could not be read in the poor local OCR.\"},\n    {\"ref\":\"AEF:259\",\"status\":\"not_checked\",\"note\":\"AEF not online; Horn no. 203 'barg Blatt ... aw. varəkah; phlv. varg' supports.\"}],\n   \"consulted\":[\n    {\"src\":\"HRN\",\"where\":\"no. 203 (HRN.txt line 2165)\",\"stance\":\"supports\",\"note\":\"'203. barg Blatt ... aw. varəkah (ZPGl.); phlv. varg Blatt, kurd. ... valg, belk, balg'.\"},\n    {\"src\":\"HUB\",\"where\":\"HUB.txt line 5457\",\"stance\":\"supports\",\"note\":\"'barg Blatt = zd. vareka-'.\"},\n    {\"src\":\"BQT\",\"where\":\"p.260 fn.\",\"stance\":\"supports\",\"note\":\"see node 1.\"},\n    {\"src\":\"ARY\",\"where\":\"Latin index 'WARG, VALG (PAHLAVI)'\",\"stance\":\"supports\",\"note\":\"Aryanpur lists Pahlavi warg, valg under برگ (index page; entry page not rendered).\"},\n    {\"src\":\"MON\",\"where\":\"vajehyab\",\"stance\":\"partial\",\"note\":\"sustenance homograph only.\"}\n   ]}\n ]})\nout={\"pdf_page\":522,\"book_page\":492,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-16\",\"entries\":E}\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-522.json','w'),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build522.py && cd /home/sfmqrb/git/rishe-private && python3 -m json.tool data/verification/page-522.json >/dev/null && python3 tools/verify_check.py 522",
 "description": "Write page-522 JSON and run checker"
}
```


### [2026-10-16T05:24:45.542Z] TOOL RESULT

```
nodes verified: 8/8
node verdicts: {'confirmed': 8}
root verdicts: {'confirmed': 3, 'plausible': 1}
ref checks: {'not_checked': 5, 'supports': 8, 'partial': 1}
books consulted: {'supports': 21, 'silent': 6, 'partial': 3} | by book: {'HRN': 6, 'PHD': 5, 'NYB': 4, 'HUB': 4, 'BQT': 3, 'ARY': 3, 'MON': 3, 'CHEUNG': 1, 'ISS_alt_DKS': 1}
```


## [2026-10-16T05:24:57.231Z] TOOL CALL #66: SubagentHandback

```json
{
 "message": "I wrote `/home/sfmqrb/git/rishe-private/data/verification/page-522.json` for PDF page 522 (book page 492). `verify_check.py 522` shows 0 PROBLEM lines.\n\n**Verdict counts:** 4 entries checked (the 3 redirects were skipped). Roots: 3 confirmed, 1 plausible. Nodes: 8 of 8 confirmed. There are no disputed or transcription_suspect items.\n\n**Notes per entry:**\n- **Vaenâ 1 (Avestan vaēnā- 'nose')**, chain Pahlavi wēnīg → bīnī: confirmed by Bartholomae, Horn no. 261, MacKenzie, and Mo'in's Borhan footnote on p.341. The deeper root is unclear: the traditional link is *weyd- 'see', and Gershevitch proposes another. Aryanpur's *nas- is wrong.\n- **Var ('Indo-Schythian', 'to cover, enclose')**, chain Pahlavi warm → barm: plausible. Bailey's Dictionary of Khotan Saka p.278 and MacKenzie's \"²warm … pool, reservoir\" support the words and the meaning. The label is misleading, though: var- is a common Iranian base from PIE *wer- 'cover' (Pokorny 1160), so the Pahlavi and Persian words cannot come from Khotanese. ISS:234 itself is not online.\n- **Varâza ('boar')**, chain warāz → vorâz / gorâz: confirmed by Horn p.200, Bartholomae, and Borhan pp.1779, 1780 and 2263. Borhan p.1780 contains the Amid Lobaki verse Nourai quotes.\n- **Varekahe / Varaka ('leaf')**, chain warg/valg → barg: confirmed by Bartholomae col. 1367, Nyberg, MacKenzie, Buck p.525 and Borhan p.260. \"Varekahe\" is the genitive varəkahe from the Frahang-i Oim, not a misprint. The proper citation form is varəka-.\n- **EAV:86** (Varekahe root): I could not find this reference, probably a misprint for one of the article's pages 861–869.\n- **MON page numbers** could not be checked against the poor local OCR, so I verified the Mo'in entries on vajehyab and abadis.\n\n**Extraction errors:** none. The JSON matches the printed page, including the extra Persian forms and both verses.\n\n**Files saved for audit:**\n- Borhan vision transcripts: `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/341.vision.txt` and `260.vision.txt`\n- Aryanpur vision transcripts: `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/ARY/0145.vision.txt` and `0425.vision.txt`\n\nI also deleted the cached `ocr/ARY/0275.png` and `0275.txt`. `ref_page.py ARY:275` had rendered the wrong page (the gorāz entry is printed p.425, pdf p.424)."
}
```


### [2026-10-16T05:24:57.514Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
