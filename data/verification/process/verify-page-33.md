# Verification process log — verify-page-33


## [2026-09-04T15:26:45.620Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 33 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-33.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-33.json. The reference table /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json is complete (local OCR texts under /home/sfmqrb/git/rishe/data/verification/sources/refs/, paginated with form-feeds; each entry gives page offsets and lookup hints). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py as required) and the local reference texts for Nourai's own citations (quote what you find). Write /home/sfmqrb/git/rishe/data/verification/page-33.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 33` to confirm complete coverage (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T15:26:47.749Z] AGENT

I'll start by reading the instructions.


## [2026-09-04T15:26:48.625Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T15:26:48.656Z] TOOL RESULT

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


## [2026-09-04T15:26:54.015Z] AGENT (thinking)

I'll fetch the chart text, source JSON, reference table, bibliography, verify script, and an example verification file all at once since they're independent of each other.


## [2026-09-04T15:26:54.024Z] TOOL CALL #2: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-33.txt",
 "description": "Show chart text for page 33"
}
```


### [2026-09-04T15:26:54.061Z] TOOL RESULT

```
=== PDF page 33 (book page 3) ===
--- entry 0 ---
ROOT [Semitic] Ab 2 : father  (refs FVQ:44; KLN:6)
#1 (parent #0) [Arabic] refs=FVQ:44; FVA:25; LKT:44 | ab, abŭ, a.b.v : father
  #2 (parent #1) [Persian] refs=FVA:25; MON | abŭ «آبو ( ابوی )» : father | extra: ابوعلی سینا ، ابوالفضل ، ابوالقاسم ، ابوالحسن ، ابوالفتح ، بوالهوس
  #3 (parent #1) [Arabic] refs=FVQ:44; FVA:25; LKT:44; AHD:152 | abŭ-zînâ : "father of whoredom" referring to gibbons ☞Z.n.y ; abŭ-araq : "father of sweat", a spicy plant used in medicine ☞A.r.q
    #4 (parent #3) [Persian] refs=MON:602; FVA:180 | bŭzîneh «بوزینه ( بوزنه )» : gibbon
      #5 (parent #4) [Hindustani] refs=PRT:253 | bojîna
        #6 (parent #5) [French] refs=KLN:655 |  | NOTE: This monkey was taken to France from India in the 18th century.
          #7 (parent #6) [English] refs=KLN:655 | gibbon
    #8 (parent #3) [Middle Latin] refs=AHD:152 | borrâco
      #9 (parent #8) [Old French] refs=AHD:152 | borrace, bourrache
        #10 (parent #9) [English] refs=AHD:152 | borage : a spicy salad seasoning
#11 (parent #0) [Hebrew] refs=KLN:6 | abh : father
  #12 (parent #11) [English] refs=KLN:6 | Abot
  #13 (parent #11) [Hebrew] refs=FVQ:44; KLN:6 | Abh-raham : father of the multitude (Abraham) ; Abh-ram : high father (Abram) ; Abh-ner : my father is light (Abner) ☞N.w.r ; Ab-šalom : father is peace (Absalom) ☞S.l.m ; Abh-igayil : father is rejoicing (Abigail) ; Yo-abh : the Lord is his father (Joab)
    #14 (parent #13) [Arabic] refs=FVQ:44 | Abrahim : Abraham
      #15 (parent #14) [Persian] refs=None | Ebrâhîm «ابراهیم»
    #16 (parent #13) [English] refs=KLN; AHD | Abraham, Abram, Abner, Absalom, Abigail, Jaob
```


## [2026-09-04T15:26:55.361Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-33.json",
 "description": "Show source JSON for page 33"
}
```


### [2026-09-04T15:26:55.393Z] TOOL RESULT

```
{
  "pdf_page": 33,
  "book_page": 3,
  "entries": [
    {
      "root": {
        "name": "Ab 2",
        "lang": "Semitic",
        "refs": "FVQ:44; KLN:6",
        "gloss": "father"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "FVQ:44; FVA:25; LKT:44",
          "words": [
            {"translit": "ab, abŭ, a.b.v", "gloss": "father", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:25; MON",
          "words": [
            {"translit": "abŭ", "gloss": "father", "script": "آبو ( ابوی )"}
          ],
          "script_extra": "ابوعلی سینا ، ابوالفضل ، ابوالقاسم ، ابوالحسن ، ابوالفتح ، بوالهوس",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Arabic",
          "refs": "FVQ:44; FVA:25; LKT:44; AHD:152",
          "words": [
            {"translit": "abŭ-zînâ", "gloss": "\"father of whoredom\" referring to gibbons", "script": null, "see": ["Z.n.y"]},
            {"translit": "abŭ-araq", "gloss": "\"father of sweat\", a spicy plant used in medicine", "script": null, "see": ["A.r.q"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:602; FVA:180",
          "words": [
            {"translit": "bŭzîneh", "gloss": "gibbon", "script": "بوزینه ( بوزنه )"}
          ],
          "note": null,
          "quote": {
            "text": "چون دل بوزینه گردد آن دلش - از دل بوزینه شد خوار آن گلش",
            "poet": "Molavî"
          }
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Hindustani",
          "refs": "PRT:253",
          "words": [
            {"translit": "bojîna", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": "KLN:655",
          "words": [],
          "note": "This monkey was taken to France from India in the 18th century.",
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "KLN:655",
          "words": [
            {"translit": "gibbon", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 3,
          "lang": "Middle Latin",
          "refs": "AHD:152",
          "words": [
            {"translit": "borrâco", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Old French",
          "refs": "AHD:152",
          "words": [
            {"translit": "borrace, bourrache", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "AHD:152",
          "words": [
            {"translit": "borage", "gloss": "a spicy salad seasoning", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:6",
          "words": [
            {"translit": "abh", "gloss": "father", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": "KLN:6",
          "words": [
            {"translit": "Abot", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 11,
          "lang": "Hebrew",
          "refs": "FVQ:44; KLN:6",
          "words": [
            {"translit": "Abh-raham", "gloss": "father of the multitude (Abraham)", "script": null},
            {"translit": "Abh-ram", "gloss": "high father (Abram)", "script": null},
            {"translit": "Abh-ner", "gloss": "my father is light (Abner)", "script": null, "see": ["N.w.r"]},
            {"translit": "Ab-šalom", "gloss": "father is peace (Absalom)", "script": null, "see": ["S.l.m"]},
            {"translit": "Abh-igayil", "gloss": "father is rejoicing (Abigail)", "script": null},
            {"translit": "Yo-abh", "gloss": "the Lord is his father (Joab)", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Arabic",
          "refs": "FVQ:44",
          "words": [
            {"translit": "Abrahim", "gloss": "Abraham", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "Ebrâhîm", "gloss": null, "script": "ابراهیم"}
          ],
          "note": null,
          "quote": {
            "text": "بت شکستی گیرم ابراهیم وار - کو بت تن را فدا کردن به نار",
            "poet": "Molavî"
          }
        },
        {
          "id": 16,
          "parent": 13,
          "lang": "English",
          "refs": "KLN; AHD",
          "words": [
            {"translit": "Abraham, Abram, Abner, Absalom, Abigail, Jaob", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-04T15:26:56.116Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json",
 "description": "Show reference lookup table"
}
```


### [2026-09-04T15:26:56.157Z] TOOL RESULT

```
<persisted-output>
Output too large (83.3KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bmt3vca1j.txt

Preview (first 2KB):
{
 "BQT": {
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
...
</persisted-output>
```


## [2026-09-04T15:26:57.636Z] TOOL CALL #5: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt",
 "description": "Show bibliography key"
}
```


### [2026-09-04T15:26:57.672Z] TOOL RESULT

```
===== page_15
 Page 15 
 TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
===== page_16
 Page 16 
 TABLE IV - Reference Abbreviations 1 AEF 2 AFA 3 AFM 4 AHD 5 AHM 6 AID 7 AIN 8 AKD 9 AKM 0 AMD i ARB 2 ARK 3 ARM 4 ARP 5 AVG 6 AWH Jalal KhaleqT Motlaq, Asas Eshteqaq Farsi, ^j1* JISsAl o"1-'' Vol. I (a - kh), Bonyad Farhang Iran, 1977. Siegmund Fraenkel, Die Aramaischen Fremdworter im Arabischen, Hildesheim, 1962. Addi Shir, Al-Alfaz Al-Farsiyya Al-Mu'arraba, (A Dictionary of Persian Words in the Arabic Language), Library of Lebanon, 1980.. W. Morris, The American Heritage Dictionary, New College Edition, 1975, Appendix on Indo-European Roots, pp 1505-1550. I. Gershevitch, The Avestan Hymn to Mithra, Oriental Publications No.4, Cambridge University Press, 1959. G. C. Withworth, Anglo-Indian Dictionary. Kegan Paul, Trench &amp; Co, London 1885. E. Liden, Studien zur Altindischen und Vergleichenden Sprachgeschichte , Almqvist &amp; Wiksells, Upsala 1897. H. Zimmem, Akkadische Fremdworter Als Beweis Fur Babylonischen Kultureinfluss, Leipzig 1917. Amir J. ATam, Farhang A'alam Ketab Moqaddas or, A Dictionary of Proper Names in the Bible, English - Persian, Iran University Press, Tehran 1988. H. A" mid, Farhang Farsi Amid, Two volumes, Amir Kabir Press, Tehran, 1369 (1990). Jawaliqi, Al-Mu'arrab, Tehran 1966. M. H. Rokn Zadeh - Adammiyat, Arkan Sokhan, Sharq Press, Tehran 1347 (1968). ^W-\A£ h_)UT joMc' OwJbjd -W*c ^— *&gt;jl^ OwJfcjd £^~&gt; O^j' A. Aryan, ks~'j'* lSj^ ^)~&gt;^ ^*j' -ujUa ^la o^lj oiajs Farhang Vajheh-hay Hamanand, Armani - AvestaT, Pahlavi, FarsT, Vol. I (a), Bonyad Nayshabflr, Tehran 1363 (1984). F. Spiegel, Die Arische Periode und ihre Zustande, Leipzig ,1887. A. V. W. Jackson, An Avesta Grammer, W. Kohl Hammer, Stuttgart 1892. H. Kinder &amp; W. Hilgemann, Atlas of World History. 2 vol., Anchor Books, 1974. A-9 
===== page_17
 Page 17 
 TABLE IV - Reference Abbreviations (continued ...) 17 BLY 18 BQT 19 BRT 20 BST 21 CEL 22 DEV 23 DMO 24 DOZ 25 DRM 26 DVS 27 DZA 28 EAV 29 ETM 30 FAF 31 FFD H. W. Baily, "Hvatanica II", (Glossary of some Khotanese words with reference to Avestan and Persian words), Bulletin of the School of Oriental and African Studies (BSOAS IX:1937-39) pp 69-78, University of London. M. H. Tabriz! (Borhan), Borhan Qate', ^l»ls ^i&amp;j&gt; Etymological footnotes by Dr. M. MoTn, 4 vol, Amfr Kabrr Press, Tehran 1362 (1983). C. Bartholomae, Altiranisches Worterbuch Zusammen Mit Den Nacharbeiten Und Vorarbeiten, Walter de Gruyter Press, 1979. Paul Horn, "Some Inscriptions on Sassanian Gems", Avesta, Pahlavi and Ancient Persian Studies, First Series, pp 224-263, Bombay Educational Society's Press, 1904. S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, 6 Vol., Sverge Haus Publishers, Milton, Ma, 1997 L. M. Devic, Dictionnaire Etymologique des Mots Francais D'Origin Orientale, Oriental Press 1876. S. NafisT, Par Maktab Ostad, ilx-,1 Zohreh Press, Tehran 1344 (1965). R. Dozy, Verklarende Lisjt der Nederlandsche Woorden, Die Uit Het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch Afkomstig Zijn, Leiden 1867. J. Darmester, Etudes Itaniennes, Paris 1883. P. Davis, Roots - Family History of Familiar Words, McGraw-Hill Book Company 1981. M. T. Rashed Mohassel, Daramadi Bar Dastur ^^jl oki _}f~&gt;* j&gt;. iSJ^&gt;^ Zaban AvestST, Khajeh Press, Tehran 1364 (1985). J. Duchesne-Guillemin, "Etymologies Avestiques", Bulletin of the school of Oriental and African Studies (BSOAS IX: 1937-39) pp 861-869, University of London. M. Abolghasemr, RTsheh ShenasT - Etimologi, Ghoghnoos Press, Tehran 1374 (1995). A. Daneshgar, Farhang A'alam Farsi, Hafez NovTn Press, 1370 (1991). M. Abolghasemr, Fe'lhay FarsT Pari, Ghoghnoos Press, Tehran 1374 (1995). v^«&gt;jls pMel 
===== page_18
 Page 18 
 TABLE IV - Reference Abbreviations (continued...) 32 FIB 33 FNI 34 FRS 35 FSD 36 FSF 37 FVA 38 FVF 39 FVQ 40 FWE 41 FWK 42 GPL 43 HID 44 HJB 45 HRN 46 HUB 47 IEC Pur Davfld, Farhang Iran Bastan, Vol. I, University of Tehran Press 1326 (1947). F. DanaT, Farhang Namhay Irani, Negah Publishers, Tehran 1370 (1991). AsadT Tflsi, Farhang Fors, Kharazmi Press, Tehran 1365 (1986). ^iljjl ^cUj^cLs &gt;^fl&gt;jS Funk and Wagnalla, New Standard Dictionary of the English Language, Funk &amp; Wagnalls Company, New York, 1940. A. H. Noushin, Farhang Shahnameh Ferdowsi, oULS 03I3 - ^-jiy i*La&gt;Li ^^ay Vajheh Namak, Donya Press, Tehran 1363 (1984). S. M. Nahvi, Farhang VSm J-^-i - ^-&gt;jl» j* ^o^ ^gb. 03I3 ^(3 ^S^a,^ Vajhehhay Arabi dar Farsi, Dakhil, TohT Azadi Press 1368 (1989). S. M. A. Emam Shflshtari, ^c ^bj ji ^-"j1* iS^ °j'3 «-fc»j» Farhang Vajhehhay Farsi dar zaban Arabi, Anjoman Asar Melli, No 58, Bahman Press, Tehran, 1347 (1968). A. Jeffrey, The Foreign Vocabulary of the Qur'an, (see VDQ). Oriental Institute, Baroda, Stephen Austin &amp; Sons Press, Great Britain 1938 A. J. Bliss, A Dictionary of Foreign Words and Phrases in Current English, Warner Books, 1966. R. Dvorak, "Fremdworter im Koran", Doctoral Dissertation, Akademische Buchdruckerei von F. Straub (1884). J.T. Platts and G.S.A. Ranking, A Grammar of the Persian Language, Oxford University Press (1911). B. Bartholomae, Handbuch der Altlranischen Dialekte, Breitkopf &amp;Hartel, Leipzig 1883. H. Yule &amp; A. C. Burnel, Hobson Jobson, A Glossary of Colloqual AngloIndian Words, Oriental Publishers, Delhi 1903-1968. Paul Horn, Grundriss der NeuPersischen Etymology, Verlag von Karl J. Trubner, Strassburg 1893-1974. H. Hubschmann, Persische Studien, Verlag von Karl J. Trubner, Strassburg 1895. Stuart E. Mann, An Indo-European Comparative Dictionary, Helmut Buske Verlag, Hamburg 1987 A-ll 
===== page_19
 Page 19 
 TABLE IV - Reference Abbreviations (continued...) 48 IRN 49 IRT 50 ISS 51 KAS 52 KFL 53 KGW 54 KLN 55 KNT 56 LAG 57 LAM 58 LAT 59 LEW 60 LKT 61 LST 62 MAG 63 MFL gsj^jljjf C. FarahvashT, Iranvij, Tehran University Press, 1368 (1989). M. A. Sajjadiyyeh, Tabar Moshtarek Iranian oMjj3 } jljljjl va Turanian, Bonyad Nayshabflr 1368 (1989). H. W. Baily, Indo-Scythian Studies (Khotanese Texts - volume VI), Cambridge University Press, 1967. M. A. Hasani Da'i Al-Eslam, ojj£-^-&lt; oki jy^j* Khod Amoz Zaban Sanskrit, Danesh Press, Tehran 1361 (1982). Tha'alebT, Ketab Feqh al-Logheh, Beirut, 1885. Jamshid Ibrahim, Kulturgeschichtliche Wortforschung. (Persisches Lehngut in Europaischen Sprachen, Wiesbaden 1991. D. Klein, A comprehensive Etymological Dictionary of the English Language, Two volumes, Elsevier Publishing Co., 1966. R. G. Kent, Old Persian - Grammer, Text, Lexicon, American Oriental Society, 1953. P. Lagarde, Persische Studien, Dieterichsce Verlag, Gottingen 1884. Henri Lammens, Remarques sur les Mots Francais Derives de l'Arabe, Imprimerie Catholique, Beyrouth 1890. A. Ernout &amp; A. Meillet, Dictionnaire Etymologique de la Langue Latine, Paris, 1951. A. Walde, Latinisches Etymologisches Worterbuch, (With Avestan and Persian Indices), Heidelberg 1938. K. Lokotsch, Etymologisches Worterbuch der Europaischen Worter Orientalischen Ursprunges, Heidelberg 1927. W. B. Henning, Bibliography of Important Studies on Old Iranian Subjects, Ketab Khaneh Danesh, Tehran 1950. G. Widengren, Mohammad, The Apostle of God, Chapter VIII, "Iranian Elements in the Kuranic Vocabulary", Uppsala Universitets Arsskrift, Uppsala, 1955 A. M. Oranski, Moqaddameh Feqh Al-Logheh Irani, ^'jj' '**&gt;S^ &amp; Z»Mb Translated into Persian by K. Keshavarz, Payam press, Tehran 1358 (1979). A- 12 
===== page_20
 Page 20 
 TABLE IV - Reference Abbreviations (continued ...) 64 MMF 65 MON 66 MPP 67 MZF 68 NAT 69 NFI 70 NYB 71 OEW 72 OXF 73 PEI 74 PHD 75 PHN 76 PLA 77 POK 78 PRT 79 RCH K. Khalili, Dictionary of Derivatives of the Persian ^wjls jiLa* ol£ii* &gt;_£^&amp;ji Infinitives or Farhang Moshtaqqat Masader FarsT, Institute of Cultural Studies and Research, Tehran, 1993. M. Mo" in, Farhang FarsT MoT'n, Six volumes, Amir Kabir press 1363 (1984). O^*® ^ ^-a-L!* Honari darbareh Zaban Farsi, Sokhan press, Tehran 1340 (1961). C. Berlitz, Native Tongues, Grosset &amp; Dunlapp Publishers, New York, 1982 F. Jonaydi, Nameh Farhang Iran, ^Ijjl ^»js i*b Bonyad Nayshabfir, Tehran 1368 (1989). Section 4, translated from C.H. Rempis' "Persische Worter im Deutschen," in Mitteilungen, Institut fur Auslands-Beziehungen, Iran-Nummer, 3/4, Stuttgart, 1960, S.229-233. H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1974. J. T. Shipley, The Origins of English Words, The John Hopkins University Press, Baltimore 1984. Jennifer Speake, Oxford Dictionary of Foreign Words and Phrases, Oxford University Press, New York 1997 M. Pei, The Families of Words, Harper &amp; Brothers press, New York 1962. D. N. MacKenzie, A Concise Pahlavi Dictionary. Oxford University press, London 1971. A. P. Pihan, Dictionnaire Etymologique des Motes de la Langue Francaise Derives de L'Arabe, du Persan ou du Turc, Paris 1866. Asya Asbaghi, Persische Lehnworter im Arabischen. Otto Harrassowitz, Wiesbaden 1988 J. Pokorny, Indogermanisches Etymologisches Worterbuck, Two volumes, Francke verlag, Bern 1959. E. Partridge, Origins - A short Etymological Dictionary of Modern English, MacMillan Co., NewYork 1958. J. Richardson, Dictionary, Persian, Arabic and English with Dissertation on the Languages, Literature and Manners of Eastern Nations, Sange-e-Meel Publications, Lahore 1829-1984. A-13 
===== page_21
 Page 21 
 TABLE IV - Reference Abbreviations (continued...) 80 ROE 81 SAP 82 SBK 83 SDQ 84 SHP 85 SIN 86 SKT 87 SLW 88 SNB 89 SNS 90 SOD 91 SOG 92 SOR 93 SPG 94 SYN 95 TAD R. Caliborne, The Roots of English, A Reader's Hanbook of Word Origins, Anchor Books, New York, 1989. A. Sayyah, Farhang Sayyah, Arabic - Persian Dictionary, ^}~&gt; «^a&gt;Js Three volumes, Translation of the Arabic "Al-Monjed" Dictionary, Eslam Publications, Tehran 1368 (1989). M. T. Bahar, Sabk ShenasT - Tarikh Tatawor Nasr Farsi, ^Ls ._£_&gt; Vol I, Tehran 1321 (1942). A. Siddiqi, Studien uber die Persischen Fremdworter im Klassischen Arabisch, Vandenhoeck &amp; Ruprecht, Gottingen 1919. J. T. Shipley, Dictionary of Word Origins, Philosophical Library press, New York 1945. G. Laufer, Sino-Iranica, Chinese Contributions to the History of Civilization in Ancient Iran, Field museum of natural History, publication 201, Anthropological Series, Vol XV, No. 3, Chicago 1919. W. W. Skeat, A Concise Etymological Dictionary of the English Language, Clarenden press, Oxford 1882-1967. W. B. Henning, "Sogdian Loan-words in New Persian", Bulletin of the School of Oriental and African Studies (BSOAS XT939-42) pp 93-106, University of London H. Kowsar, Sang Nebeshteh-ha Sokhan Miguyand, *ujj£~«&gt; Military Public Relations, Iranian Military Press, Tehran (1960's). M. Tavoosi, A Glossary of Shayast Ne Shayast, Shiraz University publications, 1986. B. Ghanb, Sogdian - Persian - English Dictionary, Farhangan Press, Tehran, 1374 (1995). jLw ^uu oV ijij ^imI^I - ^wjli - 
===== page_22
 Page 22 
 TABLE IV - Reference Abbreviations (continued...) 96 TLM 97 TTS 98 TYL 99 TZF 00 UNV 01 VDQ 02 VFO 03 VGH 04 VIE 05 VOP 06 VSF 07 WEB 08 WLD 09 ZAP 10 ZAW 11 ZFS 12 ZMA F. C. Tolman, Ancient Persian Lexicon, The Vanderbilt Oriental Series, American Book co. 1890-1908. G. Vambery, Etymologisches Worterbuch der Turko-Tatarischen Sprachen, Biblio Verlag, Osnabriick, 1972. W. Taylor, Arabic Words in English, Clarenton Press, London 1933. M. Abolghasemi, Tarikh Mokhtasar Zaban FarsT, ^-d1* oki j^""« ejJjIj Bonyad Andisheh EslamT Press, Tehran, 1373 (1994). J. M. Unvala, King Husrav and His Boy - Pahlavi Text and Glossary, Paul Geuthner publishers, Paris 1963. F. Badreh-t, Vajheh-hay Dakhil dar jl*=w oTjsji J-''2 i^l&amp;ejfj Qoran-e Majid, Translation of A. Jeffrey's book with Comments (see FVQ). Toos Publishers, Tehran 1372 (1993). M. Ahmad Soltam, Vajhgan FarsT dar Zabanhay ^jjl ^k-Sbj _ji ^j1* oT;'? OrupaT, Avay Niir Press, Tehran, 1372 (1993). H. Khadiv Jam, Vajheh Nameh Ghazalhay Hafez, Elmi Press, Tehran, 1371 (1992). £i9b» ^L^Jjc ^Ub OjT^ M. A. Sajjadiyyeh, Vajheh-hay Irani dar ^....JLCil ^bj ji ^IjjI ^la 03I3 Zaban EngelTsT, Bonyad Nayshabur, Tehran 1364 (1985). M. MoshM, Farhang Vajheh-hay Orupayl ^-"j1* j* ^kiJ lS1* °3'3 &gt;-^»j» dar FarsT, Alborz Press, Tehran 1371 (1992). K. Mehravand, Vajheh Sazi dar Zaban FarsT, Rasti press, Tehran 1349 (1970). v^-jl* ok) j4 lSJ1- °3'3 W. Collins, Webster's New Twentieth Century Dictionary of the English Language, second edition 1978. A. Walde, Vergleichendes Worterbuch der Indogermanischen Sprachen, two volumes, Walter de Gruyter &amp; co., Leipzig 1930-1973. H. W. Bailey, Zoroastrian Problems in the Ninth-Century Books, Clarendon press, Oxford 1943-1971. C. Bartholomae, Zum Altlranischen Worterbuch Nacharbeiten and Vorarbeiten, Vorlag von Karl J. Trubner, Strassburg 1906. M. Abolghasemi, Zaban FarsT va Sargozasht An, HTrmand Press, Tehran, 1375 (1996). F. Jonaydi, ZendegT va Mohajerat Aryaian, Bonyad Nayshabur, Tehran, 1374 (1995). A-15 
===== page_23
```


## [2026-09-04T15:26:58.555Z] TOOL CALL #6: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/tools/verify_check.py; echo ----; cat /home/sfmqrb/git/rishe/tools/fetch_source.py | head -80; echo ----; ls /home/sfmqrb/git/rishe/data/verification/ | head -50; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/",
 "description": "Show verify script, fetch script, and existing verification files"
}
```


### [2026-09-04T15:26:58.612Z] TOOL RESULT

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
----
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
                title = html.unescape(mt.group(1)).strip() if mt else ""
                text = html_to_text(body)
            else:
                text = body
    except Exception as ex:
        status = -1
        text = f"FETCH FAILED: {ex}"
    header = f"URL: {url}\nFETCHED: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\nSTATUS: {status}\nTITLE: {title}\n\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(header + text)
    with open(INDEX, "a", encoding="utf-8") as f:
        f.write(json.dumps({"url": url, "file": os.path.relpath(path, ROOT), "fetched": header.split("\n")[1][9:],
                            "status": status, "bytes": len(text), "title": title, "note": note}, ensure_ascii=False) + "\n")
    print(path)
    return 0 if status == 200 else 1


if __name__ == "__main__":
    sys.exit(main())
----
page-101.json
page-126.json
page-311.json
page-31.json
page-32.json
page-345.json
process
sources
AFA.txt
AFM_pages.txt
AFM.txt
AHD_watkins1985.txt
AHM.txt
AID.txt
AIN.txt
AKD.txt
ARB_abdulraheem.txt
ARB_mo3rb.txt
ARP.txt
AVG.txt
BQT_alt_v1.txt
BQT_dli_part1.txt
BQT_v1_djvu.xml
BQT_v1_pages.txt
BQT_v1.txt
BQT_v2_pages.txt
BQT_v2.txt
BRT.txt
BST.txt
CHEUNG.txt
DEV.txt
DOZ.txt
DRM.txt
EAV_studies.txt
FRS_pages.txt
FRS.txt
FSD_vol1.txt
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
FSF_pages.txt
FSF.txt
FVQ_pages.txt
FVQ.txt
GPL.txt
HENNING_selected_papers.txt
HID.txt
HJB.txt
HRN.txt
HUB.txt
IEC.txt
incoming
ISS_alt_DKS.txt
KFL.txt
KLN_1966.txt
KLN_1971.txt
KNT.txt
LAM.txt
LAT.txt
LEW_1910.txt
LKT.txt
LST.txt
MON_part1.txt
MON_part2.txt
MPP.txt
NAT_2005.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
PEI.txt
PHD_mackenzie.pdf
PHD_mackenzie.txt
PHD.txt
PHN.txt
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
RCH.txt
SBK.txt
SDQ.txt
SIN.txt
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
```


## [2026-09-04T15:27:07.497Z] AGENT (thinking)

I'll pull the reference-table entries for the page's abbreviations (FVQ, KLN, FVA, LKT, AHD, MON, PRT) along with an existing verification file to use as a format model, fetching them all at once since they're independent.


## [2026-09-04T15:27:07.512Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['FVQ','KLN','FVA','LKT','AHD','MON','PRT']:\n    print('=====',k); print(json.dumps(d.get(k),ensure_ascii=False,indent=1))\n\"",
 "description": "Show ref table entries for this page's abbreviations"
}
```


## [2026-09-04T15:27:07.532Z] TOOL CALL #8: Bash

```json
{
 "command": "head -c 6000 /home/sfmqrb/git/rishe/data/verification/page-32.json",
 "description": "Show an existing verification file as format model"
}
```


### [2026-09-04T15:27:09.360Z] TOOL RESULT

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
===== PRT
{
 "title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958",
 "edition_found": "1958 (lending-only copies)",
 "kind": "archive_restricted",
 "url": "https://archive.org/details/originsshortetym00part",
 "identifier": "originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)",
 "local_file": null,
 "page_offset": null,
 "lookup_hint": "Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q=<word>. Entries are alphabetical with numbered sub-senses.",
 "notes": "djvu.txt returns 401/403 for all copies."
}
```


### [2026-09-04T15:27:09.398Z] TOOL RESULT

```
{
  "pdf_page": 32,
  "book_page": 2,
  "verified_by": "claude-fable-5-1",
  "verified_on": "2026-09-04",
  "entries": [
    {
      "entry": 0,
      "root": "Ab 1, Ap 1",
      "verdict": "confirmed",
      "modern_form": "PIE *h₂ep- 'water, body of water; river' (Pokorny 2. ap- p.51, by-form ab- p.1) > Proto-Indo-Iranian *Hā́ps > Proto-Iranian *Hā́fš (Av. āfš/āp-, OP ap-, MP āb)",
      "note": "Part 2 of the chart begun on pdf p.31. The root is real and correctly glossed (Pokorny IEW p.1 'ab- Wasser, Fluß' cross-referring to '2. ap- Wasser, Fluß' p.51; AHD ap-2 'water, river ... Persian ab'). What this part of the chart adds is a semantic branch 'water' -> 'lustre, glitter' (NP āb 2, ābrū, āftāb) -> Arabic ubbaha -> Persian obbohat. The first step (āb 'lustre' from the glitter of a water-surface, ābrū 'water of the face') is accepted; āftāb is not from āb but from Proto-Iranian *abi-tāpah (Cheung 2007); and the Arabic link is Addi Shir's (AFM p.7) isolated proposal that ubbaha is an Arabization of Persian āb + bahā — a claim no modern Arabic or Persian etymological source accepts (Lisān al-ʿArab, Wiktionary and Mo'in treat ubbaha as native Arabic from the root ʔ-b-h 'notice; be haughty'). So the chain is sound down to ābrū and breaks at node 3; node 4 (Persian obbohat < Arabic ubbaha) is a real Arabic loan but has nothing to do with the water root.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hā́fš",
        "https://en.wiktionary.org/wiki/آب"
      ],
      "ref_check": [
        {
          "ref": "POK:1",
          "status": "supports",
          "note": "POK_01.txt (IEW p.1, leaf 9): 'ab- Wasser, Fluß. Lat. amnis ... air. ab ... cymr. afon ... Vgl. auch 2. ap- Wasser, Fluß'; the Iranian forms stand under 2. ap- p.51 (POK_full.txt 'Root ap-2 (*hap-2) water, river ... Avestan Nom. Sg. āfš, Akk. Sg. āpəm'). Same finding as for pdf p.31; Pokorny is still the standard reference."
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Avestan / Pahlavi",
          "words": "âp",
          "verdict": "confirmed",
          "derivation": "Avestan āp- f. 'water' (nom. sg. āfš, acc. āpəm, gen. pl. apąm) and Old Persian ap- (loc. apiyā, DSf) continue Proto-Iranian *Hā́fš < PIIr. *Hā́ps < PIE *h₂ep- (Skt. āp-/āpaḥ, Hitt. ḫapa- 'river', Lat. amnis < *abnis). Middle Persian āb (Book Pahlavi ʾp̄, Manichaean ʾb; Pāzand āw) shows the Sasanian-era lenition of post-vocalic -p- to -b/-β; the label 'Avestan / Pahlavi' collapses the Old- and Middle-Iranian stages. Identical to node 1 of the Part-1 chart on pdf p.31.",
          "sources": [
            "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hā́fš",
            "https://en.wiktionary.org/wiki/آب"
          ],
          "ref_check": [
            {
              "ref": "KLN:2",
              "status": "supports",
              "note": "KLN_1966.txt line 1142 (p.2, s.v. abdest): 'Pers. āb, water, is rel. to Avestic āp-, OI. āpaḥ (fem. pl.), water; see amnic and cp. the first element in abkari and the second element in doab and in julep.'"
            }
          ]
        },
        {
          "id": 2,
          "lang": "Persian",
          "words": "âb; âberŭ; âftâb",
          "verdict": "disputed",
          "derivation": "(a) āb 2 'lustre, glitter, brilliance' (as of a blade, a gem, a water-surface; hence 'honour'): Horn (Grundriss no. 3) listed it as a separate lemma 'āb Glanz' comparing Skt. ābhā- 'splendour' (ā- + bhā- 'shine'), but in his own footnote judged that comparison 'keineswegs sicher' and observed that from 'glittering water-surface' one very easily reaches 'Glanz'; Wiktionary today simply lists 'honour, reputation, standing' as a sense of āb 'water' (Etymology 1, PIE *h₂ep-), with no separate ābhā-etymology. So the arrow āp 'water' -> āb 'lustre' is the majority view (a semantic extension, no sound change involved): CONFIRMED. (b) ābrū 'honour, reputation', shortened from āb-e rūy 'water (= lustre) of the face', Kurdish avrû, loaned into Urdu/Hindi ābrū, Ottoman âb-ı rû, Azerbaijani abır, Armenian abuṙ; Horn already cited ab[rō under the same lemma: CONFIRMED. (c) āftāb 'sunshine, sun' < MP āftāb (Pahlavi ʾptʾb, Manichaean ʾpdʾb) < Proto-Iranian *abi-tāpah 'shining upon' = preverb abi- (> MP āf-/af-) + tāp- 'to shine, be hot' (Cheung 2007 s.v. tap; Wiktionary). The first element is the preverb, not āb 'water/lustre'; Nourai's gloss 'glitter shine' follows Horn's older grouping (Horn no. 3 lists af[tāb under āb 'Glanz'), which modern Iranian etymology has abandoned: DISPUTED. Worst verdict for the node is therefore 'disputed' (for āftāb only); the Ferdowsi quotation illustrates āb 'lustre/splendour' correctly (jahān gašt bā farr o āyīn o āb).",
          "sources": [
            "https://en.wiktionary.org/wiki/آب",
            "https://en.wiktionary.org/wiki/آبرو",
            "https://en.wiktionary.org/wiki/آفتاب",
            "https://en.wiktionary.org/wiki/आभा"
          ],
          "ref_check": [
            {
              "ref": "HRN:1",
              "status": "supports",
              "note": "HRN.txt leaf 22 (Horn p.1, entry no. 3, OCR lines 464-473): '3. āb Glanz (Šahn. I S. 14 Vers 7), vergl. āb]rō, āb]tāb, āb]mend, Rōd]ābe, Suhr]āb, Mihr]āb, Ardā Vīr]āf, āf[tāb, phlv. āb; skr. ābhā- Glanz' with footnote 2: 'Die Zusammenstellung von np. āb und skr. ābhā- ist keineswegs sicher; von der Bedeutung (glitzernder) Wasserspiegel könnte man sehr leicht zu Glanz kommen' — i.e. Horn lists exactly Nourai's three words (āb 'Glanz', ābrū, āftāb) and himself suggests the 'water' origin Nourai draws; but Horn's inclusion of āftāb is superseded by Cheung's *abi-tāpah."
            },
            {
              "ref": "AEF:2",
              "status": "not_checke
```


## [2026-09-04T15:27:59.162Z] AGENT (thinking)

I'll run parallel lookups: local OCR checks for FVQ, KLN, and LKT entries, targeted grep searches in MON, AHD (verified online since p.152 falls in the main dictionary), and PRT via archive.org's in-book search, plus a check for page images to resolve possible transcription issues.


## [2026-09-04T15:27:59.188Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ leaf 61 (p.44) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==62' FVQ_pages.txt | head -120; echo; echo \"=== FVQ grep Ibrah/Abraham ===\"; grep -n -i 'Ibr.h.m\\|Abrah' FVQ_pages.txt | head -30",
 "description": "Read Jeffery FVQ p.44 (Ibrahim entry)"
}
```


### [2026-09-04T15:28:00.810Z] TOOL RESULT

```
=== FVQ leaf 61 (p.44) ===
44 FOREIGN VOCABULARY OF THE QUR'lN
Burton, Pilgrimage, ii, 175, quotes a Major Price as suggesting
that the word has nothing to do with the birds but is another calamity
in addition, the name being derived from 4x 1 a vesicle. Sprengel
indeed as early as 1794 (see Opitz, Die Medizin im Koran, p. 76), had
suggested a connection of the word with smallpox, deriving it from
^,1 ^father and JA> 1 = lamentation, and stating that the f Persians
^ \^
use the word A^JO I for smallpox. This theory has some support in the
tradition that it was smallpox which destroyed Abrahams army, 1
but it is difficult to see how the word could be of Pers. origin for it
occurs in Pers. only as a borrowing from Arabic, and doubtless from
this passage.
Carra de Vaux, Penseurs, iii, 398, has a suggestion that it is of
Persian origin, and would take the J^y' '- as a s taken reading
for .JA y j = babylonian arrows, which caused the destruction of
the army. The suggestion is ingenious, but hardly convincing, as we
seem to know nothing elsewhere of these JAI y jv.
Apparently the word occurs nowhere in the early literature outside
the Qur'an, unless we admit the genuineness of Umayya's line
5 s S
lj^.JU \jji+* ijXi J>fcj # J^M (W^ a r"' vj*- (Frag. 4,
1. 3, in Schulthess' ed.), where it also means crowds. If it is to be taken
as an Arabic word it may possibly be a case of & U * I A^ j> , especially
in view of the expression quoted from al-Akhfash JAi 1 1 C-4i 1 O*W.
The probability, however, seems in favour of its being of foreign
origin, as Cheikho, Nasrdniya, 471, notes, though its origin is so far
unknown.
/fr*-Jbl J I (Ibrahim).
r* ' *
Occurs some 69 times, cf. ii, 118 ; iii, 30 ; xlii, 11, etc.
Abraham.
1 8cc Sprcnger, Life, 35.

=== FVQ grep Ibrah/Abraham ===
395:the Qur'an, viz. Ibrahim, Mfisa, Daw (id, Sulaiman, Nuh, 'Isa, are well-
845:up under Abraha to destroy the city. It is practically certain that
1477:his beloved son Ibrahim, and the cause of no little scandal and flurry
1951:tradition that it was smallpox which destroyed Abrahams army, 1
1970:/fr*-Jbl J I (Ibrahim).
1973:Abraham.
2285:Azar the father of Abraham.
2291:of Abraham's father, and is "^^ f\- 1* was also wel1 known,
2292:however, that the real name of Abraham's father was 7-jlT or r-jv, e.g.
2297:idol A^ p^\ 9 or an abusive epithet applied by Abraham to his
2313:that Azer was the heathen name of Abraham's father, who only became
2326:fire demon, 2 and in the Persian histories given as the name of Abraham's
2328:name jSI j Jj, given to Abraham in the Persian writings 3 simply means
2334:(he who has sprung from the East) applied to Abraham in the Talmud
2343:of the Abraham story as it came to him, so that instead of his father
2344:fTnri he has given the name of Abraham's faithful servant "1T17 V&.
3398:a Xfl in the Abraha inscription, CIS, iv, No. 541, 11. 66 and 117.FOREIGN VOCABULARY OF THE QUR ? AN 87
3883:The sole occurrence of the Avord is in the story of Abraham pre-
4070:i, 935), and according to the Talmud, Baba bathra, 91 a, Abraham was
4274:the faith of Abraham, and in nine of them there is an added phrase
4286:to the Jews he began to preach a new doctrine about Abraham, 1
4296:path, a right religion, the faith of Abraham, a Hanif " (vi, 162).
4298:religion of Abraham, a Hanif" (ii, 129); "Who hath a better
4300:follows the faith of Abraham as a Hanif " (iv, 124). He calls on the
4305:ii, 129, is very clearly drawn in iii, 60, " Abraham was neither a Jew
4330:case in none of these passages is it associated with Abraham, and there
4375:Margoliouth has noticed, in using the word of Abraham, Muhammad
4377:argued from Rom. iv, 10-12, that Abraham's faith was counted for
4395:influence from the prophecy that Abraham should be the father of many nations, as
7108:Abraham, and Idris are called ^ *X^ } and the Virgin Mary <a^*X^ in
```


## [2026-09-04T15:28:01.156Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN grep ===\"; grep -n '^Abraham,\\|^Abram,\\|^Abner,\\|^Absalom,\\|^Abigail,\\|^Joab,\\|^Abot\\|^ab-,\\|^abba,\\|^Abba\\|^gibbon,\\|^borage,\\|^Abu\\|^abu' KLN_1966.txt | head -40",
 "description": "Grep Klein for the headwords cited on this page"
}
```


### [2026-09-04T15:28:01.208Z] TOOL RESULT

```
=== KLN grep ===
1137:abba,  n.,  title  of  honor.  —  L.,  fr.  Gk.  fr.
1190:Abner,  n.,  masc.  PN.;  in  the  Bible,  commander of  Saul.  —  Heb.  Abhnir,  lit.  ‘my  father  is  light’, fr.  abh,  ‘father’,  and  ner,  ‘light’;  cp.  the  Baby¬
1217:Abraham,  masc.  PN. ;  in  the  Bible,  the  first  of  the patriarchs  and  father  of  the  Hebrew  nation.
1219:Abram,  masc.  PN.;  in  the  Bible,  former  name  of Abraham.  —  Heb.  Abhrdm,  compounded  of abh,  ‘father’,  and  ram,  ‘high,  exalted’,  which  is prop.  part,  of  rum,  ‘to  be  high,  to  be  exalted  . For  the  first  element  see  Aboth  and  cp.  Abra¬ ham.  From  the  second  element  derive  ramd>', ‘height’  (prop.  fem.  part,  of  rum),  romdm,  ‘ex¬ tolling,  praise;  song  of  praise’,  mardm,  ‘height’, tlrumdh,  ‘contribution,  offering  (for  sacred use)’,  lit.  ‘something  lifted  up,  something  sep¬ arated’.  Cp.  Aram.-Syr.  ram,  ‘was  high’,  Arab. rdma  prop,  ‘he  rose',  hence  ‘he  strove  for’,  and, in  Zanzibar  and  Oman,  ‘he  was  able  to’.  Cp. the  second  element  in  Hiram.
1236:Absalom,  masc.  PN. ;  in  the  Bible,  King  David  s son;  fig.  a  favorite  son.  —  Heb.  Abhshaldm,  lit. ‘father  is  peace’,  fr.  abh,  ‘father’,  and  shaldm, ‘peace’.  See  Aboth  and  shalom. abscess,  n„  a  swelling  in  body  tissues  (med.).  — L.  abscessus,  ‘a  going  away,  departure,  abscess  , fr.  abcedere,  ‘to  go  away’,  fr.  abs-,  ab-,  ‘away from,  from’,  and  cedere,  ‘to  go’.  See  ab-  and cede  and  cp.  cease.
1268:abundant,  adj.  —  ME.  fr.  OF.  abundant,  abondant (F.  abondant),  fr.  L.  abundantem,  acc.  of  aban¬ dons,  ‘abounding’,  pres.  part,  of  abunddre.  See abound  and  -ant.
1271:abuse,  n.  —  F.  abus,  fr.  L.  abusus,  fr.  abusus,  pp. of  abuti.  See  prec.  word.
1273:abusive,  adj.  —  F.  abusif  (fern,  abusive ),  fr.  L. abusivus,  fr.  abusus,  pp.  of  abuti.  See  abuse,  v., and  -ive.
1276:Abutilon,  n.,  a  genus  of  plants  of  the  mallow family  (hot.)  —  ModL.,  fr.  Arab,  aubutildn,  a name  coined  by  the  Arab  philosopher  Avicenna (=  Ibn-Sina).
16112:gibbon,  n.,  a  small,  long-armed  ape.  —  F.,  a  name of  Indian  origin  brought  to  Europe  by  the Marquis  Joseph-Frangois  Dupleix  (1697-1763), governor-general  of  the  French  possessions  in India  (1742-54).
20305:Joab,  1)  masc.  PN. ;  2)  in  the  Bible,  the  chief  cap¬ tain  of  David’s  army.  —  Late  L.  Joab,  fr.  Gk. ’lojafi,  fr.  Heb.  Yd'dbh ,  lit.  ‘the  Lord  is  (his) father’.  For  the  first  element  cp.  the  PN’s  Joel, John,  Jonathan,  Joshua,  for  the  second  see Aboth  and  cp.  words  there  referred  to.
```


## [2026-09-04T15:28:03.399Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT leaf 70 (p.44) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==71' LKT.txt | head -80; echo; echo \"=== LKT grep ===\"; grep -n -i 'abū\\|abu \\|būz\\|buz\\|borrag\\|borag\\|gibbon' LKT.txt | head -40",
 "description": "Read Lokotsch p.44 and grep for abū, būzīna, borrago"
}
```


### [2026-09-04T15:28:05.685Z] TOOL RESULT

```
=== LKT leaf 70 (p.44) ===
n';  hieraus  mit  ar. Art.  sp.  adufe  'dass.',  pg.  adufe  'Schellen- trommel', arfi</"fc'8Vo  [Constancio  Dicc26c]. Wie  die  Kastagnette  arabischer  Herkunft. [DE  50.
538.  Ar.  dnfifa:
'Platte',  vulg.  Form  des  kl.  ar.  daffa; hieraus  mit  ar.  Art.  sp.  pg.  adufa  bei einer  Miihle  die  'Platte,  die  man  in  die Mündung  der  Wasserzuleitung  stellt, damit  das  Wasser  nicht  zur  Mühle  ge- langt'.  [DE  48/50.
539.  Ar.  dahän:
'Rauch',  duhän  sariba  'rauchen',  ebenso tk. ;  hieraus  bulg.  serb.  duhan  'Rauch- tabak', poln.  duchan,  klruss.  dochan, Cech.  dohan  'dass.'.
540.  Tk.  düjme:
'Knopf  [vom  Stamme  tok  >  ttij,  tilj 'binden,  befestigen',  s.  hier  Nr.  528] ; hieraus  hul^.dugme  'dass.,  Knoten',  serb. dugme  'Knopf.    [Bern  SlEtWb  233.
541.  Mal.  düjoug:
[Pijn  113]  'Seekuh,  Halicore  Dujong'  im Indischen  Ozean  [über  sie  vgl.  besonders 0.  Finsch,  Der  Dujong.  Zoologisch- ethnologische Skizze  einer  untergehenden Sirene.  Hamburg  1901.  Sammlung  ge- meinverständlicher wissenschaftlicher
Vorträge.  NF  XV,  359],  auch  H.  taber- naculi  im  Roten  Meere,  H.  austrahs  in Australien,  mit  dem  amerikanischen Manati  [nianatee]  verwandt;  hieraus  frz. dugong,  dougong;  dtsch.  Dugong.  [Devic DEt  1U6/107.  MMM  18.  JAOS  XVH, 135/137.
542.  Ar.  dnkkäu:
'Laden';  \k. ebenso  dükjan;  hieraus  rum. dughiana  'Kramladen';  bulg.  dukan 'Laden',  djukjan  'Werkstätte',  serb.  du- can  'Laden,  Werkstatt',  doganja  'Kauf- mannsladen", russ.  duhan  'Schenke, Bude',  duhanscik.  —  Im  westlichen Afrika  und  Spanien  sprach  man  mit Imäla:  dokkin;  hieiaus  mit  ar.  Art.  sp. adoquin  'viereckige  Steinplatte',  meist als  Pflaster  verwandt,  fig.  'Tölpel'  [zu der  Bedeutungswandlung  vgl.  frz.  tete carrie].  [Gorjajew  99.  Bern  SlEtWb 237.    DE  46/47.
543.  Ar.  düläb:
'Wasserrad,  Bewässerungsmaschine' ; hieraus  vielleicht  sp.  alep  'Mühlrad'. [Eguilaz  151.
544.  Pers.  dulbänd:
'Turban'  [aus  pers.  dil  'Herz'  Horn NpEt  S.  127,  Nr.  571  und  band,  Präsens- stamm von  bästän  'binden'  ebenda  S.  50, Nr. 219;  also  'herzentzückend'];  hieraus l  um.^M^pan'Musseline,  Kopftuch  daraus', tulhent  'Brautschleier',  turban  'Turban', bulg.  serb.  turban,  russ.  tjtirban;  afrz. tolleban,  frz.  turban,  it.  twhante,  sp.  pg. torbante  'Turban';  ndl.  tulband,  engl. turban,  dtsch.  Turban.  —  Aus  demselben Grundwort  ist  der  Name  der  Pflanze Tulipa  Gesneriana  entstanden;  i.  J.  1554 sah  sie  der  kaiserliche  Gesandte  BUS- BECK in  Adrianopel  und  nannte  die  weit offen  stehenden  Blumen  nach  ihrer  Ähn- lichkeit mit  dem  tk.-pers.  Worte  für 'Turban'  [die  Perser  und  Türken  nennen die  Tulpe  übrigens  nicht  so,  sondern peTS.lälä,  tk.lale]:  rv\m.  tuliiyan  [=  la- lea],  it.  tulijxino,  frz.  tulipe,  sp.  pg.  tu- lipa, tulipan;  dtsch.  Tulpe,  ndl.  ftclp, engl,  tulip;  russ.  tjul'pan,  öech.  poln. tulipan.  —  Ableitg.  sp.  torbandalo 'Hammerfisch'.  [ML  8974.  MWiD 11.5/116.
545.  Tk.  dutnan:
'Rauch'  [aus  pers.  düd,  düdmän  Horn NpEt  S.  129,  Nr.  579];  hieraus  bulg. poln.  russ.  tunian  'Nebel',  bulg.  fzma 'dass.'.    [Gorjajew  380.
546.  Tk.  düuibelek:
Auch  tiimbelek  'eine  Art  kleiner  Kupfer- trommel in  Halbkugelform'  [Kelekian Kämüs  417b  mit  ."Abbildung];  hieraus rum.  timbelechiü  'Zimbel,  Schallbecken', timbeleg  in.
Tk.  dilmen.]
44
547.  Tk.  dümeu:
'Steuerruder  [aus  it.  timone];  hieraus bulp.  serb.  dumen,  klruss.  denien  'dass.'. [Bern  SlEtWl)  i2öy.
548.  Tk.  dur-:
Durma  subst.  Intiiiiliv  zu  dtirmak  'blei- ben, stehen'  [vom  Stamme  tw  'vorne, oben,  stellen,  stehen'  Vämbery  TklEtWh S.  184,  Nr.  11)711];  hieraus  serb.  durma 'unaufhörlich'  [wohl  vom  negativen  tk. Stamme  dur-ma-  'nicht  stehen'].  [Bern SlEtWb  239.
549.  Ar.  dürawä: 'Getreidesplitter,  Spreu,  die  beim  Worfeln des  Getreides  abstiebenden  Hülsen'; hieraus  Ober  *dräwa,  *dröwa  die  roma- nischen Formen  sp.  it.di-oga,  irz.drogue; engl,  drugs,  dtsch.  Droge.  [Zahlreiche andere  Ableitungen  sind  vor  allem  be- deutungsgeschichthch  unhaltbar,  so  aus pers.  därü  'Arznei'  Horn  NpEt  S.  116, Nr.  523:  pehl.  därük;  aus  lat.  irochiscus, gr.  TpoxiöKO^  'Pille,  Seifenkugel';  aus ndl.  droog  'trocken';  aus  slav.  doi-gz 'teuer'  Bern  SlEtWb  213;  vgl.  vor  allem BAIST  in  ZffrzSpr  XXXII,  298/39 1.| [Kluge  98.  KLUYVER  in  ZfdWf  XI,  7/10. SEYBOLD  in  ZfdWf  X,  218f.  ZfdU  XV, 335.
550.  Mal.  düri:
'Stachel,  Dorn'  [Pijn  112];  hieraus  dü- rlan  'ein  Baum  Ostindiens,  Durio  zibe- thinus  L.',  der  veegen  seiner  melonen- artigen Früchte,  die  eine  mit  Stacheln versehen

=== LKT grep ===
248:'Vater  des  Schweißes',  hieraus  lat.  bor- rago,  eine  Pflanze,  die  durch  die  ar. Medizin  im  Mittelalter  verbreitet  wurde. Die  romanischen  Formen  sind:  it.  bor- race,  borragine,  borrana;  prov.  borrage; sp.  borraja ;  pg.  borragem ;  frz.  hourrache. Auch  germanisch,  z.  B.  engl,  borage, dtsch.  Burrich,  Bor( rjetsch.  Wohl  über das  Ngr.  entstand  rum.  boranjä  'dass.'. Trotz  ML  1412  scheint  diese  Ableitung noch  immer  die  beste  und  wenig  an- fechtbar zu  sein.    [Kluge  64.
789:[Aus  tk.  bas  s.  hier  Nr.  260  und  boznk 'verdorben'  vom  Stamme  bos,  bot  'leer, wüst,  verdorben'  Vämbery  TktEtWb S.  207,  Nr.  222]  'irregulärer  Soldat', wegen  seiner  Plündereien  berüchtigt,  da- her rum.  ba^ibuzuc  'dass.,  Vagabund', dtsch.  Baschibosuk  [MWiD  109],  engl. bashibazouk,  frz.  bachi-bouzwick.
935:Vienne  183S.  S.  130b:  B.  topns] 'Keule'  [wohl  vom  Stamme  6os,  bot 'leer,  wüst,  zerstört.'  Vamböry  TktEtWb S.  '101,  Nr.  ^2-2-1  und  tok,  tog  'empor- kommen, entstehen,  erzeugen'  ebenda S.  18-J,  Nr.  194;  also  wörtlich  'Zerstörung bewirkend'];  hieraus  rum.  buzdugan 'Streitkolben,  Kommandostab',  bulg.  huz- dogan,  serb.  biizdohan  'Keule',  poln. klruss.  buzdt/ga>i,  klruss.  ozdygnn  'Sti  eit- kolben'.  [iMikl  SlEtWb  20a.  Bern SlElWb  105.
1026:'Hirse  MiUum'  aus  der  Familie  der Gramineen,  tk.  hüza,  böza  'eine  Art Hirsenbier'  [über  die  Bestandteile  und Bereitung  s.  Silv.  de  Sacy,  Relation  de l'Egypte  par  Abd-Allatif  S.  572].  Hier- aus rum.  bozan  'eine  Art  Bier';  russ. serb.  cech.  poln.  buza,  bulg.  boza  'dass.'; frz.  hoiiza,  bosan  'tk.  Hirsentrank',  dtsch. Busa;  sp.  ps^.  buza.  [Bern  SlEtWb  104. DE  243/244.  Devic  DEt  70.  ZDMG XVni,  705,  Anm.  2.
1413:5.56.  Tk.  ebnzine: Auch  buzine  'Affe'  [aus  ar.  abü  zina" 'Vater   der   Unzucht'];    hieraus  russ. obez'jana,  klruss.  obezjana  'Affe'  [vgl. lit.  bezdona].
1993:824.  Pers.  härbuz:
1994:"Melone'  [aus  'här  'Esel'  Horn  NpEt S.  104,  Nr.  473  "und  buz  'Ziege'  ebenda S.  49,  Nr.  213,  also  'Eselsziege',  nicht 'Eselsgurke',  wie  Horn  NpEt  S.  105  hat; die  dort  in  Anm.  1)  fehlende  Band-  und Seitenzahl  in  Brugsch,  Reise  der  K. Preuß.  Gesandtschaft  nach  Persien,  ist: Bd.  I,  S.  334/336.  Übrigens  scheint  sich BRUGSCH  die  dort  erzählte  „nicht  sehr geistreiche"  Volksetymologie  des  Wts. nicht  haben  aufbinden  lassen,  da er  sie  selbst  als  eine  „einfältige  Ge- schichte' bezeichnet];  ebenso  Ik.karpiiz [vgl.  ngr.  KapTTOüöia];  hieratis  rum.  car- puz,  carpus  'Melone,  Cucurbita  citrullus', bulg.  serb.  karpuz,  serb.  karpuza,  poln. karbuz,  garbuz,  harbuz,  arbuz,  klruss. garbuz,  russ.  arbuz  'Wassermelone'. [Gorjajew  5.    Bern  SlEtWb  491.
2830:'Eine  Art  Zither  in  Birnenform  mit einer  einzigen,  sehr  dicken  Saite'  [vom Stamme  kob  'anschwellen,  dick  und  rund', s.  hier  Nr.  1203  und  1205] ;  hieraus  rum. cobuz,  cobzä  'Mandoline,  kleine  Schal- mei'; russ.  kobza  'Saiteninstrument  mit acht  Saiten'  (in  Kleinrußland),  klruss. kobza  'dass..  Laute',  kobzar  'Sänger  zur Laute',  poln.  cech.  kobza  'Laute'.  [Gor- jajew  147.    Bern  SlEtWb  534.
4449:197:2.  Polyues.  tabn: 'Unverletzlich';  es  können  für  den  Be- wohner Polynesiens  gottgeweihte  Gegen- stände, Orte,  Personen  sein;  hieraus frz.  tabou,  engl,  taboo  [z.  B.  «  tabooed snbject  of  conrersnfion  'ein  Gesprächs- stoff, an  den  nicht  gerührt  werden  darf], dtsch.  Tabu  [z.  B.  halb  scherzhaft  'das ist  mir  tabu'].
5027:Muhammad  abu  Bakr  ihn  \ I      Zuknrlja  1712 i  Muhammad  ihn  Müsä  631 . 890
5813:JUacheier  1497 Madapolam  1342 Magazin  1362 Maharadscha  1692 Mah-Jong  1338  a Mamluk  1384 Mammon  1386 Mammut  1385 M'indarin  1400 Mandoline  2015 Mandarin  1400 Mango  1393 Mangrove  1394 Manguxte  1395 Manichäer  1397 Jlf«MM«  1398 manna  ahd.  1398 Marabu  1410 Marienkäfer  1417 Markab  St.  1420 Markasit  1374
6016:borage  13
6888:borragine  13
7371:garbuz  824
7425:halascius  151 balsatnum  293 bambagium  1617 Barabbas  220 ftarca  2148 harracanus  250 basilica  (vena)  262 bezoar  1605 birrus  365 bisamutn  293 bombacium  1617 borrago  13 bronzium  1657 brundisinum  Caes)  1657 brunitius  1657 buccina  347 burgns  362 burrus  365
7642:(na)  balykti  208 baragola  145d barakan  250 haran  219 barasnik  258 barasznik  258 barchan  250 bastramy  261 ias^/(/Ä;  260 fcasa;-  278 *     bedew  164 b§dzwim  1332 benzoes  1332 bezestan  280 bezmian  272 biczak  311 hisurman  1516  a ^>o&a^•  181 bohatyr  IIb boraks  356 borsuk  254 borysz(nik)  258 bronz  1657 6mö/v/L-  337 bugaj  339 buhaj  339 bujurdan  346 butany  350 iM?a<  1672 bunczuczny  354 bunczuk  354 &MrÄ;a  221 burnus  365 bursztyn  1004 ftwara  376 buzdygan  333
7648:gabela  974 gajda  643 galgan(t)  795 garbuz  824 gazeta  1059 giaur  632 ^rocÄ  760
7649:Äa6a  2 ;ia;<?a  779 hajdamak  780 liajde(sz)  112 hamal  806 haracz  825 harbuz  824 harem  819 hazuka  1143 ÄMm  2167
7653:kabala  977 kaban  975 Ä;a6a^  971 kaczan  1192 Ä:a(ft  984 fcarfy  984 kafenauz  1005 kaftan  Iii. kaik  1014 kalauz  1276 Ä;a/efca  1040 kaleta  828 Ä;afÄ;aw  1034 kalkun(t)  1031 kamcha  1043 kamfora  1100 katnlot  653 kanczug  1042 kanczuk  1042 kanfora  1100 kaparki  978 kapary  978 kapinaz  1005 kapkan  1064 karabacz  1279 karaczan  2027 karafka  689 karawana  1075 karbacz  1279 karhona  1208 karbuz  824 karczma(rz)  825 karczoch  833 kardasz  1089 fcary  1070 Ä:a<MM  1272 ÄsttM^a  1005 kawak  1134 kawiar  851 kawon  1138 kazan  1144 kazna  855 kazmirek  1116
8088:borragem  13
8542:borrage  13
8692:buduhald  338 budulac  338 budnla^  338 buhaiü  339 buhur(dan)  342 buhurgiü  343 bulgär(e)  352 bulgäriü  351 bulgur  352 buluba§a  353 5m?mc  330 bumbac  1617 bunduc  355 burghiü  363 bursuc  254 burungiuc  367 but(urä)  372 buturo§  372 buturugä  372 buzdugati  333
9385:buzdohan  333
```


## [2026-09-04T15:28:05.750Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON grep بوزینه ===\"; grep -n 'بوزینه\\|بوزنه' MON_part1.txt | head -20; echo \"=== MON grep ابو ===\"; grep -n '^ابو\\|^اب ' MON_part1.txt | head -20; echo \"=== AHD 1985 grep borage ===\"; grep -n -i 'borage\\|borrago' AHD_watkins1985.txt | head",
 "description": "Grep Mo'in abridgement and AHD roots for buzineh, abu, borage"
}
```


### [2026-09-04T15:28:05.840Z] TOOL RESULT

```
=== MON grep بوزینه ===
26095:بورینه: (6-)۱1212 [- بوزینا - بوزنه - 
26100:بوزنه: (م-)هم002 (۱.) شکو فه و هار درخت 
82874:میمون» بوزینه. 
=== MON grep ابو ===
79:ابوالقاسم. در شهر رشت در خانواده‌ای روحانی متولد گردید. به هنگام طفولیت 
748:اب 0 (1.) مایعی است شفاف» بی‌طعم و 
762:اب 
1059:اب بسسته: (۵)هادهه 2.6 (امر.) شیشه؛ 
1077:اب بینی: 101 2-.2 (امر.) آب غلظ که از 
1085:اب پاش: *05-.2 (امر.) آلتی آهنی یا حلبی 
1088:اب نظارت دارد. 
1102:اب پز: 2-.3 (ص مر .) آنجه که دز آب 
1131:اب جو: (10۷-) 12۷ 0-.2 (امر.) آبی که در 
1143:اب جوش: 2-155 (امر.) آبی که در حال 
1160:اب چشم: («3)63 2.۰ (امر.) اشکک» 
1211:اب خفته: (0-)70112 20-6 (امر .) آب را کد» 
1257:اب دادن: :50-1542 (مصم.) اعطای آن به 
1310:اب دست: اعدل 20-6 راعحث-20 (امر.) آبی 
1360:اب دهان: عقدمه ععطة (امر.) (یز.) آبی 
1365:اب دهن). 
1376:اب دیبده: (0-)0142 50-6 (امر.) اشکده 
1389:اب رز؛ 30-672 (امر.) شراب باده» می. 
1420:اب روی. اعتبار» قدر» جاه» شرف عرض.» 
1496:اب زییو: 20-0 (امر.) (عم.) چیز رقیق و 
=== AHD 1985 grep borage ===
```


## [2026-09-04T15:28:07.980Z] TOOL CALL #13: Bash

```json
{
 "command": "ls data/ ; ls data/* | head -40; find . -iname '*page*33*' -not -path './data/extracted/*' -not -path './data/verification/*' | head",
 "description": "Look for page images or PDF of the book in the repo"
}
```


### [2026-09-04T15:28:08.140Z] TOOL RESULT

```
ANOMALIES.md
extracted
EXTRACTION_SPEC.md
research
translations
verification
data/ANOMALIES.md
data/EXTRACTION_SPEC.md

data/extracted:
batch
NEXT_CHUNK
RETRY.txt
test

data/research:
domains.json
ganjoor.json
research.json

data/translations:
fa.json

data/verification:
page-101.json
page-126.json
page-311.json
page-31.json
page-32.json
page-345.json
process
sources
```


## [2026-09-04T15:28:11.188Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -s 'https://archive.org/metadata/originsshortetym00part' | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nprint(d.get('server'), d.get('dir'))\nfor f in d.get('files',[]):\n    if f['name'].endswith('.djvu') or 'djvu' in f['name'] or f['name'].endswith('_abbyy.gz') or f['name'].endswith('.xml'): print(f['name'])\n\" 2>&1 | head -20",
 "description": "Get archive.org server/dir for Partridge in-book search"
}
```


### [2026-09-04T15:28:13.759Z] TOOL RESULT

```
ia800104.us.archive.org /5/items/originsshortetym00part
originsshortetym00part_abbyy.gz
originsshortetym00part_dc.xml
originsshortetym00part_djvu.txt
originsshortetym00part_djvu.xml
originsshortetym00part_files.xml
originsshortetym00part_marc.xml
originsshortetym00part_meta.xml
originsshortetym00part_metasource.xml
originsshortetym00part_scandata.xml
```


## [2026-09-04T15:28:35.014Z] AGENT (thinking)

I'll next read the FVQ Ibrāhīm continuation, the full Klein entries, and the LKT leaves for "borrago" and "ebuzine," check the Mo'in būzīna context, and try archive.org's in-book search for Partridge's "gibbon" entry, along with loading WebFetch/WebSearch for modern sources—all independently.


## [2026-09-04T15:28:35.018Z] TOOL CALL #15: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T15:28:35.024Z] TOOL RESULT

```


```


## [2026-09-04T15:28:35.393Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ leaf 62 (p.45) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==63' FVQ_pages.txt | head -70",
 "description": "Read Jeffery FVQ p.45 (Ibrahim entry continued)"
}
```


### [2026-09-04T15:28:36.840Z] TOOL RESULT

```
=== FVQ leaf 62 (p.45) ===
FOREIGN VOCABULARY OF THE QUB'AN 45
It is always used of the Biblical Patriarch and thus is ultimately
derived from Heb. QmSX. If the name had come direct from the
Heb. we should have expected the form *U^ I, and as a matter of
fact the Muslim philologers themselves recognized that the Qur'anic
form was not satisfactory, for we hear of attempts to alter the form, 1
and an-N,wawI, Taklhlb, 126, gives variant forms *Uj;i ; (%*' J*J 5
and pjtl j\. Moreover we learn from as-Suyutl, Muzhir,
i, 138, and al-Jawallql, 8, that some early authorities recognized it as a
foreign borrowing, al-Marwardi, indeed, informing us that in Syriac
it means /%A>-jiJ (Nawawl, 127), which is not far from the Rabbinic
derivations.
The form p*A\ J\ cannot be evidenced earlier than the Qur'an,
for the verses of Umayya (ed. Schulthess, xxix, 9), in which it occurs,
are not genuine, and Horovitz, KU, 86, 87, rightly doubts the authen-
ticity of the occurrences of the name in the Uxd al-(!hdba and such
works. The form would thus seem to be due to Muhammad himself,
but the immediate source is not easy to determine. The common
Syr. form is ^Sooi-jDJ which is obviously the source of both the Eth.
JMICyjF 1 and the Arm. |J ^mi^mir 2 A marginal reading in Luke i, 55,
in the Palestinian Syriac Lectionary of the Gospels reads J>QjiOl^ul,
but Schulthoss, Lex, 2, rightly takes this as due to a scribe who was
familiar with the Arabic. 3
Lidzbarski, Johanwsbuch, 73, 4 compares the Mandacan DTIX12,
which shortened form is also found as iDOlja[j] in the Christian
Palestinian version of Luke xiii, 16 (Schulthess, Lex, 2), and may be
compared with the +\*J, mentioned in Ibn Hisham, 352, 1. 18, and
the Brahain b. Buriaj whom Horovitz, AT/, 87, quotes from the Safii
inscriptions. The final vowel, however, is missing here. Brockelmann,
1 Sprenger, Leben, i, 06; Sycz, Eigetinamen, 21 ; Margoliouth in MW, xv, 342.
2 Hubschmann, Arm. Gramm, i, 290.
3 The forms *lQjkC7l]^] and SO^O1^1 found in Bar Hebraeus are also
probably of Arabic origin.
4 See also Ephemerw, ii, 44, n. 1.
```


## [2026-09-04T15:28:39.988Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '^Aboth\\|^Abigail\\|^Abba\\|^abbot,\\|^borage' KLN_1966.txt | head; echo ---; sed -n '1187,1192p;1215,1220p' KLN_1966.txt | cut -c1-1500; echo \"--- leaf index of line 1190 and 16112:\"; awk 'BEGIN{RS=\"\\f\"} {n+=gsub(/\\n/,\"\\n\"); if(n>=1190 && !a){print \"line1190 leaf\", NR-1; a=1} if(n>=16112 && !b){print \"line16112 leaf\", NR-1; b=1}}' KLN_1966.txt; sed -n '16112,16113p' KLN_1966.txt | cut -c1-800; grep -n -i 'borage' KLN_1966.txt | head -5",
 "description": "Read Klein entries for Aboth, Abraham, Abigail, gibbon, borage and find their leaves"
}
```


### [2026-09-04T15:28:41.639Z] TOOL RESULT

```
---
alb.
ablution,  n.,  a  washing,  esp.  as  a  ritual.  —  L.  ab- lutio,  gen.  -onis,  ‘a  washing,  cleansing’,  fr.  ab- lutus,  pp.  of  abluere,  ‘to  wash  off’,  fr.  ab-  and luere,  ‘to  wash’,  which  is  rel.  to  lavare,  ‘to  wash’. See  lave  and  -ion.
Derivative:  ablution-ary ,  adj. abnegate,  tr.  v.,  to  deny,  give  up.  —  L.  abnegdtus, pp.  of  abnegare,  ‘to  refuse,  deny’,  fr.  ab-  and negare,  ‘to  say  no,  deny’.  See  negate, abnegation,  n.  —  L.  abnegatio,  gen.  -onis,  ‘re¬ fusal,  denial’,  fr.  L.  abnegdtus,  pp.  of  abnegare. See  prec.  word  and  negation.
Abner,  n.,  masc.  PN.;  in  the  Bible,  commander of  Saul.  —  Heb.  Abhnir,  lit.  ‘my  father  is  light’, fr.  abh,  ‘father’,  and  ner,  ‘light’;  cp.  the  Baby¬
lonian  PN.  Abunuri.  For  the  first  element  see Aboth,  for  the  second  see  Menorah. abnormal,  adj.  — ■  A  blend  of  L.  abnormis  and ML.  anormalis,  this  latter  itself  being  a  blend of  L.  anomalus  and  normalis.  See  anomalous  and norm  and  cp.  anormal.
Derivatives:  abnormal-ity,  n.,  abnormal-ly,  adv., abnormal-ness,  n.
above,  adv.  —  ME.  aboven,  fr.  OE.  abufan,  form¬ ed  fr.  a-,  ‘on’,  and  bufan,  ‘above’,  which  itself is  formed  fr.  be,  ‘by’  (see  by),  and  ufan,  ‘up¬ ward,  above’;  cp.  OE.  ofer,  ‘over’  which  is  the compar.  of  ufan,  and  see  over.  Cp.  also  about. Derivatives:  above,  prep,  and  adj. abracadabra,  n.,  a  magic  formula.  —  Late  L.,  fr. Gk.  dppao48oc(ipa,  in  which  word  the  letter  c  = s  was  misread  for  k.  It  was  originally  written as  a  magic  formula  on  Abraxas  Stones,  whence its  name.  See  abraxas.
abrade,  tr.  v.,  to  scrape  off.  —  L.  abradere,  ‘to scrape  off’,  fr.  ab-,  and  ruder e,  ‘to  scrape  off, to  shave’.  See  raze  and  cp.  abrase.
Abraham,  masc.  PN. ;  in  the  Bible,  the  first  of  the patriarchs  and  father  of  the  Hebrew  nation.
Heb.  Abhrahdm,  lit.  ‘father  of  the  multitude’, compounded  of  abh,  ‘father’,  and  *rahdm, ‘multitude’,  which  is  rel.  to  Arab,  ruhdm,  of s.m. ;  see  Gen.  17:5*  See  A  both  and  cp.  next word.
Abram,  masc.  PN.;  in  the  Bible,  former  name  of Abraham.  —  Heb.  Abhrdm,  compounded  of abh,  ‘father’,  and  ram,  ‘high,  exalted’,  which  is prop.  part,  of  rum,  ‘to  be  high,  to  be  exalted  . For  the  first  element  see  Aboth  and  cp.  Abra¬ ham.  From  the  second  element  derive  ramd>', ‘height’  (prop.  fem.  part,  of  rum),  romdm,  ‘ex¬ tolling,  praise;  song  of  praise’,  mardm,  ‘height’, tlrumdh,  ‘contribution,  offering  (for  sacred use)’,  lit.  ‘something  lifted  up,  something  sep¬ arated’.  Cp.  Aram.-Syr.  ram,  ‘was  high’,  Arab. rdma  prop,  ‘he  rose',  hence  ‘he  strove  for’,  and, in  Zanzibar  and  Oman,  ‘he  was  able  to’.  Cp. the  second  element  in  Hiram.
Abramis,  n.,  a  genus  of  fishes  ( ichthyol .) — ModL., fr.  Gk.  dppapit?,  ‘bream’,  fr.  Egyptian  rem, ‘fish’.
--- leaf index of line 1190 and 16112:
line1190 leaf 14
line16112 leaf 354
gibbon,  n.,  a  small,  long-armed  ape.  —  F.,  a  name of  Indian  origin  brought  to  Europe  by  the Marquis  Joseph-Frangois  Dupleix  (1697-1763), governor-general  of  the  French  possessions  in India  (1742-54).
gibbose,  adj.,  gibbous.  —  See  gibbous, gibbosity,  n.  —  F.  gibbosite.  See  next  word  and -ity.
1209:Derivatives:  abortion-al,  adj.,  abortion-ist ,  n. abortive,  adj.,  I)  born  prematurely;  2)  unsuccess¬ ful.  —  L.  abortivus,  ‘pertaining  to  miscarriage’, fr.  abortus,  pp.  of  aboriri.  See  abort,  v.,  and  -ive. Derivatives:  abortive-ly,  adj.,  abortive-ness,  n. Aboth,  also  Abot,n.,  i)the  Mishnah  treatise  also called  Pirke  Aboth  or  The  Ethics  of  the  Fathers  ', 2)  name  of  the  first  benediction  of  the  Shemoneh Esreh  ( Jewish  liturgy).  —  Heb.  Abhdth,  pi.  of abh,  ‘father’,  rel.  to  Aram,  abh  (absolute  state), abbd  (emphatic  state),  Ugar.  ’b,  Arab,  ab, Ethiop.  ab,  ‘father’ ;  of  uncertain  origin,  possibly traceable  to  *ab(a),  a  child’s  word  for  father. Cp.  the  first  element  in  Abraham,  Abner,  Absa¬ lom,  Abigail,  and  the  second  element  in  Joab, Moab,  Barabbas.  Cp.  also  abbot  and  words there  referred  to.  Cp.  also  borage, abound,  intr.  v.  —  ME.  abounden,  fr.  OF,  (=  F.) abonder,  fr.  L.  abundare,  ‘to  overflow;  to  a- bound’,  fr.  ab-  and  unda,  ‘wave’.  See  undate  and cp.  redound,  surround.  Derivatives:  abound-er, n.,  abound-ing,  adj.,  abound-ing-ly,  adv. about,  adv.  —  ME.  abuten,  abouten,  about e,  fr. OE.  abutan,  onbutan,  ‘on  the  outside  of’,  formed fr.  a-,  ‘on’,  and  butan,  ‘outside’,  which  itself  is formed  fr.  be,  ‘by’,  and  iitan,  ‘outside’,  fr.  ut, ‘out’.  See  by  and  out  and  cp.  but.
2234:Alkanna,  n.,  a  genus  of  plants  of  the  borage family  (bot.)  —  ModL.,  fr.  Sp.  alcana,  fr.  Arab. al-hinnd',  fr.  al-,  ‘the’,  and  hinnd',  ‘henna’.  See henna.
2693:Anchusa,  n.,  a  genus  of  plants  of  the  borage  fa¬ mily.  —  L.  anchusa ,  fr.  Gk.  avy/jorca,  ‘alkanet’, which  is  of  uncertain  origin, anchylose,  n.  —  See  ankylose. anchylosis,  n.  —  See  ankylosis, anchylotic,  adj.  — -  See  ankylotic. ancient,  adj.,  old.  —  F.  ancien,  fr.  VL.  *antianus, ‘former’,  fr.  ante,  ‘before’ ;  see  ante-.  The  -t  in ancient  is  excrescent  and  is  due  to  a  confusion of  the  ending  of  F.  ancien  with  -ent,  the  English equivalent  of  L.  -ens  (gen.  -entis),  the  pres.  part, sulf.  of  the  II-IV.  Latin  conjugations.  Cp.  pag¬ eant,  peasant,  pheasant,  tyrant.
3484:Amebia,  n.,  a  genus  of  plants  of  the  borage family  (bot.) — Arab,  arnabtya *,  name  of  a  plant, lit.  ‘hare  plant’,  fr.  drnab,  ‘hare’,  which  is  rel. to  Heb.  arnebheth,  Arm.  arnabhtd,  Syr.  ar- nlbhA,  Ugar.  'nhb.  Akkad,  annabu,  ‘hare’.
3492:Derivatives:  arous-al,  n.,  arous-er,  n. a  rovescio,  a  musical  direction  indicating  imita¬ tion  by  contrary  motion.  —  It.,  lit.  ‘upside down’,  fr.  a  (fr.  L.  ad),  ‘to’,  and  rovescio,  ‘re¬ verse,  wrong  side’,  fr.  L.  reversus,  ‘turned  back’, pp.  of  revertere.  See  ad-  and  revert, arpeggio,  n.,  the  playing  of  the  notes  of  a  chord in  rapid  succession  instead  of  simultaneously; a  chord  on  which  the  notes  are  so  played (mus.)  —  It.,  fr.  arpeggiare,  ‘to  play  upon  the harp',  fr.  arpa,  ‘harp’.  See  harp, arpent,  n.,  an  old  French  land  measure.  —  F., fr.  VL.  *arependis,  alteration  of  L.  arepennis, a  Gaulish  word  of  uncertain  origin, arquebus,  n.  —  See  harquebus, arrack,  in  the  East,  a  strong  alcoholic  drink  made from  rice  or  molasses.  —  Fr.  Arab,  ‘araq,  ‘sweat, juice  of  fruit’.  Cp.  rack,  ‘arrack’,  and  borage, arraign,  tr.  v.,  to  call  to  account;  to  bring  before a  law  court.  —  ME.  areinen,  fr.  AF.  areiner, fr.  OF.  araisnier,  aresnier  (F.  arraisonner),  fr. VL.  *arrationare,  fr.  ad-  and  *rationdre,  ‘to reason’,  fr.  L.  ratio,  ‘reckoning,  calculation; reason’.  See  reason  and  cp.  deraign. Derivatives:  arraign,  n.,  arraign-er,  n.,  arraign¬ ment  (q.v.)
```


## [2026-09-04T15:28:42.141Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n+=gsub(/\\n/,\"\\n\"); if(n>=248 && !a){print \"line248 leaf\", NR-1; a=1} if(n>=1413 && !b){print \"line1413 leaf\", NR-1; b=1}}' LKT.txt; echo \"--- borrago entry:\"; sed -n '244,249p' LKT.txt | cut -c1-600; echo \"--- ebuzine entry:\"; sed -n '1411,1416p' LKT.txt | cut -c1-600",
 "description": "Locate Lokotsch entries for borrago and ebuzine with their leaves"
}
```


## [2026-09-04T15:28:43.660Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26092,26102p' MON_part1.txt; echo ---; sed -n '82870,82876p' MON_part1.txt",
 "description": "Read Mo'in abridgement entries around buzineh"
}
```


### [2026-09-04T15:28:43.678Z] TOOL RESULT

```
line248 leaf 28
line1413 leaf 71
--- borrago entry:
[Wörtlich  „Vater  der  Zecken",  die  ar. kiräd,  plr.  kirdän  heißen].  Der  rein weifae  'Kuhreiher',  Ardea  bubuleus  Sa- vigny,  ein  afrikanischer  Vogel  [die Schreibung  aboogerdan  bei  ML  36  wie schon  vorher  bei  Körting,  Lateinisch- romanisches Wörterbuch.  3.  Aufl.  Pader- born 1907,  s.  V.  ist  englisch].  Durch volksetymologische  Neugestaltung  hier- aus vielleicht  frz.  bwuf-garde,  garde- bcfuf  'eine  Art  Silberreiher'.  [FASS in  RomForsch  III,  488.  KURYLOWICZ in  Rocznik  Orientalistyczny.  Tom  II. Lwöw  1925.    S.  252.
12.  Ar.  'abar:
In  der  Zusammensetzung  as-sirä  al- "abiir  'der  [sc.  auf  der  Milchstraße] wandernde  Sirius'  [hierzu  s.  hier  Nr.  1915] vom  ar.  Stamme  'fcr  'wandern'  [vgl. hebr.  "ibrl  'Hebräer',  d.  h.  derjenige,  der gewandert  ist  od.  überschritten  hat  sc. den  Euphrat  od.  Jordan].  Hieraus  Alha- bor,  Alchabar  als  Name  des  Sirius  a Ganis  majoris.  [Devic  DEt  40/41. Ideler  Sternn  237  und  246.
13.  Ar.  abü  rag':
'Vater  des  Schweißes',  hieraus  lat.  bor- rago,  eine  Pflanze,  die  durch  die  ar. Medizin  im  Mittelalter  verbreitet  wurde. Die  romanischen  Formen  sind:  it.  bor- race,  borragine,  borrana;  prov.  borrage; sp.  borraja ;  pg.  borragem ;  frz.  hourrache. Auch  germanisch,  z.  B.  engl,  borage, dtsch.  Burrich,  Bor( rjetsch.  Wohl  über das  Ngr.  entstand  rum.  boranjä  'dass.'. Trotz  ML  1412  scheint  diese  Ableitung noch  immer  die  beste  und  wenig  an- fechtbar zu  sein.    [Kluge  64.
14.  Ar.  abü  tilün:
--- ebuzine entry:
.554.  Pers.  dnsmäu: 'Feind'  [aus  dui,  dus  'übel,  böse'  Horn NpEt  S.  126,  Nr.  565  und  män(is)  ebenda S.  222,  Nr.  992],  ebenso  tk.  dähnen; hieraus  rum.  du§man  'dass.',  Ableitung du^mancä,  du^mänie,  du^manesc;  bulg. dusman,  dusmanin,  serb.  dusman,  dus- manin  'Feind',  klruss.  dusman  'Wüiger, Tyrann'.    [Bern  SlElWb  239.
555.  Tk.  düweiek: 'Kleine,  noch  grüne  Melone  oder  andere Frucht'  [Kelekian  Kämüs  591  b];  hieraus rum.  dovleac  'Kürbis',  doviecel  'VValzen- kürbis'.
5.56.  Tk.  ebnzine: Auch  buzine  'Affe'  [aus  ar.  abü  zina" 'Vater   der   Unzucht'];    hieraus  russ. obez'jana,  klruss.  obezjana  'Affe'  [vgl. lit.  bezdona].
557.  Tk.  efendi:
[Aus  gl-,  aiiöevxrii;  'Herr',  s.  Glotta  III, 289 ff.,  moderne  Aussprache  aftendis, und  zwar  Vokativ  auö^vxri  afMdi  MSOS I,  44,  Anm.  2];  früher  Ehrentitel  [s.  hier Nr.  28],  jetzt  entsprechend  unserer  höf- lichen Anrede  „mein  Herr,  monsieur". Frz.  efendi,  effendi,  dtsch.  Effendi  usw. [MWilJ  107.
558.  Mal.  egung :
```


### [2026-09-04T15:28:43.745Z] TOOL RESULT

```
بوزه: (-)۳۳22 (.) شرابی که از آرد برنج و 
ارزن و جو سازند. 

بورینه: (6-)۱1212 [- بوزینا - بوزنه - 
بوزنینه ] (.) (جاذ.) میمون. 

بوژ: (02۳2)00۷ (.) گرداب. 

بوزنه: (م-)هم002 (۱.) شکو فه و هار درخت 
که هنوز نشگفته باشدء کم. 

---
شادمانی» مسرت. به سلامتی (به هنگام 
نوشیدن باده به یاد عزیزی یا دوستی گویند). 
(احح, نت.) فرح. شادی ستاره: (ا<. نح.) 
فرح کوکب (مقدمه التفهیم ص قسط). (ا.) 
میمون» بوزینه. 

شادیانه: (م»)د«-01: (امر.) آنچه که از
```


## [2026-09-04T15:28:45.306Z] TOOL CALL #20: Bash

```json
{
 "command": "curl -sG 'https://ia800104.us.archive.org/fulltext/inside.php' --data-urlencode 'item_id=originsshortetym00part' --data-urlencode 'doc=originsshortetym00part' --data-urlencode 'path=/5/items/originsshortetym00part' --data-urlencode 'q=gibbon' | head -c 3000",
 "description": "Search Partridge Origins on archive.org for 'gibbon'"
}
```


### [2026-09-04T15:28:47.289Z] TOOL RESULT

```
<!DOCTYPE html>
<html lang="en">
<!-- __ _ _ _ __| |_ (_)__ _____
    / _` | '_/ _| ' \| |\ V / -_)
    \__,_|_| \__|_||_|_| \_/\___| -->
  <head>
    <title>Item not available</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link href="/about/css/ia.css?v=1" rel="stylesheet" type="text/css"/>
    <link rel="SHORTCUT ICON" href="https://archive.org/images/glogo.jpg"/>
  </head>
  <body class="navia">
    <a href="#maincontent" class="hidden-for-screen-readers">Skip to main content</a>

    <!-- Wraps all page content -->
    <div id="wrap">
      <div id="navwrap1">
        <div id="navwrap2">
          <div class="navbar navbar-inverse navbar-static-top1" role="navigation">
            <ul class="nav navbar-nav navbar-main">
              <li class="pull-left">
                <a title="Home" class="navia-link home" href="https://archive.org/" target="_top">
                  <span class="iconochive-logo"></span>
                  <span><img src="https://archive.org/images/wordmark-stacked.svg" alt="IA wordmark-stacked-logo" height="30px" style="margin-left: 10px;"/></span>
                </a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
                <a title="Web" class="navia-link web"  href="https://web.archive.org" target="_top"><span class="iconochive-web" aria-hidden="true"></span><span>Web</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
                <a title="Books" class="navia-link books"  href="https://archive.org/details/books" target="_top"><span class="iconochive-books" aria-hidden="true"></span><span>Books</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
                <a title="Video" class="navia-link movies"  href="https://archive.org/details/movies" target="_top"><span class="iconochive-movies" aria-hidden="true"></span><span>Video</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
                <a title="Audio" class="navia-link audio"  href="https://archive.org/details/audio" target="_top"><span class="iconochive-audio" aria-hidden="true"></span><span>Audio</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-left">
                <a title="Software" class="navia-link software"  href="https://archive.org/details/software" target="_top"><span class="iconochive-software" aria-hidden="true"></span><span>Software</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-left rightmost">
                <a title="Images" class="navia-link images"  href="https://archive.org/details/image" target="_top"><span class="iconochive-images" aria-hidden="true"></span><span>Images</span></a>
              </li>
              <li class="dropdown dropdown-ia pull-right leftmost">
                <a class="nav-upload" href="https://archive.org/create" _target="top" data-event-click-tracking="
```


## [2026-09-04T15:29:14.244Z] AGENT (thinking)

I still need Klein's borage entry and gibbon page, another attempt at Partridge via BookReader, and a batch of modern sources (Wiktionary, Etymonline, AHD, Platts) covering roots and words like borage, gibbon, and the "ab" names. I'll request all of these together now.


## [2026-09-04T15:29:14.278Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'borage,  n\\|borage, n' KLN_1966.txt | head -3 | cut -c1-900; echo \"--- leaf 354 head:\"; awk 'BEGIN{RS=\"\\f\"} NR==355' KLN_1966.txt | head -5 | cut -c1-200; echo \"--- leaf 14 head:\"; awk 'BEGIN{RS=\"\\f\"} NR==15' KLN_1966.txt | head -3 | cut -c1-200",
 "description": "Read Klein borage entry and page headers of the gibbon and Abraham leaves"
}
```


## [2026-09-04T15:29:14.322Z] TOOL CALL #22: Bash

```json
{
 "command": "curl -sG 'https://ia800104.us.archive.org/BookReader/BookReaderSearch.php' --data-urlencode 'item_id=originsshortetym00part' --data-urlencode 'doc=originsshortetym00part' --data-urlencode 'path=/5/items/originsshortetym00part' --data-urlencode 'q=gibbon' | head -c 2500",
 "description": "Try archive.org BookReader search for 'gibbon' in Partridge"
}
```


## [2026-09-04T15:29:15.286Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/ʔab-",
 "prompt": "Give the reconstruction, gloss, notes on origin (nursery word?), and the full list of descendants (Akkadian, Arabic, Hebrew, Aramaic, Ugaritic, Ethiopic, etc.) with their forms."
}
```


### [2026-09-04T15:29:15.897Z] TOOL RESULT

```
5360:Borachio,  n.,  name  of  a  drunkard  in  Shakespeare’s Much  Ado  About  Nothing.  —  Sp.  borracho, 'drunk,  intoxicated’,  fr.  L.  burrus,  ‘red’  (see burro);  so  called  in  allusion  to  the  red  com¬ plexion  of  intoxicated  people, boracic,  adj.,  boric.  —  See  borax  and  -ie. borage,  n.,  a  blue-flowered  plant  used  in  salads. —  ME.,  fr.  OF.  borrace  (cp.  its  variant  burage and  F.  bourrache),  fr.  ML.  borrago,  ult.  fr. Arab,  abu  ‘ arak ,  lit.  ‘father  of  sweat’,  so  called by  the  Arab  physicians  because  of  its  sudorific effect.  See  abbot  andc  p.  arrack, boraginaceous,  adj.  —  Formed  with  suff.  -aceous fr.  ML.  borrago,  gen.  borrdginis.  See  prec.  word, borate,  n.,  salt  of  boric  acid  ( chem .)  —  See  boron and  chem.  suff.  -ate.
--- leaf 354 head:
 by  the English  poet  William  Wordsworth  (1770-1850). giant,  n.  —  ME.  geant,  fr.  OF.  geant  (F.  geant), fr.  earlier  jaiant,  fr.  VL.  *gagantem,  acc.  of *gagas,  assimilated  vr.  L
Derivatives:  giant,  adj.,  giant-ess,  n.,  giantism (q.v.),  giant-like,  adj.
giantism,  n.,  pathological  condition  characterized by  abnormal  tallness  (med.)  —  A  hybrid  formed from  prec.  word  with  -ism,  a  suff.  of  Greek  ori¬ gin.  The  correct  form  is  g
gib,  n.,  a  tomcat.  —  From  Gib,  pet  form  of  the name  Gilbert.
gib,  n.,  a  hook.  —  Of  uncertain  origin, gibbar,  n.,  a  finback  whale  ( obsol .)  —  F.,  fr.  Arab. jabbdr,  ‘giant,  tyrant’,  which  is  rel.  to  Heb.  gibbdr, ‘strong,  mighty
--- leaf 14 head:
nt,  efficient,  elicit,  exhibit,  Illicium,  inci¬ dent,  incipient,  inhibit,  inimical,  institute,  insipid, insipient,  irritate,  ‘to  make  null  and  void’,  navi¬ gate,  obstinate,  Oc
-ability,  subst.  suff.  expressing  ability,  capacity, fitnrss.  —  L.  -abilitas,  forming  nouns  from  ad¬ jectives  ending  in  -abilis.  See  -able  and  -ity  and cp.  -ibility.
abh>-,  combining  form  meaning  ‘without  life’.  — Fr.  Gk.  Sffioi;,  ‘without  life’,  fr.  a-  (see  priv. pref.  a-)  and  (JIo?,  ‘life’.  See  bio-, abiogenesis,  n.  supposed
```


## [2026-09-04T15:29:17.600Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/أب",
 "prompt": "For the Arabic section: etymology (Proto-Semitic root), forms (ab, abū construct, root ʔ-b-w), meaning, and any note on kunya usage 'abū X'. Also list any descendants/borrowings into Persian, Turkish, etc."
}
```


### [2026-09-04T15:29:18.314Z] TOOL RESULT

```
<html>
<head><title>404 Not Found</title></head>
<body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx/1.31.3</center>
</body>
</html>
```


## [2026-09-04T15:29:20.042Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/אב",
 "prompt": "For the Hebrew section: etymology (Proto-Semitic), forms (ʾāḇ, construct ʾăḇī, plural ʾāḇōṯ), meaning, and derived terms / names (Abraham, Abram, Abner, Absalom, Abigail, Joab, Pirkei Avot)."
}
```


## [2026-09-04T15:29:22.282Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/بوزینه",
 "prompt": "Give the full etymology section for Persian بوزینه (buzina, 'monkey'), including any Middle Persian or Arabic origin claimed (e.g. Arabic abū zinā/ abū zanna), the cited references (Hasandust, Mo'in, etc.), alternative forms (بوزنه), and descendants/borrowings into Turkish, Russian, Urdu, Hindi etc."
}
```


## [2026-09-04T15:29:23.800Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/gibbon",
 "prompt": "Give the full etymology of English 'gibbon' (French origin, any Indian-language source suggested, Dupleix/Buffon, first attestation date), and the French etymology section if present."
}
```


## [2026-09-04T15:29:24.540Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/gibbon",
 "prompt": "Give the full etymology text for 'gibbon'."
}
```


## [2026-09-04T15:29:26.130Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/borage",
 "prompt": "Give the full etymology of English 'borage' including Middle English, Old French, Medieval Latin forms, and the proposed Arabic origin (abū ʿaraq 'father of sweat') vs alternatives (Latin burra), and any dates."
}
```


### [2026-09-04T15:29:26.307Z] TOOL RESULT

```
# Proto-Semitic *ʔabw- (Father)

## Reconstruction
**\*ʔabw-** (masculine noun)

## Gloss
"father"

## Origin Notes
The term derives from Proto-Afroasiatic *ʔab- and is "ultimately an onomatopoeic nursery word." This reflects the universal tendency of languages to use simple, repetitive sounds for parental terms.

## Descendants

**East Semitic:**
- Akkadian: abum

**West Semitic:**
- Arabic: ʔab
- Maltese: bu
- Aramaic: ʾabā́
- Classical Syriac: ʾaḇā́
- Hebrew: av (ʾāḇ)
- Phoenician/Punic: ʾb
- Ugaritic: ʾabu

**Old South Arabian:**
- Minaean, Qatabanian, Sabaean: ʾb

**Ethiopian Semitic:**
- Amharic: ʾabbat
- Ge'ez: ʾäb
- Tigre: ʾäb
- Tigrinya: ʾabo

The term also influenced Ancient Greek (abba) through Aramaic transmission.
```


## [2026-09-04T15:29:26.785Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/borage",
 "prompt": "Give the full etymology text for 'borage'."
}
```


## [2026-09-04T15:29:28.298Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=borage",
 "prompt": "Give the etymology bracket for 'borage' exactly as printed (Middle English, Old French, Medieval Latin, Arabic forms)."
}
```


### [2026-09-04T15:29:28.942Z] TOOL RESULT

```
# Etymology and Forms of أب (ab) - Father

## Etymology
The Arabic word أب derives from **Proto-Semitic *ʔabw-**, inherited through the Semitic root ء ب و (ʔ b w). It cognates with Hebrew אָב ('áv), sharing ancient roots tracing back to Proto-Afroasiatic.

## Forms and Grammar
- **Base form**: أَب (ʔab) - masculine noun
- **Construct state**: أَبُو (ʔabū) - used when possessive pronouns attach
- **Dual**: أَبَوَان (ʔabawān)
- **Plural**: آبَاء (ʔābāʔ) - broken plural

The word exhibits irregular behavior as one of "six nouns with long construct singular," maintaining special declension patterns across cases.

## Meanings
Primary definitions include "father" and "ancestor/forefather." The construct form أبو (abū) commonly appears in *kunya* (patronymic) formations like أبو حبّاب (abū ḥibāb, "father of many seeds") or أبو المسك (abū l-misk, "father of musk").

## Notable Descendants
The term generated numerous borrowings:
- Persian, Turkish, Urdu variants (abbū)
- European languages through Medieval Latin routes: Italian *borragine*, Spanish *borraja*, English *borage*
- Swahili *bwana*
- Plant-name derivatives like *baobab* and *abelmosk*
```


### [2026-09-04T15:29:29.513Z] TOOL RESULT

```
# Summary of אב (Av)

The Hebrew term **אב** (av) has multiple meanings across different languages and contexts:

## Primary Meanings

**Hebrew (Etymology 1):** The word primarily means "father" — "a male parent, especially of a human; a male who parents a child (which he has sired, adopted, fostered, etc.)." It can also denote ancestor, progenitor, originator, or prototype.

**Hebrew (Etymology 2):** As a proper noun, אב refers to the eleventh month of the civil year in the Jewish calendar, occurring between Tammuz and Elul.

**Hebrew (Etymology 3):** In botanical contexts, the term describes "swelling, spreading" or "the young shoots of a tree."

## Other Languages

- **Aramaic:** Means both "father" (absolute form of אַבָּא) and refers to the month of August/Av
- **Bukhari:** Derived from Tajik, it means "water," tracing back through Persian to Proto-Indo-European roots

## Notable Derived Terms

The word generates numerous Hebrew names incorporating אב, including Abraham, Absalom, and Abigail, plus phrases like "Tisha B'Av" (the ninth of Av, a significant date in Jewish tradition).
```


## [2026-09-04T15:29:29.787Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/إبراهيم",
 "prompt": "Give the full etymology of Arabic إبراهيم (Ibrāhīm): source language (Hebrew/Aramaic/Syriac/Ge'ez?), explanation of the -īm vowel, and list descendants (Persian, Turkish, Urdu, etc.)."
}
```


### [2026-09-04T15:29:31.163Z] TOOL RESULT

```
# Etymology of Persian بوزینه (buzina)

Based on the Wiktionary entry provided, here is the documented etymology:

## Documented Origin

The word is **inherited from Proto-Iranian**, though the specific Proto-Iranian form is not provided in the article.

## Comparative Evidence

The entry cites **Pashto بيزو (bízo, "monkey")** as a comparative form within Iranian languages, suggesting a shared Proto-Iranian root.

## Borrowings into Other Languages

The etymology section documents ancient borrowings into:

- **Old East Slavic обезьꙗ́на (obezĭjána)**, which led to Russian обезья́на (obezʹjána, "monkey, ape")
- **Old Turkic 𐰋𐰃𐰲𐰃𐰤 (béčin, "monkey")**

## Alternative Forms

The entry lists obsolete variants: **بوزنه (buzane)** and **ابوزینه (abuzine)**

## Descendants

**Middle Armenian ապուզնայ (apuznay)** is documented as a descendant.

---

**Note:** The provided Wiktionary entry does not mention Arabic origins, Middle Persian intermediaries, or specific scholarly references (Hasandust, Mo'in, etc.). The article focuses on the Proto-Iranian inheritance and documented borrowings into neighboring language families.
```


## [2026-09-04T15:29:31.284Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ابراهیم",
 "prompt": "Give the etymology and pronunciation of Persian ابراهیم (Ebrāhim) and any other language sections (Urdu, Ottoman Turkish)."
}
```


### [2026-09-04T15:29:32.138Z] TOOL RESULT

```
# Etymology of English "Gibbon"

## English Etymology
The English term derives from a "reborrowing from French _gibbon_" involving folk etymology. The word ultimately traces to a Northern Aslian language source, with the Batek language offering a comparable form (_kəboɲ_). The etymology section notes this connection through folk etymology associations with the English surname "Gibbon."

## French Etymology
French acquired the word when it "brought to Europe from French India by Joseph François Dupleix, probably from an English folk etymology" with an Aslian root. This suggests the term entered European languages through colonial Indian contact rather than direct transmission.

## Source References
The etymologies cite two scholarly works:
- Skeat's 1910 etymological dictionary
- Lim's 2020 article "An Aslian origin for the word gibbon" in the journal _Lexis_

**Note:** The provided content does not include a specific first attestation date for English "gibbon," nor does it mention Buffon explicitly in connection with the etymology.
```


### [2026-09-04T15:29:32.733Z] TOOL RESULT

```
# Etymology of Gibbon

According to the Online Etymology Dictionary, the word "gibbon" dates to 1770 and comes from French *gibbon* (18th century). The source indicates it was "supposedly from a word in the French colonies of India but not found in any language there."

The term was introduced to Europe through Marquis Joseph-François Dupleix, the French governor general in India from 1742-54, who brought these long-armed apes from the East Indies.

Additionally, the dictionary notes that the surname Gibbon itself has separate origins, deriving from Old French *Giboin*, which traces back to Frankish *Geba-win* meaning "gift-friend," or alternatively as a diminutive of Gibb (a familiar form of Gilbert).
```


## [2026-09-04T15:29:32.791Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Abraham",
 "prompt": "Give the full etymology text for 'Abraham' and any related entries shown (Abram, Abigail, Abner, Absalom, Joab)."
}
```


## [2026-09-04T15:29:34.285Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Abraham",
 "prompt": "Give the English etymology (Hebrew Avraham, Latin/Greek route, folk-etymology 'father of a multitude', relation to Abram 'exalted father'), and any other language sections briefly."
}
```


### [2026-09-04T15:29:35.000Z] TOOL RESULT

```
# Etymology of English "Borage"

The English term "borage" has a rich etymological path through multiple languages:

**Middle English → Old French → Medieval Latin:**
The word entered Middle English as "borage," borrowed from Old French "borage" (compare modern French "bourrache"). This Old French term derived from Medieval Latin "borrago."

**Medieval Latin Origins - Two Competing Theories:**

1. **Latin "borra" theory:** The Medieval Latin "borrago" may come from Latin "borra," meaning "short wool, rough hair"—possibly referencing the plant's hairy texture.

2. **Arabic origin theory:** Alternatively, "borrago" could stem from Arabic "أَبُو العَرَق" (ʔabū l-ʕaraq), literally translating to "father of sweat." This appears to reference the plant's traditional use as a sudorific herb.

**Timeline:** The source material does not provide specific dates for these etymological transitions, only tracing the borrowing pathway from Medieval Latin backward through Old French to Middle English.

The documentation treats both the Latin and Arabic possibilities as plausible alternatives rather than definitively established, indicating scholarly uncertainty about which origin is correct.
```


## [2026-09-04T15:29:35.925Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Abigail",
 "prompt": "Give the etymology of Abigail (Hebrew form and literal meaning) and, if present, the etymology of the common-noun sense 'lady's maid'."
}
```


### [2026-09-04T15:29:35.995Z] TOOL RESULT

```
# Etymology of Borage

The word "borage" entered English in the mid-13th century from Anglo-French *burage* and Old French *borage*, which derive from Medieval Latin *borrago*. This Latin term also gave rise to related words in Spanish (*boraja*), Italian (*borraggine*), and German (*Boretsch*).

The etymologists note two competing theories about the ultimate origin. One folk-etymology attributed the Medieval Latin word to Arabic *abu arak*, meaning "the father of sweat," supposedly referencing the plant's effects on the body. However, the OED and other sources suggest a more plausible origin: "Latin *borra* 'rough hair, short wool,'" which would reference the texture of the plant's leaves. The term is also related to *Boraginaceous*, the plant family classification.
```


## [2026-09-04T15:29:36.602Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Joab",
 "prompt": "Give the etymology of Joab (Hebrew form, literal meaning, Latin/Greek route)."
}
```


## [2026-09-04T15:29:37.292Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Absalom",
 "prompt": "Give the etymology of Absalom (Hebrew form, literal meaning, Latin/Greek route) and of Abner if linked."
}
```


## [2026-09-04T15:29:38.786Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Abner",
 "prompt": "Give the etymology of Abner (Hebrew form, literal meaning, Latin/Greek route)."
}
```


### [2026-09-04T15:29:39.341Z] TOOL RESULT

```
# Etymology of 'Borage'

According to the dictionary entry, the etymology bracket states:

"[Middle English, from Old French _bourage_, from Medieval Latin _borāgō_, probably from Arabic _bū'araq_, from _'abū 'araq_, source of sweat (from its use as a sudorific) : _'ab_, father, source; see **ʾb** in the Appendix of Semitic roots + _'araq_, sweat; see **ʿrq**2 in the Appendix of Semitic roots.]"

The word traces back through Old French and Medieval Latin to Arabic origins, ultimately deriving from terms meaning "father" and "sweat," referencing the plant's historical use as a sweating agent.
```


## [2026-09-04T15:29:39.703Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Abram",
 "prompt": "Give the etymology of Abram (Hebrew form, literal meaning 'exalted father', route into English)."
}
```


## [2026-09-04T15:29:41.113Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Pirkei_Avot",
 "prompt": "Give the etymology of 'Pirkei Avot' / 'Avot' (Hebrew avot 'fathers', plural of av) and alternative spellings (Aboth, Abot)."
}
```


### [2026-09-04T15:29:41.934Z] TOOL RESULT

```
# Etymology of Arabic إبراهيم (Ibrāhīm)

## Source Language
According to the Wiktionary entry, the word was "Borrowed from Aramaic אַבְרָהָם (ʾaḇrāhām)." The etymology tree also indicates the term derives from Biblical Hebrew אַבְרָהָם (ʔaḇrɔhɔm), which itself traces to Aramaic origins.

## The -īm Vowel
The documentation does not explicitly explain the vowel pattern or the -īm ending's etymological significance. The classical Qur'anic spellings show variant forms like إِبْرَٰهِـۧم, but no analysis of the vocalic development is provided in this source.

## Major Descendants
The entry lists extensive descendants across multiple language families:

- **Persian and derived languages**: Classical Persian, Chagatai (leading to Uyghur and Uzbek)
- **Turkish varieties**: Ottoman Turkish, Modern Turkish (İbrahim)
- **South Asian languages**: Urdu, Hindi, Bengali
- **Other major languages**: Malay, Indonesian, Swahili, English (Ibrahim)

This demonstrates the term's widespread adoption across Islamic and neighboring cultures following Arabic's medieval influence.
```


## [2026-09-04T15:29:42.555Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ابوی",
 "prompt": "Give etymology and meaning of Persian ابوی (abavi/abuy) 'father', and any note on Arabic source أبوي."
}
```


### [2026-09-04T15:29:43.902Z] TOOL RESULT

```
# Etymology and Pronunciation of ابراهیم

## Persian

**Etymology:** The word is "Borrowed from Arabic _[إِبْرَاهِيم](/wiki/%D8%A5%D8%A8%D8%B1%D8%A7%D9%87%D9%8A%D9%85#Arabic:_prophet "إبراهيم")_ (ʔibrāhīm)."

**Pronunciation:** Multiple regional variants exist:
- Classical Persian: /ʔib.raː.ˈhiːm/
- Iranian formal: \[ʔeb.ɹɒː.ɦíːm\]
- Dari formal (Kabuli): \[ʔɪb.ɾɑː.jíːm\]
- Tajik formal: \[ʔib.ɾɔ.ɦím\]

The name represents a biblical and Islamic figure, with the Persian transliteration as "ibrāhīm" or "ebrâhim."

## Ottoman Turkish

**Etymology:** This variant is "Derived from Arabic," ultimately tracing back through Aramaic to Biblical Hebrew origins.

**Note:** The document does not provide explicit pronunciation data for the Ottoman Turkish form, only etymological connections to the Arabic source.
```


## [2026-09-04T15:29:44.226Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://dsal.uchicago.edu/cgi-bin/app/platts_query.py?qs=%D8%A8%D9%88%D8%B2%D9%86%D9%87&searchhws=yes",
 "prompt": "Give the Platts dictionary entry for بوزنه (būzna/bozna) 'monkey' exactly: language label (P = Persian), meaning, and any variants."
}
```


### [2026-09-04T15:29:44.302Z] TOOL RESULT

```
# Etymology of Abraham

Based on the provided content, here is the etymology information available:

**Abraham** is a masculine proper name from Hebrew *Abraham*, meaning "father of a multitude." The name combines *abh* (father) + *raham* (cognate with Arabic *ruham*, meaning multitude). Originally, the name was *Abram*, meaning "high father," from the second element *ram* signifying "high, exalted."

Related terms include *Abrahamic* and *Abrahamite*.

**Abraham-man** was a historical term (1560s) for mendicant lunatics or frauds who wandered England "shamming madness so as to collect alms." One theory suggests the term originated from Bethlehem Hospital, which reportedly had an *Abraham* ward for such persons, though the ward itself may have been named after the beggars.

---

**Note:** The webpage content provided does not include etymologies for Abram, Abigail, Abner, Absalom, or Joab. Only the Abraham entry appears in the supplied text.
```


### [2026-09-04T15:29:47.554Z] TOOL RESULT

```
# Etymology of Abigail

## Hebrew Origin and Meaning

According to the Wiktionary entry, Abigail comes from Hebrew *אֲבִיגַיִל* (avigáyil), which literally means **"my Father's joy" or "fountain of joy."**

## Common-Noun Sense

The provided Wiktionary content does not include information about a common-noun sense of "abigail" meaning a lady's maid. The entry focuses exclusively on the proper noun—the biblical figure and the female given name—without addressing any secondary definitions as a common noun.
```


### [2026-09-04T15:29:47.819Z] TOOL RESULT

```
I cannot provide the etymology of Joab based on the webpage content provided. While the page lists the Hebrew form as "יוֹאָב" and shows translations in Greek (Ιωάβ), Latin (Iōabus), and Russian (Иоав), it does not include etymological information such as the literal meaning or how the name traveled through different linguistic traditions.

To find this information, you would need to consult a more comprehensive etymological resource or the Wikipedia article on Joab (which is referenced but whose full content is not included here).
```


### [2026-09-04T15:29:47.999Z] TOOL RESULT

```
# Abraham - Etymology and Language Overview

## English Etymology

The name derives from **Biblical Hebrew** אַבְרָהָם (*'aḇrāhām*), passing through **Ancient Greek** Ἀβραάμ (*Abrāā́m*) and **Late Latin** *Ābrahām* before reaching Middle and Old English.

Regarding its meaning, scholar Thomas L. Thompson proposes that "the original meaning was 'Father is exalted.'" The Wiktionary entry also notes a folk-etymological gloss connecting it to Hebrew אַב (*aḇ*, "father of") + הֲמוֹן (*hăˈmōn*, "multitude of"), from Genesis 17:4–5. Additionally, the name relates to **Abram** (*'aḇrām*), an earlier form.

The term appears as a doublet of *Ibrahim*, *Avraham*, *Abramo*, and *Abrahan* across various languages.

## Other Languages

The name appears standardized across Romance languages (French, Spanish, Italian, Portuguese), Germanic languages (German, Dutch), Slavic languages (Polish, Russian, Czech), and numerous others. Muslim-majority regions often prefer variant forms like *Ibrahim* or *Ibrāhīm*. Notable differences include Portuguese *Abraão* and Italian *Abramo*, reflecting phonetic adaptations in those linguistic traditions.
```


### [2026-09-04T15:29:50.187Z] TOOL RESULT

```
# Etymology of Absalom

**Hebrew Origin & Meaning:**
The name comes from Hebrew אַבְשָׁלוֹם (avshalóm), which literally means "father of peace." It combines אָב (av, "father") and שָׁלוֹם (shalom, "peace").

**Latin/Greek Route:**
The name traveled through Latin as Absālōm/Abessālōm before reaching modern European languages. Ancient Greek rendered it as Ἀβεσσαλώμ (Abessalóm).

---

**Regarding Abner:**
The provided content does not include information about Abner or any link between Absalom and Abner, so I cannot address that part of your request based on this source material alone.
```


### [2026-09-04T15:29:52.578Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T15:29:52.900Z] TOOL RESULT

```
# Etymology of Abner

**Hebrew Form:** אבנר (Abner)

**Literal Meaning:** "Father of light"

**Composition:** The name derives from two Hebrew elements:
- אָב (av) = "father"
- נור (nur) = "light"

**Route:** The etymology comes directly from Hebrew with no Latin or Greek intermediary route mentioned in the source material. The name is a compound of native Hebrew words rather than a loan word from classical languages.
```


### [2026-09-04T15:29:53.961Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T15:29:54.500Z] TOOL RESULT

```
# Etymology of Abram

**Hebrew Origin:**
The name Abram derives from Hebrew *אַבְרָם* (ʾaḇrām), composed of two elements: *אָב* (áb, "father") and *רָם* (rám, "high" or "exalted"). Thus, the literal meaning is "exalted father."

**Route into English:**
The path of entry proceeded through multiple languages: Hebrew → Koine Greek (*Ἀβράμ*, Abrám) → Latin (*Abram*) → English. According to the Wiktionary source, "From Latin *Abram*, from Koine Greek *Ἀβράμ* (Abrám), from Hebrew *אַבְרָם* (ʾaḇrām)."

The name first appeared in English attestation prior to 1150, initially referring to the Biblical patriarch Abraham, particularly in his early life before his name change.
```


### [2026-09-04T15:29:58.012Z] TOOL RESULT

```
# Platts Dictionary Entry for بوزنه

**Language label:** P (Persian)

**Headword:** بوزنه _būzna_, _bozna_

**Meaning:** "Monkey, ape (syn. _bandar_)"

**Variant:** The entry notes equivalence with P بوزنينه _boznīna_

The entry indicates this is a noun in the masculine gender (s.m.) and appears on page 175 of Platts' dictionary.
```


## [2026-09-04T15:30:23.085Z] AGENT (thinking)

I still have several independent follow-ups to check: the Wiktionary wikitext for بوزینه and обезьяна, Dehkhoda/abadis entries for بوزینه, a search for Lim 2020 on the Aslian origin of "gibbon", the Wikipedia Pirkei Avot article, Wiktionary's ابو entry, and a search on Arabic أبو زنة as the monkey's kunya.


## [2026-09-04T15:30:26.038Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -s 'https://en.wiktionary.org/w/index.php?title=%D8%A8%D9%88%D8%B2%D9%8A%D9%86%D9%87&action=raw' | head -60; echo ======; curl -s 'https://en.wiktionary.org/w/index.php?title=%D8%A8%D9%88%D8%B2%DB%8C%D9%86%D9%87&action=raw' | head -80",
 "description": "Fetch raw wikitext of Wiktionary buzina pages (Arabic-script and Persian-script spellings)"
}
```


## [2026-09-04T15:30:27.471Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/обезьяна",
 "prompt": "Give the full etymology of Russian обезьяна 'monkey' (Old East Slavic form, Persian/Turkic source, any date of borrowing, references cited)."
}
```


### [2026-09-04T15:30:28.153Z] TOOL RESULT

```
Exit code 1
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

<p>Not Found</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1110 cp1110, Varnish XID 677784244<br>Upstream caches: cp1110 int<br>Error: 404, Not Found at Fri, 04 Sep 2026 15:30:28 GMT<br><details><summary>Sensitive client information</summary>IP address: 128.100.1.30</details></code></p>
</div>
</html>
(eval):1: ===== not found
```


## [2026-09-04T15:30:29.721Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/بوزینه/",
 "prompt": "Quote the Dehkhoda (لغت‌نامه دهخدا) and Mo'in (فرهنگ فارسی معین) entries for بوزینه verbatim in Persian, especially any etymological remark (e.g. ابوزنه, معرب, پهلوی, بوزنه, بوزنینه)."
}
```


## [2026-09-04T15:30:30.473Z] TOOL CALL #47: WebSearch

```json
{
 "query": "Lim 2020 \"An Aslian origin for the word gibbon\" Lexis"
}
```


## [2026-09-04T15:30:31.976Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Pirkei_Avot",
 "prompt": "Give the Hebrew name, transliterations (Pirkei Avot / Pirke Aboth / Abot), literal meaning of 'Avot' (fathers), and the date/nature of the tractate."
}
```


## [2026-09-04T15:30:33.195Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ابو",
 "prompt": "Give all language sections (Arabic, Persian, Urdu, Ottoman Turkish) with etymology and meaning of ابو 'father / Abu'."
}
```


## [2026-09-04T15:30:33.200Z] TOOL CALL #50: WebSearch

```json
{
 "query": "\"أبو زنة\" القرد كنية"
}
```


### [2026-09-04T15:30:33.710Z] TOOL RESULT

```
# Etymology of Russian обезьяна

**Old East Slavic Form:**
The Russian word descends from Old East Slavic обезьꙗ́на (obezĭjána) or обозьꙗ́на (obozĭjána).

**Persian Source:**
The word was "borrowed from Persian ابوزینه (abuzina), بوزینه (buzina, 'simian')."

**Cognates:**
A related form appears in Old Ruthenian: обезъꙗ́на (obezʺjána).

**Dating:**
The source document does not specify the precise date of borrowing from Persian to Old East Slavic.

**References Cited:**
- Vasmer, Max (1964–1973) - Etymological Dictionary of the Russian Language
- Chernykh, P. Ja. (1999) - Historical-Etymological Dictionary of the Russian Language, 3rd edition
```


### [2026-09-04T15:30:38.022Z] TOOL RESULT

```
# Dehkhoda and Mo'in Entries for بوزینه

**Dehkhoda (لغت‌نامه دهخدا):**
"بوزینه. [ ن َ/ ن ِ ] ( اِ ) میمون را گویند. ( برهان ). کنیت میمون که آنرا"
The entry notes it is "مخفف ابوزینه" (abbreviated form of Abulzina) and lists variant forms including بوزنه and بوزنینه.

**Mo'in (فرهنگ معین):**
"(نِ ) ( اِ. ) میمون"

The Mo'in dictionary provides a minimal entry identifying بوزینه simply as a monkey, without etymological elaboration. In contrast, Dehkhoda offers more detailed historical and linguistic information, tracing the word to Abulzina and documenting its various historical spellings and usages in classical Persian literature.
```


### [2026-09-04T15:30:38.036Z] TOOL RESULT

```
Web search results for query: "Lim 2020 "An Aslian origin for the word gibbon" Lexis"

Links: [{"title":"An Aslian origin for the word gibbon","url":"https://journals.openedition.org/lexis/4291?lang=en"},{"title":"(PDF) An Aslian origin for the word gibbon","url":"https://www.researchgate.net/publication/342148504_An_Aslian_origin_for_the_word_gibbon"},{"title":"gibbon - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/gibbon"},{"title":"Authors – Teckwyn Lim","url":"https://journals.openedition.org/lexis/4321"},{"title":"Keywords - morphological analysis","url":"https://journals.openedition.org/lexis/433"},{"title":"Dr. Teckwyn Lim | Author","url":"https://sciprofiles.com/profile/1109525?amp=&amp="},{"title":"Mots-clés - analyse morphologique","url":"https://journals.openedition.org/lexis/4296"},{"title":"The word 'gibbon' originated in an Orang Asli language ...","url":"https://www.thestar.com.my/lifestyle/living/2020/06/26/the-word-gibbon-originated-in-an-orang-asli-language-researcher-discovers"},{"title":"An Aslian origin for the word gibbon | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-Aslian-origin-for-the-word-gibbon-Lim/a7414c553a8ecb74030ed3960edc579e9166b004"},{"title":"portfolio and links - teckwyn","url":"http://teckwyn.wikidot.com/"}]

I found the article you were looking for. Here are the key details:

Teckwyn Lim published "An Aslian origin for the word gibbon" in Lexis in 2020 (Volume 15), published online on June 13, 2020.

**Summary of the article's findings:**

The article examines the etymology of the word gibbon, which is not yet clear. The article presents a phonemic analysis using the ALINE algorithm which suggests that the root word is Northern Aslian kbɔɲ, used by Menraq communities in the heart of Peninsular Malaysia. The article reviews morphological, ethno-geographical, semantic, historical and linguistic evidence that supports this hypothesis, and proposes Malay as an intermediary, noting that several other Aslian words entered European languages via Malay.

The article is published in Lexis, a journal in English Lexicology, and is available at: http://journals.openedition.org/lexis/4291


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T15:30:40.989Z] TOOL RESULT

```
# Pirkei Avot: Essential Information

**Hebrew Name:** פִּרְקֵי אָבוֹת (pirqē aḇoṯ)

**Transliterations:** Pirqei Avoth, Pirkei Avos, Pirke Aboth, Abhoth

**Literal Meaning:** The word "pirkei" means "chapters of," while "avot" translates to "fathers." However, scholars note that in Mishnaic usage, "avot" typically refers to "fundamentals or principal categories" rather than exclusively to patriarchal figures.

**Tractate Nature & Dating:** This compilation consists of the Mishnaic tractate of Avot (the second-to-last in the order of Nezikin) plus an additional chapter. It contains sayings attributed to sages spanning from Simon the Just (approximately 200 BCE) through the period shortly after Judah haNasi (around 200 CE), the Mishnah's redactor. Uniquely among Mishnaic tractates, this work focuses exclusively on "ethical and moral principles" with minimal Jewish legal content.
```


### [2026-09-04T15:30:42.791Z] TOOL RESULT

```
# ابو (Abu) - Etymology and Meanings Across Languages

## Egyptian Arabic
**Meaning:** "Father of" (construct state); also an adjective meaning "which has" or "with"

**Etymology:** Derived from Classical Arabic أَبُو (ʔabū), the construct state of أَب (ʔab, "father"). The adjective form replaced uses of ذُو (ḏū).

**Example:** "الراجل أبو طربوش" (the man with the fez)

## Persian
**Meaning:** Used primarily in kunyas (teknonyms) borrowed from Arabic and similar loanwords

**Etymology:** Borrowed from Arabic أَبُو (ʔabū), the nominative construct state of أَب (ʔab, "father")

**Note:** The final vowel shortens before Arabic words beginning with wasla, as when followed by the definite article.

## Urdu
**Meaning:** An endearing diminutive of ابا (abbā, "dad")

**Etymology:** Borrowed from Arabic أَب (ʔab). Traces back through Proto-Semitic *ʔabw- to Proto-Afroasiatic *ʔab-

**Form:** اَبُّو (abbū) - masculine noun

---

All languages share the common root meaning connected to fatherhood, with variations in grammatical function and cultural usage patterns.
```


### [2026-09-04T15:30:43.853Z] TOOL RESULT

```
Web search results for query: ""أبو زنة" القرد كنية"

Links: [{"title":"زنا - - The Arabic Lexicon - Hawramani.com","url":"https://arabiclexicon.hawramani.com/%D8%B2%D9%86%D8%A7/"},{"title":"زَنَا - - The Arabic Lexicon - Hawramani","url":"https://arabiclexicon.hawramani.com/%D8%B2%D9%8E%D9%86%D9%8E%D8%A7/"},{"title":"زِنْنَ - - The Arabic Lexicon","url":"https://arabiclexicon.hawramani.com/%D8%B2%D9%90%D9%86%D9%92%D9%86%D9%8E/"},{"title":"زنن - - The Arabic Lexicon - Hawramani.com","url":"https://arabiclexicon.hawramani.com/%D8%B2%D9%86%D9%86/"},{"title":"تعريف و شرح و معنى زنة بالعربي في معاجم اللغة العربية معجم المعاني الجامع، المعجم الوسيط ،اللغة العربية المعاصر ،الرائد ،لسان العرب ،القاموس المحيط - معجم عربي عربي صفحة 1","url":"https://www.almaany.com/ar/dict/ar-ar/%D8%B2%D9%86%D8%A9/"},{"title":"شرح نهج البلاغة - ابن أبي الحديد - ج ٧ - الصفحة ٢٨٠","url":"http://shiaonlinelibrary.com/%D8%A7%D9%84%D9%83%D8%AA%D8%A8/2191_%D8%B4%D8%B1%D8%AD-%D9%86%D9%87%D8%AC-%D8%A7%D9%84%D8%A8%D9%84%D8%A7%D8%BA%D8%A9-%D8%A7%D8%A8%D9%86-%D8%A3%D8%A8%D9%8A-%D8%A7%D9%84%D8%AD%D8%AF%D9%8A%D8%AF-%D8%AC-%D9%A7/%D8%A7%D9%84%D8%B5%D9%81%D8%AD%D8%A9_279"},{"title":"العرب أهل البلاغة يطلق على الحمار أبو زياد وعلى القرد ...","url":"https://www.facebook.com/eslam.elshater.188/videos/%D8%A7%D9%84%D8%B9%D8%B1%D8%A8-%D8%A3%D9%87%D9%84-%D8%A7%D9%84%D8%A8%D9%84%D8%A7%D8%BA%D8%A9-%D9%8A%D8%B7%D9%84%D9%82-%D8%B9%D9%84%D9%89-%D8%A7%D9%84%D8%AD%D9%85%D8%A7%D8%B1-%D8%A3%D8%A8%D9%88-%D8%B2%D9%8A%D8%A7%D8%AF-%D9%88%D8%B9%D9%84%D9%89-%D8%A7%D9%84%D9%82%D8%B1%D8%AF-%D8%A3%D8%A8%D9%88-%D8%B2%D9%86%D8%A9-%D8%AF%D9%87-%D9%81%D9%8A-%D8%A7%D9%84%D9%84%D8%BA%D8%A9-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A/1088010219784670/"},{"title":"تفسير/شرح/ معنى (الزنة)","url":"https://www.almougem.com/search.php?query=الزنة"},{"title":"المكتبة الإسلامية - أضخم مكتبة إسلامية على الإنترنت - إسلام ويب","url":"https://www.islamweb.net/ar/library/content/122/3620/index.php?page=bookcontents_ver3&ID=3606&bk_no=122&idfrom=3600&idto=3600"},{"title":"كنى العرب في المعجم العربي | ملتقى أهل التفسير","url":"https://mtafsir.net/threads/%D9%83%D9%86%D9%89-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8-%D9%81%D9%8A-%D8%A7%D9%84%D9%85%D8%B9%D8%AC%D9%85-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A.62939/"}]

Based on the search results, I can provide you with information about "أبو زنة" (Abu Zunnah):

"أبو زنة" is a nickname for the monkey (القرد). This is a traditional Arabic linguistic term documented in various Arabic lexicons and dictionaries.

The term appears in multiple authoritative Arabic language sources, confirming that "أبو زنة" (meaning "Father of Zunnah") is the traditional epithet or nickname given to monkeys in classical Arabic terminology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T15:31:01.692Z] AGENT (thinking)

I still need the raw wikitext for بوزینه, Lane's lexicon entry on أبو زنّة, the Lim 2020 article, and archived copies of all URLs used so far—these can be fetched independently.


## [2026-09-04T15:31:01.710Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -s 'https://en.wiktionary.org/w/api.php?action=parse&page=%D8%A8%D9%88%D8%B2%DB%8C%D9%86%D9%87&prop=wikitext&format=json&formatversion=2' | python3 -c \"import json,sys; print(json.load(sys.stdin)['parse']['wikitext'][:3500])\"",
 "description": "Fetch raw wikitext of Wiktionary Persian بوزینه via API"
}
```


## [2026-09-04T15:31:02.676Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://arabiclexicon.hawramani.com/زنن/",
 "prompt": "Quote the passages (Lane's Lexicon or other lexica shown) where زِنَّة / أبو زنة is defined, especially anything saying 'أبو زنة: the ape/monkey (القرد)'."
}
```


### [2026-09-04T15:31:03.718Z] TOOL RESULT

```
==Persian==

===Etymology===
{{inh+|fa|ira-pro}}; compare {{cog|ps|بيزو|tr=bízo|t=monkey}}. Anciently borrowed into {{cog|orv|обезьꙗ́на}} whence {{cog|ru|обезья́на|t=monkey, ape}}, and likely into {{cog|otk|𐰋𐰃𐰲𐰃𐰤|t=monkey|tr=béčin}}.

===Pronunciation===
{{fa-IPA|būzīˈna}}

===Noun===
{{fa-noun|cls=بُوزِینَه}}

# [[monkey]]; [[ape]]
#: {{syn|fa|میمون|tr1=meymun|کپی|tr2=kapi}}
#* {{RQ:fa:Masnavi|I|282|هرچه مردم می‌‌کند بوزینه هم<br>آن کند کز مرد بیند دم‌‌به‌‌دم‌‌|harči mardum mē-kunad '''būzīna''' ham<br>ān kunad k-az mard bēnad dam ba dam|Whatever a man does, the '''ape''' at every moment does the same thing that he sees done by the man.}}

====Alternative forms====
* {{alt|fa|بوزنه|tr=buzane|ابوزینه|tr2=abuzine||obsolete}}

====Descendants====
* {{desc|axm|ապուզնայ|bor=1}}
```


## [2026-09-04T15:31:04.996Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://journals.openedition.org/lexis/4291?lang=en",
 "prompt": "Summarize the abstract and the section on previous etymologies of 'gibbon' (Dupleix, Buffon 1766, the claim of an Indian-language origin, OED's verdict, any mention of a Hindi/Hindustani or Persian source such as bojina/buzina), and the proposed Aslian etymon."
}
```


### [2026-09-04T15:31:10.256Z] TOOL RESULT

```
# References to أبو زنة (Abu Zanna)

Based on the content provided, here are the relevant passages defining أبو زنة as the ape/monkey:

**Ibn Manẓūr, Lisān al-ʿArab:**
"وأَبو زَنَّةَ: كنية القرد" (Abu Zanna is a nickname for the monkey)

**Ismāʿīl bin Ḥammād al-Jawharī, Tāj al-Lugha wa Ṣiḥāḥ al-ʿArabīya:**
"وأبو زنة: كنية القرد" (Abu Zanna serves as an epithet designating the simian creature)

**Murtaḍa al-Zabīdī, Tāj al-ʿArūs:**
"أَبو زَنَّةَ: كُنْيَةُ القِرْدِ" (This term functions as a traditional appellation for primates)

All three classical Arabic lexicographers consistently identify أبو زنة as a colloquial designation for the monkey (القرد), though the exact usage context and metaphorical applications vary across different hadith and poetic citations presented in their respective entries.
```


### [2026-09-04T15:31:14.586Z] TOOL RESULT

```
# Etymology of "Gibbon": Previous Theories and New Evidence

## Previous Etymologies

The word's origin has long puzzled linguists. Buffon, who first recorded "gibbon" in 1766, "suggested that gibbon may have had its origins in the East Indies, but he was unable to identify which language it came from." The Oxford English Dictionary dismisses an Indian source, stating the term is "alleged to be an Indian word, but it has not been found in any Indian language." Etymologist Skeat proposed it derived from the English surname Gibbon, extended from Gilbert.

## The Proposed Aslian Solution

Lim's research employs the ALINE phonetic algorithm to analyze 69 gibbon-related terms across 54 languages in the animal's native range. The analysis identifies Northern Aslian *kbɔɲ*—used by Menraq hunter-gatherer communities in peninsular Malaysia—as the closest phonemic match to French "gibbon" (ALINE distance of 0.1556).

The proposed etymological pathway runs: Northern Aslian *kbɔɲ* → 18th-century Malay *kəbɔn* → French *gibbon*. Supporting this theory are semantic alignment (both terms denote white-handed gibbons), biogeographical consistency with gibbon subspecies distributions, historical trade contact between the Malay Peninsula and French India, and documented Aslian loanwords in Malay and European languages.
```


## [2026-09-04T15:31:23.361Z] TOOL CALL #54: Bash

```json
{
 "command": "for u in \\\n'https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/ʔab-|page 33, root Ab 2, Proto-Semitic *ʔab(w)- father, descendants Akkadian/Arabic/Hebrew' \\\n'https://en.wiktionary.org/wiki/أب|page 33, root Ab 2, Arabic ab/abu construct, kunya, borage descendant' \\\n'https://en.wiktionary.org/wiki/אב|page 33, root Ab 2, Hebrew av father, names Abraham/Absalom/Abigail' \\\n'https://en.wiktionary.org/wiki/بوزینه|page 33, root Ab 2, Persian buzina monkey: Wiktionary gives Proto-Iranian origin, no Arabic abu zina' \\\n'https://en.wiktionary.org/wiki/gibbon|page 33, root Ab 2, gibbon: French via Dupleix, Aslian origin (Lim 2020)' \\\n'https://www.etymonline.com/word/gibbon|page 33, root Ab 2, gibbon 1770 from French, Dupleix, not found in any Indian language' \\\n'https://en.wiktionary.org/wiki/borage|page 33, root Ab 2, borage < OF < ML borrago, Arabic abu l-araq vs Latin burra' \\\n'https://www.etymonline.com/word/borage|page 33, root Ab 2, borage mid-13c., Arabic abu arak folk etymology vs OED Latin borra' \\\n'https://ahdictionary.com/word/search.html?q=borage|page 33, root Ab 2, AHD borage etymology: probably from Arabic abu araq' \\\n'https://en.wiktionary.org/wiki/إبراهيم|page 33, root Ab 2, Arabic Ibrahim borrowed from Aramaic/Hebrew Abraham; descendants Persian etc.' \\\n'https://en.wiktionary.org/wiki/ابراهیم|page 33, root Ab 2, Persian Ebrahim borrowed from Arabic Ibrahim' \\\n'https://www.etymonline.com/word/Abraham|page 33, root Ab 2, Abraham father of multitude, Abram high father' \\\n'https://en.wiktionary.org/wiki/Abraham|page 33, root Ab 2, Abraham Hebrew > Greek > Latin > English; folk etymology Gen 17:5' \\\n'https://en.wiktionary.org/wiki/Abigail|page 33, root Ab 2, Abigail Hebrew avigayil my father is joy' \\\n'https://en.wiktionary.org/wiki/Absalom|page 33, root Ab 2, Absalom Hebrew avshalom father is peace; Greek/Latin route' \\\n'https://en.wiktionary.org/wiki/Abner|page 33, root Ab 2, Abner Hebrew av + ner father of light' \\\n'https://en.wiktionary.org/wiki/Abram|page 33, root Ab 2, Abram Hebrew exalted father; Greek > Latin > English before 1150' \\\n'https://en.wiktionary.org/wiki/Joab|page 33, root Ab 2, Joab Hebrew Yoav form only' \\\n'https://en.wiktionary.org/wiki/обезьяна|page 33, root Ab 2, Russian obezyana < Old East Slavic < Persian abuzina/buzina (Vasmer)' \\\n'https://abadis.ir/fatofa/بوزینه/|page 33, root Ab 2, Dehkhoda: buzina = kunya of monkey, shortened from abu-zina; Moin: مِیمون' \\\n'https://en.wikipedia.org/wiki/Pirkei_Avot|page 33, root Ab 2, Avot/Aboth = Hebrew avot fathers, Mishnah tractate' \\\n'https://en.wiktionary.org/wiki/ابو|page 33, root Ab 2, Persian abu borrowed from Arabic construct abu, used in kunyas' \\\n'https://dsal.uchicago.edu/cgi-bin/app/platts_query.py?qs=%D8%A8%D9%88%D8%B2%D9%86%D9%87&searchhws=yes|page 33, root Ab 2, Platts Hindustani buzna/bozna monkey labelled P (Persian loan)' \\\n'https://journals.openedition.org/lexis/4291?lang=en|page 33, root Ab 2, Lim 2020 Aslian origin of gibbon' \\\n'https://arabiclexicon.hawramani.com/زنن/|page 33, root Ab 2, Arabic abu zinna = kunya of the ape (Lane)' \\\n; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\"; done 2>&1 | tail -30",
 "description": "Archive all web sources used for page 33 with fetch_source.py"
}
```


### [2026-09-04T15:31:37.857Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7c075ba11f1326fe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/930f37629a1c69c6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d554bdf30a94c766.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eebb9864227854c6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5b69fb503d4db1b7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5480297bf52b0bbb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1f5b311fdd534ea6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7132c6e9ee680f10.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/190cfd02015a87df.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4bbcf207bcfda749.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8a1f15f79b85123e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/84968c1b11aefb03.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8d97f7dfbd80795d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a6166fba4d6c72f1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4f9b6cd7f1eaa47e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/742be4a834deab00.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2c0b97792899fda7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ce0ca0bdc264ca9d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/de71bb615c38ad6d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8206cb483a0bf9b0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2a9bf9a356192bd2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/81180a22d4eeb322.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/173b04f442fdd37a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f175f9f724d70738.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f89da69d6a3e8866.txt
```


## [2026-09-04T15:31:41.472Z] AGENT

All sources are archived; I'll confirm their HTTP statuses were 200 before citing them, then write the verification file.


## [2026-09-04T15:31:42.637Z] TOOL CALL #55: Bash

```json
{
 "command": "tail -25 /home/sfmqrb/git/rishe/data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d['status'], d['bytes'], d['url'])\"",
 "description": "Check archive status of the fetched sources"
}
```


### [2026-09-04T15:31:44.378Z] TOOL RESULT

```
200 4932 https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/ʔab-
200 20028 https://en.wiktionary.org/wiki/أب
200 11842 https://en.wiktionary.org/wiki/אב
200 3623 https://en.wiktionary.org/wiki/بوزینه
200 9350 https://en.wiktionary.org/wiki/gibbon
200 5890 https://www.etymonline.com/word/gibbon
200 5576 https://en.wiktionary.org/wiki/borage
200 6078 https://www.etymonline.com/word/borage
200 4566 https://ahdictionary.com/word/search.html?q=borage
200 5332 https://en.wiktionary.org/wiki/إبراهيم
200 8562 https://en.wiktionary.org/wiki/ابراهیم
200 4538 https://www.etymonline.com/word/Abraham
200 48897 https://en.wiktionary.org/wiki/Abraham
200 9361 https://en.wiktionary.org/wiki/Abigail
200 8952 https://en.wiktionary.org/wiki/Absalom
200 4748 https://en.wiktionary.org/wiki/Abner
200 15719 https://en.wiktionary.org/wiki/Abram
200 2463 https://en.wiktionary.org/wiki/Joab
200 6347 https://en.wiktionary.org/wiki/обезьяна
200 5052 https://abadis.ir/fatofa/بوزینه/
200 24285 https://en.wikipedia.org/wiki/Pirkei_Avot
200 6889 https://en.wiktionary.org/wiki/ابو
200 375 https://dsal.uchicago.edu/cgi-bin/app/platts_query.py?qs=%D8%A8%D9%88%D8%B2%D9%86%D9%87&searchhws=yes
200 59376 https://journals.openedition.org/lexis/4291?lang=en
200 12430 https://arabiclexicon.hawramani.com/زنن/
```


## [2026-09-04T15:32:50.390Z] AGENT (thinking)

I'll verify the small Platts archive actually captured its entry, then pull the Wiktionary pages for Pashto بيزو and Old Turkic béčin to check the cognate/borrowing evidence for būzīna, and finally check vajehyab for ابوی via Mo'in/Dehkhoda.


## [2026-09-04T15:32:50.393Z] TOOL CALL #56: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/sources/web/173b04f442fdd37a.txt",
 "description": "Inspect the archived Platts page"
}
```


### [2026-09-04T15:32:50.427Z] TOOL RESULT

```
URL: https://dsal.uchicago.edu/cgi-bin/app/platts_query.py?qs=%D8%A8%D9%88%D8%B2%D9%86%D9%87&searchhws=yes
FETCHED: 2026-09-04T15:31:35Z
STATUS: 200
TITLE: A Dictionary of Urdu, Classical Hindi, and English.

A Dictionary of Urdu, Classical Hindi, and English. 

 A Dictionary of Urdu, Classical Hindi, and English. 

 Search for headword: 'بوزنه' 

 1 result

 Highlight text and press "t" to transliterate (devanagari script only)

 1) بوزنه būzna, bozna
 ( p. 175 )
 P بوزنه būzna , bozna , = P بوزنينه boznīna , s.m. Monkey, ape (syn. bandar ). 

 Search Form 

 •

 DDSA 

 Close
```


## [2026-09-04T15:32:51.518Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/بيزو",
 "prompt": "Give the Pashto section: etymology of بيزو (bízo) 'monkey', any Proto-Iranian reconstruction or cognates cited (Persian buzina?), and references."
}
```


## [2026-09-04T15:32:53.769Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/𐰋𐰃𐰲𐰃𐰤",
 "prompt": "Give the Old Turkic etymology of 𐰋𐰃𐰲𐰃𐰤 (béčin) 'monkey': source language claimed (Iranian/Persian/Sogdian?), attestation (12-animal calendar), references (Clauson etc.), and descendants."
}
```


## [2026-09-04T15:32:54.555Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=ابوی&d=moein",
 "prompt": "Quote Mo'in's (and Dehkhoda's if shown) entry for ابوی verbatim in Persian, including any origin tag like [ع.] and the gloss (پدر)."
}
```


### [2026-09-04T15:32:56.455Z] TOOL RESULT

```
# Pashto Etymology for بيزو (bizó)

Based on the Wiktionary content provided, **no etymology section is included** for the Pashto word بيزو (bizó) meaning 'monkey.'

The entry contains only:
- Pronunciation: /biˈzo/
- Part of speech: Feminine noun
- Definition: monkey
- Declension table
- A single reference to "Pashto-English (Academy of Sciences Kabul)"

**No Proto-Iranian reconstructions, cognates (such as Persian buzina), or etymological information are cited** in this dictionary entry. The references section merely directs to an external Pashto-English dictionary resource without providing etymological details in the visible content.
```


### [2026-09-04T15:32:59.867Z] TOOL RESULT

```
# Mo'in's Entry for ابوی

According to the dictionary content shown, Mo'in's entry states:

"(اَ بَ) [ع.] (ص نسب.) 1 - پدری. 2 - (عا.) پدر."

The term means paternal/fatherly (پدری) and father (پدر), with the origin marked as Arabic [ع.].
```


### [2026-09-04T15:33:00.469Z] TOOL RESULT

```
# Etymology of Old Turkic 𐰋𐰃𐰲𐰃𐰤 (béčin)

**Source Language:** The word is "Inherited from Proto-Turkic *bẹ̄čin" with "unknown origins, possibly a borrowing from an Iranian language."

**Persian Connection:** A Persian cognate is cited: بوزینه (buzine, "monkey"), suggesting Iranian origins rather than purely Turkic development.

**Attestation:** The 9th-century Kültegin Inscription from the Orkhon inscriptions provides the earliest documented use, where béčin appears in a calendar context: "Year of Monkey" (27th day of the 7th month).

**Key References:**
- Clauson's *Etymological Dictionary of pre-thirteenth-century Turkish* (1972)
- Tekin's *Grammar of Orkhon Turkic* (1968)
- Starostin, Dybo & Mudrak's *Etymological dictionary of the Altaic languages* (2003)

**Descendants:** The page doesn't explicitly list descendants, but the term's presence in Old Turkic suggests continuity through Turkic language families.
```


## [2026-09-04T15:33:09.003Z] AGENT (thinking)

The Pashto page has no etymology, so I'll skip citing it. Next I'll archive the Old Turkic and vajehyab pages, write and validate the verification file, and run verify_check in one command.


## [2026-09-04T15:35:42.171Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/𐰋𐰃𐰲𐰃𐰤' --note 'page 33, root Ab 2, Old Turkic bečin monkey (Kul Tegin inscr.), possibly Iranian loan cf. Persian buzina' && python3 tools/fetch_source.py 'https://vajehyab.com/?q=ابوی&d=moein' --note 'page 33, root Ab 2, Moin: ابوی [ع.] paternal; colloq. father' && cat > data/verification/page-33.json <<'EOF'\n{\n  \"pdf_page\": 33,\n  \"book_page\": 3,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ab 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Proto-Semitic *ʔab- / *ʔabw- 'father' (Akkadian abum, Ugaritic ʾabu, Hebrew ʾāḇ, Aramaic ʾabbā, Arabic ʔab / construct ʔabū, Ge'ez ʾab), from Proto-Afroasiatic *ʔab-; a nursery word\",\n      \"note\": \"The root is real, the 'Semitic' label and the gloss 'father' are right (Wiktionary Proto-Semitic *ʔabw-; Klein p.6 s.v. Aboth: 'Heb. abh, rel. to Aram. abh, abba, Ugar. 'b, Arab. ab, Ethiop. ab, father; of uncertain origin, possibly traceable to *ab(a), a child's word for father'). Klein p.6 is in fact the model for the whole chart: his Aboth entry cross-refers to Abraham, Abner, Absalom, Abigail, Joab, abbot and borage exactly as Nourai draws. Two branches are weak: (1) Persian būzīna 'monkey' is drawn as a loan from Arabic abū zinā 'father of whoredom' — the traditional Persian/Lokotsch view, but modern sources (Wiktionary, with the Pashto cognate bízo and the 8th–9th-c. Old Turkic borrowing béčin) treat the word as inherited Iranian and the Arabic kunya abū zanna as a reinterpretation; (2) French/English gibbon is drawn from Hindustani bojīna (= Urdu būzna) — no source supports this; OED/Etymonline say gibbon 'has not been found in any Indian language', and Lim 2020 derives it from Northern Aslian kbɔɲ via Malay. The borage branch (Arabic abū ʿaraq 'father of sweat' > ML borrago) is accepted by AHD, Klein and Lokotsch but rejected by OED/Etymonline in favour of Latin burra 'rough hair', so it is only plausible. FVQ:44 cited for the root is Jeffery's Ibrāhīm entry, which concerns node 14, not the root itself.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/ʔab-\",\n        \"https://en.wiktionary.org/wiki/أب\",\n        \"https://en.wiktionary.org/wiki/אב\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:6\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 14 (p.6), line 1209 s.v. 'Aboth, also Abot': 'Heb. Abhōth, pl. of abh, father, rel. to Aram. abh (absolute state), abbā (emphatic state), Ugar. 'b, Arab. ab, Ethiop. ab, father; of uncertain origin, possibly traceable to *ab(a), a child's word for father. Cp. the first element in Abraham, Abner, Absalom, Abigail, and the second element in Joab, Moab, Barabbas. Cp. also abbot ... Cp. also borage.' — Klein is the source of the chart's Semitic root and of most of its branches.\"},\n        {\"ref\": \"FVQ:44\", \"status\": \"partial\", \"note\": \"FVQ_pages.txt leaf 61-62 (printed pp.44-45): the entry on p.44 is 'Ibrāhīm ... Abraham. It is always used of the Biblical Patriarch and thus is ultimately derived from Heb. [Abrāhām]'. Jeffery does not discuss the Semitic word for 'father'; the reference belongs to node 14.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"ab, abŭ, a.b.v\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic أَب ʔab 'father' continues Proto-Semitic *ʔab(w)-; the lexical root is ʔ-b-w (the final w surfaces in the dual ʔabawāni and in the 'six nouns' declension, where the construct state before a genitive is lengthened: nom. أَبُو ʔabū, gen. ʔabī, acc. ʔabā). The construct ʔabū is the form used in kunyas (teknonyms) 'father of X', which is why it heads the derivatives in node 3. Nourai's 'a.b.v' is the root ʔ-b-w; all three items are correct.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/أب\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/ʔab-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVQ:44\", \"status\": \"partial\", \"note\": \"FVQ_pages.txt leaf 61 (p.44): only the Ibrāhīm entry; Jeffery gives no entry for ab/abū (a native Arabic word is outside his scope).\"},\n            {\"ref\": \"FVA:25\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e vāžehā-ye ʿarabī dar fārsī: no digital copy found.\"},\n            {\"ref\": \"LKT:44\", \"status\": \"partial\", \"note\": \"LKT.txt leaf 70 (printed p.44) contains entries 538-546 (Ar. duffa, duhān, Tk. düğme ... Tk. dümen) — nothing on ab; the relevant Lokotsch material is entry 13 'Ar. abū ʿaraq' (leaf 28, p.2) and entry 556 'Tk. ebuzine, auch buzine Affe [aus ar. abū zina Vater der Unzucht]' (leaf 71, p.45). Lokotsch presupposes Ar. abū 'father' but has no entry for it.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"abŭ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian ابو abu is the Arabic construct ʔabū taken over inside Arabic kunyas and names: Abū ʿAlī Sīnā (Avicenna), Abu l-Fażl, Abu l-Qāsem, Abu l-Ḥasan, Abu l-Fatḥ; before the Arabic article the vowel shortens (abu-l-), and in colloquial/poetic use the initial a- drops, giving Bu l-havas 'father of caprice = whimsical' (بوالهوس), Bū ʿAlī etc. The bracketed ابوی abavi 'father' (polite/colloquial) is the Arabic relative adjective أَبَوِيّ ʔabawī 'paternal', which Mo'in tags [ع.] '(ص نسب.) 1- پدری 2- (عا.) پدر'. The chart's spelling «آبو» with madda is not a Persian orthographic form (the word is written ابو); it is probably a typographic artefact, but the derivation itself is correct: all forms are Arabic loans in Persian, borrowed with Islamic onomastics from the 7th-9th c. onward.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/ابو\",\n            \"https://vajehyab.com/?q=ابوی&d=moein\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVA:25\", \"status\": \"not_checked\", \"note\": \"Nahvi: no digital copy found.\"},\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in via vajehyab (?q=ابوی&d=moein): 'ابوی (اَ بَ) [ع.] (ص نسب.) 1- پدری. 2- (عا.) پدر.' — Arabic origin tag, sense 'father' in colloquial use, as the chart says. The abridged MON_part1.txt has no separate ابو lemma (grep '^ابو').\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"abŭ-zînâ; abŭ-araq\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"(a) أَبُو زَنَّة abū zanna is a genuine Arabic kunya of the ape: Lisān al-ʿArab, al-Jawharī's Ṣiḥāḥ and Tāj al-ʿArūs all have 'وأبو زَنَّةَ: كنية القرد'. The classical lexica vocalise the second element زَنَّة (zanna, root z-n-n), not زِنَا zinā 'fornication'; the gloss 'father of whoredom' is Lokotsch's ('Vater der Unzucht', entry 556) and Nourai's reading, i.e. a folk-etymological interpretation of the kunya, not its established meaning — so the word exists but the gloss is only plausible. (b) أَبُو عَرَق abū ʿaraq 'father of sweat' is the name under which medieval Arabic pharmacology knew borage (a sudorific), the accepted or 'probable' source of Medieval Latin borrāgō in AHD ('probably from Arabic bū ʿaraq, from ʔabū ʿaraq, source of sweat'), Klein and Lokotsch; Wiktionary lists borage among the derivatives of Arabic أب; OED/Etymonline prefer Latin burra. Both compounds are ordinary kunya formations with the construct ʔabū + genitive, so the arrow from node 1 is formally correct.\",\n          \"sources\": [\n            \"https://arabiclexicon.hawramani.com/زنن/\",\n            \"https://en.wiktionary.org/wiki/أب\",\n            \"https://ahdictionary.com/word/search.html?q=borage\",\n            \"https://en.wiktionary.org/wiki/borage\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"LKT:44\", \"status\": \"supports\", \"note\": \"LKT.txt leaf 71 (printed p.45, i.e. the page after the one cited), entry '556. Tk. ebuzine: Auch buzine Affe [aus ar. abū zina Vater der Unzucht]; hieraus russ. obez'jana, klruss. obezjana Affe [vgl. lit. bezdona]' — this is the source of the 'father of whoredom' gloss; and leaf 28 (p.2) entry '13. Ar. abū ʿaraq: Vater des Schweißes, hieraus lat. borrago, eine Pflanze, die durch die ar. Medizin im Mittelalter verbreitet wurde ... Trotz ML 1412 scheint diese Ableitung noch immer die beste und wenig anfechtbar zu sein.'\"},\n            {\"ref\": \"AHD:152\", \"status\": \"supports\", \"note\": \"AHD p.152 (1975 New College Ed.) is the main-dictionary page with 'borage', not the IE appendix; the current online AHD (search.html?q=borage) reads '[Middle English, from Old French bourage, from Medieval Latin borāgō, probably from Arabic bū ʿaraq, from ʔabū ʿaraq, source of sweat (from its use as a sudorific): ʔab, father, source + ʿaraq, sweat]'.\"},\n            {\"ref\": \"FVQ:44\", \"status\": \"not_found\", \"note\": \"FVQ_pages.txt leaf 61 (p.44): only the Ibrāhīm entry; nothing on abū zanna or abū ʿaraq.\"},\n            {\"ref\": \"FVA:25\", \"status\": \"not_checked\", \"note\": \"Nahvi: no digital copy found.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"bŭzîneh\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Persian بوزینه būzīna (variants بوزنه būzna, بوزنینه būznīna, and a learned/obsolete ابوزینه abūzīna) 'monkey, ape' is attested from Classical Persian (Rūmī, Masnavī I 282: har-či mardum mē-kunad būzīna ham ...). The traditional derivation, followed by Borhān-e Qāṭeʿ/Dehkhoda ('کنیت میمون ... مخفف ابوزینه'), Lokotsch (entry 556) and Nourai, takes it as Arabic abū zanna/zinā 'father of whoredom' with aphaeresis of a- (abū-zīna > būzīna). Modern sources reject this: Wiktionary treats būzīna as inherited from Proto-Iranian, comparing Pashto بيزو bízo 'monkey' (which cannot come from an Arabic kunya), and notes that the word was borrowed 'anciently' into Old East Slavic обезьꙗ́на (> Russian обезьяна; Vasmer, Chernykh) and likely into Old Turkic 𐰋𐰃𐰲𐰃𐰤 béčin, already attested in the Kül Tegin inscription (8th-9th c.) as the calendar 'monkey' year — a chronology and a phonetic shape (-č-) that fit an Iranian rather than an Arabic source. On that view Arabic abū zanna 'kunya of the ape' and the Persian variant abūzīna are folk-etymological reshapings of the Iranian word, i.e. the arrow runs the other way. Mo'in's own entry gives no Arabic tag. The Rūmī quotation in the chart (Masnavī, 'čūn del-e būzīna gardad ān del-aš') correctly illustrates the word.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/بوزینه\",\n            \"https://en.wiktionary.org/wiki/обезьяна\",\n            \"https://en.wiktionary.org/wiki/𐰋𐰃𐰲𐰃𐰤\",\n            \"https://abadis.ir/fatofa/بوزینه/\",\n            \"https://arabiclexicon.hawramani.com/زنن/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:602\", \"status\": \"partial\", \"note\": \"MON_part1.txt line 26095 (abridged Mo'in): 'بوزینه ... [بوزینا، بوزنه، بوزنینه] (اِ.) (جا.) میمون' and abadis 'فرهنگ معین: (نِ) (اِ.) میمون' — the word and its variants are there with the gloss 'monkey', but Mo'in gives NO [ع.] Arabic tag and no abū-zinā etymology; the Arabic derivation in the chart comes from Borhān/Dehkhoda ('مخفف ابوزینه') and Lokotsch, not from Mo'in.\"},\n            {\"ref\": \"FVA:180\", \"status\": \"not_checked\", \"note\": \"Nahvi: no digital copy found.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Hindustani\",\n          \"words\": \"bojîna\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Urdu/Hindustani بوزنہ būzna, bozna (also boznīna) 'monkey, ape (syn. bandar)' is recorded by Platts (p.175) with the label P = Persian loan, i.e. Persian būzna/būzīna taken into Hindustani through the Persianate court and literary culture of the Delhi Sultanate and Mughal period (13th-18th c.); the Indian vowel o for Persian ū is regular in Hindustani pronunciation (bozna). Nourai's 'bojîna' with j is unusual (Platts has z) but evidently the same word. The edge Persian > Hindustani is correct.\",\n          \"sources\": [\n            \"https://dsal.uchicago.edu/cgi-bin/app/platts_query.py?qs=%D8%A8%D9%88%D8%B2%D9%86%D9%87&searchhws=yes\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"PRT:253\", \"status\": \"not_checked\", \"note\": \"Partridge, Origins (1958) is lending-only on archive.org (originsshortetym00part); the fulltext-search endpoints (inside.php, BookReaderSearch.php) returned 'Item not available'/404, so p.253 could not be read.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"French gibbon (Buffon, Histoire naturelle 1766) was introduced by Joseph-François Dupleix, governor of French India 1742-54, who brought the animal and its name to Europe. But no source connects it with Hindustani būzna/bojīna, and the shapes do not match (b-z-n vs. g-b-n). OED (quoted by Lim 2020) says the word is 'alleged to be an Indian word, but it has not been found in any Indian language'; Etymonline: 'supposedly from a word in the French colonies of India but not found in any language there'; Klein: 'a name of Indian origin brought to Europe by ... Dupleix' without giving an etymon; Skeat suggested the English surname Gibbon. The current proposal (Lim 2020, Lexis 15; adopted by Wiktionary) is Northern Aslian kbɔɲ 'white-handed gibbon' (Menraq, Peninsular Malaysia) > 18th-c. Malay kəbɔn > French gibbon, via Malay trade with French India. Nourai's chart-note ('taken to France from India in the 18th century') is right about the route; the derivation from būzīna is not supported by anyone.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/gibbon\",\n            \"https://en.wiktionary.org/wiki/gibbon\",\n            \"https://journals.openedition.org/lexis/4291?lang=en\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:655\", \"status\": \"partial\", \"note\": \"KLN_1966.txt leaf 354, line 16112 s.v. gibbon: 'F., a name of Indian origin brought to Europe by the Marquis Joseph-François Dupleix (1697-1763), governor-general of the French possessions in India (1742-54).' Klein supports 'French, from India, 18th c.' but names no Indian word — nothing about būzīna/bojīna. (The printed page on this leaf is c. 684-686 by the leaf formula, not 655; the entry is unmistakable regardless.)\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"gibbon\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English gibbon is borrowed from French gibbon (Buffon 1766), first attested in English in 1770 (Etymonline; Wiktionary calls it a re-borrowing shaped by folk-association with the surname Gibbon). The French > English step is uncontroversial; only the origin of the French word (node 6) is in dispute.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/gibbon\",\n            \"https://en.wiktionary.org/wiki/gibbon\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:655\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 354 s.v. gibbon: 'gibbon, n., a small, long-armed ape. — F., a name of Indian origin brought to Europe by the Marquis Joseph-François Dupleix' — English from French, as drawn.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Middle Latin\",\n          \"words\": \"borrâco\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The Medieval Latin plant-name is borrāgō (gen. borrāginis; also borāgō, burrāgō), the source of Italian borragine, Spanish borraja, Portuguese borragem, Provençal borrage, French bourrache, German Boretsch. 'borrâco' with -c- is not a recorded form; the book almost certainly printed 'borrâgo' and the scan misread g as c (Klein s.v. borage: 'fr. ML. borrago'; AHD 'Medieval Latin borāgō'). As for the arrow from Arabic abū ʿaraq: AHD ('probably'), Klein and Lokotsch (entry 13: 'Trotz ML 1412 scheint diese Ableitung noch immer die beste') derive borrāgō from the Arabic name of the plant, abū ʿaraq 'father of sweat', spread by Arabic medicine in the Middle Ages; the initial a- was lost and ʿaraq gave -rāgō with the Latin plant-suffix -āgō (cf. plantāgō, lappāgō). OED and Etymonline prefer Latin burra 'rough hair, short wool' (the hairy leaves), and Wiktionary lists both. So the derivation is plausible, not certain; the node is flagged for the misprinted form.\",\n          \"sources\": [\n            \"https://ahdictionary.com/word/search.html?q=borage\",\n            \"https://en.wiktionary.org/wiki/borage\",\n            \"https://www.etymonline.com/word/borage\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:152\", \"status\": \"supports\", \"note\": \"Online AHD s.v. borage: 'from Medieval Latin borāgō, probably from Arabic bū ʿaraq, from ʔabū ʿaraq, source of sweat (from its use as a sudorific)'. (p.152 of the 1975 New College Edition is not online; the online text is the revised edition of the same entry.) Note the form is borāgō, with g.\"},\n            {\"ref\": \"KLN:106\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 5360 s.v. borage (not cited by Nourai but the chart's evident model): 'ME., fr. OF. borrace (cp. its variant burage and F. bourrache), fr. ML. borrago, ult. fr. Arab. abu ʿarak, lit. father of sweat, so called by the Arab physicians because of its sudorific effect. See abbot and cp. arrack.'\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Old French\",\n          \"words\": \"borrace, bourrache\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old French borrace / borage / burage (13th c.; Anglo-French burage) continues Medieval Latin borrāgō (accusative borrāginem gave the learned/Italianate forms; the vernacular form drops the -gin- syllable). Modern French bourrache is the same word with the later French spelling ou for /u/ and -ache. Klein: 'OF. borrace (cp. its variant burage and F. bourrache)'; AHD: 'Old French bourage'; Etymonline: 'Anglo-French burage, Old French borage (13c., Modern French bourrache)'.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/borage\",\n            \"https://en.wiktionary.org/wiki/borage\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:152\", \"status\": \"supports\", \"note\": \"Online AHD s.v. borage: '[Middle English, from Old French bourage, from Medieval Latin borāgō ...]' — Old French stage as drawn.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"borage\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle English borage / burage (mid-13th c.) borrowed from Anglo-French burage / Old French borage; the plant (Borago officinalis) was used in salads and cordials, hence the gloss 'salad seasoning' (Klein: 'a blue-flowered plant used in salads'). The Old French > English step is standard and undisputed.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/borage\",\n            \"https://en.wiktionary.org/wiki/borage\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:152\", \"status\": \"supports\", \"note\": \"Online AHD s.v. borage: 'Middle English, from Old French bourage' — same chain.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Hebrew\",\n          \"words\": \"abh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Biblical Hebrew אָב ʾāḇ 'father; ancestor; originator' (construct אֲבִי ʾăḇī, pl. אָבוֹת ʾāḇōṯ) is the direct reflex of Proto-Semitic *ʔab(w)-, with the Hebrew spirantisation of post-vocalic b to ḇ [v] that Nourai's 'abh' represents. Cognate with Aramaic ʾabbā (whence Greek/English abba), Arabic ʔab, Akkadian abum.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/אב\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/ʔab-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:6\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 14 (p.6) s.v. Aboth: 'Heb. Abhōth, pl. of abh, father, rel. to Aram. abh ... Arab. ab, Ethiop. ab, father'.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"Abot\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Abot / Aboth / Avot is the name of the Mishnah tractate פִּרְקֵי אָבוֹת Pirqē Āḇōṯ 'Chapters of the Fathers' (sayings of the sages c. 200 BCE - 200 CE), and of the first benediction of the Amidah; Hebrew אָבוֹת ʾāḇōṯ is simply the plural of ʾāḇ 'father' (in Mishnaic usage also 'principal categories'). The English spelling Abot(h) is a direct transliteration used in Jewish-studies English since the 19th c.\",\n          \"sources\": [\n            \"https://en.wikipedia.org/wiki/Pirkei_Avot\",\n            \"https://en.wiktionary.org/wiki/אב\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:6\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 14 (p.6): 'Aboth, also Abot, n., 1) the Mishnah treatise also called Pirke Aboth or The Ethics of the Fathers; 2) name of the first benediction of the Shemoneh Esreh (Jewish liturgy). — Heb. Abhōth, pl. of abh, father'.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Hebrew\",\n          \"words\": \"Abh-raham; Abh-ram; Abh-ner; Ab-šalom; Abh-igayil; Yo-abh\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"All six are genuine Biblical Hebrew theophoric/kinship names built on ʾāḇ 'father' and all are drawn correctly as compounds of node 11: אַבְרָם ʾAḇrām 'father is exalted' (ʾāḇ + rām 'high', participle of rūm) — CONFIRMED; אַבְרָהָם ʾAḇrāhām — the gloss 'father of a multitude' is the explanation given in Genesis 17:5 (ʾaḇ hămōn gōyim), followed by Klein (who invokes an otherwise unattested *rahām ~ Arabic ruhām 'multitude'), Etymonline and Nourai; modern scholarship (Wiktionary, citing T. L. Thompson) treats this as folk etymology and Abraham as a dialectal expansion of Abram 'father is exalted' — so PLAUSIBLE; אַבְנֵר ʾAḇnēr 'my father is a lamp/light' (ʾāḇ + nēr; cf. Babylonian Abu-nūri) — CONFIRMED; אַבְשָׁלוֹם ʾAḇšālōm 'father is peace' (ʾāḇ + šālōm) — CONFIRMED; אֲבִיגַיִל ʾĂḇīḡayil 'my father is joy' (ʾăḇī + gīl 'rejoicing') — CONFIRMED; יוֹאָב Yōʾāḇ 'YHWH is father' (Yō- theophoric + ʾāḇ) — CONFIRMED. Nourai's cross-references to Semitic roots N.w.r (nēr 'lamp') and S.l.m (šālōm) are correct. Node verdict 'plausible' only because of the Abraham gloss.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Abraham\",\n            \"https://en.wiktionary.org/wiki/Abram\",\n            \"https://en.wiktionary.org/wiki/Abner\",\n            \"https://en.wiktionary.org/wiki/Absalom\",\n            \"https://en.wiktionary.org/wiki/Abigail\",\n            \"https://en.wiktionary.org/wiki/Joab\",\n            \"https://www.etymonline.com/word/Abraham\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:6\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 14 (p.6): 'Abraham ... Heb. Abhrāhām, lit. father of the multitude, compounded of abh, father, and *rahām, multitude, which is rel. to Arab. ruhām, of s.m.; see Gen. 17:5'; 'Abram ... Heb. Abhrām, compounded of abh, father, and rām, high, exalted'; 'Abner ... Heb. Abhnēr, lit. my father is light, fr. abh, father, and nēr, light; cp. the Babylonian PN. Abunuri'; 'Absalom ... Heb. Abhshālōm, lit. father is peace, fr. abh, father, and shālōm, peace'; and line 20305 'Joab ... Heb. Yōʾābh, lit. the Lord is (his) father'. Nourai's glosses are copied from Klein.\"},\n            {\"ref\": \"FVQ:44\", \"status\": \"partial\", \"note\": \"FVQ_pages.txt leaves 61-62 (pp.44-45), s.v. Ibrāhīm: 'ultimately derived from Heb. [Abrāhām]' — supports the Hebrew name but says nothing about its internal etymology or the other five names.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Arabic\",\n          \"words\": \"Abrahim\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic إِبْرَاهِيم ʔIbrāhīm (Qur'an, c. 69 occurrences, e.g. 2:124) is ultimately Hebrew ʾAḇrāhām, but Jeffery shows that the immediate source was not Hebrew (which would have given *ʾAbrāhām) but the Syriac/Aramaic Christian form ʾAḇrāhām/Aḇrāhām, with the peculiar Qur'anic vocalism -īm (early Muslim philologists themselves noted the form as foreign and recorded variants Abrāhām, Ibrāhām); Wiktionary likewise gives 'borrowed from Aramaic ʾaḇrāhām', from Biblical Hebrew. So the arrow Hebrew > Arabic is right in substance, with Aramaic/Syriac as the intermediary. Nourai's 'Abrahim' is a rough transcription of Ibrāhīm.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/إبراهيم\",\n            \"https://en.wiktionary.org/wiki/Abraham\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVQ:44\", \"status\": \"supports\", \"note\": \"FVQ_pages.txt leaf 61-62 (pp.44-45): 'Ibrāhīm. Occurs some 69 times ... Abraham. It is always used of the Biblical Patriarch and thus is ultimately derived from Heb. [Abrāhām]. If the name had come direct from the Heb. we should have expected the form [Abrāhām] ... some early authorities recognized it as a foreign borrowing ... The common Syr. form is [Abrāhām] which is obviously the source of both the Eth. and the Arm. ... the immediate source is not easy to determine.'\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Persian\",\n          \"words\": \"Ebrâhîm\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian ابراهیم Ebrāhīm (Classical Persian Ibrāhīm, /ʔib.raː.ˈhiːm/) is borrowed from Arabic ʔIbrāhīm with the Islamic onomasticon; the Persian spelling drops the Arabic hamza-seat alif-kasra (إ > ا) and Iranian Persian lowers short i to e (Ebrāhīm). The Rūmī quotation ('bot šekastī gīram Ebrāhīm-vār') illustrates the name of the prophet as idol-breaker.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/ابراهیم\",\n            \"https://en.wiktionary.org/wiki/إبراهيم\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; Wiktionary confirms 'Borrowed from Arabic إِبْرَاهِيم'.\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"English\",\n          \"words\": \"Abraham, Abram, Abner, Absalom, Abigail, Jaob\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The English names reach English through the Bible: Hebrew > Septuagint Greek (Ἀβραάμ, Ἀβράμ, Ἀβεννήρ, Ἀβεσσαλώμ, Ἀβιγαία, Ἰωάβ) > Latin Vulgate (Abraham, Abram, Abner, Absalom, Abigail, Ioab) > Old/Middle English (Abraham and Abram already before 1150 in Old English biblical prose; the others in Wycliffite and later Bibles). The Greek/Latin route explains why English has Abraham with -h- but Absalom (Greek/Latin -s-) rather than Hebrew Abšalom. All five real names are correctly placed. 'Jaob' is a transposition error for 'Joab' (Hebrew Yōʾāḇ, Late Latin Joab) — either a misprint in the book or a scan misreading; the book must intend Joab, which Klein's Aboth entry lists.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Abraham\",\n            \"https://en.wiktionary.org/wiki/Abram\",\n            \"https://en.wiktionary.org/wiki/Absalom\",\n            \"https://en.wiktionary.org/wiki/Joab\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 14 (p.6) entries Abraham, Abram, Abner, Absalom (all 'masc. PN.; in the Bible ...' from Heb.) and line 20305 'Joab ... Late L. Joab, fr. Gk. Ἰωάβ, fr. Heb. Yōʾābh, lit. the Lord is (his) father' — Klein spells it Joab, confirming that 'Jaob' is an error.\"},\n            {\"ref\": \"AHD\", \"status\": \"not_checked\", \"note\": \"No page given; the AHD IE appendix (AHD_watkins1985.txt) does not cover Semitic names, and the 1975 main dictionary is not online.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nEOF\npython3 -m json.tool data/verification/page-33.json > /dev/null && echo JSON_OK && python3 tools/verify_check.py 33",
 "description": "Archive last sources, write page-33 verification JSON, validate, and run verify_check"
}
```


### [2026-09-04T15:35:44.989Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9b0725f3b09705ed.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7501ebdd4ebfb2ef.txt
JSON_OK
nodes verified: 16/16
node verdicts: {'confirmed': 10, 'plausible': 2, 'disputed': 2, 'transcription_suspect': 2}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 5, 'not_checked': 7, 'supports': 13, 'not_found': 1}
```


## [2026-09-04T15:36:00.480Z] AGENT

Wrote `/home/sfmqrb/git/rishe/data/verification/page-33.json`; `verify_check.py 33` reports 16/16 nodes, no PROBLEM lines.

**Page 33 (book p. 3) — root Ab 2 "father" [Semitic]: root confirmed** (Proto-Semitic *ʔab(w)-; Klein p.6 s.v. Aboth is the evident model for the whole chart).

Node verdicts: confirmed 10 · plausible 2 · disputed 2 · transcription_suspect 2. Ref checks: 13 supports, 5 partial, 1 not_found, 7 not_checked (FVA has no digital copy; PRT is lending-only; AHD:152 is a main-dictionary page, checked against the online AHD instead).

- **disputed — #4 Persian bŭzîneh < Arabic abū-zinā**: Wiktionary treats būzīna as inherited Iranian (cf. Pashto bízo), anciently borrowed into Old East Slavic obezʹjana and Old Turkic béčin (Kül Tegin inscr.); Arabic abū zanna "kunya of the ape" (Lisān, Ṣiḥāḥ) is a reinterpretation. Nourai follows Borhān/Dehkhoda/Lokotsch; Mo'in gives no Arabic tag.
- **disputed — #6 French gibbon < Hindustani bojīna**: no source links them; OED/Etymonline: "not found in any Indian language"; Lim 2020 (Lexis) derives gibbon from Northern Aslian kbɔɲ via Malay. Klein p.655 only says "of Indian origin, brought by Dupleix".
- **transcription_suspect — #8 Middle Latin "borrâco"**: the form is borrāgō (g misread as c). The Arabic abū ʿaraq origin itself is plausible (AHD "probably", Klein, Lokotsch) but OED/Etymonline prefer Latin burra.
- **transcription_suspect — #16 English "Jaob"**: transposition for Joab (Klein p.6 Joab).
- plausible: #3 (abū zanna's gloss "father of whoredom" is folk-etymological; abū ʿaraq > borage accepted only by some) and #13 (Abraham "father of a multitude" is the Gen 17:5 folk etymology; the other five names confirmed).

Minor: #2's script «آبو» with madda is not a Persian spelling (should be ابو); derivation otherwise fine (ابوی = Arabic ʔabawī, Mo'in [ع.]).
