# Verification process log — verify-page-413


## [2026-09-14T01:08:31.057Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 413 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-413.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-413.json. Write /home/sfmqrb/git/rishe/data/verification/page-413.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 413` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:08:32.070Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:08:32.897Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:08:32.912Z] TOOL RESULT

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


## [2026-09-14T01:08:33.476Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-413.txt"
}
```


### [2026-09-14T01:08:33.498Z] TOOL RESULT

```
1	=== PDF page 413 (book page 383) ===
2	--- entry 0 ---
3	ROOT Qusěros -> redirect to Sper
4	--- entry 1 ---
5	ROOT Qusudros -> redirect to Ksudros
6	--- entry 2 ---
7	ROOT Qwe -> redirect to Kwe
8	--- entry 3 ---
9	ROOT Qwei -> redirect to Kwei 1
10	--- entry 4 ---
11	ROOT Qwek -> redirect to Kwek
12	--- entry 5 ---
13	ROOT Qwel -> redirect to Kwel
14	--- entry 6 ---
15	ROOT Qwer -> redirect to Kwer
16	--- entry 7 ---
17	ROOT Qwetwor -> redirect to Kwetwer
18	--- entry 8 ---
19	ROOT Qweye -> redirect to Kweye
20	--- entry 9 ---
21	ROOT Qwi -> redirect to Kwei 1
22	--- entry 10 ---
23	ROOT Qwri -> redirect to Kwri
24	
```


## [2026-09-14T01:08:36.079Z] AGENT

All 11 entries are redirects. Let me confirm against the source JSON and check how prior all-redirect pages were handled.


## [2026-09-14T01:08:38.030Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-413.json'))\nprint(type(d), list(d.keys()) if isinstance(d,dict) else len(d))\nprint(json.dumps(d, ensure_ascii=False)[:3000])\n\"",
 "description": "Inspect source JSON for page 413"
}
```


## [2026-09-14T01:08:38.733Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-14T01:08:39.106Z] TOOL RESULT

```
<class 'dict'> ['pdf_page', 'book_page', 'entries']
{"pdf_page": 413, "book_page": 383, "entries": [{"root": {"name": "Qusěros", "redirect": "Sper"}, "nodes": []}, {"root": {"name": "Qusudros", "redirect": "Ksudros"}, "nodes": []}, {"root": {"name": "Qwe", "redirect": "Kwe"}, "nodes": []}, {"root": {"name": "Qwei", "redirect": "Kwei 1"}, "nodes": []}, {"root": {"name": "Qwek", "redirect": "Kwek"}, "nodes": []}, {"root": {"name": "Qwel", "redirect": "Kwel"}, "nodes": []}, {"root": {"name": "Qwer", "redirect": "Kwer"}, "nodes": []}, {"root": {"name": "Qwetwor", "redirect": "Kwetwer"}, "nodes": []}, {"root": {"name": "Qweye", "redirect": "Kweye"}, "nodes": []}, {"root": {"name": "Qwi", "redirect": "Kwei 1"}, "nodes": []}, {"root": {"name": "Qwri", "redirect": "Kwri"}, "nodes": []}]}
```


### [2026-09-14T01:08:39.144Z] TOOL RESULT

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


## [2026-09-14T01:08:44.195Z] AGENT

All 11 entries are redirects, which the instructions say to skip. Let me check precedent for all-redirect pages, verify the redirect targets exist in the book, and confirm the extraction matches the printed page.


## [2026-09-14T01:08:48.199Z] TOOL CALL #5: Bash

```json
{
 "command": "for f in data/verification/page-*.json; do n=$(python3 -c \"import json,sys;print(len(json.load(open('$f')).get('entries',[])))\" 2>/dev/null); if [ \"$n\" = \"0\" ]; then echo \"EMPTY: $f\"; fi; done | head -20; echo \"---targets---\"; python3 - <<'EOF'\nimport json,glob,os\ntargets=[\"Sper\",\"Ksudros\",\"Kwe\",\"Kwei 1\",\"Kwek\",\"Kwel\",\"Kwer\",\"Kwetwer\",\"Kweye\",\"Kwri\"]\nnames={}\nfor f in glob.glob('data/extracted/batch/page-*.json'):\n    d=json.load(open(f))\n    for e in d['entries']:\n        names.setdefault(e['root']['name'],[]).append((d['pdf_page'], bool(e['root'].get('redirect')), len(e['nodes'])))\nfor t in targets:\n    print(t, '->', names.get(t, 'NOT FOUND'))\nEOF"
}
```


## [2026-09-14T01:08:50.649Z] TOOL CALL #6: Bash

```json
{
 "command": "ls site/pages/413.jpg 2>/dev/null; pdftoppm -f 413 -l 413 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg413 && pdftotext -f 413 -l 413 EtymologicalDictionary-persian-english.pdf - | head -60"
}
```


### [2026-09-14T01:09:06.343Z] TOOL RESULT

```
EMPTY: data/verification/page-146.json
EMPTY: data/verification/page-163.json
---targets---
Sper -> NOT FOUND
Ksudros -> NOT FOUND
Kwe -> NOT FOUND
Kwei 1 -> NOT FOUND
Kwek -> NOT FOUND
Kwel -> NOT FOUND
Kwer -> NOT FOUND
Kwetwer -> NOT FOUND
Kweye -> NOT FOUND
Kwri -> NOT FOUND
```


### [2026-09-14T01:09:08.062Z] TOOL RESULT

```
site/pages/413.jpg
```


## [2026-09-14T01:09:12.673Z] TOOL CALL #7: Bash

```json
{
 "command": "ls data/extracted/batch/ | wc -l && python3 - <<'EOF'\nimport json,glob\nnames=set()\nfor f in glob.glob('/home/sfmqrb/git/rishe/data/extracted/batch/page-*.json'):\n    d=json.load(open(f))\n    for e in d['entries']:\n        names.add(e['root']['name'])\nfor t in [\"Sper\",\"Ksudros\",\"Kwe\",\"Kwei\",\"Kwek\",\"Kwel\",\"Kwer\",\"Kwetwer\",\"Kweye\",\"Kwri\"]:\n    print(t, [n for n in names if n.lower().startswith(t.lower())][:8])\nEOF"
}
```


## [2026-09-14T01:09:13.545Z] TOOL CALL #8: Bash

```json
{
 "command": "pdftotext -f 413 -l 413 EtymologicalDictionary-persian-english.pdf - 2>&1 | head -40; echo \"EXIT=$?\""
}
```


### [2026-09-14T01:09:13.947Z] TOOL RESULT

```
541
Sper ['Spereg, Sphereg, Spergh', 'Spergh', 'Sper, Qusĕros, Kĕros']
Ksudros ['Ksudros, Qusudros']
Kwe ['Kwer, Qwer', 'Kwei 2, Kwoi', 'Kwek, Qwek', 'Kwes', 'Kwel, Qwel', 'Kwen 1', 'Kwei 1, Qwei, Qwi', 'Kwe, Qwe, Kue, Que, Kwi 2']
Kwei ['Kwei 2, Kwoi', 'Kwei 1, Qwei, Qwi', 'Kweit']
Kwek ['Kwek, Qwek']
Kwel ['Kwel, Qwel']
Kwer ['Kwer, Qwer', 'Kwermi']
Kwetwer ['Kwetwer, Qwetwor']
Kweye ['Kweye, Qweye']
Kwri ['Kwri, Qwri']
```


### [2026-09-14T01:09:15.043Z] TOOL RESULT

```
EXIT=0
```


## [2026-09-14T01:09:18.134Z] TOOL CALL #9: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/413.jpg"
}
```


### [2026-09-14T01:09:18.172Z] TOOL RESULT

```

```


## [2026-09-14T01:09:21.465Z] AGENT

The printed page matches the extraction exactly. Let me check the format used for the two existing all-redirect pages, then write the file.


## [2026-09-14T01:09:22.021Z] TOOL CALL #10: Bash

```json
{
 "command": "cat data/verification/page-146.json; echo; cat data/verification/page-163.json"
}
```


### [2026-09-14T01:09:22.073Z] TOOL RESULT

```
{
  "pdf_page": 146,
  "book_page": 116,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "note": "This page contains no charts. Both entries are cross-reference stubs: 'Dyě  see root: Dei' and 'Dyeu  see root: Dei'. Per the verification instructions redirect entries are skipped, so this file carries no entries. Checked against the printed page (site/pages/146.jpg, book p. 116): the page shows exactly two headword boxes with 'see root: Dei' in italics and nothing else, so the extraction in data/extracted/batch/page-146.json is faithful. The redirect target is real: the root box 'Dei, Deiw, Dyeu, Dyě' stands on PDF page 112 (verified in data/verification/page-112.json), and it explicitly lists both Dyě and Dyeu among its variant spellings, so both pointers resolve correctly. Nourai's variants correspond to the standard PIE root *dyew- / *dei̯H- 'to shine; sky, day, god' (Pokorny 183-187 dei-, deia-, di-, deía-).",
  "note_fa": "این صفحه هیچ نموداری ندارد؛ هر دو مدخل آن تنها ارجاع‌دهنده‌اند: «Dyě» و «Dyeu» هر دو به ریشهٔ «Dei» ارجاع داده شده‌اند. بر پایهٔ دستورالعمل ارزیابی، مدخل‌های ارجاعی بررسی نمی‌شوند، پس این پرونده بدون مدخل است. تصویر صفحهٔ چاپی (صفحهٔ ۱۱۶ کتاب) با دادهٔ استخراج‌شده مطابقت کامل دارد و خطای خوانش در کار نیست. ریشهٔ مقصد نیز واقعی است: جعبهٔ «Dei, Deiw, Dyeu, Dyě» در صفحهٔ ۱۱۲ پی‌دی‌اف آمده و هر دو صورت را در خود جای داده است؛ این صورت‌ها همان ریشهٔ شناخته‌شدهٔ هندواروپایی آغازین *dyew- / *dei̯H- «درخشیدن؛ آسمان، روز، خدا» (پوکورنی، صفحات ۱۸۳–۱۸۷) هستند.",
  "entries": []
}

{
  "pdf_page": 163,
  "book_page": 133,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "note": "This page contains no charts. All six entries are cross-reference stubs, printed as a column of six headword boxes each followed by italic 'see root:' and a target: Eueguh -> Wegwh, Eu-es -> Wes 3, Ewan -> Eu 1, Ewegwh -> Wegwh, Ew-es -> Wes 3, Ey -> Ei. Per the verification instructions redirect entries are skipped, so this file carries no entries. Checked against the printed page (rendered with pdftoppm -f 163, copy saved as data/verification/sources/refs/ocr/BOOK/163.png; also site/pages/163.jpg): the page shows exactly those six stubs and nothing else, so the extraction in data/extracted/batch/page-163.json is faithful, including the spelling 'Eueguh' and the running header 'Eueguh | Ey'. All four redirect targets resolve to real root boxes elsewhere in the book, and all four are genuine PIE roots: (1) Wegwh, Ewegwh, Eueguh 'to speak solemnly' stands on PDF page 532 with refs POK:348 - Pokorny's lemma 'eueg^h- (*hue-hueg^h-), Meaning: to praise, worship ... Page(s): 348' (data/verification/sources/refs/POK_full.txt line 29030ff), Watkins/AHD 'weg^wh-, Also eug^wh-. To preach, speak solemnly ... [Pok. ewegvh- 348]' (AHD_watkins1985.txt line 1132), Wiktionary *h1wegwh- 'to promise, to vow' citing Pokorny p. 348; Latin voveo, votum, Greek eukhomai, Skt. vaghat- belong here. (2) Wes 3, Ew-es, Eu-es 'to wear, put on' stands on PDF page 551 with refs POK:1172 - Pokorny 'ues-5 (*haues-5), Meaning: to dress, put on ... Page(s): 1172-1173', Watkins 'wes-4. To clothe. Extension of eu-1 ... [Pok. 5. wes- 1172]', which also explains why Nourai lists Eu-es / Ew-es as variants of the same root. (3) Ewan -> Eu 1: the box 'Eu 1, Ewan, Wa: to be empty' stands on PDF page 162 with refs POK:345 - Pokorny 'eu-1, eua-, ua- ua- (*hue-), Meaning: to lack; empty ... Page(s): 345-346', Watkins 'eu-2. Lacking, empty. Extended forms *eua-, *wa-, *wa- ... [Pok. 1. eu- 345]' (which matches Nourai's variants Ewan = *eua- and Wa = *wa-), Wiktionary *h1weh2- 'to be/become empty' citing Pokorny 345-346. (4) Ey -> Ei: the box 'Ei, Ey, I 1, Ia 1: to go' stands on PDF pages 148-149 with refs POK:293,501; KLN:825 - Pokorny 'ei- (*hei-), Meaning: to go ... Page(s): 293-297', Watkins 'ei-1. To go ... [Pok. 1. ei- 293]', Wiktionary *h1ey- 'to go'. One inconsistency, which belongs to the extraction and not to the book: the root box on PDF page 532 is printed 'Wegwh, Ewegwh, Eueguh' (see data/verification/sources/refs/ocr/BOOK/532.png), but data/extracted/batch/page-532.json records its name as 'Wegwh, Ewegwh, Euegh' - the 'u' of 'Eueguh' was dropped in extraction. The stub on this page is therefore correct as printed, and the pointer Eueguh -> Wegwh resolves exactly once page 532 is fixed. Nourai's own spelling 'Eueguh' is simply his transliteration of Pokorny's eu(e)gwh- with the labiovelar written 'guh' rather than 'gwh'; both spellings occur in the book.",
  "note_fa": "این صفحه هیچ نموداری ندارد؛ هر شش مدخل آن تنها ارجاع‌دهنده‌اند: «Eueguh» و «Ewegwh» به ریشهٔ «Wegwh»، «Eu-es» و «Ew-es» به «Wes 3»، «Ewân» به «Eu 1» و «Ey» به «Ei». بر پایهٔ دستورالعمل ارزیابی، مدخل‌های ارجاعی بررسی نمی‌شوند، پس این پرونده بدون مدخل است. تصویر صفحهٔ چاپی (صفحهٔ ۱۳۳ کتاب) با دادهٔ استخراج‌شده مطابقت کامل دارد و خطای خوانشی در کار نیست. هر چهار ریشهٔ مقصد واقعی‌اند و در جای خود در کتاب آمده‌اند: «Wegwh» در صفحهٔ ۵۳۲ پی‌دی‌اف، برابر با هندواروپایی آغازین *h₁wegʷʰ- «سوگند خوردن، سخن آیینی گفتن» (پوکورنی، صفحهٔ ۳۴۸؛ واتکینز؛ ویکی‌واژه)؛ «Wes 3» در صفحهٔ ۵۵۱، برابر با *wes- «پوشیدن، جامه پوشاندن» (پوکورنی، صفحات ۱۱۷۲–۱۱۷۳)، که واتکینز آن را گسترش‌یافتهٔ همان ریشهٔ eu- می‌داند و همین توضیح می‌دهد چرا نورایی صورت‌های Eu-es و Ew-es را نیز آورده است؛ «Eu 1، Ewân، Wâ» در صفحهٔ ۱۶۲، برابر با *h₁weh₂- «تهی بودن، کم داشتن» (پوکورنی، صفحات ۳۴۵–۳۴۶)؛ و «Ei، Ey» در صفحات ۱۴۸–۱۴۹، برابر با *h₁ey- «رفتن» (پوکورنی، صفحات ۲۹۳–۲۹۷). تنها ناهمخوانی به این صفحه مربوط نیست: در صفحهٔ ۵۳۲ پی‌دی‌اف، کتاب «Wegwh, Ewegwh, Eueguh» چاپ کرده، ولی در دادهٔ استخراج‌شده «Euegh» ثبت شده است؛ این خطای خوانش اسکن است و باید در پروندهٔ page-532.json اصلاح شود.",
  "sources": [
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81weg%CA%B7%CA%B0-",
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wes-",
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81weh%E2%82%82-",
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ey-"
  ],
  "consulted": [
    {"src": "POK", "where": "p. 348 (eueg^h-), p. 345-346 (eu-1), p. 1172-1173 (ues-5), p. 293-297 (ei-)", "stance": "supports", "note": "POK_full.txt: 'Root / lemma: eueg^h-i* huehueg^h-) / Meaning: to praise, worship ... Page(s): 348' (line 29030); 'Root /lemma: eu-1, eua-, ua- ua-(**hue-) / Meaning: to lack; empty ... Page(s): 345-346' (line 28864); 'Root / lemma: ues-5 (* haues-5) / Meaning: to dress, put on ... Page(s): 1172-1173' (line 92484); 'Root / lemma: ei- (*hei-) / Meaning: to go ... Page(s): 293-297' (line 24798). All four match the POK page numbers carried by the target root boxes."},
    {"src": "AHD", "where": "Watkins 1985, s.v. weg^wh-, wes-4, eu-2, ei-1", "stance": "supports", "note": "AHD_watkins1985.txt: 'weg”h-, Also eug’h-. To preach, speak solemnly ... [Pok. ewegvh- 348.]'; 'wes-4. To clothe. Extension of eu-1 ... [Pok. 5. wes- 1172.]'; 'eu-2. Lacking, empty. Extended forms *eua-, *wa-, *wa- ... [Pok. 1. eu- 345.]'; 'ei-1. To go ... [Pok. 1. ei- 293.]'. Watkins' own double headword 'weg^wh-, also eug^wh-' is exactly Nourai's variant pair Wegwh / Ewegwh(Eueguh)."},
    {"src": "BOOK", "where": "printed pp. 133 and 502 (pdf 163, 532)", "stance": "partial", "note": "pdf 163 prints six 'see root:' stubs exactly as extracted; pdf 532 prints the root box as 'Wegwh, Ewegwh, Eueguh : to speak solemnly' while data/extracted/batch/page-532.json has 'Wegwh, Ewegwh, Euegh' - an extraction error on page 532. Images: data/verification/sources/refs/ocr/BOOK/163.png, 532.png."}
  ],
  "entries": []
}
```


## [2026-09-14T01:09:25.363Z] AGENT

Now let me locate the target root boxes in the book and check them against Pokorny and Watkins.


## [2026-09-14T01:09:28.745Z] TOOL CALL #11: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob\ntargets={\"Sper\",\"Ksudros\",\"Kwe\",\"Kwei 1\",\"Kwek\",\"Kwel\",\"Kwer\",\"Kwetwer\",\"Kweye\",\"Kwri\"}\nfor f in sorted(glob.glob('data/extracted/batch/page-*.json'), key=lambda p:int(p.split('-')[-1][:-5])):\n    d=json.load(open(f))\n    for i,e in enumerate(d['entries']):\n        r=e['root']\n        nm=r['name']\n        parts=[p.strip() for p in nm.split(',')]\n        if targets & set(parts):\n            print(d['pdf_page'], 'bk', d['book_page'], '| entry',i,'|', json.dumps(r,ensure_ascii=False)[:400], '| nodes', len(e['nodes']))\nEOF"
}
```


### [2026-09-14T01:09:29.944Z] TOOL RESULT

```
282 bk 252 | entry 1 | {"name": "Ksudros, Qusudros", "lang": "Indo-European", "refs": "IEC:576,1060", "gloss": "coarse, granular, crushed in small pieces"} | nodes 5
288 bk 258 | entry 7 | {"name": "Kwe, Qwe, Kue, Que, Kwi 2", "lang": "Indo-European", "refs": "POK:635", "gloss": "and"} | nodes 6
289 bk 259 | entry 0 | {"name": "Kwei 1, Qwei, Qwi", "lang": "Indo-European", "refs": "POK:637", "gloss": "to pay back, revenge, punish"} | nodes 5
290 bk 260 | entry 1 | {"name": "Kwek, Qwek", "lang": "Indo-European", "refs": "POK:638", "gloss": "to appear, see, show"} | nodes 4
290 bk 260 | entry 2 | {"name": "Kwel, Qwel", "lang": "Indo-European", "refs": "POK:640", "gloss": "to move around, dwell"} | nodes 14
291 bk 261 | entry 0 | {"name": "Kwel, Qwel", "lang": "Indo-European", "refs": "POK:640", "gloss": "to, move around, dwell"} | nodes 12
292 bk 262 | entry 2 | {"name": "Kwer, Qwer", "lang": "Indo-European", "refs": "POK:641", "gloss": "to make, form"} | nodes 7
293 bk 263 | entry 0 | {"name": "Kwer, Qwer", "lang": "Indo-European", "refs": "POK:641", "gloss": "to make, form"} | nodes 9
295 bk 265 | entry 0 | {"name": "Kwetwer, Qwetwor", "lang": "Indo-European", "refs": "POK:642", "gloss": "four"} | nodes 22
296 bk 266 | entry 0 | {"name": "Kweye, Qweye", "lang": "Indo-European", "refs": "KLN:1740; POK:638", "gloss": "quiet, comfortable"} | nodes 6
299 bk 269 | entry 0 | {"name": "Kwri, Qwri", "lang": "Indo-European", "refs": "POK:648", "gloss": "to buy"} | nodes 6
467 bk 437 | entry 2 | {"name": "Sper, Qusĕros, Kĕros", "lang": "Indo-European", "refs": "POK:997; IEC:613,1056", "gloss": "sparrow"} | nodes 6
```


## [2026-09-14T01:09:32.905Z] AGENT

All 11 redirects resolve to real root boxes that explicitly list the Q-variant. Now let me verify those roots in Pokorny and Watkins.


## [2026-09-14T01:09:34.090Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -50"
}
```


### [2026-09-14T01:09:34.141Z] TOOL RESULT

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
```


## [2026-09-14T01:09:35.184Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 63[5-9]\\|Page(s): 64[0-9]\\|Page(s): 99[7-9]\\|Page(s): 648\" POK_full.txt | head -40"
}
```


### [2026-09-14T01:09:35.239Z] TOOL RESULT

```
52371:Page(s): 635 
52393:Page(s): 635 
52437:Page(s): 649 
52549:Page(s): 636-637 
52578:Page(s): 637-638 
52608:Page(s): 638 
52636:Page(s): 638-639 
52640:Page(s): 636 
52758:Page(s): 639-640 
52780:Page(s): 640 
52806:Page(s): 640 
52834:Page(s): 640-641 
52860:Page(s): 641 
52891:Page(s): 641 
52935:Page(s): 641-642 
52957:Page(s): 642 
52974:Page(s): 642 
53063:Page(s): 643-644 
53127:Page(s): 635-636 
53156:Page(s): 636 
53162:Page(s): 649 
53461:Page(s): 644-648 
53508:Page(s): 648 
53549:Page(s): 649 
53578:Page(s): 649 
79654:Page(s): 998 
80358:Page(s): 998-999 
80592:Page(s): 999-1000 
80631:Page(s): 999 
80651:Page(s): 999
```


## [2026-09-14T01:09:38.181Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 52371 52393 52578 52608 52780 52860 52957 53508; do echo \"=== line $L ===\"; sed -n \"$((L-12)),$((L+1))p\" POK_full.txt | grep -n \"Root\\|lemma\\|Meaning\\|Page(s)\"; done"
}
```


## [2026-09-14T01:09:39.466Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sper-\\|sparrow\" POK_full.txt | sed -n '1,20p'; echo \"--- 997 ---\"; grep -n \"Page(s): 99[67]\" POK_full.txt | head"
}
```


### [2026-09-14T01:09:39.546Z] TOOL RESULT

```
=== line 52371 ===
6:Page(s): 626-627 
10:Root / lemma: Icalo-s {* Icehu-lo-s) 
11:Meaning: a kind of big fish 
13:Page(s): 635 
=== line 52393 ===
13:Page(s): 635 
=== line 52578 ===
13:Page(s): 637-638 
=== line 52608 ===
13:Page(s): 638 
=== line 52780 ===
13:Page(s): 640 
=== line 52860 ===
13:Page(s): 641 
=== line 52957 ===
13:Page(s): 642 
=== line 53508 ===
13:Page(s): 648
```


### [2026-09-14T01:09:39.612Z] TOOL RESULT

```
12266:sparrow'; 
44403:loud call, shout, cry, name'; russ. sycb " midget owl, sparrow owl ', Czech syc'owl ' {*Ruk- 
44969:v/fjka-' sparrow', ka/a- - " leise tonend, undeutlich vernehmbar', ka/aka/a-m. ' bewildered 
79633:Note: Erweit. from sper-' twitch, schnellen'. 
79685:Root / lemma: sper-2(g-) 
79687:Meaning: a kind of bird (sparrow?) 
79689:Material: Gothic sparwa. Old English spearwa. Old High German spare ^ sparrow' (*proto 
79711:forms auf p: gr. PN iTTopyiAoq "sparrow', (a)TT£pyouAo(; 6pvi9apiov aypiov Hes.; Old 
79712:High German sperk, sperch, SyO//r/7 'sparrow'. Old Prussian spergla-wana^is] 'Sperber' 
79713:(actually 'Sperlingsgeier'), ablaut, spurglisvn. 'sparrow'. 
79718:Root / lemma: sper-3 
80099:Note: compare /OeA-f sprijhen, spray', further: sper- "sparrow', sper- 'rafter', sp(h)er- 
80117:aspernarfj, apa-sphura-^\NegstoQ>er\6' (: Latin asper-), sphura- "blinking', sphurana- 
80148:cymr. uffarn'2x\V\€ from * opi-sper-no-. 
80613:Meaning: sparrow, finch 
80619:Sperber: 0\d High German sparo' sparrow'), ani^u) 'piepe'; Swedish sp/nk, sp/kke'smaW 
80621:bird, sparrow under a.', engl. (from dem Nord.) sp/nkl\r\c\r\'; Old lndiC/0/7//7^a/ra-m. 'ein 
80627:pincione, span, pinzon, as probably also in Swedish pink ^sparrow', engl. dial, pink, pincti 
86823:'chirp, twitter, from sparrow'; Latvian //7e/'sing'. 
--- 997 ---
43012:Page(s): 996-998
```


## [2026-09-14T01:09:46.362Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=52350 && NR<=53600 && (/^Root \\/ ?lemma/ || /^Meaning:/ || /^Page\\(s\\):/)' POK_full.txt | paste - - - 2>/dev/null | sed -n '1,60p'"
}
```


### [2026-09-14T01:09:47.507Z] TOOL RESULT

```
Page(s): 626-627 	Root / lemma: Icalo-s {* Icehu-lo-s) 	Meaning: a kind of big fish 
Page(s): 635 	Root / lemma: Icas-io-, -lo- {* IC'ehus-lo-) 	Meaning: basket-work 
Page(s): 635 	Meaning: to cough 	Page(s): 649 
Root / lemma: k''ei-1(t){*k''ehu-tj Note: common Proto Germanic -u- > -u-, -y-, -/-. 	Meaning: to observe; to appreciate 	Page(s): 636-637 
Root / lemma: k''ei-2{*k''ehu-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 	Meaning: to pile, stow, gather 	Page(s): 637-638 
Root / lemma: Iceia-, k''lie-{*IC'ehu-es) Note: common Proto Germanic -u- > -u-, -y-, -/-. 	Meaning: to rest quietly, quiet, peaceful 	Page(s): 638 
Root / lemma: IceR-, IcoR-, IceR-s- {* k^ehuR-s-) 	Meaning: to seem, see, show 	Page(s): 638-639 
Root / lemma: k^'e-l {*k''ehu-) 	Page(s): 636 	Root /lemma: k^el-l, k''el9-{*k'^ehulah-) 
Meaning: to turn; wheel; neck? 	Page(s): 639-640 	Root / lemma: lrel-2{*k''ehul-) 
Meaning: far (with regard to place and time) 	Page(s): 640 	Root / lemma: k''el-3{*k''ehul-) 
Meaning: swarm, flock, shoal, school, clan, herd, crowd 	Page(s): 640 	Root / lemma: Icem- {*k''ehum-) 
Meaning: to swallow, sip 	Page(s): 640-641 	Root / lemma: Icene {*k^ehus-) 
Meaning: particle of generalization/uncertainty 	Page(s): 641 	Root / lemma: k''enth-{*k''ehuth-) 
Meaning: to suffer, endure 	Page(s): 641 	Root / lemma: k''er-1 {*k''ehur-) 
Meaning: to do 	Page(s): 641-642 	Root / lemma: k''er-2{*k''ehur-) 
Meaning: a kind of dish or pot 	Page(s): 642 	Root / lemma: k''eru- {*k''ehur-) 
Meaning: to chew; to grind 	Page(s): 642 	Root /lemma: Icetuer-, Icetuor-, ICetur-xw., k''etes(o)r-i. {* k''ehut-ehsor-) 
Meaning: four 	Page(s): 643-644 	Root / lemma: Ice 1 {*k''ehu-) 
Meaning: and (end.) 	Page(s): 635-636 	Root / lemma: Iced- k^od-i^k^ehutt-) 
Meaning: to prick; to drill, sharpen 	Page(s): 636 	Root / lemma: k^t^ei- 
Page(s): 649 	Meaning: indefinite/interrogative pronominal base 	Page(s): 644-648 
Root / lemma: k''rei-{*k''ehur-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 	Meaning: to buy 	Page(s): 648 
Root / lemma: ICfmi-i^ k^ehurmi-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 	Meaning: worm, grub 	Page(s): 649 
Root / lemma: Irsep- (?) {*g''sehup-) 	Meaning: dark 	Page(s): 649 
Root / lemma: /ab^- {*/ehdb^-) 	Meaning: to grab, hold 	Page(s): 652
```


## [2026-09-14T01:10:08.048Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== kwetuer ===\"; grep -n \"Icetuer-, Icetuor-\" POK_full.txt; sed -n '52974,52990p' POK_full.txt; echo \"=== sper-2 ===\"; sed -n '79685,79700p' POK_full.txt; echo \"=== sper2 page ===\"; awk 'NR>=79685 && NR<=79740 && /Page\\(s\\)/' POK_full.txt"
}
```


### [2026-09-14T01:10:09.243Z] TOOL RESULT

```
=== kwetuer ===
52976:Root /lemma: Icetuer-, Icetuor-, ICetur-xw., k''etes(o)r-i. {* k''ehut-ehsor-) 
Page(s): 642 

Root /lemma: Icetuer-, Icetuor-, ICetur-xw., k''etes(o)r-i. {* k''ehut-ehsor-) 

Meaning: four 

Note: (contains?? *50/'"wife, woman') 

Material: 

In a- grade: 

Old Indie catvarahm. (Akk. caturah), catvariu., catasraht; Avestan ca^warom. (Gen. 
caturqm), catarjrdi., npers. cahar, 

Latin quaftuor {a seems, as hom. moupzc;, ©to continue); 
In e- grade: 
=== sper-2 ===
Root / lemma: sper-2(g-) 

Meaning: a kind of bird (sparrow?) 

Material: Gothic sparwa. Old English spearwa. Old High German spare ^ sparrow' (*proto 

Germanic *sparwan-); Middle High German sper//nc Moderr\ High Qerrr\ar\Sperling, 



diminutive; Old Icelandic spgrrds. from *sparwa-z, compare also Modern High German 
Sperber, Old High German sparwari{i\v\a\ ending after Old High German aro^ eagle ' 
transfigured?); 

gr. anapaaiov opvsov i\x(^z^ZQ, arpouGco Hes. (*anapF/7-//c»/77); the formant ^also (??) in 
gr. ijjap, Ionian ep. i^jrip (hom. Akk. PI. ii;r|pa(;), Gen. ijjap6(; 'Star' (originally *ijjapF-(;, 
=== sper2 page ===
Page(s): 991
```


## [2026-09-14T01:10:10.016Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC 576 / 1060 ksudros ===\"; grep -n -i \"ksudro\\|k.sudros\" IEC.txt | head -20; echo \"=== IEC sper 613/1056 ===\"; grep -n -i \"qus.ros\\|kuseros\\|k.eros\" IEC.txt | head"
}
```


### [2026-09-14T01:10:10.113Z] TOOL RESULT

```
=== IEC 576 / 1060 ksudros ===
8230:ksudros (skudhros) ‘coarse, granular; coarse- ness, granules, grit’. Cf. also qusudros, skudh- ros Skt. ksudráh ‘small, fine’; Prakritic ksulla-, id. cf. Romani čulo, adv. ‘little’; (e-gde in) Skt. ksódàmi ‘pulverize’; Av. xsudrom “seed”; Per. xurd ‘small’; Arm. xord ‘sackcloth’; G cf. (with *-dh-) Schotter “clinkers, road-metal, shingle'
=== IEC sper 613/1056 ===
8161:ksërið (1) ‘dry, parch, wither; turn dry, etc. Cf. kseros (1). WP I, 503 Skt. ksáràmi (2) ‘perish’; Arm. cf. xarem (‘sear, brand”, fr. *ksor-2); Per. cf. xirman “barn, threshing-floor'; Gk. cf. kseraino ‘dry’; Lat. seresco, Gre “dry in the sun; get dry’; Li. Seri- uos, -uotis (^wither', intrans.); Latv. seru, sert *dry (grain) in kiln?
8162:ksérió (2) *ill-use, abuse". Cf. kseros (2) Skt. cf. ksaritah (2) 'abused'; Alb. shorr *squeeze'; Pol. szarzac, inf. “abuse, bully, tor- ment
8165:kseros (2) (quseros ?) “sharp, harsh'. (Same as (1)? The alternative initial is suggested by Gk. psorós (rough?) Skt. khárah, kharuh 'rough, harsh'; Oss. cf. áxsálí ‘Juniper’; Tokh. A tsår, B Scire trough, hard’; R cf. Sero-xovatyj ‘rough, rugged’; Ukr. Sory, pl. ‘barbs’. Long-gde in R o-šaràšiť ‘dumbfound’
8842:Kieros (Kéros) ‘dark, grey ON hárr, id.; Ir. cíor & ciar, d R séryj ‘grey’; Cz. Ser, id.
14304:qusaros (1), variant of type quseros, q. v.
14305:qusaros (2). See Supt:Qu
14330:qusero, ið ‘scrape, scratch, itch. Cf. qusoros and next. Per. (ambig. *-ē- or *-0-) xaram, v. ‘scratch, itch’; Alb. cf. shore, f. trash, eruption on skin’; R šàrju, inf: Sàrit, v. Árummage'
14331:quseros ‘rough, harsh’. (Variant: qusóros). Cf. kseros, and WP I, 355 Skt. kharah (frough, sharp, hard’. Phonol. ambig.); Gk. cf. (o-gde) psorós 'rough, un- even'; Tokh. A tsår, id.; Pol. cf. szor-stki, adj. as Skt.
14332:quséros (qusáros? Initial and vocalism pro- blematic) ‘motley’. Variant initial consonant- ism in Indo-Iranian. Cf. WP II, 666 Skt. cf. Caráh, Sàrab, id.; Per. sar, sarak, s. "star. ling’; Gk. psàrós, adj. ‘motley’; pser, gs: -ós, beside psar, m. ‘starling’; Alb. cf. shore ( rash, eruption’, but see quseros above); OCS Sarü, šara, mf. ‘colour’; Sar&jo se, v. “be variegated'; Srb. Sar, adj. ‘motley’; Blg. Sar, m. ‘dye’ be- side šaren, adj. ‘motley’. (The initial conso- nantism of Lat. varius, adj. ‘motley, change- able’ and vārī, mpl. ‘rash, pockmarks? is of uncertain background)
14374:qusõros ‘rough, gritty; gravel, scab, mange’. (Indo-Iran. ambig. cf. ksēr-) Skt. khárah “rough; Per. xāriš, xware "ich, mange’; xaram, v. ‘itch, scratch’; Oss. cf. (z- gde) xür, Dig. xurä ‘gravel, rubble’; Gk. pso- rós, adj. “rough, uneven; scabby’; psóra, f. ‘scab, itch’; Cz. charý ‘shabby, dingy’; Big. cf. xáro ‘rascal; ill-luck’; Li. šuoras, m. ‘scratch, line, groove, stripe; outburst, rage’; Ukr. cf. xaryty, inf. ‘clean’
```


## [2026-09-14T01:10:24.403Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== who is on POK 997 ===\"; grep -n \"Page(s): 99[1-8]\" POK_full.txt | head; echo; for L in $(grep -n \"Page(s): 99[1-7]\" POK_full.txt | cut -d: -f1 | head -12); do echo \"--- $L\"; awk -v l=$L 'NR>=l-40 && NR<=l && (/^Root \\/ ?lemma/||/^Root\\/lemma/||/^Meaning:/)' POK_full.txt | tail -4; done"
}
```


## [2026-09-14T01:10:25.463Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"qusudros\" IEC.txt | head; echo \"--- page tags near 8230 / near qusudros ---\"; ls IEC*; grep -c \"\" IEC.txt"
}
```


### [2026-09-14T01:10:26.212Z] TOOL RESULT

```
=== who is on POK 997 ===
43012:Page(s): 996-998 
79654:Page(s): 998 
79716:Page(s): 991 
79745:Page(s): 991-992 
80091:Page(s): 995-996 
80176:Page(s): 992-993 
80288:Page(s): 993-995 
80306:Page(s): 995 
80324:Page(s): 992 
80358:Page(s): 998-999 

--- 43012
--- 79716
Root / lemma: sper-2(g-) 
Meaning: a kind of bird (sparrow?) 
--- 79745
Root / lemma: sper-3 
Meaning: to turn, wind 
--- 80091
--- 80176
--- 80288
--- 80306
Root / lemma: sp(h)er-3 
Meaning: cattle excrements 
--- 80324
Root / lemma: sp(h)er-3 
Meaning: cattle excrements 
Root / lemma: (s)p(h)er-4, (s)p(h)erag- 
Meaning: to tear; rag, snippet
```


### [2026-09-14T01:10:26.285Z] TOOL RESULT

```
8230:ksudros (skudhros) ‘coarse, granular; coarse- ness, granules, grit’. Cf. also qusudros, skudh- ros Skt. ksudráh ‘small, fine’; Prakritic ksulla-, id. cf. Romani čulo, adv. ‘little’; (e-gde in) Skt. ksódàmi ‘pulverize’; Av. xsudrom “seed”; Per. xurd ‘small’; Arm. xord ‘sackcloth’; G cf. (with *-dh-) Schotter “clinkers, road-metal, shingle'
14335:do, Siditi, v. ‘scorn, if fr. *qusiüd-, but *ksiüd- is possible; and ON skjóttr *piebald' ofa horse) quseudros (qusudros) ‘bent, awry, wrong, false? ; Arm. (zero-gde) xotor ‘awry’; Gk. psudrós ‘false’; Moravian šídrý, adj. 'awry. (Iso- phonic: Blg. šùdrav (1) ‘dirty’) quseuið (quseuð, qusëuãið) "come, become, happen’. Phonol. ambig. (ks-?) Per. šavam, inf; šūdan, v. ‘become, happen’; Blg. (long-gde) šàvam, tr. and intr. ‘sway; move; go; depart’; cf. also šàvra, tr. intr. ‘move’; R cf. ševeliť, inf. tr. ‘stir, move’ qusibà, ið “sway, swish; whip, lash’; qusibos, à, S. id. Skt. ksibami, v. "be drunk’; kgibah, adj. ‘tipsy’: Ir. cf. síobaim, v. “blow, gust? beside sfobhas, m. (Frage, fr. *qusibost-, if here); Welsh chwi- fio, inf. (fly round, wander round beside (short vowel) chwyfio, v. ‘move’; OCS cf. ši- bajo, ati, v. ‘flog’ beside R o-Sibit'sa, inf. ‘err’; za-Sibit, inf. “hurt, bruise’; cf. also R &ibkij ‘swift; ó-Sib, m. ‘tail, brush’; po-Sib, m. “style, manner’; OCS šiba, f. ‘lash’; Srb. šib *brush- wood. Variant of type squib- in OE swipian, ON svipa, v. “flog? beside (long-vowel) EME to swipe, v. id.; swipe, s. ^well-beam', cf. MHG swifen, sv. L “move, go' and (*-i- in) Du. zwiepen, v. ‘lash, flog; totter, sway’. The Gmc. forms display all the variants of sense seen in the Slavonic forms. Cf. also (short vowel in) LG swipp, adj. ‘dashing; shrill’. (The phonology of Lat. vibrāre is uncertain) qusidh- ‘whizz, whistle, blow, whisper. Onomat. Gk. cf. psithurós, On. mn. ‘whisper’; Lat. si- bilus, um, mn. “hiss? beside the Umbrianism implied in OLat. sifilare, Fr. siffler, but Sp. silbar, inf. ‘whisper’; cf. Rumansch sivel, m. ‘blast’; MIr. & Ir. sidhe, m. id.; Br. chwéza, inf. ‘blow, inflate’; chwéz, m. ‘blast’; W chwyddo, inf. ‘swell’; chwydd, m. ‘swelling’. Variants implied in Skt. ksvid-, vb. root “hiss, whizz’ and in Ukr. švydkyj, adj. “swift? qusiið (qusinið) “crush, destroy” Skt. ksinómi, ksinami, v. “destroy” beside ksih, f. ‘destruction’; Av. xSi-, id.; Gk. psío, v. ‘crush’. Extns. of this root are seen in Gk.
14336:quseudros (qusudros) — quso£os, à, us
14376:qusoudhos ‘puny’. Cf. qusudros & ksud-. (Phonology indeterminate in some instances) Skt. cf. ksódhukah, adj. dim. type “hungry”; Av. šud-, v. ‘hunger’ beside Suðo, m. id. (both z-gde); cf. Gk. (?) psüthos, n. (ffalsehood". Infl. of type quseud-, q. v.); ON sauór, pl. sau- ðir, s. sheep’, lit. small animal"); OCS xudŭ, adj. ‘little’; Blg. xud, Srb. hud, adj. ‘bad’; OCz. & Cz. chudý, adj. ‘poor’; Moravian ‘slim, thin’; Ukr. cf. xudoba “cattle?
14377:qusudros ‘worn, granular’. Cf. ksudh- (sic) and qusoudhos. (Phonol. ambig. in some in- stances). WP I, 502 (Various reflexes in Iran.) Skt. ksudráh, adj. ‘crushed; small; humble; mean’; Av. xšudrəm, n. geed Per. cf. (from various dialects) xurd ‘minute, tiny’; sūdan, pp: süde, v. (rub, wear down’, fr. *Ksud- ?); sul ‘feeble, weak-willed'; Romani: cf. culo, adv. "little; Gk. cf. psüdrakes, fpl., & psudrá- kia, npl. ‘pimples, rash’. Radical in Av. x3ud-, v. “pound, crush?
--- page tags near 8230 / near qusudros ---
IEC.txt
20499
```


## [2026-09-14T01:10:37.318Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=42970 && NR<=43013 && (/^Root \\/ ?lemma/||/^Meaning:/||/^Page\\(s\\)/)' POK_full.txt; echo \"=== AHD watkins ===\"; grep -n -i \"^kwe-\\|^kwei-\\|^kwek\\|^kwel-\\|^kwer-\\|^kwetwer\\|^kwrei\\|^sper-\\|kwetwer\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-14T01:10:38.665Z] TOOL RESULT

```
Page(s): 996-998 
=== AHD watkins ===
980:sper-4
1328:CABARET kamer- CABEZON kaput CABLE kap- CABRILLA kapro- CABRIOLET kapro- CACHE ag- CACHEXIA segh- caco- kakka- CACODYL kakka- CACOETHES kakka-, s(w)e- CACOPHONOUS bha-2, kakka- CACOPHONY kakka- CACUMINAL keu-2 CADASTER  steigh- CADAVER kad- CADELLE kat-1 CADENCE kad- CADENT kad- CADET kaput CADRE kWetwer- CADUCEUS kar-2 CADUCICORN kad-, ker-1 CADUCOUS kad- CAECILIAN kaiko- CAECUM kaiko- CAELUM_ kae-id- CAESURA kae-id- CAGE keua-2 CAHIER kWetwer- CAINOTOPHOBIA ken-3 CAIRD kerd-2 CAISSON kap-
1334:CANDENT kand- CANDID kand- CANDIDA kand- CANDIDATE kand- CANDLE kand- CANDOR kand- CANESCENT kas- CANICULA kwon- CANINE kwon- CANKER kar-1 CANNABIS kannabis CANOROUS_ kan- CANT? kan- CANTABILE kan- CANTEEN kanto- CANTICLE kan- CANTILLATE kan- CANTO kan- CANTON kanto- CANTOR kan- CANVAS kannabis CANZONE kan- CAPABLE kap- CAPACIOUS kap- CAPE2 kaput CAPELLA kapro- CAPIAS kap- CAPITAL! kaput CAPITAL? kaput CAPITATE kaput CAPITATION kaput CAPITELLUM kaput CAPITULATE kaput CAPITULUM kaput CAPO! kaput CAPON skep- CAPRIC ACID kapro- CAPRICE kaput CAPRICORN kapro-, ker-1 CAPRIFIG kapro- CAPRIOLE kapro- CAPROIC ACID kapro- CAPSICUM kap- CAPSID kap- CAPSTAN kap- CAPSULE kap- CAPTAIN kaput CAPTION kap- CAPTIOUS kap- CAPTIVATE kap- CAPTIVE kap- CAPTOR kap- CAPTURE kap- CAR kers-2 CARAMEL kolem- CARAT ker-1 CARAVANSARY tere-2 CARBON ker-4 CARBUNCLE ker-4 CARCINO-  kar-1 CARCINOGEN kar-1 CARCINOMA kar-1 CARD? kars- CARDIA kerd-1 CARDIAC kerd-1 CARDIO- kerd-1 CARDOON kars- CARE gar- CAREEN kar-1 CAREER kers-2 CARESS ka- CARET kes-2 CARGO kers-2 CARICATURE kers-2 CARIES ker-5 CARILLON kWetwer- CARINA kar-1 CARIOLE kers-2 CARL karlaz CARLING karlaz CARMINATIVE kars- CARNAGE sker-1 CARNAL sker-1 CARNASSIAL_ sker-1 CARNATION sker-1 CARNET kWetwer- CARNIVAL legh-, sker-1 CARNIVOROUS = sker-1 CAROCHE kers-2 CAROL aulo- CAROTID ker-1 CAROUSE ud- CARP! ger-2 “CARP kerp- CARPAL kwerp- CARPEL kerp- CARPENTER kers-2 CARPET kerp- CARPO- kerp-
1336:CASE2 kap- CASHIER kes-2 CASTE kes-? CASTIGATE kes-2 CASTLE kes-2 CASTRATE kes-2 CATA- kat-1 CATABOLISM gWele-1 CATACHRESIS gher-5 CATACLYSM kleu-2 CATALECTIC slég- CATALEPSY (s)lag¥- CATALOGUE leg-1 CATALYSIS leu-1 CATAMENIA mé-2 CATAPLEXY plak-2 CATAPULT pél- CATARRH sreu- CATASTASIS sta- CATASTROPHE streb(h)- CATCH kap- CATCHPOLE pau- CATECHIZE (s)wagh- CATEGORY ger-1 CATER-CORNERED kWetwer- CATERPILLAR pilo- CATHEDRA sed-1 CATHEPSIN kat-1 CATHETER yé- CATHODE sed-2 CATHOLIC sol- CATION ei-1 CATOPTRIC okw- CATTLE kaput CAUDILLO kaput CAUDLE kele-1 CAULESCENT kaul- CAULICLE kaul- CAULIFLOWER _bhel-3, kaul- CAULINE kaul- CAUSTIC kéu- CAUTERY kéu- CAUTION keue-1 CAVE keue-2 CAVEAT keue-1 CAVERN keue-2 CAVETTO keue-2 CAVIL  kel-8
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
1498:FARCE bhrekw- FARCI bhrekw. FARCY bhrekw- FARE per-2 FARINA bhares- FARINACEOUS _bhares- FARM dher-2 FARRAGINOUS_ bhares- FARRAGO bhares- FARRIER ferrum FARROW! porko- FART perd- FARTHING kWetwer- FARTHINGALE virére FASCES bhasko- FASCIA bhasko- FASCICLE bhasko- FASCINATE bhasko- FASCINE bhasko- FASCISM bhasko- FASHION dhé-1 FAST! past-
1512:FIRE piir- FIRKIN kWetwer- FIRM dher-2 FIRMAMENT dher-2 FIRN pert
1533:FORE- pert FORECLOSE dhwer- FOREFATHER per, peter- FOREGO! ghé- FOREIGN dhwer- FOREMOST per! FORENSIC dhwer- FOREST dhwer- FORESTALL | stel- FORFEIT dhé-1, dhwer- FORFICATE bherdh- FORGE! dhabh- FORGET ghend- FORGIVE ghabh- FORGO ghé- FORLORN leu-! FORLORN HOPE keu-?, leu-1 FORM merph- FORMAL merph- FORMER? per! FORMIC morwi- FORMICARY morwi- FORMICIVOROUS morwi- FORMULA merph- FoRNAX gWher- FORNICATE gWher- FORSAKE sag- ForT bhergh-2 FORTALICE bhergh-2 FORTE! bhergh-2 FORTE? bhergh-2 FORTH pert FORTIFY bhergh-2 FORTIS bhergh-2 FORTISSIMO bhergh-2 FORTITUDE bhergh-2 FORTRESS bhergh-2 FORTY kWetwer- FORUM dhwer- Fossa bhedh- FOSSE bhedh- FossIL bhedh- FOSSORIAL bhedh- FOSTER pa- FOUDROYANT bhel-1 FOUL pu-2
1534:FOUND! bhudh- FOUND? gheu- FOUNDER bhudh- FOUNTAIN dhen-! FOUR kWetwer- FOURTEEN kWetwer- FOURTH kWetwer- FOWL pleu-
2146:QUA kWo- QUACKSALVER gWébh-2, selp- QUADRANT kWetwer- QUADRATE kWetwer- QUADRENNIUM at- QUADRI- kWetwer- QUADRILLE! kWetwer- QUADRILLE? kwetwer- QUADROON kWetwer- QUADRUMANOUS man-2 QUADRUPLE pel-3 QUAESTOR quaerere QUAGMIRE meu- QUAINT gnd- QUALIFY dhé-1 QUALITY kWo- QUANTITY k¥o- QUARANTINE kWetwer- QUARREL! kwes- QUARREL2 kwetwer- QUARRY! kerd-1 QUARRY? kwetwer- QUART kWetwer- QUARTAN kwetwer- QUARTER kWetwer- QUARTO kWetwer- QUARTZ twer-2 QUASH kes-2
2147:QUASI kWo-, swo- QUATERNARY kWetwer- QUATERNION kWetwer- QUATRAIN kwetwer- QUATROCENTO dekm QUATTROCENTO kWetwer- QUAVER gWébh-2 quay kagh-
2155:QUIRE! kwetwer- QUITCH GRASS gWel- QUITTOR pekw- QUODLIBET kWo-, leubh- QUONDAM kWo-
2281:SPRINGE spergh- SPRINKLE (8)preg- SPRIT sper-4 SPROUT sper-4 SPRY (s)preg- SPUME (S)poi-mo- SPUR spere- SPURGE peue- SPURN spere- SPURRY (s)preg- SPURT sper-4 SPUTNIK ksun, pent- SPUTTER spyeu- SPUTUM spyeu- SPY spek- SQUAD kWetwer- SQUALENE (8)kWal-o- SQUARE kWetwer- SQUASH2 kwét- SQUAT ag- SQUIRE skei- SQUIRREL ors-, skeoi- STABLE! sta- STABLE? sta- STACK steg- STACTE stag- STADDLE sta- STADHOLDER sta- STAFF! stebh- STAG stegh- STAGE sta- STAGGER steg- STAGNANT stag- STAIN teng-
2362:TERTIARY trel- TESSERA kWetwer- TESTAMENT trei- TESTIFY trei- TESTIMONY trei- TETCHY deik- TETRA- kWetwer- TETRACHORD ghere- TETRAD kWetwer- TETRADYMITE dwo-
2405:TRAPEZIUM kWetwer-, ped-1
2411:TRIO trei- TRIOECIOUS weik-1 TRIP der-1 TRIPEDAL ped-1 TRIPLE pel-3, trei- TRIPLEX trei- TRIPLOBLASTIC pel-3 TRIREME ere-1 TRISKELION skel-3 TRISMUS | strei- TRISOCTAHEDRON trei- TRITANOPIA ei- TRITE ter * TRITIUM trei- TRITONE trei- TRITURATE tere-1 TRIUMVIR trei-, wi-ro- TRIUNE oi-no- TRIVET ped-1 TRIVIAL wegh- TRIVIUM wegh- TROCAR kwetwer-, trei- TROCHAL dhregh- TROCHANTER dhregh- TROCHE dhregh- TROCHEE dhregh- TROCHLEA dhregh- TROCHOPHORE dhregh- TROGON tere-1 TROIKA trei- TROPE trep-2 TROPHALLAXIS al-1 TROPHIC- threph- TROPHO-  threph- -TROPHY threph-, trep-2 TROPIC trep-2 TROPO- trep-2 -TROPOUS  trep-2 TROT der-1
```


## [2026-09-14T01:10:45.338Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '42995,43015p' POK_full.txt; echo \"==== watkins lemmas ====\"; grep -n -E \"^(kWe-?[0-9]?|kWei-|kWek|kWel-|kWer-|kWetwer-|kWrei-|kWeia-|sper-[0-9])\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-14T01:10:45.556Z] TOOL RESULT

```
probably also Old Church Slavic prbga^ neuer Kornansatz des Weizens ', russ. perga' 
pollen ' ; Old Church Slavic /s-prbgngt/ ^spr'\r\g out', poln. p/erzgn^c^ break, crack (skin)'; 
nasalized Old Bulgarian vbs-prggngt/" sprout ', prggb ' locust, grasshopper '; as 'shooting 
up ' Old Church Slavic prgg/o ' a little snare, noose, a little stretcher ', russ. pruga, pruzina 
"jumping feather', u-prugij^ shooting up flexibly, bulging ', also the family proto Slavic 



*pr§gQ^ tighten, hitch, harness an animal; tense, pull taught, stretch tight ', prggh' yoke ', 
poln. popr^g^beW.' etc. 

Maybe alb. pranga " cuffs ' : Slavic prggh ' yoke '. 

References: WP. II 672 ff., WH. II 566 f., Trautmann 276 f., 278 f., Vasmer 2, 337, 450. 
Page(s): 996-998 

Root / lemma: *uep-1 : uop- : up- 
Meaning: water 
==== watkins lemmas ====
980:sper-4
```


## [2026-09-14T01:10:56.321Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E \"Pok\\. (2\\. )?k.etuer|Pok\\. .*642|k.etwer-\\. Four|Four\\.\" AHD_watkins1985.txt | head; echo ---; grep -n \"Four\\.\" AHD_watkins1985.txt | head; echo \"--- sper-4 ctx ---\"; sed -n '978,984p' AHD_watkins1985.txt"
}
```


### [2026-09-14T01:10:56.453Z] TOOL RESULT

```
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
654:four (genitive tessardn): TESSERA; DIATESSARON. c. Greek tetras, group of four: TETRAD; d. zero-grade form *k¥t(w)r- in Greek tra-, four: TRAPEZIUM. III. Ordi- nal adjective *ketur-to-. 1. Germanic *fe(d)worthén- in: a. Old English féortha, féowertha, fourth: FOURTH; b. Middle Dutch veerdel, one-fourth: FIRKIN; c. Old English féorthing, féorthung, fourth part of a penny: FARTHING. 2. Latin qudrtus, fourth, quarter: QUA- DRILLE?, QUADROON, QUART, QUARTAN, QUARTER, quarto. [Pok. kvetuer- 642.]
---
652:kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
--- sper-4 ctx ---
spé-'
in: a. Latin sollus, whole, entire, unbroken: SOLICITOUS; b. Latin sollemnis (second element obscure), celebrated at fixed dates (said of religious rites), established, relig- ious, solemn: SOLEMN. II. Variant form *sob-. 1. Suffixed zero-grade form *sb-u- giving *sal-u- in Latin saliis, health, a whole or sound condition: SALUBRIOUS, SALU- TARY, SALUTE. 2. Suffixed zero-grade form “slo-wo- giv- ing *sala-wo- in Latin salvus, whole, safe, healthy, uninjured: SAFE, SAGE?, SALVAGE, SALVO!, SAVE!, SAVE. [Pok. solo- 979.] sp6-1. To thrive, prosper. Contracted from *spea-. 1. Suf- fixed o-grade form *sp6-ti- in Germanic *spddiz in Old English spéd, success: SPEED. 2. Suffixed form *spé-s- in Latin spés (plural spérés), hope, with denominative spérdre, to hope: DESPAIR, ESPERANCE. 3. Suffixed zero-grade form “spo-ro- in Latin prosperus, favorable, prosperous (traditionally regarded as from pro spéré, according to one’s hope; pro-, according to; see per’): PROSPER. [Pok. 3. sp(h)éi- 983.] spé-?. Long, flat piece of wood. Contracted from *speo-. I. Basic form *spé-. 1. Germanic *spé-nu- in: a. Old English spén, chip of wood, splinter: SPOON; b. Old Norse spdnn, shingle, chip: SPANNEW. 2. Possibly Greek sphén, wedge (formation unclear; earliest Greek form *sphdan): SPHENE, SPHENO-. II. Suffixed zero-grade form *spa-dh-. 1. Germanic *spadan in: a. Old English spadu, digging tool: sPADE!; b. Middle High German spat (> German Spat), spar: SPATHIC. 2. Greek spathé, broad blade: SPADE?, SPATHE, SPATULA, SPAY. [Pok. sp(hjé- 980.] spei-. Sharp point. I. Basic form *spei-. 1. Germanic *spituz in Old English spitu, stake on which meat is roasted: sPIT?. 2. Germanic *spitja- in German spitz, pointed: spitz. 3. Germanic *spi-ra- in: a. Old English spir, slender stalk: SPIRE!; ACROSPIRE; b. possibly Mid- dle Dutch spierlinc, a small, slender fish, smelt, akin to the source of Old French esperlinge, smelt: SPARLING. 4. Germanic “spik- in Old Norse spik, nail, perhaps akin to the possible source of Middle English spyk, spike: SPIKE}. 5. Germanic *spil- in Middle Low German spile, wooden peg: SPILE, SPILL?. 6. Suffixed form *spei-nd in Latin spina (> Old French espin), thorn, prickle, spine: SPINE, SPINEL, SPINNEY; PORCUPINE. 7. Suffixed form *spei-kd in Latin spica, point, ear of grain: SPICA, SPICA, SPICULUM, SPIKE?. IT. Extended o-grade form *spoig- in Germanic *spaik6én- in Old English spdca, spoke: SPOKE}. [Pok. 1. sp(hjéi- 981.] (s)peik-. Bird’s name, woodpecker, magpie. 1. Suffixed form *peik-o- in Latin picus, woodpecker: PICARO, (PICKET), (PIKE!), (PIQUE). 2. Suffixed form *peik-d- in Latin pica, magpie: PICA2, PIE2. [Pok. (s)piko- 999.] spek-. To observe. I. Basic form *spek-. 1. Germanic *spehon in: a. Old French espier, to watch: ESPY, SPY; b. Germanic derivative *speh-6n-, watcher, in Old Italian spione, spy: ESPIONAGE. 2. Suffixed form *spek-yo- in Latin specere, to look at: SPECIMEN, SPECIOUS, SPECTA- CLE, SPECTRUM, SPECULATE, SPECULUM; ASPECT, AUS- PICE, CIRCUMSPECT, CONSPICUOUS, DESPISE, EXPECT, FRONTISPIECE, INSPECT, INTROSPECT, PERSPECTIVE, PROSPECT, RESPECT, (RESPITE), RETROSPECT, SUSPECT. 3. Latin speciés, a seeing, sight, form: SPECIES; ESPE- CIAL. 4, Latin -spex (< *-spek-), “he who sees,” in: a. haruspex, diviner (see ghere-); b. auspex, augur (see awi-). 5, Suffixed form *spek-d- in Latin (denominative) déspicari, to despise, look down on (de-, down; see de-): DESPICABLE. 6. Suffixed metathetical form *skep-yo- in Greek skeptesthai, to examine, consider: SKEPTIC. IT. Ex- tended o-grade form “spoko- metathesized in Greek skopos, one who watches, also object of attention, goal, and its denominative skopein (< *skop-eyo-), to see: SCOPE, -SCOPE, -SCOPY; BISHOP, EPISCOPAL, HOROSCOPE, TELESCOPE. [Pok. spek- 984.] spel-'. To split, break off. 1. Extended form *speld- in Germanic *spilt- in Middle Dutch spelte, wheat (prob-
sper-4
ably from the splitting of its husk at threshing), akin to the Germanic source of Late Latin spelta, spelt: SPELT!. 2. Extended form ‘*spelt- in Germanic *spilthjan in Old English spillan, to spill, destroy: sPILLt. 3. Suffixed o-grade form *spol-yo- perhaps in Latin spolium, hide torn from an animal, armor stripped from an enemy, booty: SPOIL; DESPOIL. [Pok. 1. (s)p(h)el- 985.] spel-2. To shine, glow. Extended form *splend- in Latin splendére, to shine: SPLENDID; RESPLENDENT. [Pok. 2. (s)p(h)el- 987.] spel-3. To say aloud, recite. Suffixed form *spel-no-. 1. Germanic *spellam in: a. Old English spell, discourse, story: SPELL?; b. Old English spel, news: GOSPEL. 2. Ger- manic denominative *spellén in Old French espeller, espelir, to read out: SPELL!. [Pok. (s)pel- 985.] spelgh-. Spleen, milt. 1. Deformation *(pjlihén in Latin lién, milt, spleen: LIENAL. 2. Uncertain preform in: a. Greek splén, spleen: SPLEEN; b. Greek splankhna, inward parts: SPLANCHNIC. [Pok. sp(h)elgh(en) 987.] (s)pen-. To draw, stretch, spin. I. Basic form *spen-. 1. Suffixed form *spen-wo- in Germanic *spinnan, to spin, in: a. Old English spinnan, to spin, with derivative *spin-thron-, “the spinner,” contracted to spithra, spi- der: SPIN, SPIDER; b. Germanic derivative *spin-ilén in Old English spinel, spindle: SPINDLE. 2. Extended form *pend- in Latin pendére, to hang (intransitive), and pendere, to cause to hang, weigh, with its frequentative pensdre, to weigh: PAINTER2, (PANSY), PENCHANT, PEN- DANT, PENDENTIVE, PENDULOUS, PENSILE, PENSION}, PENSIVE, PESO, POISE!; ANTEPENDIUM, APPEND, (APPEN- DIX), COMPENDIUM, COMPENSATE, DEPEND, DISPENSE, EXPEND, IMPEND, PENTHOUSE, PERPEND, PERPENDICU- LAR, PREPENSE, PROPEND, SUSPEND, VILIPEND. 3. Per- haps suffixed form *pen-ya- in Greek penia, lack, poverty (< “a strain, exhaustion”): -PENIA. II. O-grade forms *spon-, *pon-. 1. Germanic “spannan in: a. Middle Dutch spannen, to bind: SPAN; b. Old High German spannan (> German spannen), to stretch: SPANNER. 2. Germanic *spanno- in Old English span(n), distance: SPAN], 3. Perhaps Germanic *spangé in Middle Dutch spange, clasp: SPANGLE. 4. Suffixed and extended form *pond-o- in Latin pondé, by weight: PoUND!. 5. Suffixed and extended form *pond-es- in Latin pondus (stem ponder-), weight, and its denominative ponderdre, to weigh: PONDER, PONDEROUS; EQUIPONDERATE, PREPON- DERATE. 6. Perhaps suffixed form *spon-t- in Latin sponte, of one’s own accord, spontaneously: SPONTANE- ous. 7. Greek penesthai, to toil, with o-grade derivatives ponos, toil, and ponein, to toil: GEOPoNic. [Pok. (s)pen-(d)- 988.] spend-. To make an offering, perform a rite, hence to engage oneself by a ritual act. O-grade form *spond-. 1. Suffixed form *spond-eyo- in Latin spondére, to make a solemn promise, pledge, betroth: SPONSOR, SPOUSE; DESPOND, ESPOUSE, RESPOND. 2. Suffixed form *spond-a in Greek spondé, libation, offering: SPONDEE. [Pok. spend- 989.]} sper-'. Spear, pole. 1. Germanic *speru- in: a. Old Eng- lish spere, spear: SPEAR; b. Middle Low German spér, spit: SPARERIBS. 2. Germanic *sparjén- in Old Norse sperra, rafter, beam: SPAR}. [Pok. 1. (s)per- 990.] sper-2. To turn, twist. 1. Suffixed form *sper-ya- in Greek speira, a winding, coil, spire: SPIRE?. 2. Suffixed zero-grade form *spr-to- in Greek sparton, rope, cable: ESPARTO. [Pok. 3. sper- 991.] . sper-3. Bird’s name, sparrow. Suffixed o-grade form *spor-wo- in Germanic *sparwan- in Old English spearwa, spearwe, sparrow: SPARROW. [Pok. sper-(g)- 997.] sper-4. To strew. I. Zero-grade form *spr-. 1. Germanic *spr- in Old English spréawlian, to sprawl: SPRAWL. 2. Extended form *spreut- in Germanic *sprit- in: a. Old English spriitan, to sprout: SPROUT; b. Old English spryttan, to sprout, come forth: sPpuRT; c. Old English
spere-
spréot, pole (< “sprout, stem”): sPRIT; d. Middle English bouspret, bowsprit: BOwsPRIT. 3. Extended form *spreit- in Germanic *spraidjan in Old English sprédan, to spread: SPREAD. II. Basic form *sper-. 1. Suffixed form *sper-yo- in Greek speirein, to scatter: Diaspora. 2. Suf- fixed form *sper-mn in Greek sperma, sperm, seed (< “that which is scattered”): SPERM}. III. O-grade form *spor-. 1. Suffixed form *spor-d- in Greek spora, a sowing, seed: SPORE, SPORO-. 2. Suffixed form *spor-nd- in Greek sporas (stem sporad-), scattered, dispersed: SPORADIC. [Pok. 2. (s)p(hJer- 993.]
spere-. Ankle. Zero-grade form *spr(o)-. 1. Germanic suffixed form *spur-6n- in Old English spura, spora, spur: SPUR. 2. Nasalized form “spr-n-o- in Germanic *spurnon in Old English spurnan, spornan, to kick, strike against: SPURN. 3. Germanic suffixed form *spur- am in Middle Dutch spor, spoor, track of an animal: Spoor. [Pok. 1. sp(hJer- 992.]
```


## [2026-09-14T01:11:06.481Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o -E \"k.e[a-z]*-?[0-9]?\\. [A-Z][^.]{0,45}\\. [^]]{0,10}\\[Pok\\. [^]]{0,40}\\]\" AHD_watkins1985.txt | grep -iE \"and\\.|pay|penalt|appear|see|revolve|turn|rest|quiet|buy|exchange\" | head -20; echo \"=== targeted ===\"; grep -o -E \"kw(rei|eia|ei|ek|el|e)-?[0-9]?\\.[^[]{0,300}\\[Pok\\.[^]]*\\]\" AHD_watkins1985.txt | cut -c1-260 | head -20"
}
```


### [2026-09-14T01:11:07.835Z] TOOL RESULT

```
=== targeted ===
kwei-. To hiss, whistle. Imitative root. Germanic *hwi-n- and *hwis- in: a. Old English hwinan, to whine: WHINE; b. Old English Awisprian, to whisper: WHISPER; Cc. Old English hAwistlian, to whistle: WHISTLE. [Pok. 2. kuei- 628.]
kwei-2. To pile up, build, make. O-grade form *koi- in: a. Sanskrit kayah, body: CHEETAH; b. suffixed form *koi-wo-, making, in denominative verb *k“oiw-eyo- in Greek poiein, to make, create: POEM, POESY, POET, POETIC, -POIESIS, -POIETIC; MYTHOPOEIC, ONOMATO
kwek-. To appear, see, show. Variant form *kveg- in Slavic *kaz- in Russian ukazat’, to order: UKASE. [Pok. k#ek- 638.]
```


## [2026-09-14T01:11:14.794Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o -E \"kw(rei|eia|ei-1|el-1|el-|e-)[^[]{0,220}\\[Pok\\.[^]]*\\]\" AHD_watkins1985.txt | cut -c1-240 | head; echo \"=== kwei-1 / kweia / kwrei ===\"; grep -o -E \"k.(rei|eia|ei)-?1?\\.[^[]{0,200}\\[Pok\\.[^]]*\\]\" AHD_watkins1985.txt | grep -iE \"pay|penal|rest|quiet|buy\" | cut -c1-300 | head"
}
```


### [2026-09-14T01:11:16.070Z] TOOL RESULT

```
=== kwei-1 / kweia / kwrei ===
```


## [2026-09-14T01:11:19.432Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o -E \".{0,120}Pok\\. (1\\. )?k.(rei|eia|ei)-[^]]*\\]\" AHD_watkins1985.txt | head; echo \"=== and / quiet / buy ===\"; grep -o -E \".{0,180}\\[Pok\\. k.(e|ei|eia|rei)-?1?,? 6(35|36|37|38|48)[^]]*\\]\" AHD_watkins1985.txt | head"
}
```


### [2026-09-14T01:11:24.611Z] TOOL RESULT

```
e, to move the eyelids, wink: NICTITATE. 3. Uncertain preform in Latin niti, to lean forward, strive: NISUS; RENITENT. [Pok. knei-geh- 608.]
to Latin as poena, penalty: PAIN, PENAL, (PENALTY), PINE?, PUNISH; IMPUNITY, PENOLOGY, (PUNITORY), (REPINE), SUBPOENA. [Pok. k#ei-t- 636.]
7.] kweia-'. To value, honor. Suffixed zero-grade form *kvi-ma (< *kvia-md) in Greek timé, honor, worth: TImocrAcy. [In Pok. kvei-(t-) 636.]
=== and / quiet / buy ===
sible root. Suffixed vari- ant form *kwét-so- in Common Slavic *kvasi in Russian kvas, kvass: Kvass. [Pok. kuat(h)- 627.] kwe, And (enclitic). Latin -que, and: SESQUI-, UBIQUITY. [Pok. kve 635.]
```


## [2026-09-14T01:11:35.570Z] AGENT

All targets check out in Pokorny and Watkins. Now let me write the verification file.


## [2026-09-14T01:12:38.681Z] TOOL CALL #27: Bash

```json
{
 "command": "cat > data/verification/page-413.json <<'JSONEOF'\n{\n  \"pdf_page\": 413,\n  \"book_page\": 383,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"note\": \"This page contains no charts. All eleven entries are cross-reference stubs, printed as a single column of eleven headword boxes each followed by italic 'see root:' and a target: Qusěros -> Sper, Qusudros -> Ksudros, Qwe -> Kwe, Qwei -> Kwei 1, Qwek -> Kwek, Qwel -> Kwel, Qwer -> Kwer, Qwetwor -> Kwetwer, Qweye -> Kweye, Qwi -> Kwei 1, Qwri -> Kwri. Per the verification instructions redirect entries are skipped, so this file carries no entries. Checked against the printed page (site/pages/413.jpg, book p. 383, running header 'Quseros | Qwri'): the page shows exactly those eleven stubs and nothing else, and the JSON in data/extracted/batch/page-413.json reproduces all eleven headwords and all eleven targets correctly, including the breve of 'Quseros' and the disambiguating numeral in 'Kwei 1' (used twice, for Qwei and for Qwi). The extraction is faithful; no extraction error on this page. All ten distinct redirect targets resolve to real root boxes elsewhere in the book, and in every case the target box itself carries the Q-spelling of this page among its variant names, so the pointers are internally consistent: (1) Sper -> box 'Sper, Qusěros, Kěros: sparrow', pdf 467 (book 437), refs POK:997; IEC:613,1056; (2) Ksudros -> 'Ksudros, Qusudros: coarse, granular, crushed in small pieces', pdf 282 (book 252), refs IEC:576,1060; (3) Kwe -> 'Kwe, Qwe, Kue, Que, Kwi 2: and', pdf 288, POK:635; (4) Kwei 1 -> 'Kwei 1, Qwei, Qwi: to pay back, revenge, punish', pdf 289, POK:637 (this one box absorbs both Qwei and Qwi, which is why two stubs point at it); (5) Kwek -> 'Kwek, Qwek: to appear, see, show', pdf 290, POK:638; (6) Kwel -> 'Kwel, Qwel: to move around, dwell', pdf 290-291, POK:640; (7) Kwer -> 'Kwer, Qwer: to make, form', pdf 292-293, POK:641; (8) Kwetwer -> 'Kwetwer, Qwetwor: four', pdf 295, POK:642; (9) Kweye -> 'Kweye, Qweye: quiet, comfortable', pdf 296, KLN:1740; POK:638; (10) Kwri -> 'Kwri, Qwri: to buy', pdf 299, POK:648. Nine of the ten are genuine PIE roots with exactly the Pokorny pages the target boxes cite: POK_full.txt gives 'Root / lemma: k\\\"e 1 (*k\\\"ehu-) / Meaning: and (end.) / Page(s): 635-636'; 'k\\\"ei-1(t) / Meaning: to observe; to appreciate / Page(s): 636-637' (Pokorny's lemma covers both 'in Ehren halten' and 'buessen, suehnen, strafen', which is Nourai's gloss); 'k\\\"ek-, k\\\"ok-, k\\\"ek-s- / Meaning: to seem, see, show / Page(s): 638-639'; 'k\\\"el-1, k\\\"ela- / Meaning: to turn; wheel; neck? / Page(s): 639-640'; 'k\\\"eia-, k\\\"iie- / Meaning: to rest quietly, quiet, peaceful / Page(s): 638'; 'k\\\"er-1 / Meaning: to do / Page(s): 641-642'; 'k\\\"etuer-, k\\\"etuor-, k\\\"etur- / Meaning: four / Page(s): 642'; 'k\\\"rei- / Meaning: to buy / Page(s): 648'. The tenth, Ksudros, has no Pokorny lemma and is cited from Mann's IEC instead, where both members of the pair stand and cross-refer to each other, exactly as Nourai's redirect does. Nourai's Q-vs-K doublets are purely a transliteration convention: he writes the PIE labiovelar *kʷ sometimes as Kw- and sometimes as Qw-/Qu- (Q = the older Brugmann/Pokorny notation qʷ), so 'Qwetwor' and 'Kwetwer' are one and the same root *kʷetwor- 'four'. That is why the whole of book page 383 is nothing but a pointer table from the Q- spellings back to the Kw- spellings, where the charts actually stand.\",\n  \"note_fa\": \"این صفحه هیچ نموداری ندارد؛ هر یازده مدخل آن تنها ارجاع‌دهنده‌اند و در یک ستون چاپ شده‌اند: «Qusěros» به «Sper»، «Qusudros» به «Ksudros»، «Qwe» به «Kwe»، «Qwei» و «Qwi» هر دو به «Kwei 1»، «Qwek» به «Kwek»، «Qwel» به «Kwel»، «Qwer» به «Kwer»، «Qwetwor» به «Kwetwer»، «Qweye» به «Kweye» و «Qwri» به «Kwri». بر پایهٔ دستورالعمل ارزیابی، مدخل‌های ارجاعی بررسی نمی‌شوند، پس این پرونده بدون مدخل است. تصویر صفحهٔ چاپی (صفحهٔ ۳۸۳ کتاب، سرصفحهٔ «Quseros | Qwri») با دادهٔ استخراج‌شده مطابقت کامل دارد و خطای خوانش اسکن در کار نیست. علت وجود این جفت‌های «ق/ک» صرفاً شیوهٔ آوانگاری نورایی است: او واکِ لبی‌کامی هندواروپایی آغازین *kʷ را گاه Kw- و گاه Qw-/Qu- می‌نویسد (حرف Q همان نشانهٔ کهن‌تر qʷ در سنت بروگمان و پوکورنی است)؛ بنابراین «Qwetwor» و «Kwetwer» یک ریشه‌اند، یعنی *kʷetwor- «چهار». هر ده ریشهٔ مقصد واقعی‌اند و جعبهٔ هر یک در جای خود در کتاب آمده و خودِ صورت Q-دار را نیز در میان نام‌های خود دارد: Sper در صفحهٔ ۴۶۷ پی‌دی‌اف، Ksudros در ۲۸۲، Kwe در ۲۸۸، Kwei 1 در ۲۸۹، Kwek و Kwel در ۲۹۰، Kwer در ۲۹۲–۲۹۳، Kwetwer در ۲۹۵، Kweye در ۲۹۶ و Kwri در ۲۹۹. ارجاع‌های پوکورنی نیز درست‌اند: *kʷe «و» (صفحات ۶۳۵–۶۳۶)، *kʷei- «تاوان دادن، کیفر» (۶۳۶–۶۳۷)، *kʷeḱ- «نمودن، دیدن» (۶۳۸–۶۳۹)، *kʷel- «گردیدن، به سر بردن» (۶۳۹–۶۴۰)، *kʷeyə- «آرام، آسوده» (۶۳۸)، *kʷer- «ساختن، کردن» (۶۴۱–۶۴۲)، *kʷetwer- «چهار» (۶۴۲) و *kʷrei- «خریدن» (۶۴۸). تنها Ksudros در پوکورنی سرمدخل ندارد و نورایی آن را از فرهنگ مان (IEC) گرفته است؛ در همان فرهنگ نیز دو صورت ksudros و qusudros به یکدیگر ارجاع داده شده‌اند، درست همان‌گونه که نورایی آورده است. ارزیابی: ادعای این صفحه (که سراسر ارجاع است) درست است و داده‌ها بی‌عیب استخراج شده‌اند.\",\n  \"consulted\": [\n    {\"src\": \"BOOK\", \"where\": \"printed p. 383 (pdf 413), site/pages/413.jpg\", \"stance\": \"supports\", \"note\": \"The image shows eleven headword boxes in one column, each with italic 'see root:' and a target, and page number 383 at the foot: 'Quseros / see root: Sper', 'Qusudros / Ksudros', 'Qwe / Kwe', 'Qwei / Kwei 1', 'Qwek / Kwek', 'Qwel / Kwel', 'Qwer / Kwer', 'Qwetwor / Kwetwer', 'Qweye / Kweye', 'Qwi / Kwei 1', 'Qwri / Kwri'. Identical to data/extracted/batch/page-413.json, so the extraction is faithful and there is nothing to flag.\"},\n    {\"src\": \"POK\", \"where\": \"IEW pp. 635-636, 636-637, 638, 638-639, 639-640, 641-642, 642, 648\", \"stance\": \"supports\", \"note\": \"grep 'Page(s): 63[5-9]|64[0-9]|648' in data/verification/sources/refs/POK_full.txt (lines 52371-53600) yields, in order: 'Root / lemma: k\\\"e 1 (*k\\\"ehu-) | Meaning: and (end.) | Page(s): 635-636'; 'k\\\"ei-1(t) | to observe; to appreciate | 636-637'; 'k\\\"eia-, k\\\"iie- | to rest quietly, quiet, peaceful | 638'; 'k\\\"ek-, k\\\"ok-, k\\\"ek-s- | to seem, see, show | 638-639'; 'k\\\"el-1, k\\\"ela- | to turn; wheel; neck? | 639-640'; 'k\\\"er-1 | to do | 641-642'; 'k\\\"etuer-, k\\\"etuor-, k\\\"etur- | four | 642' (line 52976); 'k\\\"rei- | to buy | 648'. Every Pokorny page cited by the ten target root boxes falls inside its lemma's page range, so all eight POK-based redirect targets are real roots correctly located.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kwe, kwei-1, kwek-, kwer-1, kwetwer-, sper-3\", \"stance\": \"supports\", \"note\": \"data/verification/sources/refs/AHD_watkins1985.txt: 'kwe. And (enclitic). Latin -que, and: SESQUI-, UBIQUITY. [Pok. kve 635.]'; 'kwek-. To appear, see, show. Variant form *kveg- ... [Pok. k#ek- 638.]' (Nourai's gloss for Kwek is Watkins' wording verbatim); 'kwer-1. To make. ... Sanskrit karoti ... [Pok. 1. kver- 641.]'; 'kvetwer-. Four. ... Latin quattuor ... [Pok. kvetuer- 642.]'; the kwei-1 entry ends '... to Latin as poena, penalty: PAIN, PENAL, PENALTY, PUNISH ... [Pok. k#ei-t- 636.]', matching Nourai's gloss 'to pay back, revenge, punish'. Watkins also writes 'sper-3. Bird's name, sparrow. Suffixed o-grade form *spor-wo- ... OE spearwa: SPARROW. [Pok. sper-(g)- 997.]' - the very page POK:997 that Nourai's Sper box cites, so that citation is correct as printed even though the local POK OCR tags the sper-2(g-) lemma 991.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.vv. ksudros and qusudros (IEC.txt lines 8230, 14377)\", \"stance\": \"supports\", \"note\": \"'ksudros (skudhros) ‘coarse, granular; coarseness, granules, grit’. Cf. also qusudros ... Skt. ksudrah ‘small, fine’; Av. xsudrom “seed”; Per. xurd ‘small’' and 'qusudros ‘worn, granular’. Cf. ksudh- ... WP I, 502 ... Skt. ksudrah, adj. ‘crushed; small; humble; mean’; Av. xsudram; Per. xurd ‘minute, tiny’'. Mann himself cross-refers the two spellings exactly as Nourai's stub Qusudros -> Ksudros does, and Nourai's gloss 'coarse, granular, crushed in small pieces' is Mann's wording. Mann's IEC text on disk carries no page tags, so the exact page numbers IEC:576,1060 could not be confirmed, only the content.\"}\n  ],\n  \"entries\": []\n}\nJSONEOF\npython3 -m json.tool data/verification/page-413.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 413"
}
```


### [2026-09-14T01:12:39.912Z] TOOL RESULT

```
JSON OK
nodes verified: 0/0
node verdicts: {}
root verdicts: {}
ref checks: {}
books consulted: {} | by book: {}
```


## [2026-09-14T01:12:54.184Z] AGENT

Done. `verify_check.py 413` reports 0 PROBLEM lines.

**Page 413 (book p. 383) — summary**

- Verdict counts: 0 roots, 0 nodes verified — **the page has no charts at all**. All 11 entries are `see root:` cross-reference stubs, which the instructions say to skip, so `data/verification/page-413.json` carries `"entries": []` plus a documented `note` / `note_fa` / `consulted` (the same shape as the existing all-redirect pages 146 and 163).
- disputed: none. transcription_suspect: none.
- **Extraction errors: none.** The printed page (`site/pages/413.jpg`, header "Quseros | Qwri") shows exactly eleven headword boxes and eleven targets, and `data/extracted/batch/page-413.json` reproduces all of them correctly, including the breve in `Qusěros` and the disambiguating numeral in `Kwei 1` (targeted twice, by `Qwei` and `Qwi`).
- All 10 distinct targets resolve to real root boxes elsewhere in the book, and each target box lists the Q-spelling among its own variant names: Sper (pdf 467), Ksudros (282), Kwe (288), Kwei 1 (289), Kwek (290), Kwel (290–291), Kwer (292–293), Kwetwer (295), Kweye (296), Kwri (299).
- Cross-checked the targets in Pokorny (`POK_full.txt`) and Watkins 1985: all eight POK-cited targets are genuine PIE roots on the cited pages (*kʷe 635, *kʷei- 636–637, *kʷeyə- 638, *kʷeḱ- 638–639, *kʷel- 639–640, *kʷer- 641–642, *kʷetwer- 642, *kʷrei- 648). Ksudros has no Pokorny lemma; Mann's IEC has both `ksudros` and `qusudros` cross-referring to each other exactly as Nourai's redirect does.
- Note for whoever verifies page 467: Nourai's `POK:997` for Sper "sparrow" is correct as printed — Watkins cites the same "[Pok. sper-(g)- 997]" — even though the local POK OCR tags that lemma's page as 991.
- The whole page is just Nourai's transliteration convention: he writes PIE *kʷ as both `Kw-` and `Qw-/Qu-` (Q = the older Brugmann/Pokorny qʷ), so book page 383 is a pointer table from the Q- spellings back to the Kw- spellings where the charts stand.
