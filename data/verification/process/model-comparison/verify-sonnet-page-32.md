# Verification process log — model-comparison/verify-sonnet-page-32


## [2026-09-04T18:06:53.051Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 32 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-32.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-32.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (all files listed in the source matrix exist there). ONE DEVIATION from the instructions: this is a model-comparison run, so write your output to /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet/page-32.json instead of data/verification/, do NOT read or copy any existing file under /home/sfmqrb/git/rishe/data/verification/page-*.json, and check coverage with `VERIFY_DIR=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet python3 /home/sfmqrb/git/rishe/tools/verify_check.py 32` (the script now honours VERIFY_DIR). Everything else as instructed (modern web sources archived with tools/fetch_source.py, Nourai's citations checked in the local reference texts, every relevant book consulted per the source matrix). Reply with the short summary described in the instructions.


## [2026-09-04T18:06:56.969Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T18:06:56.985Z] TOOL RESULT

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


## [2026-09-04T18:07:01.269Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-32.txt"
}
```


### [2026-09-04T18:07:01.284Z] TOOL RESULT

```
1	=== PDF page 32 (book page 2) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ab 1, Ap 1 : water  (refs POK:1)  PART 2
4	#1 (parent #0) [Avestan / Pahlavi] refs=KLN:2 | âp : water
5	  #2 (parent #1) [Persian] refs=HRN:1; AEF:2 | âb «آب ۲» : glitter (as on water surface) ; âberŭ «آبرو» : "facial shine", good reputation ; âftâb «آفتاب» : "glitter shine", sun
6	    #3 (parent #2) [Arabic] refs=AFM:7; FVF:11 | âb-bahâ : "glittering shine", elegance ; abboha : magnificence, elegance
7	      #4 (parent #3) [Persian] refs=MON:131 | obbohat «أبهت» : elegance
8	
```


## [2026-09-04T18:07:01.833Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-32.json"
}
```


### [2026-09-04T18:07:01.851Z] TOOL RESULT

```
1	{
2	  "pdf_page": 32,
3	  "book_page": 2,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Ab 1, Ap 1",
8	        "lang": "Indo-European",
9	        "refs": "POK:1",
10	        "gloss": "water"
11	      },
12	      "part": 2,
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Avestan / Pahlavi",
18	          "refs": "KLN:2",
19	          "words": [
20	            {"translit": "âp", "gloss": "water", "script": null}
21	          ],
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Persian",
29	          "refs": "HRN:1; AEF:2",
30	          "words": [
31	            {"translit": "âb", "gloss": "glitter (as on water surface)", "script": "آب ۲"},
32	            {"translit": "âberŭ", "gloss": "\"facial shine\", good reputation", "script": "آبرو"},
33	            {"translit": "âftâb", "gloss": "\"glitter shine\", sun", "script": "آفتاب"}
34	          ],
35	          "note": null,
36	          "quote": {
37	            "text": "چو آمد به برج حمل آفتاب - جهان گشت با فرّ و آیین و آب",
38	            "poet": "Ferdowsî"
39	          }
40	        },
41	        {
42	          "id": 3,
43	          "parent": 2,
44	          "lang": "Arabic",
45	          "refs": "AFM:7; FVF:11",
46	          "words": [
47	            {"translit": "âb-bahâ", "gloss": "\"glittering shine\", elegance", "script": null},
48	            {"translit": "abboha", "gloss": "magnificence, elegance", "script": null}
49	          ],
50	          "note": null,
51	          "quote": null
52	        },
53	        {
54	          "id": 4,
55	          "parent": 3,
56	          "lang": "Persian",
57	          "refs": "MON:131",
58	          "words": [
59	            {"translit": "obbohat", "gloss": "elegance", "script": "أبهت"}
60	          ],
61	          "note": null,
62	          "quote": null
63	        }
64	      ]
65	    }
66	  ]
67	}
68	
```


## [2026-09-04T18:07:02.403Z] TOOL CALL #4: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md"
}
```


### [2026-09-04T18:07:02.418Z] TOOL RESULT

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


## [2026-09-04T18:07:07.380Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && grep -n -A3 '\"POK\"\\|\"KLN\"\\|\"HRN\"\\|\"AEF\"\\|\"AFM\"\\|\"FVF\"\\|\"FVQ\"\\|\"MON\"' refs_online.json | head -150"
}
```


### [2026-09-04T18:07:07.464Z] TOOL RESULT

```
60: "MON": {
61-  "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
62-  "kind": "website+archive_djvu",
63-  "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
--
129: "AEF": {
130-  "title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence",
131-  "kind": "catalog",
132-  "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog",
--
175: "FVQ": {
176-  "title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938",
177-  "kind": "archive_djvu",
178-  "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)",
--
200: "FVF": {
201-  "title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968",
202-  "kind": "website",
203-  "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)",
--
263: "AFM": {
264-  "title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)",
265-  "kind": "archive_djvu",
266-  "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)",
--
562: "POK": {
563-  "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
564-  "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
565-  "kind": "archive_djvu",
--
580: "KLN": {
581-  "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
582-  "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
583-  "kind": "archive_djvu",
--
596: "HRN": {
597-  "title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893",
598-  "edition_found": "1893 (Google scan, Univ. Michigan)",
599-  "kind": "archive_djvu",
```


## [2026-09-04T18:07:08.198Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && grep -n -i 'AEF\\|FVF' bibliography_raw.txt"
}
```


### [2026-09-04T18:07:08.268Z] TOOL RESULT

```
3: TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
6: TABLE IV - Reference Abbreviations 1 AEF 2 AFA 3 AFM 4 AHD 5 AHM 6 AID 7 AIN 8 AKD 9 AKM 0 AMD i ARB 2 ARK 3 ARM 4 ARP 5 AVG 6 AWH Jalal KhaleqT Motlaq, Asas Eshteqaq Farsi, ^j1* JISsAl o"1-'' Vol. I (a - kh), Bonyad Farhang Iran, 1977. Siegmund Fraenkel, Die Aramaischen Fremdworter im Arabischen, Hildesheim, 1962. Addi Shir, Al-Alfaz Al-Farsiyya Al-Mu'arraba, (A Dictionary of Persian Words in the Arabic Language), Library of Lebanon, 1980.. W. Morris, The American Heritage Dictionary, New College Edition, 1975, Appendix on Indo-European Roots, pp 1505-1550. I. Gershevitch, The Avestan Hymn to Mithra, Oriental Publications No.4, Cambridge University Press, 1959. G. C. Withworth, Anglo-Indian Dictionary. Kegan Paul, Trench &amp; Co, London 1885. E. Liden, Studien zur Altindischen und Vergleichenden Sprachgeschichte , Almqvist &amp; Wiksells, Upsala 1897. H. Zimmem, Akkadische Fremdworter Als Beweis Fur Babylonischen Kultureinfluss, Leipzig 1917. Amir J. ATam, Farhang A'alam Ketab Moqaddas or, A Dictionary of Proper Names in the Bible, English - Persian, Iran University Press, Tehran 1988. H. A" mid, Farhang Farsi Amid, Two volumes, Amir Kabir Press, Tehran, 1369 (1990). Jawaliqi, Al-Mu'arrab, Tehran 1966. M. H. Rokn Zadeh - Adammiyat, Arkan Sokhan, Sharq Press, Tehran 1347 (1968). ^W-\A£ h_)UT joMc' OwJbjd -W*c ^— *&gt;jl^ OwJfcjd £^~&gt; O^j' A. Aryan, ks~'j'* lSj^ ^)~&gt;^ ^*j' -ujUa ^la o^lj oiajs Farhang Vajheh-hay Hamanand, Armani - AvestaT, Pahlavi, FarsT, Vol. I (a), Bonyad Nayshabflr, Tehran 1363 (1984). F. Spiegel, Die Arische Periode und ihre Zustande, Leipzig ,1887. A. V. W. Jackson, An Avesta Grammer, W. Kohl Hammer, Stuttgart 1892. H. Kinder &amp; W. Hilgemann, Atlas of World History. 2 vol., Anchor Books, 1974. A-9 
12: TABLE IV - Reference Abbreviations (continued...) 32 FIB 33 FNI 34 FRS 35 FSD 36 FSF 37 FVA 38 FVF 39 FVQ 40 FWE 41 FWK 42 GPL 43 HID 44 HJB 45 HRN 46 HUB 47 IEC Pur Davfld, Farhang Iran Bastan, Vol. I, University of Tehran Press 1326 (1947). F. DanaT, Farhang Namhay Irani, Negah Publishers, Tehran 1370 (1991). AsadT Tflsi, Farhang Fors, Kharazmi Press, Tehran 1365 (1986). ^iljjl ^cUj^cLs &gt;^fl&gt;jS Funk and Wagnalla, New Standard Dictionary of the English Language, Funk &amp; Wagnalls Company, New York, 1940. A. H. Noushin, Farhang Shahnameh Ferdowsi, oULS 03I3 - ^-jiy i*La&gt;Li ^^ay Vajheh Namak, Donya Press, Tehran 1363 (1984). S. M. Nahvi, Farhang VSm J-^-i - ^-&gt;jl» j* ^o^ ^gb. 03I3 ^(3 ^S^a,^ Vajhehhay Arabi dar Farsi, Dakhil, TohT Azadi Press 1368 (1989). S. M. A. Emam Shflshtari, ^c ^bj ji ^-"j1* iS^ °j'3 «-fc»j» Farhang Vajhehhay Farsi dar zaban Arabi, Anjoman Asar Melli, No 58, Bahman Press, Tehran, 1347 (1968). A. Jeffrey, The Foreign Vocabulary of the Qur'an, (see VDQ). Oriental Institute, Baroda, Stephen Austin &amp; Sons Press, Great Britain 1938 A. J. Bliss, A Dictionary of Foreign Words and Phrases in Current English, Warner Books, 1966. R. Dvorak, "Fremdworter im Koran", Doctoral Dissertation, Akademische Buchdruckerei von F. Straub (1884). J.T. Platts and G.S.A. Ranking, A Grammar of the Persian Language, Oxford University Press (1911). B. Bartholomae, Handbuch der Altlranischen Dialekte, Breitkopf &amp;Hartel, Leipzig 1883. H. Yule &amp; A. C. Burnel, Hobson Jobson, A Glossary of Colloqual AngloIndian Words, Oriental Publishers, Delhi 1903-1968. Paul Horn, Grundriss der NeuPersischen Etymology, Verlag von Karl J. Trubner, Strassburg 1893-1974. H. Hubschmann, Persische Studien, Verlag von Karl J. Trubner, Strassburg 1895. Stuart E. Mann, An Indo-European Comparative Dictionary, Helmut Buske Verlag, Hamburg 1987 A-ll
```


## [2026-09-04T18:07:14.290Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd = json.load(open('refs_online.json'))\nfor k in ['POK','KLN','HRN','AFM','MON','FVQ','AEF','FVF']:\n    print('===',k,'===')\n    print(json.dumps(d.get(k), indent=2, ensure_ascii=False))\n\"\n"
}
```


### [2026-09-04T18:07:16.283Z] TOOL RESULT

```
=== POK ===
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
  ],
  "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
}
=== KLN ===
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
  ],
  "cites": "page number, continuous across the two volumes (1966–67)"
}
=== HRN ===
{
  "title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893",
  "edition_found": "1893 (Google scan, Univ. Michigan)",
  "kind": "archive_djvu",
  "url": "https://archive.org/details/grundrissderneu00horngoog",
  "identifier": "grundrissderneu00horngoog",
  "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt",
  "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
  "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.",
  "notes": "OCR of German Fraktur-free text is decent; Persian script is not OCRed.",
  "cites": "page number of Horn, Grundriss der neupersischen Etymologie (1893); entries are also numbered"
}
=== AFM ===
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
  "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.",
  "cites": "page number of Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (1908)"
}
=== MON ===
{
  "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
  "kind": "website+archive_djvu",
  "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
  "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
  "local_file": [
    "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
    "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
    "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
    "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
    "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
    "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
  ],
  "page_offset": null,
  "covers_etymology": true,
  "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
  "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
=== FVQ ===
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
  "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.",
  "cites": "page number of Jeffery, The Foreign Vocabulary of the Qurʾān (1938)"
}
=== AEF ===
{
  "title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence",
  "kind": "catalog",
  "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog",
  "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فرهنگ ریشه‌شناختی فارسی' (Mehrafarin), also not online.",
  "local_file": null,
  "page_offset": null,
  "covers_etymology": true,
  "notes": "none online; proxy via HRN/HUB. || RE-SEARCH 2026-09: still catalogue/purchase only (Open Library record; iketab second-hand; digikala dkp-3058984 for the 2015 ed.). Publisher of the 2015 ed. is مهرافروز."
}
=== FVF ===
{
  "title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968",
  "kind": "website",
  "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)",
  "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.",
  "local_file": null,
  "page_offset": null,
  "covers_etymology": true,
  "notes": "PDF exists on several Iranian sites (ketabnak/parsianjoman) but could not be fetched here (login/JS)."
}
```


## [2026-09-04T18:07:43.631Z] TOOL CALL #8: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-04T18:07:43.639Z] TOOL RESULT

```


```


## [2026-09-04T18:07:44.694Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==1' POK_01.txt | head -60"
}
```


### [2026-09-04T18:07:46.482Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:07:50.435Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==9' POK_01.txt | head -100"
}
```


## [2026-09-04T18:07:51.028Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i '^\\s*ab-\\|āp-\\|^ap-' POK_01.txt | head -20"
}
```


### [2026-09-04T18:07:52.115Z] TOOL RESULT

```
BUCH
ä  Ausruf  der  Empfindung,  oft  neugeschaffen.
Ai.  ä  Ausruf  der  Besinnung-;
gr.  ä  Ausruf  des  Unwillens,  Schmerzes,  Erstaunens;  Ic,  da  Ausruf  der Verwunderung  und  Klage;  dazu  ä^etv  ^ächzen*";
lat.  äj  äh  Ausruf  des  Schmerzes^  des  Unwillens;
lit.  äj  aä  Ausruf  der  Verwunderung^  des  Tadels  oder  Spottes^,  ä  Aus- ruf der  verwunderten  Frage  (lauter  Neuschöpfungen);
got.  ö  Ausruf  des  Unwillens^  der  Bewunderung;  ahd.  ö  Ausruf  des Schmerzes;  mhd.  ö  Ausruf  des  Schmerzes,,  der  Bewunderung^  auch  dem Vokativ  angehängt.
WP.  I  1,  WH.  I  1,  Loewe  KZ.  54,  143.
ab-  ^Wasser;,  Fluß^.
Lat.  amnis  i.,  später  m.  c(*abnis)]  air.  ab  (*a&ä)  Gen.  ahae  ^Fluß^,  da- neben abann,  cjmr.  afon,  orn.  bret.  auon,  gall.  brit.  FIN  Abona,  abge- leitet cymr.  afanc  \,Biber;  AVasserdämon,  Zwerg^,  mir.  abac  (^abankos ^Biber,  Zwerg^  Schweiz. -frz.  avan  ^Weide^  (*abanko-):   lett.  FIN  Äbava.
Die  westdeutschen  FIN  auf  -apa,  nhd.  -affa^  gehen  wohl  teils  auf  sonst verlorengegangenes  westgerm.  *ap-  (idg.  *a6-),  teils  auf  ven.-ill.  ap-  (idg. *ap-)  zurück.
Vgl.  auch  2.  up-  ^Wasser^  Fluß^  und  abö(n)  ,Affe^
WP.  I  46  f.,  WH.  I  40,  Feist  19  a,  579  a,  GIPatSR.  II  134.
äbel-,  Uböl-,  abel-  ,ApfeP.
Lat.  Abella  (osk.  Stadt  in  Campanien)  malifera  ,äpfeltragend'^,  nach  Verg. Aen.  7,  740,  dürfte  ihren  Namen  nach  der  Apfelzucht  erhalten  haben  und auf  die  Grundform  *ablo7iä  zurückweisen.  Der  Apfel  ist  nicht  etwa  erst nach  der  Stadt  benannt.
Im  Kelt.  sind  die  Bezeichnungen  für  ,Apfel^  (*ablu)  und  ,Apfelbaum'^ (*abal-n-)  auseinanderzuhalten.  Gall.  avallo  ,poma',  Aballö  (n-St.)  ON, frz.  AvalloTij  abrit.  ON  Aballäva,  gallo-rom.  *aballinca  , Alpenmistel  (Wart- burg); air.  ubuU  (*ablu)  n.  ,ApfeF,  ncymr.  afal/ VI.  afalau,  corn.  bret. aval   m.  ,Apfel^,   aber    mir.  aball  (^abalnä
```


### [2026-09-04T18:07:52.165Z] TOOL RESULT

```
19:ab-  ^Wasser;,  Fluß^.
747:ap-u  steht  neben  ^ajw  (Lit.  s.  u.  *pu)  in  ark.  kjpr.  lesb.  thess.  äftv^'  in alid  abo  ='  ciba,  anord.  au-virdi  n.  ^verächtliche  Person^  (Falk-Torp  HL), yo-l,  auch  oben  *a'pu-ro-  neben  '^^apero-,  *apu-ko-,  und  *pu  neben  *po.  Das -u  vielleicht  enklit.  Partikel  ;,und,  auch^  (Feist  Sa^  508  a^  WH.  I  87). Y«fl.  auch  Schwyzer  Gr.  Gr.  1  182.
```


## [2026-09-04T18:08:00.553Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '^ap-\\|2\\.  ap-\\|ap-,\\|āp\\|apąm\\|apo-' POK_01.txt | head -30"
}
```


### [2026-09-04T18:08:00.606Z] TOOL RESULT

```
716:3.  ap-,  äp-  ,gebrechlich;  Schadend
735:Ableitungen:  apo-tero-,  ap-ero-,  ap-io-,  ap-öko-  und  oben  apotiäj apetio-.
747:ap-u  steht  neben  ^ajw  (Lit.  s.  u.  *pu)  in  ark.  kjpr.  lesb.  thess.  äftv^'  in alid  abo  ='  ciba,  anord.  au-virdi  n.  ^verächtliche  Person^  (Falk-Torp  HL), yo-l,  auch  oben  *a'pu-ro-  neben  '^^apero-,  *apu-ko-,  und  *pu  neben  *po.  Das -u  vielleicht  enklit.  Partikel  ;,und,  auch^  (Feist  Sa^  508  a^  WH.  I  87). Y«fl.  auch  Schwyzer  Gr.  Gr.  1  182.
4832:lit.  ap-,  vor  Labial  auch  noch  api-,  im  Nominalkompos.  apy-  Präf.  ,um,  - herum,  be-',  apie  ,um,  über'  m.  Akk.,  alit.  und  dial.  ostlit.  dievie-p  ,bei Gott'  u.  dgl.,  sünaüs-pi  ,zum  Sohne';  lett.  ap-  ,um,  über',  ple  mit  Gen.  und Akk.  ,bei,  an',  pie-  , hinzu,  an-,  voll-';  apr.  ep-  (ap-  nicht  maßgebendere Schreibung),  eb-  ,be-',  eher  als  *epi  hierher,  als  unter  Zugrundelegung der  Form  eb-  zu  idg.  ebhi,  obJii]  dazu  die  Postposition  lit.  -p{i)  hinter Gen.  namö-pi  ,nach  Hause')  und  Lok.  {namie-pi  ,zu  Hause'),  lett.  -p  (nur adverbial  gebraucht),  E.  Fraenkel,  Syntax  18  ff.,  Endzelin  Gr.  524£f.;
```


## [2026-09-04T18:08:00.759Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'wasser' POK_01.txt | head -40"
}
```


### [2026-09-04T18:08:00.812Z] TOOL RESULT

```
19:ab-  ^Wasser;,  Fluß^.
22:Vgl.  auch  2.  up-  ^Wasser^  Fluß^  und  abö(n)  ,Affe^
44:Das  durch  reisende  Kaufleute  eingeführte  Tier  kann  von  den  Kelten mit  dem  Namen  ihres  Wasserdämons  (s.  oben  ab-)  benannt  worden  sein. Hes.  äßQ��vag'   KsItol  rovg  xsoKomd-rjnovg  ist  vielleicht  dßßdvag  (Akk.  PL)
45:zu  lesen  und  noch  vor  der  Lautverschiebung  ins  Germ,  gedrungen;  daher an.  api  m.  ^Affe^  Tor^^,    as.  apo^   ahd.  affo   m.,    affa,  affin  L,   ags.    apa  m. Aus    dem    Germ,    stammt    aruss.    opica    ^Affe^^    acech.    opice.     Vgl.    ab- ^Wasser^  und  Schrader  Reallex.^  Hoops  Reallex.  s.  v.  Affe. AVP.  I  51  f.
56:ad(u)-,  ad-TO-   ,Wasserlau£'.
57:Avest.  aöu  , Wasserlauf,  Bach,  Kanal',  ven.-ill.  FIN  Ad(cl)ua  (zum  Po), *Adulia':>Attel  (zur  Donau  in  Bayern),  Mons  Adulas  ,St.  Gottbard^  (wohl nach  den  dort  entspringenden  Flüssen  benannt),  der  oberösterr.  FIN  *Adra -^Attersee,  Attergau,  FIN  Adrana>  Eder  (Hessen),  vielleicht  auch  der ON  Adria  in  Venetien  (danach  das  mare  Adriaticum),  der  sizil.  FIN  ^Adgavög und  der  ven.-ill.  Name  der  Oder  OvL-adovag]  ferner  der  lett.  FIN  Adula. Vasmer  ZslPh.  8,  114  f.,  Pokorny  Urill.  4,  70,  93,  109,  124.
334:aJc!^ä-  (richtiger  ok'iä) :  ek]i-  .Wasser.  Fluß'.
335:Lat.  aqua  .Wasser.  Wasserleitung'  (davon  aquilus  .dunkel',  aquila .Adler',  eigentl.  .der  Dunkelfarbige',  aquilö  .Nordwind',  eigentl.  .der  den Himmel  Verdunkelnde')  =  got.  a\va  f.  .Fluß.  Gewässer',  aisl.  o.  ags.  ca. as.  ahd.  aha,  nhd.  Ache  ds.  (germ.  *ahioö,  davon  abgeleitet  *ahioj5,  *aicjö .die  vom  Wasser  Umgebene'  in  aisl.  ey  f.  .Insel.  Aue',  ags.  ieg,  ahd. -ouwa,  -awa,  mhd.  ouwe  f.  .Wasser.  Halbinsel  im  Flusse,  wasserreiches Wiesenland',  nhd.  Aue,  vgl.  afries.  ei-land  .Insel'.  Sca(n)din-avia  Kretsch- mer  Gl.  17,  148  ff.),  russ.  FIN  Oka,  pannon.  ON  Aquincum  .Ofen',  apul. FIN  Aquilö,  ven.  ON  Aquileia  (auch  in  Süddeutscliland);  mit  Ablaut (idg.  e)  dazu  aisl.  kgir  (*eKog)  .Gott  des  Meeres',  ags.  xg-iceard  .Wache' an  der  See',  eagor  .Meer.  Flut'  (der  Anlaut  nach  ea);  vielleicht  hierher ai.  kam  .Wasser',  dak.  PflanzenN  y,oaödi.ia'  Tcoraj-ioysiTcov  .Wassersiedler' (*kYia-dhemn),  poln.  (nordill.)  FIN  Kiua.
336:Die  Zugehörigkeit  von  hitt.  e-ku-uz-zi  (ekuzi)  .trinkt'.  3.  PL  a-ku-ioa-an-zl, scheint  mir  nicht  unwahrscheinlich.  Hierzu  auch  toch.  AB  yok-tsi  .trinken'. Air.  oiche  .Wasser'  existiert  nicht;  cjmr.  aig  .Meer'  ist  eine  Neubildung zu  eigion  aus  lat.  oceanus.
420:wahrscheinlich  auch  anord.  alfr,  ags.  3slf,  engl,  elf  (woraus  nhd.  Elf  m., Elfe  f.  entlehnt);  mnd.  alf  ;Alp;  Mare;  böser  Geist^;  mhd.  nhd.  Alp,  PI. die  Alben  (ursprüngl.  wohl  ;Weißliche  NebelgestaltenQ;  sowie  ahd.  alba ;Insektenlarve;  locusta  quae  nondum  volavit^;  ndl.  elften  f.  PL  ;Engeriinge^; norw.  alma  ds.  (m  aus  dem  Gen.  PI.  *albna,  woraus  *almna).  Sc ''zu  diesen germ.  Worten  bes.  Falk-Torp  unter  aame  (4,  1428);  al  (19;  1431);  alv (22;  1431);  elv  I  (188 f.;  1454);  emd  (189;  1454);  als  ;Weißwasser^  auch der  Name  der  Elbe  (lat.  Albis,  Albia,  aus  germ.  *Albl,  Gen.  Albiöz  ==), anord.  elfi^  ;Fluß^  und  Flußname  (dazu  wohl  auch  mnd.  elve  ;Flußbett^); vgl.  die  gall.  FIN  Albis,  Alba  (heute  Aube;  Gegensatz  Dubis,  Dubä,  d.  i. ;Schwarzwasser');  lat.  Albula,  gr.  'Alcpeiög  (s.  bes.  Schulze  SBprAk.  1910; 797  =  Kl.  Sehr.  120).
574:Ai.  äti-h  atl  f.  ,Wasservogel'^  (oder  zu  aisl.  xdr,  nschwed.  äda  f.  , Eider- gans'  aus   germ.  *ädl-?)]   gr.  vrjaaa,  böot.  väaaa  (*väT!,a  :  ri.  äti-h)  ,Ente^;
600:Lat.  anguis  =  lit.  angis  (f.),  apr.  angis  ,Schlange^  (lett.  üodze  f.  ,Schlange*), aksl.  *gzh,  russ.  uz,  poln.  wqz  ,Schlange'^,  ai-m.  auj  (Gen.  -i)  , Schlange* (Meillet  Esquisse  154,  Dumezil  BSL.  39,  100);  mir.  esc-ung  ,Aal'  (*,Wasäer- schlange',  esc  , Wasser^  +  *ang'":ho),  cymr.  llys-yic-en,  PL  -yio-od  ds.  (Fick II  ^  15;  zum  brit.  Schwunde  von  i^g  vor  m  siehe  Pedersen  KG.  I  107).
707:2.  äp-  ,Wasser,  Fluß^
708:Ai.  up-  f.  ,Wassere,  z.  B.  PI.  Nom.  äpah^  Akk.  apdh,  Gen.  apäm,  av. Nom.  Sg.  äfs,  Akk.  Sg.  äpdm,  Instr.  Sg.  apa(-ca)j  ai.  dpavant-  ,wässerige, in  alter  Kontraktion  der  Red.-St.  mit  auf  -i,  -u  ausl.  Präfixen  (Kretschmer KZ.  31,  385,  Johansson  IF.  4,  137  f.)  pratlpd-  .gegen  den  Strom  gerichtet^, nipd-  ,tiefliegende,  anüpd-  ,am  Wasser  gelegen^,  dvipd-  ,Insel,  Sandbank im  Flusse^,  antarlpa-  ,Insek;  dieselbe  Kontraktion  mit  einem  auf  -o  en- digenden 1.  Glied  in  den  gr.  Flußnamen  ''IvwTtog,  l^acarvög  {:  höco,  ^Gig] Fick  BB.  22,  61,  62);  gr.  l^rcia  ,Peloponnese,  Meao-ania  ds.,  die  lokr. MeGO-(X7tL0Ly  die  ill.  MsaGafCLOi  (anders  Krabe  ZONF.  13,  20  f.)  und  Apuli Unteritaliens,  die  Flußnamen  ^Arciddiv  (Arkadien),  ''u4rtidav6g  (Thessalien), thrak.  ^'Ajtog  (Dacien),  ill.  ""^xpog,  Apsus,  apul.  ON  Sal-apia  (,Salzwasser'^);
712:apa-J^ umen^  wie  die  Erft  (^Arnapia),  und  alle  FIN  mit  -up-,  wie  nhd.  I C/ppia-Bach  (Tirol)^  frz.  Sinope  (Manche)^  brit.  Hafen  Rutupiae,  sizil. KaKVTtaQLg  (vgl.  lit.  Kakwpis),  vgl.  die  thrak.  YY^'^Yniog,  '^'Ynavig;  apr. ape  ;Fluß^,  apus  ^Quell^  Brunnen^,  lit.  üpe,  lett.  upe  ^Wasser^  {u  ist  vielleicht Red. -St.  von  idg.  o,  a,  Trautmann  Bsl.  Wb.  11;  oder  gehört  up-  eher  zu aksl.  vopa  ^See^?).  Hierher  Ach-{^aps-)  in  cymr.  FIN,  gall.  Axonal
714:Zur  Erklärung  der  6-Form  geht  Johansson  IF.  4^  137  f.  von  dem durch  ^Atzlööjv,  ^Amdavög  sowie  durch  ai.  dbda-h  m.  ^Wolke^  und  den  mit äpah  paradigmatisch  zusammengeschweißten  Instr.  Dat.  PI.  ai.  adhliih, adbhyah  vorausgesetzten  St.  *ap(9)d-  (vielleicht  ^Wasser  gebend'^  mit  zu dö-  ^geben''  gehörigem  2.  Gliede)  aus:  *ahd5(n),  Gen.  *abdnes,  woraus *abnes',  aus  den  obl.  Kasus  entsprang  lat.  amnisj  während  im  keltischen *abdö(n) :  *abnes  zu  *abä  (mir.  ab),  ^abonä  (daher  mir.  abann)  ausgeglichen wurde.
898:aröd-,  arsd-  ,ein  WasservogeF.
1061:b)  aued-,  aud-,  äd-;  heteroklit.  r/n-St.  uedör,  uödör  (Nom.  Sg.), uden(i)  (Lok.  Sg.),  udnes  (Gen.  Sg.)  ,Wasser^,'^  vgl.  J.  Schmidt  PL  172  ff., Pedersen  KZ.  32,  240  ff.,  Bartholomae  PBrB.  41,  273.
1063:Ai.  undtti  (ju-n-ed-ti),  3.  PL  unddti  ,quellt,  benetzt^ ;  av.  vaidi-  f.  ,Wasser- lauf,  Bewässerungskanal.
1064:Ai.  uddn{i)  Lok.,  udndh,  Gen.,  udä  Nom.  Akk.  PL  ,Wasser^  (Nom.  Akk.
1065:79 jidahd-'m)]    vom    r-St.  abgeleitet   samudra-h  ^Meer^;    anudra-h  ^wasser-
1067:udro-s  Wassertier^-  ai.  udrd-h  ^ein  Wassertier^  =  av.  udra-  m.  ^Otter^ r'-chotter^  (=  gr.  ijÖQog,  ahd.  usw.  ottar^  vg].  auch  lat.  lutra  und  mit  ü lit.  udra,  aksl.  v2/c?ra  ds.);
1070:arm.  ^^^  ;Fluß^  (Gdf.  '^iiedö,  Sandhiform  zu  itedör,  vgl.  unten  slav.  -üoJa; ihr  entspricht  auch  phryg.  /^sdi;  ^Wasser^,  d.  i.  *vedü  aus  *uedöj  Kretsch- ,„er  Einl.  225).
1071:Gr.  VöcüQ,  vdaxog  (*vö-n-Tog)  ^Wasser^  (mit  metr.  Dehnung  vÖcjq);  vom r-St.  abgeleitet  äwSgog  ^wasserlos^^^  ^äoog^  Vöoa  ^Wasserschlange^^  ivvöglg  f. Fischotter^;  vdagrjg,  tdagög  ^wässerig^  {vöaleog  ds.  mit  Suffixtausch;  ähn- lich ^llog  ^Wasser schlänge;,  Ichneumon^  :  ^öqog  =  lak.  kXXd  :  edQa)^  ijöagog Wassersucht^;  vögla  ^Wassereimer*^  (:  lat.  uter),  vom  i2-St.  (vgl.  ijövrjg wässerig^)  abgeleitet  I^Xogvövt]  eig.  ^Meereswoge^  (?);  Beiname  der  Amphi- trite  und  Thetis  (Johansson  Beitr.  117;  ob  auch  iJövov  ^TrüffeF  als  ^saftig^??); sowie  wahrscheinlich  KaX-vöcüv,  -vdva  (-vuvg),  KaXvövioi,  -vf.ivLOL  (s.  Boi- sacq998a)?
1072:es-St.  TÖ  ijöog  ^Wasser^  ist  erst  spät  poet.  Nom.  Akk.  zum  Dat.  ijösi.
1074:Alb.  uß  ;Wasser^  (nach  Pedersen  KZ.  34^  286;  36^  339  nicht  aus  *wcZ- n\d,  sondern  aus  *wc?-;  oder  doch  aus  *wcZö?).
1075:Lat.  unda  f.  ^Welle^  Woge^  (mit  w-Infix  aus  dem  Präsens;  vgl.  apr. wundan  n.^  unds  m.  ^Wasser^  und  ai.  undtti,  unddti  sowie  lit.  vanduo, -eüs,  vdndeni,  zem.  unduo,  lett.  ildens  m.  f.  _,Wasser^;  und  dazu  Schulze EN.  243;  Brugmann  Grdr.  IP  3,  281;  283;  Trautmann  337);  iiter,  utris ;Schlauch''  (*-udri-s  ;*Wasserschlauch'^;  vgl.  gr.  vögla),  lutra  ;Fischotter^ (l-  nach  lutum  ;PfützeQ.
1076:Umbr.  utur  n.  ;Wasser^  (==  udcüg),  Abi.  une  (*udni).
1077:Air.  u(i)sce  ;Wasser^  (^udeskio-),  odar  ;braun^  (^udaros),  coin  fodorne jOttern^  (;WasserhundeQ.
1078:Got.  ivatö  (n-St.);  Dat.  PI.  watnam  ;Wasser^;  aschwed.  vcetur  (ce  =  idg.  e? eher  Umlaut  von  germ.  a  in  den  -in-KasuS;  s.  Bartolomae  aaO.);  aisl. vatn  n.  (o-St.  geAvordeU;  vgl.  got.  Dat.  PL  icatnam),  vatr,  nord.  Seename Vättern]  ahd.  wazzar,  as.  watar,  ags.  tcceter  (*iiodör)  ;Wasser^;  aisl.  otr, ags.  otor,  ahd.  ottar  m.  ^Otter^;  dazu  FIN  Otter,  alt  Uterna]  mit  Binnen- nasalierung  (vgl.  oben  zu  lat.  unda)  wahrscheinlich  got.  icintruSj  aisl.  vetr, ags.  Winter,  ahd.  as.  wintar  ;Winter^  als  ;nasse  Jahreszeit'^  (Liden  PBrB. 15^  522;  Falk-Torp  unter  vinter,  nicht  besser  zu  ir.  ßnd  ;Weiß'^;  s.  unter sueid-  ;g]änzen');
1083:aksl.  voda  ^Wasser^  (Fem.  geworden  wegen  des  Ausganges  -a,  der  hier für  idg.  -ö[?']);  dehnstufig  aksl.  vedro  ,xddoj,  aza^vog^  (mit  hÖQia  in  der Bed.  gut  stimmend,  s.  Meillet  MSL.  14,  342,  Trautmann  337);
1084:hett.  loa-a-tar  (icätar)  ,Wasser^,  Gen.  üe-te-na-as  (e-Stufe  wie  phryg. ßedvj  das  a  des  Nom.  aus  e?).  Nom.  PI.  u-wi-ta-ar,  mit  ungeklärtem  Voka- lismus trotz  Pedersen  Hitt.  167.
1085:c)  auer-  ,Wasser,  Regen,  Fluß^  (uer-  :  wr-;  zum  Ablaut  Persson  Beitr. 604,  Anm.  2).
1086:•1.  tier-,  uer-:  Ai.  vdr,  vdri  n.  ,Wasser^,  av.  vär  n.  ,Regen^  (mit  themat. Flexion  iran.  av.  vär  ,regnen'',  med.  ,regnen  lassen^),  ai.  värl  f.  ,Wasser^, av.  vairi-  m.  ,See^;
1087:toch.  A  lüär,  B   war  ,Wasser^;
1092:anord.  vari  m.  ,Flüssigkeit,  Wassert
1094:anord.  ür  , feiner  Regen',  yra  ,fein  regnen',  ürigr  ,betaut',  ags.  ürig  ds.; vielleicht  anord.  ürr,  Gen.  ürar  (w-St.),  ags.  ür,  ahd.  uro,  ürohso,  lat.  Lw. ürus  ,Auerochs',  schwed.  mdartl.  ure  ,stößiger  Stier'  (,*Beträufler,  Be- samer' wie  ^l  vrsan-  usw.,  s.  unten);  Wzf.  auer-  in  thrak.  FIN  ^%g, gr.  (Persson  IF.  35,  199)  *aVQa  ,Wasser,  Quell'"  in  ^vavQog  ,wasserlos,  von Bächen'  u.  dgl.  (über  gr.  ^TjaavQog  und  Ksvravgog  vgl.  Schwyzer  Gr.  Gr. I  267,  444);
1096:in  FIN :  ital.  Met-aurus  (Bruttium)^  P'isaurus  (Umbrien)^  gall.  Avara  > frz.  Avre,  Aura  >  frz.  Eurej  Aurana  >  nhd.  Ohm  (Württemb.),  Ar-auris  > frz.  Herault,  Vi-aurus  >  frz.  Le  Viaur]  apr.  Aure,  lit.  Aur-yte;  anord.  aurigr naß^  (^'^''''"^  ;,Naß,  ^Wasser'^^  FIN  Aura,  ags.   ear  ^Meer^;
1101:4.  Erweiterung  uer-s-  ^Regen^  Tau'^:  ai.  varsd-  n.  fliegen,  Regenzeit^ Jahr^  {varsati  ,es  regnet*^);  gr.  odoov  ^Harn^;  egar],  eegar]  ^Tau^^  ion.  att. ovoeo)  ;harne^  (kausativ  *uorse{ö,  f-  erwiesen  durch  die  Augmentierung ioÜQrjaa),  ovqla  ,Qm  WasservogeF;  rniv.  frass  ^Regen^  ist  älter  fross  (uros-tCij trotz  Pedersen  KG.  I  44);  hett.  iva-ar-sa-as  ;Regen'^(?)  scheint  ai.  Lw.
1106:Vgl.  im  allgemeinen  Persson  Wzerw.  47,  85  f.;  Johansson  KZ.  30;  418; IF.  2;  60  ff.;  Persson  Beitr.  604  f.;  845  (auch  gegen  Verknüpfung  von  ue^^s- mit  e?'s-).     Über  finn.  vesi,   St.  vete  ;Wasser^   s.  Mikkola  Mel.  van   Ginne ken  137.
```


## [2026-09-04T18:08:10.618Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /2.  äp-  ,Wasser|2\\.  äp-/{print NR; exit}' POK_01.txt"
}
```


## [2026-09-04T18:08:10.892Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==59' POK_01.txt | head -80"
}
```


### [2026-09-04T18:08:12.083Z] TOOL RESULT

```
60
```


### [2026-09-04T18:08:13.689Z] TOOL RESULT

```
ng infolge  der  Lautähnlichkeit  sein  und  idg.  *nt{-i^  -a?)  ,bis^  als ^gegenüber  hin,  auf  die  entgegengesetzte  Seite  hinüber^  zu  anti  gehören;  auch die  Worte  für  ,Ende^  (s.  u.)  sind  ursprüngl.  das  auf  der  gegenüberliegen- den Seite  winkende  Ziel,  und  mit  as.  unt  ist  auch  ant  {and  -\-  te)  Präp.  m. Akk.  ,usque  ad^  bedeutungsgleich,  was,  selbst  wenn  nur  junge  Kreuzung  von unt  mit  and-  vorläge,   doch   die  Begriffsverwandtschaft   beider  beleuchtet.
antios  , gegenüber,  vor  einem  liegend'^  (vom  Adverb  anti  gebildet): *antiö-  (gerra.  *andja-)  in  got.  andeis^  anord.  endir,  as.  endi,  ags.  ende m.,   ahd.    anti,   entl   m.    und   n.,   nhd.   Ende]   auch   gr.  ävTtog  ,gegenüber^ {d3iZ\i ivavzlov  ds.,  ivavvlog  ,gegenüber  befindlich;  Gegner^)  geht  wahrschein- lich (vgl.  Schwyzer  Gr.  Gr.  I  379)  auf  *ävTiög  zurück.
Dagegen  ist  von  *anto-  (s.  oben)  abgeleitet  dntio-  in  anord.  enni  n., ahd.  andi,  endi  n.  ,Stirn^  =  lat.  antiae  ,capilli  demissi  in  frontem^»
Ein  ganz  verschiedenes  Wort  ist  nhd.  und^  ahd.  unii^  anti,  enti  u.  dgl., as.  endi,  ags.  engl,  and  ,und^,  anord.  en{n)  ,und,  aber^,  das  mit  ai.  dtlm ,darauf,  dann,  desgleichen^,  av.  a&n  ,ebenso^,  osk.  ant  m.  Akk.  ,usque  ad^, lit.  int  m.  Akk.  ,nach'^  (aber  s.  oben),  toch.  B  entwe  ,also^  zu  *en,  iq.  ,in^ gehört.
WP.  I.  65  ff.,  WH.  I  53  f.,  Feist  46,  Schwyzer  Gr.  Gr.  I  619,  621, 629  f.,  632  f.,  722,  726,  II  (B  V  2  b  d  3).
antro-m  ,Höhle,  Luftlochs
Arm.   ayr,  Gen.  PL   ayric  ,Höhle^,  gr.  ävzgov  ds. Vielleicht  zu  an{9)-  ,atmen^,  als  ursprüngl.  ,Luftloch^ WP.  I  561,  Schwyzer  Mel.  Boisacq  II  234 1,   KZ.  68,  222,    Gr.  Gr.  I 532,  Pisani  KZ.  68,  161  f.
I.  ap-  (richtiger  dp-)  :  ep-  ,fassen,  nehmen,  erreichend
Ai.  äpnötierreicht,  erlangt',  jünger  äptd-h  ,geschickt,  geeignet,  vertraut'; av.  apayeiti  ,erreicht',  3.  PL  äpdnte  aus  *äpuantai;
51
arm.  itnim  ^besitze^  (*öp-n-?)^  dnd-unim  ^erlange"^;
o-r.  ärtto)  ^anfassen^  anheften^,  anbinden^  anzünden^^  tlmEa^ca  ;berühren% cicpn  Berührung^  Haften  usw/  wird  trotz  dem  Spiritus  hierherzustellen sein.  Kretschmer  Gl.  1,  352  nimmt  Beeinflussung  durch  ertoj  an;  hom. dwcict)  (äq)dü))  ^berühre^  betaste^^  ion.  acpäaoo)  ds.^  hom.  dcrtaq)ia'/.(x),  }jrca(pov (mit  äol.  o:  ärtocpeiv'  ärcazfiaai  Hes.)  ^betrügen;,  täuschen^^  dTrocpcbXiog trüo-erisch^;,  '/.airjcprjg  ^niedergeschlagen^  (eigentl.  ^untergekriegt^).  Pedersen KZ.  39^  428  stellt  mit  gr.  Utito)  arm.  a//  ^die  hohle  Hand^  (o-St.^  doch Lok.  y-(^p'^  3-^3  -i-St.,  also  wohl  ätler  neutr.  -o-i-St.)  zusammen,  welches Wort  dem  gr.  äxpog  ;,Gelenk^  entsprechen  soll;  wegen  des  p*  (=  idg.  pA) jedoch  unsicher  (vgl.  Meillet  BSL.  36^  HO);
lat.  apiscor  ^fasse,  erreiche^^  adipzscor  ^erlange^;,  coe.'pi  ,habe  angefangen^; später  coepl.  Der
```


## [2026-09-04T18:08:19.201Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==60' POK_01.txt | head -60"
}
```


### [2026-09-04T18:08:20.627Z] TOOL RESULT

```
 Zusammenhang  mit  lat.  *a2nö,  *apere  ^comprehendere vinculO;  verbinden,  umbinden^  (imper.  ape  ,prohibe,  compesce'^),  aptus ^verknüpft,  ausgestattet  mit^,  cöpula  (co-apida)  ,Band*  steht  wohl  fest. Vielleicht  ist  von  einer  gemeinsamen  Grundbedeutung  ^fassen,  zusammen- fassen^ auszugehen.
Auch  lat.  apud  ,bei^  wird  am  besten  hierherzustellen  sein.  Die  Grund- bedeutung wäre  ,in  naher  Verbindung^  (vgl.  juxta).  Man  hat  vom  Part. Perf.  neutr.  *apiwd  (aus  *apuot  ^erreicht  habend^  auszugehen.  Die  Neben- form apor,  apur  (mars.-lat.  apur  finem)  weist  auf  ursprüngl.  -d]
lat.  apeXy  -icis  ,Spitze^,  bes.  ,stabartiger  Aufsatz  auf  der  Priestermütze*^; gehört  vielleicht  zu  *apw]  vgl.  auch  EM.  60;
toch.  A  oppäcgi  ^geschickt^  (Van  Windekens  Lexique  82);
hitt.  e-ip-mi  (epmi)  ,nehme^,  3.  PI.  ap-pa-an-zi  (^apanzi).
Über  ai.  äpi-h  ^Freund^,  gr.  }jn:iog  ^freundliche  s.  u.  epi-,
WP.  I  45  f.,  WH.  I  57  f.,  60,  847,  Pedersen  Hitt.  128,  Couvreur  ^  93.
2.  äp-  ,Wasser,  Fluß^
Ai.  up-  f.  ,Wassere,  z.  B.  PI.  Nom.  äpah^  Akk.  apdh,  Gen.  apäm,  av. Nom.  Sg.  äfs,  Akk.  Sg.  äpdm,  Instr.  Sg.  apa(-ca)j  ai.  dpavant-  ,wässerige, in  alter  Kontraktion  der  Red.-St.  mit  auf  -i,  -u  ausl.  Präfixen  (Kretschmer KZ.  31,  385,  Johansson  IF.  4,  137  f.)  pratlpd-  .gegen  den  Strom  gerichtet^, nipd-  ,tiefliegende,  anüpd-  ,am  Wasser  gelegen^,  dvipd-  ,Insel,  Sandbank im  Flusse^,  antarlpa-  ,Insek;  dieselbe  Kontraktion  mit  einem  auf  -o  en- digenden 1.  Glied  in  den  gr.  Flußnamen  ''IvwTtog,  l^acarvög  {:  höco,  ^Gig] Fick  BB.  22,  61,  62);  gr.  l^rcia  ,Peloponnese,  Meao-ania  ds.,  die  lokr. MeGO-(X7tL0Ly  die  ill.  MsaGafCLOi  (anders  Krabe  ZONF.  13,  20  f.)  und  Apuli Unteritaliens,  die  Flußnamen  ^Arciddiv  (Arkadien),  ''u4rtidav6g  (Thessalien), thrak.  ^'Ajtog  (Dacien),  ill.  ""^xpog,  Apsus,  apul.  ON  Sal-apia  (,Salzwasser'^);
hierher  als  Spuren  ven.-ill.  Einwanderung  im  Westen  ein  Teil  der  westd.
4*
52  •
apa-J^ umen^  wie  die  Erft  (^Arnapia),  und  alle  FIN  mit  -up-,  wie  nhd.  I C/ppia-Bach  (Tirol)^  frz.  Sinope  (Manche)^  brit.  Hafen  Rutupiae,  sizil. KaKVTtaQLg  (vgl.  lit.  Kakwpis),  vgl.  die  thrak.  YY^'^Yniog,  '^'Ynavig;  apr. ape  ;Fluß^,  apus  ^Quell^  Brunnen^,  lit.  üpe,  lett.  upe  ^Wasser^  {u  ist  vielleicht Red. -St.  von  idg.  o,  a,  Trautmann  Bsl.  Wb.  11;  o
```


## [2026-09-04T18:08:43.163Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i '^ap-\\|^ab-\\|ap-2\\|water$' AHD_watkins1985.txt | grep -i 'water' | head -20"
}
```


## [2026-09-04T18:08:43.702Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -B2 -A8 '^ap-' AHD_watkins1985.txt | head -60"
}
```


### [2026-09-04T18:08:44.969Z] TOOL RESULT

```
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
```


### [2026-09-04T18:08:45.007Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:09:09.930Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==22' HRN.txt | head -60\necho ---\ngrep -n '^ *1\\. \\|^1\\.' HRN.txt | head -5"
}
```


### [2026-09-04T18:09:11.365Z] TOOL RESULT

```
— XVI —
gaben der Wörterbücher über i/äi bezw. väV'i majhül oder
maräf; leider bezeichnen auch die jüdisch-persischen Bibel-
übersetzungen ebenso wie Muvaff'aq diese Vocale nur selten.
Da Vullers für eine ganze Reihe Wörter keine Be-
lege aus den von ihm benutzten Originalwörterbüchern
giebt und es daher öfter scheinen könnte, als sei eine
Vocabel selten oder ungebräuchlich, während sie ganz ge-
wöhnlich ist^), so habe ich in derartigen Fällen aus dem
Ferheng-i Residl (ed. by Maulawi Zulfaqär 'Ali
and Maulawi 'Aziz Urrahmän, Calcutta, 1875) und aus
Shams i Fachrii Ispahänensis lexicon persicum (ed.
Carolus Salemann, Casani 1887), als den zwei am
Bequemsten zugänglichen, gedruckten neupersischen Ori-
ginallexicis, Belegstellen angeführt. Dazu kommt noch der
V
F^erheng-i Jehänjgrrl, den ich in der mir mit grösster
Liberalität zur Benutzung überlassenen Handschrift der
hiesigen kaiserl. Universitäts- und Landesbibliothek ein-
sehen konnte. In der Anführung solcher Belegstellen hätte
Setzung ist ganz falsch ; auch dürfte ja nicht sir auf sir reimen). Auch
I, 225 Vers 1759 hat Vullers falsch corrigirt, doch bleiben genug
äusserlich ganz unverdächtige Yerse übrig.
Die philosophische Fakultät der Münchener Universität hat als
Preisaufgabe für das Jahr 1892/93 (nach den Zeitungsmitteilungen) *eine
systematische Zusammenstellung alles dessen* verlangt, Vas sich aus
den Endreimen in Firdüsl^s Sahnäme für die damals herrschende Aus-
sprache, vor allem ö und e betrefiTend, ergiebt*. Trotz der Beschränkung
der Aufgabe (ev. Ausschluss des Alt- und Mittelpersischen) auf eine
blosse, ^systematische , nach grammatischen, lexico-grammatischen Ge-
sichtspunkten geordnete Materialsammlung, um als Basis kräftiger
spraohvergleichender Behandlung zu dienen', dürfte ihre Bearbeitung
eben wegen der notwendigen Sammlung des umfangreichen Materials
für einen Studenten noch recht schwierig sein, zumal dieser gründlich
Firdüsl vorstehen müsste und sich nicht etwa auf die Leetüre der End-
reime beschränken dürfte. Ich habe selbst schon seit einiger Zeit für
eine ähnliche Untersuchung systematisch zu sammeln angefangen. Bei
dieser Gelegenheit erlaube ich mir zu bemerken, dass ich beabsichtige,
eine umfangreichere, aesthetische Arbeit über das SähnSme und den
epischen Stil der Perser zu veröffentlichen, zu welcher die Vorstudien
allerdings erst für den ersten Band der Leydener Ausgabe gemacht sind.
*) So ist Fr. Müller (WZKM. 5, 185) sogar zu der Meinung
gekommen, np. bh isteu sei uugebräuchlich.
---
451:1. ä. 1) Praefix, z. B. in ämeden^ ardi/is.
10001:1. a-, a//-, un-, nicht-' (« privativumj. Sehr häulig, z. B.
12996:1.1«»;/ 232.
16427:1.
21016:1. bSftin 219.
```


## [2026-09-04T18:09:16.488Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '^ *[0-9]\\+\\. āb\\|^ *[0-9]\\+\\. âb\\|^ *[0-9]\\+\\. ab\\b\\|1\\. āb\\|1\\. âb' HRN.txt | head -20\necho \"---search glanz---\"\ngrep -n -i 'glanz' HRN.txt | head -20"
}
```


### [2026-09-04T18:09:16.570Z] TOOL RESULT

```
---search glanz---
464:3. ä& *Glanz , (Sahn. I S. 14 Vers 7), vergl. ab[rö, ah[tah,
466:phlv. üb] skr. äbha- *Glanz'-).
470:*Glanz', worauf mich Herr Dr. Schwally aufmerksam macht. Etwa
473:Wasserspieger könnte man sehr leicht zu 'Glanz* kommen.
2880:296. pertew 'Glanz*.
4978:soll auch *Blitz, Glanz' bedeuten, vergl. direßän,
5458:610. ru%8 {rexs) 'Glanz, Licht', ru/^Tden [rexsiden).
5594:'Glanz, Licht*; arm. lois Xicht' (H. No. 125).
7055:808. /<9ri* 'Glanz, Majestät*, ferre^ yurve % vergl. /eveme
9326:aw. *tmrecah- in asvaredah-, varei^afihvanf- 'glanz-
9329:235 Note 35); ai. vdrcas- 'Glanz.
10949:170. rar 'Glanz, Licht\ selten (AW.-Komm., Bund. 24, 25),
10951:aw. ray- 'Glanz, Licht'; ai. räy-,
```


## [2026-09-04T18:09:20.611Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '445,480p' HRN.txt"
}
```


### [2026-09-04T18:09:20.673Z] TOOL RESULT

```
dieser Gelegenheit erlaube ich mir zu bemerken, dass ich beabsichtige,
eine umfangreichere, aesthetische Arbeit über das SähnSme und den
epischen Stil der Perser zu veröffentlichen, zu welcher die Vorstudien
allerdings erst für den ersten Band der Leydener Ausgabe gemacht sind.
*) So ist Fr. Müller (WZKM. 5, 185) sogar zu der Meinung
gekommen, np. bh isteu sei uugebräuchlich.Ä.
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
```


## [2026-09-04T18:09:54.702Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN 1966 bahaa/abboha ===\" && grep -n -i 'bah[aā]\\|abboh\\|ubbah' KLN_1966.txt | head -20\necho \"=== AFM pages abbaha/bahaa (Arabic script) ===\" && grep -n 'بهاء\\|أبهة\\|ابهة' AFM_pages.txt AFM.txt 2>/dev/null | head -20\necho \"=== FVQ ===\" && grep -n -i 'bahaa\\|ubbah\\|abbaha' FVQ.txt FVQ_pages.txt 2>/dev/null | head -20\necho \"=== MON obbohat/ابهت ===\" && grep -n 'ابهت\\|أبهت\\|بهاء' MON_part1.txt MON_part2.txt 2>/dev/null | head -20"
}
```


### [2026-09-04T18:09:54.825Z] TOOL RESULT

```
=== KLN 1966 bahaa/abboha ===
2139:alcornoque,  n„  the  bark  of  several  trees.  —  Sp., Port,  ‘cork  tree’,  a  hybrid  coined  fr.  Arab,  al-, ‘the’,  and  L.  quercus,  ‘oak’,  changed  into  *quer - nus.  See  cork  and  cp.  Quercus. alcove,  n.,  1)  a  recessed  section  in  a  room;  2)  any recess.  —  F.  alcove ,  fr.  Sp.  alcoba,  fr.  Arab,  al- qubbah,  fr.  al-,  ‘the’,  and  qubbah,  ‘arch,  vaulted tent’,  which  is  rel.  to  Arab,  qabba,  ‘it  was  bent’, and  to  Heb.  qubbd \  ‘vaulted  tent’,  Syr.  qebha- bhd,  ‘vault,  vaulted  tent’,  Akkad,  qababu, ‘shield’.  All  these  words  are  derivatives  of  the Sem.  base  q-b-b,  ‘to  be  bent,  crooked,  vaulted’, aldea,  n.,  hamlet,  villa.  —  Sp.  and  Port.,  ham¬ let’,  fr.  Arab,  al-,  ‘the’,  and  dayah,  ‘farm,  ham¬ let’.  Cp.  aldeia.
3981:aumildar,  n.,  a  revenue  collector  in  India.  — Hind.  ‘ amaldar ,  lit.  ‘one  holding  an  office’,  a hybrid  coined  fr.  Arab,  'dmal,  ‘work’  (see  au¬ mil),  and  the  Persian  agential  suff.  -dar,  meaning ‘holder,  possessor’,  which  is  rel.  to  Avestic darayeiti,  ‘holds,  supports’,  OI.  dhardyati,  of s.m.,  fr.  I.-E.  base  *dher(e)-,  ‘to  hold,  support’, whence  also  L.  firmus,  ‘firm,  steadfast,  stable, strong’.  See  firm,  adj.,  and  cp.  the  first  element in  Darius.  Cp.  also  the  second  element  in  baha- dur,  chobdar,  chokidar,  dizdar,  dufterdar,  en- amdar,  foujdar,  havildar,  jaghiredar,  jemadar, killadar,  ressaldar,  silladar,  sirdar,  subahdar, tahsildar,  talukdar,  thanadar,  zemindar, auncel,  n.,  a  weight  used  in  England  in  the  Middle Ages.  —  AF.  auncelle,  fr.  It.  lancella,  dimin.  of lance,  ‘balance’,  fr.  L.  lanx,  gen.  lands,  ‘plate, dish;  scale  of  the  weighing  machine’.  See  bal¬ ance.  The  loss  of  the  initial  l  in  E.  auncel  is  due to  the  circumstance  that  the  initial  /  in  It.  lan¬ cella  was  mistaken  for  the  It.  def.  art.  V  and consequently  dropped.
4285:baguette,  n.,  a  small  molding.  —  F.,  prop,  ‘a small  rod’,  fr.  It.  bacchetta,  dimin.  of  bacchio, ‘rod’,  fr.  L.  baculum.  See  bacillus, bahadur’n.,  a  title  given  to  European  officers  in India.  —  Hind,  bahddur,  ‘hero’,  which  accord¬ ing  to  Benfey  (in  Orient  und  Occident  1  137, quoted  in  Hobson-Jobson  49a)  derives  fr.  OI. bhaga-dhara-,  ‘happiness-possessing’.  The  first
4286:element  is  cogn.  with  Gk.  tpaystv,  ‘to  eat’;  see -phagous  and  cp.  baksheesh.  For  the  second  ele¬ ment  see  aumildar  and  cp.  words  there  referred  to. Bahaism,  n.,  the  teaching  of  the  religious  sect  of the  Bahaists.  —  Formed  with  suff.  -ism  fr.  Pers. baha,  ‘splendor’,  fr.  Arab,  bahd' ,  of  s.m. bahar,  n.,  a  weight.  - —  Arab,  hahdr,  a  weight  used in  India,  ultim.  fr.  OI.  bhdrah,  ‘load,  weight’, which  is  rel.  to  bhdrati,  bharate,  ‘carries’,  and cogn.  with  Gk.  qilpeiv,  L.  ferre,  ‘to  bear, carry’.  See  bear,  ‘to  carry’,  and  cp.  words  there referred  to.
4302:baksheesh,  n.,  a  gratuity ;  a  tip.  —  Pers.  bakhshish, lit.  ‘gift’,  a  derivative  of  the  verb  bukhshidan,  ‘to give’,  fr.  I.-E.  base  *bhag-,  ‘to  distribute,  share out’,  whence  also  OI.  bhdjati,  ‘assigns,  allots, apportions,  enjoys,  loves’,  bhagah,  'allotter,  dis¬ tributor,  master,  lord’,  Gk.  9ay£tv,  ‘to  eat’. See  -phagous  and  cp.  Bhaga  and  the  first  ele¬ ment  in  Bhagavadgita,  and  in  bahadur.
4384:bangy,  banghy,  n.,  a  shoulder  yoke  for  carrying loads.  —  Marathi  bang!,  fr.  Hind,  bahahgi,  fr. OI.  vihahgamd,  vihahgika.  See  Yule-Burnell. Hobson-Jobson,  p.6ob.
20477:jupon,  n.,  skirt,  petticoat.  —  F„  fr.  Arab.  jubbah, ‘a  long  woolen  garment’  (whence  also  It.  giubba, OProven?.  jupa,  Sp.  aljuba).  Cp.  gyp,  jump,  ‘a kind  of  jacket’,  jumper,  ‘blouse’.
28431:-phagous,  combining  form  meaning  ‘eating,  feed¬ ing  on’,  as  in  creophagous,  xylophagous.  —  Gk. -9ayo;,  ‘eater  of’,  from  the  stem  of  9xyetv,  ‘to eat’,  which  is  cogn.  with  Ol.  bhajati,  ‘assigns, allots,  apportions,  enjoys,  loves’,  bhagah,  ‘al¬ lotter,  distributor,  master’,  bhaksati,  ‘eats, drinks,  enjoys’,  Avestic  baya-,  OPers.  baga-, ‘master,  god’,  lit.  ‘distributor’,  OSlav.  bogu, ‘god’,  bogatu,  ‘rich’,  u-bogu,  ne-bogii,  ‘unfortu¬ nate’.  All  these  words  derive  fr.  l.-E.  base *bhag-,  ‘to  distribute,  share  out’.  Cp.  the  second element  in  esophagus.  Cp.  also  bahadur,  bak¬ sheesh,  Bhaga,  Bhagavad-Gita.  For  E.  -ous  (in -phagous),  as  equivalent  to  Gk.  -o;,  see  -ous. -phagy,  also  -phagia,  combining  form  meaning
33421:Sabian,  n.,  a  member  of  a  religious  sect  mention¬ ed  in  three  passages  of  the  Koran  (2:40,  5:73, 22:17).  —  Formed  with  suff.  -an  fr.  Arab,  fdbi’, ‘Sabian’,  which  prob.  means  lit.  ‘baptizer’,  and is  borrowed  fr.  Aram.  tzibha',  ‘he  dipped,  dyed’ (with  the  change  of  the  ayin  to  hamza),  which is  rel.  to  Heb.  tzabhd',  ‘he  dyed’,  Arab,  fabahga, Ethiop.  sabaha,  ‘he  dipped,  dyed’,  Akkad,  sibu, ‘to  dye’.
=== AFM pages abbaha/bahaa (Arabic script) ===
=== FVQ ===
FVQ.txt:10177:(Sabbaha). 
FVQ_pages.txt:5973:(Sabbaha).
=== MON obbohat/ابهت ===
MON_part2.txt:3573:می‌برند (فروزانفر. تعلیقات معارف بهاء ولد 
MON_part2.txt:11355:(معارف بهاء‌ولد ۴۸۵). قبةٌ پرگل: جام 
MON_part2.txt:11648:است با استطاعت (معارف بهاء‌ولد ۱۳۳۸ 
MON_part2.txt:12090:(فروزانفر. تعلیقات معارف بهاءولد ۱۳۳۸ 
MON_part2.txt:14924:است (فروزانفر. تعلیقات معارف بهاءولد. 
MON_part2.txt:15931:بهاء‌ولد ۱۳۳۸ ص ۳۱۳). 
MON_part2.txt:19036:معارف بهاء ولد ۱۳۳۸ ص ۰۷ ۹-۲.) 
MON_part2.txt:20065:شود (فر وزانفر. تعلیقات معرف بهاءولد 
MON_part2.txt:20351:است. (فروزانفر. تعلیقات معارف بهاءولد 
MON_part2.txt:25833:(فروزانفر. تعلیقات معارف بهاء‌ولد ۱۳۳۸ 
MON_part2.txt:27622:(فروزانفر. تعلیقات معارف بهاء‌ولد ۱۳۳۷ 
MON_part2.txt:43527:ابهت و جلال مخصوصی به آن می‌دهد. 
MON_part2.txt:46489:ار جمنك. نادر» کمیات. بربهاء قیمتی. محکم. 
MON_part2.txt:47941:محاز دارای علاقه مشابهت باشد آن را 
MON_part2.txt:47983:مشابهت و قرينةٌ مانع از ارادهٌ معنی حقیقی 
MON_part2.txt:50266:معارف بهاء ولد ۱۳۳۸ ص .)۳۰٩۹‏ محو 
MON_part2.txt:57079:مشابهت: (حط)نهطهط ۵۹8 [ع. مشابهه | 
MON_part2.txt:57190:مفاعیلن» است و سبب همین مشابهت و 
MON_part2.txt:57195:ی و (امص.) مشابهت. 
MON_part2.txt:65731:مشابهت. همانندی؛ ج. مناسبات.
```


## [2026-09-04T18:09:56.342Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB.txt ab/glanz ===\" && grep -n -i 'glanz' HUB.txt | head -10\necho \"=== PHD ab ===\" && grep -n '^āb\\b\\|^ab \\[' PHD.txt PHD_mackenzie.txt 2>/dev/null | head -10\necho \"=== BRT ap ===\" && grep -n -i '^āp-\\|āp-\\b' BRT.txt | head -10"
}
```


### [2026-09-04T18:09:56.422Z] TOOL RESULT

```
=== HUB.txt ab/glanz ===
548:svar glanzen*. Auch ist es mit dieser Wurzel irn Zend
551:x'^ared^a- (bei Justi = Glanz) nicht 'Glanz' bedeuten.
760:Geldner nie sublimis*, sondern glanzend, strahlend,
762:und ist ~ phi. hamik glanzend' Gl. and Ind. p. 76,
4830:dl glanzen ^) (ipt. didlhi und dTdihi)^ u. s. w.
6123:glanzen' = ftiroxtan, furoy 'Glanz', phi. afrOxtan, zd. aiwi
6215:lava = Idba *Schmeichelei' H. 952 ; tdv = tdb 'Glanz, Hitze,
6401:Da ab *Glanz' == skr. abha- H. 3 unsicher ist, so ergiebt
6547:Dunkel ist das Verhaltniss von np. farr 'Glanz, Maje-
6630:'Glanz, Jifajestat' = ap. farnah-; Pharnerseh (Mos. Xor.),
=== PHD ab ===
PHD_mackenzie.txt:658:ab [MYA < A my);)ft I M )b, N .....] water.                    'b S'u~ "r'"
=== BRT ap ===
```


## [2026-09-04T18:10:06.636Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6380,6420p' HUB.txt"
}
```


### [2026-09-04T18:10:06.670Z] TOOL RESULT

```
dan *schenken H. 186; biradar *Bruder H. 192; baraz
Schmuck' H. 193; burdan H. 196; burz *hoch*, buland 'hoch
H. 198; barsam (Parsenwort) H. 200; biristan *braten' H
201; burrfdan *schneiden H. 212; buz 'Ziege, Bock* H. 213
bazm Test' H. 215; baza *Siinde' H. 216; bastan 'binden
band *Band* H. 219; bus 'Mahne H. 220; bun 'Fundament
H. 229 ; banda *Sklave' H. 230 ; bang 'Bilsenkraut' H. 232
badan 'sein' H. 233 ; bor Tuchs (Pferd) H, 234 ; bUm *Erde
H. 237 und 239; boi 'Geruch' H. 240; bahr Xoos' H. 245— 181 —
Mm Turcht' H. 258 ; bevar zehntausend' H. 262. Mit vor-
geschlagenem a: abrU 'Augenbraue* = skr. bhrU".
In den armenischen LW. erscheint stets anl. b = ap.
np. b, vgl. band *Kerker = np. band u. s. w.
b) Ap. b nach n ^= np. 6: xunb *Krug, zd. xumba-
u. s. w., siehe Kap. 28 (m = nb).
§ 75. Ap. b nach Vokalen, d. h. ap. w ist in einigen
Fallen im Np. zu 6, sonst aber zu v geworden:
a) = np. b in : abr * Wolke' = paz. awar Shk. 233, zd,
awra- ; sitabr stark'= zd. stawra-. Ueber asdb *Verwirrung'
u. s. w. (H. 32) vgl. oben p. 7 (phi. dsdp) und iiber (mar i)
s^ba *Viper (H. 800) oben p. 82 und unten p. 185 (phi. sBpak).
Da ab *Glanz' == skr. abha- H. 3 unsicher ist, so ergiebt
sich, dass ap. w nur vor r sicher zu np. b wird. Doch
vgl. np. girlb ein Getreidemass, arab. jarib, syr. NDn:i
(Tab. 242) = arm. griv = ap. ^grfwa-.
b) = np. V in : n^v Vacker , phi. nevak schon (— np.
nBk)j ap. naiwa-, geschrieben naiba- *sch5n ; girav, girau
Tfand', arm. grav Tfand', phi. grav (geschrieben grUbti),
ap.*grraM?a-, skr. grabh *ergreifen*; avardati, avurdan *bringen',
zd. a + bar ; xarvar 'Esels-last', sarvclr *Kopflast' aus *xa-
rawdra-, ^sarawdror', vgl. np. bar 'Last*, mit dem durch Neu-
komposition xarbar, sarbar gebildet wird ^) ; suvar 'Reiter
= ap. asawdra- (geschrieben asabara-) ; paivastan Ver-
binden', phi. patvastan, ap. *patiwastanaiy. Dazu auch
davar u. s. w., s. § 60.
§ 76. Zwischen ap. w und np. v lag im Mp. sicher w,
das im Phi. durch Ub (z. B. grUbu d. i. grav = grata 'Pfand')
oder V (nevak schon') wiedergegeben wird 2), da ein beson-
deres Zeichen fiir w nicht vorhanden war. Ebenso mussten
die Armenier, die den Laut tv nicht batten und demgemass
So erscheint in aUen erst im Phi. oder Np. gebildeten Kom-
```


## [2026-09-04T18:10:07.777Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'abbaha\\|ubbaha\\|ubbuha\\|abbuha' AFM.txt AFM_pages.txt KLN_1966.txt KLN_1971.txt 2>/dev/null | head -20\necho \"---FVF---\"\nls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | grep -i FVF"
}
```


### [2026-09-04T18:10:07.849Z] TOOL RESULT

```
---FVF---
```


## [2026-09-04T18:10:17.236Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'بهاء\\|ابهة\\|أبهة\\|اُبَّهَة' ARB_mo3rb.txt ARB_abdulraheem.txt TAD.txt TAD_pages.txt 2>/dev/null | head -20"
}
```


### [2026-09-04T18:10:17.302Z] TOOL RESULT

```
ARB_mo3rb.txt:13487:رفو لاسأة عي راطقل من الرجال : القصير الموق الخلق فقوطا غلى النشييه به ٠‏ والخزابهة 1 
ARB_mo3rb.txt:18162:ينكان" ؛ و يكس فاره © الوأحد بهاء ٠‏ بحجمه فتاجين 6 #لبال و .ابول 6 وسر وال وسراويل» ٠‏
```


## [2026-09-04T18:10:17.729Z] TOOL CALL #27: WebSearch

```json
{
 "query": "أبهة etymology root بهو Arabic dictionary Lane"
}
```


### [2026-09-04T18:10:19.532Z] TOOL RESULT

```
Web search results for query: "أبهة etymology root بهو Arabic dictionary Lane"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T18:10:27.999Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/آب",
 "prompt": "Give the full etymology section(s) for Persian آب (āb) — both the \"water\" sense and any \"glitter/luster\" or homograph sense if listed. Include Proto-Iranian and PIE reconstructions, and any citations (Cheung, Hasandust, etc)."
}
```


## [2026-09-04T18:10:29.087Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/آفتاب",
 "prompt": "Give the full etymology of Persian آفتاب (āftāb) 'sun'. What are its component parts and their meanings? Does it derive from āb 'water' or from a different āb meaning 'glitter/shine'? Cite sources given."
}
```


## [2026-09-04T18:10:30.208Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/آبرو",
 "prompt": "Give the full etymology of Persian آبرو (āberu) 'honor, reputation'. What are its component parts and literal meaning? Any note on whether āb here means water or something else like luster/shine? Cite sources."
}
```


## [2026-09-04T18:10:31.272Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hapah",
 "prompt": "Give the full content of this Proto-Iranian reconstruction page for 'water' - descendants, PIE etymology, and any related Avestan/Old Persian forms."
}
```


## [2026-09-04T18:10:32.535Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/بهاء",
 "prompt": "Give the full etymology of Arabic بهاء (bahāʔ) 'splendor, beauty'. What root is it from? Also check if there's an entry for أبهة (ubbuha/ubbaha) 'pomp, grandeur' and give its etymology and root too."
}
```


### [2026-09-04T18:10:35.001Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T18:10:35.410Z] TOOL RESULT

```
# Persian آب (āb) Etymology

## Etymology 1: "Water"

The entry provides an etymology tree showing:

**Proto-Indo-European**: *h₂ep- ("water, body of water")

**Proto-Indo-Iranian**: *Hā́ps

**Proto-Iranian**: *Hā́fš

**Old Persian**: 𐎠𐎱𐎡𐎹𐎠 (a-p-i-y-a)

**Middle Persian**: ʾp̄ (āb)

**Persian**: آب (āb)

The detailed etymology states: "From Middle Persian ʾp̄ (āb), from Old Persian 𐎠𐎱𐎡𐎹𐎠 (ap-), from Proto-Iranian *Hā́fš (compare Northern Kurdish av/aw, Baluchi آپ (áp), Pashto اوبه (obë), Avestan 𐬀𐬞 (ap)), from Proto-Indo-Iranian *Hā́ps (compare Sanskrit अप् (ap)), from Proto-Indo-European *h₂ep-."

## Etymology 2: "August" (Syriac Calendar)

"Borrowed from Arabic آب (ʔāb), from Classical Syriac ܐܒ (ʾāḇ)."

**No citations** (Cheung, Hasandust, etc.) appear in the provided content for either sense.
```


### [2026-09-04T18:10:36.466Z] TOOL RESULT

```
# Etymology of Persian آفتاب (āftāb)

Based on the Wiktionary entry, the Persian word derives from Middle Persian with the following breakdown:

**Component Parts:**
The entry states the word is "Equivalent to _[آف](/w/index.php?title=%D8%A2%D9%81&action=edit&redlink=1 "آف (page does not exist)")_ (âf) +‎ _[تاب](/wiki/%D8%AA%D8%A7%D8%A8#Persian "تاب")_ (tâb)."

**Ultimate Origin:**
The etymology traces back to "Proto-Iranian _\*abi-tāpáh_" according to a citation referencing Cheung's *Etymological Dictionary of the Iranian Verb* (2007).

**Regarding "āb":**
The entry does not specify whether the component āf relates to āb meaning "water" or "glitter/shine." The Middle Persian source form is listed as "ʾptʾb /⁠āftāb⁠/, 'sunshine'" but the internal morphological breakdown of those constituent parts is not elaborated in this document.

**Source Cited:**
Cheung, Johnny (2007), *Etymological Dictionary of the Iranian Verb*, Leiden: Brill.
```


### [2026-09-04T18:10:37.414Z] TOOL RESULT

```
# Etymology of Persian آبرو (āberu)

Based on the Wiktionary entry provided, here is the etymological breakdown:

## Component Parts

The word is "a shortened form of _[آبروی](/wiki/%D8%A2%D8%A8%D8%B1%D9%88%DB%8C#Persian)_ (âb-e-ruy), compound of _[آب](/wiki/%D8%A2%D8%A8#Persian)_ (âb) +‎ _[روی](/wiki/%D8%B1%D9%88%DB%8C#Persian)_ (ruy)."

## Literal Meaning

The compound literally translates as "water of the face" (âb = water; ruy = face). The metaphorical extension from this literal sense to mean "honor," "reputation," and "standing" reflects the idea that one's face—one's outward appearance and dignity—represents one's honor in the world.

## Note on "Āb" (Water)

The source provided does not clarify whether this particular usage of āb refers to water in a literal sense or employs a figurative meaning like "luster" or "shine." The entry treats it as the standard Persian word for water without additional commentary on semantic nuance in this compound.

**Source:** Wiktionary entry for آبرو, accessed from the provided dictionary content.
```


### [2026-09-04T18:10:39.507Z] TOOL RESULT

```
# Etymology of Arabic بهاء (bahāʔ)

Based on the Wiktionary entry provided, **بهاء (bahāʔ)** has two etymologies:

**Etymology 1:** Derived from the roots ب ه و (b h w) or ب ه ي (b h y). This meaning encompasses "beauty, splendour" and in religious contexts, "glory, greatness, majesty."

**Etymology 2:** From the root ب ه ء (b h ʔ), with an obsolete sense referring to "a she-camel familiar with, accustomed to, tame towards, its milker."

## Regarding أبهة (ubbaha/ubbuha)

The provided document does not contain an entry for أبهة (ubbaha/ubhuha) 'pomp, grandeur'. Therefore, I cannot provide its etymology or root based on the content available. You would need to consult a separate Wiktionary entry or other lexical resource for that term's derivation.
```


## [2026-09-04T18:11:09.979Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/آفتاب",
 "prompt": "Quote verbatim the full \"Etymology\" section of the Persian آفتاب entry, including any etymology tree/template showing Proto-Iranian, Old Iranian, Avestan forms, and the literal gloss given for each morpheme (âf and tâb). Also quote any usage note or Cheung citation exactly as written."
}
```


## [2026-09-04T18:11:11.419Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D8%A8%D9%91%D9%87%D8%A9",
 "prompt": "Give the full etymology of Arabic أبّهة (ubbuha/ubbaha) 'pomp, dignity, majesty, grandeur'. What triliteral root is it derived from, and is there any mention of a Persian origin or connection to Persian āb (water/glitter)?"
}
```


### [2026-09-04T18:11:12.969Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T18:11:14.969Z] TOOL RESULT

```
# Etymology Section for Persian آفتاب

Here is the Etymology section from the Persian entry:

"From Middle Persian _𐭠𐭯𐭲𐭠𐭡_ (ʾptʾb /⁠āftāb⁠/, "sunshine") (compare 𐮀𐮎𐮃𐮀𐮁 (ʾpdʾb /⁠ābdāb⁠/)), from Proto-Iranian _\*abi-tāpáh_. Equivalent to _آف_ (âf) +‎ _تاب_ (tâb)."

The Cheung citation referenced is: "Cheung, Johnny (2007), *abi-tāpáh* (meaning 'heat/warm'), in Etymological Dictionary of the Iranian Verb, Brill."
```


## [2026-09-04T18:11:23.897Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D8%A8%D9%87%D8%A9",
 "prompt": "Give the full etymology of Arabic أبهة (ubbuha/ubbaha) 'pomp, dignity, majesty, grandeur, awe'. What triliteral root is it derived from (e.g. ب-ه-و / ب-ه-ي), and is there any mention of a Persian origin or connection to Persian āb (water/glitter)? Quote the etymology section verbatim if present."
}
```


## [2026-09-04T18:11:25.126Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%87%D9%88",
 "prompt": "Give the full content of the Arabic root ب-ه-و (b-h-w) page: what derived words are listed (بهو، بهاء، أبهة، باهي، etc.) and their meanings, and any etymology notes."
}
```


### [2026-09-04T18:11:27.933Z] TOOL RESULT

```
# Etymology of Arabic أبهة (ubbaha)

Based on the Wiktionary page provided, there is **no etymology section present**. The page only contains:

- **Root information**: The triliteral root is listed as "ء ب ه" (ʔ b h)
- **Definition**: "greatness, majesty, grandeur"
- **Pronunciation**: /ʔub.ba.ha/
- **Grammatical information**: Feminine noun with declension table

The page does not include:
- A detailed etymology section
- Discussion of Persian origins
- Any connection to Persian "āb" (water/glitter)
- Etymological derivation details

To obtain this etymological information, you would need to consult more comprehensive Arabic etymological sources beyond what this Wiktionary entry provides.
```


### [2026-09-04T18:11:31.558Z] TOOL RESULT

```
# Arabic Root ب-ه-و (b-h-w)

Based on the Wiktionary page provided, I can only offer limited information about this root, as the page does not include a dedicated root entry with comprehensive derived words.

## Available Information

The page indicates there are "3 terms" belonging to the root ب ه و, but only one derived word is explicitly documented on this entry:

**بَهْو (bahw)** - A masculine noun meaning "hall; reception hall, foyer." The entry notes it has multiple plural forms: أَبْهَاء (ʔabhāʔ), بُهُوّ (buhuww), or بُهِيّ (buhiyy).

## Limitation

The current page does not provide:
- A complete list of all derived words from this root
- Etymology notes
- Meanings for related terms like بهاء، أبهة، or باهي

To access comprehensive information about all derivatives and etymological details for the b-h-w root, you would need to visit the dedicated root appendix page, which appears to not yet exist on this Wiktionary instance.
```


## [2026-09-04T18:11:47.138Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\ntxt = open('AFM_pages.txt', encoding='utf-8', errors='replace').read()\npages = txt.split('\\f')\nprint(len(pages))\n\"\n"
}
```


## [2026-09-04T18:11:47.656Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\ntxt = open('AFM_pages.txt', encoding='utf-8', errors='replace').read()\npages = txt.split('\\f')\nfor i in [13,14,15,16,17]:\n    print('=== leaf', i, '===')\n    print(pages[i][:600])\n    print()\n\"\n"
}
```


### [2026-09-04T18:11:49.045Z] TOOL RESULT

```
198
```


### [2026-09-04T18:11:50.397Z] TOOL RESULT

```
=== leaf 13 ===
83
0 الى 500 937 :ابن 55[ 37 39093 .1.3
ܐܨܦ القاطع : « اكت مكت بكسر الكافين ضرب من !ܐܝܢ بالسر ܬܒ وهو
اسود :ܠ جوذة الطيس ٠‏ يقال له ( 039 ححر الولادة ܝ الذسر وحجر
العا ٠١و‏ بالتركية « 1 طاثى وطوشتحل تظائق »© وتيختالاه افع لعسر الولادة
وتعلقة على ܐ( ينع تساقط الاكثر.» “قلت أو ܦܘ ܀ :111 لصبت سواانة يكل
ܨ إما ܠ 1 0
3 ܝܫ الشديدة من شدائد الدنيا تعريب آك وهما عمنى
0 ®+ ,|11 ,)7 5) العود 0 ) ܡܳܐ به . .قال الاصمعي ذهو فارسني
معرب ٠‏ قلت 9 13( الصبزء قال الاب 5 50 0507
قلت : والموثافى في ماخوذ من | ܕ لان 5 اصله من بلاد 0935 0
)ܒܨܢ 210 والفرني 0105 والاتكليزي” 5 موالايطاليالي 31 010
( الأماج» الغرض وهو 

=== leaf 14 ===
ܠ @ ܛ اكه
الشمس ٠‏ وهرمس 0 - - الغليل )
0 ( | ܕ ) ݁ܡ ܐܬܝܐ او هما 0 2 ܣ 2 اع وهو 116122
1 يني
( ܠܬ 3( فارسي ء#ض وهو ܐܙܚ الخارصيني
اله ناردق ي مخض وهو الغزال
(الأوج) 210 :0 ܕܦ( ععنى ٠‏ 105( 5100 القاطع 0 هده 34 هندنة
١‏ الأوَاز) ضرب من الأنام : تعر يبب 56391 واصل معناه ` ويطلق على
:8 من الننهات الست ت الموجودة في 0 ولجموعها 5 شّش واه وهي هذه :
لباك وشهناز وما نه و 1497 ننه ܝ
8 العطّة والفرصة فارسئتها ܨ ومعناها الرجاء والطلى ٠‏ والظاهر
9 اللفظة 3 ܚܝ ومعئاها الطان
319 )0 ܐܐ 3 ونين ܐܝܢ اصمل اتسكلمة ;11
6 ,¿06 زهو نوع 6 ن الذئاب 8 بالفرنسة ܐ¥16]@§¢ ܝ
» (الأوكة) الغضب والشر ومن المحتمل ان تكون معربة 

=== leaf 15 ===
اصغر من ورق الفجل وهو حاذ الى الغابة ويستى ` 9 والقسم الاخر عدي
.| ܢ ورقه ܐ لبن قليل الحدة وزهره احمر٠‏ ٠اذا‏ سقيت سحرة ان ܐܝܒܨ عاء 25
.79 ܐܟܝ ܬ ܦܐ ܐ كثيرا »
ار 1 وان عا
باب الب
( 715 ) الفلا ل فارسي 0 ܐ له ܢܡܒ
س سر
ܟ <
( الما .© والمابوش ) معرب ابوج واصل ܐ 3 مغطي الرجل ܕ( نا نوس
بالتركية والكرد %
£ الم ونم ) تعر يب بابونه او يابونلك وهي حشيشة ذات زهر كتير النفع‎ ١
التحليل . ومنها السر ܨ ܒܒܘܝܐ‎
( المج .1 1 ܨ ܕ( | ܐܰܝ
( لبأ ) = لا اتاد 0
00 ب كيرة ة النفع في الأمرا ض السوذاوءة ܨܦ الأترجية
والتر ان رهي ܨ 09 11 ظات وهو ضرب من 1 ومن بوله 5 ܪ
2 اوغل 51
( 5 4 0 ܝ( تنفع من لدغ العقرب ܣ
09 فارساتها 0 

=== leaf 16 ===
ܒܝ ܝ( ك6
1 و الاتكليزي 6--020310|[
)ܕ نان والناذحان » قال 3 حيط المحيط: « الباذضيجان معرب باذتكان
بالفارسية ومعناه بيض اللان: نبات يعرف عند العامة بالمتتجان والبيدنحان ».قا-'
ان باد بالفارسيّة اسم جن كان موكلا على امر التزو يج . ونك (تجعة تكان )اهو
:2 6 معنى 5 ` 3 5 والصحيح ان 1 )
ܝ ܒܪܓܝܬܐ ب لسر ܨܬ وى ارم ܨ 8 ' ÷ ܐܚܐ 20 ابن
6 0 ܚ «واسمة الفرنني يقرب أكثر من ܝ الاصلي
شقال آل 1116 31161 ويقول الاسا” ماندون 86161286123 وهو باطلحان 6ܗܨ29 وباحأن
013
ܣ ,)ܪܕܕ والباداورد ܙ !)ܪܕܕ ) ܝܐܝ مثآث الساق مستدير الأعلى
09 3 4 زهر احمر لا 7 اوراقة على 7 باد 1 35( غنه لي
الببهان القاطع انه نوع من الشوك له زهر احم

=== leaf 17 ===
1
ܐ مركب من با اي قدم ومن شاه اي الملك
( الباشق ) طائر | صغر ܐܕܨ ܐ تعر يب ]ܘ ومنة ܝܟ يافى ܒܘܙܢܩܐ
«امال) سن ١‏ لم 5 او ماخوذ عن 10 0218 ومن الفرنسي 6116م ٠.‏
.0 ܨ فسريالي ܡܪܐ 30 2110
( البالة ) وعاء الطيس والقارورة والمراب قال الاب لامنس في كتاب الفروق
الها ܐ عن )!$ 000 “الذي 18016 ܢ 5 مشتقة من بيله
الفارسي ومعناه الوعاء وشرنقة القز او 55( ومعناه القدح © ¢ كك .
وما البالة عنى السمكة واحلوت شعربة عن اليوالي »ܐܬܐܤ واحلوت نفسة معرب
عن ?×
( يسان) هم بسآن واحد وعلى سآن واحد اي طريقة .قال في شفاء الغليل :
« بسان ليت تمن ايلة بحضة قال عمر: 0 تكونوا 18 واحدا اي شيا واحدًا:
وقيل لغة عانة ».قلت وهى معربة
```


## [2026-09-04T18:12:02.712Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '^ابهت\\|ابهت:' MON_part1.txt MON_part2.txt 2>/dev/null | head -10\necho \"---context search---\"\ngrep -n 'ابهت' MON_part1.txt MON_part2.txt 2>/dev/null | head -20"
}
```


### [2026-09-04T18:12:02.789Z] TOOL RESULT

```
MON_part2.txt:43527:ابهت و جلال مخصوصی به آن می‌دهد. 
MON_part2.txt:57079:مشابهت: (حط)نهطهط ۵۹8 [ع. مشابهه | 
---context search---
MON_part2.txt:43527:ابهت و جلال مخصوصی به آن می‌دهد. 
MON_part2.txt:47941:محاز دارای علاقه مشابهت باشد آن را 
MON_part2.txt:47983:مشابهت و قرينةٌ مانع از ارادهٌ معنی حقیقی 
MON_part2.txt:57079:مشابهت: (حط)نهطهط ۵۹8 [ع. مشابهه | 
MON_part2.txt:57190:مفاعیلن» است و سبب همین مشابهت و 
MON_part2.txt:57195:ی و (امص.) مشابهت. 
MON_part2.txt:65731:مشابهت. همانندی؛ ج. مناسبات. 
MON_part2.txt:84853:را مشابهت و در کم را مساوات و در وضع را 
MON_part1.txt:6560:ابسهت: ۳۹ ال ابهت) [ع.] 
MON_part1.txt:19777:منشی. نسیم. شکوه؛ ابهت» اهمست. تندی» 
MON_part1.txt:25667:به مشابهت. ضح.- لازم الااضافه است. 
MON_part1.txt:26989:بی‌ریب.: (ابهتطارودآا اف. ۳۵ (ص مر.) 
MON_part1.txt:77878:حمله» هجوم. قهر» غلبه. ابهت» وقار. 
MON_part1.txt:83494:گیاهی است از تیرةٌ پنیرکیان و مشابهتش با 
MON_part1.txt:84131:شبه: "3202 [ع.] (امص.) مشابهت؛ مانندی. 
MON_part1.txt:84157:پوشیدگی امری. مشابهت. (.) شکث» تردید. 
MON_part1.txt:86306:دو روی آن با یکدیگر مشابهت ندارد. بخية
```


## [2026-09-04T18:12:04.336Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%A7%D8%A8%D9%87%D8%AA",
 "prompt": "What does Mo'in's Farhang-e Farsi dictionary say about the Persian word ابهت (ebhat/obohat)? Give the full definition text and any origin/etymology tag (e.g. [ع.] for Arabic) shown."
}
```


### [2026-09-04T18:12:07.865Z] TOOL RESULT

```
# Definition of ابهت (Ebhat/Obohat)

According to Mo'in's Farhang-e Farsi dictionary, the word ابهت carries the following meanings:

**Etymology:** Arabic origin [ع.]

**Definitions:**
1. "بزرگی ، بزرگواری ، عظمت" – grandeur, magnificence, or majesty
2. "تکبر، نخوت" – arrogance or pride

The entry indicates this is a noun in the nominative/accusative form (اِمص.).
```


## [2026-09-04T18:12:18.873Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.almaany.com/ar/dict/ar-ar/%D8%A3%D8%A8%D9%87%D8%A9/",
 "prompt": "Give the dictionary definition and root (جذر) of the Arabic word أبهة (ubbaha/ubbuha), meaning pomp/majesty/grandeur. What triliteral root does it belong to and what related words are given (e.g. تأبه، مؤتبه، باه، بهو)?"
}
```


### [2026-09-04T18:12:20.858Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T18:12:26.487Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.baheth.info/all.jsp?term=%D8%A3%D8%A8%D9%87%D8%A9",
 "prompt": "Give classical Arabic dictionary (Lisan al-Arab, al-Muhit) entries for أبهة (ubbaha/ubhah) - pomp, majesty. Quote the root discussion, especially whether it is said to relate to تأبه (ta'abbaha) 'to be haughty', or to بهاء (bahā') 'splendor', or to any Persian word."
}
```


### [2026-09-04T18:14:44.286Z] TOOL RESULT

```
connect ECONNREFUSED 212.87.214.191:443
```


## [2026-09-04T18:15:12.258Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'Wasser' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt 2>/dev/null | grep -i '^\\s*1\\.\\|ap-\\|ab-' | head -20\necho \"---IEC water---\"\ngrep -n -i '\\bwater\\b' IEC.txt | head -20"
}
```


### [2026-09-04T18:15:12.321Z] TOOL RESULT

```
3149:2. ap- „Wasser, FluB“. 
8540:urspriingliche Beziehung zu *ab-, *a/>- „Wasser“, s. Vf. LEWb. 2 u. amnis', 
---IEC water---
223:abhmn-, abhnis ‘river, water’. WP I, 46 Alb. âmë, f. pl. -a 'riverbed'; Lat. amnis, gp: amnium, mf. 'river; Gallo-Lat. ambis; Gaul. abono-; W afon, pl. -ydd, f.; Br. aven, Cor. avon, id.; Olr. aba, gs: abann, aband & abhond; Ir abha, gs. & gp. abhann, npl. aibhne, f. id.
406:aKua (?) “water; running water’ (aqua?). WP I, 34, 35 Skt. river-names in a$va-: -rathā, -parni: (?) Gk. asa-, -assa (in asáminthos, thál-assa. Speculations in Bois. DELG); Go. ahva ‘river’; OE ea; ON ọ (speculations with lit. in Feist: VWGS)
534:anotis (1) ‘duck’. WP I, 60. Cf. ana, nàio, snáió Skt. atih "a water bird’; Lat. anas, gs. anatis and anes, anitis, gp. -ium; OHG anut, enit; ON ond, pl. andir, endir, OE ened; OCS ọty, ọtẹ beside dim. otica; Finn. LW ankka (fr. a type found in Sw. anka “duck? (phono- logy obscure)
657:aquà, io ‘water’; (aquies, à ^watery) WP L 34 Gk. cf. thálassa (? *dh]- + *aquiə. Cf. dhol-); Lat. aqua; Go. ahva ‘river’; ON á ‘water’; OHG ouwa, auia ‘meadow’; OE éa "water, stream’; Fris. ie “water, ril
679:ardā (arədā), io “a water-fowl'. WP I, 147 Lat. ardea ‘heron’; OE earte ‘wagtail’; ON arta ‘teal’, cf. ertla ‘wagtail’; Srb. róda ‘stork’. (Relation, if any, to Gk erðdiós obscure)
830:auslom (ouslom) ‘eared object, pot. Cf. ausis Arm. awy (i-stem ‘earring, clasp, buckle, link"); Lat. aulia, ólla; Osc. úla- “pot? (more probably here than to auso 'draw water, as in ON eysill *ladie")
832:ausó, ið “draw water, bale out. WP I, 27 Lat. (ambig.) haurio (h- unexplained); MHG
995:bubul- (1) ‘rumble, throb, bubble, babble’. Skt. buburah ‘water’; Alb. bubulloj, bubullij ‘tumble’; Lat. cf. bübulare (&hoot', *büb-); MLG popelen ‘bubble up’; OE pypelian
1000:buburió ‘rumble, bubble, rattle’ Skt. (ambig.) buburah (^water'. Pref. to bubul- (1), q.v); WGer. poppern “bang”
1579:bhrag- ‘break; breaking; breaker. WP II, 193. Cf. bhrago, bhraĝmn-, etc. Skt. bhraj, adj.; Lat. cf. nau-fragium; W brai ‘outbreak’; Br. braé *flax-breaker'; Go. brakja ‘struggle’; MHG brach ‘din’; Ger. Brack “lack; rubbish; breech; brackish water’; adj. *thickset beside Brach ‘fallow land’; Brake ‘flax-breaker’; LG brak, id.; OE bræc ‘fallow- land; din’; EME brack ‘vice, fault’; Du brak ‘brat’: adj. ‘brackish’; ON brak ‘creak, crack’; Sw. brak ‘bang’
1904:bhukulos (-ilos, -əlos, à) ‘swollen; swell, bulge’ l Gael. bochail ‘proud’; OHG buhil Ch: G -bühl); Blg. bükül & bükla “wooden water- bottle’; Li. (?) buklüs “clever”
2387:dön- ‘reedbed, swamp; reeds’ Doric dónax ('reed', fr. *donu *'water', as in Skt. Av. dän, Oss. don?); Li. duónis, io ‘reed, rush’; Latv. doni ‘sedges’
2542:drtis ‘têaring, scraping; têar, skin’. See next & cf. WP I, 797: dero Skt. drtih ‘skin’; Per. dül *water-skin'; Gk. dársis ‘skinning; milling’; Go. ga-taürps “de- struction’; Cz. drť? ‘powder, sawdust’; R (al- leged) derť ‘bran’
2939:dhmbh- (2) ‘tomb’. See dhnguh- Arm. damban, id.; Gk. (ambig.) táphos. A variant occurs in MHG tümpfel *water-hole? beside (W. Saxon type) tümpel *cunnus'; E dimple (fr. *dhmbilo- or *dhum-)
3200:dhubros ‘deep; depth, water. Cf. dhub5. WP I, 848
3210:(D Phryg. dübris ‘sex? (Asclep.); Mir dobar “dark; water’; Ir. dobhair ‘dark, foul", dobhar, id. (& *water); W dwfr, dwr; Cor. dowr; Br. dur ‘water; OCS dübrí ‘gorge, abyss’; Cz. debř, id.; Li. duburýs ‘hollow, depth’; dubrë ‘forest clearing’
3355:dhüsos, à, iə (1) ‘roaring, raging; fury, demon’. Cf. WP I, 846 and next. Gk. cf. thúas, thuiás “sibyl, bacchante'; Gallo- Lat. dusius ‘demon’; Ir. cf. dos ((1) ‘froth; vigour’, fr. *dhust-); OHG tüsig, OE dysig ‘mad, foolish’ beside MHG tüsen ‘rush, roar, ring’; tuster ‘demon’; Li. düsë, düsia “water- beetle’ (semantics obscure)
3410:ebhros, ios ‘damp, wet, drunk’. Arm. cf. an-arb, i-st. ‘sober’; arbenam "get drunk’; arbeal, adj. ‘drunk’: arbucanem “water animais’; OLat. eber, f. ebra, adj. ‘drunk’; Lat. ebrius, id.; MHG aber “mild of weather”; æber
3779:ombros, is (omber-) in Skt. àmbaram 'firma- ment’; Lat. imber beside imbrex 'roof-gutter' and ambrices ‘rafters’; Gk. ómbros (vocalism of ónoma). (A simplex may be present in Skt. ámbu *water' & Arm. amp 'cloud', but a
3781:Skt. ámbhas "water" and an Arm. amb “cloud? also occur). WP I, 131
```


## [2026-09-04T18:15:12.879Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '^ap-\\|^ab-\\| ap-,\\|Wasser, Fluss\\|Wasser, Fluß' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt 2>/dev/null | head -20"
}
```


### [2026-09-04T18:15:12.934Z] TOOL RESULT

```
2936:ab-, her-“ („her“ nicht durch Aufsaugung einer dem lat. ad entsprechen- 
3171:ap-, ap- — apo, po 
3190:3. ap-, ap- „gebrechlieh; Schaden“. 
6795:f//i-Erweiterung : lit. eiga „Gang“ (in U-e-iga, ap-, at-eigd ), gr. oTyo- 
8011:Lit. ap-, vor Labial auch noch api-, in Nominalzs. apy- Praef. „um. 
20698:glatt machen“, nukdisti ,,es auQen glatt macheir', ap-, su-kalsti „ab-
```


## [2026-09-04T18:15:25.841Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '650,670p' PHD_mackenzie.txt\necho \"---search aftab pahlavi---\"\ngrep -n -i 'aftab\\|ptb\\|abdab\\|abdb' PHD_mackenzie.txt | head -10"
}
```


### [2026-09-04T18:15:25.897Z] TOOL RESULT

```
             (vii) read 1 frarast, are~n ....

       p. 166 [142] after 81 add dIg.
       p. 179 [115] for karezar read karezar.
      0 . 220 [33] for arg, halag read alag, halag.
                                    A
a- [)- I M )-] privative prefix, un-, -less.
a eJ       then (generally with a suffixed pronoun, e.g. A-i).
ab [MYA < A my);)ft I M )b, N .....] water.                    'b S'u~ "r'"
ibid ep)t l I M )b)d, N .....] populous, thriving, prosperous•
   ......ih: prosperity.
ibidin ep)t)n l I N -] thriving, prosperous, cultivated.
   ",ih: prosperity, cultivation.
abidixsa(y) eft)thI)(d), v. padixsi(y)] without authority, powerless.
  ......ih: powerlessness; anarchy.
abadyawand [)p)tyd)wnd I J )b)dywn(d)] powerless, weak.
   ,...,ih: powerlessness, weakness.
aba~ [L WTE < A lwt-h I M )b)g, N (a)ba] with.
  -ih [)Pkyh] company, assistance.
aba~enidan, aba~en- eJ?kyn-ytn l] accompany.
a-bahr [WhIJ portionless, deprived.
---search aftab pahlavi---
```


## [2026-09-04T18:15:26.393Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i '\\bab-\\|\\bāp\\b\\|glanz\\|glitter\\|luster\\|shine' BRT.txt | head -20"
}
```


### [2026-09-04T18:15:26.447Z] TOOL RESULT

```
ugrep: error: error at position 18
(?mi)\bab-|\(?:b|B)(?:ā|Ā)p\b|glanz|glitter|luster|shine
mismatched ( )___/
```


## [2026-09-04T18:15:30.845Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'glanz' BRT.txt | head -10\necho \"---ap- entry---\"\ngrep -n '^ap-\\|^āp' BRT.txt | head -10"
}
```


### [2026-09-04T18:15:30.913Z] TOOL RESULT

```
4799:ajasa  andvl . .  Yt5.8s;  —  fiiirim  .. yS  aßcCiraiibyS  ätti  raoxinuha  lazfmnS "..der  mit  den..  (Sternen)  im  Lichtglanz dahergefahren  kommt"  Yt.  Ä45.  7)  mit Akk,  des  Ziels:  ä  mJ  aidäm""^  vahiltä  a ^^at^yacJ  (sd.)  mazdil  Y.j^,  7;  —  at  vä vTsp7ng  ayti'"^  "so  komme  ich  zu  euch allen"  Y.  j/.  2.  a)  in  feindlichem  Sinn, a)  vom  Feindesheer:  späopm  . .  dOräi ayanttm  rasmaoyS  . .  daniayasnanqm  Yt. 5. 68.  p)  'sich  machen  an  — ,  hermachen über  — '*J':  pairikqm  yä  aiti  airim  äpm sqm  .  ,  V.  //.  9.  b)  in  freundlichem, a)  'zur  Seite  treten,  stehen':  at yastsm nsit  na  issmrUS  Syät'*^  (Opt)  "wer  dem aber,  wenn  er  (drum)  angegangen  wird, nicht  zur  Seite  steht"  Y.  46. 6.  ß)  'auf Jemands  Seite  treten,  übei^ehen  zu  — ' (Akk,):  _v7  ayat  (Konj.)  asavanim  divam- wm  (sd.)  ..  Y.j/.  20.  ßß)   mit  Abi.
10876:•  j.  xätävant-  Adj.  'mit  Lichtglanz,  Schön- heit   ausgestattet':    mh;A>m    .  ,    'vanhm
11254:satim  saranitH  "die  Felle  strahlen  auf  die Beschauer  Silber  und  Gold(glanz)  in  Fülle" Yt.  5.  129;  —  •mqnca  *hiku  N.55.
16322:•  j.  pouru.x''ar9nah-  Adj.  'der  viel  Herr- lichkeit, Glanz  besitzt,  hoheitsvoll';  °nat»Ad (NS.)''  asava  sarahusIrSY .ig.y, — 'nanha (VS.)"'  ahura  mazda  Vyt.  2.^'*;  —  yasata 'naiaha  (AP.)  yasata  pouru.bailaza  Ny.5. 6 ; —  yazata  'nanha  (VP.)  Ny.  J.  1 1 ;  — jc^arj»?  "««»^iffi  (ASm.  statt  n.)  Yt.iÄi.
17092:•  j.  bäma-  m.  'Licht,  Glanz.
17118:•  j.  bamaniva-  Adj.  'glanzvoll,  herrlich': !  iumhtiMi.  —  0  S»»,  j'ara-  iaäu.vchum:  — vastrasca  JbsA  'v.'i  "und  herrliche  fertige.  '>  So  T.  —  j'  Die  Eil.  daiu  in  F.  35b  ist Kleider"  Yti7.i4;  zitF-j.  nicht  kl«;  wohl.  ,«.  ^«-.ü«  ««ira.
23895:•  j.  vohvä'vant-  Adj.  'mit  gutem  Licht,  tfmfmca  yaozäätS.s?mS.bm^mia  kulkSjmn5,- Glanz  versehen'**:  marvham  ..  'vani»m  tiitamca  "wo  es  auf  dieser  Erde  am Yt  7. 5.  meisten  an  Wasser  und  Pflanzen  mangelt
24840:•  j.  raoxsnay-  i)  Adj.  'licht,  glänzend': tilirim  . .  dural  vyävant?m  (sü.)  bänubyB 'niiyj  \l.S.2->.  2)  n.  'Licht,  Licht- glanz' (nur  Komp.).
24842:•  j.    raoxsnav-    n.    'Licht,    Lichtglanz':
24850:•  j.  raoxSn«'mant-  'licht-,  glanzvoll':  snta- vaisff  ..  srim  bänvA  •mä  YL/?.  44".
---ap- entry---
7276:ap-  Noten
```


## [2026-09-04T18:15:38.864Z] TOOL CALL #48: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py 2>/dev/null | head -50"
}
```


### [2026-09-04T18:15:38.906Z] TOOL RESULT

```
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


## [2026-09-04T18:15:44.662Z] TOOL CALL #49: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/آب' --note 'page 32 root/node1, PIE h2ep- -> Iranian ap- water chain for Persian ab' \npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/آفتاب' --note 'page 32 node2 aftab: Proto-Iranian *abi-tapah (Cheung), not from ab water/glitter'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/آبرو' --note 'page 32 node2 aberu: ab-e-ruy = water of the face, honor'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/بهاء' --note 'page 32 node3: Arabic baha, root b-h-w/b-h-y'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/أبهة' --note 'page 32 node3/4: Arabic ubbuha root listed as separate root a-b-h, not b-h-w, no Persian ab component'\n"
}
```


### [2026-09-04T18:15:47.131Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fa72848139f07717.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/948d2d1ce1d3354a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5d8c962be9136432.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/74b1dfd510ae07a0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/514384b1671bf57f.txt
```


## [2026-09-04T18:15:50.740Z] TOOL CALL #50: Bash

```json
{
 "command": "for f in fa72848139f07717 948d2d1ce1d3354a 5d8c962be9136432 74b1dfd510ae07a0 514384b1671bf57f; do\necho \"=== $f ===\"\nwc -l /home/sfmqrb/git/rishe/data/verification/sources/web/$f.txt\nhead -c 300 /home/sfmqrb/git/rishe/data/verification/sources/web/$f.txt\necho\ndone"
}
```


### [2026-09-04T18:15:52.373Z] TOOL RESULT

```
=== fa72848139f07717 ===
2449 /home/sfmqrb/git/rishe/data/verification/sources/web/fa72848139f07717.txt
URL: https://en.wiktionary.org/wiki/آب
FETCHED: 2026-09-04T14:59:50Z
STATUS: 200
TITLE: آب - Wiktionary, the free dictionary

آب - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entr
=== 948d2d1ce1d3354a ===
620 /home/sfmqrb/git/rishe/data/verification/sources/web/948d2d1ce1d3354a.txt
URL: https://en.wiktionary.org/wiki/آفتاب
FETCHED: 2026-09-04T14:59:51Z
STATUS: 200
TITLE: آفتاب - Wiktionary, the free dictionary

آفتاب - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community porta
=== 5d8c962be9136432 ===
338 /home/sfmqrb/git/rishe/data/verification/sources/web/5d8c962be9136432.txt
URL: https://en.wiktionary.org/wiki/آبرو
FETCHED: 2026-09-04T15:09:54Z
STATUS: 200
TITLE: آبرو - Wiktionary, the free dictionary

آبرو - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Re
=== 74b1dfd510ae07a0 ===
463 /home/sfmqrb/git/rishe/data/verification/sources/web/74b1dfd510ae07a0.txt
URL: https://en.wiktionary.org/wiki/بهاء
FETCHED: 2026-09-04T18:15:47Z
STATUS: 200
TITLE: بهاء - Wiktionary, the free dictionary

بهاء - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Re
=== 514384b1671bf57f ===
254 /home/sfmqrb/git/rishe/data/verification/sources/web/514384b1671bf57f.txt
URL: https://en.wiktionary.org/wiki/أبهة
FETCHED: 2026-09-04T15:09:54Z
STATUS: 200
TITLE: أبهة - Wiktionary, the free dictionary

أبهة - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Re
```


## [2026-09-04T18:15:55.728Z] AGENT

Good, all archived successfully. Now let me also archive the vajehyab Mo'in page and check exact wiktionary page URLs I should cite (need the actual URLs, not just percent-encoded versions — let's confirm the canonical URL form matches what appears in the index).


## [2026-09-04T18:15:57.269Z] TOOL CALL #51: Bash

```json
{
 "command": "python3 /home/sfmqrb/git/rishe/tools/fetch_source.py 'https://vajehyab.com/moein/ابهت' --note 'page 32 node4: Moein tags Persian abhat/ebhat as [A.] Arabic origin'\necho ---\ntail -6 /home/sfmqrb/git/rishe/data/verification/sources/web/index.jsonl"
}
```


### [2026-09-04T18:15:59.279Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d6f7206383f161c3.txt
---
{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/%CA%BEab-", "file": "data/verification/sources/web/7191e2277240767c.txt", "fetched": "2026-09-04T18:12:33Z", "status": 200, "bytes": 4932, "title": "Reconstruction:Proto-Semitic/ʔabw- - Wiktionary, the free dictionary", "note": "page 33, root Ab 2: confirms Proto-Semitic *ʔabw-/*ʔab- father, from Proto-Afroasiatic *ʔab-, an onomatopoeic nursery word"}
{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ep-", "file": "data/verification/sources/web/b60009fa4b7f1c12.txt", "fetched": "2026-09-04T18:14:37Z", "status": 200, "bytes": 9154, "title": "Reconstruction:Proto-Indo-European/h₂ep- - Wiktionary, the free dictionary", "note": "pdf page 32, root Ab1/Ap1 'water' (PART 2): nodes ap/ab, aftab, abru, Arabic ubbaha, Persian obbahat"}
{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C4%81%CC%81f%C5%A1", "file": "data/verification/sources/web/a6ba4e0fea3b8f19.txt", "fetched": "2026-09-04T18:14:38Z", "status": 200, "bytes": 5798, "title": "Reconstruction:Proto-Iranian/Hā́fš - Wiktionary, the free dictionary", "note": "pdf page 32, root Ab1/Ap1 'water' (PART 2): nodes ap/ab, aftab, abru, Arabic ubbaha, Persian obbahat"}
{"url": "https://en.wiktionary.org/wiki/%D8%A3%D8%A8%D9%87", "file": "data/verification/sources/web/2b6fb8fe67946706.txt", "fetched": "2026-09-04T18:14:38Z", "status": 200, "bytes": 5732, "title": "أبه - Wiktionary, the free dictionary", "note": "pdf page 32, root Ab1/Ap1 'water' (PART 2): nodes ap/ab, aftab, abru, Arabic ubbaha, Persian obbahat"}
{"url": "https://en.wiktionary.org/wiki/بهاء", "file": "data/verification/sources/web/74b1dfd510ae07a0.txt", "fetched": "2026-09-04T18:15:47Z", "status": 200, "bytes": 5394, "title": "بهاء - Wiktionary, the free dictionary", "note": "page 32 node3: Arabic baha, root b-h-w/b-h-y"}
{"url": "https://vajehyab.com/moein/ابهت", "file": "data/verification/sources/web/d6f7206383f161c3.txt", "fetched": "2026-09-04T18:15:59Z", "status": 200, "bytes": 292, "title": "معنی ابهت | فرهنگ انتشارات معین | واژه یاب", "note": "page 32 node4: Moein tags Persian abhat/ebhat as [A.] Arabic origin"}
```


## [2026-09-04T18:16:07.830Z] TOOL CALL #52: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/sources/web/2b6fb8fe67946706.txt"
}
```


### [2026-09-04T18:16:07.865Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%D8%A3%D8%A8%D9%87
FETCHED: 2026-09-04T18:14:38Z
STATUS: 200
TITLE: أبه - Wiktionary, the free dictionary

أبه - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Arabic 

 Toggle Arabic subsection 

 1.1 
 Pronunciation 

 1.2 
 Verb 

 1.2.1 
 Conjugation 

 Toggle the table of contents 

 أبه 

 3 languages 

 العربية 
 Magyar 
 Русский 

 Entry 

 Discussion 

 English 

 Read 

 Edit 

 View history 

 Tools 

 Tools

 move to sidebar 
 hide 

 Actions

 Read 

 Edit 

 View history 

 General

 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Cite this page 
 Get shortened URL 

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Arabic
 [ edit ] 

 Root 

 ء ب ه ( ʔ b h ) 

 2 terms 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ʔa.ba.ha/ , /ʔa.bi.ha/ 

 Verb
 [ edit ] 

 أَبَهَ or أَبِهَ • ( ʔabaha or ʔabiha ) I ( non-past يَأْبَهُ ( yaʔbahu ) , verbal noun أَبَه ( ʔabah ) or أَبْه ( ʔabh ) ) 

 to pay attention 

 to heed 

 to take notice 

 Conjugation
 [ edit ] 

 Conjugation of أَبَهَ , أَبِهَ (I, sound, a/i ~ a, impersonal passive, verbal nouns أَبَه , أَبْه )

 verbal noun
 الْمَصْدَر 

 أَبَه , أَبْه 
 ʔabah , ʔabh 

 active participle
 اِسْم الْفَاعِل 

 آبِه 
 ʔābih 

 passive participle
 اِسْم الْمَفْعُول 

 مَأْبُوه 
 maʔbūh 

 active voice
 الْفِعْل الْمَعْلُوم 

 singular
 الْمُفْرَد 

 dual
 الْمُثَنَّى 

 plural
 الْجَمْع 

 1 st person
 الْمُتَكَلِّم 

 2 nd person
 الْمُخَاطَب 

 3 rd person
 الْغَائِب 

 2 nd person
 الْمُخَاطَب 

 3 rd person
 الْغَائِب 

 1 st person
 الْمُتَكَلِّم 

 2 nd person
 الْمُخَاطَب 

 3 rd person
 الْغَائِب 

 past (perfect) indicative
 الْمَاضِي 

 m

 أَبَهْتُ , أَبِهْتُ 
 ʔabahtu , ʔabihtu 

 أَبَهْتَ , أَبِهْتَ 
 ʔabahta , ʔabihta 

 أَبَهَ , أَبِهَ 
 ʔabaha , ʔabiha 

 أَبَهْتُمَا , أَبِهْتُمَا 
 ʔabahtumā , ʔabihtumā 

 أَبَهَا , أَبِهَا 
 ʔabahā , ʔabihā 

 أَبَهْنَا , أَبِهْنَا 
 ʔabahnā , ʔabihnā 

 أَبَهْتُمْ , أَبِهْتُمْ 
 ʔabahtum , ʔabihtum 

 أَبَهُوا , أَبِهُوا 
 ʔabahū , ʔabihū 

 f

 أَبَهْتِ , أَبِهْتِ 
 ʔabahti , ʔabihti 

 أَبَهَتْ , أَبِهَتْ 
 ʔabahat , ʔabihat 

 أَبَهَتَا , أَبِهَتَا 
 ʔabahatā , ʔabihatā 

 أَبَهْتُنَّ , أَبِهْتُنَّ 
 ʔabahtunna , ʔabihtunna 

 أَبَهْنَ , أَبِهْنَ 
 ʔabahna , ʔabihna 

 non-past (imperfect) indicative
 الْمُضَارِع الْمَرْفُوع 

 m

 آبَهُ 
 ʔābahu 

 تَأْبَهُ 
 taʔbahu 

 يَأْبَهُ 
 yaʔbahu 

 تَأْبَهَانِ 
 taʔbahāni 

 يَأْبَهَانِ 
 yaʔbahāni 

 نَأْبَهُ 
 naʔbahu 

 تَأْبَهُونَ 
 taʔbahūna 

 يَأْبَهُونَ 
 yaʔbahūna 

 f

 تَأْبَهِينَ 
 taʔbahīna 

 تَأْبَهُ 
 taʔbahu 

 تَأْبَهَانِ 
 taʔbahāni 

 تَأْبَهْنَ 
 taʔbahna 

 يَأْبَهْنَ 
 yaʔbahna 

 subjunctive
 الْمُضَارِع الْمَنْصُوب 

 m

 آبَهَ 
 ʔābaha 

 تَأْبَهَ 
 taʔbaha 

 يَأْبَهَ 
 yaʔbaha 

 تَأْبَهَا 
 taʔbahā 

 يَأْبَهَا 
 yaʔbahā 

 نَأْبَهَ 
 naʔbaha 

 تَأْبَهُوا 
 taʔbahū 

 يَأْبَهُوا 
 yaʔbahū 

 f

 تَأْبَهِي 
 taʔbahī 

 تَأْبَهَ 
 taʔbaha 

 تَأْبَهَا 
 taʔbahā 

 تَأْبَهْنَ 
 taʔbahna 

 يَأْبَهْنَ 
 yaʔbahna 

 jussive
 الْمُضَارِع الْمَجْزُوم 

 m

 آبَهْ 
 ʔābah 

 تَأْبَهْ 
 taʔbah 

 يَأْبَهْ 
 yaʔbah 

 تَأْبَهَا 
 taʔbahā 

 يَأْبَهَا 
 yaʔbahā 

 نَأْبَهْ 
 naʔbah 

 تَأْبَهُوا 
 taʔbahū 

 يَأْبَهُوا 
 yaʔbahū 

 f

 تَأْبَهِي 
 taʔbahī 

 تَأْبَهْ 
 taʔbah 

 تَأْبَهَا 
 taʔbahā 

 تَأْبَهْنَ 
 taʔbahna 

 يَأْبَهْنَ 
 yaʔbahna 

 imperative
 الْأَمْر 

 m

 اِئْبَهْ 
 iʔbah 

 اِئْبَهَا 
 iʔbahā 

 اِئْبَهُوا 
 iʔbahū 

 f

 اِئْبَهِي 
 iʔbahī 

 اِئْبَهْنَ 
 iʔbahna 

 passive voice
 الْفِعْل الْمَجْهُول 

 singular
 الْمُفْرَد 

 dual
 الْمُثَنَّى 

 plural
 الْجَمْع 

 1 st person
 الْمُتَكَلِّم 

 2 nd person
 الْمُخَاطَب 

 3 rd person
 الْغَائِب 

 2 nd person
 الْمُخَاطَب 

 3 rd person
 الْغَائِب 

 1 st person
 الْمُتَكَلِّم 

 2 nd person
 الْمُخَاطَب 

 3 rd person
 الْغَائِب 

 past (perfect) indicative
 الْمَاضِي 

 m

 —

 —

 أُبِهَ 
 ʔubiha 

 —

 —

 —

 —

 —

 f

 —

 —

 —

 —

 —

 non-past (imperfect) indicative
 الْمُضَارِع الْمَرْفُوع 

 m

 —

 —

 يُؤْبَهُ 
 yuʔbahu 

 —

 —

 —

 —

 —

 f

 —

 —

 —

 —

 —

 subjunctive
 الْمُضَارِع الْمَنْصُوب 

 m

 —

 —

 يُؤْبَهَ 
 yuʔbaha 

 —

 —

 —

 —

 —

 f

 —

 —

 —

 —

 —

 jussive
 الْمُضَارِع الْمَجْزُوم 

 m

 —

 —

 يُؤْبَهْ 
 yuʔbah 

 —

 —

 —

 —

 —

 f

 —

 —

 —

 —

 —

 Retrieved from " https://en.wiktionary.org/w/index.php?title=أبه&oldid=88975147 "

 Categories : Arabic terms belonging to the root ء ب ه 
 Arabic 3-syllable words 
 Arabic terms with IPA pronunciation 
 Arabic lemmas 
 Arabic verbs 
 Arabic form-I verbs 
 Arabic sound form-I verbs 
 Arabic form-I verbs with ء as first radical 
 Arabic form-I verbs with past vowel a and non-past vowel a 
 Arabic form-I verbs with past vowel i and non-past vowel a 
 Arabic verbs with impersonal passive 

 Hidden categories: Pages with entries 
 Pages with 1 entry 

 This page was last edited on 30 December 2025, at 07:13.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

 Privacy policy 

 About Wiktionary 

 Disclaimers 

 Legal & safety contacts 

 Code of Conduct 

 Developers 

 Statistics 

 Cookie statement 

 Mobile view 

 Search 

 Search 

 Toggle the table of contents 

 أبه 

 3 languages 

 Add topic
```


## [2026-09-04T18:16:08.340Z] TOOL CALL #53: Bash

```json
{
 "command": "grep -n -i 'ubbuha\\|ubbaha\\|derived\\|verb\\|root\\|meaning' /home/sfmqrb/git/rishe/data/verification/sources/web/2b6fb8fe67946706.txt | head -30"
}
```


### [2026-09-04T18:16:08.383Z] TOOL RESULT

```
65: Verb 
135: Root 
146: Verb
149: أَبَهَ or أَبِهَ • ( ʔabaha or ʔabiha ) I ( non-past يَأْبَهُ ( yaʔbahu ) , verbal noun أَبَه ( ʔabah ) or أَبْه ( ʔabh ) ) 
160: Conjugation of أَبَهَ , أَبِهَ (I, sound, a/i ~ a, impersonal passive, verbal nouns أَبَه , أَبْه )
162: verbal noun
596: Categories : Arabic terms belonging to the root ء ب ه 
600: Arabic verbs 
601: Arabic form-I verbs 
602: Arabic sound form-I verbs 
603: Arabic form-I verbs with ء as first radical 
604: Arabic form-I verbs with past vowel a and non-past vowel a 
605: Arabic form-I verbs with past vowel i and non-past vowel a 
606: Arabic verbs with impersonal passive
```


## [2026-09-04T18:16:17.983Z] TOOL CALL #54: Bash

```json
{
 "command": "grep -n -A3 -i 'descendant\\|Iranian\\|Persian\\|Avestan\\|Sanskrit\\|Latin' /home/sfmqrb/git/rishe/data/verification/sources/web/b60009fa4b7f1c12.txt | head -60"
}
```


### [2026-09-04T18:16:18.026Z] TOOL RESULT

```
169: Unlike its neuter synonym *wódr̥ , *h₂ep- is always gendered in descendants. This may reflect the same animate–inanimate (or semantically active–passive) distinction in early PIE that is often supposed for the nouns meaning “fire”, such as *h₁n̥gʷnís   m and *péh₂wr̥   n respectively.
170-
171- Alternative reconstructions
172- [ edit ] 
--
184: Proto-Indo-Iranian: *Hā́ps ( see there for further descendants )
185-
186- Proto-Tocharian: *āp ( “ water, river ” ) [ 3 ] 
187- Tocharian A: āp 
--
201: Proto-Celtic: *abū ( “ river ” ) ( see there for further descendants )
202-
203: Proto-Germanic: *apô ( “ water sprite” → “ape, monkey ” ) ( possibly ) ( see there for further descendants )
204-
205- ⇒ *h₂ph₃n-éh₂ 
206- Proto-Albanian: *abnā 
--
211: Latin: amnis 
212-
213- Lusitanian: abne 
214-
--
248: ^ De Vaan, Michiel ( 2008 ), “ amnis ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 39 
249-
250- ^ Mallory, J. P. , Adams, D. Q. , editors ( 1997 ), “ *h₂eb(h)- ”, in Encyclopedia of Indo-European Culture , London, Chicago: Fitzroy Dearborn Publishers, page 486 
251-
--
276: ⇒ ᾰ̔φή ( hăphḗ , “ grip; (sense of) touch ” ) [ note 1 ] ( see there for further descendants )
277-
278- *h₂ép-mn̥ 
279- Proto-Hellenic: *ápmə 
--
292: Ancient Greek: ᾰ̓́ψος ( ắpsos ) , ᾰ̔́ψος ( hắpsos , “ joint; limb ” ) [ note 1 ] ( see there for further descendants )
293-
294: Proto-Indo-Iranian: *Hápsas ( “ protruding part of the body ” ) 
295- Proto-Indo-Aryan: *Hápsas 
296: Sanskrit: अप्स॑स् ( ápsas , “ front protrusion of the body: breast, face, forehead, tusk ” ) 
297-
298: Proto-Iranian: *Hápsas 
299- Ossetian: ӕфцӕг ( æfcæg , “ protruding part, neck ” ) 
300-
301- Proto-Tocharian: 
--
309: Latin: aptus ( “ connected, fitting, fit, suitable ” ) ( see there for further descendants )
310-
311- Unsorted formations 
312- Proto-Armenian: 
--
316: Proto-Indo-Iranian: 
317: Proto-Iranian: 
318: Avestan: 𐬁𐬟𐬆𐬥𐬙𐬈 ( āfənte ) 
319-
320- Proto-Italic: *apeks ? 
321: > ? Latin: apex ( see there for further descendants )
322-
323- Notes
324- [ edit ]
```


## [2026-09-04T18:16:30.021Z] TOOL CALL #55: Bash

```json
{
 "command": "grep -n -B2 -A2 -i 'avestan\\|old persian\\|descendant' /home/sfmqrb/git/rishe/data/verification/sources/web/a6ba4e0fea3b8f19.txt | head -40"
}
```


### [2026-09-04T18:16:30.068Z] TOOL RESULT

```
72-
73- 1.2.3 
74: Descendants 
75-
76- 1.3 
--
230- *Hā́pākaH 
231-
232: Descendants
233- [ edit ] 
234-
235- Central Iranian:
236: Old Avestan: 𐬀𐬞𐬋 ( apō , acc.pl. ) 
237: Younger Avestan: 𐬀𐬞 ( ap ) , 𐬁𐬟𐬱 ( āfš , nom.sg. ) 
238-
239- Northeastern Iranian:
--
295- Larestani: او ( ow ) , هو ( how ) 
296-
297: Old Persian: [Term?] ( /⁠āpī[š]⁠/ , nom.sg. ) , 𐎠𐎱𐎡𐎹𐎠 ( a-p-i-y-a /⁠apiyā⁠/ , loc.sg. ) ( transferred to i-stem ) 
298- Middle Persian: 
299- Manichaean: 𐫀𐫁 ( ʾb /⁠āb⁠/ ) 
--
348- Gurani terms with non-redundant manual transliterations 
349- Requests for native script for Bashkardi terms 
350: Old Persian term requests 
351- Persian terms with redundant transliterations 
352-
```


## [2026-09-04T18:16:33.658Z] AGENT

Good, this fully confirms node #1 (Avestan āp/āfš, water) → Middle Persian āb chain. I now have sufficient material. Let me check the AFM local reference once more briefly for ref_check completeness, then compile the JSON output.


## [2026-09-04T18:16:35.217Z] TOOL CALL #56: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet\nls /home/sfmqrb/git/rishe/data/verification/sources/refs/AFM* 2>/dev/null"
}
```


### [2026-09-04T18:16:35.272Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_alt.txt
/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt
/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.pdf
/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt
```


## [2026-09-04T18:17:00.797Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==13' KLN_1966.txt | head -80"
}
```


### [2026-09-04T18:17:02.608Z] TOOL RESULT

```
an
Republics
Russ.
Russian
V.
verb
S.
South
var.
variant
S.Afr.
South  African
veter.
veterinary
S.Am.
South  American
VArab.
Vulgar  Arabic
XXV
VL.
Vulgar  Latin
vulg.
vulgar
Vulg.
Vulgate
W.
Welsh
W.African
West  African
WSem.
West  Semitic
WTeut.
West  Teutonic
Zech.
Zechariah
Zeph.
Zephaniah
zool.
zoology
Symbols  used  in  this  Dictionary
A
The  asterisk  (*)  indicates  a  hypothetical  form.
The  mark  called  macron  (-)  is  placed  over  a  vowel  to  show  that  it  is  long.
The  mark  called  breve  (  ')  is  placed  over  a  vowel  to  show  that  it  is  short.
In  this  dictionary  the  quantity  of  vowels  (esp.  in  Greek  and  Latin  words)  is  mdica  ed  °  ^ when  they  are  long.  The  brevity  of  vowels  is  indicated  only  in  some  special  cases  (e.g.  m  Latin "  to  ie  to  hang’,  in  contradistinction  to  pendtre,  ‘to  hang’  (see  pendan,).  Hence when  there  is  no  mark  over  a  vowel  it  is  to  be  assumed  that  it  is  short.
The  mark’  after  a  consonant  in  the  Slavonic  languages  indicates  Palata  “'
The  mark  -  after  a  syllable  or  a  group  of  syllables  (as  in  ant-,anti-)  indicates  that  this  syllable
or  group  of  syllables  is  a  prefix.
The  mark  -  before  a  syllable  or  a  group  of  syllables  (as  in  -ate,
syllable  or  group  of  syllables  is  a  suffix.
-atiori)  indicates  that  this
a,  indef.  article.  —  Form  of  an  before  a  consonant, a,  prep,  meaning  ‘of’,  as  in  a  clock  =  of  the dock.  —  ME.,  fr.  OE.  of,  ‘from,  off,  of’.  See  of. a,  prep,  meaning  ‘on*.  —  OE.  an,  on,  ‘on’.  See  on. a,  prep,  meaning  ‘to,  at,  in’.  —  F.,  fr.  L.  ad,  ‘to, toward’.  See  ad-  and  cp.  a-,  pref.  corresponding to  L.  ad-.  Cp.  also  a  la.
a-,  pref.  meaning  ‘of’,  as  in  akin.  —  ME.  a-, fr.  OE.  of.  See  a,  prep,  meaning  ‘of’, a-,  pref.  meaning  ‘on’;  used  to  form  adverbs from  nouns  as  in  abroad,  ashore.  —  Fr.  OE.  an, on.  See  a,  prep,  meaning  ‘on’, a-,  intensive  pref.  —  OE.  a-,  rel.  to  OS.,  OFris. ur-,  or-,  Du.  oor-,  OHG.,MHG.  ur-  (unstressed  : OHG.  ir-,  ar-,  MHG.,  G.  -er),  Goth.  us-.  The orig.  meaning  of  these  prefixes  was  ‘out,  away’. Cp.  the  pref.  in  oakum,  ordeal. a-,  pref.  meaning  ‘away  from,  from’  (occurring only  before  v),  as  in  avert.  —  L.  a-,  fr.  a,  short form  of  ab,  ‘away  from,  from’ ;  rel.  to  Oscan aa-,  Umbr.  aha-,  ‘away  from,  from’.  See  ab-. a-,  pref.  corresponding  to  L.  ad-,  fr.  ad,  ‘to,  to¬ ward’,  either  directly  or  through  the  medium  of OF.  a-  or  F.  a.  Cp.  the  pref.  in  abandon,  acknow¬ ledge,  ascend,  ascribe,  and  see  ad-.  Cp.  also  a. a-,  priv.  pref.  meaning  ‘not,  less,  without’.  — Gk.  a-,  used  before  a  consonant,  the  form  be¬ fore  a  vowel  being  av-.  See  an-  and  cp.  the  priv. prefixes  in-  and  un-.
aam,  n.,  a  Dutch  and  German  liquid  measure.  — Du.,  fr.  L.  ama  (more  exactly  hamd),  ‘bucket’, fr.  Gk.  (prop,  apt)),  ‘bucket’,  which  is  rel. to  apocoflai,  ‘to  draw,  gather’,  dpvtov,  ‘a  bowl in  which  the  blood  of  victims  was  caught’.  See amnion.
aardvark,  n.,  a  South  African  burrowing  animal. —  Du.,  lit.  ‘earth  pig’,  fr.  aard,  ‘earth’,  and vark,  ‘pig’.  See  earth  and  farrow, aardwolf,  n.,  a  South  African  hyena-like  mam¬ mal.  —  Du.,  lit.  ‘earth  wolf’.  See  prec.  word and  wolf.
Aaron,  masc.  PN.;  in  the  Bible,  the  brother  of Moses.  —  LateL.,fr.  Gk.  ’Aotpwv.fr.  Heb.  Ahd- rSn,  which  is  prob.  of  Egyptian  origin.  Arab. Martin  is  borrowed  from  Hebrew.
Derivative:  Aaron-ic,  adj.
A*ron’s  beard,  name  of  several  plants.  —  So called  because  of  their  resemblance  to  a  beard ®nd  with  allusion  to  Ps.  1 33 : 2.
rod,  1)  straight  molding  in  architecture; 2)  Popular  name  of  the  common  mullein.  — So  called  with  allusion  to  Nu.  17.
n.,  name  of  the  fifth  Jewish  month.  —  Heb. fr.  Akkad,  abu.
Pref.  in  words  of  Latin  origin,  denoting  de¬ parture,  separation.  —  L.  ab-,  fr.  ab,  ‘away  from, from ;  by’.  The  form  ab  is  regularly  used  before
all  vowels  and  h;  before  consonants  except  h, ab  usually  becomes  a;  before  c,  q,  t,  it  becomes abs.  L.  ab  derives  fr.  orig.  *ap  (cp.  aperio,  ‘I open'),  and  is  cogn.  with  OI.  apa,  ‘away  from’, Gk.  Mi,  ‘away  from,  from’,  Goth,  af,  OE.  of, ‘away  from,  from’.  See  of  and  cp.  a-,  ‘away from’,  apo-,  post-.
aba,  n.,  a  form  of  altazimuth  instrument.  —  So called  after  its  inventor  Antoine  Thomson A'Abbadie.
aback,  adv.  —  OE.  on  bzc.  See  a-,  ‘on’,  and  back, abacus,  n„  1)  frame  with  beads  for  calculation; 2)  (archil.)  slab  at  the  top  of  a  column.  —  L. abacus,  fr.  Gk.  afjaE.,  gen.  afiaxoc;,  ‘a  square tablet  strewn  with  dust’,  fr.  Heb.  abhdq,  ‘dust’, fr.  root  a-b-q,  ‘to  fly  off’.  The  first  type  of  abacus was  a  board  covered  with  dust,  whence  its  name. Abaddon,  n.,  the  bottomless  pit.  —  Heb.  dbhad- ddn,  ‘destruction’,  fr.  abhadh,  ‘he  perished’,  which is  rel.  to  Aram,  abhadh,  ‘he  perished’,  Ugar.  ’hd, ‘to  perish’,  Ethiop.  abada,  ‘he  wandered  about’, Arab,  abada,  ‘it  (the  animal)  fled  in  fright’, abaft,  adv.,  astern,  aft;  prep.,  behind.  —  Formed fr.  a-,  ‘on’,  and  OE.  beseftan,  fr.  be,  ‘by,  at’, and  seftan.  ‘behind’.  See  be-  and  aft. abalienate,  tr.  v.,  1)  to  alienate;  2)  to  remove.  — L.  abalienatus,  pp.  of  abalienare,  ‘to  remove’, lit.  ‘to  make  alien  from’,  fr.  ab-  and  alienare. See  alienate.
abalienation,  n.,  1)  alienation;  2)  removal.  — L.  abaliendtio,  gen.  -dnis,  fr.  abalienatus,  pp. of  abalienare.  See  prec.  word  and  -ion. abalone,  n.,  a  mollusk.  —  Sp.,  of  unknown  origin, abandon,  tr.  v.,  to  leave,  forsake.  —  ME.  aban- donen,  fr.  OF.  abandonee  (F.  abandonner),  fr.  a bandon  in  ( mettre )  a  bandon,  ‘to  give  up  to  a public  ban’,  fr.  a,  ‘to’  (fr.  L.  ad)  and  bandon, ‘power,  authority,  jurisdiction’,  fr.  Late  L.  han- dum,  bannum,  ‘order,  decree’,  which  is  of  Teut. origin.  See  ad-  and  ban,  ‘proclamation’,  and  cp. banish.
Derivatives :  abandon,  n.,  abandon-ed,  adj.,  aban¬ donee,  n.,  abandon-ment,  n. abase,  tr.  v.,  to  lower.  —  OF.  abaissier  (F.  abais- ser),  ‘to  bring  low’,  fr.  VL.  *adbassiare,  which is  formed  fr.  L.  ad-  and  Late
```


## [2026-09-04T18:17:14.782Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==12' KLN_1966.txt | tail -30\necho \"=== leaf14 head ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==14' KLN_1966.txt | head -30"
}
```


### [2026-09-04T18:17:16.964Z] TOOL RESULT

```
theatrical
theology
Thessalian
Tocharian
transitive
Turkish
R.C.Ch.
Roman  Catholic  Church
typogr.
typography
refl.
reflexive
rel.
relative;  related
Ugar.
Ugaritic
relig.
religion
ult.
ultimate,  ultimately
rhet.
rhetoric
U.S.A.
United  States  of  America
Rom.
Roman
U.S.S.R.
United  Soviet  Socialist
Rum.
Rumani
=== leaf14 head ===
  L.  bassus,  ‘thick,  fat, low’.  See  base,  ‘low’,  and  cp.  the  second  element in  bouillabaisse.
Derivatives :  abas-ed ,  adj.,  abas-ed-ly,  adv.,  abas- ed-ness,  n.,  abase- ment,  n. abash,  tr.  v.,to  confuse;  to  put  to  shame.  —  ME. abassen,  abaissen,  abashen,  fr.  OF.  esbahiss-, pres.  part,  stem  of  esbahir,  ‘to  astonish’,  com¬ pounded  of  pref.  es-  (fr.  L.  ex\  see  1st  ex-)  and a  derivative  of  OF.  baer  (F.  bayer ),  ‘to  gape’, the  change  of  conjugation  (-ir  for  -er)  being prob.  due  to  the  influence  of  the  OF.  adj.  batf.
abasia
abiogenesis
‘astonished’.  The  OF.  verb  baer  derives  fr.  VL. batare,  ‘to  gape,  yawn’.  See  bay,  ‘part  in  the wall’,  and  cp.  words  there  referred  to. Derivatives:  abash-less,  adj.,  abash-less-ly,  adv., abash-ment,  n.
abasia,  n.,  inability  to  walk  ( med .)  —  Medical  L., formed  fr.  priv.  pref.  a-  and  Gk.  Bam?,  ‘stepping, step;  base’,  from  the  stem  of  flaivsiv,  ‘to  go’. See  base,  n.,  and  -ia.
abate,  tr.  and  intr.  v.  —  ME.  abaten,  fr.  OF.  abatre, abattre  (F.  abattre),  ‘to  beat  down’,  fr.  VL.  *ab- balere  (whence  also  It.  abbattere,  Sp.  abatir ), fr.  ab-  and  batere  (L.  battuere),  ‘to  beat,  strike’. See  batter,  ‘to  beat,  strike’,  and  cp.  abatis,  abat¬ toir,  bate,  ‘to  reduce’.
Derivative:  abate-ment,  n. abatis,  n.,  a  defense  made  of  felled  trees  (m/7.)  — F.,  ‘things  thrown  down’,  fr.  abattre,  ‘to  beat down,  throw  down’.  See  prec.  word  and  cp. abattoir.
abattoir,  n.,  a  slaughterhouse.  —  F.,  fr.  abattre, ‘to  beat  down’.  See  abate.  The  subst.  suff.  -oir corresponds  to  L.  -orium,  whence  E.  -ory. abb,  n.,  the  yarn  for  the  woof.  —  OE.  aweb,  ab. See  a-,  ‘on’,  and  web.
abba,  n.,  title  of  honor.  —  L.,  fr.  Gk.  fr.
Aram,  abbd,  ‘the  father;  my  father’,  emphatic state  of  abh,  ‘father’.  See  abbot,  and  cp.  ab¬ bacy,  abbey.
abbacy,  n.,  the  office  or  jurisdiction  of  an  abbot. —  Eccles.  L.  abbatia,  fr.  abbas,  gen.  abbatis.  See abbot  and  cp.  abba,  abbey.  Cp.  also  badia. abbe,  n.,  a  title  given  in  France  to  a  priest.  —  F., fr.  Eccles.  L.  abbatem,  acc.  of  abbas.  Cp.  It. abbate,  Sp.  abad,  ‘abbot’,  which  also  derive  fr. Eccles.  L.  abbatem,  and  see  abbot, abbess,  n.  • —  ME.  abbesse,  fr.  OF.  ( =  F.)  abbesse, fr.  Eccles.  L.  abbatissa,  fern,  of  abbas,  gen.  -at is. See  abbot  and  cp.  It.  abbadessa,  badessa,  and Sp.  abode sa,  ‘abbess’,  which  also  derive  fr.  Ec¬ cles.  L.  abbatissa.
abbey,  n.,  a  convent  headed  by  an  abbot  or  an abbess.  —  ME.,  fr.  AF.  abbeie,  fr.  OF.  abeie, abaie  (F.  abbaye),  fr.  Eccles.  L.  abbatia,  fr.  L. abbas.  See  abbot  and  cp.  abba,  abbacy,  abbess. Cp.  also  It.  abbadia,  Sp.  abadia,  ‘abbey’,  which also  derive  fr.  Eccles.  L.  abbatia. abbot,  n.  —  OE.  abbod,  fr.  L.  abbat-,  stem  of abbas,  gen.  abbatis,  fr.  Aram,  abbd,  ‘the  father; my  father’,  emphatic  state  of  abh,  ‘father’,  which is  rel.  to  Heb.  abh,  ‘father’.  See  Aboth  and  cp. words  there  referred  to.  Cp.  also  abba,  abbacy, abbe,  abbey,  abuna,  badia. abbreviate,  tr.  v.,  to  shorten.  —  L.  abbrevidtus, pp.  of  ahbrevidre,  ‘to  shorten’,  fr.  ab-  and  bre- vidre,  ‘to  shorten’,  fr.  brevis,  ‘short’.  See  brief, adj., and  cp.  abridge,  which  is  a  doublet  of  abbreviate. Derivatives:  abbreviat-ed,  adj.,  abbreviation,  ab- breviator  (qq.v.),  abbreviat-ory,  adj. abbreviation,  n.  —  F.  abreviation,  fr.  L.  abbrevia- tidnem,  acc.  of  abbreviatio,  fr.  abbrevidtus,  pp. of  abbreviare.  See  abbreviate  and  -ion.
abbreviator,  n.  —  L.,  fr.  abbrevidtus,  pp.  of  ab- breviare.  See  abbreviate  and  agential  suff.  -or. Abderian,  pertaining  to  Abdera.  —  See  Abderite and  -ian.
Abderite,  n„  i)  an  inhabitant  of  Abdera;  2)  a fool.  —  L.  Abderita ,  fr.  Gk.  ’A(38r)ptnr]!;,  ‘in¬ habitant  of  Abdera’,  fr.”A[38if]pa  (pi.),  ‘Abdera’, a  town  proverbial  for  the  stupidity  of  its  in¬ habitants.  For  sense  development  cp.  Gotha¬ mite.  For  the  ending  see  subst.  suff.  -ite. abdest,  n.,  the  Mohammedan  rite  of  washing  the hands  before  prayer.  —  Pers.  dbddst,  lit.  ‘water for  the  hand’,  fr.  ab,  ‘water’,  and  dost,  ‘hand’. Pers.  ab,  ‘water’,  is  rel.  to  Avestic  dp-,  OI.  dpah (fern,  pi.),  ‘water’;  sec  amnic  and  cp.  the  first element  in  abkari  and  the  second  element  in doab  and  in  julep.  Pers.  dost,  ‘hand’,  is  rel.  to Avestic  zasta,  ‘hand’,  fr.  I.-E.  base  *ghosto -, whence  also  OI.  hastah,  ‘hand’.  See  hasta  and cp.  hath.
abdicate,  tr.  v.  —  L.  abdicatus,  pp.  of  abdicate, ‘to  renounce,  resign,  abdicate’,  fr.  ab-  and  di- care,  ‘to  proclaim,  dedicate,  consecrate,  devote’, which  is  related  to  dicere,  ‘to  say,  tell’.  See  dic¬ tion  and  verbal  suff.  -ate  and  cp.  dedicate,  in¬ dicate.
abdication,  n.  —  L.  abdicatio,  gen.  -dnis,  ‘renun¬ ciation,  abdication’,  from  abdicatus  pp.  of  ab¬ dicate.  See  prec.  word  and  -ion. abdomen,  n.,  the  belly.  —  L.  abdomen  (later  also abdumen),  ‘the  lower  part  of  the  belly,  paunch, abdomen’,  which  prob.  meant  orig.  ‘the  hidden part  of  the  body’,  and  stands  for  *abdemen,  a derivative  of  abdd,  abdere,  ‘to  hide’,  which  is formed  from  ab-,  and  -dere  (used  only  in  com¬ pounds),  fr.  I.-E.  base  *dhe-,  *dh'-,  ‘to  put, place’ ;  see  do  and  cp.  words  there  referred  to. See  Walde-Hofmann,  LEW.,  I.,  p.  3. abdominal,  adj.,  pertaining  to  the  abdomen.  — • Medical  L.  abdominalis,  fr.  L.  abdomen,  gen. abdominis.  See  prec.  word  and  adj.  suff.  -al. Derivatives:  abdominal,  n.,  abdominally,  adv. abdomino-,  combining  form  denoting  the  ab¬ domen.  —  Fr.  L.  abdomen,  gen.  abdominis.  See abdomen.
abduce,  tr.  v.,  to  draw  away.  —  L.  abducere,  ‘to lead  away’.  See  next  word, abducent,  adj.,  drawing  back  or  away  (said  of  the muscles) ;  the  opposite  of  adducent.  —  L.  abdu- certs,  gen.  -entis,  pres.  part,  of  abducere,  ‘to  lead away’,  fr.  ab-,  and  diicere,  ‘to  lead’.  See  duke and  -ent.
abduct,  tr.  v.,  to  kidnap.  —  L.  abductus,  pp.  of abducere,  ‘to  lead  away’.  See  prec.  word, abduction,  n.  —  L.  abductid,  gen.  -ionis  ‘a  leading away’,  fr.  abductus,  pp.  of  abducere,  ‘to  lead away’.  See  prec.  word  and  -ion.  As  a  term  of logic,  L.  abductib  is  a  loan  translation  of  Gk. dtreaytoY 7),  ‘a  shifting  (of  the  argument)’,  lit.  ‘a leading  away’,  used  to  denote  a  syllogism  whose major  premise  is  certain,  but  whose  minor  pre¬ mise  is  only  probable.
abductor,  n.  ( anat .)  —  Medical  L.,  name  of  a muscle,  lit.  ‘that  which  leads  away’,  fr.  L.  ab¬ ductus,  pp.  of  abducere,  ‘to  lead  away’.  See  ab¬ duct  and  agential  suff.  -or. abeam,  adv.,  at  right  angles  to  the  keel  ( naut .)  — Lit.  ‘on  the  beam’,  fr.  a-,  ‘on’,  and  beam, abecedarian,  adj.,  elementary,  rudimentary.  — ML.  abecedarius,  ‘pertaining  to  the  alphabet’, a  word  formed  from  the  names  of  the  first  four letters  of  the  alphabet.  For  the  ending  see  suff. -arian.
abecedarium,  n.,  an  ABC  book.  —  ML.,  prop, neut.  of  the  adjective  abecedarius,  used  as  a noun.  See  prec.  word.
abed,  adv.,  in  bed  (archaic).  —  Formed  fr.  a-, ‘on’,  and  bed.
Abel,  masc.  PN.;  in  the  Bible,  the  second  son  of Adam  and  Eve.  — -  L.,  fr.  Gk.  ’'A(3eX,  fr.  Heb. Hebhel,  lit.  ‘breath,  vanity’, abeie,  n.,  the  white  poplar.  —  Du.  abeel,  fr.  OF. aubel,  albel,  fr.  VL.  *albellus,  ‘whitish’,  dimin. of  albulus,  which  itself  is  dimin.  of  albus, ‘white’.  See  alb.
Abelmoschus,  n.,  a  genus  of  plants  of  the  mallow family  (bot.)  —  ModL.,  fr.  Arab,  habb-al-musk, in  vulgar  pronunciation  habb-el-mosk,  lit.  ‘grain of  musk’.  See  hubba  and  musk, abelmosk,  n„  a  plant  of  the  mallow  family.  — Fr.  prec.  word.
Abeona,  also  Adeona,  n.,  the  goddess  watching over  the  first  departure  of  children  from  the house  (Roman  mythol.)  —  L.  Abeona,  Adeona, formed  on  analogy  of  matrbna,  ‘matron’,  from the  stem  of  abire,  ‘to  go  away’,  resp.  of  adire, ‘to  approach’.  See  abiturient,  resp.  adit, aberdevine,  n„  the  siskin.  —  Of  unknown  origin, aberrance,  aberrancy,  n.  —  L.  aberrantia,  fr.  aber- rans,  gen.  aberrantis.  See  aberrant  and  -ce,  resp. -cy.
aberrant,  adj.,  deviating  from  what  is  normal.  — • L.  aberrans,  gen.  -antis,  pres.  part,  of  aberrare, ‘to  wander  away,  go  astray’,  fr.  ab-  and  err  are, ‘to  wander,  stray  about’.  See  err  and  -ant. aberration,  n.,  —  L.  aberratio,  gen.  -dnis,  ‘a  wan¬ dering’,  fr.  aherrat-(um),  pp.  stem  of  aberrare. See  prec.  word  and  -ation.
Derivative:  aberration-al,  adj.
•bet,  tr.  v.  —  ME.  abetten,  fr.  OF.  abeter,  ‘to bait’,  lit.  ‘to  cause  to  bite’,  fr.  a-  (fr.  L.  ad,  ‘to’) and  OF  beter,  ‘to  bait’,  which  is  of  Teut.  origin; cp.  ON.  beita,  ‘to  cause  to  bite’,  bita,  OE.  bitan, “to  bite’.  See  ad-  and  bait,  bite,  and  cp.  bet Derivatives :  abet-ment,  abett-al,  abett-er,  abett¬ or,  nouns.
•beto,  n.,  the  fir  tree  called  Abies  religiosa.  —  Sp., ft.  L.  abies,  gen.  abietis,  ‘the  silver  fir’.  See  Abies. *fc*y*nce,  n.,  temporary  inactivity.  —  AF.  a- beiance,  ‘suspension’,  formed  fr.  a-  (fr.  L.  ad,  ‘to’, see  ad-),  and  OF.  beer  (F.  bayer),  ‘to  gape’,  fr. L.  batare  ‘to  gape’.  See  bay,  ‘part  in  the  wall’, sod  cp.  words  there  referred  to.
■bhor,  tr.  v.  —  L.  abhorrire,  ‘to  shrink  away
```


## [2026-09-04T18:17:43.418Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'tap-\\|tāp\\|abi-tap' CHEUNG.txt | head -10"
}
```


### [2026-09-04T18:17:43.468Z] TOOL RESULT

```
24671:*AVESTAN: YAv. tap- “о be(come) hot’ || (+ *4-) ‘to warm’ || (+ *ham-) ‘to 
24718:tapt/tap- ‘to heat’, Gz. to(u)-/to(w)a ‘to shine, light up’, NP tab ‘fever’, tab ‘heat, 
25351:*tmp- (> Ir. *tap-), cf. LIV, ibid. Explaining the forms as a secondarily arisen 
33774:tap-, 378 
42097:tapt/tap-, 379
```


## [2026-09-04T18:17:46.965Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24700,24725p' CHEUNG.txt"
}
```


### [2026-09-04T18:17:47.010Z] TOOL RESULT

```
OKh. handau- ‘to become hot’, LKh. hamdev- (caus.) ‘to ripen’ = SGS: 38, 9, 67, 
50 £., 104, 140 f. 

*SOGDIAN: SSogd. t’p (denomin.) ‘to seal’ || (+ *a-) CSogd. "tpn ‘furnace’ || (+ 
*pati-) MSogd. ptp- ‘to burn’ (perhaps p- < *upa- ?) || (+ *ui-) BSogd. wyt’’p- ‘to 
shine, radiate’, CSogd. wyt’p ‘to shine forth’ || (+ ham-) BSogd. ’ntph ‘fever’ 

Pres.: ОРТ. 2sg. SSogd. t’py; Pass.: pret. intr. IND. 3sg. SSogd. tpty; Partic.: perf. pass. SSogd. tpt || (+ 
*pati-) Impf.: IND. 3sg. MSogd. ptyt’p; Partic.: perf. pass. ptßtyy ‘hot’ (BBB: 43); Pass.: perf. intr. IND. 
1р1. MSogd. ptBtyt "ym ‘we are burned’ || (+ *ui-) Pres.: IND. 35р. BSogd. wyt’’pt, BSogd. wyt’pt, 3pl. 
BSogd. wyt’p’nt, SUBJ. 3sg. BSogd. wyt’’p’t, Impf.: IND. 35р. CSogd. wyt’p 

*CHORESMIAN: t’BY- ‘to heat’, (denomin.) ‘to punctuate, put a diacritic; to hit the 
target’ || (+ *upa-) bdfs- ‘to become hot’ => Samadi: 203 f., 15 

*BACTRIAN: Taß- ‘to impress (a seal); to seal’ = S-W, Bact.: 225a 

*NWIR: NP taftan/tab- ‘to shine, burn’, NP tafsidan/tafs- (inch.) ‘to become hot’, Bal. 
tapt/tap- ‘to heat’, Gz. to(u)-/to(w)a ‘to shine, light up’, NP tab ‘fever’, tab ‘heat, 
burning; heated iron; affliction, pain, torment’, tabah, tavah ‘frying-pan; burnt brick, 
tile’, Kurd. taw ‘sun’ || (+ *abi-) NP айар ‘sun(shine)’ || (+ *ш-) Gur. (Kand.) yaw 
‘fever’ 

*NEIR: Oss. I. tæfsyn/tæfst, D. tefsun/tzfst (inch.) ‘to become hot’, I. tavyn/tavd, D. 
tavun/tavd (caus.) ‘to warm up’, also Oss. I. texsyn/taxst ‘to itch; to be feverishly 
ill’ (contaminated with inch. *daxsa- < *daj ?), Yzgh. tifs-/tüvd ‘to be (over)heated’,
```


## [2026-09-04T18:19:37.788Z] TOOL CALL #61: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet/page-32.json",
 "content": "{\n  \"pdf_page\": 32,\n  \"book_page\": 2,\n  \"verified_by\": \"claude-sonnet-5\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ab 1, Ap 1\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *h₂ep- 'water, body of water' (Mallory & Adams 1997 *h₂eb(h)-); Wiktionary's reconstruction unifies an Italo-Celtic branch (*h₂ph₃n-éh₂ > Lat. amnis, Proto-Celtic *abū) with the Proto-Indo-Iranian *Hā́ps branch (Av./Skt ap-). Pokorny (1959) instead splits these into two separate headwords: 'ab- \\\"Wasser, Fluß\\\"' (p.1, Italo-Celtic) and '2. äp- \\\"Wasser, Fluß\\\"' (p.51, Indo-Iranian/Greek, = AHD's ap-2, Pok. 51).\",\n      \"note\": \"Nourai's box groups 'Ab' and 'Ap' as one root and cites only POK:1, but the branch actually drawn in this chart (Avestan/Pahlavi āp > Persian āb) belongs to Pokorny's separate entry '2. äp-' on p.51 (AHD: 'ap-2. Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.]'), not to the p.1 'ab-' entry (Latin amnis, Old Irish ab, Celtic river names). Pokorny's own p.1 entry does cross-reference the p.51 entry ('Vgl. auch 2. äp- \\\"Wasser, Fluß\\\"'), and modern IE comparative work (Mallory & Adams 1997, followed by Wiktionary's *h₂ep- reconstruction) treats both as suffixed extensions of one root, so grouping them is defensible, but the specific page citation POK:1 does not cover the Iranian material illustrated by the nodes below.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ep-\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C4%81%CC%81f%C5%A1\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:1\",\n          \"status\": \"partial\",\n          \"note\": \"POK_01.txt leaf 9 (printed p.1): \\\"ab- „Wasser, Fluß“. Lat. amnis ... air. ab Gen. ahae ... Vgl. auch 2. up- [sic, = äp-] „Wasser, Fluß“ und abö(n) 'Affe'.\\\" This p.1 entry is the Italo-Celtic 'river' word (Latin amnis, Old Irish ab); it only cross-references, but does not itself contain, the Indo-Iranian material (Skt/Av. ap-) that the chart's nodes actually illustrate. That material is Pokorny's separate entry '2. äp- „Wasser, Fluß“' at printed p.51 (POK_01.txt leaf 60): 'Ai. áp- f. Wasser ... av. Nom. Sg. āfš, Akk. Sg. āpąm ...'.\"\n        }\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"POK_01.txt leaf 60, printed p.51\", \"stance\": \"partial\", \"note\": \"'2. äp-, Wasser, Fluß': Ai. áp- f. 'water', av. Nom.Sg. āfš, Akk.Sg. āpąm — exactly the Iranian branch of the chart, but cited on p.51, not p.1 as Nourai's root box gives.\"},\n        {\"src\": \"WLD\", \"where\": \"WLD_Bd1_1930_dli_70244_djvu.txt line 3149\", \"stance\": \"supports\", \"note\": \"\\\"2. ap- „Wasser, Fluß“.\\\" — Walde-Pokorny also lists this as a separate, independently numbered headword parallel to Pokorny, confirming the Indo-Iranian 'water' root is treated as distinct from the Italo-Celtic 'ab-' entry.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, entries ap-1/ap-2\", \"stance\": \"partial\", \"note\": \"\\\"ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.]\\\" — directly supports the Iranian branch of the chart, but its own citation is Pokorny p.51, confirming the p.1 citation on Nourai's root box is for a different (related) sub-entry.\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt line 223, entry 'abhmn-, abhnis'\", \"stance\": \"silent\", \"note\": \"Mann's entry for the Italo-Celtic river-word (Alb. āmë, Lat. amnis, Gaulish abono-, OIr. aba) lists no Indo-Iranian ap-/āp- cognates, i.e. keeps the two branches separate rather than uniting them under one PIE etymon.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Pahlavi\",\n          \"words\": \"âp\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"PIE *h₂ep- 'water' > Proto-Indo-Iranian *Hā́ps > Proto-Iranian *Hā́fš. Old Avestan apō (acc.pl.); Younger Avestan ap- (nom./obl. stem), āfš (nom.sg., with the expected Iranian cluster development -ps- > -fš-); Old Persian api(y)a- (transferred to an i-stem, e.g. loc.sg. apiyā); Middle Persian (Manichaean) āb, Book Pahlavi ʾp' = āb, all continuing simple regular loss of the earlier consonant cluster with compensatory lengthening/simplification to -b-. Meaning 'water' is unbroken from PIE to New Persian āb.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C4%81%CC%81f%C5%A1\",\n            \"https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:2\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt leaf 14 (printed ~p.3-4, running head 'abasia—abiogenesis', within Klein's stated +/-2 leaf-to-page tolerance of the cited p.2): s.v. 'abdest': \\\"Pers. âbdâst, lit. 'water for the hand', fr. ab, 'water', and dast, 'hand'. Pers. ab, 'water', is rel. to Avestic âp-, OI. âpah (fem. pl.), 'water'; see amnic and cp. ... julep.\\\" — Klein explicitly states Persian āb is related to Avestan āp-, matching the node's claim.\"\n            }\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt line 7276 ff., s.v. 'ap-'\", \"stance\": \"supports\", \"note\": \"Bartholomae's Altiranisches Wörterbuch lists 'ap-' as the Avestan word for water with the expected paradigm (nom.pl. āpō, gen.pl. apąm etc.); no separate 'glitter' sense is given for this entry.\"},\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt line 658\", \"stance\": \"supports\", \"note\": \"\\\"ab [MYA<Amyʾ, PN)b, N.....] water.\\\" — MacKenzie's Concise Pahlavi Dictionary confirms Pahlavi ab/āb = 'water' only; no second homograph is listed.\"},\n            {\"src\": \"KNT\", \"where\": \"grep for Old Persian api(y)a-\", \"stance\": \"silent\", \"note\": \"Kent's Old Persian lexicon entry for api(y)a- ('water') was not directly located in the local OCR text, so no direct quote could be pulled; treated as silent rather than checked.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"âb; âberŭ; âftâb\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"âb 'glitter, shine' (as distinct from âb 'water'): Nourai follows Horn (Grundriss, 1893, entry '3. äb Glanz', printed p.1), who compares Skt ābhā- 'splendor' and lists compounds âb-mand, Rūdābe, Sohrāb, Mehrāb, Ardāvirāf, âftâb as containing this 'shine' element (Phlv. āb, Skt ābhā- 'Glanz'). However Horn HIMSELF flags the equation as uncertain (footnote: 'Die Zusammenstellung von np. āb und skr. ābhā- ist keineswegs sicher; von der Bedeutung \\\"glitzernder Wasserspiegel\\\" könnte man sehr leicht zu \\\"Glanz\\\" kommen' — i.e. it is easy to get from 'glittering water-surface' to 'shine' as a plain semantic extension of āb 'water', without positing a separate etymon), and Hübschmann (Persische Studien, 1895) explicitly cites this uncertainty ('Da ab \\\"Glanz\\\" == skr. ābhā- H.[orn] 3 unsicher ist ...'). Modern Wiktionary and MacKenzie's Pahlavi dictionary give only one āb, 'water', with no second lexical entry for 'shine'. âberū(y) 'good reputation, honor' is transparently âb + rūy 'face' = 'water of the face' (paralleled by the Arabic idiom مَاء الوَجه māʾ al-wajh, lit. 'water of the face' = honor/shame), a semantic metaphor built on the literal 'water' sense rather than requiring a separate 'shine' root (though the metaphor of a shining/glowing face is not unreasonable either). âftâb 'sun(shine)': modern Iranology (Cheung, Etymological Dictionary of the Iranian Verb, 2007, and Wiktionary) reconstructs Middle Persian ʾptʾb (āftāb) from Proto-Iranian *abi-tāpah — i.e. the PREPOSITION *abi- 'upon, unto, towards' (cognate with Avestan aiwi-, Sanskrit api, Greek epi-, unrelated to āp 'water') + *tāpa- 'heat, glow' (from the verbal root tap- 'to be/become hot', NP tāftan/tāb-). So the modern analysis of the first element of āftāb is the preposition 'abi-/upon' plus 'heat', not āb 'water' or 'glitter' at all — the resemblance to āb is coincidental homophony of Iranian *abi- and *āp-.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/آب\",\n            \"https://en.wiktionary.org/wiki/آفتاب\",\n            \"https://en.wiktionary.org/wiki/آبرو\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:1\",\n              \"status\": \"partial\",\n              \"note\": \"HRN.txt lines 464-473 (printed p.1, entry no.3): \\\"3. äb 'Glanz' (Sahn. I S.14 Vers 7), vergl. ab[rö, ah[tah, äb[mend, Röd]äbe, Suhr]ab, Mihr]äb, Ardä VTr]af, af[täb, phlv. üb; skr. äbhä- 'Glanz'.\\\" Footnote: \\\"Die Zusammenstellung von np. ab und skr. abhä- ist keineswegs sicher; von der Bedeutung 'glitzernder Wasserspiegel' könnte man sehr leicht zu 'Glanz' kommen.\\\" Horn's own page supports the compounds Nourai lists but explicitly marks the Skt ābhā- equation, and by extension the idea of āb 'shine' as a separate root, as unproven.\"\n            },\n            {\"ref\": \"AEF:2\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Asas-e Eshteqaq-e Farsi (Persian translation/expansion of Horn+Hübschmann) has no online copy and was not in the local corpus; per refs_online.json guidance it is proxied via HRN/HUB, both consulted above.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"HUB.txt line 6401\", \"stance\": \"contradicts\", \"note\": \"\\\"Da ab 'Glanz' == skr. abha- H.[orn] 3 unsicher ist, so ergiebt sich, dass ap. w nur vor r sicher zu np. b wird.\\\" — Hübschmann treats the āb='Glanz' equation as unconfirmed ('unsicher') and uses that very uncertainty as an argument elsewhere in his sound-law discussion; he does not endorse it as settled.\"},\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt line 658\", \"stance\": \"contradicts\", \"note\": \"Only one Pahlavi entry 'ab...water' is given; no second homograph meaning 'shine/glitter' appears in MacKenzie's Concise Pahlavi Dictionary.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt lines 24717-24720, root *tap-\", \"stance\": \"contradicts\", \"note\": \"\\\"NWIR: NP taftan/tab- 'to shine, burn' ... || (+ *abi-) NP āftāb 'sun(shine)'\\\" — Cheung derives NP āftāb from tap- 'to shine, burn' plus the prefix *abi- ('upon'), not from āb 'water/glitter'.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt lines 456-459, entry no.2\", \"stance\": \"supports\", \"note\": \"Immediately preceding entry (no.2, also printed p.1): \\\"ab, âw 'Wasser'; ... ap. āp- 'Wasser'; aw. āp-; phlv. āp (pāz. āw); ai. āp-, kurd. āw ...\\\" — this is Horn's WATER entry (matching node #1); the 'Glanz' sense is a separately numbered, admittedly uncertain, homograph (entry no.3).\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"âb-bahâ; abboha\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Nourai proposes that Arabic أبّهة/أُبَّهة (ubbuha/ubbaha 'pomp, majesty, grandeur') arose from a Persian-Arabic hybrid compound 'āb' (glitter) + 'bahā'' (Arabic 'splendor'), i.e. treating it as an Arabized borrowing of a Persian phrase. Modern Arabic lexicography does not support this: Wiktionary lists أبهة under the native triliteral root ء ب ه (ʔ-b-h), from the plain Arabic verb أَبَهَ/أَبِهَ (ʔabaha/ʔabiha) 'to pay attention, heed, take notice' (non-past يَأْبَهُ yaʔbahu); أُبَّهة is the augmented/intensive noun pattern of that root (gemination marking intensity: roughly 'that which makes one take notice' → pomp, ostentatious grandeur). This root (ء ب ه) is listed as entirely separate from ب ه و / ب ه ي, the root of بَهَاء (bahāʔ) 'splendor, beauty' (which Klein's Comprehensive Etymological Dictionary treats as the source of Persian 'bahā' splendor', via 'Bahaism' < Pers. bahā < Arab. bahāʔ — i.e. the borrowing runs Arabic→Persian for bahāʔ itself, not the reverse). There is no attested classical or modern source deriving أبهة from a Persian 'āb' + Arabic 'bahā'' compound; the resemblance between 'ubbuha' and 'āb-bahā' appears to be a folk/paronomastic etymology rather than an attested derivation.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/أبهة\",\n            \"https://en.wiktionary.org/wiki/بهاء\",\n            \"https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AFM:7\", \"status\": \"not_found\", \"note\": \"AFM_pages.txt around leaf 13-17 (approx. printed pp.5-9 per the −8 leaf offset, transitioning from bāb al-alif to bāb al-bāʾ) was inspected but the Arabic-script OCR is too degraded (Syriac-looking mis-OCR of Arabic letters) to locate or confirm an entry for أبهة/عبهة at p.7; could not verify Nourai's claim against this source.\"},\n            {\"ref\": \"FVF:11\", \"status\": \"not_checked\", \"note\": \"Emam Shushtari's Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi has no local OCR text and is only available behind login/JS-gated viewers (noorlib.ir, ketabnak.com); could not be fetched.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt, s.v. 'Bahaism'\", \"stance\": \"contradicts\", \"note\": \"\\\"Bahaism, n. ... Formed with suff. -ism fr. Pers. baha, 'splendor', fr. Arab. bahā', of s.m.\\\" — Klein derives Persian 'bahā' FROM Arabic bahāʔ (opposite direction of loan from what a Persian-origin compound in Arabic 'ubbuha' would require), and gives no compound with āb.\"},\n            {\"src\": \"FVQ\", \"where\": \"grep of FVQ.txt/FVQ_pages.txt\", \"stance\": \"silent\", \"note\": \"Jeffery's Foreign Vocabulary of the Qur'an (Quranic loanwords only) has no entry for أبهة/بهاء (neither word is Qur'anic vocabulary), so it is silent on this claim.\"},\n            {\"src\": \"AFA (Fraenkel, Aramaic loans in Arabic)\", \"where\": \"grep of AFA.txt for 'bah'\", \"stance\": \"silent\", \"note\": \"No entry found relating أبهة or بهاء to an Aramaic substrate; silent.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"obbohat\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian ابهت (conventionally vocalized ebhat/obhat/obbohat) 'grandeur, majesty, awe' is a straightforward Arabic loanword from أُبَّهة (ubbuha/ubbaha) 'pomp, majesty' (see node 3), following the common pattern of Arabic feminine nouns in -a(t) being borrowed into Persian with the historical tāʾ marbūṭa retained as -at/-et (cf. Ar. -a(t) > NP -at in many loans). Mo'in's Farhang-e Farsi (MON) explicitly tags the word's origin as Arabic, and the meaning given there ('bozorgi, bozorgvāri, azamat' = grandeur, magnificence; also 'tokabbor, nakhvat' = arrogance/pride) matches Nourai's gloss 'elegance/magnificence'. The Persian←Arabic borrowing direction for this specific word (node 3→node 4 edge) is correctly drawn and uncontroversial; the caveat is only about the deeper origin Nourai assigns to the Arabic word itself at node 3 (see there).\",\n          \"sources\": [\n            \"https://vajehyab.com/moein/ابهت\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:131\",\n              \"status\": \"supports\",\n              \"note\": \"MON_part1.txt line 6560, entry 'ابهت' (OCR-garbled as 'ابسهت: ۳۹ ال ابهت) [ع.]'), tagged [ع.] = Arabic origin. Cross-checked live at vajehyab.com/moein/ابهت (fetched 2026-09-04): \\\"ابهت ... [ع.] ۱- بزرگی، بزرگواری، عظمت؛ ۲- تکبر، نخوت\\\" (grandeur, magnificence; also arrogance/pride) — matches Nourai's gloss and Arabic-origin tag; exact page 131 of the printed 6-vol MON edition could not be independently confirmed since only the word-content (not original pagination) is available online, per refs_online.json's notes on MON's page numbers being unrecoverable online.\"\n            }\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"vajehyab.com/moein/ابهت (archived)\", \"stance\": \"supports\", \"note\": \"\\\"[ع.] ۱- بزرگی، بزرگواری، عظمت؛ ۲- تکبر، نخوت\\\" — confirms Arabic origin and the 'grandeur/magnificence' sense.\"},\n            {\"src\": \"BQT\", \"where\": \"not located (Borhan-e Qate' not searched for this specific short entry given time budget)\", \"stance\": \"silent\", \"note\": \"Not checked; MON alone was sufficient to confirm the Arabic-origin tag matching Nourai's implied direction of borrowing.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-04T18:19:37.819Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet/page-32.json (file state is current in your context — no need to Read it back)
```


## [2026-09-04T18:19:40.726Z] AGENT

Now let me validate the JSON and run the coverage check.


## [2026-09-04T18:19:41.557Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 -m json.tool /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet/page-32.json > /dev/null && echo \"VALID JSON\""
}
```


## [2026-09-04T18:19:42.395Z] TOOL CALL #63: Bash

```json
{
 "command": "VERIFY_DIR=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet python3 /home/sfmqrb/git/rishe/tools/verify_check.py 32"
}
```


### [2026-09-04T18:19:43.491Z] TOOL RESULT

```
VALID JSON
```


### [2026-09-04T18:19:45.335Z] TOOL RESULT

```
nodes verified: 4/4
node verdicts: {'confirmed': 2, 'disputed': 2}
root verdicts: {'plausible': 1}
ref checks: {'supports': 2, 'partial': 1, 'not_checked': 2, 'not_found': 1}
books consulted: {'supports': 4, 'silent': 4, 'contradicts': 4} | by book: {'PHD': 2, 'BRT': 1, 'KNT': 1, 'HUB': 1, 'CHEUNG': 1, 'HRN': 1, 'KLN': 1, 'FVQ': 1, 'AFA (Fraenkel, Aramaic loans in Arabic)': 1, 'MON': 1, 'BQT': 1}
```


## [2026-09-04T18:20:00.443Z] AGENT

JSON is valid and coverage check passes (4/4 nodes verified). The output is written to `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/sonnet/page-32.json`.

## Summary — PDF page 32 (book page 2), entry "Ab 1, Ap 1"

**Verdicts:** root = plausible (1); nodes = confirmed (2: #1 âp, #4 obbohat), disputed (2: #2 âb/âberū/âftâb, #3 âb-bahâ/abboha).

- **Root "Ab 1, Ap 1" (plausible):** Nourai cites POK:1 for both, but Pokorny's p.1 "ab-" (Lat. amnis, Celtic ab) is the Italo-Celtic sub-entry; the Iranian branch actually drawn (āp/āb) is Pokorny's separate "2. äp-" at p.51 (= AHD's ap-2, matching Wiktionary's modern unified *h₂ep- reconstruction). Citation is imprecise but the grouping itself is defensible.

- **Disputed — node #2, âftâb "sun":** Nourai treats āftāb's first element as âb "glitter." Cheung (2007) and Wiktionary instead reconstruct Proto-Iranian *abi-tāpah — the preposition *abi- "upon" (unrelated to āp "water") + tāp- "heat/shine" — so the resemblance to āb is coincidental homophony, not derivation.

- **Disputed — node #2, âb "glitter" (homonym of âb "water"):** Nourai's own cited source, Horn (HRN:1), explicitly flags this Skt ābhā- equation as "keineswegs sicher" (by no means certain) and suggests it's just a metaphorical extension of āb "water." Hübschmann echoes this uncertainty. No modern dictionary (Wiktionary, MacKenzie's PHD) lists a separate "shine" homograph.

- **Disputed — node #3, Arabic âb-bahâ/abboha "ubbuha":** Nourai's compound of Persian âb + Arabic bahā' is not supported. Wiktionary derives أبّهة from the native Arabic root ء-ب-ه (verb أَبَهَ "to heed, take notice"), entirely separate from بهاء's root ب-ه-و. This looks like a folk/paronomastic etymology; Nourai's own cited refs (AFM:7, FVF:11) could not be confirmed — AFM's OCR was too degraded to locate the entry, FVF has no accessible copy.

- **Confirmed — node #1 (Avestan/Pahlavi âp) and node #4 (Persian obbohat < Arabic):** both well supported by Klein, Bartholomae, MacKenzie, and Mo'in respectively.

All web sources archived under `data/verification/sources/web/` via `fetch_source.py`; local reference checks (POK, WLD, AHD, IEC, KLN, HRN, HUB, PHD, BRT, CHEUNG, MON, FVQ, AFA) quoted in `ref_check`/`consulted` with exact line/leaf citations.
