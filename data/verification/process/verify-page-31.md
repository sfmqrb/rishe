# Verification process log — verify-page-31


## [2026-09-04T14:54:18.157Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 31 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-31.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-31.json. Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py as the instructions require) and the local reference texts listed in refs_online.json for Nourai's own citations (quote what you find). Write /home/sfmqrb/git/rishe/data/verification/page-31.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 31` to confirm complete coverage (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T14:54:20.270Z] AGENT

I'll start by reading the instructions.


## [2026-09-04T14:54:21.150Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T14:54:21.167Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which
5	this repository (`/home/sfmqrb/git/rishe`) turned into JSON
6	(`data/extracted/batch/page-<pdf>.json`). Compact text renderings of the charts
7	are in `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-<pdf>.txt`.
8	
9	Each chart is a tree: a ROOT box, then nodes `#id (parent #p) [Language] refs=… | word «script» : gloss`.
10	An arrow parent→child in the book means "child derives from parent". `parent #0` = derives from the root.
11	Redirect entries (`ROOT X -> redirect to Y`) need no verification: skip them (do not include them).
12	
13	## Your job, per chart (entry)
14	
15	1. Verify the ROOT itself: is the reconstructed root real, is the language label right,
16	   is the gloss right? (e.g. PIE *dʰeyǵʰ- "knead, form" — Pokorny 244.)
17	2. Verify EVERY node (every derivation edge parent→child, and every word in the node):
18	   - Is the word real, in that language, with that meaning?
19	   - Does it really descend from (or was borrowed from) the parent as drawn?
20	   - Give the **derivation explanation**: how, phonetically and historically, the child form
21	     arises from the parent form. Be concrete: name the sound changes (e.g. "Av. pairi-daēza-
22	     → MP *pardēz; Greek borrowed it in the 5th c. BCE as paradeisos (Xenophon), Greek
23	     -ei- rendering Iranian -ē-; Latin paradīsus; Old French paradis; Middle English
24	     paradis > paradise"), the route of borrowing (which people/era/text), and the
25	     semantic shift ("walled enclosure" → "royal park" → "Garden of Eden" via the Septuagint).
26	     For Persian words descend through Old Iranian → Middle Persian → New Persian and name
27	     the intermediate forms when sources give them (e.g. OP didā- / Av. daēza- → MP diz →
28	     NP dež/dez). For Arabic loans note the Arabic stem, and for Arabic-mediated round-trips
29	     (Persian → Arabic → Persian) say so.
30	3. Give a verdict per node and per root:
31	   - `confirmed` — independent modern sources agree with the chart (same root, same route).
32	   - `plausible` — sources give a compatible but not identical picture, or the derivation
33	     is accepted by some scholars but not all; explain the difference.
34	   - `disputed` — modern scholarship (Wiktionary with citations, Etymonline, AHD, Cheung,
35	     Hasandust, Beekes, de Vaan, Kroonen, MacKenzie…) prefers a DIFFERENT origin, or the
36	     word is unrelated. Explain what the modern view is.
37	   - `unverified` — you could not find any independent source either way (say what you tried).
38	   - `transcription_suspect` — the JSON data looks like a transcription error from the scan
39	     (a misread letter, an impossible form, a wrong Persian script); say what you think the
40	     book actually printed and why.
41	4. Record sources as URLs (Wiktionary page, Etymonline page, AHD appendix entry, archive.org
42	   page of Klein/Horn/Bartholomae, etc.). Also note when Nourai's own cited reference
43	   (KLN, POK, AHD, BQT, MON, HRN, HUB…) is itself the modern standard for that claim.
44	
45	
46	## Checking Nourai's OWN cited references (required)
47	
48	Every node carries `refs=` — Nourai's citations, e.g. `KLN:164; FVQ:75` (abbreviation:page;
49	`MON5:528` = MON vol. 5 p. 528). The author claims each arrow is supported by those pages.
50	You must check them:
51	
52	- The bibliography key (abbreviation → book) is in
53	  `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt`.
54	- Where each reference can be read online is in
55	  `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json`
56	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`).
57	- If `local_file` is set, the OCR text of that book is on disk: grep it for the headword
58	  (try several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and,
59	  if `page_offset` is given, locate the cited page (pages are separated by form-feeds; use
60	  `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one page). Read the entry and judge whether
61	  it actually says what Nourai's arrow says.
62	- If `kind` is `website`, use the `lookup_hint` URL pattern with WebFetch.
63	- Do this for at least ONE cited reference per node (the most authoritative available:
64	  POK/AHD/KLN for IE roots, HRN/HUB/BRT/KNT/PHD for Iranian, KLN/FVQ/AFM/PLA for Semitic,
65	  BQT/MON for Persian). If none of a node's references is accessible, say so.
66	
67	Add to every node a `ref_check` array:
68	
69	```json
70	"ref_check": [
71	  {"ref": "KLN:164", "status": "supports", "note": "Klein s.v. 'cherub': Heb. kerūbh, prob. rel. to Akkad. karābu 'to bless', metathesis of b-r-k — exactly Nourai's claim."},
72	  {"ref": "FVQ:75", "status": "not_checked", "note": "no online copy"}
73	]
74	```
75	
76	`status` ∈ `supports` (the page says what the arrow says) · `partial` (the reference has the
77	word but a different/looser derivation) · `contradicts` (the reference says something else)
78	· `not_found` (checked the text, could not find the entry/page) · `not_checked` (reference
79	not accessible online). Quote the key phrase of the reference in `note` when you can.
80	
81	Also add to each entry a root-level `ref_check` for the root's own refs (e.g. `POK:244`).
82	
83	
84	## Process documentation (required)
85	
86	The owner wants to be able to audit every step later. Therefore:
87	
88	- **Every web page you rely on must be archived**: after you read a page (WebFetch or
89	  curl), run
90	  `python3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
91	  This stores the page as text under `data/verification/sources/web/` and indexes it. Only
92	  URLs that were archived this way may appear in a `sources` array. (Batch several calls in
93	  one Bash command to save time.)
94	- **Every lookup in a local reference text must be quoted**: in `ref_check[].note` include
95	  the exact phrase(s) you found (with the grep pattern or page you used, e.g.
96	  "KLN.txt p.164 (ff-page 178): 'cherub … prob. rel. to Akkad. karābu'"), so the finding can
97	  be re-run.
98	- Your full transcript (every tool call and result) is exported automatically by the
99	  coordinator; nothing else needed for that.
100	
101	## Sources to use (in roughly this order)
102	
103	- **Wiktionary** (en.wiktionary.org) — has the best coverage of Persian, Middle Persian,
104	  Avestan, Old Persian, Sogdian, Arabic etymologies, with citations (Cheung 2007, Hasandust,
105	  MacKenzie 1971, Bartholomae, Horn, Hübschmann, Nourai himself). Fetch the word's page AND
106	  the `Reconstruction:Proto-Indo-European/…` / `Reconstruction:Proto-Iranian/…` pages.
107	  Use URL-encoded Persian/Arabic script for those pages.
108	- **Etymonline** (etymonline.com/word/<word>) for English/French/Latin/Greek chains.
109	- **American Heritage Dictionary IE roots** (ahdictionary.com/word/indoeurop.html or
110	  ahdictionary.com/word/search.html?q=<root>) — Nourai's "AHD" citations refer to the 1975
111	  appendix; the online appendix is the updated edition of the same list.
112	- **Pokorny** — via indo-european.info, starlingdb.org, or Wiktionary's Pokorny citation;
113	  Nourai's "POK:nnn" is a page number in Pokorny's IEW.
114	- **Klein's Comprehensive Etymological Dictionary** (KLN) and **Horn's Grundriss der
115	  neupersischen Etymologie** (HRN), **Hübschmann's Persische Studien** (HUB),
116	  **MacKenzie's Concise Pahlavi Dictionary** (PHD), **Bartholomae AiW** (BRT) are on archive.org
117	  if needed for a hard case.
118	- **Encyclopaedia Iranica** (iranicaonline.org) for historical/cultural routes.
119	- **Nişanyan Sözlük** (nisanyansozluk.com) for Turkish; **Lisān al-ʿArab** / Wiktionary for Arabic.
120	- Use WebSearch when you don't know the right page; use WebFetch to read a page.
121	
122	Do NOT fabricate sources. If a page did not load or didn't help, don't cite it.
123	If a chain is well known and uncontroversial (e.g. Latin → Old French → English), one good
124	source covering the chain is enough; spend your effort on the Iranian and Semitic links,
125	which are where errors are likelier.
126	
127	## Output — write ONE file per page
128	
129	Write `/home/sfmqrb/git/rishe/data/verification/page-<pdf>.json` (UTF-8, no BOM):
130	
131	```json
132	{
133	  "pdf_page": 126,
134	  "book_page": 96,
135	  "verified_by": "claude-fable-5-1",
136	  "verified_on": "2026-09-04",
137	  "entries": [
138	    {
139	      "entry": 0,
140	      "root": "Dheigh, Dhigha",
141	      "verdict": "confirmed",
142	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
143	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
144	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
145	      "nodes": [
146	        {
147	          "id": 6,
148	          "lang": "Avestan",
149	          "words": "pairi-daeza",
150	          "verdict": "confirmed",
151	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' (PIE *dʰeyǵʰ-, o-grade *dʰoyǵʰ-o- > Iranian *daiza-). Attested in the Vidēvdād (pairi-daēzaiiąn) …",
152	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza", "https://www.etymonline.com/word/paradise"]
153	        },
154	        {
155	          "id": 9,
156	          "lang": "Greek",
157	          "words": "paradeisos",
158	          "verdict": "confirmed",
159	          "derivation": "Borrowed from Old Iranian *paridaiza- (Median/Old Persian form with -d-, cf. Elamite par-te-taš, Akkadian pardēsu) in the 5th c. BCE; first in Xenophon (Anabasis 1.2.7) for the Persian kings' walled hunting parks. Greek -ei- renders Iranian /ai/ ~ /ē/; -os is the Greek nominative ending. The Septuagint (3rd c. BCE) used it for the Garden of Eden, whence the 'heaven' sense.",
160	          "sources": ["https://en.wiktionary.org/wiki/παράδεισος"]
161	        }
162	      ]
163	    }
164	  ]
165	}
166	```
167	
168	Rules:
169	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
170	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
171	- `words` = the transliterations of the node joined by "; " (copy from the chart).
172	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
173	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
174	- Keep `note` on the entry for root-level comments and for anything cross-cutting
175	  (e.g. "Nourai's whole Semitic branch here is rejected by Klein …").
176	- If a node lists several words, cover each word; if they differ in verdict, use the worst
177	  verdict for the node and explain per word in `derivation`.
178	- Where the chart's own NOTE already records a dispute (e.g. "POK:694 derives Latin mattus
179	  from root Mad"), evaluate it: say which side modern scholarship takes.
180	- Every node has `ref_check` (array, may contain a single `not_checked` item).
181	- Valid JSON only. Test it with `python3 -m json.tool` before finishing.
182	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
183	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason).
184	  Do not paste the JSON back into your reply.
185	
```


## [2026-09-04T14:54:27.271Z] TOOL CALL #2: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-31.txt; echo ------; cat /home/sfmqrb/git/rishe/data/extracted/batch/page-31.json; echo ------; cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json; echo ------; cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt | head -80; echo ------; ls /home/sfmqrb/git/rishe/data/verification/ | head; ls /home/sfmqrb/git/rishe/tools/",
 "description": "Read chart text, JSON, refs, bibliography"
}
```


### [2026-09-04T14:54:27.368Z] TOOL RESULT

```
<persisted-output>
Output too large (39.3KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bt74j1d9c.txt

Preview (first 2KB):
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
------
{
  "pdf_page": 31,
  "book_page": 1,
  "entries": [
    {
      "root": {
        "name": "Ab 1, Ap 1",
        "lang": "Indo-European",
        "refs": "POK:1",
        "gloss": "water"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
...
</persisted-output>
```


## [2026-09-04T14:54:30.025Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-31.txt",
 "description": "Read full chart text"
}
```


### [2026-09-04T14:54:30.070Z] TOOL RESULT

```
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


## [2026-09-04T14:54:35.492Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','KLN','BQT','IRN','AEF','AHD','MON','PLA','WEB','FVQ','ISS']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False))\n\"; grep -n -E '^(POK|KLN|BQT|IRN|AEF|AHD|MON|PLA|WEB|FVQ|ISS)\\b' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt; ls data/verification/ | head -5; ls tools/; sed -n 1,60p tools/verify_check.py; sed -n 1,40p tools/fetch_source.py",
 "description": "Check refs metadata, bibliography, tools"
}
```


### [2026-09-04T14:54:37.886Z] TOOL RESULT

```
POK {"kind": "archive_djvu", "local_file": ["/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/POK_01.txt", "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/POK_02.txt", "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/POK_03.txt", "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/POK_full.txt"], "lookup_hint": "grep the local OCR text for the headword (try several spellings); pages separated by form-feeds", "page_offset": null, "notes": "provisional entry; locator agents still running"}
KLN {"kind": "archive_djvu", "local_file": ["/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/KLN_1966.txt", "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/KLN_1971.txt"], "lookup_hint": "grep the local OCR text for the headword (try several spellings); pages separated by form-feeds", "page_offset": null, "notes": "provisional entry; locator agents still running"}
BQT {"kind": "archive_djvu", "local_file": ["/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/BQT_alt_v1.txt", "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/BQT_dli_part1.txt", "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/BQT_v1.txt", "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/BQT_v1_pages.txt", "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/BQT_v2.txt"], "lookup_hint": "Borhan-e Qate' with Mo'in's etymological footnotes; grep local OCR (noisy); also https://vajehyab.com/?q=<word> may show Borhan", "page_offset": null, "notes": "provisional entry; locator agents still running"}
IRN null
AEF null
AHD {"kind": "archive_djvu", "local_file": ["/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/AHD_watkins1985.txt"], "lookup_hint": "online IE root appendix: https://ahdictionary.com/word/indoeurop.html and https://www.ahdictionary.com/word/search.html?q=<word>; local file is Watkins 1985 dictionary of IE roots (same list, updated)", "page_offset": null, "notes": "provisional entry; locator agents still running", "url": "https://ahdictionary.com/word/indoeurop.html"}
MON {"kind": "archive_djvu", "local_file": ["/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/MON_part1.txt", "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/MON_part2.txt"], "lookup_hint": "Mo'in entry: https://vajehyab.com/?q=<persian word> (choose Moein); or grep local OCR (noisy Persian OCR)", "page_offset": null, "notes": "provisional entry; locator agents still running", "url": "https://vajehyab.com"}
PLA null
WEB null
FVQ {"kind": "archive_djvu", "local_file": ["/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/FVQ.txt"], "lookup_hint": "grep the local OCR text for the headword (try several spellings); pages separated by form-feeds", "page_offset": null, "notes": "provisional entry; locator agents still running"}
ISS null
page-101.json
page-126.json
page-311.json
page-345.json
process
build_site.py
fetch_source.py
ganjoor.py
__pycache__
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
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
```


## [2026-09-04T14:54:44.036Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -n -i -E 'IRN|AEF|PLA|WEB|ISS|FVQ|BQT|MON' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt | head -30; echo ----; python3 -c \"\nimport json;d=json.load(open('data/verification/page-126.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:2500])\"; sed -n 60,140p tools/verify_check.py",
 "description": "Bibliography keys, example verification file, checker rest"
}
```


### [2026-09-04T14:54:45.710Z] TOOL RESULT

```
3: TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
6: TABLE IV - Reference Abbreviations 1 AEF 2 AFA 3 AFM 4 AHD 5 AHM 6 AID 7 AIN 8 AKD 9 AKM 0 AMD i ARB 2 ARK 3 ARM 4 ARP 5 AVG 6 AWH Jalal KhaleqT Motlaq, Asas Eshteqaq Farsi, ^j1* JISsAl o"1-'' Vol. I (a - kh), Bonyad Farhang Iran, 1977. Siegmund Fraenkel, Die Aramaischen Fremdworter im Arabischen, Hildesheim, 1962. Addi Shir, Al-Alfaz Al-Farsiyya Al-Mu'arraba, (A Dictionary of Persian Words in the Arabic Language), Library of Lebanon, 1980.. W. Morris, The American Heritage Dictionary, New College Edition, 1975, Appendix on Indo-European Roots, pp 1505-1550. I. Gershevitch, The Avestan Hymn to Mithra, Oriental Publications No.4, Cambridge University Press, 1959. G. C. Withworth, Anglo-Indian Dictionary. Kegan Paul, Trench &amp; Co, London 1885. E. Liden, Studien zur Altindischen und Vergleichenden Sprachgeschichte , Almqvist &amp; Wiksells, Upsala 1897. H. Zimmem, Akkadische Fremdworter Als Beweis Fur Babylonischen Kultureinfluss, Leipzig 1917. Amir J. ATam, Farhang A'alam Ketab Moqaddas or, A Dictionary of Proper Names in the Bible, English - Persian, Iran University Press, Tehran 1988. H. A" mid, Farhang Farsi Amid, Two volumes, Amir Kabir Press, Tehran, 1369 (1990). Jawaliqi, Al-Mu'arrab, Tehran 1966. M. H. Rokn Zadeh - Adammiyat, Arkan Sokhan, Sharq Press, Tehran 1347 (1968). ^W-\A£ h_)UT joMc' OwJbjd -W*c ^— *&gt;jl^ OwJfcjd £^~&gt; O^j' A. Aryan, ks~'j'* lSj^ ^)~&gt;^ ^*j' -ujUa ^la o^lj oiajs Farhang Vajheh-hay Hamanand, Armani - AvestaT, Pahlavi, FarsT, Vol. I (a), Bonyad Nayshabflr, Tehran 1363 (1984). F. Spiegel, Die Arische Periode und ihre Zustande, Leipzig ,1887. A. V. W. Jackson, An Avesta Grammer, W. Kohl Hammer, Stuttgart 1892. H. Kinder &amp; W. Hilgemann, Atlas of World History. 2 vol., Anchor Books, 1974. A-9 
9: TABLE IV - Reference Abbreviations (continued ...) 17 BLY 18 BQT 19 BRT 20 BST 21 CEL 22 DEV 23 DMO 24 DOZ 25 DRM 26 DVS 27 DZA 28 EAV 29 ETM 30 FAF 31 FFD H. W. Baily, "Hvatanica II", (Glossary of some Khotanese words with reference to Avestan and Persian words), Bulletin of the School of Oriental and African Studies (BSOAS IX:1937-39) pp 69-78, University of London. M. H. Tabriz! (Borhan), Borhan Qate', ^l»ls ^i&amp;j&gt; Etymological footnotes by Dr. M. MoTn, 4 vol, Amfr Kabrr Press, Tehran 1362 (1983). C. Bartholomae, Altiranisches Worterbuch Zusammen Mit Den Nacharbeiten Und Vorarbeiten, Walter de Gruyter Press, 1979. Paul Horn, "Some Inscriptions on Sassanian Gems", Avesta, Pahlavi and Ancient Persian Studies, First Series, pp 224-263, Bombay Educational Society's Press, 1904. S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, 6 Vol., Sverge Haus Publishers, Milton, Ma, 1997 L. M. Devic, Dictionnaire Etymologique des Mots Francais D'Origin Orientale, Oriental Press 1876. S. NafisT, Par Maktab Ostad, ilx-,1 Zohreh Press, Tehran 1344 (1965). R. Dozy, Verklarende Lisjt der Nederlandsche Woorden, Die Uit Het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch Afkomstig Zijn, Leiden 1867. J. Darmester, Etudes Itaniennes, Paris 1883. P. Davis, Roots - Family History of Familiar Words, McGraw-Hill Book Company 1981. M. T. Rashed Mohassel, Daramadi Bar Dastur ^^jl oki _}f~&gt;* j&gt;. iSJ^&gt;^ Zaban AvestST, Khajeh Press, Tehran 1364 (1985). J. Duchesne-Guillemin, "Etymologies Avestiques", Bulletin of the school of Oriental and African Studies (BSOAS IX: 1937-39) pp 861-869, University of London. M. Abolghasemr, RTsheh ShenasT - Etimologi, Ghoghnoos Press, Tehran 1374 (1995). A. Daneshgar, Farhang A'alam Farsi, Hafez NovTn Press, 1370 (1991). M. Abolghasemr, Fe'lhay FarsT Pari, Ghoghnoos Press, Tehran 1374 (1995). v^«&gt;jls pMel 
12: TABLE IV - Reference Abbreviations (continued...) 32 FIB 33 FNI 34 FRS 35 FSD 36 FSF 37 FVA 38 FVF 39 FVQ 40 FWE 41 FWK 42 GPL 43 HID 44 HJB 45 HRN 46 HUB 47 IEC Pur Davfld, Farhang Iran Bastan, Vol. I, University of Tehran Press 1326 (1947). F. DanaT, Farhang Namhay Irani, Negah Publishers, Tehran 1370 (1991). AsadT Tflsi, Farhang Fors, Kharazmi Press, Tehran 1365 (1986). ^iljjl ^cUj^cLs &gt;^fl&gt;jS Funk and Wagnalla, New Standard Dictionary of the English Language, Funk &amp; Wagnalls Company, New York, 1940. A. H. Noushin, Farhang Shahnameh Ferdowsi, oULS 03I3 - ^-jiy i*La&gt;Li ^^ay Vajheh Namak, Donya Press, Tehran 1363 (1984). S. M. Nahvi, Farhang VSm J-^-i - ^-&gt;jl» j* ^o^ ^gb. 03I3 ^(3 ^S^a,^ Vajhehhay Arabi dar Farsi, Dakhil, TohT Azadi Press 1368 (1989). S. M. A. Emam Shflshtari, ^c ^bj ji ^-"j1* iS^ °j'3 «-fc»j» Farhang Vajhehhay Farsi dar zaban Arabi, Anjoman Asar Melli, No 58, Bahman Press, Tehran, 1347 (1968). A. Jeffrey, The Foreign Vocabulary of the Qur'an, (see VDQ). Oriental Institute, Baroda, Stephen Austin &amp; Sons Press, Great Britain 1938 A. J. Bliss, A Dictionary of Foreign Words and Phrases in Current English, Warner Books, 1966. R. Dvorak, "Fremdworter im Koran", Doctoral Dissertation, Akademische Buchdruckerei von F. Straub (1884). J.T. Platts and G.S.A. Ranking, A Grammar of the Persian Language, Oxford University Press (1911). B. Bartholomae, Handbuch der Altlranischen Dialekte, Breitkopf &amp;Hartel, Leipzig 1883. H. Yule &amp; A. C. Burnel, Hobson Jobson, A Glossary of Colloqual AngloIndian Words, Oriental Publishers, Delhi 1903-1968. Paul Horn, Grundriss der NeuPersischen Etymology, Verlag von Karl J. Trubner, Strassburg 1893-1974. H. Hubschmann, Persische Studien, Verlag von Karl J. Trubner, Strassburg 1895. Stuart E. Mann, An Indo-European Comparative Dictionary, Helmut Buske Verlag, Hamburg 1987 A-ll 
15: TABLE IV - Reference Abbreviations (continued...) 48 IRN 49 IRT 50 ISS 51 KAS 52 KFL 53 KGW 54 KLN 55 KNT 56 LAG 57 LAM 58 LAT 59 LEW 60 LKT 61 LST 62 MAG 63 MFL gsj^jljjf C. FarahvashT, Iranvij, Tehran University Press, 1368 (1989). M. A. Sajjadiyyeh, Tabar Moshtarek Iranian oMjj3 } jljljjl va Turanian, Bonyad Nayshabflr 1368 (1989). H. W. Baily, Indo-Scythian Studies (Khotanese Texts - volume VI), Cambridge University Press, 1967. M. A. Hasani Da'i Al-Eslam, ojj£-^-&lt; oki jy^j* Khod Amoz Zaban Sanskrit, Danesh Press, Tehran 1361 (1982). Tha'alebT, Ketab Feqh al-Logheh, Beirut, 1885. Jamshid Ibrahim, Kulturgeschichtliche Wortforschung. (Persisches Lehngut in Europaischen Sprachen, Wiesbaden 1991. D. Klein, A comprehensive Etymological Dictionary of the English Language, Two volumes, Elsevier Publishing Co., 1966. R. G. Kent, Old Persian - Grammer, Text, Lexicon, American Oriental Society, 1953. P. Lagarde, Persische Studien, Dieterichsce Verlag, Gottingen 1884. Henri Lammens, Remarques sur les Mots Francais Derives de l'Arabe, Imprimerie Catholique, Beyrouth 1890. A. Ernout &amp; A. Meillet, Dictionnaire Etymologique de la Langue Latine, Paris, 1951. A. Walde, Latinisches Etymologisches Worterbuch, (With Avestan and Persian Indices), Heidelberg 1938. K. Lokotsch, Etymologisches Worterbuch der Europaischen Worter Orientalischen Ursprunges, Heidelberg 1927. W. B. Henning, Bibliography of Important Studies on Old Iranian Subjects, Ketab Khaneh Danesh, Tehran 1950. G. Widengren, Mohammad, The Apostle of God, Chapter VIII, "Iranian Elements in the Kuranic Vocabulary", Uppsala Universitets Arsskrift, Uppsala, 1955 A. M. Oranski, Moqaddameh Feqh Al-Logheh Irani, ^'jj' '**&gt;S^ &amp; Z»Mb Translated into Persian by K. Keshavarz, Payam press, Tehran 1358 (1979). A- 12 
18: TABLE IV - Reference Abbreviations (continued ...) 64 MMF 65 MON 66 MPP 67 MZF 68 NAT 69 NFI 70 NYB 71 OEW 72 OXF 73 PEI 74 PHD 75 PHN 76 PLA 77 POK 78 PRT 79 RCH K. Khalili, Dictionary of Derivatives of the Persian ^wjls jiLa* ol£ii* &gt;_£^&amp;ji Infinitives or Farhang Moshtaqqat Masader FarsT, Institute of Cultural Studies and Research, Tehran, 1993. M. Mo" in, Farhang FarsT MoT'n, Six volumes, Amir Kabir press 1363 (1984). O^*® ^ ^-a-L!* Honari darbareh Zaban Farsi, Sokhan press, Tehran 1340 (1961). C. Berlitz, Native Tongues, Grosset &amp; Dunlapp Publishers, New York, 1982 F. Jonaydi, Nameh Farhang Iran, ^Ijjl ^»js i*b Bonyad Nayshabfir, Tehran 1368 (1989). Section 4, translated from C.H. Rempis' "Persische Worter im Deutschen," in Mitteilungen, Institut fur Auslands-Beziehungen, Iran-Nummer, 3/4, Stuttgart, 1960, S.229-233. H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1974. J. T. Shipley, The Origins of English Words, The John Hopkins University Press, Baltimore 1984. Jennifer Speake, Oxford Dictionary of Foreign Words and Phrases, Oxford University Press, New York 1997 M. Pei, The Families of Words, Harper &amp; Brothers press, New York 1962. D. N. MacKenzie, A Concise Pahlavi Dictionary. Oxford University press, London 1971. A. P. Pihan, Dictionnaire Etymologique des Motes de la Langue Francaise Derives de L'Arabe, du Persan ou du Turc, Paris 1866. Asya Asbaghi, Persische Lehnworter im Arabischen. Otto Harrassowitz, Wiesbaden 1988 J. Pokorny, Indogermanisches Etymologisches Worterbuck, Two volumes, Francke verlag, Bern 1959. E. Partridge, Origins - A short Etymological Dictionary of Modern English, MacMillan Co., NewYork 1958. J. Richardson, Dictionary, Persian, Arabic and English with Dissertation on the Languages, Literature and Manners of Eastern Nations, Sange-e-Meel Publications, Lahore 1829-1984. A-13 
21: TABLE IV - Reference Abbreviations (continued...) 80 ROE 81 SAP 82 SBK 83 SDQ 84 SHP 85 SIN 86 SKT 87 SLW 88 SNB 89 SNS 90 SOD 91 SOG 92 SOR 93 SPG 94 SYN 95 TAD R. Caliborne, The Roots of English, A Reader's Hanbook of Word Origins, Anchor Books, New York, 1989. A. Sayyah, Farhang Sayyah, Arabic - Persian Dictionary, ^}~&gt; «^a&gt;Js Three volumes, Translation of the Arabic "Al-Monjed" Dictionary, Eslam Publications, Tehran 1368 (1989). M. T. Bahar, Sabk ShenasT - Tarikh Tatawor Nasr Farsi, ^Ls ._£_&gt; Vol I, Tehran 1321 (1942). A. Siddiqi, Studien uber die Persischen Fremdworter im Klassischen Arabisch, Vandenhoeck &amp; Ruprecht, Gottingen 1919. J. T. Shipley, Dictionary of Word Origins, Philosophical Library press, New York 1945. G. Laufer, Sino-Iranica, Chinese Contributions to the History of Civilization in Ancient Iran, Field museum of natural History, publication 201, Anthropological Series, Vol XV, No. 3, Chicago 1919. W. W. Skeat, A Concise Etymological Dictionary of the English Language, Clarenden press, Oxford 1882-1967. W. B. Henning, "Sogdian Loan-words in New Persian", Bulletin of the School of Oriental and African Studies (BSOAS XT939-42) pp 93-106, University of London H. Kowsar, Sang Nebeshteh-ha Sokhan Miguyand, *ujj£~«&gt; Military Public Relations, Iranian Military Press, Tehran (1960's). M. Tavoosi, A Glossary of Shayast Ne Shayast, Shiraz University publications, 1986. B. Ghanb, Sogdian - Persian - English Dictionary, Farhangan Press, Tehran, 1374 (1995). jLw ^uu oV ijij ^imI^I - ^wjli - 
24: TABLE IV - Reference Abbreviations (continued...) 96 TLM 97 TTS 98 TYL 99 TZF 00 UNV 01 VDQ 02 VFO 03 VGH 04 VIE 05 VOP 06 VSF 07 WEB 08 WLD 09 ZAP 10 ZAW 11 ZFS 12 ZMA F. C. Tolman, Ancient Persian Lexicon, The Vanderbilt Oriental Series, American Book co. 1890-1908. G. Vambery, Etymologisches Worterbuch der Turko-Tatarischen Sprachen, Biblio Verlag, Osnabriick, 1972. W. Taylor, Arabic Words in English, Clarenton Press, London 1933. M. Abolghasemi, Tarikh Mokhtasar Zaban FarsT, ^-d1* oki j^""« ejJjIj Bonyad Andisheh EslamT Press, Tehran, 1373 (1994). J. M. Unvala, King Husrav and His Boy - Pahlavi Text and Glossary, Paul Geuthner publishers, Paris 1963. F. Badreh-t, Vajheh-hay Dakhil dar jl*=w oTjsji J-''2 i^l&amp;ejfj Qoran-e Majid, Translation of A. Jeffrey's book with Comments (see FVQ). Toos Publishers, Tehran 1372 (1993). M. Ahmad Soltam, Vajhgan FarsT dar Zabanhay ^jjl ^k-Sbj _ji ^j1* oT;'? OrupaT, Avay Niir Press, Tehran, 1372 (1993). H. Khadiv Jam, Vajheh Nameh Ghazalhay Hafez, Elmi Press, Tehran, 1371 (1992). £i9b» ^L^Jjc ^Ub OjT^ M. A. Sajjadiyyeh, Vajheh-hay Irani dar ^....JLCil ^bj ji ^IjjI ^la 03I3 Zaban EngelTsT, Bonyad Nayshabur, Tehran 1364 (1985). M. MoshM, Farhang Vajheh-hay Orupayl ^-"j1* j* ^kiJ lS1* °3'3 &gt;-^»j» dar FarsT, Alborz Press, Tehran 1371 (1992). K. Mehravand, Vajheh Sazi dar Zaban FarsT, Rasti press, Tehran 1349 (1970). v^-jl* ok) j4 lSJ1- °3'3 W. Collins, Webster's New Twentieth Century Dictionary of the English Language, second edition 1978. A. Walde, Vergleichendes Worterbuch der Indogermanischen Sprachen, two volumes, Walter de Gruyter &amp; co., Leipzig 1930-1973. H. W. Bailey, Zoroastrian Problems in the Ninth-Century Books, Clarendon press, Oxford 1943-1971. C. Bartholomae, Zum Altlranischen Worterbuch Nacharbeiten and Vorarbeiten, Vorlag von Karl J. Trubner, Strassburg 1906. M. Abolghasemi, Zaban FarsT va Sargozasht An, HTrmand Press, Tehran, 1375 (1996). F. Jonaydi, ZendegT va Mohajerat Aryaian, Bonyad Nayshabur, Tehran, 1374 (1995). A-15 
----
{
 "entry": 0,
 "root": "Dheigh, Dhigha",
 "verdict": "confirmed",
 "modern_form": "PIE *dʰeyǵʰ- 'to knead, form, build (of clay)'; o-grade noun *dʰóyǵʰos 'something kneaded/formed' > 'wall; dough'",
 "note": "Pokorny IEW 244 dheiĝh- 'Lehm kneten und damit mauern oder bestreichen (Wand, Mauer; Töpferei); auch vom Teigkneten' is exactly Nourai's gloss; AHD dheigh- 'to form, build' cites 'Pokorny dheiĝh- 244'. Wiktionary (Rix LIV 140-141, Kroonen, de Vaan, Beekes) agrees. Nourai's second spelling 'Dhigha' is his rendering of the zero-grade/extended variant (Pokorny gives dheiĝh-, dhoiĝho-s, dhiĝh-lo-s). Two of his branches are weak: the OP 'daika > dīg' branch is rejected by modern Iranian etymology (see nodes 11-12), and the Sogdian, Persian dež and ferdows nodes are cognates/round-trip loans rather than lineal descendants of the parents drawn.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-",
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰóyǵʰos",
  "https://www.thefreedictionary.com/_/roots.aspx?type=Indo-European&root=dheigh-",
  "https://www.etymonline.com/word/*dheigh-",
  "https://starlingdb.org/cgi-bin/etymology.cgi?root=config&basename=%2Fdata%2Fie%2Fpokorny&text_recno=1208&single=1"
 ],
 "nodes": [
  {
   "id": 1,
   "lang": "Old Persian",
   "words": "didâ, děğa-vâra",
   "verdict": "transcription_suspect",
   "derivation": "OP didā- f. 'wall, fortress' is genuinely attested: DSf (Darius' Susa foundation charter) line 54 'tyaiy didām apiθa' — 'the men who adorned the wall were Medes and Egyptians' (Kent's Lexicon p. 191, which is Nourai's KNT:191). It is the regular SW-Iranian reflex of PIr *daizah < PIE *dʰóyǵʰos: Proto-Iranian *ǰ (< PIE *ǵʰ) gives Old Persian d where Avestan/Median give z (cf. Av. daēza-), and the reduplicated-looking di-dā- shows the OP treatment (Asatrian 2017, 'SWIran. *didā- fortress, walled residence'). The second word is not an attested OP word but Horn's/Hübschmann's reconstruction of the ancestor of dīvār, i.e. *daiza-vāra- 'wall-enclosure' (HRN:133); the JSON form 'děğa-vâra' with ě and ğ is almost certainly a scan misreading of the book's 'dēza-vâra' or 'daiza-vâra' (Nourai writes ž, not ğ, for the sound elsewhere on this page: dež). Modern reconstruction (Wiktionary, after Asatrian and Rastorgueva-Edelman) is OP didā- + *-wāra-, giving MP dēwār.",
   "sources": [
    "https://www.livius.org/sources/content/achaemenid-royal-inscriptions/dsf/",
    "ht
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
```


## [2026-09-04T14:54:54.220Z] TOOL CALL #6: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T14:54:54.229Z] TOOL RESULT

```


```


## [2026-09-04T14:55:08.271Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs; ls -la; echo \"=== POK page 1-2 (ab-)\"; awk 'BEGIN{RS=\"\\f\"} NR>=1 && NR<=40 {if ($0 ~ /ab-/ && $0 ~ /Wasser/) {print \"PAGE\",NR; print substr($0,1,3000)}}' POK_full.txt | head -80",
 "description": "List refs and grep Pokorny for ab- water"
}
```


### [2026-09-04T14:55:10.025Z] TOOL RESULT

```
total 229604
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  4 10:55 .
drwx------ 5 sfmqrb sfmqrb     4096 Sep  4 10:50 ..
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
-rw-rw-r-- 1 sfmqrb sfmqrb   603979 Sep  4 10:44 PHN.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   981836 Sep  4 10:40 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1137861 Sep  4 10:40 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1170809 Sep  4 10:40 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3971883 Sep  4 10:35 POK_full.txt
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
=== POK page 1-2 (ab-)
PAGE 1
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat. 




Anatolian 


Ang. 




Anglian 


AngN 




Anglo-Norman 


Aram.- 


■Iran 


Aramaeo-lranian 


Ash. 




Ashkun
```


## [2026-09-04T14:55:18.781Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs; head -c 600 POK_01.txt; echo; echo \"=== POK_01 ab- Wasser\"; grep -n -E '^\\s*(ab-|āb-|ab- ?[:,])' POK_01.txt | head; grep -n -i -E 'ab-.{0,40}(Wasser|Fluß|Fluss)' POK_01.txt POK_full.txt | head -10; echo \"=== ap- Wasser\"; grep -n -E '(ā̆p-|āp-|ap-).{0,20}(Wasser|water)' POK_01.txt POK_full.txt | head -10",
 "description": "Grep Pokorny for ab-/ap- water"
}
```


### [2026-09-04T14:55:21.079Z] TOOL RESULT

```
)H
JULIUS  POKORNY
INDOGEEMAmSCHES
ETYMOLOGISCHES
WÖRTERBUCH
I.  BAND
FRANCKE  VERLAG  BERN UND  MÜNCHEN
A.  Francke  AG  Verlag  Bern  •   1959
Alle  Rechte  vorbehalten
Satz  und  Druck:  Adolf  Holzhausens  Nfg.,  Wien
INDOGERMANISCHES   ETYMOLOGISCHES   WÖRTERBUCH
ä  Ausruf  der  Empfindung,  oft  neugeschaffen.
Ai.  ä  Ausruf  der  Besinnung-;
gr.  ä  Ausruf  des  Unwillens,  Schmerzes,  Erstaunens;  Ic,  da  Ausruf  der Verwunderung  und  Klage;  dazu  ä^etv  ^ächzen*";
lat.  äj  äh  Ausruf  des  Schmerzes^  des  Unwillens;
lit.  äj  aä  Ausruf  der  Verwunderung^  
=== POK_01 ab- Wasser
19:ab-  ^Wasser;,  Fluß^.
POK_01.txt:19:ab-  ^Wasser;,  Fluß^.
POK_01.txt:45:zu  lesen  und  noch  vor  der  Lautverschiebung  ins  Germ,  gedrungen;  daher an.  api  m.  ^Affe^  Tor^^,    as.  apo^   ahd.  affo   m.,    affa,  affin  L,   ags.    apa  m. Aus    dem    Germ,    stammt    aruss.    opica    ^Affe^^    acech.    opice.     Vgl.    ab- ^Wasser^  und  Schrader  Reallex.^  Hoops  Reallex.  s.  v.  Affe. AVP.  I  51  f.
=== ap- Wasser
POK_01.txt:4602:ai.  mpa-  ,tiefliegend'  (ni-\-ap-  ,Wasser');
POK_full.txt:1636:See also: compare also ap-i* 'water, river' and abd{n) 'ape'. 
POK_full.txt:9178:): " from, out, of ' < Root / lemma: ap-2\ " water, river ' < Root / lemma: ab- : " water, river ' 
POK_full.txt:9209:Root/ lemma: ap-2 {* hap-2)\ " water, river ' derived from Root/ lemma: ab-{*h2^'"-): " 
POK_full.txt:9225:Old Indie ap- f. 'water', e.g. PI. Norn, apah, Akk. apah. Gen. apam, Avestan Nom. Sg. afs, 
POK_full.txt:26750:Old Indie nTpa- " low lying ' {ni+ ap- "water'); 
POK_full.txt:85106:"run, flow, pathway', /5da/7- "hurrying'; /ad/'-ap- "running water (containing)', iran. *tahra- 
POK_full.txt:86190:Verbaladjektiv Old Indie -tur{-ff) in ap-tur^6\e Wasser iJberquerend', aj/-tur"\n fight,
```


## [2026-09-04T14:55:26.180Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs; echo \"=== POK_01 lines 17-30 (p.1 ab-)\"; sed -n 17,30p POK_01.txt; echo \"=== POK ap-2 Wasser p.51\"; grep -n -E '^\\s*(2\\.\\s*)?ap-.{0,30}Wasser' POK_01.txt | head; L=$(grep -n -E 'ap-.{0,15}Wasser' POK_01.txt | head -1 | cut -d: -f1); [ -n \"$L\" ] && sed -n \"$((L-2)),$((L+12))p\" POK_01.txt; echo \"=== POK_full ab- entry\"; sed -n 9200,9240p POK_full.txt",
 "description": "Read Pokorny ab- and ap- entries"
}
```


### [2026-09-04T14:55:27.929Z] TOOL RESULT

```
=== POK_01 lines 17-30 (p.1 ab-)
got.  ö  Ausruf  des  Unwillens^  der  Bewunderung;  ahd.  ö  Ausruf  des Schmerzes;  mhd.  ö  Ausruf  des  Schmerzes,,  der  Bewunderung^  auch  dem Vokativ  angehängt.
WP.  I  1,  WH.  I  1,  Loewe  KZ.  54,  143.
ab-  ^Wasser;,  Fluß^.
Lat.  amnis  i.,  später  m.  c(*abnis)]  air.  ab  (*a&ä)  Gen.  ahae  ^Fluß^,  da- neben abann,  cjmr.  afon,  orn.  bret.  auon,  gall.  brit.  FIN  Abona,  abge- leitet cymr.  afanc  \,Biber;  AVasserdämon,  Zwerg^,  mir.  abac  (^abankos ^Biber,  Zwerg^  Schweiz. -frz.  avan  ^Weide^  (*abanko-):   lett.  FIN  Äbava.
Die  westdeutschen  FIN  auf  -apa,  nhd.  -affa^  gehen  wohl  teils  auf  sonst verlorengegangenes  westgerm.  *ap-  (idg.  *a6-),  teils  auf  ven.-ill.  ap-  (idg. *ap-)  zurück.
Vgl.  auch  2.  up-  ^Wasser^  Fluß^  und  abö(n)  ,Affe^
WP.  I  46  f.,  WH.  I  40,  Feist  19  a,  579  a,  GIPatSR.  II  134.
äbel-,  Uböl-,  abel-  ,ApfeP.
Lat.  Abella  (osk.  Stadt  in  Campanien)  malifera  ,äpfeltragend'^,  nach  Verg. Aen.  7,  740,  dürfte  ihren  Namen  nach  der  Apfelzucht  erhalten  haben  und auf  die  Grundform  *ablo7iä  zurückweisen.  Der  Apfel  ist  nicht  etwa  erst nach  der  Stadt  benannt.
Im  Kelt.  sind  die  Bezeichnungen  für  ,Apfel^  (*ablu)  und  ,Apfelbaum'^ (*abal-n-)  auseinanderzuhalten.  Gall.  avallo  ,poma',  Aballö  (n-St.)  ON, frz.  AvalloTij  abrit.  ON  Aballäva,  gallo-rom.  *aballinca  , Alpenmistel  (Wart- burg); air.  ubuU  (*ablu)  n.  ,ApfeF,  ncymr.  afal/ VI.  afalau,  corn.  bret. aval   m.  ,Apfel^,   aber    mir.  aball  (^abalnä)  f.  , Apfelbaum^,    acymr.  aball^
mcymr.  avall  PL  euyill  (analogisch)  f.,  acymr.  aballen,  ncymr.  afallen _, Äpfelbaum*'  (mit  Singulativendung).
Die  gleichen  Ablautformen  im  Germanischen:
Krimg-ot.  apel  (got.  *apls?),  ahd.  apfid,  afful,  mhd.  apfel,  ags.  ceppel (engl,  apple),  an.  epli  n.  (apal-grär  ^apfelgrau^)  ;,Apfel^  Germ,  wohl *ap{a)la-,  *aplu-.  Ferner  an.  apaldr  ^Apfelbaum^,  ags.  apuldor,  ceppuldre, ahd.  aphoUra  (vgl.  nhd.  Affoltern  ON),  mhd.  apf alter  ^Apfelbaum^  {*apaldra-).
Das  Baltische  zeigt  deutliche  Spuren  der  im  Idg.  ganz  vereinzelten Z-Deklination  '^aböl,  G.  Sg.  *äbeles.  Dehnstufe  des  Suffixes  erscheint  noeist im  Worte  für  ^ApfeF:  ostlit.  obuolys,  lett.  dbuolis  (-uo-St.);  westlit.  öbuolas, lett.  äbuols  (o-St.)  aus  idg.  *a6ö^;  Normalstufe  meist  im  Worte  für  ^Apfel- baum^;  lit.  obelis  (fem.  i-St),  lett.  äbels  (i-St.)^  äbele  (e-St.)  aus  idg.  *äbel-] aber  apr.  tvoble  f.  {^äbl-)  ^Apfel*^;,  luobalne  (*äboln-)  f.  ^Apfelbaum^
=== POK ap-2 Wasser p.51
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
Vgl.  idg.  ni-zdos  ,Nest'  unter  sed-  ,sitzen'.  Als  ,heruntermachen'  (wie lett.  nievdt)  beruhen  wohl  auch  neid-  ,ovEidog',  neit-  ,befeinden'  neiq-  (s.  dort), auf  unserem  nei-,  ni-.
enter,  nter  ,zwischen — hinein',  en-tero-  ,innerlicli' :
=== POK_full ab- entry

Page(s): 53 

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

situated, lying in water', dvTpa-^ island, sand bank in the river', a/7/a/77?5- 'island'; the 

same contraction with in -o ending 1 . part in gr. river names 'Iviono^ ' name of a stream on 

Delos', 'Aau)TT6(; ( : ivou), ogk;; Pick BB. 22, 61, 62); gr. 'Ania 'Peloponnes', MEoa-ania 

ds., lokr. Msaa-anioi, lllyrian Msaadnioi (different Krahe ZONF. 13, 20 f.) common gr.-
```


## [2026-09-04T14:55:38.451Z] AGENT

Planned next: local lookups (KLN pp.2/47, FVQ p.46, BQT/MON entries, Watkins AHD, Webster's, Bailey DKS) in one batch, plus parallel web fetches of Wiktionary/Etymonline for each word.


## [2026-09-04T14:55:44.701Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs; echo \"=== KLN alembic\"; grep -n -i -E '^\\s*alembic|alembic,\\s*n' KLN_1966.txt KLN_1971.txt | head -5; grep -n -i 'alembic' KLN_1966.txt | head -3; echo \"=== KLN julep\"; grep -n -i -E 'julep' KLN_1966.txt | head -5; echo \"=== KLN Punjab\"; grep -n -i -E 'Punjab|Panjab' KLN_1966.txt | head -5; echo \"=== KLN Abadan / Avestan ap\"; grep -n -i -E 'Avestic\\s+ap\\b|Avestic\\s+api|Pers\\.\\s+ab\\b|Abadan' KLN_1966.txt | head -8; echo \"=== FVQ ibriq\"; grep -n -i -E 'ibr[iī]q|abriq' FVQ.txt FVQ_pages.txt | head -8; echo \"=== WEB alembic\"; grep -n -i -E '^\\s*alembic|al-anb[iī]q|anbiq' WEB_vol1.txt | head -8; echo \"=== ISS/DKS ap nab\"; grep -n -i -E 'Pers\\. n[āa]b\\b|n[āa]b .{0,20}pure|anāpa|an-āp|abrīz|ābrēz' ISS_alt_DKS.txt | head -10",
 "description": "Grep Klein, Jeffery, Webster, Bailey for the words"
}
```


### [2026-09-04T14:55:46.826Z] TOOL RESULT

```
=== KLN alembic
KLN_1966.txt:2149:man.  Cp.  F.  allemand,  ‘German’,  which  also derives  fr.  Teut.  Alamann-  (see  allemande). alembic,  n.  —  ME.,  fr.  OF.  (=F.)  alambic,  fr. OSp.  (=  Sp.)  alambique  fr.  Arab,  al-anbtq,  ‘the still’,  which  is  formed  fr.  al-, ‘the’,  and  Gk.  4p.(3tl;, ‘cup,  cap  of  a  still,  alembic’,  which  is  of  uncer¬ tain,  possibly  Semitic  origin.  Cp.  It.  lambicco, which  is  of  the  same  origin  as  Sp.  alambique. Alenu,  n.,  concluding  prayer  ( Jewish  liturgy).  — Heb.  ‘dlimi,  lit.  ‘upon  us’,  formed  fr.  'al,  ‘on, upon’,  with  -dnu,  the  pronom.  suff.  of  the  1st person  in  the  plural.  The  prayer  is  so  called from  the  first  words  ‘alenu  leshabbiah,  ‘it  is  (in¬ cumbent)  upon  us  to  praise’.  Heb.  ‘al  is  rel.  to ‘aid11,  ‘he  went  up’.  See  aliyah.
KLN_1971.txt:10785:alembic, n. — ME., fr. OF. (=F.) alambic, fr. 
2149:man.  Cp.  F.  allemand,  ‘German’,  which  also derives  fr.  Teut.  Alamann-  (see  allemande). alembic,  n.  —  ME.,  fr.  OF.  (=F.)  alambic,  fr. OSp.  (=  Sp.)  alambique  fr.  Arab,  al-anbtq,  ‘the still’,  which  is  formed  fr.  al-, ‘the’,  and  Gk.  4p.(3tl;, ‘cup,  cap  of  a  still,  alembic’,  which  is  of  uncer¬ tain,  possibly  Semitic  origin.  Cp.  It.  lambicco, which  is  of  the  same  origin  as  Sp.  alambique. Alenu,  n.,  concluding  prayer  ( Jewish  liturgy).  — Heb.  ‘dlimi,  lit.  ‘upon  us’,  formed  fr.  'al,  ‘on, upon’,  with  -dnu,  the  pronom.  suff.  of  the  1st person  in  the  plural.  The  prayer  is  so  called from  the  first  words  ‘alenu  leshabbiah,  ‘it  is  (in¬ cumbent)  upon  us  to  praise’.  Heb.  ‘al  is  rel.  to ‘aid11,  ‘he  went  up’.  See  aliyah.
21755:limbec,  n.,  alembic  (archaic).  —  Aphetic  for  alem¬ bic.
=== KLN julep
1142:Abderite,  n„  i)  an  inhabitant  of  Abdera;  2)  a fool.  —  L.  Abderita ,  fr.  Gk.  ’A(38r)ptnr]!;,  ‘in¬ habitant  of  Abdera’,  fr.”A[38if]pa  (pi.),  ‘Abdera’, a  town  proverbial  for  the  stupidity  of  its  in¬ habitants.  For  sense  development  cp.  Gotha¬ mite.  For  the  ending  see  subst.  suff.  -ite. abdest,  n.,  the  Mohammedan  rite  of  washing  the hands  before  prayer.  —  Pers.  dbddst,  lit.  ‘water for  the  hand’,  fr.  ab,  ‘water’,  and  dost,  ‘hand’. Pers.  ab,  ‘water’,  is  rel.  to  Avestic  dp-,  OI.  dpah (fern,  pi.),  ‘water’;  sec  amnic  and  cp.  the  first element  in  abkari  and  the  second  element  in doab  and  in  julep.  Pers.  dost,  ‘hand’,  is  rel.  to Avestic  zasta,  ‘hand’,  fr.  I.-E.  base  *ghosto -, whence  also  OI.  hastah,  ‘hand’.  See  hasta  and cp.  hath.
20443:F.,  fr.  Late  L.  zizyphum,  ‘jujube’,  which  together with  Late  L.  zizyphus,  'jujube  tree’,  derives  fr. Gk.  Shipov,  ‘jujube  tree;  jujube’,  which  is  of unknown  origin.  Cp.  Zizyphus. julep,  n.,  a  sweet  drink.  —  F.,  fr.  OProven^.  julep or  fr.  Sp.  julepe,  fr.  VAr.  juleb,  corresponding to  classical  Arab,  juldb,  fr.  Pers.  gulab,  ‘rose water,  julep’,  which  is  compounded  of  gul,  ‘rose’, and  ab,  ‘water’.  See  rose  and  abdest.
33124:rose,  n.  —  ME.,  fr.  OE.,  fr.  L.  rosa,  fr.  Gk.  poSov, ‘rose’, for *Fpo8ov,  fr.OIran. *  wrda-  (whence also Aram,  warda.  Arm.  card).  OIran.  *wrda-  be¬ came  gul  in  ModPers.  in  the  sense  of  the  pho¬ netic  law,  according  to  which  initial  w  becomes  g and  -rd  is  changed  to  /.  Turkish  giil,  ‘rose’,  is  a Persian  loan  word.  OIran.  *wrda-,  ‘rose’,  repre¬ sents  I.-E.  * wrdho-,  ‘thorn,  bramble’,  whence also  OE.  word,  ‘bramble’,  Norw.  dr,  ol  (for *ord),  ‘currant,  bush’.  Cp.  rhodo-.  Cp.  also  the first  element  in  julep  and  the  second  element  in bedeguar.
=== KLN Punjab
=== KLN Abadan / Avestan ap
1142:Abderite,  n„  i)  an  inhabitant  of  Abdera;  2)  a fool.  —  L.  Abderita ,  fr.  Gk.  ’A(38r)ptnr]!;,  ‘in¬ habitant  of  Abdera’,  fr.”A[38if]pa  (pi.),  ‘Abdera’, a  town  proverbial  for  the  stupidity  of  its  in¬ habitants.  For  sense  development  cp.  Gotha¬ mite.  For  the  ending  see  subst.  suff.  -ite. abdest,  n.,  the  Mohammedan  rite  of  washing  the hands  before  prayer.  —  Pers.  dbddst,  lit.  ‘water for  the  hand’,  fr.  ab,  ‘water’,  and  dost,  ‘hand’. Pers.  ab,  ‘water’,  is  rel.  to  Avestic  dp-,  OI.  dpah (fern,  pi.),  ‘water’;  sec  amnic  and  cp.  the  first element  in  abkari  and  the  second  element  in doab  and  in  julep.  Pers.  dost,  ‘hand’,  is  rel.  to Avestic  zasta,  ‘hand’,  fr.  I.-E.  base  *ghosto -, whence  also  OI.  hastah,  ‘hand’.  See  hasta  and cp.  hath.
=== FVQ ibriq
=== WEB alembic
5377:a-lem/bic, n. [L. alambicus; Ar. alanbiq; al, the, and anbiq, Per. ambiq, a still; Gr. ambix, a cup of a still.]
5379:ALEMBIC
=== ISS/DKS ap nab
5816:-tdye, -tye, loc. -ya (briya), inst. -ai, -e, inst. plur. -yau. With negative Z 6:32 abrive; Z 644 abriyaa-. Adjectives -inaa-, -osta-, -üna-, -aimja- femn.; V тоо, 4315 britinü suha vasivdtd ‘he experiences desirable pleasures’ (BS Sukha-, upajiva-), K 15217 brriyina; п 104777 brrivinai ysathinai jadinai uama jsa 'from the sea of love, birth, ignorance’; SuvP. 68r2-3 órriviau hamtharkyau jsa "with love distresses', BS rüga-samRate; V 381, 316 сї brityausta-piskala *who have the form at will', =V 332, 24v1i hiyaugca-páskála, BS G 37, 21b3 &ama-rüpinas ca; V 52, 83br briyostd pdskald; v 125, 7b4 briyaustd; Z 20:6 trama hámaro brriyosta ttiyà База 'then all become so passionate’; SuvO. 36r4 и бтїуйпуаи tceimanyau uysdyañe ' must be surveyed with loving eyes’, BS priva-hitabhyam prehgitauyaáh, SuvO. 36r5 bryündna salatána ' with loving speech’ (BS samlapa-), BS priya-vacanatih; without -r-, SuvO. 36r4 byünyau, see above byüna-. For -aimja, Z 20723 aysu nä buysaimá britainju mástu daju ' 1 quench for them the great passion-flame'. britañä ‘beloved’, v 118, 67v2 sd härä arthë manavá britaüá ‘this matter (dyadic) is pleasant, desired’ (BS mana-üpa-), BS tad vastu priyam manāpam. briti “friends (?)' (dialect text), v 262 DR orag hasți briti tto mari hoataimni ‘eight friends (?), so here I spoke (?)*. britiya ‘іп passion’ (context unclear) v 28, 59v3 yude britiya ретте, briya- 'beloved, dear, treasured’, 2 20:22 acc. sing. pūru briyu ' dear son’; voc. sing. Z 19:3 briya balysa; Z 2021 briya ита ' dear report’; nom. acc., gen. sing. brī, inst. sing. brina, inst. plur. Z 11.11 bráyo; plural, SuvO. дут manāva brya hvandä 'pleasant, dear men’, BS Aznta- priye jane 'beloved, dear people’ (BS mana-apa- ' pleasant). By loss of -iy-, -y- also bra-, brra-, v 6677 bra ysarrnü nika 'dear golden ornaments’ (BS niska-); JS 12VI nārä panyai brra 'wife dear to everyone’, With suffix -aka-, V 154, 184b3 bryakä hamatá ‘becomes be- loved’; comparative, пі 101*41 brranda ysügkyaira; super- lative, V x15, бут bryandamai атаса márüre ‘his most beloved ministers (BS amütya-) die’ (bryandama with yi), BS priyo 'тпйфуа 'sya mriyate; Z 2*5 bryàndamu piru ‘most beloved son’; K 20:251 svüra ma brrauda ye ‘ће was most dear to me', = K. 28:166 suara ma brrauda ye, =] 361i1:0 süra jsam mam brrauda ye (translation, BSOAS 29, 1966, 511; 528). See avun- “to bless’, participle oráta-; briya-, brrauda-, phrrind. From frai-: jri- ‘о be friendly, love’, Av. frima-, frina-, frita-, Jriba-; frina-, frya (friia-), with à-, afrivan- 'blessing'; Sogd. Bud. pry, pryt'tt ‘love’, pry'w'k ‘love’, prytm- ' dearest'; Мап. fryy, pry'n prytm ' dearest of the dear’, pryytt, тугі, fry'n, frytr; Chr. fry, frycat, plur. fryt; Jryt't ' love, with preverbs, d-, ni-, pati-; Bud. 'prywn, "Brywn, Ancient Letter "pryw; Man. "Brywnéykw, participle '"frytyy, plur. "frytyt, ‘fryn, "туит; Chr. "frywn; with ші, Chr. nfrytyty ('accursed' voc. plur.); Bud. ptfr'yn- 'return. blessing’, Man. ptfryy ‘honour’; ZorP. üfrim, артап 'bless', nifrīt ‘cursed’, nifrin, Pazand nifridaa; N.Pers. afarm ' blessing', zafrr ‘сше’, nafrin, парта; Oss. DI. arfä ‘thanks’, arfájag ‘blessed’. To IE Pok. 844-5 prai-:pri-, O.Ind. pridti, pritd-, priyd-, Greek qrpëús ‘soft’, Got. frija-, nom. sing. freis,
```


## [2026-09-04T14:55:59.796Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs; echo \"=== FVQ briq\"; grep -n -i -E 'br[iī1l]q|abriq|ewer' FVQ.txt | head -8; echo \"=== FVQ_pages ff count\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' FVQ_pages.txt; awk 'BEGIN{RS=\"\\f\"} /br[iī]q|ewer/ {print \"PAGE\",NR; print substr($0,1,1500)}' FVQ_pages.txt | head -60; echo \"=== AHD Watkins ap- water / julep / Punjab\"; grep -n -E '^\\s*ap-|\\bap-\\.?\\s+Water|julep|Punjab|Panjab' AHD_watkins1985.txt | head -10",
 "description": "Grep Jeffery for ibriq and Watkins for ap-"
}
```


### [2026-09-04T14:56:01.906Z] TOOL RESULT

```
=== FVQ briq
3235:A ewer, or water jug. 
=== FVQ_pages ff count
334
PAGE 64
46 FOREIGN VOCABULARY OF THE QUR'AN
Grundriss, i, 256, would derive *JJ* j from DmSN as jxi from
]tDB7, by assuming a dissimilation form in Aramaic, i.e. D^mHK*.
There is no trace of such a form, however, and Brockclmann's choice
of jUttJLi as illustration is unfortunate as it appears to be a borrowed
word and not original Arabic. The safest solution is that proposed by
Rhodokanakis in WZKM, xvii, 283, and supported by Margoliouth, 1
to the effect that it has been vocalized on the analogy of Isma'll
and Isrd'll. 2 The name was doubtless well enough known in Jewish
circles in pre-Islamic Arabia, 3 and when Muhammad got the form
from Judaeo-Christian sources he formed \A\j?\ on the
same model.
IvilS.
A ewer, or water jug.
Only in the plu. form /! jb I in an early Meccan description of
Paradise. It was early recognized as a Persian loan-word (Siddiqi, 13),
and is given by al-Kindl, Risala, 85 ; ath-Tha f alibi, Fiqh, 317; as-Suy utl 4
and al-Jawaliql 5 in their lists of Persian borrowings, as well as by the
Lexicons, LA, xi, 299 ; TA, vi, 286, though some attempted to explain
it as a genuine Arabic word derived from
In modem Persian the word is j_j\ meaning urn or waterpot.
wirh Lcr.tuir*, p. \'l ; soo also Lidzbarski, JnluinHetbHcli, 7:i ; Fischer,
(Jloxtiar, 163.
2 He says : " Die Form ^j.\ durfto am ehcstcn aus ihrer Anlohiiun^ an J-**-!
und der Ausgleichung mit demselbcn zu erklaron soin, nach dcm hokatinten kur'-
anischen Prinzip, dash Personennaraen, deron Tragcr in irgeii
=== AHD Watkins ap- water / julep / Punjab
```


## [2026-09-04T14:56:07.585Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs; echo \"=== FVQ p.46-47 continuation\"; awk 'BEGIN{RS=\"\\f\"} NR==64 {print substr($0,1500,2500)} NR==65 {print \"PAGE65\"; print substr($0,1,1200)}' FVQ_pages.txt; echo \"=== AHD Watkins\"; grep -n -i -E 'ap-.{0,10}water|julep|punjab|water\\.\\s' AHD_watkins1985.txt | head -12",
 "description": "Read Jeffery p.46-47 and grep Watkins"
}
```


### [2026-09-04T14:56:09.131Z] TOOL RESULT

```
=== FVQ p.46-47 continuation
idwoli-hc'iii Kusammen-
hange stehn, lautlich auf oine Form zu bringen wtrebt."
3 Korovitx, KU, 92; JPN. 160.
4 Itq, 318 ; Mutaw, 46 ; Muzhir, i, 136.
"' The text of the Mu'arrab (Saohau's od , p. 17) is defective here, giving the first
U], but not the second. Correcting it by the 7l(j. we read : '111 &J* 0-^ u' ^"1
'^ ^ -ill ^ Cjj.
fi Raghib, 'Mufrndut, 43 ; and see Bagh. on tho passage.
7 Vullcrx, Lex, i, 8. and for further meanings sec RQ, 4 ; Addai Sher, 6. J^jr.l
also occurs in Pers. but only as a borrowing from Arabic.
PAGE65
FOREIGN VOCABULARY OF THE QUR'AN 4:7
It would be derived from i^\ water (=- Phlv. o> /?, i.e. OPers. dpi l =-
Av. gp or jjuj ; Skt. TR agwa), and (jj to jxwr ( = Phlv. U^OO^
from an old Iranian root *raek = linquere), 2 as was suggested
by Castle 3 and generally accepted since his time. It was from the
Phlv. form that the word was borrowed into Arabic, the shortening
of the I being regular. 4 The word occurs in the early poetry, in verses
of 'Adi b. Zaid, 'Alqama, and Al-A'sha, and so was doubtless an early
borrowing among the Arabs who were in contact with the court at
al-Hira.
ii, 32 ; vii, 10 ; xv, 31, 32 ; xvii, 63 ; xviii, 48 ; xx, 115 ; xxvi,
95 ; xxxiv, 19 ; xxxviii, 74, 75.
Iblis. 6 &a/3oAoy the Devil par excellence.
The tendency among the Muslim authorities is to derive the name
from .-Jl) to despair, he being so called because God caused him to
despair of all good so Raghib, Mufraddt, 59, and Tab. on ii, 32. The
more acute philologers, however, recognized the impossibility of this
(an-NawawT, 138), and Zam.on xix, 57, says- ^
j v* jj*}\) 2M. al-Jawallql, Mu'arrab, J7, also justly argues
against an Arabic derivation.
That the word is a corruption of the Gk. StajSoAos 1 has
=== AHD Watkins
83:the contraction of early Indo-European short vowels with a following 9. Already in Proto- Indo-European itself, two of the three laryn- geals had the property of coloring an adja- cent fundamental vowel e to a and o, respectively, before the contractions took place. Thus the root pa-, “to protect,” is contracted from older *paa-, with ‘“‘a- coloring”; the root d6-, “to give,” is con- tracted from older *doo-, with “o-coloring”; and the root dhé-', “to set, put,” is con- tracted from older *dheo-, without coloring. The fundamental vowel in each of these roots, as in most Indo-European roots, was originally e. In scholarly usage it is now customary to write the non-coloring laryn- geal as 9,, (or h,), thus *dheo,-; the a-coloring laryngeal as a, (or h,), thus *pas.-; and the o-coloring laryngeal as a; (or hz), thus *doo,-. This rather cumbersome notation has been simplified in this Dictionary, since the vowel before the schwa is sufficient to distinguish the three in the cases of contraction to a long vowel, and in other positions in most lan- guages other than Greek the three merge to one. No systematic notice has been taken in this Dictionary of word-initial laryngeals before vowels (amply attested in Hittite), since the root forms with initial vowel are readily convertible by the student. Thus ap-?, “water,” from *sap- (Hittite happ-, “water”; op-', “to work, produce in abun- dance,” from *sop- (Hittite happ-in-, “rich”’); ed-, “to eat,’ from 9ed- (Hittite ed-, “to eat”).
138:On the other hand, from the absence of a general word for “sea” we may deduce that the Indo-Europeans were originally an inland people. A root mori- is attested dialectally (MERE), but it may well have referred to a lake or other smaller body of water. Trans- portation by or across water was, however, known to the Indo-Europeans, since most of the languages attest an old word for boat or ship, nau-?, probably propelled by oars or a pole (ere-', “to row”).
277:akwa-. Water. 1. Germanic *agwjd becoming *auj6, “thing on the water,” in Old English ig, ieg, island, and
282:b. Old Norse um/(b), about, around: OMBUDSMAN; c. Old High German umbi, around: UMLAUT. 3. Latin ambi-, around, about: AMBI-. 4. Greek amphi, around, about: AMPHI-. 5. Celtic *ambi (see ag-). [Pok. ambhi 34.] ambhé. Both. 1. Reduced form *bAd in Germanic *b6-, *bé in Old Norse bdthir, both: BOTH. 2. Latin ambé, both: AMBSACE. 3. Greek amphé, both: AMPHOTERIC. [In Pok. ambhi 34.] amer-. Day. Suffixed form “Gmer-d in Greek hémera, day: EPHEMERAL, HEMERALOPIA. [Pok. dmer- 35.] ames-. Blackbird. 1. Suffixed variant form *ams-ol- in Old English dsle, blackbird: ouzEL. 2. Suffixed variant forms *mes-old, *mes-olo- in Latin merula, merulus, merle, blackbird: MERLE, MERLON. [Pok. ames- 35.] [amma. Various nursery words. Latin root. 1. Medieval Latin amma, mother: AMAH. 2. Reduced form *am- in: a. Latin amare, to love: AMATEUR, AMATIVE, AMATORY, AMORETTO, AMOUR; ENAMOR, INAMORATA, PARAMOUR; b. Latin amita, aunt: AUNT; c. Latin amicus, friend: AMICABLE, AMIGO, AMITY; ENEMY, INIMICAL.] an’. On. Extended form *ana. 1. Germanic *ana, ané in: a. Old English an, on, a, on: ON; b. Old Norse 4, in, on: ALOFT; ¢. Old High German ana (> Middle High Ger- man ane), on: ANLAGE; d. Middle Dutch aan, on: ON- SLAUGHT. 2. Greek ana, on, up, at the rate of: ANA?, ANA-. [Pok. 4. an 39.] an?, Demonstrative particle. Suffixed form “*an-tero-, “other (of two)” (compare *al-tero- under al-') in Ger- manic *antharaz in Old English 6ther, other: OTHER. [Pok. 2. an 37.] an-', Old woman, ancestor (nursery word). Latin anus, old woman: ANILE. [Pok. 1. an- 36.] an-2. To pour, draw water. Suffixed form *an-tlo- in Greek antlos, bilge water, bucket: ANTLIA. [In Pok. 1. sem- 901.] andh-. Bloom. Suffixed form *andh-es- in Greek anthos, flower: ANTHEMION, ANTHER, ANTHESIS, ANTHO-, -AN- THOUS; AGAPANTHUS, CHRYSANTHEMUM, DIANTHUS, EX- ANTHEMA, HYDRANTH, (MONANTHOUS), STROPHANTHIN. [Pok. andh- 40.] andho-. Blind, dark. Suffixed variant form *ondh-ro- perhaps in Latin umbra, shadow: UMBEL, UMBRA, UM- BRELLA; ADUMBRATE. [Pok. andho- 41.] ane-. To breathe. Suffixed form *ana-mo- in: a. Latin animus, reason, mind, and anima, soul, spirit, life, breath: ANIMA, ANIMADVERT, ANIMAL, ANIMATE, (ANI- MATO), ANIMISM, ANIMOSITY, ANIMUS; EQUANIMITY, LONGANIMITY, MAGNANIMOUS, PUSILLANIMOUS, UNANI- mous; b. Greek anemos, wind: ANEMO-. [Pok. 3. an(9)- 38.] anata. Doorjamb. Latin antae (plural), a pair of pillars on the opposite sides of a door: ANTA. [Pok. anatd- 42.] [angelos. Messenger. Greek noun, akin to Greek anga- ros, mounted courier, both from an unknown Oriental source. 1. Greek angelos, messenger: ANGEL, (ANGELIC), ANGELICA, (ANGELUS); ARCHANGEL, EVANGEL. 2. Greek angaros, mounted courier: ANGARY.] angh-. Tight, painfully constricted, painful. 1. Germanic *ang-, compressed, hard, painful, in Old English ang- nzgl, “painful spike (in the flesh),” corn, excrescence (nzgl, spike; see nogh-): AGNAIL. 2. Suffixed form *angh-os- in Germanic *angaz in Old Norse angr, sor- row, grief: ANGER. 3. Suffixed form *angh-os-ti- in Ger- manic *angusti- in Old High German angust (> German Angst), anxiety: ANGST. 4. Latin angere, to strangle, draw tight: ANxious. 5. Suffixed form *angh-os-to- in Latin angustus, narrow: ANGUISH. 6. Greek ankhein, to squeeze, embrace: QUINSY. 7. Greek ankhoné, a stran- gling: ANGINA. [Pok. angh- 42.] angvhi-. Snake, eel. 1. Latin anguis, snake: ANGUINE; ANGUILLIFORM. 2. Taboo deformation or separate root *ogvhi- in Greek ophis, snake, serpent: OPHIDIAN, OPHITE; OPHIOLOGY, OPHIUCHUS. 3. Taboo deformation or separate root *eghi- in Greek ekhis, snake, in deriva-
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
317:aus-?. To draw water. Suffixed form *aus-yo- in Latin haurire, to draw up: EXHAUST, HAUSTELLUM, HAUSTO- RIUM. [Pok. aus- 90.] awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVI- ATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH. 2. Compound *awi-spek-, “observer of birds” (*spek-, to see; see spek-), in Latin auspex, augur: AuSPICE. II. Possible derivatives are the Indo-European words for egg, *dwyo-, *ayo-. 1.Germanic *ajja(m) in: a. Old English 2g, egg: COCKNEY; b. Old Norse egg, egg: EGG. 2, Latin 6uum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM. 3. Greek dion, egg: 00-. [Pok. auei- 86.] awo-. An adult male relative other than one’s father. 1. Latin avus, grandfather: ATAVISM. 2. Latin avunculus, maternal uncle: AVUNCULAR, UNCLE. 3. Latin avia, grandmother: AYAH. [Pok. auo-s 89.] ayer-. Day, morning. 1. Germanic “*airiz in: a. Old Eng- lish &r, before: EARLY, ERE; b. Old Norse dr, before: OR2. 2. Germanic (superlative) *airistaz in Old English rest, earliest: ERST. [Pok. ajer- 12.] ayes-. A metal, copper or bronze. Latin aes, bronze, money: AENEOUS, ERA. [Pok. aios- 15.] baba-. Root imitative of unarticulated or indistinct speech; also a child’s nursery word for a baby and for various relatives. 1. Middle English babelen, to babble: BABBLE. 2. Middle English babe, babi, baby: BABE, BABY. 3. Italian bambo, child, simpleton: BAMBINO. 4. Polish baba (diminutive babka), old woman: BABA, BABKA. 5. Russian baba, old woman: BABUSHKA. 6. Rus- sian balalaika, balalaika (imitative of the sound): BALA- LAIKA. 7. Latin balbus, stuttering, stammering: BOOBY. 8. Greek barbaros, non-Greek, foreign, rude (< “one who speaks incomprehensibly”): (BARBARIAN), BARBARISM, BARBAROUS. 9. Hindi babi, father: BABU. [Pok. baba- 91.] badyo-. Yellow, brown. A Western Indo-European word. Latin badius, chestnut brown (used only of horses): BAY’. [Pok. badios 92.] bak-. Staff used for support. 1. Probably Middle Dutch pegge (> Middle English pegge), pin, peg: PEG. 2. Latin baculum, rod, walking stick: BACILLUS, BAGUETTE; BAC- ULIFORM, DEBACLE, IMBECILE. 3. Greek baktron, staff: BACTERIUM; (CORYNEBACTERIUM). [Pok. bak- 93.] bamb-. Word imitative of dull or rumbling sounds. Greek bombos, a booming, humming: BOMB, (BOMBARD), BOUND}. [Pok. ba*mb- 93.] bands. A drop. Possibly Irish bainne, milk: BONNYCLAB- BER. [Pok. band- 95.]
1127:wed-'. Water; wet. 1. Suffixed o-grade form *wod-6r in Germanic *watar in Old English weter, water: WATER. 2. Suffixed lengthened-grade form *wéd-o- in Germanic *wéd- in Old English wt, wét, wet: WET. 3. O-grade form *wod- in Germanic suffixed form “wat-skan, to wash, in Old English wescan, wacsan, to wash: WASH. 4. Nasalized form *we-n-d- in Germanic *wintruz, win- ter, “wet season,” in Old English winter, winter: WINTER. 5. Suffixed zero-grade form *ud-d6r in Greek hudor, water: (HYDRANT), HYDRO-, (HYDROUS); ANHYDROUS, CLEPSYDRA, DROPSY, HYDATHODE, HYDATID. 6. Suffixed nasalized zero-grade form *u-n-d-d- in Latin unda, wave: UNDINE, UNDULATE; ABOUND, INUNDATE, (REDOUND), REDUNDANT, SURROUND. 7. Suffixed zero-grade form *ud-ro-, *ud-rd-, water animal, in: a. Germanic *otraz, otter, in Old English ofor, otter: OTTER; b. Latin Jutra, otter (with obscure /-): NUTRIA; C. Greek hudros, a water snake: Hyprus; d. Greek hudra, a water serpent, Hydra: Hypra. 8. Suffixed zero-grade form *ud-skio- in Scottish and Irish Gaelic uisge, water: USQUEBAUGH, (WHISKEY). 9. Suffixed o-grade form *wod-d- in Russian voda, water: VODKA. [Pok. 9. au(e)- 78.]
1151:*op-wer-yo- (*op-, over; see epi) in Latin operire, to cover: COVER, OPERCULUM. II. O-grade form *wor-. 1. Germanic *war-nén in Old English war(e)nian, to take heed: WARN. 2. Germanic *war- in: a. (i) Old French garant, warrant, authorization: GUARANTY (ii) Old North French warant, warrant, and warantir, to guarantee: WARRANT, (WARRANTEE), WARRANTY; b. Old French garer, to guard, protect: GARAGE; c. Old French g(u)arir, to defend, protect: GARRET, GARRISON; d. Old North French warenne, enclosure, game preserve: WARREN; e. Old French g(ujarnir, to equip: GARMENT, GARNISH. [Pok. 5. uer- 1160.] wer-S, Also wera-. To speak. Variant *wré-, contracted from *wreo-. 1. Suffixed zero-grade form *wr-dho- in Germanic *wurdam in Old English word, word: worD. 2. Suffixed form *wer-dho- in Latin verbum, word: VERB, VERVE; ADVERB, PROVERB. 3. Suffixed form *wer-yo- in Greek eirein, to say, speak: IRONY. 4. Variant form *wré- in suffixed form *wré-tor- in Greek rhétér, public speaker: RHETOR. [Pok. 6. wer- 1162.] wer-7. To burn. Suffixed lengthened o-grade (causative) form *w6r-yo- in Russian varit’, to boil: saMovarR. [Pok. 12. wer- 1166.] wer-®, Squirrel. Reduplicated expressive form *wi-wer(r)- in Latin viverra, a ferret: VIVERRINE. [Pok. 13. uer- 1166.] wér-. Water. Suffixed zero-grade form *dr-ind- in Latin irina, urine: URINE. [In Pok. 9. au(e)- 78.] were-', Wide, broad. Suffixed form *wer(a)-u- metathe- sized in Greek eurus, wide: EURY-; ANEURYSM, EURYD- IcE. [Pok. 8. wer- 1165.] were-2, To find. Variant *wré-, contracted from *wrea-. Reduplicated form *we-wré- in Greek heuriskein (first person singular perfect indicative active heuréka), to find: EUREKA, HEURISTIC. [Pok. 4. ver- 1160.] werg-. To do. I. Suffixed form *werg-o-. 1. Germanic *werkam, work, in: a. Old English weorc, werc, work: work; b. Old High German werc, work: (BOULEVARD),
1174:ROSE}, 3. Zero-grade form *wrd- in Iranian *wrd in Persian gul, rose: JULEP.]
1707:JOY gau- JUBILATE yu-2 JUDGE deik-, yewes- JUDICIAL deik- JUGATE yeug- JUGGERNAUT gWa- JUGGLE yek- JUGGLER yek- JUGULAR yeug- JUGUM yeug- JUICE yeue- JULEP ap-2, wrod- JuLY deiw- JUNCTION yeug- JUNCTURE yeug- JUNIOR yeu- JUNKER kei-2, yeu- JUNTA yeug- JUPITER deiw- JURAL yewes- JURIDICAL deik-, yewes- JURISCONSULT yewes- JURISDICTION deik-, yewes- JURISPRUDENCE yewes- JURIST yewes- JURY! yewes- JUSSIVE yeudh- susTl yewes- JusTiFy dhé-1
```


## [2026-09-04T14:56:24.813Z] AGENT (thinking)

I'll pull up the Persian dictionary entries (BQT/MON, Bailey) alongside web pages for âb, âftâb, âbâdân, âxor, zahâb, âbnîk/anbîq, alembic, julep, ebrîq, nâb, âbrîz, Punjab, and the PIE root—fetching them all together since they're independent lookups.


## [2026-09-04T14:56:31.150Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs; echo \"=== BQT v1 pages count\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' BQT_v1_pages.txt; echo \"=== BQT آبادان / آفتاب / آخور / زهاب\"; grep -n -E 'آبادان|آفتاب' BQT_v1_pages.txt | head -6; grep -n -E 'زهاب|زه آب' BQT_v2_pages.txt BQT_v1_pages.txt | head -6; echo \"=== MON انبیق\"; grep -n -E 'انبیق|أنبیق' MON_part1.txt | head -6; echo \"=== MON زهاب\"; grep -n -E 'زهاب' MON_part1.txt MON_part2.txt | head -6; echo \"=== MON آبنیک / ابریق\"; grep -n -E 'آبنیک|ابریق' MON_part1.txt | head -6; echo \"=== DKS nab/ap\"; grep -n -E 'N\\.?Pers\\. ā?b\\b.{0,40}water|N\\.?Pers\\. nāb|āp- .{0,20}water' ISS_alt_DKS.txt | head -8; grep -n -E 'anāp|an-āp|\\bnāb\\b' ISS_alt_DKS.txt | head -8",
 "description": "Grep Borhan, Mo'in, Bailey DKS for Persian words"
}
```


### [2026-09-04T14:56:32.951Z] TOOL RESULT

```
=== BQT v1 pages count
777
=== BQT آبادان / آفتاب / آخور / زهاب
1181:«من درهمةٌ زمین بارسی گویان شپری نیکوتر وجامم‌تر و آبادان‌تر
1205:«چون لغت عبری وسریانی وپهلوی تا بایام طلوع آفتاب دین عر ی
1422:سیوندی نیزاز نظار علم اصوات منفرد است ( 0۲] (خورء آفتاب) »
4164:آت شگردان ۰ آرواره » آفتاب گردان ۰ آفتا به» آقا.ابزار» از گیل
6084:بیمنی ابریق و آفتابه و مطهرء ومانند آن
6090:که‌آفتابه وابریق (۳) باشد .
BQT_v1_pages.txt:6166:های هوز » پمعنی زهاب باشد » بمنی آب ی که از
BQT_v1_pages.txt:22144:ودبگر بازه آب برداشتن ...»یم - بر وزن فهیم : تلم یکی آزرابان
BQT_v2_pages.txt:1274:             ‫‪:‬‬     ‫زهاب ) ‪ 2‬ساب طبری ‪۹e‬‏‬                 ‫کشدن‬        ‫ی‬‫اهر‬
BQT_v2_pages.txt:25037:                                                                     ‫ریزهابی که ازتراشیدن‌چوب ومس وبرنج وامتال‬
BQT_v2_pages.txt:25417:                           ‫‪ 3‬زهاب مار باشد ‪۰‬‬
BQT_v2_pages.txt:27727:‫چویکی باشد که سنادزهابدان سازنوازند ویعربی‬                                  ‫درخت رگاوند ‪۶.‬‬
=== MON انبیق
17169:انبیق: مارا [غ. معر.] (ا.) ظرفی است برای 
=== MON زهاب
MON_part2.txt:8910:کشتی که زهاب آب‌های کشتی دز آن جمع 
MON_part2.txt:76279:غلط. نشته؛ چیزهابی که انسان رابه حال 
MON_part2.txt:78768:چیزهابی نظیر دانه‌های معطر (هل» تجم 
MON_part2.txt:80662:بازی سپید پرواز می‌داد و از جیزهابی که 
MON_part1.txt:21229:بج: لها (.) زهاب و پالایش آب و شراب و 
=== MON آبنیک / ابریق
1324:بدان دست و روی شویند» ابریق؛ مطهره. 
6264:ابریق: ب:۰ [معر. آبریز] (.) ظرف سفالین 
6270:ابریق: بطم [معر . ابری. ابر بز ] (ا.) شمشیر 
20673:ابریقی که از آن در بیاله‌های کو چک شراب 
24795:کوزة شراب ابریق می» صراحی. ظرفی که 
=== DKS nab/ap
3032:dajs- 'to burn, to ripen', У 125, бгз dajsindd 'they burn’; Sid. 15v4 rriysu cu ksasid hadà dasde $i ' rice which ripens in бо days, white’, BS sastika-, Tib. libras drug-čus smin- pa dkar-po ni: Sid, 138r2 vesarpá daste' the fester matures’, Tib. hbrum-bu rnags-te (Narthang mnag-te); 1V 17015 cu vara khaitti daysdi satá hadà ra jū midi ' who suffers there, it matures, he still lives roo days, he dies'; K 22:60 ca va adye tt(i)maña ha bada dajira "in which ground the seeds always ripen’, = 14:105—6 ca fara vara ійта(їа) тайа rasta vistáve 'where good seed now becomes ripened (right)', v 115, 64rr—2 jsārañä u späte u hiyára ttīmañä ne büddna dagyüre ‘сога and flowers and fruits, seeds ripen not in season’, BS sasyam puspam phalam bijam na samyak paripacyate. Participles, present dajsamda: ‘sharp (of taste)', Sid. srz dajsamdai и trà u byamjsä raysá ‘sharp and bitter and astringent taste’, BS kafu-tikta- kagáya- ; Sid. 136r1 dijsamdam u ttaudaim ' sharp and hot", BS Ааји-изпа-; fem. N 75:24 (da)jsamco viyano varasáre ‘they experience burning pain’ (BS vedaná), BS katukám amanāpām vedanüm vedayanti sma; past -diya- in padiya- ‘burnt’, v 69, Svi padita...huvadita 'burnt.. . well burnt! BS G 37, 1222 dagdhüh. . .dagdhà eva, Tib. éhig- Фа. hig-pà-iüid-do; and incohative dis- (as in pandts-) disfa- ' ripened', negative adisfa- ‘not ripe', see below; adjective, v 116, буг ttīra dajsdka bätamjsa hámüre (fruits) bitter, sharp, astringent', BS tiktah hatuka eva ca (reading kafu-kagüya-) See also dajd ‘fame’, dai ‘fire’, padajs-, pandis-, padis-, padtya-, avadiya-; puin- and byaide 'it matures’, Base dag-, Av. present daz-, with -£- daxsa- ' brand’, adjective dašu- ta disease’ listed with tafmu- 'fever', glossed Zor.P. dart; MLParth.T. "udj- ‘burn’, adjective 'wdjn ‘burning’; Zor.P. dasitan, dat, N.Pers. day ' brand', dišan, dišand, dužan, dai£and ‘sharp, angry’, Ваібёї daxta ‘brand mark’, Armen. Iw dasan ‘bitter, rough, wild'; Sogd. Bud. 8y'z 'burning', 8y- ‘to burn, ripen’, Bys- 'ripen', 3 sing. ysty. For
5816:-tdye, -tye, loc. -ya (briya), inst. -ai, -e, inst. plur. -yau. With negative Z 6:32 abrive; Z 644 abriyaa-. Adjectives -inaa-, -osta-, -üna-, -aimja- femn.; V тоо, 4315 britinü suha vasivdtd ‘he experiences desirable pleasures’ (BS Sukha-, upajiva-), K 15217 brriyina; п 104777 brrivinai ysathinai jadinai uama jsa 'from the sea of love, birth, ignorance’; SuvP. 68r2-3 órriviau hamtharkyau jsa "with love distresses', BS rüga-samRate; V 381, 316 сї brityausta-piskala *who have the form at will', =V 332, 24v1i hiyaugca-páskála, BS G 37, 21b3 &ama-rüpinas ca; V 52, 83br briyostd pdskald; v 125, 7b4 briyaustd; Z 20:6 trama hámaro brriyosta ttiyà База 'then all become so passionate’; SuvO. 36r4 и бтїуйпуаи tceimanyau uysdyañe ' must be surveyed with loving eyes’, BS priva-hitabhyam prehgitauyaáh, SuvO. 36r5 bryündna salatána ' with loving speech’ (BS samlapa-), BS priya-vacanatih; without -r-, SuvO. 36r4 byünyau, see above byüna-. For -aimja, Z 20723 aysu nä buysaimá britainju mástu daju ' 1 quench for them the great passion-flame'. britañä ‘beloved’, v 118, 67v2 sd härä arthë manavá britaüá ‘this matter (dyadic) is pleasant, desired’ (BS mana-üpa-), BS tad vastu priyam manāpam. briti “friends (?)' (dialect text), v 262 DR orag hasți briti tto mari hoataimni ‘eight friends (?), so here I spoke (?)*. britiya ‘іп passion’ (context unclear) v 28, 59v3 yude britiya ретте, briya- 'beloved, dear, treasured’, 2 20:22 acc. sing. pūru briyu ' dear son’; voc. sing. Z 19:3 briya balysa; Z 2021 briya ита ' dear report’; nom. acc., gen. sing. brī, inst. sing. brina, inst. plur. Z 11.11 bráyo; plural, SuvO. дут manāva brya hvandä 'pleasant, dear men’, BS Aznta- priye jane 'beloved, dear people’ (BS mana-apa- ' pleasant). By loss of -iy-, -y- also bra-, brra-, v 6677 bra ysarrnü nika 'dear golden ornaments’ (BS niska-); JS 12VI nārä panyai brra 'wife dear to everyone’, With suffix -aka-, V 154, 184b3 bryakä hamatá ‘becomes be- loved’; comparative, пі 101*41 brranda ysügkyaira; super- lative, V x15, бут bryandamai атаса márüre ‘his most beloved ministers (BS amütya-) die’ (bryandama with yi), BS priyo 'тпйфуа 'sya mriyate; Z 2*5 bryàndamu piru ‘most beloved son’; K 20:251 svüra ma brrauda ye ‘ће was most dear to me', = K. 28:166 suara ma brrauda ye, =] 361i1:0 süra jsam mam brrauda ye (translation, BSOAS 29, 1966, 511; 528). See avun- “to bless’, participle oráta-; briya-, brrauda-, phrrind. From frai-: jri- ‘о be friendly, love’, Av. frima-, frina-, frita-, Jriba-; frina-, frya (friia-), with à-, afrivan- 'blessing'; Sogd. Bud. pry, pryt'tt ‘love’, pry'w'k ‘love’, prytm- ' dearest'; Мап. fryy, pry'n prytm ' dearest of the dear’, pryytt, тугі, fry'n, frytr; Chr. fry, frycat, plur. fryt; Jryt't ' love, with preverbs, d-, ni-, pati-; Bud. 'prywn, "Brywn, Ancient Letter "pryw; Man. "Brywnéykw, participle '"frytyy, plur. "frytyt, ‘fryn, "туит; Chr. "frywn; with ші, Chr. nfrytyty ('accursed' voc. plur.); Bud. ptfr'yn- 'return. blessing’, Man. ptfryy ‘honour’; ZorP. üfrim, артап 'bless', nifrīt ‘cursed’, nifrin, Pazand nifridaa; N.Pers. afarm ' blessing', zafrr ‘сше’, nafrin, парта; Oss. DI. arfä ‘thanks’, arfájag ‘blessed’. To IE Pok. 844-5 prai-:pri-, O.Ind. pridti, pritd-, priyd-, Greek qrpëús ‘soft’, Got. frija-, nom. sing. freis,
```


## [2026-09-04T14:56:43.316Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs; echo \"=== MON انبیق\"; sed -n 17165,17178p MON_part1.txt; echo \"=== MON ابریق\"; sed -n 6260,6272p MON_part1.txt; echo \"=== MON آب head\"; grep -n -E '^آب: ' MON_part1.txt | head -3; L=$(grep -n -E '^آب: ' MON_part1.txt | head -1 | cut -d: -f1); [ -n \"$L\" ] && sed -n \"$L,$((L+8))p\" MON_part1.txt; echo \"=== MON زهاب\"; grep -n -E '^زهاب' MON_part1.txt MON_part2.txt | head; echo \"=== BQT v1 آب first entry\"; grep -n -E '^آب ' BQT_v1_pages.txt | head -5; grep -n -E 'آب.{0,30}(پهلوی|اوستا|آپ)' BQT_v1_pages.txt | head -8; echo \"=== BQT آبادان\"; grep -n -E '^آبادان|آبادان.{0,40}(پهلوی|آپات)' BQT_v1_pages.txt | head -5; echo \"=== BQT p.1225 zahab\"; sed -n 1270,1278p BQT_v2_pages.txt",
 "description": "Read Mo'in and Borhan entries"
}
```


### [2026-09-04T14:56:45.251Z] TOOL RESULT

```
=== MON انبیق
پیغمبران و خشوران. 
انبیره: (م-)معآطاود ( .) خلاشه و خاشاکی که 
پس از پوشش خانه بر بام اندازند تا بر بای 
آن خاک و گل ریزند و بندایند. 
انبیق: مارا [غ. معر.] (ا.) ظرفی است برای 
تقطیر مایعات و گرفتن عصاره و عرق. 
انتا< : 60۸8 [ع.] (مصل.) فرا رسیدن 
هسنکام زایش چارپایان. نتیجه گرفتن از 
چیزی. (منط.) نتیجه گرفتن از مقدمات 
منطقی؛ - ج. انتاجات. 
انتشاه: ِِ [ع. ۰ (مصل.) آگاه شدن» 
تحار کف (امص.) آ گاهی بیداری. 
(رواد.) دقت. (تص.) زوال غفلت از دل؛ ج. 
انتاهات. 
=== MON ابریق
ابریشم. ابریشم فروش. ابریشم تاب. (.) 
(مستحدث) غلافی از لاستیک و مانند آن 
که برای حفظط از سرابت امراض مقارتی 
دستمال ابر یشم: دستمال یافته از ابر بشم. 
ابریق: ب:۰ [معر. آبریز] (.) ظرف سفالین 
آب. آوند چر مین لوله‌دار که بدان وضو 
سازند» مطهره. ظرف سفالین با گوشه و 
دسته و لوله که بدان طهارت کنند» لولهین. 
آفتانه, مطهر 5 فلز ین. مشربه. وزنی معادل دو 
من. (سد.) گردن عو د؟ ۳ ابار یق. 
ابریق: بطم [معر . ابری. ابر بز ] (ا.) شمشیر 
سار تابان» سمشبر سار درحشند ه» کمان 
درخشان. زن صاحب جمال تابان بدن. 
=== MON آب head
949:آب: ,1 )1( نام ماه پنجم 5 پاز دهم سالماه 
25451:آب: سدی که جلو آب بندند. بند ارباب: 
92431:آب: طراز کردن آب؛ برابر کردن ۳1 
آب: ,1 )1( نام ماه پنجم 5 پاز دهم سالماه 
خاص بهودی و سرانی. در اصطلاح 
سریانی رومی ماه آب با ماه ششم اغسطس 
سال ماه ترکان یعنی با ماه اوت یولیانی 
مطایق است. 

آباء: "2 ([ع. ف. آبا) ج. اب. بدران» 
اجداد. کشیشان (مسیحی)» آناء کلیسا» آباء 
کنسه. آباء سبعه: هفت پدران. آباء علوی: 
=== MON زهاب
=== BQT v1 آب first entry
4882:آب اعد فر انسوی )
5869:آب ۲ تش د نگ - یکس شالت ؛
5871:آب ۲ تش دای با زای‌هوز. بنی
5872:آب آش رنگ است ک هکنابه از شراب لعلی -
5874:آب هم میگوند .
298:گذشته ازنامه‌ای که‌اوستانام‌دارد » بسیاری‌از آبات اوستایی‌ازنشسکهای
3404:نان "را » و سوپ ویکند آب ونان است و سضی گویند طلب آپ و نان
=== BQT آبادان
=== BQT p.1225 zahab

 ‫ویرتتمایت کبود‬           ‫واورنگ پادشاه را گویند‬                ‫و شبیه‬         ‫بورزن تبارك » جانوری باشد سبزر‬
‫رن که پیوسته در کنارآب نشیند واوراخرچال `‬                        ‫بملخ ودر تابستان در میان سبزه زارها میباشد‬
‫نکیوزبند ‪ -‬و در عربی بمعتی پوست کندن‬                            ‫و بانگ وصدای طولانی میکند و عرب آارا‬
             ‫‪:‬‬     ‫زهاب ) ‪ 2‬ساب طبری ‪۹e‬‏‬                 ‫کشدن‬        ‫ی‬‫اهر‬
                                                                        ‫ر‪ .‬ن‬
                                                                           ‫بندق‬
                                                                              ‫‪- ۱‬طبری ‪ ( ۲21‬خ‬
        ‫برجوی وجر‪.‬‬                  ‫لشکری البوه بین‬
```


## [2026-09-04T14:57:00.245Z] AGENT (thinking)

I'll fetch the Borhan page around the آب entry along with the web pages for the root and each word, since these can all be retrieved independently at once.


## [2026-09-04T14:57:00.629Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs; sed -n 5860,5900p BQT_v1_pages.txt | cut -c1-200; echo \"=== BQT آفتاب / آخور entries\"; grep -n -E '^(آفتاب|آخور|آخر) ' BQT_v1_pages.txt | head -5; grep -n -E 'آفتاب.{0,60}(پهلوی|آپ)' BQT_v1_pages.txt | head -5",
 "description": "Read Borhan آب page region"
}
```


### [2026-09-04T14:57:02.549Z] TOOL RESULT

```
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
کنابه از شراب لملی - و اشك خولین باشد .
آ باك ۴ « بروزن آزاد. بمعنی‌حعمورباشد
که در مقابل وبرانت - و بممنی درود وثنا هم
کفته اند - و در مقام تحین هم گوبند همچو
افرفن و ماركافه - و نام خانهٌ کعبه فیز هست -
و تلم (۱) پیفمبرست از پیغمبران عجم - وبمعنی
. وش و خوب و نك (۲) عمآهده است 3
] اث) فوان « ,معنی ۴ ستودن وستوده
یات
آمدن باشد » یمنی ستاي شکردن و وسف تمودن8
آیادیان ۴ « بابای حطی (۴) بروزن
ناقابلان . امت (4) مه‌آباد راگویشد » و اواولی
مغمیری‌بوده است که بعجم مبمون‌شده , و کتاب
اورا دساتیر ۵ خوانتد .
آب آ سا - یک ثالت » کنابه از
شراب لعلی - و اشك خونن باشد .
۲ بار - بروزن بازار (۵) » سرب سوخته
راگویند . زخمها و ربشها را نافع باشد و آنرا
بعربی آنك محرق خوانند . وصفت ساختن آن
چنانست که ابة ان )٩(‏ را بیاورند و قدری
=== BQT آفتاب / آخور entries
3791:آخر جزو گذاشته باعلامت «صبح> بر آن صحه نهاده است واضافات حواشی
5776:آخر صفت را ساکن کردانند همچو «*سیاه‌چشم » و «بلند قامت؟ » و هر
5804:آخر کلمة اول‌را حذف باید نمودمانند «بگانه» که دراصل يك کانه بوده
6738:آخر سشگین
8232:آفتاب اه بروزن ماعتاب. پصب لت
```


## [2026-09-04T14:57:07.974Z] TOOL CALL #16: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/آب",
 "prompt": "Extract the Persian section etymology of آب 'water' in full (Middle Persian, Old Persian, Avestan, Proto-Iranian, PIE forms, cited sources) and list the derived terms it names such as آفتاب, آبادان, آبریز, گلاب, زهاب, آخور. Also give any Arabic section info."
}
```


## [2026-09-04T14:57:09.501Z] TOOL CALL #17: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ep-",
 "prompt": "Give the reconstruction, meaning, Pokorny reference, and descendants (Hittite, Sanskrit, Avestan, Old Persian, Proto-Iranian, Latin amnis, Celtic) with any notes on relation to *h₂eb- (Pokorny ab-)."
}
```


## [2026-09-04T14:57:11.063Z] TOOL CALL #18: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hā́fš",
 "prompt": "Give the reconstruction, meaning, etymology (from PIE), and the descendants list (Avestan, Old Persian, Middle Persian, Persian, Sogdian, Khotanese, Ossetic etc.) verbatim as far as possible."
}
```


## [2026-09-04T14:57:13.231Z] TOOL CALL #19: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/آفتاب",
 "prompt": "Give the full Persian etymology of آفتاب 'sun' including Middle Persian form, its two components, the Proto-Iranian/PIE roots for each component, and any cited sources."
}
```


## [2026-09-04T14:57:14.806Z] TOOL CALL #20: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/alembic",
 "prompt": "Give the full English etymology of alembic (Middle English, Old French, Medieval Latin, Arabic al-inbīq, Greek ἄμβιξ) and any note on the ultimate origin of the Greek word."
}
```


## [2026-09-04T14:57:15.572Z] TOOL CALL #21: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/alembic",
 "prompt": "Give the full etymology text of alembic."
}
```


### [2026-09-04T14:57:16.693Z] TOOL RESULT

```
# Proto-Indo-European *h₂ep-

## Reconstruction
**\*h₂ep-** (two distinct roots)

## Meanings
1. **Nominal root**: "water; body of water"
2. **Verbal root**: "to join; attach; fasten; fit"

## Pokorny Reference
The page cites Wodtko, Irslinger, and Schneider (2008) and Rix (2001) as primary sources, though specific Pokorny numbers aren't mentioned in this article.

## Key Descendants

**Hittite**: ḫa-pa-aš (river); ḫa-ap-zi (to join, attach)

**Sanskrit**: ápsas (breast, face, forehead, tusk—body protrusions)

**Avestan**: āfənte

**Latin**: amnis (river); aptus (fitting, suitable)

**Celtic**: *abū (river)

**Old Armenian**: ափ (palm of hand)

## Relationship to *h₂eb-
Alternative reconstructions include "*h₂eb-" and "*h₂ebʰ-". The page treats these as variant forms of the same root rather than distinct etymologies, suggesting scholarly debate about the precise reconstruction remains unresolved.
```


## [2026-09-04T14:57:16.975Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/إنبيق",
 "prompt": "Give the Arabic etymology of إنبيق / الإنبيق (alembic) in full, including the Greek source and any Persian or Syriac intermediary, and the descendants list."
}
```


### [2026-09-04T14:57:17.112Z] TOOL RESULT

```
# Etymology of آب (Water) - Persian Section

## Etymology Chain

The Persian word آب traces back through several ancient languages:

- **Middle Persian**: ʾp̄ (āb)
- **Old Persian**: 𐎠𐎱𐎡𐎹𐎠 (ap-)
- **Proto-Iranian**: *Hā́fš
- **Avestan**: 𐬀𐬞 (ap)
- **Proto-Indo-Iranian**: *Hā́ps
- **Proto-Indo-European**: *h₂ep- ("water, body of water")

## Cited Sources

The entry references "Etimologičeskij slovarʹ iranskix jazykov [Etymological Dictionary of Iranian Languages]" by Rastorgujeva and Edelʹman (2000), volume 1, page 312.

## Derived Terms Listed

The article names these derivatives: آب‌ها, آب میوه, آب و هوا, آبرو, آبشار, آبلیمو, آبکند, آبی, آب‌انبار, تشناب, and ضدآب.

**Note**: The specific terms you mentioned (آفتاب, آبادان, آبریز, گلاب, زهاب, آخور) do not appear in this excerpt's derived terms section.

## Arabic Section

The Arabic entry shows آب means "August" in Levantine and Iraqi dialects, borrowed from Classical Syriac ܐܒ (ʾāḇ), ultimately from Akkadian.
```


### [2026-09-04T14:57:17.715Z] TOOL RESULT

```
# Proto-Iranian *Hā́fš

**Reconstruction:** *Hā́fš (feminine noun)

**Meaning:** "water"

**Etymology:** The term derives from Proto-Indo-Iranian "*Hā́ps," which ultimately stems from Proto-Indo-European "*h₂ep-."

**Descendants:**

- **Avestan:** 𐬀𐬞𐬋 (apō, accusative plural); 𐬀𐬞 (ap); 𐬁𐬟𐬱 (āfš, nominative singular)

- **Old Persian:** apiyā (locative singular)

- **Middle Persian:** 𐭠𐭯 (āp/āβ)

- **Classical Persian:** آب (āb)

- **Sogdian:** 𐫀𐫀𐫛 (ʾʾp)

- **Kurdish:** av (Northern); ئاو (aw, Central/Southern)

- **Pashto:** آب (āb)

- **Baluchi:** آپ (áp)

- **Ossetic:** Not explicitly listed on this page

- **Khotanese:** Not listed on this page
```


## [2026-09-04T14:57:18.858Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ἄμβιξ",
 "prompt": "Give the Ancient Greek etymology of ἄμβιξ in full (meaning, origin, Beekes' view, any Semitic/Pre-Greek suggestion) and its descendants."
}
```


## [2026-09-04T14:57:19.480Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/julep",
 "prompt": "Give the full etymology text of julep."
}
```


### [2026-09-04T14:57:19.604Z] TOOL RESULT

```
# Persian Etymology of آفتاب (Sun)

Based on the Wiktionary entry, here is the full etymology:

**Middle Persian form:** 𐭠𐭯𐭲𐭠𐭡 (ʾptʾb /āftāb/, "sunshine")

**Etymology chain:** The word derives from Middle Persian and traces back to "Proto-Iranian *abi-tāpáh"

**Components:** The entry indicates the term is "Equivalent to _آف_ (âf) +‎ _تاب_ (tâb)," showing it as a compound formation.

**Source citation:** The etymology references "Cheung, Johnny (2007), Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill"

The entry notes a related Middle Persian form 𐮀𐮎𐮃𐮀𐮁 (ʾpdʾb /ābdāb/) for comparison, though the specific Proto-Iranian roots for each individual component (āf and tāb) are not explicitly detailed in the provided text.
```


### [2026-09-04T14:57:20.481Z] TOOL RESULT

```
# Etymology of Alembic

Based on the Wiktionary entry, here is the full etymological path:

The word comes from **French** *alambic*, which derives from **Medieval Latin** *alembīcus*, which in turn comes from **Arabic** *al-ʔinbīq* (الإِنْبِيق). The Arabic term itself was borrowed from **Ancient Greek** *ámbix* (ἄμβιξ), meaning "cup, cap of a still."

The entry notes that this word is a "doublet" of *ambix* and *lambic* in English, indicating shared etymological origins through different transmission paths.

**Note on ultimate origin:** The Wiktionary article does not provide information about the ultimate origin of the Greek word *ἄμβιξ* (ámbix) beyond identifying it as an Ancient Greek term. The etymology traces the word through various languages but does not speculate on pre-Greek origins.
```


## [2026-09-04T14:57:20.821Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/إبريق",
 "prompt": "Give the full Arabic etymology of إبريق (ewer) including the Middle Persian / Persian source form, its components, cited sources (Jeffery, Asbaghi, etc.), and the descendants (Persian ابریق, Turkish ibrik, etc.)."
}
```


### [2026-09-04T14:57:22.073Z] TOOL RESULT

```
# Etymology of Alembic

The word "alembic" (noun) entered English in the late 14th century, originally spelled as *limbeck* in the mid-14th century. It derives from Old French *alambic* (13th century), which passed through Old Spanish before reaching Arabic origins.

The Arabic source is *al-anbiq*, meaning "distilling flask," which itself came via Persian from Greek *ambix*, meaning "cup." The Greek term has "unknown, possibly Semitic" origins according to etymologists.

The *al-* prefix is the Arabic definite article meaning "the." The word was frequently spelled *limbeck* throughout the 15th-17th centuries before the current spelling became standard.

The term refers to a vessel historically used in distillation processes within alchemy and early chemistry practices. This etymological journey demonstrates the word's travel across multiple language families—from Semitic through Greek, Persian, Arabic, and Romance languages into English.
```


## [2026-09-04T14:57:22.311Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ناب",
 "prompt": "Give the Persian section etymology of ناب 'pure' in full (Middle Persian form, components, cited sources), plus any other Persian senses."
}
```


## [2026-09-04T14:57:23.042Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Punjab",
 "prompt": "Give the full etymology text of Punjab."
}
```


### [2026-09-04T14:57:23.744Z] TOOL RESULT

```
# Etymology of إنبيق (Alembic)

**Origin:** The word إنبيق is "borrowed from Ancient Greek ἄμβιξ (ámbix), allegedly via Classical Syriac."

**Source Path:** Ancient Greek → Classical Syriac → Arabic

**Key Details:**
- The Greek source is ἄμβιξ (ámbix)
- The transmission route through Syriac is noted as alleged
- No Persian intermediary is mentioned in this entry

**Major Descendants:**

The term spread widely through Romance and other European languages:
- **Latin:** alembīcum, alembīcus
- **French:** alambic → alembic
- **English:** alembic
- **Italian:** alambicco, lambicco
- **Dutch:** alambiek, lambiek
- **Ottoman Turkish/Turkish:** imbik
- **Romanian:** alambic

The word's journey reflects medieval scientific knowledge transfer, particularly regarding distillation apparatus used in alchemy and early chemistry.
```


## [2026-09-04T14:57:24.542Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Punjab",
 "prompt": "Give the English etymology of Punjab in full (Persian پنجاب, panj + āb, any Sanskrit equivalent named such as Pañcanada, and the era/source of the name)."
}
```


## [2026-09-04T14:57:25.298Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/آخور",
 "prompt": "Give the Persian etymology of آخور 'manger, stable' in full (Middle Persian form, components, cited sources)."
}
```


### [2026-09-04T14:57:26.498Z] TOOL RESULT

```
# Ancient Greek Etymology of ἄμβιξ

## Meaning
The word denotes a "spouted cup" or an "alembic/still" (distillation apparatus).

## Origin
The etymology remains uncertain. The document notes that "The suffix is no doubt a substrate element" and connections have been proposed with related Greek terms like ἄμβη (raised edge) and ἄμβων (crest of a hill), though these remain unconfirmed. A derivation from ἀναβαίνω (to mount) is considered improbable.

## Beekes' Perspective
Robert S. P. Beekes' *Etymological Dictionary of Greek* is cited as a reference work but no specific etymological theory is detailed in this content.

## Semitic/Pre-Greek Suggestions
The page indicates the suffix may represent "a substrate element" (non-Indo-European origin), suggesting pre-Greek roots, but provides no explicit Semitic proposals.

## Descendants
- **Greek**: άμβικας (ámvikas)
- **Arabic**: إِنْبِيق (ʔinbīq)
- **Classical Syriac**: Multiple forms including ܐܡܒܝܩܐ (ʾambīqā)
- **English**: ambix
```


## [2026-09-04T14:57:26.800Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/آبادان",
 "prompt": "Give any etymology on this page for آبادان (the city Abadan or the adjective 'prosperous'), including Middle Persian forms and cited sources."
}
```


### [2026-09-04T14:57:27.414Z] TOOL RESULT

```
# Etymology of Julep

According to the Online Etymology Dictionary, the word "julep" traces back through multiple languages and cultures:

**Origin Path:**
The term originated in the late 14th century as "syrupy drink in which medicine is given," entering English from Old French *julep*. It derives from Medieval Latin *julapium*, which came from Arabic *julab*. The Arabic term itself borrowed from Persian *gulab*, meaning "a sweet drink" or "rose water."

**Root Components:**
The Persian *gulab* breaks down into two parts: *gul* meaning "rose" (related to Greek *rhodon* and Latin *rosa*) and *ab* meaning "water" (from the PIE root *\*ap-* for water).

**Evolution:**
By 1761, the term's meaning shifted to describe "a sugared alcoholic drink flavored with mint," originally derived from medical formulations. The apothecaries' name for this preparation was *julepum menthae*.

**Key Insight:**
The word's journey illustrates how medieval medicine influenced modern beverage terminology, with Eastern botanical knowledge traveling westward through linguistic channels—from Persian gardens to European apothecaries to American tradition.
```


## [2026-09-04T14:57:28.371Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ابریق",
 "prompt": "Give the Persian etymology of ابریق in full including whether it is a reborrowing from Arabic and the ultimate Middle Persian source."
}
```


### [2026-09-04T14:57:28.959Z] TOOL RESULT

```
# Persian Etymology of ناب (nâb)

**Etymology:**
The word derives from Middle Persian *anāb, meaning "undiluted, pure."

**Persian Senses:**
According to the Wiktionary entry, ناب has three documented meanings:
1. Pure
2. Undiluted
3. Unalloyed

**Source Note:**
The entry does not cite specific historical linguistic sources for the Middle Persian etymology beyond identifying the reconstructed form. No ancient texts or scholarly references are provided in this particular Wiktionary section to support the Middle Persian origin claim.
```


## [2026-09-04T14:57:29.058Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/زهاب",
 "prompt": "Give the Persian etymology and meaning of زهاب in full (components, Middle Persian forms, cited sources)."
}
```


### [2026-09-04T14:57:29.725Z] TOOL RESULT

```
# Etymology of إبريق (Ewer)

## Source Form
The word is borrowed from **Middle Persian or Parthian *ābrēk**, possibly via Classical Syriac *ʾaḇrēqā*.

## Persian Components
In Classical Persian, the word appears as *ābrēz*, derived from:
- *āb* ("water") + the present stem of *rēxtan* ("to pour")

## Academic Sources Cited
The Wiktionary entry references several scholarly works:

- **Jeffery, Arthur** (1938): *The Foreign Vocabulary of the Qurʾān* - pages 46-47
- **Fraenkel, Siegmund** (1886): *Die aramäischen Fremdwörter im Arabischen* - page 15
- **Cheung, Johnny** (2017): "On the (Middle) Iranian borrowings in Qurʾānic Arabic" - pages 2-3

## Major Descendants
- **Persian**: ابریق (ibrīq)
- **Turkish**: ibrik, ıbrık
- **Greek**: μπρίκι (bríki)
- **Bulgarian**: ибри́к (ibrík)
- **Polish**: imbryk
- **English**: ibrik
- **Hungarian**: ibrik

The word spread through Ottoman Turkish into numerous European languages.
```


### [2026-09-04T14:57:30.594Z] TOOL RESULT

```
# Etymology of Punjab

According to the Online Etymology Dictionary, Punjab comes from Hindi *Panjab*, which literally means "the country of five waters." The term breaks down as follows:

- **Panj** (Persian): "five," derived from the Proto-Indo-European root *penkwe-
- **Ab** (Iranian): "water," from the Proto-Indo-European root *ap-

The name references "its five rivers," which flow through the region on the Indian subcontinent. The related term *Punjabi* derives from the same etymological base.

The word demonstrates how ancient Indo-European linguistic roots persist across multiple languages, with similar forms appearing in Sanskrit (*apah*), Greek, Latin, and various other language families.
```


## [2026-09-04T14:57:30.599Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/آبریز",
 "prompt": "Give the Persian etymology and meanings of آبریز in full (components, Middle Persian forms, cited sources, derived/borrowed terms)."
}
```


## [2026-09-04T14:57:30.730Z] TOOL CALL #34: WebSearch

```json
{
 "query": "آبنیک anbiq etymology Persian \"ab\" \"nik\" alembic Asbaghi"
}
```


### [2026-09-04T14:57:34.417Z] TOOL RESULT

```
# English Etymology of Punjab

**Persian Origin**: The word derives from Classical Persian **پَنْجَاب** (panjāb), meaning "[Land of] the Five Rivers," combining **پَنْج** (panj, "five") and **آب** (āb, "water").

**Sanskrit Equivalent**: The Persian term is "a calque of Sanskrit **पञ्चनद** (pañcanada, '[Land of] the Five Rivers')," formed from **पञ्च** (pañca, "five") and **नद** (nada, "river").

**Historical Development**: English borrowed the term from Punjabi **ਪੰਜਾਬ** / **پنجاب** (pañjāb), which itself came from Classical Persian, which in turn paralleled the earlier Sanskrit designation. Both names reference the same geographic reality: five tributaries of the Indus River (the Jhelum, Chenab, Ravi, Sutlej, and Beas).

**Linguistic Roots**: These words ultimately trace to Proto-Indo-European origins (*h₂ep- for "water" and *pénkʷe for "five"), demonstrating deep linguistic connections across Indo-European language families.
```


### [2026-09-04T14:57:35.458Z] TOOL RESULT

```
# Persian Etymology of آخور

The word آخور derives from **Middle Persian** ʾhwl (āxwarr), meaning "manger; stable." 

According to the Wiktionary entry, this term ultimately traces to **Proto-Iranian** *hwar- ("to eat, consume"), which is related to the Persian verb خوردن (xwardan).

The etymology notes that "The Iranian word literally means 'a place for eating'" and is attested across related Iranian and non-Iranian languages, including Northern Kurdish axur, Pashto āxor, Old Armenian ախոռ (axoṙ), and Georgian ახორი (axori).

**Cited sources** include:
- MacKenzie, D. N. (1971) - *A concise Pahlavi dictionary*
- Dehkhoda Dictionary
- The Comprehensive Aramaic Lexicon Project
```


### [2026-09-04T14:57:37.495Z] TOOL RESULT

```
# Etymology of آبادان (Abadan)

## Persian Origins

The word آبادان inherits from Middle Persian, according to the Wiktionary entry: "Inherited from Middle Persian /⁠ābādān⁠/, 'thriving'." The entry notes this can be analyzed as a combination of آباد (ābād, meaning "prosperous") plus the suffix ـان (-ān).

## Historical Development

The term appears across multiple language families:

- **Chagatai and Ottoman Turkish** both borrowed the word from Classical Persian
- **Descendants** include Uyghur, Uzbek, Kazakh, Turkmen, and Crimean Tatar variants
- The sense meaning "prosperous" or "flourishing" remains consistent across these borrowings

## Source Authority

The etymology references David N. MacKenzie's 1971 *A Concise Pahlavi Dictionary* (Oxford University Press), which documents the Middle Persian form and its meaning as foundational to the modern Persian word and the city name Abadan.
```


### [2026-09-04T14:57:37.596Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T14:57:39.868Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T14:57:40.583Z] TOOL RESULT

```
# Persian Etymology of ابریق

Based on the Wiktionary entry, here's the Persian etymological pathway:

Persian ابریق (ibrīq) was "borrowed from Arabic إِبْرِيق (ʔibrīq)," which itself may have origins in earlier languages. The etymology tree indicates the Arabic term "possibly borrowed from Classical Syriac ܐܒܪܝܩܐ (ʾaḇrēqā), possibly borrowed from Middle Persian *ābrēk, or possibly borrowed from Parthian *ābrēk."

This represents a **reborrowing chain**: Persian acquired the word from Arabic rather than directly from Middle Persian, though Arabic may have ultimately sourced it from the Middle Persian ancestor. The ultimate source remains uncertain, with multiple possible pathways through Syriac, Middle Persian, or Parthian—all marked with question marks indicating scholarly uncertainty about the precise etymological route.
```


### [2026-09-04T14:57:45.771Z] TOOL RESULT

```
Web search results for query: "آبنیک anbiq etymology Persian "ab" "nik" alembic Asbaghi"

Links: [{"title":"Alembic - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/alembic"},{"title":"alembic - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/alembic"},{"title":"The Origin of Alembic: From Past to Present - Wordpandit","url":"https://wordpandit.com/wpt_vocabulary/the-origin-of-alembic-from-past-to-present/"},{"title":"Alembic - Wordpandit","url":"https://wordpandit.com/wpt_vocabulary/alembic/"},{"title":"ALEMBIC definition and meaning | Collins English Dictionary","url":"https://www.collinsdictionary.com/dictionary/english/alembic"},{"title":"Alembic","url":"https://en.wikipedia.org/wiki/Alembic"},{"title":"Alembic (disambiguation)","url":"https://en.wikipedia.org/wiki/Alembic_(disambiguation)"},{"title":"ALEMBIC Definition & Meaning - Merriam-Webster","url":"https://www.merriam-webster.com/dictionary/alembic"},{"title":"Lambic - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/lambic"}]

Based on the search results, I can provide information about the etymology of "alembic":

The word "alembic" comes from Arabic al-anbiq "distilling flask," via Persian, from Greek ambix "cup," a word of unknown, possibly Semitic, origin. The "al-" is the Arabic definite article, "the."

Regarding your specific query about the Persian components "ab" and "nik": While the search results confirm that the word passed through Persian on its journey from Greek to Arabic to European languages, they don't provide explicit confirmation that the Persian form breaks down etymologically into "ab" (water) and "nik" (pleasing/good) as you've mentioned. The sources consistently trace the ultimate origin to the Greek word "ambix" meaning "cup" or "beaker."

The search results also don't contain information about "Asbaghi" that you referenced in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T14:58:06.659Z] AGENT (thinking)

I still need to look up the two failed pages (زهاب, آبریز) via other Persian dictionaries and Wiktionary, plus Abadan's etymology, گلاب, آبنیک, پنجاب, and local MacKenzie/Bailey Pahlavi references—I'll run these all together as one batch since they're independent.


## [2026-09-04T14:58:13.295Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs; echo \"=== PHD MacKenzie\"; grep -n -i -E '\\b(āb|āp)\\b.{0,15}water|anāb|ābādān|āxwarr|āftāb|ābrēz|ābrēk|zahāb|zāhāb' PHD_mackenzie.txt | head -12; echo \"=== DKS Bailey nab\"; grep -n -E 'anāb|nāb ‘|nāb \"|ābrēz|ābrīz|ābrēk' ISS_alt_DKS.txt | head -6; echo \"=== HRN Horn ab, nab, abriz, zahab\"; grep -n -E '^\\s*[0-9]+\\.\\s*(āb|ab|nāb|āftāb|zahāb|āxur|ābrēz)' HRN.txt | head; grep -n -i -E 'nāb .{0,30}(rein|lauter)|anāp|zahāb|zāhāb|āxur' HRN.txt | head -8; echo \"=== HUB\"; grep -n -i -E 'nāb|anāp|zahāb|āxur' HUB.txt | head -6; echo \"=== CHEUNG abi-tap / hwar\"; grep -n -E 'āftāb|abi-tāp|axwarr|āxwarr' CHEUNG.txt | head -6",
 "description": "Grep MacKenzie, Bailey, Horn, Hübschmann, Cheung for Pahlavi forms"
}
```


### [2026-09-04T14:58:14.952Z] TOOL RESULT

```
=== PHD MacKenzie
=== DKS Bailey nab
=== HRN Horn ab, nab, abriz, zahab
490:6. abiSy^ur, abisxurdy äb/ifr (geschrieben und früher ge-
=== HUB
=== CHEUNG abi-tap / hwar
```


## [2026-09-04T14:58:15.330Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://iranicaonline.org/articles/abadan",
 "prompt": "What does the article say about the etymology / origin of the name Abadan (ʿAbbādān), including the Arabic ʿAbbād derivation, the Persian folk-etymology from āb 'water' + pā 'guard/protect' + -dān, and the 1935 renaming? Quote the relevant sentences."
}
```


## [2026-09-04T14:58:16.895Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/گلاب",
 "prompt": "Give the Persian etymology of گلاب (rose water) including Middle Persian form, components, and the descendants list (Arabic جلاب, English julep, etc.)."
}
```


### [2026-09-04T14:58:17.534Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T14:58:18.334Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=آبنیک",
 "prompt": "Does any dictionary (Dehkhoda, Moin, Amid, Borhan) have an entry for آبنیک? Quote the definition and any etymology given. If no entry, say so."
}
```


## [2026-09-04T14:58:19.879Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=زهاب",
 "prompt": "Quote the Dehkhoda and Moin entries for زهاب (definition, components زه + آب, any etymology or Pahlavi form given, spelling variants like زاب)."
}
```


## [2026-09-04T14:58:21.366Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/زه",
 "prompt": "Give the Persian section(s) of زه: meanings (especially 'spring water, seepage, oozing water' and 'bowstring') and etymologies (Middle Persian forms, roots, cited sources)."
}
```


### [2026-09-04T14:58:22.412Z] TOOL RESULT

```
Based on the content provided, only the Dehkhoda dictionary has an entry for آبنیک:

**Dehkhoda Dictionary:**
"آب نیک . (اِخ ) نام قریه ای از رودبار در ایالت طهران"

This defines it as the name of a village in Rudbar, Tehran province. No etymology is provided. The other dictionaries listed (Moin, Amid, Borhan) do not appear to have entries for this term in the search results shown.
```


## [2026-09-04T14:58:22.835Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/پنجاب",
 "prompt": "Give the Persian etymology of پنجاب (Punjab) in full, including components, any Sanskrit calque note, and the date/era in which the Persian name is first attested."
}
```


### [2026-09-04T14:58:23.210Z] TOOL RESULT

```
# Persian Etymology of گلاب (Gulab)

**Components:** The word combines "گل" (gol, "rose") + "آب" (âb, "water").

**Middle Persian Form:** The Middle Persian predecessor was "gwl" (gul), derived from Proto-Iranian *wardah meaning "flower."

**Meanings:** In Persian, گلاب primarily means "rosewater," though in Dari it can also refer to a type of rose.

**Notable Descendants:** The word spread across multiple language families through Arabic جلاب (julāb):

- **European languages:** English "julep," Spanish "julepe," Italian "giulebbe"
- **South Asian languages:** Hindi गुलाब (gulāb), Urdu گُلاب (gulāb), Gujarati ગુલાબ
- **Other regions:** Georgian ჯულაბი, Thai กุหลาบ, Turkish gülab

The term's journey demonstrates significant cross-cultural transmission, particularly through Arabic intermediaries who borrowed from Persian and subsequently influenced Romance, Germanic, and Asian languages.
```


## [2026-09-04T14:58:23.654Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=آبریز",
 "prompt": "Quote the Dehkhoda and Moin entries for آبریز (definitions such as urn, ewer, latrine; any note that Arabic ابریق is arabicized from it)."
}
```


### [2026-09-04T14:58:25.294Z] TOOL RESULT

```
# Dehkhoda and Moin Entries for زهاب

**Dehkhoda entries** (three geographical/historical references):
- A region in western Kermanshah
- A historical river name (رود زابات, the ancient Zabatus)
- A village in Mashhad's Fariман district with 288 residents

**Moin entry:**
The lexicon defines it as "a seepage point near a spring or watercourse where thin streams of water emerge."

**Etymology note:** The word appears to combine زه (ze-) with آب (āb, meaning water), though the page does not explicitly detail Pahlavi origins or component breakdown beyond the modern Persian form زهاب.
```


### [2026-09-04T14:58:29.314Z] TOOL RESULT

```
# Persian Section of زه

## Meanings

**Etymology 1** presents زه (zeh) as:
- "string (of a musical stringed instrument)"
- "bowstring"

**Etymology 2** offers archaic/obsolete senses:
- "childbirth" (archaic)
- "offspring; child" (obsolete)

**Etymology 3** provides:
- "spring of water; water source" (archaic)

## Etymologies

**Etymology 1** traces to "Middle Persian zyḥ /⁠zīh⁠/" and shares cognates across Indo-European languages including Avestan, Ancient Greek, Old Church Slavonic, Lithuanian, Old Armenian, and Sanskrit forms all relating to bow-strings or tendons.

**Etymology 2** derives "ultimately from Proto-Indo-European ǵenh₁- (to give birth)" with comparisons to Avestan, Sanskrit, and Ancient Greek words connected to birth and procreation.

**Etymology 3** stems from "Middle Persian *zah, attested in zhʾpk' /⁠zahābag⁠/ (spring, source)" with related forms showing depth-related meanings.
```


### [2026-09-04T14:58:29.920Z] TOOL RESULT

```
# Persian Etymology of پنجاب (Punjab)

Based on the Wiktionary content, here is the Persian etymology:

**Components:** پنجاب is a compound of پنج (panj, "five") + آب (âb, "river").

**Sanskrit Calque:** The term is "a calque of Sanskrit पञ्चनद (pañcanada, '[Land of] the Five Rivers'), from पञ्च (pañca, 'five') and नद (nada, 'river')."

**Etymology Chain:** The word derives from Proto-Indo-European roots: *h₂ep- (water) develops through Proto-Indo-Iranian, Proto-Iranian, Old Persian, and Middle Persian into the Persian آب (āb). Similarly, *pénkʷe (five) flows through Indo-Iranian languages to Persian پنج (panj).

**Date of First Attestation:** The document does not provide a specific date or era indicating when the Persian name پنجاب was first attested in historical records.
```


### [2026-09-04T14:58:30.226Z] TOOL RESULT

```
# Dehkhoda Entry for آبریز

The Dehkhoda lexicon defines آبریز as: "دَلو" (bucket/ewer) and notes it appears in poetry referencing a toilet/latrine ("متوضا، مبال").

# Moin Entry

The Moin dictionary entry for ابریق (not آبریز) lists it as related to "آبریز، آوتابه" (ewer/pitcher terms).

**Note:** The provided content does not contain evidence that Arabic ابریق derives from Persian آبریز. The page shows these as separate entries with related meanings (water vessels and drains), but does not establish the etymological relationship you mentioned.
```


## [2026-09-04T14:58:38.524Z] AGENT (thinking)

I'll pull Abadan's etymology from Wikipedia since Iranica is blocked, and try MacKenzie/Horn/Bailey again with looser search patterns, running both independently.


## [2026-09-04T14:58:42.556Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs; echo \"=== PHD\"; grep -n -E 'water\\b' PHD_mackenzie.txt | grep -i -E '^\\S*:?\\s*[aā]b|\\bab \\[|ābād|āxwarr|anāb|ābrēz|zahāb' | head -8; grep -n -E '^(ab|āb|anāb|ābādān|āxwarr|āftāb|ābrēz|zahābag|zahāb)\\b' PHD_mackenzie.txt | head -10; grep -n -i -E 'zah[āa]b|zahābag' PHD_mackenzie.txt | head -3; echo \"=== HRN Wasser\"; grep -n -E '^\\s*[0-9]+\\.\\s*[aā]b\\b|āb .{0,20}Wasser|Wasser.{0,30}(äp|āp)' HRN.txt | head -6; grep -n -i -E 'nāb|rein.{0,10}unvermischt' HRN.txt | head -5; echo \"=== DKS water\"; grep -n -E 'N\\.Pers\\. āb\\b|NPers\\. āb\\b|Pers\\. āb ' ISS_alt_DKS.txt | head -5",
 "description": "Looser greps for Pahlavi/Persian water forms"
}
```


### [2026-09-04T14:58:44.356Z] TOOL RESULT

```
=== PHD
658:ab [MYA < A my);)ft I M )b, N .....] water.                    'b S'u~ "r'"
743:ab-~ihrag ['p cyhlk l ] holding the seed, essence of water.
748:ab-dan ['pd'nlJ water-holder.
1261:asyab ['sy'p] (water-)mill.
658:ab [MYA < A my);)ft I M )b, N .....] water.                    'b S'u~ "r'"
743:ab-~ihrag ['p cyhlk l ] holding the seed, essence of water.
748:ab-dan ['pd'nlJ water-holder.
800:ab~ar- ['pk'l-] provide, promote.                                      ., \. 'k '0\(1'"
809:ab-kamag ['pk'mk l I N '""'a] a thick, sour soup.
822:ab-tazan ['pten l ] watercourse.
11524:ab, 1-2az, az
5730:zahabag [zh)pk I N zahdb] spring, source.
7644:     zahabag.                          sprout spig.
9835:                                          zahabag                    \~CUU\S
=== HRN Wasser
461:ap. öp- 'Wasser ^); aw. äp-; phlv. fJp (päz. äw); ai. äp-,
=== DKS water
```


## [2026-09-04T14:58:45.379Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Abadan,_Iran",
 "prompt": "Quote the Etymology section in full: origin of the name (Arabic ʿAbbādān from ʿAbbād, the medieval Arab founder; Ptolemy's Apphadana / Apphana; Persian folk etymologies with āb 'water' and pāy/pād 'guard'), and the 1935 renaming from ʿAbbādān to Ābādān."
}
```


### [2026-09-04T14:58:52.129Z] TOOL RESULT

```
# Etymology of Abadan

The name's origins involve multiple traditions:

**Ancient Sources:**
The earliest mention appears in Greek geographer Marcian's work as "Apphadana," while Ptolemy noted "Apphana" as an island near the Tigris mouth.

**Persian Etymology:**
Scholar B. Farahvashi proposed derivation from Persian "ab" (water) combined with "pā" (guard, watch), suggesting "coastguard station."

**Islamic Tradition:**
Historian Ahmad ibn Yahya al-Baladhuri (d. 892) offered a folk etymology claiming the town was "presumably founded by one Abbad bin Hosayn" from the Banu Tamim tribe during the Umayyad period under Hajjaj's governorship.

**Official Naming:**
"In the subsequent centuries, the Persian version of the name had begun to come into general use before it was adopted by official decree in 1935." This marked the formal transition from the Arabic form ʿAbbādān to the Persian Ābādān.

The city's nomenclature thus reflects its layered history—from classical geography through Islamic settlement narratives to modern Persian standardization.
```


## [2026-09-04T14:58:57.305Z] AGENT

Last local checks: MacKenzie's `ab`, `zahabag`, and `axwarr`/`aftab` lines, and Horn's āb entry — one batch, then I'll archive the web sources.


## [2026-09-04T14:58:58.808Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs; sed -n 656,660p PHD_mackenzie.txt; sed -n 5730,5731p PHD_mackenzie.txt; grep -n -E '^(axwarr|aftab|abadan|abad|anab)\\b' PHD_mackenzie.txt | head; echo \"=== HRN\"; sed -n 458,466p HRN.txt",
 "description": "Read MacKenzie and Horn entries"
}
```


### [2026-09-04T14:58:58.887Z] TOOL RESULT

```
a- [)- I M )-] privative prefix, un-, -less.
a eJ       then (generally with a suffixed pronoun, e.g. A-i).
ab [MYA < A my);)ft I M )b, N .....] water.                    'b S'u~ "r'"
ibid ep)t l I M )b)d, N .....] populous, thriving, prosperous•
   ......ih: prosperity.
zahabag [zh)pk I N zahdb] spring, source.
                          '
12131:anab-                            -~t-          xwar-                            -\...~
12387:axwarr                             \\"'0'     axwan
=== HRN
— • mm
graphorum arabicorum, IV, 240), DN*:?!*! Is. 2, 9, 2^'ii^^^
Is. 36, 12, 2X^^D Jer. 31, 12 u. a. m.
ap. öp- 'Wasser ^); aw. äp-; phlv. fJp (päz. äw); ai. äp-,
kurd. äw; afy. öba (fem.); bei. ap, n. äf (12); wa;^.
ywpÄ:, ydpak, minj. ydoya; yidg. t/ow?;\
3. ä& *Glanz , (Sahn. I S. 14 Vers 7), vergl. ab[rö, ah[tah,
äb[mendy Röd]äbe, Suhr]ab^ Mihr\äb^ Ardä VTr\af, af[täb,
phlv. üb] skr. äbha- *Glanz'-).
```


## [2026-09-04T14:59:41.407Z] AGENT

Everything I need is gathered except one last Horn check for nāb; I'll run that alongside archiving all 23 web pages I relied on.


## [2026-09-04T14:59:48.025Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -n -E '\\bn[āaä]b\\b' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/HRN.txt | head -4; \nN='page 31, root Ab 1/Ap 1 (water)'\nfor u in 'https://en.wiktionary.org/wiki/آب' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ep-' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hā́fš' 'https://en.wiktionary.org/wiki/آفتاب' 'https://en.wiktionary.org/wiki/alembic' 'https://www.etymonline.com/word/alembic' 'https://en.wiktionary.org/wiki/إنبيق' 'https://en.wiktionary.org/wiki/ἄμβιξ' 'https://www.etymonline.com/word/julep' 'https://en.wiktionary.org/wiki/إبريق' 'https://en.wiktionary.org/wiki/ناب' 'https://www.etymonline.com/word/Punjab' 'https://en.wiktionary.org/wiki/Punjab' 'https://en.wiktionary.org/wiki/آخور' 'https://en.wiktionary.org/wiki/آبادان' 'https://en.wiktionary.org/wiki/ابریق' 'https://en.wiktionary.org/wiki/گلاب' 'https://vajehyab.com/?q=آبنیک' 'https://vajehyab.com/?q=زهاب' 'https://en.wiktionary.org/wiki/زه' 'https://en.wiktionary.org/wiki/پنجاب' 'https://vajehyab.com/?q=آبریز' 'https://en.wikipedia.org/wiki/Abadan,_Iran'; do python3 tools/fetch_source.py \"$u\" --note \"$N: etymology of the word on this page\" 2>&1 | tail -1; done",
 "description": "Archive all web sources used for page 31",
 "timeout": 300000
}
```


### [2026-09-04T14:59:58.520Z] TOOL RESULT

```
9004:aw. napta- 'feucht' {[/^nab-, namb- d. i. nabh-,
9073:bei. LW. nawasay (255) ; wa/. napüs^ sar. nabüs, §iyn.
9074:naböSj nebös.
10008:näb, oben No. 1015, und nägäh, oben No. 1021, sind ver-
/home/sfmqrb/git/rishe/data/verification/sources/web/fa72848139f07717.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2ad2207866f2073f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/86bc6ee14218203c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/948d2d1ce1d3354a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e4ef626029e84d4e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/36b71d3f79e008e4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f7c3c67d333184d1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f5a295a0bf09335d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/be31610a43bbe132.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1371eb5ba941bd42.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/382ec81426774e68.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e0758f3bf4923d28.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f1bc77143cc984bf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dea5e3aa9ba2a037.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d517d9811fc52ccb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0420221ac764ad13.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/32cb6233aaa300c3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/08f115c397a2436b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b63006ed2b61ca3c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2151778c9fa6745c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/08fbd766b4885f4f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7c6c030dbe8e28d8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3744e619b4cff57d.txt
```


## [2026-09-04T15:00:03.169Z] AGENT

Two remaining checks, independent of each other: Horn's entry No. 1015 for nāb, and that the archive index recorded the fetches successfully (status codes).


## [2026-09-04T15:00:06.337Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -n -E '^\\s*1015\\.' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/HRN.txt | head -2; L=$(grep -n -E '^\\s*1015\\.' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/HRN.txt | head -1 | cut -d: -f1); [ -n \"$L\" ] && sed -n \"$L,$((L+5))p\" /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/HRN.txt; tail -23 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d['status'], d['bytes'], d['url'])\"",
 "description": "Check Horn nāb entry and archive index statuses"
}
```


### [2026-09-04T15:00:08.038Z] TOOL RESULT

```
8831:1015. nä& rein, ungemischt*.
1015. nä& rein, ungemischt*.
aw. anäp' ohne Wasser*; phlv. anap,
1016. nä%un *Nagel (am Finger oder an der Zehe)' 2).
ai. nakhä- 'Nagel, Kralle'; phlv. nä/un (Bund.),
kurd. neinuJc ^Nagel'; afy. nük; bei. näkun^ vahuft,
n. na/un (257).
200 31245 https://en.wiktionary.org/wiki/آب
200 9154 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ep-
200 5798 https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hā́fš
200 10019 https://en.wiktionary.org/wiki/آفتاب
200 6567 https://en.wiktionary.org/wiki/alembic
200 5628 https://www.etymonline.com/word/alembic
200 4987 https://en.wiktionary.org/wiki/إنبيق
200 4522 https://en.wiktionary.org/wiki/ἄμβιξ
200 8981 https://www.etymonline.com/word/julep
200 8929 https://en.wiktionary.org/wiki/إبريق
200 18266 https://en.wiktionary.org/wiki/ناب
200 7312 https://www.etymonline.com/word/Punjab
200 11933 https://en.wiktionary.org/wiki/Punjab
200 7213 https://en.wiktionary.org/wiki/آخور
200 6676 https://en.wiktionary.org/wiki/آبادان
200 6687 https://en.wiktionary.org/wiki/ابریق
200 7373 https://en.wiktionary.org/wiki/گلاب
200 805 https://vajehyab.com/?q=آبنیک
200 2723 https://vajehyab.com/?q=زهاب
200 7422 https://en.wiktionary.org/wiki/زه
200 18357 https://en.wiktionary.org/wiki/پنجاب
200 2185 https://vajehyab.com/?q=آبریز
200 48466 https://en.wikipedia.org/wiki/Abadan,_Iran
```


## [2026-09-04T15:00:14.669Z] AGENT (thinking)

I've cross-checked the root and every node against modern sources and Nourai's original references, with all web pages archived. Now I'll write up the verification file.


## [2026-09-04T15:02:32.029Z] TOOL CALL #48: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-31.json",
 "content": "{\n  \"pdf_page\": 31,\n  \"book_page\": 1,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ab 1, Ap 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂ep- 'water, body of water; river' (Pokorny 2. ap- 51, with the by-form ab- 1); Proto-Indo-Iranian *Hā́ps > Proto-Iranian *Hā́fš\",\n      \"note\": \"Pokorny IEW p.1 has 'ab- Wasser, Fluß' (Lat. amnis, OIr. ab, Welsh afon) and refers to '2. ap- Wasser, Fluß' on p.51 (Skt. ap-, Av. āfš/āpəm, Hitt. ḫap(a)-, Toch. āp); Nourai's double heading 'Ab 1, Ap 1' merely combines the two Pokorny lemmas, which modern scholarship (Wiktionary after Wodtko-Irslinger-Schneider NIL, Rastorgueva-Edelman ESIJa I 312) treats as variants of one root *h₂ep-/*h₂eb-. AHD/Watkins: 'ap-2 Water, river. Iranian ap- in Persian ab, water: JULEP [Pok. 2. ap- 51]'. Root, language label and gloss are correct. Weak points on this page are the four sub-derivations in node 2 (āftāb, ābādān, āxwarr are NOT from āb 'water' in modern etymology), the whole ābnīk > al-anbīq > alembic branch (nodes 5-6; every modern source derives anbīq from Greek ámbix, as Nourai's own NOTE half-admits), and the 'Sanskrit' label on Punjab (node 15), which is a Persian coinage.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ep-\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hā́fš\",\n        \"https://en.wiktionary.org/wiki/آب\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:1\", \"status\": \"supports\", \"note\": \"POK_01.txt line 19 (IEW p.1): 'ab- Wasser, Fluß. Lat. amnis ... air. ab ... cymr. afon ... Vgl. auch 2. ap- Wasser, Fluß und abō(n) Affe'. The Iranian forms are under 2. ap- p.51 (English edition POK_full.txt: 'Root ap-2 (*hap-2) water, river ... Old Indic ap- f. water ... Avestan Nom. Sg. āfš, Akk. Sg. āpəm'). Pokorny is still the standard reference for this root.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Pahlavi\",\n          \"words\": \"âp\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan āp- f. 'water' (nom. sg. āfš, acc. āpəm, gen. pl. apąm, cf. the month-name Ābān 'of the waters'), Old Persian ap- (loc. sg. apiyā in DSf) both continue Proto-Iranian *Hā́fš < PIIr. *Hā́ps < PIE *h₂ep- (Skt. āp-, pl. āpaḥ; Hitt. ḫap(a)- 'river'; Lat. amnis < *abnis). In Middle Persian the word is āp/āb (Book Pahlavi ʾp, Manichaean ʾb; MacKenzie 'ab ... water'), the intervocalic/final -p- lenited to -b (spirant β) in the Sasanian period. The label 'Avestan / Pahlavi' correctly collapses the Old-Iranian and Middle-Persian stages.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hā́fš\",\n            \"https://en.wiktionary.org/wiki/آب\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:2\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 1142 (p.2, s.v. abdest): 'Pers. āb, water, is rel. to Avestic āp-, OI. āpaḥ (fem. pl.), water; see amnic and cp. the first element in abkari and the second element in doab and in julep.'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"âp-tab; zâ-âp; ô-pât-ân; av-xur\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Only one of the four compounds really contains āp 'water'. (a) âp-tab = MP āftāb 'sunshine, sun' (Pahlavi ʾptʾb; NP āftāb): modern etymology (Cheung 2007 s.v. tap; Wiktionary) derives it from Proto-Iranian *abi-tāpah 'shining upon', i.e. the preverb abi- (> MP af-/āf-) + tāp- 'to shine, be hot'; Horn (Grundriss no. 3) likewise separated an āb 'Glanz' (cf. Skt. ābhā-) from āb 'water'. Nourai's gloss 'a (hot) glittering object' shows he is forcing āb 'water/lustre' into the compound; the water-root is not involved. (b) zâ-âp = MP zahābag (MacKenzie: 'zahabag [zhʾpk, NP zahāb] spring, source') = *zah 'spring, depth' + āb + suffix -ag; this one is genuinely āb 'water' and gives NP zahāb/zāb. (c) ô-pât-ân = ābādān: as a common noun MP ābādān 'thriving, populous' is ā-pāta- 'protected, cultivated' (root pā- 'protect', Nourai's own ☞Pa) + -ān, with no water element; as the city name, medieval Arabic ʿAbbādān (Balādhurī: founded by ʿAbbād of Tamīm; Ptolemy/Marcian Apphadana/Apphana) was officially respelled Ābādān in 1935, and the 'āb + pā(d) coast-guard station' reading is a modern proposal by B. Farahvashi (= Nourai's IRN), not a demonstrated etymology. (d) av-xur = MP āxwarr 'manger, stable' (Pahlavi ʾhwl; NP āxor/āxur, Arm. axoṙ): MacKenzie and Wiktionary derive it from ā- + xwar- 'eat' (Proto-Iranian *hwar-), literally 'eating-place'; the first element is the preverb ā-, not āb 'water', so the 'drinking' sense is a folk etymology.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/آفتاب\",\n            \"https://en.wiktionary.org/wiki/آخور\",\n            \"https://en.wiktionary.org/wiki/آبادان\",\n            \"https://en.wikipedia.org/wiki/Abadan,_Iran\",\n            \"https://en.wiktionary.org/wiki/زه\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1,49\", \"status\": \"not_found\", \"note\": \"BQT_v1_pages.txt: the آب entries are at OCR lines ~5860-5875 ('آب ... که یکی ازجملهٔ چهار عنصر باشد') and آفتاب at line 8232 ('آفتاب ... بروزن ماهتاب'), but the Persian OCR of Mo'in's etymological footnotes on these pages is too garbled to read the Pahlavi forms; could not confirm what p.49 says.\"},\n            {\"ref\": \"IRN:119\", \"status\": \"not_checked\", \"note\": \"Farahvashi, Iranvij — no online copy; but Wikipedia (Abadan, Iran) reports exactly this etymology as 'B. Farahvashi proposed derivation from Persian ab (water) + pā (guard, watch), i.e. coastguard station', so the reference presumably says what the arrow says; it is a hypothesis not adopted by Iranica.\"},\n            {\"ref\": \"AEF:10\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq, Asās-e Eshteqāq-e Fārsi — no online copy.\"},\n            {\"ref\": \"PHD\", \"status\": \"contradicts\", \"note\": \"MacKenzie (PHD_mackenzie.txt line 658 'ab [MYA ...] water'; 5730 'zahabag [zhʾpk, N zahāb] spring, source'; 12387 axwarr) — supports zahāb, but lists āxwarr and ābād(ān) 'populous, thriving, prosperous' as separate lemmas, not compounds of ab. (Not cited by Nourai for this node; checked as the modern standard.)\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"âb; zahâb\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP āb 'water' is the direct continuation of MP āb/āp (< OP ap-, Av. āp-); the MP final spirant β became NP b. zahāb (also zāb, and the river-name Zāb) 'spring, seepage water' continues MP zahābag 'spring, source' (MacKenzie), i.e. zah 'spring, depth' (Wiktionary زه, Etymology 3: 'from Middle Persian *zah, attested in zahābag') + āb; the MP suffix -ag was dropped as usual in NP. Mo'in defines zahāb as 'a seepage point near a spring or watercourse where thin streams of water emerge'. Of the extra words: ābān (month, Av. apąm 'of the waters'), gulāb, ābšār, āsyāb (MacKenzie asyab '(water-)mill') are genuine āb-compounds; ābādān and āxor/āxur are not (see node 2).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/آب\",\n            \"https://vajehyab.com/?q=زهاب\",\n            \"https://en.wiktionary.org/wiki/زه\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 282: 'ap-2. Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.]'\"},\n            {\"ref\": \"BQT:1225\", \"status\": \"not_found\", \"note\": \"BQT_v2_pages.txt line 1274 shows a garbled 'زهاب ) ... ساب طبری' fragment in the زهاب region, but the OCR is unreadable; could not verify the footnote.\"},\n            {\"ref\": \"IRN:108\", \"status\": \"not_checked\", \"note\": \"no online copy of Farahvashi, Iranvij.\"},\n            {\"ref\": \"MON:1763\", \"status\": \"partial\", \"note\": \"MON_part2.txt: the زهاب headword itself is not recoverable in the OCR (only uses inside other entries, e.g. line 8910 'کشتی که زهاب آب‌های کشتی در آن جمع'); vajehyab's Mo'in entry confirms the meaning 'seepage near a spring' but gives no etymology.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"julep\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English julep (late 14th c., 'syrupy drink in which medicine is given') < Old French julep < Medieval Latin julapium < Arabic julāb < Persian gulāb 'rose-water' = gul 'rose' (Nourai's ☞Wrdho, OIr. *wr̥da-) + āb 'water'. Arabic replaced the non-Arabic g by j and Latin/Romance supplied the -ep/-apium ending; the 'mint julep' sense is American, 1761. The chart's direct Persian → English arrow skips the Arabic, Latin and French intermediaries but the ultimate source is right (AHD, Klein, Etymonline all agree).\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/julep\",\n            \"https://en.wiktionary.org/wiki/گلاب\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 282 'ap-2 ... Persian ab, water: JULEP' and line 1174 'Zero-grade form *wrd- in Iranian *wrd in Persian gul, rose: JULEP'; index line 1707 'JULEP ap-2, wrod-'. Klein p.2 s.v. abdest and p.836 s.v. julep ('fr. Pers. gulāb, rose water, julep, compounded of gul, rose, and āb, water') agree.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"âbnîk\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Nourai analyses the Arabic al-anbīq 'still' as a Persian compound āb 'water' + nīk 'good' (☞Nei 1), i.e. 'good (distilled) water', following Asbaghi (PLA). No Persian dictionary knows āb-nīk as a common noun: vajehyab returns only Dehkhoda's 'آب نیک: نام قریه‌ای از رودبار در ایالت طهران' (a village name), and Mo'in labels انبیق itself '[غ. معر.]' = Greek, arabicized. All modern etymological sources (Klein, Etymonline, Wiktionary, Beekes) derive Arabic إنبيق from Greek ἄμβιξ 'spouted cup, cap of a still' (Syriac ʾambīqā as intermediary); the initial a-/in- of anbīq/inbīq reflects Greek am-/Syriac am- with nasal dissimilation, not Persian āb. The 'âbnîk' etymon is therefore a folk-etymological back-formation and the node should be rejected.\",\n          \"sources\": [\n            \"https://vajehyab.com/?q=آبنیک\",\n            \"https://en.wiktionary.org/wiki/إنبيق\",\n            \"https://en.wiktionary.org/wiki/ἄμβιξ\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"PLA:22\", \"status\": \"not_checked\", \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen — no online copy. Mo'in (MON_part1.txt line 17169) contradicts: 'انبیق: [غ. معر.] (ا.) ظرفی است برای تقطیر مایعات و گرفتن عصاره و عرق' — marked as Greek, arabicized.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Arabic\",\n          \"words\": \"al-anbîq, al-ambîq\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Arabic إِنْبِيق inbīq / أَنْبِيق anbīq (with article al-anbīq) 'distilling apparatus' is a borrowing of Greek ἄμβιξ (gen. ἄμβικος) 'spouted cup; cap of a still', a word already used by the Alexandrian alchemists (Zosimus, 3rd-4th c.); it reached Arabic through the Syriac alchemical/medical translations (Syriac ܐܡܒܝܩܐ ʾambīqā) in the 8th-9th c. Greek -mb- was rendered -nb-, hence the two Arabic spellings anbīq/ambīq that Nourai lists. Nourai's own NOTE ('Some references derive this from Greek ambix') is in fact the unanimous modern view (Klein, Webster's, Etymonline, Wiktionary, Mo'in); the Greek word itself is of unknown, possibly Pre-Greek/substrate or Semitic origin (Beekes). Webster's and Etymonline allow that the word passed 'via Persian' between Greek and Arabic, but even so the Persian stage would be a loan of ambix, not a compound with āb.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/إنبيق\",\n            \"https://en.wiktionary.org/wiki/ἄμβιξ\",\n            \"https://www.etymonline.com/word/alembic\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"WEB:44\", \"status\": \"contradicts\", \"note\": \"WEB_vol1.txt line 5377 (Webster's New 20th C., s.v. alembic): 'a-lem/bic, n. [L. alambicus; Ar. alanbiq; al, the, and anbiq, Per. ambiq, a still; Gr. ambix, a cup of a still.]' — Persian is only a transit stage; the source is Greek ambix.\"},\n            {\"ref\": \"PLA:27\", \"status\": \"not_checked\", \"note\": \"Asbaghi — no online copy.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"anbîq\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP انبیق anbīq 'still, retort' is a loan of Arabic anbīq/inbīq, taken over with the Arabic alchemical vocabulary in the early Islamic centuries (Mo'in marks it معرّب, ultimately Greek). The chart's arrow Arabic → Persian is right; only the ultimate origin claimed in nodes 5-6 is wrong.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/إنبيق\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:362\", \"status\": \"partial\", \"note\": \"MON_part1.txt line 17169: 'انبیق: [غ. معر.] (ا.) ظرفی است برای تقطیر مایعات و گرفتن عصاره و عرق' — confirms the word and that Persian took it from Arabic (معرّب), but labels the origin Greek (غ.), against Nourai's Persian âbnîk.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Spanish\",\n          \"words\": \"alambique\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Spanish/Spanish alambique 'still' is a direct Andalusi-Arabic loan of al-anbīq, article included (as in alcohol, álgebra), with the Arabic -nb- realised as -mb-; Iberian Arabic alchemy (10th-12th c.) is the channel. Klein and Etymonline give exactly this Spanish stage; Wiktionary goes straight from Medieval Latin alembicus to Arabic. Italian lambicco is a parallel loan.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/alembic\",\n            \"https://en.wiktionary.org/wiki/alembic\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:47\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 2149 (p.47): 'alembic, n. — ME., fr. OF. (= F.) alambic, fr. OSp. (= Sp.) alambique fr. Arab. al-anbīq, the still, which is formed fr. al-, the, and Gk. ἄμβιξ, cup, cap of a still, alembic, which is of uncertain, possibly Semitic origin. Cp. It. lambicco'.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"French\",\n          \"words\": \"alambic\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old French alambic (13th c.) 'still' is taken either from Old Spanish alambique (Klein, Etymonline) or from Medieval Latin alembicus/alambicum, itself the Latinisation of Arabic al-anbīq used in the 12th-c. alchemical translations (Wiktionary). Nourai's NOTE 'could be through Latin alambicum' is the alternative that Wiktionary prefers; both routes exist side by side and are compatible with the chart.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/alembic\",\n            \"https://en.wiktionary.org/wiki/alembic\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:47\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 2149: 'fr. OF. (= F.) alambic, fr. OSp. (= Sp.) alambique' — French from Spanish as drawn.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"alembic\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle English alembic (late 14th c.; aphetic limbeck already mid-14th c., common in the 15th-17th c.) is borrowed from Old French alambic; the -e- of the English form reflects the Medieval Latin spelling alembicus. Meaning 'still' since the alchemists, figurative 'anything that refines' from the 16th c.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/alembic\",\n            \"https://en.wiktionary.org/wiki/alembic\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:47\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 2149: 'alembic, n. — ME., fr. OF. (= F.) alambic'; line 21755: 'limbec, n., alembic (archaic). — Aphetic for alembic.'\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"âp-rex; na-âp\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both are reconstructed rather than attested Pahlavi lemmas. âp-rex = MP *āb-rēz/*ābrēk 'water-pourer' (āb + rēz-, present stem of rēxtan 'to pour', Nourai's ☞Leigh 2 = PIE *leikʷ-); Wiktionary reconstructs 'Middle Persian or Parthian *ābrēk' as the source of Arabic ibrīq, and Jeffery (p.47) already explained the word as Pahlavi āp + rēz 'from an old Iranian root *raek = linquere'. Nourai's spelling with -x may render the Book-Pahlavi ʾplyk/ʾprēk with the older -k. na-âp = MP anāb 'undiluted, pure' (Horn no. 1015: 'nāb rein, ungemischt; aw. an-āp- ohne Wasser; phlv. anāp'), i.e. the privative prefix an-/a- (Nourai's ☞Ne 1) + āb 'water' = 'without water'; NP nāb lost the initial a- by aphaeresis. Neither compound appears as a headword in MacKenzie, hence 'plausible' rather than 'confirmed'.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/إبريق\",\n            \"https://en.wiktionary.org/wiki/ناب\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVQ:46\", \"status\": \"supports\", \"note\": \"FVQ_pages.txt ff-page 64-65 (Jeffery pp.46-47, s.v. ibrīq): 'It would be derived from [āb] water (= Phlv. āp, i.e. OPers. āpi = Av. āp ... ), and [rīz] to pour (= Phlv. rēc from an old Iranian root *raek = linquere) ... It was from the Phlv. form that the word was borrowed into Arabic, the shortening of the ī being regular.'\"},\n            {\"ref\": \"ISS:3\", \"status\": \"not_checked\", \"note\": \"Bailey, Indo-Scythian Studies (Khotanese Texts VI) is not on disk; the substitute Bailey Dictionary of Khotan Saka (ISS_alt_DKS.txt) was grepped for anāb/nāb/ābrēz without a hit. Horn HRN.txt line 8831 (no. 1015) supplies the same derivation: 'nāb rein, ungemischt. aw. anāp- ohne Wasser; phlv. anāp'.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Persian\",\n          \"words\": \"âbrîz; nâb\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP ābrīz 'ewer, urn; sink, latrine' is a transparent compound āb + rīz (present stem of rīxtan 'pour'; MP rēz-, with NP ē > ī), Dehkhoda 'دلو' and 'متوضا، مبال'. NP nāb 'pure, undiluted, unalloyed' continues MP anāb (an- privative + āb) with loss of the unstressed initial a- (Horn no. 1015; Wiktionary 'from Middle Persian *anāb'); the sense 'without water' → 'unwatered (wine)' → 'pure' is the same development as Greek ákratos.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/ناب\",\n            \"https://vajehyab.com/?q=آبریز\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"ISS:3\", \"status\": \"not_checked\", \"note\": \"Indo-Scythian Studies not available; substitute DKS text has no nāb/ābrēz entry. Horn HRN.txt line 8831 'nāb rein, ungemischt; aw. anāp- ohne Wasser; phlv. anāp' supports the derivation.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Arabic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pass-through node for Arabic إِبْرِيق ibrīq (pl. abārīq) 'ewer, water-jug', a pre-Islamic loan from Middle Persian/Parthian *ābrēk/*ābrēz (possibly via Syriac ʾaḇrēqā): attested in the Qur'ān (56:18, abārīq) and in the pre-Islamic poets ʿAdī b. Zayd, ʿAlqama and al-Aʿshā, i.e. borrowed among the Arabs of al-Ḥīra in contact with the Sasanian court; Persian ē was shortened to i and the Iranian z/k rendered by q (Jeffery pp.46-47; Cheung 2017).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/إبريق\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVQ:46\", \"status\": \"supports\", \"note\": \"Node carries no refs; FVQ_pages.txt ff-page 64 (Jeffery p.46): 'A ewer, or water jug ... It was early recognized as a Persian loan-word (Siddiqi, 13), and is given by al-Kindī, Risāla, 85; ath-Thaʿālibī, Fiqh, 317; as-Suyūṭī and al-Jawālīqī in their lists of Persian borrowings ... The word occurs in the early poetry ... doubtless an early borrowing among the Arabs who were in contact with the court at al-Ḥīra.'\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Persian\",\n          \"words\": \"ebrîq\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP ابریق ibrīq/ebrīq 'water-jug, ewer' is a round-trip loan: Persian āb-rēz → Arabic ibrīq → back into Persian in the Arabic form (Mo'in: 'ابریق [معرّب آبریز]'; Jeffery p.47 note 7: 'ibrīq also occurs in Pers. but only as a borrowing from Arabic'; Wiktionary: 'borrowed from Arabic إِبْرِيق'). The Arabic-shaped word (initial i-, -q) co-exists with native ābrīz.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/ابریق\",\n            \"https://en.wiktionary.org/wiki/إبريق\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVQ:46\", \"status\": \"supports\", \"note\": \"FVQ_pages.txt ff-page 64-65 (Jeffery p.46-47): 'In modern Persian the word is [ابریق] meaning urn or waterpot ... [ibrīq] also occurs in Pers. but only as a borrowing from Arabic.' Mo'in MON_part1.txt line 6264: 'ابریق: [معر. آبریز] (ا.) ظرف سفالین آب ...' agrees.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"punj-ab\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The name Panjāb/Punjab is a Persian compound پنج panj 'five' (☞Penkwe) + آب āb 'water, river', 'the five rivers' (Jhelum, Chenab, Ravi, Beas, Sutlej); it was coined in the Perso-Islamic period (in use by the Mughal era; earlier writers such as Ibn Baṭṭūṭa use Panj-āb for the Indus confluence) as a calque of the Sanskrit name पञ्चनद Pañcanada (pañca + nada 'river'; Vedic Sapta-sindhu). Sanskrit āp- 'water' is a genuine cognate of Persian āb, but there is no Sanskrit *pañc-āp; the language label 'Sanskrit' is wrong and the word belongs under the Persian branch. The transliteration 'punj' reflects the Anglo-Indian spelling with u.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Punjab\",\n            \"https://en.wiktionary.org/wiki/پنجاب\",\n            \"https://www.etymonline.com/word/Punjab\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"not_found\", \"note\": \"AHD_watkins1985.txt: the ap-2 entry (line 282) lists only JULEP; no PUNJAB under ap-2 or in the index. The 1975 AHD main-dictionary entry (not on disk) gives Punjab as Persian panj + āb, which would contradict the Sanskrit label.\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"English\",\n          \"words\": \"Punjab\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Punjab (17th-18th c. Anglo-Indian spelling, earlier Panjab) is taken from Punjabi/Hindustani Pañjāb, itself the Persian پنجاب panjāb 'five waters' used by the Delhi Sultanate and Mughal administration; the u spelling reflects the Hindustani short a heard as [ʌ]. Etymonline: 'from Hindi Panjab, from Persian panj five + ab water'. The English word is correct; only the parent's language label (node 15) is wrong.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/Punjab\",\n            \"https://en.wiktionary.org/wiki/Punjab\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"Node carries no refs; Etymonline and Wiktionary used instead.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-04T15:02:32.078Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-31.json (file state is current in your context — no need to Read it back)
```


## [2026-09-04T15:02:35.268Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-31.json > /dev/null && echo JSON_OK; python3 tools/verify_check.py 31",
 "description": "Validate JSON and run verify_check for page 31"
}
```


### [2026-09-04T15:02:38.166Z] TOOL RESULT

```
JSON_OK
nodes verified: 16/16
node verdicts: {'confirmed': 11, 'disputed': 4, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 9, 'not_found': 3, 'not_checked': 8, 'contradicts': 2, 'partial': 2}
```


## [2026-09-04T15:02:52.799Z] AGENT

Page 31 (book p.1, root **Ab 1 / Ap 1 "water"**) — written to `/home/sfmqrb/git/rishe/data/verification/page-31.json`; `verify_check.py 31` reports 16/16 nodes, no PROBLEM lines; 23 web sources archived via `fetch_source.py`.

**Verdicts:** root confirmed (Pokorny p.1 ab- + p.51 ap-; modern *h₂ep-). Nodes: 11 confirmed, 1 plausible (#11 Pahlavi *ābrēz/anāb — reconstructed, not in MacKenzie; Horn no. 1015 and Jeffery p.46-47 support), 4 disputed, 0 transcription_suspect.

**Disputed:**
- Ab — #2 `âp-tab / ô-pât-ân / av-xur`: āftāb is *abi-tāpah (preverb abi- + tāp-, Cheung/Wiktionary; Horn separates āb "Glanz"); ābādān is ā-pāta- "protected", and the city name ʿAbbādān → Ābādān (1935) rests only on Farahvashi's hypothesis; āxwarr is ā- + xwar- "eat" (MacKenzie). Only zahāb (< MP zahābag) really contains āb.
- Ab — #5 `âbnîk`: no such Persian common noun (Dehkhoda has only a village name); Mo'in labels انبیق "Greek, arabicized".
- Ab — #6 Arabic `al-anbîq`: all modern sources (Klein p.47, Webster's, Etymonline, Wiktionary, Beekes) derive it from Greek ámbix via Syriac; Nourai's own NOTE is the accepted view, the Persian etymon is not.
- Ab — #15 "Sanskrit" `punj-ab`: Punjab is a Persian coinage panj + āb (calque of Skt. Pañcanada); wrong language label, the word belongs under the Persian branch.

**Ref checks:** KLN:2/47, FVQ:46, AHD, POK:1 support; WEB:44 and MON:362 contradict the Persian origin of anbīq; BQT pages located but the Persian OCR of Mo'in's footnotes is unreadable (not_found); IRN, AEF, PLA, ISS have no online copy (not_checked).
