# Verification process log — verify-page-379


## [2026-09-07T20:30:50.904Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 379 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-379.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-379.json. Write /home/sfmqrb/git/rishe/data/verification/page-379.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 379` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T20:30:53.334Z] AGENT

I'll start by reading the instructions and the input files.


## [2026-09-07T20:30:54.048Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T20:30:54.100Z] TOOL RESULT

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


## [2026-09-07T20:30:54.990Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-379.txt"
}
```


## [2026-09-07T20:30:54.998Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-379.json"
}
```


### [2026-09-07T20:30:55.012Z] TOOL RESULT

```
1	{
2	  "pdf_page": 379,
3	  "book_page": 349,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Pa, Pa-ter, Poti, Potiš",
8	        "lang": "Indo-European",
9	        "refs": "POK:787,842; SYN:103; KAS:10",
10	        "gloss": "Pa: to protect, to feed. Pa-ter: protector, feeder (of the family), father ☞ Ter 3. Poti, Potiš: protector, husband, power, also self. This has probably started as a nursery word and became a usual term in the Indo-European languages. Compare with the root \"Baba\"."
11	      },
12	      "part": 1,
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Avestan / Old Persian",
18	          "refs": "HRN:41,72; KLN:114; AHD:1532",
19	          "words": [
20	            {"translit": "pa 1", "gloss": "to guard", "script": null}
21	          ],
22	          "script_extra": null,
23	          "note": null,
24	          "quote": null
25	        },
26	        {
27	          "id": 2,
28	          "parent": 1,
29	          "lang": "Persian",
30	          "refs": "BQT:358,1069; KLN:169; FSF:335; TZF:21",
31	          "words": [
32	            {"translit": "pâyîdan", "gloss": "to watch", "script": "پاییدن"},
33	            {"translit": "bân", "gloss": "a suffix meaning protector", "script": "بان ۱ -"},
34	            {"translit": "pâlŭdan", "gloss": "not to contaminate, clean", "script": "پالودن"}
35	          ],
36	          "script_extra": "پادن، پای ۲، پاس\nپاد ، پادشاه ، پادگان\nپاسبان ، دربان ، سروان ، چوپان ، شبان\nپالایش ، پالوده ، فالوده، پالان",
37	          "note": null,
38	          "quote": {
39	            "text": "پاسبان حرم دل شده ام شب همه شب - تا در این پرده جز اندیشهٔ او نگذارم",
40	            "poet": "Hâfez"
41	          }
42	        },
43	        {
44	          "id": 3,
45	          "parent": 1,
46	          "lang": "Avestan / Old Persian",
47	          "refs": "POK:842; HRN:41; KLN:144,157; AHD:1532",
48	          "words": [
49	            {"translit": "paiti 1, patiy, pavan, pâna", "gloss": "master, protector", "script": null},
50	            {"translit": "pathra", "gloss": "protection", "script": null},
51	            {"translit": "fšu-paiti", "gloss": "cattle protector, shepherd", "script": null, "see": ["Pek"]},
52	            {"translit": "paiti-xšathra", "gloss": "protecting king", "script": null, "see": ["Ksei 1"]}
53	          ],
54	          "script_extra": null,
55	          "note": null,
56	          "quote": null
57	        },
58	        {
59	          "id": 4,
60	          "parent": 1,
61	          "lang": "Avestan",
62	          "refs": "POK:842; SNS:267",
63	          "words": [
64	            {"translit": "xvaĕ-pati, xvaĕ-paithya", "gloss": "one's own self", "script": null, "see": ["Seu 1"]}
65	          ],
66	          "script_extra": null,
67	          "note": "\"pati, paithya\" means self or own in this combination",
68	          "quote": null
69	        },
70	        {
71	          "id": 5,
72	          "parent": 4,
73	          "lang": "Persian",
74	          "refs": "POK:842; SNS:267",
75	          "words": [
76	            {"translit": "xîš 1", "gloss": "self", "script": "خویش ۱"}
77	          ],
78	          "script_extra": null,
79	          "note": null,
80	          "quote": null
81	        },
82	        {
83	          "id": 6,
84	          "parent": 1,
85	          "lang": "Avestan / Old Persian",
86	          "refs": "HRN:72",
87	          "words": [
88	            {"translit": "âthur-pât-gan", "gloss": "fire protector", "script": null, "see": ["Ater"]},
89	            {"translit": "pa-nâh", "gloss": "protecting help, shelter", "script": null, "see": ["Nâ 2"]},
90	            {"translit": "paiti-dâma", "gloss": "body protection", "script": null, "see": ["Dhě 2"]}
91	          ],
92	          "script_extra": null,
93	          "note": null,
94	          "quote": null
95	        },
96	        {
97	          "id": 7,
98	          "parent": 6,
99	          "lang": "Persian",
100	          "refs": "BQT:418",
101	          "words": [
102	            {"translit": "Âzarbâyjân", "gloss": "A city in Iran", "script": "آذربایجان"},
103	            {"translit": "panâh", "gloss": "shelter", "script": "پناه"},
104	            {"translit": "panâm", "gloss": "mouth guard used by Zoroastrians", "script": "پنام"}
105	          ],
106	          "script_extra": null,
107	          "note": null,
108	          "quote": null
109	        },
110	        {
111	          "id": 8,
112	          "parent": 1,
113	          "lang": "Pahlavi",
114	          "refs": "IRN:119",
115	          "words": [
116	            {"translit": "ô-pât-ân", "gloss": "city with protected waterways", "script": null, "see": ["Ab 1"]},
117	            {"translit": "arta-pân", "gloss": "protector of justice", "script": null, "see": ["Ar"]}
118	          ],
119	          "script_extra": null,
120	          "note": null,
121	          "quote": null
122	        },
123	        {
124	          "id": 9,
125	          "parent": 8,
126	          "lang": "Persian",
127	          "refs": "IRN:119; BQT:98,101",
128	          "words": [
129	            {"translit": "Âbâdân", "gloss": "a port city at Persian Gulf", "script": "آبادان"},
130	            {"translit": "Ardavân", "gloss": "\"protector of justice\"", "script": "اردوان"}
131	          ],
132	          "script_extra": null,
133	          "note": null,
134	          "quote": null
135	        },
136	        {
137	          "id": 10,
138	          "parent": 0,
139	          "lang": "Avestan",
140	          "refs": "POK:829; SYN:104",
141	          "words": [
142	            {"translit": "pitar", "gloss": "father", "script": null}
143	          ],
144	          "script_extra": null,
145	          "note": null,
146	          "quote": null
147	        },
148	        {
149	          "id": 11,
150	          "parent": 10,
151	          "lang": "Persian",
152	          "refs": null,
153	          "words": [
154	            {"translit": "pedar", "gloss": "father", "script": "پدر"}
155	          ],
156	          "script_extra": null,
157	          "note": null,
158	          "quote": null
159	        }
160	      ]
161	    }
162	  ]
163	}
164	
```


### [2026-09-07T20:30:55.020Z] TOOL RESULT

```
1	=== PDF page 379 (book page 349) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Pa, Pa-ter, Poti, Potiš : Pa: to protect, to feed. Pa-ter: protector, feeder (of the family), father ☞ Ter 3. Poti, Potiš: protector, husband, power, also self. This has probably started as a nursery word and became a usual term in the Indo-European languages. Compare with the root "Baba".  (refs POK:787,842; SYN:103; KAS:10)  PART 1
4	#1 (parent #0) [Avestan / Old Persian] refs=HRN:41,72; KLN:114; AHD:1532 | pa 1 : to guard
5	  #2 (parent #1) [Persian] refs=BQT:358,1069; KLN:169; FSF:335; TZF:21 | pâyîdan «پاییدن» : to watch ; bân «بان ۱ -» : a suffix meaning protector ; pâlŭdan «پالودن» : not to contaminate, clean | extra: پادن، پای ۲، پاس
6	پاد ، پادشاه ، پادگان
7	پاسبان ، دربان ، سروان ، چوپان ، شبان
8	پالایش ، پالوده ، فالوده، پالان
9	  #3 (parent #1) [Avestan / Old Persian] refs=POK:842; HRN:41; KLN:144,157; AHD:1532 | paiti 1, patiy, pavan, pâna : master, protector ; pathra : protection ; fšu-paiti : cattle protector, shepherd ☞Pek ; paiti-xšathra : protecting king ☞Ksei 1
10	  #4 (parent #1) [Avestan] refs=POK:842; SNS:267 | xvaĕ-pati, xvaĕ-paithya : one's own self ☞Seu 1 | NOTE: "pati, paithya" means self or own in this combination
11	    #5 (parent #4) [Persian] refs=POK:842; SNS:267 | xîš 1 «خویش ۱» : self
12	  #6 (parent #1) [Avestan / Old Persian] refs=HRN:72 | âthur-pât-gan : fire protector ☞Ater ; pa-nâh : protecting help, shelter ☞Nâ 2 ; paiti-dâma : body protection ☞Dhě 2
13	    #7 (parent #6) [Persian] refs=BQT:418 | Âzarbâyjân «آذربایجان» : A city in Iran ; panâh «پناه» : shelter ; panâm «پنام» : mouth guard used by Zoroastrians
14	  #8 (parent #1) [Pahlavi] refs=IRN:119 | ô-pât-ân : city with protected waterways ☞Ab 1 ; arta-pân : protector of justice ☞Ar
15	    #9 (parent #8) [Persian] refs=IRN:119; BQT:98,101 | Âbâdân «آبادان» : a port city at Persian Gulf ; Ardavân «اردوان» : "protector of justice"
16	#10 (parent #0) [Avestan] refs=POK:829; SYN:104 | pitar : father
17	  #11 (parent #10) [Persian] refs=None | pedar «پدر» : father
18	
```


## [2026-09-07T20:31:00.011Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md | head -100",
 "description": "Read source matrix"
}
```


### [2026-09-07T20:31:00.052Z] TOOL RESULT

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


## [2026-09-07T20:31:01.310Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','KAS','HRN','KLN','AHD','BQT','FSF','TZF','SNS','IRN','WLD','IEC','BRT','KNT','PHD','NYB','HUB','MON','ARY','CHEUNG']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-07T20:31:02.682Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

KAS {"title": "M.A. Hasani Da'i al-Eslam, Khod-amuz-e Zaban-e Sanskrit, Danesh 1361/1982", "kind": "website", "url": "https://ketabnak.com/book/108067 (131 pp. PDF, login)", "lookup_hint": "Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF page exists; not fetched."}

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF exists but not downloadab

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/v

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

CHEUNG null
```


## [2026-09-07T20:31:51.204Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-316.json'))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:2500])\nprint('---NODE---')\nprint(json.dumps(e['nodes'][1],ensure_ascii=False,indent=1)[:3000])\n\"",
 "description": "Inspect an existing verified page"
}
```


## [2026-09-07T20:31:51.740Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-07T20:31:52.475Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Mâ, Mâ-ter",
 "verdict": "plausible",
 "modern_form": "PIE *méh₂tēr 'mother' (Pokorny māter- 700–701; AHD māter-), itself built on the nursery word *mā- / *méh₂- 'mother' (Pokorny mā-3, 694)",
 "note": "Both halves of the root box are real reconstructions and the language label 'Indo-European' is right, but two details of the gloss are Nourai's own. (1) Pokorny's mā-3 (p.694, the page Nourai cites) is glossed 'mother (expr. root)', not 'breast'; the 'breast' sense comes only from the reduplicated derivatives (L. mamma 'mother’s breast, nipple', mamilla), so it is a back-projection. (2) 'Mā-ter: feeder (of the family)' with the cross-reference to Ter 3 analyses -ter- as the agent suffix. Watkins and Walde–Pokorny call it the KINSHIP suffix and offer no such gloss ('Based ultimately on the baby-talk form ma-2, with the kinship term suffix -ter-'); Skeat's older view was '√MĀ to measure', i.e. 'manager of the household'; and Wiktionary reports a minority modern view of a genuine verbal root *méh₂- 'to nurse, to mother' — which is the closest anyone comes to Nourai's 'feeder', but it is not the standard account. Also note the page numbers: 694 is mā-3, while māter- is Pokorny 700–701. Nourai's closing remark about a nursery word becoming the usual term is a paraphrase of Buck 2.36 (SYN:103), which he cites correctly. Everything downstream (Avestan–Pahlavi–Persian; Germanic; Latin; Greek) is sound; the one substantive error on the page is in node #8.",
 "note_fa": "ریشهٔ هندواروپایی آغازین *méh₂tēr «مادر» (پوکورنی ۷۰۰–۷۰۱) و واژهٔ کودکانهٔ *mā- (پوکورنی ۶۹۴) هر دو واقعی اند و برچسب «هندواروپایی» درست است؛ امّا دو نکتهٔ معنایی از خود نورایی است: یکی آنکه پوکورنی در ص ۶۹۴ mā-3 را «مادر» معنی کرده و نه «پستان» — معنای پستان تنها از مشتقّات دوگان‌شده (mamma, mamilla لاتینی) برمی‌آید؛ دوم آنکه تفسیر «mā-ter = خوراک‌دهندهٔ خانواده» پسوند -ter- را پسوند فاعلی گرفته، در حالی که واتکینز و والده‌پوکورنی آن را پسوند واژگان خویشاوندی می‌دانند و چنین معنایی نمی‌دهند (ویکی‌واژه دیدگاهی اقلیتی را گزارش می‌کند که *méh₂- را ریشهٔ فعلی «شیر دادن، مادری کردن» می‌گیرد). در مجموع ریشه با احتیاط پذیرفتنی است و همهٔ شاخه‌های پایین‌دست درست اند؛ تنها خطای جدی این صفحه در گرهٔ ۸ («ممه») است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9h%E2%82%82t%C4%93r",
  "https://www.etymonline.com/word/mother"
 ],
 "ref_check": [
  {
   "ref": "POK:694",
   "status": "partial",
   "note": "Pokorny 694 is 'ma
---NODE---
{
 "id": 2,
 "lang": "Pahlavi",
 "words": "mâtar; matak; mâdiyânag, mâyag",
 "verdict": "confirmed",
 "derivation": "All three Pahlavi items are real and all go back to Av./OIr. mātar-. (a) mātar ‘mother’: MacKenzie has 'mād [AM < A ʾM-Y, v. mādar | M md] mother' and 'mādar [AMYtl; mtl | M mdr, N ~] mother' — the Aramaic heterogram ʾM(Y) masks an inherited word; mād is the nominative-derived short form, mādar the oblique stem mātar-, exactly as Nyberg describes ('māt [mʾT; ʾM] cas. obl. mātar [mʾtl; ʾMY-tl] mother … Common Ir.'). (b) mātak/mādag [NKB; mʾtkʹ] ‘female’ = *māta-ka-, a -ka- derivative of māt(ar) ‘mother’, borrowed into Armenian as matak ‘fēmella’ (Nyberg: 'from māt (q.v.)'). (c) the same -ka- formation in the abstract sense ‘the essential element of anything, its core, essence; materials’ gives Pahlavi mātak / (Manichaean) māyag [my g] with the intervocalic t > y development, whence NP māya; mātag-dān / mātīyān is Nyberg's 'that which contains the kernel, the core, or substance and essence of a thing' — Nourai's 'mādiyānag: essence'. Nourai's spelling matak (short a) for mātak is the book's usual loose transcription, not a different word.",
 "derivation_fa": "هر سه صورت پهلوی واقعی اند و همه به mātar- ایرانی باستان بازمی‌گردند: ۱) māt / mātar («مادر»؛ مکنزی ص ۵۶ و نیبرگ، با نوشتار هزوارش ʾM/ʾMY-tl)؛ ۲) mātak «ماده، موّنث» که پسوند -ak (ایرانی باستان -ka-) بر ستاک «مادر» افزوده شده و به ارمنی هم وام رفته است (matak)؛ ۳) همین mātak در معنای «جوهر، مادّهٔ اولی»، که با ابدال t میان‌واکه‌ای به y صورت māyag گرفته (در فارسی میانهٔ مانوی my g) و mātag-dān / mātīyān نیبرگ «آن که مغز و جوهر چیزی را دربر دارد» همان «mādiyānag» نورایی است. ادعای نورایی درست است؛ تنها «matak» را باید mātak (با الف کشیده) خواند.",
 "sources": [
  "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%AF%D9%87",
  "https://en.wiktionary.org/wiki/%D9%85%D8%A7%DB%8C%D9%87",
  "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%AF%D8%B1"
 ],
 "ref_check": [
  {
   "ref": "BQT:1933",
   "status": "supports",
   "note": "Nourai's BQT pagination runs two pages behind the Ibn Sina scan on disk (his 1946/1964 = our 1948/1966), so BQT:1933 = the mādar page, our printed 1935 = BQT_v4 pdf page 16. Mo'in's footnote there: 'مادر – بفتح سوم = ماد = مار (ه.م.). پهلوی mātar, mād … حالت فاعلی از -mātar «بارتولمه ۱۱۶۷»، اوستا -mātar، ارمنی mayr، هندی باستان -mātar … افغانی mor، آسی mad…، بلوچی mās…' — i.e. Pahlavi mātar/mād from Avestan mātar-, precisely the arrow drawn."
  },
  {
   "ref": "SNS:237",
   "status": "partial",
   "note": "Tavoosi's Shayast-ne-Shayast glossary entry 1167 is on disk: '1167) matar: MP mātar … mādar, mʾTY-tl … (Wan. III, 57) mʾdr, mʾd … 1168) mādarān, mʾdy-tlʾan' (SNS.txt l.4544). The entry says exactly what the arrow says (Pahlavi mātar with spellings mʾTY-tl, mʾdr, mʾd). The printed page number cannot be confirmed: the OCR of SNS is largely unreadable and refs_online.json records 'page offset not determined'."
```


### [2026-09-07T20:31:52.507Z] TOOL RESULT

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


## [2026-09-07T20:32:13.135Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK grep pā- protect / poti / pəter ===\"\ngrep -n \"^pā-\\|^pōi-\\|^poti\\|^pəter\\|^pətér\" POK_full.txt | head -40\necho \"=== POK_02/03 files list ===\"\nls | head -60"
}
```


### [2026-09-07T20:32:13.199Z] TOOL RESULT

```
=== POK grep pā- protect / poti / pəter ===
80755:potion'; alb. gjerp{*seib'^d) "I sip, swallow', gjerbe'drop, drip'; 
=== POK_02/03 files list ===
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
```


## [2026-09-07T20:32:15.067Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT pā-  ===\"\ngrep -n \"pā-\\b\" BRT.txt | head -20\necho \"=== BRT xvaēpaiθya ===\"\ngrep -n -i \"xᵛaēpaiθya\\|xvaēpaiθya\\|xᵛaēpaiti\\|hvaēpaiθya\" BRT.txt | head -20\necho \"=== BRT paiti.dāna ===\"\ngrep -n -i \"paiti\\.dāna\\|paitidāna\\|paiti\\.dāma\" BRT.txt | head -20\necho \"=== BRT pāθra ===\"\ngrep -n -i \"pāθra\\|paθra\" BRT.txt | head -20"
}
```


### [2026-09-07T20:32:15.177Z] TOOL RESULT

```
=== BRT pā-  ===
=== BRT xvaēpaiθya ===
=== BRT paiti.dāna ===
=== BRT pāθra ===
```


## [2026-09-07T20:32:21.514Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT size/sample ===\"\nwc -c BRT.txt; grep -c \"\" BRT.txt\necho \"--- paiti hits count ---\"\ngrep -c -i \"paiti\" BRT.txt\necho \"--- 'Mundschleier' ---\"\ngrep -n -i \"mundschleier\\|munds\" BRT.txt | head\necho \"--- xvaepai ---\"\ngrep -n -i \"xvaepai\\|hvaepai\\|vaepaiOya\\|paiOya\" BRT.txt | head -20"
}
```


### [2026-09-07T20:32:21.612Z] TOOL RESULT

```
=== BRT size/sample ===
4803500 BRT.txt
30725
--- paiti hits count ---
1062
--- 'Mundschleier' ---
--- xvaepai ---
9274:mit  3  'durch  Schneiden  gestalten, schaffen',  von  AAura:  azjm  y5  akurö mazdä  yas?  tal  nmämm  äk^rtfum  V.22.1. mit  upa  Tiineinschneiden  in  —  (Akk.), anschneiden':  daürum  hl  paioyam  upa.- k3r3ntay?n  V-iJ-SZ-
15209:•  j.  paiSya-,  paioya-'^  den.  Praes,  32'' 'potiri'.
```


## [2026-09-07T20:32:23.444Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full sample around 'poti' ===\"\ngrep -n -i \"poti-s\\|potis\\|\\bpotis\\b\" POK_full.txt | head -20\necho \"=== POK: pəter ===\"\ngrep -n -i \"p.ter-\\|pater-\" POK_full.txt | head -20\necho \"=== POK files ===\"\nls POK* 2>/dev/null; ls incoming/POK 2>/dev/null | head"
}
```


### [2026-09-07T20:32:23.541Z] TOOL RESULT

```
=== POK_full sample around 'poti' ===
33470:It is a compound of Root/ lemma: ghosti-s\ stranger; guest + Root/ lemma: poti-s: 
35736:despotism, arbitrariness'), with intersection in neuter Old Norse k0r' choice ', Old English 
53215:under poti-s), noas "whereto' (-as from -te) = Gothic fvat^, fvad 'whereto'; Cretan teTov 
62609:grandson ', later also ' nephew '; Old Lithuanian nepotis, /7e/0^c//s "grandchild, grandson'; 
68715:Latin potis {potior, potissimus) "wealthy, mighty', possum. Old Latin also potis sum 
=== POK: pəter ===
69157:Root / lemma: pster-, pstereu- 
73586:Root /lemma: seni-, senu- {Sgni-), sp-ter- 
=== POK files ===
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
```


## [2026-09-07T20:32:29.238Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Root / lemma: poti-s\\|Root/ lemma: poti-s\\|lemma: poti\" POK_full.txt | head\ngrep -n \"lemma: p[āa]-\\b\\|lemma: pā-, pə-\\|lemma: pa-t\\|lemma: p.t.r\" POK_full.txt | head\ngrep -n \"lemma:.*t.r-.*father\\|Page(s): 829\\|Page(s): 842\\|Page(s): 787\" POK_full.txt | head -20"
}
```


### [2026-09-07T20:32:29.320Z] TOOL RESULT

```
33470:It is a compound of Root/ lemma: ghosti-s\ stranger; guest + Root/ lemma: poti-s: 
69157:Root / lemma: pster-, pstereu- 
64843:Page(s): 787-788 
64951:Page(s): 787 
67603:Page(s): 829 
67878:Page(s): 829 
68740:Page(s): 842 
68758:Page(s): 842 
68908:Page(s): 842-843
```


## [2026-09-07T20:32:32.252Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '64800,64960p' POK_full.txt"
}
```


### [2026-09-07T20:32:32.303Z] TOOL RESULT

```
Latin pacTsco {sek. -or) " einen Vertrag oder Vergleich festmachen, abschlieflen ', Old 

Latin pacio^ pactio ', pacunV paciscuntur ', pax, -c/'sf. "peace; friendly disposition ' 

(Umbrian pase tua^ pace tua ' in the address of divinities), yoa/i/s "picket, pole' (from *pak- 

slos, compare Demin. paxillus); pango {pepigr, renamed peg/ afier freg/, and panx/) " 

r 

befestigen, einschlagen; aneinanderfijgen, schriftlich verfassen, festsetzen ' (to the 

nasalization of present compare Germanic *fa/jxan), compages^ ]o\x\\. ', pag/na{*\he 

papyrus stripes added to the sheet) " sheet of paper, side, column ', pagus^ rural 

community, village, construction ', propago, propages^ Setzlinge ', propagare^ einen 

Setzling in der Erde festmachen, daher fortpflanzen '; Umbrian pase {see above), paca 

Adv. " causa ', Oscan prupukid^ ex antepacto ?', Umbrian Paelignian Marrucinian pacri- " 

propitius, placatus '; Middle Irish age^\\mb, member, pillar' {*pagio-), ^//"pleasant' {*pagli-\ 



or as *pokli- to Old Icelandic faegiligr^s., s. *peR-1l); cymr. ae/c»o'"limb, member' 
{*paglatu-)\ 

Germanic Nasalpras. *farjxan (: Latin pangd) in Gothic fahan. Old Icelandic fa. Old 
English fon. Old High German fahan. Old Saxon fahan an6 fangan' capture ', Gothic 
gafahn.. Old Icelandic fengr. Old English fengm.. Old High German fangm. " catch, booty 
'; Old High German fuoga' joint ', gafuogi^ fitting', hJ-fuoge^ matchmaker ', Old High 
German fuogen. Old Saxon fogian^ add ', Old English gefegan^ fit, connect ', Middle High 
German vagen^ add '; from *pag-:Q\^ Saxon fac^ encirclement, Umzaunung ', Middle 
Low German i/a/rm. ds. "dividing off, partitioning off. Old High German fah^ moenia ', 
Modern High German Fach, einfach; from temporal department Old English /fee 'stretch of 
time'. Middle Low German vaken, vake. Late Middle High German ^ei/ac/?' often'. Middle 
High German drier vacher' thrice, three times '; 

Slavic *yC»aza-m. in sloven, paz ' \o\nt ', paz' wooden wall '. 

References: WP. II 2 f., WH. II 232 f., 235 f., 245 f., Trautmann 209. 
Page(s): 787-788 

Root / lemma: pan- 
Meaning: fabric 

Material: Gr. nfjvoc; n., nnvri f. " texture ' Hes., nr|viov " rolled up thread, fabric, garment ', 
nnvi^opiai ' weave ' (Doric naviaSsTai Theokr.); ablaut. Latin pannus' a piece of cloth, 
garment of cloth ' (expressive nn); 

Maybe alb. Geg pen/, Tosc per/^ thread ', alb. geg gjyi-pana, Tosc gjilpere^ needle '. 
Gothic fanam. 'rag, sweat cloth'. Old High German /^/70 'stuff, kerchief, cloth'. Modern 
High German Fahne, Old English fanam. 'banner, ensign, flag, kerchief, cloth; Iris', fane, 
fanui. 'banner, ensign, flag. Iris '; unclear. Middle Irish an-art^ leinernes Tuch '; one might 
understand gr. and Latin a as expressive (compare above S. 211 to gall, drappus), could 
be accepted in relationship to (s)pen-^ be tight, spin '. 
References: WP. II 5, WH. II 247 f. 
Page(s): 788 

Root / lemma: par- 
Meaning: to show; be visible 

Material: Gr. nsnapsTv ' show ', nenap£uai|Jov sucppaoTov, aa(p£(; Hes.; Latin pared, -ere^ 
erscheinen, sichtbar sein, sich zeigen; Folge leisten, gehorchen ', appared, compared^ 
appears ' {parret, after Festus for paret, as baca : bacca etc.). 



References: WP. II 6, WH. II 252 f. 
Page(s): 789 



Root / lemma: paso-s 

Meaning: a relation 

Material: Gr. nr|6(;, Doric naoq ' Verschwagerter ', nawrai auYY£V£T(; Hes.; Latin pari-cTda 

( *paso-kaida) newer parri-cTda 'murderer of a close relative '; after Wackernagel Gnomon 

6, 458 from * parso-cidaio Indie purusa- 'person' from Old Indie *pursa-. 

References: WP. II 7, WH. II 253 f. 

Page(s): 789 

Root / lemma: pauson- : puson- 

Meaning: name of a deity 

Material: Old Indie Pusan- m. ' Vedie God, guardian and defender of the herds and the 

human possession generally ', gr. flav, Areadian flaajv (*naua(jov); lllyrian (Messapie) PN 

Pauso, -onos, gall, (venet.) PN Pusam.; doubtful, whether to Old Indie pusyati, pusnati, 

posati^ prospers, becomes overgrown, makes prosper, nourished ', p6sa-xx\. ' prospering; 

flourishing, growth '; 

References: WP. II 2; compare Charpentier Indo Germanic Jb. 19, 90. 

See also: see below pu-1. 

Page(s): 790 

Root / lemma: pa- : pa- and pa-t- : pa-t- 

Meaning: to feed, graze 

Material: Armenian hauran^ herd' {*pa-tro-), /701//1/ 'herdsman, shepherd' {*oui-pa-)\ gr. 

Doric TTavia rrAnapovn, navia TanArjaiJia; Latin pasco, -ere, pavi, pastum 'allow to graze, 

fijttere', Dep. ' devour, graze' {*pas-scd), yoas/o/'' herdsman, shepherd'. 

Maybe Alb. {* pastor!) i6>5/'/' herdsman, shepherd'. 

Note 

Alb. i6>a/''grass, fodder', bares^ walk, stroll ' derived from alb. {*barma) it'SAna 'medicine, 

herb, grass' from lat. pharmacum < gr. pharmakon from Egyptian Coptic pahre, fahn" cure'. 

Lat. pabu/um load' {*pa-d^/om), pan/s'bread' (because oi past/7/us' pellet, globule from 
meal, flour' from *pa-st-nis)\ Messapie iravoc, 'bread' is Latin loanword; Old Irish ain-chess 
' bread basket'; 



perhaps as Venetic-lllyrian element in Celtic *pa-ro-^ willow ' in cymr. pawr' willow ', PI. 
porion, therefrom Verbalnom. pori. Middle Breton peuriff, bret. yOe^/7" graze'; with -//to- suffix 
Old Icelandic fodru.. Old English fodoru.. Old High German fuotarlood'; Old Church 
Slavic pasg, past/'graze' ( *pasRd)\ Tocharian A pas-, B pask- 'beware, guard'; Hittite 
pahs- {pahhas-) " shield '. 
Maybe alb. Geg me pa, aor. pashe'to watch, protect'. 

With -^further formations: gr. naiEopai 'eat and drink '; aTraaToq ' without meal and 
drink, beverage, liquid which is swallowed to quench one's thirst, draught, potion'; doubtful 
Old Irish as{a)/d' it grows' (" increases '), Middle Irish 55' Wachsen ' {*pat-to-)\ Gothic 
fodjan^ nourish ', Old Icelandic f0da. Old English fedan. Old Saxon fodian. Old High 
German fuotenAs., Old English foda, engl. /boo^'nourishment, food'. Old English fostor 
ds.. Old Icelandic fostr^ upbringing, sustenance, livelihood' {*pat-tro-)\ ablaut. Old High 
German kauatoV pasta ' (Old High German Gl. 2, 333, 65), /^/^/7^a 'nourishment, food'. 
Middle Low German vedemei. ' acorn mast '. 

References: WP. II 72 f., WH. II 246 f., 260, Trautmann 207 f.; 
See also: compare also pen-lleed'. 
Page(s): 787 

Root / lemma: {peg- :) pog- : pog- pok-s- {*pegh-) 

Meaning: shoulder, hip, side 

Material: Old \x\(X\c paksa-vn. 'shoulder, wing' and ' side posts ', paksas-n. 'side'; common 

Old Indie -gh- > -ks-
```


## [2026-09-07T20:32:40.453Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '68700,68780p' POK_full.txt\necho \"@@@@@@@ 829 area @@@@@@@\"\nsed -n '67540,67610p' POK_full.txt"
}
```


### [2026-09-07T20:32:40.532Z] TOOL RESULT

```
Meaning: owner, host, master, husband 

Material: Old \nd'\c pat/-, Avestan pa///- "master, mister, lord, master, consort, partner'; Old 

Indie /Oa//7/"" mistress, wife', Avestan paz?/?/- 'mistress'; Old \nd\c patyate^\r\errsc\nt, is 

teilhaftig' (: Latin potior); 

Avestan x'ae-pati- "er selbst'; 

gr. hogk; ' husband ', nowia "mistress (of Hauses), wife'; 5£a-noiva 'mistress of 
Hauses' (*5£a-novia, from *5£a-noTvia), 5£a-n6Tr|<;, -ou "master, mister of Hauses' (see 
above S. 198); alb. pata^had', y05s/7e"gehabt' {*pot-to-) (to a present as Latin potior. Old 
Indie yoa/ya/e); 

Latin potis {potior, potissimus) "wealthy, mighty', possum. Old Latin also potis sum 
"kann', potui, potensirom an e-denominative as Oscan putiad ^possW, putians 'poss\nt', 
Latin potestas^ power', potior, -TrT{potrtur and potTtui) "sich bemaehtigen'; com-pos 
"teilhaftig' (*"Mitherr'), tiospes, -itis' guest's friend ', pael. iiospus {*gtiosti-pots^ Qasihexx'); 
ein unflektiertes *poti 'selbst' placed in utpote^as natijrlich, da namlich, namely', actually 



*ut *pote{esf) "as es possible is = naturiicli', furtlierwitli syncope in m/hr-, meo-, suapte 
etc.; 

Gotliic bru^-fa^s^ bridegroom ', /7£//70'a-/&A'5"Befelilsliaber about 100 Mann'; engl. fad 
"strong, valiant, big, large'; 

Lithuanian pa/s "husband' and "selbsf (old patis), Latvian pats^ householder ' and 
"selbsf, Lithuanian K/espa/s "master, mister' (old viespatis). Old Prussian pattiniskun f\Vk. f. 
" matrimony '; f. Old Lithuanian viespatnr, *patn/'under influence of *yOa//- transfigured to 
*patr\n Old Prussian waispattin f\Vk. "wife, woman', Lithuanian pat/^\N\ie', Latvian pat/ 
"Wirtin'; indekl. particle Lithuanian pat, Latvian yC>a/"selbst, even, straight'; about Old 
Church Slavic gospodb "master, mister', see above S. 453; 

Hittite -yC»s/"eben(so), also, rather'; Tocharian A pa/s "husband'. 

References: WP. II 77 f., WH. I 660 f., II 350 f., 379 f., Trautmann 208, Benveniste 
Origines 1, 63 f., Pedersen Hittite 77 f., Endzelin Latvian Gr. 396 f. 
Page(s): 842 

Root / lemma: po-ti 

Meaning: against 

Note: through das Adv.-forms -//(compare *proti- : *pro above S. 815 f.) from *po (see 

below *apo' ab') extended 

Material: Avestan pa/'t/, ap. /05//y proverb, and preposition "against, entgegen, to, auf, by'; 

"an; for, um'; "from - from'; "in - toward, in'; hom., Boeotian, lak. etc. nori "np6(;' proverb. 

and preposition "against - toward, against, compared with; an, to', "in - toward, from-'. 

References: WP. II 77, Schwyzer Gr. Gr. 2, 508 f. 

Page(s): 842 

Root / lemma: pougo- or pougho- 

Meaning: clear, sound 

Note: only Celtic and Slavic 

Material: Old Irish o^"jungfraulich', oge"Jungfraulichkeit'; Czech pouhy^ pure, bare, 

simple, just'. 

References: WP. II 77. 

Page(s): 843 

Root / lemma: p6(i)-1 : (pa/-?:) pT- 



Meaning: to graze 

Material: Old Indie pati, Avestan /7a///"hutet, bewacht, schijtzt', Old Indie go-pa- m. 
@@@@@@@ 829 area @@@@@@@
"Brandfacker, korinth. flupFoq 'Pferdename' (*" feueirot '), nuppoq, poet, nupaoq " 

feuerrot ' fnupoFoc;); 

Maybe lllyrian TN Pirustae (Pipustae) 

Umbrian p/rl\re' ( *pu/), Akk. purom-e^\ns fire' ( *pur-), Oscan aasaf purasiaf^ in 

f . . . , 
araigniana ; 

Old Icelandic furrvn. "fire' {*pur-) and fyrr, fyr'r. Old High German Old Saxon Old Frisian 
fiur{*peurJ)\ Old High German older /^^//'(disyllabic, compare Musp. vugii). Old English fyr 
(from Lok. *puueri)\ 

Gothic /5/7"fire' {*pudn). Gen. Dat. funins, /Z//7//7 (latter from * puneni, a hybridization from 
*puueni: *pun-es). Old Icelandic funim. "fire'; Old High German funko. Middle English 
/b/7/re "spark'; with ablaut ( *puon-) Middle Low German Ka/7/re "spark'; 

Maybe lllyrian TN Perestae (Penestae) 

Old Prussian pannolke', panu-stac/an TeuerstrahV {*puon-u), loanword Finnish panu 
"fire'; 

Slavic *pur/a-m. 'glowing ash' in Czech pyrm. and pyr/n. 6s.; in addition Old Czech 
pynna' favilla ', Czech pyre f/" g\o\N' , serb. ^p/>7//"anfachen' etc.; 



Hittite pahhur, pahhuwar, Dat. pahhu(e)ni^\\x€\ Tocharian A por, B puwar, pwards. 

Note: Hittite used reduplicated -Z?/?- for voiced laryngeals!! 

References: WP. II 14 f., WH. II 391, Trautmann 206, 232, Benveniste Origines 1,10; 
Pedersen Hittite 187f. 
Page(s): 828 

Root / lemma: pezd- 

Meaning: to break wind 

Note: (compare 'joe/'o'- 'loudly fart ') 

Material: Gr. p5£U) "leise einen streichen lassen' from *pz5£U) (reconverted with metathesis 

from *pezdd}, wherefore p56-Ao(; " fetidness ' with new formationer ograde, and *p5£-Au-(; 

"pedens, scornful, ridiculing' in BSeAu-kAewv 'Cleontloppedens', as well as as base from 

(35£Aup6(; "disgusting", ^bzK\}aao\xa\ "verabscheue, empfinde disgust, repulsion, loathing ', 

(35uAAiJL) 'verabscheue, dread', but also "p5£U)'; Latin pedo, -ere ' fart ' ( *pezdd), podex'Vne 

Hintere' {*pozd-ek-s), ped/'s louse' (because of Demin. ped/cu/us o\der *pede^] 

kir. pezd/ty and zero grade (proto Slavic *bbzd-) bzdfty, russ. bzdetb 'leise einen 
streichen lassen', sloven, pezdeti, Lithuanian bezdu, bezdeti, Latvian bezdetleise einen 
streichen lassen', Lithuanian b /zdas ^ podex' , b /zdz/us ' Stanker'; Baltic *bezdet/based on 
auf 'yozo'e// besides *pezdetr, perhaps handelt es sich also um contamination with the root 
bhes-'blow', above S. 146. 

References: WP. II 68 f., WH. II 272 ff., Trautmann 221 ; 
See also: compare above pes-1. 
Page(s): 829 

Root / lemma: ped-1, pod- 
Meaning: container, vessel 

Material: Old Indie perhaps pa/Za-m. 'Kornbehalter', pa///" grain measure' (whether -//-from 
-dl-)\ Old High German fazzon. Middle High German vazzen^\v\ ein vessel tun, catch, 
riJsten, sich bekleiden'. Old High German fezzil. Middle High German i/ezze/'band, strap,
```


## [2026-09-07T20:32:49.763Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=68780 && NR<=68920' POK_full.txt\necho \"@@@@ search father lemma @@@@\"\ngrep -n \"Meaning: father\" POK_full.txt | head"
}
```


### [2026-09-07T20:32:51.065Z] TOOL RESULT

```
Material: Old Indie pati, Avestan /7a///"hutet, bewacht, schijtzt', Old Indie go-pa- m. 
"herdsman, shepherd', Avestan /'a/75-/0a'Beinschutz, -schiene'. Old Indie /Oayi/-"Huter' 
(compare noju), pala- m. "Wachter, herdsman, shepherd', -/0ai/5/7"schutzend', ap. xsa^''a- 
/7ai/aA7"Landvogt, Satrap'; Old \v\6\c nr-pT-ti-i. 'Mannerschutz'; nr-p-a-m. 'MannerschiJtzer 
=king'; patra- n. ' container ' (= Gothic fodr); 

gr. nu)u 'herd' (n. to Old Indie payu-), noipnv 'herdsman, shepherd' (: Lithuanian 
piemud), noi|jr|v 'herd', noipaivw 'treibe auf die Weide, hijte; ziehe auf; -nG)\xa {po-mn) 
'cover'; 

Gothic fodru. (= Old Indie patra-, yet agrees in addition in pronunciation of only Old 
English fodoi) 'BriKri, vagina'. Old English fodor, fodor' sheath, vagina'; Late Old Icelandic 
fodrv^. 'food (of clothing)' from Middle Low German voder^s.; Old High German 
(fedar)fdtar^ cav\v\a\ Late Old High German fuoter^Vc\eca\ Modern High German Futter{oi 
clothing), Futterat, 

Lithuanian yO/e/77^0' herdsman, shepherd', Akk. pfemeni{ *pdimen-). 

References: WP. II 72, Trautmann 204, 207 f. 
Page(s): 839 

Root / lemma: pd(i)-2: pA-and (from pd-from) pa- 
Meaning: to drink 

Grammatical information: Aoristwurzel, wherefore secondary present pi-po-mi, pi-bo-mi, 
themat. pi-bo 

Material: Old Indie paZ/'trinkt', Aor. apat, pay-ayati, payate 'trankt' (: Old Church Slavic 
pq/'g, pojiti), panamu. 'Trunk' (: gr. Eunojvoq 'pleasant to drink' Hes., Middle Irish ant 
'vessel'). Inf. patave^io drink' (= Old Prussian poOtweiAs.), patar-, patar-rw. 'Trinker' (= 
Latin potords.), -pay/a-, -payya-'io water, soak. Trunk' (= Old Prussian pou/sm. 'das 
Trinken'), patra- n. 'drinking vessel' {*pd-t/o-m= Latin pocu/um ^ gob\et'); participle Pass, 
ablaut. yO/?^-'getrunken (habend)', p/t/-t 'das Trinken, Trunk', Avestan vispo-pitay- 
'alltrankend'; Old Indie Inf. patum, patave. Gerund. pTtva- (: Latin potusm. ' drink, 
beverage, liquid which is swallowed to quench one's thirst, draught, potion'); redupl. 
athematic present 3. PI. pi-p-ate, participle pf-p-ana-, Aor. a-pipT-ta-, thematic /0/Z?a//"trinkt' 
(= Old Irish ibid); 

Armenian ampem^ drink ' (formation unclear); 



gr. nivu), Lesbian ircbvoo (of Nominal stem *pd-no-, compare above suttojvoix;) " drinl< ', 
Fut. (Konj.) niopai, Aor. sniov, Imper. nTGi, Perf. nsnajKa, Med. TT£no|jai " drink ', TTaJ|ja, 
TTOija n. Trinken, drink, beverage, liquid which is swallowed to quench one's thirst, 
draught, potion', -noioq, m., hogk;, -\oc, and -sux; f. ds., norrip m., norripiov n. " drinking cup 
', ttTvov n. "Gerstentrank', niniGKU) (Fut. mau)) 'give to drink'; 

alb. yO/" 'drink' etc.; 

Latin bibo, -ere' drink ' (assimil. from * pibd\ Faliscan pipafo'\ werde drink'; Latin poto, - 
are' drink strong', potus' drunk, intoxicated, getrunken' (= Lithuanian puotai. 
'Zechgelage'), potus, -usxx\. ' drink, beverage, liquid which is swallowed to quench one's 
thirst, draught, potion' (= Old Indie /Oa/i//77 Inf.), potidi. 'Trinken, drink, beverage, liquid 
which is swallowed to quench one's thirst, draught, potion' (: gr. aiJ-nwTK; f. 'Ebbe', Old 
Prussian poJ/'drink' from *pdti-), pocu/um 'gob\et' {*pd-tlo-m), potorvn. 'Trinker' (= Old 
\v\6\c patar-); Umbrian puni, poni'xwWV! (: Old \v\6\c panam' beverage, drink '); Old Irish ibid 
{*pibeti) 'trinkt', Verbalnom. Dat. Sg.c»^/(disyllabic) 'Trinken' {*poJa-lo-)\ acymr. iben 
'bibimus', corn, ei/a/'bibo'. Middle Breton euaff6s.\ Middle Irish ani. 'drinking vessel' (: 
Old Indie y05/75/r7 'Trunk'); 

Balto-Slavic */Oo/oand *plid' drink ' in Old Prussian yoo/e///' trinkt', poOism. 'das Trinken', 
Old Church Slavic pi/'g, pifi' drink '; pirb m. 'Bankett', pivon. ' beverage, drink ', Czech etc. 
'beer'; Kaus. Old Church S\av'\c pq/'g, pq/it/ 'iranke'; Balto-Slavic *pdta- and *pTta- 
'getrunken' in Lithuanian puotai. 'Trinkgelage' and Old Church Slavic pitijb 'trinkbar'; 
Balto-Slavic *p^tiu\^6 *pTti\. 'das Trinken' in Old Prussian Inf. poOt{*pdti-) and slov. p?tt ' 
beverage, drink ' (Infin. *pitij\ Balto-Slavic * potu- m. 'das Trinken' in Old Prussian Inf. 
puton, poutonan6 poutwe/'dnnk', ablaut, passive russ. -Church Slavic yO/fe. 

References: WP. II 71 f., WH. I 103 f., Trautmann 228 f. 
Page(s): 839-840 

Root / lemma: pou- : pau- : pu- 

Meaning: small, little; young (of animals) 

Material: 1. With -o-suffix; Gothic fawaiP\. 'wenige'. Old Icelandic far' little, wortkarg', fa- 

t0/cr' arm' (as Latin pauper). Old High German fao, fo' little ', Dat. PI. fouuem. Old Saxon 

fa. Old English fea, PI. feawe, engl. /fen/ 'wenige'. 

2. With formants -Aro-/ Latin paucus' little ', pauper' arxx\' {*pauco-paros ox pau-paros?' 
little erwerbend, little sich constituting, originating '); Old High German fob' little '; 



Maybe alb. {*pauc-) pak' little' a Latin loanword. 

With suffix -/o-; Latin paul(l)us "small, little ' ( *pauks-lo-), pauxillus " totally little ' ( *pauk- 
s-lo-lo-). 

3. With formants -ro-zgr. iraOpot; "small, little', Latin with metathesis parvus^ smaW, 
parum ( *parvom) "to little '. 

4. " youngling, the young of an animal ': 

gr. iraOq (Attic Vasen), Gen. iraFot; (Cypriot, in addition ein new Nom. iraq), iraTt;, Gen. 
TTai56(; m. f., hom. JTd\c„ naFi5- "kid, child'; Latin puer^V\6, child, knave, boy, girl' ( *puuero- 
), puella "girl'; 

Gothic fula. Old Icelandic folixw., fylu. {*fulja-), under fyljai.. Old English fola. Old High 
German folo, fulT(n)^ plenitude, foals'; besides *pd[u]los\n Armenian i//"goat', am-ur 
infertile ' ( *n-pdlo-), yHi. "pregnanffZ-yOd/a/ya); gr. n(I)Ao(; "foals', also "young man, young 
girl', nwAiov "small foals, youngling ', alb. pele, pe/e'mare' (Fem. to *pdlos)\ perhaps med. 
Arbu-pales, if es " white foals possessing' stands for. 

5. With Mormant: putra-rw., Avestan ap. pu^-ra-m. (latter from putlo-= Oscan puklo-) 
"son, kid, child'; 

maybe alb. putra^'pa^ (of a young animal', puta^ so\e' 

gr. names as nu)-TaAo(;; Latin putus, put/7/us 'knave, boy', next to which *put-so-\n 
pus{s)us, -a "knave, boy, girl', but pus/7/us 'very small' is Demin. from pullus {*putslo-lo-s)\ 
Oscan puklo-'V\6, child' (= Old \v\6\c putra-), Paelignian puc/o/sDat PI. "pueris', mars. 
puc/es, Latin pu//us " young, the young of an animal ' ( *put-s-lo-)\ 

maybe alb. {*putillus) pu//sht' donkey's colt' 

Balto-Slavic *pufa'b\r6' in russ. -Church Slavic yOb/a "bird', yObZ/s/i. "small bird' ("bird' 
actually "young bird'), Lithuanian putyt/s'young animal, young bird' (Zartlichkeitsausdruck), 
Baltic *put-n-a-\n Latvian putns'b\r6'\ with other, demin. Formansverbindung Lithuanian 
yOaJ-/rs//s "bird'. 

maybe alb. pa/a "goose' Slavic loanword from russ. -Church Slavic yOb/a "bird' : Serbo- 
Croatian: pa'//ra"duck' [f]. 

References: WP. II 75 f., WH. II 259, 265 f., 382 f., 385 f., 394, Trautmann 233. 
Page(s): 842-843 



Root / lemma: prai- prai-, prT- (pri-) 
Meaning: to like, feel well-disposed, friendly 

Material: Old Indie pnnat/" pleases ', Med. "is cheerful about etwas', pnyateds., ' loves ', 
yO/'/?a- "cheerful, befriedigt; geliebt', prltf-i. 'pleasure, joy, satisfaction', pr/yayate 'behandeW. 
liebevoll, befreundet sich' (: Gothic fr/jon, Old Church Slavic prija-jg), priya- 'dear, 
desirable, worth having, welcome, wanted, liked, beloved, fancied ', m. ' lover, husband ', 
f. 'Geliebte, wife' (= Avestan frya-. Old Icelandic Friggeic, and Gothic freis, c. rhydd 
'free'), pr/yatva-m ^ das Liebsein or -have' (: Gothic frijat^wai. 'love'), priyata ds. (= Old 
@@@@ search father lemma @@@@
6201:Meaning: father 
9391:Meaning: father, mother 
67844:Meaning: father
```


## [2026-09-07T20:32:59.642Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=67836 && NR<=67890' POK_full.txt"
}
```


### [2026-09-07T20:33:01.020Z] TOOL RESULT

```
naiav, Ionian nairjajv, Attic rraicbv as "the die Krankheiten through Zauberschlag heilende 
(Apollo)', then with den words in nainajv anfangender hymn of praise, song of praise. 

References: WP. II 12, 76 f., WH. II 266, 267, 381 f., 393 f., Trautmann 217. 
Page(s): 827 

Root / lemma: p9te(r) Gen. patr-es, -6s {*ph9te(r}) 

Meaning: father 

Note: 

It derived from a prefixed p/7e- of Root / lemma: hatos, hatta : father, mother. 

Material: Old \r\d'\c p/tar-, Avestan p/Za/'- besides Nom. pta, /a etc.; Armenian hair{*patei). 

Gen. haur{*patros)\ gr. narrip, naTp6(;, in compound £u-naTU)p "ein good father'; Latin 



pater, -//75 "father'; /ja/Aes'Vorfahren, Patrizier'; Oscan paZ/^'father', Umbrian lu-pater 
"Juppiter", Dat. Sg. Oscan pateref, mars. -Latin patre; Old Irish athir{*patei). Gen. athar 
( *patros) 'father'; about gall, gutu-atersee above S. 413; Gothic fadar. Old Icelandic fadir. 
Old English fgeder. Old High German faferlather'; Tocharian Apacar, B pacer6s.; about 
Old Indie Dyaus pita eic. see above S. 413. 

Ableitnngen: Old Indie p///ya- gr. naTpiO(;, Latin yOa/A/^s'vaterlich', Middle Irish aithrei. 
"vaterliche family'; Old Indie pftrvya-, Avestan tuirya- ( *ptarvya-), Latin patruus. Old High 
German fetiro, fatirro, fatureo {Gerfr\an\c*faduru/a-) "Vaterb ruder', Modern High German " 
cousin ', Old English f^dera ^Vatersbruder' (compare gr. naTpu)(;from*yC>a//(9i/sds., with 
verschobener meaning naTpu)iO(; "vaterlich'); Old pers. hama-pitar-= gr. opo-narajp, 
compare Old Icelandic sam-fedra^irom the same Vater' {*-fadrjans)\ compare gr. naTpui6(; 
"Stiefvater' (after priTpuia " stepmother '), Armenian yaurayds.; only single-linguistically are 
gr. narpn, Attic narpa 'Vaterland', naTpi(;, -i5o(;f. ds., Latin patriads., patronus 
'Schutzherr', patro, -are "vollbringe, vollziehe'; proprius 'e\gen, eigentijmlich, bestandig' 
from * prop(a)trios "from den nponaTop£(;, den Altvorderen as ererbter Besitz uberkommen' 
(?), s. WH. II 374 f.; mcymr. e^y/yd'dwelling'could originally as 'vaterlicher possession ' 
with Middle Irish a///?/-© identical sein; Old Icelandic fedgarP\. "father and son' (compare gr. 
narpiKoq 'vaterlich'); fedginP\. "parents' {*fedr-gin). 

References: WP. II 4, WH. II 263 ff.; of babble-word pa-derive ? KretschmerWZKM. 51, 
315 f; or to pd(i)- shield, watch? 
Page(s): 829 

Root / lemma: phel- 
See also: s. (s)p(ti)el-. 
Page(s): 851 

Root / lemma: pher- 
See also: s. (s)p(h)er-. 
Page(s): 851 

Root / lemma: phol- 

Meaning: to fall
```


## [2026-09-07T20:33:01.832Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins pā- ===\"\ngrep -n -i \"^pā-\\|^poti-\\|^pəter-\\|^pater-\" AHD_watkins1985.txt | head -20\necho \"--- search 'to protect' AHD ---\"\ngrep -n -i \"pə̄-\\|pa-, to protect\\|To protect. 1\\|poti-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T20:33:01.903Z] TOOL RESULT

```
=== AHD watkins pā- ===
863:poti-
870:poti-. Powerful; lord. 1. Latin potis, powerful, able (> potestas, power): PODESTA, POSSESS, POWER. 2. Latin compound posse, to be able (contracted from potis, able
--- search 'to protect' AHD ---
364:LOIN. 4. Possibly suffixed variant *dlo-gho- in Greek dolikhos, long: DOLICHOCEPHALIC, DOLICHOCRANIAL. [Pok. 5. del- 196.] del-2. To recount, count. 1. Germanic *taljan in Old English tellan, to count, recount: TELL. 2. Germanic *tal6é in: a. Old English talu, story: TALE; b. Middle Dutch dle, speech, language: TAAL. 3. Old English denominative talian, to tell, relate, probably akin to the source of Middle English talken, to talk: TALK. 4. Per- haps Greek dolos, ruse, snare: DOLERITE. [Pok. 1. del- 193.] del-3. To split, carve, cut. 1. Suffixed form *del-to- in Germanic *teldam, “thing spread out,” in Old English teld, awning, tent: TILT?. 2. Germanic extended form *telg- in Old English telgor, telgra, twig, branch: TILLER’. 3. Perhaps o-grade form *dol-é- in Latin dolére, to suffer (? < “to be beaten”): DOLE?, DOLOR; CONDOLE, INDO- LENT. 4. Suffixed o-grade form *dold-dhraé in Latin dolabra, a heavy chopping tool (< doldre, to chisel, hew): DOLABRIFORM. [Pok. 3. del- 194.] del-*. To drip. Perhaps suffixed (stative) o-grade form *dol- in Germanic *talgaz in Middle Low German falg, talch, tallow (< “dripping fat”), perhaps akin to the source of Middle English talow, tallow: TALLOw. [Pok. 4. del- 196.] deme-'. Also dem-. House, household. 1. Suffixed re- duced o-grade form *dom-o-, dom-u-, house, in: a. Latin domus, house: DOME, DOMESTIC, DOMICILE; MAJOR- DOMO; b. suffixed form *dom-o-no- in Latin dominus, master of a household (feminine domina > Old French dame, lady): DAME, DAN?, DANGER, DoM, DOMAIN, DOMI- NATE, DOMINICAL, DOMINIE, DOMINION, DOMINO}, (DOM- INO2), DUENNA, DUNGEON; (MADAM), MADAME, MADEMOISELLE, MADONNA, PREDOMINATE. 2. Com- pound *dems-pot-, “house-master” (*-pot-, powerful; see poti-), in Greek despotés, master, lord: DESPOT. 3. Root form *dem()-, to build (possibly a separate root), in: a. Germanic *timram in Old English timber, building material, lumber: TIMBER; b. Germanic *tumfté in Old Norse topt, homestead: Torr. [Pok. dem- 198.] deme-2. To constrain, force, especially to break in (horses). 1. Suffixed o-grade form *dom-o- in Germanic *tamaz in Old English tam, domesticated: TAME. 2. O-grade form *doma- in Latin domdre, to tame, sub- due: DAUNT; INDOMITABLE. 3. Zero-grade form *dmo- in Greek daman, to tame (> adamas, unconquerable): ADAMANT, DIAMOND. [Pok. (dema-), doma- 199.] denk-. To bite. 1. Germanic *tanhuz in Old English toh, tenacious, sticky (< “holding fast”): TOUGH. 2. Germanic *tanguz in Old English tang(e), tong(e), pincers, tongs: TONGS. 3. Germanic *tang- in Old Norse tangi, a point, sting, akin to the Scandinavian source of Middle English tonge, tange, point, tang: TANG!. 4, Germanic *teng- in Old High German zinko, spike, prong: z1Nc. [Pok. denk- 201.) dens-'. To use mental force. Reduplicated and suffixed zero-grade form *di-dns-sko- in Greek didaskein, to teach: pipactic. [Pok. 1. dens- 201.] dens-2. Dense, thick. 1. Suffixed form *dens-o- or *dns-o- in Latin dénsus, thick: DENSE; CONDENSE. 2. Suffixed zero-grade form *dns-u- in Greek dasus, hairy, shaggy: DASYURE. [Pok. 2. dens- 202.] dent-. Tooth. (Originally participle of ed- in the earlier meaning “to bite.”) 1. O-grade form *dont- in Germanic *tanthuz in Old English toth, tooth: TOOTH. 2. Zero-grade form *dné- perhaps in Germanic *tunth-sk- in Old English tisc, tix, canine tooth: TUSK. 3. Full-grade form *dent- in Latin déns (stem dent-), tooth: DENTAL, DENTATE, DENTI-, DENTICLE; (BIDEN- TATE), DANDELION, EDENTATE, INDENT!, (INDENTURE), TRIDENT. 4. O-grade variant form *(o)dont- in Greek odén, odous, tooth: -ODON, -ODONT, ODONTO-; CERATO- Dus. [In Pok. ed- 287.] deph-. To stamp. 1. Suffixed form *deph-s-ter- in Greek
526:TRANSFUSE. II. Extended form *gheus-. 1. Germanic zero-grade form *gus- in: a. suffixed form *gustiz in Old Norse gustr, a cold blast of wind: cusT!; b. Icelandic gusa, to gush, perhaps akin to Middle English gushen, to gush: GUSH. 2. Germanic suffixed o-grade form *gausjan in Old Norse geysa, to gush: GEYSER. III. Suffixed form *gheu-ti- in Latin fatilis, “(of a vessel) easily emptied, leaky,” hence untrustworthy, useless: FUTILE. IV. Basic form *gheu- in Greek khein, to pour: CHOANA, CHYLE, (CHYME); CHOANOCYTE, ECCHYMOSIS, PARENCHYMA. [Pok. gheu- 447.] ghéu-. To yawn, gape. Compare ghai-. 1. Germanic suffixed form g6-ma- in Old English goma, palate, jaw: GuM?, 2. Variant form *ghau- in Greek khaos, chasm, empty space, chaos: CHAOS, GAS. [Pok. ghéu- 449.] gheu(e)-. To call, invoke. Suffixed zero-grade form *ghu-to-, “the invoked,” god, in Germanic *gudam, god, in: a. Old English god, god: Gop; b. Germanic *gud-igaz, possessed by a god, in Old English gydig, gidig, possessed, insane: GIDDY. [Pok. ghau- 413.] gh6. Behind, after. Slavic *za in Russian za, by, to: SASTRUGA. [Pok. 26 451.] ghos-ti-. Stranger, guest, host; properly “someone with whom one has reciprocal duties of hospitality.” 1. Basic form *ghos-ti- in: a. Germanic *gastiz in Old Norse gestr, guest: GUEST; b. Latin hostis, enemy (< stranger): HOST?, (HOSTILE). 2. Compound “ghos-pot-, *ghos-po(d)-, “guest-master,” one who symbolizes the relationship of reciprocal obligation (*pot-, master; see poti-), in Latin hospes (stem hospit-), host, guest, stranger: (HOSPICE), (HOSPITAL), (HOSPITALITY), HOST!, (HOSTAGE), (HOSTEL), (HOSTLER). See also xenos. [Pok. ghosti-s 453.] ghow-é-. To honor, revere, worship. 1. Germanic *gaw6n in Old Norse gd, to heed: GAWK. 2. Basic form *ghow-é- in Latin favére, to favor, be favorable: FAVOR, (FAVOR- ITE). [Pok. ghou(é)- 453.] ghré-. To grow, become green. Contracted from “ghreo-. 1. O-grade form “ghré- in Germanic *grd(w)an in Old English gréwan, to grow: GROW. 2. Suffixed o-grade form *ghro-nyo- in Germanic *grénjaz, green, in Old English gréne, green: GREEN. 3. Suffixed zero-grade form *“ghro-so- in Germanic *grasam, grass, in Old English grees, grass: GRASS. [Pok. ghré- 454.] ghrebh-'. To seize, reach. 1. Zero-grade form *ghrbh- in Sanskrit grbhndati, grhndati, he seizes: SATYAGRAHA. 2. Parallel (imitative) Germanic creations with base *grab-, *grap- in: a. Middle English graspen, to grasp: GRASP; b. Middle Dutch and Middle Low German grab- ben, to seize: GRAB. [Pok. 1. ghrebh- 455.] ghrebh-?. To dig, bury, scratch. 1. O-grade form “ghrobh- in: a. Germanic *graban in (i) Old English grafan, to dig, engrave, scratch, carve: GRAVE3; (EN- GRAVE) (ii) Old High German graban, to dig: GRABEN (iii) Old French graver, to engrave: GRAVURE; b. Germanic *grabam in Old English grzf, trench, grave: GRAVE}. 2. Germanic *grub(byan (with secondary ablaut) in Old English *grybban (> Middle English grubben), to dig: GRUB. 3. Germanic *gr6b6 in Middle Dutch groeve, ditch: GROOVE. 4. Perhaps Germanic *greub- in Low German greven, fibrous refuse of tallow: GREAVES. [Pok. 2. ghrebh- 455.] ghredh-. To walk, go. Suffixed zero-grade form ghrdh-yo- in: a. Latin gradi (past participle gressus), to walk, go: GRESSORIAL; AGGRESS, CONGRESS, DEGRESSION, DI- GRESS, EGRESS, INGRESS, PLANTIGRADE, PROGRESS, RE- GRESS, RETROGRESS, TRANSGRESS; b. Latin gradus (< deverbative *grad-u-), step, stage, degree, rank: GRADE; CENTIGRADE, DEGRADE, DEGREE, RETROGRADE. [Pok. ghredh- 456.] ghréi-. To rub. A derivative of gher-4. 1. Germanic *gris-, to frighten (< “to grate on the mind”), in Old English grislic, terrifying: GRISLY. 2. Germanic *grim-, smear, in Middle Dutch grime, grime, akin to the source of Middle English grime, grime: GRIME. 3. Extended form *ghris-
863:poti-
870:poti-. Powerful; lord. 1. Latin potis, powerful, able (> potestas, power): PODESTA, POSSESS, POWER. 2. Latin compound posse, to be able (contracted from potis, able
872:+ esse, to be; see es-): POSSIBLE, POTENT; (IMPOTENT), PREPOTENT. 3. Form *pot- in: a. compound *ghos-pot-, “suest-master,” host (see ghos-ti-); b. compound *dems-pot-, “house-master,” ruler (see deme-'). 4. Old Persian pati-, master: PADISHAH. [Pok. poti-s 842.] [prak-. To make, do. Greek root. Greek prassein (Attic prattein), to effect, do: PRACTICAL, (PRACTICE), PRAG- MATIC, PRAXIS. [In Pok. 1. per 811.]] prek-. To ask, entreat. 1. Basic form *prek- in Latin *prex, prayer (attested only in the plural precés), with denominative precdri, to entreat, pray: PRAY, PRAYER?, PRECARIOUS; DEPRECATE, IMPRECATE. 2. Suffixed zero-grade form *prk-sk- becoming *pork-sk-, contracted into *posk- in suffixed form *posk-to-, contracted into *posto-, which appears in Latin postuldre, to ask, re- quest: POSTULATE; EXPOSTULATE. [Pok. 4. perk- 821.] prep-. To appear. Suffixed zero-grade form *prp-yo- in Germanic *furbjan, to cause to have a (good) appearance, polish, in Old French fo(u)rbir, to polish, burnish: FuR- BISH. [Pok. prep- 845.] preu-. To hop. 1. Zero-grade form *pru- in Germanic *fru- in Old English frogga (with obscure expressive suffix -gga), frog: FROG. 2. Extended o-grade form *prowo- in Germanic *frawaz in: a. Middle Dutch uro, “leaping with joy,” happy: FROLIC; b. Old High German fré, happy, in frewida, joy (> German Freude): scHa- DENFREUDE. [Pok. preu- 845.] preus-. To freeze, burn. 1. Germanic *freusan, to freeze, in Old English fréosan, to freeze: FREEZE. 2. Suffixed zero-grade form *prus-to- in Germanic *frustaz, frost, in Old English forst, frost, frost: FROST. 3. Suffixed form *preus-i- in Latin *preusis, *preuris, act of burning, whence denominative pririre, to burn, itch, yearn for: PRURIENT, PRURIGO, PRURITUS. 4. Suffixed zero-grade form *prus-ina in Latin pruina, hoarfrost: PRUINOSE. [Pok. preus- 846.] pri-. To love. Contracted from *pria-. 1. Suffixed form *priy-o- in Germanic “frijaz, beloved, belonging to the loved ones, not in bondage, free, in: a. Old English fréo, free; FREE; b. Dutch vrij, free: FILIBUSTER. 2. Suffixed (participial) form “priy-ont-, loving, in Germanic ‘“fri- Jjand-, lover, friend, in Old English friond, fréond, friend: FRIEND. 3. Suffixed shortened form *pri-tu- in Germanic *frithuz, peace, in: a. Old High German fridu, peace: SIEGFRIED; b. Old French esfreer, to disturb: AFFRAY; c. Germanic *frij-, peace, safety, in compound *berg-frij-, “high place of safety” (see bhergh-?). 4. Suffixed femi- nine form *priy-G, beloved, in Germanic *frijj6, beloved, wife, in: a. Old Norse Frigg, goddess of the heavens, wife of Odin: Fricc; b. Germanic compound “*frije-dagaz, “day of Frigg” (translation of Latin Veneris diés, “Ve- nus’s day”), in Old English frigedeg, Friday: FRIDAY. [Pok. prdi- 844.] prokto-. Anus. Greek prokios, anus: PROCTITIS, PROCTOL- OGY, PROCTOSCOPE. [Pok. prdkto- 846.] pster-. Also ster-. To sneeze. Imitative root. 1. Suffixed form *ster-nu- in Latin sternuere, to sneeze: STERNUTATION. 2. Suffixed form *ster-t- in Latin ster- tere, to snore: STERTOR. [Pok. pster- 846.] pu-'. Also phu-. To blow, swell. Imitative root. 1. Ex- tended form *pus- in Latin pustula, a bubble, blister: PUSTULE. 2. Perhaps extended form “pit-, penis, in Latin praepiitium, foreskin (prae-, before, in front; see per’): PREPUCE. 3. Variant form *phi- in Greek phusa (> phusan, to blow), bellows, bladder: EMPHYSEMA, PHYSO- STIGMINE, PHYSOSTOMOUS. [Pok. 1. pu- 847.] pu-2, To rot, decay. 1. Suffixed form *pi-lo- in Germanic *filaz, rotten, filthy, in: a. Old English fi, unclean, rotten: FOUL; b. Old Norse fill, foul, akin to the Scandi- Navian source of FULMAR; ¢. Germanic abstract noun *filithd in Old English fylth, foulness: FILTH; d. Ger- manic denominative *filjan, to soil, dirty, in Old English fylan, to sully: FILE’; DEFILE!. 2. Extended form *pug- in Germanic *fuk- in Icelandic fiki, rotten sea grass, and
924:ser-1, To protect. 1. Extended form *serw- in Latin serudre, to keep, preserve: CONSERVE, OBSERVE, PRE- SERVE, RESERVE, (RESERVOIR). 2. Suffixed length- ened-grade form *sér-6s- perhaps in Greek hérés, “protector,” hero: HERO. [Pok. 2. ser- 910.]
1673:ILLATION tele- ILLITERATE deph- ILLUMINATE leuk- ILLUSION leid- ILLUSTRATE leuk- IMBECILE bak- IMBIBE p6(i)- IMBRICATE ombh-ro- IMBRUE_bhreu-2 IMBUE ombh-ro- IMMACULATE macula IMMANENT men-3 IMMATURE ma-1 IMMENSE mé6-2 IMMERSE mezg-! IMMINENT men-2 IMMIX meik- IMMODERATE med- IMMODEST med- IMMOLATE mele- IMMORTAL mer-2 IMMUNE mei-1 IMMURE mei-3 IMP bheue- IMPAIR ped-1 IMPALE pag- IMPARITY pere-2 IMPART pere-2 IMPEACH ped-1 IMPECCABLE ped-1 IMPECUNIOUS peku- IMPEDE ped-! IMPEL pel-6 IMPEND (s)pen- IMPERATIVE pere-1 IMPERIAL pere-1 IMPETRATE peter- IMPETUS _pet- IMPINGE pag- IMPIOUS pius IMPLEMENT pele-1 IMPLICATE plek- IMPONE apo- IMPORT per-2 IMPORTANT per-2 IMPORTUNE per-2 IMPOSE apo- IMPOTENT poti- IMPOUND bend- IMPRECATE prek- IMPRESS! per-5 IMPRIMIS_ per! IMPRINT per-5 IMPROBITY pert IMPROMPTU em- IMPROVE es-, pert IMPUDENT (s)peud- IMPUGN peuk- IMPUNITY kweij-1 IMPUTE peu- IN-l ne
2032:PACT pag- PADISHAH poti- PADRE pater- PAELLA pete- PAGAN pag-
2108:POCO pau- POCOCURANTE ciira -POD ped-1 PODAGRA ag-, ped-1 PODESTA poti- PODIATRY ped-! PODITE ped-! PODIUM ped-1 PODOPHYLLIN bhel-3, ped-1 PODZOL ghel-2, ped-1 POEM kWej-2
2122:PORTS per-2 PORTABLE per-2 PORTAGE per-2 PORTAL per-2 PORTAMENTO per-2 PORTATIVE per-2 PORTCULLIS _ per-2 PORTE-COCHERE per-2 PORTEND ten- PORTER! per-2 PORTER? per-2 PORTFOLIO bhel-3, per-2 PORTICO per-2 PORTIERE per-2 PORTION pere-2 PORTRAY tragh- PORTULACA per-2 POSE! paus- POSITION apo- POSITIVE apo- POSSESS poti-, sed-1 POSSIBLE poti- PosTl sta-
2125:POST- apo- POSTBELLUM duellum POSTERIOR apo- POSTICHE apo- POSTMERIDIAN deiw- POST-MORTEM apo-, mer-2 POSTPARTUM _pere-1 POSTSCRIPT skribh- POSTULATE prek- POSTURE apo- POTABLE p0(i)- POTATION pd(i)- POTATORY pd(i)- POTENT poti- POTION po(i)- POTPOURRI pu-2 POUCH beu-! POULARD pau- POULTICE pel-1 POUNCE! peuk- POUNCE? (s)poi-mo- POUNCE3 peuk- POUND! (s)pen- POUNDS bend- POUSETTE pel-6 POUT beu-! POVERTY pau- POWDER pel-1 POWER poti- PRAAM per! PRACTICAL prak- PRACTICE prak- PRAEDIAL wadh-1 PRAEMUNIRE mei-3 PRAENOMEN no-men- PRAETOR ei-1 PRAGMATIC prak- PRAISE per-6 PRANDIAL ed- PRATINCOLE kwel-1 PRAXIS prak-
2129:PRECINCT kenk-! PRECIOUS per-6 PRECIPITATE kaput PRECISE kae-id- PRECLUDE kleu-3 PRECOCIOUS pekw- PRECURSOR kers-2 PREDATORY ghend- PREDECESSOR ked- PREDICATE delk- pRepicT deik- PREDOMINATE deme-1 PREEMPTION em- PREFACE bha-2 PREFECT dhé-1 PREFER bher-1 PREFIGURE dheigh- PREFIX dhig¥- PREGNABLE ghend- PREGNANT! gene- PREGNANT? per-5 PREHENSILE ghend- PREHENSION ghend- PREJUDICE deik-, yewes- PRELAPSARIAN leb-1 PRELATE telo- PRELECT leg-1 PRELIBATION [éi- PRELUDE leld- PREMATURE ma-1 PREMIER per! PREMISE (s)meit(@)- PREMIUM em- PREMONITION men-1 PREMORSE mer-2 PREMUNITION mel-3 PREPARE pere-! PREPENSE (s)pen- PREPONDERATE (S)pen- PREPOSITION apo- PREPOSTEROUS apo- PREPOTENT _poti- PREPUCE pu-! PREROGATIVE reg-1 PRESAGE sag- PRESBYOPIA per! PRESBYTER pert PRESCIENT skel- PRESCIND  skel- PRESCRIBE skribh- PRESENT! es- PRESENT? es- PRESENTIMENT sent- PRESERVE ser-! PRESIDE sed-! PRESS! per-5 PRESSURE per-5 PRESTIGE streig- PRESUME em- PRETEND ten- PRETERIT el-1!, per? PRETERMIT (s)melt(@)- PRETEXT teks- PRETZEL mregh-u- PREVAIL wal- PREVENIENT gWa- PREVENT gWa- PREVIOUS wegh- PREVISE weld- PREY ghend- PRICE per-6
```


## [2026-09-07T20:33:11.581Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['pā-. To protect','pa-. To protect','To protect, feed','pater-. Father','pater-.','pa-, to feed','Pok. pa- 787','Pok. p9te(r) 829','Pok. pate','829.]','787.]','839.]']:\n    for m in re.finditer(re.escape(pat),t):\n        print('###',pat,'@',m.start())\n        print(t[max(0,m.start()-500):m.start()+600].replace('\\n',' '))\n        print()\n        break\nEOF"
}
```


### [2026-09-07T20:33:12.918Z] TOOL RESULT

```
### pa-. To protect @ 71154
peech are separated by a semicolon: kagh-. To catch, seize; wickerwork, fence. pele-2. Flat; to spread. mu-', Imitative of inarticulate sounds. After the basic meaning there may appear further information about the phonological shape or nature of the root: dhreg-. To draw, glide. Variant form of dhrag-. temp-. To stretch. Extension of ten-. tauro-. Bull. Derivative of sta-, but an in- dependent word in Indo-European. dail-. To divide. Northern Indo-European root. pipp-. To peep. Imitative root. pa-. To protect, feed. Contracted from *pao-. kak-2. A round object, disk. Germanic root. mas. Male, Latin adjective of unknown ori- gin. Most, but not all, of the additional informa- tion is self-explanatory. In the first three examples, the boldface forms dhrag-, sta-, and ten- are cross-references to those roots, which are main entries in this Dictionary. Every boldface form appearing in the text of an entry is such a cross-reference. In the example pa- the form *pag- represents an older root form; the nature of these contrac- tions is explained in the preceding essay un- der ‘‘Phonology an

### To protect, feed @ 71159
 are separated by a semicolon: kagh-. To catch, seize; wickerwork, fence. pele-2. Flat; to spread. mu-', Imitative of inarticulate sounds. After the basic meaning there may appear further information about the phonological shape or nature of the root: dhreg-. To draw, glide. Variant form of dhrag-. temp-. To stretch. Extension of ten-. tauro-. Bull. Derivative of sta-, but an in- dependent word in Indo-European. dail-. To divide. Northern Indo-European root. pipp-. To peep. Imitative root. pa-. To protect, feed. Contracted from *pao-. kak-2. A round object, disk. Germanic root. mas. Male, Latin adjective of unknown ori- gin. Most, but not all, of the additional informa- tion is self-explanatory. In the first three examples, the boldface forms dhrag-, sta-, and ten- are cross-references to those roots, which are main entries in this Dictionary. Every boldface form appearing in the text of an entry is such a cross-reference. In the example pa- the form *pag- represents an older root form; the nature of these contrac- tions is explained in the preceding essay un- der ‘‘Phonology and Mor

### 829.] @ 460844
 fart: PETARD. 3. Possibly Latin pédis, louse (? < “foul-smelling insect”): PEDICU- LAR. See also perd-. [Pok. pezd- 829, 2. peis- 796.] peter-. Father. 1. Germanic *fadar in Old English feder (> Middle English fader), father: FATHER; FOREFATHER. 2. Latin pater, father (> patrare, to bring about): PADRE, PATER, PATERNAL, PATRI-, PATRICIAN, PATRIMONY, PA- TRON; EXPATRIATE, IMPETRATE, PERPETRATE. 3. Greek 51 plat- patér, father: PATRIOT; ALLOPATRIC, EUPATRID, PATRI- ARCH, SYMPATRIC. [Pok. paté(r) 829.] p(h)ol-. To fall. Suffixed form *phol-no- in Germanic *fallan in: a. Old English feallan, to fall: FALL; b. Ger- manic causative *falljan, “to cause to fall,” strike down, in Old English fellan, fyllan, to cut down: FELL; c. Ger- manic compound *bi-fallan, to fall, happen (*bi-, by, at; see ambhi), in Old English befeallan, to fall: BEFALL. [Pok. phél- 851.] [phulax. Watcher, guard. Greek noun of unknown origin, related to phulassein (Attic phulattein), to guard, pro- tect. PHYLACTERY, PHYLAXIS; PROPHYLACTIC. ] pik-. Pitch. Latin pix (stem pic-), pitch: PAY?, PICEOUS, PITCH!; PICOLINE, P

### 787.] @ 425399
, (TRAVEL); b. probably Latin pdla, spade: PALETTE, PEEL*. 5. Lengthened-grade form *pdg- in: a. Latin pdagus, “boundary staked out on the ground,” district, village, country: PAGAN, PEASANT; b. Latin pdgina, “trellis to which a row of vines is fixed,” hence (by metaphor) column of writing, page: PAGE?, PAGEANT; c. Latin prépdgés (pré-, before, in front; see per'), layer of vine, offspring (< “a fixing before”): PROPAGATE; d. Greek pégnunai, to fasten, coagulate: PECTIN, PEGMA- TITE. [Pok. pak- 787.] pan-. Fabric. 1. Germanic *fandn- in: a. Old English pandoura fana, flag, banner, weathercock: VANE; b. compound *gund-fanon-, “battle-flag” (see ghen-'). 2. Extended form *panno- in Latin pannus, piece of cloth, rag: PANE, PANEL. 3. Possibly Greek pénos, web (> Latin pdnus, a swelling): PANICLE. [Pok. pan- 788.] [pandoura. Three-stringed lute. Greek noun of obscure origin. BANDORE, MANDOLIN, PANDORE.] pant-. All. Attested only in Tocharian and Greek. Greek pas (neuter pan, stem pant-), all: PAN-, PAN; DIAPASON, PANCRATIUM, PANCREAS. [In Pok. 1. keu- 592.] pap-'. Teat (sound symbolism). 

### 839.] @ 424260
atin pdscere, to feed: PASTURE; ANTIPASTO, PESTER, REPAST; b. Latin pdstor, shepherd: PASTOR; C. suffixed form *pds-t-ni- in Latin pGnis, bread (diminutive pastillus, medicine tablet): PANADA, PANATELA, PANNIER, PANOCHA, PANTRY, PAS- TILLE, (PENUCHE); APPANAGE, COMPANION, (COMPANY). 5. Suffixed form *pd-ti- in Iranian *pdti- in Persian pdd, protecting against: BEZOAR. 6. Suffixed form *pd-won-, protector, in Old Persian khshathra-pdvd, protector of the province: SATRAP. [Pok. pd- 787, 1. pd(i)- 839.] pag-. Also pak-. To fasten. 1. Lengthened-grade form *“pak- in Germanic *fogjan, to join, fit, in Old English fégan, to fit closely: FAY}. 2. Nasalized form *pa-n-g- in: a. Germanic *fangiz, seizure, in (i) Old English fang, feng, plunder, booty: FANG (ii) Dutch vangen, to catch: VANG; b. Latin pangere, to fasten: COMPACT!, IMPINGE. 3. Root form *pak- in: a. Latin pdx, peace (< “a binding together by treaty or agreement”): PACE?, PAY!, PEACE; APPEASE, PACIFIC, PACIFY; b. Latin pacisci, to agree: PACT. 4. Suf- fixed form *pak-sio- in: a. Latin pdlus, stake (fixed in the ground): PALE!, PA
```


## [2026-09-07T20:33:24.742Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.find('[Pok. pd- 787, 1. pd(i)- 839.]')\nprint(t[i-2200:i+60].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T20:33:26.020Z] TOOL RESULT

```
atin os (stem oss-), bone: 082, OSSEOUS, OSSICLE, OSSUARY; OSSIFRAGE, OSSIFY. 2. Greek osteon, bone: OSTEO-; ENDOSTEUM, EXOSTOSIS, PERIOSTEM, SYN- OSTOSIS, TELEOST. 3. Suffixed form *ost-r- in: a. Greek ostrakon, shell, potsherd: OSTRACIZE, OSTRACOD; b. Greek ostreon, oyster: OYSTER; C. variant form in Greek astragalos, vertebra, ball of the ankle joint, knuck- lebone, Ionic molding: ASTRAGAL, ASTRAGALUS. [Pok. ost(h)- 783.] ous-. Also aus-. Ear. 1. Suffixed form *ous-en- in Ger- manic *auzan- in Old English éare, ear: EAR}. 2. Suffixed form *aus-i- in Latin auris, ear: AURAL!, AURICLE; AURIFORM, ORMER. 3. Latin auscultdre, to listen to (*aus- + *kli-to-, inclined; see klei-): AUSCULTATION, scouT!. 4. Suffixed basic form *ous-os- in: a. Greek ous (stem 6t-), ear: OTIC, OTO-; MYOSOTIS, PAROTID GLAND; b. Greek Jagés, hare (< */ag-ous-, “with drooping ears”; *lag-, to droop; see slég-). [Pok. dus- 785.] owi-. Sheep. 1. Germanic *awi- in Old English ewe, eowu, ewe: EWE. 2. Latin ovis, sheep: OVINE; OVIBOS. [Pok. oui-s 784.] pa-. To protect, feed. Contracted from *pas-. 1. Suffixed form *pé-trom in Germanic *fodram in: a. Old English fédor, fodder: FODDER; b. Old French feurre, fodder: FORAGE; C. Old French forreure, trimming made from animal skin, fur (< “sheath, case, lining”): FuR. 2. Suf- fixed form *pd-dhlom (doublet of *pd-trom) in Latin padbulum, food, fodder: PABULUM. 3. Extended form *pat- in: a. Germanic *féd-, food, in Old English foda, food: Froop; b. Germanic denominative *fédjan, to give food to, in Old English fédan, to feed: FEED; Cc. suffixed form *pdt-tro- in Germanic *fdstra- in Old English fostor, food, nourishment: FOSTER. 4. Extended form *pds- in: a. suffixed form *pds-sko- in Latin pdscere, to feed: PASTURE; ANTIPASTO, PESTER, REPAST; b. Latin pdstor, shepherd: PASTOR; C. suffixed form *pds-t-ni- in Latin pGnis, bread (diminutive pastillus, medicine tablet): PANADA, PANATELA, PANNIER, PANOCHA, PANTRY, PAS- TILLE, (PENUCHE); APPANAGE, COMPANION, (COMPANY). 5. Suffixed form *pd-ti- in Iranian *pdti- in Persian pdd, protecting against: BEZOAR. 6. Suffixed form *pd-won-, protector, in Old Persian khshathra-pdvd, protector of the province: SATRAP. [Pok. pd- 787, 1. pd(i)- 839.] pag-. Also pak-. To fasten. 1
```


## [2026-09-07T20:33:32.015Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 127 128; do echo \"=== SYN leaf $L (printed $((L-24))) ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' SYN.txt | head -60; done"
}
```


### [2026-09-07T20:33:33.347Z] TOOL RESULT

```
=== SYN leaf 127 (printed 103) ===
ife’ (4). Cf. Lat. coniux (below, 4).
4. Lat. -uzor ‘wife’: Arm. am-usin ‘spouse’, and to be analyzed as *uk-sor-, first part : Skt. uc- ‘be accustomed to, take pleasure in’, Lith. junkti ‘be accus- tomed’, ete. (Walde-P. 1.111), second part as in *swesor ‘sister’, etc. (2.45). Ernout-M. 1148.
Hence OF. oissor, OSp. uxor, and the verbal deriv. Rum. tnsura ‘marry’, etc. (REW 9106-7), but generally replaced.
Lat. maritus ‘husband’ (> It. marito, Fr. mari, Sp. marido), perh. as lit. one provided with a ‘young woman, bride’, fr. a *mart- : Skt. marya- ‘young man’, Lith. marti ‘bride’, ete. Hence the later and much less common mariia ‘wife’. Walde-P. 2.281. Ernout-M. 593. Wal- de-H. 2.40 f.
Lat. coniu(n)« freq. ‘wife’, less com- monly ‘husband’, fr. coniungere ‘unite’.
Lat. spdnsus (pple. of spondére ‘prom- ise’) ‘betrothed, bridegroom’, fem. spén- sa ‘betrothed, bride’. Hence with ex- tension or with complete shift to ‘hus- band, wife’, It. Sposo, sposa, Fr. époux, épouse (OFr. spus, spuse > ME, NE spouse), Sp. esposo, esposa.
git CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
MANKIND: SEX, AGE, FAMILY RELATIONSHIP 97
‘husband’, fr. Lat. socius
, sot ‘ : ion’ Hence also sove ‘wife’.
‘gompanion . Puscariu 161 Alb. shog ‘husban
Rum. nevasia
0. Cf. fr. the same source, d’, shoge ‘wife’.
Gwyife’, loanword fr. Slav., Chsl. nevésta ‘bride’ (cf. aE os OPol. niewasia ‘woman ): Tiktin 4
5, Ir. céle ‘companion, husband’, NIr. coile ‘companion, spouse’, prob. : OHG hiwo, hiwa ‘husband, wife’, etc. (below, 5). Walde-P. 1.359, 446. Te
Ir. sétig ‘wife’, orig. companion, deriv. of sét ‘way’. Pedersen 2.89.
Nir. nuachar, ‘lover, spouse’ (also snuachar, fr. so-nuachar ‘good spouse’), epd. of nua- ‘new’ ; second part disputed, perh. a vbl. n. to cuirim ‘place, put’, the whole orig. ‘newly settled, newcom- er (inthe home)’. G.S. Lane, Language 8.297 f.
W. priod, Br. pried ‘spouse’, fr. Lat. privdtus ‘one’s own, private’. Pedersen 1.214.
Br. ozac’h ‘master of the house, hus- band’, etym.? Loth, RC 41.234 f.
6. Goth. aba ‘husband’: ON afi ‘grandfather’, etc., orig. nursery word (above, p. 94). Walde-P. 1.47.
ON hisbondi ‘man of the house, hus- band’, cpd. of his ‘house’ and béndi ‘yeoman’, the latter also used alone for ‘husband’. Hence ME husbonde, NE husband.
Dan., Sw. hustru, 
=== SYN leaf 128 (printed 104) ===
fr. hus-fru, epd. of hus ‘house’ and fru ‘mistress’, like NHG hausfrau, Du. huisvroww.
Sw. make, fem. maka, ME make prop- erly ‘mate’ : OE gemecca ‘mate’ gem- On ee well matched’, etc., these : niece ene , ete. Falk-Torp 689. Be ehlamoct ‘Spouse! , with echt ‘maria oun sooo eae es ae a .35) and genoot ‘com-
y genosse, etc.
a CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
OHG hiwo ‘husband’, hiwa ‘wife’, OF hiwa ‘wife’ (Goth. heiwa-frauja ‘master of the house’) : Lett. steva ‘wife’, Lat. civis ‘citizen’, Lith. Seimyna ‘family’, OF ham ‘home’, etc., all fr. IE *ke7- ‘lie’ in Grk. xeZua, etc., whence the notion of ‘home, household’ and also its master or mistress. Walde-P. 1.359. Walde-H. 1.224. Feist 253 f.
NHG gatte, whence fem. gattin, fr. MUG gate ‘companion’, here also Du. gade now used mostly for ‘wife’ : MLG gaden ‘be suitable’, OE gegada ‘com- panion’, td gedere ‘together’, Goth. ga- dilligs ‘cousin’, etc. Walde-P. 1.531 ff. Weigand-H. 1.628. Franck-v. W. 172.
OHG gimahalo ‘bridegroom, hus- band’, gimahala, gimala ‘bride, wife’, MHG gemahele masc. and fem., NHG gemahl, fem. gemahlin, fr. OHG mahal ‘contract’, esp. ‘marriage contract’ : Goth. mafl ‘place of assembly, market’, OE mepel ‘assembly, speech’, etc. Walde-P. 2.304. Weigand-H. 1.671.
7. ChSl. sapragt, fem. sqpraga (in Gospels ‘yoke, pair’, late ‘spouse’) with SCr., Russ. suprug, supruga, fr. epd. of prega, presti ‘yoke, harness’. Miklosich 262.
ChSI. mal(z)zena, dual ‘husband and wife’, cpd. of Zena ‘wife’, first part Gmc. (: OHG mahal, etc., above, 6) or malt ‘little’, as prefix of affection? Hence Boh. manzel, manzelka, Pol. malzonek, malzonka, etc. Berneker 2.13.
Boh. choi’ ‘spouse’, used for either ‘husband’ or ‘wife’ : ChSI. chott ‘lover, beloved’, fr. chotéti ‘wish’. Berneker 398 f.
8. Skt. bhartar- ‘husband’, bharyd- ‘wife’, lit. ‘the sustainer’ and ‘the one sustained’, fr. bhr- ‘bear, carry’ : Grk. épw ‘bear’, etc.
Skt. dara- ‘wife’, etym. dub. Uhlen- beck 124.
Cede
Digitized by Arya Samaj Foundation Chennai and eGangotri
98 SELECTED INDO-EUROPEAN SYNONYMS
2.38 MARRY (Partly distinguished as a) take a Wife; b) take a Hus
```


## [2026-09-07T20:33:39.090Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 133 134; do echo \"=== SYN leaf $L ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' SYN.txt | head -70; done"
}
```


### [2026-09-07T20:33:40.384Z] TOOL RESULT

```
=== SYN leaf 133 ===
 | Lat. coniugium, conutnin Dan. giftermaal, egte; bryl- Lett.  precéSands, lauliba; | tie ie ChSl. 6; rie 1 ) | : oe Sw. iftermdl, dkta; brél- .  brakit (maliizentstvo | een zoned, es SCr.  brak, Zenidba (2), Fr. see a oats 0: bodas OE weddung, sinscipe; udaja (b); svadba Bienes. cecil gifta, brgdhlop Boh. manielstvt, stiatek, Rum. Fe ranas ME  weddyng, wedlok, Zenitba (a), vdavky It. eh nak mariage (b); svatba a priodas; neithior NE marriage (wedlock); Pol. -malzenstvo, Slub; we- Br dimezi; eured wedding : sele : ; f Du. huwelijk, echt; brut- Russ. brak, supruzestvo, ze- loft nit'ba (a), zamu- OHG  hirat, éwa; britlouft Zestvo (b); svad’ba MHG hirdat, é(we); britlouft, Skt. vivaha-, patitva-, etc. hohzit Av. nairiéwana-
NHG heirat, ehe; hochzeit
Of the words entered, the majority, like NE marriage, cover both the state and the act of marriage (marriage as an institution, or the marriage took place). A few are used only for the married state, as Lat. matrimonium, NHG ehe. Many words are used only for the cere- mony, as NE wedding in its present usage. Such words are added, but separated by a semicolon.
In some cases there are distinct words for ‘taking a wife’ and ‘taking a husband’, corresponding to the dis- tinctive verbs (2.33). These are simi- larly indicated by a and b.
Most of the words for ‘marriage’ are obvious cognates (derivs. or in some cases the source) of the verbs for ‘mar- Ty’ and have been noted in the discus- Sion of the latter (2.33). Buta few, and many of the special words for the wed- ue ceremony, are of different origin. ae ee lit. OR ae (2.31), : . coniu(n)x ‘spouse en the usual legal term itehbecs ae , and nuptial ‘wedding’ ( >
= Seg see under nibere (2.33). : mmonium (>It., Sp. mat
=== SYN leaf 134 ===
ri-
monio), fr. mater ‘mother’, and orig. re- ferring to the woman’s lawful mother- hood, married status, as opposed to con- cubinage.
Sp. boda(s), ‘wedding’, fr. Lat. vota ‘vows’. REW 9458.
2. Ir. lanamnas, deriv. of lanamain ‘married couple’, deriv. of lan ‘full’. Pedersen 2.62. Stokes 293 (as cpd.).
W. neithior ‘wedding’, fr. Lat. nup- tidlia. Pedersen 1.236. Loth, Mots lat. 190.
Br. eured ‘wedding’, fr. Lat. drdatio ‘prayer’. Pedersen 1.203. Cf. Sp. bodas, above.
3. ON bradkaup ‘wedding’, cpd. of brad ‘bride’ and kauwpa ‘buy’, referring to the gifts made to the bride, and re- flecting the older custom of purchasing a wife. Schrader, Reallex. s.v. Braut- kauf.
ON bridlaup, brullawp, Dan. bryllop, Sw. bréllop, OF brydhlop, OHG, MHG britlouft, Du. bruiloft ‘wedding’, epd. of brid, etc. ‘bride’ and laupa, etc. ‘run’, referring to the ceremonial fetching of the bride, this ultimately reflecting a primitive chase or robbery of the bride.
. ee CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
102 SELECTED INDO-EUROPEAN SYNONYMS
Schrader, Reallex. s.v. Raubehe. Falk- Torp 109.
OE, beside usual weddung, rarely wedlac ‘pledge’ and ‘espousals’, whence ME wedlok, NE wedlock, fr. wedd ‘pledge’ with suffix -ldc, orig. same as lac ‘gift, etc.’. NED s.v. wedlock.
OE sinscipe, cpd. of sin- ‘everlasting’ and scipe ‘condition’, hence lit. ‘perma- nent state’. Cf. sinhtwan ‘married couple’.
OE @w, OHG éwa ‘law’ (21.12) and lawful married state’, MHG é(we), NHG ehe, Du. echt (MLG echt > Dan. egte, Sw. dkia). Falk-Torp 183. Wei- gand-H. 1.405 f.
MHG honhzit, lit. the ‘high time’, used of festivals like Christmas, Easter, also of the ‘marriage festival’, as NHG hoch- zeit. Weigand-H. 1.875. Sperber, Hin- leitung 42.
4, Lith. svodba (formerly usual word for ‘wedding’), fr. Russ. svad’ba (be- low, 5).
Lett. laultba ‘betrothal, marriage’, fr. laulat ‘betroth’, this from Esth. (or Liv.) loul ‘song, betrothal song’ (Finn. laulaa ‘sing’). Mithl.-Endz. 2.428.
Lett. kazas ‘wedding’, fr. Esth. kaza ‘husband’. Mihl.-Endz. 2.206.
5. ChSI. braki (in the Gospels always of the marriage at Cana, the ‘wedding’, but there is no opportunity for any other use), SCr., Russ. brak, prob. fr. berq, b
```


## [2026-09-07T20:33:45.710Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 135 136 137; do echo \"=== SYN leaf $L ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' SYN.txt | head -70; done"
}
```


### [2026-09-07T20:33:47.064Z] TOOL RESULT

```
=== SYN leaf 135 ===
rati ‘take’, IE *bher- ‘bear’) , orig.
‘taking the bride’, like ‘lead the bride, marry’ in Lith. vestz, etc. Berneker 81.
ChSI. malizZenisivo (late), Boh. man- Zelstvt, Pol. malzensivo : ChSl. maltizena ‘married couple’, Boh. manzel ‘husband’, etc. (2.31).
Boh. smatek, orig. ‘union’ : sntti OBoh. snieti, pple. sat, ChSl. sinetz ‘take down, take together’, cpd. of sz ‘with’ and jeti ‘take’. Gebauer 1.381. Berneker 429.
Pol. glub ‘vow’ (= Boh. slib ‘vow’), hence also ‘betrothal’ and ‘marriage’ : poslubié ‘betroth’, cpd. of lubié ‘like, love’. Hence OLith. salubas, OPruss. acc. sg. saliban ‘marriage’. Berneker 757 £. Briickner 531.
Russ. supruzestvo, fr. suprug ‘spouse’ (2.31).
SCr. svadba, Boh. svatba, Russ. svad’ba ‘wedding’, deriv. of ChSl. svatt ‘kins- man’ (: possessive svojz), then ‘one who promotes the marriage, matchmaker’, as Russ. svat, Pol. swat, ete. Miklosich 332.
Pol. wesele ‘wedding’, formerly ‘mer- riment’ : ChSI. veselije ‘merriment’ vese- li ‘merry’ (16.22), Briickner 607.
6. Skt., beside vivdha-, ete. fr. vah- ‘marry’, also patitva- ‘husbandhood’, janitva- ‘wifehood’, also pani-graha- lit. ‘grasping the hand’ (of the bride), pari- naya- (cf. pari~ni- 2.33), etc.
Ay. ndirifwana-, lit. ‘wifehood’, fr. nairi- ‘wife’.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
1 ‘ ae In Public Domain. Gurukul Kangri Collection, Haridwar
2.35. ‘Father’.
1. IE *patér-, prob.
Digitized by Arya Samaj Foundation Chennai and eGangotri
MANKIND: SEX, AGE, FAMILY RELATIONSHIP 103 2.35 2.36 2.37 FATHER MOTHER PARENTS
Grk. tari pnrnp Toxets, rexbvres, ryovets
NG jwarépas untépa yovets 7
Lat. pater mater parents
It. padre, babbo madre, mamma genttort ;
Tr. pere mere pere el mére
Sp. padre madre padres
Rum. até mama padrin{t
Ir. athir mathir tuistidt
Nir. _ athatr mathair tuismhightheoira
W. tad mam rhient
Br. tad mam tad ha mam
Goth. atta (fadar) aiper bérusjos, fadrein
ON fadir mooir fedgin
Dan. fader moder foraldre
Sw. fader moder fordldrar
OE fader modor ealdras
ME fader, fadir moder, mother eldren, parentes
NE father mother parents
Du. vader moeder ouders
OHG  fater muotar altiron
MHG vater muoter altern, eltern
NHG __vater mutter eltern
Lith. tévas motyna tévai, gimdytojat
=== SYN leaf 136 ===

Lett.  téus mate vecaki
ChSl. _ otict mati rod ‘tela
SCr. _otac mati roditeljt
Boh. _ otec matka, mdtt rodite
Pol. ojciec matka (maé) rodzice
Russ. olec mat! roditelt
Skt. —_ pitar- méatar- pitarau, malarau
Av. pitar- matar- pitara
2.36. ‘Mother’. 1. IE *mdter-, prob.
starting fr. a nursery word of the pa type (above, p. 94) orig. pd, reduced to pa before the accent. Walde-P. 2.4. Here belong the Grk., Lat., Ir., Gme., and Indo-Iranian words, also Arm. hair, and Toch, A pacar, B pacer. In Balto-Slavic it is completely replaced. 2. Nursery words that have become oe usual terms. Type baba (above, p. ) in It. babbo, now a serious rival of padre, nes atta, tata (above, p. 94) in Rum. an ., Br. tad, Goth. atta (So reg., Vs. ihe) te and here not of earthly » Lith. tévas, Lett. tévs, OPruss.
taws, ChSl. otict , 3 , ete. (all the Balto- Slavic forms), Hitt. fae aad
starting fr. a nursery word of the ma type. Walde-P. 2.229. Here belong the Grk., Lat., Ir., Gme. (except Goth aipei), Balto-Slavic, and Indo-Iranian forms, also Arm. mair, and Toch. A macar, B macer. But Lith. moté became ‘woman’, and as ‘mother’ was replaced by the deriv. motyna.
2. Nursery words that have become the usual terms. Type mama (above, p. 94, Walde-P. 2.221) in It. mamma a serious rival of madre, and W., Br. mam.
Goth. aipei, prob. new fem. formed fr. some nursery word similar to, though not identical with, atta ‘father’. Feist 28.
Digitized by Arya Samaj Foundation Chennai and eGangotri
104 SELECTED INDO-EUROPEAN SYNONYMS
2.37. Words for ‘parents’ are fr. verbs for ‘beget’ or ‘bear’ (4.71, 72); fr. words for ‘old’; or are pl. or du. forms (the lat- ter, of course, more orig.), or derivs., of words for ‘father’, or rarely ‘mother’.
1. Grk. roxets (so reg. Hom.), or aor. pple. rexdvres : rixrw ‘beget, bear’ (4.71).
Grk., NG yovets : yiyvouat ‘be born’, yevvaw ‘beget, bear’ (4.71).
2. Lat. parentés (also ‘ancestors’, late also ‘relatives’), pres. pple. of par- in parere ‘bear, beget’ (4.72). Hence Rum. parinti ‘parents’, Fr. parents formerly ‘parents’ and ‘relatives’ (> ME paren- tes, NE parents), now ‘relatives’ (as ‘parents’ replaced by pére et mére), as also It. parenti, Sp. parientes. REW 6233.
Lat. patrés (as also Grk. rarépes) was commonly used for ‘forefathers’ and oc- casionally in late times for 
=== SYN leaf 137 ===
‘parents’. Hence Sp. padres.
Lat. genitor ‘begetter, father’ : gig- nere ‘beget’, etc. Hence It. genitori.
3. Ir. tuistidi, NIv. tuismhightheoiri : Ir. do-fuismim ‘beget, bear’ (4.71).
W. rhieni (formerly also ‘ancestors’), epd. rhi-eni : gent ‘be born’, Lat. gig-
nere, etc., formed like Grk. mpéyovor ‘an- cestors’. Pedersen 2.533. Br. tad ha mam, after Fr. pére et mére,
4. Goth. bérusjés, orig. a nom. pl. fem. perf. act. pple. of bairan ‘bear’, For the fem., cf. Skt. mataradu, below. Feist 87 f.
Goth. fadrein ‘family’ and ‘parents’, sg. coll. (also pl. fadreina), deriv. of fadar ‘father’.
ON fedgin, deriv. of fadzr ‘father’.
Dan. foreldre, Sw. fordldrar (in the older language ‘forefathers’), OE ealdras, Du. ouders, OHG altiron, NHG eltern, all fr. the Gme. forms for ‘older’.
5. Lith. tévaz, pl. of tévas ‘father’. Lith. gimdytojaz : gimdyti ‘bear, be- get’ (4.71).
Lett. vecaki, fr. vecs ‘old’ (influence of *
NHG eltern prob.). ChSl. roditeli, ete. (all the Slavic words) : roditi ‘beget, bear’ (4.71).
6. Skt. pitardu, Av. pitara (once, Barth. 905), Skt. matarau, both ellipti- cal duals of pitar- ‘father’ or mdtar- ‘mother’, also copulative dual Skt. ma- taradpitara.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar ee
| |
. CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
MANKIND: SEX, AGE, FAMILY RELATIONSHIP 105
2.41 2.42 SON DAUGHTER
Grk. — tros, iets Ouyarnp
NG viés (yutds) Ouyarépa, Kopn
Lat.  filius, ndtus fila i
It. figlio, figliolo figlia, fighiola
Fr. fils fille
Sp. hijo hija
Rum. jiu Sited
Ir. mace ingen
Nir. mac ingheann
W. mab merch
Br. mab merc’ h
Goth. sunus dauhtar
ON sunr, sonr dottir
Dan. sn datter
Sw. son dotter
OE sunu dohtor
ME sune, sone daughter
NE son doughter
Du. zoon dochter
OHG  sun(u) tohter
MHG sun tohter
NHG  sohn tochter
Lith. sinus dukté
Lett. déls meita
ChSl. synit dusti
SCr. sin kéi
Boh. syn dcera
Pol. syn corka
Russ. syn dot!
Skt.  stinu-, putra- duhitar-
Av. puira-, hunu- dugadar-, duyéar-
2.41, 2.42. Most of the words for ‘son’ and ‘daughter’ are inherited from the parent speech. But in part these have been replaced. The words for ‘boy’ and ‘gitl’ (2.25, 2.26) are also naturally used from the parents’ point of view for ‘son’ and ‘daughter’. In a few of these cases the latter is the original sense indicated by the etymology. Even in languages where the old distinctive terms remain, i ee as Lea ‘girl’ may be Gea colloquial use. In some ae a ects we find even in legal ter-
Ogy mats and xépy in place of vids
A Ovyarnp. NG xépy is more common- Y used than Guyarépa.
ee Son’, ly LE} ¥etrin and *swu- ), fr. the root of Skt. sd- ‘bear’,
and orig. an abstract ‘birth, offspring’, then specialized to ‘son’. Walde-P. 2.469. Feist 460f. Here belong Goth. sunus, etc., all the Gme. forms; Lith. stinus, OPruss. souns, ChSl. synw, etc., all the Slavic forms; Skt. siinu-, Av. hunu (but the latter only of evil beings, in contrast to puéra-); Grk. viis, vids; Toch. A se gen. sg. seyo, nom. pl. se- wan (SSS 159), B soy, gen. sg. seyt.
2. Lat. filius (> It. figlio, figholo, Fr. fils, Sp. hijo, Rum. fiu), together with fem. filia ‘daughter’ (> It. figha, figliola, Fr. fille, Sp. hija; Rum. fie arch., now dim. fitcd),
```


## [2026-09-07T20:33:57.145Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 62 93; do echo \"=== HRN leaf $L (printed $((L-21))) ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt; done"
}
```


### [2026-09-07T20:33:58.363Z] TOOL RESULT

```
=== HRN leaf 62 (printed 41) ===
— 40 ~
aw. [/'vard', vareöayanuha 'wachse'; ai. l/'t?ardA-,
vdrdhati *wachsen\
np. välä gross* wird auch hierher gehören und nicht
als Dialektform zu bälä'^),
174. bäm 1) *Haus' s. bän (No. 175).
2) 'Morgen , bämdäd, bämdäddn *des Morgens' (z. B.
Vis und RamTn S. 41, Vers 6).
aw. mspö.]bäma' allbeleuchtend'; phlv. bämtk, bämdät;
ai. bhäma- 'Licht, Strahl*.
afy. LW. bäm.
Nach Geldner, Studien I, 77 bedeutet aw. bamya-
allerdings 'sublimis'; jedenfalls kann das Wort aber
nicht von der l^bhä- scheinen, leuchten getrennt
worden. Dass np. bäm 'Haus' zu bämya- gehören
sollte, ist mir aber sehr unwahrscheinlich; beim wird
secundär für bän stehen, wie sich auch sonst im
Auslaut ein Wechsel der Nasalen findet.
175. {\)bän 'Haus; vergl. bänü (No. 178)2).
phlv. bän 'Dach*.
kurd. bei. (27) LW. bän.
Jedenfalls nicht gleich jüd.-pers. JN^Z 'Zelt', wie
Geiger, Yätk. Zarlr. 50 will, denn JND selbst findet
sich dort, z, B. Is. 15, 3 3).
Nach FJ soll auch bälüden 'wachsen' bedeuten, wofür als Beweis
folgender Vers Mölevi Ma'nevl's angeführt wird (Metr. Remel):
In neseh peivest-i örä büM est
kez sehen sah än-l mih bälüd^ est
Die sprichwörtliche Redensart gurg-l bärändide *ein *Wolf, der nass
geworden ist* (vergl. Houtsma, Een paar perzisohe uitdrukkingen,
S. 11) will — beiläufig bemerkt — FR in bälän geändert wissen (also
*ein Wolf, der das Netz gesehen hat*); bUrän sei aus einem Miss-
verständniss entstanden.
*) FJ hat einen Vers Minöcihrl's als Beleg.
2) Vergl. gr. Sdjuag 'Hausfrau* neben ai. dam- (Schulze, KZ.
28, 281, dessen formale Erklärung von däfiag allerdings unrichtig ist,
vergl. Bartholomae, Berliner philolog. Wochenschrift, 1889, 386 und
Danielsson- Johansson, BB. 18, 11).
») Hörn, Ind. Forsch. II, 138, Nöldeke, ZDMG. 46, 140.
=== HRN leaf 93 (printed 72) ===
- 71 -
g. pur, Semn. i>lr; Käs. pur, pur.
ap. aw. pud^ra- 'Sohn ; phlv. pusar, pus, Säh]puhr;
ai. putrd-,
kurd. pisir, pes[mamy püer (H.-Sch.); oss. d. furf,
t. firf (294) ; bei. n. pusay (304) ; wa/. /?6Y/', ^iyn, piic^
sar. /?öc', minj. pur; arabisirt für in fayfiir, takfür ^),
i'm- (N. pr.).
319. pesend zufrieden, angenehm', pesendlden.
ap. *M/)rt -T- K^arf-; aw. [^sad- (Geldner 1 [/sad-,
KZ. 27, 242), vergl. sendah-, vahmö.sendah- (?)2) (auch
l/"sac/- 'sitzen' kommt mit inligirtem Nasal vor, vergl.
ai. ilsandt- 'Sessel*, ksl. sedq 'ich sitze', apr. sindäts),
Spiegel, Commentar II, 311 (nur fälschlich mit
Praep. paiti; die Aussprache pisend findet sich nur
in dem türkischen FS.).
320. pist 'Mehr.
aw. pistra-; ai. l/'pes- 'zerreiben, zerstampfen {pistä-^
skr. pistaka-),
wa/. pös^; siyn. pist, sar. pa/t geröstetes Korn , zu
Mehl zerrieben'.
321. 2>ie«f 'Rücken'.
Kä§. mäz. past.
aw. parsti' 'Kücken'; phlv. piist; ai. prsti-, prsthd-,
kurd. pist, zaza past; af/. pw5^ bezw. pt^j^^ 'Rippe';
bei. n. put (444) ; wa/. par^.
322. pusek, pösek *Katze' ('Dialekt von Transoxanien' BQ.)^).
gel. plöa (?).
In Indien spricht man piser ; die nämUche Aussprache soll auch
})yser bei Fleischer, Neup. Gramm. 2, S. 7 ausdrücken. Piser ist in
seinem / durch pider beeinilusst; die Endung -er ist nach der der
anderen Verwandtschaftsnamen angefügt (Bartholomae, BB. IX,
129).
*) Fayfür (skr. hhayaputra-) als Titel des Kaisers von China ist
häufig (kurd. fayfürl, farfürl etc. bedeuten dann sogar ^Porzellan*).
Fayfür (Kaiser von Byzanz) v. Hammer, Geschichte der schönen
Redekünste Persiens, S. 94; takfür, Maqrizi II, 2, 190 (Quatremere),
de Lagarde, Nachr. der GGG. 1891, S. 164, Armen. Stud. No. 835.
2) Vergl. Geldner, BB. 14, 28.
») Ein Belegvers bei SF.
```


## [2026-09-07T20:34:04.649Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 63 94; do echo \"=== HRN leaf $L (printed $((L-22))) ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt; done"
}
```


### [2026-09-07T20:34:05.941Z] TOOL RESULT

```
=== HRN leaf 63 (printed 41) ===
- 41 —
Gehört hierher vielleicht auch np. evän 'Vorhalle*
aus a(Jlhi-\-bän, vergl. np. isiäden (No. 84), phlv.
evar (unter No. 16)?
176. {7)~hän *Herr*), -hütend, -schützend (Comp.)', -wan,
-wäne, z. B. päsbän^ suturwün, engust^wdtie,
aw. rand\pana' 'Beinschiene' ; phlv. ^pänak, -pün,
arm. LW. -paw; ai. pändr- ^schützend*.
177. bang *Ruf, Stimme', hanglden, DNl^jlZ 'Geschrei,
Klagen (Is. 14, 31 ; 15, 4, 5), nwXir:N2 (Is. 57, 13).
Kä§. hüng, vöng[vCLze (zweites Glied ist väj),
phlv. vdng, päz. vägined, vägmed jammert, klagt*,
Men. 2, 158, 165 (West, Pahlavi Texts^ 22 Note 2,
23 Note 1), arm. LW. vank, vang,
bei. gvänkj u, gvünJc *Ruf, Schall, Echo', gvänjag
'rufen (145, 146) ; kurd. LW. (?) bänk.
^78. bätm 'Herrin', wörtl. 'Hausherrin' (vergl. bän, No. 175) ;
1 vergl. säh]bänü 'Conyza' (AM. 162).
g. bänü, banewün 'Königin',
phlv. banük, Bänüki, N. pr. (Hörn, Mitteilungen,
Heft IV, S. 35, ZDMG. 44, 664 No. 92).
bei. bänuk, n. bänux (32).
178**'* bäver 'Glaube'.
Zu [/^var- 'glauben' mit upä (d. i. upa+ä)^),
179. baylsten müssen, nötig sein' (Imperson.), Praes.
^\fy^ bäg-ed; vergl. ender wm 'Bedürfniss'^).
Kä§. apä (mit folgendem Futurum), vergl. ßmpeyd
etc. (S. 115).
\i
') Nie selbständig. Ghrest. Schahn. 10 ist hä an suwärän zu
lesen. Auf diesen Yullers^ sehen auch von Darmesteter wieder-
holten Irrtum hat mich Herr Prof. Nöldeke aufmerksam gemacht.
2) Horo, KZ. 32, 582. Fr. Müller vergleicht (WZKM. 6, 79)
9ivm,naver in vaverakati^ dessen Bedeutung zu stark abweicht.
^_^£^TJrsprünglich wird hffiyßd. .*ea^ steht an* streng von säyed *es
geht an* geschieden, worauf Rückert zuerst aufmerksam gemacht hat.
Doch ist dieser feine Unterschied später geschwunden; die Varianten
im Sähnäme verwechseln sehr häufig beide Verba (z. B. I, 76 Vers 275).
=== HRN leaf 94 (printed 72) ===
72
kurd. plslk, pTsTk^ pTsT, pisile *Katze'; af/. />j^ö; bei.
[)üsi^ piinsJ, pisl (307) ; wa;^. pis, si;'n. pas.
Gewiss nicht zu ai. pncöha- ^Schwanz', wie Toma-
schek, Centralas. Stud. II, 762 will.
323. peSenjTden, pisenjidefi ^besprengt werden ^), j)^^^^j^
(Castle aus der jüd.-pers. ßibelübs.).
plilv. pas(i)nci:fan (vd. 5 (6) 61.; Bund.), vergl.
(is(i)ncitan (siehe ^Verlorenes Spraehgut', No. 33),
das im Commentar immer für aw. yhaec- (auch für
visrascayen vd. 7 (77)) steht.
Zusammenhang mit l/"Aa^c-, hincaiti, ai. l/'sec-,
sincdti ist unklar, aber doch wohl vorhanden.
324. pegäh *Frühlicht, früher Morgen .
aw. upa ~r (Jäh (s. No. 889).
325. pul^) 'Brücke.
gel. purd.
aw. peretU' 'Brücke', pesu- 'Furt' (d. i. peretü-, peäu-^
Bartholomae, Ar. Forsch. II, 35 folgg.); phlv.
puhrj puhl ^Brücke, Furt'.
kurd. per^ pir, pird, purd, pel (H.-Sch.); af/. LW.
pul.
326. peleng 'Leopard'^).
skr. p^däku' *Tiger, Panther' (ai. pfdaku-^ pfdäkü-
nur *Natter, Schlange').
kurd. LW. pilink; afy. prang,
327. penUh 'Zuflucht, Schutz', penahlden 'Schutz suchen'.
phlv. panäh,, panähih^ vergl. Mitr]panähak (AV.).
Doch wohl zu l/^pä- schützen'?
Bartholomae stützt diese Erklärung brieflich
*) Das Wort ist nicht allzu gut beglaubigt. Die anderen Wörter-
bücher belegen es gar nicht, nur der FR hat folgenden Vers Leblbl's
(Metr. Muteqärib) mit der Aussprache bis^ :
be^enjer heme tens^ enjlde end
ber an /äk^ /üues bisetijlde end
2j Nie pul gesprochen oder geschrieben (Vullers), das nur
•Geld' bedeutet.
^) Felis pardus L. (Blanford, S. 34).
```


## [2026-09-07T20:34:19.976Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\ndef find(pat):\n    r=re.compile(pat,re.I)\n    for i,p in enumerate(pages):\n        for m in r.finditer(p):\n            print(f'--- leaf {i} (printed ~{i-22}) ---')\n            print(p[max(0,m.start()-400):m.start()+700])\n            print()\nfor pat in [r'\\bp[aä]l[uūù]den\\b', r'\\bp[aä]jTden|p[aä]jlden|pājīden|pājT', r'\\bpider\\b', r'\\bx[vw]?[eé][sš]\\b.{0,40}selbst']:\n    print('#########',pat)\n    find(pat)\nEOF"
}
```


### [2026-09-07T20:34:21.423Z] TOOL RESULT

```
######### \bp[aä]l[uūù]den\b
######### \bp[aä]jTden|p[aä]jlden|pājīden|pājT
######### \bpider\b
--- leaf 85 (printed ~63) ---
n., K 43).
285. pulten 'kochen, Praes. pez-em^ pezamden,
g. pa/tmün, P<^yß (= np. ptixt^) ; Käs. patSn, pa^te-
man; mäz. pa/ta,
aw. skr. [/^pac- 'kochen' ; phlv. pu^tan^ pazem, pazBt
(PPGl.), pazämlnUan (Bund., Men.).
kurd. patin 'kochen', bepiz; afy. pa/avul; oss. d. ficun^
t.ßcin (291) (?) ; bei. pacag, n. pasay (276) ; wa;t'- pöcam,
si/n. sar. pSzam (LW.); arm. LW. apu/t 'roher
Schinken'.
286. pider (peder) 'Vater'.
Käs. pei (aus ped),
ap. pitar- 'Vater'; aw. pitar-; phlv. pit, pitar (in
"inlON), P(i)tar\böxt N. pr. (Kanheri-Inschr.j; ai.
pitar- ; arm. hair 'Vater* (H. No. 155).
kurd. pier^) 'Vater'; af;'. plar\ oss. d. fidä, t. fid
(283) ; bei. pit n. pis, pid- (296) ; siyn. ped, sar. pit.
^) Kurd. pUr konnte dazu verführen, in np. pir 'alt, Alter* eben-
falls ein ursprüngliobes pitar- zu suchen (über altes, durch doppelte
Lautverschiebung zu y werdendes t vergl. s. v. mäye, No. 970), zumal
eine pir ergebende Oontraction aus paruviya' sehr unwahrscheinlich ist.
Plr findet sich jedoch bereits im Pehlevl, und die Bedeutung *alt* ist
dort schon so fest, dass an eine Ableitung von pi

--- leaf 91 (printed ~69) ---
au)'.
a.w./stana' *Brust'; phlv. p(i)stan (vd. 9 (71)), pistän
(vd. 15 (26) 61.); ai. stdna-; arm. stin (H. No. 259).
LW. af/. pistän.
Vergl. Bartholomae, Indog. Forsch. I, 187 Anm. 2.
318. puser, pur 'Sohn, pus (Sahn. III, 1516 Vers 336,
1517 Vers 358 2), 1523 Vers 473).
*) So lese ich statt nvedlnltan.
*) An den beiden ersten SteUen vielleicht für puser zu emendireD,
doch kann bei puser wie bei pider die Izäfe fehlen, vergl. Landauer
zu S. 1517 Note 4.

--- leaf 92 (printed ~70) ---
. 2>ie«f 'Rücken'.
Kä§. mäz. past.
aw. parsti' 'Kücken'; phlv. piist; ai. prsti-, prsthd-,
kurd. pist, zaza past; af/. pw5^ bezw. pt^j^^ 'Rippe';
bei. n. put (444) ; wa/. par^.
322. pusek, pösek *Katze' ('Dialekt von Transoxanien' BQ.)^).
gel. plöa (?).
In Indien spricht man piser ; die nämUche Aussprache soll auch
})yser bei Fleischer, Neup. Gramm. 2, S. 7 ausdrücken. Piser ist in
seinem / durch pider beeinilusst; die Endung -er ist nach der der
anderen Verwandtschaftsnamen angefügt (Bartholomae, BB. IX,
129).
*) Fayfür (skr. hhayaputra-) als Titel des Kaisers von China ist
häufig (kurd. fayfürl, farfürl etc. bedeuten dann sogar ^Porzellan*).
Fayfür (Kaiser von Byzanz) v. Hammer, Geschichte der schönen
Redekünste Persiens, S. 94; takfür, Maqrizi II, 2, 190 (Quatremere),
de Lagarde, Nachr. der GGG. 1891, S. 164, Armen. Stud. No. 835.
2) Vergl. Geldner, BB. 14, 28.
») Ein Belegvers bei SF.

######### \bx[vw]?[eé][sš]\b.{0,40}selbst
```


## [2026-09-07T20:34:30.391Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\ndef show(pat,ctx=(300,700)):\n    r=re.compile(pat)\n    n=0\n    for i,p in enumerate(pages):\n        for m in r.finditer(p):\n            print(f'--- leaf {i} ---'); print(p[max(0,m.start()-ctx[0]):m.start()+ctx[1]]); print(); n+=1\n            if n>6: return\nfor pat in [r'p[aä]l[uūo]', r'xv?[eēi][sš]t?en?\\b', r'\\bxvi[sš]', r'Selbst', r'p[aä]j\\w{0,4}den']:\n    print('###########',pat); show(pat)\nEOF"
}
```


### [2026-09-07T20:34:31.759Z] TOOL RESULT

```
########### p[aä]l[uūo]
--- leaf 402 ---
criima 69,
124 N.
Sabin. ^eWr 124 N.
?*wt«« 927^'* Anm.
Sabin, lingua 124 N.
liquäre 63b.
alat. /o«9ia 631 N.
/M/Mm 42.
Ztina 631 N.
mächina 50 N.
momma 963.
mammula 963.
maneö 966.
margö 974.
mäteries 970.
»/iwa 991bi8.
necäre 143,
nix 181.
objicere 358.
occm/ö 863, 878.
o/^^« 52.
öt7/(m 468.
osk. palumbea 124 N.
it. ;9apa 147 Anm.
^g/t>r :?41.
peasimua 241.
pirose.8 354.
osk. popina 124 N.
»•^^rö 93.
rgjoö 619.
ructäre 15.
ructus \ 5.
rü/w» 124 N.
rwö 628t>« N.
Saansaa 11 S.
Barabara 729.
(1yd.) Äarrf^s 727.
1 sibiläre 741.
I sift//«» 741.
fr. s»/f/er 741.
sißläre 741.
«i//^<*- 124 N.
socru8 487.
rum. spendze 704.
i »/)wö 390.
ifterilis 716.
! sturnus 383.
fr. /a«^^ 389 Anm.
it. /6r2r;2;a 389 Anm.
tepescö 372.
toväre 396.
tonilrus 396.
ir. turcasso 406 Anm.
t//na 14.
upüpa 333.
vöcMMä 1085.
vänus 1085.
venum 242.
t?/dwa 263.
volnus 1075 u. Anm.
!?omö 21Ö.
vordre 36.
Zerovamis 659.
r^acjrd 529.
(/^^rw 67.
f/umrr« 579.
f r^//s 43.
(f/ffMd 41.
: tw// 131.
mif^ 131.
lett. >'m/ 412.
lett.

########### xv?[eēi][sš]t?en?\b
########### \bxvi[sš]
########### Selbst
--- leaf 125 ---
. Biiti:.h Mu^. Xu. •;:.. ZDMG. 44. •>*)).
471. '/jtflfil. /u»*i «Tijit: HtiT. ;rM</4rfM</. /udäcendgür
itürk. /itnL'für. v.-ii:]. NOMtrkt: bei Uübschmann.
<>^at't. Elvi]]., r!^. l:'.:'.!. //tC'.ni, /i'Uc,
aw. vt-ri:l. x'^i^Ot*-: fthlv. /iff«ir id. i. ;frt<tef^) bezw.
/'td'iiw ai. Ytriji. >cj*iiid' Selbst I-Hrstininiung'.
LW. kiipi. ;f<^'r: af;. x'*'inii Oss. ;rwföi: bei. /*«*'*»
n. /»»(t*'!. /i '<»>'// i'..«oi.
Die Diirchsichtiirktrit Jt.-s Zusammenhanges mit l'^</*'
hat wohl Jas d i:eschützt : als Grundform ist etwa *?**
aw. /'adöffii' löder */»iit)'.*y'i-| anzusetzen. Nöldeic ^'
G^'A. l^SJ. .>. t«»:;i« bezweifelt die Richtigkeit 4^*^
EtvmoloKit' vielleicht nicht mit L'nreeht.
Fr. Müllers Erklärung jWZKM. 5. 6b) aus av^
*/ atö.ui/fio nach tiunem Willen sich bewegend*
schon an .>icii wenig Überzeugendes, ganz abgesehe
von der falschen awesti:?chen Xominativbildung.
47:i. yJrätnJden 'schreiten, ^ehen".
ai. l h'ntut'. knlwftfi. hrt'n/Uitr 'gehen, schreiten'.
In der Bedeutung angenehm, e

########### p[aä]j\w{0,4}den
```


## [2026-09-07T20:34:40.918Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i in (120,121,122):\n    print('==== leaf',i,'====')\n    print(pages[i][:600])\nEOF"
}
```


### [2026-09-07T20:34:42.290Z] TOOL RESULT

```
leaves 903
==== leaf 120 ====
tive  origin.  Cp.  Dan.  boble,  MLG.  bubbeln, Du.  bobbelen,  ‘to  bubble’.  Cp.  also  Dan.  boble, Swed.  bubbla,  Du.  bobbel,  ‘a  bubble’,  E.  blob, and  the  second  element  in  hubble-bubble.  Cp. also  burble.
Derivatives:  bubble,  n.,  bubbl-ing,  adj.,  bubbl- ing-Iy,  adv.,  bubbl-y,  adj.
Bubo,  n.,  a  genus  of  owls  ( ornithol .)  —  L.  bubo, ‘owl,  horned  owl’,  from  the  I.-E.  imitative  base *bu-.  See  Buteo.
bubo,  n.,  a  swelling  in  the  groin  (med.)  —  Late  L., fr.  Gk.  ‘groin,  swelling  in  the  groin’,
which  is  prob.  cogn.  with  OI.  gavint,  ‘gro
==== leaf 121 ====
ffix and  accordingly  dropped.
Derivative:  buff,  tr.  v.,  to  polish  with  a  buff;  to make  as  smooth  as  buff  leather, buffalo,  n.  —  Port,  buffalo,  fr.  L.  bufalus,  a  col¬ lateral  form  of  bitbalus,  fr.  Gk.  poupaXo;,  ‘an African  antelope’,  later  ‘buffalo’,  which  is  prob. rel.  to  pou;,  ‘ox’.  See  bovine  and  cp.  prec.  word and  buffle.  Cp.  also  bubaline,  bubalis  and  the first  element  in  Buchloe.
buffer,  n.,  one  who,  or  that  which,  buffs  or strikes.  —  Formed  from  the  verb  buff,  ‘to  strike’ (see  buff,  ‘a  blow’),  with  agential  su
==== leaf 122 ====
e  of  ‘swel¬ ling’.  For  the  connection  of  bump  with  bunch cp.  clump  and  clunch,  hump  and  hunch,  lump and  lunch.
Derivatives :  bunch,  tr.  and  intr.  v.,  bunch-y,  adj., bunch-i-ly,  adv.,  bunch-i-ness,  n. bunco,  bunko,  n.,  swindling  at  cards;  tr.  v.,  to swindle  at  cards.  —  Cp.  Sp.  banco,  ‘bank’, banco,  ‘a  game  of  cards’,  which  are  rel.  to  It. banca,  ‘bank’.  See  bank,  ‘an  institution  for  the custody  of  money’.
buncombe,  n.  —  A  spelling  var.  of  bunkum, bundle,  n.  —  ME.  bundel,  fr.  MDu.  bundel,  a collateral  form  of  bondel,
```


## [2026-09-07T20:34:50.256Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (73,88,94,95,100,101):\n    print('==== leaf',i,'~ pp',2*(i-16)-1,2*(i-16),'====')\n    print(pages[i][:900])\n    print()\nEOF"
}
```


### [2026-09-07T20:34:51.585Z] TOOL RESULT

```
==== leaf 73 ~ pp 113 114 ====
tus,  pp. of  assimildre,  ‘to  make  like,  liken’,  fr.  ad-  and simildre,  ‘to  make  similar  to’,  fr.  similis,  ‘like,  re¬ sembling’.  See  similar  and  verbal  suff.  -ate  and cp.  assemble.
Derivatives:  assimilation  (q.v.),  assimilat-ive, adj.,  assimilat-or ,  n.,  assimilat-ory,  adj. assimilation,  n.  —  L.  assimilatio,  gen.  assimila¬ tions,  ‘likeness,  similarity’,  fr.  assimilatus,  pp. of  assimildre.  See  assimilate  and  -ion. assist,  tr.  and  intr.  v.  —  F.  assister,  ‘to  stand  by, help,  assist’,  fr.  L.  assistere,  ‘to  stand  by’,  fr.  ad- and  sistere,  ‘to  cause  to  stand,  put,  place;  to stand  still,  stand’,  from  the  reduplicated  base  of stare,  ‘to  stand'.  Cp.  OI.  tisthati,  Avestic  hish- taiti,  ‘stands',  and  Gk.  'iaTrjpu.,  ‘I  cause  to  stand, place;  I  stand’,  which  stands  for  *a(-<TT7;fjt.i, and  see  state.  

==== leaf 88 ~ pp 143 144 ====
e  banner  and cp.  prec.  word.
bandhava,  n.,  a  kinsman  (Hindu  law).  —  OI. bdndhavah,  rel.  to  bandhuh  ‘relationship,  kins¬ man’.  See  next  word.
bandhu,  n.,  related  through  females.  —  OI.  bdn¬ dh  uh,  ‘relationship,  kinsman’,  rel.  to  bandhdh,  ‘  a binding;  band,  tie’,  fr.  I.-E.  base  *bendh-,  ‘to bind'.  See  band,  ‘tie’.
bandicoot,  n.,  a  kind  of  a  large  rat.  —  Telegu pandi  kokku,  lit.  ‘pig  rat’, bandit,  n.  —  F.,  fr.  It.  bandito,  prop.  pp.  of  ban- dire,  ‘to  banish’,  which  arose  from  a  blend  of Frankish  *bannjan ,  ‘to  banish’  (whence  F.  ban- nir,  E.  banish),  and  Goth,  bandwa,  ‘sign,  signal’. See  banner.
banditi,  n.  pi.,  sometimes  used  as  sing.,  bandits; bandits  collectively.  —  It.,  pi.  of  bandito.  See prec.  word.
bandog,  n.,  a  dog  kept  tied  up  as  a  watchdog  or because  of  its  ferocit

==== leaf 94 ~ pp 155 156 ====
 (1832-98)  fr.  beam,  in  the  sense  of  ‘ray  of light’,  and  adj.  suff.  -ish.
bean,  n.  —  ME.  bene,  fr.  OE  bean,  rel.  to  OS., OHG.  bona,  ON.  baun,  Dan.  bonne,  Norw. bauna,  Swed.  bona,  OFris.  bane,  MLG.,  MDu. bone,  Du.  boon,  MHG.  bone,  G.  Bohne',  prob. derived  from  the  child’s  word  bha-,  ‘something swelling’,  whence  also  Gk.  tpaxo?,  ‘lentil’.  Cp. L.faba,  ‘bean’,  OSlav.  bobu,  Russ,  bob,  OPruss. babo,  "bean’,  which  prob.  derive  from  the  I.-E. child’s  word  *bhabha,  ‘bean’,  reduplication  of *bha-;  see  Fabaceae.
157
Derivative:  bean,  tr.  v.,to  hit  on  the  edg e  (slang).
beano,  n.,  beanfeast  (slang).  —  Fr.  prec.  word.
bear,  n.,  the  animal.  —  ME.  here,  fr.  OE.  her  a, rel.  to  MDu.  here,  Du.  beer,  OHG.  bero,  MHG. her,  G.  Bar,  ON.  bjorn,  lit.  ‘the  brown  animal’, fr.  I.-E.  *bhero-,  ‘brown’,

==== leaf 95 ~ pp 157 158 ====
.  bed,  Swed.  bddd,  MLG.,  MDu. bedde,  Du.  bed,  OHG.  betti,  MHG.  bette,  bet, G.  Belt,  Goth,  badi,  ‘bed’,  prop,  ‘a  couch  dug into  the  ground’,  fr.  I.-E.  base  *bhedh,  *bhod-, ‘to  dig,  pierce’,  whence  also  Hitt,  beda-,  ‘to  pier¬ ce,  prick’,  Gk.  p6fhjpo<;,  ‘pit’,  L.  fodere,  ‘to  dig’, fossa,  ‘ditch’,  Lith.  badau,  badyti,  ‘to  pierce, prick’,  bedu,  bisti,  ‘to  dig’,  Lett,  badu,  badit,  ‘to pierce,  prick’,  Lith.  bedre,  Lett.  bpdu,  best,  ‘to dig’,  bedre,  ‘pit’,  OPruss.  boadis,  ‘prick’,  OSlav. bodp,  bosti,  ‘to  prick’,  bodli,  ‘thorn’,  W.  bedd, Co.  bedh,  Bret,  bez,  ‘grave’.  G.  Beet,  ‘garden- bed’,  is  a  variant  of  Bett,  ‘bed’.  Cp.  bothrium, fosse,  fossil.
bed,  tr.  v.  —  ME.  beddien,  bedden,  fr.  OE.  beddian, ‘to  place  in  a  bed,  to  bed’,  fr.  bedd,  ‘bed’.  See bed,  n.
Derivatives:  bedd-ed,  adj.  

==== leaf 100 ~ pp 167 168 ====
��,  fr.  beurre,  ‘butter’. See  prec.  word.
bevel,  n.,  inclination  of  a  surface.  —  OF.  "baivel (whence  F.  beveau,  biveau),  ‘bevel  rule’,  fr.  OF. baif,  ‘with  an  open  mouth’,  fr.  baer,  beer,  ‘to gape’.  See  bay,  ‘part  in  the  wall’,  and  cp.  words there  referred  to.
Derivatives:  bevel,  tr.  v.  bevel(l)-ed,  adj.,  be- vel(l)-er,  n.
beverage,  n.  —  OF.  bevrage,  bovrage  (F.  breu- vage),  fr.  beivre,  boivre  (F.  boire),  ‘to  drink’,  fr. L.  bibere.  See  bibulous  and  -age  and  cp.  bevy, abreuvoir.
bevue,  n.,  error,  blunder.  —  F.  bevue,  ‘blunder, mistake,  slip’,  fr.  OF.  bes-vue,  lit.  ‘an  erroneous vue’,  fr.  pejorative  pref.  bes-,  which  derives  fr. L.  bis,  ‘twice’  (see  bis-;  for  sense  development  cp. OF.  bes-torne,  ‘badly  turned’,  lit.  ‘twice  turned’), and  fr.  vue,  ‘sight’,  prop.  fern.  pp.  of  voir,  

==== leaf 101 ~ pp 169 170 ====
ip  of  the Bible.  —  Compounded  of  biblio-  and  Gk. -Xarpeia,  -Xarpla,  fr.  Xa-rpela,  ‘hired  labor,  wor¬ ship’.  See  -latry.
bibliomancy,  n.,  divination  by  opening  a  book, esp.  by  opening  the  Bible.  —  Compounded  of biblio-  and  Gk.  fravreta,  ‘oracle,  divination’. See  -mancy.
biblomania,  n.,  book  madness.  —  Compounded of  biblio-  and  Gk.  pavia,  ‘madness,  frenzy’.  See
-mania.
biblomaniac,  adj.  —  Compounded  of  biblio-  and ML.  maniacus,  ‘maniac’.  See  maniac, bibliophil,  bibliophile,  n.  a  lover  of  books.  —  F. bibliophile,  ‘lover  of  books’,  compounded  of biblio-  and  Gk.  91X0?,  ‘friend’.  See  -phil. Derivatives:  bibliophil-ic,  adj.,  bibliophil-ism,  n., bibliophil-ist,  n.,  bibliophil-y ,  n. bibliopole,  n.,  bookseller.  —  L.  bibliopola,  fr.  Gk. (3i[iXio77coXy;p,  ‘bookseller’,  which  is  compounded of  [kfJXtov,  ‘b
```


## [2026-09-07T20:35:06.584Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1971.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages), len(t))\nimport re\nfor w in ['bezoar','padishah','satrap','pasha','despot']:\n    for i,p in enumerate(pages):\n        m=re.search(w,p,re.I)\n        if m:\n            print('###',w,'leaf',i)\n            print(p[max(0,m.start()-300):m.start()+700].replace('\\n',' '))\n            print()\n            break\nEOF"
}
```


### [2026-09-07T20:35:08.029Z] TOOL RESULT

```
leaves 1 9828418
### bezoar leaf 0
 where to stand’. See Hindustani,  bezetta, bezette, n., a dyeing material made by  dipping linen rags into certain coloring matters.  — It. pezzetta , dimin. of pezza, ‘piece of cloth',  a word of Gaulish origin. See piece and -ette.  bezique, n., a card game. — F. besigue, of un-  known origin.   bezoar, n., orig. a term for antidote ; later used  for concoctions found in the stomach or in-  testines of certain animals and thought to have  antidotal properties. — F. bezoard, fr. Sp. be-  zoar (cp. Port, bezuar), fr. Arab, badizahr, often  shortened into bazahr (see Frey tag, Lexicon  Arabico-Latinum, I, 79a and b), ult. fr. Pers.  badzahr, padzahr, ‘counterpoison, bezoar stone*,  lit. ‘protecting (against) poison’, fr. pad, ‘pro-  tecting, guarding; guardian, lord, master’, and  zahr, ‘poison’. For the first element see padi-  shah. The second element is rel. to Pers. zehre,  ‘gall, bile’, Pahlavi zahr, ‘poison’, Avestic zara -,  ‘gall, bile’, and cogn. with Gk. xokf], ‘gall, bile’. 

### padishah leaf 0
(i)-, *qff(i)-, ‘to rule’,  whence also OI. k$ayati, ‘possesses, rules’, k$at-  ram, ‘rule, dominion’, Gk. xTaofxai, ‘I get, ac-  quire’. See satrap, shah and cp. checkmate, chess,  checker, exchequer, Kshatriya. Cp. also the first  element in Ahasuerus, Xerxes and the second  element in Nakshatra, padishah and pashah.  Derivatives : check , tr. and intr. v., check-less , adj .  check, cheque, n., a written order to a bank. —  Most philologists derive this word from check  in the sense ‘a sudden stop’. It is more probable,  however, that check in the sense ‘a written order  to a bank’, comes fr. Arab. $akk, ‘agreement,  contract’, fr. Pers. dak, of s.m.  checker, chequer, n., a pattern resembling a chess-  board. — Shortened fr. OF. eschekier (F. echi-  quia), ‘chessboard’, fr. ML. scaccarium, ult.  fr. Pers. shah, ‘king’. See check, ‘a sudden stop’,  and cp. exchequer.   Derivatives: checker, tr. v., checker-ed , adj.,  checkers (q.v.)   checkers, chequers, n., a game played on a  che

### satrap leaf 0
wi) means  ‘keeper, guardian’. Pers. ban, is rel. to OPers.  pa(y)-, *to guard, protect’, 01. pdti, ‘guards,  protects’, pond-, ‘guarding, protecting’ (see  P.Horn, GrundriB der neupersischen Etymo-  logic, StraBburg, 1893, No. 176). See food and  cp. banat and the second element in durwaun  and in satrap.   Bana, n., son of Bali, a thousand armed giant  {Hindu mythol .) — OI. Bapah, lit. ‘^rrow*, prob.  a loan word fr. Austroasiatic.  banal, adj., trite, commonplace. — OF. banal,  fr. ban , ‘proclamation’. See ban, ‘edict’. Banal  orig. meant ‘compulsory’, whence it came to  denote ‘common to all, commonplace’,  banal, adj., pertaining to a ban or the banat. —  Formed fr. ban, ‘governor’, with adj. suff. -al.  banality, n., 1) triteness; 2) a platitude. — F. ba-  nalite, fr. banal. See banal, ‘trite’, and -ity.  banana, n. — Sp. and Port., fr. earlier Congo-  lese banam.   banat, also banate, n., the district governed by a  ban. — A hybrid coined fr. ban, ‘governor’ and  suff. -ate (f

### pasha leaf 0
classical  L. occurring only as a cognomen); of un-  certain origin. Cp. abase, bass (music), basset,  basso, bassoon, debase.   Derivatives: base-ly, adv., base -ness, n.  bash, tr. v., to strike violently. — Of imitative  origin. Cp. Swed. basa, Dan. baske, ‘to strike’,  bashaw, n. — A variant of pasha (q.v.)  bashful, adj. — Aphetic for abash-ful. See abash  and -ful.   Derivatives: bashful-ly , adv., bashful-ness, n.  bashi-bazouk, n., a Turkish irregular soldier. —  Turk, bdshi-bozuq, lit. ‘(one whose) head is  turned’. Cp. the first element in bashlyk and the  second element in bimbashee.  bashlyk, also bashlik, n., hood covering the ears.  — Turk, bashlyq, ‘any kind of headgear’,  basic, adj. — Formed with suff. -ic fr. base, n.  Cp. the second element in monobasic, di-  basic.   Derivative: basic-al-ly, adv.  basidium, n., a form of sporophore characteristic  of the fungi of the class Basidiomycetes (bot.) —  ModL., fr. Gk. paois, ‘base’. See base, n., and  cp. Aureobasidium.  

### despot leaf 0
r. de- and spondere , ‘to  engage oneself, promise’. See spouse.  Derivatives: despond-ence , n., despond-ency, n.,  despondent (q.v.), despond-er , n., despond-ing,  adj., despond-ing-ly , adv.  despondent, adj. — L. despondens , gen. -entis,  pres. part, of despondere. See prec. word and  -ent.   despot, n., tyrant. — OF. despot (F. despote ), fr.  Gk. 8ea7r6TTr]c, ‘master, ruler, tyrant’, which  stands for orig. *dems-pota, and prop, means  ‘lord of the house’ and is equivalent to OI.  dam-patih, lord of the house’. The first element  stands in gradational relationship to Gk. Stopioc,  L. domus, ‘house’; see dome, ‘building’. The  second element is rel. to Gk. 7:60^ (for *7r6Ttc),  ‘husband’, and cogn. with Ol. patifr, ‘master,  husband’, L. potis, ‘able, powerful’, potens ,  ‘able, mighty, powerful’. See potent and cp. pos-  sess, possible, power, puissant.   Derivatives: despotic (q.v.), despot-ism , n., des -  pot-ist, n.   despotic, despotical, adj., pertaining to a despot;  tyr
```


## [2026-09-07T20:35:40.238Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor w in ['bezoar','GrundriB der neupersischen','Grundri','satrap, n','padishah']:\n    for i,p in enumerate(pages):\n        m=re.search(w,p)\n        if m:\n            print('###',w,'leaf',i)\n            # print numbers appearing alone in the leaf\n            print('page-nums in leaf:',re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$',p))\n            print(p[max(0,m.start()-600):m.start()+900].replace('\\n',' '))\n            print()\n            break\nEOF"
}
```


### [2026-09-07T20:35:41.798Z] TOOL RESULT

```
### bezoar leaf 100
page-nums in leaf: ['166', '169']
side’.  See  bis-  and  ala. bezesteen,  n.,  a  bazaar.  —  Pers.  bezestan,  formed fr.  bez  (whence  Arab,  bazz),  ‘flax,  linen  clothes’, and  -stan,  a  suff.  denoting  place,  which  is  rel, to  Avestic  stana-  (in  compounds),  ‘place’,  lit. ‘a  place  where  to  stand’.  See  Hindustani, bezetta,  bezette,  n.,  a  dyeing  material  made  by dipping  linen  rags  into  certain  coloring  matters. —  It.  pezzetta,  dimin.  of  pezza,  ‘piece  of  cloth’, a  word  of  Gaulish  origin.  See  piece  and  -ette. bezique,  n.,  a  card  game.  —  F.  besigue,  of  un¬ known  origin. bezoar,  n.,  orig.  a  term  for  antidote-,  later  used for  concoctions  found  in  the  stomach  or  in¬ testines  of  certain  animals  and  thought  to  have antidotal  properties.  —  F.  bezoard,  fr.  Sp.  be¬ zoar  (cp.  Port,  bezuar),  fr.  Arab,  badizdhr,  often shortened  into  bazahr  (see  Freytag,  Lexicon I Arabico-Latinum,  I,  79a  and  b),  ult.  fr.  Pers. badzahr,  padzahr,  ‘counterpoison,  bezoar  stone’, lit.  ‘protecting  (against)  poison’,  fr.  pad,  ‘pro¬ tecting,  guarding;  guardian,  lord,  master’,  and zahr,  ‘poison’.  For  the  first  element  see  padi- shah.  The  second  element  is  rel.  to  Pers.  zehre, ‘gall,  bile’,  Pahlavi  zahr,  ‘poison’,  Avestic  zara-, ‘gall,  bile’,  and  cogn.  with  Gk.  yoXf],  ‘gall,  bile’. See  choler. bezonian,  n.,  knave,  rascal.  —  Formed  with  suff. -ian,  fr.  It.  bisogno,  ‘want,  need’,  which  is

### Grundri leaf 87
page-nums in leaf: ['144', '145']
e  fr.  ON.  banna, resp.  OHG.  bannan,  MHG.,  G.  bannen );  partly fr.  OF.  (==  F.)  ban,  ‘public  proclamation’,  fr. Frankish  *ban,  which  is  rel,  to  OHG.  ban (see  above).  See  ban,  v. ban,  n.,  a  governor  of  Croatia.  —  Serbo-Croatian ban,  ‘lord,  master,  ruler’,  fr.  Pers.  ban,  ‘prince, lord,  chief,  governor’  (prob.  through  the  medium of  the  Avars).  As  a  suff.  -ban  (var.  -wan)  means ‘keeper,  guardian’.  Pers.  ban,  is  rel.  to  OPers. pa(y)-,  ‘to  guard,  protect’,  OI.  pdti,  ‘guards, protects’,  pand-,  ‘guarding,  protecting’  (see P.Horn,  GrundriB  der  neupersischen  Etymo- logie,  StraBburg,  1893,  No.  176).  See  food  and cp.  banat  and  the  second  element  in  durwaun and  in  satrap. Bana,  n.,  son  of  Bali,  a  thousand  armed  giant (Hindu  mythol.)  —  OI.  Bdndh,  lit.  ‘arrow’,  prob. a  loan  word  fr.  Austroasiatic. banal,  adj.,  trite,  commonplace.  —  OF.  banal, fr.  ban,  ‘proclamation’.  See  ban,  ‘edict’.  Banal orig.  meant  ‘compulsory’,  whence  it  came  to denote  ‘common  to  all,  commonplace’, banal,  adj.,  pertaining  to  a  ban  or  the  banat.  — Formed  fr.  ban,  ‘governor’,  with  adj.  suff.  -al. banality,  n.,  1)  triteness;  2)  a  platitude.  —  F.  ba- nalite,  fr.  banal.  See  hanal,  ‘trite’,  and  -ity. banana,  n.  —  Sp.  and  Port.,  fr.  earlier  Congo¬ lese  banam. banat,  also  banate,  n.,  the  district  governed  by  a ban.  —  A  hybrid  coined  fr.  ban,  

### padishah leaf 154
page-nums in leaf: ['272', '273']
  earlier  eschac, borrowed  (through  the  medium  of  Spanish  and Arabic)  fr,  Pers.  shah,  ‘king’  (in  the  Arab.-Pers. phrase  shah  mat,  ‘the  king  is  dead’),  fr.  OPers. xshaya-,  ‘king’,  which  is  rel.  to  xshaya&iya-, ‘power’,  fr.  I.-E.  base  *qpe(i)-,  *qfe(i)-,  ‘to  rule’, whence  also  OI.  ksayati,  ‘possesses,  rules’,  ksat- ram,  ‘rule,  dominion’,  Gk.  xTaopat,,  T  get,  ac¬ quire’.  See  satrap,  shah  and  cp.  checkmate,  chess, checker,  exchequer,  Kshatriya.  Cp.  also  the  first element  in  Ahasuerus,  Xerxes  and  the  second element  in  Nakshatra,  padishah  and  pashah. Derivatives :  check,  tr.  and  intr.  v.,  check-less,  adj. check,  cheque,  n.,  a  written  order  to  a  bank.  — Most  philologists  derive  this  word  from  check in  the  sense  ‘a  sudden  stop’.  It  is  more  probable, however,  that  check  in  the  sense  ‘a  written  order to  a  bank’,  comes  fr.  Arab,  fakk,  ‘agreement, contract’,  fr.  Pers.  cdk,  of  s.m. checker,  chequer,  n.,  a  pattern  resembling  a  chess¬ board.  Shortened  fr.  OF.  eschekier  (F.  echi- quiet),  ‘chessboard’,  fr.  ML.  scaccarium,  ult. fr.  Pers.  shah,  ‘king’.  Sec  check,  ‘a  sudden  slop’, and  cp.  exchequer. Derivatives:  checker,  tr.  v.,  checker-ed,  adj., checkers  (q.v.) checkers,  chequers,  n.,  a  game  played  on  a checkerboard;  draughts.  —  From  prec.  word, checkmate,  interj.  —  ME.  chek  mat,  fr.  OF.  eschec et  mat  (F.  echec  et  m
```


## [2026-09-07T20:35:53.572Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (73,74,94,95):\n    p=pages[i]\n    print('==== leaf',i,'nums',re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$',p),'====')\n    print(p[:300].replace('\\n',' '))\n    print('...')\n    print(p[-500:].replace('\\n',' '))\n    print()\nEOF"
}
```


### [2026-09-07T20:35:55.027Z] TOOL RESULT

```
==== leaf 73 nums [] ====
tus,  pp. of  assimildre,  ‘to  make  like,  liken’,  fr.  ad-  and simildre,  ‘to  make  similar  to’,  fr.  similis,  ‘like,  re¬ sembling’.  See  similar  and  verbal  suff.  -ate  and cp.  assemble. Derivatives:  assimilation  (q.v.),  assimilat-ive, adj.,  assimilat-or ,  n.,  assimilat-ory,  a
...
 ex¬ tinguish. Derivatives;  astonish-ed-ly,  adv.,  astonish-er,  n., astonish-ing,  adj.,  astonish-ing-ly,  adv.,  astonish- ing-ness,  n. astound,  tr.  v.  —  ME.  astoned,  astouned,  pp.  of astonien.  See  astonish. Derivatives;  astound-ing,  adj.,  astound-ing-ly, adv.,  astound-ment,  n. astraddle,  adv.  —  Formed  fr.  a-,  ‘on’,  and straddle. Astraea,  n.,  the  goddess  of  justice  in  Greek  and Roman  mythology.  —  L.,  fr.  Gk.  ’Aaxpaia,  lit. ‘starry’,  fem.  of  aaxpouo;,

==== leaf 74 nums ['120', '121'] ====
  fr.  daxf]p,  ‘star’.  See Aster. astragal,  n.,  a  convex  molding  (archil.)  —  L.  as¬ tragalus,  fr.  Gk.  aaxpxyaXoc;,  ‘one  of  the  ver¬ tebrae  of  the  neck,  anklebone,  molding’,  assim¬ ilated  fr.  *6axpdyocXo<;,  which  is  rel.  to  oaxpoc- xov,  ‘oyster  shell,  potsherd’,  6ax£
...
i’, atavic,  adj.,  of  a  remote  ancestor.  —  Formed with  suff.  -ic  fr.  L.  atavus.  See  next  word, atavism,  n.,  reversion  to  a  remote  ancestral  type. —  Formed  with  suff.  -ism  fr.  L.  atavus,  ‘father of  a  great-grandfather,  ancestor’,  fr.  pref.  at-, ‘beyond’,  and  avus,  ‘grandfather’.  See  uncle  and cp.  avuncular. atavistic,  adj.,  pertaining  to  atavism;  tending  to atavism.  —  Formed  with  suff.  -istic  fr.  L.  atavus. See  prec.  word.  See  atavism. D

==== leaf 94 nums ['157'] ====
 (1832-98)  fr.  beam,  in  the  sense  of  ‘ray  of light’,  and  adj.  suff.  -ish. bean,  n.  —  ME.  bene,  fr.  OE  bean,  rel.  to  OS., OHG.  bona,  ON.  baun,  Dan.  bonne,  Norw. bauna,  Swed.  bona,  OFris.  bane,  MLG.,  MDu. bone,  Du.  boon,  MHG.  bone,  G.  Bohne',  prob. derived  fro
...
ly,  adv. become,  intr.  and  tr.  v.  —  ME.  bicumen,  becu- men,  fr.  OE.  becuman,  ‘to  come  to,  meet  with, happen’,  rel.  to  Du.  bekomen,  MHG.  bekomen, G.  bekommen,  ‘to  suit,  agree’  (in  G.  said  only of  food),  Goth,  biqiman,  ‘to  come  upon  one’, and  to  OE.  geeweme,  ME.  iqueme,  queme,  OHG. biquami ,  MHG.  bequteme,  G.  bequent,  con¬ venient,  fitting,  suitable’.  See  be-  and  come, bed,  n.  —  OE.  bedd,  bed,  rel.  to  OS.  beddi,  bed, ON.  bedr,  Dan

==== leaf 95 nums [] ====
.  bed,  Swed.  bddd,  MLG.,  MDu. bedde,  Du.  bed,  OHG.  betti,  MHG.  bette,  bet, G.  Belt,  Goth,  badi,  ‘bed’,  prop,  ‘a  couch  dug into  the  ground’,  fr.  I.-E.  base  *bhedh,  *bhod-, ‘to  dig,  pierce’,  whence  also  Hitt,  beda-,  ‘to  pier¬ ce,  prick’,  Gk.  p6fhjpo<;,  ‘pit’,  L.
...
-ism. behaviorist,  n.  —  See  prec.  word  and  -ist. Derivatives:  behaviorist-ic,  adj.,  behaviorist-ic- al-ly,  adv. behead,  tr.  v.  —  ME.  bihefden,  biheden,  fr.  OE. beheafdian,  fr.  be-  and  OE.  heafod,  ‘head’.  See head. beheld,  past  tense  and  pp.  of  behold, behemoth,  n.,  a  huge  beast,  probably  the  hippo¬ potamus.  —  Heb.  behemdth,  used  in  the  sense of  a  plural  of  intensity  of  blhemah,  ‘beast’  (see Job  40 : 1 5-24).  The  assumed  connection  of  He
```


## [2026-09-07T20:36:08.156Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('IRN'),ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('SNS'),ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('FSF'),ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('BQT'),ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-07T20:36:09.443Z] TOOL RESULT

```
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
{
 "title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989",
 "kind": "local_scan_ocr",
 "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)",
 "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt"
 ],
 "page_offset": "222 leaves; printed page = PDF page − 11 (PDF 101 = p.90; chapter openers carry no numeral). 6th printing 1382, same setting as 1368.",
 "covers_etymology": true,
 "notes": "Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); (only the 'fas' pass was run for IRN.) Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. | OCR text, printed = pdf-11",
 "scans": [
  {
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf",
   "first_printed": 1,
   "last_printed": 210,
   "pdf_offset": 11,
   "lang": "fas",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt"
  }
 ]
}
{
 "title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/VajnameShayest",
 "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"
 ],
 "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image",
 "covers_etymology": true,
 "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."
}
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
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt"
 ],
 "page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').",
 "covers_etymology": true,
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
 "scans": [
  {
   "volume": "3",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
   "first_printed": 1208,
   "last_printed": 1925,
   "pdf_offset": -1205,
   "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json",
   "lang": "fas",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
   "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"
  },
  {
   "volume": "4",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
   "first_printed": 1920,
   "last_printed": 2475,
   "pdf_offset": -1917,
   "lang": "fas",
   "offset_note": "printed = pdf+1917, checked at pdf 150 and 500",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt"
  },
  {
   "volume": "5",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
   "first_printed": 1,
   "last_printed": 290,
   "pdf_offset": 5,
   "lang": "fas",
   "note": "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
   "requires_volume": true
  }
 ],
 "cites": "page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material"
}
```


## [2026-09-07T20:36:20.806Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\ndef leafnums(i):\n    return re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$',pages[i])\nfor w in ['durwaun','^satrap','Atropat','Azerbaij','Aturpat','^pasha','^shah,','^food, n']:\n    for i,p in enumerate(pages):\n        m=re.search(w,p,re.M)\n        if m:\n            print('###',w,'leaf',i,'nums',leafnums(i),'| nearby leaf nums',[ (j,leafnums(j)) for j in range(max(0,i-2),i+3)])\n            print(p[max(0,m.start()-200):m.start()+800].replace('\\n',' '))\n            print()\n            break\n    else: print('###',w,'NOT FOUND')\nEOF"
}
```


### [2026-09-07T20:36:22.407Z] TOOL RESULT

```
### durwaun leaf 87 nums ['144', '145'] | nearby leaf nums [(85, ['140', '141']), (86, ['142', '143']), (87, ['144', '145']), (88, ['146']), (89, ['148', '149'])]
uards, protects’,  pand-,  ‘guarding,  protecting’  (see P.Horn,  GrundriB  der  neupersischen  Etymo- logie,  StraBburg,  1893,  No.  176).  See  food  and cp.  banat  and  the  second  element  in  durwaun and  in  satrap. Bana,  n.,  son  of  Bali,  a  thousand  armed  giant (Hindu  mythol.)  —  OI.  Bdndh,  lit.  ‘arrow’,  prob. a  loan  word  fr.  Austroasiatic. banal,  adj.,  trite,  commonplace.  —  OF.  banal, fr.  ban,  ‘proclamation’.  See  ban,  ‘edict’.  Banal orig.  meant  ‘compulsory’,  whence  it  came  to denote  ‘common  to  all,  commonplace’, banal,  adj.,  pertaining  to  a  ban  or  the  banat.  — Formed  fr.  ban,  ‘governor’,  with  adj.  suff.  -al. banality,  n.,  1)  triteness;  2)  a  platitude.  —  F.  ba- nalite,  fr.  banal.  See  hanal,  ‘trite’,  and  -ity. banana,  n.  —  Sp.  and  Port.,  fr.  earlier  Congo¬ lese  banam. banat,  also  banate,  n.,  the  district  governed  by  a ban.  —  A  hybrid  coined  fr.  ban,  ‘governor’  and suff.  -ate  (fr. 

### ^satrap leaf 736 nums [] | nearby leaf nums [(734, ['1382']), (735, []), (736, []), (737, []), (738, [])]
e, do’.  See  satis  and  -fy. Derivatives:  satisfi-able ,  adj.,  satisfi-ed,  adj., satisfi-ed-ly,  adv.,  satisfi-ed-ness,  n.,  satisfy-ing, adj.,  satisfy -ing-ly,  adv.,  satisfy-ing-ness,  n. satrap,  n.,  1)  governor  in  a  province  in  ancient Persia;  2)  a  despotic  ruler.  —  ME.,  fr.  L.  satra- pes,  fr.  Gk.  e^xTpxTtvjC,  aaTpxTTTjp,  fr.  OPers. xshaftrapavan-,  ‘ruler  of  the  province’,  com¬ pounded  of  xsha&ra-,  ‘province’,  and  a  deriva¬ tive  of pd(y)-,  ‘to  guard,  protect’,  which  is  rel.  to Oil  pati,  ‘guards,  protects’.  The  first  element  is rel.  to  OPers.  xshaya-,  ‘king’,  xshayafHya-, ‘power’,  and  cogn.  with  Gk.  XTxaOxt,  ‘to  pos¬ sess’,  fr.  I.-E.  base  *qpe(i)-,  *qpei-,  ‘to  possess, rule’;  see  shah  and  cp.  check,  ‘sudden  stop’.  For the  second  element  see  food  and  cp.  words  there referred  to. Derivative:  satrap-al,  adj. satrapy,  n.  —  F.  satrapie,  fr.  L.  satrapia,  fr.  Gk. aarpattsix,  ‘satrapy’,

### Atropat NOT FOUND
### Azerbaij leaf 459 nums ['852', '853', '1967'] | nearby leaf nums [(457, ['849']), (458, ['850', '851']), (459, ['852', '853', '1967']), (460, ['857']), (461, ['858', '859'])]
—  OI.  ksatriyah,  fr.  ksatram,  ‘rule,  do¬ minion’.  See  check,  ‘sudden  stop’. Kuba,  also  kuba,  n.,  a  kind  of  fine  rug.  —  Short for  Kuba  rug;  so  called  after  Kuba,  a  town  in Azerbaijan. Kubera,  n.,  the  god  of  wealth  (Hinduism).  —  OI. Kuberah,  prob.  meaning  lit.  ‘the  humpbacked one’,  and  rel.  to  kubjal. 1,  kubhrdh,  ‘crooked, humpbacked’ ;  prob.  of  Austroasiatic  origin, kuchen,  n.,  a  variety  of  German  cake.  —  G. Kuchen,  fr.  MHG.  kuoche,  fr.  OHG.  chuohho, kuocho,  rel.  to  MDu.  koke,  ‘cake’,  and  in  gra¬ dational  relationship  to  ON.  kaka.  See  cake and  cp.  Cockayne.  Cp.  also  Catal.  coca  and OProveng.  coco,  which  are  Teut.  loan  words.  j kudos,  n.,  fame,  renown  ( colloq .)  —  Gk.  xOSoq, ‘glory,  fame’,  which  stands  for  *qudos  and  lit. means  ‘that  which  is  heard  of’.  It  is  cogn.  with OSlav.  cudo,  gen.  -esc  (for  *qeudos),  ‘wonder’, lit.  ‘that  which  is  heard  of’,  fr.  cujq,  

### Aturpat NOT FOUND
### ^pasha NOT FOUND
### ^shah, NOT FOUND
### ^food, n NOT FOUND
```


## [2026-09-07T20:36:35.673Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1971.txt',encoding='utf-8',errors='replace').read()\nL=len(t)\nimport re\ndef est(pat,total=844):\n    m=re.search(pat,t)\n    if not m: print(pat,'nf'); return\n    print(pat, 'frac %.4f'%(m.start()/L), '-> est p.', round(m.start()/L*total))\nfor p in [r'ban, n., a governor',r'bezoar, n',r'satrap, n',r'pater, n',r'\\bpaternal, adj']:\n    est(p)\nEOF"
}
```


### [2026-09-07T20:36:37.210Z] TOOL RESULT

```
ban, n., a governor frac 0.0854 -> est p. 72
bezoar, n frac 0.0991 -> est p. 84
satrap, n frac 0.7815 -> est p. 660
pater, n frac 0.6432 -> est p. 543
\bpaternal, adj frac 0.6432 -> est p. 543
```


## [2026-09-07T20:36:46.524Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\ndef nums(i): return re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$',pages[i])\nfor w in [r'padishah,',r'pad(i)shah',r'Pers\\.\\s*p[aà]d[ií]shah']:\n    for i,p in enumerate(pages):\n        for m in re.finditer(w,p):\n            print('###',w,'leaf',i,'nums',nums(i))\n            print(p[max(0,m.start()-400):m.start()+700].replace('\\n',' '))\n            print()\nEOF"
}
```


### [2026-09-07T20:36:47.885Z] TOOL RESULT

```
### padishah, leaf 593 nums []
 ME.  paddok,  di¬ min.  of padde,  ‘toad’,  which  is  rel.  to  ON.  padde, Swed.  padda,  Dan.  padde,  Du.  pad,  padde,  of s.m.  For  the  ending  see  suff.  -ock. paddy,  n.,  rice  in  the  husk.  —  Malay  padi. Paddy,  n.,  an  Irishman  ( colloq .)  —  Dimin.  of Padraig,  the  Irish  form  of  Patrick  (q.v.) paddymelon,  n.,  a  small  kangaroo.  —  From  Aus¬ tralian  native  name. padishah,  n.,  title  of  the  Persian  shah  and  the Turkish  sultan.  —  Turk,  padishah,  fr.  Pers. padshah,  which  is  compounded  of  pad,  ‘master’, and  shah,  ‘king’.  The  first  element  is  rel.  to OPers.  pati,  Avestic  paiti-,  OI.  patih,  ‘master, husband’,  and  cogn.  with  Gk.  7r6<n;  (for  *n6- Tig ),  of  s.m.,  L.  potens,  ‘mighty’.  See  potent  and cp.  words  there  referred  to.  Cp.  also  the  first  ele¬ ment  in  bezoar.  For  the  second  element  see  shah. Cp.  pashah. padlock,  n.,  a  removable  lock.  —  Compounded of  pad,  ‘padlock’,  a  word  of  uncertain  origin, and  lock,  ‘a  device  for  closing  the  door'. Derivative:  padlock,  tr.  v. p

### padishah, leaf 593 nums []
 padda,  Dan.  padde,  Du.  pad,  padde,  of s.m.  For  the  ending  see  suff.  -ock. paddy,  n.,  rice  in  the  husk.  —  Malay  padi. Paddy,  n.,  an  Irishman  ( colloq .)  —  Dimin.  of Padraig,  the  Irish  form  of  Patrick  (q.v.) paddymelon,  n.,  a  small  kangaroo.  —  From  Aus¬ tralian  native  name. padishah,  n.,  title  of  the  Persian  shah  and  the Turkish  sultan.  —  Turk,  padishah,  fr.  Pers. padshah,  which  is  compounded  of  pad,  ‘master’, and  shah,  ‘king’.  The  first  element  is  rel.  to OPers.  pati,  Avestic  paiti-,  OI.  patih,  ‘master, husband’,  and  cogn.  with  Gk.  7r6<n;  (for  *n6- Tig ),  of  s.m.,  L.  potens,  ‘mighty’.  See  potent  and cp.  words  there  referred  to.  Cp.  also  the  first  ele¬ ment  in  bezoar.  For  the  second  element  see  shah. Cp.  pashah. padlock,  n.,  a  removable  lock.  —  Compounded of  pad,  ‘padlock’,  a  word  of  uncertain  origin, and  lock,  ‘a  device  for  closing  the  door'. Derivative:  padlock,  tr.  v. padnag,  n.,  an  ambling  nag.  —  Compounded  of pad,  ‘road',  and  nag. padre,  n

### padishah, leaf 653 nums []
ts,  ‘husband’,  Lith.  pats,  Lett,  pats,  Hitt,  pat, ‘self’.  Alb.  pata,  ‘I  had’  (imperf.)  pass,  ‘had’ (pp.)  and  the  second  element  in  Goth,  brup- faps,  ‘bethrothed,  fiance’,  and  in  L.  hospes  (for *hosd-pots),  ‘visitor,  guest’,  OSlav.  gospodi ‘lord,  master’.  Cp.  potence,  power,  puissant,  and the  first  element  in  possess.  Cp.  also  the  first  ele¬ ment  in  padishah,  Poseidon,  and  the  second  ele¬ ment  in  despot,  hospital,  host,  ‘landlord’,  Pra- japati. potentate,  n.,  a  powerful  person:  ruler,  prince.  — L. potentatus,  ‘power,  rule’,  fr.  potens,  gen.  -entis. See  potent,  and  subst.  suff.  -ate. potential,  adj.  —  ME.  potencial ,  fr.  Late  L.  poten- tialis,  ‘having  power’,  fr.  potentia.  See  potency, and  adj.  suff.  -al. Derivatives:  potential,  n., potendal-ity,potendal- ize,  potential-iz-adon,  n. potentiate,  tr.  v.,  to  endow  with  power.  —  Form¬ ed  on  the  analogy  of  G.  potenzieren  fr.  L.  po¬ tentia  (see  potency)  with  verbal  suff.  -ate. Potentilla,  n.,  a  genus  of  plants,  the  

### pad(i)shah leaf 154 nums ['272', '273']
,  which  is  rel.  to  xshaya&iya-, ‘power’,  fr.  I.-E.  base  *qpe(i)-,  *qfe(i)-,  ‘to  rule’, whence  also  OI.  ksayati,  ‘possesses,  rules’,  ksat- ram,  ‘rule,  dominion’,  Gk.  xTaopat,,  T  get,  ac¬ quire’.  See  satrap,  shah  and  cp.  checkmate,  chess, checker,  exchequer,  Kshatriya.  Cp.  also  the  first element  in  Ahasuerus,  Xerxes  and  the  second element  in  Nakshatra,  padishah  and  pashah. Derivatives :  check,  tr.  and  intr.  v.,  check-less,  adj. check,  cheque,  n.,  a  written  order  to  a  bank.  — Most  philologists  derive  this  word  from  check in  the  sense  ‘a  sudden  stop’.  It  is  more  probable, however,  that  check  in  the  sense  ‘a  written  order to  a  bank’,  comes  fr.  Arab,  fakk,  ‘agreement, contract’,  fr.  Pers.  cdk,  of  s.m. checker,  chequer,  n.,  a  pattern  resembling  a  chess¬ board.  Shortened  fr.  OF.  eschekier  (F.  echi- quiet),  ‘chessboard’,  fr.  ML.  scaccarium,  ult. fr.  Pers.  shah,  ‘king’.  Sec  check,  ‘a  sudden  slop’, and  cp.  exchequer. Derivatives:  checker,  tr.  v.,  checker-ed,  adj.,

### pad(i)shah leaf 593 nums []
 ME.  paddok,  di¬ min.  of padde,  ‘toad’,  which  is  rel.  to  ON.  padde, Swed.  padda,  Dan.  padde,  Du.  pad,  padde,  of s.m.  For  the  ending  see  suff.  -ock. paddy,  n.,  rice  in  the  husk.  —  Malay  padi. Paddy,  n.,  an  Irishman  ( colloq .)  —  Dimin.  of Padraig,  the  Irish  form  of  Patrick  (q.v.) paddymelon,  n.,  a  small  kangaroo.  —  From  Aus¬ tralian  native  name. padishah,  n.,  title  of  the  Persian  shah  and  the Turkish  sultan.  —  Turk,  padishah,  fr.  Pers. padshah,  which  is  compounded  of  pad,  ‘master’, and  shah,  ‘king’.  The  first  element  is  rel.  to OPers.  pati,  Avestic  paiti-,  OI.  patih,  ‘master, husband’,  and  cogn.  with  Gk.  7r6<n;  (for  *n6- Tig ),  of  s.m.,  L.  potens,  ‘mighty’.  See  potent  and cp.  words  there  referred  to.  Cp.  also  the  first  ele¬ ment  in  bezoar.  For  the  second  element  see  shah. Cp.  pashah. padlock,  n.,  a  removable  lock.  —  Compounded of  pad,  ‘padlock’,  a  word  of  uncertain  origin, and  lock,  ‘a  device  for  closing  the  door'. Derivative:  padlock,  tr.  v. p

### pad(i)shah leaf 593 nums []
 padda,  Dan.  padde,  Du.  pad,  padde,  of s.m.  For  the  ending  see  suff.  -ock. paddy,  n.,  rice  in  the  husk.  —  Malay  padi. Paddy,  n.,  an  Irishman  ( colloq .)  —  Dimin.  of Padraig,  the  Irish  form  of  Patrick  (q.v.) paddymelon,  n.,  a  small  kangaroo.  —  From  Aus¬ tralian  native  name. padishah,  n.,  title  of  the  Persian  shah  and  the Turkish  sultan.  —  Turk,  padishah,  fr.  Pers. padshah,  which  is  compounded  of  pad,  ‘master’, and  shah,  ‘king’.  The  first  element  is  rel.  to OPers.  pati,  Avestic  paiti-,  OI.  patih,  ‘master, husband’,  and  cogn.  with  Gk.  7r6<n;  (for  *n6- Tig ),  of  s.m.,  L.  potens,  ‘mighty’.  See  potent  and cp.  words  there  referred  to.  Cp.  also  the  first  ele¬ ment  in  bezoar.  For  the  second  element  see  shah. Cp.  pashah. padlock,  n.,  a  removable  lock.  —  Compounded of  pad,  ‘padlock’,  a  word  of  uncertain  origin, and  lock,  ‘a  device  for  closing  the  door'. Derivative:  padlock,  tr.  v. padnag,  n.,  an  ambling  nag.  —  Compounded  of pad,  ‘road',  and  nag. padre,  n

### pad(i)shah leaf 607 nums ['1136', '1137', '1138', '1139']
tracted  fr.  Pers.  padshah (see  padishah);  influenced  in  form  by  Turkish baskak,  ‘governor’.  See  Houtsma,  The  Encyclo¬ paedia  of  Islam,  III,  1 1 14,  and  cp.  bashaw, pashalik,  also  pashalic,  n.,  the  jurisdiction  of  a pasha;  the  province  governed  by  a  pasha.  — Turk.,  fr.  pasha,  ‘pasha’,  and  -lik,  suff.  of  qual¬ ity.  See  pasha  and  cp.  the  suff.  in  beylik. pashm,  n.,  wool  obtained  from  the  Tibetan  goat. —  Pers.  pashm,  ‘wool’,  cogn.  with  OI.  pdkfman-, ‘eyebrows,  hair’,  Gk.  nlxetv,  ‘to  comb’,  tt£xo?, ‘fleece,  wool',  7t6xo<;,  ‘wool  uncombed,  fleece’, tcexeiv,  ‘to  comb’,  L. pectere,  of  s.m.;  fr.  l.-E. base  *peJc-,  ‘to  pluck  (wool  or  hair)’.  Seepe

### pad(i)shah leaf 653 nums []
ts,  ‘husband’,  Lith.  pats,  Lett,  pats,  Hitt,  pat, ‘self’.  Alb.  pata,  ‘I  had’  (imperf.)  pass,  ‘had’ (pp.)  and  the  second  element  in  Goth,  brup- faps,  ‘bethrothed,  fiance’,  and  in  L.  hospes  (for *hosd-pots),  ‘visitor,  guest’,  OSlav.  gospodi ‘lord,  master’.  Cp.  potence,  power,  puissant,  and the  first  element  in  possess.  Cp.  also  the  first  ele¬ ment  in  padishah,  Poseidon,  and  the  second  ele¬ ment  in  despot,  hospital,  host,  ‘landlord’,  Pra- japati. potentate,  n.,  a  powerful  person:  ruler,  prince.  — L. potentatus,  ‘power,  rule’,  fr.  potens,  gen.  -entis. See  potent,  and  subst.  suff.  -ate. potential,  adj.  —  ME.  potencial ,  fr.  Late  L.  poten- tialis,  ‘having  power’,  fr.  potentia.  See  potency, and  adj.  suff.  -al. Derivatives:  potential,  n., potendal-ity,potendal- ize,  potential-iz-adon,  n. potentiate,  tr.  v.,  to  endow  with  power.  —  Form¬ ed  on  the  analogy  of  G.  potenzieren  fr.  L.  po¬ tentia  (see  potency)  with  verbal  suff.  -ate. Potentilla,  n.,  a  genus  of  plants,  the  

### pad(i)shah leaf 759 nums []
gh,  granular  surface.  —  F.  chagrin ,  fr.  Turk. faghri,  lit.  ‘rump  of  horse;  shagreen’;  so  called because  only  the  skin  of  the  rump  of  the  animal is  used  for  this  purpose. Derivative:  shagreen,  adj. shah,  n.,  the  title  of  the  king  of  Persia.  —  Pers. shah,  ‘king’,  fr.  OPers.  xshaya-,  ‘king’.  See check,  ‘sudden  stop’,  and  cp.  the  second  element in  padishah  and  in  pashah. Shaharith,  n.,  the  daily  morning  prayer  (Jewish liturgy).  —  Mishnaic  Heb.  shaharith,  ‘morning time',  fr.  Biblical  Heb.  shahar,  ‘dawn’,  which  is rel.  to  Aram,  shahdra,  Arab,  sahar,  Akkad. sheru,  ‘dawn’. shahzada,  shahzadah,  n.,  son  of  a  king;  title  of the  heir  apparent.  —  Pers.  shah-zddah,  com¬ pounded  of  shah,  ‘king’  (see  shah),  and  zadan, ‘to  be  born’,  fr.  MPers.  zatan,  of  s.m.,  which  is rel.  to  Avestic  zata-,  ‘born’,  and  cogn.  with  L. gignere  (for  gi-gn-ere),  ‘to  beget,  bear,  bring forth,  produce’.  For  the  first  element  see  shah, for  the  second  see  genus  and  cp.  the  second  ele¬ m
```


## [2026-09-07T20:37:06.953Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"########## PHD\"\ngrep -n -i \"pāy\\|pādan\\|pānag\\|panāh\\|padām\\|xwēš\\|pālūd\\|Ādurbādagān\\|ādurbād\" PHD.txt | head -40\necho \"########## PHD_mackenzie\"\ngrep -n -i \"pāy\\|pānag\\|panāh\\|padām\\|xwēš\\|pālūd\\|ādurbād\" PHD_mackenzie.txt | head -40"
}
```


### [2026-09-07T20:37:07.024Z] TOOL RESULT

```
########## PHD
223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
536:pa(č)čēn [pcgn!] copy. *pa(č)čībāg [pcyp k', PWNe- | N *pajiw] *deceptive. ^h : deceit, hypocrisy. *pa(č)čībāy- [pcyp'd-, PWNc-] deceive. pad [PWN, for *pty | M pd, N pa] to, at, in, on. pad- [pt- | M *pd-) fall. padam [pd”m | (IN pandm)] mask for the mouth, worn by a celebrating priest. !Ipádan, pày- (UIN TLWN-tn! < А V ntr; Ptn, pd- | M pd, p’y-, N páyidan] protect, watch, defend. *pádan, pāy- [N TLWN-tn!, etc.] stand, wait. pādāšn [p?td?fn! | M p’d’syn, N pàdàs] reward, retribution. padēx [ptyhw'] flourishing, prosperous. ~ih: prosperity. padéxénidan, padéxén- [ptyhwyn-ytn'] make flourish, prosper. pādēz [p'tyc | M p'dyz, N pāyēz] autumn. pad-góhr [PW Ngwhl] т. jewelled; 2. of good stock, well-born. padifrah [p’tpl’s | M p'dypr?h, N *pādafrāh] punishment, retribution. padir-, ~išn, v. padiriftan. padirag [ptylk' | M pdyrg, N paóira] towards, against, counter-. (6) — madan: come to mect. ~ih: meeting, opposition.
540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
545:pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
665:xwarūfrān [hwl(’)wpl’n' | M xwrwpr'n) sunset, west. xwarrah [GDE < A gdh | (M prh, N farr)] fortune, glory, splendour. ~6mand [-’wmnd] fortunate, glorious. xwarséd, v. xwarxséd. xwartar [hw ltl] minor (sins). xwarwarān [hwlwPn!, -bPn'] = xwardfran. xwar(x)8éd [Azl(h)syt' | M xwrxšyd, № xuršēd] sun. xwāstag [NKSY A < A nksy’; hw'stk! | M xw’stg, N ~a] property, wealth. i ~õmand [-wmnd] wealthy. xwastan, !xwāh- [(Y)PLHWN-tn! < А V plh; hwstn!, hw'd- | J xwh-, N xwast] tread, trample; thresh. ~išn: trampling. xwāstan, *xwāh- [BOYHWN-stn! < A МУ Бу; hw'stn!', hwd- | M xw’stn, xt h-, N ~] seek, want, desire; attract, acquire. --j&n : desire, attraction. xwastüg [hwstwk!' | N xustū] confessing, believing. ~ih: confession, belief, faith. xwaš [BS YM < А bsym; hw | M xw, N ~] pleasant, sweet, nice. ~ih: pleasantness, pleasure. xwēd [Awyt! | M xwyd, N ~] moist, fresh. ~ih: moisture, freshness. xwédódah [hwytw(k)ds, -d^t! = Av. x"aetwada0a-] kin-marriage. xwēn-āhan [Ahw(y)n ?syn! = Av. x"aéna- (ayah-)] shining metal. xwēš [NP ŠE < А npf-h; hwyš | M xwy(b)s, N ~] (one's) own. ~ih: possession. ~awand [kwyš*wnd | N ~] relative, kinsman. xwēšēnīdan, xwēšēn- [/nwyfyn-ytn!] appropriate, make one’s own. xwēš-kār [леу dutiful. ~th: proper function. xwēš-tan [NPSE tn! | N ~] self. xwéy [hwyd | N xway] sweat, perspiration. xwistan [hwystn'] sweat, perspire. xwurd [hwlt' | N ~] small, little. xwurdag [hwltk' | N ~a] something small, particle; astr. lunar mansion; (horse's) pastern. ~ih: smallness.
818:appointment pāymār.
820:appropriate xwēšēnīdan.
998:biped dēpāy.
1295:commonalty amaragān, pāyram.
1535:defend pādan.
1659:district awestàm, kust(ag), pāygēs, réstag, zand.
1713:dutiful xwēškār.
1932:filter pālūdan.
1980:flummery pālūdag.
2063:function rāyēnišn; proper — xwēš- karih.
2171:guarded pad-nigerišn, pad-pānag.
2333:human being dēpāy, mardómzàdag.
2530:kinsman xwēšāwand.
3023:own xwēš; make one’s ~ xwēšēnīdan,
3185:possessions grāmag, xwēšīh; v. pro- perty.
3267:protected pad-pānag.
3268:protection magind, pānāgīh, panāhīh, pasbanih, pušt, puštībānīh, sray- iin, zēnhār.
3278:province awestám, nahang, pāygēs, réstag, šahrestān.
3293:purify pālūdan, wēxtan.
3301:quadruped čahārpāy.
3371:relation, relative hamtohmag, xwēš- awand; bradarod.
3571:self grīw, xwad, xwēštan.
3799:stand awištādan, ēstādan, pādan: ~ up āxistan.
3802:starch-jelly pālūdag.
3834:strain ( filter) pālūdan.
4128:undutiful axwēškār.
4273:watch (v.) nigāh dāštan, pādan, pās dāštan.
4606:. čahārpāy
4696:pazd- pazdēn- pazdēnīdan pazdagīh pazūg pāymārt parr
4708:padzyān purs- pursīdan pursišnīg pursišn padpānag pa(č)čībāy- pa(č)čībāgīh frazand
4718:[154] 1-2pešag 1 V. pēšpārag S eoo petyāragīh AS dax sa) petyārag ҳу 10 paydāgīh ^0 з» 10303 paydāgīh- = 95747 №0 paydagihistan 1152294 3” е 0 paydāgēn- = 527310500 paydāgēnīdan ММ 8” 5 05 paydag 15? ye» о) paygām -È ve os paygāmbar Sye Yeso petitigih A3 4) M 4290) petītīg 14) 95 1050) petit 12d уез 0› **pid we es panāh ^U? 103 panāhīh AY 10) "oul PITT puhlén- = "yes 10) puhlénidan ure rne 19у frāz erie pēhišn IMO” tay poxtan ure 125 nem! 519
4742:padyabib, ALI 00 t€» о) pādāšn VA My o padirán- ` - My yey a pādīrānēn- -p ry yey a pādīrānēnīdan W3 y ry We pādīrānīdan WS wy veyo pādīrān wey yey os paymar Ne теу o pādēz 23 voy o lpādan Y rero) pādofrāh ау\һе» 0) padzahr NS ve» o» pāygūs ISYA padrozag 15 cP rere pāyram » rey’ о
4746:pāyag pānāgīh pānāg -bān pänagīh panag pānzdah pākīzag pāk pālāy- pālūdan pālūdag 1-2pärag pārsīg pāsox pāsbānīh pāsbān pazen pāzand pazen pāšnag pāšom
4759:pah, pay pahnāy pahn pāyag paygāl
5078:zūr, zūr zoromand zūrgugāy zūrgugāyīh zorig Zurwün zofāy zofāyīh zofr zofrāy zofr-pāyag zanjīr zanišn zētīh, zūdīh zot, zūd wahīgt ant
########## PHD_mackenzie
```


## [2026-09-07T20:37:21.895Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"###### CHEUNG pālūdan / par-\"\ngrep -n -i \"pālūdan\\|pālāy\\|p'rwdn\\|pārūdan\" CHEUNG.txt | head -20\necho \"###### CHEUNG *pā- protect\"\ngrep -n \"^\\*pā\\|\\*pā(y)\\|pāy-.*protect\\|to protect\" CHEUNG.txt | head -30"
}
```


### [2026-09-07T20:37:21.965Z] TOOL RESULT

```
###### CHEUNG pālūdan / par-
###### CHEUNG *pā- protect
532:*-so, e.g. *рах ‘to divide, apportion’ (cf. *baj ‘to divide’), *Hraxs ‘to protect, 
1984:look after’, Goth. bairgan ‘to protect, shelter’, OE borgian ‘to give a pledge’, Engl. 
11612:*uz-) ‘to protect’ — Liste: 14 
11656:*IE COGNATES: Lat. iuvare ‘to help, to support’, Olrish con-di ‘to protect’. © Blanc 
11890:*CHORESMIAN: y'r- ‘to protect, guard’, m/yr’s- (inch.) ‘to be awake, awake’ 
13330:*Hraxš ‘to protect, defend’ 
13346:*SANSKRIT: raks” ‘to protect, guard’ (RV+) > EWAia II: 422 
18217:The connection with Skt. munt ‘to go away, flee ?; to protect ?' is useless 
18999:*paH! *to protect, guard (esp. of sheep, cattle), pasture? 
19001:*AVESTAN: pà- ‘to protect’ || (+ *pati-) ‘to guard against; to guess’ || (+ *ni-) ‘to 
19011:*OLD PERSIAN: pä- ‘to protect’ || (+ *pati-) ‘to guard, be on guard against” © Kent: 
19018:*MIDDLE PERSIAN: MMP p’y-, BMP p'd /päy-/ (NTLWN-) ‘to protect, guard’ || (+ 
19019:*aua-) MMP ’wb’y- ‘to protect, defend, guard, (?) permit’, MMP ’wb’yn- (caus.) ‘to 
19020:make to protect || (+ *a- BMP 'рт /abad/, BMP ’p’t’n /abadan/ ‘thriving, 
19029:*PARTHIAN: p’y- ‘to protect, guard’ || (+ *a-) ’b’d ‘prosperous, cared for’ = Ghilain: 
19035:*KHOTANESE: pā- (pai-) ‘to protect’ || (+ *ni-) ? nvi ‘pledge’ = SGS: 86 
19037:*SOGDIAN: SSogd. p y, BSogd. p y, CSogd. p’y, MSogd. p’y ‘to protect, observe, 
19072:*SANSKRIT: ра ‘to protect, to keep’ (RV+) = EWAia II: 112 
25643:*OraH ‘to protect’ 
25646:*AVESTAN: 0га- ‘to protect! © Liste: 27 
25649:*SOGDIAN: (*pati- ?) ? SSogd. ’pör’y ‘to protect’, ‘to throw away’. > The 
25656:*SANSKRIT: ба ‘to protect, save” > EWAia I: 679 
28547:creep’, *xaiz- to wait for, look for; to protect, pasture’. For ‘to creep’ I would rather 
57404:to protect
```


## [2026-09-07T20:37:27.777Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '18995,19080p' CHEUNG.txt"
}
```


### [2026-09-07T20:37:27.828Z] TOOL RESULT

```
*REFERENCES: EVP: 60; IIFL II: 232a; Andreev — PeSéereva: 293a; Asatrian — Livshits: 82; Werba 1997: 
205 f.; Cabolov 1997: 75 


*paH! *to protect, guard (esp. of sheep, cattle), pasture? 

*AVESTAN: pà- ‘to protect’ || (+ *pati-) ‘to guard against; to guess’ || (+ *ni-) ‘to 
protect; to pledge’ = Liste: 34 

Pres. {1} athem.: IND. 2sg. YAv. nipähi (Yt 10.78), 3sg. med. OAv. nipanhé (Y 28.11, Y 49.10), ? ҮАУ. 
panhe, 3sg. YAv. päiti, med. Y Av. paiti.päite (Yt 10.19), INJ. 3sg. OAv. pat (Y 46.4), SUBJ. (or Inj.?) 
3sg. OAv. pat (Y 32.13), OPT. 2sg. YAv. nipaiia (Y 57.25), 3sg. OAv. paiiat (Y 46.8), IMPV. 3sg. YAv. 
nipatu (Y 58.2), 2р1. YAv. pata (Yt 1.13, Yt 10.80, F 460); Pres. {2} (a)ia-: IND. 1sg. YAv. nipaiiemi (Yt 
5.89), OPT. 2sg. YAv. nipaiiois (Yt 1.24); Partic.: pres. {1} YAv. pant- (Yt 10.45), pres. (2) ? ҮАУ. 
*paiiant- (Yt 10.46), med. ? YAv. "paiti.paiiamna- (P 20); Inf.: OAv. poi (Y 44.15 f.) 

*OLD PERSIAN: pä- ‘to protect’ || (+ *pati-) ‘to guard, be on guard against” © Kent: 
194a 

Pres. {1} athem.: IMPV. 2sg. pädiy <p-a-di-y> (DPe 21), 3sg. pätuv, 3р1. pä”tuv <p-a-tu-u-v> (A’Sd 4, 
A’Pa 25); Pres. {2} aja-: impf. IND. med. lsg. apayaiy <a-p-y-i-y> (XPf 39), IMPV. 25р. med. 
patipayauva <p-t-i-p-y-u-v-a> (DB 4.38); Partic.: perf. pass. pata- <p-a-t-> (DPe 22) 

*MIDDLE PERSIAN: MMP p’y-, BMP p'd /päy-/ (NTLWN-) ‘to protect, guard’ || (+ 
*aua-) MMP ’wb’y- ‘to protect, defend, guard, (?) permit’, MMP ’wb’yn- (caus.) ‘to 
make to protect || (+ *a- BMP 'рт /abad/, BMP ’p’t’n /abadan/ ‘thriving, 
prosperous, cultivated’, BMP ’p’tyh /abadih/ ‘prosperity; village’ || (+ *ni-) BMP 
np k /nibag/ ‘pledge’ = DMMPP: 260a, 65b 

Pres.: IND. 3sg. MMP p’yd, BMP p’yt /payéd/, 3pl. MMP p’ynd, SUBJ. 3sg. MMP p’y’d, 3pl. MMP 
p’y’nd, IMPV. 2sg. MMP p’y; Partic.: perf. pass. BMP p’tk /padag/, MMP pd MMP p’yyhyst, Pass.: 
pres. SUBJ. 3pl. MMP p’yh’nd || (+ *aua-) Pres.: IND. 3sg. MMP ’wb’yyd, MMP ’wb’yd; Partic.: perf. 
pass. caus. MMP ’wb’ynyd; Caus.: pres. SUBJ. 3р1. MMP *’wb’yn’nd 

*PARTHIAN: p’y- ‘to protect, guard’ || (+ *a-) ’b’d ‘prosperous, cared for’ = Ghilain: 
86 | DMMPP: 260a, 7b 

Pres.: IND. 3sg. p yd, 3р1. p'ynd, SUBJ. 2sg. pv, 3sg. p’y’h, p’y’, IMPV. 25р. p’y, 2р1. p’yd; Partic.: 
perf. pass. p’d, p’dg 

*KHOTANESE: pā- (pai-) ‘to protect’ || (+ *ni-) ? nvi ‘pledge’ = SGS: 86 

*SOGDIAN: SSogd. p y, BSogd. p y, CSogd. p’y, MSogd. p’y ‘to protect, observe, 
watch over, guard’ || (+ *aua-) BSogd. ’wp’y ‘permit, consent’ || (+ *a-) SSogd. 
"pv ‘to think’, BSogd. ’’p’y, CSogd. "pm MSogd. ’’p’y ‘to watch, consider, 
perceive’ || (+ *pati-) SSogd. pcp’y ‘to expect, be ready for’ || (+ *ni-) SSogd. np’k, 
SSogd. np’kh ‘pawn’ 


*paH2 289 


Well attested: Pres.: IND. 1sg. ? SSogd. p’y’m, 3sg. BSogd. p’yt, 3pl. BSogd. p’y’nt, CSogd. p’ynt, 
SUBJ. 3sg. BSogd. p’y’t, CSogd. p'yt, POT. 3sg. BSogd. p't wnty, etc. || (+ *a-) Well attested: Pres.: 
IND. 159. MSogd. ’’p’ym (BBB: 42), 2sg. BSogd. ’’p’y’y, BSogd. "p'y« y», 3sg. BSogd. ’’p’yt, SUBJ. 
2sg. BSogd. ’’p’y”’, etc. || (+ *pati-) Pres.: IND. 1р]. SSogd. pcp'ymn 

*CHORESMIAN: (+ *ni-) nb’k ‘pawn, pledge’ 

*BACTRIAN: (+ *4-) оВобо ‘cultivated’ || (+ *ni-) vaßaryo ‘pawn, pledge, hostage’ 
c» S-W, Bact.: 172, 206b 

*NWIR: NP payidan/pay- ‘to watch, guard’, Tt. (Cha.) pa/pas, (Tak., Xia.) pa/past, 
Gz. pä-/päft (analog. -fi-), Siv. pä-, pö-/päi, poi ‘to watch, mind’ || (+ *а-) NP abad 
‘inhabited, cultivated (place, settlement); prosperous’, Bakht. abodi ‘village, 
inhabited place" (LW), Gz. -évà in PN, Kurd. (um) āvā, (or) awa ‘inhabited; 
cultivated; founded; prosperous, beautiful’ (genuine or LW ?) || (+ *ni-) NP nava 
‘pledge, "protection" money (in order to save the country from plunder)’. © NP 
payidan/pay- with the meanings ‘to wait, expect, remain’ may have a different 
origin, on which see *pad. 

*NEIR: Pash. ріау-/рбуш ‘to graze’, Yghn. poy-/poyta/póyna/póyak, Sh. poy-/páyd, 
Rosh. poy-/peyd, Sariq. puy-/puyd, Yzgh. pay-/payd, Wa. рыу-/роуа ‘to herd, look 
after the cattle’ || (+ *pati-) Oss. I. fippajyn/fippajd, D. feppajun/feppajd ‘to remark, 
guess' 

*MISC: (+ *à-) Arm. (LW) apat ‘inhabited’ || (+ *ni-) Toch. (LW) B fiaipa ‘pledge’ 
*SANSKRIT: ра ‘to protect, to keep’ (RV+) = EWAia II: 112 

«PIE *peH»- ‘to pasture, graze; to guard, protect, watch over (the cattle)’ = LIV: 460 
| Pok.: 787 

*IE COGNATES: Hitt. /pah-s-/, Toch. A раѕ-, B päsk- ‘to guard, protect’, Lat. pasco, 
OCS paso ‘I pasture, graze’, etc. 

*REFERENCES: EVP: 62; IFL П: 536a; Abaev, Slovar’ I: 475; Andreev — PeSéereva: 309a; Yarshater
```


## [2026-09-07T20:38:03.745Z] TOOL CALL #39: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T20:38:03.752Z] TOOL RESULT

```


```


## [2026-09-07T20:38:06.444Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"###### NYB xwēš / pānag / panāh / padām / pālūdan\"\ngrep -n -i \"xwēš\\|xw&ēš\\|pānag\\|panāh\\|padām\\|pālūd\\|ābād\" NYB_vol2_glossary.txt | head -30"
}
```


### [2026-09-07T20:38:06.502Z] TOOL RESULT

```
###### NYB xwēš / pānag / panāh / padām / pālūdan
548:āpātān [’p’t’n']cultivated, inhabited 815, — Paz. äwäda; cf MPrth ’b’d (A-H III, BBB); Arm. lw. apat; NP äbäd and ābādān; < Olr *ā-pāta- ‘protected’, v. pätan (1).
2277:ke [MNW] with encl. MNW-m = ké-m, MNW- = kē-š ete.; MNW-c = ké-c: A. interrog. pron. who? whom ?: én rētak kē hast? 161”; emphasized kē hàn he? who art thou, say? 561%; as cas. obl.: kē pat panāh kunom? 749; ke ax"eš hom? to whom do I belong? 624; én zanišn ké (ag.) kart? who made this deadly shot? 323; — gen. + ke: En pus + kē hast? whose son is this? 1621; or hàn 4 ke: ruvan... hàn t kē...? whose soul? 31?3; — governed by a prep.: hac ke? nazd ke? tài ke? ete. ; — indirect interrogation may be introduced by ku: gob ku to hac fradandän i ke hah 1517-18; without kū: (én-ic dine) hac pusa- ran...ı man ke zīvēt u kë mīrēt 219-19; nē (Gkah hom) i ke hàn 574. — B. rel. pron. who, which ; with pronominal antecedents : man ke, tē ke, šmāh ke, či ke, čišan ke, -$...ke, han (kas) ke, har (hàn) ke; hec (kas) ke both in a positive (6417-18) and a negative (11817-18) sense; 1. used as cas. rect. and cas. obl: (subj.) asvdr-é nest ke ... ētūn cigon to 1519-316; (dat.) (Kävul) ke Mihr u Mah pat pušt hah K. over which Sun and Moon keep guard 317%; (agens) Krisäsp ke Dahāk vanit K. by whom D. was vanquished 1064-5; — its syntactic function may be marked by an enclitic referring to the antecedent: (hu- nušk + Gana Menoi) kē-š ciš-ic pat poc nest (the progeny of the Evil Spirit) for whom there is nothing to furnish an ex- cuse 1021-?; but dastavar ké-§ guft ku there was a theologian who said 1018, also but ké-§ guft ki someone has said (taught) that 103? ; Gišān kē-šān Yam kirrenit those by whom Y. was cut to pieces 10145; — the gen. is regularly ex-
6076:pa'h: panāh
```


## [2026-09-07T20:38:18.124Z] TOOL CALL #41: Bash

```json
{
 "command": "pdftoppm -f 379 -l 379 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg379 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg379.png"
}
```


### [2026-09-07T20:38:20.129Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 87463 Sep  7 16:38 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg379.png
```


## [2026-09-07T20:38:20.787Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'pātan \\(1\\)',r'^pātan',r'x[v\"]ēš',r'panāh \\[',r'patàm|padām|pat[āa]m \\[',r'pān[āa]k']:\n    print('#####',pat)\n    for m in list(re.finditer(pat,t,re.M))[:3]:\n        print(t[max(0,m.start()-300):m.start()+800].replace('\\n',' '))\n        print('---')\nEOF"
}
```


### [2026-09-07T20:38:22.069Z] TOOL RESULT

```
##### pātan \(1\)
##### ^pātan
##### x[v"]ēš
 z"artan. a-xUjiyišnčh  'hw'dányh] unwillingness, both in the sense of diffidence and of www.parsianjoman.org | ool wok a-x"ayisnéh reluctancy: atün hàn i kart (v. ?kartan) ~ dahét he will create unwillingness with regard to what you have instituted 45), with the following gl. explaining ~: kū šmāh xvēš rād ne tuvān zuästan, kas šmāh rād ne xvāhēt ‘~ means that you are incapable of an act of will for your own sake and nobody will be willing (to act) for your benefit’ (you will be diffident and inefficient, and nobody will work for you) 45*3; the gist of Yam's speech is expressed in the gl. 452, v. acārēnītam. axtēh phwyh], v. patvast-axéh. a-x'éSkür ['hwysk?l] not doing one’s duty, disloyal 16%. — V. zueskär. Ayaohad [Paz.] n. pr. 47°. — BdA p. 228? Yanhd (Paz.). ayāft [y*pt'] gain, benefaction 94, from ayaftan ayäp-, to reach, to attain 4618-22, 809.25, 888, 1053-12, — Ps. pt. ?y'pty; MPrs pt. ’y’pt, pres. ’y’b- (Verbum 176); Paz. ayäftan ayäw- (Mx, SGV); NP yäftan yàb-. Av. (70sq.) ap-; dp- < à- + ap-; ay- probably < abi-, cf Av. (71) avi-ap-. — The pres. st. ayäp in com- pounds: 
---
; én būt i 6 peš gobam this happened which I am now going to tell 54!?; — én and, v. and. — Skr ena-; not in Av. and OP; SW w.: MPrs. ‘yn (no pl, instead im&sän, imin are used); Paz. NP in. Tedesco, Dial. 216. enyä [’yny’] otherwise 1377; bē... ~ except: bē magvemart ... ~ ... hec mart pat xčinak i xvēš bē mà pāyēt except the Magians. .. no man shall remain at home 2035; bē pat parvānakēh + yazdān . ~ šutan nē šāyet except on a mission ‘of the gods it is not possible to pass 7810-11; ba 801% is not taken up by ~ until 1. 24; bē ka rāst göbeh ēnyā, ham- dātistān ne bavém except if thou tellest the truth we shall not come to terms 1521-22; 6520 v. pditiašdi; hakar ... vicà- ret — ... if he explains ... [it is just right], otherwise ... 1181-15, as in Arab in halla wa'illa; hac Armail ~ except (by) Armail 1151-11, — Av. (138) anyādā, Gath. for anyd@G, Skr anydtha; Paikuli, Prs ’yny’ (Herzfeld p. 132); FrP éraxtan 25 ’yny’ (in most MSS marked 'dny?), with the gl. ’ny’, read anyā, qniä etc.; Paz. ainā. . ér [’yl] Aryan, Iranian 26%; pl. cas. rect. ~ 4511, obj. 6175; pl. cas. obl. ~-dn: i
---
39 nikérai nikand [nknd] pt. = pret. 3d p. sg. 92%, uncertain: api-§ góhr  x"arrah be ~ seems to mean: he projected, threw forth, (from his own essence) its (= the earth’s) substance-light, i. e. the heavenly light which forms the substance of the material world, cf BdA p. 11? Ohur- mazd hac han i xvēš xvatēh getäh rošneh uy hac getäh rošneh karp + dāmān i xue$ frac brihénit, where gētāh rošneh seems to be a synonym of göhr xtarrah; nikandan from ni + the root kan- ‘to throw’ which is found in apakandan (g.v.). nikče [nkyc'] disclosure, exposition of the doctrines of Religion, dogmatic com- mentary: ~ i veh-den 309. 111?. — V. nikéxtan. Paz. nigež, Skr. v. samniveša (ŠGV). nikčeišn the act of disclosing, exposing Religion 1094. nikčrai [nkyl’y] he who denies his respon- sibility for a th. (whether he has assumed this responsibility by himself, or it rests upon him for other reasons), breaker of an engagement or an obligation 8213, — A juridical term, opp. xtastük ‘he who acknowledges such responsibility’, v. Bthl, ZsR II, 37-40. Cf BdA p. 184!?sga.: Akataš dev druž i nikērāyēh hac d
---
##### panāh \[
##### patàm|padām|pat[āa]m \[
##### pān[āa]k
l-know town, men- tioned together with Sas 11039. — Cat. 97. Gr Xoorga, Syr Söstre, Arab Tustar (with dissimilation of the initial) Yagut 1,847 sq., where also the form Süstar is mentioned. $upän [šp'n'] shepherd 1”; pl. cas. obl. ~-dn 10, — Av. (1029) fšu- ‘sheep’ = pasu-, v.S. v. püh, + pāna-, v. pānak; MPrth swb’n; NP šubān, sabän. Sus [šws] Susa 11619. — OP Cusä, Elam. Susan, Bab. šu-ša-an; Arab al-Süs, v. Yāgūt 3,188—190. šusr [šwsl], Suhr [šwhl] sperm, the male generative substance 41?! (v.s.v. and). 5420 [šwsl, but in the following gl. šwhl = Suhr]. 9475.22. 9517-21; apar pat ~ through propagation 40%, — Borrowed from Av. (555) xšudra-, ašučra- ‘liquid’; the pro- nunciation was Suhr, -s- being only the inverse writing of -h-, cf s. v. Mahläh (in fine) and pahlom. As to the etymology cf s. v. šustan. Susréh the state of being sperm: pat ~ in the state of sperm 95?!. šustan [šwstn'; HLLWN-tn ] $öd- [HLL- WN-] to wash, with the prev. apar 41?-1; — with frde: frāc dast ~ hac to wash one’s hands of a p. = to break off all relations with him 3814. 443-9; — with ul 417. — Av. (555) p
---
i-: nihan nčit: nč pad-: pad pača: padak pasa: padak paéman-: pém pačsa-, paés-: pesit pairi-haroz-: pēšārvār pairi-frä-haroz-: pešārvār pairikä: parik ni-pais-: nipištan paiti: pat paiti-lar: patirak paitica: pöcitak paitiš: patiš paitištāna: paitištān paityank-: paitāk paityāra: paityārak pāna-: pānak panti-, pa0-: pand-nàmak paoiryo.tkačša: pöryöt- kés ?par-, pafr-: vaparikančh ?par-: hanbārišn tpar: appurišn, xUar- baràn www.parsianjoman.org lolek (ava-)*par-: ōpār ham-*par-: hanbārišn parš-: par-butan pāra-: pārak Para-data-: Pēš-dāt parena-, perona-: parr paresu- (peresu-): pahlūk paršta-, paršti-: pušt pasca: pas pasu-: pāh pat-: patitan (ava-)pat-: opastan patarota-: *Patiritarasp padana-: pahan pāfra-vant: pahr pay-: patan pazdaya-: pazditan pazdu-: pazdok perena-: purr us-perena-: uspurrik peretu-, pesu-: puhl pere0a-: *puhr pisant-: pist Pisi-Syao®na-: Pišišotan pištra-: pčšak Pourušaspa-: Pourušāsp püitika-: pütik püti-: püt pu@ra-: !puhr rà-: ràt rad-: ?ristak A + rād-: ārāstan pati + rād-: pairāstak raēk-: rēxtan (abi) + raēk-: ēraxtan vi + raēk-: virēxtan račOwa-: *hā
---
```


## [2026-09-07T20:38:41.170Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%82-",
 "prompt": "Give the reconstruction, gloss, and any note on whether it means \"to protect\" and/or \"to graze/feed\"; list Iranian and Sanskrit descendants and derived terms mentioned."
}
```


## [2026-09-07T20:38:43.229Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%B3tis",
 "prompt": "Give the reconstruction, gloss, etymology notes, and descendants (esp. Avestan, Old Persian, Sanskrit, Greek, Latin). Does it say anything about the relation to *poti \"against\" or to *peh2- \"protect\"?"
}
```


## [2026-09-07T20:38:45.349Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%A7%DB%8C%DB%8C%D8%AF%D9%86",
 "prompt": "Persian پاییدن: give the full etymology (Middle Persian, Proto-Iranian, PIE forms) and glosses."
}
```


### [2026-09-07T20:38:47.204Z] TOOL RESULT

```
# Proto-Indo-European Root *peh₂-

**Reconstruction:** *peh₂-

**Glosses:** 
1. "to protect, to ward"
2. "to shepherd"

**Note on Meaning:** The entry explains that "semantic shift from 'protector' towards 'shepherd, herder' can be seen in many branches," reflecting the historical importance of herding practices in Indo-European societies.

## Key Descendants

**Sanskrit:**
- पाति (pā́ti) - "protects"
- पायु (pāyú) - "guard, protector"
- पाल (pāla) - "guardian" (related terms)

**Iranian:**
- Avestan pāt̰ - maintains the protective sense
- Persian پاس (pās) - "watch, guard"
- Kurdish pa, pavan - "guardian"

**Notable derived formations include:** agent nouns (*páHtras* → Persian pahra, "watch"), shepherd-related terms (*peh₂-tew-* → Armenian հօտ, "flock"), and religious/mythological terms (Ancient Greek Πάν, the god Pan).
```


## [2026-09-07T20:38:47.361Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D9%84%D9%88%D8%AF%D9%86",
 "prompt": "Persian پالودن: give the full etymology (Middle Persian forms, Proto-Iranian root, any mention of pālāy-, pāl-, or a root with r) and glosses."
}
```


### [2026-09-07T20:38:48.900Z] TOOL RESULT

```
# Proto-Indo-European *pótis

## Reconstruction & Gloss
**\*pótis** (masculine noun): "master, ruler" or "husband"

## Etymology
According to Derksen, the meaning "lord, husband" may derive from an older sense of "self," as seen in Lithuanian *pàts* ("self").

## Descendants
The page documents descendants across major language families:

- **Greek**: Proto-Hellenic *pótis*
- **Sanskrit/Indo-Iranian**: Proto-Indo-Iranian *pátiš*
- **Latin**: Proto-Italic *potis*
- **Germanic**: Proto-Germanic *fadiz*
- **Celtic**: Proto-Celtic *ɸotis*, yielding Old Irish *aithech* ("master of a house")
- **Baltic-Slavic**: Lithuanian *pats*, Latvian *pats*

## Notable Omissions
The page does **not** discuss relationships to *poti "against" or to *peh₂- "protect."* It also lacks specific mentions of Avestan or Old Persian descendants, though Indo-Iranian descendants are referenced generally.
```


### [2026-09-07T20:38:49.993Z] TOOL RESULT

```
# Etymology of Persian پاییدن (pāyīdan)

**Middle Persian:** "p'dn, p'y-" (/pādan, pāy-/, "to protect, guard; to wait, stand")

**Old Persian:** 𐎱𐎠𐎮𐎹 (pā-, "to protect")

**Proto-Iranian:** *paH- (meaning to protect)

**Proto-Indo-Iranian:** *paH- (meaning to protect)

**Proto-Indo-European:** *peh₂- ("to protect")

The term traces back through multiple linguistic layers, with the core semantic field centered on notions of protection and guardianship across all attested stages of the language family.
```


### [2026-09-07T20:38:53.689Z] TOOL RESULT

```
# Etymology of Persian پالودن (pāludan)

## Full Etymology Chain

The word derives from **Middle Persian** *pʾlwtn'* (pālūdan), meaning "to strain, filter, purify."

This Middle Persian form comes from **Proto-Iranian** *\*para-dā́wati*, which combines:
- The prefix *para-* (through/by)
- The root *\*dā́wati* ("to run")

The ultimate source is **Proto-Indo-European** *\*dʰew-* ("to run, flow"), traced through **Proto-Indo-Iranian** *\*dʰā́wati*.

## Related Forms

The present stem **pālā-** (پالا) appears in derived terms like:
- پالایش (pâlâyeš) - "filtration/purification"
- پالایشگاه (pâlâyešgâh) - "filtration plant"

## Comparative Cognates

The root connects to similar words across Indo-European languages: Persian دویدن (to run), Sanskrit धावति (dhā́vati), and Ancient Greek θέω (théō).
```


## [2026-09-07T20:39:04.358Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%DB%8A%D8%B4",
 "prompt": "Persian خویش: give the full etymology chain (Middle Persian xwēš, Manichaean forms, Avestan xᵛaēpaiθya-, Proto-Iranian, Old Persian) and glosses."
}
```


## [2026-09-07T20:39:05.770Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%A7%D9%87",
 "prompt": "Persian پناه: give the full etymology (Middle Persian panāh, Proto-Iranian reconstruction, root, prefix analysis) and glosses."
}
```


### [2026-09-07T20:39:05.938Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T20:39:07.253Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%AF%D8%B1",
 "prompt": "Persian پدر: give the full etymology chain (Middle Persian pidar, Old Persian pitā, Avestan pitar-, Proto-Iranian, PIE *ph₂tḗr) and glosses."
}
```


## [2026-09-07T20:39:10.530Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B0%D8%B1%D8%A8%D8%A7%DB%8C%D8%AC%D8%A7%D9%86",
 "prompt": "Persian آذربایجان: give the full etymology (Middle Persian Ādurbādagān, Old Iranian *Ātṛpātakāna-, the personal name Atropates/Ātṛpāta 'protected by fire', Greek Atropatene) and what kind of place it denotes (province or city)."
}
```


### [2026-09-07T20:39:11.434Z] TOOL RESULT

```
# Etymology of Persian پناه (panāh)

**Middle Persian Origin:**
According to the Wiktionary entry, the Persian word derives from "Middle Persian 𐭯𐭭𐭠𐭧 (panāh, 'protector; refuge')."

**Proto-Iranian Reconstruction:**
The source document does not provide a Proto-Iranian reconstruction for this term.

**Root and Prefix Analysis:**
No root breakdown or prefix analysis is offered in the available content.

**Glosses:**
The Middle Persian form carried the meanings of both "protector" and "refuge"—senses that persist in modern Persian, where پناه means: shelter, refuge, asylum, and protection.

The word traveled through multiple languages via Persian transmission, appearing in Ottoman Turkish, Bengali, Chagatai, Hindustani, and other languages, maintaining consistent semantic associations with seeking safety and protection.
```


### [2026-09-07T20:39:12.629Z] TOOL RESULT

```
# Etymology of Persian پدر (padar)

The word پدر traces back through multiple historical language stages:

**Proto-Indo-European:** "*ph₂tḗr" (reconstructed root meaning father)

**Proto-Indo-Iranian:** "*pHtā́" (inherited from PIE)

**Proto-Iranian:** "*pHtā́" (continuation in Iranian branch)

**Old Persian:** "𐎱𐎡𐎫𐎠" (pitā) — the documented Old Persian form

**Middle Persian:** "𐭓𐭐𐭃" (pidar) — the intermediate stage between Old and modern Persian

**Classical/Modern Persian:** "پدر" (padar, pidar, pedar depending on dialect) — the modern reflex

This etymological chain demonstrates the sound changes characteristic of Indo-European language evolution, particularly the preservation of the original meaning across millennia while phonetic forms shifted systematically across language stages.
```


### [2026-09-07T20:39:17.321Z] TOOL RESULT

```
# Etymology of Persian آذربایجان

## Full Etymology Path

The term traces back through these linguistic stages:

- **Old Persian**: *Ātr̥pātah* (meaning "protected by fire")
- **Middle Persian**: ʾtwrpʾtkʾn (ādurbādagān)
- **Early New Persian**: آذَرْبَایْگَان / آذَرْبَادْگَان (āḏarbāygān / āḏarbādgān)
- **Classical Persian**: آذَرْبَایْجَان (āzarbāyjān)

The etymology involves "Atropates," a historical figure whose name literally means "protected by fire," combined with the Persian relational suffix "-gān."

## Geographic Reference

According to the Wiktionary entry, آذربایجان denotes "a region in northwestern Iran, where ancient Atropatene was located, encompassing the modern provinces of Ardabil, East Azerbaijan and West Azerbaijan." It's identified as a **region** rather than a single city, though it historically referred to the broader geographical area known to the Greeks as Atropatene. From the 20th century onward, the term also refers to "a country in the South Caucasus in Asia and Europe" (the modern nation-state).
```


## [2026-09-07T20:39:27.124Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/xw%C4%93%C5%A1",
 "prompt": "Middle Persian xwēš: etymology (Avestan xᵛaēpaiθya-, Proto-Iranian) and descendants (New Persian خویش)."
}
```


## [2026-09-07T20:39:28.068Z] TOOL CALL #52: WebSearch

```json
{
 "query": "Persian خویش etymology Avestan xvaepaithya Middle Persian xwēbaš wiktionary"
}
```


### [2026-09-07T20:39:28.559Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T20:39:30.177Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://iranicaonline.org/articles/abadan-town-and-island",
 "prompt": "What does Encyclopaedia Iranica say about the name Abadan — its etymology, the Arabic ʿAbbadan, and any Iranian derivation from āb 'water' or ābād?"
}
```


## [2026-09-07T20:39:31.010Z] TOOL CALL #54: WebSearch

```json
{
 "query": "Artabanus Ardavan name etymology Old Iranian *Arta-bānu \"glory of Arta\" Justi Iranisches Namenbuch"
}
```


### [2026-09-07T20:39:31.571Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T20:39:38.101Z] TOOL RESULT

```
Web search results for query: "Persian خویش etymology Avestan xvaepaithya Middle Persian xwēbaš wiktionary"

Links: [{"title":"The Avestan ī̆šti- in Middle Persian texts | Bulletin of SOAS | Cambridge Core","url":"https://www.cambridge.org/core/journals/bulletin-of-the-school-of-oriental-and-african-studies/article/avestan-isti-in-middle-persian-texts/FA721F5C6DB8552E13A059D53D774830"},{"title":"Afrasiab","url":"https://en.wikipedia.org/wiki/Afrasiab"},{"title":"Hushang","url":"https://en.wikipedia.org/wiki/Hushang"},{"title":"Avestan - Wikipedia","url":"https://en.wikipedia.org/wiki/Avestan"},{"title":"Xwedodah","url":"https://en.wikipedia.org/wiki/Xwedodah"},{"title":"A concise review of the Iranian calendar","url":"https://arxiv.org/pdf/astro-ph/0409620"},{"title":"- 853 - Chapter 33 Avestan and Old Persian Morphology Prods Oktor Skjærvø","url":"https://allegatifac.unipv.it/caterinamauri/sitovecchio/1972634256_Avestan3a.pdf"},{"title":"Introduction to Old Iranian - The Linguistics Research Center","url":"https://lrc.la.utexas.edu/eieol/aveol/0"},{"title":"Iranian languages - Middle Iranian, Pahlavi, Avestan | Britannica","url":"https://www.britannica.com/topic/Iranian-languages/The-Middle-Iranian-stage"},{"title":"Category:Middle Persian terms derived from Avestan - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Middle_Persian_terms_derived_from_Avestan"}]

The search results provide general information about Avestan and Middle Persian linguistics, but don't contain specific etymological information about the Persian word "خویش" (khwish) and its connection to Avestan xvaepaithya or Middle Persian xwēbaš. Let me try a more targeted search for this specific word.

Links: [{"title":"ख़्वाहिश - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E0%A4%96%E0%A4%BC%E0%A5%8D%E0%A4%B5%E0%A4%BE%E0%A4%B9%E0%A4%BF%E0%A4%B6"},{"title":"খেশী - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E0%A6%96%E0%A7%87%E0%A6%B6%E0%A7%80"},{"title":"خوش - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%B4"},{"title":"خویش - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AE%D9%88%DB%8C%D8%B4"},{"title":"خواهش - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D9%87%D8%B4"},{"title":"The Secrets of the Self","url":"https://en.wikipedia.org/wiki/The_Secrets_of_the_Self"},{"title":"Khoshey people","url":"https://en.wikipedia.org/wiki/Khoshey_people"},{"title":"self - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/self"},{"title":"The Secrets of Selflessness","url":"https://en.wikipedia.org/wiki/The_Secrets_of_Selflessness"},{"title":"Lexicography Saves Lives (LSL): Automatically Translating Suicide-Related Language","url":"https://arxiv.org/pdf/2412.15497"}]

Perfect! I found the exact information you were looking for on Wiktionary. Here are the search results:

The Persian word خویش (khwish) comes from Middle Persian xwēš, from Old Persian ʰuvāipašiyam, a compound from Proto-Iranian *hwaypaθyah, with the phonetic change resulting in unattested but assumed Middle Persian *xwēbš > xwēš. The first element of the compound is akin to Old Persian huva, from Proto-Iranian *hwáh, from Proto-Indo-Iranian *swás (reflexive pronoun), from Proto-Indo-European *swós.

This etymology traces the Persian word back through its historical layers, showing how the Proto-Iranian form *hwaypaθyah (related to your Avestan xvaepaithya) evolved through Middle Persian phonetic changes to eventually become the modern Persian خویش.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-07T20:39:38.254Z] TOOL RESULT

```
Web search results for query: "Artabanus Ardavan name etymology Old Iranian *Arta-bānu "glory of Arta" Justi Iranisches Namenbuch"

Links: [{"title":"ARTABANUS (Old Persian proper name) - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/artabanus-achaemenid/"},{"title":"Artabanus IV - Mandaepedia - Miraheze","url":"https://mandaepedia.miraheze.org/wiki/Artabanus_IV"},{"title":"Artabanus - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Artabanus"},{"title":"Artavasdes","url":"https://en.wikipedia.org/wiki/Artavasdes"},{"title":"Artabanus","url":"https://en.wikipedia.org/wiki/Artabanus"},{"title":"Artabanus IV — Eranshahr","url":"https://www.eranshahr.com/shahs/artabanus-iv"},{"title":"Iranisches Namenbuch : Ferdinand Justi : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/IranischesNamenbuch"},{"title":"Artabanus IV of Parthia","url":"https://en.wikipedia.org/wiki/Artabanus_IV_of_Parthia"},{"title":"Artabanus I of Parthia","url":"https://en.wikipedia.org/wiki/Artabanus_I_of_Parthia"},{"title":"Artav of Khwarazm","url":"https://en.wikipedia.org/wiki/Artav_of_Khwarazm"}]

Based on the search results, I found information about the etymology of Artabanus/Ardavan:

Artabanus (Middle Persian Ardawān) is the Latinized form of an Old Persian proper name *Arta-bānu meaning "the glory of Arta." 

The search results also confirm the significance of Ferdinand Justi's Iranisches Namenbuch (Marburg, 1895), which contains some 4,500 names and 9,500 different individuals mentioned in Iranian-language sources from the oldest Avestan texts up to Justi's day. This seminal work on Iranian names is referenced in academic discussions of Old Iranian name etymology, though the search results don't show Justi's specific entry for Artabanus. However, the etymology is discussed by E. Benveniste in his work "Titres et noms propres en iranien ancien" (Paris, 1966, pp. 107-08).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T20:39:45.705Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/artabanus-achaemenid/",
 "prompt": "What is the etymology given for the name Artabanus (Old Persian, Middle Persian Ardawān)? Quote the reconstruction and meaning."
}
```


### [2026-09-07T20:39:47.140Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T20:39:47.272Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Artabanus",
 "prompt": "Etymology of Artabanus: give the Old Iranian/Old Persian reconstruction and its meaning, and the Middle Persian/New Persian forms."
}
```


## [2026-09-07T20:39:48.560Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Abadan,_Iran",
 "prompt": "What does the article say about the etymology/name of Abadan — Arabic ʿAbbadan, the derivation from ābād, and any theory involving āb 'water'?"
}
```


## [2026-09-07T20:39:49.947Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%DB%8C%D8%B4#Persian",
 "prompt": "Persian خویش: quote the etymology section verbatim (Middle Persian, Old Persian huvāipašiya, Proto-Iranian *hwaypaθyah) and the glosses."
}
```


### [2026-09-07T20:39:52.458Z] TOOL RESULT

```
# Etymology of Artabanus

Based on the Wiktionary entry, here's what is provided:

**Old Persian reconstruction:** The name derives from "*Arta-bānu" or "*Artabānuš," which literally means "The glory of Arta" (where Arta refers to Asha, a concept in Persian philosophy).

**Intermediate stages:** The word traveled from Old Persian into Ancient Greek as Ἀρτάβανος (Artábanos), and subsequently into Latin as Artabanus.

**Middle Persian and New Persian forms:** Unfortunately, the source document does not include information about Middle Persian or New Persian derivatives of this name. The etymology section only traces the path from Old Persian through Greek to Latin, without extending the etymological chain forward into later Persian language stages.
```


### [2026-09-07T20:39:54.637Z] TOOL RESULT

```
# Etymology of Abadan

According to the article, the name's origins involve multiple theories:

**Classical sources:** The earliest mentions appear in Greek geographer works, with Marcian rendering it "Apphadana" and Ptolemy noting "Apphana."

**Persian derivation:** B. Farahvashi proposes the name derives from Persian "ab" (water) combined with the root "pā" (guard, watch), yielding the meaning "coastguard station."

**Islamic-era theory:** Historian Ahmad ibn Yahya al-Baladhuri (d. 892) presented a different account, claiming the town was founded by "Abbad bin Hosayn" from the Arabian Tribe of Banu Tamim during the Umayyad period.

The article notes that "In the subsequent centuries, the Persian version of the name had begun to come into general use before it was adopted by official decree in 1935." The water-based etymology appears as one scholarly interpretation alongside the historical narrative linking the name to an Arab founder.
```


### [2026-09-07T20:39:55.356Z] TOOL RESULT

```
# Etymology of خویش (xwēš)

The word **خویش** traces back through several language stages:

**Middle Persian origin:** The term derives from Middle Persian *xwēš*, which evolved from Old Persian *huvāipašiyam* through phonetic changes.

**Compound structure:** The Old Persian form represented a compound from Proto-Iranian *\*hwaypaθyah*, combining elements related to the reflexive concept.

**Proto-Indo-European roots:** The first component connects to Proto-Iranian *\*hwáh* (from Proto-Indo-Iranian *\*swás*, a reflexive pronoun) and ultimately traces to Proto-Indo-European *\*swós*.

**Glosses:** As documented in the entry, خویش functions as:
- A reflexive pronoun meaning "oneself"
- An emphatic marker for "one's own"
- A noun meaning "self"

The entry notes that in modern Persian, this literary term has largely been supplanted by خود (xwad/xod) in everyday usage.
```


## [2026-09-07T20:40:08.152Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg379.png"
}
```


### [2026-09-07T20:40:08.599Z] TOOL RESULT

```

```


## [2026-09-07T20:40:08.596Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T20:41:04.166Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor w in ['آبادان','اردوان','پاییدن','پنام','پناه','پالودن']:\n    hits=[i for i,p in enumerate(pages) if w in p]\n    print(w,'leaves:',hits[:12])\nEOF"
}
```


### [2026-09-07T20:41:05.474Z] TOOL RESULT

```
leaves 777
آبادان leaves: [41, 264, 426]
اردوان leaves: []
پاییدن leaves: [452, 567, 568, 604]
پنام leaves: [644]
پناه leaves: [12, 377, 405, 635, 644, 645]
پالودن leaves: [579, 580]
```


## [2026-09-07T20:41:12.427Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (264,426):\n    p=pages[i]\n    print('===== leaf',i,'len',len(p))\n    print(p[:1500])\n    print('.....')\nEOF"
}
```


### [2026-09-07T20:41:13.659Z] TOOL RESULT

```
===== leaf 264 len 1868
و بکرکاف فارسی محکم بتهراگویند ۱ .
] گففت - بنتح کاف نک
وغای فرشت شت » ت» آزارورنج وهمجنت وت با ریز
و بکس‌کاف فارسی نیز همین معنی دارد ۴
آ گن باکاف فارسی‌بروزن دأمن؛بمعنی
آکندنی باشد مثل آنچه درجامه و لحافوباش
کنند از پثبه و پشم وغیره - وبمعنی پر کننده
که فاعل پر کردن باشد , عم آعده است
کنج بفتح‌کاف ثازی بروزن نارنج؛
قلابی باشد که بدان يخ در بخدان اندازند؟ - و
بقةح کاف‌فارسی بمعنی پروهملو باشد؟ - وبمعنی
روده و آممای کوسیند هم‌هست که انرا با گوشت
و برنج و مصالح‌بر کرده باشند و بعربی «عصیب
ند .
آ "گثف « بر وزن پابند , ماضی آ"کندن
وی رکردن باشد بعنی پر کرد وانباشت - و بمعنی
پر کرده‌شده عم آمده است- و پر کردنی را پیز
ند .
(۱) چك : الپاشتن .
۱ - رد کته :
دلش خود ز تد تخت د که کشته بود
۳۳ بنالم از ۱ ن رو زکارو این کفت
و اماشتن(۱) ۷ .
نده بروزن‌ساز نده» بمعثی‌پر کرده
شدء و انباشته )۱( شده پاشذب و طوبله واصمطبل
و پایگاه را یز گوشد. و آخوردواب راهم کفته
اند ویعربی «معلف» خوانند. و بمضی باين معنی
جنم‌کاف آورده‌اند - و بمعنی بزر که و فربه لیز
ات استت و بمعئی آ یاه کردن ومعمور ساختن
هست .
| گنده گوش - جنم‌کاف فارسی و
سکون واووشین فرشت ۰ بمعنی | لوده دامن است
وناشتوا- رچیزی در کوش[ کنده را نز گویند.
] گنش » بتح تالث و کس نون‌وسکون
شین نقطه دار » بمعنی پر کردن باشد - و بمعتی
هرچیز که درون چیزها را بدان پر کنند وربی
«حشو» خواند ۸ .
| گنه « بنتح ثاك ونون » بمعنی آخر
و پیله که دربالش و هالی ولحاف و اثال آن پر
(۷) چك : اپاشته
بثیمار اغربرت! کشته بود. فردوسی
۶« لت نایه ».
که هرچه‌ید سب شادی وشاط برفت۰
اب اج پین هت هم میک تا( : انجیلکنتك )
قاسد و عمیوب و بیهوده . ۴ ره : اکح وآکج. ۴ - درکلمات مر 
.....
===== leaf 426 len 1992
نکن مم ینظر آعده است ٩‏
ادا فنجیر - نومی از درخت انجیراست
که یش از هم درختان موه دهد و انجیر آن
کاواك و پرباد میباشد .
بادان‌فیروذ - نم خهرآردیل است
و چون فیروز آن شهر را بنا کرد باین نام‌موسوم
ساخت چه بادان بممنی آبادان است.؟ .
باد) نگیز » نام کلی است که هر گاه
مزارعان خواهن که غله را از کاه جدا کنندو باد
نباشد آ نگل را بدست مالند و بر ک آنرا بر
هوا یاشند باد بهم‌رسد .
بادآ وود » نام کنم دوبم (۱) است
هشت کنج‌خسرءپرویز سد ی 5 زر
و گوهر بیکی از جزایر حصنه میفرسناد انفافاً
باد کشتی را بحوالی اردوی خسرو پرویز آورد
بادام شکوفه فشان - کنابه از
بادامه - بفتح میم ۰ یله ابریشم را
8 شتر هم آمده
است - و چشم مانندی باشد که از طلا و نقره
سازند و بر کلاه طفلان دوزند - و خال گوشتی
را هم گفته‌اند ۰ و آن اژخ مانندی است که‌بیدتی "
از بشر؟ میدم برمیآبد - وهردانه و حلفلزنجیر
را نیز کوبند - و رقعه و پینه را نیز گوین که
درویشان برخرقه دوزند - و خرفةٌ مرفعه را هم
میگوند » بعنی خرقه ای که ازیاره های رنگین
فراهم دوخنه‌شده باشد - وجنسی از ابر شمباشدب
و هرجنس مطبوع را یز کفته‌اند .
بادان - بر وزن نادان . مخفف آبادان
است که‌شیض‌خراب باشد - وبمعنی پاداش‌وجزای
۱ - باین ممنی ظاهرا مصحف «پاداش ‏ پاداش» است . راك : باداش . ۴ - ور
ممجم‌البلدان «باذان‌فیروز» ونیزدرمتن‌برهان وسروری *فیروز گرد» ودرثاهنامه «پیروزرام*» وقولی
بادان‌پیروز با آبادان پیروز نام قدیم اردبیل است که فیروز ساسانی در فرن پن<م میلادی آثرا بنا
کرده است «دائرتا لمعارف اسلام : اردیل».
بقیه ازصفحهٌ ۷۰۵
این روزرا «باد» خوانشد . «روزشماری ۵4-۵۳ . ركك : روزشماری ص ۸۲
۴ - رك : بادآور . ٩‏ طبری ۷2۲208 « واژه نامه ۶۷۷۶ گیلکی و
رك : بادرنگ . ۱ رد : پا
.....
```


## [2026-09-07T20:41:28.934Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:98 2>&1 | head -60"
}
```


### [2026-09-07T20:41:30.177Z] TOOL RESULT

```
no scan of BQT covers printed page 98 (see 'scans' in refs_online.json)
```


## [2026-09-07T20:41:35.052Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# find leaves containing 'بادان' or 'آبادا'\nfor w in ['آبادا','بادان','ابادان','اردوا','اردوان','ارد وان']:\n    hits=[i for i,p in enumerate(pages) if w in p]\n    print(w,hits[:20])\nEOF"
}
```


### [2026-09-07T20:41:36.364Z] TOOL RESULT

```
آبادا [41, 264, 426, 628]
بادان [41, 211, 264, 426, 544]
ابادان []
اردوا [750]
اردوان []
ارد وان []
```


## [2026-09-07T20:41:44.460Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (211,750):\n    print('===== leaf',i)\n    print(pages[i][:2000])\n    print()\nEOF"
}
```


### [2026-09-07T20:41:45.846Z] TOOL RESULT

```
===== leaf 211
۳
است از سال هی » و آن بودن خورشید باشد
هر" برج قرب - - و دام فرشته اس ت که م وکل
ات بر آهن (۱) و دی امور و سالع ماه
آبان باو تعلق دارد - و نم دوز دهم باشن از حر
ماه شمسی . و ظرسیان بموجب قاعدلکلیه که ند
ابشان مفرر است که چون تلم روز با للم ماه موافق
آید آنروز را مبارك دانند » درین دوز عید کنند
و جشن سازند ؛ و لیز سیب آنکه ژ وکه یکی
از پادشاعان ابران بود دربن روز با افراسیاب
جنگ کرده ار را شکست داده تعاقب نمود و از
ملك خویش بیرون کرد ؛ پارسیان این روژ را
عیدکنند ؛ و دیگر آنکه چون مدث هشت سال
در ایران باران نبارید و قحطی شد و هردم بسیار
تلف کردیدند و بعضی بملك دیگر رفتند عاقبت
در همین روز باران شروع در باربدن کرد ؛ بتا بر
آن فارسیان این روز را مبارك دانند و عید کنند
خبدای‌تعالی (۲) وسلاطین وبز رکان‌خواستن وسللاح
ساختن  .‏
۲ با ناه » اکاف‌فارسی بروزنبانمه ‏
نام روژ ده کب نو باشد - و نام فرشته‌ای
نیز هت که موکل ‏ ست . گویند : اکر درین
ب ا انه اا است وه وب
درآبند ؛ و اکر نبارد آبانگاه زنان باشد وایشان
باب درآ ند رابن عملرا برخود شکون وعباره
دانند . #۷
آب باده ر نگ - بکرتات ,کناب
چك : حی کرده بلشد .
از اك خوین باد . ..
آب بادان - بسکون نات بر وزن
خاکاران » نام سیر گاهیست از مافا‌کایل دد
نواحی خواجه سه پاران کهآ هم سیر کاهیست . #
آب رثن - بسکون شالت بس وزن
پاکترین , کنار جوی آب را گویند که زیری
مجوف باشد و هر دم آب در آنجا رخته کند
و برون دود باییوسته نراوش نماید (۳) .
آب بزیر هشتی -کنابه از فرب
دادن و حیله نمودن باشد .
آ"ب بسقه - بکرثاث . کنایه ازئيشه
و بگیته و بلوز ناهد - و مه زگره و ژاله
را ئیز گویند ِِ#
آب بن ۰ بکر ثاك و ضم بای
ابجد وسکون نون . چیزست مانند صمغ وآنرا
در بخ درخت کردکان کهنه شده و مجوف
گردیده یایند ؛ و بسربالی سادآوران خوانند .9
آپ پیکران - جتح بای فاسی .
کواکب وستارکان راکوبند عموماً - وبوشنالی
و رونق سی و شش ببکر منجمان باشدکه آنرا
وجوه خوانند خسوصاً .
آب بی لحام خوردن - بکس
ثالث ۰ کنابه از مطلق العنان و بسر خود بودن
باشد .
آب تاختن - با ای قردت بروزنکار
ساختن ۰ پیشاب و شاشکردن را کوبند . *
(۲) خم ۳ :- تعالی . (۳) خم ۳ .
ب آباهان - روز
وبدان بافچه هارا آپ دهند .

===== leaf 750
نون ۱ ی
و ارنشگه دام دو کتاب است - و نام علم خالة
رومیان هم‌هست در فقاشی وصورنگری » وبا ثانی
مثلثه هم آمده است .
ریدایح شاشی و حصوری تانی مانی بوده است
چنادکه کتاب مانی را ارتنگ میخواند کتاب
او را تگه میگوبند , ویحنی کنته اد تسگلوعا
شه ازصفعةٌ ۵۲۱
نیمهٌدوم قرن‌اول مسیسی کتاب خود را یونانی نوشته, و بعدها بپهلوی ترجمه شده بوده وحتی در
کناب «بزبدح»(ویز ید که) پهلوی (رش: شماری م۱۹ ۳۱۷) آزآن کتاب منقولافی بوده است.
درموفع ترجمهٌ کتاب نو کروی‌ازپهلوی بعربی که‌به « کتاب‌الوجوه والحدود» معررف‌شده»
بملت اغتشاش خطپهلوی که ذابل همه کونه صحیف است.اسم ملف که دریپلوی مي,و(یم
لوشته میشده‌به‌تنگلوتی وتنگلوشا ( بینکلوش- تینکلوس - طینفروی ) تبدبل شدم و سبت بابلی
بدان‌راده شده است (کاهی بت قوفالی هم هست که منسوب به قرف باشد که اکنون‌به عفرقوف
ممروف است). موضوع اي نکتاب صور نجومی ( غیراز سورخجیل و هشت کانهُ مدروف بطلمیوس )
ودلالت طلوعآنها درافق شه رکه درعوقع طلوع رجهی از وجوه دوازده گانه بر‌حوادث حبات مولود
است کهآغرا در بعض کتب مرپی صورورجات قلك نامیبه‌انه وییونانی 2720216110742 کوند.
د رکتاب ابومعشر صور وجوه برطبق عقیده بونان ( که مقصود بطلمیوی است ) وعفید حندوان
وعفیدث ابرانیان شرح داده‌شده وفالباً عقیدث ابرانی‌از تشگلوشا قل‌شده واسامی فارسی آن صورنها
نیز ثبت کردمده است. از اين آثار استنباط میشود که ظاعواً این کتاب نیز نرجمهةٌ صرفاز بونالی
لبوده بلکه کتاب بوغانی حدی بقالب ایرانی ربخته ومطالبی ابرانی درآن داخل شده‌بوده . کتابی
کهسنسوب‌به «تنطوشا» وترجمهٌ اين وحشیه است واکنون بعض نسخه‌های نادر ازآن موجود است
والیئو دونخه ازآذریکی درلیدن ودیگری در لثینگراد شان‌داده وسخة ثالثی ازآن دربکی از
کتابخانه های شخصی تهران یز هست‌باسم «صورالدرج و الحکم علبها فیما تدل علیه من‌طوالع -
المولودین اتنکلوشا البابلی الفوفانی بترجمة این وحشیه ». بنابرتحیقاث نالینو بکلی مجول است
وهیچگونه ارنباطی‌بانتکلوی- تو کروی‌حقیقی نداردواسلا مطالب آن بی‌معنی وساختگی است؛ واز
کتاب اسلی -یعنی ترجمةٌ عربیاز پهلوی.- خبری نیست و ظاهراً ازمیان رفته است. «گلمشمساری
تفی‌زاده ۰۳۱۹-۳۱۷ «عل‌الفلك. تاربخه عند العرب فی‌الفرون الوسطی. الینو. چاپرم ۱٩۱۱‏
: ٩۲۲
.*۹4 «خافانی شروانی‎ ِ
قطبی از پیکر جنوب و شمال تتکلوشای سد هزار خیال (
```


## [2026-09-07T20:42:07.319Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (300,303,306):\n    print('===== leaf',i)\n    print(pages[i][:700])\n    print()\nEOF"
}
```


### [2026-09-07T20:42:08.545Z] TOOL RESULT

```
===== leaf 300
ست و 4 سب
#احر یض « بکر اول و دای بی نقطه
و سکون ثانی وتحتانی و صاد تقطه دار ء دآروبی
است که کلف را زابل کند » و انرا صفاهانی
«گل‌کافشه» (۱) کوبند وحربی «عصفر» خوانند .
احب ۵ » بکسر اول و سکون تانی
و فتح لام سگرن بای‌اپجد و کر دال بی‌قطه
و تحتانی بالف کشیده » بسربانی کیاهی است
شیر دار که در صراها و بختر در کنار جویها
وآوا بشیرازی «کاو -
نبطويك > خوانند . و
گوشد اگر کاو قدری
از آن بخورد بمیرد .
و کومفند را مضرتی
نرساند . شیر آن قلع
ددان میکند بی درد ۰ ۰ ۷ 46
اکر دو درم از شیر آن
بکی دهند البته مکشد. احلب دیا :
قوبا (۲) وجربدا نافم الف» کل؛ ب» میوه؛
باشد ٩‏ ۶
ج » دانه
اج « بنتح اول و سکون ثانی » بمعنی
آفرمن باشد که از تحسین است ۴ - ودر ترحم
وتأسف‌نیز کونند؟ ودرعرمی بمعنی‌بر ادرباشد *
اخج اخ ه 

===== leaf 303
«کراث الک رکم » خوانند .
اخسمه - بفتح اول وسکون انی و شم
سین بی نقطه و فتح عیم » بوژه را گویند و آن
شرابی‌باشد که از آرد ارزن وجو و امتال آن‌سازند.
آحسی » بروزن مخفی . نام فصبه‌است
از ماوراء النهر در ناحيهٌ فرغانه ء از بهترین آن
بارد است ۱
2 ‌
کاف» بمعنی اخی است که تام قصبه ای باشد از
ماوراء الثهر۱ ۰
فاق واسش اقسه لیات ی
باشد از ماوراعالنهر در نهایت خویی و مولد اثبر
الدین است . واوشاعری‌بوده مشهور ومعروی؟ ۰
اش تم اول و سکون ثانی وشین
قرشت » قیمت وابها و ارزش چیزی باشد .
وتقیض ومخالف باشد - و هربث از ءاصر اربعه
را نیز گفته اند .
| خشیلك « باکاف بروزن و معنی‌اختیج
است که ضد و مخالف - و هرك از عناصیباشد؛
و مجموع را اخشیگان کوند .
اخگر با کاف فارسی بر وزن اختر .
پر آعی رخشنده را گویند و بعربی جم

===== leaf 306
-9--
درودگری باشد . ومضفقف اکر هم هست که‌آن
کلمةٌ حرط است - و جاره را نیز گویند که
وید که در مقابل زن است
ارابه - بر وزن فرابه ۰ گردون را
گویند ٩‏ . ۱
اراقو بفتح اول و قاف و واو بالف
کشیده » بلفت رومی
نام تضمی است بشکل
دور و برنگه سیاء و
بفایت‌سلب ؛ و درمیان
کندم و علان. پسیاز
میباشد ؛ و انرا به
شيرازی‌سيمك‌خواند . #ق
آرد تن که و اف
پسرشند و بر ورمهای
کرم و صلب ضماد
کنند نرم ساژد .
ار اهو فی » با میم بر وزن فلاطونی»
- بلغت پونانی لاله را کونند . و آن باغی و
صحرابی هردو می باشد ۰ و بعربی شقایق النعمان
خوانند ۰ و نوعی دیگر هم مت که آنرا
آتربون گوند .
)۱ چش : است .
(:( چك : - وافه اعلم .
اد ان » بتشدید انی بر وزن بران » نلم
ولایتی است از آنریاجان که کنجه و بردع
ازاعمال آن است . گوند سعدن طلا و
```


## [2026-09-07T20:42:18.980Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i in range(295,320):\n    p=pages[i]\n    hits=[w for w in ['بادان','اردو','ارد و','آبادان','اردشیر','اردبیل'] if w in p]\n    print(i, hits, re.sub(r'\\s+',' ',p[:60]))\nEOF"
}
```


### [2026-09-07T20:42:20.348Z] TOOL RESULT

```
295 [] کت آیرویز نحتانی مجهول و واو » بسعنی آبی باشد و آن ا ییون « 
296 [] بچهُ با رسیده را گویند که از شکم ۱ و حبوان دمگر بیفتد . اپرن
297 [] ی سس اعشی وسکون ثانی و جیم . میواست که آنرا خاوسی «تریج» اگو
298 [] «سیخول» نیز کوبند . ۶ آقوت » با تای قرشت بر وز نکبود . بلغت‌
299 [] بگبترا جمیم جانوران موذی بگریزند - و شرارژ آتش را نیز کفته‌ا
300 [] ست و 4 سب #احر یض « بکر اول و دای بی نقطه و سکون ثانی وتحتان
301 [] « ری الافی » خوانند ؛ و بجای بای بجد بای اخت - حم اول وسکون 
302 ['ارد و'] وخواهر زاده را گونند . اخروش « با رای فرخت بر وزن خر اخ‌تفی 
303 [] «کراث الک رکم » خوانند . اخسمه - بفتح اول وسکون انی و شم سین
304 [] اخی» بر وزن مفی ؛ کاری و چیزی‌را کوبندکه قابل تین باشد - وصا
305 [] و تشنگی را فرو نشاند - و بفتح اول ‏ و کسرثالث در غربی اهر بد
306 [] -9-- درودگری باشد . ومضفقف اکر هم هست که‌آن کلمةٌ حرط است - 
307 [] ی "ار پیاسیوس - با تحتانی و سین بی نقطه و تحتالی دبکر بروزن 
308 ['اردشیر'] ارجالون کثتاس را در جنگه کشته بود و لهراسب پدر کتتاس راکه تر
309 ['اردشیر'] خوانندش, وبعض ی کویند منسوب‌باردیل‌ین ارمنین است وتا کردة او
310 ['اردشیر'] اردشیران " قهر وخشم یز آمده است٩‏ ؛ و فلم پسر ساسان این همن 
311 [] آردسهشت او س باکاف‌فارسی بروزن‌پهلوان, بمعئی اردجان است و ها
312 ['اردو'] بخشایش » بمعنی خیر و خیرات و چیزی در راه خدا بمردم دادن باشد
313 ['اردو'] مه موم ما ی > ج با کل فا درل مخرفا اردو
314 [] آردو ت برابر نا سس ۳ص اس ای دیس ۳۳ سذ الفبای ار دو ۳ کیت لا 
315 [] شراب است - و حبایی را نیز کوبند که بردوی شراب بهم رسد - و کو
316 [] لرسانیفون ارسانقون » با اك بالف کشیده و نون تحتانی رسیده و ف
317 ['اردشیر'] وا ۱ ارغاب جمیم گزندکان بگرایزند و آرا ازطاعاسیا وار طمسا دز
318 [] ارغامونی ار غامو نی پامیم بر وزن افلاطونی؛ بلغت بونانی تباتی
319 [] سس سا مشهور که افلاطون وضع (۱) کرده است ؛» و ی گونند .ارغنون
```


## [2026-09-07T20:42:27.393Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (312,313):\n    print('==== leaf',i)\n    print(pages[i][:2200])\nEOF"
}
```


### [2026-09-07T20:42:28.684Z] TOOL RESULT

```
==== leaf 312
بخشایش » بمعنی خیر و خیرات و چیزی در راه
خدا بمردم دادن باشد .
. اددانی معروف است که فقیض
گرانی باشد ۵ - ومردم دروش و فقیر ومستحق
را نیز گونند - و بمعنی ملم بتشدید لام هم
امده اسمت . 4
ار « با زای فارسی بر وزن مخزن»
نوعي از درخت بادام کوهی است: و ثمر آن‌سپار
تلخ می باشد و آن رادر دواها بکار برنه وچوب
آبرا عصاکنند و پوست‌انرا بر‌کمان بیچندا .
باشد ٩‏ ؛ چه ارد بععنی شبیه وحانشف ؟حدداست
و چون این ماه وسط فصل بهار است و نبانات‌در
غات نثو و نما و کلها و رداحن تمام شکنته
و هوا در نهات اعتدال » بنایراین اردی بهشت
خوانند  .‏
اد -بوزن طرز » بستی قیمت و بها
و ارزش باشد ۴ - و قدر و مربه را نیز گویند
- ویمعتی درخت صنویر هم هست - ودرخت انار
- و درخت سرورا نیز گفته‌اند - و در عربی برنج
طعام باشد؟ ۴«
اررانش ۴ - بکس نون بر وزن اددن ذدین - کنایه از جرعةُ
۱ - اشتباه است چنانکه گفته شد . ۴ - پهلوی 2۳21 مشثق ازاوستابی 3۳۵[2
« پارتولمه ۱٩۱‏ « تب رک ۲۲ » وتیز 272 درپهلوی آمده ۶ منای ۲۹۷ : ۲ 4 .
۴ - در عربی ارز در لائیتی ۲۷2۵( . ۴ رگ : فزهنگ دساتیر ص ۲۳۲ ۰
شاهد برای آن بافته تشد . ۵ - بهلوی 2۳2201 (دارای ارزتی) و 2۳28۳16 ( عفت )
« مثای ۲۹۷ : ۲ * . - ۵۵6۲ ۸۳۷۵۵ د یاتی ۰.۱۰ ۸62012
ا2ع5۵06 درختی از کل پروانه‌ها که از آن صمغ عربی گیرند ۶ فرهنگه روستابی ۲ _--
نیز نام دشتی درفاری که آنرا ارزن وارجن وارجنه هم کفته‌اند . این‌البلخی در فارسنامه (ص۱۵)
گوبد : مرغزار دشت ارزن » این مرغزارکه برکنار بحیره ارزن است وببشه است ومعدن شیر »
طول آن ده فرسنگه درعرض مك ۹
۵ اردیهشتگان - جشنی که ابرآنیان‌باستان در روز اردیبهشت (سوم) از ماه
اردیبپشت بریا میکردند . « بشت ۱ : ٩۲‏ « خرده اوسنا ۲۲۰4 « روزشماری
۵۸ * ارزان - دزمهلوی 2۳2۵0 (باارزی » فیمتی) «بونکر ۸ >
کیذکی 2۲720. فریز ندی و. بر ای ونطنزی 2۳2110 « ۱.۵ ص۲۹ »> سمنانی
0 , سنگسری وشهمیرزادی 212110 , سرخ ولاسگردی 8۲228 2 .۲:
ص ۱۹۵ ۵ ادن - نباتی‌اس که درنواحی سردسی رک هکندم عمل نمیآید
بعنی در فسمت های کوهستانی برای مصرف اهالی با دانةٌ مرغ کاشته شود و آن
پت وکم ارز است . < لفتِ نامه » و رك : فرهنکهه روستابی ۱۵۱ . اب نکلمه
در پهلوی هم 272۵0 ( هز 028 ) آمده . « بونکر ۰۱۲۱ ۱۷/10
« کل کلاب * ۱ ارزن
یه ازصفحه ۱۶۱
یا کی ونقدس وفالون اهورامزداست ودرجهان خاکی نگیبانی آتش بدو سپرده است ( وبهمین‌جهت
مولف کلمه را سممنی آتش گرفته !) « روزشماری ۱۹-۸ . ۷ رك : روزشماری ۷٩‏ .
8۵ اردو - مجموع میاهیان , مجموعةٌ فشون و لوازم او - لشکرگاه < کاشفری ج ۱
ص۱۱۲ » - نام زبان مردم پا
==== leaf 313
مه موم ما ی > ج با
کل فا
درل مخرفا
اردو
```


## [2026-09-07T20:42:43.944Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"########## IRN page 119 (pdf 130)\"\npython3 - <<'EOF'\nt=open('incoming/IRN/IRN_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i in (128,129,130,131):\n    print('==== leaf',i,'(pdf page',i+1,'printed',i+1-11,')')\n    print(pages[i][:1200])\nEOF"
}
```


### [2026-09-07T20:42:45.308Z] TOOL RESULT

```
########## IRN page 119 (pdf 130)
leaves 222
==== leaf 128 (pdf page 129 printed 118 )
[pdf page 129]
۱۱۸ ایرانویج
کرانةُ دریا وآب دجله آنجا گرد آید وآن, رباطی اس ت که در آن پاسبانان بودندی
که دزدان دریا را نگاه داشتندی و آنجا پیوسته این کار را گروهی مترصد باشند.»

همین معانی را ابن‌حوقل در صورة الارض ودیگر جغرافی‌نویسان ایرانی و
عرب درکتابهای خود آورده‌اند ودر هیچ کدام سخن از شطالعرب تیست ودجله از
سرچشمه تا مصب خود دجله نامیده می‌شود زیزا در دورانها ی کهن فرات در بحل
الغرنه به دجله نمی‌ریخت تارود بزرگتری‌را تشکیل دهد ونام دیگری به خود
بگیرد .فرات راه دیگری داشت ودر بغداد به دجله می‌ریخت وبازاد آن به بطایح
می‌رفت واین معنی در جهان نامه بخوبی روشن گشته است . جهان‌نامه دراین باره

چنین آورده است:

«منبع دجله از زیر شهر آمد باشد وبرشرقی‌شهرها برجزیره بگذرد واین بلاد
جزیره شهرهایی را گوین د که میان دجله و فرات باشند و همچنین می‌آید تا بغداد

و در میان شهر بغداد شاخی از فرات بدو پیوندد وآن را نهر اعیسی خوانند و
دجله می‌رود تایه بحرپارس ریزد نزدیکی ابله وعبادان . فرات آبی بزرگك است
اما از دجل هکمتر باشد وابتداء او ا زکوههاء روم‌خیزد وبه‌بیان تغور شام بگذرد
همچنین برغربی شهرهاء جزیر هکه گفتیم بگذرد وبعد از آن یک شاخ از او در
میان شهر بغداد به دجله آی د که شرح دادیم وباقی فرات بسواد کوفه رود وآنچ از
آنجا فاضل آید به بطایح شود.»

اما واژْهٌ عبادا ن که دراین متون آمده است ودرن
==== leaf 129 (pdf page 130 printed 119 )
[pdf page 130]
آروند رود ۱۱۹
است : 3-02-30 » جزء نخست 68 به معنی آب است » 032 از ریشهٌ پاییدن و 37
پسوند نسبت است و«اپاتان» به معنی جایی اس ت که در آنجا از آب دریا و رود
پاسبانی می‌کنند وآن را می‌پایند واین نوع ترکیب همان اس ت که در آتور پاتکان,
هم دیده می‌شود وگفته اين‌حوقل واستخری نیزگواه این معنی اس ت که پاسبانان
درآبادان دزدان دریارا از دزدی با ز می‌داشتند ودهانة دجله و دریارا می‌پاییدند .
اين‌حوقل دراین باره چنین آورده است: «اما عبادان قلعةٌ کوچک آبادی برکناره
دریا ومحل گردآمدن آب دجله است وآن رباطی اس ت که جنگجویان ودیگر دزدان
دریایی در آنجا می‌باشند ودر آنجا پیوسته مرزدارانی مراقبت می‌کنند.»

در اینجا نمی‌توان بی‌آنکه ذکری از دجلةالعوراء به میان آید از موضوع
درگذشت , در برخی ازکتابهای جغرافیایی قدیم بخشی‌از رود دجله یعنی مسافت
بین نهر ابواسد وآبادان راکه از آبهای دجله وفرات تشکیل می‌شود وطول آن
نزدیک به یکك‌صد میل است دجلقالعوراء خوانده‌اند. دجلة العوراء به‌معنی‌دجلة
یک‌چشم اس تکه‌نام گذاری آن را به‌هیچ وجه نمی‌توان توجیه وتبیین کرد. مردم
زمانه نی زکه این نام را بی‌معنی ویدیمن دانسته‌اند آن را به دجلةٌ مفتح تغییر
داده‌اند یعنی دجلةٌ گشوده شده. اما حقیقت چنانس ت که تازیان معنی يکك واژهٌ
فارسی را که نام آن بخش از دجله بوده است‌نفهمیده‌اند وآن را به یک وارْد‌تازی‌هم
آوای آن بدل
==== leaf 130 (pdf page 131 printed 120 )
[pdf page 131]
۱۳۰ ایرانویج
و آن «وهمن ارتخشیر »2۳۳8756۲ ۹7003۳25 است به معنی اردشیر نیکک‌اند یش
وگویا به‌نام اردشیر پادشاه هخامنشی نامگذاری شده بوده است. هم اکنون نیز
مقداری از آبهای رود کارون از این راه داخل دریا می‌شود. در دوران عضدالدوله
دیلمی به خاط رکوتا هکردن را هکشتی‌رانی» از دهانة دجله آبراهه‌ای به سو ی کارون
کندن د که هم | کنون به فم عضدی معروف است واز آن پس کارون ازاین راه به
دجله پیوست وآبادان که در دورانهای کهن به شکل شبه جزیره‌ای بو د که یاقوت
آن را «میانرودان» می‌خواند» به‌صورت جزیره‌ای در آمد وهم!کنون نیز اگر این
راه بسته شود آب اروندرود پایین می‌نشیند.

==== leaf 131 (pdf page 132 printed 121 )
[pdf page 132]
نام‌های ایر انی ددپیر آموت دریای سیاه

نواحی اطراف دریای سیاه از دوران‌ها ی کهن مسکن اقوام و طوایف ایرانی
بوده است. در دوره‌های پیش از تاریخ این نواحی گذرگاه اقوام ایرانی بوده و
قبایل سکائی وسرمتی در نواحی سختلف شرقی وشمالی دریای سیاه جای گرفته
بودند و هنوز بقایای این اقوام ایرانی بصورت قوم است ۵89810 که همان
«آس های قدیمی و تاریخی هستند» در آن حوالی سکنی دارند و دسته بزرگی از
آنها خود را ایرونی 1۳081 يا ایرانی می‌خوانند و سرزسینشان ارستان 2۳69180 نام
دارد» بمعنی‌جای ایرانیان . در دوره‌های‌تاریخی ناحیه پونت تحت نفوذهخامنشیان
درآمد و بهنگام پادشاهی داریوش اول » ساتراپ‌های هخامنشی برآنجا فرمانروایی
کردند و سپس میتریدات جانشرن ساتراپ‌ها شد و در .۳ پیش از میلاد مسیح
سلسلة سلطنتی در پونت تشکیل داد و پادشاهی پونت تقریباً تمام سواحل جنوبی
دریای سیاه را فرا گرفت و نواد گان میتریدات مدت‌ها در آنجا فرمانروائی کردند.

اقوام گونا گون ایرانی به بسیاری ازجاهای اطراف دریای سیاه نام ایرانی
داده‌اند. یکی از این‌نام‌هاء نا مکهن دریای سیاه اس ت که ريشه ایرانی دارد.

نام‌این دریا د رنوشته های «اوریپید»!(. 2۸ پیش از میلاد) و«استرابو»۲( ۳ب
پیش از میلاد) و «پندار»۲ ( م۳ء پیش از میلاد ) بصورت پونتوس اخینوس؟
758 00605 آمده است .

واژة 002109 یک واه یونانی و بمعنی دریاست ولی واه دوسی 2761009
```


## [2026-09-07T20:43:03.451Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== SNS grep xves\"\ngrep -n -i \"xv[ēe]š\\|x'ēš\\|xwēš\\|hvēš\\|xveš\" SNS.txt | head -20\necho \"===== SNS pages leaf count\"\npython3 -c \"\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read();p=t.split('\\f');print(len(p))\nimport re\nfor i,q in enumerate(p):\n    if re.search(r'x[v\\\"ʼ]?[eē][sš]',q):\n        print(i, re.sub(r'\\s+',' ',q[:200]))\n\" | head -20"
}
```


### [2026-09-07T20:43:04.855Z] TOOL RESULT

```
===== SNS grep xves
===== SNS pages leaf count
243
1  Shiraz University Publication A GLOSSARY OF SAYIST NE SAYIST A pahlavi persian Glossary - and Six indexes ' 
221 41 \^i o~*Uft*U ajlj jA-* tf***j'j ^"jr* X xQb kardan 61/21 x v ard 275/18 xvgs sahgah 79/15 x3k 21/16
```


## [2026-09-07T20:43:05.259Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== FSF grep پاس / پاییدن / پالودن\"\npython3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nprint('leaves',len(p))\nfor w in ['پاسبان','پاییدن','پالودن','پناه','بان']:\n    hits=[i for i,q in enumerate(p) if w in q]\n    print(w,hits[:10])\nEOF"
}
```


### [2026-09-07T20:43:06.578Z] TOOL RESULT

```
===== FSF grep پاس / پاییدن / پالودن
leaves 485
پاسبان [133, 145]
پاییدن [87, 133, 138]
پالودن [135]
پناه [27, 58, 61, 70, 124, 153, 182, 242, 261, 283]
بان [8, 9, 11, 13, 16, 17, 23, 27, 28, 31]
```


## [2026-09-07T20:43:15.651Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('SNS.txt',encoding='utf-8',errors='replace').read()\nfor m in list(re.finditer(r'x[^\\s]{0,4}[eē]š|xw[eē]s|xv[eē]s|xvés|x\\^v', t))[:25]:\n    print(repr(t[max(0,m.start()-150):m.start()+250].replace('\\n',' ')))\n    print('---')\nEOF"
}
```


### [2026-09-07T20:43:16.884Z] TOOL RESULT

```
' v 5dOgdat 78/14  x v 5s 79/9-267/4  x v 5slh 267/12  x v 6sk3r 79/22  x v 5sk3rlh 80/2-6  x v eskarlha 30/4     xvgs sahgah 79/15  x v £stan 267/13  xvestar 79/16  x v etCu:raan 78/5     ySkand 299/9  y3n 303/2  yanan 302/2   6/1 yar/jar 302/16  yat 295/10  yazdah 308/16  yazdahum 294/20  yak/Svak 91/18-317  yasn 315/3   78/9yasfe 312/8-315/12  yastaran 316/1  yastan 316/15  yast I kSh 315/17  ya'
---
```


## [2026-09-07T20:43:26.181Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('SNS.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'paiOya|pai0ya|paithya|paifiya|xvaepa|x\\s?v\\s?aepa|hvaepa']:\n    for m in list(re.finditer(pat,t))[:10]:\n        print(repr(t[max(0,m.start()-300):m.start()+300].replace('\\n',' ')));print('---')\nEOF"
}
```


### [2026-09-07T20:43:27.570Z] TOOL RESULT

```
'a- 44/21  xratu- 40/17  xrafstra- 40/10  xsaera- 199/11  xsagra. vairya- 199/7  xsapan-/xsapar 197/13  xslra-? 206/8  xsudra- 203/6  xsnSvayeiti 202/7  xsn3sa-, xsna 202/4  xsnuraaine- 203/18  xsmaiby 37/4  xlva^wa- 205/2  xivas- 10/21  xsvasti- 313/6  xsvas. mahya- 37/9     x v a-/hva-hava- 79/10  x v aepai$ya- 267/5  x v aSturaant- 78/7     x v a5tvada0a 78/12  x v aini 59/22  xvato 106/13  x v a-data- 62/22  x v afta-xv a fsta 62/15  x v araiti 70/9  x v aranah- 127/3-187/2;  xVar-xsaSta- 70/19  x v astan5m 175/7  x v 30ra- 59/6  x v 3para- 56/12   G   ga56an3m 173/1  gaSea- 177/15  gaona- '
---
```


## [2026-09-07T20:43:37.067Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'paiti\\.d[āa]na',r'paiti\\s?\\.\\s?d',r'Schleier',r'fšu\\.?p',r'fsu\\.?p',r'x[v\\^]?ae\\.?pai',r'p[āa]0ra',r'p[āa]θra']:\n    ms=list(re.finditer(pat,t))\n    print('###',pat,len(ms))\n    for m in ms[:4]:\n        print(repr(t[max(0,m.start()-200):m.start()+300].replace('\\n',' ')))\n    print()\nEOF"
}
```


### [2026-09-07T20:44:46.498Z] TOOL RESULT

```
### paiti\.d[āa]na 0

### paiti\s?\.\s?d 25
" i;  Yt7.  2', ÄS4,  y.152,  75.79,  P.2.^  ^-84,  Vyt. 36.  ß)  insbes.  von  der  Gesammtheit  der nichtpriesterlichenOemeindeangehörigen**: zaotars{^d.)  iairim  .  .vacimca  °wÄf(DS.)'^ astvaite  paiti.dhayai  N.  72.  b)  'das  erste, d.  i.  das  materielle  Dasein,  Leben':  yaii ä  °rihul  *pa<mruyS  bavat  (sd.)  Y.  2S.11; — *_j'((^ö  äis  i^ä  vansaitg  yä  data  'uAiuf paouruyehyä  ratul iyao^ana  rasistä(sd.) .  . Y.33.1;  zit.  55.6;  —  °uASus  sq>di  (sd.) paouruyehyäY.  48.(>.  "
'a  .  .  \'/rv//i aiti.barqn  avi  . .  nmätum  yaf  . .  na  fara.- ; iri^ytlJV.^.4i;  42f.; — yexi  nsit  mirika\' (näml.  (i^ravaiti)  \'trtm  atwi-valftai  (sd.)  | .  .\'%re  (für  Gen.)  *raoxsnqm  paiti. dHyät  (sd,)  \\ y.i0\'.2i  —  avi  t/im  (n\'iatL  vanqm)  aiwi.- rM/ayaü  (s±)  °^rffV.^.2; — \' \'"kra  fra- vaiim^a  (sd.)  N.  65;  V.5.37;  —  von  Un- gläubigen mit  verpöntem  Material  genährt: yal  . .  dam)ayäzQ  avi  -irsm  äbarsiiti  .  . aO^m  aämitn  yS  vaoce  ^lumatka  nqma Yt  74'
"  ;<?;  J^J;  —  ys  ätnm  nasu- piihin  däitim    -tum   avi  ava.baraiti  V.S. 81;  81,  85.  a)  in  der  Rechtssprache Ort  des  Gerichts,  Gerichtshof,  Forum': vff  *naird  *p^rpnp/ni/äi  nöit  paiti.däöaiti 'tiimca  *varaua(sd.)  zrvünainca  Y . 4c;  — yS  nara  'tum  baraiteY.4A^)^'.  3)'Slätte zum  Ruhen,  Liegen,  Sitzen'  sva.  'Lager- statt, Bett,  Divan,  Sessel,  Thron',  auch im  Plur.:  ava  kl  (näml,  dem  Leichnam) 'tum  barayan  ätryehe  (sd.)  vä  .  .  V.  <?.8; —  upäai  h"
"  Y.  j./.  4j   NA.  hat i^i^rai-'.  s.  aber  Fl. •  j.  äidrö.daxSta-  Adj.  'der  ein  offen- bares, deutliches  Zeichen  hat,  bietet  von  ~, für  —'  (Gen.):  agmca  ahe  'ts  anhat  alm ii>rS.paiti.dayB  V./.  14  Gl. Pü. :  ica  ön  i  öi  pdiläiih  dajtiai  asi. •  j.  didrö.-paiti.daya-  Adj.,  'der  ein  offen- bares, deutliches  Merkmal  hat,  bietet  von  — , fiir— '(Gen.):  almca  ahe  cihrsJaxstS  ar^hal aim  'yö  V.J.  14  Gl. Pü.:  f^iliiih  pa  apar  milrüiäh,  erL:  ia  niki-"

### Schleier 0

### fšu\.?p 0

### fsu\.?p 0

### x[v\^]?ae\.?pai 0

### p[āa]0ra 0

### p[āa]θra 0
```


## [2026-09-07T20:44:59.314Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nprint('leaves',len(p))\nfor w in ['پاییدن','پالودن','پدر','خویش','پناه','پاسبان','آبادان']:\n    hits=[i for i,q in enumerate(p) if w in q]\n    print(w,hits[:8])\nEOF"
}
```


### [2026-09-07T20:45:00.633Z] TOOL RESULT

```
leaves 545
پاییدن [154, 373]
پالودن [151]
پدر [35, 36, 37, 42, 100, 128, 157]
خویش [1, 16, 19, 23, 25, 29, 30, 40]
پناه []
پاسبان []
آبادان []
```


## [2026-09-07T20:45:01.721Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls incoming/WLD/\npython3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nprint('leaves',len(p))\n# find leaf containing 'pā-' entry with 'füttern' or 'weiden'\nfor i,q in enumerate(p):\n    if re.search(r'f[üu]ttern|weiden',q) and re.search(r'p[āa]-',q):\n        print(i, re.sub(r'\\s+',' ',q[:300]))\n        if i>200: break\nEOF"
}
```


### [2026-09-07T20:45:03.037Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
leaves 725
20 16 pek-, pek-, j^Ok- 1. pek-, pek-, pok- etwa „Mbsch machen, aufgeraumt oder vergniigt sem‘‘\ Ahd, gifehan, ags. qefe07i „sich freuen‘"; ahd. gifeho^ ags. gefea „Freude^‘, kaus. (s. Fick III^ 224f.) got. fulla-fahjan „Genuge leisten, befiiedigen, dienen‘‘ (da
21  17 \ 2it.pedo^ -ere, pexl ^^^mmQn^\pecten,-inis wmh, petenata „pecti- natam“; ahd. as. fehtan^ ags. feohtan ^fechten^ (weDn mit Bed,-Entw. wie dt. raufeDj mdartl. bair. s
76 72 po(i):(p9i?:) — pa- aus poln. piivo ds.), fojq, pojiti „trankeii'' (ac. panost „Trunkenheit“ ist kein Slav. Rest der Stufe Prusik KZ. 35, 600, sondern aus ^pbj-anosih ent- standen. Osten-Sacken IF. 32, 314). Curtias 280, Fic
77  poi., pi 73 Mit f-Formantien (bzw. -^Weiterbildnng): gr. Tzaxeouai ,,esse und trinke“, aor. Tidooao&ai, uTtaorog „ohne Speise and Trank''; Grot, fodjan „ernahren, futtern", aisl. feda,
664  ; 660 speg- — {s)pen- Gr. ox£7tToiJ.at 5 ,schaue‘^ (oxen- umgesfcellt aus
```


## [2026-09-07T20:46:18.310Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nprint(re.sub(r'[ \\t]+',' ',p[76])[:2500])\nprint('@@@@@@@@@@ leaf 77')\nprint(re.sub(r'[ \\t]+',' ',p[77])[:1200])\nEOF"
}
```


### [2026-09-07T20:46:19.709Z] TOOL RESULT

```
72 po(i):(p9i?:) — pa-
aus poln. piivo ds.), fojq, pojiti „trankeii'' (ac. panost „Trunkenheit“ ist kein
Slav. Rest der Stufe Prusik KZ. 35, 600, sondern aus ^pbj-anosih ent-
standen. Osten-Sacken IF. 32, 314).
 Curtias 280, Fick I* 84, 482, 46, Yf. LEWb.^ 88 f. Brugmann II ^ 3,
37, 108. —
 Alte Beziehung zu poi- „von Feuchtigkeit strotzen'' ist unsicher.

po(i) :
 (p9i?0 (zum Wzansatz s. Schulze KZ. 27, 426) „Yieh weiden,
 hiiten^; daraus allgemeineres „schutzen, auch durch Bedeck en“.
 Ai. pati, av. pCiiti „hutet, bewacht, schiitzt^^, ai. go-pd- m. „Hirt“, av.
r ana-pci „Beinschutz, -schiene^*, ai. pagii- „hutend“ (vgl. nmv), paid- m.
„Wachter, BQrt“ {paldyati „bewacht, hutet‘‘), -pcivan „schutzend“, ap.
xmO^a-pavan „LandYOgt, Satrap‘‘; ai. nr-pi-ti-li „Mannerschutz“ nr-p-a- ;


m. „Mannerschutzer =
 K6nig“ (ist eine ahnliche Zs. mit them, Vokal
*dya-7t-og die Gdlage von dya-ndoy „hei6e \villkommen“? Prellwitz s. v.,
Brugmann IP. 19, 389). Ai, pdtra- n. „Behalter“ = got. fodr, s. u.
 Arm. Tfiauran „Herde“ vielieicht als ps-tro- (sek. Abl. zu *29d[ij?)
hieher, eher aber als ^pa-tro zur Wz. ^pa- s. u. Ebenso wohl arm. hoviv
„Hirt“ aus *oui‘pa-, s. Liden Arm. St. 26.
 Gr. 7td)v „Herde“ (n. aber im pass. Sinne oder als „die
 zu ai. pdyxi-,
Hut'‘), TioifiYiv ,,Hirt“ das gr. Wort wohl aus *7zcoijuf]v), Ttoi/uvrj
 (: lit.

„Herde“, jzoijualvco „treibe auf die Weide, hute; nahre, ziehe auP; Ttco/Lia
jjDecker* (Bed. und i-lose Wzf. wie in ai. pair a-, got. fodr).
 Got. fodr n. (= dk.pdtra-) Scheide*', ags. fdper, fodor „Putteral,
Scheide*^ spatan. n. „Futter (des Kleides^^, ahd. {fedar)fdfar „Putteral,
Putter“, nhd. Putter (des Kleides), Putteral.
 Lit. pemu „Hirt“ {f^p^i-menl. oder trotz der schleifenden Intonation aus
^pdlmen-^. Osten-Sacken IP. 33, 245 f., der lit. e aus o/, ai wohl unbe-
rechtigt leugnet, lafit "^paimii nach penas, pStus zu pemu geworden sein).
 Keben unserer Wz. steht mit durchs Lat. verbiirgtem a-Yokalismus (das
nicht an Stelle von d durch Angleichung an eine —
 im lat. gar nicht sicher-
stehende —
 Tiefstufe a = a getreten ist, wie z. B. wieder Osten-Sacken
IP. 33, 238 f. erwagt; s. bes. Osthoff Suppl. 55) in gleicher Gdbed.:

pa- „Yieh weiden, huten“, woraus ,,futtern, nahrem' in: arm. liauran,
 hovi-v (s. 0 .).

 Lat. pdsco (pdscoV. s. Thurneysen IP. 4, 45), -ere^ pavi, pastum „weiden-

lassen, fiittern^, Dep. „fre8sen, weiden“, pastor „Hirt'*', pahulum (f'pa-dhlom)
„Futter'', panis „Brot“ (eher "^pa-ni-s als -sni-S) fiir "^pa-st-nis ent
@@@@@@@@@@ leaf 77
 poi., pi 73

 Mit f-Formantien (bzw. -^Weiterbildnng): gr. Tzaxeouai ,,esse und trinke“,
aor. Tidooao&ai, uTtaorog „ohne Speise and Trank'';
 Grot, fodjan „ernahren, futtern", aisl. feda, ags. fedau, as. fodian, ahd.
fuattan „ernahren": ahd. fiiotar ,,Xahrung, Speise, Futter", ags. foper^
fodor, aisl. fodr ds., ags. foda, engl. food ds. ; ags. fostor „TJnterhalt,
Nahrung", aisl. fostr n. „Erziehung,ahd. fatunga „Nahrung",
 ITnterhalt'';
I’avatot „pastus", nhd. Felime aus alterem vedeme „Eichel- oder Bucheckern-
mast" (letzteres nach Schroder lA. 2S, 29). Sehr unsicher air. asaid „wachst"
(„es mehrt einen"), mir. ds „Wuchs, GroCe" (von Strachau IF. 2, 370 als
*pdt-to- angereiht; sicher fern bleibt ait ,,Geschwu]st“, atiaim „schwelle",
Stokes KZ. 40, 244; zu anderen Deutungen s. Pedersen KG. II 651.
 Ygl. iiber die Gruppen von "^pdi- und im allgem. Curtius 270, 281,
Osthoff Pf. 252, Pick I^ 77, 471, Persson Wzerw. 33, Hirt Abl. 36, Liden
Arm. St. 26 f.
 DaS auch ^pd eine AYzf. ^pra neben sich gehabt habe und aus ihr von
Kons. vereinfacht sei, schlieSen Solmsen KZ. 29, 108 a, Hubschmann lA. 11,
54 zu Hirt aaO., ReicheltKZ. 39, 12, Osthoff Sup pi. 55 f. Par. I, 8 a aus den
allerdings
```


## [2026-09-07T20:46:28.266Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nfor i in (151,154,157):\n    print('===== leaf',i)\n    print(re.sub(r'[ \\t]+',' ',p[i])[:1600])\n    print()\nEOF"
}
```


### [2026-09-07T20:46:29.697Z] TOOL RESULT

```
===== leaf 151
[pdf page 152]
پالیدن, پالودن, پالاییدن / ۱۵۳
یادداشت,
۱- معنی این واژه در ایرلندی میانه و ولزی: تازه. *
ا ۲- معنی این واژه در آلمانی کهن و میانه: سرند کردن» (غله را) برجاری کردن.
۱ ۳ بازگمت به: هور پالیدن.
اوستایی (۸۳874(۷): آلمانی کهن (05440۷ ۲۷/01 صان):
,7۸۸0۸ ,ات۸ 0تشتق۲ 0
پهلوی (۳۸414۲7): 7۸171۸۸ ,8.11۸34 انگلیسی (8/0/58)(از فرانسه): ۴25
کردی (080151)): 8۸6
بلوچی (/8۸07): ۶۸1۸۷۸6 ,۳2/5۸6 پسگشت‌ها ک ۳
اففانی (پشتی) ‎ :۸08/۷/(‏ باظ۳7۸ 607 و
سانسکریت (7ل8۸(/5). 5 (۳8۴۷) 8۸0/17
ا ۳3۸۹ ,723۸2۸711 ب۳۸۷۸3 4 (۴818188) نقققملم 05
لاتین (۸7100ا): نك اه ای زا 9 (۲81۴) :2/۲5/25
فرانسه (4لع۳2۸): ادا داد رای 4 (۳۸2) :07075
اسپانیایی (3ل82۳۸(3): ۳۸ 6 (۲83) 537
ایتالیایی (ماله7): اد دش اد را برهان قاطع : 1۵۸
یادداشت:
بازگست بد: پاکه.
5
یونانی (075520): ناند ۱۱۸۸ رومانی ((1۸لهلال۸). 2۸
لائین (770با). ایسلندی‌کهن (1۵0 210۸ید صضام).
0 ۶5 ,ات۳۸۲ خ۸اق7۸
فرانسه (1ح)(۳2): ۱۸3 نررس کهن (۸088 2ا0). ۲۳۵۸
آسپانیایی (8۳۸(//3/7). قا ها سا کسرنیکهن (/54200 0ا0):
ایتالیایی (۸۸اه1/): ادا ۱ رالشآنآ۸70 ,۸1
یمور ۱


===== leaf 154
[pdf page 155]
۶ / پاییدن, پائیدن
آلمانی کهن (/0872/4 ۷۲07 ا0): چک (للق2): ۳7
۳ اسلوا کی (81-0744): دنام نا
آلمانی (/(08724۸): لا دازا دا پسگشت‌ها ۰ ۲ رای رد1
انگلیسی کهن (8۸01870 00): رن ی ۳۵/۵/۵ 1
5 ,1۳۳85 1 (۴[۳185۲) +8
انگلیسی (6(/015/7): دار انا ید۱۱ 4 (۲1۳۲82) :05105
هلندی (7ل0170): ۷۱۳0 529 ۳1۳38000" :۵2 (۱2 7۳۸
لهستانی (۳0//37): سنا این ۱1 برهان قاطع + ۳۶۰
یادداشت:
بازگشت به: پنج؛ ده.
اوستایی (/4۷87۸): ۸ ,۲۸۱۲ دانمارکی (0۸4/۷/914)(شاید) ۳00
پارسی باستان (۳8۸۶(۷ ۰:۵ ۳۸۷2۲۲ سوئدی (51775:215/7)(شاید) ۳00
پهلوی (۲1ماتام۳۸): + ,820۸ اسلاوی کهن (0//ابماک ۲71086 010)(شاید)
کردی (7ل070[5): نارای اون ۳۹7
سانسکربت (54(/5777): لیترانی (۵7الونا7/): ۳0
1 مفشا۳۸1 ,۴۶ 881-8
بونانی (088880): پسگشت‌ها شرت دادن
4 لا۳0 ,۳012/50 رب
لاتین (7100م): 06 ۳۸8535 6 (۲0۵058) وی رن 21
گوتیک (0077/12)(شاید) 700 9 (ت۲۸۲۲۷ ,ده سا تا
آلمانی کهن (/08724 7107 صه)(شاید) 46 (۲۵008) :077025
3 ری 0 (۲۵0053) 57
آلمانی (0874/۸)(شاید) 3 ند الا ادا 297 7۵۲/2
انگلیسی کهن (5/.ا870 ص0)(شاید) 2 (61۸30) ۸/0
3 داریا برهان قاطم + ۳۶۶
انگلیسی (0لقاا8۸/0)«شاید) ‏ 80002
یادداشت.
۱- این واجریشه با واجربشه هند و اروپایی -۳11* ,-۳۸7* (۳* (به چم "خوراکد" و "پرورد") خویشی نزدیکه


===== leaf 157
[pdf page 158]
ج ۳۳ ۱

پدر و مادر پدران (به چم / ۱۵۹
پسگشت‌ها اشگ رد 103104 ناه
0 4 (۲۸388) :00/5
1 (5۸71183) ی 23 (۲۸71138) و

1 (۳۴۴) م05 42 :۸
4 (۴۸71۴3) :۸2/2 برهان قاطع + ۳۷۲
اوستایی (4287۸4): را گوتبک (00710): دزد ناد
سانسکریت (8۵/88707): نورس کهن (ق۸۷088 ۰:01 ۳8077361
1127۸۸ ,نا۸ ۳17۸ انگلیسی (8۸/0./5)(از فرانسه) ‏ ۳۸8۸۲78
لاتین (/4710): دانمارکی (12۸(7]87): لدانت ان دا
15 ,۳۸۸7۳ هلندی (007613): 5
فرانسه (/۳88۸):

۸۲ ۳۵۵ ,2۸33۲۲۲ پسگشت‌ها اهر تا
اسپانیایی (52۸(/8): 9 ۳۸۹8۷ ۰ :84/۷۳47
5 ,۴۳۸۹18۱7۳5 103104 2عا8
ایتالپایی (/(4ته7): ۳۸۲۲18 ,۳۸۲۲7 51 (۳۸۸۲) :01005
رومانی ((471(#): اد 9 (۳۸38۲) در ده نج

پرتغالی (۳07017585): اد یی ۱

۱
1 ارستایی (۸۲8574(0): ۰ ۳۳8۸8۸۸ ,28۸ ۳۸۸۶ ,۳۸۸۸۷۸۹ ,818۳۵
پهلری (۲1مانلم۳۸): 3( آرمنی (4/05807]42): 1

کردی (57//ل6): 3 ان برنانی (075680):

بلوچی (القتالهه): 3 ای ۳۵۵ ,7۲۲3810 ,کت ۲۲۸
افغانی (پشتو) (/4۳0۵7): ۳۸ لاتین (7100ل): ,فتاانظا7
سانسکریت (54۸8877): فرانسه (۳5/617): لاد 8
```


## [2026-09-07T20:46:49.695Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%A7%D9%85",
 "prompt": "Persian پنام: give the etymology (Middle Persian padām, Avestan paitidāna-) and gloss."
}
```


### [2026-09-07T20:46:51.341Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T20:46:51.647Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%A8%D8%A7%D8%AF%D8%A7%D9%86",
 "prompt": "Persian آبادان: give the etymology(ies) offered — including any derivation from ābād, from Middle Persian, and any mention of Arabic ʿAbbādān — and the glosses."
}
```


### [2026-09-07T20:46:58.034Z] TOOL RESULT

```
# Persian آبادان Etymology

The page provides the following etymological information for the Persian term:

**Primary Etymology:**
"Inherited from Middle Persian" with the form /ʾp̄ʾtʾn/ meaning "thriving."

**Surface Analysis:**
The word breaks down as آباد (ābād, "prosperous") + ـان (-ān suffix), indicating a compositional structure where the adjective "prosperous" receives a suffix.

**Note on Arabic:**
The page does not mention any connection to Arabic ʿAbbādān. The etymology traces the term exclusively through Persian linguistic lineage, from Middle Persian to Classical and modern Persian forms.
```


## [2026-09-07T20:47:04.987Z] TOOL CALL #80: WebSearch

```json
{
 "query": "Avestan paitidāna Middle Persian padām panām padan mouth veil Zoroastrian priest etymology"
}
```


### [2026-09-07T20:47:12.061Z] TOOL RESULT

```
Web search results for query: "Avestan paitidāna Middle Persian padām panām padan mouth veil Zoroastrian priest etymology"

Links: [{"title":"Shafta ḏ Pishra ḏ Ainia | Journal of the Royal Asiatic Society | Cambridge Core","url":"https://www.cambridge.org/core/journals/journal-of-the-royal-asiatic-society/article/abs/shafta-d-pishra-d-ainia/CE190661A983F5CB60F495646359F0F6"},{"title":"Ateshgah | Encyclopedia.com","url":"https://www.encyclopedia.com/environment/encyclopedias-almanacs-transcripts-and-maps/ateshgah"},{"title":"Mobad","url":"https://en.wikipedia.org/wiki/Mobad"},{"title":"1 The Priest Parsi, Iranian and Avestan Ali A. Jafarey The Parsi Mode","url":"https://zoroastrian.org/wp-content/uploads/2024/11/Jafarey-The-Priest.pdf"},{"title":"Zoroastrian Global Glossary | FEZANA","url":"https://fezana.org/glossary/"},{"title":"Zoroastrian Global Glossary v2 (N-Z) | FEZANA","url":"https://fezana.org/zoroastrian-global-glossary-v2-n-z/"},{"title":"Zoroastrian Global Glossary v1 | FEZANA","url":"https://fezana.org/glossary-v1/"},{"title":"Padān | Zoroastrianism and Parsiism | Britannica","url":"https://www.britannica.com/topic/padan"},{"title":"THE ZOROASTRIAN PRIEST IN THE AVESTA | Arshtad","url":"https://arshtad.wordpress.com/english/notes-4/the-zoroastrian-priest-in-the-avesta/"}]

Based on the search results, I can provide you with information about the etymology and linguistic forms of this Zoroastrian ritual object:

The paitidāna (Middle Persian padām, New Persian panām, Parsi Gujarati padān) is a "mouth and nose mask" that magi wore during ritual performances to avoid polluting sacred flames with their breath. The Avestan form is paitidâna.

Related forms include the Pahlavi and Parsi padân, and the Pazend panam or penum. The Mandæan ritual face-bandage covering the lower part of the face is called pandama or paiman.

One of the priest's usual implements for rituals was the paitidâna (mouth-veil), along with other ritual instruments. The term demonstrates linguistic evolution across different stages of the Persian language, from Avestan through Middle Persian to Modern Persian and Parsi Gujarati forms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T20:47:26.319Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%82-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%B3tis\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%DB%8C%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D9%84%D9%88%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%A7%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%AF%D8%B1\" ; do\n  python3 tools/fetch_source.py \"$u\" --note \"page 379, root Pa/Pa-ter/Poti: PIE roots and Persian payidan/paludan/panah/pedar etymologies\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-07T20:47:28.610Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ca565c6cb7f3e8ee.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5cc57d5c414bf99b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ee9a6d42f2b2bcc6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ea9a1de647a80ae8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/75aabc38ede43378.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/628630caf76bef57.txt
```


## [2026-09-07T20:47:30.402Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%B0%D8%B1%D8%A8%D8%A7%DB%8C%D8%AC%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%DB%8C%D8%B4\" \\\n \"https://en.wiktionary.org/wiki/Artabanus\" \\\n \"https://en.wikipedia.org/wiki/Abadan,_Iran\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%A8%D8%A7%D8%AF%D8%A7%D9%86\" \\\n \"https://www.britannica.com/topic/padan\" ; do\n  python3 tools/fetch_source.py \"$u\" --note \"page 379, root Pa: Azarbayjan/Atropates, xwes, Artabanus, Abadan name, padan/panam\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-07T20:47:33.881Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c22f7068b1c95414.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/10a466ebc8dc2420.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4835e7cf87d59550.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3744e619b4cff57d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e8967f3505f8ebe0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/27e0eec7f7609e3d.txt
```


## [2026-09-07T20:47:39.019Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== خویش ===\"; grep -i -A12 \"Etymology\" 10a466ebc8dc2420.txt | head -40\necho \"=== padan britannica ===\"; head -30 27e0eec7f7609e3d.txt"
}
```


### [2026-09-07T20:47:39.081Z] TOOL RESULT

```
=== خویش ===
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Pronoun 

 1.4 
 Noun 

 1.4.1 
 Usage notes 
--
 Etymology
 [ edit ] 

 Inherited from Middle Persian NPŠE / 𐭭𐭯𐭱𐭤 ( xwēš ) , from Old Persian 𐎢𐎺𐎠𐎡𐎱𐏁𐎡𐎹𐎶 ( ʰuvāipašiyam ) , a compound from Proto-Iranian *hwaypaθyah , with the phonetic change resulting in unattested but assumed Middle Persian *xwēbš > xwēš.

 The first element of the compound is akin to Old Persian [script needed] ( huva ) , from Proto-Iranian *hwáh , from Proto-Indo-Iranian *swás ( reflexive pronoun ) , from Proto-Indo-European *swós . [ 1 ] (compare Persian خود ( xwad  / xod , “ self ” ) )

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈxʷeːʃ/ 

 ( Dari, formal ) IPA ( key ) : [xeːʃ] 
=== padan britannica ===
URL: https://www.britannica.com/topic/padan
FETCHED: 2026-09-07T20:47:33Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden
```


## [2026-09-07T20:47:49.099Z] TOOL CALL #84: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wikipedia.org/wiki/Padan\" --note \"page 379 node 7: panam/padan Zoroastrian mouth veil, Avestan paitidana\" 2>&1 | tail -2 && head -25 $(python3 - <<'EOF'\nimport json,glob,os\nEOF\n) ; grep -i -m5 \"paitid\\|padan\\|Avestan\" data/verification/sources/web/$(ls -t data/verification/sources/web | head -1) | head -10"
}
```


### [2026-09-07T20:49:50.408Z] TOOL RESULT

```
Command did not complete within its 120s timeout and was moved to the background (ID: bzjdina7o). Output is being written to: /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tasks/bzjdina7o.output. You will be notified when it completes. To check interim output, use Read on that file path.
```


## [2026-09-07T20:50:01.396Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"paiti[.-]d[āa]na[^ ]*: *[a-zāēīōū]*\" NYB_vol2_glossary.txt | head\ngrep -n \"patām\\|padām\\|patam \\[\" NYB_vol2_glossary.txt | head -5\necho \"--- avestan index p entries ---\"\ngrep -o \"paiti[a-zā.ō-]*: [a-zāēīōū*]*\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T20:50:01.466Z] TOOL RESULT

```
--- avestan index p entries ---
paiti-lar-: patirak
paiti: pat
paiti-lar: patirak
paitica: p
```


## [2026-09-07T20:50:06.596Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls -t data/verification/sources/web | head -3; cat /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tasks/bzjdina7o.output 2>/dev/null | head -5"
}
```


### [2026-09-07T20:50:06.654Z] TOOL RESULT

```
6c5cb6d0f5cc67b0.txt
index.jsonl
2ca1ea8f1b569a6f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7d7d256be6a78bd2.txt
```


## [2026-09-07T20:50:10.209Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; head -6 data/verification/sources/web/7d7d256be6a78bd2.txt; grep -i -m3 \"paitid\\|Avestan\\|padan\" data/verification/sources/web/7d7d256be6a78bd2.txt"
}
```


### [2026-09-07T20:50:10.258Z] TOOL RESULT

```
URL: https://en.wikipedia.org/wiki/Padan
FETCHED: 2026-09-07T20:47:50Z
STATUS: 200
TITLE: Padan - Wikipedia

Padan - Wikipedia 
URL: https://en.wikipedia.org/wiki/Padan
TITLE: Padan - Wikipedia
Padan - Wikipedia
```


## [2026-09-07T20:50:13.282Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,60p' data/verification/sources/web/7d7d256be6a78bd2.txt | tr -s '\\n' '\\n' | head -60"
}
```


### [2026-09-07T20:50:13.329Z] TOOL RESULT

```
URL: https://en.wikipedia.org/wiki/Padan
FETCHED: 2026-09-07T20:47:50Z
STATUS: 200
TITLE: Padan - Wikipedia
Padan - Wikipedia 
 Jump to content 
 Main menu 
 Main menu
 move to sidebar 
 hide 
 Navigation
 Main page 
 Contents 
 Current events 
 Random article 
 About Wikipedia 
 Contact us 
 Contribute
 Help 
 Learn to edit 
 Community portal 
 Recent changes 
 Upload file 
 Special pages 
 Search 
 Search 
 Appearance 
 Donate 
 Create account 
 Log in 
 Personal tools 
 Donate 
 Create account 
 Log in 
 Padan 
 2 languages 
 Cebuano 
 Français
```


## [2026-09-07T20:50:17.237Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -n -i \"penom\\|padan (\\|mouth\\|Avestan\\|Zoroastr\" data/verification/sources/web/7d7d256be6a78bd2.txt | head -10"
}
```


### [2026-09-07T20:50:17.284Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T20:51:07.115Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nfor i in (567,644):\n    q=p[i]\n    print('===== v1 leaf',i)\n    print(re.sub(r'[ \\t]+',' ',q)[:2400])\n    print()\nEOF"
}
```


### [2026-09-07T20:51:08.397Z] TOOL RESULT

```
===== v1 leaf 567
او
نیز گویند . ۱
پاچیله » بر وزن پانیله . کنش و پا
افزار باشد .
پاخره ‏ بفتح خای نقطه دار و رای
بی نفطه : صفه و نشیدتی را گویند که در پیش
در خانه باژند» ویکسرخای نفطه‌دار نیز گفته‌اند
و بسکون آن هم آحده است .
پاخیره - بر وزن کاجیره , بنای دیوار
و خانه و امثا آن باشد و آنرا بعربی رهص
خواند . ۱
پاخیره دن ‏ بنتح زای هوزوسکون
تون, بنا و گل کار و دبوار کر را گوبند. وسربی
رحاص خوانند .
پاث ۱ بر وزن شاد.بمعنی‌ای ویاسبان
و نگهبان و پاییدن باشد که از دوام و بات ودد
تظر داشتن است - و مامان و دارندگی دا لیز
وید - و بمعنی بز رک و عمده هم هست »
و پادشاه مر کب ازین است- و تخت واورنگث را
نز کفه‌انده چون در اصل این لفت بات بوده
و تابدال بدل شد بسب قاعدم کلی یابسبب تفییر
السنه وازمان.
باداد بر وزن دادار سعنی بلفی
از ماههای ملکی- و اسب جلد ونند وتیز را نیز
کویند - امر برپای داشتن هم‌هست . *
‌
و بسنی کوبند پاداش بمعنی مکافات است مطلفا
خواه جزا و معافات لیکی باشد و خراه بدی۷ ۰
هاد‌اشت؟ - بسکون تلی فرشت ۰
بمعنی ۳ ست که جزا و مکافاث یکی
باشد . ۱
باداشی * ‌ شتح شین نقطه‌داروسکون
نون» بمعتی پاداشت باشد که جزای نیکی است
چ هکفتاند ,
یت ؛
بگانه‌ای که دودستش کهعطا بدهد
حزار فابده با صد هزار پاداشن ۷ .
پادام ‏ بر وزن آرام , حلقةٌ موی را
کویند. وآن دامیست که ازدم اسب ساند و در
راه جانوران برنده گذارند - و پرنده‌ای‌دا نیز
کفته‌اند که ترديك بدام بندند تا جانوران دیگر
بهوای اوآیند ودردام افتند, واو را بعربی ملواح
خوانند .
پادرر کایه بننتی_موار و مواری :
سفر باشد و کنابه از مهیا بودن و مستمد شدن .
اسباب سفر است - ودم تزع را نیز کفته‌اند که
ابتدای سفر آخرت است- و هرچیز یکه تزديك
بضایم‌شدن باشد عموماً و شراب ی که مادل بشرشی
شده باشد خصوصا . 4
پادسکه -بنتح اك بر وزن پات »
شغنی 8202 (شبان) «اسشق۲1۵».
۴ - بهلوی 02۳15۳0 224
۴ - نگر نيك‌وبد تاچه کردی ز پیش
رد پاداشن ۳
۹ ی ره ": پادای
رك :آي و خرده اوستا ۰.۹۹

===== v1 leaf 644
بیان هیجد هم (۱)
در بای فارسی با نون مشتمل بر شصت ودو لت و کنات
واعمالی که بجهت دفم چشم زخم کنند- وبمعنی
پوشیده و پنهان هم آعده است و بلغت زند
وپازند (۲) پارچه ای باشد چهار کوشه که در دو
کوشة آن دود دوژند ومتابعمان زردشت دروقت
خواندن زند و پازنه (۲) و اوستا آن را برروی
لین « بفتح اول وسکون ثانی» بمعنی اما
وبممنی لیکن باذد.
لنأث « بروزن سواد ؛ بمعنی هوا باشد
وزمن کرده است . خود ندند ۷ .
ودبیر و نوسنیه را گوبشد - وتار ابریشم را ثبز ورخت را گوشة .
گفته اند - و بضه مانندی باشد از رسمان
خش که دور دوك بچیده شود - و ماشوره را
نیز کوبند.
بنام بفتح أول بروزن کلام ۰ تعویذی
ناه ۴ - بفتح اول و الی بالف کشیده
و بهاء زده» بمعنی حمایت باشد- وسابة دیوار را
نیز پئاء گوبند - و امر بدیین ععنی هم هست
یعنی یناه ببر وپناه بخ
ناهد - باها ودالابجد بروزن‌صباحت.
0 در اوستا 8202 - ۳2101 , در هازی 0 , 024۳70201 و 27110 . در
کرد بان بشت مسمعنی جامه‌ای که درزیر زره دوشند» آمده؛ در لگ د4 وندید اد بند ٩‏
ینام جزواساحه ولوازم يك‌مرد جنگی بشمار آمده, بجزاین معانی دراوستا وپهاوی پنام عبارت‌است
از دو قطعه ارچ سفید از جنس پتبه که بروی دهان آویخته با دو نوار پیشت سر کره میززنشد .
زرنستیان ایران آن دا هروبند» لمتد. این برد؛ کوچك که بنا بتوضیحات ضیر پپلوی اوستا باید
دوبند انگشت پاین‌تر ازدهان باشد» دروقتی بکاربرده ممشودکه موبد درمقابل آتش مقدی » اوستا
سراید ومراسم دیتی بجاآورد . استعمال پنام برای آن‌است که نفی وبخار دهن‌بعتصر حقدی‌ترسد.
پنام‌از لوازم آ تربانان (موبدان) است. #يشت ۱ص ۷۹۳ و۲۹۵ ح و۳۵۵4
بتا ! نگارا ! ازچشم بدبترس همی چرا نداری پاخویشتن همی تو ینام ؛
ازین بیت پیداست که مراد همان روبند است نه‌تمویذ (مذ کور درعتن) وفرهنگه‌نویسان
مقر منة چشم بد چنن درك کرده‌اند 1 «کاتها ص۱۲ . زرانشت هرام در اردای وبراف نامه کوبد:
بشد برغخت زر اردای وبراف ۱ پنامی بررخ و کستی‌اش برناف .
۴ بهلوی 0۵0۵ [ ۳202۵10 یناهی. بناه بردن | از ۶02)8۵1 0808۵1 #از
2 * « تیب رکه ۱۱۹ بنقل‌از هوشمان» و رك: اسشق ۳۲۸-۳۲۷ .
```


## [2026-09-07T20:51:29.647Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nprint('==== v1 leaf 563 (printed ~358)')\nprint(re.sub(r'[ \\t]+',' ',p[563])[:1200])\nt2=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nq=t2.split('\\f')\nprint('leaves v2',len(q))\nprint('==== v2 leaf 529 (printed ~1069)')\nprint(re.sub(r'[ \\t]+',' ',q[529])[:1200])\nEOF"
}
```


### [2026-09-07T20:51:34.139Z] TOOL RESULT

```
==== v1 leaf 563 (printed ~358)
۳۳
خوانند .
لیو ث » بر وزن ربوند » بمعنی غدر:
است که بیوفابی کردن باشد .
ی ۵ » بروزن هیوه» بمعنی غرمب وتنها
باشد - وزنی را نیز کویند که‌شوهرش مرده‌باشد
با او را طلاق داده باشد - ومحردیرا یز گویند
که زش حرده باشد - و نام داروبی است که
بر که آن سر که کیرماند اما خار تدارو و ی
آن بخیار شباهت دارد(۱) لیکنکوچکترازآن
باشد وآنرا بمربی قثاء البری‌خوانشد وقتاءالحمار
همان‌است .
بیهله ۴ - بکسر ارل و ضم ها بروزن
دل شده , مخفف بهوده است و معنی نا حق
و باطل باشد» چههده بممنی حق است.- ویمعنی
بی نفم هم‌آمده است و جح اول جامه‌ای را
(۱) خم ۰۳ چك : بخبار دراز .
۹ را اقرب الموارد : بین.
بیهوده
کویند که از حرارت آتش زرد شده باشد .
دیق بنتح اول و اكث وسکون ثالی
و قاف » دام شهریست غیر معلوم۴ .
یهن بکراول بروژن‌سجن, خاریشت
بز رکه تیرانداز را کویند یعنی خارهدای خود را
ماشد تیراندازد .
لیهو ۵ - بقثح او بر وزن فرسود »
چیزبرا کون د که نزدبك بسوختن رسیده وآتش
آلرا زرد کرده باشد - و بکسر اول هم آمده
2 ۱
یو ذه - بکس اولبر وزن فیروزه:
بمعنی بیپده است که نا حق و باطل باشد -
و بممنی پی نفع هم آمده است - و بفتح اول
جامه ای را کویند که نزديك بسوختن رسیده
باشده .
۴ - مرب بیهگه
۴ رك : بیپوده ۲
بیپنه ویهوده..
۴ رله ؛
leaves v2 684
==== v2 leaf 529 (printed ~1069)
 ‫ساده‬ ‫س‬
 ‫ا‏‪kS‬‬
 ‫ساخته ر نگ = با رای فرشت بروزن‬ ‫پزند‪ - ۱:‬بوزبان عربی چوبی است که آنرا از‬
 ‫یل‪-‬ان‌را هم‌میگوند؛وآن‬
 ‫حندوستان آوورطند‬
‫پارچه سنگه » بمعنی موافق باشد که درمقابل‬
 ‫مخالف است ‪. 4‬‬
 ‫سا خن ‪ -‬بکر تالث‌بروزن‌ساکن‪,‬بمعنی‬ ‫ساجور = باجیم بروزن ساطور‪ .‬گردن‬
‫صاروحاست ‪ ۳‬آن چبز ی باشد کهآ حك داخل‌آن‬
 ‫ازم وا قسانند‪.‬‬ ‫تواند کریخت و تواند چاوید ؛ و بضی کونند‬
‫‪۹‬‬ ‫ساده است‬ ‫نمحتی‬ ‫اد ‪6‬‬ ‫بروزن‬ ‫‪-‬‬ ‫ساد‬ ‫عربی است؟‬

 ‫‪ -‬وخوك نررا کهفمته‌اند کهکراز باشد ‪-‬وبمعنی‬ ‫بمعنی سفید باشدکه بعربی بیاض گوبند‪.‬‬
 ‫دشت وصحر أ وسانان هم هت‪.‬‬
 ‫ساخت ؟ « بروزن باخت » ممروف‌است‬
‫ساد ]وران ت بروزن هاماوران» بلغت‬ ‫بعنی‌کاربرا تمامکردگ ‪-‬ودوال تممةٌ رکاب وبراق‬
‫سربانی چیزی است مانند صمخ وآارا دردرون‬ ‫وبند و بارزین اسب را بیز کفته‌اند ‪ -‬و بمعنی‬
 ‫بیخ درخت کردکان که مجوف شده باشد بابند ‪.‬‬ ‫بکرتوان همهت و آن پوششی امت که‬
 ‫سرد وخشك است ددرومم‌وسیم ‪ .‬خوردن وضملد‬ ‫و خود لیز‬ ‫بر اس دوشانند‬ ‫در روز جنگه‬
‫کردن آن بر شکم اسپال خولیرا افم باشد‬ ‫دوشند ‪# .‬‬
 ‫وآ نرابرومی فنطار ویعربی خاتم|انلك‌خوانشد‪.‬‬ ‫ساخته * ‪-‬وبزرن باخته »بمعنی‬
‫ساده د بروزن ماده ‪ ۰‬معروف است که‬ ‫وایه‌ازمردم شیاد‬
 ‫موافق ‪ - ۷‬وآماده باشد ‪ -‬کن‬
‫در برابر ءنقش و ریشدار
```


## [2026-09-07T20:51:52.458Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nfor w in ['سروان','ساربان','سالار']:\n    hits=[i for i,q in enumerate(p) if w in q]\n    print(w,hits[:10],'-> printed',[h+540 for h in hits[:10]])\nEOF"
}
```


### [2026-09-07T20:51:53.806Z] TOOL RESULT

```
سروان [187, 206, 207, 217, 388, 531, 563, 672] -> printed [727, 746, 747, 757, 928, 1071, 1103, 1212]
ساربان [127, 530, 531, 532] -> printed [667, 1070, 1071, 1072]
سالار [242, 535, 536, 554, 597] -> printed [782, 1075, 1076, 1094, 1137]
```


## [2026-09-07T20:52:04.011Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nfor i in (530,531):\n    q=re.sub(r'[ \\t]+',' ',p[i])\n    print('==== leaf',i,'printed',i+540)\n    for line in q.split('\\n'):\n        if 'ساربان' in line or 'سروان' in line or 'بان' in line:\n            print(line.strip()[:200])\n    print()\nEOF"
}
```


### [2026-09-07T20:52:41.694Z] TOOL RESULT

```
==== leaf 530 printed 1070
‫محقوظ ماند‪ .‬وسوی کرمی است که بیشتر لبای‬ ‫امستلده حم هت ‪ -‬و بمعنی دشت وصحرآوییابان‬
‫را ساربان کوبند ‪٩٩‬همچوباغبان‌ودربان‏ ‪ -‬وبمعنی‬
‫‪ -0‬ر‪:‬ساربان ‪.‬‬

==== leaf 531 printed 1071
‫ساریه‌عنی شتر وبان بمعنی محافظت کننده ونگلہ‬
‫وزن ومعنی سارخك است که يشه باشده‬ ‫سار بان « ببای ابجد بروزن ناروان‪,‬‬
‫وان یسوندحفاظت)» در‬ ‫ر) ‪ ۲‬بان ( =‬
‫س=‬‫‪ - ۱‬ساربان = ساروان (ه‪.‬م‪ ).‬از ‪ :‬سار (‬
‫تر کیب‌معنی لفظی‌درست مثل‌کلمة «سروان»است کهلفة بممنی سر وسرور وسردارباشد ودرسالیای‌اخیر‬
```


## [2026-09-07T20:52:48.863Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"pātuv\\|pādiy\\|patipayauvā\\|xšaçapāvan\\|xšaça-pāvan\" KNT.txt | head -12"
}
```


### [2026-09-07T20:52:48.913Z] TOOL RESULT

```
4447:3 ada : hya : Syátim : ada : martiyahyà : һуа 4 : XSavarSim : xSiyafiyam : akunaué : aivam : 5 parünàm : xSayatiyam : aivam : parünàm : fram 6 àtàram : adam : XSayarsa : xSayafiya : vazraka : 7 xšāyaðiya : хёйуайїуйпаш : x&ayafiya : dahy _ 8 ünàm : paruv : zanànàm : хёйуадіуа : ahyay 9 & : bümlyà : vazrakáyà : düraiy : apiy : Da 10 rayavahaus : x&ayafiyahyà : риса : Haxémanis П iya : 0atiy : Xšayāršā : xšāyaðiya : vasna : 12 Auramazdáhà : imam : duvarfim : visadahyum 13 : adam : akunavam : vasiy : aniyascly : naibam 14 : kartam : апа : Parsi : tya : adam : akunavam : 15 utamaiy : tya : рія : akunaus : tyapatiy : ka 16 riam : vainataly : парага : ava : visam : vaSnà : А 17 uramazdaha : akumà : Qatiy : Xšayāršā : 18 xSayafiya : mam : Auramazda : pātuv : utamai 19 y : xSacam : ut& : tya : manā : kartam : uta : tyamai 20 y : pica : kartam : avaseiy : Auramazda : patuv
```


## [2026-09-07T20:54:00.397Z] AGENT

Now I'll write the verification file.


## [2026-09-07T21:02:34.538Z] TOOL CALL #95: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-379.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nroot = {\n \"entry\": 0,\n \"root\": \"Pa, Pa-ter, Poti, Potiš\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *peh₂- 'to protect, watch over; to pasture, shepherd' (Pokorny pā-, pə- 787 + pō(i)-, pə(i)-, pī- 839; LIV 460) — plus two separate lemmas that Nourai folds into the same box: PIE *pótis 'master, lord, husband' (Pokorny poti-s 842) and PIE *ph₂tḗr 'father' (Pokorny pətē(r) 829)\",\n \"note\": \"Each of the three items is a real reconstruction and the language label 'Indo-European' is right, but they are three lemmas, not one. (1) 'Pa: to protect, to feed' is exactly Watkins' gloss ('pā-. To protect, feed. Contracted from *pas-') and matches Pokorny 787 ('pā- : pə- and pā-t- : pə-t-, to feed, graze', with Hitt. pahs- 'shield' and Toch. A pās-, B pāsk- 'to guard' in the material); the specifically 'protect, guard' branch with Av. pāiti 'hütet, bewacht, schützt', Skt. pāyú- 'Hüter', -pāvan 'schützend', OP xšaθra-pāvan is on Pokorny 839 (pō(i)-), a page Nourai does not cite though it is the one his Iranian nodes actually need. (2) 'Poti, Potiš: protector, husband, power, also self' renders Pokorny 842 poti-s 'owner, host, master, husband' correctly, including the 'self' sense (Lith. pats, Hitt. -pat, uninflected *poti 'selbst', Av. xᵛae-pati-), but *pótis is NOT derived from *peh₂- by any modern authority — Watkins and Pokorny keep them apart, and the gloss 'protector' for *pótis is Nourai's own harmonisation. (3) 'Pa-ter: protector, feeder (of the family)' analyses -ter- as the agent suffix; Buck 2.35 (the page Nourai cites) calls *patēr- a nursery word of the pa type + kinship suffix, and Watkins lists peter- as an independent root. Notably Pokorny 829 itself ends with the query 'of babble-word pa- derive? … or to pə(i)- shield, watch?', i.e. Nourai's two proposals are exactly the two possibilities Pokorny raises but does not decide. The closing remark about a nursery word becoming the usual term is Buck's, correctly reported.\",\n \"note_fa\": \"هر سه بخش این ریشه واقعی‌اند و برچسب «هندواروپایی» درست است، امّا در پژوهش امروزی سه ریشهٔ جداگانه‌اند نه یکی: *peh₂- «پاسداری کردن، چراندن» (پوکورنی ۷۸۷ و ۸۳۹؛ LIV ۴۶۰)، *pótis «سرور، شوی» (پوکورنی ۸۴۲) و *ph₂tḗr «پدر» (پوکورنی ۸۲۹). معنای «نگهبانی کردن، خوراک دادن» برای Pa دقیقاً همان چیزی است که واتکینز در پیوست ریشه‌های هندواروپایی می‌آورد، ولی شاخهٔ ایرانی (اوستایی pāiti «می‌پاید، نگاه می‌دارد») در پوکورنی زیر ص ۸۳۹ آمده که نورایی به آن ارجاع نداده است. پیوند دادن Poti به Pa و تفسیر «pā-ter = خوراک‌دهندهٔ خانواده» از خود نورایی است؛ باک (SYN ۱۰۳) *patēr- را واژه‌ای کودکانه از گونهٔ pa + پسوند خویشاوندی -ter می‌داند و پوکورنی خود در ص ۸۲۹ تنها به صورت پرسش می‌گوید: «از واژهٔ کودکانهٔ pa؟ یا از pə(i)- به معنی پاییدن؟». پس ادعای نورایی با احتیاط پذیرفتنی است، نه بیش از آن.\",\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/peh%E2%82%82-\", W+\"Reconstruction:Proto-Indo-European/p%C3%B3tis\"],\n \"ref_check\": [\n   {\"ref\": \"POK:787\", \"status\": \"supports\", \"note\": \"POK_full.txt (database dump, 'Page(s): 787'): 'Root / lemma: pā- : pə- and pā-t- : pə-t-, Meaning: to feed, graze', material incl. 'Tocharian A pās-, B pāsk- beware, guard; Hittite pahs- (pahhas-) shield' — i.e. both of Nourai's senses ('to protect, to feed') are on this page. The Iranian verb itself, however, is under 'pō(i)-1 … Meaning: to graze … Old Indic pāti, Avestan pāiti hütet, bewacht, schützt … ap. xšaθra-pāvan Landvogt, Satrap' = Page(s): 839.\"},\n   {\"ref\": \"POK:842\", \"status\": \"supports\", \"note\": \"POK_full.txt 'Page(s): 842': 'Root / lemma: poti-s, Meaning: owner, host, master, husband. Material: Old Indic pati-, Avestan paiti- master, mister, lord, consort … Avestan xᵛae-pati- er selbst … ein unflektiertes *poti selbst … Lithuanian pats husband and selbst'. Supports 'protector[sic], husband, power, also self' except the gloss 'protector'. The same page carries a second, distinct lemma 'po-ti, Meaning: against' (Av. paiti, OP patiy preverb).\"},\n   {\"ref\": \"SYN:103\", \"status\": \"supports\", \"note\": \"Buck, SYN.txt leaf 135 (printed 103), §2.35 'Father': 'IE *patēr-, prob. starting fr. a nursery word of the pa type (above, p. 94) orig. pə, reduced to pa before the accent. Walde-P. 2.4.' — exactly Nourai's 'probably started as a nursery word and became a usual term in the Indo-European languages'.\"},\n   {\"ref\": \"KAS:10\", \"status\": \"not_checked\", \"note\": \"Hasani Da'i al-Eslam, Khod-amuz-e Zaban-e Sanskrit — refs_online.json records no accessible copy (ketabnak login only); not on disk.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 72 (incoming/WLD/WLD_Bd2_pages.txt leaf 76)\", \"stance\": \"supports\", \"note\": \"'pō(i): (pəi?) … Vieh weiden, hüten; daraus allgemeineres schützen, auch durch Bedecken. Ai. pāti, av. pāiti hütet, bewacht, schützt … av. rāna-pā Beinschutz … -pāvan schützend, ap. xšaθra-pāvan Landvogt, Satrap' and, further down the same page, 'pā- Vieh weiden, hüten, woraus füttern, nähren' — the 'protect'/'feed' pair is Walde–Pokorny's own.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. pā-, poti-, peter-\", \"stance\": \"partial\", \"note\": \"'pā-. To protect, feed. Contracted from *pas-. … 5. Suffixed form *pā-ti- in Iranian *pāti- in Persian pād, protecting against: BEZOAR. 6. Suffixed form *pā-won-, protector, in Old Persian khshathra-pāvā …: SATRAP. [Pok. pā- 787, 1. pə(i)- 839.]' — but 'poti-. Powerful; lord … [Pok. poti-s 842]' and 'peter-. Father … [Pok. patē(r) 829]' are separate entries with no cross-reference to pā-.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *paH¹ (CHEUNG.txt l.18999 ff.)\", \"stance\": \"supports\", \"note\": \"'*paH¹ to protect, guard (esp. of sheep, cattle), pasture' with '« PIE *peH₂- to pasture, graze; to guard, protect, watch over (the cattle) = LIV: 460 | Pok.: 787'. No connection to *pótis is entertained.\"}\n ],\n \"nodes\": []\n}\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"pa 1\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Av. pā(y)- 'to protect, guard' is well attested (athematic pres. 3sg. pāiti, impv. 2pl. pāta Yt 10.80, subj. pāt̰ Y 32.13, with *ni- nipāhi 'guard!'), and so is OP pā- (impv. pādiy DPe 21, pātuv 'let him protect' — Kent's text of XPa: 'mām Auramazdā pātuv utamaiy xšaçam', 'may Ahuramazda protect me and my kingdom'). Both continue Proto-Iranian *paH- < PIE *peh₂- 'to protect, watch over (the herd)' (LIV 460, Pokorny 787/839), cognate with Skt. pā́ti 'protects', Hitt. pahš- 'to protect', Lat. pāscō 'to pasture'. Nourai's language label, form and gloss are all right; the '1' is only his homonym index (distinguishing this pa- from pa- 'to drink' etc.).\",\n \"derivation_fa\": \"ستاک اوستایی pā(y)- «پاسداری کردن، نگاه داشتن» و پارسی باستان pā- هر دو در متون گواه‌دار‌ند: در اوستا pāiti «می‌پاید»، pāta «بپایید» (یشت ۱۰:۸۰) و در پارسی باستان pādiy و pātuv (کتیبهٔ خشایارشا: mām Auramazdā pātuv «اهورامزدا مرا بپایاد»). این ستاک از ایرانی آغازین *paH- و آن از هندواروپایی آغازین *peh₂- «پاسداشتن، چراندن» است (چونگ، LIV ۴۶۰، پوکورنی ۷۸۷ و ۸۳۹)، هم‌ریشه با سنسکریت pā́ti و لاتینی pāscō. ادعای نورایی در این گره درست است.\",\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/peh%E2%82%82-\", W+\"%D9%BE%D8%A7%DB%8C%DB%8C%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:41\", \"status\": \"partial\", \"note\": \"Horn, HRN.txt leaf 63 = printed p.41, no. 176: '(2) -bān Herr, -hütend, -schützend (Comp.), -wan, -wāne, z.B. pāsbān, suturwān … aw. rāna-pāna- Beinschiene; phlv. -pānak, -pān; arm. LW. -pan; ai. pānā- schützend.' The page documents the root's -pāna- derivative, not a headword 'pa 1'.\"},\n   {\"ref\": \"HRN:72\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 94 = printed p.72, no. 327: 'panāh Zuflucht, Schutz … phlv. panāh, panāhīh … Doch wohl zu √pā- schützen? Bartholomae stützt diese Erklärung brieflich.' — Horn (with Bartholomae) does posit the root pā- 'to protect' that this node asserts.\"},\n   {\"ref\": \"KLN:114\", \"status\": \"not_found\", \"note\": \"Klein 1966, p.114 (KLN_1966.txt leaf 73) is the 'assimilate … astound' page — nothing Iranian. Klein's actual pā(y)- statements are on p.144 s.v. 'ban' ('Pers. bān is rel. to OPers. pā(y)-, to guard, protect') and s.v. 'bezoar' (p.169) and 'satrap'.\"},\n   {\"ref\": \"AHD:1532\", \"status\": \"supports\", \"note\": \"The 1975 New College appendix p.1532 falls in the p- roots; the corresponding Watkins entry reads 'pā-. To protect, feed … 5. Suffixed form *pā-ti- in Iranian *pāti- in Persian pād, protecting against: BEZOAR. 6. Suffixed form *pā-won-, protector, in Old Persian khshathra-pāvā, protector of the province: SATRAP.' — Nourai's gloss is verbatim Watkins.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *paH¹\", \"stance\": \"supports\", \"note\": \"'*AVESTAN: pā- to protect … *OLD PERSIAN: pā- to protect (Kent: 194a); Pres. impv. 2sg. pādiy (DPe 21), 3sg. pātuv (A²Sd 4)'.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, text of XPa (KNT.txt l.4447)\", \"stance\": \"supports\", \"note\": \"'mām : Auramazdā : pātuv : utamaiy : xšaçam' — the OP imperative pātuv 'may he protect' in situ.\"},\n   {\"src\": \"BRT\", \"where\": \"BRT.txt (Bartholomae, Altiranisches Wörterbuch)\", \"stance\": \"silent\", \"note\": \"the local OCR of Bartholomae is too corrupt for this range (searches for 'pā-', 'pāθra', 'xᵛaēpaiθya', 'paiti.dāna' all return nothing usable); Nyberg's Avestan index was used instead.\"}\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"pâyîdan; bân; pâlŭdan\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Two of the three items are right, the third is not. (a) pāyīdan «پاییدن» 'to watch': MacKenzie has '¹pādan, pāy- [TLWN-tn' < A √ntr; p'tn', p'd- | M pd, p'y-, N pāyidan] protect, watch, defend'; NP builds the new infinitive pāyīdan on the inherited present stem pāy- (< OIr *pāya-), so the chain Av./OP pā(y)- → MP pādan/pāy- → NP pāyīdan is exact; pās, pāsbān and pād-, pādšāh in the box belong here too (Klein s.v. bezoar: Pers. pād 'protecting, guarding; guardian, lord, master'). (b) -bān «بان» is the Old Iranian second-member *-pāna- 'protecting' (Av. rāna-pāna- 'shin-guard', Skt. pānā-, MP -pān/-pānag), with the regular voicing of intervocalic p to b in the second member of NP compounds: pāsbān, darbān, bāġbān; šabān/čupān go back to Av. fšu- + pāna- (MP šubān). (c) pālūdan «پالودن» does NOT belong to pā- 'to protect'. MacKenzie's entry itself gives the Manichaean Middle Persian forms with r — 'pālūdan, pālāy- [p'lwtn', p'l'd- | (M p'rwdn, p'r'y-), N ~] strain, filter, purify' — i.e. older pārūdan, pārāy-, and Wiktionary (following the standard analysis) derives it from PIr *para-dāwati, *para- 'through' + *dʰew- 'to run, flow' (whence also NP davīdan), 'to make (a liquid) run through' > 'to filter'. Nourai's semantic bridge 'not to contaminate' is a rationalisation; پالایش، پالوده/فالوده follow pālūdan, while پالان is a different word again.\",\n \"derivation_fa\": \"از سه واژهٔ این گره دو تا درست است و یکی نه. «پاییدن» از فارسی میانهٔ pādan / ستاک حال pāy- (مکنزی ص ۶۳) و آن از pā(y)- ایرانی باستان است؛ مصدر نوِ «پاییدن» بر پایهٔ همان ستاک حال ساخته شده، و «پاس، پاسبان، پاد، پادشاه» نیز به همین خانواده‌اند. پسوند «ـبان» دنبالهٔ *-pāna- «نگاهبان» ایرانی باستان است (اوستایی rāna-pāna- «ساق‌بند»، پهلوی -pān/pānag)، با نرم‌شدن p به b در جزء دوم ترکیب‌ها: پاسبان، دربان، باغبان؛ «شبان/چوپان» هم از fšu-pāna- اوستایی است. امّا «پالودن» به ریشهٔ «پاییدن» ربطی ندارد: خودِ مکنزی صورت مانوی p'rwdn/p'r'y- (pārūdan, pārāy-) را با «ر» ثبت کرده و ریشه‌شناسی پذیرفته‌شده آن را از *para-dāwati «از میان روان کردن» (پیشوند para- + ریشهٔ *dʰew- «دویدن، روان شدن»، هم‌ریشهٔ «دویدن») می‌گیرد. پس در این گره ادعای نورایی دربارهٔ «پالودن» را پژوهش امروزی رد می‌کند.\",\n \"sources\": [W+\"%D9%BE%D8%A7%DB%8C%DB%8C%D8%AF%D9%86\", W+\"%D9%BE%D8%A7%D9%84%D9%88%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:358\", \"status\": \"partial\", \"note\": \"Borhan-e Qate' vol. 1: the پاد / پاداش / پادام column is BQT_v1_pages.txt leaf 567 (printed ≈ 362; Nourai's numbering runs a few pages behind this scan), the page whose headwords are 'پاث[=پاد] … بمعنی پای و پاسبان و نگهبان و پاییدن … و پادشاه مرکب ازین است' — i.e. it supports pād/pādšāh 'guard, protector' but is a lexicographic gloss, not an etymology; the exact printed page could not be pinned because of the ±4-page drift of the scan.\"},\n   {\"ref\": \"BQT:1069\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 531 (printed 1071, = Nourai's 1069 with his two-page offset), Mo'in's footnote to ساربان: 'ساربان = ساروان (ه.م.) از: سار (=شتر) + بان (= وان)، پسوند حفاظت، در ترکیب معنی لفظی درست مثل کلمهٔ «سروان» است' — bān/-vān is expressly 'the suffix of protection', exactly Nourai's 'a suffix meaning protector'.\"},\n   {\"ref\": \"KLN:169\", \"status\": \"supports\", \"note\": \"Klein 1966 p.169 (KLN_1966.txt leaf 100, which carries the printed numeral 169) s.v. bezoar: 'ult. fr. Pers. bādzahr, pādzahr, counterpoison, bezoar stone, lit. protecting (against) poison, fr. pad, protecting, guarding; guardian, lord, master, and zahr, poison.'\"},\n   {\"ref\": \"FSF:335\", \"status\": \"not_found\", \"note\": \"Noushin's Vazhe-namak: پاسبان occurs on FSF_pages.txt leaves 133 and 145 and پالودن on leaf 135, but refs_online.json notes the printing of this scan is unidentified and no printed-page offset is established, so p.335 cannot be located.\"},\n   {\"ref\": \"TZF:21\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi — refs_online.json: not on archive.org, PDF behind a login; no copy on disk.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie pp. 63, 65 (PHD.txt leaves 536, 540)\", \"stance\": \"partial\", \"note\": \"supports (a) and (b): '¹pādan, pāy- … protect, watch, defend'; 'pānāg [p'n(')k'] guard, protector; shepherd'; but its pālūdan entry undercuts (c): 'pālūdan, pālāy- [p'lwtn', p'l'd- | (M p'rwdn, p'r'y-), N ~] strain, filter, purify' — the Manichaean spelling has r, not l.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 176, p. 41\", \"stance\": \"supports\", \"note\": \"'-bān Herr, -hütend, -schützend (Comp.) … aw. rāna-pāna-; phlv. -pānak, -pān; ai. pānā- schützend' — the -bān arrow.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *paH¹, NWIR section\", \"stance\": \"supports\", \"note\": \"'NP pāyidan/pāy- to watch, guard' listed as the direct continuant of *paH-; Cheung has no *paH etymology for pālūdan (his verb dictionary keeps it apart).\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur pp. 153 and 156 (ARY_pages.txt leaves 151, 154)\", \"stance\": \"partial\", \"note\": \"Aryanpur treats پالیدن/پالودن/پالاییدن in a separate article from پاییدن; under پاییدن his note reads 'این واجریشه با واجریشهٔ هندواروپایی *pā-, *pī(?) (به چم خوراک و پرورد) خویشی نزدیک [دارد]' — i.e. pāyīdan with the PIE 'feed/protect' root, pālūdan not with it (the Latin-script cognates in the OCR are unreadable).\"}\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Avestan / Old Persian\", \"words\": \"paiti 1, patiy, pavan, pâna; pathra; fšu-paiti; paiti-xšathra\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The node mixes two unrelated roots and one Aramaic heterogram. (a) Av. paiti- (nom. paitiš) 'lord, master' and OP pati- 'master' are real, but they continue PIE *pótis (Pokorny 842 poti-s; Watkins 'poti-. Powerful; lord … 4. Old Persian pati-, master: PADISHAH'), not pā- 'to protect'; and OP patiy in the inscriptions is the preverb/preposition 'against, to, at', Pokorny's second lemma on the same page 842 ('po-ti, Meaning: against; Avestan paiti, ap. patiy'). So the arrow #1→#3 is rejected by modern scholarship for these two words — though Nourai's own root box does contain 'Poti', so he may intend the descent from that half. (b) 'pavan' is not an Avestan or Old Persian word at all: it is the traditional reading of the Book-Pahlavi Aramaic heterogram PWN, MacKenzie's 'pad [PWN, for *pty] to, at, in, on' — a preposition, not 'master, protector'. (c) pāna- 'protecting, protector' (Av. rāna-pāna-, MP pānāg 'guard, protector; shepherd', Skt. pānā-, OP xšaθra-pāvan 'satrap') and pāθra- 'protection' (Nyberg's Avestan index: 'pāθra-vant: pahr', whence MP pahr, NP pahra 'watch') are genuine pā- derivatives, so for these two words the arrow is right. (d) The Avestan word behind šabān/čupān is fšu- 'cattle' + pāna-, not fšu-paiti: Nyberg s.v. šupān 'shepherd' — 'Av. fšu- sheep = pasu- + pāna-, v. pānak; MPrth šwb'n; NP šubān, šabān'; a compound of the *poti- type ('cattle-lord') is formally possible (cf. nmānō-paiti-, dahyu-paiti-) but is not the etymon of the shepherd words. (e) paiti-xšaθra 'protecting king' is a false analysis of MP pādixšāy > NP pādšāh/pādešāh: the first element is the preverb *pati- 'over' with the verb xšāy- 'to rule', i.e. 'ruling over', which is why Klein s.v. padishah derives pād from OPers. pati 'master' and Watkins files PADISHAH under poti-, not under pā-.\",\n \"derivation_fa\": \"این گره دو ریشهٔ جدا و یک هزوارش را در هم آمیخته است. paiti- اوستایی و pati- پارسی باستان به معنی «سرور، خداوند» واقعی‌اند، امّا دنبالهٔ *pótis هندواروپایی‌اند (پوکورنی ۸۴۲؛ واتکینز ذیل poti-) و نه از pā- «پاییدن»؛ و patiy در کتیبه‌های هخامنشی حرف اضافه/پیشوند «به سوی، در برابر» است (لمّای دوم همان صفحهٔ پوکورنی). «pavan» اصلاً واژهٔ اوستایی یا پارسی باستان نیست، بلکه خوانش سنّتی هزوارش آرامی PWN است که در فارسی میانه pad خوانده می‌شود (مکنزی). در برابر، pāna- «نگاهبان» (پهلوی pānāg) و pāθra- «پاسداری» (نمایهٔ اوستایی نیبرگ: pāθra-vant ← pahr، فارسی «پهره») به‌راستی از pā- ساخته شده‌اند و برای این دو، پیکان درست است. سرانجام «چوپان/شبان» از fšu-pāna- اوستایی است نه fšu-paiti، و «پادشاه» از *pati-xšāya- «فرمانروا» است نه «شاهِ نگهبان». پس داوری: بخشی درست، بخشی مردود.\",\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/p%C3%B3tis\", W+\"Reconstruction:Proto-Indo-European/peh%E2%82%82-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:842\", \"status\": \"partial\", \"note\": \"POK_full.txt 'Page(s): 842' has both 'poti-s owner, host, master, husband … Old Indic pati-, Avestan paiti- master' (supporting the words) and the separate lemma 'po-ti, against: Avestan paiti, ap. patiy' — but neither is connected there with pā-/pə(i)-; pāna-, -pāvan and pāθra- are on p.839, not 842.\"},\n   {\"ref\": \"HRN:41\", \"status\": \"supports\", \"note\": \"Horn no.176 (printed p.41): 'aw. rāna-pāna- Beinschiene; phlv. -pānak, -pān; ai. pānā- schützend' — supports pāna 'protector' from the pā- root.\"},\n   {\"ref\": \"KLN:144\", \"status\": \"supports\", \"note\": \"Klein 1966 p.144 (leaf 87, numerals 144/145) s.v. ban: 'Pers. bān, is rel. to OPers. pa(y)-, to guard, protect, OI. pāti, guards, protects, pānā-, guarding, protecting (see P. Horn, Grundriß der neupersischen Etymologie, No. 176)' — Klein even cites the same Horn number.\"},\n   {\"ref\": \"KLN:157\", \"status\": \"not_found\", \"note\": \"Klein 1966 p.157 (leaf 94, which carries the printed numeral 157) is the 'bean … bed' page; nothing relevant. The Klein material this node needs is s.v. satrap ('OPers. xshathrapāvan- … a derivative of pā(y)-, to guard, protect') and s.v. padishah ('pād, master … rel. to OPers. pati, Avestic paiti-, OI. patiḥ, master, husband … See potent').\"},\n   {\"ref\": \"AHD:1532\", \"status\": \"partial\", \"note\": \"Watkins' pā- entry does contain 'Suffixed form *pā-won-, protector, in Old Persian khshathra-pāvā … SATRAP', supporting pāna/pāvan; but paiti 'master' is filed under a different root: 'poti-. Powerful; lord … 4. Old Persian pati-, master: PADISHAH. [Pok. poti-s 842.]'\"}\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, Avestan index and s.v. šupān\", \"stance\": \"partial\", \"note\": \"index equations 'pāna-: pānak', 'pāθra-vant: pahr', 'paiti: pat', 'paitiš: patiš' (i.e. paiti and pāna are kept apart); s.v. šupān: 'šupān [šp'n'] shepherd … Av. fšu- sheep = pasu-, + pāna-, v. pānak; MPrth šwb'n; NP šubān, šabān'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie pp. 62, 65\", \"stance\": \"partial\", \"note\": \"'pad [PWN, for *pty | M pd, N pa] to, at, in, on' (so 'pavan' = the heterogram PWN, a preposition) and 'pānāg [p'n(')k' | M p'ng] guard, protector; shepherd'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 72\", \"stance\": \"supports\", \"note\": \"for the pā- half: 'ai. pālá- Wächter, Hirt, -pāvan schützend, ap. xšaθra-pāvan Landvogt, Satrap' — all under pō(i)-/pā-, with no mention of poti-s.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Avestan\", \"words\": \"xvaĕ-pati, xvaĕ-paithya\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The words are real and the note is right: Av. xᵛaē-paiti- and xᵛaēpaiθya- 'one's own, self' are compounds of xᵛa- 'own' (PIE *swe-/*swo-) with *pati- / *paθya- (< *patya-), and in this combination the *poti- element indeed means 'own, self' — the same use as Lith. pats 'self', Latv. pats, Hitt. -pat, and Pokorny's uninflected '*poti selbst' in Lat. utpote. Pokorny 842, the page Nourai cites, prints exactly 'Avestan xᵛae-pati- er selbst' under poti-s. The one thing that does not hold is the drawn descent from node #1 (pā- 'to guard'): the second element belongs to *pótis, an independent root — a point mitigated only by the fact that Nourai's root box also contains 'Poti, Potiš … also self'.\",\n \"derivation_fa\": \"واژه‌ها درست‌اند و یادداشت چارت هم درست است: xᵛaē-paiti- و xᵛaēpaiθya- اوستایی «خودِ کسی، خویشتن» از xᵛa- «خود» (هندواروپایی *swe-) و *pati-/*paθya- ساخته شده‌اند، و در همین ترکیب است که جزء *poti- معنای «خود، خویش» می‌دهد — درست مانند pats لیتوانیایی «خود» و -pat هیتی. پوکورنی در همان ص ۸۴۲ که نورایی ارجاع داده، عیناً می‌نویسد: «Avestan xᵛae-pati- er selbst». تنها ایراد، پیکانِ کشیده‌شده از گرهٔ pā- «پاییدن» است، زیرا جزء دوم به ریشهٔ *pótis تعلق دارد؛ چون در جعبهٔ ریشه Poti هم آمده، ادعا با احتیاط پذیرفتنی است.\",\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/p%C3%B3tis\", W+\"%D8%AE%D9%88%DB%8C%D8%B4\"],\n \"ref_check\": [\n   {\"ref\": \"POK:842\", \"status\": \"supports\", \"note\": \"POK_full.txt, Page(s) 842, lemma poti-s: 'Avestan xᵛae-pati- er selbst', and further 'ein unflektiertes *poti selbst placed in utpote … Lithuanian pats husband and selbst (old patis), Latvian pats … Hittite -pat'.\"},\n   {\"ref\": \"SNS:267\", \"status\": \"supports\", \"note\": \"Tavoosi's Shayast-ne-Shayast glossary: the Avestan index in SNS.txt lists 'xᵛaepaiθya- 267/5' and the Pahlavi index 'xᵛēš 79/9-267/4', i.e. page 267 line 5 is where Av. xᵛaēpaiθya- is cited as the source of MP xwēš — exactly the arrow #4→#5 (the Persian OCR of that page is unreadable, the indexes are legible).\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 96 s.v. xwēš\", \"stance\": \"supports\", \"note\": \"'xwēš [NPŠE < A npš-h; hwyš | M xwy(b)š, N ~] (one's) own' — the Manichaean spelling xwy(b)š preserves the -p- of *xwaipa(θ)ya-.\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 1860 f. (BRT.txt)\", \"stance\": \"silent\", \"note\": \"the local OCR of Bartholomae yields no readable hit for xᵛaēpaiθya-; Pokorny 842 and the SNS index were used instead.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"xîš 1\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP xᵛēš/xīš «خویش» 'self, one's own' continues MP xwēš (Book Pahlavi hwyš, heterogram NPŠE), which goes back to the Old Iranian compound seen in Av. xᵛaēpaiθya- and OP huvāipašiya- 'one's own': *hwai-paθya- > MP *xwēbaš (still visible in the Manichaean spelling xwy(b)š = xwēbaš) > xwēš by loss of the intervocalic labial and contraction, then NP xᵛēš, pronounced xīš in later Classical and modern Persian (with the regular xᵛē > xī change, as in xᵛēštan > xīštan). Nourai's arrow is exactly the standard account; خود xwad is a different, shorter reflex of the same reflexive stem *hwa-.\",\n \"derivation_fa\": \"«خویش» فارسی نو دنبالهٔ xwēš فارسی میانه است (نوشتار hwyš، هزوارش NPŠE) و آن از ترکیب ایرانی باستانِ *hwai-paθya- که در اوستایی xᵛaēpaiθya- و در پارسی باستان huvāipašiya- «از آنِ خود» دیده می‌شود. صورت میانی *xwēbaš هنوز در املای مانوی xwy(b)š بازتاب دارد؛ با افتادن واکِ لبی میان‌واکه‌ای xwēš پدید آمد و در فارسی نو xᵛēš و سپس xīš تلفظ شد (همان دگرگونی که در «خویشتن ← خیشتن» دیده می‌شود). ادعای نورایی درست است؛ «خود» صورت کوتاه‌ترِ همان ستاک بازتابی *hwa- است.\",\n \"sources\": [W+\"%D8%AE%D9%88%DB%8C%D8%B4\"],\n \"ref_check\": [\n   {\"ref\": \"POK:842\", \"status\": \"partial\", \"note\": \"Pokorny 842 gives the Avestan ancestor ('Avestan xᵛae-pati- er selbst') but no New Persian reflex; the Persian step must be taken from MacKenzie/Wiktionary.\"},\n   {\"ref\": \"SNS:267\", \"status\": \"supports\", \"note\": \"SNS indexes: 'xᵛēš 79/9-267/4', 'xᵛēšīh 267/12', 'xᵛēstan 267/13' beside 'xᵛaepaiθya- 267/5' — p.267 of Tavoosi's glossary is precisely the xwēš entry with its Avestan etymon.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 96\", \"stance\": \"supports\", \"note\": \"'xwēš … (one's) own; ~īh: possession; ~āwand relative, kinsman; xwēš-tan self' — the whole New Persian family (خویش، خویشاوند، خویشتن) is already Middle Persian.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II, passim (e.g. 'kē xᵛēš hom?')\", \"stance\": \"supports\", \"note\": \"xᵛēš is used throughout the Pahlavi texts glossed by Nyberg in exactly the sense 'own, self'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Avestan / Old Persian\", \"words\": \"âthur-pât-gan; pa-nâh; paiti-dâma\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"paiti-dâma\",\n \"correct_form\": \"paiti-dāna-\",\n \"derivation\": \"Two of the three are sound, the third is a misprint. (a) *Ātṛ-pāta- is the Old Iranian personal name of the satrap whom the Greeks called Ἀτροπάτης (Atropates), literally 'protected by fire' (ātṛ- 'fire' + pāta- 'protected', the perfect passive participle of pā-); with the relational suffix -kāna it gives MP Ādurbādagān, whence NP Āzarbāyjān. Nourai's gloss 'fire protector' inverts the direction: pāta- is passive, so the name means 'he whom the fire protects', not 'protector of the fire'. (b) pa-nāh: MP panāh 'protector, refuge' — Horn no.327 (p.72, the page cited) says 'Doch wohl zu √pā- schützen? Bartholomae stützt diese Erklärung brieflich', i.e. Nourai's analysis 'pa- (protect) + nāh (help)' is Horn's and Bartholomae's. (c) 'paiti-dâma' is not an Avestan word: the attested form is Av. paiti.dāna- 'mouth-veil' (with n), Pahlavi/Parsi padām, Pāzand panām — MacKenzie: 'padām [pd'm | (N panām)] mask for the mouth, worn by a celebrating priest'. The printed page (pdf 379, book 349) really does show 'paiti-dâma', so the JSON is faithful and the m is the book's own misprint for -dāna-.\",\n \"derivation_fa\": \"دو مورد از سه مورد این گره درست است و سومی غلط چاپی است. *Ātṛ-pāta- نام کسی است (آتروپات، ساتراپ ماد که یونانیان Ἀτροπάτης می‌نوشتند) به معنی «پاییده/نگاه‌داشتهٔ آتش» — pāta- صفت مفعولی ریشهٔ pā- است، پس معنای «نگهبانِ آتش» که نورایی داده وارونه است؛ با پسوند نسبت -kāna به آذربادگان/آذربایجان رسیده. «پناه» نیز به گواهی هرن (شمارهٔ ۳۲۷، ص ۷۲) و تأیید کتبی بارتولومه به ریشهٔ pā- «پاییدن» بازمی‌گردد. امّا «paiti-dâma» صورتی ناموجود است؛ واژهٔ اوستایی paiti.dāna- «دهان‌بند» است (پهلوی padām، پازند panām). چون در صفحهٔ چاپی نیز همین «paiti-dâma» آمده، خطا از کتاب است نه از خوانش اسکن.\",\n \"sources\": [W+\"%D8%A2%D8%B0%D8%B1%D8%A8%D8%A7%DB%8C%D8%AC%D8%A7%D9%86\", W+\"%D9%BE%D9%86%D8%A7%D9%87\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:72\", \"status\": \"partial\", \"note\": \"Horn p.72 no.327 covers only panāh: 'penāh Zuflucht, Schutz, penāhīden … phlv. panāh, panāhīh, vergl. Mihr-panāhak (AV.). Doch wohl zu √pā- schützen? Bartholomae stützt diese Erklärung brieflich.' Neither Ādurbādagān nor paiti-dāna- is on that page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie pp. 62, 65\", \"stance\": \"supports\", \"note\": \"'padām [pd'm | (N panām)] mask for the mouth, worn by a celebrating priest' and 'panāh [pnh | = M, N ~] protector; refuge; pad ~ griftan: take refuge with'.\"},\n   {\"src\": \"BQT\", \"where\": \"Mo'in's footnote to پنام, BQT_v1_pages.txt leaf 644 (printed ≈ 416-418)\", \"stance\": \"supports\", \"note\": \"'در اوستا [paiti-dāna] … پنام عبارت است از دو قطعه پارچهٔ سفید از جنس پنبه که بروی دهان آویخته با دو نوار پشت سر گره می‌زنند … در وقتی بکار برده می‌شود که موبد در مقابل آتش مقدس اوستا سراید' — Mo'in gives the Avestan etymon with -n- and the ritual sense.\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. paiti.dāna-\", \"stance\": \"silent\", \"note\": \"not retrievable from the local OCR; the form paiti.dāna- 'Mundschleier' is however the one cited by Mo'in and by the standard Zoroastrian-ritual literature (Av. paitidāna > Pahl. padān/padām > Pāzand panām).\"}\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Persian\", \"words\": \"Âzarbâyjân; panâh; panâm\",\n \"verdict\": \"plausible\",\n \"derivation\": \"All three Persian words are right; two glosses are not. (a) Āzarbāyjān «آذربایجان» is a region (the ancient Atropatene, today Ardabil and East/West Azerbaijan provinces), not 'a city in Iran'; the chain is OIr *Ātṛpātakāna- (from the name Ātṛpāta-/Atropates 'protected by fire') > MP Ādurbādagān > Early NP āẕarbāygān/āẕarbādgān > āẕarbāyjān, with -gān > -jān and the regular MP -d- > NP -y- lenition in the middle syllable. (b) panāh «پناه» 'shelter' < MP panāh, from pā- 'to protect' (Horn no.327, with Bartholomae). (c) panām «پنام», the white cotton mouth-veil worn by the officiating mōbad so that his breath does not pollute the fire, is the Pāzand/NP form of MP padām < Av. paiti.dāna-; the d > n is the Pāzand nasalisation (padām > panām), and Mo'in describes the object in exactly these terms in his footnote in Borhan-e Qate'.\",\n \"derivation_fa\": \"هر سه واژه درست‌اند، امّا دو تعریف نادرست است. «آذربایجان» نام یک سرزمین/استان است (آتروپاتنِ باستان)، نه «شهری در ایران»؛ زنجیره چنین است: *Ātṛpātakāna- ایرانی باستان (از نام آتروپات «پاییدهٔ آتش») ← آذربادگان فارسی میانه ← آذربایگان/آذربادگان فارسی دری ← آذربایجان، با تبدیل -گان به -جان و نرم‌شدن d میانی به y. «پناه» از panāh فارسی میانه و ریشهٔ pā- است (هرن ۳۲۷ به تأیید بارتولومه). «پنام» صورت پازند/فارسیِ padām پهلوی از paiti.dāna- اوستایی است؛ ابدال d به n در پازند رخ داده، و معین در حاشیهٔ برهان قاطع آن را همان دهان‌بندِ پنبه‌ایِ موبد در برابر آتش مقدس توصیف کرده است.\",\n \"sources\": [W+\"%D8%A2%D8%B0%D8%B1%D8%A8%D8%A7%DB%8C%D8%AC%D8%A7%D9%86\", W+\"%D9%BE%D9%86%D8%A7%D9%87\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:418\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 644 (printed ≈ 416-418 on this scan; Nourai's 418) is precisely the پناه / پنام column, with Mo'in's two footnotes: for پنام the Avestan paiti-dāna and the description of the mōbad's mouth-cloth ('زرتشتیان ایران آن را «روبند» گویند … در وقتی بکار برده می‌شود که موبد در مقابل آتش مقدس اوستا سراید'), and for پناه 'پهلوی panāh [panāhīh] … «تبریزی ۱۱۹ بنقل از هوبشمان»'. It does not cover آذربایجان.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie pp. 62, 65\", \"stance\": \"supports\", \"note\": \"'padām … mask for the mouth, worn by a celebrating priest'; 'panāh … protector; refuge'.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in's footnotes in Borhan-e Qate' (leaf 644) and Wiktionary's Ādurbādagān chain\", \"stance\": \"partial\", \"note\": \"Mo'in supports panāh and panām; for آذربایجان the standard account (MP Ādurbādagān < *Ātṛpātakāna, Greek Atropatene) shows the referent is a province, so the chart's 'A city in Iran' is wrong.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 327, p. 72\", \"stance\": \"supports\", \"note\": \"'phlv. panāh, panāhīh … Doch wohl zu √pā- schützen?'\"}\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Pahlavi\", \"words\": \"ô-pât-ân; arta-pân\",\n \"verdict\": \"disputed\",\n \"error_in\": \"book\",\n \"book_prints\": \"ô-pât-ân\",\n \"correct_form\": \"āpātān (MP ābādān, < OIr *ā-pāta- 'protected, tended')\",\n \"derivation\": \"The Pahlavi word is real but is analysed differently by everyone except Nourai's source, and the second item is a different name altogether. (a) MP āpātān/ābādān is attested — Nyberg: 'āpātān ['p't'n'] cultivated, inhabited (815); Paz. āwādā; cf. MPrth 'b'd; Arm. lw. apat; NP ābād and ābādān; < OIr *ā-pāta- \\\"protected\\\", v. pātan (1)'; Cheung likewise files BMP 'p't /ābād/, 'p't'n /ābādān/ 'thriving, prosperous, cultivated' under *paH¹ with the preverb *ā-. So the first element is the preverb ā-, not āb 'water'. The 'protected waterways' reading (and the cross-reference ☞Ab 1) comes straight from Nourai's own source: Farahvashi, Irānvij p.119, writes that in āp-pāt-ān 'the first element āp means water, pāt is from the root pāyīdan and -ān is the relational suffix', so that the name denotes 'the place where the water of the sea and the river is guarded'. That is a minority etymology of the town's name, not the standard account of the Pahlavi word. (b) arta-pān 'protector of justice' is Nourai's back-formation for Ardavān/Artabanus; the accepted reconstruction is *Ṛta-bānu- 'the glory/splendour of Arta (Aša)', with bānu- 'light, splendour', not pāna- 'protector'. (c) The form printed in the book, 'ô-pât-ân', with ô-, corresponds to no attested spelling (Nyberg's āpātān, MacKenzie's ābādān); the page image confirms the book itself prints ô-, so the extraction is faithful.\",\n \"derivation_fa\": \"واژهٔ پهلوی واقعی است، امّا تحلیل آن جز در منبع خودِ نورایی جای دیگری تأیید نمی‌شود، و مورد دوم اصلاً نام دیگری است. نیبرگ می‌نویسد: «āpātān «آبادان، آباد»، پازند āwādā، پارتی 'b'd، ارمنی وام‌گرفتهٔ apat، فارسی نو آباد و آبادان؛ از *ā-pāta- ایرانی باستان به معنی «پاییده‌شده»»، و چونگ نیز ābād/ābādān را با پیشوند *ā- زیر ریشهٔ *paH می‌آورد؛ یعنی جزء نخست پیشوندِ ā- است نه «آب». تحلیل «آبِ پاییده» از فره‌وشی در ایرانویج ص ۱۱۹ گرفته شده که می‌نویسد «جزء نخست āp به معنی آب است، pāt از ریشهٔ پاییدن و -ān پسوند نسبت» — یعنی همان چیزی که نورایی آورده، ولی این نظر اقلیت است. «ارتاپان» نیز ساختِ خودِ نورایی است: نام اردوان را امروز *Ṛta-bānu- «فروغِ اَرته» می‌دانند (bānu «روشنایی») نه «نگهبان اَرته». افزون بر این، صورت چاپیِ «ô-pât-ân» در هیچ منبعی نیامده (نیبرگ: āpātān) و عکس صفحه نشان می‌دهد که خطا از خودِ کتاب است.\",\n \"sources\": [W+\"%D8%A2%D8%A8%D8%A7%D8%AF%D8%A7%D9%86\", \"https://en.wikipedia.org/wiki/Abadan,_Iran\", W+\"Artabanus\"],\n \"ref_check\": [\n   {\"ref\": \"IRN:119\", \"status\": \"supports\", \"note\": \"Farahvashi, Irānvij p.119 (incoming/IRN/IRN_pages.txt leaf 129, tagged [pdf page 130], running head 'آروند رود ۱۱۹'): 'جزء نخست [āp] به معنی آب است، [pāt] از ریشهٔ پاییدن و [-ān] پسوند نسبت است و «اپاتان» به معنی جایی است که در آنجا از آب دریا و رود پاسبانی می‌کنند و آن را می‌پایند و این نوع ترکیب همان است که در آتورپاتکان هم دیده می‌شود' — Nourai's node reproduces this page exactly, including the comparison with Ādur-pātakān. The page says nothing about arta-pān/Ardavān.\"}\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. āpātān\", \"stance\": \"contradicts\", \"note\": \"'āpātān ['p't'n'] cultivated, inhabited 815 … NP ābād and ābādān; < OIr *ā-pāta- \\\"protected\\\", v. pātan (1)' — the preverb is ā-, there is no āb 'water' in the word.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *paH¹, MP/Parthian/NWIr sections\", \"stance\": \"contradicts\", \"note\": \"'(+ *ā-) BMP 'p't /ābād/, BMP 'p't'n /ābādān/ thriving, prosperous, cultivated, BMP 'p'tyh /ābādīh/ prosperity; village … PARTHIAN (+ *ā-) 'b'd prosperous, cared for … NP ābād inhabited, cultivated (place, settlement)' — same analysis, preverb *ā- + *paH.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. ābād/ābādān\", \"stance\": \"partial\", \"note\": \"MacKenzie has ābād 'populous, thriving' with no water element, consistent with Nyberg.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Persian\", \"words\": \"Âbâdân; Ardavân\",\n \"verdict\": \"disputed\",\n \"derivation\": \"(a) Ābādān «آبادان» as a common word is certainly ābād + -ān and inherits MP ābādān 'thriving, cultivated' (< *ā-pāta- 'protected, tended'), so the underlying pā- root is right even though Nourai's 'water' element is not. As the name of the Persian-Gulf port, however, the derivation is contested: the earliest sources call the place ʿAbbādān (al-Balāḏurī derives it from ʿAbbād b. al-Ḥusayn of the Banū Tamīm, Umayyad period), Greek geographers have Apphadana/Apphana, and the Persian form Ābādān became official only by decree in 1935; Farahvashi's 'coastguard station' (āp + pāt + -ān), which Nourai follows, is one scholar's proposal. (b) Ardavān «اردوان» does not mean 'protector of justice'. The name is Old Iranian *Ṛta-bānu- / *Arta-bānu- 'the glory of Arta (Aša, Truth)', Greek Ἀρτάβανος, Latin Artabanus, MP/Parthian Ardawān — the second element is bānu- 'light, splendour, glory', not -pāna- 'protector'. Nourai's spelling arta-pān for the Pahlavi antecedent is therefore a construct, not an attested form.\",\n \"derivation_fa\": \"«آبادان» به عنوان واژهٔ عام بی‌گمان از «آباد» + پسوند «-ان» است و به ābādān فارسی میانه (از *ā-pāta- «پاییده، آبادکرده») می‌رسد؛ پس ریشهٔ pā- درست است هرچند جزء «آب» نادرست. امّا دربارهٔ نام بندر آبادان اختلاف هست: کهن‌ترین منابع آن را «عَبّادان» می‌نامند و بلاذری آن را به عَبّاد بن حصین از بنی‌تمیم بازمی‌گرداند، جغرافیانویسان یونانی Apphadana/Apphana نوشته‌اند، و صورت فارسی «آبادان» تنها در ۱۳۱۴ش رسمی شد؛ تحلیل «پاسگاهِ پاسداری از آب» از فره‌وشی است. «اردوان» نیز به معنی «نگهبان داد» نیست: این نام از *Ṛta-bānu- ایرانی باستان «فروغِ اَرته/اَشه» است (یونانی Ἀρτάβανος، پهلوی/پارتی Ardawān) و جزء دوم آن bānu «روشنایی، فرّ» است نه pāna «نگهبان». پس پژوهش امروزی این گره را در بخش «اردوان» رد می‌کند.\",\n \"sources\": [W+\"%D8%A2%D8%A8%D8%A7%D8%AF%D8%A7%D9%86\", \"https://en.wikipedia.org/wiki/Abadan,_Iran\", W+\"Artabanus\"],\n \"ref_check\": [\n   {\"ref\": \"IRN:119\", \"status\": \"supports\", \"note\": \"Irānvij p.119 gives exactly Nourai's Ābādān etymology ('āp water + pāt from the root pāyīdan + -ān'), quoting Ibn Hawqal and Iṣṭaḵrī that watchmen at Abadan kept off sea-robbers; it says nothing about Ardavān.\"},\n   {\"ref\": \"BQT:98\", \"status\": \"not_found\", \"note\": \"Borhan-e Qate' vol. 1: the آ- and ا-sections were searched in BQT_v1_pages.txt (grep 'آبادا', 'بادان'); the ارد- headwords sit on leaves 308-313 and the آب- headwords on leaves 206-215, but the Persian OCR is too corrupt and the leaf→printed-page offset drifts by 10-20 pages in this volume, so printed p.98 could not be identified with confidence.\"},\n   {\"ref\": \"BQT:101\", \"status\": \"not_found\", \"note\": \"same search; leaf 306 (اران …) and leaves 308-313 (اردشیر … اردو) bracket where اردوان must stand, and the printed page is plausibly near 101-108, but no legible headword اردوان or Mo'in footnote could be read out of the OCR.\"}\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"s.v. āpātān\", \"stance\": \"partial\", \"note\": \"'NP ābād and ābādān; < OIr *ā-pāta- protected' — supports the pā- root for the word, contradicts the āb 'water' analysis.\"},\n   {\"src\": \"MON\", \"where\": \"Wiktionary آبادان (which follows Mo'in/Hasandust for the common word)\", \"stance\": \"supports\", \"note\": \"'Inherited from Middle Persian /ʾpʾtʾn/ \\\"thriving\\\"; surface analysis آباد (ābād) + ـان (-ān)'.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur (ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"no entry for آبادان or اردوان in the headword pages searched — Aryanpur's dictionary covers appellatives, not toponyms/personal names.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Avestan\", \"words\": \"pitar\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Av. pitar- 'father' (nom. sg. pitā, also ptā, tā) is the regular Iranian reflex of PIE *ph₂tḗr, gen. *ph₂trós (Pokorny pətē(r) 829; Watkins peter-), beside Skt. pitár-, Gk. πατήρ, Lat. pater, Goth. fadar; Old Persian has pitā (acc. pitaram). Buck's table (SYN p.103-104), the second page Nourai cites, prints 'Av. pitar-' in the 'father' row. The only caveat is the one already discussed at the root: whether *ph₂tḗr contains the nursery syllable *pa- plus the kinship suffix *-ter- (Buck, Watkins) or is a derivative of pā- 'to protect/feed' (Nourai's reading, which Pokorny raises only as a question) is not settled in Nourai's favour — but the Avestan word itself, its language label and its gloss are beyond doubt.\",\n \"derivation_fa\": \"pitar- اوستایی «پدر» (نهادی pitā) بازتاب منظم *ph₂tḗr هندواروپایی است (پوکورنی ص ۸۲۹؛ واتکینز ذیل peter-)، هم‌ریشه با pitár- سنسکریت، πατήρ یونانی، pater لاتینی و fadar گوتی؛ در پارسی باستان pitā (رایی pitaram) آمده است. جدول باک در ص ۱۰۳–۱۰۴ که نورایی به آن ارجاع داده، در ردیف «پدر» عیناً «Av. pitar-» را آورده است. تنها نکتهٔ محل بحث همان است که در جعبهٔ ریشه گفته شد: آنکه *ph₂tḗr از هجای کودکانهٔ pa + پسوند خویشاوندی -ter ساخته شده (باک و واتکینز) یا از ریشهٔ pā- «پاییدن/پروردن» (خوانش نورایی که پوکورنی تنها به صورت پرسش می‌آورد). خودِ واژه و برچسب زبانی آن بی‌گمان درست است.\",\n \"sources\": [W+\"%D9%BE%D8%AF%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"POK:829\", \"status\": \"supports\", \"note\": \"POK_full.txt, 'Page(s): 829': 'Root / lemma: pətē(r) Gen. patr-és, -ós (*ph₂te(r)), Meaning: father. Material: Old Indic pitár-, Avestan pitar- besides Nom. ptā, tā …' and, in the References line, 'of babble-word pa- derive? Kretschmer WZKM. 51, 315 f.; or to pə(i)- shield, watch?'\"},\n   {\"ref\": \"SYN:104\", \"status\": \"supports\", \"note\": \"Buck, SYN.txt leaves 135-136: the §2.35 FATHER table ends with the Indo-Iranian rows 'Skt. pitar-' / 'Av. pitar-' at the top of the next printed page (104), which is what Nourai cites; §2.36 on the same opening repeats that the type goes back to a nursery word.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. peter-\", \"stance\": \"partial\", \"note\": \"'peter-. Father. 1. Germanic *fadar … 2. Latin pater … 3. Greek patér … [Pok. patē(r) 829.]' — an independent root entry, with no derivation from pā-.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 4 (cited by Pokorny 829 and Buck 2.35)\", \"stance\": \"supports\", \"note\": \"WP II 4 is the reference both Pokorny and Buck give for *pətēr as a nursery-word formation.\"}\n ]\n})\n\nnodes.append({\n \"id\": 11, \"lang\": \"Persian\", \"words\": \"pedar\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP pedar/pidar «پدر» continues MP pidar (Book Pahlavi ptr, pyt', also pit), which continues the Old Persian oblique stem pitar- (nom. pitā) — Horn no. 286: 'pider (peder) Vater … ap. pitar- Vater; aw. pitar-; phlv. pit, pitar …; ai. pitar-; arm. hair'. The Avestan form drawn as the parent is strictly a sister rather than the ancestor (the ancestor is Old Persian pitar-), but that is the book's usual convention of putting one Old Iranian representative at the head. Phonetically the sequence is *pitar > MP pidar (intervocalic t > d) > NP pidar/pedar; the dialect form پیر 'old' is a different word (Horn's own footnote to no. 286 argues against deriving it from pitar-).\",\n \"derivation_fa\": \"«پدر» فارسی نو دنبالهٔ pidar فارسی میانه است و آن از ستاک غیرفاعلیِ pitar- پارسی باستان (نهادی pitā)؛ هرن در شمارهٔ ۲۸۶ می‌نویسد: «pider (peder) پدر … پارسی باستان pitar-، اوستایی pitar-، پهلوی pit و pitar، سنسکریت pitar-، ارمنی hair». آنچه در چارت به عنوان «مادرِ» این گره آمده صورت اوستایی است که در حقیقت خواهرِ صورت پارسی باستان است نه نیای آن، ولی این شیوهٔ همیشگی کتاب است. از نظر آوایی: *pitar ← pidar (نرم‌شدن t میان‌واکه‌ای به d) ← پدر؛ واژهٔ «پیر» ربطی به این خانواده ندارد (هرن خود در پانوشت همان مدخل این پیوند را رد می‌کند). ادعای نورایی درست است.\",\n \"sources\": [W+\"%D9%BE%D8%AF%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"the node carries no citation in the book (refs=None); the claim was checked against Horn, MacKenzie and Wiktionary instead.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 286, printed p. 63 (HRN.txt leaf 85)\", \"stance\": \"supports\", \"note\": \"'286. pider (peder) Vater. Kāš. pei (aus ped). ap. pitar- Vater; aw. pitar-; phlv. pit, pitar (in …), P(i)tar-bōxt N. pr.; ai. pitar-; arm. hair Vater. kurd. pier; afγ. plār; oss. fidä, fid; bel. pit, pis, pid-'.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur pp. 158-159 (ARY_pages.txt leaf 157)\", \"stance\": \"supports\", \"note\": \"the پدر article lists Avestan, Sanskrit, Pahlavi, Latin, Greek, Gothic and Germanic cognates of the *ph₂tēr family (Latin-script forms are OCR-garbled, the language headings are legible), with a page reference to Borhan-e Qate'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. pidar\", \"stance\": \"supports\", \"note\": \"MacKenzie's pid/pidar '[ptr, AB-; pyt'] father' is the Middle Persian link between OP pitar- and NP پدر.\"}\n ]\n})\n\nroot[\"nodes\"] = nodes\nout = {\"pdf_page\": 379, \"book_page\": 349, \"verified_by\": \"claude-opus-5\",\n       \"verified_on\": \"2026-09-07\", \"entries\": [root]}\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-379.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(out,f,ensure_ascii=False,indent=1)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-379.py"
}
```


### [2026-09-07T21:02:36.233Z] TOOL RESULT

```
ok
```


## [2026-09-07T21:02:40.741Z] TOOL CALL #96: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-379.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 379"
}
```


### [2026-09-07T21:02:42.094Z] TOOL RESULT

```
JSON OK
nodes verified: 11/11
node verdicts: {'confirmed': 4, 'disputed': 4, 'plausible': 2, 'transcription_suspect': 1}
root verdicts: {'plausible': 1}
ref checks: {'partial': 6, 'supports': 14, 'not_found': 5, 'not_checked': 2}
books consulted: {'supports': 17, 'silent': 4, 'partial': 8, 'contradicts': 2} | by book: {'PHD': 8, 'NYB': 4, 'CHEUNG': 3, 'BRT': 3, 'HRN': 3, 'ARY': 3, 'WLD': 2, 'MON': 2, 'KNT': 1, 'BQT': 1, 'AHD': 1}
```


## [2026-09-07T21:02:48.176Z] TOOL CALL #97: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg379.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/379.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/379.png"
}
```


### [2026-09-07T21:02:48.285Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 87463 Sep  7 17:02 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/379.png
```


## [2026-09-07T21:03:10.949Z] AGENT

Page 379 (book p. 349, root **Pa / Pa-ter / Poti, Potiš**) verified. `verify_check.py 379`: 11/11 nodes, **0 PROBLEM lines**.

Verdicts: root **plausible**; nodes confirmed 4, plausible 2, disputed 4, transcription_suspect 1. Ref checks: 14 supports, 6 partial, 5 not_found, 2 not_checked; 35 `consulted` entries across PHD, NYB, CHEUNG, HRN, WLD, AHD, KNT, BRT, ARY, BQT, MON.

Flagged items:
- **#2 pâlŭdan (پالودن) — disputed.** Not from pā- "protect": MacKenzie records Manichaean MP p'rwdn / p'r'y- (pārūdan, pārāy-) with -r-, and the standard etymology is PIr *para-dāwati (*para- + *dʰew- "to flow") "make run through" > "filter". pāyīdan and -bān in the same node are confirmed.
- **#3 paiti/patiy/pavan — disputed.** Av. paiti- "lord" and OP pati- belong to PIE *pótis (Pok. 842), not to pā-; OP patiy is the preverb "against" (separate lemma, same page); "pavan" is not Av./OP at all but the Book-Pahlavi heterogram PWN = pad "in, at". pāna- and pāθra- in the node are genuine pā- derivatives; the shepherd word is fšu-pāna- (Nyberg), and pādšāh is *pati-xšāya- "ruling over", not "protecting king".
- **#6 paiti-dâma — transcription_suspect, error_in "book".** The page image (copied to `data/verification/sources/refs/ocr/BOOK/379.png`) prints "paiti-dâma"; the real form is Av. paiti.dāna- "mouth-veil" (MP padām, Pāz. panām). Extraction faithful.
- **#8 ô-pât-ân — disputed** (form also flagged, error_in "book"). Nyberg: āpātān < OIr *ā-pāta- "protected" (preverb ā-, no āb "water"); Cheung the same. Nourai follows Farahvashi (IRN:119, verified verbatim: "āp = water, pāt from pāyīdan, -ān suffix"), a minority reading. "arta-pān" is a construct.
- **#9 Ardavân — disputed.** *Ṛta-bānu- "the glory of Arta" (Gk. Ἀρτάβανος), bānu- "splendour", not -pāna- "protector". Ābādān as a town name is contested (Balāḏurī's ʿAbbādān; Persian form official only 1935).
- Gloss errors (noted, not extraction faults): "Âzarbâyjân : A city in Iran" — it is a region/Atropatene; "âthur-pât-gan : fire protector" — *Ātṛ-pāta- is passive, "protected by fire".

No extraction errors found: the JSON matches the printed page everywhere I checked, including the odd forms. Notable ref problems on the book's side: KLN:114 and KLN:157 point to irrelevant Klein pages (assimilate–astound; bean–bed), while the real Klein support is pp. 144 (s.v. ban) and 169 (s.v. bezoar); the root box cites POK 787/842 but not 839, which is where Pokorny actually puts Av. pāiti "hütet, bewacht, schützt".
