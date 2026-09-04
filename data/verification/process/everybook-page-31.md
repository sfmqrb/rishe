# Verification process log — everybook-page-31


## [2026-09-04T18:06:47.323Z] INPUT

Task: bring an existing verification file up to the "consult every relevant book" rule. File: /home/sfmqrb/git/rishe/data/verification/page-31.json (root Ab 1/Ap 1 "water", 16 nodes). The chart with Nourai's citations is /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-31.txt.

Read /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md, in particular the sections "Use EVERY relevant book on disk", "Checking Nourai's OWN cited references" and "Process documentation", and the source matrix /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md (file paths of every local book — they all exist under /home/sfmqrb/git/rishe/data/verification/sources/refs/; the reference table /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json gives page offsets and lookup hints).

For the root entry and for EVERY node: grep the books the matrix lists for that node's language (for New Persian words that includes Horn HRN, Hübschmann HUB, Cheung, Borhan BQT vols 1-5 with Mo'in's footnotes, Mo'in MON, and Aryanpur ARY; for Arabic Klein, Jeffery FVQ, Addi Shir AFM, Asbaghi PLA, Fraenkel AFA, Lokotsch LKT; for IE nodes Pokorny, Walde-Pokorny WLD, Watkins AHD, Mann IEC, Buck SYN; for Pahlavi MacKenzie PHD and Nyberg NYB; etc.), and add a `consulted` array to the node exactly as specified: {"src","where","stance" (supports/contradicts/partial/silent),"note" with the quoted phrase}. At least two different books per node where the matrix lists two or more; "silent" entries count. Do not duplicate what is already in `ref_check` (Nourai's own citations) — but if a `ref_check` item is `not_checked` and the book is NOW on disk (e.g. Borhan vols 3-5, Asbaghi, Irānvij, Walde-Pokorny 1-2), re-check it and update its status/note. Do NOT change verdicts, derivations or sources unless a book plainly overturns the existing verdict; in that case update the verdict, append one sentence to `derivation`, and say so in your summary. If you use a web page, archive it with tools/fetch_source.py and add it to `sources`.

Write the file back in place (valid JSON, UTF-8). Run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 31` (0 PROBLEM lines; "books consulted" tally non-empty). Reply with a short summary: number of consulted entries by stance, which books were used, any ref_check upgrades, and any verdict changes with reasons.


## [2026-09-04T18:06:49.466Z] AGENT

I'll start by reading the instructions, source matrix, chart, and the verification file.


## [2026-09-04T18:06:50.694Z] TOOL CALL #1: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && sed -n '1,400p' AGENT_INSTRUCTIONS.md",
 "description": "Read agent instructions"
}
```


### [2026-09-04T18:06:50.757Z] TOOL RESULT

```
# Etymology verification task — instructions

You are verifying the etymological derivations from Ali Nourai's *An Etymological
Dictionary of Persian, English and other Indo-European Languages* (1999), which
this repository (`/home/sfmqrb/git/rishe`) turned into JSON
(`data/extracted/batch/page-<pdf>.json`). Compact text renderings of the charts
are in `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-<pdf>.txt`.

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
   - `transcription_suspect` — the JSON data looks like a transcription error from the scan
     (a misread letter, an impossible form, a wrong Persian script); say what you think the
     book actually printed and why.
4. Record sources as URLs (Wiktionary page, Etymonline page, AHD appendix entry, archive.org
   page of Klein/Horn/Bartholomae, etc.). Also note when Nourai's own cited reference
   (KLN, POK, AHD, BQT, MON, HRN, HUB…) is itself the modern standard for that claim.


## Checking Nourai's OWN cited references (required)

Every node carries `refs=` — Nourai's citations, e.g. `KLN:164; FVQ:75` (abbreviation:page;
`MON5:528` = MON vol. 5 p. 528). The author claims each arrow is supported by those pages.
You must check them:

- The bibliography key (abbreviation → book) is in
  `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt`.
- Where each reference can be read online is in
  `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json`
  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`).
- If `local_file` is set, the OCR text of that book is on disk: grep it for the headword
  (try several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and,
  if `page_offset` is given, locate the cited page (pages are separated by form-feeds; use
  `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one page). Read the entry and judge whether
  it actually says what Nourai's arrow says.
- **Scanned references without OCR text** (Borhan-e Qate' vols 3-5 = BQT pages ~1208-2475,
  Farahvashi's Iranvij = IRN, and any entry whose table record has a `scans` list): do NOT
  OCR whole books. Fetch only the cited page:
  `python3 /home/sfmqrb/git/rishe/tools/ref_page.py BQT:918 --image`
  It renders that one page to PNG, OCRs it (Persian OCR is rough), caches both under
  `data/verification/sources/refs/ocr/`, and prints the text plus the PNG path. If the OCR
  is unreadable, Read the PNG (you can read Persian print directly), and then SAVE what you
  read: write the entry/entries you used (headword, Mo'in's etymological footnote, and any
  surrounding lines you relied on) verbatim to the companion file
  `data/verification/sources/refs/ocr/<ABBR>/<page>.vision.txt` (the tool prints the exact
  paths). The tool prefers that file next time, so nobody pays for reading the image again.
  If the printed page number on the image is off, re-run with `--pdf-page <n>` adjusted, and
  note the correct pdf page in your ref_check note.
- If `kind` is `website`, use the `lookup_hint` URL pattern with WebFetch.
- Do this for at least ONE cited reference per node (the most authoritative available:
  POK/AHD/KLN for IE roots, HRN/HUB/BRT/KNT/PHD for Iranian, KLN/FVQ/AFM/PLA for Semitic,
  BQT/MON for Persian). If none of a node's references is accessible, say so.

Add to every node a `ref_check` array:

```json
"ref_check": [
  {"ref": "KLN:164", "status": "supports", "note": "Klein s.v. 'cherub': Heb. kerūbh, prob. rel. to Akkad. karābu 'to bless', metathesis of b-r-k — exactly Nourai's claim."},
  {"ref": "FVQ:75", "status": "not_checked", "note": "no online copy"}
]
```

`status` ∈ `supports` (the page says what the arrow says) · `partial` (the reference has the
word but a different/looser derivation) · `contradicts` (the reference says something else)
· `not_found` (checked the text, could not find the entry/page) · `not_checked` (reference
not accessible online). Quote the key phrase of the reference in `note` when you can.

Also add to each entry a root-level `ref_check` for the root's own refs (e.g. `POK:244`).


## Process documentation (required)

The owner wants to be able to audit every step later. Therefore:

- **Every web page you rely on must be archived**: after you read a page (WebFetch or
  curl), run
  `python3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
  This stores the page as text under `data/verification/sources/web/` and indexes it. Only
  URLs that were archived this way may appear in a `sources` array. (Batch several calls in
  one Bash command to save time.)
- **Every lookup in a local reference text must be quoted**: in `ref_check[].note` include
  the exact phrase(s) you found (with the grep pattern or page you used, e.g.
  "KLN.txt p.164 (ff-page 178): 'cherub … prob. rel. to Akkad. karābu'"), so the finding can
  be re-run.
- Your full transcript (every tool call and result) is exported automatically by the
  coordinator; nothing else needed for that.


## Use EVERY relevant book on disk (required)

Checking only the reference Nourai cites is not enough. For every node, also consult the
other books in the local library that could speak to that claim, and record what each says.
The list of which books cover which kind of node, with file paths, is
`/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md`
(also `data/verification/sources/SOURCE_MATRIX.md`). Minimum per node:

- an Indo-European node or root box: Pokorny (POK) AND Walde-Pokorny (WLD) AND Watkins/AHD,
  plus Mann (IEC) or Buck (SYN) when the word is a common noun;
- an Avestan / Old Persian node: Bartholomae (BRT) or Kent (KNT);
- a Pahlavi / Middle Persian node: MacKenzie (PHD) and Nyberg (NYB);
- a New Persian node: Horn (HRN), Hübschmann (HUB), Cheung (CHEUNG, for verbs), Borhan-e
  Qate' with Mo'in's footnotes (BQT), Mo'in (MON), and Aryanpur (ARY, once its text exists);
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

## Sources to use (in roughly this order)

- **Wiktionary** (en.wiktionary.org) — has the best coverage of Persian, Middle Persian,
  Avestan, Old Persian, Sogdian, Arabic etymologies, with citations (Cheung 2007, Hasandust,
  MacKenzie 1971, Bartholomae, Horn, Hübschmann, Nourai himself). Fetch the word's page AND
  the `Reconstruction:Proto-Indo-European/…` / `Reconstruction:Proto-Iranian/…` pages.
  Use URL-encoded Persian/Arabic script for those pages.
- **Etymonline** (etymonline.com/word/<word>) for English/French/Latin/Greek chains.
- **American Heritage Dictionary IE roots** (ahdictionary.com/word/indoeurop.html or
  ahdictionary.com/word/search.html?q=<root>) — Nourai's "AHD" citations refer to the 1975
  appendix; the online appendix is the updated edition of the same list.
- **Pokorny** — via indo-european.info, starlingdb.org, or Wiktionary's Pokorny citation;
  Nourai's "POK:nnn" is a page number in Pokorny's IEW.
- **Klein's Comprehensive Etymological Dictionary** (KLN) and **Horn's Grundriss der
  neupersischen Etymologie** (HRN), **Hübschmann's Persische Studien** (HUB),
  **MacKenzie's Concise Pahlavi Dictionary** (PHD), **Bartholomae AiW** (BRT) are on archive.org
  if needed for a hard case.
- **Encyclopaedia Iranica** (iranicaonline.org) for historical/cultural routes.
- **Nişanyan Sözlük** (nisanyansozluk.com) for Turkish; **Lisān al-ʿArab** / Wiktionary for Arabic.
- Use WebSearch when you don't know the right page; use WebFetch to read a page.

Do NOT fabricate sources. If a page did not load or didn't help, don't cite it.
If a chain is well known and uncontroversial (e.g. Latin → Old French → English), one good
source covering the chain is enough; spend your effort on the Iranian and Semitic links,
which are where errors are likelier.

## Output — write ONE file per page

Write `/home/sfmqrb/git/rishe/data/verification/page-<pdf>.json` (UTF-8, no BOM):

```json
{
  "pdf_page": 126,
  "book_page": 96,
  "verified_by": "claude-fable-5-1",
  "verified_on": "2026-09-04",
  "entries": [
    {
      "entry": 0,
      "root": "Dheigh, Dhigha",
      "verdict": "confirmed",
      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
      "nodes": [
        {
          "id": 6,
          "lang": "Avestan",
          "words": "pairi-daeza",
          "verdict": "confirmed",
          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' (PIE *dʰeyǵʰ-, o-grade *dʰoyǵʰ-o- > Iranian *daiza-). Attested in the Vidēvdād (pairi-daēzaiiąn) …",
          "sources": ["https://en.wiktionary.org/wiki/pairidaēza", "https://www.etymonline.com/word/paradise"]
        },
        {
          "id": 9,
          "lang": "Greek",
          "words": "paradeisos",
          "verdict": "confirmed",
          "derivation": "Borrowed from Old Iranian *paridaiza- (Median/Old Persian form with -d-, cf. Elamite par-te-taš, Akkadian pardēsu) in the 5th c. BCE; first in Xenophon (Anabasis 1.2.7) for the Persian kings' walled hunting parks. Greek -ei- renders Iranian /ai/ ~ /ē/; -os is the Greek nominative ending. The Septuagint (3rd c. BCE) used it for the Garden of Eden, whence the 'heaven' sense.",
          "sources": ["https://en.wiktionary.org/wiki/παράδεισος"]
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
- Keep `note` on the entry for root-level comments and for anything cross-cutting
  (e.g. "Nourai's whole Semitic branch here is rejected by Klein …").
- If a node lists several words, cover each word; if they differ in verdict, use the worst
  verdict for the node and explain per word in `derivation`.
- Where the chart's own NOTE already records a dispute (e.g. "POK:694 derives Latin mattus
  from root Mad"), evaluate it: say which side modern scholarship takes.
- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted` (array).
- Valid JSON only. Test it with `python3 -m json.tool` before finishing.
- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason).
  Do not paste the JSON back into your reply.
```


## [2026-09-04T18:06:55.226Z] TOOL CALL #2: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat SOURCE_MATRIX.md; echo ======; cat charts/page-31.txt; echo ======; python3 -c \"\nimport json;d=json.load(open('refs_online.json'));\nfor k,v in d.items(): print(k, v.get('local_file'), v.get('page_offset'), v.get('lookup_hint','')[:80])\"",
 "description": "Read source matrix, chart, refs table"
}
```


### [2026-09-04T18:06:56.905Z] TOOL RESULT

```
Exit code 1
# Source matrix — which local books to grep for each kind of node

All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.

ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).


## Indo-European roots (any IE node, root boxes)

- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt`
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt`
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt`
- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt`
- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`

## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt`
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD_mackenzie.txt`
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt`
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt`
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt`
- **CHEUNG** — CHEUNG
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/CHEUNG.txt`
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt`
- **

... [9709 characters truncated] ...

le.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`

## English / Romance / Germanic

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt`
- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt`
- **WEB** — Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt`
- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt`
- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt`
- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt`
- **RCH** — J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt`
- **NAT** — C. Berlitz, Native Tongues, New York 1982
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NAT_2005.txt`
- **PEI** — M. Pei, The Families of Words, New York 1962
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PEI.txt`

## Turkic / Mongolian

- **TTS** — H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
- **VIE** — M.A. Sajjadiyyeh, Vazheha-ye Irani dar Zaban-e Engelisi, Bonyad-e Neyshabur 1364/1985
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_sajjadieh1364_parsianjoman.pdf`

## Sanskrit / Hindustani

- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt`
- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt`
- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt`(eval):1: ===== not found
```


## [2026-09-04T18:07:03.513Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && sed -n '/^## Iranian/,/^## English/p' SOURCE_MATRIX.md | grep -v '^  `' ; echo \"-----\"; sed -n '/^## Iranian/,/^## English/p' SOURCE_MATRIX.md | grep -E 'MON|BQT|ARY|AFM|PLA|AFA|FVQ|DKS|ISS' ; echo \"===== CHART\"; cat charts/page-31.txt",
 "description": "Read matrix middle section and chart"
}
```


### [2026-09-04T18:07:05.566Z] TOOL RESULT

```
## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
- **CHEUNG** — CHEUNG
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
- **FSF** — Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/
- **HENNING** — HENNING
- **EAV** — J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869
- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
- **AHM** — I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
- **TLM** — H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Seri
- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
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
-----
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ISS_alt_DKS.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt`
- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt`
- **PLA** — A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt`
- **AFA** — S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
===== CHART
=== PDF page 31 (book page 1) ===
--- entry 0 ---
ROOT [Indo-European] Ab 1, Ap 1 : water  (refs POK:1)  PART 1
#1 (parent #0) [Avestan / Pahlavi] refs=KLN:2 | âp : water
  #2 (parent #1) [Pahlavi] refs=BQT:1,49; IRN:119; AEF:10 | âp-tab : a (hot) glittering object, sun ☞Tep ; zâ-âp : spring, river ☞Ud 1,Ôus 2 ; ô-pât-ân : place of protected water ways: (modern city of Abadan in Iran) ☞Pa ; av-xur : animal shelter for drinking and eating ☞Swel
    #3 (parent #2) [Persian] refs=AHD; BQT:1225; IRN:108; MON:1763 | âb «آب ۱» : water ; zahâb «زهاب ( زاب )» : spring, river | extra: آبان ، آبادان ، گلاب ، آبشار ، آسیاب ، آخور ، آخُر
      #4 (parent #3) [English] refs=AHD | julep ☞Wrdho
#5 (parent #0) [Persian] refs=PLA:22 | âbnîk «آبنیک» : good (distilled) water ☞Nei 1
  #6 (parent #5) [Arabic] refs=WEB:44; PLA:27 | al-anbîq, al-ambîq : distilling apparatus | NOTE: Some references derive this from Greek "ambix: distill cup".
    #7 (parent #6) [Persian] refs=MON:362 | anbîq «انبیق» : still
    #8 (parent #6) [Spanish] refs=KLN:47 | alambique
      #9 (parent #8) [French] refs=KLN:47 | alambic : still | NOTE: Could be through Latin "alambicum".
        #10 (parent #9) [English] refs=KLN:47 | alembic : still
#11 (parent #0) [Pahlavi] refs=FVQ:46; ISS:3 | âp-rex : a water container for pouring ☞Leigh 2 ; na-âp : no water, undiluted (wine), pure ☞Ne 1
  #12 (parent #11) [Persian] refs=ISS:3 | âbrîz «آبریز» : urn ; nâb «ناب» : pure
  #13 (parent #11) [Arabic] refs=None | 
    #14 (parent #13) [Persian] refs=FVQ:46 | ebrîq «إبریق» : a water container
#15 (parent #0) [Sanskrit] refs=AHD | punj-ab : a region in India crossed by five rivers ☞Penkwe
  #16 (parent #15) [English] refs=None | Punjab
```


## [2026-09-04T18:07:12.102Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/page-31.json; echo; echo ====; python3 -c \"\nimport json;d=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'));\nfor k in ['POK','KLN','BQT','IRN','AEF','AHD','MON','PLA','WEB','FVQ','ISS','HRN','HUB','CHEUNG','ARY','AFM','AFA','LKT','WLD','IEC','SYN','PHD','NYB','BRT','SKT','FSD','PHN','DEV','LAM','DOZ','SOD','HJB','AID','KNT']:\n  v=d.get(k); print(k, json.dumps(v, ensure_ascii=False)[:600] if v else None)\"; echo ====; sed -n 1,80p tools/verify_check.py",
 "description": "Read existing verification file, refs table, and checker"
}
```


### [2026-09-04T18:07:13.719Z] TOOL RESULT

```
Exit code 1
{
  "pdf_page": 31,
  "book_page": 1,
  "verified_by": "claude-fable-5-1",
  "verified_on": "2026-09-04",
  "entries": [
    {
      "entry": 0,
      "root": "Ab 1, Ap 1",
      "verdict": "confirmed",
      "modern_form": "PIE *h₂ep- 'water, body of water; river' (Pokorny 2. ap- 51, with the by-form ab- 1); Proto-Indo-Iranian *Hā́ps > Proto-Iranian *Hā́fš",
      "note": "Pokorny IEW p.1 has 'ab- Wasser, Fluß' (Lat. amnis, OIr. ab, Welsh afon) and refers to '2. ap- Wasser, Fluß' on p.51 (Skt. ap-, Av. āfš/āpəm, Hitt. ḫap(a)-, Toch. āp); Nourai's double heading 'Ab 1, Ap 1' merely combines the two Pokorny lemmas, which modern scholarship (Wiktionary after Wodtko-Irslinger-Schneider NIL, Rastorgueva-Edelman ESIJa I 312) treats as variants of one root *h₂ep-/*h₂eb-. AHD/Watkins: 'ap-2 Water, river. Iranian ap- in Persian ab, water: JULEP [Pok. 2. ap- 51]'. Root, language label and gloss are correct. Weak points on this page are the four sub-derivations in node 2 (āftāb, ābādān, āxwarr are NOT from āb 'water' in modern etymology), the whole ābnīk > al-anbīq > alembic branch (nodes 5-6; every modern source derives anbīq from Greek ámbix, as Nourai's own NOTE half-admits), and the 'Sanskrit' label on Punjab (node 15), which is a Persian coinage.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ep-",
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hā́fš",
        "https://en.wiktionary.org/wiki/آب"
      ],
      "ref_check": [
        {"ref": "POK:1", "status": "supports", "note": "POK_01.txt line 19 (IEW p.1): 'ab- Wasser, Fluß. Lat. amnis ... air. ab ... cymr. afon ... Vgl. auch 2. ap- Wasser, Fluß und abō(n) Affe'. The Iranian forms are under 2. ap- p.51 (English edition POK_full.txt: 'Root ap-2 (*hap-2) water, river ... Old Indic ap- f. water ... Avestan Nom. Sg. āfš, Akk. Sg. āpəm'). Pokorny is still the standard reference for this root."}
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan / Pahlavi",
          "words": "âp",
          "verdict": "confirmed",
          "derivation": "Avestan āp- f. 'water' (nom. sg. āfš, acc. āpəm, gen. pl. apąm, cf. the month-name Ābān 'of the waters'), Old Persian ap- (loc. sg. apiyā in DSf) both continue Proto-Iranian *Hā́fš < PIIr. *Hā́ps < PIE *h₂ep- (Skt. āp-, pl. āpaḥ; Hitt. ḫap(a)- 'river'; Lat. amnis < *abnis). In Middle Persian the word is āp/āb (Book Pahlavi ʾp, Manichaean ʾb; MacKenzie 'ab ... water'), the intervocalic/final -p- lenited to -b (spirant β) in the Sasanian period. The label 'Avestan / Pahlavi' correctly collapses the Old-Iranian and Middle-Persian stages.",
          "sources": [
            "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hā́fš",
            "https://en.wiktionary.org/wiki/آب"
          ],
          "ref_check": [
            {"ref": "KLN:2", "status": "supports", "note": "KLN_1966.txt line 1142 (p.2, s.v. abdest): 'Pers. āb, water, is rel. to Avestic āp-, OI. āpaḥ (fem. pl.), water; see amnic and cp. the first element in abkari and the second element in doab and in julep.'"}
          ]
        },
        {
          "id": 2,
          "lang": "Pahlavi",
          "words": "âp-tab; zâ-âp; ô-pât-ân; av-xur",
          "verdict": "disputed",
          "derivation": "Only one of the four compounds really contains āp 'water'. (a) âp-tab = MP āftāb 'sunshine, sun' (Pahlavi ʾptʾb; NP āftāb): modern etymology (Cheung 2007 s.v. tap; Wiktionary) derives it from Proto-Iranian *abi-tāpah 'shining upon', i.e. the preverb abi- (> MP af-/āf-) + tāp- 'to shine, be hot'; Horn (Grundriss no. 3) likewise separated an āb 'Glanz' (cf. Skt. ābhā-) from āb 'water'. Nourai's gloss 'a (hot) glittering object' shows he is forcing āb 'water/lustre' into the compound; the water-root is not involved. (b) zâ-âp = MP zahābag (MacKenzie: 'zahabag [zhʾpk, NP zahāb] spring, source') = *zah 'spring, depth' + āb + suffix -ag; this one is genuinely āb 'water' and gives NP zahāb/zāb. (c) ô-pât-ân = ābādān: as a common noun MP ābādān 'thriving, populous' is ā-pāta- 'protected, cultivated' (root pā- 'protect', Nourai's own ☞Pa) + -ān, with no water element; as the city name, medieval Arabic ʿAbbādān (Balādhurī: founded by ʿAbbād of Tamīm; Ptolemy/Marcian Apphadana/Apphana) was officially respelled Ābādān in 1935, and the 'āb + pā(d) coast-guard station' reading is a modern proposal by B. Farahvashi (= Nourai's IRN), not a demonstrated etymology. (d) av-xur = MP āxwarr 'manger, stable' (Pahlavi ʾhwl; NP āxor/āxur, Arm. axoṙ): MacKenzie and Wiktionary derive it from ā- + xwar- 'eat' (Proto-Iranian *hwar-), literally 'eating-place'; the first element is the preverb ā-, not āb 'water', so the 'drinking' sense is a folk etymology.",
          "sources": [
            "https://en.wiktionary.org/wiki/آفتاب",
            "https://en.wiktionary.org/wiki/آخور",
            "https://en.wiktionary.org/wiki/آبادان",
            "https://en.wikipedia.org/wik

... [13571 characters truncated] ...

ense 'without water' → 'unwatered (wine)' → 'pure' is the same development as Greek ákratos.",
          "sources": [
            "https://en.wiktionary.org/wiki/ناب",
            "https://vajehyab.com/?q=آبریز"
          ],
          "ref_check": [
            {"ref": "ISS:3", "status": "not_checked", "note": "Indo-Scythian Studies not available; substitute DKS text has no nāb/ābrēz entry. Horn HRN.txt line 8831 'nāb rein, ungemischt; aw. anāp- ohne Wasser; phlv. anāp' supports the derivation."}
          ]
        },
        {
          "id": 13,
          "lang": "Arabic",
          "words": "",
          "verdict": "confirmed",
          "derivation": "Pass-through node for Arabic إِبْرِيق ibrīq (pl. abārīq) 'ewer, water-jug', a pre-Islamic loan from Middle Persian/Parthian *ābrēk/*ābrēz (possibly via Syriac ʾaḇrēqā): attested in the Qur'ān (56:18, abārīq) and in the pre-Islamic poets ʿAdī b. Zayd, ʿAlqama and al-Aʿshā, i.e. borrowed among the Arabs of al-Ḥīra in contact with the Sasanian court; Persian ē was shortened to i and the Iranian z/k rendered by q (Jeffery pp.46-47; Cheung 2017).",
          "sources": [
            "https://en.wiktionary.org/wiki/إبريق"
          ],
          "ref_check": [
            {"ref": "FVQ:46", "status": "supports", "note": "Node carries no refs; FVQ_pages.txt ff-page 64 (Jeffery p.46): 'A ewer, or water jug ... It was early recognized as a Persian loan-word (Siddiqi, 13), and is given by al-Kindī, Risāla, 85; ath-Thaʿālibī, Fiqh, 317; as-Suyūṭī and al-Jawālīqī in their lists of Persian borrowings ... The word occurs in the early poetry ... doubtless an early borrowing among the Arabs who were in contact with the court at al-Ḥīra.'"}
          ]
        },
        {
          "id": 14,
          "lang": "Persian",
          "words": "ebrîq",
          "verdict": "confirmed",
          "derivation": "NP ابریق ibrīq/ebrīq 'water-jug, ewer' is a round-trip loan: Persian āb-rēz → Arabic ibrīq → back into Persian in the Arabic form (Mo'in: 'ابریق [معرّب آبریز]'; Jeffery p.47 note 7: 'ibrīq also occurs in Pers. but only as a borrowing from Arabic'; Wiktionary: 'borrowed from Arabic إِبْرِيق'). The Arabic-shaped word (initial i-, -q) co-exists with native ābrīz.",
          "sources": [
            "https://en.wiktionary.org/wiki/ابریق",
            "https://en.wiktionary.org/wiki/إبريق"
          ],
          "ref_check": [
            {"ref": "FVQ:46", "status": "supports", "note": "FVQ_pages.txt ff-page 64-65 (Jeffery p.46-47): 'In modern Persian the word is [ابریق] meaning urn or waterpot ... [ibrīq] also occurs in Pers. but only as a borrowing from Arabic.' Mo'in MON_part1.txt line 6264: 'ابریق: [معر. آبریز] (ا.) ظرف سفالین آب ...' agrees."}
          ]
        },
        {
          "id": 15,
          "lang": "Sanskrit",
          "words": "punj-ab",
          "verdict": "disputed",
          "derivation": "The name Panjāb/Punjab is a Persian compound پنج panj 'five' (☞Penkwe) + آب āb 'water, river', 'the five rivers' (Jhelum, Chenab, Ravi, Beas, Sutlej); it was coined in the Perso-Islamic period (in use by the Mughal era; earlier writers such as Ibn Baṭṭūṭa use Panj-āb for the Indus confluence) as a calque of the Sanskrit name पञ्चनद Pañcanada (pañca + nada 'river'; Vedic Sapta-sindhu). Sanskrit āp- 'water' is a genuine cognate of Persian āb, but there is no Sanskrit *pañc-āp; the language label 'Sanskrit' is wrong and the word belongs under the Persian branch. The transliteration 'punj' reflects the Anglo-Indian spelling with u.",
          "sources": [
            "https://en.wiktionary.org/wiki/Punjab",
            "https://en.wiktionary.org/wiki/پنجاب",
            "https://www.etymonline.com/word/Punjab"
          ],
          "ref_check": [
            {"ref": "AHD", "status": "not_found", "note": "AHD_watkins1985.txt: the ap-2 entry (line 282) lists only JULEP; no PUNJAB under ap-2 or in the index. The 1975 AHD main-dictionary entry (not on disk) gives Punjab as Persian panj + āb, which would contradict the Sanskrit label."}
          ]
        },
        {
          "id": 16,
          "lang": "English",
          "words": "Punjab",
          "verdict": "confirmed",
          "derivation": "English Punjab (17th-18th c. Anglo-Indian spelling, earlier Panjab) is taken from Punjabi/Hindustani Pañjāb, itself the Persian پنجاب panjāb 'five waters' used by the Delhi Sultanate and Mughal administration; the u spelling reflects the Hindustani short a heard as [ʌ]. Etymonline: 'from Hindi Panjab, from Persian panj five + ab water'. The English word is correct; only the parent's language label (node 15) is wrong.",
          "sources": [
            "https://www.etymonline.com/word/Punjab",
            "https://en.wiktionary.org/wiki/Punjab"
          ],
          "ref_check": [
            {"ref": "none", "status": "not_checked", "note": "Node carries no refs; Etymonline and Wiktionary used instead."}
          ]
        }
      ]
    }
  ]
}

(eval):1: === not found
```


## [2026-09-04T18:07:18.717Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nd=json.load(open('data/verification/page-31.json'))\nfor n in d['entries'][0]['nodes']:\n    print('###', n['id'], n['lang'], n['words'], n['verdict'])\n    print(n['derivation'][:900])\n    for r in n['ref_check']: print('  RC', r['ref'], r['status'], '|', r['note'][:400])\n    print('  SRC', n['sources'])\n    print('  consulted' in n, n.get('consulted'))\nEOF",
 "description": "Print all nodes of the verification file compactly"
}
```


### [2026-09-04T18:07:20.560Z] TOOL RESULT

```
### 1 Avestan / Pahlavi âp confirmed
Avestan āp- f. 'water' (nom. sg. āfš, acc. āpəm, gen. pl. apąm, cf. the month-name Ābān 'of the waters'), Old Persian ap- (loc. sg. apiyā in DSf) both continue Proto-Iranian *Hā́fš < PIIr. *Hā́ps < PIE *h₂ep- (Skt. āp-, pl. āpaḥ; Hitt. ḫap(a)- 'river'; Lat. amnis < *abnis). In Middle Persian the word is āp/āb (Book Pahlavi ʾp, Manichaean ʾb; MacKenzie 'ab ... water'), the intervocalic/final -p- lenited to -b (spirant β) in the Sasanian period. The label 'Avestan / Pahlavi' correctly collapses the Old-Iranian and Middle-Persian stages.
  RC KLN:2 supports | KLN_1966.txt line 1142 (p.2, s.v. abdest): 'Pers. āb, water, is rel. to Avestic āp-, OI. āpaḥ (fem. pl.), water; see amnic and cp. the first element in abkari and the second element in doab and in julep.'
  SRC ['https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hā́fš', 'https://en.wiktionary.org/wiki/آب']
False None
### 2 Pahlavi âp-tab; zâ-âp; ô-pât-ân; av-xur disputed
Only one of the four compounds really contains āp 'water'. (a) âp-tab = MP āftāb 'sunshine, sun' (Pahlavi ʾptʾb; NP āftāb): modern etymology (Cheung 2007 s.v. tap; Wiktionary) derives it from Proto-Iranian *abi-tāpah 'shining upon', i.e. the preverb abi- (> MP af-/āf-) + tāp- 'to shine, be hot'; Horn (Grundriss no. 3) likewise separated an āb 'Glanz' (cf. Skt. ābhā-) from āb 'water'. Nourai's gloss 'a (hot) glittering object' shows he is forcing āb 'water/lustre' into the compound; the water-root is not involved. (b) zâ-âp = MP zahābag (MacKenzie: 'zahabag [zhʾpk, NP zahāb] spring, source') = *zah 'spring, depth' + āb + suffix -ag; this one is genuinely āb 'water' and gives NP zahāb/zāb. (c) ô-pât-ân = ābādān: as a common noun MP ābādān 'thriving, populous' is ā-pāta- 'protected, cultivated' (root pā- 'protect', Nourai's own ☞Pa) + -ān, with no water element; as the city name, medieval A
  RC BQT:1,49 not_found | BQT_v1_pages.txt: the آب entries are at OCR lines ~5860-5875 ('آب ... که یکی ازجملهٔ چهار عنصر باشد') and آفتاب at line 8232 ('آفتاب ... بروزن ماهتاب'), but the Persian OCR of Mo'in's etymological footnotes on these pages is too garbled to read the Pahlavi forms; could not confirm what p.49 says.
  RC IRN:119 not_checked | Farahvashi, Iranvij — no online copy; but Wikipedia (Abadan, Iran) reports exactly this etymology as 'B. Farahvashi proposed derivation from Persian ab (water) + pā (guard, watch), i.e. coastguard station', so the reference presumably says what the arrow says; it is a hypothesis not adopted by Iranica.
  RC AEF:10 not_checked | Khaleqi Motlaq, Asās-e Eshteqāq-e Fārsi — no online copy.
  RC PHD contradicts | MacKenzie (PHD_mackenzie.txt line 658 'ab [MYA ...] water'; 5730 'zahabag [zhʾpk, N zahāb] spring, source'; 12387 axwarr) — supports zahāb, but lists āxwarr and ābād(ān) 'populous, thriving, prosperous' as separate lemmas, not compounds of ab. (Not cited by Nourai for this node; checked as the modern standard.)
  SRC ['https://en.wiktionary.org/wiki/آفتاب', 'https://en.wiktionary.org/wiki/آخور', 'https://en.wiktionary.org/wiki/آبادان', 'https://en.wikipedia.org/wiki/Abadan,_Iran', 'https://en.wiktionary.org/wiki/زه']
False None
### 3 Persian âb; zahâb confirmed
NP āb 'water' is the direct continuation of MP āb/āp (< OP ap-, Av. āp-); the MP final spirant β became NP b. zahāb (also zāb, and the river-name Zāb) 'spring, seepage water' continues MP zahābag 'spring, source' (MacKenzie), i.e. zah 'spring, depth' (Wiktionary زه, Etymology 3: 'from Middle Persian *zah, attested in zahābag') + āb; the MP suffix -ag was dropped as usual in NP. Mo'in defines zahāb as 'a seepage point near a spring or watercourse where thin streams of water emerge'. Of the extra words: ābān (month, Av. apąm 'of the waters'), gulāb, ābšār, āsyāb (MacKenzie asyab '(water-)mill') are genuine āb-compounds; ābādān and āxor/āxur are not (see node 2).
  RC AHD supports | AHD_watkins1985.txt line 282: 'ap-2. Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.]'
  RC BQT:1225 not_found | BQT_v2_pages.txt line 1274 shows a garbled 'زهاب ) ... ساب طبری' fragment in the زهاب region, but the OCR is unreadable; could not verify the footnote.
  RC IRN:108 not_checked | no online copy of Farahvashi, Iranvij.
  RC MON:1763 partial | MON_part2.txt: the زهاب headword itself is not recoverable in the OCR (only uses inside other entries, e.g. line 8910 'کشتی که زهاب آب‌های کشتی در آن جمع'); vajehyab's Mo'in entry confirms the meaning 'seepage near a spring' but gives no etymology.
  SRC ['https://en.wiktionary.org/wiki/آب', 'https://vajehyab.com/?q=زهاب', 'https://en.wiktionary.org/wiki/زه']
False None
### 4 English julep confirmed
English julep (late 14th c., 'syrupy drink in which medicine is given') < Old French julep < Medieval Latin julapium < Arabic julāb < Persian gulāb 'rose-water' = gul 'rose' (Nourai's ☞Wrdho, OIr. *wr̥da-) + āb 'water'. Arabic replaced the non-Arabic g by j and Latin/Romance supplied the -ep/-apium ending; the 'mint julep' sense is American, 1761. The chart's direct Persian → English arrow skips the Arabic, Latin and French intermediaries but the ultimate source is right (AHD, Klein, Etymonline all agree).
  RC AHD supports | AHD_watkins1985.txt line 282 'ap-2 ... Persian ab, water: JULEP' and line 1174 'Zero-grade form *wrd- in Iranian *wrd in Persian gul, rose: JULEP'; index line 1707 'JULEP ap-2, wrod-'. Klein p.2 s.v. abdest and p.836 s.v. julep ('fr. Pers. gulāb, rose water, julep, compounded of gul, rose, and āb, water') agree.
  SRC ['https://www.etymonline.com/word/julep', 'https://en.wiktionary.org/wiki/گلاب']
False None
### 5 Persian âbnîk disputed
Nourai analyses the Arabic al-anbīq 'still' as a Persian compound āb 'water' + nīk 'good' (☞Nei 1), i.e. 'good (distilled) water', following Asbaghi (PLA). No Persian dictionary knows āb-nīk as a common noun: vajehyab returns only Dehkhoda's 'آب نیک: نام قریه‌ای از رودبار در ایالت طهران' (a village name), and Mo'in labels انبیق itself '[غ. معر.]' = Greek, arabicized. All modern etymological sources (Klein, Etymonline, Wiktionary, Beekes) derive Arabic إنبيق from Greek ἄμβιξ 'spouted cup, cap of a still' (Syriac ʾambīqā as intermediary); the initial a-/in- of anbīq/inbīq reflects Greek am-/Syriac am- with nasal dissimilation, not Persian āb. The 'âbnîk' etymon is therefore a folk-etymological back-formation and the node should be rejected.
  RC PLA:22 not_checked | Asbaghi, Persische Lehnwörter im Arabischen — no online copy. Mo'in (MON_part1.txt line 17169) contradicts: 'انبیق: [غ. معر.] (ا.) ظرفی است برای تقطیر مایعات و گرفتن عصاره و عرق' — marked as Greek, arabicized.
  SRC ['https://vajehyab.com/?q=آبنیک', 'https://en.wiktionary.org/wiki/إنبيق', 'https://en.wiktionary.org/wiki/ἄμβιξ']
False None
### 6 Arabic al-anbîq, al-ambîq disputed
Arabic إِنْبِيق inbīq / أَنْبِيق anbīq (with article al-anbīq) 'distilling apparatus' is a borrowing of Greek ἄμβιξ (gen. ἄμβικος) 'spouted cup; cap of a still', a word already used by the Alexandrian alchemists (Zosimus, 3rd-4th c.); it reached Arabic through the Syriac alchemical/medical translations (Syriac ܐܡܒܝܩܐ ʾambīqā) in the 8th-9th c. Greek -mb- was rendered -nb-, hence the two Arabic spellings anbīq/ambīq that Nourai lists. Nourai's own NOTE ('Some references derive this from Greek ambix') is in fact the unanimous modern view (Klein, Webster's, Etymonline, Wiktionary, Mo'in); the Greek word itself is of unknown, possibly Pre-Greek/substrate or Semitic origin (Beekes). Webster's and Etymonline allow that the word passed 'via Persian' between Greek and Arabic, but even so the Persian stage would be a loan of ambix, not a compound with āb.
  RC WEB:44 contradicts | WEB_vol1.txt line 5377 (Webster's New 20th C., s.v. alembic): 'a-lem/bic, n. [L. alambicus; Ar. alanbiq; al, the, and anbiq, Per. ambiq, a still; Gr. ambix, a cup of a still.]' — Persian is only a transit stage; the source is Greek ambix.
  RC PLA:27 not_checked | Asbaghi — no online copy.
  SRC ['https://en.wiktionary.org/wiki/إنبيق', 'https://en.wiktionary.org/wiki/ἄμβιξ', 'https://www.etymonline.com/word/alembic']
False None
### 7 Persian anbîq confirmed
NP انبیق anbīq 'still, retort' is a loan of Arabic anbīq/inbīq, taken over with the Arabic alchemical vocabulary in the early Islamic centuries (Mo'in marks it معرّب, ultimately Greek). The chart's arrow Arabic → Persian is right; only the ultimate origin claimed in nodes 5-6 is wrong.
  RC MON:362 partial | MON_part1.txt line 17169: 'انبیق: [غ. معر.] (ا.) ظرفی است برای تقطیر مایعات و گرفتن عصاره و عرق' — confirms the word and that Persian took it from Arabic (معرّب), but labels the origin Greek (غ.), against Nourai's Persian âbnîk.
  SRC ['https://en.wiktionary.org/wiki/إنبيق']
False None
### 8 Spanish alambique confirmed
Old Spanish/Spanish alambique 'still' is a direct Andalusi-Arabic loan of al-anbīq, article included (as in alcohol, álgebra), with the Arabic -nb- realised as -mb-; Iberian Arabic alchemy (10th-12th c.) is the channel. Klein and Etymonline give exactly this Spanish stage; Wiktionary goes straight from Medieval Latin alembicus to Arabic. Italian lambicco is a parallel loan.
  RC KLN:47 supports | KLN_1966.txt line 2149 (p.47): 'alembic, n. — ME., fr. OF. (= F.) alambic, fr. OSp. (= Sp.) alambique fr. Arab. al-anbīq, the still, which is formed fr. al-, the, and Gk. ἄμβιξ, cup, cap of a still, alembic, which is of uncertain, possibly Semitic origin. Cp. It. lambicco'.
  SRC ['https://www.etymonline.com/word/alembic', 'https://en.wiktionary.org/wiki/alembic']
False None
### 9 French alambic confirmed
Old French alambic (13th c.) 'still' is taken either from Old Spanish alambique (Klein, Etymonline) or from Medieval Latin alembicus/alambicum, itself the Latinisation of Arabic al-anbīq used in the 12th-c. alchemical translations (Wiktionary). Nourai's NOTE 'could be through Latin alambicum' is the alternative that Wiktionary prefers; both routes exist side by side and are compatible with the chart.
  RC KLN:47 supports | KLN_1966.txt line 2149: 'fr. OF. (= F.) alambic, fr. OSp. (= Sp.) alambique' — French from Spanish as drawn.
  SRC ['https://www.etymonline.com/word/alembic', 'https://en.wiktionary.org/wiki/alembic']
False None
### 10 English alembic confirmed
Middle English alembic (late 14th c.; aphetic limbeck already mid-14th c., common in the 15th-17th c.) is borrowed from Old French alambic; the -e- of the English form reflects the Medieval Latin spelling alembicus. Meaning 'still' since the alchemists, figurative 'anything that refines' from the 16th c.
  RC KLN:47 supports | KLN_1966.txt line 2149: 'alembic, n. — ME., fr. OF. (= F.) alambic'; line 21755: 'limbec, n., alembic (archaic). — Aphetic for alembic.'
  SRC ['https://www.etymonline.com/word/alembic', 'https://en.wiktionary.org/wiki/alembic']
False None
### 11 Pahlavi âp-rex; na-âp plausible
Both are reconstructed rather than attested Pahlavi lemmas. âp-rex = MP *āb-rēz/*ābrēk 'water-pourer' (āb + rēz-, present stem of rēxtan 'to pour', Nourai's ☞Leigh 2 = PIE *leikʷ-); Wiktionary reconstructs 'Middle Persian or Parthian *ābrēk' as the source of Arabic ibrīq, and Jeffery (p.47) already explained the word as Pahlavi āp + rēz 'from an old Iranian root *raek = linquere'. Nourai's spelling with -x may render the Book-Pahlavi ʾplyk/ʾprēk with the older -k. na-âp = MP anāb 'undiluted, pure' (Horn no. 1015: 'nāb rein, ungemischt; aw. an-āp- ohne Wasser; phlv. anāp'), i.e. the privative prefix an-/a- (Nourai's ☞Ne 1) + āb 'water' = 'without water'; NP nāb lost the initial a- by aphaeresis. Neither compound appears as a headword in MacKenzie, hence 'plausible' rather than 'confirmed'.
  RC FVQ:46 supports | FVQ_pages.txt ff-page 64-65 (Jeffery pp.46-47, s.v. ibrīq): 'It would be derived from [āb] water (= Phlv. āp, i.e. OPers. āpi = Av. āp ... ), and [rīz] to pour (= Phlv. rēc from an old Iranian root *raek = linquere) ... It was from the Phlv. form that the word was borrowed into Arabic, the shortening of the ī being regular.'
  RC ISS:3 not_checked | Bailey, Indo-Scythian Studies (Khotanese Texts VI) is not on disk; the substitute Bailey Dictionary of Khotan Saka (ISS_alt_DKS.txt) was grepped for anāb/nāb/ābrēz without a hit. Horn HRN.txt line 8831 (no. 1015) supplies the same derivation: 'nāb rein, ungemischt. aw. anāp- ohne Wasser; phlv. anāp'.
  SRC ['https://en.wiktionary.org/wiki/إبريق', 'https://en.wiktionary.org/wiki/ناب']
False None
### 12 Persian âbrîz; nâb confirmed
NP ābrīz 'ewer, urn; sink, latrine' is a transparent compound āb + rīz (present stem of rīxtan 'pour'; MP rēz-, with NP ē > ī), Dehkhoda 'دلو' and 'متوضا، مبال'. NP nāb 'pure, undiluted, unalloyed' continues MP anāb (an- privative + āb) with loss of the unstressed initial a- (Horn no. 1015; Wiktionary 'from Middle Persian *anāb'); the sense 'without water' → 'unwatered (wine)' → 'pure' is the same development as Greek ákratos.
  RC ISS:3 not_checked | Indo-Scythian Studies not available; substitute DKS text has no nāb/ābrēz entry. Horn HRN.txt line 8831 'nāb rein, ungemischt; aw. anāp- ohne Wasser; phlv. anāp' supports the derivation.
  SRC ['https://en.wiktionary.org/wiki/ناب', 'https://vajehyab.com/?q=آبریز']
False None
### 13 Arabic  confirmed
Pass-through node for Arabic إِبْرِيق ibrīq (pl. abārīq) 'ewer, water-jug', a pre-Islamic loan from Middle Persian/Parthian *ābrēk/*ābrēz (possibly via Syriac ʾaḇrēqā): attested in the Qur'ān (56:18, abārīq) and in the pre-Islamic poets ʿAdī b. Zayd, ʿAlqama and al-Aʿshā, i.e. borrowed among the Arabs of al-Ḥīra in contact with the Sasanian court; Persian ē was shortened to i and the Iranian z/k rendered by q (Jeffery pp.46-47; Cheung 2017).
  RC FVQ:46 supports | Node carries no refs; FVQ_pages.txt ff-page 64 (Jeffery p.46): 'A ewer, or water jug ... It was early recognized as a Persian loan-word (Siddiqi, 13), and is given by al-Kindī, Risāla, 85; ath-Thaʿālibī, Fiqh, 317; as-Suyūṭī and al-Jawālīqī in their lists of Persian borrowings ... The word occurs in the early poetry ... doubtless an early borrowing among the Arabs who were in contact with the cour
  SRC ['https://en.wiktionary.org/wiki/إبريق']
False None
### 14 Persian ebrîq confirmed
NP ابریق ibrīq/ebrīq 'water-jug, ewer' is a round-trip loan: Persian āb-rēz → Arabic ibrīq → back into Persian in the Arabic form (Mo'in: 'ابریق [معرّب آبریز]'; Jeffery p.47 note 7: 'ibrīq also occurs in Pers. but only as a borrowing from Arabic'; Wiktionary: 'borrowed from Arabic إِبْرِيق'). The Arabic-shaped word (initial i-, -q) co-exists with native ābrīz.
  RC FVQ:46 supports | FVQ_pages.txt ff-page 64-65 (Jeffery p.46-47): 'In modern Persian the word is [ابریق] meaning urn or waterpot ... [ibrīq] also occurs in Pers. but only as a borrowing from Arabic.' Mo'in MON_part1.txt line 6264: 'ابریق: [معر. آبریز] (ا.) ظرف سفالین آب ...' agrees.
  SRC ['https://en.wiktionary.org/wiki/ابریق', 'https://en.wiktionary.org/wiki/إبريق']
False None
### 15 Sanskrit punj-ab disputed
The name Panjāb/Punjab is a Persian compound پنج panj 'five' (☞Penkwe) + آب āb 'water, river', 'the five rivers' (Jhelum, Chenab, Ravi, Beas, Sutlej); it was coined in the Perso-Islamic period (in use by the Mughal era; earlier writers such as Ibn Baṭṭūṭa use Panj-āb for the Indus confluence) as a calque of the Sanskrit name पञ्चनद Pañcanada (pañca + nada 'river'; Vedic Sapta-sindhu). Sanskrit āp- 'water' is a genuine cognate of Persian āb, but there is no Sanskrit *pañc-āp; the language label 'Sanskrit' is wrong and the word belongs under the Persian branch. The transliteration 'punj' reflects the Anglo-Indian spelling with u.
  RC AHD not_found | AHD_watkins1985.txt: the ap-2 entry (line 282) lists only JULEP; no PUNJAB under ap-2 or in the index. The 1975 AHD main-dictionary entry (not on disk) gives Punjab as Persian panj + āb, which would contradict the Sanskrit label.
  SRC ['https://en.wiktionary.org/wiki/Punjab', 'https://en.wiktionary.org/wiki/پنجاب', 'https://www.etymonline.com/word/Punjab']
False None
### 16 English Punjab confirmed
English Punjab (17th-18th c. Anglo-Indian spelling, earlier Panjab) is taken from Punjabi/Hindustani Pañjāb, itself the Persian پنجاب panjāb 'five waters' used by the Delhi Sultanate and Mughal administration; the u spelling reflects the Hindustani short a heard as [ʌ]. Etymonline: 'from Hindi Panjab, from Persian panj five + ab water'. The English word is correct; only the parent's language label (node 15) is wrong.
  RC none not_checked | Node carries no refs; Etymonline and Wiktionary used instead.
  SRC ['https://www.etymonline.com/word/Punjab', 'https://en.wiktionary.org/wiki/Punjab']
False None
```


## [2026-09-04T18:07:29.332Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'));\nfor k in ['BQT','IRN','AEF','PLA','ISS','WLD','ARY','MON','AFM','AFA','LKT','HRN','HUB','NYB','PHD','IEC','SYN','SKT','FSD','WEB','PHN','DEV','LAM','DOZ','HJB','AID','BRT','KNT','CHEUNG','SOD','TTS','LEW','LAT','FVQ','KLN','AHD','POK']:\n  v=d.get(k); print('##',k, json.dumps(v, ensure_ascii=False)[:700] if v else None)\"; echo ====; cat tools/verify_check.py | head -150; ls data/verification/sources/refs/ | head -80; ls data/verification/sources/refs/incoming/",
 "description": "Read refs table entries, checker script, and list local books"
}
```


### [2026-09-04T18:07:31.136Z] TOOL RESULT

```
Exit code 1
## BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
## IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf", "/home/sfmqrb/git/rishe/data/verific
## AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, ver
## PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
## ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "local_file": null, "page_offset": "DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file ha
## WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
## ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
## MON {"title": "Mohammad Mo'in

... [15479 characters truncated] ...

de q={word}   (get s
## TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": "TTS_pages.txt: 253 leaves; printed page N = leaf N+30.", "lookup_hint": "Not searched exhaustively 
## LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
## LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
## FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 
## KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
## AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
## POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
(eval):4: === not found
```


## [2026-09-04T18:07:40.618Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'));\nfor k in ['BQT','IRN','ISS','MON','ARY','AFM','HRN','HUB','NYB','PHD','WLD','IEC','SYN']:\n  v=d.get(k); print('##',k, 'page_offset=', v.get('page_offset'), '| hint=', (v.get('lookup_hint') or '')[:500], '| local=', v.get('local_file'))\"; echo; echo '--- checker'; sed -n 1,200p tools/verify_check.py",
 "description": "Read refs page offsets and the checker script"
}
```


### [2026-09-04T18:07:42.491Z] TOOL RESULT

```
## BQT page_offset= vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint= grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf imag | local= ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
## IRN page_offset= 222 leaves; printed page = PDF page − 11 (PDF 101 = p.90; chapter openers carry no numeral). 6th printing 1382, same setting as 1368. | hint= archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor) | local= ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt']
## ISS page_offset= DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint= Khotanese Texts VI itself is not online. Nourai's ISS page numbers cannot be checked directly; the Dictionary of Khotan Saka (headword at line start, Khotanese in transliteration, with 'Pok.' refs) covers the same etymological material and can verify the substance of a claim. | local= None
## MON page_offset= None | hint= Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Aden | local= ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
## ARY page_offset= printed page = pdf page + 1 | hint= Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image | local= ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt']
## AFM page_offset= 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | hint= Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير'). | local= ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt']
## HRN page_offset= leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint= Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann. | local= /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
## HUB page_offset= leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint= Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number. | local= /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
## NYB page_offset= Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint= Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs. | local= /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt
## PHD page_offset= leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint= Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB). | local= /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt
## WLD page_offset= Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | hint= Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP. | local= ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt']
## IEC page_offset= TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint= Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root. | local= /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
## SYN page_offset= leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint= Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line. | local= /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt

--- checker
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


## [2026-09-04T18:07:51.211Z] AGENT

Now I'll grep the books. First batch: IE books (POK, WLD, AHD, IEC, SYN) plus Old/Middle Iranian (BRT, KNT, PHD, NYB) for the root and nodes 1, 2, 11.


## [2026-09-04T18:07:56.944Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; \necho '--- POK ab-'; grep -n -m3 -E '^ *ab- ' POK_01.txt; grep -n -m5 -E '^ *2\\. ap-|^2\\. ap-' POK_01.txt POK_full.txt;\necho '--- WLD Bd1 ab-/ap-'; grep -n -E '^ *(1\\. |2\\. )?ab- |^ *ap- ' incoming/WLD/WLD_Bd1_pages.txt | head; grep -n -i -E 'āp-.*Wasser|ap- .*Wasser' incoming/WLD/WLD_Bd1_pages.txt | head -5;\necho '--- WLD band3 index'; grep -n -E 'ap-|āp' WLD_band3.txt | grep -i -E 'aw\\.|ai\\.|np\\.' | head -5;\necho '--- AHD'; grep -n -E 'ap-2|JULEP|PUNJAB|Punjab' AHD_watkins1985.txt | head;\necho '--- IEC'; grep -n -E '^ *ap-|^ *āp-|^ *ab-' IEC.txt | head; \necho '--- SYN water'; grep -n -E '1\\.31 WATER|1\\.36 RIVER' SYN.txt | head; ",
 "description": "Grep IE books for ap-/ab- root"
}
```


### [2026-09-04T18:07:57.094Z] TOOL RESULT

```
--- POK ab-
19:ab-  ^Wasser;,  Fluß^.
--- WLD Bd1 ab-/ap-
4256:2.   ap- „Wasser, FluB“.
--- WLD band3 index
--- AHD
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
814:fana, flag, banner, weathercock: VANE; b. compound *gund-fanon-, “battle-flag” (see ghen-'). 2. Extended form *panno- in Latin pannus, piece of cloth, rag: PANE, PANEL. 3. Possibly Greek pénos, web (> Latin pdnus, a swelling): PANICLE. [Pok. pan- 788.] [pandoura. Three-stringed lute. Greek noun of obscure origin. BANDORE, MANDOLIN, PANDORE.] pant-. All. Attested only in Tocharian and Greek. Greek pas (neuter pan, stem pant-), all: PAN-, PAN; DIAPASON, PANCRATIUM, PANCREAS. [In Pok. 1. keu- 592.] pap-'. Teat (sound symbolism). Probably the same word as pap-2. 1. Middle English pap(pje, nipple: Pap}. 2. Latin diminutive papula, pimple (diminutive papilla, nipple): PAPILLA, PAPULE. 3. Variant form *pup(p)- in Latin piipus, boy, and pupa, girl: puPA, PUPIL. [In Pok. barb- 91.] pap-?. Food (baby-talk root). Reduplication of pa-. 1. Germanic nasalized form *pamp- in Flemish frequen- tative pamperen, to cram with food, akin to the source of Middle English pamperen, to pamper: PAMPER. 2. Latin pappa, food (> Middle English pap, soft food): PAP?, POPPYCOCK. [Pok. pap(p)a 789, ba*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by marriage. Latin parri- (for pari-) in compound parri-cida (oldest form paricidas), murderer of a near relation: PARRICIDE. [Pok. pdso-s 787.] past-. Solid, firm. 1. Germanic *fastuz, firm, fast, in: a. Old English fest, fixed, firm: FAST!; STEADFAST; b. Middle Dutch vast, firm, fast: AvAST. 2. Germanic *fastinon, to make firm or fast, in Old English festnian, to fasten, establish: FASTEN. 3. Germanic *fastén, to hold fast, observe abstinence, in: a. Old English festan, to abstain from food: rasT?; b. Old Norse fasta, to abstain from food: BREAKFAST. [Pok. pasto- 789.] pau-. Few, little. I. Adjectival form *pau-, few, little. 1. Germanic *fawaz in Old English féawe, few: FEW. 2. Suffixed form *pau-ko- in Latin paucus, little, few: PAUCITY, POCO. 3. Suffixed form *pau-ro- in metathetical form *par-wo- in Latin parvus, little, small, neuter parvum, becoming parum, little, rarely: PARAFFIN, PAR- vovirus. 4. Compound “pau-paros, producing little, poor (*par-os, producing; see pere-'), in Latin pauper, poor: PAUPER, POOR, POVERTY. II. Suffixed reduced variant form “pu-lo-, young of an animal. 1. Germanic *fulén- in Old English fola, young horse, colt: FOAL. 2. Germanic derivative *fuljé in Old Norse fylja, female colt: FILLY. 3. Latin pullus (probably with expressive gemination), young of an animal, chicken: POLTROON, PONY, POOL?, POULARD, PULLET; CATCHPOLE. III. Basic form *pau- and variant form *pi-, boy, child. 1. Suffixed form *pu-ero- in Latin puer, child: PUERILE, PUERPERAL. 2. Suffixed form “pi-sso- in Latin piisus, boy: PUSIL- LANIMOUS. 3. Suffixed form *paw-id- in Greek pais (stem paid-), child (> paideia, education): PEDO-?; ENCY- CLOPEDIA, ORTHOPEDICS. [Pok. pdu- 842.] paus-. To leave, desert, cease, stop. Greek pauein, to stop (> Latin pausa, a stopping): PAUSE, (PESADE), (POSE!); COMPOSE, DIAPAUSE, (REPOSE!). [Pok. paus- 79.] ped-'. Foot. I. Nominal root. 1. Lengthened o-grade form *pod- in Germanic *fot- in Old English fot, foot: Foor. 2. Suffixed form *ped-ero- in Germanic *feteré in Old English fetor, feter, leg iron, fetter: FETTER. 3. Suffixed form *ped-el- in Germanic *fetel- in Old High German vizzelach, fetlock, akin to the Germanic source of Middle English fitlock, fetlock, fetlock: FETLOCK. 4. Basic form *ped- in Latin pés (stem ped-), foot: PAWN2, -PED, PEDAL, PEDATE, PEDESTRIAN, PEDI-, PEDICEL, PEDUNCLE, (PEON), PES, PIONEER; MILLIPEDE, SESQUIPEDALIAN, TRIPEDAL, TRIVET, VAMP!. 5, Form *ped-yo- in: a. Latin expedire, to free from a snare (ex-, out of; see eghs): EXPEDITE; b. Latin impedire, “to put in fetters, hobble,
1174:ROSE}, 3. Zero-grade form *wrd- in Iranian *wrd in Persian gul, rose: JULEP.]
1707:JOY gau- JUBILATE yu-2 JUDGE deik-, yewes- JUDICIAL deik- JUGATE yeug- JUGGERNAUT gWa- JUGGLE yek- JUGGLER yek- JUGULAR yeug- JUGUM yeug- JUICE yeue- JULEP ap-2, wrod- JuLY deiw- JUNCTION yeug- JUNCTURE yeug- JUNIOR yeu- JUNKER kei-2, yeu- JUNTA yeug- JUPITER deiw- JURAL yewes- JURIDICAL deik-, yewes- JURISCONSULT yewes- JURISDICTION deik-, yewes- JURISPRUDENCE yewes- JURIST yewes- JURY! yewes- JUSSIVE yeudh- susTl yewes- JusTiFy dhé-1
2044:PAMPER pap-2
2052:PAP? pap-2
2119:POPE papa POPLAR p(y)el- POPPLE? p(y)el- POPPYCOCK kakka-, pap-2 POPULACE populus POPULAR populus POPULATE populus PORCELAIN porko- PORCH per-2 PORCINE porko- PORCUPINE porko-, spei- PORE? per-2
--- IEC
622:ap-, radical of āpnu-, āpos, aptos, q.v.
623:ap-aĝð, see apo, ag0 Skt. apåjami; Arm. v-azem “dash, trespass, pass away, spill; Gk. apágo; Lat. ab-igo; Ir. f-ágaim ‘quit
624:ap-anó (apana, apono) cf. apo, ana (ono) Av. apano “distant; distance’; Gk. cf. epano (epi, ano); OHG (aphetic) fona, fana “from
17804:ap-
--- SYN water
1220:1.31 WATER
1374:1.36 RIVER; STREAM; BROOK
```


## [2026-09-04T18:08:05.341Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; \necho '--- POK_01 p.51 2. ap-'; grep -n -E 'ap-.*Wasser|āp-|āfš|Wasser, Fluß' POK_01.txt | head -8; \necho '--- POK_full ap-2'; grep -n -i -E 'Root ap-2|āfš' POK_full.txt | head -5;\necho '--- WLD Bd1 around 4256'; awk 'NR>=4250 && NR<=4275' incoming/WLD/WLD_Bd1_pages.txt; grep -n -c $'\\f' incoming/WLD/WLD_Bd1_pages.txt; awk 'BEGIN{RS=\"\\f\"} /2\\.   ap- /{print \"LEAF\", NR; exit}' incoming/WLD/WLD_Bd1_pages.txt; grep -n '^ *ab- ' incoming/WLD/WLD_Bd1_pages.txt | head -3;\necho '--- IEC ap-'; awk 'NR>=17800 && NR<=17815' IEC.txt;\necho '--- SYN water'; awk 'NR>=1220 && NR<=1262' SYN.txt | grep -n -i -E 'ap|Av\\.|Skt\\.|NPers|Pers' | head -12",
 "description": "Read POK p.51, WLD Bd1 ap-, IEC, Buck WATER"
}
```


### [2026-09-04T18:08:07.224Z] TOOL RESULT

```
--- POK_01 p.51 2. ap-
4602:ai.  mpa-  ,tiefliegend'  (ni-\-ap-  ,Wasser');
--- POK_full ap-2
--- WLD Bd1 around 4256
artiger Aufsatz auf der Priestermutze“, welches Wort       von den Alten, aber
auch von Vanieek 15,         Thurneysen Thes. „fortasse“ zu *apio gezogen wird.
Vgl. Yf. LEWb. 2 50.             Stokes erklart nicht iiberzeugend               ir.    Cm „Hand“ als
„die Ergreiferin“ aus *ap-s-men (Fick II 4 16 u. BB. 23, 60).


2.   ap- „Wasser, FluB“.
           „Wasser“, z. B. n. a. sgl. dpah, apdh, g. pi. ap&m , av. n. sg. afi,
     Ai. dp-
a. sg. apam, i. sg. apa(-ca), ai. apavant- „wasserig“, in alter Kontraktion
der Red.-St. mit auf -i, -u ausl. Praefixen (Kretschmer KZ. 31, 385, Jo-
hansson IF. 4, 137 f.) pratlpd- „gegen den Strom gerichtet“, mpd- „tief-
liegend“, aniipa- „am Wasser gelegen“, dvlpa- „Insel, Sandbank im Flusse“,
antarlpa „Insel“; dieselbe Kontraktion mit einem auf -o endigenden 1. Glied
                             3
in  den gr. FluBnamen Ivamog ’Aoconog ( :7v6a> doig; Fick BB. 22, 61, 62);
                                         ,                       ,



gr. AtiUi Bezeichnung des Peloponnes, Meaa-dma ds., die lokr. Msaa-amoi
                                                                                                       ,

die illyr. Megooitiioi und Apuli Unteritaliens, die FluBnamen AmScor (Ar-
kadienj, Amdarog (Thessalien), illyr. ’Ayog, Apsus; apr. ape „FluB“, apus
„Quell, Brunnen“, lit. itpe, lett. upe „Wasser“ (bsl. A ist Red.-St. von idg.
887
LEAF 55
--- IEC ap-
sük- “juice, sap, resin, whey, liquor Lat. sücus & succus, gs. 1 m. “juice, sap, strength’; cf. sücinum ‘amber’; Latv. cf. sücu, Sükt, v. ‘suck, sup’; sūkalas, fpl. ‘whey’; Li. cf. (w. infix) sunka, f. ‘juice, sap’. (WH irrelevant and untenable)
su-Klutos "of good report Skt. su-$rüt “hearing well’; sú-śrutih, f. ‘good hearing’; Av. cf. husravo, -åh- (‘famous. Hence Chosroes); Arm. h-lu ‘obedient’; Olr. so-chlúd, m. ‘fame’; Ir. so-chla, adj. ‘famous’; W hy-glod, id. (and “praiseworthy')
sul- (sulio, suliio) ‘sole, base’. Cf. suol-. (Not to sol- (1)) Gk. hulía, f. ‘sole of foot: Go. sulja, f. “sole of foot, base’; OE syll, f. “sill, threshold, base'. Cf. WP II, 532. (NB. Lat. solea, if not from a type *sueliio, is a hybridism w. type sol- in solum)
sul- (1) (sulo, io, aio) “issue, put forth’. Cf. WP IL, 505 & 513 & sulis, os Arm. cf. h-yem, v. ((send', fr. Sen Lat. cf. ex-sulo, åre, v. “be banished’; OW cf. de- hol, v. ‘banish’? beside (*-ü- in) hilio, inf. ‘yield, produce’; OSC süljo & Sljo, inf: sülati, freq: sylati, v. ‘send’; R po-sylat', freq. inf. wd:
ap-
süghó — sulu- (suluio)
Lë
15
20
25
30
35
40
45
1334
cf. R po-sòl, Cz. po-sel, m. (“'envoy': Lat. ex-sul 'exile")
--- SYN water
2:Grk.  bdwp Goth. wats Lith. vanduo NG vepd ON vain Lett. adens Lat. aqua Dan. vand ChSl.  voda It. acqua Sw. vatten SCr.  voda Fr. eau OE weler Boh.  voda Sp. agua ME water Pol. _voda am apd aa water Russ. voda
3:usce u water Skt. jala-, Gp-, udan- put ae cee wazzar ; Abie ate :
12:The words for ‘water’, with few ex- belong to certain widespread nates, one of these reflect- ing what was clearly the general IE word for ‘water’, and three others also reflecting I words for ‘water’ , but per- haps in some more special application, such as ‘running water’ or ‘rain water’. Many words belonging to these groups appear in other lists, as under ‘sea’, “vave’, ‘river’, ‘rain’.
13:1. IE *wedor, *wodor, *uden-, a typi- cal r/n stem neuter, with gradation of the root syllable, fr. root *wed- in Skt. ud- ‘wet, flow’. Some forms with nasal in root syllable (intrusion from verb forms with nasal infix, or anticipation of n of stem). Walde-P. 1.252 ff. Er- nout-M. 1124.
14:Grk. téwp; Umbr. utur (Lat. unda ‘wave’); Ir. usce, NIr. uisce (Gael. wesge- beatha ‘water of life’ > NE whiskey); the Gme. group, Goth. waté, OF weter, etc.; Lith. vanduo, Lett. uidens, OPruss. wundan, unds; ChSl. voda, ete. general Slavic; Skt. wdan-; Hitt. watar, gen. we- tenas; Alb. wé.
16:3. IK *a@p-. Walde-P. 1.46. Skt. dp-, ap- mostly pl. dpas, used esp. of the per-
18:sonified ‘Waters’, Av. ap-, ap- the reg. word for ‘water’, also freq. personified, OPers. api-, NPers. ab ‘water’. Else- where only of ‘running water’ in words for ‘river’, as Lith. upé, Lat. amnis, Ir. abann, etc. (1.46).
19:4, IB *wer-. Walde-P. 1.268f. Skt. var-, vari, ‘water’ (of all kinds), Toch. A war, B war ‘water’. Elsewhere in words for ‘rain water, rain’, as Av. var-, ON ar (1.75), or for ‘sea’ or ‘lake’, as Av. vairi-, Lith. jurés, etc. (1.32, 1.33). Also Grk. obpov, Lat. wrina ‘urine’ (cf. NE make water).
21:NG vepé fr. veapov (tdwp) ‘fresh water’, through vypdv (cf. Phrynichus vypdv dep ui) elrgs), with regular change of ir to er (Hatzidakis, Mec. 2.598).
23:Skt. jala-, the commonest word for ‘water’ : gal- ‘drip’, NHG quelle ‘spring’, etc. Walde-P. 1.690 ff.
24:Skt. ambhas- and ambu- : Grk. duBpos, Lat. imber ‘rainstorm’, Skt. abhra-
30:GAs, 74 Goth. marei Lith. jira (mares) i ee ieee ON haf, ser (marr) Lett. jira NG Oédacca, téAayos Dan. hav (s4) ChSl. morje Lat. mare (aequor, etc.) Sw. hav (sjé) SCr. more It. mare OE s@ (mere, haf) Boh. moje Fr. mer ME _ see Pol. morze Sp. mar NE sea Russ. more Rum. mare Du. zee Skt. sdgara-, samudra-, Tr. muir, fairrge, ler OHG mari, séo etc. NIr.  fatrrge, muir, lear MHG mer, sé Av. zrayah-, OPers. W. mor NHG meer, see (fem.) drayah- Br. mor
```


## [2026-09-04T18:08:28.093Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; \necho '--- POK_01 near 4602'; awk 'NR>=4585 && NR<=4612' POK_01.txt; awk 'BEGIN{RS=\"\\f\"} /ni-\\\\+ap-/{print \"LEAF\", NR-1; exit}' POK_01.txt;\necho '--- POK_full'; grep -n -E 'Root ap-2|Root ab-|hap-2' POK_full.txt | head;\necho '--- BRT ap-'; grep -n -E '^ *[0-9]*\\.? *ap- |^ap-|āp- f\\.|^ *āp- ' BRT.txt | head -8; grep -n -i -E 'anāp|an-āp|Wasser.*āp' BRT.txt | head -6;\necho '--- KNT'; grep -n -E '^ *api-|^ *ap-|apiyā|ap- .*water' KNT.txt | head -8",
 "description": "POK p.51 text, Bartholomae ap-, Kent api-"
}
```


### [2026-09-04T18:08:29.887Z] TOOL RESULT

```
--- POK_01 near 4602
air
aus  O/tC.        *Ä*-*     ''"'»VC''«'    CliUO      Lllil..     «'#l<«'-«JQ#€.L*      ^  J.  I^^XXÜV?!.      )        V  ^1  IXiCllg  li      JJJ.1  b      t-ZtCfc-    z^s    (y»»l|
ande-,  s.  Thumeysen  Grammar  531  f.,  Pedersen  KG.  I  45),  acjmr.  abret in  ,m^j  com.  bret.  en,  ncymr.  yn-j  gall.   essedon  (*en-sedon)  ^Streitwao-A  t embrekton  ^eingetauchter  Bissen^  (s.  unter  mereq-)-,  *
got.  in  ,\n',  adnom.  m.  Dat.,  Akk.,  Gen.;  ahd.  as.  ags.  in,  anord.  %  {^t adnom.  m.  Dat.  und  Akk.,  aus  *em  (über  Ableitungen  wie  got.  {7,' ,hinein^,  inna^  innana,  wohl  aus  *eni-n-,  s.  Brugmann  IF.  33,  304 f.)-
apr.  en  ,in',  adnom.  m.  Dat.  und  Akk.,  lett.  ie-  (nur  Präfix);  tiefstufi^ ^T}  in  lit.  f  (älter  und  heute  dial.  in,  int)  ,in^,  adnom.  m.  Lok.  und  Akk  •
aksl.  on-  {on-uUa  ,Schuhwerk^,  q-doh  ,Tal^),  schwundstuf,  v^n',  v^  in< adnom.  m.  Lok.  und  Akk. ;
toch.  AB  y-,  yn-j  B  in-  (nur  Präfix).
n-dhi:  ai.  ddhi  ,über,  auP,  apers.  adiy  ,in';  gall.  Intensivpräfix  Andi> (PN  Ände-roudus  ,der  sehr  rote^),  cymr.  an{ne)-  in  anne-l  ,Vorrichtunc^ =  air.  2«cZe-Z  {*ndhi-l-om),  cymr.  an-daw  ,lauschen^  (zu  taw  ,schweigend')* air.  ind-  (teils  aus  *indi-j  teils  aus  sekundärem  *indo-)  in  ind-reth  ,Eia- fall'  (*indi-reto-),  indnaide  (s.  weiter  unten),  usw.  Pedersen  (KG.  I  45)' will  auch  got.  und  ,bis  zu'  hierher  stellen;  s.  über  andere  Möglichkeiten  ' oben  S.  50  und  S.  181.  >^
(e)nero-  ,innerlich':  arm.  *nero-  ,das  Innere',  vorausgesetzt  von  ner- ,intra,  hinein',  nerJts  ,innen',  nerkoy  , drinnen';  vielleicht  gr.  bvsqol  als  ,die drinnen',  nämlich  in  der  Erde;  oder  besser  Hypostase  aus  o\  iy  egc^?
ni-,  nei'  ,nieder',  Komparativ  nitero-  ,nieder'  (im  Gegensatz  zu  ,oberer'):
ai.  ni,  av.  nl  ,nieder(wärts)',  ai.  nitardm  ,unterwärts',  av.  nitdma-  ,der
unterste';
arm.  ni-,  n-  ,nieder';  ;!fj
kelt.  *ne  aus  *nei  in  air.  ar-neut-saj  in-neut-sa  ,ich  erwarte',  (urir. *-ne-sedu)j  Yerbaln.  indn{a)ide  (*indo-ne-sodion)  und  in  ar-neigdet  ,sie beten'  (*ari-ne-gedont)]  vgl.  anders  Bergin  Eriu  10,  111;
ahd.  nidar,  as.  nithar,  ags.  nipei',  aisl.  nidr  ,niederwärts',  ahd.  nidana^ as.  nithana  ,unten',  ags.  neodan,  nipan  ,herunter,  unter',  aisl.  nedana  ,von unten  her',  Präp.  mit  Akk.  ,unterhalb',  as.  nithe  Adv.  ,unten',  ahd.  nida Präp.  mit  Dat.  und  Akk.  ,unterhalb,  unter';
abg.  niz^  ,hinab,  hinunter'  (Bildung  wie  prä-zi,  usw.);
im  Kompositum:  *
ai.  mpa-  ,tiefliegend'  (ni-\-ap-  ,Wasser');
*ni'oJcu-  als  ,die  Augen  niederhaltend'  in:
ai.  nlcä  ,abwärts'  (vgl.  nyanc-  ,nach  unten  gerichtet');
^^«
313
abg.  nicb  .pronus',  poniknqti,  nicati  ,pronum  esse,;  Wackernao-el-De- brunuer  Ai.  Gr.  III  230  f.,  Trautmann  198  f.  "^
mit  Formans  -uo-:
^v.  veLÖg  f.  ;Feld,  Flur^  (,*NiederungO.  veiaTog,  veacoq  ,der  unterste', vBLodxv  ,von  unten',  veiod-L  ,unterhalb',  vEiaiqa  yaarriQ  ,der  untere  Teil  des Bauches',  vr^iaxa'  ecxara,  xcrwrara  Hes.,  theb.  NrjLTzai  Ttvlai  (rj  scheint für  e  aus  ei  vor  pal.  Vokal  zu  stehen);
abg.  niva  , Acker'  (,*Niederung'),  skr.  7ijwa  (woher  das  J?),  öech.  russ. niva   ds.  {*neiuä  f.);
schwundstufig  ags.  neowol,  neol,  nlhol  ,pronus'  aus  *niwol,  mnd.  nigel ,niedrig';
hierher  wohl  auch  mit  Vollstufe  lit.  neivoti  ,quälen',  lett.  nievdt  ,ver- ächtlich  behandeln,  schmähen,  niederdrücken'  (auch  got.  *naüü  ivsTysv^ Marc.  VI  19?).
--- POK_full
9203:Root / lemma: ap-2{*hap-2) 
9209:Root/ lemma: ap-2 {* hap-2)\ " water, river ' derived from Root/ lemma: ab-{*h2^'"-): " 
--- BRT ap-
3477:71  ap-  3
7276:ap-  Noten
--- KNT
1531:*ap- ‘water’ in inst. pl. abi$, *üp- in nom. dpi, loc. apryd.
2224:"$88. Tue Srems IN Stops, 1ч OP: these in- elude stems ending in £ (napdf- ‘prandson’), nf (*tunvant- ‘strong’), d (éard- ‘year’, pad- ‘foot, rād- ‘cause’), p (xSap- ‘night’, ap- ‘water’ cf. épi-) k (vif- ‘house’, vas- ‘will’).
```


## [2026-09-04T18:08:50.385Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; \necho '--- POK_01 leaf 59-60 ap-'; awk 'BEGIN{RS=\"\\f\"} NR==60' POK_01.txt | grep -n -i -E 'ap-|afs|Wasser' | head -8;\necho '--- POK_full 9203-9230'; sed -n 9203,9232p POK_full.txt | cut -c1-300;\necho '--- BRT'; grep -n -E \"ap- .*Wasser|äp- .*Wasser|āp- .*Wasser|'Wasser' *\\(?āp|^ *āp- |^ *ap- f\" BRT.txt | head -8; grep -n -i -E 'an-?āp-|anäp|anap- ' BRT.txt | head -5;\necho '--- KNT 1525-1535'; sed -n 1528,1533p KNT.txt | cut -c1-400;\necho '--- PHD'; grep -n -E '^(ab|āb|zahabag|aftab|āftāb|abadan|ābādān|axwarr|āxwarr|anab|anāb|abrez|ābrēz|asyab|gulab|abriz|abad) ' PHD_mackenzie.txt | head -14;\necho '--- NYB'; grep -n -E '^(āp|ap|āpātān|āftāp|āptāp|zahāp|anāp|āxwarr|āxwar|āpāt|āpādān)\\b' NYB_vol2_glossary.txt | head -14;\necho '--- HRN'; grep -n -E '^ *(1|3|1015)\\. |ābādān|āxur|āxwur|zahāb|gulāb|gul-āb|ābrīz|anbīq|zāb ' HRN.txt | head -20;\necho '--- HUB'; grep -n -E '^ *(1|3|1015)\\. |āftāb|ābād|āxur|nāb|gulāb' HUB.txt | head -14;\necho '--- CHEUNG'; grep -n -E '^\\*(tap|raič|hwar|raiz)|āftāb|ābrēz|ābrīz|nāb|ābād' CHEUNG.txt | head -14",
 "description": "Grep Iranian books for ap and its compounds"
}
```


### [2026-09-04T18:08:52.180Z] TOOL RESULT

```
--- POK_01 leaf 59-60 ap-
5:hitt.  e-ip-mi  (epmi)  ,nehme^,  3.  PI.  ap-pa-an-zi  (^apanzi).
8:2.  äp-  ,Wasser,  Fluß^
9:Ai.  up-  f.  ,Wassere,  z.  B.  PI.  Nom.  äpah^  Akk.  apdh,  Gen.  apäm,  av. Nom.  Sg.  äfs,  Akk.  Sg.  äpdm,  Instr.  Sg.  apa(-ca)j  ai.  dpavant-  ,wässerige, in  alter  Kontraktion  der  Red.-St.  mit  auf  -i,  -u  ausl.  Präfixen  (Kretschmer KZ.  31,  385,  Johansson  IF.  4,  137  f.)  pratlpd-  .gegen  den  Strom  gerichtet^, nipd-  ,tiefliegende,  anüpd-  ,am  Wasser  gelegen^,  dvipd-  ,Insel,  Sandbank im  Flusse^,  antarlpa-  ,Insek;  dieselbe  Kontraktion  mit  einem  auf  -o  en- digenden 1.  Glied  in  den  gr.  Flußnamen  ''IvwTtog,  l^acarvög  {:  höco,  ^Gig] Fick  BB.  22,  61,  62);  gr.  l^rcia  ,Peloponnese,  Meao-ania  ds.,  die  lokr. MeGO-(X7tL0Ly  die  ill.  MsaGafCLOi  (anders  Krabe  ZONF.  13,  20  f.)  und  Apuli Unteritaliens,  die  Flußnamen  ^Arciddiv  (Arkadien),  ''u4rtidav6g  (Thessalien), thrak.  ^'Ajtog  (Dacien),  ill.  ""^xpog,  Apsus,  apul.  ON  Sal-apia  (,Salzwasser'^);
13:apa-J^ umen^  wie  die  Erft  (^Arnapia),  und  alle  FIN  mit  -up-,  wie  nhd.  I C/ppia-Bach  (Tirol)^  frz.  Sinope  (Manche)^  brit.  Hafen  Rutupiae,  sizil. KaKVTtaQLg  (vgl.  lit.  Kakwpis),  vgl.  die  thrak.  YY^'^Yniog,  '^'Ynavig;  apr. ape  ;Fluß^,  apus  ^Quell^  Brunnen^,  lit.  üpe,  lett.  upe  ^Wasser^  {u  ist  vielleicht Red. -St.  von  idg.  o,  a,  Trautmann  Bsl.  Wb.  11;  o
--- POK_full 9203-9230
Root / lemma: ap-2{*hap-2) 

Meaning: water, river 

Note: 

Root/ lemma: ap-2 {* hap-2)\ " water, river ' derived from Root/ lemma: ab-{*h2^'"-): " 

water, river ' < Root/ lemma: abofn) {* h2abd-): " ape, *water demon ' < Root/ lemma: ab^- 

(*/7i'ab*^-): " quicl<, abrupt ' < Root/ lemma: ^^ro-{*h2^^ro-): " strong, mighty ' < root /pb^- 

{ro-)\ < with Aformant {n^^el§)\ < Root/ lemma: {eneb'"-2)\ neb'"-, errt'"-, /pb^-: " wet, 

damp; water; clouds '. 

Material: 

Hittite: hap{a)- ' river ', Pal. hapnas, Luvian hapinni- (Tischler 159-160) 

Tokharian: A, B ap 'water, river' (Adams 44) 

Old Indie ap- f. 'water', e.g. PI. Norn, apah, Akk. apah. Gen. apam, Avestan Nom. Sg. afs, 

Akk. Sg. apsm, Instr. Sg. apa(-ca). Old Indie apavant-^\Na{evj\ in older eontraetion with 

reduplieation-stem in -/; -^auslaut prefixes (Kretsehmer KZ. 31, 385, Johansson IF. 4, 137 

f.) pratTpa-^ directed against the stream ', nlpa-^ low lying, deep-recumbent ', anupa-^ 

--- BRT
8465:•  j.  uniyäp-  Adj.  'des  Wasser  sich  weit- hin erstreckt':  zrayaahs  vourukasahe  .  . ja/rahe  'iipaAt''>  \t.8.^6.
8494:•  j,  urv-äp-  Adj.  'des  Wasser  sich  weit ausdehnt,  mit  weiter  Wasserfläche' '' :  ainö.- /aya>um  . .  yahmya  jafra  varayö  °apat>hd (NPm.)'>  hisl-itie\i.io.  14;  —  *pasne  varöis *äu^aitahe  jafrahe  'spahe'^  YL  V49.
11883:•  j.  tadLäp-  i)  'ßiessendes  Wasser":  yat alte  (sd.)  ysi  mazdayasna  ..  'apaya  (LS.)" nasaum  frajasqrt  V.<?,  26.  i)  Adj.  (auch fem.)  'mit  fiiessendem  Wasser':  vat^lm (sd.)  'apam  (A.SQ'i  V.  14.12.
11905:•  j.  tatäp-  Adj.  'fallende  Wasser  habend', sva.  'der  den  Regen  fallen  lässt':  sata- %ais5  .  .  'äpa  (NS.)">  zavarm.srats  'äfS (NS.)''  ux^at.urvarS  Yt.  7^,44;  43"';  — tnihrsm  .  .  frat.ap)m  zavanlS.srBt>m  •ap?m uxryat.urvar»n  Yt  10. 6 1  "*,
17652:•  j.  frat-äp-  Adj.  'die  Wasser,  Gewässer füllend':  mi^rvm  .  .  'Spam  savans.srBttm tat.Hp3m  uxyat.urvanm  Yi.I0.6i,
4927:Et-?  —  Pü.:  anäpitän,  erl.{?J;  ahramati. Baitiuildui,  Aliinu.  Wb.
7049:•  j.  'äi  Praen.  mit  Akk.  'hin  zu  — "':  yat vä  anäßpm  (sd.)  3i  sp^m  kirftiaoiti  yat  vä apfin  ai  anäp^in  kinnaeiti  V-5.4.
10138:—  tistryS ..vaz»mnö  -Jus  k)hrpa  zaranyS.-  bagä  x^ar^mnif  (sd.)  Y. 32. 8;  —  "Su/x'ar»- srvahe  YLÄ16;  i4-l,  Y.ig.yi.  A)  Das  \%ahe  nr^yJ  V.7.  43; — 'Sul  vä  s^var3%ahe Rind  gilt  als  Repräsentant  aller  nützlichen  j  (sd.)  vä  W.14.1T,  —  '!us  i^ar/itinqm {ahumohtn)  Tiere,  daher  ^gav-  auch  inJH, /.  5;  —  yasca  ..  lanumazs {^A.)  'Jui weiterem  Sinn  gebraucht  wird*"':  para\da%at  "W-iS.!!);  —  °amla  ifsst)m  anäp»m •Su^  ca^war).paitistanaya  dänheit  para\{%d.)  V.5,  52;  S3f.',  7.55;  —  buiri 'aas  ,  . nars  asaotiB  bipaittstänahe  zq%st  Y.  /p.  8 ;  j  3far>^a  . .  VyL  4:5.  3)  'Milch',  bes.  zur
11982:Wbst   SBE,  j/,  62    "(by   a  Tanäpükar   sin)   a
11985:KompE.  —  'pirAia-  n.  'Verwirkung',  lum  V. ^•OT'.  —  PiLi  lanäpuhrSi,  erl.i  mark  ariän; ».•).  —  ')  Unthem.?  Ebenso  N.  .j*  2.  ^t. Wohl  -la  M  lesen.  —  ')  Hds.  "i.a.  —  S)  Laut- lich (ül)  von  aaäpuArai  beeinflusst.  —  i)  S. nnter  Iraorf.  No.  8.
--- KNT 1525-1535
*gthen- in ajanam ‘I smote’, *g*hn- in jadiy ‘do thou smite’, -jata ‘slain’.
*dher- or *dhr- in adarsty Ч held’; *dhr- in duruva- ‘firm’; (Ar.) *dàr- in dárayatiy ‘he holds’.
*g¥em- ‘come’ in -jamiy ‘may it come’, *g*m- in pardgmata ‘gone forth’ (see $244).
*ap- ‘water’ in inst. pl. abi$, *üp- in nom. dpi, loc. apryd.
*bhag- in baga ‘god’, *bhàg- in bàji- ‘tribute’.
*7"02- in guzddm ‘cattle’ (oi proved by the lack of palatalization of the g), *g*i- in jiva ‘living’.
--- PHD
658:ab [MYA < A my);)ft I M )b, N .....] water.                    'b S'u~ "r'"
1261:asyab ['sy'p] (water-)mill.
5730:zahabag [zh)pk I N zahdb] spring, source.
12387:axwarr                             \\"'0'     axwan
--- NYB
466:ap- [’p-] as a rule used together with an encl. pers. pron.: pm: api-m, "pt: api-t,
467:ap-
471:ap-
473:ap [MY”; ’p' 607. 787. 862.6, 878-11] water 1416-26 and passim; pl. cas. obl. āpān Dp?n'] 1095. — Av. (325 sqq.) āp-, OP āpt-; MPrthPrs ’b; Paz. āw, àv; NP ab. - V. dp-cthrak, āp-sārān, āpīk.
476:apäc [L'WEIL ; ’p’c] 1. adv. back, back- ward (opp. frāc 25?-*), again: hac 7-salak ~ for seven years 16?5; hac én and (q.v.) sal ~ 1674; — prev. with vbs. of motion, e. g. dmatan, šutan, vastan, ete., and many others, e.g. guftan, gumeatan, etc. — 2. prep. with (= apäk) 42%. — 1. < *apācā instr. adv. from Olr adj. *apdnk-, weak st. apük- and apác, derived from Av. (72) apa, OP apa, cf Skr apdfic- ‘situated be- hind’; MPrth °b’c; Paz. awāž; NP baz. — 2. < *upācā, instr. adv. from Olr adj. *wpünk- derived from Av. (388 sq.) upa, OP upä ‘under, with’; J-Prs ?b?z ‘with’ (common); v. further apäk.
479:apāc-kartakēh [L°>WHL ‘BYDWN-tkyh] the state of having been taken to pieces,
481:apāc-sārēh [—-s'lyh] rebellion 13%. — Paz.
486:apäkönitän
497:apākēh [’p’kyh] 1. company; pat ~ together 5712, — 2. backward movement: pat ~ back 418; v. pat-apākēnītan. — 3. help, assistance 5919-20, 729-26 (opp. ha- mēstārēh). — V. lapāk and ?apäk. Paz. āvāgī. V. also apar-apākēh.
498:apäkenitan [—-ynytn'] to make a p., or a th., one's helper, or companion, or help: hakar vēnākēh apakéné [-yd] (if thou wilt make Clear Vision thy helper
502:apäk-puhr
503:apäk-puhr [LWTH pwhl] he who has a son 22%. - Cf the NP compounds with bà: bā-āb ‘having water’ and the like.
516:apārīk [’p’ryk; Prs inser. ’p’lyk] other l. attribute, placed before its subst., passim; seldom inflected in pl. before a subst. in pl. cas. obl.: hac ~-dn giyākān u röstäkän 8617-18, — 2. independent: ~ other people 5026-27; han i evak ... the one ... and the other 1093; ēvak-ē ... u ~ one... and another 12115; ~ har cé all other things that ... 862. 10411, 1211; u ~ and others (z who) 10812; ‘ete.’ 11015. 12119; u ~-dn ‘et ceteri’ 11017; sak u dalman tdi <... except for dogs ... and vultures, (all the) other (animals) 9421-22, — MPrthPrs bryg (S, A-H II); apär- < *upārda < Olr upa- + *arda- ‘side’ (v. ärak): ‘standing by a p.s side, placed at the side of a th.’ = ‘his, its counterpart’ (HP II, 14); cf apärön. Paz. aware, which must be another w.: < *awarrég < *apar- rek < *upari-raika- ‘left over, remainder’ (from reztan, g. v.)?
521:apürón ['p'lwn'; Ps. *p’lwny] 1. adj. wrong 664-11, 691, etc., opp. frärön (g.v.). — 2. adv. backward (= apäc) 1281, — Paz. dwārūn, Skr. v. asadācārin (Mx); NP vārūn ‘inverted, turned upside down’; < OIr apdrda-van-, derived, by means of the suff. -van-, from *apärda- < *apa- arda- ‘whose side is turned away’ (HP II, 15). V. ärak; cf apärik and frärön.
--- HRN
451:1. ä. 1) Praefix, z. B. in ämeden^ ardi/is.
464:3. ä& *Glanz , (Sahn. I S. 14 Vers 7), vergl. ab[rö, ah[tah,
8831:1015. nä& rein, ungemischt*.
10001:1. a-, a//-, un-, nicht-' (« privativumj. Sehr häulig, z. B.
10021:3. äfräH 'Mitteilung, Belehrung (Men.).
21016:1. bSftin 219.
21027:1. 6»>-Sj. 910.
21496:3. ^«ce 545.
21500:3. <Jö i)75.
21592:1. kannä 845.
22069:1. 3fl)-(i 671.
--- HUB
384:3. p. sg. *histataiy (vgl. zd. histaiti^ skr. tisthati) oder
3539:1015. Dazu arm. LW. anapak ungemischt, rein (vom Wein).
3909:1. Z.).
4739:3. Jhd. p. Chr. stattgefunden.
5730:3. pr. gardBd etc. Shk. 246, Min. Gl. 85 neben varoism
6363:3. Jhd., Haug, Essay on Pahlavi p. 4, syr. pDDinN am
6488:3. pr. go^d, arm. gov in Jata-gov) erwartet.
6576:1. im Anlaut vor r (also pers. fr durch arm. hr) : Hraz-
6813:1. pat in patrast, patvast, patgam, patkandaran, patker
7241:1. t in gUi *Welt\ zd. ga^&ga- *irdisch' (siehe oben
7247:3. Fur Or : fr in FrSdun, siehe p. 207.
8588:1. Regelmassig: a) sag *Hund' = med. andxa, zd. spa
9804:1. Jhd. p. Chr. zu d geworden (Pauly-
--- CHEUNG
3298:*tap ‘to seize, attach, stick, strike’ 
20403:*raiz ‘to lick 
20427:*raiz3 311 
20447:*raiz? ? ‘to jump’ 
20469:*raiz? ‘to fall (out), drop’ 
24669:*tap ‘to warm up, heat’ 
24686:*tap 379 
25332:*tap ‘to twist, wind’ 
55127:*tap (s.v.), *zarH' (s.v.) 
56446:*raiz', *zgar 
56579:*raiz’ 
56938:*raiz 
57060:*raiz!
```


## [2026-09-04T18:09:29.141Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; \necho '--- HRN 451-470'; sed -n 451,470p HRN.txt | cut -c1-300; echo '--- HRN 8831'; sed -n 8829,8836p HRN.txt | cut -c1-300;\necho '--- HRN other'; grep -n -i -E 'äbäd|abad[aä]n|äxur|axur|zah[äa]b|gul[äa]b|äft[äa]b|abr[iī]z|anb[iī]q|ibr[iī]q|zäb' HRN.txt | head -20;\necho '--- HUB 3535-3542'; sed -n 3535,3542p HUB.txt | cut -c1-300; grep -n -i -E 'äft[äa]b|äb[äa]d|äxur|axur|gul[äa]b|zah[äa]b' HUB.txt | head -10;\necho '--- CHEUNG tap'; sed -n 24669,24700p CHEUNG.txt | grep -n -i -E 'āftāb|aftab|tāb|NP ' | head -8; grep -n -i -E 'rēxtan|rextan|ābrēz|abrez|^\\*raik|^\\*raič' CHEUNG.txt | head -8; grep -n -i -E 'āxwar|axwar|^\\*hwar' CHEUNG.txt | head -6",
 "description": "Read Horn, Hübschmann, Cheung entries"
}
```


### [2026-09-04T18:09:29.275Z] TOOL RESULT

```
--- HRN 451-470
1. ä. 1) Praefix, z. B. in ämeden^ ardi/is.
ap. aw. phlv. ä; ai. d,
2) Praeposition , z. B. in her ä her, gird ä gird,
aw. ai. ä,
/2^' ab, ätv *Wasser ; vergl. slm]ab (*Quecksilber, wortl.
'Silberwasser' d. i. flüssiges Silber), i^'^i^M Jer. 41, 8
(Etymologie Nüldeke's bei de Goeje, Bibliotheea geo-
— • mm
graphorum arabicorum, IV, 240), DN*:?!*! Is. 2, 9, 2^'ii^^^
Is. 36, 12, 2X^^D Jer. 31, 12 u. a. m.
ap. öp- 'Wasser ^); aw. äp-; phlv. fJp (päz. äw); ai. äp-,
kurd. äw; afy. öba (fem.); bei. ap, n. äf (12); wa;^.
ywpÄ:, ydpak, minj. ydoya; yidg. t/ow?;\
3. ä& *Glanz , (Sahn. I S. 14 Vers 7), vergl. ab[rö, ah[tah,
äb[mendy Röd]äbe, Suhr]ab^ Mihr\äb^ Ardä VTr\af, af[täb,
phlv. üb] skr. äbha- *Glanz'-).
afy. bei. LW. ab, abrü; kurd. LW. äwrü.
*) So lautet das Thema nach Bartholomae BB. 14, 244.
*) Im Arabischen bedeutet mäun auch zugleich ^Wasser' und
*Glanz', worauf mich Herr Dr. Schwally aufmerksam macht. Etwa
--- HRN 8831
1014. nä- *un-, nicht-', ne- (z. B. nespas).
aw. wa ; ai. nd.
1015. nä& rein, ungemischt*.
aw. anäp' ohne Wasser*; phlv. anap,
1016. nä%un *Nagel (am Finger oder an der Zehe)' 2).
ai. nakhä- 'Nagel, Kralle'; phlv. nä/un (Bund.),
kurd. neinuJc ^Nagel'; afy. nük; bei. näkun^ vahuft,
n. na/un (257).
--- HRN other
475:f\ [^ äbäd ^bewohnt', vergl. abadän , äwäda^i , |Nn2X Is.
5901:g. Jen (Vullers sen, Asteräbäd); Käs. K. zen, Jen,
14055:Zäbulsitän 710 Anm.
--- HUB 3535-3542
259. Daraus ist np. na, alter noch ne (vgl. nest 'ist
nicht' und nay-amad er kam nicht', Salem. Shuk.
Gram. p. 16 und 59) entstanden. Die nachdriickliche
Form nai reimt nach NSldeke auf kaL
1015. Dazu arm. LW. anapak ungemischt, rein (vom Wein).
1017. Dazu arm. LW. naz-i-m *thue stolz , briiste mich,
liebkose' (5. Jhd.). Im Phi. ist ndzuU zu lesen.
Afgh. nazuk (mit u) bei Raver ty; nazaka, nenzdka f.
--- CHEUNG tap
41054:gurextan/gurez-, 307 
41409:rextan/rez-, 187,311
```


## [2026-09-04T18:09:38.523Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; \necho '--- HRN 471-490'; sed -n 471,490p HRN.txt | cut -c1-250; grep -n -i -E 'äxwur|äxor|axor|ax[uo]r ' HRN.txt | head -5;\necho '--- CHEUNG pour / huar'; grep -n -i -E \"to pour|^\\*huar|āxwarr|axwarr|axur\" CHEUNG.txt | head -10; sed -n 24669,24690p CHEUNG.txt | cut -c1-200 | head -25",
 "description": "Horn ābād entry; Cheung pour/eat roots"
}
```


### [2026-09-04T18:09:38.617Z] TOOL RESULT

```
--- HRN 471-490
in Anlehnung an das Persische? Die Zusammenstellung von np. ab
und skr. abhä- ist keineswegs sicher; von der Bedeutung ^glitzernder)
Wasserspieger könnte man sehr leicht zu 'Glanz* kommen.
U o r n , GrundrisB d. neup. Etyiuolog-io. 1— 2 —
f\ [^ äbäd ^bewohnt', vergl. abadän , äwäda^i , |Nn2X Is.
^Va^'^ 58, 121).
ap. *äpä^a-; phlv. öpö^ (päz. dwäd), äpatth, apatan,
äpätänzhf armen. LW. apat,
5. äbisten 'schwanger, abist^ ßhiste, äbistegl, JDDiN Is.
7, 14.
mäz. äwisin,
aw. "^apu^ra-tami- 'mit dem Leibe am Kinde seiend'-);
oder vielmehr genauer *einen am Kinde seienden Leib
habend'; phlv. äptistan, äpustamh,
kurd. äfviste (Houtum-Schindler); bei. n. äfsin (13).
Daneben phlv. äptis 'schwanger , äpvsttan für aw. vereti-
vainte, verenüite, vd. 18, 32 (77); aw. aptid^ra-; kurd. äuüs,
amse (Justi-Jaba), äu4Sy ä?fvre (Houtum-Schindler);
bei. äptis, äps, afus (13).
6. abiSy^ur, abisxurdy äb/ifr (geschrieben und früher ge-
557:I 42) 'Stallmeister' (arm. LW. axorapet, a/orapan), —
--- CHEUNG pour / huar
2103:*Huar ‘to cover’, which is not mentioned in DKS: l.c. 
8853:*NWIR: ? NP saridan/sar- ‘to flow as rivers, with a great noise; to pour, trickle, urine’ 
8854:*NEIR: Oss. I. æğzælyn (yzgalyn)/zg&ld, D. egz&lun/zgzald ‘to pour down, drip’, 
8861:D. egzalun/egzald "to pour down, drop’, ? Wa. Zarz ‘milk’ || (+ *fra-) Oss. legzer, 
9045:*haié ‘to pour (out), moisten’ 
9046:*AVESTAN: Y Av. haéc- ‘to pour (out); to irrigate’ || (+ *pati-) ‘to besprinkle, pour on 
9047:(ritually with water or cow’s urine)’ || (+ *para-) ‘to pour, flow out, away’ || (+ *fra-) 
9068:*PARTHIAN: (+ *ä-) ’Syxt (pret. stem) ‘to pour, flow, overflow; sprinkle’ 
9075:*SOGDIAN: (+ *а-) MSogd. "Sync ‘to pour’ (-s- from *pati-formation) || (+ *pati-) 
9076:CSogd. pSync- ‘to pour’ 
*tap ‘to warm up, heat’ 

*AVESTAN: YAv. tap- “о be(come) hot’ || (+ *4-) ‘to warm’ || (+ *ham-) ‘to 
be(come) hot’ — Liste: 24 

Pres. inch.: INJ. 3sg. YAv. tafsat- (Y 9.11, rep.), SUBJ. 3pl. YAv. tafsan (V 3.32); Caus.: pres. IND. 3sg. 
YAv. täpaiieiti (Yt 6.1, Yt 7.4, Yt 17.20, etc.), ? YAv. "a.tapaiieiti (V 9.41); Partic.: perf. pass. YAv. 
ham.tapta- (V 4.46) 

*MIDDLE PERSIAN: MMP t’b- ‘to shine’ ?, BMP t’p- /tab-/ ‘to heat, burn (up); shine’. 
© No certain attestations in MMP, DMMPP: ibid. > DMMPP: 321a 

Pres.: IND. 3sg. BMP t’pyt /tabéd /, SUBJ. 35р. ? MMP t’b’d {rather Pth. 7}, OPT. 3sg. ? MMP ®t’byy, 
ІМРУ. 2sg. BMP t^p /tab/; Inf.: BMP t’ptn /taftan/; Partic.: perf. pass. BMP грі /tafi/; Pass.: pres. IND. 
35р. BMP t’pyhyt /tabihed/ 


*tap 379 


*PARTHIAN: t’b- ‘to shine, burn’ || (+ *abi-) *bd’b ‘sunshine’ || (+ *pati-) pt’b- ‘to 
burn into’ || (+ *ui-) wyt’b- ‘to shine’ (young formation) = Ghilain: 72 | DMMPP:
```


## [2026-09-04T18:09:58.226Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; \necho '--- CHEUNG tap cont'; sed -n 24690,24720p CHEUNG.txt | grep -n -i -E 'PERSIAN|āftāb|aftab|abi' | cut -c1-250 | head -8;\necho '--- CHEUNG rez'; grep -n -E \"NP rextan|NP rēxtan|rez- ‘to pour|rextan/rez- ‘\" CHEUNG.txt | head -5; grep -n -E \"^\\*rai[čc]\" CHEUNG.txt | head;\necho '--- CHEUNG huar'; grep -n -E \"^\\*h[uw]ar\" CHEUNG.txt | head; grep -n -i -E \"axwarr|āxwarr|axur|āxur\" CHEUNG.txt | head -5;\necho '--- HRN 490-500, 550-560'; sed -n 490,500p HRN.txt | cut -c1-200; sed -n 552,560p HRN.txt | cut -c1-200;\necho '--- PHD'; sed -n 656,660p PHD_mackenzie.txt | cut -c1-200; sed -n 12385,12390p PHD_mackenzie.txt | cut -c1-200; grep -n -E '^(aftab|abad|abadan|anab|abrez|gulab|aban|abrez|abgin|ab-)' PHD_mackenzie.txt | head -10; grep -n -E '^(aftab|abad|anab|abrez|axwarr|ab )' PHD.txt | head -8;\necho '--- NYB'; sed -n 466,475p NYB_vol2_glossary.txt | cut -c1-300; grep -n -E '^(āpāt|apāt|āpātān|āftāp|āptāp|zahāp|anāp|āxwarr|āxwar|ap-rēc|āp-)' NYB_vol2_glossary.txt | head -12",
 "description": "Cheung, Horn, MacKenzie, Nyberg entries"
}
```


### [2026-09-04T18:09:58.419Z] TOOL RESULT

```
--- CHEUNG tap cont
31:tile’, Kurd. taw ‘sun’ || (+ *abi-) NP айар ‘sun(shine)’ || (+ *ш-) Gur. (Kand.) yaw 
--- CHEUNG rez
57054:*raic, *xa(m)p/b, *zaH 
--- CHEUNG huar
10284:*huar 1 147 
10309:*huar' ‘to consume, eat’ 
10401:*huar3 149 
10404:*huar? “to sound, swear’ 
10448:*huar ‘to swear’ etymologically separate from *hyar! ‘to eat, consume’. 
10460:*huar? ‘to take’ 
10489:*huar ‘to have a sore, scratch, itch’ 
10516:*huar ‘to paint, colour; to stain’ 
56039:*huar’, *kar (s.v.), *pais 
56145:*huar! 
--- HRN 490-500, 550-560
6. abiSy^ur, abisxurdy äb/ifr (geschrieben und früher ge-
sprochen abisx'er etc.) 'Tränke* etc.^).
*) de Lagarde, Persische Studien, 70 verfährt zu künstlieh.
Ap. apadäna- (arab. LW. fadan^ das selbst wieder weithin entlehnt
ist, vergl. Miklosich) gehört nicht hierher.
2) Vergl. Geldner, KZ. 25, 193 Anm. 3.
') Die Wörterbücher Ftf und FR geben folgende Bedeutungen
der Worte und belegen dieselben sehr reichlich :
a) ^Schicksal, Loos, Antheil'.
•/^'äst^ dilem tä ki bemesjid seced
hab^^res jäuth-i mei^äne burd
1*— 4 -
8. üj^xir *Stair.
aw. avöx^'arena- *Stall, Futterplatz' ; phlv. av;(ur oder
avx^'ar (Darmesteter, Et. ir. II, 136), arm. LW. ayor,
vergl. Talmud LW. •imnx (de Lagard e, Semitica
I 42) 'Stallmeister' (arm. LW. axorapet, a/orapan), —
Anders Geldner KZ. 28, 186.
9. ä(fer *Feuer', ader,
ap. vergl. Äd^rina-, Ä&riyädiya- ; aw. äfar- 'Feuer ;
--- PHD
a- [)- I M )-] privative prefix, un-, -less.
a eJ       then (generally with a suffixed pronoun, e.g. A-i).
ab [MYA < A my);)ft I M )b, N .....] water.                    'b S'u~ "r'"
ibid ep)t l I M )b)d, N .....] populous, thriving, prosperous•
   ......ih: prosperity.
                                              iihidih                   -"-'~
ahog, ahug, xanag                 \ ~ t"O'    rrhid                          \~
axwarr                             \\"'0'     axwan
                                                                             \""' t"U'
axwarrsaHir                ~~~                axwarih                   ~~
ahomanag                \~~~                  ahang                            .,,~
665:abadyawand [)p)tyd)wnd I J )b)dywn(d)] powerless, weak.
673:aband efmd, v. pand I M )bnd] erring.
743:ab-~ihrag ['p cyhlk l ] holding the seed, essence of water.
748:ab-dan ['pd'nlJ water-holder.
809:ab-kamag ['pk'mk l I N '""'a] a thick, sour soup.
822:ab-tazan ['pten l ] watercourse.
5877:abandon abaz estadan az, histan.          action kard, kardag(an), karm,
11414:abannand               ~~Q)I           aharag, apparag'                ~~
11415:abanniinig
11434:aband                             ",va        abyoz-                -~ Vtt)'
--- NYB
ap- [’p-] as a rule used together with an encl. pers. pron.: pm: api-m, "pt: api-t,
ap-
"p: api-š, ”pm’n' or (Ps.) *pmn: api- man, ’pt’n': api-tän, "p$^n! or (Ps.) *pšn: api-ščin: 1. and, introducing and coordi- nating sentences, e.g. andar-rón andar šut api-$ guft 1818-14; coordinating substan- tives if the second subst. is determined by an encl. pron., e. g. zantšn + 
www.parsianjoman.org | ool )b
Qe
ap-
with the MPrs forms ^wm ete. v. u. Ap- was certainly obsolete in the spoken language when the Manicheans created their own literary SW language, which was not based on the usage of the Sassa- nian chancelleries. Prth preserved the encl. form -p(z), but ap- only in combi- nation with other particles:
ap [MY”; ’p' 607. 787. 862.6, 878-11] water 1416-26 and passim; pl. cas. obl. āpān Dp?n'] 1095. — Av. (325 sqq.) āp-, OP āpt-; MPrthPrs ’b; Paz. āw, àv; NP ab. - V. dp-cthrak, āp-sārān, āpīk.
apa-, api-, apč-: MIr pren. and prev. 1. MIr apa- represents both OIr apa- ‘off, away, de-, ex-’ and upa- ‘on (to), at, ad-'. — 2. api-, Olr ‘on, in, over’, replaced a) the synonymous upa- when this merged with apa, and b) (in SW) Olr abi- (Skr abhi-) which became irrecognizable through
apa-dast
548:āpātān [’p’t’n']cultivated, inhabited 815, — Paz. äwäda; cf MPrth ’b’d (A-H III, BBB); Arm. lw. apat; NP äbäd and ābādān; < Olr *ā-pāta- ‘protected’, v. pätan (1).
```


## [2026-09-04T18:10:19.962Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; \necho '--- CHEUNG huar1'; sed -n 10309,10400p CHEUNG.txt | grep -n -i -E 'PERSIAN|āxwar|axwar|axur|manger|stable' | cut -c1-250 | head -6;\necho '--- CHEUNG raiz/raic'; sed -n 20403,20475p CHEUNG.txt | grep -n -i -E '^\\*|PERSIAN|rez|rextan|pour' | cut -c1-250 | head -12;\necho '--- BRT Wasser'; grep -n -E \"äp-.*f\\..*Wasser|'Wasser'.*äp|^• *j\\. *[äa]p- |Wasser' *[0-9]\" BRT.txt | head -8; grep -n -E \"an°?äp|an-äp|anäp- \" BRT.txt | head -4;\necho '--- KNT water'; grep -n -E \"water\" KNT.txt | head -6;\necho '--- IEC'; grep -n -E \"^(āp|ab-|ap- .*water|ab- .*water)\" IEC.txt | head -6; grep -n -i -E \"^ap- .*|āpos\" IEC.txt | head -4;\necho '--- WLD Bd1 ab-'; grep -n -E \"^ *[0-9]?\\.? *ab- \" incoming/WLD/WLD_Bd1_pages.txt | head -4; awk 'BEGIN{RS=\"\\f\"} NR==55' incoming/WLD/WLD_Bd1_pages.txt | head -3;\necho '--- SYN river'; awk 'NR>=1374 && NR<=1420' SYN.txt | grep -n -i -E 'Pers|Skt\\. |Av\\.' | cut -c1-300 | head -6",
 "description": "Cheung eat/pour, Bartholomae, Kent, Mann, WP, Buck"
}
```


### [2026-09-04T18:10:21.910Z] TOOL RESULT

```
--- CHEUNG huar1
10:*MIDDLE PERSIAN: MMP xwr-, BMP hwl- /xwar-/ (‘STHN-) ‘to drink, eat, enjoy 
--- CHEUNG raiz/raic
1:*raiz ‘to lick 
2:*AVESTAN: YAV. riz- ‘to lick = Liste: 58 
6:«MIDDLE PERSIAN: BMP Is- /Iis-/ ‘to lick’ 
10:*KHOTANESE: rri$- ‘to lick’? © SGS: 116 
12:*SOGDIAN: BSogd. rys- (inch.) ‘to lick’ 
16:*NWIR: Widely attested: NP listan/lés-, Kurd. (Sor.) lēsīn, listin/les-, Abz., Abyan. 
21:*NEIR: Sangl. l&s-/let, Ishk. les-/list, Wa. lix-/lixt, Yzgh. yiz- ‘to lick’ (with sec. g- ?) 
25:*raiz3 311 
28:*MISC: Par. Jis-/lust, Orm. las- ‘to lick’ 
30:*SANSKRIT: reh, Ich ‘to lick’ (RV) = EWAia II: 463 
35:*PIE *Jeig®- ‘to lick" = LIV: 404 | Pok.: 668 
37:*IE COGNATES: Gr. aixo, Lat. lingo, OCS liZo, Lith. lieZü, Arm. liz(an)em, Goth. 
--- BRT Wasser
4423:•  j.  an-äpa-  Adj.  ('wo  kein  Wasser  ist' sva.)  'trocken'  von  Speisen,  'ungemischt' vom  Wein:  gqmla  a^astsm  °apim  yaomca ahm  °äppm  maoula  "Spim  "trockenes  gar- gekochtes Reisch  .  .  und  ungemischten Wein"  V,  5.  52,  A)  als  ncutr.  Subst "Wüste,  17  änuhpoi':  yal  vä  '3p>m  ai  api kpfinaoiii  \yat  vS  3p3m  ai  °äppm  iir)- naoift]^^  "wo  man  zur  Wüste  hin  Wasser schafft"  V.J. 4.
4927:Et-?  —  Pü.:  anäpitän,  erl.{?J;  ahramati. Baitiuildui,  Aliinu.  Wb.
7049:•  j.  'äi  Praen.  mit  Akk.  'hin  zu  — "':  yat vä  anäßpm  (sd.)  3i  sp^m  kirftiaoiti  yat  vä apfin  ai  anäp^in  kinnaeiti  V-5.4.
10138:—  tistryS ..vaz»mnö  -Jus  k)hrpa  zaranyS.-  bagä  x^ar^mnif  (sd.)  Y. 32. 8;  —  "Su/x'ar»- srvahe  YLÄ16;  i4-l,  Y.ig.yi.  A)  Das  \%ahe  nr^yJ  V.7.  43; — 'Sul  vä  s^var3%ahe Rind  gilt  als  Repräsentant  aller  nützlichen  j  (sd.)  vä  W.14.1T,  —  '!us  i^ar/itinqm {ahumohtn)  Tiere,  daher  ^gav-  auch  inJH, /.  5;  —  yasca  ..  lanumazs {^A.)  'Jui weiterem  Sinn  gebraucht  wird*"':  para\da%at  "W-iS.!!);  —  °amla  ifsst)m  anäp»m •Su^  ca^war).paitistanaya  dänheit  para\{%d.)  V.5,  52;  S3f.',  7.55;  —  buiri 'aas  ,  . nars  asaotiB  bipaittstänahe  zq%st  Y.  /p.  8 ;  j  3far>^a  . .  VyL  4:5.  3)  'Milch',  bes.  zur
--- KNT water
1041:ТҮ. Combinations of the labials with follow- ing consonants, other than т, chance to be rare in OP; there is however *ap-bhis > *abbhiS > OP abiS ‘with the waters’ (JAOS 62.269-70; $73.V, §130). For p in sp from pIE ky, $90; for b in zb from ghy, $01; for f from " in Vi"da- farnah-, §118.IV.
1531:*ap- ‘water’ in inst. pl. abi$, *üp- in nom. dpi, loc. apryd.
1774:йр- ‘water’, zíap- ‘night’, xfnau- in u-zfnau- ‘well satisfied’, gau- ‘cow’ in compounds, bard- ‘year’, dwar- ‘door’ in duvara-, nar- ‘man’ in üv-nara-, nàv- ‘ship’, паћ- ‘nose’, pad- ‘foot’ in nipadiy etc., vas- ‘wish’ in adv. vasiy, vib- ‘house’, séd- in upa-stá- ‘aid’, zam- ‘earth’ in u- zma- etc.; perhaps napdl- ‘grandson’, an old pIE word, probably a compound; possibly dà- in ‘wada- as element of Paisiyà-uvüdà-, and vaj- in gen. daha-vaja. $143. Noun AND ApjectivE STEMS WITH THE-
2224:"$88. Tue Srems IN Stops, 1ч OP: these in- elude stems ending in £ (napdf- ‘prandson’), nf (*tunvant- ‘strong’), d (éard- ‘year’, pad- ‘foot, rād- ‘cause’), p (xSap- ‘night’, ap- ‘water’ cf. épi-) k (vif- ‘house’, vas- ‘will’).
2718:G. Alone, to express cause: DB 1.86 2015 naviya dha ‘on account of the waters there was navig- ability’; DSe 46f didà ha[natüyà avagmat|é ‘wall fallen down from lapse of time’ (both examples doubtful, see Lex. a.vv.).
3295:DB = Dans, BeursTAN: The inscription of Behistan, trilingual, is inscribed on the face of a gorge in the cliff rising on the left-hand side of the main caravan route from Baghdad to Teheran, about 65 miles before reaching Hamadan. Here, at the height of about 225 feet (obliquely 322 feet) above the road, the last 100 feet being steep and difficult, rock-climbing—the final portion being in part cut smooth by Darius's orders, to prevent access by vandals—sculptures and accompanying inscriptions are engraved in the natural rock. The panel of the sculptures contains at the left the standing figure of Darius, with two attendants behind him; his right foot is firmly planted on the prostrate figure of Gaumata. Beyond Gaumata stand m line the captive rebels, 9 in number, with hands tied behind their backs and a rope around their necks linking them together. Above, there is a figure of the God Ahuramazda. The inscrip- tions in OP, Elam., and Akk. occupy the free parts of the panel and its lower margin, as well as the spaces below, to right, to left, and diagonally below to the left. These have suffered both from erosion by water torrents and by limestone in- crustations deposited by water in and over the engraved characters. Further damage was suffered
--- IEC
622:ap-, radical of āpnu-, āpos, aptos, q.v.
6765:kāpos, a “holding; garden’. WP I, 345 Gk. képos ‘garden’; Alb. cf. kop-sht, id.; OHG huoba ‘yard’; MHG huobe, id. & ‘measure of lang’; G (fr. LG) Hot: Du. hoeve ‘farm’; LG hauw ‘smallholding; outfield’; Fris. hôf ‘orchard’ (LG has several dialectal variants)
15581:skēpos ‘staff, pole, pike’. WP II, 561. (Vari- ant of skåpos, q.v.) OCS Stapú, m. “pole, stick’; Big. Scap, m. id.; Latv. šķēps, m. ‘spear’. The Doricism in Alb. shkop, m. “stick? is ambig. (see skāpos) in view of Dor. Hes. skápos & the Lat. (inherited or LW) scapus
--- WLD Bd1 ab-
46                                           ap     ap-


--- SYN river
4:It. fiume; rivo; ruscello, NE river; stream; brook Pol. rzeka; potok; ruczaj, etc. Du. rivier; stroom; beek strumyk Fr. fleuve; riviére; ruis- OHG fluz, aha; strom; bah Russ. eka; potok; rutej : seau MHG _  vluz; strom; bach Skt. nadi-; sarit-, srotas-; Sp. rio; arroyo NHG  fluss; strom; bach kul
5:Ay. Graotah-, ravan-, etc., OPers. rauta-
8:1. Derivs. of IE *sreu- ‘flow’ in Grk. pew, Skt. sru-, ete. Walde-P. 2.702 f.
14:tourse’ (with or without water); Ir. sruaim, sruth ‘stream, river’ (NIr. ‘river’ in river names), NIr. srutén ‘brook’, W. ffrwd ‘stream’, Br. froud ‘torrent’ (so Pedersen 1.35; fr. *spru-tu- : OE spritan ‘sprout’, etc. Walde-P. l.c.); ON straumr, OE stréam, OHG strdm, 
15:2. Derivs. of IE *rei- in Skt. ri- ‘et go’, mid. ‘flow’, Goth. rinnan ‘run, flow’, ete. Walde-P. 1.139 ff., Ernout- M. 866 f. -
18:3. From IE *ap (and ab-) ‘water’, Skt. pas, etc. (1.31). Walde-P. 1.46, Ernout-M. 45. Walde-H. 1.40.
```


## [2026-09-04T18:10:43.998Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; \necho '--- CHEUNG raiz3'; sed -n 20469,20510p CHEUNG.txt | grep -n -i -E '^\\*|PERSIAN|rez|rextan|pour' | cut -c1-250 | head -10;\necho '--- IEC āpos'; grep -n -E \"^(āpos|apos|āp-|ab-)\" IEC.txt | head -5;\necho '--- BRT āp-'; grep -n -E \"[äa]p- +f\\. +'Wasser|f\\.  'Wasser'|'Wasser'.*\\(ap\\)\" BRT.txt | head -6;\necho '--- KNT api'; grep -n -E \"^ *[āaä]pi- |[āaä]pi- *f|^ *ap- \" KNT.txt | head -6;\necho '--- HRN 548-556'; sed -n 546,556p HRN.txt | cut -c1-200",
 "description": "Cheung pour, Mann apos, Bartholomae ap, Kent api, Horn axur"
}
```


### [2026-09-04T18:10:44.130Z] TOOL RESULT

```
--- CHEUNG raiz3
1:*raiz? ‘to fall (out), drop’ 
3:*PARTHIAN: ryz- ‘to fall (of leaves)’ = Ghilain: 94 | DMMPP: 304a 
7:*SOGDIAN: BSogd. ryz ‘to drop’ (GMS: §900A) || (+ *aua-) MSogd. ’wryz ‘to drop’ 
11:*CHORESMIAN: ryz- ‘to fall ош” = Samadi: 176 
13:*NWIR: NP réxtan/réz- ‘to drop’, Bal. rézit/réz- ‘to atrophy, become thin, decay’ 
14:*NEIR: Pash. raZ-/raZed-, rez-/rezed- ‘to fall (leaves)'. © The Pash. verb has also the 
15:meaning ‘to pour’, which is perhaps a calque on Pers. réxtan/réz- ‘1. to be shed; 2. to 
16:pour’, МЕУР: l.c. 
24:*PIE— > LIV: — | Pok.: 
27:*IE COGNATES: — 
--- IEC āpos
646:apos, ios (1) ‘miid, gentle, thoughtful Skt. apyam ‘friendship’; Gk. épios; OCS cf. za-japü ‘thought’; Li. opüs ‘sensitive, tender, gentle’ |
647:apos, ios (2) “taking, seizing, snatching’. Cf. āpnu-. WP I, 46, 47; I, 121 Skt. åpyah ‘obtainable’; apyam ‘alliance’; Av. apa-; Gk. cf. n-épios (simple, childish’: Cz. nejapny 'inept'); ON œfr ‘vehement’; Cz. japny “clever, smart’; OCS cf. ne-za-japü “care- lessness'
648:aposthos, us, ios ‘stopping; stop, confronta- tion’. Cf. apo, sthà- Skt. apasthuh; Ir. fos “stop, rest; OE æfest ‘hate’; aphetic in fæsten ‘fasting’; ON fasta; OCS postü “fasting”
--- BRT āp-
--- KNT api
--- HRN 548-556
hemänjä büd üräm ü Ubi^x^'eret
Hekim Esedl, Metr. Muteqärib.
Die Grundbedeutung scheint 'Tränke* (so Sahn. I, 12 Vers 209) und
V
dann 'Trunk, Unterhalt* etc. zu sein. Zu a) füge ich noch Sahn. I, 84
Vers 422 hinzu. Bei Hafiz ist das Wort häufig, z. B. Ohazel 4, 8 u. ö.
1*— 4 -
8. üj^xir *Stair.
aw. avöx^'arena- *Stall, Futterplatz' ; phlv. av;(ur oder
avx^'ar (Darmesteter, Et. ir. II, 136), arm. LW. ayor,
vergl. Talmud LW. •imnx (de Lagard e, Semitica
```


## [2026-09-04T18:10:54.784Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; \necho '--- IEC water'; grep -n -E \"^(ab|ap)[a-z]*[-,].*(water|river)\" IEC.txt | head -6; grep -n -i -E \"^abnis|^amnis\" IEC.txt | head -3;\necho '--- BRT ap- lemma'; grep -n -E \"^ *[äaā]p- +[0-9]?|^• *[jg]\\. *[äaā]p- \" BRT.txt | head -8; grep -n -E \"äfs|āfš\" BRT.txt | head -5;\necho '--- KNT apiya'; grep -n -E \"api-|apiy[āa]|abis\" KNT.txt | grep -v -E '§|\\$' | head -8",
 "description": "Extra greps in Mann, Bartholomae, Kent"
}
```


### [2026-09-04T18:10:56.552Z] TOOL RESULT

```
--- IEC water
223:abhmn-, abhnis ‘river, water’. WP I, 46 Alb. âmë, f. pl. -a 'riverbed'; Lat. amnis, gp: amnium, mf. 'river; Gallo-Lat. ambis; Gaul. abono-; W afon, pl. -ydd, f.; Br. aven, Cor. avon, id.; Olr. aba, gs: abann, aband & abhond; Ir abha, gs. & gp. abhann, npl. aibhne, f. id.
--- BRT ap- lemma
7276:ap-  Noten
3944:•  j.  aiwiä.x^arsUa-  Adj.  (fem.  '5*)  'zum Genuss  geeignet':  aü~a  äfs yaoidya  bavaiii vaiS  'ia  foiubya  vlraiibya  V.ö'.32.
7042:—  jfff  ('wer'  sva,  'wenn  einer')  i/irar/i  zn aiwi.v?r)zyHti  .  .  ä"  aoxta  Tm  za  nara V.^j.aö.  8)  Ohne  Beziehung  nach  vom oder  zurück,  einfach  satzeinleitend: aoxta  saraiiuärö  "es  sprach  Z"  Y./0.17, Vt.1.5,  3.2,  A2.I,  'Vyt24;  Y.21.3,  Aog. 57,  A'/D,  Vd./2,  20,  Yt.  ij.  54;  —  3° /ra/ssat  anävl . .  aal  (s.  2)  aoxta  ar»dvl Yt.5.  88;  7;  —  äat  aokU  haxa  haia  "es spricht  der  Freund  zum  Freund"  V.  18. 26; 18,  FrW./o.4i.  a)  bes.  vor  ya-,  yat, yezi:  ä°  ya/tmäi  xlnüts  bavatti  (sd.)  .  . ahmai  .  .  äat  (s.  3)  yahmäi  tbistö  bavaiti mihrB  ahmai  .  .  Yt./o.S?;  —  ä'  yg  na his  frayasaite  .  .  ahmai  .  .  "qui  vir  eas adorat  . .,  ei  . ."  Yt.y5.s1;  18,  P.57;  — ä'  yat . .  ipa  vä  . .  iriiiyät  iu'^a  . .  "wenn . .  ein  Hund  .  .  stirbt,  wie  .  ."  V.  .V.  1 ;  Yt. 6'.if.->,  7.4,  14.63;  —  ä'  yasp  %wapa'^qm (sd.)  Jasaiti  vahwassö  yezih  . .  a^a  .  . Yt/?.2o;  —  ä'  yat  apo  uzbarpnte .  .  äai (s.  7)  . .  Yt.  13.6si10.AZ,  ss;  —  ,r  yäl mi>rpm  .  .  /radaöam  .  .  äat  (s.  7)  .  .  "als ich  den  M.  schuf  . .,  da  . ."  Yt  to. ä°  yezi  anhat  äfs  . .  äat  (s.  3)  yezi  anhat urvara  V. 8. 1Ö4-6 ;  Vd.  2  i.,3.St  a)  ein- geschoben :  ye^he  hätam  ä'  yesng  (sd.)  . . vai%ä  .  .  yänhamca  ..  Y.2j.i$;  H.2.14
8743:. .  vahistsm  paityämraot  ¥.27.4;  F.5;  — vXspäyämca  "tatim  .  .  'tätfm  aiararum yazamaide  Vt.iS.a;  —  vahistimla  ahütn .  .  vlspäyümca  HSs  (statt  Akk.)  P,  48;  — .  sadr>m  urvistnmla  (sd.)  ,  .  -tatsm  nimra- vaite tistryö  .  .  usta  ml  .  .  YLÄ  23  und I '9;  '3-93i  PrG.;  —  uslavaittm  g^qm '■  sravayS  'täfsm  nimraomns  'usta  ahmai  . .' ,  H.  2. 2 ;  Y.  7/.  1 6 ;  —  nf  -taite  nl  vahiÜai atnthe  .  .  Vyt.j'j.
11761:surunvata  yasna  tarn  yjzäi  . .  arfdvJm YL5, 9;  /7.  3;  —  la  hasHt  upa.sbayeiU tqra.-fravalayS  Yt.ij.ög;  —  .Ja  nipa- yemi  vispa  vokü  Yt  5. 89;  —  harn  taät (NDm.)  bJeus  baratö ..  tistryasi'a ..  daFvasca .  .  la  (Sp.  615  m.)  yaitya^S  Yt.  S artikelhaft:  //{AD£)  aifam  paili  sruye(sä.) aZsa  druxs  upa.dvqsaiti'S ."j.  24'"';  — ya^a te  vTspe  aurvanta  zasvauha  (sd.)  paili. jasqnXX.  ^.\%t\  ;o.i2S;  —  ta  nS  data  tä (Sp.  6 1 5  u.)  fravaocäma  Y.  70.  2 ;  —  ava  Al baraytn  läshm  dauru{'si.)  upa  tqm  manao- ürTm  "sie  sollen  ihm  . .  am  Hals  anbringt V.  ij.  30;  —  minutn  barat  andvl  .,  upa tqm  srirqm  manao^rim'Vt. 5.  i2T. titn  urva^fm  /rayavaySiJ'(sä.)  sna^äi  Yt. 7.  24;  —  i^m  valmcit  yazamaide  "(ihn) den  f. , ."  Yl  75. 1 ;  i;  —  äal  t>m  varpm kfrsnava  V.  2.  25;  —  avavanOm  asa- vaynyäi  (sd.)  tqm  ä^qm  dagtayJ  V.  5. 14;  —  ä  tai  :^ami5  yasamaide  Vr.  ig.  a ; Ytö.iä;  —  nöit  kl  tä  vlsB  tilyul . . apaili.- buili  haca  vTiibyS  para.baraiti  (sd.)  V.  13. 40(?);  —  nava  äfs. .  navata  baiiacajipsa V.  21.  3  (?);  —  s.  noch  Yt.  10.  6,  i§.  49, V.p,  29;  s.  Sp.  616  o.  bb)  mit  rela- tivischem  Anschlüsse' ;  a)  im  gAiv.:  at  tSng dngva  ySng  asalefl  vazdrJng p,lt  gä fror»' f^{s6..)  Y.4Ö.4;  —  t3is  . .  yäis  daiäis  . . ^,46.  15.  B)imjAvr.:  tat  drvais..ta! . .  pairi.urvalstsm  yat  tamS  voku  Yt. //.  a; Y-jÄ  I';  —  ta  (NPn.)  ns  ama  ta"  . . uxjamyqn  yä  staota  yestiya  Y.  55.  3;  — ta  vanukJ?  tä  vahisth  yazamaide  ya  .  . fravasayö  Yt. y.  27;  —  tä  .  .  upastqm k^Ttti  dahiita  ya  fravasayS  Yt  13. 17;  76;
13113:yahmat  haca  Jräkwirisal  näfs  airyanqm °Hyunqm  ^r^m  airyanqm  'hyunqm  Yt. '^■^7)  —  ifar^Rö  .  .  yat  asti  airyanqm 'Ayunqm  Ytip.  56;  V. /^.  39;  —  iava/ftn :^arpnd  'hrähr^m  airyanqm  "AyunamYl-ig. 69;/?.  10; —  avavat  kavaSm  3^ar>ns yaha yat  iöa  anairym  °Ahus  hakat  usäi  us.frs- vayöit  (sd.)  Yl.  ip.  6  8 ;  —  taurvayeiti  anairya *'/iAävS(3isA'P.)Yt.iS.2;  —  airaityanqm tat  °Ayunqm  Vf/y^rai  uzjasaiH  N.(iS;  — aiioitaradyJ  haca  'nhubyö  Yt  i'j.  14;  — mi>r)m  .  .  yim  yazmte  daiAkupatayS  .  . aniar»  -iiihu  (AD.)  papr^täne  Yt.  10.  8; r_5.  49;  —  hasaaräis  (näml.  asH  mihrS) aiitary  °Ryu  (AD.)  Yt.  /o.  117;  —  yd  .  . karafanö  urapayeintl  (sd.)  yacä  xrata *Ju£>sc/a'irä  "Ayunqm  Y.4^'.io;  —  säsia 'rthSui  äaähupailii  *äxsta  isimnS  'lihave amtm  is^mnS  tanuye  YtJÖ^.  19;  —  sSsta 'itißaus  hams^ia%rö  Yt  13.  r8,  69,  75.  50; — fraiimatcltl!  'Xyunqm  Yt  13.  95;  *lo.  18; —  nöit  me..  ährava  . .  'iiifiava  (LS,)  earät Y.p,  34;  —  Siihqm  'hyunqm  yä  anyä rajSit  Y.ig.  18;  —  bawrSil paiti  'tJihaove Yti.ag.  a)  GS.  mit  GS.  des  Landes- namens  zur  Bezeichnung  der  Gebürtigkeit bei  EN.:  parlatgava  dazgrS^ava  apa- jTjVavi  (sd.)  'iähfus'  Ytrj.i2j;  127;  — ^rüJ  atv5jar3(^  fyultahe  tanyehe  tanyayä •tViÄÄ/ Yl  jy.  125;  125';  —  s,  noch tnzavant-  daitiksus  EN.  a)  bes.  im Gegensatz  zu  Haus,  Gemeine  und  Gau***; a)  im  gAiw.:  *S  sl  dimSnsm  vTs)m  v3 söihnrrt  vä 'Ayäm  vä  adaj  du^iäcd(sd.) .. Y.jt.  18;  —  yP  Auäänus  d^manahyä  xla- %r?m  iiSi^rahyS  vä  'AySus  vä  .  .fi-ada'iiäi (sd.)  asppmaia  Y.Jl.  16;  —  ga  JrSnKis' (sd.)  /tfiiraAyä  vä  'AySus  vä  Y.4ß.^; —  ähnlich:  patri  jfaSSuf  airyamanascä dadaiii  (sd.)  tiSil  ma  xsnäus  yä  v^rvsSnä (sd.)  ..  naida  'hy3u!  ..  sästärB  (sd.)  Y.46. 1.  b)    im  jAw.:    */ratainitm   .  .  yä
--- KNT apiya
2138:Inst. Pl.: abis, arasanis: see Lex. s.vv.
2233:V. Inst. pl. viðbiš and abis show the regular
2234:-bhis seen in Skt. -bhis, Av. -bi; -6b- as a cluster remains by the influence of the separate stem and ending (we expect -db- from -f-bh-), and the -b- of abis is for -bbh- from -p-bh-. ‚74189. Тнк Dua Casg-Forms or ОР: nom. ubà ‘both’, uSiy ‘two ears, understanding’; acc. gauSa ‘two ears’, luffü-ed; inst. dasiaibiya ‘with two hands’, рбай ‘with two feet’, и.а, ušiyā, gausaya.' These are masculines, except ну, which is neuter.”
3491:42 :agarbàyatà : Garmapadahya : máhyà : IX : raucabis : 0akatà : dha : ауаба : xša 43 cam :agarbàysatá : pasáva : Kabüjiya : uvamarSiyuS : amariyatà : іу
3499:56 máhyà : X : raucabis : 6akatà : dha : ауаба : adam : hada : kamnaibis : martiyaibi
3542:96 pisim : parábara : Andmakahya : māhyā : 11 : raucabis : бака: dha :avatà : hamaranam : akuma
3641:98 m : aja : vasiy : Viyaxnahya : máhyà : X XII : raucabis : Sakata : dha : avatáSám : hamaranam : kartam
3721:39 zdàátahya : aja : vasiy : Güravaharahya : mahya : XII : raucabis : бака
```


## [2026-09-04T18:11:09.869Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; \nfor w in 'آبریز' 'انبیق' 'ابریق' 'آفتاب' 'آخور' 'آبادان' 'گلاب' 'آبنیک' 'زهاب'; do echo \"--- BQT v1: $w\"; grep -n -m4 \"$w\" BQT_v1_pages.txt | cut -c1-200; done;\necho '--- BQT v3 زهاب/زاب'; grep -n -m6 -E 'زهاب|زاب ' incoming/BQT/BQT_v3_pages.txt | cut -c1-200;\necho '--- BQT v4 ناب'; grep -n -m6 -E '^ *ناب|ناب ' incoming/BQT/BQT_v4_pages.txt | cut -c1-200;\necho '--- BQT v2 پنجاب'; grep -n -m4 'پنجاب' BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt | cut -c1-200",
 "description": "Grep Borhan-e Qate volumes for the Persian headwords"
}
```


### [2026-09-04T18:11:12.298Z] TOOL RESULT

```
--- BQT v1: آبریز
--- BQT v1: انبیق
--- BQT v1: ابریق
6084:بیمنی ابریق و آفتابه و مطهرء ومانند آن
6090:که‌آفتابه وابریق (۳) باشد .
--- BQT v1: آفتاب
1205:«چون لغت عبری وسریانی وپهلوی تا بایام طلوع آفتاب دین عر ی
1422:سیوندی نیزاز نظار علم اصوات منفرد است ( 0۲] (خورء آفتاب) »
4164:آت شگردان ۰ آرواره » آفتاب گردان ۰ آفتا به» آقا.ابزار» از گیل
6084:بیمنی ابریق و آفتابه و مطهرء ومانند آن
--- BQT v1: آخور
5552:«خویله» وبا «خویش» و «خویشتن» مکسور و با *آخور؛ و *میر آخور »
6747:« آخور » . بسببآنکه رس‌الخط این‌زمان است .
6803:آخورد ات بعفیده مولف آد ۲ 1 9
6817:| خو دسا لاد ع می رآخورء(۲) وسلار
--- BQT v1: آبادان
1181:«من درهمةٌ زمین بارسی گویان شپری نیکوتر وجامم‌تر و آبادان‌تر
8498:و آبادان کردن :
16035:ساخت چه بادان بممنی آبادان است.؟ .
16056:بادان - بر وزن نادان . مخفف آبادان
--- BQT v1: گلاب
4465:سپامی چپر . ۱۳۷۸شمسی (-- گلگلاب).
8318:آن از آمربکای جنوبی است «فرهتکه روستابی 6۹۷ « کل گلاب ۲۹5۶». ره : آفتاب پرست .
8638:مرخبان . « کل گلاب ۲۲۳۷>. 4 آلتمغا - را: آل طمفا. » آلنوی - ترکی
9132:روستابی ۱۰۰ » ونز رک : گلگلاب ۲۹۹ . ۸ - شاهدی برای آهازیدن و مشتفی از
--- BQT v1: آبنیک
--- BQT v1: زهاب
6166:های هوز » پمعنی زهاب باشد » بمنی آب ی که از
--- BQT v3 زهاب/زاب
12965:جنیر ی سثبل - کنابه اززلف وموی | وآن‌چویی باشد که چیزهابدان‌رنگه کنتسوخون
19671:بدیدن وی ‎whe‏ وآن حنگام جشن فروردین است یعنی روزهابی که برای فرودآمدن فروهرهای
22387:‏؟ - رگ : رشیدی . اشاره ‎LT‏ ۷۱ از سور ۳۳ ( الاحزاب ) : انا عرضنا ‎ge ULV‏
30715:۶- دینور و کنگاور ‎-٩‏ ماهیدشت وهارونآ باد و فیروزآ باد ۷ سحنه ۸-کرند 4- زهاب
30848:‏۴ -کرند ؛ داحیه ایست از کرمانتاهان » از شمال محدود است به زهاب » از مشرق
34855:‏خاییدن وجاویدن چیزهابی که صدا کند مانند
--- BQT v4 ناب
402:از کناب بردان قاطع درحرف میم با حروف تجی مبتنی
983:کوبن د که منسوب بماکان باشند - و حربه‌ا ی که | که برکلو بندند همچو رسن وطناب - و بمعنی
1015:کرده ونوشته آند : « صحیح است » [ رس بمعنی طناب وکند ورسن است . رك : برهان فاطع :
1444:دهندة مطالب کناب بوده و در پونانی باسم « ایقون » و درزبان پارتی ۸ اردهنگه » و در پارسيك
1983:۱ - نام این کناب دراسل(5181515) 1368101516 ,ز
2036:است که حرف اول احمد باشد ۲ . ا محك * زرآپمان - کناب ازحجر
--- BQT v2 پنجاب
incoming/BQT/BQT_v3_pages.txt:23468:۴ - 2 قزدار ؛ بالقتح هریت در حوالی پنجاب که الحال بنام ‎Sis‏ مبوانده باشند -
incoming/BQT/BQT_v3_pages.txt:50445:۵ لاهور = لاوهور ‏ لهاور. شپری با کستان » کرسی‌پنجاب 6 دارای ۷۲۰۰۰٩سکنه.‏
BQT_v2_pages.txt:2251:       ‫مابین پشاور ولاهور ممرش از وسط شهر کشمیر و ازآنجا جبال کشمیر آبد و صحرای پنجاب‬
BQT_v2_pages.txt:6964:                               ‫ازماهی باشد ‏‬                               ‫مشهور درولابت پنجاب ‪. ۴‬‬
BQT_v2_pages.txt:21855:           ‫گل با از خمیر نان بازند و در‬                  ‫ودیبال پور که قصبه ابت در ملك‌پنجاب‪ .‬اوبتا‬
```


## [2026-09-04T18:11:26.873Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/sources/refs/ocr/ 2>/dev/null; for d in BQT IRN ARY PLA; do echo \"## $d\"; ls data/verification/sources/refs/ocr/$d 2>/dev/null | head -40; done; sed -n 1,60p tools/ref_page.py | grep -E 'argparse|add_argument|usage|Usage' ",
 "description": "List cached OCR pages and ref_page.py options"
}
```


### [2026-09-04T18:11:28.546Z] TOOL RESULT

```
ARY
BQT
IRN
PLA
## BQT
0001.png
0001.txt
0049.png
0049.txt
1225.png
1225.txt
1357.png
1357.txt
1803.png
1803.txt
## IRN
0108.png
0108.txt
0119.png
0119.txt
## ARY
0051.png
0051.txt
## PLA
0022.png
0022.txt
0027.png
0027.txt
```


## [2026-09-04T18:11:33.525Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr; for f in BQT/0001.txt BQT/0049.txt BQT/1225.txt IRN/0108.txt IRN/0119.txt PLA/0022.txt PLA/0027.txt ARY/0051.txt; do echo \"=== $f ($(wc -c <$f) bytes)\"; head -c 2500 $f; echo; done",
 "description": "Read cached OCR of the cited BQT, IRN, PLA, ARY pages"
}
```


### [2026-09-04T18:11:35.356Z] TOOL RESULT

```
=== BQT/0001.txt (1684 bytes)
REF: BQT:1  PDF: data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf page 6  OCR-lang: fas

حلد او ل
۱ مدمه
صفحلاچهارده» پی ازسطر ۱۳- استر|پون گوید : زبان‌مادها شبیه زبان
پارسیان » بلخیان (مردم باکتریا) و سغدیان است! .
سطر ‎۱٩‏ رك . «سگث» در همین کتاب .
صفحا پا نزده» پس‌از سطر۱ - افزژوده شود :
«کنت» لنات پادسی باستان را که دارای خصایص زبان‌مادی هستند »
بطریق ذیل تقسیم کرده۲ :
‎٩‏ اسماه امکنه :
آسه گرته 4 (فناممهده) * نام موضعی در ماد .سس و در
238 مأخوذ از و ظاهر] بمعی دسنگ؛» ۰
سیکه‌ی‌اوتیش «(ءز)۲۸دووززه » قلعه‌ای مادی, با ای و » مأخوذ
از پر محتمل است که بخش‌اول آن با یک انم پادسی باستان‌یکی باشد
بمعنی «سنگک شکسته» .
۷ - اسماء اشخاس :
تخمه چربربرد) (مشجاع)؛ با ح که پیش از 7 محفوظ مانده ؛ در نام
شخصی‌مادی باسم تخمسپاد» و0ژم‌یوودد 2 و نام‌شخص‌سکر‌تی‌موسوم به سیس
تخمه ورور‌ها هم( ۳ ۰
خشثریته ۵ع:۶طع 72 » نأامی که مردی مادی موسوم به فرورتیش
,رد۳ ,607487 هعنوجم2 ۵0 م۴ 6 ۲-2
,وه بظز ,1930 00206011001 م2ع1330 ببعل2
۳ باید در نظن داشت که -دوز» درین نام شکل پارسی باستان داردء نه
شکل مادی - )0۱ *#(کنت)

=== BQT/0049.txt (2677 bytes)
REF: BQT:49  PDF: data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf page 54  OCR-lang: fas

-4۹- برهان قاطم

لهجه‌ای‌از لغات‌سندی 20 زپرووق * » باتبدیل پیشو ندفعل سغ وسوورو
که در سفدی متداول است . راه حل اول از لحاظ تهجی فارسی ( رك .
فولری » ۰1 ۳۹ : ۹۷ ؛ نیز و1010 ووهه » سفده » ایضاً 77 ؛ ص۲۹۸ ۰
مشکو4است) وتصادف استعمال کلمدسندی - موم کهلا! قل دردو لهجه‌مستعمل
است » هرجح است . رلك

(103 .1:0 +جعطردد.[0 38۸08۷ ووصفنصص 13 )

صفحه ۴۴ , ستون ۱ سطر ۵ آسیم - درپهلوی پررژیی بمعنی( نقره سیم )
است «فرهنگك پهلوی. دستور جاماسب‌جی‌اسا - هوگه س ۷۵ (رلك. سیم)
و «استاد» را در هزوارش ۱/۹1 دز نوشته| ند «هینو خرد . چأاپ وست ص
۰ قانا(ه)رقاقه 0۹۳ « یونکر ۱۲۲» ظاهراً در لغت و معنی آن
خلطی‌شده .

مطر ۸ آسیمه <ه سیمه( رك . هرمزد نامه ۳۶8 - ۵)قس . اوستایی
وصرزه (سهمگین) «هرمزدنامه ۳۶۵ ۰

صفحلا ۷۳۵, حاشيةٌ سطر ۳ - آخر حاشيهٌ دوم افزوده شود: بقول هرن
طقءلطاعه » پهلوی مخز اعد از لغات آرامی دخیل درفارسی است «اسفا ۱
ای

صفحه ۳۷ ستون ۱ سطر ۲۳ » آغار - رك . آغاردن , آغاریدن .

ستون ۲ سطر ‎٩‏ ( اغراء )- بمعنی|خیر < آغال( آغالیدن» بر‌آغالیدن؛
آغالانیدن) ولغة ربطی به «اغراء» عربی ندارد .

سطر ۱4 (صدا| وندا) - «یمعنی صوت و صدا| واستشهاد بشعررود کی :

«ت وگفتی‌مگر تندرآغاز کرد» یعنیت و گویی مگردعد شروع کرد...محل
ایراد است .» (انجم نآداء» رك . اغاز .۰

سطر ۱4 (ابتدای کارها) - سغدی رای ۷ (شرو ع کردن) « بنوفوست.
۱ هنینگک نویسد : آغاز وق‌رایوق «شروع»< سغدی بارزم:« بسیار
امدن» (هنینگه . سندی 880۸8 ج ۰۱۰ ۱ص ۰)۹۸

صفحه ۴۸ سطر ۱۹ :آغالیدن-از: آغال(۸.م. ) +-یدن( پسو ندمصدری).
این مصدر متعدی است . بعضشی «آغالانیدن» �
=== BQT/1225.txt (4412 bytes)
REF: BQT:1225  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 16  OCR-lang: fas

-و۱۲۲- هارو
امران را شاه و ترکتان را خان میگوبندوبستی | کتابی است از تسنیفات فرزانه بهرام که یکی‌از
کوبند شار پادشاه حبعه باشد - و غل وغشی |[ حکمای عجم است ۱*۶ - وکوشك وعمازتی رافیز
را نی زکویند که در طلا ونقره و چیزهای دیگر | کویند که اطرافش بائین باشد.
کنند - و بهمتی شفال هم آمده است ۱ ۰ وآن شارشات!۱- بنتح نالك و سکون شین
جانوری باشد شبیه پروباه - و چادری باشدبقایت | نقطه‌دار وکاف » بمعثی تیهو باشد "و آن‌جافوری
نازك و رلگین که ببشتر زنان ازآن لبای کنند | است ماندکيك لیکن کوچکتر ا زكبك است -
و جامةٌ فانوی نیز سازند ۴ - ونام جانوری‌است |[ او بمعنی رباب, نیز آمده است ۰ و آن سازست
سیاه رنگه و مانند طوطی سخن کوید ۴ -وبنای مانند طنبور بزر کی :که دستهٌ کوتاهی‌داشته باشد
بلند وعمارت عالی را نیز گفته اند - و بمعنی و بجاي تخته برروی آن پوست آه وکشند وچپلر
شاء راء هم هت که راه قراخ وکشاد باشد ۴ تار برآن بندد .
وفروربختنآب ودراب و امثال آن باغدهمچو شار لد ۱۴ - بروزن ناوك » پرسماست
آبغار و سرشار ‎٩‏ - و به‌عنی رقص و سماع یز سیاه و مانند طوطی سخن کوید ؛ ویستی کوبند
بنظن آمده است. پرنده‌ایست میاه و كوچك و آنرا هزار دستان‌لیز
شارده < بسکون ثالك و فتح‌دال ابجد» | کویند ؛ ویعتی دیگر گفته‌اند مرفیست كوچك
نام جزیره‌اپست از جزایر دریای روم ‎٩‏ ۰ و خوش‌آواز که آواز اورا دای چهارتار تشبیه
شارسان ۷ - باسین بی نقطه بروزن | کرده‌اند و قید سیاه و سفید نکرده‌اند.
خاکدان » بمعنی شهر «شهرستان باشد. شار مار؟۱۴-با میم بروزن کارزاره نوعی
شارستان ۸ -بروزن 
=== IRN/0108.txt (2984 bytes)
REF: IRN:108  PDF: data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf page 119  OCR-lang: fas

۱۸ ایرانویج
می گیرد و پس از آنکه بخش جنوب شرقی ترکیه را آییاری کرد وارد کشور عراق
می‌شود. در این سرزمین از تنگه‌های کوهستانی‌بسیار می گذرد و در ناحیةٌ کردستان
در پائین موصل» آبهای زاب بزرگك وزاب کوچک ك که ازکوههای غربی ایران
سرچشمه می‌گيرند به‌آن می‌پیوندند. این رود زا ب که در فرهنگها وکتابها ی
جغرافیای تاریخی کندن آن را به «زو» پادشاه داستانی ایران نسبت می‌دهند, در
اصل ترکیب شده است از واژه‌های «زه» و «آب» واین ترکیب همانست که در
واژهٌ «زهاب» در نام محل سرپل زهاب» دیده می‌شود. دراين ترکیب زه به
معنی زاینده است از ريشهٌ 22 به معنی زاییدن وزهاب یا زاب به‌معنی رود زاینده
است و بازاینده‌رود هم‌معنی‌است . نام های محلی اين دو زاب درکردستان‌به گویش
محلی «زی بج وکث» بدا 2:27 زاب کوچکه‌و«زی گور»80۷۳2 227 -زاب بزرگك
است .

اروندرود سپس بینْ سامره وبلد وارد دشت میانرودان می‌شود ورسوبات رود
دیاله آن‌را به‌سوی غرب می‌راند. رود دیاله از بهم آمیختن رودهای «سیروان»و
«زالم» و«تنجه‌رو» پدید می‌آید وجای پیوستن این رودها «دوآوان» نام دارد.
دیاله در همه مسیر خود در سرزمین عراق به‌نام یکی از رودهای تشکیل دهنده
آن» سیروان نامیده می‌شود ونزدیک «سلمان پا کك» درجنوب بغداد به دجله می‌ریزد
و دجله را به سوی غرب می‌راند و آن را به فرات نزديکك می‌سازد, رود دجله
پس از پیمودن مسافتی دوباره به‌سو ی کوههای زا گرس باز می گردد ونزدیک عماره
در اثر رسوبا تکرخه به سوی جنوب می‌گراید و در «الغرنه» در ء + کیلومتری
شمال بصره رود فرات به‌�
=== IRN/0119.txt (3321 bytes)
REF: IRN:119  PDF: data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf page 130  OCR-lang: fas

اروند رود ۱۱۹
است : 3-026-30 » جزء نخست 2 به معنی آب است » 027 از ريشهٌ پاییدن و 27
پسوند نسبت است و«اپاتان» به معنی جایی اس ت که در آنجا از آب دریا و رود
پاسبانی می‌کنند وآن را می‌پایند واین نوع ترکیب همان اس ت که در آتور پاتکان,
هم دیده می‌شود وگفتهٌ ابن‌حوقل واستخری نیزگواه این معنی اس ت که پاسبانان
درآبادان دزدان دریارا از دزدی باز می‌داشتند ودهانة دجله و دریارا می‌پاییدند .
ابن‌حوقل دراین باره چنین آورده است: «اما عبادان قلعةٌ کوچک آبادی برکنارة
دریا ومحل گردآمدن آب دجله است وآن رباطی اس ت که جنگجویان ودیگر دزدان
دریایی در آنجا می‌باشند ودر آنجا پیوسته مرزدارانی مراقبت می‌کنند,»

در اینجا نمی‌توان بی‌آنکه ذکری از دجلةالعوراء به میان آید از موضوع
درگذشت . در برخی ازکتابهای جغرافیایی قدیم بخشی‌از رود دجله یعنی مسافت
بین نهر ابواسد وآبادان راکه از آبهای دجله وفرات تشکیل می‌شود وطول آن
نزدیک به يک‌صد میل است دجلقةالعوراء خوانده‌اند . دجلة العوراء به‌معنی‌دجلةٌ
یک‌چشم اس ت که‌نام گذاری آن را به هیچ وجه نمی‌توان توجیه وتبیین کرد. مردم
زمانه نیزکه اين نام را بی‌معنی وبدیمن دانسته‌اند آن را به دجلة مفتح تغییر
داده‌اند یعنی دجلةٌ گشوده شده, اما حقیقت چنانس ت که تازیان معنی يکك واژهٌ
فارسی را که نام آن بخش از دجله بوده است‌نفهمیده‌اند وآن را به یک وارْه‌تازی‌هم
آوای آن بدل کرده‌اند . عوراء در اصل یک وارهٌ فارسی بوده است «واو راه»۵۷۷73
تلفظ می‌شده‌است وساخته شده است از واه «او 6» به معنی‌آب وواژةٌ راه 
=== PLA/0022.txt (3831 bytes)
REF: PLA:22  PDF: data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf page 22  OCR-lang: deu+ara

adab                                                                                      7                                                         adarbigän


I -            ’adab:                "literarische                        Bildung"        aus       dem    pers,      —,ı    Adab      <<    mp.305           dipi
              "Inschrift" —T air.                                    *dipi-vara,

   5                                                                    -                                        -
;b3)_              ?”udabä:            Pl.           v. al            adib        "Gelehrter"             s.   adib.


 abo                 -     ’ adabhäna:                        "Klosett,           Toilette,          WC."      aus    pers.
                                                                                                                          —                adab      s.       adab
              + pers,                „4      häne              "Haus"       TU mp.       19»         xänag      mit       der       Bed.    "Haus        der
              Erziehung".                    Nach              Dehhoda        könnte          es    alt        abhane        "ein      Haus,        in    dem    es
              Wasser             gibt"         heißen.


ri             -     ”adbil:              Ort             in Armenien              s.    ‚>        dabil       m.           Ir       adbil     1,

          s                                                                                                                                               -
®,>!           -     ”adrün:                "Wohnung,                 Heimat"           pers.       2 aus      dem    pers,          Jy.ı      andarun          "in,
              drin"             T mp.             dw               andar-ron,            mand,       andruna         5,


@b>} - ”adyän: Pl. v. (u din s. din.

on - ”adib:                           "Gelehrter"                     act.        Pt.    aus
                                                                                          _,) ’adab q. v.

Uni - ’adyün = ’adyan s. 'adyan 4. v.

      r        .                                                                                                                -
„>t-           agdar:            "3.   
=== PLA/0027.txt (4498 bytes)
REF: PLA:27  PDF: data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf page 42  OCR-lang: deu+ara

 amirabür                                                                                      27                                                             ambiq

     7.                                  _                                                                                            -
Pi                         _ ”amiräbür:                        "Stallmeister"                   aus dem ar. „-ı ’amir + pers.                            _.>'
              ähör             s.       äbör,           syr.         ı91lyel.

                       j                ._                                  __                             u
ob!                            - ’amirbäris                       = ’ambarbäris                 s. ’ambarbäris               .
 r
ol-           An:          "Zeit",                 offensichtlich                    handelt           es     sich    um    einen         Singular,       der
              analog                    zum        Plural,           nachgebildet                   wurde.      s.d\,i ’awan u.uL; ’ibban .

              .5           >        -ı7                               >          -              >      -
 o»ab1-                        "anabir:              Pl.       v._1 ambär                 s.        'ambar.

  „3                             -
21                         "anafir: Pl. v._si’angar s. ”’ankar.
              s                           -                                                                                                               -
„ob                -       ”anähid:                  "Venus"          (astrolog.)                    pers.     ı aus       dem       pers.    „si     nahid
               << mp.                   up           anähit          am.             anähitä           2, ap.        anähita          "fleckenlos;            Göttin
              Anahita" -

      3,

Löl _ ”ambär:                                  "Magazin,              Kornspeicher"                    pers.        9 aus    dem pers.           21       ambar
                                                                                                                     ’
                  —mp.>r                           hanbar          ap.           hambara              4      syr.    fyaatlao 5,

     .$
ol - �
=== ARY/0051.txt (1571 bytes)
REF: ARY:51  PDF: data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf page 50  OCR-lang: fas+eng

آب. | ۵۱
۳ ُ
اوستایی ([/۸۳397): ۷ ,۸۳ پروسی کهن ((۶۴-95۸ 0ا0): ۸۳ :
پارسی باستان (/(۳8۴۶/۸ 01.0): ۸۳15 ,20 ایرلندی کهن (بلول#/ طا0): ۸۸0
پپلری (۳۸/7]۸1): ۸۳ و۸8
کردی (870157/): ۷ ,۸۷ پسگشت‌ها 5
سانسکرپیت (5۸(۹۴77): ۸۸ ,8 5152 200
یونانی (08286): ۸1۸ 9 (۷۸788) :۲62(/28 ۸۸
لاتین (710هل): ۸5 5 (۷۸788) 8
فرانسه (1ل)/۳/۸): ۸۷ 129 ی
لینوانی (771۸/1۷/.ا): 1 برهان قاطع : ۱
نوی (لتی) (771۸۷ا): 16 لغت نامه دهخدا: ۳۵
اوستایی (/(۸۲۳874): ۸7۸383 ۸788 1
پیلری (۲1هاتز۸): ۰ ۸7۸381 ,۸71 پسگشت‌ها ندش درد
کردی (۸)(7015/7): ۸1 9 ق2010
سانسکریت (5/۸(/987): ,8711۸3۷۸۷ 9 (ت۲8) پندن ۱۱۲ انا
کچ 31۸81 ,801705 4 (۲15) دم »ها
ارمنی (/(7۵/201۸): لد ی ۹ 71 8۸0
بونانی (058): ۸105 7 (۴138) 1/0(
4 لائین 700شلا: .. ۸ برهان قاطع : ۱۳-۱۴
فریزی کهن (لهلولغ۳ (لاه): 7 لغت‌نامه دهخدا: ۶۵-۶۶
ایرلندی کهن (57ن8] صا0): ۸171
یادداشت. َ
۱- چم این واژه در ایرلندی کهن: تنور.
چم این واژه در لاتین: سیاه) تیره.
۲- شاید واژه‌ی لاتین ۵714 با واژه لاتین ۸10814 (-> ۸310 > ۸140۸7۳) همريشه باشد.
سییر ی
```


## [2026-09-04T18:12:18.918Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; \necho '--- BQT v1 leaf of line 5860 / 8232'; awk 'NR<=5860 && /\\f/{n++} END{print \"leaf(0-based) for 5860 =\", n}' BQT_v1_pages.txt; awk 'NR<=8232 && /\\f/{n++} END{print \"leaf for 8232 =\", n}' BQT_v1_pages.txt;\necho '--- BQT v1 5855-5880'; sed -n 5855,5880p BQT_v1_pages.txt | cut -c1-160;\necho '--- BQT v1 8228-8240'; sed -n 8228,8240p BQT_v1_pages.txt | cut -c1-160",
 "description": "Locate the آب and آفتاب pages in Borhan vol 1 OCR"
}
```


### [2026-09-04T18:12:20.540Z] TOOL RESULT

```
--- BQT v1 leaf of line 5860 / 8232
leaf(0-based) for 5860 = 205
leaf for 8232 = 255
--- BQT v1 5855-5880
( برهان قاطع ۷ )۱ بروزن جاء امر بآآمدن باشد (۱)
یعنی بیا و بمربی تعالکویند - و بر وزن داه()
ذر عرمی حعایت از آواز هی چیز است - و نام
درختی هم هست .
آ یب س بسکون بای ابید . ممر‌وف است
که یکی ازجملةٌ چهار عنصر باشد ۴ - و بمعثی
رواح ورواق - وعزت وآرر ولطافت وقدر ۳
وقت تس وفیض وعطا و رحمت.- ودولت وترقی -
وجاء ومنزلت‌هم آمده.است (4) -.وطرز وروش
وفاعده وقانون‌را نیز کوبند (۵) سوبکی ازنامهای
خیاانت ه بزبان رومی تل‌ماه بازدهم بود از
سال ابشان وآن بودن آفتاست در برج اسد؟ -
(۷) چش: - هم .اشارتمت بر ضی‌کامل و عقل کل » و او را ضس
حلهیه گویتد ۷ -
آب ۲ تش د نگ - یکس شالت ؛
کنابه از شراب لعلی - و اشك خونین باشد .
آب ۲ تش دای با زای‌هوز. بنی
آب آش رنگ است ک هکنابه از شراب لعلی -
و ائك کلگون باشد . وآنرا آب آتئن وآشن
آب هم میگوند .
آب آ تش دده - کناب از اشك
۱
اب | فشیی شا - بس‌کون ات ؛ یعنی
آشوب برخاست و شور و غوغا بهم رسید - وآب
کرم شد .
آب تش نمای ه بکر ناك ,
--- BQT v1 8228-8240
یل هب رذن فاییل ».جسنی آغول
است که نگرستن بگوشهُ چشم باشد از روی
خثم ؟ .
]له - بروزن کاف. بمعنی مهراست
آفتاب اه بروزن ماعتاب. پصب لت
تایش و روشنی و برتو عهر است همحو ماحتاب
ترکیبی آن آفت آب است - و جصب احطلاح
شمی‌دا گویند - و بمعنی روز عم آمده است -
و کتابه ازشراب انگوری هم همت - ونزد ازیاب
سلوك از آفتابت دوح مراد است و از ماهتاب
نف ؛ و کوبند روح دریدن یمنرَلهٌ آفتاب است
غلامان ویندکان ترژك :
ای خواجهٌ ارسلان و آغوش
```


## [2026-09-04T18:12:46.230Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; \necho '--- BQT v1 leaf 205 (0-based) tail (footnotes)'; awk 'BEGIN{RS=\"\\f\"} NR==206' BQT_v1_pages.txt | tail -25 | cut -c1-200;\necho '--- BQT v1 leaf 255 tail'; awk 'BEGIN{RS=\"\\f\"} NR==256' BQT_v1_pages.txt | tail -22 | cut -c1-200;\necho '--- ref_page options'; grep -n -E 'add_argument' /home/sfmqrb/git/rishe/tools/ref_page.py | cut -c1-160",
 "description": "Borhan vol 1 footnotes for āb and āftāb; ref_page options"
}
```


### [2026-09-04T18:12:47.788Z] TOOL RESULT

```
--- BQT v1 leaf 205 (0-based) tail (footnotes)
لط قواعد دستورواهلع پارسی
وبی تشدید تای فوقانی وا گر ادغام کنندبتر شود باتشدید فوقانی» و کلمة
«زودتر» نیز از این مقوله است .
دیگر هر گاه لغتی را که در آخر آن تای فوقانی باشد. وآنرا
در عبارت عربی صورت *ها» توسند همجو «ظهیر الدولة و السعادة
والرفعة » چون در فارسی خواهند که بنوسند آنرا بی الف و لام و های
آتراشاعاق عبات و فت:هتعو اطی ول فسماوت و وت
وا کز ای کرد شوهتند نی املا خواهد بو و هر کاه که «ازنشاءاط
تعالی» و «عن قریب» در عدارت عربی نویسند نفصل باید نوشت و چون
در فارسی بنوسند متصل » چه فارسی زبانان این کلمات را باك لفظ
می‌دانند .
دیگر هر گاه در کلمه ای نون وبای ابجد پپلوی هم بوده باشد "
سیب ضرورت شعری با قافیه هر دو را قلب بمیم کنند همجو « خنب »
وادئب؟واستب* و«خنبره*. | ن راخم‌ودم وسم‌وخمره بنویسند.وا گرضرورت
فناغد بحال خود ناد گذاشت که ال افسته.
دییگر در بیان الفاظی که مخصوص آدمی و ذی روح و غیرذی‌دوح
است . بدانکه لفط « او »و لفط « وی » اشاره بانسان و |دهیست ‏ و لفط
«آن» و داین» بغتر انسان وادمی . و اکر کلمةٌ «بر» يا کلمةٌ « در »
بر لفظ او و لفط هوی» در آورندب-ویغیر انسان و آدمی‌نیزراجم‌هیساز ند
لیکن در نظ چنانکه کفته‌اند. مصراع» :
چرخ فانوس خبال و عالمی حیران در او .
ودر نثر جایز نیست. و ذی‌روح‌را بالف و نون جمع کنند همجو
۱ چش: باشند.
ا لغاظ
مغصوص آدمی و دی روح وغیر ذی روح
--- BQT v1 leaf 255 tail
قتایی اد که اتتوزی و فا کففد اسخ 9 :
آشنا گر « بفتم کاف فارسی و سکون
۱ کند بیستر. جندبادستر , قندقیری* مخزن الادوبه » : فسطوریون 1251076120
«لت نایه» و رله ؛ شنها ۱ : ۲۸۷ ‌ و ۲۹۵ ج. بهلوی م29۳۵ «منای ۱۵۸: ۲
« دعارله ۱۸۹ ۰ . ۴ - مرکب اژ: پیشوند 2 ور اوستابی و پارسی باستان 1807
بمعنی شناختن « بارتولمه ۵۵4 > پهلوی 250086 « متون پهلوی ٩۸‏ *: « منای۲۹۸ *.
۴ - مرکب از : پشوند 2 + اوستابی 502 شنن » ساسکربت 5020 , حاشا20۵ ,
اسنی شرقی 9818 .استی غربی 257100 ۲ «بارنولمد ۱۹۲۸ - ۲٩‏ پهلوی 50۵1 , 51020
* دیشکرت ۰۷۵۹ ۷۹۰ * در پارسی شنا » شناو ؛ شناب » شناء , شنار » آشناء » آشناب » و در
ت کب آشناور و آشناگر و شناور و شناکر دیده مشود . در طبری 925۷1 , مازندرانی کنونی
ور 98110 « واژه نامه ۳۰۸ » . ۵ _ ره : آشنا .
ه آشتی _ پهلوی الم « مررکب از 2506 بمشی صلح و آرامش . دراوستا
کم < بارئولیه ۰۲۳۹۹ بر کب ۰۲۵ وا[ نثانٌ حاصل مصدر . هب آشفتن _
م رکب از "پیشوند 2 و1510800 اوستائی بمعنی مضطرب شدن ۰ نحريك شدن, در سانسکربت
6 د«بارنولمه ۲ ۵۶» خشم کرفن » مشب کردن - شوریدن . انقلاب . - بهیجانآمدن .
«لغت ناعد». آشکارا_ بپلوی 1 هسمنای۲۱۸» « تب رکگ۲۵ * اوراعالی
[25016872 «2 . اورامان ۱۲»؛ صریح » بی پرده - علایه ؛ مقابل‌س . ه آشکاره _
بپلوی 251162721 دنب رکه۲»؛ آشتارا : «ستارگان همیشه پنهان وهميشه آشکاره کدامند؛ »
«التفهیم۸ ۱۷و همیشهآشکاره راییرونی درترجمةٌ «ابدی‌الظور» آورده است. . ه آشموغ _
رك : آسموغ . - نیزشری , فریفتار : این شاخبشاه اردشیر باسواران سلاح پوشیده گرد ی کط
آنشگاه نگاه میداشت نانه که آشموغی با عثافقی پنهان چیزی بر وبراف کند « مقدمهٌ اردا
ویرافنامه ترجمةٌ قدم » « اروا ویرافتامه بقلم نگارنده ۱۲-۱ »
--- ref_page options
```


## [2026-09-04T18:13:05.070Z] TOOL CALL #23: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1225.png"
}
```


## [2026-09-04T18:13:05.647Z] TOOL CALL #24: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ARY/0051.png"
}
```


### [2026-09-04T18:13:05.668Z] TOOL RESULT

```

```


## [2026-09-04T18:13:05.665Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


### [2026-09-04T18:13:06.227Z] TOOL RESULT

```

```


## [2026-09-04T18:13:06.225Z] INPUT

[Image: original 1500x2400, displayed at 1250x2000. Multiply coordinates by 1.20 to map to original image.]


## [2026-09-04T18:13:10.403Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA; echo '--- PLA leaf 37 (p.22)'; awk 'BEGIN{RS=\"\\f\"} NR==37' PLA_pages.txt | sed 's/  */ /g' | grep -v '^ *$' | head -60; echo '--- PLA leaf 42 (p.27) ambiq part'; awk 'BEGIN{RS=\"\\f\"} NR==42' PLA_pages.txt | sed 's/  */ /g' | grep -v '^ *$' | tail -25; echo '--- PLA leaf 43 (p.28) head'; awk 'BEGIN{RS=\"\\f\"} NR==43' PLA_pages.txt | sed 's/  */ /g' | grep -v '^ *$' | head -12; echo '--- PLA grep'; grep -n -i -E 'ibr[iī]q|abr[eēi]z|ambiq|anbiq|nīk|gul[aā]b|ǧul[aā]b|julāb' PLA_pages.txt | cut -c1-200 | head -12",
 "description": "Asbaghi pp.22, 27-28 and greps for ibrīq/ambīq/julāb"
}
```


### [2026-09-04T18:13:12.208Z] TOOL RESULT

```
--- PLA leaf 37 (p.22)
”isbahän 22 ° 1sfähän
 5
olywri - ”isbahän: eine Stadt in Persien. s. ”isfähan .
2tlg»>1 - ”isbahänak: eine Ortschaft bei Isfahan !.
 3
 . s -
_slyeri- ”’isbahäni: Nisba v. ”’isbahan .
 3
ie ’isbahbad: eine Burg in Sistan ® s.’isbahbad u. ’isfahbad .
alas! - ”isbahbadän: Titel der Emire von Tabaristän °-
 s
 s 3
 Sy - ’isbahbadiyya: Währung im Irak. pers. *.
 3
-V\.err1 - "isbahsalär = ’isfahsalär s. ”’isfahsälär .
 5 . - -
 Ebaei - ’isbidbäß: "Eintopf" pers. > 5 ?isbidbäß .
 . s _ _ - _ _ _
 Eb aeet - ’isbiabäp = ’isbIdbäg s. ’isbidbag ®.
 >
rl - ’asräm: Pl. v. sarm s. sarm 7,
 \ 5
Er - ’istahr: eine Stadt in der Provinz Fars im Iran.
 s - 2 1= -
 Se - istahrI: Nisba v. _»4s1 ’istabr, ”abü-Hätam ”istahri ®.
&blgEol - ”igtehbänät: ein Ort im Osten v. Schiraz, Hauptstadt v. Fars. °
 ’
 ol, - ”ustuwäna = ”’ustuwäna s. ”ustuwäna 10,
 . s - _ - - - -
Gel _ ’isfähän = ’isfähän s. ’isfähan .
1. LD. s. v.
2. ebda.
3. ebda.
4. Addai Scher s. v., FN. Ss. v.
5. TaCalibi s. v.
6. ebda.
7. Wahrmund Ss. v.
8. al-MuCarrab s. v.
9. LD. s. v.
10. Muhit s. v.
--- PLA leaf 42 (p.27) ambiq part
 ’
 —mp.>r hanbar ap. hambara 4 syr. fyaatlao 5,
 .$
ol - ”anbar = “anbar s. “anbar .
 „5 - _ _
ob 21 - ”anbarbäris = ’ambarbäris s. ”’anbarbäris .
au) -
 s
 ’anba: "Mango" aus dem pers, as] anbe m. 2 ambag 6, syr.Nest
 7
 ..3 -
=>! - ”ambig: "Alembik" pers. ®, mand. anpaga (iranian, talm. xmyıx ) 9,
 syr. anı 10, sp. alambique, engl. alembic, frz. alambic, dtsch.
 Alembik "Destillierkolben" 11, wahrscheinlich aus dem pers. ‘«_7T äbnik.
1. al-Marfa® s. v., Addai Scher s. v.
2. Nyberg Bd. II s. v.
3. Wahrmund Ss. v., al-MuCarrab s. v.
4. Bartholomae s. v., Mayrhofer s. v.
5. Brockelmann s. v.
6. Hosrow Qobädän n. Chista 9. S. 1072
7. Brockelmann Ss. v.
8. al-Mundid s. v.
9. Macuch Ss. v.
10. Brockelmann s. v.
11. Wildhagen s. v.
--- PLA leaf 43 (p.28) head
> ank 28 ’unmüdal
lası - ’infibär: " eine Pflanze; Bistro" pers. 1,
Slası - ”’anfudän: "Sylphium, Laserpitium, Assafatida" pers. 2, aram. gl
ots - ”ankudan = ’anfudän s. ”ankudän ,
 : Fr
jeDi - "Anker" pers. 3 aus pers. _{J langar, mand. angara 4 lat. ancora.
 5
e,»1 - ”anfura: "Nessel" pers.
 5
del
 si -- ’angal:
 "ankal: "Alth ee, i
--- PLA grep
362:di:     pers.       b >          ar.        f z.         B.:     pers.    abriz    >          ar.    afriz
390:           pers.     2> ar.                2. B.: pers. SurI2   ar. IbrIq
555:>>!              -        abriz:             "pures              Gold,          Obryzum"               pers.      8, aus    dem    pers.      —.ı äb    "Glanz"         +
582:or!               -       ’ibrig:                "Gießkanne;                 Ibrik"     aus       dem    pers.    +1        abriz        a s.        äbriz,
1734:Ar              -       ’ ifriz:               "Regendach,                   Fries"             pers.,               aus       dem       pers.   ri   abriz        s.   abriz   ı
1888: amirabür                                                                                      27                                                             ambiq
1929:              syr.             anı            10,       sp.       alambique,              engl.        alembic,           frz.       alambic,         dtsch.
4056:tärig                                                                       68                                                   tabriz
4089:re         - tabriz:                  "Tisch"        pers.       !° ‚„ wahrscheinlich               aus    dem    pers,   Be      tabarzad
4112:tabriz                                                                  69                                                        tabt
4117:Sp          - tabrizi:               Nisba v. tabriz.
6509:ae            - bambiq:                  "Keller           aus       Holz    mit       gewölbtem        Dach"   aus        dem     pers.     £ ham
```


## [2026-09-04T18:13:13.218Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in '^آب ' '^آب:' 'آفتاب:' 'آبادان:' 'آخور:' 'آبریز' 'زهاب:' 'گلاب:' 'پنجاب' 'آبنیک' 'ناب:' '^ناب' 'انبیق' 'ابریق:' 'زاب:' 'آبان:'; do echo \"--- MON: $w\"; grep -n -m3 -E \"$w\" MON_part1.txt MON_part2.txt | cut -c1-260; done",
 "description": "Grep Mo'in for the Persian headwords"
}
```


### [2026-09-04T18:13:17.183Z] TOOL RESULT

```
--- MON: ^آب 
MON_part2.txt:1093:آب و مانند آن که به یک دم نوشند. (ص.) 
MON_part2.txt:1203:آب و امثال آن را از چاه و غیره به مدد آن 
MON_part2.txt:1240:آب با مایعی دیگر در گلو گردانیدن؛ 
MON_part1.txt:754:آب دهان؛ خدو. عصاره؛ شیره. عطر؛ عرق 
MON_part1.txt:771:آب آتش رنگ: شراب لعلی. اشککك 
MON_part1.txt:794:آب استاده: ات استاده. اب‌باده رنگ: 
--- MON: ^آب:
MON_part1.txt:949:آب: ,1 )1( نام ماه پنجم 5 پاز دهم سالماه 
MON_part1.txt:25451:آب: سدی که جلو آب بندند. بند ارباب: 
MON_part1.txt:92431:آب: طراز کردن آب؛ برابر کردن ۳1 
--- MON: آفتاب:
MON_part1.txt:3758:آفتاب به آفتاب: رم 
MON_part1.txt:3762:پنجةٌ آفتاب: بسیار زیبا. آفتاب به گل 
MON_part1.txt:32812:خورشد. رخسار» عارض. مثل پنجهٌ آفتاب: 
MON_part2.txt:26359:آن را محدود کر ده است. کمر آفتاب: خطی 
MON_part2.txt:38513:اسمی: لب آفتاب: شعاع آفتاب که متصل به 
MON_part2.txt:71433:ترکیات اسمی: ناخن آفتاب: (کد.) اشعة 
--- MON: آبادان:
--- MON: آخور:
--- MON: آبریز
MON_part2.txt:44977:آبریز» طهارت جای. چاه مبرز: چاه مستراح. 
MON_part1.txt:1463:آبریزان. نوعی از طعام. 
MON_part1.txt:6264:ابریق: ب:۰ [معر. آبریز] (.) ظرف سفالین 
--- MON: زهاب:
--- MON: گلاب:
MON_part1.txt:96867:عطر گل گلاب» عطر گل. عطر گل گلاب: 
MON_part2.txt:33810:گلاب: (گیا.) یکی از گونه‌های گل سرخ 
MON_part2.txt:34160:گلاب: «2ج (امر.) آب 1 
MON_part2.txt:34161:گلاب: 0-0 | - جلات؛ معر.] (امر.) ۳ 
--- MON: پنجاب
--- MON: آبنیک
--- MON: ناب:
MON_part1.txt:9214:اذناب: 22220 [ع. )1( ج. دنب. دم‌هاء 
MON_part1.txt:14147:اطناب: طاقماه [ع.] (مص‌ل.) دراز گفتن» 
MON_part1.txt:15984:اللناب: اقطله [ع. ۲۰ ج. لب؛ خردها» 
MON_part2.txt:31929:کرد. گره سر طناب: برای اینکه رشته‌های سر 
MON_part2.txt:65651:شدن, نیابت کردن. نایب مناب: جانشین؛ 
MON_part2.txt:71128:ناب: ۰-20 [(ب ی آب» بدون آب)] (ص.) 
--- MON: ^ناب
MON_part1.txt:1681:نابا کك» هو کشیدن. آب کشیدن غذایی: 
MON_part1.txt:4292:نابا کی. عادت زشت مانند عادت به افیون با 
MON_part1.txt:17293:نابودی. 
MON_part2.txt:6267:نابود کردن] (فرسوده فرساید» خواهد 
MON_part2.txt:6271:نابود کردن. کاستن» کم کر دن. لکد ردن. 
MON_part2.txt:26597:نابینا گر دیدن. (امص.) کوری (مادرزادی و 
--- MON: انبیق
MON_part1.txt:17169:انبیق: مارا [غ. معر.] (ا.) ظرفی است برای 
--- MON: ابریق:
MON_part1.txt:6264:ابریق: ب:۰ [معر. آبریز] (.) ظرف سفالین 
MON_part1.txt:6270:ابریق: بطم [معر . ابری. ابر بز ] (ا.) شمشیر 
--- MON: زاب:
MON_part2.txt:36173:گوزاب: (22۷2-20)860۷ (امر .) آشی که از 
MON_part2.txt:53094:مرزاب: ۱62-0 [<- مرزات» معر.] .( 
MON_part2.txt:70160:میزاب: 7-2] ۱2۱ [ مت ات» معر. فتنز انتا] 
MON_part1.txt:7923:احسزاب: 0قتاه [ع.] () ج. حسزب. 
MON_part1.txt:45587:تیزاب: تا (امر.) (شیم.) مایعی است 
MON_part1.txt:58580:خیزاب: 212-20 (امر .) موج» کوهة 11 
--- MON: آبان:
```


## [2026-09-04T18:13:19.527Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; echo '--- ARY latin index'; grep -n -E '^ *(AB|ĀB|NAB|NĀB|ABRIZ|ĀBRIZ|AFTAB|ĀFTĀB|AKHOR|ĀKHOR|ABADAN|ĀBĀDĀN|GOLAB|GOLĀB|PANJAB|PANJĀB|ZAHAB|ZAHĀB|ABAN|ĀBĀN|ASIAB|ĀSIĀB)\\b' ARY_latin_index_pages.txt | cut -c1-160 | head -20; grep -n -i -E '\\b(nab|abriz|aftab|akhor|abadan|golab|panjab|zahab)\\b' ARY_latin_index_pages.txt | cut -c1-160 | head -12; echo '--- ARY pages headwords'; for w in 'آفتاب' 'آبادان' 'آخور' 'ناب' 'گلاب' 'پنجاب' 'زهاب' 'آبریز' 'آبان' 'آسیاب'; do echo \"-- $w\"; grep -n -m3 -E \"^ *$w[ .۱-۹]|^$w$\" ARY_pages.txt | cut -c1-160; done; grep -n -c 'pdf page' ARY_pages.txt",
 "description": "Grep Aryanpur index and pages for the headwords"
}
```


### [2026-09-04T18:13:21.295Z] TOOL RESULT

```
--- ARY latin index
782:AB eB ree SBE EVV 6) cle calS Ab J (53910 JV Dees
1164:AB SET JS ons ste 59 (Gps Sica Say esl ') 65 pis Dltatls Lg as
1358:AB, AP (PAHLAVI) 6 shy,
7685:AB at MT Obs 22 ls cal ee
1199:nab pleat oI Kis ew go SB bagi cal pale obs sbeedly 5 Babes 209" 2? Bay
14751:NEFA (OLD ENGLISH) oS po! NAB (PAHLAVI) 5 3h
--- ARY pages headwords
-- آفتاب
(eval):1: bad floating point constant
-- آبادان
(eval):1: bad floating point constant
-- آخور
(eval):1: bad floating point constant
-- ناب
(eval):1: bad floating point constant
-- گلاب
(eval):1: bad floating point constant
-- پنجاب
(eval):1: bad floating point constant
-- زهاب
(eval):1: bad floating point constant
-- آبریز
(eval):1: bad floating point constant
-- آبان
(eval):1: bad floating point constant
-- آسیاب
(eval):1: bad floating point constant
545
```


## [2026-09-04T18:13:31.918Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; \necho '--- AFM'; grep -n -E 'ابريق|إبريق|انبيق|أنبيق|الإبريق|الأنبيق|جلاب|جُلاب' AFM_pages.txt AFM.txt | cut -c1-220 | head -10;\necho '--- AFA'; grep -n -i -E 'ibr[iī]q|amb[iī]q|anb[iī]q|ἄμβιξ|ambix|jul[aā]b|ǧul[aā]b' AFA.txt | cut -c1-220 | head -10;\necho '--- LKT'; grep -n -i -E 'alembic|alambic|alambique|julep|ibr[iī]q|anb[iī]q|ambix|Pandschab|Punjab|Pendschab' LKT.txt | cut -c1-260 | head -12;\necho '--- FVQ anbiq'; grep -n -i -E 'anb[iī]q|amb[iī]q|ambix' FVQ_pages.txt | cut -c1-200 | head -5;\necho '--- KLN'; grep -n -i -E '^(Punjab|Panjab|doab|abkari)|Punjab, ' KLN_1966.txt | cut -c1-300 | head -6;\necho '--- SKT'; grep -n -i -E '^(ALEMBIC|JULEP|Alembic|Julep)|alembic,|julep,' SKT.txt | cut -c1-300 | head -6;\necho '--- FSD'; grep -n -i -E '^ *a-lem.?bic|^ *ju.?lep|^ *Pun.?jab|alembic\\b.*\\[|julep\\b.*\\[' FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt | cut -c1-300 | head -8;\necho '--- WEB'; grep -n -i -E \"^ *ju.?lep|^ *Pun.?jab|julep, *n|Punjab, *n\" WEB_vol1.txt | cut -c1-300 | head -6;\necho '--- PHN'; grep -n -i -E 'ALAMBIC|JULEP|alambic|julep' PHN.txt | cut -c1-260 | head -6;\necho '--- DEV'; grep -n -i -E 'ALAMBIC|JULEP|alambic|julep' DEV.txt | cut -c1-260 | head -6;\necho '--- LAM'; grep -n -i -E 'ALAMBIC|JULEP|alambic|julep' LAM.txt | cut -c1-260 | head -6;\necho '--- DOZ'; grep -n -i -E 'alambiek|alembiek|julep|ALAMBIEK' DOZ.txt | cut -c1-260 | head -6;\necho '--- HJB'; grep -n -i -E '^ *(PUNJAB|JULEP|PANJAB|DOAB)|Punjab, |Punjaub' HJB.txt | cut -c1-300 | head -8;\necho '--- AID'; grep -n -i -E '^ *(Punjab|Panjab|Doab)|Punjab, ' AID.txt | cut -c1-300 | head -6",
 "description": "Grep Semitic and European dictionaries for alembic, julep, ibrīq, Punjab"
}
```


### [2026-09-04T18:13:32.302Z] TOOL RESULT

```
--- AFM
AFM_pages.txt:5433:(5١ نمه‎ابريق "
AFM_pages.txt:5689:ابريق ܪ
AFM.txt:8290:ابريق " 
AFM.txt:8634:ابريق ܪ 
--- AFA
5864:^Ujsoh Cast. 809 » Julabium" 1. ^Uffoh. Die echt grie-
--- LKT
1811:prov.  frz.  julep,  sp.  julepe,  pg.  julepo. Dagegen  in  der  uisprüngliclien  Bedeu- tung russ.  guljaf  'Hundsrose',  guljafnaja u'oda  'Rosenwasser'.  [DE  293.  Eguilaz 434.  Devic  DEt  146.  ML  395"2.  Gor- jajew  84.
3047:Medizinischer  Fachausdruck,  eigentlich 'was  man  aufleckt',  d.  h.  in  kleiner  Dosis nimmt  [vom  Vb.  la'aka  'lecken'],  syno- nym zu  ralat.  eclegma  und  linctus;  hier- aus pg.  looch  [mit  k  gesprochen,  Con- stancio Dicc  662  b],  lohoc  
3704:'Fünf  [Horn  NpEt  S.  73,  Nr.  328;  vgl. päng-äb  'Pandschab',  engl.  Schreibung Punjaub  'FOnfstromland'] ;  hieraus  engl. punch,  dtsch.  Punsch,  ein  Getränk,  das aus  fünf  Zutaten  hergestellt  wird:  Arrak, Zucker,  Zitronensaft,  Wasse
6207:alambic  79
6210:alambique  79
7423:Aegidius  951 aegyptus  1222 alambicum  79 alchanna  867 algorismus  890 algorithmus  890 alleluia  793 ahnageshim  1348 almutium  1520 amaracum  1411 amen  68
8292:julepo  742
8522:julep  742
8598:alambic  79
9796:arfor  501 adraja  485 aduana  526 aduar  502 adufa  538 adufe  537 agengibre  1930 oguajaque  2168 aguanafa  1535 ahorrar  886 ajarafe  1840 «;e&e  1735 ajedrea  1872 ajedrez(atama)  1871 ajimenez  1815 ajimiz  1816 ajonjoU  744 ajorca  1951 ajovar  195
--- FVQ anbiq
--- KLN
--- SKT
527:Alembic,  0  vessel  for  distilling.  (F  — Span.-Arab.-Gk.)  M.  E.  aUpthk."?. altxmhique  (Cot.)  •  Span,  alambiqut.  — Arab.  tU,  the;  and  antik  (pronouncctl  am' ink's,  a  still.  —  Gk.  li/i^i^.  a  cup,  goblet; can  of  a  GtjU.-Gk.  &^^,  4l/i^<vr,  foot  of  a goulct ;
--- FSD
FSD_vol3.txt:8572:Punjab. 8. W Himalayas. 1,200 sq m. 2. Its capital,
FSD_vol4.txt:22731:packed  Compare  stilling stll"la-tl'tIoust,  a   TrlcHlng  in  drops  or  drawn  b>  a   still stin.i-to-r}t,  n   1.  A   dlstuilng-vcsscl,  an  alembic  2.  A still-room  laboratorj  stll'II-to-rj  ! still 'er*,  1   stil'or,  2   stn'er,  n   1.  One  who  or  that  which sti
FSD_vol4.txt:64063:Julep,  jOnep  C   E   Af  S   TF ,   2   3,  4   5,  6,  7,
FSD_vol4.txt:87224:Punjab  States
FSD_vol1.txt:65381:Punjab.  onychidx.  Chlt'ra*,  n.  (t.  g.)  [<  chitra».]  mas.
FSD_vol2.txt:40989:Punjab,  British  India.
FSD_vol2.txt:76601:llm'bec,  lllm'bek:2Um'b6e,  71.  1.  Her.  A   bearing  represent- ing an  alembic.  3t.  A   still.  [Contr.  of  alembio.1  liin^-
--- WEB
102769:ju/lep, 7. [Fr. julep; Sp. julepe; Ar. julab; Per. ‘alab, gūlāb, julep, rose water; gul, rose, and ab, water. a 3 i a cool drink containing aromatic herbs.
--- PHN
1052:différence qui existe entre : alambic et vase à distillation; —
1095:ALAMBIC, s. m. (a.-gr.)
1098:cordent à regarder alambic comme la transcription du grer
1791:distillation à l'alambic; précédé de ^^j \rotW]esprit, <S^I ^jjARH 43
6310:JULEP, s. m. composé, (a.-p.)
10646:Julep, s. m. composé, (a.-p.) 991
--- DEV
270:Alambic  Esp.  alamhique,  port,  lamhique,  itai.  lambico, de  l'arabe  (^^^^j^î  al-anhiq,  venant  du  grec  a^^i^^  vase  à distiller,  précédé  de  l'article  arabe  al.
1581:JuLEP.  Esp.  et  portug.  jidepe;  ital.  giulebbo,  giidebbe; bas  latin ,  julapium.  De  l'arabe-persan  <-->!^:^  djoulâb  ou djoullâb,  qui  a  le  même  sens,  cdls  font  une  potion.  .  . (ju'ils  donnent  au  malade  et  qu'ils  appellent.  
2403:Alambic.
2404:Alambique,  esp.  voy.  Alambic.
2698:Afxé'/^,  voy.  Alambic.
3574:Giulebbe,  ital.  voy.  Julep.
--- LAM
1610:feit poui» almageste, alchimie, alambic, c'est-à-dire qu'ils ont accolé leur
4694:Julep. Esp : julepe. Ptg: julepo. Majorq : culepe It :
4716:fie bi-euvage (iom. Le julep lies Anciens (■toit beaucoup plus auorà qui la
6982:rencontre plusieurs termes d'alchimie, les éîixirs obj-TV» » les alambics
9202:Julep
--- DOZ
2636:ook onder julepe o xarope en lamedor que lame el
--- HJB
141:It  bas  been  already  intimated  that,  as  the  work  proceeded,  its  scope  ex- panded somewhat,  and  its  authors  found  it  expedient  to  introduce  and  trace many  words  of  Asiatic  origin  which  have  disappeared  from  colloquial  use, or  perhaps  never  entered  it,  but  whic
1149:Punjab  Plants,  comprising  Botanical  and Vernacular  Names  and  Uses,  by  J.  L. Stewart.    Lahore,  1869.
5853:Citantts),  which  English  people  also bitually  miscall  sycamore,  ana  Scotch people  miscall  plane-tree  !  Our  quota- tions show  how  old  the  confusion  is. The  tree  is  not  a  native  of  India, though  there  are  fine  chindrs  in  Eash- mere,  and  a  few  in  old  native  ga
6016:CHICK0BE,8.  The  red-legged  part- ridffe,  or  its  close  congener  Caccahis chvJeor,  Gray.  It  is  common  in  the Western  Himalaya,  in  the  N.  Punjab, and  in  Afghanistan.  The  francolin  of Moorcrof  t^  Travels  is  really  the  chickore. The  name  appears  to  be  Skt.  chdkora
6318:CHOOIiIA,  s.  €kulid  is  a  name given  in  Ceylon  and  in  Malabar  to  a particular  class  of  Mahommedans,  and sometimes  to  Mahommedans  generally. There  is  much  obscurity  about  the origin  and  proper  application  of  the term.  fThe  word  is  by  some  derived from  Skt  ck
7039:C0MMI88I0NEB,s.  In  the  Bengal and  Bombay  Presidencies  this  is  a ffrade  in  the  ordinary  administrative hierarchy  ;  it  does  not  exist  in  Madras, but  is  found  in  the  Punjab,  Central Provinces,  &c.  The  Commissioner  is over  a  Division  embracii^  several Districts  or 
8717:DHAWK,  s.  Hind.  dhOk;  also called  palds.  A  small  bushy  tree,  BuUa frondota  (N.  O.  Legurwinowy,  which forms  large  tracts  of  jungle  in  the Punjab,  and  in  many  dry  parts  of India.  Its  deep  orange  flowers  give a  brilliant  aspect  to  the  jungle  in  the early  part
8899:DOAB.
--- AID
```


## [2026-09-04T18:14:44.417Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA; for L in 555 582 1929; do awk -v L=$L 'NR<=L && /\\f/{n++} END{print \"line\",L,\"-> leaf(1-based)\",n+1,\"printed\",n+1-15}' PLA_pages.txt; done; sed -n 553,560p PLA_pages.txt | sed 's/  */ /g'; sed -n 580,586p PLA_pages.txt | sed 's/  */ /g'; echo '--- bnik / gulab'; grep -n -i -E 'bnik|bn[iī]k|[ǧgğ]ul[aā]b|ulläb|ǧulläb|gulläb' PLA_pages.txt | cut -c1-200 | head -8",
 "description": "Asbaghi: pages of abrīz/ibrīq entries, search ābnīk and julāb"
}
```


### [2026-09-04T18:14:46.575Z] TOOL RESULT

```
line 555 -> leaf(1-based) 17 printed 2
line 582 -> leaf(1-based) 18 printed 3
line 1929 -> leaf(1-based) 42 printed 27
 - -_
 -..-
>>! - abriz: "pures Gold, Obryzum" pers. 8, aus dem pers. —.ı äb "Glanz" +
 riz s. äbriß, targ. srrÄsıy-
 .
 Ser!- Bbrizi: Nisba v. BAU äbriz s. äbriz..


 "Seidenhändler" q. v.
 5 _ 7 z
or! - ’ibrig: "Gießkanne; Ibrik" aus dem pers. +1 abriz a s. äbriz,
 syr. se} 5, dtsch. Ibrik "im Orient Wasserkanne mit dünnem Hals und
 ovalem Bauch" pers. 6,

 8 - = _-
--- bnik / gulab
1930:              Alembik                   "Destillierkolben"                           11, wahrscheinlich                     aus       dem     pers.    ‘«_7T äbnik.
```


## [2026-09-04T18:14:48.661Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; echo '--- NAB latin index page'; awk 'NR<=14751 && /pdf page/{p=$0} END{print p}' ARY_latin_index_pages.txt; sed -n 14749,14753p ARY_latin_index_pages.txt | cut -c1-200; echo '--- latin idx other'; grep -n -i -E '\\b(aftab|abadan|akhor|akhur|golab|gulab|panjab|zahab|abriz|asiab|aban)\\b' ARY_latin_index_pages.txt | cut -c1-160 | head -12; echo '--- ARY pages'; for w in آفتاب آبادان آخور ناب گلاب پنجاب زهاب آبریز آبان آسیاب; do echo \"-- $w\"; grep -n -F \"$w\" ARY_pages.txt | awk 'length($0)<60' | head -4 | cut -c1-120; done",
 "description": "Aryanpur: find pages for nāb and other headwords"
}
```


### [2026-09-04T18:14:50.817Z] TOOL RESULT

```
--- NAB latin index page
[pdf page 505]
NEVO :(OLD HIGH GERMAN) <5 git NAPAT, (OLD PERSIAN) Skul os),
NEEFE (GERMAN) gla NAPA
NEFA (OLD ENGLISH) oS po! NAB (PAHLAVI) 5 3h
NEPHEW ENGLISH) aS). NEVI (KURDISH) 52,5
NEVE (DANISH) Sails NAPAT (SANSKRIT) 4 Sasle
--- latin idx other
--- ARY pages
-- آفتاب
-- آبادان
-- آخور
-- ناب
2950:اسلاوی کهن (8677نابل) 2ا0):
8412:اسلاوی کهن (۲12ما5 #77نابل صا0): ۸0
9996:اوسنابی (48724/4): ادا
13302:بلوچی (ا8نابله8): 1 ردان
-- گلاب
-- پنجاب
-- زهاب
-- آبریز
-- آبان
-- آسیاب
```


## [2026-09-04T18:14:53.853Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '--- MON āb 745-760'; sed -n 745,760p MON_part1.txt | cut -c1-200; echo '--- MON āftāb'; grep -n -E '^آفتاب' MON_part1.txt | head -3; grep -n -E 'آفتاب: ' MON_part1.txt | head -3; echo '--- MON ābādān/āxor/zahāb/panjāb'; grep -n -E '^(آبادان|آخور|آخر|زهاب|پنجاب|آبان|آبریز|آسیاب)' MON_part1.txt MON_part2.txt | cut -c1-220 | head -12; echo '--- MON golab'; sed -n 34158,34164p MON_part2.txt | cut -c1-220; echo '--- MON nab'; sed -n 71126,71131p MON_part2.txt | cut -c1-220; echo '--- MON abriz'; sed -n 44974,44979p MON_part2.txt | cut -c1-200; grep -n -E 'آبریز: ' MON_part1.txt MON_part2.txt | head -3",
 "description": "Mo'in entries for āb, āftāb, ābādān, golāb, nāb, ābrīz"
}
```


### [2026-09-04T18:14:54.040Z] TOOL RESULT

```
--- MON āb 745-760
مشدی حسن (اقا مشهدی حسن). 
اثروپلان: 1۳0 ((.) هو اییما. 

اب 0 (1.) مایعی است شفاف» بی‌طعم و 
بی‌بو؛ مر کب از دو عنصر اکسیژن و تیدرژن. 
نشانه آن در شیمی ۵۵است و آن به عقند ه 
کار و موب تیف 
مق. آتش. دریا» بحر؛ مق. خش؟ می» بر . رو ده 
نهر. اشکد» سر شکث. عرق؛ خوی. سزاق» 
آب دهان؛ خدو. عصاره؛ شیره. عطر؛ عرق 
۳ . مسنی » آنبه نفت: شاب ادرار. 
طراوت. لطافت؛ تری» تکار که صفا؛ 
رخ کی جلا. رونق» رواج. اترف 
عزت؛ شرف. روش طرز» گونه. نوع. 
حقیقت روحانی؛ ج. آب‌ها؛ آبان (فقط در 

--- MON āftāb
3758:آفتاب به آفتاب: رم 
3759:آفتاب سر دیوار: بری نزدیک به مرگگک. 
3760:آفتاب لب بام: کسی که عمرش نزدیکث به 
3758:آفتاب به آفتاب: رم 
3762:پنجةٌ آفتاب: بسیار زیبا. آفتاب به گل 
32812:خورشد. رخسار» عارض. مثل پنجهٌ آفتاب: 
--- MON ābādān/āxor/zahāb/panjāb
MON_part2.txt:6846:آخر رسانیدن خوانندگی و آن سا 
MON_part2.txt:6869:آخر سال؛ خمسه مستر قه. 
MON_part2.txt:8259:آخرین مرحلةٌ زنبدگی این کرم بیدا می‌شو د. 
MON_part2.txt:9686:آخرین مسابقة ورزشی. (مس.) آخرین 
MON_part2.txt:10534:آخر ابیات دیگر تکرار نشود. بٍ رن | کنو 
MON_part2.txt:10537:آخرین كلمةٌ اصلی و غیره مکرر بیت (یا 
MON_part2.txt:14789:آخرین بازی نرد است که کسی بر سر خود يا 
MON_part2.txt:17190:آخر همین که سفت شد برداشته با کشک با 
MON_part2.txt:19899:آخر که عاقت» که بالا خر ه. 
MON_part2.txt:40122:آسیابه گردش درآید. سر آن چوب 
MON_part2.txt:40975:آخرالامر مقداری مغز بستة خرد کرده و 
MON_part2.txt:43363:آخر شباط (زمستان) آذار» نیسان؛ ایار 
--- MON golab
گل آلود: ۳ | - گل آلوده| ( (رص مف.) 
گل آلوده. خم گل آلود: ( کد.) کر 5 زمین 
گلاب: «2ج (امر.) آب 1 
گلاب: 0-0 | - جلات؛ معر.] (امر.) ۳ 
که از گل سرخ استخراج کنند و معطر است. 
آبی که از هر نوع کل استخراج کنند. گلاب 
چشم: ر کته اشکته بت شکت: کلارت شک( 
--- MON nab
عمل کند؛ ناخلف؟ ج. نااهلان. 

ناب: ۰-20 [(ب ی آب» بدون آب)] (ص.) 
خالص» بی‌غش. محفضص» صرف. 

ناب: 250 [- ناو ] (ا.) ناو عموما. فرورفتگیی 
--- MON abriz
خنکك کتنده. (بز.) بایین آورندهة درجه 
حرارت بدن. (بز.) کاهندة تمابلات جنسی. 
مبرز:. 2جصه [ع.] (۱.) ممال؛ مستراح؛ 
آبریز» طهارت جای. چاه مبرز: چاه مستراح. 
مبرز: ۱9۱0۳2 [ع.] (اسف.) ظاهر شده» 
هو بدا شده.
```


## [2026-09-04T18:14:56.413Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '--- LKT 79'; grep -n -E '^ *79\\. ' LKT.txt | head -2; grep -n -B2 -A6 -i 'anbīq\\|anbiq' LKT.txt | cut -c1-300 | head -24; echo '--- LKT 742'; sed -n 1804,1812p LKT.txt | cut -c1-300; echo '--- LKT 3700'; sed -n 3700,3706p LKT.txt | cut -c1-300",
 "description": "Lokotsch entries for alambic, julep, punch/Pandschab"
}
```


### [2026-09-04T18:14:56.491Z] TOOL RESULT

```
--- LKT 79
398:79.  Ar.  anbik:
--- LKT 742
740.  Per^.  gul:
'Rose'  [Horn  NpEt  S.  206,  Nr.  927],  tk. gill ;  hieraus  bulg.  gul,  serb.  dzul  'Rose'.
741.  Ar.  gül:
Ein  Wüstengeist,  die  Mitte  zwischen Mensch  und  Ginn  [s.  hier  Nr.  723]  hal- tend, mit  menschlicher  Gestalt  und Eselsbeinen,  doch  häufig  seine  Gestalt wechselnd  [Lammens  Farük  870] ;  hier- aus frz.  la  goule  'ein  Ungeheuer';  aus dem  ar.  plr.  gailän  ergab  sich  frz. g
742.  Pers.  guläb: 'Rosenwasser'  [aus  pers.  gul  'Rose',  s. hier  Nr.  740,  und  ab  'Wasser',  s.  hier Nr.  5],  ebenso  ar.  guläb,  vulg.  guleb; hieraus  m\2L\..  jidapium  'eine  Art  Sirup, Kühltrank',  li.giulebbe,  giulebbo,giuleppo,
59
[Hebr.  gulgolQd.
prov.  frz.  julep,  sp.  julepe,  pg.  julepo. Dagegen  in  der  uisprüngliclien  Bedeu- tung russ.  guljaf  'Hundsrose',  guljafnaja u'oda  'Rosenwasser'.  [DE  293.  Eguilaz 434.  Devic  DEt  146.  ML  395"2.  Gor- jajew  84.
743.  Hebr.  gulgöl§ö:
--- LKT 3700
pzJimnr  'langer  Strick';  rum.  pälämar 'Ankertau',  it.  palamaro  'dass.'.  [Löbel EITAP  73.    Mikl  SIEtWb  230.
1617.  Pers.  piiiibä: 'Baumwolle',  hieraus  tk.  pembe  'dass., rosafarben';  hieraus  rum.  pambria 'Schafwolle',  jmnbeii  'blaßrot'.  Aus  der pers.  Form  pänbäk  ergaben  sich  tk. pambuk  'Baumwolle'  und  gr.  udiußaE, ■iraiißdKiov  'dass.';  hieraus  rum.  bumbac, buig.  bubak,  s
1618.  Telugn  paudi-kokkn: 'Schweine-Ratte'  Mus  melabaricus,  eine große  Ratte,  die  über  ganz  Indien  und den  malayischen  Archipel  bis  nach Queensland  verbreitet  ist  und  deren Fleisch  ein  Lieblingsgericht  der  Kulis ist;  hieraus  angloind.  bandicoot,  engl. 6aM(?tcoo;'pig-rat'
1619.  Pers.  päng:
'Fünf  [Horn  NpEt  S.  73,  Nr.  328;  vgl. päng-äb  'Pandschab',  engl.  Schreibung Punjaub  'FOnfstromland'] ;  hieraus  engl. punch,  dtsch.  Punsch,  ein  Getränk,  das aus  fünf  Zutaten  hergestellt  wird:  Arrak, Zucker,  Zitronensaft,  Wasser  (oder  Tee) und  Gewürz  (Zimt)  [SCHILLE
1620.  Pers.  pängä:
'Faust'  [Horn  wie  hier  Nr.  1619],  tk. pence  'Handfläche' ;  hieraus  rum.  pingea 'Halbsohle',  pingelui  'wieder  besohlen' ; bulg.  pence,  serb.  pendze  'Sohle',  [Löbel EITAP  76.    Mikl  SIEtWb  238b.
```


## [2026-09-04T18:15:02.667Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '--- SKT julep'; grep -n -E '^Julep|Julep,' SKT.txt | cut -c1-300 | head -3; echo '--- FSD alembic'; grep -n -i -E \"a-lem.?bic|alembic, *n\" FSD_vol1.txt | cut -c1-300 | head -3; grep -n -i -E \"^ *ju.?lep|julep, *n|ju'lep\" FSD_vol2.txt FSD_vol3.txt | cut -c1-300 | head -4; grep -n -i -E \"Pun.?jab, *n|^ *Pun.?jab|Panjab\" FSD_vol3.txt FSD_vol4.txt | cut -c1-300 | head -4; echo '--- WEB Punjab'; grep -n -E \"Pun.?jab|Panjab\" WEB_vol1.txt | cut -c1-200 | head -3; echo '--- HJB'; sed -n 8899,8912p HJB.txt | cut -c1-300; grep -n -i -E 'Panj.?āb|Panj-?ab|five rivers|Punjaub' HJB.txt | cut -c1-200 | head -5; echo '--- AID'; grep -n -i -E 'Panj|Punj' AID.txt | cut -c1-250 | head -5; echo '--- KLN'; grep -n -E 'Punjab|Panjab|doab, n|abkari, n|punch, n' KLN_1966.txt | cut -c1-350 | head -6",
 "description": "Skeat, Funk & Wagnalls, Webster, Hobson-Jobson, Whitworth, Klein for julep/alembic/Punjab"
}
```


### [2026-09-04T18:15:02.974Z] TOOL RESULT

```
--- SKT julep
--- FSD alembic
FSD_vol2.txt:65496:Jn'lep,  1   ju'lep;  2   ju'lSp  (xin), n.  1.  A   drink  com  posed  usu- ally of  brandy  or  whisky,  sugar, cracked  ice,  and  some  flavor- ing, commonly  fresh  crushed g   r   e   e   ri  mint.  2.  A   subacid, mucilaginous,  sweetened  drink, often  used  as  a   vehic
FSD_vol3.txt:8572:Punjab. 8. W Himalayas. 1,200 sq m. 2. Its capital,
FSD_vol4.txt:87224:Punjab  States
--- WEB Punjab
90784:1. the group of Indo-European, Indic lan- guages spoken in northern India, including Assamese, Bengali, Marathi, Punjabi, Hindu- stani, etc.
101830:ety of terra-cotta invented and used by Josiah ja-rd/si. x Wedgwood, particularly for cameo effects. ro site, 2. [named from Barranco Jaroso, in jas’pér-y, a. having the qualities of jasper.
--- HJB
DOAB.
321
DOAR
forvaS  du  mot  Indien  Div,  qni  signifie  une lie.  D'Herbelot  ...  la  comond  aveo  Din, dont  la  Bituation  est  k  Ventr^  da  Golfe  de CsmheLyer-^D'AnvaU,  p.  40.
DOAB,  8.  and  n.p.  P. — H.  dodb^ *two  waters,'  i.e.  'Mesopotamia,'  the tract  between  two  confluent  rivers.  In Upper  India,  when  used  absolutely, the  term  always  indicates  the  tract between  the  Ganges  and  Jumna.  Each of  the  like  tracts  in  the  Punjab  has  its distin
DOAI!  DW7EI  Interj.  Properly H.  dohOij  or  dahdi,  Qujarati  cUmdnlf  an exclamation  (hitherto  of  obscure  ety- mology) shouted  aloud  by  a  petitioner for  redress  at  a  Court  of  Justice,  or  as any  one  passes  who  is  supposed  to have  it  in  rds  power  to  aid  in  render- in
*  It  will  be  seen  that  the  Indian  cry  also  appeals to  the  Prince  expreBsly.  It  was  the  wood  fortune of  one  of  the  present  writers  (Jl  B.)  to  have witoessed  the  call  of  Haro !  brouight  into  serious operation  at  Jersey.
X
Wilson  derives  the  exclamation  from doy  *two'  or  repeatedly,  and  hdi  'alas,* illustrating  this  by  tne  phrase  *  dohai tthdi  kamd,^  *to  make  exclamation  (or invocation  of  justice)  twice  and  thrice.* [Platts  says,  do-hdy,  Skt.  hri-haha,'  a crying  twice  "alas!"]  This  p
c.  1340.—**  It  is  a  custom  in  India  that when  money  is  due  from  any  person  who  is favoured  by  the  Sultan,  and  the  creditor wants  bis  debt  settled,  he  lies  in  wait  at  the Palace  gate  for  the  debtor,  and  when  the latter  is  about  to  enter  he  assails  him  w
1609.— "He  is  severe  enough,  but  all helpeth  not ;  for  his  poore  Riats  or  clownes complaane  of  Iniustice  done  them,  and  cry for  justice  at  the  King's  hands." — ffatckins, in  Purchas,  i.  223.
c.  1666. — "Quand  on  y  veut  arrdter  une personne,  on  crie  seulement  Doa  padecha; cette  clamour  a  autant  de  force  que  celle  de haro  en  Normandie ;  et  si  on  defend  h,  ^uel- qu'un  de  sortir,  du  lieu  oh  il  est,  en  dnant DOA  jxtdecha,  il  ne  pent  partir  sans  se
1834. — "The  servant  woman  began  to make  a  great  outciy,  and  wanted  to  leave  the ship,  and  cried  Dohaee  to  the  Company,  for she  was  murdered  and  kidnapped." — Tk« Baboo,  ii.  242.
DOAB,  n.p.  A  name  applied  to  the strip  of  moist  land,  partially  cultivated witn  rice,  which  extends  at  the  foot  of
832:and  the  Panjab,  with  notes  by  Major
1657:to  controL  Since  the  annexation  of the  Fanjab,  however,  they  have  ceased to  give  trouble.  The  Akalee  is  dis- tinguished by  blue  clothing  and  steel armlets.  Many  of  them  al
1737:AT.T.TLTA^  s.  This  appears  to  be  a stuff  from  Turkestan  called  (Turki) alchali,  alajah,  or  alftchah.  It  is thus  described  :  ''a  silk  cloth  5  yards long,  which  has  a  sort
1846:ALPEEN,  8.  H.  cUjnfiy  used  in Bombay.  A  common  pin,  from  Port. alfineU  {Panjab  N,  do  Q.,  ii.  117).
3041:B A 88 AN,  s.  H.  bdean,  'a  dinner- plate  ' ;  from  Port  bacia  (Panjab  N. (t  Q.  ii.  117).
--- AID
294:Adi  Gtranth.  [Panjdbi,  ddi,  the  first, and  granthy  book,  from  the  Sanskrit granthy  to  string  together.]  The first  and  principal  scripture  of  the Sikhs,  consisting  of  the  sayings  of the  first  four  gurus,  collected  by A
401:Akdli.  [Panjdbi,  from  the  Sanskrit,  a privative,  and  kdla,  time.]  Eternal or  immortal ;   the  name  of  a   body of  Sikh  devotees,  who  claimed  for themselves  a   direct  institution  by Govind  Singh,  the  last  guru.  They prof
424:AlhuwAliA.  [PanjAbi,  from  Alhu,  a village  on  the  left  bank  of  the  Bias.] The  name  of  one  of  the  Sikh  misls and  of  the  family  now  ruling  in KapurthAla.
515:Anjaman.  [Persian.]  An  assembly, a   society ;   as  the  Anjamaq-i-Panjdb, the  name  of  a   society  in  the  Panjdb for  the  revival  of  Oriental  learning and  for  discussion.  Among  the Pdrsis,  a   council  to  which  disputes conce
549:Ardin.  The  name  of  a   tribe  peculiar to  the  Panjdb ;   they  are  market-
--- KLN
```


## [2026-09-04T18:15:06.302Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '--- PHN alambic'; sed -n 1095,1104p PHN.txt | cut -c1-250; echo '--- PHN julep'; sed -n 6310,6318p PHN.txt | cut -c1-250; echo '--- DEV alambic'; sed -n 268,274p DEV.txt | cut -c1-250; echo '--- DEV julep'; sed -n 1581,1586p DEV.txt | cut -c1-250; echo '--- LAM julep'; sed -n 4694,4700p LAM.txt | cut -c1-250; echo '--- LAM alambic'; sed -n 1608,1612p LAM.txt | cut -c1-250; echo '--- DOZ'; sed -n 2630,2640p DOZ.txt | cut -c1-250; grep -n -i -E 'alambiek|alembiek' DOZ.txt | head -3",
 "description": "Pihan, Devic, Lammens, Dozy on alambic and julep"
}
```


### [2026-09-04T18:15:06.423Z] TOOL RESULT

```
--- PHN alambic
ALAMBIC, s. m. (a.-gr.)
(^Afj^lt [aUn^] Nom d'un appareil de chimie qui sert à la
distillation de certains liquides. — Les étymologistes s'ac-
cordent à regarder alambic comme la transcription du grer
i(x€t^y vase- à bords relevés, précédé de l'article arabe al. Cepen-
dant il est probable que les chimistes ont emprunté directe-
ment ce terme aux Arabes, qui sans doute l'avaient tiré de la
langue grecque. — Les Espagnols et les Portugais écrivent
alnmbique.
ALBUFÉRA, n. pr. (a.)
--- PHN julep
JULEP, s. m. composé, (a.-p.)
Lj'^k^ [djoulAb] et v^^ [djouUah] Potion médicinale, rafraî-
chissante, composée de fruits, de miel ou de sucre, et d'eau.
— Le terme arabe est une imitation du persan v^^^ [s^^^ |
eau de rose, formé de J^^ [gti/] rose, et de v' [àb] ^^u, à cause
de la couleur rosée que l'on donne habituellement à cette es-
pèce de breuvage. — De là viennent aussi l'espagnol et le por-
tugaisyu/epe, ainsi que l'italien gitdebbo et giulebbe.
JUPE, s. f. et JUPON, 8. m. (a.)
--- DEV alambic
AiGKEFO.  C'était  autrefois  le  nom  d'une  monnaie  qui avait  cours  en  France.  En  portugais,  xarajîm,  xerafim,  dé- signe une  monnaie  des  Indes  orientales,  que  Baumgar- ten,  au  commencement  du  xvf  siècle,  appelle  en  latin 
Si  aigrefin,  monnaie,  vient  de  achraji,  il  ne  serait  pas impossible  que  aigrefin,  homme  rusé,  en  vînt  également; c'est  par  cette  qualification  de  très-illustres  que  les  Arabes désignaient  les  plus  éminents  philosoph
Alambic  Esp.  alamhique,  port,  lamhique,  itai.  lambico, de  l'arabe  (^^^^j^î  al-anhiq,  venant  du  grec  a^^i^^  vase  à distiller,  précédé  de  l'article  arabe  al.
Alancabuth.  Terme  d'astronomie.  Partie  de  l'astrolabe. De  l'arabe  ci^^-aX^x)!  al-anhahoût,  dont  le  sens  propre  est l'araignée.  L'alancabutli,  en  effet,  rappelle  assez  bien  l'idée d'une  araignée  posée  sur  sa  toile  (dont 
6  DICTIOINNAIRE  ETYMOLOGIQUE
Albara  ou  Alboha.  Nom  d'une  espèce  de  ièpre  ,  dans  les anciens  traités  de  médecine.  De  l'arabe  ij^y^^  al-b(iras, la  lèpre,  cjui  a  donné  l'espagnol  alharazo  et  le  portugais alvaraz..
**•"  Albatros.  Ce  mot,  écni  aJgatroa  par  Flacourt  et  Dam- pier,  est  une  altération  de  l'espagnol  et  portugais  rt/c^fraz^ qui  désigne  le  pélican  onocrotale,  mais  fjui  a  été  appliqué à  plusieurs  autres  oiseaux  aq
--- DEV julep
JuLEP.  Esp.  et  portug.  jidepe;  ital.  giulebbo,  giidebbe; bas  latin ,  julapium.  De  l'arabe-persan  <-->!^:^  djoulâb  ou djoullâb,  qui  a  le  même  sens,  cdls  font  une  potion.  .  . (ju'ils  donnent  au  malade  et  qu'ils  appelle
Jupe.   Esp.  juba,  chupa,  veste,   aljuba ;  portug.  aljuba.
'    Voyage  en  Perse,  ôd.  Smith,  p.  33-3.
DES  MOTS  D'ORIGINE  OIUENTALE.  \lil
casai|iie  moresque;  ital.  gruppn.  De  l'arabe  iC.:^  (Ijoahha. (Voy.  Dozy,  Dkt.  des  vêt.  p.  107.)  cd^ar-dessus  le  caftan, les  Turcs  mettent  une  jitppe  ou  surtout  à  manches  très- courtes.  57  (Niebuhr,  Voy.  en  Arah.  p.  
K
--- LAM julep
Julep. Esp : julepe. Ptg: julepo. Majorq : culepe It :
giulebbo, ginlebbe de l'arabe ^>U goulâb ou goullâbj
eau de rose; sirop (i). Ce mot d'origine persane est
m i . . . ■ I i I I I <
(1) Sacy. Abdalîatif.ç. 317, note 12.ancien en arabe. On le trouve cité dans un iiadith attribué
à 'j^icha. [i).
K
--- LAM alambic
Eguilaz le dérive de « ^Ul( Kalendariam en R. Martin » (Glos. etimol. s. y.).
(2) On a prétendu qae les Ai*abes ont fait pour almanach ce qu'ils ont
feit poui» almageste, alchimie, alambic, c'est-à-dire qu'ils ont accolé leur
article à des mots grecs ou latins. Fort bien, mais cette opération aurait
laissé des traces, comme dans les mots cités. Or on ne connaît aucun ex-
--- DOZ
conserve of violets or roses or mulberries etc."
Siroop , stroop , zgn afkomstig van het Arab. woord
sjardb, dat Freytag alleen heeft in den zin van: drank,
bepaaldelgk wgn of koflSe. L: den zin van siroop staat
het reeds in een schrgver der 11« eeuw, namelgk bg
Bekrï, p. 3 ed. de Slane; Pedro de Alcala heeft het
ook onder julepe o xarope en lamedor que lame el
doliente (ons likpot), en Bocthor onder sirop (Marcel
geeft sjorba voor sirop en Roland de Bussy, Vidióme
d'Algerj p. 454, 't meervoud sjorbdt). Dit sjardb is
onveranderd in 't Sp. overgegaan, xarabe, b. v. bg
```


## [2026-09-04T18:15:10.233Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '--- AFM ibriq'; sed -n 5430,5440p AFM_pages.txt; echo ...; sed -n 5686,5694p AFM_pages.txt; awk 'NR<=5433 && /\\f/{n++} END{print \"leaf(0-based)\",n}' AFM_pages.txt; echo '--- AFM anbiq/julab'; grep -n -E 'أنبيق|الانبيق|انبيق|الأنبيق|جلاب|جُلاب|جلّاب' AFM_pages.txt | cut -c1-200 | head -8; echo '--- AFA 5860'; sed -n 5858,5868p AFA.txt | cut -c1-250; grep -n -i -E 'Alembik|ambix|ἄμβ|ibrīq|ibriq' AFA.txt | head -5",
 "description": "Addi Shir and Fraenkel on ibrīq, anbīq, julāb"
}
```


### [2026-09-04T18:15:12.199Z] TOOL RESULT

```
--- AFM ibriq
بخميصا وم
يلم ١51١‏
بلنجوج ١٠١١‏
(5١ نمه‎ابريق "
اخلاد اغاحى ١١6‏
ܫܝ ^
١5١ ارمغان‎
1 1021
١١ اشنا‎
اغارءق ܘ | |
31 أوت ܘ ܘ
...
ܝܝ /اه ١‏# ي +
بأسمين ٠١١‏
يبان مازومى اه
ابريق ܪ
احور مم
١٠٠١ 1‏
ا
}1115
ܨܘ |
leaf(0-based) 178
--- AFM anbiq/julab
--- AFA 5860
Ein anderes \Vort dieser Art ist ^j«iLi#J ilu'^arrab p. 70 ;
p. 13, ult.; Agani XV. 51,3, wo Walid sagt: Sie trinkt
den Rasatün rein, in einem mächtigen Glaskruge.** Es ist,
wie schon Bernstein erkannt hat (vgl. Sachau zu Mu^arrab
34), rosatum seil, vinum, das in griechischer Form also
etwa * :ojxTsv gelautet haben wird. Dasselbe ist auch
^Ujsoh Cast. 809 » Julabium" 1. ^Uffoh. Die echt grie-
chische Form ist poS/rsf^. Die drei eben genannten Wein-
sorten finden sich neben einander im Edict. Diocletiani
De vinis: 18 apsinthi 17 conditum 19 rosathi.
Erkannt ist längst «liuLyo, AjlLjo, AU^j» (bei Freytag
```


## [2026-09-04T18:15:17.162Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '--- PHD tab/sunshine'; grep -n -E \"^(tab|tab-|xwarsed|aftab) |sunshine|\\bsun\\b\" PHD_mackenzie.txt | cut -c1-200 | head -6; grep -n -E \"^(abad|abadan|abadih) \" PHD_mackenzie.txt | cut -c1-200 | head -4; echo '--- NYB zah/anap/axwarr'; grep -n -E \"^(zah|anāp|anap|āxwarr|axwarr|āxwar|axur|āftāp|aftāp)\" NYB_vol2_glossary.txt | cut -c1-250 | head -8; grep -n -E 'āxwarr|axwarr|zahāp|zahāβ' NYB_vol2_glossary.txt | cut -c1-200 | head -5; echo '--- CHEUNG lines'; grep -n -E \"NP (āftāb|aftab|āftāb) ‘sun|\\(\\+ \\*abi-\\) NP\" CHEUNG.txt | cut -c1-200 | head -3; grep -n -E \"NP réxtan/réz-|NP rēxtan\" CHEUNG.txt | cut -c1-200 | head -3; awk 'NR<=24700 && /^\\*[a-z]+ [0-9]+ *$/{p=$0} END{print \"page marker before 24700:\",p}' CHEUNG.txt; awk 'NR<=20482 && /^\\*[a-z]+.? [0-9]+ *$/{p=$0} END{print \"page marker before 20482:\",p}' CHEUNG.txt",
 "description": "MacKenzie, Nyberg, Cheung details and page markers"
}
```


### [2026-09-04T18:15:19.300Z] TOOL RESULT

```
--- PHD tab/sunshine
158: ~~ ~wl represents xwar 'sun', but to transliterate it ·xwr
676:  ...... amadan: rise (sun).
1086: ....., sudan: enter, set (sun).
3560:lmihr [mtr' 1M myhr, N -] Mithra; sun; cal. 7th month; 16th day.
4864:tab [tp IN .....] fever.
5615:txwar [hwll M xwr, N .......] sun; cal. 11th day.
--- NYB zah/anap/axwarr
4476:zahr [z’hl] poison 919-?!, 103. 2516, 2814, 76°. — MPrth jhr; Arm. lw. Zahr; MPrs zhr (A-H I); NP zakr; < *ja@ra- ‘means for killing’, v.s. v. zatan (because of -hr Prs zahr must have been borrowed from NW).
4477:zahyāi [zhy’y] depth 92°. 935. - < *zafydi, v. zufr; Ps. z(wp]?dy; MPrs zwp*y (List 90); Paz. zufaé (SGV); cf pahnäi.
--- CHEUNG lines
8208:*NWIR: (+ *abi-) NP afzudan/afzäy- ‘to increase’ 
10176:call; to read’ || (+ *a-) NP ax'and ‘teacher’ || (+ *abi-) NP afgan, figän ‘tears, crying’ 
12065:*NWIR: (+ *abi-) NP yad ‘memory, remembrance’, widely borrowed (e.g. in Bal. yat, 
12801:*NWIR: Widely attested: NP réxtan/réz- ‘to flow, pour’, Bal. rétk/réc- ‘to pour’, 
20481:*NWIR: NP réxtan/réz- ‘to drop’, Bal. rézit/réz- ‘to atrophy, become thin, decay’ 
page marker before 24700: *tap 379 
page marker before 20482: *raiz3 311
```


## [2026-09-04T18:15:51.783Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '--- LKT 79'; sed -n 398,404p LKT.txt | cut -c1-400; echo '--- LKT 5'; grep -n -A3 -E '^5\\.  Pers\\. ' LKT.txt | cut -c1-300 | head -6; echo '--- CHEUNG 12801 lemma'; awk 'NR<=12801 && /^\\*[a-zA-Zčšžʰ]+[0-9¹²³]* ‘/{p=$0;pl=NR} END{print pl\": \"p}' CHEUNG.txt; awk 'NR<=12801 && /^\\*[a-z]+.? [0-9]+ *$/{p=$0} END{print \"page:\",p}' CHEUNG.txt; grep -n \"NP айар\\|NP āftāb ‘sun\" CHEUNG.txt | head -2; echo '--- AFM بريق'; grep -n 'بريق' AFM_pages.txt | cut -c1-200 | head -8; echo '--- SKT julep'; grep -n -i 'julep' SKT.txt | cut -c1-300 | head -3; echo '--- FSD alembic'; grep -n -i 'alembic' FSD_vol1.txt | cut -c1-300 | head -3; echo '--- KLN doab/punch'; grep -n -E '^doab|^punch, n|Pers\\. panj' KLN_1966.txt | cut -c1-300 | head -4; echo '--- ARY dir'; ls incoming/ARY/",
 "description": "Lokotsch, Cheung, Addi Shir, Skeat, F&W, Klein follow-ups"
}
```


### [2026-09-04T18:15:53.715Z] TOOL RESULT

```
--- LKT 79
79.  Ar.  anbik:
[Das  selbst  aus  gr.  äußiE;  in  der  Aus- sprache amblk]  'Destilliergefäß'.  Hieraus z.  T.  mit,  z.  T.  ohne  ar.  Art.  lat.  alam- bicum  und  die  romanischen  Formen: it.  lambicco,  lambiccio,  limbiccio  'Destil- lierkolben', Vb.  lambicare  'durch  das Reagenzglas  gehen,  genau  prüfen',  lam- biccarsi  od.  beccarsi  il  cervello  'sich  den
Ar.  aiiilnl  ]
8
Kopf  zerbrechen';  prov.  elamhic,  frz. tiliimbic,  runi.  alanibic,  .sp.  alambiqnc, pg.  lamhiqnc;  en^'l.  aleinhic.  Vb.  frz. alamhiquer  'destillieren',  auch  figür- licli.  [DE  r)(i.  Devic  DEl  5.  ML  ii± Warlbg  FEWb  57.  GIBBS  in  American Journal  of  Science  and  Arts  XXXIII,  325.
80.  Ar.  audul :
(Auch  haudrd;  selbst  aus  dem  pers. und  letzten  Endes  aus  sanskr.  himlöla, andöla  'chinesische  Sänfte',  vgl.  ZDMG LI,  «58;  LH,  i282;  auch  syrisch  andül BrLexSyr  28  a]  'Sänfte'.  Hieraus  viel- leicht mit  ar.  Art.  sp.  lando  'leichter mit  Maultieren  bespannter  Wagen  mit 4  Sitzen'  [Dicc  Gast  1240c,  freilich  mit unrichtiger  Etymologie],  frz.  londau, engl, 
--- LKT 5
228:5.  Pers.  abdär:
229-[Aus  äb  'Wasser'  od.  'Glanz'  Hoi-n  NpEt S.  1,  Nr.  2  und  3,  und  Stamm  där- 'habend,  haltend'  ebda.  S.  116,  Nr.  527] 'wässerig,  hell,  glänzend'  [von  Stahl od.  Waffen  gesagt].  Über  das  tk.  hier- aus rum.  abitir  'besser,  vortrefflicher'; russ.  ob'jar  'Art  Sto
230-6.  Ar.  abjad :
231-'Weiß'.  Hieraus  fiz.  abit  'Bleiweiß', alter  chemischer  Terminus.  Aus  dem ar.  Subst.  bajäd  'Weiße'  wurde  mit  ar. Art.  sp.  albayalde  'kohlensaures  Blei- salz', Vb.  albayaldar.    [Devic  DEl  1.
--- CHEUNG 12801 lemma
12712: *HraH ‘to offer, give’ 
page: *huar3 149 
24720:tile’, Kurd. taw ‘sun’ || (+ *abi-) NP айар ‘sun(shine)’ || (+ *ш-) Gur. (Kand.) yaw 
--- AFM بريق
156:( الاربريق) إناء من حرف او معدن 71 عرؤة ܬ و بلملة ܨ $ ܠ
5433:(5١ نمه‎ابريق "
5689:ابريق ܪ
--- SKT julep
--- FSD alembic
10898:Al'a-math,  1   al'a-mafh;  2   al'a-mSth,  n.  Bib.  (DouaO. a-Iam'bict,  n.  An  alembic.
11540:[Hare.]  To  distil,  as  by  the  alembics.  a-Iem'bi- cate}.
11552:The  world  cares  little  for...  any  thing  J a   man  has  to  utter  that  has  not  previously  been  dis- tilled  in  tho  alembicol  hia  life.
--- KLN doab/punch
--- ARY dir
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
ARY_pages.txt.pages
```


## [2026-09-04T18:16:07.524Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '--- AFM 156'; sed -n 154,158p AFM_pages.txt | cut -c1-250; awk 'NR<=156 && /\\f/{n++} END{print \"leaf(0-based)\",n}' AFM_pages.txt; echo '--- CHEUNG 12780-12801'; sed -n 12778,12801p CHEUNG.txt | grep -E '^\\*' | cut -c1-200; echo '--- FSD 11536-11542'; sed -n 11536,11542p FSD_vol1.txt | cut -c1-400; echo '--- KLN punch'; grep -n -E '^punch' KLN_1966.txt | cut -c1-300 | head -3; echo '--- ARY PERSIAN headwords'; grep -n -E 'PERSIAN' incoming/ARY/ARY_pages.txt | grep -E 'ناب|آفتاب|گلاب|پنجاب|آبادان|آخور|زهاب|آبریز|آسیاب|آبان' | cut -c1-120 | head; grep -n -E '^ *(ĀFTĀB|AFTAB|GOLĀB|GOLAB|NĀB|NAB|ĀBĀDĀN|ABADAN|ĀKHOR|PANJĀB|ZAHĀB|ĀBRIZ)\\b' incoming/ARY/ARY_pages.txt | cut -c1-120 | head",
 "description": "Addi Shir ibrīq entry, Cheung lemma, F&W alembic, Klein punch, Aryanpur headwords"
}
```


### [2026-09-04T18:16:09.209Z] TOOL RESULT

```
--- AFM 156
( !ܨ ܙܬ ) !ܙ + تعريب ابر < ܙ في الارامسة الدارجة ܐ ܒܪܝܣܡ
وي الارمشة 120010101 وبالكردنة ܬܕ يم
( الاربريق) إناء من حرف او معدن 71 عرؤة ܬ و بلملة ܨ $ ܠ
يصب الماء وهو يطلق بالفارسسة على الدلو ܢܸܐ وكاس الممام والسطل وغير ذلك مما
يضارعها ٠‏ ومئة السر يالى ܐܒ ܘܝܩ والفرذ. ܨ 80 والايطا !3 95 :ܐ
leaf(0-based) 6
--- CHEUNG 12780-12801
*Hraié ‘to pour, flow’ 
*MIDDLE PERSIAN: MMP ryc- (sic), BMP lyc- /réz-/ ‘to flow; pour’ || (+ *pati-) MMP 
*PARTHIAN: ryz- ‘to pour’. On ryz- ‘to fall (of leaves)’ see *raiz’. > Ghilain: 94 | 
*SOGDIAN: BSogd. ryz ‘to flow’ || (+ *apa-) SSogd. p’ryc (caus.) ‘to pour (out) 
*NWIR: Widely attested: NP réxtan/réz- ‘to flow, pour’, Bal. rétk/réc- ‘to pour’, 
--- FSD 11536-11542
usually  affixed  to  a   stem  representing  the  typical  family  of the  group;  as,  Rosales,  a   group  of  allied  families  of  which Rosacex  is  the  type.  Such  a   group  In  one  classification,  as Lindlcy’s,  is  called  an  alliance;  in  another,  as  Bentbam  and Hooker’s,  a   cohort;  In  still  another,  as  Engler’s.  a   series,  in current  acceptance  an  order.  [L
A"lem"bert'»  1   a'lafl'hS.r';  2   a'laft'ber',  Jean  le  Bond  d’  a-le'sef,  vt.  To  lease  again;  repurchase.
(u /is  171  7—10/:j  1783).  A   French  mathematician  and  philoso-  A-le'sI-a,  1   e-H'jflu-a:  2   a-16'shl-a.  n.  A   town  and  fortress  In pher;  Joint  editor  with  Diderot  of  the  Encyclopedic.  ancient  Gaul  captured  by  Julius  Caesar,  A.  D.  52,  com-
a-Iem'blc,  1   a-Iem'bik;  2   a-16m'blc,  vt.  T-bioked:  -bick-ing.]  pleting  the  subjugation  of  Gaul.
[Hare.]  To  distil,  as  by  the  alembics.  a-Iem'bi- cate}.
aleatory  sale;  aleatory  contract^,  g.,  an  insurance  pol-  a-Icm'blc,  n.  1.  An  apparatus  of  glass  or
icy.  2.  Of  or  pertaining  to  gambling  or  gamblers.
--- KLN punch
29857:puncheon,  ‘stamp’),  partly  fr.  pounce,  ‘claw  of  a hawk ;  a  punch’.
30998:punch,  tr.  v.,  to  perforate.  —  Either  derived  fr. punch,  ‘a  tool’,  or  a  collateral  form  of  pounce, ‘to  emboss’.
31000:punch,  n.,  a  short,  thick -set  person;  anything short  and  thick.  —  Prob.  fr.  the  PN.  Punch  (q.v.) punch,  n.,  a  beverage.  —  Hind,  punch,  fr.  OI. pahca,  ‘five’,  which  is  cogn.  with  Gk.  news,  L. quinque,  Goth,  fimf,  OE.  fif  (see  five  and  cp. Panchata
--- ARY PERSIAN headwords
```


## [2026-09-04T18:16:23.714Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n 11542,11547p FSD_vol1.txt | cut -c1-500; awk 'NR<=12780 && /^\\*[a-zA-Z]+.? [0-9]+ *$/{p=$0} END{print \"CHEUNG page before Hraič:\",p}' CHEUNG.txt; awk 'NR<=10309 && /^\\*[a-zA-Z]+.? [0-9]+ *$/{p=$0} END{print \"CHEUNG page before huar1:\",p}' CHEUNG.txt; awk 'NR<=4423 && /\\f/{n++} END{print \"BRT leaf(0-based) for an-āpa-:\",n}' BRT.txt; awk 'NR<=8831 && /\\f/{n++} END{print \"HRN leaf for 1015:\",n}' HRN.txt; awk 'NR<=464 && /\\f/{n++} END{print \"HRN leaf for no.3:\",n}' HRN.txt; awk 'NR<=553 && /\\f/{n++} END{print \"HRN leaf for no.8:\",n}' HRN.txt; awk 'NR<=5864 && /\\f/{n++} END{print \"AFA leaf:\",n}' AFA.txt; awk 'NR<=527 && /\\f/{n++} END{print \"SKT leaf:\",n}' SKT.txt; awk 'NR<=102769 && /\\f/{n++} END{print \"WEB leaf:\",n}' WEB_vol1.txt; awk 'NR<=8899 && /\\f/{n++} END{print \"HJB leaf:\",n}' HJB.txt; awk 'NR<=1220 && /\\f/{n++} END{print \"SYN leaf:\",n}' SYN.txt; awk 'NR<=223 && /\\f/{n++} END{print \"IEC leaf:\",n}' IEC.txt; awk 'NR<=548 && /\\f/{n++} END{print \"NYB leaf apatan:\",n}' NYB_vol2_glossary.txt; awk 'NR<=473 && /\\f/{n++} END{print \"NYB leaf ap:\",n}' NYB_vol2_glossary.txt; awk 'NR<=658 && /\\f/{n++} END{print \"PHD leaf ab:\",n}' PHD_mackenzie.txt; awk 'NR<=5730 && /\\f/{n++} END{print \"PHD leaf zahabag:\",n}' PHD_mackenzie.txt; awk 'NR<=12387 && /\\f/{n++} END{print \"PHD leaf axwarr:\",n}' PHD_mackenzie.txt",
 "description": "Page/leaf numbers for the quoted entries"
}
```


### [2026-09-04T18:16:25.792Z] TOOL RESULT

```
icy.  2.  Of  or  pertaining  to  gambling  or  gamblers.
Failure  in  aleatory  operations  is  .   .   .   more  apt  than  failure  in ...  business  to  induce  despondency.
N.  V.  Times  July  28,  1892,  p.  4,  col. ‘3.
[<  L.  aleatorius,  <   alea,  die,  chance.] ale'ber"ry,  etc.  See  under  ale.
a 'Icc,  1   C'lek;  2   fi'lCc,  n.  [L.]  An  ancient  sauce  made  of small  herrings;  also,  a   herring. al"e-cam-pane'f,  n.  Same  as  elecampane. a-Icc'i-thal,  1   s-les'i-fhal;  2   a-lCg'l-thal,  a.  Embryol.  1. Having  the  food-yolk  absent,  or  small  and  uniformly distributed:  said  of  certain  ova.  2.  Of  or  pertaining to  such  ova.  I   <   Gr.  a-  priv.  ■+■  lekitho*,  yolk  of  an  egg.] al'c-clzc,  1   al'i-salz;  2   fil'c-elz,  vl.  To  dress  (a  dish)  wit
a-lcc'rln,  l   a-lek'rln;  2   a-15c^rln,  n.  A   fish,  the  tiger-shark. A"lec-san'drl,  1   a’lek-san'drl;  2   :i "K-c-sun'dri,  VasslII (7/-l 82 1**D/ < 1 890) .   A   Roumanian  poet  and  polltlrian.
CHEUNG page before Hraič: *Hmarz 181 
CHEUNG page before huar1: *huaid 143 
BRT leaf(0-based) for an-āpa-: 101
HRN leaf for 1015: 242
HRN leaf for no.3: 15
HRN leaf for no.8: 18
AFA leaf: 188
SKT leaf: 21
WEB leaf: 1026
HJB leaf: 368
SYN leaf: 59
IEC leaf: 12
NYB leaf apatan: 33
NYB leaf ap: 27
PHD leaf ab: 18
PHD leaf zahabag: 114
PHD leaf axwarr: 252
```


## [2026-09-04T18:16:41.335Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n 65496,65500p FSD_vol2.txt | cut -c1-700; echo; grep -n -o -E 'a-lem.blc,  n\\..{0,600}' FSD_vol1.txt | grep -i -E 'Ar\\.|Gr\\.|anb|amb' | cut -c1-500 | head -2; grep -n -o -E '\\[.{0,80}(anbiq|ambix|ambik|anbik).{0,80}\\]' FSD_vol1.txt | head -3",
 "description": "Funk & Wagnalls etymologies of julep and alembic"
}
```


### [2026-09-04T18:16:44.988Z] TOOL RESULT

```
Jn'lep,  1   ju'lep;  2   ju'lSp  (xin), n.  1.  A   drink  com  posed  usu- ally of  brandy  or  whisky,  sugar, cracked  ice,  and  some  flavor- ing, commonly  fresh  crushed g   r   e   e   ri  mint.  2.  A   subacid, mucilaginous,  sweetened  drink, often  used  as  a   vehicle  for  the administration  of  medicine. IF,  <   Bp.  julepe,  <   Ar.  jUMb, “   '   "   water.]  juTapt-
ry,  a.  Of  or  pertaining  to  the  malar  and  the  superior  maxll-  pa.  Supplied  with  juice;  .succulent:  usually  in  combina- lary  bones;  as,  the  j«ffomaa:«2ary  suture.  [<  L.  Juffurn,  tlon:  as,  fuU-;j«fced  apple.— juIccTul,  juIccTess,  a. yoke,  4- MAXILLART.]  Having  no  juloa
Ju"Bo-na'saJ,T  jfl’go-nS'zal:  2   ju'go-na'aal,  o.  Antbrap.  Re- Julc'y,  1   jos'i;  2   juc'y,  a.  [JuicT-er;  juic'i-est.]  1. lating  to  both  the  nose  and  the  jugal  point.  l<  h.  Jugttm,  Abounding  with  juice:  moist;  -
Jujus  of  Jehba,
compound  (CtoHoOa),  resembling  quinone,  obtained the  walnut.  *   I<  Jdglajss.I

ugrep: error: error at position 105
|anbik)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,80}\]
                exceeds complexity limits___/
```


## [2026-09-04T18:18:21.552Z] AGENT

I have all the lookups I need. Now I'll write the vision transcripts for the two page images I read, then apply the `consulted` arrays and `ref_check` upgrades with a script.


## [2026-09-04T18:18:42.101Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr; cat > BQT/1225.vision.txt <<'EOF'\nBQT:1225 — Borhan-e Qate' vol. 3 (Mo'in ed.), running head «-۱۲۲۵-» / «شارو», read from ocr/BQT/1225.png (BQT_v3_picofile.pdf page 16). Entries on this page are شار … شارو (letter ش), NOT زهاب.\nUsed for Nourai's BQT:1225 citation under آب / آبشار:\nشار (main entry, right column, continued): «… و بمعنی شاه راه هم هست که راه فراخ و گشاد باشد ۴ - و فرو ریختن آب و شراب و امثال آن باشد همچو آبشار و سرشار ۵ - و بمعنی رقص و سماع نیز بنظر آمده است.»\nMo'in footnote ۵: «گیلکی و دزفولی shorra (آوای فرو ریختن آب) «امام» و غالباً در فارسی به تکرار «شارشار» گویند. رک: شاریدن.»\nOther entries on the page: شارده (نام جزیره‌ایست از جزایر دریای روم)، شارسان / شارستان (شهر و شهرستان؛ fn ۸: از: شار = شهر (ه.م.) + ستان (پسوند مکان)؛ Henning, Sogdian loan-words, p. 94, note 2)، شارشك (تیهو)، شارك (پرنده‌ای سیاه؛ fn ۱۲: معرب آن «شارك» دزی)، شارمار (fn ۱۳: از: شار (ه.م.) + مار)، شارو.\nEOF\ncat > ARY/0051.vision.txt <<'EOF'\nARY:51 — Aryanpur Kashani, Farhang-e Rishe-ha-ye Hend-o-Orupayi, printed p. 51 (pdf page 50), read from ocr/ARY/0051.png.\nEntry آب (PERSIAN) ĀB — English gloss WATER — Indo-European *ĀP.\nCognates: اوستایی (AVESTAN): ĀP, APAM; پارسی باستان (OLD PERSIAN): ĀPI, APUS; پهلوی (PAHLAVI): ĀB, ĀP; کردی (KURDISH): ĀV, DjYRAV; سانسکریت (SANSKRIT): ĀP, ĀPA; یونانی (GREEK): APIA; لاتین (LATIN): AMNIS; فرانسه (FRENCH): EAV [sic]; لیتوانی (LITHUANIAN): ŪPĒ; لتونی (LATVIAN): UPĒ; پروسی کهن (OLD PRUSSIAN): APE; ایرلندی کهن (OLD IRISH): ABANN.\nپسگشت‌ها / REFERENCES: POKORNY 51-52; MACKENZIE (WATER) 139; BUCK (WATER) 34-35; MALLORY 129; برهان قاطع: ۱; لغت‌نامه دهخدا: ۳۵.\n(Next entry on the page: آتش ĀTASH 'FIRE' < *ĀTER; Avestan ĀTER, ATARSH; Pahlavi ĀTUR, ĀTAXSH; refs Pokorny 69, Delamarre 179, MacKenzie 114, Buck 71, Amindarov 247, Borhan 13-14, Dehkhoda 65-66.)\nEOF\nls -la BQT/1225.vision.txt ARY/0051.vision.txt",
 "description": "Save verbatim transcriptions of the two page images read"
}
```


### [2026-09-04T18:18:43.950Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 1003 Sep  4 14:18 ARY/0051.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1254 Sep  4 14:18 BQT/1225.vision.txt
```


## [2026-09-04T18:22:07.630Z] TOOL CALL #42: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/apply_p31.py",
 "content": "import json, io\n\nP = '/home/sfmqrb/git/rishe/data/verification/page-31.json'\nd = json.load(open(P, encoding='utf-8'))\ne = d['entries'][0]\nnodes = {n['id']: n for n in e['nodes']}\n\ndef C(src, where, stance, note):\n    return {\"src\": src, \"where\": where, \"stance\": stance, \"note\": note}\n\n# ---------- shared quotes ----------\nWLD46 = C(\"WLD\", \"Bd. I p. 46 (WLD_Bd1_pages.txt leaf 55)\", \"supports\",\n          \"'2. ap- \\\"Wasser, Fluß\\\". Ai. āp- \\\"Wasser\\\", z. B. n. sg. āpaḥ ... g. pl. apām, av. n. sg. āfš, a. sg. āpəm, i. sg. apa(-ca) ... apr. ape \\\"Fluß\\\", apus \\\"Quell, Brunnen\\\", lit. ùpė, lett. upe \\\"Wasser\\\"' — the Walde-Pokorny article that Pokorny 51 revises; Buck cites it as 'Walde-P. 1.46'.\")\nAHD_AP2 = C(\"AHD\", \"Watkins 1985 s.v. ap-2 (AHD_watkins1985.txt line 282)\", \"supports\",\n            \"'ap-2. Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.]'\")\nIEC223 = C(\"IEC\", \"Mann col. 22 s.v. abhmn-, abhnis (IEC.txt line 223)\", \"partial\",\n           \"'abhmn-, abhnis \\\"river, water\\\". WP I, 46 ... Lat. amnis ... Gaul. abono-; W afon ... OIr. aba, gs. abann' — Mann has only the ab-/amnis group; no āp- lemma with the Indo-Iranian 'water' word is recoverable in the OCR (line 622 'ap-, radical of āpnu-' is the unrelated 'take' root).\")\nSYN131 = C(\"SYN\", \"Buck 1.31 WATER §3, p. 35 (SYN.txt line 1236)\", \"supports\",\n           \"'3. IE *āp-. Walde-P. 1.46. Skt. āp-, ap- mostly pl. āpas ..., Av. āp-, ap- the reg. word for \\\"water\\\", also freq. personified, OPers. api-, NPers. āb \\\"water\\\". Elsewhere only of \\\"running water\\\" in words for \\\"river\\\", as Lith. upė, Lat. amnis, Ir. abann' (also 1.36 RIVER §3: 'From IE *ap (and ab-) \\\"water\\\"').\")\nARY51 = C(\"ARY\", \"p. 51 s.v. آب (ocr/ARY/0051.vision.txt)\", \"supports\",\n          \"Headword آب ĀB 'WATER' < Indo-European *ĀP; cognates Avestan ĀP, APAM; Old Persian ĀPI, APUS; Pahlavi ĀB, ĀP; Kurdish ĀV; Sanskrit ĀP, ĀPA; Latin AMNIS; Lith. ŪPĒ; Latv. UPĒ; Old Prussian APE; Old Irish ABANN; refs Pokorny 51-52, MacKenzie 139, Buck 34-35, Mallory 129, Borhan-e Qate' 1, Dehkhoda 35.\")\nBRT_ANAP = C(\"BRT\", \"AiW col. 122 s.v. an-āpa- (BRT.txt line 4423)\", \"supports\",\n             \"'j. an-āpa- Adj. (\\\"wo kein Wasser ist\\\" sva.) \\\"trocken\\\" von Speisen, \\\"ungemischt\\\" vom Wein: ... V. 5.52; als neutr. Subst. \\\"Wüste\\\"' — Avestan privative an- + āp- 'water' = 'without water; unmixed (wine)', the etymon of NP nāb; the āp- article itself is at cols 325 ff. (Nyberg's cross-reference 'Av. (325 sqq.) āp-').\")\nKNT_AP = C(\"KNT\", \"Kent §143 and §88 (KNT.txt lines 1531, 2224)\", \"supports\",\n           \"'*ap- \\\"water\\\" in inst. pl. abiš, *āp- in nom. āpi, loc. apiyā' and '§88 ... stems ending in ... p (xšap- \\\"night\\\", ap- \\\"water\\\" cf. āpi-)' — OP ap-/āpi- 'water' is the Old Persian member of the family.\")\nPHD_AB = C(\"PHD\", \"MacKenzie s.v. ab (PHD_mackenzie.txt line 658)\", \"supports\",\n           \"'ab [MYA | M ʾb, N āb] water' — Book Pahlavi āb with the Aramaeogram MYA, Manichaean ʾb, New Persian āb.\")\nNYB_AP = C(\"NYB\", \"Nyberg Part II s.v. āp (NYB_vol2_glossary.txt line 473)\", \"supports\",\n           \"'āp [MYʾ; ʾp' ...] water ...; pl. cas. obl. āpān. — Av. (325 sqq.) āp-, OP āpi-; MPrthPrs ʾb; Paz. āw, āv; NP āb.'\")\nNYB_APATAN = C(\"NYB\", \"Nyberg Part II s.v. āpātān (NYB_vol2_glossary.txt line 548)\", \"contradicts\",\n               \"'āpātān [ʾpʾtʾn'] cultivated, inhabited ...; Paz. āwāda; cf MPrth ʾbʾd; Arm. lw. apat; NP ābād and ābādān; < OIr *ā-pāta- \\\"protected\\\", v. pātan (1)' — ābādān is ā- + pā- 'protect', no āb 'water'. Nyberg has no āftāp, zahāp or āxwarr headwords.\")\nHRN3 = C(\"HRN\", \"Horn no. 3 āb 'Glanz', p. 1-2 (HRN.txt line 464)\", \"contradicts\",\n         \"'3. āb \\\"Glanz\\\" (Šahn. I S. 14 Vers 7), vergl. āb-rō, āb-tāb, āb-mend, Rōd-ābe, Suhr-āb, Mihr-āb, Ardā Vīr-āf, āf-tāb, phlv. āb; skr. ābhā- \\\"Glanz\\\"' — Horn puts āftāb under a separate āb 'lustre' (Skt. ābhā-), not under āb 'Wasser' (no. 2).\")\nHRN4 = C(\"HRN\", \"Horn no. 4 ābād, p. 2 (HRN.txt line 475)\", \"contradicts\",\n         \"'4. ābād \\\"bewohnt\\\", vergl. ābādān, āwādān ...; ap. *āpāta-; phlv. āpāt (pāz. āwād), āpātīh, āpātān, āpātānīh; armen. LW. apat' — ābādān from OP *ā-pāta- 'protected', without āb 'water'.\")\nHRN8 = C(\"HRN\", \"Horn no. 8 āxur, p. 4 (HRN.txt line 553)\", \"contradicts\",\n         \"'8. āxur \\\"Stall\\\". aw. avō.xᵛarəna- \\\"Stall, Futterplatz\\\"; phlv. āxur oder avxᵛar (Darmesteter, Et. ir. II, 136), arm. LW. axoṙ ... (de Lagarde, Semitica I 42) \\\"Stallmeister\\\"' — Avestan avō.xᵛarəna- 'feeding-place' (xᵛar- 'eat'), no āb 'water'.\")\nHRN2 = C(\"HRN\", \"Horn no. 2 āb 'Wasser', p. 1 (HRN.txt lines 455-461)\", \"supports\",\n         \"'2. āb, āw \\\"Wasser\\\"; vergl. sīm-āb (\\\"Quecksilber\\\", wörtl. \\\"Silberwasser\\\") ...; ap. āp- \\\"Wasser\\\"; aw. āp-; phlv. āp (pāz. āw); ai. āp-, kurd. āw; afγ. ōba (fem.); bal. āp, n. āf' — NP āb < OP/Av. āp-. Horn has no zahāb entry.\")\nCH_TAP = C(\"CHEUNG\", \"Cheung 2007 s.v. *tap 'to warm up, heat', p. 379 (CHEUNG.txt line 24720)\", \"contradicts\",\n           \"'... Kurd. taw \\\"sun\\\" || (+ *abi-) NP āftāb \\\"sun(shine)\\\"' (and Parthian '(+ *abi-) ʾbdʾb \\\"sunshine\\\"', line 24686) — āftāb = preverb *abi- + *tap 'to shine/heat'; no āp 'water'.\")\nCH_HUAR = C(\"CHEUNG\", \"Cheung 2007 s.v. *huar1 'to consume, eat', p. 147 (CHEUNG.txt line 10309 ff.)\", \"partial\",\n            \"'*MIDDLE PERSIAN: MMP xwr-, BMP hwl- /xwar-/ ... \\\"to drink, eat, enjoy\\\"' — the verb behind MP āxwarr 'manger'; Cheung does not list āxwarr itself, but the root is 'eat', not āb.\")\nCH_RAIC = C(\"CHEUNG\", \"Cheung 2007 s.v. *Hraič 'to pour, flow', p. 181-182 (CHEUNG.txt lines 12780-12801)\", \"supports\",\n            \"'*MIDDLE PERSIAN: MMP ryc- (sic), BMP lyc- /rēz-/ \\\"to flow; pour\\\" ... *PARTHIAN: ryz- \\\"to pour\\\" ... *NWIR: Widely attested: NP rēxtan/rēz- \\\"to flow, pour\\\"' — the second element of āb-rēz/ābrīz is the present stem rēz- of *Hraič (Nourai's ☞Leigh 2 = PIE *leikʷ-).\")\nHUB1015 = C(\"HUB\", \"Hübschmann Pers. Studien no. 1015, p. 100 (HUB.txt line 3539)\", \"supports\",\n            \"'1015. Dazu arm. LW. anapak ungemischt, rein (vom Wein).' — the Armenian loan anapak preserves the full MP anāp(ak) 'un-watered', confirming nāb < anāp.\")\nPLA_IBRIQ = C(\"PLA\", \"Asbaghi p. 3 s.v. ibrīq and p. 2 s.v. abrīz (PLA_pages.txt lines 582, 555)\", \"supports\",\n              \"'ibrīq: \\\"Gießkanne; Ibrik\\\" aus dem pers. آبریز ābrīz s. ābrīz, syr. ..., dtsch. Ibrik \\\"im Orient Wasserkanne mit dünnem Hals und ovalem Bauch\\\"'; the preceding 'abrīz: \\\"pures Gold, Obryzum\\\" pers., aus dem pers. āb \\\"Glanz\\\" + rīz' is the homonymous āb 'lustre' compound.\")\nAFM_IBRIQ = C(\"AFM\", \"Addi Shir p. 6-7 s.v. (الإبريق) (AFM_pages.txt leaf 6, line 156)\", \"supports\",\n              \"'(الإبريق) إناء من خزف أو معدن ... يُصبّ [منه] الماء وهو يطلق بالفارسية على الدلو ... ومنه السرياني ܐܒܪܝܩܐ والفرنسي ... والإيطالي' — Arabic ibrīq listed as an arabicized Persian word (āb-rīz), with the Syriac and Romance descendants.\")\nMON_IBRIQ = C(\"MON\", \"Mo'in s.v. ابریق (MON_part1.txt line 6264)\", \"supports\",\n              \"'ابریق: [معر. آبریز] (اِ.) ظرف سفالین آب ...' — Mo'in marks ibrīq as the arabicized form of Persian ābrīz.\")\nLKT79 = C(\"LKT\", \"Lokotsch no. 79 Ar. anbīk, p. 8 (LKT.txt line 398)\", \"contradicts\",\n          \"'79. Ar. anbīk: [Das selbst aus gr. ἄμβιξ; in der Aussprache ambīk] \\\"Destilliergefäß\\\". Hieraus z. T. mit, z. T. ohne ar. Art. lat. alambicum und die romanischen Formen: it. lambicco ...; prov. elambic, frz. alambic, rum. alambic, sp. alambique, pg. lambique; engl. alembic' — Arabic anbīq from Greek ámbix, no Persian āb-nīk.\")\nDEV_ALAMBIC = C(\"DEV\", \"Devic p. 5 s.v. Alambic (DEV.txt line 270)\", \"contradicts\",\n                \"'Alambic. Esp. alambique, port. lambique, ital. lambico, de l'arabe الأنبيق al-anbīq, venant du grec ἄμβιξ vase à distiller, précédé de l'article arabe al.'\")\nPHN_ALAMBIC = C(\"PHN\", \"Pihan s.v. ALAMBIC (a.-gr.) (PHN.txt lines 1095-1103)\", \"contradicts\",\n                \"'Les étymologistes s'accordent à regarder alambic comme la transcription du grec ἄμβιξ, vase à bords relevés, précédé de l'article arabe al. Cependant il est probable que les chimistes ont emprunté directement ce terme aux Arabes, qui sans doute l'avaient tiré de la langue grecque. — Les Espagnols et les Portugais écrivent alambique.'\")\nSKT_ALEMBIC = C(\"SKT\", \"Skeat s.v. Alembic, p. 12 (SKT.txt line 527)\", \"contradicts\",\n                \"'Alembic, a vessel for distilling. (F. — Span. — Arab. — Gk.) M.E. alembike; F. alambique (Cot.); Span. alambique. — Arab. al, the; and anbīq (pronounced ambīq), a still. — Gk. ἄμβιξ, a cup, goblet; cap of a still' — Greek origin; chain Greek > Arabic > Spanish > French > English.\")\nLKT742 = C(\"LKT\", \"Lokotsch no. 742 Pers. gulāb, p. 59 (LKT.txt line 1810)\", \"supports\",\n           \"'742. Pers. gulāb: \\\"Rosenwasser\\\" [aus pers. gul \\\"Rose\\\", s. hier Nr. 740, und āb \\\"Wasser\\\", s. hier Nr. 5], ebenso ar. gulāb, vulg. guleb; hieraus mlat. julapium \\\"eine Art Sirup, Kühltrank\\\", it. giulebbe, giulebbo, giuleppo, prov. frz. julep, sp. julepe, pg. julepo.'\")\nLKT1619 = C(\"LKT\", \"Lokotsch no. 1619 Pers. pānǧ, p. 131 (LKT.txt line 3704)\", \"contradicts\",\n            \"'1619. Pers. pānǧ: \\\"Fünf\\\" [Horn NpEt S. 73, Nr. 328; vgl. pānǧ-āb \\\"Pandschab\\\", engl. Schreibung Punjaub \\\"Fünfstromland\\\"]; hieraus engl. punch, dtsch. Punsch' — Lokotsch treats Panjāb as a Persian compound panj + āb, against the 'Sanskrit' label.\")\nHJB_DOAB = C(\"HJB\", \"Hobson-Jobson s.v. DOAB, p. 321 (HJB.txt line 8899)\", \"partial\",\n             \"'DOAB, s. and n.p. P.—H. doāb, \\\"two waters\\\", i.e. \\\"Mesopotamia\\\", the tract between two confluent rivers ... Each of the like tracts in the Punjab has its distinctive name' — Persian āb 'water/river' in North-Indian toponyms; there is no PUNJAB headword (Panjāb only in passing, e.g. lines 832, 1657).\")\nKLN_PUNCH = C(\"KLN\", \"Klein p. 1273 s.v. punch (beverage) (KLN_1966.txt line 31000)\", \"partial\",\n              \"'punch, n., a beverage. — Hind. punch, fr. OI. pañca, \\\"five\\\", which is cogn. with Gk. πέντε, L. quinque ...' — Klein has the Sanskrit numeral but no Punjab, doab or panj-āb entry.\")\n\n# ---------- ENTRY (root) ----------\ne['consulted'] = [WLD46, AHD_AP2, IEC223, SYN131, ARY51,\n    C(\"BRT\", \"AiW cols 122, 325 ff. (BRT.txt lines 4423, 3944)\", \"supports\",\n      \"Avestan āp- f. 'Wasser' (nom. āfš, e.g. line 3944 'aēša āfš yaoždya bavaiti V. 6.32'; compound an-āpa- 'wo kein Wasser ist') — the Old-Iranian member of the root that Pokorny lists under 2. ap- 51.\"),\n    KNT_AP]\n\n# ---------- node 1 ----------\nnodes[1]['consulted'] = [BRT_ANAP, KNT_AP, PHD_AB, NYB_AP, WLD46, ARY51]\n\n# ---------- node 2 ----------\nn = nodes[2]\nn['consulted'] = [NYB_APATAN, HRN3, HRN4, HRN8, CH_TAP, CH_HUAR,\n    C(\"PHD\", \"MacKenzie s.v. zahabag, asyab, abad (PHD_mackenzie.txt lines 5730, 1261, 659)\", \"partial\",\n      \"'zahabag [zhʾpk | N zahāb] spring, source' supports zā-āp; but 'abad [ʾpʾt | M ʾbʾd, N ābād] populous, thriving, prosperous' and axwarr (line 12387) are independent lemmas, not āb-compounds (already recorded in ref_check as PHD contradicts).\"),\n    C(\"BQT\", \"vol. 1 p. ~49 s.v. آفتاب (BQT_v1_pages.txt line 8232)\", \"partial\",\n      \"Borhan: 'آفتاب - بروزن ماهتاب. بمعنی تابش و روشنی و پرتو مهر است همچو ماهتاب، ترکیبی آن آفت آب است' — Borhan's own folk-etymology 'āfat-e āb' (bane of water) shows the compound was already felt to contain āb; Mo'in's etymological footnote on this page is not legible in the OCR (and vol. 1 exists only as archive.org OCR, no page image).\"),\n    C(\"HUB\", \"Hübschmann Pers. Studien (HUB.txt, grep āftāb/ābād/āxur)\", \"silent\",\n      \"No addition to Horn nos 3, 4, 8 found in the OCR of Hübschmann's Part I.\"),\n    C(\"MON\", \"Mo'in (MON_part1/2.txt, grep آبادان/آخور/آفتاب headwords)\", \"silent\",\n      \"The headword lines for آفتاب, آبادان and آخور are not recoverable in the OCR (only compounds like 'آفتاب سر دیوار'); no etymology readable.\")]\nfor rc in n['ref_check']:\n    if rc['ref'] == 'BQT:1,49':\n        rc['status'] = 'partial'\n        rc['note'] = (\"BQT vol. 1 (BQT_v1_pages.txt): p. 1 s.v. آب at OCR line 5859: 'آب - بسکون بای ابجد. معروف است که یکی از جملهٔ چهار عنصر باشد ...' (Mo'in's footnote with the Pahlavi form is garbled); p. ~49 s.v. آفتاب at line 8232: 'آفتاب - بروزن ماهتاب. بمعنی تابش و روشنی و پرتو مهر است همچو ماهتاب، ترکیبی آن آفت آب است' — the dictionary has both words, but the only etymology legible is Borhan's folk 'āfat-e āb'; Mo'in's Pahlavi āp/āftāp footnotes cannot be read. NB: tools/ref_page.py BQT:1 and BQT:49 render vol. 5 (تعلیقات, separately paginated) pages, not vol. 1.\")\n    if rc['ref'] == 'IRN:119':\n        rc['status'] = 'supports'\n        rc['note'] = (\"Now on disk: ocr/IRN/0119.txt (IRN_eliteraturebook.pdf page 130, printed p. 119 'اروند رود'): 'جزء نخست āp به معنی آب است، pāt از ريشهٔ پاییدن و -ān پسوند نسبت است و «اپاتان» به معنی جایی است که در آنجا از آب دریا و رود پاسبانی می‌کنند و آن را می‌پایند ... گفتهٔ ابن‌حوقل و استخری نیز گواه این معنی است که پاسبانان در آبادان دزدان دریا را از دزدی باز می‌داشتند' — Farahvashi says exactly what Nourai's ô-pât-ân arrow says (āp 'water' + pā- 'guard' + -ān). It remains Farahvashi's own hypothesis; Nyberg and Horn derive ābādān from *ā-pāta- 'protected' with no water element.\")\n\n# ---------- node 3 ----------\nn = nodes[3]\nn['consulted'] = [HRN2, ARY51,\n    C(\"PHD\", \"MacKenzie s.v. zahabag and asyab (PHD_mackenzie.txt lines 5730, 1261)\", \"supports\",\n      \"'zahabag [zhʾpk | N zahāb] spring, source' and 'asyab [ʾsyʾp] (water-)mill' — MP zahābag is the direct source of NP zahāb; āsyāb is a genuine āb-compound.\"),\n    C(\"NYB\", \"Nyberg Part II (NYB_vol2_glossary.txt, grep zah-)\", \"silent\",\n      \"Only zahr 'poison' and zahyāi 'depth' at lines 4476-4477; no zahāp/zahābag entry.\"),\n    C(\"HUB\", \"Hübschmann Pers. Studien (HUB.txt, grep āb/zahāb)\", \"silent\",\n      \"No note on Horn no. 2 āb and no zahāb entry found in the OCR.\"),\n    C(\"MON\", \"Mo'in s.v. آب (MON_part1.txt line 748)\", \"partial\",\n      \"'آب ... (اِ.) مایعی است شفاف، بی‌طعم و بی‌بو؛ مرکب از دو عنصر اکسیژن و هیدروژن' — the headword is there but the bracketed origin tag ([په. āp]) is garbled in the OCR; زهاب headword not recoverable (see ref_check MON:1763).\"),\n    C(\"BQT\", \"vol. 1 p. 1 s.v. آب (BQT_v1_pages.txt line 5859) and vol. 3 p. 1225 s.v. شار (ocr/BQT/1225.vision.txt)\", \"partial\",\n      \"'آب ... معروف است که یکی از جملهٔ چهار عنصر باشد' (footnote unreadable); p. 1225 شار: 'و فرو ریختن آب و شراب و امثال آن باشد همچو آبشار و سرشار' with Mo'in fn 5 'گیلکی و دزفولی shorra (آوای فرو ریختن آب)' — supports the extra word آبشار = āb + šār 'pouring'; زهاب is not on that page (it is in vol. 2, OCR unreadable).\"),\n    C(\"LKT\", \"Lokotsch no. 5 Pers. abdār, p. 1 (LKT.txt line 228)\", \"supports\",\n      \"'5. Pers. abdār: [Aus āb \\\"Wasser\\\" od. \\\"Glanz\\\" Horn NpEt S. 1, Nr. 2 und 3, und Stamm dār- \\\"habend, haltend\\\"] \\\"wässerig, hell, glänzend\\\"' — Lokotsch, like Horn, keeps two homonyms āb 'water' (no. 2) and āb 'lustre' (no. 3).\")]\nfor rc in n['ref_check']:\n    if rc['ref'] == 'BQT:1225':\n        rc['status'] = 'partial'\n        rc['note'] = (\"Now on disk (vol. 3, BQT_v3_picofile.pdf page 16; running head ۱۲۲۵ confirmed on the page image, ocr/BQT/1225.png; transcription in ocr/BQT/1225.vision.txt): the page holds the entries شار … شارو, not زهاب. Entry شار: 'و فرو ریختن آب و شراب و امثال آن باشد همچو آبشار و سرشار ۵'; Mo'in footnote ۵: 'گیلکی و دزفولی shorra (آوای فرو ریختن آب) ... و غالباً در فارسی به تکرار «شارشار» گویند. رک: شاریدن' — so Nourai's BQT:1225 documents the extra word آبشار (āb + šār 'pouring'), not zahāb; for zahāb the reference is silent.\")\n    if rc['ref'] == 'IRN:108':\n        rc['status'] = 'supports'\n        rc['note'] = (\"Now on disk: ocr/IRN/0108.txt (IRN_eliteraturebook.pdf page 119, printed p. 108): 'این رود زاب ... در اصل ترکیب شده است از واژه‌های «زه» و «آب» و این ترکیب همانست که در واژهٔ «زهاب» در نام محل سرپل زهاب دیده می‌شود. در این ترکیب زه به معنی زاینده است از ريشهٔ zan- به معنی زاییدن و زهاب یا زاب به معنی رود زاینده است' — Farahvashi derives zahāb/Zāb from zah + āb as the arrow says (his gloss of zah as 'begetting' differs from MacKenzie's 'spring, source', but the āb element is agreed).\")\n\n# ---------- node 4 ----------\nnodes[4]['consulted'] = [LKT742,\n    C(\"WEB\", \"Webster's New 20th C. s.v. julep (WEB_vol1.txt line 102769, leaf 1026)\", \"supports\",\n      \"'julep, n. [Fr. julep; Sp. julepe; Ar. julab; Per. gulab, julep, rose water; gul, rose, and ab, water.] ... a cool drink containing aromatic herbs.'\"),\n    C(\"FSD\", \"Funk & Wagnalls vol. 2 s.v. julep (FSD_vol2.txt line 65496)\", \"supports\",\n      \"'julep ... n. 1. A drink composed usually of brandy or whisky, sugar, cracked ice ... mint. 2. A subacid, mucilaginous, sweetened drink, often used as a vehicle for ... medicine. [F, < Sp. julepe, < Ar. julāb, < Pers. gulāb ... water.]' (OCR partly garbled).\"),\n    C(\"DEV\", \"Devic p. 146 s.v. Julep (DEV.txt line 1581)\", \"supports\",\n      \"'Julep. Esp. et portug. julepe; ital. giulebbo, giulebbe; bas latin julapium. De l'arabe-persan جلاب djoulâb ou djoullâb, qui a le même sens' — Devic gives the Arabic-Persian julāb as source.\"),\n    C(\"PHN\", \"Pihan s.v. JULEP (a.-p.) (PHN.txt line 6310)\", \"supports\",\n      \"'JULEP, s. m. composé, (a.-p.) ... Potion médicinale, rafraîchissante ... Le terme arabe est une imitation du persan گلاب [gulāb] eau de rose, formé de گل [gul] rose, et de آب [āb] eau ... De là viennent aussi l'espagnol et le portugais julepe, ainsi que l'italien giulebbo et giulebbe.'\"),\n    C(\"LAM\", \"Lammens s.v. Julep (LAM.txt line 4694)\", \"supports\",\n      \"'Julep. Esp: julepe. Ptg: julepo. Majorq: culepe. It: giulebbo, giulebbe, de l'arabe جلاب goulâb ou goullâb, eau de rose; sirop. Ce mot d'origine persane est ancien en arabe. On le trouve cité dans un hadith'\"),\n    C(\"MON\", \"Mo'in s.v. گلاب (MON_part2.txt line 34161)\", \"supports\",\n      \"'گلاب: [- جلاب؛ معر.] (اِمر.) ... که از گل سرخ استخراج کنند و معطر است' — Mo'in gives the arabicized form جلاب julāb beside Persian گلاب.\"),\n    C(\"AFA\", \"Fraenkel p. 166 (AFA.txt line 5864, leaf 188)\", \"partial\",\n      \"In the discussion of rosātum: 'Dasselbe ist auch ... Cast. 809 \\\"Julabium\\\"' — Fraenkel only mentions Latin julabium in a note on Aramaic wine-words; no julāb entry.\"),\n    C(\"SKT\", \"Skeat (SKT.txt, grep julep)\", \"silent\", \"No julep entry found in the OCR of the Concise Dictionary.\")]\n\n# ---------- node 5 ----------\nn = nodes[5]\nn['consulted'] = [LKT79, DEV_ALAMBIC, PHN_ALAMBIC,\n    C(\"PLA\", \"Asbaghi p. 27 s.v. ambīq (PLA_pages.txt leaf 42, line 1929)\", \"supports\",\n      \"'ambīq: \\\"Alembik\\\" pers., mand. anpaqa (iranian, talm. ...), syr. ..., sp. alambique, engl. alembic, frz. alambic, dtsch. Alembik \\\"Destillierkolben\\\" [Wildhagen], wahrscheinlich aus dem pers. آبنیک ābnīk.' — Asbaghi is the (only) source of the ābnīk etymon; see ref_check PLA:22/PLA:27.\"),\n    C(\"MON\", \"Mo'in (MON_part1.txt, grep آبنیک; s.v. انبیق line 17169)\", \"contradicts\",\n      \"No headword آبنیک; 'انبیق: [غ. معر.] (اِ.) ظرفی است برای تقطیر مایعات' — Mo'in marks anbīq as Greek, arabicized.\"),\n    C(\"BQT\", \"Borhan-e Qate' vol. 1 (BQT_v1_pages.txt, grep آبنیک)\", \"silent\", \"No آبنیک entry in the OCR of vol. 1 (آ–ت).\"),\n    C(\"HRN\", \"Horn (HRN.txt, grep āb-nīk/nīk)\", \"silent\", \"No āb-nīk compound; Horn's āb-compounds are sīmāb, āb-dast etc.\"),\n    C(\"HUB\", \"Hübschmann (HUB.txt)\", \"silent\", \"Nothing on ābnīk or anbīq.\"),\n    C(\"ARY\", \"Aryanpur (ARY_pages.txt / latin index)\", \"silent\", \"No آبنیک or انبیق headword found.\")]\nfor rc in n['ref_check']:\n    if rc['ref'] == 'PLA:22':\n        rc['status'] = 'not_found'\n        rc['note'] = (\"Now on disk: PLA_pages.txt leaf 37 = printed p. 22 (running head 'isbahān 22 isfāhān') contains only the entries isbahān … isfāhān; nothing on āb-nīk. Asbaghi's ābnīk claim is on p. 27 s.v. ambīq (see node 6, PLA:27): 'wahrscheinlich aus dem pers. آبنیک ābnīk' — so the page number is wrong but the reference does make Nourai's claim. (ref_page.py PLA:22 rendered pdf page 22 = printed p. 7 'adab'; the offset is pdf = printed + 15.) Mo'in (MON_part1.txt line 17169) contradicts: 'انبیق: [غ. معر.]' = Greek, arabicized.\")\n\n# ---------- node 6 ----------\nn = nodes[6]\nn['consulted'] = [LKT79, SKT_ALEMBIC, DEV_ALAMBIC, PHN_ALAMBIC,\n    C(\"KLN\", \"Klein p. 47 s.v. alembic (KLN_1966.txt line 2149)\", \"contradicts\",\n      \"'fr. Arab. al-anbīq, the still, which is formed fr. al-, the, and Gk. ἄμβιξ, cup, cap of a still, alembic, which is of uncertain, possibly Semitic origin' — Greek, not Persian āb-nīk.\"),\n    C(\"MON\", \"Mo'in s.v. انبیق (MON_part1.txt line 17169)\", \"contradicts\", \"'انبیق: [غ. معر.] (اِ.) ظرفی است برای تقطیر مایعات و گرفتن عصاره و عرق' — origin tag غ. = Greek.\"),\n    C(\"AFM\", \"Addi Shir (AFM_pages.txt, grep انبيق/أنبيق)\", \"silent\", \"Addi Shir does not list anbīq among the arabicized Persian words (no hit for انبيق/الأنبيق).\"),\n    C(\"FVQ\", \"Jeffery (FVQ_pages.txt, grep anbīq/ambīq)\", \"silent\", \"Not a Qur'anic word; no entry.\"),\n    C(\"AFA\", \"Fraenkel (AFA.txt, grep ambix/Alembik)\", \"silent\", \"No entry.\")]\nfor rc in n['ref_check']:\n    if rc['ref'] == 'PLA:27':\n        rc['status'] = 'supports'\n        rc['note'] = (\"Now on disk: PLA_pages.txt leaf 42 = printed p. 27 (running head 'amīrāḫūr 27 ambīq'), last entry: 'ambīq: \\\"Alembik\\\" pers., mand. anpaqa (iranian, talm. ...), syr. ..., sp. alambique, engl. alembic, frz. alambic, dtsch. Alembik \\\"Destillierkolben\\\" [11 Wildhagen s.v.], wahrscheinlich aus dem pers. آبنیک ābnīk.' — Asbaghi does derive Arabic ambīq (and the European alembic words) from Persian āb-nīk, i.e. he is the source of Nourai's whole branch; but it is a lone 'wahrscheinlich' against Klein, Skeat, Lokotsch, Devic, Pihan, Webster's, Mo'in and all modern sources, which start from Greek ἄμβιξ.\")\n\n# ---------- node 7 ----------\nnodes[7]['consulted'] = [\n    C(\"LKT\", \"Lokotsch no. 79 Ar. anbīk, p. 8 (LKT.txt line 398)\", \"partial\",\n      \"'Ar. anbīk [Das selbst aus gr. ἄμβιξ ...] \\\"Destilliergefäß\\\"' — treats the Arabic word (from Greek); Persian anbīq not mentioned, but as an Arabic word it can only have reached Persian as a loan, as the chart draws.\"),\n    C(\"PLA\", \"Asbaghi p. 27 s.v. ambīq (PLA_pages.txt line 1929)\", \"partial\",\n      \"'ambīq: \\\"Alembik\\\" pers. ... wahrscheinlich aus dem pers. ābnīk' — Asbaghi reverses the direction (Persian → Arabic); he does not treat NP انبیق as an Arabic loan.\"),\n    C(\"BQT\", \"Borhan-e Qate' vol. 1 (BQT_v1_pages.txt, grep انبیق)\", \"silent\", \"No انبیق headword recoverable in the OCR of vol. 1.\"),\n    C(\"HRN\", \"Horn (HRN.txt, grep anbīq)\", \"silent\", \"Arabic loans are outside Horn's scope; no entry.\"),\n    C(\"ARY\", \"Aryanpur (ARY_pages.txt)\", \"silent\", \"No انبیق entry (not an Indo-European word).\")]\n\n# ---------- node 8 ----------\nnodes[8]['consulted'] = [\n    C(\"LKT\", \"Lokotsch no. 79, p. 8 (LKT.txt line 398)\", \"supports\", \"'... prov. elambic, frz. alambic, rum. alambic, sp. alambique, pg. lambique; engl. alembic' — Spanish alambique from Arabic al-anbīq with the article.\"),\n    C(\"DEV\", \"Devic p. 5 s.v. Alambic (DEV.txt line 270)\", \"supports\", \"'Esp. alambique, port. lambique, ital. lambico, de l'arabe al-anbīq ... précédé de l'article arabe al.'\"),\n    C(\"PHN\", \"Pihan s.v. ALAMBIC (PHN.txt line 1103)\", \"supports\", \"'Les Espagnols et les Portugais écrivent alambique.'\"),\n    C(\"PLA\", \"Asbaghi p. 27 s.v. ambīq (PLA_pages.txt line 1929)\", \"supports\", \"'sp. alambique, engl. alembic, frz. alambic, dtsch. Alembik' listed as descendants of Arabic ambīq.\"),\n    C(\"LAM\", \"Lammens p. ? s.v. almanach, note 2 (LAM.txt line 1610)\", \"partial\", \"'les Arabes ont fait pour almanach ce qu'ils ont fait pour almageste, alchimie, alambic, c'est-à-dire qu'ils ont accolé leur article à des mots grecs ou latins' — alambic cited as an Arabic article + Greek word; no separate entry.\"),\n    C(\"SKT\", \"Skeat s.v. Alembic, p. 12 (SKT.txt line 527)\", \"supports\", \"'(F. — Span. — Arab. — Gk.) ... F. alambique (Cot.); Span. alambique. — Arab. al, the; and anbīq' — Spanish stage between Arabic and French, as drawn.\")]\n\n# ---------- node 9 ----------\nnodes[9]['consulted'] = [SKT_ALEMBIC,\n    C(\"LKT\", \"Lokotsch no. 79, p. 8 (LKT.txt line 398)\", \"partial\", \"'Hieraus z. T. mit, z. T. ohne ar. Art. lat. alambicum und die romanischen Formen ... prov. elambic, frz. alambic' — French derived from Arabic via Latin alambicum / the Romance forms; Lokotsch does not single out Spanish (cf. Nourai's NOTE 'could be through Latin alambicum').\"),\n    C(\"DEV\", \"Devic p. 5 s.v. Alambic (DEV.txt line 270)\", \"partial\", \"French alambic 'de l'arabe al-anbīq' directly, with Esp. alambique, port. lambique, ital. lambico as parallels — no Spanish intermediary claimed.\"),\n    C(\"PHN\", \"Pihan s.v. ALAMBIC (PHN.txt lines 1095-1103)\", \"partial\", \"'il est probable que les chimistes ont emprunté directement ce terme aux Arabes' — French taken straight from Arabic, not through Spanish.\"),\n    C(\"LAM\", \"Lammens (LAM.txt line 1610)\", \"partial\", \"Only the passing remark that alambic is Arabic article + Greek word.\")]\n\n# ---------- node 10 ----------\nnodes[10]['consulted'] = [SKT_ALEMBIC,\n    C(\"LKT\", \"Lokotsch no. 79, p. 8 (LKT.txt line 398)\", \"supports\", \"'... prov. elambic, frz. alambic ...; engl. alembic' — English alembic among the Romance-mediated descendants of Arabic al-anbīq.\"),\n    C(\"FSD\", \"Funk & Wagnalls vol. 1 s.v. alembic and vol. 2 s.v. limbec (FSD_vol1.txt lines 11540-11542; FSD_vol2.txt line 76601)\", \"partial\", \"'a-lem'bic, n. 1. An apparatus of glass or ...' (etymology bracket not legible in the OCR) and 'limbec ... 1. Her. A bearing representing an alembic. 2. A still. [Contr. of alembic.]' — confirms the word and the aphetic limbec.\"),\n    C(\"KLN\", \"Klein p. 47 s.v. alembic and p. 884 s.v. limbec (KLN_1966.txt lines 2149, 21755)\", \"supports\", \"'alembic, n. — ME., fr. OF. (= F.) alambic' (already quoted in ref_check); 'limbec, n., alembic (archaic). — Aphetic for alembic.'\")]\n\n# ---------- node 11 ----------\nnodes[11]['consulted'] = [BRT_ANAP, CH_RAIC, HUB1015, PLA_IBRIQ,\n    C(\"PHD\", \"MacKenzie (PHD_mackenzie.txt, grep anab/abrez; lines 743-822)\", \"partial\",\n      \"No anāb or ābrēz headword; MacKenzie does list parallel āb-compounds 'ab-dān [ʾpdʾn] water-holder', 'ab-tāzān [ʾptʾcʾn] watercourse', 'ab-čihrag ... essence of water' — the type is Middle Persian, the two specific lemmas are unattested there.\"),\n    C(\"NYB\", \"Nyberg Part II (NYB_vol2_glossary.txt, grep anāp/āp-rēc)\", \"silent\", \"No anāp or āp-rēč entry; only āp 'water' (line 473) and the compounds āp-čihrak, āp-sārān, āpīk cross-referenced there.\")]\n\n# ---------- node 12 ----------\nnodes[12]['consulted'] = [HUB1015, CH_RAIC, PLA_IBRIQ,\n    C(\"MON\", \"Mo'in s.v. ناب (MON_part2.txt line 71128) and s.v. مبرز (line 44977)\", \"supports\",\n      \"'ناب: [بی آب، بدون آب] (ص.) خالص، بی‌غش، محض، صرف' — Mo'in glosses nāb etymologically as 'without water'; 'مبرز: [ع.] (اِ.) مبال؛ مستراح؛ آبریز، طهارت جای' gives ābrīz as the Persian synonym of 'latrine'; the آبریز headword itself is not recoverable in the OCR.\"),\n    C(\"HRN\", \"Horn no. 1015 nāb, p. ~221 (HRN.txt line 8831)\", \"supports\", \"'1015. nāb \\\"rein, ungemischt\\\". aw. anāp- \\\"ohne Wasser\\\"; phlv. anāp' (already quoted under ISS:3 in ref_check; listed here as an independent book).\"),\n    C(\"BQT\", \"Borhan-e Qate' vol. 1 (آبریز) and vol. 4 (ناب) OCR (BQT_v1_pages.txt, BQT_v4_pages.txt)\", \"silent\", \"grep آبریز in vol. 1 and ناب as a headword in vol. 4 returned nothing legible (Persian OCR of vols 3-5 is rough); not verified on the page images.\"),\n    C(\"ARY\", \"Aryanpur latin index (ARY_latin_index_pages.txt line 14751, pdf page 505)\", \"silent\", \"The only 'NAB (PAHLAVI)' in the index sits in the row NAPAT/NEFA/NEPHEW, i.e. it is Pahlavi nab 'grandson' under نوه, not nāb 'pure'; no آبریز or ناب 'pure' entry.\")]\n\n# ---------- node 13 ----------\nnodes[13]['consulted'] = [AFM_IBRIQ, PLA_IBRIQ, MON_IBRIQ,\n    C(\"AFA\", \"Fraenkel (AFA.txt, grep ibrīq)\", \"silent\", \"No ibrīq entry — consistent with the word being Persian, not Aramaic, in origin.\"),\n    C(\"LKT\", \"Lokotsch (LKT.txt, grep ibrīq/Ibrik)\", \"silent\", \"No entry for ibrīq/Ibrik among the European Orientalisms.\"),\n    C(\"KLN\", \"Klein (KLN_1966.txt, grep ibrik/ibriq)\", \"silent\", \"No entry.\")]\n\n# ---------- node 14 ----------\nnodes[14]['consulted'] = [PLA_IBRIQ, AFM_IBRIQ,\n    C(\"BQT\", \"Borhan-e Qate' vol. 1 (BQT_v1_pages.txt lines 6084, 6090)\", \"silent\",\n      \"ابریق occurs only inside other definitions ('بمعنی ابریق و آفتابه و مطهره و مانند آن', 'که آفتابه و ابریق باشد'); no ابریق headword with Mo'in's footnote is recoverable in the OCR.\"),\n    C(\"HRN\", \"Horn (HRN.txt, grep ibrīq/abrīz)\", \"silent\", \"Neither ābrīz nor the Arabic-shaped ibrīq is an entry in Horn.\"),\n    C(\"ARY\", \"Aryanpur (ARY_pages.txt)\", \"silent\", \"No ابریق entry.\")]\n\n# ---------- node 15 ----------\nnodes[15]['consulted'] = [LKT1619, HJB_DOAB, KLN_PUNCH,\n    C(\"SYN\", \"Buck 1.31 WATER / 1.36 RIVER (SYN.txt lines 1220-1420)\", \"silent\", \"Skt. āp- and NPers. āb are listed as cognates, but no Pañcāp/Panjāb compound.\"),\n    C(\"WLD\", \"Walde-Pokorny Bd. I p. 46 (WLD_Bd1_pages.txt leaf 55)\", \"silent\", \"Root article lists Skt. āp-, Av. āfš etc.; no Punjab.\"),\n    C(\"AID\", \"Whitworth Anglo-Indian Dictionary (AID.txt, grep Panj/Punj)\", \"silent\", \"Panjāb appears only inside other entries (Adi Granth, Akāli, Anjaman ...); no headword or etymology.\"),\n    C(\"FSD\", \"Funk & Wagnalls vol. 3 gazetteer s.v. Punjab (FSD_vol3.txt line 8572)\", \"silent\", \"'Punjab. ... NW Himalayas. 1,200 sq m.' — geographical entry only, no etymology.\"),\n    C(\"MON\", \"Mo'in (MON_part1/2.txt, grep پنجاب)\", \"silent\", \"No پنجاب headword recoverable in the OCR.\")]\n\n# ---------- node 16 ----------\nnodes[16]['consulted'] = [LKT1619, HJB_DOAB,\n    C(\"FSD\", \"Funk & Wagnalls vol. 3 gazetteer s.v. Punjab (FSD_vol3.txt line 8572)\", \"partial\", \"'Punjab. ... NW Himalayas. 1,200 sq m. 2. Its capital ...' — attests the English spelling Punjab; no etymology.\"),\n    C(\"KLN\", \"Klein (KLN_1966.txt, grep Punjab/Panjab/doab)\", \"silent\", \"No Punjab or doab entry (only 'doab' cross-referenced s.v. abdest, p. 2).\"),\n    C(\"SKT\", \"Skeat (SKT.txt, grep Punjab)\", \"silent\", \"No entry.\"),\n    C(\"WEB\", \"Webster's New 20th C. vol. 1 (WEB_vol1.txt, grep Punjab)\", \"silent\", \"Only Punjabi in the list of Indic languages (line 90784); the P- entries are outside vol. 1 on disk.\")]\n\n# sanity: every node has >=2 consulted from different books\nfor nid, nn in nodes.items():\n    srcs = {c['src'] for c in nn['consulted']}\n    assert len(srcs) >= 2, nid\n    for c in nn['consulted']:\n        assert c['stance'] in ('supports','contradicts','partial','silent'), (nid, c)\n\nwith io.open(P, 'w', encoding='utf-8') as f:\n    json.dump(d, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written; nodes', len(nodes))\n"
}
```


### [2026-09-04T18:22:07.688Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/apply_p31.py (file state is current in your context — no need to Read it back)
```


## [2026-09-04T18:22:16.497Z] TOOL CALL #43: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/apply_p31.py && python3 -m json.tool data/verification/page-31.json > /dev/null && echo JSON_OK && python3 tools/verify_check.py 31 && python3 - <<'EOF'\nimport json, collections\nd=json.load(open('data/verification/page-31.json'))\ne=d['entries'][0]\nst=collections.Counter(); books=collections.Counter()\nfor c in e.get('consulted',[]): st[c['stance']]+=1; books[c['src']]+=1\nfor n in e['nodes']:\n    for c in n['consulted']: st[c['stance']]+=1; books[c['src']]+=1\nprint('incl. root:', dict(st), sum(st.values())); print(sorted(books))\nfor n in e['nodes']:\n    for rc in n['ref_check']:\n        if rc['ref'] in ('BQT:1,49','IRN:119','IRN:108','BQT:1225','PLA:22','PLA:27'): print(n['id'], rc['ref'], rc['status'])\nEOF\ngit status --short",
 "description": "Apply the update, validate JSON, run verify_check and tally"
}
```


### [2026-09-04T18:22:18.776Z] TOOL RESULT

```
written; nodes 16
JSON_OK
nodes verified: 16/16
node verdicts: {'confirmed': 11, 'disputed': 4, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 12, 'partial': 4, 'not_checked': 4, 'contradicts': 2, 'not_found': 2}
books consulted: {'supports': 39, 'contradicts': 19, 'partial': 19, 'silent': 32} | by book: {'LKT': 11, 'HRN': 8, 'MON': 8, 'PLA': 7, 'ARY': 6, 'BQT': 6, 'SKT': 6, 'HUB': 5, 'DEV': 5, 'PHN': 5, 'KLN': 5, 'PHD': 4, 'NYB': 4, 'CHEUNG': 4, 'FSD': 4, 'LAM': 3, 'AFA': 3, 'AFM': 3, 'BRT': 2, 'WLD': 2, 'WEB': 2, 'HJB': 2, 'KNT': 1, 'FVQ': 1, 'SYN': 1, 'AID': 1}
incl. root: {'supports': 45, 'partial': 20, 'contradicts': 19, 'silent': 32} 116
['AFA', 'AFM', 'AHD', 'AID', 'ARY', 'BQT', 'BRT', 'CHEUNG', 'DEV', 'FSD', 'FVQ', 'HJB', 'HRN', 'HUB', 'IEC', 'KLN', 'KNT', 'LAM', 'LKT', 'MON', 'NYB', 'PHD', 'PHN', 'PLA', 'SKT', 'SYN', 'WEB', 'WLD']
2 BQT:1,49 partial
2 IRN:119 supports
3 BQT:1225 partial
3 IRN:108 supports
5 PLA:22 not_found
6 PLA:27 supports
 M data/verification/page-31.json
 M data/verification/sources/web/index.jsonl
?? data/verification/sources/web/1434f0e1b9b9efaf.txt
?? data/verification/sources/web/164451e81ebc84d8.txt
?? data/verification/sources/web/1ec52071e8412e12.txt
?? data/verification/sources/web/2b6fb8fe67946706.txt
?? data/verification/sources/web/3330ab177a4310bb.txt
?? data/verification/sources/web/343f0d6122563b9e.txt
?? data/verification/sources/web/3ef8647d4ccc22af.txt
?? data/verification/sources/web/481e10d7c983be67.txt
?? data/verification/sources/web/502cae4552b1f9f6.txt
?? data/verification/sources/web/592e452f63db0413.txt
?? data/verification/sources/web/5d9f56ec33a4be23.txt
?? data/verification/sources/web/6705660c9331c56e.txt
?? data/verification/sources/web/7191e2277240767c.txt
?? data/verification/sources/web/74b1dfd510ae07a0.txt
?? data/verification/sources/web/84797bff845fa8f4.txt
?? data/verification/sources/web/8dc356d5b98d7f9b.txt
?? data/verification/sources/web/9271f40e20f0e45d.txt
?? data/verification/sources/web/9c835b7d502e3ae2.txt
?? data/verification/sources/web/a4bcccc2e05357e4.txt
?? data/verification/sources/web/a69d8e203fe0d4ff.txt
?? data/verification/sources/web/a6ba4e0fea3b8f19.txt
?? data/verification/sources/web/a79258c7fe012fe6.txt
?? data/verification/sources/web/b60009fa4b7f1c12.txt
?? data/verification/sources/web/be3348e92a3dd02f.txt
?? data/verification/sources/web/c2b4c1fb59b8f19a.txt
?? data/verification/sources/web/c73ecb7ce905c5e2.txt
?? data/verification/sources/web/cf1e707350809384.txt
?? data/verification/sources/web/d4fcfb7cc6766634.txt
?? data/verification/sources/web/d6f7206383f161c3.txt
?? data/verification/sources/web/dcd40df518ed1b47.txt
?? data/verification/sources/web/f13fc692782489b9.txt
?? data/verification/sources/web/f7773a8aa6c1f5a2.txt
```


## [2026-09-04T18:22:40.957Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-31.json` now carries a `consulted` array on the root entry and on all 16 nodes; `python3 tools/verify_check.py 31` passes with 0 PROBLEM lines (16/16 nodes; books consulted: supports 39, contradicts 19, partial 19, silent 32 on nodes, plus 7 root-level entries — 116 total).

**Books used (28):** POK (already in ref_check), WLD Bd. I p. 46, AHD/Watkins, IEC, SYN (Buck 1.31/1.36), ARY p. 51 (page image read; transcript saved to `sources/refs/ocr/ARY/0051.vision.txt`), BRT (an-āpa- col. 122), KNT, PHD, NYB (āp, āpātān), HRN (nos 2, 3, 4, 8, 1015), HUB (1015), CHEUNG (*tap p. 379, *huar1 p. 147, *Hraič p. 181), BQT vol. 1 OCR (آب, آفتاب) and vol. 3 p. 1225 (image read; transcript in `ocr/BQT/1225.vision.txt`), MON, IRN pp. 108/119, PLA pp. 2-3/22/27, AFM (الإبريق), AFA, FVQ, KLN, SKT, FSD, WEB, LKT (nos 5, 79, 742, 1619), PHN, DEV, LAM, HJB (DOAB), AID. No web pages were used, so `sources` is unchanged.

**ref_check upgrades (books now on disk):**
- #2 `IRN:119` not_checked → **supports** (Farahvashi: «جزء نخست āp به معنی آب است، pāt از ريشهٔ پاییدن و -ān پسوند نسبت» — the source of the ābādān = āb+pā claim; still contradicted by Nyberg/Horn *ā-pāta-).
- #2 `BQT:1,49` not_found → **partial** (vol. 1 OCR has آب p. 1 and آفتاب p. ~49 with Borhan's own folk-etymology «ترکیبی آن آفت آب است»; Mo'in's footnotes unreadable). Note: `ref_page.py BQT:1/49` renders vol. 5 pages, not vol. 1.
- #3 `IRN:108` not_checked → **supports** (زاب/زهاب «ترکیب شده است از واژه‌های زه و آب»).
- #3 `BQT:1225` not_found → **partial**: page 1225 (confirmed on image) is the شار entry — «فرو ریختن آب … همچو آبشار و سرشار» — i.e. it documents the extra word آبشار, not zahāb.
- #5 `PLA:22` not_checked → **not_found** (p. 22 = isbahān entries; wrong page).
- #6 `PLA:27` not_checked → **supports**: Asbaghi s.v. ambīq «… sp. alambique, engl. alembic, frz. alambic … wahrscheinlich aus dem pers. آبنیک ābnīk» — he is the sole source of Nourai's ābnīk branch.
- ISS:3 and AEF:10 remain not_checked (not on disk).

**Verdict changes:** none. Node 2 stays disputed (Horn, Nyberg, Cheung all separate āftāb, ābādān, āxwarr from āb); nodes 5-6 stay disputed even though PLA:27 supports Nourai, because Klein, Skeat, Lokotsch, Devic, Pihan, Webster's and Mo'in unanimously derive anbīq from Greek ἄμβιξ; node 15's Sanskrit label is further contradicted by Lokotsch no. 1619 (pānǧ-āb 'Pandschab' as Persian).
