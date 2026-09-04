# Verification process log — refcheck-pilot-pages-101-126-311-345


## [2026-09-04T15:06:37.770Z] INPUT

Task: add the reference-check layer to four verification files that were produced before it was required. Files: /home/sfmqrb/git/rishe/data/verification/page-101.json, page-126.json, page-311.json, page-345.json. The corresponding charts (with Nourai's citations per node, `refs=`) are in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-<N>.txt.

Read /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md, specifically the sections "Checking Nourai's OWN cited references" and "Process documentation". The reference table is /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json (local OCR texts under /home/sfmqrb/git/rishe/data/verification/sources/refs/, paginated with form-feeds; each entry gives page offsets and lookup hints).

For every entry (root-level refs) and every node in those four files, add a `ref_check` array exactly as specified (status ∈ supports / partial / contradicts / not_found / not_checked, with the quoted phrase and location in `note`). Check at least one reference per node where any is accessible; the most authoritative first (POK/AHD/KLN for IE roots, HRN/HUB/BRT/KNT/PHD for Iranian, KLN/FVQ/AFM for Semitic, BQT/MON for Persian). Do NOT change any other field (verdicts, derivations, sources stay as they are) unless a reference check reveals the existing verdict is plainly wrong, in which case update the verdict and append a sentence to `derivation` explaining why, and mention it in your summary. If a check uses a web page (e.g. vajehyab for Mo'in), archive it with `python3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note '...'` and add the URL to the node's `sources`.

Write the files back in place (valid JSON, UTF-8), run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 101 126 311 345` (must show 0 PROBLEM lines and a non-empty "ref checks" tally), and reply with a short summary: ref-check status counts per page and a bullet for every `contradicts` (root, node, what the reference actually says).


## [2026-09-04T15:06:40.044Z] AGENT

I'll start by reading the instructions and the relevant sections.


## [2026-09-04T15:06:41.619Z] TOOL CALL #1: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && grep -n \"^#\" AGENT_INSTRUCTIONS.md | head -60; wc -l AGENT_INSTRUCTIONS.md",
 "description": "List section headings in instructions"
}
```


### [2026-09-04T15:06:41.683Z] TOOL RESULT

```
1:# Etymology verification task — instructions
13:## Your job, per chart (entry)
46:## Checking Nourai's OWN cited references (required)
84:## Process documentation (required)
101:## Sources to use (in roughly this order)
127:## Output — write ONE file per page
184 AGENT_INSTRUCTIONS.md
```


## [2026-09-04T15:06:45.502Z] TOOL CALL #2: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && sed -n 1,184p AGENT_INSTRUCTIONS.md",
 "description": "Read the full instructions file"
}
```


### [2026-09-04T15:06:45.547Z] TOOL RESULT

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
- Every node has `ref_check` (array, may contain a single `not_checked` item).
- Valid JSON only. Test it with `python3 -m json.tool` before finishing.
- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason).
  Do not paste the JSON back into your reply.
```


## [2026-09-04T15:06:47.005Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && for n in 101 126 311 345; do echo \"=== page-$n.txt ===\"; cat charts/page-$n.txt; echo; done",
 "description": "Print the four chart files"
}
```


## [2026-09-04T15:06:47.802Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && for n in 101 126 311 345; do echo \"=== page-$n.json ===\"; cat page-$n.json; echo; done",
 "description": "Print the four verification JSON files"
}
```


### [2026-09-04T15:06:48.867Z] TOOL RESULT

```
=== page-101.txt ===
=== PDF page 101 (book page 71) ===
--- entry 0 ---
ROOT [Semitic] B.r.k : originally "to kneel" used of the camel. Eventually the root developed the sense of "to bless".  (refs FVQ:75)
#1 (parent #0) [Arabic] refs=KLN:164; FVQ:75 | b.r.k : to bless ; barakat : blessing
  #2 (parent #1) [Persian] refs=FVA:45 | barekat «برکت» : blessing | extra: تبریک ، تبرّک ، مبارک
#3 (parent #0) [Akkadian] refs=KLN:164; AHD:579 | karâbu : to bless (letters are interchanged)
#4 (parent #0) [Hebrew] refs=KLN:164, 274 | berâkah : blessing ; kerŭbh : a winged angel (consonants R & B are reversed)
  #5 (parent #4) [Arabic] refs=MON:2958 | karŭbiyy : a winged angel
    #6 (parent #5) [Persian] refs=MON:2958 | karrŭbî «کرّوبی» : angel | extra: کروبیان، کروبیون
  #7 (parent #4) [English] refs=AHD:231 | cherub : a winged angel (of love)
  #8 (parent #4) [Greek] refs=AHD:579; KLN:680 | gruphos, grups : an eagle-headed lion
    #9 (parent #8) [Latin] refs=AHD:579 | gryphus
      #10 (parent #9) [Old French] refs=KLN:680 | grifion
        #11 (parent #10) [English] refs=AHD:579 | griffin
--- entry 1 ---
ROOT [Semitic] B.r.q : to shine  (refs KLN:514)
#1 (parent #0) [Arabic] refs=KLN:514 | b.r.q : to shine
  #2 (parent #1) [Persian] refs=FVA:45; SOR:35 | barq «برق» : lightning, electricity | extra: برّاق ، بارقه
#3 (parent #0) [Akkadian] refs=KLN:514 | baraqtu : lightning
#4 (parent #0) [Greek] refs=KLN:514 | smaraldos : a shiny stone, emerald
  #5 (parent #4) [Arabic] refs=MON:1746 | 
    #6 (parent #5) [Persian] refs=MON:1746; KLN:514 | zomorrod «زمرّد» : emerald
  #7 (parent #4) [Latin] refs=KLN:514 | smaragdus
    #8 (parent #7) [English] refs=AHD:427 | smaragdite : a green mineral
    #9 (parent #7) [Old French] refs=KLN:514 | esmeralde
      #10 (parent #9) [English] refs=AHD:427 | emerald
#11 (parent #0) [Sanskrit] refs=SKT:163; KLN:514 | marakata : emerald

=== page-126.txt ===
=== PDF page 126 (book page 96) ===
--- entry 0 ---
ROOT [Indo-European] Dheigh, Dhigha : to form out of clay, to knead clay or dough  (refs POK:244; KNT:191; CEL3:203)
#1 (parent #0) [Old Persian] refs=HRN:133; KNT:191; IEC:191 | didâ, děğa-vâra : clay wall ☞Wer 3
  #2 (parent #1) [Persian] refs=BQT:918 | dîvâr «دیوار» : wall
  #3 (parent #1) [Sogdian] refs=SOD:151 | dyz` : fort
#4 (parent #0) [Avestan] refs=POK:244 | daeza : wall, fortification
  #5 (parent #4) [Persian] refs=BQT:851; MON5:528 | dež «دژ ( دژبان، دژدار )» : fort ; dež-pol «دژ پل ( دزفول )» : strong bridge
  #6 (parent #4) [Avestan] refs=POK:244 | pairi-daeza : with walls around it (garden) ☞Per 1
    #7 (parent #6) [Persian] refs=BQT:359; MON:680 | pâlîz, jâlîz «پالیز ، جالیز» : melon farm
    #8 (parent #6) [Persian] refs=BQT:1455 | pardîs, ferdows «پردیس ، فردوس» : heaven
    #9 (parent #6) [Greek] refs=AHD:950 | paradeisos : garden, park
      #10 (parent #9) [English] refs=None | paradise
#11 (parent #0) [Old Persian] refs=HUB:65; KLN:469 | daika : clay pot
  #12 (parent #11) [Persian] refs=BQT:912,914; KLN:469 | dîg «دیگ ( دیزی )»
#13 (parent #0) [Germanic] refs=AHD | daigaz : dough ; dîg : one who kneads dough, lady of the house
  #14 (parent #13) [English] refs=None | dough ; lady, dairy
#15 (parent #0) [Latin] refs=AHD | figŭra : result of kneading, shape
  #16 (parent #15) [English] refs=None | figure, fiction

=== page-311.txt ===
=== PDF page 311 (book page 281) ===
--- entry 0 ---
ROOT [Indo-European] Leudh, Rei : to grow  (refs POK:684; KLN:885; SYN:874; VDQ:39)
#1 (parent #0) [Avestan] refs=KLN:885; SYN:874 | raod 1, raoda, raodha : growth, face
  #2 (parent #1) [Persian] refs=BQT:944 | rŭy-îdan «روییدن ( رُستن )» : to grow ; rŭy 1 «روی ۱ ( رو )» : face
    #3 (parent #2) [Persian] refs=BQT:944; FSF:199 | raz «رَز ۱ ( رَزبان ، رَزبُن )» : garden, vineyard, vine
      #4 (parent #3) [Arabic] refs=PLA:138 | rauza : garden | NOTE: AFM:75 derives this from Persian "rîxtan: to pour"; see "Leigh 2".  VDQ:226 derives it from Pahlavi "rôt: river"; see "Ser 1".
        #5 (parent #4) [Persian] refs=MON | rowzeh «روضه ( ریاض )» : garden
    #6 (parent #2) [Persian] refs=None | rŭnîk «رونیک ( نیکروی )» : beautiful ☞Nei 1
      #7 (parent #6) [Arabic] refs=AFM:74 | raonaq : beauty, splendor
        #8 (parent #7) [Persian] refs=MON:1694 | rownaq «رونق» : growth, success
#9 (parent #0) [Pahlavi] refs=MON:1689 | rôstâk : village
  #10 (parent #9) [Persian] refs=IEC:1103; MON:1689 | rŭstâ «روستا ( روستای )» : village
#11 (parent #0) [Avestan] refs=KLN:885; SYN:874 | raodha-taxma : grown strong, name of a legendary hero ☞Tenk
  #12 (parent #11) [Persian] refs=BQT | Rostam «رُستم» : a legendary hero
#13 (parent #0) [Avestan] refs=VDQ:39; MAG:186 | hava-rd : well grown, well built, beautiful ☞Su 1
  #14 (parent #13) [Pahlavi] refs=MAG:186; VDQ:39 | hu-rust : well built, beautiful ☞Su 1
    #15 (parent #14) [Arabic] refs=VDQ:39; MAG:186 | hŭr : houries of paradise
      #16 (parent #15) [Persian] refs=MON:1378 | hŭr 1 «حور» : a heavenly woman | extra: حوری ، حورالعین ، حوروش
#17 (parent #0) [Sogdian] refs=SOD:344 | rwd : to grow
#18 (parent #0) [Indo-European] refs=KLN:885 | leudho : people ; leudheros : free
  #19 (parent #18) [Latin] refs=None | liber : free
    #20 (parent #19) [English] refs=None | liberty, deliver, Latvia

=== page-345.txt ===
=== PDF page 345 (book page 315) ===
--- entry 0 ---
ROOT [Pahlavi] Murvârît : small pearl  (refs PLA:247; FVQ:261)
#1 (parent #0) [Persian] refs=BQT:1997; FVQ:261; KGW:112 | morvârîd «مروارید» : pearl | NOTE: BQT derives this word from Greek
#2 (parent #0) [Aramaic] refs=FVQ:261 | 
  #3 (parent #2) [Arabic] refs=FVQ:261; PLA:247 | mardjân : pearl, coral
    #4 (parent #3) [Persian] refs=BQT:1981 | marjân «مرجان» : coral
#5 (parent #0) [Greek] refs=AHD:1527; KGW:111; FVQ:261 | margarites : pearl
  #6 (parent #5) [Latin] refs=None | 
    #7 (parent #6) [Old French] refs=None | 
      #8 (parent #7) [English] refs=None | margarite, margarine, Margaret, Marjorie, Margarita, Maggie, Rita
--- entry 1 ---
ROOT Mus -> redirect to Mu
--- entry 2 ---
ROOT [Arabic] M.v.t : to die  (refs FVA:384; KLN:946)
#1 (parent #0) [Arabic] refs=FVA:387 | maot : death
  #2 (parent #1) [Persian] refs=FVA:387; MON:3678,4421 | mawt, mowt «موت ( مَمات )» : death ; mayyet «میّت» : dead person ; mât «مات» : dead, dull, confused ; kîš-mât «کیش مات» : "king is dead", checkmate ☞Ksei 1
    #3 (parent #2) [Latin] refs=FSD:1526 | mattus : dull, dead | NOTE: POK:694 derives Latin "mattus" from Indo-European root "Mad: wet".
      #4 (parent #3) [French] refs=FSD:1526 | mat : dull
        #5 (parent #4) [English] refs=FSD:526 | mat 1 : dull | NOTE: AHD:805 derives English "mat" from root "Mad".
      #6 (parent #3) [French] refs=PHN:257; DEV:159 | mat : defeated ; e'chec et mat : checkmate | NOTE: "checkmate" reached Europe through debatable paths
        #7 (parent #6) [English] refs=LKT:115; KLN:946 | mate 2 : to overcome ; checkmate
#8 (parent #0) [Spanish] refs=KLN:946 | matar : to kill ; matador : (bull) killer
  #9 (parent #8) [French] refs=MON:3678 | matador
    #10 (parent #9) [Persian] refs=MON:3678 | mâtâdor «ماتادُر»
  #11 (parent #8) [English] refs=KLN:946 | matador
```


### [2026-09-04T15:06:50.605Z] TOOL RESULT

```
<persisted-output>
Output too large (78.8KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bpqc1v83e.txt

Preview (first 2KB):
=== page-101.json ===
{
  "pdf_page": 101,
  "book_page": 71,
  "verified_by": "claude-fable-5-1",
  "verified_on": "2026-09-04",
  "entries": [
    {
      "entry": 0,
      "root": "B.r.k",
      "verdict": "confirmed",
      "modern_form": "Semitic root b-r-k: Proto-Semitic *birk- 'knee' / West Semitic brk 'to kneel; to bless' (AHD Semitic roots brk)",
      "note": "The root is real and its label 'Semitic' is right. Wiktionary reconstructs Proto-Semitic *birk- 'knee' (Akk. birkum, Heb. berekh, Ug. brk, Syr. burkā, Ge'ez bərk) with a metathetic variant *rukbat- (Ar. rukba). The 'kneel (of a camel) > bless' story is the traditional Gesenius/BDB account and matches Arabic baraka 'to kneel (camel)' / bāraka 'to bless'. The AHD Semitic appendix (Nourai's own AHD source) instead treats brk 'to bless' as 'probably a metathesized variant of krb' (Akk. karābu 'to praise, bless') — that is the hypothesis underlying Nourai's Akkadian/Hebrew cherub branch; it is accepted by AHD and Klein but rejected by recent Hebrew lexicography (SAHD, citing Mitchell: metathesis of first and third radicals is extremely rare). The griffin sub-branch is speculative (Klein) and not adopted by AHD's own griffin entry.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/birk-",
        "https://ahdictionary.com/word/semitic.html",
        "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%83%D8%A9"
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Arabic",
          "words": "b.r.k; barakat",
          "verdict": "confirmed",
...
</persisted-output>
```


## [2026-09-04T15:06:50.772Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nprint(type(d), len(d))\nif isinstance(d,dict):\n    for k,v in d.items(): print(k, json.dumps(v,ensure_ascii=False)[:600]); print()\nelse:\n    for v in d: print(json.dumps(v,ensure_ascii=False)[:600]); print()\n\"; ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/",
 "description": "Inspect refs table and local OCR files"
}
```


## [2026-09-04T15:06:51.373Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/tools && sed -n 1,200p verify_check.py; ls /home/sfmqrb/git/rishe/tools",
 "description": "Read the verify_check tool"
}
```


### [2026-09-04T15:06:52.703Z] TOOL RESULT

```
<persisted-output>
Output too large (61.1KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bedrt28t5.txt

Preview (first 2KB):
<class 'dict'> 110
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱-

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

...
</persisted-output>
```


### [2026-09-04T15:06:52.745Z] TOOL RESULT

```
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
VER = os.path.join(ROOT, "data", "verification")


def page_no(path):
    return int(os.path.basename(path).split("-")[1].split(".")[0])


def main(argv):
    only = set(int(a) for a in argv[1:])
    missing_pages, problems = [], []
    tally = collections.Counter()
    root_tally = collections.Counter()
    ref_tally = collections.Counter()
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
    print(f"nodes verified: {nodes_done}/{nodes_total}")
    print("node verdicts:", dict(tally))
    print("root verdicts:", dict(root_tally))
    print("ref checks:", dict(ref_tally))
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
build_site.py
fetch_source.py
ganjoor.py
__pycache__
ref_locator
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
```


## [2026-09-04T15:07:00.821Z] AGENT (thinking)

I'll gather the refs table rows for the page abbreviations, list the local OCR files, review the four JSON files (ids/verdicts) compactly, and check the ref_locator tool's help.


## [2026-09-04T15:07:02.044Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['FVQ','KLN','AHD','FVA','MON','POK','KNT','CEL3','HRN','IEC','BQT','SOD','HUB','SYN','VDQ','FSF','PLA','AFM','MAG','KGW','FSD','PHN','DEV','LKT','SKT','SOR']:\n    v=d.get(k); print('=====',k); print(json.dumps(v,ensure_ascii=False,indent=1) if v else 'MISSING')\n\"",
 "description": "Print refs table rows for the needed abbreviations"
}
```


## [2026-09-04T15:07:03.569Z] TOOL CALL #8: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/; ls /home/sfmqrb/git/rishe/tools/ref_locator; head -60 /home/sfmqrb/git/rishe/tools/ref_locator/*.py 2>/dev/null | head -120; sed -n 1,60p /home/sfmqrb/git/rishe/tools/fetch_source.py",
 "description": "List local OCR files and ref_locator/fetch_source tools"
}
```


### [2026-09-04T15:07:03.643Z] TOOL RESULT

```
===== FVQ
{
 "title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)",
 "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"
 ],
 "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)",
 "covers_etymology": true,
 "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites."
}
===== KLN
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ]
}
===== AHD
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website",
 "url": "https://ahdictionary.com/word/indoeurop.html",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
 "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition."
}
===== FVA
{
 "title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989",
 "kind": "none",
 "url": null,
 "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": true,
 "notes": "none online."
}
===== MON
{
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view."
}
===== POK
{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
 ]
}
===== KNT
{
 "title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953",
 "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/oldpers",
 "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt",
 "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.",
 "notes": ""
}
===== CEL3
MISSING
===== HRN
{
 "title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893",
 "edition_found": "1893 (Google scan, Univ. Michigan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/grundrissderneu00horngoog",
 "identifier": "grundrissderneu00horngoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.",
 "notes": "OCR of German Fraktur-free text is decent; Persian script is not OCRed."
}
===== IEC
{
 "title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87",
 "edition_found": "1984-1987 (complete, cols./pp. 1-1682)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987",
 "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt",
 "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.",
 "notes": ""
}
===== BQT
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary)",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)"
 ],
 "page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375.",
 "covers_etymology": true,
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition)."
}
===== SOD
{
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used."
}
===== HUB
{
 "title": "H. Hübschmann, Persische Studien, Strassburg 1895",
 "edition_found": "1895 (Google scan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/persischestudie00hbgoog",
 "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt",
 "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.",
 "notes": "Built from djvu.xml (no hocr); OCR quality moderate."
}
===== SYN
{
 "title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949",
 "edition_found": "1949 (reprint scans, same pagination in all printings)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt",
 "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.",
 "notes": "Two other open copies: dictionaryofselectedsynonyms...buck_963_N, fock_a-dictionary-...; restricted: dictionaryofsele0000carl."
}
===== VDQ
{
 "title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993",
 "kind": "website",
 "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)",
 "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": true,
 "notes": "Not on archive.org. Also on ghaemiyeh (ghbook.ir) as an app/EPUB per news reports."
}
===== FSF
{
 "title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/20220809_20220809_1444",
 "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"
 ],
 "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking",
 "covers_etymology": false,
 "notes": "Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Donya print Nourai used."
}
===== PLA
{
 "title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988",
 "edition_found": null,
 "kind": "none",
 "url": "https://catalog.hathitrust.org/Record/001080729",
 "identifier": null,
 "local_file": null,
 "page_offset": null,
 "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online.",
 "notes": "68 citations - the most-cited item NOT available. Alphabetical by Arabic word; Nourai's page numbers could be sanity-checked with HathiTrust full-text search (https://babel.hathitrust.org/cgi/ls?q1=<word>) which returns page hits even for search-only items."
}
===== AFM
{
 "title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)",
 "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"
 ],
 "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled."
}
===== MAG
{
 "title": "G. Widengren, Muhammad, the Apostle of God, and his Ascension (King and Saviour V), Uppsala 1955, ch. VIII 'Iranian elements in the Kuranic vocabulary'",
 "edition_found": null,
 "kind": "none",
 "url": "https://catalog.hathitrust.org/Record/001689168",
 "identifier": null,
 "local_file": null,
 "page_offset": null,
 "lookup_hint": "HathiTrust has it search-only (limited view); Google Books ids -r4rAAAAIAAJ / h20wAAAAYAAJ are snippet view.",
 "notes": "No full text online (1955 Swedish publication, in copyright)."
}
===== KGW
{
 "title": "J. Ibrahim, Kulturgeschichtliche Wortforschung: Persisches Lehngut in europäischen Sprachen, Wiesbaden 1991",
 "edition_found": null,
 "kind": "none",
 "url": "https://books.google.com/books?id=OUtZZNSUi3cC",
 "identifier": null,
 "local_file": null,
 "page_offset": null,
 "lookup_hint": "Google Books limited preview only (index pages).",
 "notes": "In copyright (1991); no full text online."
}
===== FSD
{
 "title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)",
 "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/in.ernet.dli.2015.147439",
 "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt",
 "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.",
 "notes": "Nourai cites 1940; page numbers in the New Standard were stable 1913-1940s (single-volume pagination 1-2814 continues across the DLI volumes). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt"
 ]
}
===== PHN
{
 "title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866",
 "edition_found": "1866",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/dictionnairetym01pihagoog",
 "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt",
 "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.",
 "notes": "Built from djvu.xml."
}
===== DEV
{
 "title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876",
 "edition_found": "1876",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/dictionnairety00devi",
 "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt",
 "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "French headword in caps at line start.",
 "notes": "Devic's text is also printed as the supplement of Littré (dictionnairedela00littuoft)."
}
===== LKT
{
 "title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927",
 "edition_found": "1927",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/etymologische00lokoguat",
 "identifier": "etymologische00lokoguat",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt",
 "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.",
 "notes": ""
}
===== SKT
{
 "title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)",
 "edition_found": "1911 'new and corrected impression' (Google scan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/aconciseetymolo01skeagoog",
 "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt",
 "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.",
 "notes": "Nourai says '1882-1967'; the 1967 Oxford reprint reproduces the 1911 rewritten edition, so the 1911 scan is the right pagination."
}
===== SOR
{
 "title": "K. Akhavan Zanjani — title unknown (Table IV entry for SOR lost in OCR; listed under Persian authors)",
 "kind": "none",
 "url": null,
 "lookup_hint": "Author search on archive.org/web found nothing.",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": false,
 "notes": "none online; title unidentified."
}
```


### [2026-09-04T15:07:03.691Z] TOOL RESULT

```
total 239468
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  4 10:56 .
drwxrwxr-x 4 sfmqrb sfmqrb     4096 Sep  4 11:03 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   600115 Sep  4 10:45 AFA.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   342401 Sep  4 10:50 AFM_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   354548 Sep  4 10:34 AFM.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   850109 Sep  4 10:40 AHD_watkins1985.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   824886 Sep  4 10:44 AHM.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1215090 Sep  4 10:44 AID.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   239712 Sep  4 10:45 AIN.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   255553 Sep  4 10:45 AKD.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   285355 Sep  4 10:39 ARB_abdulraheem.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1296442 Sep  4 10:39 ARB_mo3rb.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   743553 Sep  4 10:45 ARP.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   633097 Sep  4 10:45 AVG.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2634275 Sep  4 10:34 BQT_alt_v1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      146 Sep  4 10:35 BQT_dli_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 26399828 Sep  4 10:42 BQT_v1_djvu.xml
-rw-rw-r-- 1 sfmqrb sfmqrb  2247721 Sep  4 10:42 BQT_v1_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2620060 Sep  4 10:34 BQT_v1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  4339896 Sep  4 10:47 BQT_v2_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2359504 Sep  4 10:39 BQT_v2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  4803500 Sep  4 10:40 BRT.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   656131 Sep  4 10:45 BST.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1769485 Sep  4 10:52 CHEUNG.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   592705 Sep  4 10:44 DEV.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   143939 Sep  4 10:45 DOZ.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1499054 Sep  4 10:44 DRM.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   559516 Sep  4 10:45 EAV_studies.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1613053 Sep  4 10:49 FRS_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   890981 Sep  4 10:39 FRS.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 16441388 Sep  4 10:45 FSD_vol1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 16801850 Sep  4 10:47 FSD_vol2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 13277749 Sep  4 10:54 FSD_vol3.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 16697862 Sep  4 10:46 FSD_vol4.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2192488 Sep  4 10:48 FSF_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1152733 Sep  4 10:39 FSF.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   628003 Sep  4 10:49 FVQ_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   649903 Sep  4 10:34 FVQ.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   572506 Sep  4 10:44 GPL.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1572807 Sep  4 10:45 HENNING_selected_papers.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   448664 Sep  4 10:45 HID.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  5610600 Sep  4 10:40 HJB.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   688044 Sep  4 10:40 HRN.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   527491 Sep  4 10:40 HUB.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3311889 Sep  4 10:40 IEC.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3409804 Sep  4 10:47 ISS_alt_DKS.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1299560 Sep  4 10:39 KFL.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 10837854 Sep  4 10:40 KLN_1966.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 10278576 Sep  4 10:35 KLN_1971.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   873578 Sep  4 10:40 KNT.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   487736 Sep  4 10:44 LAM.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  4618386 Sep  4 10:45 LAT.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   627390 Sep  4 10:45 LEW_1910.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1056082 Sep  4 10:44 LKT.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    62059 Sep  4 10:45 LST.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  4377831 Sep  4 10:34 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  4331421 Sep  4 10:34 MON_part2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   372944 Sep  4 10:44 MPP.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   470206 Sep  4 10:45 NAT_2005.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   504627 Sep  4 10:38 NYB_vol1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   920054 Sep  4 10:40 NYB_vol2_glossary.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   664199 Sep  4 10:55 PEI.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  4 10:52 PHD_mackenzie.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   609465 Sep  4 10:52 PHD_mackenzie.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   340898 Sep  4 10:56 PHD.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   603979 Sep  4 10:44 PHN.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   981836 Sep  4 10:40 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1137861 Sep  4 10:40 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1170809 Sep  4 10:40 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3971883 Sep  4 10:35 POK_full.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  9753256 Sep  4 10:56 RCH.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1264311 Sep  4 10:39 SBK.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   225642 Sep  4 10:45 SDQ.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1365234 Sep  4 10:44 SIN.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2656202 Sep  4 10:40 SKT.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1292394 Sep  4 10:48 SNS_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   325929 Sep  4 10:39 SNS.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3741182 Sep  4 10:48 SOD_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1845041 Sep  4 10:39 SOD.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   466443 Sep  4 10:45 SPG_keilinschriften1881.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  4502081 Sep  4 10:40 SYN.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   243285 Sep  4 10:49 TAD_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   151889 Sep  4 10:39 TAD.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   312765 Sep  4 10:45 TLM.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    89292 Sep  4 10:45 UNV.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 12198872 Sep  4 10:45 WEB_vol1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   317372 Sep  4 10:45 WLD_band3.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   548741 Sep  4 10:45 ZAP.txt
djvu.sh
ia.sh
pageoff.py
paginate.py
==> /home/sfmqrb/git/rishe/tools/ref_locator/pageoff.py <==
import sys,re,collections
# usage: pageoff.py file  -> prints number of ff pages, most common (ffindex - printed) offsets, and sample
txt=open(sys.argv[1],encoding='utf-8',errors='replace').read()
pages=txt.split('\f')
print("ff pages:",len(pages), "chars:",len(txt))
offs=collections.Counter(); samples={}
for i,p in enumerate(pages):
    lines=[l.strip() for l in p.strip().split('\n') if l.strip()]
    cand=lines[:3]+lines[-3:]
    for l in cand:
        m=re.fullmatch(r'[—\-–\s]*(\d{1,4})[—\-–\s]*',l)
        if not m:
            m=re.match(r'^(\d{1,4})\s+\S',l) or re.search(r'\S\s+(\d{1,4})$',l)
        if m:
            n=int(m.group(1))
            if 0<n<3000:
                offs[i-n]+=1
                samples.setdefault(i-n,(i,n,l[:60]))
for o,c in offs.most_common(6):
    print(f"offset ff-printed={o}: {c} hits, e.g. ffpage {samples[o][0]} printed {samples[o][1]} line {samples[o][2]!r}")

==> /home/sfmqrb/git/rishe/tools/ref_locator/paginate.py <==
#!/usr/bin/env python3
"""usage: paginate.py <identifier> <out.txt> [basename-filter]
Builds a local text with \f between leaves (leaf i == ff-page i, 0-based) from IA hocr_searchtext+pageindex,
falling back to djvu.xml. Prints page_numbers-derived offset."""
import sys,json,gzip,io,re,collections,urllib.request,urllib.parse,html
ident,out=sys.argv[1],sys.argv[2]; filt=sys.argv[3] if len(sys.argv)>3 else ''
meta=json.load(urllib.request.urlopen(f'https://archive.org/metadata/{ident}'))
names=[f['name'] for f in meta['files'] if filt in f['name']]
def get(name):
    u=f'https://archive.org/download/{ident}/'+urllib.parse.quote(name)
    r=urllib.request.urlopen(u,timeout=300); data=r.read()
    if name.endswith('.gz'): data=gzip.decompress(data)
    return data
pi=[n for n in names if n.endswith('_hocr_pageindex.json.gz')]
st=[n for n in names if n.endswith('_hocr_searchtext.txt.gz')]
pages=[]
if pi and st:
    idx=json.loads(get(pi[0])); txt=get(st[0])
    for e in idx:
        pages.append(txt[e[0]:e[1]].decode('utf-8','replace'))
    src='hocr'
else:
    xmls=[n for n in names if n.endswith('_djvu.xml')]
    if not xmls: print('NO SOURCE',names); sys.exit(1)
    data=get(xmls[0]).decode('utf-8','replace')
    for obj in re.split(r'<OBJECT\b',data)[1:]:
        lines=[]
        for ln in re.findall(r'<LINE>(.*?)</LINE>',obj,re.S):
            words=re.findall(r'<WORD[^>]*>(.*?)</WORD>',ln,re.S)
            lines.append(html.unescape(' '.join(words)))
        pages.append('\n'.join(lines))
    src='djvuxml'
open(out,'w',encoding='utf-8').write('\f'.join(pages))
print(f'{ident}: {len(pages)} leaves written to {out} via {src}, {sum(len(p) for p in pages)} chars')
pn=[n for n in names if n.endswith('_page_numbers.json')]
if pn:
    d=json.loads(get(pn[0]))
    offs=collections.Counter(); ex={}
    for p in d['pages']:
        s=p.get('pageNumber') or ''
        if s.isdigit():
            o=p['leafNum']-int(s); offs[o]+=1; ex.setdefault(o,(p['leafNum'],int(s)))
    for o,c in offs.most_common(4):
        print(f'  page_numbers: leaf = printed + {o}  ({c} leaves, e.g. leaf {ex[o][0]} = p.{ex[o][1]})')
    nums=[int(p['pageNumber']) for p in d['pages'] if (p.get('pageNumber') or '').isdigit()]
    if nums: print(f'  printed range {min(nums)}-{max(nums)}')
#!/usr/bin/env python3
"""Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
"""
import sys, os, json, hashlib, re, html, time, urllib.request, urllib.parse

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
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-04T15:07:06.359Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && python3 -c \"\nimport json\nfor n in [101,126,311,345]:\n    v=json.load(open(f'page-{n}.json'))\n    print('=== page',n, [k for k in v.keys()])\n    for e in v['entries']:\n        print(' entry',e['entry'],e['root'],'|',e['verdict'],'| keys:',[k for k in e if k not in('nodes',)])\n        for nd in e['nodes']:\n            print('   #',nd['id'],nd['lang'],'|',nd['words'],'|',nd['verdict'],'| keys:',[k for k in nd if k not in ('id','lang','words','verdict','derivation','sources')])\n\"",
 "description": "Compact structural view of the four verification files"
}
```


### [2026-09-04T15:07:08.150Z] TOOL RESULT

```
=== page 101 ['pdf_page', 'book_page', 'verified_by', 'verified_on', 'entries']
 entry 0 B.r.k | confirmed | keys: ['entry', 'root', 'verdict', 'modern_form', 'note', 'sources']
   # 1 Arabic | b.r.k; barakat | confirmed | keys: []
   # 2 Persian | barekat | confirmed | keys: []
   # 3 Akkadian | karâbu | plausible | keys: []
   # 4 Hebrew | berâkah; kerŭbh | plausible | keys: []
   # 5 Arabic | karŭbiyy | confirmed | keys: []
   # 6 Persian | karrŭbî | confirmed | keys: []
   # 7 English | cherub | confirmed | keys: []
   # 8 Greek | gruphos, grups | plausible | keys: []
   # 9 Latin | gryphus | confirmed | keys: []
   # 10 Old French | grifion | plausible | keys: []
   # 11 English | griffin | confirmed | keys: []
 entry 1 B.r.q | confirmed | keys: ['entry', 'root', 'verdict', 'modern_form', 'note', 'sources']
   # 1 Arabic | b.r.q | confirmed | keys: []
   # 2 Persian | barq | confirmed | keys: []
   # 3 Akkadian | baraqtu | plausible | keys: []
   # 4 Greek | smaraldos | transcription_suspect | keys: []
   # 5 Arabic |  | plausible | keys: []
   # 6 Persian | zomorrod | disputed | keys: []
   # 7 Latin | smaragdus | confirmed | keys: []
   # 8 English | smaragdite | confirmed | keys: []
   # 9 Old French | esmeralde | confirmed | keys: []
   # 10 English | emerald | confirmed | keys: []
   # 11 Sanskrit | marakata | plausible | keys: []
=== page 126 ['pdf_page', 'book_page', 'verified_by', 'verified_on', 'entries']
 entry 0 Dheigh, Dhigha | confirmed | keys: ['entry', 'root', 'verdict', 'modern_form', 'note', 'sources']
   # 1 Old Persian | didâ, děğa-vâra | transcription_suspect | keys: []
   # 2 Persian | dîvâr | confirmed | keys: []
   # 3 Sogdian | dyz` | plausible | keys: []
   # 4 Avestan | daeza | confirmed | keys: []
   # 5 Persian | dež; dež-pol | confirmed | keys: []
   # 6 Avestan | pairi-daeza | confirmed | keys: []
   # 7 Persian | pâlîz, jâlîz | plausible | keys: []
   # 8 Persian | pardîs, ferdows | plausible | keys: []
   # 9 Greek | paradeisos | confirmed | keys: []
   # 10 English | paradise | confirmed | keys: []
   # 11 Old Persian | daika | disputed | keys: []
   # 12 Persian | dîg | disputed | keys: []
   # 13 Germanic | daigaz; dîg | confirmed | keys: []
   # 14 English | dough; lady, dairy | confirmed | keys: []
   # 15 Latin | figŭra | confirmed | keys: []
   # 16 English | figure, fiction | confirmed | keys: []
=== page 311 ['pdf_page', 'book_page', 'verified_by', 'verified_on', 'entries']
 entry 0 Leudh, Rei | confirmed | keys: ['entry', 'root', 'verdict', 'modern_form', 'note', 'sources']
   # 1 Avestan | raod 1, raoda, raodha | confirmed | keys: []
   # 2 Persian | rŭy-îdan; rŭy 1 | confirmed | keys: []
   # 3 Persian | raz | disputed | keys: []
   # 4 Arabic | rauza | disputed | keys: []
   # 5 Persian | rowzeh | confirmed | keys: []
   # 6 Persian | rŭnîk | plausible | keys: []
   # 7 Arabic | raonaq | disputed | keys: []
   # 8 Persian | rownaq | confirmed | keys: []
   # 9 Pahlavi | rôstâk | disputed | keys: []
   # 10 Persian | rŭstâ | confirmed | keys: []
   # 11 Avestan | raodha-taxma | disputed | keys: []
   # 12 Persian | Rostam | plausible | keys: []
   # 13 Avestan | hava-rd | transcription_suspect | keys: []
   # 14 Pahlavi | hu-rust | confirmed | keys: []
   # 15 Arabic | hŭr | disputed | keys: []
   # 16 Persian | hŭr 1 | confirmed | keys: []
   # 17 Sogdian | rwd | confirmed | keys: []
   # 18 Indo-European | leudho; leudheros | confirmed | keys: []
   # 19 Latin | liber | confirmed | keys: []
   # 20 English | liberty, deliver, Latvia | disputed | keys: []
=== page 345 ['pdf_page', 'book_page', 'verified_by', 'verified_on', 'entries']
 entry 0 Murvârît | confirmed | keys: ['entry', 'root', 'verdict', 'modern_form', 'note', 'sources']
   # 1 Persian | morvârîd | confirmed | keys: []
   # 2 Aramaic |  | plausible | keys: []
   # 3 Arabic | mardjân | confirmed | keys: []
   # 4 Persian | marjân | confirmed | keys: []
   # 5 Greek | margarites | confirmed | keys: []
   # 6 Latin |  | confirmed | keys: []
   # 7 Old French |  | confirmed | keys: []
   # 8 English | margarite, margarine, Margaret, Marjorie, Margarita, Maggie, Rita | confirmed | keys: []
 entry 2 M.v.t | confirmed | keys: ['entry', 'root', 'verdict', 'modern_form', 'note', 'sources']
   # 1 Arabic | maot | confirmed | keys: []
   # 2 Persian | mawt, mowt; mayyet; mât; kîš-mât | plausible | keys: []
   # 3 Latin | mattus | disputed | keys: []
   # 4 French | mat | plausible | keys: []
   # 5 English | mat 1 | confirmed | keys: []
   # 6 French | mat; e'chec et mat | disputed | keys: []
   # 7 English | mate 2; checkmate | confirmed | keys: []
   # 8 Spanish | matar; matador | plausible | keys: []
   # 9 French | matador | confirmed | keys: []
   # 10 Persian | mâtâdor | plausible | keys: []
   # 11 English | matador | confirmed | keys: []
```


## [2026-09-04T15:07:39.886Z] AGENT (thinking)

I'll run batched greps across the local reference files for all the pending lookups—KLN, FVQ, POK, AHD 1985, HRN, HUB, KNT, IEC, SYN, SOD, BQT, FSF, AFM, FSD, PHN, DEV, LKT, SKT, and MON—firing them independently to speed things up.


## [2026-09-04T15:07:41.622Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in '^bless,' '^cherub,' '^griffin,' '^emerald,' '^smaragd' '^dish,' '^liberal,' '^liberty,' '^mate,' '^matador,' '^checkmate,' '^paradise,' '^dough,' '^figure,' '^dairy,' '^lady,' '^deliver,' '^Latvia' '^margarite' '^Margaret,' '^Margarita' '^Marjorie' '^margarine' '^mat,' '^matt,' '^fiction,' '^smaragdite' '^Rita,' '^Maggie'; do echo \"## $w\"; grep -n \"$w\" KLN_1966.txt | head -3; done",
 "description": "Find KLN headword line numbers"
}
```


### [2026-09-04T15:07:43.835Z] TOOL RESULT

```
## ^bless,
5166:bless,  tr.  v.  —  ME.  blessen,  fr.  OE.  bledsian,  blet- sian,  ‘to  bless,  consecrate’,  rel.  to  OE.  blod. ‘blood’;  see  blood.  The  orig.  meaning  of  bless was  ‘to  sprinkle  or  consecrate  with  blood'  (said of  the  sacrificing  priest).
## ^cherub,
7347:cherub,  n.  —  Heb.  klrubh ,  ‘winged  angel’,  prob. rel.  to  Akkad,  karabu,  ‘to  bless’,  karibu,  ‘one who  blesses’,  epithet  of  the  bull-colossus,  and  to Heb.  bertikh,  ‘he  blessed’,  berakhdh,  ‘blessing’. See  berakah  and  cp.  griffin.
## ^griffin,
## ^emerald,
## ^smaragd
35636:smaragd,  n.,  an  emerald.  —  ME.  smaragde,  fr. OF.  smaragde,  fr.  L.  smaragdus,  fr.  Gk.  aptdpa- ySo g.  See  emerald.
35637:smaragdite,  n.,  a  green  variety  of  amphibole.  — F.,  formed  with  subst.  suff.  -ite  fr.  Gk.  ofxdpa- ySoc,  ‘emerald’.  See  prec.  word, smart,  intr.  v.  —  ME.  smerten,  fr.  OE.  smeortan, rel.  to  MDu.  smerten,  smarten,  Du.  smarten, OHG.  smerzan,  MHG.  smerzen,  G.  schmerzen, ‘to  pain*,  orig.  to  bite’,  rel.  to  LG.  marten,  ‘to
## ^dish,
11691:dish,  n.  —  ME.  disch,  fr.  OE.  disc,  ‘dish,  plate, bowl’,  rel.  to  ON.  diskr,  ‘dish’,  OS.  disk,  ‘table’, OHG.  tisc,  ‘dish;  table’,  MHG.,  G.  tisch, ‘table’,  fr,  L.  discus,  ‘quoit’,  in  Late  L.  ‘dish’ (so  called  because  of  its  shape),  fr.  Gk.  Stoxo?, ‘quoit,  disk’,  which  is  dissimilated  fr.  ‘Six-oxo? and  prop,  means  ‘that  which  is  thrown’,  from the  stem  of  Sixctv,  ‘to  throw,  cast',  whence  also Stxxuov,  ‘net’.  Cp.  dais,  desk,  disc,  discus  and the  second  element  in  oftish.  Cp.  also  Dictynidae, Dictynna,  dictyo-.
## ^liberal,
## ^liberty,
## ^mate,
23107:mate,  n.,  checkmate.  —  ME.  mat,  fr.  MF.,  fr.  OF. See  prec.  word.
23108:mate,  n.,  a  companion.  —  ME.,  fr.  MLG.  mate, mat,  ‘companion’,  orig.  ‘a  messmate’,  whence
## ^matador,
## ^checkmate,
## ^paradise,
## ^dough,
## ^figure,
14703:figure,  tr.  and  intr.  v.  —  F.  figurer,  fr.  L.  figurare, ‘to  form,  shape’,  fr.  figura.  See  figure,  n.,  and cp.  configure,  disfigure,  prefigure,  transfigure. Derivative:  figur-ed,  adj. figurine,  n.,  a  small  figure;  a  statuette.  —  F.,  fr. It.  figurina,  dimin.  of  figura,  fr.  L.  figura.  See figure,  n.,  and  -ine  (representing  L.  -inus). fig  wart,  a  condyloma.  -  Cp.  OE./ic,  MHG.  vie, veig,  ‘the  piles’,  fr.  L.  ficus,  ‘fig  tree,  fig;  the piles’  (see  fig,  n  );  so  called  from  its  shape. Filago,  n.,  a  genus  of  plants  of  the  thistle  family (hot.)  —  ModL.,  fr.  L.  filum,  ‘thread’.  See  file, ‘collection  of  papers’.  Cp.  Gifola. filament,  n.,  a  fine  thread,  fiber.  —  F.,  fr.  ModL. filamentum,  fr.  Late  L.  filare,  ‘to  spin’.  See  file, ‘collection  of  papers’,  and  -ment.
## ^dairy,
## ^lady,
21000:lady,  n.  —  ME.  lafdl,  lavede,  ladi,  fr.  OE.  hlxf- dlge,  ‘mistress  of  the  house’,  lit.  ‘loaf-maker’.
## ^deliver,
10738:deliver,  tr.  v.  —  OF.  delivrer  (F.  delivrer ),  ‘to  set free’,  fr.  VL.  deliberdre,  of  s.m.,  fr.  de-  and  libe- rare,  ‘to  set  free’,  fr.  liber,  ‘free’.  See  liberal  and cp.  liberate.
## ^Latvia
21237:Latvia,  n.  —  Lit.  ‘the  country  of  the  Letts’.  See Lett  and  cp.  lat.
## ^margarite
## ^Margaret,
## ^Margarita
## ^Marjorie
## ^margarine
22919:margarine,  n.,  artificial  butter.  —  F. ;  see  prec. word.  The  name  arose  from  the  erroneous  no¬ tion  that  all  oils  and  fats  contain  margaric  acid, margarite,  n.,  1)  a  pearl  (archaic)',  2)  a  basic aluminum  calcium  silicate  (mineral.)  —  ME.,  fr. OF.  margarite  (F.  marguerite),  fr.  L.  margarita, fr.  Gk.  papyapfxT)?  (scil.  Xiffop),  ’pearl’,  which is  of  uncertain  origin.  It  possibly  derives  fr.  OI. mahjaram,  mahjari,  ‘bud,  pearl  .  Gk.  pxpyapov is  prob.  a  back  formation  fr.  uxpyapf-nr,;.  Cp. Margaret,  margaric,  margarin,  marguerite.  For the  ending  see  subst.  suff.  -ite. margaritiferous,  adj.,  producing  pearls.  —  Com¬ pounded  of  L.  margarita,  pearl  ,  and  the  stem of  ferre,  ‘to  bear,  carry’.  See  prec.  word  and -ferous.
## ^mat,
23101:mat,  n.,  a  coarse  fabric  made  of  straw,  hemp, rushes,  etc.  —  ME.  matte,  fr.  OE.  matt,  fr.  Late L.  matta,  ‘mat  made  of  rushes’  (whence  also OHG.  matta,  MHG.,  G.  matte),  fr.  Phoem- Punic  matta,  corresponding  to  Heb.  mitta  , ‘bed’,  which  is  formed  from  the  stem  of  natd  , ‘he  bent’  (for  sense  development  cp.  Gk.  xXfvr„ ‘bed’,  fr.  xXtvEtv,  ‘to  bend’).  From  Late  L. natta,  a  secondary  form  of  Late  L.  matta,  which occurs  in  the  writings  of  Gregoire  de  Tours,  de¬ rives  F.  natte,  ‘mat,  matting’.  For  the  change of  Heb.-Punic  initial  m  to  n  cp.  F.  nappe, ‘tablecloth’,  fr.  L.  nappa,  which  derives  fr.  Heb.- Punic  mappdh  (see  napery,  napkin).
23103:mat,  adj.,  dull  (said  of  color  or  a  surface).  —  F., ‘dull,  lusterless,  unpolished’,  fr.  OF.  mat,  ‘de¬ feated,  afflicted,  depressed,  dejected;  dull’,  fr. Arab,  mat  in  the  sentence  mat  ash-shah,  ‘the king  has  died’.  The  word  mat,  orig.  used  only as  a  term  of  chess,  gradually  developed  also  the meanings  ‘faint,  feeble,  dull-colored .  See checkmate  and  cp.  matador,  mate,  adj. matador,  n.,  1)  the  man  who  kills  the  bull  in  the bullfight ;  2)  one  of  the  three  chief  cards  in  the game  of  ombre  and  quadrille.  —  Sp,,  ‘killer, murderer’,  fr.  matar,  ‘to  kill,  murder’,  fr.  Arab. mdta,  ‘he  died’.  Cp.  checkmate.  Cp.  also  mat, ‘dull’.
## ^matt,
## ^fiction,
14673:fiction,  n.  —  F.,  fr.  L.  fictidnem,  acc.  of  fictid,  ‘a forming,  shaping’,  fr.  fictus,  pp.  of  fingere,  ‘to form,  shape’.  The  original  meaning  of  this  verb was  ‘to  knead’.  It  derives  fr.  I.-E.  base  *dheigh-, *dhoigh-,  *dhigh-,  ‘to  knead,  form  out  of  clay, form,  shape’,  whence  also  OE.  dag,  ‘dough’;  see dough  and  -ion.  For  the  change  of  the  concrete meaning  to  the  abstract  cp.  L.  comprefiendere, ‘to  seize,  grasp;  to  comprehend,  understand’ (see  comprehend).
## ^smaragdite
35637:smaragdite,  n.,  a  green  variety  of  amphibole.  — F.,  formed  with  subst.  suff.  -ite  fr.  Gk.  ofxdpa- ySoc,  ‘emerald’.  See  prec.  word, smart,  intr.  v.  —  ME.  smerten,  fr.  OE.  smeortan, rel.  to  MDu.  smerten,  smarten,  Du.  smarten, OHG.  smerzan,  MHG.  smerzen,  G.  schmerzen, ‘to  pain*,  orig.  to  bite’,  rel.  to  LG.  marten,  ‘to
## ^Rita,
## ^Maggie
```


## [2026-09-04T15:07:45.373Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nprint(len(pages))\n# find the leaf containing certain headwords and show the printed page numerals at top\ndef find(pat):\n    for i,p in enumerate(pages):\n        if re.search(pat,p,re.M):\n            head=[l.strip() for l in p.strip().split('\\n')[:4]]\n            return i,head\n    return None\nfor pat in [r'^bless,', r'^cherub,', r'^griffin,', r'^emerald,', r'^dish,', r'^liberal,', r'^mate,', r'^matador,', r'^checkmate,', r'^paradise,', r'^dough,', r'^figure,', r'^margarite', r'^Margaret,']:\n    print(pat, find(pat))\nEOF",
 "description": "Locate KLN leaves for the headwords"
}
```


## [2026-09-04T15:07:47.632Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### FVQ leaf 92 (p.75)\"; awk 'BEGIN{RS=\"\\f\"} NR==93' FVQ_pages.txt; echo \"### FVQ leaf 278 (p.261)\"; awk 'BEGIN{RS=\"\\f\"} NR==279' FVQ_pages.txt; echo \"### FVQ grep marjan/lulu/baraka\"; grep -n -i 'marj\\|barak\\|bless' FVQ_pages.txt | head -30",
 "description": "Read FVQ pages 75 and 261"
}
```


### [2026-09-04T15:07:48.039Z] TOOL RESULT

```
903
^bless, (106, ['erred  to.  Cp.  also  blenny. blennorrhea,  blennorrhoea,  n.,  excessive  discharge of  mucus  ( med .)  —  Medical  L.,  compounded  of blenno-  and  -rrhea.', 'blenny,  n.,  a  small  seafish.  —  L.  blenttius,  fr.  Gk. (3X£vvoc;,  name  of  a  fish,  fr.  pXlvva,  ‘slime’,  lit. ‘slime  fish’;  so  called  from  the  mucus  which covers  its  skin.  See  blenno-. blepharo-,  before  a  vowel  blephar-,  combining form  meaning ‘eyelid’.— Gk.pXe^apo-.pXe^ap-, fr.  [JXc9apov  (Dor.  yX^ocpov),  ‘eyelid’,  which  is rel.  to  pxlrrstv  (Dor.  yXcTteLv),  ‘to  look,  sec’;  of uncertain  etymology.  Cp.  Ablepharus,  ablepsia, anableps.', 'blepharospasm,  n.,  contraction  of  the  eyelids (med.)  —  Compounded  of  blepharo-  and  Gk. amxapioc,  ‘spasm,  convulsion’.  See  spasm. Blephilia,  n.,  a  genus  of  plants  of  the  mint  family (bot.)  —  ModL.,  contraction  of  Gk.  [iXe^xpi?, ‘eyelash’  (which  is  rel.  to  flXeipapov,  ‘eyelid’), and  L.  cilium,  ‘eyelid’  (see  blepharo-  and  cilia); so  called  because  of  its  fringed  bracts  and  calyx teeth.', "bless,  tr.  v.  —  ME.  blessen,  fr.  OE.  bledsian,  blet- sian,  ‘to  bless,  consecrate’,  rel.  to  OE.  blod. ‘blood’;  see  blood.  The  orig.  meaning  of  bless was  ‘to  sprinkle  or  consecrate  with  blood'  (said of  the  sacrificing  priest)."])
^cherub, (155, ['See  alchemy  and  -ist.  Derivative:  chemist-ry,  n. chemo-,  combining  form  denoting  relation  to chemical  actions  or  chemicals.  —  See  chemic. chemosis,  n.,  swelling  of  the  conjunctiva  (med.)  — Medical  L.,  fr.  Gk.  yfioiaic,  ‘affection  of  the eye  in  which  the  cornea  swells  like  a  cockle¬ shell’,  fr.  yj],u. r],  ‘a  yawning,  gaping:  cockleshell’, which  is  rel.  to  yatvsiv,  ‘to  yawn,  gape’;  fr. I.-E.  base  *ghei-,  *ghi-,  ‘to  gape,  yawn’.  See chaos  and  -osis  and  cp.  chela,  ‘claw’, chemotherapy,  n.,  —  Coined  by  the  Jewish  bac¬ teriologist  and  chemist  Paul  Ehrlich  (1854-1915) fr.  chemo-  and  therapy.', 'Chen,  n.,  a  genus  of  geese,  the  snowgoosc  (orni- thol.)  —  Gk.  yfy,  ‘goose’,  rel.  to  Boeotian  y&v, for  */Sc,  ‘goose’.  See  goose  and  cp.  words  there referred  to.', 'chen-,  form  of  cheno-  before  a  vowel, chenevixite,  n.,  a  copper  and  iron  arsenate  (min¬ eral.)  —  Named  after  the  Irish  chemist  Richard Chenevix  who  analyzed  it.  For  the  ending  see subst.  suff.  -ite.', 'chenille,  n.,  tufted  cord  of  silk,  wool,  etc.  —  F., prop,  ‘caterpillar’,  fr.  L.  canicula,  ‘a  little  dog’, dimin.  of  canis,  ‘dog’.  See  canine, cheno-,  before  a  vowel  chen-,  combining  form meaning  ‘goose’.  —  Gk.  yryo-,  yyy-,  fr.  yfy, gen.  yyycz,  ‘goose’.  See  Chen.'])
^griffin, None
^emerald, None
^dish, (251, ['d  countenance.  Cp.  F.  de- contenancer.', 'discourage,  tr.  v.  —  OF.  descoragier,  descoura- gier  (F.  decourager),  fr.  des-  (fr.  L.  dis-)  and corage  (F.  courage).  See  dis-  and  courage  and cp.  encourage.', 'discouragement', 'dishonest'])
^liberal, None
^mate, (508, ['nis, ‘chewing,  mastication’,  fr.  masticatus,  pp.  of masticare.  See  masticate  and  -ion. mastiff,  n.  —  ME.  mastif,  fr.  OF.  muslin  (whence F.  matin),  fr.  VL.  *md(n)suetinus,  ‘tamed’,  fr. L.  mansuetus,  of  s.m.,  pp.  of  mansuescere,  ‘to tame’ ;  see  mansuete.  The  ending  of  E.  mastiff  is due  to  a  confusion  with  OF.  mestif,  ‘mongrel’, mastitis,  n.,  inflammation  of  a  breast  ( med .)  — Medical  L.,  coined  by  Konig  fr.  Gk.  aaoxo;, "breast’,  and  suff.  -tTiq.  See  masto-  and  -itis. masto-,  before  a  vowel  mast-,  combining  form meaning  ‘breast’.  — -  Gk.  p.a paaT-,  fr. [x\'/.n-ric,  ‘breast’,  which  prob.  stands  for  *trccS- toi;  and  derives  from  the  stem  of  paSav,  ‘to  be wet,  to  flow’,  fr.  I.-E.  base  *mad-,  ‘wet,  moist, dripping’.  See  mast,  ‘fruit  of  the  beech’,  and  cp. prec.  word,  mastoid,  mazo-,  ‘breast’,  amastia, bimastism.', 'mastodon,  n.,  an  extinct  elephantlike  mammal.  — ModL.,  compounded  of  mast-  and  Gk  68c ov, gen.  oSovtoc,  ‘tooth’  (see  odonto-);  so  called from  the  nipple-shaped  projections  on  the  mo¬ lar  teeth.', 'mastodontic,  adj.,  pertaining  to,  or  resembling,  a mastodon.  —  See  prec.  word  and  -ic. mastoid,  adj.,  resembling  a  breast  or  nipple.  — Gk.  paaTOEiS-r)!;,  compounded  of  paaro;, ‘breast’,  and  -oeiSt)!;,  ‘like’,  fr.  eT8oc,  ‘form, shape’ .  See  masto-  and  -oid.', 'Derivative:  mastoid,  n.,  the  mastoid  process  or bone.'])
^matador, None
^checkmate, None
^paradise, None
^dough, None
^figure, (320, ['alf-ripe  fig’.  Cp. Ficus,  the  first  element  in  ficoid  and  the  second element  in  beccafico,  caprification,  comfrey. fig,  tr.  v.,  to  dress.  —  A  var.  of  feague. Derivative:  fig,  n.,  dress;  condition.', '590', 'fight,  tr.  and  intr.  v.  —  ME.  fehten,  fr.  OE.  feoh- tan ,  rel.  to  OFris.  fiuhta,  OS.,  OHG.  fehtan, Du.  vechten,  MHG.  vehten,  G.  fechten,  fr.  I.-E. base  *pek-,  ‘to  pluck  out  (wool  or  hair)’,  whence also  Gk.  Trexeiv,  Att.  ttexteiv,  ‘to  comb,  shear’, xtelc,  gen.  xtevo ?  (for  *pkten-),  ‘comb’,  L. pecten,  gen.  -inis,  of  s.m.,  pectere,  ‘to  comb’. For  sense  development  cp.  Lith.  pesti,  ‘to  pluck out’,  su-si-pesti,  ‘to  fight,  scuffle’,  which  are  of the  same  base.  See  fee,  ‘cattle’,  and  cp.  pecten. Derivatives:  fight,  n.  (q.v.),fight-er,  n.,fight-ing, adj.,  fight-ing-ly,  adv.', 'fight,  n.  —  ME.  fiht,  fr.  OE.  feoht,  fr.  feohtan, ‘to  fight’.  See  fight,  v.'])
^margarite None
^Margaret, None
```


### [2026-09-04T15:07:49.677Z] TOOL RESULT

```
### FVQ leaf 92 (p.75)
FOREIGN VOCABULARY OF THE QUB/AN 75
magic, a fact which, we would also gather from the use of the word
Bavil in the Manichaean Uigur fragments from Idiqut-Schahri. 1
dtyJ (Baraka).
vii, 52, 133 ; xvii, 1 ; xxi, 71, 81, etc.
To bless.
j f s^-s
With this should be taken the forms C>LJ j> 9 (vii, 94 ; xi, 50, 76),
^ ^ ^
and &'j^+* (iii, 90 ; vi, 92, 156, etc.).
^
1 1 s-**
The primitive verb O j , which is not used in the Qur'an, means
to kneel, used specially of the camel, so that &j} * s t^ 10 technical
word for making a camel kneel. In this primitive sense it is common
Semitic, so we find Heb. HIPP ^3B7 n3133 " let us kneel
before Jehovah"; Syr. wiOJoaiao^l ^JQ " he knelt upon his
knees " ; Eth. <0Mt"fl^Vl- * ^fXO " and they bowed the knee
before him ". It was in the N. Semitic area, however, that the root
seems to have developed the sense of to 6Zess, and from thence it passed
to the 8. Semitic area. Thus we have Heb. ^^, and Phon. "1*13 to
Wm ; Aram. TD3 to 6fe*s or praise ; Syr, ^a to bless or praise ;
and in Palm, such phrases as NQ^SJ*? 1Q2? "p" 13 (de Vogue,
No. 94) " blessed be his name for evermore ", and *"|n3l^ (ibid., No.
144) "may he bless". From this N. Semitic sense we find derived
the Sab. rf)R (Kossini, Glossarium, 118), Eth. fl^h to bless, celebrate
the praises of, and Ar. ciljl as above. Note also the formations Heb.
Aram. JQHH ' Syr. }ADiQ), which also were taken
over into S. Semitic, e.g. Eth. fl^h'1* ; Ar.
I^Jj (Bard* a).
Ivii, 22.
To create.
1 Ed. Le Coq, SB AW, Berlin, 1908, pp. 400, 401 ; cf. also Salemann, Manichaeische
Studien, i, 58.
### FVQ leaf 278 (p.261)
FOREIGN VOCABULARY OP THE QUR ? AN 261
The truth is that it is from a root related to JlS, but is not
an Arabic formation at all, being like the Heb. n3^*"JQ, a borrowing
from the Aram. Nn3*HQ, Syr. jAi^Lo. 1 Aram. NnS'HQ means
a province and then a city, 2 and Syr. (Ala ,10 is city? From Aram.
it was borrowed into Middle Persian where we find the ideogram
madma, meaning a large fortified city (PPGl, 150).
(Marjdn).
Iv, 22, 58.
Small pearls.
The word occurs only in a description of Paradise, and was early
recognized as borrowed from Persia, 4 but it is certain that it did not
come directly from Iranian into Arabic. 5
We find in Phlv. ^)jjp^ murvdnt,* a pearl used, e.g. in the
Gosht-i-Frydno, ii, 13, in describing the crowns presented to the
daughters of Spitama after death. From Middle Persian the word was
borrowed widely, e.g. Gk. jJiapyapirris 7 ; Aram. WP33"1Q ;
Syr. ]AjLl..;iO, and from some Aram, form 8 it came into Arabic.
It would have come at an early date for it is used in the old poetry
and was doubtless well known in the pre-Islamic period.
(Mursd).
xi, 43.
Harbour, haven.
1 Fraenkel, Fremdw, 280; Horovitz, KU. 137.
2 It has this meaning in Arabic as early as the Nemiira inscription ; cf. RES, i,
No. 483.
3 There is some discusaitm of the meaning of the word by Torrey in JAOS, xliii,
230 ff.
4 al-Jawallqi, Mu'arrab, 144 ; as-Suyuti, Itq, 324 ; MuJiit, sub voc., and sceSachau's
note to the Mu'arrah, p. 65.
3 In spite of Addai Sher, 144, and his attempted derivation from 0^.
6 West, Glossary, 213 ; 8aya*t, Glossary, 163 ; cf. Horn, Qrundriss, 218, n.
7 Also fiapyapis 1805, from which comes the Arm. t/uy^ 111^1111 and the European
forms.
8 Fraenkel, Fremdw, 59. The Mand. XDN^KaiXQ would also seem to be
from the same source, vide Noldeke, Mundart, 53 ; Mingana, Syriac Influence, 90 ;
Vollers, ZDMQ, 1, 611 ; li, 303.
### FVQ grep marjan/lulu/baraka
2684:stood the verb Jift^ik, 3 used of the blessed departed, as a place-
3010:dtyJ (Baraka).
3012:To bless.
3028:Wm ; Aram. TD3 to 6fe*s or praise ; Syr, ^a to bless or praise ;
3030:No. 94) " blessed be his name for evermore ", and *"|n3l^ (ibid., No.
3031:144) "may he bless". From this N. Semitic sense we find derived
3032:the Sab. rf)R (Kossini, Glossarium, 118), Eth. fl^h to bless, celebrate
3958:Blessed (Ixix, 22 ; Ixxxviii, 10, etc.).
4899:virgins, the blessed are promised IsLjo L*.lj .
7714:blessed state into which Christ brings men during their earthly sojourn-
8097:was very commonly used for the abode of the Blessed, and could
8385:to bless, sanctify, ii, 28 ; ^^-A and <U*\ju,4 holy, sacred, v, 24 ;
8875:of the fountain from which the Blessed drink, or the material used to
9401:(Marjdn).
9465:Both passages refer to the tempering of the drink of the blessed
```


## [2026-09-04T15:07:49.937Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### POK_full dheigh\"; grep -n -A3 'lemma: dhei' POK_full.txt | head -40; echo \"### POK_full leudh\"; grep -n -A3 'lemma: leudh' POK_full.txt | head -40; echo \"### POK_full mad\"; grep -n -A3 'lemma: mad' POK_full.txt | head -40",
 "description": "Find Pokorny roots dheigh, leudh, mad in POK_full"
}
```


### [2026-09-04T15:07:50.010Z] TOOL RESULT

```
### POK_full dheigh
### POK_full leudh
### POK_full mad
57042:Root/ lemma: mad-: wet; glossy, fat, well-fed, intoxicating : Root/ lemma: meA^w. honey, 
57043-
57044-intoxicating. 
57045-
```


## [2026-09-04T15:07:52.188Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in '^dheigh' '^leudh' '^mad-' '^per' 'margar' 'pairi' 'paradise' 'daeza' 'dough' 'liberal' 'Latvia'; do echo \"## $w\"; grep -n -i \"$w\" AHD_watkins1985.txt | head -8; done",
 "description": "Grep AHD 1985 Watkins for roots"
}
```


### [2026-09-04T15:07:54.377Z] TOOL RESULT

```
## ^dheigh
## ^leudh
## ^mad-
708:mad-. Moist, wet; also refers to various qualities of food. 1. Sanskrit madati, “it gladdens, it bubbles,” hence madana-, delightful, joyful, hence madanah, a myna bird: MYNA. 2. Suffixed form *mad-i- in Germanic *mati- in: a. Old English mete, food: MEAT; b. Middle Low German (ge)mate (ge-, together, from Germanic *ga-; see kom), “he with whom one shares one’s food,” compan- ion: MATE}, 3. Suffixed form *mad-sto-, becoming *mazdo-, in Germanic *masta- in Old English mest, fodder: MasT?. [Pok. mad- 694.]
## ^per
611:perhaps akin to the source of Middle English nokke, nock: NOCK; b. Norwegian (dialectal) nok, projection, hook, akin to the Scandinavian source of Middle English nok, corner, nook: NooK. [Pok. 1. ken- 558.]
836:per’
838:per-?
840:per-3. The young of an animal (< “a bringing forth,” “offspring”), Derivative root belonging to the group of per'. Suffixed o-grade form *por-si- in Germanic *farzi-, young cow, in Old English fearr, calf, and compound heahfore, calf (first element obscure): HEIFER. [In Pok. 2. D. per 818.]
841:per-‘. To try, risk (< “to lead over,” “press forward”). A verbal root belonging to the group of per’. 1. Lengthened grade *pér- in Germanic *féraz, danger, in Old English
2079:PER- pert PERCEIVE kap- PERCENT dekm PERCH? perk-1 PERCOLATE kagh- PERCURRENT kers-2 PERCUSS kwét- PERDITION d6- PERDURABLE deue- PEREGRINE agro- PEREMPTORY em- PERENNIAL at- PERFECT dhé-1 PERFIDY bheidh- PERFORATE bher-2 PERFUME dheu-1 PERFUNCTORY bheug-2 PERFUSE gheu- PERGOLA perg- PERI- per! PERICARDIUM kerd-1 PERICLINE Klei- PERIGEE gé PERIHELION sawel- PERIL per-4 PERIMYSIUM mis- PERINEPHRIUM negWh-ro- PERIOD sed-2 PERIONYCHIUM nogh- PERIOSTEM ost- PERIPATETIC pent- PERIPETEIA pet- PERIPHERY bher-1 PERIPHRASIS gWhren- PERIPHYTON bheue- PERIPTERAL pet- PERISARC  twerk- PERISH ei-1 PERISSODACTYL per! PERISTALSIS | stel- PERISTYLE sta- PERITHECIUM dhé-1 PERITONEUM ten- PERITRICH _ thrix PERIWINKLE! weng- PERJURE yewes- PERMANENT men-3 PERMEATE mei-1 PERMIT (s)meit(a)- PERMUTE mei-1 PERNICIOUS nek-1 PERONEAL per-2 PERORAL 6s- PERORATE 6r- PERPEND (S)pen- PERPENDICULAR (S)pen- PERPETRATE peter- PERPETUAL pet- PERPLEX plek-
2081:PERQUISITE quaerere PERSE s(w)e- PERSECUTE sekw-1 PERSEVERE wéro- PERSIFLAGE swei-! PERSIST sta- PERSPECTIVE spek- PERSPIRE spirare PERSUADE swad- PERT wer-5 PERTAIN ten- PERTINACIOUS ten- PERTURB twer-1 PERVADE wadh-2 PERVERT wer-3 PERVIOUS wegh- PES ped-!
## margar
725:[margarités. Pearl. Greek noun of Oriental origin (prob- ably immediately from Iranian). Greek margarités, mar- garon, pearl: MARGARIC, MARGARIC ACID, (MARGARINE), MARGARITE!, MARGARITE?.]
1818:MARE? mori- MARGARIC margarités MARGARIC ACID margarités MARGARINE margarités MARGARITE! margarités MARGARITE2 margarités MARGIN merg- MARGRAVE gravo-, merg- MARICOLOUS mori- MARICULTURE mori- MARINARA mori- MARINE mori- MARITAL mari- MARITIME mori- MARK! merg-
## pairi
837:“around.” I. Basic form *per and extended form *peri. 1. Germanic *fer-, *far-, used chiefly as an intensive prefix denoting destruction, reversal, or completion, in: a. Old High German far-, in German vereinen, to unite: TURNVEREIN; b. Middle Dutch vieren, to let out, slacken: VEER; C. compound “*fer-getan, “‘to lose one’s hold,” forget (see ghend-). 2. Suffixed (comparative) form *per-ero-, farther away, in Germanic *fer(e)ra’in Old English feor(r), far: FAR. 3. Compound “per-n-yo-, of last year (*-n-, year; see en-), in Germanic *fernja- in Old High German firni, old: FmRN. 4. Latin per, through, for, by: PER, PER-; PARAMOUNT, PARAMOUR, PARGET, PAR- VENU. 5. Greek peri, around, near, beyond: PERI-; PERIS- SODACTYL. 6. Sanskrit pari, through, around: PALANQUIN. 7. Avestan pairi, around: PARADISE. II. Zero-grade form *pr-. 1.Germanic *fur, before, in: a. Old English for, before, instead of, on account of: FOR; b. Old English for-, prefix denoting destruction, pejora- tion, exclusion, or completion: For-. 2. Extended form *prt- in Germanic *furth-, forward, in Old English forth, forth: FORTH; AFFORD. 3. Suffixed (comparative) form *pr-tero- in Germanic *furthera- in Old English furthra, furthor, farther away: FURTHER. 4. Compound *pr-st-i- (or *por-st-i-, with o-grade form *por-), “that which stands before,” stake, post (see sta-). III. Extended zero-grade form “pro-. 1. Suffixed (superlative) form *pro-mo- in: a. Germanic *fruma-, *furma- in Old Eng- lish forma, first, foremost: FOREMOST, FORMER?; b. Latin compound prandium, “first meal,” late breakfast, lunch (probably < *pram-d-ium < *pram-(e)d-yo-; second ele- ment *-(e)d-, to eat; see ed-). 2. Suffixed (superlative) form *pro-isto- in Germanic *furista-, foremost, in Old English fyrst, fyrest, first: FIRST. 3. Suffixed form *pre-wo- in Greek *prowo-, first, foremost, in: a. analogi- cally suffixed Greek form *préw-arya in Greek prdira, forward part of a ship: PROw; b. suffixed (superlative) Greek form *préw-ato- in Greek prétos, first, foremost: PROTEIN, PROTIST, PROTO-, PROTON. 4. Suffixed form *pro-i in Celtic *(p)ari, *are in Gaulish ari (combining form are-), before, in Latin arepennis, half-acre (second element obscure): ARPENT. IV. Extended form “prod. 1. Germanic *fura, before, in: a. Old English fore, for (> Middle English fore-), before: FORE, FORE-; FOREFA- THER; b. Old High German fora (> German vor), before: VORLAGE; Cc. Germanic prefixed and suffixed form *bi-fora-na, in the front (*bi-, at, by; see ambhi), in Old English beforan, before: BEFORE. 2. Greek para, beside, alongside of, beyond: PARA-); PALFREY. V. Extended form *pré. 1. a. Germanic *fra, forward, away from, in Old Norse *frd (> Middle English fro), from: FRO; FROWARD; b. Germanic *fra-, completely (see ed-, éik-). 2. Suffixed form *pro-mo- in: a. Germanic *fram, from, in Old English from, from: FROM; b. Germanic *frum, forward, hence derivative verb *frumjan, to further, in Old French f(ojurnir, to supply, provide: FURNISH, VE- NEER; C. Czech pram, raft: PRAAM. 3. Suffixed form *pr6é-wo- in Germanic *frdw6-, lady, in: a. Old High German frouwa, lady: FRAU, (FRAULEIN); b. Middle Dutch vrouwe, woman: vRouw. 4. Latin pré, pro-, be- fore, for, instead of: PRO!, PRO-!; PURCHASE. 5. Suffixed form *pr6-no- in Latin prénus, leaning forward: PRONE. 6. Possible suffixed form *pro-ko- in Latin compound reciprocus, alternating, ‘‘backward and forward” (*re-ko-, backward; see re-): RECIPROCAL. 7. Suffixed adverb *pro-kve in: a. Latin prope, near: APPROACH, RAPPROCHEMENT, REPROACH; b. suffixed form *prok- ink“o- in Latin propinquus, near: PROPINQUITY; Cc. suf- fixed (superlative) form *prok’-samo- in Latin proximus, nearest: PROXIMATE; APPROXIMATE. 8. Compound *pro-bhw-o-, growing well or straightforward (*bhw-o-, to grow; see bheue-), in Latin probus, upright, good, virtuous: (PROBABLE), PROBE, PROBITY, (PROOF), PROVE; APPROVE, IMPROBITY, (IMPROVE), (REPROVE). 9. Greek pro, before, in front, forward: PRO-2. 10. Suffixed (com-
## paradise
168:Roots indicating a number of technical operations are attested in most of the lan- guages of the family. One such is teks-, which in some dialects means “to fabricate, espe- cially by working with an ax,” but in others means “to weave” (TEXTILE). A root dheigh-, meaning “to mold, shape,” is applied both to bread (DOUGH) and to mud or clay, whence words for both pottery and mud walls (Ira- nian *pari-daiza, “walled around,” borrowed into Greek as the word that became English PARADISE).
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
837:“around.” I. Basic form *per and extended form *peri. 1. Germanic *fer-, *far-, used chiefly as an intensive prefix denoting destruction, reversal, or completion, in: a. Old High German far-, in German vereinen, to unite: TURNVEREIN; b. Middle Dutch vieren, to let out, slacken: VEER; C. compound “*fer-getan, “‘to lose one’s hold,” forget (see ghend-). 2. Suffixed (comparative) form *per-ero-, farther away, in Germanic *fer(e)ra’in Old English feor(r), far: FAR. 3. Compound “per-n-yo-, of last year (*-n-, year; see en-), in Germanic *fernja- in Old High German firni, old: FmRN. 4. Latin per, through, for, by: PER, PER-; PARAMOUNT, PARAMOUR, PARGET, PAR- VENU. 5. Greek peri, around, near, beyond: PERI-; PERIS- SODACTYL. 6. Sanskrit pari, through, around: PALANQUIN. 7. Avestan pairi, around: PARADISE. II. Zero-grade form *pr-. 1.Germanic *fur, before, in: a. Old English for, before, instead of, on account of: FOR; b. Old English for-, prefix denoting destruction, pejora- tion, exclusion, or completion: For-. 2. Extended form *prt- in Germanic *furth-, forward, in Old English forth, forth: FORTH; AFFORD. 3. Suffixed (comparative) form *pr-tero- in Germanic *furthera- in Old English furthra, furthor, farther away: FURTHER. 4. Compound *pr-st-i- (or *por-st-i-, with o-grade form *por-), “that which stands before,” stake, post (see sta-). III. Extended zero-grade form “pro-. 1. Suffixed (superlative) form *pro-mo- in: a. Germanic *fruma-, *furma- in Old Eng- lish forma, first, foremost: FOREMOST, FORMER?; b. Latin compound prandium, “first meal,” late breakfast, lunch (probably < *pram-d-ium < *pram-(e)d-yo-; second ele- ment *-(e)d-, to eat; see ed-). 2. Suffixed (superlative) form *pro-isto- in Germanic *furista-, foremost, in Old English fyrst, fyrest, first: FIRST. 3. Suffixed form *pre-wo- in Greek *prowo-, first, foremost, in: a. analogi- cally suffixed Greek form *préw-arya in Greek prdira, forward part of a ship: PROw; b. suffixed (superlative) Greek form *préw-ato- in Greek prétos, first, foremost: PROTEIN, PROTIST, PROTO-, PROTON. 4. Suffixed form *pro-i in Celtic *(p)ari, *are in Gaulish ari (combining form are-), before, in Latin arepennis, half-acre (second element obscure): ARPENT. IV. Extended form “prod. 1. Germanic *fura, before, in: a. Old English fore, for (> Middle English fore-), before: FORE, FORE-; FOREFA- THER; b. Old High German fora (> German vor), before: VORLAGE; Cc. Germanic prefixed and suffixed form *bi-fora-na, in the front (*bi-, at, by; see ambhi), in Old English beforan, before: BEFORE. 2. Greek para, beside, alongside of, beyond: PARA-); PALFREY. V. Extended form *pré. 1. a. Germanic *fra, forward, away from, in Old Norse *frd (> Middle English fro), from: FRO; FROWARD; b. Germanic *fra-, completely (see ed-, éik-). 2. Suffixed form *pro-mo- in: a. Germanic *fram, from, in Old English from, from: FROM; b. Germanic *frum, forward, hence derivative verb *frumjan, to further, in Old French f(ojurnir, to supply, provide: FURNISH, VE- NEER; C. Czech pram, raft: PRAAM. 3. Suffixed form *pr6é-wo- in Germanic *frdw6-, lady, in: a. Old High German frouwa, lady: FRAU, (FRAULEIN); b. Middle Dutch vrouwe, woman: vRouw. 4. Latin pré, pro-, be- fore, for, instead of: PRO!, PRO-!; PURCHASE. 5. Suffixed form *pr6-no- in Latin prénus, leaning forward: PRONE. 6. Possible suffixed form *pro-ko- in Latin compound reciprocus, alternating, ‘‘backward and forward” (*re-ko-, backward; see re-): RECIPROCAL. 7. Suffixed adverb *pro-kve in: a. Latin prope, near: APPROACH, RAPPROCHEMENT, REPROACH; b. suffixed form *prok- ink“o- in Latin propinquus, near: PROPINQUITY; Cc. suf- fixed (superlative) form *prok’-samo- in Latin proximus, nearest: PROXIMATE; APPROXIMATE. 8. Compound *pro-bhw-o-, growing well or straightforward (*bhw-o-, to grow; see bheue-), in Latin probus, upright, good, virtuous: (PROBABLE), PROBE, PROBITY, (PROOF), PROVE; APPROVE, IMPROBITY, (IMPROVE), (REPROVE). 9. Greek pro, before, in front, forward: PRO-2. 10. Suffixed (com-
2059:-PARA pere-1 PARABLE gWelg-1 PARABOLA gW¥ele-1 PARACHUTE pere-1 PARACLETE kele-2 PARADE pere-1 PARADIGM deik- PARADISE dheigh-, pert PARADOX dek-! PARAFFIN pau- PARAGRAPH gerbh- PARALLAX al-1 PARALLEL al-1 PARALLELEPIPED ped-! PARALOGISM leg-1 PARALYSIS leu PARAMECIUM mak- PARAMOUNT ad-, per! PARAMOUR amma, pert PARANOIA nous PARAPET peg- PARAPHERNALIA bher-1 PARAPHRASE gWhren- PARAPLEGIA plak-2 PARASOL pere-1, sawel- PARATAXIS tag- PARBOIL beu-! PARCAE pera-1 PARCEL pere-2 PARCENER pere-2 PARDON d6-
## daeza
## dough
168:Roots indicating a number of technical operations are attested in most of the lan- guages of the family. One such is teks-, which in some dialects means “to fabricate, espe- cially by working with an ax,” but in others means “to weave” (TEXTILE). A root dheigh-, meaning “to mold, shape,” is applied both to bread (DOUGH) and to mud or clay, whence words for both pottery and mud walls (Ira- nian *pari-daiza, “walled around,” borrowed into Greek as the word that became English PARADISE).
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
382:blind: TYPHUS; TYPHLOSOLE. 11. Extended form *dheubh., “beclouded in the senses,” in suffixed o-grade form *dhoubh-o- in: a. Germanic *daubaz in Old English déaf, deaf: DEAF; b. nasalized form *dhu-m-bho- in Germanic *dumbaz in Old English dumb, dumb: pumps; c. Germanic *diibén- in Old English *dife, dove (< “dark-colored bird”): DOVE!. 12. Extended zero-grade form *dhwel- in: a. Germanic *dwelan, to go or lead astray, in Old English dwellan, to deceive (but influenced in sense by cognate Old Norse dvelja, to tarry): DWELL; b. Germanic *dulaz in (i) Old English dol, dull: DoL- DRUMS (ii) Middle Low German dul, dull: (DOLT), DULL. 13. Extended zero-grade form *dhwes- in Greek suffixed form *th(wjes-es-, smoke, whence Greek *th(w)es-es-yon, becoming theion, brimstone, sulfur: THIO-, THION-. 14. Perhaps Old English docce, dock (< “dark-colored plant”): Dock‘. 15. Perhaps Irish did, pipe: DUDEEN. [Pok. 4. dheu- 261.] dheu-2. To flow. Germanic *dauwaz, dew, in: a. Old English déaw, dew: DEW; b. compound *melith-dauwaz, “honeydew” (see melit-). [Pok. 1. dheu- 259.] dheu-’. To become exhausted, die. 1. Suffixed o-grade form *dhou-to- in Germanic *daudaz in Old English déad, dead: DEAD. 2. Suffixed o-grade form *dhou-tu- in Germanic *dauthuz in Old English déath, death: DEATH. 3. Suffixed o-grade form *dhow-yo- in Old Norse deyja, to die: DIE}. 4. Suffixed extended zero-grade form *dhwi-no- in Germanic *dwinan in Old English dwinan, to diminish, languish: DWINDLE. [Pok. 2. dheu- 260.] dheub-. Deep, hollow. 1. Germanic *deupaz in Old Eng- lish déop, deep: DEEP, DEPTH. 2. Germanic expressive denominative *duppjan in Old English dyppan, to im- merse, dip: pip. 3. Parallel root form *dheubh- in Ger- manic *deub-, *dub- in verb *diibjan in Old English dyfan, to dip, and difan, to sink, dive: pivE. [Pok. dheu-b- 267.] dheubh-. Wedge, peg, plug. Germanic *dub- in: a. Old English dubbian, to tap, strike (with a sword): DUB); b. Low German dubben, to hit: puB?; c. Germanic di- minutive *dub-ila- in Middle Low German dével, peg: DOWEL. [Pok. dheubh- 268.] dheugh-. To produce something of utility. 1. Germanic extended form *duht- in Old English dyhtig, dohtig, strong (< “useful”): DOUGHTY. 2. Suffixed form *dheugh- os- in Greek teukhos (< *theukhos), gear, anything produced, tool: HEPTATEUCH, HEXATEUCH, PENTA- TEUCH. [Pok. dheugh- 271.] dhghem-. Earth. 1. Suffixed zero-grade form *(dh)ghm-on-, “earthling,” in Germanic *gumén- in Old English guma, man: BRIDEGROOM. 2. O-grade form *dhghom- in Greek khthon, earth: CHTHONIC; AUTOCH- THON. 3. Zero-grade form *dhghm- in Greek khamai, on the ground: CHAMAEPHYTE, CHAMELEON, CHAMOMILE, GERMANDER. 4. Suffixed o-grade form *(dh)ghom-o- in Latin humus, earth: HUMBLE, (HUMILIATE), (HUMILITY), HUMUS; EXHUME, INHUME, TRANSHUMANCE. 5. Suffixed o-grade form *(dh)ghom-on-, “earthling,” in: a. Latin homé, human being, man: HOMAGE, HOMBRE!, HOMINID, HOMO!, HOMUNCULUS, OMBRE; BONHOMIE, HOMICIDE; b. (in part) Latin himdnus, human, kind, humane: HUMAN, (HUMANE). 6. Suffixed form *(dh)ghem-ya in Russian zemlya, land, earth: SIEROZEM, ZEMSTVO. 7. Full-grade form *(dh)ghem- in Persian zamin, earth, land: ZAMINDAR. [Pok. ghdhem- 414.] dhghut-. Fish. Greek ikhthus, fish: 1cHTHYO-. [Pok. ghdha- 416,] dhgh(y)es-. Yesterday. Suffixed (comparative) form (dh)ghes-ter- in Germanic “ges-ter- in Old English geo- stran, giestran, “yester-”: YESTER-, (YESTERDAY). [Pok. ghdhies 416.] dhgvhei-. To perish, die away. Zero-grade form *dhgvhi- in Greek phthinein, to die away: PHTHISIS. [Pok. gthdhei(a)- 487.)
1434:DOTE dud- DOUBLE dwo- DOUBLET dwo- DOUBLOON dwo- DOUBLURE dwo- DOUBT dwo- DOUCEUR dik-u- DOUCHE deuk- poucH dheigh- DOUGHTY dheugh- DOUR deru. DOVE! dheu-1 DOWAGER dé- DOWEL dheubh- DOWER do- Down! dhino- pDowN2 dheu-! pown’ dhiino- Dowry do- DOXOLOGY dek-1 DOYEN deki DOZE dheu- DOZEN dekm, dwo- DRAB! der-2 DRAB? dher-! DRABBLE dher-! DRACHMA dergh- DRAFT dhragh- DRAG dhragh- DRAGON derk- DRAGOON derk- DRAIN dreug- DRAKE? derk- DRAMA dera- DRAMATURGE werg- DRAPE der-2 DRASTIC dere- DRAW dhragh- DRAY dhragh- DREAM dhreugh- DREARY dhreu- DRECK sker-4 DREGS dher-1 DRENCH dhreg- DRIFT dhreibh- DRILL! tere-1 DRINK dhreg- DRIP dhreu- DRIVE dhreibh- DRIVEL dher-! DRIZZLE dhreu- -DROME der-1 DROMEDARY der-1 DROMOND der-1 -DROMOUS der-1
## liberal
693:in: a. Old English -Jéosan, to lose: LORN, (LOSEL); b. Ger- manic *fer-leusan, *far-leusan (*fer-, *far-, prefix denot- ing rejection or exclusion; see per’) in (i) Old English forléosan, to forfeit, lose: FORLORN (ii) Dutch verliezen, to lose (past participle verloren): FORLORN HOPE. 2. Ger- manic */aww6 in Swedish lagg, barrel stave (< “split piece of wood”), akin to the probable source of LAG?. 3. Germanic *lausaz in: a. Old English léas, “loose,” free from, without, untrue, lacking: LEASING, -LESS; b. Old English los, loss: LOSE, (LOSS); CG. Old Norse Jauss, louss, loose: LOOSE; d. Swiss German lésch, loose: LOESS. 4. Zero-grade form *lu- in: a. Greek luein, to loosen, release, untie: LYSIS, LYSO-, -LYTE, -LYTIC; ANALYSIS, CATALYSIS, DIALYSIS, LYASE, PARALYSIS, TACHYLYTE; b. Latin lués, plague, pestilence (< “dissolution, putre- faction”): LUES; Cc. prefixed form *se-lu- (se-, apart; see s(w)e-) in Latin solvere, to loosen, untie: SOLUBLE, SOLUTE, SOLVE; ABSOLUTE, (ABSOLVE), ASSOIL, CONSO- LUTE, DISSOLVE, RESOLVE. [Pok. 2. Jeu- 681.] leu-2. Dirt; to make dirty. 1. Latin polluere, to pollute (< *por-luere; por- for pr6-, forth, forward; see per’): POLLUTE. 2. Suffixed zero-grade form */u-to- in Latin lutum, mud, mire, clay: LUTE?. [Pok. 1. leu- 681.] léu-1, Stone. Welsh Jlech, flat stone (from an uncertain preform): CROMLECH. [Pok. 2. léu- 683.] léu-2. Echoic root. 1. Extended form */eut- in Germanic *leuth- in Old High German liod (> German Lied), song: LIED; VOLKSLIED. 2. Extended variant form *laud- in Latin laus, praise, glory, fame: LAUD. [Pok. 3. éu- 683.] leubh-. To care, desire; love. I. Suffixed form *leubh-o- in Germanic *leubaz in Old English /éof, dear, beloved: LIEF; LEMAN, LIVELONG. II. O-grade form *loubh-. 1. Germanic */aubé in: a. Old English léaf, permission (< “pleasure, approval”): LEAVE?; b. Middle Dutch verlof, leave, permission (ver-, intensive prefix, from Germanic *fer-; see per'): FURLOUGH; Cc. Germanic *galaubd (*ga-, intensive prefix; see kom) in Old English geléafa, biléafa (bi-, about; see ambhi), belief, faith: BELIEF. 2. Ger- manic *galaubjan (*ga-, intensive prefix; see kom), “to hold dear,” esteem, trust, in Old English geléfan, beléfan (be-, about; see ambhi), to believe, trust: BELIEVE. III. Zero-grade form *lubh-. 1. Suffixed form *lubh-a- in Germanic */ubé in Old English Jufu, love: LovE. 2. Suf- fixed (stative) form *lubh-é- in Latin libére, to be dear, be pleasing: QUODLIBET. 3. Latin libid6, pleasure, desire: LIBIDO. [Pok. leubh- 683.] leud-. Small. Germanic */it- in: a. West Germanic *lutti- laz in Old English /ytel, little: LITTLE; b. Old English liitan, to bend down: LouT?; c. Old Norse lita, to bend down (< “to make small”): (LouT!); d. perhaps Middle Dutch loteren, to shake, totter (< “to make smaller”), perhaps akin to the source of Middle English Joitren, to idle away time: LOITER. [Pok. leud- 684.] leudh-'. To go. Zero-grade form *(e)ludh- in suffixed unextended form *elu-to- in Greek prosélutos, “one who comes to a place,” stranger (pros-, to; see per’): PROS- ELYTE. [In Pok. 6. e/- 306.] leudh-2. To mount up, grow. Suffixed form */eudh-ero- in Latin liber, free (the precise semantic development is obscure): LIBERAL, LIBERATE, LIBERTINE, LIBERTY, LIV- ERY; DELIVER. [Pok. 1. leudh- 684.] leu(e)-. To wash. 1. Suffixed form *lou-kd- in Germanic *laugo in Old English /éag, lye: LYE. 2. Suffixed form *lou-tro- in Old English /éathor, washing soda: LATHER. 3. Variant form *Jaw- in: a. Latin lavere, to wash, with its derivative -luere, to wash: LOTION; ABLUTION, ALLU- VION, COLLUVIUM, DELUGE, DILUTE, (ELUANT), ELUTE, ELUVIUM; b. form */aw-d- in Latin lavdre, to wash: LAVE, LOMENT; C. Latin lavatrina, ldtrina, a bath, privy: LATRINE. [Pok. Jou- 692.] leug-'. To bend, turn, wind. 1. Germanic *Jauk-, leek (semantic transition obscure), in Old English Jéac, leek: LEEK; GARLIC. 2. Zero-grade form *lug- in Germanic *luk- in: a. Old English loc, lock (perhaps < “a bending
1741:LETHAL ol- LETHARGY |adh- LETHE ladh- LETTER deph- LETTUCE melg- LEVEL [ithra LEVER leg’h- LEVIGATE ag-, leg’h- LEVIRATE daiwer- LEVITY leg¥h- LEVo- laiwo- LEVOROTATION laiwo- LEVOROTATORY laiwo- LEX leg-1 LEXICON leg-1 LIABLE leig-1 LIBATION Iéi- LIBERAL leudh-2 LIBERATE leudh-2 LIBERTINE leudh-2 LIBERTY leudh-2 LIBIDO leubh- LIBRA fithra
## Latvia
```


## [2026-09-04T15:07:54.436Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HRN p.133 leaf 154\"; awk 'BEGIN{RS=\"\\f\"} NR==155' HRN.txt; echo \"### HRN grep dez/diz\"; grep -n -i 'didā\\|dida\\|diz\\b\\|dēz\\|dez ' HRN.txt | head -20",
 "description": "Read Horn p.133 and grep for diz/didā"
}
```


### [2026-09-04T15:07:56.554Z] TOOL RESULT

```
### HRN p.133 leaf 154
— 138 —
596. dltn i^dem) ') *Geöiclit, Waiigun , dliue,
aw. daeman- ; plilv. andemän\kar 'empfangend,
führend', päz. andlmdnl 'entgegen, vor; arm. LW.
dem, det, y-andman (Hübschmann, No. 88).
kurd. LW. djm\ bei. LW. dem (80); afy. leina
'Pupille.
597. dtn 'Glaube, Religion*.
aw. dafwö-; phlv. diu bezw. den, paz. diu, dlmk,
arm. LW. den.
Allgemein entlehnt*'^).
598. dev 'Dämon, Teufel', dcväne Verrückt*, n^NDH (Jer.
29, 26.) 3).
aw. daeva- 'Dämon'; phlv. dev; ai. devd- 'Gott'.
599. dlvär 'Mauer, Wand'.
ap. ^deghavära- (vergl. gr. th/o^-, osk. felhuss).
Nöldeke (mündliche Mitteilung), unter der Voraus-
setzung, dass die np. Grundform '^devür lautete, was
die Zusammenstellung mit dev (8ähn. I, 24 Vers 86)
wahrscheinlich macht.
kurd. LW. dwär; wa;^. LW. dival^ sar. delvül 'Mauer,
Wand, Umwallung.
*) Der Majhül vokal ist nicht mehr in der Aussprache erhalten.
') College Jensen hat din sogar im Verdachte, babylonisch zu
sein. Er äussert sich in folgender WeiBe über diese Ansicht:
y»Üe(i)nim in der elamitisohen Version = framänä, de(i)Him-
dattira ibid. = framätaram, beides in der Inschr. von Naqs-i-Rustani.
iJeCOnhn unmöglich = daina, muss vielmehr = babyl. dinim sein,
welches in der babyl. Version der Achämonideninschriften vorkommt.
iHiiii = 'Gesetz, Recht* könnte sehr wohl persisches daina übersetzen,
das im Altpersischen nicht vorhanden. Ich halte es daher für möglich
(falls nichts Entscheidendes dagegen einzuwenden), dass daina durcli
elamitischcs den- mit assyr.-babyl. dlmi zu verknüpfen ist."
Vergl. Geldner's Etymologie von aw. dapiä- unter No. 413.
Jensen nimmt als Grundbedeutung *Recht, Gesetz' an, Geldner da-
gegen *Glaube, Religion*, wie im Neup.
^) Ursprünglich natürlich 'teuflisch , dämonisch*, vergl. Sahn. 1,
)5? Vers 408, 413.
### HRN grep dez/diz
2786:phlv. pätej^ päz. pädez 'Herbst'.
5058:563. dix, diz, dez-) 'Burg, vergl. dizhäii-^), dlzdär (syr. LW.
5063:Die neupersischon Formen diz und dcz sind beide
5064:gleich ursprünglich. Ap. dida- steht für dlöä- und
5067:Erklärung von np. dwar 'Mauer aus ap. '^didavara-
5072:2) Dez findet sich in einer ganzen Reilie trän soxanisch er
5083:LW. (?) kurd. diz *Dieb', dizhi 'stehlen'; bei. duz,
5091:505. duS', duS' {diz-, dez-) *übel, böse'; vergl. dust (Bahn.
5102:bei. n. diday, pp. da/fa 'brandmarken' (433).
12126:1 .livlltte 698,dez 568 u. Anm-, 594.
12220:diz 568.
17416:pädez 288.
```


## [2026-09-04T15:07:56.686Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HUB p.65 leaf 75\"; awk 'BEGIN{RS=\"\\f\"} NR==76' HUB.txt; echo \"### HUB grep dīg/deg\"; grep -n -i 'dēg\\|deg\\b\\|dīg\\|daika\\|dig\\b' HUB.txt | head -20",
 "description": "Read Hübschmann p.65 and grep dīg"
}
```


### [2026-09-04T15:07:58.208Z] TOOL RESULT

```
### HUB p.65 leaf 75
— 65 -
aus der dih wurde, wie -kert, -gerd (in Namen) zu gird
u. s. w. geworden ist, oder geht np. dih = dlh, dsh,
das haufig vorkommt, auf mp. dsh zuriick?
589. Bei Rosen, Np. Sprachfiihrer p. 26, 39: ddhdnd*Qe-
bissstiick des Ziigels ; afgh. LW. dahana fem. *the bit
of a bridle', kal dehand, dahnd etc.
593. Ich stelle -des, -dis *ahnlich' zu gr. Jaxv/t/'zeige', dsixrjXov
*Ebenbild', skr. dig 'zeigen', subst. dig *Hinweis, Art and
Weise', zd. dis Veisen', osset. dwd%8}n zeigen u. &. w.
Also doeh -dEs = zd. ^da^a-, auch wenn dies nicht
rait daesa- yt. 13, 104 (*Traumbild'?) identisch ist.
594. Wenn dBz, deza *Kochtopf zu got. deigan *kneten, aus
Thon formen* (Wzl. dhig%) gehOrt, ist es verwandt mit
Nr. 563 diz, dSz *Burg', s. oben. Ob auch deg *Koch-
topf dazu gehort, ist fraglich, da 1) idg. dhig^h durch
skr. dBgdhiy digdha- nicht gesichert ist (vgL Brug-
mann, Grundriss I, p. 344) und 2) idg. dhoi^ho- im
Neup. zu *d^y werden miisste. Np. d^ (afgh. LW.
dEg *Kesser) setzt ap. ^daika- voraus. Phi. dSg 'Kesser
(Gl. and Ind. 288) kann eine junge Form sein. Zu d.
Tiegel u. s. w. vgl. Kluge, Wb. 5. Aufl. s. v.
595. Piige hinzu : paz. dddlgar ^secondly, other' Shk. 240,
Min. Gl. 53, did 'second' Shk. 241, Min. Gl. 61, dadum
'second' Shk. 240. Dieses paz. did ist direct = ap.
duvitiya- *der zweite . Vgl. WZKM. 5, 262.
596. Die kurdische Form lautet dem *Gesicht' bei Socin,
kurd. Sammlungen II, p. 307 ; afgh. lies ISmq.
599. Besser *daidavara- (Fe&tungBmsiuer*)^) Sils *daigavara-
anzusetzen, vgl. oben Nr. 594 und 563. Anders Fr.
Mil Her, WZKM. 8, 95 {^daya-vara- *Scheidemauer).
Falls dtvar (mit i) die urspriingliche Form ist (vgl.
afgh. LW. dlval *a wall'), ware dUvdr iiber *diyvar =
*did-vclr auf ap. *dida-vara- zuriickzufiihren. Alles
unsicher. Nebenform dwal JRAS. 1893, 463.
600. NSldeke macht mich darauf aufmerksam, dass im
ersten Verse von Vis u Ramin ra Dativpartikel (und
niar an Nominativ) ist.
>) Vgl. bara I diz *Mauer der Festung' Fird. I, 452, 325.
HUbsohmann, Peraisohe Studien. 5
### HUB grep dīg/deg
132:Avesta II, p. 66, Anm. 7 durch *sundig, schuldig machen'
373:skr. avasthita 'dastehend, verbleibend, bestandig' etc.
693:Ob osset. bairag, dig. bairag junges Pferd, Fullen'
799:wiirdig, giiltig (WZKM 6, 79), an-vaver, an-vaver-akan
800:'unglaubwurdig, ungiltig, nichtig*. Vgl. zd. vaura- (aus
802:glaubwiirdig oben unter Nr. 16.
1239:bestandig, dauernd, ewig (denora. von pai Tuss' = ap.
1368:wendig zu machen suchen; phi. parlk bose Fee'
1845:zu zd. x^apara- giitig, gnadig (Epitheton weiblicher
2108:erwarten. Ich kann np. durust ganz, voUstandig,
2110:standig Min. Gl. 66 (LW. bal. drust^ afgh. drast ganz,
2111:vollstandig' u. s. w.) nur auf ein iran. "^drusta- = skr.
2256:*Ebenbild', skr. dig 'zeigen', subst. dig *Hinweis, Art and
2262:Nr. 563 diz, dSz *Burg', s. oben. Ob auch deg *Koch-
2267:dEg *Kesser) setzt ap. ^daika- voraus. Phi. dSg 'Kesser
4353:sie selbstRndig waren, nach dem oben p. 116 erwahnten
4549:aw(for;e; awvat;er 'unglaubwiirdig', vaver glaubwiirdig, np.
4558:*Oberhaupt, Chef* (selbstandig und als 2. Glied zahlreicher
4760:p. 36) ; baxsudan : baxsdyam 'gnadig sein, verzeihen . Von
4875:sUdan gnadig sein, verzeihen', paz. atvaxiaisni 'forgiving*--^
```


## [2026-09-04T15:07:58.392Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KNT p.191 leaf 206\"; awk 'BEGIN{RS=\"\\f\"} NR==207' KNT.txt; echo \"### KNT grep didā\"; grep -n -i 'didā\\|dida-\\|daida\\|diz' KNT.txt | head -20",
 "description": "Read Kent p.191 and grep didā"
}
```


### [2026-09-04T15:08:00.015Z] TOOL RESULT

```
### KNT p.191 leaf 206
n, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (conj. of Kent, cf. JAOS 54.46).
рата + gam- ‘go forth’: paragmata nsf. past pte. ($101, $103.IV, §122, 8132.2, §244) DNa 44f.
ham- + gam- ‘come together, assemble’: ha"- gmaté npm. past pte. ($101, $1081У, $1322, $140.V, $244) DB 2.32, 38, 43, 52, 58; 3.65. See also Надтаійла-.
gay- vb., see Jiv-. gara- ‘devouring’, see bdtugara-.
garta- sb., either ‘cave’ or ‘wagon’, see Asa- garla-.
Garmapada- adj. ‘Garmapada’, the fourth month, June-July: Elam. kormabadas, АКК. du-
183
'"üzu. From garma- ‘heat’, Av. garama-, Skt. gharmá-, Lt. formus ‘hot’, NEng. warm, pIE *gthormo-, cf. Gk. bepuos (with analogical -e-), + pada- ‘step, station’ ($29, §31, $149.1, $161.Ib, $165): ‘Heat-Station Month’. — Garmapadahya gsm, DB 1.42; 3.71, 46.
gav- sb. ‘cow, cattle’ ($101): Av. gau£, Skt. gaus, Gk. fois, NEng. cow, pIE nom. *g*dus: in Gaubaruva-, Gaumäla-, perhaps in Gatagu-.
gasta- adj. ‘repugnant, evil’; пі, as sb., ‘evil, harm’: past pte. ($85, $242.I) of vb. *gant- *gandh- ‘smell’, Av. ganti- ‘evil odor’ (AIW 493), duZ-gantt- ‘evil-smelling’ (AiW 757), Skt. gandhá- ‘odor’ (Bv. Gr. $179); for meaning, ef. Lt. odor ‘smell’, бй ‘(I have smelled), I hate’, odium ‘dislike, hatred’. Not abstract to same root, *gant-tdi-, nom. gasta', abl. shortened by haplology, as taken by Hz. AMI 8.68, ApL 173-7. gastá nsf. DNa 57f. дазій absn. DNa 52; XPh 57; ASa 5°; A’Sde 4 (gasta da, db; $53); A?Ha 6°.
gud- vb., see gaud-.
gub- vb., see gaub-.
grab- vb. ‘seize (аз possession), seize (as prisoner)’, pres. garbaya- (§30, $217): Av. grab-, pres. gaurvdya-, Skt. grabh-, pres. grbhdyah, NEng. grab, pIE *ghrebh-. See also Patigraband-. agar- . bayam Ist sg. imf. DB 24 bis; 4.7, 32; 5.25f; DNa 17; DSe 16; DZe 8. agarbáya imf. DB 2.88; 3.74, 90°; 5.12. agarbaya* 3d pl. imf. 04232.) DB 2.18; 3.48, 49; 5.27f. agarbayalà imf. mid. (§235.11) DB 1.42, 43, 81; 3.82f. When meaning ‘seize as prisoner’ (DB 2.4 second occurrence, 13, 88; 3.48, 49, 74, 90; 4.7, 32; 5.12, 25f, 27f) per- haps not agarb- but ágarb-, from à + grab- (see below).
à + grab- ‘seize (as prisoner)’: dgarbita пзш. past pte. pass. ($80, §217, $232.11) DB 2.73. For uncertain examples, see under grab- (uncom- pounded).
-cé (i.e. -cd) enel. conj. ‘and’: GAv. -@, LAv. -€a, Skt. ca, Gk. тє, Lt. -que, pIE уш, ~... -cé ‘both ... and’ DB 1.65, DNb 32; cà .. . -cã ula ‘both ... and... and’ DB 1.66-7. -cé DB 1.65 ter, 66, 66f; DPd 9f; DNb 32 bis; XPh 41, 51, 54. -ca-maiy DNb 28, 51, 52 (§51).
+++ canüm, see ustasand-.
canah- sb. ‘desire’, see Aspacanah-; cf. also kam-.
184 | 631689 V, ОГ car- vb. ‘move’, see abicarig; cf. also under
ucara-. cdra- (5126), see ucüra-.
| caša- sb. ‘eye’: to root in Skt. caks- ‘see,
speak’, derivatives cdksas- cakşu- cakgus- caksan-, and Ау. čašman-, Phi. NPers. čašm ‘eye’; initial u- of ucasma is an error (Bv. TPS 1945.53-4, quoting Jn. IF 25.182). The stem is caSa-, not caKman- (Kent, Lg. 19.225-6), since the nom.-acc. of nt. casman- would be cašmā and not ca$ma. Cf. $102, $143.I, $187.n1l. Attempts to explain the erroneous u- of ucaima, Wb. ZDMG 61.726; Wackernagel, KZ 61.205-8. саат asn. DB 2.75, 89 (Cameron found ст“ legible in 89, but only the final me in 75); caSa{m} (case and form uncer- tain) DSq 2.
ci- interrog.-indef. pron. ‘what, any’; col- lateral stem (8201) to OP ka-. See also -ciy, cid, cind, cijükara-.  ciš-ciy asn. ‘anything’ (§9.VI, $105, 5132.2, §201) DB 1.58, Lt. quicquid, pIE *q*id-q*id: reduplicated form with Med. sandhi; see OP -ciy for exact cognates.
-ciy encl. particle, emphasizing or generaliz- ing, nsn. or asn. of с1-: Ау, -Git, Skt. eid, СК. т, Tat. quid, pIE *q*id (840, §84, $113, 5191.11, §201, 6998.11). In the following combinations: aciy (q.v.) ХРЇ 21. aniyaš-ciy nsn. DB 4.46; XPa 13; aniya&-c (452.1) XPh 41f; aniyai-ciy npm. XPf 29. avas-ccy nsn. DNb 55; asn. DNb 5
### KNT grep didā
4220:48 дада : à : pasàva : didām : ашу
5555:didà- sb. ‘wall, stronghold, fortress’: N Pers. diz, pIE *dhióhà-, cf. Skt. dehi- ‘wall’, Gk. réxos,
```


## [2026-09-04T15:08:02.002Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### IEC grep dheigh\"; grep -n -i '^dheiĝh\\|^dheigh\\|^dhei' IEC.txt | head -10; echo \"### IEC grep leudh\"; grep -n -i '^leudh\\|^leud' IEC.txt | head -10; python3 - <<'EOF'\nimport re\npages=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(pages))\nfor pat in [r'^dheiĝh', r'^dheigh', r'^leudh', r'rōstāk|rostak|rūstā|rusta']:\n    for i,p in enumerate(pages):\n        if re.search(pat,p,re.M|re.I):\n            print(pat,'leaf',i, p.strip().split('\\n')[0][:80]); break\nEOF",
 "description": "Locate Mann IEC entries for dheigh and leudh"
}
```


### [2026-09-04T15:08:03.657Z] TOOL RESULT

```
### IEC grep dheigh
2741:dheig- (dhoig-?) ‘shoot, pierce, stab, sew’. Cf. dhig-
2753:dheigó, io “shape, mould, make’. (There is some confusion w. next, q. v.) WP I, 833 Tokh. (ambig.) A tsek-, B tsaik-; Lat. cf. fingo, pf. finxi beside figulo, figlinus, etc.; Osc. cf. fifikus “shalt make’; Fal. fifiked (if not fr. *tuak-, q.v.) “has shaped; MHG tichen, sv.l. *make, form" beside tich *dam'; OE dic: Du. dijk; (?) cf. Cz. diže (trough for kneading dough’, but see next entry); metath. in OCS ziždọ, zidati “build, found”; OLi. Ziedmi, Li. žiedžiù, Ziesti (“fashion on potter's wheel). See next entry
2754:dheigh- ‘shape, earth up; form, wall (There is some confusion with dheig- above). WP I, 833. Cf. dhoigh- Skt. (ambig. prob. o-gde) dehah, am “shape, body’; Av. (pairi-) daezo ‘surrounding fence” beside diz- “earth up, cover’; LW in Arm. dez ‘mound’, dizem ‘pile up’; Gk. teikhos “outer wall, dam’; Ose. feíhüss, acc.pl. ‘walls’; Go. digan (z-gde) ‘shape, mould’; OPr. zeidis (metath. *wall') For Cz. dize ‘kneading- trough” and OHG teic, E dough, etc. see dhoiĉh-. The connexion, if any, with OE digan ‘overcome, survive, benefit’ is obscure
2755:dheió (1) ‘suckle, milk; suck at the breast’. Cf. dhen- (1), dhinió. WP I, 829, and see dhoið Skt. dhayami; Av. dà-; Oss. däin, dajun, pp. dadton; Arm. diem; Gk. inf. thé-sthai "be suckled'; Hes. thenion ‘milk’, gala-thenós, aj. tunweaned'; Lat. cf. fe-mina; OHG Gen. lsg: taju beside MLG dien ‘suck, suckle’; OE dēon ‘suck’; cf. diend ‘suckling’; Sw. di ‘suck’; giva di ‘suckle’; Latv. dejals ‘mother’s milk, accretion of milk’. For Sw. dägga ‘suckle’ and OCS dojo, id. see dhoið. (NB. Per. dāyā ‘nurse, wetnurse, midwife�� is an Arabic LW). ON akr-dái “galeopsis? may belong here.
### IEC grep leudh
6401:leudho ‘stir, move’. See iudheio, ioudh- and next. WP I, 203 OLat. cf. ioubeo, ére (*order'. But class. jub-!); Ukr. judyty ‘stir’; Pol. judzic ‘incite’; Li. jáu- daus, jáudytis ‘rage’; jáudinu, D. v. ‘rouse’
9710:leud- (loud-, lud-) ‘deceive’. Cf. WP II, 406 & 416 Lat. e-lüdo, il-lüdo, ére, id. (but for lüdus ‘game’ cf. WP I, 661 & II, 402); W (prob.) Iludd, pl. -ion, m. ‘obstacle’; Go. liuts *deceit- ful”; Fris. liat, id.; ON ljótr ‘ugly’; mod. "fend. ish’; cf. also á-ljótr, gs -ljóts, m. “harm, slan- der; Sw. lytt ‘defective’; lyte, n. ‘defect’; z- gde: OE lot, n. ‘fraud, guile’; o-gde in OCS ludŭ ‘silly’; luZdo, luditi, v. ‘beguile’; Pol. tud- zic, id.; Cz. loudit, v. ‘entice’ beside pře-lud, m. ‘illusion’. Cf. loud- and Skt. rodàmi, v. ‘rave’
9711:leudheros (leudhər-) “active, free; action, freedom, abandon'. Cf. leus-. WP II, 417. Cf. leudhó and next. Armenian ambig., cf. plu- dhuró Arm. lur£, gs Iréo (gay, lively’, sic: Awgerian. Eng.-Arm. otherwise: 'earnest, serious") (!); Tokh. A lyutar ‘superior, high; highly’; Myc. and Gk. eleütheros ‘free’; Venetic louzera ‘the goddess Libera’; cf. louzerofhos "liberis"; Paelig. loufir ‘free’; Lat. liber, f.; libera, id. (& “bold; open"); Ir. luadar, m. ‘vigour, acti- vity'; cf. MIr. com-lüadar, m. (&company'. Cf. Lat. col-libertus & hliberr); WG cf. (z-gde) lodern, v. ‘thrive’
9712:leudhis ‘tribe, people’. Cf. leudhó, leudheros. WP II, 416
9715:leudho ‘grow, thrive’. WP II, 416. Cf. leu- dheros, leudhis, loudh- Skt. rodhàmi, id.; Av. raoðë, mp. id.; Mir. cf. lúad, m. ‘exertion’; Go. liudan ‘grow’; OHG ar-liutan, id.; OE leodan, sv. 2 ‘grow’; O-gde or z-gde in LG loden ‘grow, sprout’
9723:leudho — leuks-
leaves 858
^dheigh leaf 112 of a tinder-box';; MHG tëgel (?) (Ccrucible', if distinct from tigel, id. cf. La
^leudh leaf 256 �nísi, id.; Li. cf. gerésne “better?
rōstāk|rostak|rūstā|rusta leaf 44 m; slobber, prate’; LG praten "chat": beside prāt ‘gossip’; Norw. (fr. LG?) prat
```


## [2026-09-04T15:08:04.291Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SYN p.874 leaf 898\"; awk 'BEGIN{RS=\"\\f\"} NR==899' SYN.txt | head -80; echo \"### SYN grep raod\"; grep -n -i 'raoδ\\|raod\\|rōy\\|rūy\\|GROW' SYN.txt | head -20",
 "description": "Read Buck p.874 and grep raod"
}
```


### [2026-09-04T15:08:06.383Z] TOOL RESULT

```
### SYN p.874 leaf 898
ollection, Haridwar
EE oe
Digitized by Arya Samaj Foundation Chennai and eGangotri
830 SELECTED INDO-EUROPEAN SYNONYMS
12.11 PLACE (sb.)
Grk. = rézros Goth. stabs Lith. _vieta
NG réros ON stadr Lett. viela
Lat. locus Dan. _plads, sled ChSl. mésto
It. luogo, posto Sw. plats SCr. mjesto
Fr. lieu, place OE sldw, stede Boh.  misto
Sp. lugar, sitio ME _ stede, place Pol. miejsce
Rum. loc NE place Russ. mesto
Ir. di, ined, ditt, airm, Du. plaats Skt. stha@na-, sthala- maigen OHG - stat Av. gatu-, asah-, slana-
Nir. il, ionad MHG stat (ort)
W. lle NHG stelle, ort, platz
Br. lec’h
‘Place’ is understood here in the wide sense of NIE place (sb.). Besides the words listed as the most important, there are many others which are used for ‘place’ mainly in the geographical sense, ‘region’ or ‘town’, as NG pépos (proper- ly ‘part’, 13.23), Sp. paraje (: parar ‘stop’), etc.
1. Grk. rémos, etym. dub., perh. : Lith. tapit ‘become’, Lett. tapt ‘become, attain’, OF pafian ‘consent to, allow’ (as orig. ‘give place to’, like NE allow through Fr. alouer fr. Lat. adlocare). Walde-P. 1.748. Boisacq 975.
2. Lat. locus, early stlocus (Festus), etym. disputed, but prob. (*stl-o-ko-) fr. the root *stel- in OHG stellan ‘set up’, etc. (12.12). Walde-H. 1.818. Hence It. luogo, Fr. lieu, OSp. luego, Rum. loc; Sp. lwego now only as adv., as sb. re- placed by deriv. lugar fr. Lat. locdlis. REW 5097, 5093.
It. posto, Sp. puesto, fr. Lat. positum, pple. of ponere ‘put’ (12.12).
Fr. place (> ME, NE place), also MHG, NHG plaiz, Du. plaats (MLG plaise > Dan. plads, Sw. plats), fr. Lat. platea ‘street, open area, courtyard’ (> It. piazza, etc.), this fr. Grk. mdareta (c5és), fem. of darts ‘wide’. REW 6583. Falk-Torp 833. Franck-v.W. 504. NED s.v. place, sb.
Sp. sitio, deriv. of vb. borrowed fr. Gme. *sitjan in ON sitja, OHG sizzan, etc. ‘sit’ (12.13). REW 7961b.
3. Ir. dia (gen., acc. don), orig, ‘earth’ : Grk. x@av ‘earth’, ete. (1.21), Walde-P. 1.663. Pedersen 1.89. Ven- dryes, RC 40.437 ff. Cf. Toch. A tkam ‘earth’ and ‘place’ (JAOS 67.43).
Ir. ined, inad, NIr. ionad, epd. *eni- pado-, cf. Ir. ed ‘space of time’, Gall. candetum (*cant-edum) ‘spatium centum pedum’: Grk. zédov ‘ground’, ChSI. podu ‘ground, foundation’, Hitt. pedan ‘place’ (Sturtevant, Hitt. Gloss. 123 with refs.). Walde-P. 2.24. Pedersen 1.91.
Ir. aitt, NIv. ait perh. (fr. *pdth-ni-) : Skt. pdthas- ‘spot, place’ also path- ‘path, way’, ChSl. patt ‘way’, etc. (10.71). Walde-P. 2.26. Pedersen 1.161.
Ir. atrm, etym.?
Ir. baile ‘place’, but esp. ‘dwelling place’ (NIr. ‘town, village, homestead, home’), etym.? Walde-P. 2.141.
Ir. maigen, fr. mag ‘plain’ (1.23), Pe- dersen 1.96.
W. lle, Br. lec’h : Iv. lige ‘bed, grave’, Grk. déxos ‘bed’, fr. root in Ir. laigim, Goth. ligan, etc. ‘lie’ (12.14). Walde-P. 2.424. Pedersen 1.98.
4. Goth. stabs, ON stadr, Dan. sted, OE, ME stede (NE stead in instead, etc.), OHG stat (NHG statt ‘place’ most- ly in phrases and epds., also stadt ‘city’); orig. ‘standing place’ : Lat. statid, sla- tus, ete., fr. IE *sta- ‘stand’. Walde-P. 2.605. Falk-Torp 1154.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar 4
Di
### SYN grep raod
71:The kind of thinking that distinguishes man n from brute has been built up by and is dependent upon the use of symbols. Since vocal utterance at- tained a higher development than gesture as a means of communication, these symbols are, in fact, the words. Animals, to be sure, have cries which in some cases cover a very considerable range of emotions and to a certain extent serve to communicate. But these are limited to the immediate ex- perience: they are not detachable symbols capable of expressing past or future experience or any abstract concept. Yet such cries, which comprise all that primitive man inherited from his ancestry, must perforce be the starting-point of human speech. Primitive man, with his more highly de- veloped brain, gained an awareness of a connection between the sound and something expressed by it. With this step taken, a nucleus provided, and doubtless aided by gesture, human speech progressed and in turn became the dominant factor in man’s further mental growth. That is, we have the spwal development: superior brain (there is, of course, a “why?” to this too) > primitive human speech > organized conceptual thought. Any more detailed picture of the process, of the much discussed “origin of lan- guage’, we shall never have. The relatively brief period of recorded speech is separated by a vast interval from the beginnings of human speech—far beyond the reach of the historical-comparative method. Nor are we further concerned here with this remote problem.
95:Various miscellaneous extensions or transfers are due to a similarity of condition or result or some natural sequence. ‘Green’ and ‘unripe’ usually coincide, though, to repeat a phrase often quoted, blackberries are red when they are green. This use of green is felt as secondary; yet in origin the color word itself, derived from the root of grow, was based on the color of growing
1387:tourse’ (with or without water); Ir. sruaim, sruth ‘stream, river’ (NIr. ‘river’ in river names), NIr. srutén ‘brook’, W. ffrwd ‘stream’, Br. froud ‘torrent’ (so Pedersen 1.35; fr. *spru-tu- : OE spritan ‘sprout’, etc. Walde-P. l.c.); ON straumr, OE stréam, OHG strdm, etc. ‘stream’; Lith. sr(z)ové, Lett. strava, etc., ‘stream’, Pol. strumier, strumyk ‘brook’; Skt. srotas-, sravat-, Av. @raotah- (in cpds.), ravan-, raodah-, ‘stream, river’, OPers. rauta ‘river’ (used of the Nile), NPers. rid ‘river’.
1536:A widespread group of words for ‘tree’, many of them meaning also ‘wood’, go back to an IE word which probably denoted a particular kind of tree, namely the oak. Others are from those for ‘woods’ (1.41); some perhaps from the notion of ‘growth’; while sev- eral are of obscure origin.
1551:3. Lat. arbor, etym. dub., perh. (through a by-form with dh beside d) : Lat. arduus ‘high, steep’, Ir. ard ‘high, tall’, etc. with development through ‘growth’ or ‘tall’ (cf. Boh. strom, below, 7). Walde-P. 1.148 ff. Walde-H. 1.62.
1558:Du. boom, OHG, MHG boum, NHG baum, etym. dub. (: Grk. diya ‘growth’, etc.?). Walde-P. 2.143. Feist 73. Falk-Torp 92.
1761:2. Grk. Bpovrn : Bpéuw ‘roar’, of imi- tative orig., parallel to *bhrem- in Lat. bremere, OHG breman, etc. ‘roar, growl’.
2304:NHG kerl. Perh. as ‘full-grown man’ : | séri- ‘woman, female’) Lat. pibés Grk. yépw, Skt. jarant- ‘old man’. | ‘adult’. Walde-P. 2.83. Ernout-M, Walde-P. 1.600. Falk-Torp 497. | 819f. Kluge-G. 296. 2.22 WOMAN Grk. yur Goth. qiné Lith. moteris, moteriskeé, NG yuvaixa ON kona Zmona Lat. mulier, féemina Dan.  kvinde Lett. steva It. donna Sw. kvinna ChSl. Zena Fr. femme OE cwene, wif, wifman SCr. Zena Sp. mujer ME —  quene, wife, woman Boh. Zena Rum. femeie NE woman Pol. kobieta Tr. ben, fracc Du. vroww Russ. ZenSéina Nir. bean OHG  wib, quena Skt.  jani-, nari-, stri- W. gwraig, benyw, dynes MHG wip Av. Jant-, ndtri-, strz- Br. maouez NHG frau, weib
2426:Grk. xépos (mostly poet.), Ion. xodpos, fr. *xopros, with fem. xdpy ‘girl’, Ion. koUpn, Dor. xwpa, Arc. kdpfa : xopévvupe ‘satisfy’ orig. ‘nourish’, Lat. créscere ‘grow’, ete. Walde-P. 1.408. Hence NG xépy ‘girl, daughter’ or xopizo. with dim. suffix.
3507:szwagrowa; bratowa (c)
3607:SCr. Sogorica, Boh. svakrova (k fr. old svekra, etc.), Pol. szwagrowa, fems. of Sogor, svagr, szwagier respectively.
4100:2. Goth. stiur ‘male calf’ (renders rév pocxov), ON stjorr (rare), OE stéor, OHG stior, all mostly ‘young ox’, MHG, NHG stier ‘bull’ (but dial. ‘ox’), NE steer ‘(young) ox’ (in U.S., where oxen are used for hauling, steer is still ‘young ox’, but otherwise and regularly in the packing industry steer is the grown cas- trated animal raised for beef, and oz is
4218:On vedr, Dan. vedder, Sw. vddur, OF weder (also ‘wether’), OHG widar (also ‘wether’), NHG widder : Goth. wiprus ‘lamb’, orig. ‘yearling’, like Lat. vitulus ‘calf’, etc. (3.24) : Grk. éros ‘year’, etc. Walde-P. 1.251. Shift from ‘lamb’ to the grown male, either ‘ram’ or ‘wether’.
4230:3.27. ‘Wether’. The castration of male sheep for fattening is an old and almost universal practice, and the ‘weth- er’ (understood here in the technical sense of NE wether ‘castrated sheep’) is the grown sheep par excellence. Hence the generic word for ‘sheep’, where it is not a distinctively feminine form, may be commonly applied to the ‘wether’ ; even though distinctive terms for the latter exist. Some of these are unfamil- iar to the layman (as NE wether except in bellwether). Conversely some words that were originally specific for ‘wether’ have become generic (as Fr. mouton) or through generic use have acquired a new specialization (as Fr. brebis ‘ ewe’, fr. Lat. vervex ‘wether’).
4421:7. SCr. nerast, epd. of neg. ne and rasti ‘grow’, lit. ‘one that does not grow’, applied to a tree that will not grow and to the ‘boar’ as the swine that will not fatten, in contrast to the castrated hog. Rjetnik Akad. 8.46.
4435:9. Lat. maidlis (Varro, RR 2.4.21 castrantur verres—quo facto nomen mu- tant aique e verribus dicuntur maiales), hence It maiale, perh fr. Maia (or only pop. etym.?), in any case prob. in- fluenced by maior ‘larger’, with refer- ence to the greater growth of the cas- trated animal. Walde-H. 2.13. Er- nout-M. 582.
4631:4, OE colt, used for the young of a horse, ass, or even a camel, ME colte, NE colt: Sw. kull ‘brood, litter’, Sw. dial. kult ‘pig, overgrown boy’, Norw. kult ‘thick round shape, block’, Skt. gadi- ‘young ox’, Goth. kilpet ‘womb’, OE cild ‘child’, etc. Walde-P. 1.614. Falk-Torp 593, 430. Cf. ON hiann ‘block’ and ‘young bear’, NE cub: Norw. kubbe ‘block, stump’.
5120:5. Skt. bhramara-, of imitative orig. here ‘buzzing’, but prob. the same as in Lat. fremere, OHG breman ‘growl, mut- ter’, NHG bremse ‘gadfly’, ete. Walde- P. 2.202.
5274:to animals and only contemptuously or facetiously to man, as NE muzzle or snout, Fr. gueule, NHG maul, ete. But words of this type, and in general vulgar expressions, of which there is a luxuriant growth, especially for certain parts (cf, Goldberger, Glotta 18.16 ff.), may in part become the accepted terms,
5490:3. Ir. adarc, NIr. adharc, an old con- tinental loanword with Celtic suffix (cf. Gallo-Lat. adarca ‘spongy growth on sedge’) fr. Basque adar ‘horn’. Walde- H. 1.12. Pokorny, Z. celt. Ph. 14.273, 16.112.
```


## [2026-09-04T15:08:06.742Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SOD grep dyz / rwd\"; grep -n -i \"^ *[0-9]* *δyz\\|dyz\\b\\| δyz\\|dyz'\\|^[0-9]* *rwδ\\|rwδ \\|rwd \\|rwδy\" SOD_pages.txt | head -30; echo \"### SOD 151 / 344 as entry numbers\"; grep -n -E '^ *(151|344) ' SOD_pages.txt | head",
 "description": "Grep Sogdian dictionary for dyz and rwd"
}
```


### [2026-09-04T15:08:07.351Z] TOOL RESULT

```
### SOD grep dyz / rwd
9070:                                                                                                                  *wdyz-
9123:     be numbed                                                    1867 Nitfynt     B => >wdyz-
9126:1856 *>wps- S                                                          o5ez ?, o5ez ? =^wdyz-
9146:      o/upde    (>wbty)     ©pp. pi. -t =»}wfc                    1871 Svdyz-      C                              j^^
14550:      5cw-mec                                                         3826 dyz> C «* 5yz>
19401: 5477 mrwrwd C                                                     5489 mspwyyc S               (^y^^j^JU^oU
24138:     py8ez (prdyz) ©Av. pari-daeza ©ob. -y; pi.                   parxut ©pt. st. =»prywn-, prywt*k
24145:7104 prdyz C *=» pr8yz                                            parxez ©<* para-hazya- ? =^pryyz-
28381:                                                                        8563 rwd C =» rw5
42017:                                                     <rWd <YHA <YYAV <YYaA «YVA
### SOD 151 / 344 as entry numbers
4204:                                                          151 "m'n B                                     o>*S<j^j
```


## [2026-09-04T15:09:18.578Z] AGENT (thinking)

I've mapped out all remaining lookups needed across the various dictionaries and leaves. Next I'll build a small leaf-printing helper, then run all the lookups in parallel.


## [2026-09-04T15:09:29.513Z] TOOL CALL #21: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py <<'EOF'\n#!/usr/bin/env python3\n\"\"\"usage: leaf.py FILE (leaf N | grep PATTERN [maxhits]) [--chars N]\nPrints the leaf, its numeric-only lines (candidate printed page numbers), and matches with context.\"\"\"\nimport sys,re\nargs=sys.argv[1:]\nchars=1500\nif '--chars' in args:\n    i=args.index('--chars'); chars=int(args[i+1]); del args[i:i+2]\nf=args[0]; mode=args[1]\npages=open(f,encoding='utf-8',errors='replace').read().split('\\f')\ndef nums(p):\n    out=[]\n    for l in p.split('\\n'):\n        s=l.strip()\n        m=re.fullmatch(r'[—\\-–\\s]*(\\d{1,4})[—\\-–\\s]*',s)\n        if m: out.append(m.group(1))\n        else:\n            m=re.match(r'^(\\d{1,4})\\s+\\S',s) or re.search(r'\\S\\s+(\\d{1,4})$',s)\n            if m and len(s)<90: out.append(m.group(1)+'?')\n    return out\nif mode=='leaf':\n    n=int(args[2]); p=pages[n]\n    print(f'--- {f} leaf {n} / {len(pages)}; page-number candidates: {nums(p)[:8]}')\n    print(p[:chars] if chars>0 else p)\nelse:\n    pat=args[2]; mx=int(args[3]) if len(args)>3 else 5; hits=0\n    for i,p in enumerate(pages):\n        for m in re.finditer(pat,p,re.M|re.I):\n            hits+=1\n            s=max(0,m.start()-100); e=min(len(p),m.end()+chars)\n            print(f'--- {f} leaf {i}; page-number candidates: {nums(p)[:8]}')\n            print(p[s:e].replace('\\n',' ')); print()\n            break\n        if hits>=mx: break\n    if not hits: print('NO HITS',pat)\nEOF\ncd /home/sfmqrb/git/rishe/data/verification/sources/refs && L=\"python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py\"; \n$L KLN_1966.txt grep '^berakah' 1 --chars 900; $L KLN_1966.txt grep '^cherub,' 1 --chars 200; $L KLN_1966.txt grep '^griff' 3 --chars 900; $L KLN_1966.txt grep '^emerald' 1 --chars 1200; $L KLN_1966.txt grep '^liberal,' 1 --chars 900; $L KLN_1966.txt grep '^liberty' 1 --chars 400",
 "description": "Create leaf helper and grep KLN berakah/cherub/griffin/emerald/liberal"
}
```


### [2026-09-04T15:09:31.274Z] TOOL RESULT

```
Exit code 127
(eval):39: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):39: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):39: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):39: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):39: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):39: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
```


## [2026-09-04T15:09:33.264Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && L=\"python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py\"; $L KLN_1966.txt grep '^checkmate' 1 --chars 1200; $L KLN_1966.txt grep '^mate,  n.,  checkmate' 1 --chars 300; $L KLN_1966.txt grep '^mat,  adj' 1 --chars 200; $L KLN_1966.txt grep '^paradise' 1 --chars 1200; $L KLN_1966.txt grep '^dough' 1 --chars 900; $L KLN_1966.txt grep '^Margaret' 1 --chars 600; $L KLN_1966.txt grep '^dig,' 2 --chars 600; $L KLN_1966.txt grep 'Pers\\.  dig\\|Pers\\.  deg\\|Pers\\.  dig' 3 --chars 400",
 "description": "Grep KLN checkmate/mate/paradise/dough/Margaret/dig"
}
```


### [2026-09-04T15:09:34.952Z] TOOL RESULT

```
Exit code 127
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
```


## [2026-09-04T15:09:36.318Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && L=\"python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py\"; $L POK_01.txt grep 'dhei[gĝ]h' 2 --chars 2500; echo ======; $L POK_02.txt grep '^1\\.  *leudh\\|leudh-' 2 --chars 2000; echo =====; $L POK_02.txt grep '^mad-\\|^ *mad- ' 2 --chars 1500",
 "description": "Read Pokorny dheigh, leudh, mad entries"
}
```


### [2026-09-04T15:09:37.942Z] TOOL RESULT

```
Exit code 127
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):1: ===== not found
```


## [2026-09-04T15:09:39.318Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && L=\"python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py\"; $L KNT.txt grep 'didà- sb\\|didā- sb\\|dida- sb' 1 --chars 700; echo =====; $L SYN.txt leaf 942 --chars 600; $L SYN.txt grep 'raoδ\\|raoda\\|raod-' 3 --chars 1200; echo =====; $L SOD_pages.txt leaf 217 --chars 2500; echo ====; $L SOD_pages.txt leaf 410 --chars 2500",
 "description": "Read Kent didā, Buck p.874, Sogdian leaves 217 and 410"
}
```


### [2026-09-04T15:09:40.825Z] TOOL RESULT

```
Exit code 127
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):1: ==== not found
```


## [2026-09-04T15:09:46.817Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && L=\"python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py\"; for n in 306 307 308 309 310; do $L BQT_v2_pages.txt leaf $n --chars 0 | grep -n 'دژ\\|دز\\|^---' | head -12; done; echo \"=== grep دژ headword\"; grep -n '^ *دژ\\b\\|^دژ ' BQT_v2_pages.txt | head; echo \"=== دیوار\"; grep -n '^ *دیوار' BQT_v2_pages.txt | head; echo \"=== دیگ\"; grep -n '^ *دیگ\\b\\|^ *دیگ ' BQT_v2_pages.txt | head; echo \"=== دیزی\"; grep -n 'دیزی' BQT_v2_pages.txt | head -5; echo \"=== روییدن/روی/رستن\"; grep -n '^ *روییدن\\|^ *رُستن\\|^ *رستن\\|^ *روی \\|^ *روی$' BQT_v2_pages.txt | head; echo \"=== رستم\"; grep -n '^ *رستم\\|^ *رُستم' BQT_v2_pages.txt | head; echo \"=== رز\"; grep -n '^ *رز \\|^ *رَز\\|^ *رز$' BQT_v2_pages.txt | head",
 "description": "Locate Borhan-e Qate' vol 2 entries for dež, dīvār, dīg, rūyīdan, Rostam, raz"
}
```


### [2026-09-04T15:09:48.454Z] TOOL RESULT

```
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
=== grep دژ headword
=== دیوار
=== دیگ
=== دیزی
22049:  ‫معنی از باد کلمةٌ « دیگه » («‪.‬م‪ ).‬د قاب اص ‪ ۱۹۲‬ح» ‪.‬قس‪ :‬دیزیی ورك ‪:‬‬                            ‫‪ ۴‬م‪-‬اين‬
26532:                                         ‫ر‬                   ‫دیزی راز = بعنی رحمتی بکن ‪۰‬‬
=== روییدن/روی/رستن
=== رستم
=== رز
```


## [2026-09-04T15:09:49.819Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v1 پالیز\"; grep -n '^ *پالیز\\|^ *پاليز' BQT_v1_pages.txt | head; grep -n 'پالیز\\|پاليز' BQT_v1_pages.txt | head -5; python3 - <<'EOF'\npages=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if re.search(r'^\\s*پال[یي]ز',p,re.M):\n        print('leaf',i); print(p[:3000]); break\nEOF",
 "description": "Locate pālīz in Borhan vol 1"
}
```


### [2026-09-04T15:09:51.606Z] TOOL RESULT

```
=== BQT v1 پالیز
23590:پالیز بان۷ - بافبان و بتان بان -
23594:پالیزبان است که محافظت کننده باغ وبوستان
559:باغ‌و بوستانست. لفت‌پاردوس ار سنی‌بمعتی باغ وپالیز پارسی و فردوس عر یی ۸
23590:پالیز بان۷ - بافبان و بتان بان -
23594:پالیزبان است که محافظت کننده باغ وبوستان
23615:۸ مر کب از: پالیز ۳ وان
leaf 581
خورند و معرب‌آن فالوزح باشد! - وپاكوساف
کرده شده از نش را یز گویند - و بممتی کته
ترازو هم آ هده است .
بالوش- بروزن آغوش؛ کافورمفشوش‌را
کوند» و بلین بی قطه هم درست است .
بالو نه هه بر وزن وآژونه. بمضی‌پالوانه
است که ترشی الا باشد؟ .
با لهنگه ۴ - بممنی‌بالاهنگه‌ات‌وآن
دوالی ورسمانی باشد که‌بر کنارلجام اسب جنببت
بندند» وصید و شکار و مجرم و گناهعار را نیز
بدان‌محکم بر شدند و کمند دوشاخه وچویکه
بر کردن سکد نهند - ونزد مجردین آنچهباعث
تعلق باشد .
بالیدن؟ بر وزن حالیدن ؛ بمسنی
جستجو کردن و تفحص تنمودن و صاف کردن
باشد.
پالیه * ح بر وزن تا دیده , صاف
شده وصاف کرده . و خلاصه را گوبند - وبمعنی
افزوده حم هت وججو کرده ونف<ص‌لمودمرا
نی زگوبند .
(۱) خم ۳: شبه .
هالیز ۱ ۰ بر وزن کاریز » بمعنی باغ
و وستان و کشت زار باشد عمومات و خریزه‌زار
وخیار زار و هندوانه زار را گویند خصوسا ۰
پالیز بان۷ - بافبان و بتان بان -
ودهقان و نگاهدارنده فالز را گویند- وتم‌صوتی
است از موسیقی .
با لیز و ان 2 با واو بروژن وععنی
پالیزبان است که محافظت کننده باغ وبوستان
و فالیز باشد - ونام صوتی است ازموسيقی .
پاليك - بر وزن باربك , پاتابه و پا
پیچ را گوند - و لفافه را نیز گفته‌اند - وبمعنی
کفش و بای افزار چردن هم‌آعده ات .
۵ ه بر وزن معنی وام است که‌فرض
باشد*٩-‏ و بمعنی‌شیبه(۱) ونظیرومانند- ورنگگ
ولون عمآمده است ٩۱‏ #۶
پاهس » بفتح میم‌بروزن اکس »بمعنی
پای بند باشد بعنی شخصبکه در شهر خود با
مه کر از ترا
بطرف دیگر رفت و در آنجا نز تنواند بود ٩۴‏
۳ ۳۳ ره 4 مالوانه :
پالودجان خویش بيالونة بلا
۴ رد : بالاهشگه ۰
و هم بمعتی نرأوبدن, زهیدن :
چودید ان بر و چهرء دلیذس
زستان مادر بپالید شیر. فردوسی‌طوسی.
بیاراست شهری زکاخ بلند
(بسوند حفاظت). ٩‏ - 4: اغت‌نامد.
ص : لو از دسباچة مولف .
۸ مر کب از: پالیز ۳ وان
۶۰ له : وام. 2-68 : فام و نیز
بقبه در فص ۳۹۶
```


## [2026-09-04T15:09:54.317Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF رز\"; grep -n '^ *رز\\b\\|^ *رَز' FSF_pages.txt | head; python3 - <<'EOF'\nimport re\npages=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(pages):\n    m=re.search(r'^\\s*رَ?ز\\s*[:(\\-—]',p,re.M)\n    if m:\n        print('leaf',i); print(p[max(0,m.start()-200):m.start()+1200]); break\nEOF\necho \"=== AFM rawnaq/rawda\"; grep -n 'الرونق\\|رونق' AFM_pages.txt | head -5; grep -n 'الروضة\\|روضة' AFM_pages.txt | head -5",
 "description": "Locate raz in Noushin's Shahnameh glossary and rawnaq/rawda in Addi Shir"
}
```


### [2026-09-04T15:09:56.138Z] TOOL RESULT

```
=== FSF رز
=== AFM rawnaq/rawda
2956:ܡ ܐܠ والترونق وايرئاق ܐ ܢ‎ 1
3877:( النرْق) اليد ( شفاء الغذيل ) ٠‏ معرب نزخ وهعناه السعد والرونق
1920:+ (الروضة ) من الرمل والعشب مستتقع الا تكو النضنت مز القز به 11
1921:وفي الكلمات الروضة ® 1 ٠‏ في !ܐܕܩ ܐܨ 03 عن ديز وهي ܬ الاء في
```


## [2026-09-04T15:09:57.338Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && L=\"python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py\"; echo \"=== FSD vol3 mat\"; $L FSD_vol3.txt grep '^mat[,\\s]|^mat\\s*\\(' 3 --chars 900; echo \"=== FSD vol3 mattus\"; $L FSD_vol3.txt grep 'mattus' 2 --chars 400; echo \"=== FSD vol1 checkmate\"; $L FSD_vol1.txt grep '^check-?mate' 2 --chars 900",
 "description": "Grep Funk and Wagnalls for mat, mattus, checkmate"
}
```


### [2026-09-04T15:09:59.055Z] TOOL RESULT

```
Exit code 127
=== FSD vol3 mat
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
=== FSD vol3 mattus
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
=== FSD vol1 checkmate
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
```


## [2026-09-04T15:10:00.077Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && L=\"python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py\"; echo \"=== PHN 257\"; $L PHN.txt leaf 288 --chars 3000; echo \"=== DEV 159\"; $L DEV.txt leaf 189 --chars 3000; echo \"=== LKT 115\"; $L LKT.txt leaf 141 --chars 3000; echo \"=== SKT 163\"; $L SKT.txt grep '^EMERALD' 1 --chars 500",
 "description": "Read Pihan p.257, Devic p.159, Lokotsch p.115, Skeat emerald"
}
```


## [2026-09-04T15:10:00.095Z] TOOL CALL #30: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-09-04T15:10:01.732Z] TOOL RESULT

```
Exit code 127
=== PHN 257
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
=== DEV 159
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
=== LKT 115
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
=== SKT 163
(eval):1: no such file or directory: python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py
```


### [2026-09-04T15:10:01.740Z] TOOL RESULT

```

```


## [2026-09-04T15:10:17.083Z] AGENT (thinking)

I'll fix the helper invocation issue with zsh's `$L` splitting, then run all the independent lookups in parallel: the KLN/POK/KNT/SYN/SOD/FSD/PHN/DEV/LKT/SKT etymology searches, unanchored BQT v2 greps to work around bidi marks breaking `^`, FSF رز context search, AFM leaves for rawnaq/rawḍa, and archive+read of the vajehyab (Mo'in) and AHD pages via fetch_source.py.


## [2026-09-04T15:10:20.063Z] TOOL CALL #31: Bash

```json
{
 "command": "printf '#!/bin/sh\\nexec python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/leaf.py \"$@\"\\n' > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf && chmod +x /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf && cd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf && $LF KLN_1966.txt grep '^berakah' 1 --chars 900; $LF KLN_1966.txt grep '^cherub,' 1 --chars 200; $LF KLN_1966.txt grep '^griff' 3 --chars 900; $LF KLN_1966.txt grep '^emerald' 1 --chars 1200; $LF KLN_1966.txt grep '^liberal,' 1 --chars 900; $LF KLN_1966.txt grep '^liberty' 1 --chars 400",
 "description": "Fix helper wrapper; grep KLN berakah/cherub/griffin/emerald/liberal"
}
```


### [2026-09-04T15:10:22.585Z] TOOL RESULT

```
NO HITS ^berakah
--- KLN_1966.txt leaf 155; page-number candidates: ['275']
 For  the second  element  see  ncso-. chert,  n.,  a  kind  of  quartz.  —  Of  uncertain  origin. cherub,  n.  —  Heb.  klrubh ,  ‘winged  angel’,  prob. rel.  to  Akkad,  karabu,  ‘to  bless’,  karibu,  ‘one who  blesses’,  epithet  of  the  bull-colossus,  and  to Heb.  bertikh,  ‘he  blessed’,  berakh

--- KLN_1966.txt leaf 367; page-number candidates: ['681']
dv.,  grievous-ness,  n. griff,  n.,  a  narrow  glen  {North.  Engl.)  —  Of  un¬ certain  origin. griff,  n.,  a  claw.  —  F.  griff e.  See  next  word, griffe,  n.,  an  ornament  resembling  a  claw.  —  F. griffe,  ‘claw’,  fr.  griffer,  ‘to  seize’,  which  is  prob. borrowed  fr.  OHG.  grifan,  ‘to  seize’.  See gripe  and  cp.  griffonage. griffin,  griffon,  gryphon,  n„  a  mythical  animal.  — ME.  griffon,  fr.  OF.  grifoun  (F.  griffon),  fr.  Late L.  gryphus  (whence  also  It.,  Sp.  grifo,  OHG., MHG.  grif,  G.  Greif  ‘griffin’),  fr.  Gk. gen.  Ypumi?,  which  was  prob.  borrowed  from the  Semites  through  the  medium  of  the  Hittites. Cp.  Heb.  klrubh,  ‘a  winged  angel’,  Akkad. karibu,  epithet  of  the  bull-colossus,  lit.  ‘one  who blesses’,  and  see  cherub.  Cp.  also  the  second  ele¬ ment  in  hippogriff.  The  connection  of  Gk.  ypu'J', ‘griffin’,  with  YpumS?,  ‘curved,  hooked,  hook¬ nosed’,  is  folk  etymology, griffin,  n.,  in  India,

NO HITS ^emerald
NO HITS ^liberal,
NO HITS ^liberty
```


## [2026-09-04T15:10:23.750Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; $LF KLN_1966.txt grep '^checkmate' 1 --chars 1200; $LF KLN_1966.txt grep '^mate,  n.,  checkmate' 1 --chars 300; $LF KLN_1966.txt grep '^mat,  adj' 1 --chars 200; $LF KLN_1966.txt grep '^paradise' 1 --chars 1200; $LF KLN_1966.txt grep '^dough' 1 --chars 900; $LF KLN_1966.txt grep '^Margaret' 1 --chars 600; $LF KLN_1966.txt grep '^dig,' 2 --chars 600; $LF KLN_1966.txt grep 'Pers\\.  dig|Pers\\.  deg' 3 --chars 400",
 "description": "Grep KLN checkmate/mate/paradise/dough/Margaret/dig"
}
```


## [2026-09-04T15:10:26.002Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; $LF POK_01.txt grep 'dhei[gĝ]h' 2 --chars 2500; echo ======; $LF POK_02.txt grep '^1\\. *leudh|leudh-' 2 --chars 2000; echo =====; $LF POK_02.txt grep '^mad-|^ *mad- ' 2 --chars 1500",
 "description": "Read Pokorny dheigh, leudh, mad entries"
}
```


### [2026-09-04T15:10:26.366Z] TOOL RESULT

```
NO HITS ^checkmate
--- KLN_1966.txt leaf 508; page-number candidates: []
 to  defeat, overcome’,  fr.  mat,  ‘checkmated ;  defeated,  over¬ come’.  See  cp.  mat,  ‘dull’. mate,  n.,  checkmate.  —  ME.  mat,  fr.  MF.,  fr.  OF. See  prec.  word. mate,  n.,  a  companion.  —  ME.,  fr.  MLG.  mate, mat,  ‘companion’,  orig.  ‘a  messmate’,  whence also  Du.  maat;  cp.  Dan.,  Swed.  mat,  OHG. gimazzo,  MHG.  gema33e,  ‘messmate’,  G.  Maat, ‘mate’;  fr.  Teut.  base  *mati-,  ‘food’,  

--- KLN_1966.txt leaf 508; page-number candidates: []
  with  a  mat  or mats,  matt-ed,  adj.,  matt-ed-ly,  adv.,  matt-ed- ness,  n.,  matting  (q.v.) mat,  adj.,  dull  (said  of  color  or  a  surface).  —  F., ‘dull,  lusterless,  unpolished’,  fr.  OF.  mat,  ‘de¬ feated,  afflicted,  depressed,  dejected;  dull’,  fr. Arab,  mat  in  the  sentence  mat 

--- KLN_1966.txt leaf 601; page-number candidates: ['1', '1126', '1127']
  (q.v.),  paradisiac(ai) (q.v.),  paradis-ial,  paradis-ian,  paradis-ic,  para- dis-ic-al,  adjs. Paradisea,  n.,  the  typical  genus  of  birds  of  para¬ dise.  —  ModL.,  fem.  of  ML.  paradiseus,  ‘per¬ taining  to  paradise’,  fr.  Late  L.  paradisus.  See prec.  word. Derivative:  paradise-an,  adj.,  pertaining  to birds  of  paradise. 1 i I ! i paradisiacal,  also  paradisiac  adj.,  pertaining  to, or  resembling,  paradise.  —  Late  L.  paradisiacus, fr.  L. paradisus.  See  paradise  and  suff.  -acand  -al. parados,  n.,  parapet  behind  a  trench.  —  F.,  prop, ‘defense  from  the  rear’,  coined  fr.  para-,  ‘that which  protects’,  and  F.  dos,  ‘back’,  fr.  L.  dor¬ sum.  See  dorso-. paradox,  n.,  a  statement  seemingly  absurd,  yet really  true.  —  F.  paradoxe,  fr.  L.  paradoxum, fr.  Gk.  7tapd8o!;ov,  ‘paradox’,  prop.  neut.  of  the adjective  itapiSo^o?,  ‘contrary  to  expecta¬ tion,  incredible,  marvelous’,  which  is  formed  fr. ttapa  (see  para-,  ‘beside,  contrary  to’)  and  86!;a, ‘opinion,  expectation’.  See  doxastic  and  cp. words  there  referred  to. Derivatives:  paradox,  tr.  and  intr.  v.,  paradox¬ al,  paradox-ial,  paradox-ic-al,  adjs.,  paradox-ic- al-ly,  adv.,  paradox-ic-al-ity,  n.,  paradox-ic-al- ness,  n.,  parad

--- KLN_1966.txt leaf 260; page-number candidates: ['476']
tist.  —  Du. doper,  lit.  ‘dipper’,  fr.  dopen,  ‘to  dip’.  See  dip and  cp.  dope. dopplerite dough dopplerite,  n.  —  G.  Dopplerit;  named  in  1849 after  the  German  physicist  Christian  Johann Doppler  (1803-53).  The  G.  stiff,  -it  represents Gk.  -Err)  4;  see  subst.  suff.  -ite. dor,  n.,  a  droning  insect,  the  dorbeetle.  —  ME. dore,  fr.  OE.  dora,  ‘bumblebee’,  rel.  to  MLG. dorte,  ‘drone’,  from  the  I.-E.  imitative  base *dher-,  ‘to  hum,  buzz,  murmur’.  See  drone. Dora,  fem.  PN.  —  A  shortened  form  of  Doro¬ thea,  Dorothy. dorado,  n.,  a  large  fish  of  the  genus  Coryphaena. —  Sp.,  prop.  pp.  of  dorar,  fr.  L.  deaurare ,  ‘to gild’,  fr.  de-  and  aurare ,  ‘to  gild’,  fr.  aurum, ‘gold’.  See  aureate  and  cp.  El  Dorado  and  dory, ‘a  seafish’. Dorcas  society,  meeting  of  ladies  to  make  gar¬ ments  for  the  poor.  —  From  Dorcas,  name  of  a woman  (mentioned  in  Acts  IX,  36-41).  The name  derives  from  Gk.  

NO HITS ^Margaret
--- KLN_1966.txt leaf 245; page-number candidates: ['447', '448']
 forth,  spreading  about’,  fr.  diffusus,  pp.  of  dif¬ fundere.  See  diffuse,  v.,  and  -ion. dig,  tr.  and  intr.  v.  —  ME.  diggen,  fr.  F.  diguer, ‘to  make  a  dike,  to  dam,  excavate;  to  spur  (a horse)’,  fr.  digue,  ‘dike,  dam’.  See  digue. Derivatives:  dig,  n.,  digg-er,  n.,  digg-ing,  n. digamist,  n.,  one  who  marries  for  the  second  time (in  contradistinction  to  bigamist,  which  denotes a  man  who  has  two  wives  or  a  woman  who  has two  husbands  at  the  same  time).  —  See  digamy and  -ist. digamma,  n.,  the  letter  F,  sixth  letter  of  the  ori¬ ginal  Greek  alphabet,  corresponding  to,  and pronounced  like,  the  Semitic  waw  (i.e.  

--- KLN_1966.txt leaf 256; page-number candidates: ['468', '469', '1?']
e,  also  dixy,  n.,  a  kind  of  mess  tin  (slang).  — Hind,  degcht,  ‘a  small  kettle’,  fr.  Pers.  degcha, dimin.  of  deg,  ‘pot’,  which  is  rel.  to  Pahlavi  deg, ‘pot’.  Arm.  dez,  ‘heap’,  and  to  OI.  dihmi,  'I smear,  anoint’,  fr.  I.-E.  base  *dheigh-,  *dhoigh-, *dhigh-,  ‘to  form  out  of  clay,  to  knead,  form’. See  dough  and  cp.  next  word, dizdar,  disdar,  n.,  the  warden  of  a  castle.  —  Pers. dizdar,  ‘holder  of  a  castle’,  fr.  diz,  ‘castle’,  and -dar,  ‘hol
```


### [2026-09-04T15:10:28.334Z] TOOL RESULT

```
Exit code 1
--- POK_01.txt leaf 255; page-number candidates: []
unkt;  Sache',  daigmti  ,keimen  machen'; WP.  I  832 f.,  WH.  I  495 f.,  865;  Trautmann  49 f. dheigh'   ,Lehm  kneten  und  damit  mauern  oder  bestreichen  (Mauer,  Wall- Töpferei;    dann   auch   von   anderweitigem   Bilden);    auch   vom  Tei». kneten  (Bäckerei)';  dhij-ii-io-s  , Former';   dheigho-s,  dhoigbo-s  ßa^ bilde,  Wall' ;  s.  zum  Sachlichen  Meringer  IF.  17,  147. Ai,  dBhmi  ,bestreiche,  verkitte'  (3.  Sg.  digdhi  statt  *dedhi),  ebenso  Partiz. digdhd-,  deha-  m.  n.  ,Körper',  dehi  f.  ,Wall,  Damm,  Aufwurf,   av.  pairi- daezayeiti  , mauert  ringsum'  (==  ai.  Kaus.    dehayati)   uzdiHa   3.  Sg.   Med. ,hat  (einen  Damm)  errichtet',  Partiz.  iiz-diUa-,  uz-daeza-  m.  ,AufhäufuDo' WalP,  pairi-daeza-  m.  ,Umfriedigung'  (daraus  gr.  nagadeiaog),  apers.  didä ,Festung'  (aus  *dizä-,  Wurzelnom.  auf  -a),  npers.  diz,  dez  ds.; arm.  dizanem  (Aor.  3.  Sg.  edez)  ,häufe  auf,  dizanim  ,häufe  mich  auf, dez  ,Haufe'; thrak.  -di^ogj  -di^cc  ,Burg'  (:  apers.  didä  oder  *dhigh-{a)-  auch  ös^iov, ON  Jei^ag,  Burto-dexion,  Burtu-dizos,  Jiyyiov  (:  lat.  fi'ngö)]  pannon.  VN An-dizetes  ,Burgan wohner' ; gr.  reXxoq  n.,  rotxoq  m.  (formell  =  ai.  deha-)  ,Mauer,  Wand';  ^lyydvw, Aor.  d-iysTv  ,mit  der  Hand  berühren'  (Bed.  wie  lat.  fingere  auch  ,streichelnd betasten'.   Media  g  bereits  ursprachlich  aus  der  nasalierten  Präsensform); lat.  fingö,  -ere,  finad,  fictum  ,eine  Masse  gestalten,  bilden,  formen;  er- dichten; streichelnd  betasten',  /^wZws  , Töpfer'  (:  germ.  *dizidaz),  filum {*figslom)  , Gestalt',  effigies  ,(plastisches)  Abbild',  figüra  ,Bildung,  Gestalt, Figur',  fictiö  ,das  Bilden,  Formen;  Bildung,  Gestaltung,  Erdichtung*, fictilis]  ,aus  Ton  gebildet,  irden,  tönern'  (zum  lat.  g  statt  h  s.  Leumana Lat.  Gr.  133;  nach  letzterem  stammt  aus  Formen  wie  fictus  auch  das  Ä  von altfalisk.  fifiked  ,finxit',  osk.  fifikus  etwa  ,du

--- POK_01.txt leaf 256; page-number candidates: ['245']
libum',  lat.  fltilla  ,Opferbrei, Opfermus'  (mit  dial.  t  aus  et))  osk.  feihüss  ,muros'  (*dheigho-)] ■% 245 •-   yi^^j.  Xi^i.filum  (identisch  mit  filum  ,Faden'?)  vgl.  WH.  I  497,  anderer- es EM-'  360; -iV    dlgen   ;fest^   (,*festo-eknetet,   kompakt');    air.  *kom-uks-ding-  ^bauen, ichten'  in  1.  Sg.  cunutgim,    3.  Sg.  conutuinc  usw.    und   vielleicht   auch „      ,.     -^  for-ding  ^unterdrückt^,  s.  unter  1.  dhengh- , drücken,  bedecken^  usw.; i'         ^^^  pamma  digandin  ,dem  Knetenden^,  kasa  digana  ,Tongefäße^,  gadigis 1  Konjektur   für   gadikis   ,rrld(T(.ia,    Gebilde',    es-St.,  ähnlich   Tetxog)]    daigs m.    Teig^  (*dhoighos),  anord.  deig  (n.),  ags.  däg^  ahd.  teig  ds.;  anord.  cZi^r dick,   wohlbeleibt'   (Bed.    wie    ir.  digen),    got.   (ii^rei    .Dichtheit,    Menge', inhd.   ^^V^^^   %ere  Adv.   ,völlig',   norw.  mdartl.  digna  ,dick  werden',  diga dicke,  weiche  Masse'  neben  mnd.  norw.  dlger;  ahd.  ^e^^aZ,  anord.  digull ■:■     '^chmelztopf,  Tiegel'  scheint  ein  echt  germ.  Wort  (*diz  . .  laz)  zu  sein,  das ^'    aber  in  der  Bed.  das  lat.  tegula  (aus  Trjyavov)  aufgesogen  hat; lit.    diezti,    dyzti    , schinden,    auspeitschen'    (,*durchkneten,    einem    eine beruuterschmieren'),  lett.  diezet  ,aufschwatzen,  anbieten'   (,*anschmieren'); ^       aruss.  deza,  klr.  diza  usw.  ,Teigmulde,  Backdose'  (*dhoigh'i-ä]  Berneker ^''    198    Mühlenbach-Endzelin  I  487). Eine  umgestellte  Form   {*gheidh-)  ist  wahrscheinlich  lit.  ziedziüj  ziesti formen',   alit.   puod-Bidys  , Töpfer',   aksl.  zizdg,   zhdati   ,bauen',   zhd^J   zidz , Mauer,  W^and'  (Büga  Kalba  ir  s.  184 f.); toch.  A  tseke  ?i  peke  si  ,i]güra  sive  pictura'  (W.  Schulze  Kl.  Sehr.  257  f., idg.  *dhoighos). Eine  Parallelwz.  *dheig-  sucht  Wood  Mod.  Phil.  4,  490  f.  in  mhd.  flehen jSchaffen  usw.';  ags.  diht{i)an  ,dictare',   ahd.  tihtön  ,erfinden  und  schaffen; dichten'  stammen  aus  spätlat.  dlctäre. \yP.  I  833  f.,  WH.  I  501  f.  507. /.  dhel-,  dholo-  , Wölbung'  und  ,  Höhlung'  (aus  , Biegung'). Gr.  d'öXog  f.  , Kuppel,  Kuppeldach,  rundes  Gebäude  (Schwitzbad)';  sizil. &oUa,  lak.  (Hes.)  aalia  , runder  Sommerhut',  d-älaiiog  m.  ,im  Inneren  des Hauses  gelegenes  Gemach,  Schlafzimmer,  Vorratskammer',  d'aldf.irj  , Höhle, Lager  von  Tieren',  d^-i9-ßAi/dg  ,Auge'  (*d7ra-'d-aX^6g  ,* Augenhöhle'); cymr

(eval):1: ===== not found
```


## [2026-09-04T15:10:28.989Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; $LF KNT.txt grep 'did[àā]- sb' 1 --chars 700; echo =====; $LF SYN.txt leaf 942 --chars 600; $LF SYN.txt grep 'raoδ|raoda|raod-' 3 --chars 1200; echo =====; $LF SOD_pages.txt leaf 217 --chars 2500; echo ====; $LF SOD_pages.txt leaf 410 --chars 2500",
 "description": "Read Kent didā, Buck p.874, Sogdian leaves 217 and 410"
}
```


### [2026-09-04T15:10:30.960Z] TOOL RESULT

```
Exit code 1
--- KNT.txt leaf 214; page-number candidates: ['191']
845); hardly vasnd-[dily XPg 7f (despite Lg. 9.320; see under apiy); 7‘va-diy A’Sd 3 (JAOS 51.229). didà- sb. ‘wall, stronghold, fortress’: N Pers. diz, pIE *dhióhà-, cf. Skt. dehi- ‘wall’, Gk. réxos, 191 NEng. dike, ditch (676.011, 588, §148.IV, 5166). Cf. also paradayadàm. й nsf. DB 1.58; 2.39, 44; 3.61, 72; DSe 46; DSf 42. didäm asf. DB 2.78; DSe 48°; DSf 54. dipi- sb. ‘inscription’: Elam. tup-pi, Akk. duppu (5152.1): borrowed from Sumerian dup- (Ву. Gr. §282; hardly contamination of Jran. *ripi- = Skt. lipi- ‘smearing, writing’, with Sum. dup-, as taken by Pisani, Riv. Stud. Or. 14.320, as Skt. lipi- ‘writing’ indicates writing with ink rather than engraving on stone) 4:4] nsf. DB 4.90, 91f. dzpim asf. DB 4.42, 48, 70, 73, 77, 89; XV 22, 24. dipiyd lsf. (§179.V) DB 447. dug- vb., see hadugá-. 

(eval):1: ==== not found
```


## [2026-09-04T15:10:34.996Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\npages=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\ndef clean(s): return re.sub('[‎‏‪-‮⁦-⁩]','',s)\nfor pat,lo,hi in [('دژ',300,318),('دیوار',368,382),('دیگ',362,378),('روییدن|رویید',395,410),('رستم',380,470),('رز\\\\b',380,470)]:\n    print('=====',pat)\n    n=0\n    for i in range(lo,hi):\n        p=clean(pages[i])\n        for m in re.finditer(pat,p):\n            line=p[max(0,m.start()-60):m.end()+200].replace('\\n',' | ')\n            # print only lines that look like headword position (near line start)\n            ls=p.rfind('\\n',0,m.start())\n            if m.start()-ls<25:\n                print('leaf',i,':',line[:260]); n+=1\n            if n>12: break\n        if n>12: break\nEOF",
 "description": "Locate Borhan vol 2 headwords dež, dīvār, dīg, rūyīdan, Rostam, raz with leaf numbers"
}
```


### [2026-09-04T15:10:36.897Z] TOOL RESULT

```
===== دژ
leaf 311 :                        = ۵بکر اول و سکون ثالی » قلمه |  بمعنی دژکام ات که زاهد ویرهیز کار )(٩ -                                    وحصارباشد - ۱وبمعلی زشت و,دوبدخوی وخشم | وخواجه‌سرا باشد ؛ وبفتح‌اول لز درست است.                                        نزد- |  
leaf 311 : ول  .رك :                   - ۴                اسشق داه“ . |  دژا کام۰         ۳۳ره :   o               ۰   دژکامه     ۰    درکام   ۰     امه |                                                                                 رك :دکژا             ۴              
leaf 311 :       ۴                وخشم معمور است . |  )      »مر کب از  :دژ( حرش                «مناس YT                   - ۷پهلوی sãkãhsud                                درکام  ۰درکامه ۰ |  |  |  |  |                      چو بل در آ گاه ودرنده شس.                      
leaf 311 : وزار دلیر |  دقیقی طوسی« .مزدیبنا 4۵۳-۵۵٩ . |                   دژ ( رکه :ج )  +آلود (لوآده) .                            ز: |                                                                              ۸ا_۵                    :د؟آ گاه ۰        رک       ۷ |  
leaf 312 : ( =             ۳ت          ۰    :دوا کا        ۱رکه |  |      ۴دژ آهنج ,از :حڑ ( = رش)  +آهنك  ,لغة بمعنی بدآهنك»                                    دژآ هنگ(ه.م ( .                 = |     » این‌کلمه که درلفت فرس اسدی چاپ تهران مکش دال باد گردیده ویمعذی مخوف 
leaf 312 : ۱۲ : ۱؛ دز (بضم‌اول .رك :ح۲ص‌قبل) بمنوان صفت بد |      - ۱رك :دژبراز .          ۰   از :دز ( = دش)  ۳براز (ھ.م > (.غه مف براز نده .رل  :دز درو                      _ ۵ |  |                                        .    ردو |                                      
leaf 313 :  اول و خای تقطه‌دار | امه = بکر اول؟ و فتح آخر »    دزک | بمعنی‌دژکام استکه سهمنالك -وخشمگین -وزاهد                                          وسکون ثانی وهیمء بدخوی وبدطبیمت راگویند |             و پرهیز گاروخواجه سرا باشد .                                     
leaf 313 : آمده است .                 دز خیم  = ۴بکراور ۴بروزن‌اقلیم» |  دژمان  - ۷بکسراول بروزن کرمان,                                                    پمعنی دژخمادت که بدخوی ودطبیعت وبدروی |        بمعتی افوس ودريغ داشتن وحسرت باشد .                                  
leaf 313 :                              بهم رسد - |  تون ودال جد ٩ بمعنی دژن است که چیزی‌نند                                          تاییدن رسمان وبا ابرم وامثاان بران افتد؛ |  وتبز طمم باشد  -ومردم قهرآ لود وخشمناك وتند                                        وبخر اول و
leaf 314 : ت را گوءنه  -وبه‌عنی‌نقاهت هم‌آمده ات |  | واف دیگر زده  ۰بمعنی دژهخت |                          مفتوح بنون ک                                                    که ازییهاری برخاستن باشد ۰ |                                                             =بفتح اوبل
leaf 314 :                                                 ۵ |       .   دژهوخت  .رك  :دژهشت     =      ۸              ورك :دزهر ج()۱               ۰    . ۴رك  ۳درهخت            » دزهوخت |  |      سا_نىكرىت |              °                      (ھ.م» (.رك  :صله دىداچة مو
===== دیوار
===== دیگ
leaf 372 :   رك :دز  .دژ ؛ آب دیز (=           ۴ |   معنی از باد کلمةٌ « دیگه » («.م ).د قاب اص  ۱۹۲ح» .قس :دیزیی ورك :                             ۴م-اين |   یابه ) |د بگدان  .دیگپابه ] ,ماز سرانی کنونی               س    (            طبری 0       ۶            دىزتدان .
leaf 372 : رك :                             ۴م-اين |   یابه ) |د بگدان  .دیگپابه ] ,ماز سرانی کنونی               س    (            طبری 0       ۶            دىزتدان . |                                                     ر= |                                 ان) « راژه ن
leaf 374 : و کشمش وبادام وفلفل ودارچینی وقرلفل وزبره | کوسفندان وکاوان و دیگر چاریابان در آنجا          ومانندآن ویعربی تابل خوانند وجمع‌آن توّابل |                                      باشند .             است  -ودنگه بزر که را نگیفزته‌اند . |  |  دیلم = با اول بتحتالی م
leaf 374 :                                #دضاقوس  رك :دیشافوی () |     #دیگر  -بکسر اولوفتح سوم» پهلوی lj_arak :1۱26101 _ « ayîtivd#اسفا»۱ |     ۹۸ ۱و ۷0-درکلمه  ل  ,پازند  7381021فارسی دیک .قس  :پهلوی انل دریبکه |    ۷ورك :اسشق وهوشمانه . ۹۵مخفف آن «دکر» (ه.م ).؛ کلمه‌
leaf 375 :  بعربی رتبلا خوانند  -و بفتح ثالث صفیردیلم |  دیمر * س بر وزن دیگر > بمعنی دم                                                                                           ام |       باشد ویعربی خد گوبند .               است که رخاره |                              
===== روییدن|رویید
===== رستم
leaf 434 :                                  فته اند . |  ۸ے معروف‌است که رستم زال                       رسوتم |                                                                     روساختی کنابه از شرمنده شدن |                                                              
leaf 460 : وهه کلوله کرده باشنف ۱         کمان |  |  موی باشد * -۷ونام پدر رستم نیز هت وچون                   اقه د بروزن دافه  .خاریشت رگاوند |  او سفید موی بوجود آمد باين نام خوانند ۱۷                 ون جانوری است  -و بمعنی گیاهی نیز هست |                             
===== رز\b
leaf 393 :   رارز                                                                                            - ۳۳ |  |      هم بنظرآمده است که بروزن فلولا باشد .                 رانج! = بفتح لون وسکون جيم » به | راوش؟ ه بفت
leaf 404 : را در رز درخت انجیر بود و هیآ مد از آن درخت میوه |            رز با مو            میخواست ولمی بافت برزبانان گفت :سه سالت می آیم وازین |                 درخت افجیر میوه میخواهم وئمي‌بايم » او رراکبنید « »...الجیل فارسی ص .*۸۲۱ |                                
leaf 405 :                                                 ٩ |    * از  :رز            وید دوم) برنج ( منتهی الارب ) ۰ |                                                        اتولشد               م |                                                                       
leaf 406 :                                       ( )۱چك :رزد () |   از  :رز (ه.م٣ ) . يدن    -    ۳             امروز « چفته ورزه » مستعمل است .   - ۱ |  |                      ۴ماخون از (عی) «ناطمالاطبا» رك :حاشية : 4               (پونه مصدری) . |          چون عهد ٽو ل
leaf 440 : ر و مهم فرمودن بمردم بی ماحصل ر مهمل | کرمی است که بر آن روغن رز ند ودیگری را                                                         وضایم باشد ۰ | بر بالای آن گذارندوهمجنین تاچندانکه باشد. |                                                            روغی خود
```


## [2026-09-04T15:10:40.241Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\npages=open('FSF_pages.txt',encoding='utf-8').read().split('\\f')\nn=0\nfor i,p in enumerate(pages):\n    for m in re.finditer(r'(^|\\n)\\s*رَ?ز\\s',p):\n        print('leaf',i,':',p[m.start():m.start()+500].replace('\\n',' | ')); n+=1; break\n    if n>6: break\nprint('---- pages with both رز and انگور')\nfor i,p in enumerate(pages):\n    if 'انگور' in p and re.search(r'\\bرز\\b',p) : print(i, end=' ')\nEOF\necho; echo \"=== AFM leaves\"; python3 - <<'EOF'\npages=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(pages):\n    for key in ['الرونق','الروضة','( الروضة','(الروضة']:\n        if key in p:\n            j=p.find(key); print('leaf',i,key,':',p[max(0,j-100):j+700].replace('\\n',' | ')); print()\nEOF",
 "description": "Locate raz in Noushin glossary and rawnaq/rawda leaves in Addi Shir"
}
```


## [2026-09-04T15:10:43.241Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; echo \"=== FSD vol3 mat\"; $LF FSD_vol3.txt grep '^mat[,\\s]|^mat\\s*\\(' 3 --chars 900; echo \"=== FSD vol3 mattus\"; $LF FSD_vol3.txt grep 'mattus' 2 --chars 400; echo \"=== FSD vol1 checkmate\"; $LF FSD_vol1.txt grep '^check-?mate' 2 --chars 900; echo \"=== FSD vol1 leaf ~575 numbers\"; $LF FSD_vol1.txt leaf 575 --chars 300",
 "description": "Grep Funk and Wagnalls for mat, mattus, checkmate"
}
```


### [2026-09-04T15:10:43.359Z] TOOL RESULT

```
---- pages with both رز and انگور
265 463 
=== AFM leaves
leaf 76 الروضة : وز اي يوم ومن نامه اي كتاب | , 7 ( قير بالرجل يقال انه « رَوْس سو » اي رجل سو وهو معرب عن | 9( 30900 | + (الروضة ) من الرمل والعشب مستتقع الا تكو النضنت مز القز به 11 | وفي الكلمات الروضة ® 1 ٠‏ في !ܐܕܩ ܐܨ 03 عن ديز وهي ܬ الاء في | الإوناء وهي ܨ ܘܐ من يدك اي صب أخذتها العرب وتصرفت با وق 1 | ( رهي ܩܣܥ 03111 09 $ «الودعة وا ونيا خا 5 اي | صب اللبن على اللإن وروي فنقع بالري ٠‏ ٠وَأْرَاضَ‏ الوادي اي استنقع فيه الماء واستراض | الحوض الى غير ذلك | (الروط) معرب رُود وهو الثهر والفارسي” مأخوذ من الأرائي ܪܕܢܐ وهو | 3 من ܪܕܐ أي جرى وسال و .شر به اليونالي 200001 | ( الرَاووق) المصفاة ܢܵܡ ܙܝ راوك وهو ما صْفًا من الخمر والماء وغيرتها ٠‏ وقالوا فيه | راق وروق الى غير ذلك ( فرتكل ص: ١506‏ ) | ( لاروك ) ( 360 زهو الشدة | * (الريغ) 00 ريك ونمو 11 | 4ق 380 | ديهاً ») جاء وذكسَ 3 من راه ومعناه الطريق ٠‏ ومنت | ܥ | ܟ:

leaf 76 (الروضة : روز اي يوم ومن نامه اي كتاب | , 7 ( قير بالرجل يقال انه « رَوْس سو » اي رجل سو وهو معرب عن | 9( 30900 | + (الروضة ) من الرمل والعشب مستتقع الا تكو النضنت مز القز به 11 | وفي الكلمات الروضة ® 1 ٠‏ في !ܐܕܩ ܐܨ 03 عن ديز وهي ܬ الاء في | الإوناء وهي ܨ ܘܐ من يدك اي صب أخذتها العرب وتصرفت با وق 1 | ( رهي ܩܣܥ 03111 09 $ «الودعة وا ونيا خا 5 اي | صب اللبن على اللإن وروي فنقع بالري ٠‏ ٠وَأْرَاضَ‏ الوادي اي استنقع فيه الماء واستراض | الحوض الى غير ذلك | (الروط) معرب رُود وهو الثهر والفارسي” مأخوذ من الأرائي ܪܕܢܐ وهو | 3 من ܪܕܐ أي جرى وسال و .شر به اليونالي 200001 | ( الرَاووق) المصفاة ܢܵܡ ܙܝ راوك وهو ما صْفًا من الخمر والماء وغيرتها ٠‏ وقالوا فيه | راق وروق الى غير ذلك ( فرتكل ص: ١506‏ ) | ( لاروك ) ( 360 زهو الشدة | * (الريغ) 00 ريك ونمو 11 | 4ق 380 | ديهاً ») جاء وذكسَ 3 من راه ومعناه الطريق ٠‏ ومنت | ܥ | ܟ:

leaf 153 الرونق : ي طقس © يان الشرقيين الأحد 0 | فم الس ليم ١‏ | ( النرْق) اليد ( شفاء الغذيل ) ٠‏ معرب نزخ وهعناه السعد والرونق | ١‏ النارَمْسْك ) ܙܘ ضغيرة مفتحة كأنها وردّة لونها الى الساض ‹1 ܠܟܕ والضترة | في ذسطها نوار لونة كذالك وطعمة نض وراتة طيية ومعناها بالفارسيّة هسك | ا زهان | ( | ܕ ) اللين ܐܐܬܐ ܩܢ مريب ܝܝ هُ الكردي زم | ܨ ܟܝܢ هن اللسمون معرب نارناك واصل معناة 3 ر اللون ܀ وفتة ܘ | ܫܫ 3 0 | + ( ×« © 815 تصن ين لزه | ١‏ 363 ܝ القصيد تعريب يزه والتيزق لغة فيه ومنة فعل ترك اي طعن | بالنيرك ٠‏ ومنه الاراعي. ܨ = | + ( الشيسب) ܐܟܟ بق ن الواضح الستقيم او ما وجد 7 الطريق ܥܕ !$
```


### [2026-09-04T15:10:46.215Z] TOOL RESULT

```
=== FSD vol3 mat
--- FSD_vol3.txt leaf 51; page-number candidates: ['1?', '1?', '1?', '11?', '1?', '9?']
 gymnastic exercise of * *• the muscles f the abdomen -charing -mat*, n Hame os 1 ymiftJLrA' n a .i MAT, 3 Chinese mat. a package In which cassia-bark of ■*Sictorh»g t^«woVhi?u\^ol^^ Bpahi ^ Inferior quality Is marketed -rorif mat {Naut}, a fend- V 1 iiiRt'^ fl a er filled with cork waste mat'-biMit*, n A large flat- n ■ ' “ ’ " --*• ^ borough bout ronslHtlng of a platform siiptsiried on scows, used for j 3 HtM.OMuZ poisonous julcoH Hen Ulus iindnr manpk uiat'd-rn, 2 niAt'a-ra, n. [Ar ] A leathern -W 411 , n J 3. A township of Munmoiith Co , the making and siriklog of brush mats along river-banks, , I i # « -r,. etc , In the making of n-vetmenis - mat-braid, n A thick, ***••?•* • M . , . * F®** '^•*'** coarsulv woven trimming or binding, os for hea\ y gurinenta 1 aiioiner, or wi put coarsely woven trimming or binding, os for hea\ y gurinenU — mat -grass, n licacb-grass - mat -hook, n 1. A book used In drawing plcf’cw or strips of rags through a linen groundwork, lii making drawn mats or ru

--- FSD_vol3.txt leaf 54; page-number candidates: ['1?', '39?', '1?', '1?', '11?', '18?', '8?', '1?']
n or other underground place for storing groin I < F matamore, c Ar.mefmur.oavem for storing corn 1 Mat 'tan, 1 mat'sn; 2 mftt'an, n. Bib e Chron. xxlli, 17 ^ rileb . gift 1 [IK-lft (Heb , gift 1 Mat'ta**nah, 1 mat's-ns; 2 m&t'a-na, n. Bib Num xxl. Mat^ta^nl'sh, 1 mat'e-nol's; 2 mkfarnl'a, n. Bib. M Kings xxlv. 17 (Heb., gift of Jab ] Mat^ta-po-nl', 1 mafs-po-nal'; 2 m&t*a-po-nl', n. A river of Virginia, length. 125 ro to York river at West Point Mat'ta-thah, 1 mat'o-Ois. 2 m&t'a-tha, n Bib Ezra x, 33. Mat^ta-thl'se, 1 mut'a-fhai'iwi. 2 mfit’a-thrae, n. Bib. (AiMicrypha) 1 7;«d lx. 43 (x, 33 Martat-toh,lmat'»-ts.8m&t'a-ta,n. Bib. (R.V.) Ezra matto, 1 mat, 2 mfit, n. [F 1 1. Metal An impure metallic product contaming sulfur: obtained ui tlie smelt- ing of the Bulfids of diffenmt metals, especially copper. 2. Bame as mat*, n.. 1 mattt. Mat''te-a-wan', 1 mat*i-s-won'; 2 m&t*e-a-wan', n A vil- lage In Dutchess county. N Y . where are the Utate Hospital for the Criminal Insane and tlie Highland

--- FSD_vol3.txt leaf 55; page-number candidates: ['1?', '1?', '1805?', '31?', '24?', '1?', '1?', '1?']
al-the'an, 1 mo-fhi'an 8 niA-tht^'an, a Uelutliig to or oharaetortsUe of St. Matthew or his Gospel. Mat 'tlip-las, 1 mat'Clu-ias or inat-thries, 2 mkl the-los or m&t-the'las, ft. Bib. (Apocrypha) i Ead lx. 11) Mat'ttaew, i mafh'lll. 2 in&th'O, Sir Toble (»Vil677-w/ii 1655). AD Kngllsb diplomat and scholar; friend of liacuii, translated Bacon's Easaya Into Italian Mnt'tbew, 1 ma£h'yu, 2 m&lb'yu, n. 1. Amasculino personal name. Dan. Mat-th»'U8, 1 ma-t6'us. 2 md- of Simplified Spelling Board, Motlire, Mta Ufe and HU H ork 2. SUuley (t/tt 1 824-»/t,iH8D), an American Jurist; JwtiTO of the Bupremo Court, 1881. MaUthl'as, l ma-thal'as; 2 mA-thFas, a. 1. A masculine eSnwnal name D Mat-thUs', 1 mo-toir. 8 mA-tls’. F. Mat'^thras', 1 mo-u-ar, 8nt&*tl*a8'. o Ma-thras, 1 ma- tras. 8 mk-tl'as; It. Mai-tl'a, 1 mot-tra, 8 mUt-tril; L. Mat-thras; Bp. Ma-tras, 1 mo-tl'DS. 2 mkptl'ils. 3. The .... .... disciple chosen to take the place of Judas Iscariot among the Mat^*rln, ImaCh'u-lormarj u-]rln. 2 mich'u*f

=== FSD vol3 mattus
--- FSD_vol3.txt leaf 51; page-number candidates: ['1?', '1?', '1?', '11?', '1?', '9?']
ts) of the West mas'lio-don, 1 rnus'to-don, 2 iiifts'tti-dAii, ti 1. An ex- ( (* matt, dim < I 2 I. mattus, see juatb^, » J *>**!«. #*?*•«**** “*****? tinct elephant, having the nmlar ercsls mammilliform « Same os mate JSIV.,,b?by cmalfi Afrlwin ! Vibe?' or mpple-shat>ed with the cement in the inter\enii)g n®*** a 1. An article woven from filler, rushes, wire. inat*a-hu'ra?« ^ ttid Hame as mataciouv valleys atrophied, a inasl^outiiie »Some of the species mgs. rope, etc , or knotUnl mii»t*^lun^ ^ j,,,.

=== FSD vol1 checkmate
NO HITS ^check-?mate
=== FSD vol1 leaf ~575 numbers
--- FSD_vol1.txt leaf 575 / 798; page-number candidates: []
ital must  not  coerce  labor.
II.  t.  To  use  coercive  measures,  as  in  government;  as, the  liberals  coerce  as  well  as  the  conservatives,  f   <   L. cocrceo  <   co-  (<  cum),  together,  +   arceo,  press.]  Synj  see compel.—  co-erc'er,  n.—  co-erc"I-bll'I-ty,  n   —   co-erc'i-
```


## [2026-09-04T15:10:46.240Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; echo \"=== PHN 257\"; $LF PHN.txt leaf 288 --chars 3000; echo \"=== DEV 159\"; $LF DEV.txt leaf 189 --chars 3000; echo \"=== LKT 115\"; $LF LKT.txt leaf 141 --chars 3000; echo \"=== SKT 163\"; $LF SKT.txt grep '^EMERALD' 1 --chars 500",
 "description": "Read Pihan p.257, Devic p.159, Lokotsch p.115, Skeat emerald"
}
```


### [2026-09-04T15:10:48.748Z] TOOL RESULT

```
=== PHN 257
--- PHN.txt leaf 288 / 438; page-number candidates: ['257?', '9?']
MAT * 257
conclu sur les bords de la Tafna en 1887; mais, l'émir ayant
rompu le traité en iSSg, la ville de Mascarat fut occupée de
nouveau par nos troupes en 1 84 1 . On trouve souvent Mascara
écrit sans t à la lin; cependant il est plus régulier de conserver
cette lettre, comme en arabe.
MASSER, V. a, (a,)
j«w» [mass] manier, toucher, palper. — L'opération du massage
ou massement, très-usitée chez les peuples orientaux , consiste à
presser avec la main les diverses parties du corps , pour donner
plus de souplesse aux articulations et aux tissus. Pratiqué sur-
tout à la suite d'un bain, le massage excite chez la personne
qui le subit un sentiment général de bien-être et de plaisir. —
Comparez avec l'arabe le verbe grec fida'CTetv dont le sens est
le même.
MAT, adj. m. (p.)
c»U [mât] défait, réduit à Vextrémité. — Faire mat ou mater veut
dire, au jeu d'échecs, mettre le roi dans l'impossibilité de changer
9 *
déplace, ce qui termine la partie. Voyez Echec. — Par exten-
sion, le verbe mateb s'emploie aussi au figuré, dans le sens de
dompter, humilier, affaiblir, abattre, comme dans les phrases sui-
vantes : mater V orgueil de quelqu'un, mater son corps par les jeûnes
et les austérités. Ce verbe alors a pour participe passé maté, k,
abattu, réprimé, dompté.
MATAMORE, s. f. (a.)
ijy^ia^ \maimjoûrat\ caveau, nom de lieu dérivé de^^^^ [t^amar]
cacher sous terre. Cellier souterrain , silo dans lequel les Maures
=== DEV 159
--- DEV.txt leaf 189 / 326; page-number candidates: ['156?']
synonyme  rngiiahiJ,  qiii  représente  J=wi^^  ra- iva/jil .  plur.  de  <\X:i^î^  rahila,  monture.
Mahométan.  Rienzi,  le  voyageur  géographe,  veut  qu'on
dise  mohmnmédan,  le  nom  du  Prophète  étant  *x^  moham- mc(J ,  le  loué,  et  non  Mahomet.
Mahoisne.  Sorte  de  galère  turque.  Esp.  mahona.  D'après Mûller,  c'est  l'arabe  (j^U  maoïin,  vase.  MaoUu  signifie  en effet  vase,  marmite,  pot,  et  en  général  tous  les  ustensiles d'une  maison,  et  bien  d'autres  choses  encore.  M.  Dozy,  à quij'emprunte  cette  étymologie\  ne  dit  pas  sur  quelle  base s'appuie  l'auteur  pour  passer  de  là  à  la  galère  turque.
Maimon.  Singe  du  genre  des  macaques.  C'est  le  persan j^-içy»  maimoûn,  même  sens,  qu'il  ne  faut  pas  confondre avec  son  homonyme  arabe  qui  signifie  heureux ,  comme  l'a fait  assez  étourdiment  l'auteur  du  catalogue  des  manus- crits malais  de  la  Bibliothèque  nationale;  un  de  ces  ma^ nuscrits  porte  en  effet  le  titre  de  ^j^4î>^  ^>*"  khodja  mai- moûn, que  le  catalogue  traduit  maître  singe.  Si  l'auteur  de cette  interprétation  avait  parcouru  seulement  le  début  du conte,  il  aurait  compris  qu'un  père,  joyeux  de  la  nais- sance de  son  premier-né,  ne  le  gratifie  pas  du  nom  de maître  smge.
'  Gloss.  p.  299.
156  DICTIONNAIRE  ÉTYMOLOGIQUE  î
Mainate.  Genre  d'oiseaux  de  l'archipel  Indien.  Une  des espèces  porte  le  nom  de  mino  ou  maïnou.  Ces  mots  sont assurément  malais.  Mais  Marsden  ne  donne  que  U-y»  ml- 7ia,  et  le  Dictionnaire  de  l'abbé  Favre  rattache  ce  mot, qu'il  écrit  sans  î  a  final,  à  l'hindoustani  maïna.
Mamelouk.  Esp.  et  portug.  mameluco,  ital.  mammalucco. De  l'arabe  ^à^  mamloûk ,  esclave,  participe  passif  du  verbe dix*  mcdak,  posséder.
Malamoqu
=== LKT 115
--- LKT.txt leaf 141 / 278; page-number candidates: ['8', '114']
wolle, Kleinbaumwoile"  bezeichnet werden;  vgl.  Hugo  Grothe,  Auf  tk.  Erde. Reisebilder  und  Studien.  ^  Berlin  1903. S.  380,  wo  sich  auch  eine  Schilderung der  Gewinnung  des  Meerschaums  findet: S.  277/281.  Ferner  vgl.  Joseph  Grunze), Die  wirtschaftlichen  Verhältnisse  Klein- asiens. Wien  1897.  S.  34/44;  Dernburg, Auf  dtsch.  Bahn  in  Kleinasien.  Berlin 1892.  S.  51  ff.  „Die  Sladt  des  Meer- schaums*. —  Der  Kuriosität  halber  sei noch  die  Etymologie :  dtsch.  Meerschaum <  ar.  morsüm  [soll  heißen  marsüm] 'gesiegelt'  erwähnt,  s.  J.  G.  Kochs, Vergleichungen  mineralogischer  Benen- nungen des  Deutschen  mit  arabischen Wörtern.  Leipzig  1795.  S.40.  [Kluge  304. Devic  DEt  2.Ö/26.    Lammens  Rem  18.
1417.  Hebr.  Maria:
Eigentlich  Mirjam  und  Marjam  'Die Bittere'  oder  'ßittermeer';  hieraus  über die  Koseform  Marion  frz.  marionnette, it.  marionetta  eigentlich  'Mariechen', dann  'Püppchen',  ursprünglich  wohl  die Bezeichnung  des  mit  einem  Puppen- kopf geschmückten  Narrenzepters,  dazu frz.  marotte  'Spielzeug,  Steckenpferd, Narrheit'.  —  Sp.  mariquita,  kat.  viari- etta,  dtsch.   Marienkä/er.    Sp,  marica
Lokotsch,  Etymolog.  Wörlerbuch.
'Elster;  Mannweib'.  —  Aus  Maria*  posa 'Maria,  setze  dich'  wurde  kat.  sp.  pg. mariposa  'Schmetterling'  [mit  einer Volksetymologie,  die  auch  in  germ. Sprac  hen  ähnlich  vorkommt,  vgl.  Ro- mania  V,  180].
1418.  Ar.  ina'rif.a:
'Wissen,  Kunst',  ebenso  tk.  marifd; hieraus  rum.  tnarafet  'Vermittlung, Kunstkniff'.
1419.  Ar.  inarih:
'Vergnügt';  hieraus  siz.  mmaria  'Witz'.
1420.  Ar.  uiarkab:
'Jede  Art  von  Fahrzeugen,  Sattel';  hier- aus entstand  als  passende  Bezeichnung für  den  Stern  a  Pegasi  der  Name  Mar- kab.    [Ideler  Sternn  117.
1421.  Ar.  markät:
'Stufe,  Treppe';  hieraus  mit  sp.  Aug- mentativsuftix  malecön  'Flußdamm',  eine Anzahl  erhöhter  Stuten,  um  die  Stadt vor  Überscliwemmungen  durch  den  Fluß zu  schützen,  bes.  in  Sevilla  am  Ufer  des Guadalquivir.   [DE  299.    Eguilaz  442.
1422.  Sskr.  inarkata:
'Affe';  hieraus  vielleicht  dtsch.  Meer- katze, Cercopithecus  [als  ob  das  Tier  zu uns  über  das  Meer  gekommen  wäre;  wie die  Katze  hat  es  einen  langen  Schwanz; vergleicht  man  daneben  aber  dtsch. Meerkalb,  Meerschweinchen  sowie  die älteren  Formen  ahd.  merikazza,  mnd. merkatte,  so  scheint  die  Etymologie  doch recht  zweifelhaft].  [MWiD  25/26.  Ander- sen DVEt  6.
1423.  Ar.  markaz: 'Mittelpunkt',  ebenso  tk.  merkez;  hieraus lum.  merchez  'Schliche,  schwache  Seite' [nach  Löbel  E1TAP63  auch 'Mittelpunkt'].
1424.  Ar.  inartiiara:
'Zornig  sein';  hieraus  nach  GrSVoci 240  siz.  marmaruca  'Zorn,  Ärger'.
1425.  Tk.  marpyc:
[Aus  pers.  märpüs  aus  mär  'Schlange' Horn  NpEt  S.  219,  Nr.  977  und  püs,  s. hier  Nr.  162.Ö]  'Das  Holzrohr  oder  der lange  gewundene  Lederschlauch',  durch den  man  den  abgekühl
=== SKT 163
--- SKT.txt leaf 156; page-number candidates: []
.E.  menden,  short for  M.  £.  am^nden,  to  amend,  by  loss  of  a: &ce  ameod  (above). Emerald,  a  green  gem.  (F.  —  L.  — Gk.) M.E.  emeraude  —  O-  F.  esmeraude,  —  L. sviara^um^  ace.  of  smansgdm.^GV.  afii' payiios,  an  emerald.  Cf.  Skt.  marakata (the  same>. smaragduB.  (L.  —  Gk.)  \*,smara^dm (nbove). Emerge ;  sec  Merge. Emeroda;  see  Hemorrhoids. Emery,  a  hard  minemi.  (F  — Itol.  — Gk) Formerly  emfril:  XVU  cent.  -  O.  F. cmeril^  tsmetil.  —  Ital.  smeri^li^.  *  Gk, <fMVP*^>  fft^^piXp  emery.  — Gk.  vftaw,  I  rub. S^eCio.  (L— Gk.)  L.  rmr/fV»r. -
```


## [2026-09-04T15:10:51.505Z] TOOL CALL #39: Bash

```json
{
 "command": "for w in کروبی زمرد پالیز روضه رونق روستا حور موت مات ماتادور; do p=$(python3 tools/fetch_source.py \"https://vajehyab.com/?q=$w&d=moein\" --note \"ref check MON (Mo'in) for $w, pages 101/126/311/345\"); echo \"##### $w -> $p\"; grep -i -m1 'status\\|title' \"$p\" | head -2; python3 - \"$p\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8').read()\ni=t.find('فرهنگ فارسی معین')\nif i<0: i=t.find('معین')\nprint(len(t),'chars; excerpt:'); print(t[i:i+900] if i>=0 else t[:900])\nEOF\ndone",
 "description": "Archive and read vajehyab Mo'in entries for ten words"
}
```


## [2026-09-04T15:10:54.162Z] TOOL CALL #40: Bash

```json
{
 "command": "for w in cherub griffin emerald paradise matte checkmate margarite matador; do p=$(python3 tools/fetch_source.py \"https://ahdictionary.com/word/search.html?q=$w\" --note \"ref check AHD dictionary entry $w (Nourai AHD page cites), pages 101/126/345\"); echo \"##### $w -> $p\"; python3 - \"$p\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8').read()\ni=t.find('Etymology'); \nif i<0: i=t.find('[')\nprint(len(t),'chars; excerpt:'); print(t[max(0,i-300):i+700] if i>=0 else t[:800])\nEOF\ndone",
 "description": "Archive and read AHD online entries"
}
```


### [2026-09-04T15:10:58.009Z] TOOL RESULT

```
##### کروبی -> /home/sfmqrb/git/rishe/data/verification/sources/web/e0e0cfa443ab207a.txt
STATUS: 200
1445 chars; excerpt:
معین
 (کَ یّ) [ ع . ] (اِ.) فرشتة مقرب درگاه . ج . کروبیون .

 جست‌وجوی مشابه

 کروبیان
 فرهنگ انتشارات معین
 (کَ یّ) [ ع . ] (اِ.) کروبی . فرشتگان مقرب درگاه .

 کروبیون
 فرهنگ انتشارات معین
 (کَ یُّ) [ ع . ] (اِ.) جِ کروبی . فرشتگان مقرب درگاه .

 کروب
 فرهنگ انتشارات معین
 (کُ) [ ع . ] جِ کرب .

 کروکی
 فرهنگ انتشارات معین
 (کُ) [ فر. ] (اِ.) نقشه ای که موقعیت محلی را نشان دهد.

 کروی
 فرهنگ انتشارات معین
 (کُ رَ) [ ع . ] (ص .) منسوب به کره ، هر چیز گرد و کره مانند.

 جست‌وجوی متن

 کروبیان
 فرهنگ انتشارات معین
 (کَ یّ) [ ع . ] (اِ.) کروبی . فرشتگان مقرب درگاه .

 کروبیون
 فرهنگ انتشارات معین
 (کَ یُّ) [ ع . ] (اِ.) جِ کروبی . فرشتگان مقرب درگاه .

 نارنگی
 فرهنگ انتشارات معین
 ( ر )(اِ.) درخت است پایا از تیرة مرکبات با میوة کروی و معطر.

 قوری
 فرهنگ انتشارات معین
 (اِ.) ظرفی کوچک ، کمابیش استوانه یا کروی برای دم کردن چای .

 گردو
 فرهنگ انتشارات معین
 (گِ) (اِ.) تیره ای از گیاهان دو
##### زمرد -> /home/sfmqrb/git/rishe/data/verification/sources/web/401f0aca2461c0b2.txt
STATUS: 200
921 chars; excerpt:
معین
 (زُ مُ رُّ) [ معر - یو. ] (اِ.) یکی از سنگ های قیمتی به رنگ سبز که در جواهرسازی به کار می رود.

 زمردین
 فرهنگ انتشارات معین
 (زُ مُ رُّ) [ معر - فا. ] (ص نسب .)منسوب به زمرد، زمردی ، ساخته شده از زمرد.

 جست‌وجوی متن

 زمردین
 فرهنگ انتشارات معین
 (زُ مُ رُّ) [ معر - فا. ] (ص نسب .)منسوب به زمرد، زمردی ، ساخته شده از زمرد.

 جواهر
 فرهنگ انتشارات معین
 (جَ هِ) [ ع . ] (اِ.) 1 - جِ جوهر؛ گوهران . 2 - هر یک از سنگ های گرانبها مانند الماس یاقوت ، زمرد و مانند آن که به عنوان زینت و زیور به کار می رود.

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره
##### پالیز -> /home/sfmqrb/git/rishe/data/verification/sources/web/33245eed4fee95d3.txt
STATUS: 200
1819 chars; excerpt:
معین
 ( اِ.) 1 - باغ ، بوستان . 2 - کشتزار. 3 - زمینی که در آن خربزه ، خیار و مانند آن بکارند.

 جست‌وجوی مشابه

 پالیزبان
 فرهنگ انتشارات معین
 (اِمر.) 1 - باغبان ، دشت بان . 2 - آهنگی از موسیقی قدیم .

 پاکیزه
 فرهنگ انتشارات معین
 (زِ) (ص مر.) 1 - پاک ، نظیف ، طاهر. 2 - منزه ، مقدس .

 پالیدن
 فرهنگ انتشارات معین
 (دَ) 1 - (مص م .) صافی کردن ، تصفیه کردن . 2 - جستجو کردن چیزی در خاک . 3 - فروریختن . 4 - به آخر رسیدن .

 پالیده
 فرهنگ انتشارات معین
 (دِ) (ص مف .) صاف شده ، خالص شده .

 پالیک
 فرهنگ انتشارات معین
 (اِمر.)= بالیک : پای افزاری از چرم گاو که رشته ها در آن بسته اند؛ پای افزار، کفش ، چارق ، شم ، پاپیچ ، پاتابه ، لفافه .

 بیشتر
 ۱ واژه مشابه 
 جست‌وجوی متن

 لته
 فرهنگ انتشارات معین
 ( ~ .) (اِ.) 1 - پالیز خربزه ، هندوانه ، خیار و غیره . 2 - کشتزار.

 تواره
 فرهنگ انتشارات معین
 (تُ رِ) (اِ.) 1 - اتاقی که در آن سرگین چارپایان و کاه و غیره ریزند. 2 - بته های خار که بالای دیوا
##### روضه -> /home/sfmqrb/git/rishe/data/verification/sources/web/6f7933488db15fb7.txt
STATUS: 200
2087 chars; excerpt:
معین
 (رَ ض ) [ ع . روضة ] (اِ.) 1 - باغ ، گلزار. ج . ریاض ، روضات . 2 - مطالب و اشعاری که هنگام عزا و سوگواری بالای منبر می خوانند.

 جست‌وجوی هم‌آوا

 روزه
 فرهنگ انتشارات معین
 (زِ) (اِ.) یکی از شعائر مذهبی است و آن خودداری از آشامیدن و خوردن سایر مبطلات مربوط به آن است از اذان صبح تا اذان مغرب .

 جست‌وجوی مشابه

 روضه خوان
 فرهنگ انتشارات معین
 ( ~. خا) [ ع - فا. ] (ص فا.) شخصی معمولاً در لباس روحانی که کارش خواندن روضه است .

 روضه گاه
 فرهنگ انتشارات معین
 ( ~.) [ ع - فا. ] (اِمر.) 1 - باغ . 2 - بهشت .

 جست‌وجوی متن

 روضه خوان
 فرهنگ انتشارات معین
 ( ~. خا) [ ع - فا. ] (ص فا.) شخصی معمولاً در لباس روحانی که کارش خواندن روضه است .

 ریاض
 فرهنگ انتشارات معین
 [ ع . ] (اِ.) جِ روضه ؛ باغ ها.

 پامنبری
 فرهنگ انتشارات معین
 (مِ بَ) [ فا - ع . ] (ص نسب .)کسی که در پایین منبر با خواندن اشعار مذهبی و مرثیه خوانی به روضه خوان اصلی کمک می کند.

 پیش خوان
 فرهنگ انتشارات معین
 ( ~.) (ص ف
##### رونق -> /home/sfmqrb/git/rishe/data/verification/sources/web/e6469fc2149c2e69.txt
STATUS: 200
1204 chars; excerpt:
معین
 (رُ نَ) [ ع . ] (اِمص .) 1 - فروغ ، روشنایی . 2 - زیبایی ، جمال . 3 - رواج .

 جست‌وجوی متن

 روایی
 فرهنگ انتشارات معین
 (رَ) (حامص .) رونق ، رواج .

 واخوردگی
 فرهنگ انتشارات معین
 (خُ دِ) (حامص .) 1 - از رواج و رونق افتادن . 2 - رد شدن . 3 - سرخوردگی ، یأس .

 بازار شکستن
 فرهنگ انتشارات معین
 (شِ کَ تَ) (مص ل .) از رونق و رواج انداختن .

 کسادی
 فرهنگ انتشارات معین
 ( ~ .) [ ع - فا ] (حامص .) بی رونقی .

 سوت و کور
 فرهنگ انتشارات معین
 (تُ) (ص مر.) (عا.) 1 - کساد، بی رونق . 2 - بی سر و صدا، ساکت .

 بیشتر
 ۲۳ واژه در متن 

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره
##### روستا -> /home/sfmqrb/git/rishe/data/verification/sources/web/253fe7b8509b6e46.txt
STATUS: 200
1361 chars; excerpt:
معین
 (اِ.) ده ، قریه .

 جست‌وجوی مشابه

 روستایی
 فرهنگ انتشارات معین
 (ص نسب .) کشاورز، دهقان .

 راستا
 فرهنگ انتشارات معین
 (اِ.) 1 - راستی . 2 - راست ، جانب راست . 3 - امتداد.

 راستاحسینی
 فرهنگ انتشارات معین
 (حُ س ) [ فا - ع . ] (ص مر.) 1 - (عا.) راست و درست ، ساده و بی ریا. 2 - (اِمر.) مقامی است در موسیقی .

 رستاخیز
 فرهنگ انتشارات معین
 (رَ) (اِمر.) رستخیز، قیامت ، به پا خاستن مردگان .

 رستاد
 فرهنگ انتشارات معین
 (رَ) (اِ.) جیره ، مقرری .

 بیشتر
 ۲ واژه مشابه 
 جست‌وجوی متن

 غلچگی
 فرهنگ انتشارات معین
 (غَ چِ) (حامص .) 1 - روستایی بودن . 2 - زندگانی کردن مانند اوباش .

 فرناس
 فرهنگ انتشارات معین
 (فِ) (اِ.) 1 - مهتر روستاییان . 2 - شیر ستبر گردن و دلیر.

 غلچه
 فرهنگ انتشارات معین
 (غَ چَ یا چِ) (ص .)1 - روستایی . 2 - اوباش .

 کلی
 فرهنگ انتشارات معین
 (کُ لِ) (ص نسب .) 1 - روستایی . 2 - جذام ، خوره .

 مخلاف
 فرهنگ انتشارات معین
 (مِ) [ ع . ] (اِ.) روستا، ده .

 بیشتر

##### حور -> /home/sfmqrb/git/rishe/data/verification/sources/web/d200c16c2b662331.txt
STATUS: 200
778 chars; excerpt:
معین
 [ ع . ] (اِ.) 1 - زن سیاه چشم . 2 - زن زیباروی .

 جست‌وجوی هم‌آوا

 هور
 فرهنگ انتشارات معین
 1 - (اِ.) آفتاب ، خورشید. 2 - ستاره ، بخت ، طالع .

 جست‌وجوی مشابه

 حوراء
 فرهنگ انتشارات معین
 [ ع . ] (ص .) 1 - زن سیاه چشم . 2 - زن بهشتی .

 حوری
 فرهنگ انتشارات معین
 [ ع - فا. ] (ص نسب .) زن بهشتی .

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره
##### موت -> /home/sfmqrb/git/rishe/data/verification/sources/web/d21f7fa1675e2fa6.txt
STATUS: 200
1785 chars; excerpt:
معین
 (مَ) [ ع . ] (اِ.) مرگ .

 جست‌وجوی مشابه

 مؤتمر
 فرهنگ انتشارات معین
 (مُ تَ مَ) [ ع . ] (اِ.) محل اجتماع ، کنفرانس .

 مؤتمن
 فرهنگ انتشارات معین
 (مُ تَ مِ) [ ع . ] (ص .) اعتماد کننده .

 مؤتمن
 فرهنگ انتشارات معین
 (مُ تَ مَ) [ ع . ] (ص مف .) اعتماد کرده شده ، امین .

 موتاب
 فرهنگ انتشارات معین
 (ص فا.) کسی که ریسمان می تابد.

 موتاسیون
 فرهنگ انتشارات معین
 (مُ) [ فر. ] (اِ.) استحالة عنصری ، جهش ، دگرگونی آنی .

 بیشتر
 ۳ واژه مشابه 
 جست‌وجوی متن

 موتور
 فرهنگ انتشارات معین
 (مُ تُ) [ فر. ] (اِ.) 1 - دستگاهی که سبب به کار انداختن و تولید ماشین می شود. 2 - دستگاهی که انواع انرژی را به انر ژی مکانیکی تبدیل می کند. 3 - موتورسیکلت .

 موتورسیکلت
 فرهنگ انتشارات معین
 ( ~. لِ) [ فر. ] (اِ.) دوچرخه ای که به وسیلة موتور حرکت می کند.

 میل لنگ
 فرهنگ انتشارات معین
 (لَ) (اِمر.) میله ای است در موتور اتومبیل که ب ه روی دو محور حرکت می کند. دستة پیستون ها روی میل لنگ سوار است ، خاصیت
##### مات -> /home/sfmqrb/git/rishe/data/verification/sources/web/cd161b1d197389e3.txt
STATUS: 200
1823 chars; excerpt:
معین
 (ص .) تار، کدر.

 مات
 فرهنگ انتشارات معین
 (ص .) 1 - حیران ، سرگشته . 2 - (اِ.) وضعیتی در بازی شطرنج که شاه قادر به هیچ حرکتی نیست و بازی به اتمام می رسد.

 جست‌وجوی مشابه

 مات کردن
 فرهنگ انتشارات معین
 (کَ دَ) (مص م .) 1 - سرگردان کردن . 2 - مغلوب کردن شاه در بازی شط رنج .

 ماتحت
 فرهنگ انتشارات معین
 (تَ) [ ع . ] (اِ.) 1 - پایین ، زیر. 2 - در فارسی به معنای مقعد.

 ماترک
 فرهنگ انتشارات معین
 (تَ رَ) [ ع . ] (اِ.) میراث ، آنچه که از شخص مرده به جا می ماند

 ماترنگ
 فرهنگ انتشارات معین
 (تُ یا تِ رَ) (اِ.) سوسمار، چلپاسه .

 ماتریالیسم
 فرهنگ انتشارات معین
 (تِ) [ فر. ] (اِ.) ماده گرایی ، نظریه ای که برطبق آن هیچ جوهری جز ماده وجود ندارد.

 بیشتر
 ۸ واژه مشابه 
 جست‌وجوی متن

 ماتم سرا
 فرهنگ انتشارات معین
 ( ی ) ( ~ . سَ) [ ع - فا. ] (اِمر.) ماتمکده ، عزاخانه .

 شاه مات
 فرهنگ انتشارات معین
 (اِمر.) شه مات ، هنگامی که «شاه » شطرنج مات شود.

 شهمات
 فرهنگ انتشارات معین
 (شَ) 
##### ماتادور -> /home/sfmqrb/git/rishe/data/verification/sources/web/8bee757de942bfb9.txt
STATUS: 200
431 chars; excerpt:
معین
 (دُ) [ فر. ] (اِ.) کسی که در میدان عمومی با گاو مبارزه می کند، گاوباز.

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره
```


### [2026-09-04T15:11:01.864Z] TOOL RESULT

```
##### cherub -> /home/sfmqrb/git/rishe/data/verification/sources/web/8c707fd797ce7ad6.txt
4639 chars; excerpt:
 
 Share: 

 Tweet 

 n. 1. pl. cher·u·bim (ch ĕ r  ə -b ĭ m ′ , -y ə -b ĭ m ′ ) a. A winged celestial being.
 b. cherubim Christianity The second of the nine orders of angels in medieval angelology.

 2. pl. cher·ubs a. A putto.
 b. A person, especially a child, with an innocent or chubby face.

 [Middle English, from Late Latin, from Hebrew k ə rûb ; see krb in the Appendix of Semitic roots .]
 che·ru  bic (ch ə -r   b ĭ k) adj. 
 che·ru  bi·cal·ly adv. 

 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.

 Indo-European & Semitic Roots Appendices
 Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
 Indo-European Roots 
 Semitic Roots 
 The Indo-European appendix covers nearly half of the Indo-European roots that have left their mark on English w
##### griffin -> /home/sfmqrb/git/rishe/data/verification/sources/web/9f131273065d9ffb.txt
4459 chars; excerpt:
s Series!
 Find out more! 

 INTERESTED IN DICTIONARIES?
 Check out the Dictionary Society of North America at http://www.dictionarysociety.com 

 grif·fin also grif·fon or gryph·on (gr ĭ f  ə n) 
 Share: 

 Tweet 

 n. A fabulous beast with the head and wings of an eagle and the body of a lion.

 [Middle English griffoun , from Old French griffon , from grif , from Latin gr ȳ pus, gr ȳ phus , variants of gr ȳ ps , gr ȳ p- , from Greek gr ū ps .]

 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.

 Indo-European & Semitic Roots Appendices
 Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
 Indo-European Roots 
 Semitic Roots 
 The Indo-European appendix covers nearly half of the Indo-European roots that have left their mark on English words. A more c
##### emerald -> /home/sfmqrb/git/rishe/data/verification/sources/web/08eae3a92d63770a.txt
4698 chars; excerpt:
the Dictionary Society of North America at http://www.dictionarysociety.com 

 em·er·ald ( ĕ m  ə r- ə ld, ĕ m  r ə ld) 
 Share: 

 Tweet 

 n. 1. A brilliant green to grass-green transparent variety of beryl, used as a gemstone.
 2. A strong yellowish green.

 adj. Of a strong yellowish green.

 [Middle English emeraude , from Old French, from Medieval Latin esmeralda, esmeraldus , from Latin smaragdus , from Greek smaragdos ; akin to Sanskrit marakatam , probably of Semitic origin; akin to Akkadian barraqtu and Hebrew b ā reqet , a kind of gemstone (probably emerald); see brq in the Appendix of Semitic roots .]

 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.

 Indo-European & Semitic Roots Appendices
 Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appen
##### paradise -> /home/sfmqrb/git/rishe/data/verification/sources/web/d72429a4addfeab9.txt
6743 chars; excerpt:
ding to some forms of Christian belief, an intermediate resting place for righteous souls awaiting the Resurrection.

 3. a. A place of great beauty or happiness: saw the park as a paradise within a noisy city. 
 b. A state of delight or happiness: The newlyweds have been in paradise for months. 

 [Middle English paradis , from Old French, from Late Latin parad ī sus , from Greek paradeisos , garden, enclosed park, paradise, from Avestan pairida ē za- , enclosure, park : pairi- , around; see per 1 in the Appendix of Indo-European roots + da ē za- , wall; see dheigh- in the Appendix of Indo-European roots .]
 par ′ a·di·si  a·cal (-d ĭ -s ī  ə -k ə l, -z ī  -), par ′ a·di·si  ac (- ă k), par ′ a·di·sa  i·cal (-d ĭ -s ā  ĭ -k ə l, -z ā  -), par ′ a·di·sa  ic (- ĭ k), par ′ a·dis  al (-d ī  s ə l, -z ə l) adj. 
 par ′ a·di·si  a·cal·ly , par ′ a·di·sa  i·cal·ly , par ′ a·dis  al·ly adv. 
 Word History: From an etymological perspective at least, paradise is located in ancient
##### matte -> /home/sfmqrb/git/rishe/data/verification/sources/web/9b25a65910ab2cd9.txt
5013 chars; excerpt:
finish.

 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.

 matte  2 (m ă t) 
 Share: 

 Tweet 

 n. A mixture of a metal with its sulfides, produced by smelting the sulfide ores of copper, lead, or nickel.

 [French, curdled milk, matte, from feminine of obsolete mat , compact, from Old French, dull, from Latin mattus , stupefied; see MAT 2 .]

 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.

 Indo-European & Semitic Roots Appendices
 Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
 Indo-European Roots 
 Semitic Roots 
 The Indo-European appendix covers nearly half of the Indo-European roots that have left their mark on English words. A more complete treatm
##### checkmate -> /home/sfmqrb/git/rishe/data/verification/sources/web/d740d81f67e9694c.txt
4878 chars; excerpt:
en on the next move with no way of escape or defense possible.
 2. To defeat completely.

 n. 1. a. A move in chess that checkmates an opponent's king.
 b. The position or condition of a checkmated king.

 2. An utter defeat.

 interj. Used to declare the checkmate of an opponent's king in chess.

 [Middle English chekmat , from Old French eschec mat , from Arabic š ā h m ā t , the king is dead : š ā h , king (from Persian sh ā h ; see SHAH ) + m ā t , died (from earlier m ā ta , to die; see mwt in the Appendix of Semitic roots ).]

 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.

 Indo-European & Semitic Roots Appendices
 Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
 Indo-European Roots 
 Semitic Roots 
 The Indo-European appendix covers nearl
##### margarite -> /home/sfmqrb/git/rishe/data/verification/sources/web/0f54b893e1d1ffb8.txt
4536 chars; excerpt:
 Series!
 Find out more! 

 INTERESTED IN DICTIONARIES?
 Check out the Dictionary Society of North America at http://www.dictionarysociety.com 

 mar·ga·rite (mär  g ə -r ī t ′ ) 
 Share: 

 Tweet 

 n. 1. A rock formation that resembles beads, found in glassy igneous rocks.
 2. Archaic A pearl.

 [Ultimately from Greek margar ī t ē s , pearl, perhaps of Iranian origin; perhaps akin to Avestan m ə r ə γ a- , bird (since the two valves of some pearl-bearing bivalves resemble a pair of bird wings when spread open) .]

 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.

 Indo-European & Semitic Roots Appendices
 Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
 Indo-European Roots 
 Semitic Roots 
 The Indo-European appendix covers nearly half of the In
##### matador -> /home/sfmqrb/git/rishe/data/verification/sources/web/5b8ea24cb3892bf7.txt
4479 chars; excerpt:
INTERESTED IN DICTIONARIES?
 Check out the Dictionary Society of North America at http://www.dictionarysociety.com 

 mat·a·dor (m ă t  ə -dôr ′ ) 
 Share: 

 Tweet 

 n. 1. A bullfighter who performs the final passes and kills the bull.
 2. Games One of the highest trumps in certain card games.

 [Spanish, from matar , to kill, possibly from Vulgar Latin *matt ā re , to beat senseless, perhaps from Latin mattus , stupefied; see MAT 2 .]

 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.

 Indo-European & Semitic Roots Appendices
 Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
 Indo-European Roots 
 Semitic Roots 
 The Indo-European appendix covers nearly half of the Indo-European roots that have left their mark on English words. A more complete t
```


## [2026-09-04T15:12:09.640Z] AGENT (thinking)

I'm tracking a batch of remaining independent lookups—unanchored KLN greps, reruns for POK/SYN/SOD, cleaned BQT leaves, FSF/AFM/FSD/DEV/LKT/HRN checks, and searches in IEC and AHD. I'll work through these next.


## [2026-09-04T15:12:13.005Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; $LF KLN_1966.txt grep 'emerald,  n' 1 --chars 1100; $LF KLN_1966.txt grep 'checkmate,  n' 1 --chars 1100; $LF KLN_1966.txt grep 'liberal,  adj' 1 --chars 700; $LF KLN_1966.txt grep 'Margaret,  fem' 1 --chars 500; $LF KLN_1966.txt grep 'berakah,' 1 --chars 700; $LF KLN_1966.txt grep 'dough,  n' 1 --chars 800; $LF KLN_1966.txt grep 'paradise,  n' 1 --chars 800; for n in 506 507 509 510; do $LF KLN_1966.txt leaf $n --chars 0 | head -1; done",
 "description": "KLN unanchored greps and page numerals near leaf 508"
}
```


### [2026-09-04T15:12:16.271Z] TOOL RESULT

```
--- KLN_1966.txt leaf 280; page-number candidates: ['1']
ation.  — Late  L.  emendatorius,  fr.  L.  emenddtus,  pp.  of emendare.  See  emend  and  -atoiy. emerald,  n.,  a  bright-green  precious  stone.  — ME.  emeraude,  fr.  OF.  esmeralde,  esmeraude  (F. emeraude ),  fr.  L.  smaragdus  (whence  also  It. smeraldo,  Sp.  esmeraldd),  fr.  Gk.  <j|j.apay8o<;, |j.dpo:ySo5,  ‘emerald’,  which  is  of  Sem.  origin. Cp.  Heb.  bareqeth ,  Akkad,  barraqtu,  ‘emerald’, lit.  ‘something  flashing’,  a  derivative  of  Heb. bardq,  resp.  Akkad,  birqu,  ‘lightning’,  which  are rel.  to  Aram,  b-raq,  barqd,  Arab,  barq,  ‘light¬ ning’,  Heb.  bdraq,  Aram.  beraq,  Arab,  baraqa, Ethiop.  baraqa,  ‘it  flashed,  glistened’,  Akkad. baraqu,  ‘to  flash’.  Cp.  OI.  marakatam ,  Pers. zumurrud  (whence  Turk,  ziimriid,  whence  Russ. izumrud),  ‘emerald’,  which  are  also  Sem.  loan words.  Cp.  also  smaragd,  which  is  a  doublet  of emerald.  Cp.  also  Esmeralda. Derivative:  emerald,  adj. emeraldine,  n.,  a  dark  green  dye.  —  Formed  fr. prec.  word  with  suff.  -ine  (representing  Gk. -Tvog). emerge,  intr.  v.,  to  rise  from  a  fluid,  to  appear.  — L.  emergere,  ‘to  come  forth,  come  up,  rise,  ex¬ tricate  oneself’, 

--- KLN_1966.txt leaf 154; page-number candidates: ['272', '273']
lso  It.  scaccomatto).  See  check,  ‘a  sudden  stop’ and  cp.  mate,  ‘checkmate’. Derivatives:  checkmate,  n.  and  tr.  v. cheeky,  adj.,  divided  into  squares  of  alternate tincture.  —  Formed  fr.  check,  n.,  ‘a  sudden stop’,  with  adj.  suff.  -y. Cheddar  cheese,  Cheddar,  also  Cheddar,  n.  — Named  fr.  Cheddar,  Somerset,  England,  where it  was  originally  made. Derivative:  cheddar-ing,  n. 272 cheddite,  n.,  an  explosive  used  for  blasting.  — Named  after  Chedde,  a  town  in  the  Department Haute-Savoie  in  France,  where  it  was  first made;  cp.  lyddite.  For  the  ending  see  subst. suff.  -ite. cheder,  n.  —  See  heder. cheek,  n.  —  ME.  cheke,  fr.  ceace,  ‘jaw,  cheek’, rel.  to  MLG.  kake,  Du.  kaak,  ‘jaw,  cheek’;  of uncertain  origin. Derivatives:  cheek,  tr.  v.,  cheek-y,  adj.,  cheek- i-ly,  adv.,  cheek-i-ness,  n. cheenar,  n.  —  A  variant  spelling  of  chinar. cheep,  intr.  and  tr.  v.  —  Of  imitative  origin. Derivatives:  cheep,  n.,  cheep-er,  n.,  cheep-y , adj.,  cheep-i-ly,  adv.,  chcep-i-twss,  n. cheer,  n.  —  ME.  chere,  ‘face,  countenance,  cheer’, fr.  OF.  chiere,  chere,  ‘face’  (whence  F.  chere, ‘coun

--- KLN_1966.txt leaf 414; page-number candidates: ['770', '771']
,  ‘not’,  and legitimate. Derivatives:  illegitimate,  n.  and  tr.  v.,  illegi- timat-ion,  n. illiberal,  adj.  —  F.  illiberal,  fr.  L.  illiberalis,  ‘un¬ worthy  of  a  freeman,  ungenerous’,  which  is formed  fr.  in-,  ‘not’,  and  liberalis,  ‘pertaining to  a  freeman,  pertaining  to  freedom’.  See liberal. Derivatives:  illiberal-ity,  n.,  illiberal-ly,  adv., illiberal-ness,  n. illicit,  adj.,  not  lawful.  —  F.  illicite,  fr.  L.  illi- citus,  ‘not  allowed,  unlawful,  illegal’,  which  is formed  fr.  in-,  ‘not’,  and  licitus,  ‘allowed,  law¬ ful’.  See  licit. Derivatives:  illicit-ly,  adv.,  illicit-ness,  n. Miciuin,  n.,  a  genus  of  trees  of  the  magnolia family  (bot.)  —  ModL.,  fr.  L.  illicium,  ‘allure¬ 770 771 ment’,  lit.  ‘that  which  entices  or  allu

--- KLN_1966.txt leaf 504; page-number candidates: []
  OF.  maresme,  Catal.  maresma,  ‘marsh’, which  are  of  the  same  origin,  and  see  maritime. Margaret,  fem.  PN.  —  OF.  Margaret  (F.  Mar¬ guerite),  fr.  L.  margarita,  pearl  .  See  margarite and  cp.  Margery. margaric,  adj.,  pertaining  to  a  white  fatty  acid C^H^CO.H  ( chem .)  —  F.  margarique,  fr.  Gk. papyapov,  ‘pearl’.  See  margarite  and  -ic. margarin,  n.,  a  fatty  substance  found  in  animal fats  and  vegetable  oils  (chem.)  —  F.  margarine , fr.  margarique,  lit.  ‘of  a  pearl-like  color  (see margaric  and  chem.  suff.  -in) ;  coined  by  the French  chemist

--- KLN_1966.txt leaf 98; page-number candidates: []
g,  declaration’,  which  is  rel.  to  OE. ewepan,  ‘to  say’.  See  quoth  and  cp.  prec.  word, berakah,  n.,  blessing,  benediction.  —  Heb. berakhdn,  ‘blessing’,  from  the  stem  of  herakh, ‘he  blessed’,  which  is  rel.  to  Aram,  bardkh, Arab,  bdraka,  Ethiop.  bdrdka,  ‘he  blessed’, Akkad,  kardbu  (a  metathesis  form),  ‘to  bless’, Ethiop.  mekrab  (metath.),  ‘temple’.  Cp.  cherub, griffin. Berber,  n.  —  Arab,  bdrbar,  ‘the  people  of  Bar¬ bary’,  perhaps  derived  fr.  Gk.  fidpjixpof;,  ‘bar- bar’  (see  barbaric). Berberidaceae,  n.  pi.,  the  barberry  family  (hot.) —  Formed  fr.  Berberis  with  suff.  -aceae. berberidaceous,  adj.  —  See  prec.  word  and -aceous. Berberis,  n.,  a  genus  of  plants,  the  barberry  ( bot .) — -  ML.  berberis,  barbaris,  ‘b

--- KLN_1966.txt leaf 261; page-number candidates: ['477']
ead¬ ing’,  fr.  diicere,  ‘to  lead’.  See  duct,  duke. Derivative:  douche,  tr.  and  intr.  v. dough,  n.  —  ME.  dog,  dogh,  dah,  fr.  OE.  dag. doughty Dracontium rel.  to  ON.  deig,  Dan  deig ,  Swed.  deg,  MLG. deck,  MDu.  deech,  Du.  deeg,  OHG.,  MHG. teic,  G.  Teig ,  Goth,  daigs,  dough’,  digan,  ‘to knead’,  fr.  I.-E.  base  *dheigh-,  *dhoigh-,  *dhigh-, ‘to  form  out  of  clay,  to  knead,  form’,  whence also  Of.  dehmi,  ‘I  smear,  anoint’,  dehah,  ‘body’, lit.  ‘that  which  is  formed’,  dehi,  ‘rampart,  dam, dike’,  Avestic  daeza,  ‘wall’,  pairi-daeza,  ‘en¬ closure’  (whence  Gk.  TrapaSsiaop,  ‘enclosed park’),  OPers.  dida,  ‘castle’,  Toch.  A  tsek-, tsaik-,  B  tsik-,  ‘to  form’,  tseke,  ‘statue’,  Arm. dez ,  ‘heap,  pile’,  dizanem,  ‘I  heap  up,  pile  up’, Gk.  Tetyo?,  zov/'K  (dissimilated  fr.  *Hixoz, *ffotyo<;),  ‘wall’  (orig.  'clay  wa

--- KLN_1966.txt leaf 600; page-number candidates: ['1124', '1125']
l,  adj.  —  Formed  fr.  para¬ dise  on  analogy  of  Hebraic. Derivative:  paradisaical-ly,  adv. paradise,  n.  —  ME .paradis,  fr.  OF.  (=  F .)  para- dis,  

--- KLN_1966.txt leaf 506 / 903; page-number candidates: ['942', '943', '944', '945']
--- KLN_1966.txt leaf 507 / 903; page-number candidates: ['1', '946', '947']
--- KLN_1966.txt leaf 509 / 903; page-number candidates: ['948', '949']
--- KLN_1966.txt leaf 510 / 903; page-number candidates: ['950']
```


## [2026-09-04T15:12:16.759Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; $LF POK_02.txt grep '^1\\. *leudh|1\\.  *leudh-' 1 --chars 2200; echo \"-- mad --\"; $LF POK_02.txt grep '^mad-|^ *mad- ' 1 --chars 1800; echo \"-- SYN 942 --\"; $LF SYN.txt leaf 942 --chars 800; echo \"-- SYN raod --\"; $LF SYN.txt grep 'raoδ|raoda|raod-' 3 --chars 1000",
 "description": "Pokorny leudh and mad, Buck p.874 and raod"
}
```


### [2026-09-04T15:12:18.610Z] TOOL RESULT

```
NO HITS ^1\. *leudh|1\.  *leudh-
-- mad --
NO HITS ^mad-|^ *mad- 
-- SYN 942 --
--- SYN.txt leaf 942 / 1545; page-number candidates: ['871?']
’, all referring to the aon of the rising Sun.
oa +qus-, *Gusos-, *ysos-, etc., in ah for ‘dawn’ and ‘east’, beside verb forms a8 Skt. ucchatt, Av. usatt ‘lights up’ (esp. of the dawn), Lith. aust, Lett. ust ‘to dawn’. Walde-P. 1.26f. Er- nout-M. 93. Walde-H. 1.86.
Grk. Aeol. atws, Dor. aus, Hom. 7ws, Att, tos dawn’ and ‘east’; Lat. aurora (‘ausis-a) ‘dawn’ and (mostly poet.) fast’ (prob. also auster ‘south wind’, 1248); ON ausir, OF éast, OHG dstan, etc, general Gmc., with various suffixes; lith. ausra ‘dawn’, Lett. austrums ‘east’ ; ChSl. za ustra ‘in the morning’; Skt. yas, Av. usd ‘dawn’, whence Av. usas- eae (fr. *wpa-usah-) adjs.
9.45. Words f
ipefore’ OT
A Gtk. avarohy ‘a rising’, esp. pl. barohal miov ‘sunrise’, hence ‘east’ : a ‘rise’ (esp. of the sun).
e “a ed pres. pple. of orir
-- SYN raod --
--- SYN.txt leaf 68; page-number candidates: []
, ‘stream’, Pol. strumier, strumyk ‘brook’; Skt. srotas-, sravat-, Av. @raotah- (in cpds.), ravan-, raodah-, ‘stream, river’, OPers. rauta ‘river’ (used of the Nile), NPers. rid ‘river’. 2. Derivs. of IE *rei- in Skt. ri- ‘et go’, mid. ‘flow’, Goth. rinnan ‘run, flow’, ete. Walde-P. 1.139 ff., Ernout- M. 866 f. - Lat. rivus ‘brook’; OE rip ‘brook’ (gl. Lat. rivus), MLG ride ‘brook’; Goth. rinnd ‘brook’; ChSl. réka, etc., general Slavic for ‘river’. From Lat. rivus (through rius) come Sp. rfo ‘river’ (Olt. rio ‘brook’ and ‘riy- er’, OF r. ri ‘brook’), Rum. rité ‘river’ (now fluviu for large rivers like the Danube). Dim. forms for ‘rivulet, brook’, Lat. rivolus, It. rivolo, Rum. rviilet, It. ruscello, Fr. ruisseau, REW 7341, 7338a. Gamillscheg 777. 3. From IE *ap (and ab-) ‘water’, Skt. pas, etc. (1.31). Walde-P. 1.46, Ernout-M. 45. Walde-H. 1.40. Lat. amnis ‘river’ (poet.); Ir. ab (aba, oub, etc.), NIr. abha ‘river’, W. afon ‘river’, afonig ‘brook’, Br. aven ‘river’ (mostly obs.), Lith. upé, Lett. upe, OPruss. ape ‘river’, Lith. upelis, Lett. upele ‘brook’ (but Lett. upe also ‘brook’). 4. 

--- SYN.txt leaf 737; page-number candidates: ['4?', '677?']
e scorrere. 1. IE *sreu-. Walde-P. 2.702 f. Grk. péw, Skt. sru-, Av. rud- (pres. stem raosa-, caus. raodaya-; cf. also raosah- ‘stream’) beside uwrvant- (*sru- vant-) pple. ‘flowing’; more widespread in derivs., esp. words for ‘river’ or ‘stream’ (1.36). 2. From ‘run’ (10.46). Grk. tpéxw ‘un’, NG ‘run’ and ‘flow’; Lat. currere ‘run’, as ‘flow’ mostly poet., It. (s)cor- rere, Sp. correr ‘run, flow’, Rum. curge (re-formed a

--- SYN.txt leaf 946; page-number candidates: ['2?', '875?']
nts (through OS liodan ‘spring up, grow’, Skt. rudh-, lah can?) or otherwise is possible. Er- | Av. raod- ‘grow’ (12.53). Walde-P. nout-M. 378f. Walde-H. 1.530f. 2.416. Feist 323. ap = sie jos eb acrn eal more or less Goth. hiwi, OF hiw, heow also ‘color, it 7 o mica! word in most of the | appearance’, ME hiewe (in all senses MW ur. ‘anguages, as Dan., Sw., NHG | NE hue restricted to ‘color’) : ON Aj Mh form, in Slavic languages forma. ‘down’, Sw. hy ‘color of the skin’, root th eg “laws prepenty ‘shape given to | connection disputed, perh. fr. that in Oo ( : fingere ‘shape, mold’, figulus | he@wen ‘blue’, Ir. ctar ‘dark’, ON hart th gpATI *skeu- in words for » ate. OF i 1.360 f. Falk-Torp 2 Walde SD 3.v. hue, sb.. _ Norw. mynd ‘manner, ca re’ ; OF gemynd ‘mem- charles : iesth. gamunds ‘remem- ory’, ete-s Lat. méns, ate Semantic change fr. ‘re- ‘appearance’ (as re- form’. Torp, Nynorsk ce’ to nem nembered) and Sw. skapnad, OE gesceap, NE shape : ON, Sw. skapa, acai Goth. gaskapjan, OHG vaphen {0rT, create’, etc., perh. orig. thip, hew out’, fr. a parallel form of the rotsin Goth. skaban,
```


## [2026-09-04T15:12:19.824Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; echo \"-- SOD 217 --\"; $LF SOD_pages.txt leaf 217 --chars 2500; echo \"-- SOD 410 --\"; $LF SOD_pages.txt leaf 410 --chars 2500; echo \"-- SOD dyz entry --\"; $LF SOD_pages.txt grep \"3826 dyz\" 1 --chars 300; echo \"-- SOD rwd entry --\"; $LF SOD_pages.txt grep \"8563 rwd\" 1 --chars 300",
 "description": "Sogdian dictionary leaves 217, 410 and dyz/rwd entries"
}
```


### [2026-09-04T15:12:21.631Z] TOOL RESULT

```
-- SOD 217 --
--- SOD_pages.txt leaf 217 / 645; page-number candidates: ['152', '3849?', '3837?', '3839?', '16?', '3840?', '3841?', '3842?']
 fVk
                                                                                                                         152
 3835 fVk ** ^s'k                                                    GMS, BSOAS 11.74, lOn 5; GMS 994
 3836 f»S»m-     C                                    <^j       3848 fcmpd     C                                   jl*r«U
        fasam    ©impf. ^fs'm-, P's'm-                               f(o)campa5     ©ob. -y =*fcmbS, fc'npS
                                                                     world
        (to)scnd
        STii 6.18; BSTii 860.34, 873.11; C2, 23V4, 55R27,            STi 14, 15, 72.4, 75.9, 77.1, 71.5; Sund. AoFviii
          66R 11                                                       1981 p214
                                                                3849 fcmrz-     C                                    d*^
 3837 f'sqr- C                           o>J'ijjjmo*J'J+>
      faskar ©impf. =»fskr-                                          facmarz, facmarz       ©<*fraca-marz ? ©impf.
      (ro)follow                                                       fcmrz ^Pcmrz-, fcmsty
        C2, EV                                                       (/cOseize
                                                                     STi 6-11; Sund. AoFiii 1975, 16R6; Schwartz.
 3838 Psn's- M                                        ^Ui              STSC 16; C2, 12R3n pl22
      fasnas ©<*fraxsnasa ©impf. =»fsnJs-
      (rc)know                                                  3850 fcmst- =» Pcmrz-
      Sogdica. 31.9; S W, BSOAS 1980, 50                        3851 fcmsty C                                   <^f mxb^
                                                                     focmaste, facmaste ©pp. =*fcmrz-
 3839 ft>yr- C, S                             oxl^^of                seizcd
       fater (Ptyr-) ©impf. =»ftyr-2                                 STSC 16
       (to)cross over, 0o)remove
       C2, 87V 12; Frag. 2a23                                  3852 fS'ymtyh      B                            vf^<o>-i'
                                                                    foScmtya      -^pS'ymtyh
 3840 Ptyr- =* f>t>yr-
                                                                     magic, illusion
 3841 Pyr- B                                         o>s~f           STii 8.4
      fair, fcr ©<*fra-araya ? =^fyr-
      (/<?)stretch,Oo)extend                                   3853 f5'ys B, M                  
-- SOD 410 --
--- SOD_pages.txt leaf 410 / 645; page-number candidates: ['343', '8513?', '110?', '8527?', '8515?', '327?', '8528?', '8531?']
343


8513 rst'wc'ry B                                      ^jUb
     rastucare (rst'wdryy)                                         jewel, noble
     consolation                                                   VJ pi 18; TSP; SCE p69; BSTBL, pl29; Frag. Len.
                                                                     pl08; STii 7.29; Sogdica. 25.9; MSP b34, 110
      VJ 379, 388, 1433; rsfwcry, VJ 52b, +wn- "to                   el3 -f>
                                                                        pi.
        console"; Hen. JRAS 1945, 154.7
                                                             8527 rtn'yn'y B                             o^jtyr
8514 rst}wc}ryy M =» rst'wc^y                                     ratnene (rtnyn^Cw), rtnyny(y), rtny^y)
8515 rst(h) B                           c^>wc~Jj ^j                with jewel inlaid
     rast, rost (rst}) ^Sraz-, Parth. rast; Khwar. rst;
                                                                   BSTBL, pi 29; TSP; VJ; BBB; Hen. BSOAS 12,
       OP rasta ©f. n. & adj. nom. ace. -7A =^rsty,
                                                                    307.63; GMS 1053; rtnynykw, VJ 862; Dhy. 327
        rysty'q, rtsth
                                                             8528 rtn'ynch B                             J^^yr
      true, truth                                                 ratnene (rtnync) ©f. adj.
      BSTBL, Vim. 70, Dhu. 205; W-Lii, 579; Frag.                  with jewel inlaid
        Len.; Hen. 112R4; Tales. 480.11, 14; MDii B-4
                                                                   VJ 18b, 345, 520; STii 5.27
        R18, A-9R11; C2 p53, 99.52R14, 6R13; Sund.
        AoFi 1974, 224, 1V17, 6R2, lOi V8; AoFviii           8529 rtnp'myk M                                          Lj^/
        1981 p217                                                 ratn-famik, ratn-J3amik               ©<Av. bamya =»rtn-,
                                                                               ent ike ewel
8516 rsty C, B                                  c~.j*«c~Jj        resplend              l        j
     raste (rstyy) ©adj.; pi. -t                                  G e r s h . S o g d .  C p d s . 1945, 146.6
     true
      BSTii 883.20: C2, 48R22; Hen. Tales. 469.2a, SCE       8530 rtnyn>k(w) B =* rtn>yn>y
                                                                       P>m ^ rtn'ynty
                                                     
-- SOD dyz entry --
--- SOD_pages.txt leaf 216; page-number candidates: ['665?', '3809?', '3811?', '3812?', '3827?', '24?', '3814?', '3815?']
           ^^W- ^v^-j*' '^y-*       5cw-mec                                                         3826 dyz> C «* 5yz>       demoniac       GMS      1103; KG 583           *                                                                             'rt', -P                 f  3812 dywnt     C                            jA kly «i^j l tJill                                                                  

-- SOD rwd entry --
--- SOD_pages.txt leaf 411; page-number candidates: ['344', '8542?', '8545?', '8546?', '8560?', '8548?', '995?', '12?']
inf. ->y, Dhy. 196; AVS 114                                                                         8563 rwd C =» rw5 8552 rw'rtyh M                                                                         8564 rw8>k B                              (•JUiJJ)^Ui.l/      r(u)war0ya ? ©<Av. urvaOra ^rw'rt                                       ro5e, roSak ?      delicacy         Sogdica. 2.16, Add.
```


## [2026-09-04T15:12:26.736Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\npages=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\ndef clean(s): return re.sub('[‎‏‪-‮⁦-⁩]','',s)\ndef show(i,pat,w=700):\n    p=clean(pages[i])\n    for m in re.finditer(pat,p):\n        print(f'### leaf {i} match {pat!r}:'); print(p[max(0,m.start()-150):m.start()+w]); print(); break\nshow(311,'دژ')\nfor i in (371,372): show(i,'دیگ\\\\s',900)\nprint('#### divar search')\nfor i in range(360,395):\n    p=clean(pages[i])\n    for m in re.finditer(r'د[یي]وار\\s*[-=:؛]',p):\n        print('leaf',i,':',p[max(0,m.start()-100):m.start()+600].replace('\\n',' | ')); break\nprint('#### ruyidan search')\nfor i in range(390,415):\n    p=clean(pages[i])\n    for m in re.finditer(r'رو[یي][یي]دن|رُستن|رستن\\s*[-=:]',p):\n        print('leaf',i,':',p[max(0,m.start()-100):m.start()+500].replace('\\n',' | ')); break\nshow(434,'رستم',900)\nshow(405,'رز',900)\nEOF",
 "description": "Print cleaned Borhan vol 2 entries for dež, dīg, dīvār, rūyīdan, Rostam, raz"
}
```


### [2026-09-04T15:12:28.433Z] TOOL RESULT

```
### leaf 311 match 'دژ':
ا زای فارسی مشتمل بر سی وهفت لغت


دزاامه ه = بکر اول وفتح آخر                                                   = ۵بکر اول و سکون ثالی » قلمه
 بمعنی دژکام ات که زاهد ویرهیز کار )(٩ -                                    وحصارباشد - ۱وبمعلی زشت و,دوبدخوی وخشم
وخواجه‌سرا باشد ؛ وبفتح‌اول لز درست است.                                        نزد-
                                                                                   انی
                                                                                     ‌را
                                                                                       هکی
                                                                                         تند
                                                                                           فبب
                                                    

#### divar search
#### ruyidan search
leaf 407 :  ایذجا بطریق |   ( )۳چك :همآ مده است .                   ( )۲چك  :ژد و بازند .               ( )۱چك  :رستن |  |  |        - ۳قس :رسمان.                 قس :بازری ( باز رسنده ).        ۴         - ۱رکه :رسدن. |                                            رزژد » رزد (ه.م (.                 ؟  رکه  :اری ۰ |                    کلو را ز رسی بسر برمیر.                      بیلفنج و زالففد خوش خور |   .       ابوشکور بلخی(« .فت فری ٩۹ |  |    ۸رکه  :رسیدن»                        رکه :رست .      ۷            رکه  :ی٩ همین ستون.     ۱ |                        ٩ .        » ابیز « بوتکر    بهلوی 72            هز 20102 ,     
### leaf 434 match 'رستم':
           گوذشتن را گیز
                                                                                                  فته اند .
 ۸ے معروف‌است که رستم زال                       رسوتم
                                                                    روساختی کنابه از شرمنده شدن
                                                                                      وخجالت کشیدن باشد .
 زده * معرب      نقطه دار ) (£وفوفالی مفتوح بم                      روس انگر ده  ۴د پنکاف فارسی,
 روسوختها سکته راسخت باشد وآن مس سوخته                              روباه تربك است که سگ انکور باشد چه روی
 است و بعربی فحاس محرق گوبند  .بهترین آن                            گویند و دعر ای        دالهُ انگوررا          دنکن        نمعنی‌رویاه




                مصری بود .گرم است در دویم.                                                                      عذب التملب خوانند .
 رو سی = بروزن‌طوسی» منوب بولایت                                    رسومی؟ د بابای فارسی‌بر وزن‌دوستی؛
 روس باشد  -وئام پپلوانی است تورالی  -ولوعی                                      

### leaf 405 match 'رز':
  رزه                                                                                               -ی ) “A


 مکان‌جنکه      زرمگاه -بروزن گا                         رنگضرا کننزته‌اند -و٩یمعنی رنگ کننده - ۴
                                                         وامر برنگ کردن هم هت ٩  -و زهر هلاهل
                                                          را کیویزند  -ویکس اول مخقف ریز باه
                       گاه باشد ۲   کردن وجنگ

   مت      که         ون     ررمگه -
             رزمگاه است که جنک گاه باشد ۹                ازریختن مشتق است  -۴ودرعربی شالی راگوبند
 بروزن گرم سیر  ,لامروز
                                                         کبهرنج پوست دباارشد  ۴چرهزاز براج کوب
                        مگیر =            رد
                   بازدهم باشد از ماهپای ملکی ۱
                                                                                      رکاویند .
 ررمه = بفتح‌اول
```


## [2026-09-04T15:12:30.530Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\npages=open('FSF_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in (265,463):\n    p=pages[i]\n    for m in re.finditer(r'\\bرز\\b',p):\n        print(f'### FSF leaf {i}:'); print(p[max(0,m.start()-300):m.start()+700]); print(); break\npages=open('AFM_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in (75,76,77,82,83):\n    p=pages[i]\n    hits=[m.start() for m in re.finditer('رون|روض',p)]\n    print(f'### AFM leaf {i}: hits at {hits[:6]}')\n    for h in hits[:3]: print(p[max(0,h-200):h+500].replace('\\n',' | ')); print('...')\nEOF",
 "description": "Noushin raz entries; Addi Shir rawda/rawnaq leaves"
}
```


### [2026-09-04T15:12:32.173Z] TOOL RESULT

```
### FSF leaf 265:
                                     ‫فرهنگ شعوری اعتباری نندامردی‌وتوان به‬
 ‫سپید سیم رده بود در و مرجان بود‬                  ‫آن اعتماد داشت‪( .‬دربار؛ فرهنگ شعوری به‬
‫ستارة سحری بود قطره باران بود‬                         ‫نوشته دهخدا در صفحهٌ شصت مقدمة برهان‬
                                ‫رز(با زبر اول)‬
                                                        ‫قاطعبهتصحیح دکتر معیننگاهکنید)‪.‬‬
                                    ‫‪-۱‬باغ‪.‬‬
                                                      ‫دشرهلغنتامة عبدالقادر رخته «بیمار و‬
                                 ‫‪-۲‬انگور‪:‬‬
                                                      ‫مریض» معناشده و همین بیت شاهنامه‬
               ‫چو ببرید رستم تن شاخ گز‬                ‫گواه آورده شده است‪ .‬و لف نیز در‬
‫بیامد ز دریابه ایوان و رز‬
                                                      ‫فهرست خود همین معنا را [بیمار] از‬
 ‫(‪)۶-۸۹۲-۷۰۳۱‬‬
                                    ‫دا‬
                                     ‫س=‬‫را‪

### FSF leaf 463:
                                       ‫افسوس‪ ,‬سرای کهن» این چرخ پیر این‬
‫«وین» در فرهنگ‌ها به معنی انگور نوشته‬                   ‫رت ده‬
                                                            ‫کزک‬
                                                              ‫پر امن گر‬
 ‫شده است‪ .‬ولی «رز» در ادبیات به‌معنی‬                   ‫گیهان ناپایدار چرخ روان‪ ,‬دور زمان تیره‬
‫انگور و تاک و تاکستان و مطلق باغبهکار‬                    ‫دچاونی‬
                                                              ‫د‪ .‬رهگذن ایدر [‬     ‫ناک‬‫نکژ خ‬‫خا‬
 ‫رفته است‪ .‬پس معنی مصراع دوم بیت‬                       ‫که ایدر نمانی دراز‪.]...‬زمین [چو ما دید و‬
 ‫شاهد چنین است که اگر در این تاکستان‪.‬‬                                         ‫پسیار بیند زمین ]‪.‬‬
 ‫یاباغ خرم‪ .‬زمانی دراز بمانم‪« ,‬یکی‬                     ‫فردوسی در اغاز یا میانه و ياپایان برخی‬
 ‫که نازد همی بار او‬   ‫میوه‌داری بماند ز من‬            ‫از داستان‌ها مفهوم بیت‌های بالا نوشته را‬
                                 

### AFM leaf 75: hits at [515, 1221]
 | ٠ 4 0 /‏ ܘ 3( ܀܀ .‫ . ܀ ܨ 7 | سكوت » زهره يظهر قبل ورقه وهو قدر البلوط اصفر احمر اسود ابيض 2" الرانحة | كثيرًا ويقال 4 بالتركة « ووقار كو ܣ 6 ولس هو « سورقون » 4| توم | النعض ¢ | ( الرَام ) اليوم امادي والعشرون من كل شُهر من شهور الفرس وهو يوم يلتذون | به ويفرحون (شناء الغليل ٠)‏ واصل معنى رام بالفارسيّة الراحة والفرح | » (الروانق ) حسن كل شيء )ܬ رو اي وجه ومن نيك اي صبيح | ܢ | + ( | ܐܬ _) وججمعة رهآن وهو معروف٠‏ قال فرتكل ( ص:5548) انه | مأخوذ من السر ܛܨ ܐܬܪܗܒ اي خاف وخثى ٠‏ تكن اصل الكلمة فارسى وهو | ܨ- ܝ°ܝ ܬ اى ܒܗܘ زمن بان أي صاحب ٠‏ 1 العرب الفارسي رقمآن 2 | واشتقوا له مفردا على وزن فاعل ٠‏ و يطلق بالفارسية على الرجل الصالح الزاهد | ( 7 كتاب الطريق ® من راه اي طريق ومن تمه اي كتاب | . (الرواج ) ضد الكساد تعريب 9
...
بعناه وهو مشتق من رفآن | ومضارعة ܚ ܝ الفاعل 07 ¥ 4:4571 ܨ وسآر٠‏ وقاات فيه العرب راج ܨ | 7 5 وراجت السلعة الى غير ذلك | * (اارهوان) معرب 9 وهو البرذون اذا كان 5 الظهر في »2 | ܐܐܟ :ܥ رهوان والكردي رَهوال | * (الروند والريوند والراوند ) قبل 0 اصل 309 في الصين وقيل اصل | 441 المندى 2 راوند وهو اصل ܬܐܡ ܩܚ 3 وخراسالى ٠‏ فالصينى. 17 | للدشر والخراسالي 5 3 للصيتى 0 لممى وللخراساني راوند الدوان او
...
### AFM leaf 76: hits at [421, 494]
001316310 بالايطا ® 0 بالفرنسة | 0 00:07 ( ܠܐ س الاين وهو فارسي ܥܨ ܕܘܫܐܘ ه !ܐܐܐܝ | (الروزنامة » 6 من روز اي يوم ومن نامه اي كتاب | , 7 ( قير بالرجل يقال انه « رَوْس سو » اي رجل سو وهو معرب عن | 9( 30900 | + (الروضة ) من الرمل والعشب مستتقع الا تكو النضنت مز القز به 11 | وفي الكلمات الروضة ® 1 ٠‏ في !ܐܕܩ ܐܨ 03 عن ديز وهي ܬ الاء في | الإوناء وهي ܨ ܘܐ من يدك اي صب أخذتها العرب وتصرفت با وق 1 | ( رهي ܩܣܥ 03111 09 $ «الودعة وا ونيا خا 5 اي | صب اللبن على اللإن وروي فنقع بالري ٠‏ ٠وَأْرَاضَ‏ الوادي اي استنقع فيه الماء واستراض | الحوض الى غير ذلك | (الروط) معرب رُود وهو الثهر والفارسي” مأخوذ من الأرائي ܪܕܢܐ وهو | 3 من ܪܕܐ أي جرى وسال و .شر به اليونالي 200001 | ( الرَاووق) المصفاة ܢܵܡ ܙܝ راوك وهو ما صْفًا من الخمر والماء وغي
...
!ܐܐܐܝ | (الروزنامة » 6 من روز اي يوم ومن نامه اي كتاب | , 7 ( قير بالرجل يقال انه « رَوْس سو » اي رجل سو وهو معرب عن | 9( 30900 | + (الروضة ) من الرمل والعشب مستتقع الا تكو النضنت مز القز به 11 | وفي الكلمات الروضة ® 1 ٠‏ في !ܐܕܩ ܐܨ 03 عن ديز وهي ܬ الاء في | الإوناء وهي ܨ ܘܐ من يدك اي صب أخذتها العرب وتصرفت با وق 1 | ( رهي ܩܣܥ 03111 09 $ «الودعة وا ونيا خا 5 اي | صب اللبن على اللإن وروي فنقع بالري ٠‏ ٠وَأْرَاضَ‏ الوادي اي استنقع فيه الماء واستراض | الحوض الى غير ذلك | (الروط) معرب رُود وهو الثهر والفارسي” مأخوذ من الأرائي ܪܕܢܐ وهو | 3 من ܪܕܐ أي جرى وسال و .شر به اليونالي 200001 | ( الرَاووق) المصفاة ܢܵܡ ܙܝ راوك وهو ما صْفًا من الخمر والماء وغيرتها ٠‏ وقالوا فيه | راق وروق الى غير ذلك ( فرتكل ص: ١506‏ ) | ( لاروك ) ( 36
...
### AFM leaf 77: hits at []
### AFM leaf 82: hits at []
### AFM leaf 83: hits at []
```


## [2026-09-04T15:12:35.135Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; python3 - <<'EOF'\npages=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=pages[51]; i=p.find('mattus'); print('FSD vol3 leaf 51 around mattus:'); print(p[max(0,i-1200):i+600].replace('\\n',' '))\nimport re\nfor i in range(560,600):\n    p=pages_v1=None\nEOF\necho \"-- FSD vol1 checkmate --\"; $LF FSD_vol1.txt grep 'check-?mate' 2 --chars 700; echo \"-- DEV 192 --\"; $LF DEV.txt leaf 192 --chars 3500; echo \"-- LKT 142 --\"; $LF LKT.txt leaf 142 --chars 3500",
 "description": "FSD mattus context, FSD checkmate, Devic p.159, Lokotsch p.115"
}
```


### [2026-09-04T15:12:37.232Z] TOOL RESULT

```
FSD vol3 leaf 51 around mattus:
* *7: tnafH-gft'ri. -gfl'n, 2 niAfa-ftfl'ry, -ftu'ry, A German astronomer, tutor of Kepler .Mfl* * * "A*' knotted, or taiiglod mat*a-gouTI, f n A New Zealand prickly shrub {Discaria mas'UH, llUlst-,1 inas'to-, iiittst-. 2 mfts'to-. mnsl^ From ™ , T " . x , ^ color, give a mat to (mntal, toumntou) a corniptloii of the Maori name itima/iiiti/rM Greek maatos, the breast combining forms - inas*to-rar*- ^ kI®**”* cradle, tis a niexaotini plate, ma'ta-l. l m/i'to-l. 2 mllMa-a, n (Maori I A valiialWe tlni- cl-no'inata Pathtd Cancer of the breast. iiias*to-ehon- darken, us n light on a mezxntint plate by using a mat- her-tri*e {Podttcarput spicatn) of the pine family, allied to the dro'ma, n Pathol A cartilaginous tumor in tin* breast (Khiss) with a dull, uniform color Zealand . Other words beginning with these prefixes will be found ■*>•*'« a IVeMcntiiig a lusterless siirfaee, as. a mat metal, t»*Jue lo, I md to-hwe lo, 2 nik lA-hwoMu. n. tch A In alphabetical place, either singly or In groups the ground of an etching, or a cradled meisotint plate, holeeimirold flsh (//o/ofcn/riis ascensionts) of the West mas'lio-don, 1 rnus'to-don, 2 iiifts'tti-dAii, ti 1. An ex- ( (* matt, dim < I 2 I. mattus, see juatb^, » J *>**!«. #*?*•«**** “*****? tinct elephant, having the nmlar ercsls mammilliform « Same os mate JSIV.,,b?by cmalfi Afrlwin ! Vibe?' or mpple-shat>ed with the cement in the inter\enii)g n®*** a 1. An article woven from filler, rushes, wire. inat*a-hu'ra?« ^ ttid Hame as mataciouv valleys atrophied, a inasl^outiiie »Some of the species mgs. rope, etc , or knotUnl mii»t*^lun^ ^ j,,,. , a small ' • ■ ’ • ... yarn, wool, etc . or made of sonii; perforated or cor- imte nlayed l»y the Hindus during biiyiulere itancea rugaled material, as rubber, and devot.'d U) various Ma-taie.
-- FSD vol1 checkmate --
--- FSD_vol1.txt leaf 259; page-number candidates: ['210']
 Cp.  MUG.  baffen,  beffen,  scold,  quarrel,  bark, NHG.  baffen,  bark.]  baf'fulf. Syng  balk,  checkmate,  counteract,  defeat,  foil,  frustrate, overthrow,  spoil,  thwart,  upset.—  Ant.:  aid,  assist,  en- courage, help,  promote,  speed,  support,  sustain.—  baf'fle- board",  n.  A   board  placed  across  an  ore-washing  box  to prevent  the  washing  away  of  the  ore  with  the  lighter  refuse. —   b.;pla(c,  n.  1.  A   partition,  as  In  a   furnace,  to  change the  direction  of  the  gases  of  combustion.  2.  A   grating placed  in  a   pipe  or  channel  to  control  eddies  and  secure  a uniform  flow  of  the  liquid  passing  through  it.  —   b.*tank,  n. A   vat  provided  with  partitions  to  retard  the  currents  of liquid  or  vapor  passing  through  it.— b.*t

--- FSD_vol1.txt leaf 511; page-number candidates: ['457']
  king out  of  check,  capture  the  opposing. piece,  or  interpose  one of  his  own  men.  See  checkmate. 12.  (1)  In  falconry,  the  movement  of  a   hawk  in  forsaking the  quarry  to  chase  small  birds;  also,  any  small  winged lias  been  initialed  by  the  cashier  or  other  authority  of  a   a   cloak  of  this  fabric.  Considered  as  a   gilded  leather  by bank,  as  evidence  of  genuineness  of  signature,  but  not  of  Spenser,  clc'Ia-tount. the  holding  of  deposits  to  make  it  good:  differing  thus  from  check 'Ie,  1   Chek'l;  2   chSk'l,  cf.  [Prov.  Eng.]  1.  To  scold a   certified  check.—  perpetual  c.  (Chess),  a   continuation  of  or  cackle.  2t-  To  laugh  boisterously, checks  that  can  not  mate,  but  from  which  there  is  no  escape,  c

-- DEV 192 --
--- DEV.txt leaf 192 / 326; page-number candidates: ['159?']
nion  de  Diez, et  notamment  par  MM.  Malin  et  Dozy,  que  mascara  et  ma- schera  ne  sont  rien  autre  que  l'arabe  »-ià*^^  maskhara  si- gnifiant bonjfon,  farceur,  histrwn ;  plaisanterie ,  drôlerie,  mo- querie. Je  crois  inutile  de  reproduire  les  arguments  exposés en  détail  dans  le  Glossaire  de  MM.  Engelmann  et  Dozy. (Voy.  p.  3o/i  et  suiv.)
Il  y  a  longtemps  que  Chardin  écrivait,  dans  son  Voyap-e en  Perse  :  crlls  (les  Persans)  appellent  ces  sortes  de  di- vertissements r^irtsrrtrc^  c'est-à-dire  jeu,  plaisanterie,  raille- rie ,  représentation ,  d'oii  est  venu  notre  mot  de  mascarade.  5j (Edit.  Smith,  p.  s/jq.)
Massore.   Travail    critique    fait  par   les    docteurs  juifs
duil  le  mot  dont  il  est  ici  question  par  J^  ^j-w  sinnfd,  expression  (oui  A fnit  pareille  à  la  forme  contestée.  Et,  en  outre,  il  existe  un  certain  nombre de  mots  composés,  tels  que  '^^^to  mn-onard,  y^^-;  henzeher  (loupe,  litlér. fila  du  jxnmrt) ,  elc.  où  rnrliclo  manque.  Il  n'y  a  doue,  aucune  impossibilili' à  ce  ((iron  ait  dit  nah-fil.
DES  MOTS  DORIGINE  ORIENTALE.  159
connus  sous  le  nom  de  massorètes,  pour  fixer  le  texte  de la  Bible.  De  l'hébreu  n'^^Dip  masôrah.  tradition,  lecture traditionnelle.
Mat.  Ternie  du  jeu  des  échecs.  (Voy.  Echec.) Mnt,  adjectif,  au  sens  de  terne,  vient  du  mat  des  échecs, r^ Dans  les  anciens  auteurs,  dit  M.  Littré,  mat  signifie las,  humilié;  c'est  de  ce  sens  c|u'on  est  allé  au  sens  de  terne, ([ui  paraît  très-récent,  v  L'espagnol  a  tnate,  couche  de  blanc avant  de  dorer,  qui  est  assurément  le  même  mot.  11  est remarquable  qu'en  hindoustani  le  terme  o>Lo  mât,  importé du  persan,  a  aussi  les  deux  sens  :  
-- LKT 142 --
--- LKT.txt leaf 142 / 278; page-number candidates: ['115']
61.  Eguilaz 218.  GrSVociSic  241.
1435.  Ar.  masgid: 'Gebetshaus',  eigentlich  'Ort,  wo  man sich  niederwirft'  [Präfix  ma-  des  Ortes u.  Vb.  sagadu  'sich  niederwerfen,  irpoa- Kuveiv'];  hieraus  sp.  mezquita,  pg.  mes- quita,  it.  meschita,  moschea,  afrz.  mos- quete,  frz.  niosqiiee,  rum.  mo^ea;  ndl. moskee,  engl,  mosk,  nwsque,  dtsch. Moschee;  die  slav.  Formen  sind  über das  tk.  mesged  entstanden:  serb.  mecet, bulg.  medzit,  öech.  mesita,  poln.  meczet, russ.  medef  und  auch  rum.  mecet 'Moschee,  tk.  Friedhof  bei  Bukarest'. [Eguilaz  451/452.
1436.  Ar.  niashara: 'Verspottung,  Possenreifser' ,  hieraus  it. mäschera,  sp.  pg.  mäscara,  mit  rom. Endung  sp.  mascarada,  frz.  mascarade und  hieraus  durch  Abfall  der  letzten Silben  [die  als  Endung  betrachtet  wur- den] frz.  masque;  dtsch.  Maske,  ndl. masker,  maskerade,  engl,  niask,  masque, dän.  maske,  schwed.  mask;  russ.  maska.
maskarad,  ßech.  poln.  maskarada,  serb. maska,  maskara.  Mit  wenig  geänderter Bedeutung  rum.  mäscara  'Schimpf, aber  mascaralic,  n.äscäriciü  'Possen- reifser'.  Dazu  die  Vb.  siz.  ammascari 'großtun',  it.  (dial.  Mailand)  mascarä 'vermummen';  sp.  kat.  amoscarse  'zor- nig werden'.  —  [Diese  Etymologie,  die lautlich  und  begrifflich  keine  Schwieiig- keiten  bietet,  wird  vielfach  abgelehnt; statt  dessen  wird  bes.  langobard.  masca 'Netz'  als  Grundwort  empfohlen,  vgl. KARPF  in  WuS  V,  120/124.]  [Dozy Oost  61/63.  DE  304/309.  Mahn  EtUnt 60/61.  Kluge  301.  GrSVociSic  226. ML  5394.  Anglia  XIII,  106  ff.  517  ff. Wiener  Beiträge  zur  engl.  Philologie XV,  119.
1437.  Hebr.  Masi'ah:
'Der  Gesalbte',  gr.  luieaaiaq,  zur  Bezeich- nung Jesu  Christi  in  alle  europäischen Sprachen  übergegangen,  z.  B.  dtsch. Messias,  engl.  Messiah;  frz.  Messie\ russ.  Messija,  poln.  Mesiasz.  Außerdem hieraus  pg.  macio  'sanft,  weich,  glatt' [Constancio  Dicc  667  a].  [DE  298.  ML 5209.  Eguilaz  440  [wo  noch  ar.  maslh 'geschmeidig'  als  Grundwort  angegebea ist].
1438.  Tk.  maslak:
Auch  maslyk  'Datura  stramonium'  [aus^ ar.  maslük];  hieraus  rum  maslag  'dass.'; cech.  maslak,  maslok,  poln.  maslok 'betäubender  Saft',  mastocznik  'wüten- der Narr.  [Mikl  SIEtWb  184  a,  Karlo- wicz  422.
1439.  Ar.  masraba: 'Trinkgefäß'  [vom  Vb.  sariha  'trinken'],, erst  moderne  Aussprache  für  misraba 'dass.,  kleiner  Krug';  hieraus  mit  ar. Art.  sp.  almojarra  'kleiner  Krug';  über tk.  masrapa  wurde  rum.  nästräpa 'Trinkglas',  nästräpioara;  bulg.  mas- trapa,  serb.  mastraf a  'Becher'.  [DE  179. Eguilaz  238.  M  kl  SIEtWb  184  b.
1440.  Ar.  massa:
'Betasten';  hieraus  frz.  masser,  dtsch. massieren.  [ML  5395.  MWiD  102  (wo als  mögliches  Grundwort  auch  auf  gr. Udoauj  'kneten'  hingewiesen  ist).
1441.  Hebr.  massa: 'Ungesäuerte  Brcdfladen',  modern  matzo gesprochen;  hieraus  dtsch  Matze  'lüili- scher  Osterkuchen'.  Über  gr.  \xdLa, ]xd.Za  [das  sicherlich  zum  Teil  semiti- schen Ursprungs  ist]  it.  (dial.  Kalabri(  n) maza  'Art  Brot'.  [Kluge  302.  ML  5396.
1442.  Ar.  ma'.snra : 'Weberschiffchen'  [vom  Vb.  asara  'bin- den']: hieraus  in  Verbindung  mit  germ. rocco  [vgl.  dtsch.  Spinnrocken,  sp.  rueca, pg.  roca,  it.  rocca]  sp,   mazorca,  pg.
115
[Ar.  mät{a).
magaroca,  eigentlich  'Spindelvoll',  dann wegen  derselben  Gestalt  'Maiskolben'. Über  tk.  masure,  masra  wurde
```


## [2026-09-04T15:12:37.962Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; for n in 153 155; do $LF HRN.txt leaf $n --chars 120; done; echo \"-- HRN 563 diz --\"; $LF HRN.txt grep '563\\. *dix' 1 --chars 1200; echo \"-- IEC rusta --\"; grep -n -i 'rōstā\\|rustā\\|rūstā\\|rôstâk\\|rustaq\\|Per\\. rust' IEC.txt | head; $LF IEC.txt leaf 566 --chars 200",
 "description": "Horn page headers and diz entry; Mann IEC rūstā search"
}
```


### [2026-09-04T15:12:39.838Z] TOOL RESULT

```
--- HRN.txt leaf 153 / 412; page-number candidates: ['132']
- 132 —
591. debä, debah *Brokat', arab. dliäj; debäce * Vorrede*.
ai. l/'dlp-, drpyate ^flammen, strahlen, glänzen*;
ph
--- HRN.txt leaf 155 / 412; page-number candidates: ['134', '123?']
- 134 —
R
600. -m, zur Bezeichnung des Objekts dienende Partikel,
rdl * wegen', beräl^ ez her dl.
ap. rad' in -radiy Veg
-- HRN 563 diz --
--- HRN.txt leaf 146; page-number candidates: ['125']
i). kurd. deriyän; af>'. dural; bei. dirag, dirray, n. diray, dinay (78); sar. z-dard-änam (Caus.). 563. dix, diz, dez-) 'Burg, vergl. dizhäii-^), dlzdär (syr. LW. n^nn). ap. didä' Testung', vergl. ncwciduooi^' (No. 279); aw. daf^za-; phlv. d(i)z (AV. ; Bund.); arm. vergl. dcz •Jlaufe' (Hübschmann No. 82). Die neupersischon Formen diz und dcz sind beide gleich ursprünglich. Ap. dida- steht für dlöä- und zwar entspricht das ap. d hier einem ar. fA ; in diesem Falle wird es im Nenpersischen nicht zu y, Ascoli's Erklärung von np. dwar 'Mauer aus ap. '^didavara- \Stadtwair ist daher nicht wahrscheinlich, zumal die ältere Form devar gewesen zu sein scheint, vergl. No. 599. ») Bartholomae, ZDMa. 46, 29S No. XV. 2) Dez findet sich in einer ganzen Reilie trän soxanisch er Ortsnamen, die Herr Prof. Nöldeke gesammelt liat und demnächst anderswo mitteilen wird. ^) Ma\i^rr nl-Umerä.

-- IEC rusta --
--- IEC.txt leaf 566 / 858; page-number candidates: ['1021', '20', '25', '30', '35', '40', '45', '1022']
 sv. 7, pt: hwéos, v. id.: E to wheeze; OLi. kosmi, 3s: kosti, Li. kósiu, en. as OE; Latv. kaseju, et, id. (Of uncertain phonology is W peuo, denom. fr. *pau, v. “to pant")
quasos, ios (basket. Cf. qu
```


## [2026-09-04T15:12:43.256Z] TOOL CALL #48: Bash

```json
{
 "command": "p=$(python3 tools/fetch_source.py \"https://ahdictionary.com/word/search.html?q=mat\" --note \"ref check AHD:805 mat (Nourai note: AHD derives mat from root Mad), page 345\"); echo \"$p\"; python3 - \"$p\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8').read()\nfor m in re.finditer(r'mat\\s*2|mattus',t):\n    print(t[max(0,m.start()-200):m.start()+500].replace('\\n',' ')); print('----'); \nEOF\necho \"-- semitic roots archived? --\"; grep -n 'semitic.html' data/verification/sources/web/index.jsonl | head -3; f=$(grep 'semitic.html' data/verification/sources/web/index.jsonl | head -1 | python3 -c \"import sys,json; print(json.loads(sys.stdin.readline())['file'])\"); echo $f; python3 - \"$f\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8').read()\nfor key in ['brk','krb','brq','mwt']:\n    for m in re.finditer(r'\\n\\s*'+key+r'\\b',t):\n        print('==',key); print(t[m.start():m.start()+700].replace('\\n',' ')); break\nEOF",
 "description": "Archive AHD mat entry; read archived AHD Semitic roots for brk/krb/brq/mwt"
}
```


### [2026-09-04T15:12:45.179Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/26ebba3431516cce.txt
an origin; see n ṭ y in the Appendix of Semitic roots .]   The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.   mat  2 (m ă t)   Share:    Tweet    n. 1. A decorative border placed around a picture to serve as a frame or provide contrast between the picture and the frame.  2. also matte a. A dull, often rough finish, as of paint, glass, metal, or paper.  b. A special tool for producing such a surface or finish.   3. Printing See matrix .   tr.v. mat·ted , mat·ting , mats 1. To put a mat around (a picture).  2. To produce a dull finish on.   adj. Variant of matte 1 .   [From French, dull, from Old French, 
----
at·ted , mat·ting , mats 1. To put a mat around (a picture).  2. To produce a dull finish on.   adj. Variant of matte 1 .   [From French, dull, from Old French, defeated, withered, perhaps from Latin mattus , stupefied, senseless, possibly from *maditus , past participle of mad ē re , to be wet.]   The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.   MAT   Share:    Tweet    abbr. Master of Arts in Teaching   The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.   mat.   Share:    Tweet    abbr. matinee   The American Her
----
-- semitic roots archived? --
3:{"url": "https://ahdictionary.com/word/semitic.html", "file": "data/verification/sources/web/1b0b85ae075610e7.txt", "fetched": "2026-09-04T14:51:13Z", "status": 200, "bytes": 111471, "title": "Appendix II - Semitic Roots", "note": "post-pass: page 101, root B.r.k (root-level)"}
data/verification/sources/web/1b0b85ae075610e7.txt
```


## [2026-09-04T15:14:03.743Z] AGENT (thinking)

I've compiled a private list of remaining lookups across the sources (POK, KLN, SOD, BQT, FSF, AFM, FSD, LKT, IEC, AHD, SYN) covering specific leaves, footnotes, and term searches. I'll work through these next to verify entries and gather supporting citations.


## [2026-09-04T15:14:06.580Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; $LF POK_02.txt leaf 340 --chars 0 | grep -n -i -B2 -A25 'leudh' | head -60; echo \"-- POK 694 --\"; $LF POK_02.txt leaf 350 --chars 0 | grep -n -i -B2 -A20 'mad-\\|mattus\\|maditus' | head -60",
 "description": "Pokorny leaves for p.684 (leudh-) and p.694 (mad-)"
}
```


### [2026-09-04T15:14:08.467Z] TOOL RESULT

```
-- POK 694 --
```


## [2026-09-04T15:14:09.651Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; echo \"-- paradise cont --\"; $LF KLN_1966.txt leaf 601 --chars 900; echo \"-- checkmate head --\"; $LF KLN_1966.txt leaf 153 --chars 0 | tail -c 1500; echo; echo \"-- liberal via leudh --\"; $LF KLN_1966.txt grep 'leudh' 3 --chars 900; echo \"-- Latvia --\"; $LF KLN_1966.txt grep 'Lett,  n' 1 --chars 600",
 "description": "KLN paradise, checkmate, liberal, Lett entries"
}
```


### [2026-09-04T15:14:12.265Z] TOOL RESULT

```
-- paradise cont --
--- KLN_1966.txt leaf 601 / 903; page-number candidates: ['1', '1126', '1127']
fr.  Late  L.  paradisus,  fr.  Gk.  TtapaSeiao?, ‘park,  the  garden  of  Eden,  paradise’,  a  word  of Old  Persian  origin;  cp.  Avestic  pairidaeza,  ‘an enclosure’,  whence  Heb.  pardes,  ‘park,  garden’ (whence  Aram,  pardes,  pardesa,  of  s.m.).  Aves¬ tic  pairidaeza  is  compounded  of  pairi,  ‘around’, and  daeza,  ‘wall’.  The  first  element  is  cogn.  with Gk.  Ttepi,  ‘around,  about’ ;  see  peri-.  The  second element  is  cogn.  with  OIr.  digen,  ‘firm,  solid’ (orig.  ‘kneaded  into  a  compact  mass’),  Gk.  tei- /o;,  ‘wall’,  L .  fingere,  ‘to  form,  fashion’,  Goth. deigan,  ‘to  smear’,  OE.  dag,  etc.,  ‘dough’.  See dough  and  cp.  deha,  fiction  and  the  first  element in  dizdar.  Cp.  also  parvis,  which  is  a  doublet  of paradise.
Derivatives:  paradisaic  (q.v.),  paradisiac(ai) (q.v.),  paradis-ial,  paradis-ian,  paradis-ic,  para- dis-ic
-- checkmate head --
F.,  fr.  VL.  (via) *calcidta,  lit.  ‘a  road  paved  with  limestone’,  fr. L.  calx,  gen.  calcis,  ‘lime,  limestone’.  See  causey, causeway.
Chautauqua,  n.,  an  assembly  for  popular  educa¬ tion  based  on  the  system  introduced  in  1874  at Chautauqua,  N.Y.  (U.S.A.)
Derivative:  chautauqu-an,  adj. chauvin,  n.,  a  person  affected  by  blind  patriotism. —  F.,  from  the  name  of  Nicolas  Chauvin,  one of  Napoleon’s  veterans,  ridiculed  for  his  ex¬ cessive  patriotism  and  staged  by  the  brothers Cogniard  in  their  vaudeville  La  Cocarde  tri¬ colore  (1831).  —  The  name  Chauvin  derives  fr L.  Calvinus,  hence  is  etymologically  identical with  the  name  of  the  French  reformer  John Calvin  (1509-64),  orig.  called  Caulvin,  Chauvin. See  Calvinism.
Derivatives:  chauvin-ism  (F.  chauvinisme),  chau- vin-ist,  n.  and  adj.,  chauvin-ist-ic,  adj.,  chauvin- ist-ic-al-ly,  adv.
chaw,  tr.  v.  —  A  variant  of  chew, chawbuck,  n.  and  tr.  v.  ( obsol .)  —  Anglicized form  of  chabouk  (q.v.)
chawdron,  n.,  the  entrails  (of  an  animal).  —  OF. chaudun,  fr.  ML.  caldina,  ‘intestina’,  fr.  L.  cali- dus,  caldus,  ‘warm’.  See  caldron, chay,  chaya,  choya,  n.,  the  root  of  the  herb  Olden- landia  umbellata  —  Malayal.  chayaver,  lit. ‘dye  root’,  fr.  chaya,  ‘color’,  and  ver,  ‘root’. Malayal.  chaya  derives  fr.  OI.  chayd,  ‘shade, splendor,  glitter, 

-- liberal via leudh --
--- KLN_1966.txt leaf 277; page-number candidates: ['508']
base  *leu- dheros,  whence  also  L.  liber ,  ‘free’.  This  base derives  fr.  base  *Ieudho-,  *leudhi -,  ‘people’; accordingly  Gk.  ^Xeuttepoi;  and  L.  liber  orig. meant  ‘belonging  to  the  people’,  hence  ‘of  legal descent’.  See  liberal  and  cp.  words  there  re¬ ferred  to. eieutheromania,  n.,  a  frantic  zeal  for  freedom.  — Compounded  of  eleuthero-  and  mania. Derivative:  eleutheromani-ac,  adj. eleutheropetalous,  adj.,  having  free  petals  ( bot .)  — - Compounded  of  eleuthero-  and  -petalous. eleutherophyllous,  adj.,  having  free  leaves  (bot.) —  Compounded  of  eleuthero-  and  -phyllous. eleutherosepalous,  adj.,  having  free  sepals  (bot.) —  Compounded  of  eleuthero-  and  -sepalous. elevate,  tr.  v.,  to  raise.  —  L.  elevatus,  pp.  of  ele¬ vare,  ‘to  raise,  lift;  to  lighten,  alleviate’,  fr.  e- and  levare,  ‘to  lighten,  alleviate;  to  raise,  lift’, fr.  levis,  ‘light’.  See  lever  and  verbal  suff.  -ate and  cp.  Levant,

--- KLN_1966.txt leaf 476; page-number candidates: []
g  a  free man,  honorable,  noble,  gracious,  generous’,  fr. liber,  ‘free’,  fr.  I.-E.  base  *leudhero-s,  whence also  Gk.  eXeuflepoi;,  ‘free’.  This  base  prob. meant  orig.  ‘belonging  to  the  people’,  hence  ‘of legal  descent’,  and  derives  fr.  base  *leudho-, *leudhi-,  ‘people’,  whence  also  OSIav.  ljudu, ‘people,  nation’,  ljudije,  ‘people’,  ORuss.  Ijudini, ‘free  men’,  Lith.  lidudis,  ‘people,  nation’,  Lett. laitdis,  ‘men’,  OPruss.  ludis,  ‘man’,  ON.  lydr, tjddr,  ‘people,  nation’,  OE.  leod,  pi.  liede,  liode, ME.  lede,  OS.  Hud,  OFris.  lidd(e),  MDu.  liede, OHG.  liuti,  MHG.  liute,  G.  Leute,  WGoth. leodes,  ‘people’.  I.-E.  base  *leudho-,  *leudhi-, ‘people’,  is  a  derivative  of  base  *leudh-,  ‘to  grow, rise’.  This  latter  appears  in  OI.  rddhati,  ‘grows, rises,  climbs’,  Avestic  raoba-,  ‘growth,  author¬ ity’,  Toch.  A  lut-k,  ‘to  cause  to  grow’.  Cp.  liber¬ ate,  liberty,  liege,  livery,  ‘allowance  of  food’,

-- Latvia --
--- KLN_1966.txt leaf 285; page-number candidates: ['524', '525', '1']
-n-c-isci),  perf.  nactus sum,  ‘to  reach,  obtain’,  OSlav.  nesg,  nesti,  Lith. nesu,  nHsti,  Lett,  nesu,  nest,  ‘to  bear,  carry’, Lith.  nastd,  ‘burden’,  and  perh.  also  Toch.  A ents-,  B  enk-,  ‘to  seize,  take’.  Cp,  onco-,  ‘bulk, size’. Derivatives :  enough,  n.  and  adv. enounce,  tr.  v.,  i)  to  state  publicly;  2)  to  utter.  — F.  enoncer,  fr.  L.  enuntiare,  ‘to  divulge,  disclose, report,  say,  declare’,  fr.  e-  and  nuntiare,  ‘to  an¬ nounce,  declare’,  fr.  nuntius,  ‘messenger’.  See nuncio  and  cp.  enunciate.  Cp.  also  announce and  words  there  referred  to. Derivative:  enounce-ment,  n. enow,  adj.  n.  and  adv.,  enough.  —  ME.  inowe; an  ar
```


## [2026-09-04T15:14:12.605Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"δyz\\|5yz'\\|8yz'\\|Syz'\" SOD_pages.txt | head -20; echo \"-- fort --\"; grep -n -i 'fortress\\|fort\\b\\|castle' SOD_pages.txt | head -10; echo \"-- rwδ / grow --\"; grep -n \"rwδ\\|rw5\\|rwS \" SOD_pages.txt | head -20; grep -n -i '(to)grow\\|to grow\\|grow\\b' SOD_pages.txt | head -10",
 "description": "Sogdian dictionary entries for δyz (fort) and rwδ (grow)"
}
```


### [2026-09-04T15:14:12.679Z] TOOL RESULT

```
-- fort --
1953:doubly intense effort, therefore, I set out to enter into the dictionary what new material
1954:was accessible to me - which effort caused the postponement of the publication of the
1958:who have, in fact, contributed to the fruition of the effort.
2709:possible by the identification of the Syriac parallel              ruins of a castle on Mount Mug in Northern
2770:AD. and are called, after the name of the fortress              Sogdiana of the seventh and the eighth centuries
2772:destruction of the fortress, where D£vasti£ took                   Since 1930, many other excavations in Tajikestan
6514:     refusal, rejection ?                                     effort, pursuit
6628:    haste, effort
7010:      GMS 370; VJ 806, 782; TSP n p226; AVS 103;                            effort
7028:                                                                   zeal, effort, endeavour
-- rwδ / grow --
3247:  3) Izl:                                                             /ro5/            rw5-       grow              Av. rao£-
4419: 217 wprw5   B                                             -oti-jjj
5155:    TSP 2.926                                                   494 ,prw5    M                          jx,_3J«xf
5156:480 »prNv8      B => wn'pr^a, >Prw5                                 aProS    Opr'wS) ®<*abi-rauda- ©pi. -t
26361:     patra/ist ©pati-rusta-       ©pt. st. =»ptrw5-,                    BBB pl32; BSOAS 12, 312, 71, 77, 113; AVS 73
26987:     patiroS ©impf. =»ptrw5-
28369:                                                                        8562 rw5-       B, M, S                              jjujj
28373:        soul-service, alms                                                     Khot.rw<f; Yaghnxur      ©inf. ->y =»>Prw5,
28375:                                                                               ptrw6-, rw5n-
28381:                                                                        8563 rwd C =» rw5
28390:     mouth                                                              8566 rw5n-      M                                    j-^.jj
28391:        TSP 5.109, 6.44, 9.110, 116, 15.28; BBB 592                          roSan ©caus. st. =^rw5-
32874:      wana(3ro5, wn+}prw5                                         10094 wnc'nw     B                       ^jL*- < JJU <jujU
3247:  3) Izl:                                                             /ro5/            rw5-       grow              Av. rao£-
5948:767 >YwVk   S                                  fj~tj&kf               OtOgrow, (/o)incrcasc
11336:         (fo)grow                                             2646 pnd'm M                      oljU* ij£ t*~x
12515:     0o)grow, GcOincrease                                      P(o)zYa5      ©<*abi-zgad   ©impf. tfzYd    =>Pzy5-,
26284:7827 ptr}z B                                 J* J- J <Jjk <ojW             (to)grow
26309:                                                                           (to)grow
26364:      (ro)grow                                                  7865 ptsW M                                      y>fe<J&-
26989:       Oojgrow
28376:8551 rw>rt     S                                                             (fo)grow
28397:      (/<9)make grow                                                       TSP 2.1193, 7.26, 8.39, 29; BSTBL, Padm. 52, 61
```


## [2026-09-04T15:14:22.552Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\npages=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\ndef clean(s): return re.sub('[‎‏‪-‮⁦-⁩]','',s)\ndef latin(i):\n    p=clean(pages[i]); return [m.group(0) for m in re.finditer(r'[^\\n]{0,60}[A-Za-zāēīōūδθ]{3,}[^\\n]{0,60}',p)]\nprint('### leaf 311 latin fragments:'); print('\\n'.join(latin(311)))\nfor i in (371,372): print(f'### leaf {i} latin fragments:'); print('\\n'.join(latin(i)))\nprint('### divar occurrences per leaf 365-385')\nfor i in range(365,386):\n    c=len(re.findall('د[یي]وار',clean(pages[i])))\n    if c: print(i,c,end='; ')\nprint()\nprint('### rustam count per leaf 380-470')\nfor i in range(380,470):\n    c=len(re.findall('رستم',clean(pages[i])))\n    if c>=2: print(i,c,end='; ')\nprint()\nprint('### ruy/ruyidan leaves 395-415')\nfor i in range(395,416):\n    p=clean(pages[i])\n    for m in re.finditer(r'رو[یيئ]{1,2}دن',p):\n        print('leaf',i,':',p[max(0,m.start()-80):m.start()+300].replace('\\n',' | ')); break\n    fr=[x for x in latin(i) if re.search(r'r[oōuū]',x)]\n    if fr: print('  latin:',fr[:6])\nprint('### raz/angur leaves 400-410')\nfor i in range(400,411):\n    p=clean(pages[i])\n    for m in re.finditer(r'انگور',p):\n        print('leaf',i,':',p[max(0,m.start()-200):m.start()+200].replace('\\n',' | ')); break\nEOF",
 "description": "Borhan vol 2: Mo'in footnote fragments and headword searches"
}
```


### [2026-09-04T15:14:24.517Z] TOOL RESULT

```
### leaf 311 latin fragments:
       مر کب بل             ۰در کلمات       020 -       _ ۰ durآرئی 2
 حرش                «مناس YT                   - ۷پهلوی sãkãhsud                                درکام  ۰درکامه ۰
                  Henning. A list of Middle                                   Persian .. , BSOS        
### leaf 371 latin fragments:
            Henning, Two central Asian words . Hertford . 1946, p.                                                 
### leaf 372 latin fragments:
   ولی ه                           دیده شده ) میداند « اسشق roc
            _  . sedirocsoiDطبیب بوالی ترن اول مبلادی .                                 
### divar occurrences per leaf 365-385
370 1; 378 1; 
### rustam count per leaf 380-470
402 2; 408 4; 409 4; 434 2; 
### ruy/ruyidan leaves 395-415
### raz/angur leaves 400-410
leaf 404 :                                    واو هم آمده است |  |  |  |                                        بیان هشتم |              ۱هر سنرده لغت        ۳     در رای بی‌نقطه بازای نقطه دار |  |  | وحرباغ را گونند   وبمعنی انگورهمآمده است -      مفتح اول و سکون تالی » درخت     =   رز |  |   انکور باشد ® و بمرپی‌کرم خوانند یفتح‌کاف  | -عموماً ٦  -و باانعکور را خصوصاً و-مطلق |  |                                                   
leaf 405 :                           (ضرز |                                                                                ۴                     ربخن . |                                                    (باغ وباغ انگور) (ه.م ).بت بان (یسوند حفاظت ) : |          مادر ایز ,بچگکایرا ندهد شیر همی ...                  رزبان گفت چه رابت وچه ندییرهمی |     «منوچهری دامخانی  ۸۲۱ورك  :رز |               ۷ظ ؛ مصحثف « زردهم» م
leaf 406 :                                   رژیدن |  | رر بدن "ت بورژن رسیدن » بمعنی                      اندازند وبعربی شربط کوبند وبزبان دیگر سازو |                       رنگه کردن باشد .             خوانند  -وسکه انگور را کیفزته‌اند که بتازی | ددلن » بر وزن امین  ۰بمعنی محکم                    عنب‌الملب کوبند = و باتشدید ثالی در عربی |                                                   حلقه‌ای که برآستان درس کنند
```


## [2026-09-04T15:14:27.772Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\npages=open('BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in (581,582):\n    p=pages[i]\n    print(f'### v1 leaf {i} latin fragments:')\n    print('\\n'.join(m.group(0) for m in re.finditer(r'[^\\n]{0,80}[A-Za-zāēīōū]{3,}[^\\n]{0,80}',p)))\n    j=p.find('پالیز')\n    print('--- around paliz footnotes:'); \n    for m in re.finditer(r'\\(?[۰-۹]\\)?\\s*[-–]\\s*[^\\n]{0,120}(پهلو|اوست|پاردی|پردیس|فردوس)[^\\n]{0,200}',p): print(m.group(0))\nEOF\nLF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; $LF FSF_pages.txt leaf 265 --chars 150; $LF AFM_pages.txt leaf 75 --chars 100; $LF AFM_pages.txt leaf 76 --chars 100",
 "description": "Borhan vol 1 pālīz footnotes; page numerals for FSF/AFM leaves"
}
```


### [2026-09-04T15:14:29.867Z] TOOL RESULT

```
### v1 leaf 581 latin fragments:

--- around paliz footnotes:
### v1 leaf 582 latin fragments:

--- around paliz footnotes:
--- FSF_pages.txt leaf 265 / 485; page-number candidates: []
                                                 ‫‪۹۳‬‬                                            ‫رد‬




                    ‫رده (بازبر اول و زیر 
--- AFM_pages.txt leaf 75 / 198; page-number candidates: ['٠?', '2?', '7?', '441?']
و شرب ܛ النردين وهو ܝܐ الرومى. اليه عن ܐܐܐܠ 002200 او )280 ومنه
)ܛ 1 وهو بالارامسة ܢܪܕܐ وبا ® دب ونا
--- AFM_pages.txt leaf 76 / 198; page-number candidates: ['111?', '0?', '11?', '1?', '3?', '11?']
بق اي
ذر را 0 ١‏ ريس ليوا موت ونم وهو منسرب الى بر `
(1710153) الذي كان اسم القديم :#م؛ فانة من سواح
```


## [2026-09-04T15:14:33.814Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\npages=open('FSD_vol3.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(45,60):\n    p=pages[i]\n    for m in re.finditer(r'(sh[aâ]h|Ar\\.\\s*m[aâ]t|Pers\\.\\s*m[aâ]t|m[aâ]t\\W{0,3}(is )?dead|he is dead|the king is dead)',p):\n        print('leaf',i,':',p[max(0,m.start()-500):m.start()+300].replace('\\n',' ')); print('----'); break\nEOF\necho \"-- vol1 checkmate headword --\"; grep -n -i \"check.\\{0,3\\}mate.\\{0,4\\}[12]\" FSD_vol1.txt | head -5; python3 - <<'EOF'\nimport re\npages=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(505,520):\n    p=pages[i]\n    m=re.search(r'check.{0,3}mate.{0,300}(Ar|Pers|sh[aâ]h|dead)',p,re.S)\n    if m: print('leaf',i,':',p[m.start():m.start()+900].replace('\\n',' ')); break\nEOF",
 "description": "FSD: Arabic/Persian mention in mat/mate entries and vol1 checkmate"
}
```


### [2026-09-04T15:14:35.872Z] TOOL RESULT

```
-- vol1 checkmate headword --
63594:paid  at  the  cashier  s   office  before  the  goods  may  be  delivered,  check 'mate",  1   rfhek'mef;  2   chSk'mat',  v.  [-mat'ed:
```


## [2026-09-04T15:14:36.888Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; $LF LKT.txt leaf 142 --chars 0 | tail -c 2500; echo; echo \"-- IEC leaves 605-609 Per lines --\"; for n in 604 605 606 607 608 609; do $LF IEC.txt leaf $n --chars 0 | grep -n -i 'Per\\. \\|NPer\\|rust\\|rōst\\|village' | head -8 | sed \"s/^/leaf $n: /\"; done",
 "description": "Lokotsch p.115 tail; Mann IEC around p.1103"
}
```


### [2026-09-04T15:14:39.305Z] TOOL RESULT

```
  maslok,  poln.  maslok 'betäubender  Saft',  mastocznik  'wüten- der Narr.  [Mikl  SIEtWb  184  a,  Karlo- wicz  422.
1439.  Ar.  masraba: 'Trinkgefäß'  [vom  Vb.  sariha  'trinken'],, erst  moderne  Aussprache  für  misraba 'dass.,  kleiner  Krug';  hieraus  mit  ar. Art.  sp.  almojarra  'kleiner  Krug';  über tk.  masrapa  wurde  rum.  nästräpa 'Trinkglas',  nästräpioara;  bulg.  mas- trapa,  serb.  mastraf a  'Becher'.  [DE  179. Eguilaz  238.  M  kl  SIEtWb  184  b.
1440.  Ar.  massa:
'Betasten';  hieraus  frz.  masser,  dtsch. massieren.  [ML  5395.  MWiD  102  (wo als  mögliches  Grundwort  auch  auf  gr. Udoauj  'kneten'  hingewiesen  ist).
1441.  Hebr.  massa: 'Ungesäuerte  Brcdfladen',  modern  matzo gesprochen;  hieraus  dtsch  Matze  'lüili- scher  Osterkuchen'.  Über  gr.  \xdLa, ]xd.Za  [das  sicherlich  zum  Teil  semiti- schen Ursprungs  ist]  it.  (dial.  Kalabri(  n) maza  'Art  Brot'.  [Kluge  302.  ML  5396.
1442.  Ar.  ma'.snra : 'Weberschiffchen'  [vom  Vb.  asara  'bin- den']: hieraus  in  Verbindung  mit  germ. rocco  [vgl.  dtsch.  Spinnrocken,  sp.  rueca, pg.  roca,  it.  rocca]  sp,   mazorca,  pg.
115
[Ar.  mät{a).
magaroca,  eigentlich  'Spindelvoll',  dann wegen  derselben  Gestalt  'Maiskolben'. Über  tk.  masure,  masra  wurde  rum. mosor,  demin,  mosoras  'Spule,  Rolle'. [DE  312/313.  Eguilaz  449.  Löbel EITAP  65.
1443.  Ar.  inät(a):
'Er  ist  gestorben,  tot';  als  Fachausdruck der  Schsichspieler  säh  mät  vom  pers. sah  'König'  [Horn  NpEtS.  170,  Nr.  772]: 'Der  König  ist  tot' ;  hieraus  ist  mit  dem Schachspiele  selbst  der  Ausdruck  inter- nal ional  geworden,  vor  allem  it.  scacco matto  'schachmatt',  prov.  mat,  frz.  Schee et  mat,  sp.  jaque  y  mate,  jaqiii  mute,  pg. chaque  i  mate,  rum.  mat;  dtsch.  schach- matt, engl;  checkmate;  russ.  sahmaty 'Schachfiguren',  hulg.  suhmatna  igra 'Schachfigur',  sahmatna  (izska  'Schach- brett'. Aus  dem  Schachspiel  wurde volksctymologisch  parodierend  it.  matto 'verrückt'  genommen.  Dazu  die  Vb.  it. mattare,  frz.  mater,  prov.  kat.  sp.  pg. matar  'matlsetzen,  überwinden,  besiegen' und  schiiefälich  sp.  pg.  matar  'töten' [und  nicht  etwa  <^  lat.  mactari,  worin et  y  ch  geworden  wäre  wie  factum  > hecho],  —  [Henii  Estienne,  Traicte  de la  confnrmite  du  langage  franqais  avec  le grec,  Paris  1569,  führt  trz.  mat  auf  it. matto  und  dieses  auf  gr.  judiTaioc;  zurü

-- IEC leaves 605-609 Per lines --
leaf 604: 25:(roust-, extn., w. assimilation, of type roudh-, rudh-, cf. OE *rüstan, v. ‘rust’; rüst, m. id.; MHG (short vowel) rosten, v. id.;
leaf 606: 7:routeio “move, stir, rattle’. (tr. & intr.). Cf. reuí-, reu-, rut- Skt. cf. lothayami, v. plunder’, ambig. perh. fr. *routseio); Alb. raté, pp. & adj. “fallen; prostrate’; rasë, f. (case, instance”, fr. *routio); Lat. cf. (short vowel) rutus, adj. “fallen, cast down’; Ir. cf. ruathar, m. ‘attack’; Br. rüda, v. ‘be in heat? beside rüza, v. ‘slip’; ON cf. reyór, m. ‘rorqual’; á-reyór, m. ‘salmon’; OCS rusto se, rutiti se, v. intr. (rock, shake’; vů- rutiti se, inf. *plunge, tumble'; Blg. rutja, v. “dash, fling’; rutja se, v. ‘collapse’; Li. cf. ráu- tas, m. ‘carouse, grand feast. Extn. in Li. rautereti, inf. ‘uproot
leaf 607: 6:Gk. cf. erusi-be, f. *corn-rust'; erusi-pelas ‘red skin’; Lat. rubia, f. madder": MIr. roid, gs: -i, s. fa red-dye plant? beside Ir. rod, adj. ‘red’; m. 'iron-ore'; ruide, m. *trust-coloured water’; OBr. rod, adj. ‘rusty’; MHG rot, sm. & sn. ‘rust’; OE rudu, f. ‘red colour’; ON ryór, m., ryó, n. ‘rust; roð, n. ‘red’; OCS rüzda, R rža, OCz. rzě, Srb. rdja, f. (rusť, fr. *rudhio); Li. rudas, adj. ‘red-brown; auburn' beside rū- dis, gs: rūdžio, m. ‘rusť; rūdos, fpl. “ore”; rude, f. “heathcock'; Latv. ruds, adj. 'red- brown’; cf. rudens, gs. id. ‘autumn’; cf. the ex- tensions in Lat. rübínus, m. ‘ruby’; OE ryden (a plant) & roden, pp. ‘reddened’; Li. rudyne, f. *turf-moss'; further Cz. rdesno 'knotweed' beside rdest, m. *pondweed'; Pol. rdest, m. *knotweed, buckwheat’; Ir. ruidheog, f. *bog- myrtle’ (all plants w. red colouring or pro- ducing red dye)
leaf 607: 7:rudhéio «turn red, be red'. Cf. reudh-, roudh-, rudh-. WP II, 358 Gk. cf. (e-gde) ereuthéo, v. ‘be red’; eruthaínóo, tr. ‘redden’; Lat. rubeo, ere, intr. ‘turn red: Br. rüsia, v. (^blushr, fr. *-eu- or *-ou-); Cor. roedhya, intr. ‘redden, blush’; W rhuddo, inf. tr. (make red”, fr. *roudhaio); OE rudian, v. “be red'; MHG roten, v. id. (and “roast, fry"); | ON cf. ryðga, intr. ‘rust’; OCS and com. Sl. rüzdo se, rüdéti se “blush”; Li. rudeju, éti, v. ‘turn red or brown’; Latv. rudeju, id. Variant of type *rudhàió in Srb. rdjam, intr. ‘rust
leaf 607: 8:rudholos (rudhilos) "red plant, red object, red dye' Lat. cf. (*-ou- or *-ü-) rüfulus, adj. (/reddish", fr. Umbr.); Mir ruidel, s. “herb robert": ME cf. rodel-wort (a plant); cf. E ruddle *face- paint' and G Rótel, id.; Li. cf. ruduólis, gs: jo, m. (‘red-one’, epith. of *squirrel). (A type *rudhikós is represented in OE rudig ‘ruddy’ and in Slovene rdeč, adj. red". A type *rü- dhios, io arises in Lat. rubeus ‘ruddy’, rubia, f. “a dye-plant'; OCS ryZdi, adj. red"; Li. rüdis, gs: rudZio, m. “brown? beside rūdis, -dZio, m. ‘rust’; rūdys, m. id.; rude, f. *heath-hen'. An extn. of type *rudhn- arises in Arm. ortn, gs: ortan, s. ‘worm’; Gk. eruthaíno, tr. ‘redden’. A type *rudhros, *rudhoros arises in Skt. ru- dhiráh, Tokh. rtár, B rátre; Myc. erutro-; Gk.
leaf 607: 18:eruthrós; Lat. long vowel rüber, f: rübra; Umb. rufru-, acc. pl. m.; OE a-ryderian, v. ‘blush’; ON roóra, f. ‘blood’; OCS rüdrü, adj. red, as Skt. Gk. Tokh. etc. A type *rudh- sio occurs in Olr. ruisse, f. ‘redness’; Du. ruis, m. ‘roach’; Li. cf. rudusis, id. A type *rüdhst-, *rüst- ‘redness’ arises in MIr. rus ‘shame’; MHG rost, rust, sm. & n. ‘rust’ be- side OE rüst, m. id.; Pol. rdest, m. *knotweed, buckwheat; Li. dial. rüstas ‘brownish’, and Latv. ruste, f. ‘redness, red dye’. The variant in OE rost, Du. roest, and Finn. LW ruoste ‘rust’ is unexplained)
```


## [2026-09-04T15:14:41.034Z] TOOL CALL #56: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport re\nt=open('data/verification/sources/web/1b0b85ae075610e7.txt',encoding='utf-8').read()\nfor key in ['brk','krb','brq','mwt']:\n    hits=[m.start() for m in re.finditer(r'(?<![a-z])'+key+r'(?![a-z])',t)]\n    print('==',key,len(hits))\n    for h in hits[:2]: print(t[max(0,h-50):h+600].replace('\\n',' ')); print('..')\nEOF\ncd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; echo \"-- SYN 945/946 raod --\"; for n in 945 946; do $LF SYN.txt leaf $n --chars 0 | grep -n -i -B3 -A3 'raod\\|raoδ\\|rōy\\|roy\\b\\|NPers' | head -40; done",
 "description": "AHD Semitic roots brk/krb/brq/mwt; Buck p.874-875 raod context"
}
```


### [2026-09-04T15:14:42.838Z] TOOL RESULT

```
== brk 3
of banû , to build ( apli , heir; see ʾ pl ).   ‌ brk   West Semitic, to bless. Probably a metathesized variant of krb. Baruch , from Hebrew bārûk , blessed, passive participle of *bārak , to bless (only attested in derived stem bērēk , to bless).   broker , from Arabic al-barka , colloquial variant of al-baraka , the blessing, divine favor, gift, from bāraka , to bless. Compare krb.    ‌ brq   To flash (especially of lightning). emerald , from Greek smaragdos , emerald, probably ultimately from a Semitic source akin to Akkadian barraqtu and Hebrew bāreqet , a kind of gemstone (probably emerald).   ‌ brr   To be(come) clear, pure, white. barr
..
itic root, with West Semitic metathesized variant brk. cherub , from Hebrew kərûb , cherub; akin to Akkadian karābu , to praise, bless. Compare also brk.   ‌ kšš   Also kwš.   West Semitic, to pound, strike. couscous , cush , cush-cush , from Arabic kuskus , from kaskasa , to crumble, pulverize.   ‌ ktb   West Semitic root, to prick, cut; later, to write. ketubah , from Mishnaic Hebrew kətubbâ , writing, writ, (marriage) contract;  Tanakh , from Hebrew kətûbôt , the Writings, from plural of kətûbâ , feminine of kətûb , written (passive participle). Both a and b from Hebrew kātab , to write.   ‌ kṯr   To succeed, achieve, be(come) suitable, pr
..
== krb 3
tic, to bless. Probably a metathesized variant of krb. Baruch , from Hebrew bārûk , blessed, passive participle of *bārak , to bless (only attested in derived stem bērēk , to bless).   broker , from Arabic al-barka , colloquial variant of al-baraka , the blessing, divine favor, gift, from bāraka , to bless. Compare krb.    ‌ brq   To flash (especially of lightning). emerald , from Greek smaragdos , emerald, probably ultimately from a Semitic source akin to Akkadian barraqtu and Hebrew bāreqet , a kind of gemstone (probably emerald).   ‌ brr   To be(come) clear, pure, white. barrio , from Arabic barrī , open (of land), rural, from barr , open 
..
vine favor, gift, from bāraka , to bless. Compare krb.    ‌ brq   To flash (especially of lightning). emerald , from Greek smaragdos , emerald, probably ultimately from a Semitic source akin to Akkadian barraqtu and Hebrew bāreqet , a kind of gemstone (probably emerald).   ‌ brr   To be(come) clear, pure, white. barrio , from Arabic barrī , open (of land), rural, from barr , open area, akin to barra , to be kind, true, in derived stem barrara , to clear, acquit.   birr 2 , from Amharic bərr , coin, silver (< "white metal").   ‌ bry   Common Semitic noun *biry‑ , interval, in-between area. B'nai B'rith , from Hebrew bərît , covenant, akin to A
..
== brq 1
, gift, from bāraka , to bless. Compare krb.    ‌ brq   To flash (especially of lightning). emerald , from Greek smaragdos , emerald, probably ultimately from a Semitic source akin to Akkadian barraqtu and Hebrew bāreqet , a kind of gemstone (probably emerald).   ‌ brr   To be(come) clear, pure, white. barrio , from Arabic barrī , open (of land), rural, from barr , open area, akin to barra , to be kind, true, in derived stem barrara , to clear, acquit.   birr 2 , from Amharic bərr , coin, silver (< "white metal").   ‌ bry   Common Semitic noun *biry‑ , interval, in-between area. B'nai B'rith , from Hebrew bərît , covenant, akin to Akkadian bi
..
== mwt 1
maic māhal , by-form of Biblical Hebrew māl .   ‌ mwt   To die. checkmate , mate 2 , from Arabic māt , he has died, from earlier māta , to die.   ‌ my 1   Northwest Semitic *mīy‑ , who?. Michael , from Hebrew mîkā ʾ ēl , who is like God? ( kā , like + ʾ ēl , God; see ʾ l );  Micah , from Hebrew mîkâ , short for mîkā ʾ ēl (see above) or mîkāyāh , who is like Yahweh (see hwy ). Both a and b from Hebrew mî , who?.   ‌ my 2   (exact root shape uncertain). Common Semitic noun *mā̆ ʾ ‑ , *mā̆y‑ , water. mem , from Hebrew mēm , mem;  mu , from Greek mū , patterned to rhyme with nū , nu (see nwn ). Both a and b from Phoenician *mēm , water, thirteent
..
-- SYN 945/946 raod --
1---- SYN.txt leaf 946 / 1545; page-number candidates: ['2?', '875?']
2:udi : liudan, OF leodan, 2 eesti of consonants (through OS liodan ‘spring up, grow’, Skt. rudh-, lah can?) or otherwise is possible. Er- | Av. raod- ‘grow’ (12.53). Walde-P. nout-M. 378f. Walde-H. 1.530f. 2.416. Feist 323. ap = sie jos eb acrn eal more or less Goth. hiwi, OF hiw, heow also ‘color, it 7 o mica! word in most of the | appearance’, ME hiewe (in all senses MW ur. ‘anguages, as Dan., Sw., NHG | NE hue restricted to ‘color’) : ON Aj Mh form, in Slavic languages forma. ‘down’, Sw. hy ‘color of the skin’, root th eg “laws prepenty ‘shape given to | connection disputed, perh. fr. that in Oo ( : fingere ‘shape, mold’, figulus | he@wen ‘blue’, Ir. ctar ‘dark’, ON hart th
3-gpATI
4-*skeu- in words for
5-» ate. OF i 1.360 f. Falk-Torp
```


## [2026-09-04T15:15:39.693Z] AGENT (thinking)

I'm keeping a running checklist of remaining lookups across POK, SOD, BQT, FSD, IEC, KLN, and SYN sources, plus a note to check how existing files format ref_check for nodes without references. Next I'll work through these one by one.


## [2026-09-04T15:15:43.322Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; $LF POK_02.txt grep 'leudh-' 2 --chars 1800; echo \"-- mattus --\"; $LF POK_02.txt grep 'mattus' 2 --chars 600; $LF POK_02.txt grep 'madeo|madēre|madere' 1 --chars 1200",
 "description": "Pokorny leudh- and mad-/mattus via grep"
}
```


### [2026-09-04T15:15:45.289Z] TOOL RESULT

```
--- POK_02.txt leaf 345; page-number candidates: ['685']
 russ.  luzü  [*laude}ö),  '" ludüh  , betrügen,  täuschen'. WP.  II  415  f.,  Trautmann  151. I.  leudh-    , emporwachsen,    hochkommen',    leudho-,    leudhi-    , Nachwuchs, Volk' ;  leudhero-  ,zum  Volk  gehörig,  frei'. Ai.  rödhati,    röliati   , steigt,    wächst',    av.  raodaiti  , wächst',  ai.  röha-  m. ,das  Aufsteigen,  Erhebung,  Höhe',  «uaröc^Aa- m.  ,W^urzeltrieb,  Luftwurzel,  _ Senkung',  av.  raoda-  m.  , Wuchs,  Ansehen',  npers.  röi  , Gesicht'; gr.  iXsv&SQog  ,frei'  aus  "^leiidhero-s  =  lat.  Über  ,frei';  fal.  loferta  ,liberta'; i 685 alb.  vielleicht  lenj  , werde  g'eboren,  entstehe'  (*leudh-n-),  lind  ,gehäre', polerJi  ,Yolk'  (leiidh-vi-) :  vela  , Bruder'  (*siie-londhä  .Sippengenosse') ;  ke- lüsh  .Geschlecht'; lat.  Liher  ,ital.  Gott  des  Wachstums,  der  Zeugung-,  Anpflanzung',  osk. Qeu.  Luvfreis  , Liberi',  lat.  liberi,  -örum  ,die  Kinder',  juristisch  auch  von einem  einzigen  Kind,  also  ,*Nachwuchs' ;  llher  ,frei'  s.  oben; air.  liiss  m.  ,Pflanze'  (Hudh-stu-),  acorn.  les  ds.,  mcorn.  leys,  PL  loso2v, cvuir.  llysiau,  bret.   louzou  ds. ; trot.  liudan,  ahd.  liotan,  as.  liodan,  ags.  leodan  , wachsen',  ahd.  sumarlota ^Sommerschößling',  anord.  lodenn  , bewachsen,  haarig,  rauh',  loda  ,(*fest- o-eTvachsen  sein  =)  festhangen,  festkleben';  got.  laudi  i.  , Gestalt',  swa-, sama-laups  ,so  groß',  jugga-lanps  ,Jüngling',  mhd.  löt  , beschaffen';  got. ludja  ^Antlitz'  (vgl.  np.  röi),  as.  lud  .Äußeres,  Körperkraft  (?  nur  Hei. 154),  ahd.  ant-lutti  , Antlitz' -^  (Nachwuchs  =  Menge,  Volk  :)  ahd.  Hut,  ags. Uod  ,Volk',  mhd.  Hute  , Leute',  ags.  leode  ds.,  dann  auch  von  einzelnen Menschen  ahd.  Hut  , Mensch',  nhd.  dial.  das  Leut  ,Person',  nd.  lud,  lüt , Weibsperson,  Mädchen',  burgund.   leudis  ,der  Gemeinfreie'; aksl.  Ijudhje  (*

-- mattus --
--- POK_02.txt leaf 355; page-number candidates: ['695']
bse^, jnodhe  ,Lolch^; lat.  madeö,  -ere  ^naß  sein,  von  Nässe  triefen,  reifen,  voll  sein%  mattus trunken'  {*madi-to-s)'^ air.  maidim  ^breche  (intr.),  gehe  in  Stücke'  (eigentlich  ^fließe  auseinander, zergehe';  formell  =  lat.  madeo) ;  in-madae  ^vergeblich,  ohne  Erfolg'  (dazu wohl  c.  maddeu  ,erlassen,  verzeihen',  abret.  in  madau  ,pessum' ;  gäl.  maistir ,urina' (*7Mac?-^rz-);  mir.  mät  f.  , Schwein'  (*mäddä  ,Mast-Schwßin')  ;

--- POK_02.txt leaf 355; page-number candidates: ['695']
reche  (intr.),  gehe  in  Stücke'  (eigentlich  ^fließe  auseinander, zergehe';  formell  =  lat.  madeo) ;  in-madae  ^vergeblich,  ohne  Erfolg'  (dazu wohl  c.  maddeu  ,erlassen,  verzeihen',  abret.  in  madau  ,pessum' ;  gäl.  maistir ,urina' (*7Mac?-^rz-);  mir.  mät  f.  , Schwein'  (*mäddä  ,Mast-Schwßin')  ;
```


## [2026-09-04T15:15:45.386Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"5yz\\|Syz\\|8yz\" SOD_pages.txt | head -20; echo \"-- rwδ- entry 8562 --\"; sed -n 28360,28400p SOD_pages.txt | cut -c60-140; echo \"-- line 3247 context --\"; sed -n 3240,3250p SOD_pages.txt",
 "description": "Sogdian δyz fortress entry and rwδ- grow entry"
}
```


### [2026-09-04T15:15:45.475Z] TOOL RESULT

```
14545:      5ew-manuk                                                       3825 Syz> M                                                *JS« >
14550:      5cw-mec                                                         3826 dyz> C «* 5yz>
16568:          138.20; Frag. Len. 82 a 26                              xwezak(u), x5yze ? (ywzky ) ©adv.
24137:7103 prSyz M                      (j*n>)u**J't{!             7115 pry'wt- B                         o^J'^^J'^j
24145:7104 prdyz C *=» pr8yz                                            parxez ©<* para-hazya- ? =^pryyz-
24147:7105 prSyzp'n S                  (Okj^k)^i3Jl^tS^J
24151:      MDii A-5, 22; prSyzpt, MDiii p97                            frayaz =*prYz-» PrYz~» f*Yz-> frYz~
-- rwδ- entry 8562 --

                  provisions
                  GMS 995
             8561 rw8 B                                        u~*i<jjj
^3j               ro8 (rwd) ©MP roy% Parth. rod

            ->    copper, brass
                  SCE 238; BSTBL, Intox. 14, 15; STii 5, 12
■ ij&hj
             8562 rw5-       B, M, S                              jjujj

                  ro5 ©<Av. raod-; * fraud-; Parth. rod-;

                    Khot.rw<f; Yaghnxur      ©inf. ->y =»>Prw5,

                    ptrw6-, rw5n-
                  (fo)grow
                  BBB 580; GMS 586; TSP 2.10, 18; W-Lii; BSTBL,
     OSf>           pi 30, Vim. 30, 150, Dhu. 31, etc., Dhy. 196, etc.;

                    Frag. Len. pl08; inf. ->y, Dhy. 196; AVS 114
             8563 rwd C =» rw5

             8564 rw8>k B                              (•JUiJJ)^Ui.l/
                   ro5e, roSak ?

                  plant, herb
                  TSP 3214: Frag. 3.4

               8565 rwdny      C =» rw6ny(y)
             8566 rw5n-      M                                    j-^.jj
                  roSan ©caus. st. =^rw5-
                                                           rwstm(y)




                TSP 2.1193, 7.26, 8.39, 29; BSTBL, Padm. 52, 61

           8577 rwke'tCh) =» rwk

-- line 3247 context --
  /sary/      srY          lion          Parth. s^r-,                 /srwan/          Vw'n            soul            Av. urvanam

                                         MP Syr-                    VII) The Sogdian frf reflects Olr. */r/115 and *[r]116.
  /xsap/      'xyp-        night         Av. xsapa-                   /r£9/ /■>#- road                  Av. rai6ya% Pers.
                                                                                                       ra/i
  Imusl       mws          mouse         Olr. mus(a)

  3) Izl:                                                             /ro5/            rw5-       grow              Av. rao£-
  /azu/       >z>v         I             Av. az9m                     /yar/            Yr-        mountain          Av. gairi
  /zirn/      zyrn         gold          Av. zaranya-                 /zirn/           zyrn       gold              Av. zaranya-
  /anxaz/     Wz-          rise          Olr. *ham-xaz-               /kirm/           kyrm-      snake             Pers. Jb>m (worm)
```


## [2026-09-04T15:15:52.946Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\npages=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\ndef clean(s): return re.sub('[‎‏‪-‮⁦-⁩]','',s)\nfor i in (370,378):\n    p=clean(pages[i]); m=re.search('د[یي]وار',p); print(f'### leaf {i} divar:',p[max(0,m.start()-300):m.start()+500].replace('\\n',' | ')); print()\nfor i in (402,408,409):\n    p=clean(pages[i])\n    for m in re.finditer('رستم',p):\n        print(f'### leaf {i} rustam:',p[max(0,m.start()-150):m.start()+250].replace('\\n',' | ')); print()\np=clean(pages[311]); print('### leaf 311 tail:'); print(p[-1800:])\np=clean(pages[404]); print('### leaf 404 latin:', [m.group(0) for m in re.finditer(r'[^\\n]{0,60}[A-Za-zāēīōū]{3,}[^\\n]{0,60}',p)])\nprint('### ruy / rustan headwords 395-415')\nfor i in range(395,416):\n    p=clean(pages[i])\n    for m in re.finditer(r'(روی|رستن|رسثن)\\s*[-=؛]\\s*[^\\n]{0,40}(وزن|فتح|ضم|کسر)',p):\n        print('leaf',i,':',p[max(0,m.start()-50):m.start()+400].replace('\\n',' | ')); print()\nEOF",
 "description": "Borhan vol 2 contexts for dīvār, Rostam, dež footnotes, raz, rūy/rostan"
}
```


### [2026-09-04T15:15:54.762Z] TOOL RESULT

```
### leaf 370 divar:    دیدیان است که بعربی ربیثه خوائند .                                      وم شده باشد . |                                                                                                 تاپیدا ک | دید بانان عالم ت کنابه از هفت |                                                           د دار  ۱عم بر وزن دیوار » ترجمهةٌ | ک وکباست کهزحل‌ومشتری‌ومرشو فتاب‌وزهره                     روت است  -وبمعنی رخ وروی وچهره باشد - |                              وعطارد وماه باشد .           ویمعتی رخ لمودن ردیدن هم هست  - ۴وچشم | دید م بان فلك  -کنابهاز کوکبزحل                           ویاعيننند  -و ببنابی  خرب |                                                                                   کاویبزندکه یمر |                     است که درفلك هفتم میباشد .             وقوت باسرء رایز کفته‌اسوبمعنی پیدا ویدیدار |  دیده با

### leaf 378 divar:                                                                                   ذی | واگرطفلی دبر بحر کت بد چون برومالند زود                                  از خراب دن خانه باشد . |                                                      ديو ار گر = دبوارساز  وگل‌کار وینارا | دیوال  ۴سبا لام" بروزن ومعنی دیوار                                                            گونشد . | است» چه درفارسی راولام بهم تبدیل مییایند #. | ۰    فرشت     رای   بفتح   دیواله رو | شخصی‌را کوبند کهمدابنوندانهاسلوك کند وبراه                                عاجز وزبون هدن باشد . |                                             رود .    همز هو بای‌فارسی   د یو اسست  ۴یک |  |  |      - ۱نظر بتصور مهيب و هولناك بودن دبوان « .هرچیز را که از افراد خودفوی جثه‌تر |      و بزرکترباشد بدیو اضافت نمابند (با بفول که آنهم دو موهوم است) مثلاکمان بز ر

### leaf 402 rustam:   4 ) ۰۷                                                                                 رخعا |  |  | وئالث بالف کشیده» بمعئی رخشان ورخشندموتابان      واحب رستم‌را لیزباین اعتبار رخش میگفته‌اند ١۔ |                باشد ؛ ویضم اول نگیفزته‌اند .    ومطلق اسب را هممیگوبند  - ۴و بمعنی ابتدا | رخشان  = ۱بم اول بروزن هتان ۰                      دوب |                                                      نزک |         

### leaf 402 rustam:         ر                           وکون ثانی |                                                          رخشا ؟  -بفتح اول س |  |   ۰ ۱چنانکه مشهور است رخش رستم مر کب بود ازرنگه قرمز وزردة تخم مرغ |   وسفیدی و کلهای بیار کوچك میان زرد وقرمزداشت وبیضه وزیر دم و از زبرچشم تا دهن سفید |   بود که اورا بورابرش بضه سفید میگفتند > « فرسنامةٌ اسداله خواناری بقل نمعلیقات نوروزنامه |  (ماسة ملی ابران  .ترجمةٌ بزر که عل

### leaf 408 rustam:         ومس ۳ |                                                                رسته |                                                                    #رستم = رستهم  ۳رو |      (بالش  ,نمو) ر[ستن و روبیدن از همين ربشه است]  +نهم =  301321درپارسی                             8 |      باستان کوانها و دیگر بخشهای اوستا بمعنی دلیرو پپلوان .تهمتن ایز ازهمین ریشه است بمعنی |      بزر که پیکر وقوی الدام و درق قت 

### leaf 408 rustam:       8 |      باستان کوانها و دیگر بخشهای اوستا بمعنی دلیرو پپلوان .تهمتن ایز ازهمین ریشه است بمعنی |      بزر که پیکر وقوی الدام و درق قت تهمتن معن یکم رستم است .بثایرآ اجه کفته شد رستم‌سنی |  |      کشیده بالا و بز رگے تن وقوی پیکر «یشتها  ۲ص ۹۳۱نام‌جهان پهلوان ابرانی پسر زال‌پسرسام. |    مارکوارت تصور کرده است که رتتخم ( اوستا  ) 210251 - 20۳7805عنوان وصفتی برای |    ل ۰ی4‌۱۲نلد که این فولرامردود داسته. |  

### leaf 408 rustam: دیگر بخشهای اوستا بمعنی دلیرو پپلوان .تهمتن ایز ازهمین ریشه است بمعنی |      بزر که پیکر وقوی الدام و درق قت تهمتن معن یکم رستم است .بثایرآ اجه کفته شد رستم‌سنی |  |      کشیده بالا و بز رگے تن وقوی پیکر «یشتها  ۲ص ۹۳۱نام‌جهان پهلوان ابرانی پسر زال‌پسرسام. |    مارکوارت تصور کرده است که رتتخم ( اوستا  ) 210251 - 20۳7805عنوان وصفتی برای |    ل ۰ی4‌۱۲نلد که این فولرامردود داسته. |                               

### leaf 408 rustam:  میداند .      یان |                                                     سکت |                                                       پاکانددفشراه سهرئفلد رستم را با |   تالف هرتفلد  .للدن  ۵۳۹۱ص ۲٩  . ۳۱ -اتاد هنینگه درمجلة مدرسةٌ السنةٌ شرفی |      لندن ح]] 162س ۵ - 4۱۱ه درمعرفی ونقد کتاب ( مذکور ) هرنفلد کوبد « :س رگذشت |      جذاب  7728۵0۷۳6و قصر واقع در «کوه خواجه» (سیستان) بارویگر درسغنرانی (هرتسفلد) |  

### leaf 409 rustam:   با                                                                                             - |  | وفتح فوقالی وها ومیم هردوسا کن » رستم زالرا         رسته  ۱ب«روزن دسته  ۰بمعنی خلاص |                                      ف2              شده ولجات‌بافته باشد ومطلق صفرالگیوزبند |                                                      اعم از انان وحیوان دیگر  - ۴وراستة هرچیز | رسقی = بض‌او

### leaf 409 rustam:                                                                                  باش |         © _ از  :رست (ه.م + ).ی (مصدری) .                       :رستم » روستم .      - ۴رک |  |                                                                         :رسدن۰    رکه      ٩ |  |  |                                                                                    ۸٤٩     حه |                                   

### leaf 409 rustam: نی‌است       متعمل بوده است  .منظر میرسد که مدارك                ۰فشر      و صفت |  |  نات) دارد  ۳رد کند و اجازه میدهد که فرض کنیم          بر اینکه نام رستم  ۰رابطةٌ مستقیم با۴۲312 |  |                         داستان رستم قدم ثر و مستقل از افانه اخس باشد  » ۰رك :رستهم  ۰روستم |  |    #ستن  -بفتح اول و سوم  ۰بهلوی ( ۲5305۵۲آزاد شدن  ۰استقبال کردن) ر=هیدن |                                                       

### leaf 409 rustam:     ۰فشر      و صفت |  |  نات) دارد  ۳رد کند و اجازه میدهد که فرض کنیم          بر اینکه نام رستم  ۰رابطةٌ مستقیم با۴۲312 |  |                         داستان رستم قدم ثر و مستقل از افانه اخس باشد  » ۰رك :رستهم  ۰روستم |  |    #ستن  -بفتح اول و سوم  ۰بهلوی ( ۲5305۵۲آزاد شدن  ۰استقبال کردن) ر=هیدن |                                                                         ر |  از ابرالی باستان  » 01۵۲فس  :بارسی باستا

### leaf 311 tail:
 - ۷پهلوی sãkãhsud                                درکام  ۰درکامه ۰




                     چو بل در آ گاه ودرنده شس.                                              سوار جپان نبوزار دلیر
 دقیقی طوسی« .مزدیبنا 4۵۳-۵۵٩ .
                  دژ ( رکه :ج )  +آلود (لوآده) .                            ز:
                                                                             ۸ا_۵                    :د؟آ گاه ۰        رک       ۷


                                                                                                                بقه اصزفحهٌ ۰۵۸
                  (سارق)  ,بپلوی ن0ز2 = ( 60یا ) .                                    اسشق 41۵؛ دراوراق‌مانوی بپپلوی 20
                  Henning. A list of Middle                                   Persian .. , BSOS                        126, p. 82.
  کسکه        ب    صارق     ِ   ٩zûd ۳           ۳    €       ۸۷     گربرسن          ۶    0۵0۳2          وخی      ,           اشکآشمی 0


 دزدان عرب بر سر کوهی نشته بودند و منفذکاروان بسته »                                               ق:
                                                                                                  ةٌ بزن ط» ر
                                                                                                       ااه     مال مردم را بب
                                                                                                             «رد
                                                                                                                         «گلتان . ۱۲
 #زدیدی  -بض اول و فتح پنجم  ,از  :دزد -۳بدن ( پود مصدری ) ؛ سرقت »
                                                                  د
                                                                                                                       بردن مال مردم .

### leaf 404 latin: ['   —ttA                                                            ', '           (Henning,      A list of Middle         )Persian..., BSOS ,lX,1,p.87.']
### ruy / rustan headwords 395-415
```


## [2026-09-04T15:15:58.077Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSD_vol1.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"check 'mate\\\",  1   rfhek'mef\"); print('vol1 checkmate:'); print(t[i:i+1200].replace('\\n',' '))\npages=t.split('\\f'); \n# which leaf\npos=0\nfor k,p in enumerate(pages):\n    pos+=len(p)+1\n    if pos>i: print('leaf',k); break\nt3=open('FSD_vol3.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'(Ar\\.|Pers\\.)[^\\n]{0,40}m[aâ]t',t3):\n    print('vol3:',t3[max(0,m.start()-300):m.start()+300].replace('\\n',' ')); print('---')\nEOF\necho \"-- IEC rusta --\"; grep -n -i 'rust[aā]\\|rōst\\|rūst' IEC.txt | grep -i 'per\\|village' | head -5",
 "description": "FSD checkmate entry text; FSD vol3 Arabic mat; IEC rūstā"
}
```


### [2026-09-04T15:16:00.062Z] TOOL RESULT

```
vol1 checkmate:
check 'mate",  1   rfhek'mef;  2   chSk'mat',  v.  [-mat'ed: -mat  iso.]  1.  Chess.  To  put  (an  opponent  s   king)  m —   to  take  c.,  to  he  offended.— travelers’  c.  (Banking), check  to  the  order  of  a   traveler  which,  when  endorsed  by the  latter,  serves  as  cash.— waived  storage  c.  (Railroad.), an  order  authorizing  delivery  and  rescinding  storage  charges, where  freight  has  been  stored  by  mistake. game  thus  diverting  the  hawk.  (2)  Hunting.  A   tem-  check2,  n.  (Scot.]  The  wheatear  or  chack.  ling  checked. a   check  from  which  no  escape  is  possible,  thus  winning the  game.  See  the  noun.  2.  Hence,  to  discomfit  or defeat  (a  person,  plan,  etc.),  as  by  a   skilful  maneuver; as,  the  diplomatist  was  checkmated  by  the  council. porary  halt  in  the  chase  due  to  the  loss  of  the  scent  check'a-fol(ep,  1   Chek'a-bl;  2   ch&k'a-bl,  a.  Susceptible  of  be-  Check'mate",  n.  1.  Chess.  The  final  position  in  a   game by  the  hounds.  13.  That  part  of  a   substance  under  check'age,  1   tfhek'ij;  2   chSk'ag,  n.  A   checking,  as  of  an  of  chess,  in  which  theki:   test  which  is 
leaf 511
vol3: tos is a hish authority on qumtions of rolixion and laws G P. Fisuaa Vntv H%et pt. ii, period IV, p. 303. (i. a oo. 1886 ] 2. [(vulloq., Brit 1 (1) Citiscns' dress w’om bv military or naval officers when off duty. (2) Ordinary dress us distmgmshfld from full dress or dress for state occa- sions [ < Ar. mufti, < mii- (formative) -i- afl%t judge.] — murtl-shtp, n. The post or rank of a mufti, muf'ty, 1 muru, 2 mOf'ty. n. [Prov. Eng ] The white- throat, muff. mug, 1 mug, 2 mflfl. c. [MTTaaF.D, inTaii*; Mun'oiNO ] I. t. I. (Slang, Eng ] To bribe with alcoholic beverages 2. iHlung, U B ) To pliolog
---
-- IEC rusta --
1654:bhrigo, ið “fry, roast Skt. bhrijjami, pp. bhrstah; Per. birištan, bu- rustan, id.; Lat. frigo, frigére, id. beside ferctum, fertum 'spice-cake'; Umb. cf. frehtu, pp. roasted". (The vocalism of Gk. phrügo, phrüsso is obscure. A form bréglen “fry, stew’ (fr. *bhrigh-?) occurs in MHG beside Swed. brácka (2) ‘roast, fry, braise’)
12277:ordhos (1), ordhō, eið, ið (rdh-) ‘erect; growth; grow, rise’. Cf. uordh- and urdh-. WP I, 87. (The Gk. reconstruction *yordh- rests solely on Hes. Bortheía: Orthía ‘the goddess Artemis’) Skt. cf. fdhyami, rdhnómi, v. ‘thrive’; rddháh, pp. as adj. (‘thriving, growing”, fr. *ordhtós); cf. ardhukah, adj. ‘prospering’; Av. (ambig.) arədus, aroóvo (“highb’, cf. ard-) beside arod-, v. ‘grow’; Oss. räzä ‘fruit; rázín, Dig. irázun, v. ‘grow’; rázt, räst ‘growth’; Per. cf. rustan, rostan, inf. ‘grow’; rust, rost ‘growth’; Tokh. A orto, adv. ‘upward’; Arm. ard, gs: ardu ‘form, fashion, way’; ardiwnk, pl. ‘produce’ beside (ambig.) ordi, gs: ordvo (son, child', if not fr. *putrio-?), cf. however h-ord, i-st. (abundant, fr. *en-ordh- or *epi-ordh-); h- ordem, v. "make grow, make abundant, be abundant; Hitt. hartu, pl. artuwa (sic) ('des- cendant': Arm. ordi?); Arm. cf. also ardak, gs: Hi, ab. s. -av “straight perh. fr. *urdh-, in view of the secondary mng. ‘even, uniform’. SEM: AFI: ardak, § 33a **ordh-'; § 100 ardak, ardar < *urdh-. Background ambig. as Gk.; MHG art, sm. & sf. ‘nature, way’; Du. aard, m. *na- ture, kind, order": G arten, v. ‘thrive’; cf. ent- arten 'de-generate'; Du. arden, v. ‘thrive, grow’; ON orð, gs: arðar, f. u-st. (crop, yield": Arm. ard) beside ọrðigr & oróugr, adj. (1) ‘upright; OCS rodü, m. “product, kind” and
```


## [2026-09-04T15:16:04.644Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && LF=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/lf; $LF KLN_1966.txt grep 'shah  mat|checkmate,  tr|checkmate,  n\\.  —' 2 --chars 900; echo \"-- SYN 946 before raod --\"; python3 - <<'EOF'\npages=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=pages[946]; i=p.find('raod-'); print(p[max(0,i-1500):i+200])\nEOF\necho \"-- existing ref_check format --\"; cd /home/sfmqrb/git/rishe/data/verification && grep -l 'ref_check' page-*.json | head -3; python3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('/home/sfmqrb/git/rishe/data/verification/page-*.json'))[:40]:\n    v=json.load(open(f))\n    found=False\n    for e in v['entries']:\n        if 'ref_check' in e:\n            print(f, 'root ref_check:', json.dumps(e['ref_check'][:1],ensure_ascii=False)[:300])\n            for n in e['nodes']:\n                if n.get('ref_check') and (n['ref_check'][0].get('ref') in (None,'none','None','') or 'no ref' in n['ref_check'][0].get('note','').lower()):\n                    print('  none-ref node example:', json.dumps(n['ref_check'],ensure_ascii=False)[:300]); found=True; break\n            if found: break\n    if found: break\nEOF",
 "description": "KLN checkmate head; Buck context; existing ref_check conventions"
}
```


### [2026-09-04T15:16:07.388Z] TOOL RESULT

```
--- KLN_1966.txt leaf 154; page-number candidates: ['272', '273']
gh  the  medium  of  Spanish  and Arabic)  fr,  Pers.  shah,  ‘king’  (in  the  Arab.-Pers. phrase  shah  mat,  ‘the  king  is  dead’),  fr.  OPers. xshaya-,  ‘king’,  which  is  rel.  to  xshaya&iya-, ‘power’,  fr.  I.-E.  base  *qpe(i)-,  *qfe(i)-,  ‘to  rule’, whence  also  OI.  ksayati,  ‘possesses,  rules’,  ksat- ram,  ‘rule,  dominion’,  Gk.  xTaopat,,  T  get,  ac¬ quire’.  See  satrap,  shah  and  cp.  checkmate,  chess, checker,  exchequer,  Kshatriya.  Cp.  also  the  first element  in  Ahasuerus,  Xerxes  and  the  second element  in  Nakshatra,  padishah  and  pashah. Derivatives :  check,  tr.  and  intr.  v.,  check-less,  adj. check,  cheque,  n.,  a  written  order  to  a  bank.  — Most  philologists  derive  this  word  from  check in  the  sense  ‘a  sudden  stop’.  It  is  more  probable, however,  that  check  in  the  sense  ‘a  written  order to  a  bank’,  comes  fr.  Arab,  fakk,  ‘agreement, contract’,  fr.  Pers.  cdk,  of  s.m. checker,  chequer,  n.,  a  pattern  re

-- SYN 946 before raod --
udi : liudan, OF leodan, 2 eesti of consonants (through OS liodan ‘spring up, grow’, Skt. rudh-, lah can?) or otherwise is possible. Er- | Av. raod- ‘grow’ (12.53). Walde-P. nout-M. 378f. Walde-H. 1.530f. 2.416. Feist 323. ap = sie jos eb acrn eal more or less Goth. hiwi, OF hiw, heow also ‘color, it 7 o mica! word in most of the | appearanc
-- existing ref_check format --
page-32.json
page-31.json
/home/sfmqrb/git/rishe/data/verification/page-31.json root ref_check: [{"ref": "POK:1", "status": "supports", "note": "POK_01.txt line 19 (IEW p.1): 'ab- Wasser, Fluß. Lat. amnis ... air. ab ... cymr. afon ... Vgl. auch 2. ap- Wasser, Fluß und abō(n) Affe'. The Iranian forms are under 2. ap- p.51 (English edition POK_full.txt: 'Root ap-2 (*hap-2) water, river ... Old 
  none-ref node example: [{"ref": "FVQ:46", "status": "supports", "note": "Node carries no refs; FVQ_pages.txt ff-page 64 (Jeffery p.46): 'A ewer, or water jug ... It was early recognized as a Persian loan-word (Siddiqi, 13), and is given by al-Kindī, Risāla, 85; ath-Thaʿālibī, Fiqh, 317; as-Suyūṭī and al-Jawālīqī in their
```


## [2026-09-04T15:18:40.788Z] AGENT (thinking)

I've compiled the last batch of lookups (SOD δyz, KLN "mate," Devic ÉCHEC, AHD smaragdite, BQT دیوار and روییدن leaves, and Pokorny mad-). Now I'll write out the files.


## [2026-09-04T15:18:43.498Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n 14540,14560p SOD_pages.txt | cut -c60-150; echo \"-- KLN mate tr --\"; grep -o 'mate,  tr\\.  v\\..\\{0,400\\}' KLN_1966.txt | head -2; echo \"-- DEV echec --\"; grep -n '^ÉCHEC\\|^ECHEC\\|Échec\\.  \\|Echec\\.  ' DEV.txt | head -5; python3 - <<'EOF'\nimport re\npages=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(pages):\n    m=re.search(r'(?m)^[ÉE]chec\\.',p)\n    if m: print('DEV leaf',i,':',p[m.start():m.start()+1500].replace('\\n',' ')); break\nEOF\necho \"-- POK mad head --\"; python3 - <<'EOF'\npages=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in (354,355):\n    p=pages[i]\n    for m in re.finditer(r'mad-',p):\n        print('leaf',i,':',p[max(0,m.start()-100):m.start()+500].replace('\\n',' ')); print('--'); break\nEOF",
 "description": "SOD δyz gloss, KLN mate verb, Devic échec, Pokorny mad- head"
}
```


### [2026-09-04T15:18:45.999Z] TOOL RESULT

```
                     1981 p214, 16V5
           3823 6yyn      M =* Syn

j^          3824 8yyw6Jt M =» 5yw5>t
           3825 Syz> M                                                *JS« >
                5iza (dyzO ©<OP dida           ©f. n.
                stronghold, fort
                BBB f 57; STii 3.27
y-*
           3826 dyz> C «* 5yz>


                 'rt', -P                 f
 tJill
          3827 -f M                                                   yt\j

                f ©2sg. pers. pron. =>-fy, tyw, d}f\ c}f\ pr'P,


                GMS 1355; S W, C2n p77.31
-- KLN mate tr --
mate,  tr.  v.,  to  give  life  to,  to  enliven.  —  L. animatus,  pp.  of  animate,  ‘to  fill  with  air  or breath,  to  animate’,  fr.  anima.  See  animus  and verbal  suff.  -ate.
mate,  tr.  v.,  to  make  parallel  to  a  given  line. —  Fr.  coilimdtus,  pp.  of  ‘collimare’,  an  er¬ roneous  reading  in  early  editions  of  Cicero  for L.  collinedre,  ‘to  direct  in  a  straight  line’,  fr. com-  and  lineu,  ’line'.  See  line,  ‘row’,  and  verbal suff.  -ate.
-- DEV echec --
-- POK mad head --
leaf 355 : er-  (s.  dort). tnad-  ,naß,  triefen;  auch  von  Fett  triefen,  vollsaftig,  fett,  gemästet';  mad-do- ,Mästung'. Ai.  mddati,  mddate  ,wallen,  sprudeln,  fröhlich  sein',  mädyati,  mamdtti, mdndati  ds.,  mdda-  m.  ,Rauschtrank'  =  av.  maSa-  , Rauschtrank,  Rausch- begeisterung', ai.  mattd-  ,trunken,  freudig,  erregt',  av.  mad-  {maöaitlj madayaTdha)  ,sich  berauschen,  sich  ergötzen  an' ;  ai.  madgu-  ,ein  bestimmter Wasservogel,  ein  Fisch'  =  np.  mäy  ,ein  Wasservogel',  ai.  mdtsya-  m.,  av. masya  ,Fisch'  (,der  nasse' ;  Ableitung  von  einem  -es-St.  *mades
--
```


## [2026-09-04T15:18:49.623Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\npages=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\ndef clean(s): return re.sub('[‎‏‪-‮⁦-⁩]','',s)\nfor i in range(375,380):\n    p=clean(pages[i])\n    for m in re.finditer(r'د\\s?[یي]\\s?و\\s?ا\\s?ر\\s*[-=؛]',p):\n        print(f'### leaf {i} divar headword:',p[max(0,m.start()-100):m.start()+500].replace('\\n',' | ')); print()\n    lat=[x.group(0) for x in re.finditer(r'[^\\n]{0,60}[A-Za-zāēīōūδ]{3,}[^\\n]{0,60}',p)]\n    if lat: print(f'   leaf {i} latin:',lat[:8])\nprint('### ruyidan variants 398-404')\nfor i in range(398,405):\n    p=clean(pages[i])\n    for m in re.finditer(r'رو[یبئي]{1,2}دن|رو[یي]\\s*[-=؛]\\s*[^\\n]{0,30}وزن',p):\n        print('leaf',i,':',p[max(0,m.start()-80):m.start()+350].replace('\\n',' | ')); print()\nEOF",
 "description": "Borhan vol 2 dīvār headword and rūyīdan variants"
}
```


### [2026-09-04T15:18:51.266Z] TOOL RESULT

```
   leaf 375 latin: ['   ۰شهرستالپای ابرانشپر              » مار کوارت       mulêD         ۰بهلوی    قومی حاکن دبلمان           ۳ ۱', '  رك :دیمه:          ©           .     eورك :دمه       GAF    طری    (رو) » صاب       .dîimطر ی md                  کی']
   leaf 377 latin: ['                                  ص . ۰ ۱۶۱          < .۳۵۷ Asclepium Dios.كل                        — ۴']
### ruyidan variants 398-404
```


## [2026-09-04T15:18:52.753Z] TOOL CALL #64: Bash

```json
{
 "command": "p=$(python3 tools/fetch_source.py \"https://ahdictionary.com/word/search.html?q=smaragdite\" --note \"ref check AHD:427 smaragdite/emerald, page 101 root B.r.q node 8\"); echo \"$p\"; python3 - \"$p\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8').read()\ni=t.find('smar'); print(t[i:i+700].replace('\\n',' '))\nEOF",
 "description": "Archive and read AHD smaragdite entry"
}
```


### [2026-09-04T15:18:54.935Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/255d29993717c128.txt
smaragdite FETCHED: 2026-09-04T15:18:54Z STATUS: 200 TITLE: American Heritage Dictionary Entry: smaragdite  American Heritage Dictionary Entry: smaragdite    HOW TO USE THE DICTIONARY  To look up an entry in The American Heritage Dictionary of the English Language, use the search window above. For best results, after typing in the word, click on the “Search” button instead of using the “enter” key.  Some compound words (like bus rapid transit, dog whistle, or identity theft ) don’t appear on the drop-down list when you type them in the search bar. For best results with compound words, place a quotation mark before the compound word in the search window.  guide to the dictionary    THE USAGE
```


## [2026-09-04T15:19:31.604Z] AGENT (thinking)

All lookups are complete. Now I'll add the `ref_check` data to the four files and append archived web URLs where used, then run the checker.


## [2026-09-04T15:23:38.739Z] TOOL CALL #65: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/apply_refchecks.py",
 "content": "#!/usr/bin/env python3\n\"\"\"Add ref_check arrays (and archived web URLs to sources) to pages 101, 126, 311, 345.\"\"\"\nimport json, collections\n\nVER = \"/home/sfmqrb/git/rishe/data/verification/page-%d.json\"\n\ndef rc(ref, status, note):\n    return {\"ref\": ref, \"status\": status, \"note\": note}\n\nNC = lambda ref, why: rc(ref, \"not_checked\", why)\nNONE = lambda extra=\"\": rc(\"none\", \"not_checked\", \"Nourai cites no reference for this node.\" + (\" \" + extra if extra else \"\"))\n\nno_FVA = \"FVA (Nahvi, Farhang-e vazheha-ye arabi dar farsi) has no digital copy (refs_online.json).\"\nno_SOR = \"SOR (K. Akhavan Zanjani) unidentified/not online (refs_online.json).\"\nno_PLA = \"PLA (Asbaghi, Persische Lehnwörter im Arabischen) is not online in full text (HathiTrust search-only).\"\nno_VDQ = \"VDQ (Badreh'i's Persian translation of Jeffery) is only on noorlib's JavaScript viewer; not readable here. Its substance = FVQ.\"\nno_MAG = \"MAG (Widengren, Muhammad the Apostle of God, 1955) has no full text online.\"\nno_KGW = \"KGW (Ibrahim, Kulturgeschichtliche Wortforschung, 1991) is in copyright; Google Books preview only.\"\nno_MON5 = \"MON vol. 5 (a'lam / proper names) is not online; vajehyab/abadis carry only the lexicon volumes.\"\nno_BQT3 = \"Borhan-e Qate' (Mo'in ed.) vols 3-5 are not online in full text (only vols 1-2 on archive.org).\"\nno_CEL = \"CEL3 is not in refs_online.json (no online copy located).\"\n\n# URLs archived with tools/fetch_source.py in this session\nU_MON = lambda w: f\"https://vajehyab.com/?q={w}&d=moein\"\nU_AHD = lambda w: f\"https://ahdictionary.com/word/search.html?q={w}\"\nU_SEM = \"https://ahdictionary.com/word/semitic.html\"\n\nKLN_BERAKAH = (\"KLN_1966.txt leaf 98 (printed pp. ~160-164), s.v. 'berakah': 'Heb. berākhāh, blessing, from the stem of bērākh, \"\n               \"he blessed, which is rel. to Aram. bārākh, Arab. bāraka, Ethiop. bārāka, he blessed, Akkad. karābu (a metathesis form), \"\n               \"to bless, Ethiop. mekrab (metath.), temple. Cp. cherub, griffin.'\")\nKLN_CHERUB = (\"KLN_1966.txt leaf 155 (printed pp. 274-275), s.v. 'cherub': 'Heb. kerūbh, winged angel, prob. rel. to Akkad. karābu, \"\n              \"to bless, karibu, one who blesses, epithet of the bull-colossus, and to Heb. bērēkh, he blessed, berākhāh, blessing. \"\n              \"See berakah and cp. griffin.'\")\nKLN_GRIFFIN = (\"KLN_1966.txt leaf 367 (printed p. 681), s.v. 'griffin, griffon, gryphon': 'ME. griffon, fr. OF. grifoun (F. griffon), \"\n               \"fr. Late L. gryphus ..., fr. Gk. grūps, gen. grūpos, which was prob. borrowed from the Semites through the medium of the \"\n               \"Hittites. Cp. Heb. kerūbh, a winged angel, Akkad. karibu, epithet of the bull-colossus, lit. one who blesses, and see cherub.'\")\nKLN_EMERALD = (\"KLN_1966.txt leaf 280 (printed pp. 514-515), s.v. 'emerald': 'ME. emeraude, fr. OF. esmeralde, esmeraude (F. émeraude), \"\n               \"fr. L. smaragdus (whence also It. smeraldo, Sp. esmeralda), fr. Gk. smaragdos, maragdos, emerald, which is of Sem. origin. \"\n               \"Cp. Heb. bāreqeth, Akkad. barraqtu, emerald, lit. something flashing, a derivative of Heb. bārāq, resp. Akkad. birqu, \"\n               \"lightning, which are rel. to Aram. beraq, barqā, Arab. barq, lightning, Heb. bāraq, Aram. beraq, Arab. baraqa, Ethiop. \"\n               \"baraqa, it flashed, glistened, Akkad. barāqu, to flash. Cp. OI. marakatam, Pers. zumurrud (whence Turk. zümrüd, whence \"\n               \"Russ. izumrud), emerald, which are also Sem. loan words. Cp. also smaragd, which is a doublet of emerald.'\")\nKLN_DIXIE = (\"KLN_1966.txt leaf 256 (printed pp. 468-469), s.v. 'dixie, dixy' (mess tin): 'Hind. degchī, a small kettle, fr. Pers. \"\n             \"degcha, dimin. of deg, pot, which is rel. to Pahlavi dēg, pot, Arm. dez, heap, and to OI. dihmi, I smear, anoint, fr. I.-E. \"\n             \"base *dheigh-, *dhoigh-, *dhigh-, to form out of clay, to knead, form. See dough and cp. next word [dizdar, fr. Pers. diz, castle].'\")\nKLN_LIBERAL = (\"KLN_1966.txt leaf 476 (printed pp. 884-885), s.v. 'liberal': 'fr. liber, free, fr. I.-E. base *leudhero-s, whence also \"\n               \"Gk. eleutheros, free. This base prob. meant orig. belonging to the people ... and derives fr. base *leudho-, *leudhi-, people, \"\n               \"whence also OSlav. ljudŭ ... OE. lēod ... G. Leute ... I.-E. base *leudho-, *leudhi-, people, is a derivative of base *leudh-, \"\n               \"to grow, rise. This latter appears in OI. rōdhati, grows, rises, climbs, Avestic raoδa-, growth, authority, Toch. A lut-k, to \"\n               \"cause to grow. Cp. liberate, liberty, liege, livery ...'\")\nKLN_MAT = (\"KLN_1966.txt leaf 508 (printed pp. 948-949; Nourai's 946 = previous leaf), s.v. 'mat, adj., dull': 'F., dull, lusterless, \"\n           \"unpolished, fr. OF. mat, defeated, afflicted, depressed, dejected; dull, fr. Arab. māt in the sentence māt ash-shāh, the king has \"\n           \"died. The word mat, orig. used only as a term of chess, gradually developed also the meanings faint, feeble, dull-colored. See \"\n           \"checkmate and cp. matador, mate, adj.'; s.v. 'matador': 'Sp., killer, murderer, fr. matar, to kill, murder, fr. Arab. māta, he \"\n           \"died. Cp. checkmate. Cp. also mat, dull'; s.v. 'mate, tr. v.' (checkmate): 'ME. maten, fr. OF. mater, to defeat, overcome, fr. \"\n           \"mat, checkmated; defeated, overcome'; 'mate, n., checkmate. — ME. mat, fr. MF., fr. OF.' Same leaf.\")\nKLN_CHECK = (\"KLN_1966.txt leaf 154 (printed pp. 272-273), s.v. 'check' (chess): '... fr. Pers. shāh, king (in the Arab.-Pers. phrase \"\n             \"shāh māt, the king is dead) ... cp. checkmate, chess, checker, exchequer'; 'checkmate' on the same leaf ends '(cp. also It. \"\n             \"scaccomatto). See check, a sudden stop, and cp. mate, checkmate.'\")\nFVQ_BARAKA = (\"FVQ_pages.txt leaf 92 (Jeffery p. 75), s.v. Baraka: 'To bless. ... The primitive verb b-r-k, which is not used in the \"\n              \"Qur'an, means to kneel, used specially of the camel, so that baraka is the technical word for making a camel kneel. In this \"\n              \"primitive sense it is common Semitic ... It was in the N. Semitic area, however, that the root seems to have developed the \"\n              \"sense of to bless, and from thence it passed to the S. Semitic area. Thus we have Heb. bērēk, and Phon. brk to bless; Aram. \"\n              \"brk to bless or praise; Syr. barrek ... From this N. Semitic sense we find derived the Sab. brk, Eth. bāraka to bless, \"\n              \"celebrate the praises of, and Ar. bāraka as above.'\")\nFVQ_MARJAN = (\"FVQ_pages.txt leaf 278 (Jeffery p. 261), s.v. Marjān: 'Small pearls. The word occurs only in a description of Paradise, \"\n              \"and was early recognized as borrowed from Persia, but it is certain that it did not come directly from Iranian into Arabic. \"\n              \"We find in Phlv. murvārīt, a pearl used, e.g. in the Gōsht-i-Fryānō, ii, 13 ... From Middle Persian the word was borrowed \"\n              \"widely, e.g. Gk. margarites; Aram. margānītā; Syr. margānītā, and from some Aram. form it came into Arabic. It would have \"\n              \"come at an early date for it is used in the old poetry ...' (fn. 5: 'In spite of Addai Sher, 144, and his attempted \"\n              \"derivation from ...'; fn. 6 cites Horn, Grundriss 218 n.).\")\nPOK_DHEIGH = (\"POK_01.txt leaves 255-256 (IEW pp. 244-245), s.v. dheiĝh-: 'Lehm kneten und damit mauern oder bestreichen (Mauer, Wall; \"\n              \"Töpferei; dann auch von anderweitigem Bilden); auch vom Teig kneten (Bäckerei)'; dheiĝho-s, dhoiĝho-s 'Gebilde, Wall' ... \"\n              \"'ai. dēhmi bestreiche ... dehī f. Wall, Damm, Aufwurf, av. pairi-daēzayeiti mauert ringsum ... uz-daēza- m. Aufhäufung, \"\n              \"Wall, pairi-daēza- m. Umfriedigung (daraus gr. paradeisos), apers. didā Festung (aus *dizā-, Wurzelnom. auf -ā), npers. \"\n              \"diz, dez ds.; ... gr. teichos n., toichos m. Mauer, Wand; ... lat. fingō ... figūra Bildung, Gestalt, Figur, fictiō ...; \"\n              \"got. daigs m. Teig (*dhoighos), anord. deig, ags. dāg, ahd. teig ds.'\")\nPOK_LEUDH = (\"POK_02.txt leaf 345 (IEW pp. 684-685), s.v. 1. leudh-: 'emporwachsen, hochkommen; leudho-, leudhi- Nachwuchs, Volk; \"\n             \"leudhero- zum Volk gehörig, frei. Ai. rōdhati, rōhati steigt, wächst, av. raoδaiti wächst, ... av. raoδa- m. Wuchs, Ansehen, \"\n             \"npers. rōi Gesicht; gr. eleutheros frei aus *leudhero-s = lat. līber frei; ... got. liudan, ahd. liotan, as. liodan, ags. \"\n             \"lēodan wachsen ... got. ludja Antlitz (vgl. np. rōi) ... ahd. liut, ags. lēod Volk, mhd. liute Leute ...'\")\nPOK_MAD = (\"POK_02.txt leaf 355 (IEW pp. 694-695), s.v. mad-: 'naß, triefen; auch von Fett triefen, vollsaftig, fett, gemästet' ... \"\n           \"'lat. madeō, -ēre naß sein, von Nässe triefen, reifen, voll sein, mattus trunken (*madi-to-s)'.\")\nAHD_DHEIGH = (\"AHD_watkins1985.txt line 377 s.v. dheigh-: 'To form, build. 1. Germanic *daigjōn in Old English dǣge, bread kneader: \"\n              \"DAIRY. 2. Germanic *-dig- in Old English compound hlǣfdige, mistress of a household (< bread kneader; hlāf, bread, loaf): \"\n              \"LADY. 3. Extended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dāg, dough: DOUGH ... 4. Suffixed zero-grade \"\n              \"form *dhigh-ūrā, in Latin figūra, form, shape (< result of kneading): FIGURE ... 5. Nasalized zero-grade form *dhi-n-gh- in \"\n              \"Latin fingere, to shape: FEIGN, FICTION, FIGMENT; EFFIGY ... 7. Suffixed o-grade form *dhoigh-o- in Avestan daēza-, wall \"\n              \"(originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.]' (same list online at \"\n              \"ahdictionary.com/word/indoeurop.html#dheigh-).\")\nAHD_PARADISE = (\"AHD online (archived) s.v. paradise: '[Middle English paradis, from Old French, from Late Latin paradīsus, from Greek \"\n                \"paradeisos, garden, enclosed park, paradise, from Avestan pairidaēza-, enclosure, park : pairi-, around; see per1 ... + \"\n                \"daēza-, wall; see dheigh- ...]'. Nourai's AHD:950 is the 1976 page of this same entry.\")\nAHD_MARGAR = (\"AHD_watkins1985.txt line 725: '[margarītēs. Pearl. Greek noun of Oriental origin (probably immediately from Iranian). \"\n              \"Greek margarītēs, margaron, pearl: MARGARIC, MARGARIC ACID, (MARGARINE), MARGARITE1, MARGARITE2.]' Online AHD s.v. \"\n              \"margarite (archived): 'Ultimately from Greek margarītēs, pearl, perhaps of Iranian origin; perhaps akin to Avestan \"\n              \"mərəγa-, bird'.\")\nHRN_DIVAR = (\"HRN.txt leaf 154 (Horn p. 133), No. 599: 'dīvār Mauer, Wand. ap. *deghavāra- (vergl. gr. teichos, osk. feíhúss). \"\n             \"Nöldeke (mündliche Mitteilung), unter der Voraussetzung, dass die np. Grundform *dēvār lautete ...; kurd. LW. dīwār; \"\n             \"wax. LW. dival, sar. delvūl Mauer, Wand, Umwallung.' Cf. No. 563 (leaf 146, p. 125): 'diz, dez Burg ... ap. didā Festung; \"\n             \"aw. daēza-; phlv. d(i)z ... Ascoli's Erklärung von np. dīvār Mauer aus ap. *didavara- Stadtwall ist daher nicht \"\n             \"wahrscheinlich'.\")\nHUB_DEG = (\"HUB.txt leaf 75 (Hübschmann p. 65), No. 594: 'Wenn dēz, dēza Kochtopf zu got. deigan kneten, aus Thon formen (Wzl. \"\n           \"dheigh) gehört, ist es verwandt mit Nr. 563 diz, dēz Burg. Ob auch dēg Kochtopf dazu gehört, ist fraglich, da 1) idg. dhigh \"\n           \"durch skr. dēgdhi, digdha- nicht gesichert ist und 2) idg. dhoigho- im Neup. zu *dēy werden müsste. Np. dēg (afgh. LW. dēg \"\n           \"Kessel) setzt ap. *daika- voraus. Phl. dēg Kessel (Gl. and Ind. 288) kann eine junge Form sein.' No. 599 (same page): \"\n           \"'Besser *daidavara- (Festungsmauer) als *daigavara- anzusetzen ... Falls dīvār (mit ī) die ursprüngliche Form ist ..., wäre \"\n           \"dīvār über *diyvār = *did-vār auf ap. *dida-vara- zurückzuführen. Alles unsicher.'\")\nKNT_DIDA = (\"KNT.txt leaf 214 (Kent p. 191): 'didā- sb. wall, stronghold, fortress: NPers. diz, pIE *dhiĝhā-, cf. Skt. dehī- wall, \"\n            \"Gk. teichos, NEng. dike, ditch ... Cf. also paradayadām. didā nsf. DB 1.58; 2.39, 44; 3.61, 72; DSe 46; DSf 42. didām asf. \"\n            \"DB 2.78; DSe 48; DSf 54.'\")\nIEC_DHEIGH = (\"IEC.txt leaf 112 (Mann cols ~193-194), s.v. dheigh-: 'shape, earth up; form, wall ... Cf. dhoigh- Skt. dehah \"\n              \"shape, body; Av. (pairi-)daēzō surrounding fence beside diz- earth up, cover; LW in Arm. dez mound, dizem pile up; Gk. \"\n              \"teikhos outer wall, dam; Osc. feíhúss, acc.pl. walls; Go. digan (z-gde) shape, mould ... For Cz. díže kneading-trough and \"\n              \"OHG teic, E dough, etc. see dhoiĝh-.'\")\nSOD_DYZ = (\"SOD_pages.txt leaf 216 (Gharib p. 151), entry 3825: 'δyz' M — δiza (dyz') < OP didā, f. n., stronghold, fort. BBB f 57; \"\n           \"STii 3.27'; entry 3826 'dyz' C = δyz''.\")\nSOD_RWD = (\"SOD_pages.txt leaf 411 (Gharib p. 344), entry 8562: 'rwδ- B, M, S — rōδ < Av. raod-; *fraud-; Parth. rōd-; Khot. rw-; \"\n           \"Yaghn. ur-; inf. -y; (to) grow. BBB 580; GMS 586; TSP 2.10, 18 ...'; entry 8563 'rwd C = rwδ-'.\")\nSYN_874 = (\"SYN.txt leaf 946 (Buck p. 875; leaf 945 = p. 874), in 12.51 FORM/SHAPE (OCR garbled): '... OS liodan spring up, grow, \"\n           \"Skt. rudh-, Av. raod- grow (12.53). Walde-P. 2.416. Feist 323.' Buck lists the Avestan word only as 'grow'; the 'face' \"\n           \"gloss and the raoδa-taxma compound are not on this page.\")\nBQT_DEZ = (\"BQT_v2_pages.txt leaf 311 (printed p. ~854; Nourai 851): 'دژ = بکسر اول و سکون ثانی، قلعه و حصار باشد' with footnote \"\n           \"marker ۱; Mo'in's footnote (Pahlavi/Avestan forms) is not legible in the OCR of this leaf.\")\nBQT_DIG = (\"BQT_v2_pages.txt leaves 371-372 (printed pp. ~914-915): the دیگ entry area; leaf 371 footnote cites 'Henning, Two \"\n           \"Central Asian words, Hertford 1946' and leaf 372 mentions «دیگه» and دیزی (فرهنگ اسدی); Mo'in's Latin-script Pahlavi/Old \"\n           \"Persian forms are not legible in the OCR.\")\nBQT_PALIZ = (\"BQT_v1_pages.txt leaf 581 (printed p. ~361; Nourai 359): 'پالیز ۱ - بر وزن کاریز، بمعنی باغ و بوستان و کشتزار باشد \"\n             \"عموماً و خربزه‌زار و خیارزار و هندوانه‌زار را گویند خصوصاً'; Mo'in's etymological footnote ۱ is not legible in the OCR.\")\nBQT_RAZ = (\"BQT_v2_pages.txt leaf 404 (printed p. ~947; Nourai 944): 'رز = بفتح اول و سکون ثانی، درخت انگور باشد و به عربی کرم خوانند \"\n           \"... و باغ را گویند و بمعنی انگور هم آمده است'; Mo'in's footnote on this leaf is illegible (only a Henning BSOS reference \"\n           \"survives), so the claimed link to rūy/rustan cannot be confirmed here.\")\nBQT_ROSTAM = (\"BQT_v2_pages.txt leaf 408 (printed p. ~951), Mo'in's footnote s.v. رستم: 'رستم = رستهم: رو (بالش، نمو) [رستن و \"\n              \"روییدن از همین ریشه است] + تهم = tahm در پارسی باستان، گاتها و دیگر بخشهای اوستا بمعنی دلیر و پهلوان؛ تهمتن نیز از \"\n              \"همین ریشه است بمعنی بزرگ‌پیکر و قوی‌اندام ... رستم یعنی کشیده‌بالا و بزرگ‌تن و قوی‌پیکر (یشتها ۲ ص ۱۳۹) ... مارکوارت \"\n              \"تصور کرده است که رئوتس‌تخم (اوستا) عنوان و صفتی برای ... ' — i.e. Mo'in derives Rostam from rō 'growth' + tahm \"\n              \"'strong', exactly Nourai's raoδa-taxma.\")\nFSF_RAZ = (\"FSF_pages.txt leaf 265 (page numeral illegible; Nourai p. 199), s.v. 'رز (با زبر اول): ۱- باغ. ۲- انگور: چو ببرید رستم \"\n           \"تن شاخ گز / بیامد ز دریا به ایوان و رز'. A Shahnameh glossary: confirms the word and glosses (garden, vine), gives no etymology.\")\nAFM_RAWNAQ = (\"AFM_pages.txt leaf 75 (Addi Shir p. ~74): '(الرونق) حسن كل شيء، معرب رو أي وجه ومن نيك أي صبيح' — i.e. rawnaq is an \"\n              \"Arabicized compound of Persian rū 'face' + nīk 'fair', exactly Nourai's arrow.\")\nAFM_RAWDA = (\"AFM_pages.txt leaf 76 (Addi Shir p. ~75): '(الروضة) من الرمل والعشب مستنقع الماء ... وهي من ريختن أي صبّ، أخذتها العرب \"\n             \"وتصرفت بها' — Addi Shir derives rawḍa from Persian rīxtan 'to pour', not from raz.\")\nFSD_MAT = (\"FSD_vol3.txt leaf 51 (printed p. ~1517; Nourai 1526), s.v. mat (dull surface) — OCR badly garbled, but the etymology \"\n           \"bracket reads '[< F. mat(t), dull, < L. mattus; see MATE2]'. Funk & Wagnalls thus takes French mat from Latin mattus and \"\n           \"refers the reader to the checkmate word (mate2) for the Arabic origin.\")\nFSD_526 = (\"FSD_vol1.txt: printed p. 526 (leaf ~575) is in the C's ('coerce' etc.) and has no 'mat'; the checkmate entry is at p. 457 \"\n           \"(leaf 511): 'check'mate, v. ... Chess. To put (an opponent's king) in a check from which no escape is possible ... 2. Hence, to \"\n           \"discomfit or defeat'. Nourai's 526 is probably a misprint for 1526 (vol. 3, the mat entry).\")\nPHN_MAT = (\"PHN.txt leaf 288 (Pihan p. 257): 'MAT, adj. m. (p.) [māt] défait, réduit à l'extrémité. — Faire mat ou mater veut dire, au \"\n           \"jeu d'échecs, mettre le roi dans l'impossibilité de changer de place, ce qui termine la partie. Voyez Échec. — Par extension, \"\n           \"le verbe mater s'emploie aussi au figuré, dans le sens de dompter, humilier, affaiblir, abattre'. Pihan tags the word '(p.)' \"\n           \"= Persian.\")\nDEV_MAT = (\"DEV.txt leaf 192 (Devic p. 159): 'Mat. Terme du jeu des échecs. (Voy. Échec.) Mat, adjectif, au sens de terne, vient du \"\n           \"mat des échecs. « Dans les anciens auteurs, dit M. Littré, mat signifie las, humilié; c'est de ce sens qu'on est allé au sens \"\n           \"de terne, qui paraît très-récent. » ... Il est remarquable qu'en hindoustani le terme māt, importé du persan, a aussi les \"\n           \"deux sens'.\")\nLKT_MAT = (\"LKT.txt leaf 142 (Lokotsch p. 115), No. 1443: 'Ar. māt(a): Er ist gestorben, tot; als Fachausdruck der Schachspieler šāh \"\n           \"māt vom pers. šāh König [Horn NpEt S. 170, Nr. 772]: Der König ist tot; hieraus ist mit dem Schachspiele selbst der Ausdruck \"\n           \"international geworden, vor allem it. scacco matto schachmatt, prov. mat, frz. échec et mat, sp. jaque y mate ..., pg. \"\n           \"chaque e mate, rum. mat; dtsch. schachmatt, engl. checkmate ... Dazu die Vb. it. mattare, frz. mater, prov. kat. sp. pg. \"\n           \"matar mattsetzen, überwinden, besiegen und schließlich sp. pg. matar töten [und nicht etwa < lat. mactare ...]'.\")\nSKT_EMERALD = (\"SKT.txt leaf 156 (Skeat 1911 p. ~136; Nourai's 163 is another printing), s.v. Emerald: '(F. — L. — Gk.) M.E. emeraude \"\n               \"— O.F. esmeraude — L. smaragdum, acc. of smaragdus — Gk. smaragdos, an emerald. Cf. Skt. marakata (the same).'\")\nMON_ZOMORROD = (\"vajehyab.com (Mo'in) s.v. زمرد: '(زُ مُ رُّ) [معر - یو.] (اِ.) یکی از سنگ های قیمتی به رنگ سبز' — Mo'in tags it \"\n                \"'Arabicized, from Greek' (page numbers of the print edition cannot be mapped online).\")\n\ndef add_sources(node, urls):\n    for u in urls:\n        if u not in node[\"sources\"]:\n            node[\"sources\"].append(u)\n\n# ------------------------------------------------------------------ page 101\nP101 = {\n    (0, \"root\"): [\n        rc(\"FVQ:75\", \"supports\", FVQ_BARAKA + \" — exactly Nourai's 'kneel (of the camel) → bless' story.\"),\n    ],\n    (0, 1): [\n        rc(\"KLN:164\", \"supports\", KLN_BERAKAH + \" Gives Arab. bāraka 'he blessed' under the Semitic root and the Akkadian metathesis, as the chart does.\"),\n        rc(\"FVQ:75\", \"supports\", \"Same page as the root: 'Ar. bāraka as above' derived from the N. Semitic sense 'to bless' (FVQ_pages.txt leaf 92).\"),\n    ],\n    (0, 2): [NC(\"FVA:45\", no_FVA)],\n    (0, 3): [\n        rc(\"KLN:164\", \"supports\", KLN_BERAKAH + \" Klein calls Akkad. karābu 'a metathesis form' of b-r-k — Nourai's 'letters are interchanged'.\"),\n        rc(\"AHD:579\", \"partial\", \"AHD:579 is the 1976 dictionary page (griffin); the current AHD griffin entry (archived, \" + U_AHD(\"griffin\") + \") derives griffin only 'from Greek grūps' with no Semitic link, but the AHD Semitic-roots appendix (archived, \" + U_SEM + \") s.v. krb: 'Common Semitic root, with West Semitic metathesized variant brk. cherub, from Hebrew kərûb, cherub; akin to Akkadian karābu, to praise, bless. Compare also brk' and s.v. brk: 'West Semitic, to bless. Probably a metathesized variant of krb.' — so AHD supports the Akkadian karābu ~ brk metathesis.\"),\n    ],\n    (0, 4): [\n        rc(\"KLN:274\", \"supports\", KLN_CHERUB + \" Klein connects kerūbh with Heb. bērēkh/berākhāh via Akkad. karābu, i.e. the reversed consonants Nourai notes.\"),\n        rc(\"KLN:164\", \"supports\", KLN_BERAKAH),\n    ],\n    (0, 5): [\n        rc(\"MON:2958\", \"supports\", \"vajehyab.com (Mo'in) s.v. کروبی: '(کَ یّ) [ع.] (اِ.) فرشتة مقرب درگاه. ج. کروبیون' — tagged Arabic; Mo'in's page numbers cannot be mapped online. Archived \" + U_MON(\"کروبی\") + \".\"),\n    ],\n    (0, 6): [\n        rc(\"MON:2958\", \"supports\", \"vajehyab.com (Mo'in) s.v. کروبی [ع.] 'فرشتة مقرب درگاه، ج. کروبیون'; also کروبیان 'فرشتگان مقرب درگاه' and کروبیون 'جِ کروبی' — the Persian word is marked as an Arabic loan, as the arrow says (archived \" + U_MON(\"کروبی\") + \").\"),\n    ],\n    (0, 7): [\n        rc(\"AHD:231\", \"supports\", \"AHD online s.v. cherub (archived, \" + U_AHD(\"cherub\") + \"): '[Middle English, from Late Latin, from Hebrew kərûb; see krb in the Appendix of Semitic roots.]' — Hebrew → (Latin →) English as in the chart; AHD:231 is the 1976 page of this entry.\"),\n    ],\n    (0, 8): [\n        rc(\"KLN:680\", \"supports\", KLN_GRIFFIN + \" — Klein does derive Gk. grūps from the Semitic kerūbh/karibu word (via Hittite), Nourai's arrow.\"),\n        rc(\"AHD:579\", \"partial\", \"AHD online s.v. griffin (archived, \" + U_AHD(\"griffin\") + \"): '[Middle English griffoun, from Old French griffon, from grif, from Latin grȳpus, grȳphus, variants of grȳps, grȳp-, from Greek grūps.]' — the chain below Greek is there, but AHD does not derive Greek grūps from Hebrew kerūbh; the Semitic appendix s.v. krb lists only cherub.\"),\n    ],\n    (0, 9): [\n        rc(\"AHD:579\", \"supports\", \"AHD online s.v. griffin (archived, \" + U_AHD(\"griffin\") + \"): 'from Latin grȳpus, grȳphus, variants of grȳps, grȳp-, from Greek grūps' — Latin gryphus from Greek.\"),\n    ],\n    (0, 10): [\n        rc(\"KLN:680\", \"supports\", KLN_GRIFFIN + \" Klein: 'ME. griffon, fr. OF. grifoun (F. griffon), fr. Late L. gryphus' — OF from Latin; the OF spelling grifion in the chart is Nourai's/OCR's.\"),\n    ],\n    (0, 11): [\n        rc(\"AHD:579\", \"supports\", \"AHD online s.v. griffin (archived, \" + U_AHD(\"griffin\") + \"): '[Middle English griffoun, from Old French griffon ...]' — English from Old French.\"),\n    ],\n    (1, \"root\"): [\n        rc(\"KLN:514\", \"supports\", KLN_EMERALD + \" Klein gives the whole Semitic b-r-q 'flash, lightning' family under 'emerald'.\"),\n    ],\n    (1, 1): [\n        rc(\"KLN:514\", \"supports\", KLN_EMERALD + \" Lists 'Arab. barq, lightning ... Arab. baraqa, it flashed, glistened'.\"),\n    ],\n    (1, 2): [NC(\"FVA:45\", no_FVA), NC(\"SOR:35\", no_SOR)],\n    (1, 3): [\n        rc(\"KLN:514\", \"partial\", KLN_EMERALD + \" Klein has Akkad. barraqtu but glosses it 'emerald, lit. something flashing' (a derivative of Akkad. birqu 'lightning'); Nourai's gloss 'lightning' belongs to birqu, not to baraqtu.\"),\n    ],\n    (1, 4): [\n        rc(\"KLN:514\", \"supports\", KLN_EMERALD + \" 'Gk. smaragdos, maragdos, emerald, which is of Sem. origin. Cp. Heb. bāreqeth, Akkad. barraqtu' — the Greek form in Klein is smaragdos (with -gd-), which confirms that the chart's 'smaraldos' is a transcription slip.\"),\n    ],\n    (1, 5): [\n        rc(\"MON:1746\", \"supports\", MON_ZOMORROD + \" Mo'in's tag [معر - یو.] = Arabicized (mu'arrab) from Greek, i.e. Greek → Arabic → Persian, which is the route drawn through this empty Arabic node. Archived \" + U_MON(\"زمرد\") + \".\"),\n    ],\n    (1, 6): [\n        rc(\"MON:1746\", \"supports\", MON_ZOMORROD + \" Archived \" + U_MON(\"زمرد\") + \".\"),\n        rc(\"KLN:514\", \"partial\", KLN_EMERALD + \" Klein: 'Cp. OI. marakatam, Pers. zumurrud (whence Turk. zümrüd, whence Russ. izumrud), emerald, which are also Sem. loan words' — Klein treats zumurrud as a direct Semitic loan and does not route it through Greek/Arabic as Nourai does.\"),\n    ],\n    (1, 7): [\n        rc(\"KLN:514\", \"supports\", KLN_EMERALD + \" 'fr. L. smaragdus ..., fr. Gk. smaragdos'.\"),\n    ],\n    (1, 8): [\n        rc(\"AHD:427\", \"partial\", \"AHD:427 is the 1976 page of 'emerald'; the current AHD emerald entry (archived, \" + U_AHD(\"emerald\") + \") reads '[Middle English emeraude, from Old French, from Medieval Latin esmeralda, esmeraldus, from Latin smaragdus, from Greek smaragdos; akin to Sanskrit marakatam, probably of Semitic origin; akin to Akkadian barraqtu and Hebrew bāreqet, a kind of gemstone ...; see brq in the Appendix of Semitic roots.]' — it confirms Latin smaragdus < Greek but does not treat smaragdite (the AHD search for smaragdite, archived \" + U_AHD(\"smaragdite\") + \", returned no entry). Klein (KLN_1966.txt leaf 280-281 s.v. smaragdite): 'F., formed with subst. suff. -ite fr. Gk. smaragdos, emerald'.\"),\n    ],\n    (1, 9): [\n        rc(\"KLN:514\", \"supports\", KLN_EMERALD + \" 'ME. emeraude, fr. OF. esmeralde, esmeraude (F. émeraude), fr. L. smaragdus'.\"),\n    ],\n    (1, 10): [\n        rc(\"AHD:427\", \"supports\", \"AHD online s.v. emerald (archived, \" + U_AHD(\"emerald\") + \"): 'Middle English emeraude, from Old French, from Medieval Latin esmeralda, esmeraldus, from Latin smaragdus, from Greek smaragdos ... probably of Semitic origin; akin to Akkadian barraqtu and Hebrew bāreqet' — the whole chain of this branch, including the Semitic b-r-q root.\"),\n    ],\n    (1, 11): [\n        rc(\"KLN:514\", \"supports\", KLN_EMERALD + \" 'Cp. OI. marakatam ... which are also Sem. loan words' — Klein makes Skt. marakata a Semitic loan, as the arrow says.\"),\n        rc(\"SKT:163\", \"partial\", SKT_EMERALD + \" Skeat only compares Skt. marakata with the Greek word; he does not say it is a Semitic loan.\"),\n    ],\n}\n\n# ------------------------------------------------------------------ page 126\nP126 = {\n    (0, \"root\"): [\n        rc(\"POK:244\", \"supports\", POK_DHEIGH),\n        rc(\"KNT:191\", \"supports\", KNT_DIDA + \" Kent puts OP didā- under pIE *dhiĝhā- with Skt. dehī-, Gk. teichos.\"),\n        NC(\"CEL3:203\", no_CEL),\n    ],\n    (0, 1): [\n        rc(\"HRN:133\", \"supports\", HRN_DIVAR + \" Nourai's 'děğa-vâra' is Horn's *deghavāra-; his 'didâ' is Horn's/Kent's ap. didā. (Horn himself, No. 563, rejects deriving dīvār from *dida-vara-.)\"),\n        rc(\"KNT:191\", \"supports\", KNT_DIDA),\n        rc(\"IEC:191\", \"partial\", IEC_DHEIGH + \" Mann gives the root and Av. (pairi-)daēza- but does not list Old Persian didā- or *daiga-vāra-.\"),\n    ],\n    (0, 2): [\n        rc(\"BQT:918\", \"not_found\", \"BQT_v2_pages.txt leaves 375-378 (printed pp. ~918-921) are the دیو- entries, but the دیوار headword and Mo'in's footnote are not recoverable from the OCR (only the following entry 'دیوال = با لام، بر وزن و معنی دیوار است، چه در فارسی را و لام بهم تبدیل می‌یابند' on leaf 378 is legible). Mo'in's online text (vajehyab) tags دیوار [په.] = Pahlavi (refs_online.json note).\"),\n    ],\n    (0, 3): [\n        rc(\"SOD:151\", \"supports\", SOD_DYZ + \" Gharib derives Sogdian δyz' 'stronghold, fort' from OP didā — exactly the arrow drawn from node #1.\"),\n    ],\n    (0, 4): [\n        rc(\"POK:244\", \"supports\", POK_DHEIGH + \" Pokorny: 'uz-daēza- m. Aufhäufung, Wall, pairi-daēza- m. Umfriedigung' under dheiĝh-.\"),\n    ],\n    (0, 5): [\n        rc(\"BQT:851\", \"partial\", BQT_DEZ),\n        NC(\"MON5:528\", no_MON5),\n    ],\n    (0, 6): [\n        rc(\"POK:244\", \"supports\", POK_DHEIGH + \" 'pairi-daēza- m. Umfriedigung (daraus gr. paradeisos)'.\"),\n    ],\n    (0, 7): [\n        rc(\"BQT:359\", \"partial\", BQT_PALIZ + \" The gloss (garden, melon field) matches; the derivation from pairi-daēza- is in Mo'in's note, which the OCR does not preserve.\"),\n        rc(\"MON:680\", \"partial\", \"vajehyab.com (Mo'in) s.v. پالیز: '(اِ.) ۱- باغ، بوستان. ۲- کشتزار. ۳- زمینی که در آن خربزه، خیار و مانند آن بکارند' — meaning confirmed; the online text carries no origin tag or Avestan form for this entry. Archived \" + U_MON(\"پالیز\") + \".\"),\n    ],\n    (0, 8): [NC(\"BQT:1455\", no_BQT3)],\n    (0, 9): [\n        rc(\"AHD:950\", \"supports\", AHD_PARADISE),\n    ],\n    (0, 10): [NONE(\"The AHD paradise entry checked at node #9 (archived \" + U_AHD(\"paradise\") + \") gives 'Middle English paradis, from Old French, from Late Latin paradīsus, from Greek paradeisos'.\")],\n    (0, 11): [\n        rc(\"HUB:65\", \"partial\", HUB_DEG + \" Hübschmann does posit ap. *daika- for np. dēg (Nourai's 'daika'), but he explicitly doubts that dēg belongs to the root dheigh- ('ist fraglich').\"),\n        rc(\"KLN:469\", \"supports\", KLN_DIXIE + \" Klein derives Pers. deg 'pot' (Pahlavi dēg) from I.-E. *dheigh- 'to form out of clay' — the arrow from the root; he does not give an Old Persian form.\"),\n    ],\n    (0, 12): [\n        rc(\"BQT:912,914\", \"partial\", BQT_DIG),\n        rc(\"KLN:469\", \"supports\", KLN_DIXIE),\n    ],\n    (0, 13): [\n        rc(\"AHD\", \"supports\", AHD_DHEIGH + \" Germanic *daigaz 'dough' and OE dǣge 'bread kneader' (DAIRY), hlǣfdige (LADY) are items 1-3.\"),\n    ],\n    (0, 14): [NONE(\"Covered by the AHD dheigh- entry checked at node #13: DAIRY, LADY, DOUGH.\")],\n    (0, 15): [\n        rc(\"AHD\", \"supports\", AHD_DHEIGH + \" Item 4: '*dhigh-ūrā, in Latin figūra, form, shape (< result of kneading): FIGURE'.\"),\n    ],\n    (0, 16): [NONE(\"Covered by the AHD dheigh- entry checked at node #15: FIGURE; FICTION (item 5, Latin fingere).\")],\n}\n\n# ------------------------------------------------------------------ page 311\nP311 = {\n    (0, \"root\"): [\n        rc(\"POK:684\", \"supports\", POK_LEUDH + \" Pokorny's 1. leudh- 'emporwachsen' with av. raoδa- 'Wuchs' and npers. rōi 'Gesicht' is the root Nourai draws (his second name 'Rei' is not in Pokorny under this root).\"),\n        rc(\"KLN:885\", \"supports\", KLN_LIBERAL),\n        rc(\"SYN:874\", \"partial\", SYN_874),\n        NC(\"VDQ:39\", no_VDQ),\n    ],\n    (0, 1): [\n        rc(\"KLN:885\", \"supports\", KLN_LIBERAL + \" 'Avestic raoδa-, growth, authority' under base *leudh- 'to grow, rise'.\"),\n        rc(\"SYN:874\", \"partial\", SYN_874),\n    ],\n    (0, 2): [\n        rc(\"BQT:944\", \"partial\", \"The روییدن/روی entries (BQT_v2_pages.txt leaves ~400-403, printed pp. ~944-946) are not legible in the OCR; but Mo'in's footnote s.v. رستم (leaf 408) states 'رو (بالش، نمو) [رستن و روییدن از همین ریشه است]', i.e. rūyīdan and rustan come from rō 'growth'. Pokorny 684 (checked at the root) gives 'npers. rōi Gesicht' under leudh-, the 'face' word of this node.\"),\n    ],\n    (0, 3): [\n        rc(\"BQT:944\", \"partial\", BQT_RAZ),\n        rc(\"FSF:199\", \"partial\", FSF_RAZ),\n    ],\n    (0, 4): [\n        NC(\"PLA:138\", no_PLA),\n        rc(\"AFM:75\", \"contradicts\", AFM_RAWDA + \" Cited by Nourai only in his NOTE as the dissenting view; it does not support the arrow raz → rawḍa.\"),\n    ],\n    (0, 5): [\n        rc(\"MON\", \"supports\", \"vajehyab.com (Mo'in) s.v. روضه: '(رَ ض) [ع. روضة] (اِ.) ۱- باغ، گلزار. ج. ریاض، روضات. ۲- مطالب و اشعاری که هنگام عزا ... می‌خوانند' — Persian rowzeh marked as Arabic rawḍa, as the arrow says. Archived \" + U_MON(\"روضه\") + \".\"),\n    ],\n    (0, 6): [NONE(\"Addi Shir's rawnaq entry checked at node #7 presupposes Persian rū + nīk.\")],\n    (0, 7): [\n        rc(\"AFM:74\", \"supports\", AFM_RAWNAQ),\n    ],\n    (0, 8): [\n        rc(\"MON:1694\", \"supports\", \"vajehyab.com (Mo'in) s.v. رونق: '(رُ نَ) [ع.] (اِمص.) ۱- فروغ، روشنایی. ۲- زیبایی، جمال. ۳- رواج' — tagged Arabic. Archived \" + U_MON(\"رونق\") + \".\"),\n    ],\n    (0, 9): [\n        rc(\"MON:1689\", \"partial\", \"vajehyab.com (Mo'in) s.v. روستا: '(اِ.) ده، قریه' — the online Mo'in text gives the meaning only; the print edition's Pahlavi form (rōstāk) is stripped online, so the Pahlavi → Persian arrow cannot be confirmed from it. Archived \" + U_MON(\"روستا\") + \".\"),\n    ],\n    (0, 10): [\n        rc(\"IEC:1103\", \"not_found\", \"IEC.txt leaves 604-607 (Mann cols ~1097-1104) contain the roudh-/rudh- 'red, rust' entries; no rōstāk/rūstā 'village' is there. Mann does list 'Per. cf. rustan, rostan, inf. grow; rust, rost growth' under ordhos (1) 'erect; growth; grow, rise' (IEC.txt line 12277), i.e. under a different root.\"),\n        rc(\"MON:1689\", \"partial\", \"vajehyab.com (Mo'in) s.v. روستا: 'ده، قریه' — meaning only, no origin tag online. Archived \" + U_MON(\"روستا\") + \".\"),\n    ],\n    (0, 11): [\n        rc(\"KLN:885\", \"partial\", KLN_LIBERAL + \" Klein has Avestic raoδa- 'growth' but not the compound raoδa-taxma / Rostam.\"),\n        rc(\"SYN:874\", \"partial\", SYN_874),\n    ],\n    (0, 12): [\n        rc(\"BQT\", \"supports\", BQT_ROSTAM),\n    ],\n    (0, 13): [NC(\"VDQ:39\", no_VDQ), NC(\"MAG:186\", no_MAG)],\n    (0, 14): [NC(\"MAG:186\", no_MAG), NC(\"VDQ:39\", no_VDQ)],\n    (0, 15): [NC(\"VDQ:39\", no_VDQ), NC(\"MAG:186\", no_MAG)],\n    (0, 16): [\n        rc(\"MON:1378\", \"supports\", \"vajehyab.com (Mo'in) s.v. حور: '[ع.] (اِ.) ۱- زن سیاه چشم. ۲- زن زیباروی'; حوری '[ع - فا.] زن بهشتی' — Persian ḥūr marked as Arabic. Archived \" + U_MON(\"حور\") + \".\"),\n    ],\n    (0, 17): [\n        rc(\"SOD:344\", \"supports\", SOD_RWD + \" Gharib derives Sogdian rwδ- 'to grow' from Av. raod-, the root of this chart.\"),\n    ],\n    (0, 18): [\n        rc(\"KLN:885\", \"supports\", KLN_LIBERAL + \" '*leudhero-s ... derives fr. base *leudho-, *leudhi-, people ... a derivative of base *leudh-, to grow, rise' — both of Nourai's forms.\"),\n    ],\n    (0, 19): [NONE(\"Klein s.v. liberal (checked at #18): 'fr. liber, free, fr. I.-E. base *leudhero-s'; Pokorny 684 (root): 'gr. eleutheros frei aus *leudhero-s = lat. līber frei'.\")],\n    (0, 20): [NONE(\"Klein (KLN_1966.txt leaf 285, s.v. deliver): 'OF. delivrer ... fr. VL. dēlīberāre, fr. de- and līberāre, to set free, fr. līber, free'; Klein s.v. Latvia (leaf ~445): 'the country of the Letts', which he does not connect with *leudh-.\")],\n}\n\n# ------------------------------------------------------------------ page 345\nP345 = {\n    (0, \"root\"): [\n        NC(\"PLA:247\", no_PLA),\n        rc(\"FVQ:261\", \"supports\", FVQ_MARJAN + \" Jeffery's Phlv. murvārīt is Nourai's root form.\"),\n    ],\n    (0, 1): [\n        NC(\"BQT:1997\", no_BQT3 + \" (BQT:1997 would be vol. 4).\"),\n        rc(\"FVQ:261\", \"supports\", FVQ_MARJAN + \" (Persian morvārīd is the NP continuation of the Phlv. murvārīt Jeffery quotes; fn. 6 cites Horn, Grundriss 218 n.)\"),\n        NC(\"KGW:112\", no_KGW),\n    ],\n    (0, 2): [\n        rc(\"FVQ:261\", \"supports\", FVQ_MARJAN + \" 'From Middle Persian the word was borrowed widely, e.g. ... Aram. margānītā; Syr. margānītā, and from some Aram. form it came into Arabic' — the Aramaic intermediary of this empty node.\"),\n    ],\n    (0, 3): [\n        rc(\"FVQ:261\", \"supports\", FVQ_MARJAN + \" Arabic marjān 'small pearls' from an Aramaic form of the Middle Persian word.\"),\n        NC(\"PLA:247\", no_PLA),\n    ],\n    (0, 4): [NC(\"BQT:1981\", no_BQT3 + \" (BQT:1981 would be vol. 4).\")],\n    (0, 5): [\n        rc(\"AHD:1527\", \"supports\", AHD_MARGAR + \" AHD:1527 is the 1976 appendix page of this same entry.\"),\n        NC(\"KGW:111\", no_KGW),\n        rc(\"FVQ:261\", \"supports\", FVQ_MARJAN + \" 'From Middle Persian the word was borrowed widely, e.g. Gk. margarites' (fn. 7: 'Also margaris ..., from which comes the Arm. margarit and the European forms').\"),\n    ],\n    (0, 6): [NONE(\"Klein (KLN_1966.txt leaf 504, s.v. margarite): 'ME., fr. OF. margarite (F. marguerite), fr. L. margarita, fr. Gk. margarites'.\")],\n    (0, 7): [NONE(\"Klein (KLN_1966.txt leaf 504, s.v. margarite/Margaret): 'OF. margarite (F. marguerite), fr. L. margarita'; 'Margaret ... OF. Margaret, fr. L. margarita, pearl'.\")],\n    (0, 8): [NONE(\"AHD_watkins1985.txt line 725 lists MARGARIC, MARGARINE, MARGARITE under margarītēs; Klein (leaf 504) s.v. Margaret 'fr. L. margarita, pearl' and s.v. margarine 'F.; ... fr. margarique ... fr. Gk. margaron, pearl'.\")],\n    (2, \"root\"): [\n        NC(\"FVA:384\", no_FVA),\n        rc(\"KLN:946\", \"supports\", KLN_MAT + \" Klein derives mat, matador, mate (checkmate) from Arab. māt/māta 'he died'.\"),\n    ],\n    (2, 1): [NC(\"FVA:387\", no_FVA)],\n    (2, 2): [\n        NC(\"FVA:387\", no_FVA),\n        rc(\"MON:3678,4421\", \"supports\", \"vajehyab.com (Mo'in) s.v. موت: '(مَ) [ع.] (اِ.) مرگ' (tagged Arabic; archived \" + U_MON(\"موت\") + \"); s.v. مات: '(ص.) ۱- حیران، سرگشته. ۲- (اِ.) وضعیتی در بازی شطرنج که شاه قادر به هیچ حرکتی نیست و بازی به اتمام می‌رسد' and 'شاه مات: هنگامی که شاه شطرنج مات شود' (no origin tag shown online; archived \" + U_MON(\"مات\") + \").\"),\n    ],\n    (2, 3): [\n        rc(\"FSD:1526\", \"partial\", FSD_MAT + \" It gives Latin mattus as the source of French mat, but does not itself derive mattus from Arabic māt.\"),\n        rc(\"POK:694\", \"contradicts\", POK_MAD + \" Pokorny derives Latin mattus 'drunk' from *madi-to-s (root mad- 'wet'), not from Arabic — the dissent Nourai records in his NOTE.\"),\n    ],\n    (2, 4): [\n        rc(\"FSD:1526\", \"supports\", FSD_MAT + \" French mat 'dull' from Latin mattus, as the arrow says.\"),\n    ],\n    (2, 5): [\n        rc(\"FSD:526\", \"not_found\", FSD_526),\n        rc(\"AHD:805\", \"contradicts\", \"AHD online s.v. mat 2 (archived, \" + U_AHD(\"mat\") + \"): '[From French, dull, from Old French, defeated, withered, perhaps from Latin mattus, stupefied, senseless, possibly from *maditus, past participle of madēre, to be wet.]' — English mat from French mat is confirmed, but AHD traces the word to Latin madēre (root mad-), not to Arabic māt; Nourai's NOTE acknowledges this. (AHD s.v. matte 2, archived \" + U_AHD(\"matte\") + \": 'from Old French, dull, from Latin mattus, stupefied; see MAT2'.)\"),\n    ],\n    (2, 6): [\n        rc(\"PHN:257\", \"supports\", PHN_MAT),\n        rc(\"DEV:159\", \"supports\", DEV_MAT),\n    ],\n    (2, 7): [\n        rc(\"LKT:115\", \"supports\", LKT_MAT),\n        rc(\"KLN:946\", \"supports\", KLN_MAT + \" Also KLN s.v. check (\" + KLN_CHECK + \").\"),\n    ],\n    (2, 8): [\n        rc(\"KLN:946\", \"supports\", KLN_MAT + \" 'matador ... fr. matar, to kill, murder, fr. Arab. māta, he died' — Nourai's arrow. (AHD s.v. matador, archived \" + U_AHD(\"matador\") + \", prefers 'possibly from Vulgar Latin *mattāre, to beat senseless, perhaps from Latin mattus'; Lokotsch 1443 sides with Klein: 'sp. pg. matar töten' from the chess word.)\"),\n    ],\n    (2, 9): [\n        rc(\"MON:3678\", \"supports\", \"vajehyab.com (Mo'in) s.v. ماتادور: '(دُ) [فر.] (اِ.) کسی که در میدان عمومی با گاو مبارزه می‌کند، گاوباز' — Mo'in marks the Persian word as a French loan, i.e. the French node is the immediate source. Archived \" + U_MON(\"ماتادور\") + \".\"),\n    ],\n    (2, 10): [\n        rc(\"MON:3678\", \"supports\", \"vajehyab.com (Mo'in) s.v. ماتادور [فر.] 'گاوباز' — French → Persian as drawn. Archived \" + U_MON(\"ماتادور\") + \".\"),\n    ],\n    (2, 11): [\n        rc(\"KLN:946\", \"supports\", KLN_MAT + \" 'matador, n. ... Sp., killer, murderer' — English from Spanish.\"),\n    ],\n}\n\n# web URLs to append to sources, per (page, entry, node)\nWEB = {\n    (101, 0, 3): [U_AHD(\"griffin\"), U_SEM],\n    (101, 0, 5): [U_MON(\"کروبی\")],\n    (101, 0, 6): [U_MON(\"کروبی\")],\n    (101, 0, 7): [U_AHD(\"cherub\")],\n    (101, 0, 8): [U_AHD(\"griffin\")],\n    (101, 0, 9): [U_AHD(\"griffin\")],\n    (101, 0, 11): [U_AHD(\"griffin\")],\n    (101, 1, 5): [U_MON(\"زمرد\")],\n    (101, 1, 6): [U_MON(\"زمرد\")],\n    (101, 1, 8): [U_AHD(\"emerald\"), U_AHD(\"smaragdite\")],\n    (101, 1, 10): [U_AHD(\"emerald\")],\n    (126, 0, 7): [U_MON(\"پالیز\")],\n    (126, 0, 9): [U_AHD(\"paradise\")],\n    (126, 0, 10): [U_AHD(\"paradise\")],\n    (311, 0, 5): [U_MON(\"روضه\")],\n    (311, 0, 8): [U_MON(\"رونق\")],\n    (311, 0, 9): [U_MON(\"روستا\")],\n    (311, 0, 10): [U_MON(\"روستا\")],\n    (311, 0, 16): [U_MON(\"حور\")],\n    (345, 2, 2): [U_MON(\"موت\"), U_MON(\"مات\")],\n    (345, 2, 5): [U_AHD(\"mat\"), U_AHD(\"matte\")],\n    (345, 2, 8): [U_AHD(\"matador\")],\n    (345, 2, 9): [U_MON(\"ماتادور\")],\n    (345, 2, 10): [U_MON(\"ماتادور\")],\n}\n\ndef insert_after(d, key_after, newkey, value):\n    \"\"\"Return an OrderedDict-like dict with newkey inserted right after key_after (or at end).\"\"\"\n    out = {}\n    done = False\n    for k, v in d.items():\n        if k == newkey:\n            continue\n        out[k] = v\n        if k == key_after:\n            out[newkey] = value; done = True\n    if not done:\n        out[newkey] = value\n    return out\n\ndef apply(page, table):\n    path = VER % page\n    v = json.load(open(path, encoding=\"utf-8\"), object_pairs_hook=collections.OrderedDict)\n    seen = set()\n    new_entries = []\n    for e in v[\"entries\"]:\n        ei = e[\"entry\"]\n        assert (ei, \"root\") in table, (page, ei)\n        e2 = insert_after(e, \"sources\", \"ref_check\", table[(ei, \"root\")]); seen.add((ei, \"root\"))\n        nodes = []\n        for n in e2[\"nodes\"]:\n            key = (ei, n[\"id\"])\n            assert key in table, (page, key)\n            n2 = dict(n)\n            for u in WEB.get((page, ei, n[\"id\"]), []):\n                if u not in n2[\"sources\"]:\n                    n2[\"sources\"] = list(n2[\"sources\"]) + [u]\n            n2 = insert_after(n2, \"sources\", \"ref_check\", table[key]); seen.add(key)\n            nodes.append(n2)\n        e2[\"nodes\"] = nodes\n        new_entries.append(e2)\n    missing = set(table) - seen\n    assert not missing, (page, missing)\n    v[\"entries\"] = new_entries\n    json.dump(v, open(path, \"w\", encoding=\"utf-8\"), ensure_ascii=False, indent=2)\n    open(path, \"a\", encoding=\"utf-8\").write(\"\\n\")\n    cnt = collections.Counter()\n    for e in v[\"entries\"]:\n        for r in e[\"ref_check\"]: cnt[r[\"status\"]] += 1\n        for n in e[\"nodes\"]:\n            for r in n[\"ref_check\"]: cnt[r[\"status\"]] += 1\n    print(page, dict(cnt))\n\napply(101, P101); apply(126, P126); apply(311, P311); apply(345, P345)\n"
}
```


### [2026-09-04T15:23:38.770Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/apply_refchecks.py (file state is current in your context — no need to Read it back)
```


## [2026-09-04T15:23:56.528Z] AGENT (thinking)

I still need to verify the KLN leaf numbers for the `deliver` and `Latvia` entries, confirm all added URLs are in the web archive index, and check the existing files' formatting style—these are all independent checks I'll run next.


## [2026-09-04T15:24:00.799Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nimport re\nleaf=0; \nfor i,l in enumerate(lines,1):\n    if i in (10738,21237): print('line',i,'leaf',leaf, l[:80])\n    leaf+=l.count('\\f')\nEOF\npython3 - <<'EOF'\nimport json,urllib.parse\nidx=[json.loads(l) for l in open('data/verification/sources/web/index.jsonl',encoding='utf-8')]\nurls={d['url'] for d in idx}\nneed=[\"https://ahdictionary.com/word/search.html?q=\"+w for w in \"cherub griffin emerald paradise matte checkmate margarite matador mat smaragdite\".split()]\nneed+=[\"https://vajehyab.com/?q=%s&d=moein\"%w for w in \"کروبی زمرد پالیز روضه رونق روستا حور موت مات ماتادور\".split()]\nneed+=[\"https://ahdictionary.com/word/semitic.html\"]\nfor u in need: print('OK ' if u in urls else 'MISSING ', u)\nEOF\nhead -c 300 data/verification/page-101.json | cat -A | head -8; tail -c 50 data/verification/page-101.json | cat -A",
 "description": "KLN leaves for deliver/Latvia; verify archived URLs; check JSON formatting style"
}
```


### [2026-09-04T15:24:04.007Z] TOOL RESULT

```
line 10738 leaf 231 deliver,  tr.  v.  —  OF.  delivrer  (F.  delivrer ),  ‘to  set free’,  fr.  VL.
line 21237 leaf 467 Latvia,  n.  —  Lit.  ‘the  country  of  the  Letts’.  See Lett  and  cp.  lat.
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'data/verification/sources/web/index.jsonl'
head: cannot open 'data/verification/page-101.json' for reading: No such file or directory
tail: cannot open 'data/verification/page-101.json' for reading: No such file or directory
```


## [2026-09-04T15:24:11.844Z] AGENT (thinking)

I'll rerun the archive-index and JSON formatting checks using absolute paths since the working directory changed, and separately fix the deliver/Latvia leaf numbers (231 and 467) in the script.


## [2026-09-04T15:24:11.862Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nidx=[json.loads(l) for l in open('/home/sfmqrb/git/rishe/data/verification/sources/web/index.jsonl',encoding='utf-8')]\nurls={d['url'] for d in idx}\nneed=[\"https://ahdictionary.com/word/search.html?q=\"+w for w in \"cherub griffin emerald paradise matte checkmate margarite matador mat smaragdite\".split()]\nneed+=[\"https://vajehyab.com/?q=%s&d=moein\"%w for w in \"کروبی زمرد پالیز روضه رونق روستا حور موت مات ماتادور\".split()]\nneed+=[\"https://ahdictionary.com/word/semitic.html\"]\nfor u in need: print('OK ' if u in urls else 'MISSING ', u)\nEOF\nhead -c 200 /home/sfmqrb/git/rishe/data/verification/page-101.json | cat -A | head -6; echo; tail -c 30 /home/sfmqrb/git/rishe/data/verification/page-101.json | cat -A",
 "description": "Verify archived URLs and JSON formatting style"
}
```


## [2026-09-04T15:24:13.221Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc && sed -i 's/Klein (KLN_1966.txt leaf 285, s.v. deliver)/Klein (KLN_1966.txt leaf 231, s.v. deliver)/; s/Klein s.v. Latvia (leaf ~445)/Klein s.v. Latvia (leaf 467)/' apply_refchecks.py && grep -n 'leaf 231\\|leaf 467' apply_refchecks.py | cut -c1-120",
 "description": "Fix KLN leaf numbers for deliver and Latvia in the script"
}
```


### [2026-09-04T15:24:13.589Z] TOOL RESULT

```
OK  https://ahdictionary.com/word/search.html?q=cherub
OK  https://ahdictionary.com/word/search.html?q=griffin
OK  https://ahdictionary.com/word/search.html?q=emerald
OK  https://ahdictionary.com/word/search.html?q=paradise
OK  https://ahdictionary.com/word/search.html?q=matte
OK  https://ahdictionary.com/word/search.html?q=checkmate
OK  https://ahdictionary.com/word/search.html?q=margarite
OK  https://ahdictionary.com/word/search.html?q=matador
OK  https://ahdictionary.com/word/search.html?q=mat
OK  https://ahdictionary.com/word/search.html?q=smaragdite
OK  https://vajehyab.com/?q=کروبی&d=moein
OK  https://vajehyab.com/?q=زمرد&d=moein
OK  https://vajehyab.com/?q=پالیز&d=moein
OK  https://vajehyab.com/?q=روضه&d=moein
OK  https://vajehyab.com/?q=رونق&d=moein
OK  https://vajehyab.com/?q=روستا&d=moein
OK  https://vajehyab.com/?q=حور&d=moein
OK  https://vajehyab.com/?q=موت&d=moein
OK  https://vajehyab.com/?q=مات&d=moein
OK  https://vajehyab.com/?q=ماتادور&d=moein
OK  https://ahdictionary.com/word/semitic.html
{$
  "pdf_page": 101,$
  "book_page": 71,$
  "verified_by": "claude-fable-5-1",$
  "verified_on": "2026-09-04",$
  "entries": [$

        }$
      ]$
    }$
  ]$
}$
```


### [2026-09-04T15:24:15.190Z] TOOL RESULT

```
366:    (0, 20): [NONE("Klein (KLN_1966.txt leaf 231, s.v. deliver): 'OF. delivrer ... fr. VL. dēlīberāre, fr. de- an
```


## [2026-09-04T15:24:17.969Z] AGENT

Everything is ready. The remaining steps are sequential: run the script, then run the checker and validate the JSON.


## [2026-09-04T15:24:21.455Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/apply_refchecks.py && for n in 101 126 311 345; do python3 -m json.tool data/verification/page-$n.json > /dev/null && echo \"page-$n valid\"; done && python3 tools/verify_check.py 101 126 311 345; git -C /home/sfmqrb/git/rishe diff --stat",
 "description": "Apply ref checks, validate JSON, run verify_check"
}
```


### [2026-09-04T15:24:24.244Z] TOOL RESULT

```
101 {'supports': 22, 'not_checked': 3, 'partial': 6}
126 {'supports': 12, 'not_checked': 6, 'partial': 6, 'not_found': 1}
311 {'supports': 10, 'partial': 9, 'not_checked': 11, 'contradicts': 1, 'not_found': 1}
345 {'not_checked': 12, 'supports': 17, 'partial': 1, 'contradicts': 2, 'not_found': 1}
page-101 valid
page-126 valid
page-311 valid
page-345 valid
nodes verified: 77/77
node verdicts: {'confirmed': 45, 'plausible': 17, 'transcription_suspect': 3, 'disputed': 12}
root verdicts: {'confirmed': 6}
ref checks: {'supports': 53, 'not_checked': 28, 'partial': 21, 'not_found': 3, 'contradicts': 3}
 data/verification/page-101.json           | 225 +++++++++++++++++++++++++++++-
 data/verification/page-126.json           | 168 +++++++++++++++++++++-
 data/verification/page-311.json           | 217 +++++++++++++++++++++++++++-
 data/verification/page-345.json           | 224 ++++++++++++++++++++++++++++-
 data/verification/sources/web/index.jsonl |   1 +
 5 files changed, 815 insertions(+), 20 deletions(-)
```


## [2026-09-04T15:24:31.926Z] AGENT (thinking)

Let me verify that the only changes in the four files are the added ref_check arrays and appended archived URLs, since the diff shows 20 deleted lines that should just be re-emitted closing brackets.


## [2026-09-04T15:24:34.293Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,subprocess\nfor n in (101,126,311,345):\n    old=json.loads(subprocess.check_output(['git','show',f'HEAD:data/verification/page-{n}.json']))\n    new=json.load(open(f'data/verification/page-{n}.json'))\n    added_urls=0\n    for e in new['entries']:\n        e.pop('ref_check')\n        for nd in e['nodes']:\n            nd.pop('ref_check')\n    # strip appended web urls (only those not in old)\n    for eo,en in zip(old['entries'],new['entries']):\n        for no,nn in zip(eo['nodes'],en['nodes']):\n            extra=[u for u in nn['sources'] if u not in no['sources']]\n            added_urls+=len(extra)\n            nn['sources']=[u for u in nn['sources'] if u in no['sources']]\n    print(n,'identical apart from ref_check/urls:',old==new,'| urls appended:',added_urls)\nEOF\ngit diff data/verification/page-101.json | grep '^-' | grep -v '^---' | head -8",
 "description": "Confirm only ref_check and archived URLs were added"
}
```


### [2026-09-04T15:24:35.941Z] TOOL RESULT

```
101 identical apart from ref_check/urls: True | urls appended: 8
126 identical apart from ref_check/urls: True | urls appended: 3
311 identical apart from ref_check/urls: True | urls appended: 5
345 identical apart from ref_check/urls: True | urls appended: 7
-            "https://www.etymonline.com/word/cherub"
-            "https://en.wiktionary.org/wiki/%D7%9B%D7%A8%D7%95%D7%91"
-            "https://en.wiktionary.org/wiki/%D9%83%D8%B1%D9%88%D8%A8%D9%8A"
-            "https://en.wiktionary.org/wiki/%CE%B3%CF%81%CF%8D%CF%88"
-            "https://en.wiktionary.org/wiki/%CF%83%CE%BC%CE%AC%CF%81%CE%B1%CE%B3%CE%B4%CE%BF%CF%82"
-            "https://languagehat.com/emerald/"
-            "https://en.wiktionary.org/wiki/smaragdite"
```


## [2026-09-04T15:24:56.474Z] AGENT

Done. The four files now carry a `ref_check` array on every entry (root level) and every node; verdicts, derivations and existing sources are untouched (verified by diffing against HEAD with the new fields stripped — the "deleted" lines in the diff are only re-emitted array brackets where a URL was appended). `verify_check.py 101 126 311 345`: 77/77 nodes, 0 PROBLEM lines, ref checks = supports 53 · partial 21 · not_checked 28 · not_found 3 · contradicts 3.

**Per page**
- **101** (B.r.k, B.r.q): supports 22, partial 6, not_checked 3 (FVA/SOR only). Klein pp. 164/274/514/680, Jeffery p. 75, AHD online (cherub, griffin, emerald) and Mo'in (کروبی, زمرد) all read; Mo'in tags زمرد [معر‑یو.], confirming the Greek→Arabic→Persian route.
- **126** (Dheigh): supports 12, partial 6, not_found 1, not_checked 6. Pokorny 244, Kent 191, Horn 133 (*deghavāra‑), Hübschmann 65 (*daika‑, but "fraglich"), Gharib 151 (δyz' < OP didā), AHD dheigh‑ all read. BQT:918 (دیوار) is `not_found` — the OCR of that Borhan leaf is unreadable.
- **311** (Leudh): supports 10, partial 9, not_found 1, contradicts 1, not_checked 11 (VDQ/MAG/PLA not online). Pokorny 684, Klein 885, Gharib 344, Addi Shir 74, Mo'in's Rostam note (rō + tahm) read. IEC:1103 `not_found` (Mann has rustan under *ordh‑*, not on that page).
- **345** (Murvârît, M.v.t): supports 17, partial 1, not_found 1, contradicts 2, not_checked 12 (FVA/PLA/KGW/BQT vols 4–5). Jeffery 261, AHD margarītēs, Klein 946, Lokotsch 115, Pihan 257, Devic 159, Funk & Wagnalls read. FSD:526 `not_found` (p. 526 is in the C's; probably a misprint for 1526).

**Contradicts**
- p. 311 Leudh, node #4 Arabic rauza — AFM:75 (Addi Shir, leaf 76): "(الروضة) … من ريختن أي صبّ" — derives rawḍa from Persian rīxtan 'pour', not from raz (Nourai cites it only in his NOTE as the dissent).
- p. 345 M.v.t, node #3 Latin mattus — POK:694 (IEW pp. 694–695): "lat. madeō … mattus trunken (*madi‑to‑s)" — Pokorny derives mattus from mad‑ 'wet', not from Arabic māt.
- p. 345 M.v.t, node #5 English mat — AHD:805 (online mat²): "from Old French, defeated, withered, perhaps from Latin mattus, stupefied, possibly from *maditus, past participle of madēre, to be wet" — AHD traces the word to Latin, not Arabic (again acknowledged in Nourai's NOTE).

No verdicts needed changing. 21 web pages were archived via `fetch_source.py` (vajehyab Mo'in ×10, AHD ×11) and added to the relevant nodes' `sources`; every local lookup quotes the phrase plus leaf/page in `note`. Files: `/home/sfmqrb/git/rishe/data/verification/page-{101,126,311,345}.json`; helper script at `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/rc/apply_refchecks.py`.
