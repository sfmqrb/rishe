# Verification process log — model-comparison/verify-sonnet-page-33


## [2026-09-04T18:07:05.441Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 33 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-33.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-33.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (all files listed in the source matrix exist there). ONE DEVIATION from the instructions: this is a model-comparison run, so write your output to /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet/page-33.json instead of data/verification/, do NOT read or copy any existing file under /home/sfmqrb/git/rishe/data/verification/page-*.json, and check coverage with `VERIFY_DIR=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet python3 /home/sfmqrb/git/rishe/tools/verify_check.py 33` (the script now honours VERIFY_DIR). Everything else as instructed (modern web sources archived with tools/fetch_source.py, Nourai's citations checked in the local reference texts, every relevant book consulted per the source matrix). Reply with the short summary described in the instructions.


## [2026-09-04T18:07:08.920Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T18:07:08.935Z] TOOL RESULT

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
62	- **Scanned references without OCR text** (Borhan-e Qate' vols 3-5 = BQT pages ~1208-2475,
63	  Farahvashi's Iranvij = IRN, and any entry whose table record has a `scans` list): do NOT
64	  OCR whole books. Fetch only the cited page:
65	  `python3 /home/sfmqrb/git/rishe/tools/ref_page.py BQT:918 --image`
66	  It renders that one page to PNG, OCRs it (Persian OCR is rough), caches both under
67	  `data/verification/sources/refs/ocr/`, and prints the text plus the PNG path. If the OCR
68	  is unreadable, Read the PNG (you can read Persian print directly), and then SAVE what you
69	  read: write the entry/entries you used (headword, Mo'in's etymological footnote, and any
70	  surrounding lines you relied on) verbatim to the companion file
71	  `data/verification/sources/refs/ocr/<ABBR>/<page>.vision.txt` (the tool prints the exact
72	  paths). The tool prefers that file next time, so nobody pays for reading the image again.
73	  If the printed page number on the image is off, re-run with `--pdf-page <n>` adjusted, and
74	  note the correct pdf page in your ref_check note.
75	- If `kind` is `website`, use the `lookup_hint` URL pattern with WebFetch.
76	- Do this for at least ONE cited reference per node (the most authoritative available:
77	  POK/AHD/KLN for IE roots, HRN/HUB/BRT/KNT/PHD for Iranian, KLN/FVQ/AFM/PLA for Semitic,
78	  BQT/MON for Persian). If none of a node's references is accessible, say so.
79	
80	Add to every node a `ref_check` array:
81	
82	```json
83	"ref_check": [
84	  {"ref": "KLN:164", "status": "supports", "note": "Klein s.v. 'cherub': Heb. kerūbh, prob. rel. to Akkad. karābu 'to bless', metathesis of b-r-k — exactly Nourai's claim."},
85	  {"ref": "FVQ:75", "status": "not_checked", "note": "no online copy"}
86	]
87	```
88	
89	`status` ∈ `supports` (the page says what the arrow says) · `partial` (the reference has the
90	word but a different/looser derivation) · `contradicts` (the reference says something else)
91	· `not_found` (checked the text, could not find the entry/page) · `not_checked` (reference
92	not accessible online). Quote the key phrase of the reference in `note` when you can.
93	
94	Also add to each entry a root-level `ref_check` for the root's own refs (e.g. `POK:244`).
95	
96	
97	## Process documentation (required)
98	
99	The owner wants to be able to audit every step later. Therefore:
100	
101	- **Every web page you rely on must be archived**: after you read a page (WebFetch or
102	  curl), run
103	  `python3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
104	  This stores the page as text under `data/verification/sources/web/` and indexes it. Only
105	  URLs that were archived this way may appear in a `sources` array. (Batch several calls in
106	  one Bash command to save time.)
107	- **Every lookup in a local reference text must be quoted**: in `ref_check[].note` include
108	  the exact phrase(s) you found (with the grep pattern or page you used, e.g.
109	  "KLN.txt p.164 (ff-page 178): 'cherub … prob. rel. to Akkad. karābu'"), so the finding can
110	  be re-run.
111	- Your full transcript (every tool call and result) is exported automatically by the
112	  coordinator; nothing else needed for that.
113	
114	
115	## Use EVERY relevant book on disk (required)
116	
117	Checking only the reference Nourai cites is not enough. For every node, also consult the
118	other books in the local library that could speak to that claim, and record what each says.
119	The list of which books cover which kind of node, with file paths, is
120	`/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md`
121	(also `data/verification/sources/SOURCE_MATRIX.md`). Minimum per node:
122	
123	- an Indo-European node or root box: Pokorny (POK) AND Walde-Pokorny (WLD) AND Watkins/AHD,
124	  plus Mann (IEC) or Buck (SYN) when the word is a common noun;
125	- an Avestan / Old Persian node: Bartholomae (BRT) or Kent (KNT);
126	- a Pahlavi / Middle Persian node: MacKenzie (PHD) and Nyberg (NYB);
127	- a New Persian node: Horn (HRN), Hübschmann (HUB), Cheung (CHEUNG, for verbs), Borhan-e
128	  Qate' with Mo'in's footnotes (BQT), Mo'in (MON), and Aryanpur (ARY, once its text exists);
129	- a Sogdian node: Gharib (SOD); a Khotanese one: Bailey (ISS_alt_DKS);
130	- an Arabic node or a Persian/Arabic loan in either direction: Klein (KLN), Jeffery (FVQ),
131	  Addi Shir (AFM), Asbaghi (PLA), Fraenkel (AFA), Lokotsch (LKT); for French/Spanish
132	  Arabisms Pihan (PHN), Devic (DEV), Lammens (LAM), Dozy (DOZ);
133	- an English / Romance node: Klein (KLN), Skeat (SKT), Funk & Wagnalls (FSD), Webster (WEB);
134	  Anglo-Indian words: Hobson-Jobson (HJB), Whitworth (AID);
135	- a Turkic node: Vámbéry (TTS), Lokotsch (LKT).
136	
137	Grep each file for the headword (several spellings; Latin transliteration for the Western
138	books, Persian script for BQT/MON/ARY, Pahlavi transliteration for PHD/NYB). A grep that
139	finds nothing is also a result ("silent"). Record everything in a `consulted` array on the
140	node (separate from `ref_check`, which is only for the references Nourai himself cites):
141	
142	```json
143	"consulted": [
144	  {"src": "HRN", "where": "no. 3, p. 1", "stance": "contradicts", "note": "Horn separates āb 'Glanz' from āb 'water' and derives āftāb from the former"},
145	  {"src": "PHD", "where": "p. 5 s.v. ābād", "stance": "supports", "note": "'ābād [ʾpʾt] populous, thriving' — no water element"},
146	  {"src": "WLD", "where": "Bd. I p. 46", "stance": "silent", "note": "root ap- listed, no Persian compound"}
147	]
148	```
149	
150	`stance` ∈ supports / contradicts / partial / silent. Quote the key phrase. Books consulted
151	via the web (vajehyab for Mo'in, AHD online) go here too, with the URL archived via
152	fetch_source.py and listed in `sources`. Every node must have at least two `consulted`
153	entries from different books whenever the matrix lists two or more books for its language.
154	
155	## Sources to use (in roughly this order)
156	
157	- **Wiktionary** (en.wiktionary.org) — has the best coverage of Persian, Middle Persian,
158	  Avestan, Old Persian, Sogdian, Arabic etymologies, with citations (Cheung 2007, Hasandust,
159	  MacKenzie 1971, Bartholomae, Horn, Hübschmann, Nourai himself). Fetch the word's page AND
160	  the `Reconstruction:Proto-Indo-European/…` / `Reconstruction:Proto-Iranian/…` pages.
161	  Use URL-encoded Persian/Arabic script for those pages.
162	- **Etymonline** (etymonline.com/word/<word>) for English/French/Latin/Greek chains.
163	- **American Heritage Dictionary IE roots** (ahdictionary.com/word/indoeurop.html or
164	  ahdictionary.com/word/search.html?q=<root>) — Nourai's "AHD" citations refer to the 1975
165	  appendix; the online appendix is the updated edition of the same list.
166	- **Pokorny** — via indo-european.info, starlingdb.org, or Wiktionary's Pokorny citation;
167	  Nourai's "POK:nnn" is a page number in Pokorny's IEW.
168	- **Klein's Comprehensive Etymological Dictionary** (KLN) and **Horn's Grundriss der
169	  neupersischen Etymologie** (HRN), **Hübschmann's Persische Studien** (HUB),
170	  **MacKenzie's Concise Pahlavi Dictionary** (PHD), **Bartholomae AiW** (BRT) are on archive.org
171	  if needed for a hard case.
172	- **Encyclopaedia Iranica** (iranicaonline.org) for historical/cultural routes.
173	- **Nişanyan Sözlük** (nisanyansozluk.com) for Turkish; **Lisān al-ʿArab** / Wiktionary for Arabic.
174	- Use WebSearch when you don't know the right page; use WebFetch to read a page.
175	
176	Do NOT fabricate sources. If a page did not load or didn't help, don't cite it.
177	If a chain is well known and uncontroversial (e.g. Latin → Old French → English), one good
178	source covering the chain is enough; spend your effort on the Iranian and Semitic links,
179	which are where errors are likelier.
180	
181	## Output — write ONE file per page
182	
183	Write `/home/sfmqrb/git/rishe/data/verification/page-<pdf>.json` (UTF-8, no BOM):
184	
185	```json
186	{
187	  "pdf_page": 126,
188	  "book_page": 96,
189	  "verified_by": "claude-fable-5-1",
190	  "verified_on": "2026-09-04",
191	  "entries": [
192	    {
193	      "entry": 0,
194	      "root": "Dheigh, Dhigha",
195	      "verdict": "confirmed",
196	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
197	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
198	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
199	      "nodes": [
200	        {
201	          "id": 6,
202	          "lang": "Avestan",
203	          "words": "pairi-daeza",
204	          "verdict": "confirmed",
205	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' (PIE *dʰeyǵʰ-, o-grade *dʰoyǵʰ-o- > Iranian *daiza-). Attested in the Vidēvdād (pairi-daēzaiiąn) …",
206	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza", "https://www.etymonline.com/word/paradise"]
207	        },
208	        {
209	          "id": 9,
210	          "lang": "Greek",
211	          "words": "paradeisos",
212	          "verdict": "confirmed",
213	          "derivation": "Borrowed from Old Iranian *paridaiza- (Median/Old Persian form with -d-, cf. Elamite par-te-taš, Akkadian pardēsu) in the 5th c. BCE; first in Xenophon (Anabasis 1.2.7) for the Persian kings' walled hunting parks. Greek -ei- renders Iranian /ai/ ~ /ē/; -os is the Greek nominative ending. The Septuagint (3rd c. BCE) used it for the Garden of Eden, whence the 'heaven' sense.",
214	          "sources": ["https://en.wiktionary.org/wiki/παράδεισος"]
215	        }
216	      ]
217	    }
218	  ]
219	}
220	```
221	
222	Rules:
223	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
224	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
225	- `words` = the transliterations of the node joined by "; " (copy from the chart).
226	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
227	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
228	- Keep `note` on the entry for root-level comments and for anything cross-cutting
229	  (e.g. "Nourai's whole Semitic branch here is rejected by Klein …").
230	- If a node lists several words, cover each word; if they differ in verdict, use the worst
231	  verdict for the node and explain per word in `derivation`.
232	- Where the chart's own NOTE already records a dispute (e.g. "POK:694 derives Latin mattus
233	  from root Mad"), evaluate it: say which side modern scholarship takes.
234	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted` (array).
235	- Valid JSON only. Test it with `python3 -m json.tool` before finishing.
236	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
237	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason).
238	  Do not paste the JSON back into your reply.
239	
```


## [2026-09-04T18:07:12.906Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-33.txt"
}
```


### [2026-09-04T18:07:12.920Z] TOOL RESULT

```
1	=== PDF page 33 (book page 3) ===
2	--- entry 0 ---
3	ROOT [Semitic] Ab 2 : father  (refs FVQ:44; KLN:6)
4	#1 (parent #0) [Arabic] refs=FVQ:44; FVA:25; LKT:44 | ab, abŭ, a.b.v : father
5	  #2 (parent #1) [Persian] refs=FVA:25; MON | abŭ «آبو ( ابوی )» : father | extra: ابوعلی سینا ، ابوالفضل ، ابوالقاسم ، ابوالحسن ، ابوالفتح ، بوالهوس
6	  #3 (parent #1) [Arabic] refs=FVQ:44; FVA:25; LKT:44; AHD:152 | abŭ-zînâ : "father of whoredom" referring to gibbons ☞Z.n.y ; abŭ-araq : "father of sweat", a spicy plant used in medicine ☞A.r.q
7	    #4 (parent #3) [Persian] refs=MON:602; FVA:180 | bŭzîneh «بوزینه ( بوزنه )» : gibbon
8	      #5 (parent #4) [Hindustani] refs=PRT:253 | bojîna
9	        #6 (parent #5) [French] refs=KLN:655 |  | NOTE: This monkey was taken to France from India in the 18th century.
10	          #7 (parent #6) [English] refs=KLN:655 | gibbon
11	    #8 (parent #3) [Middle Latin] refs=AHD:152 | borrâco
12	      #9 (parent #8) [Old French] refs=AHD:152 | borrace, bourrache
13	        #10 (parent #9) [English] refs=AHD:152 | borage : a spicy salad seasoning
14	#11 (parent #0) [Hebrew] refs=KLN:6 | abh : father
15	  #12 (parent #11) [English] refs=KLN:6 | Abot
16	  #13 (parent #11) [Hebrew] refs=FVQ:44; KLN:6 | Abh-raham : father of the multitude (Abraham) ; Abh-ram : high father (Abram) ; Abh-ner : my father is light (Abner) ☞N.w.r ; Ab-šalom : father is peace (Absalom) ☞S.l.m ; Abh-igayil : father is rejoicing (Abigail) ; Yo-abh : the Lord is his father (Joab)
17	    #14 (parent #13) [Arabic] refs=FVQ:44 | Abrahim : Abraham
18	      #15 (parent #14) [Persian] refs=None | Ebrâhîm «ابراهیم»
19	    #16 (parent #13) [English] refs=KLN; AHD | Abraham, Abram, Abner, Absalom, Abigail, Jaob
20	
```


## [2026-09-04T18:07:13.419Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-33.json"
}
```


### [2026-09-04T18:07:13.460Z] TOOL RESULT

```
1	{
2	  "pdf_page": 33,
3	  "book_page": 3,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Ab 2",
8	        "lang": "Semitic",
9	        "refs": "FVQ:44; KLN:6",
10	        "gloss": "father"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Arabic",
17	          "refs": "FVQ:44; FVA:25; LKT:44",
18	          "words": [
19	            {"translit": "ab, abŭ, a.b.v", "gloss": "father", "script": null}
20	          ],
21	          "note": null,
22	          "quote": null
23	        },
24	        {
25	          "id": 2,
26	          "parent": 1,
27	          "lang": "Persian",
28	          "refs": "FVA:25; MON",
29	          "words": [
30	            {"translit": "abŭ", "gloss": "father", "script": "آبو ( ابوی )"}
31	          ],
32	          "script_extra": "ابوعلی سینا ، ابوالفضل ، ابوالقاسم ، ابوالحسن ، ابوالفتح ، بوالهوس",
33	          "note": null,
34	          "quote": null
35	        },
36	        {
37	          "id": 3,
38	          "parent": 1,
39	          "lang": "Arabic",
40	          "refs": "FVQ:44; FVA:25; LKT:44; AHD:152",
41	          "words": [
42	            {"translit": "abŭ-zînâ", "gloss": "\"father of whoredom\" referring to gibbons", "script": null, "see": ["Z.n.y"]},
43	            {"translit": "abŭ-araq", "gloss": "\"father of sweat\", a spicy plant used in medicine", "script": null, "see": ["A.r.q"]}
44	          ],
45	          "note": null,
46	          "quote": null
47	        },
48	        {
49	          "id": 4,
50	          "parent": 3,
51	          "lang": "Persian",
52	          "refs": "MON:602; FVA:180",
53	          "words": [
54	            {"translit": "bŭzîneh", "gloss": "gibbon", "script": "بوزینه ( بوزنه )"}
55	          ],
56	          "note": null,
57	          "quote": {
58	            "text": "چون دل بوزینه گردد آن دلش - از دل بوزینه شد خوار آن گلش",
59	            "poet": "Molavî"
60	          }
61	        },
62	        {
63	          "id": 5,
64	          "parent": 4,
65	          "lang": "Hindustani",
66	          "refs": "PRT:253",
67	          "words": [
68	            {"translit": "bojîna", "gloss": null, "script": null}
69	          ],
70	          "note": null,
71	          "quote": null
72	        },
73	        {
74	          "id": 6,
75	          "parent": 5,
76	          "lang": "French",
77	          "refs": "KLN:655",
78	          "words": [],
79	          "note": "This monkey was taken to France from India in the 18th century.",
80	          "quote": null
81	        },
82	        {
83	          "id": 7,
84	          "parent": 6,
85	          "lang": "English",
86	          "refs": "KLN:655",
87	          "words": [
88	            {"translit": "gibbon", "gloss": null, "script": null}
89	          ],
90	          "note": null,
91	          "quote": null
92	        },
93	        {
94	          "id": 8,
95	          "parent": 3,
96	          "lang": "Middle Latin",
97	          "refs": "AHD:152",
98	          "words": [
99	            {"translit": "borrâco", "gloss": null, "script": null}
100	          ],
101	          "note": null,
102	          "quote": null
103	        },
104	        {
105	          "id": 9,
106	          "parent": 8,
107	          "lang": "Old French",
108	          "refs": "AHD:152",
109	          "words": [
110	            {"translit": "borrace, bourrache", "gloss": null, "script": null}
111	          ],
112	          "note": null,
113	          "quote": null
114	        },
115	        {
116	          "id": 10,
117	          "parent": 9,
118	          "lang": "English",
119	          "refs": "AHD:152",
120	          "words": [
121	            {"translit": "borage", "gloss": "a spicy salad seasoning", "script": null}
122	          ],
123	          "note": null,
124	          "quote": null
125	        },
126	        {
127	          "id": 11,
128	          "parent": 0,
129	          "lang": "Hebrew",
130	          "refs": "KLN:6",
131	          "words": [
132	            {"translit": "abh", "gloss": "father", "script": null}
133	          ],
134	          "note": null,
135	          "quote": null
136	        },
137	        {
138	          "id": 12,
139	          "parent": 11,
140	          "lang": "English",
141	          "refs": "KLN:6",
142	          "words": [
143	            {"translit": "Abot", "gloss": null, "script": null}
144	          ],
145	          "note": null,
146	          "quote": null
147	        },
148	        {
149	          "id": 13,
150	          "parent": 11,
151	          "lang": "Hebrew",
152	          "refs": "FVQ:44; KLN:6",
153	          "words": [
154	            {"translit": "Abh-raham", "gloss": "father of the multitude (Abraham)", "script": null},
155	            {"translit": "Abh-ram", "gloss": "high father (Abram)", "script": null},
156	            {"translit": "Abh-ner", "gloss": "my father is light (Abner)", "script": null, "see": ["N.w.r"]},
157	            {"translit": "Ab-šalom", "gloss": "father is peace (Absalom)", "script": null, "see": ["S.l.m"]},
158	            {"translit": "Abh-igayil", "gloss": "father is rejoicing (Abigail)", "script": null},
159	            {"translit": "Yo-abh", "gloss": "the Lord is his father (Joab)", "script": null}
160	          ],
161	          "note": null,
162	          "quote": null
163	        },
164	        {
165	          "id": 14,
166	          "parent": 13,
167	          "lang": "Arabic",
168	          "refs": "FVQ:44",
169	          "words": [
170	            {"translit": "Abrahim", "gloss": "Abraham", "script": null}
171	          ],
172	          "note": null,
173	          "quote": null
174	        },
175	        {
176	          "id": 15,
177	          "parent": 14,
178	          "lang": "Persian",
179	          "refs": null,
180	          "words": [
181	            {"translit": "Ebrâhîm", "gloss": null, "script": "ابراهیم"}
182	          ],
183	          "note": null,
184	          "quote": {
185	            "text": "بت شکستی گیرم ابراهیم وار - کو بت تن را فدا کردن به نار",
186	            "poet": "Molavî"
187	          }
188	        },
189	        {
190	          "id": 16,
191	          "parent": 13,
192	          "lang": "English",
193	          "refs": "KLN; AHD",
194	          "words": [
195	            {"translit": "Abraham, Abram, Abner, Absalom, Abigail, Jaob", "gloss": null, "script": null}
196	          ],
197	          "note": null,
198	          "quote": null
199	        }
200	      ]
201	    }
202	  ]
203	}
204	
```


## [2026-09-04T18:07:14.015Z] TOOL CALL #4: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md"
}
```


### [2026-09-04T18:07:14.036Z] TOOL RESULT

```
1	# Source matrix — which local books to grep for each kind of node
2	
3	All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.
4	
5	ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).
6	
7	
8	## Indo-European roots (any IE node, root boxes)
9	
10	- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
11	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt`
12	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt`
13	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt`
14	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt`
15	- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
16	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt`
17	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
18	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
19	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
20	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
21	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
22	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
23	- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
24	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt`
25	- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
26	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt`
27	- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
28	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt`
29	- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
30	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
31	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
32	- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
33	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt`
34	- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
35	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt`
36	- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
37	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt`
38	- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
39	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
40	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
41	
42	## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian
43	
44	- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
45	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt`
46	- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
47	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt`
48	- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
49	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt`
50	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD_mackenzie.txt`
51	- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
52	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt`
53	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt`
54	- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
55	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt`
56	- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
57	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt`
58	- **CHEUNG** — CHEUNG
59	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/CHEUNG.txt`
60	- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
61	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt`
62	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt`
63	- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
64	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt`
65	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt`
66	- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
67	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_alt_v1.txt`
68	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_dli_part1.txt`
69	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt`
70	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt`
71	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt`
72	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt`
73	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
74	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
75	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
76	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
77	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
78	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
79	- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
80	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt`
81	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt`
82	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
83	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
84	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
85	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
86	- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
87	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt`
88	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt`
89	- **FSF** — Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/
90	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt`
91	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt`
92	- **HENNING** — HENNING
93	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HENNING_selected_papers.txt`
94	- **EAV** — J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869
95	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/EAV_studies.txt`
96	- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
97	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ISS_alt_DKS.txt`
98	- **AHM** — I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
99	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt`
100	- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
101	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
102	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
103	- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
104	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf`
105	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt`
106	- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
107	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf`
108	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt`
109	- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
110	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AVG.txt`
111	- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
112	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HID.txt`
113	- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
114	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf`
115	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt`
116	- **TLM** — H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Seri
117	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TLM.txt`
118	- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
119	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/UNV.txt`
120	- **SBK** — M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
121	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SBK.txt`
122	
123	## Semitic / Arabic loans in either direction
124	
125	- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
126	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
127	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
128	- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
129	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt`
130	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt`
131	- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
132	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt`
133	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt`
134	- **PLA** — A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
135	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf`
136	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt`
137	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt`
138	- **AFA** — S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)
139	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt`
140	- **TAD** — Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-huru
141	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt`
142	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt`
143	- **ARB** — al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edi
144	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt`
145	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt`
146	- **KFL** — Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885
147	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KFL.txt`
148	- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
149	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
150	- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
151	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt`
152	- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
153	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt`
154	- **LAM** — H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890
155	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt`
156	- **DOZ** — R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeu
157	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt`
158	- **AKD** — H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
159	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt`
160	- **SIN** — B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)
161	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt`
162	- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
163	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt`
164	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt`
165	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
166	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
167	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
168	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
169	- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
170	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_alt_v1.txt`
171	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_dli_part1.txt`
172	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt`
173	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt`
174	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt`
175	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt`
176	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
177	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
178	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
179	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
180	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
181	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
182	
183	## English / Romance / Germanic
184	
185	- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
186	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
187	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
188	- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
189	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt`
190	- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
191	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt`
192	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt`
193	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt`
194	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt`
195	- **WEB** — Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)
196	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt`
197	- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
198	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt`
199	- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
200	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt`
201	- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
202	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt`
203	- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
204	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt`
205	- **RCH** — J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1
206	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt`
207	- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
208	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
209	- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
210	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt`
211	- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
212	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt`
213	- **NAT** — C. Berlitz, Native Tongues, New York 1982
214	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NAT_2005.txt`
215	- **PEI** — M. Pei, The Families of Words, New York 1962
216	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PEI.txt`
217	
218	## Turkic / Mongolian
219	
220	- **TTS** — H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)
221	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt`
222	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf`
223	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt`
224	- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
225	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
226	- **VIE** — M.A. Sajjadiyyeh, Vazheha-ye Irani dar Zaban-e Engelisi, Bonyad-e Neyshabur 1364/1985
227	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_pages.txt`
228	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_sajjadieh1364_parsianjoman.pdf`
229	
230	## Sanskrit / Hindustani
231	
232	- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
233	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt`
234	- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
235	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt`
236	- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
237	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt`
238	- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
239	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt`
240	- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
241	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt`
242	- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
243	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt`
```


## [2026-09-04T18:07:18.782Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['FVQ','KLN','FVA','LKT','MON','AHD','PRT']:\n    print(k, d.get(k))\n\"\n"
}
```


## [2026-09-04T18:07:19.450Z] TOOL CALL #6: Bash

```json
{
 "command": "grep -n -i -E '^FVA|^PRT|^LKT|^FVQ|^AHD|^KLN|^MON' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt | head -50"
}
```


### [2026-09-04T18:07:20.284Z] TOOL RESULT

```
FVQ {'title': "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", 'kind': 'archive_djvu', 'url': 'https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)', 'lookup_hint': 'Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).', 'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'], 'page_offset': 'printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)', 'covers_etymology': True, 'notes': 'Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.', 'cites': 'page number of Jeffery, The Foreign Vocabulary of the Qurʾān (1938)'}
KLN {'title': 'E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67', 'edition_found': "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", 'kind': 'archive_djvu', 'url': 'https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein', 'identifier': 'a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt', 'page_offset': 'KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", 'notes': 'Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)', 'local_files': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt'], 'cites': 'page number, continuous across the two volumes (1966–67)'}
FVA {'title': 'S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989', 'kind': 'catalog', 'url': 'https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)', 'lookup_hint': 'Searched archive.org, ketabnak, noorlib, web: no digital copy found.', 'local_file': None, 'page_offset': None, 'covers_etymology': True, 'notes': "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام\u200cواژه\u200cهای عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}
LKT {'title': 'K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927', 'edition_found': '1927', 'kind': 'archive_djvu', 'url': 'https://archive.org/details/etymologische00lokoguat', 'identifier': 'etymologische00lokoguat', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt', 'page_offset': 'leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.", 'notes': '', 'cites': 'entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)'}
MON {'title': "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", 'kind': 'website+archive_djvu', 'url': 'https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)', 'lookup_hint': "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", 'local_file': ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'], 'page_offset': None, 'covers_etymology': True, 'notes': "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم\u200cها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).", 'cites': "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"}
AHD {'title': "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", 'edition_found': 'Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)', 'kind': 'archive_djvu+website+archive_restricted', 'url': 'https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only', 'identifier': 'watkins-american-heritage-dictionary-of-indo-european-roots-1985', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt', 'page_offset': "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", 'lookup_hint': "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).", 'notes': 'AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.', 'cites': 'page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)'}
PRT {'title': 'E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958', 'edition_found': '1958 (lending-only copies)', 'kind': 'archive_restricted', 'url': 'https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending', 'identifier': 'originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)', 'local_file': None, 'page_offset': None, 'lookup_hint': 'Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q=<word>. Entries are alphabetical with numbered sub-senses.', 'notes': "RE-SEARCH 2026-09: 8 lending copies on archive.org, none open; HathiTrust search-only; Google no view. Borrow the 1958 copy to match Nourai's pagination."}
```


### [2026-09-04T18:07:20.334Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:07:47.662Z] TOOL CALL #7: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/tools/verify_check.py 2>/dev/null | head -100"
}
```


### [2026-09-04T18:07:47.704Z] TOOL RESULT

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


## [2026-09-04T18:07:48.340Z] TOOL CALL #8: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/tools/ | grep -i fetch; cat /home/sfmqrb/git/rishe/tools/fetch_source.py 2>/dev/null | head -60"
}
```


### [2026-09-04T18:07:48.388Z] TOOL RESULT

```
fetch_source.py
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


## [2026-09-04T18:07:56.117Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 : ab/abu father ===\"\ngrep -n \"^ab,\" KLN_1966.txt | head -5\ngrep -n -i \"father'\" KLN_1966.txt | head -5\necho \"=== KLN gibbon ===\"\ngrep -n -i \"^gibbon\" KLN_1966.txt\necho \"=== KLN borage (in AHD block, but check KLN too) ===\"\ngrep -n -i \"^borage\" KLN_1966.txt\necho \"=== KLN Abraham ===\"\ngrep -n -i \"^abraham\" KLN_1966.txt\necho \"=== KLN abh/Hebrew father ===\"\ngrep -n -i \"'father'\" KLN_1966.txt | head -10\n"
}
```


### [2026-09-04T18:07:56.239Z] TOOL RESULT

```
=== KLN 1966 : ab/abu father ===
26126:ab,  MHG.  abe,  ab,  G.  ab,  ‘off,  from,  down’, Goth,  af,  ‘away  from’,  cogn.  with  OI.  dpa, Avestic  apa,  ‘away  from’,  Hitt,  apa,  ‘behind’, Gk.  atro,  ‘away  from,  from’,  L.  ab,  ‘away  from, from’  (orig.  *ap,  cp.  ap-erio,  ‘I  open’),  Alb. prape  (for  *  per- apt),  ‘back,  again’,  Lith.  apacid, Lett,  apaksa,  ‘the  lower  part’.  Cp.  off,  ebb.  Cp. also  ab-,  apo-,  post-, of-,  assimilated  form  of  ob-  before /. off,  adv.,  prep,  and  adj.  —  The  stressed  form  of of.  Cp.  offal,  offing,  offish,  and  the  second  ele¬ ment  in  doff.
2807:anile,  adj.,  like  an  old  woman.  —  L.  anilis,  ‘per¬ taining  to  an  old  woman’,  fr.  anus,  gen.  anus, ‘old  woman',  from  the  I.-E.  imitative  base  *an-, whence  also  Hitt,  annash,  ’mother’,  hannash, ‘grandmother’,  Gk.  avvip,  ‘grandmother’, Lith.  ahyta,  ‘mother-in-law’,  OPruss.  ane,  ‘old mother’,  OHG.  ano,  MHG.  ane,  an,  ‘grand¬ father,  great  grandfather’,  OHG.  ana,  ‘grand¬ mother,  great  grandmother’,  G.  Ahnen,  ‘ances¬ tors’,  OHG.  eninchili  (whence  MHG.  eninkel, enenkel,  G.  Enkel),  ‘grandson’,  prop,  dimin. of  OHG.  ano,  ‘great  grandfather'.  Cp.  the  first element  in  Olaf.
10196:Dacus,  n.,  a  genus  of  flies,  the  olive  fly  ( entomol .) —  ModL.,  fr.  Gk.  Saxo?,  ‘any  animal,  the  bite of  which  is  dangerous’,  lit.  ‘a  biting  animal’, rel.  to  Saxveiv,  ‘to  bite’,  8a£,  ‘biting’,  8rjy[za,  ‘a biting’,  8f]XTr)s,  ‘biter’,  fr.  I.-E.  base  *denk -, ‘to  bite’,  whence  also  OI.  ddsati  (for  *di}keti), ‘bites’,  ON.  tong,  OE.  tang,  tange,  ‘tongs’.  See tongs  and  cp.  the  second  element  in  carpodacus, Tridacna,  Demodex,  Mixodectes. dad,  daddy,  n.,  father.  —  A  child’s  word.  Cp. W.  tad,  dad ,  Ir.  daid,  Co.  tat,  ‘father’,  hendat, ‘grandfather’,  Czech  tata,  Russ,  tdta,  Lith. let  is,  tete,  'father',  OPruss.  thetis,  ‘father,  old man’,  Ir.  daid,  Co.  tat,  W.,  Bret,  tad,  tat,  ‘father’, Alb.  tats,  ‘father’,  L.  tata,  ‘father’,  Gk.  toct<x, ‘father’,  tol-ol,  tettx,  ‘O  father,  daddy’,  xaxa- Xt^etv,  ‘to  flatter’,  ModGk.  Sa8a?,  ‘father’,  OI. tatah,  ‘father,  son’,  which  all  are  of  childish origin.
=== KLN gibbon ===
16112:gibbon,  n.,  a  small,  long-armed  ape.  —  F.,  a  name of  Indian  origin  brought  to  Europe  by  the Marquis  Joseph-Frangois  Dupleix  (1697-1763), governor-general  of  the  French  possessions  in India  (1742-54).
=== KLN borage (in AHD block, but check KLN too) ===
=== KLN Abraham ===
1217:Abraham,  masc.  PN. ;  in  the  Bible,  the  first  of  the patriarchs  and  father  of  the  Hebrew  nation.
=== KLN abh/Hebrew father ===
10196:Dacus,  n.,  a  genus  of  flies,  the  olive  fly  ( entomol .) —  ModL.,  fr.  Gk.  Saxo?,  ‘any  animal,  the  bite of  which  is  dangerous’,  lit.  ‘a  biting  animal’, rel.  to  Saxveiv,  ‘to  bite’,  8a£,  ‘biting’,  8rjy[za,  ‘a biting’,  8f]XTr)s,  ‘biter’,  fr.  I.-E.  base  *denk -, ‘to  bite’,  whence  also  OI.  ddsati  (for  *di}keti), ‘bites’,  ON.  tong,  OE.  tang,  tange,  ‘tongs’.  See tongs  and  cp.  the  second  element  in  carpodacus, Tridacna,  Demodex,  Mixodectes. dad,  daddy,  n.,  father.  —  A  child’s  word.  Cp. W.  tad,  dad ,  Ir.  daid,  Co.  tat,  ‘father’,  hendat, ‘grandfather’,  Czech  tata,  Russ,  tdta,  Lith. let  is,  tete,  'father',  OPruss.  thetis,  ‘father,  old man’,  Ir.  daid,  Co.  tat,  W.,  Bret,  tad,  tat,  ‘father’, Alb.  tats,  ‘father’,  L.  tata,  ‘father’,  Gk.  toct<x, ‘father’,  tol-ol,  tettx,  ‘O  father,  daddy’,  xaxa- Xt^etv,  ‘to  flatter’,  ModGk.  Sa8a?,  ‘father’,  OI. tatah,  ‘father,  son’,  which  all  are  of  childish origin.
```


## [2026-09-04T18:07:57.209Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD borage ===\"\ngrep -n -i \"^borage\" AHD_watkins1985.txt\ngrep -n -i \"borage\" AHD_watkins1985.txt\necho \"=== AHD gibbon ===\"\ngrep -n -i \"gibbon\" AHD_watkins1985.txt\n"
}
```


### [2026-09-04T18:07:57.277Z] TOOL RESULT

```
=== AHD borage ===
=== AHD gibbon ===
```


## [2026-09-04T18:07:58.075Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ ab / abu ===\"\ngrep -n -i \"^ab[ ,\\.]\" FVQ.txt | head -20\ngrep -n -i \"abu\" FVQ.txt | head -20\n"
}
```


### [2026-09-04T18:07:58.153Z] TOOL RESULT

```
=== FVQ ab / abu ===
28:THE FOREIGN VOCABULARY 
35:FOREIGN VOCABULARY 
80:bee^n made of the vocabulary of the Qur'an. It is interesting to note 
84:vocabulary. The Qur'an is the first Arabic book, for though there 
100:the vocabulary of the Qur'an. Meanwhile this present Essay attempts 
102:of the non-Arabic elements in the Qur'anic vocabulary. 
109:through intercourse there was a natural interchange of vocabulary. 
172:important task of investigation of the Qur'anic vocabulary. 
193:Aghani. Kitdb al-Aghdni of Abu'l-Faraj al-Isfahani, 20 vols. Cairo, 1868. 
226:Cheikho, L. An-Nasraniya wa Adabuha bain 'Arab al-Jahiliyya. Beirut, 1912-1923. 
260:Fraenkel, S. De Vocabulis in antiquis Arabum carminibus et in Corano peregrinis. 
740:religious vocabulary, but also most of the cultural vocabulary of the 
909:of Abu 'TJbaida 8 as given by al-Hasan -"I heard Abu 'Ubaida say 
940:Abu 'Ubaida Ma'mar b. al-Muthanna, the great Humanist of the reign of Harun 
955:Shafi'i, 1 and Ibn Jarlr, 2 and Abu 'Ubaida, and the Qacji Abu Bakr, 3 
990:2 This is at-Tabarl, the well-known commentator, whoso full name was Abu Ja'far 
995:3 This is in all probability the QadT Abu Bakr al-Baqilanl whose book ^l ^ill j^I 
998:4 Abu'l-Husain Ahmad b. Faris of Qazwin, also very frequently quoted by 
1031:was lacking in the necessary religious vocabulary, and that Allah 
1105:peoples would have borrowed vocabulary from the Arabs than that
```


## [2026-09-04T18:08:04.792Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==62' FVQ_pages.txt | head -100\n"
}
```


## [2026-09-04T18:08:05.319Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page\" FVQ_pages.txt | sed -n '55,65p'\n"
}
```


### [2026-09-04T18:08:06.439Z] TOOL RESULT

```
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
```


### [2026-09-04T18:08:06.485Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:08:12.001Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==63' FVQ_pages.txt | head -80\n"
}
```


### [2026-09-04T18:08:13.670Z] TOOL RESULT

```
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


## [2026-09-04T18:08:26.760Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==61' FVQ_pages.txt | head -60\necho \"---page 42 (leaf 60)---\"\nawk 'BEGIN{RS=\"\\f\"} NR==60' FVQ_pages.txt | tail -40\n"
}
```


### [2026-09-04T18:08:28.377Z] TOOL RESULT

```
THE FOREIGN WORDS
1,1 (066).

Ixxx, 31.
Herbage.
It occurs only in an early Meccan passage describing the good
things GT)d has caused to grow on the earth by sending down rain.
The early authorities in Islam were puzzled by the word as is evident
from the discussion by Tab. on the verse, and the uncertainty evidenced
by Zam. and Baid. in their comments, an uncertainty which is shared
by the Lexicons (cf. LA, i, 199; Ibn al-Athir, Nihaya, i, 10), and
particularly by the instructive story given in Bagh, vii, 175. as-Suyuti,
Itq, 318, quotes Shaidhala as authority for its being a foreign word
meaning grass in the language of <^^*5 1 Jj&i, by which, as we gather
from the Mutaw, 65, he means the Berber tongue.
There can be little doubt that it is the Aram. JO^N (----- !"Q3K of
Dan. iv, 9, where the Dagesh forte is resolved into Nun). The NITK
of the Targums is the equivalent of Heb. 3K from 33X to be green
(cf. Cant, vi, 11 ; Job viii, 12). Fraenkel, Vocab, 24, thought that the
Arabia word was a direct borrowing from the Targumic fcO^X but tin*
probabilities seem in favour of its coming rather from Syr. JO|,
meaning quicquid terra producil (Mingana, Kyriac Influence, 88).
It was probably an early borrowing from the Mesopotamia!! area. 1
- '>
jjbl (ubabll).
cv, 3.
In the description of the rout of the Army of the Klephant we
-- ^ ^ ^ s ^ ^
ad <U u I \*Jb '(*i&> Jf-*jl3 where J,X 11 is said to mean
.... ..
flocks -jjfl j>- Zam., or Olp" Hugh, and to be the plu. of
which KhafajT, Shi/a, 31, lists as a foreign word whether spelled
AlU or 3flLjl or AJU1. The long account in LA, xiii, 5, makes it
clear that the philologers knew not what to make of the word.
1 Cf. Zimmorn, Akkudische, Frenidwvrter, p. 55.
43
---page 42 (leaf 60)---
```


## [2026-09-04T18:08:46.251Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==15' KLN_1966.txt | grep -n -i -A5 -B2 \"^ab\\b\\|abba\\|Abot\\|father\" | head -80\n"
}
```


## [2026-09-04T18:08:47.473Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor i in 13 14 15 16 17; do echo \"=== leaf $i ===\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | grep -n -i \"^ab\\b\\|^abba\\|^Abot\\|^abbot\\|father'\" ; done\n"
}
```


### [2026-09-04T18:08:47.792Z] TOOL RESULT

```
27-ablution,  n.,  a  washing,  esp.  as  a  ritual.  —  L.  ab- lutio,  gen.  -onis,  ‘a  washing,  cleansing’,  fr.  ab- lutus,  pp.  of  abluere,  ‘to  wash  off’,  fr.  ab-  and luere,  ‘to  wash’,  which  is  rel.  to  lavare,  ‘to  wash’. See  lave  and  -ion.
28-Derivative:  ablution-ary ,  adj. abnegate,  tr.  v.,  to  deny,  give  up.  —  L.  abnegdtus, pp.  of  abnegare,  ‘to  refuse,  deny’,  fr.  ab-  and negare,  ‘to  say  no,  deny’.  See  negate, abnegation,  n.  —  L.  abnegatio,  gen.  -onis,  ‘re¬ fusal,  denial’,  fr.  L.  abnegdtus,  pp.  of  abnegare. See  prec.  word  and  negation.
29:Abner,  n.,  masc.  PN.;  in  the  Bible,  commander of  Saul.  —  Heb.  Abhnir,  lit.  ‘my  father  is  light’, fr.  abh,  ‘father’,  and  ner,  ‘light’;  cp.  the  Baby¬
30:lonian  PN.  Abunuri.  For  the  first  element  see Aboth,  for  the  second  see  Menorah. abnormal,  adj.  — ■  A  blend  of  L.  abnormis  and ML.  anormalis,  this  latter  itself  being  a  blend of  L.  anomalus  and  normalis.  See  anomalous  and norm  and  cp.  anormal.
31-Derivatives:  abnormal-ity,  n.,  abnormal-ly,  adv., abnormal-ness,  n.
32-abnormity,  n.  —  L.  abnormitas,  formed  with  suff.
33--itas  fr.  abnormis.  See  prec.  word  and  -ity. aboard,  adv.  and  prep.  — •  Formed  fr.  a-,  ‘on’, and  board.
34-Abobra,  n.,  a  genus  of  plants  of  the  gourd  family (bot.)  —  ModL.,  fr.  Port,  abobora,  abobra, ‘gourd’,  fr.  L.  apopores,  apoperes  (see  Isidorus, XVII,  10,  16),  from  a  Hispanic  language. abodah,n.,  t)  service  in  the  Temple  in  Jerusalem; 2)  liturgy;  3)  name  of  the  seventeenth  bene¬ diction  of  the  Shemoneh  Esreh,  containing  the prayer  for  the  restoration  of  the  Temple  ( Jewish liturgy).  —  Heb.  ‘ abhodhd h,  ‘service’,  fr.  ‘ab- hadh,  ‘he  served,  worshiped’,  which  is  rel.  to Aram. -Syr.  ‘ dbhadh ,  Arab.  ‘ abada ,  'he  served, worshiped’,  Dgar.  ‘ bd ,  ‘to  serve,  worship’,  and to  Heb.  ‘ebhedh,  Aram,  'abhdii,  ‘slave,  servant, worshiper’,  Arab,  ‘abd,  ‘slave,  worshiper’.  Cp. Obadiah,  Obed.
35-abode,  n.,  dwelling  place.  —  Formed  from  the past  tense  of  abide.  See  next  word, abode,  v.,  past  tense  of  abide.  —  ME.  abood,  fr. OE.  abad,  past  tense  of  abidan.  See  abide  and cp.  prec.  word.
```


### [2026-09-04T18:08:49.460Z] TOOL RESULT

```
Exit code 1
=== leaf 13 ===
=== leaf 14 ===
10:abba,  n.,  title  of  honor.  —  L.,  fr.  Gk.  fr.
12:abbacy,  n.,  the  office  or  jurisdiction  of  an  abbot. —  Eccles.  L.  abbatia,  fr.  abbas,  gen.  abbatis.  See abbot  and  cp.  abba,  abbey.  Cp.  also  badia. abbe,  n.,  a  title  given  in  France  to  a  priest.  —  F., fr.  Eccles.  L.  abbatem,  acc.  of  abbas.  Cp.  It. abbate,  Sp.  abad,  ‘abbot’,  which  also  derive  fr. Eccles.  L.  abbatem,  and  see  abbot, abbess,  n.  • —  ME.  abbesse,  fr.  OF.  ( =  F.)  abbesse, fr.  Eccles.  L.  abbatissa,  fern,  of  abbas,  gen.  -at is. See  abbot  and  cp.  It.  abbadessa,  badessa,  and Sp.  abode sa,  ‘abbess’,  which  also  derive  fr.  Ec¬ cles.  L.  abbatissa.
=== leaf 15 ===
=== leaf 16 ===
=== leaf 17 ===
```


## [2026-09-04T18:09:03.502Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== Aboth ===\"\ngrep -n -i \"^aboth\" KLN_1966.txt\necho \"=== Abram/Absalom/Abigail/Joab ===\"\ngrep -n -i \"^abram\\|^absalom\\|^abigail\\|^joab\" KLN_1966.txt\necho \"=== context around Abraham line 1217 ===\"\nsed -n '1210,1230p' KLN_1966.txt\n"
}
```


### [2026-09-04T18:09:03.586Z] TOOL RESULT

```
=== Aboth ===
=== Abram/Absalom/Abigail/Joab ===
1219:Abram,  masc.  PN.;  in  the  Bible,  former  name  of Abraham.  —  Heb.  Abhrdm,  compounded  of abh,  ‘father’,  and  ram,  ‘high,  exalted’,  which  is prop.  part,  of  rum,  ‘to  be  high,  to  be  exalted  . For  the  first  element  see  Aboth  and  cp.  Abra¬ ham.  From  the  second  element  derive  ramd>', ‘height’  (prop.  fem.  part,  of  rum),  romdm,  ‘ex¬ tolling,  praise;  song  of  praise’,  mardm,  ‘height’, tlrumdh,  ‘contribution,  offering  (for  sacred use)’,  lit.  ‘something  lifted  up,  something  sep¬ arated’.  Cp.  Aram.-Syr.  ram,  ‘was  high’,  Arab. rdma  prop,  ‘he  rose',  hence  ‘he  strove  for’,  and, in  Zanzibar  and  Oman,  ‘he  was  able  to’.  Cp. the  second  element  in  Hiram.
1220:Abramis,  n.,  a  genus  of  fishes  ( ichthyol .) — ModL., fr.  Gk.  dppapit?,  ‘bream’,  fr.  Egyptian  rem, ‘fish’.
1236:Absalom,  masc.  PN. ;  in  the  Bible,  King  David  s son;  fig.  a  favorite  son.  —  Heb.  Abhshaldm,  lit. ‘father  is  peace’,  fr.  abh,  ‘father’,  and  shaldm, ‘peace’.  See  Aboth  and  shalom. abscess,  n„  a  swelling  in  body  tissues  (med.).  — L.  abscessus,  ‘a  going  away,  departure,  abscess  , fr.  abcedere,  ‘to  go  away’,  fr.  abs-,  ab-,  ‘away from,  from’,  and  cedere,  ‘to  go’.  See  ab-  and cede  and  cp.  cease.
20305:Joab,  1)  masc.  PN. ;  2)  in  the  Bible,  the  chief  cap¬ tain  of  David’s  army.  —  Late  L.  Joab,  fr.  Gk. ’lojafi,  fr.  Heb.  Yd'dbh ,  lit.  ‘the  Lord  is  (his) father’.  For  the  first  element  cp.  the  PN’s  Joel, John,  Jonathan,  Joshua,  for  the  second  see Aboth  and  cp.  words  there  referred  to.
=== context around Abraham line 1217 ===
Derivative:  about,  prep.
above
abstinent
6
7
above,  adv.  —  ME.  aboven,  fr.  OE.  abufan,  form¬ ed  fr.  a-,  ‘on’,  and  bufan,  ‘above’,  which  itself is  formed  fr.  be,  ‘by’  (see  by),  and  ufan,  ‘up¬ ward,  above’;  cp.  OE.  ofer,  ‘over’  which  is  the compar.  of  ufan,  and  see  over.  Cp.  also  about. Derivatives:  above,  prep,  and  adj. abracadabra,  n.,  a  magic  formula.  —  Late  L.,  fr. Gk.  dppao48oc(ipa,  in  which  word  the  letter  c  = s  was  misread  for  k.  It  was  originally  written as  a  magic  formula  on  Abraxas  Stones,  whence its  name.  See  abraxas.
abrade,  tr.  v.,  to  scrape  off.  —  L.  abradere,  ‘to scrape  off’,  fr.  ab-,  and  ruder e,  ‘to  scrape  off, to  shave’.  See  raze  and  cp.  abrase.
Abraham,  masc.  PN. ;  in  the  Bible,  the  first  of  the patriarchs  and  father  of  the  Hebrew  nation.
Heb.  Abhrahdm,  lit.  ‘father  of  the  multitude’, compounded  of  abh,  ‘father’,  and  *rahdm, ‘multitude’,  which  is  rel.  to  Arab,  ruhdm,  of s.m. ;  see  Gen.  17:5*  See  A  both  and  cp.  next word.
Abram,  masc.  PN.;  in  the  Bible,  former  name  of Abraham.  —  Heb.  Abhrdm,  compounded  of abh,  ‘father’,  and  ram,  ‘high,  exalted’,  which  is prop.  part,  of  rum,  ‘to  be  high,  to  be  exalted  . For  the  first  element  see  Aboth  and  cp.  Abra¬ ham.  From  the  second  element  derive  ramd>', ‘height’  (prop.  fem.  part,  of  rum),  romdm,  ‘ex¬ tolling,  praise;  song  of  praise’,  mardm,  ‘height’, tlrumdh,  ‘contribution,  offering  (for  sacred use)’,  lit.  ‘something  lifted  up,  something  sep¬ arated’.  Cp.  Aram.-Syr.  ram,  ‘was  high’,  Arab. rdma  prop,  ‘he  rose',  hence  ‘he  strove  for’,  and, in  Zanzibar  and  Oman,  ‘he  was  able  to’.  Cp. the  second  element  in  Hiram.
Abramis,  n.,  a  genus  of  fishes  ( ichthyol .) — ModL., fr.  Gk.  dppapit?,  ‘bream’,  fr.  Egyptian  rem, ‘fish’.
abranchiate,  adj.,  having  no  gills.  —  Formed  fr. priv.  pref.  a-  and  branchiate.
Derivative :  abranchiate,  n. abrase,  tr.  v.,  to  abrade.  —  L.  abrasus,  pp.  of abradere,  ‘to  scrape  off’.  See  abrade, abrasion,  n.  —  Formed  with  suff.  -ion  fr.  L. abrasus,  pp.  of  abradere.  See  prec.  word, abrasive,  adj.  and  n.  —  Formed  with  suff.  -ive fr.  L.  abrasus,  pp.  of  abradere.  See  abrade, abraxas,  n.,  a  mystical  word  used  as  a  charm.  — Gk.  ’  APpi£a<;,  according  to  Irenaeus  (in  Adver- sus  haereses  I,  c.  23  and  24)  a  word  formed  from the  Greek  letters  a,  p,  p,  a,  \,  ot,  a,  whose  numer¬ ical  value  amounts  to  365  (a  =  1,  P  =  2> p  =  100,  a  =  1,  5  —  6°,  *  —  *,  a  =  20°)> responding  to  the  number  of  aeons  in  Basilidian gnosticism  and  to  the  number  of  days  in  a  year. It  is  more  probable,  however,  that  the  word abraxas  is  an  acrostic  formed  from  the  initials of  certain  consecutive  Hebrew  words.  Cp.  abra¬ cadabra.
abreast,  adv.  —  Formed  fr.  a-,  ‘on’,  and  breast, abreovoir,  n.,  an  interstice  between  stones  ( ma¬ sonry ).  —  F.,  lit.  ‘a  watering  trough’,  fr.  abreu-
ver,  ‘to  give  drink  to  (animals)’,  fr.  OF.  abevrer, abrever,  fr.  VL.  *abbiberare,  fr.  ad-  and  L. bibere,  ‘to  drink’.  See  beverage,  and  cp.  It.  abbe- verare,  Proven?.,  Catal.  abeurar,  Sp.,  Port,  abre- var,  which  all  derive  fr.  VL.  *abbiberare. abridge,  tr.  v.  —  ME.  abregen,  fr.  OF.  abregier, abreger  (F.  abreger),  ‘to  shorten’,  fr.  L.  abbre- viare,  fr.  ad-  and  breviare,  ‘to  shorten’,  fr.  brevis, ‘short*.  See  brief,  adj.,  and  cp.  abbreviate,  which is  a  doublet  of  abridge.
Derivatives:  abridg-ed,  adj.,  abridg-ed-ly,  adv., abridg-er,  n.,  abridgment  (q.v.) abridgment,  abridgement,  n.  —  OF.  abregement (F.  abregement),  fr.  abregier.  See  abridge  and -ment.
abrin,  n.,  a  toxic  albumin  (biochem.).  —  Formed with  chem.  suff.  -in  fr.  Abrus;  so  called  because it  is  found  in  the  shrub  Abrus  precatorius. abroach,  adv.  —  Formed  fr.  a-,  ‘on’,  and  broach, abroad,  adv.  —  Formed  fr.  a-,  ‘on’,  and  broad, abrogate,  tr.  v.,  to  annul,  repeal.  —  L.  abrogatus, pp.  of  abrogare,  ‘to  annul,  to  repeal  (a  law)’,  fr. ab-  and  rogare,  ‘to  ask;  to  ask  the  people  about a  law,  to  propose  a  law’.  See  rogation  and  verbal suff.  -ate.
Derivatives:  abrogation  (q.v.),  abrogat-ive,  adj., abrogat-or,  n.
abrogation,  n.  —  L.  abrogdtid,  gen.  -onis,  repeal of  a  law’,  fr.  abrogatus,  pp.  of  abrogare.  See prec.  word  and  -ion.
Abroma,  n.,  a  genus  of  plants  of  the  chocolate family  ( bot .).  —  ModL.,  formed  fr.  priv.  pref. a-  and  Gk.  ppujia,  ‘food’.  See  broma.
Abronia,  n.,  a  genus  of  plants  of  the  four-o’clock family  (bot.)  —  ModL.,  for  *Habronia,  fr.  Gk. appo?.  See  Abrus.
```


## [2026-09-04T18:09:12.419Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"aboth\\|Abot\\b\" KLN_1966.txt | head -20\n"
}
```


### [2026-09-04T18:09:12.473Z] TOOL RESULT

```
1140:abbey,  n.,  a  convent  headed  by  an  abbot  or  an abbess.  —  ME.,  fr.  AF.  abbeie,  fr.  OF.  abeie, abaie  (F.  abbaye),  fr.  Eccles.  L.  abbatia,  fr.  L. abbas.  See  abbot  and  cp.  abba,  abbacy,  abbess. Cp.  also  It.  abbadia,  Sp.  abadia,  ‘abbey’,  which also  derive  fr.  Eccles.  L.  abbatia. abbot,  n.  —  OE.  abbod,  fr.  L.  abbat-,  stem  of abbas,  gen.  abbatis,  fr.  Aram,  abbd,  ‘the  father; my  father’,  emphatic  state  of  abh,  ‘father’,  which is  rel.  to  Heb.  abh,  ‘father’.  See  Aboth  and  cp. words  there  referred  to.  Cp.  also  abba,  abbacy, abbe,  abbey,  abuna,  badia. abbreviate,  tr.  v.,  to  shorten.  —  L.  abbrevidtus, pp.  of  ahbrevidre,  ‘to  shorten’,  fr.  ab-  and  bre- vidre,  ‘to  shorten’,  fr.  brevis,  ‘short’.  See  brief, adj., and  cp.  abridge,  which  is  a  doublet  of  abbreviate. Derivatives:  abbreviat-ed,  adj.,  abbreviation,  ab- breviator  (qq.v.),  abbreviat-ory,  adj. abbreviation,  n.  —  F.  abreviation,  fr.  L.  abbrevia- tidnem,  acc.  of  abbreviatio,  fr.  abbrevidtus,  pp. of  abbreviare.  See  abbreviate  and  -ion.
1162:Derivatives:  abid-ing,  adj.,  abid-ing-ly,  adv. Abies,  n.,  a  genus  of  trees,  the  true  fir  (bot.)  — L.  abies,  ‘silver  fir’,  cogn.  with  Gk.  fiffiv  (acc.), ‘silver  fir’,  ’Affix)),  name  of  Southern  Russia, lit.  ‘a  region  of  firs’.  Cp.  abeto. abietic,  adj.,  pertaining  to  the  crystalline  acid C20H30O2  (chem.)  —  Formed  with  suff.  -ic  fr. L.  abies,  gen.  abietis,  ‘silver  fir’.  See  prec.  word. Abigail,  fem.  PN. ;  in  the  Bible,  the  wife  of  Nabal, later  of  David.  —  Heb.  Abhigayil,  lit.  ‘my  father is  rejoicing’,  fr.  abh,  ‘father’  and  gil,  ‘to  rejoice’. For  the  first  element  see  Aboth.  The  second  ele¬ ment  is  rel.  to  Arab,  jdla,  ‘he  went  round’  and to  Heb.  galdl,  ‘he  rolled,  unfolded’;  see  gelilah. The  use  of  the  name  in  the  sense  of  ‘waiting maid’  is  due  to  the  passage  ini  Sam.  25 : 35,  where Abigail  calls  herself  a  ‘handmaid’, abigeat,  n.,  cattle  stealing  (civil  law).  —  L.  abi- geatus,  fr.  abigeus,  ‘cattle  stealer’,  fr.  abigere, ‘to  drive  away’,  fr.  ab-  and  agere,  ‘to  drive’ ;  see agent.  The  change  of  Latin  d  (in  agere)  to  f  (in  ab¬ igere)  is  due  to  the  Latin  phonetic  law  according to  which  in  the  unaccented  open  radical  syllable of  the  second  element  of  compounds,  original b  becomes  i.  Cp.  accident,  adhibit,  ambiguous, ancipital,  anticipate,  artifice,  comfit,  conceive, consilient,  constitute,  contiguous,  council,  de¬ ceive,  deciduous,  deficient,  delicious,  delitescent, desipient,  destine,  destitute,  difficulty,  disciple, dissilient,  efficient,  elicit,  exhibit,  Illicium,  inci¬ dent,  incipient,  inhibit,  inimical,  institute,  insipid, insipient,  irritate,  ‘to  make  null  and  void’,  navi¬ gate,  obstinate,  Occident,  occiput,  office,  partici¬ pate,  precipice,  prodigal,  proficient,  prohibit,  pros¬ titute,  receive,  recidivist,  resilient,  resipiscence, restitute,  reticent,  substitute,  superficies,  super¬ stition,  supplicate,  transilient. ability,  n.  —  ME.  abilite,  fr.  OF.  ablete,  habilite (F.  habilite),  fr.  L.  habffitatem,  acc.  of  habilitas, ‘aptitude,  ability’,  fr.  habilis,  ‘that  may  be  easily handled  or  managed,  suitable,  fit,  proper’.  See able  and  -ity.
1191:lonian  PN.  Abunuri.  For  the  first  element  see Aboth,  for  the  second  see  Menorah. abnormal,  adj.  — ■  A  blend  of  L.  abnormis  and ML.  anormalis,  this  latter  itself  being  a  blend of  L.  anomalus  and  normalis.  See  anomalous  and norm  and  cp.  anormal.
1209:Derivatives:  abortion-al,  adj.,  abortion-ist ,  n. abortive,  adj.,  I)  born  prematurely;  2)  unsuccess¬ ful.  —  L.  abortivus,  ‘pertaining  to  miscarriage’, fr.  abortus,  pp.  of  aboriri.  See  abort,  v.,  and  -ive. Derivatives:  abortive-ly,  adj.,  abortive-ness,  n. Aboth,  also  Abot,n.,  i)the  Mishnah  treatise  also called  Pirke  Aboth  or  The  Ethics  of  the  Fathers  ', 2)  name  of  the  first  benediction  of  the  Shemoneh Esreh  ( Jewish  liturgy).  —  Heb.  Abhdth,  pi.  of abh,  ‘father’,  rel.  to  Aram,  abh  (absolute  state), abbd  (emphatic  state),  Ugar.  ’b,  Arab,  ab, Ethiop.  ab,  ‘father’ ;  of  uncertain  origin,  possibly traceable  to  *ab(a),  a  child’s  word  for  father. Cp.  the  first  element  in  Abraham,  Abner,  Absa¬ lom,  Abigail,  and  the  second  element  in  Joab, Moab,  Barabbas.  Cp.  also  abbot  and  words there  referred  to.  Cp.  also  borage, abound,  intr.  v.  —  ME.  abounden,  fr.  OF,  (=  F.) abonder,  fr.  L.  abundare,  ‘to  overflow;  to  a- bound’,  fr.  ab-  and  unda,  ‘wave’.  See  undate  and cp.  redound,  surround.  Derivatives:  abound-er, n.,  abound-ing,  adj.,  abound-ing-ly,  adv. about,  adv.  —  ME.  abuten,  abouten,  about e,  fr. OE.  abutan,  onbutan,  ‘on  the  outside  of’,  formed fr.  a-,  ‘on’,  and  butan,  ‘outside’,  which  itself  is formed  fr.  be,  ‘by’,  and  iitan,  ‘outside’,  fr.  ut, ‘out’.  See  by  and  out  and  cp.  but.
1219:Abram,  masc.  PN.;  in  the  Bible,  former  name  of Abraham.  —  Heb.  Abhrdm,  compounded  of abh,  ‘father’,  and  ram,  ‘high,  exalted’,  which  is prop.  part,  of  rum,  ‘to  be  high,  to  be  exalted  . For  the  first  element  see  Aboth  and  cp.  Abra¬ ham.  From  the  second  element  derive  ramd>', ‘height’  (prop.  fem.  part,  of  rum),  romdm,  ‘ex¬ tolling,  praise;  song  of  praise’,  mardm,  ‘height’, tlrumdh,  ‘contribution,  offering  (for  sacred use)’,  lit.  ‘something  lifted  up,  something  sep¬ arated’.  Cp.  Aram.-Syr.  ram,  ‘was  high’,  Arab. rdma  prop,  ‘he  rose',  hence  ‘he  strove  for’,  and, in  Zanzibar  and  Oman,  ‘he  was  able  to’.  Cp. the  second  element  in  Hiram.
1236:Absalom,  masc.  PN. ;  in  the  Bible,  King  David  s son;  fig.  a  favorite  son.  —  Heb.  Abhshaldm,  lit. ‘father  is  peace’,  fr.  abh,  ‘father’,  and  shaldm, ‘peace’.  See  Aboth  and  shalom. abscess,  n„  a  swelling  in  body  tissues  (med.).  — L.  abscessus,  ‘a  going  away,  departure,  abscess  , fr.  abcedere,  ‘to  go  away’,  fr.  abs-,  ab-,  ‘away from,  from’,  and  cedere,  ‘to  go’.  See  ab-  and cede  and  cp.  cease.
1267:absurdity,  n.  —  F.  absurdite,  fr.  L.  absurditatem, acc.  of  absurditds,  ‘dissonance,  incongruity’, fr.  absurdus.  See  prec.  word  and  -ity. abulia,  n.,  loss  of  will  power  (psychol.)  —  Medical L.,  formed  fr.  priv.  pref.  a-,  the  stem  of  Gk. (3o')Asa&ai,  ‘to  will’,  and  suff.  -ia.  See  boule, ‘senate’,  and  cp.  Gk.  a(3ouXia,  ‘ill-advisedness  . abuna,  n.,  the  patriarch  of  the  Abyssinian Church.  —  Ethiop.  abuna,  ‘our  father’,  fr.  ab, ‘father’,  which  is  rel.  to  Heb.  abh,  ‘father  .  See Aboth  and  cp.  abbot  and  words  there  referred  to. abundance,  also  abundancy,  n.  —  ME.,  fr.  OF. abundance,  abondance  (F.  abondance),  fr.  L. abundantia,  ‘abundance,  plenty,  fullness’,  fr. abandons,  gen.  antis.  See  next  word  and  -ce, resp.  -cy.
4420:Barabbas,  masc.  PN.  —  L.,  fr.  Gk.  BapappSp,  fr. Aram,  bar  abba,  ‘son  of  the  father,  son  of  the master',  fr.  bar,  ‘son’,  which  is  rel.  to  Heb.  ben, ‘son’,  and  fr.  Aram,  abbd,  ‘the  father’,  emphatic state  of  abh,  which  is  rel.  to  Heb.  abh,  ‘father’. For  the  first  element  sec  ben,  ‘son’,  and  cp.  bar mitzvah  and  words  there  referred  to.  For  the second  element  see  Aboth  and  cp.  Abba,  abbot, barad,  n.,  the  unit  of  pressure  in  the  centimeter- gram-second  system  (physics).  —  Fr.  Gk.  Papop, ‘weight’.  See  baro-.
6437:lid’,  kapalt-,  ‘mendicant’s  bowl’.  See  head  and  cp. capital,  ‘principal’,  capital,  ‘head  of  a  column’, and  chief.  Cp.  also  achieve,  ancipital,  biceps, cabildo,  cabotage,  cadet,  camail,  camouflage,  Ca- pito,  cap-a-pie,  cape,  ‘promontory’,  capitan,  ca¬ pitation,  capitellum,  Capito,  Capitol,  capitulate, caporal,  capot,  caprice,  captain,  cater,  ‘to  provide food’ ;  cattle,  caudillo,  cavesson,  chabot,  chapiter, chapter,  chef,  chevet,  chieftain,  corporal  (mil.),  da capo,  decapitate,  kerchief,  mischief,  muscovado, occiput,  precipice,  precipitant,  precipitate,  quadri¬ ceps,  sinciput,  triceps.  Cp.  also  capillary. Derivatives:  capital,  n.  (q.v.),  capital-ly,  adv. capital,  n.,  stock  of  money,  principal.  —  Late  L. capitate,  ‘property’,  prop.  neut.  of  the  Latin  ad¬ jective  capitalis,  ‘pertaining  to  the  head,  chief, first’.  Cp.  It.  capitate,  F.  capital,  G.  Kapital, ‘capital,  principal’,  and  see  capital,  adj.  For sense  development  cp.  cattle.
6441:Capito,  n.,  a  genus  of  fishes,  the  South  American barbet  (ichthyoid)  —  L.  capito,  ‘a  large-headed fish’,  lit.  Targe  head’,  augment,  of  caput,  gen. capitis,  ‘head’.  See  capital,  adj.,  and  cp.  chabot. Capitol,  n.,  the  temple  of  Jupiter  on  one  of  the seven  hills  of  Rome  (on  the  Mons  Capitolinus). —  L.  Capitolium,  a  derivative  of  caput,  gen. capitis,  ‘head’.  See  capital,  adj. capitoline,  adj.,  pertaining  to  the  Capitol  in  Rome or  to  the  hill  on  which  it  stood.  —  L.  Capito- linus,  fr.  Capitolium.  See  prec.  word  and  adj. suff.  -ine  (representing  L.  -inus). capitular,  adj.,  pertaining  to  a  chapter.  —  ML. capitularis,  fr.  L.  capitulum,  ‘a  small  head,  chap¬ ter’,  dimin.  of  caput,  gen.  capitis,  ‘head’.  See capital,  adj.,  and  -ar  and  cp.  chapter, capitulary,  adj.,  pertaining  to  a  chapter.  —  See prec.  word  and  adj.  suff.  -ary. capitulary,  n.,  a  collection  of  decrees.  —  ML. capitularium,  fr.  capitaldris.  See  capitular  and subst.  suff.  -ary.
7101:chabot,  n.,  the  fish  called  miller’s  thumb  (her.)  — F.,  ‘miller’s  thumb’,  also  ‘bullhead’,  fr.  earlier cahot,  fr.  OProven?.  cabotz,  ‘a  large-headed (fish)’,  fr.  VL.  *capoceus,  fr.  L.  caput,  ‘head’.  See capital,  adj.,  and  cp.  Capito. chabouk,  chabuk,  n.,  a  long  whip.  —  Pers.  chdbug, ‘a  whip’.  Cp.  chawbuck,  sjambok, cha-cha,  also  cha-cha-cha,  n.,  a  dance  in  3-beat rhythm.  —  Amer.  Sp.  cha-cha-cha. chacma,  n.,  a  South  African  baboon.  —  Hot¬ tentot.
20108:jabot,  n.,  frill  of  a  shirt.  —  F.,  ‘crop,  maw;  frill of  a  shirt’,  prob.  rel.  to  F.  gaver,  ‘to  cram, gorge’,  OProvenf.  gava,  ‘crop,  maw’.  See  jaw. jacamar,  n.,  an  insectivorous  bird  of  tropical America.  —  F.,  erroneously  formed  by  the French  naturalist,  Comte  Georges-Louis  Le- clerc  Buffon  (1707-88)  fr.  Tupi  jacamd-ciri. jacana,  n.,  a  S.  American  wading  bird  resembling the  rail.  —  Port,  jafana,  fr.  Tupi  yasana. jacaranda,  n.,  a  tropical  American  tree.  —  Port. jacaranda,  fr.  Tupi  yacaranda. jacinth,  n.  — •  ME.  iacynth,  iacinth,  fr.  OF.  ia- cinthe  (F.  jacinthe),  fr.  L.  hyacinthus,  fr.  Gk. uaxivUoi;.  See  hyacinth.
20198:‘to  cram,  gorge’,  OProven?.  gava,  ‘crop,  maw’ ; prob.  influenced  in  form  by  jowl.  Cp.  jabot.
20305:Joab,  1)  masc.  PN. ;  2)  in  the  Bible,  the  chief  cap¬ tain  of  David’s  army.  —  Late  L.  Joab,  fr.  Gk. ’lojafi,  fr.  Heb.  Yd'dbh ,  lit.  ‘the  Lord  is  (his) father’.  For  the  first  element  cp.  the  PN’s  Joel, John,  Jonathan,  Joshua,  for  the  second  see Aboth  and  cp.  words  there  referred  to.
33424:sable,  n.,  a  small  animal,  Mustella  zibellina.  — ME.,  fr.  MF.  sable  (F.  zibeline),  fr.  OF.,  fr.  ML. sabelum,  fr.  MLG.  sabel,  fr.  MHG.  zobel,  a  loan word  fr.  Russ.  soboV,  which  itself  is  borrowed from  an  East-Asiatic  language.  Cp.  zibeline. sable,  adj.,  black  (her.)  —  F.  sable,  prop,  ‘of  the color  of  the  sable’.  See  prec.  word, sabot,  n.,  a  wooden  shoe.  —  F.,  blend  of  hot,  a dialectal  var.  of  botte,  ‘boot’,  and  savate,  ‘old shoe’.  See  boot  and  savate. sabotage,  n.,  willful  destruction  of  machinery, etc.  —  F.,  fr.  saboter,  ‘to  do  willful  damage  fto machinery  and  the  like),  fr.  sabot  (see  prec. word) ;  the  verb  was  formerly  used  in  the  sense ‘to  throw  wooden  shoes  into  the  machinery  for the  sake  of  damaging  it’.  For  the  ending  see suff.  -age.
33848:Derivatives:  savage,  n.  and  tr.  v.,  savage-dom, n.,  savage-ly,  adv.,  savage-ness,  n.,  savag-ery,  n., savag-ism ,  n.,  savag-ize,  tr.  v. savannah,  savanna,  n.,  a  treeless  plain.  —  Sp.  za- vana  (now  spelled  sabana),  fr.  Taino  zavana. Cp.  F.  savane,  which  is  also  a  Spanish  loan  word, savant,  n.,  a  learned  man.  —  F.,  orig.  pres.  part, of  savoir,  ‘to  know’,  fr.  VL.  * sapere ,  fr.  L.  sape- re.  See  sapient  and  cp.  words  there  referred  to. For  the  ending  see  suff.  -ant. savate,  n.,  boxing  with  feet  or  fists.  —  F.,  ‘old shoe;  boxing  with  the  feet’,  prob.  fr.  Basque  za- pata,  zapato,  ‘shoe’,  whence  zapatain ,  ‘shoe¬ maker’.  Cp.  Sp.  zapata,  zapato,  ‘shoe’,  and  E. sabot  —  See  Littr6,  Dictionnaire  de  la  langue frangaise,  p.  1842  s.v.  savate. save,  tr.  and  intr.  v.  —  ME.  sauven,  saven,  fr.  OF. salver,  sauver  (F.  sauver),  fr.  Late  L.  salvare,  ‘to save’,  fr.  L.  salvus,  ‘safe’.  See  safe  and  cp.  sal¬ vage,  salvation,  savoir.
```


## [2026-09-04T18:09:24.287Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"borage\" KLN_1966.txt\n"
}
```


### [2026-09-04T18:09:24.338Z] TOOL RESULT

```
1209:Derivatives:  abortion-al,  adj.,  abortion-ist ,  n. abortive,  adj.,  I)  born  prematurely;  2)  unsuccess¬ ful.  —  L.  abortivus,  ‘pertaining  to  miscarriage’, fr.  abortus,  pp.  of  aboriri.  See  abort,  v.,  and  -ive. Derivatives:  abortive-ly,  adj.,  abortive-ness,  n. Aboth,  also  Abot,n.,  i)the  Mishnah  treatise  also called  Pirke  Aboth  or  The  Ethics  of  the  Fathers  ', 2)  name  of  the  first  benediction  of  the  Shemoneh Esreh  ( Jewish  liturgy).  —  Heb.  Abhdth,  pi.  of abh,  ‘father’,  rel.  to  Aram,  abh  (absolute  state), abbd  (emphatic  state),  Ugar.  ’b,  Arab,  ab, Ethiop.  ab,  ‘father’ ;  of  uncertain  origin,  possibly traceable  to  *ab(a),  a  child’s  word  for  father. Cp.  the  first  element  in  Abraham,  Abner,  Absa¬ lom,  Abigail,  and  the  second  element  in  Joab, Moab,  Barabbas.  Cp.  also  abbot  and  words there  referred  to.  Cp.  also  borage, abound,  intr.  v.  —  ME.  abounden,  fr.  OF,  (=  F.) abonder,  fr.  L.  abundare,  ‘to  overflow;  to  a- bound’,  fr.  ab-  and  unda,  ‘wave’.  See  undate  and cp.  redound,  surround.  Derivatives:  abound-er, n.,  abound-ing,  adj.,  abound-ing-ly,  adv. about,  adv.  —  ME.  abuten,  abouten,  about e,  fr. OE.  abutan,  onbutan,  ‘on  the  outside  of’,  formed fr.  a-,  ‘on’,  and  butan,  ‘outside’,  which  itself  is formed  fr.  be,  ‘by’,  and  iitan,  ‘outside’,  fr.  ut, ‘out’.  See  by  and  out  and  cp.  but.
2234:Alkanna,  n.,  a  genus  of  plants  of  the  borage family  (bot.)  —  ModL.,  fr.  Sp.  alcana,  fr.  Arab. al-hinnd',  fr.  al-,  ‘the’,  and  hinnd',  ‘henna’.  See henna.
2693:Anchusa,  n.,  a  genus  of  plants  of  the  borage  fa¬ mily.  —  L.  anchusa ,  fr.  Gk.  avy/jorca,  ‘alkanet’, which  is  of  uncertain  origin, anchylose,  n.  —  See  ankylose. anchylosis,  n.  —  See  ankylosis, anchylotic,  adj.  — -  See  ankylotic. ancient,  adj.,  old.  —  F.  ancien,  fr.  VL.  *antianus, ‘former’,  fr.  ante,  ‘before’ ;  see  ante-.  The  -t  in ancient  is  excrescent  and  is  due  to  a  confusion of  the  ending  of  F.  ancien  with  -ent,  the  English equivalent  of  L.  -ens  (gen.  -entis),  the  pres.  part, sulf.  of  the  II-IV.  Latin  conjugations.  Cp.  pag¬ eant,  peasant,  pheasant,  tyrant.
3484:Amebia,  n.,  a  genus  of  plants  of  the  borage family  (bot.) — Arab,  arnabtya *,  name  of  a  plant, lit.  ‘hare  plant’,  fr.  drnab,  ‘hare’,  which  is  rel. to  Heb.  arnebheth,  Arm.  arnabhtd,  Syr.  ar- nlbhA,  Ugar.  'nhb.  Akkad,  annabu,  ‘hare’.
3492:Derivatives:  arous-al,  n.,  arous-er,  n. a  rovescio,  a  musical  direction  indicating  imita¬ tion  by  contrary  motion.  —  It.,  lit.  ‘upside down’,  fr.  a  (fr.  L.  ad),  ‘to’,  and  rovescio,  ‘re¬ verse,  wrong  side’,  fr.  L.  reversus,  ‘turned  back’, pp.  of  revertere.  See  ad-  and  revert, arpeggio,  n.,  the  playing  of  the  notes  of  a  chord in  rapid  succession  instead  of  simultaneously; a  chord  on  which  the  notes  are  so  played (mus.)  —  It.,  fr.  arpeggiare,  ‘to  play  upon  the harp',  fr.  arpa,  ‘harp’.  See  harp, arpent,  n.,  an  old  French  land  measure.  —  F., fr.  VL.  *arependis,  alteration  of  L.  arepennis, a  Gaulish  word  of  uncertain  origin, arquebus,  n.  —  See  harquebus, arrack,  in  the  East,  a  strong  alcoholic  drink  made from  rice  or  molasses.  —  Fr.  Arab,  ‘araq,  ‘sweat, juice  of  fruit’.  Cp.  rack,  ‘arrack’,  and  borage, arraign,  tr.  v.,  to  call  to  account;  to  bring  before a  law  court.  —  ME.  areinen,  fr.  AF.  areiner, fr.  OF.  araisnier,  aresnier  (F.  arraisonner),  fr. VL.  *arrationare,  fr.  ad-  and  *rationdre,  ‘to reason’,  fr.  L.  ratio,  ‘reckoning,  calculation; reason’.  See  reason  and  cp.  deraign. Derivatives:  arraign,  n.,  arraign-er,  n.,  arraign¬ ment  (q.v.)
3654:Derivatives:  aspers-ed,  adj.,  aspers-er,  n.,  aspers- ive,  adj.,  aspers-ive-ly,  adv. aspersion,  n.  —  L.  aspersio,  gen.  -dnis,  fr.  asper¬ sus,  pp.  of  aspergere.  See  prec.  word  and  -ion. Asperuga,  n,,  a  genus  of  plants  of  the  borage
5360:Borachio,  n.,  name  of  a  drunkard  in  Shakespeare’s Much  Ado  About  Nothing.  —  Sp.  borracho, 'drunk,  intoxicated’,  fr.  L.  burrus,  ‘red’  (see burro);  so  called  in  allusion  to  the  red  com¬ plexion  of  intoxicated  people, boracic,  adj.,  boric.  —  See  borax  and  -ie. borage,  n.,  a  blue-flowered  plant  used  in  salads. —  ME.,  fr.  OF.  borrace  (cp.  its  variant  burage and  F.  bourrache),  fr.  ML.  borrago,  ult.  fr. Arab,  abu  ‘ arak ,  lit.  ‘father  of  sweat’,  so  called by  the  Arab  physicians  because  of  its  sudorific effect.  See  abbot  andc  p.  arrack, boraginaceous,  adj.  —  Formed  with  suff.  -aceous fr.  ML.  borrago,  gen.  borrdginis.  See  prec.  word, borate,  n.,  salt  of  boric  acid  ( chem .)  —  See  boron and  chem.  suff.  -ate.
5384:borrow,  tr.  and  intr.  v.  —  ME.  borwen,  fr.  OE. borgian,  ‘to  lend;  to  borrow’,  fr.  borg,  ‘pledge, security',  rel.  to  ON.  borga ,  ‘to  become  bail  for, to  guarantee’,  MDu.  borghen,  ‘to  protect,  guar¬ antee’,  OHG.  boragen,  borgen,  ‘to  beware  of; to  spare;  to  remit  a  debt',  G.  borgen,  ‘to  bor¬ row;  to  lend’,  biirgen,  ‘to  become  bail  for,  to guarantee’,  OE.  beorgan,  OHG.  bergan,  ‘to  hide, save’.  See  bury.
7038:Cerinthe,  n.,  a  genus  of  plants  of  the  borage family  ( bot .)  — -  ModL.,  fr.  L.  cerintha,  cerinthe, ‘the  waxflower’,  fr.  Gk.  xyjoivIJo:,  ‘beebread’, which  was  prob.  formed  fr.  xvjpoc,  ‘wax’,  with suff.  -ivho;.  See  cere,  n.
8336:comforter,  n.  —  OF.  conforteor,  fr.  conforter.  See comfort,  v.,  and  agential  suff.  -er. comfrey,  n.,  a  plant  of  the  borage  family  —  ME. confine,  cumfirie,  fr.  OF.  confirie,  fr.  con-  (see con-)  and  firie,  ‘liver’  (=  F  .foie),  which  prob. derives  fr.  L.  ( iecur )  ficatum,  ‘liver  (of  a  goose) fattened  with  figs’,  neut.  pp.  of fiedre,  ‘to  fatten with  figs’,  fr.  ficus,  ‘fig’;  see  fig.  The  plant  was so  called  because  of  its  congealing  properties, comic,  adj.  —  L.  comicus,  fr.  Gk.  x(0fxtx6i;,  ‘per¬ taining  to  comedy’,  fr.  xtop.0?,  ‘comic  chorus’. See  comedy  and  -ic.
10111:Cynoglossum,  n.,  a  genus  of  the  borage  family {bot.)  —  ModL.,  fr.  Gk.  xuvAyAcoaoov,  ‘hound’s- tongue’,  which  is  compounded  of  xumv,  gen. XUV69,  ‘dog’  and  yAcocraa,  ‘tongue’.  See  cyno-  and gloss,  ‘explanation’.
17491:heliotrope,  n.,  orig.  a  plant  that  turns  to  the  sun; now  any  plant  of  the  borage  family,  with  frag¬ rant  purple  or  white  flowers.  —  F.  heliotrope, fr.  L.  heliotropium,  fr.  Gk.  vjXioxpoTUov,  ‘helio¬ trope’,  lit.  ‘that  which  turns  toward  the  sun’, fr.  Tpxoc,,  ‘sun’,  and  -xporox;,  ‘turning’,  fr. xpsbreiv,  ‘to  turn’.  See  helio-  and  trope, heliotropic,  adj.,  characterized  by  heliotropism. —  See  next  word  and  -tropic.
23588:Mertensia,  n.,  a  genus  of  plants  of  the  borage family  (bot.)  —  ModL.,  named  after  the  Ger¬ man  botanist  Franz  Karl  Mertens  (1764-1831). For  the  ending  see  1st  suff.  -ia.
30901:puccoon,  n.,  any  of  the  plants  of  the  borage  fam¬ ily. —  Virginian  puccoon.  See  poke,  ‘pokeweed’. puce,  n.,  a  brownish  color.  —  F.,  ‘flea ;  flea  color’, fr.  L.  pidicem,  acc.  of piilex,  ‘flea’.  See  Pulex  and cp.  puceron.
```


## [2026-09-04T18:09:41.015Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON part1/2 بوزینه ===\"\ngrep -n \"بوزینه\\|بوزنه\" MON_part1.txt MON_part2.txt 2>/dev/null | head -20\necho \"=== BQT ===\"\ngrep -n \"بوزینه\\|بوزنه\" BQT_v1.txt BQT_v2.txt BQT_alt_v1.txt BQT_dli_part1.txt 2>/dev/null | head -20\necho \"=== incoming MON djvu ===\"\ngrep -n \"بوزینه\\|بوزنه\" incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -20\n"
}
```


### [2026-09-04T18:09:41.137Z] TOOL RESULT

```
=== MON part1/2 بوزینه ===
MON_part2.txt:12191:فرد: 2۵«(ع.] (4.) بوزینه» میمون نر) ج. 
MON_part2.txt:12195:فردبوزینه؛ ج. قرد. 
MON_part2.txt:29953:ک 0۲ [- کپی - کبی] (.) بوزینه؛ 
MON_part2.txt:70813:هندوستان می‌زید؛ بوزینه‌هاء بوزنه‌ها. 
MON_part2.txt:72114:نازین (قس. بوزینه) | (ص‌نسه.) دارنده نازء 
MON_part1.txt:26095:بورینه: (6-)۱1212 [- بوزینا - بوزنه - 
MON_part1.txt:26100:بوزنه: (م-)هم002 (۱.) شکو فه و هار درخت 
MON_part1.txt:82874:میمون» بوزینه. 
=== BQT ===
BQT_alt_v1.txt:2359:عربی معروف است» این‌لفت هندی است اما نه مانند لغات کپی (بوزینه) وشکر وشمن و چندن 
BQT_alt_v1.txt:35679:و بوزینه. میان اسان وحیوان »و انان مان‌خلق 
BQT_alt_v1.txt:36455:بوزینه هم آمده است که میمون باشد » و جفتح 
BQT_alt_v1.txt:40428:میمون است که بوزینه باشد - و بکسر اول بر 
BQT_alt_v1.txt:57949:سر کرمی و مشفولی: «و بفرمود ناهمةٌ مطربان و مسخرگان و هزالان و سگان شکاری و بوزنه 
BQT_v2.txt:11927:چو لین سبروزن بوزینه, بمعنی‌چوینك 
BQT_v2.txt:34715:وزن بوزینه, بمعنی‌دوزنه است که یش جانوران 
BQT_v2.txt:62139:بوزینه را گوبند . و آن نوعی از میمون باشد- 
BQT_v1.txt:44099:میمون است که بوزینه بائد - و بکسر او بر 
BQT_v1.txt:63065:س رکرمی و مشفولی: هو بفرمود تاهمةٌ مطربان و مسض رکان و هزالان و سگان شکاری و بوزنه 
=== incoming MON djvu ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:26095:بورینه: (6-)۱1212 [- بوزینا - بوزنه - 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:26100:بوزنه: (م-)هم002 (۱.) شکو فه و هار درخت 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:82874:میمون» بوزینه. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:12191:فرد: 2۵«(ع.] (4.) بوزینه» میمون نر) ج. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:12195:فردبوزینه؛ ج. قرد. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:29953:ک 0۲ [- کپی - کبی] (.) بوزینه؛ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:70813:هندوستان می‌زید؛ بوزینه‌هاء بوزنه‌ها. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:72114:نازین (قس. بوزینه) | (ص‌نسه.) دارنده نازء
```


## [2026-09-04T18:09:44.460Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '26090,26105p' MON_part1.txt\n"
}
```


### [2026-09-04T18:09:44.505Z] TOOL RESULT

```
بوز: 2 (ص.) اسب تندرو؛ اسب جلد. 
مرد تیزهوشء» صاحب ادرا کت مق. کودن. 
بوزه: (-)۳۳22 (.) شرابی که از آرد برنج و 
ارزن و جو سازند. 

بورینه: (6-)۱1212 [- بوزینا - بوزنه - 
بوزنینه ] (.) (جاذ.) میمون. 

بوژ: (02۳2)00۷ (.) گرداب. 

بوزنه: (م-)هم002 (۱.) شکو فه و هار درخت 
که هنوز نشگفته باشدء کم. 

بوس: ۰" [- بوسه] (ا.) (حامص.) گٌاه در 
ترکیب به معنی «بوسی» آید: پابوس. (افاء) 
گاه در ترکیب به معنی («یوسنده) آید:
```


## [2026-09-04T18:09:52.422Z] TOOL CALL #23: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-04T18:09:52.428Z] TOOL RESULT

```


```


## [2026-09-04T18:09:58.084Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/gibbon",
 "prompt": "Give the full etymology text for \"gibbon\" (the ape), including any mention of Arabic, Persian, or Hindustani origin."
}
```


## [2026-09-04T18:09:59.167Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/borage",
 "prompt": "Give the full etymology text for \"borage\" (the plant), including the Arabic \"father of sweat\" theory and Latin burra theory."
}
```


## [2026-09-04T18:09:59.720Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/arrack",
 "prompt": "Give the full etymology text for \"arrack\", including the Arabic 'araq root."
}
```


## [2026-09-04T18:10:00.238Z] TOOL CALL #27: WebSearch

```json
{
 "query": "Proto-Semitic *ʔab- father etymology Wiktionary Akkadian abu Hebrew Arabic Ugaritic"
}
```


## [2026-09-04T18:10:01.155Z] TOOL CALL #28: WebSearch

```json
{
 "query": "بوزینه ریشه شناسی واژه میمون فارسی اتیمولوژی"
}
```


### [2026-09-04T18:10:02.957Z] TOOL RESULT

```
# Etymology of Gibbon

Based on the provided content, here is the full etymology:

The word "gibbon" entered English in 1770, derived from French *gibbon* (18th century). According to the source, the French term's origin is "supposedly from a word in the French colonies of India but not found in any language there."

The text notes that the animal was introduced to Europe by Marquis Joseph-François Dupleix (1697-1763), who served as French governor general in India from 1742-54.

**Important caveat:** The source makes no mention of Arabic, Persian, or Hindustani origins. It explicitly states the supposed colonial Indian source was never actually located in any documented language. The etymology remains uncertain beyond its French transmission.
```


### [2026-09-04T18:10:05.393Z] TOOL RESULT

```
# Etymology of Borage

**Origin**: The word "borage" entered English in the mid-13th century from Anglo-French *burage* and Old French *borage*, ultimately deriving from Medieval Latin *borrago*.

**Two Competing Theories**:

1. **Arabic Theory (Folk Etymology)**: According to historical sources, Medieval scholars believed the term came from Arabic *abu arak*, meaning "the father of sweat," supposedly referencing the plant's supposed effects on perspiration as noted by Arab physicians.

2. **Latin Theory (More Likely)**: The OED and other scholarly sources propose an alternative origin from Latin *borra*, meaning "rough hair, short wool," which would reference the texture of the plant's foliage.

**Linguistic Parallels**: The word spread across European languages, appearing as Spanish *boraja*, Italian *borraggine*, and German *Boretsch*.

**Related Term**: The adjective *Boraginaceous* connects to borage's botanical classification.

The plant itself has been used in salads and similar culinary applications since medieval times.
```


### [2026-09-04T18:10:06.388Z] TOOL RESULT

```
Web search results for query: "Proto-Semitic *ʔab- father etymology Wiktionary Akkadian abu Hebrew Arabic Ugaritic"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T18:10:07.025Z] TOOL RESULT

```
# Etymology of Arrack

The word "arrack" entered English around 1600, likely acquired through India via Portuguese, Spanish, and French sources. It derives from Hindi *arak* and Tamil *araku*, which ultimately trace back to Arabic *araq*, meaning "distilled spirits, strong liquor."

The Arabic root carries a literal sense of "sweat, juice" and was applied to native Eastern liquors, particularly those distilled from coconut palm fermented sap, though rice and molasses varieties also existed under this designation.
```


### [2026-09-04T18:10:08.357Z] TOOL RESULT

```
Web search results for query: "بوزینه ریشه شناسی واژه میمون فارسی اتیمولوژی"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T18:10:22.292Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=borage",
 "prompt": "Give the full etymology/origin note for the word \"borage\" as printed on this American Heritage Dictionary page."
}
```


## [2026-09-04T18:10:23.476Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/borage",
 "prompt": "Give the full etymology section for the English word \"borage\", including any mention of Arabic abu 'araq and any alternate Latin burra theory, and note which is preferred."
}
```


## [2026-09-04T18:10:23.936Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/gibbon",
 "prompt": "Give the full etymology section for the English word \"gibbon\" (the ape), including any theories about Persian, Arabic, or Hindustani origin."
}
```


## [2026-09-04T18:10:25.630Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%B2%DB%8C%D9%86%D9%87",
 "prompt": "Give the full etymology section for the Persian word بوزینه (buzine/buzineh, \"monkey/ape\"), including any proposed Arabic or other origin."
}
```


## [2026-09-04T18:10:26.832Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D8%B1%D8%A7%D9%87%DB%8C%D9%85",
 "prompt": "Give the full etymology section for the Persian word ابراهیم (Ebrâhim, \"Abraham\"), including its derivation route from Hebrew/Arabic."
}
```


### [2026-09-04T18:10:27.349Z] TOOL RESULT

```
# Etymology of "Borage"

According to the American Heritage Dictionary entry, borage's origin traces back through several languages:

**Direct quote from the etymology section:**
"[Middle English, from Old French _bourage_, from Medieval Latin _borāgō_, probably from Arabic _bū'araq_, from _'abū 'araq_, source of sweat (from its use as a sudorific) : _'ab_, father, source; see **ʾb** + _'araq_, sweat; see **ʿrq**2.]"

The word's linguistic journey flows from Arabic roots referring to sweat (reflecting the plant's historical use as a sudorific), through Medieval Latin, Old French, and finally into Middle English. The Arabic components break down as "father" and "sweat," combining to reference the herb's traditional medicinal properties.
```


### [2026-09-04T18:10:29.009Z] TOOL RESULT

```
# Etymology of "Borage"

Based on the Wiktionary entry, borage has the following etymological path:

The word comes from Middle English _borage_, borrowed from Old French _borage_ (related to French _bourrache_). This traces back to Medieval Latin _borrago_.

The source presents **two competing theories** for the ultimate origin, without explicitly stating a preference:

1. **Latin theory**: From Latin _borra_ meaning "short wool, rough hair"

2. **Arabic theory**: From Arabic _أَبُو العَرَق_ (ʔabū l-ʕaraq), literally translating to "father of sweat"

The entry lists both possibilities with the conjunction "either...or," indicating scholarly uncertainty about which etymology is correct rather than endorsing one as preferred.
```


### [2026-09-04T18:10:31.571Z] TOOL RESULT

```
# Etymology of "Gibbon" (English)

Based on the Wiktionary article provided, here is the complete etymology section for the English word "gibbon":

The term represents a "reborrowing from French *gibbon*," involving folk etymology that connects to the English surname Gibbon. The ultimate origin traces back to a Northern Aslian language, with comparison to the Batek word *kəboɲ*.

The article notes that the word came to Europe through French India, brought by Joseph François Dupleix. The etymology acknowledges an Aslian root combined with English folk etymological influence.

**Important note:** The provided Wiktionary content contains no theories regarding Persian, Arabic, or Hindustani origins for this word. The documented etymology focuses exclusively on French transmission and Aslian linguistic roots from Southeast Asian languages.
```


### [2026-09-04T18:10:33.166Z] TOOL RESULT

```
# Etymology of بوزینه (buzine)

According to the Wiktionary entry, the word is **inherited from Proto-Iranian**. The entry notes a comparison with Pashto _بيزو_ (bízo, "monkey").

The word has an ancient borrowing history into other languages: it was borrowed into Old East Slavic _обезьꙗ́на_ (obezĭjána), which led to Russian _обезья́на_ (obezʹjána, "monkey, ape"). It was also likely borrowed into Old Turkic _𐰋𐰃𐰲𐰃𐰤_ (béčin, "monkey").

Notably, **no Arabic origin is mentioned** in this etymology section. The documented origin traces the word back to Proto-Iranian ancestry with subsequent borrowing into neighboring language families rather than deriving from Arabic sources.
```


### [2026-09-04T18:10:35.100Z] TOOL RESULT

```
# Etymology of Persian ابراهیم (Ebrâhim)

The Persian word ابراهیم traces its origins through a multi-language chain. According to the Wiktionary entry, it was "Borrowed from Arabic إِبْرَاهِيم (ʔibrāhīm)."

The Arabic term itself derives from earlier Semitic languages. The etymology tree shows that Arabic borrowed from Aramaic אַבְרָהָם (ʾaḇrāhām), which in turn borrowed from Biblical Hebrew אַבְרָהָם (ʔaḇrɔhɔm).

Therefore, the complete derivation path for Persian ابراهیم is:

**Biblical Hebrew → Aramaic → Arabic → Persian**

The name ultimately originates in Biblical Hebrew and traveled westward through Aramaic and Arabic before being adopted into Persian, where it retained its religious and cultural significance as the name of the Islamic prophet Abraham.
```


## [2026-09-04T18:10:56.646Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"gibbon\\|bozin\\|buzin\\|bojina\\|abu.zin\\|abuzin\" LKT.txt | head -20\n"
}
```


### [2026-09-04T18:10:56.693Z] TOOL RESULT

```
1413:5.56.  Tk.  ebnzine: Auch  buzine  'Affe'  [aus  ar.  abü  zina" 'Vater   der   Unzucht'];    hieraus  russ. obez'jana,  klruss.  obezjana  'Affe'  [vgl. lit.  bezdona].
```


## [2026-09-04T18:10:58.720Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD (Pahlavi) ===\"\ngrep -n -i \"boz\\|wozan\\|bwcyn\" PHD.txt PHD_mackenzie.txt 2>/dev/null | head -20\necho \"=== HRN ===\"\ngrep -n -i \"buzin\\|bozin\" HRN.txt 2>/dev/null | head -20\necho \"=== HUB ===\"\ngrep -n -i \"buzin\\|bozin\" HUB.txt 2>/dev/null | head -20\necho \"=== CHEUNG ===\"\ngrep -n -i \"buzin\\|bozin\\|*bauĵ\\|monkey\\|ape\" CHEUNG.txt 2>/dev/null | head -20\n"
}
```


### [2026-09-04T18:10:58.805Z] TOOL RESULT

```
=== PHD (Pahlavi) ===
PHD_mackenzie.txt:1593:boxtan, boz- [bwhtn', bwc- I M bwxtn, bwz-] save, redeem .
PHD_mackenzie.txt:1607:boz- .......isn. v. boxtan.
PHD_mackenzie.txt:5925:alas ala.                                 apology bozisn.
PHD_mackenzie.txt:7475:roast briStan.                             salvation boxtagih, boxtarih, bozisn.
PHD_mackenzie.txt:11115:                          \~\      boz-
PHD_mackenzie.txt:11117:baladur                 ),,,w)     bozisn                    \ t-"O s.,l.)
=== HRN ===
=== HUB ===
3066:dafur buztna, buzina etc. gebraucht.
9718:p. 87, Nr. 842 — 845. Np. buzina (im pi. huzinagan) schon
=== CHEUNG ===
```


## [2026-09-04T18:11:08.756Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9705,9730p' HUB.txt\necho \"---\"\nsed -n '3055,3075p' HUB.txt\n"
}
```


### [2026-09-04T18:11:08.818Z] TOOL RESULT

```
Wb.) = phi. asman Phi. Vd. 79, Z. 9,
Darmesteter, le Zend-Avesta II, p. 93 =-
zd. *a8todana- 'Knochen-behaiter. Vgl. Sale-
mann, Shams i Fachri p. 101 Anm.
p. 77, Nr. 747. Vgl. g. satmun (inf.) : vesenj (ipt.) wagen'
ZDMG. 36, 73.
p. 78, Nr. 759. Vgl. sayum 'der dritte' Muwaffaq 128, 7; 263,
11 n. 8. w.
p. 79, Nr. 782. Vgl. WZKM. 8, 276.
p. 82, Nr. 800. Np. mdrisBba belegt v. Stackelberg, ZDMG.
48, 494.
p. 83, Nr. 808. Vgl. syr. HIID (in Ardasir-xurrah) ZDMG.
43, 397, Z. 1 (vor 544 p. Chr.).
p. 87, Nr. 842 — 845. Np. buzina (im pi. huzinagan) schon
im alten Korancommentar, JRAS. 1894, 449.
p. 87, Nr. 861. Np. kal (wo vorkommend?) = ka6al *calvus*
= zd. kaurva-, lat. calvus, Geiger, Idg. F.
IV, Anz. 23. Lat. calvus (aus *calovos) zu
skr. kulva-- (in atikulva-) Solmsen, Stndien
zur lat. Lautgesch. p. 136. Idg. Grundform
also klvO'.
p. 89 unten. Hierher np. kahar *hellbraun* (Polak, Persien
II, p. 108) = zd. kadrva-, skr. kadru- roth-
braun*, Geiger, Idg. F. IV, Anz. p. 23. Zn
kahar aus *kahr vgl. taham aus tahm (p. 175).
p. 90, Nr. 885. Fr. Muller, WZKM. 8, 281 stellt np. gas^-
---
schen ein idg. k voraus.
840. Dazu nach Geiger hsA, kdh 'frisches griines Gras,
das, wenn es nicht entlehnt ist, auf iran. *kah€h =
*) Besser: hari = idg. kor9 zweisilbig.— 87 —
skr. ^JfOsa^ zuriickgeht. Den Lauten nach kann das
Wort sowohl Lehnwort wie Originalwort sein.
842. Vgl. modern asp i kdtbud *Grausehimmer, Kosen,
Np. Sprachftihrer p. 38.
Hier fehlt np. kaM 'Affe JRAS. 1894, p. 480 = phi.
hapik, arm. LW. kapik, skr. Icapi-. Das Wort ist
in alter Zeit aus dem Indischen entlehnt. Jetzt wird
dafur buztna, buzina etc. gebraucht.
845. Lies afgh. kon (fem. kana *taub'). Vgl. Idg. Forsch.
Ill, 169, Anm.
848. Man erwartet karg, das in den Dialekten (vgl. ZDMG.
32, 535 ; 38, 80) mit kark etc. wechselt. Dazu kas.
karged4n *Nest' (von Menschen gemacht) Shuk. p. 55.
850. Die Bedeutung von zd. kerema- ist ganz unsicher.
Ueber skr. krimi- siehe Idg. Forsch. Ill, 161.
852. Fur skr. kuksi- wie fiir lit. kmzys miisste man np.
*A:wi erwarten. Arab, kuss 'pudendum muliebre sieht
```


## [2026-09-04T18:11:29.886Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"gibbon\\|bojin\\|bandar\\|monkey\" HJB.txt | head -30\n"
}
```


### [2026-09-04T18:11:29.945Z] TOOL RESULT

```
1460:32  5. — Apollo  Bunder.  Mr.  S.  M.  Edwardes  {History  of  Bombay^  Town and  Island^  Census  Report^  1901,  p.  17)  derives  this  name  from *  Pallav  Bandar,' '  the  Harbour  of  Clustering  Shoots.'
2120:Gate.'  The  name  is  said  to  be  a corruption,  and  probably  is  so,  but of  what  it  is  a  corruption  is  not  clear. The  quotations  given  afford  different suggestions,  and  Dr  Wilson's  dictum is  entitled  to  respect,  though  we  do not  know  what  pdlawd  here  means. Sir  G.  Birdwood  writes  that  it  used to  be  said  in  Bombay,  that  ApoUo- bandar  was  a  corr.  of  pa^io-bandar, because  the  pier  was  the  place  where the  boats  used  to  land  pahoa  fish. But  we  know  of  no  fish  so  called ; it  is  however  possible  that  the  paUa or  SaJble-fuiK  ^Hilsa)  is  meant,  which is  so  called  m  Bombay,  as  well  as in  Sind  [The  A^  (ii.  338)  speaks of  ^a  kind  of  fish  callea  vcdwah  which comes  up  into  the  Inaus  from  the sea,  unnvalled  for  its  fine  and  ez- Quisite  flavour,"  which  is  the  Hilsa.] On  the  other  hand  we  may  observe that  there  was  at  Calcutta  in  1748 a  freuuented  tavern  called  the  Apollo (see  Longy  p.  11).  And  it  is  not  im- possible that  a  house  of  the  same name  may  have  given  its  title  to  the Bombay  street  and  wharf.  But  Sir Michael  Westropp's  quotation  below shows  that  PaUo  was  at  least  the native  representation  of  the  name more  than  150  years  ago.  We  may add  that  a  native  told  Mr  W.  G. Pedder,  of  the  Bom1)ay  C.S.,  from whom  we  have  it,  tliat  the  name was  due  to  the  site  having  been  the place  where  the  "po/i"  cake,  eaten at  the  Holi  festival,  was  baked.  And so  we  leave  the  matter.
2122:1847.— "A.  littie  after  sunset,  on  2nd Jan.  1848,  I  left  my  domicile  in  Ambrolie, and  drove  to  the  Ptiawi  bandar,  which reoeiTes  from  our  aooommodatiye  country- men the  more  classical  name  of  Apollo  pier." —  WiUo%,  Lands  of  the  Bible,  p.  4.
2416:BABOON,  s.  This,  no  doubt,  comes to  OS  tlirouffh  the  ItaL  hahuinoj  but it  is  probable  that  the  latter  word  is a  oormption  of  Pers.  mavmS/n  FHhe auspicious  one  1  and  then  applied  by way  of  euphemism  or  irony  to  the baboon  or  monkey.  It  also  occurs in  ItaL  under  the  more  direct  form of  maimone  in  gaUo-maimoney  'cat- monkey/  or  rather  *  monkey-cat'  [The N^.D,  leaves  the  origin  of  the  word doubtful,  and  does  not  discuss  this among  other  suggested  derivations:]
2698:BANDAREE,
2712:1548. — ".  .  .  .  certain  duties  collected from  the  bandarys  who  draw  the  toddy {sura)  from  the  aldeas.  .  .  ." — S,  Batelho, Tambo,  203.
2713:1644.— "The  people  ...  are  all  Chris- tians, or  at  least  the  g^reater  part  of  them consisting  of  artizans,  carpenters,  c/umdaris (this  word  is  manifestly  a  mistranscription  of bandaris),  whose  business  is  to  gather  nuts from  the  coco-palms,  and  eoriimbis  (see KOONBEE)  who  till  the  ground.  .  .  ."— BocarrOf  MS.
2715:„  ".  .  .  besides  60  Field-pieces  ready in  their  Carriages  upon  occasion  to  attend the  Militia  and  Bandarines." — Ibid,  66.
2716:c.  1760.—"  There  is  also  on  the  island  kept up  a  sort  of  militia,  composed  of  the  land- tillers,  and  bandarees,  whose  living  depends chiefly  on  the  cultivation  of  the  coco-nut trees."— G^/wc,  i.  46.
2718:1810. — "Her  husband  came  home,  laden with  toddy  for  distilling.  He  is  a  bandari or  toddy-gatherer."— i/aria  Gi-aham,  26.
2734:BANDEL, 'n.p.  The  name  of  the old  Portucuese  settlement  in  Bengal about  a  mile  above  Hoogly,  where  there still  exists  a  monastery,  said  to  be  the oldest  church  in  Bengal  (see  Imp. Gaseteer).  The  name  is  a  Port,  corrup- tion of  bandar,  *  the  wharf ' ;  and  in this  shape  the  word  was  applied  among the  Portuguese  to  a  variety  of  places. Thus  in  Correa,  under  1641-42,  we find  mention  of  a  port  in  the  Red Sea,  near  the  mouth,  called  Bandel dos  Malemos  0  of  the  Pilots ').  Chitta- gong  is  calleci  Bandel  de  Chaiigao  (e.g. m  Bocarro,  p.  444),  corresponding  to Bandar  Chdtgdm  in  the  Autobiog.  of Jahangir  {Elliot,  vi.  326).  [In  the Diarjr  of  Sir  T.  Roe  (see  below)  it  is applied  to  (Gombroon],  and  in  the following  passage  the  original  no  doubt runs  Bandar-i-Hvghll  or  Hngll-Bandar,
3045:1766.— "  Bandar  BaMai."— If imi-i-^A- nuuU,  Bird's  tr.,  129.
3353:1589.— * 'There  the  Bandara  (Bendara)  of Malaca,  (who  is  as  it  were  Chief  Justicer among  the  Mahometans),  (o  supremo  no mando,  na   konra  e  ne  pistica  dos  mouros)
3357:1561. — ^'Entfiomanson  .  .  .  quedizerque matfoi  o  seu  bandara  polo  mao  conselho  que Ihe  devo." — Correa,  Lmdat,  ii.  225.
3365:1726.— "  BandaroB  or  AdoMinge^re  those who  are  at  the  Court  as  Dukes,  Counts,  or even  Princes  of  tiie  Royal  House."— Fo&ji- t^  (Ceylon),  Names  of  Officers,  dx.,  8.
3520:„  ' '  The  Monkey  Beioan  which  are  long, are  the  best.  .  .  /*—Ilnd.  212.
4136:1756.— "Bandar  of  Bhrtch."— (Bird's  *»*. of)  MiraU'Akmadi,  115.
4388:c.  1S44.— "The  profit  of  the  treasury, which  they  call  bandar,  consists  in  the right  of  buying  a  certain  portion  of  all  sorts «f  cargo  at  a  fixed  price,  whether  the  ff oods be  omy  worth  that  or  more;  and  wis  is «aned  the  Law  of  the  Bandar."--Ibn  BaMa, IT.  120.
4938:CALYAN,  n.p.  The  name  of  more than  one  city  of  fame  in  W.  and  S. India  ;  Skt.  Kalydna^  'beautiful,  noble, propitious.'  One  of  these  is  the  ])lace still  known  as  KcUydn^  on  the  Ulas  river, more  usually  called  by  the  name  of  the city,  33  m.  N.E.  of  Bombay.  This  is a  ver/  ancient  port,  and  is  probably the  one  mentioned  by  Cosmas  below. It  appears  as  the  residence  of  a  donor in  an  inscription  on  the  Kanheri  caves in  Salsette  (see  FergvMon  and,  Burgess^ p.  349).  Another  Kalsrana  was  the capital  of  the  Chalukyas  of  the  Deccan in  the  9th-12th  centuries.  This  is  in the  Nizam's  district  of  Naldrug,  about 40  miles  E.N.E.  of  the  fortress  called by  that  name.  A  third  Ealyana  was a  port  of  Canara,  between  Mangalore and  Kundapur,  in  lat.  13**  28'  or  there- abouts, on  the  same  river  as  Bacanore (q.v.).  [This  is  apparently  the  place which  Tavemier  (ed.  Ball,  ii.  206) calls  Callian  Bondi  or  Kalydn  Bandar.} The  quotations  refer  to  the  first  Calyan.
5081:o.  1580.— "And  passing  into  the  heart  of the  Island,  there  came  to  the  Kingdom  of Caadia,  a  certain  Friar  Pascoal  with  two companions,  who  were  well  reoeired  by  the King  of  the  country  Javira  Bandar  ...  in so  much  that  he  gave  them  a  great  piece  of ground,  and  everything  needral  to  huild  a church,  and  houses  for  them  to  dwell  in."— CoutOf  Dec.  VI.  liv.  iv.  cap.  7.
5353:„  "In  this  country  (Calicut)  a  great number  of  apes  are  produced,  one  of  which is  worth  4  oasia,  and  one  oasM  is  worth  a q%uUtruu>."—Ibid.  172.  (Why  a  monkey should  be  worth  4  wtse  is  obscure.)
6707:GGAST,  THE.  n.p.  Tliis  term  in lK)oks  of  the  18th  century  means  the *  Madras  or  Coromandel  Coast,*  and often  *the  Madras  Presidency.'  It  is curious  to  find  IlapaXia,  "the  Shore,** applied  in  a  similar  specific  way,  in Ptolemy,  to  the  coast  near  Cape Comorin.  It  will  be  seen  that  the term  ^^ Coast  Army,**  for  "Madras Army,**  occurs  quite  recently.  The Persian  rendering  of  CoaM  Army  by Bandart  below  is  curious.
6826:The  more  common  etymology  is  that which  is  given  by  Barros,  Garcia  de Orta,  Linschoten,  &c.,  as  from  a Spanish  word  coco  applied  to  a  monkey's or  other  grotesque  face,  with  reference to  the  appearance  of  the  base  of  the shell  with  its  three  holes.  But  after all   may   the  term  not  have   origin-
6846:1568. — " .  .  .  We  have  spven  it  the  name of  0000,  because  it  looks  uke  the  face  of  a monkey,  or  of  some  other  animal." — Garcia, 666.
7227:OONOO-BUNDEB,  CONa,  n.p. Rung  bandar  J  a  port  formerly  of  some consequence  ana  trade,  on  the  north shore  of  the  Persian  Qulf,  about  100  m. west  of  Gombroon.  The  Portuguese had  a  factory  here  for  a  good  many years  after  their  expulsion  from  Or- nius,  and  under  treaty  with  Persia, made  in  1625,  had  a  right  of  pearl- fishing  at  Bahrein  and  a  claim  to  half of  the  customs  of  CJong.  These  claims seem  to  have  been  gradually  disre- garded, and  to  have  had  no  effect after  about  1670,  though  the  Portu- guese would  appear  to  have  still  kept up  some  pretext  of  monopoly  of  rights there  in  1677  (see  Chardin,  ed.  1735, i.  348,  and  Bruc^s  Annals  of  the  E.I.C.. iii.  393).  Some  confusion  is  created by  the  circumstance  that  there  is  an- other place  on  the  same  coast,  called KongHn,  which  possessed  a  good  many vessels  up  to  1859,  when  it  was  de- stn^ed  bv  a  neighbouring  chief  (see Stiffe^B  P.  Gulf  Pilot,  128).     And  this
7229:1652. — '*Near  to  the  place  where  the Euphrates  falls  from  Balsara  [see  BAL80RA] into  the  Sea,  there  is  a  little  Island,  where the  Barques  generally  come  to  an  Anchor. . . . There  we  stay'd  four  days,  whence  to Bandar-Congo  it  is  14  days  Sail.  .  .  .  This place  wo'uld  be  a  far  better  habitation  for the  Merchants  than  OrmuSf  where  it  is  rery unwholsom  and  dangerous  to  liye.  But that  which  hinders  the  Trade  from  Bandar- Congo  is,  because  the  Road  to  Lar  is  so bad.  ...  The  30th,  we  hir'd  a  Vessel  for Bander-Abasaij  and  after  3  or  4  hours  Sail- ing we  put  into  a  Village  ...  in  the  Island of  Kectmishe"  (see  ilBBJ/L).—Tavemitr, B.T.  i.  94.
7230:1053.— "Congue  est  vne  petite  viUe  fort agreable  sur  le  sein  Persique  a  trois  joum^s du  Bandar  Abbassi  tirant  k  I'Ouest  doming par  le  Schah  .  .  .  les  Portugais  y  ont  vn Feitour  (see  FACTOR)  qui  prend  la  moiti€ de  la  Douane,  et  donne  la  permission  aux barques  de  tiauiger,  en  luy  payant  vn  certain droit,  parceque  toutes  ces  mers  sont  tribu- taires  de  la  generality  de  Mascati,  qui  est k  I'entr^  du  sein  Persique.  .  .  .  Cette  yille est  peupl^  d'Arabes,  de  Parsis  et  d'Indous qui  ont  leur  Pagodes  et  leur  Saincts  hors  la Tine."— Z>c  la  Boullaye-U-Gouz.  ed.  1667, p.  284.
7289:E  either  under  the  head  of  oook-roomi, ans,  or  other  expenses  whatever." — Tke t*8  Letter,  Biaroh  3,  in  Long,  180. 1878. — "I  was  one  day  watching  an  old female  monkey  who  had  a  young  one  by  her side  to  whom  she  was  giving  snudi  bits  of  a piece  of  bread  which  we  had  evidently  just received  from  my  oook-TOOm." — Life  xn  the MqfvLuil,  ii.  44.
7889:188S.— "There  is  that  unffainly  object  the cmteal,  orow-phaaaant,  jungle-orow,  or  what- ever else  you  like  to  call  the  miscellaneous thing,  asitchtmbers  through  a  creeper-laden bush  or  spreads  its  reddish-bay  wings  and niakes  a  slow  voyage  to  the  next  tree.  To judge  by  its  appearance  only  it  mi^ht  be  a crow  developing  for  a  peacock,  but  its  voice seems  to  have  been  borrowed  from  a  black- faoed  monkey."— TWbef  on  my  Frontier^  155.
9656:1565. — "  Suddenly  news  came  from  Thatta that  the  Firingls  had  passed  Lahori  Bandar, and  attacked  the  dty, '—TaHihri-Tdkiri,  in Elliot,  I  276.
```


## [2026-09-04T18:11:41.306Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=gibbon",
 "prompt": "Give the full etymology/origin note for the word \"gibbon\" (the ape) as printed on this American Heritage Dictionary page, if present."
}
```


## [2026-09-04T18:11:42.624Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/bau%C4%B3an-",
 "prompt": "Give the full content of this Proto-Iranian reconstruction page (root meaning \"monkey/ape\"), including descendants list and any note about Persian buzine/بوزینه."
}
```


### [2026-09-04T18:11:44.745Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T18:11:45.340Z] TOOL RESULT

```
# Etymology of "Gibbon" (the ape)

According to the American Heritage Dictionary entry, the origin note states:

"[French, applied to the animals by Georges Louis Leclerc de Buffon in his *Histoire Naturelle*, in which the word is said to be a local name in a language of Southeast Asia.]"

The term derives from French usage, where naturalist Buffon applied it to these animals, with the word itself reportedly originating as a local designation in a Southeast Asian language.
```


## [2026-09-04T18:11:55.478Z] TOOL CALL #40: Bash

```json
{
 "command": "\\\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/gibbon' --note 'page 33, node 6/7 gibbon: modern Etymonline account, French <Indies word not identified in any language>, no Persian/Arabic link' && \\\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/borage' --note 'page 33, node 8/9/10 borage: two competing theories, Arabic abu-arak vs Latin borra' && \\\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/arrack' --note 'page 33, node 3 abu-araq: Arabic araq sweat/juice -> arrack chain, cross-check' && \\\npython3 tools/fetch_source.py 'https://www.ahdictionary.com/word/search.html?q=borage' --note 'page 33, node 3/8/9/10 borage: AHD confirms Arabic abu-arak \"father of sweat\" etymology, Nourai cites AHD:152' && \\\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/borage' --note 'page 33, node 8/9/10 borage: Wiktionary gives both Latin burra and Arabic abu l-arak theories without preference'\n"
}
```


### [2026-09-04T18:11:57.997Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5480297bf52b0bbb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7132c6e9ee680f10.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3330ab177a4310bb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/343f0d6122563b9e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1f5b311fdd534ea6.txt
```


## [2026-09-04T18:11:59.969Z] TOOL CALL #41: Bash

```json
{
 "command": "\\\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/gibbon' --note 'page 33, node 6/7 gibbon: modern Wiktionary derives from Northern Aslian (cf. Batek kəboɲ), not from Persian/Arabic' && \\\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%B2%DB%8C%D9%86%D9%87' --note 'page 33, node 4 Persian buzineh: Wiktionary says inherited from Proto-Iranian, cf Pashto بيزو, source of Russian obezyana - contradicts Arabic abu-zina derivation' && \\\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D8%B1%D8%A7%D9%87%DB%8C%D9%85' --note 'page 33, node 15 Persian Ebrahim: borrowed from Arabic Ibrahim < Aramaic < Biblical Hebrew Abraham' && \\\npython3 tools/fetch_source.py 'https://www.ahdictionary.com/word/search.html?q=gibbon' --note 'page 33, node 6/7 gibbon: AHD - Buffon applied French gibbon, said to be local Southeast Asian name, no Persian/Arabic link'\n"
}
```


### [2026-09-04T18:12:02.166Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5b69fb503d4db1b7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a79258c7fe012fe6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1434f0e1b9b9efaf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d4fcfb7cc6766634.txt
```


## [2026-09-04T18:12:07.502Z] TOOL CALL #42: Bash

```json
{
 "command": "for f in 5480297bf52b0bbb 7132c6e9ee680f10 5b69fb503d4db1b7 a79258c7fe012fe6; do\necho \"=== $f ===\"; wc -l /home/sfmqrb/git/rishe/data/verification/sources/web/$f.txt; grep -m2 -i \"gibbon\\|borage\\|buzin\\|Aslian\\|burra\" /home/sfmqrb/git/rishe/data/verification/sources/web/$f.txt\ndone\n"
}
```


### [2026-09-04T18:12:09.164Z] TOOL RESULT

```
=== 5480297bf52b0bbb ===
154 /home/sfmqrb/git/rishe/data/verification/sources/web/5480297bf52b0bbb.txt
URL: https://www.etymonline.com/word/gibbon
TITLE: Gibbon - Etymology, Origin & Meaning
=== 7132c6e9ee680f10 ===
156 /home/sfmqrb/git/rishe/data/verification/sources/web/7132c6e9ee680f10.txt
URL: https://www.etymonline.com/word/borage
TITLE: Borage - Etymology, Origin & Meaning
=== 5b69fb503d4db1b7 ===
540 /home/sfmqrb/git/rishe/data/verification/sources/web/5b69fb503d4db1b7.txt
URL: https://en.wiktionary.org/wiki/gibbon
TITLE: gibbon - Wiktionary, the free dictionary
=== a79258c7fe012fe6 ===
254 /home/sfmqrb/git/rishe/data/verification/sources/web/a79258c7fe012fe6.txt
 buzine
 buzina
```


## [2026-09-04T18:12:12.417Z] AGENT

Good, all archived with real content. Now let me check a couple more nodes and the FVQ page structure, then write the output file.


## [2026-09-04T18:12:13.668Z] TOOL CALL #43: Bash

```json
{
 "command": "grep -o \"gibbon.\\{0,400}\" /home/sfmqrb/git/rishe/data/verification/sources/web/5480297bf52b0bbb.txt | head -5\necho \"---borage---\"\ngrep -o \"borage.\\{0,400}\\|borra.\\{0,300}\" /home/sfmqrb/git/rishe/data/verification/sources/web/7132c6e9ee680f10.txt | head -5\n"
}
```


### [2026-09-04T18:12:15.476Z] TOOL RESULT

```
gibbon
gibbon 
gibbon (n.) 
gibbon (18c.), supposedly from a word in the French colonies of India but not found in any language there. Brought to Europe by Marquis Joseph-François Dupleix (1697-1763), French governor general in India 1742-54. The surname is Old French Giboin , from Frankish *Geba-win "gift-friend," or in some cases a diminutive of Gibb , itself a familiar form of Gilbert .
gibbon 
---borage---
borage
borage 
borage (n.) 
borage (13c., Modern French bourrache ), from Medieval Latin borrago , which also is the source of Spanish boraja , Italian borraggine , German Boretsch .
borra "rough hair, short wool," in reference to the texture of the foliage. Related: Boraginaceous .
```


## [2026-09-04T18:12:20.731Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/%CA%BEab-",
 "prompt": "Give the full content: the reconstructed Proto-Semitic root for \"father\", its descendants list, and any etymology note."
}
```


### [2026-09-04T18:12:27.922Z] TOOL RESULT

```
# Proto-Semitic Root for "Father"

## Reconstructed Root
The entry documents **\*ʔabw-** (masculine noun), meaning "father," with plural **\*ʔaban-**.

## Etymology
According to the article, this term derives from "Proto-Afroasiatic *ʔab- ("father"), ultimately an onomatopoeic nursery word." The entry notes cognates across Afroasiatic languages including Egyptian, Proto-Berber, Hausa, Somali, and Afar variants.

## Major Descendants
The documented descendants span multiple Semitic branches:

**East Semitic:** Akkadian *abum*

**West Semitic branches include:**
- Arabic *ʔab* (with Maltese *bu*)
- Aramaic *ʾabā'* (yielding Classical Syriac and Ancient Greek *abba*)
- Hebrew *av* (אָב)
- Ugaritic *ʾabu*
- Phoenician and Punic *ʾab*
- Old South Arabian forms (Minaean, Qatabanian, Sabaean)
- Ethiopian Semitic: Amharic *ʾabbat*, Ge'ez *ʾäb*, Tigre *ʾäb*, Tigrinya *ʾabo*

## Reconstruction Note
The entry notes scholarly variation: "The final consonant of the stem is inferred based on construct forms, but Kogan reconstructs this item as \*_ʔab-_ instead."
```


## [2026-09-04T18:12:31.921Z] TOOL CALL #45: Bash

```json
{
 "command": "python3 /home/sfmqrb/git/rishe/tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/%CA%BEab-' --note 'page 33, root Ab 2: confirms Proto-Semitic *ʔabw-/*ʔab- father, from Proto-Afroasiatic *ʔab-, an onomatopoeic nursery word'"
}
```


### [2026-09-04T18:12:33.669Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7191e2277240767c.txt
```


## [2026-09-04T18:12:36.604Z] AGENT

Now let me build the output JSON with all findings.


## [2026-09-04T18:12:38.212Z] TOOL CALL #46: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet\nls /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet"
}
```


### [2026-09-04T18:12:38.269Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:12:52.675Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==70' LKT.txt | head -60"
}
```


### [2026-09-04T18:12:54.273Z] TOOL RESULT

```
s  Abwärtsgleiten  des  Dirhams  für die  ersten  tausend  Jahre  der  Hedschra bis  auf  den  50.  Teil  seines  ursprünglichen Wertes  nachgewiesen  wird],  vulgär  aus- gesprochen dirhem  [das  ar.  Wort  kommt selbst  aus  gr.  bpaxMn  ZDMG  LI,  297, das  auf  bpdTTU),  bpäTTOiuai  zurückgeführt wird  u.  soviel  wie  'eine  Handvoll',  sc. von  Spießen,  bedeutet];  hieraus  frz. dirhem,  sp.  adereme,  adarme,  pg.  adarme 'Gewicht  od.  Münze',  pg.  auch  figürlich 'geringfügige  Sache'  [Gonstancio  Dice 21b];  über  das  tk.  drem  wurde  rum. dram  'ein  Quentchen,  V^oo  einer  Okka [s.  hier  Nr.  1.590]',  also  in  der  Walachei 3,370  g,  in  der  Moldau  3,229  g.  [DE 41.    Devic  DEt  103.
524.  Ar.  dis:
'Schilfrohr, Ginster',  Einheitsnomen Äsa ; hieraus  siz.  ddisa  'grasartige  Pflanze', aus  der  man  Seile  macht  oder  mit  der man  Reben  bindet  u.  dergl.,  sp.  aldiza 'Ginster'  [aciano  menor].  [GrSVociSic233. DE  97.    Eguilaz  148.    ML  2650.
525.  Ar.  disär:
'Starker  Palm  hast,  Schnur  daraus';  hier- aus mit  ar.  Art.  und  häufigem  Wechsel von  r  zu  l  sp.  adazal  'eine  Angel  mit Sparto,  die  zum  Fange  des  Tunfisches benutzt  wird'.    [DE  44.
526.  Pers.  diwän:
[Letzten  Endes  von  ^evs.dibir  'Schreiber' Horn  NpEtS.  119,  Nr.  540]  'Amtszimmer, Rat,  Tribunal',  hieraus  wurde  der  Sitz des  Beamten,  ein  bequemer  Sitz,  ein Ruhelager,  andererseits  aber  auch  Samm- lung von  Gedichten  eines  oder  mehrerer Dichter,  jedoch  nur  auf  den  Orient  be- züglich. Im  einzelnen  hat  man :  sp.  pg. aduana  'Zollhaus',  prov.  doana,  frz. douane,  it.  doana,  dogana  [mit  Konta- mination von  *ducana  aus  dux  >  doge] 'dass.'.  Frz.  divan  'Ruhebett',  it.  divano, rum.  divan,  russ.  bulg.  diivan,  öech.  dy- van,  dtsch.  Diwan,  engl,  divan,  angloind. dewaun  'Ruhebett,  Gedichtsammlung'. —  Aus  tat.  duwan  [Wechsel  zwischen u  und  i  im  Tk.  häufig,  vgl.  z.  B.  osm. diwar  und  duwar  'Wand'],  duwan  etmek 'richten'  kommt  russ.  duwan  'Teilung eines  Gewinns',  duwanit'  'eine  Beute, Gewinn  teilen'.  [DE  47.  Eguilaz  61. Devic  DEt  104.  ML  2707.  Gorjajew  91 u.  98.  Hobson-Jobson  309/311.
527.  Tk.  dizgiii:
'Zaum,  Zügel'  [vom  Stamme  tir,  tiz,  s. hier  Nr.  522] ;  hieraus  rum.  diaghin, desghin  'Kapriole  (des  Pferdes)',  bulg. serb.  dizgin,  serb.  dizden  'Zügel'.  [Bern SlEtWb  203.
528.  Tk.  dojum:
'Großer  Haufe'  [vom  Stamme  tok,  toj 'dicht,  fest,  volP  Vämbery  TktEtWb S.  179,  Nr.  1931];  hieraus  rum.  duium 'Haufe,  großer  Auflauf.
529.  Pers.  döläb:
'Schrank',  ebenso  ik.dolap;  hieraus  rum. dulap  'Schrank,  Schaukel'  [das  letztere nach  Sain  51],  fig.  'Intrige'  [nach  Löbel EITAP  40],  Abltg.  duläpärie,  duläpior; bulg.  dulap  'Schrank'.
530.  Tk.  dolaina:
'Roter  Tuchmantel,  den  die  Janitscharen als  Paradeanzug  trugen';  hieraus  rum. dulama  'langes  Unterkleid,  Damenober- kleid',  Abltg.  dulämifä;  bulg.  dolama 'langes  Oberkleid',  serb.  dolama  'langes Unterkleid',  russ.  doloman,  dolman,  kl- russ.  doloman,  poln.  dolman  'kurzer Husarenmantel',  öech.  doloman,  dolman 'ungarischer  Pelzrock';  dtsch.  Dohna)}, frz.  doliman,  dolman  'Husarenjacke'. [Gorjajew  104.  Bern  SlEtAVb  206.  Devic DEt  104.
531.  Tk.  doldur-:
Doldurmak  'füllen'  ['voll  machen',  Kau-
43
[Tk.  dory.
saliv  zu  dolu  'voll'  vom  Stamme  tok  usw., s.hier  Nr.528],  subst.  Infinitiv  doldurma; hieraus  rum.  doldora  'voll,  strotzend'.
.5312.  Tk.  dory: 'Braun'  (vom  Pferde)  [Kelekian  Kämüs 81()];  hieraus  bulg.  rforya,  rfory esi 'dass.', serb.  dorin  [und  von  tk.  dory  at  'braunes Pferd',  s.  hier  Nr.  128J,  dorat  'Pferd  von brauner  F'arbe'.    [Bern  SlEtWb  211.
533.  Tk.  dösek:
'Bett,  Matratze'  [vom  Stamme  töz,  tos, tös  'glatt,  eben,  glätten,  ausstrecken' Vämbery  TktEtWb  S.  190,  Nr.  202]; hieraus  bulg.  serb.  dusek  'Matratze',  russ. tjufjak  'Matratze,  träger  Mensch'.
534.  Tk.  döseme:
'Möbel,  Tapezieruiig'  [subst.  Infinitiv, vom  gleichen  Stamme  wie  Nr.  533]; hieraus  rum.  du^umea  'Fußboden'.
535.  Ar.  dubb:
'Bär',  vollständig  ad-dubb  al-akbnr  'der Große  Bär';  hieraus  der  Sternname Dubhe  a  ürsi  maioris.  [Ideler  Sternn  23.
536.  Tk.  dndnk:
'Flöte'  [vom  gleichen  Stamme  wie  dudak 'Lippe',  eigentlich  'Erfasser',  vom  Stamme tok  usw.  'fassen',  s.  hier  Nr.  528];  hieraus bulg.  serb.  duduk  'Pfeife,  Schalmei',  russ. dudka,  dudak,  dudocka  'Schalmei',  ßech. dudy  'Dudelsack'.  Aus  dem  slav.  wahr- scheinlich dtsc-h.  dudeln,  Dudelsack. [Gorjajew  98.  Bern  SlEtWb  233.
537.  Ar.  dnff:
'Trommel,  Tamburi
```


## [2026-09-04T18:13:02.046Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^[0-9]\\+\\.\\s*Ar\\.\\s*ab[^a-z]\" LKT.txt | head\ngrep -n \"Ar\\. ab:\" LKT.txt\ngrep -n \"^44\\.\\|^ *44\\.\" LKT.txt | head -5\n"
}
```


### [2026-09-04T18:13:02.119Z] TOOL RESULT

```
243:11.  Ar.  abü  kirdän:
247:13.  Ar.  abü  rag':
249:14.  Ar.  abü  tilün:
315:44.  Ar.  'akida: 'Rosenkonserve,  Bonbon',  plr.  'akiVid; hieraus  tk.  akyde  sekeri  'Karamel),  Ger- stenzucker' [Kelökian  Kämos  855]  od. kurz  akede  [A.  Hindoglu,  Dictionnaire Turc-Fran(;ais.  Vienne  1838.  S.  329]. Wohl  aus  dieser  Form  rum.  acadea, acadele  'dass.'.
```


## [2026-09-04T18:13:11.309Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '225,260p' LKT.txt"
}
```


### [2026-09-04T18:13:11.361Z] TOOL RESULT

```
Lokotsch,  Etymolog,  Wörterbuch.
4.  Ar.  'Abbäs:
N.  pr.  Nach  dem  pers.  Schah  'ABBAS  I. [1586 — 1628]  wurde  eine  Münze  mit seinem  Bilde  so  genannt  [vgl.  Napoleon d'or,  Louis  d'or];  hieraus  russ.  «6«^ 'Münze  von  20  Kopeken'.    [Gorjajew  1.
5.  Pers.  abdär:
[Aus  äb  'Wasser'  od.  'Glanz'  Hoi-n  NpEt S.  1,  Nr.  2  und  3,  und  Stamm  där- 'habend,  haltend'  ebda.  S.  116,  Nr.  527] 'wässerig,  hell,  glänzend'  [von  Stahl od.  Waffen  gesagt].  Über  das  tk.  hier- aus rum.  abitir  'besser,  vortrefflicher'; russ.  ob'jar  'Art  Stoff'.
6.  Ar.  abjad :
'Weiß'.  Hieraus  fiz.  abit  'Bleiweiß', alter  chemischer  Terminus.  Aus  dem ar.  Subst.  bajäd  'Weiße'  wurde  mit  ar. Art.  sp.  albayalde  'kohlensaures  Blei- salz', Vb.  albayaldar.    [Devic  DEl  1.
7.  Pers.  äbkärl:
[Aus  pers.  äb  s.  hier  Nr.  5  und  kär 'Werk,  Tat'  Horn  NpEt  S.  185,  Nr.  831; dazu  das  T  des  AbstraktumsJ,  ebenso bind.  'Wasserarbeit'.  Hieraus  angloind. abcaree,  abkary  ursprünglich  'die  Arbeit, Wasser  zu  destillieren  und  zu  verkau- fen', heutzutage  'die  Steuer  auf  diesas Geschäft'.  Abkary-System  ist  also das  System  der  Besteuerung  geistiger Getränke  in  Britisch-Indien.  [Hobson- Jobson  2.
8.  Hebr.  Abraham:
N.  pr.  [  Volksetymologisch  '  Vater  der Menge'].  lu  frz.  Dialekten  in  der  Be- deutung 'Milchstraße',  wallon.  abe d'Abraham  [—  arbre  d'A.]  sind  fächer- förmig vom  Horizont  aus  sich  über  den Abendhimmel  ausbreitende  Wolkenge- bilde.   [Wartbg  FEWb  8.
9.  Ar.  abras:
Auch  tk.  'Pferd  mit  weißen  und  schwar- zen Füßen'.  Hieraus  rum.  abra§  'ge- fleckt, buntscheckig',  tig.  'Unheil  ver- kündend'; im  walachischen  Dialekt iabrai^,  iambra^  'Pferd  mit  weißen Flecken'.
10.  Pers.  äbresäui:
[Horn  NpEt  S.  16,  Nr.  65]  'Seide',  ent- weder gehaspelte  od,  gedrehte,  gezwirnte 1
Ar.  ahn  kirdäii.]
2
Ganzseide  [auch  ins  Semitische  über- gegangen :  syr.  abräsom,  ahr'isüm  BrLex- Syr  ob;  ar.  ibnsam,  ibrisum,  schon häufig  mit  der  Bedeutung  'Seidenfaden, Seidenzwirn',  vgl.  Joseph  Karabacek, Über  einige  Benennungen  mittelallei'- 1  icher  Gewebe  I.  Wien  1882.  S.  21 bis  2'2.].  Ins  Tk.  übergegangen  als  ibri- sim  [offenbar  mit  Anlehnung  an  die Wurzel  ip,  ib  'winden'  Vämbeiy  Tkt- EtWb  Nr.  37].  Aus  dem  Tk.  wurde  rum. ibri^im,  ibri^in  'Seidenfaden,  Zwirn'; Ableitung  ibri^inar.
11.  Ar.  abü  kirdän:
[Wörtlich  „Vater  der  Zecken",  die  ar. kiräd,  plr.  kirdän  heißen].  Der  rein weifae  'Kuhreiher',  Ardea  bubuleus  Sa- vigny,  ein  afrikanischer  Vogel  [die Schreibung  aboogerdan  bei  ML  36  wie schon  vorher  bei  Körting,  Lateinisch- romanisches Wörterbuch.  3.  Aufl.  Pader- born 1907,  s.  V.  ist  englisch].  Durch volksetymologische  Neugestaltung  hier- aus vielleicht  frz.  bwuf-garde,  garde- bcfuf  'eine  Art  Silberreiher'.  [FASS in  RomForsch  III,  488.  KURYLOWICZ in  Rocznik  Orientalistyczny.  Tom  II. Lwöw  1925.    S.  252.
12.  Ar.  'abar:
In  der  Zusammensetzung  as-sirä  al- "abiir  'der  [sc.  auf  der  Milchstraße] wandernde  Sirius'  [hierzu  s.  hier  Nr.  1915] vom  ar.  Stamme  'fcr  'wandern'  [vgl. hebr.  "ibrl  'Hebräer',  d.  h.  derjenige,  der gewandert  ist  od.  überschritten  hat  sc. den  Euphrat  od.  Jordan].  Hieraus  Alha- bor,  Alchabar  als  Name  des  Sirius  a Ganis  majoris.  [Devic  DEt  40/41. Ideler  Sternn  237  und  246.
13.  Ar.  abü  rag':
'Vater  des  Schweißes',  hieraus  lat.  bor- rago,  eine  Pflanze,  die  durch  die  ar. Medizin  im  Mittelalter  verbreitet  wurde. Die  romanischen  Formen  sind:  it.  bor- race,  borragine,  borrana;  prov.  borrage; sp.  borraja ;  pg.  borragem ;  frz.  hourrache. Auch  germanisch,  z.  B.  engl,  borage, dtsch.  Burrich,  Bor( rjetsch.  Wohl  über das  Ngr.  entstand  rum.  boranjä  'dass.'. Trotz  ML  1412  scheint  diese  Ableitung noch  immer  die  beste  und  wenig  an- fechtbar zu  sein.    [Kluge  64.
14.  Ar.  abü  tilün:
[Vgl.  Ihn  Sinä,  Kitäb  al-känün  fi't-tibb. Romae.  In  typographia  Medicea  1593. S.  137]  'eine  Zierpflanze'  aus  der  Familie der  Malvaceen:  Abutilon  indicum.  Hier- aus frz.  abutilon  'dass.',  nämlich  abutilon striS  Abutilon  striatum  Diks.  (Sida  striata Hort.)  und  abutilon  itendard  A.  vexilla- rium  Ed.  Morrea  (S.  vexillaria  Hort.). [Devic  DEt  3.    Lammens  Rem  3.
15.  Pers.  acär:
'Sauer',  hieraus  malay.  a£ar  [Pijn  237] in  der  Bedeutung  'Eingemachtes,  pickles' und  ebenso  in  allen  Eingeborenen- sprachen Indiens;  daher  angloind.  achar 'dass.';  frz.  achars  'Obst  od.  Gemüse, das  in  Essig  eingemacht  ist',  ein  im indischen  Archipel,  auf  Mauritius  usw. sehr  beliebtes  Gericht.  [Devic  DEt  3/4. Hobson-Jobson  3.
16.  Ar.  'äda:
'Sitte,  Gebrauch',  ebenso  Ik.  adet  'dass.'; hieraus  rum.  adet  'Brauch,  Sitte,  Regel', früher  'Steuer'.    [Sain  46.
17.  Malayälam  adakka:
[Aus  arfa/ 'enge  Anordnung  einer  Traube' und  kay  'Nuß'].  Hieraus  pg.  areca, angloind.  Areca,  worunter  man  allge- mein den  Samen  od.  die  Nuß  der  Palme, Areca  catechu  L.,  versteht.  [Hobson- Jobson  35.
18.  Ar.  'adäla:
[Aus  ar.  'adl  'Gerechtigkeit']  'Gerichts- barkeit', in  vulgärer  Aussprache  'adälet, woraus  über  das  Hind.  das  angloind. adawlut  'Gerichtshof  wurde.  —  Aus- führlich in  Hobson-Jobson  4/6.
19.  Hebr.  Ädäm:
'Mensch',  dann  N.  pr.  für  den  Stamm- vater des  Menschengeschlechtes  [vgl. assyr.  admu  'Kind,  bes.  junges  Kind' Del  HWB  25  b],  daraus  bei  den  Ana- tomen des  Mittelalters  hebr.  iappü"h ha-ädäm,  wörtlich  'Apfel  des  Mannes', zur  Bezeichnung  des  Vorsprungs  am Kehlkopf  des  Mannes  [gr.  irpöXoßo;]. Da  er  nur  am  Halse  des  Mannes  zu sehen  ist,  ist  der  Name  treffend  ge- wählt, dann  aber  durch  mißverständ- liche Übersetzung  zu  Pomum  Adami 'Adamsapfel'  geworden  und  die  bekannte Fabel  entstanden,  daß  Adam  den  ihm hingereichten  Apfel  nicht  ganz  habe verschlucken  können.  Ii. morso d'Adamo, frz.  morceau  d' Adam,  pomme  d'Adatn. Engl.  Ada7n's  apple,  schwed.  adanis aepple,  dän.  adams  üble,  ndl.  adanis  appel. Poln.  jabiko  Adamowe,  ßech.  Adamavo jahlko.  Im  Angloind.  ist  Adanis  apple die  Frucht  von  Mimusops  Elengi  L., im  It.  joomo  d'Adamo  [od.  pomo  di  para- diso]  eine  Orangenart,  Citrus  decumana. [Kluge  6.  Hobson-Jobson  4.  HArllebr- An  164.
```


## [2026-09-04T18:13:25.969Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"zin\\b\\|abü.zin\\|zina\\|buzine\\|ebüzine\" LKT.txt | head -20"
}
```


### [2026-09-04T18:13:26.027Z] TOOL RESULT

```
248:'Vater  des  Schweißes',  hieraus  lat.  bor- rago,  eine  Pflanze,  die  durch  die  ar. Medizin  im  Mittelalter  verbreitet  wurde. Die  romanischen  Formen  sind:  it.  bor- race,  borragine,  borrana;  prov.  borrage; sp.  borraja ;  pg.  borragem ;  frz.  hourrache. Auch  germanisch,  z.  B.  engl,  borage, dtsch.  Burrich,  Bor( rjetsch.  Wohl  über das  Ngr.  entstand  rum.  boranjä  'dass.'. Trotz  ML  1412  scheint  diese  Ableitung noch  immer  die  beste  und  wenig  an- fechtbar zu  sein.    [Kluge  64.
397:Mit  Assimilation  'ambar  gesprochen; hieraus  it.  ambra,  frz.  ambre,  sp.  pg. ambar,  [mit  ar.  Art.]  alambar,  alambre, rum.  ambrä,  ambru;  engl,  ambre,  ndl. amber,  dtsch.  Amber;  russ.  ambra.  — Aniber  ist  eine  ihrer  Herkunft  nach zweifelhafte,  ilirer  Zusammensetzung nach  unvollständig  bekannte,  sehr  teure, dunkelgraue  Masse,  die  in  früheren Zeiten  in  der  Medizin  hochgeschätzt war,  während  sie  heute  fast  nur  noch zur  Herstellung  von  Parfümen  benutzt wird.  In  rundlichen  oder  kantigen Stücken  auf  dem  Meere  schwimmend oder  am  Strande  angespült,  wird  die Ambra  im  Indischen  Ozean  gefunden und  für  feine  Sorten  je  kg  5000  Mark und  mehr  gezahlt.  Vermutlich  ist  der Amber  die  verhärtete  Kotmasse  des Pottwals  Catodon  macrocephalus  Lac. —  Dazu  engl,  yellow  amber  'Bernstein'. [DE  188/9.  Eguilaz  258.  ML  441. Gorjajew  4.
706:'Lager,  Magazin,  Vorhalle'  [Pijn  35b]; hieraus  angloind.  bankshall  'Warenhaus, Büro  eines  Halenmeisters'.  [Hobson- Jobson  61/62.
1413:5.56.  Tk.  ebnzine: Auch  buzine  'Affe'  [aus  ar.  abü  zina" 'Vater   der   Unzucht'];    hieraus  russ. obez'jana,  klruss.  obezjana  'Affe'  [vgl. lit.  bezdona].
1546:'Magazin,  Lager,  Wirtshaus'  [seit  Golius bereits  auf  gr.  iravboxeiov  zurückgeführt; besser  irdvboxoq] ;  hieraus  rum.  fundac 'Heuschober',  it.  fondaco.  venez.  (alt) fonteco,  (modern)  fontego,  afrz.  fondique, sp.  alhöndiga,  fundago,  pg.  alhondega, alfandega 'Zollhaus' ;  siz. f 'Wirts- haus niederster  Sorte',  wo  sicii  die  Fuhr- leute usw.  mit  ihren  Pferden  und  Maul- tieren erholen,  funnacaru  'Wirt'.  Rück- gebildet ist  sp.  fo7ida  'Hotel,  Wirtshaus'. [DE  139  u.  270.  Eguilaz  192.  Devic DEt  121.    ML  .3424.
2066:854.  Ar.  hazin:
2093:zination (puXaKTTipiov'  MSOS  XII,  192 Anm.  1).  Vgl.  auch  ZOTENBERG  in Revue  Critique  ("10.  4.  1867),  der  beide Ansichten  zu  vereinen  sucht,  und  Fausto LASINIO  in  GSAJ  III  (1889),  142.
2143:890.  Pers.  Hwärizin:
2287:9.55.  Chili,  jensheil : [Aus  jen  'Mensch'  und  shen  'die  Wurzel von  Panax  ginseng']  Name  für  die Wurzel  der  Panax  ginseng,  die  berühmte Universalmedizin  der  Chinesen;  die  Vor- setzung der  Bestimmung  jen  ist  wohl
2628:'Richter,  Führer'  [wurzelverwandt  mit ar.  kädi,  s.  hier  Nr.  984],  in  moderner Aussprache  közin  'reicher  Mann';  hier- aus jüd.-dtsch.  'ein  dicker,  fetter  Koze', in  Berlin :  so'n  Jroßkoz  'einer,  der  sich viel  auf  sein  Geld  einbildet'.
2684:'Türhüter,  Diener  der  Gesandtschaften in  der  Türkei'  [vom  ar.  kaus  'Bogen', Berufsnamen  kawwäs  eigentlich  'Bogen- schütze'] ;  hieraus  bulg.  sei'b.  kawaz,  bulg. kavazin  'Polizeidiener;  dtsch.  Kaimß, frz.  cavasse  'Konsulatswächter'.
2688:Ein  Strauch  aus  der  Familie  der  Myr- taceen,  Melaleuca  leucadendron  [auch schon  mal.  'weißer  Baum',  da  er  wie die  Birke  weiße  Rinde  zeigt] ;  aus  seinen Blättern  und  Zweigen  zieht  man  durch Destillation  ein  flüchtiges  Öl  von  durch- dringendem Gerüche:  frz.  htiile  de  caje- piit,  auch  kurz  cajeput,  pg.  cajeput,  engl. cajeput,  cajuput  'Kajeputöl'.  Es  wird in  der  Medizin  gegen  Wechselfieber  und in  der  Industrie  zur  Herstellung  von Firnis  gebraucht.  [MMM  9.  Devic  DEt 76.    JAOS  XVII,  120/123.
2859:1219.  Sskr:  krmip: 'Wurmerzeugt'  [aus  sskr.  krmi  'Wurm', vgl.  pers.  kirnt  'dass.'  Horn  NpEl  S.  190, Nr.  850],  ein  Insekt,  das,  getrocknet  und zu  Puder  gestampft,  die  rote  Farbe  gibt, die  mit  den  aus  diesem  Grundwort  sich ergebenden  Wörtern  bezeichnet  wird: Über  das  betr.  Insekt,  die  Cochenille oder  Schildlaus,  vgl.  Ed.  Wiepen,  Die geographische  Verbreitung  der  Coche- nillezucht. Köln  1890.  Zunächst  ergab sich  ar.  kinnizi  ZDMG  L,  650  und  hier- aus: it.  carmesino,  cremisino,  carminio, frz.  cramoisi,  carmin,  sp.  carmesi,  car- mtn,  quernies,  pg.  carmesim,  carmim, rum.  cänniz  [wobei  die  Formen  auf  in durch  Kontamination  mit  lat.  minium zu  erklären  sind];  ndl.  karmezijn,  kar- mozijn,  karmijn,  engl,  carmine,  dtsch. karmin ;  russ.  karmin,  karmazin,  poln. karmazyn  'scharlachrot',  kiermes,  al- kiermes  'Kermes,  Cochenille',  cech.  kar- mazin,  klruss.  karmazyn,  serb.  grimiz 'purpurrot',  bulg.  k^rm^z.  [Dozy  Oost  8. DE  185.  Eguilaz  248.  Devic  DEt  24. ML  6907/8.  Gorjajew  131  und  135. Bern  SlEtWb  491.
3097:'Javanischer  Weihraucli'  [s.  hier  Nr.  1331 ; obwohl  er  aus  Sumatra  stammt],  mit Imiila  [ä  >>  e]  luben  gäwi;  hieraus  mit Abtall  der  er.sten  Silbe  it.  henju\,  belgiu), gebräuchlicher:  belgioina,  henzoino,  frz. boijoin,  kat.  benjugi,  sp.  benjul,  menjid, pg.  beijoim,  beijuim  'Benzoegummi'; ei\\x\.benjamin,  benjoin,  chemischer  Fach- ausdruck, und  Aisdh.. Benzoe;  russ.  benzoi, poln.  benzoes.  Hieraus  weiter  it.  belztiino, frz.  benzin,  dtsch.  Benzin,  Benzol,  russ. benzin,  poln.  (dial.)  b^dzivim  usw.  [Hob- son-Jobson  86/87.  DE  !239.  Eguilaz  344. Devic  DEt  66.  Lammens  Rem  186/187. Gorjajew  15.    MWiD  86.
3151:1356.  Ar.  mahlab: 'Weichselkirschbaum,  Prunus  mahaleb'; hieraus  sp.  mahaleb  [Dicc  Gast  13U0a], frz.  mahaleb,  mahalep,  maguelet;  unter diesem  Namen  importierte  man  früher aus  Syrien  nach  Europa  eine  kleine Frucht,  die  man  in  der  Medizin  brauchte und  jetzt  noch  in  der  Parfümerie  ver- wendet. Frz.  hois  de  mahaleb  'Weichsel- holz' [vulgär  hois  de  Ste.  Lucie  genannt]. [Devic DEt  154.  Eguilaz 441/442.  ML5240
3162:1362.  Ar.  mahzan: 'Warenniedei  läge,  Scheune,  Zeughaus', plr.  mahäzin;  hieraus  it.  tnagazzino, sai'd.  magasinu,  camasinu  [mit  Meta- thesis],  SIZ.  magasenu,  maasemi,  mala- senu,  malase,  frz.  ntagasin,  sp.  magacSn, almagacen,  alniacen,  pg.  almazem,  ar- mazem,  almacen,  rum.  magaza,  magazin; dtsch.  Magazin,  ndl.  magazijn,  engl,  ma- gazi)ie ;  russ.  magazyn,  (dial )  gamazeja [Metathesis  wie  im  Sard. !],  klruss.  ma- gazyn, kamazej,  bulg.  serb.  magaza, magazin  'Warenniederlage,  Zeughaus'. [Lasii.io  8.  DE  147.  Eguilaz  205.  ML 5447  (wo  als  Grundwort  mayzen  'Scheune' gegeben  wird!).  Gorjajew  199.  Mikl SIElWb  180.
3264:'Koralle'  [aus  gr.  laapTapiTr^q  ZDMG  LI, 304],  tk.  mergan  'dass.';  hieraus  rura. märgean,  mnrgicä;  bulg.  merdzan  'Ko- ralle'. Mit  ar.  Art.  und  Imäla  [ä  >  e] «rgab  sich  der  alte  pharmazeutische Ausdruck  frz.  almargen:  poudre  d^al- margen  'gepulverte  iioralle',  die  früher in  der  Medizin  benutzt  wurde.  —  Als Fraueiiname  ist  Morgiane  in  der  Ge- schichte von  'ALI  BABÄ  und  den  vierzig Räubern  in  1001  Nacht  zuerst  durch GALLAND  bekannt  geworden.  Er  steckt auch  in  it.  fata  morgana  'Fee  Morgana', dann  'Luftspiegelung  in  der  Wüste', schon  in  Eschenbachs  Parzival  56,  18 mhd.  Fämurgän,  Feimurgan.  —  Man hat  auch  versucht,  auf  das  ar.  Grund- wort margän  das  dtsch.  Meerschaum zurückzuführen,  zuerst  A.  Vambery  in Magyar  Nyelvör  1899,  S.  537 ;  vgl. ZfdWf  I,  361.  II,  345/346.  VII,  79^/796. Da  aber  der  tatsächlich  auf  tk.  Boden bei  Eskisehir  in  Kleinasien  gewonnene Meerschaum  tk.  liile  tisy  oder  dehiz köjmjil  'Pfeifenstein'  oder  'Meeres-, schäum',  niemals  aber  margan  heißt, muß  Meerschaum  [engl,  meerschaum, ndl.  meerschuim,  frz.  Racine  de  mer] deutsch  erklärt  werden,  was  um  so leichler  möglich  ist,  als  auch  die  vier Sorten  in  Eskisehir  an  Ort  und  Stelle mit  dtsch  Namen  „Lager,  Kasten,  Groß- baumwolle, Kleinbaumwoile"  bezeichnet werden;  vgl.  Hugo  Grothe,  Auf  tk.  Erde. Reisebilder  und  Studien.  ^  Berlin  1903. S.  380,  wo  sich  auch  eine  Schilderung der  Gewinnung  des  Meerschaums  findet: S.  277/281.  Ferner  vgl.  Joseph  Grunze), Die  wirtschaftlichen  Verhältnisse  Klein- asiens. Wien  1897.  S.  34/44;  Dernburg, Auf  dtsch.  Bahn  in  Kleinasien.  Berlin 1892.  S.  51  ff.  „Die  Sladt  des  Meer- schaums*. —  Der  Kuriosität  halber  sei noch  die  Etymologie :  dtsch.  Meerschaum <  ar.  morsüm  [soll  heißen  marsüm] 'gesiegelt'  erwähnt,  s.  J.  G.  Kochs, Vergleichungen  mineralogischer  Benen- nungen des  Deutschen  mit  arabischen Wörtern.  Leipzig  1795.  S.40.  [Kluge  304. Devic  DEt  2.Ö/26.    Lammens  Rem  18.
3427:'Gebetsausrufer',  der  von  der  Galerie  des Minaretts  [s.  hier  Nr.  1463a]  aus  den  Ge- betsruf adän  hören  läßt,  tk.  muezzin; hieraus  rum.  muezin,  frz.  muSzzin,  sp. almuecin,  almuedano;  engl,  mueddin, muezzin,  dtsch.  Muezzin.  [DE  150. Eguilaz  240/241.    MWiD  ö2.
4204:(c)  Auf  das  ar.  Grundwort  sarki  geht auch  sicherlich  der  aus  byzantinischen Quellen  bekannte  Name  eines  zwischen Ägypten  und  Syrien  zeltenden  Beduinen- stammes lapaKfivoi  zurück;  hieraus  zur Bezeichnung  aller  islamischen  Völker des  Orients  lat.  Saraceni,  Adj.  saracenus 'sarazenisch',  it.  saracino  'Stechpuppe oder  hölzerner  Mann,  nach  dem  die Reiter  mit  der  Lanze  stießen',  saracenüo 'sarazenisch',  saracwiffre 'seil  warz  werden (Weintraube)',  hz.  sarrasin  'Buchweizen' [nach  de  Candolle  im  XV.  Jahrhundert aus  der  Tartarei  und  Rufsland  nach Mittel-  und  Westeuropa  eingeführt:  Poly- gonum  fagopyrum],  sarassine  'Gatter', Sarrazin  im  Argot  der  Pariser  Setzer 'Streikbrecher',  sp.  sarraccino  'Buch- weizen', überall  in  der  Bedeutung  'Sa-
4542:2017.  Gnzerati  tänkh: 'Wasserbehälter';  hieraus  engl,  tank, ritsch.  Tank  'großer  Behälter',  z.  B.  für Wasser  oder  Benzin.  —  [Die  Ähnlich- keit mit  pg.  tanque,  it.  sta(/no,  frz.  itang, sp.  estanque,  mengl.  stank  aus  lal.  stag- num  'Teich'  ist  zufällig.  Das  Wort engl,  tank,  dtsch.  Tank  'Kampfwagen', das  im  Weltkriege  entstanden  ist,  ist nach  seinem  Erfinder  entstanden.]  [Hob- son-Jobson 898/900.
```


## [2026-09-04T18:13:42.779Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D0%BE%D0%B1%D0%B5%D0%B7%D1%8C%D1%8F%D0%BD%D0%B0",
 "prompt": "Give the full etymology section for Russian обезьяна (obez'yana, \"monkey\"), including any theories tracing it to Persian, Arabic, or Turkic."
}
```


### [2026-09-04T18:13:47.785Z] TOOL RESULT

```
# Etymology of Russian обезьяна

Based on the Wiktionary entry, here is the etymological information provided:

The Russian word **обезья́на** (obezʹjána) is "Inherited from Old East Slavic _обезьꙗ́на_ (obezĭjána), _обозьꙗ́на_ (obozĭjána), further borrowed from Persian _ابوزینه_ (abuzina), _بوزینه_ (buzina, 'simian')."

The entry notes cognates in Old Ruthenian (_обезъꙗ́на_), but does not present alternative theories tracing the word to Arabic or Turkic origins. The documented path shows transmission from Persian through Old East Slavic into modern Russian, with the Persian root referring to simian creatures being the earliest identified source in this etymological chain.
```


## [2026-09-04T18:15:03.055Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT gibbon/borage ===\"\ngrep -n -i \"^gibbon\\|^borage\" SKT.txt\necho \"=== FSD gibbon/borage ===\"\ngrep -n -i \"^gibbon\\|^borage\" FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt 2>/dev/null\necho \"=== WEB gibbon/borage ===\"\ngrep -n -i \"^gibbon\\|^borage\" WEB_vol1.txt 2>/dev/null\necho \"=== DEV (Devic) bourrache/gibbon ===\"\ngrep -n -i \"bourrache\\|gibbon\" DEV.txt 2>/dev/null\necho \"=== PHN bourrache/gibbon ===\"\ngrep -n -i \"bourrache\\|gibbon\" PHN.txt 2>/dev/null\n"
}
```


### [2026-09-04T18:15:03.206Z] TOOL RESULT

```
=== SKT gibbon/borage ===
=== FSD gibbon/borage ===
FSD_vol3.txt:83395:borage and mint fuiuiiies (2) A diminutive nut. 2> bloslHln which one of two organisms draws nourishment flioiB
FSD_vol2.txt:8403:Gibbons  vs.  Oadenia  vol.  vi.  p.  J3.  [l.  b.  is  co.  1S58.1 Ilf.  t.  To  seize  or  acquire  wrongfully.  [<  OF.  e
FSD_vol2.txt:31759:gibbon  {ffylobateslar')  of  Ten-  White-handed  Gibbon.  .i  /u asaerlm,  the  dun-cotored  gibbon  (B.  entelloUes)  of  the Malay  archipelago,  and  the  slamang  are  examples.
FSD_vol2.txt:67537:Gibbon  Rome  vol.  iii,  p.  11.  (p.  s.  *   co,  1852.1
FSD_vol4.txt:62668:borage,  bur'll,  C   Af  TF,  5.  6,  7,  8,  13,  15,  brochantite,  bro-Shant'clt,  C   TF*.  1,  3,  7,  tur-i  E   —kal-sln'a-to-n,f,3,12,18,—  kal- 16, 18.  20.21,  22.23.  24,  25.— bor'd]  E.  3.  8   12,  15,  20.  22.  24*.  25  — bro'kan-talt,  E   .   a-na-to-n,  Af*.  11, 16
FSD_vol1.txt:10061:Gibbon  Rome  vol.  i,  ch.  2,  p.  103.  W.  a   c.  1880.]
FSD_vol1.txt:12215:Gibbon  Home  vol.  i,  p.  245.  [j.  a.  a.  18S0.] (2)  Connection  of  families  by  marriage.
FSD_vol1.txt:17182:Gibbon  Rome  vol.  l,  p.  258.  Ip.  h.  a   Co.  1852.]
FSD_vol1.txt:30269:Gibbon  
FSD_vol1.txt:34418:Gibbon  Hone  vol.  ii,  p.  226.  classical  form.
FSD_vol1.txt:69649:Gibbon  Rome  vol.  iii.  ch.  33,  p.  G3S.  Ip.  b.  *   co.  1852.1 {   <   LL.  coaliiio(n-),  <   L.  coalitus :   feee  coalite.  a.J Std:  see  alliance.—  Prep.:  a   coalition  of  former  op- ponents tcith  one  another,  against  a   common  enemy:  a   co- alition between  the  church  and  the  world.—  co"a-]rtlon-al, a.—  co^a-lFtlon-cr,  n„  -1st,  n.  An  advocate  of  coalition; a   member  or  a   coalition.—  co'a-llzed,  a.  (Rare.]  Brought Into  or  united  In  a   coalition,  co'a-llsedj.
=== WEB gibbon/borage ===
=== DEV (Devic) bourrache/gibbon ===
=== PHN bourrache/gibbon ===
10312:Bourrache, s. f. compose, (a.) 74
```


## [2026-09-04T18:15:05.065Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM buzin/zina ===\"\ngrep -n -i \"بوزینه\\|زنا\" AFM.txt 2>/dev/null | head -10\necho \"=== FVQ zina/whoredom ===\"\ngrep -n -i \"zin[aā]\" FVQ.txt FVQ_pages.txt 2>/dev/null | head -10\necho \"=== HUB abu/kunya ===\"\ngrep -n -i \"\\babu\\b\\|\\bebu\\b\" HUB.txt 2>/dev/null | head -10\n"
}
```


### [2026-09-04T18:15:05.153Z] TOOL RESULT

```
=== AFM buzin/zina ===
3100:(الروزنامة » 6 من روز اي يوم ومن نامه اي كتاب 
3349:وورد ايضاً ܪ † الزنادقة 010 الرنذ” 50 :في كتات الأ بستا ܩܘ حيث قبل :2 اننا 
7455:زنانه ܙ ^ 
=== FVQ zina/whoredom ===
=== HUB abu/kunya ===
153:persischen Dichter (Abu Suktir!) veraltet und wurde
1033:232. Np. bang bei Abu Muwaffaq p. 54. Zu np. mang
3006:'Hilfe' belegt Horn aus Abu Muwaffaq, sie findet
```


## [2026-09-04T18:15:09.807Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10305,10320p' PHN.txt"
}
```


### [2026-09-04T18:15:09.851Z] TOOL RESULT

```
Bordât, s. m. (a.) 71
Bostandji, s. m. compose, (p.-t.) 71
Boudjou, 8. m. (t.) — BiyAlb(nidjoû; valeur de cette monnaie. ... 79
Bougie, n. pr. (a.) 78
Bouquet , 8. m. ( a.) 73
Bouracan, s. m. (a.)« 7/1
Boumou8, 8. m. (a.) 74
Bourrache, s. f. compose, (a.) 74
Boutargue, s. f. compose, (a.) 75
Bouteille , s. f. (a.-p. ) 76
Bouzah, s. m. (t.) 75
Brevet, s. m. (a.) 76
Briquet, s. m. (a.) 76
Broc, s. m. (a.) 76
Buccine, s. f. (a.) 77
Buse, s. f. (a.) — Busard, Buson, s. m 77
```


## [2026-09-04T18:15:14.538Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^Bourrache\" PHN.txt"
}
```


### [2026-09-04T18:15:14.588Z] TOOL RESULT

```
10312:Bourrache, s. f. compose, (a.) 74
```


## [2026-09-04T18:18:22.232Z] TOOL CALL #56: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet/page-33.json",
 "content": "{\n  \"pdf_page\": 33,\n  \"book_page\": 3,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ab 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Proto-Semitic *ʔab(w)- 'father' (< Proto-Afroasiatic *ʔab-, an onomatopoeic nursery/baby-talk word)\",\n      \"note\": \"Real, well-attested Semitic noun: Akkadian abum, Hebrew ʼāḇ, Aramaic ʼabbā (emphatic), Ugaritic ʼb, Arabic ʼab, Geʽez/Ethiopic ʼab all 'father'. Klein (s.v. 'Aboth') treats it as of uncertain ultimate origin, 'possibly traceable to *ab(a), a child's word for father' - i.e. not a deep reconstructible root in the Pokorny sense but a nursery word independently stabilized across the family, which is also the modern Wiktionary Proto-Semitic reconstruction. Nourai's own citation FVQ:44 (Jeffery, Foreign Vocabulary of the Qur'an) does NOT actually discuss 'ab'=father on that page - Jeffery's book only catalogs non-Arabic LOANWORDS in the Qur'an, and 'ab' is native Semitic vocabulary, not a loanword, so it has no entry there; printed p.44 of FVQ is entirely about 'ababīl' and the start of the 'Ibrāhīm' entry (relevant instead to nodes 13-15 below). KLN:6 does support the root.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/%CA%BEab-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"FVQ:44\", \"status\": \"not_found\", \"note\": \"FVQ_pages.txt leaf 62 (printed p.44): whole page is the end of the 'ababīl' entry and the start of 'Ibrāhīm' ('Occurs some 69 times... Abraham'); no entry for 'ab' (father) is present. Jeffery's dictionary covers only foreign loanwords, and 'ab' is native Semitic, so this is not a discussion of the root itself - likely a mis-pointed/forward citation toward the Ibrahim material (nodes 13-15).\"},\n        {\"ref\": \"KLN:6\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 15 (printed pp.6-7, confirmed by the running heads 'above'/'abstinent' immediately preceding the page-number markers '6' and '7' in the OCR): s.v. 'Aboth, also Abot ... Heb. Abhōth, pl. of abh, \\\"father\\\", rel. to Aram. abh (absolute state), abbā (emphatic state), Ugar. ’b, Arab. ab, Ethiop. ab, \\\"father\\\"; of uncertain origin, possibly traceable to *ab(a), a child's word for father.'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 15, s.v. Aboth\", \"stance\": \"supports\", \"note\": \"gives the full comparative Semitic set (Aram., Ugar., Arab., Ethiop.) and the nursery-word hypothesis; also cross-references 'Cp. also borage' at the end of this very entry, anticipating the abu-'araq branch below.\"},\n        {\"src\": \"Wiktionary (web)\", \"where\": \"Reconstruction:Proto-Semitic/ʔab-\", \"stance\": \"supports\", \"note\": \"'*ʔabw- (m.) father... from Proto-Afroasiatic *ʔab- (\\\"father\\\"), ultimately an onomatopoeic nursery word' with descendants Akkadian abum, Arabic ʔab, Aramaic ʔabā', Hebrew av, Ugaritic ʔabu, Ge'ez ʔäb, etc.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"ab, abŭ, a.b.v : father\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Classical Arabic ʼab 'father' (triptote, declined obliquely as ʼabū-/ʼabī-/ʼabā- - Nourai's 'a.b.v' is evidently a rendering of this weak wāw-final root ʾ-b-w seen in the oblique/construct stems) is the direct Arabic reflex of Proto-Semitic *ʔab(w)-, exactly parallel to Hebrew ʼāḇ and Aramaic ʼabbā. The construct-state form abū is the base for the many Arabic 'father of X' kunya-compounds discussed at node 3.\",\n          \"ref_check\": [\n            {\"ref\": \"FVQ:44\", \"status\": \"not_found\", \"note\": \"same page as the root check: covers 'ababīl'/'Ibrāhīm', not the base word 'ab'.\"},\n            {\"ref\": \"FVA:25\", \"status\": \"not_checked\", \"note\": \"S.M. Nahvi's Farhang-e Vazheha-ye Arabi dar Farsi has no known digital copy (refs_online.json: 'RE-SEARCH 2026-09: still no digital copy on any permitted platform').\"},\n            {\"ref\": \"LKT:44\", \"status\": \"not_found\", \"note\": \"Lokotsch's dictionary is an etymological glossary of ORIENTAL LOANWORDS IN EUROPEAN LANGUAGES; it has no headword for plain Arabic 'ab'/'abū' by itself (only compounds like abū kirdān, abū 'araq, abū tīlūn, entries 11/13/14, which sit near the front of the book, not at a page '44'). Could not locate the cited page in the scan; refs_online.json notes Lokotsch is 'usually cited by entry number, but Nourai cites pages', so the numbering may not be recoverable from this print run.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 15, s.v. Aboth\", \"stance\": \"supports\", \"note\": \"'Aram. abh (absolute state), abbā (emphatic state)... Arab. ab... father'.\"},\n            {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt leaf 62-63 (pp.44-45)\", \"stance\": \"silent\", \"note\": \"no headword 'ab'; book only covers foreign loanwords.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"abŭ «آبو ( ابوی )» : father\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian borrowed the Arabic construct-state form abū wholesale as a bound element (rendered آبو /abu/) used only inside honorific kunya-style compound names and epithets taken directly from Arabic/Islamic usage: Abū ʿAlī Sīnā (Ibn Sina/Avicenna), Abu'l-Fażl, Abu'l-Qāsem (an epithet of the Prophet, also of Ferdowsi), Abu'l-Ḥasan, Abu'l-Fatḥ, and the colloquial pejorative بوالهوس /bu(l)havas/ 'frivolous, capricious person' (lit. 'father of caprice/lust', havas being Arabic). This is a simple, uncontroversial case of a whole naming-pattern (not a native root) being imported with Islamization, not an inherited Persian word for 'father' (the inherited Persian word is pedar, from OIr. *pitar-, a different IE root entirely).\",\n          \"ref_check\": [\n            {\"ref\": \"FVA:25\", \"status\": \"not_checked\", \"note\": \"no digital copy available.\"},\n            {\"ref\": \"MON\", \"status\": \"not_found\", \"note\": \"Mo'in's abridged 2-vol text (MON_part1/2.txt) has no dedicated headword for the productive Arabic loan-element بو/ابو itself (it is a bound formative appearing only inside proper names, which the abridged dictionary does not list); the citation gives no page number to pin down further.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt/MON_part2.txt, grep 'بوالحسن|ابوعلی|بوالهوس'\", \"stance\": \"silent\", \"note\": \"no separate entries found in the abridged 2-vol edition; proper-name compounds of this kind are normally treated in onomastic works, not general dictionaries.\"},\n            {\"src\": \"HRN\", \"where\": \"grep 'abu' in HRN.txt\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss covers inherited/borrowed NP roots, not this Arabic naming pattern.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"abŭ-zînâ : \\\"father of whoredom\\\" (gibbon); abŭ-araq : \\\"father of sweat\\\" (medicinal plant)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both are genuine Arabic kunya-style compounds built on the construct form abū + genitive noun, a very productive naming pattern in Arabic (cf. abū kirdān 'father of ticks' = cattle egret, abū tīlūn = a mallow genus - Lokotsch entries 11 and 14). (1) abū 'araq, lit. 'father of sweat' (ʿaraq 'sweat, exudate'), was the name Arab physicians gave to the borage plant because of its diaphoretic/sudorific use in medieval Arabic medicine; this is exactly Klein's and the AHD's etymology for English 'borage' (see node 8-10). (2) abū zinā, lit. 'father of fornication/whoredom' (zinā 'illicit sex'), is attested by Lokotsch (entry 556) as the Arabic source of Turkish (e)büzine/büzine 'ape', a derogatory nickname reflecting old folklore about apes' promiscuity.\",\n          \"ref_check\": [\n            {\"ref\": \"FVQ:44\", \"status\": \"not_found\", \"note\": \"same p.44 issue as above; page covers 'ababīl'/'Ibrāhīm', not these compounds.\"},\n            {\"ref\": \"FVA:25\", \"status\": \"not_checked\", \"note\": \"no digital copy.\"},\n            {\"ref\": \"LKT:44\", \"status\": \"partial\", \"note\": \"LKT.txt line ~247: entry 13, 'Ar. abū raǧʿ [=abū 'araq]: \\\"Vater des Schweißes\\\" [father of sweat], hieraus lat. borrago...' confirms the abū-'araq/borage claim word-for-word, and line 1413: entry '(5)56. Tk. ebüzine: Auch buzine \\\"Affe\\\" [aus ar. abū zinā \\\"Vater der Unzucht\\\"]; hieraus russ. obez'jana...' confirms abū zinā as an Arabic source for an ape-word - but only as far as TURKISH/RUSSIAN, not Persian/Hindustani/French/English gibbon as the chart's downstream nodes claim (see node 4-7); also could not confirm either entry sits on a scanned page literally numbered '44'.\"},\n            {\"ref\": \"AHD:152\", \"status\": \"supports\", \"note\": \"AHD online (ahdictionary.com, search 'borage'): '[Middle English, from Old French bourage, from Medieval Latin borāgō, probably from Arabic bū'araq, from 'abū 'araq, source of sweat... : 'ab, father, source; see ʾb + 'araq, sweat; see ʿrq2.]' - matches the abū-'araq half exactly; AHD has no comparable entry discussing abū-zinā/gibbon.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt, s.v. 'borage' and 'arrack'\", \"stance\": \"supports\", \"note\": \"'borage... ult. fr. Arab. abu 'arak, lit. \\\"father of sweat\\\", so called by the Arab physicians because of its sudorific effect'; 'arrack... fr. Arab. 'araq, \\\"sweat, juice of fruit\\\"'.\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt entries 13 and 556\", \"stance\": \"partial\", \"note\": \"see ref_check above - confirms both Arabic compounds exist with these glosses, but the zinā entry's onward chain is Turkish/Russian in Lokotsch, not Persian/Hindustani/French as Nourai draws it.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"bŭzîneh «بوزینه ( بوزنه )» : gibbon\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Nourai derives NP بوزینه buzīne 'monkey, ape' from the Arabic kunya abū zinā 'father of whoredom' as a euphemistic/derogatory nickname reanalyzed as a plain noun in Persian. This IS the etymology found in the older Semitic-loanword literature (Lokotsch 1927, entry 556, though he routes it through Turkish rather than Persian). However, current Iranian comparative linguistics (Wiktionary, following modern Iranological scholarship) instead treats بوزینه as an INHERITED native Iranian word from Proto-Iranian, cognate with Pashto بيزو (bízo) 'monkey' - i.e. not an Arabic loan at all. Hübschmann's Persische Studien (addenda, p.87 no.842-845) independently notes that NP buzina/buzinagān already occurs 'in the old Qur'an commentary' (i.e. early New Persian, 10th c.), which favors it being old, native vocabulary rather than a late reanalysis of an Arabic kunya-insult, though Hübschmann does not give a source etymology either way. On the modern view, the causality is more likely the reverse or coincidental: the genuinely native Iranian animal-name buzīne (whose form happens to resemble abū-zinā) was later folk-etymologized by some Arabic/Persian philologists into the 'father of whoredom' kunya, rather than the word actually originating from that phrase. Persian buzīne (not the Arabic phrase) is itself the accepted donor of Old Turkic böčin and Old East Slavic обезьꙗна > Russian обезьяна.\",\n          \"ref_check\": [\n            {\"ref\": \"MON:602\", \"status\": \"not_found\", \"note\": \"MON_part1.txt line ~26095 s.v. بوزینه (buzine, variants buzina/buzaneh/buzanineh) gives only the meaning '(zool.) monkey/ape' with no etymological note (this is the abridged Adena 2-vol edition, which generally omits etymologies for common nouns); could not verify against the page number MON:602 of the full 6-vol edition, which is not digitized.\"},\n            {\"ref\": \"FVA:180\", \"status\": \"not_checked\", \"note\": \"no digital copy of Nahvi's dictionary.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt l.26095-26096\", \"stance\": \"silent\", \"note\": \"'بوزینه: [- بوزینا - بوزنه - بوزنینه] (اِ.) (جانور.) میمون' - meaning only, no etymology given.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt l.9718-9719 (addenda to p.87, no.842-845)\", \"stance\": \"partial\", \"note\": \"'Np. buzina (im pl. buzinagan) schon im alten Korancommentar, JRAS. 1894, 449' [NP buzina, pl. buzinagan, already occurs in the old Qur'an commentary] - shows the word is old in NP but gives no etymon.\"},\n            {\"src\": \"Wiktionary (web)\", \"where\": \"en.wiktionary.org/wiki/بوزینه\", \"stance\": \"contradicts\", \"note\": \"'Inherited from Proto-Iranian... Compare Pashto بيزو (bízo, \\\"monkey\\\")... borrowed into Old East Slavic обезьꙗна... Old Turkic بٮچن (béčin, \\\"monkey\\\")' - treats it as native Iranian, not an Arabic loan.\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt line 1413, entry 556\", \"stance\": \"partial\", \"note\": \"derives 'buzine' from Arabic abū zinā but as a TURKISH word (Tk. ebüzine/buzine), with Russian obez'jana as its offspring - not a Persian word in Lokotsch's own account.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Hindustani\",\n          \"words\": \"bojîna\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"Chart claims a Hindustani intermediate form 'bojina' between Persian buzīne and French/English gibbon. Partridge's Origins (PRT:253) could not be checked (no accessible digital copy - all archive.org scans are lending-only). No Hindustani/Anglo-Indian source available locally (Hobson-Jobson, Whitworth) contains any entry for 'bojina', 'buzina', or 'gibbon'. Given that the modern consensus on 'gibbon' derives it from a Southeast Asian (Malayan Aslian) source unconnected to India (see node 6-7), this Hindustani way-station is very likely part of the same unsupported chain.\",\n          \"ref_check\": [\n            {\"ref\": \"PRT:253\", \"status\": \"not_checked\", \"note\": \"E. Partridge, Origins (1958): all copies on archive.org are lending-only (originsshortetym00part etc.); could not access p.253 to check.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"grep 'gibbon|bojin|monkey' in HJB.txt\", \"stance\": \"silent\", \"note\": \"Hobson-Jobson has no entry for 'gibbon' or any word resembling 'bojina'; it does derive Anglo-Indian 'baboon' from Persian maimūn, a different animal name entirely.\"},\n            {\"src\": \"AID\", \"where\": \"grep 'gibbon|bojin' in AID.txt\", \"stance\": \"silent\", \"note\": \"Whitworth's Anglo-Indian Dictionary has no matching entry.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"(no word given)\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The chart's NOTE ('This monkey was taken to France from India in the 18th century') matches the traditional story that French naturalist Georges-Louis Leclerc, Comte de Buffon, coined/popularized 'gibbon' in his Histoire Naturelle after a word supposedly used in French India, brought to Europe via Marquis Joseph-François Dupleix (governor-general of French India, 1742-54) - this part is genuine and is exactly what Klein's own cited entry (KLN:655) says. But modern scholarship (Etymonline, AHD, Wiktionary) is explicit that the supposed Indian source word was never actually found in any Indian language, and current etymology instead traces 'gibbon' to a Northern Aslian language of the Malay Peninsula (cf. Batek kəboɲ) - i.e. Southeast Asian, not South Asian/Indian, and completely unrelated to Persian buzīne or Arabic abū-zinā.\",\n          \"ref_check\": [\n            {\"ref\": \"KLN:655\", \"status\": \"partial\", \"note\": \"KLN_1966.txt: 'gibbon, n., a small, long-armed ape. - F., a name of Indian origin brought to Europe by the Marquis Joseph-François Dupleix (1697-1763), governor-general of the French possessions in India (1742-54).' Confirms the Dupleix/India story in the chart's NOTE but gives no specific etymon at all - certainly not 'buzīne'/'bojina'/'abu-zina' - so it does not actually corroborate the derivation chain drawn in nodes 3-5.\"}\n          ],\n          \"sources\": [\n            \"https://www.etymonline.com/word/gibbon\",\n            \"https://en.wiktionary.org/wiki/gibbon\",\n            \"https://www.ahdictionary.com/word/search.html?q=gibbon\"\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. gibbon\", \"stance\": \"partial\", \"note\": \"see ref_check above.\"},\n            {\"src\": \"SKT\", \"where\": \"grep 'gibbon' SKT.txt\", \"stance\": \"silent\", \"note\": \"Skeat's Concise Etymological Dictionary has no entry for 'gibbon'.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"gibbon\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"English 'gibbon' (1770s) is simply borrowed from French gibbon, the scientific name applied by Buffon. As at node 6, modern etymology (Etymonline: 'supposedly from a word in the French colonies of India but not found in any language there'; Wiktionary: from a Northern Aslian language, cf. Batek kəboɲ; AHD: 'said to be a local name in a language of Southeast Asia') rejects any link to Persian buzīne/Hindustani bojina/Arabic abū-zinā - the whole chain in nodes 3-6 leading to 'gibbon' is not supported by any current reference and looks like Nourai grafting a genuine but separate Arabic/Turkish/Russian word-history (abū zinā > Turkish büzine > Russian obezyana, per Lokotsch) onto the unrelated word 'gibbon'.\",\n          \"ref_check\": [\n            {\"ref\": \"KLN:655\", \"status\": \"partial\", \"note\": \"same entry as node 6: confirms only 'name of Indian origin', no etymon matching buzīne/bojina.\"}\n          ],\n          \"sources\": [\n            \"https://www.etymonline.com/word/gibbon\",\n            \"https://en.wiktionary.org/wiki/gibbon\",\n            \"https://www.ahdictionary.com/word/search.html?q=gibbon\"\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. gibbon\", \"stance\": \"partial\", \"note\": \"see above.\"},\n            {\"src\": \"WEB\", \"where\": \"grep 'gibbon' WEB_vol1.txt\", \"stance\": \"silent\", \"note\": \"no hit in the available Webster's volume.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Middle Latin\",\n          \"words\": \"borrâco\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Medieval Latin borrāgō (the plant borage) is traditionally derived - already in medieval Arabic-influenced European medicine - from Arabic abū 'araq 'father of sweat', reflecting the plant's use as a diaphoretic by Arab physicians (attested via the school of Salerno and Constantinus Africanus's translations of Arabic medical texts, 11th c.). This is the etymology given by Klein, Lokotsch (entry 13), and the American Heritage Dictionary. However, the OED and modern Etymonline flag a competing, purely Latin derivation from borra 'rough hair, short wool' (referring to the plant's bristly leaves), and treat the matter as genuinely unsettled rather than settled in Arabic's favor - hence 'plausible' rather than 'confirmed'.\",\n          \"ref_check\": [\n            {\"ref\": \"AHD:152\", \"status\": \"supports\", \"note\": \"AHD online s.v. borage: 'from Medieval Latin borāgō, probably from Arabic bū'araq, from 'abū 'araq, source of sweat...'\"}\n          ],\n          \"sources\": [\n            \"https://www.etymonline.com/word/borage\",\n            \"https://en.wiktionary.org/wiki/borage\",\n            \"https://www.ahdictionary.com/word/search.html?q=borage\"\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. borage\", \"stance\": \"supports\", \"note\": \"'fr. ML. borrago, ult. fr. Arab. abu 'arak, lit. \\\"father of sweat\\\"'.\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt entry 13\", \"stance\": \"supports\", \"note\": \"'hieraus lat. borrago... Trotz ML 1412 scheint diese Ableitung noch immer die beste... zu sein' [despite Meyer-Lübke's competing entry, this (Arabic) derivation still seems the best].\"},\n            {\"src\": \"Wiktionary/Etymonline (web)\", \"where\": \"en.wiktionary.org/wiki/borage; etymonline.com/word/borage\", \"stance\": \"partial\", \"note\": \"Wiktionary gives both the Arabic and the Latin borra theories without preference; Etymonline states the OED favors Latin borra 'rough hair' over the Arabic folk story.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Old French\",\n          \"words\": \"borrace, bourrache\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Old French borrace (> Modern French bourrache) is a straightforward phonetic adaptation of Medieval Latin borrāgō/borrāgin- (stem borragin-), with loss of the Latin ending and normal Old French sound development of the medial consonants; attested from the 13th century in herbals alongside Italian borrag(g)ine/borrana, Spanish borraja, Provençal borrage. The ultimate Arabic-vs-Latin dispute at node 8 carries through unchanged to this link, which is otherwise a routine and uncontroversial Vulgar/Medieval-Latin-to-Old-French transmission.\",\n          \"ref_check\": [\n            {\"ref\": \"AHD:152\", \"status\": \"supports\", \"note\": \"AHD's etymology chain runs Old French bourage/borrage < Medieval Latin borrāgō, consistent with this node.\"}\n          ],\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/borage\"\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. borage\", \"stance\": \"supports\", \"note\": \"'ME., fr. OF. borrace (cp. its variant burage and F. bourrache), fr. ML. borrago.'\"},\n            {\"src\": \"PHN\", \"where\": \"PHN.txt line 10312\", \"stance\": \"supports\", \"note\": \"Pihan's index of French words of Arabic/Persian/Turkish origin lists: 'Bourrache, s. f. compose. (a.) 74' - classifying bourrache as an Arabic-derived ('a.') compound, consistent with the abu-'araq etymology.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"borage : a spicy salad seasoning\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Middle English borage (c.1300) is a direct borrowing of Old French borrace/bourrache; the plant (Borago officinalis) has cucumber-flavored leaves traditionally used fresh in salads and drinks, matching the chart's gloss. As with nodes 8-9, the word's deeper origin is 'plausible' rather than 'confirmed': Klein, Lokotsch and AHD back the Arabic abū-'araq derivation, while Etymonline/OED prefer or at least seriously entertain the Latin borra 'rough hair' alternative, so the matter remains genuinely disputed among modern authorities even though Nourai presents it as settled.\",\n          \"ref_check\": [\n            {\"ref\": \"AHD:152\", \"status\": \"supports\", \"note\": \"AHD online s.v. borage, full etymology quoted at node 8.\"}\n          ],\n          \"sources\": [\n            \"https://www.etymonline.com/word/borage\",\n            \"https://en.wiktionary.org/wiki/borage\"\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. borage\", \"stance\": \"supports\", \"note\": \"'borage, n., a blue-flowered plant used in salads. - ME., fr. OF. borrace... See abbot and cp. arrack.'\"},\n            {\"src\": \"SKT\", \"where\": \"grep 'borage' SKT.txt\", \"stance\": \"silent\", \"note\": \"no entry found in the available Skeat text.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Hebrew\",\n          \"words\": \"abh : father\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Biblical Hebrew ʼāḇ 'father' (construct ʼăḇī-/ʼăḇōṯ pl.) is the direct Hebrew continuation of Proto-Semitic *ʔab(w)-, identical in sense and cognate set to the Arabic and Aramaic forms at node 0-1.\",\n          \"ref_check\": [\n            {\"ref\": \"KLN:6\", \"status\": \"supports\", \"note\": \"same 'Aboth' entry quoted at the root: 'Heb. Abhōth, pl. of abh, \\\"father\\\"...'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 15, s.v. Aboth\", \"stance\": \"supports\", \"note\": \"see quote above.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"Abot\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English 'Abot' (also spelled Aboth) names the Mishnah tractate Pirkei Avot ('Ethics/Chapters of the Fathers') and the first benediction of the Shemoneh Esreh; it is simply the Hebrew plural ʼāḇōṯ 'fathers' of ʼāḇ used as a loanword/title in English Judaic studies, taken over unchanged.\",\n          \"ref_check\": [\n            {\"ref\": \"KLN:6\", \"status\": \"supports\", \"note\": \"KLN_1966.txt: 'Aboth, also Abot, n., 1) the Mishnah treatise also called Pirke Aboth or \\\"The Ethics of the Fathers\\\"; 2) name of the first benediction of the Shemoneh Esreh (Jewish liturgy). - Heb. Abhōth, pl. of abh, \\\"father\\\"...'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 15, s.v. Aboth\", \"stance\": \"supports\", \"note\": \"quoted above; exact match for the chart's gloss and language label.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Hebrew\",\n          \"words\": \"Abh-raham; Abh-ram; Abh-ner; Ab-šalom; Abh-igayil; Yo-abh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All six are real Hebrew names built on ʼāḇ 'father' as first or second compound element, matching the chart's glosses almost verbatim against Klein: Abhrāhām 'father of the multitude' (ʼāḇ + *rāhām, cf. Arabic ruhām 'multitude', Gen. 17:5); Abhrām 'high/exalted father' (ʼāḇ + rām, from rūm 'to be high'); Abhnēr 'my father is light' (ʼāḇ + nēr 'light'); Abhshālōm/Abšālōm 'father is peace' (ʼāḇ + shālōm 'peace'); Abhigayil 'my father is rejoicing' (ʼāḇ + gîl 'to rejoice'); Yô'āḇh 'the LORD is (his) father' (Yô- theophoric element + ʼāḇ). Every element and gloss in the chart is confirmed by Klein's individual entries.\",\n          \"ref_check\": [\n            {\"ref\": \"FVQ:44\", \"status\": \"partial\", \"note\": \"FVQ_pages.txt leaf 63 (p.45): Jeffery's Ibrāhīm entry states the Qur'anic name 'is always used of the Biblical Patriarch and thus is ultimately derived from Heb. [Abraham]', discussing Syriac/Ethiopic/Armenian intermediaries - relevant background for the Hebrew-to-Arabic route (node 14) but not a treatment of the six Hebrew compound names themselves.\"},\n            {\"ref\": \"KLN:6\", \"status\": \"supports\", \"note\": \"KLN_1966.txt (leaves 15-16, printed pp.6-9 area): 'Abraham... Heb. Abhrahām, lit. \\\"father of the multitude\\\", ... abh, \\\"father\\\", and *rahām, \\\"multitude\\\"... rel. to Arab. ruhām'; 'Abram... Heb. Abhrām, compounded of abh, \\\"father\\\", and ram, \\\"high, exalted\\\"'; 'Absalom... Heb. Abhshalōm, lit. \\\"father is peace\\\"'; 'Abigail... Heb. Abhigayil, lit. \\\"my father is rejoicing\\\"'; and elsewhere 'Abner... Heb. Abhnir, lit. \\\"my father is light\\\"'; 'Joab... fr. Heb. Yô'ābh, lit. \\\"the Lord is (his) father\\\"'. All six match the chart exactly.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt, six separate entries (Abraham, Abram, Abner, Absalom, Abigail, Joab)\", \"stance\": \"supports\", \"note\": \"each entry's Hebrew form and literal gloss matches the chart word-for-word (see ref_check note).\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Arabic\",\n          \"words\": \"Abrahim : Abraham\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Qur'anic/Classical Arabic Ibrāhīm is not a native Arabic formation but a borrowing of the Biblical patriarch's name, most likely mediated through Syriac (Nourai's 'Abrahim' matches this well). Jeffery traces the Qur'anic form's likely immediate source to the common Syriac form (cf. Ethiopic and Armenian forms borrowed the same way), ultimately from Hebrew ʼAḇrāhām, with the vowel pattern altered from the expected Arabic *Abrāhām under this foreign-mediated transmission - one of the clearest cases in the Qur'an of a Biblical proper name entering Arabic via the Aramaic/Syriac-speaking Christian and Jewish communities of Late Antique Arabia, not directly from Hebrew.\",\n          \"ref_check\": [\n            {\"ref\": \"FVQ:44\", \"status\": \"supports\", \"note\": \"FVQ_pages.txt leaves 62-63 (pp.44-45), s.v. Ibrāhīm: 'It is always used of the Biblical Patriarch and thus is ultimately derived from Heb. [ʼAḇrāhām]... The common Syr. form is [Syriac form], which is obviously the source of both the Eth. [Ethiopic] and the Arm. [Armenian]... The form would thus seem to be due to Muhammad himself, but the immediate source is not easy to determine.' Confirms the Hebrew-ultimate/Syriac-mediated route the chart implies.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt leaves 62-63\", \"stance\": \"supports\", \"note\": \"see ref_check quote.\"},\n            {\"src\": \"Wiktionary (web)\", \"where\": \"en.wiktionary.org/wiki/ابراهیم\", \"stance\": \"partial\", \"note\": \"modern Wiktionary's simplified chain has Arabic borrowing directly 'from Aramaic ʾaḇrāhām, from Biblical Hebrew ʾaḇrāhām' without singling out Syriac specifically, but agrees on the Aramaic-mediated, ultimately-Hebrew origin.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Persian\",\n          \"words\": \"Ebrâhîm «ابراهیم»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian Ebrāhīm is a straightforward borrowing of Arabic Ibrāhīm (itself from Aramaic/Syriac ʼaḇrāhām < Biblical Hebrew ʼAḇrāhām), entering Persian with Islamization from the 7th century onward like other Qur'anic prophet-names (Mūsā, ʿĪsā, etc.); the /i/ > /e/ shift in the first syllable and general vocalism reflect ordinary New Persian adaptation of Arabic loanwords, not a separate line of descent.\",\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"chart lists no refs for this node.\"}\n          ],\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D8%B1%D8%A7%D9%87%DB%8C%D9%85\"\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary (web)\", \"where\": \"en.wiktionary.org/wiki/ابراهیم\", \"stance\": \"supports\", \"note\": \"'Borrowed from Arabic إِبْرَاهِيم (ʔibrāhīm). [Arabic] Aramaic أَبْرَاهَام (ʾaḇrāhām) ... Biblical Hebrew אַבְרָהָם (ʔaḇrɔhɔm).'\"},\n            {\"src\": \"MON\", \"where\": \"grep 'ابراهیم' in MON_part1/2.txt\", \"stance\": \"silent\", \"note\": \"no separate etymological entry found in the abridged Mo'in text (proper names of this kind are not generally treated as headwords there).\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"English\",\n          \"words\": \"Abraham, Abram, Abner, Absalom, Abigail, Jaob\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"Abraham, Abram, Abner, Absalom and Abigail are all genuine, unremarkable English reflexes of the Hebrew names at node 13, arriving via the Vulgate/Septuagint-mediated Biblical name tradition (Late Latin/Greek transliterations of the Hebrew), exactly as documented in Klein's individual entries. The sixth item, 'Jaob', is almost certainly a scanning/transcription error for 'Joab' (matching node 13's 'Yo-abh' precisely, and Klein has a separate entry headed exactly 'Joab', not 'Jaob'): 'Joab... Late L. Joab, fr. Gk. Iōab, fr. Heb. Yô'āḇh, lit. \\\"the Lord is (his) father\\\"'. The book almost certainly printed 'Joab', not 'Jaob'.\",\n          \"ref_check\": [\n            {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966.txt has individual entries for Abraham, Abram, Absalom, Abigail (all quoted at node 13) and for Joab (leaf ~ line 20305): 'Joab, 1) masc. PN.; 2)... - Late L. Joab, fr. Gk. Iōab, fr. Heb. Yô'āḇh, lit. \\\"the Lord is (his) father\\\".' No entry exists under the spelling 'Jaob'.\"},\n            {\"ref\": \"AHD\", \"status\": \"not_checked\", \"note\": \"no page number given; AHD's 1976 New College Edition body is not available online or locally beyond the IE-roots appendix (AHD_watkins1985.txt), which does not cover proper names.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt, entries Abraham/Abram/Absalom/Abigail/Joab\", \"stance\": \"supports\", \"note\": \"all five correctly-spelled names confirmed (see node 13 quotes); no headword 'Jaob' exists anywhere in the file, only 'Joab'.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-04T18:18:22.270Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet/page-33.json (file state is current in your context — no need to Read it back)
```


## [2026-09-04T18:18:26.820Z] AGENT

Now let me validate the JSON and run the coverage check.


## [2026-09-04T18:18:28.482Z] TOOL CALL #57: Bash

```json
{
 "command": "python3 -m json.tool /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet/page-33.json > /dev/null && echo \"VALID JSON\"\nVERIFY_DIR=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet python3 /home/sfmqrb/git/rishe/tools/verify_check.py 33"
}
```


### [2026-09-04T18:18:32.360Z] TOOL RESULT

```
VALID JSON
nodes verified: 16/16
node verdicts: {'confirmed': 8, 'disputed': 3, 'unverified': 1, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'not_found': 5, 'not_checked': 7, 'partial': 4, 'supports': 9}
books consulted: {'supports': 13, 'silent': 10, 'partial': 7, 'contradicts': 1} | by book: {'KLN': 11, 'MON': 3, 'LKT': 3, 'Wiktionary (web)': 3, 'FVQ': 2, 'SKT': 2, 'HRN': 1, 'HUB': 1, 'HJB': 1, 'AID': 1, 'WEB': 1, 'Wiktionary/Etymonline (web)': 1, 'PHN': 1}
```


## [2026-09-04T18:18:46.880Z] AGENT

All 16 nodes verified, no problems reported, valid JSON. The file is written to the model-comparison output path as instructed (not touching `data/verification/`).

## Summary — PDF page 33 (book page 3), entry 0 "Ab 2" (Semitic, "father")

**Root:** confirmed — Proto-Semitic *ʔab(w)- 'father', a nursery word per Klein/Wiktionary.

**Node verdicts:** 8 confirmed, 3 plausible, 3 disputed, 1 unverified, 1 transcription_suspect.

**Disputed:**
- **#4 Persian bŭzîneh "gibbon/monkey"** — Nourai derives it from Arabic *abū zinā* "father of whoredom." Modern Wiktionary instead treats بوزینه as **inherited native Proto-Iranian** vocabulary (cognate with Pashto بيزو), and itself the donor to Turkic/Russian обезьяна — the causal arrow is likely backwards from Nourai's chart.
- **#6/#7 French/English "gibbon"** — Nourai's own cited source (Klein, KLN:655) only says "name of Indian origin," not the Persian/Arabic chain claimed. Modern sources (Etymonline, AHD, Wiktionary) now derive "gibbon" from a **Northern Aslian (Malay Peninsula) language**, unrelated to Persian/Arabic/Hindustani entirely — the whole abū-zinā→buzīne→bojina→gibbon chain appears to be Nourai grafting a real but separate Arabic/Turkish/Russian word-history (found in Lokotsch, entry 556, which stops at Russian обезьяна) onto an unrelated English word.

**Unverified:** #5 Hindustani "bojîna" — Partridge (PRT:253) inaccessible; no Anglo-Indian source (Hobson-Jobson, Whitworth) attests it.

**Transcription_suspect:** #16 "Jaob" is almost certainly a scan error for "Joab" (Klein has a "Joab" entry, none for "Jaob"; matches node 13's Yo-abh).

**Plausible:** #3/#8/#9/#10 (borage chain, abū-'araq "father of sweat") — AHD, Klein, and Lokotsch all support the Arabic derivation, but Etymonline/OED flag a competing Latin *borra* "rough hair" theory as at least equally credible, so it's not settled.

Also flagged: Nourai's own citation FVQ:44 doesn't actually discuss "ab"=father at all — that page of Jeffery covers "ababīl" and the start of "Ibrāhīm" (which does support nodes 13-15 on Abraham/Ibrahim, just not the root/node-1 citation).

Output written to `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet/page-33.json`. Nine new web sources archived under `data/verification/sources/web/`.
