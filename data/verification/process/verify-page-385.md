# Verification process log — verify-page-385


## [2026-09-07T20:42:18.299Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 385 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-385.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-385.json. Write /home/sfmqrb/git/rishe/data/verification/page-385.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 385` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:42:20.109Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T20:42:20.570Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:42:20.590Z] TOOL RESULT

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
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	```json
231	{
232	  "pdf_page": 126,
233	  "book_page": 96,
234	  "verified_by": "claude-opus-5",
235	  "verified_on": "2026-09-05",
236	  "entries": [
237	    {
238	      "entry": 0,
239	      "root": "Dheigh, Dhigha",
240	      "verdict": "confirmed",
241	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
242	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
243	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
244	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
245	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
246	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
247	      "nodes": [
248	        {
249	          "id": 6,
250	          "lang": "Avestan",
251	          "words": "pairi-daeza",
252	          "verdict": "confirmed",
253	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
254	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
255	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
256	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
257	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
258	        }
259	      ]
260	    }
261	  ]
262	}
263	```
264	
265	Rules:
266	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
267	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
268	- `words` = the transliterations of the node joined by "; " (copy from the chart).
269	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
270	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
271	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
272	- If a node lists several words, cover each word; if they differ in verdict, use the worst
273	  verdict for the node and explain per word in `derivation`.
274	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
275	  scholarship takes.
276	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
277	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
278	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
279	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-09-07T20:42:21.853Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-385.txt"
}
```


## [2026-09-07T20:42:21.860Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-385.json"
}
```


### [2026-09-07T20:42:21.876Z] TOOL RESULT

```
1	{
2	  "pdf_page": 385,
3	  "book_page": 355,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Peg",
8	        "lang": "Indo-European",
9	        "refs": "POK:792",
10	        "gloss": "breast"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Sanskrit",
17	          "refs": "AHD",
18	          "words": [
19	            {"translit": "pakša", "gloss": "breast, wing", "script": null}
20	          ],
21	          "note": null,
22	          "quote": null
23	        },
24	        {
25	          "id": 2,
26	          "parent": 1,
27	          "lang": "Hindustani",
28	          "refs": "AHD; KLN:1272",
29	          "words": [
30	            {"translit": "pankâ", "gloss": "a curtain used to fan a room", "script": null}
31	          ],
32	          "note": null,
33	          "quote": null
34	        },
35	        {
36	          "id": 3,
37	          "parent": 2,
38	          "lang": "Persian",
39	          "refs": "MON:824",
40	          "words": [
41	            {"translit": "pankeh", "gloss": "fan", "script": "پنکه"}
42	          ],
43	          "note": null,
44	          "quote": null
45	        },
46	        {
47	          "id": 4,
48	          "parent": 2,
49	          "lang": "English",
50	          "refs": "AHD:1060; KLN:1272; FWE:233",
51	          "words": [
52	            {"translit": "punka", "gloss": "curtain used for fanning a room", "script": null}
53	          ],
54	          "note": null,
55	          "quote": null
56	        },
57	        {
58	          "id": 5,
59	          "parent": 0,
60	          "lang": "Latin",
61	          "refs": "AHD",
62	          "words": [
63	            {"translit": "pectus", "gloss": "breast", "script": null}
64	          ],
65	          "note": null,
66	          "quote": null
67	        },
68	        {
69	          "id": 6,
70	          "parent": 5,
71	          "lang": "English",
72	          "refs": "AHD",
73	          "words": [
74	            {"translit": "pectoral", "gloss": null, "script": null}
75	          ],
76	          "note": null,
77	          "quote": null
78	        }
79	      ]
80	    },
81	    {
82	      "root": {
83	        "name": "Peî",
84	        "lang": "Indo-European",
85	        "refs": "POK:793",
86	        "gloss": "sap, fat"
87	      },
88	      "nodes": [
89	        {
90	          "id": 1,
91	          "parent": 0,
92	          "lang": "Avestan",
93	          "refs": "HRN:81,181",
94	          "words": [
95	            {"translit": "pitu, pithwa", "gloss": "food, fat", "script": null},
96	            {"translit": "fra-pithwa", "gloss": "fat (adjective)", "script": null, "see": ["Per 1"]},
97	            {"translit": "duš-pithwa", "gloss": "bad fat, abscess", "script": null, "see": ["Dus"]}
98	          ],
99	          "note": null,
100	          "quote": null
101	        },
102	        {
103	          "id": 2,
104	          "parent": 1,
105	          "lang": "Pahlavi",
106	          "refs": "BQT:1450",
107	          "words": [
108	            {"translit": "pîh", "gloss": "fat (noun)", "script": null},
109	            {"translit": "fra-pîh", "gloss": "fat (adjective)", "script": null}
110	          ],
111	          "note": null,
112	          "quote": null
113	        },
114	        {
115	          "id": 3,
116	          "parent": 2,
117	          "lang": "Persian",
118	          "refs": "BQT:1450; MON:844",
119	          "words": [
120	            {"translit": "pîh", "gloss": "fat (noun)", "script": "پیه"},
121	            {"translit": "farbeh", "gloss": "fat (adjective)", "script": "فربه"}
122	          ],
123	          "script_extra": "په ١",
124	          "note": null,
125	          "quote": {
126	            "text": "صد جگر پاره شد زهر سویی - تا درآمد پهی به پهلویی",
127	            "poet": "Nezâmî"
128	          }
129	        },
130	        {
131	          "id": 4,
132	          "parent": 1,
133	          "lang": "Persian",
134	          "refs": "BQT:852; MON:1523",
135	          "words": [
136	            {"translit": "došpîh", "gloss": "abscess", "script": "دُشپیه"}
137	          ],
138	          "script_extra": "دُژپیه",
139	          "note": null,
140	          "quote": null
141	        },
142	        {
143	          "id": 5,
144	          "parent": 0,
145	          "lang": "Avestan",
146	          "refs": "POK:793",
147	          "words": [
148	            {"translit": "payah", "gloss": "milk", "script": null},
149	            {"translit": "paěman", "gloss": "mother's milk", "script": null}
150	          ],
151	          "note": null,
152	          "quote": null
153	        },
154	        {
155	          "id": 6,
156	          "parent": 5,
157	          "lang": "Persian",
158	          "refs": "MON:969; BQT:449; SNS:141",
159	          "words": [
160	            {"translit": "pînŭ", "gloss": "dried whey, sour milk", "script": "پینو"},
161	            {"translit": "panîr", "gloss": "cheese", "script": "پنیر"}
162	          ],
163	          "note": null,
164	          "quote": {
165	            "text": "نیکی بگزین و بد به نادان ده - روغن بخر و جدا کن از پینو",
166	            "poet": "Nâser-Khosrow"
167	          }
168	        },
169	        {
170	          "id": 7,
171	          "parent": 5,
172	          "lang": "Avestan",
173	          "refs": "SOD:42",
174	          "words": [
175	            {"translit": "angu-paěna", "gloss": "sweet sap, honey", "script": null, "see": ["Embhi"]}
176	          ],
177	          "note": null,
178	          "quote": null
179	        },
180	        {
181	          "id": 8,
182	          "parent": 7,
183	          "lang": "Pahlavi",
184	          "refs": "BQT:174",
185	          "words": [
186	            {"translit": "angubin", "gloss": "honey", "script": null}
187	          ],
188	          "note": null,
189	          "quote": null
190	        },
191	        {
192	          "id": 9,
193	          "parent": 8,
194	          "lang": "Persian",
195	          "refs": "BQT:174",
196	          "words": [
197	            {"translit": "angabîn", "gloss": "sweet sap, honey", "script": "انگبین"}
198	          ],
199	          "script_extra": "سکنجبین ، گزانگبین",
200	          "note": null,
201	          "quote": {
202	            "text": "آن یکی گفت انگبین دارم بسی - میفروشم سخت ارزان، کو کسی ؟",
203	            "poet": "Attâr"
204	          }
205	        },
206	        {
207	          "id": 10,
208	          "parent": 0,
209	          "lang": "Sogdian",
210	          "refs": "SOD:53,109",
211	          "words": [
212	            {"translit": "`pt", "gloss": "meat", "script": null},
213	            {"translit": "`pt-xw`r", "gloss": "meat eater", "script": null},
214	            {"translit": "brpyğ", "gloss": "fat", "script": null}
215	          ],
216	          "note": null,
217	          "quote": null
218	        },
219	        {
220	          "id": 11,
221	          "parent": 0,
222	          "lang": "Germanic",
223	          "refs": "AHD",
224	          "words": [
225	            {"translit": "faitaz", "gloss": "fat", "script": null}
226	          ],
227	          "note": null,
228	          "quote": null
229	        },
230	        {
231	          "id": 12,
232	          "parent": 11,
233	          "lang": "English",
234	          "refs": null,
235	          "words": [
236	            {"translit": "fat", "gloss": null, "script": null}
237	          ],
238	          "note": null,
239	          "quote": null
240	        },
241	        {
242	          "id": 13,
243	          "parent": 0,
244	          "lang": "Latin",
245	          "refs": "AHD",
246	          "words": [
247	            {"translit": "pinus", "gloss": "a resinous tree (pine)", "script": null}
248	          ],
249	          "note": null,
250	          "quote": null
251	        },
252	        {
253	          "id": 14,
254	          "parent": 13,
255	          "lang": "English",
256	          "refs": null,
257	          "words": [
258	            {"translit": "pine", "gloss": null, "script": null}
259	          ],
260	          "note": null,
261	          "quote": null
262	        }
263	      ]
264	    }
265	  ]
266	}
267	
```


### [2026-09-07T20:42:21.879Z] TOOL RESULT

```
1	=== PDF page 385 (book page 355) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Peg : breast  (refs POK:792)
4	#1 (parent #0) [Sanskrit] refs=AHD | pakša : breast, wing
5	  #2 (parent #1) [Hindustani] refs=AHD; KLN:1272 | pankâ : a curtain used to fan a room
6	    #3 (parent #2) [Persian] refs=MON:824 | pankeh «پنکه» : fan
7	    #4 (parent #2) [English] refs=AHD:1060; KLN:1272; FWE:233 | punka : curtain used for fanning a room
8	#5 (parent #0) [Latin] refs=AHD | pectus : breast
9	  #6 (parent #5) [English] refs=AHD | pectoral
10	--- entry 1 ---
11	ROOT [Indo-European] Peî : sap, fat  (refs POK:793)
12	#1 (parent #0) [Avestan] refs=HRN:81,181 | pitu, pithwa : food, fat ; fra-pithwa : fat (adjective) ☞Per 1 ; duš-pithwa : bad fat, abscess ☞Dus
13	  #2 (parent #1) [Pahlavi] refs=BQT:1450 | pîh : fat (noun) ; fra-pîh : fat (adjective)
14	    #3 (parent #2) [Persian] refs=BQT:1450; MON:844 | pîh «پیه» : fat (noun) ; farbeh «فربه» : fat (adjective) | extra: په ١
15	  #4 (parent #1) [Persian] refs=BQT:852; MON:1523 | došpîh «دُشپیه» : abscess | extra: دُژپیه
16	#5 (parent #0) [Avestan] refs=POK:793 | payah : milk ; paěman : mother's milk
17	  #6 (parent #5) [Persian] refs=MON:969; BQT:449; SNS:141 | pînŭ «پینو» : dried whey, sour milk ; panîr «پنیر» : cheese
18	  #7 (parent #5) [Avestan] refs=SOD:42 | angu-paěna : sweet sap, honey ☞Embhi
19	    #8 (parent #7) [Pahlavi] refs=BQT:174 | angubin : honey
20	      #9 (parent #8) [Persian] refs=BQT:174 | angabîn «انگبین» : sweet sap, honey | extra: سکنجبین ، گزانگبین
21	#10 (parent #0) [Sogdian] refs=SOD:53,109 | `pt : meat ; `pt-xw`r : meat eater ; brpyğ : fat
22	#11 (parent #0) [Germanic] refs=AHD | faitaz : fat
23	  #12 (parent #11) [English] refs=None | fat
24	#13 (parent #0) [Latin] refs=AHD | pinus : a resinous tree (pine)
25	  #14 (parent #13) [English] refs=None | pine
26	
```


## [2026-09-07T20:42:27.203Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md | head -100",
 "description": "Read source matrix"
}
```


### [2026-09-07T20:42:27.249Z] TOOL RESULT

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
```


## [2026-09-07T20:42:28.627Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','FWE','MON','BQT','HRN','SOD','SNS','WLD','IEC','SYN','BRT','PHD','NYB','HUB','ARY','CHEUNG','SKT','FSD','WEB','HJB','AID','KNT']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-07T20:42:29.868Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
FWE {"title": "A. J. Bliss, A Dictionary of Foreign Words and Phrases in Current English, 1966", "edition_found": "1966 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/dictionaryoffore00blis (+8 other lending copies)", "identifier": "dictionaryoffore00blis (also dictionaryoffore0000alan, dictionaryoffore0000ajbl)", "local_file": null, "page_offset": null, "lookup_hin
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG MISSING
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
```


## [2026-09-07T20:42:37.626Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"peĝ-\\|peg̑-\\|Schulter, Brust\" POK_full.txt | head -20; echo \"=== 793\"; grep -n \"fett sein\" POK_full.txt | head -20"
}
```


### [2026-09-07T20:42:37.696Z] TOOL RESULT

```
=== 793
```


## [2026-09-07T20:42:40.099Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80; echo ---; python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','MON','BQT','HRN','SOD','SNS','BRT','PHD','NYB','HUB','IEC','SYN','WLD','SKT','FSD','LKT','HJB','AID']:\n    v=d.get(k) or {}\n    print(k,'|offset:',v.get('page_offset'),'|hint:',(v.get('lookup_hint') or '')[:200])\n\""
}
```


### [2026-09-07T20:42:41.592Z] TOOL RESULT

```
AFA.txt
AFM_alt.txt
AFM_pages.txt
AFM.pdf
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
NYB.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
ocr
pageimg
PEI.txt
PHD_mackenzie.pdf
PHD_mackenzie.txt
PHD_pages.txt
PHD.pdf
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
---
POK |offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.i
AHD |offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. |hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the 
KLN |offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume p
MON |offset: None |hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Aves
BQT |offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). |hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'http
HRN |offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered ent
SOD |offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) |hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD
SNS |offset: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image |hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) fo
BRT |offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin glos
PHD |offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A
NYB |offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
HUB |offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
IEC |offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
SYN |offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed p
WLD |offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). |hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, u
SKT |offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
FSD |offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
LKT |offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
HJB |offset: leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers
AID |offset: leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> |hint: Headword in bold at line start; grep -n '^Word'.
```


## [2026-09-07T20:42:46.025Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 447 448 449 450; do echo \"===== POK_02 leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} FNR==N+1{print}' POK_02.txt | head -60; done"
}
```


### [2026-09-07T20:42:47.546Z] TOOL RESULT

```
===== POK_02 leaf 447
===== POK_02 leaf 448
===== POK_02 leaf 449
===== POK_02 leaf 450
```


## [2026-09-07T20:42:51.197Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c POK_01.txt POK_02.txt POK_03.txt POK_full.txt; for f in POK_01 POK_02 POK_03 POK_full; do echo \"$f leaves: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f.txt)\"; done"
}
```


### [2026-09-07T20:42:52.444Z] TOOL RESULT

```
 981836 POK_01.txt
1137861 POK_02.txt
1170809 POK_03.txt
3971883 POK_full.txt
7262389 total
POK_01 leaves: 363
POK_02 leaves: 433
POK_03 leaves: 429
POK_full leaves: 1
```


## [2026-09-07T20:42:56.885Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 28 29 30 31 32; do echo \"===== POK_03 leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} FNR==N+1{print}' POK_03.txt | head -70; done"
}
```


### [2026-09-07T20:42:58.052Z] TOOL RESULT

```
===== POK_03 leaf 28
06,  308,  311,  312,  Trautmann  207  f.,  210,  217.
1.  peig-  und  peik-  , Kennzeichnen  durch  einritzen  oder  färben ;  bunt,  farbig' (daneben  Worte  für  ,stechen');  pik-ro-  ,bunt';  poiko-  ds.;  pelu-poiko- ,viele  Flecken  habend'.
A.  Ai.  pirdkte  (unbel.)  ,malt',  pirdga-,  pmgald-  , rötlich,  braun',  pinjdra- ,rötlich,  goldgelb';  gr.  TtiyyaXog  (Hes.)  , Eidechse',  ^r/yav  ,Kücken'  Hes.; lat.  pingö,  -ere,  pinxi,  pictum  , malen;  mit  der  Nadel  sticken',  pictor ,Maler' ;  abg.  peg^  ,bunt' ;  toch.  A  pik-,  pek-  ,schreiben,  malen'  {pekant- , Maler'),  B  pink-,  pai(y)k'  ,schreiben'.
B.  Ai.  pim§dti  ,haut  aus  (bes.  Fleisch),  schneidet  zurecht,  gestaltet, schmückt',  pEsah-  n.,  pe§a-  m.  , Gestalt,  Form,  Farbe',  peiald-  .YQvziQvi] lieblich;  geschickt'  (vgl.  Ttoimlog)-,  püdvga-  ,rötlich,  rotbraunS  pUa-  m. ,Dammhirsch'  usw.;  vielleicht  silpd-  ,bunt',  falls  aus  *piüd-  (Tedesco, Lang.  23,  383 ff.);
av.  paes-  ,farbig  machen,  schmücken',  paesa-  m.  paesah-  n.  Schmuck, Zierat',  apers.  ni-pistä  »niedergeschrieben',  av.  fra-pixsta-  ,verziert' ;
795
crf    TtOLy-i^og  ,bunt' ;  TTiyLQÖq  , scharf  (vom  Pfeil),  bitter,  gellend,  feindselig'
, "    eil  ==  abg.   pbstr^    ,bunt') ;    lat.   pignus,    -oris   , Pfand'    (wenn    ,festge-
tecktes'  ?) ;    g'O^-  filu-faihs  .sehr  mannigfaltig^  {^^^-  3-i.  puru-pesa-  ,mannig-
filti^')>  ^^^-  ^^'  f^^  ,bunt',  ags.  fäh,  fäg  ,bunt',  wovon   aisl.  fä  (*faihön)
färben,    schmücken',   fä  rünar    , Runen    ritzen'  (ursprüngl.    ,rot    färben^),
fäinn  ,bunt  gesprenkelt',  ags.  fägian,  ahd.  fehen  , schmücken' ;
lit.  piesti  , malen,  schreiben',  paisas,  piesas  , Rußfleck',  pie§ä  ,Ruß*, paisinas,  puisinas,  puisus  , rußig,  schmutzig',  ispaisäu  .adumbrö';  apr.  ^eisäi sie  schreiben';  aksl.  püq  phsati  , schreiben',  phstrz  (=  Ttiycgög)  ,bunt', mstrog^  , Forelle'  (auch  phs^  ,Hund'  von  der  Farbe  genannt).
WIP.  11  9  f.,  WH.  II  301  f.,  305  f.,  Trautmann  210 f.
2.  peij"- und  peik-  (halt.  peik-woWi  mit  westidg.  Guttural)  , feindselig  gesinnt', teils  in  aktiver  Feindseligkeit  oder  Heimtücke,  teils  in  passivem Widerwillen  oder  Dummheit  sich  äußernd ;  Adjektiv  poiko-,  pik-to-,
A.  Lat.  piget  ,es  verdrießt  mich,  erregt  Widerwillen',  piger,  -gra,  -grum , verdrossen,  langsam,  faul';  aisl. /ei702  n.  , Verderben',  ags.  fäcen,  3i.s.  fecan XL.  , Verrat,  Bosheit,  Betrug'  {a.gs.  fcecne  , betrügerisch,  böse'),  3i\iä.  fei hhan n.  , Arglist,  Betrug',   ags.  gefic  , Betrug',  ßcol  , arglistig,  unzuverlässig'.
B.  Ai-  pisuna- , bösgesinnt,  verräterisch,  verläumderisch',  puäcd- , Dämon' ; hierher  der  gall.  (ven.-illyr.)  VN  Pictones,  Pictävi  (:  lit.  ptktas)  ,Poitou'; wgerm.  *faihipö  in  ahd.  fehida  ,Haß,  Streit',  nhd.  Fehde,  ags.  foehp[u) f.  , Feindschaft,  Fehde' ;  ahd.  fehan  ,zeläre^  und  , hassen',  as.  äfehj
===== POK_03 leaf 29
an  , feind- lich behandeln',  vom  Adj.  ahd.  gifeh  , feindlich',  ags.  fäh,  fäg  , geächtet, verfemt'  (engl,  foe  , Feind');  dazu  auch  ahd.  feigi  ,dem  Tode  verfallen', nhd.  feige  , furchtsam'  (dial.  auch  ,dem  Tode  verfallen',  ,fast  reif,  oder ,faul'),  as.  fegi  ,des  Todes',  ags.  fäge  ,dem  Tode  nahe,  bang'  (engl./e?/),  aisl. feigr  ,dem  Tode  verfallen'  {*poikiös,  vgl.  lit.  palJcas  ,dumm');
lit.  palkas  ,dumm',  peiJciü,  peikti  , tadeln,  schmähen';  piktas  ,böse,  zornig', pykstü,  pykti  , zürne,  böse  sein' ;  lett.  peiksts  , unzuverlässiger  Mensch' ; apr.  paikemmai  1.  PL  Konj.,  aupaichit  , betrügen',  pickuls  , Teufel',  lit. pikülas  , Teufel',  lett.  -pikis,  pikuls  , Teufel'.
WP.  II  10  f.,  WH.  II  300  f.,  Trautmann  203  f.
pei-zn(i)-  ,rasch,  flink^?  Nur  kelt.  und  german.
Air.  eim  (^peimi-)  ,rasch^  flink^;    aisl.  fimr  ds.,  ord-fimi  f.  , Gewandtheit in  Worten^ ;  aber  norw.  fimra  ^umhertappen*,  mnd.  fimmelen,  ßmmeren  ds.^ engl.   dial.  ßmble  ds.;  schwed.  famla,  fumla,  ndd.  fummeln^  engl,  fumble ,umhertappen'  sind  deutlich  lautnachahmend. WP.  II  11,  Sommer  IF.  51,  247.
796  '
1.  (peis-'i)  :pis-  ^zerstampfen,  zermalmen^  (bes.  Getreide);   Nomen  actionij"
p(e)is-ter-.  ..£
Ai.  pindsti  ^zerreibt^  zerstampft^  (3.  PL  pisdnti  =  lat.  finsunt),  pi^td ,gemahlen',  n.  ^MehP,  pestar-  ^Zerreiber^  (:  lat.  pistor),  av.  pisant-  ^zer. stampfend';  gr.  TtTiaact)  ^stampfe,  schrote'  (wohl  expressives  aa),  nTiq^f^ TfCLGdvTj,  ^enthülste  Gerste',  rcriaig,  ftTiafxög  ,das  Stampfen',  ^SQLnlauazQ ^ausgepreßte  Weintrauben'  (diss.  aus  *7i£QLnTLO(xa'ca) ;  lat.  plnsö,  -ere,  pinsiö pi(n)söy  -äre  , zerstampfen,  zerstoßen'  (pis-  mit  Nasalreduktion  aus  pins-) '^pistum,  plnstim^  pijisüum]  pistor  , Bäcker',  plsö  , Mörser',  pila  ds.,  pilufj^ ,Mörserkeule'  (und  ,Wurfspieß'),  pzs^i/Zwm  ,Stampfer':  nmhv.  pistu  ,pistum'* mnd.  vUel  , Mörser',  mhd.  ,^se^  ,penis';  lit.  Iterat.  paisyti  , (Gerste)  abklo- - pfen,  den  Gerstenkörnern  die  Grannen  abschlagen',  primär  pisti  ,coire cum  femina' ;  aksl.  phsq  und  pbchajq,  pbchati  ,stoßen',  *pb§eno  ,MehP,  russ. psenö  TL.  ,enthülste  Hirse',  öech.  Iterat.  p^chovati  , stampfen'.
WP.  II  1,  WH.  II  267,  307  f.,  Trautmann  220  f.,  Schwyzer  Gr.  Gr.  1,692.
2.  peis-,  speis-  , blasen'.
Mit  s- :  lat.  splrö,  -äre  ,blasen,  wehen,  hauchen,  atmen'  (*speis-),  spiritus, -üs  ,Hauch,  Atem,  Seele,  Geist';  spiräculum  ^Luftloch';
ohne  S-:  ai.  picchörä  ,Pfeife,  Flöte';  mhd.  Visen,  visiert  ,einen  Wind streichen  lassen',  v^st  ,Furz',  ags.  fisting  ds.,  ndd.  fister  ,podex',  ndl. veest  (yaist)  ,Furz',  aisl.  flsa  ,furzen',  norw.  ftsa  ds.  und  , blasen',  nhd. fispern,  fispeln  ,zische�
===== POK_03 leaf 30
�';  baltoslav.  *plsketi  ,piept,  pfeift'  in  lit.  pyskki ,knallen',  slav.  *pü^Q,  *piscati  in  russ.  piicü,  piscdtb  , piepen,  kreischen', ksl.  pistalh  f.  , Pfeife',  aksl.  piskati  ^pfeifen'  usw. ;
mit  n-Formans:  cymr.  ^^m  (^spoi-nä)  ,Atem'.
WP.  n  11,  WH.  n  575  f.,  Trautmann  221.
peisk-,  pisk-  ,Fisch'.
Lat.  piscis  m.  ,Fisch',  pisclna  .Fischteich',  piscor,  -äri  ,fischen';  got. fisks  m.,  aisl.  fiskr,  ahd.  ags.  fish  ,Fisch'  {*piskos),  got.  fiskön,  nhd.  fischen (:  lat.  plscäri',  vgl.  mhd.  vischin  :  lat.  pis-cina);  vollstufig  air.  läse  {""peiskos), Gen.  eise  ,Fisch',  Kollekt.  ,Fische';  poln.  piskorz  ,Peißker',  russ.  piskdn ,Gründling';  beruht  die  Übereinstimmung  mit  mir.  esc  ,Wasser',  schott. FIN  Esk  (kelt.  Hskä) :  acjmr.  FIN  Uisc,  ncjmr.  Wysg  (kelt.  *eskä  aus *eiskä  oder  *eidskä)  auf  Zufall?    s.  auch  oben  S.  794
WP.  II  11,  WH.  II  310,  Max  Förster  Themse  840  f.
I.  pek-,  pek-,  pök-  etwa  ,hübsch  machen,  aufgeräumt  oder  vergnügt  sein'. Ahd.  gifehan,  ags.  gefeon  ,sich  freuen';  as.  ahd.  fehön  ,verzehren',  ahd. gi-fekön   ds.   =  ags.   ge-feon,   ahd.   gi-fehan    ,sich    erfreuen';    Kaus.    got.   1
797
f^lla-falijan  , Genüge  leisten,  befriedigen,  dienen^,  ahd.  fagön  , beistehen^;
.rot.  faheps  ^Freude^,  aisl.  fecjinn,  a.gs.  fcegen  ,iToh%  got.  ahd.  faginön,  ags.
^fceqenian  ,sich   freuen^,   aisl.  fagna   ds.,  got.   ga-fehaba  ^passend,   ehrbar^,
aisl.  fösgiligr  ^angenehm';  got.  fagrs  ^geeignet^  aisl.  fagr,  ags.  fxger c:chÖn^  usw.;  got.  ga-fahrian  ^zubereiten';  in  materieller  Bed.  mhd.  vegen reinigen,   scheuern,  fegen^,  aisl.  fäga  ,schmücken,  reinigen^,  f^gja  ,glän-
zend  machen,   putzen^  und   lit.  püosiu  (^pökeiö),  püoUi  ,schmücken',  lett.
püost  ,reinigen,  säubern,  schmücken^,  refl.  ,sich  putzen';    vielleicht  hieher
mir.  äil  , angenehm'  als  *jpökli'  (doch  s.  auch  unter  jpäk-  ,fe^tmachen'). WP.  11  16,  Wissmann  Nom.  Postverb.  14,  91,  Trautmann  229.
2,  pek-  ,Wolle  oder  Haare  rupfen,  zausen';  peku-  n.  Gen.,  peku-6s  ,das Geschorene,  Wolltier,  Schaf,  dann  ,Kleinvieh,  Vieh  überhaupt^ ; ,Wolle,  Fließ,  auch  Haar';  poko-s  ,Fließ',  pekos-  ds.;  pk-t-en- jKamm':  von  hier  aus  schon  idg.  ein  Verbalstamm  pekt-  gebildet.
Ai.  pdsu-y  pasu-  n.,  Gen.  jpasvdh]  pasü-  m.  ,Vieh'  av.  pasu-  m.  ,Vieh' (meist  noch  , Kleinvieh^),  im  Kompos.  flu-,  -fiu-^  womit  ai.  ksu-män-  ,nah- rungsreich',  puru-lcH  ds.  (zweimal  auch  einfaches  km)  als  Diss. -Formen für  psu-  identisch;  =  lat.  pecüj  -üs  n.  ,Vieh',  woneben  jpecus,  -oris  n. (formell  =  gr.  tö  Ttixog),  pecus,  -üdis  f.  ds. ;  Ableitungen  ji^ecilma  ,Geld', pecülium  ,Handgeld,  Taschengeld';  umbr.  pequo  PL  n.  ,pecua';  =  got. faihu  , Besitz,  Vermögen',  aisl.  /ö,  ags.  feoh,  sls.  fehuj  ahd.  fihu  ,Vieh';  = lit.  pekus,  apr.  pecku  ,Vieh'  (westidg.  Gutt.);  got.  bi-,  ga-faihon  , übervor- teilen' sind  nach  W.  Wissmann  (Die  ältesten  Postverbalia  79  ff.)  Denomi- nativa  von  faihu,  und 
===== POK_03 leaf 31
 hi-faih  ,Betrug'  ist  Nomen  postverbale;
arm.  asr,  Gen.  asu  , Schaf  wolle.  Fließ',  asvei  , wollig'  {^poku-\-r,  mit  a aus  0  in  offener  Anlautsilbe) ;  gr.  tt^xw  (=  lit.  pe§ü),  niv.Tü)  (=  lat.  pectö, ahd.  fehtan),  Ttsr/.rEo)  ,kämme,  schere',  rci-Aog  n.  ,Fließ,  Wolle',  Tiöxog  m.; ,Fließ',  xTfi/g,  Y.Tev6g  ,Kamm'  (aus  schwundst.  *7rx'r£v-;  lat.  pecten)-,
alb.  pile  , Werkzeug  zum  Flachskämmen,  -hecheln'  (*pekla) ;  lat.  pectö, -ere,  pexl  ,kämmen',  pecten,  -inis  ,Kamm',  umbr.  petenata  ,pectinatam'; ahd.  as.  fehtan,  ags.  feohtan  , fechten' ;  ahd.  as.  fahs,  ags.  feax  ,(Haupt)- haar',  aisl. /aa?  ,Mähne'  (*-poJc-s-o-,  vgl.  den  es-St.  ney-og),  aisl.  fcer,  aschwed. fär  ^Schaf^  {^fahaz  =  Ttöyiog),  aschwed.  fcet  (*fahti-)  ,Wolle,  Fließ',  ags. feht  ,Fließ',  ndl.  vacht  f.  , Wolle,  Schur',  ags.  fihl  ,pannus';  lit.  pesü, pesti  ,rupfen,  an  den  Haaren  zausen',   Iter.  pasyti,  susijpeUi  ,sich  raufen'.
Hierher  wohl  ai.  paks-man-  n.  ,Augenwimpern,  Haar',  paks-malä-  ,mit starken  Augenwimpern,  dichthaarig'  av.  pasna-  n.  ,Augenlid',  vgl.  in  nicht so  spezialisierter  Bed.  np.  pasm  ,Wolle'.
WP.  II  16  f.,  WH.  II  269  f.,  270  ff.,  Trautmann  217,  Specht  KZ  68,  205  ff.
798  '
pek^-  ,kochen';  Partiz.  pek^-to-  .gekocht^;  pek'i-ti-  ,das  Kochen',  peicM-^er^^ pok^o-s  ,Koch^ Ai.  pdcati,   av.  pacaiti  ,kocht,   bäckt,   brät'   (=  lat.  coquö^   cymr.  poh{ aXh.pjek,  ^hg,  pelcg,  vgl  auch  lit.  Jcepü)-,  Fut.  pähsyaii:  gT.  nsipw)]  Supi^; paktum  =  lat.    coctum^    aksl.   peUh]   Partiz.   paktd-    (=    gr.    TtsTVTÖQ,    l^t^ coctuSj    cymr.   poeth),   ai.   pdcyate   ,reift',  pakvd-   ^gekocht,   reif',  jpa/cii-  f/ ,das  Kochen,  gekochtes  Gericht'  (=  gr.  n:hptg,  lat.  cocti-ö,  abg.  pes^t,  apr. pectis)j  paktdr-  ,(ier   Kochende'   (=  lat.    coctor,   fem.   gr.  nsrtTQia),  pakd^ m.  ,das  Kochen,  Backen,  Reifen',  av.  nasu-päka-  ,Leichen  (teile)  kochend verbrennend';    arm.    wahrscheinlich    Äac   ,Brot'   als    *pok'^-ti-]   gr.    TceoGfo  " att.  TrfTTü)   ,koche,  verdaue'   {*peky:io)j    ^o-Präs.  fisTiTco]   rcexpig  f.  Kochen';     I 7teTt(j)Vj    -ovog    ,reif'    (f.   nertSLQa    nach    jx'nov  iTtiSLQo),    nörtavov    , Gebäck, Kuchen';  umgestelltes    *k^opos   in   äQto-'AOnog   (neben    dQTo-Ttonog)    ,Brot-^ bäcker';  alb.  pjek  ,ich  backe';   lat.  coquö,  -ere  ,kochen'  (ital.  kelt.  Assim.  " von   *pek]^ö    zu  *k"ek1tö),    coquus  ,Koch'  ( :  ägTO-xörtog),   coqulna    , Küche', als  osk.-umbr.  Lw.  poplna]   cymr.  pobi  (o  aus  e),   com.  pohas,   bret.  pibi ,backen',  bret.  pohet  , gebacken',  cymr.  poeth  {*k^ek^-tos)  ,heiß',  bret.  'poaz  • ,gekocht',  mcymr.  poburies   ,Bäckerin',  coru.  peber^  bret.  pober  ,Bäcker';  ' air.  cuchtar  , Küche'  aus  lat.  coctüra  ds. ;  ags.  ä-figen  ,geröstet';    lit.  (um- II gestellt)  kepü,  kepti,  lett.   cepu^   cept  , backen,   braten',   ceplis   ,Backofen'; ohne  Umstellung   apr.  pectis  , Ofenschaufel'  =  aksl.  peHh  ,Ofen,    Höhle'; lit.  pektas  ,gebraten*,  aksl.  *pekg,
===== POK_03 leaf 32
  *peHi  , backen'  in  serb.  pecem,  peci  ds.,   " usw. ;    aksl.  pek^   , Hitze',   pot^   ,Schweiß'   (*pokto-),  pestb    ,Ofen',   peStera    I ,Höhle,  Ofen'  usw.;   toch.  AB  päk-  ,zum  Reifen  bringen,  kochen',  Partiz.  ^ Pass.  B  pepakßu]  A  pukäl,  B  pikul  ,Jahr'  (=  ,Reife'). WP.  II  17  f.,  WH.  I  270  f.,  Trautmann  211  f.
I.  pel-,  pelo-,  ple-  ,gießen,  fließen,  aufschütten,  füllen,  einfüllen^;  auch ,schwimmen,  fließen  machen,  fliegen,  flattern'  und  ^schütteln,  schwin- gen, zittern  (machen)';  nominal:  pel  (Gen.  Pei-es)  und  Peii-s  ,Burg' (,aufgeschütteter  Wall');  pl-no-,  ple-no-,  ple-ro-  ,voll',  pl-no-tä ,Fülle',  pl-tö-,  ple-to-  ^gefüllt',  pJ-ti-,  ple-mn  ,das  Füllen';  pelu , Menge',  Pclu-  ,viel'.
A.  Arm.  heium  ,ich  gieße  aus'  (*pel-nu-mi)^  zeium  (*z-heium)  ,lasse strömen',  Pass.  ,fließe  über';
cymr.  llanw  m.  ,Flut',  Verbalnom.  llanw,  llenim  ,Füllen,  Fließen',  mbret. lanoj  lanv  Flut',  corn.  lanwes  , Fülle'  (^pkn-uo-)',
lit.  trans.  pilü,  pilti  ,gießen,  schütten,  aufschütten,  füllen',  intrans. ,fließen',  lett.  piUt  ,tröpfeln',  pile  ,Tropfen',  pilt  ,tröpfeln',  pali  ,Über- schwemmung',  lit.  afhpalas  {*ant-palas)  ,Aufwasser  auf  dem  Eise';  russ. vodo-poh{je),  pol{n)o-vodt>je  »Hochwasser',  kslov.  poh  ,Schöpfgefäß*.
799
ß,  pel  ;Burg^  in  ai.  pör,  Gen.  purds  ,Burg-^  Stadt^,  pura-  n.j  jünger puri-j  i?^^^  ^s.,  vgl.  Singapur  , Löwenstadt',  gr.  (äol.)  jiöXig  ^Burg,  Stadt, Staat^  (*pji-s),  hom.  kypr.  TtröXig  ds.,  lit.  jpüis,  lett.  pile  ,Burg,  Schloß' (s.  Schwyzer,  Gr.  Gr.  1,  325,  344,  SpecKt  KZ  59,  65  f.,  11  f.,  Trautmann 217).
C.  Wörter  für  ,SumpF  (pel-,  pel-eu-),  wie  osset.  farwe,  färer  ,Erle', :ihd. /e^(«)iüa;  nbd.  Feiher  ,  Weidenbaum'  (als  , Sumpf  bäum'),  und  lat.  pahis, -üdis  f.  , stehendes  Wasser,  Sumpf,  Pfütze'  {*p)J-ou-d-),  wohl  zu  ai.  palvald- n.  ,Teich'  und  palvalya-  ,sumpfig^;  dazu  noch  pelok-  :  pläk-  in  gr. fcdlnog '  nrjXog  Hes.,  TcaXaaao)  (*7taXa'Aicü)  , bespritze',  lit.  pelke  , Moorbruch', apr.  pelky  ds.,  lett.  pelce  ,Pfütze'  :  pläcis  ,Morast' ;  nach  W.  Schulze  Kl. Sehr.   112  alle  ursprüngl.  Farbenbezeichnungen,  also  zu  8.  pel-,
D.  , füllen,  Fülle' :  Ai.  piparti  :  pipi'mdh ;  prndti  {prndti)  , füllt,  sättigt, nährt,  spendet  reichlich,  beschenkt',  auch  ppiöti  ds.,  püryate,  püryate , füllt  sich',  Aor.  dprät  (:  nXfJTo),  Imp.  pürdhi,  Perf.  papräu  (:  Isit.  plevl), Partiz.  prätd-  (=  lat.  -pletus,  alb.  p^ot]  vgl.  auch  präti-  :  lat.  com-pleti-ö), pürtd-  ,voll',  präna-  ,voll'  (=  lat.  plenus,  s.y.  fräna-  ,Füllung',  air.  lln-aim , fülle'),  pürnd-  ,voll'  (=  got.  fulls,  litt,  pilnas,  abg.  phm,  air.  Zän;  von *pel-  hingegen  av.  pdrdna-  , gefüllt') ;  parinah  n.  , Fülle'  (:  av.  pardnah-vant- , reichlich'),  parl-man-  , Fülle,  Spende'  (*peh-)',  av.  par-  , füllen* ;
arm.  li,  Gen.  Uog  ,voll'  (aus  *ple-io-s  =  gr.  nXecog?  oder  aus  *ple-to-s ==  ai.  prätd-?),  Inum  , fülle'  (Hinum,  Neubildung),  Aor.  eli-c  ,ich  füllte'; lir  (i-St.)  , Fülle';  vermutlich  holom,  holonem  , häufe  auf,  sammle  an';
gr.  7tL(.LTcXr]HL  ,  füll
```


## [2026-09-07T20:43:04.198Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 24 25 26 27; do echo \"===== POK_03 leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} FNR==N+1{print}' POK_03.txt; done"
}
```


### [2026-09-07T20:43:05.592Z] TOOL RESULT

```
===== POK_03 leaf 24
treffend';  aus  , Fußfessel'  ist  z.  T. schon  grundsprachlich  ,Fessel  überhaupt'  geworden. 1.  Ai.  päd-  ,Fuß'   {pdt,  pädam,  paddh),   av.  päd-  ds. ;   apers.   pädaibiyä ,mit    den   Füßen';    arm.  ot-k'    „Ttödsg'',    ot-n   ,,7tovg,    noda'']    gr.  jtwg,  att. Tiovg,   Gen.  nodög  ,Fuß'   {kyLaTÖiiTradog  ,100  Fuß  lang');  lat.  pes,  p^dis  ds., umbr.  peri,  persi   ,pede'    (dupursus   ,bipedibus',  -u-  wohl   aus   -ö-);    air.  is , unterhalb'    (wovon    ise      ,niedrig')   m.   Dativ,   aus   dem   Lok.    PL   *ped-su ,zu  Füßen'  deutbar  =  alb.  posh  in  perposh  ,unten',  posh-te  ,herab,  unter- irdisch; unten,  hinunter';   got.  fötus,    aisl.   fötr,  ags.  föt  (Nom.   PI.   aisl. fetr,  ags.  fet  aus  *föt-iz)  ahd.  fuoz   ,Fuß' ;   hitt.   luv.  pata-^   Hierogl.-bitt. pat  ds.;  toch.  A  pe,  B  pai,  Dual  A  pem,  B  paine-
791
zu  ped-  ,Fuß'  gehört  gv.  dial.  rceda  „^«t«",  ursprüngl.  ,(jemandem) auf  dem  Fuße',  vg-1.  lat.  pedisequus,  -a  , Diener,  -in*  eig.  ,auf  dem  Fuße folgend'  und  unten  die  arm.  von  het  , Fußspur'   gebildeten  Präpositionen;
mit  -i-ös,  -i-t-  , gehend'  sind  gebildet:  gr.  rtet^ög  ,pedestris',  lat.  _pec?-es, -i't-is  , Fußgänger,  Fußsoldat' ;  von  lat.  jpes  stammt  pedäre  ,mit  einem  Fuß versehen,  stützen',   und  davon  wieder  pedum  , Hirtenstab,  Stütze';
pedio-  in  ai.  pddya-  .den  Fuß  betreffend',  pddyä  , Fußtritt,  Huf,  av. paiöyä  ,Fuß',  gr.  neCa  f.  ,Fuß,  unterer  Rand,  Kante,  Saum,  kleines Fischernetz',  lat.  acu-pedius  , schnellfüßig',  ahd.  ßzza  , Gewinde,  Garn' (=  gr.  7t6^a),  nhd.  , Fitze',  (wozu  germ.  *fetl  f.  in  aisl.j^^  , Schwimmhaut, Rand^,  ags.  ßtt  , Abschnitt,  Gedicht',  norw.  dial.  ßor-ßt  , Eidechse',  „tstqü- /Tfi^og"),  lit.  lengva-pldis  ,leisefüßig' ;  pedi-  in  gr.  nsdllov  n.  , Sandale' und  germ.  *fetl]  podio-m  :  mir .  u{i)de  n.  , Reise'.
2.  Verbal:  ai.  pddyate  ,geht,  fällt'  (ä-patti-  , Unfall';  padäti-,  pat-ti-  m. ,Fußknecht'),  av.  paiöyeiti  ,bewegt  sich  nach  abwärts,  legt  sich  nieder': 2iVs[.  pad<^,  pasti  , fallen'  auch  _po-pasfi  , fassen'  eig.  , auf  jemanden  fallen,  an- fallen' (oder  zu  1.  pgc?-?);  napasth  , casus' ;  lit.  pedinu,  -inti  , langsam  gehen, leise  treten',  peduoti  , Fußtritte  machen',  gr.  Tcrjödcü  , springe,  hüpfe';  vgl.  zur e-Stufe  noch  lit.  pedä  , Fußspur',  pescias  ,zii  Fuß'  aus  *ped-tios,  lett.  p^da  , Fuß- sohle, Fußstapfe,  Fuß  als  Maß',  pec  (aus  pedis,  Instr.  Fl.  von  p^ds  , Fuß- spur*, vgl.  lit.  pedas  ds.)  ,nach,  wegen,  gemäß',  aksl.  p^H  ,zu  Fuß',  gr. Tfijööv  , Ruderblatt',  TtrjddXLOv  , Steuerruder' ;  auf  der  verbalen  Bed.  ,mehr abfallend  oder  zum  Fallen,  Verkommen  geneigt'  beruht  letzten  Endes auch  der  Kompar.  lat.  peior  , schlechter'  (*ped-iös),  Superl.  pessimus  ,der schlechteste'  (^ped-Stmos)]  pessum  ,zu  Boden,  zugrunde'  (*ped-tu-m)  =  Inj6n. ai.  pdttum ;  aisl.  feta  st.  V.  (auch  mit  leip,  veg,  heim)  ,den  Weg  finden' ags.  ge-fetan  st.  V.  , fallen',  ahd. /ezzan  ,labare',  gi-fezzan  ,exire,  excidere', 3As\.fata  , seinen  Weg  finden',  ags.  fatian  (wlf)  ,uxorem  ducere',  ahd.  s
===== POK_03 leaf 25
ih uazzon  ,scandere',  ags.  fetian,  engl,  fetch  , holen'  (ags.  fatian  und  fetian könnten  auch  zu  1.  ped-  gehören,  wie  überhaupt  die  beiden  Sippen  nicht scharf  zu  trennen  sind).
3.  pedo-m  usw.:  ai.  padd-  n.  , Schritt,  Tritt,  Fußstapfe',  av.  paöa-  n. jSpur'  (und  ,Fuß  als  Maß'),  ap.  pati-padam  ,an  seine  Stelle  zurückkehrend' ;
arm.  het,  Gen.  hetoy  ^Fußspur^,  Präpos.  y-et  (*i-het  ,in  der  Fußspur') ,nach^,  z-hetj  zetoy  ^hinter  nach^;  mir.  ined  (*eni-pedo-)  ,Spur  (der  Füße); Ort^,  air.  ed  n.  ^Zeitraum^,  ö^U-  candetum  ^spatium,  centum  pedum^  wohl für  cant-lp'ledum]  vgl.  laX.  peda  ,vestigium  humanum^,  aisl.  fet  n.  , Schritt; Fuß  als  Maß'';  lit.  pedä  , Fußspur',  lett.  p^da  , Fußsohle^  usw.  (s.  oben);  gr. nsdov  ;Grund,  Boden'^;  Tcediov  ^Ebene,  Feld'  (£(j,-7tsdog  ,fest  stehend';  über I  öd/tsdov  s.  oben  S.  198) ;   lat.  oppidö  ^völlig;  ganz  und  gar'  (oh  -\-  *pedom
792  •
,auf  der   Stelle');    unibr.   pefum,  persom-e  ,nEdovy  solum';    hitt.  pedan  ^^ Stelle^ ;
o-stufig :  lit.  pädas  .Fußsohle,  Stiefelsohle'  =  aksl.  *pod^  ,Boden,  Unter, grund,  Unterlage'  (Präp.  pod^  .unterhalb,  unter'),  lit.  pädziai  PI.  ,Unter. gestell  einer  Tonne',  aksl.  pozdh  fundamentum,  locus  subterraneus';
schwundstufige  Formen :  ai.  upa-bdd-  m.  , Getrampel',  av.  fra-bda  ,VordeN fuß'  (von  ped-  ,Fuß'),  a-bda-  ,wo  man  nicht  hintreten,  nicht  festen  Fuß fassen  kann';  gr.  sjti-ßdai  ,Tag  nach  dem  Feste'.
4.  Bedeutungsgruppe  ,(Fuß)fessel,  Hindernis  für  die  Füße':  av.  bi-bda. .zweifache  Fessel' ;  gr.  neörj  ,Fessel',  nedaw,  Ttodit^w  ,feßle'  dvöqa-noöov  d. ,Sklave',  iv,-nodö)v  ,aus  dem  Wege',  e^i-nodcbv  ,im  Wege,  hinderlich';  lat. pedica  ,Fessel,  Schlinge'  (womit  z.  B.  ein  Tier  an  einem  Fuß  angebunden wird) ;  lat.  peccäre  .fehlen,  sündigen'  zu  *peccos  <  *ped'Cos  ,einen  Fehler  am Fuß  habend',  wozu  auch  umbr.  pesetom  ,peccatum',  compes  .Fußschelle Fußblock',  impediö,  -Ire  .hindern'.  Gegensatzbildung  expedzre  .das  Hindernis wegnehmen'  (wohl  zu  *pedis  f.  , Fußfessel'  gebildet) ;  dazu  oppidum  ,die Schranken  des  Zirkus  (also  ,quod  pedibus  obest') ;, Landstadt'  (ursprüngl. mit  Hindernissen  verrammelte  Fluchtburg);  allenfalls  umbr.  tribrigu,  tri- hrisine  ,ternio'  als  Hri-pedikiö  , Dreikoppelung' ;  aisl.  fjgttirr  m.  , Fessel. Band',  ags.  föer,  feotor  f.,  as.  f'etur,  ahd.  f'ezzer  ds.
WP.  11  23 ff.,  WH.  I  428  f.,  II  214 f.,  269,  272  f.,  293 ff.,  Trautmann  209 f.
(peg-:)  pog-:pog-,  pbk-s-  , Achsel,  Hüfte,  Lende,  Seite'.
Ai.  pdksa-  m.  , Schulter,  Flügel'  und  .Seitenpfosten',  pdlcsas-  n.  , Seite'; lat.  pectus  , Brust';  lett.  paksis  , Hausecke';  toch.  A  pässäm,  B  päscane ,die  beiden  Brüste';  langvokalisch  sü.  päjasyd-  n.  ,Bauchgegeud,  Weichen', russ.  (usw.)  pach.  , Leistengegend',  pacha  , Achselhöhle',  pachva  .Achsel- höhle, Leistengegend';  d
===== POK_03 leaf 26
aneben  ein  io-St.  *pögio-  in  6ech.  pa^e  ,Arm'  u.  dgl.
WP.  II  3  f.,  WH.  II  270,  Specht  Idg.  Dekl.  237  f.
P^{^-f  P^'  ,weh  tun,  beschädigen,  schmähen';  pe-mn  .Leid,  Krankheit'.
Ai.  piyati  , schmäht,  höhnt',  piyu-,  piyäru-  , höhnend,  schmähend';
gr,  Tifi^ia  ,Verderben,  Leid',  drci^^cjv  , unbeschädigt;  unschädlich',  nrj- fiaivü)  ,stifte  Unheil,  richte  zugrunde'  (idg.  *pe-mn),  nrioao^ai'  ^sixxpaa^ai Hes.,  ij-Ttavla  ,Mangel,  Entbehrung';  rcrjQÖg,  dor.  näQog  ,verstümmelt,  blind',  | U-nriQoq  ,unverstümmelt' ;  lat.  paene  (pene)  , beinahe,  fast;  ganz  und  gar'  ' (ursprüngl.  Neutrum  eines  Adj.  *pe-ni-s  , beschädigt,  mangelhaft'),  paenitet  . ,es  reut,  tut  leid',  penüria  ,Mangel';  von  einem  Partiz.  '*p9-tö'S  ,geschädigt'  j stammt  patior,  -l,  passus  sum  ,dulde,  erdulde,  leide' ;  "
idg.  pei-  in  got.  faian  ,tadeln',  pi-  in  got.  fijan,  aisl.  fjä,  ags.  ßon, ahd.  fien  ,hassen',   Partiz.  Präs.  in  got.  fjands,  ahd.  fiänt  usw.   ,Feind' ;
793
mit  gebrochener  Reduplikation  ai.  päpä-  , schlimm,  böse';  päpmdn-  m. Unheil,  Schaden,  Leiden'  erst  nach  dem  vielleicht  lallwortartigen  päpd- für  *pä7nan-  eingetreten;  ai.  pämdn-  bedeutet  ,eine  Hautkrankheit,  Krätze', Tjämand-,  pämard-  ,krätzig',  wie  av.  päman-  , Krätze,  Fläche,  Trockenheit', ^ozu  vermutlich  lat.  paeminösus,  peminösus  , brüchig,  rissig';  ai.  päpd-  = arm-  hivand-  ,krank*  (Ernst  Lewy).
WP.  n  8 f.,  WH.  II  234f.,  264,  283.
pei{9y,  P^-  , fett  sein,  strotzen*;  pei-tu-f  poi-tu-,  pl-tu-  ,Fett,  Saft,  Trank', pi-k-  ,Pech*,  pi-mo-  ,fett',  pi-u-er- j -en-  ,Fett,  fett',  poi-uä  (,fette) Wiese';  poi-men-  , Muttermilch*,  pi-pi-us-i  , Milch  habend*.
Ai.  pdyate  ,schwillt,  strotzt,  macht  schwellen,  strotzen',  pipyüsi  , strotzend, milchreich',  av.  (a)-pij)yüäi-  ,(keine)  Milch  in  der  Brust  habend^  (nicht) säugend'  (:  lit.  pa-pijusi),  ai.  plnd-  ,fett,  feist,  dick',  pyäyate  , schwillt, strotzt',  pinvati  ,macht  schwellen',  a.v .  fra-pinaoiti  , bringt  zum  Gedeihen'; ai.  pdyas-  n.  ,Saft,  Wasser,  Milch',  av.  payah-  n.  , Milch',  av.  paeman-  n. , Muttermilch'  (:  ags.  fcemne);  np.  pinü  , saure  Milch,  frischer  Käse'  (:  lit. pienas  , Milch'),  ai.  piru-,  pei'u-  , anschwellend,  schwellend  machend'  (wohl mit  idg.  l,  so  daß  zu  norw.  fei);
norw. /eZ  ,Rahm,  dickgemachte  Milch*;  a.gs.  fcßmne  , Jungfrau,  junge Frau',  as.  femea  , schwangere  Frau',  a.is\.  feima  .Mädchen'  (:  a.Y.  paeman- , Muttermilch') ;
lit.  papijusi  kdrve  ,Kuh,  die
===== POK_03 leaf 27
  beim  Melken  die  Milch  nicht  zurückhält', pydau,   -dyti   ,zum  Milchen   reizen',  pyti  , Milch   spenden',  pienas  , Milch' ;
pimo-s  ,fett'  in  gr.  Tilf-isli^  ,Fett',  lat.  oplmus  ,fett,  wohlgenährt; fruchtbar;  reich'  (wohl  pinguis  .fett' :  Kreuzung  von  '^plmos  und  *finguis, s.  oben  S.  128).
u-Bildungen :
att.  nöa,  ep.-ion.  Ttolrj,  dor.  nola  ,Gras,  Rasenplatz',  aus  *noiJ^ä  =-  lit. pieva  , Wiese'  (*poiuä);
piuo-s-  und  piu-erj-en-  ,Fett,  fett':  ba.  pivas-  n.,  av.  pwah-  n.  ,Fett, Speck';  3A.  pivan-,  L  pivari  , schwellend,  strotzend,  feist,  fett',  plvard-  ds., jüngere  Bildung  vom  Fem.  aus,  mit  dem  ebenfalls  nicht  alten  gr.  niegög, TCiagög  =  gr.  7tt(x)v,  f.  rcieiga  ,fett,  fruchtbar,  reich',  nlaQ  (nur  Nom.  Akk. Sg.  '^pt-ur)  ,Fett' ;  air.  Iriu,  Gen.  irenn  (*pl-uer-iö)  , Erdboden,  Land',  wenn eigentl.  „TtUtga  yrf^ ;
fu-St.  pei-tu-,  pl-tu-  ,Fett,  Saft,  Trank,  Nahrung' :  ei  in  lit.  pietüs , Mittagsmahl' ;  vgl.  ai.  pkv-a-  m.  ,Bock,  Hammel'  (eig.  , feist'),  av.  pöid-ioa , feist';
794  ^
pl-tu-  ,Trank,  Speise':  ai.  pitü-  m.,  3lv.  pitu-s  m.  ,Saft,  Trank,  Nahrung^ Speise',  av.  ai^mpi&wä,  ra-pi&wä  i.  , Mittag,  Mittagszeit',  eig.  ,die  z^^jj Mahle  passende  Zeit';  air.  ith  ,(*Nahrung),  Korn,  Getreide',  acyinr.  {<^ ncjmr.  yd  {*pitu-)  usw.  ,ds.' ;  l3it.  pltuUa  , reiche  Feuchtigkeit,  Schnupfen«, mir.  Uh  ,Talg'  (*pitu-);  wozu  als  Denominativ  aksl.  pitäti,  jünger pitati  , füttern,  ernähren,  aufziehen';  hieher  von  der  Bed.  ,Harz'  aus:  ai. pUu-däru  ,eine  Fichtenart',  eig.  , Harzbaum',  und  als  Kurzformen  eine« solchen  Kompositums  pamird.  pit  , Fichte',  gr.  TrtVug  ds. ;  vollstufig  mip^ lath  n.  (,fette)  Wiese,  Land'  (*pei-tu-)]  die  Bedeutung  ,Harz'  auch  in  der k-Ableitung  *pi-k-:  gr.  Ttiaaa  att.  ttiVit«  f.  ,Pech^,  TtiTTamov  n.  , Schreib- täfelchen, Pflaster',  lat.  pix,  picis  f.  ,Pech,  Teer'  (daraus  ahd.  peh  usw.), vielleicht  mnd.  vi(g),  vlhe  , Sumpf,  Bruch';  (lit.  pthis  ,Pech'  ist  germ.  Lw.), aksl.  pbcih,  russ.-ksL  ptkhh  ,Pech';  aber  lat.  pinus,  -üs  und  -l  , Fichte, Föhre,  Kiefer'  wegen  alb.  pishe  , Fichte,  Kienfackel'  (*pit-s-{a)  wohl  aus *pit-s-nu-s ;  *
Erweiterung  poi-d-,  pi-d-  :  gr.  TtiörjeLg  , quellenreich',  nXöa^  , Quelle*, niövo)  , lasse  durchsickern,  quelle  hervor',  Nom.  PL  n.  niosa  , feuchte  Orte, Wiesen'  (*2?Z-cZ-s-es-) ;  aisl.j^^a  f.  ,Fett',  germ.  *faltian  .mästen'  (alid.  feizen, ags.  fztan,  aisl.  feita),  *faita-  ,fett'  (ahd.  feiz,  aisl.  feitr),  Partiz.  germ. *faitida- :  a\id.  feizzüj  mhd.  veiz{e)t,  nhd.  feist,  sgs.  fäeted,  engl,  fat,  mnd. vet  ,fett';  aisl.  fit  ,Wiese',  ostfries.  , Pfütze';  lett.  pha,  plse  , Morast,  Busch- wald' ;  über  mir.  esc  , Wasser^  (s.  oben  S.  43  über  mir.  esc-ung  , Aal'), wozu  mir.  esca  f.  , Sumpf,  s.  unter  peisk-  , Fisch';  oder  esc  aus  *pid-skä'^
WP.  II  73  ff.,  WH.  211  f.,  3
```


## [2026-09-07T20:43:45.101Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD peg\"; grep -n -i \"^peg\\b\\|^peg-\\|pectus\" AHD_watkins1985.txt | head -20; echo \"=== AHD pei\"; grep -n -i \"^pei\\b\\|^peia\\|^pei-\\|^peia-\\|faitaz\\|pinus\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-07T20:43:45.155Z] TOOL RESULT

```
=== AHD peg
820:peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit
2071:PEG bak- PEGMATITE pag- PEJORATION ped-1 PELAGE pilo- PELAGIC plak-1 PELARGONIUM pel-2 PELECYPOD ped-1 PELISSE pel-4 PELLAGRA ag-, pel-4 PELLICLE pel-4 PELL-MELL meik- PELLUCID leuk- PELOPS okw-, pel-2 PELORIA kwer-1 PELT! pel-4 PELTATE pel-4 PELTRY pel-4 PELVIS pel-7 PEN! pet-
=== AHD pei
823:peie-. Also pei-. To be fat, swell. 1. Extended o-grade form *poid- in Germanic *faitaz, plump, fat, in derivative Germanic verb *faitjan, to fatten, whence Germanic past participle *faitidaz, fattened, in Old English f#t/t), fat: FAT. 2. Possibly suffixed zero-grade form *pi-tu- in Latin pituita, moisture exuded from trees, gum, phlegm: PIP 5, PITUITARY, PITUITOUS. 3. Possibly suffixed zero-grade form “pi-nu- in Latin pinus, pine tree (yielding a resin): PINE!, PINEAL, PINON, PINNACE; PINA CLOTH. 4. Suffixed zero-grade form *pi-won- in Greek pidn, fat: PROPIONIC ACID. 5. Suffixed zero-grade form *pi-wer-, “fat, fertile,” in: a. *Iwer-ii, the prehistoric Celtic name for Ireland, in Old English Jras, the Irish: (ERSE), IRISH; b. * Piwer-id in Greek Pieria, a region of Macedonia: PIERIAN SPRING. [Pok. pei()- 793.]
1108:eaves: EAVES; b. Germanic *obisdrup-, dripping water from the eaves (*drup-, to drip, from *dhrub-; see dhreu-), in Old English yfesdrype, yfes drypx, water from the eaves: EAVESDROP. 6. Variant form *(s)up- in: a. Latin sub, under: SOUTANE, SUB-; b. Latin supinus, lying on the back (< “thrown backward or under’): SUPINE!, SUPINE?; Cc. suffixed form *sup-ter in Latin subter, secretly: SUBTERFUGE; d. Latin supplex, “with legs folded under one” (-plex, -fold; see plek-): SUPPLE. 7. Basic form *upo in Greek hupo, under: HYPO-. 8. Suf- fixed variant form *ups-o- in Greek hupsos, height, top: HYPSO-. 9. Basic form *upo- in Celtic *vo-, under, in Latin verédus, post horse (see reidh-). 10. Compound *upo-st-o- probably in Celtic *wasso-, “one who stands under,” servant, young man (*sto-, standing; see sta-), in Medieval Latin vassus, vassal: VALET, (VARLET), VASSAL. 11. Sanskrit wpa, near to, under (in upanisad, Upani- shad): OPAL, UPANISHAD. [Pok. upo 1106.]
```


## [2026-09-07T20:43:46.809Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN punkah/punka\"; grep -n -i \"punkah\\|punka,\" KLN_1966.txt | head; echo \"=== KLN pectoral\"; grep -n -i \"^pectoral\" KLN_1966.txt|head; echo \"=== HJB PUNKAH\"; grep -n -i \"^PUNKAH\\|PUNKAH,\" HJB.txt | head"
}
```


### [2026-09-07T20:43:46.889Z] TOOL RESULT

```
=== KLN punkah/punka
31025:Algonquian  punk,  ponk,  'live  ashes’, punk,  n.,  1)  a  prostitute  ( obsol .);  2)  a  young gangster  (slang).  —  Of  uncertain  origin, punka,  punkah,  n.,  a  large  curtain  serving  to  fan  a room.  —  Hind,  pankha,  *a  fan ,  fr.  pankh , ‘feather,  wing’,  fr.  OI.  pakfah,  pdkfas,  ‘wing, side,  half’,  which  is  possibly  cogn.  with  Lett. paksis,  ‘corner  of  a  house’,  Russ,  pach,  ‘flank’, punner,  n.,  a  rammer.  —  Formed  fr.  dial  pun,  ‘to pound,  beat’,  with  agential  suff.  -er. punnet,  n.,  a  small  round  chip  basket.  —  Of  un¬ known  origin.
=== KLN pectoral
27810:pectoral,  n.,  something  worn  on  the  breast; specif,  the  breast  plate  of  the  Jewish  high  priest.
=== HJB PUNKAH
18220:PUNKAH.
18242:PUNKAH,
18244:PUNKAH,
```


## [2026-09-07T20:43:57.171Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '818,826p' AHD_watkins1985.txt; echo \"=== KLN leaf for punka\"; awk 'BEGIN{RS=\"\\f\"} /punka,  punkah/{print NR-1}' KLN_1966.txt; echo \"=== HJB\"; sed -n '18215,18260p' HJB.txt"
}
```


### [2026-09-07T20:43:58.525Z] TOOL RESULT

```
ANTIPODES, APODAL, APPOGGIATURA, APUS, CALIBER, LYCOPODIUM, MONOPODIUM, OCTOPUS, PELECYPOD, PHALAROPE, PLATYPUS, PODAGRA, PODIATRY, PODOPHYL- LIN, POLYP, POLYPOD, SYMPODIUM; b. Russian pod, un- der: PODZOL. 8. Suffixed form *ped-ya in Greek peza, foot: TRAPEZIUM. 9. Suffixed form *ped-o- in: a. Greek pedon, ground, soil: PEDO-!; PARALLELEPIPED; b. San- skrit padam, footstep, foot, and pat (> Hindi paisd), foot: PAISA, PICE, PIE’, PUG3; c. Middle Persian pdi, leg, foot: PAJAMAS, TEAPOY; d. lengthened-grade form *pédo- in (i) Greek pédon, rudder, steering oar: PILOT (ii) Greek pédan, to leap: DIAPEDEsIs. 10. Suffixed form *ped-i- in Greek pedilon, sandal: CYPRIPEDIUM. II. Verbal root *ped-, to stumble, fall. 1. Germanic *fetén in Old English fetian, feccean, to bring back: FETCH!. 2. Latin *ped- in: a. suffixed (comparative) form *ped-yos in Latin péor, worse (< “stumbling”): PEJORATION; IMPAIR; b. suffixed (superlative) form *ped-samo- in Latin pessimus, worst: PESSIMISM; C. suffixed form *ped-ko- in Latin peccdre, to stumble, sin: PECCABLE, PECCADILLO, PECCANT; IMPEC- CABLE. [Pok. 2. péd- 790.]
ped-2. Container. 1. Suffixed o-grade form *pod-om in Germanic “fatam in Old English fzt, cask: vat. 2. Suf- fixed o-grade form *pod-ilo- in Germanic *fatilaz in Old English fetel, girdle: FETTLE. 3. Probably full-grade form *ped- in Germanic *fet- in Middle High German vetze, “clothes,” rags, probably akin to the source of obsolete English fritter, fragment: FRITTER}. [Pok. 1. péd- 790.]
peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit
paksah, wing: PUNKA. [Pok. (peg-), pdg- 792.]
p@(i)-. Also pé-, pi-. To hurt. Possible root; contracted from *pea(i)-. 1. Suffixed (participial) form *pi-ont- (< *pia-ont-) in Germanic *fiand-, hating, hostile, in Old English féond, fiond, enemy, devil: FIEND. 2. Possibly *pé- in suffixed zero-grade form *po-to- in Latin pati, to suffer: PASSIBLE, PASSION, PASSIVE, PATIENT; COMPAS- SION. [Pok. pé(i)- 792.]
peie-. Also pei-. To be fat, swell. 1. Extended o-grade form *poid- in Germanic *faitaz, plump, fat, in derivative Germanic verb *faitjan, to fatten, whence Germanic past participle *faitidaz, fattened, in Old English f#t/t), fat: FAT. 2. Possibly suffixed zero-grade form *pi-tu- in Latin pituita, moisture exuded from trees, gum, phlegm: PIP 5, PITUITARY, PITUITOUS. 3. Possibly suffixed zero-grade form “pi-nu- in Latin pinus, pine tree (yielding a resin): PINE!, PINEAL, PINON, PINNACE; PINA CLOTH. 4. Suffixed zero-grade form *pi-won- in Greek pidn, fat: PROPIONIC ACID. 5. Suffixed zero-grade form *pi-wer-, “fat, fertile,” in: a. *Iwer-ii, the prehistoric Celtic name for Ireland, in Old English Jras, the Irish: (ERSE), IRISH; b. * Piwer-id in Greek Pieria, a region of Macedonia: PIERIAN SPRING. [Pok. pei()- 793.]
peig-'. Also peik-. To cut, mark (by incision). 1. Alter- nate form *peik- in Germanic *fihala, cutting tool, in Old English fil, file: FILE. 2. Nasalized zero-grade form *pi-n-g- in Latin pingere, to embroider, tattoo, paint, picture: PAINT, PICTOR, PICTURE, PICTURESQUE, PIG- MENT, PIMENTO, PINTO; DEPICT, PICTOGRAPH. 3. Suffixed zero-grade form *pik-ro- in Greek pikros, sharp, bitter: PICRO-. 4. O-grade form *poik- in Greek poikilos, spotted, pied, various: POIKILOTHERM. [Pok. 1. peig- 794.]
peig-?. Also peik-. Evil-minded, hostile. 1. Suffixed zero-grade form *pig-olo- in Germanic *fikala- in Old
English ficol, treacherous, false: FICKLE. 2. Suffixed o-grade form *poik-os in Germanic *gafaihaz (*ga-, collective prefix; see kom), in Old English gefah, enemy: FOE. 3. Suffixed o-grade form *poik-yos in Germanic *faigjaz in Old English fege, fated to die: FEY. 4. Suf-
=== KLN leaf for punka
678
=== HJB
(2)  Jelam  (see  JELUH)  or  Behat,  the ancient  Vitasta  which  the  Greeks  made "TSdinryis  (Straho)  and  BiSdunrijs  (PtoL).
(3)  Chenab,  ancient  Gkandrabd^ha  and Asikni,  Ptolemy  preserves  a  corrup- tion of  the  former  Sanskrit  name  in Sai'Sa/SdX,  but  it  was  rejected  by  the older  Greeks  because  it  was  of  ill omen,  i.e.  probably  because  Grecized it  would  be  AapSpotpdyos,  '  the  devourer of  Alexander.'  The  alternative  Asikiii they  rendered  'AKeffiyrjs.  (4)  Ravi,  the ancient  Airdvatl,  'Tdpwrrfs  (Straho), TSpaiirriji  (Arrta7i),  "ASpis  or  'PoiJadtf (PtoL),  (5)  Bias,  ancient  Fijxf^/T^ao-is (Arrian),  Bi/3<£<rto»  {Ptol,).  This  ex- cluded the  Sutlej,  Satadru,  Hesydrus of  Pliny,  Zapddpos  or  Zadddfnis  {PtoL), as  Timur  excludes  it  below.  We  may take  in  the  Sutlej  and  exclude  the Indus,  but  we  can  hardly  exclude  the Chenab  as  Wassaf  does  below.
No  corresponding  term  is  used  by the  Greek  geographers.  "Putandum est  iiomen  JranclUul&dae  Graecos  aut omnino  latuisse,  aut  casu  quodam  non ad  nostra  usque  tempora  pervenisse, quod  in  tanta  monumentorum  ruina facile  accidere  potuit"  {Lassen,  Penta- potamia,  3).  Lassen  however  has termed  the  country  Pentepotamia  in a  learned  Latin  dissertation  on  its ancient  geography.  Though  the  actual word  Panjdb  is  Persian,  and  dates from  Mahommedan  times,  the  corre- sponding Skt.  Panchanada  is  ancient and  genuine,  occurring  in  the  Mahd- bhdrata  and  Rdmdyana.  The  name Panj-db  in  older  Mahommedan  writers is  applied  to  the  Indus  river,  after
FUNJAUB.
742
PUNKAH.
receiving  the  rivers  of  the  country which  we  call  Punjaub,  In  that  sense Panj-nad,  of  equivalent  meaning,  is  still occasionally  used.  [In  S.  India  the term  is  sometimes  applied  to  the country  watered  by  tne  Tumbhadra, Wardha,  Malprabha,  Gatprabha  and Kistna  (WiUcH^  Hid.  Sketches,  Madras reprint,  i.  405).]
We  remember  in  the  newspapers, after  the  second  Sikh  war,  the  report of  a  speech  by  a  clergyman  in  England, who  spoke  of  the  deposition  of  "the l)loody  Punjaub  of  Lanore."
B.C.  «.— "  Having  explored  the  Umd  of  the Pahlavi  and  the  country  adjoining,  there had  then  to  be  Rearched  Panchimada  in every  part ;  the  monkeys  then  explore  the region  of  Kashmir  with  its  woods  of  acacias." — RSmAyana,  Bk.  iv.  ch.  43.
c.  940.— MaK'udI  details  (with  no  correct- ness) the  five  rivers  that  form  the  Mihran or  Indus.  He  proceeds:  "When  the  Five Rivers  which  we  have  named  have  past  the House  of  Grold  which  is  Multan,  they  unite at  a  place  three  days  distant  from  that  city, between  it  and  Mansura  at  a  place  called Doshab."— i.  377-8.     '
c.  1020.— "  They  all  (Sind,  Jhailam,  Irawa, Biah)  combine  with  the  Satlader  (Sutlei) below  MiHt^n,  at  a  place  called  Paiijiiaa, or  'the  junction  of  the  five  rivers.'  They form  a  very  wide  stream."— ^/-^I'rflwf,  in BUiot,  i.  48.
c.  1300.— "After  crossing  the  Panj-ftb, or  five  rivers,  namely  Sind,  Jelam,  the  river of  Loh^wnr  (i.e.  of  Lahore^  viz.  the  Ravi), SatliSt,  and  Biyah.  .  .  ."—WoMOf,  in  Elliot, iii.  36.
c.  1333.— "By  the  grace  of  God  our  cara- van arrived  safe  and  sound  at  Baoj-Ab,  i.e. at  the  River  of  the  Sind.  BanJ  ( panj)  signi- fies 'five,'  and  flA,  *  water  ;'^  so  that  the name  signifies  *the  Five  Waters,'  They flow  into  this  great  river,  and  water  the country."— /6n.  Batutay  iii.  91.
c.  1400.— "All  these  (united)  rivers  (Jelam, Chen^b,  Rivf,  Blyfli,  Sind)  are  called  the Sind  or  Panj-ib,  and  this  river  falls  into the  Persian  Gulf  near  Thatta."— 7%c  Emp. Timur,  in  Elliot,  iii.  476.
[c.  1680. — "  He  also  takes  a  Survey  of Pang-ob  .  .  :'—Sir  T.  Hm-heH,  ed.  1677, p.  63.    He  gives  a  list  of  the  rivers  in  p.  70.]
1648.—".  .  .  Pang-ab,  the  chief  city  of which  is  Lahor,  is  an  excellent  and  fruitful province,  for  it  is  watered  by  the  five  rivers of  which  we  have  formerly  spoken." — Van Twtjtt,  3.
"  "  The  River  of  the  ancient  Indus, is  by  the  Persians  and  Magols  called  Pang- ab,  i.e.  the  Five  Waters."— /frirf.  i.
1710. — "  He  found  this  ancient  and  famous city  (Lahore)  in  the  Province  Pansohaap, by  the  side  of  the  broad  and  fish-abounding river  Rari  (for  Jtavty'—Valmtiin,  iv.  (Su- 7-aae),  282.  ^  »         \
1790.  —  "Investigations  of  the  religious oeremomes  and  customs  of  the  Hindoo«, written  in  the  Caniatic,  and  in  the  Pnajmb, would  in  many'cases  widely  differ."— /TDrtTw, Preface  to  Journey.
1793.—"  The  Province,  of  which  Lahore  i^ the  capital,  is  of  toner  named  PanJab  than Lahore." — RennelCt  Memoir,  8rd  ed.  82.
1804.— "I  rather  think  .  .  .  thathe(HoI- kar)  wOl  go  off  to  the  PnnJanb.  And  what gives  me  stronger  reason  to  think  so  is,  that on  the  seal  of  his  letter  to  me  he  calls  him- self '  tka  SUvt  of  Shah  Makmoud,  the  King of  Kingg.*  Shah  Mahmoud  is  the  brother of  Zemaun  Shah.  He  seised  the  musnnd  and government  of  Caubul,  after  having  defeated Zemaun  Shah  two  or  three  years  ago,  and put  out  his  eyes." — WellingtaR,  Desp.  under March  17.
1815. — "He  (Subagtageen)  .  .  .  oventin the  fine  province  of  the  Poajanb,  in  his  fir»t expedition."  —  MafcoltHj  Hut.  of  Prrsia,  i.
PUNELAJE,  s.     Hind,  pankhd.
a.  In  its  original  sense  a  portable fan,  generally  made  from  tbe  leaf  of the  palmyra  {Borass^is  ftaheUiformi*,  or *  fan-shaped  *),  the  natural  type  and oricin  of  the  fan.  Such  pankhds  in India  are  not  however  formed,  as Chinese  fans  are,  like  those  of  our ladies ;  they  are  generally,  whetlier large  or  small,  of  a  l)ean-shape,  irith a  part  of  the  dried  leaf-stalk  adhering, wnich  forms  the  handle.
b.  But  tlie  specific  application  iu Anglo-Indian  colloquial  is  to  the  large fixed  and  swinging  fan,  formed  of cloth  stretched  on  a  rectangular  frame, and  suspended  from  the  ceiling,  which is  used  to  agitate  the  air  in  hot weather.  The  date  of  the  introduc- tion of  this  machine  into  India  i^^  not known  to  us.  The  quotation  from Linschoten  shows  that  some  such  ap- paratus was  known  in  the  16th  century, though  this  comes  out  clearly  in  the French  version  alone  ;  the  original Dutch,  and  the  old  English  translation are  here  uuintellicible,  and  indicate that  Linschoten  (who  apparently  never was  at  Ormuz)  was  describing,  from hearsay,  something  that  he  did  not understand.  More  remarkable  pas- sages are  those  which  we  take  from Dozy,  and  from  El-Fakhri,  which show  that  the  true  Anglo-Indian  7nirij» was  known  to  the  Arabs  as  early  hs the  8th  century.
a.—
1710.— "Aloft  in  a  Gallery  the  King  sits in  his  chaire  of  State,  accompanied  with  hia
PUNKAH,
743
PUNKAH,
Children  and  chiefe  Vizier  ...  no  other without  calling  daring  to  goe  yp  to  him, saue  onelv  two  PnnkawB  to  gather  wind."— W.  Fin^h,  in  Purckat,  i.  439.  The  word seems  here  to  be  used  improperly  for  the men  who  plied  the  fans.  We  find  also  in  the same  writer  a  verb  to  ponkaw :
"...  behind  one  punkawiBg,  another holding  his  sword."— iWrf.  488.
Terry  does  not  use  the  word  :
1616. — ".  .  .  the  people  of  better  quality, lying  or  sitting  on  their  Cazpets  or  Pallats, have  servants  standing  about  them«  who  con- tinually beat  the  air  upon  them  with  Fla- Mfa's,  or  Fans,  of  stiffned  leather,  which keepe  off  the  flyes  from  annoying  them, '  and  cool  them  as  they  lye."— Ed.  1666, p.  405.
1668. — "  On  such  occasions  they  desire nothing  but  ...  to  lie  down  in  some  cool and  shady  place  all  along,  having  a  servant or  two  to  fan  one  by  turns,  with  their  great Pankas,  or  Faiia.—Beniier,  E.T.,  p.  76  ; [ed.  Constable,  241].
1787. — "Over  her  head  was  held  a  pim- ker."— .Sir  C.  Malet,  in  Pari.  Papers,  1821, *  Hindoo  WidoKS.*
1809.—"  He  .  .  .  presented  me  .  .  .  two puakahB^—Loixl  Vateniia,  i.  428.
1881.—"  The  chair  of  state,  the  sella  ^esta- toriay  in  which  the  Pope  is  borne  aloft,  is  the ancient  palanquin )  of  the  Roman  nobles, and,  of  course,  of  the  Roman  Princes  .  .  . the  fans  which  go  behind  are  the  punkahB of  the  Eastern  Emperors,  borrowed  from the  Court  of  Persia.  — Bean  Stanley ,  Chris- tian Institutionf,  207.
b.-
c.  1150-60.— "Sous  le  nom  de  Khaich  on entend  des  dtoffes  de  mauvais  toile  de  lin qui  servent  k  diff^rents  usages.  Dans  ce passage  de  Rhas^s  (c.  A.D.  900)  ce  sont  des ventilateurs  faits  de  cet  ^toffe.  Ceci  se pratique  de  cette  mani^re :  on  en  prend  un niorceau  de  la  grandeur  d'un  tapis,  un  pou plus  grand  ou  un  pen  plus  petit  selon  les dimensions  de  la  chambre,  et  on  le  rembourre avcc  des  objets  qui  ont  de  la  consistance  ct qui  ne  plient  pas  facilement,  par  exemple avec  du  sparte.  L'ayant  ensuite  suspendu au  milieu  de  la  chambre,  on  le  fait  tirer  et lacher  doucement  et  continuellement  par  un homme  plac^  dans  le  haut  de  I'appartement. De  cette  mani^re  il  fait  beauooup  de  vent  et rafcaichit  I'air.  Quelquefois  on  le  trempe dans  de  Teau  de  rose,  et  alors  il  parfume I'air  en  m6me  temps  qu'il  le  rafraichit." — Olitfsaire  sur  le  Man^ouri,  quoted  in  Lhny  et Engelviann,  p.  342.  See  also  Dozy,  Suppt. avx  Dictt.  Araf^Sy  s.v.  Khaich.
1166.  — "He  (Ibn  Hamdun  the  Katib) once  recited  to  me  the  followinp^  piece  of  his composition,  containing  an  enigmatical  de- scription of  a  linen  fan :  (^)
"  *Fast  and  loose,  it  cannot  touch  what it  tries  to  reach ;  though  tied  up  it  moves swiftly,  and  though  a  prisoner  it  is  free. Fixed  in  its  place  it  drives  before  it  the gentle  breeze  ;  though  its  path  lie  closed  up
it  moves  on  in  its  nocturnal  journey.'"— Quoted  by  Jbn,  KhalliJcan,  E.T.  ui.  91.
"  {})  The  linen  fan  {Mirwaha-t  al  Khaith) is  a  large  piece  of  linen,  stretched  on  a frame,  and  suspended  from  the  ceiling  of the  room.  Th^  make  use  of  it  in  Ir&k. See  de  Sacy's  Hariri^  p.  474."— Note  by MacOucHn  de  Slane^  ibid,  p.  92.
0.  1800. — "One  of  the  innovations  of  the Caliph  MansOr  (A.D.  753-774)  was  theKhaish of  linen  in  summer,  a  thing  which  was  not known  before  his  time.  But  the  Sasanian Kings  used  in  summer  to  have  an  apartment freshly  plastered  (with  clay)  every  day, which  they  inhabited,  and  on  the  morrow another  apartment  was  plastered  for  them." —M-Fakhri,  ed.  Ahlwardt,  p.  188.
1596. — "And  (they  use)  instruments  like swings  with  fans,  to  rock  the  people  in,  and to  make  wind  for  cooling,  which  they  call cattaventos.*' — Literal  Transln.  from  Lin- schoten,  ch.  6.
```


## [2026-09-07T20:44:07.446Z] TOOL CALL #15: Bash

```json
{
 "command": "pdftoppm -f 385 -l 385 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg385 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T20:44:09.069Z] TOOL RESULT

```
total 35604
drwx------ 2 sfmqrb sfmqrb    12288 Sep  7 16:44 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   107524 Sep  7 12:27 328-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43713 Sep  7 12:35 331-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135301 Sep  7 12:35 331-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52382 Sep  7 12:41 333-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88345 Sep  7 12:41 333-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68568 Sep  7 12:43 335-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105946 Sep  7 12:43 335-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:57 340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24993 Sep  7 13:57 340-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92337 Sep  7 13:59 342-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92697 Sep  7 13:56 343hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30778 Sep  7 13:56 343-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:52 346-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81599 Sep  7 14:37 350-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99691 Sep  7 14:40 351-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115624 Sep  7 14:43 355-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85914 Sep  7 14:35 358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19549 Sep  7 14:35 358-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74812 Sep  7 14:35 358-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    95065 Sep  7 15:49 361-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65864 Sep  7 15:52 362-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77269 Sep  7 15:46 364-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   160756 Sep  7 15:55 365-full.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87585 Sep  7 15:50 366-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67738 Sep  7 16:41 369-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56986 Sep  7 16:30 371-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94684 Sep  7 16:37 372hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    16118 Sep  7 16:37 372-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   100033 Sep  7 16:40 377hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30053 Sep  7 16:40 377-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1579505 Sep  7 14:24 afm76.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1055262 Sep  7 14:23 afm77.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1759 Sep  7 16:43 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   153966 Sep  7 13:44 bqt2014_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299343 Sep  7 15:34 bqt2173_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79304 Sep  7 15:38 bqt2195_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59998 Sep  7 15:38 bqt2210_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   257093 Sep  7 16:29 bqt71-373.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    87252 Sep  7 16:40 build-369.py
-rw-rw-r-- 1 sfmqrb sfmqrb    56326 Sep  7 16:40 build-370.py
-rw-rw-r-- 1 sfmqrb sfmqrb    82003 Sep  7 16:42 build-373.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46805 Sep  7 16:38 build-375.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68148 Sep  7 16:40 build-378.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11800 Sep  7 14:19 c355_arab2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7474 Sep  7 14:19 c355_conn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10501 Sep  7 14:19 c355_runik2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7270 Sep  7 14:19 c355_runik.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6375 Sep  7 16:28 crop377-niush.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46690 Sep  7 13:44 crop_av3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40759 Sep  7 13:44 crop_heb.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94819 Sep  7 13:44 crop_pers0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70860 Sep  7 15:48 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    34373 Sep  7 15:52 e0_p363.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37506 Sep  7 15:51 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37506 Sep  7 15:52 e2_p363.json
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78732 Sep  7 13:40 ffd32.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30152 Sep  7 15:34 ffd77_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 15:34 ffd77.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 13:44 ffd82.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63978 Sep  7 12:35 mk330.py
-rw-rw-r-- 1 sfmqrb sfmqrb    64100 Sep  7 12:34 mk331.py
-rw-rw-r-- 1 sfmqrb sfmqrb    90456 Sep  7 12:42 mk332.py
-rw-rw-r-- 1 sfmqrb sfmqrb    99976 Sep  7 12:34 mk334.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57252 Sep  7 12:38 mk337.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83271 Sep  7 13:58 mk338.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74349 Sep  7 13:57 mk340.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59512 Sep  7 13:57 mk341.py
-rw-rw-r-- 1 sfmqrb sfmqrb    82502 Sep  7 13:57 mk342.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66284 Sep  7 13:55 mk343.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58811 Sep  7 13:57 mk344.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36436 Sep  7 13:51 mk348b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    20510 Sep  7 13:47 mk348.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67410 Sep  7 14:53 mk353.py
-rw-rw-r-- 1 sfmqrb sfmqrb    87481 Sep  7 14:40 mk354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    38634 Sep  7 14:34 mk358.py
-rw-rw-r-- 1 sfmqrb sfmqrb    53090 Sep  7 15:49 mk361.py
-rw-rw-r-- 1 sfmqrb sfmqrb    86861 Sep  7 15:51 mk362.py
-rw-rw-r-- 1 sfmqrb sfmqrb    33821 Sep  7 15:52 mk363a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36857 Sep  7 15:52 mk363b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62290 Sep  7 15:49 mk366.py
-rw-rw-r-- 1 sfmqrb sfmqrb    54370 Sep  7 15:45 mk368.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66902 Sep  7 16:39 mk377.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:42 navak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3021 Sep  7 13:42 navak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1525 Sep  7 13:41 p342_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1759 Sep  7 13:41 p342_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1703 Sep  7 13:41 p342_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108903 Sep  7 13:41 p342hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10531 Sep  7 13:39 p343_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30408 Sep  7 13:39 p343_mus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103027 Sep  7 14:19 p355hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86505 Sep  7 14:27 p358_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114524 Sep  7 14:19 p358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    37883 Sep  7 14:20 p358_q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36134 Sep  7 14:20 p358_q3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4274 Sep  7 14:19 p358_quote.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4789 Sep  7 15:38 p361_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4152 Sep  7 15:38 p362_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3458 Sep  7 15:35 p362_germ1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2606 Sep  7 15:35 p362_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135659 Sep  7 15:34 p363_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   223838 Sep  7 15:34 p363_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   118891 Sep  7 15:45 p365_row8.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13022 Sep  7 15:42 p366_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3884 Sep  7 16:21 p372_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6025 Sep  7 16:21 p372_q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36604 Sep  7 16:22 p372_q3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    15566 Sep  7 16:22 p372_q4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4259 Sep  7 16:21 p372_quote.png
-rw-rw-r-- 1 sfmqrb sfmqrb    21223 Sep  7 13:47 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb     5736 Sep  7 14:43 patch354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb   146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb   128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb   104609 Sep  7 12:27 pg333hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70886 Sep  7 12:26 pg333.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88659 Sep  7 12:22 pg335.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57846 Sep  7 12:31 pg336.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65267 Sep  7 13:37 pg338.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63922 Sep  7 13:44 pg339.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:44 pg340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75149 Sep  7 13:40 pg342.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60735 Sep  7 13:42 pg344.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168870 Sep  7 13:42 pg346hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59757 Sep  7 14:29 pg349.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70743 Sep  7 14:25 pg350.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86553 Sep  7 14:25 pg351.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69045 Sep  7 14:18 pg355.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78195 Sep  7 14:27 pg357.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49496 Sep  7 14:19 pg358.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82867 Sep  7 15:38 pg359.png
-rw-rw-r-- 1 sfmqrb sfmqrb    45536 Sep  7 15:36 pg360.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57895 Sep  7 15:38 pg361.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111691 Sep  7 15:34 pg362hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76202 Sep  7 15:29 pg362.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66511 Sep  7 15:33 pg363.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49805 Sep  7 15:37 pg364.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94462 Sep  7 15:45 pg365.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59224 Sep  7 15:34 pg367.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49419 Sep  7 15:35 pg368.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1760 Sep  7 16:24 pg369-eb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    18053 Sep  7 16:23 pg369-emptybox.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108532 Sep  7 16:23 pg369hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7447 Sep  7 16:23 pg369-latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3387 Sep  7 16:24 pg369-nocht.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74176 Sep  7 16:23 pg369.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40427 Sep  7 16:22 pg371crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9084 Sep  7 16:22 pg371crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90632 Sep  7 16:22 pg371hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53926 Sep  7 16:17 pg371.png
-rw-rw-r-- 1 sfmqrb sfmqrb   152304 Sep  7 16:21 pg372hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59170 Sep  7 16:21 pg372.png
-rw-rw-r-- 1 sfmqrb sfmqrb    47783 Sep  7 16:19 pg375.png
-rw-rw-r-- 1 sfmqrb sfmqrb   100033 Sep  7 16:28 pg377.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67102 Sep  7 16:30 pg378.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87463 Sep  7 16:38 pg379.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79597 Sep  7 16:42 pg380.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75771 Sep  7 16:40 pg381.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61185 Sep  7 16:44 pg385.png
-rw-rw-r-- 1 sfmqrb sfmqrb        8 Sep  7 16:43 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3120575 Sep  7 14:24 skeat1882.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2985742 Sep  7 14:25 skeatdli.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0022.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0158.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4676 Sep  7 14:29 sns_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   135853 Sep  7 14:30 sns_n157.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129673 Sep  7 14:30 sns_n159.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   113320 Sep  7 14:30 sns_n21.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb      341 Sep  7 13:46 s.py
-rw-rw-r-- 1 sfmqrb sfmqrb   116699 Sep  7 14:30 t1.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T20:44:10.444Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD pih\"; grep -n \"^pīh\\|^pih \\|pyh\\|tallow\" PHD_mackenzie.txt PHD.txt | head -20; echo \"=== PHD farbay\"; grep -n \"farbay\\|frab\\|plby\\|plbyh\" PHD_mackenzie.txt PHD.txt | head -20; echo \"=== PHD angub\"; grep -n -i \"angub\\|ʾngwbyn\\|honey\" PHD_mackenzie.txt PHD.txt | head -20; echo \"=== PHD panir\"; grep -n -i \"panīr\\|panir\\|cheese\" PHD_mackenzie.txt PHD.txt | head"
}
```


### [2026-09-07T20:44:10.551Z] TOOL RESULT

```
=== PHD pih
PHD.txt:325:farr-, v. xwarrah. Farrūbāģ [plwb(’)g] the first major Fire of Sasanian Eran, that of priests and nobles. farrox [plhw' | M prwx, N ~] fortunate, blessed, happy. ~ih: fortune, joy, happiness. filāsūfā [pyPswkp!y] philosopher. frabih [plpyh | (P frbyw), N farbih] fat, stout. Fradadafš [pldtpš = Av. fradašafšū-| the south-eastern continent of the earth. fradág [MHL < A mhr; ИРА! | N farda] tomorrow. frādahišnīh [pP dhšnyh] increase, progress. fradom [AWLA < Ar. !?wD; pltwm | (M prtwm)] first. ~th: first, beginning. fragan [plk?n'] base, foundation; origin. fragandan, fragan- [plkn-dn'} lay foundations. frahang [pl’hng | N farhang] education; knowledge. --estàn [-st?n!] school. frahanj-, v. frahixtan. frahist [p/h(y)st! | (M pryst)] most (superlative of freh), frahixtag [plhhtk' | N farhixta] educated, trained, skilled. frahixtan, frahanj- [plhhtn', pDhnc- | P frhynj-, N far~] educate, teach, instruct. framādār [рж?РЦ commander, ruler, chief. framān [pim^n! | M frmn, N farman] order, command; a minor degree of sin. ~-burdar [-bwlt?l | N -bardār] obedient, submissive. framāy-, ~išn, v. framüdan. framds [bl(?)mwš | M pr’mws, N farámos] forgotten. framošidan [plmwšytn'] = framuštan. framüdan, framāy- [plmwin', plm'd- | M prm'dn, prmy-, N far~] order, command. — $n: order, commandment. frāmuštan, frāmēš- [pl(?)mws-in' | M prhmwst, pr’mwi-, N fard~] forget. franaftan, *franam- [pinptn!, *plnm- | M prnpt, prnm-] go, proceed, depart. franāftan, franām- [pin!ptn!, pli m- | P fri m-] 1. lead, conduct, re- move, promote; 2. profess, propagate (faith). ~išn: removal, promotion, profession. frarast [p/”Pst'] a cubit (18 in.). fràrón [p lwn'] righteous, honest. ~ih : righteousness, honesty. frasang [plsng | N farsang) parasang (4 Roman miles).
PHD.txt:435:~igih : soldiering. lawzénag [lwcynk' | N ~ina] almond sweetmeat, marzipan. *lipi [/pyh] a minute (of arc).
PHD.txt:549:pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. pen [p(y)n'] mean, miserly, niggardly. ~ih: meanness. pérámoón [pyPmwn! | M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš [LOYN! < A I-‘yn; руї | = M, N ~] before. IpéSag [py$k! | N péfa] trade, craft; guild, caste. *pēšaģ [pysk'] limb, member, part. pëššánig [pyš”nyk! | N pēšānī] forehead. pēšār [py | M py?r] leader, guide. ~ büdan: be guilty (of), commit. pēšārwār [руло], v. pëšyàr] urination. péSémàl [руѓут?/, v. hamēmāl] plaintiff. ~ih: prosecution, pēšēnīg [pysynyk! | (M pysyn(g), N pésina)] former; foremost, noble. pëš-gāh [pyšg”5 | N ~) audience chamber; foremost seat. pēš-kār [py$k'/ | N ~] servant. pēšēbāy [byš')wp?d | M руйору, N péfwa] leader, vanguard. ~th: leadership. pēš-pāraģ [pyšp*/k! | N —a] an appetizer. pēšyār [pyšk”/ | N ~] urine. petit [pytyt! = Av. paitita-] penance. ~ig [-yk'] penitent. ~igih: penitence. petyárag [p(y)tyd'lk! = Av. paityára- | M pty’r, N patydra] evil, mis- fortune; adversary; astr. detriment, ~th: (onslaught of) evil. рі [AB' < А "bur р(у) | M pyd] father. *pid [5(5)!! | P pyd] meat, flesh. pidar [AB Ytl, v. ipid ; ру | M pydr, N ~] father. pih [pyhw'] food, victuals. pīh [TL BA = A trb; рур | N ~] fat, tallow. pil [py] | M pyl, N ~] elephant; (chess) bishop. --bān [-p’n' | N ~] elephant-driver.
PHD.txt:555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
PHD.txt:576:Sabixón [špyhwn'! | N —xün] night raid.
PHD.txt:3932:tallow pih.
PHD.txt:4628:pih iva ]
PHD.txt:4744:pih YO е
PHD_mackenzie.txt:2284:frabih [plpyh I (P frbyw), N farbth] fat, stout.
PHD_mackenzie.txt:3388:*'1ipi [lpyh] a minute (of arc).
PHD_mackenzie.txt:4233:pih [pyhw ' ] food, victuals.
PHD_mackenzie.txt:4234:pih [TLBA = A trb); pyb IN....,] fat, tallow.
PHD_mackenzie.txt:4297:rabih [lpyh I M rbyh] noon, midday (heat).
PHD_mackenzie.txt:4737:Aabixon [lpyhwn ' I N -xun] night raid.
PHD_mackenzie.txt:7749: tallow pih.                              thing tis, (cis), xir.
=== PHD farbay
PHD.txt:325:farr-, v. xwarrah. Farrūbāģ [plwb(’)g] the first major Fire of Sasanian Eran, that of priests and nobles. farrox [plhw' | M prwx, N ~] fortunate, blessed, happy. ~ih: fortune, joy, happiness. filāsūfā [pyPswkp!y] philosopher. frabih [plpyh | (P frbyw), N farbih] fat, stout. Fradadafš [pldtpš = Av. fradašafšū-| the south-eastern continent of the earth. fradág [MHL < A mhr; ИРА! | N farda] tomorrow. frādahišnīh [pP dhšnyh] increase, progress. fradom [AWLA < Ar. !?wD; pltwm | (M prtwm)] first. ~th: first, beginning. fragan [plk?n'] base, foundation; origin. fragandan, fragan- [plkn-dn'} lay foundations. frahang [pl’hng | N farhang] education; knowledge. --estàn [-st?n!] school. frahanj-, v. frahixtan. frahist [p/h(y)st! | (M pryst)] most (superlative of freh), frahixtag [plhhtk' | N farhixta] educated, trained, skilled. frahixtan, frahanj- [plhhtn', pDhnc- | P frhynj-, N far~] educate, teach, instruct. framādār [рж?РЦ commander, ruler, chief. framān [pim^n! | M frmn, N farman] order, command; a minor degree of sin. ~-burdar [-bwlt?l | N -bardār] obedient, submissive. framāy-, ~išn, v. framüdan. framds [bl(?)mwš | M pr’mws, N farámos] forgotten. framošidan [plmwšytn'] = framuštan. framüdan, framāy- [plmwin', plm'd- | M prm'dn, prmy-, N far~] order, command. — $n: order, commandment. frāmuštan, frāmēš- [pl(?)mws-in' | M prhmwst, pr’mwi-, N fard~] forget. franaftan, *franam- [pinptn!, *plnm- | M prnpt, prnm-] go, proceed, depart. franāftan, franām- [pin!ptn!, pli m- | P fri m-] 1. lead, conduct, re- move, promote; 2. profess, propagate (faith). ~išn: removal, promotion, profession. frarast [p/”Pst'] a cubit (18 in.). fràrón [p lwn'] righteous, honest. ~ih : righteousness, honesty. frasang [plsng | N farsang) parasang (4 Roman miles).
PHD.txt:1889:fat (a.) frabih.
PHD.txt:3832:stout frabīh.
PHD.txt:4660:frasp Q3» o parist- - юз? o paristār ` тез? Ф paristidan ure» e» o paristog/k 181 үел%о› paristagih ASS dv paristag \% vead o paristišn TOUR o frabih ^ > v
PHD_mackenzie.txt:2284:frabih [plpyh I (P frbyw), N farbth] fat, stout.
PHD_mackenzie.txt:6560:fat (a.) frabih.                           fitldable windisnig.
PHD_mackenzie.txt:7686:stout frabih.                              suffering (a.) dardomand.
PHD_mackenzie.txt:8634:frabih                    -"\)~q)          fr6dmand               J~yD~4>
=== PHD angub
PHD.txt:172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
PHD.txt:212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
PHD.txt:439:~ith: femininity. *madag [mtk' | (M myg, N māya)] essence, substance. ~ig [-yÀ!] essential. ~war [-w/] essential, especial, principal. madan [mtn! | M mdn] come. madār [т comer. mādar [AMYtl < А т-у; mtl | M mdr, N ~] mother. imādayān [m!tgd?n! | М m'dy'n] book. *mādayān [m tyd?n'] essence, basis, core; essential, chief. mādayār [m tgd’l] steward; (chess) rook, castle. mādišt [m’tyst'] *matter, protoplasm. mādīyān [m’tyg?n | N ~] mare. may [my | N ~] hole, pit. magas [mks | P mgs, N ~] fly. ~ i angubén: honey-bee. magind [mkn'd | M mgyn(d)] shield, protection.
PHD.txt:961:bee magas i angubén.
PHD.txt:2303:honey angubén; ~-bee magas i angubén.
PHD.txt:5470:gabrih anguben! gowiin
PHD_mackenzie.txt:878:   afrosag [)p/wlk l I N - a] a sweetmeat made of flour, butter, and honey.
PHD_mackenzie.txt:1103:anguben [DWBSYA < A dbs; )ngpyn' IN angubin] honey. lJ}~) ~""~...
PHD_mackenzie.txt:3412: ....... i anguben: honey-bee.
PHD_mackenzie.txt:6041:bee magas i anguben.                        bitterness taxlih.
PHD_mackenzie.txt:6772:helmd targ.                                    honey anguben; ,..,-bee magas
PHD_mackenzie.txt:6773:help (n.) ayarih, dastyarih, frayad,              anguben.
PHD_mackenzie.txt:10799:                                                        angubcn[
=== PHD panir
PHD.txt:540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
PHD.txt:1212:cheese panir.
PHD.txt:4705:рапа, (пет!) poy- penih pus | frazand frazandih panir pondik pēyišnīg pad!, pen padgohr padnérog
PHD_mackenzie.txt:4012:panir [pnyil N -] cheese.
PHD_mackenzie.txt:6160:carpenter durgar.                       cheese panir.
PHD_mackenzie.txt:8731:purr-rawisnih   ~~)~,v                        panir                          '\...ICU
```


## [2026-09-07T20:44:21.695Z] TOOL CALL #17: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg385.png"
}
```


### [2026-09-07T20:44:21.721Z] TOOL RESULT

```

```


## [2026-09-07T20:44:37.388Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"##### HRN leaf 102 (p.81)\"; awk 'BEGIN{RS=\"\\f\"} FNR==103{print}' HRN.txt; echo \"##### HRN leaf 202 (p.181)\"; awk 'BEGIN{RS=\"\\f\"} FNR==203{print}' HRN.txt"
}
```


### [2026-09-07T20:44:38.620Z] TOOL RESULT

```
##### HRN leaf 102 (p.81)
— 81 —
aw. *paiti' -p l/^mö- ; phlv. patmay^d (AV.), patman,
patmänih^ patmänak 'Mass'.
kurd. piwdn messen; wa/. piHmiHam 'nachahmen,
nachmachen' (?).
)4. peiwesten ^vorbinden', Praes. peitvend-em, peiwend,
aw. "^paiti- 4- \/hnfid' (s. No. 219) ; phlv. patwastan,
patwand Band*.
kurd. pevandn *kleben .
55. plh *Talg, Fett', ^S (Is. 1, 11); vergl. ferhih (No. 813).
ap. ^pi^u-; aw. pitu- 'Speise*; phlv. pxh bezw. pih;
ai. pitü'. Vergl. np. ferbih (No. 813).
aw. pjvah' ^) 'Fett'; ai. pfvas- *Fett, Speck'; kurd. ptü
'Talg (ZDMG. 88, 57); oss. d, ßti, t. fite Tett, Speck'
(289); bei. pT<j, n. pty (298); wa/. j>7/ 'Biestmilch'
dagegen gehören zu paz. j>^y (lies piy) *Fett' (West,
Sik. gura.-Glossar) , das aus *pivaka' entstanden ist
(vergl. Hörn, KZ. 32, 584 No. 17).
T.
)6. tä *bis; damit*.
phlv. ^öi6(?), Hs. tai oder tag, vd. 3 (136) (Thon-
nelier; Spiegel 11), päz. afi]dak, an\dd (phlv. 11).
kurd. da 'damit' ; bei. da\l7i, da[m, da[n/{ö 'bis jetzt,
noch* (73).
17. täj 'Krone*, täjver,
arm. LW. fag, fagavor.
Hat mit ap. Yauna takabara nichts zu tun; und
ebenso wenig mit assyr. agü 'Krone' (nach Jensen,
mündliche Mitteilung).
de Lagarde, Nachr. GGG. 1891, 160 folg. stellt
np. Täßk, Täzik, TäzT f Ureinwohner Persiens, die
weder Araber noch Türken sind' (vergl. phlv. Tajik
(Bund.), arm. Tacik 'Araber), taziyüne 'Peitsche'
*) Aw. pivasca steht neben *pivo (ohne nachfolgende Enklitika)
e starewcä neben stärem (Burtholoniae, Handbuch § 69 Anm. 2).
Hörn, Grundrisg d. noup. F^tyniolugio.
##### HRN leaf 202 (p.181)
— 181 —
811. ferüx Vorwärts, aufwärts; offen' etcJ).
aw. frq^ Vorwärts' (schw. St. ^frac-^ vergl. N. pr.
FrOdi/a-); phlv. fräd- (päz. fräz^ frfl^); ai. pränc-
(schw. St. präC') ^vorwärts*.
oss. räzäi Von vorn* etc. (210).
812. feramöS Vergessend; Vergessenheit', ferämus^ fera-
muSt^ fer(a)mösiden (Vis und RämTn, S. 50 V. 13).
ai. pra + |/';/?«rs-, ////ifya^c Vergessen' ; y\\]w , framös
bezw. farmös^ framöst^).
bei. samusag, samDsay, n. samusay^ Samösay Ver-
gessen (361), mit anderem Pracfix.
813. ferbih, ferheh^ ferhl (d. i. "^ferhiQi)) 'fett'. Vergl. np.
pih (No. 365).
aw. frapi^wa- 'Voizug, first-rate' (Geldner, Ve-
dische Studien 11, 17iJ)'^); phlv. frapili hi^zw. farpfh;
ai. prapitüd' (vergl. Geldner a. a. (). 155 folg.).
LW. wa;^. farhl^ sar. farhe,
Jüd.-pers. HO*!^ (Is. 17, 4) geht auf ein ap. *//(/-
2)itU' zurück.
814. ferjätn *Ende\
ap. ^frajäma- {{^gani- 'gehen*); \)\\\v, frajäm bezw.
farjam 'Ende', frajämtnltany vergl. fraj(a)ftan (AV.,
jung in Kolophonen. Siehe No. 113).
815. ferxane V^eise, gelehrt*, ferzanegl.
ai. pra + [/^./aw- , jafiäti- 'erkennen , verstehen' ;
phlv. frazänak bezw. farzänak,
Vergl. dänisten (ar. l/iaw-), No. 534.
816. ferzend 'Spross'. sowohl *Sohn* als auch 'Tochter (N'is
und Kämln, S. 22 V. 4, 5 v. u.).
aw. frazainti' 'Nachkonimenschalt*; phlv. farc^attd
bezw. frazand.
*) Vergl. Dar mestcter, Et. ir. IT, 112 foli^g.
*J Nach den arm. LW. hraman^ hrasak, hrahany zu sclilicsson,
scheint im Pehlevi noch /ra-, nicht schon far- gesprochen zu sein.
Das Päzend lässt beide Möglichkeiten offen.
'j Justi' Thema /raj9J/M- *Füllc' rauss also fallen.
```


## [2026-09-07T20:44:49.486Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT pitu\"; grep -n \"pitu-\\|pi&wa\\|piθwa\\|pi\\\\\\\\wa\" BRT.txt | head -30; echo \"=== BRT payah\"; grep -n \"payah-\\|pa&man\\|paēman\\|paeman\" BRT.txt | head -20"
}
```


### [2026-09-07T20:44:49.565Z] TOOL RESULT

```
=== BRT pitu
=== BRT payah
5886:•  j.  aspya-payah-  n.  'Pferdemilch':  dakmd huram  (sd.)  :i^araili  maoB  *°ya»Al>'^  N._J0.
14796:•  j,  'paeman-  Adj.,  nur  fem.  'mat/iT- 'säugend',  von  der  HUndio;  gatwqm  , . pu^raca  (sd)  'mainiea  V./5.  49.
14798:•  j.  "paemanyo  vs  Vyt.  13.
15266:■payah-
15285:•  j.  'payah-  n.  'Milch',  auch  Plur.:  *'yB F.  10  i  —  nsit  *yB  fsuta  (sd.) , .  toit  gstd . . ^■7-  77;  —  aipi.yiaurvatqm  aspayanqm^a °yar3hqm  gävayanamcä  malsinatiqmca  buz- yanqmla  hqm.vaoirinqm  la.vaoirinqm  V. 5.  5a;  —  rafu/ris  *°ySbls'^^  sfastiisca a:^ästäisca  N.57.  a)  mit  'tütrya-  Adj. 'Molke':  taitya  (sd.)  paya  bavat  aspa- yüaiea  *'xaraySaJ/a  "die  Molke  kann  von
15288:*payah-
15295:•  j.  'payah-  Adj.  '(milchend,  Milch  sva.) Saft  gebend,  schaffend"':  maiaydizarf- ma^tt  {sd.)  'yanhim  Vr.  2.  2;  —  mailySi- zanmayehe  'yatths  Vr.  /.  2.
18181:•  j.  Frä-payah-  m.  Name  eines  Bergs  oder Gebirgs:  ahmai  haia  garayS  fi-aex^an  .. baranas^a  'yäs^a  gairif  Yt  ig.  6.
18275:•  j.  frä.uruzda-payah-  Adj.  'dem  die Milch  verhalten  ist,  was  keine  Milch  (zum Säugen)  hat',  von  weiblichen  Tieren:  pa- ssu?  ganbus  yDütahe  (sd.)  °yai>ks  A.3.  3.
29053:•  j.  bafatpaeman-  Adj.,  nur  fem,  'maul- 'die  Milch  (zum  Säugen)  bekommt':  ifrt- naomi  hwqm  hacat.fti^rqm  'tnaiiyqm (ASf.) "  "ich  will  schaffen,  dass  du  schwanger wirst  und  Milch  bekommst"  V.  21. 6.
```


## [2026-09-07T20:44:56.967Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Speise, Nahrung\\|'Speise'\\|Nahrung'\" BRT.txt | head -20; echo \"=== search pi.wa\"; grep -nE \"\\bpi[^a-z]{1,2}wa\" BRT.txt | head -20; echo \"=== dus.pi\"; grep -n \"dus\\.pi\\|du§\\.pi\\|dus,pi\" BRT.txt|head"
}
```


## [2026-09-07T20:44:57.737Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD apt meat\"; grep -n \"'meat'\\|meat\" SOD.txt | head -30"
}
```


### [2026-09-07T20:44:58.310Z] TOOL RESULT

```
11656:•  g-i  j-  J^iää-  f.  'Erquickung,  Nahrung': .  .  iahm3ictt  hätqm  °sqin  vahihqm  adä (sd.)  ubdibya  akübyä  Y.J5.8;  —  benützt; kätqm  yastum  ctnasti  yaha  ha%bls  "sam "iäiqm  bezieht  sich  auf  das  Gebet,  inso- fCTn  es  zui  Erquickung  der  Seienden  dient" Y.  a/.if.'>
16360:•  j.  pitav-  m.  'Speise',  insbes.  feste,  'Fleisch- speise': yim  (näml.  azim)  upairi  kirssaspB .  .  °täm  pacata  ".  .  sich  (Reise h) speise kochte"  Y.().  11;  —  'tum  F.  jo,  *N.ö'7'J;
=== search pi.wa
12079:Bildung  wie  iari.zaairä.;  vgl,  /iaeli./ara-.  — ai.  vgl.  iar6ddzi}as-  Adj.  —  ")  Nach  der fl-Dekl, t^d  (wieder)  verschafft,  heimlichWasserj.j,  tarö.piS-wa- i)  Adj. 'der  ungenügende aad  Kraut"  V.  75. 10;  9',  s)  Praen.  mit  |  Nahrung  hat,  bekommt,  Mangel  anNahrung Akt;  a)  'durch  -  hin,  über  -  hin,  über  l^xditV:  yff  spätum^'^wim^dasH yim  pasus.- -  hinw^,  hinaus';  o)  räumlich:  husi^m  \  ^aurum  "wenn  einer  den  Hund  ,/*.  an f^sm  ra^aya  TS  . .  vilanuhaitm  Yt  5,  [  Nahrungsmangel  leiden  lässlf'  V.  13.  20, '•r,  ?8;  —  hrTs'^J  'rff  pir>tamcit  h!  urva- 1  24;  20.  2)  n.  'ungenügende  Nahrung, »■  ..frqparaymi  Y./5.6;  7J.  i6,  Vyt.|  Nahrungsmangel' (?):  paiH  'w>m  daidyat •fc>  Nik.2;  —  mtknm  .  .  yS  paeiryö  'r3\yai:a  . .  Vytß  (?);  —  *Vf^  N.  13  (?)". **■«   asnaffUi     Yt  10.  13;  V.ltj.jo;   — |      I'ü,  (lu  Vyt.h  lar  i'ariin,(ra'S.):  *tar  fihn'\
13344:73 1  däityö.piS'wa-
14635:•  j,  *ri-pi9Twa-  Adj.  'der  drei  Mahl- zeiten bekommt':  *'w5  *al  asti  ätarl ahurahe  ma^äa  hama  bipi^ws  aiwigSme
17282:•  j.  bi-piSTwa-  Adj.  'der  zwei  Mahlzeiten bekommt';  ^än^iäwif  (sd.)  *el  asii  ätars .  .  iama  '%w3  aiwi-gäme  F.  25b.
17659:•  j.  fra-piÖ-wa-  Adj.  'in  Fülle,  reichlich vorhanden,  copiosus':  äat  paslaSta  ahe nmStiahe  'viS  gaul  "dann  ist  in  diesem Haus   reichlich  vorhanden  das  Rind"  V.
18492:•  j.  haarvS^^pass  fraSa^shH  naemö.- "piÖTwa  tara%ustrS  N.  64.
=== dus.pi
```


### [2026-09-07T20:44:58.354Z] TOOL RESULT

```
=== SOD apt meat
16532:meat 
39543:fish-meat 
82017:meat,  flesh 
82079:meat  production 
82167:meat,  flesh 
89617:fish-meat    4809 
91649:meat     1355,  10908,  10927 
91650:meat  production     10915
```


## [2026-09-07T20:45:10.123Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '82010,82025p;82160,82175p;16525,16540p' SOD.txt; echo \"=== grep entries 1355 10908\"; grep -n \"^ *1355\\| 1355 \\|^ *10908\\|^ *10927\" SOD.txt | head"
}
```


### [2026-09-07T20:45:10.187Z] TOOL RESULT

```
spilling 

GMS  957,  1168  n  1;  Hen.  Magi.  143.18  n  1 

1355  >pt-  B,  M  o^/ 
op(a)t,  (a)pat  ?  ©Av.  pitu  ^ptyw'r 

meat 
GMS  170 

1356  >pt>r-  B  {j^:J^S)(y>)d^ 
(o)ftor  ?  =*ftr-,  ptr-5 

OcOpulI  ouiihair) 

SCE  88;  Hen.  Magi.  143n4;  GMS  89 
yat  ©<hyah  *ah-  ©3sg.  opt.  ^x-1 

GMS  768;  BBB  plOl  el2;  KG  2330;  AVS  225 

10908  y't'k   B  cJ^/ 
yate   ©Yaghn.  yota  ^yHy 

meat,  flesh 

VJ  805;  TSP  p277;  SCE  377,  270 

10909  yVk  ywVy   B  *        j^c 
yate-xware  ©pres.  part.  *±y}tyv/}T*k 
carnivore 
SCE  239 

856.26:  C2,  23R26,  TSP  7.150 

10926  y'twkyh    B  =»  y>twqy) 

10927  y'ty   M,  C,  S  c^/ 
yate  ©ace.  y}tw  ^y^'k 

meat,  flesh 

BBB  p57,  499,  762;  Hen.  Tales.  476.17;  STi 
55.19;  C2,  94V3,  105R8;  Frag.  Len.  25.3 

10928  y»wr  B,  M,  C  c^iJuiam 
yawar  ©Parth.  y}wr  ^'ny'wr 

time,  occasion 
=== grep entries 1355 10908
16529:1355  >pt-  B,  M  o^/ 
34995:VJ  1355 
82014:10908  y't'k   B  cJ^/ 
82164:10927  y'ty   M,  C,  S  c^/
```


## [2026-09-07T20:45:10.843Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD_pages leaf 108-109 (p42/43)\"; awk 'BEGIN{RS=\"\\f\"} FNR==109{print}' SOD_pages.txt | head -60"
}
```


### [2026-09-07T20:45:48.294Z] TOOL RESULT

```
=== SOD_pages leaf 108-109 (p42/43)
                                                                                                                                    'ns'yp-



 43

       ready                                                                        snare, trap

       TSP 7.79, 134                                                                TSP 2.275; S W,C2, p!79.4
                                                             ■i^'j'j'j
 1085 >ns>kcyk B                                                               1098 'nsp'kh's                                     J^.^J
      ansakcik                                                                      anspak ^nsp'kh, fsp*
                                                                                    carpet, rug
       suitable
       TSP 6.187 n p205                                                             TSP 13.7; Bcnv. >nsp>kh, "equipment"; S W, IIJ
                                                                                      1976, 54, 56; STSC 13
 1086 »ns»k(y)        B                 ( jU^)jO jU o'j'>^ 'v*'^
                                                                               1099 »nsp»nh ? S                       l#oi^<4*;OLr-
       ansak(c) =^ns*k, Vq
       suitable, fitting                                                            a(n)span ? ^'sp'nh ?
       BSTBL, Dhu. 37; TSP 23.11; Frag. Lcn. 23.4, 7.75;                            compensation
         ob. -y(hh TSP 2.420, 6.130 n pi 75                                         MDii p22 V16; Gcrsh. Advice. 91 n 39

 1087 'ns'rty B                                                               1100 »nspst»ky*kh   S =* ^spstqy*
      ansartc *=»srt
                                                                              1101 'nspstqy* M       {^jJ'^j^j^c^lJ^^jZ.
      cold, cooled
                                                                                   anspastakya Onspst'ky'kh) ^spstky*
      SCE 103                                                                      zeal, willingness to serve
 1088 >ns>\vr     B                                                                GMS 338; W-Lii; BBB; Sogdica. 3; KG 490,
                                              swr
      ansur Onswr) ©s^as-; Oss. ansurd                                                -y>kh, 612; S W.IIJ 1976, 57n61
      G'vory)tusk                                                             1102 *>nspt- ? S                              jju^^U-^
      VJ; Bailey. BSOAS 23, 28 n6; Prolcxis. 407                                   anspat ©impf. mnspt

 1089 Wwr'k     B                                                                   0o)risc, (rc>)bccome active
                      ( juU^ ^ j,t jj)^y ^txj* <jh^y
                                                                                    Rust. TSP 13.25 n p226; S W, IIJ 1976, 55, 57n61;
      ansure Onswr'k, 'nswr'y, 'ns'w^y)                                               Bcnv. mnspt
      with tusk
      VJ passim.                                                              1103 >nsr B                                          ^ j&
 1090 »nsWy       ** 'ns'wr'k                                                       ansar
                                                                                    headless
 1091 'nsWpr'k   B                                                    Ji^           TSP 9.133
      ansur-pare                                        jj^Ipo'^U y
      with tusk                                                               1104 >nst S                                           9^
      VJ 68, ~vv                                                                   crowd ?
                                                                                    Rust. TSP 13.9; Gcrsh. apud. S W, IIJ 1976 p59;
1092 Wwrprch              B
                                                                                      Bcnv. yyst
      ansur-f3arc         ©f. adj.
      with tusk
                                                                              1105 'nswr => 'ns'wr
      VJ65
                                                                              1106 'nswr'k => 'ns'wr'k
1093 Wych         S                                                 iQ}j*»
                                                                              1107 'nswr'y => Wwr'k
      ansic Onsytch) ©f. adj. =vnsy-
                                                           6«UlU<
```


## [2026-09-07T20:45:58.160Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'\\b1355\\s+.pt-',p) or re.search(r'\\b1354\\b',p) or 'brpyg' in p or 'brpy' in p and 'fat' in p:\n        print('LEAF',i,'printed~',i-66)\n        print(p[:3000])\n        print('======')\nEOF"
}
```


### [2026-09-07T20:45:59.807Z] TOOL RESULT

```
LEAF 118 printed~ 52
                                                                                                                      ?p\v "stnyh

  53

                                                                     1353 'psys'r S                             o~r"a~i
 1340 >ps'y-      B                       ^UIjjjo^c"
        opsay =»>ps*y-, ps}y-                                              3p(o)se-sar ©<*pasa~ka- sar ^'pysys'r, psys'r
        (rc)rcject,(/o)throw                                               then, afterwards
                                                                           GMS 373; KG 520; Frag. Len. 37.3
        TSP 2.1083, 3.71, 167, 169; inf. ->y, TSP 3.177
                                                                     1354 'psyyk M                                     6xy^ <*juil
 1341 'ps'y's'y => 'pfcr'y-
                                    ei^*ijO«                              op(o)sik
                                                                          spilling     Opsyk)    =*ywxn> >psyyk
 1342 'ps'yn'k    B
                                                   k ^-JJ,J fU
        opsene                                                            GMS 957, 1168 n 1; Hen. Magi. 143.18 n 1
        (name of aXlr't?
                                                                     1355 >pt- B, M                                           o^/
        TSP 3.66 n pl94
                                                                          op(a)t, (a)pat ? ©Av. pitu ^ptyw'r
 1343 'ps'ynt B
                                             (js-i.JI^L^JaS               meat
      opasint ©<OP       paisya ©pi. ?                                    GMS 170
        pieceCO                                                      1356 >pt>r- B                       {j^:J^S)(y>)d^
        TSP 11212, '/tfy/u yy/i/jSW,       C2 p59.11-2
                                                                          (o)ftor ? =*ftr-, ptr-5
 1344 >pskr- B                                      o^/JU                 OcOpulI ouiihair)
      op(a)skar ©<*apa-skar         =»*pskr-, pskyr-,                     SCE 88; Hen. Magi. 143n4; GMS 89
                                                                     1357 'pt'yn'kCw) S                                      ^/
       OcOpcshkars-c
                                                                          (o)patcnc Optynyy) =>ptyny(y)
       SCE 54; AVS 103
                                         ?(-ufU^)Js*ii0ij                 (made <9/)fIesh
 1345 'psm'kntyh S                                                        GMS 170;KGpl79, 380-2, -w
      opasmagande ?
      wool-stuffed saddle ?                                         1358 'ptyw'r B                                      Jy~^/
                                                                          opat-xwar ^'pt-, ptywr-
       MDiii p74 n 1; MDii, "psrrikntyk Mack. BSTBL                       carnivorous, flesh-cater
         n p60

======
LEAF 187 printed~ 121
                                                                                                                            122
     bznqVqy*

            'Pjng'ry                                                      how, what, how much
          sinful, evildoer                                                GMS 1312, 1582; VJ 1100, cVry, VJ 825
          STii4.28;C2, 69R17                                         3110 c>-                                                 jl
     3098 bznqVqy' C                      Ojl^- ialo    <^J^A^
                                                                          ca-     (cy) ©<*haca ©encl. prepos.     ^c'm'kOO,
          P(o)zangar(o)kya                                                   c^klh), cKvysn
          sinfulness, wickedness                                          of, from
          C2, 11V21                                                       GMS 1610-21
     3099 bznqVy => bzng'ry                                          3111 cJp B, S               (uys >^     j^jjjjbtx^-ijjM*-
     3100 bznq'ry1 C                   ^>J^A '^J^       <l? J^y.          caf ©indecl. adj. & adv. ^c'f
          (3(o)zangarya     ^bzng'ry                                      how many, how much, as much as
          wickedness                                                      GMS 1540; EGSii 160; TSP; VJ; MDii; MDiii;
          C2, 40V 6 n p85                                                  MSP
                                                                    3112 c'p* S                                        y jUy
     3101 pZ\vt-       B           :     j&j^SjSiQX^Jjj
                                                                          cafa    ©<haca-0wa    ? ©prepos. + 2sg. pers. pron.
          (3(o)zut ©pi. st. =»Pz>w-
          {to)gio\\f
          TSP 6.175
                                                                          (of)you
                                                                          GMS 437 n5, 1354; Hen. Talcs. 474
     3102 pZyk     S                                        <L$*

          Pozik -^Pz'yk, bzyq                                       3113 c^kCh)      B.S                                j jl,y
          hardship
                                                                          cafak    ©prepos. + 2sg. pcrs. pron. =*c>-
          MDii Pzykw A14, 19                                              (<?/)you
                                                                          VJ 1406; KG 518, 566; MDii, Nov. 4 R5 etc.;
§    3103 bzyq     C
          P(o)zik ©pi. -/ =»Pzyk
                                               ^S*jJj iOPtyJU iJv
                                                                            GMS 1354; c'filc, MDii B-17R2 etc. MDiii B3,
                                                                            7
          bad, evil
          C2 gloss.; Sund. AoFviii 1981 p214                        3114 cJp c>p B,S               
======
LEAF 575 printed~ 509
      509
$
     so fed up 9845                           so strong    9909, 11213
     soft 9660, 9661                          so stronger     11214                    (to)spit  4294
                                              so that    5170, 5266, 9834              spitting   10879
     softly 9661                                                                       splendid    95, 701, 731, 1432, 2089,
     Sogdian    8761, 8763, 8764, 9037,       soul    1030, 1513, 4278, 8546              10497, 10822
       9038, 9039, 9079                       soul-lover     3976                      Splenditenens     2105, 10672
    Sogdian family name     183               soul-service   8548, 8550                splendour     483, 702, 732, 733,
    Sogdian prince   3805                     sound    2151,3569,4599,4601,               1429, 2090, 2462, 3918
    Sogdians    9041                             10097, 10109, 10258
                                                                                       splenic      8907
    soil 4438, 10633, 10751                   so unhappy     9790                      0<?)split     4627, 4698, 7922, 8078
    sold   6927                               source    4048, 4049, 10607, 10608
                                                                                       split-minded     5192
    soldier    337, 338, 1594, 2342, 88 77    south    2701, 3880, 6277, 6278, 6279
                                                                                       splitted   1113
    sole 2851, 6614                           south wind     3659                      (to)spoil   2761, 3877, 3912, 3913,
    solicitude     10777, 10849               sovereign     5727, 8684, 8685             6313, 6327
    solitary     11076                        sovereignty     8687                     spoiled   5816, 6331, 10078
    so long     7152,9842                     (to)sow    835, 836, 4905, 4916,         spontaneously     6784
    so many      9772, 9804                     4919, 5105, 6967                       spread    7082, 7083, 10235, 10786
i   somebody       36, 39, 56, 665, 2161      sowed     6969                           OcOspread     7028, 7081, 7086, 7091,
    something       30, 40, 45, 370, 371,     sowing   836, 4923, 4930, 6965             7231, 7232
       372, 624, 642, 2149, 2157, 2158,       sown   4918
                                                                                      spreading    677
      2159,2160                               space     133, 134                      spring    10185,10608
    sometimes       2442, 2445                spade   9696                            Go)sprinkle    6500, 7496, 7537
    so miserable       9790
                                              span   10341                            sprinkler    7538
    so much     3216, 9776, 9778, 9780,       Spandarmaz         8895                 Spritus Sanctus       11379
       9786, 9804, 9808, 1010
======
```


## [2026-09-07T20:46:06.747Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"##### leaf 175 (p~109)\"; awk 'BEGIN{RS=\"\\f\"} FNR==176{print}' SOD_pages.txt | head -70"
}
```


### [2026-09-07T20:46:08.077Z] TOOL RESULT

```
##### leaf 175 (p~109)
                                                                                                                          110

 Prtpcxwnyh

 2775 prtpcxwnyh         M          ^y   ^ojluTJ-j*; ij^\&&y       2790 prwrtk ? S                       ^U «^</y f>r «»
      Part-pacxonc                                                       frawarte (prwrtk) ©MP         frwrdg ^frwrty1
                                                                         scroll, letter
      suffering contempt, humiliated
      BBB 687                                                            MDii p73.12

 2776 prtp5     B, S                                       .if 7   2791 prwy B                                       f*j<^J
                                                                        farwe ? =^prwy, frwy
      Pratpa5, Partpa5 (brtpd) =»frtp55, brdpd
      informed                                                           illusion
                                                                         BSTBL, Vim. 115; VJ 230; STii 7.32, 34
      MDii 1.1, 15; TSP 6.115, 16.23 n p205; STi 77.4;
        STii 1.67, 89; C2, 3V 7, 22R 11, 14 pl48.11;               2792 prwz-      B                                 0^j'j>,
        Bugut. Insc. B2.16                                               frawaz =>frwz-
                                                                         (ro)fly
2777 brtpd      C =* prtpS, prtpd
                                                                         GMS 329; AVS       132
2778 brtpdy'     C =* prtp5y>h
                                                                   2793 ♦prwz'n'k     B                              oU"-*U
2779 prtp8y}h M                  :                   jtU<j*lfl
                                                                         frawazane,
                                                                         bird, flying parwazane (brwz'ny)
     PratpaSya, partpa5ya        (brtpdyO
     information
                                                                         SCE 304; C2, 17V2 p58; Schwartz. BSOAS        1971,
      GMS     1405; C2, 12V6, 87R14; BSTii 878.14                          412
2780 prtp6y,kh S                                  ^b^lTF
     PartpaSya(k)                                                  2794 brwz'ny     C ==> *Prwz)n>k
     information, knowledge                                        2795 brxs- C                JiJ'^j < dzj'^j, *tf*-Mjj
     KG 471                                                             Praxs ©impf. byrxs ^pr'ys-, Pr'xs-
                                                                        (/<9)shoot, GcOrcIease
2781 brtp9 -» prtpd
                                                                        BTii 827.44; Benv. Eti 299; S W, C2, 94V 14 n
2782 prtwy B                          jt^ <j£j« <f Ij7
     Pratux, partux (prt'wy, brtwx) ©pi. -/                               p74, 176 C
       -^PrtVx                                                     2796 brxs'mnty                               v^   \*jIjuL*
                                                                        shooting
                                                                        praxsamande ©ace. -tw
      sure, tranquil

     BSTii 84211; Benv. Eti '323; C2, 68R11 p!48                         BSTii 892.20; C2, 31R20 +06
2783 brtwx   C => Prtwy
                                                                   2797 brxsqy'(-) C                       0->^V^>T '(JJ'^L*7
2784 brtwxt =* prtpd                                                    shooting
                                                                        Praxsakya ^prysky*
2785 brw      C =» bry
2786 prwVtn rwc S               jjj^jjJ "u ^ j> Jjj                      BSTii 892.18, 20; C2, 31R18-19; Gersh. IF 1970,
     frawartin roc ^prw'rtn rwc, frwrr                                    305
     nineteenth day of the month                                   2798 BRY S                                             ^
     MDiii p64
                                                                        son
                                                                        pise, zate ©ace. -vv; abl. ->; Idg.
2787 prw>y5-     B                          u*/>*^OJl-o
                                                                        MDii; MDiii; Frag. Len. 69.3; TSP 8.168
     frawe6 ©*fra-waid ? J~vid           ^prw'yS-,
       frwy5(5)-                                                   2799 bry C                                          ^.^
                                                                          Pryy
     (fo)reach, (to)hit, (research
                                                                        Pare    ©ace. -w; pi. -t\ ob. pi. -ty ^Pr'y, PrJk2,
     TSP 3.117; GMS 329; Gersh. AHM          p263 n; AVS
       115                                                              fruit
2788 prwm'yk S, M                                                       STi 21.14-, C2, gloss, brw, BSTi 113, 121
                                            ^^
     fromik
       frwmyq(prwmyk) ©pi ob. ~ty ^Pr'wmyn,                        2800 pry>(h)   M                                   ^U_^
```


## [2026-09-07T20:46:12.900Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"brpy\\|Brpy\\|βrpy\" SOD.txt SOD_pages.txt | head -20; echo \"=== fat\"; grep -n \"^fat\\| fat  \\|'fat'\" SOD.txt | head -20"
}
```


### [2026-09-07T20:46:12.966Z] TOOL RESULT

```
=== fat
11166:father 
16560:father 
24115:fatsr  ?  ©impf.   =*}ptyr-,  pt>r- 
25939:fat 
29045:fat 
32796:fater  (Ptyr-)  ©impf.  =»ftyr-2 
34080:fatart  ©pt.  st. 
34158:fatercik   ^n'ftyrcyq 
60406:father 
65606:fat,  oil 
69984:father  of  Sudashan 
74611:fat,  heavy 
74988:fathom 
88467:cow's  fat    4076 
89443:fat    2770,  3257,  8570,  9858 
89444:father    565,  1359,  7808 
89446:father  of  Sudashan    9184 
89447:fathom    9912
```


## [2026-09-07T20:46:17.746Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25925,25950p;29035,29055p' SOD.txt; echo \"==== leaf 174 (p~108/109)\"; awk 'BEGIN{RS=\"\\f\"} FNR==175{print}' SOD_pages.txt | grep -n -A6 \"2770\\|2769\\|2771\" | head -40"
}
```


### [2026-09-07T20:46:18.981Z] TOOL RESULT

```
womb 

STi  86.13;  GMS  1090 

2769  prpt-   S  a^-o^  <jx>J 
Prpat  ?,  frapat  ? 

tumble 

Mack.  AI  424,  8 

2770  prpyy  S  (^-»4=4^>r 
farpix  ?   ©Av.  pivah  Pahl.  farbih 

fat 

MDii  p32  n  20 

2771  *5rt-   B,  M  {jy>  ^^  j->)CpjjT  <o^ 
Pn,  pa/art   (brd'r-)  ©<*brta   **Pr-,  Pwrt- 
(/6>)bring,  0o)carry,  0o)bear 

GMS  592,  trans,  pret.  firtw&r-,  KG  635 

2772  prt*wY  =*  Prtwy 

skinworker 
Sogdica.  54.5 

3256  crmny   C 
carm(a)ne  ©pi.  -t 
(made  <?/)skin 
BSTii  90523;  C2,  57V23 

3257  crp   B 
carp  ©ob.  -y 
fat 
TSP  2.372 

3258  crpYwfin   B 
carp-Yo5an 
ointment 
TSP  3.171  n  pl97 

3259  CRWRH   B  ->  CWRH 

3260  crxwst   C 
==== leaf 174 (p~108/109)
35:       frakrand (frkr'nt-) ©<*fra-krnta         -»0rkst-,        2769 prpt-    S                              a^-o^ <jx>J
36-         frkrnd-                                                       Prpat ?, frapat ?
37-       (fo)cut in pieces                                               tumble
38-       TSP 2.159; GMS 145; AVS 112                                     Mack. AI 424, 8
39-
40:2758 prkst- S                                                    2770 prpyy S                          (^-»4=4^>r
41-                                               b*j><o*£*j>-
42-     frakast ©pt. st.                                                 farpix ? ©Av. pivah Pahl. farbih
43-     (ro)cut in pieces
44-                                                                      fat
45-     GMS 601; Hen. JRAS 1944, 137.7                                   MDii p32 n 20
46:2759 brqy> C                                                ^    2771 *5rt- B, M                 {jy> ^^       j->)CpjjT <o^     rj
47-     Par(a)kya =*8b}rqy\ bznbrqy*                                      Pn, pa/art (brd'r-) ©<*brta **Pr-, Pwrt-
48-                                                                       (/6>)bring, 0o)carry, 0o)bear
49-       gift 29.5; STSC 113; C2, 57V 13: BSTii 905.13
50-       STi                                                             GMS 592, trans, pret. firtw&r-, KG 635
51-2760 prm>y-     S                                 j^j            2772 prt*wY =* Prtwy
52-       framay   ©impf. flr^rriy =*frm>y-, prnVy-1                2773 prtVx B, S                         ^L^ <juLa <f IjT
```


## [2026-09-07T20:46:35.024Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"honey\" SOD.txt | head -20; echo \"=== leaf108\"; awk 'BEGIN{RS=\"\\f\"} FNR==109{print}' SOD_pages.txt | head -5"
}
```


### [2026-09-07T20:46:36.315Z] TOOL RESULT

```
14594:honey  4 
90457:honey     1066 
=== leaf108
                                                                                                                                    'ns'yp-



 43
```


## [2026-09-07T20:46:42.030Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14580,14605p' SOD.txt; echo \"=== leaf107 = p42\"; awk 'BEGIN{RS=\"\\f\"} FNR==108{print}' SOD_pages.txt | grep -n -B3 -A8 \"1066\\|1065\\|1067\""
}
```


### [2026-09-07T20:46:43.467Z] TOOL RESULT

```
TSP  2.159;  SCE  183,  223;  GMS  152;  BBB  p58, 
500;  AVS  112 

1065  'nkr'yp-    B  J-h~^-  (oJ^lj^^y^ 
angryp  ?   ©impf.  mnk^yp 

Go)agitate 
VJ  1000 

1066  'nkwpyn   B,  S  ^i 
angupen    Ongwpyn)   ©<*angupaina-;  Av. 

paena 
honey  4 

TSP  19.7,  16  n  p232;  BSTBL,  Padm.  40;  KG  368 

1067  'nkwst(h)    B,  S  ^i 
angusl   OnkHvst)   ©ob.  -y;  pi.  -//    ^p>5y  >nkwst, 

}ngwsl 
finger 
BSTBL,  Padm.  42;  Dhy.  21,  29;  MDiii;  TSP  14.23, 

24,  25;ob.  pi.  >nkwstyt,  TSP  5.24 
=== leaf107 = p42
13-      TSP 2.159; SCE 183, 223; GMS 152; BBB p58,                   anpa6
14-         500; AVS 112                                               footless, without feet ?
15-                                                                    TSP 9.133
16: 1065 'nkr'yp- B                      J-h~^- (oJ^lj^^y^
17-      angryp ? ©impf. mnk^yp                                  1075 >npst-    S                                        o^i
18-      Go)agitate                                                    anpast   ©pt. st. ^'np'st-, 'mpst- 'mst-, 'mpd-
19-      VJ 1000
20-                                                                    (w)fall453; Hen. Tales. 483.19; Frag. Len. 57.5
21-                                                                    GMS
22: 1066 'nkwpyn      B, S                               ^i
23-      angupen      Ongwpyn) ©<*angupaina-; Av.                1076 >npt-     B, S                                     o^Usi
24-
25-        paena                                                       anpat ©impf. mnpt      ^}mpd-, 'np't-
26-
27-      honey                 4                                       Go)faII
28-      TSP 19.7, 16 n p232; BSTBL, Padm. 40; KG 368                  TSP; SCE; BSTBL, Vim. 128; MSP bl5; Frag.
29-                                                                      2a.l7; GMS 633
30: 1067 'nkwst(h)     B, S                              ^i
31-      angusl                                                  1077 >ns»c- B => ^s'c-
32-        }ngwsl OnkHvst)   ©ob. -y; pi. -//   ^p>5y >nkwst,
33-                                                              1078 Wk     B                      ^jo^^jjL.
34-      finger
35-                                                                    ansak ©<*ham-sdka ^'ns'kCy)
36-      BSTBL, Padm. 42; Dhy. 21, 29; MDiii; TSP 14.23,
37-                                                                    provisions, means
38-        24, 25;ob. pi. >nkwstyt, TSP 5.24                           BSTBL, Dhy. 98, -\ Dhy. 286; ob. -y, Dhu. 175;
```


## [2026-09-07T20:46:55.374Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT paena\"; grep -n \"paena-\\|pa8na\\|paēna\" BRT.txt | head -10; echo; echo \"=== BQT v1 angubin leaf\"; python3 - <<'EOF'\nimport io\nfor f in ['BQT_v1_pages.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    for i,p in enumerate(t):\n        if 'انگبین' in p:\n            print(f,'leaf',i, 'printed~',i-212)\nEOF"
}
```


### [2026-09-07T20:46:56.659Z] TOOL RESULT

```
=== BRT paena
14792:Ableit.  aus  *paena-  m.  'Honig'');  mp.  attgu- fin,  np.  angHÜn  'Bienenhonig'.  —  Ob  zu  lit. /Ami  'Milch'?  {s.  daiu  JSchmidt  Krit.  :<h)'). —  Pü.:  fehlt. —  ")  So  der  Ausgang  in  T.  — >)  Die  Bedeutung  'Milch'  ist  für  *ptüna-  nicht wahrscheinlich,  obwohl  sich  ja  np.  anpibln allenralls  als  'Bienen milch' fassen  Hesse;  vgl. Hb«.  PSL  19,  AGr.  /.  124.

=== BQT v1 angubin leaf
```


## [2026-09-07T20:46:57.732Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfiles={'BQT_v1_pages.txt':212,'BQT_v2_pages.txt':-543,'incoming/BQT/BQT_v3_pages.txt':-1208}\nimport os\nfor f,off in files.items():\n    t=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    for w in ['پینو','دژپیه','دشپیه','پیه']:\n        hits=[i for i,p in enumerate(t) if w in p]\n        print(f,w,hits[:12])\nEOF"
}
```


### [2026-09-07T20:46:59.255Z] TOOL RESULT

```
BQT_v1_pages.txt پینو [675]
BQT_v1_pages.txt دژپیه []
BQT_v1_pages.txt دشپیه []
BQT_v1_pages.txt پیه [79, 342, 509, 676]
BQT_v2_pages.txt پینو []
BQT_v2_pages.txt دژپیه []
BQT_v2_pages.txt دشپیه []
BQT_v2_pages.txt پیه [24, 507]
incoming/BQT/BQT_v3_pages.txt پینو [586]
incoming/BQT/BQT_v3_pages.txt دژپیه []
incoming/BQT/BQT_v3_pages.txt دشپیه []
incoming/BQT/BQT_v3_pages.txt پیه [86, 309, 335, 665]
```


## [2026-09-07T20:47:05.269Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14770,14800p' BRT.txt"
}
```


### [2026-09-07T20:47:05.314Z] TOOL RESULT

```
VgL  lbae!ö'.laumayqtOma:  —  Pü.  (m  Yt.  I): tri  larvinltärlum,  etl.!  bei  hae  dämäit  afiäc därim  pa  slH  u  ra=m  i  duSmanän;  [iv.  V.  p): ^ffffit  .  .  bei  laniftiene  (iSg.).  —  ')  iF.  %  4O3. ,
—  »)  NA.  trennt.
•  j.  tbaeSö.taurvayffSttma-  Adj.  'der die  Feindschaften  am  besten  überwindet';
ia£  asti  Mq%rahe  tpmtahe..  'm?m  datva- nqm  maSySttamca'^^  Yt.i. i;5.
Sapeil.  au(  *'laurvayaHt:  —  Vgl.  ^äeiö.faui- vati:  —  Pü, :  bis  tarvhülärtum  hal  divän  u martamän  i  vai.  —  1)  Die  Gen.  d'  und  m' sind  vom   1.  Glied  des  Komp.  abhängig.
•  j.  tbaeäö.par^ta-  Adj.  'aus  Feindschaft, in  feindseliger  Absicht  gefragt':  uia  hl fraiha  (sd.)  paiti.mravSne  navaca  navai- tXmla  xruidranqm  °tanqm  yat  mqtn  p»r>- sai ..  "..  auf  die  99  schwierigen,  in  feind- seliger Absicht  gefragten  (Fragen),  wenn  . ." Ytj.  82'';  —  iard^uströ  asaritS  aka manatgka  xrüzdya  'tanqm  ",  .  durch  die Schwierigkeit  der  in  feindseliger  Absicht gefragten  (Fragen)"  V.  ig.  4.
PQ. ;  ifs  pursiin.  —  ')  Hier  Korr.  der  NA.  nach V.  19.  4.
j.  tbi^;  g.  daibi/-'^  f.  'Feindseligkeit, -Schaft'.
KompE.;   Ableit    —    Zara  \.  ßtül-,   —    ai. dvif-  f.  —   O  S  36S.  56. j.  "/iilaSqm  Vyt,  rp:  ».  xoiUt  Jbiiyaitt:
•  j.  tbiSifi-  tn.  'Glied'  des  Fingers;  kasil^take imahmahe,  masistake)  »rszvB  fraltnum  °iis V. 6.10(12,  i4),iÄ44PüZ.
Pii.i  b  c  k;  vgl.  zu  baiidräjah:
•  j.  tbista-.  'Uisla-  Adj,  PPfP.:  s. Ibai^-.
KompE.  —  li.  dvif/ä-  Adj,
•  j.  (bisyant-,  g.  daibisyant-**  Adj.  'feind- lich, fcind,  inimtcus':  rapantl  .  .  at  .  . -yanti  zastäi/täi/ (sd.) . .  Y.34. 4;  —  aei'qm *°yafitqm ''>  . .  tbaesä  \t.jo.'j6;  —  aurva- 'äianqm  'yantqnt  Y.57.  a6,  Yt  J^.  31,  *Vyt. i^";  Yt  74.34,  ^■57-''f>\  —  aurvahafiiyS pars  'yanbys  Yt.  13.  69,  Y.  68.  13;  Yt.  10. 75,75.31;  — -  vlspim  aurvd^jm  °yanttm vXspfm  ay)m  °yant>m  A.  7,  10;  —  vanä{ vupe  'yantö  Yt  75.54; — pala  nS  'yantat pairi  SrB.5.
PPA.  lum  V.lban-,  —  Pü. :  imär.  —  ')  S  i6S. 56.  —  ')  NA.  'yatqm,  s.  Var.  —  3)  In  den Hds,  TCideibt.
•  j.  (biS'vant-,  g.  daibiä'vant- '>  Adj. 'feindselig,   feind';    tbü'vatqm   tba^ä  H.g.
8;  28;  —  daibirvatö  dt'aliS  Y.2S.6. Vi..:  bSiiiär.  -  i>  S  368.  56.
*  }■  P^°>  /"%  tii'^  KompA.:  sva.  apa. In  ptarmta    und  fiäyaozä   (beide    an   wenig Vertrauens  werten  Stellen). — pa',fä.'  können sich    zu    ai.  ap&   verhalten  wie  ai. />'  zu  äpi\ vgl.  ksl.  podati  'atn-liidyai'.
ob,Google
8i7
paenaena-
•  j.  paenaena-  Adj.  (fem.  'nl-)  'aus  Honig bestehend,  bereitet";  *'nyä^t  (ISt)'>  zao- %raya  N.57.
Ableit.  aus  *paena-  m.  'Honig'');  mp.  attgu- fin,  np.  angHÜn  'Bienenhonig'.  —  Ob  zu  lit. /Ami  'Milch'?  {s.  daiu  JSchmidt  Krit.  :<h)'). —  Pü.:  fehlt. —  ")  So  der  Ausgang  in  T.  — >)  Die  Bedeutung  'Milch'  ist  für  *ptüna-  nicht wahrscheinlich,  obwohl  sich  ja  np.  anpibln allenralls  als  'Bienen milch' fassen  Hesse;  vgl. Hb«.  PSL  19,  AGr.  /.  124.
•  j.  'pacman-  n.  'Muttermilch';  yU  (nätnl. aridvt)  vupanqm  hütriünqm  däitlm  ra- %wTtn  'ma  ava.daraiti  Y.Ö^.z;  Vyt  50; —  Aä  (näml.  andvt)  .  .  yaeiäa%äiti  .  . ar^qm  xhtdrä  hä  x^a%rinqm  garm>q  hä xia%rinqm  'ma  Y,  65. 5.
KocnpE.;  Ab!eit.  —  Zum  V.  pay-,  —  S.  'pac- man- and  auch  paenaena-.  —    mp.  (Pü.)  p/m :
5.  noch  JSchmidt  Krit  104.
•  j,  'paeman-  Adj.,  nur  fem.  'mat/iT- 'säugend',  von  der  HUndio;  gatwqm  , . pu^raca  (sd)  'mainiea  V./5.  49.
Zum  V.  pay-,  —  VgL  'pacman-.  —  Pü,:  pem i  ra/l.
•  j.  "paemanyo  vs  Vyt.  13.
Vgl.  V.  31.   7,  wo  paemavaili.
•  '].  paema'vant-  Adj.,  nur  fem.  'vaili- 'die  mit  Muttermilch  versehen  ist"h  °vaHi xsviptavaiH  (VSf.)  V.  21.  7.
```


## [2026-09-07T20:47:06.386Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[675]\nprint(len(p))\nimport re\ni=p.find('پینو')\nprint(p[max(0,i-2500):i+1500])\nEOF"
}
```


### [2026-09-07T20:47:07.665Z] TOOL RESULT

```
1480
بح
«یینکی» برروزن زیر کی غذودنی باشد
ین ۱ با نون بروزن لموء کشك‌باشد
که دوغ نرش خشك‌شده‌است‌ویعربی اقطوبتر کی
چکده رانیز گونشد که
روغن آ ترا نگرفته باشند ۰
ا۶ ۰
بنو له یپ مسکون‌کاف» سمعنئی بیتواست
که قروت و کشك باشد؟ .
پینو وا با واو بروزن گیسوها ۰ 9
آش است .
لیفه _ « بروزنکینه, پارچه که بر کفش
وجامه وخرقه دوزند- وپوست دست ویا واعضارا
یز گوبند که بسبب کار کردن سخت وسطبر شده
باشد .
بو ِ بقتح اول و تانی بواو کشیده ,
کلوخ را کونند که پارچپای گل خشكث شده‌باشد.
و با ثالث مجهول‌مرضی است که آنرا رشته گویشد
وازاعنای آدمی ۳ هی آ بد.
بو‌ار بروزن شیراز» شیر ه راگوننده
فقروت خوانند - وماست
وآنرا مرغ عیسی خوانند .
یواسته آم بروزن پبراسته . برج قلمه
وحصار -- وفصیل را گویه ,
یوس ه بکر اول و واو مجهول بر
وزن ف-وی, بمعنی انتظلار باشد- وطمم و توقعوا
فلز گویت ۳
لیو ست ع»_بفتح اول بر وزن لی‌بست ۰
ییعنی سوسته است که همیشه ودأیم وهدام باشلس
ویمعنی پیوند هم هست که ماضی پیوسئن وپیود
کردن و الحاق باشد- و باسطلاح .-حنفین‌وسول
سالك است از قید شید بدرجهٌ اطلاق حققت
اسدای ای فان لس ای
شد ۵ .
پیوستگان + مر کباترا گونند همچو
نبات وجماد وحیوان ٩‏ .»
مق ست4 » بروزن برجسته, بمعنی‌هميشه
ودایم باشد - ویمعنی پیوند کرده شده و در عم
پسته ‏ وبلا فاسله هم‌آمده است - و کسی رالیز
کون د که از بیاری کریستن تواند مخن گفتن
وگن کوند گر برمخنش أفد رد
. مازندرانی کتونی
برادران را بوسف چو داد گندم وجو
اگر بناعت مزجاه . پشم و پینو بود
۳ - رشك: سنو .
۴ رژد: سوس.
فرهنگه دساتس .
۵ _ ره :
نبود گندم وجولیر جز تیک
سوزنی‌سمر قندی. #جهانگیری».
1 - <هع پوسته » مر کب این سیط,
ت [ رك : پیمان] ,
نیب رک ۰۱۸۳ ؛ ملحق شدن,
```


## [2026-09-07T20:47:30.715Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB pih/ferbih\"; grep -n \"pîh\\|pih '\\|ferbih\\|farbih\\|angubîn\\|angubin\\|panîr\\|panir\\|pinû\\|pinu \" HUB.txt | head -20; echo \"=== NYB\"; grep -n \"^pih\\|^pīh\\|frabih\\|angubēn\\|anguben\\|panīr\\|panir\\|^pēm\\|pym\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T20:47:30.777Z] TOOL RESULT

```
=== HUB pih/ferbih
2960:= np. farbih pinguis, robustus, florens, copiosus' ist
4921:Vgl. den Weohsel von I mit e vor r in np, panlr *K&se' = &rm,panir
6249:*Nacht*, ap. xsapa-va; sitab *Eile', arm. stap; farbih 'fett',
7220:H. 947 = zd. guda-, skr. gutha--, farbih fett' = zd. fra-
=== NYB
522:apar-pém [MDM pymj heavenly, divine milk 429. — < *apar + pem (g. v.). apar-rösneh [MDM lwšnyh] the Heavenly Light 371?. — V. rēšnēh.
583:apé-mieak [’pymck'] tasteless, flat 6814. 691. — V. micak.
2068:hu-pém [hwpym] having good milk, of cows 422.8,
3072:patmin [ptm’n'] measure 915; contract 778; moderation, modesty 7019-21, 8517; maturity 225 (opp. araséh). — MPrth pdm'n; MPrs pym?n; Paz. pačma(n); NP paimän; from pati + Av. (1165 sq.) mäy- ‘to measure’ = OP.
3075:patmöcan [ptmwen'] garment 2!?. 171, — Arm. lw. patmucan; MPrth pdmwen; M Prs pymwen; v. next w.
3076:patmóxtan [ptmwhtn'] patmöc- to dress oneself, to put on one's clothes 218. 8515, — Cf Av. (837 sq.) pasti.Smuxta- ‘shoed’; MPrth pdmwatn pdmwe/j- (MHC); MPrs. pymwatn pymwc-; Paz. padmöztan pad- mož-; NP paimostan paimoz-.
3116:pēm [pym] milk 423-13.25, 431, 533,543-11, _ Av. (817) pačman-; Paz. pim.
6106:pwlwd: polavatčn pwr: purr pwrsydn: pursitan pws: pus pwst: post pwšt: pušt py'dg: padatak pyd, pydr: pit pyd’g: paitak pyg: padak pygm: paitäm pym’n: patmän pymwen: patmöcan pymwxtn, pymwe-: patmöxtan pyr’yg: pairayak pyrwz: péroz pyšwb'y: p&söpäi pyšyn: pēšēnīk Pyš, pyšyy, pyšyh: pēš pyw’c-: patvac- pywn: patvand pywst: patvastan
```


## [2026-09-07T20:47:33.661Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC\"; grep -n \"^pī-\\|^peiə\\|^pitu\\|^poimen\\|^pīwō\\|pinos\\|^pī̆\" IEC.txt | head -20; echo \"=== SYN fat\"; grep -n \"4\\.85\\|FAT (SB\\|FAT (ADJ\" SYN.txt | head; echo \"=== WLD band3 pinu\"; grep -n \"pinu\\|angubin\\|pitu\" WLD_band3.txt | head"
}
```


### [2026-09-07T20:47:33.747Z] TOOL RESULT

```
=== IEC
3918:spinosa"; MIr. Ir. guaire ‘shag; bristle’; ON kárr “lock, curl; Li. gauras, id.; in pl. wool
6824:karpinos “a tree, hornbeam (?) Hitt, karpinas (a tree); Lat. carpinus “horn- beam’. (Isophonic: Li. karpiniai 'lace")
12669:peluo (2) “fill”. Cf. pelu, polua, pluos, pinos Skt. parvàmi, v. id.
13111:pletos, is “spreading, spread, flooding, full. Cf. pléió, pletó, pinos Skt. pratáh ‘full’; Arm. li, gs: lio, ost id.; cf. licK, s. ‘filling’; Gk. cf. ém-plemi, v. (fill: Lat. impleó, ére); Alb. i plotë "full; Lat. cf. im-, com-pletus beside locu-ples, gs: -pletis (^rich', cf. Iucar, lucrum & *ləuð above); Olr. líth, n. ‘plenty; festivity’; Gallo-Lat. cf. liduna, f. (for *lituna *ebb-tide'?); OBr. liti-, adj. “busy, fre- quented"; Li. cf. pletejas, m. ‘spreader’; iX-plé- tas *wide open, WP II, 64. See next
13241:plnéio (plneu-) “fill; be full’. Cf. pinos Skt. prāmi, v. ‘fil’; Arm. cf. Inum, v. id. (fr. *plenu-); Lat. polleo, v. "be strong; OW llanw, llenwi, v. fil’; W Ilanw, id.; Cor. len- wel, inf. id.; Br. cf. lanw, m. ‘tide, inflow’; W llanw, m. id.; Go. us-, ga-fullnan, inf. ‘get full? beside fulljan and com. Gmc., v. ‘fill’; OCS plünjo, -iti, v. and com. Sl. "DI: Li. pilneju, eti, v. ‘get full
=== SYN fat
6281:3. Lith. kelys, Lett. celis, ChSl. ko- léno, etc., general Balto-Slavic : Grk. xadny ‘hollow of the knee’, x&)ov ‘limb’, oxédos ‘leg’, etc. (4.85). Walde-P. 2.599. Berneker 545 f.
7794:4.85 WOUND (sb.)
18463:cf. Falk, Wort. u. Sach. 4.85 ff.
=== WLD band3 pinu
2123:ar =o ae spildan, pape hd 675". sorga, sorpen B2u* 4pillan age. hee st ave. 454". spinala ahd. 661° #0 . 468", apind nd. 662°. fous mhd. 46" epinde ndl. 662°. goum abd, 515* epink engl. G82*. epedo as. 653". «pinkel mnd. 674° epahhe ahd. 652°, 653" pinnae ali. 661°. epdhi abd. 660°, spianewe! mini. 17 #poichen nbd. dial, 655* spinula, ep ahd. 654". epak a ren epiog ahd. LI9?, B69". epakeren mnd. 652", 664%, spird(a)rén epoch mb. 653%. eplocen ahd. 633° spachten nbd. dial. 652%, @mg ahd. 665° epacken bair. 653°. epizz) abd. 655" apale mh. 675*. epliaf nd. 679* epalt, apell . 6TS* emitter mhd, Gi" spon mnd. 662°. epok, apGk mnd. (664*). apan alul, 652". op ra Se é pan milred. ma ?poo rm ¢ a fponen abd. 655°". #por ahd. 669* ene yoann age. GO2*. #porkel moi. A74"
2542:sétie Lit. 444", splatu, aplati lit, (Ge4*), a ay, sr Se ighia, apaig ~ 855%. Gl, apitull lit, a pl oof = geo pier Pg e78* are. pliati Lit, 100" i : " | “ F i a ri Ra te pr Mie e7k* O74" pando “fal eal" vera io, pra. epemdia lit, G2". eprat lit. O71", | epanga lott. 652*. eprondsu, sprang? lett. 671°. spaigas lit. O85". oem ot, seprauiies lett, Caen SS lett. OBS". sprangie Wit. 667%. epanakis lit, GOL". spriucuo, eproukties lett, spdrdau, -yéi Ht. 660°. 671". = sparginti lit, G74". eprauga lett, 671°. epargl on oie eprauad? lott, 25%. a, spars lott. G60". 870°. gparias alit. 687°, epraiitu, -du, =e lott. 671%. Pe tae Ht, 66" arse = Tjudtie, epbuse fuati Lit. 650°. apréndulis lit, 672°, ypenije Ut. 113. sprindiiu lit. 672°.
```


## [2026-09-07T20:47:42.627Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2955,2965p;7215,7228p' HUB.txt"
}
```


### [2026-09-07T20:47:42.667Z] TOOL RESULT

```
psiz. framos, farmos (Min. 61. 75, Shk. 244), np. fara-
moS nicht. Doch ware np. faramnst = skr. ^pramrsta-,
*pramrsti-. Dames hat nh, sa-musay^ sa^musay (mitw,
u) *to forget'.
813. Gegensatz von zd. frapi^wa- gut genahrt, gedeihend'
= np. farbih pinguis, robustus, florens, copiosus' ist
zd. tardpt&wa- vd. 13, 20 = *sehleeht genS-hrt*. Np.
farbt JRAS. 1894, p. 477 = phi. frapfh = zd. *fra-
p^d^wa-? Zur jiid. pers. Form vgl. paz. pad = phi.
pit ^fat' Shk. 261.
Nach 816 ware nach Salemann np. farasp = phi. frasp
phi. mShmdn (lies mihmdn) 'darinnen befindlich, innewohnend*
Min. kap. 21, 13, Shk. 257, Bdh. Gl. 241, Gl. and Ind. 208,
ap. *maidwd7i^ zu zd. ma^dana- ^Wohnung ; pahn *weit',
paz. pahandl *Weite' Min. Gl. 154, phi. pahandk Gl. and
Ind. 89, 92 = zd. pa&ana-; guh *Koth, Schmutz, phi. guh
H. 947 = zd. guda-, skr. gutha--, farbih fett' = zd. fra-
pi&tvD ; gdh *Ort, Thron , paz. gdh Shk. 245, Min. Gl. 87,
ap. gddU', zd. gdtu-j phi. gels, aber arm. gah 'Thron, Sitz,
Rang (5. Jhd.), syr. n;i2N cisterna ; gdhvdra, gahvdra 'Wiege',
phi. gdsvarah *bed-place' West, FT. IV, 123, aber arm.
gahavorak *Sessel, Sanfte, Bett' (5. Jhd.) ; cahdr Vier , paz.
cihdr = zd. cad ward; cihil 'vierzig = zd. dadwaresatem;
Gdh 'Brunnen , phi. cdh PN. 84, ap. '^cdd^-, zd. odt^ ^) ; sdh
*J Ueber den Weohsel von altiran. ^ und i aus urspr. t (je nach-
```


## [2026-09-07T20:47:43.381Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"#### WLD Bd2 leaf 8 (p3)\"; awk 'BEGIN{RS=\"\\f\"} FNR==9{print}' incoming/WLD/WLD_Bd2_pages.txt | head -50"
}
```


### [2026-09-07T20:47:44.667Z] TOOL RESULT

```
#### WLD Bd2 leaf 8 (p3)
          :




4                                            pag.   — pap(p)a

vokalisch ai. pajasyd- n. Bauchgegend. Weichen^^, russ.    pachz „Leisten-
gegend^, pacha ^Achselholile^^, pachva „ Achselhohle, Leistengegend^^ da-                                ;


neben ein ?o-st. '^pagip- oder ^pogio^- in cech. paSe j,Ariii^^ u. dgl. (s. Wiede-
                        —
maBn BB. 27, 251 260 m. Lit.; uber abg. pasucha usw. s. aber u. dms-
„Arm'‘‘; iiber apr. paggan „wegen^^ s. Trautmann 388, Levy IF. 32, 163).

pag-,            „Wasser, Quelle “?
  Gr. Tzrjy']^, dor. Ttdyd „ Quelle “ (Deutungsversuche s. bei Boisacq                                  s.    v.)
verbindet Scheftelowitz St. 33, 151a 1 mit ai. urii-hjd- BY. 9,77, 4,                                    nach
Sayana „reichliches Wasser erzeugend^^, so daS -ija-                         = idg.        "^pidjgo-.   Inter-
essant, aber sehr unsicher.

pat^r- „Yater“ (poteir), gen. p9tr-es, -os, -5, acc. pdter-n usw.).
   Ai. pitdr- „Yater“ {pita, -dram), ay. nom. pita-, ao. pitar- (daneben
p^ta, 0ardm, f^droi und ia, s. Osthoff Par. 225 m. Lit.); arm. (Hiibsch-
mann arm. Gr. 2, 453) hair, gen. haur, n. pi. harJz „7taxriQ, nargog, naTegsg'^
gr. TiaxriQ, -rgog „Yater“ {evjiaTcoQ, -ogog); lat, pater, -iris, o. patir, umbr.
dat. paire,      voc. lu-pater       (lat.   Iiippiter,      gr.    Zsv    Jidzeg;       ai.   Dyaus pitd)\
air.   athir         (dazu nach Loth Be. 15, 225 cymr. -gwal-aclr, bret.
                „Yater^^
ual-art aisl. val-fadir), gall. Ateronius 30. got. faclar, ais. factir, ags.
                                                                    ;


feeder, ahd. fater „Yater“.
   Yon einer «(o)-Ableitung: ai. pitrvya-, av. tilirya- (d. i. [p\t9 rvya-)
„Yatersbruder"*       = ahd.     fetiro, fatirro,           fatureo      „Yater8bruder‘'^                    ^/«-
diir(u)ia-  mit Gberfiihrung in die w-Dekl.), nhd. Vetter, ags. faedera
„Yatersbruder“; Kurzformen sind ags. fadu, mnd. meZe „Yatersschwester“;
gr. Ttargviog „Stiefvater^‘ (nach prjrgvid aus ^mafrtmla )   arm. yauraij ds.        ;


(Leviratsehe) lat. patrmis „Yatersbruder^^ gr. Jidrgojg ds., gen. 7taTg(jb{f)og
                  ;                                            ;


(dazu TiaTgcDiog ,,vaterlich‘‘^ mit verschobener Gdbed.), lat. patromis (Bil-
dung vde 7natrona);            ein   uo-Formans    in anderer Bed. in ditaTovgia jon.
aus ^sni-jcarog-^ta         (Lit. bei    Boisacq 1096).
   Anderes Zubehor: ai. pitrya-, gr. Jidigtog, lat. patrius „yaterlich^^ ; lat.
```


## [2026-09-07T20:47:55.342Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 78 79; do echo \"#### WLD Bd2 leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} FNR==N+1{print}' incoming/WLD/WLD_Bd2_pages.txt | head -45; done"
}
```


### [2026-09-07T20:47:56.694Z] TOOL RESULT

```
#### WLD Bd2 leaf 78
74                                    poi-, pi



   lAi, papijusi 'kdrve „Kuh, die beim Melken die Milch nicht zuruckhalt“,
zeme iszpijusi „durch Wasser aufgeweichte (d. h. Wasser vorquellen lassende)
Erde^^ pydau, -dyti „eiiie Kuh zum Milchen reizend'^ (vielleicht in alter
Beziehung zu gr. mdvoy usw., wenn namlich 'pydyti eine der Formen ist,
aus denen die Faktitiva auf -dyte ihren Ausgang genommen haben), lit.
penas „Milch“ („beim Melken vorqnellende Fliissigkeit^, Leskien Abl. 280;
Osten-Sacken IF. 33, 245 f., also nicht als „Gretrank^‘ zu 'poi- „trinken“; an
e aus oi, auch bei p'eva ,,Wiese“, zweifle ich trotz Wiedemann BB. 28,41,
Osten-Sacken aaO. nicht. -n- aus -wm-? s. o.).
   Norw. /*e? „Rahm, dickgemachte Milch“ (s. Wiedemann BB. 28, 39, Traut-
mann grm. Ltg. 33); ags./'<^wwe „ Jungfrau, junge Frau“, as./*emm „schwangere
Frau“, ^dA.feima „Madchen“ (; av. paeman- „Muttermilch“, J. Schmidt Krit.
104 f.).
   *pJmo-s „fett“ in gr.       „Fett“, lat. opTnms „fett, wohlgenahrt; frucht-
bar ; reich'^ (wohl Riickbildung aus ^op-ptmare, d, i. "^ob-plmare, vgl. be-
legtes opTmare „fett machen, masten“; Yf. LEWb.^ s. y. m. Lit.), pmguis
„fett^‘ (im Ausgang mit der Entsprechung von gr. Tzaxvg, ai. balm-, gekreuzt,

s.   bhengh’ „dick“).
     w-Bildungen: att. noa, ep.-jon. tzou], dor. noia ,,Gras, Rasenplatz^, aus
jraj:a   = lit. peVa „Wiese“ (Schulze Quep, 45 a 2, s. auch Persson BB. 19,
257,     Wiedemann BB. 28, 41; 29, 315).
     "^piu-os- mi. *pJu-er-l-en- „Fett, fett“: ai. pivas- n.,   av. plvdh-   n. „Fett,

Speck“;      ai. ptvan-, ptvari „schwellend, strotzend, feist, feW pivard- ds.
                           f.

jungere, mit dem ebenfalls nicht alten gr. Tileoogj Tilagog nicht in die Grund-
sprache zuruckreichende Bildung vom Fern, aus, s. Frankel KZ. 42, 119 a 1)
= gr. Titcov, f. TUEiqa „fett, fruchtbar, reich“, TxiaQ (hur n. a. sg.) „Fett''; air.
%rm, gen. irenn „Erdboden, Land'^,       wenn eig. ^nkiga yrj'" Pokorny KZ, 47,
233ff., wo gegen Anreihung von ^dr/Eriu, cymr. Ywerddon „Irland“, das nach
P. aus ^epi-uerjd „Hugel, Insel“). f«-St. "^poi-tu-, *pj4u~ „Fett, Saft, Trank,
Nahrung“ (gegen Verb, der Worte fiir „Nahrung“ mit poi oder pa „Yieh“
weiden“ s. d.): oi in lit, pBtus „Mittag“, das nicht blo6 Ablautneubildung
(gegen Osten-Sacken aaO., vgl. ai. petv-a-li m. „Bock, Hammel“ (eig. „feisf'),
av. poi&wa „feist'‘, auch lit. iszpdiive-jti, -ti „wieder zu Kraften kommen,
gesund werden“, eig. sich herausfuttern'’;
   ai. pitii-h m., av. pitii-s m. „Saft, Trank, Kahrung, Speise“, av. arom-

pi'^iva ra^pi'&ica f. „Mittag, Mittagszeit^^, eig. „die zum Mahle passende Zeit“;
#### WLD Bd2 leaf 79
                                        pou- p0u- (pau-) : pu
                                              :                                                   75

      Die Bed. „Harz“ auch         in    der ^-Abteilung                  :
                                                                              gr. mooa (^mxuct), att.
nizia, lat. fix,                 Teer“ (daraus ahd. usw. peh), life, pihis „Pech'‘,
                      -cis „Pecli,
abg. pfbTih, pfbCfblz ds.; wahrscheinlich isfe auch lafe. pinus^ -us und     „Pichte,
Pohre, Kiefer‘S aus "^pie-sno-s entstanden (s. Yf. LEWb.^ s. v., w-Flexion
nach quercus] unklar ist die Gdf. von alb. we „Fichte, Kien, Kienfackel‘‘,
s. G. Meyer Wb. 340,        Alb. Sfe. Ill, 30; in Laufe und Bed. ganz fragwiirdig
deutefe Sommer GrLtsfe. 72 quvaxa' dgvv Hes. aus 7ti(x)-ov-ax-). In anderer
Bed. vielleichfe mnd. v%          vihe, vie n. „Sumpf, Bruch, Sferauchwald, Teich“
(Holthausen AfnSpr. 121, 291). Erw.                pTd-: gr. nldiqetg „quellenreich“,
Tiida^ „Quelle“ Ttldvoy       „la8se durchsintern,             quelle hervor, sprudle hervor“
(falsch Charpenfeier IF, 28, 180 f.), ntosa n. a. pi. n. „feuchte Orfee, Wiesen“;
aisl. fit f. „niedrige   Wiese am Wasser, Wiesenland“, ostfries. „Pfuhl, Wasser-
pfutze*^ (Fick III'^ 241);         aisl. fita      f.   „Fett“, fitna   „fett werden^^ (Fick III*,
241);                   mhd, vei0       „fetfe“,ahd. fei 0zen „nahren“, Ftc. ahd. fei 00 if,
mhd.  veizt, nhd. feist; da6 ir.             esc „Wasser, Sumpf“ als *pidsq(l hierher-
gehore (Stokes BB. 19, 73, Fick II* 329, Foy IF. 6, 325), isfe an sich fraglich
und wird durch acymr. uisc (ware dann "^peidsqd) widerraten, da -ei- in
unserer Wz. sonst fehlfe;
  Ygl. im allgem. Curtius^ 164, 276, Fick I* 80, 247, 481, 482, II* 44 f.. Ill*
240, 241, Yf. LEWb.^ s. vv. DaB unsere Wz. Erw. von dp- „Was8er“ sei,
isteine wertlose Konstruktion.              —
                               Sollte gr, dmov „Birne“ als "^apisom mife
lat. pirum zshangen, so ist doch nicht als „saftige Frucht“ hier anzureihen;
wohl voridg. Mifetelmeerwort (s. Yf. LEWb.^ 586, Boisacq Rev. d’instr. publ.
55, If., Diet. et. gr. 1096); daB dmov fiir sich                    als       „wasserige Fruchfe“ zu
dp „Wasser“ gehore, isfe nicht wahrscheinlich.

pou-     :
              pou- (pan-) : pu „klein, gering, wenig“, vielfach fur „Junges, Tier-
        junges, kleines Tier‘\
      Lafe.    ^pavos, pauper „arm“ (f^pauo-paros „wenig erwerbend,                       wenig sich
schaffend'*); got. faivai pi. „wenige“, aisl. /“ar         „wemg, wortkarg“, ahd. fao,
fd ,,wenig“, as. fa, ags. fea,             pi, feawe, engl. few „wenige“ (feawe nicht
nach Kluge Gl. 2, 56 aus ^paukuo-, sondern fea       "^^fawe)       X
                                                              aber air. dfhad,      ;


nathad „Einzahl, geringe Zahl, Selfeenheif’ (Fick II* 53, Foy ZfceltPh. 3,
266) s. u. au „herab“.
  Mife (deminutivem) Formans -ko-: lat. paucits „wenig“ = ahd. foh ds.
```


## [2026-09-07T20:48:08.380Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in پنکه پیه فربه پینو پنیر انگبین دژپیه; do echo \"### $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null; done"
}
```


## [2026-09-07T20:48:09.614Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN fat\"; grep -n \"^fat,  adj\\|^fat, adj\" KLN_1966.txt | head; echo \"=== KLN pine\"; grep -n \"^pine,  n\\|^pine, n\" KLN_1966.txt | head; echo \"=== SKT\"; grep -n \"^FAT\\b\\|^PINE\\b\" SKT.txt | head; echo \"=== LEW pinus\"; grep -n \"^pinus\\|^pectus\" LEW_1910.txt LAT.txt | head"
}
```


### [2026-09-07T20:48:09.712Z] TOOL RESULT

```
### پنکه
MON_part1.txt:1
MON_part2.txt:0
### پیه
MON_part1.txt:26
MON_part2.txt:2
### فربه
MON_part1.txt:37
MON_part2.txt:29
### پینو
MON_part1.txt:1
MON_part2.txt:2
### پنیر
MON_part2.txt:18
MON_part1.txt:11
### انگبین
MON_part2.txt:8
MON_part1.txt:5
### دژپیه
MON_part1.txt:1
MON_part2.txt:0
```


### [2026-09-07T20:48:09.813Z] TOOL RESULT

```
=== KLN fat
=== KLN pine
28856:pine,  n.,  a  tree  of  the  genus  Pinus  (bot.)  —  ME., fr.  OE.  pin,  (in  ME.  fr.  F.  pin),  fr.  L.  pinus,  ‘pine', which  is  cogn.  with  OI.  pitiih,  ‘juice,  sap,  resin, food’,  pttu-daruh,  ‘a  kind  of  pine’,  lit.  ‘resini- ferous  tree’  (for  OI.  daru,  ‘tree’,  cp.  Gk.  8p3c, ‘oak’,  and  see  dryad),  Gk.  rtruc,  ‘pine’.  These words  are  traceable  to  I.-E.  base  pi-,  ‘sap,  juice", whence  also  Gk.  nritov,  ‘fat,  wealthy’,  TtLue/.f,, ‘fat,  lard’,  rtiacuz  (for  *ttixia),  ‘pitch’,  L.  pin- guis,  ‘fat’,  pituita,  ‘slime,  phlegm,  viscous  mois¬ ture’,  opimus,  ‘fat,  fertile,  rich’.  See  fat  and  cp. words  there  referred  to.  Cp.  also  pina,  pinaster, pineal,  pine  turn,  pinnace,  pifion.
=== SKT
6338:FAT.
=== LEW pinus
LAT.txt:47700:pinus, -I (et -Us, abi. pinu-, gdn. et. dat.abl.pl. pinarum, pinis,
LAT.txt:63955:pectus. Ancien (Enn., Pl. ), usuel. Non represent <5 dans les 1 . romanes,
```


## [2026-09-07T20:48:16.020Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in پنکه دژپیه پینو; do echo \"##### $w\"; grep -n -o \".\\{200\\}$w.\\{300\\}\" MON_part1.txt | head -3; done"
}
```


### [2026-09-07T20:48:17.299Z] TOOL RESULT

```
##### پنکه
##### دژپیه
##### پینو
```


## [2026-09-07T20:48:17.503Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN fat\"; grep -n \"^fat,\" KLN_1966.txt | head; grep -n \"fat,  adj\" KLN_1966.txt|head -3; echo \"=== LAT pinus\"; sed -n '47695,47720p' LAT.txt; echo \"=== LAT pectus\"; sed -n '63935,63960p' LAT.txt"
}
```


### [2026-09-07T20:48:17.589Z] TOOL RESULT

```
=== KLN fat
14435:fat,  tr.  and  intr.  v.  —  ME.  fatten,  fr.  OB.  fxttian, ‘to  grow  fat’,  it.fxtt,  ‘fat’.  See  fat,  adj. fat,  n.,  vessel.  —  ME.  fat,  fr.  OE.  faf,  a  var.  of vat  (q.v.)  Cp.  fettle.
14432:Derivatives :  fastuous-ly,  adv.,  fastuous-ness,  n. fat,  adj.  —  ME.  fatt,  fat,  fr.  OE.  fatt,  contraction of f letted,  pp.  of fxttian,  ‘to  fatten’,  rel.  to  ON. feitr,  OFris.  fatt,  fet,  MLG.,  MDu.,  Du.  vet, OHG.  feijit,  MHG.  vei3(e)t,  G.  feist,  ‘fat’  (G. fell,  ‘fat’,  is  a  LG.  loan  word).  These  adjectives are  prop.  pps.  of  Teut.  *faitian,  ‘to  feed,  fatten’ (appearing  in  ON.  feita,  OHG.  fei^eri),  fr.  I.-E. base  *poid-,  *pld-,  ‘to  abound  in  water,  milk, fat,  etc.’,  whence  also  Gk.  irTSueiv,  ‘to  gush forth’,  nlSod;,  ‘spring,  fountain’,  7u8 faiq,,  ‘rich in  springs’.  Base  *poid-,  *ptd-,  is  a  -^-enlarge¬ ment  of  base  *poi-,  *pt-,  ‘sap,  juice ;  to  abound in  sap  or  juice,  etc.’,  whence  OI.  payate,  ‘swells, exuberates’,  payas-,  ‘water,  milk’,  Lith.  pienas, ‘milk’.  Cp.  OI.  pituh,  ‘juice,  sap,  resin,  drink’, pivan,  ‘fat,  fatty’,  ptvah  ‘fat,  grease’,  Gk.
14435:fat,  tr.  and  intr.  v.  —  ME.  fatten,  fr.  OB.  fxttian, ‘to  grow  fat’,  it.fxtt,  ‘fat’.  See  fat,  adj. fat,  n.,  vessel.  —  ME.  fat,  fr.  OE.  faf,  a  var.  of vat  (q.v.)  Cp.  fettle.
28946:pit-a-pat,  adv.,  palpitatingly;  n.,  the  sound  of something  going  pit-a-pat;  intr.  v.,  to  go  pit-a- pat-  —  Of  imitative  origin, pitarrah,  n.,  a  basket  or  coffer  used  to  carry  the clothes  of  a  person  traveling  by  palankin  (India). —  Hind,  pitdrd,  petard,  fr.  OI.  pitakah,  ‘basket’, fr.  pit  ah,  pitam,  ‘basket’,  which  is  rel.  to  Pali pitaka-,  petika-,  pettdlah,  ‘basket’,  peld,  pelika, ‘a  large  basket’,  Singhalese  pelawa,  pettiya,  ‘bas¬ ket’;  prob.  of  non- Ary  an  origin, pitch,  n.,  a  resinous  substance.  —  ME.  pick,  fr. OE.  pic,  fr.  L.  pix,  gen.  picis,  ‘pitch’,  which  is cogn.  with  Gk.  niaax  (for  *Ttixia),  Lith . pikis, OSlav.  piklu,  ‘pitch’,  fr.  I.-E.  base  *pt-,  ‘sap, juice’,  whence  also  L.  pinus,  ‘pine’,  pituita, ‘slime,  phlegm,  viscous  moisture’.  See  fat,  adj., and  cp.  pine,  the  tree,  pituitary.  Cp.  also  pay,  ‘to coat  with  pitch’,  petechia,  picamar,  Picea,  pitta- cal,  pizza.
=== LAT pinus
lit. paisati, paisati "battre des grains pour les ddbarrasser de la
balle" et dans v.b.a./eso "balle (du grain)". - Le grec a une initiale
7 tT“ dans 7 CTI.oou) (avec -CRT- expressif dans un aot technique) "jMcraae
avec un pilon, je aouds", 7 iTioavr) "orgenondd" (avec siaplification
de en -CT-).
pinus, -I (et -Us, abi. pinu-, gdn. et. dat.abl.pl. pinarum, pinis,
cf. Enn. A.iyo et 490) f. : pin; et par adtonyaie, en podsie, tout
objet fait en bois de pin: vaisseau (cf. alnus), torche, bois de lauce,
etc. - Anci en, usuel. Panroaan. M. 1.6519. Gera.: ags .pinhnutu-, celt.:
irl.piqn, britt. pinwydd.
Ddrivds et ooapoads: pineus, M.L.6511; d'ou pinea, et pineum : poaae
de pin, pignon; pinetum : pinede, M.L.G510; plni-fer,-ger; pinaster
"pinus ailueatris" (cf. oleaster); pinastellus = peuce donum. Tardifs:
pinalis, pinicusiplniceIlus.
On rapproche skr. pltu-d 5 rufr qui ddsigne une sorte de "pin", c.-A-d.
un arbre rdsineux: le preaier terae seable se retrouver dans le
ddrivd la.t, pltu-lta (v. ce.aot) et dans gr. 7 tiTU£ "pin", paair ,pit
"pin". La foxaation en -nu- de pinus rappelle celle de TtiTUC.
plp5ti5: v. pipila.
piper, -eris n.: poivre; poivrier. Ne seable pas attestd avant
Varron. Panroaan. M.L.6531. Gera.: v.b.all .pepar et finn .pippuri’,
celt.: iri .pipur, scibar} britt. pebr.
Ddrivds: piperatus : poivrd; subat.piperatum: poivrade; piperatCriumx
poivrier; piperlnus, attestd dans Isid.iy,10,8 piperinus (scii.
lapis) subalbidus cum punctis nigris, durus atque fortissimus, et
dans la glose corroapue piperina : ciienines, OGL XII 537,31: pdpdrin;
=== LAT pectus
le sens de "clair, pur, net", tersum diem pro sereno dictum ab antiquis,
F#4y8,13. Les formes romanes remontent a tergere, M.L.8GG3.
Derives et composes: tersus,—us m.(Apul.); abs— M.L.48, circum—,
de-, ex-, M.L.3088, per-tergeo. S'y rattachent aussi mantele-, q.u.;
manutergium. ,
Aucun rapprochement net. On ne peut faire etat de gr.CTTSpyi-C
"rodoir, «Hrille", qui fait partie d'un ensemble de formes instables:
(TTeXy^S^ orXeyY^S, etc. Le sens de got .fiairko "trou" est eloigni.
Ni la forme ni le sens ne favorisent un rapprochement avec le groupe
de tero, La racine doit etre ancienne, mais ne se retrouve pas ail-
leurs. - On cite ombr.man-trahklu, man-draclo "essuie-main" (?).
tergum, -I n.(et tergus m.; Pl.As.319); tergus, -oris n. (l'abl.
tergibus dans Lucr.3,88 qui supposerait tergu, ou tergus,-us est
unique et douteux): peau (qui recouvre le dos^ cf. Plin.8,30 durissimum
dorso tergus', puis "dos" (de 1'homme et des animaux); s'emploie aussi
au pl. terga, merae en pariant d'un seul individu, le dos etant compos^
de deux parties. II est possible que la forme ancienne ait ^te terga
collectif, sur lequel on a refait tergus et tergum. Tergum est la
forme ancienne, et la seule qui figure dans les locutions adverbiales :
5 tergU, post tergum, etc. Tergus, -oris, plus recent, est fait d'apres
pectus. Ancien (Enn., Pl. ), usuel. Non represent <5 dans les 1 . romanes,
ou il a et e supplante par dorsum. - Voir aussi tegus.
Derives et composes: tergilla: couenne de lard (Apic., Gloss.);
terglnus: de cuir, de peau; d'ou terginum: fouet, courroie; tergoro
(Plin.): cuirasser, couvrir le dos.
De terga uertere a ete tire le compose tergiuersor, -aris (frequent
```


## [2026-09-07T20:48:28.053Z] TOOL CALL #43: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-07T20:48:28.097Z] TOOL RESULT

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


## [2026-09-07T20:48:29.084Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^pectus\" LAT.txt LEW_1910.txt | head; echo ---; grep -n \"pectus, -oris\" LAT.txt | head"
}
```


### [2026-09-07T20:48:29.149Z] TOOL RESULT

```
LAT.txt:63955:pectus. Ancien (Enn., Pl. ), usuel. Non represent <5 dans les 1 . romanes,
---
```


## [2026-09-07T20:48:37.100Z] TOOL CALL #45: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peyH-\" \\\n \"https://en.wiktionary.org/wiki/pectus\" \\\n \"https://en.wiktionary.org/wiki/punkah\" \\\n \"https://www.etymonline.com/word/punkah\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A8%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%86%DB%8C%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%DA%AF%D8%A8%DB%8C%D9%86\" \\\n \"https://en.wiktionary.org/wiki/pinus\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 385, roots Peg / Pei: verifying node forms and derivations\" ; done"
}
```


### [2026-09-07T20:48:46.233Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/44aa185600e7bd61.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d18d2741d620b330.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f9298bef58c5abcf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a1800cbbb6b4e947.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1ceda065440dddc5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/db89d6439aad5114.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a949eac8201fd441.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/966132e6ec2af018.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f916d981e118edb1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3fa7430102cf8af4.txt
```


## [2026-09-07T20:48:49.268Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 44aa185600e7bd61 1ceda065440dddc5 db89d6439aad5114; do echo \"########## $f\"; head -c 4000 $f.txt; echo; done"
}
```


### [2026-09-07T20:48:50.843Z] TOOL RESULT

```
########## 44aa185600e7bd61
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peyH-
FETCHED: 2026-09-07T20:48:38Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/peyh₂- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/peyh₂- - Wiktionary, the free dictionary 

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
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Root 

 1.1.1 
 Derived terms 

 1.2 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ peyh₂- 

 Add languages 

 Reconstruction 

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
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 (Redirected from Reconstruction:Proto-Indo-European/peyH- ) 

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *peyh₂- [ 1 ] [ 2 ] [ 3 ] 

 to swell (with milk )
 Synonyms: *ḱewh₁- , *swelH- , *tewh₂- 

 to be swollen , fat 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *peyh₂- (33 c, 0 e) 

 *péyh₂-de-ti ( de-present ) [ 1 ] 
 Proto-Tocharian: *päit- ( “ to be swollen, fat ” ) 
 ⇒ Proto-Tocharian: *päit-sk- ( “ to become swollen, fat ” ) ( or < *péyh₂d-sḱe-ti ) 
 ⇒ ? Tocharian B: pitke ( “ fat, grease, oil ” ) [ 4 ] ( or < *päits-ko- < *péyh₁d-s [ 5 ] ) 

 ⇒ Proto-Tocharian: *päit-tāk 
 > ? Tocharian B: pittāk ( “ blister, swelling ” ) 

 ⇒ ? *péyh₂d-s ~ *pih₂d-(s)-és ( “ pitch, resin ” ) 

 ⇒ *poyh₂d-o-s [ 1 ] 
 Proto-Germanic: *faitaz ( “ fat ” ) ( see there for further descendants )
 → Proto-Samic: *puojtē ( see there for further descendants )

 *péyh₂-t ~ *pih₂-ént ( athematic root aorist ) [ 2 ] 
 Proto-Balto-Slavic: *pīˀtei 
 Lithuanian: pýti ( “ to become wet, become muddy, start to give milk ” ) 

 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Sanskrit: पियान ( píyāna , “ full of, overflowing with ” , ptc.med. ) 

 *pi-né-h₂-ti ~ *pi-nh₂-énti ( nasal-infix present ) [ 2 ] 
 Proto-Indo-Iranian: *pináHti ~ *pinHánti 
 ⇒ Proto-Indo-Iranian: *pinHáwti ( “ to be swollen, fat ” ) ( see there for further descendants )

 *pe-póyh₂-e ~ *pe-pih₂-ḗr ( reduplicated perfect ) [ 2 ] 
 Proto-Indo-Iranian: *pipáyHa ( “ to be swollen (with milk) ” ) ( see there for further descendants )

 *péyh₂-mō ~ *pih₂-mén-s [ 1 ] 
 Proto-Indo-Iranian: *páyHma 
 Proto-Iranian: *páyHma ( “ milk ” ) ( see there for further descendants )
 → ? Proto-Finno-Ugric: *pejmä ( “ milk ” ) 
 Proto-Finnic: *piimä ( see there for further descendants )

 *péyh₂-os ~ péyh₂-es-os [ 6 ] 
 Proto-Indo-Iranian: *páyHas ( “ milk ” ) ( see there for further descendants )

 *péyh₂-tu ~ *pih₂-téw-s ( “ something fattening, nourishing ” ) 

 *péyh₂-wr̥ ~ *pih₂-wén-s ( “ fat; swelling ” ) 

 *pih₂-wes 
 Proto-Indo-Iranian: *píHwas [ 7 ] [ 8 ] [ 9 ] 
 Proto-Indo-Aryan: *píHwas 
 Sanskrit: पीवस् ( pī́vas , “ fat ” ) 

 Proto-Iranian: *píHwah 
 Avestan: 𐬞𐬍𐬎𐬎𐬀𐬵 ( pīuuah ) 

 Khotanese: [script needed] ( pyau , “ swelli
########## 1ceda065440dddc5
URL: https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D9%87
FETCHED: 2026-09-07T20:48:42Z
STATUS: 200
TITLE: پیه - Wiktionary, the free dictionary

پیه - Wiktionary, the free dictionary 

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
 Khalaj 

 Toggle Khalaj subsection 

 1.1 
 Noun 

 1.1.1 
 Declension 

 2 
 Persian 

 Toggle Persian subsection 

 2.1 
 Alternative forms 

 2.2 
 Etymology 

 2.3 
 Pronunciation 

 2.4 
 Noun 

 2.4.1 
 Derived terms 

 2.4.2 
 Related terms 

 2.4.3 
 Descendants 

 2.5 
 References 

 2.6 
 Further reading 

 Toggle the table of contents 

 پیه 

 3 languages 

 فارسی 
 Kurdî 
 Malagasy 

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

 Khalaj
 [ edit ] 

 Noun
 [ edit ] 

 پیه ( pîh ) ( definite accusative پیهی , plural پیهلَر ) 

 Arabic spelling of pîh ( “ fat ” ) 

 Declension
 [ edit ] 

 Declension of پیه 

 singular

 plural

 nominative

 پیه 

 پیهلر 

 genitive

 پیهۆݧ 

 پیهلریݧ 

 dative

 پیهکه 

 پیهلرکه 

 definite accusative

 پیهۆ 

 پیهلری 

 locative

 پیهچه 

 پیهلرچه 

 ablative

 پیهده 

 پیهلرده 

 instrumental

 پیهله 

 پیهلرله 

 equative

 پیهواره 

 پیهلرواره 

 Persian
 [ edit ] 

 Alternative forms
 [ edit ] 

 په ( peh ) , پی ( pi ) 

 Etymology
 [ edit ] 

 Inherited from Middle Persian [script needed] ( TLBA /⁠pīh⁠/ , “ fat, tallow ” ) , [ 1 ] from Old Persian [Term?] , from Proto-Indo-Iranian *piHtú , from Proto-Indo-European *péyh₂tu .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈpiːh/ 

 ( Dari, formal ) IPA ( key ) : [pʰiːʱ] 

 ( Dari, formal ) IPA ( key ) : [pʰiːʱ] 
 ( Kabuli ) IPA ( key ) : [pʰiː] 

 ( Hazaragi ) IPA ( key ) : [pʰi] 

 ( Iran, formal ) IPA ( key ) : [pʰiːʱ] 

 ( Tajik, formal ) IPA ( key ) : [pʰiʱ] 

 Rhymes: -iːh 

 Readings

 Classical reading ? 

 pīh

 Dari reading ? 

 pīh

 Iranian reading ? 

 pih

 Tajik reading ? 

 pih

 Noun
 [ edit ] 

 پیه • ( pīh / pih ) ( Tajik spelling пиҳ ) 

 fat , tallow 

 Derived terms
 [ edit ] 

 پیهبا ( pih-bâ , “ tallow soup ” ) 

 دژپیه ( dož-pih , “ tumour, ganglion ” ) 

 Related terms
 [ edit ] 

 فربه ( farbeh , “ fat, corpulent ” ) 

 Descendants
 [ edit ] 

 → Azerbaijani: piy 

 → Khalaj: pîh 

 References
 [ edit ] 

 ^ MacKenzie, D. N. ( 1971 ), “pīh”, in A concise Pahlavi dictionary , London, New York, Toronto: Oxford University Press, page 68 

 Further reading
 [ edit ] 

 Hayyim, Sulayman ( 1934 ), “ پیه ”, in New Persian–English dictionary , Teheran: Librairie-imprimerie Béroukhim 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=پیه&oldid=92230874 "

 Categories : Khalaj lemmas 
 Khalaj nouns 
 Khalaj terms in Arabic script 
 Persian terms inherited from Middle Persian 
 Persian terms derived from Middle Persian 
 Persian terms inherited from Old Persian 
 Persian terms derived from Old Persian 
 Persian terms inherited from Proto-Indo-Iranian 
 Persian terms derived from Proto-Indo-Iranian 
 Persian terms inherited from Proto-Indo-European 
 Persian terms derived from Proto-Ind
########## db89d6439aad5114
URL: https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A8%D9%87
FETCHED: 2026-09-07T20:48:43Z
STATUS: 200
TITLE: فربه - Wiktionary, the free dictionary

فربه - Wiktionary, the free dictionary 

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
 Persian 

 Toggle Persian subsection 

 1.1 
 Alternative forms 

 1.2 
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Adjective 

 1.4.1 
 Derived terms 

 1.4.2 
 Descendants 

 1.5 
 References 

 Toggle the table of contents 

 فربه 

 4 languages 

 فارسی 
 Kurdî 
 Malagasy 
 Türkçe 

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

 Persian
 [ edit ] 

 Alternative forms
 [ edit ] 

 فربی ( farbī ) 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *per- der. ? 

 Proto-Indo-European *per- der. ? 

 Proto-Indo-European *pér 

 Proto-Indo-European *-o 

 Proto-Indo-European *pró 
 Proto-Indo-European *pro- 
 Proto-Indo-Iranian *pra- 
 Proto-Iranian *fra- 

 Proto-Indo-European *peyh₂- 

 Proto-Indo-European *-tu 

 Proto-Indo-European *péyh₂tu 
 Proto-Indo-Iranian *piHtú 
 Proto-Iranian *piHtú 

 Old Persian *frapīδwa- 
 Middle Persian [script needed] ( plpyh /⁠frabīh⁠/ ) 
 Persian فربه 

 Inherited from Middle Persian [script needed] ( plpyh /⁠frabīh⁠/ ) , [ 1 ] from Old Persian *frapīδwa- , from Proto-Iranian *fra- + *piHtú ( “ fat, tallow ” ) . By surface analysis , فرـ ( far- ) +‎ پیه ( pih , “ fat, tallow ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /far.ˈbih/ 

 ( Dari, formal ) IPA ( key ) : [fäɾ.be̞ʱ] 

 ( Dari, formal ) IPA ( key ) : [fäɾ.be̞ʱ] 
 ( Kabuli ) IPA ( key ) : [fäɾ.bɪ] 

 ( Hazaragi ) IPA ( key ) : [fäɾ.bi] 

 ( Iran, formal ) IPA ( key ) : [fæɹ.beʱ] 

 ( Tajik, formal ) IPA ( key ) : [fäɾ.beʱ] 

 Rhymes: -ih 

 Readings

 Classical reading ? 

 farbih

 Dari reading ? 

 farbeh

 Iranian reading ? 

 farbeh

 Tajik reading ? 

 farbeh

 Adjective
 [ edit ] 

 فربه • ( farbih / farbeh ) ( Tajik spelling фарбеҳ ) 

 fat , corpulent 
 Synonyms: چاق ( čâq ) , لنبه ( lombe ) 

 copious , plenty 

 Derived terms
 [ edit ] 

 فربهی ( farbihī  / farbehi , “ corpulence ” ) 

 Descendants
 [ edit ] 

 Tajik: фарбеҳ ( farbeh ) 

 → Azerbaijani: fərbeh 

 → Baluchi: فَرْبَہ ( farbah ) 

 → Chagatai: فربه ( farbah, farbih ) 

 → Hindustani: 
 Hindi: फ़र्बा ( farbā ) 
 Urdu: فَرْبَہ ( farba ) 

 → Ottoman Turkish: فربه ( ferbih ) 

 References
 [ edit ] 

 ^ MacKenzie, D. N. ( 1971 ), “frabīh”, in A concise Pahlavi dictionary , London, New York, Toronto: Oxford University Press, page 32 

 Bartholomae, Christian ( 1904 ), Altiranisches Wörterbuch [ Old Iranian Dictionary ]‎ [1] (in German), Strassburg: K. J. Trübner, column 984 

 Dehkhoda, Ali-Akbar ( 1931– ), “ فربه ”, in Dehkhoda Dictionary Institute , editors, Dehkhoda Dictionary (in Persian), Tehran: University of Tehran Press . 

 Horn, Paul ( 1893 ), Grundriss der neupersischen Etymologie (in German), Strasbourg: K.J. Trübner, page 81 Nr. 365 

 Hübschmann, Heinrich ( 1895 ), Persische Studien [ Persian Studies ] (in German), Strasbourg: K.J. Trübner, pa
```


## [2026-09-07T20:49:00.174Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in a949eac8201fd441 966132e6ec2af018; do echo \"########## $f\"; sed -n '/^ From Wiktionary/,$p' $f.txt | head -80; done"
}
```


### [2026-09-07T20:49:01.411Z] TOOL RESULT

```
########## a949eac8201fd441
 From Wiktionary, the free dictionary

 See also: تنير and پنير 

 Baluchi
 [ edit ] 

 Etymology
 [ edit ] 

 From Persian پنیر ( paner ) .

 Noun
 [ edit ] 

 پنیر • ( paner ) 

 cheese 

 Khalaj
 [ edit ] 

 Noun
 [ edit ] 

 پَنیر ( pənîr ) ( definite accusative پَنیری , plural پَنیرلَر ) 

 Arabic spelling of pənîr ( “ cheese ” ) 

 Declension
 [ edit ] 

 Declension of پنیر 

 singular

 plural

 nominative

 پنیر 

 پنیرلر 

 genitive

 پنیرۆݧ 

 پنیرلریݧ 

 dative

 پنیرکه 

 پنیرلرکه 

 definite accusative

 پنیرۆ 

 پنیرلری 

 locative

 پنیرچه 

 پنیرلرچه 

 ablative

 پنیرده 

 پنیرلرده 

 instrumental

 پنیرله 

 پنیرلرله 

########## 966132e6ec2af018
 From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 انگبین 
 Etymology
 [ edit ] 

 From Middle Persian [Book Pahlavi needed] ( DWBŠYA, ʾngpyn' /⁠angubēn⁠/ , “ honey ” ) , from Proto-Iranian *Hangubáynah .

 Cognate with Northern Kurdish hingiv , Zazaki engemin , Central Kurdish ھەنگِوین ( hengiwîn ) and Talysh انگوین ( anqevin ) .

 Probably not related انگ ( ang , “ yellowjacket ” ) ; instead related to انگم ( angom , “ resin ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔan.ɡu.ˈbiːn/ , /ʔan.ɡa.ˈbiːn/ 

 ( Dari, formal ) IPA ( key ) : [ʔäŋ.ɡä.biːn] 

 ( Dari, formal ) IPA ( key ) : [ʔäŋ.ɡä.biːn] 
 ( Kabuli ) IPA ( key ) : [ʔäŋ.ɡä.biːn] 

 ( Hazaragi ) IPA ( key ) : [ʔäŋ.ɡä.bin] 

 ( Iran, formal ) IPA ( key ) : [ʔæŋ.ɡo.biːn] , [ʔæɲ.ɡʲæ.biːn] 

 ( Tajik, formal ) IPA ( key ) : [ʔäŋ.ɡu.bin] 

 Rhymes: -iːn 

 Readings

 Classical reading ? 

 angubīn, angabīn

 Dari reading ? 

 angabīn

 Iranian reading ? 

 angobin, angabin

 Tajik reading ? 

 angubin

 Noun
 [ edit ] 

 Dari

 انگبین 

 Iranian Persian

 Tajik

 ангубин 

 انگبین • ( angubīn, angabīn / angabin ) ( Tajik spelling ангубин ) 

 ( archaic ) honey 
 Synonyms: عسل ( asal ) , شهد ( šahd ) 
 c. 1520 , Selim I of the Ottoman Empire , edited by Benedek Péri, The Persian Dīvān of Yavuz Sulṭān Selīm , Budapest, Hungary: Research Centre for the Humanities, Eötvös Loránd Research Network, →ISBN , page 205 : دوا جستم برای درد دل افزون صد دردم
مگس‌وار انگبین کردم طمع زان مبتلا گشتم dawā justam barā-yi dard-i dil afzwun sad dardam
magas-wār angubīn kardam tam' z-ān mubtalā gaštam I sought a cure for my heart's pain, and my pain increased a hundredfold;
I craved for honey like a fly, and I was captured by that. (Classical Persian transliteration) 

 Derived terms
 [ edit ] 

 ترانگبین ( tar-angobin , “ Persian manna ” ) 
 سرکنگبین ( serkangobin , “ vinegar-honey drink ” ) 
 مگس انگبین ( magas-e angobin , “ honeybee ” ) 
 گزانگبین ( gaz-angobin , “ tamarisk manna ” )
```


## [2026-09-07T20:49:15.215Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### panir persian\"; grep -n -A25 \"^ Persian$\" a949eac8201fd441.txt | head -60; echo \"#### pectus\"; sed -n '/^ From Wiktionary/,$p' d18d2741d620b330.txt | grep -n -B3 -A18 \"Latin\" | head -60"
}
```


### [2026-09-07T20:49:16.613Z] TOOL RESULT

```
#### panir persian
675: Persian
676- [ edit ] 
677-
678- Persian Wikipedia has an article on: پنیر 
679-
680- Wikipedia fa 
681-
682- پنیر 
683- Etymology
684- [ edit ] 
685-
686- From Middle Persian pnyl ( panīr ) ; see there for further information.
687-
688- Pronunciation
689- [ edit ] 
690-
691- ( Classical Persian ) IPA ( key ) : /pa.ˈniːr/ 
692-
693- ( Dari, formal ) IPA ( key ) : [pʰä.níːɾ] 
694-
695- ( Dari, formal ) IPA ( key ) : [pʰä.níːɾ] 
696- ( Kabuli ) IPA ( key ) : [pʰä.níːɾ] 
697-
698- ( Hazaragi ) IPA ( key ) : [pʰä.níɾ] 
699-
700- ( Iran, formal ) IPA ( key ) : [pʰæ.níːɹ] 
#### pectus
6- Etymology
7- [ edit ] 
8-
9: Borrowed from Latin pectus .
10-
11- Noun
12- [ edit ] 
13-
14- pectus ( plural pectora ) 
15-
16- ( anatomy , zoology ) The breast , especially of a bird .
17-
18- Related terms
19- [ edit ] 
20-
21- pectoral 
22-
23- pectus excavatum 
24-
25- pectus carinatum 
26-
27- Anagrams
--
29-
30- cupset 
31-
32: Latin
33- [ edit ] 
34-
35- Etymology
36- [ edit ] 
37-
38- Likely cognate with Old Irish ucht , but a Proto-Indo-European precursor is uncertain, as is the connection to Sanskrit पक्ष ( pakṣá , “ wing ” ) . [ 1 ] Suggestions include *pekt- , *pek- and *peg- ( “ breast ” ) . ( Can this ( + ) etymology be sourced ?) 
39-
40- Pronunciation
41- [ edit ] 
42-
43: ( Classical Latin ) IPA ( key ) : [ˈpɛk.tʊs] 
44-
45- ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈpɛk.tus] 
46-
47- Noun
48- [ edit ] 
49-
50- pectus   n ( genitive pectoris ) ; third declension 
51-
52- chest , breast 
53-
54- ( figuratively ) heart , breast, as the seat of emotion 
55- Synonym: cor 
56-
57- ( figuratively ) soul , spirit , mind , understanding 
58- Synonym: animus 
59- 8 CE , Ovidius , Fasti 6.509 : ‘ō nimium facilēs, ō tōtō pectore captae!’ “O too easy [souls]! O [those] with every spirit having been captured!” 
60-(That is to say, easy to deceive and entirely believing. Several figurative translations are possible. The poetic voice is that of Juno (mythology) .) 
61-
--
181- References
182- [ edit ] 
183-
```


## [2026-09-07T20:49:24.216Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '/ References/,$p' d18d2741d620b330.txt | head -20; echo \"#### punkah wikt\"; sed -n '/^ From Wiktionary/,$p' f9298bef58c5abcf.txt | head -40; echo \"#### etymonline punkah\"; grep -n -i -A10 \"punkah\" a1800cbbb6b4e947.txt | head -40"
}
```


### [2026-09-07T20:49:25.490Z] TOOL RESULT

```
 References 

 2.5 
 Further reading 

 Toggle the table of contents 

 pectus 

 31 languages 

 Aragonés 
 Català 
 Corsu 
 Čeština 
 Deutsch 
 Ελληνικά 
 Español 
 Eesti 
 فارسی 
#### punkah wikt
 From Wiktionary, the free dictionary

 English
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from Hindi पंखा ( paṅkhā , “ fan ” ) , from Sanskrit पक्षक ( pakṣaka ) , from पक्ष ( pakṣa , “ wing ” ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ˈpʌŋkə/ , /ˈpʌŋkɑː/ 

 Rhymes: -ʌŋkə 

 Noun
 [ edit ] 

 punkah ( plural punkahs ) 

 ( South Asia , Myanmar ) A fan , particularly a large fan made of leaf or cloth and hung from the ceiling , ( historical ) formerly often operated by a servant .
 1810 , Thomas Williamson, East India Vade-Mecum... , page 313 : A punkah is, by some, used instead of a chattah , (or umbrella); but it is very inferior as a defence against either sun, wind, or rain. 

 1900 , Joseph Conrad , chapter 4, in Lord Jim : Outside the court the sun blazed—within was the wind of great punkahs that made you shiver … 

 1943 November and December, G. T. Porter, “The Lines Behind the Lines in Burma”, in Railway Magazine , page 325 : In the refreshment room a few would-be passengers were cooled by the punkah , worked by a string tied to the big toe of a sleepy Burmese boy. 

 1973 , Patrick O'Brian , HMS Surprise : Perhaps it was a mistake to invite Mr Stanhope; the day was intolerably hot and humid; all he wanted to do was to lie on his bed with a punkah sighing over him, at least moving the unbreathable air. 

 Derived terms
 [ edit ] 

 punkahwallah 

 Translations
 [ edit ] 

 fan
#### etymonline punkah
1:URL: https://www.etymonline.com/word/punkah
2-FETCHED: 2026-09-07T20:48:40Z
3-STATUS: 200
4-TITLE: Etymonline - Online Etymology Dictionary
5-
6-Etymonline - Online Etymology Dictionary 
7-
8- Search 
9- Log in 
10-
11- Columns
```


## [2026-09-07T20:49:32.544Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"Hindi\\|Sanskrit\\|1620\\|fan\" a1800cbbb6b4e947.txt | head -20; echo \"#### pinus latin\"; sed -n '/^ From Wiktionary/,$p' f916d981e118edb1.txt | grep -n -A20 \"^ Latin$\" | head -40; echo \"#### paksa\"; sed -n '/^ From Wiktionary/,$p' 3fa7430102cf8af4.txt | grep -n -A30 \"Sanskrit\" | head -60"
}
```


### [2026-09-07T20:49:33.755Z] TOOL RESULT

```
#### pinus latin
57: Latin
58- [ edit ] 
59-
60- pīnus (a pine) 
61- Etymology
62- [ edit ] 
63-
64- From Proto-Italic *pīnos , of disputed origin, with multiple theories proposed: [ 1 ] 
65-
66- From the same origin as Ancient Greek πῐ́νᾰξ ( pĭ́năx , “ wooden board, plank ” ) .
67-
68- From the same origin as Ancient Greek πίτῠς ( pítŭs , “ pine tree ” ) and Albanian pishë ( “ id ” ) , which is generally reconstructed as Proto-Indo-European *pī́ts .
69-
70- Related to pix ( “ pitch, tar ” ) , itself generally considered of the same origin as the second etymology above.
71-
72- See also Sanskrit पितु ( pitu , “ sap, juice, resin ” ) .
73-
74- Pronunciation
75- [ edit ] 
76-
77- ( Classical Latin ) IPA ( key ) : [ˈpiː.nʊs] 
#### paksa
15: Borrowed from Sanskrit पक्ष ( pakṣa ) .
16-
17- Pronunciation
18- [ edit ] 
19-
20- ( Standard Hindi ) IPA ( key ) : /pəkʂ/ , [pɐkʃ] 
21-
22- Noun
23- [ edit ] 
24-
25- पक्ष • ( pakṣ )  m 
26-
27- faction , side , party 
28- Synonym: तरफ़ ( taraf ) 
29- पक्ष साथ-साथ लड़ रहे थे। pakṣ sāth-sāth laṛ rahe the. The factions were fighting amongst themselves. 
30-
31- aspect , quality 
32-
33- support , approval 
34-
35- ( Hinduism ) paksha , lunar fortnight 
36- Synonym: पखवाड़ा ( pakhvāṛā ) 
37-
38- Declension
39- [ edit ] 
40-
41- Declension of पक्ष (masc cons-stem) 
42-
43- singular
44-
45- plural
--
120: Learned borrowing from Sanskrit पक्ष ( pakṣa ) .
121-
122- Pronunciation
123- [ edit ] 
124-
125- IPA ( key ) : /pək.ʂə/ 
126-
127- Audio : ( file ) 
128-
129- Noun
130- [ edit ] 
131-
132- पक्ष • ( pakṣa )  m 
133-
134- ( politics ) political party 
135- Synonym: राजकीय पक्ष ( rājakīya pakṣa ) 
136-
137- fortnight in lunar month 
138-
139- side ; position in a discussion , argument etc.
140-
141- Declension
142- [ edit ] 
143-
144- Declension of पक्ष (masc cons-stem) 
145-
146- singular
147- एकवचन
```


## [2026-09-07T20:49:43.684Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && awk '/^ Sanskrit$/{f=1} f' 3fa7430102cf8af4.txt | head -60; echo \"#### etymonline\"; wc -l a1800cbbb6b4e947.txt; sed -n '1,80p' a1800cbbb6b4e947.txt"
}
```


### [2026-09-07T20:49:44.991Z] TOOL RESULT

```
 Sanskrit
 [ edit ] 

 Alternative scripts
 [ edit ] 

 Alternative scripts
 পক্ষ ( Assamese script ) 
 ᬧᬓ᭄ᬱ ( Balinese script ) 
 পক্ষ ( Bengali script ) 
 𑰢𑰎𑰿𑰬 ( Bhaiksuki script ) 
 𑀧𑀓𑁆𑀱 ( Brahmi script ) 
 ပက္ၑ ( Burmese script ) 
 પક્ષ ( Gujarati script ) 
 ਪਕ੍ਸ਼ ( Gurmukhi script ) 
 𑌪𑌕𑍍𑌷 ( Grantha script ) 
 ꦥꦏ꧀ꦰ ( Javanese script ) 
 𑂣𑂍𑂹𑂭 ( Kaithi script ) 
 ಪಕ್ಷ ( Kannada script ) 
 បក្ឞ ( Khmer script ) 
 ປກ຺ຩ ( Lao script ) 
 പക്ഷ ( Malayalam script ) 
 ᢒᠠᡬᢢᠠ ( Manchu script ) 
 𑘢𑘎𑘿𑘬 ( Modi script ) 
 ᢒᠠᢉᢔᠠ᠋ ( Mongolian script ) 
 𑧂𑦮𑧠𑧌 ( Nandinagari script ) 
 𑐥𑐎𑑂𑐲 ( Newa script ) 
 ପକ୍ଷ ( Odia script ) 
 ꢦꢒ꣄ꢰ ( Saurashtra script ) 
 𑆥𑆑𑇀𑆰 ( Sharada script ) 
 𑖢𑖎𑖿𑖬 ( Siddham script ) 
 පක්‍ෂ ( Sinhalese script ) 
 𑩰𑩜 𑪙𑪀 ( Soyombo script ) 
 𑚞𑚊𑚶 ( Takri script ) 
 பக்ஷ ( Tamil script ) 
 పక్ష ( Telugu script ) 
 ปกฺษ ( Thai script ) 
 པ་ཀྵ ( Tibetan script ) 
 𑒣𑒏𑓂𑒭 ( Tirhuta script ) 
 𑨞𑨋𑩇𑨯 ( Zanabazar Square script ) 

 Etymology
 [ edit ] 

 Probably from Proto-Indo-Iranian *pakšás ( “ side, flank ” ) , from Proto-Indo-European *peg- ( “ side, flank ” ) .

 Cognate with Ossetian фахс ( faxs , “ side ” ) and maybe Latvian paksis ( “ corner of a house ” ) . [ 1 ] 

 Alternatively, from a Proto-Indo-Iranian *paćšás and cognate with Prasuni [script needed] ( obuć , “ side ” ) , Waigali pāći ( “ side ” ) .

 Pronunciation
 [ edit ] 

 ( Vedic ) IPA ( key ) : /pɐk.ʂɐ́/ 

 ( Classical Sanskrit ) IPA ( key ) : /pɐk.ʂɐ/ 

 Noun
 [ edit ] 

#### etymonline
48 a1800cbbb6b4e947.txt
URL: https://www.etymonline.com/word/punkah
FETCHED: 2026-09-07T20:48:40Z
STATUS: 200
TITLE: Etymonline - Online Etymology Dictionary

Etymonline - Online Etymology Dictionary 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 

 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.

 About
 Who Did This 
 Sources 
 Introduction 
 Links 

 Support
 Premium 
 Patreon 
 Donate with PayPal 
 Merch 

 Apps

Get Chrome Extension 

Get iOS App 

Get Android App 

 Dark
 Auto
 Light

 Terms of Services Privacy Policy 

 English (English) 
 © 2001–2026 Douglas Harper & Talia Felix
```


## [2026-09-07T20:50:00.897Z] TOOL CALL #52: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%82%E0%A4%96%E0%A4%BE\" \\\n \"https://en.wiktionary.org/wiki/pan%C4%ABr\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/p%C3%A1yHas\" \\\n \"https://en.wiktionary.org/wiki/fat\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 385, roots Peg / Pei: node verification\" ; done"
}
```


## [2026-09-07T20:50:03.082Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS\"; grep -n -i \"panir\\|panīr\\|pēm\\|pem \\|pih\\|pīh\" SNS.txt | head -20; echo \"=== LKT pankha\"; grep -n -i \"pankha\\|punkah\\|pinu\\|angubin\" LKT.txt | head -10; echo \"=== ARY\"; for w in پیه پنیر انگبین فربه پینو; do echo \"-- $w\"; grep -c \"$w\" incoming/ARY/ARY_pages.txt; done"
}
```


### [2026-09-07T20:50:05.702Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/719d10c4845aca28.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1ea1261a4b155047.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2ca1ea8f1b569a6f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6c5cb6d0f5cc67b0.txt
```


### [2026-09-07T20:50:06.973Z] TOOL RESULT

```
=== SNS
8290:.Ui ?>&#» :pihan/pihn: \^JU 
8291:642-906) ?pihn : j*4* pi-Ow* : *- 
10809:■ o 1 *- 1 "^* *.*-- rspihr: ^-*otMJ 
31431:spihr 176/19 
31506:pihan/pihn 123/18 
=== LKT pankha
479:'Eine  Fichtenart,  pinus  cedrus'.  Hieraus mit  dem  ar.  Art.  sp.  alerce  'Lärche'; siz.  arzanu  'Tanne'.  Auffallend  ist  die Ähnlichkeit  mit  lat.  lärix,  laricem,  wor- aus it.  larice,  pg.  larico;  dtsch.  Lärche. [GrSVociSic  227.    ML  635.    DE  98.
3709:1622.  Hind.  pankha:
3710:'Fächer';  hieraus  angloind.  en^l.punkah 'Fächer  aus  den  Blättern  der  Fächer- palme Borassus  flabelliformis',  ins- besondere ein  fester,  schwingender Fächer,  der  an  der  Decke  hängt,  um  die Luft  bei  warmem  Wetter  in  Bewegung zu  halten ;  es  ist  also  eine  Art  Ventilator, der,  brettartig,  an  mehreren  Fäden  von der  Decke  des  Zimmers  herabhängt  und vermittelst  eines  durch  die  Wand  ge- zogenen Stricks  von  einem  außerhalb des  Zimmers  befindlichen  Diener  in  un-
6147:j  /)oZo  1666 popingay  147 ^•«M  1651 ^/•ow  1651 />McÄra  983.  1614 punch  1619 punkah  1622 Pyjamas  1606 pyjamma  1606 pyramid  1457
=== ARY
-- پیه
1
-- پنیر
1
-- انگبین
0
-- فربه
0
-- پینو
1
```


## [2026-09-07T20:50:15.403Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    for w in ['پیه','پنیر','پینو']:\n        if w in p:\n            j=p.find(w)\n            print('### leaf',i,w)\n            print(p[max(0,j-800):j+500])\nEOF"
}
```


## [2026-09-07T20:50:16.225Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('LKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if '1622.  Hind.  pankha' in p or '1622. Hind. pankha' in p:\n        print('leaf',i,'printed~',i-26)\nEOF"
}
```


### [2026-09-07T20:50:16.743Z] TOOL RESULT

```
### leaf 183 پنیر
[pdf page 184]
پیئو» پینوک (به چم / ۱۸۵
(از فرانسه‌ی‌کهن) ود پسگشت‌ها کی
انگلیسی (50لا8(/0): ۳ ان ۳
لیتوانی (7141۸2/40۷/رت): ادا 8 (۳82) :7
پروسی کهن (۳۴55314۸ 0ا0): الدد نا :ا(سا05
ایرلندی کهن (ا5ل#] 0(2: ۸ #ل۸ 1 (08 7 )
گالی ((8لالا0۸): -۸ 4 (87085) ,68 :۸۸215
آلبانی (0۷فاامقلم): 72۸ 3 (88۸8۰) :0۸105

0 (5) :57
برهان قاطع + ۳۴۰
بادداشت:
واژه‌ی انگلیسی 7 عم از همین ریشه است (۳0160۸۲۷:812).
اوستایی (4857۸27): یترانی (40742نا4ل7ل): 2۸5
۳۸۷۸۹۰ +ا۳۸3۸۸۵ تل۸ 2۸
سانسکریت (54۸/5777): پسگشت‌ها بدا درد
۳۷۸۸75 ,8180۷۸33 ,۳۸۸75 زر
ایسلندی کهن (140/ 90/0/0 صا0): 6 (81) +537
۱ 1۸ برهان قاطع : ۳۴۹
انگلیسی کهن (0ل8ل/80/0 2 7۸3/8 فرهنگ معین : ۹۶۹-۰
روژی (اممزه من دا لغت‌نامه دهخدا ۶۳
بادداشت:. ۹
۱- به احتمال زیاد واژه‌ی "پنیر" (پهلوی: ۱۳۸۷1 کردی: ۳338131) نیز از همین ريشه است.
۲- چم این واژه در سانسکریت: ورم کردن؛ یاد کردن,
چم این واژه در زبان‌های ژرمنی: خامه» سرشیر,
چم این واژه در زبان لیتوانی؛ شیر,

### leaf 183 پینو
[pdf page 184]
پیئو» پینوک (به چم / ۱۸۵
(از فرانسه‌ی‌کهن) ود پسگشت‌ها کی
انگلیسی (50لا8(/0): ۳ ان ۳
لیتوانی (7141۸2/40۷/رت): ادا 8 (۳82) :7
پروسی کهن (۳۴55314۸ 0ا0): الدد نا :ا(سا05
ایرلندی کهن (ا5ل#] 0(2: ۸ #ل۸ 1 (08 7 )
گالی ((8لالا0۸): -۸ 4 (87085) ,68 :۸۸215
آلبانی (0۷فاامقلم): 72۸ 3 (88۸8۰) :0۸105

0 (5) :57
برهان قاطع + ۳۴۰
بادداشت:
واژه‌ی انگلیسی 7 عم از همین ریشه است (۳0160۸۲۷:812).
اوستایی (4857۸27): یترانی (40742نا4ل7ل): 2۸5
۳۸۷۸۹۰ +ا۳۸3۸۸۵ تل۸ 2۸
سانسکریت (54۸/5777): پسگشت‌ها بدا درد
۳۷۸۸75 ,8180۷۸33 ,۳۸۸
### leaf 184 پیه
[pdf page 185]
اٍ ۶ پیه
| م‌انکلیسی سرواژهی نار رو 1385
اوستایی (۸۲887۸1): انگلیسی کهن (87ا8/0 ۰۰:۵2 ۳۸3۳ :تب
-۳۳۷۸ ,201773۷۷۸ ,نا۴17 انگلیسی (8(/01/877): ۳۸7
پارسی پاستان(2288407 صا۵): ۰۰ ۲1773۲ دانمارکی (0۸(/187): راد
پهلوی (ماقلهه): 1 سرئدی (5۲780/37): لاین ۱
اوستی (05587[76): 7 ,31۷ نروژی (۸/0۳780۵۸)+ 77
کردی (7ل0/5ل0): زر هلندی (007677): ۷7
بلوچی (31ل6لام): ۳6 لینرانی (۵(۷1۸0تا77ل): دا
سانسکریت (854867): ایرلدی کهن (نل5لجا 0ا :)0‏ " 11
۸ ل ۴17 ,۸5 ۷]ظ َ
یونانی (07280): 85 ,۶1۸ پسگشت‌ها اند ای دی دنا ۲
لاین ۰:0
```


### [2026-09-07T20:50:18.120Z] TOOL RESULT

```
leaf 158 printed~ 132
```


## [2026-09-07T20:50:44.456Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i,p in enumerate(t):\n    if 'فربه' in p or 'فربی' in p:\n        print('leaf',i,'printed~',i+1208)\nEOF"
}
```


### [2026-09-07T20:50:45.752Z] TOOL RESULT

```
leaves 721
leaf 22 printed~ 1230
leaf 30 printed~ 1238
leaf 36 printed~ 1244
leaf 61 printed~ 1269
leaf 80 printed~ 1288
leaf 115 printed~ 1323
leaf 154 printed~ 1362
leaf 176 printed~ 1384
leaf 192 printed~ 1400
leaf 200 printed~ 1408
leaf 207 printed~ 1415
leaf 219 printed~ 1427
leaf 220 printed~ 1428
leaf 233 printed~ 1441
leaf 242 printed~ 1450
leaf 253 printed~ 1461
leaf 257 printed~ 1465
leaf 259 printed~ 1467
leaf 262 printed~ 1470
leaf 264 printed~ 1472
leaf 275 printed~ 1483
leaf 276 printed~ 1484
leaf 299 printed~ 1507
leaf 323 printed~ 1531
leaf 335 printed~ 1543
leaf 360 printed~ 1568
leaf 379 printed~ 1587
leaf 397 printed~ 1605
leaf 411 printed~ 1619
leaf 422 printed~ 1630
leaf 436 printed~ 1644
leaf 447 printed~ 1655
leaf 496 printed~ 1704
leaf 586 printed~ 1794
leaf 623 printed~ 1831
leaf 625 printed~ 1833
leaf 631 printed~ 1839
leaf 638 printed~ 1846
leaf 650 printed~ 1858
leaf 673 printed~ 1881
leaf 685 printed~ 1893
leaf 688 printed~ 1896
```


## [2026-09-07T20:50:49.502Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[242]\nprint(p[:4000])\nEOF"
}
```


### [2026-09-07T20:50:50.871Z] TOOL RESULT

```
[pdf page 243]
فربود
8 99 ۱ ۰ با بای ابجدبروزن‌فرموده
یمعنی راست ودرست ‎ath‏ چه فربود کیش‌وفربود
دی نکیرا گونند که در کیش وملت ومذهب‌خود
راست ودرست باشد .

فر بودگ ؟ = بروزن‌امودی ‎ine‏
‏فربود دین است ‎TOT,‏ باشد که دردین وملت
خود ‎cl)‏ و درست باشد .۷

‎wr‏ ۴ = بفتح اول وسکون انی‌وبای
ابجد بتحتالی‌رسیده. بمعنی فربه باشد که‌درمقابل

‏لاغر است .

‎Foss‏ با بای ابجد . بر وزن
ومعتی فرفیون است » ون داروبی باشد دوابی.

‏وا

‏فرت ‎oie‏ اول وسکون ثالیوفوفانی»
تانه و تارهای جامه ‎ath‏ که جولاهگان بجهت
یافتن آراسته و مرتب ساخته باشند - ‎ping‏ اول
گیاهی است که درد شکم را سود دارد وروشن
کردن و صاف کردن دل را نیز گویشد بربانت
وطاعت و آنرا بعربی مجاهده خوانندث .

‎۳ air ۵

‏فر ناش.۱ ح_باتای‌قرشت بروزن‌پررخاش»
بمعنی وجود است که در برابرعدم باشد .

‏فر نوت ۲ = بانای‌فرشت بروزن‌مر ‎shy‏
‏پرسالتخورده وخرف شده واز کار رفته را گوبند.

‏فر وث 4 = باواومجپول بروزنمحمود,
‎aw‏ فرتوت است که پیرسالخورده واز کارافتاده

‏وخرف باشد .

‏چون ب رگز ند گی‌جانورانوسکگ دبوانه طلاکنند
فر ود * - بنتحاول ‎lt‏ وسکون‌انی

‎. ‏باشد‎ gl

‎fraybut ۰ ‏مناعت ؛ تکیر « تاوادیا ص۱۸۱‎ caw fre - DOL ‏در پهلوی‎ ٩
, . ‏کیوان است‎ ST BS Lay ‏متن‎ Cove ‏(کترت . افراط ) « مناس‎

‎= frapth sale < ‏رك:فربود . ۴ - ازاوستا -2 2۳00100۷ = فربی‎ - ۴
۰۷۹۱ ‏شکند گماندك‎ « ) Sle . ‏(فربه‎ Pit sol. = padh ‏فی پازند‎ .ofrapithwa_? ‏ایستا‎
‏اسشق‎ « farbé ‏باستان - ۳۳۵810۷ , وخی ع 82۳01 , سریکلی‎ sae . ۸۱۳ olay?
Henning, A list of Middle persian..., ) ‏(چاق‎ frhyw ‏در اوراق‌مانوی‌بپارتی‎ ۳
BSOS,IX, |,p.82.

‏= فرفبون ‎(pe)‏ = افریون » عربی ازیوتاتی ‎Euphérbion‏ ذ عقار ۰۲۵ .

‏۴ - فریبون (جم‌اول) = ‎cévadille‏ (فی) ‎crave‏

‎٩‏ - در فرهنگه ‎le‏ « فرتود » بممنی روشن ساختن دل و ‎hake‏ قلب است برنج و
ربانت و پرستش ‎Ob py‏ که بتازی مجاهده کویند و ‎Leg‏ لفظ اتراقمت چه حکیم اشراقی را
+ فرتودی » گویند . از ‎whe‏ این ممنی معلوم و مرقوم گردیده (۱) « فرهنگه دسائیر ۷۵۹ ۰ .

‏-ظ . ‎ALS STS) SL,‏ . ۷ فرنود ! کردی ع 070066] (عجوزه)
‎LIS?‏ س ۲۹۰ » «فرتوت . سخت پیر و خرف باشد . رودکی (سمرقندی) گوید :
دولت او مرا بکرد جوان.» ‎cal?‏ فری 90

‎(pe) og pm A‏ قس : توت تود : « یکی را زنی صاحب جمال جوان در گذشت
و مادر زن فرتوت بعلت کابین درخانه متمکن بمالد. » «کلتان ‎VEE‏

‎«٩‏ فرتور ؛ عکس بود شم

‎.» ۱۹4 ‏می از قدح: فتاده برسفف سرا چوآب روشن. » « لت فری‎ od
‏این‌کلمه. (پرتوی می ) [با: قرتو می بکسر واو. مم. ) تبوده وغلطخوانده‌شده‌است؟ (دهخدا).‎ LT
+ td : ‏بفتح اول وکسرسوم » رك‎ ado

‏پیر فرتوت گشته بودم سخت

‏) برهای قاطع ۱۸ )
```


## [2026-09-07T20:51:25.068Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('v2 leaves',len(t))\np=t[309]\nprint(p[:2500])\nEOF"
}
```


### [2026-09-07T20:51:26.490Z] TOOL RESULT

```
v2 leaves 684
 ‫دربو‬                                                                                                  ‫‪٩‎‬و‬

‫و کردا کرد خانه واطراف هرچیز رادز کفته‌اند‬                ‫در یم د بکراول وانی‌سحتانیمجهول‬
‫در انداژند تا در کشوده‬        ‫و چوییکه در پس‬             ‫طمه ابست که آبرا‬
                                                                        ‫کشده و یفن نقطه دار زده »‬
          ‫لگردد ؛ ویکراول هم مده است `‬                    ‫درمقام تأسف و حسرت کویند ‪ -‬وبمعنی افوس‬
                                                           ‫شتته‬‫ذا‬‫گصیر‬
                                                                    ‫واندوه ودشوار واندوه کردن بر تق‬
‫در بور ‪ ۴‬هبسر وزن هر روز ‪ ۰‬بمعلی‬
                                                                     ‫باشد؛ وبضم اول هم بنظرآمده است ‪.‬‬
         ‫و کدابی باشد ‪.‬‬       ‫به‬
                               ‫کتدکه‬
                                   ‫دربوزه ام‬

‫در بوری ‪ = ۴‬بروزن هرروزه » بسعئی‬
                                                          ‫دریگان ‪ ۱‬بااك مجهول کواف‬
                                                         ‫فارسی بروزن حریفان ‪ ۰‬نوعی از اعمال و اشکال‬
          ‫دربوزاست که کدبه و کدابی باشد هة‬
                                                                  ‫فجومی باشد » ومعرب آن دریجان است ‪.‬‬
‫در بوش ؟ ‪ -‬بروزن خر کوش کدا‬
                                   ‫‪a‬‬


                                                         ‫در یو اس (‪)١‬ہ‏ با الك مجهول وواو‬
                  ‫ومسکن را گونند ‪۰‬‬          ‫ودرورش‬
                                                          ‫بروزن بلیناس » چارچوب در خانه راکویند =‬




                                                                          ‫)‪ (۱‬چش ‪ :‬دربوای (‪)۱‬‬

  ‫درکان ‪ 202606۲‬درهندوی‌مر کب از‪( ۱۲ = 1۲1 :‬ے) ‪ ( 20۵۷ +‬بخش»‬                                       ‫‪۱‬‬
 ‫بیرولی درتحقیق ماللهند(ص‪ )۷۰۳‬کوید ‪ 2:‬الا ثلاثو نسمی دریکان ولافائدة‬                 ‫بپر) * نی سه‌بهره‬
  ‫فی‌ذ کرها لانها ای تسمی عندنا دربجانات سنها؛‪ .‬وهمو درالتنهیم (س ‪ )4۰4‬آرد‪«:‬دریگان‌چست؟‬
 ‫وخداو ندانثان بخلاف و حوه»‬    ‫‪ ۰‬ومردمان ما آ را در بسجان‌خوانند»‬      ‫برجهااند نزديك حندوان‬            ‫هم سك‬

‫يدجم برجرا ازاو ‪ 1‬وسوم‌خداو ند‬         ‫خداوند‬    ‫ازهر برجی خداو ندش راباشد ‪a‬‏ ودوم‬   ‫دریسجان‬       ‫نشتین‬     ‫که‬


  ‫هم را» وسپس بیرونی جدول خداوندان وجوه ودریگان رائت کرده است ‪ .‬رك ‪ :‬التاهیمص ‪404‬‬
        ‫رك ‪:‬درنوژه ‪.‬‬      ‫‪۳‬‬             ‫‪.‬‬   ‫‪۷۳۳‬‬    ‫مورك‪ :‬تقی زاده‪
```


## [2026-09-07T20:51:37.768Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,unicodedata\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\ndef clean(s):\n    return re.sub(r'[‌‎‏‪-‮⁦-⁩\\s]','',s)\nfor i,p in enumerate(t):\n    c=clean(p)\n    for w in ['ژپیه','دژپ','دشپ','ژپبه']:\n        if w in c:\n            print('leaf',i,'printed~',i+543,w)\nEOF"
}
```


### [2026-09-07T20:51:39.507Z] TOOL RESULT

```
leaf 9 printed~ 552 دشپ
leaf 200 printed~ 743 دشپ
leaf 293 printed~ 836 دشپ
leaf 325 printed~ 868 دشپ
leaf 575 printed~ 1118 دشپ
```


## [2026-09-07T20:51:47.824Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\ndef clean(s): return re.sub(r'[‌‎‏‪-‮⁦-⁩]','',s)\nfor i in [293,325,300,305,310,315,320]:\n    c=clean(t[i])\n    print('=== leaf',i,'printed~',i+543)\n    print(c[:600].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-07T20:51:49.149Z] TOOL RESULT

```
=== leaf 293 printed~ 836
   ے6 |   درحسی                                                                                        سح     ۳۳ |  |  |  | از زنبور سياه هم هت که چوب را ضوراخ                      درج تنگ کنایه ازدمان معشرق |                                          میکند . ۴                                                    است . | درختلك دانا س بکر کاف » دم                               درح  ۱كر = ضم دال دوم » بمعنی | فهتأاب بکرددبر کپای       درختیاست که بپرجانب ک         اهیه ازدهان معشوق باشد . |                                                                                 درج تنک اکستنک |  کوبند درخت ی ض ع ب و  ٩ آن روی
=== leaf 325 printed~ 868
                                                        بیان دهم |      تست وذو لقت و کنات                       نقطه دار مشتمل بو                     در دال بی نةطه مأ شن |  |                                                                                                                       ھ |  .هت |    بجوشد |        بد وزشت وپیل ( )۳بمعنی کره با                              دس » بفتحاول وسکونتانی» خودآرایی | تخفیف تارا الداختهالد دشپیل()4شدهاست همجو                       وخود راساختن وآراستن  -وصورت خوش -وشبه | دشمن که آن دشت من بوده معنی بد دل وزشت                                                       
=== leaf 300 printed~ 843
        رح |  |  ولام وسکونالی      در لك  = ۳تکراول                         در لك = بقتح اول بروزن قدك,دستارجه | وکاف  .جام کوناه قد آستن کوناه پیش واز را                 رگاونند که رومال ورویاك باشد ؛ و باين معثی |                                                وتف        بجای حرف انی زای نقطهدار همأ مدهاست -ودر |  |  در لورینه سیر خوردن - ۴                                                               عربی مممنی مال باشد . |  | کنابه از فرب خوردن  -و کردنکاری باشد" که | عمش کنن را منخص سازند  -ویمعئی درشادیغم                   ۰و عصی یخی را گوند که درزیرناودان           گوند |  |                                 
=== leaf 305 printed~ 848
  دره                                                                                                                ز6ح |                                                                                                                        بی |  |  |  کنابه ازشکم باشد ©  -و قوس قزح (- ۱ )۳                         بشکل عقرب وببب آن درونج عفربی خوانندش. |  کومانحلاجی رانیزکوبندا ؛ وم اول همبدو                      کرم وخشكاست دردویم( ۱)۰کز ندکیجانورانرا |   ون |    ک۳م)ا |        معنی آخر است کقهوس قزح (                                کوش اکر فدری از آن درمانخانه                         افع است |  |              
=== leaf 310 printed~ 853
                                              يان هفتم |                 در دال بینقطه با زای نقطه دار مشتمل بر ده لغت |  |  |                           وزهره وعطارد باشد *.           در = بکر اول و سکون ثالی » قلعه |                                                           بالاخاله را   وبفتح اول کوثشك و        ۳ ۱       وحصارباشد | فلك  ,دمتار را گویند      بروژن    =   درك |  | دستارچه را    و روپاك است ؛ :و بى         که یل            کربند؛ و با زای ( )۱فارسی هم باين دو معنی |                                                                                                 آهوه است (<( ۳ |               گفتها
=== leaf 315 printed~ 858
 دستاران                                                                                           -وو ارات |  |  هست  -وفتح و نصرت وفیروزی  -و فرصت  | -لومسند همچنان که اسب را سر وشتررا لوففریل | ودمعتی اندازه.  را ز اسر " ۳و .معتی ىك عدد - وظفر بافتن را نگیفزتهاند  -وصدر ومسند ماش | و بکبار باختن قمار -وبازی سه تیر  -و بمعنی                                       وسلاطین و اکابر باشد  -وقوت |                    ۰   است     هم و           و ده   حرفت |                                                                                  وقدرت و توانابیرا نیز گویند- | بروزن پتا .مخفف وعرخم |             ورء ياك باش
=== leaf 320 printed~ 863
      کک | دست گز اد ہنم کاف فارسی و زای                                     دستگار » باکاف بروزندستبار .همکار- | نقطه دار بالف کشده وبرای بینقطة زده » کنابه                      ند  - ۱و بمعنی ساخته |                                                                                      وهیرا |                                                                                          گرند |                                                                                             و دست کا |               از مددکار وممد ومماون باشد . ۳                            ه |
```


## [2026-09-07T20:52:00.936Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in [310,311]:\n    c=re.sub(r'[‌‎‏‪-‮⁦-⁩]','',t[i])\n    print('=== leaf',i); print(c)\nEOF"
}
```


### [2026-09-07T20:52:02.207Z] TOOL RESULT

```
=== leaf 310
                                              يان هفتم
                در دال بینقطه با زای نقطه دار مشتمل بر ده لغت


                          وزهره وعطارد باشد *.           در = بکر اول و سکون ثالی » قلعه
                                                          بالاخاله را   وبفتح اول کوثشك و        ۳ ۱       وحصارباشد
فلك  ,دمتار را گویند      بروژن    =   درك

دستارچه را    و روپاك است ؛ :و بى         که یل            کربند؛ و با زای ( )۱فارسی هم باين دو معنی
                                                                                                آهوه است (<( ۳
              گفتهاند که دستمال وروياك باشد ۰
                                                          رتا  -بکراول وسکون انی وفتح
                                                                                    داف
درمار = طم اول بروزن گلزار  .دام
                                                           لامحصاری     بالف کشیده ۰   وفای ساکن ۳              همر ه
جابی است کهکان سرب در آیجاست وکان نوعی
 لزاجور دهم متصل بدانهاست وآر الاحجو رددزماری
                                            ا
                                                           وقلعهایست که شاپوربنا کرده بودهاست ؛ وبجای
                                                                          فوقانی نون هم بنظرآمده است #.
                                        . ۵   کو
                                                            ۳دال ایح بروزن بیاره          9 ۳    دردار
و دال أ جد    اول   بكر        در ندیس ۰


بروزن فرنگیس  ۰بممنی همانا و ظاهرا و کوبا                             کوتوال وضابط وحافظ قلمه راکویند .

د بکراول وسکون ثالی               درهر چ                             معاون وباری دهنده وثربك دزد باشد .

وهای مفتوح برای فرشت ) (£وجیم رده » له                     دارورای      طینه
                                                                           قحش
                                                                             نبفل
                                                                                در دافشره = ۴
پیشینیان باشد و آنرا بسربالی ایلیا  ۷خواند                 ومماون     a تحعتی دزد افشار است .که عمق          بیقطه


                                                                                           وشربك دزد باشد .
وسکونهابروزن سپرغم همگفتهاند  -وبتخالهرا
             ای فارسی همست -
                           نیزکرنند ؛ وزبا                 ساراترا کویند که زحل ومشتریومریخ و آفتاب

              ( )۳چك + :وقوفالی -                (() چك - :اک                   ( )۱چك :بزای .
                                                                                  ) (4چك :برا .

  = ڑر .).م.ھ( زد و زد نکمم تسا لکش یبهجپل دشاب یفا تیرکساس _ 4601                                   ١
  ( dêzتوده)   (  ۰آرھثی     نهادن   مدنگ    (انباشتن ٠ روی      اوستا_azeadzu     (سده بارو وحصار) ۰

   = ۴از  :دز (۶م +۳ ).دار (دارنده),                     «هوبشمان  ۰ ۳۹۵۰پپلوی « 2(1)0استق ۳و .
                 رك :افثار و دزد افشره ۰        ۴            .   معربآن نیز «رزدار» دزی جح۱ص ۹۴

   ت   دوم) قلمها   و تشد نف   (یکراول    کے درمار   ۵            افثار .   افثره و دزد    رك:         ۴


  » - ۱مدف وهشاف دڑ                           استوار از تواحی آذرباجان قردىك تبریز «ممجم ال لدان»
              :-ابلا .
                     رك۷                e دزهر ح )(۱     .رك :دزهضت  :دژهخت کنك  ۰دز دوست                   هوخت؟

   »nil « hZud ۰ ۷۲:۷ناوادیا ,dhzud« ۰۱:۲                       #دزد  -بضم ارل» پهاوی 7
  اوتا ( 020۳2بدجنس) ک»ردی ( 21سارق)(81210 .سرفت)» بلوچی< ۰ 2۱أا  .رك
  بقیه درصفبحةٌ۱۵۸:

=== leaf 311
                                                               يان هشتم
                    در دال بینقطه با زای فارسی مشتمل بر سی وهفت لغت


دزاامه ه = بکر اول وفتح آخر                                                   = ۵بکر اول و سکون ثالی » قلمه
 بمعنی دژکام ات که زاهد ویرهیز کار )(٩ -                                    وحصارباشد - ۱وبمعلی زشت و,دوبدخوی وخشم
وخواجهسرا باشد ؛ وبفتحاول لز درست است.                                        نزد-
                                                                                   انی
                                                                                     را
                                                                                       هکی
                                                                                         تند
                                                                                           فبب
                                                                                             گوچ
                                                                                               وقهر نیزهست - ۴
دز ] اه  ۱ت باها بمعنی درآ پاداست
که سهمگن وخشمآ لود باشد  -وبداندش وتند                                                                                   ۰    است   درست   قىر




شده رانیز کرد  -کووتوال و محافظت کنندة                                       و دال         ایجد     با بای        دژ] باد  ۴ت
                                    ذلعه را هم گفتهاند ۰
                                                                             بر وزن اشارات » بمعنی سهمگین و خشم آلود
دز | گه »مخنف دگژاآه است  ۷که
خشمکن وقهرناك و-بداندیش  -وکوئوال قلمه
                                                                                                                                    &

                                                                             درا گام  = ۴با کاف فارسی بر وژن
                                                               باشف          زاهد         و یمعتی         دلارام »خواجه سرا را کت
بععتی      دل»
             لزونک
                 آبرو
                    دز ] لو  ۸ ۵س                                                                           ویرهیز گار همآمده است .

                                                      چش  :برهیز کار .              ()۱               .    -ست
                                                                                                             ( )۱چك :ا

   ۹۳ ۳بابن معنی لفة بضم اولسحیح است»                                      اسلام ۰       و دائرة المعارف        دز    رك:      ۱


     .هلوی . 01511 -هندی باستان_ 5100
                                    دژ= دش » پارسی باستان _ 05لا " اوا  5110 -ب
 دشنام  ۰دشمن ) ودو ا گاه) آمده                  ِ دزخیم a           مر کب بل             ۰در کلمات       020 -       _ ۰ durآرئی 2

 آنجاکه از بدی              آباد " لفة »   ) +        ح ۲       از  :دژ (بضم اول  .رك :                   - ۴                اسشق داه“ .
 دژا کام۰         ۳۳ره :   o               ۰   دژکامه     ۰    درکام   ۰     امه
                                                                                رك :دکژا             ۴                وخشم معمور است .
 )      »مر کب از  :دژ( حرش                «مناس YT                   - ۷پهلوی sãkãhsud                                درکام  ۰درکامه ۰




                     چو بل در آ گاه ودرنده شس.                                              سوار جپان نبوزار دلیر
 دقیقی طوسی« .مزدیبنا 4۵۳-۵۵٩ .
                  دژ ( رکه :ج )  +آلود (لوآده) .                            ز:
                                                                             ۸ا_۵                    :د؟آ گاه ۰        رک       ۷


                                                                                                                بقه اصزفحهٌ ۰۵۸
                  (سارق)  ,بپلوی ن0ز2 = ( 60یا ) .                                    اسشق 41۵؛ دراوراقمانوی بپپلوی 20
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
```


## [2026-09-07T20:52:13.908Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nc=re.sub(r'[‌‎‏‪-‮⁦-⁩]','',t[312])\nprint(c[:3500])\nEOF"
}
```


### [2026-09-07T20:52:15.290Z] TOOL RESULT

```
                                                                                                                        جد
      ح
      ب ۷ی                                                                                                           درا لون



دلنواز» بمعنی زشت خوی  -وبدلما و لا زیبا -                                 ۰   وقهر آ لود باشد       ومهم ناك        خشمگین

                                                                                                                 ~~
وخشم| لود وسهمگین  -وخام طمعوعیب جوی                            در | لون  -بروزن طلا کون  ۰تمعتی
باشد ؛ وبفتح انوفلزدرست است ؛ وبابای فارسی                      حیف ودریغ وافوی باشد ودرمۇ,دالفضلا بهمین
                          هم امده است .
                                                                ممنی بعد از واو الف نوشته بودند که دژالوان
دز براران  -و داژتیرابنابای ابجد                                                                                        باد .
 ۱است که بمعنی              از
                             رجمم
                                بی .
                                   ژارس
                                      دای ف
                                          وب                نظام    فارسیبروزن       ماف   a   ۱    درانگاه


               عیب جوبان ولا.زیبایان وغیره بلشد .          و خشمآ لود          گاهاست که سهمگین               بمعنیدژآ    شاه“



دز برو  = ۴بکراول ۸وسکون انی                                                                                    وقپر ناك باشد


واو ساکن » خشمگین
                وضم الث ورای قرشت و                         بهفتح ها و سکون نون                      هرن|ح؟
                                                                                                       ۰

                                                                                                          د      2   ب




وقپرآلود گوره برایرو زننده راگونند » ویفتح                      وجدم» بدخوی وخشمگین وسپمناك  -وکبرددار
                             اوز  ۸هم درست است .                باشد  -وبمعنیتیر تخش  -وژوبین ( )۱که سنان
دز بسن بتح اول  ۸سین بینفطه
                                                                دهرن|گه  « ۴باکاف فارسی بروزن
                                                                                                                     و
بروزن سربلند  :بمعنیزاهد وپرهیز کارباشد *.
کله بای
      د۰ر 94۳بکر اول  ۸و تا                                 و بد کردار          و معنی دژآهنج است که بخدوی

فارسیباشد وسکون انی وهای حوز( )۲گرهپابی                        -ژویین()۱
                                                                        وخشمناله وسهمگین  -و تیرتخش و
                                                                                               باشد .
رگوابند که در میان گوشت و پوست آدمی
»    وحوانات دیگر میباشد » ومربی غگدودنند                       دز ]هنگ افراسیاب  ۴م غاری
                             وبفتح اول نیز گفتهاند .                   بود که افراسیاب بدانجا کربخته بود .
                                                                                                           ۰         ۳
دز په  ۲بکراول  ۸ثوالك وسکون                                    سفتح بای ابجد بر وزن
                                                                                   در برار ِ ب

                                            :وها .   چك   ()۲                         ) (۱چك  :زوین ۰


    آ هنك («.م)).        از  :دز (رکت :ح۲صقبل)  +آهنج( =             ۳ت          ۰    :دوا کا
```


## [2026-09-07T20:52:38.907Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT dus-pi\"; grep -nE \"du[sš]\\.?pi|duz\\.pi|du§\\.pi\" BRT.txt | head -20; echo \"=== BQT v1 angubin\"; python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\ndef clean(s): return re.sub(r'[‌‎‏‪-‮⁦-⁩]','',s)\nfor i,p in enumerate(t):\n    c=clean(p)\n    if 'انگبین' in c or 'نگبین' in c:\n        print('leaf',i,'printed~',i-212)\nEOF"
}
```


### [2026-09-07T20:52:40.308Z] TOOL RESULT

```
=== BRT dus-pi
=== BQT v1 angubin
```


## [2026-09-07T20:52:46.820Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\ndef clean(s): return re.sub(r'[‌‎‏‪-‮⁦-⁩\\s]','',s)\npats=['گبین','انگب','انکب','نکبین','عسل']\nfor i,p in enumerate(t[:500]):\n    c=clean(p)\n    for w in pats:\n        if w in c:\n            print('leaf',i,'printed~',i-212,w)\n            break\nEOF"
}
```


### [2026-09-07T20:52:48.277Z] TOOL RESULT

```
leaf 89 printed~ -123 عسل
leaf 97 printed~ -115 انگب
leaf 109 printed~ -103 عسل
leaf 260 printed~ 48 عسل
leaf 299 printed~ 87 عسل
leaf 366 printed~ 154 عسل
leaf 384 printed~ 172 انگب
leaf 432 printed~ 220 انکب
leaf 444 printed~ 232 عسل
leaf 461 printed~ 249 عسل
leaf 489 printed~ 277 عسل
```


## [2026-09-07T20:52:52.286Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nc=re.sub(r'[‌‎‏‪-‮⁦-⁩]','',t[384])\nprint(c[:3000])\nEOF"
}
```


### [2026-09-07T20:52:53.534Z] TOOL RESULT

```
انج - بفتح اول وسکون ثانی و جیم»
اطراف 2 روی و رخار ( ۱ ) باشد -
«بمعنی بیرون رفتن وبیرون کشیدنهم آمدماست
- وامر بان معنی هم حست بمنی بیرون بکش .
انحام ۱
و آخر هرکار و هوچیز باشد ه بنظام آیشوهاعل
رانیز گویند کهبنهایت رساننده و با خرآورنده(۲)
و شهات برسان .
اتحباد ه با بای ابجد . ععرب انگبار
نت آی نت یاعد سم نگ وتو
پواسیر دانافم است .
نالك و خای نقطهدار ساکن ۰ بمعنی چین وشکن
ری و اندام و غیره باشد .
) نجحت باجیم فارسی بروزنبدبخت»
انش  باجیم؛ بر وز ند حعنی ب رجستن
باشد .
| نجخیدن « بنثاكبروزنب رگزیدن,
درهم کشیده شدن پوست روی و اندام باشد -
انحشان » منم ناك بروزن مردمان ؛
)۱ ساره
0
اصلآلانجدان خوانند ۴ ؛وبعضی گویند تسنایاست
و آن جانوری باشد. شببه بآدمی .
انجر لك - بکس ثاك وفتح رای فرخت
وسکون کاف » نام دشتیو صحرادیست غیرمعلوم-
و مرزنگوش را نیز گوبند و آن نومی آزرباحین
است که در دوا ها بکاد برند و درعریی ! ذانالفار
کویند ۴ .
اتجره - بروزن پنجره ؛ نباتی است که
آنرا بعربی بنات النار گویند بقتح بای ابجد ؛ و
نخم آن را قرضخوانند وتخم آن مستعملاست.
سهدرم آنرا با شیر نازه بشورند قوت باه دهد
و بکوبند وبا عصل برقضیب مالند سطب کرداند .
)نج ۴ - بنتح اول و سکون ثٌانی
وکسر جیم و سین بینقطة بالف کشده ؛ بمعنئی
ابوخلسا ۴ است که نوعی ازسرخ مردیاشد و آنرا
عربی شجرءالدم گویند , خون شکم را ببندد .
انح - با خن نقطهدار » بروزن و ععنی
انجخ ۱ سا که جچن و شکنج روی واندام عاشد .
انحکك - باکاف مروزنمردمك ءدانهای
باشد سیله شبیه یداه امرود و مفز فد دارد
وآنرا بخورند . خاصتشآاست که هرچند فراش
خبال جاروب سنبل ی تا
بوست آن باه نون
۴ - ۹6۱66۱ «لك۱ سی۱۹۷*.
انحرك « لك ۱ مس ۱۱۲ > .
۶ ملای ۲:۲۷ *.
است توجهی نکر دها ند)
```


## [2026-09-07T20:53:03.580Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\ndef clean(s): return re.sub(r'[^؀-ۿ]','',s)\nfor i in range(380,400):\n    c=clean(t[i])\n    hits=[w for w in ['انگبین','گبین','انگبن','انکبین','عسل','انگ'] if w in c]\n    print(i, i-212, hits, c[:60])\nEOF"
}
```


### [2026-09-07T20:53:04.860Z] TOOL RESULT

```
380 168 ['انگ'] کهزربائد۷امیصادقبنماولاشاره۱بهحضرترسالتناهصلواتالهعلیهباشدام
381 169 [] یوتانی۱وممنیآنبفارسیسنگهزاییدنآمانکنباشدوآندانهایستساهرنگهبم
382 170 ['انگ'] اتبارشکهپرکردهباشدوبمعنیپرنسمتوبانعستهماجهات۵نبادشبروزنافزای
383 171 [] سبی٩بودنبروزنافزودنبربالایحمچیدنباشداثبوذنسبازالقطهداربروزنا
384 172 ['انگ'] انجبفتحاولوسکونثانیوجیماطرافرویورخار۱باشدبمعنیبیرونرفتنوبیرو
385 173 [] بوفحلسبفتماولوکسرثالثوسکوننانیولامرسثنیباشدکهآیراخطمیخوانند۳
386 174 ['انگ'] انجینازتوابمبزدوناوچهٌمقمدوسوراخکونرانیزگویند٩نجین۲بروزندنگی
387 175 [] ۱۹۹ادبروزنپرواژ؛ممنیشسدومیلنمودنوحملهکردنباشدوامرباينمعنیهمه
388 176 [] اندرخوراندزخودربنمخاینفطهداروسکونواوممدولهورایمینقعلهممحنیاج
389 177 [] افاورفتیبکشببایشدوآتشرابکشتراندرویدرمیاندرباکمکردیدسینمینقطه
390 178 [] انسجانکهکرفتگیدلودلگیریباشداندهانبروزنمردمان؛جمماندهباشدچنان
391 179 ['انگ'] رنارهباازایفارسیبروزنغمزه؛مرجماثباشدوآثراببربیعدیگویندانستهب
392 180 ['انگ'] اگاردهاستکهافسانهوسرگذشتباشدانگاده۱هبروزنعموارءهرچیزکهافانهو
393 181 ['انگ'] مردمفررنگمهست٩۰الثوزایقطهدارساکنسلیباشدکهبآنزمنراهموارسازند۹
394 182 ['انگ'] انگشتبحرفنهادنکنابهازعیبکرفتنودکتهگیریکردنباشدنگشتبردهانگداش
395 183 ['انگ'] یافچنکالیومالیده۳وانیشکیباروغنوشیرینیبهمبمالندانگشتو۰بکسالكو
396 184 ['انگ'] انگوززیتونیوبعربیاصابعالمذاریگوبندنگوژه؟بازایفارسیبروزنسنبوص
397 185 [] نوهیانبکرمبروزنمجوسیانلالهباشدودرصحاحالادوبهبهمینححنیباسقاطن
398 186 [] کوبندکهبدشواریازاناشودوحلثیشهبررزنهمینهجاسویوچاپلویهرچیزبسته
399 187 ['انگ'] رلاسیفکنوبشماولنالهوزاربراگوینداوباریدن۱بنتحاولبروزنسرخاریدن
```


## [2026-09-07T20:53:16.886Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in [392,393]:\n    c=re.sub(r'[‌‎‏‪-‮⁦-⁩]','',t[i])\n    print('==== leaf',i); print(c[:2600])\nEOF"
}
```


### [2026-09-07T20:53:18.477Z] TOOL RESULT

```
==== leaf 392
اگارده است که افسانه و سر گذشت باشد .
انگاده ۱ ه بروزن عموارء ."هر چیز
"که افانه وس گذشت داشد - وباد گذشتها کردن
رانیز کوبند - و ازسر گرفتن سر گذشت وافانه
را عم گفته اند بطریق کنابه چنانکه ا گر کسی
بسیارومکرراز گذشته بگوید گویشدهانگارهمیکند»
یعنی باز از سر هیگیرد - و پس پی خزنده از
شرم و حیا را نیز کوبند - وبمعتي دفتر وحساب
و نامه اعمال هم نوشتهاند .
انگادیدن ۱ » بر وزن ترسانیدن »
بمعنی هو رکردن وینداشتن  و گمان بودنباشد .
اناد » با زایهوزبروزن پرواز .افزار
آن اووات است .
انگاشتی ۱ -بر وزن برداشتن. بمعنی
صور کردن و نداشتن و کمان بردن باشه. .-
انگام ۴ » بروزن و معنیهتگام است
که موسم و وفت باشد .
انگاهه ۲ - بر وزن و معنی هنکامه
۱ راد : انگاردن ۰
۳ ت ازمادهٌ اذیدمن» رژد انجمن.
ات
است که مجمع و انجمن بازیگران و قصهخوانان
ا لگیین ۴ - با بایابجد بروزنعنبرین,
سل و شهد را گوبند .
انگیینه - بروزن شنبلیله , نام حلوامی
است و ان قلن باشد که نيك بقوام آوردهباشند
و برطبقی ریزند تا سختشود و دندان کیر گردد .
انگدان ه بنم نالك ودال بالف کشیده
بروزن مردمان , شنای را گوبند یمنی دمومردم؛
و آن جانوری باشد وحشی شبیه بادمی ؛ و در
جاوتری میگوبند واه اعلم - و نام درختی حم
نقطهدار هم آمذه است - و نام قربهاستازفرای
کاشان که بانگوان اشتهار دارد.
انگرده ۳ بشم ثالث بروزنافرده. دانةً
انگور که از خوشه جدا شده باشد . ۱
افگر یز - بکوننالت بروزندنگریز,
رستنی باشد و گلآن مانندگل خسك زرد.متود
و اطراف آن خار دارد و انرا بعربی قرطم بری
خوانند » و بیونانی طریفان کویند - و نوعی از
شه ازصفحهٌ ۱۷۳
يب ۲۳۵ ۰ رك : انگزد .
« نیب گی۰۹٩ >.
==== leaf 393
مردم فررنگ «م هست ٩ ۰
الث و زای قطهدار ساکن » سلی باشد که بآن
زمن را هموار ساز ند ۹
انگز ح بفت اول و خم نالث: و کت
تابی و زای فارسی» آهنی باشد سر کج که فیلرا
بدان بهرطرف که خواهند بيند .
انگژ د ۴ ختح اول دضم ثالثوسکون
انی و فتح زای فارسی ودال ابجد -اکن مطلق
صعفها را گویندعموعاً و صمفی باشد بغایتبدبوی
و آترا پعربی حلتیت خوانندو آنرا انگژدیسب
آن گون که سمغ درحت انگدان است و ال
آن انگدان ژد باشد بفتح زای فارسی چه ژد
بلفت فرس بمعنی صمغ است و آن گرم و خشكت
است در درجه سیم .
انگز لك . بازای هوز بروزن مرجمك ,
کجك فل را گونند و آن آلی باشد سر کج از
آهن که فیلبانان فیل رابدان بپرطرف کهخواهند
برند . و بازای فارسی هم بنظر آهده است :
اآلگژ واه بکس نات و سکون زای
فارسی و واو بالف کشپدهبروزن »نزلها. جابیرا
کودت که شنها گوتفندان زا چر ادا تک
دارند - و کوسفندانرا نیز گفتهاند - ویمعنیدانه
و ختَهةٌ میوه ها هم آهده است .
انگشت برچشم نفادن
۱ نگژه  ح با زای فارسی مفتوحبروزن
خربزه , مخفف انگوژه است که صمغ درخت
انکدان باشد و آلرا عربان حلنیت و شیرازبان
انگثت گنده ( ۱ ) کوند. و با زای هوز نیز
ال اسگ:
ا نگسبه بفتح اول والت و سکونانی
و سین بی قطه و فتح بای ابجد » برزیگربرا
گویند که صاحب سامان بود وکار کنان وزراعت
کاران ببار داشته باشد .
انگشبه - با شین نقطه دار . بر وزن
و معنی انکته کت که مرن وا اسان
باشد - و سودا کر صاحب مابه را نیز گفهاند.
انگشت؟ - بنم اك , ممروضت که
عربك از انگشتان دست و بای باشد - و بکس
ثالت زغال را گوند که اخگر کشنه شده است.
انگشتال * ه یکی تاك , فوفانی بالف
کشبده و لام سکن , مردمشمیف و نحیف وعلیل
ویارنا وصاحب تقاهت راگونند .<
انگشت بد ندان گز بدن - کناه
ازنهجب کردن و نحیر نمودن باشد - و حسرت
و اقوی خوردن را نیز گوبند .
انگشت بر چشم نهادن د کاب
ازقبول کردن ومسلمداشتن باشد, وانگثث بر دیده
۳ ۳۳ رلك؛ انگود.
```


## [2026-09-07T20:53:36.558Z] TOOL CALL #68: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:174 --image 2>&1 | tail -30"
}
```


### [2026-09-07T20:53:38.008Z] TOOL RESULT

```
no scan of BQT covers printed page 174 (see 'scans' in refs_online.json)
```


## [2026-09-07T20:53:45.574Z] TOOL CALL #69: Bash

```json
{
 "command": "for u in \\\n \"https://abadis.ir/fatofa/%D9%BE%D9%86%DA%A9%D9%87/\" \\\n \"https://abadis.ir/fatofa/%D9%BE%DB%8C%D9%86%D9%88/\" \\\n \"https://abadis.ir/fatofa/%D8%AF%DA%98%D9%BE%DB%8C%D9%87/\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%86%DA%A9%D9%87\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 385: Mo'in / Dehkhoda entries for pankeh, pinu, dozpih\" ; done"
}
```


### [2026-09-07T20:53:51.026Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b0d81eb569ab69bc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b1297a3c0711fce0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d91e456c1fdb8f01.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6bb909788d234e72.txt
```


## [2026-09-07T20:53:54.489Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in b0d81eb569ab69bc b1297a3c0711fce0 d91e456c1fdb8f01; do echo \"######## $f\"; grep -n -A6 \"معین\\|فرهنگ فارسی\" $f.txt | head -40; done"
}
```


### [2026-09-07T20:53:55.841Z] TOOL RESULT

```
######## b0d81eb569ab69bc
22: فرهنگ فارسی
23-
24- بادزن برقی، ماخو ازهندی
25-( اسم ) بادبزن برقی . 
26-
27: فرهنگ معین
28-
29- (پَ کِ ) [ هند. ] (اِ. ) بادبزن برقی . 
30-
31- فرهنگ عمید
32-
33- بادزن برقی. 
--
45: پَنکه ( به هندی: पंखा ) یک فن مکانیکی است ( فرهنگ معین؛ بادبزن برقی ) که برای خنک کردن در خانه ها و ساختمان ها فراوان مورد استفاده است. پنکه دارای پره های اریب است که با چرخیدن خود باعث جابجایی و خنکی هوا می شود گرچه محصول جدیدتر و مشابهی به نام پنکه بی پره وجود دارد که فاقد پره است. 
46-پنکه های خانگی در چهار مدل رومیزی، ایستاده، سقفی یا دیواری ساخته می شوند. یکی از کاربردها پنکه در محیط هایی است که به دلیل بالا بودن درصد رطوبت هوا امکان استفاده از کولر آبی وجود ندارد. [ ۱] 
47-ریشه واژه پنکه از زبان سانسکریت آمده و به معنای بال پرنده است. [ ۲] [ ۲] ( هندی: पङ्खा, pangkhā ) پنکه های اولیه به صورت صفحه های تخت آویزان از سقف بوده که بوسیله یک بند جهت جابجایی هوا به صورت دستی تکان داده می شده
48-از فن پانکا حدود ۵۰۰ سال قبل از میلاد در هند استفاده می شد. این یک فن دستی بود که از نوارهای بامبو یا الیاف گیاهی دیگر ساخته شده بود که می توانست برای حرکت دادن هوا چرخش یا فن داشته باشد. در زمان حکومت انگلیس، این کلمه توسط انگلیسی - هندی به معنای یک فن تخت بزرگ تاب دار استفاده می شود، که در سقف ثابت می شود و توسط بنده ای بنام پانکاواله کشیده می شود. 
49-برای اهداف تهویه مطبوع، صنعتگر و مهندس سلسله هان، دینگ هوان یک فن دوار دستی با هفت چرخ اختراع کرد که قطر آن ۳ متر ( ۱۰ فوت ) بود. در قرن ۸، در زمان سلسله تانگ ( ۶۱۸–۹۰۷ ) ، چینی ها از نیروی هیدرولیکی برای چرخاندن چرخ های فن برای تهویه مطبوع استفاده می کردند، در حالی که فن دوار در طول سلسله سونگ ( ۹۶۰–۱۲۷۹ ) حتی بیشتر متداول شد. 
50-در قرن هفدهم، آزمایش ها دانشمندانی از جمله اتو فون گوریکه، رابرت هوک و رابرت بویل، اصول اساسی خلأ و جریان هوا را ایجاد کرد. معمار انگلیسی سر کریستوفر رن از سیستم تهویه اولیه در خانه های پارلمان استفاده کرد که از دمنده برای گردش هوا استفاده می کرد. طراحی رن می تواند کاتالیزوری برای پیشرفت و نوآوری های بعدی باشد. همان طور که توسط گئورگ آگریکولا ( ۱۴۵۵–۱۵۵۵ ) نشان داده شده است، اولین فن چرخشی استفاده شده در اروپا برای تهویه مین بوده است. 
51-John Theosophist Desalinizes، مهندس انگلیسی، استفاده موفقیت آمیز از سیستم فن را برای بیرون آوردن هوای راکد از معادن زغال سنگ در سال ۱۷۲۷ نشان داد و بلافاصله پس از آن دستگاه مشابهی را در پارلمان نصب کرد. تهویه مناسب به ویژه در معادن زغال سنگ مهم بود تا تلفات ناشی از خفگی را کاهش دهد. مهندس عمران جان اسماتون و بعداً جان بودل پمپ های هوای متقابل را در معادن شمال انگلیس نصب کردند. با این وجود، این آرایش ایدئال نبوده زیرا ماشین آلات ممکن است خراب شوند. 
--
73:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
74-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
75-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
76-
77- اسپنک و پنکه ؛ 
78- این کلیدواژه از ارگانیک وجود انسان عینیت یافته است. و ریشه ی اصلی این کلمه پنک یا پنگ یا پنج منشعب از پهنای کف دست به همراه پنج تا انگشت می باشد یعنی با ریخت پهنگه و پهنجه و پنجه که در زبان های مختلف، کلمات دچار تغییرات آوایی و نگارشی می شود. عینیت ایجاد عدد پنج در عالم واقع نیز بر مبنای پهنای کف دست به همراه تعداد انگشتانی که وصل به کف دست است می باشد. 
79- ... [مشاهده متن کامل] 
--
128: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
129-
130- لینک ها 
131-
132- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
133-
134- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
######## b1297a3c0711fce0
40: فرهنگ فارسی
41-
42- پینوک، کشک ، قروت، ترف
43-( اسم ) دوغ ترش که خشک کرده باشند کشک قورت ترف : نیکی بگزین و بد بنادان ده . روغن بخر و جدا کن از پینو . ( ناصرخسرو )
44-ماستینه دوغ ترش بود که خشک کرده باشند یعنی کشک 
45-
46: فرهنگ معین
47-
48- (پِ ) (اِ. ) کشک ، قره قروت . 
49-
50- فرهنگ عمید
51-
52- کشک، قروت، ترف: شعر ژاژ از دهان من شکر است / شعر نیک از دهان تو پینو (طیان: شاعران بی دیوان: ۳۱۹ ). 
--
74: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
75-
76- لینک ها 
77-
78- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
79-
80- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
######## d91e456c1fdb8f01
20: فرهنگ فارسی
21-
22- ( اسم ) غدهای بزرگ زیر پوست یا ضمن مخاطهای بدن بر آید . دشپل دشپیل . 
23-
24: فرهنگ معین
25-
26- ( ~. یِ ) (اِمر. ) غده های زیرپوستی . 
27-
28- فرهنگ عمید
29-
30- غدۀ سفت و سختی که زیر پوست بدن پیدا شود، دشپل، دشپیل. 
--
50: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
51-
52- لینک ها 
53-
54- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
55-
56- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است.
```


## [2026-09-07T20:54:30.932Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN CHEESE\"; grep -n \"CHEESE\" SYN.txt | head; echo \"=== SYN FAT\"; grep -n \"^5.6\\| FAT \" SYN.txt | head; echo \"=== LEW pectus\"; grep -n \"pectus\" LEW_1910.txt | head -5; echo \"=== IEC pitu\"; grep -n \"^pitus\\|^pītus\\|^peiə\\|^pī-, poi-\\|^poimen\\|^pinos \\|^pīwos\" IEC.txt | head"
}
```


### [2026-09-07T20:54:31.036Z] TOOL RESULT

```
=== SYN CHEESE
8314:CHAPTER 5 FOOD AND DRINK; COOKING AND UTENSILS 5.11 Eat 5.57 Minn 5.12 Foop 5.61 Mezar 5.13 Drink (vb.) 5.612 Burcurr 5.14 Hunexr (sb.) 5.62 Brrr 5.15 Turrsrt (sb.) 5.63 Sausace 5.16 Suck (vb.) 5.64 Sour, Brots 5.17 Mrx 5.65 VEGETABLES ' 5.21 Cook (vb.) 5.66 Bran ? 5.22 Bor 5.67 Pra 5.23 Roast, Fry 5.68 Onion 5.24 Baxe 5.69 CaBBAGE 5.25 Oven 5.70 Porato 5.26 Por 5.71 Fruir 5.27 Kerrin 5.72 APPLE 5.28 Pan 5.73 PEAR 5.31 Disx 5.74 Pracu 5.32 Prats 5.75 Wie : 5.33 Bown 5.76 Grape 5.34 Pircuer, Jue 5.77 Nur 5.35 Cup 5.78 OLIvE 5.36 Saucer 5.79 Om 5.37 Spoon 5.80 Berry 5.38 Kyire 5.81 Saur 5.39 Fork 5.82 Prpprr 5.41 A Mua, 5.83 VINEGAR 5.42 BReakFast Bi Rdeer ona 5.43 Luncx 585 § 544 Dinner een Base Sucnbn. 5.86 Mixx (sb.) 5.51 Breap 5.87 Minx (vb.) 5.52 Caxn 5.88 CHEESE 5.58 Dover 5.89 Burrer 5.54 Kwrap 5.91 Merap 5.55 Mzau, Frour 5.92 Wine 5.56 Grinp 5.93 Brrr
9704:5.83 CHEESE
=== SYN FAT
47:50649 CARL DARLING BUCK
232:536 661 739 829 916 953 1017
6814:566. - ce Ir. saile, N saliva ‘spittle’. denom. NIr. sez guage vb. ‘spit’ ren
9239:5.612 BUTCHER
9293:5.68 SAUSAGE
9328:5.64 SOUP, BROTH
9352:5.65 VEGETABLES ; Goth. gras Lith. darZovés
9382:5.66 BEAN Grk. —_xbayos, paondos Goth. Lith. pupa NG kouxxl, dacobAr ON baun Lett. pupa Lat. faba, phasélus Dan. bdénne ChSl. bobit It. fava, fagiuolo Sw. béna SCr. — grah, bob, pasulj Fr. Seve, haricot OE béan Boh. _ bob, fazol Sp. haba, frijol, judia ME bene Pol, b6b, fasola Rum. fasole NE bean Russ. bob, fasol’ Ir. seib Du. boon Skt.  mdgsa- Nir. ponaire (pl.) OHG bona Av. ets lave W. Sden MHG bone, fasal Br. JSavenn NHG _bohne, fasole
9418:5.68 ONION
9436:5.69 CABBAGE
=== LEW pectus
=== IEC pitu
```


## [2026-09-07T20:54:38.375Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9704,9730p' SYN.txt; echo \"=== IEC\"; grep -n \"pitus\\|pīwō\\|poimen\\|pīnos\\|peiə\\|pīwos\" IEC.txt | head -10"
}
```


### [2026-09-07T20:54:38.442Z] TOOL RESULT

```
5.83 CHEESE
Lith.  sdris, kiezas
Goth. .--- u Lett. szers ostr % a Den. a ae caseus . Sw. ost z B ‘i td. , 1 maggias caer? OE _ ciese, cése oh.  syr (tvaroh) henge ME chese Pol. ser (twarég) ie NE cheese Russ. syr (trorog) FG  brinzd Du. ‘aas Skt.  (dadhi-ja-, ksira-ja-) * aise OHG chast Av. fsula- (tiiri-) It ogise MHG kese alos NHG kaise
ca : fourma)
- ripss, dim. riplov, NG 7vpl, i oe le that has become like 1 prob. ; Lat. ob-tdrare, re-turare cheesey Ff, fll up’, turunda ‘pellet for ee ley a Skt. iura- ‘abundant, tae ete., all fr. the root Beet in Gric. ry ‘swelling’, Lat. tumére “be srollen., ee, Here also possibly the mugh :dis- puted Boh. waroh, Pol. twardg, Russ. irorog ‘curds’ or soft ‘cheese’, whence MHG tware, quare, NHG quark ‘curds’. Walde-P, 1.710f. (with refs. to other views), 2. Lat. cadseus : ChSl. kvast ‘leaven’, Skt. kuath- ‘seethe, boil’, Goth. hwapjan ‘foam’, ete. Hence It. cacio, Sp. queso, Rum. cas (‘fresh sheep’s milk cheese’); It, edise, W. caws; OF ciese, cése, ME chese, NEE cheese, Du. kaas, OHG chasi, MHG hese, NHG hase (> Lith. kieZas). ies 1468. Walde-H. 1.176 f. a Pedersen 1.49, 202. ngs eae Br. fourmaj), It. for- fi on i at. formaticum, deriv. of a ‘shape, form, mold’ (cf,
MlLat. casei forma, and Prov. furmo ‘cheese’). REW 3441.
Rum. brinzd (cf. It. brinze, NHG local (Austrian) primsenkdse, for which see Kretschmer, Wortgeogr. 564), orig. dub. REW 1272.
3. ON ostr, Dan., Sw. ost : Grk. fwpés, Lat. itis, Skt. yiisa-, etc., ‘soup’ (5.64), Grk. ¢bun ‘leaven’. Walde-P. 1.199. Falk-Torp 803.
4. Lith. saris, Lett. siers (te instead of u by association with siet ‘bind’ in sieru siet ‘make cheese’), ChSl. syri, etc., general Slavic : ChSl. syrt% ‘moist’, SCr. sirov ‘raw, fresh’, Lith. suras ‘salted’, ON starr, OHG, OE sar ‘sour’, etc. Walde- P. 2.5138. Trautmann 293f. Miihl.- Endz. 3.859.
5. Skt. dadhi-ja-, kstra-ja-, lit. ‘milk- born’, cpds. of dadhi- or kstra- ‘milk’ (5.86) are used for ‘curds’, whether formed ‘cheese’ is not clear.
Ay. fsuta-, fr. fsu-‘fatten’? Barth. 1029.
Av. tiiri- above, 1.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
388 SELECTED INDO-EUROPEAN SYNONYMS
5.89 BUTTER Grk. — Bobripov (late) Goth. Lith.  sviestas NG — Bobrupov ON — smjor Lett.  sviests Lat. bityrum (late) Dan. smé¢r ChSl. a It. burro Sw. smér SCr. maslac Fr. beurre OE butere Boh.  mdslo Sp. manicca ME _butere Pol. —masto Rum. unt NE butler Russ. maslo Ir. amb Du. _boter Skt. ghrta-, navanita- NIr. im OHG = ancho, bulera Av. (raoyna-) W. ymenyn MHG buter, anke Br. amann NHG butter
Butter was a common article of food from early times in India and Iran (‘melted butter’) and in northern Eu- rope, but not among the ancient Greeks and Romans, who first heard of it as a Scythian product. It is first reported by Herodotus (4.2), who describes the proc- ess of churning, later by Hippocrates (4.20), who first introduces the word Bobrupov. Pliny (28.183) tells of buty- rum, barbararum gentium lautissimus cibus. Schrader, Reallex 1.175 ff.
1. Grk. Botripor, lit. ‘cow-cheese’, but either a translation or an adaptation of a native Scythian word (tov, 8 Bobrupoy kaAéovat, Hipp. 4.20). Hence Lat. bity- rum, and fr. this OFr. burre (> It. burro), Fr. beurre, OE, ME butere, NE buiter, Du. boter, OHG (late) butera, MHG buter, NHG butter.
2. Sp. manteca (also ‘fat, lard’), prob. of pre-Roman orig. REW 5324a,
Rum. unt (also ‘oil’) : It. unto, OF. oint ‘fat’, fr. Lat. dnctum ‘ointment’, pple. of unguere ‘smear, anoint’. REW 9057.
3. Ir. umb, imm, NIr. im, W. ymenyn, Br. amann, OHG ancho, MHG anke, OPruss. anctan : Lat. unguen ‘fat, oint-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
ment’, unguere ‘smear, anoint’, Skt, aij. ‘anoint, adorn’. Walde-P. 1.181. Peder- sen 1.46.
4. ON smjor, Dan. smgr, Sw, Smér, OHG chuo-smero (lit. ‘cow-grease’) : Goth. smairpr ‘fat’, OF smeoru, OHG smero ‘fat, grease’ (NI smear), Ir. smir ‘marrow’, ete. Walde-P. 2.690f. Falk- Torp 1086 f.
5. Lith. sviestas, Lett. sviests, perh. : Av. xsvid- ‘milk’. Walde-P. 2.521.
SCr. maslac (beside maslo ‘grease’), Boh. mdslo, Pol. masto, Russ. maslo (‘butter’ and ‘oil’) : ChSI. maslo ‘oint- ment, oil’, mazati ‘anoint’, Grk. pacow ‘knead’, etc. Walde-P. 2.226. Berneker 2.23, 28.
6. Skt. ghrta- ‘clarified butter, ghee’ : Skt. ghr- ‘besprinkle’, further connec- tions dub. Uhlenbeck 85, 100. Walde- P. 1.407.
=== IEC
12944:pit- (pit-) (1) “food? Skt. pituh, m. 1d.; Av. pitus, m. id.; Oss. fid, Iron. fid, s. *meat' cf. also fidar, adj. ‘strong’; OIr. & mod. ithe, f. “food, eating’ beside Olr. íth, s. (fat; mod. ith, ioth, f. ‘coro’; W yd, m. ‘corn’; OBr. it-, id.; Br. éd, id, m. ‘cereal’; OCS pista, f. “food”, Cz. píce, f. ‘fodder’; Li. pitas, m. ‘food’; Latv. pitas, fpl. *pease-pud- ding” beside pite, f. id. (and 'dumpling); ON cf. (?) fita, f. ‘fat. Cf. Ir. ithir, f. ‘cornfield’
12946:pit- (pitus, piteu-) (3) ‘pine’. Pamiri (alleged) pit, id.; Gk. pítus, f. id.; OCorn. iteu, Cor. etew, pl. -i, m. “firelog'; LG (?) fid, n. wooden splice-pin'. (ISophones: Skt. pituh m. ‘drier — epithet of sun’; Kurd. pitew, adj. “hard, solid"). Cf. Skt. pitu-daru, n. "Dr See pit- (2)
13311:poimóo(n), poimen- ‘herdsman’. WP II, 72 Myc. & Gk. poimén, gs: -enos, m. (and “guard, ruler); Li. piemuó, gs. -efis, m. id.; (LW in) Finn. paimen, id.; cf. also OE fæmne, wf. *gir; (?) ON. feima ‘shy girl’; Li. pieméne, f. 'shepherdess, cowgirl
17361:strebhó. (Gmc. ambig.) Lat. streng, ére, v. “bustle; murmur; MHG (ambig.) strében, wv. ‘throng; stiffen; stir; struggle’; Du. streven, v. ‘strive’ beside strib- belen, v. ‘bicker’; OCz. střepěti, inf. ‘strive’; Li. cf. strepinēti, inf. ‘rampage; fidget’; stre- peciuoti, inf. “hop around”; strepëtas, m. “les- ser bustard" (NB. E to strive derives from OFT. estriver despite vowel alternation in strove, striven. A reconstruction of type *srep- to in- clude Greek rhépo ‘tend, incline, prevail’ is possible for Gmc. but excludes Lat. on se- mantic grounds. For OFr. estrif, cf. strepor, estrit, cf. strepitus, and estriver, fr. Lat. *stre- pāre, w. vocalism of prix, six, mi, pire, sire from Lat. -e-)
```


## [2026-09-07T20:55:13.921Z] TOOL CALL #73: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-07T20:55:13.962Z] TOOL RESULT

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


## [2026-09-07T20:55:20.328Z] TOOL CALL #74: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg385.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/385.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/385.png"
}
```


### [2026-09-07T20:55:20.487Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 61185 Sep  7 16:55 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/385.png
```


## [2026-09-07T20:55:37.021Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 719d10c4845aca28 1ea1261a4b155047 2ca1ea8f1b569a6f 6bb909788d234e72; do echo \"######## $f\"; sed -n '/^ From Wiktionary/,$p' $f.txt | head -35; done; echo \"###### fat\"; sed -n '/^ From Wiktionary/,$p' 6c5cb6d0f5cc67b0.txt | grep -n -A12 \"Etymology 1\" | head -30"
}
```


### [2026-09-07T20:55:38.383Z] TOOL RESULT

```
######## 719d10c4845aca28
 From Wiktionary, the free dictionary

 See also: पंख , पंखे , and पंखो 

 Hindi
 [ edit ] 

 Etymology
 [ edit ] 

 Inherited from Sauraseni Prakrit 𑀧𑀓𑁆𑀔 ( pakkha ) , from Sanskrit पक्ष ( pakṣa , “ wing ” ) . Cognate with Gujarati પંખો ( paṅkho ) , Marathi पंखा ( paṅkhā ) .

 Pronunciation
 [ edit ] 

 ( Standard Hindi ) IPA ( key ) : /pəŋ.kʰɑː/ , [pɐ̃ŋ.kʰäː] 

 Noun
 [ edit ] 

 पंखा • ( paṅkhā )  m ( Urdu spelling پَن٘کھا ) 

 fan 
 पुराना पंखा काम नहीं करता। purānā paṅkhā kām nahī̃ kartā. The old fan doesn't work. 

 ventilator 

 Declension
 [ edit ] 

 Declension of पंखा (masc ā-stem) 

 singular

 plural
######## 1ea1261a4b155047
######## 2ca1ea8f1b569a6f
 From Wiktionary, the free dictionary

 This Proto-Indo-Iranian entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-Iranian
 [ edit ] 

 Etymology
 [ edit ] 

 From Proto-Indo-European *péyh₂-os ~ péyh₂-es-os ( “ fat, milk ” ) .

 Noun
 [ edit ] 

 *páyHas   n 

 milk 
 Synonym: *kšiHrám 

 Inflection
 [ edit ] 

 neuter as-stem

 singular

 dual

 plural

 nominative

 *páyHas

######## 6bb909788d234e72
 From Wiktionary, the free dictionary

 See also: تنگه and پنکھ 

 Iraqi Arabic
 [ edit ] 

 Noun
 [ edit ] 

 پنکه ( panka )  f 

 alternative form of بنكة ( banka ) 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from Hindi पंखा ( paṅkhā ) , ultimately from Sanskrit पक्ष ( pakṣá ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /pan.ˈka/ 

 ( Dari, formal ) IPA ( key ) : [pʰäŋ.kʰá] 

 ( Dari, formal ) IPA ( key ) : [pʰäŋ.kʰá] 
 ( Kabuli ) IPA ( key ) : [pʰäŋ.kʰá] 

 ( Hazaragi ) IPA ( key ) : [pʰäŋ.kʰá] 

 ( Iran, formal ) IPA ( key ) : [pʰæɲ.kʰʲé] 
###### fat
47: Etymology 1
48- [ edit ] 
49-
50- A fat cat 
51- From Middle English fat , from Old English fǣtt ( “ fatted, fat ” ) , from Proto-West Germanic *faitid ( “ fatted ” ) , originally the past participle of the verb *faitijan ( “ to make fat ” ) , from *fait ( “ fat ” ) .
52-
53- Adjective
54- [ edit ] 
55-
56- fat ( comparative fatter , superlative fattest ) 
57-
58- ( sometimes derogatory ) Carrying more fat than usual on one's body; plump ; not lean or thin .
59- The fat man had problems going through the door. 
--
1475: Etymology 1
1476- [ edit ] 
1477-
1478- From Latin fātum .
1479-
1480- Noun
1481- [ edit ] 
1482-
1483- fat   m ( uncountable ) 
1484-
1485- fate , destiny 
1486-
1487- Related terms
--
1685: Etymology 1
1686- [ edit ]
```


## [2026-09-07T21:03:43.712Z] TOOL CALL #76: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk385.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\n\nW = \"https://en.wiktionary.org/wiki/\"\nS = {\n \"peyh2\": W+\"Reconstruction:Proto-Indo-European/peyH-\",\n \"pectus\": W+\"pectus\",\n \"punkah\": W+\"punkah\",\n \"pih\":    W+\"%D9%BE%DB%8C%D9%87\",\n \"farbeh\": W+\"%D9%81%D8%B1%D8%A8%D9%87\",\n \"panir\":  W+\"%D9%BE%D9%86%DB%8C%D8%B1\",\n \"angabin\":W+\"%D8%A7%D9%86%DA%AF%D8%A8%DB%8C%D9%86\",\n \"pinus\":  W+\"pinus\",\n \"paksa\":  W+\"%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7\",\n \"pankha\": W+\"%E0%A4%AA%E0%A4%82%E0%A4%96%E0%A4%BE\",\n \"pankeh\": W+\"%D9%BE%D9%86%DA%A9%D9%87\",\n \"payHas\": W+\"Reconstruction:Proto-Indo-Iranian/p%C3%A1yHas\",\n \"fat\":    W+\"fat\",\n \"ab_pankeh\": \"https://abadis.ir/fatofa/%D9%BE%D9%86%DA%A9%D9%87/\",\n \"ab_pinu\":   \"https://abadis.ir/fatofa/%D9%BE%DB%8C%D9%86%D9%88/\",\n \"ab_dozpih\": \"https://abadis.ir/fatofa/%D8%AF%DA%98%D9%BE%DB%8C%D9%87/\",\n}\n\ndoc = {\n  \"pdf_page\": 385,\n  \"book_page\": 355,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n   {\n    \"entry\": 0,\n    \"root\": \"Peg\",\n    \"verdict\": \"plausible\",\n    \"modern_form\": \"PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'\",\n    \"note\": (\"Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, \"\n             \"Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. \"\n             \"Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, \"\n             \"which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A \"\n             \"pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. \"\n             \"Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong \"\n             \"together at all. Root is real and the language label is right; the gloss is a one-sided simplification.\"),\n    \"note_fa\": (\"ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ \"\n                \"«(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و \"\n                \"درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا \"\n                \"«Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و \"\n                \"paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در \"\n                \"پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ریشه واقعی است و برچسب زبانی درست، اما معنای داده‌شده \"\n                \"یک‌سویه و ساده‌سازانه است — ادعای نورایی با احتیاط پذیرفتنی است.\"),\n    \"sources\": [S[\"paksa\"], S[\"pectus\"]],\n    \"ref_check\": [\n      {\"ref\": \"POK:792\", \"status\": \"partial\",\n       \"note\": (\"Pokorny IEW p.792 (local POK_03.txt, form-feed leaf 25) reads: '(peg-:) pog-: pōg-, pŏk-s- \"\n                \"\\\"Achsel, Hufte, Lende, Seite\\\". Ai. pákṣa- m. \\\"Schulter, Flugel\\\" und \\\"Seitenpfosten\\\", pákṣas- n. \"\n                \"\\\"Seite\\\"; lat. pectus \\\"Brust\\\"; lett. paksis \\\"Hausecke\\\"; toch. A pässäṃ, B päścane \\\"die beiden \"\n                \"Bruste\\\" ... WP. II 3 f., WH. II 270.' The page number is exact; the gloss is not 'breast'.\")}\n    ],\n    \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. peg-\", \"stance\": \"supports\",\n       \"note\": \"'peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA. [Pok. (peg-), pog- 792.]' — this is verbatim Nourai's chart (grep '^peg-' AHD_watkins1985.txt line 820).\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 3-4 (WLD_Bd2_pages.txt leaf 8)\", \"stance\": \"partial\",\n       \"note\": \"Entry headed 'pag-' (their spelling) with 'ai. pajasyá- n. Bauchgegend, Weichen, russ. pachu \\\"Leistengegend\\\", pacha \\\"Achselhohle\\\" ... ein io-St. *pagio- in cech. paze \\\"Arm\\\"' — again 'flank/armpit', no 'breast'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann, alphabetical\", \"stance\": \"silent\",\n       \"note\": \"grep of IEC.txt for 'peg-', 'pokso-', 'pektos' returns no headword for this root.\"}\n    ],\n    \"nodes\": [\n      {\n        \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"pakša\",\n        \"verdict\": \"plausible\",\n        \"derivation\": (\"Sanskrit पक्ष (pakṣá-) m. is real and old (RV), but its meanings are 'wing, feather; side, flank; \"\n                       \"half (of a month); party, faction' — not 'breast'. Monier-Williams and Wiktionary give no 'breast' \"\n                       \"sense; the chart's 'breast' is imported from Nourai's root gloss. Formally pakṣa- goes back to \"\n                       \"Proto-Indo-Iranian *pakšás 'side, flank' < PIE *peg-/*pok-s-, with the regular Indo-Aryan treatment \"\n                       \"of *-ks- > -kṣ-; the Iranian cognate is Ossetic fæxs 'side'. So the arrow root -> Sanskrit is sound; \"\n                       \"only the gloss 'breast' is wrong.\"),\n        \"derivation_fa\": (\"واژهٔ سنسکریت pakṣá- «بال، پر؛ پهلو، سو؛ نیمه (ماه)؛ دسته» از ریگ‌ودا به‌بعد گواهی شده است، اما \"\n                          \"معنای «سینه» برای آن ثبت نشده و نورایی آن را از معنای ریشه به این گره تسری داده است. از دید آوایی \"\n                          \"pakṣá- بازماندهٔ هندوایرانی آغازین *pakšás «پهلو، سو» است (خوشهٔ *-ks- در هندوآریایی به -kṣ- بدل \"\n                          \"می‌شود) و هم‌ریشهٔ آن در ایرانی، fæxs آسی به معنی «پهلو» است. بنابراین پیکان «ریشه ← سنسکریت» درست \"\n                          \"است و تنها معنای «سینه» نادرست است.\"),\n        \"sources\": [S[\"paksa\"]],\n        \"ref_check\": [\n          {\"ref\": \"AHD\", \"status\": \"partial\",\n           \"note\": \"Watkins 1985 s.v. peg-: '2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA.' Watkins glosses the Sanskrit word 'wing' only, and marks the connection 'possibly'.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"POK\", \"where\": \"IEW 792 (POK_03 leaf 25)\", \"stance\": \"partial\",\n           \"note\": \"'Ai. pákṣa- m. \\\"Schulter, Flugel\\\" und \\\"Seitenpfosten\\\", pákṣas- n. \\\"Seite\\\"' — shoulder/wing/side, not breast.\"},\n          {\"src\": \"KLN\", \"where\": \"1966 ed. p.1272 s.v. punka (leaf 678)\", \"stance\": \"partial\",\n           \"note\": \"'fr. OI. pakṣaḥ, pákṣas, \\\"wing, side, half\\\", which is possibly cogn. with Lett. paksis, \\\"corner of a house\\\", Russ. pach, \\\"flank\\\".' Klein too has no 'breast'.\"},\n          {\"src\": \"WLD\", \"where\": \"WP II 3-4\", \"stance\": \"partial\", \"note\": \"lists ai. pajasyá- 'Bauchgegend, Weichen' beside the pakṣa- family; gloss 'flank'.\"}\n        ]\n      },\n      {\n        \"id\": 2, \"lang\": \"Hindustani\", \"words\": \"pankâ\",\n        \"verdict\": \"transcription_suspect\",\n        \"error_in\": \"book\",\n        \"book_prints\": \"pankâ\",\n        \"correct_form\": \"pankhā\",\n        \"derivation\": (\"The Hindustani word is पंखा / پنکھا paṅkhā 'fan', with an aspirated -kh-, not 'pankâ'. The printed page \"\n                       \"(pdf 385, image saved as data/verification/sources/refs/ocr/BOOK/385.png) does read 'pankâ', so this is \"\n                       \"Nourai's own misprint, not an extraction error: the JSON is faithful to the book. Klein, whom Nourai cites \"\n                       \"here, spells it 'pankha'. The history: Sanskrit pakṣá- 'wing' > pakṣaka- (with -ka- suffix) > Sauraseni \"\n                       \"Prakrit pakkha- > Hindi paṅkh 'feather, wing', whence paṅkhā 'fan' (the -kh- is the Middle Indo-Aryan \"\n                       \"reflex of -kṣ-, and the nasal is an anusvara developed before the cluster). Its basic sense is simply \"\n                       \"'fan' (originally a palmyra-leaf hand fan); the 'curtain hung from the ceiling and pulled by a servant' \"\n                       \"that Nourai glosses is the Anglo-Indian specialisation of the word from the 17th c. on, not the Hindustani \"\n                       \"meaning.\"),\n        \"derivation_fa\": (\"صورت درست واژهٔ هندوستانی paṅkhā «بادبزن» است (با کاف دمیده -kh-)، نه «pankâ». تصویر صفحهٔ چاپی \"\n                          \"(pdf ۳۸۵) نشان می‌دهد که خودِ کتاب «pankâ» چاپ کرده است؛ پس این خطای چاپی نورایی است نه خطای خوانش \"\n                          \"اسکن. کلاین که نورایی به او ارجاع می‌دهد، «pankha» نوشته است. راه تحول چنین است: pakṣá- سنسکریت \"\n                          \"«بال» ← pakṣaka- (با پسوند -ka-) ← pakkha- در پراکریت شورسنی ← paṅkh هندی «پر، بال» و از آن paṅkhā \"\n                          \"«بادبزن»؛ خوشهٔ -kṣ- در هندوآریایی میانه به -kh- بدل می‌شود و پیش از آن غنّه (انوسوارَه) پدید می‌آید. \"\n                          \"معنای پایهٔ واژه همان «بادبزن» است؛ معنای «پردهٔ آویخته از سقف که خدمتکار می‌کشد» تخصیص انگلیسی‌ـ‌هندی \"\n                          \"واژه از سدهٔ هفدهم به بعد است.\"),\n        \"sources\": [S[\"pankha\"], S[\"punkah\"]],\n        \"ref_check\": [\n          {\"ref\": \"KLN:1272\", \"status\": \"partial\",\n           \"note\": \"Klein 1966 p.1272 (leaf 678): 'punka, punkah, n., a large curtain serving to fan a room. — Hind. pankha, \\\"a fan\\\", fr. pankh, \\\"feather, wing\\\", fr. OI. pakṣaḥ, pákṣas, \\\"wing, side, half\\\"...' — the derivation is Nourai's, but Klein spells the Hindi word pankha and glosses it 'a fan'.\"},\n          {\"ref\": \"AHD\", \"status\": \"supports\",\n           \"note\": \"Watkins 1985 s.v. peg- routes Sanskrit pakṣaḥ to English PUNKA, i.e. the same Sanskrit -> Hindustani -> English chain.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.742 s.v. PUNKAH\", \"stance\": \"partial\",\n           \"note\": \"'PUNKAH, s. Hind. pankhā. a. In its original sense a portable fan, generally made from the leaf of the palmyra ... b. But the specific application in Anglo-Indian colloquial is to the large fixed and swinging fan, formed of cloth stretched on a rectangular frame, and suspended from the ceiling.' Confirms the aspirate and shows the 'curtain' sense is the Anglo-Indian one.\"},\n          {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1622 (printed p.132)\", \"stance\": \"supports\",\n           \"note\": \"'1622. Hind. pankha: \\\"Facher\\\"; hieraus angloind. engl. punkah \\\"Facher aus den Blattern der Facherpalme Borassus flabelliformis\\\"...'\"},\n          {\"src\": \"AID\", \"where\": \"Whitworth, Anglo-Indian Dictionary\", \"stance\": \"silent\",\n           \"note\": \"grep -i 'punkah|pankha' AID.txt returns no entry in the local OCR.\"}\n        ]\n      },\n      {\n        \"id\": 3, \"lang\": \"Persian\", \"words\": \"pankeh\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\"New Persian پنکه pankeh / panke 'electric fan' is a modern (19th-20th c.) loan from Hindi-Urdu paṅkhā, \"\n                       \"taken over during the period of Indo-Persian contact and British India; Persian has no aspirated stops, \"\n                       \"so paṅkhā was rendered pank-, and the Indic final -ā was reshaped as the Persian final -e(h) spelt with \"\n                       \"silent ه, exactly as in other Indic loans. Mo'in tags the entry [هند.] 'Hindi'. Meaning 'fan' is right; \"\n                       \"the word only later came to mean 'electric fan'.\"),\n        \"derivation_fa\": (\"واژهٔ «پنکه» در فارسی نو وام‌واژه‌ای است از هندی‌ـ‌اردوی paṅkhā «بادبزن» که در دورهٔ نو (سدهٔ سیزدهم \"\n                          \"و چهاردهم هجری، همزمان با روابط ایران و هند بریتانیا) وارد فارسی شده است. چون فارسی واکهٔ دمیده \"\n                          \"(kh دمیده) ندارد، paṅkhā به pank- بدل شده و کشیدهٔ پایانی -ā به «ـه»ی پایانی فارسی (e) دگرگون شده \"\n                          \"است، همان‌گونه که در دیگر وام‌واژه‌های هندی. معین در فرهنگ خود این واژه را با نشان [هند.] آورده و \"\n                          \"«بادبزن برقی» معنی کرده است. ادعای نورایی درست است.\"),\n        \"sources\": [S[\"pankeh\"], S[\"ab_pankeh\"]],\n        \"ref_check\": [\n          {\"ref\": \"MON:824\", \"status\": \"partial\",\n           \"note\": \"Mo'in's entry, read through abadis.ir (فرهنگ معین section): '(پَ کِ) [هند.] (اِ.) بادبزن برقی' — Mo'in expressly tags the word Hindi, which is Nourai's claim. The page number 824 could not be checked (Mo'in's lexicon volumes are not on disk with pagination), but it is consistent with the position of پنکه in the پ section.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"MON\", \"where\": \"abadis.ir, فرهنگ معین s.v. پنکه\", \"stance\": \"supports\",\n           \"note\": \"'(پَ کِ) [هند.] (اِ.) بادبزن برقی.' Also Farhang-e Amid: 'بادزن برقی'.\"},\n          {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\",\n           \"note\": \"grep 'پنکه' in Aryanpur's IE-roots dictionary returns nothing — he treats only inherited vocabulary.\"},\n          {\"src\": \"BQT\", \"where\": \"Borhan-e Qate'\", \"stance\": \"silent\",\n           \"note\": \"grep 'پنکه' in BQT_v1_pages.txt / BQT_v2_pages.txt returns nothing; the word is later than Borhan (1062 AH).\"}\n        ]\n      },\n      {\n        \"id\": 4, \"lang\": \"English\", \"words\": \"punka\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\"English punkah (also punka) is an 18th-19th c. Anglo-Indian borrowing of Hindi paṅkhā. It is first \"\n                       \"recorded in Indian English contexts in the 17th c. (W. Finch 1610 'two Punkawes to gather wind', \"\n                       \"Bernier 1668 'their great Pankas, or Fans') and settles in the sense Nourai gives — the big cloth-on-frame \"\n                       \"fan slung from the ceiling and worked by a rope-pulling servant (the punkah-wallah) — during the Raj. \"\n                       \"The English spelling with -k- (no aspirate) reflects the usual anglicisation of Indic kh.\"),\n        \"derivation_fa\": (\"واژهٔ انگلیسی punkah/punka وام‌واژه‌ای انگلیسی‌ـ‌هندی از paṅkhā هندی است. نخستین کاربردهای آن در \"\n                          \"متون انگلیسیِ هند از سدهٔ هفدهم میلادی است (فینچ ۱۶۱۰، برنیه ۱۶۶۸) و در دورهٔ استعمار بریتانیا معنای \"\n                          \"ویژهٔ «بادبزن بزرگ پارچه‌ای آویخته از سقف که خدمتکار با ریسمان می‌کشد» یافته است. نبودِ «h» در املای \"\n                          \"انگلیسی، بازتاب عادیِ ساده‌شدن همخوان دمیدهٔ هندی در انگلیسی است. ادعای نورایی درست است.\"),\n        \"sources\": [S[\"punkah\"]],\n        \"ref_check\": [\n          {\"ref\": \"KLN:1272\", \"status\": \"supports\",\n           \"note\": \"Klein 1966 p.1272: 'punka, punkah, n., a large curtain serving to fan a room. — Hind. pankha...' — both the headword forms and the gloss are Nourai's, word for word.\"},\n          {\"ref\": \"AHD:1060\", \"status\": \"not_checked\",\n           \"note\": \"the 1975/76 AHD main dictionary is not open online; the Watkins appendix (on disk) lists PUNKA under peg-, which covers the same claim.\"},\n          {\"ref\": \"FWE:233\", \"status\": \"not_checked\",\n           \"note\": \"Bliss, A Dictionary of Foreign Words and Phrases in Current English (1966) is lending-only on archive.org; no copy on disk.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"HJB\", \"where\": \"Hobson-Jobson pp.742-743 s.v. PUNKAH\", \"stance\": \"supports\",\n           \"note\": \"gives 'PUNKAH, s. Hind. pankhā' with the 1610, 1668, 1809 quotations for the ceiling fan.\"},\n          {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1622 (p.132)\", \"stance\": \"supports\",\n           \"note\": \"'hieraus angloind. engl. punkah' — with the date 1622 in Lokotsch's English word-list ('punkah 1622').\"},\n          {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"silent\",\n           \"note\": \"grep '^PUNKAH' SKT.txt finds nothing; Skeat omits Anglo-Indian words of this class.\"}\n        ]\n      },\n      {\n        \"id\": 5, \"lang\": \"Latin\", \"words\": \"pectus\",\n        \"verdict\": \"plausible\",\n        \"derivation\": (\"Latin pectus, -oris n. 'chest, breast' (Ennius on) is correctly given. Its attachment to this root is the \"\n                       \"weak link: Pokorny 792 and Watkins put it here as a suffixed *pek-tos-, comparing Skt. pakṣas- 'side' and \"\n                       \"Toch. B pāścane 'the two breasts', but the *-k-/*-g- alternation is irregular and de Vaan (via Wiktionary) \"\n                       \"calls the PIE precursor uncertain, preferring a comparison with Old Irish ucht 'breast'. So the word and the \"\n                       \"gloss are right; the arrow from *peg- is one of several competing suggestions (*pekt-, *pek-, *peg-).\"),\n        \"derivation_fa\": (\"واژهٔ لاتین pectus (اضافی pectoris) «سینه» از قدیمی‌ترین متون لاتین (انیوس) گواهی شده و معنای داده‌شده \"\n                          \"درست است. حلقهٔ سست، خودِ پیوند آن با ریشهٔ *peg- است: پوکورنی (ص ۷۹۲) و واتکینز آن را صورت پسوندی \"\n                          \"*pek-tos- می‌دانند و با pakṣas- سنسکریت «پهلو» و pāścane تخاری «دو پستان» می‌سنجند، ولی جانشینی \"\n                          \"*g/*k در این ریشه بی‌قاعده است و دِ ڤان (به نقل ویکی‌واژه) ریشهٔ هندواروپایی آن را نامعلوم می‌داند و \"\n                          \"همسنجی با ucht ایرلندی کهن «سینه» را ترجیح می‌دهد. پس ادعای نورایی با احتیاط پذیرفتنی است.\"),\n        \"sources\": [S[\"pectus\"]],\n        \"ref_check\": [\n          {\"ref\": \"AHD\", \"status\": \"supports\",\n           \"note\": \"Watkins 1985 s.v. peg-: '1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET.'\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"POK\", \"where\": \"IEW 792\", \"stance\": \"supports\",\n           \"note\": \"'lat. pectus \\\"Brust\\\"' stands in the same entry, between ai. pákṣas- 'Seite' and toch. B päścane 'die beiden Bruste'.\"},\n          {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, s.v. tergum (cross-reference)\", \"stance\": \"silent\",\n           \"note\": \"grep '^pectus' in LAT.txt/LEW_1910.txt finds no headword block in the local OCR (only the cross-reference under tergus: 'Tergus, -oris, plus recent, est fait d'apres pectus'); Ernout-Meillet's own pectus entry is not in the scanned range.\"},\n          {\"src\": \"KLN\", \"where\": \"1966 s.v. pectoral\", \"stance\": \"supports\",\n           \"note\": \"Klein takes pectoral from L. pectus, gen. pectoris, 'breast' (p.1146 area, leaf 615).\"}\n        ]\n      },\n      {\n        \"id\": 6, \"lang\": \"English\", \"words\": \"pectoral\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\"English pectoral is a learned borrowing (15th c.) of Latin pectorālis 'of the breast', adjective in \"\n                       \"-ālis to the oblique stem pector- of pectus; it entered English partly through Old French pectoral. \"\n                       \"The noun sense Klein records — 'something worn on the breast, specif. the breast-plate of the Jewish \"\n                       \"high priest' — is the Vulgate's pectorale. The chart leaves the gloss blank; the arrow Latin -> English \"\n                       \"is uncontroversial.\"),\n        \"derivation_fa\": (\"واژهٔ انگلیسی pectoral وام‌واژه‌ای دانشورانه از سدهٔ پانزدهم میلادی است: از لاتین pectorālis «مربوط \"\n                          \"به سینه»، صفتی با پسوند -ālis بر ستاک غیرفاعلی pector- از pectus، که تا اندازه‌ای از راه فرانسهٔ کهن \"\n                          \"pectoral به انگلیسی رسیده است. معنای اسمیِ آن نزد کلاین «چیزی که بر سینه می‌آویزند، به‌ویژه سینه‌بندِ \"\n                          \"کاهن بزرگ یهود» بازتاب pectorale در ترجمهٔ ولگات است. این حلقه (لاتین ← انگلیسی) بی‌مناقشه است و \"\n                          \"ادعای نورایی درست است.\"),\n        \"sources\": [S[\"pectus\"]],\n        \"ref_check\": [\n          {\"ref\": \"AHD\", \"status\": \"supports\",\n           \"note\": \"Watkins 1985 s.v. peg-: Latin pectus yields 'PECTORAL; EXPECTORATE, PARAPET'.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. pectoral (line 27810 of KLN_1966.txt)\", \"stance\": \"supports\",\n           \"note\": \"'pectoral, n., something worn on the breast; specif. the breast plate of the Jewish high priest.'\"},\n          {\"src\": \"SKT\", \"where\": \"Skeat\", \"stance\": \"silent\",\n           \"note\": \"no '^PECTORAL' headword in the local Skeat OCR.\"}\n        ]\n      }\n    ]\n   },\n   {\n    \"entry\": 1,\n    \"root\": \"Peî\",\n    \"verdict\": \"confirmed\",\n    \"modern_form\": \"PIE *peyH- / *peyh₂- (Pokorny pei(ə)-, pī-) 'to be fat, swell (with milk); sap, fat'\",\n    \"note\": (\"Pokorny 793 has exactly this root: 'pei(ə)-, pī- \\\"fett sein, strotzen\\\"; pei-tu-, poi-tu-, pī-tu- \\\"Fett, Saft, \"\n             \"Trank\\\", pi-k- \\\"Pech\\\", pī-mo- \\\"fett\\\", pī-u-er-/-en- \\\"Fett, fett\\\", poi-uā \\\"(fette) Wiese\\\"; poi-men- \"\n             \"\\\"Muttermilch\\\", pi-pi-us-ī \\\"Milch habend\\\".' Watkins prints 'peiə-. Also pei-. To be fat, swell. [Pok. pei(ə)- 793.]' \"\n             \"Wiktionary's laryngealist form is *peyh₂- 'to swell (with milk); to be swollen, fat'. Nourai's page number, \"\n             \"language label and gloss 'sap, fat' are all right. Remarkably, Pokorny's own entry on this page names two of the \"\n             \"Persian words of the chart: 'av. payah- n. \\\"Milch\\\", av. paēman- n. \\\"Muttermilch\\\"; np. pīnū \\\"saure Milch, \"\n             \"frischer Kase\\\"'. The one branch that is not Pokorny's is angubīn (node 7-9), and the *fra-/duš- compounds are \"\n             \"Iranian-internal, not PIE.\"),\n    \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *peyH- / *peyh₂- «چاق بودن، آماسیدن (از شیر)؛ شیره، پیه» — پوکورنی در صفحهٔ ۷۹۳ \"\n                \"دقیقاً همین سرواژه را با صورت pei(ə)-, pī- «fett sein, strotzen» آورده و گونه‌های آن را نیز برشمرده است: \"\n                \"*pī-tu- «پیه، شیره، نوشیدنی»، *pī-mo- «چرب»، *poi-men- «شیر مادر». واتکینز نیز «peiə-. To be fat, swell» \"\n                \"نوشته و ویکی‌واژه صورت حنجره‌ای *peyh₂- را می‌آورد. شمارهٔ صفحه، برچسب زبانی و معنای «شیره، پیه» در نمودار \"\n                \"نورایی هر سه درست است. نکتهٔ درخور توجه آنکه خودِ پوکورنی در همان صفحه payah- و paēman- اوستایی و «پینو»ی \"\n                \"فارسی را در ذیل این ریشه آورده است. تنها شاخه‌ای که در پوکورنی نیست شاخهٔ «انگبین» است.\"),\n    \"sources\": [S[\"peyh2\"], S[\"payHas\"]],\n    \"ref_check\": [\n      {\"ref\": \"POK:793\", \"status\": \"supports\",\n       \"note\": \"IEW p.793 (POK_03.txt leaf 26): 'pei(ə)-, pī- \\\"fett sein, strotzen\\\" ... ai. páyas- n. \\\"Saft, Wasser, Milch\\\", av. payah- n. \\\"Milch\\\", av. paēman- n. \\\"Muttermilch\\\" (: ags. fǣmne); np. pīnū \\\"saure Milch, frischer Kase\\\" (: lit. pienas \\\"Milch\\\") ... WP. II 73 ff.' Exactly Nourai's root and page.\"}\n    ],\n    \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. peiə- (line 823)\", \"stance\": \"supports\",\n       \"note\": \"'peiə-. Also pei-. To be fat, swell. 1. Extended o-grade form *poid- in Germanic *faitaz ... 3. Possibly suffixed zero-grade form *pi-nu- in Latin pinus, pine tree (yielding a resin): PINE. ... [Pok. pei()- 793.]'\"},\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 73-75 (WLD_Bd2_pages.txt leaves 77-79)\", \"stance\": \"supports\",\n       \"note\": \"the full entry, incl. '*pīmo-s \\\"fett\\\" in gr. πῑμελή \\\"Fett\\\", lat. opīmus', '*pīuos- und *pīu-er-/-en- \\\"Fett, fett\\\": ai. pīvas- n., av. pīvah- n. \\\"Fett, Speck\\\"' and 'ai. pitú-ḥ m., av. pitú-š m. \\\"Saft, Trank, Nahrung, Speise\\\"'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann, s.v. pit- (1) 'food'\", \"stance\": \"supports\",\n       \"note\": \"'pit- (1) \\\"food\\\": Skt. pituh, m. id.; Av. pitus, m. id.; Oss. fid \\\"meat\\\"; OIr. ith \\\"fat\\\"; OCS pista \\\"food\\\"; Li. pietus \\\"food\\\"; ON cf. (?) fita, f. \\\"fat\\\".'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 5.83 CHEESE / 5.89 BUTTER\", \"stance\": \"silent\",\n       \"note\": \"Buck's cheese section lists Av. fšuta-, tūiri- but no Persian panīr and no discussion of this root.\"}\n    ],\n    \"nodes\": [\n      {\n        \"id\": 1, \"lang\": \"Avestan\", \"words\": \"pitu, pithwa; fra-pithwa; duš-pithwa\",\n        \"verdict\": \"plausible\",\n        \"derivation\": (\"Av. pitu- (nom. pitu-š) m. 'food, victuals, esp. meat dish' is well attested (Y. 9.11) and is the exact \"\n                       \"cognate of Skt. pitú- 'juice, drink, nourishment', from PIE *pih₂-tu-. The stem piθwa- is its thematic \"\n                       \"by-form 'meal', seen in the attested compounds bi-piθwa- 'having two meals', θri-piθwa- 'having three meals', \"\n                       \"tarō.piθwa- 'ill-fed, lacking food' and rapiθwā- 'midday (meal-time)'. fra-piθwa- is likewise attested, but \"\n                       \"Bartholomae (col. 984) glosses it 'in Fulle, reichlich vorhanden, copiosus' (Vd. 2), i.e. 'abundant', not \"\n                       \"'fat'; Horn no. 813 renders it 'gut genahrt, gedeihend' — the 'fat' sense belongs to the Persian descendant, \"\n                       \"not to the Avestan word. duš-piθwa- 'bad fat, abscess', by contrast, is NOT in Bartholomae at all; the \"\n                       \"attested privative compound of this stem is tarō.piθwa-. Nourai's duš-piθwa- is a back-projection of New \"\n                       \"Persian دژپیه; the gloss 'fat' on the node as a whole is therefore an over-reading.\"),\n        \"derivation_fa\": (\"در اوستا pitu- (فاعلی pitu-š) «خوراک، توشه، به‌ویژه خوراک گوشتی» به‌روشنی گواهی شده (یسنا ۹٫۱۱) و \"\n                          \"هم‌ریشهٔ دقیق pitú- سنسکریت «شیره، نوشابه، خوراک» و بازماندهٔ *pih₂-tu- هندواروپایی است. ستاک piθwa- \"\n                          \"گونهٔ ستاک‌داری همان واژه به معنی «وعدهٔ غذا» است و در ترکیب‌های گواهی‌شدهٔ bi-piθwa- «دارای دو \"\n                          \"وعده»، θri-piθwa- «دارای سه وعده»، tarō.piθwa- «کم‌خوراک» و rapiθwā- «نیم‌روز» دیده می‌شود. \"\n                          \"fra-piθwa- نیز گواهی شده، اما بارتولومه (ستون ۹۸۴) آن را «فراوان، بسیار، copiosus» و هرن (بند ۸۱۳) \"\n                          \"«خوب‌پرورده، بالنده» معنی می‌کند؛ معنای «چاق» از آنِ بازماندهٔ فارسی است نه واژهٔ اوستایی. اما \"\n                          \"duš-piθwa- در فرهنگ بارتولومه هیچ‌گاه نیامده است و بازسازیِ واپس‌نگرِ نورایی از «دژپیهِ» فارسی نو \"\n                          \"است. پس این گره با احتیاط پذیرفتنی است و معنای «پیه» برای واژهٔ اوستایی نادرست.\"),\n        \"sources\": [S[\"peyh2\"], S[\"farbeh\"]],\n        \"ref_check\": [\n          {\"ref\": \"HRN:81\", \"status\": \"supports\",\n           \"note\": \"Horn, Grundriss p.81 no.365 (HRN.txt leaf 102): 'pīh \\\"Talg, Fett\\\" ... ap. *piθu-; aw. pitu- \\\"Speise\\\"; phlv. pīh bezw. pih; ai. pitú-. Vergl. np. ferbih (No. 813). aw. pīvah- \\\"Fett\\\"' — exactly Nourai's Avestan pitu- and the link to pīh.\"},\n          {\"ref\": \"HRN:181\", \"status\": \"partial\",\n           \"note\": \"Horn p.181 no.813 (leaf 202): 'ferbih, ferbeh, ferbī \\\"fett\\\". Vergl. np. pīh (No. 365). aw. frapiθwa- \\\"Vorzug, first-rate\\\" (Geldner); phlv. frapīh bezw. farpīh; ai. prapitvá-.' Supports fra-piθwa- > farbeh, but glosses the Avestan word 'first-rate', not 'fat'; and Horn says nothing about duš-piθwa-.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW cols. 826 (pitav-), 984 (fra-piθwa-), 731 (dāityō.piθwa-), 1300 (tarō.piθwa-)\", \"stance\": \"partial\",\n           \"note\": \"'j. pitav- m. \\\"Speise\\\", insbes. feste, \\\"Fleischspeise\\\": yim ... pitūm pacata' ; 'j. fra-piθwa- Adj. \\\"in Fulle, reichlich vorhanden, copiosus\\\"' ; 'j. bi-piθwa- Adj. \\\"der zwei Mahlzeiten bekommt\\\"'. A grep of BRT.txt for du(š)/duz + piθwa returns nothing: duš-piθwa- is unattested.\"},\n          {\"src\": \"KNT\", \"where\": \"Kent, Old Persian lexicon\", \"stance\": \"silent\",\n           \"note\": \"grep 'pitu' / 'piθu' in KNT.txt gives no Old Persian entry; Horn's *pi(θ)u- is a reconstruction.\"},\n          {\"src\": \"HUB\", \"where\": \"Hubschmann, Persische Studien §813 (HUB.txt line 2960, 7220)\", \"stance\": \"supports\",\n           \"note\": \"'Gegensatz von zd. frapiθwa- \\\"gut genahrt, gedeihend\\\" = np. farbih \\\"pinguis, robustus, florens, copiosus\\\" ist zd. tarō.piθwa- Vd. 13, 20 = \\\"schlecht genahrt\\\". Np. farbī ... = phl. frapīh = zd. *fra-piθwa-?' — note Hubschmann's question mark.\"}\n        ]\n      },\n      {\n        \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"pîh; fra-pîh\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\"MacKenzie's Concise Pahlavi Dictionary has both words verbatim: 'pīh [TLBA = A trb; pyh | N ~] fat, tallow' \"\n                       \"(p.68, the Aramaic heterogram TLBA standing for Semitic trb 'fat'), and 'frabih [plpyh | (P frbyw), N farbih] \"\n                       \"fat, stout' (p.32) — where the Book-Pahlavi spelling plpyh is literally fra-pīh, Nourai's form. Phonetically \"\n                       \"Old Iranian *pitu- gave MP pīh by the regular loss of intervocalic -t- and its replacement by -h- after a long \"\n                       \"vowel (*pitu > *piθu > pīh), and *fra-piθwa- gave frabīh with fra- > far- and the voicing of the p after r; \"\n                       \"Manichaean Parthian has frbyw (Henning, BSOS IX 1, p.82). Nourai's chart is exactly MacKenzie's data.\"),\n        \"derivation_fa\": (\"هر دو صورت در فرهنگ کوچک پهلوی مکنزی آمده است: «pīh [TLBA؛ pyh] چربی، پیه» (ص ۶۸؛ هزوارش TLBA همان \"\n                          \"trb سامی «پیه» است) و «frabih [plpyh؛ فارسی نو farbih] چاق، فربه» (ص ۳۲) که املای پهلویِ plpyh دقیقاً \"\n                          \"همان fra-pīh نورایی است. از دید آوایی، *pitu- ایرانی باستان با سایش و افتادن -t- میان‌واکه‌ای و \"\n                          \"پیدایش -h- پس از واکهٔ بلند به pīh فارسی میانه رسیده (*pitu > *piθu > pīh) و *fra-piθwa- به frabīh \"\n                          \"بدل شده که در آن fra- به far- و «پ» پس از «ر» به «ب» نرم شده است؛ در پارتی مانوی frbyw ثبت شده \"\n                          \"است (هنینگ). ادعای نورایی درست است.\"),\n        \"sources\": [S[\"pih\"], S[\"farbeh\"]],\n        \"ref_check\": [\n          {\"ref\": \"BQT:1450\", \"status\": \"supports\",\n           \"note\": \"Borhan-e Qate' printed p.1450 = vol.3 pdf p.243 (BQT_v3_pages.txt leaf 242), the page carrying فربود/فربه; Mo'in's footnote 4 there reads 'فربی = ... اوستا frapithwa؟ ... = frapīh ... فی پازند padh = pih ... در اوراق مانوی به پارتی frhyw (Henning, A list of Middle Persian..., BSOS IX, 1, p.82)' — i.e. exactly Nourai's Av. fra-piθwa- > Pahl. frapīh chain.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 pp. 32 and 68\", \"stance\": \"supports\",\n           \"note\": \"'frabih [plpyh | (P frbyw), N farbih] fat, stout.' and 'pīh [TLBA = A trb; pyh | N ~] fat, tallow.' (also 'pih [pyhw'] food, victuals', the direct continuation of Av. pitu- 'food').\"},\n          {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"partial\",\n           \"note\": \"Nyberg has no pīh entry in the local OCR, but does give 'pēm [pym] milk 423.13.25 ... Av. (817) paēman-; Paz. pīm', showing the same root family in Pahlavi.\"},\n          {\"src\": \"HRN\", \"where\": \"Grundriss no.365 / no.813\", \"stance\": \"supports\",\n           \"note\": \"'phlv. pīh bezw. pih' and 'phlv. frapīh bezw. farpīh'.\"}\n        ]\n      },\n      {\n        \"id\": 3, \"lang\": \"Persian\", \"words\": \"pîh; farbeh\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\"NP پیه pīh 'fat, tallow' continues MP pīh unchanged; its alternative spelling په peh (the chart's \"\n                       \"'په ۱' footnote) and پی pi are late shortenings. NP فربه farbeh / farbih 'fat, corpulent; copious' \"\n                       \"continues MP frabīh: Old Iranian *fra-piθwa- 'abundantly provided, well-fed' > MP frabīh > NP farbeh, \"\n                       \"with the usual Middle-to-New Persian anaptyxis fra- > far- and the raising of the final -īh to -eh in \"\n                       \"modern Iranian pronunciation (Dari and the classical reading keep farbih). Wiktionary reconstructs \"\n                       \"exactly Nourai's chain: MP plpyh /frabīh/ < Old Persian *frapīδwa- < Proto-Iranian *fra- + *piHtú, \"\n                       \"'by surface analysis فرـ (far-) + پیه (pih)'. Both words and both glosses are right.\"),\n        \"derivation_fa\": (\"«پیه» در فارسی نو دنبالهٔ بی‌تغییر pīh فارسی میانه است؛ گونه‌های «په» (همان زیرنویس ۱ در نمودار) و \"\n                          \"«پی» کوتاه‌شدهٔ متأخر آن‌اند. «فربه/فربی» نیز دنبالهٔ frabīh فارسی میانه است: از ایرانی باستان \"\n                          \"*fra-piθwa- «برخوردار، خوب‌پرورده» ← frabīh پهلوی ← «فربه» فارسی نو، با پیدایش واکهٔ میانجی در \"\n                          \"fra- > far- و بدل شدن -īh پایانی به -eh در تلفظ ایرانیِ امروز (در فارسی دری و خوانش کلاسیک هنوز \"\n                          \"farbih است). ویکی‌واژه همین زنجیره را می‌آورد: فارسی میانه frabīh ← پارسی باستان *frapīδwa- ← \"\n                          \"ایرانی آغازین *fra- + *piHtú، و از دید تجزیهٔ سطحی «فرـ + پیه». هر دو واژه و هر دو معنا درست است.\"),\n        \"sources\": [S[\"pih\"], S[\"farbeh\"]],\n        \"ref_check\": [\n          {\"ref\": \"BQT:1450\", \"status\": \"supports\",\n           \"note\": \"Borhan p.1450 (v3 leaf 242) carries the headword فربه ('بمعنی فربه باشد که در مقابل لاغر است') with Mo'in's etymological footnote deriving فربی from Av. *frapiθwa- via Pahl. frapīh, and comparing Sariqoli farbé, Manichaean Parthian frbyw.\"},\n          {\"ref\": \"MON:844\", \"status\": \"partial\",\n           \"note\": \"Mo'in's entries themselves support the words, but the page number looks wrong: Nourai cites MON:824 for پنکه and MON:969 for پینو, and in Mo'in's strict alphabetical order پیه follows پینو, so it must stand at c. p.970+, not 844. Probably a slip in the book (the printed page does read MON:844).\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"HRN\", \"where\": \"Grundriss nos. 365 and 813\", \"stance\": \"supports\",\n           \"note\": \"'365. pīh \\\"Talg, Fett\\\" ... Vergl. np. ferbih (No. 813)' and '813. ferbih, ferbeh, ferbī (d.i. *ferbihi) \\\"fett\\\". Vergl. np. pīh (No. 365).'\"},\n          {\"src\": \"HUB\", \"where\": \"Persische Studien §813\", \"stance\": \"supports\",\n           \"note\": \"'np. farbih \\\"pinguis, robustus, florens, copiosus\\\" ... = phl. frapīh = zd. *fra-piθwa-?' — note also Hubschmann's remark that Judaeo-Persian farbī goes back to an OP *fra-pitu-.\"},\n          {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-ha, s.v. پیه (ARY_pages.txt leaf 184, pdf p.185)\", \"stance\": \"supports\",\n           \"note\": \"the entry پیه lists 'اوستایی pitu-/piθwa-, پارسی باستان *pitu-, پهلوی pīh, اوستی, کردی, بلوچی, سانسکریت pitu/pīvas, یونانی, لاتین' and English FAT / Old English FÆTT in the same family — an independent modern confirmation of the whole branch.\"}\n        ]\n      },\n      {\n        \"id\": 4, \"lang\": \"Persian\", \"words\": \"došpîh\",\n        \"verdict\": \"plausible\",\n        \"derivation\": (\"The word is real: Borhan-e Qate' (vol. 2, the 'باب دال با زای فارسی' section) has دژپیه, defined as \"\n                       \"'گره‌پایی ... که در میان گوشت و پوست آدمی و حیوانات دیگر می‌باشد، و معرب آن غدود است' — a lump between \"\n                       \"flesh and skin, Arabic ghudūd 'gland'; Mo'in glosses it 'غده‌های زیرپوستی' (subcutaneous glands) and \"\n                       \"Wiktionary 'tumour, ganglion'. So Nourai's gloss 'abscess' is a shade off — it is a gland/nodule, not a \"\n                       \"suppuration. Morphologically it is transparently a NEW PERSIAN compound دژ dož- (< OIr. duš- 'bad, ill-') \"\n                       \"+ پیه pih 'fat', of the same type as دژخیم, دژآگاه, and Borhan's own variants دشپل/دشپیل; the arrow should \"\n                       \"therefore start from the Persian pīh of node 3, not from an Avestan *duš-piθwa-, which is nowhere attested \"\n                       \"(Bartholomae has only tarō.piθwa- 'ill-fed'). The etymon is right, the route is drawn one step too early.\"),\n        \"derivation_fa\": (\"خودِ واژه واقعی است: برهان قاطع (جلد دوم، «باب دال بی‌نقطه با زای فارسی») مدخل «دژپیه» را چنین \"\n                          \"تعریف می‌کند: «گره‌پایی ... که در میان گوشت و پوست آدمی و حیوانات دیگر می‌باشد، و معرّب آن غُدود \"\n                          \"است»؛ معین نیز «غده‌های زیرپوستی» معنی کرده و ویکی‌واژه «غده، ورم». پس معنای «آبسه/دُمَل» که نورایی \"\n                          \"داده اندکی نادرست است. از دید ساخت‌واژه، «دژپیه» ترکیبی است روشن و متعلق به فارسی نو: «دژ» (از \"\n                          \"*duš- ایرانی باستان «بد») + «پیه»، از همان گونهٔ «دژخیم» و «دژآگاه»، و برهان گونه‌های «دشپل/دشپیل» \"\n                          \"را نیز آورده است. بنابراین پیکان باید از «پیه»ی فارسی (گرهٔ ۳) بیرون بیاید نه از *duš-piθwa- اوستایی \"\n                          \"که هیچ گواهی ندارد (بارتولومه تنها tarō.piθwa- «کم‌خوراک» را ثبت کرده است). ریشه درست است، ولی مسیر \"\n                          \"یک پله زودتر رسم شده.\"),\n        \"sources\": [S[\"ab_dozpih\"], S[\"pih\"]],\n        \"ref_check\": [\n          {\"ref\": \"BQT:852\", \"status\": \"supports\",\n           \"note\": \"found in BQT_v2_pages.txt leaf 312 (printed p. c.852-855; leaf 311 opens 'بیان هشتم: در دال بی‌نقطه با زای فارسی مشتمل بر سی و هفت لغت'): 'دژپیه ... گره‌پایی را گویند که در میان گوشت و پوست آدمی و حیوانات دیگر می‌باشد، و معرّب آن غدود است؛ و به فتح اول نیز گفته‌اند.'\"},\n          {\"ref\": \"MON:1523\", \"status\": \"partial\",\n           \"note\": \"Mo'in's entry, read through abadis.ir (فرهنگ معین): '( ~. یِ ) (اِمر.) غده‌های زیرپوستی' — note the tag اِمر = اسم مرکب, i.e. Mo'in analyses it as a Persian COMPOUND, not an inherited word. Page 1523 could not be checked against a paginated copy.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"BQT\", \"where\": \"Borhan v2 leaf 312\", \"stance\": \"supports\", \"note\": \"see the quotation above; the same page also has دژپه as a by-form.\"},\n          {\"src\": \"MON\", \"where\": \"abadis.ir, فرهنگ معین / فرهنگ عمید s.v. دژپیه\", \"stance\": \"partial\",\n           \"note\": \"Mo'in 'غده‌های زیرپوستی'; Amid 'غدهٔ سفت و سختی که زیر پوست بدن پیدا شود، دشپل، دشپیل' — gland, not abscess.\"},\n          {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW\", \"stance\": \"contradicts\",\n           \"note\": \"no duš-piθwa- entry exists; the attested negative compound is 'j. tarō.piθwa- Adj. \\\"der ungenugende Nahrung hat, Mangel an Nahrung leidet\\\"' (V. 13.20).\"},\n          {\"src\": \"PHD\", \"where\": \"MacKenzie 1971\", \"stance\": \"silent\",\n           \"note\": \"no MP *duš-pīh; grep 'dušpīh|dwšpyh' in PHD.txt finds nothing.\"}\n        ]\n      },\n      {\n        \"id\": 5, \"lang\": \"Avestan\", \"words\": \"payah; paěman\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\"Both are genuine Avestan neuters and both are quoted by Pokorny on the very page Nourai cites. Av. payah- n. \"\n                       \"'milk' (Y. 7.77, V. 5.52, N. 57) continues PIE *péyh₂-os ~ *peyh₂-es-os via Proto-Indo-Iranian *páyHas, the \"\n                       \"exact match of Skt. páyas- 'juice, water, milk' — an s-stem (Avestan -ah- < *-as-) to the verb pay- 'to swell, \"\n                       \"be full'. Av. paēman- n. 'mother's milk' (Y. 68.2, Yt. 5) is a men-stem *poyh₂-men- to the same verb, matched \"\n                       \"by Lith. pienas 'milk' and OE fǣmne 'young woman'. Bartholomae (col. 817-818) gives both; his paēman- is \"\n                       \"listed twice, as a neuter 'Muttermilch' and as a feminine adjective 'nursing'.\"),\n        \"derivation_fa\": (\"هر دو واژه اوستایی و خنثی‌اند و پوکورنی در همان صفحهٔ ۷۹۳ که نورایی به آن ارجاع می‌دهد هر دو را آورده \"\n                          \"است. payah- «شیر» (یسنا ۷٫۷۷، وندیداد ۵٫۵۲) بازماندهٔ *péyh₂-os هندواروپایی از راه *páyHas هندوایرانی \"\n                          \"است و برابر دقیق páyas- سنسکریت «شیره، آب، شیر»؛ ستاکی است سین‌دار (-ah- اوستایی از *-as-) بر پایهٔ \"\n                          \"فعل pay- «آماسیدن، پر شدن». paēman- «شیر مادر» نیز ستاکی است با پسوند -men- (*poyh₂-men-) از همان \"\n                          \"فعل، هم‌ریشه با pienas لیتوانیایی «شیر» و fǣmne انگلیسی کهن. بارتولومه (ستون ۸۱۷–۸۱۸) هر دو را ثبت \"\n                          \"کرده است. ادعای نورایی درست است.\"),\n        \"sources\": [S[\"peyh2\"], S[\"payHas\"]],\n        \"ref_check\": [\n          {\"ref\": \"POK:793\", \"status\": \"supports\",\n           \"note\": \"IEW 793: 'ai. páyas- n. \\\"Saft, Wasser, Milch\\\", av. payah- n. \\\"Milch\\\", av. paēman- n. \\\"Muttermilch\\\" (: ags. fǣmne)' — the node is copied straight out of this line.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW cols. 817-818\", \"stance\": \"supports\",\n           \"note\": \"'j. payah- n. \\\"Milch\\\", auch Plur.' (with Y. 7.77, N. 57) and 'j. paēman- n. \\\"Muttermilch\\\": ... daitīm raθwīm paēma ava.daraiti Y. 68.2'; also aspya-payah- 'Pferdemilch' and frā.uruzda-payah-.\"},\n          {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. pēm\", \"stance\": \"supports\",\n           \"note\": \"'pēm [pym] milk 423.13.25, 431, 533, 543.11. — Av. (817) paēman-; Paz. pīm' — Nyberg cites Bartholomae col. 817, confirming the column.\"},\n          {\"src\": \"WLD\", \"where\": \"WP II 74\", \"stance\": \"supports\",\n           \"note\": \"'ags. fǣmne \\\"Jungfrau, junge Frau\\\", as. femea \\\"schwangere Frau\\\", aisl. feima \\\"Madchen\\\" (: av. paēman- \\\"Muttermilch\\\", J. Schmidt Krit. 104 f.)'.\"}\n        ]\n      },\n      {\n        \"id\": 6, \"lang\": \"Persian\", \"words\": \"pînŭ; panîr\",\n        \"verdict\": \"plausible\",\n        \"derivation\": (\"پینو pīnū 'dried sour whey, kashk, qara-qurut' is confirmed in the strongest possible way: Pokorny prints \"\n                       \"'np. pīnū \\\"saure Milch, frischer Kase\\\" (: lit. pienas \\\"Milch\\\")' in the *pei(ə)- entry itself; it is a \"\n                       \"derivative in -nu- of the same *poyh₂-n- 'milk' stem as Av. paēman- and Lith. pienas. Mo'in glosses it 'کشک، \"\n                       \"قره‌قروت' and cites the identical Naser-Khosrow line that Nourai quotes. پنیر panīr 'cheese' is a different \"\n                       \"matter: it continues MP panīr (MacKenzie p.65 'panir [pnyl | N ~] cheese'), and the connection to *payah-/\"\n                       \"*payHa- is probable but not demonstrated — Wiktionary derives NP panīr from MP panīr and stops there, and \"\n                       \"Aryanpur, listing panīr in this root's entry, hedges it as 'به احتمال زیاد ... نیز از همین ریشه است' \"\n                       \"('very probably also from this root'). Formally one has to assume *pay-nīra-/*panīra- with the same -n- \"\n                       \"extension. Hence: pīnū confirmed, panīr probable — node verdict plausible.\"),\n        \"derivation_fa\": (\"«پینو» به استوارترین شکل تأیید می‌شود: پوکورنی در همان مدخل *pei(ə)- می‌نویسد «np. pīnū \\\"شیر ترش، \"\n                          \"پنیر تازه\\\" (: lit. pienas \\\"شیر\\\")»؛ این واژه مشتقی است با -nu- از همان ستاک *poyh₂-n- «شیر» که \"\n                          \"paēman- اوستایی و pienas لیتوانیایی نیز از آن‌اند. معین آن را «کشک، قره‌قروت» معنی کرده و همان بیت \"\n                          \"ناصرخسرو را شاهد آورده که نورایی نقل کرده است. اما «پنیر» حکایت دیگری دارد: دنبالهٔ panīr فارسی \"\n                          \"میانه است (مکنزی ص ۶۵) و پیوند آن با *payah-/*payHa- محتمل است ولی اثبات نشده؛ ویکی‌واژه تنها تا \"\n                          \"فارسی میانه پیش می‌رود و آریان‌پور نیز آن را با قید احتیاط «به احتمال زیاد ... از همین ریشه» \"\n                          \"می‌آورد. از دید ساختواژی باید *pay-nīra-/*panīra- با همان افزودهٔ -n- را فرض کرد. پس: «پینو» \"\n                          \"قطعی و «پنیر» محتمل — داوری این گره «با احتیاط پذیرفتنی».\"),\n        \"sources\": [S[\"ab_pinu\"], S[\"panir\"], S[\"peyh2\"]],\n        \"ref_check\": [\n          {\"ref\": \"MON:969\", \"status\": \"supports\",\n           \"note\": \"Mo'in's پینو entry, read via abadis.ir: '(پِ) (اِ.) کشک، قره قروت' with the Naser-Khosrow line 'نیکی بگزین و بد بنادان ده / روغن بخر و جدا کن از پینو' — the very verse the chart quotes. The page number 969 is independently corroborated: Aryanpur's پینو entry cites 'فرهنگ معین: ۹۶۹'.\"},\n          {\"ref\": \"BQT:449\", \"status\": \"supports\",\n           \"note\": \"found at BQT_v1_pages.txt leaf 675 (printed c. p.447-455), the پینو/پیه stretch: 'پینو، با واو بر وزن گیسو ...' with a کشک/قروت definition; Aryanpur's پینو entry cites 'برهان قاطع ۳۴۹/۴۴۹' for the same word.\"},\n          {\"ref\": \"SNS:141\", \"status\": \"not_found\",\n           \"note\": \"greps of SNS.txt / SNS_pages.txt for panir, pēm, pīh return nothing relevant (only 'pihan/pihn 123/18' and 'spihr'); the Shayast ne Shayast glossary page 141 could not be located because its page offset is undetermined.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"POK\", \"where\": \"IEW 793\", \"stance\": \"supports\",\n           \"note\": \"'np. pīnū \\\"saure Milch, frischer Kase\\\" (: lit. pienas \\\"Milch\\\")' — Pokorny names the Persian word itself.\"},\n          {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.65\", \"stance\": \"supports\",\n           \"note\": \"'panir [pnyl | N ~] cheese' — the Middle Persian antecedent of پنیر.\"},\n          {\"src\": \"ARY\", \"where\": \"Aryanpur, s.v. پینو/پینوک (ARY_pages.txt leaf 183, pdf p.184)\", \"stance\": \"supports\",\n           \"note\": \"the entry gives Avestan pay-, Sanskrit pipyuṣī, Lithuanian 'milk' etc. and adds the footnote 'به احتمال زیاد واژهٔ \\\"پنیر\\\" (پهلوی panīr، کردی penîr) نیز از همین ریشه است', citing برهان قاطع and فرهنگ معین ۹۶۹.\"},\n          {\"src\": \"SYN\", \"where\": \"Buck 5.83 CHEESE\", \"stance\": \"silent\",\n           \"note\": \"Buck's cheese article has no Persian panīr and derives no Iranian word here.\"}\n        ]\n      },\n      {\n        \"id\": 7, \"lang\": \"Avestan\", \"words\": \"angu-paěna\",\n        \"verdict\": \"plausible\",\n        \"derivation\": (\"The second element is real: Bartholomae (col. 817) has 'j. paēnaēna- Adj. \\\"aus Honig bestehend, bereitet\\\"' \"\n                       \"(N. 57) and derives it from an 'Ableit. aus *paēna- m. \\\"Honig\\\"', adding 'mp. angu-βīn, np. angubīn \"\n                       \"\\\"Bienenhonig\\\"'. But *paēna- itself is starred, and the COMPOUND angu-paēna- is not an Avestan word: it is \"\n                       \"the Proto-Iranian preform *angu-paina- that Gharib reconstructs for Sogdian 'nkwpyn angupēn 'honey' (entry \"\n                       \"1066, printed p.42 — Nourai's SOD:42, where Gharib writes '<*angupaina-; Av. paēna'). Nourai has copied \"\n                       \"Gharib's reconstruction and labelled it 'Avestan'. Note also that Bartholomae is expressly sceptical about \"\n                       \"attaching *paēna- to this root: 'Ob zu lit. pienas \\\"Milch\\\"? ... Die Bedeutung \\\"Milch\\\" ist fur *paēna- \"\n                       \"nicht wahrscheinlich, obwohl sich ja np. angubīn allenfalls als \\\"Bienenmilch\\\" fassen liesse.' Wiktionary \"\n                       \"reconstructs the whole word as Proto-Iranian *Hangubáynah and relates it not to 'milk' but to angom 'resin'. \"\n                       \"So: the etymon is defensible, the language label and the root affiliation are not secure.\"),\n        \"derivation_fa\": (\"جزء دوم واقعی است: بارتولومه (ستون ۸۱۷) صفتِ اوستایی paēnaēna- «از عسل، عسلی» را ثبت کرده و آن را \"\n                          \"مشتق از *paēna- m. «عسل» می‌داند و می‌افزاید «فارسی میانه angu-βīn، فارسی نو angubīn \\\"عسل زنبور\\\"». \"\n                          \"اما خودِ *paēna- بازسازی‌شده (ستاره‌دار) است و ترکیب angu-paēna- هیچ‌گاه در اوستا نیامده: این صورت، \"\n                          \"بازسازیِ ایرانی آغازینِ *angu-paina- است که قریب برای واژهٔ سغدی 'nkwpyn (angupēn «عسل»، مدخل ۱۰۶۶، \"\n                          \"ص ۴۲ — همان SOD:42 نورایی) پیشنهاد کرده و همان‌جا نوشته است «<*angupaina-; Av. paēna». نورایی این \"\n                          \"بازسازی را برداشته و برچسب «اوستایی» بر آن زده است. افزون بر این، بارتولومه در پیوند *paēna- با \"\n                          \"همین ریشه به‌صراحت تردید می‌کند و معنای «شیر» را برای آن نامحتمل می‌داند؛ ویکی‌واژه نیز کل واژه را \"\n                          \"*Hangubáynah ایرانی آغازین بازسازی می‌کند و آن را نه با «شیر» بلکه با «انگم» (صمغ) مربوط می‌داند. \"\n                          \"پس ریشه‌یابی دفاع‌پذیر است اما برچسب زبانی و انتساب به این ریشه استوار نیست.\"),\n        \"sources\": [S[\"angabin\"]],\n        \"ref_check\": [\n          {\"ref\": \"SOD:42\", \"status\": \"supports\",\n           \"note\": \"Gharib, Sogdian Dictionary printed p.42 (SOD_pages.txt leaf 107), entry 1066: \\\"'nkwpyn B, S — angupēn ('ngwpyn) <*angupaina-; Av. paēna — honey — TSP 19.7, 16 n p232; BSTBL, Padm. 40; KG 368\\\". Exactly Nourai's *angu-paēna, though as a Proto-Iranian reconstruction, not an Avestan attestation.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 817 s.v. paēnaēna-\", \"stance\": \"partial\",\n           \"note\": \"'j. paēnaēna- Adj. (fem. -nī-) \\\"aus Honig bestehend, bereitet\\\" ... Ableit. aus *paēna- m. \\\"Honig\\\"; mp. angu-βīn, np. angubīn \\\"Bienenhonig\\\". — Ob zu lit. pienas \\\"Milch\\\"? ... Die Bedeutung \\\"Milch\\\" ist fur *paēna- nicht wahrscheinlich.'\"},\n          {\"src\": \"POK\", \"where\": \"IEW 793\", \"stance\": \"silent\",\n           \"note\": \"Pokorny's *pei(ə)- entry does not mention angubīn or *paēna- at all.\"},\n          {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.11\", \"stance\": \"partial\",\n           \"note\": \"'angubēn [DWBSYA < A dbš; 'ngpyn' | N angubin] honey' — the Middle Persian form, but MacKenzie gives no Avestan etymon.\"}\n        ]\n      },\n      {\n        \"id\": 8, \"lang\": \"Pahlavi\", \"words\": \"angubin\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\"MacKenzie p.11: 'angubēn [DWBSYA < A dbš; ʾngpyn' | N angubin] honey' — the Book-Pahlavi spelling ʾngpyn \"\n                       \"is *angu-pēn, with the Aramaic heterogram DWBŠYA (Semitic dbš 'honey') beside it; the compound also survives \"\n                       \"in the standing phrase magas ī angubēn 'honey-bee'. The form goes back to *angu-paina- with the regular \"\n                       \"lenition of intervocalic -p- to -b- in Middle Persian and the monophthongisation of *ai to ē (*angupaina- > \"\n                       \"angubēn); the first element angu- is the same as in angom 'resin, gum'. Nourai spells the node 'angubin', \"\n                       \"which is really the New Persian reading of the Pahlavi spelling, but the form is right.\"),\n        \"derivation_fa\": (\"مکنزی (ص ۱۱): «angubēn [هزوارش DWBSYA از dbš سامی؛ املای پهلوی 'ngpyn؛ فارسی نو angubin] عسل»؛ همین \"\n                          \"ترکیب در عبارتِ ثابتِ magas ī angubēn «زنبور عسل» نیز به‌کار رفته است. این صورت از *angu-paina- \"\n                          \"بازمی‌گردد: «پ» میان‌واکه‌ای در فارسی میانه به «ب» نرم شده و دوواکهٔ *ai به ē تک‌واکه شده است \"\n                          \"(*angupaina- > angubēn)؛ جزء نخست همان angu- در «انگم» (صمغ) است. نورایی صورت را «angubin» نوشته که \"\n                          \"در واقع خوانش فارسی نوِ املای پهلوی است، ولی صورت درست است.\"),\n        \"sources\": [S[\"angabin\"]],\n        \"ref_check\": [\n          {\"ref\": \"BQT:174\", \"status\": \"partial\",\n           \"note\": \"Borhan-e Qate' printed p.174 = BQT_v1_pages.txt leaf 392 (identified by the footnote 'بقیه از صفحهٔ ۱۷۳' at the foot of that leaf): the headword انگبین is there, glossed 'عسل و شهد را گویند'. Mo'in's etymological footnote on that page is too degraded in the OCR to read, and the page is outside the scan range served by tools/ref_page.py ('no scan of BQT covers printed page 174'), so the Pahlavi form itself could not be read off Borhan; MacKenzie supplies it instead.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.11 (and p.23, magas ī angubēn)\", \"stance\": \"supports\",\n           \"note\": \"'angubēn [DWBSYA < A dbš; \\\\'ngpyn\\\\' | N angubin] honey'; 'magas i angubēn: honey-bee'; also 'afrōšag ... a sweetmeat made of flour, butter, and honey'.\"},\n          {\"src\": \"BRT\", \"where\": \"AiW col. 817\", \"stance\": \"supports\",\n           \"note\": \"'mp. angu-βīn, np. angubīn \\\"Bienenhonig\\\"' — Bartholomae himself names the Middle Persian form.\"},\n          {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II\", \"stance\": \"silent\",\n           \"note\": \"grep 'angub' in NYB_vol2_glossary.txt finds no entry.\"}\n        ]\n      },\n      {\n        \"id\": 9, \"lang\": \"Persian\", \"words\": \"angabîn\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\"NP انگبین angabīn/angubīn 'honey' continues MP angubēn directly, with the classical -ē- read as -ī- in New \"\n                       \"Persian (majhūl ē > ma'rūf ī) and the first-syllable vowel varying between -gu- and -ga-. It is well attested \"\n                       \"in classical verse (the chart's Attar line) and survives above all in the compounds the chart adds as extra \"\n                       \"script: سکنجبین sekanjabīn (< سرکه serke 'vinegar' + انگبین, the oxymel of the medical tradition, Arabicised \"\n                       \"as سكنجبين) and گزانگبین gaz-angabīn 'tamarisk manna', beside ترانگبین tar-angabīn 'Persian manna'. In modern \"\n                       \"Persian the plain word is archaic, عسل having replaced it.\"),\n        \"derivation_fa\": (\"«انگبین» در فارسی نو دنبالهٔ مستقیم angubēn فارسی میانه است؛ «ی» مجهولِ پهلوی در فارسی نو به «ی» \"\n                          \"معروف بدل شده و واکهٔ هجای نخست میان -gu- و -ga- نوسان دارد. این واژه در شعر کلاسیک فراوان به کار \"\n                          \"رفته (از جمله بیت عطار که در نمودار آمده) و بیش از همه در ترکیب‌هایی که نمودار افزوده زنده مانده \"\n                          \"است: «سکنجبین» (از «سرکه» + «انگبین»، همان oxymel طب سنتی که به عربی سكنجبين معرّب شده) و \"\n                          \"«گزانگبین» (شیرابهٔ درخت گز)، و نیز «ترانگبین». در فارسی امروز خودِ واژه کهنه شده و جای آن را «عسل» \"\n                          \"گرفته است. ادعای نورایی درست است.\"),\n        \"sources\": [S[\"angabin\"]],\n        \"ref_check\": [\n          {\"ref\": \"BQT:174\", \"status\": \"supports\",\n           \"note\": \"Borhan p.174 (BQT_v1_pages.txt leaf 392): 'انگبین، با بای ابجد بر وزن عنبرین، عسل و شهد را گویند' — honey; the same page has انگبینه, a honey sweetmeat.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"BQT\", \"where\": \"Borhan v1 leaf 392 (printed 174)\", \"stance\": \"supports\", \"note\": \"see quotation above.\"},\n          {\"src\": \"MON\", \"where\": \"Wiktionary's Persian entry, citing the classical usage\", \"stance\": \"supports\",\n           \"note\": \"'From Middle Persian (DWBŠYA, ʾngpyn' /angubēn/, \\\"honey\\\"), from Proto-Iranian *Hangubáynah ... Derived terms: ترانگبین, سرکنگبین, مگس انگبین, گزانگبین' — the last two are precisely the chart's extra forms.\"},\n          {\"src\": \"HRN\", \"where\": \"Horn, Grundriss\", \"stance\": \"silent\",\n           \"note\": \"grep 'angubin|angubîn' in HRN.txt gives no numbered entry for this word.\"}\n        ]\n      },\n      {\n        \"id\": 10, \"lang\": \"Sogdian\", \"words\": \"`pt; `pt-xw`r; brpyğ\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\"All three are in Gharib exactly where Nourai says. SOD:53 (printed p.53, entry 1355) has \\\"ʾpt- B, M — \"\n                       \"op(a)t, (a)pat ? © Av. pitu — meat\\\", and entry 1358 \\\"ʾptywʾr B — opat-xwar — carnivorous, flesh-eater\\\", \"\n                       \"i.e. pat + xwar- 'to eat' — Nourai's `pt-xw`r. SOD:109 (printed p.109, entry 2770) has \\\"prpyγ S — farpix ? \"\n                       \"© Av. pīvah, Pahl. farbih — fat\\\": Nourai renders the initial as b- because Sogdian p- is here the fricative \"\n                       \"β-, so βarpēγ. Semantically Sogdian ʾpt shows the same 'nourishment' > 'meat' shift as Avestan pitu- 'esp. \"\n                       \"meat dish'; βrpyγ is the Sogdian counterpart of MP frabīh (node 2), a *fra- compound, so strictly it hangs \"\n                       \"under the Avestan branch rather than directly under the root.\"),\n        \"derivation_fa\": (\"هر سه صورت دقیقاً در همان جایی است که نورایی گفته. قریب در ص ۵۳ (مدخل ۱۳۵۵) می‌آورد: «ʾpt- در متون \"\n                          \"بودایی و مانوی، خوانش op(a)t/(a)pat؟، هم‌سنجِ pitu اوستایی، به معنی گوشت» و در مدخل ۱۳۵۸ «ʾptywʾr \"\n                          \"— opat-xwar — گوشت‌خوار» که همان `pt-xw`r نورایی است (pat + xwar- «خوردن»). در ص ۱۰۹ (مدخل ۲۷۷۰) نیز \"\n                          \"«prpyγ — farpix؟ — هم‌سنجِ pīvah اوستایی و farbih پهلوی — چاق» آمده است؛ نورایی حرف نخست را b نوشته \"\n                          \"چون «پ» در این املا همان سایشی β است، یعنی βarpēγ. از دید معنایی، ʾpt سغدی همان تحول «خوراک ← گوشت» \"\n                          \"را نشان می‌دهد که در pitu- اوستایی («به‌ویژه خوراک گوشتی») دیده می‌شود، و βrpyγ برابر سغدیِ frabīh \"\n                          \"فارسی میانه است، یعنی ترکیبی با *fra-؛ پس به‌دقت باید زیرِ شاخهٔ اوستایی بنشیند نه مستقیماً زیر ریشه.\"),\n        \"sources\": [S[\"peyh2\"]],\n        \"ref_check\": [\n          {\"ref\": \"SOD:53\", \"status\": \"supports\",\n           \"note\": \"SOD_pages.txt leaf 118 (printed p.53): '1355 ʾpt- B, M | op(a)t, (a)pat ? ©Av. pitu ^ptywʾr | meat | GMS 170' and '1358 ʾptywʾr B | opat-xwar | carnivorous, flesh-eater'.\"},\n          {\"ref\": \"SOD:109\", \"status\": \"supports\",\n           \"note\": \"SOD_pages.txt leaf 174 (printed p.109): '2770 prpyγ S | farpix ? ©Av. pivah Pahl. farbih | fat | MDii p32 n 20'.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"SOD\", \"where\": \"Gharib, entries 1355, 1358, 2770\", \"stance\": \"supports\", \"note\": \"quotations above; Gharib himself links ʾpt to Av. pitu and prpyγ to Av. pīvah / Pahl. farbih.\"},\n          {\"src\": \"BRT\", \"where\": \"AiW s.v. pitav-, pīvah-\", \"stance\": \"supports\",\n           \"note\": \"'j. pitav- m. \\\"Speise\\\", insbes. feste, \\\"Fleischspeise\\\"' — the 'meat' sense that Sogdian generalised is already Avestan.\"},\n          {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.32\", \"stance\": \"supports\",\n           \"note\": \"'frabih [plpyh | (P frbyw), N farbih] fat, stout' — the Middle Persian match of Sogdian βrpyγ.\"}\n        ]\n      },\n      {\n        \"id\": 11, \"lang\": \"Germanic\", \"words\": \"faitaz\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\"Proto-Germanic *faitaz 'fat, plump' is the standard reconstruction and is put under this root by everyone: \"\n                       \"Watkins 'Extended o-grade form *poid- in Germanic *faitaz, plump, fat', Pokorny p.794 under the extension \"\n                       \"poi-d-/pi-d- ('germ. *faitian \\\"masten\\\" (ahd. feizen, ags. fǣtan, aisl. feita), *faita- \\\"fett\\\" (ahd. feiz, \"\n                       \"aisl. feitr)'), Wiktionary '*poyh₂d-o-s > Proto-Germanic *faitaz'. PIE *poyd-o- gives Gmc *faitaz by Grimm's \"\n                       \"law (*p > f, *d > t) with the o-grade diphthong *oi > Gmc ai. Descendants: ON feitr, OHG feiz, MDu. vet.\"),\n        \"derivation_fa\": (\"*faitaz ژرمنی آغازین «چاق، فربه» بازسازیِ استاندارد است و همهٔ مراجع آن را زیر همین ریشه می‌نهند: \"\n                          \"واتکینز «صورت گستردهٔ درجهٔ o یعنی *poid- در ژرمنی *faitaz»، پوکورنی در ص ۷۹۴ زیر گسترش poi-d-/pi-d- \"\n                          \"(«ژرمنی *faitian \\\"پروار کردن\\\"، *faita- \\\"چاق\\\"»)، و ویکی‌واژه «*poyh₂d-o-s ← *faitaz ژرمنی آغازین». \"\n                          \"از دید آوایی *poyd-o- هندواروپایی بر پایهٔ قانون گریم به *faitaz ژرمنی می‌رسد (*p > f و *d > t) و \"\n                          \"دوواکهٔ *oi به ai ژرمنی بدل می‌شود. بازماندگان: feitr نورسی کهن، feiz آلمانی علیای کهن، vet هلندی \"\n                          \"میانه. ادعای نورایی درست است.\"),\n        \"sources\": [S[\"peyh2\"], S[\"fat\"]],\n        \"ref_check\": [\n          {\"ref\": \"AHD\", \"status\": \"supports\",\n           \"note\": \"Watkins 1985 s.v. peiə-: '1. Extended o-grade form *poid- in Germanic *faitaz, plump, fat, in derivative Germanic verb *faitjan, to fatten, whence Germanic past participle *faitidaz, fattened, in Old English fǣt(t), fat: FAT.'\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"POK\", \"where\": \"IEW 794 (POK_03 leaf 27)\", \"stance\": \"supports\",\n           \"note\": \"'Erweiterung poi-d-, pi-d- ... germ. *faitian \\\"masten\\\" (ahd. feizen, ags. fǣtan, aisl. feita), *faita- \\\"fett\\\" (ahd. feiz, aisl. feitr), Partiz. germ. *faitida-: ahd. feizzit, mhd. veiz(e)t, nhd. feist, ags. fǣted, engl. fat, mnd. vet \\\"fett\\\".'\"},\n          {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. fat, adj.\", \"stance\": \"supports\",\n           \"note\": \"'These adjectives are prop. pps. of Teut. *faitian, \\\"to feed, fatten\\\" ... fr. I.-E. base *poid-, *pīd-, \\\"to abound in water, milk, fat, etc.\\\" ... Base *poid-, *pīd-, is a -d-enlargement of base *poi-, *pī-, \\\"sap, juice\\\".'\"},\n          {\"src\": \"WLD\", \"where\": \"WP II 75\", \"stance\": \"supports\",\n           \"note\": \"'aisl. fita f. \\\"Fett\\\", fitna \\\"fett werden\\\" ... mhd. veiz \\\"fett\\\", ahd. feizzen \\\"nahren\\\", Ptc. ahd. feizzit, mhd. veizt, nhd. feist'.\"}\n        ]\n      },\n      {\n        \"id\": 12, \"lang\": \"English\", \"words\": \"fat\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\"English fat continues Old English fǣtt 'fatted, fat', originally the past participle of the weak verb \"\n                       \"fǣtan 'to fatten' (Proto-West-Germanic *faitid, from *faitijan, denominative of *fait < PGmc *faitaz). \"\n                       \"The ME form fatt gives NE fat; the participial origin explains the geminate -tt-. Klein: 'ME. fatt, fat, \"\n                       \"fr. OE. fǣtt, contraction of fǣtted, pp. of fǣttian, \\\"to fatten\\\"'. The chart leaves the gloss blank; \"\n                       \"the arrow Germanic -> English is standard.\"),\n        \"derivation_fa\": (\"واژهٔ انگلیسی fat دنبالهٔ fǣtt انگلیسی کهن «پروارشده، چاق» است که در اصل صفت مفعولی فعل ضعیف fǣtan \"\n                          \"«پروار کردن» بوده (ژرمنی غربی آغازین *faitid از *faitijan، فعل ساخته‌شده از نامِ *fait < *faitaz \"\n                          \"ژرمنی آغازین). صورت انگلیسی میانهٔ fatt به fat امروزی رسیده و همین خاستگاه وصفی، دوتایی شدن -tt- را \"\n                          \"توضیح می‌دهد. کلاین می‌نویسد: «ME fatt, fat، از OE fǣtt، کوتاه‌شدهٔ fǣtted، صفت مفعولی fǣttian \"\n                          \"\\\"پروار کردن\\\"». این حلقه (ژرمنی ← انگلیسی) استاندارد است.\"),\n        \"sources\": [S[\"fat\"], S[\"peyh2\"]],\n        \"ref_check\": [\n          {\"ref\": \"None\", \"status\": \"not_checked\",\n           \"note\": \"the chart gives no reference for this node; the parent node's AHD citation covers the chain ('...in Old English fǣt(t), fat: FAT').\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. fat, adj. (line 14432)\", \"stance\": \"supports\",\n           \"note\": \"'fat, adj. — ME. fatt, fat, fr. OE. fǣtt, contraction of fǣtted, pp. of fǣttian, \\\"to fatten\\\", rel. to ON. feitr, OFris. fatt, fet, MLG., MDu., Du. vet, OHG. feizit, MHG. veiz(e)t, G. feist, \\\"fat\\\".'\"},\n          {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. peiə-\", \"stance\": \"supports\",\n           \"note\": \"'...whence Germanic past participle *faitidaz, fattened, in Old English fǣt(t), fat: FAT.'\"},\n          {\"src\": \"POK\", \"where\": \"IEW 794\", \"stance\": \"supports\", \"note\": \"'ags. fǣted, engl. fat, mnd. vet \\\"fett\\\"'.\"}\n        ]\n      },\n      {\n        \"id\": 13, \"lang\": \"Latin\", \"words\": \"pinus\",\n        \"verdict\": \"plausible\",\n        \"derivation\": (\"Latin pīnus, -ūs/-ī f. 'pine' is correctly glossed as the resinous tree. Its assignment to this root is the \"\n                       \"traditional one and rests on the 'resin' sense of the *pi-tu- family: Pokorny 794 'die Bedeutung \\\"Harz\\\" auch \"\n                       \"in der k-Ableitung *pi-k-: gr. πίσσα, lat. pix ... aber lat. pinus ... wegen alb. pishë \\\"Fichte\\\" (*pit-s-nu-s)', \"\n                       \"i.e. pīnus < *pit-s-no-s, with loss of the cluster and compensatory lengthening; Klein and Watkins say the same \"\n                       \"(*pi-nu-), comparing Skt. pītu-dāru- 'resin tree' and Gk. pítys. But Wiktionary/de Vaan call the origin disputed \"\n                       \"(Proto-Italic *pīnos, alternatively to be joined with Gk. pínax 'plank'), so the arrow is probable rather than \"\n                       \"secure.\"),\n        \"derivation_fa\": (\"واژهٔ لاتین pīnus «کاج» و معنای «درخت صمغ‌دار» درست است. انتساب آن به این ریشه سنتی است و بر معنای \"\n                          \"«صمغ/رزین» در خانوادهٔ *pi-tu- تکیه دارد: پوکورنی در ص ۷۹۴ می‌نویسد معنای «رزین» در مشتق کافی \"\n                          \"*pi-k- (یونانی πίσσα، لاتین pix «قیر») نیز هست و لاتین pinus را به سبب pishë آلبانیایی «کاج» از \"\n                          \"*pit-s-nu-s می‌داند، یعنی pīnus < *pit-s-no-s با ساده شدن خوشه و کشش جبرانی؛ کلاین و واتکینز نیز \"\n                          \"همین را می‌گویند (*pi-nu-) و pītu-dāru- سنسکریت «درخت صمغ» و pítys یونانی را هم‌سنگ می‌آورند. اما \"\n                          \"ویکی‌واژه به پیروی از دِ ڤان خاستگاه آن را «مورد اختلاف» می‌داند (ایتالیایی آغازین *pīnos، و شاید \"\n                          \"هم‌ریشه با pínax یونانی «تخته»). پس این پیکان محتمل است نه قطعی.\"),\n        \"sources\": [S[\"pinus\"], S[\"peyh2\"]],\n        \"ref_check\": [\n          {\"ref\": \"AHD\", \"status\": \"supports\",\n           \"note\": \"Watkins 1985 s.v. peiə-: '3. Possibly suffixed zero-grade form *pi-nu- in Latin pinus, pine tree (yielding a resin): PINE, PINEAL, PINON, PINNACE; PINA CLOTH.' Note Watkins' own 'Possibly'.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"POK\", \"where\": \"IEW 794\", \"stance\": \"supports\",\n           \"note\": \"'aber lat. pinus, -ūs und -ī \\\"Fichte, Fohre, Kiefer\\\" wegen alb. pishë \\\"Fichte, Kienfackel\\\" (*pit-s-(n)a) wohl aus *pit-s-nu-s'.\"},\n          {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. pinus\", \"stance\": \"partial\",\n           \"note\": \"'On rapproche skr. pītu-dāru qui designe une sorte de \\\"pin\\\", c.-a-d. un arbre resineux: le premier terme semble se retrouver dans le derive lat. pituita et dans gr. πίτυς \\\"pin\\\" ... La formation en -nu- de pinus rappelle celle de πίτυς.' — same comparison, no certainty.\"},\n          {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. pine, n.\", \"stance\": \"supports\",\n           \"note\": \"'fr. L. pinus, \\\"pine\\\", which is cogn. with OI. pītuḥ, \\\"juice, sap, resin, food\\\", pītu-dāruḥ, \\\"a kind of pine\\\", lit. \\\"resiniferous tree\\\" ... These words are traceable to I.-E. base pī-, \\\"sap, juice\\\" ... See fat.'\"},\n          {\"src\": \"IEC\", \"where\": \"Mann, s.v. pit- (3) 'pine'\", \"stance\": \"supports\",\n           \"note\": \"'pit- (pitus, piteu-) (3) \\\"pine\\\". Pamiri (alleged) pit, id.; Gk. pítus, f. id. ... Cf. Skt. pitu-daru. See pit- (2).'\"}\n        ]\n      },\n      {\n        \"id\": 14, \"lang\": \"English\", \"words\": \"pine\",\n        \"verdict\": \"confirmed\",\n        \"derivation\": (\"English pine (the tree) is an early borrowing of Latin pīnus: Old English pīn, reinforced in Middle English \"\n                       \"by Old French pin; the modern spelling with -e reflects the ME long vowel that later diphthongised in the \"\n                       \"Great Vowel Shift. It is unrelated to the verb pine 'to languish' (< L. poena). The chart's arrow Latin -> \"\n                       \"English is uncontroversial; the node carries no reference and needs none.\"),\n        \"derivation_fa\": (\"واژهٔ انگلیسی pine «کاج» وام‌واژه‌ای کهن از لاتین pīnus است: pīn در انگلیسی کهن، که در انگلیسی میانه \"\n                          \"با pin فرانسهٔ کهن تقویت شده است؛ املای امروزی با -e پایانی بازتاب واکهٔ بلند انگلیسی میانه است که \"\n                          \"بعدها در «جابه‌جایی بزرگ واکه‌ها» دوواکه شده است. این واژه با فعل pine «پژمردن» (از poena لاتین) \"\n                          \"هیچ پیوندی ندارد. حلقهٔ «لاتین ← انگلیسی» بی‌مناقشه است.\"),\n        \"sources\": [S[\"pinus\"]],\n        \"ref_check\": [\n          {\"ref\": \"None\", \"status\": \"not_checked\",\n           \"note\": \"no reference is printed for this node; the parent's AHD citation ('Latin pinus ... : PINE') covers it.\"}\n        ],\n        \"consulted\": [\n          {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. pine, n. (line 28856)\", \"stance\": \"supports\",\n           \"note\": \"'pine, n., a tree of the genus Pinus (bot.) — ME., fr. OE. pin, (in ME. fr. F. pin), fr. L. pinus, \\\"pine\\\".'\"},\n          {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. peiə-\", \"stance\": \"supports\", \"note\": \"'Latin pinus, pine tree ... : PINE'.\"}\n        ]\n      }\n    ]\n   }\n  ]\n}\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-385.json\"\nwith open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"wrote\", out, os.path.getsize(out))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk385.py"
}
```


### [2026-09-07T21:03:45.281Z] TOOL RESULT

```
wrote /home/sfmqrb/git/rishe/data/verification/page-385.json 78622
```


## [2026-09-07T21:03:48.704Z] TOOL CALL #77: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-385.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 385"
}
```


### [2026-09-07T21:03:50.244Z] TOOL RESULT

```
JSON OK
nodes verified: 20/20
node verdicts: {'plausible': 7, 'transcription_suspect': 1, 'confirmed': 12}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'partial': 7, 'supports': 17, 'not_checked': 4, 'not_found': 1}
books consulted: {'partial': 10, 'supports': 38, 'silent': 12, 'contradicts': 1} | by book: {'POK': 7, 'KLN': 7, 'BRT': 6, 'PHD': 6, 'WLD': 3, 'MON': 3, 'ARY': 3, 'BQT': 3, 'NYB': 3, 'HRN': 3, 'HJB': 2, 'LKT': 2, 'SKT': 2, 'LAT': 2, 'HUB': 2, 'AHD': 2, 'AID': 1, 'KNT': 1, 'SYN': 1, 'SOD': 1, 'IEC': 1}
```


## [2026-09-07T21:04:12.783Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-385.json` written; `verify_check.py 385` reports 20/20 nodes, 0 PROBLEM lines.

**Page 385 (book p. 355), 2 entries, 20 nodes**
- Root verdicts: 1 confirmed (Peî), 1 plausible (Peg)
- Node verdicts: 12 confirmed, 7 plausible, 1 transcription_suspect
- Ref checks: 17 supports, 7 partial, 1 not_found, 4 not_checked

**transcription_suspect**
- Peg, #2 Hindustani `pankâ` — the word is Hindi/Urdu **paṅkhā** (पंखा) with aspirated -kh-; Klein (whom Nourai cites, p.1272), Hobson-Jobson p.742 and Lokotsch no. 1622 all spell it *pankha*. The printed page really does read "pankâ", so `error_in: book` — the extraction is faithful. Page image saved to `data/verification/sources/refs/ocr/BOOK/385.png`.

**Notable plausible/qualified findings (no `disputed`)**
- Root *Peg* "breast": Pokorny 792 actually glosses it "armpit, hip, loin, side"; "breast" is copied from Watkins/AHD and rests only on Lat. *pectus* + Toch. B *pāścane*. Wiktionary/de Vaan doubt the *pectus* ↔ Skt *pakṣa-* equation. Skt *pakṣa* means 'wing, side, half', never 'breast'.
- Peî #1: Av. *fra-piθwa-* is attested but means 'copious, abundant' (Bartholomae col. 984), not 'fat'; **Av. *duš-piθwa- is not attested at all** (only *tarō.piθwa-* 'ill-fed'). دژپیه is a New Persian compound دژ + پیه (Mo'in tags it اسم مرکب), and its sense is 'subcutaneous gland/nodule' (Borhan: معرّب آن غدود), not 'abscess'.
- Peî #7: *angu-paēna* is labelled Avestan but is Gharib's Proto-Iranian reconstruction *\*angu-paina-* for Sogdian *angupēn* (SOD p.42, entry 1066); Bartholomae (col. 817) has only *paēnaēna-* and expressly doubts the link to the 'milk/fat' root.
- Peî #6: پینو is confirmed verbatim by Pokorny 793 ("np. pīnū"); پنیر's attachment is only probable (Aryanpur: "به احتمال زیاد").
- Peî #13 Lat. *pinus*: traditional (Pokorny/Watkins/Klein) but de Vaan/Wiktionary call the origin disputed.

**Citation issues for the owner (not extraction errors)**
- `MON:844` (Peî #3, پیه/فربه) is almost certainly a slip: Nourai's own `MON:824` for پنکه and `MON:969` for پینو (the latter independently corroborated by Aryanpur) put پیه at ≈ p. 970+, not 844.
- `SNS:141` could not be located (Shayast ne Shayast glossary has no page offset and no panīr/pēm hit).
- `AHD:1060` and `FWE:233` are not accessible online (lending-only).
- Confirmed-correct page hits worth noting: BQT:1450 = the فربه page with Mo'in's *frapīh* footnote; BQT:174 = the انگبین page; BQT:449 ≈ the پینو page; BQT:852 ≈ the دژپیه page; HRN:81/181 = Horn nos. 365/813; SOD:42/53/109 all exact.
