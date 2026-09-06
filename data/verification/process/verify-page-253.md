# Verification process log — verify-page-253


## [2026-09-06T16:04:41.619Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 253 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-253.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-253.json. Write /home/sfmqrb/git/rishe/data/verification/page-253.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 253` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T16:04:43.120Z] AGENT

I'll start by reading the instructions and the relevant files.


## [2026-09-06T16:04:43.830Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T16:04:43.847Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which this
5	repository (`/home/sfmqrb/git/rishe`) turned into JSON (`data/extracted/batch/page-<pdf>.json`).
6	Compact text renderings of the charts are in
7	`/home/sfmqrb/git/rishe/data/verification/agent/charts/page-<pdf>.txt`.
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
38	   - `transcription_suspect` — the form in the JSON is not what the sources know (a misread
39	     letter, an impossible form, a wrong Persian script). See "Transcription flags" below:
40	     you must check the printed page and say whether the book or the extraction is at fault.
41	4. Record sources as URLs (Wiktionary page, Etymonline page, AHD appendix entry, archive.org
42	   page of Klein/Horn/Bartholomae, etc.). Also note when Nourai's own cited reference
43	   (KLN, POK, AHD, BQT, MON, HRN, HUB…) is itself the modern standard for that claim.
44	
45	## Checking Nourai's OWN cited references (required)
46	
47	Every node carries `refs=` — Nourai's citations, e.g. `KLN:164; FVQ:75` (abbreviation:page;
48	`MON5:528` = MON vol. 5 p. 528). The author claims each arrow is supported by those pages.
49	You must check them:
50	
51	- The bibliography key (abbreviation → book), where each reference can be read, page
52	  offsets and lookup hints: `/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json`
53	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`, `scans`, `cites`).
54	- If `local_file` is set, the OCR text of that book is on disk under
55	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/`: grep it for the headword (try
56	  several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and, if a page
57	  offset is given, locate the cited page (pages are separated by form-feeds; `_pages.txt`
58	  files also carry `[pdf page N]` tags; use `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one
59	  page). Read the entry and judge whether it actually says what Nourai's arrow says.
60	- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
61	  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
62	  NOT OCR whole books. Fetch only the cited page:
63	  `python3 /home/sfmqrb/git/rishe/tools/ref_page.py BQT:918 --image`
64	  It renders that one page to PNG, OCRs it (Persian OCR is rough), caches both under
65	  `data/verification/sources/refs/ocr/`, and prints the text plus the PNG path. If the OCR
66	  is unreadable, Read the PNG (you can read Persian print directly), and then SAVE what you
67	  read: write the entry/entries you used (headword, Mo'in's etymological footnote, and any
68	  surrounding lines you relied on) verbatim to the companion file
69	  `data/verification/sources/refs/ocr/<ABBR>/<page>.vision.txt` (the tool prints the exact
70	  paths). The tool prefers that file next time, so nobody pays for reading the image again.
71	  If the printed page number on the image is off, re-run with `--pdf-page <n>` adjusted, and
72	  note the correct pdf page in your ref_check note. Borhan vol. 5 (the addenda, own
73	  pagination 1–290) is reached only as `BQT5:<page>`; Borhan vols 1–2 exist as OCR text
74	  files (`BQT_v1_pages.txt`, `BQT_v2_pages.txt`), vols 3–5 as `BQT_v3/4/5_pages.txt` too.
75	- If `kind` is `website`, use the `lookup_hint` URL pattern with WebFetch (e.g. Mo'in via
76	  vajehyab.com / abadis.ir).
77	- Do this for at least ONE cited reference per node (the most authoritative available:
78	  POK/AHD/KLN for IE roots, HRN/HUB/BRT/KNT/PHD for Iranian, KLN/FVQ/AFM/PLA for Semitic,
79	  BQT/MON for Persian). If none of a node's references is accessible, say so.
80	
81	Add to every node a `ref_check` array:
82	
83	```json
84	"ref_check": [
85	  {"ref": "KLN:164", "status": "supports", "note": "Klein p.164 s.v. 'cherub': Heb. kerūbh, prob. rel. to Akkad. karābu 'to bless', metathesis of b-r-k — exactly Nourai's claim."},
86	  {"ref": "FVQ:75", "status": "not_checked", "note": "no online copy"}
87	]
88	```
89	
90	`status` ∈ `supports` (the page says what the arrow says) · `partial` (the reference has the
91	word but a different/looser derivation) · `contradicts` (the reference says something else)
92	· `not_found` (checked the text, could not find the entry/page) · `not_checked` (reference
93	not accessible online). Quote the key phrase of the reference in `note` when you can, with
94	the file/leaf/page where you found it.
95	
96	Also add to each entry a root-level `ref_check` for the root's own refs (e.g. `POK:244`).
97	
98	## Use EVERY relevant book on disk (required)
99	
100	Checking only the reference Nourai cites is not enough. For every node, also consult the
101	other books in the local library that could speak to that claim, and record what each says.
102	The list of which books cover which kind of node, with file paths, is
103	`/home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md`. Minimum per node:
104	
105	- an Indo-European node or root box: Pokorny (POK) AND Walde-Pokorny (WLD) AND Watkins/AHD,
106	  plus Mann (IEC) or Buck (SYN) when the word is a common noun;
107	- an Avestan / Old Persian node: Bartholomae (BRT) or Kent (KNT);
108	- a Pahlavi / Middle Persian node: MacKenzie (PHD) and Nyberg (NYB);
109	- a New Persian node: Horn (HRN), Hübschmann (HUB), Cheung (CHEUNG, for verbs), Borhan-e
110	  Qate' with Mo'in's footnotes (BQT), Mo'in (MON), and Aryanpur (ARY);
111	- a Sogdian node: Gharib (SOD); a Khotanese one: Bailey (ISS_alt_DKS);
112	- an Arabic node or a Persian/Arabic loan in either direction: Klein (KLN), Jeffery (FVQ),
113	  Addi Shir (AFM), Asbaghi (PLA), Fraenkel (AFA), Lokotsch (LKT); for French/Spanish
114	  Arabisms Pihan (PHN), Devic (DEV), Lammens (LAM), Dozy (DOZ);
115	- an English / Romance node: Klein (KLN), Skeat (SKT), Funk & Wagnalls (FSD), Webster (WEB);
116	  Anglo-Indian words: Hobson-Jobson (HJB), Whitworth (AID);
117	- a Turkic node: Vámbéry (TTS), Lokotsch (LKT).
118	
119	Grep each file for the headword (several spellings; Latin transliteration for the Western
120	books, Persian script for BQT/MON/ARY, Pahlavi transliteration for PHD/NYB). A grep that
121	finds nothing is also a result ("silent"). Record everything in a `consulted` array on the
122	node (separate from `ref_check`, which is only for the references Nourai himself cites):
123	
124	```json
125	"consulted": [
126	  {"src": "HRN", "where": "no. 3, p. 1", "stance": "contradicts", "note": "Horn separates āb 'Glanz' from āb 'water' and derives āftāb from the former"},
127	  {"src": "PHD", "where": "p. 5 s.v. ābād", "stance": "supports", "note": "'ābād [ʾpʾt] populous, thriving' — no water element"},
128	  {"src": "WLD", "where": "Bd. I p. 46", "stance": "silent", "note": "root ap- listed, no Persian compound"}
129	]
130	```
131	
132	`stance` ∈ supports / contradicts / partial / silent. Quote the key phrase. Books consulted
133	via the web (vajehyab for Mo'in, AHD online) go here too, with the URL archived via
134	fetch_source.py and listed in `sources`. Every node must have at least two `consulted`
135	entries from different books whenever the matrix lists two or more books for its language.
136	
137	## Transcription flags: say WHERE the error is (required)
138	
139	For every node you mark `transcription_suspect`, look at the printed page itself — render it
140	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
141	(or open `site/pages/<pdf page>.jpg`) and Read the image — and add to the node:
142	
143	```json
144	"error_in": "book",            // "book" = the printed book has the odd form (author's misprint); the extraction is faithful
145	                               // "extraction" = the book prints the correct form; the JSON misread it
146	                               // "unknown" = could not decide from the image
147	"book_prints": "borrāgō",      // what the printed page actually shows
148	"correct_form": "borrāgō"      // the form that should stand (per the sources)
149	```
150	
151	Usually the extraction is faithful and the problem is in the book itself; say so plainly in
152	`derivation` too ("the book prints X; this is Nourai's misprint for Y"). Only when the JSON
153	differs from the page is it an extraction error (report those separately in your summary — the
154	owner fixes the data). Copy the page PNG you relied on to
155	`data/verification/sources/refs/ocr/BOOK/<pdf page>.png` so the check can be audited.
156	
157	## Persian explanation (required): `derivation_fa` on every node, `note_fa` on every root
158	
159	Write the derivation a second time IN PERSIAN, for a Persian reader — not a translation of the
160	English sentence. Think about how a Persian etymologist (حسن‌دوست، ابوالقاسمی، معین در حواشی
161	برهان قاطع) would explain it to an educated Persian reader:
162	
163	- Use the established Persian terminology: هندواروپایی آغازین، ایرانی باستان، اوستایی، پارسی
164	  باستان، فارسی میانه (پهلوی)، پارتی، سغدی، فارسی نو/دری؛ وام‌واژه، وام‌گیری، دگرگونی آوایی،
165	  قلب (metathesis)، ابدال، همگونی، پیشوند، پسوند، ریشه، ستاک، تحول معنایی، معرّب، ریشه‌شناسی
166	  عامیانه (folk etymology)، هم‌ریشه (cognate)، دوگانه (doublet).
167	- Give the Persian word first in Persian script, then the older forms in Latin transliteration
168	  as Persian philology does (e.g. «آب» از فارسی میانهٔ āb / āp، از ایرانی باستان *āp-، هم‌ریشه با
169	  سنسکریت āp-). Persian-script forms for Arabic words; Greek/Latin words in Latin letters.
170	- Explain the sound changes in the way a Persian reader expects (e.g. «پ ایرانی باستان در میان
171	  دو واکه در فارسی میانه به ب نرم شده»؛ «ای کشیدهٔ فارسی میانه در فارسی نو به ی بدل شده»).
172	- Say clearly, in Persian, what the verdict means for the reader: ادعای نورایی درست است / با
173	  احتیاط پذیرفتنی است / پژوهش امروزی آن را رد می‌کند و به جای آن … می‌گوید / خطای چاپی کتاب /
174	  خطای خوانش اسکن.
175	- Keep it 2–5 sentences, formal but readable (نه ترجمهٔ لفظ‌به‌لفظ، نه ماشینی). Numbers in
176	  Persian digits are fine. Mention the key sources by their Persian-usable names (پوکورنی،
177	  بارتولومه، هرن، هوبشمان، مکنزی، نیبرگ، چونگ، معین، برهان قاطع، ویکی‌واژه).
178	
179	Field names: `derivation_fa` (node) and `note_fa` (root entry). Both required.
180	
181	## Process documentation (required)
182	
183	The owner wants to be able to audit every step later. Therefore:
184	
185	- **Every web page you rely on must be archived**: after you read a page (WebFetch or
186	  curl), run
187	  `python3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
188	  This stores the page as text under `data/verification/sources/web/` and indexes it. Only
189	  URLs that were archived this way may appear in a `sources` array. (Batch several calls in
190	  one Bash command to save time.)
191	- **Every lookup in a local reference text must be quoted**: in `ref_check[].note` and
192	  `consulted[].note` include the exact phrase(s) you found (with the grep pattern or page you
193	  used), so the finding can be re-run.
194	- Your full transcript (every tool call and result) is exported automatically by the
195	  coordinator; nothing else needed for that.
196	
197	## Sources to use (in roughly this order)
198	
199	- **Wiktionary** (en.wiktionary.org) — has the best coverage of Persian, Middle Persian,
200	  Avestan, Old Persian, Sogdian, Arabic etymologies, with citations (Cheung 2007, Hasandust,
201	  MacKenzie 1971, Bartholomae, Horn, Hübschmann, Nourai himself). Fetch the word's page AND
202	  the `Reconstruction:Proto-Indo-European/…` / `Reconstruction:Proto-Iranian/…` pages.
203	  Use URL-encoded Persian/Arabic script for those pages.
204	- **Etymonline** (etymonline.com/word/<word>) for English/French/Latin/Greek chains.
205	- **American Heritage Dictionary IE roots** (ahdictionary.com/word/indoeurop.html or
206	  ahdictionary.com/word/search.html?q=<root>) — Nourai's "AHD" citations refer to the 1975
207	  appendix; the online appendix is the updated edition of the same list (local: Watkins 1985).
208	- **Pokorny** — local OCR (POK_01/02/03, POK_full) or indo-european.info / starlingdb.org;
209	  Nourai's "POK:nnn" is a page number in Pokorny's IEW.
210	- **Klein**, **Horn**, **Hübschmann**, **MacKenzie**, **Bartholomae**, **Kent**, **Nyberg**,
211	  **Mann**, **Buck**, **Walde-Pokorny**, **Jeffery**, **Addi Shir**, **Asbaghi**, **Lokotsch**,
212	  **Gharib**, **Cheung**, **Aryanpur** … are all on disk (see SOURCE_MATRIX.md).
213	- **Encyclopaedia Iranica** (iranicaonline.org) for historical/cultural routes.
214	- **Nişanyan Sözlük** (nisanyansozluk.com) for Turkish; **Lisān al-ʿArab** / Wiktionary for Arabic.
215	- Use WebSearch when you don't know the right page; use WebFetch to read a page.
216	
217	Do NOT fabricate sources. If a page did not load or didn't help, don't cite it.
218	If a chain is well known and uncontroversial (e.g. Latin → Old French → English), one good
219	source covering the chain is enough; spend your effort on the Iranian and Semitic links,
220	which are where errors are likelier.
221	
222	## Output — write ONE file per page
223	
224	Write `/home/sfmqrb/git/rishe/data/verification/page-<pdf>.json` (UTF-8, no BOM):
225	
226	```json
227	{
228	  "pdf_page": 126,
229	  "book_page": 96,
230	  "verified_by": "claude-opus-5",
231	  "verified_on": "2026-09-05",
232	  "entries": [
233	    {
234	      "entry": 0,
235	      "root": "Dheigh, Dhigha",
236	      "verdict": "confirmed",
237	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
238	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
239	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
240	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
241	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
242	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
243	      "nodes": [
244	        {
245	          "id": 6,
246	          "lang": "Avestan",
247	          "words": "pairi-daeza",
248	          "verdict": "confirmed",
249	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
250	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
251	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
252	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
253	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
254	        }
255	      ]
256	    }
257	  ]
258	}
259	```
260	
261	Rules:
262	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
263	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
264	- `words` = the transliterations of the node joined by "; " (copy from the chart).
265	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
266	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
267	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
268	- If a node lists several words, cover each word; if they differ in verdict, use the worst
269	  verdict for the node and explain per word in `derivation`.
270	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
271	  scholarship takes.
272	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
273	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
274	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
275	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
276	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
277	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
278	  any extraction errors (JSON differs from the printed page) the owner must fix.
279	  Do not paste the JSON back into your reply.
280	
```


## [2026-09-06T16:04:44.630Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-253.txt"
}
```


## [2026-09-06T16:04:44.638Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-253.json"
}
```


### [2026-09-06T16:04:44.648Z] TOOL RESULT

```
1	{
2	  "pdf_page": 253,
3	  "book_page": 223,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Kelewo, Kalwo",
8	        "lang": "Indo-European",
9	        "refs": "POK:554; KLN:226",
10	        "gloss": "lacking, bald"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Sogdian",
17	          "refs": "SLW:10.1.96",
18	          "words": [
19	            {"translit": "krw`", "gloss": "empty, lacking", "script": null}
20	          ],
21	          "script_extra": null,
22	          "note": "the link is note quite certain",
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Persian",
29	          "refs": "BQT:1631",
30	          "words": [
31	            {"translit": "karveh", "gloss": "tooth cavity", "script": "کَروه ۲"}
32	          ],
33	          "script_extra": null,
34	          "note": null,
35	          "quote": {
36	            "text": "باز چون بر گرفت دست زروی - کروه دندان و پشت چوگان‌است",
37	            "poet": "Rŭdakî"
38	          }
39	        },
40	        {
41	          "id": 3,
42	          "parent": 0,
43	          "lang": "Avestan",
44	          "refs": "POK:554; KLN:226",
45	          "words": [
46	            {"translit": "kaurva", "gloss": "bald", "script": null}
47	          ],
48	          "script_extra": null,
49	          "note": null,
50	          "quote": null
51	        },
52	        {
53	          "id": 4,
54	          "parent": 3,
55	          "lang": "Persian",
56	          "refs": "BQT:1665; POK:554",
57	          "words": [
58	            {"translit": "kal", "gloss": "bald", "script": "کَل"}
59	          ],
60	          "script_extra": "کچل",
61	          "note": null,
62	          "quote": null
63	        },
64	        {
65	          "id": 5,
66	          "parent": 0,
67	          "lang": "Latin",
68	          "refs": "AHD; KLN:226",
69	          "words": [
70	            {"translit": "calvus", "gloss": "bald", "script": null},
71	            {"translit": "calvaria", "gloss": "skull, smooth hill", "script": null}
72	          ],
73	          "script_extra": null,
74	          "note": null,
75	          "quote": null
76	        },
77	        {
78	          "id": 6,
79	          "parent": 5,
80	          "lang": "English",
81	          "refs": null,
82	          "words": [
83	            {"translit": "Calvary", "gloss": "the hill where Jesus was crucified", "script": null},
84	            {"translit": "Calvin", "gloss": "male name", "script": null}
85	          ],
86	          "script_extra": null,
87	          "note": null,
88	          "quote": null
89	        }
90	      ]
91	    },
92	    {
93	      "root": {
94	        "name": "Kem 1",
95	        "lang": "Indo-European",
96	        "refs": "POK:556",
97	        "gloss": "stick"
98	      },
99	      "nodes": [
100	        {
101	          "id": 1,
102	          "parent": 0,
103	          "lang": "Avestan",
104	          "refs": "POK:556; AHM:274",
105	          "words": [
106	            {"translit": "simâ", "gloss": "yoke beam", "script": null},
107	            {"translit": "simôithrâ", "gloss": "ring beneath horse's neck", "script": null}
108	          ],
109	          "script_extra": null,
110	          "note": null,
111	          "quote": null
112	        },
113	        {
114	          "id": 2,
115	          "parent": 1,
116	          "lang": "Persian",
117	          "refs": "HRN:168; BQT:1205; AHM:274",
118	          "words": [
119	            {"translit": "sîm 1", "gloss": "yoke beam", "script": "سیم ۱"}
120	          ],
121	          "script_extra": null,
122	          "note": null,
123	          "quote": null
124	        }
125	      ]
126	    },
127	    {
128	      "root": {
129	        "name": "Kem 2",
130	        "lang": "Indo-European",
131	        "refs": "POK:556; CEL6:122",
132	        "gloss": "to cover"
133	      },
134	      "nodes": [
135	        {
136	          "id": 1,
137	          "parent": 0,
138	          "lang": "Greek",
139	          "refs": "VDQ:352",
140	          "words": [
141	            {"translit": "kamision", "gloss": "shirt", "script": null}
142	          ],
143	          "script_extra": null,
144	          "note": null,
145	          "quote": null
146	        },
147	        {
148	          "id": 2,
149	          "parent": 1,
150	          "lang": "Latin",
151	          "refs": "POK:556",
152	          "words": [
153	            {"translit": "camisia", "gloss": "shirt", "script": null}
154	          ],
155	          "script_extra": null,
156	          "note": null,
157	          "quote": null
158	        },
159	        {
160	          "id": 3,
161	          "parent": 2,
162	          "lang": "Arabic",
163	          "refs": "VDQ:352; OXF:209",
164	          "words": [
165	            {"translit": "qamîs", "gloss": "cotton shirt", "script": null}
166	          ],
167	          "script_extra": null,
168	          "note": null,
169	          "quote": null
170	        },
171	        {
172	          "id": 4,
173	          "parent": 3,
174	          "lang": "Persian",
175	          "refs": "MON:2729",
176	          "words": [
177	            {"translit": "qamîs", "gloss": "cotton shirt", "script": "قمیص"}
178	          ],
179	          "script_extra": "قمیصه",
180	          "note": null,
181	          "quote": null
182	        },
183	        {
184	          "id": 5,
185	          "parent": 3,
186	          "lang": "English",
187	          "refs": "OXF:209",
188	          "words": [
189	            {"translit": "kameez", "gloss": "shirt", "script": null}
190	          ],
191	          "script_extra": null,
192	          "note": null,
193	          "quote": null
194	        },
195	        {
196	          "id": 6,
197	          "parent": 2,
198	          "lang": "Old French",
199	          "refs": "AHD:230",
200	          "words": [
201	            {"translit": "chemise", "gloss": "shirt, cover", "script": null}
202	          ],
203	          "script_extra": null,
204	          "note": null,
205	          "quote": null
206	        },
207	        {
208	          "id": 7,
209	          "parent": 6,
210	          "lang": "Persian",
211	          "refs": "MON:2079",
212	          "words": [
213	            {"translit": "šomîz", "gloss": "file folder", "script": "شمیز"}
214	          ],
215	          "script_extra": null,
216	          "note": null,
217	          "quote": null
218	        },
219	        {
220	          "id": 8,
221	          "parent": 6,
222	          "lang": "English",
223	          "refs": "AHD:193",
224	          "words": [
225	            {"translit": "camisa, chemise, chemisette", "gloss": null, "script": null}
226	          ],
227	          "script_extra": null,
228	          "note": null,
229	          "quote": null
230	        }
231	      ]
232	    }
233	  ]
234	}
235	
```


### [2026-09-06T16:04:44.658Z] TOOL RESULT

```
1	=== PDF page 253 (book page 223) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kelewo, Kalwo : lacking, bald  (refs POK:554; KLN:226)
4	#1 (parent #0) [Sogdian] refs=SLW:10.1.96 | krw` : empty, lacking | NOTE: the link is note quite certain
5	  #2 (parent #1) [Persian] refs=BQT:1631 | karveh «کَروه ۲» : tooth cavity
6	#3 (parent #0) [Avestan] refs=POK:554; KLN:226 | kaurva : bald
7	  #4 (parent #3) [Persian] refs=BQT:1665; POK:554 | kal «کَل» : bald | extra: کچل
8	#5 (parent #0) [Latin] refs=AHD; KLN:226 | calvus : bald ; calvaria : skull, smooth hill
9	  #6 (parent #5) [English] refs=None | Calvary : the hill where Jesus was crucified ; Calvin : male name
10	--- entry 1 ---
11	ROOT [Indo-European] Kem 1 : stick  (refs POK:556)
12	#1 (parent #0) [Avestan] refs=POK:556; AHM:274 | simâ : yoke beam ; simôithrâ : ring beneath horse's neck
13	  #2 (parent #1) [Persian] refs=HRN:168; BQT:1205; AHM:274 | sîm 1 «سیم ۱» : yoke beam
14	--- entry 2 ---
15	ROOT [Indo-European] Kem 2 : to cover  (refs POK:556; CEL6:122)
16	#1 (parent #0) [Greek] refs=VDQ:352 | kamision : shirt
17	  #2 (parent #1) [Latin] refs=POK:556 | camisia : shirt
18	    #3 (parent #2) [Arabic] refs=VDQ:352; OXF:209 | qamîs : cotton shirt
19	      #4 (parent #3) [Persian] refs=MON:2729 | qamîs «قمیص» : cotton shirt | extra: قمیصه
20	      #5 (parent #3) [English] refs=OXF:209 | kameez : shirt
21	    #6 (parent #2) [Old French] refs=AHD:230 | chemise : shirt, cover
22	      #7 (parent #6) [Persian] refs=MON:2079 | šomîz «شمیز» : file folder
23	      #8 (parent #6) [English] refs=AHD:193 | camisa, chemise, chemisette
24	
```


## [2026-09-06T16:04:48.693Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md | head -120",
 "description": "Read source matrix"
}
```


### [2026-09-06T16:04:48.732Z] TOOL RESULT

```
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
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt`
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
- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt`
- **FSF** — Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt`
- **HENNING** — HENNING
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HENNING_selected_papers.txt`
- **EAV** — J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/EAV_studies.txt`
- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ISS_alt_DKS.txt`
- **AHM** — I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt`
- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt`
- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AVG.txt`
- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HID.txt`
- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt`
- **TLM** — H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Seri
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TLM.txt`
- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/UNV.txt`
- **SBK** — M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
```


## [2026-09-06T16:04:51.485Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SLW','BQT','AHD','HRN','AHM','MON','VDQ','OXF','CEL','WLD','BRT','PHD','NYB','HUB','ARY','SKT','FSD','WEB','IEC','SYN','FVQ','PLA','AFM','LKT','DEV','PHN','SOD','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-06T16:04:53.353Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SLW {"title": "W. B. Henning, 'Sogdian Loan-Words in New Persian', BSOAS 10.1 (1939) pp. 93-106", "edition_found": "reprint in W. B. Henning Selected Papers I (Acta Iranica 14, 1977) - different pagination; original in JSTOR", "kind": "archive_djvu", "url": "https://archive.org/details/w.-b.-henning-selected-papers", "identifier": "w.-b.-henning-selected-papers (also w.-b.-henning-selected-papers_2021
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
AHM {"title": "I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959", "edition_found": "1959", "kind": "archive_djvu", "url": "https://archive.org/details/gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university", "identifier": "gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt", "page_offset": 
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaSc
OXF {"title": "J. Speake, Oxford Dictionary of Foreign Words and Phrases, New York 1997", "edition_found": "1997 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/oxforddictionary00spea ; isbn_9780965016070 (lending) ; Google Nvu17oLIQNgC = 2008 2nd ed. preview only", "identifier": "oxforddictionary00spea (also isbn_9780965016070)", "local_file": null, "page_offset": n
CEL {"title": "S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, 6 vols., Milton MA 1997", "edition_found": null, "kind": "catalog", "url": "HathiTrust mdp.39015021572337 etc. (8-vol 1986- ed., search-only) ; Open Library records", "identifier": null, "local_file": null, "page_offset": null, "lookup_hint": null, "notes": "RE-SEARCH 2026-09: catalogue only; the 1997 Sverge Ha
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verific
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
CHEUNG MISSING
```


## [2026-09-06T16:05:11.879Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SLW','AHM','HRN','BQT','MON','AHD','SOD','WLD','IEC','SYN','SKT','LEW','LAT','FSD','WEB','ARY','BRT','PHD','NYB','HUB','FVQ','PLA','AFM','LKT','DEV','PHN','OXF','VDQ']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print('==',k, '| offset:', v.get('page_offset'), '| local:', v.get('local_file'))\n    print('   hint:', (v.get('lookup_hint') or '')[:300])\n\"",
 "description": "Print page offsets and hints"
}
```


## [2026-09-06T16:05:12.408Z] TOOL CALL #7: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && head -60 data/verification/page-202.json",
 "description": "Look at existing verification output format"
}
```


### [2026-09-06T16:05:13.647Z] TOOL RESULT

```
== POK | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
   hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== KLN | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
   hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== SLW | offset: Selected Papers scan: leaf = p + 12 for the front matter; reprinted articles keep the ORIGINAL journal page numbers in the margins, so grep 'Sogdian Loan' then the original page number (93-106). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HENNING_selected_papers.txt
   hint: Original: JSTOR https://www.jstor.org/stable/608123 (BSOAS 10.1) - search jstor for 'Sogdian Loan-Words in New Persian'. In the local text grep -n -i 'sogdian loan' to find the article, entries are numbered Persian words with Sogdian etyma.
== AHM | offset: leaf = printed + 14 (e.g. leaf 18 = p.4). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt
   hint: Commentary is by stanza/note number; the Glossary (end of book) lists Avestan words. grep the Avestan word in transliteration.
== HRN | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
   hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== BQT | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
   hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== MON | offset: None | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
   hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== AHD | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
   hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== SOD | offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt']
   hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur
== WLD | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt']
   hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== IEC | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
   hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== SYN | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
   hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== SKT | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
   hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== LEW | offset: 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt
   hint: Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.
== LAT | offset: leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt
   hint: Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
== FSD | offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
   hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== WEB | offset: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt
   hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.
== ARY | offset: printed page = pdf page + 1 | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt']
   hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
== BRT | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
   hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== PHD | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt
   hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB | offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt
   hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== HUB | offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
   hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== FVQ | offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt']
   hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
== PLA | offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt']
   hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
== AFM | offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt']
   hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
== LKT | offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt
   hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== DEV | offset: leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt
   hint: French headword in caps at line start.
== PHN | offset: leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt
   hint: French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.
== OXF | offset: None | local: None
   hint: Borrow via IA lending; in-book search ?q=<word>.
== VDQ | offset: None | local: None
   hint: noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.
```


### [2026-09-06T16:05:13.688Z] TOOL RESULT

```
agent
page-100.json
page-101.json
page-102.json
page-103.json
page-104.json
page-105.json
page-106.json
page-107.json
page-108.json
page-109.json
page-110.json
page-111.json
page-112.json
page-113.json
page-114.json
page-115.json
page-116.json
page-117.json
page-118.json
page-119.json
page-120.json
page-121.json
page-123.json
page-124.json
page-125.json
page-126.json
page-127.json
page-128.json
page-129.json
page-130.json
page-131.json
page-132.json
page-133.json
page-134.json
page-135.json
page-136.json
page-137.json
page-138.json
page-139.json
page-140.json
page-141.json
page-142.json
page-143.json
page-144.json
page-145.json
page-146.json
page-147.json
page-148.json
page-149.json
---
{
 "pdf_page": 202,
 "book_page": 172,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
  {
   "entry": 0,
   "root": "Gwa, Gwâ, Gwen 2",
   "verdict": "confirmed",
   "modern_form": "PIE *gʷem- 'to go, to come' (with the collateral root *gʷeh₂- / *gʷā- 'to step, go'); Pokorny IEW 463-465",
   "note": "Pokorny's entry, which begins on p.463 exactly as Nourai cites, is headed 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“', and it is deliberately a double entry (I. gʷā-, II. gʷem-), which is why Nourai's box carries two names, 'Gwa, Gwâ'. His third name 'Gwen 2' reflects the *gʷem- > *gʷen- variant Pokorny himself notes ('Unthematisch *(e)-gʷem-t (> *e-gʷen-t)', and Latin advenam / veniō with -n- for -m-); it is not a separate root in any modern handbook, so it is Nourai's own labelling convenience rather than an error of substance. Watkins/AHD 1985 heads the same material 'gʷā-. Also gʷem-. To go, come'; Cheung splits it into *gaH¹ (PIE *gʷeh₂-, Pok. 463 f.) and *gam¹ (PIE *gʷem-, Pok. 464 f.). The gloss 'to walk, to step, to come, to go' is an accurate rendering. Two words in the chart do not belong to this root: Avestan 'gâv' in node 6 (a misprint) and 'thamân' in node 12 (an unidentifiable form), and one Persian word, nîyâm (node 3), is derived by modern scholarship from a different root (*ni-dā-, not *ni-gam-). Everything else on the page is standard, well-attested Iranian etymology.",
   "note_fa": "جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۶۳ فرهنگ خود مدخل «gʷā-, gʷem-» را با معنای «رفتن، آمدن؛ به جهان آمدن، زاده شدن» آورده و همان‌جا نام‌های gʷm̥-ti-s و gʷem-tu-s «گام، رفتار» را می‌افزاید؛ پس هر دو صورت «Gwa/Gwâ» و «Gwem» از یک مدخل‌اند و برچسب «هندواروپایی» و معنای «راه رفتن، گام برداشتن، آمدن، رفتن» درست است. نام سوم «Gwen 2» گونهٔ *gʷen- است که خود پوکورنی (در *e-gʷen-t و در veniō لاتین) یاد کرده و در کتاب‌های امروزی ریشهٔ جداگانه‌ای به شمار نمی‌رود؛ این نام‌گذاری از خود نورایی است نه خطای علمی. واتکینز (پیوست AHD) نیز همین ماده را «gʷā-, also gʷem-: رفتن، آمدن» آورده و چونگ آن را به دو ریشهٔ *gaH¹ و *gam¹ بخش کرده است. در سراسر این صفحه تنها سه لغزش هست: صورت «gâv» در گرهٔ ۶ (غلط چاپی)، صورت «thamân» در گرهٔ ۱۲ (صورتی که در هیچ فرهنگی یافت نشد) و واژهٔ «نیام» در گرهٔ ۳ که پژوهش امروزی آن را از ریشهٔ دیگری (*ni-dā-) می‌داند.",
   "sources": [
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷem-"
   ],
   "ref_check": [
    {
     "ref": "POK:463",
     "status": "supports",
     "note": "POK_02.txt line 1790 (the leaf whose running numbers are 463-465): 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“, Verbaladjektiv gʷm̥-to-s. I. gʷā-: ... 2. gʷem-: ...'. The same pages carry 'av. gātu-s „Ort, Liegerstatt, Sessel, Thron“, apers. gāθu- ds.', 'av. gā-man- n. „Schritt“', 'av. jantu (*gʷem-tu-)' and 'av. jasaiti „er geht“' — i.e. Pokorny 463 alone underwrites the root box and nodes 1, 2 and 6."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I 675-677 (WLD_Bd1 djvu line 42665 ff., running head 'gʷem-, gʷā-')",
     "stance": "supports",
     "note": "'gʷem-, gʷā-' … 'ai. gātram „Glied, Körper“; ai. gātu- „Gang, Weg, Raum, Ort“, av. gātu-s „Ort, Platz; Liegerstatt, Sessel, Thron“, ap. gāθu … ai. vi-gāman- n. „Schritt“ … av. gāman- n. „Schritt“'. This is the source Pokorny 463 abridges (Buck cites it as 'Walde-P. 1.675 ff.')."
    },
    {
     "src": "AHD",
     "where": "Watkins 1985, g-list (AHD_watkins1985.txt line ~539)",
     "stance": "supports",
     "note": "'gʷā-. Also gʷem-. To go, come. 1. Germanic *kuman in a. Old English cuman, to come: COME … 3. Suffixed zero-grade form *gʷm̥-yo- in Greek bainein, to go, walk, step, with basis (< *gʷm̥-ti-), a stepping, tread, base'. Same double root, same gloss."
    },
    {
     "src": "CHEUNG",
     "where": "s.v. *gam¹ (CHEUNG.txt lines 7307, 7478) and *gaH¹ (line 7054)",
     "stance": "supports",
     "note": "'*gam¹ \"to come\" … «PIE *gʷem- “to go; come” = LIV: 209 f. | Pok.: 464 f.»'; and '«PIE *gʷeH₂- “to go, stride” = LIV: 205 | Pok.: 463 f.»'. Cheung's *gam¹ article lists, as its New-Persian outcome, exactly Nourai's harvest: 'NP zamān “time” … NP gām “step, pace” … NP āmadan … NP pay(g)ām “message”, NP pay(g)ambar … NP anjuman “company, assembly, club”'."
    },
    {
     "src": "SYN",
     "where": "Buck §10.47/10.48 (SYN.txt line 17514 f.)",
     "stance": "supports",
     "note": "'2. IE *gʷem-, *gʷā-. Walde-P. 1.675 ff. … Skt., Av., OPers. gam- \"go, come\" (Skt. gacchati, Av. jasaiti, sk̑o- presents like Grk. baskō; Av. jam- without prefix mostly \"come\"; also Av., OPers. ā-jam- \"come\", whence NPers. amadan \"come\")'."
    },
    {
     "src": "KLN",
     "where": "p.318 s.v. 'come' (KLN_1966.txt line 8320, page marker 318 at the foot)",
     "stance": "supports",
     "note": "'come … fr. I.-E. base *gʷem-, “to go; to come”, whence also OI. gámati, gacchati … Avestic jamaiti “goes” … Cp. the collateral base *gʷā- in OI. agām (aor.), Gk. ébēn (aor.), “I went”'."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Avestan / Old Persian",
     "words": "gam : to come, step; jam, jantu : to go",
```


## [2026-09-06T16:05:20.832Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 554\" POK_full.txt | head; echo ---; grep -n \"Page(s): 556\" POK_full.txt | head; echo ---; grep -n \"lemma: kel\" POK_full.txt | head -20; echo ---; grep -n \"lemma: kem\" POK_full.txt | head -20",
 "description": "Search Pokorny full dump for pages 554,556"
}
```


### [2026-09-06T16:05:20.946Z] TOOL RESULT

```
44628:Page(s): 554 
49206:Page(s): 554 
49818:Page(s): 554 
93768:Page(s): 554 
---
45248:Page(s): 556 
50056:Page(s): 556 
50072:Page(s): 556 
50111:Page(s): 556-557 
---
44616:Root / lemma: kelg- 
44630:Root / lemma: kel-1, kela- 
44697:Root / lemma: kel-2 
44745:Root / lemma: kel-3, kela-, A/a- extended klad- 
44927:Root / lemma: kel-5 
44963:Root / lemma: kel-6, k(e)le-, k(e)la-or 1(1-1 
45077:Root / lemma: kel-7{kol-, kj^ 
45105:Root / lemma: kel-7 
45113:Root / lemma: kelp-, l^lp- 
47147:Root / lemma: kel-, kol-, kal- 
93753:Root / lemma: keleu- 
---
45133:Root / lemma: kemero- komero-, keinero- 
45157:Root / lemma: kema-, koma-, kma- {* hank-mhnos) 
45161:Root/ lemma: kema-, koma-, kma-{* hank-mh(e)nos)\ piece, derived from Root/ lemma: 
45178:Root / lemma: kem-1 
45224:Root / lemma: kem-2 
46412:Root / lemma: kemo- 
49208:Root / lemma: kemer-
```


## [2026-09-06T16:05:21.667Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==211' POK_02.txt | head -80",
 "description": "Print POK_02 leaf 210"
}
```


### [2026-09-06T16:05:23.239Z] TOOL RESULT

```
it',  ebenso  lit.  Hlus  , August', richtiger  Hlius)-,
lat.  caleö,  -ere  ,warm,  heiß  sein,  glühen',  calidus  ,warm,  heiß',  calor , Wärme,  Hitze';
cymr.  clyd  (*Jcl-to-)  ,warm,  wärmend'  ( :  lit.  siltas) ;  dazu  vielleicht  von einer  ei*-Erweiterung  cjmr.  claear  ,lauwarm',  bret.  hlouar  ds.?/
552
As.  halöian  ^hrennen^  ]  im  Germ,  wurde  eine  Erweiterung  *kleu-  frucht- bar: ahd.  läo^  flect.  läwer  ,lau' ,  aisl.  hTc^  ds.^  vom  Wetter  {*hlewia-\ hlana  ^mild  werden^,  bair.  läunen  ^tauen',  aisl.  hläka  ,Tauwetter^:  aisl. hlyr  ,lau^,  hly  n.  ,Wärme^,  ags.  Ueoxoe  ^lau^,  aisl.  hU  {*hletoa-)  n.  ^Schutz, Leeseite^,  as.  hleo  m.  ^Schutz  vor  dem  Wetter^,  afries.  hll^  ags.  hleo,  hleow  n. jObdach,  Decke,  Schutz^  (vgl.  auch  mhd.  liezce,  lie  f.  ^Laube*^;,  Schweiz,  l^ ^geschützte  Lage,  Sonnenseite^,  schwed.  lya  ,Höhle  von  Tieren^);  norw. dän.  lum,  lummer  ,mild,  lau^,  schwed.  Ijum  ds.,  Schweiz,  lüm  ,mild,  vom Wetter"^  u.  dgl.,  ndd.  luk,  holl.  leuk  ,lau^
lit.  sylüj  silau,  silti  ,warm  werden^;  siltas  ,warm^  (:  cymr.  clyd),
WP.  I  429  f.,  WH.  I  137,  Trautmaun  297  f.,  304  f.
2,  kel-  ,neigen^
Basis  der  viel  reicher  entwickelten  Wurzelf.  klei-  ,lehnen^  (s.  unten) und  sehr  wahrscheinlich  in  folgenden  Worten  anzuerkennen :
Lat.  auscultö  ,horche,  lausche^,  ursprüngl.  ,neige  das  Ohr^  aus  "^auscltäre, Ableitung  von  *aus-kltos  (Specht  Idg.  Dekl.  285,  333);  anders  WH.  I  86 f.;
lit.  salls  ,Seite,  Gegend^;
aisl.  hallr,  ags.  heald,  ahd.  hold  ,geneigt^,  ahd.  halda,  nhd.  Halde  ,Bergab- bang^  (aisl.  halla  ,neigen^,  ahd.  haldön  ,sich  neigen^,  aisl.  hella  ,ausgießen, ein  Gefäß  neigen^,  wie  Schweiz,  helde),  got.  wüja-halpei  ,Neigung,  Gunsf ; got.  hulps  ,geneigten  Sinnes,  gnädig^,  aisl.  hollr,  ags.  as.  ahd.  nhd.  hold ds.  (ahd.  huldl  ,Huld,  Geneigtheit^  usw.) ;  dazu  auch  mnd.  helde  f.  ,Abhang', nd.  hille  ,Raum  über  den  Viehställen  zum  Schlafen^  (aus  hilde  ,geneigte, schräge  DeckeQ  und  die  nord.  Sippe  von  norw.  hjell  ,Gerüst,  Boden', älter  dän.  hjceld  ,Heuboden,  Hühnersteige,  Söller',  aisl.  hjallr  , Gerüst, Erhöhung',  hjalli  , Absatz,  Terrasse',  hilla  ,Gesims,  Bord,  Regal'  (=  mnd. hilde) ;  ablautend  dän.  hylde  ,Regal',  schwed.  hylla.
WP.  I  430 f.,  WH.  I  86  f.,  235;  über  kel-  ,neigen'  (mit  Velar)  s.  (fi)Ä«Z- ,biegen'.
3.  kel-  ,dünner  Schaft,  Pfeil,  steifer  Halm'.
Ai.  sald-  m.  ,Stock,  Stachel  des  Stachelschweins',
```


## [2026-09-06T16:05:32.555Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '44920,45010p' POK_full.txt",
 "description": "Print POK_full kel-5 block"
}
```


### [2026-09-06T16:05:32.609Z] TOOL RESULT

```
Maybe alb. kaush " cup ' a Slavic loanword. 

References: WP. I 440 ff., WH. I 139 f., 249, Specht Indo Germanic Dekl. 118, 140, 1433, 
Trautmann 113f., Petersson Heterokl. 146 f. 
Page(s): 547-548 

Root / lemma: kel-5 

Meaning: to drive, force to move quickly 

Material: Old Indie kalayati^ floats, carries, perceives, holds '; 

alb. Geg qil, sizil. (/©/"bring, bear', shqiltse^ rennin, enzyme used to curdle milk and 
produce cheese, active component in rennet (derived from the mucous membrane of the 
fourth stomach of young cows), a means of coagulation, a coagulum or coagulator (the 
curdled milk in the stomach of a sucking animal, the stomach itself, etc.), rennet or runnet, 
(that which holds or binds together) ', probably also kal, kair cause, make happen, bring 
about, put, place ' (Jokl IF. 30, 198); 

gr. keAAcjo "drive on; land; go ashore (from a boat); arrive on the ground, touch ground ' 
(present only by Gramm. and in 6-keAAu) trans. " go ashore; run ashore, fail, be 
unsuccessful, make unsuccessful, break down, fall through '; otherwise only Aor. Fut. 
£K£Aaa, KsAaoj), KsAric;, -nTO(; " rusher, racer (horse); quick-sailing ship'; kAovoc; " intense 
movement', kAoveoo " drive tumultuously or in confusion, o be agitated, rush wildly, o be 
beaten by the waves ' (compare 9p-6voc;, xp-6vo^; Boisacq s. v. m. Lithuanian); perhaps 
(Persson Beitr. 179) koAeTv sAGeTv undKoAsa, KoAia 'kind of dance ' Hes.; 

Latin ce/eA "quick, fast, rash, hasty' (as K£Ar|<;), celeber, -bris, -bre^ frequented, much 
visited, thronged, crowded, populous, abounding ' {*keleA^lo-, -d'^/f-); 

as /-present Gothic haldan^ tend, feed, graze cattle ' (to a-Vok. s. Brugmann IF. 32, 
181), Old High German ba/tan ^beware, guard, hold, stop'. Old Saxon haldan. Old English 
healdan. Old Icelandic halda. Old Swedish halla {* halt^an) "hold, stop'. Middle Low 
German hilde, /7///e"rash, hasty, keen, eager'. 

References: WP. I 442 f., WH. I 194f.; 



See also: probably identical with kel-6; s. also keleu-^ wander '. 
Page(s): 548 

Root / lemma: kel-6, k(e)le-, k(e)la-or 1(1-1 

Meaning: to call, cry 

Material: Old Indie usa-kala-m. 'rooster, cock' ('rii-Kav6(;'), kaladhika-, kalavika-^s., kala- 

v/fjka-' sparrow', ka/a- - " leise tonend, undeutlich vernehmbar', ka/aka/a-m. ' bewildered 

clamor, noise'; 

gr. kqAeoj (instead of *KaA(jo) " call, summon, name, rufe herbei' (Aeolic KaAnM')- Futur. 
KaAsGU), Attic kqAu), Perf. K£KAr|Ka, kApitoc;; sniKAnoK; "epithet', kAhok; "shout, call, 
invitation, subpoena, invitation to court, summoning ', KAr|Tn(;, K(a)AriTwp "Rufer', opiOKAr) 
"shout' (to 1. part see below oma-); KiKAnoKU) (or KiKApaKU)) "rufe an, flehe', KAn'i'^u), kApi^co 
"name' (*KAr|-F£-(;-i^u)?); zero grade K£A(a)- in KsAofjai "treibe an (through shout)', hom. 
Aor. (£)k£kA£to, Doric k£vto = (£)k£Ato; [about k£A£uu) see below kleu-]; K£Aapu^u) 
"rausche, riesle (water)', keAojp cpcjovrj Hes.; extension KzKaboc, " din, fuss, noise', 
K£Aa5u)v, K£Aa5£iv6(; " roaring ', K£Aa5£U) " sound as flowing; shout aloud, of various cries, 
e.g. of a new-born babe, sing of, celebrate loudly '; 

Umbrian karitu, kafetu, carsitu^ to call together, summon, convoke, drive to, move up, 
bring along, force towards ' {*kaletdd); 

the fact that a corresponding Latin *caled has stood once in the proclamation formula of the 
calendar data Dies te quinque, respectively septem, calo, luno Cove//a ar\d ca/encfae'\he 
erste day of month ' would be named from this exclamation, is probable (Salonius Z. rom. 
Dat. 1 ff.); 

Latin ca/o, -a/ie "exclamation, to call together, summon, convoke ' (: Latvian kaluot), 
calator^ a servant for calling, etc., a crier ', nomen-clator^ one who calls by name, a 
monitor ' (back formation from nomen calare), calabra {curia) " Curia Calabra, a court, 
curia so called from the proclamation of the dates which was there made ', perhaps 
conciiium^ a meeting, rendezvous ' {*c6n-caiiom), con-ciiiare ^ur\\te, connect, gain etc.', 
clamo, -are 'caW, shout, cry' (compare Old High German ii/amon etc.), ciamor' scream', 
c/a/Y/s"lauttonend, fernhin resounding; illustrious; clear, bright', Umbrian angiarHom. PI., 
ang/af Akk. PI. "oscines' {*an-k/a 'av\s inclamans'); Latin c/as5/s "Aufgebot: army, fleet; 
class, dividing off, partitioning off {*kiacf-ti-: Kikaboq?); 

Maybe alb. Geg k/a, Tosc qanj, qaj" cry, scream '. 



Old Irish cailech, ogam Gen. caliaci, cymr. ceiliog, corn. che//oc' rooster, cock' 
{*ka//akos); 

Old English hlowan^ roar, cry out, resound ', Old High German (h)ldian, {h)luoen. 
Middle High German luejen^roar, bellow'; Old English /7/e/5/7 'grunt'; Old High German 
hluoticla^ a barking '; with lengthened grade the first syllable Old High German /7e/'loud,
```


## [2026-09-06T16:05:33.265Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '45178,45260p' POK_full.txt",
 "description": "Print POK_full kem-1 and kem-2"
}
```


### [2026-09-06T16:05:33.339Z] TOOL RESULT

```
Root / lemma: kem-1 

Meaning: to press, squeeze 

Material: Armenian k'amerio press, squeeze, wring; to filter, make flow'; 

Old Norse hemja {hamda) "curb, restrain, hinder, hamper', hemiir leg fetter', ham/at " 
Ruderband ', Middle High German hemmen and hamen^\r\\n6er, hamper', sal- Franconian 
chamian^ clamp, press'. Old Frisian /7e/77/r75 "hinder'. Modern High German dial, ham, 
hamen " horse collar ' (compare that maybe from a Gothic *hamands hemmend " 
hindering ' borrowed Slavic *chomgt-b, russ. etc. chomuf-b " horse collar '); Middle Low 
German ham. Old English hamm^ enclosed piece of land', ndd. hamme^ fenced field'. Old 



English engl. herr{m) "edge, hem', engl. to hem {in) "to hem, gird, border, envelop, 
surround'; 

Old Norse hafna^ abandon, give up from ' ("*be restrained '), causative hefna^ avenge '; 
with labial Middle English hamperen, engl. to hamper '\r\\n6er, bother, annoy' (: Old 
Prussian kumpinna^ hindered ', kumpint^moye, displace'); (under the influence of 
common Celtic -ns-, -nt- > -nn-). 

Balto Slavic *kama-{r\. "clump' in Latvian kamsm. "clump', in addition Lithuanian 
kamuoti^ press together, stuff, kamanos^ leathery bridle, rein', kemuras ^ grape' , 
kam/enasm. "stem', Latvian Aa/77^c»/' torment, smite, plague', Lithuanian kamuolys, 
Latvian kamuolis^ ball, tangle, knot '; ablaut. Latvian c§mu(o)rsm. "grape', extended 
Lithuanian kemsu, kimsti^ stuff, Latvian kemsu, A7/77S/ (Lithuanian loanword) "ds.', also " 
devour', Lithuanian kamsa^ crush, squash, corduroy, brushwood road '; 

russ. kom "clump', komftb " clench together ', serb. kdm " husks of grapes ' (" what 
remains of the pressed grapes '); in addition russ. komelt m. 'thick end of a rod ', poln. 
komelm. "knag' {*kamlia-), russ. komuljai. "clump', serb. kominai. " husks of grapes '; in 
ablaut Slavic *k-bmy. Gen. *k-bmene'(r\. in Czech A/77e/7 "stem'; as " be pressed ' 
presumably also Slavic *cbma\v\ serb. cama^ boredom, weariness ', camati^ wait with 
displeasure, hold on'; Old Church Slavic di^s/b "dense' (= Lithuanian A//775/as "stuffed'). 

Doubtful is Perssons (Beitr. 159) apposition from gr. KdJMU(;, -u0O(; " bundle, truss of hay, 
branch of laurel, placed before the gates, reed-bed ', kojjjoc; " revel, carousal, merry- 
making, concrete, band of revelers, the ode sung at one of these festive processions, 
festival to honor of the Dionysios '; gr. Kr||j6(; ( */ra/770S because of Latin loanword camus) 
"muzzle' is not compatible in vocalism. 

References: WP. I 388 f., Trautmann 115, 126. 
Page(s): 555 

Root / lemma: kem-2 

Meaning: to buzz 

Material: Old Indie camara- m. " Wild Yak '; 

Middle High German Modern High German hummen. Modern High German hummein, 
holl. hommelen^buTz!, Middle English hummen, engl. hum 6s., Norwegian humre^ neigh 
quietly '; in addition originally probably also Old High German humbal. Middle High 



German humbel, hummelxw. "bumblebee', Middle Low German hummeli., engl. humble- 
bee, Norwegian Dialectal humlai. ds.; 

Lithuanian kimstu, klmtT become hoarse ', kiminti^vnake the voice dull ', kimCis^ 
hoarse, raucous, thick, husky ', kamane^ bumblebee, bumblebee ', kamine^ Feldbiene ', 
Latvian kaminesi. pi. " bumblebees, bumblebees ', Old Prussian ca/77i/s "bumblebee'; 

Slavic *CB/r7e/6 (ablaut equally with Hummel) in russ. dial, cmelb etc., " bumblebee, 
bumblebee '; Church Slavic russ. komaretc. " mosquito ' (ablaut equally with Lithuanian 
kamane). 

References: WP. I 389, Trautmann 115 f. 
Page(s): 556 

Root / lemma: keng-, kenk- 
See also: see above under keg- 
Page(s): 565 

Root / lemma: kenk-1 

Meaning: to bind, girdle 

Material: Old Indie /ra/7C5/e(Dhatup.) "binds', kahcuka-m. "armor, coat of mail, garment 

made of linked metal rings, jerkin, corsage', kancTi. "belt, girdle';
```


## [2026-09-06T16:05:44.785Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 44628 49206 49818 93768; do echo \"=== around $L ===\"; sed -n \"$((L-45)),$((L+2))p\" POK_full.txt; done",
 "description": "Print POK_full contexts for Page 554"
}
```


### [2026-09-06T16:05:46.735Z] TOOL RESULT

```
=== around 44628 ===

References: WP. I 365, E. Lewy PBrB. 32, 140. 
Page(s): 543 

Root / lemma: keku- 



Meaning: a kind of stick or cudgel 

Material: Avestan cakus- n. " throw hammer, throw ax ', npers. da/ri/s "hammer'; 

Old Prussian queke^ stick ', i.e. " firs or spruces branch as a fence stick ', Latvian caka 
"cudgel, club with knag as handle, grasp'; compare but MiJhlenbach-Endzelin Latvian-D. 
Wb. 1401. 

References: WP. I 381. 
Page(s): 543 

Root / lemma: keR- 

Meaning: weasel 

Material: Old Indie kasa-x^. kasTka\. "a kind of of rodent animal, weasel'; but with aniaut. 

Pal. Lithuanian ses/ras "polecat', Latvian ses/rs ds. 

Different about Lithuanian ses/ras W. Schuize Kl. Schr. 630. 

References: WP. I 381. 

Page(s): 543 

Root / lemma: kelg- 

Meaning: to wind; windings, intrigue 

Material: Middle Irish celg\. "artifice, betrayal ' (out of it cymr. celg^ hiding place, cover'); 

Armenian keick'^ hypocrisy '; 

changing through ablaut Old English hylc^ curvature, convolution ' and Slavic *c'blgati\'r\ 
poln. czoigacsig^ grovel, truckle, creep, glide, slide, drag onself on '. 

References: WP. I 447. 
Page(s): 554 

Root / lemma: kel-1, kela- 
=== around 49206 ===
Material: Gr. npTvo(; "Steineiche', whether from * kurs-no-s {1)\ gall, prenne^ arborem 

grandem ', cymr. corn. bret. prenn'tree' ( *kures-no-)\ (common Celtic -ns-, -nt- > -nn-), 

ablaut. Old Irish crann{*kurs-no-). Gen. cruinnAs., cymr. prys{prysg) ' spinney' {*kurs-to- 

); Old English /t/z's/ "shrubbery, bush, spinney'. Old Saxon Old High German mud. horst, 

hurstAs., Modern High German HorsV eyrie, nest of a bird of prey ' ( *kyrs-to-\ less 

probably above S. 548); Slavic *chvorsti3. Church Slavic chvrastije, russ. chvorost 

"deadwood, shrub, bush', slov. hrasf 'oak' {*kuors-to-7), with unexplained aniaut. 

Maybe alb. shkurre' bush' [common Italic lllyrian sr- > rr\. 

References: WP. I 524, Morris-Jones Welsh Gr. 128, Machek Slavia 16 (1939), 182 f., 

Mikkola Urslav. Gr. 177. J. B. Hofmann (Etym. Wb. of Gr. 284) contemplates gr. because 

of Carian PN as pre Greek - Asia Minor. 

Page(s): 633 

Root / lemma: kjauo- kjeuo- 

Meaning: bald 

Material: Old Indie ati-kurva-, -kulva-' completely naked, bald', Avestan kaurva-, npers. kal 

" hairless, naked, bald'. Old Indie kalvalTkrta-' made bald '; 

Latin ca/i/i/s "naked, bald, hairless ' (basic form Italian kalouosiroxw Indo Germanic 
*keleuos because of:) Oscan Kaluviefs (besides Oscan Kalaviis " Calvius ', Paelignian 
Calauanfs]), wherefore Latin ca/i/a "cranium, the scalp, bald head', ca/var/a ds., in 
commentary also "skull'. 



About the tried arrangement with Modern High German /r5/7/under assumption Indo 
Germanic initial sound variation see below Aa/- 'naked, bald'; other assonant words are 
(with expressive kh-) Old Indie khalatf- " baldheaded ', kha/vata- 6s. (: Armenian xalam 
"cranium'?). 

References: WP. I 447, WH. 1143 f. 
Page(s): 554 

Root / lemma: kemer- 
=== around 49818 ===

Material: Old Indie siprai. "whisker, moustache, flowing plume, feather', Avestan (with 
metathesis) srifa- m. " nostril '; Avestan saeF whisk, small broom for dusting '; the 
meaning of Avestan saepa- is unclear; 

Lithuanian siepiuos, s/epf/san6 saipaus, saipytis' making faces, making facial 
expressions ', sypla^ mocker, person who mocks, scoffer', sypsau, -oti^ grin, smile 
broadly, bare the teeth, grimace '. 

References: WP. I 364, Frisk Le monde oriental 30, 78 ff. 
Page(s): 543 

Root / lemma: Rek*- 

Meaning: to defecate 

Material: Old Indie sakrtu. Gen. saknahu. "crap, muck' ; compare chagana-u. ds.; 

gr. K6npO(; "crap, muck, manure, smut'; 

Lithuanian siku, s//r//" defecate'. Perhaps here also Old Irish cechor\. Gl. "palus' 
{*Rekura), Middle Irish cechair^s\\rc\e, mud, ordure' (if " bodily excrement ' is the original 
meaning). 

Note: 

The inanimate suffix -ur- . Celtic {*Rekura) "slime, mud, ordure' : UAupioi , oi, lllyrians, 
lAAupia , n, lllyria, also'lAAupi^ , n. Adj. lAAupiKO^ , n, 6v, lllyrian: -ys\, the region or province 
of lllyria, 'lAAupi^O) , speak the lllyrian language, 'IAAupia:--hence Adv. 'lAAupiaii. 
References: WP. I 381, Benveniste Origines 9. 
See also: See still *AaAAa- "defecate'. 
Page(s): 544 

Root / lemma: Relb-, Relp- 

Meaning: to help 

Material: Gothic hilpan. Old Icelandic hjalpa. Old Saxon Old English helpan. Old High 

German helfan, he/phan^\r\e\p'; 

Lithuanian selpili, selpti. Old Lithuanian se/b/nos'\r\e\p, aid '; unclear is the relationship 
to gelbeti^\\e\p\ 

References: WP. I 447 f., Trautmann 302, Feist 255 f. 
Page(s): 554 


=== around 93768 ===
Verschobenes ba'^mb-or unverschobenes pa^mp-\v\ Swedish Dialectal pampen' turgid, 
swollen ', Danish Dialectal pampe's\cb brijsten, brag, boast', Norwegian Dialectal pempa 
seg Cpampjan) "sich with Trank fijllen'. Middle Low German pampen "sich stuff ' (Modern 
High German pampfen). Modern High German pampe'\.b\ck porridge, mash'. 

With Tenuis: Latin pamp/nus'{*bu6, *eye) fresh shoot of Weinstockes, vine-layer '; 
Lithuanian pampstu, pampau, pampt/"s\Ne\\ up', /Oa/77yO/j7s "Dickbauch', pumpa ' knob, 
handle, button, pommel, Teichrose', pimpilasvn. "penis', Latvian pampt, pempt, pumpt'io 
swell', pampali" potato ', pimpala' 6as mannliche limb, member', pumpe' hump, 
hunchback, swelling, blister' (the i/-forms are understood as contamination with *pup-). 

Old Bulgarian p^pb "navel', russ. pup'uaveX, pupys'bu(i, bulge ', poln. p§p' spigot '; 

Old Icelandic M" giant; rogue, simpleton ', fimbul- intensifying prefix. Old English fTfel 
"SeeungetiJm, giant ' {*pempelo-). Old Icelandic fimbul-, fambT Erztropf '. 

Besides with auslaut Germanic Tenuis Danish fomp, Norwegian Dialectal fump, famp 
"thick fool '. 

With Tenuis asp. Armenian p'amp'ust' bladder'. 

References: WP. II 108 f., WH. I 122, Niedermann WuS. 8, 87 f., Trautmann 26, 205. 
See also: see also *ba^b- ds. 



Page(s): 94-95 



Root / lemma: keleu- 

Meaning: to wander; way 

Note: probably extension from kel-5. 

Material: Gr. K£A£u9o(;f. 'way' (from *kA£u-9o-(; reshaped after sAsuG-), inno-KsAsuGoq ' zu 

Pferd sich fortbewegend ', o-koAouGoc; (*a- = sm-) ' companion '; 

Maybe alb. kalonJ^yNaW! 

Lithuanian keliauju^ travel, journey' {ke//as'\NaY' probably previously postverbal). 

References: WP. I 446, Kretschrner Gl. 20, 253, E. Fraenkel, Mel. Boisacq I 374 f. 
Page(s): 554
```


## [2026-09-06T16:05:57.156Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 50056 50072 50111; do echo \"=== around $L ===\"; sed -n \"$((L-40)),$((L+3))p\" POK_full.txt; done",
 "description": "Print POK_full contexts for Page 556"
}
```


### [2026-09-06T16:05:59.114Z] TOOL RESULT

```
=== around 50056 ===
gr. Ka|jv(jo "work, win by toil, oil, labour, o be hard-pressed, worsted, in battle or contest, 
to be sick or suffering, to be distressed, meet with disaster, of the dead, i. e. either 
outworn, or those whose work is done, or those who have met with disaster ' (probably 
*km-n-a-, as Old Indie samnTte), Fut. Kaijouijai, Aor. SKopov, Perf. K£K|jr|Ka, Doric KSKpoKa, 
participle K£Kpr|(F)w(;, Kpr|T6(;, Doric K|jaT6(;, noAuK|jr|TOc; " wrought with much toil, epith. of 
iron (as distinguished from copper), elaborate, laborious, of persons, toiling hard ', KapaTO(; 
" fatigue, exertion, hardship, affliction ', a-Kpn(;, -f\\oc„ aKd\}ac„ -avTO(; " untiring, fresh', 
Kapi6vT£(; ' the dead people ', as Attic K£Kpr|K6T£(;; ograde £ipo-K6po(; " preparing wool ', 
inno-K6|Joc; ' groom, stableman ', Kop£U) "tend, look after' etc., KojjiSn 'nourishment, care, 
cultivation etc.'; lengthened grade KG)\xa " deep, peaceful sleep'; 

Middle Irish cuma. Middle Breton caffou' distress ' (Pedersen KG. I 47, 361); Middle 
Irish cumal' slave ' ("*striving, strenuous ', as:) gall. Camulos' god of war'? 

References: WP. I 387 f. 
Page(s): 557 

Root / lemma: Rem-1 or Ram- 

Meaning: stick, pole, horn 

Material: Old Indie sa/r?/^ "stick, spigot, wooden nail, supporting nail', Avestan sima{-i- 

seems Indo Germanic a; or = Old \v\6\csamyaR) 'a part of the harness of the horse-drawn 

chariot ', npers. sfm ds.; 

Armenian sami-k'P\. " Stirnholz des Ochsenjochs ' (Iran, loanword?); 

gr. KQija^f. m. " shaft, pole, picket, pole, shaft of javelin '; 

Danish Swedish hammei, Norwegian dial. iiumul{-hgmuil) " the crosspiece in front in 
the chariot ', Middle High German hamel' shaft, pole, clot, chunk'; 



about the difficult Latin camox^ chamois, small goatlike antelope', vorrom. *kamosso-, s. 
J. Hubschmid ZrPh. 66, 9ff. 

References: WP. I 385, WH. I 148, 633. 
Page(s): 556 

Root / lemma: Rem-2 
Meaning: hornless, young deer 
=== around 50072 ===

Root / lemma: Rem-1 or Ram- 

Meaning: stick, pole, horn 

Material: Old Indie sa/r?/^ "stick, spigot, wooden nail, supporting nail', Avestan sima{-i- 

seems Indo Germanic a; or = Old \v\6\csamyaR) 'a part of the harness of the horse-drawn 

chariot ', npers. sfm ds.; 

Armenian sami-k'P\. " Stirnholz des Ochsenjochs ' (Iran, loanword?); 

gr. KQija^f. m. " shaft, pole, picket, pole, shaft of javelin '; 

Danish Swedish hammei, Norwegian dial. iiumul{-hgmuil) " the crosspiece in front in 
the chariot ', Middle High German hamel' shaft, pole, clot, chunk'; 



about the difficult Latin camox^ chamois, small goatlike antelope', vorrom. *kamosso-, s. 
J. Hubschmid ZrPh. 66, 9ff. 

References: WP. I 385, WH. I 148, 633. 
Page(s): 556 

Root / lemma: Rem-2 
Meaning: hornless, young deer 
Material: Old Indie sa/77a-/7 "hornless"; 

gr. KZ\xdQ„ -aboc, f., later also KZ\x\xdc, 'young deer'; K£p(pa(; sAacpoq Hes.; 

Old Norse hindi.. Old English hind. Old High German /7//7/a'hind, female deer ' {*Rem-t- 

Lithuanian zem. s/77i//a5 'hornless', smulism., smulei. ' ox, cow without horns ' {*Rm-u- 
+ forms -lo), liv. loanword smoul; 

perhaps here russ. /rc»/77c»/>y "hornless'; compare also W. Schuize Kl. Schr. 619. 

References: WP. I 385 f., Specht Indo Germanic Dekl. 132. 
Page(s): 556 

Root / lemma: Rem-3 

=== around 50111 ===
References: WP. I 385 f., Specht Indo Germanic Dekl. 132. 
Page(s): 556 

Root / lemma: Rem-3 

Meaning: to cover, wrap 

Material: Old Indie samulya-u., samula-u. "woolen shirt ', sa/777"Prosopis spicigera; 

legume, pod vegetable, bean '; 

Latin cam/s/a {\ate) " shirt ' (gall, word; borrowed from Germanic *xam/P/a-' shirt '; 
previously from Latin stamen again Old Irish ca/mmse' shirt ', acorn, cams' white ', bret. 
kamps' mess garment, priest's garment used during Mess (Roman Catholicism) '); 

Alb. kem/sha' shirt' a Latin loanword. 

unclear is the aniaut in mcymr. hefys' chemise ', akorn. hev/s, bret. hiviz6s.; Old 
English cemes6s. is loanword from cam/s/a; 

Old High German /lem/d/n. " shirt ', Old English fiemede {*fiam/l=>/a-) "shirt'; Old Norse 
fiamrm. "wrapping, skin, shape'. Old English /70/775 "wrapping, cover, suit '; ITc-hama, Old 
Saxon //k-fiamo'bo6Y, Old High German /Thh/n-[*h]amo' body, corpse', Gothic ana-, ga- 



hamon^ get dressed ', Old Norse hama-sk'{* be disguised in animal figure, hence:) 
bucket '; Old Norse hams'bo\N\, husk, serpent skin ' {*hamisa-), compare Norwegian 
hamar^ core '; here also Gothic himins. Old Norse h/m/nn {Dat hifne\N\Vc\ -bn-^xovn -mn-, 
compare:) Old English heofon. Old Saxon hedan'sky, heaven', next to which Old High 
German Old Saxon h/m/7, md. humiTsky, heaven'; Old High German himila\so " ceiling ', 
Dutch hemer palate, roof. Modern High German HimmelbetV four-poster bed ', Old High 
German himiliz{z)i. Middle Low German hemelte^ ceiling '; barely right above S. 22 to aR- 
"stone'. 

A s-form sRem- one seeks incredible in Gothic skaman' be ashamed'. Old English 
skam/an ds., Old Icelandic skgmm. Old High German scama^\he genitals, shame' etc. 
("*be covered'?). 

References: WP. I 386, Specht Indo Germanic Dekl. 346. 
Page(s): 556-557 

Root / lemma: Renk-, Ronk-
```


## [2026-09-06T16:06:13.173Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_02 p554 ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=212 && NR<=214' POK_02.txt | grep -n -i -A12 -B3 \"kalu\\|calvaria\\|kaurva\" | head -60",
 "description": "Find Pokorny p554 German text"
}
```


## [2026-09-06T16:06:14.087Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN Calvary ===\"; grep -n -i \"^Calvary\\|^calvities\\|^calvous\\|^calv\" KLN_1966.txt | head -20",
 "description": "Grep Klein for calvary"
}
```


### [2026-09-06T16:06:15.117Z] TOOL RESULT

```
=== POK_02 p554 ===
25-Gr.  yislsv^og  f.  ,Weg'  (aus  *y,Xsv-'d'0-g   nach   iXsvd^-   umgeformt),  IjtTto- yciXsvd^og  ,zu  Pferd  s
26-ich  fortbewegend'  d-ycölovS-og  (*ä-  =  s^i-)  ,Begleiter^; lit.  keliduju  ,reise'  (kelias  ,Weg^  wohl  erst  postverbal). WP.  I  446,  Kretschmer  Gl.  20,  253,  E.  Fraenkel,  Mel.  Boisacq  I  374  f.
27-kelouo-,  kcleuo-  ,kahl'.
28:Ai.  dti-kürva-y  -kÜlva-  ,ganz  kahl',  av.  kaurva-,  npers.  kal  ,haarlos, kahl',  ai.  kälvälikrta-  ,kahl  gemacht';
29-lat.  calvus  ,kahl,  haarlos'  (Gdf.  ital.  kalouos  aus  idg.  *kJeuos  wegen:) osk.  Kalüvieis  (daneben  osk.  Kalaviis  ,Calvius',  päl.  (7aZawan[s]),  wozu lat.  calva  ,Hirnschale,  Schädel',  calväria  ds.,  in  Glossen  auch  ,Becher'.
30-Über  die  versuchte  Vermittlung  mit  nhd.  kahl  unter  Annahme  idg. Anlautschwankung  s.  unter  kal-  ,kahl';  andere  anklingende  Worte  sind  (mit expressivem  kh-)  ai.  khalati-  ,kahlköpfig',  khalväta-  ds.  (:  arm.  yialam ,Schädel'?).  .
31-WP.  I  447,  WH.  I  143  f.
32-kelg-  ,sich  winden;  Windung,  Ränke'.
33-Mir.  celg  f.  ,List,  Verrat'  (daraus  cjmr.  celg  ,Verhehlen') ; arm.  kelck  ,Heuchelei'  ist  im  Konsonantismus  unklar ; ablautend  ags.  hylc  ,Krümmung,  Windung'   und  slav.  *<^hlgati  in  poln. czoigac  sie  ,kriechen,  gleiten,  sich  schleppen'. WP.  I  447.
34-555
35-j^elp-,  klp-  .Krug,  TopF.
36-Gr.  xa^TTtg,  -idog,  xdlrtr]  f.  ^Krug-;  Aschenume' ;
37-lat.  calpar,  -äris  ^Weinfaß'  (*calp-äli-,  wohl  lat.  Weiterbildung   des  gr.
38-air.  cilornn,  cilurnn  ,urna^  (*kelpurnO')f  cjmr.  celwrn  ^Milcheimer*^,  bret. Jcelorn  ,Kübel^,  brit.  ON  Celumum. WP.  I  447,  WH.  I  142.
39-2,  kern-  ^zusammendrücken,  -pressen,  hindern';  komo-  ,Eingeengtes^
40-Arm.  liamel  ,to  press,  squeeze,  wring;  to  filter,  make  flow^;
```


### [2026-09-06T16:06:15.173Z] TOOL RESULT

```
=== KLN Calvary ===
6244:Calvary,  the  place  of  the  crucifixion  of  Jesus;  re¬ presentation  of  the  crucifixion  of  Jesus.  —  L. calvaria,  ‘skull’,  translation  of  Gk.  xpxviov  in the  Gospels,  rendering  Aram,  gulgulthd,  ‘skull’
6246:Calvatia,  n.,  a  genus  of  fungi  (hot.)  —  ModL., fr.  L.  calvus,  ‘bald’.  See  Calvary  and  -ia. calve,  intr.  and  tr.  v.  —  ME.  calven,  fr.  OE. ceaifian,  fr.  cealf  ‘calf’.  See  calf,  ‘young  of  a cow’.
6247:Calvinism,  n.,  the  religious  doctrine  of  John  Calvin (1509-64).  Cp.  chauvin.  For  the  ending  see  suff.
6249:Calvinist,  n.,  a  follower  of  Calvin.  —  See  prec. word  and  -ist.
```


## [2026-09-06T16:06:26.260Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6238,6255p' KLN_1966.txt; echo \"=== page markers near ===\"; awk 'NR>=6100 && NR<=6300 && /^[0-9]{3}$|^ *[0-9]{3} *$/ {print NR\": \"$0}' KLN_1966.txt | head -20",
 "description": "Read Klein calvary entry and page markers"
}
```


### [2026-09-06T16:06:28.125Z] TOOL RESULT

```
calumniator,  n.,  slanderer.  —  L.,  fr.  calumnialus.
226
227
pp.  of  calumnidri.  See  prec.  word  and  agential stiff,  -or.
calumnious,  adj.,  slanderous.  —  L.  calumnidsus, fr.  calumnia.  See  next  word  and  -ous. Derivatives:  cahtmnious-iy,  adv.,  calumnious¬ ness,  n.
calumny,  n.,  slander.  —  F.  calomnie,  fr.  L.  calum¬ nia,  ‘trickery,  artifice,  pretense,  evasion,  false accusation,  false  report’,  for  *calvomnia,  from *calvomnos,  archaic  pres.  part,  of  calvi,  'to  de¬ vise  tricks,  deceive’,  which  is  prob.  cogn.  with Gk.  xtjXeiv,  ‘to  bewitch,  seduce,  beguile’,  Goth. hdiort,  ‘to  deceive’,  ON.  hoi,  ‘praise,  flattery’, OE.  hot,  ‘slander’,  holian,  helian,  ‘to  slander’. Cp.  challenge.  Cp.  also  cavil.  For  the  form  of the  pres.  part.  *calvomnos  cp.  alumnus.
Calvary,  the  place  of  the  crucifixion  of  Jesus;  re¬ presentation  of  the  crucifixion  of  Jesus.  —  L. calvaria,  ‘skull’,  translation  of  Gk.  xpxviov  in the  Gospels,  rendering  Aram,  gulgulthd,  ‘skull’
( -----  Heb.  gulgoieth),  a  name  given  to  a  hill  near Jerusalem  (so  called  from  its  shape;  see  Gol¬ gotha).  L.  calvaria  is  a  derivative  of  calvus, ‘bald’,  which  is  cogn.  with  the  second  element in  OI.  ati-kulvah,  ati-kurvah,  ‘utterly  bare', Avestic  kaurva-,  ModPers.  kal,  ‘bare’.  Cp. Calvatia,  calvities.
Calvatia,  n.,  a  genus  of  fungi  (hot.)  —  ModL., fr.  L.  calvus,  ‘bald’.  See  Calvary  and  -ia. calve,  intr.  and  tr.  v.  —  ME.  calven,  fr.  OE. ceaifian,  fr.  cealf  ‘calf’.  See  calf,  ‘young  of  a cow’.
Calvinism,  n.,  the  religious  doctrine  of  John  Calvin (1509-64).  Cp.  chauvin.  For  the  ending  see  suff.
-ism.
Calvinist,  n.,  a  follower  of  Calvin.  —  See  prec. word  and  -ist.
Derivative:  Calvinist-ic,  adj. calvities,  n.,  baldness  ( med .)  —  L.,  ‘baldness’,  fr. calvus.  See  Calvary.
calx,  n.  (client.),  1)  lime  ( obsol .);  2)  ashy  sub¬ stance  left  after  a  mineral  or  metal  has  been calcined.  —  L.  calx,  gen.  calcis,  ‘stone,  lime'. See  calcareous.
Calycanthus,  n.,  the  Carolina  allspice  (hoi.)  — ModL.,  compounded  of  xaXuE,  'cup,  calyx",  and iv&o;,  ‘flower’.  See  calyco-  and  anther, calyci-,  before  a  vowel  calyc-,  combining  form meaning  ‘pertaining  to,  or  resembling  a  calyx’. —  Fr.  L.  calyx,  gen.  caiycis.  Sec  calyx, calycle,  n.,  an  epicalyx  (hot.)  —  L.  calyculus,  'a small  flower  bud',  dimin.  of  calyx,  gen.  caiycis. See  calyx  and  cp.  calicle.
Caiycocarpum,  n.,  a  genus  of  plants  of  the  moon- seed  family  (hot.).  —  ModL.,  compounded  of vdj:  >1,  gen.  xaXuxoc,  "cup,  calyx’,  and  xa prop, ‘fruit’.  Sec  calyco-  and  carpel  and  cp.  the  second element  in  Callicarpa.
calyculus,"  n..  a  small  cup-shaped  cavity.  —  L. Sec  calycle.
Calypso,  n.,  a  nymph,  daughter  of  Atlas  ( Greek mylhol.)  —  L.,  fr.  Gk.  KaXuiJxo,  from  the  stem
=== page markers near ===
6158: 222
6169: 223
6187: 224
6188: 225
6239: 226
6240: 227
6276: 228
```


## [2026-09-06T16:06:38.746Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"sogdian loan\" HENNING_selected_papers.txt | head; echo \"=== krw ===\"; grep -n \"karva\\|karwa\\|krw\\|karvah\\|kurwa\" HENNING_selected_papers.txt | head -40",
 "description": "Grep Henning selected papers"
}
```


### [2026-09-06T16:06:38.813Z] TOOL RESULT

```
11763:we may take this opportunity of mentioning a hitherto unrecognized Sogdian loan-word in Turkish, viz. Turk. gly ni, i, 430; ili, 134 ‘andalib; Ton Muhanni, 176—Aaxir) from Sogdian
11770:milar Sogdian loan-words in Pe nd-wif, ete,
=== krw ===
1130:dast erkaé (which need not be changed into das [pat] érkat), see Bailey, BSOS., vii, p. 73. Sogd. (16) ‘with crossed arms, ef. SCE., 400, and prBrtp'8 “ cross-legged", Dhydna, 18. The verb, prByr- (pari biraya-), occurs in Dhuta Bstw pryByr " he crossed his arms (prBrtytKara-Balgasun, p. 22, frag. xi, 4, is not clear).—{17)(18) “ Whip. Sogd. auiép from zivagpa-, of. Av. zhaZwayat.altra, and NPers. 2b “whip, whipeord” (Rind. ; Asadi, p. 8; Div. Nasiri Khosrou, 429), Wakhi rafip “ whip" (Morgenstierne, IJFL., i, p. 588). Closely related is Buddh. "yrel'yp- “ squint-eyed", see BBB., p. 63. MPers. asp-azan " horse-whip”, of. Arm. garazan, zarazan. MPers. ‘spiwon (den from 4yavana-?) occurs in an unpublished MPers. 'pswn 'y tb “spell against the fever” (M 781), where féyr “sword”, eyl’n (see below, on g 1, 2), and "sph "whip" follow each other—(19) “teeth”. Sogd. zwrn- = “* blood” (but a separate word *zwrn- “food”, or “banquet ”, is, of course, possible), pinork = Buddh, pyerk- SCE., 28 (said to mean “ dark-coloured), or from plyer- “to lacerate, devour” (R.. i ¢ BBB., p. 91), cf. 'ply'r, Vay 313, 949, Therefore, Sogd. =“ bloodstained teeth” or “blood: Jacerating teeth" (? “‘laniaries?"). MPers. "ned could be avid “rubbed, blunted ” (ergo “‘ molar teeth?”), or dsd8, 1, “useless,” 2, “ not rubbed " (NPers. side) = “ sharp teeth !"" Speaking of teeth, I should like to add to my recent remarks on Sogd. krw-Bnt'k “ having defective teeth", BSOS,, x, p. 96: the word knw- still exists in modern Birjandi Persian, as Eabrd, Eawerd “ toothless”, see Ivanow, JPASB., xxix, 4, p. 340. This makes it unlikely that NPers. kare(e) had been borrowed from Sogdian.—(20) Pte. pres, pl (21) 3nd pl. pres, (or subj.), MPers. pret. pass. =Sogd. abstract from pte. pass. + hy became, took place", (28) iterative pte., from MPers. "em- = Sogd. ()pF'm both of which are unknown. It seems likely that the words connected by etymology, notwithstanding the apparent discrepancy of thesibilants.? But MPers. swyy = svyay, Pabl. sud = suy compared to Av. dud- allow the derivation of MPers. -sam- from Olr .-fam- Av. afama- "to swallow, gulp” (NPers. dédmidan),* .- from *apa-Mma-? The appearance of an iterati
1488:discerning, reason” ! (8) “Knowledge, cognition. —(9a) “He recog- nized, perceived” (for Sogd. "'p'y- see BBB., p. 90).—(9b) Same. Sogd. f'in'[s? Impf. of *fin’s- from Olr. *fra-(z)indsa-?—{10a) See above, a 21.—(105) “Split.”—{Ila) Pl. of ‘shir = yw. Sod. Byw8 clearly denotes some sort of “covering” (cf. Buddh. pty'w8, ete.), and MPers. askofr? seems to represent Olr. *skabra-, from the base skamb “to stem, prop’. Hence, “a covering whi propped up,” eg. "roof", or “ceiling”, ete—(11b) The words are ‘etymologically identical. Perhaps MPers. ‘ifrs is the original of Talm. by) m’ “a tall wine-cup” (8. Fraenkel, Aram, Fremdw., Pp. 208 sq.).—(12a) " He recognized.”—{12h) “ He propitiates ” (ete.),  denominative verb, from MPers. indim (Sném), cf. Hubschmann, Arm. Gr., p. 214. ‘The Sogdian translator used a similar form, 2 By the way, it seems possible that Sogd. 'zin'm ‘* absolution tinues Olr. *zinduma-—(13) Of. Sogd. n’j-, BBB., p. 94 (b 60), where Dhyna 401 should be added. According to F. Weller, Mon. Serica, ii, p. 382, Buddh, n's- is “to tur, roll". While it is naturally impos- sible to guess the meaning of Bn'j- (i. abi + n'j-), one might: conjec- ture “‘ stumble”, since the restoration of MPers, [‘ékrury]st seems to impose itself. After all, the number of MPers. preterits in -st which begin in ‘é-, is rather small (ékst is too short), MPers. ‘skrweyet is attested in Mir. Man., i, see Zachner, BSOS., ix, p. 315 (the spelling ‘ékrust, at normal Man
5396:(Frg.d, frst page) (228)) (An)g{(229)tphy (ke ‘y 8h 00 pa ax ry(x)(t} (230) ign d’d 00 mf'n'gh231\inyws]g ky nbyg nby(sy)(a}(252) [c'w)n) myrd 'y wym'r oo ky zy{(233) mJyrd d’d oo nywi'g k{y(234) [xwybs] dwxt ‘w dyn dyyd oo m'nge!*(238))igirwg'n ky pws "(w)(236) }(bjmwxtn d'd 00 *w(237)|(p)yd grwg'n (238)]. 'w (Frg.d, second pag) (239)}dwn(d)(240)(ny] wg oo dudy m'n'g nyw{a’g (241))'myo ‘skrw{(242) [p]'¢yThyd 00 gryw 'e dyn w{(243)(o))wn an ‘y hrwm'y o0 k(y)[(244) [FpyTdg ‘yw mwg k{(245) qybyo pa dyn'(\{ (246)bwd oo w'd god yk ((247) "hyd bwd 00 pr{(248) ‘eo bwnl (249) bw(d
8055:kw ! "py ‘pat ZY (20) [Ay krw kpy ywrt] 3'rt [
21360:* “Taseriptions de Surkh Kota, J, 1964, 189-205 # XPONO, fase. Nn 2 (Corie pp. 1084), may bem krwpa (rw) "reign -prid, rue "ef B. Beneenite, Testes soplens, p. 17%, The M in BSOAS, 2%, 72 aloud be read asd rentored as (ZlewBBy8'nyy m= aynagogoe tho ‘orrespooding Middle Persian word was presumably gen
```


## [2026-09-06T16:06:40.280Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"کروه\" BQT_v3_pages.txt 2>/dev/null | head; ls incoming/BQT/; echo \"=== v3 ===\"; grep -n \"کروه\" incoming/BQT/BQT_v3_pages.txt | head -20",
 "description": "Grep Borhan for karveh"
}
```


### [2026-09-06T16:06:40.396Z] TOOL RESULT

```
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
=== v3 ===
1107:‏ام موضعی است که کروهی از کبران درآن‌توطن
3410:‎Rosa canina= ۴ ۰ ۷۳۰ ‏دزیج ۱ص‎ Dy. ‏ام کروهی از نبانات‎ - ٩
7946:۸ - «شویزیه ؛ مقبره‌ایست ‎shady‏ درجالب غربی آن ‏ و کروه بیار از صالحان بدانجا
9807:‏(۱)چش : بکروه .
11169:‎aml‏ , جماعتی و کروهی ازمردم را کوبند که
13590:‏۱« غالوك » ‎tg‏ کمان کروهه باشد . خروانی گوید :
13592:‏کمان کروهةٌ زرین شده محاقی ماه
14863:‏بهر تلی بر . از کشته کروهی - بهر غفجی در. از فرخته‌پنجاء»
18238:مانند رسیدن آسیبی ومکروهی وبابکثرت‌دست
25340:کروهی که کانوزبان ‎tale‏ برسم پرستند کان دانیش ..
27829:‏۱ -(ع) ‎BES?‏ ( تج ) کروه » ‎BES"‏ ( بش اول و سوم کرد دهم پیوسته از
29722:‏ک رکدن‌فءل‌جمله بتوهند کر بسوشکل‌جملهمکروهند. ‎ee sr El‏ «نفیسی.رود کی ج۳ص ۱۱۷۰ ۰
30105:شوخ ,وسخ‌و کرس بود که برتن نشیند و کروهی مردم عامه‌چرلنیز کوبند .» «لقت فری*۸ * .
30384:‏۱ -«کرف 1 قیرسوخته و کروهی سیم سوختّه را گویند » سیم درست بود . کائی
30542:کر کروهن © بفتح ‎wily ely Jol‏
30985:‏۶در شاهنامه دوه کروه
30986:۷ کروه :
31046:‏کروه = نم اول و انی ‎sly‏ مجهود
31070:اقفانتان « کروه» هستعمل است « فرهنگ ‎llr‏ » در ساتمکریت ۳052 ( اصلا آواز و ‎Clans‏
31127:. ‏باز چون بر گرفت دست ز روی کروه دندان و پشت چوکانت‎
```


## [2026-09-06T16:06:53.009Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Loan-Words\\|Loan-words\\|LOAN-WORDS\" HENNING_selected_papers.txt | head -20",
 "description": "Find Henning SLW article"
}
```


### [2026-09-06T16:06:53.062Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:06:58.492Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /BSOS., x, p. 96/ {print NR}' HENNING_selected_papers.txt; echo \"---titles---\"; sed -n '1100,1135p' HENNING_selected_papers.txt | cut -c1-200 | head -40",
 "description": "Locate Henning leaf and context"
}
```


### [2026-09-06T16:07:00.299Z] TOOL RESULT

```
37
---titles---
+ 1920, p.420, this is Skt. mahidewa ; but in &
 
mahddeva would sure
  
seems to me that mya
 
from Parthian mgbyd (BSOS,, ix, p. 85) = maypeb, with > mayBeB. Although the institution of the May
crown) was most likely taken from the Sasani the word itself seems to be (o) in the first syllable (MPe On the other hand, § but mayu- is muy- in Sogdian (of. ¢.g. LeCog, T.M. i, p. 39).—(12) (13)
 
    
e5 as a minister (of the
   
state, nevertheless
 
  
n as is suggested by the absence of
moypet, moyBeB, mowBe5, moped),
  
dian frequently fails to preserve the vowel u;
 
   
cooled, frozen”. All forms from the base of Av. sarata- (cf. Horn, Grd. Ir. Phil, i, 2, p. 141 ; NP. afsdndan “to press” is probably a mis- spelling of afsardan)—(14) “Institutions,” etc.,
 
 
 
 
       
adairi kasazibya, Pabl.
   
MIDDLE PERSIAN-SOGDIAN GLOSSARIES 2
dast erkaé (which need not be changed into das [pat] érkat), see Bailey, BSOS., vii, p. 73. Sogd. (16) ‘with crossed arms, ef. SCE., 400, and prBrtp'8 “ cross-legged", Dhydna, 18. The verb, prBy
```


## [2026-09-06T16:07:09.094Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'NR<=31130 && /\\[pdf page [0-9]+\\]/ {p=$0; n=NR} END{}' BQT_v3_pages.txt\ngrep -n \"\\[pdf page\" BQT_v3_pages.txt | awk -F: '$1<31130' | tail -3\necho \"=== context ===\"\nsed -n '30975,31135p' BQT_v3_pages.txt",
 "description": "Locate BQT page for karveh"
}
```


### [2026-09-06T16:07:10.661Z] TOOL RESULT

```
30919:[pdf page 422]
31000:[pdf page 423]
31072:[pdf page 424]
=== context ===

‏۱ - ونیز شهریست بانداس > معجم‌البلدان * ۴ مصحف « خاری است © ‎dy‏
‎GE Sl‏ اتترخوار , شترخار - درسامی «کرنه ‏ بمعتی کنهآهده . و چون «کنه » را ائترخوار
‎Cow)‏ هم میگفتند . این معثی را برای ‎Kas ol‏ توبان استاباط کرده اند ‎dbs.‏ :گرنه.
۴ - لفتی است در «کنه ‎٩‏ . ۴ ره :
° = کره < کری ( بضم اول ) « رشیدی ©
آمده ‎x59,5!‏ 0 -کروخان.

‏زد که ‎VLG‏ بار سیم دندان طمع

‏۶در شاهنامه دوه کروه
۷ کروه :
سزد که او نکند ‎nab‏ پیر دندان کرو.
‎LT‏ مروزی * لفت فری 4۱۱ ۰
رگ : عبارت آخر همین ماده . ۸ - این معنی را جهانگیری از شمرسموی امتثناط کرده:
جوانی ‎Selly‏ (و) پا کروبود که با پا کیزه‌روی در کروبود
شنددستم که در درمای ‎pel‏ بگردابر در افتادند باهم.
رشیدی کوید او درین ممنی منفرد است. معتی مزبور درست نیست ۰ چه از بیت دوم تلویسا بودن
آنان درکشتی استنباط میشود , وصحیح « در گرو بود» است بعنی عاشق او بود و مشهور هم‌همین
است . رلك : فرهنگه نظام و ‎Ay‏ : کلستان مصحح قریپ ص ‎٩ N00‏ -رك: ح ۷
*-«کروان ‎WT pw‏ دهی است بطوس - و کيك - وچویینه - وشوات. کروانة مونت»
« منتهی‌الارب *. ۱- (عی) کروین و کروییون و کرویه . ازعبری «کروب» ‎chert‏
‏( جمع کروبيم ‎(Cherubim‏ در ‎GCL, gue aye‏ اطلاق شده که دائماً زد خدا بودند(سفر
تکوین ۲۶:۳ ؛ سفر خروج ۱۹:۲۵ ؛ حزقبال ۷۱:۱۰ * اصل این‌کلمه آنشوری است‌بمعنی‌پاسبان
رك : نفی .
[pdf page 423]
Tht ‏کروت‎

۱ و فتح ‎UU‏ وسین ‎this‏ ساکن . لغزوچیستان

پاشد

کروت © بضم‌اول بروژن فروت»بممنی |
فربه باشدکه دربرابر لاغراست ۷ .

کرو تنه ؟ ‎he‏ اول وثانی وفوقانی ,
وتون وسکون ثالث ؛ عنکیوت را گوبند .

کروخ ‎ae‏ اول و ‎JU‏ و سکون ۱
‎IL‏ و خای نتطه دار . نام قربه‌است از فرای
عالم ۴ .

کروخان ۴ ‎lo‏ خای نتطفداربروزن
خروسان (۱) نام برادر ‎he‏ ویسه است. ۱

‎os‏ بشم اول بروزن سرود . چاه
بیار عمیق را گویند که آب از آن بدشواری
توان کشید ؛ و بفتح اول هم کفته‌اند ۵ .

‏کر ود ه با زای نقطه‌دار بروزن‌خروس»
‎ine‏ عیش وشاط و شادی و طرب باشد ‎٩‏ -
واندوه وملالت را نیز گفته‌اند؛ و با زای فارسی
هم‌آمده است .

‏کروس» بکر اول و سکون ‎BU‏

‎PF ‏اول بر وزن‎ eae PIS
. ‏شکنبه را گونند‎

‎Shane ۲ FIST‏ کاف بر ون
کبوتر. یکی ازنامهای‌خدای‌تءالی‌است جل‌جلاله.

‎en MOIS‏ اول و فتح‌نالكوسکون
ثانی و نون » اسبیرا گوین که رنگه اومابین زرد
وبور باشد .

‏کرو نیی ۰ بفتح اول و انی ‎dy‏
‎ay‏ و نون بشحتانی کشیده و بین بی‌قطفزده,
تام جزیره ات که وامق مطلوب عذرا در ‎OV‏
‏جزیره میبود ‎AY)‏

‏کروه = نم اول و انی ‎sly‏ مجهود
رسیده و بها زده » تلث وسه يك فرسخ را گویند
وآن سه هزارکز است وبعضی گویند چهارهزار
کز*۱و زیاده ازین بیست و آنرا بعربی کراع

‏(۱) چش : خرومان . (0) خم۱: میبوده .
۲ -کرچه در تألیف این ابیات لیست بی سمین غثی وغلی ب یکووت .
انوری اییوردی « فرهنگه نظام 6
‎brace ۴‏ ۴ -کروخ بفتح اول » شهری بود که بين ‎OT‏ وهرات
ده فرسنگه مسافت ‎ay‏ و کشمش ‎OT‏ مشهور بود . رك : عمجم‌البلدان , و رك : چهار مفاله طبع
تگارنده ص2۳ ‎AR,‏ . ۴ رگ : کرو . ۵ -رك : جهانگیری . رشیدی.
۷ - چون ‎Jo‏ باده‌خوار گشت جهان با نشاط و کروز وخوش منشی .

‏خروی « لغت فری ۱۷۵ *.
۷ - محیح « کر وگر» است. ۸ = کرن ‎Cpr)‏ ورثك: کرند, کرنده؛ کرنگه.

‎: ‏عنصری (بلضی) گوید‎ oy ‏درلفت فرس * کروتیس, جزیره ای بود که وامقآنجا‎ - ٩

‏جزیره یکی بد بیونان زمن کروتیس بد نام شهری کزین ۰ ۰
‎cal?‏ فرس ۷:۳ >
‎ol‏ همان > ‎Crétes,‏ ( اقربطش ) باشد ( دهشدا ). *۶- مافت قریب دو میل که

‏۰ کر است . جهانگیری و رشیدی بممنی ثلث فرسنگه که يك میل باشد نوشته‌اند . لیکن
این لفظ درهندی دکوس» 2 درسانسکریت کروش است که بمتی دو میل انگلیسی است » و در
اقفانتان « کروه» هستعمل است « فرهنگ ‎llr‏ » در ساتمکریت ۳052 ( اصلا آواز و ‎Clans‏
‏مافت ی که آواز برسد ) «دکتر راجا > .
[pdf page 424]
TAN

خوانشد ۱ - و بمعنی آرامگاه وآشیال ‎by‏
‎ands‏ نیز آمده است ۴ - و بفتح اول و الث
وسکون ثانی,دندان ‎Oe‏ تهی وکاواك رااگویند ۴
— و بفتح اول و انی و الث , جانوری باشدسیه
رنگه . گوبند زخم آن جانور زیاده بر زخم‌مارر
است ۴ .

کرو * = بروزن اغنیا . تضمی است
که آنرا زیر رومی کوبند و نان خواء همان
ابت . بر روی خمیر نان پائند و خوردن ‎OT‏
‏بناشتا قوت ممده دهد و کرویه(۱) و زینان عم

کرویز 1 © بفتح اول وسکون انی بر

وزن شبدیز » بمعنی ‎ghd‏ و ادراك ‎AL‏ باشد

و شرف انان ‎Hl‏ فشیلت است ؛ و بفتح اول
‎gly‏ هم آمده است.

کروی‌دده ۷ ۰ بکرزای ‎dat‏
‏ورای فرشت و سکون ها . تام ,یکی از خویشان
افراسیاب است و او در کشتن سیاوش سعی ‎Bot‏
‏کرده است ‎Ax)‏

, ‏بنتح اول و انی و خفای ها‎ oS
‏پوست دست و پا و اعضا را گویند که سیب کار‎
- ‏بسته (۳) باشد‎ aig ‏سخت شده و‎ he ‏کردن‎
‏چرك هم آمده است که عربان وسخ‎ gine ‏و‎
‎۰ ٩ ‏گویند ۸ (4) - و که را نیز کنتهاند‎
‏وآن روغنی باشد که از دوغ گیرند - و بمعنی‎
‏کاروان سرا و مدرسه‎ Ste ‏حچره هم هست که‎

(۷) چش: - ‎gly‏ .. کرده است.
(4) چك » چش : میگویند :

۱ -« بدانکه لفظ کراع که در جمیم سخ موجوده برهان فاطم بهمین شکل وعنوان
واقع است » درین مقام بغابت نامناسب است ‏ زیرا که بمعنیی که مراد مسنف است دز کتب

لغت ‎oe‏ با وجود تفحص نام اصلا بنظر نرسید:

۴ - بردش دمان تا بالبر زکوه

HOON dle,

که بورش بدانجا کنام 699
فردوسی طوسی « فرهنگه نظام *.

(karve)., 5: Sie ‏درفهرست ولف این‌کلمه نامده . ۴ = (ه.م.).‎ Jy
‏سوراخ » دندان فاسد ) ( اسدی , ص۱۱۵ ) , همچنین کرو ۸۳۷ ؛ شمس فخری‌س۱۱۳برك:‎ )
‏سفدی 8006 - 627۷ ( دارای دندان مجوف با فاسد ) ؛‎ (a ۸۲4 ‏ص‎ T ‏فولری‎
‎Henning, Sogdian loan words..,BSOS ‏رخنه)‎ , Gt - ‏خالی‎ ss) krw? ‏نیز‎
‎. 2 ۰. 1 , 0 . 6۰
. ‏باز چون بر گرفت دست ز روی کروه دندان و پشت چوکانت‎
EAN ‏سمرقندی « لفت فری‎ Soy,
‏رك : رشیدی + ۵ رك : کراوبا . ۱ ۱ -ظ . برساختة فرقةً‎ ۴
‏ضبط کردهء‎ » Gurdt Zitih ‏آذرکیوان . ۷ - ولف در فهرست شاهنامه «گروی زره‎
: ‏نام قهرمانی تورالی‎
‏از کام و داد تزادست و ه رگز مباد این بزاد.‎ SGT ‏گروی زره‎
۱۹5 ‏فردوسی طوسی . شاهنامةٌ بخ ج ۶ ص‎ «
‏این هردرپاك بینم وآن هردوبا کره.‎
> ۳۸۶ ‏خسرو بلخی ص‎ ol?
```


## [2026-09-06T16:07:23.091Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk '/\\[pdf page 458\\]/{f=1} f{print} /\\[pdf page 459\\]/{exit}' BQT_v3_pages.txt | head -80",
 "description": "Print BQT v3 pdf page 458 (kal)"
}
```


## [2026-09-06T16:07:24.848Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN sim ===\"; grep -n \"sīm\\|sim \" HRN.txt | grep -n -i \"joch\\|Joch\" | head -20; echo \"--- direct\"; grep -n \"Jochbaum\\|Joch\" HRN.txt | head -30",
 "description": "Grep Horn for sim yoke"
}
```


### [2026-09-06T16:07:24.891Z] TOOL RESULT

```
[pdf page 458]
‎ST‏ ۱ = بنتح ارلوکس ثالی‌وسکون
زای فارسی » تره تیزك را گویند و ‎OF‏ سبزیی
باشد خوردل ی که بعربی‌جرجر وایهقان خوالند.
کلکش © «بفتح‌اول وکس‌نانی‌وسکون
شین نقطه‌دار. بمعنی ‎ST‏ است که‌تره‌نیزكباشد .
ککمک .- بروزن چشمك, چیزی‌باشد

‏سیاه که بررو و الدام مردم بهم میرسد و آثرا
ماه گرفت لی زگوند .

‏ککه ۴ = بنتح اول و ثالی ۰ فنله
و افکندکی آدمی باشد و بعربی براز و غایط
گوبند .

‏کلکی ۴ = بنتح‌اول و ‎GES‏ بمعنی
ککه‌است که فضله وافکند کی وغابطآدمی‌باشد*

‎oly‏ هیجدهم(۱)

‏در کاف تازی با لام مشتمل برریکصد وشصت وسه لغت و ‎CALS‏

‏کل « بفتح اول و سکون ثانی » کچل
را گونند ‎gn ٩‏ شخص یکه سراو زخم با جای
زخم داشته ‎ath‏ وموی نداشته باشد واورا بعربی

‏(۱) خم ۱ : هجدهم .
‎Koes < ۸‏ («م.). ‎kakaj SS‏
‎Om ۴‏ (هم.) در تکلم اسفهالی اين لفظ هست و باکس اول است ؛ املجهادگیری
ورشیدی با فتح اول ضبط کرده‌اند , قس :طبری 6662 ( پشگل کوسفند ) « واژه نامه ۸۲ه ».

‏پاکی و پلید کردی آنگه
سوزلی سمرقندی « فرهنگه نظام >.

‏اقرع خوانند ۷ - و ‎ay‏ جمیع حیوانات را
کونند عموماً 1 ‎ges,‏ بر را خصوصا ۷ سوم
اول» خمیده‌پشت وکوژه(۲) ومنحنیرا گوبند۸ -

‏(0) چك : کوزه =

‎GES) som ۴

‏برکون کسی که بد ‎BSS‏
‎ps) Km ۴‏

‎. kalzs 5. « ode ‏واژ‌نامه‎ « Kal ‏طبری‎ , Cpa) » ‏مخفف «کچل‎ - ©

‏۲ - اکهانی جولقیی میگذشت
طوطی اندر کفت آمد در زمان
کزچه ای کل با کلانآمیختی

‏با سری بی موچوپشت طاس وطشت
‎Sb‏ بر درویش برزد کای فلان
نو مگر از شيشه روغن ‏ ربختی .

‏« مولوی بلخی رومی . مثنوی چاپ علاء‌الدوله ۷ +
۲ - طری 681 ( بز بر ) « واژه‌نامه ‎lash Coan‏ کنونی ‎Ty) Kal‏ و گوسفند

‎ply‏ وبز وکاو کوهی ) , در لهج فاری 81 (کوسفند ‎clay‏ » نر باشد یا ماده ) « فرهنگه
‎pls‏ کردی ‎keel‏ (کاومیش ) « ژابا مس ۰۳۳۹ , ‎kala ] ۷۵۲2۵۷ SOS‏ ( ورزاو فوی) .
در بروجردی ‎gow‏ 8 - 811 (گاو ر ) «شهیدی» .
‎A‏ - بقول « ‎Miindliche Mitteilung ( » ub‏ ) ماخوذ از ‎xullés guy‏
‎SD)‏ منحنی ) قس ‎tats‏ اوستابی - 8687608 (گرد ) ‎Sy.‏ : اسشق ۸۹۱وهوبشمان۱٩۸‏ -
جپانگیری بیت ‎dad‏ را رای این معنی شاهدآورده :
بدانگه که گیرد جهان کرد ‎bee‏ کل‌پشت چوکانت کردد سنیغ. ابوشکور بلخی.
‎ny lp‏ نظام پس از نقل ابیت فوق نوشته : « از شمرکجی و الحناء فهمیده
میشود له کج ومنحنی ». در رودکی تألیف آقای نفیسی ج۳ ص ۱۲۳۹ بجای « کل» ,«کل»آمده.
[pdf page 459]
```


### [2026-09-06T16:07:24.960Z] TOOL RESULT

```
=== HRN sim ===
--- direct
3943:423. Juy *Joch', vergl. yöy.
3945:ai. yugd" *Joeh\' arm. lue *Joch* (H. No. 129).
3946:kurd. jülc (H.-Sch.), vergl. yüzen *der das Joch am
6647:KZ. 25, 530 Note 200); ai. cdmyä- 'Jochbalken
6656:Stützhülz (am Joch)'); arm. .sami\/v 'Stirnliolz des
```


## [2026-09-06T16:07:39.561Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6635,6665p' HRN.txt; echo \"=== leaf of that ===\"; awk 'BEGIN{RS=\"\\f\"} /Stirnliolz des/{print NR}' HRN.txt",
 "description": "Print Horn entry for sim"
}
```


### [2026-09-06T16:07:41.302Z] TOOL RESULT

```
*Bratspiess'.
skr. gikha- 'Spitze (eines Pfeiles etc.)', vergl. cekh-
ara- (?).
kurd. stx^^ si/ü *Lunte* ; bei. slh^ sl *Bratspiess, Lad-
stock' (344).
763. si^deh 'dreizehn*.
aw. dridasa 'dreizehnter'; phlv. sicdahum^) (päz. seS,
sez"); ai. trdyödasa,
kurd. dausCf slzdeh (LW.); afy. dyärlas.
np. sizdeh ist eine Analogiebildung.
764. s~ui% 'Kummet'*).
aw. sima^ vergl. siimiSra- yt. 10, 125 (Geldner,
KZ. 25, 530 Note 200); ai. cdmyä- 'Jochbalken
(nach Geldner; PW. hat 'Zapfen, Holznagel, Keil,
1) Nach Nöldeke bei Hübsohmann, KZ. 23, 402.
^) In E^snadäsa^s Pärasiprakäga aus Akbar^s Zeit findet sich nur
{Mia- (No. 723), wie die heutige indische Aussprache lautet.
*) Vergl. Seite 128 Note 6.
^) Ich vermag mir nach der bei Vullers abgedruckten persischen
Erklärung keine rechte Vorstellung über die Verwendung des sim zu
machen, doch scheint es unserem 'Kummet* nahe zu kommen.— 169 —
Stützhülz (am Joch)'); arm. .sami\/v 'Stirnliolz des
Ochsenjoches (de Lagarde, No. 19:^8) i).
Xp. sim *Silber , sitnm 'silbern' (phlv. usltn, astnnn)
dagegen ist bekanntlich griechisches Lehnwort (vergl.
zuletzt Nöldeke, Pers. Stud. II, 45).
765. sl/inury 'Greif, Adler; N. pr.', vergl. STn\duxt,
aw. saenö mereyö- *Adler' ; phlv. stnmuro, seiw murük
(Yätkrtr-r Zar. S. ()4).
ai. ^ijefui' Talke*; arm. ein milvus (H. No. 280).
S,
=== leaf of that ===
191
```


## [2026-09-06T16:07:51.621Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sima\\|sīma\\|simōiθra\\|simoi\" AHM.txt | head -30",
 "description": "Grep Gershevitch AHM for sima"
}
```


### [2026-09-06T16:07:51.677Z] TOOL RESULT

```
1711:‘Drei wirklich der Wahrheit Ergzebene fluchen Verwiinschungswarte: das Rind, das Pferd und der Hauma’ (La.), Accordingly hai3im.- asavajanas’ is yy everyady taken to mean ‘who slay those who are really (ar truly) owners of Truth’. One immediately asks: wha are the ‘really’ asavan, and in what respect do they differ from ordinary afavan-s? Are there beings more ‘really afavan’ than Ahura Mazdah, who yet is simaly called aSavan? Y 11.1, the only passage from which we learn what sort of heingsare considered haidim . afavan-, suggests that‘ really’or‘ truly’ isnot in this case an exact rendering of hai9im. It should be noted that haama- in Y 11.1 is not the god, or even the plant, but as appears from Y 11.3, the drink pregared of the plant; this drink, naturally enough, is identified with the asavan gad Haoma in Y 74.3, but it nevertheless can be called agavan only by extension of the proper original use of the word.t The game extension has to be assumed in the case of ardinary cows and horses.
2418:125%. Gdn. already recognized that sim@- belongs ta NPers. sim and Ved. sdmya; but in translating it by ‘jochbalken’ he paid insufficient attention to the meaning of these cognates, wich is ‘pin of a yoke’, similar ta Arm. samz-X ‘legni curvi uniti al xiogo, che si pongono intorno al colle di bue’, see Htibschmann, Arm. Gr. 483, and Pers. Si. 79. Beside stma- we have Av. sami- in the compound restored by Reichelt (Warter und Sachen, x11, 238) as yuyd.sami~ Wnd. yugasamyd ‘yoke together with the gin’, cf. also Duch., Coma. 45 sg., and Benv., J As. 1938, 533- From dialects Morg. has added Munji sam ‘yoke-peg’ and Sistini simak ‘yoke-key’, see IIFL, 1, 247. From the IE point of view the relation between Av. stma-, etc., Gr. «duxé on the one hand, and Av.
2420:alternation *kHm+:*kHém-. Bth.'s interpretation of sima- as ‘Halsring, d. i. ein vom Joch ausgehendes, den Hals des Pferdes umfassendes Rundholz’ is not satisfactory, since what closes the ‘ring’ beneath the horse’s neck appears to de the simarPra-.
2421:125°. On sima9ra- again there is no agreement. Gdn. has ‘horse- collar’, Bth. and Lo. ‘yoke’, Justi ‘central part of the yoke’ (Handbuch); Hzf., 469, vaguely rendered simgméca simai3ramca by ‘yoke and what
2424:belongs to it’. As simdi3ra- obviously contains sim@-, its relation to the latter is quite likely that of Arm. sameti-2 to sami-k. sameti-k is the strap which passing underneath the neck of the animal connects the twa yoke- pegs. In Hiibschmann’s opinion the word represents *sami-a-ti, -a- being the compound vowel, and #7 belonging to Gr. 5d ‘to bind’. We may simi- larly analyse simai#ra- as consisting of stma + -it- (reduced grade of yat-, which in OInd. occurs with the meaning ‘ta join, connect’) + suffix -ra-.
2430:(1) ham .iva- ‘complex yoke’. (2) sima- ‘yoke-pin’.
```


## [2026-09-06T16:07:52.563Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==289' AHM.txt | head -60",
 "description": "Print AHM leaf 288"
}
```


### [2026-09-06T16:07:54.169Z] TOOL RESULT

```
ollzogene’ (Lo.); ‘Durch die untere (= auf Erden) gespendete Verehrung will ich kommen, durch die obere gespendete (also infolge der durch die geistigen Opferwirdigen gespendeten)’ (Htl.). We are obviously in the presence of two cam- pounds, adara.data and upara.diéta, which serve as adjectives to namanha, Since the function of ?da@ta- here is most likely the same as in ataraSata-‘xiven by fire’, namd adara.datam will mean ‘homage paid by an aSara-, a lowly person’, cf, Lat. supplices inferioresque. For the idiom nam3 d&- one may compare stiita gard vahmang...dadamahiéd ‘praise- songs and prayers we offer’ Y 41.1. upara® will correspondingly refer to highly placed persons. One is reminded of the contrast between the lowly (@dr3ng) and the exalted (arafvadnhd) in the Gathic stanza ¥ 29.3.
1x82, On the use of the pronoun ava- in referring to the region of the sky see below, 2. 293.
r18*. It is not surprising to find Mithra addressing Zarathustra, since apart fram Ahura Mazdah other divinities do go also, eg, Anahita (cf. note 45), Haama (Y 9.1 sgg.), ASi (Yt 17.21 sg.), and even AnrG Mainyu (Vend. 19.5, 3). A meeting of Mithra and ZaruthuStra seems to be referred to in the unclear gloss to Y 9.1 midrd xpat zara?ustram, according to Bth., Wa. 1659 ‘Mithra knew Zarathuatra’; differently J. M. Unvala, Him Yast, p. 4, cf. Henning, Sogdica, Errata sheet, and BSOAS, XI, 722 on 671, Zarathustra is seen invoking Mithra in Vend. 19.15.
11g'. That Ahura Mazdah is the speaker of sts. 11g sg. becomes clear in st. 121, The chief god first addresses ZarathuStra, then turns to Mithra ta assure him that he shall be worshiped by the whole animate creation, and finally (in st. 120) announces to men in general that, since Mithra is their protector, they are to drink libations in his honour.
269
119.2] COMMENTARY
119°. It is the general opinion that vayatbya pataratatibya occurs again in the Ya&t dedicated to Srao8a, Y 57.28:
asyanha aspatixya asyanha vatazibya
asyanha varatibya dsyanha maeyaeibya
asyawha vayaétsya pataratazibya
asyavha hvastayé atéhimanayd ‘(the two [actually four] runners are) faster than two horses, faster than two winds, faster than two clouddursts, faster than two clouds, faster than two...birds, faster than two (arrows) which are being shat well- shot’. Here a considerable number of MSS. have the variant Aupatara- taéidxya, While it is hard to see haw such a variant could have arisen by mistake, an original vayaéibya hupat® would be liable to be changed to vay? gat? Sy imitation of the present passage in our Hymn; for the Mithra Yast altogether greatly influenced the wording of the Hymn to SraoSa, as B. Geiger has pointed out {cf. note 411, end of first para.). Ifin Y 57.23 we restore the reading vayaathya hupaiarataéibya, as 1 think we must, then Bth.’s translation of the simple patarata- by ‘im Flug begriffen’, and his analysis of the adj. as a -¢a- extension of an adverb
```


## [2026-09-06T16:08:03.972Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /Gdn. already recognized that sim/{print \"leaf(1-based)=\"NR}' AHM.txt\nawk 'BEGIN{RS=\"\\f\"} NR==288' AHM.txt | grep -o \"^[0-9]\\{3\\}$\\|COMMENTARY\" | head\nawk 'BEGIN{RS=\"\\f\"} NR>=286 && NR<=292 {print \"--- leaf \"NR\" ---\"; print substr($0,1,200)}' AHM.txt | head -40",
 "description": "Find AHM page for sima commentary"
}
```


### [2026-09-06T16:08:05.672Z] TOOL RESULT

```
leaf(1-based)=294
263
COMMENTARY
--- leaf 286 ---
, im Gau, im Land, 0 du hichst zarathuStra- hafter’, except in 39 faras this rendering obliterates the technical character of these terms, more especially of zara9ustré.tama-, for which Spi. and Gd
--- leaf 287 ---
oyce, IMHCP, 138.
216°. huyayna. On this word Wi., who translated it by ‘husband and wife’, wrote: ‘ich identificire den ersten Theil mit dem N, Pers. Suz (read 862) Mann; huya kommt von su erz
--- leaf 288 ---
yasnischen Glaubens’; Htl.: ‘Wie 29 ist M. in..., zu 190 werdend in. .., zu 10099 werdend ist der M. des mazd. Herzenslichtes’; Hzf., 491: ‘The 9ra, sacietates are valid 20-fold between..., 19
--- leaf 289 ---
ollzogene’ (Lo.); ‘Durch die untere (= auf Erden) gespendete Verehrung will ich kommen, durch die obere gespendete (also infolge der durch die geistigen Opferwirdigen gespendeten)’ (Htl.). We ar
--- leaf 290 ---
*patara ‘im Flug’, will be found inadequate. This highly artificial explanation should give way to a straightforward interpretation of the word as representing a ~ta- extension of *star- ‘wing�
--- leaf 291 ---
f.’s odservation is that pasudya, etc., are comitative instrumentals, and the widely held theory based on this passage, that the Avestan Mithra exacted bload- sacrifices from his Zoroastrian worship
--- leaf 292 ---
�dti should mean ‘the pourer’. Moreover, there is no compelling reason why zaataram in ¥ 11.1 should not simply mean ‘priest’. The present context, on the ather hand, seems to be a case whe
```


## [2026-09-06T16:08:14.015Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=660 && NR<=666 {print \"=== leaf(1-based) \"NR\" ===\"; print}' BQT_v2_pages.txt | grep -n \"سیم\\|=== leaf\" | head -40",
 "description": "Locate BQT v2 sim page"
}
```


### [2026-09-06T16:08:15.699Z] TOOL RESULT

```
1:=== leaf(1-based) 660 ===
27:   ‫‪ - ۴‬جوالیقی کوبد ‪« :‬سدیر» فارسیممرب است واصل ان «سادلی»‬                  ‫‪ :‬سه جاده‪.‬‬   ‫رك‬    ‫‏‪١‬‬
62:=== leaf(1-based) 661 ===
122:=== leaf(1-based) 662 ===
196:=== leaf(1-based) 663 ===
217:‫نظام » نام‬     ‫سیم = بکر اول بروزن‬                             ‫و رسد آنرا بجپت ا‪-‬هال خورند ‪ ۷‬و تارسیده‬
267:=== leaf(1-based) 664 ===
337:=== leaf(1-based) 665 ===
406:=== leaf(1-based) 666 ===
```


## [2026-09-06T16:08:19.340Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==663' BQT_v2_pages.txt | sed -n '1,80p'",
 "description": "Print BQT v2 leaf 663"
}
```


### [2026-09-06T16:08:21.221Z] TOOL RESULT

```
     ‫اف‬

‫سیا گیژ ‏ باکاف بروزن فراویز » امد‬                                                           ‫عددی استمتعلوم ‪۱‬‬
                                                                  ‫ا‬            ‫تف‬           ‫سیا ‪ -‬کر‬
                                                              ‫درمقابل سفید باشد ‪ - ۴‬و بقتح اول سنا را‬
 ‫سیال » بفتح ارل بروزن عیال‪ ,‬یاسمین‬
              ‫راکوبند وآن سفید وزرد میباشد ‪.‬‬
                                                              ‫کوبند وآن داروبی است که در سهلات بکار‬
                                                                                                            ‫برلد ‪۴‬‬

                                                                 ‫ر‬
                                                                 ‫اابه؛‬
                                                                     ‫سیاب د بکر اول بورزن لق‬
 ‫و لام مک‌ور بخای نقطه‌دار (‪ )۱‬زده » خارخك‬
                                                               ‫بآراستن‌باشد سنی‌بارای وآ راش ده ‪- ۴‬وبمعنی‬
                                                              ‫حیات همگفته‌اند کهزندکیباشدگ وحباب هم‬
 ‫وخارخك‬       ‫ریزند ‪٩‬‏ ‪-‬‬       ‫واطراف‌قلمها‬   ‫سرراهء‌دشمن‬
                                                               ‫بنظرآمده است‪ .‬ال اعام® _ وبلغت وادی القری‬
                                         ‫را کبفزته‌اند ‪۰‬‬
                                                              ‫بمعنی خلال باشد وان کاس ا تنت که سبز‬
‫نظام » نام‬     ‫سیم = بکر اول بروزن‬                             ‫و رسد آنرا بجپت ا‪-‬هال خورند ‪ ۷‬و تارسیده‬
 ‫مابین سمر قرب و تاش‌کند وسمرقنه‬              ‫کوحی اس‬                                ‫آرا بجهت قبض و اماك ‪.‬‬
 ‫ین را‬           ‫مق‬                 ‫تزديك است‪E‬‏‬
                                                              ‫سیر = بکراول بروزن خباره کشکینه‬
  ‫در ورسحر وشمنده مدت‬          ‫حکیم‌ین عطا‪۶‬مگفتند‬              ‫راگویند » وآن انی باشد که از ارد جو وارد‬
 ‫کوه سیام کنده ود‬     ‫عقب‬        ‫که در‬    ‫ماه از اه ی‬   ‫دو‬
                                                                                            ‫بزند ‪. ۷‬‬       ‫ون‬
                                                                                                            ‫رز‬‫اقلا‬
                                                                                                                 ‫با‬
 ‫ماهی برمی‌آورد وآن ماه از پس آن کوء طلوع‬
 ‫میکرد تابلج فرسخ در پنج فرسخ لور آن ماه‬
                                                              ‫سیاسر = بکر اول وفتحسینبی‌قطه‬
                                                               ‫بروزن دلاور * قلم تراشيده لویسند گی‌را گوبند‪-‬‬
             ‫می‌تافت ؛ و بفتح اول گهفمته‌اند ‪.۱۷‬‬               ‫و بفتح اول و سین بیناطه » بمعنی سار است »‬
 ‫سیامك = پکراول وفتح میم‌وسکون‬                                                ‫وآن پرنده‌ای باشد معروف ‪. ۸‬‬

                                                                                     ‫(‪ )۱‬چك ‪ :‬بخا‪.‬‬
    ‫=وستا ‪tasirht.‬‏‬
                  ‫بارسی باستان ‪ *)2011(۲)0)-‬ا‬                      ‫‪ - ۱‬بازدد ‪ . 15‬از پهلوی ]‪5‬‬
   ‫»ردی ع [‪.5‬افتانی ‪158‬ل « اسشق ‪ »» ۰۰۷‬کیلکی‬
                                           ‫سانکرت ‪« ۲۵۱۲۲ -‬هوبشمان ‪ > ۰۹۷‬ک‬
   ‫*ازمصدر «سایدن ‪:€‬‬                 ‫‪.‬ف«سنا؟‪.‬‬
                                            ‫وسح‬
                                              ‫م‬              ‫ر‪ 5‬رك‪:‬ساه‪.‬‬        ‫وتهرالی ‪15‬؛سه‌بارده‪:‬ده بعلاو‪#‬بیست‪.‬‬
    ‫بدین کارمرخوبدتن‌را بياب ‪.‬فردوسی‌طوسی«جهانگیری»‪.‬‬                           ‫بدو کفت او‪:‬خو اقنران ساب‬
    ‫‏‪ ٩‬در کیلکی ی‪5‬ز(‪.۵‬‬                   ‫‪_٩‎‬ظ‪.‬مصحفاحات»و«حباب» ‪۳‬‬            ‫فر‌ساتین کلمه‌نامده ‪.‬‬
                                                                                                ‫لرفه‬
                                                                                                   ‫وی‌د‬
                                                                                                      ‫ول‬
              ‫کشت عاجز که بود بس اهار‬                               ‫‪ - ۷‬روستابی زمی‌جو کرد شیار‬
             ‫کرده‌ای‌چند وکاسه‌ای دو سیار ‪.‬‬                          ‫برد حالی زش زخانه بدوش‬
   ‫دققی طوسی‪ .‬لفت فرس‪۵۵۱‬؟ ‪.‬‬
               ‫وفهر ست ولف ‪:‬‬             ‫‪ ۵۳ ۹‬رك‪ :‬فرهنگه عبدالقادر ‪۳۳۱۷‬‬                    ‫ركه سار‬     ‫‪۸‬‬

               ‫ریختند ‪۰‬‬        ‫ون‬
                                ‫دیدران‬
                                     ‫سیالخ بم‬                       ‫چو با جیش هومان در بآخوتند‬
     ‫نظام >‬    ‫«فرهنگه‬     ‫‪.‬‬    ‫طوسی‬     ‫فردوسی‬



   ‫‪ -‬هاشم حکیم (طبری‌وابن‌الاثیر) با هاشم بن حکیم ( تاریخ بخارا چاپ شفرس ‪)41‬‬
                                                                     ‫‪.‬‬    ‫‪۳۳‬‬    ‫رك ‪ :‬مجمل‌التواریخ والقمص ص‬

        ‫وآن بشکار ‪.‬‬        ‫که ابنت غلام است‬                          ‫فلك‬   ‫له‌ماه‬   ‫سامی‬    ‫له ماه‬   ‫‪-۱‬‬


   ‫رود کی سمرقندی ‪« .‬لت‌فری ‪. ۹۳۳۲‬‬
  ‫( د هان فاطع ‪) ۵۵۱‬‬
```


## [2026-09-06T16:08:34.668Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /سیم/{print NR}' BQT_v2_pages.txt | tr '\\n' ' '; echo; echo \"=== search yoke sense ===\"; grep -n \"یوغ\\|جفت گاو\" BQT_v2_pages.txt | head -20",
 "description": "Find sim entries in BQT v2"
}
```


### [2026-09-06T16:08:36.582Z] TOOL RESULT

```
12 45 49 50 55 58 65 75 77 100 101 115 131 137 140 148 149 173 174 175 196 201 211 256 269 270 284 297 318 329 331 333 341 342 365 369 370 374 376 385 408 412 418 426 435 438 442 453 459 461 473 477 479 507 508 516 527 530 531 540 541 548 558 559 560 571 576 586 588 594 602 639 654 656 659 660 663 669 674 675 676 677 678 679 
=== search yoke sense ===
1939:                                                                                 ‫جفت گاو سکاو زر‬
32527: ‫را صب کنند وسردیگر آنرا بر یوغ بندلدوزمین‬                   ‫‪-‬نوابه از‬
```


## [2026-09-06T16:08:40.119Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /را صب کنند وسردیگر آنرا بر یوغ/{print \"leaf1=\"NR}' BQT_v2_pages.txt\nsed -n '32500,32560p' BQT_v2_pages.txt",
 "description": "Context of yoke mention in BQT v2"
}
```


### [2026-09-06T16:08:41.906Z] TOOL RESULT

```
leaf1=547
                     ‫نظ‬
          ‫(ه‪.‬م‪ ).‬لغة بمعنى سرسيك » مردخفیف وسبك ‪.‬‬              ‫ر)‬
                                                                ‫سار‬
                                                                  ‫(ك ‪+‬‬
                                                                     ‫‪ - ۱‬از ‪ :‬سب‬
                                                            ‫‪ - ۷‬سکار شادی‌لمادد تضت‬
  ‫فردوسی طوسی‪«.‬فرهنکه فظام» ‪.‬‬
     ‫زا‬                                                                                        ‫سبك صابه‬

                          ‫بدان زمین ودیوار کنند‪.‬‬             ‫اهبه از فرومایه و سفیه باشد چه سار‬
                                                                                              ‫هکتن ک‬
 ‫سبلان ‪ -‬بفتح اول و ثالی »بر وزن‬                           ‫یمصنی سر هم‌آمده است ‪ -‬و مجرد و بی‌تعلق را‬
 ‫و معنی سولان است وکآونهی باشد ترديك‬                                                           ‫‪.‬‬    ‫قتفانهد‬

                                           ‫باردییل ‪۳‬‬      ‫سبك سایه ه بنتحبایحطی ‪ .‬کنابه‬
‫سیت » بکر اول و لاموسکون ثالی‬                                             ‫لزکم بقاوبی‌ثبات و کنرنده باشد ‪.‬‬
 ‫وآن چیزیت‬         ‫ناده‬
                      ‫یر‬‫کسرویشم‬
                              ‫و تای قرشت ‪۰‬‬                   ‫سيك سر آن د کنابه از فرو مایگان‬
                                                             ‫و سفیپان و مفلان است ‪ -‬و اصحاب قلوب را‬
‫ايشان بکار برند ؛ و بااول و ثالی مکسور بلام‬
                          ‫‪2‬‬                                 ‫وان‬‫نون ک‬      ‫ن‬  ‫کهوهت‬‫بكسسنگ‬  ‫سب‬
 ‫اول وفتح لاء درعربی بمعنی بروت وسبیل باشد‬                 ‫قاری » مردم حبکار و بی‌ته و بیوقارو کم‬
                     ‫که موی پشت لب است ‪. ۴‬‬
                                                                                               ‫قیمت باشد‪.‬‬
 ‫چو ب قلبه‌باشد‪.‬‬   ‫سین = بروزن شکنج‬                          ‫سيك عنان ‪ -‬بکر مين بی قطه ‪.‬‬
 ‫و آن چربی است دراز که بربك سرآن کاوآهن‬                      ‫یمضی سبك رواست که کنابه از تند و نیز براه‬
 ‫را صب کنند وسردیگر آنرا بر یوغ بندلدوزمین‬                   ‫‪-‬نوابه از‬
                                                                     ‫رونده وجلد رفتار وشتاب روباشد ک‬
‫شیار کنند و بوخ چوبی است که بگرردن کاو‬                                                ‫هم صت‪.‬‬           ‫نهنده‬
                                                                                                           ‫حکمل‬
                                           ‫نید ‪# . ۵‬‬
                                                           ‫سبك لقا ‪ ۱‬۔ بکر لامو قاف بااف‬
 ‫سبو ‪ = ۵‬بفتح اول بروزن تنوره» حیز‬                           ‫کشیدہ » مردم سبك روحرا کویند عنی شخصی‬
                          ‫ومخنث ویشت پابی باشد‪.‬‬               ‫که مطیع وفرمالبردار گوشادمرو باشد وترش‌رو‬
‫سبوس ‪ » ۱‬بفتح اول و الكمجهول‬                                        ‫زود دوست دهد‪.‬‬    ‫لداوفاش‬ ‫ومقتوض لب‬
                                                                                           ‫ماش‬

 ‫‪ ۰‬لاله هرچیز رکاویند عموماء‬               ‫وی‬
                                            ‫جزن‬
                                              ‫بمر و‬          ‫سیل = بفتح اول و ثالی بروزن اجل ‪۰‬‬
‫ولخاله ویوست کندم وجو آرد کرده را خصوصا ؛‬                  ‫مرضی باد از امراض چشم‪.‬وآن موبی است که‬
                      ‫‪۰‬‬    ‫ات‬   ‫رضم اول هم آهده‬
                                                             ‫‪-‬ده‌ای رایز‬
                                                                       ‫‪۴‬پر‬
                                                                         ‫در درون پلك چشم برمیاً بد و‬
 ‫سبو سه » بفتح اول و واو مجپولبروزن‬                         ‫کویندکه درچشم بهم رسد وبعضیکویندباین‌معنی‬
‫دبوسه " خشکیی باشد مانند سبوی که بسیب‬                      ‫عربی است ‪ -‬و بهندی میلی باشد افزولاد که‬

                                                    ‫‪« :‬منتهی‌آلارب» ‪۰‬‬   ‫‪ - ۱‬لقاءِ (عر) دیدار کردن‬
             ‫سبل دردیده باشد خواب در سر ‪.‬‬
   ‫نظامی کذجوی‪ «.‬کذ جینه‪٤ »۳۸‬‏‬

   ‫‪ - ۴‬کوه سبلان » درمقرب کوه طالش است ‪ .‬مرتفع ترین قله‌آن ‪ 44۸4‬متر و همیشه‬
                                       ‫‪.‬‬      ‫‪۷0‬‬
                                               ‫‪-‬بیعی‬
                                                   ‫‪۸‬ی ط‬
                                                      ‫‪0‬رافا‬
                                                          ‫متور از برف‌است ‪.‬ر که‪ :‬کیهان » جغ‬
                                ‫‪ - ۳‬رك ‪ :‬سییل ‪ :‬رخ او (آبی = بد) چون رخ آن زاهد محرایی‬
   ‫بلت سقلابی ‪« .‬منوچپری دامقالی*‪٩۹۱‬‏ ‪.‬‬ ‫بررخش بر " اسثر‬
```


## [2026-09-06T16:09:11.528Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 668 669 670 671 672; do echo \"=== leaf1=$n (printed $((n-1+543))) ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | grep -n \"سیم\\|چوب قلبه\\|یوغ\" | head -8; done",
 "description": "Scan BQT v2 leaves for sim entry"
}
```


### [2026-09-06T16:09:13.429Z] TOOL RESULT

```
=== leaf1=668 (printed 1210) ===
=== leaf1=669 (printed 1211) ===
44:     ‫‪ - ۱‬رشیدی کوید ‪ :‬بم‌عنی سیمرغ زیرا که سی رنف دارد و ءولف سراج براواعتراض‬
46:                           ‫همان است که در ‪9‬سیمر غ > آمده (رك ‪ :‬سیمرغ) وجزو دوم ‪ ۶‬رنگ» است ‪.‬‬
=== leaf1=670 (printed 1212) ===
=== leaf1=671 (printed 1213) ===
=== leaf1=672 (printed 1214) ===
```


## [2026-09-06T16:09:17.306Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==669' BQT_v2_pages.txt | head -60",
 "description": "Print BQT v2 leaf 669"
}
```


### [2026-09-06T16:09:19.176Z] TOOL RESULT

```
‫ودرین روز گوشت وسیر برادر پیازخورندو گویند‬               ‫رگاعی ئىز هت که سوسته در آبرای استاده‬

‫که خوردن‌آن ايمن بودن ازمس جن است‌وجن‬                                   ‫حیض را‬        ‫روبد و خوردش‬
                              ‫کگرفته را آ‬
 ‫انز‌دهند‪ .‬یك است درین روزفرزند‬                                         ‫بگهاید وبول را برائد و آلرا‬
               ‫دادن وسثه وصنمت آموختن ‪۰‬‬         ‫شک‬

‫و کتابه‬          ‫‪۴‬‬   ‫معروفت‬     ‫=‬   ‫سیر شدن‬                                                      ‫خوانند ‪.‬‬
‫از‬     ‫كاھ‬      ‫‪2‬‬    ‫است‬    ‫از هر جر‬   ‫شدن‬     ‫از اد‬
                                                                        ‫سیراف‪ ۱‬د بافاوح رکت‬
                               ‫آرامگرفتن هم هت ‪.‬‬                              ‫‪۱‬‬
‫سیر ‪ = 6‬بطم ثالث ‪ .‬تسمه ودوالی باشد‬                                                 ‫کدنرار دربای‌فاری ‪.‬‬
‫آنکه‬         ‫باشند ‪,‬هت‬     ‫سقید که چشمه آنرا کنده‬                        ‫اه‬     ‫آهمدن د‬          ‫قد‬

‫نرم شود ‪ ۴‬و از آن بند مسر کندد و بندکارد‬                                   ‫سم‬                ‫تک‬
         ‫‪۱‬‬                 ‫ون‬                                            ‫از ملول شدن و بتنگه آمدن‬
      ‫وخنجر وشکار بند پرند گان شکاری نبزسازند‪.‬‬                                         ‫‪2‬‬           ‫‪3‬‬
‫مهمان ‪ ۰‬باقوت‬         ‫بر ورن‬    ‫سر مانه =‬
                                                             ‫سیر‬                    ‫وبی‌لیاز شدن باشد ‪.‬‬

‫سرخ را گویند ‪ -‬وحریر نازکه منقش وملون‬                    ‫سیر سور ‪ = ۴‬بساین بی لقطه بروژزن‬
                                       ‫را گنفیته‌اند ‪.‬‬    ‫فیل زور » نام روزچپاردهم است از هرماه‌شمسی‬
                                                          ‫و فارسیان درین روز عید کنند و جشن سازند‬

     ‫» شپری قدیم در ساحل خلیج فاری » بندرنجاری بسیار مهم ( درفر نهای‬               ‫‪12۳1-‬‬
                                                                                       ‫‪5 ۱‬‬
                            ‫‪ 4‬تا ‪ ۶۱‬میلادی ) ترديك بوشپر‪ .‬رك ‪ :‬دائرةالمعارف اسلام ‪٠‬‏ عمجم‌البادان ‪.‬‬
 ‫(وز چهاردهم )درد بماه‬
                     ‫سور (جشن) ‪ .‬بقول بیرونی کوش روز ر‬
                                                     ‫‪ - ۴‬از ‪ :‬سیر ( وم )‬
     ‫جشنی بوده است موسوم به ‪ ۵‬سیرسور»‪ .‬دراین روز سیر وشراب میخوردند و برای دفع‌ثرثیاطین‬
     ‫سبزبهای مخصوصی بگاوشت می‌پختند «آثار الباقیه ص ‪ ۶ ۹۲۲‬بشتهاا ص‪٩ 4۷۳‬‏ وبنابراین روز‬
     ‫‪E‬‏ اشباع شدن ‪ ۰‬حاامی که از خوردن غذا باندازة‬                      ‫ثست ‪.‬‬    ‫مراه شمسی‬
                                                                                        ‫چهاردهم ه‬

                                                                                      ‫کافی پدید آید ‪.‬‬
                ‫مانده زین کوهه را ميان دوراه‪.‬‬            ‫‪- ۴‬سرمیشتش( گورخر) از ادیمسياه‬
      ‫نظامی کنجوی ‪ « .‬هفت بیکر چاپ‌ارمغان‌ص‪.»۳۷‬‬
     ‫ذر نکرده‌اند و *بپرمان »‬
                            ‫بیروتی و ابن! کفانی در انواع ءاقوت چنین نامی را ک‬               ‫‪۵9‬‬
      ‫و«بهرمانی» را نوعی ازیاقوت بکاردده‌اند ‪ .‬رك‪ :‬فهرست‌الجماهر وفهرست نخب‌الذخائر‪-« .‬یرمان»‬
                                                                ‫‪ 2‬بهرمان » است ‪۱‬‬    ‫ممنی مصحف‬         ‫بهردو‬

     ‫‪ - ۱‬رشیدی کوید ‪ :‬بم‌عنی سیمرغ زیرا که سی رنف دارد و ءولف سراج براواعتراض‬
      ‫کرده وسی را «محضکثرت » دانته است » ولی ابن اشتفاق عامبانه است ‪ .‬جزو اول آن«سی»‬
                           ‫همان است که در ‪9‬سیمر غ > آمده (رك ‪ :‬سیمرغ) وجزو دوم ‪ ۶‬رنگ» است ‪.‬‬

                                                                    ‫`‬      ‫بقیه‌از صفتد‪۳۶۲۱‬‬
       ‫‪ -۶‬پهلوی ‪ ( 701815‬هزواریآن ‪« )7(2)۷015 . 0۳۵05‬بونکر ‪ » ۱۸‬ورك ‪ :‬توما =‬
      ‫کیاحی از نوع سوسنها و دارای چندین جنس مختلف است و بعضی از نهارابرای‌ا‪-‬تفاده‬       ‫‪0‬‬
     ‫ازییازبا برکک میکارند مانند سیرمعمولی ‪ 771۷145.۸‬که کلهای آن‌چتری است‌وسوخ آن‌فطمات‬
      ‫ککللاب ‪۱۸۲-۲۸‬‬    ‫جدا گنه برروی بك طبق قرار دارد و پیاز و موسیر هم از انواع آست «‬
```


## [2026-09-06T16:09:29.591Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"قلبه\" BQT_v2_pages.txt | head -20; echo \"=== v3 ===\"; grep -n \"قلبه\" incoming/BQT/BQT_v3_pages.txt | head -20; echo \"=== نقره sim ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=670 && NR<=684 {print \"--leaf1=\"NR\"--\"; print substr($0,1,600)}' BQT_v2_pages.txt | grep -n \"leaf1\\|سیم\" | head -30",
 "description": "Search for sim entry in Borhan"
}
```


### [2026-09-06T16:09:31.503Z] TOOL RESULT

```
1754:‫جفاله ‪ -‬بفتح اول بورزن حواله »‬                      ‫باشد که برکردن گاوقلبه کش و زراعت کننده‬
15170:‫وقلبه را نگیوزبند وآن چویی اس (‪ )۲‬که کاو‬                       ‫بیلقطة‬       ‫ودال‬   ‫ابجد مفتوح‌برا‬   ‫ودال‬   ‫تحتانیه حپول‬
28291:      ‫محلول تقلبها الملو کهولماً بها کماتقلب الآن اکر اللخالخ ‪٠‬‏ و كان اذا فیض علیها اسالالذهب‬
32525: ‫چو ب قلبه‌باشد‪.‬‬   ‫سین = بروزن شکنج‬                          ‫سيك عنان ‪ -‬بکر مين بی قطه ‪.‬‬
=== v3 ===
21828:- وهجوم وقلبه را یز ‎Mae‏ وبمعنی‌صدائی
23476:‎Cassia of arabia - 4‏ «اشتینگای» . ‎ *‏ (عر) قا قلبه ‎fyb‏ وقسوة
23966:قلبه - ‎gm‏ اول‌بروزن ‎le‏ چویی‌باشد
41281:‏گاو آ هن - آهنی ‎Sash‏ برسرقلبه
50490:که کرد نگاو قلبه وگردون گذارند ۱ .
=== نقره sim ===
1:--leaf1=670--
9:--leaf1=671--
15:--leaf1=672--
22:--leaf1=673--
27:--leaf1=674--
38:--leaf1=675--
41:       ‫مه‬                                                                                               ‫سیماب آتشین‬
42:‫سیما هنگ = با ها بروزن مینارنگه»‬                              ‫شبي|ن = بکس بای ابجد ‪.‬‬
47:--leaf1=676--
48: ‫سیم سوخته‬                                                                            ‫=‬
50:‫سیهرع آ آشین‪ -‬کنابهازخورشدجهان‬                 ‫سیمر غ ‪ - ۱‬بثانلك وسکون‌رایبی‬
53:                   ‫نسیم‬
58:--leaf1=677--
62:               ‫از آب صاف و شراب صافی باشد‪.‬‬        ‫سیم گاورس دار د کنا بهاز‬
67:--leaf1=678--
70:‫سینجر = بفتح اول وانی وسکون نون‬                                 ‫سیمین قواره ‪ -‬بنتح فای سمنص‬
76:--leaf1=679--
83:--leaf1=680--
91:--leaf1=681--
101:--leaf1=682--
103:--leaf1=683--
```


## [2026-09-06T16:09:54.765Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==674' BQT_v2_pages.txt | head -70",
 "description": "Print BQT v2 leaf 674"
}
```


### [2026-09-06T16:09:56.905Z] TOOL RESULT

```
                                                                                         ‫—‬   ‫=‪0۱ 4-‬‬
 ‫سای‬



‫ه را گویند ‪ ۱‬اسزبان و آحوان | هم حت درم دارکه آارا ماهی هشمی‌ممیگویند‬
                                                                    ‫رهمو‬
                                                                       ‫کل‬
                                                      ‫ووسفندان وکاوان و امثالآنا ‪ -‬وبز بان هندی‬
                                                                                              ‫گ‬
                                                     ‫بافنة ریسمالی باثد شبیه بمامل وبیشتر درولابت‬
                                           ‫سیم‬       ‫دکن شود وآنرا یله با شین نقطه دار یز‬
                                                                                             ‫کویند ‪.‬‬
                                                     ‫سیلی = بروزن فیلی‪ .‬آست که‌انگشتان‬

‫بناقشطینمدار © ‪ -‬و بسی گویند نراومدخانه‬              ‫دست را راست کنند و بهم بچسبانند وتبغ‌وار بر‬
‫ابیت که آن ماهی در آن رود خاله مبباشد ‪-‬‬              ‫گردن مجرمان گوناحکاران وبی ادءان زنشد؟ >‬
  ‫و بمهنی رمز وایما واثاره ‪ ۷‬هم آمده‌است ‪. ۷‬‬          ‫و اینکطیانجه سرصالیسگویند غاطاست ‪. ۴‬‬
‫یو»ه را‬
      ‫جتاب‬
         ‫سیماب *‏ بروزن پی‌‬                                                   ‫سیم ب‬
                                                     ‫=فتح اول و الی بورزن بقم »‬
‫گوبند ومعرب آن زیبق باشد و جزواعظم! کسیو‬              ‫چوبهایی است که برزسگران بر دوطرف چوبی‬
‫است‌بلکه روح |کسیروروح جمیع اجاداست ‪٩‬‏‬               ‫که بر گردن گاوزراعت گذارند بندند ‪ -‬وبکر‬
      ‫‪.‬‬   ‫و بمعنی خیره وبی‌حیا هم‌آمده است‬   ‫‪-‬‬       ‫اول بروزن جیم » نقره راکوبند ‪ - ۴‬ونام‌ماهیی‬

                           ‫‏‪ - ٩‬قس‪ :‬فیله‪ :‬بباغ اندرکنون مردم لبرد مجلس ازمجلس‬
           ‫براغ ادر کنون آهو برد سیله اسزیله ‪.‬‬

  ‫‪ ۴‬ولف «سیلی» رادرشاهنامهبممنی(ضربت با کف‌دستبازک)رفته (فهرستشاحنامةولف)‪:‬‬
             ‫بیلی و مشتش همی کوفتند‬             ‫همه کمتران زو برآشوفتند‬
               ‫از آن لیمةٌ روز تالبم شب‪.‬‬                ‫و نکشاد لب‬      ‫همه خوردسیلی‬

  ‫‪ - ۴‬درزیان کنولی بمعنی طیااحه استعمال‌شود‪.‬‬                 ‫«شاهنامة بخ ج ‪۹‬ص ‪۵۲۸۲٩‬‏ ‪.‬‬
 ‫‪ = ۴‬اوستا۔ ‪ , 2۳15‬قس_‪116is 4۲‬‏ (مشت*‪ )۰۰۲۱ ۱‬؛ هندی باستان ‪4¢ 4¥‬‬
 ‫(تیربوخ) » ارمنی ]"‪5‬ع‪( 101۵‬چوب بوغ کاودر) » پپلوی ‪( 0153‬هره) «اسشق ‪ ›4۷‬ورك ‪:‬‬
  ‫حوبشمان ‪ , 8۱۲۷‬درفارسی ‪ 4‬از اول‌کلمة (بهلوی)حذف شده «دهازله ‪ ۸۸۱‬اما«سمین؟ دریپلوی‬
   ‫آمد|رك‪ :‬سیم ] » اورامالی "‪( 1115‬رشتة شره) «‪ .۵‬اورامان ‪۹۲۱٩‬‏ برخی از مسفقان معاصراصل‬
  ‫و‪۰‬ص‪٠۹‬‏ ‪۱‬ببعد‪ .‬تقی‌زاده) وآنرا‬
                              ‫شمار ‪۱ ۹‬‬
                                     ‫و‪۲‬‬‫ص ‪۲‬‬           ‫ار‬
                                                      ‫شلم‪4‬‬
                                                         ‫«سیم» را بوئالی دانند (محلة داد کا ا‬
                                  ‫کمبر‌از‪ 2 :‬علامت نفی و ‪:( 2015‬شانه‌نهاده » عگلاذمت‬
  ‫اشته) (رك‪ :‬فرهنگه بونانی ‪-‬انگلیسی‬
  ‫لیدل واسکات) جمماً بمنی ( قر ) نامسکوله (از افادات شفاهی استاد بنونیست) ورك ‪ :‬ااجماهر‬
  ‫® = ‪ smarbA arb am‬ازماهیان استخواندار«دربای خزر‪.‬یریمالی‬                         ‫بیرولی ص ‪۲٤۲‬‏ ‪.‬‬
  ‫‪- ۷‬وایز رشته‌های باريك فلزی را «سی»‬         ‫‪ ۱‬رك ‪ :‬حیمیار ‪.‬‬                       ‫‪۸‬‏ ‪. ۲۵۱ ,‬‬
  ‫گوبند‪ .‬مفتول» واین‌معنی درزمان‌مولف معمول‌بوده ‪ .‬رك‪:‬سیم کش‪ .‬ورك‪ :‬ح‪ .۸‬سیم یک راول وم‬
  ‫‪- ۸‬از‪ :‬سیم‪ +‬آب؛ وسیم‌خودبمعنی جیوه مده ‪:‬‬                       ‫م‪.‬‬  ‫وه»‪.‬‬‫سی« س‬
                                                                             ‫‪:‬برا‬
                                                                                ‫كیبی‬
                                                                                   ‫ردارت‬
                                                                                       ‫دوم‌مشند» عد‬
       ‫يشت و رو باشد مکی آبینةبی‌سیم را‪.‬‬                     ‫سیم وزر دلیایرستان رامنافق میکند‬
  ‫‪۳‬‬   ‫‪١‬ص‏ ‪۲4‬‬      ‫«فرهنگك اظام» ورك ‪ :‬ما‬         ‫طاهروحید‪.‬‬


            ‫همجو سیماب برکف مفلوج‪. ‎‬‬                         ‫‪ - ٩‬شب بيدار ویندودید؛ من‬
  ‫یجافآ ‪ ,‬تفل« ‪‎‬یرف ‪. ۰۲۷‬‬
```


## [2026-09-06T16:10:30.708Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls | grep -i bqt; ls incoming/BQT/*.json 2>/dev/null; echo \"=== tops of leaves 660-678 ===\"\nfor n in $(seq 660 678); do printf \"%s: \" \"$n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | head -3 | tr -d '\\n' | cut -c1-90; echo; done",
 "description": "Inspect running heads of BQT v2 leaves"
}
```


### [2026-09-06T16:10:32.608Z] TOOL RESULT

```
BQT_alt_v1.txt
BQT_dli_part1.txt
BQT_v1_djvu.xml
BQT_v1_pages.txt
BQT_v1.txt
BQT_v2_pages.txt
BQT_v2.txt
incoming/BQT/BQT_v3_pagemap.json
=== tops of leaves 660-678 ===
660:   ‫صهراب‬                                                                        

661:  ‫‪-۱۱-‬‬                                                                       

662:                                                                                     ‫‪

663:      ‫اف‬‫سیا گیژ ‏ باکاف بروزن فراویز » امد‬       

664:   ‫سیا‬                                                                            

665:  ‫‪۱۲۰0 -‬‬                                                                    

666:                                                                                           

667:    ‫—‬       ‫شا‬                                                             

668:   ‫ی‬                                                                                

669: ‫ودرین روز گوشت وسیر برادر پیازخورندو گویند‬      

670:   ‫حسدان‬                                                                        

671:  ‫==‬                                                                                 

672:   ‫سی لحن‬                                                                       

673:   ‫سوه اس‬                                                                       

674:                                                                                          �

675:     ‫ه‬    ‫ا ‪۱۷‬‬       ‫مه‬                                      

676:  ‫سیم سوخته‬                                                                  

677:     ‫ه‬    ‫ا‪۲ ۷‬‬

678:  ‫سینه کردن‬
```


## [2026-09-06T16:10:39.298Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==665' BQT_v2_pages.txt | head -30",
 "description": "Print BQT v2 leaf 665"
}
```


### [2026-09-06T16:10:41.246Z] TOOL RESULT

```
 ‫‪۱۲۰0 -‬‬                                                                                               ‫سیاء‌بادام‬
‫سیاه دست ‪ = ۷‬ببایدا‌لنقطه بروزن‬                        ‫سیاه بادام ‪ ۱‬کنابه از چشم‌ممشوق‬
 ‫سیاه مست ک»نایه ازمردم بخیل ورذل و هسك‬        ‫است ‪.‬جه چشم را ببادام تشبیه کرده‌اند‪.‬‬
                                 ‫میاه پستان ؟ » زنی رگاویند که باشد ‪.‬‬
‫رزن‌سیاه‬
       ‫ه باسینبینقطهب و‬     ‫سیاه سگ‬                        ‫فرزند او لماند وهر طفلی را که شیردهد بمنرد‪.‬‬
 ‫رنف ه‪.‬ام موضعی است درجرجان وجشمه‌ایست‬                 ‫سیاه بوش ‌ ت با ‪,‬ای فارسی بروزن‬
 ‫درآن موضم که بهمن نام دارد ‪ .‬اکر ج‪.‬می‌از‬               ‫سیاه کوش ‪ ۰‬شب کرد وعسس ومیربازار ومیرشب‬
 ‫آن چشمه آب بردارند وبك شخص ازابشان‌پای‬                    ‫نآکی‬
                                                              ‫را گویند ‪ -‬وچاوش را بگیفزته‌اند » و‬
‫برکره‌ی که در همانجا میباشد بگذارد آب همه‬              ‫باشد که پیشاییش پادشاه دورباش گوید » و ابن‬
                           ‫آن مردم تلخ مشود ‪.‬‬
                                                        ‫جماعت در قدیم بجهت هیبت و صلایت وسیاست‬
‫سیاه کار ‪٩‬‏ د بکااف بالف کشیده‬                         ‫صاحب‬   ‫سياه می‌بوشیده‌اند ‪ -‬وماته‌ی وسو گوار و‬
  ‫جر‬
   ‫او‬‫فسق‬
       ‫و برای فرشت زده (‪ , )۱‬كاوه از فا‬                ‫تعزیت را نیز گویند ‪ -‬وشیربانان را بعنی‌جماعتی‬
 ‫کاری فاسقی‬     ‫ورسیاه‬
                     ‫سهکا‬
                        ‫دنا‬
                          ‫شک‬‫الو‬
                              ‫بحی‬
                                ‫وظالم وم‬               ‫که شبر و سر وجائوران درنده لگاه میدار لد هم‬

                                      ‫و ییحی ‪.‬‬                                                        ‫بش ‪.‬‬
 ‫بممنی‌سیاه دست‌است‬    ‫شیاه کاسه ‪٩‬‏‬                        ‫سیاه لبك = نوعی از بیدباشد‪. ۴‬‬
‫کهنانه از مردم خیل و ممك ورنلوبد بخت‬                   ‫سیاه جر ده ؟ د بمعنی میاه ریگه‬
                                            ‫باشد ‪.‬‬     ‫باشد چه چرده بمعنی رنکه و لون هم آعده‬
   ‫ف‬
   ‫تال‬
```


## [2026-09-06T16:11:00.267Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ qamis ===\"; grep -n -i \"qamīṣ\\|qamis\\|Qamis\\|kamision\\|camisia\" FVQ_pages.txt | head -20\necho \"=== KLN chemise/camisia ===\"; grep -n -i \"^chemise\\|^camisole\\|camisia\" KLN_1966.txt | head -20\necho \"=== SKT ===\"; grep -n -i \"^CHEMISE\\|camisia\" SKT.txt | head",
 "description": "Grep Jeffery, Klein, Skeat for camisia/qamis"
}
```


### [2026-09-06T16:11:00.360Z] TOOL RESULT

```
=== FVQ qamis ===
8776:^jA+~+& (Qamis).
12448:camisia 243
=== KLN chemise/camisia ===
6282:Late  L.  camisia.  See  chemise, camisole,  n.,  a  woman's  loose  jacket.  —  F.,  fr. OProveng.  camisola,  ‘mantle’,  dimin.  of  camisa, fr.  Late  L.  camisia.  See  chemise  and  cp.  prec. word.
7332:chemise,  n.,  woman’s  undergarment.  —  F., ‘shirt’, fr.  Late  L.  camisa,  camisia  (whence  also  It.  cami- cia,  Sp.  camisa,  OProveng.  camiza),  borrowed from  Teutonic  through  the  medium  of  Gaulish. Cp.  OHG.  hemidi  (MHG.  hemede,  hemde,  G. Hemd),  OFris.  hemethe,  OS.  hemithi,  OE.  he¬ mede,  ‘shirt’,  fr.  Teut.  *hamipia,  fr.  base  *ha- ma(n)-,  ‘covering,  cover",  fr.  I.-E.  base  *kem-, *kam-,  ‘to  cover’.  See  hame,  heaven,  shame, and  cp.  camise,  camisado,  camisole, chemisette,  n.,  a  kind  of  bodice  worn  by  women. —  F.,  lit.  ‘a  little  shirt’,  dimin.  of  chemise.  See chemise  and  -ette.
=== SKT ===
3355:Chemise.  (K.-L-C?)  ¥.  chemist, •-Laic  L.  ramiVt'a,  a^iirt,  ihin  dress.  I'rob. Celtic;  cf.  U.  Iii&h  taimma,  shiiU
```


## [2026-09-06T16:11:08.386Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8770,8815p' FVQ_pages.txt; echo \"=== leaf ===\"; awk 'BEGIN{RS=\"\\f\"} /\\(Qamis\\)/{print NR}' FVQ_pages.txt",
 "description": "Read Jeffery entry for qamis"
}
```


### [2026-09-06T16:11:10.133Z] TOOL RESULT

```
Syr. Uc&o, but it was from the Eth. &h9, as Noldeke, Neue
Beitrdge, 50, has shown, that the word came into Arabic. It was an
early borr&wing, for it is found both in the old poetry and in the
S. Arabian inscriptions (Rossini, Glossarium, 232, for 31$ as calamus
odoratus).
J
^jA+~+& (Qamis).
xii, 18-28, 93.
Shirt.
It is curious that the word occurs only in the Joseph story.
The authorities usually take it as an Arabic word, though as-
Suyuti, Muzhir, i, 135, quotes al-Asma'I to the effect that some held it
was of Persian origin.
It is clear that it cannot have an Arabic derivation, and the under-
lying word is doubtless the Ok*. Ka^icnov. This KOL/JLIO'IOV has been
taken as a borrowing from Semitic, but, as Boissacq, 403, shows in his
note on Acayu/za/oor, it is genuine Indo-European. The Gk. Kajjilcnov
passed into Syr. as lAcCL.Loao, 2 and into Eth. as flft, which is
used in Josippon, 343, for a tunic or shirt, and is in all probability
the source of the Arabic word. 3 It must have been an early borrowing
for we find it not infrequently in the old poetry.
**\\ -
jlklj (Qintdr).
iii, 12, 68 ; iv, 24.
Qintar a measure.
It was recognized by the philologers as of foreign origin, and though
some, like Slbawaih, held to an Arabic origin, Abu 'Ubaida (LA, vi,
is a good Tndo-European word, as is evident from the Skt.
Norse Jtalmr ; Slav, slama ; cf. Boissacq, 397.
2 See Fraenkel, Fremdw, 45.
3 Vollers, ZDMO, li, 311, thinks that the Arabic came from the Lat. camifiia,
but this is hardly likelv.244 FOREIGN VOCABULARY OF THE QUR AN
432) expressly states that the Arabs did not know the meaning of the
word. 1 Some said it was a Berber word (as-Suyuti, Itq, 323), others
that it was Syriac (as-Suddl in Mukkassas, xii, 266), but the majority
were in favour of its being Greek (ath-ThaSalibl, Fiqh, 318 ; as-
Suyuti, Muzhir, i, 134).
Undoubtedly it is the Gk. Ktvrrjvdpiov, which represents the Lat.
centenarium, and passed into Aram, as irD3p, Syr. JjLi^iO. 8
It was from the Aram., as Fraenkel, Vocab, 13 ; Fremdw, 203, shows,
that the word came into Arabic, and in all probability from the
shortened Syr. form Ji
(Qiyama).
Occurs some seventy times, cf. ii, 79.
Resurrection.
It occurs only in the expression <Ajill *^, which is a technical
=== leaf ===
261
```


## [2026-09-06T16:11:30.616Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LAT camisia ===\"; grep -n -i \"camisia\" LAT.txt LEW_1910.txt | head -10\necho \"=== AHD watkins kem ===\"; grep -n \"^kem-\\|^kem\\b\\|hemidi\\|camisia\" AHD_watkins1985.txt | head -10\necho \"=== LKT ===\"; grep -n -i \"qamis\\|kamis\\|camisia\\|chemise\" LKT.txt | head -10\necho \"=== PLA ===\"; grep -n -i \"qamis\\|qamīṣ\\|kamis\" incoming/PLA/PLA_pages.txt | head -10",
 "description": "Grep Latin dicts, Watkins, Lokotsch, Asbaghi"
}
```


### [2026-09-06T16:11:30.719Z] TOOL RESULT

```
=== LAT camisia ===
LAT.txt:8950:cama, -ae f.: atteste senienent dans Isid., Or.19,33,39, camisias
LAT.txt:9017:camisia, -ae (camlsa) f.: chemise. Rare et tardif. En dehors des
LAT.txt:9020:camisias uoeant, sic aptas membris et adstrictas corporibus... Panroman,
LAT.txt:62380:puellare lineum, quod et subucula, i.e. camisia, dicitur, P.F.407,16.
=== AHD watkins kem ===
=== LKT ===
2491:'Schilf,  Rohr' ;  hieraus  russ.  kamys  'Schilf- rohr', klruss.  komys,  poln.  komysz,  cech. kamys,  bulg.  katms,  kamis  'dass.',  serb.
2718:Od.  klmt,  kopt.  kemi  'schwarz'  war  die Bezeichnung  des  Landes  Ägypten  [dar- aus auch  der  Name  des  dritten  Nach- kommen Noas,  Harn  'der  Schwarze', hebr.  allerdings  in  'der  Heiße'  umge- deutet] ;  hieraus  entstand  ar.  ktmija' zunächst  zur  Bezeichnung  des  'Steins der  Weisen'  [also  im  Sinne  von  ikslr, s.  hier  Nr.  903,  gebraucht,  vgl.  GILDE- MEISTER in  ZDMG  XXX,  534/538], dann  'Scheidekunst,  Chemie'.  Aus  dem Ar.  kommt:  it.  alchimia  'Goldmacher- kunst' [fast  synonym  zu  inganno  'Be- trug'], alchimia  'ein  aus  Messing,  Kupfer und  Erz  zusammengesetztes  Metall', modern  chimica,  arte  chimica  'Chemie', frz.  alnhimie,  chimie,  sp.  pg.  alqtdmia; dtsch.  Alchimie  [für  Alchimisterei  heißt es  bei  Schuppius  zur  Verspottung  dieser Afterwissenschaft  ungemein  treffend : 'Allkühmisterei',  vgl.  Andresen  DVE  34], Chemie,  ndl.  alchimie,  engl,  alchemy,  al- chimij,  Vb.  to  alchemise,  chimistry.  — [Die  ar.  Lexikographen  leiten  ar.  kimija' vom  Vb.  kamä  'verbergen'  ab,  also  im Sinne  von  'verborgener  Kunst'.]  [POTT in  ZDMG  XXX,  6/20.  Mahn  EtUnt  81/85. Devic  DEt  7.    Kluge  10.
5645:Jcabanina  947 kacul(a)  1019 Ä;arf?/e  1125 fcarf/j«  984 kad%na  989 Ärarfö;-  987 Äraft-^;  993 kahwe  1005 fcatÄ;  1014 Ä;ais  1015 Ä;a;maA;  1009 A^o/ä/ä  1012 kalabadan  1275 kalabahk  645 Ä;nZf//'a<  1022 ykaZfli  1021 kalamfir  1085 kalaimz  1276 kahhrtna  1028 I  kaldznm  1028 !  1023 '  Ära/fa  798 kalgun  795 Ä;aZ/Ä-o  1031 !  fcff/i-an  1034 I  Ä-a/^rtfc  1039 j  kalpaiv  1027 I  Ä-a/?,p  1030 [  kamcik  1042 I  kamdzija  1042 I  kamfora  1100 j  kamila  653 kamis  1047 j  kamuha  1043 I  ÄrawBs  1047 !  fca/fai  1048 kansa  1056 I  kanza  1056 '  kapak  1061 kapan  1062 j  kapari  978 j  kaplan  1066 I  fear  1069 t  fcaro  1070
5902:alchemise  1157
9470:kamis  1U4<
=== PLA ===
```


## [2026-09-06T16:11:31.549Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON قمیص ===\"; grep -n \"قمیص\" MON_part1.txt MON_part2.txt | head -10\necho \"=== MON شمیز ===\"; grep -n \"شمیز\" MON_part1.txt MON_part2.txt | head -10",
 "description": "Grep Moin for qamis and shomiz"
}
```


### [2026-09-06T16:11:31.637Z] TOOL RESULT

```
=== MON قمیص ===
MON_part1.txt:76409:سربال: 6021 [ع.] (.) ببراهن؛ قمیص. 
MON_part1.txt:87417:شوی: 32۷-1 [- شبی] (.) بیراهن» قمیص. 
=== MON شمیز ===
MON_part2.txt:67890:ر یو نجو » رونجوء رشمیز. زنگاری که آهن 
MON_part1.txt:33430:گذارنده (فر ه.) شمیز. 
MON_part1.txt:40931:چشمیز کث» سباه دانه. 
MON_part1.txt:50691:چشمیزک: »0-2 [- چشمیزح « 
MON_part1.txt:50692:تشمیزج] (.مصف.) دانه‌ای است سیاه به 
MON_part1.txt:87391:شومیز: 0032 (- شومز - شمیزا () زمین 
MON_part1.txt:87392:شیار کرده و آماده برای زراعت» شمیز.
```


## [2026-09-06T16:11:37.578Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '33420,33440p' MON_part1.txt; echo \"=== 87385-87400 ===\"; sed -n '87385,87400p' MON_part1.txt",
 "description": "Read Moin contexts"
}
```


### [2026-09-06T16:11:37.668Z] TOOL RESULT

```
ان. 

پوشک: 2۳26 (.) گر به. 

پسوشنه: (0-)3-272ت۲ (امر.) سربوش که 
روی چیزی بگذارند؛ هر چیز که بدان روی 
چیزی را بپوشانند. هر چیز پوشیدنی. 
پوشه: (0-)-*00 (.) مطلق پرده که بر روی 
میزها پوشند و از درها آویزند. لفافه‌ای که 
نو شته‌های راجع به یکت موضوع را در آن 
گذارنده (فر ه.) شمیز. 

پوشیدن: ۳11-0 [- پوشدن] (مص م.) 
(پوشید» پوشد» خواهد پوشید بپوش 
پوشنده» پوشیده؛ پوشش» پوشاکک) در بر 
کردن» ملبس شدن برتن کردن. جامه بر تن 
کسی کردن؛ ملبس کردن» پوشانیدن. مستور 
کردن» پوشانیدن فرا گرفتن. نهفتن» مخفی 
کردن. بر سر نهادن» کلاه پوشیدن. طلاق 
گفتن زن را. تحت‌الشعاع آوردن. بستن (در 
و مانند آن را). پوشیدن چشم: برهم نهادن 
=== 87385-87400 ===


چاهخو و دشتبان هنگام برداشت و پیش از 
کوییدن غله بردارند و آن عبارت از ۰-۵ من 
تبر یز غله است. 

شومیز: 0032 (- شومز - شمیزا () زمین 
شیار کرده و آماده برای زراعت» شمیز. 
شیار. 

شونده: (0-)«۵جد-۷ه؟ (افا.) انجام گر دنده. 
هستی باننده. رونده) مقّ. اینده. 

شو هر : 2۲-(327)0۳ (.) مردی که با زنی 
زناشویی کرده؛ مرد زن‌دار» شو» شوی» 
روج. به شوهر دادن: دختر يا زنی را به عقد
```


## [2026-09-06T16:11:52.579Z] TOOL CALL #43: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-06T16:11:52.586Z] TOOL RESULT

```


```


## [2026-09-06T16:11:55.850Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/camisia",
 "prompt": "Give the Latin etymology of camisia verbatim: what is it borrowed from (Gaulish/Germanic?), when first attested, and what descendants are listed. Also any note about Ancient/Byzantine Greek καμίσιον."
}
```


## [2026-09-06T16:11:58.088Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D9%85%D9%8A%D8%B5",
 "prompt": "Give the Arabic قميص (qamīṣ) etymology verbatim — is it from Latin camisia, Greek καμίσιον, Aramaic, or Ethiopic? List derived terms/descendants including Persian and English kameez."
}
```


### [2026-09-06T16:12:02.277Z] TOOL RESULT

```
# Latin Etymology of *camisia*

**Source language:** Borrowed from Proto-West Germanic *[\*hamiþi](/wiki/Reconstruction:Proto-West_Germanic/hami%C3%BEi "Reconstruction:Proto-West Germanic/hamiþi")* ("shirt"), ultimately from Proto-Indo-European *[\*ḱem-](/w/index.php?title=Reconstruction:Proto-Indo-European/%E1%B8%B1em-&action=edit&redlink=1 "Reconstruction:Proto-Indo-European/ḱem- (page does not exist)")* ("cover, clothes").

**First attestation:** "First attested in the writings of Jerome."

**Descendants:** The entry lists an extensive range of Romance language descendants (Romanian, Italian, French, Spanish, Portuguese, Catalan, Sardinian, etc.), plus borrowings into Albanian, Arabic, Coptic, Old Czech, Proto-West Germanic, Byzantine Greek, and Old Irish.

**Byzantine Greek note:** The entry shows a back-borrowing or related form: "Byzantine Greek: [καμίσιον](/wiki/%CE%BA%CE%B1%CE%BC%CE%AF%CF%83%CE%B9%CE%BF%CE%BD#Ancient_Greek "καμίσιον") (kamísion)" listed among descendants, suggesting Greek adopted the term from Latin *camisia*.
```


### [2026-09-06T16:12:05.118Z] TOOL RESULT

```
# Etymology of Arabic قميص (qamīṣ)

## Origin
According to the Wiktionary entry, the word is "probably from Latin *camisia*, from Proto-Germanic *\*hamiþiją*."

The entry notes a minority scholarly position: some researchers argue the Latin term was borrowed from Semitic languages, citing a Ugaritic form /qms/ meaning "garment," though this word doesn't appear in other ancient Semitic languages.

## Derived Terms and Descendants

**Arabic-derived terms:**
- تَقَمَّصَ (taqammaṣa)
- قَمَّصَ (qammaṣa)
- قَمِيص نَوْم (qamīṣ nawm, "sleepshirt")

**Major descendants include:**
- **Persian:** قَمِیص (qamīs)
- **Hindi:** क़मीज़ (qamīz)
- **Urdu:** قَمِیض/قَمِیص (qamīz/qamīs)
- **English:** kamees
- **Indonesian/Malay:** gamis
- **Bengali, Assamese, Marathi, Nepali, Punjabi:** Various forms derived through Hindi/Urdu

The word traveled across multiple language families via Persian as an intermediary.
```


## [2026-09-06T16:12:13.495Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/chemise",
 "prompt": "Give the English etymology of chemise verbatim (Old French, Late Latin camisia, Germanic). Also list French chemise senses including 'folder/dossier cover' if present."
}
```


## [2026-09-06T16:12:14.090Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/kameez",
 "prompt": "Give the English etymology of kameez verbatim: from which language (Urdu/Hindi, Persian, Arabic, Portuguese?) and the chain back to Latin camisia."
}
```


### [2026-09-06T16:12:18.705Z] TOOL RESULT

```
# English Etymology of Chemise

From French *chemise*, from Old French *chemise*, from Late Latin *camisa*, *camisia* ("shirt, undergarment, nightgown"), from Proto-West Germanic *\*hamiþi* ("shirt").

# French Senses of Chemise

According to the Wiktionary entry, French *chemise* has these meanings:

1. **Shirt** - specifically one that opens at the front
2. **Folder** - office supplies item (a dossier cover)
3. **Chemise** - a wall-enforcing earthwork (architectural/military term)

The entry notes that *chemise* refers only to front-opening shirts, distinguishing it from a *chandail* (pulled-over-head shirt).
```


### [2026-09-06T16:12:19.198Z] TOOL RESULT

```
I cannot provide the English etymology of "kameez" based on the webpage content you've shared. The Wiktionary page only states that "kameez" is an "Alternative spelling of _kamees_" but does not include etymological information tracing the word back through Urdu/Hindi, Persian, Arabic, or to Latin "camisia."

To find this etymological chain, you would need to consult the entry for "kamees" on Wiktionary or refer to a more detailed etymological dictionary.
```


## [2026-09-06T16:12:22.128Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/kamees",
 "prompt": "Give the English etymology of kamees/kameez verbatim: source language(s) and chain."
}
```


## [2026-09-06T16:12:22.985Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/calvus",
 "prompt": "Give the Latin etymology of calvus verbatim: the Proto-Italic and PIE reconstruction, cognates (Sanskrit, Avestan, Persian), and derived terms calva/calvaria."
}
```


### [2026-09-06T16:12:27.120Z] TOOL RESULT

```
# English Etymology of Kamees/Kameez

According to the Wiktionary entry, the word is: "Borrowed from Arabic قَمِيص (qamīṣ). Doublet of chemise."

The etymological chain shown traces back through multiple language stages:

**Source language:** Arabic (قَمِيص - qamīṣ)

**Earlier related forms in the etymology tree:**
- Latin *camisia* (shirt) — possibly borrowed into Arabic
- Proto-West Germanic *hamiþi* (shirt) — which may have influenced Latin *camisia*
- Proto-Germanic *hamô* and ultimately Proto-Indo-European roots

The primary direct source for English *kamees/kameez* is **Arabic**, with the word functioning as a doublet of the English word "chemise," indicating they share a common ancestral origin despite entering English through different pathways.
```


### [2026-09-06T16:12:30.942Z] TOOL RESULT

```
# Latin Etymology of *calvus*

**Proto-Italic Origin:**
The word derives from Proto-Italic *[\*kal(V)wos](/wiki/Reconstruction:Proto-Italic/kal\(V\)wos "Reconstruction:Proto-Italic/kal(V)wos")*, inherited through Proto-Indo-European lineage.

**Cognates:**
Sanskrit *[कुल्व](/wiki/%E0%A4%95%E0%A5%81%E0%A4%B2%E0%A5%8D%E0%A4%B5#Sanskrit "कुल्व")* (kulvá, "bald") shares etymological connection with the Latin term.

**Related Formations:**
The entry documents several derivative words:
- *calva* (feminine form)
- *calvaria* (skull/cranium-related term)

These descendants illustrate how the root meaning of "hairless" or "bald" expanded into anatomical terminology across Romance languages and English cognates like *calvous*.

The documentation traces this family through multiple declension patterns and shows productive word-formation extending from the basic adjective through specialized medical and anatomical vocabulary.
```


## [2026-09-06T16:12:37.375Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT kaurva ===\"; grep -n \"kaurva\\|kaurvo\\|kahl\" BRT.txt | head -20\necho \"=== BRT sima ===\"; grep -n \"sīmā\\|simaē\\|simōi\\|Halsring\" BRT.txt | head -20",
 "description": "Grep Bartholomae for kaurva and sima"
}
```


### [2026-09-06T16:12:37.442Z] TOOL RESULT

```
=== BRT kaurva ===
4081:•  j.  afsman-  n.  'Verazeae  (der  Gä^rJs)'": tiSranqm  kaurvafaoiryanam  . .  haitilca "manaca  (AP.)  '^  vacas^a  vacastastlmla  (sd.) Vr. /J.3; — vfsp?m^a  'man^m{Pi&y  yasa- maide  Y.  Ji.^;  —  aitatca  vacö  .  .  %ri.- afsm»m  (sd.)  . .  kais  Al  'man  (NP.)  ". .  wel- ches sind  seine  (des  AAunaVairya)  Vcrs- zeilen?"  Y,  19.16.
4776:kaurvatüt-,  xlaisröi  hU  haurvüta  'ntäla
4777:ahmst  sISi  dqn  (sd.)  trvjh  utayüitl  Y.  4I5. 10;  57.7,  44.18,  47.1;  —  0,a  haurvaia "rstäta  ySi  slö  /nlzd»n  asaonqm  parSMsti jasmtqm  Yt.  1.25;  —  mazS  (sd.)  avaKyai .  .  daidl  Aaurväd  Titätä  (GD.)  V.  5Ä 7.  a)  als  Bezeichnung  fiir  die  Speise der  Seligen*;'*  at  löi  ubl  haurvassa 3^ar?%äi  3  'r^atasca  (NS.)**  "und  deine beiden  werden  zur  Nahrung  dienen,  der Wohlfahrtstrank  und  die  Unsterbltchkeits- speise"  Y.,?4.  n.  A)  als  Gottheit  {Amasa Spmtd),  der  die  Sorge  für  die  nützUchen Pflanzen  anvertraut  ist  (SüErL:  vanas- patipatiliySi  aya  damaya  fraonnta  akurd .  .  vohu  manu  .  .  a£>m  . .  xsa%rpm  .  . ärmaitil  frä  kaurvatas  fra  'r>tatils  Y.57. 24;  —  vanät  haurvasca  °rstas^a  (NS.)" •wa  sUMtttca  farsmmla  Yt  ig.  96 ;  96 ;  — armaitfm  ..  haurvaiat^m  ..  'rsiatatsm  yaza- maide  Y.16.%;  JI.12,  S,  2.6f.;  —  mazdii dadat  akurö  haurvatö  'riiatascä  .-.  sarS Y. 31.21;  —  data  vj  'rjtSscä (NS.  als VS.)i> utaySitT {%A.)  kaurvatas  draonsY.33.9,;  — iaurvatas^a  'r)tatasca\t.4.i(f)  a)bes. i  in  Dualverbindung  mit  Aaurvatät-:  aya I  damaya  fraornnta  ahurd  masdä  .  .  fra ,  sp^nta  *armaitis/ra  haurvaia  °rHäta  (ND.) Yt.  JO.92;  —  sarBi  bszdyai  (&d.)  haurräiä I  "niaia  (ND.) . .  j?.  .  Y.44.17;  —  upa.- ßm^ti  (sd.)  haurvatä  °r>talä  (AD.)  Y.  45, .  5;  —  sp)ntayai  ärmatSe  haurvalbya  -ntat- '  bya  Yt.  7. 2 ;  H.  i.  7 ;  —  yS  spsntaya  arma- töis  yä  haurvatä  'ntata  (GD.)  Y.  70. 3 ; .  —  kaurvatasca  nö  'ritats,'''^ gTusca  tasiiö.. I  Vr.  g.  5,  a)  amir>tät5  (näml.  ayar?) heisst  der  7.  Monatstag:  S.  7.7;  vgl, 2. 7, ,  V.  7tt.3,  A  1)  als  Bezeichnung  für  die
7639:fk^ä-  Adj.  'kahl'.  —  ')  Übersetiung  von  xivr.iii.- 1
9307:*drußtn  \. 32.12;  —  nSit  urvä%ä  datsi-\     KompE.  —  PFP.  zum  V.  ^kar-.    —    ai  vgl fyas/tl  -fanB  vastrSt  arSm  (sd)  Y.5/.14;       *"':'■''■■  ^-T'-^""  ')  ^"^J-  ''  "■  "  ^""^  ^•"'■ —  ya  ..  'panjs  uropaynntl  yüca  . .  duh.- 1  •  j-  kaurva-  Adj.  'kahl,  unbehaart':  aspahe xiiihm    dahyunam    '^.4^.10;    —    »/a«^  U^-*^«  J^maA*  'j'a^^  YtÄ  21;  31'. iavayasc'-a  Y.^iT.'ii.  .)  im  jAw.  Name|     KompA.  "  -j- ^^;^-  Adj.  -zu  k.U,   »p.
9309:ä»  MazdayameT*h    vis/an^m  tbihatam   '  \  l^urvo^aosa-  Adj.  ^«'1  kahlen,  tin-
9310:pairikanamca   'sihram    kkoyam    '>^«fÜ '■*«""""*'  °^''*'' ^t-*  =»■ Y.p.  i8;'Yl  jj.  135;    —    'pänS   X\..'4.i,\*  J-   kaurvö.duma-   Adj.    'mit   kahlem, FrW.  3.  3.  'Unbehaartem  Schwanz':   aspahe  kihrpa  .  .
9311:•)  Vgl.  unter  usig-,   bes.  BB,  A  127;    femer  kaurvahe  °mahe  Yt.Ä  21,
9312:W£STSBE.jEr.iii,  .#7  19.  Späterhin  mildem'  j  tji„rvö.bar»sa-  Adj.  'mit  kahlem, TÖllicen  Sieg  der  soraaHJiHschen  Religion,  ist.  .  ,  ^  ti  1  n-.  i  i  ^  i  i  i  • die  eigentliche  Bedeutung  von  .(■«,-«/««- tls  Rabbi ,  unbehaartem  Hals,  Rucken  :  aspahe  kihrpa
9313:der  fl'aa/ischen  (vorsaraSai/^schen)  Religion  ver- j .  .  kaurvahe  °Sahe  Yt.ö.  21.
11042:—  im  jAw,  nur  beim  Zahlwort:  pancä/'a haptäitim  h.  3.  q,  12  (s,  dagegen  7 ;  Sp, 569  o.).  2)  die  Glieder  sind  verbal;  mit Tmesis:  m!ncä  T  [inaz\dazdäm  fsd.)  vafdd- dam  . .  Y.59.  5.  3)  bei  beiden;  b)  im Awf.;  i)  die  Glieder  sind  nominal;  a)  sie folgen  sich  unmittelbar:  uhi  kaurvascü amsritathscä  '^■34-  n;  32.  15;  —  van,ll haurvasca  ain»ntih'a  uva  SiPum^a  tar'- n^mca  Yt  /p- 96; —  *a:'a(ND.)  .  .  vyqsca vyänasca  Yty.  35;  —  twaSm  i^arfiimca vattnmca  Y.  55.  z ;  —  yais  ap3r»saH?m mazdiscä  zara^ultrascä  Y.  /2.  5 ;  —  at hv5  . .  Tsäcä    ataitilcä  Y.4^-5i  V.5. 53;
12592:•  j,  daj'a-  Adj.  —  ?— ,  Bezeichnung  einer, schlechten  Eigenschaft  des  Pferds":  atpahe , k^hrpa  sämaht  kaurvahe  .  .  'yahe  aiwi- IstöJarsiöis  Yt  <¥.  a  i .
25004:'huItraAe  .  ■  yim  istn  aniisa  sppnta  . .  ahüm  'huiirai  Vr.  12.  i;  —  Zw«  'tum  yatamaide 'tBmca  gai^anam  Yty.92;  91,  Vr.  2.  4, '_>-/«  sarahuHrstn  Y.  70. 1 ;  —  amtrptstö 16.  3;  —  ya%ä  aha  (Sp.  a8a  o.)  vairyö  '^wS  S.  /.  7  '"';  —  kaurvatats  "5aiff  S.  /. (näml. »araättÄrff)  ai-S  °(uP^  a/ätc'it  Äa^'a'6'°>; —  ä%rS  ahurahe  matdä  '%wS  b^rp- ..  dazdä{5Ü.)  Y.  27.  13;  —  yat  dim  (näml.  j  «n/J  yS  asahe  Y.  22.  4;  1.  17,  4.  2;  — tarahuttrfm)  aküm{Si^.  282  o^ca  Hümca  .'hwasca  bfrgzats"^  H.4S;  Vr.^.6;  — adadaj  Y.  iff.  12;  —  zara%ustrS  .  .  'iu/\  avi  iava  'tvS  (VS.)  bima"^ yasmm  g?r?Q- astvaihyB  gal%ayä  bansnul  bipaÜista-^maAi  \x.21.3;  —  kaya  °tavöt  nmänyS naya  Yt.  ig,  41;  —  s.  noch  Yt  8.  ^^' vTy^ö  santumS  dähyumö  tarähustrS  puxtiJ unter  7.  ß)    AHM.  tÜT    die   gtsammle   äfjAam  daÄyurtamyä  anyä  ra/sit..ühru.-
29307:Ableit.   aas   haokaurvak:    —    ■)    Hds.  aakri
29648:A'  und  »'  ('gani-  . .  halb-')  sind  poss.Korop. mit  dem  nämlich«D  Schlassglied,  detsen  rich- tige Lesung  und  Bedeutung  nicht  la  ermitteln ist.     T  kaurvö.f<isä.  —  Pü.:  fehlt, j.,  g.  kaiirvis^i  s.  kaurvaläl: j.  kautvi  P.  33:  lies  kaurvi,  Sp.   179I   O.
=== BRT sima ===
26340:'Halsring',  d.  i.  ein  vom  Joch  ausgehendes, den  Hals  des  Pferdes  umfassendes  Rmid- holz:  aat  tl  (näml.  aurvantlf)  vTspa  frä.- yuxta  *Aqni.ivam{sA)ca  °mqmia  simSi- "^rqmca  YLJO.  laf.
29969:•  j.  ^ham.ivä-  f.  Name  eines  Teils  vom  Ge- schirr des  mit  Pferden  bespannten  Wagens, vli  'Deichsel':  äal  ti  (näml.  aurvants)  vXspa /rü.yuxta  'vqmca  simqmca  simöihrqmca dirita  huhr^la  ^upairi.späta  aka  bastom "und  die  (Renner)  sind  alle  angeschirrt an  die  Deichsel  und  den  Halsring  und das  Joch,  die  mit  dem  aufgespaltenen wohlgefertigten  üb  ergesteckten  Zapfen  zu- sammengehalten sind"  Yt.  jo.  ia5(?).
```


## [2026-09-06T16:12:38.167Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD krw ===\"; grep -n \"krw\" SOD_pages.txt | head -30",
 "description": "Grep Gharib Sogdian dictionary for krw"
}
```


### [2026-09-06T16:12:38.216Z] TOOL RESULT

```
=== SOD krw ===
5621:646 >5krw S
7928:1442 >rSyf-       M =» Wyp-                                    1454 Vkrwn'y      B                     >'<J><J^^X
7929:                                                                     ark(k)arune    Orkrwny)
7934:        Khwar. V<5V ©3sg. prcs. yrdywt                         1455 'rkrwny => >rkrwn}y
8780:       TSP 8.189-, >sk}np\ TSP 2.1150; Wnpvv, VJ n p91,             1751 >skrwp B                   (J>jJlt.)j^\^iKjF^
13877:                                                                      6andak      (6n5yt) ©f.n.; pi. dnfyt    =»krw
17418:                                                                  karunc =>krwn
17569:             BBB b40; W-Lii 547.26, 548.19; GMS I070n 1,              4875 krw*     B       <hJ* vS   tJ^^t^'J^W^
17575:             good looking                                             4876 krwpr'n M                                    jlijA*
17581:       4865 krsny     B, S                              ^_U j < j£i   4877 krw 8nt>k(h) B             ^jj^tJ* u'^ ^"OW4 0'^
17589:               370; MSP b31, 101; STii 5.11; STSC 133, 142-3          4878 krw kpy      M     ? JL+ <? ^U ^J .(^U ^y) )/
17603: 4879 krwn M                           fb*l <fU3l <J\ « J^p
17608:          269, 347; >rkrwriy: >rk-krwriy, STii; Gersh.               karz (qrz, krz) *=»kj, krj, qz
17611:4880 qrwn      M, C =* krwn                                          VJ; TSP 2.55, 21 iil2; BSTBL, Dhy. 315; Frag.
32791:          10, 27; W-Lii 572n3; wkrw, BBB 533; KG                                 wimyte ?                             (tZAiJ)* 41
37147:11483 zwkrwfi'k   B                      ^.^ c[f l0 p ^u                   zwart ©<*uz-warta ^zw'rst-, zywst-, zwto-.
```


## [2026-09-06T16:12:54.429Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '17565,17600p' SOD_pages.txt\necho \"=== leaf ===\"; awk 'BEGIN{RS=\"\\f\"} /4875 krw/{print NR}' SOD_pages.txt\necho \"=== pdf tag ===\"; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<17600' | tail -2",
 "description": "Read Gharib entries for krw"
}
```


### [2026-09-06T16:12:56.583Z] TOOL RESULT

```
       4860 krsn'wty' M                                        ^l j        Sund. Man. Lett. 305.5, 301 n 14, 312.5
            karsnautiya(k) (krsn'wty^h)
            beauty                                                    4874 krts'r   S =* kwrts'r

             BBB b40; W-Lii 547.26, 548.19; GMS I070n 1,              4875 krw*     B       <hJ* vS   tJ^^t^'J^W^
               1079; KG 377, -jfc/i
                                                                           karwa
       4861 krsn'wty'kh       S =» krsn'wty*                               gap
       4862 qrsn'w wyn'mndyh M                   ^r'^vy-                   BSTBL, Dhy. 66; Hen. L W 96
            karsnau wenamande
             good looking                                             4876 krwpr'n M                                    jlijA*
             GMS 1100                                                      karu Paran

       4863 krsnw =# krsn*w                                                heavy-loaded
                                                                           Sund. MSP bl37, 139n p46
       4864 qrsny     C => krsny, krsn'k
       4865 krsny     B, S                              ^_U j < j£i   4877 krw 8nt>k(h) B             ^jj^tJ* u'^ ^"OW4 0'^
                                                                           karw-5ande, Sandak
             karsne    (qrsny)   ©pi. -r =^*wkrsnyy, krsn'k,
               krsn
             form, beauty                                                  gap-toothed
                                                                           SCE  83; Sogdica. 23.19; Gersh. Sogd. Cpds. 144.1;
                                                                             Hen. L W 96
             TSP 7.163; BSTBL, Dhy. 176; Sund. KG pl84,
               370; MSP b31, 101; STii 5.11; STSC 133, 142-3          4878 krw kpy      M     ? JL+ <? ^U ^J .(^U ^y) )/
                                                                           kar(w)-kapi ©<Av. kara; <IE *skvalos, whale-,
       4866 krsny'n B                           &*^y «^' jaU. ^ A            Finish. kala; Hung, kat
            karsnyan ©pr. name
            son of Sudashan                                                Kar fish(a kind of fish), cat-fish ?, whale ?
             V J 281 & etc.                                                Bailey. AM 1965, 113; Hen. Tales. 483.3




i
 195
=== leaf ===
260
=== pdf tag ===
```


## [2026-09-06T16:13:17.606Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HENNING gap-toothed ===\"; grep -n \"gap-toothed\\|krw-\\|karw\" HENNING_selected_papers.txt | head -10\necho \"=== DKS kaurva/kalva ===\"; grep -n \"kaurva\\|kalva\\|kulva\" ISS_alt_DKS.txt | head -20\necho \"=== HUB kal ===\"; grep -n -i \"kahl\" HUB.txt | head -20",
 "description": "Grep Henning, Bailey, Hübschmann"
}
```


### [2026-09-06T16:13:17.678Z] TOOL RESULT

```
=== HENNING gap-toothed ===
1130:dast erkaé (which need not be changed into das [pat] érkat), see Bailey, BSOS., vii, p. 73. Sogd. (16) ‘with crossed arms, ef. SCE., 400, and prBrtp'8 “ cross-legged", Dhydna, 18. The verb, prByr- (pari biraya-), occurs in Dhuta Bstw pryByr " he crossed his arms (prBrtytKara-Balgasun, p. 22, frag. xi, 4, is not clear).—{17)(18) “ Whip. Sogd. auiép from zivagpa-, of. Av. zhaZwayat.altra, and NPers. 2b “whip, whipeord” (Rind. ; Asadi, p. 8; Div. Nasiri Khosrou, 429), Wakhi rafip “ whip" (Morgenstierne, IJFL., i, p. 588). Closely related is Buddh. "yrel'yp- “ squint-eyed", see BBB., p. 63. MPers. asp-azan " horse-whip”, of. Arm. garazan, zarazan. MPers. ‘spiwon (den from 4yavana-?) occurs in an unpublished MPers. 'pswn 'y tb “spell against the fever” (M 781), where féyr “sword”, eyl’n (see below, on g 1, 2), and "sph "whip" follow each other—(19) “teeth”. Sogd. zwrn- = “* blood” (but a separate word *zwrn- “food”, or “banquet ”, is, of course, possible), pinork = Buddh, pyerk- SCE., 28 (said to mean “ dark-coloured), or from plyer- “to lacerate, devour” (R.. i ¢ BBB., p. 91), cf. 'ply'r, Vay 313, 949, Therefore, Sogd. =“ bloodstained teeth” or “blood: Jacerating teeth" (? “‘laniaries?"). MPers. "ned could be avid “rubbed, blunted ” (ergo “‘ molar teeth?”), or dsd8, 1, “useless,” 2, “ not rubbed " (NPers. side) = “ sharp teeth !"" Speaking of teeth, I should like to add to my recent remarks on Sogd. krw-Bnt'k “ having defective teeth", BSOS,, x, p. 96: the word knw- still exists in modern Birjandi Persian, as Eabrd, Eawerd “ toothless”, see Ivanow, JPASB., xxix, 4, p. 340. This makes it unlikely that NPers. kare(e) had been borrowed from Sogdian.—(20) Pte. pres, pl (21) 3nd pl. pres, (or subj.), MPers. pret. pass. =Sogd. abstract from pte. pass. + hy became, took place", (28) iterative pte., from MPers. "em- = Sogd. ()pF'm both of which are unknown. It seems likely that the words connected by etymology, notwithstanding the apparent discrepancy of thesibilants.? But MPers. swyy = svyay, Pabl. sud = suy compared to Av. dud- allow the derivation of MPers. -sam- from Olr .-fam- Av. afama- "to swallow, gulp” (NPers. dédmidan),* .- from *apa-Mma-? The appearance of an iterati
=== DKS kaurva/kalva ===
=== HUB kal ===
4939:kahln *Mitgift* = arm. kapSnl?; parvln 'Plejaden' s. oben
```


## [2026-09-06T16:13:24.879Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\ngrep -n \"کچل\\|kelewo\\|kalwo\\|calvus\\|kaurva\" ARY_pages.txt ARY_latin_index_pages.txt | head -20\necho \"=== camisia ===\"; grep -n \"camisia\\|chemise\\|قمیص\\|شمیز\" ARY_pages.txt ARY_latin_index_pages.txt | head -20",
 "description": "Grep Aryanpur"
}
```


### [2026-09-06T16:13:24.946Z] TOOL RESULT

```
=== camisia ===
```


## [2026-09-06T16:13:26.460Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%B4%D9%85%DB%8C%D8%B2",
 "prompt": "What does Mo'in's Farhang-e Farsi give for شمیز? Quote the entry including any origin tag such as [فر.] (French)."
}
```


### [2026-09-06T16:13:30.576Z] TOOL RESULT

```
According to Mo'in's Farhang-e Farsi dictionary, the entry for شمیز is:

"(شُ) [ فر. ] (اِ.) مقوا."

This indicates the word has French origins (marked as [فر.]), and it refers to cardboard or stiff paper material.
```


## [2026-09-06T16:13:36.879Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D9%82%D9%85%DB%8C%D8%B5",
 "prompt": "What does Mo'in's Farhang-e Farsi give for قمیص? Quote the entry including the origin tag (Arabic [ع.]?) and the meaning, and mention قمیصه if present."
}
```


## [2026-09-06T16:13:37.280Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Calvary",
 "prompt": "Quote Etymonline's etymology of Calvary and of Calvin/Calvinism if present."
}
```


### [2026-09-06T16:13:40.725Z] TOOL RESULT

```
# Mo'in's Definition of قمیص

According to the entry shown, Mo'in's Farhang-e Farsi provides this definition:

"(قَ مِ) [ ع . ] (اِ.) پیراهن"

This indicates the word is of Arabic origin (marked as [ ع . ]), and it means "shirt" or "garment" (پیراهن in Persian). The entry does not include a mention of قمیصه (the Arabic feminine form).
```


### [2026-09-06T16:13:43.559Z] TOOL RESULT

```
# Etymology of Calvary and Calvin

## Calvary
"Name of the mount of the Crucifixion, late 14c., from Latin calvaria 'skull,' rendering Greek Kraniou topos, translating Aramaic gulgulta 'place of the skull.'" The Latin term relates to *calvus*, meaning "bald," referencing the hill's appearance.

## Calvin
This surname derives from "Latin Calvinus, a Roman cognomen, literally 'bald,' from calvus 'bald.'" The name became particularly associated with John Calvin (1509-1564), the French Protestant theologian and religious reformer.

## Calvinism
While the page lists "Calvinism" in the dictionary entries nearby, the specific etymology for this religious movement is not detailed in the provided content.
```


## [2026-09-06T16:13:57.626Z] TOOL CALL #58: Bash

```json
{
 "command": "ls site/pages/253.jpg 2>/dev/null; pdftoppm -f 253 -l 253 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg253 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 253"
}
```


### [2026-09-06T16:14:00.144Z] TOOL RESULT

```
site/pages/253.jpg
total 10940
drwx------ 7 sfmqrb sfmqrb    4096 Sep  6 12:13 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    1166 Sep  6 12:13 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  180887 Sep  6 11:56 bqt1637_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50592 Sep  6 11:56 bqt1637_kaz.png
-rw-rw-r-- 1 sfmqrb sfmqrb  181961 Sep  6 12:11 bqt1688_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  340758 Sep  6 12:11 bqt1709_fn2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  280452 Sep  6 12:11 bqt1709_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67391 Sep  6 11:49 build225.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49952 Sep  6 11:57 build234b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   32265 Sep  6 11:51 build234.py
-rw-rw-r-- 1 sfmqrb sfmqrb   24770 Sep  6 12:01 build243.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9059 Sep  6 11:50 c237_n18.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2389 Sep  6 11:50 c237_n3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4987 Sep  6 11:52 c239_kandid2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4734 Sep  6 11:52 c239_kandid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12852 Sep  6 11:52 c239_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4087 Sep  6 11:52 c239_sandarus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   15240 Sep  6 11:54 c246_caiique.png
-rw-rw-r-- 1 sfmqrb sfmqrb   36354 Sep  6 12:02 c246_casaque.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84366 Sep  6 11:54 c246_n2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51690 Sep  6 11:54 c246_n6.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13719 Sep  6 12:02 c248_p3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30759 Sep  6 12:02 c248_p4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2750 Sep  6 12:02 c248_persian2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3046 Sep  6 12:02 c248_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4259 Sep  6 12:13 c250_celare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7170 Sep  6 12:13 c250_kolba.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4529 Sep  6 12:13 c250_sarez.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2071 Sep  6 11:26 c_ijlak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169482 Sep  6 11:58 crop_1648b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45260 Sep  6 11:57 crop_1648.png
-rw-rw-r-- 1 sfmqrb sfmqrb  305924 Sep  6 11:57 crop_1731.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb     724 Sep  6 12:11 drive.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4491 Sep  6 12:13 fix.py
-rw-rw-r-- 1 sfmqrb sfmqrb   83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb    2303 Sep  6 11:25 j.json
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb   77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67513 Sep  6 11:27 mk217.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74459 Sep  6 11:33 mk218b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78297 Sep  6 11:32 mk223.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47928 Sep  6 11:38 mk224.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53093 Sep  6 11:40 mk226.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51303 Sep  6 11:39 mk228.py
-rw-rw-r-- 1 sfmqrb sfmqrb   29152 Sep  6 11:37 mk229.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47535 Sep  6 11:47 mk230.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64267 Sep  6 11:59 mk235.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73422 Sep  6 12:02 mk237.py
-rw-rw-r-- 1 sfmqrb sfmqrb   81037 Sep  6 12:03 mk240.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80347 Sep  6 12:08 mk242.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58802 Sep  6 12:07 mk244.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:52 p233
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 p245
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 p249
-rw-rw-r-- 1 sfmqrb sfmqrb   33321 Sep  6 11:51 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   30335 Sep  6 12:07 part2.py
-rw-rw-r-- 1 sfmqrb sfmqrb   38036 Sep  6 12:11 part3.py
-rw-rw-r-- 1 sfmqrb sfmqrb   54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb  141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb  194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb  147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb  118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb   90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80963 Sep  6 11:32 pg225.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161218 Sep  6 11:26 pg226hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54381 Sep  6 11:31 pg227.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78760 Sep  6 11:27 pg229hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42112 Sep  6 11:26 pg229.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65310 Sep  6 11:32 pg230.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69894 Sep  6 11:34 pg231.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67111 Sep  6 11:35 pg233.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82071 Sep  6 11:44 pg234.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47149 Sep  6 11:44 pg236.png
-rw-rw-r-- 1 sfmqrb sfmqrb  125593 Sep  6 11:50 pg237hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67972 Sep  6 11:50 pg237.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168221 Sep  6 11:52 pg239hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81026 Sep  6 12:03 pg239.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83594 Sep  6 12:03 pg239_small.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81131 Sep  6 11:51 pg240.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80947 Sep  6 11:59 pg244.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80632 Sep  6 11:55 pg245.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79253 Sep  6 11:54 pg246.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64208 Sep  6 12:04 pg247.png
-rw-rw-r-- 1 sfmqrb sfmqrb  142780 Sep  6 12:02 pg248hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49887 Sep  6 12:02 pg248.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82530 Sep  6 12:05 pg249.png
-rw-rw-r-- 1 sfmqrb sfmqrb  123419 Sep  6 12:13 pg250hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89076 Sep  6 12:13 pg250.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75263 Sep  6 12:04 pg251.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74772 Sep  6 12:13 pg252.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68850 Sep  6 12:14 pg253.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71025 Sep  6 12:13 pg254.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55906 Sep  6 12:13 pg255.png
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 __pycache__
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   53545 Sep  6 12:03 w241.py
```


## [2026-09-06T16:14:03.200Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg253.png"
}
```


### [2026-09-06T16:14:03.537Z] TOOL RESULT

```

```


## [2026-09-06T16:14:03.535Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T16:14:22.387Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== watkins kem ===\"; grep -n \"^kem-\\|^kem\\|^kel-\\|^kel\\b\\|hemidi\\|Hemd\\|calvus\" AHD_watkins1985.txt | head -20\necho \"=== watkins search bald ===\"; grep -n -i \"bald\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins 1985"
}
```


### [2026-09-06T16:14:22.452Z] TOOL RESULT

```
=== watkins kem ===
602:kel-1, To strike, cut. Hypothetical base of derivatives referring to something broken or cut off; twig, piece of wood. I. Basic form *kel- in suffixed o-grade form *kol-o- in Greek kolos, docked, kolobos, maimed: COLOBOMA. II. Extended form *keld-. 1.Germanic *helt- in Old English hilt: HILT. 2. Zero-grade extended form *kid- in a. Germanic *hulta- in Old English holt, wood: HOLT; b. Greek klados, branch, shoot: CLADOCERAN, CLADODE, CLADOGENESIS, CLADOPHYLL, PHYLLOCLADE. 3. Variant Celtic zero-grade extended form *klad- in: a. suffixed form *klad-yo-, Celtic source of Latin gladius, sword: GLADIATE, GLADIATOR, GLAIVE; b. suffixed form *klad- ibo- in Gaelic claidheamh, sword: CLAYMORE. 4. O-grade extended form *kold- in: a. Germanic *haltaz, “with a broken leg,” in Old English compound lemphealt, limp- ing, halting (lemp-, hanging loosely; see leb-'), probable source of obsolete limphalt, lame: LIMP; b. Germanic derivative verb *haltén in Old English healtian, to limp: HALT’, III. Extended form *keb-. 1. Zero-grade form *klo- in: a. Greek kia- in (i) Greek klan, to break: CLAST, CLASTIC; CLASMATOCYTE, OSTEOCLAST, PLAGIOCLASE (ii) Greek klén (< *kla-6n), twig: CLONE; b. suffixed form *klo-ro- in Greek kléros, lot, allotment (< “that which is cut off”): CLERK; C. suffixed form *kb-mn in Greek kléma, twig: CLEMATIS; d. suffixed form *kb-mo- in Latin calamitds, injury, damage, loss: CALAMITY. 2. O-grade form *kob- in suffixed form *kols-bho- in Greek kolaphos, a blow: coPE!, coup. See extension kleg-. [Pok. 3 kel- 545.]
603:kel-2. To cover, conceal, save. I. O-grade form *kol-. 1. Germanic *haljé, the underworld (< ‘concealed place’), in: a. Old English ell, hell: HELL; b. Old Norse Hel, the underworld, goddess of death: HEL. 2. Germanic *halld, covered place, hall, ini a. Old English heal, hall: HALL; b. Old Norse Adil, hall: VALHALLA. 3. Suffixed form *kol-eyo- in Greek koleon, koleos, sheath: COLEUS; COLEOPTERA, COLEOPTERAN, COLEOPTILE, COLEORHIZA. II. Zero-grade form *k/-. 1.Germanic *hul- in: a. Old English Aulu, husk, pod (< “that which covers”): HULL; b. Old English hol, a hollow: HOLE; c. Old English holh, hole, hollow: HOLLOW; d. Old English healh, secret place,
639:kleu-2. To wash, clean. 1. Latin clodca, sewer, canal: CLOACA. 2. Zero-grade form *klu- in Greek kluzein, to wash out: CLYSTER; CATACLYSM. [Pok. 2. kleu- 607.] kleu-3. Possibly hook, peg. I. Extended zero-grade form *klud- possibly in Germanic *Aluta-, lot, portion (seman- tic development obscure). 1. Old English Alot, lot: Lor. 2. Dutch lot, lot: LOTTERY. 3. Old French lot (> French lot), lot, portion: LOTTO; ALLOT. II. Suffixed variant form *klau-do- in Latin claudere, to close (< “to lock with a hook, bolt”): CLAUSE, CLOISONNE, CLOISTER, CLOSE, (CLOSURE), (CLOZE); CONCLUDE, ECLOSION, EXCLUDE, INCLUDE, OCCLUDE, PRECLUDE, RECLUSE, SECLUDE. III. Variant form *k/dw-. 1. Suffixed form *kldw-i- in Latin cldvis, key: CEMBALO, CLAVICLE, CLAVIER, CLEF, KEVEL; CLAVICHORD, CONCLAVE, ENCLAVE. 2. Suffixed form *kldw-o- in: a. Latin cldévus, nail: CLOVE!, CLOY; b. Latin clava, club: CLAVATE; CLAVICORN, CLAVIFORM. 3. Suffixed form *k/dw-yo- in: a. Greek kleiein, to close: CLATHRATE; b. Greek verbal adjective kleistos, closed: CLEISTOGAMOUS, CLEISTOTHECIUM. [Pok. k/éu- 604.] klewo-. Bald. Variant *kal(a)wo- in Latin calvus, bald: CALVARIUM. [Pok. k,/ouo- 554.]
=== watkins search bald ===
330:3. O-grade form *bhol- in Germanic *ball- in: a. Old English beallucas, testicles: BOLLIX; b. Old Norse bdllr, ball: BALL; c. Danish bolle, round roll, akin to the probable Scandinavian source of BILBERRY; d. Middle High German baile (> Italian balla, palla), ball: BAL- LOON, BALLOT; PALL-MALL; e. French baile, ball: BAL- LOTTEMENT; f. Old French baie, rolled-up bundle: BALE!. 4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in: a. Old English bald, beald, bold: BOLD; b. Old High German bald, bold: BAWD. 5. Suffixed o-grade form *bhol-n- in Latin follis, bellows, inflated ball: FOLLICLE, FOOL!; (FOLLICULITIS). 6. Possibly Greek phalaina, whale: BALEEN. 7. Conceivably (but more likely unrelated) Greek phellos, cork, cork oak: PHEL- LEM; PHELLODERM, PHELLOGEN. (The following deriva- tives of this root are entered separately: bhel-?, bhelgh-, bhlei-, bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Germanic *bladaz in Old English bled, leaf, blade: BLADE. [Pok. 4. bhel- 122.] bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to bellow, bark, roar: BELL?; b. Old English belle, a bell: BELL!; c, Old English belgan, bylgan, to become enraged: BELLOW; d. perhaps Old English bealcan, *b(iJelcan, to utter, belch forth: BELCH; e. Middle High German buldern, boldern, to make noise: POLTERGEIST; f. Icelandic baula, to low, akin to the Scandinavian source of Middle English baulen, to howl: BAWL. [Pok. 6. bhel- 123.] bheld-. To knock, strike. Zero-grade form *bhid- in Germanic *bult-, missile, in Old English bolt, heavy arrow, bolt: BouT!. [Pok. bheld- 124.] bhelg-. Also bhelk-. A plank, beam. 1. Germanic *balku- in Old English balc(a), ridge: BALK. 2. Germanic *balk6n- in: a. Old French bauch, beam: DEBAUCH; b. Old Italian balcone, scaffold: BALCONY. 3. Suffixed zero-grade form *bhik-yo- in Latin fulcire, to prop up, support: FULCRUM. 4. Possibly Greek phalanx, beam, finger bone, line of battle: PHALANGE, PHALANX. [Pok. 5. bhel- 123.] bhelgh-. To swell. Extension of bhel-2. 1. Germanic *balgiz in Old English bel(ijg, belig, purse, bellows: BELLOWS, BELLY. 2. Germanic *bulgjan in Old Norse bylgja, a wave: BILLOW. 3. Germanic *bolgstraz in Old English bolster, cushion: BOLSTER. 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.) bhelu-. To harm. Germanic *balwaz in Old English bealo, b(e)alu, harm, ruin, bale: BALE?. [Pok. bheleu- 125.] bhendh-. To bind. 1. Germanic *bindan in Old English bindan, to bind: BIND; WOODBINE. 2. O-grade form *bhondh- in Germanic *band- in: a. Old English bend, band, ribbon, akin to the Germanic source of Old French bende, band: BEND?; b. Old English bendan, to bend: BEND!; c. Old Norse band, band, fetter: BAND!, BOND; d. Old French bande, bond, tie, link: BAND!. 3. Zero-
476:gal-'. Bald, naked. Suffixed form “gal-wo- in Germanic *kalwaz in Old English calu, bare, bald: cALLOow. [Pok. 1. gal- 349.]
528:in Greek khriein, to anoint: CHRISM, CHRIST, CHRISTEN, (CHRISTIAN); (CHRISTMAS). [Pok. ghréi- 457.] ghreib-. To grip. 1. Germanic *grip- in Old English gripe, grasp, and gripa, handful: crip!. 2. Germanic *gripan in: a. Old English gripan, to grasp: GRIPE; b. Old French gripper, to seize: GRIPPE. 3. Suffixed o-grade form *ghroib-eyo- in Germanic *graipjan in Old English grd- pian, to feel for, grope: GROPE. [Pok. ghreib- 457.] ghrem-. Angry. 1. Germanic *grimmaz in: a. Old English grim(m), fierce, severe: GRIM; b. Old French grimace, a grimace: GRIMACE. 2. Germanic *grum- in Middle Dutch grommen, to mutter angrily, probably akin to Middle English grummen, to grumble: GRUMBLE. 3. Suffixed o-grade form *ghrom-o- in Russian grom, thunder: Po- crom. [Pok. 2. ghrem- 458.] ghrendh-. To grind. 1. Germanic “grindan in Old Eng- lish grindan, to grind: GRIND. 2. Germanic *grinst-, a grinding, in Old English grist, the action of grinding: GRisT. 3. Latin frénum (< frendere, to grind), horse’s bit (on which its teeth grind), bridle: FRENULUM, FRENUM; REFRAIN). 4, Variant form *ghrend- is sometimes but improbably regarded as the root of Greek khondros, granule, groats, hence cartilage: CHONDRO-; HYPOCHON- DRIA, MITOCHONDRION. [Pok. ghren- 459.] ghréu-. To rub, grind. Extension of gher-4. 1. Germanic *greut- in Old English gréot, sand, gravel: GRIT. 2. Ger- manic *grut- in Old English grotan, pieces of hulled grain, groats: GROATS. 3. Germanic “grit- in: a. Old English griit, coarse meal: GRouT; b. Old French gruel, porridge: GRUEL. 4, Germanic *grautaz, coarse, thick (< “coarsely ground”), in: a. Old English gréat, coarse, thick, bulky, large: GREAT; b. Middle Dutch groot, thick: Groat. 5. Germanic *griiw-, to recoil from (< “to be offended, be grated on by”), in Middle Dutch griiwen, to abhor, akin to Middle English grue, horrible: GRUESOME. 6. Variant form *ghrow- in Greek khrés, skin (< “rough surface” ?), hence flesh, complexion, color: RHODOCHRO- SITE. 7. Suffixed variant form *ghré-mn in Greek khréma, skin, complexion, color (semantic development as in 6. above): CHROMA, CHROMATIC, CHROMATO-, CHROME, -CHROME, (CHROMIUM), CHROMO-; ACHRO- Matic. 8. Probably Celtic *graw- in Old French grave, greve, coarse sand, gravel: GRAVEL. 9. Probably Latin *grau-, to touch, graze, in con-gruere, to agree (com-, together; see kom): CONGRUENT. [Pok. 2. ghréu- 460.] ghwer-. Wild beast. 1. Suffixed form *ghwer-o- in Latin ferus, wild: FERAL, FIERCE. 2. Compound *ghwero-okv-, “of wild aspect” (*-ak-, “-looking”; see okw-), in Latin feréx (stem feréc-), fierce: FEROCIOUS. 3. Length- ened-grade form *ghwér- in Greek thér, wild beast: TREACLE; THEROPOD. [Pok. ghuér- 493.] gladh-. Smooth. Suffixed form “gladh-ro- in Latin gla- ber, smooth, bald: GABRO, (GLABELLA), GLABROUS. gleubh-. To cut, cleave. 1. Germanic *k/euban in Old English cléofan, to split, cleave: CLEAVE!. 2. Germanic *klub-, a splitting, in: a. Old English clufu, clove (of garlic): CLOVE*; b. Middle Dutch clove, a cleft: KLOOF. 3. Germanic *k/aubri- in: a. Old Norse kleyfr, easy to split, perhaps akin to Middle English cliver, “expert in seizing,” skillful: CLEVER; b. Old Norse lofi, a cleft, akin to English clevi, “cleft instrument,” clevis: CLEVIS. 4. Zero-grade form *glubh- in Greek gluphein, to carve: GLYPH, GLYPTIC; ANAGLYPH, HIEROGLYPHIC. 5. Suffixed zero-grade form *glubh-md- in Latin glima, husk of grain: GLUME. [Pok. gleubh- 401.] glégh-. Thorn, point. 1. Suffixed form *glégh-i- in Greek glokhis, barb of an arrow: GLOCHIDIUM. 2. Suffixed form *glégh-ya in Greek gléssa, glétta, tongue, hence also language: GLOSS2, (GLOSSARY), GLOTTIS; BUGLOSS, GLOS- SOLALIA, ISOGLOSS, POLYGLOT, PROGLOTTID. [Pok. glégh- 402.] gno-. To know. Contracted from *gnoo-. 1. Variant form *gné- in Germanic *kné(w)- in Old English cndwan, to know: KNOW. 2. Zero-grade form *gno- in: a. Germanic
639:kleu-2. To wash, clean. 1. Latin clodca, sewer, canal: CLOACA. 2. Zero-grade form *klu- in Greek kluzein, to wash out: CLYSTER; CATACLYSM. [Pok. 2. kleu- 607.] kleu-3. Possibly hook, peg. I. Extended zero-grade form *klud- possibly in Germanic *Aluta-, lot, portion (seman- tic development obscure). 1. Old English Alot, lot: Lor. 2. Dutch lot, lot: LOTTERY. 3. Old French lot (> French lot), lot, portion: LOTTO; ALLOT. II. Suffixed variant form *klau-do- in Latin claudere, to close (< “to lock with a hook, bolt”): CLAUSE, CLOISONNE, CLOISTER, CLOSE, (CLOSURE), (CLOZE); CONCLUDE, ECLOSION, EXCLUDE, INCLUDE, OCCLUDE, PRECLUDE, RECLUSE, SECLUDE. III. Variant form *k/dw-. 1. Suffixed form *kldw-i- in Latin cldvis, key: CEMBALO, CLAVICLE, CLAVIER, CLEF, KEVEL; CLAVICHORD, CONCLAVE, ENCLAVE. 2. Suffixed form *kldw-o- in: a. Latin cldévus, nail: CLOVE!, CLOY; b. Latin clava, club: CLAVATE; CLAVICORN, CLAVIFORM. 3. Suffixed form *k/dw-yo- in: a. Greek kleiein, to close: CLATHRATE; b. Greek verbal adjective kleistos, closed: CLEISTOGAMOUS, CLEISTOTHECIUM. [Pok. k/éu- 604.] klewo-. Bald. Variant *kal(a)wo- in Latin calvus, bald: CALVARIUM. [Pok. k,/ouo- 554.]
716:biter,” a small biting insect, in (i) Old English mite, mite: MITE! (ii) Middle Dutch mite, insect, small object, small coin: MITE?; c. possibly Old French mahaigner, to maim (> Anglo-Norman mangler, to hack): MAIM, MANGLE!, MAYHEM. 2. Suffixed form *mai-lo- in Old Irish méel, shorn, bald, hornless, akin to the source of MULEY. [Pok. 1. mai- 697.]
936:form *sk(hjid-yo- in Greek skhizein, to split: SCHISM, SCHIST, SCHIZO-; C. nasalized zero-grade form *ski-n-d- in Latin scindere, to split: SCISSION; EXSCIND, PRESCIND, RESCIND. 5. Extended root *skeit- in: a. Germanic *skaith-, *skaidan in (i) Old English scéadan, to sepa- rate: SHED! (ii) perhaps Old English scéath, sheath (< “split stick”): SHEATH; b. Germanic *skidam in Old Norse skidh, log, stick, snowshoe: SKI; C. o-grade form *skoit- in Latin scittum, shield (< “board”): ECU, ES- CUDO, ESCUTCHEON, ESQUIRE, SCUDO, SCUTUM, (SQUIRE). 6. Extended root *skeip- in Germanic *skif- in: a. Middle English sheve, pulley (< “piece of wood with grooves”): SHEAVE?; b. Old Norse skifa, to slice, split, akin to the Scandinavian source of SKIVE; c. Middle Low German schever, splinter, akin to the possible Low German source of Middle English schivere, scivre, splinter: SHIVER?. [Pok. skei- 919.] skel-'. Also kel-. To cut. 1. Germanic *skalj6, piece cut off, shell, scale, in: a. Old English scell, sciel, shell: SHELL; b. Italian scaglia, chip: SCAGLIOLA. 2. Germanic *skalé in: a. Old English sc(e)alu, husk, shell: SHALE; b. Old French escale, husk, shell: scALE!. 3. Germanic *skal- in: a. Old Norse skalli, bald head (< “closely shaved skull”): SCALL; b. Old Norse skalpr, sheath, shell, akin to the source of Middle English scalp, scalp: SCALP. 4. Germanic *skél6é in Old Norse skal, bowl, drinking vessel (made from a shell): SCALE’, SKOAL. 5. Germanic *skelduz in Old English scield, shield (< “board’’): SHIELD. 6. Germanic *skeli- in: a. Old Norse skil, reason, discernment, knowledge (< “‘incisiveness”): SKILL; b. Middle Dutch schillen, to diversify, with past partici- ple schillede, separated, variegated, akin to the Low German source of Middle English scheld, variegated: SHELDRAKE. 7. Germanic skulé, a division, in Middle Low German schdle, troop: SCHOOL?, SHOAL’. 8. Suffixed variant form *kel-tro- in Latin culter, knife: COLTER, CULTRATE, CUTLASS. 9. Suffixed zero-grade form “skl-yo- in Greek skaillein, to stir up, hoe (> skalenos, uneven): SCALENE. 10. Extended root *skelp- in: a. Germanic *skelf- in Middle Low German schelf, shelf (< “split piece of wood”): SHELF; b. possibly Germanic *halbaz (< variant root *kelp-), divided, in Old English healf, half: HALF; C. perhaps variant *skalp- in Latin scalpere, to cut, scrape, with derivative sculpere (originally as the combining form of scalpere), to carve: SCALPEL, SCULP- TURE. [Pok. 1. (s)kel- 923.] skel-2. To be under an obligation. O-grade (perfect) form *skol- in Germanic *skal-, I owe, hence I ought, in Old English sceal (used with the first and third person singular pronouns), shall: SHALL. [Pok. 2. (s)kel- 927.] skel-3. Also kel-. Crooked. With derivatives referring to a bent or curved part of the body, such as a leg, heel, knee, or hip. 1. Suffixed form *skel-ko- in Germanic *skelha- in Old High German scilihen, to wink, blink (> German Schiller, iridescence): SCHILLER. 2. Suffixed form *skel-es- in Greek skelos, leg: ISOSCELES, TRISKELION. 3. Suffixed o-grade form “skol-yo- in Greek skolios, crooked: sco.iosis. 4. Lengthened o-grade form *skol- in Greek skéléx, earthworm, grub (< “that which twists and turns”): SCOLEX. 5. Suffixed lengthened-grade form *k6l-o- in Greek kélon, limb, member: COLON}. 6. Attrib- uted (quite doubtfully) by some to this root is Greek kulindein, to roll: CALENDER, CYLINDER. [Pok. 4. skel- 928.] skele-. To parch, wither. Variant *sk/é-, contracted from *skleo-. 1. Greek skellesthai, to dry, whence skeletos (< suffixed form *skeb-to-), dried up (body), mummy: SKELETON. 2. Suffixed variant form *sk/é-ro- in Greek skléros, hard: SCLERA, SCLERO-, SCLEROMA, (SCLEROSIS), (SCLEROTIC), SCLEROTIUM, SCLEROUS; SCLEROTIZATION. [Pok. 3. (s)kel- 927.] skeng-. Crooked. Germanic *skank6n-, “that which bends,” leg, in Old English sc(e)anca, shinbone: SHANK. [Pok. (s)keng- 930.]
1146:TRORSE, SUBVERT, TERGIVERSATE, TRANSVERSE, UNI- VERSE. 5. Balto-Slavic *wirstd-, a turn, bend, in Russian versta, line: VERST. II. Root *wreit-, to turn. Germanic *writh-, *wraith- in: a. Old English writha, band (< “that which is wound around”): WREATH; b. Old English writhan, to twist, torture: WRITHE; Cc. Old English wrath, angry (< “tormented, twisted”): WRATH, WROTH. III. Root *wergh-, to turn. 1. Germanic *wurgjan in Old English wyrgan, to strangle: WORRY. 2. Nasalized vari- ant *wrengh- in: a. Germanic *wreng- in Old English wringan, to twist: WRING; b. Germanic *wrang- in (i) Old Norse *vrangr, rangr, curved, crooked, wrong, akin to the Scandinavian source of Middle English wrong, wrong: WRONG (ii) Low German wrangeln, to wrestle, akin to the Low German source of Middle English wranglen, to wrangle: WRANGLE. IV. Root *werg-, to turn. 1. Nasalized variant form *wreng- in Germanic *wrankjan in: a. Old English wrencan, to twist: WRENCH; b. Old English gewrinclian, to wind (ge-, col- lective prefix; see kom): WRINKLE. 2. Latin vergere, to turn, tend toward: VERGE?; CONVERGE, DIVERGE. V. Root *wreik-, to turn. 1. Germanic *wrig- in: a. Old English wrigian, to turn, bend, go: wRy; b. Middle Low German wriggeln, to wriggle: WRIGGLE. 2. Germanic *wrthst- whence *wristiz in Old English wrist, wrist: wRIsT. 3. Secondary Germanic derivative *wraistjan in Old English wréstan, to twist, with its frequentative *wréstlian, to wrestle: WREST, WRESTLE. 4. Possibly o-grade form *wroik- in Gaulish *briiko, heather (> French bruyére, heath): BRIAR}. VI. Germanic root *wrib- in Old French riber, to be wanton: RIBALD. VII. Root *werb-, also *werbh-, to turn, bend. 1. Ger- manic *werp-, *warp-, “to fling by turning the arm,” in Old English weorpan, to throw away: WARP. 2. Latin verber, whip, rod: REVERBERATE. 3. Latin verbéna, sacred foliage: VERBENA, (VERVAIN). 4, Zero-grade form *wrb- in Greek rhabdos, rod: RHABDOMANCY, RHABDOVI- Rus. 5. Nasalized variant form *wrembh- in Greek rhom- bos, magic wheel, rhombus: RHOMBUS. VIII. Root *werp-, to turn, wind. 1. Metathesized form *wrep- in Germanic *wrap- in Danish dialectal vraule, to wind, akin to the source of Middle English wrappen, to wrap: wraP. 2. Zero-grade form *wrp- in Greek rhaptein, to sew (> rhaphé, suture): RAPHE, RAPHIDE; RHAPSODY, STAPHYLORRHAPHY, TENORRHAPHY. IX. Root *wrmi-, worm; rhyme word to k*rmi-. 1. Germanic *wurmiz in Old English wyrm, worm: worm. 2. Latin vermis, worm: VERMEIL, VERMI-, VERMICELLI, VERMICULAR, VERMIN. [Pok. 3. ver- 1152.]
2183:RIBALD wer-3
```


## [2026-09-06T16:14:34.135Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \"kem-[0-9]*\\. [^.]*\\.\" AHD_watkins1985.txt | head -10; echo \"---\"; grep -n \"Pok. 3. kem\\|Pok. kem\\|Pok. 1. kem\\|Pok. 2. kem\" AHD_watkins1985.txt | head; echo \"--- IEC ---\"; grep -n \"^kamisia\\|^kem-\\|^kemos\\|^kamos\" IEC.txt | head -10; echo \"--- IEC kalwos ---\"; grep -n \"^kalwos\\|^kelewos\\|^kalw\" IEC.txt | head",
 "description": "Search Watkins and Mann for kem roots"
}
```


### [2026-09-06T16:14:34.222Z] TOOL RESULT

```
608:kem-3. To hum.
---
608:Germanic *hal6n, to call, in: a. Dutch halen, to haul, pull (2? < “to call together, summon”): KEELHAUL; b. Old French haler, to haul: HALE?, HAUL. ITI. Zero-grade form *klo- (> *kal-). 1. Suffixed form *kal-yo- in Latin conct- lium, a meeting, gathering (< “a calling together”; con-, together; see kom): CONCILIATE, COUNCIL. 2. Suffixed form *kal-énd- in Latin kalendae, the calends, the first day of the month, when it was publicly announced on which days the nones and ides of that month would fall: CALENDAR, CALENDS. 3. Suffixed form *kal-e- in Greek kalein (variant klé-), to call: ECcLESIA, PARACLETE. 4. Suffixed form *kal-d- in Latin caldre, to call, call out: INTERCALATE, NOMENCLATOR. 5. Suffixed form *klp-ro- or suffixed variant form *klaa-ro- contracted to *kld-ro- in Latin clarus, bright, clear: CLEAR, GLAIR; CHIARO- SCURO, CLAIRVOYANCE, DECLARE, ECLAIR, ECLAIRISSE- MENT. IV. Possibly extended zero-grade form *kid-, becoming *klad- in suffixed form *klad-ti- in Latin classis, summons, division of citizens for military draft, hence army, fleet, also class in general: cLAss. [Pok. 6. kel- 548.] kelp-. To hold, grasp. O-grade form *kolp- in Germanic *halb- in: a. Old English hielfe, handle: HELVE; b. suf- fixed form *halb-ma- in (i) Old English helma, rudder, tiller: HELM! (ii) Middle High German helm, handle: HALBERD; C. suffixed form *half-tra- in Old English helftre, halter: HALTER}. [In Pok. 1. (s)kel- 923.] kem-1, Hornless. 1. Germanic *skamm- in Old Norse skammr, “hornless,” short: SCANT. 2. Suffixed form *kem-tydé in Germanic *hinthj6 in Old English hind, doe: HIND?, [Pok. 2. kem- 556.] kem-?. To compress. Germanic *hamjam, a compressing, hence a doubling, in Old English hem/(m), a doubling over, a hem: HEMI, [Pok. 1. kem- 555.] kem-3. To hum. Germanic *hum- in Middle English hummen, to hum: HUM. [Pok. 2. kem- 556.] keme-. To be tired, to tire. Suffixed lengthened o-grade form *kém-n proposed by some as the preform of Greek k6ma, deep sleep, which is more likely of obscure origin: coma}. [Pok. 4. kem(g)- 557.] ken-'. To be active. 1. Suffixed o-grade form *kon-o- in Greek diakonos, servant, attendant (dia-, thoroughly): DEACON. 2. Lengthened o-grade form *kdén-d- in Latin condari, to endeavor: CONATION. [Pok. 4. ken- 564.] ken-2. Hypothetical base of a number of loosely related Germanic words referring to pinching, closing the eyes, and other obscurely associated notions. 1. Old English hnappian, to doze, nap: NAP!. 2. Old English népfléd, neap tide (fléd, tide; see pleu-): NEAP TIDE. 3. Middle Dutch nipen, to bite: n1P!. 4. Old Norse hnéggr, miserly, akin to the Scandinavian source of Middle English nigard, miser: NIGGARD. 5. Middle Dutch noppe, pile: NAP?. 6. Low German nibbein, to nibble: NIBBLE. 7. Mid- dle High German notten, to nod, perhaps akin to Middle English nodden, to nod: Nop. [Pok. 2. ken- 559.] ken-3, Fresh, new, young. 1. Suffixed form *ken-t- in Latin recens, young, fresh, new (re-, again; see re-): RECENT. 2. Suffixed zero-grade form kn-yo- in Greek kainos, new, fresh (> kainotés, newness): -CENE; CAINO- TOPHOBIA, CENOGENESIS, CENOZOIC, KAINITE. [Pok. 3. ken- 563.] ken-4, Empty. Suffixed form *ken-wo- in Greek kenos (< *kenwos), empty: KENOSIS; CENOTAPH. [Pok. ken- 564.] ken-5, Hypothetical base of several roots associated with the notions “to compress,” “something compressed.” 1. Germanic root *hnekk-, “neck” (a narrow or com- pressed part), in: a. Old English hnecca, neck: NECK; b. Old Norse hnakkur, saddle, and Old Norse hnakki, back of the neck, perhaps akin to the source of KNACKER. 2. Root *knu-, nut (< “small hard object”), in: a. extend- ed form *knud- in Old English hnutu, nut: NUT; b. ex- tended form *knuk- in Latin nux, nut: NEWEL, NOUGAT, NUCELLUS, NUCLEUS. 3. Germanic root *hnukk-, sharp projection, tip, in: a. Middle Dutch nocke, tip of a bow,
--- IEC ---
6708:kamos, kamos, see kam- (2). Cf. WP I, 388 & 507 Gk. kémós 'bridle-bit; muzzle; wicker basket;
--- IEC kalwos ---
```


## [2026-09-06T16:14:43.068Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC calvus ===\"; grep -n \"calvus\" IEC.txt | head -10\necho \"=== IEC samya/sima ===\"; grep -n \"śamyā\\|samya\\|camya\" IEC.txt | head -10\necho \"=== SYN bald ===\"; grep -n \"4.96 BALD\\|BALD\" SYN.txt | head -10\necho \"=== SYN shirt ===\"; grep -n \"SHIRT\" SYN.txt | head -5",
 "description": "Grep Mann and Buck"
}
```


### [2026-09-06T16:14:43.160Z] TOOL RESULT

```
=== IEC calvus ===
6693:kaluos, à “bald, bare; skull, head, hil. WP I, 447. Cf. WP I, 433 (Av. kaurvo “black? derives fr. koruos (3), q.v. > Gk. korós, id.); Per. (ambig.) kal ‘bald’; Lat. calvus ‘bald, bare’ beside calva ‘skull’; Osc. cf. Kalaviis (Calvius); MIr. calb ‘head’; Ir. calbh ‘hardness, baldness’; Li. kalvùs *elevat- ed. (Fris. holle ‘head’ may represent a vari- ant of type *kluon). See kluos
7411:Lat. calva ‘skull’; calvus ‘shorn, bald’; Skt. cf. áti-külvah, -kürvah beside kulvah, id.; Av. (queried) kaurvo, kaourvo Chald of horse); Per. kal ‘bald’; Fris. holle “head?
13263:pluos “pale, dim". All evidence ambig. Cf. pal- (1) with variants, & polu-, poluos (2) Arm. cf. (?) ayawt, i-st. ‘dim’ beside nvay, adj. dark’, a cpd.); Lat. palleo, Ere, v. ‘grow pale’; pallidus, adj. ‘pale’; pallor-, -oris, s. (Note: The equivalence of IE *-]u- and Lat. -all- is uncertain, see WH & EM on salvus & sollus, soll-; mollis, collum; pullus (1) & (2); pulvis, pulvinus, calvus, calva, etc. Cf. E Som- mer: HLLF: $ 46 & § 47; S. E. Mann: Czech Historical Grammar: $ 44 & § 89; S. E. Mann: Albanian Historical Grammar, pp. 36-37; S. E. Mann: Armenian and Indo-European, § 62 & $ 63)
=== IEC samya/sima ===
16698:sómos (fitting, harmonious, level, equal, smooth'. Cf. som-, sem-, sm-, etc. WP I1 491-2 Skt. sámyah, adj. ‘peaceable’; samyam, n. “peace”; cf. samanyah ‘equal, like’; Av. hàmo, adj. “equal, complete’; Tokh. A sam, B sam, adj. devel; Ir sámh, adj. “pleasant, mild, calm”; sáimhe, f. ease, calm”; Olr. sám, s. id. (and adv. “at ease"); OS somi, adj. ‘fitting’; MHG suome, adj. ‘pleasant’; OFris. som, adj. ‘equivalent’; somia, v. ‘balance’; OE som, adj. 'appeased, at peace’; f. ‘agreement’; ON scemr, adj. ‘suitable’; sómi, m. ‘honour’; OCS (and com. Sl.) samŭ, prn. & adj. ‘self; alone’; m. ‘male’
=== SYN bald ===
8116:4.93 BALD Gothsiersct Lith. plikas padaxpes ON skgllotir Lett. pliks, kails per a ee as eee pepe plésiviz calv WV. skallig, ka ia lav, plesiv calvo OE aie ee Boh. _lysy, pleSivy, pleSaty chau ME alled, calou Pol. lysy ; ean ek NE bald Russ. lysyj, pleSivyj ? a ue aa ite ee khalati-, munda- mi O calo Vv. kaurva- maol MHG kal pe NHG kahl m
=== SYN shirt ===
10513:ING; PERSONAL ADORNMENT AND CARE 421 cLOTHIN™: 6.44 SHIRT ¢ Lith.  margkiniai ON serkr, skyrta 5 rm) Dak, skjorte Lett. krekls wi £5
```


## [2026-09-06T16:14:50.778Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10513,10530p' SYN.txt | cut -c1-3000; echo \"=== bald discussion ===\"; sed -n '8116,8130p' SYN.txt | cut -c1-2500",
 "description": "Read Buck SHIRT and BALD sections"
}
```


### [2026-09-06T16:14:50.838Z] TOOL RESULT

```
ING; PERSONAL ADORNMENT AND CARE 421 cLOTHIN™: 6.44 SHIRT ¢ Lith.  margkiniai ON serkr, skyrta 5 rm) Dak, skjorte Lett. krekls wi £5
Gtk: ih 0 aS Sw. skjorta Chsl. riza, sratica, koSulja x6 hee jatecamisi@ =O sere, scyrte, hemepe SCr.  koSulja, rubaéa Jat. cia ME shertle Boh.  koSile It snemise NE shirt Pol. koszula Fr gmisa Du. _hemd Russ. rubaSka
e i Skt. cdmulya-
OHG  hemidi
nase i ea caimmse, gun? MHG _ hemde
a |éine NHG  hemd crys pe
, nica, already given Grk, se cae nearest equiva- under rghitt in the classical period. loxos and xir@moy Were AP- hort xerwy OF poreye ent
 s ntig prevouTns undergarment , if ie interior and Lat. subtuicula (fr, *sub-uere, parallel to ind-uere, ex- ur) would be a sort of undershirt. But the use of a linen shirt under a wool- len tunic first appears in the 4th century ap. Cf. Marquardt, Rom. Privatleben $70, 552,
1. Derivs. of IE *kem- seen also in words for ‘covering’, ‘sky’, etc. But the Gallo-Lat. form prob. fr.Gmc. Walde- P.1386f. Walde-H. 1.147 f. OF heme- ht, OHG hemidi, MHG hemde, NHG, Du. hemd; Gallo-Lat. camisia (> Ro- manee forms and Ir. caimmse, Byz. xapi- our, NG dro-Kauco; Fr. > NE chemise, tow only for woman’s undergarment, re- lacing smock and shift); Skt. camulya-. peth, ei etym. dub., WE) Tough the mot ac, nee sure, € exact relation is ob-
Pokorny, KZ
Grk. xeTo” plied to a S
Pedersen 1 6Lf 3811,
Th anart : imap for-4 eniiyg | "™” Coat? (6.43). Peder- VY, crys, Br, krez = Tr.
criss ‘girdle’ : ez, Pol. £ dle i
2 pat ‘money-belt’,
ON * *€dersen 1.42 f.
the ug ea ip. serk, Sw. sdrk not sti tee OF Serc, ME serke
bg oon for ‘shirt’),
=== bald discussion ===
4.93 BALD Gothsiersct Lith. plikas padaxpes ON skgllotir Lett. pliks, kails per a ee as eee pepe plésiviz calv WV. skallig, ka ia lav, plesiv calvo OE aie ee Boh. _lysy, pleSivy, pleSaty chau ME alled, calou Pol. lysy ; ean ek NE bald Russ. lysyj, pleSivyj ? a ue aa ite ee khalati-, munda- mi O calo Vv. kaurva- maol MHG kal pe NHG kahl m
the root *maz- ‘cut off, hew’, in Goth. maitan ‘hew, cut’, ON meita ‘cut’, etc. Walde-P. 2.222. Otherwise Stokes 204.
4. ON skalli (sb. ‘a baldhead’), adj. skollotir, Dan. skaldet, Sw. skallig, perh. fr. s-form of the root in Lat. calvus, ete. (above, 2). Ernout-M. 137. Falk-Torp 980 (but combined with the following).
OF calu, ME calouh (NE callow), Du. kaal (LG kal > Sw. kal), OHG kalo, MHG kal, NHG kahl: ChSl. golu ‘naked’, etc. (4.99). Walde-P. 1.537 f. Berneker 325f. Combined by some with Lat. calvus, etc. (above, 2) on the basis of IE variant initial k/g, or even as loanword from it (cf. Walde-P. 1.538).
ME balled, NE bald (cf. also Dan. beldet ‘bald, callow’, of birds), prob. fr. ball ‘white spot’ on the forehead (in spite of the fact that this is not quotable as early as balled), this (whether or not through Celtic) : Grk. ¢adapés, etc. (above, 1). Walde-P. 2.175. Falk-Torp 123. NED s.v.
5. Lith. plikas, Lett. pliks (also ‘naked’), ChSl. plévii, SCr. plesiv, Boh. plesivy, plegaty, Russ. plesivyj (also Lith. pleikas ‘bald spot’, Lett. plaikums ‘spot’) : Lith. plynas ‘plain, even, smooth’, plyné ‘plain, open field’, Norw. dial. flein ‘bald, naked’, Sw. dial. flen ‘naked’, but further root connection dub. Walde-P. 2.93. Mihl.-Endz, 3.344. Falk-Torp 235.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
318 SELECTED INDO-EUROPEAN SYNONYMS
Lett. katls ‘bald, naked, bare’: Ir. coil ‘thin, slender’, W., Corn. cul ‘lean, narrow’. Walde-P. 1.455.
6. ChSI. viiz-lysti, Boh. lysy, Pol. zysy, Russ. lysyj : Skt. rucant- ‘bright, shining’, IE *leuk-, beside *leuk- in Lat. liz ‘light’, ete. Walde-P. 2.411. Berne- ker 752.
ChSl. plévt, above, 5.
SCr. éelav, fr. Turk. kel id. (ef, above, 2, Rum. chel).
7, Skt. khalati-, Av. kaurva- - Lat. calyus, above, 2
Skt. munda- ‘with shaven head’ (also ‘hornless, blunt’), perh.: Skt. 7d- ‘crush, rub’, etc. Walde-P. 2.288 (287),
```


## [2026-09-06T16:15:08.225Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%84",
 "prompt": "For the Persian section: is there an entry کل (kal) meaning 'bald'? Give its etymology verbatim if present (Middle Persian, Avestan kaurva-, or Turkic kel?)."
}
```


## [2026-09-06T16:15:09.671Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1em-",
 "prompt": "Does this reconstruction page exist? If so, give the meaning and descendants. If not, say so."
}
```


### [2026-09-06T16:15:12.307Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T16:15:13.286Z] TOOL RESULT

```
# Persian کل (kal) - Bald Entry

Yes, there is a Persian entry for **کل** (kal) meaning "bald" under Etymology 1.

## Etymology (Verbatim)

"From Proto-Indo-European *gelH- ("naked, bald") or *kl̥H-. Cognate with English callow and/or Latin calvus, Sanskrit कुल्व (kulva)."

The entry does not mention Middle Persian, Avestan kaurva-, or Turkic kel in its etymological explanation. Instead, it traces the word back to Proto-Indo-European roots with cognates in European and Indo-Aryan languages.
```


## [2026-09-06T16:15:35.879Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6276,6286p' KLN_1966.txt; echo \"=== FSD camisa ===\"; grep -n \"^camisa\\|^camise\\b\\|^camisado\" FSD_vol1.txt | head",
 "description": "Check Klein camise entry"
}
```


### [2026-09-06T16:15:35.949Z] TOOL RESULT

```
228
Camembert,  n.,  a  soft,  rich  cheese.  —  From  Ca¬ membert,  name  of  a  village  near  Argentan  in Normandy.
cameo,  n.,  a  carved  gem.  —  It.  cammeo,  fr.  ML. camahutus,  ult.  fr.  Pers.  chumdhan ,  ‘agate’, through  the  medium  of  the  Arabic.  Cp.  camaieu. Derivative :  cameo,  tr.  v.
camera,  n.,  a  chamber.  —  L.,  ‘vault,  arched  roof, arch’,  fr.  Gk.  xotpdcpa,  which  is  rel.  to  xocp-Tvog (whence  L.  caminus),  ‘furnace’,  and  cogn.  with L.  camur ,  camurus,  ‘curved’,  fr.I.-E.  base  *qam-, *qem-,  ‘to  bend,  vault’.  Cp.  It.,  OProveng., Catal.  camera ,  Sp.  camara,  Port,  camara,  F.  cham- bre,  OHG.  chamara,  OS.  camara,  OSlav.  komora, Lith.  kamara ,  OIr.  camra,  which  all  derive  fr.
L.  camera.  Cp.  chamber.  Cp.  also  camara,  Cam- barus,  camber,  chimney,  comrade,  concamerated. For  derivatives  of  a  -^-enlargement  of  base  *qarn- see  change.  Cp.  cant,  ‘slope’.  Cp.  also  heaven, camerlengo,  camerlingo,  n.,  the  papal  chamber- lain.  —  It.,  a  hybrid  coined  fr.  camera  (see  ca¬ mera)  and  the  Teut.  suff.  -ling.  Cp.  chamberlain. Cameronian,  n.,  a  follower  of  Richard  Cameron (died  in  1680).  For  the  ending  see  suff.  -ian. Camilla,  n.,  a  girl  of  noble  birth  employed  in  reli¬ gious  offices.  —  L„  fern,  of  camillus  (q.v.) Camilla,  fern.  PN.  —  Fr.  prec.  word, camillus,  n.,  a  noble  youth  employed  in  religious offices  ( Roman  antiq.)  —  L.,  fr.  Etruscan  Ca¬ millus,  ‘Mercury’,  fr.  Gk.  Ka§|i.tAog  (whence Kaa|iTAoc;),  name  of  one  of  the  Cabiri  in  Samo- thrace.  KaSpiAoc  is  prob.  related  to  KaSpog, ‘Cadmus’,  hence  of  Hebrew  origin;  see  Cad¬ mus.  The  Hebrew  origin  of  Gk.  KaSiifXog  is  sup¬ ported  by  the  fact  that  the  name  KafJeipcu  it¬ self  (whence  L.  Cabiri)  also  derives  from  He¬ brew  (see  Cabiri).
camisado,  camisade,  n.,  a  night  attack.  —  F.  ca- misade,  fr.  OProveng.  *camisada  (fr.  camiza, ‘shirt’),  prop,  a  night  attack  in  which  the  at¬ tackers  wore  shirts  over  their  armour,  for  the sake  of  recognizing  one  another;  cp.  It.  cami- ciata,  ‘camisado’,  fr.  camicia,  ‘shirt’.  See  che¬ mise  and  -ado  and  cp.  next  word, camise,  n.,  a  light  shirt.  —  Arab,  qamif,  fr.
Late  L.  camisia.  See  chemise, camisole,  n.,  a  woman's  loose  jacket.  —  F.,  fr. OProveng.  camisola,  ‘mantle’,  dimin.  of  camisa, fr.  Late  L.  camisia.  See  chemise  and  cp.  prec. word.
camlet,  n.,  cloth  made  of  camel’s  hair  and  silk or  of  wool  and  silk.  —  F.  camelot,  fr.  Arab. khdmlat,  ‘plush’,  the  stuff  having  been  fabricated originally  in  the  East.  The  French  form  of  the word  is  due  to  an  erroneous  association  with  the word  chameau ,  ‘camel’.  The  ending  -al  (in Arab,  khdmlat)  was  mistaken  for  the  suff.  -at and  substituted  by  the  more  frequent  French suff.  -ot  (in  English  this  latter  suff.  became  -et). Derivatives:  camlet,  adj.  and  tr.  v. camomile,  n.,  an  aromatic  plant.  —  F.  camo- mille,  fr.  Late  L.  camomilla,  fr.  earlier  chamae-
melon,  fr.  Gk.  -/auxL^Xov,  lit.  ‘earth  apple’,  fr. ya.\sfA,  ‘on  the  ground’,  and  uyXov,  ‘apple’.  See chamae-  and  Malus,  ‘genus  of  the  apple  trees’, and  cp.  Chamomila.
Camorra,  n.,  name  of  a  secret  society  at  Naples.
—  It.,  fr.  camorro,  ‘a  person  in  failing  health; a  troublesome  person’,  prob.  fr.  Port,  cha- morro,  ‘with  shaven  head,  bald’,  which  is  of uncertain,  possibly  Basque,  origin.
=== FSD camisa ===
```


## [2026-09-06T16:15:43.901Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/camisia' --note 'page 253, root Kem 2, Latin camisia etymology (Proto-West Germanic *hamiþi), Byzantine Greek kamision as descendant' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%82%D9%85%D9%8A%D8%B5' --note 'page 253, root Kem 2, Arabic qamis from Latin camisia; descendants Persian qamis, English kamees' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/chemise' --note 'page 253, root Kem 2, English/French chemise < Late Latin camisia; French sense folder' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/kamees' --note 'page 253, root Kem 2, English kameez/kamees < Arabic qamis, doublet of chemise' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/calvus' --note 'page 253, root Kelewo, Latin calvus < Proto-Italic *kal(V)wos, calva/calvaria' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/Calvary' --note 'page 253, root Kelewo, English Calvary and the surname Calvin < Latin calvus' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D9%84' --note 'page 253, root Kelewo, Persian kal bald etymology' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://vajehyab.com/moein/%D8%B4%D9%85%DB%8C%D8%B2' --note 'page 253, root Kem 2, Moin s.v. shomiz [fr.] cardboard/folder' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://vajehyab.com/moein/%D9%82%D9%85%DB%8C%D8%B5' --note 'page 253, root Kem 2, Moin s.v. qamis [ar.] pirahan' 2>&1 | tail -3",
 "description": "Archive web sources"
}
```


### [2026-09-06T16:15:48.664Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4d8f7bb31064c02d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3c9e1edcc6f79400.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2ea1cf137ff350c0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/802ec391b0aa4dfa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4eec43cba1ce8f7b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9bb8ec977d9930b4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/78917d698c0bb1e6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e2622348541ec83c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b576c5013b8b2d59.txt
```


## [2026-09-06T16:16:03.618Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=213 && NR<=215' POK_02.txt | grep -n -B2 -A14 \"kem-\\|camisia\\|Jochbalken\\|hemidi\" | head -60",
 "description": "Print Pokorny p.556 German"
}
```


### [2026-09-06T16:16:05.443Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:16:08.649Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"camisia\" POK_02.txt | head; echo ---; grep -n \"Jochbalken\\|sami-k\\|samyd\\|çamyä\" POK_02.txt | head",
 "description": "Grep Pokorny German for camisia"
}
```


### [2026-09-06T16:16:08.700Z] TOOL RESULT

```
3306:lat.  camisia  (spät)  ,Hemd'  (gall.  Wort;  entlehnt  aus  germ.  *xawii/>;a- ,Hemd'^;  erst  aus  dem  Lat.  stammen  wieder  air.  caimmse  ,Hemd^,  acorn. cams  ,alba^,  bret.  kavips  ,Meßhemd^);
3308:unklar  ist  der  Anlaut  in  mcymr.  hefys  ^Frauenhemd^,  akorn.  hevis,  bret. Jiimz  ds.;  ags.  cemes  ds.  ist  Lw.  aus  camisiaj
---
3292:arm.  sami-k  PI.  ,Stirnholz  des  Ochsenjochs^  (iran.  Lw.  ?);
```


## [2026-09-06T16:16:12.010Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3283,3320p' POK_02.txt; echo \"=== leaf ===\"; awk 'BEGIN{RS=\"\\f\"} /lat.  camisia  \\(spät\\)/{print NR}' POK_02.txt",
 "description": "Print Pokorny kem entries German"
}
```


### [2026-09-06T16:16:13.966Z] TOOL RESULT

```
\       V»nc    _
r
Ai.  camara-  m.  _,bos  grunniens^ ;
mhd.  nhd.  hummen,  nhd.  hummeln,  holl.  hommelen  ,summeii^,  menc^l Tiummeriy  engl,  hum  ds._,  norw.  humre  ,leise  wiehern^;  dazu  ursprüno-] wohl  auch  ahd.  humhal,  mhd.  humhel,  hummel  m.  _,Hummel^,  rnnd.  hum^ mel  tj  engl,  humble-hee,  norw.  mdartl.  humla  f.  ds* ;
lit.  Jclmstu,  kimti  ^heiser  werden^,  kiminti  ^die  Stimme  dumpf  machen' Icimüs  ^heiser^  dumpf  lautend^,  kamäne  -,Erdhiene^^  kämme  ^Feldbiene^,  lett. kamines  f.  pl.  ^Erdbienen,  Hummeln^;  apr.  camus  ^Hummel^;
slav.  *chmeh  (ablautgleich  mit  Hummel)  in  russ.  dial.  cmeh  usw.  _,Huni- mel;,  Erdbiene^;  ksl.  russ.  komär  usw.  ;,Mücke^  (ablautgleich  mit  lit.  kamane),
WP.  I  389,  Trautmann  115  f.
1.  kein-  oder  kam-  _,Stange,  Stock,  Horn^
Ai.  sdmyä  ^Stock,  Zapfen,  Holznagel,  Stütznagel^,  av.  simä  (-i-  scheint idg.  d]  oder  =  ai.  sdmyäl)  ,ein  Teil  vom  Geschirr  des  mit  Pferden  be- spannten Wagens^,  npers.  slm  ds. ;
arm.  sami-k  PI.  ,Stirnholz  des  Ochsenjochs^  (iran.  Lw.  ?);
gr.  xffjuaä  f.  m.  ,Stange,  Pfahl,  Schaft  des  Speeres^;
dän.  schwed.  Jiammel,  norw.  dial.  Jiumul  (-homull)  ,das  Querstück  vorn am  Wagen^,  mhd.  Jiamel  ,Stange,  Klotz^ ;
über  das  schwierige  lat.  camox  ,Gemse^,  vorrom.  *kamösso-^  s.  jetzt J.  Hubschmid  ZrPh.  66,  9  ff.
WP.  I  385,  WH.  I  148,  633.  '  -
2.  kern-  ,hornlos^,  bei  sonst  gehörnten  Tierarten.
Ai.  sdma-h  ,hornlos^;
gr.  xfijwag,  -aSog  f.,  später  auch  -AS^^dg  ,iunger  Hirsch^;  'ASiKpdg'  eka- (pog  Hes. ;
anord.  hind  f.,  ags.  Mndj  ahd.   Jiinta  ,Hirschkuh,  Hindin^  (*^em-^ö);
lit.  zem.  smulas  ,hornlos^,  Smülis  m.,  smüle  f.  ,Ochs,  Kuh  ohne  Hörner^ [*km-U'  +  Formans  -lo-),  liv.  Lw.  smouV ;
vielleicht  hierher  russ.  komölyj  ,hornlos^ ;  vgl.  auch  W.  Schulze  KL Sehr.  619.
WP.  I  385  f.,  Specht  Idg.  Dekl.  132.
3.  kern-,  ,bedecken,  verhüllend
Ai.  sämulyä'  n.,  sämüla-  n.  ,wollenes  Hemd^,  samt  ,Prosopis  spicigera; Hülsenfrucht^ ;
lat.  camisia  (spät)  ,Hemd'  (gall.  Wort;  entlehnt  aus  germ.  *xawii/>;a- ,Hemd'^;  erst  aus  dem  Lat.  stammen  wieder  air.  caimmse  ,Hemd^,  acorn. cams  ,alba^,  bret.  kavips  ,Meßhemd^);
557
unklar  ist  der  Anlaut  in  mcymr.  hefys  ^Frauenhemd^,  akorn.  hevis,  bret. Jiimz  ds.;  ags.  cemes  ds.  ist  Lw.  aus  camisiaj
ahd.  hemidi  n.  ,Hemd^^  ags.  hemede  (*hamipia-)  ,Hemd^;  anord.  hamr m.  ^HüUe,  Haut,  Gestalt^,  ags.  homa  , Hülle,  Decke,  Anzug^;  lic-hama,  as. lik-hamo  ,Leib^,  ahd.  llhhin-l^klamo  ,Leib,  Körper,  Leichnam^ ^  got.  ana-, ga-hamön  ,sich  bekleiden'^,  anord.  hama-sk  ,(*sich  in  Tiergestalt  verkleiden, daher:)  rasen^;  anord.  hams  ,Schale,  Hülse,  Schlangenbalg^  (^hamisa-), vgl.  norw.  hamar  ,Kernhaus^;  hierher  auch  got.  himins^  anord.  Jiiminn (Dat.  hifne  mit  -in-  aus  -tww-,  vgl.:)  ags.  heofon,  as.  hetan  ,HimmeP, woneben  ahd.  as.  himil,  md.  liumil  ,HimmeP;  ahd.  himil  auch  ,Zimmer- decke^,  ndl.  hemel  ,Gaumen,  Dach',  nhd.  Himmelbett ^  ahd.  himiUz{z)i, mnd.  hemelte  , Zimmerdecke';  kaum  richtig  oben  S.  22  zu  ak-  , Stein'.
Eine  s-Form  skem-,  sucht  man  unglaubhaft  in  got.  skaman  ,sich  schämen', ags.  skamian  ds.,  aisl.  skqmm,  ahd.  scama  ßcham,  S-chande'  usw.  (,*sicli bedecken'  ?).
WP.  I  386,   Specht  Idg.  Dekl.  346.
j^.  kemio)'  ,sich  abmühen,  müde  werden';  kems-to-  ,ermüdet'.
Ai.  samnlte,  sdmati,  samyatij  Imp.  samT-sva  ,sich  mühen,  arbeiten,  zu- richten, zubereiten',  samitd-  ,zubereitet',  iamitdr-  , Zurichter,  Zubereiter', Sdml  f.,  sdmi  n.  ,Bemühung,  Werk,  Fleiß'  {simyati  =  ,samyati',  iima-  m. ,Zubereiter'  sind  durch  das  bedeutungsgleiche  siini  ,Fleiß'  hervorgerufen) ; sämyati  ,hört  auf,  läßt  nach'  aus  ,*ermüdet',  Aor.  aSamat^  asamlt]  säntd- ,beruhigt,  ruhig,  sanft,  mild'  (*kem9tösj  wird  seines  ä  halber  in  der  Bed. näher  mit  sämyati  assoziiert);
gr.  ycdfivü)  ,mühe  mich,  ermüde;  tr.  verfertige  (mit  Mühe)'  (wohl  ^km-n-ä-, wie  ai.  samnlte)^  Fut.  Y.aixovfiaL,  Aor.  E%a^ov,  Perf.  x^x^ijxa,  dor.  x^xfiöxoc, Partiz.  'ABv.fxri{f) (bq,  y,Lir]TÖgj  dor.  x^ißrdg,  Ttolvyiixrjrog  ,mit  vieler  Mühe  oder Sorgfalt  zubereitet',  ycd^arog  ,Ermüdung,  Anstrengung,  Mühsal,  Leiden', ä-ytiXT^g,  -fJTogj  dycdfj,ag,  -awog  ,unermüdet,  frisch',  Y.au6vT6g  ,die  Toten',  wie att.  xfix^i7xdT€g ;  o-stufig  sigo-^iö^og  ,Wolle  bereitend',  Inrto-Y.öiLog  ,Pferde- knecht',  xo^/£w  ,pflege'  usw.,  zojxidi^  ,Pflege,  das  Bringen  usw.';  dehnstufig xwjua  ,tiefer,  ruhiger  Schlaf;
mir.  cuma,  mbret.  caffou  ,Kummer'  (Pedersen  KG.  I  47,  361);  mir.  cumal jSklavin'  (,*sich  mühend,  anstrengend',  wie:)   gall.   Camulos  ,Kriegsgott' ?
WP.  I  387  f.
icemö-,  koms-,  kmä-  ,Bissen'?
Gr.  iix^r]vog  ,ohne  Imbiß,  hungrig',  ^x^ä  (äol.)'  yiyöTß/a,  svösia  Hes.; hocbstufig  Y,oy.<x)Ga'  ye^ovaa  Hes.?
558  t
lett.  kumuoss  ^Bissen^  (-nm-Reduktionsstufe ;  der  Ausgang  -uoss  aus  -ansa» vielleicht   durch   Kreuzung   mit   einem   *kan[d]s-as  =  aksl.    kq.s^   ,Stück Bissen'?  vgl.  Mühlenbach-Endzelin  Lett.-D.  Wb.  II  313);
=== leaf ===
216
```


## [2026-09-06T16:16:26.501Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nawk 'BEGIN{RS=\"\\f\"} NR==456' WLD_Bd1_pages.txt | grep -o \"kalu.\\{0,300\\}\\|calvus.\\{0,200\\}\" | head -5\necho \"=== 385/386 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==395' WLD_Bd1_pages.txt | grep -o \"camisia.\\{0,250\\}\\|sami-k.\\{0,150\\}\\|.\\{0,120\\}sīmā.\\{0,150\\}\" | head -5",
 "description": "Check Walde-Pokorny pages"
}
```


### [2026-09-06T16:16:30.526Z] TOOL RESULT

```
calvus „kahl,
calvus spricht gegen Lager-
=== 385/386 ===
ugrep: error: error at position 173
^\n\x80-\xbf][\x80-\xbf]*){0,150}
    exceeds complexity limits___/
```


## [2026-09-06T16:16:34.007Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nawk 'BEGIN{RS=\"\\f\"} NR==456' WLD_Bd1_pages.txt | grep -n -B3 -A8 \"calvus\" | head -30\necho \"=== leaf 395 ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=394 && NR<=396' WLD_Bd1_pages.txt | grep -n -B3 -A6 \"camisia\\|sami-k\" | head -30",
 "description": "Read WLD entries"
}
```


### [2026-09-06T16:16:36.399Z] TOOL RESULT

```
5-
6-
7-(Yanieek LEWb. 2 312, Geiger IA. IY 23 Horn Grd. d. iran. Phil. I'2, 55),
8:ai. knlvallkrta- “kahl gemacht“ (J. Schmidt Yoc. II 354       lat. calvus „kahl,
9-                                                                              >
10-                                                                                  ;
11-
12-
13-
14-haarlos“ (Gdf. ital. kalcnios aus idg. *qe leuos wegen :) osk. Knlmieis (daneben
15-osk. Kalaviis „Calvius“, pal. Calauan; s. Solmsen Stud. 136, KZ. 37, 16;
16-38, 447), wozu lat. calva „Hirn3chale, Schadel", calvaria ds., in Glossen
--
23-
24-
25-
26:felnde Herkunft des Subst. lat calva vom Adj. calvus spricht gegen Lager-
27-crantz’s KZ. 37, 181 ff. Gleichung calva = gr. xeXsfir] „Becher“ (konnte aus
28-*xalefir] assimiliert sein), idg. qjeq'ia.             —
29-                                           Nur auf dem wenig iiberzeugenden
30-                                                       -
31-
32-
33-
34-Umwege, dafi die idg. Bed. „kahl“ ihrerseits wieder aus einem Worte fur
=== leaf 395 ===
139-     Ai. gamutyd- n.,
140-                   gomuJa- n. „wollenes Ilemd", cami ..Prosopis spicigera;
141-Hulsenfrucht";
142:  lat. camisia split  „Hemd" (gall. Wort; gegen Entlehnung aus germ.
143-                                      —
144-                                      >
145-
146-
147-
148-
--
160-KZ. 40, 555         ;    anord. hams ,,Schale, Hiilse, Schlangenbalg" *hamisa- dem         (
161-                                                                                                       ,
162-
163:gall,   camisia niichststehendj                 ;   eher hierher als zu qem- „w61ben‘" <s. d.      :       auch
164-
165-                                                                         kem(a x )-                                                                      387
166-
167-got. Minins, anord. himinn (dat. hifne                                           mit -in- aus -inn-, vgl :) ags. heofon             .
168-                                                                                                                                                           ,
169-
```


## [2026-09-06T16:16:44.988Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nawk 'BEGIN{RS=\"\\f\"} NR==394' WLD_Bd1_pages.txt | grep -n -B4 -A10 \"Stange, Stock, Horn\\|Stirnholz\" | head -30",
 "description": "WLD kem- stick entry"
}
```


### [2026-09-06T16:16:46.904Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:16:50.096Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\ngrep -n \"Stirnholz\" WLD_Bd1_pages.txt | head; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} /Stirnholz/{print \"leaf1=\"NR}' WLD_Bd1_pages.txt",
 "description": "Find Stirnholz in WLD Bd1"
}
```


### [2026-09-06T16:16:51.894Z] TOOL RESULT

```
---
```


## [2026-09-06T16:16:55.259Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nawk 'BEGIN{RS=\"\\f\"} NR>=393 && NR<=395' WLD_Bd1_pages.txt | grep -n -i \"sami\\|kamax\\|Pfahl\\|Zapfen\\|hornlos\" | head -20",
 "description": "Search WLD for kem stick entry"
}
```


### [2026-09-06T16:16:57.682Z] TOOL RESULT

```
115:     Ai.   qamya „Stock, Zapfen, Holznagel, Stiitznagel“, av. sima {-i- scheint
118:Pferdes umfassendes Rundholz", npers. slm ds.  arm. sami-Ti PI. „zwei             ;
123:     gr.       m. „Stange, Pfahl, Schaft des Speeres“ (trotz Fick II 4 69
155:2.   kem- „hornlos“ bei sonst gehcirnten’Tierarten.
166:     Ai.   gam a-       ,.   hornlos'" (woran gambara- „eine Hirschart", eamana- „eine
167:Gazellenart"                 nur zufallig anklingen); lit. zem. smulas „hornlos“, semulis
179:slav. Ursprungs sind wegen nslov. miil, mulast        mvljav ..hornlos; bart-,    ,
195:tiber andern Yerwandten als ..hornlos'- erschiene).
202:KZ. 40, 257 Red.-Kote, 566) bleiben fern: russ. (usvv.) lcomohjj hornlos"
205:poln. gonwhf, cech. lamtohj ..hornlos " und iihnliche bait. Formen auf eine
216:Horner", engl. humble „hornlos“ (Schulze aaO.; von Falk-Torp u. hammel-
```


## [2026-09-06T16:17:37.949Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} {n=NR} /j.  kaurva-  Adj./{print \"kaurva leaf1=\"NR}' BRT.txt\nawk 'BEGIN{RS=\"\\f\"} /Halsring.,  d\\.  i\\./{print \"sima leaf1=\"NR}' BRT.txt\nawk 'BEGIN{RS=\"\\f\"} NR==250' BRT.txt | grep -o \"^[0-9]\\{3,4\\}\" | head",
 "description": "Find BRT leaves"
}
```


### [2026-09-06T16:17:39.709Z] TOOL RESULT

```
kaurva leaf1=276
sima leaf1=864
403
404
```


## [2026-09-06T16:17:45.205Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 276 864; do echo \"leaf1=$n:\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BRT.txt | grep -o \"^[0-9]\\{3,4\\}\" | head -4; done",
 "description": "Get BRT column numbers"
}
```


### [2026-09-06T16:17:47.511Z] TOOL RESULT

```
leaf1=276:
leaf1=864:
```


## [2026-09-06T16:17:50.546Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 276 864; do echo \"leaf1=$n:\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BRT.txt | grep -oE \"\\b1?[0-9]{3}\\b\" | head -6; done",
 "description": "Get BRT column numbers loosely"
}
```


### [2026-09-06T16:17:52.826Z] TOOL RESULT

```
leaf1=276:
303
187
456
135
127
leaf1=864:
700
170
242
136
105
167
```


## [2026-09-06T16:18:51.588Z] TOOL CALL #79: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T16:18:51.629Z] TOOL RESULT

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
```


## [2026-09-06T16:28:08.808Z] TOOL CALL #80: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-253.json",
 "content": "{\n \"pdf_page\": 253,\n \"book_page\": 223,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Kelewo, Kalwo\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *kelh₂u̯o- / *kal(o)u̯o- 'bald, hairless' (Pokorny IEW 554 'kelou̯o-, k(a)leu̯o- „kahl“'; Watkins/AHD 'klewo-, variant *kal(a)wo-')\",\n   \"note\": \"The root box is right. Pokorny IEW 554 heads the entry exactly 'kelou̯o-, k(a)leuo- „kahl“' and gathers precisely Nourai's material: 'Ai. áti-kūrva-, -kūlva- „ganz kahl“, av. kaurva-, npers. kal „haarlos, kahl“ … lat. calvus „kahl, haarlos“ (Gdf. ital. kalouos aus idg. *kleuos wegen:) osk. Kalūvieis … wozu lat. calva „Hirnschale, Schädel“, calvāria ds.' Watkins (AHD appendix, 1985 ed.) has the same root under both names: 'klewo-. Bald. Variant *kal(a)wo- in Latin calvus, bald: CALVARIUM. [Pok. k(e)louo- 554.]' So the two-part name 'Kelewo, Kalwo' and the language label are correct. One nuance: the attested meaning is only 'bald, bare'; the first half of Nourai's gloss, 'lacking', is not in Pokorny, Walde-Pokorny, Klein, Mann or Buck — it looks like a gloss stretched to accommodate the Sogdian branch (nodes 1–2), which is the one weak arrow on this chart. Pokorny himself warns that this root cannot be cleanly separated from *gal-/*gel- 'kahl' (NHG kahl, OE calu > callow): 'Über die versuchte Vermittlung mit nhd. kahl unter Annahme idg. Anlautschwankung s. unter kal- „kahl“' (IEW 554) — which is why Wiktionary hesitates over Persian kal (node 4).\",\n   \"note_fa\": \"جعبهٔ ریشه درست است. پوکورنی در صفحهٔ ۵۵۴ فرهنگ ریشه‌شناختی هندواروپایی مدخل «kelou̯o-, k(a)leu̯o-» را با معنای «کچل، بی‌مو» آورده و همان‌جا سنسکریت áti-kūrva-/-kūlva-، اوستایی kaurva-، فارسی نو kal و لاتین calvus (و مشتقات آن calva و calvāria «کاسهٔ سر») را کنار هم نشانده است؛ واتکینز نیز در پیوست AHD همین ریشه را با دو نام «klewo-» و گونهٔ «*kal(a)wo-» ثبت کرده است. پس نام دوگانهٔ «Kelewo, Kalwo» و برچسب «هندواروپایی» درست است. تنها نکته آنکه معنای گواهی‌شدهٔ ریشه فقط «کچل، برهنه» است و جزء نخست معنای نورایی («lacking / کم‌داشتن») در هیچ‌یک از پوکورنی، والده‑پوکورنی، کلاین، مان و باک نیامده؛ به‌نظر می‌رسد این معنا را برای جا دادن شاخهٔ سغدی (گره‌های ۱ و ۲) افزوده باشد. افزون بر این، خود پوکورنی هشدار می‌دهد که این ریشه را نمی‌توان به‌روشنی از ریشهٔ *gal-/*gel- «کچل» (آلمانی kahl) جدا کرد؛ همین ابهام است که در گرهٔ ۴ (فارسی «کل») مشکل می‌آفریند.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/calvus\",\n    \"https://www.etymonline.com/word/Calvary\"\n   ],\n   \"ref_check\": [\n    {\n     \"ref\": \"POK:554\",\n     \"status\": \"supports\",\n     \"note\": \"POK_02.txt leaf 213 (running head 554/555), and the English dump POK_full.txt line ~49206 ('Page(s): 554'): 'kelou̯o-, k(a)leuo- „kahl“. Ai. áti-kūrva-, -kūlva- „ganz kahl“, av. kaurva-, npers. kal „haarlos, kahl“, ai. kālvālīkr̥ta- „kahl gemacht“; lat. calvus „kahl, haarlos“ (Gdf. ital. kalouos aus idg. *kleuos wegen:) osk. Kalūvieis (daneben osk. Kalaviis „Calvius“, päl. Calauan[s]), wozu lat. calva „Hirnschale, Schädel“, calvāria ds. … WP. I 447, WH. I 143 f.' — the page underwrites the root box and nodes 3, 4 and 5 word for word.\"\n    },\n    {\n     \"ref\": \"KLN:226\",\n     \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt line 6244; the page markers 226/227 stand at line 6239-6240, so the entry straddles pp.226-227 exactly as cited. 'Calvary … L. calvaria, „skull“ … L. calvaria is a derivative of calvus, „bald“, which is cogn. with the second element in OI. ati-kulvah, ati-kurvah, „utterly bare“, Avestic kaurva-, ModPers. kal, „bare“. Cp. Calvatia, calvities.'\"\n    }\n   ],\n   \"consulted\": [\n    {\n     \"src\": \"WLD\",\n     \"where\": \"Bd. I 447 (WLD_Bd1_pages.txt leaf 456)\",\n     \"stance\": \"supports\",\n     \"note\": \"'ai. kulvālīkr̥ta- „kahl gemacht“ … lat. calvus „kahl, haarlos“ (Gdf. ital. kalouos aus idg. *k(e)leuos wegen:) osk. Kalūvieis … wozu lat. calva „Hirnschale, Schädel“, calvaria ds.' This is the article Pokorny 554 abridges (he cites it as 'WP. I 447').\"\n    },\n    {\n     \"src\": \"AHD\",\n     \"where\": \"Watkins 1985, k-list (AHD_watkins1985.txt line 639, end of the kleu- run)\",\n     \"stance\": \"supports\",\n     \"note\": \"'klewo-. Bald. Variant *kal(a)wo- in Latin calvus, bald: CALVARIUM. [Pok. k(e)louo- 554.]' — same root, same two name-forms, same Pokorny page.\"\n    },\n    {\n     \"src\": \"IEC\",\n     \"where\": \"Mann s.v. kaluos (IEC.txt line 6693) and line 7411\",\n     \"stance\": \"partial\",\n     \"note\": \"'kaluos, ā „bald, bare; skull, head, hill“. WP I, 447 … Per. (ambig.) kal „bald“; Lat. calvus „bald, bare“ beside calva „skull“; Osc. cf. Kalaviis (Calvius); MIr. calb „head“ …' and 'Lat. calva „skull“; calvus „shorn, bald“; Skt. cf. áti-kūlvah, -kūrvah beside kulvah, id.; Av. (queried) kaurvo …'. Mann has the root and the Latin/Indic material, but he marks the Persian word 'ambig.' and the Avestan one 'queried'.\"\n    },\n    {\n     \"src\": \"SYN\",\n     \"where\": \"Buck §4.93 BALD (SYN.txt lines 8116 ff.)\",\n     \"stance\": \"supports\",\n     \"note\": \"The word-list gives 'Av. kaurva-', 'Skt. khalati-', 'Lat. calvus', and the discussion §7 reads 'Skt. khalati-, Av. kaurva- : Lat. calvus, above, 2'. Buck also notes under §4 that OE calu, NHG kahl are 'combined by some with Lat. calvus, etc. … on the basis of IE variant initial k/g' — the same k-/g- doubt Pokorny records.\"\n    }\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Sogdian\",\n     \"words\": \"krw`\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The Sogdian word itself is beyond doubt: Gharib, Sogdian–Persian–English Dictionary no. 4875 'krw' B — karwa — gap', with the compound no. 4877 'krw δnt'k(h) B — karw-δande, δandak — gap-toothed', both referred to 'Hen. LW 96', i.e. exactly Nourai's SLW:10.1.96 (Henning, 'Sogdian Loan-Words in New Persian', BSOS 10.1 [1939] 96). The transliteration krw` in the JSON is the standard krw' with the aleph rendered as a backtick; the gloss 'empty, lacking' is Mo'in's Persian rendering (خالی، رخنه) of Henning's 'gap'. What is NOT supported is the arrow from the root: no source connects Sogd. karw- to PIE *kal(o)wo- 'bald'. Bartholomae knows no Old Iranian *karva- beside kaurva-, Pokorny 554 and Klein 226 list no Sogdian, and Sogdian karw- would presuppose a zero-grade *kr̥H-wo- rather than the o-grade that gives Av. kaurva-. The semantic bridge 'bare, bald' → 'gap, hollow' is Nourai's own inference, and his chart note ('the link is note quite certain', a misprint for 'not') concedes it.\",\n     \"derivation_fa\": \"خودِ واژهٔ سغدی جای تردید ندارد: قریب در «فرهنگ سغدی» شمارهٔ ۴۸۷۵ صورت krw' (karwa) را با معنای «رخنه، شکاف» و شمارهٔ ۴۸۷۷ ترکیب krw-δnt'k (karw-δande) «دارای دندان مجوف» را ثبت کرده و هر دو را به هنینگ، «وام‌واژه‌های سغدی در فارسی نو»، BSOS ۱۰/۱، ص ۹۶ — همان مأخذ نورایی — ارجاع داده است. معنای «خالی، تهی» که نورایی می‌آورد همان برگردان فارسی معین است. اما پیوند این واژه با ریشهٔ هندواروپایی *kal(o)wo- «کچل» در هیچ منبعی نیامده: بارتولومه صورت ایرانی باستان *karva- در کنار kaurva- نمی‌شناسد و پوکورنی و کلاین هیچ صورت سغدی‌ای نقل نکرده‌اند. تحول معنایی «برهنه/بی‌مو» ← «رخنه، حفره» استنباط خود نورایی است و او نیز در یادداشت نمودار («این پیوند چندان قطعی نیست») به آن اذعان کرده است. پس: با احتیاط پذیرفتنی است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"SLW:10.1.96\",\n       \"status\": \"supports\",\n       \"note\": \"The article itself (BSOS 10.1, 1939) is not in the local Selected Papers scan, but its p.96 content is quoted by two independent witnesses: Gharib SOD no. 4875/4877 ('Hen. LW 96'), and Mo'in's footnote 3 to Borhan-e Qate' p.1631, which reads '… سغدی krw'-δnt (دارای دندان مجوف یا فاسد)؛ نیز krw' (خالی … رخنه), Henning, Sogdian loan words.., BSOS 10.1 … 96'. Both confirm that p.96 carries Sogd. krw' 'gap' and krw-δnt'k 'gap-toothed'.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"SOD\",\n       \"where\": \"Gharib no. 4875 and no. 4877, printed p.195 (SOD_pages.txt leaf 260)\",\n       \"stance\": \"supports\",\n       \"note\": \"'4875 krw' B | karwa | gap | BSTBL, Dhy. 66; Hen. LW 96' and '4877 krw δnt'k(h) B | karw-δande, δandak | gap-toothed | SCE 83; Sogdica. 23.19; Gersh. Sogd. Cpds. 144.1; Hen. LW 96'.\"\n      },\n      {\n       \"src\": \"HENNING\",\n       \"where\": \"'Middle Persian–Sogdian Glossaries', Selected Papers leaf 37 (HENNING_selected_papers.txt line 1130)\",\n       \"stance\": \"partial\",\n       \"note\": \"'Speaking of teeth, I should like to add to my recent remarks on Sogd. krw-δnt'k „having defective teeth“, BSOS., x, p. 96 …' — Henning confirms the Sogdian form and gloss, but says nothing about an Indo-European root for it.\"\n      },\n      {\n       \"src\": \"BRT\",\n       \"where\": \"grep 'karva', 'kaurva' in BRT.txt\",\n       \"stance\": \"silent\",\n       \"note\": \"Bartholomae has kaurva- (col. 456) and its compounds but no Avestan/Old Iranian *karva-, so there is no Old Iranian antecedent on record for the Sogdian word.\"\n      }\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"karveh «کَروه ۲»\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The Persian word is real and the reference is accurate: Borhan-e Qate' p.1631 (BQT_v3_pages.txt, pdf page 424 = 424+1207) has under کروه '… و بفتح اول و ثالث و سکون ثانی، دندان میان تهی و کاواک را گویند' ('a hollow, cavitied tooth'), with the Rudaki line quoted in the chart, 'باز چون بر گرفت دست ز روی — کروه دندان و پشت چوگان است'. Mo'in's footnote 3 to that page is verbatim Nourai's arrow: '(karve) … (سوراخ، دندان فاسد) (اسدی، ص۱۱۵) … سغدی krw'-δnt (دارای دندان مجوف یا فاسد)؛ نیز krw' (خالی … رخنه), Henning, Sogdian loan words.., BSOS 10.1 … 96'. But Henning, whose 1939 note is the sole authority for the borrowing, publicly withdrew it four years later in 'Middle Persian–Sogdian Glossaries' (BSOAS 11, 1943 = Selected Papers leaf 37): 'the word krw- still exists in modern Birjandi Persian, as kavard, kaward „toothless“, see Ivanow, JPASB., xxix, 4, p. 340. This makes it unlikely that NPers. karve had been borrowed from Sogdian.' A living East-Persian (Birjandi) form shows the word is inherited Iranian in the Persian dialect area, cognate with the Sogdian rather than taken from it — so the arrow Sogdian → Persian as drawn is rejected by its own source.\",\n     \"derivation_fa\": \"واژهٔ فارسی و ارجاع هر دو درست‌اند: در برهان قاطع، ص ۱۶۳۱، ذیل «کَروه» آمده است «و بفتح اول و ثالث و سکون ثانی، دندان میان تهی و کاواک را گویند»، با همان بیت رودکی که در نمودار نقل شده. حاشیهٔ ۳ معین بر همان صفحه دقیقاً همان چیزی است که نورایی رسم کرده: «(karve) … (سوراخ، دندان فاسد) (اسدی، ص۱۱۵) … سغدی krw'-δnt … نیز krw' (خالی، رخنه)، Henning, Sogdian loan words, BSOS 10.1, ص ۹۶». اما هنینگ که تنها مرجع این وام‌گیری است، چهار سال بعد در مقالهٔ «واژه‌نامه‌های فارسی میانه–سغدی» (BSOAS ۱۱، ۱۹۴۳) نظر خود را پس گرفت: «این واژه هنوز در فارسیِ بیرجندی به‌صورت kavard/kaward «بی‌دندان» زنده است … و همین بعید می‌کند که karve فارسی نو از سغدی وام گرفته شده باشد». بقای صورت در گویش بیرجند نشان می‌دهد واژه در حوزهٔ فارسی موروثی است و با واژهٔ سغدی هم‌ریشه است، نه وام‌گرفته از آن. بنابراین پژوهش امروزی (و خودِ مأخذ نورایی) پیکان «سغدی ← فارسی» را رد می‌کند.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"BQT:1631\",\n       \"status\": \"supports\",\n       \"note\": \"Page number exact: BQT_v3_pages.txt pdf page 424 (= printed 1631 by the +1207 offset) carries کروه with 'دندان میان تهی و کاواک' and the Rudaki verse, plus Mo'in's footnote citing Henning BSOS 10.1 p.96 — i.e. the very footnote Nourai turned into this arrow.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"HENNING\",\n       \"where\": \"Selected Papers leaf 37 (HENNING_selected_papers.txt line 1130)\",\n       \"stance\": \"contradicts\",\n       \"note\": \"'… the word krw- still exists in modern Birjandi Persian, as kavard, kaward „toothless“ … This makes it unlikely that NPers. karve had been borrowed from Sogdian.'\"\n      },\n      {\n       \"src\": \"SOD\",\n       \"where\": \"Gharib no. 4875/4877 (SOD_pages.txt leaf 260, p.195)\",\n       \"stance\": \"partial\",\n       \"note\": \"Gharib records the Sogdian words and Henning's 1939 reference, but makes no claim that the New Persian word was borrowed from Sogdian.\"\n      },\n      {\n       \"src\": \"HRN\",\n       \"where\": \"grep 'karv', 'karwe' in HRN.txt; grep in HUB.txt\",\n       \"stance\": \"silent\",\n       \"note\": \"Neither Horn's Grundriss nor Hübschmann's Persische Studien has an entry for کروه — the word is a rare Ghaznavid-era poeticism known mainly from Asadi's Loghat-e Fors.\"\n      }\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Avestan\",\n     \"words\": \"kaurva\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Avestan kaurva- 'bald, hairless' is well attested: Bartholomae, Altiranisches Wörterbuch col. 456, 'j. kaurva- Adj. „kahl, unbehaart“: aspahe [kəhrpa] … Yt. 8.21', with the possessive compounds kaurvō.gaoša- 'with bald, hairless ears', kaurvō.duma- 'with a bald tail' and kaurvō.barəša- 'with a bald neck, back' (all Yt. 8.21, describing the demon Apaoša's horse). Formally it continues PIE *kolH-u̯o-/*kl̥H-u̯o-: the o-grade before the laryngeal yields Proto-Iranian *kaur-wa- (au regularly from *o + r + laryngeal in Avestan), parallel to Vedic áti-kūrva-/-kūlva- 'utterly bare' with the zero grade. Pokorny 554 and Klein 226 both set Av. kaurva- beside Latin calvus, exactly as the chart does.\",\n     \"derivation_fa\": \"صورت اوستایی kaurva- «کچل، بی‌مو» به‌خوبی گواهی شده است: بارتولومه در «فرهنگ ایرانی باستان»، ستون ۴۵۶، می‌آورد «kaurva- صفت: کچل، بی‌مو» با شاهد یشت ۸، بند ۲۱، و نیز ترکیب‌های kaurvō.gaoša- «بی‌موگوش»، kaurvō.duma- «بی‌مودم» و kaurvō.barəša- «بی‌موگردن» که همگی وصف اسب دیو اپوش‌اند. از نظر ساخت، این واژه دنبالهٔ *kolH-u̯o- هندواروپایی است: درجهٔ o پیش از حنجری در ایرانی به *kaur-wa- می‌انجامد، در برابر درجهٔ صفرِ سنسکریت áti-kūrva-/-kūlva- «یکسره برهنه». پوکورنی (ص ۵۵۴) و کلاین (ص ۲۲۶) هر دو kaurva- اوستایی را در کنار calvus لاتین نشانده‌اند — دقیقاً همان چیزی که نمودار می‌گوید. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/calvus\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"POK:554\",\n       \"status\": \"supports\",\n       \"note\": \"IEW 554: 'Ai. áti-kūrva-, -kūlva- „ganz kahl“, av. kaurva-, npers. kal „haarlos, kahl“' — the Avestan word stands in the root article itself.\"\n      },\n      {\n       \"ref\": \"KLN:226\",\n       \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt line 6244 (pp.226-227): 'L. calvaria is a derivative of calvus, „bald“, which is cogn. with the second element in OI. ati-kulvah, ati-kurvah, „utterly bare“, Avestic kaurva-, ModPers. kal, „bare“.'\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"BRT\",\n       \"where\": \"Altiranisches Wörterbuch col. 456 (BRT.txt leaf 276, where the column numeral 456 is printed)\",\n       \"stance\": \"supports\",\n       \"note\": \"'j. kaurva- Adj. „kahl, unbehaart“ … Yt. 8. 21' with 'kaurvō.gaoša- Adj. „mit kahlen, unbehaarten Ohren“', 'kaurvō.duma- Adj. „mit kahlem, unbehaartem Schwanz“', 'kaurvō.barəša- Adj. „mit kahlem, unbehaartem Hals, Rücken“ … Yt. 8. 21'.\"\n      },\n      {\n       \"src\": \"SYN\",\n       \"where\": \"Buck §4.93 BALD (SYN.txt line 8116 and §7)\",\n       \"stance\": \"supports\",\n       \"note\": \"The BALD word-list carries 'Av. kaurva-', and the discussion §7 says 'Skt. khalati-, Av. kaurva- : Lat. calvus'.\"\n      },\n      {\n       \"src\": \"IEC\",\n       \"where\": \"Mann, IEC.txt line 7411\",\n       \"stance\": \"partial\",\n       \"note\": \"'Av. (queried) kaurvo, kaourvo' — Mann lists it but flags the reading as uncertain.\"\n      }\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Persian\",\n     \"words\": \"kal «کَل» (extra: کچل)\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"NP کَل kal 'bald' with its by-form کچل kačal is the word Nourai means, and the equation with the *kalwo- family is the standard one in every book he could have used: Pokorny 554 'npers. kal „haarlos, kahl“'; Klein 226 'Avestic kaurva-, ModPers. kal, „bare“'; Buck §4.93; Mann s.v. kaluos. Two things make the arrow as drawn only 'plausible'. (i) Route: Avestan is not the ancestor of New Persian, and the phonology does not work through it — Av./Old Ir. *kaurva- would give MP *kōr(w)- and NP *kōr, not kal; NP kal presupposes an Old Iranian *kal(a)wa- with a-vocalism, i.e. a sister form, not a descendant of kaurva-. (ii) Root: Pokorny at this very page concedes that *kelou̯o- cannot be kept apart from *gal-/*gel- 'kahl' ('Über die versuchte Vermittlung mit nhd. kahl unter Annahme idg. Anlautschwankung s. unter kal- „kahl“'), and Wiktionary accordingly derives Persian کل from '*gelH- „naked, bald“ or *kl̥H-, cognate with English callow and/or Latin calvus, Sanskrit कुल्व (kulva)'. Mann marks the Persian word 'ambig.' Mo'in's own footnote 5 to Borhan p.1665 hedges differently again, taking کل as a clipped form of کچل ('مخفف «کچل» (؟)') and comparing Tabari kal. The word, its gloss and the Persian script (کَل، کچل) are all correct; only the drawn line of descent is looser than the chart admits.\",\n     \"derivation_fa\": \"واژهٔ فارسی «کَل» (و گونهٔ آن «کچل») درست ثبت شده و برابر نهادن آن با خانوادهٔ *kalwo- در همهٔ منابعی که نورایی در دست داشته آمده است: پوکورنی ص ۵۵۴ «npers. kal „haarlos, kahl“»، کلاین ص ۲۲۶ «Avestic kaurva-, ModPers. kal»، باک §۴٫۹۳ و مان ذیل kaluos. با این همه، پیکان «اوستایی ← فارسی» دو اشکال دارد. نخست راهِ اشتقاق: اوستایی نیای فارسی نو نیست و از نظر آوایی نیز *kaurva- در فارسی میانه به *kōr و در فارسی نو به «کور» می‌انجامید نه «کل»؛ «کل» صورتی ایرانی باستان با واکهٔ a (یعنی *kalava-) را پیش‌فرض می‌گیرد، پس هم‌ریشه (خواهرْواژه) است نه بازماندهٔ kaurva-. دوم خودِ ریشه: پوکورنی در همان صفحه می‌پذیرد که *kelou̯o- را نمی‌توان از *gal-/*gel- «کچل» (آلمانی kahl، انگلیسی callow) جدا کرد، و ویکی‌واژه نیز «کل» فارسی را از *gelH- «برهنه، کچل» یا *kl̥H- می‌گیرد. مان آن را «مبهم» نشانه گذاشته و معین در حاشیهٔ ۵ برهان قاطع (ص ۱۶۶۵) آن را با علامت پرسش «مخفف کچل» دانسته و با kal مازندرانی/طبری سنجیده است. خلاصه: واژه و معنا درست است، ولی زنجیرهٔ رسم‌شده سست‌تر از آن است که نمودار می‌نماید.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%DA%A9%D9%84\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"BQT:1665\",\n       \"status\": \"partial\",\n       \"note\": \"Page exact (BQT_v3_pages.txt pdf 458 = printed 1665): 'کل، بفتح اول و سکون ثانی، کچل را گویند … شخصی که سر او زخم یا جای زخم داشته باشد و موی نداشته باشد و او را بعربی اقرع خوانند'. So Borhan gives the word, the meaning 'bald' and the equivalence with کچل that Nourai prints as the extra script. But Mo'in's footnote 5 offers a different etymology — 'مخفف «کچل» (؟)، طبری Kal' — and nowhere mentions Avestan kaurva-, so the reference supports the word, not the arrow.\"\n      },\n      {\n       \"ref\": \"POK:554\",\n       \"status\": \"supports\",\n       \"note\": \"IEW 554 lists 'npers. kal „haarlos, kahl“' directly after 'av. kaurva-' in the root article, which is precisely the pairing Nourai draws.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"HRN\",\n       \"where\": \"grep 'kal' in HRN.txt\",\n       \"stance\": \"silent\",\n       \"note\": \"Horn's Grundriss has no numbered entry for کل 'bald' (his only 'kahl' hit is unrelated), so the standard handbook of NP etymology does not treat the word.\"\n      },\n      {\n       \"src\": \"IEC\",\n       \"where\": \"Mann s.v. kaluos (IEC.txt line 6693)\",\n       \"stance\": \"partial\",\n       \"note\": \"'Per. (ambig.) kal „bald“' — Mann lists it under the root but explicitly marks it as an ambiguous witness.\"\n      },\n      {\n       \"src\": \"SYN\",\n       \"where\": \"Buck §4.93 BALD (SYN.txt lines 8116 ff.)\",\n       \"stance\": \"partial\",\n       \"note\": \"Buck files Av. kaurva- with Lat. calvus (§7) but for the modern forms notes the competing k-/g- root ('OE calu, ME calouh (NE callow), Du. kaal … OHG kalo, MHG kal, NHG kahl … Combined by some with Lat. calvus, etc. … on the basis of IE variant initial k/g'), and separately records Turkish kel 'bald' as the source of SCr. čelav and Rum. chel — a reminder that a look-alike kal/kel circulates in the region.\"\n      },\n      {\n       \"src\": \"BQT\",\n       \"where\": \"Mo'in's footnote 5, Borhan-e Qate' p.1665\",\n       \"stance\": \"contradicts\",\n       \"note\": \"'مخفف «کچل» (؟)' — Mo'in derives کل from کچل rather than from the Avestan/IE root.\"\n      }\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Latin\",\n     \"words\": \"calvus : bald ; calvaria : skull, smooth hill\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin calvus 'bald, hairless' < Proto-Italic *kal(o)wos; Pokorny 554 explicitly reconstructs the Italic base as kalouos from IE *kleuos on the evidence of Oscan Kalūvieis (beside Kalaviis 'Calvius' and Paelignian Calauan[s]). From the adjective Latin formed the substantive calva 'cranium, bald head' and its enlargement calvāria, likewise 'skull' (in glosses also 'cup'). Wiktionary gives the same Proto-Italic *kal(V)wos with Sanskrit कुल्व (kulvá) as cognate. One correction: 'smooth hill' is not a Latin sense of calvāria — the word means only 'skull'. It acquires a topographical use solely through the Vulgate's Calvariae locus for Golgotha (node 6), and the notion 'bald/smooth hill' belongs to the English/toponymic afterlife, not to Latin.\",\n     \"derivation_fa\": \"لاتین calvus «کچل، بی‌مو» از ایتالیایی آغازین *kal(o)wos است؛ پوکورنی در ص ۵۵۴ ستاکِ ایتالیایی را kalouos از *kleuos هندواروپایی بازسازی می‌کند و گواه او صورت اسکی Kalūvieis (در کنار Kalaviis «کالویوس» و پلیگنی Calauan) است. از همین صفت، لاتین اسم calva «کاسهٔ سر، سرِ بی‌مو» و گستردهٔ آن calvāria «کاسهٔ سر» را ساخته است. ویکی‌واژه نیز همان *kal(V)wos ایتالیایی آغازین را می‌آورد و kulvá سنسکریت را هم‌ریشه می‌داند. یک تصحیح: معنای «تپهٔ صاف» برای calvāria در لاتین وجود ندارد؛ این واژه تنها «کاسهٔ سر» است و کاربرد جغرافیایی‌اش تنها از راه ترجمهٔ ولگات (Calvariae locus برای جُلجُتا) پدید آمده است (رک: گرهٔ ۶).\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/calvus\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"AHD\",\n       \"status\": \"supports\",\n       \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 639): 'klewo-. Bald. Variant *kal(a)wo- in Latin calvus, bald: CALVARIUM. [Pok. k(e)louo- 554.]' The 1976 New College appendix Nourai cites is not open online, but the 1985 standalone edition is the same list.\"\n      },\n      {\n       \"ref\": \"KLN:226\",\n       \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt line 6244: 'L. calvaria is a derivative of calvus, „bald“' — with Calvatia and calvities cross-referenced on the same page.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"LAT\",\n       \"where\": \"Ernout–Meillet s.v. camisia/cama region, LAT.txt line 9017 and the calvus article\",\n       \"stance\": \"supports\",\n       \"note\": \"Ernout–Meillet carry calvus/calva/calvāria as a native Latin family; the dictionary knows no non-Italic source for them.\"\n      },\n      {\n       \"src\": \"WLD\",\n       \"where\": \"Bd. I 447 (WLD_Bd1_pages.txt leaf 456)\",\n       \"stance\": \"supports\",\n       \"note\": \"'lat. calvus „kahl, haarlos“ (Gdf. ital. kalouos aus idg. *k(e)leuos wegen:) osk. Kalūvieis … wozu lat. calva „Hirnschale, Schädel“, calvaria ds.' — and a warning against Lagercrantz's equation calva = Gk. κελέβη 'Becher'.\"\n      },\n      {\n       \"src\": \"IEC\",\n       \"where\": \"Mann s.v. kaluos (IEC.txt line 6693)\",\n       \"stance\": \"supports\",\n       \"note\": \"'Lat. calvus „bald, bare“ beside calva „skull“; Osc. cf. Kalaviis (Calvius)'.\"\n      }\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"Calvary : the hill where Jesus was crucified ; Calvin : male name\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Neither word is inherited; both are learned Latin imports built on calvus. Calvary is the Vulgate's Calvariae locus at Luke 23:33, where Jerome rendered Greek Κρανίου Τόπος 'place of the skull', itself a translation of Aramaic gulgultā (Hebrew gulgōleṯ) — Golgotha, a knoll outside Jerusalem said to be so named from its shape; English took the Latin form over in the late 14th century (Wycliffe's Bible) and it later generalised to 'a representation of the Crucifixion' and to 'an ordeal'. Klein pp.226-227 states this chain exactly, and Etymonline agrees: 'Calvary … late 14c., from Latin calvaria „skull,“ rendering Greek Kraniou topos, translating Aramaic gulgulta „place of the skull“.' Calvin is the Latin cognomen Calvinus, a diminutive-adjective of calvus, 'little bald one'; the reformer's family name was French Cauvin, which he latinised as Calvinus (Klein p.227 'Calvinism … John Calvin (1509-64)'; Etymonline s.v. Calvin: 'from Latin Calvinus, a Roman cognomen, literally „bald,“ from calvus „bald“'). The node carries no refs in the book; both words are nonetheless securely documented.\",\n     \"derivation_fa\": \"هیچ‌یک از این دو واژه موروثی نیست؛ هر دو وام‌واژه‌های کتابیِ لاتین بر پایهٔ calvus‌اند. «Calvary» همان Calvariae locus در ترجمهٔ ولگات (لوقا ۲۳:۳۳) است؛ ایرونیموس (جروم) عبارت یونانی Κρανίου Τόπος «جایگاه کاسهٔ سر» را چنین برگرداند و آن عبارت خود ترجمهٔ آرامی gulgultā (عبری gulgōleṯ) یعنی «جلجتا» است، نام تپه‌ای بیرون اورشلیم که گفته‌اند از شکلش چنین نامیده شده. انگلیسی این صورت لاتین را در اواخر سدهٔ چهاردهم (انجیل ویکلیف) گرفت. کلاین (ص ۲۲۶–۲۲۷) و اتیمانلاین همین زنجیره را می‌آورند. «Calvin» نیز لقب رومی Calvinus «کچلِ کوچک» از calvus است؛ نام خانوادگی ژان کالون در فرانسه Cauvin بود که خودش آن را به Calvinus لاتینی برگرداند. ادعای نورایی درست است، هرچند این گره در کتاب بی‌ارجاع مانده است.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/Calvary\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"None\",\n       \"status\": \"not_checked\",\n       \"note\": \"The node carries no reference in the book; it inherits KLN:226 from its Latin parent, and Klein's Calvary article (pp.226-227) does in fact cover both words.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"pp.226-227 s.v. Calvary, Calvinism (KLN_1966.txt lines 6244-6249)\",\n       \"stance\": \"supports\",\n       \"note\": \"'Calvary, the place of the crucifixion of Jesus … L. calvaria, „skull“, translation of Gk. κρανίον in the Gospels, rendering Aram. gulgulthā, „skull“ (= Heb. gulgoleth), a name given to a hill near Jerusalem (so called from its shape; see Golgotha)' and 'Calvinism, n., the religious doctrine of John Calvin (1509-64)'.\"\n      },\n      {\n       \"src\": \"SKT\",\n       \"where\": \"grep 'CALVARY' in SKT.txt\",\n       \"stance\": \"silent\",\n       \"note\": \"Skeat's Concise has no Calvary entry (it is a proper name, outside his scope).\"\n      },\n      {\n       \"src\": \"WEB\",\n       \"where\": \"Webster's New Twentieth Century, vol. 1\",\n       \"stance\": \"supports\",\n       \"note\": \"Webster's article on Calvary gives the same Vulgate route (Latin calvaria, translating Greek kranion, Aramaic Golgotha).\"\n      }\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Kem 1\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ḱem- / *ḱam- 'stick, pole, horn' (Pokorny IEW 556 '1. ḱem- oder ḱam- „Stange, Stock, Horn“')\",\n   \"note\": \"Correct, and correctly numbered: Pokorny's page 556 carries three homonymous ḱem-/kem- roots, and Nourai's 'Kem 1 : stick' is Pokorny's '1. ḱem- oder ḱam- „Stange, Stock, Horn“' — the material of which is, in order, 'Ai. śámyā „Stock, Zapfen, Holznagel, Stütznagel“, av. sīmā … „ein Teil vom Geschirr des mit Pferden bespannten Wagens“, npers. sīm ds.; arm. sami-k' Pl. „Stirnholz des Ochsenjochs“ (iran. Lw.?); gr. κάμαξ f. m. „Stange, Pfahl, Schaft des Speeres“; dän. schwed. hammel …'. In other words the whole of Nourai's chart (root, node 1 and node 2) is one Pokorny paragraph. The initial is the palatal ḱ, which is why Indo-Iranian shows ś/s (Skt. śamyā, Av. sīmā, NP sīm) while Greek shows κ (κάμαξ) — a detail Nourai's 'Kem' spelling hides but does not misstate. Watkins/AHD does not include this root at all (his kem-1 is 'hornless' = Pok. 2 ḱem- 556, kem-2 'to compress' = Pok. 1 kem- 555, kem-3 'to hum' = Pok. 2 kem- 556).\",\n   \"note_fa\": \"درست است و شماره‌گذاری آن نیز درست: در صفحهٔ ۵۵۶ پوکورنی سه ریشهٔ هم‌نگارهٔ ḱem-/kem- کنار هم آمده‌اند و «Kem 1: چوب/میله» نورایی همان «1. ḱem- یا ḱam- „میله، چوب، شاخ“» است. مادهٔ آن مدخل به‌ترتیب چنین است: «سنسکریت śámyā „چوب، میخ چوبی، گوه“؛ اوستایی sīmā … „بخشی از ساز و برگ گردونهٔ اسبی“؛ فارسی نو sīm همان؛ ارمنی sami-k „چوب پیشانی یوغ گاو“ (وام ایرانی؟)؛ یونانی κάμαξ „میله، تیرک، دستهٔ نیزه“». یعنی سراسر این نمودار (ریشه و هر دو گره) از یک بند پوکورنی برگرفته شده است. صامت آغازین، کامی (ḱ) است و به همین سبب در هندوایرانی s/š و در یونانی κ می‌بینیم؛ املای «Kem» نزد نورایی این نکته را می‌پوشاند ولی نادرست نمی‌گوید. واتکینز در پیوست AHD این ریشه را اصلاً نیاورده است.\",\n   \"sources\": [],\n   \"ref_check\": [\n    {\n     \"ref\": \"POK:556\",\n     \"status\": \"supports\",\n     \"note\": \"POK_02.txt leaf 216 (running heads 556/557), line 3290 ff.: '1. ḱem- oder ḱam- „Stange, Stock, Horn“. Ai. śámyā „Stock, Zapfen, Holznagel, Stütznagel“, av. sīmā (-i- scheint idg. ə, oder = ai. śámyā?) „ein Teil vom Geschirr des mit Pferden bespannten Wagens“, npers. sīm ds.; arm. sami-k' Pl. „Stirnholz des Ochsenjochs“ (iran. Lw.?); gr. κάμαξ f. m. „Stange, Pfahl, Schaft des Speeres“ … WP. I 385, WH. I 148, 633.' Exactly Nourai's root, gloss and both nodes.\"\n    }\n   ],\n   \"consulted\": [\n    {\n     \"src\": \"WLD\",\n     \"where\": \"Walde-Pokorny Bd. I 385 (WLD_Bd1_pages.txt leaf 394)\",\n     \"stance\": \"supports\",\n     \"note\": \"'Ai. śamyā „Stock, Zapfen, Holznagel, Stütznagel“, av. sīmā (-i- scheint …) „… des Pferdes umfassendes Rundholz“, npers. sīm ds.; arm. sami-k' Pl. „zwei …“' — the article Pokorny 556 condenses ('WP. I 385').\"\n    },\n    {\n     \"src\": \"AHD\",\n     \"where\": \"Watkins 1985, k-list (AHD_watkins1985.txt line 608)\",\n     \"stance\": \"silent\",\n     \"note\": \"Watkins lists 'kem-1. Hornless … [Pok. 2. kem- 556]', 'kem-2. To compress … [Pok. 1. kem- 555]', 'kem-3. To hum … [Pok. 2. kem- 556]' but has no entry for Pokorny's 1. ḱem- 'Stange, Stock, Horn' — no English reflex, so the root falls outside his appendix.\"\n    },\n    {\n     \"src\": \"IEC\",\n     \"where\": \"Mann, IEC.txt line 6708 (kamos, kāmos, see kam- (2))\",\n     \"stance\": \"partial\",\n     \"note\": \"Mann treats the Greek κάμαξ/κημός material under kam-, with 'WP I, 388 & 507', i.e. he splits it differently from Pokorny and does not print the Iranian branch.\"\n    }\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"simâ : yoke beam ; simôithrâ : ring beneath horse's neck\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Both words are Avestan hapax legomena from one line of the Mihr Yašt, Yt. 10.125: 'āat tē (aurvaṇtō) vīspa frā.yuxta hąm.ivamca sīmąmca simōiθrąmca …' — 'and the (steeds) are all harnessed to the pole, the sīmā- and the simōiθra-'. Bartholomae, AiW s.v., glosses sīmā- as 'Halsring, d. i. ein vom Joch ausgehendes, den Hals des Pferdes umfassendes Rundholz'; Geldner (KZ 25, 530 n.200) glossed it 'Jochbalken', and it is Geldner's gloss that Horn no. 764 and Pokorny 556 pass on, and that Nourai prints ('yoke beam'). Gershevitch, The Avestan Hymn to Mithra, p.274 (commentary on 125b–c), settles the pair: sīmā- is the 'yoke-pin', matching Ved. śamyā 'pin of a yoke' and Arm. sami-k' 'the curved pieces of wood joined to the yoke that are placed round the ox's neck'; simōiθra- is analysed as sīmā + -it- (reduced grade of yat- 'join') + -ra- and identified with Arm. sameti-k', 'the strap which passing underneath the neck of the animal connects the two yoke-pegs' — 'what closes the „ring“ beneath the horse's neck appears to be the simaiθra-'. So Nourai's split of the two glosses (beam vs. ring beneath the neck) is exactly Gershevitch's conclusion; only the -ai-/-ôi- of the second form varies between editors (Av. simōiθrā- ~ simaiθra-).\",\n     \"derivation_fa\": \"هر دو واژه در اوستا تنها یک بار و در یک بند از مهریشت (یشت ۱۰، بند ۱۲۵) آمده‌اند: «… hąm.ivamca sīmąmca simōiθrąmca» یعنی «(اسبان تیزتک) همه به مال‌بند و sīmā و simōiθra بسته شده‌اند». بارتولومه sīmā- را «حلقهٔ گردن، یعنی چوب گِردی که از یوغ بیرون می‌آید و گردن اسب را دربر می‌گیرد» معنا کرده، ولی گلدنر آن را «تیر یوغ» گرفته و همین معنا از راه هرن (شمارهٔ ۷۶۴) و پوکورنی (ص ۵۵۶) به نورایی رسیده است. گرشویچ در «سرود اوستایی مهر»، ص ۲۷۴، کار را یکسره می‌کند: sīmā- همان «میخ/گوهِ یوغ» است، برابر śamyā ودایی و sami-k ارمنی («چوب‌های خمیدهٔ پیوسته به یوغ که گرد گردن گاو نهاده می‌شود»)، و simōiθra- را sīmā + it- (درجهٔ کاستهٔ yat- «پیوستن») + پسوند -ra- می‌داند و آن را با sameti-k ارمنی، یعنی تسمه‌ای که از زیر گردن جانور می‌گذرد و دو میخ یوغ را به هم می‌بندد، یکی می‌گیرد: «آنچه آن „حلقه“ را زیر گردن اسب می‌بندد ظاهراً simaiθra- است». پس تقسیم معناییِ نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"POK:556\",\n       \"status\": \"supports\",\n       \"note\": \"IEW 556: 'av. sīmā … „ein Teil vom Geschirr des mit Pferden bespannten Wagens“' under 1. ḱem- 'Stange, Stock, Horn'.\"\n      },\n      {\n       \"ref\": \"AHM:274\",\n       \"status\": \"supports\",\n       \"note\": \"Page exact. AHM.txt leaf 294 (1-based), whose neighbours carry the printed numbers 269 ff. so that this leaf is p.274, has the notes '125ᵃ. Gdn. already recognized that sīmā- belongs to NPers. sīm and Ved. śámyā; but in translating it by „Jochbalken“ he paid insufficient attention to the meaning of these cognates, which is „pin of a yoke“, similar to Arm. sami-k' … see Hübschmann, Arm. Gr. 483, and Pers. St. 79. … Bth.'s interpretation of sīmā- as „Halsring …“ is not satisfactory, since what closes the „ring“ beneath the horse's neck appears to be the simaiθra-' and '125ᶜ. On simaiθra- again there is no agreement. Gdn. has „horse-collar“, Bth. and Lo. „yoke“ … As simaiθra- obviously contains sīmā-, its relation to the latter is quite likely that of Arm. sameti-k' to sami-k'.'\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"BRT\",\n       \"where\": \"Altiranisches Wörterbuch s.v. sīmā- and s.v. hąm.ivā- (BRT.txt lines 26340, 29969, leaf 864)\",\n       \"stance\": \"partial\",\n       \"note\": \"'„Halsring“, d. i. ein vom Joch ausgehendes, den Hals des Pferdes umfassendes Rundholz: āat tē (näml. aurvaṇtō) vīspa frā.yuxta hąm.ivamca sīmąmca simōiθrąmca Yt. 10. 125'. Bartholomae has both words at the right place but assigns the 'neck-ring' sense to sīmā-, i.e. he swaps Nourai's two glosses.\"\n      },\n      {\n       \"src\": \"AHM\",\n       \"where\": \"Gershevitch p.274, and the summary list on the same commentary ('(1) hąm.ivā- „complex yoke“. (2) sīmā- „yoke-pin“')\",\n       \"stance\": \"supports\",\n       \"note\": \"Gershevitch's own conclusion, quoted above, is the modern one and matches Nourai's division of the glosses.\"\n      },\n      {\n       \"src\": \"HUB\",\n       \"where\": \"Hübschmann, Armenische Grammatik 483 / Persische Studien 79, as cited by Gershevitch\",\n       \"stance\": \"supports\",\n       \"note\": \"Hübschmann's Arm. sami-k' 'legni curvi uniti al giogo, che si pongono intorno al collo di bue' is the comparandum on which the 'yoke-pin' reading rests.\"\n      }\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"sîm 1 «سیم ۱»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP سیم sīm 'the beam/pin of a yoke' is the direct Iranian continuant of Old Iranian *sīmā- (Av. sīmā-), with the regular Middle→New Persian retention of the long ī and loss of the final vowel. Horn, Grundriss der neupersischen Etymologie no. 764 (pp.168-169) is the classic treatment: 'sīm „Kummet“ … aw. sīmā, vergl. simōiθra- Yt. 10, 125 (Geldner, KZ. 25, 530 Note 200); ai. śámyā „Jochbalken“ (nach Geldner; PW. hat „Zapfen, Holznagel, Keil, Stützholz (am Joch)“); arm. sami-k' „Stirnholz des Ochsenjoches“'; Horn adds, in a footnote, that he cannot picture the exact use of the sīm from Vullers' Persian gloss, 'doch scheint es unserem „Kummet“ nahe zu kommen'. Pokorny 556 repeats 'npers. sīm ds.' Borhan-e Qate' gives the concrete definition: 'سیم … چوب قلبه باشد. و آن چوبی است دراز که بر یک سر آن گاوآهن را نصب کنند و سر دیگر آن را بر یوغ بندند و زمین شیار کنند، و یوغ چوبی است که بگردن گاو نهند' — the plough-beam, one end on the share, the other lashed to the yoke. Horn's numbering '1' matters and Nourai keeps it: NP سیم 'silver' is an entirely different word, a Greek loan (ἄσημον 'unstamped metal' > MP asēm, with loss of the initial a-), as Horn states on the same page and as Mo'in's footnote in Borhan repeats after Benveniste.\",\n     \"derivation_fa\": \"«سیم» فارسی نو، به معنی چوب/میخ یوغ، دنبالهٔ مستقیم ایرانی باستان *sīmā- (اوستایی sīmā-) است؛ ای کشیده در فارسی میانه و نو نگاه داشته شده و واکهٔ پایانی افتاده است. هرن در «مبانی ریشه‌شناسی فارسی نو»، شمارهٔ ۷۶۴ (ص ۱۶۸–۱۶۹)، آن را چنین آورده: «sīm „کمند/یوغِ گردن“ … اوستایی sīmā، قس simōiθra- یشت ۱۰، ۱۲۵ (گلدنر)؛ سنسکریت śámyā „تیر یوغ“ … ارمنی sami-k „چوب پیشانی یوغ گاو“». پوکورنی نیز در ص ۵۵۶ می‌نویسد «npers. sīm همان». برهان قاطع تعریف عینی می‌دهد: «سیم … چوب قلبه باشد و آن چوبی است دراز که بر یک سر آن گاوآهن را نصب کنند و سر دیگر آن را بر یوغ بندند و زمین شیار کنند». شمارهٔ «۱» که نورایی نگاه داشته اهمیت دارد: «سیم» به معنی نقره واژهٔ دیگری است و وام یونانی (ásēmon «فلز ناسکه») از راه فارسی میانهٔ asēm با افتادن a آغازین، چنانکه هرن در همان صفحه و معین در حاشیهٔ برهان (به نقل از بنونیست) گفته‌اند. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\n       \"ref\": \"HRN:168\",\n       \"status\": \"supports\",\n       \"note\": \"Page exact. HRN.txt leaf 191 (1-based) = printed 168/169, entry '764. sīm „Kummet“. aw. sīmā, vergl. simōiθra- yt. 10, 125 (Geldner, KZ. 25, 530 Note 200); ai. śámyā „Jochbalken“ … arm. sami-k' „Stirnholz des Ochsenjoches“ (de Lagarde, No. 1938). Np. sīm „Silber“, sīmīn „silbern“ (phlv. asīm, asēm) dagegen ist bekanntlich griechisches Lehnwort.'\"\n      },\n      {\n       \"ref\": \"AHM:274\",\n       \"status\": \"supports\",\n       \"note\": \"Gershevitch p.274: 'Gdn. already recognized that sīmā- belongs to NPers. sīm and Ved. śámyā' — the Avestan→New Persian equation is stated on exactly the cited page.\"\n      },\n      {\n       \"ref\": \"BQT:1205\",\n       \"status\": \"partial\",\n       \"note\": \"The substance is in Borhan but not on the cited page. Printed p.1205 (BQT_v2_pages.txt leaf 665, whose running head reads ۱۲۰۵) carries سیاه‌بادام، سیاه‌پستان، سیاه‌پوش، سیاه‌دست، سیاه‌کار — no سیم. The سیم entry stands nine leaves later, on printed p.1214 (leaf 674): 'سیم = بفتح اول و ثانی بر وزن بقم، چوب‌هایی است که برزگران بر دو طرف چوبی که بر گردن گاو زراعت گذارند بندند - و بکسر اول بر وزن جیم، نقره را گویند', with Mo'in's footnote 'اوستا sīma … هندی باستان [śamyā] (تیر یوغ)، ارمنی sami-k (چوب یوغ گاو نر) …'. So Borhan+Mo'in fully support the arrow; Nourai's page number is off by about nine.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"BQT\",\n       \"where\": \"Borhan-e Qate' p.1214 with Mo'in's footnote (BQT_v2_pages.txt leaf 674)\",\n       \"stance\": \"supports\",\n       \"note\": \"Definition 'چوب قلبه … بر یک سر آن گاوآهن را نصب کنند و سر دیگر آن را بر یوغ بندند' and Mo'in's etymological footnote citing Avestan sīma, Skt. śamyā 'تیر یوغ' and Arm. sami-k'.\"\n      },\n      {\n       \"src\": \"HRN\",\n       \"where\": \"no. 764, pp.168-169\",\n       \"stance\": \"supports\",\n       \"note\": \"See ref_check; Horn is the source Hübschmann and Pokorny both build on.\"\n      },\n      {\n       \"src\": \"PHD\",\n       \"where\": \"grep 'sym', 'sēm', 'asēm' in PHD.txt / PHD_mackenzie.txt\",\n       \"stance\": \"silent\",\n       \"note\": \"MacKenzie's Concise Pahlavi Dictionary has asēm 'silver' but no Middle Persian word for the yoke-pin, so the MP link in the chain is not directly attested — the NP word is known only from the New Persian lexicographers and the dialects.\"\n      },\n      {\n       \"src\": \"CHEUNG\",\n       \"where\": \"grep 'sim', 'śam' in CHEUNG.txt\",\n       \"stance\": \"silent\",\n       \"note\": \"Cheung's Etymological Dictionary of the Iranian Verb covers verbs only; sīm is a noun and does not appear.\"\n      }\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Kem 2\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ḱem- 'to cover, wrap' (Pokorny IEW 556-557 '3. ḱem- „bedecken, verhüllen“')\",\n   \"note\": \"The root box is right: Pokorny 556-557 has '3. ḱem- „bedecken, verhüllen“' with Skt. śāmulyà- 'woollen shirt', Latin camisia, OHG hemidi, OE hemede, ON hamr 'skin, covering', Gothic himins 'heaven'; Klein s.v. chemise derives the whole family 'fr. I.-E. base *kem-, *kam-, „to cover“'. The chart's internal order, however, is upside down. Nourai makes Greek kamision the head of the branch and Latin camisia its child, following Jeffery's 1938 Foreign Vocabulary of the Qur'an (his VDQ is Badreh'i's Persian translation of Jeffery), who argued that καμίσιον is 'genuine Indo-European' and the ultimate source. Every source since — Pokorny 556 ('lat. camisia (spät) „Hemd“ (gall. Wort; entlehnt aus germ. *hamiþja- „Hemd“)'), Walde-Pokorny I 386, Buck §6.44 ('Gallo-Lat. camisia (> Romance forms and Ir. caimmse, Byz. καμίσιον …)'), Klein, Skeat and Wiktionary — has Latin camisia (first attested in Jerome, c. 400 CE, who calls it a soldiers' word) borrowed from Gaulish/West Germanic *hamiþi, with Byzantine Greek καμίσιον a loan FROM Latin, not its source. So nodes 1 and 2 reverse the direction of a well-established borrowing; everything downstream of camisia is sound.\",\n   \"note_fa\": \"جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۵۵۶–۵۵۷ مدخل «3. ḱem- „پوشاندن، فروپوشیدن“» را با سنسکریت śāmulyà- «پیراهن پشمی»، لاتین camisia، آلمانی علیای کهن hemidi، انگلیسی کهن hemede و گوتی himins «آسمان» آورده است؛ کلاین نیز کل این خانواده را از «ریشهٔ هندواروپایی *kem-, *kam- „پوشاندن“» می‌گیرد. اما ترتیب درونی نمودار وارونه است. نورایی یونانی kamision را سرِ شاخه و لاتین camisia را فرزند آن نهاده و در این کار پیرو جفری («واژه‌های دخیل در قرآن»، ۱۹۳۸ — همان VDQ در ترجمهٔ فارسی بدره‌ای) است که καμίσιον را «به‌راستی هندواروپایی» و سرچشمهٔ نهایی می‌دانست. ولی همهٔ منابع پس از او — پوکورنی («لاتین camisia (متأخر) „پیراهن“، واژه‌ای گُلی، وام‌گرفته از ژرمنی *hamiþja-»)، والده‑پوکورنی جلد ۱ ص ۳۸۶، باک §۶٫۴۴ («camisia گُلی‑لاتینی > صورت‌های رومانس و ایرلندی caimmse و یونانی بیزانسی καμίσιον»)، کلاین، اسکیت و ویکی‌واژه — لاتین camisia را (نخستین گواه نزد ایرونیموس، حدود سال ۴۰۰ میلادی، که آن را واژهٔ سربازان می‌خواند) وامی از گُلی/ژرمنی غربی *hamiþi می‌دانند و καμίσιον یونانی را وامی از لاتین. پس گره‌های ۱ و ۲ جهت یک وام‌گیریِ شناخته‌شده را وارونه کرده‌اند؛ باقی زنجیره از camisia به بعد درست است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/camisia\",\n    \"https://en.wiktionary.org/wiki/chemise\"\n   ],\n   \"ref_check\": [\n    {\n     \"ref\": \"POK:556\",\n     \"status\": \"partial\",\n     \"note\": \"POK_02.txt leaf 216, line 3300 ff.: '3. ḱem- „bedecken, verhüllen“. Ai. śāmulyà- n., śāmūla- n. „wollenes Hemd“ … lat. camisia (spät) „Hemd“ (gall. Wort; entlehnt aus germ. *hamiþja- „Hemd“; erst aus dem Lat. stammen wieder air. caimmse „Hemd“, acorn. cams „alba“, bret. kamps „Meßhemd“) … ags. cemes ds. ist Lw. aus camisia; ahd. hemidi n. „Hemd“, ags. hemede (*hamiþia-) … WP. I 386.' The page supports the root and the Latin word but flatly contradicts the Greek→Latin direction Nourai's citation is attached to: for Pokorny camisia is Gaulish/Germanic, and no Greek is involved.\"\n    },\n    {\n     \"ref\": \"CEL6:122\",\n     \"status\": \"not_checked\",\n     \"note\": \"S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words (Milton MA 1997), vol. 6 — refs_online.json records it as catalogue-only (HathiTrust search-only, no open text), so the page could not be read.\"\n    }\n   ],\n   \"consulted\": [\n    {\n     \"src\": \"WLD\",\n     \"where\": \"Walde-Pokorny Bd. I 386 (WLD_Bd1_pages.txt leaf 395)\",\n     \"stance\": \"partial\",\n     \"note\": \"'Ai. śāmulyà- n., śāmūla- n. „wollenes Hemd“, śamī „Prosopis spicigera; Hülsenfrucht“; lat. camisia spät „Hemd“ (gall. Wort; gegen Entlehnung aus germ. …)'. WP hesitates over the Germanic source (Pokorny 1959 later accepted it), but like Pokorny it knows no Greek antecedent.\"\n    },\n    {\n     \"src\": \"SYN\",\n     \"where\": \"Buck §6.44 SHIRT (SYN.txt line 10513 ff.)\",\n     \"stance\": \"contradicts\",\n     \"note\": \"'1. Derivs. of IE *ḱem- seen also in words for „covering“, „sky“, etc. But the Gallo-Lat. form prob. fr. Gmc. Walde-P. 1.386 f., Walde-H. 1.147 f. OE hemethe, OHG hemidi, MHG hemde, NHG, Du. hemd; Gallo-Lat. camisia (> Romance forms and Ir. caimmse, Byz. καμίσιον, NG ἀπο-κάμισο; Fr. > NE chemise …); Skt. śāmulya-.' Buck explicitly lists Byzantine Greek καμίσιον among the DESCENDANTS of Gallo-Latin camisia.\"\n    },\n    {\n     \"src\": \"AHD\",\n     \"where\": \"Watkins 1985, k-list (AHD_watkins1985.txt line 608)\",\n     \"stance\": \"silent\",\n     \"note\": \"Watkins's appendix has no *ḱem- 'to cover' entry (his three kem- roots are 'hornless', 'to compress' and 'to hum'), so the AHD IE appendix does not cover this root; Nourai's AHD:230/193 citations further down are main-dictionary pages, not appendix pages.\"\n    },\n    {\n     \"src\": \"KLN\",\n     \"where\": \"p.372 s.v. chemise (KLN_1966.txt line 7332)\",\n     \"stance\": \"supports\",\n     \"note\": \"'chemise … fr. Late L. camisa, camisia (whence also It. camicia, Sp. camisa, OProveng. camiza), borrowed from Teutonic through the medium of Gaulish. Cp. OHG. hemidi … fr. Teut. *hamiþia, fr. base *hama(n)-, „covering, cover“, fr. I.-E. base *kem-, *kam-, „to cover“.' Klein confirms the root and the Germanic-via-Gaulish route.\"\n    }\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Greek\",\n     \"words\": \"kamision\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The word exists but not as a direct Indo-European descendant. Byzantine Greek καμίσιον 'shirt, tunic' is first attested in the late Roman/early Byzantine period and is universally taken today as a loan from Latin camisium/camisia, with the productive Greek diminutive suffix -ιον attached to the Latin stem; Modern Greek still has ἀποκάμισο. Buck §6.44 lists it among the descendants: 'Gallo-Lat. camisia (> Romance forms and Ir. caimmse, Byz. καμίσιον, NG ἀπο-κάμισο)', and Wiktionary's Latin camisia article likewise puts 'Byzantine Greek: καμίσιον (kamísion)' under Descendants. Nourai's arrow follows Jeffery, Foreign Vocabulary of the Qur'an p.243 (= his VDQ:352), who wrote 'the underlying word is doubtless the Gk. καμίσιον. This καμίσιον has been taken as a borrowing from Semitic, but, as Boisacq, 403, shows … it is genuine Indo-European.' Jeffery was arguing only against a Semitic source; his positive claim that Greek is the fountainhead has not survived, because Latin camisia is attested a good deal earlier (Jerome, Epist. 64.11, c. 400) and is transparently the Gaulish/Germanic word.\",\n     \"derivation_fa\": \"این واژه هست، اما بازماندهٔ مستقیم هندواروپایی نیست. καμίσιον در یونانی بیزانسی به معنی «پیراهن، جامهٔ زیرین» از دورهٔ رومی متأخر گواهی شده و امروزه همگان آن را وامی از لاتین camisium/camisia می‌دانند که پسوند تصغیر یونانی -ιον بر ستاک لاتین افزوده شده است؛ در یونانی امروز نیز ἀποκάμισο بازمانده است. باک در §۶٫۴۴ آن را در شمار بازماندگان می‌آورد: «camisia گُلی‑لاتینی > صورت‌های رومانس، ایرلندی caimmse، یونانی بیزانسی καμίσιον»؛ ویکی‌واژه نیز καμίσιον را ذیل «بازماندگان» مدخل لاتین camisia نشانده است. پیکان نورایی از جفری («واژه‌های دخیل در قرآن»، ص ۲۴۳ = همان VDQ:352) گرفته شده که نوشته بود «واژهٔ زیرین بی‌گمان καμίσιον یونانی است … و چنانکه بواساک نشان داده، به‌راستی هندواروپایی است». اما جفری تنها در برابر خاستگاه سامی استدلال می‌کرد؛ ادعای مثبت او دوام نیاورده است، چون camisia لاتین بسیار زودتر (ایرونیموس، نامهٔ ۶۴٫۱۱، حدود ۴۰۰ م.) گواهی شده و آشکارا همان واژهٔ گُلی/ژرمنی است. پژوهش امروزی این گره را رد می‌کند.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/camisia\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"VDQ:352\",\n       \"status\": \"supports\",\n       \"note\": \"VDQ is Badreh'i's Persian translation of Jeffery; the original passage is FVQ p.243 (FVQ_pages.txt leaf 261, index entry 'camisia 243'): 'It is clear that it cannot have an Arabic derivation, and the underlying word is doubtless the Gk. καμίσιον. This καμίσιον has been taken as a borrowing from Semitic, but, as Boisacq, 403, shows … it is genuine Indo-European.' The cited reference does say what Nourai's arrow says — but Jeffery's view is the one modern scholarship has abandoned.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"SYN\",\n       \"where\": \"Buck §6.44 SHIRT (SYN.txt line 10513 ff.)\",\n       \"stance\": \"contradicts\",\n       \"note\": \"'Gallo-Lat. camisia (> Romance forms and Ir. caimmse, Byz. καμίσιον, NG ἀπο-κάμισο …)' — Greek is a descendant, not the source.\"\n      },\n      {\n       \"src\": \"POK\",\n       \"where\": \"IEW 556-557 s.v. 3. ḱem- (POK_02.txt leaf 216)\",\n       \"stance\": \"contradicts\",\n       \"note\": \"Pokorny's article on the root lists no Greek word at all; the shirt-words are Indic, Italic, Celtic and Germanic.\"\n      },\n      {\n       \"src\": \"KLN\",\n       \"where\": \"s.v. chemise (KLN_1966.txt line 7332)\",\n       \"stance\": \"contradicts\",\n       \"note\": \"Klein derives Late Latin camisia from Teutonic via Gaulish and mentions no Greek stage.\"\n      }\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Latin\",\n     \"words\": \"camisia\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Latin camisia 'shirt' is real and well dated — it is late, first appearing in Jerome (Epist. 64.11, c. 400 CE), who introduces it as a word of the soldiers' Latin; Ernout–Meillet (LAT.txt line 9017) call it 'chemise. Rare et tardif … Panroman', and Isidore, Orig. 19.33.39 explains 'camisias vocant, sic aptas membris et adstrictas corporibus'. What is wrong is the parent. Pokorny 556 says outright 'lat. camisia (spät) „Hemd“ (gall. Wort; entlehnt aus germ. *hamiþja- „Hemd“)'; Klein s.v. chemise says 'borrowed from Teutonic through the medium of Gaulish'; Buck §6.44 'the Gallo-Lat. form prob. fr. Gmc.'; Skeat, 'Late L. camisia … Prob. Celtic; cf. O. Irish caimmse, shirt'; Wiktionary, 'Borrowed from Proto-West Germanic *hamiþi „shirt“, ultimately from Proto-Indo-European *ḱem- „cover, clothes“ … First attested in the writings of Jerome.' So Latin got the word from a Continental Germanic *hamiþja- (whence also OHG hemidi, OE hemede, G Hemd), probably through Gaulish mouths in the Rhine army — it did not get it from Greek, and Greek got it from Latin. The root affiliation Nourai draws is right; only the intermediate step is inverted.\",\n     \"derivation_fa\": \"لاتین camisia «پیراهن» واژه‌ای واقعی و متأخر است: نخستین گواه آن نزد ایرونیموس (نامهٔ ۶۴٫۱۱، حدود ۴۰۰ م.) است که آن را واژهٔ زبان سربازان می‌خواند؛ ارنو–مِیه آن را «کمیاب و متأخر … سراسرِ رومانس» می‌نامند و ایزیدور در «ریشه‌شناسی‌ها» ۱۹٫۳۳٫۳۹ توضیح می‌دهد «camisias vocant، چنان بر اندام و تن چسبیده». آنچه نادرست است، پدر این گره است. پوکورنی (ص ۵۵۶) صریح می‌گوید «لاتین camisia (متأخر) „پیراهن“، واژه‌ای گُلی، وام‌گرفته از ژرمنی *hamiþja-»؛ کلاین می‌نویسد «وام‌گرفته از ژرمنی به میانجی گُلی»؛ باک، «صورت گُلی‑لاتینی احتمالاً از ژرمنی»؛ اسکیت، «احتمالاً کِلتی، قس ایرلندی کهن caimmse»؛ و ویکی‌واژه، «وام از ژرمنی غربی آغازین *hamiþi، سرانجام از *ḱem- هندواروپایی». پس لاتین این واژه را از ژرمنی قاره‌ای (که hemidi آلمانی علیای کهن و Hemd آلمانی امروز نیز از آن است) و به احتمال از راه گویندگان گُلی در سپاه راین گرفته است، نه از یونانی؛ و یونانی خود آن را از لاتین گرفته است. وابستگی ریشه‌ای که نورایی رسم کرده درست است؛ تنها حلقهٔ میانی وارونه شده است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/camisia\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"POK:556\",\n       \"status\": \"contradicts\",\n       \"note\": \"The cited page is the very place that gives the opposite derivation: 'lat. camisia (spät) „Hemd“ (gall. Wort; entlehnt aus germ. *hamiþja- „Hemd“; erst aus dem Lat. stammen wieder air. caimmse „Hemd“, acorn. cams „alba“, bret. kamps „Meßhemd“)' — Latin from Germanic via Gaulish, and Celtic (and, per Buck, Greek) from Latin.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"LAT\",\n       \"where\": \"Ernout–Meillet s.v. camisia (LAT.txt lines 9017-9020) and cama (line 8950)\",\n       \"stance\": \"supports\",\n       \"note\": \"'camisia, -ae (camisa) f.: chemise. Rare et tardif. En dehors des …', with Isidore Orig. 19.33.39 'camisias vocant, sic aptas membris et adstrictas corporibus … Panroman.' — the word is confirmed as a late, non-inherited Latin item.\"\n      },\n      {\n       \"src\": \"KLN\",\n       \"where\": \"s.v. chemise (KLN_1966.txt line 7332)\",\n       \"stance\": \"contradicts\",\n       \"note\": \"'fr. Late L. camisa, camisia … borrowed from Teutonic through the medium of Gaulish. Cp. OHG. hemidi … fr. Teut. *hamiþia … fr. I.-E. base *kem-, *kam-, „to cover“.'\"\n      },\n      {\n       \"src\": \"SKT\",\n       \"where\": \"s.v. Chemise (SKT.txt line 3355)\",\n       \"stance\": \"contradicts\",\n       \"note\": \"'Chemise. (F.-L.-C?) F. chemise, — Late L. camisia, a shirt, thin dress. Prob. Celtic; cf. O. Irish caimmse, shirt.' Skeat too has no Greek stage.\"\n      },\n      {\n       \"src\": \"WLD\",\n       \"where\": \"Bd. I 386 (WLD_Bd1_pages.txt leaf 395)\",\n       \"stance\": \"contradicts\",\n       \"note\": \"Same article, discussing whether camisia is borrowed from Germanic — never from Greek.\"\n      }\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Arabic\",\n     \"words\": \"qamîs\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Arabic قَمِيص qamīṣ 'shirt' is a genuine loanword and an early one: it occurs five times in the Qur'an, all in the Joseph sura (12:18, 25-28, 93), and in pre-Islamic poetry, which is why the philologists debated it (as-Suyūṭī, Muzhir I 135, quotes al-Aṣmaʿī that some held it Persian). The mainstream modern derivation is exactly the one Nourai draws: Latin camisia > Arabic qamīṣ, the Latin ending -ia being reshaped to the Arabic faʿīl pattern; Klein s.v. camise, p.228, writes 'camise, n., a light shirt. — Arab. qamīṣ, fr. Late L. camisia', and Wiktionary has 'probably from Latin camisia, from Proto-Germanic *hamiþiją' (noting, and setting aside, a minority attempt to make Ugaritic qms the source). What is not right is the immediacy: Jeffery, whom Nourai cites, expressly denies a direct Latin route — 'The Gk. καμίσιον passed into Syr. as qamīṣā and into Eth. as … which is in all probability the source of the Arabic word', with the footnote 'Vollers, ZDMG, li, 311, thinks that the Arabic came from the Lat. camisia, but this is hardly likely.' Whether the mediator was Syriac/Ethiopic or the Latin word directly, the chart's single arrow Latin → Arabic simplifies a link that the cited source itself denies.\",\n     \"derivation_fa\": \"«قَمیص» عربی وام‌واژه‌ای است اصیل و کهن: پنج بار در قرآن، همه در سورهٔ یوسف (۱۲:۱۸، ۲۵–۲۸، ۹۳)، و نیز در شعر جاهلی آمده و همین سبب گفت‌وگوی لغویان شده است (سیوطی در «المزهر» ۱/۱۳۵ از اصمعی نقل می‌کند که برخی آن را فارسی می‌دانستند). اشتقاق رایج امروزی همان است که نورایی رسم کرده: لاتین camisia ← عربی qamīṣ، با هم‌ساز شدن پایانهٔ لاتین با وزن «فَعیل» عربی؛ کلاین در ص ۲۲۸ می‌نویسد «camise: پیراهن سبک — عربی qamīṣ، از لاتین متأخر camisia»، و ویکی‌واژه نیز «احتمالاً از لاتین camisia» می‌آورد. اما بی‌واسطه بودن این راه درست نیست: جفری، که مأخذ خود نورایی است، صراحتاً راه مستقیم لاتین را رد می‌کند: «καμίσιون یونانی به سریانی qamīṣā و به حبشی … رفت، و همین به احتمال زیاد سرچشمهٔ واژهٔ عربی است»، و در پانوشت: «فولرس (ZDMG ۵۱، ۳۱۱) عربی را از لاتین camisia می‌داند، ولی این بعید است». پس پیکان یگانهٔ «لاتین ← عربی» حلقه‌ای را ساده کرده که مأخذ نورایی خودش آن را نمی‌پذیرد. با احتیاط پذیرفتنی است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%82%D9%85%D9%8A%D8%B5\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"VDQ:352\",\n       \"status\": \"partial\",\n       \"note\": \"= Jeffery FVQ p.243 (FVQ_pages.txt leaf 261): 'qamīṣ. xii, 18-28, 93. Shirt … It is clear that it cannot have an Arabic derivation, and the underlying word is doubtless the Gk. καμίσιον … The Gk. καμίσιον passed into Syr. as [qamīṣā] and into Eth. as [ḳamis], which is used in Josippon, 343, for a tunic or shirt, and is in all probability the source of the Arabic word.' Footnote 3: 'Vollers, ZDMG, li, 311, thinks that the Arabic came from the Lat. camisia, but this is hardly likely.' The reference has the word and an ultimately compatible route, but explicitly rejects Nourai's Latin → Arabic arrow.\"\n      },\n      {\n       \"ref\": \"OXF:209\",\n       \"status\": \"not_checked\",\n       \"note\": \"J. Speake, Oxford Dictionary of Foreign Words and Phrases (1997) is lending-only on archive.org (oxforddictionary00spea) and not on disk; p.209 could not be read.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"p.228 s.v. camise (KLN_1966.txt line 6282)\",\n       \"stance\": \"supports\",\n       \"note\": \"'camise, n., a light shirt. — Arab. qamīṣ, fr. Late L. camisia. See chemise.' Klein derives Arabic qamīṣ straight from Late Latin, i.e. exactly Nourai's arrow.\"\n      },\n      {\n       \"src\": \"FVQ\",\n       \"where\": \"Jeffery p.243 (FVQ_pages.txt leaf 261; index 'camisia 243')\",\n       \"stance\": \"partial\",\n       \"note\": \"See ref_check: Greek → Syriac/Ethiopic → Arabic, with an explicit note against the direct Latin route.\"\n      },\n      {\n       \"src\": \"PLA\",\n       \"where\": \"grep 'qamis', 'qamīṣ' in incoming/PLA/PLA_pages.txt\",\n       \"stance\": \"silent\",\n       \"note\": \"Asbaghi's Persische Lehnwörter im Arabischen has no entry — i.e. the modern authority on Persian loans in Arabic does not accept al-Aṣmaʿī's report that qamīṣ is Persian, which indirectly supports a western (Latin/Greek/Aramaic) source.\"\n      },\n      {\n       \"src\": \"LKT\",\n       \"where\": \"grep 'qamis', 'kamis', 'camisia' in LKT.txt\",\n       \"stance\": \"silent\",\n       \"note\": \"Lokotsch's entries nos. 1047 kamis / kamis are Turkish 'reed' (kamış), not the shirt-word; he has no article for qamīṣ.\"\n      }\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Persian\",\n     \"words\": \"qamîs «قمیص» (extra: قمیصه)\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian قمیص qamīṣ 'shirt' is a straightforward Arabic loan of the literary register, taken over with its Arabic spelling (ص) and its Qur'anic associations — the Joseph story is where the word is at home in Persian too. Mo'in's Farhang tags it accordingly: 'قمیص (قَ مِ) [ ع . ] (اِ.) پیراهن' — '[Arabic] (noun) shirt'. The extra form قمیصه that Nourai prints is the Arabic feminine/unit noun qamīṣa, likewise borrowed. Wiktionary lists 'Persian: قَمِیص (qamīs)' among the descendants of Arabic قميص. Nourai's gloss 'cotton shirt' is narrower than the Persian usage (the word simply means 'shirt'), but the derivation is exactly right.\",\n     \"derivation_fa\": \"«قمیص» فارسی وامی است مستقیم و آشکار از عربی، از لایهٔ ادبی زبان، که با همان املای عربی (با «ص») و همان پیوند قرآنی — داستان یوسف — وارد فارسی شده است. معین در فرهنگ خود همین را می‌گوید: «قمیص (قَ مِ) [ ع . ] (اِ.) پیراهن». صورت افزودهٔ «قمیصه» که نورایی می‌آورد همان مؤنث/وحدتِ عربی qamīṣa است که آن هم وام‌گرفته شده. ویکی‌واژه نیز «فارسی: قَمیص» را در شمار بازماندگان «قميص» عربی آورده است. تنها نکته آنکه معنای «پیراهن پنبه‌ای» که نورایی می‌نویسد تنگ‌تر از کاربرد فارسی است؛ واژه صرفاً «پیراهن» است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://vajehyab.com/moein/%D9%82%D9%85%DB%8C%D8%B5\",\n      \"https://en.wiktionary.org/wiki/%D9%82%D9%85%D9%8A%D8%B5\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"MON:2729\",\n       \"status\": \"partial\",\n       \"note\": \"The entry is confirmed in Mo'in's Farhang-e Farsi via vajehyab (which reproduces the lexicon volumes without pagination): 'قمیص (قَ مِ) [ ع . ] (اِ.) پیراهن' — the Arabic origin tag [ع.] is exactly Nourai's arrow. The local MON OCR (MON_part1/part2) is too poor to carry page numbers, so the printed page 2729 itself could not be confirmed.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"MON\",\n       \"where\": \"Mo'in, Farhang-e Farsi s.v. قمیص (vajehyab)\",\n       \"stance\": \"supports\",\n       \"note\": \"'[ ع . ] (اِ.) پیراهن' — Arabic loan, 'shirt'.\"\n      },\n      {\n       \"src\": \"ARY\",\n       \"where\": \"grep 'قمیص' in incoming/ARY/ARY_pages.txt\",\n       \"stance\": \"silent\",\n       \"note\": \"Aryanpur's dictionary of Indo-European roots in Persian has no entry for قمیص — as expected, since he covers inherited Persian vocabulary, not Arabic loans.\"\n      },\n      {\n       \"src\": \"KLN\",\n       \"where\": \"p.228 s.v. camise\",\n       \"stance\": \"supports\",\n       \"note\": \"Klein confirms the Arabic word from which the Persian is taken: 'Arab. qamīṣ, fr. Late L. camisia'.\"\n      }\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"kameez\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"English kameez (also kamees) is an Anglo-Indian word, current in Britain almost only in the collocation salwar kameez, the tunic worn with loose trousers in Pakistan and north India; it is recorded in English from the later 19th century. Wiktionary's kamees entry says 'Borrowed from Arabic قَمِيص (qamīṣ). Doublet of chemise' — literally Nourai's arrow. The concrete route, however, runs through India: Arabic qamīṣ was taken into Persian (node 4), from Persian into Urdu/Hindi as قَمِیض / क़मीज़ qamīz (with the characteristic voicing of the final sibilant), and English borrowed the Indian form — which is why the English word ends in -eez, not -ees. Wiktionary's own descendant tree for قميص shows the Hindi/Urdu qamīz feeding Bengali, Assamese, Marathi, Nepali and Punjabi, and notes that 'the word travelled across multiple language families via Persian as an intermediary'. So the node is right as to ultimate origin, loose as to route.\",\n     \"derivation_fa\": \"«kameez» انگلیسی (و گونهٔ kamees) واژه‌ای انگلیسی–هندی است که در بریتانیا تقریباً تنها در ترکیب salwar kameez به‌کار می‌رود، یعنی پیراهن بلندی که با شلوار گشاد در پاکستان و شمال هند می‌پوشند، و از اواخر سدهٔ نوزدهم در انگلیسی ثبت شده است. ویکی‌واژه ذیل kamees می‌نویسد «وام از عربی قَمیص؛ دوگانهٔ chemise» — یعنی درست همان چیزی که نورایی رسم کرده. اما راه واقعی از هند می‌گذرد: «قمیص» عربی نخست به فارسی رفت (گرهٔ ۴)، از فارسی به اردو و هندی به‌صورت قَمیض/क़मीज़ (با واک‌دار شدن سایشی پایانی) درآمد، و انگلیسی همان صورت هندی را گرفت؛ به همین سبب است که واژهٔ انگلیسی به ‎-eez‎ ختم می‌شود نه ‎-ees‎. پس گره از نظر خاستگاه نهایی درست است ولی مسیر آن ساده‌سازی شده. با احتیاط پذیرفتنی است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/kamees\",\n      \"https://en.wiktionary.org/wiki/%D9%82%D9%85%D9%8A%D8%B5\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"OXF:209\",\n       \"status\": \"not_checked\",\n       \"note\": \"Speake's Oxford Dictionary of Foreign Words and Phrases is lending-only on archive.org and not on disk; p.209 (which by alphabetical position would indeed fall in the K's) could not be read.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"p.228 s.v. camise (KLN_1966.txt line 6282)\",\n       \"stance\": \"partial\",\n       \"note\": \"Klein has the parallel English borrowing from Arabic — 'camise, n., a light shirt. — Arab. qamīṣ, fr. Late L. camisia' — but no entry for kameez (his dictionary predates its general currency).\"\n      },\n      {\n       \"src\": \"HJB\",\n       \"where\": \"Hobson-Jobson / Whitworth AID, the Anglo-Indian glossaries\",\n       \"stance\": \"silent\",\n       \"note\": \"Neither Anglo-Indian glossary carries kameez; the word became common in British English only with late-20th-century South Asian migration, well after both books.\"\n      }\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Old French\",\n     \"words\": \"chemise\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Old French chemise 'shirt, undergarment' (12th c.) is the regular Gallo-Romance outcome of Late Latin camisia: intervocalic -m- holds, the initial ca- palatalises to che- as everywhere in Northern French (cf. campus > champ, caballus > cheval), and -isia gives -ise. Wiktionary: 'From French chemise, from Old French chemise, from Late Latin camisa, camisia („shirt, undergarment, nightgown“), from Proto-West Germanic *hamiþi.' Klein s.v. chemise gives the same, adding the Italian, Spanish and Old Provençal cognates camicia, camisa, camiza. Nourai's second gloss, 'cover', is not a mistake: French chemise acquires exactly that extended sense — the wall-facing of a fortification (chemise d'un donjon), the paper wrapper of a dossier — and it is the second of these that produces node 7.\",\n     \"derivation_fa\": \"«chemise» فرانسهٔ کهن (سدهٔ دوازدهم) به معنی «پیراهن، جامهٔ زیرین» بازتاب قانونمند camisia لاتین متأخر در گالو‑رومانس است: میم میان‌واکه‌ای می‌ماند، ca- آغازین مانند همه‌جا در فرانسهٔ شمالی به che- کامی می‌شود (قس campus > champ، caballus > cheval) و ‎-isia‎ به ‎-ise‎ می‌انجامد. ویکی‌واژه: «از فرانسهٔ chemise، از فرانسهٔ کهن chemise، از لاتین متأخر camisa/camisia، از ژرمنی غربی آغازین *hamiþi». کلاین نیز همین را می‌آورد و هم‌ریشه‌های ایتالیایی camicia، اسپانیایی camisa و پروانسی کهن camiza را می‌افزاید. معنای دوم که نورایی می‌نویسد («cover / پوشش») نادرست نیست: chemise در فرانسه دقیقاً همین معنای گسترده را می‌یابد — دیوارهٔ پوششیِ برج و بارو، و پوشهٔ کاغذیِ پرونده — و همین معنای دوم است که گرهٔ ۷ را می‌سازد. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/chemise\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"AHD:230\",\n       \"status\": \"not_checked\",\n       \"note\": \"AHD New College Edition (1975/76) p.230 is a main-dictionary page (the 'che-' range, which fits alphabetically), not an appendix page; the 1976 New College text is not open online and the local AHD file is only Watkins's IE-roots appendix. The claim itself is not in doubt.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"s.v. chemise (KLN_1966.txt line 7332)\",\n       \"stance\": \"supports\",\n       \"note\": \"'chemise, n., woman's undergarment. — F., „shirt“, fr. Late L. camisa, camisia (whence also It. camicia, Sp. camisa, OProveng. camiza) …'\"\n      },\n      {\n       \"src\": \"SKT\",\n       \"where\": \"s.v. Chemise (SKT.txt line 3355)\",\n       \"stance\": \"supports\",\n       \"note\": \"'Chemise. (F.-L.-C?) F. chemise, — Late L. camisia, a shirt, thin dress.'\"\n      },\n      {\n       \"src\": \"SYN\",\n       \"where\": \"Buck §6.44 SHIRT\",\n       \"stance\": \"supports\",\n       \"note\": \"'Gallo-Lat. camisia (> Romance forms …; Fr. > NE chemise, now only for woman's undergarment, replacing smock and shift)'.\"\n      }\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"Persian\",\n     \"words\": \"šomîz «شمیز»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Persian شمیز šomiz is a modern French loan, not an Old French one: it comes from French chemise in its office sense, 'the paper or card wrapper in which the papers on one subject are kept', and entered Persian with European bureaucratic vocabulary in the late Qajar/Pahlavi period; the French [ʃ] and the final [z] are rendered ش and ز, and the French [ə] of che- is reshaped as Persian šo-. Mo'in's Farhang gives 'شمیز (شُ) [ فر . ] (اِ.) مقوا' — '[French] (noun) card, pasteboard', i.e. the card folder, and under پوشه he defines 'لفافه‌ای که نوشته‌های راجع به یک موضوع را در آن گذارند … (فر.) شمیز', which is exactly Nourai's gloss 'file folder'. The derivation is therefore right in substance; what is wrong is the label on the parent box — the source is 19th/20th-century French, not Old French, and a millennium separates the two. (Persian also has an unrelated homograph شمیز ~ شومیز 'ploughed land', which Mo'in files separately.)\",\n     \"derivation_fa\": \"«شمیز» فارسی وامی است از فرانسهٔ امروزین، نه فرانسهٔ کهن: از chemise فرانسه در معنای اداری آن، یعنی «پوشهٔ کاغذی یا مقوایی که نوشته‌های مربوط به یک موضوع را در آن می‌گذارند»، و همراه با واژگان دیوانی اروپایی در اواخر قاجار و دورهٔ پهلوی وارد فارسی شده است؛ [ʃ] فرانسه به «ش» و [z] پایانی به «ز» بدل شده و واکهٔ خنثای che- به شکل «شُ» درآمده است. معین می‌نویسد: «شمیز (شُ) [ فر . ] (اِ.) مقوا»، و ذیل «پوشه» می‌آورد «لفافه‌ای که نوشته‌های راجع به یک موضوع را در آن گذارند … (فر.) شمیز» — دقیقاً همان «file folder» نورایی. پس اصل اشتقاق درست است و تنها برچسب جعبهٔ مادر نادرست است: خاستگاه، فرانسهٔ سدهٔ نوزدهم/بیستم است نه فرانسهٔ کهن، و میان این دو هزار سال فاصله است. (فارسی هم‌نگارهٔ دیگری نیز دارد: «شمیز/شومیز» به معنی «زمین شیارکرده» که معین آن را جداگانه آورده است.)\",\n     \"sources\": [\n      \"https://vajehyab.com/moein/%D8%B4%D9%85%DB%8C%D8%B2\",\n      \"https://en.wiktionary.org/wiki/chemise\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"MON:2079\",\n       \"status\": \"partial\",\n       \"note\": \"The entry is confirmed via vajehyab's reproduction of Mo'in's lexicon: 'شمیز (شُ) [ فر . ] (اِ.) مقوا' — the [فر.] tag is Nourai's French origin. The cross-reference under پوشه in the local OCR (MON_part1.txt line 33430) reads '… لفافه‌ای که نوشته‌های راجع به یک موضوع را در آن گذارند (فر.) شمیز', giving the exact 'file folder' sense. Mo'in's printed page 2079 itself could not be verified: the online edition has no pagination and the local MON OCR carries no page markers.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"MON\",\n       \"where\": \"Mo'in s.v. شمیز and s.v. پوشه (vajehyab; MON_part1.txt line 33430)\",\n       \"stance\": \"supports\",\n       \"note\": \"'[ فر . ] (اِ.) مقوا' and, under پوشه, '(فر.) شمیز' for the dossier wrapper.\"\n      },\n      {\n       \"src\": \"BQT\",\n       \"where\": \"grep 'شمیز' in BQT_v1/v2/v3 pages files\",\n       \"stance\": \"silent\",\n       \"note\": \"Borhan-e Qate' (1652 CE) naturally has nothing: the word entered Persian some 250 years after the dictionary was written.\"\n      },\n      {\n       \"src\": \"ARY\",\n       \"where\": \"grep 'شمیز' in incoming/ARY/ARY_pages.txt\",\n       \"stance\": \"silent\",\n       \"note\": \"Aryanpur has no entry — a modern European loan falls outside his Indo-European-roots dictionary.\"\n      }\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"English\",\n     \"words\": \"camisa, chemise, chemisette\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Two of the three are exactly as drawn. English chemise came in through Old French/French in the 14th c. and was re-borrowed in its modern 'woman's undergarment' sense in the 19th; chemisette is French chemisette, the diminutive of chemise, 'a little shirt', borrowed in the early 19th c. (Klein: 'chemisette, n., a kind of bodice worn by women. — F., lit. „a little shirt“, dimin. of chemise'). The third word does not come through French: English camisa 'a loose shirt or chemise', an Americanism of the Southwest, is taken from Spanish and Portuguese camisa, which continue Late Latin camisia directly (Spanish did not palatalise ca-). English also has camise 'a light shirt', which Klein p.228 derives from Arabic qamīṣ — i.e. from node 3's branch, not node 6's. So the node's third item is attached to the wrong parent, though it belongs to the same root.\",\n     \"derivation_fa\": \"دو واژه از سه واژه دقیقاً همان‌اند که رسم شده: «chemise» انگلیسی در سدهٔ چهاردهم از فرانسهٔ کهن آمد و در سدهٔ نوزدهم در معنای «جامهٔ زیرین زنانه» دوباره وام گرفته شد؛ «chemisette» نیز همان chemisette فرانسه، مصغّر chemise، است که در اوایل سدهٔ نوزدهم وارد شد (کلاین: «chemisette: نوعی نیم‌تنهٔ زنانه — فرانسه، لفظاً „پیراهن کوچک“، مصغّر chemise»). اما واژهٔ سوم از راه فرانسه نیامده است: «camisa» انگلیسی («پیراهن گشاد»)، که واژه‌ای آمریکایی و ویژهٔ جنوب باختری ایالات متحده است، از اسپانیایی و پرتغالی camisa گرفته شده که خود مستقیماً دنبالهٔ camisia لاتین متأخرند (در اسپانیایی ca- کامی نشده است). انگلیسی «camise» را نیز دارد که کلاین در ص ۲۲۸ آن را از qamīṣ عربی می‌گیرد، یعنی از شاخهٔ گرهٔ ۳ نه گرهٔ ۶. پس واژهٔ سوم به مادرِ نادرست بسته شده، هرچند از همان ریشه است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/chemise\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"AHD:193\",\n       \"status\": \"not_checked\",\n       \"note\": \"AHD New College Edition p.193 is a main-dictionary page in the 'cam-' range (which is where camisa, camise, camisole stand) — alphabetically consistent with Nourai's citation — but the 1976 New College text is not open online and the local AHD file is only Watkins's IE-roots appendix, so it could not be read.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"p.228 s.v. camisado, camise, camisole and s.v. chemise/chemisette (KLN_1966.txt lines 6282, 7332)\",\n       \"stance\": \"partial\",\n       \"note\": \"'camise, n., a light shirt. — Arab. qamīṣ, fr. Late L. camisia. See chemise.'; 'camisole, n., a woman's loose jacket. — F., fr. OProveng. camisola, „mantle“, dimin. of camisa, fr. Late L. camisia.'; 'chemisette, n. … F., lit. „a little shirt“, dimin. of chemise.' Klein supports chemise and chemisette from French but routes the cam- words through Arabic or Provençal/Spanish, not through Old French.\"\n      },\n      {\n       \"src\": \"SKT\",\n       \"where\": \"s.v. Chemise (SKT.txt line 3355)\",\n       \"stance\": \"supports\",\n       \"note\": \"Skeat gives the French route for chemise; he has no camisa.\"\n      },\n      {\n       \"src\": \"FSD\",\n       \"where\": \"grep '^camisa', '^camise' in FSD_vol1.txt\",\n       \"stance\": \"silent\",\n       \"note\": \"The Funk & Wagnalls OCR did not yield the headwords (the scan of the cam- range is poor), so the American dictionary tradition could not be checked here; the Spanish source of camisa is nevertheless standard (AHD s.v. camisa: 'Spanish and Portuguese, from Late Latin camisia').\"\n      }\n     ]\n    }\n   ]\n  }\n ]\n}\n"
}
```


### [2026-09-06T16:28:08.845Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-253.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T16:28:13.440Z] TOOL CALL #81: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-253.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 253",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-06T16:28:16.677Z] TOOL RESULT

```
JSON OK
nodes verified: 16/16
node verdicts: {'plausible': 6, 'disputed': 3, 'confirmed': 7}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 12, 'partial': 5, 'not_checked': 5, 'contradicts': 1}
books consulted: {'supports': 21, 'partial': 9, 'silent': 13, 'contradicts': 8} | by book: {'KLN': 8, 'SYN': 4, 'SKT': 4, 'BRT': 3, 'HRN': 3, 'IEC': 3, 'BQT': 3, 'SOD': 2, 'HENNING': 2, 'LAT': 2, 'WLD': 2, 'MON': 2, 'ARY': 2, 'WEB': 1, 'AHM': 1, 'HUB': 1, 'PHD': 1, 'CHEUNG': 1, 'POK': 1, 'FVQ': 1, 'PLA': 1, 'LKT': 1, 'HJB': 1, 'FSD': 1}
```


## [2026-09-06T16:28:37.434Z] AGENT

Done. Wrote `/home/sfmqrb/git/rishe/data/verification/page-253.json`; `verify_check.py 253` reports 16/16 nodes, 0 PROBLEM lines.

**PDF page 253 (book p. 223) — 3 roots, 16 nodes**
- Roots: 3 confirmed (Pokorny 554 `kelou̯o-/k(a)leu̯o- "kahl"`; IEW 556 `1. ḱem- "Stange, Stock, Horn"`; IEW 556-557 `3. ḱem- "bedecken, verhüllen"` — all three root names, labels and glosses check out).
- Nodes: 7 confirmed, 6 plausible, 3 disputed.
- Ref checks: 12 supports, 5 partial, 1 contradicts, 5 not_checked (OXF, AHD:230/193 main-dictionary pages, CEL6 — none openly available).

**Disputed**
- *Kelewo* #2 Persian `karveh` ← Sogdian: Nourai copies Mo'in's Borhan footnote (p.1631), which rests on Henning, BSOS 10.1 (1939) 96. Henning himself retracted it in BSOAS 11 (1943): Birjandi `kavard/kaward` "toothless" survives, "This makes it unlikely that NPers. karve had been borrowed from Sogdian."
- *Kem 2* #1 Greek `kamision` and #2 Latin `camisia` ← Greek: the direction is reversed. Pokorny 556, Walde-Pokorny I 386, Buck §6.44, Klein, Skeat and Wiktionary all make Latin `camisia` (first in Jerome, c. 400) a Gaulish/West-Germanic `*hamiþi` loan, with Byzantine Greek καμίσιον borrowed *from* Latin. Nourai follows Jeffery FVQ 243, whose "genuine Indo-European Greek" claim is the abandoned view.

**Notable plausibles**: Sogdian `krw'` (form confirmed by Gharib no. 4875/4877, but nothing links it to *kalwo-*; Nourai's own note concedes it); Persian `kal` (in Pokorny/Klein/Buck, but Av. `kaurva-` would give NP *kōr, and Wiktionary prefers *gelH-); Persian `šomîz` (right route, but modern French, not Old French); English node #8 (`camisa` is from Spanish/Portuguese, not via French).

**Reference-page corrections for the owner (Nourai's citations, not extraction errors)**
- `BQT:1205` for `sîm 1`: p.1205 is سیاه‌بادام…سیاه‌کار; the سیم entry (with Mo'in's Avestan `sīma` / Skt. `śamyā` / Arm. `sami-k'` footnote, which fully supports the arrow) is on p.1214.
- `BQT:1631` and `BQT:1665` verified exact; `HRN:168`, `AHM:274`, `POK:554/556`, `KLN:226` all verified exact.

**Extraction**: none. I rendered the printed page and the JSON matches it word for word, including the book's own typo "the link is note quite certain" (Nourai's misprint for "not") and the English node's "camisa, chemise, chemisette".
