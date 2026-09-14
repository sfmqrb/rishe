# Verification process log — verify-page-431


## [2026-09-14T01:21:57.603Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 431 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-431.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-431.json. Write /home/sfmqrb/git/rishe/data/verification/page-431.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 431` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:21:58.684Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:21:59.450Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:21:59.465Z] TOOL RESULT

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


## [2026-09-14T01:21:59.960Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-431.txt"
}
```


### [2026-09-14T01:21:59.979Z] TOOL RESULT

```
1	=== PDF page 431 (book page 401) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Saus, Sus : dry  (refs POK:881)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:881; SOD:373; ETM:64 | hauš : to dry ; hauš-a, huška : dry
5	  #2 (parent #1) [Persian] refs=BQT:752; MON:1461; ETM:64 | xošk «خشک» : dry | extra: خشکیدن ، خوشیدن ، خشکیده ، خوشیده
6	  #3 (parent #1) [Sogdian] refs=SOD:373 | škw : dry
7	#4 (parent #0) [Old Persian] refs=KNT:178 | uška : dry
8	#5 (parent #0) [Greek] refs=AHD | austěros : harsh
9	  #6 (parent #5) [English] refs=None | austerity
10	--- entry 1 ---
11	ROOT [Avestan] Sav 1, Savah 1 : Sav 1: to benefit. Savah 1: welfare.  (refs HRN:166; NYB:181)
12	#1 (parent #0) [Pahlavi] refs=HRN:166 | sŭt : benefit, interest
13	  #2 (parent #1) [Persian] refs=HRN:166 | sŭd «سود» : interest, benefit, advantage | extra: سودمند
14	#3 (parent #0) [Sogdian] refs=SOD:366 | swt : interest, benefit
15	--- entry 2 ---
16	ROOT Savah 1 -> redirect to Sav 1
17	--- entry 3 ---
18	ROOT [Sanskrit] Šavala : (a fabric) marked with colors  (refs HJB:824)
19	#1 (parent #0) [Persian] refs=HJB:824; KLN:1432; MON:2000; FRS:171; BQT:1228 | šâl 1 «شال ۱» : scarf ; šâl 2, šâlang «شال ۲ ، شالنگ» : a thin rough and inexpensive rug | extra: شال کلاه | NOTE: KLN:1432 derives these from "Šaliat" an Indian town famous for its shawls
20	  #2 (parent #1) [Hindustani] refs=AHD:1192 | šawl : shawl | NOTE: Through Urdu language
21	    #3 (parent #2) [English] refs=AHD:1192; KLN; SKT | shawl
22	  #4 (parent #1) [Arabic] refs=BQT:1228; FVF:391 | šal : a rough rug or thick cloth
23	    #5 (parent #4) [French] refs=BQT:1228 | châle
24	
```


## [2026-09-14T01:22:03.482Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-431.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:8000])\n\"",
 "description": "Dump source JSON for page 431"
}
```


### [2026-09-14T01:22:04.560Z] TOOL RESULT

```
{
 "pdf_page": 431,
 "book_page": 401,
 "entries": [
  {
   "root": {
    "name": "Saus, Sus",
    "lang": "Indo-European",
    "refs": "POK:881",
    "gloss": "dry"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan / Old Persian",
     "refs": "POK:881; SOD:373; ETM:64",
     "words": [
      {
       "translit": "hauš",
       "gloss": "to dry",
       "script": null
      },
      {
       "translit": "hauš-a, huška",
       "gloss": "dry",
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
     "refs": "BQT:752; MON:1461; ETM:64",
     "words": [
      {
       "translit": "xošk",
       "gloss": "dry",
       "script": "خشک"
      }
     ],
     "script_extra": "خشکیدن ، خوشیدن ، خشکیده ، خوشیده",
     "note": null,
     "quote": {
      "text": "بخوشید سرچشمه های قدیم - نماند آب جز آب چشم یتیم",
      "poet": "Sa`dî"
     }
    },
    {
     "id": 3,
     "parent": 1,
     "lang": "Sogdian",
     "refs": "SOD:373",
     "words": [
      {
       "translit": "škw",
       "gloss": "dry",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 0,
     "lang": "Old Persian",
     "refs": "KNT:178",
     "words": [
      {
       "translit": "uška",
       "gloss": "dry",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 5,
     "parent": 0,
     "lang": "Greek",
     "refs": "AHD",
     "words": [
      {
       "translit": "austěros",
       "gloss": "harsh",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 6,
     "parent": 5,
     "lang": "English",
     "refs": null,
     "words": [
      {
       "translit": "austerity",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    }
   ]
  },
  {
   "root": {
    "name": "Sav 1, Savah 1",
    "lang": "Avestan",
    "refs": "HRN:166; NYB:181",
    "gloss": "Sav 1: to benefit. Savah 1: welfare."
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Pahlavi",
     "refs": "HRN:166",
     "words": [
      {
       "translit": "sŭt",
       "gloss": "benefit, interest",
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
     "refs": "HRN:166",
     "words": [
      {
       "translit": "sŭd",
       "gloss": "interest, benefit, advantage",
       "script": "سود"
      }
     ],
     "script_extra": "سودمند",
     "note": null,
     "quote": {
      "text": "خود را مپسند دلپسند همه باش - نقصان بپذیر و سودمند همه باش",
      "poet": "Khâqânî Shervânî"
     }
    },
    {
     "id": 3,
     "parent": 0,
     "lang": "Sogdian",
     "refs": "SOD:366",
     "words": [
      {
       "translit": "swt",
       "gloss": "interest, benefit",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    }
   ]
  },
  {
   "root": {
    "name": "Savah 1",
    "redirect": "Sav 1"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Šavala",
    "lang": "Sanskrit",
    "refs": "HJB:824",
    "gloss": "(a fabric) marked with colors"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Persian",
     "refs": "HJB:824; KLN:1432; MON:2000; FRS:171; BQT:1228",
     "words": [
      {
       "translit": "šâl 1",
       "gloss": "scarf",
       "script": "شال ۱"
      },
      {
       "translit": "šâl 2, šâlang",
       "gloss": "a thin rough and inexpensive rug",
       "script": "شال ۲ ، شالنگ"
      }
     ],
     "script_extra": "شال کلاه",
     "note": "KLN:1432 derives these from \"Šaliat\" an Indian town famous for its shawls",
     "quote": {
      "text": "زآن مثل حال من بگشت و بتافت - که کسی شال ۲ جُست و دیبا یافت",
      "poet": "Onsorî"
     }
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Hindustani",
     "refs": "AHD:1192",
     "words": [
      {
       "translit": "šawl",
       "gloss": "shawl",
       "script": null
      }
     ],
     "note": "Through Urdu language",
     "quote": null
    },
    {
     "id": 3,
     "parent": 2,
     "lang": "English",
     "refs": "AHD:1192; KLN; SKT",
     "words": [
      {
       "translit": "shawl",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 1,
     "lang": "Arabic",
     "refs": "BQT:1228; FVF:391",
     "words": [
      {
       "translit": "šal",
       "gloss": "a rough rug or thick cloth",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 5,
     "parent": 4,
     "lang": "French",
     "refs": "BQT:1228",
     "words": [
      {
       "translit": "châle",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    }
   ]
  }
 ]
}
```


## [2026-09-14T01:22:06.498Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SOD','ETM','BQT','MON','KNT','AHD','HRN','NYB','HJB','KLN','FRS','FVF','FVQ','SKT','WLD','PHD','IEC','SYN','BRT','HUB','ARY','AID','WEB','FSD','LKT','CHEUNG','PLA','AFM']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Show ref metadata"
}
```


### [2026-09-14T01:22:07.721Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_ety
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_p
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabeti
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
CHEUNG MISSING
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
```


## [2026-09-14T01:22:16.586Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80; echo ---; ls ocr 2>/dev/null | head -40",
 "description": "List local refs files"
}
```


### [2026-09-14T01:22:16.649Z] TOOL RESULT

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
AFM
ARY
BOOK
BQT
FFD
HRN
IRN
PLA
SNS
SOD
TAD
```


## [2026-09-14T01:22:17.358Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:22:17.433Z] TOOL RESULT

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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SBK.txt`

## Semitic / Arabic loans in either direction

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
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
- **TAD** — Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-huru
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt`
- **ARB** — al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edi
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt`
- **KFL** — Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KFL.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt`
- **LAM** — H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt`
- **DOZ** — R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeu
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt`
- **AKD** — H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt`
- **SIN** — B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt`
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
```


## [2026-09-14T01:22:21.040Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"saus-\" POK_full.txt | head -20; echo \"=== POK saus context ===\"; grep -n -m3 \"saus\" POK_03.txt | head",
 "description": "Grep Pokorny for saus-"
}
```


### [2026-09-14T01:22:21.106Z] TOOL RESULT

```
71439:Root / lemma: saus- sus- 
71446:dor, -term PIE. It seems that the Root/ lemma: saus- sus-: (dry) derived from Root/ 
=== POK saus context ===
973:baltoslav.  "^putä  , Vogel'  in  russ.-ksl.  pita  , Vogel',  p^t^§th  »kleiner  Vogel' (, Vogel'  eigentL  ,junger  Vogel'),  lit.  putytis  ,junges  Tier,  junger  Vogel' (Zärtlicbkeitsausdruck),  balt.  ^put-n-a-  in  lett.  putns  , Vogel*;  mit  anderer, demin.  Formansverbindung  lit.  paü-kstis  ,Vogel^
1036:p{h)u-s-:  ai.  püSyati,  pumäti,  pösati  .gedeiht,  macht  gedeihen,  wächst zu.  ernährt',  pustd-  .wohlgenährt,  reichlich',  pusti-y  pusti-  f.  .Gedeihen, Wachstum.  Fülle',  pösa-  ds..  puspa-m  ,Blume.  Blüte',  pushald-  .reichlich, prächtig,  in  voller  Lebenskraft';  gr.  cpvaa  .Blasen,  Blasebalg.  Blase' {*(ptaaa  oder  *pliüt-ia),  cpvadu  .blase,  blase  auf.  (fDoiaa)  .schnaube', cpvaiy^  f.  .Knoblauch,  Zwiebel'.  (pvaal(l)ig  f.  .Blase',  cpvaxa  f.  .Blase, Schwiele',  cpvayirj  f.  .Darm,  Wurst'.  cpvay,cüv  ,Dickbauch'.  7toi-(pvGöa)  .blase, schnaube';  lat.  pussula,  pustula  .Blase.  Bläschen.  Blatter';  norw.  feysa {*fausian)  .aufschwellen,  aufgähren'.  f{j)usa  .sausen,  mit  Gewalt  aus- strömen'; lit.püsU  ,Blase',  lett.  püslis  ds.,  lit.  pusnis^  pusnynas  , zusammen- gewehter Schneehaufe',  püse  (pü§e)  ,Blatter',  pü§kas  , Hitzbläschen  auf der  Haut',  lett.  puSJcis  .Blumenstrauß,  Bänderstrauß,  Büschel'  u.  dgl.;  aksl. *puchati  .blasen'  *opucJinpti  .anschwellen',  puchh  .cavus  (aufgedunsen)', russ.  pychdH  .keuchen.  Gluthitze  von  sich  geben*,  pychah  .aufgeblasen, hochmütig  sein',  pysnyj  .üppig,  aufgeblasen,  hochmütig*  usw.,  aksl.  napyUiti s^  ,sich  aufblasen',  russ.  pyscüh  ds.  (*pyskiti]  wohl  auch  öech.-poln.  usw. pysTc  ,Schnauze,  Maul  mit  dicken  Lippen');  vgl.  oben  S.  790  päuson-?
1523:saus-,  sus-  ,trocken,  dürr*;  sauso-,  sus-ko  ds.
```


## [2026-09-14T01:22:24.464Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re,json\nd=json.load(open('../refs_online.json'))\nfor k in ['POK','SOD','KNT','HRN','NYB','HJB','KLN','FRS','BQT','MON','BRT','PHD','AHD','IEC','SYN','WLD','SKT','FSD','WEB','AID','HUB','CHEUNG','LKT','TAD','AFM','PLA','FVQ']:\n    v=d.get(k) or {}\n    print(k,'|',v.get('page_offset'),'|',str(v.get('local_file'))[:120])\n\"",
 "description": "Show page offsets"
}
```


### [2026-09-14T01:22:25.612Z] TOOL RESULT

```
POK | POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
SOD | printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/source
KNT | leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt
HRN | leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
NYB | Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt
HJB | leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt
KLN | KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
FRS | different edition — no mapping | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/source
BQT | vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sou
MON | None | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/source
BRT | Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
PHD | leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt
AHD | 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
IEC | TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
SYN | leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
WLD | Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/source
SKT | leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
FSD | vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
WEB | not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt
AID | leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt
HUB | leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
CHEUNG | None | None
LKT | leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt
TAD | 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/source
AFM | 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/source
PLA | 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/d
FVQ | printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/source
```


## [2026-09-14T01:22:30.649Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=1520 && NR<=1535' POK_03.txt; echo \"=== leaf number ===\"; python3 -c \"\nt=open('POK_03.txt',encoding='utf8',errors='replace').read()\ni=t.find('saus-,  sus-')\nprint('leaf', t[:i].count('\\f'))\n\"",
 "description": "Read Pokorny saus- entry"
}
```


## [2026-09-14T01:22:31.591Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '71430,71470p' POK_full.txt",
 "description": "Pokorny db entry saus-"
}
```


### [2026-09-14T01:22:31.737Z] TOOL RESULT

```
Ai.  sasyd-  n.  , Feldfrucht* ;  jav.  hahya-  , Getreide*;  gall.  Akk.  {s)as{am jRoggen*  (,secale  Taurini  sub  Alpibus  asiam  vocant*  Plin.  H.  N.);  cymr. haidd  ,hordeum*,  bret.  heiz  ,orge';  vgl.  auch  ved.  sasd-  ,Nahrung,  Speise, Kraut,  Gras,  Saatfeld*.  r-
WP.  II  454,  WH.  I  72.
sä-ti-  s.  sä-.  r
saus-,  sus-  ,trocken,  dürr*;  sauso-,  sus-ko  ds.
Ai.  süsyati  , trocknet,  welkt*,  danach  sosa-  m.  (assimil.   aus  *sosa-)  ,das
881'
;\.ustrockiien',  auch  Adj.  ,trocken  machend*;  av.  haos-  ,exarescere*,  aidhao- '^gTuna-  ,nicht  trocknend*;  ai.  süska-  (aus  ^^suska-),  av.  huska-  , trocken*;
gr.  avoq  (Hom.),  alog  (att.)  ,dürr,  trocken*,  aiaraXeog  ,struppig,  schmut- zig', avarrjQÖg  ,herb,  streng';  Denomin.  avaivu),  avaivu)  ,mache  trocken, dorj-e*,  aijw  ,trockne,  dörre*;  unsicher  gr.  aijx(^ög  m.  ,Dürre,  Trockenheit, Schmutz*,  falls  aus  *sau-k-smo-  von  einer  Wurzelvariante  *sau-k-  neben *sau-s-,  zu  ai.  süksma-  ,fein,  dünn,  schmal*  ?
alb.  thanj  {*sausnio)  , trockne* ;
lat.  südus  ,trocken,   heiter'   {*suz-do-),   südum   ,der  klare   Himmelsraum heiteres  Wetter';  anders  M.  Mayrhofer  KZ.  73,  117;
ags.    sear,    mnd.   sör  ,trocken',  norw.   seyr  ds.,   ahd.   sören  ,verdorren*;
\it.  saüsas  , trocken*,  saüsti  ,trocken  werden*,  saüsinti  , trocken  machen*, süsti  , räudig  werden*,  süshis  ^Aussatz,  Krätze*  (:  ai.  §üska-)]  lett.  s«s^ .trocken  werden';  aksl.  sucH  ,trocken*,  siiHti  ,trocken  machen*,  s^chngti jtrocken  werden*.
WP.  II  447,  WH.  II  624,  Trautmann  250  f:,  Frisk  188 f.,  192f.
säuel-,  säuol-,  suuel-,   suel-,  sQl-   , Sonne*,  woneben  suen-,   sun-,  also alter  Z/n-Stamm;   siiel-  , schwelen,   brennen*  ist  wohl   damit  identisch.
1.  Ai.  ved.  süvar  n.  =  av.  hvard  , Sonne,  Licht,  Himmel*,  Gen.  sürah ==  jav.  hüröy  ai.  sürya-  (*sülnO')  m.  (vgl.  gr.  fjlLog),  süra-  m.  , Sonne*; davon  ai.  sürta-  ,hell',  ai.  svdrnara-  m.  ,Lichtraum,  Äther*,  av.  x'^ardnah-j ap.  -farnah-  ,Ruhmesglanz,  Herrlichkeit* ;
gr.  hom.  ^sXiogj  att.  fjhog,  dor.  dehog,  äXiog,  kret.  äßshog  Hes.  (d.  i. afeXiog)  , Sonne',  Weiterbildung  des  n.  *sauel  zum  m.  -lo-St.  {y^\.  ai.  sür- ya-)'^  lat.  söl,  -is  m.  ,Sonne*  (aus  neutr.  *säuel  über  *säuol,  *säol)]  cymr. haulj  acorn.  heuulj  mcorn.  heul,  houl,  bret.  heol  , Sonne*  (*säuel-) ;  dazu air.  Süll  f.  ,Auge'  aus  *süli-j  ablautgleich  mit  ai.  sürah,  und  alb.  hiil,  ül , Stern*  (*sülO'  oder  *süU-)',
=== leaf number ===
leaf 115
```


### [2026-09-14T01:22:31.789Z] TOOL RESULT

```
bret. he/z^orge'; compare also ved. sasa- "nourishment, food, dish, food, herb, grass, 

sown field '. 

References: WP. II 454, WH. I 72. 

Page(s): 880 

Root / lemma: saus- sus- 
Meaning: dry 

Note: 

The real root was *sa-, su-'dry' which was suffixed either with common -ska or -tra, -dra, - 

dor, -term PIE. It seems that the Root/ lemma: saus- sus-: (dry) derived from Root/ 

lemma: sauel- sauol- suuel- suel- sul-\ (sun). 

Material: Old Indie susyati^ dries, wilts ', thereafter sosa-m. (assimil. from *sosa-) "the 

drying up', also Adj. " made dry '; Avestan haos-^ dry up, become dry ', arjhao-samna-^uoX 

drying '; Old Indie suska- {iroru *suska-), Avestan huska-^dry'; 



gr. auo(; (Horn.), auoq (Attic) "arid, dry', avoiaktoq " scrubby, dirty, fiitliy', auaTr|p6(; " 
harsh, austere '; Denomin. auaivw, auaivu) 'make dry, desiccate ', auw 'trockne, desiccate 
'; doubtful gr. auxM6(; m. " aridity, dryness, smut', whether from *sau-k-smo- irom a root 
variant *s5^-/r- besides *sau-s-, to Old Indie suksma-l\v\e, thin, narrow, tight, slim, 
slender, thin '? common Old Indie -gh- > -ks- 

alb. thanj{ *sausnid) ' dry '; 

Note: 

Common alb. s > th 

Latin sudus^dry, cheerful' {*suz-do-), sudum^ cloudless, bright, clear, serene '; different
```


## [2026-09-14T01:22:39.308Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"saus-\" AHD_watkins1985.txt | head; echo \"=== austere ===\"; grep -n -i \"auster\" AHD_watkins1985.txt | head",
 "description": "Watkins saus-"
}
```


### [2026-09-14T01:22:39.377Z] TOOL RESULT

```
904:saus-. Dry. 1. Extended form *sauso- in Germanic *sau- saz in: a. Old English séar, withered: SEAR!, SERE!; b. Frankish *saur, dry, whence Old French saur, sor, red-brown: SORREL?; SURMULLET. 2. Suffixed form *saus-t- in Greek austéros, harsh: AUSTERE. [Pok. saus- 880.]
1270:AUSPICE awi-, spek- AUSTERE saus- AUTACOID y@k- AUTARCHY arkhein AUTARKY arek- AUTHOR aug-! AUTHORIZE aug-! AUTOBAHN g*hen-* AUTOCHTHON dhghem- AUTOECIOUS weik-1 AUTOGIRO géu- AUTOMATIC men-1 AUTONOMOUS nem-
2225:SCHISM skei- SCHIST skei- SCHIZO-  skei- SCHIZONT es- SCHLEP |leij- SCHLIEREN sleu- SCHLOCK | slak- SCHMALTZ mel-1 SCHMEER (s)mer-3 SCHMUCK meug-2 SCHNAUZER snu- SCHNITZEL sneit- SCHNORRER sner- SCHNOZZLE snu- SCHOLAR segh- SCHOLASTIC segh- SCHOLIUM segh- SCHOOL! segh- SCHOOL? §skel-1 SCHUss skeud- SCIENCE skei- SCILICET skei- SCINTILLA skeei- SCINTILLATE skeei- SCIOLISM skei- SCION géi-1 SCIRE FACIAS dhé-1, skei- SCISSION  skei- SCISSORS kae-id- SCLERA skele- SCLERO- skele- SCLEROMA §skela- SCLEROSIS skela- SCLEROTIC skelo- SCLEROTIUM skela- SCLEROTIZATION skela- SCLEROUS skelo- SCOFF skeubh- SCOLD sekw-3 SCOLEX skel-3 SCOLIOSIS skel-3 SCONCE? dhé-1 SCONE keu-! SCOOP skep- Scop skeubh- -SCOPE spek- -SCOPY spek- SCORCH skerbh- SCORE sker-1 SCORIA_ sker-4 scoT skeud- SCOT AND LOT skeud- SCOTOMA  skot- SCOUR! cira SCOUR2 kéwero- SCOURGE reig-1 SCOUT! ous- scouT? skeud- SCRABBLE  sker-! SCRAG gWere-4 SCRAP!  sker-1 SCRAPE sker-1 SCRATCH grat- SCREAK ker-2 SCREAM ker-2 SCREECH ker-2 SCREED skreu- SCREEN sker-1 SCREW sker-! SCRIBBLE skribh- SCRIBE skribh- SCRIMP_ skerbh- SCRIPT skribh- SCRIPTORIUM skribh- ScRIPTURE  skribh- SCROBICULATE sker-1 SCROD skreu- SCROFULA  sker-1 SCROLL skreu- SCROTUM skreu- SCRUB!  sker-1 SCRUTINY skreu- SCUDO skei- SCUFF skeubh- SCUFFLE! skeubh- SCUFFLE? skeubh- SCULPTURE skel-1 SCUM (s)keu- SCUTCH kwét- SCUTTLE! skeud- SCUTUM  skei- SCYPHISTOMA skep-, ste-men- SCYPHOZOAN skep- SCYTHE sek- SEAL! sekw-1 SEAL? selk- SEAM syi- SEANCE sed-! SEAR! saus-
2249:SEQUESTRUM sekw-1 SERAC ser-2 SERE! saus- SERENE ksero- SERF servus SERGEANT servus SERIES ser-3 SERIF skribh- SERIOUS swer-5 SERMON ser-3 SEROTINOUS sé@-2 SERPENT serp-2 SERPIGO serp-2 SERRIED ser-3 SERTULARIAN ser-3 SERUM ser-2 SERVAL_ ker-! SERVE servus SERVICE servus SERVILE servus SERVITUDE servus SESQUI- kwe, sémi- SESQUIPEDALIAN ped-! SESSILE sed-1 SESSION sed-1 SESTERCE sémi-, trei- SESTET s(w)eks SESTINA s(w)eks SET! sed-1 SETTLE sed-1 SEVEN septm SEVER pere-! SEVERAL pere-1 SEVERE WEér0- SEW syu-
2277:SOP seue-2 SOPOR swep-1 SOPORIFIC swep-1 SOPRANINO uper SOPRANO uper SORCERER ser-3 SORDID swordo- SORDINO swer-2 SORE sai- SORITES teue- SORORAL swesor- SORORITY swesor- SORREL! siiro- SORREL? saus- SORROW swergh- SORRY Sai- SORT ser-3 SORTILEGE leg-1, ser-3 SORUS teue- SOTERIOLOGY teue- SOUBRETTE uper SOUFFLE bhlé-2 SOUGH (s)wagh- SOUND! swen- SOUND2 swento- SOUND3 swem- SOUND4 swem- SOUP seue-2 sOUR siiro- SOURDINE swer-2 SOUSE sal-1 SOUTANE upo SOUTH sawel- SOUTHERN sawel- SOUVENIR gWa- SOVEREIGN uper SOVIET sem-! sow! sé-1
2328:SURE cilra, s(w)e- SURFACE dhé-1 SURFEIT dhé-1 SURGE reg-! SURGEON ghesor- SURGERY ghesor-, werg- SURLY sen-1 SURMISE (s)meit(9)- SURMULLET mel-2, saus- SURPLICE pel-4 SURPLUS pele-' SURPRISE ghend- SURRENDER d6- SURREPTITIOUS rep- SURROUND wed-! SURVEILLANT weg-2 SURVEY weid- SURVIVE gWei- SUSCEPTIBLE kap- SUSPECT spek- SUSPEND (s)pen- SUSPIRE spirare SUSTAIN ten- SUSURRATION swer-2 SUTLER seut- SUTRA syil- SUTTEE e@8- SUTURE syu- SVELTE wel-4 SWAB swep-2 SWAG sweng(W)- SWAIN s(w)e- SWALE swel-2 SWALLOW! swel-1 SWAMI s(w)e- SWAMP swombho- SWAN swen- SWANK sweng(w)- swaP swei-2 SWARF swerbh- SWARM swer-2 SWART swordo- SWASTIKA @S-, SU- SWEAR swer-1 SWEAT sweid-2 SWEET swad- SWELTER swel-2 SWERVE swerbh- SWIFT swei-2 SWILL swel-!
=== austere ===
321:yawn, gape: BAY2, BEVEL; ABASH, ABEYANCE. 2. Possibly Vulgar Latin *abbaidre (> Old French (a)baiier), to bay: BAY‘*.] [battuere. To beat. Latin verb of unknown origin. (BATE?), BATTER!, (BATTER’), (BATTERY), BATTLE; ABATE, COMBAT, DEBATE, (RABBET), (REBATE?), (RE- BATO).] bel-. Strong. 1. Suffixed o-grade form *bol-iyo- in Russian bol’shoi, large: BOLSHEVIK. 2. Prefixed form *dé-bel-i- (dé-, privative prefix; see de-), “without strength,” in Latin débilis, weak: DEBILITATE, DEBILITY. [Pok. 2. bel- 96.] bend-. Protruding point. 1. Germanic *pannja-, “struc- ture of stakes,” in Old English penn, pen for cattle: PEN2. 2. Germanic *pund- possibly in Old English pund- (> Middle English pound), pundfald, enclosure for stray animals: POND, POUND3; IMPOUND, PINFOLD. 3. Germanic *pin- in Old English pintel, penis: PINTLE. [Pok. bend- 96.) beu-'. Also bheu-. Appears in words loosely associated with the notion “to swell.” I. Root form *beu-. 1. Ger- manic *puk- in: a. Old English pocc, pustule: POCK; b. Old French po(u)che and Old North French poke, bag: POACH!, POCKET, POKE3, POUCH, (PUCKER). 2. Old Eng- lish pyffan, to blow out: puFF. 3. Old English -piite, “fish with large head” (in aele-piite, eelpout): pouT?. II. Root form *bheu- with various Germanic derivatives. 1. Old English bdsm, bosom: Bosom. 2. Old English biic, belly, pitcher: BUCKBOARD. 3. Frankish *biak (> Old French buc), trunk of the body: TREBUCHET. 4. Old English bye), pustule: BorL?. 5. German dialectal baustern, to swell, akin to the source of Middle English bost, a bragging: BoasT!. III. Root form *beu-. 1. Latin bulla, bubble, round object, amulet (> Old French boule and Spanish bola, ball): BILL!, BILLET!, BOLA, BOULE?, BOWL’, (BULL?2), BULLA, BULLATE, BULLET, (BULLETIN); BOULE- VERSEMENT. 2. Latin bullire (> French bouiller), to bubble, boil: BOIL!, BOUILLON, BUDGE!, (BULLION), BULLY?; BOUILLABAISSE, EBULLIENCE, GARBOIL, PAR- BOIL. 3. Possibly Latin bucca (> Old French boucle, buckle, curl, and Spanish boca, mouth), (inflated) cheek: BOCACCIO, BOUCLE, BUCCAL, BUCKLE!, BUCKLE?; DE- BOUCH, DISEMBOGUE, EMBOUCHURE. 4. Greek boubén, groin, swollen gland: BUBO. [Pok. 2. beu- 98.] beu-2. Root imitative of muffled sounds. 1. Latin bitié (perhaps > Old French butor), bittern: BITTERN!. 2. Latin bited, a kind of hawk: BUZZARD. [Pok. 1. b(e)u- 97.] bha-'. To shine. Contracted from *bhas-. 1. Germanic *baukna-, beacon, signal, in: a. Old English béac(e)n, beacon: BEACON; b. Old English denominative bécnan, biecnan, to make a sign, beckon: BECKON. 2. Perhaps Germanic *bazja-, berry (< “bright-colored fruit”), in Old English berie, berige, berry: BERRY. 3. Germanic *bandwa-, “identifying sign,” banner, standard, sash, also “company united under a (particular) banner,” in: a. Spanish banda, sash: BANDOLEER; b. Late Latin ban- dum, banner, standard: BANNER, (BANNERET). 4. Suf- fixed form *bhaw-es- in Greek phds (stem phét-), light: PHOS-, PHOT, PHOTO-; PHOSPHORUS. 5. Extended and suffixed form *bhan-yo- in Greek phainein, “to bring to light,” cause to appear, show, and phainesthai (passive), “to be brought to light,” appear: FANTASY, (PANT), PHANTASM, (PHANTOM), PHASE, PHENO-, PHENOMENON; DIAPHANOUS, EMPHASIS, EPIPHANY, HIEROPHANT, PHAN- EROGAM, (PHANTASMAGORIA), PHOSPHENE, SYCOPHANT, THEOPHANY, (TIFFANY). [Pok. 1 bha@- 104.] bha-2. To speak. Contracted from *bhaa-. 1. Latin fari, to speak: FATE; AFFABLE, (FANTOCCINI), INEFFABLE, IN- FANT, (INFANTRY), PREFACE. 2. Greek phanai, to speak: -PHASIA; PROPHET. 3. Suffixed form in Germanic *ban- wan, *bannan, to speak publicly (used of particular kinds of proclamation in feudal or prefeudal custom; “to proclaim under penalty, summon to the levy, declare
904:saus-. Dry. 1. Extended form *sauso- in Germanic *sau- saz in: a. Old English séar, withered: SEAR!, SERE!; b. Frankish *saur, dry, whence Old French saur, sor, red-brown: SORREL?; SURMULLET. 2. Suffixed form *saus-t- in Greek austéros, harsh: AUSTERE. [Pok. saus- 880.]
1270:AUSPICE awi-, spek- AUSTERE saus- AUTACOID y@k- AUTARCHY arkhein AUTARKY arek- AUTHOR aug-! AUTHORIZE aug-! AUTOBAHN g*hen-* AUTOCHTHON dhghem- AUTOECIOUS weik-1 AUTOGIRO géu- AUTOMATIC men-1 AUTONOMOUS nem-
```


## [2026-09-14T01:22:40.933Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ===\"; grep -n \"saus\" IEC.txt | head -20; echo \"=== SYN dry ===\"; grep -n -i \"sausas\" SYN.txt | head -10",
 "description": "Mann and Buck for saus-"
}
```


### [2026-09-14T01:22:41.022Z] TOOL RESULT

```
=== IEC ===
4436:grpis, os (?) 'slough, skin, gut, pipe” Hes. grápis ‘slough of snake’; Sw. korv 'saus- age” (?).
5320:guotolos, guotilos ‘bulge, swelling". Lat. botulus ‘sausage’, beside botellus, id.; OHG chwadilla, quedilla ‘pustule, papule’
14308:qusauió (qusausió) ‘touch, strike’. (Gk. am- big.) Gk. (ambig.) psaüo, v. ‘touch; reach; hit — a target; Li. Sauju, šauti “shoot, fire’; Latv. Sauju, Saut “buffet; shoot. Variant in OCS xušọ, xusiti, v. ‘plunder’; po-xu&o, -xusiti, v. ‘tear up, shred'; xusa, f. ‘ambush’; Slovene hüsati, v. ‘sweep’ (here? or isophone?)
15033:sausos ‘dry, withered, mature’; sausið ‘dry, wither, mature’; sausiə ‘dryness, dry land, dried object’. WP II, 447 Skt. (variant) Sosah, adj. ‘dry’; Av. cf. hao- Səmna-, pres. pass. pt, id.; OP cf. huška-, dim. id.; Per. xušk, id.; Gk. aüos, adj. id.; aúð, v. ‘parch’; aa f. (‘dry land’: OCS suša, Cz. souš, gs: souše, id.; Li. saüse, f. (2) ‘dried- out tree’); Br. (?) haw, adj. ‘ripe’; Sicilian cf. (variant) saukos ‘dry’ (Desk: MHG sor, OE sear, siere, LG & WG sohr, Du. zoor, adj. ‘dry, barren, arid, withered, sear’; ON seyra, f. (famine’: Gk. aa OCS suša: Li. sausē); OCS (and com. Sl.) suxü, adj. ‘dry’; Li. sausas, Latv. sauss, id. Verbal types: cf. Skt. susyami, pp: Sositáh ‘get dry’; Gk. auo, id.; OE sēarian, id.; LG soren; OCS and com. Sl. sušọ, -iti, ‘dry’; Li. cf. saustü, saüsti, id.; Latv. sauseju, ét, tr. intr. ‘dry’
15283:seus-, seuser- (?) ‘vermin’ OHG siurra, siura, wf. & siuro, wm. ‘tick, mite’; Du. zier, f. id. (and ‘bit, scrap’); R cf. šušera, f. ‘rabble’; Li. cf. sause, f. ‘grub’; Latv. cf. šaušalas, fpl. ‘revulsion’
15316:Sousos, see sausos
17855:sus ‘dry’. Cf. sausos, susó OCS cf. sos f. 'brushwood', fr. *susio; süx- nọ, -noti, v. ‘get dry’; Latv. susu, et, v. ‘dry’; Av. hu$- (radical), id.
17869:susó, ið ‘go dry, wither, be dry’. Cf. sus-, saus- Skt. cf. (variant initial) $usyami, intr. id.; OCS süxng, -noti, v. id. (and com. Sl.) b ide süxlí, f. ‘dry branches’; Li. sunsü, süsti, v. ‘flake off" beside susas, m. ‘scab’. Cf. Av. hus-, v. ‘dry’ in ppp. haoSomna-, id.
17871:susur- (susurs-, surs-) ‘whisper, squeak’. Onomat. WP II, 527. Var: saus(r)- Arm. cf. krking, s. ‘murmur, gossip’; krkngam, v. id. (fr. *sursunjo, via *sursunujó); Gk. cf. húron, n. ‘swarm of bees’; hürax, m. 'shrew- mouse’; Lat. susurrus, adj. & s. ‘whispering; whisper’ beside sorex (‘shrew’, if fr. *sausr-); G surren, v. “hum? beside såuseln, v. ‘whisper’; Latv. susurs, m. ‘grey shrew’; cf. (*-au- in) Hes. sausarós, adj. ‘whispering’; R surók, m. *marmot
18560:touom- 'firm, hard; firmness, hardness' Gk. sóma, gs: -atos, n. ‘corpse; body”; Lat. cf. tomaculum; tomentum, n. (lit. *'stuffing', hence (1) ‘sausage’; (2) *upholstery")
19256:tük- (2) “plug, cram, force’. WP I, 711. (Gmc. types ambig. cf. tüqu-) Lat. cf. tüc-etum, n. “forcemeat, sausage’; fis- tüca, f. (rammer, piledriver. Ambig. cf. stúk-?); OHG dühan E dühen, diuhen, wv. "thrust, press, squeeze’; OE pyan & pywan, wv. id.; Du. duwen, id.; OCS tüko, tükati, v. (1) ‘push’; Arm. cf. variant tkrim, v. (stuff, cram’, fr. *tukurio). Long-grade in OCS po-tykati, -tykajo, v. ‘press’; Cz. tyč, m. ('stick', ambig. (1) or (2), fr. *tükjo-. Dim. type in OCS and com. Sl. tüc-ka, f. *dot^)
=== SYN dry ===
801:ce. The solid surface of the earth in contrast with that which is covered with water, now regularly land. This sense is in some languages commonly ex- pressed more specifically as ‘dry (land)’, as Byz., NG émpa, Rum. uscat (fr. adj. uscat ‘dry’), Lith. sauszemis (sausas ‘dry’ and Zeme).
1136:5. Lith. sauszemis, cpd. of sausas ‘dry’ and Zemé ‘land’.
27220:15.84 DRY Grk, Enpbs, ad i NG y aos Goth. paursus Lith. sausas Lat, fenés, oreyvbs ON purr Lett. sauss I, “us, Gridus Dan. gr ChSl.  suchit th tea, ascrutto (arido) Sw. torr SCr. suh Sp, Ee (aride) OE = drgge, pyrre, séar Boh.  suchy Rum, et Budo ME  drie, sere Pol. —suchy Ir, peal Sec NE dry Russ. suchoj Nir, tintin Du. droog Skt.  cuska- uf na. OHG — durri, trucchan Av. huSka-, hiku-, hiSku- Br, Bech, rg MHG _ trucken, dtirre
27228:Grk. (Hom.) aios, Att. atos; OE séar, ME (NE) sere (esp. ‘withered’), MLG sor; Lith. sausas, Lett. sauss, ChSI. sucht, etc., general Balto-Slavic; Skt. cuska- (for *sus-ka-), Av. huska-, OPers. uska-.
```


## [2026-09-14T01:22:49.613Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"huška\" BRT.txt | head -20; echo \"=== haoš ===\"; grep -n \"haoš\\|haos-\\|hu§ka\\|huska\" BRT.txt | head -20",
 "description": "Bartholomae huška/haoš"
}
```


### [2026-09-14T01:22:49.715Z] TOOL RESULT

```
=== haoš ===
4127:|(ADf.)  äpa  urvaire  Y.5.4;  Yt  79.32. *kaasimna-,  PPM.  lu  *haosa;  Praes.  2.  —  Vgl aL  iüfyati  'er  vertrocknet',  np.  sSüdan  'ver- dorrt sein',  gr.  aIo(.  —  Vgl.  huska-.  —  Pü. : undeutl.,  dazu  die  Erl.:  an  i  ne  afiäyojl  Ausk ne  Ausi;  SQ. :  aSaft.  —  »  Zu  Yt.  1$.  16  fälsch- lich aai/iis',  s.  S  26S.  57.
13235:—  tairlm  gäma  (sd.)  frabarat  .  .  urva anayragiva  raocöAva  mdarjät  H.  2. 1 5 ;  1 5^, 33;  vgl.  f;  —  yavat  .  .  kangmrvayqn altavat  . .  Au/ie  (sd.)  zpme  nidaiiyan  V. ''■  29;  31;  —  Ja/W  (sd.)  . .  WM?  nihaite (NDf.)^'>  V.7.45;  49;  —  taohri  ..  ta Als  dasva  garS  nmätu  Yt.  /0. 3  2 ;  —  at  Asi vaAmSng  dfmäTig  garS  (sd.)  nidämä  Y. 45-  8;  —  mi^ma  . .  yaAmt  vyäne  (sd.)  . . masfl  amava  niiälim  Yt./o.64.  b)  wo?- Adverb:  kva  narqm  iristanqtn  tanom  ba- räma..kva  nidäiiäma  V.6'.44;  —  astala . .  tanüm  nidai^yan  V.5, 12;  —  daxma  . . yaAmya  narö  irista  tmayeinte  V,^.  9;  • — an'öpäo  m  nidaiaite^  a/is  .  .  *aniar?.- ar^i^m  nmSnoAe  Yt  iS.  4.  c)  Instr. : Aiiu  pqsnu  (sd.)  gitu  niaayaila  V.  16. 2.  d)T>3X.:  ai^ä  aAmäi  varmüi  ..nidä- tfttt  ahm  süiäyäi  tkalsäi  (sd.)  rSiayeAAf druxSY.4S-Z''  —  amtmca  Vfr^^rayti^mca ni'jät>m  tanuye  Yt  14.  38.  e)  Gen.: huskanqm  (näml.  alsmanqia,  als  Obj.)  . airiAa  S3ms  (sd.)  niäaÜyqn  V.  7.  29;  — aSa^qm:a  (näml.  Aaoliianqm,  als  Obj.) zftitö  nidaiiyqn  antarfin  ar?wtn  nmänaAe V.  6".  43;  -—  äat  vohu  maiiB  nidatoTi.. raocaukiim  yat  Ae  stärqm  aiwi.raocayantt "dann  sollst  du  (ihn)  .  .  dem  Licht  aus- setzen, damit  . ."  V. /^.  23.  f)/(7jÄund Lok. :  paoirim  gäma  (sd.)  frabarat . .  urva Attmate  paiü  nidaläl  H.  2.  15;  15';  vgl.  a,
18556:•  j.  napta-  Adj.  'feucht':  altavat  huskatiam alsmanqm  aztavat  "ianqm  V,  7.  31;  29,  30, 33.  34;  —  kuskanqm  yavanqm  .  .  'tanan V.7.35.
30531:PPfP.  lum  V.  haos-i-).  —  PÖ.:  huik.  —  ')  Die Bildung  ist  ungewöhnlich.  Sie  scheint  ein Praei.  3  huia-  varäusiuseticn;  s.  Sp.  501  No.  d,
```


## [2026-09-14T01:22:50.643Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"uška\" KNT.txt | head -20",
 "description": "Kent uška"
}
```


### [2026-09-14T01:22:50.699Z] TOOL RESULT

```
923:*susko-, OP *uška-, Skt. $ügka-, Lith. satisa-s
1438:Saka-, Sug(u)da-, Nisdya-, si*kabru-, and the 3 dubious siyamam. 3 5117. рів. f from pIE s after certain sounds 1 (8115) remained unchanged in OP: у ОР тав: Ма- ‘greatest’, Av. masisla-, Gk. шікито 5 "longest". : OP fràisayam ‘I sent’, Skt. ejayat? ‘he brings’, OP uška- ‘dry’, Av. huska-, Lith. satisa-s. OP gausa- ‘ear’, Skt. ghóga- ‘noise’. 4 OP adarínaus ‘he dared’, Skt. dhysnéti ‘he dares’. 4 OP aría- ‘male’ in ArSama- ‘Arsames’, Skt. 4 rsa-bhd- ‘bull’. 4 pIE *sed-as- in ОР Лай ‘seat’, cf. СК. &os (from -$ pIE *sedos). 4 pIE *e-st-sfe-to, OP ачЧаіа ‘he stood’, cf. Gk. : israrat ‘he stands’ (from *sestatat). 4 pIE *rsti-, OP nom. arštiš, Skt. rstf-s (cf. $115). 4 OP nom. tani ‘body’, Skt. tani-s. 4 For ks and other clusters giving zš, see $102; 4 for kn and gn giving initial тп and medial im, 4 $06; for -Sc- as a sandhi product, $105; for pAr. 4 & giving OP Sy, $104; for pAr. t giving OP y 4 $80; for pAr. én giving OP $n, $82. 1 The verbal prefix ni- affects an initial s of the 4 verbal root; thus ni-$d- from ni- + stä- and 4
2037:Gen. Sg. martiyahyā, xSdyabiyahyd, kdrahya, Pār- sahyd, visahyd, probably máhyà; nt. uškahyā, uvaipasiyahyd, jiwahyd, [ha]kartahyā.
5224:uška- adj. ‘dry’; nt. as sb., ‘land, mainland’: Av. hu&ka- ‘dry’, NPers. zusk, Skt. $ügka-, Sisyatt ‘dries’, Lith. saüsa-s ‘dry’, NEng. sere, sear ($146.1). uškahyā gsn. DPe 13.
```


## [2026-09-14T01:22:55.275Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KNT.txt',encoding='utf8',errors='replace').read()\ni=t.find(\\\"uška- adj. 'dry'\\\")\nleaf=t[:i].count('\\f')\nprint('leaf',leaf,'-> printed approx',leaf-15)\nprint(t[i-200:i+400])\n\"",
 "description": "Kent uška leaf/page"
}
```


### [2026-09-14T01:22:56.399Z] TOOL RESULT

```
leaf 231 -> printed approx 216
```


## [2026-09-14T01:22:56.898Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"austere\" KLN_1966.txt | head -5; echo \"=== SKT austere ===\"; grep -n -i \"austere\" SKT.txt | head -5",
 "description": "Klein/Skeat austere"
}
```


### [2026-09-14T01:22:57.093Z] TOOL RESULT

```
3589:ascetic,  adj.,  self-denying,  austere.  —  Gk.  Aa- xt)tix6<;,  ‘practiced,  laborious,  athletic’,  fr. acrxT)T7)<;,  ‘one  who  practices  any  art  or  trade’, fr.  aoxelv,  ‘to  form  by  art,  to  practice  gym¬ nastics,  to  practice,  exercise’,  which  is  of  un¬ certain  origin.  The  word  ascetic  was  introduced into  English  by  Sir  Thomas  Brown  (1663-1704). Derivatives:  ascetic,  n.,  ascetic-al-ly,  adv.,  as¬ cetic-ism,  n.
3696:Derivative:  assessor- ial ,  adj. assets,  n.  —  Orig.  a  singular  noun  fr.  OF.  asez (pronounced  asets)  (whence  F.  assez),  ‘enough’, fr.  VL.  *ad-satis,  ‘in  sufficiency’,  fr.  L.  ad,  ‘to’  (see ad-),  and  satis,  ‘enough’.  Cp.  O Proven?,  assatz, ‘enough’,  It.  assai,  ‘much’,  which  also  derive  fr. VL.  *ad-satis,  and  see  satis,  sad. asseverate,  tr.  v.,  to  affirm.  —  L.  asseveratus,  pp. of  asseverare,  ‘to  act  with  earnestness,  to  assert strongly’  (said  of  speech),  fr.  ad-  and  severus, ‘serious,  grave,  strict,  austere’.  See  severe  and cp.  persevere.
3927:auantic,  adj.,  atrophic.  —  Formed  with  suff.  -ic fr.  Gk.  xuavTTj,  ‘a  wasting,  atrophy’,  fr.  auaE- veiv,  ‘to  wither,  be  dry’,  fr.  a\kiv,  ‘to  dry’,  fr. cchoq,  ‘dry’,  which  stands  for  *saitso-s  and  de¬ rives  fr.  I.-E.  base  *saus-,  *sus-,  ‘dry’,  whence also  OE.  sear,  ‘dry’,  OHG.  soren,  ‘to  become dry’.  See  sere,  adj.,  and  cp.  austere, aubade,  n.,  morning  serenade.  —  F.,  fr.  Proven?. aubado,  fr.  auba,  ‘dawn’,  fr.  L.  alba,  fem.  of albus,  ‘white’,  used  as  a  noun.  See  alb  and  -ade. aubain,  n.,  alien,  foreigner.  —  F.,  orig.  written aubene,  fr.  Frankish  *aliban,  lit.  ‘belonging  to another  ban’.  The  first  dement  of  this  w'ord  is rel.  to  Goth,  aljis,  ‘other’,  and  to  E.  else  (q.v.) The  second  element  is  rel.  to  E.  ban,  v.  (q.v.) See  Bloch-Wartburg,  DELF.,  p.43  s.v.  aubain. aubergine,  n.,  the  eggplant.  —  G.,  fr.  Catal.  al- berginera,  alberginia,  fr.  Arab,  al-badinjan,  ‘the eggplant’,  fr.  al-,  ‘the’,  and  badinjdn,  ‘eggplant’, fr.  Pers.  badin-gan,  fr.  OI.  vatin-ganah.  Cp. berengena.
4008:austere
4011:austere,  adj.,  stem,  severe;  very  simple.  —  OF. austere  (F.  austire),  fr.  L.  austerus,  ‘dry,  harsh, sour,  tart’,  fr.  Gk.  auax^pit;,  ‘harsh,  rough, bitter’,  fr.  aiisiv,  ‘to  dry’,  fr.  auo<;,  ‘dry’.  See auantic.
=== SKT austere ===
1187:Austere.  (F.-L.-Gk.)     '^A.'E.  amUrt.
18490:Stem(t),  severe,  austere.  (E.)  M.E. MUrH*.  A.S,  ttyme,  stem  (which  shoold rather  be  spelt  stum).  Allied  to  Du. stuurifh,  stem,  .Swcd.  stursk.  rcfrnctory; Goth,  aftiisltiurran.  to  murraar  agai&it.
```


## [2026-09-14T01:23:05.020Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KNT.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nfor n in [229,230,231,232]:\n    p=pages[n]\n    print('--- leaf',n,'len',len(p))\n    print(p[:300].replace('\\n',' '))\n\"",
 "description": "Kent leaves around uška"
}
```


### [2026-09-14T01:23:06.089Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 5, in <module>
IndexError: list index out of range
--- leaf 229 len 3950
d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (Ogden ap. JAOS 58.325; not yadiyatš 2d sg. opt. mid. with Wb. Symbolae Koschaker 196, nor fut. pass. with Hz. AMI 8.67, ApI 357-8) XPh 39. lwadé- conj.
--- leaf 230 len 1505
am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2. гада- sb. ‘wagon’ (570.11, $148.11), see urata-. Irad- vb. ‘leave’: Skt. rah-, pres. rahati 'sep- arates, leaves’, to pIE *regh-, Av. razah- 5isola- tion’, or to pIE *redh-, NPers. (through Ars. РЫ.
--- leaf 231 len 1256
1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29. vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur
```


## [2026-09-14T01:23:24.448Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('KNT.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nprint('total leaves',len(pages))\nfor n in range(218,234):\n    p=pages[n]\n    m=re.findall(r'\\b(1[5-9][0-9]|2[0-2][0-9])\\b',p[:120])\n    print(n, m, repr(p[:80].replace(chr(10),' ')))\n\"",
 "description": "Find page numerals in KNT leaves"
}
```


### [2026-09-14T01:23:25.521Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 7, in <module>
IndexError: list index out of range
total leaves 232
218 ['166'] 'with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing’ + "wüdá- ‘abode’ ('
219 [] '‘I pierce (as with a spit)’, Gt. faran ‘to travel’. рамо[т- іаїу| nsn. past pte.'
220 [] 'tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pfiana- ‘battle, army’'
221 ['154'] 'r-, Gk. rarnp, Lt. pater, Gt. fadar, pIE *poler- (863.11, 875.1, 576.1, $154.II)'
222 [] '-. — fra&aram asn. XPf 26f, 37. Fraéda- sb. ‘Frada’, a Margian rebel: Elam. pir-'
223 [] '1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1; XPc 1; XPd 1; XPf '
224 [] '2; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55, 88, 94; 2.25, 34f, 40, 45, 54'
225 [] "BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy 2; D'Sb 2"
226 [] '24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]jiSta-ISàm] '
227 [] 'ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1'
228 [] 'so a province of the Persian Empire, ‘Egypt’; тазе. sg. as sb., ‘Egypt’, a provi'
229 ['223'] 'd sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; '
230 [] 'am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71'
231 [] '1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-'
```


## [2026-09-14T01:23:33.479Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('HRN.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor n in [186,187,188]:\n    print('=== leaf',n,'printed',n-21)\n    print(pages[n][:2500])\n\"",
 "description": "Horn p.166 area"
}
```


### [2026-09-14T01:23:34.627Z] TOOL RESULT

```
412
=== leaf 186 printed 165
- 165 -
747. Aeny 'Stein ; Gewicht, Würde', senrjin.
ap. ad^a(n)(jaina' steinern'; phlv. sa{n)(j (P.-V. z. B.
vd. 19 (13)), sang (AV.)
Allgemein entlehnt, z. B. kurd. senk^ seng; af/.
sang ; bei. sing (289) ; sangL. song,
Np. senjJdm (mit sekundärem Infinitiv se/ten —
phlv. sa/tan, sanßt , PP61. ; g. satnmn, Käs. örsaten,
örsatman, verset — PPP. sf?;^^e, Sahn. I, 1 Vers 10)
^wiegen* ist ein sekundäres Denominativum von seng,
Nöldeke (mündliche Mitteilung) schlägt vor, das
altpersische Wort (wie Spiegel, (jlossar) mit an-
lautendem d zu lesen, indem er dieses a in np.
murd]aseng 'Bleiglätte' und must\aseng \Schleuderstein'
wiederfindet. Auch denkt er an Zusammenhang mit
ai. ägman- 'Stein* (vergl. np. rts, No. 22) und (mit
Spiegel und Darmestete r) dem schwierigen aw.
asengöl.gäum (yt. 19, 43)^).
748. sün Stil 'Richtung, Seite', "^ID (Jer. 17, 1).
phlv. sük *Seite, Richtung' 2).
Eine ältere Form ist nicht vorhanden; das np. l
•ff
beruht auf Übertragung (vergl. No. 373). Ursprüng-
lich soft, wie skr. LW. söya- beweist (Weber, Pär.
des Kpn.).
749. suwär, eswär (Lex.) 'Reiter'.
ap. as(s)a]bära- 'Reiter' (doch wohl = *aspabara- ^) ;
phlv. (tsbär 'Reiter, aspwar Ritter (Nöldeke, Karn.
39 Note 2)4).
LW. kurd. suvär ; afy. spör, swör ; bei. sawär (232).
750. sötten 'anzünden, verbrennen, Praes. söz-em^ söz,
nw-^^yü (Qiss. Dan.).
') Zu derselben Auffassung über aw. aaehyö.gäum ist soeben auch
Burtholomae, Indog. Forsch. II, 268 gelangt (Correkturnote).
^) Arab. LW. cahärsüj *Markt', syr. LW. "^IDlNnii^ scheinen
herher zu gehören (ursprünglich *Vierseit, Viereck'); dann etwa auch
die mit s beginnenden, zuletzt von Hübschmann, ZDMG. 46, 247
No. 90 zusammengestellten Worte?
^) Aspa- auch in aw. A8(s)a\hana- {ß. pr.)?
^) Savärdk (vd. 1 (24 J) kann nicht *Reiter* sein.
=== leaf 187 printed 166
- 16() -
Käs. Q. bdsüy, Causat. sujünüden, K. bisiij^ Z. bosot,
aw. l/'saoc-, saoöayähi 'anzünden', atare. |saofca- Teuer-
brand', saocant' 'brennend'; phlv. sö/tan, Praes. söcem
(päz. sözet), söc(i)sn, söcäk (vd. 8, 253), söclmtan ; ai.
l/"(;öc-, gocati.
kurd. sötm^ ez disuzim brennen* ; afy. sezal, sejal '),
smjavul; oss. d. sojun^ t. s^/i« Verbrennen (226);
bei. sucarj^ n. s?«5ay intr. 'brennen (349), söcag ^ n.
sösay trans. 'brennen* (358) ; wa/. LW. säz^ sar. srfw^
'Brand'.
751. 8üd 'Nutzen, Vorteil'.
g. sid 'Zinsen*.
aw. [/'saV' 'nützen'; phlv. süt , sütih, sütömand,
sütlnUa/L
bei. sät, Sit (357); sonst allgemein entlehnt.
752. Süden 'reiben', Praes. säy-em, sät/lden.
ai. l/'cd' 'wetzen, schärfen .
kurd. süin^ sün 'reiben, ein Messer reiben, schärfen'.
Die Bedeutung ist im Neupersischen verblasst ;
vergl. aber das Kurdische.
753. sür *Fest, Gelage'. •
aw. süirya- 'Morgenessen* (Darniesteter, Et. ir.
II, 161 und Geldner, KZ. 25, 531 Note 228); phlv.
5/Tr 'Morgenmahl, Mahl'.
bei. LW. slr 'Hochzeit, Verlobung' (241) ; siyn. sur
'Gelage, Hochzeitsfest* (die Bedeutung ist hier noch
mehr als im Np. specialisirt).
754. sTirfii, sülax, ^Nt^lD (Is. 11, 8) 'Loch'.
Darmesteter's Etymologie (Et. ir. I, 62) aus
aw. *siifräka' , phlv. "^sufräk , "^suhräk , ^süräk in
säräk]öniand bezw. süläk]ömand ist unmöglich, da im
Aw. nur suwrä- ('Ring' oder Pfeil') vorkommt (vergl.
oben No. 740).
kurd. LW. särä/; afy. sürai^ LW. süläy.
*) Vergl. bezüglich des Vokals Kas. V. bdslz, bäalzün neben
Inf. Hüten, hafilznv (Oftusat.), g. lie.^(Ji(J (3. Sg.), sejeuph 'Tripper*.
=== leaf 188 printed 167
— 167 —
755. Hözen 'Nadel'.
g. sejen ; Käs. Z. sö^ö,
aw. vergl. snlca- 'Nadel'; plilv. säcau (päz. süzan,
sözan) (Bund.); skr. rüka- '(jetreidegranne , Stachel
eines Insekts'.
kurd. mzin^ hezüzin {*sü£in) 'Nadel'; oss. LW. d.
sojine, t. sujtn ^Nadel' (S. 181); bei. sücin, slöin^ n.
slsin^ sisan^ sisin (356) ; wa/. s/c, sar. s'ic.
Das Wort bietet in seinen verschiedenen Formen
mehreres Auffällige. Der np. Majhfilvokal wird durch
Kä§. Z. sözo, oss. sojine neben supn, süjln etc. gestützt,
während die sänimtlichen anderen Formen (besonders
auch das 7, vergl. aber auch S. KiG Note 1) gegen ihn
sprechen. Skr. siict-^ tmöU (schon Ait.-Br., ^at.-Br.)
stehen isolirt. Wenn man mit Tomaschek (Central-
asiat. Stud. 11, 8().'ij Entlehnung aus dem Sanskrit
annehmen will, so dürften aw. snka-, skr. güka-y
np. sök *Ähre, Granne* nicht herangezogen werden.
756. sog 'Trauer, Kummer.
aw. vergl. atare,]saoka' 'Feuerbrand'; ai. röku- ciber
schon in der übertragenen Bedeutung 'Qual, Schmerz,
Trauer neben '(ilut, Brand*'); arm. sug Trauer* (H.
No. 254, nach Bartholomae, Studien II, 17, LW.).
757. söf/end *Eid'.
aw. saokenta]vant' 'Schwefel enthaltend' (vergl.
Geldner, Studien I, 103).
LW. kurd. sö7id 'Eid* ; bei. sauylnd^ sögind (359).
V
758. sTilT, snl 'Pflug* (unbelegt, nur im FS).
Von Justi (Handbuch s. v. sufra-) mit aw. sufrd-
'Pflug* zusammengebracht, was aber nicht vorkommt
(s. oben No. 740).
759. si (geschrieben sih) 'drei', siyum^ seyum (AM.), poiHD
(Is. 37, 30).
ap. I^Httya- dritter'; aw. ^n- 'drei'; phlv. s(i)\tigar
'dritter*, päz. sl ; ai. tri- ; arm. ereU (H. No. 100).
') Vergl. np. ä/efi'i säg (»Sälin. T, 16 Vers 42).
```


## [2026-09-14T01:23:42.329Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sūt\\|süt\\|sut \" NYB_vol2_glossary.txt | head -20; echo \"=== leaf 189 ===\"; python3 -c \"\nt=open('NYB_vol2_glossary.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nprint(pages[189][:1800])\n\"",
 "description": "Nyberg glossary sūt"
}
```


### [2026-09-14T01:23:43.282Z] TOOL RESULT

```
468:"p: api-š, ”pm’n' or (Ps.) *pmn: api- man, ’pt’n': api-tän, "p$^n! or (Ps.) *pšn: api-ščin: 1. and, introducing and coordi- nating sentences, e.g. andar-rón andar šut api-$ guft 1818-14; coordinating substan- tives if the second subst. is determined by an encl. pron., e. g. zantšn + Ahriman api-š visütakän 8819; also preceded by u: u api-t 6°, u api-š 7822, u api-sdn 79°, etc. — 2. introducing the apodosis after ka 94. 1025, 5225-27, 5418; after cigon 931; after an isolated w. having the character of a protasis: hämöden api-š hàn zan... ayyāt būt all this [to supply: engaging his attention], the remembrance of that woman came upon him 11'!-!*; — taking up the sentence again after a preceding digression: han zan u hàn fradand 1-8... api-man ne özat 1212-3. — Av. (82 sg.) aipi, OP apiy ‘moreover, further’, both encl. and often only emphasizing: OP düraiy apiy (and other spellings) ‘very far’; surviving in Milr -p(?), g. v. Along with it there must have existed a fully stressed form "dpi; id.-europ. "dpi (Gr postp. Ézt, prep. èni), whence the gen- uine Arm. eu ‘and’; it is the counterpart of Gr ču, Lat et (eti-am). This "dpi > Milr ap, in the sense of ‘and’ and in the apodosis, is normally used in the Sassa- nian official language as the bearer of encl. pronouns beginning the sentence, but in fact occasionally occurs alone, as in the Ps. (several instances, v. Gloss.); PR 231.14, 347. 404; PhlY 31! (intro- ducing the apodosis). Apparently it was counted among the archaisms which need- ed explanation, because it was included in the FrP (ch. 24). Paz. has preserved some remnants of the archaic form: awam = api-m SGV VII, 22, awama = api-mān ibd. VI, 47. X, 28. 35; Paz. AV, ed. Antiā, Päz. texts 35818; hawasq = api- gan SGV V, 62, etc.; the Paz. forms reg- ularly occurring may be shortened allegro forms of api-m ete., v.s.v. u. The equi- valents of api-m etc. given by the FrP are wm, wt, wš, which seem to coincide
532:apa-sütak
535:scindo). This act. is generally supplanted by the secondary caus. apasihčnitan from apa-sih-. — Note: — There is a synonymous vb. of uncertain origin which may have been influenced by the apa-sih- vbs.: Paz. awasdinidan SGV XI" = Phl *apa-sāyēnītan; "ps'dín! = apa-sāyišn Mx 15% (wanting in Cod. K); *pys’synytn' = apēsāhēnītan (the second -s- inverse spelling of h) DkM 175°. 351! (in the MS 13419. 27015), *pys'hšnyh = apesahiš- neh ibd. 180° (= MS 13816); to be de- rived from *apa-sü- *apa-säy- ‘to rub away’, cf s. v. apa-sütak ?
542:apa-stam [’pst’m] reliance 725. 8215, — Paz. awastgm; for *apa-stān < *upa- stäna-; Arm lw. apastan ‘refuge, resort’. apastéh [’p’styh] support 8222. — < Olr *upa-ā-stā-, ci Av. (396) upa-stā- ‘assis- tance, help’. Paz. substitutes dasti. apa-sütak [’pswtk'] probably: treated with magic art, of a sword 2516, 2813, —
544:apa-sütak
546:Cf NP afsün, ausün ‘charm’, afsä ‘a wizard’, afsäyidan ‘to subdue, esp. by magic’, undoubtedly to be connected with NP sidan säy-, farsūdan farsäy (< *fra-) ‘to rub’, the magic treatment con- sisting of some special rubbing or strok- ing of the sword (< *upa-sü-, v. apa-). However, the corresponding OInd. vb. šā- means ‘to sharpen, to whet’ ($ita- ‘sharp’) a sense also attested in Ir: NP afsän, ausän ‘whetstone’; MPrs hswd = hassüd < *ham-süt "whetted' of a sword (Hen- ning, BSOAS XII, 1947, 45), directly to be compared with OInd (RV) sam-sä- ‘to whet’; thus apa-sütak could simply mean ‘sharpened, whetted’. The parallel epi- thet distak (g. v.) is not quite clear.
2182:Kämak-süt [~-swt'] n. pr. one of the seven heroes who will usher in the fraš- kart (g. v.) 1069-14, — Av. (1431) Vouru.- savak- Yt. 13128; in Phl vouru- *wide(ly spread)’ was mistakenly combined with (1360) žvar- ‘to choose’, hence the ren- dering by kämak. i
2183:Kāmak-vaxšišn [—-whššn'] n. pr. one of the seven heroes who will usher in the fraškart 1069-18, — Av, (1431) Vouru.- nomah- Yt. 13128; on kāmak for vouru- v. the preceding w. Usually vaxsısn is emended to niyäyisn (g. v.) in order to obtain congruency with namah- (v. na- mac), but I do think we should retain vaxsisn, which is attested by all MSS: ‘from whose will growth (or increase) arises’, as the counterpart of Kämak-süt ‘from whose will beneficial works arise’.
2833:östikän [^wstyk?n'] trustworthy, truthful 7015, — Ps. ’wstyknyhy ‘reliability’ (pat ~ = Syr ba-šrārā Ps. 13111) from *östikän- ; Arm. lw. ostikan 'supervisor, manager', which seems to suggest an original *östekän < *ava-staya-ka-; -ē- could, of course, be supposed also for BP, but cf óstak. MPrs hwstyg'n 'firm, steadfast'; Paz. ostign, Skr v. säbhipräya- (Mx), sütradhàra etc. (SGV).
3464:pt. fut. of (1561) sav-; Paz. Saosyös (ete.); ci sūt.
3547:181 sūtēh
3565:sit [swt'] use, advantage, benefit 6219. 6313.24 ote, — MPrs swd; Paz. sud, NP süd, from Av. (1561) sav- ‘to benefit’, savā- savah- '(eternal) welfare’, cf Sošans. sütak [swtk'] torn to rags 112'*. — Pt. of sutan = NP sidan säy- ‘to rub, to wear, to tear’.
3566:sütaköh [swtkyh] utility, salvation 106°. — V. süt.
3567:sūtēh = sütakeh 78* (Paz. sudai).
3569:sūtē-karēh
3570:sūtē-karēh [swtyklyhy] supplication, en- treaty 1284, — sūtē- probably < OP *euti- from Av. (1648) srūtt-, v.s. v. srūtan and cf srav and sobdr.
5361:srūti-: sūtēkarēh
5456:Vouru.savah-: Kāmak- sūt
6005:hswd: apa-sütak hšyptg: šēp- hweyhr: hu-cihr hwnsnd: xYan-sand hwy, xwy: hči hwsrwg: hu-srav hwstyg’n: östikän hwsk: husk hwšnwd: ēšnūtak hwždg: yatak hyštn, hyl-: hištan
6127:soxtan swend: sčkand swd: süt swyg: a-sčhišn sxt: saxt sxwn: saxUan sygyn: *sak syh: ?sih szyd: sac-
=== leaf 189 ===
295
 Ps. sky; MPrs sygyn ‘of stone’ (A-H II) suggesting stk, NW form of OP ikä ‘gravel’.
3gak [sk'] a Saka-man; pl. the Sakas, the : Saka people, cas. rect. — 5827; pl. cas. obl: —-dan-šah P1:2. P2:4.6. — OP Saka-.
sāk [s’k'], sai [s'y] tax, impost: ~ u baz 177. 5874. 1185-24, 1218; 2 barak ~ double impost 1192. - MPrth s’g ‘number, part’ (MHC; Henning, BSOAS XII, 1947, 308); Arm. lw. sak; KZSPrth 1. 9 xmys*k ‘in all, all told’ = Prs 11 ult. ’mly (...), Gr. v. óuo0; NP sā, sd ‘tribute’; cf MPrs sgwmnd ‘calculable’, ’s’g ‘innumerable’ (A-H II).
Sakistān [skst’n' ; inscr. skstn] the country of the Sakas: P1:3.5.6. 1162. — Medi- eval Arab form Stjtstān, modern Sistän. sak-äzät [sk’z’t] the Saka nobility P 1: 8. — V. āzāt.
sal, Prth sar [ŠNT] year; in dating: apar ~ 2 mazdésn bag" Šāhpuh<r)Y in the year 2
www.parsianjoman.org | ool wok
sal | 173
of His Mazdayasnian Majesty Sh. P I: 1; apar — 68 [this seems to be the correct reading] inthe year 68 [of the reign of King Shapur II] P2:1; ~ 58, àtur* + Artaxšer ~ 40 etec., v.s. v. tur; — ~ pat ~ year by year 191; pat har 40 m every 40th year 86**; pat 3 ~, pat 6 ~, pat 9 — in three, six, nine years 9319-21; 10621-22; pat 3000 ~ 4 menos āstišnēh within the 3000 years of heavenly exis- tence 3820-21; 393; ka 30000 ~ gētē āstišnēh (but), anaibigatik 330 ~ apäc but when it was the 3000 years’ (period) of material existence, and 330 years of the unassailed period still remained 3926-27; — hac én and — apäc so many years ago 1674. — Av. (1566) sarad-, OP Gard-; MPrthPrs sr; Paz. NP sal.
sälak [s?lk' ; SNT-k'] adj. of the preceding w. used in composition with a numeral: duxt-é ... 3-— a three year old daughter 14%; dāt + 15-— the age of 15 years 3! etc. ; ka Zartuxšt 7-~ būt 5217-18, 7-~ homänäk about seven years old 26°; — in repe- titio
```


## [2026-09-14T01:23:50.783Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD sūd ===\"; grep -n \"sūd\\|sud \\[\" PHD.txt | head -20; echo \"=== PHD hušk/xušk ===\"; grep -n \"hušk\\|xušk\\|xwšk\" PHD.txt | head -20",
 "description": "MacKenzie sūd and xušk"
}
```


### [2026-09-14T01:23:50.854Z] TOOL RESULT

```
=== PHD sūd ===
172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
216:arzómand I2 āsūdan
217:arzómand [le wmnd | (N arjumand)] valuable, worthy. ~ih: value, worth. Arzür []zwl] a demon; a mountain at the mouth of hell. a-sag [?s?*k! | M *s?g] innumerable, countless. азап Pon! | N ~] at rest, easy, peaceful. “АП: rest, ease, peace. a-sar Dell endless. āsāy-, ~išn, v. āsūdan. a-sazāģ ["sc? k!] unfitting, unsuitable. a-sazisn|ig Dscfn-yk'] imperishable, permanent. ~ih: imperishability, permanence. a-sēj [Psyc] free from danger.
219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
572:stün(ag) [stwn(k)!' | M 'stwn, N sutūn] column, pillar, mast. stir [sżwl] trustee, curator, guardian. ~ЛЬ : trusteeship. sturģ [stwlg | N suturg] fierce, contentious; gross, coarse. süd [swt! | M send, N ~] use, profit, advantage. sudab [st?*5 | N ~] rue. sūd-abģār [swt?fk'/] profitable. sūdaģ [swtk!] negligent, indolent. ~ih: negligence, indolence. sidan, sāy- [swtn', s'd- | N ~] rub. sūd(ö)mand [swt(?w)mnd | N sūdmand] useful. suft [swpt' | N ~] shoulder. suftan, sumb- [swptn!, swmb- | N ~] pierce, bore. sumb [swmb* | N ~] hoof. isūr [sw] | M swr, N ~] meal, feast, banquet. *sür [sel] strong. sūrāg [swl(?)k'] hole, burrow. ~ig [-yk'] burrowing (animal). ««Omand (-'wmnd] holed. sūrāx [swPh | N ~] hole. sust [swst! | = M, N —] slack, lazy. ~ih: slackness, laziness. Iguš [swš | (N šus)] lung. *suš [stw$] degree (of arc). suxr [swhl | N surx] red. suy [swd | M swy-] hunger. *swahistan, swah- [swh-stn' | P swh-] sigh. sya [syd? | (P syw, N styah)] black. ~hag [-hk' | N -a] pupil (of eye).
736:advantage bahrwarīh, sēg, sūd; v. profit.
2422:indolence ajgahānīh, sūdagīh.
2423:indolent ajgahān, sūdag.
3237:profitable nirmadómand, sūdabgār.
3238:profitless abēsūd.
3414:rest (v.) āsūdan, wisāy-.
4179:useful sūd(ē)mand.
5499:suft suftan sanj-, sūz- sozag sózan sozisnig sozián sug südomand sūdabgār sūd sūdan sūdagīh sūdag sūdmand panjāhx geg
=== PHD hušk/xušk ===
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
400:huniyāģar [hwayd’kl | N xunyágar] entertainer, musician. hu-niyox$ [hwnydwhs] attentive. hunsand [hwnsnd | = P, (N xursand)] happy, contented. ~ih : happiness, content. hunušak [hwnsk' = Av. hunu§] offspring (daevic). hunušakēnīdan [hwnskynytn'] bear daevic offspring. hu-pādixšā(y) [hwp?thš”(d)) good ruler. ~th: good rule. hu-passandagih [hwpsndkyh] satisfaction. hur [ŠKL < A fkr; hwl] an alcoholic drink, *koumiss. huram [hwlm | N xurram !] happy. ««īh: happiness. hurām [л?т] blissful. hu-|-ramag [hwlmk'] having good flocks. ~-rust [-/wst'] well-grown. ---Süzagih [-s’ckyh] agreement. ~-8рӣз [-s5?s] grateful. ^ husraw [hwslwb' | (M hwsrwg), N xusraw] famous, of good керше у m ~ih: fame, good repute. Ms hušk [kwšśk! | = M, N xušk] dry. —-kün [-S TE] impotent. hu-škūh [kwškwh] dignified, splendid. ^h: dignity. hu&nüd(ag) [лото (А)! | M hwinwd, N xusniid] contented, happy. ~th: contentment, happiness. hu-tuxš [kwtwhš] artisan. huwaršt [hwwlst! = Av. hwarfta-] virtue, good deed. hu-xém [hwhym] of good character, good-natured. ^h: good character. hüxt [kwht' = Av. hüxta-] good speech.
1610:dignity huškēhīh, škēh.
2397:impotent hušk-kün.
3781:splendid huškēh, P nisāg.
```


## [2026-09-14T01:23:52.199Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD swt ===\"; grep -n \"swt\" SOD.txt | head -20; echo; echo \"=== SOD skw ===\"; grep -n \"škw\\|skw\" SOD.txt | head -20",
 "description": "Gharib Sogdian swt, škw"
}
```


### [2026-09-14T01:23:52.303Z] TOOL RESULT

```
=== SOD swt ===
4008:different  forms,  swt(y)k,  swt  and  swptyk.  The  first 
4014:The  second  Pahlavi  form,  swt  (su5),  is  reflected  in 
49133:6155  nwswtr  B  ^Uj^U^T 
67032:s(u)yu6lk   ©<*suY6iyaka   ^swyS^k,  swt*yk 
67719:8861  snk'swtr   B      (^-^  c^^L^m  jj  ^^  ^)\j^^^ 
68914:suydik   (swy5yk)  ©pi.  -u  gen.  pi.  -n   ^swt'yk 
69201:9078  swt   B  >y* 
69208:9079  swt}yk   M  ^jl^ 
69215:9080  swtr  =»  swttr 
69217:9081  swttr  B  vuf  «JUjJ^>, 
69218:sutr  (swtr) 
70975:sow,  saw   ©pi.  swt   -»s*w 
70989:saw,  so  ©OP  syava—,  <*cyav  ©3sg,  pres.  swt 
71176:swane  ?  =»sw-,  swtondyCy),  sw^n^e/y 

=== SOD skw ===
11498:acku   ®<*asruka   ©pi.  -'   =»cskw 
17749:'skw'ch 
17888:1567  >skw-   B,  M,  S       (u>>  y  \.>  j->)j£kJJ  *u-^  *o-\# 
17889:(s)skaw   Oskw'y-,  sqw-)   ^skwn,  swq-,  skw-, 
17891:'skw't- 
17895:1568  >skw>ch  S 
17896:(o)skwac   ©f.  n.   ^'skw't- 
17907:'skw'nVk 
17913:1569  'skwWk   B  >&j>\5\  <JLS  ^ 
17914:(o)skwame 
17919:1570  »skw'mc(h)   B,  M,  S  ,l^J  oJy  <  J^C- 
17920:(o)skwamc 
17927:1571  'skw'mt'k   B  jLS.jj^ 
17929:(o)skwamte  ?   ^'skw'm'k 
17935:1572  'skw't-    B  "  j^hjj  i jxU  <Oj_^ 
17936:(o)skwat   ©pt.  st.   =>>skw-,  Jskw}ch 
17940:GMS  536;  TSP;  SCE;  >skwtt>  Anc.  Lett.  2.206 
17942:1573  >skw'y-  =>  'skw- 
17944:1574  'skw'ynV   S  ^xU 
17945:(o)skw(a)ene  ©prcs.  part.;  pi.  -/   =>'skw-,
```


## [2026-09-14T01:23:59.585Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '69195,69230p' SOD.txt; echo \"=== skw dry? search for 'dry' glosses ===\"; grep -n \"škw\\b\" SOD.txt | head -20",
 "description": "SOD swt entry context"
}
```


### [2026-09-14T01:23:59.663Z] TOOL RESULT

```
sus,  sos  ? 

degree 

Hen.  JRAS  1942,  239;  GMS  1592 

9078  swt   B  >y* 
sOt 

benefit 

Frag.  Len.  60.3 

9079  swt}yk   M  ^jl^ 
sutik  ^swyS'yk,  sywSyk 

Sogdian 

Sogdica.  8.7;  GMS  996 

9080  swtr  =»  swttr 

9081  swttr  B  vuf  «JUjJ^>, 
sutr  (swtr) 

Sutra  i 

TSP  6.43,  8.62 

9082  swx'y-  C,  S  o*£xL  <^b^  L^S 
suxay   =»swxst»,  sxw*y-,  syw*y- 

(to)take  up,  0<?)lift  up 

GMS  417;  STi  13.10-,  STii  628;  BSTii:  C2,  12V12; 
CII,  G13,  17 
=== skw dry? search for 'dry' glosses ===
```


## [2026-09-14T01:24:06.534Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"^ *[0-9]*  *šwk\\|šwk \\|swk'\\|škwh\" SOD.txt | head -20; echo \"=== grep 'dry' as gloss line ===\"; grep -n \"^dry\" SOD.txt | head -20",
 "description": "Search Sogdian 'dry'"
}
```


### [2026-09-14T01:24:06.680Z] TOOL RESULT

```
31972:2.28;  <5wky  prSwk'cyk,  TSP  2.1079 
36825:xur   ©*hvan  IE  *swel  -»swk'nt 
68961:soyand   ©<Av.  saokdnta   =*swqnt  xwr-,  swk'nt 
69025:9053  swk'nt  B,  S 
=== grep 'dry' as gloss line ===
19168:dry 
19173:dry  land 
61461:dry  I 
61516:dry 
61524:dry,  dried 
70327:dry 
70342:dry  land 
70381:dry 
71096:dry 
71118:dry 
77224:dry  land,  continent 
89018:dry     1752,  7967,  7975,  7976,  9238, 
89024:dry  land     1753,  9240,  10225
```


## [2026-09-14T01:24:09.470Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 19160 61450 61510 70320 70370 71090; do echo \"---- $n ----\"; sed -n \"${n},$((n+30))p\" SOD.txt; done",
 "description": "SOD dry entries"
}
```


### [2026-09-14T01:24:10.526Z] TOOL RESULT

```
---- 19160 ----
(a)skaruP,  askruf  ?  ©<*skarf 

trouble 

SCE  21  n  p34;GMS  366,482 

1752  >skw   B,  M 
(o)sku   ©<*hisku   =*skw,  swk1 
dry 
GMS  93;  Sogdica.  64.13;  BBB  486 

1753  >skw>c   M(S) 
(o)skuca(+z}y)  ©f.  adj. 
dry  land 
Sogdica.  64.13;  S  W,  C2  n  pl50.26 

1754  >skwch    B 
(o)skuc   ®<*skuth  Khot.  skat  a 
throat 
TSP  6.88;  GMS  147  A 

1755  'skwch-'ptr'ywstk 
(o)skuc-(o)patrxusk  ? 
having  an  obstructed  throat 

SCE  390;  Gersh.  Sogd.  Cpds.  TSP  1945,  147; 
JRAS  1942,  9 

1756  >skwr5    B,  M  =»  »sk»wr8,  skwr5 

1757  >skwr5y>   S  ^  >sk,wr5y> 
---- 61450 ----
7965  ptw>p-   B  o^£-l 
patwaP  (ptw^-)  ©Khwar.  pcrffly- 
Go)respond 

BSTBL,  Dhy.  8;  Benv.  JA  1939,  377n;  STii  5.37 

7966  ptw'b-    C  =»  ptw»p- 

7967  ptw*c   M  *jSjj>.  iS~Li>- 
patwac   =»ptw>tch,  ptwHyCy) 

dry  I 

BBB  p56,  491;  GMS  1273 

7968  ptw'f-   M  ^U 
patwaf  ©impf.  ptyw}f 

(r<9)weave 

Hen.  JRAS  1942,  232  n  6;  BSOAS  12,  312.124; 
GMS  622 

7969  ptwVt-   M  o^jjj* 
patwart   ©<*pati-  warta-  =»ptw*yrt- 
driving  away 

Hen.  Sogdica.  31.17b  34,  7 

7970  ptw}rt   B,  M  ?  o-if  ^  tc^r  j-» 
patwart   =»pw  ptw'rt 
---- 61510 ----
charm  stone 
TSP  3.92 

7975  ptw'tch    B  u£i^<«ju£i£- 
paftva(t)c   ©f.  pp.  *=» ptw^yfy),  ptw>c 

dry 

VJ  902,  +zay 

7976  ptw>ty(y)   S,  M  Jj&-  «ajCii>- 
patwate   ©<*pati-wa(y)   ©pp.  ^ptw^-,  ptw>c, 

ptw>tch 
dry,  dried 
BBB  500;  GMS  1273;  Hen.  Tales.  481.50  n  f; 

Frag.  Len.  29.17 

7977  ptw'y-    B  oxl^^l^- 
patway   ©<*pati-  wdya;  <*way/*wey  ©impf. 

pt>yw}y   ^ptwy^- 
0o)wind,  (to)rol\ 
VJ  29(;  GMS  570;  Bailey.  HMV  30 

7978  ptw^e-    B  cpb^  O^olf T 
patwe5  ©<*pati-waidaya-   ^ptwyS-1 
OcOinform,  transmit 

Benv.  TSP  6.97,  8.171n  p204;  GMS  302 
---- 70320 ----
9236  sks'pwt  =»  sks'pt 

9237  skth    B  =»  sykth 

9238  skw   M  sSj^ 
(o)sku   ©<Av.  hisku   ^'skw,  swk1,  skwy(y) 

dry 

GMS  96,  397;  BBB  p53.486 

9239  sqwnt   C  Ji<Xj 
sks/unt  ?,  skund  ?   -^sk'ntCy) 

lame 

BSTi  219  n  p26 


9240  sqwpn   C  ^ji{Jii^ 
skupn  ?  ©ace.  -n}  =»wskwpn 

dry  land 

BSTii  857.15;  Benv.  Eti:  JA  1955,  329;  C2,  22V15 

9241  skwr6   M  oiw 
skorG  (sqwr9,  }skwr5)  ^sk'wrStr,  ^k'wrS, 

sk*wr5 
difficult 
---- 70370 ----
thinking  of  hardship 
BSTi  184 

9246  sqwrGy*  =*  'sk'wrSy* 

9247  sqwyy  =>  skwy(y) 

9248  skwy(y)   M  >Si±- 
skawe  ?  (sqwyy)  ©<*(hi)$kuwaka   =»swkc\ 

skw 
dry 

GMS  412,  952;  BBB  f59 

9249  sqyr-   C  =*  sk>yr- 

9250  sl}wk   B  -»  sr>wk()) 

9251  sin-   C  jjii-^^  ^  jl 
sem  ?  =»sym- 

(ro)blush 

C2npl80,  111  V4 

9252  sm'V-    B  =*  sm>r- 

9253  smV   B  =*  sm>r» 

9254  smVkh    B  =¥  srn^'kh 
---- 71090 ----

9355  swq-   C  =»  swk- 

9356  swk-   M  Sj^ 
suk   (swq-)  ©f.  -*  =*}skw,  skw,  swkc* 

dry 

GMS  93;  BSTi  162;  C2,  69R26,  swq\  pl50  n26 

9357  swk*   M.  (c~J  ^UoG  (tylfjX 
(a)soka 

Ashoka 

Hen.  JRAS  1944,  138.30  n  pl41.4 

9358  swk}csmy   M  j-\^£  i^-^j^ 
suk-casme,  sok-  casme 

insolent 

BBB  p65,  526  f  nl;  GMS  285nl 

9359  swkc*   M  ^jj>- 
sukca   Oswkc)  ©*(hi)$kwaka  ©f.  adj.  =»swk\ 

skwy(y) 
dry 
■v    BBB  486;  GMS  412,  1272
```


## [2026-09-14T01:24:21.310Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SOD_pages.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nimport re\nfor target in ['9078  swt','9238  skw','9356  swk-','1752  >skw']:\n    for i,p in enumerate(pages):\n        if target in p:\n            print(target,'-> leaf',i,'printed~',i-66)\n            break\n\"",
 "description": "SOD page numbers for entries"
}
```


### [2026-09-14T01:24:22.457Z] TOOL RESULT

```
leaves 645
```


## [2026-09-14T01:24:25.480Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SOD_pages.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor target in ['9078','9238','9356','1752']:\n    for i,p in enumerate(pages):\n        if re.search(r'\\b'+target+r'\\b',p):\n            print(target,'-> leaf',i,'printed~',i-66)\n            break\n\"",
 "description": "SOD leaf lookup by entry number"
}
```


### [2026-09-14T01:24:26.956Z] TOOL RESULT

```
9078 -> leaf 433 printed~ 367
9238 -> leaf 440 printed~ 374
9356 -> leaf 445 printed~ 379
1752 -> leaf 134 printed~ 68
```


## [2026-09-14T01:24:38.191Z] TOOL CALL #28: Bash

```json
{
 "command": "pdftoppm -f 431 -l 431 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg431 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg431.png",
 "description": "Render PDF page 431"
}
```


## [2026-09-14T01:24:40.081Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nimport re\nfor i,p in enumerate(pages):\n    if 'خشک' in p and 205<=i<=215:\n        print('leaf',i,'printed~',i+543)\n\" ",
 "description": "Find خشک in Borhan vol2"
}
```


### [2026-09-14T01:24:40.359Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 81124 Sep 13 21:24 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg431.png
```


### [2026-09-14T01:24:41.626Z] TOOL RESULT

```
leaves 684
leaf 210 printed~ 753
leaf 211 printed~ 754
leaf 212 printed~ 755
```


## [2026-09-14T01:24:43.692Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg431.png"
}
```


### [2026-09-14T01:24:44.508Z] TOOL RESULT

```

```


## [2026-09-14T01:24:44.500Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T01:25:11.347Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('HJB.txt',encoding='utf8',errors='replace').read()\ni=t.lower().find('shawl, s.')\nprint(i)\nimport re\nfor m in re.finditer(r'SHAWL', t):\n    print(m.start(), repr(t[m.start()-100:m.start()+800].replace(chr(10),' ')))\n    print('---')\n\" | head -60",
 "description": "Hobson-Jobson shawl"
}
```


### [2026-09-14T01:25:12.572Z] TOOL RESULT

```
-1
3938483 'aps,  tir,  \'head,\' suihy  \'pleasure.\' 3.  Shalbaft.  -  P.  skalbaf^  *  ab^^i- weaving.\'    (See  SHAWL.) 3.  SicktenoyB. 3.  8008IES. 3.  SubnomB,  BuhlomB.—"  Shnhnam  is  a thin  pellucid  muslin  to  which  the  Persian figurative  name  of  \'evening  dew\'  {skab- nam)  is  given,  the  fabric  being,  when  spread over  the  Dleaching-field,  scarcely  distinguish- able from  the  dew  on  the  grass."  {Taylor, op.  cit.  45.) 3.  SuccatoozLB.    (See  SUCLAT.) 3.  TaffatieB  of  sorts.  "  A  name  applied to  plain  woven  silks,  in  more  recent  times signifying  a  light  thin  silk  stuff  with  a considerable  lustre  or  gloss  "  {Drapn^*  Dirt. S.V.).  The  word  comes  from  r.  td/Uai,  \'to twist,  spin.\'  The  Aln  (i.  94)  has  tltfiak  in the  list  of  silks. 3.  TainBOOks. — H.  tansuihy  \'taking  ease.* (See  above  under  NAINSOOKS.) 3.  TanjeebB.  F,tanseby '
---
4558593 'as  perpetrated with  the  knowledge  of  Bajerow.\' —  Jfa^/m, CetUral  India,  2nd  ed.  i.  307.] SHAWL,  s.  Pers.  and  Hind,  sk&l, also  doshala,  \'a  pair  of  shawls.\'  The Persian  word  is  perhaps  of  Indian origin,  from  Skt.  savcUa,  *  variegated.\' Sir  (>eorffe  Birdwood  tells  us  that  he has  founa  among  the  old  India  records ^\'Carmania  shSls"  and  ^\'Carmania shawools,"  meaning  apparently  Ker- mdn  shawls.  He  gives  no  dates  un- fortunately. [In  a  book  of  1686 he  finds  "Shawles  Garmania"  and "  Carmania  Wooll "  ;  in  one  of  1704, **  Chawools  "  (RepaH  on  Old  Records,  27, 40).  Carmania  goats  are  mentioned in  a  letter  in  Forrest^  Bombay  Letters^ i.  140.]  In  Meninski  (published  in 1680)  skdl  is  defined  in  a  way  that shows  the  humble  sense  of  the  word originally : "Panni  yiliores  qui  partira  albi,  partim '
---
```


## [2026-09-14T01:25:19.149Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('HJB.txt',encoding='utf8',errors='replace').read()\ni=t.find('SHAWL,  s.  Pers.')\nprint('leaf',t[:i].count('\\f'))\nprint(t[i:i+2500].replace(chr(10),' '))\n\"",
 "description": "HJB shawl leaf + full text"
}
```


### [2026-09-14T01:25:20.357Z] TOOL RESULT

```
leaf 868
SHAWL,  s.  Pers.  and  Hind,  sk&l, also  doshala,  'a  pair  of  shawls.'  The Persian  word  is  perhaps  of  Indian origin,  from  Skt.  savcUa,  *  variegated.' Sir  (>eorffe  Birdwood  tells  us  that  he has  founa  among  the  old  India  records ^'Carmania  shSls"  and  ^'Carmania shawools,"  meaning  apparently  Ker- mdn  shawls.  He  gives  no  dates  un- fortunately. [In  a  book  of  1686 he  finds  "Shawles  Garmania"  and "  Carmania  Wooll "  ;  in  one  of  1704, **  Chawools  "  (RepaH  on  Old  Records,  27, 40).  Carmania  goats  are  mentioned in  a  letter  in  Forrest^  Bombay  Letters^ i.  140.]  In  Meninski  (published  in 1680)  skdl  is  defined  in  a  way  that shows  the  humble  sense  of  the  word originally : "Panni  yiliores  qui  partira  albi,  partim cineritii,  partim  nigri  esse  solent  ex  lana et  pillis  caprinis;  ni:gusmodi  pannum  seu telam  injiciunt  humeris  Dervidi  .  .  .  instar atolae  aut  pallii."  To  this  he  adds, "Datur  etiam  sericea  ejusmodi  tela,  fere instar  nostri  multitii,  sive  siroplicis  aive duplicati."  For  this  the  2nd  edition  a century  later  substitutes:  ** Shdl-i-Htndl" (Indian  shawl).  "Tela  aericed  subtilissima ex  India  adferri  solita." c.  1590. — "In  former  times  shawls  were often  brought  from  Kashmir.  People  folded them  in  four  folds,  and  wore  them  for  a  very long  time.  .  .  .  His  Majesty  encourages in  every  possible  way  the  (*kdi-bctf%)  manu- facture of  shawls  in  Kashmir.  In  Lah6r also  there  are  more  than  1000  workshops." — A  In  i.  92.  [Also  see  ed.  Jarretty  ii. 849,  855.] c.  1665. — "Us  mettent  sur  eux  a  toufe saison,  lorsqu'ils  sortent,  une  Chal,  qui  est ime  maniere  de  toilette  d'une  laine  tres-fine qui  se  fait  a  Cachmlr.  Ces  Chals  ont environ  deux  aunes  (the  old  French  aunCj nearly  47  inches  English)  de  long  sar  une de  lar^e.  On  les  achete  vingt-cinq  ou  trente ^cus  SI  elles  sont  fines.  II  y  en  a  m6me  qui oofHtent  cinquante  ^us,  mais  ce  sont  les trfc-fines."— TA^ttpnoi,  v.  110. o.  1666. — "  Ces  cfaalas  sont  certaines  pieces d'tftoffe  d'une  aulne  et  demie  de  long,  et d*une  de  large  ou  environ,  qui  aont  bcodte aux  deux  bouts  d'une  esp^oe  de  broderie, faite  au  metier,  d'un  pied  ou  environ  de large.  .  .  .  J'en  ai  vu  de  ceox  que  les Oimxikt  font  faire  expr^  qui  ooatotent jusqu'k  cent  cinquante
```


## [2026-09-14T01:25:26.003Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\ni=t.find('shawl,')\nwhile i>0 and 'Pers' not in t[i:i+400]:\n    i=t.find('shawl,',i+1)\nprint('leaf',t[:i].count('\\f'))\nprint(t[i:i+700].replace(chr(10),' '))\n\"",
 "description": "Klein shawl"
}
```


### [2026-09-14T01:25:27.153Z] TOOL RESULT

```
leaf 760
shawl,  n.  —  Pers.  shdl,  named  after  Shaliat ,  a town  in  India,  where  it  was  first  manufactured. Cp.  F.  chale,  Du.  sjaal,  G.  Schal. Derivative:  shawl ,  tr.  and  intr.  v. shawm,  n.,  an  obsolete  wind  instrument,  the  fore¬ runner  of  the  modern  oboe.  —  ME.  shalmye,  fr. OF.  chalemie,  a  var.  of  chalemel,  fr.  Late  L.  ca- lamellus,  ‘a  small  reed’,  dimin.  of  L.  calamus, ‘reed’,  fr.  Gk.  xaXa;j.oq.  See  culm, shay,  n.,  a  chaise  (obsol.)  —  Back  formation  fr. chaise,  mistaken  for  a  plural  (as  if  spelled  chais). For  similar  back  formations  cp.  pea  and  words there  referred  to. she,  nom.  sing,  of  the  3rd  person  fern.
```


## [2026-09-14T01:25:27.820Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT shawl ===\"; grep -n -i \"shawl\" SKT.txt | head -5; echo \"=== AHD shawl ===\"; grep -n -i \"shawl\" AHD_watkins1985.txt | head -5; echo \"=== AID shawl ===\"; grep -n -i \"shawl\" AID.txt | head -5",
 "description": "Skeat/AHD/Whitworth shawl"
}
```


### [2026-09-14T01:25:27.913Z] TOOL RESULT

```
=== SKT shawl ===
17058:Shawl.  (Pcrs.)  Pcrs.  Mi/(pron.  jAaW), a  shawl,  mmtle.
23617:b^hau,   I'artce,    pasha    (^lacha,    pashaw, saw),  peri,  »aih  Ca)>  Kpoy,  ibab,  shawl,
=== AHD shawl ===
=== AID shawl ===
1416:Chadar.  [Hindustani,  from  the  Per- sian.] A   sheet,  a   cloth,  a   shawl.
3368:Kamarband.  [Hindi,  from  kamar , the  loins,  and  band,  to  bind.]  A shawl  or  cloth  worn  round  the waist.
```


## [2026-09-14T01:25:42.048Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor n in range(755,766):\n    p=pages[n]\n    nums=re.findall(r'\\b1[34][0-9][0-9]\\b',p)\n    print(n, nums[:8], repr(p[:60].replace(chr(10),' ')))\n\"",
 "description": "KLN page numerals near shawl"
}
```


### [2026-09-14T01:25:43.224Z] TOOL RESULT

```
leaves 903
755 ['1422'] 'no,  ‘coin’, dimin.  formed  fr.  zecca,  ‘a  mint’,  fr.  A'
756 ['1424', '1425'] 'net,  sermonette  (qq.  v.),  sermonettino (q.v.),  sermon-i'
757 ['1426', '1427'] '  shape’.  See  prec.  word  and  suff.  -oid. Derivative:  '
758 ['1428'] 'verus.  See  severe and  -ity. Seville  orange,  also  Sevil'
759 [] 'darkness’,  Olr.  scath,  OW.  scod, Bret,  squeut,  ‘darkne'
760 [] 'n.  F.  chantier,  ‘workshop’, fr.  F.  chantier,  ‘timberya'
761 [] 'cepter’,  and  to  Heb. shebhet,  Tod,  staff,  club,  scept'
762 [] ' let  loose, loosened,  detached;  he  unsheathed,  drew  (s'
763 ['1438'] 's:  Shinto-ism,  n.,  Shinto-ist,  n. ship,  n.  —  ME.  sch'
764 ['1439', '1440', '1441', '1488'] 'shout-er,  n.,  shout-ing,  n. shove,  tr.  and  intr.  v.  '
765 ['1442'] 'er,  tr.  v.,  shutt-er- less,  adj.,  shutt-ing,  n. shuttl'
```


## [2026-09-14T01:25:50.078Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nfor n in [209,210]:\n    print('=== leaf',n,'printed~',n+543)\n    print(pages[n][:2200])\n\"",
 "description": "Borhan vol2 خشک page"
}
```


### [2026-09-14T01:25:51.228Z] TOOL RESULT

```
=== leaf 209 printed~ 752
                                                                                                ‫یوا‬


‫‪٩‬‏ ‪-‬‬    ‫ند‬
         ‫زبان‬
            ‫دانوتن‬
                 ‫که در زیربغل جامه و می‬              ‫باشد ‏‪٩‬وآن‌یز؛ کوچکی‌استکه در میان‌آن‬
             ‫ویمعنیآینه زالو هم‌آمده امتا ‪۰‬‬          ‫بافته بسته باشند‬       ‫شم‬
                                                                             ‫رنیبا‬
                                                                                 ‫بسما‬
                                                                                    ‫ا ری‬
                                                                                       ‫حلقه‌ای از‬
‫ت بکسر دوخای تقطمدار‬     ‫حشت‬       ‫حشت‬
                                                    ‫وانگشت سبابة رادرآن حلقه کرده بجانب خسم‬
                                                     ‫انداز ند‪ - ۴‬ونام نك دوازدهم است از جمله‬
‫وسکون دوشین و تای قرشت » صدای ورق‌کاغذ‬
                                                      ‫و سك کتاب‪ .‬زند پوازند (ی‪۱‬ع)نی‬‫يتك‬ ‫بيس‬
‫ر جامه که نو پوشیده باشند‪.‬‬‫زمهیو‬
                              ‫وصدای جا‬
  ‫شیت‬
    ‫قتحررا‬
         ‫اول وف‬          ‫کهسدر‬
                             ‫بتر‬
                               ‫خش‬                    ‫بك قىم ازجملابیست وبك‌فم‪,‬چه نك بمعنی‬
                                                    ‫قم باشد ‪ - ۴‬و نوعی از حلوا هم هت که‬
                                                     ‫در مشکها و جاها ریزند نابك پارچه وقرص‬
‫پارچة چهار كوشة زبر بغل جامه و زبر جامه‬                                                               ‫دود‬

                             ‫وشلوار باشد ‪. ۸‬‬
                                                    ‫خشت تابه ه بافوقالی بالف کشد‪.‬‬
‫خشت رر د خشت ر رین کنابه‬                            ‫فوتح بای ابجد ‪ .‬کوره و داش خشت یزی را‬
                                                                                                  ‫‪۳۱‬‬
‫جفتلث = مصغر خشت است ‪ -‬وبارچة‬                        ‫خشتامی ‪ -‬بفتح اول بروزن تردامن »‬
‫مربع زیر بغل جامه ومیان تنبان وشلوار را لیز‬           ‫و سم اول نیز درست‬         ‫مادر زن رگاونند‬
       ‫عنته‌اسه‬
  
=== leaf 210 printed~ 753
           ‫‪۷‬ی‬‫‪۲‬‬



                                                                      ‫خشتنشار ‪ = ۱‬بفتح اول وشین نقطه‌دار‬
 ‫کنابه از زر بر ه‬          ‫‪-‬‬   ‫کردن‬          ‫خشخاش‬                   ‫بالفکشیده بر وزن بهمنبار ‪ .‬مرغابی بزر گی‬
                                             ‫ریزه کردن باشد ‪.‬‬        ‫است تیره رنگ و میان‌سراوسفیدمیباشدوبتر کی‬
                                                                                                ‫قعقلداق خواند ‪.‬‬

‫وسکون دوشین وبك نای قرشت * بمعنی خشت‬
 ‫شد‬        ‫خای‬   ‫دو‬    ‫نکش‬       ‫‌‬   ‫‪5‬‬   ‫خشت‬        ‫حش‬

                                                                      ‫مفلوك ‪» .‬‬        ‫خشتو ك =(‪ )۱‬بر وزن‬
                                                                       ‫حرامزاده رااگویند ؛ ویض اول هم آمده است‪.‬‬
 ‫خشت‌است که صدای‌ورق‌کاغن وجامه وازاروشلوار‬
                                             ‫نو پوشیده باشد ‪.‬‬         ‫حشته = بفتح اول و فوقانی و سکون‬
 ‫‏‪ =m‬بققح اول وثانی وسکون‌کاف‪.‬‬                   ‫حك‬                    ‫انی ‪ ,‬مردم مفلس وبی برگك ونوا گروابند ‪.‬‬
 ‫وهی است وبعریی جبل خوانند ‪ -‬وبضم اول‬
                                    ‫نکام‬                              ‫خشحان ‪ ۲‬ه باجم بر وزن افشان ‪.‬‬
 ‫و سکون انی وکاف معروف است که دز مقابل‬                                ‫عناصر اربعه کروایند کهآب و خاك وهوا وآتش‬
  ‫ترباشد ‪٩‬‏ ‪ -‬وبمعنی محض و بحت (‪ )۲‬وصرف‬                                                                                 ‫باشد ‪.‬‬
‫ممسك را هم‬             ‫و‬       ‫و نحل‬          ‫انت‬     ‫امد‬   ‫لو‬        ‫خشخاش ‪ -‬مروف است ‪ ۰ ۴‬و آن‬
                                                 ‫میگویند ‪. ۷‬‬           ‫چند قم باشد ‪ :‬اببض واسود وزبدی ومقرن‪. ۴‬‬
                                                                       ‫خشخاش اییض بوستانی امت وآن سرد وترباشد‬
                               ‫مانم ومنم کننده را گوشد ‪۰‬‬               ‫و بعضی گویند خشك امت ‪ .‬خوردن آن باعسل‬
     ‫‪ .‬بضم اول و فتح خای‬                 ‫خشکاخور‬                       ‫منی‌را زبادکند ؛وخشخاش اسود صحرایی امت‬
                                                                       ‫و آنرا خشخاش مصری هم میگونن
```


## [2026-09-14T01:25:59.663Z] TOOL CALL #37: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:752 --image 2>&1 | tail -40",
 "description": "Render Borhan page 752"
}
```


### [2026-09-14T01:26:00.765Z] TOOL RESULT

```
no scan of BQT covers printed page 752 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:26:06.480Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\" MON_part1.txt MON_part2.txt; grep -n \"خشک\" MON_part1.txt | head -5; echo \"===\"; grep -n \"hušk\\|husk\" MON_part1.txt MON_part2.txt | head -10",
 "description": "Mo'in local files check"
}
```


### [2026-09-14T01:26:06.573Z] TOOL RESULT

```
MON_part2.txt:94500
MON_part1.txt:99339
1170:مرده را بعد از سل دادن بدان خشک کنند. 
1171:کاغذ آب خشکککن. 
1203:اب‌خشک؛: ۸ 20-4 (امر.) ش‌سیشه» 
1362:کند و محتوی ۵ درصد مواد خشکت 
1667:از آن فرو چکد گویند.) آب خشکدکس. 
===
```


## [2026-09-14T01:26:08.321Z] TOOL CALL #39: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['FRS'],ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('FVF'),ensure_ascii=False,indent=1))\n\"",
 "description": "BQT/MON/FRS/FVF metadata"
}
```


### [2026-09-14T01:26:09.453Z] TOOL RESULT

```
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
{
 "title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')",
 "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt"
 ],
 "page_offset": "different edition — no mapping",
 "covers_etymology": false,
 "notes": "Persian OCR fair. Ganjoor does not host Loghat-e Fors."
}
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


## [2026-09-14T01:26:14.916Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nfor n in [211,212,213]:\n    print('=== leaf',n,'printed~',n+540)\n    print(pages[n][:2500])\n\"",
 "description": "Borhan v2 leaf 212"
}
```


### [2026-09-14T01:26:16.015Z] TOOL RESULT

```
=== leaf 211 printed~ 751
  ‫دهان‬    ‫خك‬                                                                                                     ‫‪۳‬و‪۷‬‬
 ‫مازه ‪ ,‬شاخهای خشکی را کوبند که از درخت‬
      ‫‪-‬ت دگرخفتتهر‌ااند ‪.‬‬ ‫ودس‬‫پاشن‬
                                ‫وده ب‬
                                    ‫برب‬                          ‫وزن‌دزد(‪ )۱‬افثار » نخود و ماش و عدس و باقلا‬
‫حشت لسشجتالورست که اوراسنگه‬                                                               ‫ناد ‪.‬‬   ‫نتر‬
                                                                                                    ‫و]‬ ‫گثال‬
                                                                                                          ‫وام‬
                                                                  ‫خثشك امار ‪ -‬بتممزء رس‬
‫= بفتح بای فارسی وسکون‬              ‫ی‬     ‫خلت‬                   ‫"رضی است که‬
                                                                          ‫بالف کشیده وبرای قرشت زده م‬
‫مارزدم شوم قدم و نامبار که‬                ‫به‬
                                           ‫نیا»‬
                                              ‫کتان‬
                                                 ‫نح‬               ‫آابعربی استسقا گوبند ؛ وبابنمعنی بجای میم»‬
                                                                                                           ‫نر‬
                                                      ‫باشد ‪۰‬‬                                   ‫نون هم بنظرآمُده است ‪.‬‬
 ‫جان‪ -‬با جيم بروزن مرغدان‬                  ‫خشك‬                    ‫خشکا مار ‪ -‬بنماور وثالك مویم‌هر‬
                                                                  ‫دو بالف کشده وبرای فرشت زده › ممعنی‌خشك‬
  ‫یده‬
    ‫ششق‬
      ‫نتج ع‬
          ‫و شخصی را نیز گوبند که اذ‬                               ‫امار است که مرض استسفا باشد؟ ‪ -‬وبمعنی‌هبم‬
  ‫ناث ‪.‬‬   ‫محروم‬        ‫نکرده واز باد دوست‬       ‫و ءاشقی‬           ‫واستقصا ونفحص وتجسی واءتفساروحاب‌واستیفا‬
‫حشلت جنیان ‪ -‬کی را گونند که‬                                                                           ‫هما مده است ؟ ‪.‬‬

‫جذبش و حکرتهای بی نفم و فایده ازو بعمل‬                           ‫را‬       ‫انگیین د شهد و علی‬                 ‫خشك‬
                                                  ‫‪۰‬‬    ‫آ‪.‬د‬       ‫گونن دکه درخانةٌ زنبور خشك شده باشد وآ درا‬
‫خشك جهان ‪ -‬کنابه از روزکار‬                                        ‫عل خشك خوانند ‪ .‬طبیمت آن گرمتر از عسل‬
 ‫ومردم صاحب‬       ‫و زمانه است که در آن اکهلرم‬     
=== leaf 212 printed~ 752
    ‫‪4‬‬


                                                                ‫خشثك دیش د بکر رای بقیطه‬
                                            ‫‪.‬‬   ‫خممر فزق‬       ‫و سکون تحتالی و شين نقطه دار ‪ .‬بمعنی مکر‬
‫خشاث مغز = بمعنی‌خنك سراست که‬                                   ‫وحله‌وفاق وفریفتن وبازی‌دادن وبهانه کردن(‪)۱‬‬
                                                               ‫وخشکیی رایزگونند که بر‬          ‫_‪)۲‬‬
                                                                                                 ‫دن(‬
                                                                                                   ‫شرد‬
                                                                                                     ‫اآو‬
                                                                                                       ‫بذر‬
                                                                                                         ‫وع‬
              ‫بی‌ته ودیوانه‌وش وتند خوی باشد ‪٩‬‏‬
                                                                                      ‫روی زخم بسته شود ‪٩‬‏ ‪.‬‬
‫خشکنانه ‪ = ۲‬بانون‌بر وزن موربانه‪.‬‬
      ‫نانیراگوبند که آنرا بی‌نان خورش خورند ‪.‬‬                  ‫خثك ر بشه » بنتح تن فرتت ‪۱‬‬
                                                               ‫بمعنی بهانه کردن و عذر آوردن باشد چنانکه‬
‫خشکنای « با ون بالف کشد‬                                        ‫اکر گوند خنك رشه میکند مرادن ‪,‬اشد‬
‫زده » نای کلورا گویند ‪ ۰‬و بعربی حلقوم‬
                                      ‫بتحتانی‬
                                                               ‫که بهانه میکند ‪ -‬وخشکی روی زخم را نیز‬
                                                    ‫خوانند ‪.‬‬                                            ‫کو‬
‫خشکو اھ » باواو ‪.‬بر وزن و ععنی‬
                                                               ‫خشکسار؟ ‪ -‬باسینبی قطهبروزن‬
      ‫خشکفاست که نانخمیر برتیامده وفطیرباشد‪.‬‬                   ‫بردبار » زمینی را گوبند که از آب دور باشد ‪-‬‬
    ‫بضم اول‌وفتح کاف" معروف‬              ‫جخشکه‪۹‬‬                       ‫و زمیلی که باران برآن لباریده باشد ‪.‬‬
‫است کهپلاو بیروغن باشد ‪ -‬وآرد گندم نايشته‬
                             ‫را نگیوزیند ‪¥.‬‬
                                                               ‫خثك سبرف=تح ین بی‌نقطه بروزن‬
                                                               ‫ففل کرء تندخوی ویهوده کوی وسيك ومی‌نه(‪)۴‬‬
‫خشل ‪ -‬بنتح اول والی وسکون لام ‪۰‬‬               
=== leaf 213 printed~ 753
                                                                                                                ‫‪۷۲‬‬


 ‫بزر کهتیرء رن میانسرسفید باشد و ترکان‬                            ‫خشی ه بنتح اول بروزن چمن گ‪.‬یاهی‬
‫قثقلداق میگوبند ‪ ۰‬وبضم اول نیز درست است "‬                         ‫باشد کهاز آن جامه بافند و فقیران ودروشان‬
‫و بشاین نقطه دار همآمده است چه در فارسی‬                           ‫پوشند ‪ -‬وبکر اول مخفف خشین است» ‪ ۰‬آن‬
 ‫سین وشین هردو بهم تبدیل می‌بابند ؛ و بجای‬                         ‫بازبی باشد نه‌سقید وله سباء ‪ -‬ودرعربی هرچیز‬
 ‫لون بای حطی هکمفته اند کهبر وزن بدیدار‬                                                             ‫درشت را گوشد ‪۳‬‬
                                                   ‫باشد ‪.‬‬         ‫خشنان ‪ -‬ب باضمول بر وزن برهان ‪۰‬‬
‫‪ -‬بر وزن بلنگ ‪ ,‬زاغ سر‬                    ‫حشنگ‬                                       ‫فرخنده وخجسته ومبارك راگوبند ‪.‬‬
‫وسر کجل و کجلی را کوبند ‪ -‬و مردم کچل را‬                           ‫ک=نابه ازمنافق‌بودن‬            ‫دن‬
                                                                                                  ‫شیلو‬
                                                                                                     ‫ش‬ ‫خ‬
                                           ‫تگبفزته‌اند‪.‬‬                                             ‫وطاق کردن باشد ‪.‬‬
         ‫‪۱‬‬       ‫‪۲‬‬     ‫معیم ‪. _ ۵‬‬
 ‫حشنو = بامول والك بروزن‌پر کو‪.‬‬                                   ‫خشی خاله = بروزن‌طر بخانه‪ .‬خانه‌ای‬
 ‫مخفف خشنود است که راضی وخوشحال باشد ‪۰‬‬
                                                                  ‫‪۰‬ویند که ازتی بوربا سازند ‪ -‬و خانه‌ای رانيز‬
                                                                                                            ‫گ‬
                    ‫ویفتح اول هم درست است ‪۴#.‬‬                      ‫گته‌اند که بر در ورنجرءآن خار شتری ندند‬
  ‫حشنی ‪ -‬بضم اول و کر الك بورزن‬                                    ‫و آب بر آن پاشند تاهوا و نیم سرد درون‬
                    ‫‪.‬‬        ‫ند‬
                              ‫وهبرا‬
                                  ‫گحش‬
                                    ‫معطی » زن فا‬                                                                         ‫ی‬
‫واو ‪۰‬‬    ‫بصم اول ونانی وسکون‬          ‫=‬   ‫حشو‬                     ‫= بقتح اول باسن بینقطه‬            ‫ر‪۶‬‬
 ‫مادر زن ومادر شوهر باشد ‪٩‬‏ ‪ -‬ویقتح اول در‬                        ‫بمعتی خشتنشار است که مرعابی‬            ‫بروز
```


## [2026-09-14T01:26:26.952Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nfor n in range(206,216):\n    lat=re.findall(r'[A-Za-zšžčāēīōūǰ]{3,}', pages[n])\n    print(n, n+540, lat[:30])\n\"",
 "description": "Latin footnotes in BQT v2 leaves"
}
```


### [2026-09-14T01:26:28.312Z] TOOL RESULT

```
206 746 []
207 747 []
208 748 ['EER']
209 749 ['yaeth', 'dartiC', 'dartiC', 'unhsar']
210 750 ['khsuh', 'akhsuh', 'rar', 'khsuxx']
211 751 ['khsux']
212 752 ['shm']
213 753 ['ERE', 'xishm']
214 754 []
215 755 []
```


## [2026-09-14T01:26:34.570Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nfor n in [210,211]:\n    print('===== leaf',n,'printed',n+540)\n    for ln in pages[n].split('\\n'):\n        if any(c.isascii() and c.isalpha() for c in ln):\n            print(repr(ln))\n\"",
 "description": "BQT footnote lines with Latin"
}
```


### [2026-09-14T01:26:35.655Z] TOOL RESULT

```
===== leaf 210 printed 750
' \u202b\u200f\u202a =m\u202cبققح اول وثانی وسکون\u200cکاف\u202a.\u202c\u202c                   \u202bحك\u202c                    \u202bانی \u202a ,\u202cمردم مفلس وبی برگك ونوا گروابند \u202a.\u202c\u202c'
'         \u202bان(\u202c         \u202b\u200f\u202a E\u202cمت\u202c               \u202b\u202a _ ۱\u202cمصحف «خهنا» ( = خهندار) (ه\u202a.\u202cم )\u202c'
'      \u202b\u202a«€\u202c\u202c    \u202b\u202a ۲\u202cمناس \u202a۷۷۲\u202c\u202c           \u202b\u202a 1\u202cتاوآدیا \u202a۲\u202c\u202c        \u202b\u202a ۹\u202cت بهلوی \u202akhsuh\u202c\u200f\u202c               \u202b\u202a.\u202c\u202c    \u202bیت\u202c       \u202bخه\u202a-\u202c\u202c   \u202b\u202a:\u202c\u202c   \u202bرك\u202c   \u202b_\u202c   \u202b\u202a۵\u202c\u202c'
'      \u202b\u202a ,\u202cبارس باستان \u202a , )51۱((1](-36-\u202cاوستا \u202a_akhsuh\u202c\u200f «اسفا\u202a ۱:۲\u202cص\u202a 51\u202cو \u202a ۹3۱\u202cگیلکی\u202c                                              \u202b\u202a1\u202c\u202c'
'      \u202bو طنزی \u202a ۰ 502\u202cفریزندی \u202aiy ۰ ۲/5۵۱\u202c\u200f \u202a» 8101502\u202cك \u202a .\u202cاس ‘\u202arar\u202c\u200f < سمنانی \u202akhsuxx,\u202c\u200f\u202c'
===== leaf 211 printed 751
'   \u202bمعرب\u202c       \u202bنشادست \u202a۲۰۵۳۰\u202c\u202c      \u202bشاست\u202c      \u202bو ندبداد\u202a٩\u202c\u200f * \u202a٩\u202c\u200f\u202c      \u202bآمده(فرهنك\u202c          \u202bداناند\u202a .\u202cگوید دریهلوی \u202ar)ã(khsux\u202c\u200f\u202c'
```


## [2026-09-14T01:26:51.512Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 -c \"\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor n in range(18,30):\n    p=pages[n]\n    tag=re.search(r'\\[pdf page (\\d+)\\]',p)\n    print('---',n,tag.group(1) if tag else '?')\n    print(p[:80].replace('\\n',' '))\n\"",
 "description": "Locate BQT v3 pdf page 23"
}
```


### [2026-09-14T01:26:52.483Z] TOOL RESULT

```
leaves 721
--- 18 19
[pdf page 19] شا کمونی مالند ؛ وبس یکوند ‎WT‏ که از یشم کوسفند و موی بز سیاه در 
--- 19 20
[pdf page 20] ATTA  ‎SL‏ ۱ » بروزن قالی. شلتوفرا کوشد که برنج از پوست برليامده ‎
--- 20 21
[pdf page 21] شاد ۲۳۰ ات  شا له ۱ = بروزن ‎le‏ معروفت‌وآن  چیزی باشد که از چوب و
--- 21 22
[pdf page 22] ۱۳ ات  شانه‌سر ۱۵ صفیر ‎als‏ سراست که  شانه کاری » ‎at‏ از در آوخت
--- 22 23
[pdf page 23] که ازآن راهپا وشمبها جدا شود - وفام‌جالوری ‎col‏ در هندوستان - ‎pl
--- 23 24
[pdf page 24] پات شاء خرگاه میتا  شاه بانگ ۱ - بنتم ون و سکون کاف »گیاهی امت دوا
--- 24 25
[pdf page 25] شاه دارو شاه ‎gale‏ ه امی است که جمشید بشراب انگوری گذاشته است»وسب
--- 25 26
[pdf page 26] سلفننهه  شاهد لعمر ك ‎gine‏ شاهد فاستقم است که اشاره بحضرت رسالت پ
--- 26 27
[pdf page 27] Sob ‏شاه قام = با قاف بالف کشیده بروزن‎ ‏است که کسی‌خود را دربازی‌
--- 27 28
[pdf page 28] -۱۲۳۷-  سوجای ‎gid‏ پادشاهان ‎ath‏ - ونوعی ازعمارت هم هت +  شاه نی
--- 28 29
[pdf page 29] شایسته ۱ - بکرستای‌بروزن‌آهته بمعتی اول شابان است که سزاوار ولایق 
--- 29 30
[pdf page 30] ات شایکه - بکر ‎at‏ و فتح کاف .لام خاریست که صمغ آلرا عنزروت خوالن
```


## [2026-09-14T01:26:58.575Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 -c \"\nt=open('BQT_v3_pages.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nfor n in [17,18,19]:\n    print('===== leaf',n)\n    print(pages[n][:3000])\n\"",
 "description": "BQT v3 شال page"
}
```


### [2026-09-14T01:26:59.538Z] TOOL RESULT

```
===== leaf 17
[pdf page 18]
{ATTY

شاشه ه بر ون ‎tle‏ » معروف است
که بول و گمیز باشد ۱ - و ‎Ory Feiner‏
وترشح ‎Gs‏ آمده است .

شاشیدن ۲ ۰ بروزن پاشیدن ؛ بمعنی
بو لکردن و کمیز کردن‌باشد - و بمعنی ترشدن
وترشح کردن مم آمده است.

شاغو 4 ۴ ‎o‏ بان ‎abt‏ دار » بروزن
و ممنی شاشوله است که ‎ales Tyke‏ و دستار
‎ask‏ .
‎DL‏ - بسکون کاف » سینه ‎ay‏ زنان
را گربند. وآن پارچه‌ای باشد چهار گوته که
پتانهای‌خود رابدان ‎Pasar‏ -وبز لر را نیز نامند
وآترا تکه خوانند بروزن مکه .

شا کار 4- پروزن پاکار.یمعنی‌بیگار(۱)
باشد » وآن کار فرمودن بزور است که مردم را

کار فرمایند و مزدوری واچرت دهد ۷ .

(۱) خم۱, چك ,چش : بیکار .
0 - شاش.*شاشه» ‎OT‏ تاختن مردم‌بودکه بی ‎WT‏ روزبه ‎GG‏ (ظ:رودکی) گوید:

ناگاه بررآرند ز کنج تو خروشی

سد ‎asl‏ وآن چیزیست که از پشم کوسفند

شا کر ۷ ‎Spee‏ بر وزن چاکر ,
بمعنی شاکار است که ‎ )۱( May‏ وکار فرمودن
بی‌عزد باشد .

شا گر ۵اه * ‎IS Ge‏ فارسی ۰
زر ‎Sal‏ باشدکه بمد از اجرت اوستاد بطریق
‎gl!‏ شا گرددهند ‎٩‏ -وعطای بفقرا ‎sly‏ گوبند
- وبمعتی شاکردهم بنظر آمده است.

شا گردی ۲۰ ‎cl Syn‏ که در
مقاپل اوستادی باشد - و بمعنی شاکردانه هم
هت - و ‎GEIS Jal‏ امرا و سلاطن دا لیز
کویند ‏

شا کلول ‏ با لام رواو بروزن‌زاغول»
مردم ‎le‏ خوار و بسیار گوی و پر حرف را
کویند .

شا کمند۲۱-بايم بروزن پای‌بند. بمعنی

کردند حمه جملهوبررش توشاشه»
‎cal?‏ فرس ۲۱۹ ورك ‎AYA:‏

Com) ‏شاشدن‎ (yee wpe) ‏بدن‎ ۴ (pe) ‏از : شاش‎ ۴

۴ ره : شاشوله :
ای بخت جوان ببا ودر ‎Fl‏ پیچ
‎Uys‏ دستار تو اینجا ‎wigs‏

۴ - مصحف ومشفف ‎Cpa)?‏

۲ - نکنی طاعت وآنگه که کنی‌ست وضیف

(ps) SE = ۷

دست خرد ‎en‏ بساغر بر پیج
دستار لگهدار و پرو در سرپیج .
‎oy!‏ یمین فربومدی. «فرهنگه نظام».
© شاء کار ‎(on)‏ = شا کر (مخفف) +
‎Sy Seal,‏ همه سخره وشا کل رکنی.

کایی مروزی. « لفت فری ‎SVT‏

۸ از : شاکرد ‎lt‏ (جمع) ۰-۲ ‎(on)‏

‎٩‏ - کگیلکی ‎shigerdanag? cage. . ٩62227420261‏ . « کنابادی».

‏۴ از ‎EHS:‏ ( مسدری - بت )۰

‎Jy ۱‏ : شال نمه .

‏# شاگرد - یکسر سوم ‎inal)‏ م رکزی) ‎(CLS.‏ 5282۳0 کنابادی ‎shagerd‏

‏«کتابادی» ۰ کلپایگانی و کرنانشاهی 5118670 «قاسمی» هوحدت» ؛ ‎SST‏ نزد مملمواستاد
کسب علم وهتر کند » کسکه در مدرسه تحصیل داش کند » متملم ۰ ‎aul‏ - کسیکه در ‎ap‏
‎ot‏ خدمت کند ‎KTH‏ در ‎cays‏ پیشه‌وران مالند بنا وجارکار آموزد .

===== leaf 18
[pdf page 19]
شا کمونی
مالند ؛ وبس یکوند ‎WT‏ که از یشم کوسفند
و موی بز سیاه در هم آمیزند وبمالند شا کمند
خوالند .

شا کمو ی ۱ »با میمبوار رسیدمولون
بتحتالی کشده » باعتقاد کفرة هند ییفمبرصاحب
کتاب است وهیچکس بر اسرار او واقف ‎cay‏
‏و در ولادت و وجود او خرق عادات و ‎AGS‏
‎ate TA‏ و کتاب او را لیزشا کمونی خوانند.
وبستی کویند پیعمبر ‎Jol‏ خطاست.*

شالخ ۲ ‎Ge‏ لام و سکون ‎BE‏
‎abe‏ دار (۱) پر فبنان بن ارفنشد بن ‎the‏ بن
لوح ‎col‏ وعایریبی آوست» وعبری ازعابرمشتق
‎el‏

شالده ؟ ‎oe‏ لام و قح
دال ‎del‏ » اسای و بئیاد دیوار و عمارت را
کونند ۴

(۱) چك : وسکرن خا . (۷)چك

» چش : شال ‎won‏

“NIA

شانگ = بفتح لام وسکون لون و کاف
فارسی » ‎Sash oT‏ شخصی را درعوض دیگری
‎com‏ طلبی که از دیگری دارد بگیرند - و بر
جستن و فروجستن شاطران و پباده روان را لیز
کویند 6 - و کلیمی‌راییز کفته‌اند که درزی‌فرشها
دوزند ۷ .

شالنگی (۳) = ‎UE qa‏ بر وزن
نارنگی + ریسمان تابنده و موتاب راکویند,وآن
شخصی باشد که پجپت خیمه وامثال ‎OT‏ رسمان
بتابد و آلرا بعربی لواف خوانند ۷.

شال ‎edad‏ سدراکرنند که از پشم
بز مالند نه از یشم گوسفند .

شالهنگ - ‎pa‏ الث و ها بر وزن
‎igh‏ بمعنی گرو و کروکان بائد و ‎VAT‏
‏بعربی رهن و مرهون خوانند - و بمعنی زیادتی
و اشتلم وسر کشی وافرمالی هم آمده‌است ۸ -
ومکر وفریب وحیله را اي زگونشد.

(۳)خم۱ : شالنکی.

. ‏سا کیامونی . شهرستالی در ملل وفحل (س*۲۸) نام او را «شاکیمن»شبط کرده‎ ٩

ر: بودا =

آرفکشد را پااصد سال زند کی لموده .

چاپ‌لندن ۱۸۵۹م. سفرتکوین آیه‌های ۱۲-۱۱ .۰

۴ - رسیده ‎tL‏ باره‌اش بگاو زمین

9 قی : شلنگه .
۷- آءکز استیلای فس شالهنگه
خنابری رازی. «جهانگیری» ۰

۴ = شلح ‎JAG)‏ وفتح دوم) = ‎Shelach‏ : هسام بعداژ تولید نمودتش
.. وارفکشد ... شلح ‎Le ry gs ad sly‏ کتاب‌المقدی .

‎olin - ۴‏ کنولی «شالودء»

‏گذشته کنگرة قامه‌اش بدو پیکر .
فرهنکه شیرازی. «فرهنگه نظام» .

‏۱ - رك : شال .

‏همچو شاللگی است وایس رفتنم .

‎-A‏ بمعئی‌س رکش «جهانگیری» (شادد درح۷آمدم).

‏# شال-از فارسی وارد عربی‌شده «شال» ‎(pd?‏ و آزعربی وارد فراسوی 00216دلاروی

‎Ser. ona SF yy‏ کلیمی بود کوچك پشمین . عنصری (بلخی) کوبد:

‎OTS‏ مثل حال من بکثت و بتافت

‏که کسی شال جست ودیبا یافت “
‎cal?‏ فري ۰۳۱۷ .

‎js -‏ پارچه‌ای که دور کمر یا کردن پیچند .

===== leaf 19
[pdf page 20]
ATTA

‎SL‏ ۱ » بروزن قالی. شلتوفرا کوشد
که برنج از پوست برليامده ‎wth‏

‎HY JL‏ » با ‎alist‏ بالف کنیده
‎cds‏ بای حطی ‎SaaS MIE»‏ برنج‌زار

‏باشد .0

‎CLL‏ با میم بالف کشیده و خای
تقطمدار (۱)ساکن » نام بوعی ازغله است‌ودانهای
‎oT‏ بفایت کوچك میباشد - وسینه‌بند زنالوا لیز
کوبند.و آن‌پارچدای باشد که زنان پستانهای‌خود
را ‎was oly‏ ۴ .

‏شاماخچه ۴ ‎et phe‏ فارسی »
‎gees‏ دوم شاماخ است که سینه‌بند ‎QU;‏ باشد.

‏شامار با رای بی‌نقطه بر وزن ‎Nk‏
‏ام موضعی است که کروهی از کبران درآن‌توطن
دارند؟ ؛ و باين معتی‌با زای نقطه‌داربروزن آواژ

‏آمده است .

‎Sku‏ « بروزن چالاك ۰ جامةٌ کوچکی
)4( چك : وخا .

‏را کون دکهمردم دررفت کار کردن پوعتصوسیته
بند زباترا هم گنته اند 9 .

‏شاما کچه ۱ ® بر وزن و ‎we‏
‏شاماخجه است که سیثه بند زهان باشد .

‏شاها کی ۷ بروزن ‎SNe‏ سینه
بند زان ‎wath‏

‏شامس ‎oS‏ بکس میم وسکون سین
بی‌شقطه . نام یکی از جزایر بودان است؛وباشین
نقطهدار هم‌آمده است.

‎°

‎the ‏وزن داموی‎ no Sn gald
Ab ‏بلدی است از بلاد بونان ؛ و بستی گوبند‎

‎+ cole po
‏شاهه = بروزن جامه ۰ مقتمه ورویاکی‎
. ‏باشد که زدان بر سر کنند‎

‏شان » بر وزن ‎ME sob‏ زبور صلرا
کوبندکه درآن ‎Le‏ باشد*۱ - و ‎le dies‏
مقید است که از هندوستان آورند - و مشقف

‏۱ - سانسکریت ‎Shali‏ (برنج وغلات مشابه آن) « وبلیامز۱:۱۰۹۸» درمازسران زراعت
‎oy‏ را «شالی» کوبند . «فرهنگهنظام». ‏ ۴ -رله:شاماخچه»شماخ. وقس:شماخیه«جهانگیری».

‏ورك : شا .
شاماکچه )0( = شماخچه «جهانگیری» .

‏شاماخج » شاماخچه , شاماکی . ‎٩‏ = شاماخجه ‎Cem)‏

‏۴ از : ‎cue‏ (هم.) +-چه ‎igs)‏ تصفیر) = ساماخچه ۶ ساما که .
۴ - ظ.مصحف «شابهار» («م.) .

‏6 رد :
۷ از : تاماك-ی ‎(os)‏

‎OT ‏در مجمع الجزایر | دارای ۷۱۰۰۶ سکته و‎ slp ‏جزیره‌ای‎ ‘Samos= A

‏موطن فیثاغوری بود :

‎. ‏بکی‌شهربار اندرو شادکام‎ le ‏یکی شهر شامس‎ nk

‏عنصری بلخی. ‎cd?‏ فری ۲۰۵ ‎٩‏ -

‎: wld, ‏نیز 51185 513202 «رحدت»‎ ta Sy ole  .یماش‎ tr ٩

‏زبد گر ‎abs Ss‏ تومذرشز آفربنش له

‏که ممذورست ومارا ‎cat‏ چون دحل‌عل شاش.

‏« خاقانی شروانی ۲۱۸ .

‏# شام - اوستا - ‎xshafniya‏ » پهلوی ‎sham‏ (غذای شب) «تاوادیاه>۱«اونوالا

‏۹ , کردیع 510800 (عصرءشب ) ‎ShOme gist.‏ (زمان فاصله بين لیمشب وآغلز روز +
غذای شب ) » بلوچی ‎SHAM‏ (غذای عمده » غذای عص )» سریکلی 260100 6 ‎SHAM Loy‏
« اسشق-- هوبشمان 6۷۹۸ ‎CLT.‏ 5910 , فریزندی ‎shum 4, , sham‏ , سلنزیهطه
‎oP‏ . اس ‎OVAL‏ »سمنالی " سنگسری و سرخهیی ‎SHUM‏ , لاسکردی ‎SHAM‏ , شهمیرزادی
‎shad‏ .۲+س۱۷۹*:آغازشب,زمانیاز آغازپیدایش تاریکی‌تب‌نا کامخفتن_غذایی کهدرشب‌خورند.
```


## [2026-09-14T01:27:21.911Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FRS شالنگ ===\"; grep -n \"شالنگ\\|شال\" FRS.txt | head -20",
 "description": "Loghat-e Fors شال"
}
```


### [2026-09-14T01:27:21.976Z] TOOL RESULT

```
=== FRS شالنگ ===
1049:۱ چ : انا مانند بود ۲ - این مشال درع ون نبست؛ س : بقرقوب و شوشیر ۰ 
1057:رود کی : هزارآوا بستان‌در کندا کنون‌ه زار آوا - این‌شال فقط درچ هست . 
4766:است ,نی شانه کرد و اين ببت سابقا منوان مشال برای لفت کلج گذشت » بداجا 
8279:ترش ترش‌باشد خاشالك خورد() . 
8846:ال و س شکل دوم را ندارد و این دوعی از مشال نیز خألیست ۳ - س : س + 
10225:سخنگوی گشتی ۲ سلیمانت کرد نغو شاله بودی مسلمائت کرد 
10370:1 این ترا فظط تین اشاله دازه.: ۲ - ن و چ: خبك کلو نشردن بود ۰ س : 
11490:و شال لفت بشك بوده است آورده و «ر مصراع دوم تصرافی محل وزن‌کرده تا لفت 
12377:زآن مثل حال* امن بکشت‌و بتافت که کی شال تا یی ۱ 
12385:۸ -کرمخلف کیرمن *کنم ٩‏ - چ ون : شال گلیم کوچك‌بود ۰ س : شال گلیمی 
12868:کجا بیش از این کار افروتشال که بود الفتیشش هماره همال 
13839:۳ - ل » زفن مر گوشت دبای بود وخادنیز گویند (بدون‌شال) » س : زغن مرغ 
14481:۱ - این مشال نقط در چ هست . ۲ - چ : چیین‌سله باشد که از ید بانند چون 
15590:( در حاشیه ) . تینکو صندوق بود ( پدون مشال ) » س مثل من » چ این لفت را 
19392:چیزی باشد ( بدون‌شال ) » چ این لفت‌را ندارد. 
19926:افر و نشال ۳۳۲ 
20865:خاشالگ ۲۰۰ 
21586:شال ۳۱۷
```


## [2026-09-14T01:27:24.267Z] TOOL CALL #46: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82sews-\" \"https://www.etymonline.com/word/austere\" \"https://www.etymonline.com/word/shawl\"; do echo \"##### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 431, roots Saus / Savala\" 2>&1 | tail -5; done",
 "description": "Archive web sources"
}
```


### [2026-09-14T01:27:26.969Z] TOOL RESULT

```
##### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82sews-
/home/sfmqrb/git/rishe/data/verification/sources/web/f4f76683aa8c4692.txt
##### https://www.etymonline.com/word/austere
/home/sfmqrb/git/rishe/data/verification/sources/web/8adf722f9eecab24.txt
##### https://www.etymonline.com/word/shawl
/home/sfmqrb/git/rishe/data/verification/sources/web/1beeb34f7a4e5af2.txt
```


## [2026-09-14T01:27:32.549Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -c 2500 8adf722f9eecab24.txt; echo; echo \"#####SHAWL\"; head -c 3000 1beeb34f7a4e5af2.txt",
 "description": "Read etymonline austere/shawl"
}
```


### [2026-09-14T01:27:32.607Z] TOOL RESULT

```
URL: https://www.etymonline.com/word/austere
FETCHED: 2026-09-14T01:27:26Z
STATUS: 200
TITLE: Austere - Etymology, Origin & Meaning

Austere - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of austere 

 austere (adj.) 

 early 14c., of persons, manner, etc., "harsh, severe; grim, fierce," from Old French austere "strict, severe, harsh, cruel" (13c., Modern French austère ) and directly from Latin austerus "dry, harsh, sour, tart," from Greek austeros "bitter, harsh," especially "making the tongue dry" (originally used of fruits, wines), metaphorically "austere, harsh," from PIE root *saus- "dry" (see sere (adj.)).

 From late 14c. as "severe, rigid;" by 1590s as "unadorned, simple in style, without luxuries;" by 1660s as "grave, sober." The classical literal sense of "sour, harsh" (1540s) is rare in English. Related: Austerely ; austereness .
 also from early 14c. 

 Entries linking to austere 

 sere (adj.) 

 Middle English sere , "dried up, withered, barren" (of plants, etc.), from Old English sear, from Proto-Germanic *sauzas (source also of Middle Low German sor , Dutch zoor "dry"), from PIE root *saus- "dry" (source also of Sanskrit susyati "dries, withers;" Old Persian uška- "dry" (adj.), "land" (n.); Avestan huška- "dry;" Greek auos "dry," auein "to dry;" Latin sudus "dry"). Related to sear . Figurative use from 1530s. Sere month was an old name for "August."

 austerity (n.) 

 mid-14c., "sternness, harshness," from Old French austerite "harshness, cruelty" (14c.) and directly from Late Latin austeritatem (nominative austeritas ), from austerus "severe, rigid," a figurative use, in classical Latin "harsh, sour" (see austere ).

 From 1580s as "severe self-discipline, ascetic practices;" hence "severe simplicity, absence of adornment or luxuries," applied during World War II to national policies limiting non-essentials as a wartime economy.

 [
 Austerity ] stands just at the edge of that frame of mind which regards self-denial as good for its own sake ; it pushes simplicity of living and the refusal of pleasure beyond what is deemed necessary or helpful to right living by the great mass of those who are equally earnest with the austere in trying to live rightly. [Century Dictionary]

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Pr
#####SHAWL
URL: https://www.etymonline.com/word/shawl
FETCHED: 2026-09-14T01:27:26Z
STATUS: 200
TITLE: Shawl - Etymology, Origin & Meaning

Shawl - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of shawl 

 shawl (n.) 

 1660s, originally of an article of dress worn in Asia, from Urdu and other Indian languages, from Persian shal , sometimes said to be named for Shaliat , town in India where it was first manufactured [Klein]. French châle , Spanish chal , Italian scialle , German Shawl (from English), Russian shal all are ultimately from the same source. As the name of an article of clothing worn by Western women, it is recorded from 1767.
 also from 1660s 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 Afghan 

 In English, attested from 1833 as a type of blanket or wrap (short for Afghan shawl); by 1877 as a type of carpet; by 1895...

 hack 

 The term hack is also frequently applied by women to any article of dress, as a bonnet, shawl, &c., which is kept for...

 tacky 

 A ribbon on the shopkeeper's counter, a curtain in the bolt, a shawl or bonnet, a bolt of cloth fresh from the loom may be...

 cloak 

 late 13c., "long, loose outer garment without sleeves," from Old North French cloque (Old French cloche, cloke) "traveling cloak," from Medieval Latin clocca "travelers' cape," literally "a bell," so called from the garment's bell-like shape (the word is thus a doublet of clock (

 alchemy 

 "medieval chemistry; the supposed science of transmutation of base metals into silver or gold" (involving also the quest for the universal solvent, quintessence, etc.), mid-14c., from Old French alchimie (14c.), alquemie (13c.), from Medieval Latin alkimia, from Arabic al-kimiya,

 oligarchy 

 "form of government in which supreme power is vested in a small exclusive class," 1570s, from French oligarchie (14c.), from Latinized form of Greek oligarkhia "government by the few," from stem of oligos "few, small, little" (a word of uncertain origin) + -arkhia, from arkhein "

 mirror 

 mid-13c., mirour, "polished surface (of metal, coated glass, etc.) used to reflect images of objects," especially the face of a person, from Old French mireoir "a reflecting glass, looking glass; observation, model, example," earlier miradoir (11c.), from mirer "look at" (oneself

 freedom 

 Old English freodom "power of self-determination, state of free will; emancipation from slavery, deliverance;" see free (adj.) + -dom. Meaning "exemption from arbitrary or despotic control, civil liberty" is from late 14c. Meaning "possession of particular privileges" is from 157

 blue-blood 

 1809 in reference to the blood that flows in the veins of the old and aristocratic families of Spain, translating Spanish sangre azul, cla
```


## [2026-09-14T01:27:39.455Z] TOOL CALL #48: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D8%AE%D8%B4%DA%A9\" \"https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%AF\" \"https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%84\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/h%C3%BA%C5%A1kah\"; do echo \"##### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 431: xošk / sud / šâl / *huškah\" 2>&1 | tail -3; done",
 "description": "Fetch Wiktionary pages"
}
```


### [2026-09-14T01:27:42.919Z] TOOL RESULT

```
##### https://en.wiktionary.org/wiki/%D8%AE%D8%B4%DA%A9
/home/sfmqrb/git/rishe/data/verification/sources/web/cea7ec76e9f3ab2c.txt
##### https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/e915afe5ece9564e.txt
##### https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%84
/home/sfmqrb/git/rishe/data/verification/sources/web/756f35401e242b56.txt
##### https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/h%C3%BA%C5%A1kah
/home/sfmqrb/git/rishe/data/verification/sources/web/a7a4ec9dd5628eea.txt
```


## [2026-09-14T01:27:45.724Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in cea7ec76e9f3ab2c e915afe5ece9564e a7a4ec9dd5628eea; do echo \"===== $f\"; grep -n -A25 -i \"Etymology\" $f | head -70; done",
 "description": "Read Wiktionary etymologies"
}
```


### [2026-09-14T01:27:46.799Z] TOOL RESULT

```
===== cea7ec76e9f3ab2c
ugrep: warning: cea7ec76e9f3ab2c: No such file or directory
===== e915afe5ece9564e
ugrep: warning: e915afe5ece9564e: No such file or directory
===== a7a4ec9dd5628eea
ugrep: warning: a7a4ec9dd5628eea: No such file or directory
```


## [2026-09-14T01:27:49.857Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in cea7ec76e9f3ab2c.txt e915afe5ece9564e.txt a7a4ec9dd5628eea.txt 756f35401e242b56.txt; do echo \"===== $f\"; sed -n '1,60p' $f; done",
 "description": "Read Wiktionary files"
}
```


### [2026-09-14T01:27:50.883Z] TOOL RESULT

```
===== cea7ec76e9f3ab2c.txt
URL: https://en.wiktionary.org/wiki/%D8%AE%D8%B4%DA%A9
FETCHED: 2026-09-14T01:27:41Z
STATUS: 200
TITLE: خشک - Wiktionary, the free dictionary

خشک - Wiktionary, the free dictionary 

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

===== e915afe5ece9564e.txt
URL: https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%AF
FETCHED: 2026-09-14T01:27:41Z
STATUS: 200
TITLE: سود - Wiktionary, the free dictionary

سود - Wiktionary, the free dictionary 

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

===== a7a4ec9dd5628eea.txt
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/h%C3%BA%C5%A1kah
FETCHED: 2026-09-14T01:27:42Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found===== 756f35401e242b56.txt
URL: https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%84
FETCHED: 2026-09-14T01:27:42Z
STATUS: 200
TITLE: شال - Wiktionary, the free dictionary

شال - Wiktionary, the free dictionary 

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
```


## [2026-09-14T01:27:55.402Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in cea7ec76e9f3ab2c.txt e915afe5ece9564e.txt 756f35401e242b56.txt; do echo \"===== $f\"; grep -n -i \"From Middle Persian\\|Proto-Iranian\\|Proto-Indo-Iranian\\|Proto-Indo-European\\|Sanskrit\\|Avestan\\|Borrowed from\\|inherited\" $f | head -25; done",
 "description": "Extract etymology lines"
}
```


### [2026-09-14T01:27:56.409Z] TOOL RESULT

```
===== cea7ec76e9f3ab2c.txt
172: Proto-Indo-European *h₂sews- 
174: Proto-Indo-European *-kos 
176: Proto-Indo-Iranian *Hsúškas 
177: Proto-Iranian *Hhúškah 
180: Inherited from Proto-Iranian *Hhúškah , from Proto-Indo-Iranian *Hsúškas , from Proto-Indo-European *h₂sews- + *-kos . Cognate with Sanskrit शुष्क ( śuṣka ) .
240: > Tajik: хушк ( xušk ) ( inherited ) 
258: Proto-Indo-European *h₂sews- 
260: Proto-Indo-European *-kos 
262: Proto-Indo-Iranian *Hsúškas 
263: Proto-Iranian *Hhúškah 
267: Borrowed from Classical Persian خُشْک ( xušk ) , from Proto-Iranian *Hhúškah , from Proto-Indo-Iranian *Hsúškas , from Proto-Indo-European *h₂sews- + *-kos . Doublet of سُوکھا ( sūkhā , “ dried up ” ) and شُشْک ( śuśk ) . Cognate with Punjabi خُشْک ( xuśk ) .
304: Categories : Persian terms inherited from Proto-Iranian 
305: Persian terms derived from the Proto-Indo-Iranian root *Hsawš- 
306: Persian terms derived from the Proto-Indo-European root *h₂sews- 
307: Persian terms derived from Proto-Indo-Iranian 
308: Persian terms inherited from Proto-Indo-Iranian 
309: Persian terms derived from Proto-Iranian 
310: Persian terms derived from Proto-Indo-European 
317: Urdu terms derived from the Proto-Indo-Iranian root *Hsawš- 
318: Urdu terms derived from Proto-Iranian 
319: Urdu terms derived from Proto-Indo-Iranian 
320: Urdu terms derived from Proto-Indo-European 
322: Urdu terms borrowed from Classical Persian 
323: Urdu terms derived from the Proto-Indo-European root *h₂sews- 
===== e915afe5ece9564e.txt
1604: From Middle Persian [Book Pahlavi needed] ( swt' ) , 𐫘𐫇𐫅 ( swd ) , 𐫘𐫇𐫇𐫅 ( swwd /⁠sūd⁠/ ) .
1664: Borrowed from French soude .
1710: Persian terms inherited from Middle Persian 
1711: Persian terms derived from Middle Persian 
1719: Persian terms borrowed from French 
===== 756f35401e242b56.txt
915: Borrowed from Persian شال ( šāl  / šâl ) .
1200: Borrowed from Persian شال ( šâl ) .
1358: Borrowed from Coptic ϫⲏⲗ ( jēl , “ a fish ” ) , also borrowed as قِيل ( gīl ) 
1440: Inherited from Arabic أَشَالَ ( ʔašāla ) .
1559: Inherited from Arabic شال ( šāl ) .
1662: Borrowed from Persian شال ( šāl  / šâl ) .
1677: Inherited from Sanskrit सृगाल ( sṛgāla ) .
1840: Borrowed from Classical Persian شال ( šāl ) .
1880: Borrowed from an Indo-Aryan language. Compare Hindi दुशाला ( duśālā ) , from Sanskrit शाटी ( śāṭī ) , feminine of शाट ( śāṭa , “ clothing ” ) . [ 1 ] [ 2 ] Sometimes said to be from or influenced by Chāliāt, a Persian pronunciation of Chaliyam in India, supposedly where they were first made. [ 3 ] [ 4 ] [ 5 ] Doublet of سَارِی ( sārī  / sâri ) .
2035: Inherited from Arabic شَالَ ( šāla ) .
2493: Borrowed from Classical Persian شال ( šāl ) . Doublet of سَاڑِی ( sāṛī ) . [ 1 ] Compare Punjabi ਸ਼ਾਲ ( śāl ) / شال ( śāl ) , Gujarati શાલ ( śāl ) , Marathi शाल ( śāl ) , Kannada ಶಾಲು ( śālu ) , Telugu శాలువ ( śāluva ) .
2536: Arabic terms borrowed from Persian 
2544: Arabic terms borrowed from Sahidic Coptic 
2549: Egyptian Arabic terms borrowed from Persian 
2555: Egyptian Arabic terms inherited from Arabic 
2560: Egyptian Arabic terms borrowed from Coptic 
2565: Gulf Arabic terms inherited from Arabic 
2571: Gulf Arabic terms borrowed from Persian 
2579: Hijazi Arabic terms inherited from Arabic 
2585: Hijazi Arabic terms borrowed from Persian 
2592: Iraqi Arabic terms inherited from Arabic 
2597: Iraqi Arabic terms borrowed from Persian 
2601: Kashmiri terms inherited from Sanskrit 
2602: Kashmiri terms derived from Sanskrit 
2613: North Levantine Arabic terms inherited from Arabic
```


## [2026-09-14T01:28:11.879Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1866,1960p' 756f35401e242b56.txt; echo \"=====SUD\"; sed -n '1595,1625p' e915afe5ece9564e.txt",
 "description": "Wiktionary šāl and sud detail"
}
```


### [2026-09-14T01:28:11.947Z] TOOL RESULT

```
 → Macedonian: шал ( šal ) 

 → Romanian: sal , șal 

 → Serbo-Croatian: šȁl 

 → Slovene: šȃl 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from an Indo-Aryan language. Compare Hindi दुशाला ( duśālā ) , from Sanskrit शाटी ( śāṭī ) , feminine of शाट ( śāṭa , “ clothing ” ) . [ 1 ] [ 2 ] Sometimes said to be from or influenced by Chāliāt, a Persian pronunciation of Chaliyam in India, supposedly where they were first made. [ 3 ] [ 4 ] [ 5 ] Doublet of سَارِی ( sārī  / sâri ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈʃaːl/ 

 ( Dari, formal ) IPA ( key ) : [ʃɑːl] 

 ( Dari, formal ) IPA ( key ) : [ʃɑːl] 
 ( Kabuli ) IPA ( key ) : [ʃɑːl] 

 ( Hazaragi ) IPA ( key ) : [ʃɔːl̥] 

 ( Iran, formal ) IPA ( key ) : [ʃɒːl̥] 

 ( Tajik, formal ) IPA ( key ) : [ʃɔl] 

 Rhymes: -aːl 

 Readings

 Classical reading ? 

 šāl

 Dari reading ? 

 šāl

 Iranian reading ? 

 šâl

 Tajik reading ? 

 šol

 Noun
 [ edit ] 

 شال • ( šāl / šâl ) ( plural شال‌ها ( šāl-hā / šâl-hâ ) , Tajik spelling шол ) 

 shawl 

 scarf 

 Derived terms
 [ edit ] 

 شال‌گردن ( šāl-gardan  / šâl-gardan ) 

 Descendants
 [ edit ] 

 → Arabic: شَال ( šāl ) 

 → Azerbaijani: şal 

 → Bashkir: шәл ( şäl ) 

 → Czech: šál 

 → Danish: sjal 

 → Dutch: sjaal 
 Afrikaans: sjaal 

 → English: shawl 
 → Japanese: ショール ( shōru ) 

 → Korean: 숄 ( syol ) 

 → Finnish: šaali 

 → French: châle → Catalan: xal 
 → Franco-Provençal: ch·âle 
 → Italian: scialle → Greek: σάλι ( sáli ) 

 → Polish: szal 
 → Spanish: chal 
=====SUD

 Kélékian, Diran ( 1911 ), “ سود ”, in Dictionnaire turc-français ‎ [2] (in French), Constantinople: Mihran, page 697a 

 Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 From Middle Persian [Book Pahlavi needed] ( swt' ) , 𐫘𐫇𐫅 ( swd ) , 𐫘𐫇𐫇𐫅 ( swwd /⁠sūd⁠/ ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈsuːd/ 

 ( Dari, formal ) IPA ( key ) : [suːd̪] 

 ( Dari, formal ) IPA ( key ) : [suːd̪] 
 ( Kabuli ) IPA ( key ) : [suːd̪] 

 ( Hazaragi ) IPA ( key ) : [sud̪̥] 

 ( Iran, formal ) IPA ( key ) : [suːd̪̥] 

 ( Tajik, formal ) IPA ( key ) : [sud̪] 

 Rhymes: -uːd 

 Readings
```


## [2026-09-14T01:28:20.588Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in DEV.txt PHN.txt LKT.txt LAM.txt; do echo \"===== $f\"; grep -n -i \"châle\\|chale\\b\\|shawl\\|Schal\" $f | head -8; done",
 "description": "French Arabism dictionaries for châle"
}
```


### [2026-09-14T01:28:21.728Z] TOOL RESULT

```
===== DEV.txt
1097:Châle.  Bien  que  le  mot  se  trouve  dans  la  langue  arabe moderne  (Jl^  chàl,  plur.  J^ïUÂ)  chïlân ,  dans  Bocthor),  ce n'est  pas  là  que  nous  l'avons  pris.  D'introduction  peu  an- cienne en  Europe,  il  a  été  apporté  de  l'Orient  par  le  com- merce anglais.  C'est  le  persan  jUi  châl,  sorte  de  drap grossier  en  poil  de  chèvre  ou  de  brebis  que  les  derviches, dit  Moninski,  jettent  sur  leurs  épaules  en  guise  de  man- teau. Le  mot  s'est  ensuite  sj)écialement  appliqué  au  tissu de  Cachemire  :  JOviU  y^^^i  ^:>  a^  Jl^  (s^j^.^  ,  dit  le  Bahâri agam  (cité  par  VuUers).
3249:Cliahban,  voy.  Ciiaban. Chalakd. Chale. Chalef.
4873:jLi  pers.  voy.  Châle.
===== PHN.txt
2771:est surtout célèbre par ses châles de luxe, qui unissent à la
2775:qualité les produits de Cachemire. — Voyez Chale.
3462:rendre le {fi par ch, comme cela se fait, du reste, pour châle,
3464:CHAlE, s. m. (p.)
3467:ou les épaules. Les châles les plus renommés viennent de l'Inde
3470:châles en Orient : l'^fermâîch, châle rayé avec des franges;
3475:de paon), châle de couleurs vives; y*' boghtchah, carré avec
3477:comniencGmeut de ce siècle que la mode des châles étrangers
===== LKT.txt
491:Lat.  Ascalon,  n.  pr.,  eine  Stadt  im  süd- lichen Palästina;  danach  wurde  eine Zwiebelart  als  cepa  ascalonla  bezeichnet; hieraus  unter  Wegfall  des  Substantivums [wie  bei  frz.  fromage  aus  lat.  lac  for- maticuni]  aprov.  escalonha,  afrz.  escha- logne,  it.  scalogno,  sp.  escalona;  mit  Suf- fixwechsel frz.  Schalotte,  pg.  xalota; dtsch.  Schalotte,  Aschlauch.  In  der Vendee  dial.  Schalotte  'derbe  Tracht Prügel'.  [Behrens  Beiträge  87.  ML  694.
872:'Zitronat bäum,  Citrus  (medica)  Bajoura'; hieraus  fvz.  bigarade  'bittere  Pomeranze', bigaradier  'bitterer  Pomeranzenbaum'; aus  seinen  dickschaligen  Früchten  stellt
1376:'Flöte'  [vom  gleichen  Stamme  wie  dudak 'Lippe',  eigentlich  'Erfasser',  vom  Stamme tok  usw.  'fassen',  s.  hier  Nr.  528];  hieraus bulg.  serb.  duduk  'Pfeife,  Schalmei',  russ. dudka,  dudak,  dudocka  'Schalmei',  ßech. dudy  'Dudelsack'.  Aus  dem  slav.  wahr- scheinlich dtsc-h.  dudeln,  Dudelsack. [Gorjajew  98.  Bern  SlEtWb  233.
1397:Auch  tiimbelek  'eine  Art  kleiner  Kupfer- trommel in  Halbkugelform'  [Kelekian Kämüs  417b  mit  ."Abbildung];  hieraus rum.  timbelechiü  'Zimbel,  Schallbecken', timbeleg  in.
1406:'Stachel,  Dorn'  [Pijn  112];  hieraus  dü- rlan  'ein  Baum  Ostindiens,  Durio  zibe- thinus  L.',  der  veegen  seiner  melonen- artigen Früchte,  die  eine  mit  Stacheln versehene  Schale  haben,  so  genannt  wird. Hieraus  ndl.  doerian,  engl,  durian,  frz. dourion,  durion,  it.  duriano.  [Devic  DEt 107.  MMM17.  JAOSXYH,  137/139.
1739:'Schiff';  hieraus  rum.^ÄJWi/e'Schaluppe'; hu\g.  gemtja,  serb.  zemija,  Wvass.hemija, pohi.  komi^ga,  kom§ga,  russ.  konijaga 'Kahn,  Boot'.  [Gorjajew  154.  Bern  Sl EtWb  300.
2329:'Steuer  oder  Taxe,  die  an  den  Fiskus  zu zahlen  ist';  hieraus  mlat.  cahalla  'Steuer', prov.  sp.  gabela,  pg.  gabella,  frz.  gabelle 'Warensteuer',  it.  gabella  'dass.',  von Neapel  südwärts  und  siz.  'Miet-  und Pachtvertrag'  [z.  B.  der  Verlrag,  durch den  die  Schwefelminen  Siziliens  an  einen Unternehmer  gabelloto  verpachtet  wer- den: gewöhnlich  gegen  20''/o  vom  Werte des  gewonnenen  Schwefels,  vgl.  Globus LXVII,  154],  rum.  havalea  'Abgabe, Arbeitsdienst'  [wohl  durch  Kontamination mit  ar.  Jiawäla  'Auftrag,  Bürgschalt, Wechsel',  s.  auch  Löbel  EITAP  52] ;  russ. kabala  'Schuldbrief,  Verschrei bung,  be- sonders zur  Leibeigenschaft',  klruss.  Ä:«- bala  'Verschreibung  zum  Leibeignen', zakabalyty  'zu  seinem  Untertanen  ma- chen'. Mitar.  Art.  ergibt  sich  sp.  alcabala 'Verkaufsgebühr',  pg.alcai^ala  'Eingangs- steuer'. Aus  dem  It.  wurde  serb.  poln. gabela'ZoU,  Steuer'.  —  [Ableitung  auslat. gabulum  <^  ags.  gafol  vom  Vb.  gifan, wie  Diez  Wb  der  rom.  Spr.  150  vorschlug, ist  abzulehnen,  da  lautlich  fast  unmög- lich.] [DE  GREGORIO  in  StGUtH.  Mikl SlEtWb  107.  Bern  SlEtWb  464.  DE  74 u.  75.  Eguilaz  121.  RomForsch  IV,  589. XXII,  629.    ML  6893.
2374:'Wagschale;  alles,  was  hohl  und  rund ist'  [auch  'innere  Handfläche',  vgl.  hier Nr.  990] ;  hieraus  siz.  gaffa  'Eisenstange, die  an  den  beiden  Enden  zurückgebogen ist,  Krampe',  sard.  gaffa,  kat.  sp.  gafa 'Haken',  plr.  'Brillengestell',  frz.  gaffe, pr.  gaf  'Haken'.    [GrSVociSic  237.
===== LAM.txt
4009:chale de Lisbonne ). Le changement de r en n ne ferait
```


## [2026-09-14T01:28:29.559Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3455,3485p' PHN.txt",
 "description": "Pihan châle entry"
}
```


### [2026-09-14T01:28:29.617Z] TOOL RESULT

```
de la Perse, depuis les temps les plus reculés, ou de Kalou-
morts à Yezdédjird, sous le règne duquel les Âi*abes firent la
conquête de la Perse. L'auteur de cette vaste composition , qui
embrasse une période de trois mille six cents ans , est le cé-
lèbre Abou-'lkasem Firdousi, né à Tous, ville du Khorassan, où
il mourut Tan loso de l'ère chrétienne. Dans quelques dic-
tionnaires on trouve schah et shah; cependant il vaut mieux
rendre le {fi par ch, comme cela se fait, du reste, pour châle,
clutrte, diéikh, chérif, etc.
CHAlE, s. m. (p.)
Jlâ [chM] Vêtement de laine plus ou moins fine, dont les
hommes et les femmes en Orient se couvrent la tête, les reins,
ou les épaules. Les châles les plus renommés viennent de l'Inde
et des Etats barbaresques. Voici, d'après le Dietiannaire turc-
français de M. Bianchi, les noms des principales espèces de
châles en Orient : l'^fermâîch, châle rayé avec des franges;
a"" keucheh dâr, avec des palmes aux quatre coins; 3" kiseli dâr,
avec des lisières larges de deux ou trois pouces; b!" tchâr, long
et simple, avec des palmes aux deux bouts; 5^ d'onlouq, long
et broché de fleurs, mais sans palmes; 6"* fériiâous (plume
de paon), châle de couleurs vives; y*' boghtchah, carré avec
une rosace ou bouquet de fleurs au milieu. — C'est vers le108 CHA
comniencGmeut de ce siècle que la mode des châles étrangers
s'est introduite en France; et, depuis ce temps, les tissus de
laine sont parvenus chez nous à un tel degré de perfection, que
les châles dits cachemires français feu\eni aujourd'hui rivaliser
avec ceux de l'Inde. — Schall, donné par plusieurs diction-
naires, ne peut exactement représenter le mot persan.
CHAMEAU, ELLE, subst. (a.)
J^ [djaml, Jjamal ou djémel] chameau, quadrupède ruminant
dont il existe deux races distinctes : la première, originaire du
```


## [2026-09-14T01:28:37.141Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB xusk ===\"; grep -n \"chuşk\\|hušk\\|xušk\\|χušk\\|huška\" HUB.txt | head -10; echo \"=== HUB sud ===\"; grep -n \"süd\\|sūd\" HUB.txt | head -10; echo \"=== CHEUNG sav ===\"; grep -n \"^\\*sau\\|sav-\\|\\*saw\" CHEUNG.txt | head -20",
 "description": "Hübschmann and Cheung"
}
```


### [2026-09-14T01:28:37.273Z] TOOL RESULT

```
=== HUB xusk ===
=== HUB sud ===
=== CHEUNG sav ===
492:*saucé ‘to burn, light", *rai9! / *frait/9 ‘to die, decompose’, *caud / *paud ‘to run’. 
3818:*NWIR: Widely attested: NP sudan/sav- ‘to become; [obs.] go’, Bal. Sut-/ (supplet. 
22171:*saut! ‘to burn, emit flames’ 
22195:*sauc | 339 
22260:*sau ‘to call’ 
22284:*sauH! ‘to rub, wear, whet’ 
22333:*sauH ‘to bulge, swell up, increase’ 
24130:*NWIR: (+ *upa-) ? NP bisudan/bisav- ‘to handle, feel, touch, rub etc.’ (rather from 
24131:*sauH! ?) 
40836:bisüdan/bisav-, 369 
55872:*sauH 
56459:*sauc! 
58382:*sauH!
```


## [2026-09-14T01:28:42.106Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22333,22400p' CHEUNG.txt; echo \"======== hauš\"; grep -n \"\\*hauš\\|\\*haus\\|haoš\" CHEUNG.txt | head -10",
 "description": "Cheung *sauH and *hauš"
}
```


### [2026-09-14T01:28:42.198Z] TOOL RESULT

```
*sauH ‘to bulge, swell up, increase’ 

*AVESTAN: su- (sáuu-) ‘to bulge, swell up, increase’ = Liste: 63 

Fut.: IND. 3sg. YAv. “saoSiiat® (A 4.6); Partic.: pres. pass. YAv. suiiamna- (Y 55.3, Y 70.4, V 4.2, intens. 
YAv. süsouuista- (Aog 19), fut. saosiiant-; Inf: OAv. süidiiai (Y 44.2, Y 49.3); Caus.: pres. INJ. 2sg. 
OAv. sauuaiiö (Y 51.9), SUBJ. 3sg. YAv. sauuaiiat (Yt 13.129) 

*MIDDLE PERSIAN: MMP swd, swwd, BMP swt /sud/ ‘profit, use, advantage’ 
=> DMMPP: 310a 

*KHOTANESE: (+ *fra-) LKh. hasv- ‘to swell’ 2 SGS: 151 

*BACTRIAN: 0000 ‘plenty’ {hapax} = S-W, Bact.: 224 

*NWIR: Bal. sit", si0/si- ‘to swell’, NP süd ‘ gain, profit’ 

*NEIR: Oss. І. sy-var, D. su-var ‘uterus’ || (+ *fra-) Oss. I. resyjyn/resyd, D. 
reesujun/resud ‘to swell’ 

*MISC: (+ *fra-) Orm. Susuk, sras-"ek ‘to swell’ 

*SANSKRIT: sav’ ‘to swell, to become strong, to increase, to prosper’ (RV+) 
= EWAia II: 623 

«PIE *KeuH;- ‘to bulge, swell up’ = LIV: 339 f. | Pok.: 592 ff. 

*IE COGNATES: Gr. коёо ‘I am pregnant’, Gr. к®но‹ (n.) ‘wave’, Lat. cavus ‘hollow’, 
in-ciéns ‘pregnant’, MWelsh cyw (m.) ‘young animal’, OE Aun (m.) ‘young one’. 
*REFERENCES: IIFL I: 409b; Abaev, Slovar’ II: 380 f.; Abaev, Slovar’ III: 213 f.; DKS: 476; Werba 1997: 
320; Shahbakhsh: s.v. si-; Korn 2005: 91, 314, 385 


*säd ‘to cover, protect, shield’ 

*AVESTAN: Y Av. saóaiianti- (f. ?) ‘long trousers ?’ (N 95) 

*MIDDLE PERSIAN: ВМР c'twl /čādur ‘sheet, veil’ (< late Skt.) || (+ *4-) BMP ’s’dk 
/asayag/ ‘shelter’ 

*SOGDIAN: (+ *а-) CSogd. ’s’dty ‘shielded, protected’ || (+ *pati-) SSogd. pts’6(°) 
‘shield’, CSogd. pts’6 ‘shield’ (Schwartz 1967: 141 f.) 

*NWIR: NP cadur ‘veil’ (< late Skt.) 

*NEIR: (+ *4-) Oss. I. asadyn/aseest, D. asadun/asast ‘to become clouded; to cover the 
seeds of the land before sowing; to plant (beans, peas)’ || (+ *upa-) ? Pash. psunai 
‘ambush’ || (+ *pati-) ? Pash. psöl (m.), psald (obl.) ‘ornament, gold or silver 
jewelry’ 


342 *séand (*skand) 


*SANSKRIT: chad ‘to cover, to conceal’ (RV+), chattra (n.) ‘parasol’ (Br.+) 
= EWAia I: 554 

© The root is exclusively Ir. with no certain IE cognates. The often cited 
comparison to the isolated form OE heteru ‘clothes’ can hardly be used for 
etymological purposes. 

*PIE — => LIV: 546 | Pok.: 919 

*REFERENCES: EVP: 60; Abaev, Slovar’ I: 76; Werba 1997: 185; Lubotsky 2001: 40; NEVP: 66 


*stand (*skand) ‘to break, cleave’ 

======== hauš
```


## [2026-09-14T01:28:53.137Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"savah-\\|sauuah\\|'Nutzen, Heil'\\|savar\" BRT.txt | head -10; echo \"=== sav 1 ===\"; grep -n \"nützen, fördern\\|1sav-\\|sav-  \" BRT.txt | head -10",
 "description": "Bartholomae sav-/savah-"
}
```


### [2026-09-14T01:28:53.214Z] TOOL RESULT

```
6255:mit  'ahura-  (sd.,  2  b)  'der  des  Rechtes wahrende,  gerechte  Gerichtsheir,  Herr'; dsfitarytä  .  .  ka  'sava^l  aAurB  (sd.)  yS .  . ^■53-9i  "^  ya'hH  Swd  z/inslim  uz^mShi (sd.)  ^aa^ansi  sp»Ht>m  ahunm  'savatum Y.  46. 9 ;  —  at  hl  ayä  frwi'aritä  (sd.)  västrlm ahyai  fsuyantim  akurgm  'savarum  Y.  j/. 10.  b)  im  YHapL:  daidl  at  mrqi iiiazdä  ahurä  °iäunö  (AP.)  asaänavAs .  . \.4o,y,  —  a%ä  . .  Ryäma  , ,  °savanB  Y. 40.4;  —  'läunqm  . ,  urunB . .  kudBsäta- nqmlu  narqmcä  nairiiiqmla  Y.  jp.  2 ;  — '{aunqm  fravail!  narqmcä  näirlnamcä  Y. .57- 3-  c)   i"'   jAw.    (unvollständig):
6260:—  Aätqm,^  arthuiqm  ..büiyantqm  'iaonqm Yt.  13.21;  —  ' savarum   mainyaomca  gai-
6263:äfaiÄ  Y.  7<?.2o; —  vahilt?m  akßm  'Saonqm raocaahpm  (Stverz.)  Y.  (J.19USW.;  —  xshätä 'saotiatn  urvänS  pärayänti  .  ,  avt  garö nrnaium.  V,/(),33;  *Y.  2.4,  *42.4;  —  kaur- TtUa  am^nläta  ySi  sis  mlzd?m  'saonam parSMsH  jasMiqm  Yt.  J.  25;  —  vJspim 'iavansfH  vahiltjm  ä  oAüm  ä.baraUi'S.24; — iäbm  *dä^aifi  urvqtam  'saonS  *irfn'^3- naht  F.  24.;  *_J5;  —  vis/ipm  "iavafum  .  . kvavayarsÄ^m  jas>nt»m  paiti.baraAi  Y.55. 4;  —  t3  ahmt  nm3ne ]amy3r?? yä  'saenqtn xtnstatca  aSayasca  Y.  60. 2;  —  ya^raca xihaa  'sava  Yt7y.36;  25;  —  -savamm ti  'iaonat  äfyeihyai  (sd.)  mraomi'^.-ji.\y, —  visp»m  'iavarum  vlspäi  'saone  para.- cinasti  Y.20.2;  a';  —  vahistim  'iovamm vaiüitäi  °iaone  Y-2/.4;  —  tumas?  tS dä'^rö  baxt»tn  vahistäi  -saone  anazq^äi 'sttone  V.  2M;  —  tumd  aAurSt  mazdäi tvms  atnsiaiikyS  spmtalibyS  rrnnS  anyailqm (sd)  'saonqm  V./().2s;  33.  Yt7.3o;  '— yähaZa  zhayenU  °Iaone  ahm  anasti  Y.  20. 3;  YL/J.  24;  —  amamm  ..  yas»  %ws  .. ynaite  6arö.taohrS  'sava  "das  Haus  des Gläubigen,  der  zu  dir  betet .  ."  Yt  /0.30; 56;  —  •savaram  vahistsmea  avasöjcla- 'inmca  Y.  ig.^a;  —  nSit  'savarum  aint^tii (sd.)  ästarayei/i  P.  12;  ^N.JOj?";  —  aipi.- Pänrnnäi  ,  .  'saone  V.S.ioj;  —  näämnäi (i&.)'säone'V .g.^o;  —  'iavanum  makrka%äi Y.  79. 1 2 ;  —  kaaa  nS  '/aum  agats  .  .  V. '5-  3  ' ;  Y.  7/.  1 6 ;  —  "iavansm  manaspaoiryS V.  19. 19  {?);  —  sava  'SavabyS  yazatnaide Vr.i^j.i;    Y.77.6'.  a)    von    nament-
6281:—  r3laca  vaauhi  .  .  °saane  (VS.)  V.  /(?. 19,  Vytjö;  S,  1.5,  2.5;  —  raziflam  astim ..  "saonJm  Yt.16.1,  4;  o,  20;  —  airyama- mm  iitm  '^avan^m  Vr.  24-  3 ;  —  kaomS °^ava  Y.p.a';  10,14;  —  haoma  °lava (als  Vok.)"'  duraosa  Y.  j/.  10;  —  rasmiö °lilum  Yt  J2. 7;  9; —  sraohm  .  .  '/avarum Y-  57-  2i  33,  Yt.  II. T,  —  Aaurvat3t>m 'savaram''^  asahe  ratüm  Y.  71.  12;  — am^ntät^m  "savanpm'i^  asahe  ratüm  Y.7J, 13;  —  ahura  müra  .  .  •s'avana  (AD.) Y.  2. 1 1 ;  YL  70. 14s;  —  ahuraHbya  miitraei- iya  '/avanaäiya  Y,  j.  11,  a)  bes.  von Ahura Mazääh:  3  äim  tä  vaca  rämayal ahurS  masdä  'sava  alavansm  zarä^ulinm V.5.2I;  jp.15  (statt  Akk.),  Y.7/.4,  5,  57. 24,  Yt.S.i,  11.1%  12.4,  16.3,  Yt/0.89, 7J.  14,  15;  —  ahur)m  mazdqm  'iavamm aiahe  ratüm  Y.2,2,    t6.\,  ^5.1,  7/.2,  4;
6330:•  j.  aäa'savah-  m.  EN.  eines  Gläubigen: 'iiarjks  alaonS  Yt.  13. 1 1 6.
11968:•  j.  tanu.parfl^a-  Adj.  'des  Leib  ver- wirkt, dem  Gericht  verfallen  ist'*',  Bezeich- nung für  den,  der  ein  mit  200  upäzana (sd.)"*'  bedrohtes  Vergehen  begangen hat  und  (bis  zu  dessen  -Sühne)  eo  ipso exkommunizirt  ist :  vispe  anasavarw  yö -ä?  (NP-)'>  N.iÖ.-iZ;  —  dahmanqm  .. dafvayasnanqm  .  .  -)ianqm  atanu.p^rf- %anqm  V./ö.öz;  N.j*/;  —  datvayasium va  °^?m  vä  "einen  Ungläubigen  oder einen,  der  im  Kirchenbann  ist"  N.  roj;  — dazvayasnake  vü  '^aAe  v3  N.  11 ;  *P.  10;  — (kat)  nä  daivayamäi  vä  °äai  va  ''aihryäi (sd.)  ^casaite'ü.iy; —  kat  na  *dalvayasnäi vä  '^äi  vä  gSui  dhäitya  (sd.)  ästrydti N.  l8\  —  kat  nä  dafvayasnät  vä  '%äl  (vä) af^rapalSit  {sd.)  pairi  *aiwya»Aat  Ü.lö; —  yi  '^aAe  aparadiamnaAe  (sd.)  aja- yaunia  .  .  ya  Aaca  da!sayasnaeiiyS  .  . N.  54.  a)  bes.  im  Gegensatz  zu  dahma- (sd.):  ciial  al^qm  tipa.mqnay»n  .  ,  cvai dahmartqm  ifea/  °'^anqm  V.  72.  i;  i;  — "^"Jö"'  zaota  daAma  upa.sraotärS  (sd.) yezi  dim  °%9m  *vToarj  .  .  yezi  äat  äim n^il  '%3m  *viaar>  N.J5;  3!)';  —  daAmS zaota  '%a  upajraotärB  yai  dii '•'^H  (AP.)'* va^ia  . .  "der  Z.  ist  Gemeinder,  die  U. sind  im  Bann;  wenn  er  weiss,  dass  sie  im Bann  sind  .  ."  N.  ji?;  3K
14187:nä^iü  ya'Öat  aiwiat  jaymat  asavaram mahrka%!ai  Ytifj.  12*';  2. 11',  j.  17^;  — nlLnasama  saoyants  *'ußm  Aa'ia  (sd.) >il/.na/äma  ya^a  Alm  janama  Y,6i.^^';-~ 'uxs' (ah  Vok.)  nase  dafvff.äSire  StB.  3; j3;  —  iu^a  Ali'  aam  k»r>navani  haca *avatiAai  °ujat  Aaca  duida  anra  mainyö y.  ig.  13;  —  paitiHatSe  bivnrS.cihrayä 'ujB  Yi.  13.12%  —  noit  sl  eis  a^Aa •uje  nyäsaite  (sd.)  ,  .  Aa  °uxs  as.aaßita anhat  .  .  yat  Aa  'uxs  aiiti  mfraxvl  FrW. 8. 1  f.  g)  in  kollektivem  Sinn,  sva,  ^ütfua (Plur.)*>:  snai^if/a  varvias/a  .  .  pairi mainyaoyat  'ujat  *varmyayaatca  *drve.- i^yat  Yt.13.11;  —  mahrS  spniS  main- yfvTm  'ußm  tiiiiairi/töYt.ii.s.  Undeut- lich: °uja  Vyt  2p;  —  'u/j  Vyt  25,  3^;  — *'ußmYi.4.$^;  —  •«;>  V.  20.  8.  \Y.g. 17,  20:  lies  drußin.vanS.  —  Y.jy.  6,  »St: ist  drBjS  und  hffis  püa  als  spätere  Zutat zu  streichen;  s.  zu  "Asi/.}
16806:tarn  arstim  barai/iYt.  10.21.  5) '(davon- 1  nanbyB  .  .  V.  77.  4;  —  ydka  ..  am?r7xtim tragen  sva.)  gewinnen;  empfangen':  yänä  avaiaräni  ..  Uta  az?m  apaiaräni  ..  sk- (sd.)  baraiti  astavB  va  .  .  m^nyahe  Yt.  o^m'a  tars/amca  haca  maata  dämaiyS  Yt 14.3^.  a)  mit  refl.  Dat:  paourva  ?ü  g.^i-;  10*; — ya  haca  daevayasnai^yü . . fumS  baraiti  "zuerst  gewinnt  er  sich  .  ."  apa.bara{^S2ih.)'^^  aya  ratit/H/"w3sinajk Yt  14.36.  b)  mit  Abi.:  iahmät  .  .  1  den  D.  ..weggenommen  hat,  damit  wird Aar»hr?m  barUi  "von  wem . .  soll  sie  Pflege  man  r."  N.  ^4;  —  mt^ram  . .  yS  nar^m  apa empfangen?"  V. y,  17;  16.  6)  'halten,!  qxanhai  baraiti  ". ,  aus  der  Not  (fortträgt pflegen,  behandehi  ab -';  die  Bestimmung '  sva.)  befreit"  YtJo.az;  aaf.*.  b)  mit erfolgt  a)  durch  praed.  Akk,:  \avam'G^vi.:  yS  daii^hSus  . .  apa  v^n%rajtum **uiaratam  abaram  "den  hab  ich  gut  ge- .  iaz-fl///  Yt  70.27;  —  «/«*  aeiqm  bärvä halten  (behandelt)"  Bh.  /.  8,  4-  13;  — ^aojd  .  .  barahi  Yt/0,a3.  c)  mitDat: in  pass.  Wendung:  *driyümca  drJvJmca'kahmäi  xiäimm  .  .  paiti.da'häni  ..  koA- ara%wyS.b?r3te  (sd.)  barimne  (ADf.) "' !  mä/  xi^dinm  .  .  apaiaräni  Yt  10.  109— P.26.  b)  durch  ein  Absolutiv  (sd.)  zuliii.  d)  mit  enkl.  Gen.-Dat  desPron.: ^bar-.  ys  vohu.b3r»tqm  baraite  milir?m  Yt  \apa  hl  vastra  baraym  V.5. 49;  —  ku%a 13. 18;  —  yS  nS  hub?r3tqtn  barst  Yt  1$. '  te  aam  *apavaräni''''>  navaca  yaskS . .  V. 40;  —  yö  nä  his  kubfnta  *barat  Yt  22,6.  a)  'Jemanden  bringen  um  — ', y-  >8;  —  ya'ha  duibirmts  *barailt'**  (in  mit  dopp,  Akk.'**:  jvö  . .  drvä  .  .  nar^m pass.  Sinn)  Yt/0. 48;  —  ya^a  Aub^ntS  asavarum  hanhus  }fan'i:ahaa  .  .  apa.- *baraite"^  (in  pass.  Sinn,  näml.  mthrö)'  baraiti  "..bringt  (er)  den  Gläubigen  um Yt/0,  112.  7)    mit   AS.    vääirt    'die  j  die  Nutzniessung  . ."  V.5.  38.         2)  'ab-
19346:•  j.  "nmänya-  Adj.  'dem  Haus  an-,  zu- gehörig, Haus-':  kaya  ratavSf  'yS  vTsyS zantumü  dähyumS  tarakuilrS  pu:^e  Y. /(>.  18;  —  kaya  ai^hh  (näml  rajüif) ratavsi  'yasla  vJsyas^a  zantumasca  (sd.)  . . Y.  ig.  18.  A)  m.  Name  der  Gottheit  der Häuser*':  'nrmca  asavaram  aiaht  ratum G.5.6;  —  'nyche  raSa'^G.5,6;  —  btnjJm 'nXmla  Y.  2.  7;   —  hryjyäi  'yäila  Y. /.  7.
19806:maitilla  altmcS  . .  °nasäi  vohü  otl^rsm^a Y.33.  11; — yada  aiim  ssvlm  (sd.)  atsktn masdäsia  ahurBahS  aüca  ärmaitfvahütä iiasa  (sd.)  'nanha  (als  Vok.)  '>  .  .  Y.  31. 4;  —  mazdä  dadät  ahurö  haurvatß  amart- tatas^a  .  .  asaÄya^  xsahrahya  sard  (sd.) vanhfus  vazdvar!  'naahd  Y.31.  21;  — US  mSi  lizarfrva  ahura  ärmaitl  tntsim dasvä . .  vanthuya  zavö  adä  a/a  hazS  Sma- vat  voha  'nanha  *fspratüm  Y.33. 12;  — ia  vS  mazda  .  .  ahura  al'ai  yecä  taibyaca armaite  dStSa  mei  ifföis' (s±,)  xsä'hnM xsmakfm  voha  "nanha  . ,  daidl  savar^hd Y.57.  2;  —  va^lßul  xratüm  °naahs  ya xSmvJ^a gSusla  *urvqmmY.28.\:, — yahml spmta  äaia  mainya  urvaisl  JasB  matdä xsa%ra  ahmJ  (Sp.  8  o.)  voha  'naaha  Y. 43-^',  —  ü>  YHapt:  ahitrsm  matdqm  .. aäm  at  vahistom  . .  vohuia  °nS  yazamaidt vohula  xsa%r3m  . .  Y.jj.  1—5.  U)  im jAvr.:  vohu  'nS  amihm  spsnttm  S.  2.  j; Y.76'.3,  G.j.s;  —  us>histat  vohu 'nS  Aaca gätvB  zaranyBJcTrttdY.  z?.  31;  31,  Vyt5/;
=== sav 1 ===
7446:•  j.,  g.  asav-  Adj.  'schnell,  rasch':  yä (mi^rs)  'sutiqm  °sus  Yt  10.  65;  —  srao- f^m..laxmym  "jäot  Y.57.1 1;  —  aurvanfym ..yS  °sui  asti  uzgasts  Yt5.i3i;  —  Aqm.- varfittm  . .  yä  saot  *äsyayä  Vr.  7.  3 ;  — buyät  -suua  asps  dtnzrasca  *vais  Yt  13. 52;  —  aspatfks  . .  °savö  Ytij.  12;  — i!  väiäi  dvqnmaibyasca  (sd.)  yaog^t  'sa (ASn.)  sva. '  'die  Schnelligkeit'  Y.  44, 4,  a)  ASn.  'SU  als  Adv.  'cito':  dayä ml  .  .  -SU  Y./i2.4i;  F.  7.
7456:Superl.  zu  äsav-  Adj.    —    ai.  aüflia-  Adj.  —
7841:•  j.  i^sav-  m.  'Schoss,  Zweig*  der  Haoma- pfianze:  ^ävaiitJ  alte  'sai'S  arihin  "wie gross  sollen  die  Zweige  sein?"  N.  to8;  — havamm  (sd.)  . .  yd  'sus  (AP.)  hangmr- vayäti  Y.jo.i.
7979:•  j.  isav-  Adj.  'frostig,  eisig";  pasia  "saos Z3mö  aiwi.gaitTm  "nach  Eintritt  des  eisigen Winters"  V.9.6.
9286:•  j.  karatö.d^sav-  m.  Name  des  Hahns:
9290:(d.  i.  verwundend)'.  —  "dqsav-  Adj-,  lum  >i.
9383:*raoi'yttm  (sd.)  hixtayal'a  HayaSca  V.  d.t;  •  g-  (.  j-)  tasav-  Adj.  Tdein,  gering':  yS  vä
13660:A  hyiin  53.  PeRMOK  Wurielerw   i54,  .59.  ^  >      '""  ^ie  strittigen  Wörter  a Vii.:  pa  frfpiin.  —  •)  iEl  s.  Gds,  BB.  /*  13.   •  j-  dujTO.va-   f.  EN.   der  Frau  Pouru- .  j.  disav-  m.  Name  eines  nächtlichen  t ^^^-^   ^^    ^^fV  /«^f**^";    "'^ Raubtieres:/«ifJÄ?(nämL  ist  der  Hund)  l'!"^"'{''"   »"'"^'"fr''*^  (sd-)    mä  pouru- ya>a  'su/V.ij.at,  473;  —  atH  SiAami""/"^  '7  2^'\F^^^t>      ■  ^^,-
14242:•  '}.  drvö.pasav-  Adj.  (auch  fem.)  'das Kleinvieh  gesund  erhaltend':  drväspqm.. 'svqm  (ASf.)''  drvSjtaorqm  Yt.p.  i.
15812:•  j.  parasav-  f.  'Rippe':  *°jz'/ (ND.)"  "die beiderseitigen  Rippen"  F.^  g.
```


## [2026-09-14T01:29:02.365Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1561\\|1567\" BRT.txt | head -10",
 "description": "Find BRT columns 1561/1567"
}
```


### [2026-09-14T01:29:02.420Z] TOOL RESULT

```
26920:KompE. ;  Ableit.  —  It.  *ipä;  worin  ar.  *ij^ -  lu  aea/;  Sp.  1561  -  und  *sphä-  -  s.  ispä-  - znsammengef allen  sein  können;  t.  zn  ipaya- %ra-.  —  iPB. !  ätäHih,  Sü.t  samädkänam.  — •>  Die  Meinung,  es  mDsse  des  Melrnins  hilbei jwf  •  statt  sf  gelesen  werden  -  Bthu  Gi^is  ' 9  -,  was  die  Herleitong  ans  ar.  *j^ilä-  aus- schlösse, ist  irrig.
```


## [2026-09-14T01:29:07.115Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nützen\" BRT.txt | head -20",
 "description": "Bartholomae 'nützen'"
}
```


### [2026-09-14T01:29:07.173Z] TOOL RESULT

```
15007:•  j.  paitinqm.  gaodana-  Adj.  'verschiedene Schüsseln,  Näpfe  benützend,  aus  ver- schiedenen Schüsseln  trinkend':  paitinam.- i^ariia  (sd.)  'na  (ND.)  N.  64.
26010:•  j-  (1  g)  sav-  V.  'nützen',  Praes.  17 (Fut.)  saoiya-,  25  (Pass.)  suya-,  30  (Her.) sävaya-.  —  Inf.  süidysi,  styg,  savayS.  S. noch  spaya%ra-.
26011:'nützen,  Nutzen  schaffen',  mit  Akk.  des wem?:  ya%a  väts  .  .  vTsptm  ahüm  .,/rä- la/icä  var3%atUa  saosyanti{ila.Xl  Sing.)& A.  4.  6;  —  ys  daitihave  hu.vaxsai  frdh>m- nake  vanltimnahe  .  .  suyamnahe  N.4-  2 Gl.  a)  insbes.  'den  Nutzen,  den  Vor- teil schaffen,  erwirken',  d.  i.  das  gute  Loos im  andern  Leben'';  wua^a  sao^qs  (sd.) ya%a  vispftn  akum  astvanhm  sävayät  Yt, y"9i  —  Aarp'hrai  asahe  gaihanqm suyaiitnanqmla  saosyantqmca  "um  zu wachen  . .  über  die,  die  den  Nutzen  be- kommen und  die  ihn  schaffen  werden" Y.55. 3;  — y^a  vS  saofyatttS  dahyunqm suyamna  väcim  ^barmti  Y,  yo.  4;  — sttoSyant-  s.  auch  bes. np.  tgl.  iSd  'Nutien'').  —  PQ.  (lu  Y,  55): sütan  u  nilömattdan,  (m  Y./O);  sütömand,  (lu V.  4);  süßiüt  (3.Sg.;^  erl.:  kui  tut  palas  kuneU
26271:S3vin-    Adj.  'nützend':    vmnjaoka
26398:•  g-  suye  Inf.  'zu  nützen,  den  (ewigen) Nutzen  zu  schaffen':  sraotB  säsnä  fsSttghyS (sd.)  f '  tastü  Y.  49. 9.
```


## [2026-09-14T01:29:13.913Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=26020 && NR<=26120' BRT.txt | grep -n -i \"savah\\|'savah\\|Heil\\|Nutzen\" | head -20; echo \"---\"; grep -n \"savah-\\s*n\\.\\|savah- n\\.\" BRT.txt | head",
 "description": "Bartholomae savah-"
}
```


### [2026-09-14T01:29:14.868Z] TOOL RESULT

```
6:Nutzen  (im  andern  I.«ben)  zu  schaffen':
13:•  j.  sava'vant-  Adj,  'der  den  Nutzen, Vorteil  hat';  'va  "d^i  Hi  att^  'S. 33.
15:•  j.,  g.  'aavah-  n.  'Nutzen,  Vorteil';  us na  aiiihai  vise  JamyJi  asimca  xsa%r)mca 'vasca  j^atfnascia  ,  .\.6o.2;  —  :^ar>nS.. 'vS  mazdatähm  Y.2. 14,8.2. 9; — a^arnta- nh5 'va>3ks  mazdahatake  Y.i.  14,  Ny.5.  5;
16:—  ahe  nmanahi  Jradäkäi  ahe  nmänahe 'vatths^''  Vr. //.  13.  a)  gAw.  nur  vom 'ewigen  Nutzen'  im  andern  Leben  (s.  sava-): yS  nä  fnzBs  'vank^  pa%ö  sJsSii  (sd.)  Y. 43.y,  —  Jr-a' (Sp.  185  o.)  zJ  kudanks vTspais  mazda  xsmavasa  'vS  Y.J4-3;  —
19:•  j.  'savah-  m.  EN.  eines  Gläubigen: nljarahe  'varghs  alaota  YL  j_y.  101.
21:•  j.  savahi-  (n.)  Name  des  im  Osten  ge- legenen Erdteils  (iarfyar-,  sd.):  avi  ar>- zahi  ''<4i{AD,)  Yt. /o.  15;  133,  *V.  ip.  39''; —  upa  karhan  yat  'hi  YLJ2. 10;  — anzahibyS  (sd.)  'hibyS  fradata/suiiyS  .  . Vr.  10. 1.
25:savahvant-
26:•  j.  savah'vant-  Adj.  (fem.  'vaitl-)  'den ' Nuuen,  Vorteil  schaffend  dir  -'  {Akk.)'>-. nisbayani  uyrä  *alaonqm  fravalayS  vispk  l ääman  'varmAatti/ (KP{.)  ". .  die  Fr.  .  ^\ die  allen  Wesen  den  Nutzen  schaffen"  \ V.  ig.  37.
30:•  j.  savö.gae9-ä- Adj. 'derdenLebewesen, dem  lebendigen  Besitz,  Haus  und  Hof, Hab  und  Gut  Nutzen  schatil':  arltätsm /rääal^al'iqm  vandai^atham  *%qm  Vr,
---
```


## [2026-09-14T01:29:24.200Z] TOOL CALL #61: Bash

```json
{
 "command": "for u in \"https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc/getword.php?key=%C5%9Bavala\" \"https://abadis.ir/fatofa/%D8%AE%D8%B4%DA%A9/\" \"https://abadis.ir/fatofa/%D8%B4%D8%A7%D9%84/\"; do echo \"##### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 431: MW savala / Mo'in xošk / Mo'in šâl\" 2>&1 | tail -3; done",
 "description": "Fetch MW and abadis"
}
```


### [2026-09-14T01:29:30.275Z] TOOL RESULT

```
##### https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc/getword.php?key=%C5%9Bavala
/home/sfmqrb/git/rishe/data/verification/sources/web/c8e39ed44a57e4e7.txt
##### https://abadis.ir/fatofa/%D8%AE%D8%B4%DA%A9/
/home/sfmqrb/git/rishe/data/verification/sources/web/f1b2977fd4eec5a4.txt
##### https://abadis.ir/fatofa/%D8%B4%D8%A7%D9%84/
/home/sfmqrb/git/rishe/data/verification/sources/web/45d621b1de2b216c.txt
```


## [2026-09-14T01:29:33.315Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== MW ===\"; sed -n '1,40p' c8e39ed44a57e4e7.txt; echo \"=== abadis xošk (moein) ===\"; grep -n -i -A6 \"معین\" f1b2977fd4eec5a4.txt | head -40",
 "description": "Read MW and abadis"
}
```


### [2026-09-14T01:29:33.455Z] TOOL RESULT

```
=== MW ===
URL: https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc/getword.php?key=%C5%9Bavala
FETCHED: 2026-09-14T01:29:26Z
STATUS: 200
TITLE: 

not found: 'śavala' (slp1 = śavala)=== abadis xošk (moein) ===
62: فرهنگ معین
63-
64- دماغ ( ~. دِ ) (ص مر. ) اندوهگین ، غمناک .
65- (خُ ) [ په . ] (ص . ) ۱ - بدون رطوبت و نم . ۲ - پژمرده . ۳ - متعصب ، بدون انعطاف و نرمی . ۴ - خالی از سبزه و گیاه . ۵ - آن چه که درونش آب نباشد، بی آب . ۶ - بدون ترشح طبیعی . ، ~ و تر با هم سوختن کنایه از: گناهکار و بی گناه به یکسان مجازات شدن . 
66-
67- فرهنگ عمید
68-
--
260: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
261-
262- لینک ها 
263-
264- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
265-
266- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است.
```


## [2026-09-14T01:29:39.164Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -A8 \"فرهنگ معین\" 45d621b1de2b216c.txt | head -30",
 "description": "abadis Mo'in for شال"
}
```


### [2026-09-14T01:29:39.236Z] TOOL RESULT

```
35: فرهنگ معین
36-
37- (اِ. ) نوعی پارچة ساده یا گلدار که از پشم یا کرک بافند. 
38-
39- فرهنگ عمید
40-
41- ۱. نوعی پارچۀ ساده یا گل دار که از پشم یا کرک بافته می شود. &delta، شال کرمانی و شال کشمیری معروف است.
42-۲. بالاپوشی که از پارچۀ پشمی خشن می دوزند و کشاورزان به تن می کنند.
43-۳. پارچه ای دراز و کم پهنا که دور کمر یا سر می بندند. 
--
271: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
272-
273- لینک ها 
274-
275- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
276-
277- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
278-
279- © 2006-2026 abadis.ir
```


## [2026-09-14T01:29:41.281Z] TOOL CALL #64: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc/getword.php?key=%C5%9Babala\" --note \"page 431: MW sabala/savala 'variegated'\" 2>&1 | tail -2",
 "description": "MW śabala"
}
```


### [2026-09-14T01:29:42.857Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/729933bc6ecc2e55.txt
```


## [2026-09-14T01:29:45.131Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,30p' 729933bc6ecc2e55.txt",
 "description": "MW śabala"
}
```


### [2026-09-14T01:29:45.185Z] TOOL RESULT

```
URL: https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc/getword.php?key=%C5%9Babala
FETCHED: 2026-09-14T01:29:42Z
STATUS: 200
TITLE: 

not found: 'śabala' (slp1 = śabala)
```


## [2026-09-14T01:29:48.909Z] TOOL CALL #66: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc/getword.php?key=Sabala\" --note \"page 431: MW sabala 'variegated'\" 2>&1 | tail -2; echo; cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,40p' $(ls -t | head -1)",
 "description": "MW Sabala slp1"
}
```


### [2026-09-14T01:29:50.854Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2cdf72774bc59d71.txt

URL: https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc/getword.php?key=Sabala
FETCHED: 2026-09-14T01:29:50Z
STATUS: 200
TITLE: 

Sabala 

 (H1) [Printed book page 1052 ,2] 

 Sabala mf( A , or I )n. (also written Savala ; cf. Sabara above) variegated, brindled, dappled, spotted (in RV. x, 14, 10 applied to the two four-eyed watch-dogs of Yama ), RV. &c. &c.
 [ ID=212623 ] 

 variegated by i.e. mixed or provided or filled with ( instr. or comp. ), Kāv. ; Sarvad. [ ID=212624 ] 

 disfigured, disturbed, BhP. (see comp. ) [ ID=212625 ] 

 Sabala m. a variegated colour, W. [ ID=212626 ] 

 N. of a serpent-demon, MBh. [ ID=212627 ] 

 of a man ( v.l. for Sabara ), Cat. [ ID=212628 ] 

 Sabala ( A ) or ( I ) f. , see below [ ID=212629 ] 

 Sabala n. water ( cf. Sabara ), W. [ ID=212630 ] 

 a partic. religious observance of the Buddhists , ib. [ ID=212631 ]
```


## [2026-09-14T01:30:00.829Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD shawl ===\"; grep -n -i \"shawl, n\" FSD_vol4.txt | head -5; grep -n \"Shawl\" FSD_vol4.txt | head -5; echo \"=== WEB austerity ===\"; grep -n -i \"austerity\\|austere\" WEB_vol1.txt | head -5",
 "description": "Funk&Wagnalls shawl; Webster austere"
}
```


### [2026-09-14T01:30:00.942Z] TOOL RESULT

```
=== FSD shawl ===
8712:Shawls  are  made  of  wool,  silk,  cotton,  hair,  or  a   mixture of  fibers,  or  of  lace  crapo,  etc  The  embroidered  shawls  of Cashmere  wore  the  first  worn  In  Europe,  and  tlnlr  designs have  been  Imitated  In  woven  shawls  Other  patterns  aro borrowed  from  the  Scottish  tartan  Shawis  are  now  worn by  women  except  In  the  East,  where  they  are  used  by  both sexes  Shawls  are  generally  named  from  the  place  of  their manufacture,  as  Cishmcre,  Indian,  Paisley,  Persian, etc  ,   or  from  the  material  of  which  they  are  made,  as  cam- el’s hair,  lace,  silk,  etc  I<  Per  shfll,  shawl )   —   shawP* dance",  n   An  Oriental  dance  in  which  the  dancer  waves a   scarf —   s.*goat,  n   The  Cashmere  goat  — s   loom,  n A   loom  for  figure-weaving  — s   *mantle,  n   A   shawl  made Into  a   sleeveless  cloak  for  womens  wear  — s.*maferlal,  n A   soft  dress-goods  figured  with  Oriental  designs  — s   *pat- tern,  n   A   v   arlegated  pattern  resembling  that  of  an  Orien- tal shawl  —   s   spin,  n   A   large  pin  or  brooch  used  for  fast- ening a   shawl  or  scarf  —   s   *s(rap,  n   A   device  for  carrying shawls,  parcels,  etc  ,   usually  consisting  of  two  leather  straps joined  by  a   transverse  band  on  which  a   handle  Is  fastened
8714:shawld,  pp  Shawled  8   S
=== WEB austerity ===
11703:right ascension; in astronomy, the are of the equator intercepted between the first point of Aries and that point of the equator which comes to the meridian with the sun or star. relating to ascension; as- cending or rising up. 2 ascensional difference; in astronomy, the dif- ference between the right and oblique ascen- sion of the same point on the surface of the sphere. ae as:cen/sive, a. 1. rising. 2. causing to rise. i; $ 3. in grammar. intensive; increasing the force; augmentative. [Rare.] ascent’, n. [L. ascensus, from ascendere, to ascend. ] > ; 1. the act of rising; rise; a mounting up- ward; as, the ascent oi vapors from the earth, 2. a going up; climbing. ot enie hill, or high place. [Obs.] 4. the amount of upward slope or elevation; as, that road has an ascent of five degrees. 5. acelivity; the rise of a hill; as, a steep ascent. 3 6. an advancement, as in rank, popularity, etc. 7. a going back in time or genealogy. as-cér-tain’, v.t.; ascertained, ptl., pp.; ascer- taining, ppr. [OFr. acertainer; L. ad, to, and certus, xed.) 3 1. to make certain; to define by removing obscurity or ambiguity; to determine. The divine law ascertains the truth. —Hooker. 2. to make certain by trial, examination, or experiment, so as to know what was before unknown; as, to ascertain the purity of a metal. 3. to make certain in the mind. [Archaic.] 4. to fix; to establish with certainty; to ren- der invariable, and not subject to will. [Obs.] The mildness and precision of their laws as- cerlained the rule and measure of taxation. — Gibbon. Syn.—find out, discover, determine, detect, discern, learn. as-cér-tain/a-ble, a. capable of being ascer- tained. as-cér-tain’a-ble-ness, n. the quality or state of being ascertainable. as-cér-tain’a-bly, adv. manner or condition. as-cér-tain/’ér, n. one who ascertains, or makes certain. as-cér-tain’ment, z. an ascertaining or being ascertained, as-ces/sin:cy, n., same as acescency. as-ces/sant, a. same as acescent. as-cet’ic, a. (Gr. askélikos, exercised, from as- kein, to exercise.] of or characteristic of as- cetics or asceticism; rigid; severe; austere. as-cet/ic, n. 1. one who lives a life of con- templation and rigorous self-denial for reli- gious purposes. . anyone who lives with strict self-disci- pline and abstinence. as-cet’/i-cal-ly, adv. 1. in an ascetic manner. 2. by means of asceticism. as-cet/i-cism, 7. 1. the practices or way of life of an ascetic; systematic self-denial for some ideal, 2. the religious doctrine that one can reach a higher spiritual state by rigorous self-dis- cipline and self-denial. as’cham, n. [after Roger Ascham (1515~1568), Eng. writer.] a receptacle for archery imple- ments. as/cl, 2., pl. of ascus. as/ciAin (ash’yan), n. [L. ascius, shadowless; Gr. askios; a priv., and skia, a shadow.] a person who casts no shadow at noon: said of the inhabitants of the Torrid Zone where the sun is vertical at noon for a few days a year. As-cid’i-a, n.pl. (Gr. askidion, a little bottle, from askos, a leather bag, a bottle.| an order of Tunicata, or sea squirts; ascidians. They are found at low tide on beaches, and are dredged from deep water attached to stones, shells, and fixed objects. They are usually sac-shaped, with a sonen outer covering or tunic. A single mass of ganglion represenis the nervous system, this mass being placed between the two openings of the body. Male and female reproductive organs exist in cach specimen. They may be single or simple, social, or compound. In social ascidians, the peduncles of a number of individuals are united into a common tubular stem. with a partial, common circulation of blood. as-cid/i-a, n., pl, of ascidium, aa lala) ©, e in te Aside s^. of the Ascidia; a sea squirt.
12659:ad, to, and stringere, to bind, strain.} 1. to bind fast; to constrict; to contract; to cause (parts) to draw together. ‘ae 2. to bind by obligation. [Obs. as-trin’/gen-cy, 7.; pl, as-trin’gen-cies, the quality of being astringent; that quality in medicines by which soft or relaxed parts of the body are contracted; as, the astringency of acids or bitters; hence, also, harshness or austerity in disposition; as, the astringencies of character or human nature. : as:trin’gent, a. [L. asiringens, ppr. of astrin- gere, to contract, draw close; ad, to, and strin- gere, to draw, bind.] ; 1. that contracts body tissue and blood vessels, checking the flow of blood; styptic. 2. causing to shrink or contract. 3. austere, harsh, or stern. as-trin’ġent, 7. an astringent substance, drug,
13425:Augustinian hermits; an order of austere mendicant friars originally hermits, who were congregated into a body in 1265: also called Austin friars.
13546:austerity —
13582:aus-tere’, a. [ME. austere, OFr. austere; austerus, harsh; Gr. austéros, dry, harsh.]_
```


## [2026-09-14T01:30:02.309Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"خشک\" ARY_pages.txt | head -10; echo \"=== sud ===\"; grep -n \"سود\" ARY_pages.txt | head -10; echo \"=== shal ===\"; grep -n \"شال\" ARY_pages.txt | head -10",
 "description": "Aryanpur lookups"
}
```


### [2026-09-14T01:30:02.397Z] TOOL RESULT

```
2789:این باشد که در اثر خشکه شدن آب و هواء اين جانور معدوم شده و لذا نام آن هم از ییاد رفته است. واژه‌ی
5797:چم اين واژه در زبان‌های یونانی و رومانس (لاتین و زبان‌های ناشی از آن): خشکه» خشکیدن,
7172:چم اپن واژه در زبان لاتین: (هوا) صاف و آفتابی و خشکه.
=== sud ===
293:است. واژه‌های همریشه‌ی دیگر نیز در شناخت ماهیت هند و اروپائیان سودمنداند: واژه‌های مشترک
691:نخستین اشاره به اقوام ایرانی (مادها و پارس‌ها) در متون آسودی وابسته به قرن نهم پیش از
965:( کشاورزان و شبانان و سوداگران) وجود داشتند که نقش اجتماعی آنها با الگوی سه گانه‌ی فوق
3000:سودی (518/521577): 30۸ 15 ۸0
6241:چم این واژه در زبان‌های پونانی و رومانس و انگلیسی: حسود» حسادت.
6242:چم اين واژه در زبان‌های اسلاوی: خشن» سخت‌گیر» حسود.
10009:واژه‌های فارسی "ساییدن" و آسودن" و "بسودن" نیز از همین واجریشه‌اند (۳۵۳073790 :542)
14265:اوستایی (/۸۷887۸2): -1۸0181 سودی (817501374): ه1۹7
=== shal ===
376:2021 ,2۸۵۵ 4 ۸0 ,تشالمه) :
1843:پهلری (1شالله۲): ۳ اسلاری کهن (16/بما5 بل تال 0ا0):
2140:۱ اوستایی (4ل4۲374): د118۸319 شال1[8۸ پهلوی (/۸87۸6,:)۳۸/4۲ ,۸8۸ ,۸۳۸
2728:رو ی هتلز0 (۸) کذ تشاله‌انی
2932:پهلری (۲7شاللمهه): اه پر تغالی (۳0/70183): ۷0
3496:- وا تشال8۸ دانمارکی (7ل0۸715): لد 1۲
4289:‏ایتالیایی (۷لشاله7): رانا تونی (لتی) (/7۲14۸): ۳0۸
4366:اوستایی (۸887۸۸): ۵۰ بشال8۸ اسپانیایی (3۳/۸//8): ۰ ۳۸718 ,8۸75
4696:0 بشال8۸ ۲8۸ ,18۸۷۸۰ نروژی (۸۷08/8501۸۷): 78
5523:پهلری (7/شالل۸): چکه (2801): ۸ ,78/8
```


## [2026-09-14T01:30:07.308Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n -i \"XUSHK\\|KHUSHK\\|XOSHK\\|SUD\\b\\|SHAL\\b\" ARY_latin_index_pages.txt | head -20",
 "description": "Aryanpur latin index"
}
```


### [2026-09-14T01:30:07.365Z] TOOL RESULT

```
305:Sa sean Beda ist IS Be Sle 3m slo shal ( Gdle) whadar Gejly col dale
652:: col 8 lle shew lal shal eels
5352:TeKO LITHUANIAN) «i p) TAGHT, TASHAL, Ossett) pis)"
5566:TRAP, TRPKY SLOVAK) 51 shal TRIV, TRIW — -{AFGHANI) (7-4) gli!
6227:ZHUVAT (SLOVAK) 5 shal TYGGVA OLD NORSE) oS 393
6993:ZOOR DUTCH) «sache HUSHK, XUSHK — (PAHLAVI) 5 hy
8335:poié POLISH) gle DAVASHAL —«(AFGHANT) (3-4) gui!
11773:KASH, KASHAL, KASHALE (oy
13578:“shal (MAT, MATER) "31" at aly j} aoa Golhaat ta sdb Sar yp old glasjly ») badly
```


## [2026-09-14T01:30:12.746Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 -c \"\nimport re\nt=open('ARY_latin_index_pages.txt',encoding='utf8',errors='replace').read()\nlines=t.split('\\n')\n# find page tag before line 6993\nfor i in range(6992,0,-1):\n    m=re.search(r'\\[pdf page (\\d+)\\]',lines[i])\n    if m:\n        print('pdf page',m.group(1),'at line',i); break\nprint('\\n'.join(lines[6985:7000]))\n\"",
 "description": "Aryanpur page for xushk"
}
```


### [2026-09-14T01:30:13.870Z] TOOL RESULT

```
pdf page 242 at line 6973
leetloak
PT edad say S std al 9 AS Sotbel y lb, O45 4205s cal oN
5 My WS 6399 2 UT 9 AS SIT Obj 22 05a cal pr
. scl ely Cee ST aati” go alb edla
SEAR, SEARIAN AVESTAN) glen s\
SERE, SEAR ENGLISH) 5 nJS3i HAOS., HUSHKA., HUSH-
sSOYR (NORWEGIAN) 5335 USHKA — {OLD PERSIAN) slealy .g+
ZOOR DUTCH) «sache HUSHK, XUSHK — (PAHLAVI) 5 hy
HOLD CHURCH SLAVIC) oS 539! HISHK * (KURDISH) 53,
SUCHD, SUSHITI SANSKRIT) 4 Sailr gg
SUXOI RUSSIAN) gos SUSYATI, SOSA-, Siska, sgsas* 4)
. SAUSAS, SAUSTI (LITHUANIAN) (gi 3 A" (GREEK) gly
SUST, SAUSS (LATVIAN) (3) ig) HATOS, AUOS, HAUEIN
THAN ALBANIAN) gi3T stpus A(LATIN) 3
OLD HIGH GERMAN) (pS ltt
```


## [2026-09-14T01:30:24.317Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n -i \"SAVAH\\|SAOSHYANT\\|SUT, SUD\\|SUD, \\|SUDOMAND\" ARY_latin_index_pages.txt | head -10; echo \"--- shal in ARY\"; grep -n -i \"SHAWL\\|SAVALA\\|SHATI\" ARY_latin_index_pages.txt | head -10",
 "description": "Aryanpur sud / shal"
}
```


### [2026-09-14T01:30:24.397Z] TOOL RESULT

```
10550:(MEAL) 123, (FEAST) 114 *SAVAH, SVAH (SANSKRIT) cy Sule
--- shal in ARY
1158:Shatig yr Oy dS glanly ATT sata cg i} Se del p bil gigs Glatadle y cul
2814:STARE, STANARE -STANVANTI, STA, TISHATI
3225:BUCK: 1095 BHAKSHATI (SANSKRIT) 2, Ss
5435:TKAT (CZECH) So ‘TAKSHATI (SANSKRIT) Sy Sile
10356:SLYSHATI SRUDHI, SRUTA, CRU
10357:SLYSHATI (BULGARIAN) 1 {il LUR ARMENIAN) a)
10358:SLOUSHATI (SERBIAN) «y po ECHLUON, KLUEIN (GREEK) Jb»
11790:KUSHNATI, KUSH- KAOSH, KUSHAITI, KUSHATI
14944:GHOSHATI, GHOSAYATI GAUSHA- :(OLD PERSIAN) ime go
15143:HOLD PRUSSIAN) eS gus 4 UKSHATI, VAKSHATI, VAKSH, UKS-
```


## [2026-09-14T01:30:31.896Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Schal '\\|Schal,\\|schal  '\\|sal  'Schal\\|Umschlagetuch\\|frz.  châle\\|chäle\" LKT.txt | head -10; echo \"=== PLA shal ===\"; grep -n \"شال\" incoming/PLA/PLA_pages.txt | head -10",
 "description": "Lokotsch and Asbaghi for shawl"
}
```


### [2026-09-14T01:30:32.009Z] TOOL RESULT

```
3989:fana  'schälen'];  hieraus  dtsch.  Safan 'weißes  Fischbein  Os  sepiae';  nicht  nur aus  der  harten  Rückenhaut  gewisser Fische,  sondern  aus  Eidechsen  und Krokodilen  gewonnen.  [FLEISCHER  in BSGW  XXI,  43.
4087:1802.  Pers.  säl: 'Umschlagetuch'  [ursprünglich  wohl  ein Eigenname,  denn  IBN  BATTÜTA  spricht IV,  109  von  einer  Stadt  Säliät  in  Indien, in  der  die  Stoffe  gemacht  werden,  die ihren  Namen  tragen];  hieraus  eT\g\.shawl, ndl.  sjaal,  dtsch.  Schal;  russ.  sal',  bulg. serb.  sal,  öech.  Sdl,  poln.  szal;  rum.  ^al, frz.  chäle,  kat.  xal,  sp.  chal,  per.  xal, chale,  it.  scialle.  [Devic  DEt  90.  Eguilaz 372.  542.
=== PLA shal ===
```


## [2026-09-14T01:30:38.800Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM ===\"; grep -n \"الشال\\|شال\" AFM.txt | head -10; echo \"=== TAD ===\"; grep -n \"شال\" TAD.txt | head -10; echo \"=== FVQ ===\"; grep -n -i \"shawl\\|shal\" FVQ.txt | head -5",
 "description": "Arabic loan dictionaries for šāl"
}
```


### [2026-09-14T01:30:38.898Z] TOOL RESULT

```
=== AFM ===
1076:و شال 4 بالتركة « طاغ صوغالى » اي بصل ابل ٠والفارسي‏ مأخرذ م ܐܐܐ 
1295:بشالي الارمن وهو نافع 2 5 ورام 35 : 
2704:( !)ܕ ) تعر يب 4 دهي و للف السترويشار هلالوين 0 ܟ مئه 4 فراء وشال 
2895:فنسكى حبائل «رحته» ܝ يعمد بالطبخ فية شال له 0 20030 ) باليونانة وحام 
3461:قبجاق (في تركستان) وهو في الأصل ماء 2 ܧܥ . والنوع الشالي معدني يرك به 
7314:دو شال 5 
8112:ܘܡܢ ܨ شال 
=== TAD ===
1576:شال - في الفارسية 2 شال » وهو مطرف ينسج فى كشمير الهند 
1700:شال سقد الاحم نظمه فى السقود للاجتواء‎ ٠ وهو حديدة لبعوى علدينا الاحم َّ ج سقاقد‎ 
=== FVQ ===
96:Some day, it is to be hoped, we shall have a Glossary to the 
1224:3 This is not the famous philologer whose Fiqh al-Lugha we shall have occasion 
1867:tion rather than the other, 2 though in many cases, as we shall see, 
4206:common, but this is a denominative from *^-" , and M^^> as we shall 
6313:1 Cor. xiv, 21. Cf. 2 E.sdras, xix, 21, and Mekilta, Beshallah, 9 (ed. Fried nmnn,
```


## [2026-09-14T01:30:46.310Z] TOOL CALL #74: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://ahdictionary.com/word/search.html?q=shawl\" --note \"page 431: AHD online s.v. shawl (Nourai cites AHD:1192 of the 1975 ed.)\" 2>&1 | tail -2; echo; cd /home/sfmqrb/git/rishe/data/verification/sources/web && f=$(ls -t | head -1); grep -n -i -A3 \"shawl\" $f | head -20",
 "description": "AHD online shawl"
}
```


### [2026-09-14T01:30:48.177Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/57b51ad5c4ad3f69.txt

1:URL: https://ahdictionary.com/word/search.html?q=shawl
2-FETCHED: 2026-09-14T01:30:48Z
3-STATUS: 200
4:TITLE: American Heritage Dictionary Entry: shawl
5-
6:American Heritage Dictionary Entry: shawl 
7-
8- HOW TO USE THE DICTIONARY
9- To look up an entry in The American Heritage Dictionary of the English Language, use the search window above. For best results, after typing in the word, click on the “Search” button instead of using the “enter” key.
--
41: shawl (shôl) 
42- Share: 
43-
44- Tweet 
--
48: tr.v. shawled , shawl·ing , shawls To cover with or as if with such a piece of cloth.
49-
50- [Persian sh ā l , ultimately from Sanskrit ś ā ṭ ī , cloth, sari.]
51- (click for a larger image) 
52: shawl
```


## [2026-09-14T01:30:56.340Z] TOOL CALL #75: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/shawl\" --note \"page 431: English shawl etymology\" 2>&1 | tail -2; cd /home/sfmqrb/git/rishe/data/verification/sources/web && f=$(ls -t|head -1); grep -n -i \"Urdu\\|Persian\\|Sanskrit\\|Chaliyam\" $f | head -15",
 "description": "Wiktionary English shawl"
}
```


### [2026-09-14T01:30:58.007Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/51b7edc08ce598ef.txt
200: Borrowed from Hindustani ( Hindi शाल ( śāl ) / Urdu شال ( śāl ) ), from Classical Persian شال ( šāl ) . Doublet of sari through Sanskrit.
364: Persian: شال   (fa) ( šâl ) 
377: Sanskrit: शाटी   (sa) ( śāṭī ) 
403: Urdu: شال   f ( śāl ) 
454: English terms borrowed from Urdu 
455: English terms derived from Urdu 
456: English terms derived from Classical Persian 
526: Terms with Persian translations 
532: Terms with Sanskrit translations 
545: Urdu terms with redundant transliterations 
546: Terms with Urdu translations
```


## [2026-09-14T01:31:40.318Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4120,4135p' BRT.txt; echo \"=== huška entry ===\"; sed -n '30520,30545p' BRT.txt",
 "description": "Bartholomae haoš- and huška-"
}
```


### [2026-09-14T01:31:40.395Z] TOOL RESULT

```
anhav-  106
Geist  entstammt,  zur  Schöpfung  des  bösen Geists  gehörig':  yat  bs  patti  fraist^m bavainti    yavanqm  gyr^iqm  V._J. lo;  22;
—  kahyäcit  'yavanqm  xrafstranqm  V.  16. 12;  —  ma  hwä  ^'yavS  manisiis  * ästaraita Vyt.  J7(?);  —  kat  tat  dqma  "yava  (statt NSn.)  'J  altarfhqm  drlmanam  V.  ij.  5.
Ableit  lu  dOrä  mainyus  (NS.).  —  Fü,:  iütäi mtnit.  —  ■>  An  dipna  nn geglichen?  Oder Pluralfarm,  weit  d<^ia  ASn.  und  APn.  ist? Vgl.  spinlö.maiHyava-  No.  I.
•  j,  aDha-  m.  'Lager,  Lagerstätte':  yS  hl 'nhat  nasdistsm  nmämm  uzdasta  "wer  das ihrer  (der  Hündin)  Lagerstätte''  nächst- gelegene Haus  gebaut  hat,  . ."  V.75.21.
Zum  u.  V.  Bosalr.  —  \'gl.  asla-.  —    Pü. :    i? hac  Si  noidist  man  u^dät  eslel,  erl. :  kui  länak dar  niad.  aah'  ist   also  nicht  besonders  aus- gedrückt. —  O  Wo  sie  geworten  hat. j.  auhatiia  Yt.  10.   129;  lies  ayai»h°.
•  j.  a-Dhaoävmna-  Adj,  (fem.  'ml-)  'nicht ver-,    austrocknend' :   yat  kprptiaoi  .  ■    °ne
|(ADf.)  äpa  urvaire  Y.5.4;  Yt  79.32. *kaasimna-,  PPM.  lu  *haosa;  Praes.  2.  —  Vgl aL  iüfyati  'er  vertrocknet',  np.  sSüdan  'ver- dorrt sein',  gr.  aIo(.  —  Vgl.  huska-.  —  Pü. : undeutl.,  dazu  die  Erl.:  an  i  ne  afiäyojl  Ausk ne  Ausi;  SQ. :  aSaft.  —  »  Zu  Yt.  1$.  16  fälsch- lich aai/iis',  s.  S  26S.  57.
•  j.  a-nhaiSya-  Adj.  'unlauter':  °^lm frafravayahi  tUm  yS  ahurS  maxdä  .  .  aoi zrayS  püitihm  "schwemmst  du  ,  .,  was unlauter  ist,  fort  . .  zum  See  .^.i^' V. 5. 76;
—  para  oAmäJ  yat  hiin  aSm  *draog»m i'äHm  '%Jm  Hnmäne  (sd.)  paiti.barata Yt/p.33-
ai.  asafyä-  Adj.  —  Pü. ;  anäikärän,  erL :  nasäk i  nikän,    dazu  die  Bern.:    asi  ie  aHarianlkän
g.  aohayä  V.  JJ.   16:  a.  hä{yy. j.  aahayati    Yt  10,  20,    2lj    lies    aohyiili, s.  iak-.
•  j.,  g.  anhav-":  aku-^''  ra,  'Sein,  Da- sein, Leben',  vora  leiblichen  und  geistigen;
auch  'Ort  des  Daseins,  Raum'":  uvaHbya nU  'hubya  nipayä  aheca  anhSus  yS  astvaiö yasca  ajrf  mffwaÄ^j"  für  beiderlei  Leben. ." Y.57.2  5^';  25,  Yt  70.93';  —  ubsibyä 'hubya  capmil  (sd.)  Y.J^.3;  JJ-3,  8;  — ubSyS  atihvö  (LD.)  \.4i.i\  —  atsam 'ahunqm    hätqm  Vyt,jo(?).  I)    ohne
nähere  Bestimmung  -  der  Zusammenhang entscheidet—;  i)  vom  leiblichen  Leben: at  fravax^ä  'uhSus  mainyU  paauruyl  "'\c\i will  reden  von   den  beiden  Geistern  zu
dby  Google
=== huška entry ===
»839
huzämay-
huäkö.zsmö.tsma-
1840
•  j.  hu-zämay-  m.  'gute,  leichte  Geburt': %wam  earaitif  zitanäilis  jaityänte  •mim Yt5.87.
AbleiL  —  Zum  V.  'mb-  (^tä-may-).
•  j.  huzämit-  Adj.  (auch  fem.)  'leicht gebärend';  ärthqm  (näml.  fravasmqm) raya  .  .  häirilli  pu&ri  vgrmvainti  .  .  *tB (NPf.)  srsuw«/!  Ytij.  15;  —  aiyävfm.. yS  . .  hairini  US  (APf.)  dalaiti  Y.  65.  a.
Ableit  «US  Auzämayi  %  i8i.  —  Pü.  {lu  Y.): ke  .  ,  husäyiltüA  dähil.
•  g.  hu-zäntav-  Adj.  'der  gute  Kunde hat  von  -,  wohlvertraut  ist  mit  -'  (Gea); yS  dalnqm  vehü  *jar>st3  (sd.)  mananhä armaüsÜ  kasht  asä  -tu!  ". .  weil  er  durch ASa  mit  dem  rechten  Deoken  wohlvertraut ist"  V.  4g.  5.  a)  absolut  'der  die  gute, rechte  Kunde  in  Glaubenssachen  hat, wissend"*:  andrS '^wavas {sA.)  °iusi  sf^nis matdä  Y.  4.^.  y,  —  yf--  dritä  ayantsm  \ urvätsi!  {%A.)  vä  Uui  .  .  Y.  4^.  5.  j
Ableil.  (s.  Amiiqispa-).  —  Vgl.  AÜtanlan:  —  I Pa.  (zu  Y.  43):  xüp  inäsai,  (sonst):  xüp  sitä- , latTA.  —  I)  Vgl.  iBed.  BB.  8.  213,  IF.  7. 224.
•  j.  huSata-  Adj.  'getrocknet,  trocken': alsmanqmSt  .  .  'tarn  (GP.)  pairjltanqm vazyail  A.J.  5;  V.  14.  2.
PPfP.  lum  V.  haos-i-).  —  PÖ.:  huik.  —  ')  Die Bildung  ist  ungewöhnlich.  Sie  scheint  ein Praei.  3  huia-  varäusiuseticn;  s.  Sp.  501  No.  d,
•  j.  hu-§ayana-  Adj.  'gutes  Wohnen  ge- während*: tistrlm  .  .  rämajayangm  'ti>m Yt.S.2.  a)  mit  Dat.  comm.:  mUnm räma/ayansm  'mm  atryabyS  dai^hubyS Yt.  10.  4.
Npü.;  nXk  sädKi).
•  g.  hu-ääna-  Adj.  'guten  Verdienst,  Lohn verschaffend':  tattiksi  "mm  aaAat"deikR das  wird  ihm  guten  Lohn  verschaffen'' V.5JS
•/uBo-  m.,  lum  V.  iait:  —  ai,  lufäna-  Adj, 'leicht  lu  erwerben'.  —  Pü. :  humäniinJA.
•  g.  hu-iöiS^man-  n,  'gute  Wohnung, gutes  Wohnen':  As  zl  nS  "mä  hä  n5 iitayüitiin  dät  trvTslm  vatahtui  mananhs binxai  (sd.)  "sie  (näm!.  Ärm^  schenke uns  gutes  Wohnen,  sie  uns  Bestand  und Kraft  .  ."  Y.  48. 6.
Zum  V.  iiy-;  aus  ar.  *xhilman-  n.;  vgl.  ai. kllma-  m.  'Wohnsiti'  und  gr.  Xarr/iB  :  Xsi/ig(; I.  noch  '/raa%man-,  vä%man-,  väri%man-.  — Pü.:  ^ärih.
•  j.  hu-äit-  Adj.  'gutes  Wohnen  bietend, wo,  bei  dem  es  sich  gut  wohnen  lässt':
'ydha  ^w3  (näml.  mikrim)  *aiwisayama  . . 'ttm  b?rffmya.saS3m  (sd.)  Yt.iO.77. ■AV-  f.,  lum  V.  iay-.  —  ai.  'kfU-  Adj.
•  j-,  g.  hu-sitay-  f.  i)  im  gAw.;  a)  'gutes Wohnen':  kads  .  .  ärmaitii  jintat  (Sp. 494  m.)  xsdhrä  'Mtis'''  västravaiii  Y. 4S.11;  — yä  'I^lli'^  rämqm(sd-)cä  dät Y.  25.  10.  b)  'gute  Wohnung,  Wohn^ statf :  at  asistä  yaojanis  (sd.)  ä  'sitsil vaiahJui  manaahö  masdä  asahyacä  Y. 30.  10.  a)  im  jAw.  mit  ysirya-  Adj. 'das  ganze  Jahr  hindurch  währendes  gutes
,  Wohnen'  als  Gottheit:  asäunqm  .  .  /ra- :  vasayS . .  ynas^a  vTrB.vakwä  . .  yairyqmca '"lim  Y.  2. 6;  1.6;  —  haurvatais  raiiwS \yäiryayasca  'sttsii' sariüaHbyS  asahe  ratuiyS iS.7.6;2.6.         IS.  -H  als  Inf.  sbes.
ai.  iuifilay-  l.  —  Pu. ;  humänisrü/i,  (zu  3} : sälän  niänisnVi  —  Sü.:  samvatsaränamca  s«j> vaiüh  -,  erl.;  ia  andar  sil  pa  ftärdnlh  i  vek täyit  mäHÜtaa.  —  ')  iSchr.  s.  S  »5*-  9-
•  j.  hu-§iti  Inf.  'gut  zu  wohnen':  '«ft' ramS.siti  danyS.Iiti  (sd.)  ite  vXse  a/rlnaiiä Y.6K14;  14;  ät.  V.rp.2  Pü.
Vgl.  husilay-,  —  Pü.;  AumänilniA.
•  j.  hugka-,  p.  Niäka-  i)  Adj.  'trocken, ausgetrocknet':  'i^m  alsmim  Y.  7/.  8;  — aHavat  'kanam  alsmanqm  aSavat  nafia- nqm  V.  7. 31;  —  vtlastiJrap  yat  (Sp. 1252  u.)  'kanqm  (als  Obj.)  ..  aitiha  s^mS nidaüyqn  "sie  sollen  in  der  Länge  einer V.  vom  trockenen  (Holz) , .  auf  der  Erde hier  niederlegen"  V,  7. 29;  3c,  33,  34;  — 'kanqm  yavanqm  V.  7.  35;  —  'hm  p>htn raicayat  Ytj.  78;  77;  —  aSavat  apat haca  nilbarayjn  °ke  z)me  nidathya»  "so- viel sollen  sie  aus  dem  Wasser  heraus-
```


## [2026-09-14T01:31:49.330Z] TOOL CALL #77: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-14T01:31:49.427Z] TOOL RESULT

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


## [2026-09-14T01:31:56.534Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,5p' f4f76683aa8c4692.txt; grep -n -i \"dry\\|Avestan\\|Old Persian\\|Ancient Greek\" f4f76683aa8c4692.txt | head -20",
 "description": "Check PIE reconstruction fetch"
}
```


### [2026-09-14T01:31:56.601Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82sews-
FETCHED: 2026-09-14T01:27:26Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/h₂sews- - Wiktionary, the free dictionary

136: to be dry 
146: Ancient Greek: αὕω ( haúō , “ to dry (tr.) ” ) [ 1 ] 
162: Ancient Greek: αὖος ( aûos ) [ 4 ] 
170: Lithuanian: saũsti ( “ to wither ” ) , saũsinti ( “ to dry (transitive) ” ) 
172: Latvian: sust ( “ to dry ” ) ( intransitive )
```


## [2026-09-14T01:32:00.671Z] TOOL CALL #79: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg431.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/431.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/431.png",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-14T01:32:00.781Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 81124 Sep 13 21:32 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/431.png
```


## [2026-09-14T01:42:32.652Z] TOOL CALL #80: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-431.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_PIE  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82sews-\"\nW_XOSK = \"https://en.wiktionary.org/wiki/%D8%AE%D8%B4%DA%A9\"\nW_SUD  = \"https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%AF\"\nW_SAL  = \"https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%84\"\nW_SHAWL= \"https://en.wiktionary.org/wiki/shawl\"\nE_AUST = \"https://www.etymonline.com/word/austere\"\nE_SHAWL= \"https://www.etymonline.com/word/shawl\"\nMW_SAB = \"https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc/getword.php?key=Sabala\"\nAB_XOSK= \"https://abadis.ir/fatofa/%D8%AE%D8%B4%DA%A9/\"\nAB_SAL = \"https://abadis.ir/fatofa/%D8%B4%D8%A7%D9%84/\"\nAHD_SH = \"https://ahdictionary.com/word/search.html?q=shawl\"\n\ndoc = {\n \"pdf_page\": 431,\n \"book_page\": 401,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": []\n}\n\n# ---------------------------------------------------------------- entry 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Saus, Sus\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *saus- / *sus- 'dry' (laryngealist notation *h₂sews-; adj. *sus-ko-)\",\n \"note\": (\"Pokorny IEW 880–881 heads the entry exactly 'saus-, sus- ‚trocken, dürr‘; sauso-, sus-ko ds.' \"\n   \"and gathers there Skt. śuṣyati, śuṣka-, Av. haos-/huška-, Gk. aὖos / auštērós, Lat. sūdus, OE sēar, \"\n   \"Lith. sausas, OCS suchŭ. The language label 'Indo-European' and the gloss 'dry' are both right; the page \"\n   \"number 881 is the second page of Pokorny's entry (the page break '881' falls in the middle of the Indo-Iranian \"\n   \"material, right beside av. haos- and huska-), so Nourai's citation is precise. Modern notation makes the root \"\n   \"*h₂sews- 'to be dry' with a *-ko- adjective *h₂sus-ko-. \"\n   \"One cosmetic point on the chart itself: on the printed page the box to the right of 'Old Persian uška' is an \"\n   \"EMPTY box (no language, no word) and the Greek→English arrow runs through a second arrowhead with no \"\n   \"intermediate box; the extraction correctly ignores both, so nothing is missing from the JSON.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *saus- / *sus- «خشک» (در نگارش حنجره‌گرایانهٔ امروز *h₂sews-) در فرهنگ پوکورنی \"\n   \"در صفحهٔ ۸۸۰–۸۸۱ به همین صورت آمده است. صورت صفتی آن با پسوند *-ko- یعنی *h₂sus-ko- بنیاد سنسکریت śuṣka-، \"\n   \"اوستایی huška-، پارسی باستان uška- و فارسی «خشک» است. نام زبان، معنی و شمارهٔ صفحهٔ نورایی هر سه درست است؛ \"\n   \"ادعای نورایی درست است.\"),\n \"sources\": [W_PIE, E_AUST],\n \"ref_check\": [\n   {\"ref\": \"POK:881\", \"status\": \"supports\",\n    \"note\": (\"POK_03.txt leaf 115 (= IEW pp. 880–881): 'saus-, sus- ,trocken, dürr‘; sauso-, sus-ko ds. ... av. haos- \"\n             \"‘exarescere’, aŋhao-səmna- ‘nicht trocknend’; ai. śuṣka-, av. huska- ‘trocken’; gr. aὖoς ... aὐστηρός \"\n             \"‘herb, streng’'. The printed page-break marker '881' stands inside this entry, immediately before the \"\n             \"Avestan material Nourai uses. Grep: grep -n 'saus-' POK_03.txt\")}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"WP. II 447 (cited by Pokorny at the foot of the entry)\", \"stance\": \"supports\",\n    \"note\": \"Pokorny closes the entry 'WP. II 447, WH. II 624, Trautmann 250 f., Frisk 188 f., 192 f.' — i.e. Walde-Pokorny II 447 is the earlier statement of the same root; POK_03.txt leaf 115.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. saus-\", \"stance\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 904: 'saus-. Dry. 1. Extended form *sauso- in Germanic *sausaz ... 2. Suffixed form *saus-t- in Greek austéros, harsh: AUSTERE. [Pok. saus- 880.]'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.v. sausos / sus / susó\", \"stance\": \"supports\",\n    \"note\": \"IEC.txt line 15033: 'sausos ‘dry, withered, mature’ ... WP II, 447 Skt. (variant) śoṣaḥ ... Av. cf. hao-šəmna- ... OP cf. huška- ... Per. xušk, id.; Gk. aūos'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 15.84 DRY, p. 1085\", \"stance\": \"supports\",\n    \"note\": \"SYN.txt line 27228: 'Grk. (Hom.) aūos, Att. aûos; OE sēar, ME (NE) sere ...; Skt. çuṣka- (for *sus-ka-), Av. huška-, OPers. uška-.'\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1,\n \"lang\": \"Avestan / Old Persian\",\n \"words\": \"hauš : to dry ; hauš-a, huška : dry\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Nourai's 'hauš' is his usual Latin rendering of Avestan haoš- (Av. ao = his au). Bartholomae lists the \"\n   \"verbal root under a-ŋhaošəmna- 'nicht ver-, austrocknend' (Y 5.4, Yt 19.32), a present participle passive to \"\n   \"*haoša-, and glosses the root 'vertrocknen' (Lat. exarescere in Pokorny's wording); the starred *haoša- is exactly \"\n   \"Nourai's second form 'hauš-a', i.e. a reconstructed thematic present stem, not an attested lemma. The adjective \"\n   \"huška- 'trocken, ausgetrocknet' is well attested (Y 71.8, V 7.29–35, Yt 8.77–78) and continues *h₂sus-ko-, the \"\n   \"zero grade *sus- of the root plus the *-ko- suffix, with Iranian *s > h before *u and the regular Indo-Iranian \"\n   \"ruki-retroflexion *-sk- > -šk- (Skt. śuṣka- shows the same with an added initial assimilation ś- for *s-). The only \"\n   \"looseness is the box label: hauš/haoša- and huška- are Avestan, while the Old Persian cognate is uška- and has its \"\n   \"own box (#4); Bartholomae himself heads the entry 'j. huška-, p. uška-', which is presumably why Nourai merged the \"\n   \"two labels.\"),\n \"derivation_fa\": (\"«hauš» در نگارش نورایی همان ریشهٔ اوستایی haoš- «خشکیدن» است (او ao اوستایی را همواره au می‌نویسد)؛ \"\n   \"بارتولومه آن را زیر a-ŋhaošəmna- «خشک‌نشونده» آورده و ستاک حال آن را *haoša- بازسازی کرده است که همان «hauš-a» نورایی است \"\n   \"(پس صورتی بازساخته‌شده است نه شاهددار). صفت huška- «خشک» از صورت صفر ریشه (*sus-) با پسوند *-ko- ساخته شده؛ س«» ایرانی باستان پیش از u به h \"\n   \"بدل شده و خوشهٔ -sk- بر اثر قاعدهٔ ruki به -šk- دگرگون شده است. تنها نکته آن که هر سه صورت اوستایی‌اند و صورت پارسی باستان (uška-) جعبهٔ جداگانه دارد؛ \"\n   \"با این همه خود بارتولومه مدخل را «j. huška-, p. uška-» عنوان کرده است. ادعای نورایی درست است.\"),\n \"sources\": [W_PIE, W_XOSK],\n \"ref_check\": [\n   {\"ref\": \"POK:881\", \"status\": \"supports\",\n    \"note\": \"POK_03.txt leaf 115: 'av. haos- ‘exarescere’, aŋhao-səmna- ‘nicht trocknend’; ai. śuṣka- (aus *suṣka-), av. huska- ‘trocken’' — both of Nourai's Avestan forms, on the very page cited.\"},\n   {\"ref\": \"SOD:373\", \"status\": \"partial\",\n    \"note\": \"Gharib's Sogdian dictionary is cited on this box only because the Sogdian descendant hangs from it; the Avestan forms are not in SOD. The Sogdian entry itself (no. 9238 skw, 'dry', '<Av. hiška') is on printed p. ~374 of SOD_pages.txt (leaf 440), i.e. within a page of the citation.\"},\n   {\"ref\": \"ETM:64\", \"status\": \"not_checked\",\n    \"note\": \"Abolghasemi, Risheh-shenasi (Qoqnus 1374) — refs_online.json records no scan online (searched archive.org, ketabnak, noorlib); no copy on disk.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. ~1839–1840 s.v. huška-, and s.v. a-ŋhaošəmna- (col. ~106)\", \"stance\": \"supports\",\n    \"note\": \"BRT.txt line 30531 ff.: '• j. huška-, p. uška- 1) Adj. ‘trocken, ausgetrocknet’'; and line 4127 s.v. a-ŋhaošəmna-: '*haosəmna-, PPM. zu *haosa; ... Vgl. ai. śuṣyati ‘er vertrocknet’, np. xušīdan ‘verdorrt sein’, gr. aὖos. — Vgl. huska-.'\"},\n   {\"src\": \"KNT\", \"where\": \"p. 178 s.v. uška-\", \"stance\": \"supports\",\n    \"note\": \"KNT.txt: 'uška- adj. ‘dry’; nt. as sb., ‘land, mainland’: Av. huška- ‘dry’, NPers. xusk, Skt. śuṣka-, śuṣyati ‘dries’...'\"},\n   {\"src\": \"ARY\", \"where\": \"pdf p. 242 (printed 243) s.v. خشک\", \"stance\": \"supports\",\n    \"note\": \"ARY_latin_index_pages.txt lines around 6990: 'HAOS-, HUSHKA-, HUSH- (AVESTAN) ... USHKA- (OLD PERSIAN) ... HUSHK, XUSHK (PAHLAVI) ... HISHK (KURDISH)' — an independent modern Persian handbook giving exactly Nourai's Avestan/OP/Pahlavi set.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2,\n \"lang\": \"Persian\",\n \"words\": \"xošk «خشک» : dry\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"NP خشک xošk (classical xušk) is the direct continuation of MP hušk (Book Pahlavi <hwšk'>), itself from \"\n   \"Old Iranian *huška- = Av. huška-; the initial Iranian h- before u was reinterpreted as x- already in late Middle \"\n   \"Persian / early New Persian (MacKenzie writes the Pahlavi as hušk and notes the NP outcome xušk), whence the \"\n   \"modern spelling with خ. Wiktionary traces the same line: Proto-Iranian *Hhúškah < Proto-Indo-Iranian *Hsúškas < \"\n   \"PIE *h₂sews- + *-kos, cognate with Skt. śuṣka-. The denominal verbs in the extra box are equally regular: \"\n   \"خشکیدن xoškīdan 'to dry up' and its participle خشکیده are built on the adjective, while خوشیدن xušīdan / خوشیده \"\n   \"continue the inherited verb itself — Bartholomae expressly cites 'np. xušīdan ‘verdorrt sein’' beside Av. haoš- and \"\n   \"Skt. śuṣyati, which is why the -k- is absent in that pair. Sa'dī's line بخوشید سرچشمه‌های قدیم quoted in the box is a \"\n   \"genuine attestation of that older verb.\"),\n \"derivation_fa\": (\"«خشک» از فارسی میانهٔ hušk [hwšk']، از ایرانی باستان *huška- (اوستایی huška-، پارسی باستان uška-) است؛ h آغازین \"\n   \"پیش از u در گذار به فارسی نو به خ بدل شده است. معین در حاشیهٔ برهان قاطع (ص ۷۵۰) همین زنجیره را با گونه‌های گیلکی، سمنانی، \"\n   \"سنگسری و فریزندی آورده است. از میان صورت‌های جعبه، «خشکیدن/خشکیده» از خود صفت ساخته شده، اما «خوشیدن/خوشیده» دنبالهٔ \"\n   \"مستقیم فعل اوستایی haoš- است که بارتولومه نیز صریحاً «np. xušīdan» را در کنار سنسکریت śuṣyati نقل می‌کند. ادعای نورایی درست است.\"),\n \"sources\": [W_XOSK, AB_XOSK],\n \"ref_check\": [\n   {\"ref\": \"BQT:752\", \"status\": \"supports\",\n    \"note\": (\"Mo'in's etymological footnote to خشک in Borhan-e Qate‘ is on the printed page reached at leaf 210 of \"\n             \"BQT_v2_pages.txt; the Latin-script part survives in the OCR mirror-reversed — 'khsuh' = hušk (پهلوی), \"\n             \"'akhsuh' = huška- (اوستا) beside پارس باستان uška-, then 'khsuxx' = xušk for Semnani and the Gilaki/Sangesari/ \"\n             \"Farizandi/Natanzi dialect forms. Content is exactly Nourai's chart. The page offset for vol. 2 is \"\n             \"uncertain by 2–3 (leaf+540 vs leaf+543), so the footnote sits on printed p. 750–753 and Nourai's 752 is \"\n             \"inside that band.\")},\n   {\"ref\": \"MON:1461\", \"status\": \"not_checked\",\n    \"note\": (\"Mo'in's 6-vol. Farhang-e Farsi is not online with its pagination (refs_online.json: only the 2-vol. Adena \"\n             \"condensation exists). Content cross-check via abadis' Mo'in text: 'خُشک (خُ) [په.] (ص.) ۱ - بدون رطوبت و نم' \"\n             \"— the tag [په.] = Pahlavi, agreeing with the chart's route.\")},\n   {\"ref\": \"ETM:64\", \"status\": \"not_checked\", \"note\": \"Abolghasemi's Risheh-shenasi is not available in any scan (see refs_online.json).\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 46 s.v. hušk\", \"stance\": \"supports\",\n    \"note\": \"PHD.txt: 'hušk [hwšk' | = M, N xušk] dry' — MacKenzie gives the Pahlavi form and the NP outcome in one line.\"},\n   {\"src\": \"BRT\", \"where\": \"col. ~106 s.v. a-ŋhaošəmna-\", \"stance\": \"supports\",\n    \"note\": \"'Vgl. ai. śuṣyati ‘er vertrocknet’, np. xušīdan ‘verdorrt sein’' — Bartholomae explicitly attaches NP خوشیدن (Nourai's extra word) to this root.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien\", \"stance\": \"silent\",\n    \"note\": \"grep -n 'hušk\\\\|xušk\\\\|chusk' HUB.txt returns nothing — Hübschmann does not treat this word.\"},\n   {\"src\": \"MON\", \"where\": \"vajehyab/abadis text of Mo'in s.v. خشک\", \"stance\": \"supports\",\n    \"note\": \"'(خُ) [په.] (ص.) ۱ - بدون رطوبت و نم ...' — Pahlavi origin tag, no Arabic or foreign tag.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3,\n \"lang\": \"Sogdian\",\n \"words\": \"škw : dry\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"škw\",\n \"correct_form\": \"skw / ʾskw (Sogd. sku, Manichaean skw, Buddhist Sogdian ʾskw)\",\n \"derivation\": (\"The Sogdian word for 'dry' does descend from the same Old Iranian *huška-/*hiška- as Avestan huška-: \"\n   \"Gharib's Sogdian dictionary has no. 1752 ʾskw (Buddhist/Manichaean) '(ə)sku ©<*hišku' 'dry' and no. 9238 skw \"\n   \"(Manichaean) '(ə)sku ©<Av. hiška' 'dry', with the by-forms swk- / swkcʾ / skwy(y) 'dry'. Sogdian lost the initial \"\n   \"h-, kept šk as sk in the transliteration, and prothesised ʾ- in the Sogdian script; that is the whole derivation, \"\n   \"and the arrow is right. What is wrong is only the shape of the word in the box: the printed page (pdf p. 431, see \"\n   \"data/verification/sources/refs/ocr/BOOK/431.png) really does show 'škw', with š, and no Sogdian form škw is known \"\n   \"to Gharib (grep of SOD.txt for 'škw' finds nothing; every attested spelling has plain s). So the book prints an \"\n   \"erroneous š for s — Nourai's own misprint, faithfully extracted — and the form that should stand is skw / ʾskw.\"),\n \"derivation_fa\": (\"واژهٔ سغدی به معنی «خشک» در فرهنگ بدرالزمان قریب به صورت‌های ʾskw (شمارهٔ ۱۷۵۲) و skw (شمارهٔ ۹۲۳۸) و swk- آمده \"\n   \"که همه از ایرانی باستان *hiška-/*huška- بازمانده‌اند؛ سغدی h آغازین را انداخته و در خط سغدی الف پروتتیک گرفته است. \"\n   \"پس پیوند درست است، اما صورت مندرج در کتاب یعنی «škw» با شین، در هیچ منبعی شاهد ندارد. تصویر صفحهٔ چاپی نشان می‌دهد که \"\n   \"خود کتاب چنین نوشته است؛ پس خطای چاپی کتاب است نه خطای خوانش اسکن، و صورت درست skw / ʾskw است.\"),\n \"sources\": [W_XOSK],\n \"ref_check\": [\n   {\"ref\": \"SOD:373\", \"status\": \"partial\",\n    \"note\": (\"Gharib no. 9238 'skw M (ə)sku ©<Av. hiška — dry — GMS 96, 397; BBB p53.486' sits at leaf 440 of \"\n             \"SOD_pages.txt ≈ printed p. 374, one page off Nourai's 373 (the file's offset is leaf−66 ±1); no. 1752 \"\n             \"'ʾskw B, M (ə)sku ©<*hišku — dry' is at p. ~68. The meaning and the etymology are as charted; the \"\n             \"spelling škw is not in the dictionary.\")}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"nos. 1752, 9238, 9248, 9356, 9359\", \"stance\": \"partial\",\n    \"note\": \"'1752 ʾskw ... (ə)sku ©<*hišku — dry'; '9248 skwy(y) M skawe? ©<*(hi)škuwaka — dry'; '9356 swk- M suk (swq-) — dry'; '9359 swkcʾ M sukca ©*(hi)škwaka — dry'. Every spelling begins with s, never š.\"},\n   {\"src\": \"BRT\", \"where\": \"col. ~1839 s.v. huška-\", \"stance\": \"supports\",\n    \"note\": \"'j. huška-, p. uška- Adj. ‘trocken, ausgetrocknet’' — the Old Iranian base from which Gharib derives the Sogdian word.\"},\n   {\"src\": \"PHD\", \"where\": \"p. 46 s.v. hušk\", \"stance\": \"supports\",\n    \"note\": \"'hušk [hwšk' | = M, N xušk] dry' — the Middle Persian sister form of the Sogdian word.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4,\n \"lang\": \"Old Persian\",\n \"words\": \"uška : dry\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"OP uška- 'dry', attested in the neuter used as a substantive 'dry land, mainland' in the genitive \"\n   \"uškahyā of Darius' Susa inscription DPe 13, is the Old Persian counterpart of Av. huška- from Old Iranian \"\n   \"*huška- < PIE *h₂sus-ko-. The only difference from Avestan is the loss of the initial h- before u in Old Persian, \"\n   \"a regular OP development that Kent treats under §146.1; the -šk- again reflects ruki. Because uška- is a sister \"\n   \"of Av. huška- and not its descendant, Nourai correctly hangs it from the root box and not from node #1.\"),\n \"derivation_fa\": (\"پارسی باستان uška- «خشک»، در کتیبهٔ داریوش در شوش (DPe ۱۳) به صورت uškahyā به معنی «خشکی، خشکی زمین» آمده است. \"\n   \"این صورت هم‌ارز اوستایی huška- است و تفاوتش تنها افتادن h آغازین پیش از u است که در پارسی باستان قاعده‌مند است (کنت §۱۴۶). ادعای \"\n   \"نورایی درست است؛ و چون uška- خواهر huška- است نه بازماندهٔ آن، جای گرفتنش زیر خود ریشه درست است.\"),\n \"sources\": [E_AUST],\n \"ref_check\": [\n   {\"ref\": \"KNT:178\", \"status\": \"supports\",\n    \"note\": (\"KNT.txt, Lexicon: 'uška- adj. ‘dry’; nt. as sb., ‘land, mainland’: Av. huška- ‘dry’, NPers. xusk, Skt. \"\n             \"śuṣka-, śuṣyati ‘dries’, Lith. saūsa-s ‘dry’, NEng. sere, sear (§146.1). uškahyā gsn. DPe 13.' The entry \"\n             \"falls on the leaf 13 leaves after the one carrying the printed numeral 166, i.e. printed p. ~178—179.\")}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. ~1839 s.v. huška-\", \"stance\": \"supports\",\n    \"note\": \"Bartholomae heads the entry '• j. huška-, p. uška-', explicitly pairing the Avestan and Old Persian forms.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 15.84 DRY\", \"stance\": \"supports\",\n    \"note\": \"SYN.txt line 27228: 'Skt. çuṣka- (for *sus-ka-), Av. huška-, OPers. uška-.'\"},\n   {\"src\": \"KNT\", \"where\": \"§117 (phonology)\", \"stance\": \"supports\",\n    \"note\": \"KNT.txt line 1438: 'OP uška- ‘dry’, Av. huska-, Lith. sausa-s' — cited among the examples of pIE s remaining unchanged in OP.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5,\n \"lang\": \"Greek\",\n \"words\": \"austěros : harsh\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Gk. αὐστηρός austērós, originally of fruit and wine 'making the tongue dry, rough, tart', hence \"\n   \"metaphorically 'harsh, severe', is a -ηρός derivative of the same root as αὖος aûos 'dry' and αὝω haúō 'to dry'. \"\n   \"Greek lost the initial *s- of *saus- to h- and then to nothing in αὖος < *sauso-; Watkins formalises the \"\n   \"adjective as a suffixed *saus-t- > austēros. Nourai attaches it to the root box rather than to the Iranian node, \"\n   \"which is right: it is a cognate, not a borrowing from Iranian.\"),\n \"derivation_fa\": (\"واژهٔ یونانی αὐστηρός (austērós) نخست دربارهٔ میوه و شراب «گس، دهان‌خشک‌کن» بود و سپس معنی «سخت، درشت» یافت؛ از همان ریشهٔ \"\n   \"αὖος «خشک» و αὝω «خشکاندن» ساخته شده است. در یونانی s آغازین *saus- نخست به h و سپس به صفر رسیده؛ واتکینز صورت \"\n   \"پسوندی *saus-t- را برای آن بازسازی می‌کند. پس این واژه هم‌ریشهٔ «خشک» است نه وام‌واژهٔ آن؛ ادعای نورایی درست است.\"),\n \"sources\": [E_AUST, W_PIE],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 904 s.v. saus-: '2. Suffixed form *saus-t- in Greek austéros, harsh: AUSTERE. [Pok. saus- 880.]' — exactly the arrow drawn.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 881\", \"stance\": \"supports\",\n    \"note\": \"POK_03.txt leaf 115: 'gr. aὖoς (Hom.), aὖoς (att.) ‘dürr, trocken’, aὐσταλέος ‘struppig, schmutzig’, aὐστηρός ‘herb, streng’'.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1432 s.v. austere / s.v. auantic\", \"stance\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 4011: 'austere, adj. ... fr. L. austerus, ‘dry, harsh, sour, tart’, fr. Gk. aὐστηρός, ‘harsh, rough, bitter’, fr. aὐειν, ‘to dry’, fr. aὖoς, ‘dry’' (and s.v. auantic: aὖoς '... stands for *sauso-s and derives fr. I.-E. base *saus-, *sus-, ‘dry’').\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. sausos\", \"stance\": \"supports\",\n    \"note\": \"IEC.txt line 15033 lists 'Gk. aūos, adj. id.; aūō, v. ‘parch’' under sausos.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6,\n \"lang\": \"English\",\n \"words\": \"austerity\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"The box has no reference because the chain is the standard Graeco-Latin one, and the printed chart even \"\n   \"draws it through a second (empty) arrowhead: Gk. austērós → Lat. austērus 'dry, harsh, sour' → Late Latin \"\n   \"abstract austēritās (acc. austeritatem) → Old French austerité 'harshness, cruelty' (14th c.) → Middle English \"\n   \"austerite, mid-14th c., 'sternness, harshness'. The sense 'severe self-discipline, ascetic practice' is from the \"\n   \"1580s and the modern economic sense ('policy limiting non-essentials') dates from the Second World War. The \"\n   \"adjective austere had entered English a little earlier, in the early 14th c., by the same route.\"),\n \"derivation_fa\": (\"واژهٔ انگلیسی austerity از راه لاتین و فرانسه به یونانی می‌رسد: austērós یونانی > لاتین austērus > لاتین \"\n   \"پسین austēritās > فرانسهٔ باستان austerité > انگلیسی میانه (نیمهٔ سدهٔ چهاردهم میلادی) به معنی «سختگی، درشتی». \"\n   \"معنی «ریاضت‌کشی» از دههٔ ۱۵۸۰ م و معنی اقتصادی امروزین از جنگ جهانی دوم است. جعبه در کتاب ارجاع ندارد و نیازی هم ندارد؛ \"\n   \"ادعای نورایی درست است.\"),\n \"sources\": [E_AUST],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book; the chain is verified from Etymonline and Klein instead.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1432 s.v. austere\", \"stance\": \"supports\",\n    \"note\": \"'austere, adj., stern, severe; very simple. — OF. austere (F. austère), fr. L. austerus ... fr. Gk. aὐστηρός'.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. Austere\", \"stance\": \"supports\",\n    \"note\": \"SKT.txt line 1187: 'Austere. (F.-L.-Gk.)' — Skeat's formula for French < Latin < Greek.\"},\n   {\"src\": \"WEB\", \"where\": \"vol. I s.v. austere / austerity\", \"stance\": \"supports\",\n    \"note\": \"WEB_vol1.txt line 13582: 'aus-tere’, a. [ME. austere, OFr. austere; L. austerus, harsh; Gr. austēros, dry, harsh.]' with 'austerity' as the next headword.\"}\n ]\n})\ndoc[\"entries\"].append(e0)\n\n# ---------------------------------------------------------------- entry 1\ne1 = {\n \"entry\": 1,\n \"root\": \"Sav 1, Savah 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Av. sav- / sū- 'to benefit, be of use' and savah- n. 'benefit, (eternal) welfare' (Proto-Iranian *sauH-, PIE *ḱewh₁- 'to swell, increase')\",\n \"note\": (\"Both root forms are real Avestan lemmas with the glosses Nourai gives. Bartholomae has '• j. (1 g) sav- V. \"\n   \"‘nützen’, Praes. 17 (Fut.) saošya-, 25 (Pass.) suya-, 30 (Iter.) sāvaya-' and, separately, '• j., g. savah- n. \"\n   \"‘Nutzen, Vorteil’' (in the Gathas specifically the eternal benefit of the next life). The 'Sav 1 / Savah 1' \"\n   \"numbering is Nourai's device to separate this root from the homonymous Av. sav- 'to move' and savah- 'the eastern \"\n   \"continent' (Bartholomae has both). One addition modern scholarship makes: Cheung (2007) shows that this Iranian \"\n   \"*sauH is the Iranian form of PIE *ḱeuh₁- 'to bulge, swell up, increase' (LIV 339 f.; Pok. 592 ff.), so the \"\n   \"'benefit' sense is secondary to 'increase, prosper' — Nourai simply stops one layer short, he does not err.\"),\n \"note_fa\": (\"هر دو صورت ریشه اوستایی و شاهددارند: بارتولومه sav- را «nützen» (سود رساندن) و savah- را «Nutzen, Vorteil» (سود، بهره) \"\n   \"معنی کرده است؛ در گاثاها ویژه به معنی «سود جاودانی» است. شمارهٔ ۱ در «Sav 1» از آن روست که ریشهٔ هم‌نویسهٔ دیگری \"\n   \"(sav- «حرکت کردن» و savah- نام کشور خاوری) هم هست. افزودنی امروزین: چونگ (۲۰۰۷) این ریشه را ایرانی *sauH و ادامهٔ \"\n   \"هندواروپایی *ḱeuh₁- «ورم کردن، افزودن» می‌داند؛ پس معنی «سود» ثانوی است. ادعای نورایی درست است.\"),\n \"sources\": [W_SUD],\n \"ref_check\": [\n   {\"ref\": \"HRN:166\", \"status\": \"supports\",\n    \"note\": \"HRN.txt leaf 187 = printed p. 166, no. 751: 'sūd ‘Nutzen, Vorteil’. ... aw. √sav- ‘nützen’; phlv. sūt, sūtīh, sūtōmand, sūtīnītan.' Horn's line is precisely the chart's Avestan→Pahlavi→Persian sequence.\"},\n   {\"ref\": \"NYB:181\", \"status\": \"supports\",\n    \"note\": \"NYB_vol2_glossary.txt, page marker '181 sūtēh' on the same leaf: 'sūt [swt'] use, advantage, benefit ... MPrs swd; Paz. sud, NP sūd, from Av. (1561) sav- ‘to benefit’, savā- savah- ‘(eternal) welfare’, cf Sošans.' — both of Nourai's root forms with both of his glosses, on the cited page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. ~1561 s.v. sav-, and s.v. savah-\", \"stance\": \"supports\",\n    \"note\": \"BRT.txt line 26010: '• j. (1 g) sav- V. ‘nützen’ ... Vgl. ... np. sūd ‘Nutzen’'; and the following column: '• j., g. savah- n. ‘Nutzen, Vorteil’ ... a) gĀw. nur vom ‘ewigen Nutzen’ im andern Leben'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *sauH ‘to bulge, swell up, increase’, p. 341\", \"stance\": \"partial\",\n    \"note\": \"'*AVESTAN: su- (sāuu-) ... *MIDDLE PERSIAN: MMP swd, swwd, BMP swt /sud/ ‘profit, use, advantage’ ... *NWIR: ... NP sūd ‘gain, profit’ ... «PIE *ḱeuH₁- ‘to bulge, swell up’'. Same chain, but Cheung glosses the Avestan root ‘swell, increase’ and takes it a layer deeper than Nourai.\"},\n   {\"src\": \"PHD\", \"where\": \"p. 79 s.v. sūd\", \"stance\": \"supports\",\n    \"note\": \"PHD.txt: 'sūd [swt' | M swd, N ~] use, profit, advantage'.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1,\n \"lang\": \"Pahlavi\",\n \"words\": \"sŭt : benefit, interest\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Middle Persian sūd, spelt <swt'> in Book Pahlavi (hence Nourai's and Horn's Latinisation 'sūt': the \"\n   \"Pahlavi <t> is the historical spelling of a sound already pronounced d) and <swd>/<swwd> in Manichaean Middle \"\n   \"Persian, where the pronunciation is unambiguous. It continues Old Iranian *sūta- / *sauta-, a verbal noun to \"\n   \"Av. sav-/sū- 'to benefit', with Old Iranian intervocalic *-t- preserved in the spelling but voiced to -d- in \"\n   \"speech. MacKenzie's entry writes it 'sūd [swt' | M swd, N ~]', i.e. Book Pahlavi swt', Manichaean swd, New \"\n   \"Persian identical; Nyberg (p. 181) glosses 'sūt [swt'] use, advantage, benefit', citing Dēnkard 62.19, 63.13.24.\"),\n \"derivation_fa\": (\"فارسی میانهٔ sūd که در خط پهلوی کتابی <swt'> نوشته می‌شده (و از همین رو نورایی و هرن آن را sūt آورده‌اند) و در \"\n   \"فارسی میانهٔ مانوی <swd> و <swwd> ضبط شده، ادامهٔ ایرانی باستان *sūta- اسم مفعولی از ریشهٔ sav-/sū- است. \"\n   \"تیٔ میان‌واکه‌ای در نوشتار پهلوی تاریخی مانده اما در گفتار به دال نرم شده بود. مکنزی و نیبرگ هر دو همین را می‌گویند؛ \"\n   \"ادعای نورایی درست است.\"),\n \"sources\": [W_SUD],\n \"ref_check\": [\n   {\"ref\": \"HRN:166\", \"status\": \"supports\",\n    \"note\": \"Horn no. 751 (printed p. 166): 'aw. √sav- ‘nützen’; phlv. sūt, sūtīh, sūtōmand, sūtīnītan' — the Pahlavi form and its family, exactly as charted.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 79 s.v. sūd\", \"stance\": \"supports\",\n    \"note\": \"'sūd [swt' | M swd, N ~] use, profit, advantage'; MacKenzie also has 'sūd(ō)mand [swt(ʾww)mnd | N sūdmand] useful'.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p. 181\", \"stance\": \"supports\",\n    \"note\": \"'sūt [swt'] use, advantage, benefit 62¹⁹. 63¹³·²⁴ etc. — MPrs swd; Paz. sud, NP sūd, from Av. (1561) sav- ‘to benefit’'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *sauH, p. 341\", \"stance\": \"supports\",\n    \"note\": \"'*MIDDLE PERSIAN: MMP swd, swwd, BMP swt /sud/ ‘profit, use, advantage’ => DMMPP: 310a'.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2,\n \"lang\": \"Persian\",\n \"words\": \"sŭd «سود» : interest, benefit, advantage\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"NP سود sūd continues MP sūd unchanged — the ū is the inherited long vowel and the final -d simply makes \"\n   \"explicit the value of Book Pahlavi <-t'>; Wiktionary's Persian entry is exactly 'From Middle Persian <swt'>, \"\n   \"𐣘𐣇𐣅 (swd), 𐣘𐣇𐣇𐣅 (swwd /sūd/)'. The extra word سودمند sūdmand 'useful' is likewise a direct continuation of \"\n   \"MP sūd(ō)mand (the Pahlavi suffix -ōmand > NP -mand), and Horn lists it among the Pahlavi family of the word. \"\n   \"The commercial sense 'interest (on money)' is a New Persian specialisation of the inherited 'benefit', already \"\n   \"visible in Horn's Judaeo-Persian citation 'sīd ‘Zinsen’'. The Khāqānī couplet in the box uses the word in the \"\n   \"older sense 'be of benefit to all'.\"),\n \"derivation_fa\": (\"«سود» دنبالهٔ بی‌دگرگونی فارسی میانهٔ sūd است؛ دال پایانی همان ارزش آوایی است که در خط پهلوی کتابی زیر <t'> \"\n   \"پنهان بوده و در فارسی میانهٔ مانوی آشکارا swd نوشته شده است. «سودمند» نیز ادامهٔ sūd(ō)mand پهلوی است \"\n   \"(پسوند -ōmand > -مند). معنی «بهرهٔ پولی» تحول معنایی متأخر از «سود، بهره» است. ادعای نورایی درست است.\"),\n \"sources\": [W_SUD],\n \"ref_check\": [\n   {\"ref\": \"HRN:166\", \"status\": \"supports\",\n    \"note\": \"Horn no. 751 heads the entry with the New Persian word itself: 'sūd ‘Nutzen, Vorteil’. g. sīd ‘Zinsen’. aw. √sav- ‘nützen’; phlv. sūt, sūtīh, sūtōmand, sūtīnītan. bel. sāt, sīt (357); sonst allgemein entlehnt.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 79 s.v. sūd, sūd(ō)mand\", \"stance\": \"supports\",\n    \"note\": \"'sūd [swt' | M swd, N ~] use, profit, advantage'; 'sūd(ō)mand [swt(ʾww)mnd | N sūdmand] useful' — covering Nourai's extra word سودمند too.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p. 181\", \"stance\": \"supports\",\n    \"note\": \"'... MPrs swd; Paz. sud, NP sūd, from Av. (1561) sav- ‘to benefit’'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *sauH, p. 341\", \"stance\": \"supports\",\n    \"note\": \"'*NWIR: Bal. sitʾ, siθ/si- ‘to swell’, NP sūd ‘gain, profit’'.\"},\n   {\"src\": \"ARY\", \"where\": \"latin index\", \"stance\": \"silent\",\n    \"note\": \"grep of ARY_latin_index_pages.txt for SUD / SAVAH as an Iranian headword returns only an unrelated Sanskrit *SAVAH entry; Aryanpur has no سود article.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3,\n \"lang\": \"Sogdian\",\n \"words\": \"swt : interest, benefit\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Gharib no. 9078 'swt B — sōt — benefit — Frag. Len. 60.3': a Buddhist Sogdian noun sōt 'benefit', the \"\n   \"exact Sogdian counterpart of MP sūd < Old Iranian *sūta- to the root sav-/sū-. Sogdian writes the historical \"\n   \"-t, like Book Pahlavi, and Gharib reads the vowel as ō. Nourai hangs it directly from the Avestan root rather \"\n   \"than from Pahlavi, which is correct: Sogdian is an East Iranian sister of Persian, not its descendant.\"),\n \"derivation_fa\": (\"قریب در فرهنگ سغدی شمارهٔ ۹۰۷۸ را چنین آورده است: 'swt B — sōt — benefit' (از متن بودایی Frag. Len. ۶۰،۳). این \"\n   \"واژه هم‌ارز فارسی میانهٔ sūd و بازماندهٔ ایرانی باستان *sūta- از ریشهٔ sav-/sū- است؛ تیٔ پایانی مانند پهلوی کتابی \"\n   \"تاریخی نوشته شده است. چون سغدی زبان ایرانی خاوری و خواهر فارسی است نه فرزند آن، وصل کردن آن به خود ریشه درست است.\"),\n \"sources\": [W_SUD],\n \"ref_check\": [\n   {\"ref\": \"SOD:366\", \"status\": \"supports\",\n    \"note\": \"SOD.txt entry '9078 swt B — sōt — benefit — Frag. Len. 60.3'; it sits at leaf 433 of SOD_pages.txt ≈ printed p. 367, i.e. Nourai's 366 within the file's ±1 offset.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"no. 9078\", \"stance\": \"supports\",\n    \"note\": \"'9078 swt B / sōt / benefit / Frag. Len. 60.3' — form, language and gloss as charted.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *sauH, p. 341\", \"stance\": \"partial\",\n    \"note\": \"Cheung lists Avestan, MP, Khotanese, Bactrian, Balochi and Ossetic continuants of *sauH but no Sogdian noun; he neither confirms nor contradicts Gharib's swt.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p. 181 s.v. sūt\", \"stance\": \"supports\",\n    \"note\": \"Nyberg derives the whole Middle Iranian family from 'Av. (1561) sav- ‘to benefit’, savā- savah-', the same source Gharib's Sogdian word requires.\"}\n ]\n})\ndoc[\"entries\"].append(e1)\n\n# ---------------------------------------------------------------- entry 3\ne3 = {\n \"entry\": 3,\n \"root\": \"Šavala\",\n \"verdict\": \"disputed\",\n \"modern_form\": \"Skt. śabala / śavala 'variegated, brindled, dappled' is a real word, but it is not the accepted source of Persian شال; modern dictionaries derive شال from Skt. śāṭī 'cloth, sari' (via an Indo-Aryan intermediary), with the Chaliyam/Šāliyāt toponym as the rival suggestion\",\n \"note\": (\"The headword itself checks out as Sanskrit: Monier-Williams s.v. śabala '(also written śavala; cf. śabara) \"\n   \"variegated, brindled, dappled, spotted (in RV. x, 14, 10 applied to the two four-eyed watch-dogs of Yama), RV. \"\n   \"&c.' — but the gloss printed in the chart, '(a fabric) marked with colors', adds the 'fabric' out of nothing: \"\n   \"no dictionary gives śavala a textile sense. The derivation of Persian شال from it comes straight from Nourai's \"\n   \"own source, Hobson-Jobson p. 824 ('The Persian word is perhaps of Indian origin, from Skt. savala, \"\n   \"‘variegated’') — a guess Yule himself hedges with 'perhaps'. Modern reference works reject it: the current \"\n   \"American Heritage Dictionary has '[Persian shāl, ultimately from Sanskrit śāṭī, cloth, sari]' and Wiktionary \"\n   \"'Borrowed from an Indo-Aryan language. Compare Hindi दुशाला (duśālā), from Sanskrit शाटी (śāṭī) ... \"\n   \"Sometimes said to be from or influenced by Chāliāt, a Persian pronunciation of Chaliyam in India'. The second \"\n   \"of those two views is the one Nourai himself records in the chart NOTE from Klein, and Lokotsch no. 1802 backs \"\n   \"it with Ibn Baṭṭūṭa IV, 109 on the town of Šāliāt. So the root box as drawn is the weakest link on the page: \"\n   \"the Persian word and every arrow below it are sound, the Sanskrit ancestor is not.\"),\n \"note_fa\": (\"سنسکریت śabala / śavala واژه‌ای واقعی است و مونیر ویلیامز آن را «رنگارنگ، ابلق، خالدار» معنی کرده است؛ اما هیچ \"\n   \"فرهنگی برای آن معنی «پارچه» نیاورده و این افزودهٔ نورایی است. خاستگاه «شال» از این واژه تنها حدس یول در \"\n   \"هابسن‌جابسن (ص ۸۲۴) است که خود با «شاید» همراه شده. پژوهش امروزی آن را رد می‌کند و «شال» را وام‌واژه‌ای از \"\n   \"زبان‌های هندوآریایی و در نهایت از سنسکریت śāṭī «جامه، ساری» می‌داند (فرهنگ میراث آمریکایی، ویکی‌واژه)؛ \"\n   \"احتمال دیگر همان است که خود نورایی از کلاین نقل کرده: نام شهر «شالیات» در هند (به گواهی ابن‌بطوطه ۴،۱۰۹ و \"\n   \"لوکوچ شمارهٔ ۱۸۰۲). خلاصه: ریشهٔ سنسکریت پیشنهادی نورایی پذیرفته نیست، هرچند بقیهٔ زنجیره درست است.\"),\n \"sources\": [MW_SAB, W_SAL, AHD_SH, E_SHAWL],\n \"ref_check\": [\n   {\"ref\": \"HJB:824\", \"status\": \"supports\",\n    \"note\": (\"HJB.txt leaf 868 (= printed p. 824, offset leaf−44): 'SHAWL, s. Pers. and Hind. shāl, also doshāla, ‘a pair \"\n             \"of shawls.’ The Persian word is perhaps of Indian origin, from Skt. savala, ‘variegated.’' The page cited \"\n             \"says what Nourai draws — including the hedging 'perhaps', which the chart drops.\")}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"current online edition, s.v. shawl\", \"stance\": \"contradicts\",\n    \"note\": \"'[Persian shāl, ultimately from Sanskrit śāṭī, cloth, sari.]' — śāṭī, not śavala.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1802\", \"stance\": \"contradicts\",\n    \"note\": \"'Pers. šāl ‘Umschlagetuch’ [ursprünglich wohl ein Eigenname, denn IBN BAṬṬŪTA spricht IV, 109 von einer Stadt Šāliāt in Indien ...]' — a toponym, with no Sanskrit śavala anywhere.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1432 s.v. shawl\", \"stance\": \"contradicts\",\n    \"note\": \"'shawl, n. — Pers. shāl, named after Shaliat, a town in India, where it was first manufactured.' — the alternative Nourai himself notes on the chart.\"}\n ],\n \"nodes\": []\n}\n\ne3[\"nodes\"].append({\n \"id\": 1,\n \"lang\": \"Persian\",\n \"words\": \"šâl 1 «شال ۱» : scarf ; šâl 2, šâlang «شال ۲ ، شالنگ» : a thin rough and inexpensive rug\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"Both Persian words are real and both are old. شال šāl in the sense 'coarse woollen cloth, wrap' is \"\n   \"attested from the 11th century: Asadi's Loghat-e Fors quotes 'Onṣorī (Balkhī): زآن مثل حال من بگشت و بتافت / که \"\n   \"کسی شال جست و دیبا یافت' with the explanation 'شال گلیمی بود کوچک پشمین' — 'a small woollen rug' — which is \"\n   \"Nourai's šāl 2, and Mo'in repeats that gloss in his note to Borhan p. 1228. شالنگ šālang is the same word with \"\n   \"the Persian suffix -ang and is glossed there as a rug/coarse woollen piece too. Meninski (1680), quoted by Yule, \"\n   \"still defines šāl as the humble 'panni viliores ... ex lana et pilis caprinis' thrown over the shoulders by \"\n   \"dervishes; the luxury 'Kashmir shawl' sense is the later specialisation. What is disputed is only the arrow from \"\n   \"the root box: the word is not derivable from Skt. śavala 'variegated' — -v-a- would not vanish and the sense \"\n   \"'variegated' is not that of the Persian word — and modern dictionaries take it either from Skt. śāṭī 'cloth' \"\n   \"through an Indo-Aryan intermediary (AHD, Wiktionary) or from the Malabar town Chaliyam / Šāliāt (Klein, \"\n   \"Lokotsch, after Ibn Baṭṭūṭa IV, 109), which is the view Nourai records in his own NOTE.\"),\n \"derivation_fa\": (\"هر دو واژهٔ فارسی اصیل‌اند و کهن. «شال» در لغت فرس اسدی با شاهد عنصری بلخی آمده و معنیش «گلیمی بود \"\n   \"کوچک پشمین» یعنی همان «شال ۲» نورایی؛ معین نیز در حاشیهٔ برهان (ص ۱۲۲۸) همین را می‌آورد. «شالنگ» همان واژه \"\n   \"با پسوند -نگ است. اما پیوند آن به سنسکریت śavala «رنگارنگ» از نظر آوایی و معنایی نااستوار است؛ پژوهش امروزی \"\n   \"یا آن را از سنسکریت śāṭī «جامه» از راه زبان‌های هندوآریایی می‌داند یا از نام شهر «شالیات» در مالابار. پس خود \"\n   \"واژه‌ها درست‌اند و این پیکان (سنسکریت ← فارسی) است که پذیرفته نیست.\"),\n \"sources\": [W_SAL, AHD_SH, AB_SAL, E_SHAWL],\n \"ref_check\": [\n   {\"ref\": \"HJB:824\", \"status\": \"partial\",\n    \"note\": \"Hobson-Jobson p. 824 gives Pers./Hind. shāl and the Sanskrit savala guess, but marks it 'perhaps'; it does not assert the derivation the chart draws as a firm arrow.\"},\n   {\"ref\": \"KLN:1432\", \"status\": \"contradicts\",\n    \"note\": \"KLN_1966.txt leaf 760 (printed pp. 1432–1433, fixed by the page numerals 1428 on leaf 758 and 1438 on leaf 763): 'shawl, n. — Pers. shāl, named after Shaliat, a town in India, where it was first manufactured. Cp. F. châle, Du. sjaal, G. Schal.' No Sanskrit śavala; Nourai's own NOTE reports this correctly.\"},\n   {\"ref\": \"MON:2000\", \"status\": \"not_checked\",\n    \"note\": \"Mo'in's 6-vol. Farhang-e Farsi is not online with its pagination. Content cross-check via abadis' Mo'in text: 'شال (اِ.) نوعی پارچهٔ ساده یا گلدار که از پشم یا کرک بافند' — no foreign-origin tag at all, i.e. Mo'in treats شال as Persian.\"},\n   {\"ref\": \"FRS:171\", \"status\": \"supports\",\n    \"note\": \"The Loghat-e Fors entry exists and carries exactly the Onṣorī verse printed in the chart: FRS.txt line 12377 'زآن مثل حال من بگشت و بتافت / که کسی شال ...' with the note 'شال گلیم کوچک بود'; index 'شال ۳۱۷'. The page number differs because the copy on disk is Eqbal's 1319/1940 edition, not the Kharazmi 1365 edition Nourai cites (refs_online.json flags this: 'pagination differs — verify the entry, not the page').\"},\n   {\"ref\": \"BQT:1228\", \"status\": \"supports\",\n    \"note\": \"BQT_v3_pages.txt, pdf page 19 = printed p. 1228 (fixed by the numeral ٫۱۲۳۷٫ on pdf p. 28). Mo'in's footnote: '# شال - از فارسی وارد عربی شده «شال» (معرّب) و از عربی وارد فرانسوی châle ...' followed by 'گلیمی بود کوچک پشمین. عنصری (بلخی) گوید: زآن مثل حال من بگشت و بتافت ... «لغت فرس ۳۱۷»' — the source of the chart's Arabic and French boxes and of the verse.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol. 3 p. 1228, Mo'in's footnote to شال / شالنگ\", \"stance\": \"supports\",\n    \"note\": \"'شال - از فارسی وارد عربی شده ... گلیمی بود کوچک پشمین' — the 'thin rough rug' sense and the Persian→Arabic direction; Mo'in gives no Sanskrit source.\"},\n   {\"src\": \"FRS\", \"where\": \"Loghat-e Fors, p. 317 of the Eqbal ed.\", \"stance\": \"supports\",\n    \"note\": \"The Onṣorī verse plus 'شال گلیم کوچک بود' — an 11th-c. attestation of šāl 2.\"},\n   {\"src\": \"HJB\", \"where\": \"p. 824 s.v. SHAWL\", \"stance\": \"partial\",\n    \"note\": \"Yule has the Persian word and the Meninski definition, but offers the Sanskrit savala only as 'perhaps'.\"},\n   {\"src\": \"MON\", \"where\": \"vajehyab/abadis text of Mo'in s.v. شال\", \"stance\": \"partial\",\n    \"note\": \"'(اِ.) نوعی پارچهٔ ساده یا گلدار که از پشم یا کرک بافند' — the word is there with no origin tag, so Mo'in claims no Indian ancestry.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\",\n    \"note\": \"grep of PLA_pages.txt for شال returns nothing — Asbaghi does not list it among the Persian loans in Arabic.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 2,\n \"lang\": \"Hindustani\",\n \"words\": \"šawl : shawl\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The route is right and is the standard one: Persian شال šāl was taken into the Indo-Aryan languages of \"\n   \"north India — Hindi शाल / Urdu شال śāl, with the compound dushālā 'a pair of shawls' recorded by Yule — and it is \"\n   \"from there, not straight from Persian, that the European word was taken in the 17th century; the chart's note \"\n   \"'Through Urdu language' is exactly Wiktionary's 'Borrowed from Hindustani (Hindi शाल / Urdu شال), from \"\n   \"Classical Persian شال'. What is not right is the SHAPE of the word in the box: the Hindustani form is śāl with \"\n   \"a long ā, never *šawl — 'shawl' with -aw- is simply the English spelling of that same ā (compare 'Lahore', \"\n   \"'Mahratta'), which Nourai has copied back into the Hindustani box from the AHD headword. The extraction is \"\n   \"faithful to the printed page, and the derivational claim is unaffected, so this is a wording slip rather than a \"\n   \"wrong etymology.\"),\n \"derivation_fa\": (\"مسیر درست است: «شال» فارسی به زبان‌های هندوآریایی شمال هند (هندی शाल، اردوی شال) وارد شده و از آنجا در \"\n   \"سدهٔ ۱۷م میلادی به انگلیسی رفته است؛ یادداشت کتاب («از راه اردو») درست است. اما صورت مندرج در جعبه یعنی «šawl» \"\n   \"صورت هندوستانی نیست؛ صورت هندی/اردو śāl با الف کشیده است و -aw- تنها رسم‌الخط انگلیسی همان آواست. پس این \"\n   \"لغزش نگارشی خود کتاب است نه خطای ریشه‌شناختی، و ادعا با احتیاط پذیرفتنی است.\"),\n \"sources\": [W_SHAWL, E_SHAWL, W_SAL],\n \"ref_check\": [\n   {\"ref\": \"AHD:1192\", \"status\": \"not_checked\",\n    \"note\": \"p. 1192 is in the main A–Z text of the 1975/76 AHD New College edition, which is not open online (only Watkins' IE-roots appendix is on disk). Cross-checked against the current AHD online, which gives '[Persian shāl, ultimately from Sanskrit śāṭī, cloth, sari]' — it keeps Persian but omits both the Hindustani step and śavala.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HJB\", \"where\": \"p. 824 s.v. SHAWL\", \"stance\": \"supports\",\n    \"note\": \"'SHAWL, s. Pers. and Hind. shāl, also doshāla, ‘a pair of shawls’' — Yule's Hindustani form is shāl, not *shawl.\"},\n   {\"src\": \"AID\", \"where\": \"Whitworth, An Anglo-Indian Dictionary\", \"stance\": \"silent\",\n    \"note\": \"grep -n -i 'shawl' AID.txt finds the word only inside the definitions of Chadar and Kamarband; Whitworth has no headword shawl/shāl.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1432 s.v. shawl\", \"stance\": \"partial\",\n    \"note\": \"Klein goes straight from Persian to English and does not mention an Indo-Aryan intermediary.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 3,\n \"lang\": \"English\",\n \"words\": \"shawl\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English shawl is first recorded in the 1660s, of an article of Asian dress, and reaches English through \"\n   \"the India trade: 'from Urdu and other Indian languages, from Persian shal' (Etymonline), 'Borrowed from \"\n   \"Hindustani (Hindi शाल / Urdu شال), from Classical Persian شال' (Wiktionary). Yule documents the earlier \"\n   \"English trade spellings from the East India Company records — 'Carmania shawools' (1686), 'Chawools' (1704) — \"\n   \"which show the -aw- spelling settling in before the word became the name of a Western woman's garment in 1767. \"\n   \"English is in turn the source of German Schal and, in part, of the other European forms, so this box is the \"\n   \"hinge of the whole European family.\"),\n \"derivation_fa\": (\"انگلیسی shawl از دههٔ ۱۶۶۰ م شاهد دارد و از راه تجارت هند، از اردو/هندی śāl و سرانجام از «شال» فارسی \"\n   \"گرفته شده است. یول صورت‌های کهن بازرگانی «Carmania shawools» (۱۶۸۶) و «Chawools» (۱۷۰۴) را از اسناد \"\n   \"کمپانی هند شرقی نقل می‌کند. ادعای نورایی درست است.\"),\n \"sources\": [E_SHAWL, W_SHAWL],\n \"ref_check\": [\n   {\"ref\": \"AHD:1192\", \"status\": \"not_checked\",\n    \"note\": \"Main-text page of the 1975/76 AHD, not open online; the current AHD online s.v. shawl was consulted instead.\"},\n   {\"ref\": \"KLN\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 760 (printed p. 1432): 'shawl, n. — Pers. shāl, named after Shaliat ... Cp. F. châle, Du. sjaal, G. Schal.'\"},\n   {\"ref\": \"SKT\", \"status\": \"supports\",\n    \"note\": \"SKT.txt line 17058: 'Shawl. (Pers.) Pers. shāl (pron. shawl), a shawl, mantle.' — Skeat even notes that the English spelling represents the Persian ā.\"}\n ],\n \"consulted\": [\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, vol. IV s.v. shawl\", \"stance\": \"supports\",\n    \"note\": \"FSD_vol4.txt line 8712 ends the article '[< Per. shāl, shawl]', with the note that 'the embroidered shawls of Cashmere were the first worn in Europe'.\"},\n   {\"src\": \"HJB\", \"where\": \"p. 824 s.v. SHAWL\", \"stance\": \"supports\",\n    \"note\": \"Yule's Anglo-Indian record: 'Shawles Garmania' (1686), 'Chawools' (1704), and the 17th-c. French travellers' Chal / chalas.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1802\", \"stance\": \"supports\",\n    \"note\": \"'hieraus engl. shawl, ndl. sjaal, dtsch. Schal; russ. šalʹ ... frz. châle ... it. scialle' — all from Pers. šāl.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 4,\n \"lang\": \"Arabic\",\n \"words\": \"šal : a rough rug or thick cloth\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Arabic شال šāl is a mu‘arrab, a straight borrowing of the Persian word with no change of shape (Arabic has \"\n   \"no separate č/ž problem here and š is native, so the loan passes through untouched); it is not built on any \"\n   \"Arabic root and Lane/Wiktionary treat it as foreign. Mo'in states the direction explicitly in his footnote to \"\n   \"Borhan p. 1228 — 'شال از فارسی وارد عربی شده «شال» (معرّب)' — and Tobia al-Unaysi's dictionary of foreign words \"\n   \"in Arabic has 'شال - في الفارسية شال، وهو مطرف ينسج في كشمير الهند' — 'in Persian šāl, a mantle woven in Kashmir in \"\n   \"India'. Wiktionary likewise marks Arabic شال 'Borrowed from Persian شال'. The gloss Nourai gives it, 'a rough \"\n   \"rug or thick cloth', matches the older Persian sense that Meninski and Asadi record, so the semantics of the \"\n   \"loan are right too. The borrowing is late — it is not a Qur'ānic or early-‘Abbāsid word, which is why Asbaghi \"\n   \"does not list it.\"),\n \"derivation_fa\": (\"عربی «شال» معرّب همان واژهٔ فارسی است و هیچ دگرگونی آوایی نیافته؛ ریشهٔ سه‌والفی عربی ندارد. معین در \"\n   \"حاشیهٔ برهان قاطع صریحاً می‌نویسد «شال از فارسی وارد عربی شده»، و طوبیا العنیسی در تفسیر الألفاظ الدخیله \"\n   \"آورده است: «شال – في الفارسية شال، وهو مطرف ينسج في كشمير الهند». این وام‌گیری متأخر است. ادعای نورایی درست است.\"),\n \"sources\": [W_SAL],\n \"ref_check\": [\n   {\"ref\": \"BQT:1228\", \"status\": \"supports\",\n    \"note\": \"Mo'in's footnote on the printed page: '# شال - از فارسی وارد عربی شده «شال» (معرّب) و از عربی وارد فرانسوی châle' (BQT_v3_pages.txt pdf p. 19).\"},\n   {\"ref\": \"FVF:391\", \"status\": \"not_checked\",\n    \"note\": \"Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi — refs_online.json records no downloadable copy (noorlib needs a browser, ketabnak needs a login); nothing on disk.\"}\n ],\n \"consulted\": [\n   {\"src\": \"TAD\", \"where\": \"al-Unaysi, Tafsir al-alfaz al-dakhila, s.v. شال\", \"stance\": \"supports\",\n    \"note\": \"TAD.txt line 1576: 'شال - في الفارسية شال، وهو مطرف ينسج في كشمير الهند'.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi 1988\", \"stance\": \"silent\",\n    \"note\": \"No شال in PLA_pages.txt — the loan is too late for Asbaghi's corpus of classical Arabic Persianisms.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, Kitab al-Alfaz al-Farisiyya al-Mu‘arraba\", \"stance\": \"silent\",\n    \"note\": \"grep of AFM.txt shows شال only inside other entries and a stray 'دو شال'; Addi Shir has no headword شال.\"},\n   {\"src\": \"HJB\", \"where\": \"p. 824\", \"stance\": \"partial\",\n    \"note\": \"Yule gives 'Pers. and Hind. shāl' but does not discuss the Arabic form.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 5,\n \"lang\": \"French\",\n \"words\": \"châle\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"French châle is a real 18th–19th-century word for the Kashmir wrap (the fashion for foreign châles reached \"\n   \"France 'vers le commencement de ce siècle' according to Pihan, i.e. c. 1800), and it does ultimately go back to \"\n   \"Persian شال, so the box is right about the word. The disputed part is the arrow: Nourai routes it through \"\n   \"Arabic, following Mo'in's footnote in Borhan ('و از عربی وارد فرانسوی châle'), but the specialist \"\n   \"dictionaries of French orientalisms deny exactly that. Devic s.v. Châle: 'Bien que le mot se trouve dans la \"\n   \"langue arabe moderne (شال châl ... dans Bocthor), ce n'est pas là que nous l'avons pris. D'introduction peu \"\n   \"ancienne en Europe, il a été apporté de l'Orient par le commerce anglais. C'est le persan شال châl ...' — \"\n   \"i.e. French got it through the English East India trade, from Persian/Indian, not from Arabic. Pihan heads his \"\n   \"article 'CHÂLE, s. m. (p.)' — (p.) = Persian, not (a.) = Arabic — and Lokotsch no. 1802 derives frz. châle \"\n   \"directly from Pers. šāl alongside engl. shawl. Wiktionary lists châle among the direct descendants of Persian \"\n   \"شال. Modern scholarship therefore keeps the box but re-draws its parent as Persian (through English/Indian \"\n   \"trade), not Arabic.\"),\n \"derivation_fa\": (\"فرانسهٔ châle واژه‌ای واقعی است و سرانجام به «شال» فارسی می‌رسد؛ اما میانجی‌گری عربی که نورایی (به پیروی \"\n   \"از حاشیهٔ معین) رسم کرده پذیرفته نیست. دویک می‌نویسد هرچند این واژه در عربی امروزین هست، فرانسه آن \"\n   \"را از عربی نگرفته بلکه از راه تجارت انگلیسی از مشرق‌زمین آورده‌اند؛ پیهان هم مدخل را با نشانهٔ (p.) یعنی \"\n   \"فارسی آورده و لوکوچ نیز châle را یکسره از فارسی می‌گیرد. پس جعبه درست است ولی پیکان آن باید از «فارسی» \"\n   \"کشیده شود نه از «عربی».\"),\n \"sources\": [W_SAL, E_SHAWL],\n \"ref_check\": [\n   {\"ref\": \"BQT:1228\", \"status\": \"supports\",\n    \"note\": \"Mo'in does say it: 'و از عربی وارد فرانسوی châle' (BQT_v3_pages.txt pdf p. 19 = printed 1228). Nourai reproduces his source accurately; it is the source itself that the French Arabists contradict.\"}\n ],\n \"consulted\": [\n   {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique des mots français d'origine orientale, s.v. Châle\", \"stance\": \"contradicts\",\n    \"note\": \"'Bien que le mot se trouve dans la langue arabe moderne (شال châl ... dans Bocthor), ce n'est pas là que nous l'avons pris ... il a été apporté de l'Orient par le commerce anglais. C'est le persan شال châl.'\"},\n   {\"src\": \"PHN\", \"where\": \"Pihan, s.v. CHÂLE\", \"stance\": \"contradicts\",\n    \"note\": \"The headword is tagged '(p.)' = persan, not '(a.)' = arabe, and the article closes 'Schall ... ne peut exactement représenter le mot persan.'\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1802\", \"stance\": \"contradicts\",\n    \"note\": \"'Pers. šāl ... hieraus engl. shawl ... frz. châle, kat. xal, sp. chal ... it. scialle' — all straight from Persian, with no Arabic stage.\"},\n   {\"src\": \"LAM\", \"where\": \"Lammens, Remarques sur les mots français dérivés de l'arabe\", \"stance\": \"silent\",\n    \"note\": \"Lammens has no article on châle (the single hit in LAM.txt is 'chale de Lisbonne' inside another entry), i.e. he does not count it as an Arabism.\"}\n ]\n})\ndoc[\"entries\"].append(e3)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-431.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-431.py",
 "description": "Build page-431.json"
}
```


### [2026-09-14T01:42:33.937Z] TOOL RESULT

```
written
```


## [2026-09-14T01:42:37.955Z] TOOL CALL #81: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-431.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 431",
 "description": "Validate and run verify_check"
}
```


### [2026-09-14T01:42:39.165Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'confirmed': 10, 'transcription_suspect': 1, 'disputed': 2, 'plausible': 1}
root verdicts: {'confirmed': 2, 'disputed': 1}
ref checks: {'supports': 13, 'partial': 3, 'not_checked': 8, 'contradicts': 1}
books consulted: {'supports': 32, 'silent': 7, 'partial': 6, 'contradicts': 3} | by book: {'BRT': 4, 'PHD': 4, 'HJB': 4, 'KLN': 3, 'NYB': 3, 'CHEUNG': 3, 'KNT': 2, 'ARY': 2, 'MON': 2, 'SOD': 2, 'PLA': 2, 'LKT': 2, 'HUB': 1, 'SYN': 1, 'POK': 1, 'IEC': 1, 'SKT': 1, 'WEB': 1, 'BQT': 1, 'FRS': 1, 'AID': 1, 'FSD': 1, 'TAD': 1, 'AFM': 1, 'DEV': 1, 'PHN': 1, 'LAM': 1}
```


## [2026-09-14T01:42:59.871Z] AGENT

Done. Wrote `/home/sfmqrb/git/rishe/data/verification/page-431.json`; `verify_check.py 431` reports 14/14 nodes, 0 PROBLEM lines.

**PDF page 431 (book p. 401) — 3 entries (1 redirect skipped), 14 nodes**

Verdicts: nodes — 10 confirmed, 1 plausible, 2 disputed, 1 transcription_suspect. Roots — 2 confirmed (Saus/Sus, Sav 1), 1 disputed (Šavala).
Ref checks: 13 supports, 3 partial, 1 contradicts, 8 not_checked (ETM, MON, FVF, AHD:1192 — none accessible in any scan).

Flagged items:
- **Šavala (ROOT, disputed)** — Skt. *śabala/śavala* is real ("variegated, dappled", Monier-Williams), but "(a fabric) marked with colors" is Nourai's own addition and the derivation of Persian شال from it is only Yule's hedged "perhaps" (HJB:824). Current AHD and Wiktionary derive شال from Skt. *śāṭī* "cloth, sari" via Indo-Aryan; Klein/Lokotsch prefer the Chaliyam/Šāliāt toponym (the alternative Nourai himself notes).
- **Šavala #1 Persian šâl 1 / šâl 2, šâlang (disputed)** — the Persian words and their 11th-c. attestation (Loghat-e Fors, ʿOnṣorī verse; Mo'in, Borhan p. 1228) check out; only the arrow from Skt. *śavala* fails.
- **Šavala #5 French châle (disputed)** — Nourai follows Mo'in ("از عربی وارد فرانسوی châle"), but Devic (s.v. Châle), Pihan (tagged "(p.)" = Persian) and Lokotsch no. 1802 all say French took it from Persian via the English India trade, not through Arabic.
- **Saus #3 Sogdian "škw" (transcription_suspect, error_in = book)** — Gharib has only *ʾskw* / *skw* / *swk* (nos. 1752, 9238, 9356); no form with š- exists. The printed page (saved to `data/verification/sources/refs/ocr/BOOK/431.png`) shows "škw", so this is Nourai's misprint, faithfully extracted. Correct form: *skw / ʾskw*.
- **Šavala #2 Hindustani "šawl" (plausible)** — route Persian → Hindustani/Urdu → English is correct (Wiktionary, Etymonline), but the Hindustani form is *śāl*; "shawl" with -aw- is the English spelling. Book prints "šawl"; not an extraction error.

**No extraction errors found** — the JSON matches the printed page everywhere. Two page-layout notes for the owner: the box to the right of "Old Persian uška" on the printed page is empty (no language, no word) and the Greek→English arrow passes through a second bare arrowhead; the extractor correctly ignored both.

Useful confirmations along the way: POK:881, KNT:178, HRN:166, NYB:181, SOD:366/373, KLN:1432, HJB:824, BQT:1228 and BQT:752 (Mo'in's footnote, Latin script preserved mirror-reversed in the OCR as "khsuh"/"akhsuh" = hušk/huška-) all check out on the cited pages; BQT vol. 2's leaf→page offset is uncertain by ~2, so the خشک footnote sits at printed 750–753.
