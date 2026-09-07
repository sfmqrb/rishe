# Verification process log — verify-page-360


## [2026-09-07T19:29:01.573Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 360 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-360.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-360.json. Write /home/sfmqrb/git/rishe/data/verification/page-360.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 360` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T19:29:03.759Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T19:29:04.465Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T19:29:04.478Z] TOOL RESULT

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


## [2026-09-07T19:29:05.453Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-360.txt"
}
```


### [2026-09-07T19:29:05.475Z] TOOL RESULT

```
1	=== PDF page 360 (book page 330) ===
2	--- entry 0 ---
3	ROOT Nembh -> redirect to Nebh
4	--- entry 1 ---
5	ROOT Nena -> redirect to Nana
6	--- entry 2 ---
7	ROOT [Indo-European] Nepôt, Neptis : grandson; grand daughter  (refs POK:764; IEC:836)
8	#1 (parent #0) [Avestan / Old Persian] refs=KLN:1039; POK:764; KNT:193; MFL:102; IEC:836 | napât, napâ : grandson ; naptis : grand daughter
9	  #2 (parent #1) [Pahlavi] refs=PHD:57 | nab : grandchild
10	    #3 (parent #2) [Persian] refs=BQT:2117,2208; HRN:234; IEC:836; MON | naveh «نوه» : grandchild ; nabas «نَبَس ( نَبَسه )» : daughter's child | extra: نواده ، نبیره ، نواسه ، نواشه
11	#4 (parent #0) [Latin] refs=KLN:1039; POK:764 | nepôs : grandson
12	  #5 (parent #4) [Old French] refs=AHD | neveu : nephew
13	    #6 (parent #5) [English] refs=None | nephew, niece
14	--- entry 3 ---
15	ROOT Neptis -> redirect to Nepôt
16	
```


## [2026-09-07T19:29:05.502Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-360.json"
}
```


### [2026-09-07T19:29:05.541Z] TOOL RESULT

```
1	{
2	  "pdf_page": 360,
3	  "book_page": 330,
4	  "entries": [
5	    { "root": { "name": "Nembh", "redirect": "Nebh" }, "nodes": [] },
6	    { "root": { "name": "Nena", "redirect": "Nana" }, "nodes": [] },
7	    {
8	      "root": {
9	        "name": "Nepôt, Neptis",
10	        "lang": "Indo-European",
11	        "refs": "POK:764; IEC:836",
12	        "gloss": "grandson; grand daughter"
13	      },
14	      "nodes": [
15	        {
16	          "id": 1,
17	          "parent": 0,
18	          "lang": "Avestan / Old Persian",
19	          "refs": "KLN:1039; POK:764; KNT:193; MFL:102; IEC:836",
20	          "words": [
21	            {"translit": "napât, napâ", "gloss": "grandson", "script": null},
22	            {"translit": "naptis", "gloss": "grand daughter", "script": null}
23	          ],
24	          "script_extra": null,
25	          "note": null,
26	          "quote": null
27	        },
28	        {
29	          "id": 2,
30	          "parent": 1,
31	          "lang": "Pahlavi",
32	          "refs": "PHD:57",
33	          "words": [
34	            {"translit": "nab", "gloss": "grandchild", "script": null}
35	          ],
36	          "script_extra": null,
37	          "note": null,
38	          "quote": null
39	        },
40	        {
41	          "id": 3,
42	          "parent": 2,
43	          "lang": "Persian",
44	          "refs": "BQT:2117,2208; HRN:234; IEC:836; MON",
45	          "words": [
46	            {"translit": "naveh", "gloss": "grandchild", "script": "نوه"},
47	            {"translit": "nabas", "gloss": "daughter's child", "script": "نَبَس ( نَبَسه )"}
48	          ],
49	          "script_extra": "نواده ، نبیره ، نواسه ، نواشه",
50	          "note": null,
51	          "quote": {"text": "صفت ذات او همین نه بس است - که رسول خدای را نبس است", "poet": "Amîr Khosrow"}
52	        },
53	        {
54	          "id": 4,
55	          "parent": 0,
56	          "lang": "Latin",
57	          "refs": "KLN:1039; POK:764",
58	          "words": [
59	            {"translit": "nepôs", "gloss": "grandson", "script": null}
60	          ],
61	          "script_extra": null,
62	          "note": null,
63	          "quote": null
64	        },
65	        {
66	          "id": 5,
67	          "parent": 4,
68	          "lang": "Old French",
69	          "refs": "AHD",
70	          "words": [
71	            {"translit": "neveu", "gloss": "nephew", "script": null}
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
83	            {"translit": "nephew, niece", "gloss": null, "script": null}
84	          ],
85	          "script_extra": null,
86	          "note": null,
87	          "quote": null
88	        }
89	      ]
90	    },
91	    { "root": { "name": "Neptis", "redirect": "Nepôt" }, "nodes": [] }
92	  ]
93	}
94	
```


## [2026-09-07T19:29:12.471Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','IEC','KLN','KNT','MFL','PHD','BQT','HRN','MON','AHD','WLD','SYN','HUB','NYB','SKT','WEB','FSD','BRT']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400])\n    print()\n\"",
 "description": "Inspect refs_online.json entries"
}
```


## [2026-09-07T19:29:12.498Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && ls refs/ | head -80"
}
```


### [2026-09-07T19:29:13.699Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca

MFL {"title": "I. M. Oranskij, Introduction to Iranian Philology (Persian translation by K. Keshavarz, Tehran 1979)", "edition_found": null, "kind": "archive_fragment", "url": "https://archive.org/details/galaxy_ub2007_yahoo_201511 (5-page image fragment of the Keshavarz translation only)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MFL/MFL_ia_ga

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
```


### [2026-09-07T19:29:13.746Z] TOOL RESULT

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
```


## [2026-09-07T19:29:19.126Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','IEC','KLN','KNT','MFL','PHD','HRN','WLD','SYN','HUB','NYB','SKT','BRT','ARY','MON','BQT','AHD','WEB','FSD']:\n    v=d.get(k) or {}\n    print('==',k, '| local:', v.get('local_file'), '| offset:', v.get('page_offset'), '| hint:', (v.get('lookup_hint') or '')[:200])\n\""
}
```


### [2026-09-07T19:29:20.383Z] TOOL RESULT

```
== POK | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.i
== IEC | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== KLN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume p
== KNT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall i
== MFL | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MFL/MFL_ia_galaxy_ub2007.pdf'] | offset: None | hint: Persian translation not found on IA; the Russian original (Vvedenie v iranskuju filologiju, 1960/1988) and French translation (Les langues iraniennes, 1977) exist but with different pagination.
== PHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A
== HRN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered ent
== WLD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, u
== SYN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed p
== HUB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== NYB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== SKT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== BRT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin glos
== ARY | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | offset: printed page = pdf page + 1 | hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword
== MON | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Aves
== BQT | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'http
== AHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the 
== WEB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | offset: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabe
== FSD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
```


## [2026-09-07T19:29:25.419Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'nepot\\|nepōt\\|nepōts\\|napāt' POK_03.txt | head -30; echo \"=== POK_full\"; grep -n -i 'nepot' POK_full.txt | head -20"
}
```


### [2026-09-07T19:29:25.513Z] TOOL RESULT

```
=== POK_full
62600:Root / lemma: nepot- {*he- nemot^ 
62609:grandson ', later also ' nephew '; Old Lithuanian nepotis, /7e/0^c//s "grandchild, grandson';
```


## [2026-09-07T19:29:26.098Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC\"; grep -n -i 'nepot\\|napat' IEC.txt | head -20; echo \"=== KNT\"; grep -n -i 'napat\\|napā' KNT.txt | head -20"
}
```


### [2026-09-07T19:29:26.170Z] TOOL RESULT

```
=== IEC
11643:nepóts (nepots) ‘nephew, grandson’. Cf. ne- pis, ön. WP II, 329 Skt. nápat ‘grandson, descendant; Av. napo, obl: napàt- ‘grandson’; Ober napa, obl: na- påt-, id.; Per. navade, id. beside nave, navàse, id., of various dial. origin; Archaic Hom. né- podes, pl. ‘children’ beside Gk. a-nepsiós, m. (nephew; cousin’, of adjectival type fr. *sm- neptio-; Lat. nepos, gs: -potis ‘grandson’; MHG nift, m. id.; Slovene cf. nec-ak, “sisters son’; OLI. nepuotis ‘nephew, grandson’; LW in Finn. nepas, nepaa
=== KNT
2192:It is to be noted that in Aryan, when a word ended in two or more consonants, the final con- sonant or consonants fell off until only one was left; thus pIE nom. *nepót-s ‘grandson’, Lt. nepos, became pAr. *napat, Skt. nápát.
5593:napüt- sb. ‘grandson’: Av. Skt. napat-, Lt.’
```


## [2026-09-07T19:29:32.243Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport sys\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index of line 11643\npos=sum(len(l)+1 for l in lines[:11642])\nleaf=t[:pos].count('\\f')\nprint('leaf',leaf)\npages=t.split('\\f')\nprint(pages[leaf][:2500])\n\""
}
```


## [2026-09-07T19:29:33.070Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npos=sum(len(l)+1 for l in lines[:5592])\nleaf=t[:pos].count('\\f')\nprint('leaf',leaf)\npages=t.split('\\f')\nprint(pages[leaf][:1800])\n\""
}
```


### [2026-09-07T19:29:33.618Z] TOOL RESULT

```
leaf 467
má, prp. & adv. “except; unless; W cf. nam, named, id. (for *nomet? with the re- duced vocalism of Lat. nam in relation to enim, for *et-nem in view ofthe hapax ennam? Speculations in WH:LEW & EM:DELL); ON nema, cj. ‘except; unless; but that; per- haps; say; but Br. némét, id.
nemet- *partition; part, lot. Cf. nemos (1) Gk. némesis, f. ‘indignation; grudge; remorse; goddess of retribution'; Gaul. neméton, nimi- da, n. & f. ‘sacred grove’; OS nimid ‘copse, thicket
nemo ‘turn, bend, bow’; nemos ‘curve, arch, heaven’ Skt. námāmi, v. id.: Av. nam-, v. intr. id.; Tokh. AB nåm-, B nem-, tr. id.; OIr. nem, n. ‘heaven’; Ir. neamb, pl. neimh, m. & f. id.; W nef, pl. nefoedd, f. id.; Br. énv, pl. -u, m. id.; Skt. námas, n. ‘bend, bow
nemos (1) “holding, taking, share’. WP II, 330 Gk. némos, gs: -eos, n. “clearing, pasture, grove'; Lat. nemus, gs: -oris, n. id.; cf. Gaul. nemeto- & variant nimida ‘sacred grove’; OS nimid, s. ‘copse, thicket. (Isophone: Ir. neimb, gs: neimhe, f. ‘poison’, unless = *share'?); Go. niman, sv. 4 (and com. Gmc. *take")
nemos, ios (2) “soft, moist’. See emnos, ios Av. námyo, id.; Per. nam, id.; Alb. i njomé, id.; cf. njom, v. ‘moisten’
neniio (?) 'skirl, wail Phryg. cf. neníaton ‘pipe-tune’; cf. (alleged) Gk. nēnía as LW in Lat. nenía ‘dreary sing- song’; LLat. ‘harangue’; It. ‘dirge, lullaby’
nepis, nepó(n) ‘nephew; grandson’. See next. WP II, 329 Per. nava ‘grandson’; Olr. nia ‘nephew’; OW nei, pl: nyeint, mod. nai, pl: neiaint ‘nephew’; Cor. noy, id.; MHG nëf, nëve ‘sisters son’; G Neffe, wm. (nephew; dial. ‘grandson’); OFris. neva, wm. ‘nephew’; OE nefa, wm. ‘nephew; grandson; stepson’; nefene, f. ‘niece, granddaughter’; Du. neef, m. ‘nephew,
nemi — nëqu- (noqu-)
20
25
30
35
40
45
 
836
cousin’; ON nefi, m. ‘nephew’. (Eng. nephew is a hybrid of OE nefa and OFr. neveu 'ne- phew, grandson’. Alb. nip *grandson' is fr. Lat. nepos. The Alb. form also = ‘nephew’, usu. nipóll, id.)
nepóts (nepots) ‘nephew, grandson’. Cf. ne- pis, ön. WP II, 329 Skt. nápat ‘grandson, descendant; Av. napo, obl: napàt- ‘grandson’; Ober napa, obl: na- påt-, id.; Per. navade, id. beside nave, navàse, id., of various dial. origin; Archaic Hom. né- podes, pl. ‘children’ beside Gk. a-nepsiós, m. (nephew; cousin’, of adjectival type fr. *sm- neptio-; Lat. nepos, gs: -potis ‘grandson’; MHG nift, m. id.; Slovene cf. nec-ak, “sisters son’; OLI. nepuotis ‘nephew, grandson’; LW in Finn. nepas, nepaa
nepteris (neptris) ‘niece, granddaughter’. Cf. WP II, 329 and nepis, nepóts
```


### [2026-09-07T19:29:34.789Z] TOOL RESULT

```
leaf 216
e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27) XPh 23.
naiy adv. ‘not’: Av. 207, РЫ. në, Skt. ned; :
from pIE *ne, Skt. na, Lt. ne-scio ‘I don't know’, -+ Эа, asn. of pron. i-, Lt. id, OP id-am, ete. (869, 884, $191.1, $291.11, §292a). DB 1.32, 48, 49 ter, 52, 53, 71, 91°; 221, 24, 31, 51, 84; 3.15, 86; 4.44, 47 bis, 51, 55, 58, 63 bis, 63f, 64°, 65 bis; 5.16°, 31; DPd 11; DNb 7f, 12, 13, 21, 23, 36, 40; DSe 36, 40 bis, 43°; DS} 3; XV 22. nai-maiy (836) DB 4.64. nai-ma DNb 8, 10, 19. nai- pati-mà (8133) ОМ 20. nai-&im DB 4.49. naty- diš ($136) DB 4.73, 78.
naiba- adj. ‘beautiful, (religiously) good’, re- .
placing GAv. vahu- ‘good’, and opposite of duš- karta- (Hz. AMI 8.68, ApI 266-7): NPers. nē ‘brave, good’ ($11, §75.V, $148.11). пафа nsf. DPd 8. naibam nsn. XPa 13, 16; XPg 4; XV 20. naibam asn. DSe 32°; DSi 4^; DSp 2f°; XPh 43.
naucaina- adj. ‘of cedar’: NPers. nóZ, пдѓап ‘pine cone’; therefore naucaina- ‘pine-cone-shaped’ ($147.11), appropriate to the cedar (König, Burg- bau 53-4; Hz. AMI 3.58). naucaina nsm. DSf 30f. |
nab- vb. ‘perish’, causative (8123.2, $215) "in- jure; destroy’: Aw. )nas-) ӨЮ. naé-, Gk. vexus
7 ыйсы аЙ eet NUI ШЕЛ, АМАА а аз an ШО. Дені. Zr é
DD де 5... anes
LEXICON
‘corpse’, Lt. acc. nec-em ‘destruction’, nocet ‘harms’, pIE *nek- (887).
vi- + nab- caus. ‘injure, harm’: vindPayatiy (8215) DNb 17f. viyanatlaya imf. (§122, $1232, $215) DB 4.66. vinátayá"tiy За pl. subj. (8222.1I, §232.1) A’Sa 5°, A?Ha 7° (conj. Kent). vinátayais opt. ($215, $223.II, $228.11) DNb 20, 21. vi- nastahyd gsn. past pte. pass. as sb. ($03, $122, $242.11) DNb 18.
Nadi"labaira- sb. ‘Nidintu-Bel, a Baby- lonian rebel: Elam. nu-ti-ut-be-ul, Akk. ni-din-ti- йе] (§75.V, §76.V, $107). Naditabaira пзш.
```


## [2026-09-07T19:29:43.434Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'napüt-' in p or 'napat-' in p and 'grandson' in p:\n        print('--- leaf',i)\n        print(p[:3000])\n\""
}
```


### [2026-09-07T19:29:44.644Z] TOOL RESULT

```
--- leaf 216
e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27) XPh 23.
naiy adv. ‘not’: Av. 207, РЫ. në, Skt. ned; :
from pIE *ne, Skt. na, Lt. ne-scio ‘I don't know’, -+ Эа, asn. of pron. i-, Lt. id, OP id-am, ete. (869, 884, $191.1, $291.11, §292a). DB 1.32, 48, 49 ter, 52, 53, 71, 91°; 221, 24, 31, 51, 84; 3.15, 86; 4.44, 47 bis, 51, 55, 58, 63 bis, 63f, 64°, 65 bis; 5.16°, 31; DPd 11; DNb 7f, 12, 13, 21, 23, 36, 40; DSe 36, 40 bis, 43°; DS} 3; XV 22. nai-maiy (836) DB 4.64. nai-ma DNb 8, 10, 19. nai- pati-mà (8133) ОМ 20. nai-&im DB 4.49. naty- diš ($136) DB 4.73, 78.
naiba- adj. ‘beautiful, (religiously) good’, re- .
placing GAv. vahu- ‘good’, and opposite of duš- karta- (Hz. AMI 8.68, ApI 266-7): NPers. nē ‘brave, good’ ($11, §75.V, $148.11). пафа nsf. DPd 8. naibam nsn. XPa 13, 16; XPg 4; XV 20. naibam asn. DSe 32°; DSi 4^; DSp 2f°; XPh 43.
naucaina- adj. ‘of cedar’: NPers. nóZ, пдѓап ‘pine cone’; therefore naucaina- ‘pine-cone-shaped’ ($147.11), appropriate to the cedar (König, Burg- bau 53-4; Hz. AMI 3.58). naucaina nsm. DSf 30f. |
nab- vb. ‘perish’, causative (8123.2, $215) "in- jure; destroy’: Aw. )nas-) ӨЮ. naé-, Gk. vexus
7 ыйсы аЙ eet NUI ШЕЛ, АМАА а аз an ШО. Дені. Zr é
DD де 5... anes
LEXICON
‘corpse’, Lt. acc. nec-em ‘destruction’, nocet ‘harms’, pIE *nek- (887).
vi- + nab- caus. ‘injure, harm’: vindPayatiy (8215) DNb 17f. viyanatlaya imf. (§122, $1232, $215) DB 4.66. vinátayá"tiy За pl. subj. (8222.1I, §232.1) A’Sa 5°, A?Ha 7° (conj. Kent). vinátayais opt. ($215, $223.II, $228.11) DNb 20, 21. vi- nastahyd gsn. past pte. pass. as sb. ($03, $122, $242.11) DNb 18.
Nadi"labaira- sb. ‘Nidintu-Bel, a Baby- lonian rebel: Elam. nu-ti-ut-be-ul, Akk. ni-din-ti- йе] (§75.V, §76.V, $107). Naditabaira пзш. DB 1.77, 92f; 2.1; 4.12; DBd 1. Naditabairam asm. DB 1.80, 84; 24, 5. Naditabairahyà gsm. DB 1.85, 89, 95.
napüt- sb. ‘grandson’: Av. Skt. napat-, Lt.’
nepos, pIE *nepot- (875.1, §110, $142). napa nsm. (§124.5, §188.1) AmH 4; DB 1.3; DBa 4; А:Ра 16°.
Nabukudracara- sb. ‘Nebuchadrezzar’, son of Nabonidus; name assumed by the rebels Nidintu- Bel and Arkha: Elam. nab-ku-tur-ra-sir, Akk. nabu-kudurri-ugur (82, 833, §75.V, $128, §163.- VD. Nabukudracara nsm. DB 3.80f, 89; 4.14, 29f; DBd 3f; written Nabukuracara ($52.V) DBi 5f. Nabuk*dracara (822) DB 1.78f, 84, 93.
Nabunaita- sb. ‘Nabonidus’, last king of the New Babylonian Empire, 556-39. в.с: Elam. na- bu-ni-da, Akk. nabü-na'id; Gk. Aaßivnros (Hat. 1.74, ete.). Nabunailahyà gsm. DB 1.79. Na- bunaitahya (§36.1Vb) DB 3.81; 4.14, 30; DBd 5f; DBi 7f.
niman- sb. ‘name’: Ау. náman-, NPers. пат, Skt. náman-, Lt. nomen, pIE *nómen-, cf. Gk. буора, NEng. name ($109, $110, 5155.11). See also Andmaka-. náma^, suffixless lsn. used with mase. and nt. generic nouns to denote specification ($112, $187, §251C, §312): DB 1.28, 30, 36, 37, 74, 77, 92; 2.8f, 9, 14°, 19, 22, 29, 38, 49, 65, 79, 82, 95; 3.5, 12, 13, 22 bis, 31, 34, 44, 51, 56, 78, 84; 4.8,
```


## [2026-09-07T19:29:53.739Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(205,222):\n    nums=re.findall(r'(?m)^\\s*(1[6-9][0-9]|2[0-2][0-9])\\s*$', pages[i])\n    head=[l for l in pages[i].split('\\n') if 'LEXICON' in l or re.match(r'^\\s*\\d{3}\\s*$', l)]\n    print(i, nums, head[:4])\n\""
}
```


### [2026-09-07T19:29:55.017Z] TOOL RESULT

```
205 [] ['LEXICON']
206 ['183'] ['183']
207 [] ['LEXICON']
208 ['185', '186'] ['185', '186']
209 [] ['LEXICON']
210 ['187'] ['187']
211 ['188'] ['188']
212 ['189'] ['LEXICON', '189']
213 [] []
214 ['191'] ['LEXICON', '191']
215 [] []
216 ['193'] ['LEXICON', '193']
217 [] []
218 [] ['LEXICON 195']
219 [] []
220 [] ['LEXICON']
221 ['197', '198'] ['197', '198']
```


## [2026-09-07T19:30:00.301Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '62590,62650p' POK_full.txt"
}
```


### [2026-09-07T19:30:00.349Z] TOOL RESULT

```
grove ', PN Nemeto-briga, VN Nemetes, Old Irish nemed' shrine ', then "privilege, privileged 
person'; asachs. nimidas' sacra silvarum '; Lithuanian FIN Nemunas' Neman, Niemen, a river 
of western Belarus ' (= ' marshy stream'), nemuoge' blueberry '; gall. nanfo\a\\ey', tr/nanto' 
three valleys ', VN Nantuates, cymr. nant'vaWey, stream, brook' {*nm-tu-, compare 
participle Old Indie nata-irom nmto-); savoy. /7a 'stream, brook'; perhaps here Old Irish 
nem'sky, heaven'; different above S. 315. 

References: WP. II 331 f., WH. II 158 f., E. Frankel REIE. 1, 405 ff. 
Page(s): 764 

Root / lemma: nepot- {*he- nemot^ 
Meaning: uncle; nephew, *descendant 
Grammatical information: fem. nepff- 

Material: Old Indie /74o^/ (secondary naptr-) " grandson, descendant ', Avestan napat-, 
naptar-, ap. napat- (is.. Old Indie apam napat, Avestan apqm napa-u. name of a divinity (" 
primeval offspring of the waters '); hom. vsnoSsq (5r|or|) " young ones, children ' from a N. 
Sg. *V£TTU)T(;; perhaps here lemnisch-tyrsenisch vacpoG "offspring, descendant, son' 
(Kretschmer, Glotta 28, 266); alb. nip' grandson, nephew '; Latin nepos, -tis^ grandchild, 
grandson ', later also ' nephew '; Old Lithuanian nepotis, /7e/0^c//s "grandchild, grandson'; 
Old High German nevo' nephew, kinsman, relative'. Old English /7e/& 'grandchild, 
grandson, nephew ', Old Icelandic nefe' nephew, kinsman, relative' {*nepdts); Middle Irish 
n'i'ae. Gen. n'lath' sister's son ' (for the form in the end Pokorny ZfceltPh. 10, 405 f.), cymr. 
nei, nai6s., corn. /7c»/"grandchild, grandson'. Middle Breton /7/" nephew '. 

Fem. Old Indie /7a,c^- "granddaughter, female descendant ', Avestan naptT- 
"granddaughter'; 

Latin nept/s {ior -///Sy) after the Astem) 'granddaughter', later 'niece'; Old Irish necht, 
cymr. abret. n/th. Middle Breton n/z, corn. /70///7 'niece'; (common alb. Celtic -f-, -ph- > -ch-, 



Old High German n/ft'r\ept\s, privigna'. Modern High German (actually Low German) 
Nichte, Old Norse nipt' sister's daughter, niece'; Old Lithuanian /7e'yO/e 'granddaughter'; 
russ. -Church Slavic nestera 'n\ece' {*nept-tera). (common Slavic -pt- > -st-) 

further formations 'i^e/T/irb-/ Avestan naptya-' offspring, descendant '; alb. {^harness!) 
mbese 'n\ece' from *nepdtia; 



\\b. Geg mesa, Tosc mt>esa'n\ece (sister's daughter)' derived from Hittite Luwial 
a descendant); Luwian /7A7sa "grandson' : Hittite hamsa- hassa{a grandson) : Latvian 
nasas-me/ta^ niece (sister's daugliter)' = Latvian /77asa"sistei^^l^^7o£g^7o^^^sisten 
i me/ta 'daughter'; alb, has lost the AnatQiian old larygeaj 



gr. a-v£4Ji6(; " brother's or sister's son ' ( *sm-nept//os)] russ. -Church Slavic net/jb ' nephew 
'. (Greek Occidental Romance vowel prefix) 

Probably as " the under-age, dependent ' to ne- and pot/s. 

References: WP. II 329 f., WH. II 161 f., Trautmann 196. 
Page(s): 764 

Root / lemma: ner-1(t)-, aner- {aner-1) {*he- ner-1(t)-) 

Meaning: vital energy; man
```


## [2026-09-07T19:30:00.985Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i in range(0,6):\n    print('--- leaf',i); print(pages[i][:1500])\n\""
}
```


### [2026-09-07T19:30:02.279Z] TOOL RESULT

```
430
--- leaf 0

--- leaf 1

--- leaf 2
i

--- leaf 3

--- leaf 4
3>\
f-^^^'i
N.
adhos,  ndheri  ,unter',  ndhero-  ^der  untere'^,  ndheino-  ^der  untersteh
Ai.  adhdh  ,unten^  (als  Präp.  m.  Akk.  u.  Gen,),  av.  add  ,mnten^,  arm. ^nd  (m.  Instr.)  ^unter'^  ^m\.  und  ds.,  toch.  A  afic  ,unten,  nach  unten^(?);
ar.  adairi  ^unter,  unterhalb^,  got.  undar  usw.,  ahd.  untar  und  untari ,unter^,  Neubildung"  nach  idg-.  *uper{  (ai.  upari  usw.  ,über^);
ai.  ddhara-,  av.  adara-  ,der  untere^,  lat.  Inferus  ds.  (*enferos,  idg*.  *ndheros)^ infernus  ds.  (nach  supernus),  infrä  ,unterhalb^  {^inferäd)  mit  Anlauts- behandlung des  -dh-]  gr.  äd^sgo-  steckt  vielleicht  in  d-^sgl^o)  , verachte' (vgl.  ai.  adharlna-  _,verachtet') ;  got.  undaro  Präp.  , unter'  (Abi.  auf  -öd) =  ai.  Adv.  ädharät  , unten';
ai.  adhamd-  ,der  unterste'  =  lat.  mfimus  ds.
WP.  I  323,  WH.  I  698,  Specht  Idg.  Dekl.  259 1.
nsi-  ,schmutzfarbig;  Schmutz,  Schlamm'.
Ai.  dsi-ta-,  fem.  dsi-knl  ,dunkelfarbig,  schwarz';  gr.  Uaig  , Schlamm (eines  Flusses)',  äaiog  ,schlamraig'.
WP.  I  324,  W.  Schulze  Kl.  Sehr.  116  f.
nsi-s  ,Schwert';  nur  arisch  und  italisch.
Ai.  asi-  m.  ,Schwert,  Schlachtmesser';  av.  ardhü-i.  ds.;  lat.  ensis  .Schwert'.
WP.  I  324,  WH.  II  406,  Specht  KZ.  66,  
--- leaf 5
34  f.
49*
m
0/
1.  o  ,zu,  mitS  s.  S.  280 f.;  dazu  thrak.  VN  "0-ÖQvaai  ,Waldanwohner'.
2.  5  Ausruf  (s.  auch  e  S.  281).
Ai.  ä  (z.  T.  auch  aus  idg.  ä,  s.  d.).
Gr.  (b,  ä  Ausruf  bes.  des  Erstaunens,  Vokativpartikel  (davon  öjI^slv  ,oh; rufen*,  d)'^  ,heda!S  vgl.  auch  wörtj  ort  ,ermunternder  Zuruf  der  RudererM nach  Kretschmer  KZ.  38,  135  auch  in  gr.  d)-Qvoiiai  ,heulen,  brüllen*).
Lat.  ö  Ausruf  verschiedenster  Stimmung.
Ir.  ä,  a  =  cymr.  corn.  bret.  a  Vokativpartikel.
Got.  ö  (dreimal  ,t5S  einmal  =  ,o^a,  pfui!'),  mhd.  ö  bes.  beim  Vokativ, und  (heute  oh  geschrieben)  Ausruf  der  Verwunderung,  Rührung,  Klage (s.  auch  Weigand-Hirt ;  germ.  ö  mag  z.  T.  auch  lautliche  Entwicklung  aus idg.  ä  sein,  s.  d.).
Lit.  0  jAusruf  des  Tadels,  der  Verwunderung,  Vokativpartikel';  lett.  a ,Vokativpartikel'.
Aksl.  0  ,(^'  (Neuschöpfung).
WP.  I  165,  WH.  II  192.
obhel-  , fegen'  und  ^vermehren^;  nur  arm.  und  griech.
Arm.  avelum  ,ich  fege'  {af-avelum  ,ich  vermehre'  :  aveli  ,mehr'),  gr. dcpiXlb)  ,fege'  und  , vermehre',  ocpeliia  , Besen'  und  , Vorteil',  ocpeXiqov , Besen'  Hes.,  dcpeXxQsvoj  ,fege' ;  ocpsXog  ^Nutzen',  (bcpslico  ^nütze^
WP.  I  178,  Schwyzer  Gr.  Gr.  1,  57,  Leumann  Hom.  Wörter  120 ff.
obhi  s.  oben  S.  287.
I.  od-  ,riechen';  od-mä  ^Geruch^
Arm.   hot  ,Duft,  Geruch'   (sek.  o-St.),   hotim  , rieche',    hototim   ,wittere';
gr.  o%ü)  ,
```


## [2026-09-07T19:30:10.883Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('npages',len(pages))\nfor i in (418,419,420,421,422):\n    p=pages[i] if i<len(pages) else ''\n    print('--- leaf',i, repr(p[:200]))\n\""
}
```


### [2026-09-07T19:30:12.197Z] TOOL RESULT

```
npages 434
--- leaf 418 'g  ist  durch  sekundäre  Nasalierung  entstanden.\nWP.  II  316,  Trautmann  201  f.;  Loth  RC  45,   199 ff.\nI.  xze,  ne,  nei  Satznegation  der  reinen  Verneinung  (ne  einzelsprachlich  auch   '
--- leaf 419 "nicht',  nekas,  nekurls  (s.  oben);  aksl.  ne  ,nicht';\nhitt.   natta  ,nicht*,  näwi  ,noch  nicht'.\nne:  ai.  (ved.)  na  ,nicht';  lat.  ne  , nicht'  in  ne-quidem,  nequäquam,  nsqm- quam,  ne"
--- leaf 420 " as.  w«,  anord.  oss  ,uns' (*ns),   aksl.  nas^  Gen.  (j^nös-söm),  apr.  nöuson  (ebenso) ;  £■_\nauf  *nsme  (wohl  ns  -j-  Partikel  *sm-,  verwandt  mit  dem  -sm-  der  Pron.- Dekl.,  z.  B. "
--- leaf 421 "- nesseP,  lett.  ndtrCj  nätra  ,Nessel',  slav.  *nat'b  , Krautblätter'  in  slov.  nät (Gen.  nati),  poln.  nac  ds.  und  allenfalls  (als  redupl.  urkelt.  *ni-nati-?) mir.  nenaid,  nir.  nea"
--- leaf 422 "nä-  r\\.  f.  ,Auge', netra-  n.  ds.\nWP.  II  321,  336,  WH.  II  168,  171,  Vendryes  RC.  46,  265  ff.\n3.  nei-,  ni-  s.  oben  S.  312  f.\nI.  neid-  ,heruntermachen,  schmähen'.\nAi.  nindati,"
```


## [2026-09-07T19:30:16.681Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'nepos' in p or 'Enkel,  Neffe' in p or 'napat' in p:\n        print('--- leaf',i); print(p[:2600]); print()\n\" | head -80"
}
```


### [2026-09-07T19:30:17.948Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T19:30:20.886Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f\"; grep -n -i 'nepot\\|Enkel' $f | head -15; done"
}
```


### [2026-09-07T19:30:22.468Z] TOOL RESULT

```
== POK_01.txt
33:WP.  I  50,  WH.  I  3,  E.  Fraenkel  KZ.  63,  172  ff.,  Trautmann  2.
509:sind:  altn.  Ali  (*anilo),  ag-s.  Anela,  alid.  Änelo  Personennamen;  mlid. '^  7  Qi-oßvatei';  EnkeF.  Ferner  ahd.  eninchil,  mlid.  enichlln,  nlid.  Enkel /  der  kleine  Ahn*).  Bei  den  Indogermanen  wurde  der  Enkel  als  Abbild oder  Ersatz  des  Großvaters  betrachtet;  vgl.  gr.  ^AvTlnaTQoq.  Gegen  diese von  W.  Schulze  KZ.  40^  409  f.  =  Kl.  Sehr.  67  f.  vertretene  Ansicht  wendet Hermann^  Nachr.  d.  Ges.  d.  Wiss.  zu  Göttingen^  Phil. -bist.  Klasse  1918^ 2l5f..  ei"j?  d^ß  bayr.  enl,  änl,  oster r.  äenl,  änl  usw.  die  Bedeutung  ^Groß- vätercben'  und  ^Enkel*  tragen  und  man  es  hier  mit  der  gleichen  Er- sciieinuu"'  zu  tun  hat  wie  bei  nhd.  -Vetter  (ursprüngl.  ,des  Vaters  Bruder^^ dann  auch  ^des  Bruders  Sohn'^);  die  Anrede  wird  vom  Großvater  an  den Enkel  zurückgegeben.  Diese  ältere  Auffassung  (vgl.  die  Literatur  bei Hermann  aaO.)  ist  beachtenswert.
640:ahd.  ancha,  enka  f.  ^Genick^  und  ^Schenkel^  Knochenrohre^  (*ank{ön-), inord.  ekkja  ^Knöchel,  Ferse^;  Derain.  alid.  anchal,  enchil  (umgedeutet (inkldo  m.;  anchala,  enchila  i.,  mhd.  mnd.  enkely  afries.  onkel,  onkleu^  iihd. Enkel,  ag-s.  (umgedeutet)  andeoic,  engl,  ankle,  anord.  okkla  {*ankulan-) .Knöchel  am  Fuß^;  auch  lat.  angidus  (womit  aksL  gg(7>)h  _,WinkeP  ur- verwandt ist)  , Winkel'   (daneben   mit   o-Stufe  lat.  tingulus,  ungnstus  s.  o.).
650:ansä,  ansi-  ^Schlinge^  Schleife^^  z.  T.  als  HandliaLe  von  Gefäßen   (Henkel^ oder  als  dem  Zugvieh  umgeleg'ter  Zügel. Lat.  änsa  ^Griff^  Henkel^  Handhabe^;  ansäe  crepidae  ,die  Ösen  am  Rand^ der  Schuhsohlen,    durch   welche   die   Bindriemen   gezogen   wurden^  =  litj qsä  f.  (Akk.  äsq)  ^Topfhenkel;  Schleife   heim   Knotenschürzen'^   (vgl.  auch] lat.  ansätus  ==  lit.  qsötas  ^gehenkelt^),   lett.  nosa  ^Henkel,   Schleife^,    Öse' woneben   2-St.    apr.  ansis   ^Kesselhaken^    lett.    üoss    (Akk.  iiosi)    , Henkel aisl.  ces  L  {^ansjo)  ^Loch  am  oberen  Kande   des  Schuhleders  zum  Durch.] ziehen  der  Riemen'  =  mnd.  Öse  f.  »ringförmige  Handhabe^  Schlinge'  (dar- aus spätmhd.  nhd.   Ose;   oder   das  wgerm.  Wort  zu  Ohr  nach   Kluge  und? Weigand-Hirt  s.  v.?);  mir.  e(i)si  PL  ^Zügel'.  gr.  fjv'ia,  dor.  ävia  ds.  {*ävGia)\ WP.  T  m,  WH.  I  51,  Trautmann  10.
1182:Daneben    Formen    mit   wohl   erst   einzelsprachlichem  Labial:   gr.  LTtvög,^ älter   Irrvög  ,Ofen'   (nach   Fick   III^  29   zw.,    Ostir  WuS.  5,  217,   Güntert Abi.  25  aus  *Uequ-nös]   nicht  *uqunös^  s.  Boisacq  m.  Lit.),  nach  E.  Fraenkel KZ.  68,202  aus  *vyißv6g  durch  dissimilatorischen  Lautw^andel??  (W.  Schulze  ^ GGA.  1897,  908);    bret.  offen  f.  ,Steintrog'  trotz    Loth  RC.  43,  410  kauml aus  *uppä]    ags.  ofnet  ,kleines  Gefaßt,  o/ew,  ahd.  ovan^  anord.  ofn  ,Ofen^ f (ebenfalls  auf  ^itgqunos  zurückführbar;   das  anlautende  u-  bewirkte  wie  in wulfa-  ,WolF   die   Entwicklung  von  -\v-  zu   -/-,  während   got.  usw.  auhns auf  idg.  '■^uqVf-nös  zurückführt;  der  Verlust  des  lo-  in  Ofen  muß  dann  aller-  ^ dings  aus  Einfluß  dieser  Schwesterform  *uhna-  erklärt  Averden).  Aus  der assimilierten    Form    aschwed.  omn,    mundartl.  umn   ,Ofen^    ist    wohl    apr. wumpnis  ,Backofen^,  umnode  ,Backhaus''  entlehnt.    S.  Meillet  MSL.  9,  137, Meringer  IF.  21,  292ff.,    Senn   Germ.  Lw.-Studien,   Falk-Torp    unter   ovn, Weigand-Hirt  und  Kluge  unter  Ofen.
1824:(fOQog  , Ertrag,  Steuer',   -q)6Qog  , tragend*,   cpoQ&  ,das  Tragen,   reichlicher Ertrag,  Fülle';  äix(p\icp]oQevg  , Gefäß  mit  zwei  Traghenkeln'; (pögrog  ,Bürde,  Ladung,  Last';
2365:WP.  II  193,  WH.  I  541  f.,  866,  Specht  KZ  62.  249.  Fraenkel  REtlE 6  f.,  Risch  Mus.  Helv.  1,118.
2380:germ.  *brök-  , Steiß',  jünger  ,Hose'  in  ags.  brec  PL  , Gesäß',  engl,  breech ds.,  aisl.  bi'ök^  PL  brekr  ,Oberschenkel,  Hose',  ags.  bröc,  ahd.  bruoh,  nhd. Bruch  ds.,  Schweiz,  bruech  , Schamgegend';  geminiert  ags.  usw.  braccas , Hosen';
2813:Urslav.  w-St.  *dhly,  Gen.  *dbhve  (:  air.  delb  aus  *delua)  in  russ.-ksl. delvi  {*dbhvi)  Lok.  Sg.,  N.  PI.  , Faß',  mbuJg.  dhli\*dhly),  Lok.  Sg.  dhhvi ,Faß',   nbulg.  delva   {*dhhva)  ,großer   tönerner  Topf   mit   zwei    Henkeln';
3086:pK  jQvrcüy-Ait.  Drüktems,  apr.  Drutenne  (E.  Fraenkel,  Pauly-Wissowa IG;  1633);
3212:lit.  duomi  (heute  sekundär  duodu,  lett.  duodu,  neugebildet  zum  alit. Ipv.  duodi  aus  "^dö-dhi-,  ostlit.  düomu),  2.  Sg.  düosi,  3.  Sg.  düost{i)  ,^\hi', apr.  däst  ds._,  beruhen  nach  Kofinek  Listy  filol.  65^  445  und  Szemerenyi Et.  Slav.  Roum.  1,  7  ff.  (vgl.  E.  Fraenkel  Balt.  Sprachw.  11  f.)  nicht  auf alter  Reduplikation  (angebl.  *dö-dd-mi,  bsl.  "^dödmi,  3.  Sg.  *dö-dd-ü,  bsl. *dödti  >  *dösti),  sondern  auf  unreduplizierter  athemat.  Flexion  (*dömi, PL  *ddmös);  lit.  düosti,  abg.  dast^  sind  Nachahmungen  von  lit.  hti  ,ißt' usw.,  die  neben  lit.  *e(d)mij  abg.  janib  (aus  ^ed-m-)  liegen^,  wo  das  d  der Wurzel  als  suffixal  empfunden  wurde;  zum  Fut.  lit.  duosiii  s.  oben  S.  223.
3256:WP.  I  816,  E.  Fraenkel  M^  Pedersen  453.
3976:Für  gr.  ^QÖva  PI.  , Blumenverzierungen  in  Gewändern  (bei  den  alexan- drin. Dichtern  für  q)dQ[.i(xy,a,  Zauber-,  Heilkräuter  gebraucht),  bunte  Ge- wänder, bunte  Tiere'  erschließen  Hoff  mann  BB.  15,  86,  Liden  Stud.  67  f. eine  Grundbed.  ,bunt'.  Unter  dieser  Grundbed.  vergleicht  Liden  aaO. alb.  dre-rij  geg,  dr^-ni-  m.  , Hirsch'  (Tiere  aus  dem  Hirsch-  und  Reh- geschlecht sind  häufig  als  ,gesprenkelt,  bunt'  benannt),  wofür  eine  illyr. Gdf.  *drani-  (idg.  dhroni-)  durch  die  wohl  illjr.  Hesychglosse  aqavL^' klaq)OQ  {A-  verschrieben  für  /1-)  geboten  wird.
4832:lit.  ap-,  vor  Labial  auch  noch  api-,  im  Nominalkompos.  apy-  Präf.  ,um,  - herum,  be-',  apie  ,um,  über'  m.  Akk.,  alit.  und  dial.  ostlit.  dievie-p  ,bei Gott'  u.  dgl.,  sünaüs-pi  ,zum  Sohne';  lett.  ap-  ,um,  über',  ple  mit  Gen.  und Akk.  ,bei,  an',  pie-  , hinzu,  an-,  voll-';  apr.  ep-  (ap-  nicht  maßgebendere Schreibung),  eb-  ,be-',  eher  als  *epi  hierher,  als  unter  Zugrundelegung der  Form  eb-  zu  idg.  ebhi,  obJii]  dazu  die  Postposition  lit.  -p{i)  hinter Gen.  namö-pi  ,nach  Hause')  und  Lok.  {namie-pi  ,zu  Hause'),  lett.  -p  (nur adverbial  gebraucht),  E.  Fraenkel,  Syntax  18  ff.,  Endzelin  Gr.  524£f.;
== POK_02.txt
50:isl.  kani  , Henkelgefäß,  Schüssel  (poet.),  norw.  dial.  kane  , Henkelschale', schwed.  dial.  kana  , Schlitten',  dän.  kane  , Schlitten'  (älter  dän.  auch jBoot^),  mnd.  kane  ,Boot'  (woraus  aschwed.  kani  ,Boot'),  ndl.  kaan  ,kleines Boot,  Kahn'  (aus  dem  Ndd.  stammt  auch  nhd.  Kahn,  s.  Kluge  EWb.  s.  v., V.  Bahder,  Wortwahl  30);  damit  ablautend  aisl.  kcena  ,Art  Boot';  dazu weiter  (<C  *gandhna)  anord.  kanna,  aschw.  kanna,  dän.  kande,  ags.  canne, and.  kanna,  ahd.  channa  , Kanne',  woraus  spätlat.  canna  entlehnt  ist;  aus fränk.  kanna  auch  prov.  cana  , Hohlmaß',  afr.  channe  ,Kanne',  s.  Meyer- Lübke  1596,  Gamillscheg  EWb.  d.  Franz.  168;  daneben  ahd.  chanta, canneta,  fränk.  cannada  ^KsLXine^  (<Cgcindha).
478:balt.  *gu7iz-  in  güzys  ,Kropf  bei  Vögeln,  Adamsapfel,  Kopf  des  Ober^ scbenkelknochens;  Kohlkopf,  gü^iü,  guzti  ,sich  zusammenballen,  ein- mummeln; sich  zur  Erde  setzen  (vom  Huhn,  das  die  Flügel  ausbreitet)', güHä  ,Lager,  Nest  eines  Huhns,  einer  Gans';  apr.  gunsix  ,Beule'  (Ht, güzas,  güzikas  ,Buckel,  Drüse,  Knorren'  u.  dgl.  aus  dem  Poln.) ;
717:a6ech.  hyzü  , Hüfte,  Oberschenkel',  poln.  giza^  giza  , Knochenkopf  am Schienbein  u.  dg'L'  (auch  ksl.  gyza  vimnaja  , Weinstock',  serb.  gidza  ds. als  , Knorren,  Knorrengewächs') ;  wahrscheinlicher  hierher  als  zu  *geng- (s.  dort),  poln.  guz  , Beule,  Höcker',  guza  , Hinterer',  ^loven.  güza  , Hinterer, Höcker',  wie  z.  T.  wohl  auch  andere,  an  sich  auch  mit  guz  =  gqz-  ansetz- bare Worte  (s.  *geng-) ;  doppeldeutig  sind  auch  die  Worte  mit  halt,  (gunz-) güz-  Avie  gunzys,  güzys  , Kropf  bei  Vögeln,  Kopf  des  Oberschenkelknochens' usw.;  s.  Mühlenbach-Endzelin  Lett.-D.  Wb.  I  685,  687;
943:Air.  mir.  gabul  ,gegabelter  Ast,  Gabel;  Gabelungspunkt  der  Schenkel, vulva^,  cymr.  gafl  , Gabel;  Schenkelgabel,  vulva^,  abret.  Plur.  gablau Gabel^,  nbret.  gavl,  gaol  ,Gabelung^  (mit  2-Umlaut  von  a  zu  e  acymr. gebel  ,dolabra^,  cymr.  gefail  [-l-St.]  ,Zange^,  bret.  gevel  m.,  acorn.  geuel- hoern  gl.  munctorium),  (gall-)lat.  gabalus  ,Marterholz,  Galgen^;  die  brit. Formen  erweisen  ein  kelt.  *^a6?o-;  das  mittlere  a  in  ^rafea^ws  ist  wohl  lat. ; V.  Wartburg  trennt  gallorom.  gabalus  ,Speer^  (älter  ,*Gabel^),  das  in  *gab- lakkos  ,Speer^  (cymr.  gaflach  ds.)  stecke,  von  gabulum  , Galgen^,  aber  das  u in  air.  gabul  (*ghabhlo-)  ist  nur  epenthetisch ;
1120:*ghei-gh-  :  aisl.  norw.  dial.,  g^^9^  , seitwärts  abschwenken',  aisl.  geigr 0j.  , Schaden'  (ursprgl.  Anschauung  ,*schief  abstehen,  klaffen'  z.  B.  von Hölzern) ;  vgl.  nhd.  Schweiz.  Geigle  , Doppelast  an  einem  Baume,  der  in beliebigem  Winkel  auseinandergeht;  PL  die  Schenkel',  nhd.  Heugeige ^Stecken  mit  seitwärts  abstehenden  Astresten  zum  Aufschobern  des  Heus'; nhd.  dial.-  geigen  ,sich  hin  und  her  bewegen',  aisl.  gigjo,  aus  mnd.  mhd.  glge, uhd.  Geige  als  Musikinstrument;  ags.  /o?'-,  of-gcegan  ,ab weichen  von,  über- schreiten', gsegl  und  gägol  ,ausgelassen,  ausschweifend',  afries.  geia  , über- treten, unterlassen,  Buße  zahlen  für,  büßen';  norw.  dial.  giga,  gigla,  gigra ,lose  stehen,  wackeln',  engl,  gig  (nord.  Lw.)  ,leichter  Wagen,  leichtes  Boot', whirligig,  dän.  gig  , Kreisel  als  Spielzeug';  ndd.  giggelen,  engl,  to  giggle  ,ver- steckt,  spöttisch  lachen';  als  ,frei  abstehende,  bewegliche  Segelstange' hierher  ndl.  gei  ,Raa'  (Grundf.  geig{*j)a?),  ndd.  glk,  ndl.  gijk  ds.  und  mnd. geck  von  drehbaren  Dingen  (z.  B.  Deckel,  Fensterladen,  Pumpstangen), auch  ,Narr'  (nhd.  Geck)-  hierher  (nach  Wissmann  Nom.  postverb.  41)  got. geigö  f.  ,Gier^,  ga-geigan  ^gewinnen^  faihu-geigan  ,begehren^;  s.  S.  427.
1413:ghengh'  ^schreiten;  Schritt,  Schenkelspreize,  Schamgegend'.
1414:Ai.jdmhas-  n.  ,Schritt,  Flügelschlag',  jaw^Ää  ,Unterschenkel',  av.  zangdvf^ , Knöchel  des  Fußes',  -zangra-  (in  Kompositis)  ds.,  schwundstufig  SA.jagJidna; m.  n.  ,Hinterbacke,  Schamgegend'  :  gr.  -/.oxco^rj  ,Stelle  zwischen  denil Schenkeln'  (assim.  aus  *-/.ax(hvQ) ;
2089:got.  qipus  ,Magen,  Mutterleib',  qipuhaftö  ,schwanger';  aisl.  kvidr  m. ,Bauch,  Mutterleib',  kvidugr  ,schwanger',  ags.  cwid(a)  m.  , Mutterleib',  ahd. quiti  ,vulva',  quoden  ,Innenseite  der  Oberschenkel';
2657:hierher  osk.  icahag  ,incipias',  kahad  ,capiat':  umbr.  3.  PI.  Konj.  Perf. kukehe(n)s  ,occupaverint^  =  lat.  capere:  cepi  (s.  unten  S.  527  f.);  umbr.  cehefi ,captus  Sit'  ist  Konj.  Pass.  des  /-Perfekts  (E.  Fraenkel,  Fil.  Biedr.  Räksti 1940,  8 f.);
2817:lat.  capiö,  -ere,  cepl,  captus  ,nehmen',  f'^^M^jceps,  -cupäre  , Vogelfänger,  K/^ Vögel  fangen',  parti-ceps  , teilnehmend',  capäx  , fassungsfähig,  tauglich', capedo,  -inis  ,einfaches  tönernes  Gefäß  im  Opfergebrauch;  Trinkgefäß', capulus  , Bahre,  später  Sarg'  und  , Griff,  Handhabe',  capula  , Schöpfgefäß' (capuläre  ,von  einem  Gefäß  ins  andere  schöpfen'),  capistrum  , Schlinge zum  Fassen  eines  Gegenstandes;  bes.  Halfter'  (aber  capis,  -idis  , Henkel- schale', umbr.  kapife  ,capide',  osk.  %a7iL6ixoix  ,oUarium'  vielleicht  aus  gr. aytacpig  mit  s-Abfall  in  allen  drei  ital.  Sprachen ;  sicher  ist  capisterium  Lw. aus  O'AacpiüTriQLov) )  capsa  , Behältnis,  Kapsel,  Kasten',  capsus  ,der  Wagen- kasten; Käfig  für  wilde  Tiere'  (daraus  gr.  xdipa,  -Kdnifia)]
2849:kap-ut,  -(g)1o-  jKopf;  Pfanne  am  Schenkel;  Kniescheibe';  ursprüngl.  etwa »Schalenförmiges',  s.  unten. Ai.  kapücchala-  n.  (aus  *kaput')  ,Haar  am  Hinterkopf,  Schopf,  Schale'; lat.  Caput,  -itis  ,Kopf,  Haupt';   bi-caps  , zweiköpfig';
2853:Mit  /-Suffixen:  ai.  kapäla-  n.  , Schale,  Hirnschale,  Schädel,  Pfanne am  Schenkel,  schalen-  oder  scherhenförmiger  Knochen',  pehl.  kaparak (Scheftelowitz  BB.  28,  144)  , Gefäß',  kapöll  , Kniescheibe',  kapöla-  j^^ jWange'  ;
2922:vielleicht  aisl.  hadda  f.  ,Ring,  Henkel,  Bügel' _(*Äa;>i/)ün  :  catena;  recht unsicher),  wohl  ags.  heador  n.  ,Einschließung,  Gefängnis';
2995:keg-y  keng-  und  kek-,  kenk-  , Pflock  zum   Aufhängen,   Haken,    Henkel*; auch  ,spitz  sein*;  vgl.  das  ähnliche  kak-^   kank-]  und  kenk-^  konk-, Npers.  (iang  , Klaue,  Faust*  (*kengo-)',
3002:heUll  m.  ,Hinterbug*;  mit  intensiver  Gemination:  ags.  haccian  ,liackeu* mnd.,  mhd.  hacken  ds.,  und  die  ^-Verba:  a^s.  ofhceccan  ,amputareS  ahd. hecchen  ,beißen,  stechenS  mhd.  hecken  , hauen,  stechen*;  nasaliert  mnd. hank  ,Henkel*  (daraus  aisl.  hgnk  m.,  hanki  f.  ,Henkel'),  ndl.  honk,  ostfries. hunk  ,Pfahl,  Pfosten';
== POK_03.txt
231:gr.  dor.  (bg  (*öus)  ,Ohr';  öu  auch  in  öjJ^ara  , Ohren'  Alkm.,  äficp-wsg Theokr.  ,mit  zwei  Henkeln',  dor.  i^-wßddia  , Ohrringe',  vTtsQ-cbirj  , Gaumen', att.  lay-cbg,  hom.  lay-coog  n.  ,Hase'  (*sbg-öusos)  ,mit  schlaffen  Ohren'; 3US-  in  gr.  lak.  a'ög  ,Ohr',  PI.  äavd-a  {^ava-avd-a)  Alkm.,  tarent.  äxa (*av(jara)]  ion.  rtaQ-rj'ioVj  att.  Ttcco-sla^  lesb.  Ttaq-ava  , Schläfe'  (:  air.  arae)-^ gr.  ous-  (Kreuzung  des  nominativischen  öus-  mit  dus-)  in  att.  oi)g  (*odaog) ,Ohr*,  hom.  Gen.  o^axog  {*ova'i}Tog),  (bytlösg  , Ohrringe'  Hes.  (*ous-n-ko-)'^ über  dy.ova)  s.  oben  S.  18,  587 ;  über  att.  dyLgcaad-ai  {*a'/.Q-ovg-)  s.  Schwyzer Gr.  Gr.  1,  348;
348:fäinn  ,bunt  gesprenkelt',  ags.  fägian,  ahd.  fehen  , schmücken' ;
412:^Qii^ipüdinät   {*pld')    ds. ;   pledindt    ,mit  den   Flügeln   schlagen',   pledins Schmetterling*  ;  vgl.  E.  Fraenkel  Mel.  Boisacq  1,  357  ff.
541:C.  Kons.  Erweiterungen  von  per-  s.  noch  miier  perk',prek-  .gesprenkelt^^ pers-  ,sprühen,  spritzen,  gesprenkelt'.
677:2.  perk-,    prek-    ,gesprenkelt,    bunt',    oft    zur  Bezeichnung  gesprenkelter,
701:perS'  ^sprühen,  stieben,  spritzen  (bespritzt  =  gesprenkelt),  prusten^ ;  prso-s , Staub,  Asche'.
702:Ai.  pfsat,  pj-satd-m  n.  ,Tropfen';  pfsant-^  L  pfsa^l , gesprenkelt,  scheckig, bunt',  prsati  , scheckige  Kuh,  gefleckte  Antilope^;  av.  parhiya-  ,vom Wasser',  n.,  vielleicht  , Schneewasser' ;  aisl.  fors^  foss  m.  ,Wasserfall' ;
706:Ai.  pärsni-  t,  av.  päSna-  n.  , Ferse';  gr.  rttegvi]  f.;  lat.  perna  f.  {^persnd) ,Hinterkeule,  Schweineschinken,  Schenkel,  Bein',  pernls  , schnell'  (mit  der Ferse);  got.  fairsna,  a.s.  f er sna,  ahd.fersana  , Ferse'  {*persna)j  Sigs.fiersin f.  ds.  (*persni-)]  hitt.  parsina  (leg.  parsna)  , Oberschenkel,  Lende',  par§- (a)näi-  ,hocken'  (auf  den  Oberschenkeln).
1193:Lit.  rai-nas  ,grau,  buntgestreift';  rm-mas  ,bunt';  air.  nahach  , gespren- kelt', lit,  raX-has  , gesprenkelt,  graubunt'  (raibti  , flimmern'),  lett.  räibs ,bunt,  fleckig',  bes.  von  Tieren,  apr.  roaban  , gestreift',  russ.  klr.  ribyj ,bunt';  *roi-ko-  scheint  die  Grundlage  von  ahd.  reh  n.,  reho  m.,  ags.  rä, räha  m.  ,Reh',  aisl.  rä  f.,  ags.  rcege  (*raigjön-),  ahd.  reia^  reia  (unklar)  und nhd.  Ricke,  ndl.  reJcke  ,Ricke',  (expressiv)  wozu  wohl  ai.  risya-  m.  , Anti- lopenbock'.
1260:^4rm.  e^^  Gen.  ervoy  ,Bug,    Schulter  von  Tieren';   lit.   rietas  m.   ^Ober- schenkel,  Lende',  lett.  iHeta  f.  ,Bein';  ksl.  i^ih,  öech.  rit  ;podex^ Trautraann  242,  Liden  Mel.  Pedersen  88  f.
1626:mir.  sen  (*segno-)  ,Fangnetz',  cymr.  hoenyn  i^sogno-),  umgelautet  hwynyn ds.;  gallo-lat.  sagum  {^sogom  oder  *Segom)  ,Soldatenmantel';  mnd.  mhd. Senkel  ,Schnürriemen',  nhd.  ßchnürsenkel,  Schuhriemen';  lit.  segti  ,heften', Iter.    sagyti,   ablaut.    sägas   , Schleife   zum   Befestigen',   sagä  f.   ,Klammer,
1920:WP.  II  497  f.,  WH.  II  525,  Schwyzer  Gr.  Gr.  1,  727^;  dazu  sreu-  ,fließen*} nach  E.  Fraenkel  Gl.  32,  33  hierher  gr.  qed-sa  ,Nasenlöcher,  Nase',  ^d^oj , Wogenschwall',  sowie  ^/^,  qivög  ,Nase^  als  ,die  Triefende'.
1976:, Enkel'  aus  *suiö[u]'nö-s),  als  uridg.  Bildung  erwiesen  durch  tochar.  g S07jä  (A  se)  ,Sohn*  und  das  nach  dustr  ,Tochter'  umgebildete  arm.  v^tr ,Sohn';  auch  ags.  suhterga  ,Enkel,  Neffe^  kann  eine  entsprechende  Um« bildung  nach   Tochter  sein.
2044:Mit  e-Vokalismus:  gr.  v.ö^ßog  m.  ,Band,  Schleife',  Y.ofxß6(j)  ,knüpfe*;  noi hempa  ,Kleiderstrippe,  Schlinge,  Henkel'  (auch  ,Zeug  von  Hanf,  in  welche? Bed.  sicher  von  hamp  ,Hanf'  beeinflußt);
2197:mit  bsl.  -ul-  =  lat.  -al-  (ind.  -o^[9-]):  mit  £-Suffix:  lit.  kiilU,  külsis  ,Hüfte' (mit  Ä:-Einschub:  kulkBs,  kulk§ms  ,Knöchel,  Sprunggelenk'),  apr.  culczi ,Hüfte';  mit  -Ä:-Suffix:  lit.  kulnas  m.,  kulnis  f.  ,Hacke,  Ferse'  (*kulk-n-), urslav.  *kulkä  f.  ,Hüfte'  in  spätksl.  khka  ,poples',  bg.  kilka  ,Hüfte,  Ober- schenkel' (^s•k^Ui  ,verrenke') ;  skr.  kük  ds.  usw. ;
```


## [2026-09-07T19:30:38.976Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(423,431):\n    print('--- leaf',i); print(pages[i][:1600]); print()\n\""
}
```


### [2026-09-07T19:30:40.364Z] TOOL RESULT

```
--- leaf 423
�ti,  lett.  niekdt  , Getreide  durch  Schwingen reinigen';  daneben  lit.  lieküoti  ds.,  lett.  liek§a  , Worfschaufel' ;  das  halt,  l- läßt  sich  nicht  durch  Dissimil.  erklären.
WP.  II  321,  Trautmann  195f.;  J.  Loth  RC.  40,  352 f.;  41,  193 ff.
neik-  :  nik-  :  nik-  , anfallen,  losstürzen,  heftig  beginnen'.
Gr.  veTyiog  n.  ,Zank,  Streit',  vsiycio)  ,zanke,  streite,  schelte',  vielleicht auch  vtyiT],  dor«  vlxä  f.  ,Sieg',  vrxaw  ,siege';  kelt.  (?)  FIN  Nicros  ^Neckar*; ags.  ge-ricestan  ,streiten'  (*naihstian?)',  bsl.  *ninkö  ,beginne  heftig'  in  lit. -ninkü,  -nikti  ds.,  lett.  nikns  , zornig',  ablaut.  naxks  , heftig',  lit.  dial.  neikom ,sehr',  apr.  neikaut  ,wandeln',  slav.  *niknq,  *nikngti  in  aksl.  v^z-nikngti , wieder  zu  sich  kommen',  russ.-ksl.  niknuti  , hervorwachsen',  usw.
WP.  II  321,  Trautmann  199,  Kuiper  Nasalpräs.  186  f.,  Hofmann  Gr. etym.  Wb.  213.
I
762  •
neic-  ^leibliche  Todesvernichtung',  neku-s  ,Toter,  Leiche^
Ai.  naiyati,  nasati  ,geht  verloren,  verschwindet,  vergeht',  näHyaV ,macht  verschwinden,  richtet  zugrunde'  (dehnstufig  gegenüber  lat.  noceö) av.  nasyeiti  , verschwindet',  Partiz.  ai.  nastd-  , verlorengegangen',  ^v* naSta-  ds.  (=  lat.  e-nectus),  nasiSta-  ,verderblichst',  nas-  f.  ,Not,  UnglücW (=  lat.  nex,  gr.  vi-K-rag,  v€y,8g'j  ai.  -nas  Adj.),  nasu-  , Leichnam,  Aas' (==  gr.  vsKVg,  lat.  nequ-älia]  vgl.  *'i}ku-  in  air.  ec  usw.),  dehnstufig  ai nä§a-  m.  ,das  Zunichtewerden';  gr.  vsTtsg'  veytqol  Hes.  (davon  vexag

--- leaf 424
 nok^t-  f.  (ursprüngl.  neutr.  ?  ?),  nok'iti-, nokj^tu-  f.,  noknt(e)r  n. ;  über  Ablautformen  s.  unten.
Ai.  ndk  (*ndkt)  Nom.  ,Nacht'  (nag  jihlte),  naktä  f.  Du.,  naktam  Adv. erstarrter  Akk.  ,nachts',  Instr.  PI.  naktdhhih  ds.  (Nachahmung  von  dhabhih), Akk.  PI.  ndktih  ,Nächte';
gr.  rv^j  vv-KTÖg  f.  , Nacht',  im  Kompositum  wtctl-,  j^xto-,  v&ktwq  Adv. ,nachts'  (*Akk.  gebildet  wie  VScjq),  wy^rsgög,  wyizsQLvög  ,nächtlich'  (:  lat. nocturnus)]  unklar  sind  vvxct'  vv%tü)q  Hes.,  hom.  elvdvvxsg  ,neun  Nächte hindurch',  evvvxog  ,nächtlich',  ftavvvxiog  ,die  ganze  Nacht  dauernd',  avrovvxi ,in  derselben  Nacht';
alb.  nate  , Nacht* ;
lat.  nox,  noctis  ,Nacht'  (Gen.  PL  noctium  i-St.,  aber  deutlich  kons.  St. im  Adv.  nox  ,nachts'  aus  Gen.  *nokt-es,  -os);  nocturnus  ,nächtlich'  (:  vvyt- TSQLvög,  vvxtcüq)  ;  vom  Stamme  *nohtu- :  lat.  noctü  ,bei  Nacht',  noctua ,Nachteule' ;
air.  i-nnocht  ,hac  nocte',  mcymr.  peu-noeth  ,jede  Nacht',  trannoeth  ,am folgenden  Tage',  acymr.  henoid,  cymr.  he-no  ,hac  nocte',  corn.  hanethj mbret.  henoz  ds.;  cymr.  corn.  nos,  bret.  noz  , Nacht',  wohl  aus  *nokt-s  u- cymr.  neithiwyr,  neithwyr  (enthält  hwyr  , Abend')  ,last  night',  corn.  nehues mbret.  neyzor,  nbr.  neizeur  ds. ;
763
got.  nahts  (Dat.  PI.  nahtam  nach  dagam),  aisl.  nött,  nätt,  ahd.  as.  naht, ^.  neaht,  niht  ,Nacht'  (kons.  St.),  ags.  nihterne  .nächtlich' ;
lit,  nahüs  (kons.  Gen.  PL  naktü),  lett.  nakts,  apr.  naÄ^iw  (Akk.  Sg.) ^Nachts  nak{t)v-yne  

--- leaf 425
.  .teile  mir zu,  fresse,  weide',  Herod.  äva-ve^iead-ai  ,verteilen,  aufrechnen',  ro/u?y , Verteilung;  Weideplatz',  vofxdg,  -döog  , weidend,  nach  Weide  umher- schweifend', voixevg  ,Hirt;  Verteiler',  vofxög  , Weide,  Wohnsitz',  vöjxog ^Anordnung,  Ordnung',  voixi^a)  ,sehe  als  geltend  an',  vöfALffjxa  , Brauch.  Sitte, Einrichtung,  gebräuchliche  Geld  Währung';  dehnstufig  vcoy,dw  , teile  zu'; vifj^saig  ,\]nwi[\G,  göttliche  Rache'  {^vs^erig,  eig.  .das  Zurechnen').  vs^ea{a)da), -aofxaL,  -i^ofxaL  .zürnen,  tadeln',  vslisxcjq  ,Rächer';  alb.  name,  neme  , Fluch, Verwünschung',  formell  =  vöfxog;  nemes  ,der  Fluchende,  Gotteslästerer'; hierher  auch  air.  nämae,  Gen.  nämait  ,Feind'?
Daß  v€(A,og  n.  .Weideplatz'  hierher  gehöre,  ist  nicht  ganz  sicher ;  s.  unter 2.  nem-'
lat.  numerus  .Zahl'  (*nomes-o-),  nummus  .Geld.  Münze'  (aus  gr.  v6f.uixog .gesetzmäßig,  üblich') ;
air.  nem  f.,  mir.  neim  ,Gift*  (vgl«  ^^^-  Gif t :  geben) ;
got.  as.  ags.  niman,  ahd.  neman,  aisl.  nema  ,nehmen',  dehnstufig  got. anda-nem  n.  .Empfang',  ahd.  näma  ,gewaltsames  Nehmen,  Raub';  ags. näm  f.  ,das  Ergreifen'  aus  aisl.  näm  m.  ,das  Nehmen,  Lernen';  got.  anda-nems ,angenehm',  ahd.  nämi  ,genehm';  lett.  y,emt  (kontaminiert  aus  nemt  und jemt)  ,nehmen';   lit.  nämas,   meist  PI.  namai  ,Wohnung,  Haus',  lett.  nams
764  *
m.  ,Haus';  ablaut.  lit.  dial.  numal  ,Tiamai'  (*?2om-);  lit.  nuoma,  lett.  nuQm ,Zins,  Pacht'  (Vokalstufe  wie  gr.  vwfxdcü).
WP.  II  330f,  WH.  II  158f.,  Tra

--- leaf 426
ti

--- leaf 427
  

--- leaf 428
, 

--- leaf 429


--- leaf 430
```


## [2026-09-07T19:30:49.344Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[425][1400:6000])\n\""
}
```


### [2026-09-07T19:30:50.550Z] TOOL RESULT

```
aus',  lett.  nams
764  *
m.  ,Haus';  ablaut.  lit.  dial.  numal  ,Tiamai'  (*?2om-);  lit.  nuoma,  lett.  nuQm ,Zins,  Pacht'  (Vokalstufe  wie  gr.  vwfxdcü).
WP.  II  330f,  WH.  II  158f.,  Trautmann  193,  201,  E.  Laroche,  La racine  veu-]  E.  Benveniste  BSL.  32,  79  ff.
2.  nem-  , biegen';  nm-tö-  ^gebogen^;  nemos-  n.  ,Hain'.
Ai.  ndmas-  n.  =  av.  ndmah-  n.  , Verbeugung  =  Verehrung,  Huldio-un?' ai.  ndmati  , beugt  sich,  neigt  sich,  beugt,  biegt'  (Kaus.  nämayati)^  av iidmai
```


## [2026-09-07T19:30:55.259Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '^nephew\\|^niece\\|^nepotism' KLN_1966.txt | head; echo \"=== 1971\"; grep -n '^nephew\\|^niece' KLN_1971.txt | head"
}
```


### [2026-09-07T19:30:55.348Z] TOOL RESULT

```
25196:nephew
25232:nephew,  n.  —  ME.  neve,  neveu,  fr.  OF.  neveu,  ne- vou  (F.  neveu),  fr.  L.  neputem,  acc.  of  nepos, ‘grandson’,  in  post-Augustan  L.  ‘nephew’,  in general  (poet.),  ‘descendant’,  which  stands  for nepot-s  and  is  cogn.  with  OI.  ndpat,  Avestic  na- pdt-,  naptar-,  OPers,  napdt-,  ‘grandson,  descen¬ dant’,  OLith.  nepuotis,  neputis,  ‘grandson’,  Olr. nia,  gen.  ninth,  ‘son  of  a  sister’,  W.  nei,  nai,  ot s.m.,  Co.  noi,  ‘grandson’,  OE.  nefa,  OS.  nebo, ON.  nefi,  OFris.  neva,  Du.  neef,  OHG.  nevo, MHG.  neve,  G.  Neffe,  ‘nephew’,  Gk.  a-veijji6?
25259:nepotism,  n.,  favoritism  shown  to  relatives  esp.  in appointments  to  high  offices.  —  Orig.  favori¬ tism  of  Popes  shown  to  their  natural  children, euphemistically  referred  to  as  their  ‘nephews’; F.  nepotisme,  fr.  It.  nepotismo,  a  var.  of  nipotis- mo,  fr.  nipote,  ‘nephew’,  fr.  L.  nepotem,  acc.  of nepos.  See  nephew.  For  the  ending  see  suff.  -ism.
25404:niece,  n.  —  ME.  nece,  neyce,  fr.  OF.  niece  (F. niece),  fr.  VL.  neptia  (whence  also  O Proven?. nepsa,  ‘niece’),  a  var.  of  VL.  nepta  (whence
=== 1971
160402:nephew, n. — ME. neve, neveu , fr. OF. neveu, ne- 
161411:niece, n. — ME. nece, neyce, fr. OF. niece (F.
```


## [2026-09-07T19:31:01.409Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (25232,25404):\n    pos=sum(len(l)+1 for l in lines[:ln-1]); leaf=t[:pos].count('\\f'); print('line',ln,'leaf',leaf)\npages=t.split('\\f')\nimport re\nprint(re.findall(r'(?m)^\\s*(10[2-5][0-9])\\s*$', pages[531]))\nprint(pages[531][:300])\n\"\necho \"---- nephew full\"; sed -n '25232,25258p' /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt\necho \"---- niece full\"; sed -n '25404,25420p' /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt"
}
```


### [2026-09-07T19:31:02.787Z] TOOL RESULT

```
line 25232 leaf 556
line 25404 leaf 560
[]
— with  -/-forma¬ tive  element — OSlav.  milu,  ‘charitable’,  Russ. milyj,  Pol.  mily,  Czech  and  Slovak  mily,  Lith. mielas,  mylas,  ‘beloved,  dear’,  Lith.  myliu, myleti,  ‘to  love’,  Lett,  mil's,  OPruss.  mijls,  ‘be¬ loved,  dear’,  Russ,  milovat’,  ‘to  show  mercy’, Pol.  milovac,
---- nephew full
nephew,  n.  —  ME.  neve,  neveu,  fr.  OF.  neveu,  ne- vou  (F.  neveu),  fr.  L.  neputem,  acc.  of  nepos, ‘grandson’,  in  post-Augustan  L.  ‘nephew’,  in general  (poet.),  ‘descendant’,  which  stands  for nepot-s  and  is  cogn.  with  OI.  ndpat,  Avestic  na- pdt-,  naptar-,  OPers,  napdt-,  ‘grandson,  descen¬ dant’,  OLith.  nepuotis,  neputis,  ‘grandson’,  Olr. nia,  gen.  ninth,  ‘son  of  a  sister’,  W.  nei,  nai,  ot s.m.,  Co.  noi,  ‘grandson’,  OE.  nefa,  OS.  nebo, ON.  nefi,  OFris.  neva,  Du.  neef,  OHG.  nevo, MHG.  neve,  G.  Neffe,  ‘nephew’,  Gk.  a-veijji6?
nepho-
1040
(for  *sm-neptiyos),  ‘cousin,  nephew'.  Cp.  Gk. veTtoSec  (Odyssey  4,  404;  said  of  seals),  which prob.  means  ‘children,  descendants’,  and  is  the plural  of  vettco?  (equivalent  to  L.  nepos),  but was  refashioned  according  to  the  declension  of ttoiji;,  gen.  710865,  ‘foot’.  Cp.  also  niece,  nepo¬ tism.
nepho-,  combining  form  meaning  ‘cloud’.  —  Gk. vetpo-,  fr.  vltpoi;,  ‘cloud’  (whence  vE<peXy], ‘cloud’),  which  is  cogn.  with  L.  nebula,  ‘mist,  fog, cloud’.  See  nebula  and  cp.  nepheline,  Nephelium, nephelo-.
nephology,  n.,  that  branch  of  meteorology  which deals  with  clouds.  —  Compounded  of  nepho- and  Gk.  -Xoyia,  fr.  -X6yo<;,  ‘one  who  speaks (in  a  certain  manner);  one  who  deals  (with  a certain  topic)’.  See  -logy.
Derivatives :  nepholog-ic-al,  adj.  nepholog-ist,  n.
nephoscope,  n.,  an  instrument  for  determining  the altitude,  velocity  and  direction  of  clouds.  — Compounded  of  nepho-  and  Gk.  -ax6mov,  fr. oxorstv,  ‘to  look  at,  examine’.  See  -scope. Derivative:  nephosocop-ic,  adj.
nephr-,  form  of  nephro-  before  a  vowel.
nephralgia,  n.,  pain  in  a  kidney  ( med .)  —  Com¬ pounded  of  nephr-  and  Gk.  -aXyia,  fr.  SXyo 5, ‘pain’.  See  -algia.
nephrectomy,  n.,  excision  of  a  kidney  (med.)  — Compounded  of  nephr-  and  Gk.  -EXTopia,  ‘a cutting  out  of’,  fr.  Ex-ropf),  ‘a  cutting  out’.  See -ectomy.
nephria,  n.,  Bright’s  disease  (med.)  —  Medical  L., , fr.  Gk.  vscppii;,  ‘kidney’.  See  nephro^  and  1st  -ia.
nephric,  adj.,  pertaining  to,  or  near,  the  kidneys. — •  Formed  with  sufT.  -ic  fr.  Gk.  vstp p6?,  ‘kidney’. See  nephro-.
nephridial,  adj.,  pertaining  to  a  nephridium.  — See  next  word  and  adj.  suff.  -al.
nephridium,  n.,  one  of  the  excretory  organs  of some  invertebrates  ( zool .)  —  ModL.,  fr.  Gk. vecppi8L05, ‘of  the  kidneys’,  fr.  VEtppo;,  ‘kidney’. See  nephro-.
nephrite,  n.,  a  variety  of  jade  (mineral.)  —  G. Nephrit,  coined  by  the  German  geologist  and mineralogist  Abraham  Gottlob  Werner  (1750- 1817)  in  1794  fr.  Gk.  ve< pp4c,  ‘kidney’  (see  ne¬ phro-),  and  suff.  -it,  which  goes  back  to  Gk. -fry?  (see  subst.  suff.  -ite);  so  called  in  allusion to  its  supposed  efficacy  against  diseases  of  the kidneys.
nephritic,  adj.,  pertaining  to,  or  affecting,  the  kid¬ neys.  —  Late  L.  nephriticus,  fr.  Gk.  vcspiTixos, ‘pertaining  to  the  kidneys’,  fr.  vcypo?,  ‘kidney’.
See  nephro-.
nephritis,  n.,  inflammation  of  the  kidney  (med,) —  Late  L.  nephritis,  fr.  Gk.  VE9PIT1.5,  fr. veppo?,  ‘kidney’.  See  nephro-  and  -itis.
nephro-,  before  a  vowel  nephr-,  combining  form meaning  ‘kidney’,  or  ‘nephric  and’.  —  Fr.  Gk. VE9P65, ‘kidney’,  which  stands  for  I.-E.  *negwh- rds,  ‘kidney;  testicle’,  and  is  cogn.  with  L. (Praenestine)  nefrdnes  (for  *negwhron-),  ‘kid¬
neys  ;  testicles’,  L.  (Lanuvian)  nebrundines,  ‘kid¬ neys,  testicles’,  ON.  nyra,  Dan.  nyre,  Swed. njure,  ONorw.  nyra,  Norw.  ryggja-nyre,  "kid¬ ney’,  ME.  nere,  MDu.  mere,  Du.  nier,  ‘kidney’, OHG.  nioro,  niero,  ‘kidney,  testicle,  loin’,  MHG niere,  nier,  ‘kidney,  loin’,  G.  Niere,  ‘kidney’  (fr. Teut.  *neurian-,  *neuran-,  fr.  I.-E.  *negwhron-). Cp.  perinephrium.
nephrolith,  n.,  a  renal  calculus  (med.)  —  Com¬ pounded  of  nephro-  and  Gk.  Xi-ffoc,  ‘stone’.
See  -lith.
nephropexy,  n.,  the  fixing  of  a  floating  kidney (med.)  —  Medical  L.  nephropexia,  compounded of  nephro-  and  Gk.  -7r»)5ta,  fr.  ‘a  making
firm,  fastening’,  which  derives  from  the  stem  of 7t7]Yvtjva!.,  ‘to  join,  make  firm’.  See  -pexy.
nephrosis,  n.,  disease  of  the  kidneys  (med.)  — Medical  L.,  coined  by  Muller  in  1905  fr.  Gk. V£cpp6c,  ‘kidney’  (see  nephro-),  and  suff.  -osis.
nephrotomy,  n.,  the  operation  of  cutting  into  the kidney  ( surg .)  — -  Compounded  of  nephro-  and Gk.  -xopta,  ‘a  cutting  of’,  fr.  Topirj,  ‘a  cutting'. See  -tomy.
---- niece full
niece,  n.  —  ME.  nece,  neyce,  fr.  OF.  niece  (F. niece),  fr.  VL.  neptia  (whence  also  O Proven?. nepsa,  ‘niece’),  a  var.  of  VL.  nepta  (whence
OProven?.  neta,  ‘niece’,  Sp.  nieta,  Catal.,  Port. neta,  "granddaughter’),  fr.  L.  neptis,  ‘grand¬ daughter’,  in  Late  L.,  "niece’,  which  is  rel.  to nepos,  gen.  nepotis,  ‘grandson’,  in  post-Augus- tan  L.,  ‘nephew’,  and  cogn.  with  OI.  naptih, Avestic  napti-,  ‘granddaughter’,  OLith.  nepte,  of s.m.,  Czech  net',  ‘niece’,  OIr.  necht,  W.,  OBret. nith,  MBret.  niz,  Co.  noith,  ‘niece’,  ON.  nipt, ‘sister’s  daughter,  niece’,  OE.  nift,  ‘niece,  grand¬ daughter,  stepdaughter’,  OHG.  nift,  of  s.m. (whence  the  dimin.  OHG.  niftila,  MHG.  niftel, ‘niece,  mother’s  sister,  cousin’),  MDu.  nifte, nichte  (Du.  nicht),  MLG.  nifte,  nichte  (whence G.  Nichte),  ‘niece’.  Sec  nephew, niello,  n.,  metallic  alloy  of  sulfur  with  silver,  cop¬ per,  lead,  etc.  —  It.,  fr.  VL.  *nigellum,  ‘a  kind of  black  enamel’,  subst.  use  of  L.  nigellum,  neut. of  nigellus,  ‘somewhat  black’,  which  is  a  dimin. of  niger,  ‘black’;  so  called  in  allusion  to  the color  of  this  alloy.  See  Negro  and  cp,  Nigella and  the  second  element  in  darnel.
Derivative:  niello,  tr.  v.,  to  decorate  with  niello. Niersteiner,  n.,  a  white  Rhine  wine  of  fine  quality.
—  Prop,  ‘wine  of  Nierstein',  a  village  near  Mainz, Germany.  For  the  ending  see  subst.  suff.  -er.
Nietzschean,  adj.,  pertaining  to  the  German  phi¬ losopher  Friedrich  Wilhelm  Nietzsche  ( 1 844- 1900)  or  his  doctrines;  n.,  a  follower  of  Nietz¬ sche.
Nietzscheanism,  n.,  the  philosophy  of  Nietzsche.
—  Formed  from  prec.  word  with  suff.  -ism. nieve,  n.,  a  fist.  —  ME.  neve,  nefe,  fr.  ON.  hnefi,
‘fist’  (whence  Dan.  nerve). nifie,  n.,  a  trifle  (dial.)  —  Perh.  a  blend  of  L.  nihil (see  nihil)  and  trifle.  Cp.  drail. nifty,  adj.,  smart,  stylish  ( American  Slang).  — Of  uncertain  origin.
Nigel,  Neal,  Neil,  Niall,  masc.  PN.  —  Fr.  Niall, lit.  ‘courageous’;  rel.  to  Ir.  niadh,  ‘champion’. The  name  was  Latinized  into  Nigellus,  whence arose  the  form  Nigel.  Cp.  the  unrelated  Roman surname  Nigellus;  this  latter  prop,  means  ‘some¬ what  black’,  and  is  the  dimin.  of  niger,  ‘black’ (see  next  word).
Nigella,  n.,  a  genus  of  plants,  the  fennel  flower (bot.)  —  ModL.,  fr.  L.  nigella,  fern,  of  nigellus, dimin.  of  niger,  ‘black’  (see  Negro  and  -ella  and cp.  niello) ;  so  called  from  the  black  color  of  the seeds.
niggard,  n.,  a  mean  person,  a  miser;  adj.,  mean, miserly.  —  ME.  niggard,  nigard,  fr.  ME.  nig,  ‘to be  stingy’,  which  is  prob.  of  Scand.  origin;  cp. ON.  Imoggr,  ‘stingy’.  Cp.  niggle.  For  the  ending see  suff.  -ard.
Derivatives:  niggard-lv,  adj.  and  adv.,  niggard- li-ness,  n.
nigger,  n.,  a  Negro.  —  Earlier  neger,  fr.  F.  negre, fr.  Sp.  negro.  See  Negro.
Derivatives:  nigger-ish,  adj.,  nigger-ling,  n. niggle,  intr.  v.,  to  busy  over  trifles  —  Related  to dial.  Norw.  nigla,  ‘to  busy  over  trifles’,  and  prob, also  to  niggard.
I
Derivatives:  niggl-ing ,  niggl-y,  adjs. nigh,  adv.,  near.  —  ME.  neih ,  neigh,  nigh,  fr.  OE. neah,  neh,  ‘near’,  adv.  and  adj.,  rel.  to  OS.  nah, adv.  and  adj.,  ON.  nd-,  Dan.,  Swed.  na-  (in  com¬ pounds),  OFris.  nei,  ni,  adv.  and  adj.,  MDu.  nd, Du.  na,  adv.,  adj.  and  prep.,  ‘nigh,  after’,  OHG. nah,  MHG.  nach,  G.  nah,  adv.  and  adj., Goth,  netva,  adv.,  and  prob.  cogn.  with  MPers. nox,  ‘the  first’  (see  Chr.  B.  Bartholomae,  Zum altiranischen  Worterbuch,  p.  48).  Cp.  near  (fr. OE.  near,  compar.  of  neah),  and  next  (fr.  OE. nehst,  niehst,  super],  of  neah).  Cp.  also  the  first element  in  neighbor.
Derivative:  nigNfiprep.
```


## [2026-09-07T19:31:13.763Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'grandchild\\|grandson' PHD.txt | head -20; echo \"=== nab\"; grep -n '^nab\\|^nap\\|nabāg\\|nab ' PHD.txt | head -20"
}
```


### [2026-09-07T19:31:13.831Z] TOOL RESULT

```
494:nab [np | N nawa] grandson. nabānazdišt [nb”nzdšt! = Av. nabünazdista-] next of kin. паї [w | M mp] family. ~ag [-R! | N náf(a)] navel. !naft [npt! | = M, N ~] moist, damp; naphtha. *naft [npt'] descendant. nahang [жле] province. *nakkira [nkyl’y] denying, repudiating. ~yih: repudiation. nāl- [wl- | P (n’r-), N ~] groan, complain. nam [nm | N ~] moisture. nám [SM < A £m; m | = M, N ~] name, fame. namad [nmt' | N <) felt. námag [MGLTA < A melt: ттк! | M пто, N пата] book, letter. namak [nmk! | M nmyhk, N ~] salt. namāz [OSGDE < A sgdh; nm’c | = M, N ~] reverence, prostration, prayer. ~ burdan: pay homage. nām-burdār [л?т bwlt?l | N ~] heir, preserving the father's name. nāmčišt [?жт-, ŠMcst'], (pad) ~: in particular, especially. ~ig [-yk'] famous, well known.
2136:grandson nab.
=== nab
494:nab [np | N nawa] grandson. nabānazdišt [nb”nzdšt! = Av. nabünazdista-] next of kin. паї [w | M mp] family. ~ag [-R! | N náf(a)] navel. !naft [npt! | = M, N ~] moist, damp; naphtha. *naft [npt'] descendant. nahang [жле] province. *nakkira [nkyl’y] denying, repudiating. ~yih: repudiation. nāl- [wl- | P (n’r-), N ~] groan, complain. nam [nm | N ~] moisture. nám [SM < A £m; m | = M, N ~] name, fame. namad [nmt' | N <) felt. námag [MGLTA < A melt: ттк! | M пто, N пата] book, letter. namak [nmk! | M nmyhk, N ~] salt. namāz [OSGDE < A sgdh; nm’c | = M, N ~] reverence, prostration, prayer. ~ burdan: pay homage. nām-burdār [л?т bwlt?l | N ~] heir, preserving the father's name. nāmčišt [?жт-, ŠMcst'], (pad) ~: in particular, especially. ~ig [-yk'] famous, well known.
2887:naphtha naft.
5154:nab
```


## [2026-09-07T19:31:20.004Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('PHD.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npos=sum(len(l)+1 for l in lines[:493]); leaf=t[:pos].count('\\f'); print('leaf',leaf, 'printed=',leaf-21)\n\"\necho \"=== NYB\"; grep -n 'nab\\b\\|napat\\|nawa' /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T19:31:21.261Z] TOOL RESULT

```
leaf 81 printed= 60
=== NYB
414:2an, anë [PNH] I, the cas. rect. of the pron. of the Ist p. sg.: P2:1.7; 5319 (v.s.v. £6).24 5719. 734-15, 7518, 9916, 11210. — Only SW: MPrs * (S, A-H II), ny (Henning, Irantstik 90 n. 2), as against MPrth "z = az < Av. (225 sqq.) azam. Identical with 1 !an(e), the full expression being an man, ané man or man anč (v. above). Through omission of man the epithet an(é) became a sort of ‘“‘modesty pronoun" for ‘T’, like NP bandah. This usage can be traced fairly far back. Cf the words of Tissaphernes, Xen. ‚Anab. II, 5%; thy učv yap šni tH xegar ridpav Bacrret uóvq šēeortv doOhy čyetv, thy 8 ent TH xapšta tomo dv tudv napdévtwv xal ēregoc ebrer@g Zyot. Curiously enough, in Swedish slang en annan ‘another’ is often
520:apa-ród [^plwd] adj. runaway 79. — < apa + !ród ‘whose face is turned away’.
781:āvaštan [HTYMWN-tn'] to seal, pt. = pret. pass. 3d p. sg. āvašt 19%; pt. āvašīt [HTYMWN-yt'] sealed up 11722; [pai- tāmbarān (*wbšt' =) ävast the seal of the prophets, of Muhammad, = Arab xdtamu l-nabīyīn, DkM 291%]. — Reading according to Henning, BSOAS XI, 1946, 725 sq. FrP ch. 23 gives for the ideogr. the gl. >wbstn' (var. *whstn'), to which Cod. U, adds the pres. forms 3d p. sg. "pbéyt! = āvašēt, Ist p. pl. "wb'šym = āvāšēm (or possibly "obhšym = āvaxšēm); it should, however, be observed that the Paz. readings are throughout anbaš-, anbiš-, thus ’nb$-, not °wbš-, so Bthl was fully exeused in his reading and etymo- logy (MirM II, 37-38), which Henning seems not quite to have understood (Bthl. translated it ‘festmachen’ but used this w. in & juridieal sense: 'to make & document valid before the law' through applying one's seal on it, which is in fact not far from the truth, v. Nyberg, By- zantion XXX VIII, 1968, 119-122).
1589:fréevanéh [plycp’nyh] works of super- erogation (Arab nawafil) 635. — Paz. fre- zawqn Antiä 136! (text not clear); -p- is inverse spelling of -v-, the normal spelling being plycw’n-: fréc-van derived from fréc (v. the preceding w.) by means of the suff. -van- (cf Av. aša-van-) ‘ex- ceeding the obligatory duties’; cf also frēcvānēnītak hac ‘moved forward, dis- placed from (its proper place)’ DkM 40418-19; v. next w. — Wrong TMK 59. — Hence
2740:nipart [nplt'] quarrel, combat 703. 1075. — MPrth pt. nbrd’d ‘to combat’, Ghilain 53; Paz. naward; NP nabard.
2752:nipistan [npštn'; YKTYBWN-tn'] nipés- to write 419. 110? etc. ; nipist estet it has been written, it is written 1139; nipist ēstāt it was written 1!—?; — pres. pass. nipēsihēt [YKTYBWN-yhyt'] is being written 18%; — pat dp i zarr nipištak 1079; apar nipistak written down 108?!; nāmak ~ 6 to write a letter to 49-9. 822, an inscription P 2:3.4; apar fravartak čton nipišt estat kū it was written in the letter (then dir. speech) 1872; apar én ayyätkär nipišt estet 1135-9. — OP ni-pais- ; MPrthPrs nbyštn nbys-; Paz. nawaštan nivés-; NP nuvistan, nivištan, nivés-.
4811:Xen. Anab. = Xenophon Anabasis.
5237:napat-: nap
6744:naward: nipart
6745:nawaštan, nivčs-: nipiš- tan
```


## [2026-09-07T19:31:27.768Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('PHD.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(76,86):\n    m=re.findall(r'(?m)^\\s*([4-9][0-9])\\s*$', pages[i])\n    print(i, m, pages[i][:80].replace('\\n',' | '))\n\""
}
```


### [2026-09-07T19:31:28.970Z] TOOL RESULT

```
76 []  kyswr, N ~] region, clime, continent. kišwzār, v. kišwānzār. kūb-, v. koftan. k
77 []  lābakkar [Pfkkl] suppliant. | — h: supplication. lajan [/cn! | N ~] mud, slime. l
78 [] ! | Р mng] mind. | manag [m^mk! | M mrg, N mana] like, resembling. ~ih: likeness, 
79 [] yk! | M mryg-] word, spell. marw [mlw! | M mrw, N —, (mary)] herb. marz [mlc | M
80 [] men- [myn-ytn' | M mn-, N man-] think, consider. „išn: thought, intention, dispo
81 [] t. móy [mwd | N ~] hair. móya$ [mwdk' | N méya] lamentation. móyen [mwdyn'] (mad
82 [] burdan: pay homage. nām-burdār [л?т bwlt?l | N ~] heir, preserving the father's 
83 [] M ny, N na] no, not. nék [nywk! | M nyk, N ~] good, beautiful. ~th: goodness. né
84 [] -, N ~] draw, design, paint. ~ag [-h! | (M agin, N nigār)] image, picture, diagr
85 [] [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-
```


## [2026-09-07T19:31:34.166Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'pdf page' PHD_pages.txt | head -5; echo ---; grep -n 'nab \\[np' PHD_pages.txt; echo ---; python3 -c \"\nt=open('PHD_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('nab [np')\nprint(t[max(0,i-3000):i+200][-1200:])\n\""
}
```


### [2026-09-07T19:31:35.475Z] TOOL RESULT

```
---
3638:nab [np I N nawa] grandson.
---
'n l ] belly (daevic).
murd                                    57                     namci5ti~

P murd      I P mwrt !] death.
            [mwlt l
murdan, mir- [YMYTWN-tn ' < A ymwtwn, '1/ mwt; mwltn l I M
  mu'rd, myr-, N .......] die.
murdar [mwTt'I, mwld'll N .......] carrion.
murnJenidan, murnJen- [mwlncyn-ytn ' ] destroy.
murw [mwlw l I M mWTW, (N mUTY)] bird.
murwa~ [mwlw'k I M mwrw', N murwa] omen.
                         '
murwizag, [mwlwyck ' ] little bird.
murw-nis [mwlwnyl] augur, soothsayer.
Imust [mwst l ] force, violence.
2must [mwst'] = must.
3must [mwst l ] complaint.
mustl-abarmand [mwstPPlm'nd] aggressive, aggressor.
 ....... ~ar [-kl] violent, rebellious.
mustomand [mwst)wmnd I N mustmand] complaining, unhappy.
Imusk [mwlk IN .......] musk.
                     '
2musk [mwsk I (N mtis)] mouse, rat.
                     '
must [mwst I N ---] fist.
                   l

mustan, mal- [mwstn', m'l- IN .......] rub, sweep.




                                        N
nab [np I N nawa] grandson.
nabanazdist [nb'nzdst = Av. naba1tazdista-] next of kin.
                       '
naf [n'p I M n'p] family.
 . . . .ag [-k l I N naf(a)] navel.
Inaft [npt l I = M, N ......
```


## [2026-09-07T19:31:41.188Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '^nap\\|^nāp\\| nap \\[' NYB_vol2_glossary.txt | head -20; echo \"=== context\"; python3 -c \"\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor m in re.finditer(r'nap[ \\[]', t):\n    print(repr(t[m.start()-120:m.start()+400]))\n    print('---')\n\" | head -60"
}
```


### [2026-09-07T19:31:42.462Z] TOOL RESULT

```
2642:nap [npy] grandson HajB:4. ŠPrs:8. -
2645:napa ;
5237:napat-: nap
=== context
'[nng] disgrace 15°; ~ räd for shame (being ashamed) 693. 8415, Skr v. lajjü-hetoh. — = Paz. NP; MPrth nng ‘infamy’ (S).\nnap [npy] grandson HajB:4. ŠPrs:8. -\nNom. sg. *napä of Av. (1039) NP navah < *napak.\nnar [ZKL] male 11?. 94%; man 74!?. 921^, — Common Ir.\nnapa ;\nnarm [nlm] soft 472°. — V. also s. v. *a- namr-tom.\nNarsah [nrshy] n. pr. masc. P 1:7 (twice). — Av. (1054) Natryē.saņha-; MPrth nrysf- yzd; MPrs nrysh-yzd (A-H I); Arm Nerseh.\nnasäi [ns’y] corpse 6021. 727. 942%. — Av. (1057) nasu-, ace. nasāum, pl. nom'
---
'65. 7419, — Av. (892) parafa- ‘penalty’.\npuhré-puhr (Prth) [pwhrypwhr] grand- son HajA:4. SPrth:7, corresponding to Prs nap (q. v.). - V. puhr.\npurr [pwl; M’LH] full: ~ äp full of water 151; ~ tigr full of arrows 2013; 542-7.11, 581; often united with the follow- ing subst. so as to form a compound, from which an abstr. subst. may be derived: ~ Yarrah full of splendour 48?3: ~ avarrahēh 37°. 10619; ~-marg full of death 11719: ~-margéh 648; (—-xrat full of Wisdom): =-xratēh 90%; —-nerök full of power 50%; — before a'
---
```


## [2026-09-07T19:31:48.466Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n '1039\\|napāt\\|napat\\|Enkel' BRT.txt | head -30"
}
```


### [2026-09-07T19:31:48.524Z] TOOL RESULT

```
5619:'raAe  paiti  iamgnöfm'W.ig.^^i^y, —  'raAe\»].  'arSan- m.  EN.  eines  iranischen  Fürsten gtwaya  . .  yat  ahmya  äalva  kandvannti  ausder^ai'ix)'djTiastie,EnkelsdesÄijW(7/a'': "..wo  die  Ä  zusammenkommen"  V.J.  7.   -{■awa^»»    'srum  Yti^.71;  —  Aavöis  'Ins
7279:charakterisirenden  Adj.  (sd.,  auch  fdSt.): vispasca  äpS  yazamaide  ya  z)m3  armaesta (sd.)  *fratat.ear3tasca  (sd.)  *xqnyk  '^raots.- stälasca  par^uya  *v3iryäsca  (sd.)  "alle Wasser  auf  der  Erde  . , :  die  stehenden  und fliessenden,  die  in  Quellen  und  in  Fluss- laufen,  die  Schnee-  und  Regenwasser"  Y. 61^.6;  usw.;  —  vJspä  apd  xä  pttiti '^raotS.- stSiasca  Y.yi.g;  —  sps yal  armal^tayä.. yat  cätayä  uzuityäsca  .  .  yat  sna^ntyaica srasUntyaica  . . yat ß^tat.^antayä'W .  6.^0, 33i  36,  39;  —  äpim*  tacintqm  . .  xayanqm .  .  zrayanqm  .  .  artmaistqm  Yt.6.2;  Y.ig. 26,  Vd.4;  —  caval  nä  apa  (statt  DS.) ''frälat.cartte  .  .  paiti.iaräi  .  .  cval .  .  ape armaisfaya  (statt  DSf.)  .  .  nävayayai  tia ape  ..  ti.66(.;  —  apqm  ..  nävayaiiqm (sd.)  paiti  pintüs  Yt  //.  4 ;  usw.;  —  andvim . .  ye^he  avavat  .  .  äps  lata  (sd.)  ava.- barmle ya%ia  ..  Yt.5.15;  Ä.47; — gairil yS  uiiiä  yim  aiwiid  paoiris  äpS  hqm  gairi- ü(/('(sd.)/(WJ«/JYL/9.66; — spim  laokmta' vaitim  zaranyävaitlm  vihusavaifim  (sd.) V.^.54;  —  ap3mca  haomyqm  {sA.)  Y.  22. 2;  usw.;  — yaSsyatitim  äp^m  *pararihät Y.g.ii;F.4 f.,  V.21;  —  ?iqm.taptibyB  aiwyS caxrare(sii.)  n^r^bydY.  4.46; — apU  ai yaza- maide malkaintllcä  (sd.)  * hsbavaintlicä  . . Y.JÄ3«.  C)  GP.  apqm  mit  napat-m. (sd.,  auch  fdSt.)  Name  einer  Gottheit: apqm  napäs?  tä  apff  ..  vliax/aiti  YtS. $4; usw.  2)  von  bestimmten  Flüssen  oder Seen,  'Gewässer':  andvl  (sd.)  nqrna  äpa (NS.)"'  V.  7. 16;  —  n?mS  artduya  aps  anü- hitaya  Yt  r.  2 1 ;  Y.  6$.  i ,  Ny.  4.  o.  Vr.  1. 5 ; —  *atikäs^a  (näml.  artduyä)  mS *aaatiAä aps  apayiarsY .  65.  i;  5;  —  upa  äp.'myqm vltaaukaittm  Yt5,76;  —  njinB  ape  däit- yayä  (sd.)  Yt./.2i;  5.112,  5,29,  /7.61, V, ig.2;  —  aoi  apjm  yqm  raiakqm  (sd.) Yt.5. 63;  —  haca  apat  kqsaeyät  (sd.)  Yt ig.92,  V.ig.$;  —  a/s  ya  aw^änva  nqma Yt  ig.  62;  —  yazäi  äp^m  frazdänaom  F. 4%.  I,  2  Anhang:  apqm  (näml  ayar^y
8516:•  j.  'usan-  m.  EN,  eines  iranischen  Königs aus  der  KavayAyaasiit,  Enkels  des  Ka- z'äia'*:  tarn  yazata  aurvB  aLvar^B  kava °sa  prpzi/yäl  paiti  garSii  Yt,5.45;  14-39', —  a/.var>äl  ya'^a  kava  'sa  Az.  2.
10042:'aufziehen,  grossziehen':  bis  hapta  pui^rqm ga'iwqm  «i/(7MJ/V"'""zweimalsiebcn junge Hunde  soll  er  gross  ziehen"  V.  14. 16.  2)  'heraufkommen  zu —,  erstehend sich  einstellen  bei  -';  a)  mit  Lok.:  Aya^ US  asa  naptyassu  naßuca  türahya  uzjSn (jSPr.^.)  '**  fryanahya  aoJyaisR  "wenn sich  das  Asa  bei  den  preislichen  Enkeln und  Nachkommen  des  Tlsrers  Fryana  ein- stellen wird"  Y..rf6".  12.  b)  mit  Dat.: US  na  aMbai  vTse  Jamyal  ahnica  xsa- ^mm^a..  Y.60.  2;  —  ta  iiö  ama  tä  v)r»- %rayna  ,  .  usjamyqn  ya  staota  yesnya  Y. i5-  3-  3)  'ausschlagen,  gereichen  zu  — '
10768:•  j.  xäa&r5.iiaptar-  m.  'Enkel  der  Herr- schaft, des  Reichs',  Beiwort  des  Nairy\- sanha:  "naförS  naiTyd,saT3hahe  Ny.  5. 6;  —  xlahrsm  na/^r»m''>  nairyS.sarAgm yazaUm  Y.  77. 1 1.
13154:—  apqm  napattm  .  ,  yB  n»rSus  daoa  yB mrSus  tatasa  Ytig.  52.         c)  insbes.  von
16411:•  j.   pisinah-   m.   EN.   eines   iranischen  |     KompE.  — Zum  v./fl?j.,eig. 'Färbung,  Farbe'; Fürsten  aus  der  A'af fly-Dynastie,  Enkels      vgl.  ai-  ''«™°- m-  -  np.  __vgU  >™  'Hand-
17403:•  j.  by'arSan-  m.  EN.  eines  iranischen Fürsten  aus  der  /Tui/aK-Dynastie,  Enkels des  Kaväta'^:  kavaim  'lamm  Yt7p.7r; —  kavSil  "Sans  (GS.)  asaoms  Yt.  13. 132.
18541:•  ).,  g.,  p.  naplt-:ffa//-  m.,  j.  naptar-: nafsir-  m.",  j.  naptl-  f.  'Enkel;  Enkelin': '  adam  d3ray^v(^ui . .  vistäspahya  puh^e^ arSätnakyä  '/J(NS.)'*  Eh.  j.  i;  —  'pS (NS.)"  ..  ■■//("  (NSf.)  i/a  V./2.11;  10;  — nyaka  haca  'ptöisSs,  (^\%y^  nyske  haca  'pti (statt  AblSf.)  V.  J2. 1 1 ;  —  hyai  us  alä napiyaisii  na/i'uCLP.yVä ..uzp//  (Sp.4gSm.)  ' fryänakya  aojyaiiü  '^.46.12.  a)  mit GP.  apam''  'Enkel  derWasser',  Name  einer Gottheit**;  a  dim  (näml.  3^ar)nö)  Hahra kangturvayat  apum  'ph  (NS.)  aun'at.aspö Yt.  rp.  s  1 ;  5 '".  '.7-  95^';  —  «/>?'»  >'»  (NS.) t&  ups  ,  .  aiiuhe  .  .  vi.baxsaiti  Yt  8.  34; —  b^ntantfm  ahuntn  xsa^rlm  xSaltitn apqm  'pättm  aurvat.asp?m  .  .  yB  upäpB yazatS  Yt  ig.  51 ;  Y.  2,  5;  —  apqm  'ptär?m yasamaide  nairJm  sanh^m  Y.  7/.  23;  — b»->sat3  ahurake  'fiorS  aPqm  apasca  maida- la/aya  Y.  r.  5;  —  b^ryza  a/iura  xsa^rya apqm  V»?(VS.)Y.6'5.ia.  _  a)Nameeiner jener  Gottheit  geweihten  Örtlichkeit*'  (oder eines  Husses,  einer  Quelle,  eines  Berges): tarn  (näml.  andriin)  yaznäa  . .  sSyuidrSis pu%ra  upa  b3r?zant?m  ahur>m  xsairim xsaWm  apqm  'paism  Ylj.  73.  [na/jonm Y. ij.ii:  s.  x/alirB.napiar-.\
18571:Ar.  'iiahAä-naaiisIlia-  eig.  'der  der  Familie, Verwandtschaft  nächtt  stehende*.  Ar.  'nahhä. f.  'Nabel;  Familie';  ahd.  naba  'Nabe',  letl. naba  'Nabel';  vgl.  näfa-  m.;  Richter  1F.  p. 309.  —  ai.  näö/iSafdiitha-n  m.  EN.  (Ableit. ans  ar.  'naih').  —  Pü. ;  nabänaiiHsl  (Transskr.), SQ.:  ncaänvävanikaläh  'novem  familise  pro- pinqui'»).  —  ')  nahlf  (BB.  12.  105}  eiistirt nicht.  —  »)  Nach  V,  13.  i  ff.  wären  das: l)£hem,  2)Kinder,  3)  Geschwister.  4)  Gross- eitcm.  5)  Enkelkinder,  6)  Kinder  der  Ge- schwister, 7)  Geschwister  der  Eltern,  8  und 9)  deren  Kinder  und  Enkelkinder.  Vgl.  nava- naplya:
```


## [2026-09-07T19:32:01.571Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npos=sum(len(l)+1 for l in lines[:18540]); leaf=t[:pos].count('\\f'); print('leaf',leaf)\npages=t.split('\\f')\nimport re\nprint(re.findall(r'10[2-5][0-9]', pages[leaf])[:20])\nprint(pages[leaf][:400])\n\""
}
```


### [2026-09-07T19:32:02.910Z] TOOL RESULT

```
leaf 580
['1040']
dg.  'netfn»'),  dafür  'na^ami^a mit  analogischem  m  (nach  dem  Zw.  für  7, 10} wie  im  Ordinale.  —  Pü.;  9  bar.  —  >)  So  Jp  1,
Mfa;  NA.  näumayäiU.
•  g.  nadant-  Adj.  'schmähend,  lästernd': ys  hwat  masäa  asrustlm  aktmiä  mans yasSi  (sd.)  apä  .  .  airyamanasSl  'dittis  .  .
'. .  und  von  dem  Sodalen  die  Lästerer  . ."
Y.^.4-
PP2A.  einer  ar.  Basis  *nW-;  Tgl.  ai
```


## [2026-09-07T19:32:07.092Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'nawa\\|nawāda\\|nawāsa\\|Enkel' HRN.txt | head -25"
}
```


### [2026-09-07T19:32:07.138Z] TOOL RESULT

```
4134:*syr. |W':51l^tDN (wie Fraenkel, Fremdwörter, S. 291
5412:605. ran 'Schenkel'.
5413:aw. räna- 'Schenkel'; phlv. ran^ ränpün, arm. LW.
6898:789. sei 'Schenkel', seieng (Sileng) ; vergl. selvär 'Hosen*.
8908:nehire "Enkel' siehe unter newade (No. 1047).
9069:1047. newäde ^Enkel*, newäse, newa (vergl. newäzade),
9071:ap. napat' 'Enkel'; aw. napat-; ai. ndpat^.
9072:kurd. nevT, nevü^ nehvö 'Enkel*; afy. LW. nwasai;
9073:bei. LW. nawasay (255) ; wa/. napüs^ sar. nabüs, §iyn.
10588:Dasselbe gilt für lia/t 'Schenkel' (vd. 8 (184), Zend-
10590:'Schenkel', oss. t. ayd 'Lende' (7).
```


## [2026-09-07T19:32:11.421Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9065,9085p' HRN.txt; echo \"=== leaf\"; python3 -c \"\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npos=sum(len(l)+1 for l in lines[:9068]); leaf=t[:pos].count('\\f'); print('leaf',leaf,'printed=',leaf-21)\n\"; echo \"=== nabas?\"; grep -n -i 'nabas\\|nebīre\\|nabīre\\|nabas' HRN.txt | head"
}
```


### [2026-09-07T19:32:12.747Z] TOOL RESULT

```
1046. neva^terij tiuvä/ten *singen; schmeicheln', Praes.
neva^-entj neväzis,
ni -+ l/"£?öfc-, im Indischen reden, sprechen;
schmähen'.
1047. newäde ^Enkel*, newäse, newa (vergl. newäzade),
neblre, nehtr (Öähn. I, 119 Vers 995^)).
ap. napat' 'Enkel'; aw. napat-; ai. ndpat^.
kurd. nevT, nevü^ nehvö 'Enkel*; afy. LW. nwasai;
bei. LW. nawasay (255) ; wa/. napüs^ sar. nabüs, §iyn.
naböSj nebös.
Gegen Leumann's Etymologie von indog. nepöt-,
neptf' als *Waise* (Festgruss an 0. von Böhtlingk,
S. 77) spricht sich z. B. Delbrück, Verwandtschaf tsn.
125 folg. aus; dafür von Bradke, GGA. 1890, S. 909.
1048. nuväzdeh 'neunzehn*.
aw. navadasa- neunzehnter; phlv. naväcdahum^);
ai. ndvadasa 'neunzehn .
^) Vullers s. v. Kaku hat aus dem FS sinnlos benesre,
2) VerKl. Seite 128 Note 6.— 235 —
kurd. LW. nözdeh neben dauneh; af/. nülas, nütias;
o»s. d. nätidäs, t. nudäs (205).
=== leaf
leaf 255 printed= 234
=== nabas?
```


## [2026-09-07T19:32:24.866Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && ls; echo ===; grep -n 'نبسه\\|نَبَسه\\|نبس\\b' BQT_v4_pages.txt | head -20"
}
```


### [2026-09-07T19:32:24.906Z] TOOL RESULT

```
Exit code 1
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
(eval):1: == not found
```


## [2026-09-07T19:32:28.319Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n 'نبسه' BQT_v4_pages.txt | head -20; echo \"-- nabire\"; grep -n 'نبیره' BQT_v4_pages.txt | head -10; echo \"-- nave\"; grep -n 'نواده\\|نواسه' BQT_v4_pages.txt | head -10"
}
```


### [2026-09-07T19:32:28.428Z] TOOL RESULT

```
-- nabire
7312:لاف , تافه » نواده » نبیر » نبیره « بشتها ۲ ص ‎0٩‏ ح > ؛ قن : نواده , نیین » لبیره .
8016:درعربی » پیشمین و رمول راکوبند ۲ ؛ وبمعنی نبیره ‎٩‏ * بروزن صغیره» بمعنی فرزند
8046:8 - رك4 : نبیره و رك : اسشق ۱*۶۷ بنقل از شاهنامه ] ۰ بیت ۰۹۹۰ ۰
8049:4 بمعتی فرزند زاده ) که از آن 381 ( کتینه‌های ساسالی ) و نبیره ( فارسی ) ساخته
10344:تاریخ بیپقی جص۸۹۲) : « اما نوا بمعنی * نبیره وفرزند زاده ونوه » تردیدی نیت که كلمهٌ
10401:کرفته و « توا» را بمعنی نبیره و وه آورده , و پا اینکه در جایی‌کانبی بخطا «نواده» را * نوا »
10502:فری ص ۵*۵ وقس : نبیره » نوه» نواده. هوبشمان گوید : فارسی 112۷28-8 ازحالت مقعول
10744:نبیره باشه که‌فرزند زاده است ۴ - وبمعنی‌فرزند | آسپهود است که نفس ناطقه باشد .
11665:سقنقور , پممنی لبیرةفرزندباشد که فرزندفرژند وه - بفتح اول وثانی » نبیره است که
11688:اول و باه مشدد ) > * اقرب‌الموارد » . ۸ - همربشه نواده » نبیره (۸م.) .کردی 26۷1
-- nave
6539:رك : دکترصفا. حماسه سرائی ص ۵44 ببعد - و این مهرداد پسر وان ( چضم اول ودوم ) و نواده
7308:(بان , خانواده) « لیب ر که ص ۱۵۳ , پپلوی 22 (ناف) , اففانی80 ۰ 32018 ۰ استی ]۰32
7312:لاف , تافه » نواده » نبیر » نبیره « بشتها ۲ ص ‎0٩‏ ح > ؛ قن : نواده , نیین » لبیره .
7967:۷ "یه (وم.) * نواسه (ه.م.) س نواسی ۳ یه « سيك شناسی ج ۲ص ۷۹+
7968:رك : نواده .
7971:۸ یی (هم.) اه نواسه 38۷282 ( در خراسان متعمل امت ) ( فرزند وه )
7972:« فرهنگه نظام »۳ نواسی ۳ لیسه . رك : نواده ‏
8050:شده «وارمتتر. تبه‌ات اج ۱ اس ۱۱4 [رك : نواده (شرح داوه شده) . نوه ,لاف ] در خراسان
8052:( فرزند نواده ) ‎٩‏ مکی نراد *:
8058:‏۷ ظ. مصحف «نبهره» (ه.م.) ۸ نواسه (هم.) ** نوابیی ‏ پنه ‎٩‏ سبك شناسی
```


## [2026-09-07T19:32:34.606Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && head -3 BQT_v4_pages.txt.pages; echo ===; grep -n 'pdf page' BQT_v4_pages.txt | head -3; echo ===; python3 -c \"\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (8016,8046,8049,10344,10401,10502,11665,11688,7967,7971,8050):\n    pos=sum(len(l)+1 for l in lines[:ln-1]); leaf=t[:pos].count('\\f')\n    print(ln,'leaf',leaf,'printed~',leaf+1917)\n\""
}
```


### [2026-09-07T19:32:35.913Z] TOOL RESULT

```
Exit code 1
head: error reading 'BQT_v4_pages.txt.pages': Is a directory
(eval):1: == not found
```


## [2026-09-07T19:32:39.669Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 -c \"\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (8016,8046,8049,10344,10401,10502,11665,11688,7967,7971,8050,7312):\n    pos=sum(len(l)+1 for l in lines[:ln-1]); leaf=t[:pos].count('\\f')\n    print(ln,'leaf',leaf,'printed~',leaf+1917)\n\""
}
```


### [2026-09-07T19:32:41.003Z] TOOL RESULT

```
8016 leaf 199 printed~ 2116
8046 leaf 199 printed~ 2116
8049 leaf 199 printed~ 2116
10344 leaf 258 printed~ 2175
10401 leaf 259 printed~ 2176
10502 leaf 261 printed~ 2178
11665 leaf 290 printed~ 2207
11688 leaf 290 printed~ 2207
7967 leaf 197 printed~ 2114
7971 leaf 197 printed~ 2114
8050 leaf 199 printed~ 2116
7312 leaf 182 printed~ 2099
```


## [2026-09-07T19:32:53.823Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 -c \"\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (289,290,291):\n    print('=== leaf',i,'printed~',i+1917)\n    print(pages[i][:4000])\n\""
}
```


### [2026-09-07T19:32:55.231Z] TOOL RESULT

```
=== leaf 289 printed~ 2206
[pdf page 290]
سم بوند
وماهی باشد9 - ونام شهری ومدینه‌ای‌هممت ۳ | رونده ولیزرو باشد قنوماً - واسب سر یزرو
- وباسطلاح آرپاب معما ایرو راکویند که عریان ۱ دا اکوبند خصوساً - ویلش وغاطروخی رآورندم 9
حلاص خاش و مردم تیز فهم راهم میگوبند ۴ - و نام مکالی
قموهه 7 اس ت که آنشکدة برزین درآنجا بود ‎٩‏ - ونم
تولف" - بروزن سمند » اسب‌راکویند | کوهی هم هست ۷ - و نام مبارزی بوده ایرانی
مطلفاً وبمربی فری خوانند۴ - وبمطتی هر تیز | که پسراوفن‌هاد نام داشته - وسیند را لی زکوبند
۱- (عر) « نون بالضم . ماهی . لینان بالکر والوان جمع - و لسمت - و دوات و در
بعض تفاسیر ان والقلمآورده‌اند - وتیزی تیخ - و نام شمشیری مربعش عرب را . سمی‌لکوده علی
مثال سمكة - و ذوالنون لقب بونی علیه‌اللام - ولقب شمشیری دیگر - و لقب زاهد مصری ‎ -‏
‏ولیزلون حرفی از حروف معجمه ... » « منتهی‌الارب ». ۴ - دام کوهی‌است درعربستان ۰
که دهرالمپجم ازآن جاری شود « تخبةالدهر س ۰۱۱۵ و فهرست آن >.
۴ نونده (ه.م.) ۴ - « نوند و نونده اسپ باشد . رود کی گفت :
روزجستن تازبانی چون نوند روز دن چون شت‌ماله سودمند.»
« لفت فری چاپ هرن ص۲۹*.
در لفت فری چاپ‌آقای اقبال س ‎۹٩‏ بیت فوق برای معنی « ييك وخبرگیر» شاهدآمده .
رسیدند برتازبان ( تازیانی ) لوند بجایی که پزدان پرستان بدد .
فردوسی طوسی « شاهنامةٌ بخ ج۱ اص*6 » ورك: صحاح‌الفرسی (نسشه آقای طاعتی)
پیاورد فرزند را چون لوند چو غرم ژبان سوی کوه بلند -
فردوسی طوسی « شاهنامةٌ بخ ج۱ ص 4۲ >
کلك سبك سیراوست ازیی اسلاح ملك از حبشه سوی روم نیز رونیم لول +
منوب برودکی بنقل صحاح الفری ( درمعتی اسب ) « فرهنگه نظام » ونیز نسشهٌ آقای طاعتی و
همکن‌است بمعنی پيك و خبر آورنده باشد . 8 ر4 : فولده . ‎۹٩‏ - + بوند » در
شاهنامه نام شهر « فپرست ولف > و موضمی است . فردوسی در شاهنامه درضوان « داستان‌جنگه
هفت کردان » کوید ( خاهنامة بخ ج ۷ ص ۸۱۹ ) :
غنیدم که روزی گو پیلتن یکی سورکرد از در انجمن.
بجایی کجا نام او ید «لوند» بدو ,انسرون کاخپای بلنده
کجا آنر برز برزی نکنون بدان‌جافروزدهمی رهنمون...
و ظ . «نوند» مصحف « ریوند (کوه) » است . بنا بتصرج تفیر پهلوی آتش لیایشءاین‌آتشکده
در ریوند ایالت خراسان جای داشت : « جای آنر برزین مهر درکوه ربوند است .کارآفر برزین
مه ر کشاورزی ( واستربوشی ) است . از باوری این آتش است که کشاورزان ازکار کشاورزی دالاتر
وتخشاتر و پاکیزه‌نر ( شستك جامك‌تز ) هستند » و با این آتش بود که گشتاسب پرسش و پاسخ
کرد .> « خرده اوستا سس ۱۲۲ ح > . کریتنشن نوید ( ساسان [ ترجمه ] صن ۱*۸ ‎٩‏ ) 5
« لازار فاریی .813872 16 1.8287 قربهٌ ربوند را ۶ قربهٌ مفان » مینامد . باعتقاد چکسن مکان
این‌آنشکده در ۵ قربهٌ مهر > بوده است که در سر راء خراسان بيك فاصله از میاندشت و سبزوار
قرار دارد .» رك : مزدیستا ص ۰۲۱۷-۲۱۹ ۷ - ر4 : حاعیهٌ قبل .

=== leaf 290 printed~ 2207
[pdf page 291]
توسول دنا
وآن‌تخمی است که‌بجهت دفع‌چع‌زخم‌سوزند۱ - | همهت ‎+٩‏
‏وبممنی صدا وآواز بلند هم آمده است . و۷ - باهمزه دربالای واو پروزن‌سبوه
نو ندول؟ بالام در آخر بروزن | خرمای تروتازه راکوبند .
سقنقور , پممنی لبیرةفرزندباشد که فرزندفرژند وه - بفتح اول وثانی » نبیره است که
زاده‌است عموماً - ویسرپسرزادرا کویند خصوصاً. | فرزندزاده باشد۸ - وبعندی‌عرچیز نورا گوبند۹_
نوندم. بروزن رونده, بممنی اسب‌چلد | وبمعنی حادث هم هست که دریرابرقدیم‌است*۱-
وتند وتیز۴ - وهرچیزتیزدونده ۴ (۱)- ومردم | و یشم اول بر وزن کوه » بمعنی نه باشد که
نیزفیم ۴ - ونغم مپندباشد؟۴ - وبممنیخر کت | بعریی تمه کوبند۱۹ -
کننده8 - وفربادزنده* - ولرزنده8 هم‌آمده نوی - بکسراول وئانی بتختانیمجهول
است . کنیده » کلام‌خدا ومصحف وقر آن‌مجیدباشد۱۳»
نو‌نیاز» با تستای بالف کدیده بروزن | وبضم اول » نیز بان معتی آمده است . و بفتح
سرو نازه شخصی راکویند که تازه بعرصه آمده | اول » بمعنی تجدید و تازکی باشد ۱۴ - و
باشد(۲)-وسالكمبتد برانیز کفته‌اند_وتفیرمبتدی | بمعنی زاری کنی وبلرزی و لرزان شوی وبجنبی
۱ ( خم۱: رونده . (۷) چك : بعرصه‌آمده مت ؛ چش : رصه درآمده باشد.
۱- از پی‌چشم زخم خوش صنمی خوبشتن را بسوز همچو لوند .
سنائی غزئوی « جهانگیری >.
۴ -قی : اصفهانی عامیانه « لونگان » ( پمر پرزاده ) « فرهنگه نظام >.
۴ -ارك : لوند . ۴ - « نونده » تیز فهم بود . پوسف عروضی گوید :
هیچ مبین سوی او بچشم حقارت زانکه یکی جلد کربزاست ونونده...
2 لغت قری سس 4۷۵ >.
ها اسم فاعل از « نویدن > (ه.م.)
‎٩‏ - ابجد مشق مجاز از تو لیازان خوش نماست
یس کشتی واگذار این بازی طفلانه را -
صائّب تبریزی * بهار عجم > .
و لیاز بممنی شوق است « فرهنگه نظام > ۷ - (عر) «النواة » عجمةالتمر ولحوهای حبه
. لو بزر ج نوی و نویات » وجمع‌النوی انواه و نوی ( بکسر اول ودوم و باه مشدد ) ولوی ( بفتح
اول و باه مشدد ) > * اقرب‌الموارد » . ۸ - همربشه نواده » نبیره (۸م.) .کردی 26۷1
( فرزند زاده ( پس) ) ؛ 22۷1 « ژاباص 24۲۵ * » ساسکریت و پارسی باستان 2221 ۰ اوستا
4 » 2202 ( ناف ) ۰ لانینی 36808 ۶ بشتها ۷ اس ۹و جح ۰۱ ‎٩‏ -رك : لو
*- از دساتین « فرهنگه دساتیر صس ۲۷۱ >. ۹۱اه (وم.)
۴ بی (هم) :
تا در نوی ودرقصص آیید که ابرهه درکفر لشکری سوی ببت‌الحرم کشید.
بادی چنانکه غاشِةٌ نو کشد ذلك دایم چنانکه اد همی تخت جم کشید .
عبدالواسم جیلی ( از سفینه‌ای ).
۴ از : وی ( حاصل مصدر » اسم معتی ) :
دبریت‌کاین بزرکی درخاندان اوست این می‌تبه نیافت کنون خواجه ازلوی
« فرخی سیستانی ص 8*۳ ۰۶

=== leaf 291 printed~ 2208
[pdf page 292]
۱۹ بریدن
ومتحرك شوی هم هست ۰۱ کوید , پعنی بلرزد وبنالد ونوحه کند ۴ - وبا
وان - بروزن کوبان » پادشاهزادمرا ثالی مجهول بروزن امید » عژده و هژژدکالی و
کوبند , وترکان ملوك و سلاطین را بدین انم | خبرخوش‌وهرچیز که‌سبب‌خوشحالی‌شوده وبشارت
خوانند؟ - وسبدی با طبفی را نیز کوبند که از دادن بضیافت ومهمانی وامیدوار کردانیدن‌ووعده
چوب بیدا بافته باشند . کردن بخغدمات دیوانی وکارهای بز رکه با نقع
۱ نویچ - بفتحاول‌وثانی بتحتا بیمجهول و ۱ ۹ ی متحرك ولرزان غد ولوزید
کشیدوبجيم فارسی‌زده, کیاهیاست که بردرخت 8 نویدن - بروزن دوبدن » بممتی‌زاری
پیچد وعربان لبلاب وعشقه کویند . کردن ونالیدن باشد۹ - وبممتی حر کت کردن
وید - بنم اول وتانی مجهول بر وزن | وجنبیدن ولرزیدن هم‌آمده است۷ .
۱ - رك : نویدن. ۴ # نوبین * نوین (مغولی) «رشیدی » « شموری » «عموماً
پادشاء اما خصوصاً خطاب سلاطین ترکان است > فرهنگه اظفری بتقل « فرهنگه نظام »4«نوبین »
نوبان » فرمانده سپاه . آمیر » نجیب > * جفتایی ۰۵۱۱ ۴ - « نویج بروزن عریج ولوج
بروزن عوج » اسم لبلاب معروف به عشقه است .» « محیط اعظم > + ۴ - رك : دوبدن .
- ۸0۷60 از : ۰۷2۵4-۲۴۵ قی اوستا 81۷26052600 « اسدق 4۱*۵۳
هوبشمان گوید : 813۷8 ( خبرخوش ) را ۳۳.۷/1116۲,۷۷2:1۳۸/.8,98 همريشهٌ آرمنی ع
7 (تقدم, فدیه. قربانی). ازپهلوی 281۷80613 میداند که‌به کلمه اوستایی 81۷860486701
(من خبر میکتم).مربوط است » بنابرین می‌باست درفارسی‌جدید 2810۷81 آمده باشدهعوبشمان
۴۳ کردی 860 ( امر » سفارش ) « ژابا ص2۲۷ >. كلمةٌ نوید را مرکب از پیشودد -81
+۷264 (7 کاهانیدن » بغارت دادن ) داسته‌اند « نا ص۱۱۵ ح۱ ». سبزواری 26۷16
( مژدکای ) « فرهنکه نظام » ۶ نوید . چنان باشد که کسی‌را بامید کنند . رود,کی (سمرقندی)
کوید :
اگر امیر جهاندار داد من ندهد چهارساله نوید مراکه هست خراب (خرام.دهشدا).
« لفت فری ص ۱۱۷ ۰۴
‎٩‏ - هرن کوید : 2811068 ( شکایت کردن ) ( شاهنامه 1 ۰ ۱۸۳بیت ۹۸۹ ؛کلکته).
نوا 86۷2 ( شکایت ) ۰ 360۷1068 . هندی باستان ۳۵۷ , 2801 ۰ 24۷816 ( غریدن
[ جانوران ]) ۰ قس : فارسی : زنودن « اسشق ۱۶۵۶ .
ز درد دل آن شب بدان سان نوید کم از ناله‌اش , هیچکی فنوید .
لبیبی « رشیدی ؟ .
ً اکنون زمفلسی چه نوی چندین بر درده‌اتی و اغم مغبولی ؟
ناصر خرء بلخی ص 2۷4 *.
و رك : نوان .
۴ - تو ازم ن کنون داستانی شنو بدین داستان بیشتر زین مئو .
پوشکور (بلخی) «لفت فرس ص4۱۷
آپری کز او کوهر بود » با دست او بر خود نود
باشد خجل کزچه بود هر دو جهاش يك خطا .
جمال‌الدین آشهری . « فرهنگه نظام؟.
```


## [2026-09-07T19:33:07.237Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 -c \"\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (198,199):\n    print('=== leaf',i)\n    print(pages[i][:4500])\n\""
}
```


### [2026-09-07T19:33:08.524Z] TOOL RESULT

```
=== leaf 198
[pdf page 199]
بعلد 1 -۲۱۱۹-
شلف - بنتح اول و نانی وسکون شین | موضع تهمت وارتکاب فواحش .
نقطه‌دار ولام مفتوح ودال ساکن ».یعنی نه‌چنید نبهره ۴ بفتح اول و ثانی و سکون
چه بعلیدن بممنی چبیدن باشد ۱ ۰ های هوزورای قرشت مفتوح. بممنی قلب وناسره
نيك ۲ بفتح آول وسکون ثالی‌وکاف» باشد عموماً 8 - وسیم قلب را کوبندخضوضاً ‎٩‏
‏زهاب راکوبند وآن تراویدن آب باشد ا زکنار - ویمعنی‌دون وفرومایه‌هم آمده است؟۴ -ویمعتی
چشمه ورودخانه . اول نابغره باشد که بز رکه و عظیم است ۷ -
فیناك ۴ - بر وزن فرهاد . بسسنی طلق | و بمعنی پوشیده وپنهان هم کفته‌اند ۸ .
نفی است وآن آزاد بوذن وخذر کردن باشد از نی - بنم اول وئانی بتختانی اشیده .
۱ در : بعلیدن . ۰-۴ نك , زه آب (رهآب . دهغدا) بود.. رودکی
( سمرقندی ) کوید :
کیردی آب جوی رز پندام چون بود بسته لك راه ز خی. »
« لفت فرس ص ۳۰۹ ۰*۱۶
۴ -ظ . برساخته فرقة آذرکیوان . ۴ - معرب‌آن * ببهرغ » و مخفف آن
« بهرج > . بیروتی در الجماهن ( ص ۸-۱۵۷ ) گوید: « درحدیت حجاج آءد که وی ببعض عمال
خویش نوشت : ان ابمت الینا بالجشیر اللولژانی الجراب تبهرج به ۰ وبهرج نزدکسانی که آنرا از
فارسی تعریب کرده‌اند » ردیء ( پت ) است . ولفظ در اصل منقول ازهندی‌است و جید (نیکو)
را « بهله » بباهگوبندوردیء ( پت )را * نبهله ». وهمچنین درفارسی« بپله > ببایی که درتعریب
فاءکردد »کوبند ؛ چنانکه بهترین زبانهای آنان - پهلوی - موب بجودت است . و درهمهای
یت را نبهر هگوبند ...> شاید از : ۱ (اشی » لب )+ بهره (۳ 027316 ۰ 82۳88 پپلوی
بمعنی پول . رشوه » پول رایج ‎)٩(‏ ) ۳ نیپ رکه * بهرج (معرب)؛ رك: بعش فواید لغوي کتاب
الجماهر بیرولی بقلم نگارندء در 1۶۵8 . ۷۵10826 0070180670072010 817۵71 - ا۸
+ - 238 .0 ,ا195 ۲100118 .رازه5
8 - کر خاط تو تیره بوطیمت نبهره است هم‌آب تست روشن وهم سیم تو سره
کمال اسماعل اصقهانی « قرهنگه نظام > .
۹ - وجه قلب :
که دارد: در هنه آقاق زهره که عرضه دارد این نقد نبهره ‎٩‏
‏: عطار لیشاپوری « فرهنگه نظام >
۷ - جهانگیری نبهره ۳ نابهره را بدین معنی نوشته و این بیت را شاهدآورده :
از آنجا پی رو (پی رو) جاسوس ره شد نبهره بر اسر چندین سپه شد .
نزاری فهستانی .
و مولف فرهنکه نظام نویسد : ازظاهرشعرمعنی پنهان «نهوم میشود. درحاشيةٌ تاریخ بیهقی مصحح
دکترفیاض همین‌بیت را بهمینءمنی‌شاهدآوزده شده است.  ‎٩-۸‏ ( محمود غزاوی ) بروزگار
جوانی که بهرات میبود و پنهان از پدر شراب میخورد » پوشیده ازریحان خادم فرودسرای خلوتها
میکرد و مطربان میداشت مرد و زن که ایشانرا از راههای نبهره نزديك وی بردندی ‎«٩».‏ تاریش
ببهقی مصحح دکتر فیاضش ص ۹

=== leaf 199
[pdf page 200]
۳-۱۷ یه
کلام خدا وقرآن ومصحف باشد ‎٩‏ - وبفتح اول گوبند ءعموماً .
درعربی » پیشمین و رمول راکوبند ۲ ؛ وبمعنی نبیره ‎٩‏ * بروزن صغیره» بمعنی فرزند
اول پا پای فارسی هم‌آمده است ؛ ویکسراول | زاده باشد عموماً - ویسرزاده راگویند خصوصاً ؛
گفته‌اند ۰ و بسی دخترزاده را هم کفته‌اند ؛ و بسنی دیگر
بیش - بنم اول وتختانیمجهول ‏ بروزن | پر پسی ویس دختر را میگوبند - وبمعنی‌خفیه
و معنی وید است که مدکالی و خبر خوش | و پنهان هم بنظر آمده است۷ .
اند ۴ و پنت‌اود: در عربی شراب خرسا زا | فیهه 8 م پروزن هریبه . فرژید زاده
کویند ۴ . راکویند که از الب پس باشد .
یس یهرز * + بر وزن صغیر» فرزند زاده را

- پهلوی 21۳08 [ تسنیا ( بوشته, نامه. ادبیات ) ۲۸وتوالا ۷۱ *. هرن نیز
#طا با ترا باسناد ص6 دوز ان کل اه #زل اعصدنه طعما< ,صصقصء‌ادگ
7 1 61 ۸1 ,۷6۲96 ازروشة ۸« نوشتن » میداند «اسشق ۱۰۵۱ ولی «هوپشمان۱*۵۱*
مینوید : نوی * نبی لمیتواند باین ريشه متعلق باشد. مولف فرهنکه نظام این کلمه را* یی *
بکس نون وبای فارسی ضبط کرده است : 8
رم دار آواز براندان چو آسان زافکه حق الکرالاصوات خواند اندر تبی صوت‌الحمیر.

سنائی غزئوی « دبوان ص ۲۸۱ ۶ .

۴ - (عر) « نبیء کامیر . پیغامبر از جانب خدای تعالی ... » « منتهی‌الارب » +

۳ *نوید (هم.). رك : جهالگیری - ان < ببیدٌ. پارسی باستان 81۳0118 ۵
( مغروب ) » قی : پارسی باستان -8168 و غیره ۶ اسشق ۱*۲۵ 019 > (عر) ۸« لبیذ کامیر » از
دست انداخته . و بکنی وآب افشرده که از حبوب و جزآن گیرند » * منشهی الارب > ۸ الفِیذ »
الملقی‌و-ما نب من عسیر ولحوه سمی به لانه ینب ای بتک حتی بشتد ویلقی فی‌الجرة حتیربغلی.
ج : البذة » و فی‌التاج بقال للخمر المعتصر من العنب نبیذ. » « افرب‌الموارد > و رك : دزی چ
۲ ص ۹۳۵ :

بیار ساقی زرین لبید وسیمین کای بباده حرمت و قدر بهار نو بشنای .
منوچهری دامقالی ص 44 >

8 - رك4 : نبیره و رك : اسشق ۱*۶۷ بنقل از شاهنامه ] ۰ بیت ۰۹۹۰ ۰

‎٩‏ - بهلوی 801۳8 ( 38۷1۲81 ) ۸« باروچا س ۳۲۳ » از ريشهٌ 388 ( اوستایی
4 بمعتی فرزند زاده ) که از آن 381 ( کتینه‌های ساسالی ) و نبیره ( فارسی ) ساخته
شده «وارمتتر. تبه‌ات اج ۱ اس ۱۱4 [رك : نواده (شرح داوه شده) . نوه ,لاف ] در خراسان
8 (فرزد فرزند زاده ) ۸ فرهنکه نظام > «گنابادی »۰ ارال ( سلطان آباد) نیز731۳8
( فرزند نواده ) ‎٩‏ مکی نراد *:

‏ندیم بخت جوان باش نا بکام ومراد یره پر خویش را به پینی پیر.

‏« معزی لیشاپوری ص ۳۸۲ 4

‏۷ ظ. مصحف «نبهره» (ه.م.) ۸ نواسه (هم.) ** نوابیی ‏ پنه ‎٩‏ سبك شناسی

‏چ اس ۷۹ ببس (همم.) هه (وم.)
```


## [2026-09-07T19:33:22.713Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 -c \"\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (195,196,197):\n    print('=== leaf',i)\n    print(pages[i][:4000])\n\""
}
```


### [2026-09-07T19:33:23.985Z] TOOL RESULT

```
=== leaf 195
[pdf page 196]
دنه دای‌تر کی
ناهاری ۱ < بر وزن بازاری » چیزی | مطربان نوازند و بعربی مزمار خوانند - و کلو
اندك را کوبن د که کی در صباح بخورد . وحلقوم‌رایز کویند
ناهد - بر وزن زاهد . دختردارپتانرا -وبوقی که در سس
کویند ۴ - و مخقف ناهد هم هست که تاره | روز جنگه نوازند
زهره باشد ۴ . وآنرا فای‌دو ین بای
ناهده ۴ * بروزن ساجده , بمعنی‌اول خوانن د که نفیر برادر وچ كکرتا باشد ؛ و ی
ناهد است که دختر اریتان باشد .۱" کردا را کویند - ونام قلمه‌ای هم‌هست که مود
کر سمدسلمان درآن قلمه محبوی بوده *۱- وبمعتی
ناهی - بروزن ماهی,مخفف ناهیداست
ی رد ی ۲ ]| فغر ومباهات هم بنظر آمده است .
ک زهره باشد ۴ - و درعربی نهی و من نای‌انبان - نی‌آنبان است وآن انبانی
ی باشد که بريك سرآن پنجه وصل کرده‌اند وآن
ناهید * - بسکون دال , ستارة زهره پنجه سوراخی‌چند داریا ایو ند
راگوبند و مکان اوفلك سیم است و افلیم ینجم | ودر زیر بغل گیرند وخوانند ورقصند ونوازند.
بدوتعلق دارد - وکنایه از دختر رسیده باشد ‎٩‏ نایب تنگری ۱() بعنی قَائم‌مقام
- و نام مادر اسکندر ذوالفرئین هم هست ۷ . خدا , چه نالّب درعربی قائم مقام و تنکری در
ناهیده یفتح دال , بمعنی‌ناهیداست | ترکی خدا راکوبند ۰ وآن کنایه است ازخلیفه
که ستارهٌ زهره ۸ - ودختر رسیده باشد ‎٩‏ . و پادغاء -
ای * - بسکون تحتانی , نبی باش که نای‌تر کی - بنم تای فرشت. سورای
(۱) چك : ناب شگری , چش : تایب تنکری .

۱ از : تاهار (ه.م )ی (نبت) وآن لفة بمعنی چیزی است که برای ناشتا شکستن
ورفع گرسنگی خورند (رك : «رمزدنامه س۸)) ومجازاً بمعنی‌غذابی که در روز خورند (امروزه
در تداول بهار ۳ ناهار ) :

پامدادانت دهد وعده بشامی خوش غامگاهات دهد وعده بناهاری .

ناسر خرو بلخی ص 2۱۷».

؟ - (عر) « ناهد . زن برآمده پستان . ناهدة مثله - وشیر بیشه . > ۶ متعچی‌الارب ».

۴ رل اد ۴ درل دح 8 رل : اناهید .

- باین ممنی صحیح « ناهده » (عر ) است . رك : اج ۲ . ولی در بض اعلام امکنه
( ماند «پل دخبر» ) (فظ « دختر» آمده که محققانآ نرا بممنی‌ناهید (فرشته . ایزد) کرفته‌اند .

۷ - در شاهنامه هم مادر اسکندر و هم اسم دیگن «کتایون > - زن کشناسب و مادر
اسفندیار - است . رك : فهرست. ولف . ۸ - رك : ناهید - ۰

: ‏زك : نی « اسشق ص ۲۲۹ ۰ بعلوی 824 [/(88 ] « اونوالا ۳۳ > ۰ معرب‎ - ٩
‏نای ( فلوت ) ۸« دزی ج ۲ ص ۹۳۲ :۰۹۲ *- رك : دیوان ممود سند مصحح پاسمی‎
. ‏ی کد -کط‎

۹۱ رك : تنگری (ص ۲۲ ح ).

=== leaf 196
[pdf page 197]
ایچ : -۱۱۶-
راگوبند وآن سازی است معروف, وبسی کوبند | قعب خوانند - و بمعنی آب چکیدن هم بنظر
نایی است که در هنگام رزم وجنکه نوازند وآن آمده است چنانکه اگر گوبند « نایژه میکند»
با یر باشد باگرنای ‎٩‏ . مرادآن باش دکه‌آب میچکد 8 .

نایچ - بکرناك وسکون جیم‌فارسی, نایلوس ؟ - با لام بروزن پای بوی,
تایی باشد که مطربان نوازند ۳ . موسیفاررا گوبندو آن سازی باشد مشهوروممروف؛
نای رللین - نابی باشد که در روز و منفصل هم نوشته‌اند که نای لوس باشد بکس
جنگه نوازند ؛ وبستی گوبند نفیراست ؛ وبیرای | تختانی واین اسح است ؛ و باشین نقطه‌دارپروژن
گوبندکرها است . بازیوش هم بنظرآمده است و درست است چه در
فایژه ۴ - بکرناك وقح زای فارسی, و تبدیل می‌باند : ز
بممنی کل وکاء باشد - ولولهٌ ابریق ولو هرجیزی [ . ی - کون ال دقع میم
دیگررا نیز کوبند۴ - ونی‌میان خالی‌وماشوره‌ای و شین وکاف هردو ساکن . بممنی نای‌انبانات
که جولاهگان برآن رسمان پیچند برای بافتن وآن سازی باشد مشهور و معروف و آثرا ای
- وهرچویی ونی (۱) میان خالی را «م کفته اند مشکات هم میگوبند با در کاف۷ . #*
که ب رکه بر آن رسته و گرعها داشته باشد - تاییدن ۸ - بر وزن زاییدن » بمعنی
و همچنین چوب خوشة گندم را تیز(۲) و بعربی | فخی کردن ومباهات نمودن باشد ‏
(۷) خم۱: نیهی - () چش :۳ کویند .
۱ - فرومانده ز بس غوغای ترکان ز بانگه نای تر کی » نای ترکان .
نظامی کنجوی * کنجینه صس ۱۵۸ >
۴ - جهانگیری این بیتا بدون ذکر نام شاعر آورده :
هزار تاله زدم بی کل رخت در باغ بدرد دل که شنیدم فغالی از نایچ -

مولف فرهنگه نظام نوید : شمر استاداند نیت . احتمال این است که لفظ نایچه (نای كوچك )
راکه سابقاً بدون هاء ( نایچ ) مینوشتند اشتباه خوانده و درشمن بسته .

۴ - از :نای جژم(< چه . ولد تصفیر ) ۳ نایزه ه بایچه . رك : اسدق ص

۹ اس آخر .

۴ - تنم ز خون جگرکشته بود مالامال اگر نه نایره خون ز دیده بگشادی .
کمال اسماعیل اصفپانی « فرهنگه نظام > .
8 - در لغت فرس « نایزه . آب چکیدن بود . عنصری ( بلخی ) کوید :
نه از خواب و از خورد بودش مزه نه بگت از چشم او نایزه . >
: * لغت فرس اس ۵*۹ .۰
‎٩‏ - در جهانگیری ورشیدی « نای موی آمده وسراج اختمال میدخد « موس » مخقف
موسیقار باشد « فرهنگه نظام > . ۷ - در رشیدی بهمین صورت آمده » با شاهد ذیل:
باد بندی سرود نای مشكك بین که چون هرزمان آن بادبندی را زسر کیرد همی.
خرو ( دهلوی ) -
۸ - باین معنی در جهانگیری و رشیدی لیامده ولی در دساتیر آمده « فرهنگه دساتیر
س ۹۹ > ظ. مصحف « بالیدن » است .
ای موس - رك:تایلوی . (برهای قاطع ۲۹۷)

=== leaf 197
[pdf page 198]
بیان دویم
در نون با بای ابحد مشتمل بر شانزده لت
نباج ۱ « بر وزن رواج , بمعنی ابباغ | وکارزار باشد ۴ چه‌نبردگاه جنکه گاه راکویند
است و آن دو زن باشد که در نکاح که هرد | - ومردم شجاع ودلیر ودلاور را کفته‌اند ۵
امت . نبرده ۹ پروزن لکرده » بممنی‌دویم
نبارش ؟ - بنتع رای بی‌نقطه پروزن | نبرد است که شجاع ودلیر و دلاور باشد .
جفاکش . چوییرا کویند که در زین چوب سقف قبس ۴ « بفتح اوزوئانی بروزن هوی,
که شکته باشد نهند و بردبواری که مقرف بر دخترزاده را گویند ؛ و باین معنی با تشدید ثالی
افتادن باشد سب سازند . هم کفته‌اند .
با ۴ « با غین ضله‌دار بروزن‌طلاق, فیسه ۸ - بننح اول وئانی وثالث, بمعنی
بممنی نباج است وآن دوژن باشد که درنکاح يك نبی‌است که دخترزاده باشد ؛ و بعضی کویند پر
مردلد - ودختر پر است که لبیره خوانند ؛ وبعضی‌دیگر
نپرد- بفتح اول وثانی‌وسکون را ودال | دختر دختر راکوبند نه پردختررا ؛ وبا تشدید
بی لقطه » بمعنی کوشش وجنکه و حدال و رزم تالی هم کنته‌اند .48
۱-ر4: بباغ («م.) * انباغ (هم.) ۴ - انجمن‌آرا وجه تمبه‌ای برای‌آن آورده
است . بدانجا رجچوع شود ۰ ۴ *انباغ (م.) ورل4: نباج ‏ ۴ < ورد (هم.) وقید
آورد « اسشق ۰۱۶۲۵ پپلوی 81021 ( جنکه . نزاع ) » ایرانی‌باستان 02۳91۳1 (مبارزه
کردن ) « بارتولمه ۸۹۸ * ۰ ورك : لیب رک اس ۱۵۹ ؛ اسشق ۱۹۲۵ ؛ ورك : لبرده ۰ * لیرد »
کارزار باشد . فردومی (طومی )گفت :
فرامرز پیش پدر شد چو کرد به پیروزی روزکار نبرد .۶ « لغت فری ص۹۸ 2 +
8 - باین معنی « نبرده > (ه.م.) و نبردی ( رك :جح ‎٩‏ ) است .
‎٩‏ - از: برد (ه.م.) + ۰ ( پسوند بت و اتصاف ) : * رده ؛ مبارز بود . عنجدی
( مروزی ) گوید :
شاه ابوالقاسم پن تاصن دین آن ببردی ( نبرده . دهشدا ) ملك » لبرده سوار .>
« لغت فری سس ۸۷۹ .۰
۷ "یه (وم.) * نواسه (ه.م.) س نواسی ۳ یه « سيك شناسی ج ۲ص ۷۹+
رك : نواده .
صفت ذات او همین نه بس است که رسول خدای رایس امت .
امیرخرو دهلوی درمنقبت امام ین . * فرهنگه نظام * .
۸ یی (هم.) اه نواسه 38۷282 ( در خراسان متعمل امت ) ( فرزند وه )
« فرهنگه نظام »۳ نواسی ۳ لیسه . رك : نواده ‏
ای بتن تیره‌گر شریفی وکر دون نب کردولی و نبیر کردون ‏
۱ امیرخسرو دهلوی * فرهنگه نظام > -
لبشتی - ر4 : لوشتن .
```


## [2026-09-07T19:33:48.262Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD watkins nepot\"; grep -n -i 'nepot' AHD_watkins1985.txt | head -10; echo \"=== SKT\"; grep -n '^NEPHEW\\|^NIECE\\|^NEPOTISM' SKT.txt | head; echo \"=== HUB\"; grep -n -i 'nawa\\|napat\\|Enkel' HUB.txt | head -10"
}
```


### [2026-09-07T19:33:48.337Z] TOOL RESULT

```
=== AHD watkins nepot
781:nepot-. Grandson, nephew. Feminine *nepti-. Latin nepos, grandson, nephew, and neptis, granddaughter, niece: NEPHEW, NEPOTISM, NIECE. [Pok. nepdt- 764.] ner-1, Under, also on the left; hence, with an eastward orientation, north. Suffixed zero-grade form *nr-t(r)o- in Germanic *north-, north, in: a. Old English north, north: NORDIC, NORTH; NORMAN; b. Old English northerne, northern: NORTHERN; c. Middle Dutch nort, north: NorsE. Compare deks-. [Pok. 2. ner- 765.] ner-2, Also aner-. Man; basic sense ‘vigorous, vital, strong.” 1. Oldest root form *aner- (with prothetic vowel) in Greek anér (stem andr-, from zero-grade “anr-), man: ANDRO-, -ANDROUS, -ANDRY; PHILANDER. 2. Extended zero-grade form *(9)nrt- in Sanskrit nrtyati, he dances (“moves vigorously”): NAUTCH. 3. Referred by some to this root (as if “having human eyes”; dps, eye; see ok’-) but more likely of unknown origin is Greek anthropos, man (earliest Greek form anthrék”os): ANTHROPIC, AN- THROPO-; LYCANTHROPE, MISANTHROPE, PHILANTHROPY, THEANTHROPIC. [Pok. 1. ner-(t)- 765.]
1908:NEED nau-! NEEDLE (s)né- NEFARIOUS dhé-1, ne NEGATE ne NEGLECT leg-1, ne NEGLIGEE ne NEGOTIATE ne NEGRO negW-ro- NEIGHBOR bheue-, néhw-iz NEITHER kWo-, ne NEKTON sna- NEMATO- (s)né- NEMESIS nem- NEO- newo- NEOGAEA gé@ NEON newo- NEONATE gene- NEOPHYTE bheue- NEOTERIC newo- NEPENTHE kWent(h)-, ne NEPHELINE nebh- NEPHELOMETER nebh- NEPHEW nepdot- NEPHOLOGY nebh- NEPHRO- negWh-ro- NEPOTISM nepot- NEREID nere- NEREIS nere- NEREUS nere- NERITIC nere- NERVE (s)neou- NESCIENCE ne, skei- NESS nas-
1914:NIBBLE ken-2 NICE ne, skei- NICHE nizdo- NICKNAME aug-? NICTITATE kneigh- NIDDERING nei- NIDE_ nizdo- NIDIFY dhé-1, nizdo- NIDUS nizdo- NIECE nepot- NIELLO negW-ro- NIFLHEIM nebh-, tkei- NIGGARD_ ken-2 NIGH néhw-iz NIGHT nekw-t- NIGHTINGALE ghel-1 NIGHTMARE mer-2 NIGRESCENCE neg¥-ro- NIGRITUDE neg¥-ro- NIGROSINE negW-ro- NIHILISM ne NIHILITY ne
=== SKT
=== HUB
3619:schrift Z. 4), zu der np. nava = jiid. tat. newe 'Enkel'
3622:*napat'ak auf den ap. Ace. *napatam = zd. napatem;
3624:(vgl. zd. naptarem) zuriick. Daneben nahasa 'Enkel*
4202:anagah, phi. anakds ^unaware* Shk. 228; nar *6ranatapfer
4789:nabard *Kampf ' ^= p z. naward quarrel* Min. Gl. 143, phi.
6209:Shk. 232, phi. apatan, arm. anapat 'unbewohnt, wiist*; na-
6210:vdda 'Enkel' neben nabasa (oben p. 103) und nablra, ap.
6564:^) Zd. fs auch ^=- pis in nc^su aus *napfsu, loc. pi. von napat-.— 186 --
9452:skr. jhillika- (LW. oder onomatop. ?); sal 'Schenkel' (fur sal?
```


## [2026-09-07T19:33:49.873Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN grandson\"; grep -n 'GRANDSON\\|NEPHEW\\|GRANDFATHER' SYN.txt | head -10; echo \"=== WLD Bd2 nepot\"; grep -n -i 'nepot\\|nep6t\\|napat' incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-07T19:33:49.937Z] TOOL RESULT

```
=== SYN grandson
2255:| CHAPTER 2 MANKIND: SEX, AGE, FAMILY RELATIONSHIP 9.1 Man! (Human Being) 2.47 GRANDMOTHER 9.91 Man? (vs. Woman) 2.48 GRANDSON 2.92 Woman 2.49 GRANDDAUGHTER 2.93 MALE’ 2.51 UNcLE 9.94 TeMALE 2.52 AUNT 9.942 Sex 2.53 NEPHEW | 9.25 Boy 2.54 NIECE 9.26 GIRL 2.55 CousIN | 2.27 CHILD 2.56 ANCESTORS 2.28 INFANT 2.57 DESCENDANTS 231 HUSBAND 2.61 Fatuer-1n-Law ~ 2.32 Wire 2.62 Morser-in-Law 2.33 Marry 2.63 Son-1n-Law 2.34 Marriage; WEDDING 2.64 DauGuHTEr-in-LAw 2.35 FaTHER 2.65 BrotuEr-in-Law 2.36 MoTHER 2.66 SisteR-1n-Law | 2.37 PARENTS 2.71 STEPFATHER 2.41 Son 2.72 STEPMOTHER 2.42 Daucuter 2.73 STEPSoN | 2.43 Cuiup (Son or Daughter) 2.74 STEPDAUGHTER 2.44 BroTuHEr 2.75 ORPHAN 2.45 SISTER 2.76 Wipow 2.452 BrotHEer(s) AND SISTER(s) 2.81 RELATIVES 2.46 GRANDFATHER 2.82 FamiIny 2.1 MAN! (Human Being) oy ae por Goth. manna Lith.  Zmogus, pl. Zmonés iy ae eee s oN maor, gumi Lett. cilveks It. heinb - an. —menneske ChSl. elovékit Tr. iter an menniska SCr. Eoujek Sp. hombre ME man(n), guma Boh. tlovtk Rum. om man Pol. czlowiek Tr. duine NE man Russ. elovek Nir. duine Du. mensch Skt.  manu-, purusa- W. dyn OHG man, mannisco, gomo Av. __masya-, masyaka-, Br. den MHG mensch OPers. martiya- NHG mensch
2933:9.46 GRANDFATHER
2975:MANKIND: SEX, AGE, FAMILY RELATIONSHIP iil 2.48 2.49 GRANDSON GRANDDAUGHTER
3142:2.53 NEPHEW (a, Brother’s Son; b, Sister’s Son)
=== WLD Bd2 nepot
21743:                                            nedo- -- nepot-                                   329
21794:   Ai. napat (und nach den andern Yerwandtschaftswortern auch ndptar-
21799:auch ,,Keffe‘': altlit. nepotis, nepatis, nepatis (Bezzenberger Beitr. z. Gesch.
21816:•(^sm-neptiios)', alb. mhese „Nichte'' aus "^nepotia (Pedersen BB. 20, 228 f.;
```


## [2026-09-07T19:34:00.061Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3610,3630p' HUB.txt; echo \"=== 6200\"; sed -n '6200,6218p' HUB.txt; echo \"=== leaves\"; python3 -c \"\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (3619,6210):\n    pos=sum(len(l)+1 for l in lines[:ln-1]); leaf=t[:pos].count('\\f'); print(ln,'leaf',leaf,'printed=',leaf-10)\n\""
}
```


### [2026-09-07T19:34:01.287Z] TOOL RESULT

```
1044. Lallwort.
1045. Wird nau (now) gesprochen, wie die Ipt. saw, rau
{soUy rou),
1046. Heisst na/vdxtan urspriinglich : streicheln, streichen,
schlagen'? Es bedeutet ein Instrument spielen (oder
schlagen), singen; schmeicheln, streicheln, liebkosen'.
Dazu auch nava 'Melodic, Gesang , arm. nuag *Melodie,
Lied*, nuagem singe, spiele ?
1047. Die Pehleviform nap (geschrieben napl Hajiab5d-In-
schrift Z. 4), zu der np. nava = jiid. tat. newe 'Enkel'
(Miller p. 74) aus phi. *napak 'gehort', geht auf den
ap. Nominativ napa zurtick; np. navada = phi.— 103 —
*napat'ak auf den ap. Ace. *napatam = zd. napatem;
np. navCLs-a (unbelegt) auf einen ap. Ace. '^napdd''am
(vgl. zd. naptarem) zuriick. Daneben nahasa 'Enkel*
JRAS. 1894, 489.
1049. Sal. Shuk., pers. Gram. p. 39: nuvacL
1051. Np. mive^ nube konnen nicht hierher gehoren.
1053. Np. nuved *frohe Botschaft' stellt Fr. Miiller,
WZKM. 8, 98 zu arm. LW. nwer *Darbringung, Weih-
geschenk, Opfergabe', das ein phi. *nived voraussetzen^)
=== 6200
geht' = phi, pesupai Gl. and Ind. 114, paz. pHawai Shk. 263,
arm. pEsopay,
^) Die Bemerkung p. 60, Nr. 528, dass dMn gesprochen worden
sei, ist falsch, wie die von Vullers s. v. angefuhrten Verse (Vis u
Ramin p. 103, 11, 12, 19, 20, 21) zeigen.
2) Daneben fam JRAS. 1894, p. 432 und 453.— 176 ^
§ 67. Ap. p = np. V und b (paz. w) in: av neben
gewShnlichem a6 *Wasser' = paz. aw Shk. 232 , ap. dpi- ;
dvaddn = abadan, abad *bewohnt', paz. dwddan 'prosperous*
Shk. 232, phi. apatan, arm. anapat 'unbewohnt, wiist*; na-
vdda 'Enkel' neben nabasa (oben p. 103) und nablra, ap.
*7}apdt', nom. napd; nivistan — nibistan (JRAS. 1894, p. 430)
*schreiben', ap. nipistanaii/; kdbln *Mitgift* = kdvm JRAS.
1894, p. 479, arm. kapen-U 'Lohn (der Hure); dvard *Kampf,
navard = nabard 'Kampf, phi. n(i)part Gl. and Ind. 233;
lava = Idba *Schmeichelei' H. 952 ; tdv = tdb 'Glanz, Hitze,
Zorn, Qual* H. 372; tdva = tdba *Pfanne*, phi. tdpak; ta-
vidan — tdbldan *drehen, spinnen' H. 372, vgl. oben p. 46 ;
tavar — tabar *Beir, arm. tapar; rev *Betrug, List': Jir^
=== leaves
3619 leaf 112 printed= 102
6210 leaf 186 printed= 176
```


## [2026-09-07T19:34:12.015Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2975,3010p' SYN.txt; echo \"=== NEPHEW\"; sed -n '3142,3175p' SYN.txt"
}
```


### [2026-09-07T19:34:12.074Z] TOOL RESULT

```
MANKIND: SEX, AGE, FAMILY RELATIONSHIP iil 2.48 2.49 GRANDSON GRANDDAUGHTER
Grk. qratéds Tats, viwvos, tbods, ma.dds mats, vlwv7n Ouyarptbods, ey yvovos
NG éyyovos ey youn
Lat. nepos neplis
It. nipote nipote
Tr. _petit-fils petite-fille
Sp. nielo mela
Rum. nepot nepoata
Ir. aue, 0a, ua aue meh : ;
NIr. mac mic, mac inghine, inghean mic, inghean inghine, garmhac gairinghean
W. wyr wyres
Br. douaren douarenez
Goth. barné barna ‘grandchildren’
ON sonar-(déttur-)sonr sonar-(dottur-)doltir
Dan. s¢nnes¢gn, dattersgn sénnedatter, datterdatter
Sw. sonson, dotterson sondotter, dotterdotter
OE suna sunu, dohtor sunu (nefa) (suna dohtor, dohtor dohtor?)
ME sonys sone, neveu (sonys doughter, etc.?) nece
NE grandson granddaughter
Du. kleinzoon kleindochter
OHG  zevo, eninchil nift
MHG enenkel (neve) niftel
NHG enkel enkelin
Lith. anukas, stinaus (dukters) anuké, stinaus (dukters) dukté vatkas
Lett.  déla(meitas)déls déla (meitas) meita
ChSl. viinukit vinuka
SCr. unuk unuka
Boh. vnuk onutka
Pol. wnulk wnuczka -
Russ. vnuk onutka
Skt. ndapat-; p&utra-, déuhitra- pautri-, déuhitri-
Av. napat- napii-
2.48, 2.49. ‘Grandson’ and ‘grand- daughter’ may always be expressed more specifically as ‘son’s (daughter’s) son (daughter)’. Such are the usual ON, Dan., Sw., OE, Lith. (in part), and Lett. terms. Or simply ‘child’s child’, a8 most commonly in Greek and so in Gothic. Some of the terms reflect an Inherited IE word. Others are deriva- tives or phrases containing the words for
‘son’ or ‘dau ghter’. A few ae ae are of the
Ns oy *nepot-, fem. *nepti-, prob. ve is , epd. of neg. ne and a form of €m seen in Skt. pati- ‘master’, Lat.
otis ‘ is li Pols ‘able’, ete., that is lit. ‘powerless’.
=== NEPHEW
2.53 NEPHEW (a, Brother’s Son; b, Sister’s Son)
Grk. dd5eAptoo0s j
NG dvepids, avuyeds -
Lat. frairis filius (a); sordris filius (b) It. nipote
Tr. neveu
Sp. sobrino
Rum. nepot
Ir. niae (b)
NIr. garmhac
W. nat
Br. niz
Gothi=, cs
ON nefi
Dan.  brodersdn (a); s¢stersén (b); nev Sw. brorson (a); systernson (b); nevd
OE nefa; suhterga (a) ME neve, neveu
NE nephew Du. neef OHG  nevo
Skt. matur-bhratar- is attested for ‘mother’s brother’, for which the usual word is matula, a dim. formation from matar- ‘mother’.
Skt. pitr-svasar- ‘father’s sister’, matr- svasar- ‘mother’s sister’, both rare.
2.54 NIECE
(a, Brother’s Daughter; b, Sister’s Daughter)
adedpid7
dvefia, avid
fratris filia (a); sororis filia (b) nipote
niece
sobrina
nepoala
necht
neacht
nith
nizez
nipt
broderdatter (a); sfsterdatter (b) brorsdotter (a); systerdotter (b) nift
nyfte, nece
niece
```


## [2026-09-07T19:34:19.362Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt; do echo \"== $f\"; grep -c '' $f; grep -n 'نوه\\|نبسه' $f | head -5; done"
}
```


## [2026-09-07T19:34:20.147Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== ARY\"; grep -n 'نوه\\|نواده\\|نبیره' incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-07T19:34:20.591Z] TOOL RESULT

```
== MON_part1.txt
99339
150:در ژانویةٌ همان سال در (موتمر اسلامی) جدننوه‌انمی عنسداهة که در لاهور 
7853:نوهاء تازه‌ها» هر چیز تازه و نو بد ید امد ه. 
10092:نشینند و کف‌های دست‌ها را بر سر زانوها 
10596:اول. (ق.) از نوه مجددآء باز هم» دوباره. از 
20308:دوبار» از نوه مجدداً بار دیگر» باز آمدن» 
== MON_part2.txt
94500
6193:شحص. نوه. نبیر ه۲ ج ج. فررزندزادگان. 
14139:مهره‌های زانوهایش دنق 
26812:مبنی بر نوهین و تعر یص. 
34183:هار آدتتشن دیهیم است. منوه‌اش 
46776:مستکاوس: ۱۱۵۵2۷ [ع.] (افا.) انوه
```


### [2026-09-07T19:34:20.643Z] TOOL RESULT

```
== ARY
47:«هند و اروپایی» نامی است که به خانواده‌ی بزرگی از زبانها داده می‌شود. این خانواده شامل
75:خانواده‌ی بزرگك از هندوستان و فلات ایران تا باختر اروپا و بریتانیای کبیر گسترش دارند. برخی
82:تنها در اشاره به یک خانواده‌ی بزرگك زبانها بلکه در اشاره به تیره‌ی بخصوص از نژاد سفید بکار
92:به عبارت دیگر» نازی‌ها واژه‌ی «آریایی» راکه قبلاً په خانواده‌ای از زبانها اطلاق می‌شد به
400:شد این پودکه در اروپا چند خانواده‌ی زبان وجود دارد (ژرمنی و لاتین و اسلاوی وغیره) وهر یک
401:از این خانواده‌ها شامل چند زبان‌اند. مثلاً خانواده‌ی لاتین شامل ایتالیایی و فرانسه و اسپانیایی و
403:و نروژی و ایسلندی. خانواده‌ی اسلاوی شامل روسی و لهستانی و چکك و صربستانی و اسلواکی و
422:موضوع دیگری نی زکه به تدریج برایشان مشهود شد این بود: خانواده‌های زبان‌های اروپایی با
523:باشند. همچنین زبان پارسی کهن را نیز می‌توان جزء این خانواده مسحسوب نمود.
533:خانواده‌اند. ۱
```


## [2026-09-07T19:34:27.939Z] TOOL CALL #44: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T19:34:27.944Z] TOOL RESULT

```


```


## [2026-09-07T19:34:32.341Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/nep%C5%8Dts",
 "prompt": "Give the reconstructed root, its gloss, the feminine form, and all descendants listed for Proto-Iranian/Indo-Iranian and Latin. Quote the etymology note."
}
```


## [2026-09-07T19:34:33.385Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%88%D9%87",
 "prompt": "Give the Persian entry for نوه: etymology (Middle Persian form, Old Iranian, Proto-Indo-European), meaning, and any related terms like نواده، نبیره، نواسه."
}
```


### [2026-09-07T19:34:33.691Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T19:34:39.756Z] TOOL RESULT

```
# Persian Entry for نوه

**Meaning:** The word denotes a "grandchild" in Persian.

**Etymology:** The term traces back through "Middle Persian" to "Old Persian," ultimately deriving from Proto-Indo-European *\*népōts*. The progression shows: Proto-Indo-European → Proto-Indo-Iranian *\*nápāts* → Old Persian → Middle Persian → Persian نوه.

**Related Terms:** Alternative forms include نواسه (nawāsa) and نواس (nawās), primarily used in Dari and Tajik dialects. An archaic variant is نوا (navâ).

**Cognates:** The entry notes linguistic parallels across Indo-European languages, including Sanskrit नपात् (napāt), Latin nepōs, and English "nephew," all sharing the same ancestral root.
```


## [2026-09-07T19:34:45.387Z] TOOL CALL #47: Bash

```json
{
 "command": "curl -s 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9p%C5%8Dts' -o /dev/null -w '%{http_code}\\n'; curl -s -L 'https://en.wiktionary.org/w/index.php?search=Reconstruction%3AProto-Indo-European%2Fnepots&title=Special%3ASearch' | grep -o 'Reconstruction:Proto-Indo-European/[a-zA-Zāēīōū̯ḱǵʰʷ%.-]*' | sort -u | head -20"
}
```


### [2026-09-07T19:34:47.333Z] TOOL RESULT

```
200
Reconstruction:Proto-Indo-European/
Reconstruction:Proto-Indo-European/b%CA%B
Reconstruction:Proto-Indo-European/bʰr
Reconstruction:Proto-Indo-European/%C
Reconstruction:Proto-Indo-European/d%CA%B
Reconstruction:Proto-Indo-European/dʰugh
Reconstruction:Proto-Indo-European/h
Reconstruction:Proto-Indo-European/h%E
Reconstruction:Proto-Indo-European/m
Reconstruction:Proto-Indo-European/m%C
Reconstruction:Proto-Indo-European/n
Reconstruction:Proto-Indo-European/n%C
Reconstruction:Proto-Indo-European/p
Reconstruction:Proto-Indo-European/p%C
Reconstruction:Proto-Indo-European/ph
Reconstruction:Proto-Indo-European/ph%E
Reconstruction:Proto-Indo-European/suHn
Reconstruction:Proto-Indo-European/suHn%C
Reconstruction:Proto-Indo-European/sw
Reconstruction:Proto-Indo-European/sw%C
```


## [2026-09-07T19:34:51.267Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9p%C5%8Dts",
 "prompt": "Give the reconstructed root and gloss, the feminine *nepth2-/neptis, the etymology note (is it ne + potis?), and the descendants listed for Proto-Indo-Iranian, Proto-Iranian, Avestan, Old Persian and Latin."
}
```


## [2026-09-07T19:34:52.265Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/nephew",
 "prompt": "Full etymology of nephew, and also what it says about niece if mentioned. Include Old French forms and dates."
}
```


### [2026-09-07T19:34:57.280Z] TOOL RESULT

```
# Proto-Indo-European *népōts Analysis

## Reconstructed Root and Gloss
**\*népōts** m or f (oblique stem **\*n̥pt-**) means "grandson," "descendant," or possibly "nephew."

## Feminine Form
The feminine derivative is **\*néptih₂**, listed under derived terms.

## Etymology Note
Yes, the page discusses this theory: "The reconstruction without a laryngeal has been suggested to be derived from **\*né** ('not') and **\*pótis** ('master, lord, husband')."

However, this etymology is debated, as some propose an initial laryngeal (*h₂népōt) based on Greek evidence.

## Descendants
The page lists these language families but **does not provide specific entries** for:
- Proto-Iranian (only Proto-Indo-Iranian is listed)
- Avestan
- Old Persian
- Latin

**Available descendants shown:**
- **Proto-Indo-Iranian:** \*nápāts
- **Proto-Italic:** \*nepōts (which would lead to Latin forms, though not explicitly detailed here)

The content does not contain the granular descendant information you requested for those specific ancient languages.
```


### [2026-09-07T19:34:59.149Z] TOOL RESULT

```
# Etymology of Nephew and Niece

## Nephew

The term "nephew" dates to around 1300, derived from Old French *neveu* (Old North French *nevu*), meaning "grandson, descendant." This ultimately traces to Latin *nepotem* (*nepos* in nominative form), which by around 150 A.D. denoted "sister's son, grandson, descendant." The word reconstructs to Proto-Indo-European *nepot-*, "grandchild."

Originally pronounced /nev-u/, the spelling shifted unetymologically to include *-ph-* after 1400, with pronunciation partially following suit. The meaning narrowed during the 17th century to its current exclusive sense.

## Niece

The entry notes that "niece" emerged around 1300 from Old French *niece* (earlier *niepce*), meaning "daughter of one's brother or sister; granddaughter; female relative." This derives from Latin *neptia*, a feminine form of *neptis* ("granddaughter"). Like nephew, "niece" initially carried broader meanings, commonly referring to "a granddaughter" or any remote female descendant until approximately 1600.

Both terms originally encompassed grandchildren but narrowed to refer specifically to siblings' children by the early modern period.
```


## [2026-09-07T19:35:04.717Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%A8%DB%8C%D8%B1%D9%87",
 "prompt": "Persian نبیره: etymology and meaning; any Middle Persian form; related words نبسه/نبس/نواسه."
}
```


## [2026-09-07T19:35:05.849Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/neveu",
 "prompt": "Old French and French neveu: etymology (from Latin nepotem/nepos), and descendants including Middle English."
}
```


### [2026-09-07T19:35:06.145Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T19:35:12.801Z] TOOL RESULT

```
# Summary of "Neveu"

Based on the Wiktionary entry, **neveu** is a word with multiple language entries:

**French**: The primary definition is "nephew" (masculine noun). The word evolved from Old French *neveu*, which came from Latin *nepōtem*, ultimately tracing back to Proto-Indo-European *népōts*.

**Etymology Chain**: The entry shows a linguistic progression: "Inherited from Old French *neveu*, from Latin *nepōtem*, from Proto-Italic *\*nepōts*, ultimately from Proto-Indo-European *\*népōts*."

**Other Languages**: 
- In **Catalan**, neveu is a verb form (second-person plural present/imperative of *nevar*)
- In **Romanian**, neveu refers to *névé* (granular snow), borrowed from French
- **Middle English** lists it as an alternative form of *nevew*
- **Old French** shows it as an alternative to *nevod*

The French term produced descendants in Scandinavian languages (Danish *nevø*, Swedish *nevö*) and Mauritian Creole (*neve*).
```


## [2026-09-07T19:35:18.624Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%86%D8%A8%D8%B3%D9%87/",
 "prompt": "What do Dehkhoda and Mo'in say about نبسه / نبس? Give the definitions and any etymology (e.g. from نواسه)."
}
```


### [2026-09-07T19:35:23.671Z] TOOL RESULT

```
# Dehkhoda and Mo'in on نبسه/نبس

**Dehkhoda's Dictionary:**
Defines نبسه as "دخترزاده" (niece/granddaughter). The entry notes it can refer to "son's daughter, daughter's daughter, son's son, or daughter's son" depending on usage. Dehkhoda also identifies it as a variant of نواسه (grandchild/descendant).

**Etymology:** The text states نبسه is "مبدل و مخفف نواسه است" (an altered and shortened form of نواسه), which originally meant grandchild in Khorasan dialect.

**Mo'in's Dictionary:**
Provides the concise definition: "نوه، فرزندزاده" (grandchild, descendant).

Both lexicographers treat نبسه/نبس as fundamentally meaning a grandchild or descendant, with Dehkhoda offering more detailed variants for different familial relationships.
```


## [2026-09-07T19:35:30.561Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%86%D9%88%D9%87/",
 "prompt": "Quote what فرهنگ معین (Mo'in) and Dehkhoda say for نوه, including any bracketed origin tag such as [په.] (Pahlavi) and any etymology."
}
```


### [2026-09-07T19:35:34.641Z] TOOL RESULT

```
# Definitions from Persian Dictionaries

**Dehkhoda Dictionary:**
"نبیره، فرزندزاده" (niece/nephew, grandchild) - listed as the primary meaning with reference to Rashidi and other classical sources.

**Mo'in Dictionary:**
"فرزندزاده، نبیره" (grandchild, niece/nephew) - defined concisely as a descendant in the second generation.

Both dictionaries present نوه as referring to grandchildren or grandchild-relations, with Dehkhoda providing more extensive historical and etymological documentation across multiple classical Persian sources.
```


## [2026-09-07T19:35:36.701Z] AGENT

Now let me archive the web sources.


## [2026-09-07T19:35:44.294Z] TOOL CALL #54: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9p%C5%8Dts' --note 'page 360 root Nepot/Neptis: PIE *nepots gloss, fem *neptih2, ne+potis etymology, Proto-Indo-Iranian *napats' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%86%D9%88%D9%87' --note 'page 360 node 3: Persian نوه etymology MP < OP < PIE *nepots; variants نواسه/نواس/نوا' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/nephew' --note 'page 360 nodes 4-6: Latin nepotem > OF neveu > ME/English nephew c.1300; niece < OF niece < L neptia' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/neveu' --note 'page 360 node 5: Old French/French neveu < Latin nepotem < Proto-Italic *nepots' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D9%86%D8%A8%D8%B3%D9%87/' --note 'page 360 node 3: Dehkhoda/Moin on نبسه/نبس = دخترزاده, مبدل و مخفف نواسه' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D9%86%D9%88%D9%87/' --note 'page 360 node 3: Moin and Dehkhoda on نوه = فرزندزاده، نبیره' 2>&1 | tail -3"
}
```


### [2026-09-07T19:35:49.851Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9a5a588399fbf658.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ccfcd5273d32b456.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/13ae2917a62da89c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6ad1fc7a388a4cef.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/90c6853a8a46662d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0cbfb57b13af007a.txt
```


## [2026-09-07T19:35:55.538Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'nephew' SKT.txt | head -5; echo \"=== FSD vol3\"; grep -n '^nephew\\|^niece' FSD_vol3.txt | head -5; echo \"=== WEB\"; grep -n -i '^nephew' WEB_vol1.txt | head -3"
}
```


### [2026-09-07T19:35:55.646Z] TOOL RESULT

```
12234:Nephew.  (K.-L.)  hi.E,mfvtu(^nevm). —  O.  F.  tifvfit,  'a  nephew;'  Cot.  —  L. nepotem,  ace.  of  tttpcst  a  grandson,  also  a nephew.  +  S^.  nap4t,  a  grandson ;  A  S. tuf^,  a  nephew ;  (^  ntffi,  ucuhcw.  Der. nep^'ism,  favouritism  to  relations,  from L.  tupat;  stem  of  tupos. ••  niece.  (F.  —  L.)  M.  E.  »«•/,  mya.  — O.  F.  ttuce  (F.  nUii),  —  Low  L.  ntptia,  a niece.  «-L.  Hiptis,  a  grand -daughter,  niece; used  OS  fern,  of  L.  nepoi  (above).
12270:Niece;  sec  Nephew.
=== FSD vol3
53448:nephew to marry a silent wotniin IniiN'rsonutcd by a boy.
=== WEB
```


## [2026-09-07T19:36:04.172Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npos=sum(len(l)+1 for l in lines[:12233]); leaf=t[:pos].count('\\f'); print('leaf',leaf,'printed=',leaf-20)\n\""
}
```


### [2026-09-07T19:36:05.453Z] TOOL RESULT

```
leaf 327 printed= 307
```


## [2026-09-07T19:36:09.478Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21790,21825p' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-07T19:36:09.520Z] TOOL RESULT

```
(dann zu ned- „zusammendrehen‘'),                 ist   unsicher.


uepot- „Enkel; Keife”, fern, '^negytl,
   Ai. napat (und nach den andern Yerwandtschaftswortern auch ndptar-
..Enkel, Kachkomme'', av. napdt-, naptar-, ap. napfit- ds., ai. aparn napaf,
av. apiqyn n.     Kame  einer Gottheit (,,Enkel der AYasser^- ; s. Bartholomae
Altiran. AYb. 1039    m. Lit.; nicht nach A\^ilhelm BB. 12, 104, Johansson TP.
4, 143 f. zu lat. Nepfumis usw.), lat. nejws, -tis ..Enkelkind, Enkel*', spater
auch ,,Keffe‘': altlit. nepotis, nepatis, nepatis (Bezzenberger Beitr. z. Gesch.
d. lit. Spr. 303 f.) ..EnkeF; ahd. nevo „NefFe, A'erwandter^', ags. nefa „Enkel,

KeffeF anord. nefe „KefFe, Yerwandter'; mir. yiice, gen. yiiath „Schw'ester-
sohn‘‘ (zur Form zuletzt Pokorny ZfceltPh. 10, 405 f.), cymr. yiei, nai ds.,
corn, noi „Enkel”, mbret. nl ,.Xeffe'\
  Fern.    ai.   napt1, naptf-h, napti-h ..Enkelin, weiblicher              Nachkomme‘\       av.
napii- „Enkelin‘‘;
330                                nebh-    — nem-
    Lai neptis (fiir -tl{s) nach den f-St.) „Enkelin'', spater „Nichte“; altlit.
nepte  (s, zur Form Lommel Stud. ub. idg. Femininbildungen 71) „Enkelin‘':

air.   necht   cymr. abret. nith, mbret. nis, corn, noith, „Ifichte“; ahd. nift
„neptis,    privigna“, nhd. (eigentlich nd.) Nichte, anord. nipt „Schwester-
tochter, Nichte“.
   Weiterbildung ^neptio-: av. naptya- „Abkoininling, Jfachkomme''; aksL
nethjh   „Neffe“, fem. cech, neti „Nichte'*, gr. avE'ipiog „Geschwistersohn“
•(^sm-neptiios)', alb. mhese „Nichte'' aus "^nepotia (Pedersen BB. 20, 228 f.;
vielleicht erst aus lat. nepos gebildet).
   Dber das von Wiedemann BB. 27, 225 mit tJnrecht auf *npat-s-U zuriick-
gefiihrte dt.   Base s. vielmehr Kluge und Weigand-Hirt s. v.
   Z. B. Curtius^ 266.       — Vermutlich als „Unmundiger, UnselbstandigeF'
zu ne und potis (s. Prellwitz^ 310, Streitberg IF. 3,334, Leumann FestgruB
an Bobtlingk 77, ZfdtWtf. 11, 63).
   Da6 unser Stamm ursprl. nur die Enkel gegeniiber dera Yater ihrer
Mutter und die KefiPen gegeniiber deren Bruder bezeichnet babe (Delbriick
A'^erw. 502 ff.), ist nicht geniigend gestiitzt (Hermann GGN, 1918, 215).
```


## [2026-09-07T19:36:18.115Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n -i 'nepot\\|napat' ARY_latin_index_pages.txt ARY_pages.txt | head -10; echo \"== nave\"; grep -n 'نوه' ARY_pages.txt | head"
}
```


### [2026-09-07T19:36:18.201Z] TOOL RESULT

```
ARY_latin_index_pages.txt:991:oY NAPAT gliay! NAPAT sey SL NEPOT Toe logy y a seul
ARY_latin_index_pages.txt:993:NBO AS gy SL NEVI 59, NEPOTIS: ol (NIPOTE ; gle | NEEF ygucla
ARY_latin_index_pages.txt:14338:NAPAT — (OLD PERSIAN) jtely gosh NARA, NABA HAVESTAN) gt 9!
ARY_latin_index_pages.txt:14747:NEVO NABA., NAPAT, —-{AVESTAN) pleas!
ARY_latin_index_pages.txt:14749:NEVO :(OLD HIGH GERMAN) <5 git NAPAT, (OLD PERSIAN) Skul os),
ARY_latin_index_pages.txt:14753:NEVE (DANISH) Sails NAPAT (SANSKRIT) 4 Sasle
ARY_latin_index_pages.txt:14755:NEVE HNORWGIAN) 5 5 NEPOS, NEPOTIS LATIN) os
ARY_latin_index_pages.txt:14758:NETUI NEPOT, NEPOATA (RUMANIAN) gl,
ARY_latin_index_pages.txt:14759:WNUK POLISH) gleng) NEPOT PORTUGUESE) J\ss 4
== nave
1014:یونانی:08870785. مثال دیگر واژه‌ی «نوه» است که همربشه‌های آن در زبان هند و اروپایی چنین
5260:8 ,51121825 6 (۲1126) ,349 لته ۰ علمانوه
14984:۶ ) نوه نواده :
```


## [2026-09-07T19:36:19.180Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/indoeurop.html",
 "prompt": "Find the entry for the root nepot-. Quote it exactly (gloss, feminine form, Latin derivatives, English words, Pokorny page)."
}
```


### [2026-09-07T19:36:25.294Z] TOOL RESULT

```
I cannot find an entry for the root "nepot-" in the provided web page content. The page shows Indo-European roots entries organized alphabetically from "ad-" through "bheuə-", but does not extend to entries beginning with "n". The content appears to be truncated before reaching roots starting with that letter.
```


## [2026-09-07T19:36:29.633Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 -c \"\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (1014,14984):\n    pos=sum(len(l)+1 for l in lines[:ln-1]); leaf=t[:pos].count('\\f'); print(ln,'leaf',leaf,'printed=',leaf+1)\nprint('---- ctx 1014')\nprint('\\n'.join(lines[1008:1030]))\nprint('---- ctx 14984')\nprint('\\n'.join(lines[14975:15000]))\n\""
}
```


### [2026-09-07T19:36:30.797Z] TOOL RESULT

```
1014 leaf 36 printed= 37
14984 leaf 504 printed= 505
---- ctx 1014
واژه‌ای وابسته به «خانه» و «خانواده» در زبان هند و اروپایی نخستین 203" بود. سر پرست يا.
رئیس خانواده 003/68-70778(پدر خانواده یا خانسالار) نامیده می‌شد. در برخی دیگر از زبانهای
[pdf page 37]
۸ ریشه‌های هندو اروپایی زبان فارسی
کهن هند و اروپایی اپن واژه چنین است: سانسکریت: 0۸۸/۳۸77 اوستایی ۴۳۸771 08070
یونانی:08870785. مثال دیگر واژه‌ی «نوه» است که همربشه‌های آن در زبان هند و اروپایی چنین
است: هند و اروپایی نخستین: 7 سانسکریت: ۸1۸77۸7 اوستابی ‎٩1۸3۸7‏ لانین:
58 آلمانی: ‎٩18۳۳8‏ انگلیسی: ایسلندی کهن:0۷3۳1 ایرلندی کهن:11۸٩‏
هلندی ۸7۳8۳ ایتالیایی: 5 لینوانی: 87۳۳0718 کردی: ‎٩3783۷1‏ سا کسو نی کهن؛ 90وی ..
این واژه‌های همريشه و واژه‌های مشابه دیگر رابطه‌ی خانوادگی هند و اروپائیان نخمتین را بطور"
تفریبی مشخص می‌کنند. ۱ :
۵- زناشویی: واژگان همربشه‌ی هند و اروپایی و متون کهن ایرلندی و ولزی و همچنین
اضانه‌های پونانی و رومی نشان می‌دهند که هند و اروپایی‌ها دارای گونه‌ای ازدواج و مراسم زناشویی
بودندکه با تأید و تحت نظ رکاهتان انجام می‌شد. ضمناً ازدواج نوعی معامله هم بود: داماد یا ایل او به
پدر عروش يا ایل عروس «هدیه؛ (مثلاً چند رس گاو) می‌دادند. در مقابل پدر عروس موظف برد که
جهیزبه عروس را تهیه کند. معمولاً مذا کرات وابسته به زناشویی طولانی بود.
ضمناً ون حقوقی گال‌ها و ایرلندی‌های کهن و همچنین حماسه‌های پاستانی (سانند آثار
هومر) نشان می‌دهند که رسم چند زنی نیز در میان توانگران هند و اروپایی رایج بوده است. ژول
سزار (2۸738۸ .7) درکتاب خو د (200ته 8811۵ 08)گزارش می‌دهد که تعدد زوجات
در میان اعیانگال رواج داشت و اگر شوهر به طرز سرا رآمیزی می‌مرد» زن‌های او مورد شکنجه قرار
می‌گرفتند. در حماسه‌ی ابلیاد (1۸0ن11) اثر هومر آمده است که پریام (/۳۸1۸3) شاه تروا دو زن
داشت. اولی هکوبا (180178۸]) برد که برایش نوزده پسر زائید. دومی لائوتو (۸07730]) بود.
---- ctx 14984

ادا ,۱۷۷029 ,۸۸۷۸2۸8۸ فریزی کهن ((۲/314 00):

آرمنی (6(41421ه): انا زان ال اد نالا

یونانی (0728): ال اه ند زرا آلمانی کهن ((44ن058 04لا 010):
لانین (710مل): یرای بدا رال ناد رانا
[pdf page 505]
۶ ) نوه نواده :
آلمانی ((0554۸): زد مراد نی بلفاری (ممتمممانا: ۰ 887513۲۸35۲
انگلیسی کهن (9[4/-ا8۷0 صا0): اسلراکی (31-0144): لانگ نراد دا
اناد ای زا نها آلبانی مهتم ۱۵۳۵0
انگلیسی (5/0/ا80): لاد ده دنا نا هه ی
دانمارکی (0۸(8[7): درادن پسگشت‌ها انش درا َ
سوئدی (/82015): 0 1 8 ۸002200
نروژی (۸/0818014۸۷: 0 5 ۰018 877
هلندی (ب77ا0): لد ید ادن 5 (0187882) نقل2 الما
لهستانی (۳015): ۰ 0211۷1577۸870 1 (۸1387880) :010/5
روسی (۷ل354تا: ۰ 08۳۷۷۸7۲۸۵78۸7 2601 (۸13۴۳۲82۲) ۸0
چک (لل280): ان نون راد ار برهان قاطع : ۳۱۹۵
اوستایی (/4897/42): ۰ ,۸۸۳۵ ۸۸8۸ 0
۸ فریزی کهن (۷لفا5ل77 صان): ۸۸
پارسی باستان (۶87814(۷ ۰:01 ,۴/۸۴۸7 آلمانی کهن (/(087244 ۲/0 ۵۱2): ۲۷۳۷۵
ای آلمانی (02704407). ند دنله
پهلوی (۷7الله۸): ۸ انگلیسی کهن (81/ا8۸0 صل0): 3۷8۸
```


## [2026-09-07T19:36:44.197Z] TOOL CALL #61: Bash

```json
{
 "command": "ls site/pages/360.jpg 2>/dev/null; pdftoppm -f 360 -l 360 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg360 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg360.png"
}
```


### [2026-09-07T19:36:46.136Z] TOOL RESULT

```
site/pages/360.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 45536 Sep  7 15:36 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg360.png
```


## [2026-09-07T19:36:49.048Z] TOOL CALL #62: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg360.png"
}
```


### [2026-09-07T19:36:49.546Z] TOOL RESULT

```

```


## [2026-09-07T19:36:49.541Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T19:37:13.874Z] TOOL CALL #63: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg360.png data/verification/sources/refs/ocr/BOOK/360.png && echo ok; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-07T19:37:13.965Z] TOOL RESULT

```
ok
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


## [2026-09-07T19:41:50.080Z] TOOL CALL #64: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-360.json",
 "content": "{\n  \"pdf_page\": 360,\n  \"book_page\": 330,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 2,\n      \"root\": \"Nepôt, Neptis\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *nepōt- / *népōts (obl. *n̥pt-) 'grandson, descendant', fem. *néptih₂ / *neptī- 'granddaughter'\",\n      \"note\": \"The root, the language label ('Indo-European') and both glosses are correct and completely standard. Pokorny 764 heads the entry 'nepot- \\\"Enkel, Neffe\\\", fem. *neptī-'; Walde-Pokorny II 329 f. has the same headword; Watkins/AHD gives 'nepot-. Grandson, nephew. Feminine *nepti-. [Pok. nepōt- 764.]'; Mann IEC 836 has 'nepóts (nepots) \\\"nephew, grandson\\\"' and, separately, 'nepteris (neptris) \\\"niece, granddaughter\\\"'. Nourai's two headword forms are the Latin shapes (nepōs/neptis) used as labels for the reconstruction; the reconstructed nominative is *népōts and the feminine *neptih₂/*neptī-, so 'Neptis' as an *IE* form is a Latinism rather than a reconstruction — a labelling convention of the book, not a factual error about the root. Both Pokorny and Walde-Pokorny add the (still current but not certain) analysis of the word as *ne-potis 'not-master' = 'the under-age, dependent one', an analysis Buck (SYN 2.48) and Wiktionary also report; Nourai does not comment on it, which is a harmless omission. The one thing that needs flagging on this page is that Nourai carries the Latin-shaped feminine 'naptis' down into the Avestan/Old Persian box (node #1), where the attested forms are Av. naptī-, Skt. naptī-; see that node.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *népōts «نبیره، فرزندزاده، بازمانده» و مؤنث آن *néptih₂ / *neptī- «نبیرهٔ دختر» است؛ پوکورنی (ص ۷۶۴) و والده-پوکورنی (ج ۲ ص ۳۲۹) و واتکینز (فرهنگ ریشه‌های هندواروپایی امریکن هریتیج) و مان (IEC ص ۸۳۶) همه همین ریشه و همین معنا را می‌آورند، پس ادعای نورایی در بارهٔ ریشه و زبان و معنا درست است. تنها نکته این است که نورایی سرواژه‌ها را به شکل لاتینی (Nepôt، Neptis) نوشته، نه به شکل بازسازی‌شدهٔ هندواروپایی؛ این شیوهٔ نام‌گذاری کتاب است و خطای علمی به شمار نمی‌آید. پوکورنی و والده-پوکورنی این واژه را با احتیاط ترکیب *ne- «نه» و *potis «سرور، خداوند» می‌دانند، یعنی «نابالغ، وابسته»؛ نورایی به این تحلیل اشاره نکرده است. اما همین شکل لاتینی naptis را به جعبهٔ اوستایی/پارسی باستان هم برده که در آنجا صورت درست naptī- است (نگاه کنید به گرهٔ ۱).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9p%C5%8Dts\",\n        \"https://www.etymonline.com/word/nephew\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:764\", \"status\": \"supports\", \"note\": \"Pokorny IEW p. 764: 'Root / lemma: nepot- … Meaning: uncle; nephew, *descendant … Grammatical information: fem. neptī- … References: WP. II 329 f., WH. II 161 f., Trautmann 196. Page(s): 764' (refs/POK_full.txt lines 62600-62648, grep -n -i 'nepot' POK_full.txt). The Toronto page scans break exactly here: POK_02.txt leaf 425 carries the running number '764' but stops inside the preceding entry '2. nem-', and POK_03.txt begins at p. 771, so the German original of the nepot- entry is not in the local leaf scans; the indo-european.info database text (POK_full) reproduces it with the same page number 764.\"},\n        {\"ref\": \"IEC:836\", \"status\": \"supports\", \"note\": \"Mann, Indo-European Comparative Dictionary col./p. 836 (refs/IEC.txt leaf 467, the leaf carries the printed number '836'): 'nepóts (nepots) \\\"nephew, grandson\\\". Cf. ne-pis, ōn. WP II, 329  Skt. nápat …; Av. napō, obl: napāt- \\\"grandson\\\"; … Per. navade, id. beside nave, navāse, id., of various dial. origin; … Lat. nepos, gs: -potis \\\"grandson\\\"'; and on the same page 'nepteris (neptris) \\\"niece, granddaughter\\\". Cf. WP II, 329 and nepis, nepóts'. Mann thus supports both halves of Nourai's root box AND the Persian node in one place.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II pp. 329-330 (incoming/WLD/WLD_Bd2_pages.txt lines 21743-21825)\", \"stance\": \"supports\", \"note\": \"'nepot- \\\"Enkel; Neffe\\\", fem. *neptī. Ai. nápāt … av. napāt-, naptar-, ap. napāt- ds. … lat. nepōs, -tis \\\"Enkelkind, Enkel\\\", später auch \\\"Neffe\\\" … Fern. ai. naptī, naptīh \\\"Enkelin\\\" … av. naptī- \\\"Enkelin\\\"; Lat. neptis (für -tī(s) nach den i-St.) \\\"Enkelin\\\", später \\\"Nichte\\\" … Vermutlich als \\\"Unmündiger, Unselbständiger\\\" zu ne und potis'. The running head of the second leaf reads 'nebh- — nem- 330'.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. nepot- (refs/AHD_watkins1985.txt line 781)\", \"stance\": \"supports\", \"note\": \"'nepot-. Grandson, nephew. Feminine *nepti-. Latin nepos, grandson, nephew, and neptis, granddaughter, niece: NEPHEW, NEPOTISM, NIECE. [Pok. nepōt- 764.]' — same root, same gloss, same two Latin outcomes, and it is the source Nourai cites as 'AHD' on node #5. (The online appendix page ahdictionary.com/word/indoeurop.html truncates before the letter n, so the 1985 book text on disk was used.)\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 2.48/2.49 'Grandson / Granddaughter', p. 111 (refs/SYN.txt lines 2975-3010)\", \"stance\": \"supports\", \"note\": \"Buck's table gives 'Lat. nepos / neptis … Skt. nápat- / naptī- … Av. napāt- / naptī-' and the discussion: 'IE *nepot-, fem. *nepti-, prob. … cpd. of neg. ne and a form of *poti- seen in Skt. pati- \\\"master\\\", Lat. potis \\\"able\\\", that is lit. \\\"powerless\\\"'. Note Buck, like Bartholomae and Walde-Pokorny, has Avestan naptī- and reserves neptis for Latin.\"},\n        {\"src\": \"IEC\", \"where\": \"p. 836\", \"stance\": \"supports\", \"note\": \"see ref_check above; Mann is both Nourai's cited reference and an independent modern comparative dictionary for this root.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"napât, napâ : grandson; naptis : grand daughter\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The masculine forms are exactly right. Old Persian has a consonant stem napāt- 'grandson' whose nominative singular is napā (final -t-s cluster reduced to nothing in Aryan: Kent, Old Persian p. 193, 'napāt- sb. \\\"grandson\\\": Av. Skt. napat-, Lt. nepos, pIE *nepot- … napā nsm.'), attested at DB 1.3, DBa 4, AmH 4 and A²Pa 16 in Darius' and Artaxerxes' formula 'napā Aršāmahyā' = 'grandson of Aršāma'; Avestan has the same napāt- (nom. napā, acc. napātəm) plus an r-stem naptar- and the compound apąm napāt- 'Scion of the Waters', name of a divinity (Bartholomae, Altiranisches Wörterbuch cols. 1039-1040: 'j., g., p. napāt-: nafəδr- m., j. naptar-: nafšar- m., j. naptī- f. \\\"Enkel; Enkelin\\\"'). PIE nom. *népōts > Proto-Indo-Iranian *nápāts > Ir. napāt-, with the regular Indo-Iranian *e > a and loss of the final cluster. The FEMININE is the problem: no Avestan or Old Persian *naptis exists. Avestan has naptī- f. 'granddaughter' (Bartholomae col. 1039; Walde-Pokorny II 329 'av. naptī- \\\"Enkelin\\\"'; Buck 2.49 'Av. naptī-'), matching Skt. naptī-; the -s nominative neptis belongs to LATIN, where it was refashioned after the i-stems (Walde-Pokorny II 330: 'Lat. neptis (für -tī(s) nach den i-St.)'). The printed page (rendered at 200 dpi, copy at data/verification/sources/refs/ocr/BOOK/360.png) shows 'naptis : grand daughter' inside the 'Avestan / Old Persian' box, so the extraction is faithful and the slip is Nourai's own: he has carried the Latin-shaped root label 'Neptis' down into the Iranian box. Read as 'Av. naptī-' the node is fully confirmed.\",\n          \"derivation_fa\": \"صورت‌های مذکر کاملاً درست‌اند: پارسی باستان napāt- «نبیره، فرزندزاده» با فاعلی napā (خوشهٔ پایانی ‑ts در ایرانی باستان می‌افتد) که در کتیبهٔ بیستون (DB ۱٫۳) و دیگر کتیبه‌ها در عبارت napā Aršāmahyā «نوادهٔ ارشام» آمده است؛ اوستایی نیز همان napāt- (نامی napā، رایی napātəm) و ستاک ‑r‑دار naptar- و ترکیب apąm napāt- «نوادهٔ آب‌ها» (نام ایزدی) را دارد — بارتولومه، ستون‌های ۱۰۳۹–۱۰۴۰. زنجیرهٔ آوایی: هندواروپایی *népōts > هندوایرانی آغازین *nápāts > ایرانی napāt-، با تحول قاعده‌مند e به a. اما صورت مؤنث نادرست است: در اوستایی و پارسی باستان هیچ *naptis وجود ندارد؛ صورت اوستایی naptī- «نبیرهٔ دختر» است (بارتولومه ستون ۱۰۳۹؛ والده-پوکورنی ج ۲ ص ۳۲۹) هم‌ریشه با سنسکریت naptī-، و شکل ‑s‑دار neptis از آنِ لاتینی است که بر قیاس ستاک‌های i بازساخته شده. تصویر صفحهٔ چاپی (پیوست در BOOK/360.png) نشان می‌دهد که خودِ کتاب naptis نوشته است، پس خطای خوانش اسکن نیست بلکه خطای چاپی/سهو نویسنده است: نورایی سرواژهٔ لاتینی Neptis را به جعبهٔ ایرانی برده است. اگر naptī- خوانده شود، این گره کاملاً پذیرفتنی است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"naptis : grand daughter\",\n          \"correct_form\": \"naptī- (Avestan fem. 'granddaughter'); neptis is the Latin form\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9p%C5%8Dts\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KNT:193\", \"status\": \"supports\", \"note\": \"Kent, Old Persian, Lexicon p. 193 (refs/KNT.txt leaf 216, which carries the printed numeral '193' with the running head 'LEXICON'): 'napāt- sb. \\\"grandson\\\": Av. Skt. napat-, Lt. nepos, pIE *nepot- (§75.I, §110, §142). napā nsm. (§124.5, §188.I) AmH 4; DB 1.3; DBa 4; A²Pa 16.' Kent p. 151 also states the rule behind napā: 'in Aryan, when a word ended in two or more consonants, the final consonant or consonants fell off … thus pIE nom. *nepót-s \\\"grandson\\\", Lt. nepos, became pAr. *napat, Skt. nápāt.' Exactly Nourai's 'napât, napâ'. Kent has no feminine.\"},\n            {\"ref\": \"KLN:1039\", \"status\": \"supports\", \"note\": \"Klein, Comprehensive Etymological Dictionary, s.v. 'nephew' beginning on p. 1039 and running onto p. 1040 (refs/KLN_1966.txt leaf 556; the page-break numeral '1040' falls inside the entry): 'L. neputem, acc. of nepos, \\\"grandson\\\" … which stands for nepot-s and is cogn. with OI. nápat, Avestic napāt-, naptar-, OPers. napāt-, \\\"grandson, descendant\\\"'. Klein's feminine forms are given two pages later s.v. 'niece' and are 'OI. naptīh, Avestic naptī-' — i.e. Klein does NOT support 'naptis' for Avestan/Old Persian.\"},\n            {\"ref\": \"POK:764\", \"status\": \"supports\", \"note\": \"Pokorny 764 (POK_full.txt): 'Old Indic nápāt (secondary naptr-) \\\"grandson, descendant\\\", Avestan napāt-, naptar-, ap. napāt- … Fem. Old Indic naptī- \\\"granddaughter, female descendant\\\", Avestan naptī- \\\"granddaughter\\\"'. Supports napāt/napā, and gives naptī- (not naptis) as the Iranian feminine.\"},\n            {\"ref\": \"IEC:836\", \"status\": \"supports\", \"note\": \"Mann p. 836: 'Av. napō, obl: napāt- \\\"grandson\\\"; Ober [= OPers.] napa, obl: napāt-, id.' — Mann even records the two nominative shapes napā/napō beside the oblique stem, matching Nourai's pair 'napât, napâ'.\"},\n            {\"ref\": \"MFL:102\", \"status\": \"not_checked\", \"note\": \"MFL = Oranskij, Introduction to Iranian Philology in Keshavarz's Persian translation (Tehran 1979). refs_online.json records that only a 5-page image fragment of that translation is on archive.org (galaxy_ub2007_yahoo_201511) and that the Russian original and French translation have different pagination, so p. 102 cannot be checked.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch cols. 1039-1040 (refs/BRT.txt leaf 580, which carries the column numeral '1040')\", \"stance\": \"partial\", \"note\": \"'j., g., p. napāt-: nafəδr- m., j. naptar-: nafšar- m., j. naptī- f. \\\"Enkel; Enkelin\\\"', with the OP citation 'adam Dārayavauš … Vištāspahya puθra Aršāmahyā napā' and the divinity 'apąm napāt-'. Supports the masculine exactly; contradicts the feminine 'naptis' — Bartholomae's Avestan feminine is naptī-. (Nyberg's glossary cites this very column, 'Av. (1039)', for Pahlavi nap.)\"},\n            {\"src\": \"KNT\", \"where\": \"p. 193 and p. 151\", \"stance\": \"supports\", \"note\": \"see ref_check; Kent is the standard Old Persian lexicon and gives both stem napāt- and nom. napā with inscription references.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 329\", \"stance\": \"partial\", \"note\": \"'Ai. nápāt … av. napāt-, naptar-, ap. napāt- ds.' supports the masculine; 'av. naptī- \\\"Enkelin\\\"' with 'Lat. neptis (für -tī(s) nach den i-St.)' on p. 330 shows the -s form is specifically Latin, not Iranian.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 2.48/2.49, p. 111\", \"stance\": \"partial\", \"note\": \"table row 'Av. napāt- / naptī-' — masculine confirmed, feminine given as naptī-.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"nab : grandchild\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian nap/nab (Book Pahlavi spelling np, Inscriptional Pahlavi np at Hājīābād line 4) 'grandson' continues the Old Persian NOMINATIVE napā rather than the oblique stem: with the loss of Old Iranian final vowels in Middle Persian, *napā > nap, and intervocalic/final Old Iranian -p- was voiced and spirantised in later pronunciation, whence MacKenzie's and Nourai's transliteration nab. MacKenzie, Concise Pahlavi Dictionary p. 57, prints 'nab [np | N nawa] grandson' — i.e. he himself already links it forward to New Persian nawa (= naveh), which is Nourai's next arrow. Nyberg's glossary adds the textual attestations and the exact reconstruction: 'nap [npy] grandson HajB:4, ŠPrs:8. — Nom. sg. *napā of Av. (1039), NP navah < *napak.' Nourai's gloss 'grandchild' is a fair rendering; MacKenzie and Nyberg both say 'grandson', and MacKenzie also records the related MP *naft [npt'] 'descendant' (from the oblique stem napāt-) and nabānazdišt 'next of kin' (< Av. nabānazdišta-).\",\n          \"derivation_fa\": \"فارسی میانه nap/nab (به خط پهلوی کتابی np، و در پهلوی کتیبه‌ای np در سنگ‌نوشتهٔ حاجی‌آباد سطر ۴) «نبیره، فرزندزاده» بازماندهٔ صورت فاعلی پارسی باستان napā است، نه ستاک غیرفاعلی napāt-: با افتادن واکهٔ پایانی در فارسی میانه *napā به nap بدل شد و «پ» ایرانی باستان در جایگاه پایانی/میان‌واکه‌ای نرم و سایشی شد و از این رو مکنزی و نورایی آن را nab آوانویسی می‌کنند. مکنزی در «فرهنگ کوچک پهلوی» ص ۵۷ می‌نویسد: nab [np | N nawa] «نبیره»، یعنی خود او این واژه را به «نوهٔ» فارسی نو پیوند می‌دهد — همان کمانی که نورایی کشیده است. نیبرگ نیز می‌افزاید: nap [npy] «نبیره»، صورت فاعلی مفرد *napā از اوستایی (بارتولومه ۱۰۳۹)، و فارسی نو navah از *napak. پس ادعای نورایی درست است؛ تنها معنای دقیق‌تر «فرزندزادهٔ پسر» است، هرچند «فرزندزاده» هم پذیرفتنی است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"PHD:57\", \"status\": \"supports\", \"note\": \"MacKenzie, A Concise Pahlavi Dictionary p. 57 exactly: 'nab [np | N nawa] grandson.' Found in refs/PHD_pages.txt (line 3638) on the page whose running head reads 'murd    57    nāmčišt' — so Nourai's page number is exact. The neighbouring entries on the same page are 'nabānazdišt [nb'nzdšt = Av. nabānazdišta-] next of kin', 'nāf [n'p | M n'p] family' and '*naft [npt'] descendant'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (Glossary) s.v. nap (refs/NYB_vol2_glossary.txt line 2642)\", \"stance\": \"supports\", \"note\": \"'nap [npy] grandson HajB:4. ŠPrs:8. — Nom. sg. *napā of Av. (1039) NP navah < *napak.' Nyberg reads the word nap (unvoiced) and derives the New Persian form from a suffixed *napak; the Parthian equivalent he gives s.v. is 'puhrē-puhr [pwhrypwhr] grandson HajA:4, ŠPrth:7, corresponding to Prs nap'.\"},\n            {\"src\": \"PHD\", \"where\": \"p. 57\", \"stance\": \"supports\", \"note\": \"see ref_check — MacKenzie is both Nourai's citation and the standard Middle Persian dictionary.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien no. 1047, pp. 102-103 (refs/HUB.txt leaf 112-113)\", \"stance\": \"supports\", \"note\": \"'Die Pehleviform nap (geschrieben nap, Hajiabād-Inschrift Z. 4), zu der np. nava = jüd.-tat. newe \\\"Enkel\\\" (Miller p. 74) aus phl. *napak gehört, geht auf den ap. Nominativ napā zurück' — Hübschmann derives the Pahlavi form from the OP nominative, exactly as reconstructed above.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"naveh «نوه» : grandchild; nabas «نَبَس ( نَبَسه )» : daughter's child\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"نوه naveh/nava 'grandchild' is the direct continuant of MP nap/nab: Hübschmann (Pers. Stud. no. 1047) sets out the whole set — 'np. nava … aus phl. *napak gehört, geht auf den ap. Nominativ napā zurück; np. navāda = phl. *napātak auf den ap. Acc. *napātam = zd. napātəm; np. navāsa (unbelegt) auf einen ap. Acc. *napātram (vgl. zd. naptārəm) zurück' — i.e. the four Persian words in this box go back to three different Old Iranian case/stem forms of the same word: نوه < *napak (nominative napā), نواده < *napātak (oblique napāt-), نواسه/نواشه < the r-stem naptar-, and نبیره from a Pahlavi *napīra/navīrak (Mo'in, in his footnote to Borhān-e Qāteʿ, p. 2117, citing Bharucha p. 323 and Darmesteter). The single regular sound change that makes all of them look alike is Old Iranian -p- > NP -v- between/after vowels (Hübschmann §67 lists this word among his examples: 'navāda \\\"Enkel\\\" neben nabasa (oben p. 103) und nabīra, ap. *napāt-, nom. napā'), with -k > -h in نوه. The second word نَبَس / نَبَسه nabas(e) 'daughter's child' is the same word with the -b- variant of that alternation: Dehkhodā calls نبسه 'مبدل و مخفف نواسه' (an altered, shortened نواسه), and Mo'in's footnote to Borhān s.v. نبسه (p. 2115) gives the chain 'نواسه navāsa (در خراسان مستعمل است) … نواسی → نبسه', citing Bahār's Sabk-šenāsī II 79. Borhān-e Qāteʿ itself, p. 2115, has both headwords — 'نَبَس … دخترزاده را گویند' and 'نَبَسه … بمعنی نبی است که دخترزاده باشد' — and Mo'in's footnote there quotes precisely the Amīr Khosrow Dehlavī couplet that Nourai reproduces ('صفت ذات او همین نه بس است / که رسول خدای را نبس است', in praise of Imām Hosayn, from Farhang-e Neẓām). So every word in the box is real, Persian, correctly glossed and correctly attached to the Pahlavi parent. Two small caveats: the arrow is drawn from Pahlavi nab, but نواده and نواسه strictly descend from the oblique and r-stem forms rather than from the nominative-based nab; and Nourai's page reference BQT:2117 is the نبیر/نبیره page, while نبس/نبسه stands two pages earlier at BQT:2115.\",\n          \"derivation_fa\": \"«نوه» بازماندهٔ مستقیم فارسی میانهٔ nap/nab است. هوبشمان در «مطالعات فارسی» (شمارهٔ ۱۰۴۷، ص ۱۰۲–۱۰۳) هر چهار واژهٔ این جعبه را از سه صورت مختلف همان واژهٔ ایرانی باستان می‌گیرد: «نوه» از پهلوی *napak (از فاعلی napā)، «نواده» از پهلوی *napātak (از ستاک غیرفاعلی napāt-)، «نواسه/نواشه» از ستاکِ ‑r‑دار naptar- (پارسی باستان *napātram)، و «نبیره» از پهلوی *napīra/navīrak (معین در حاشیهٔ برهان قاطع ص ۲۱۱۷، به نقل از بهروچا و دارمستتر). دگرگونی آوایی کلیدی، بدل شدن «پ» ایرانی باستان به «و» در فارسی نو است — هوبشمان در بند ۶۷ همین واژه را در فهرست نمونه‌ها می‌آورد: «navāda در برابر nabasa و nabīra، پارسی باستان *napāt-، فاعلی napā» — و افتادن ‑k پایانی به ‑ه در «نوه». واژهٔ دوم، «نَبَس / نَبَسه»، همان واژه با ابدال «و» به «ب» است: دهخدا نبسه را «مبدل و مخفف نواسه» می‌داند و معین در حاشیهٔ برهان (ص ۲۱۱۵) زنجیرهٔ «نواسه (در خراسان مستعمل است) ← نواسی ← نبسه» را به نقل از سبک‌شناسی بهار (ج ۲ ص ۷۹) می‌آورد. خودِ برهان قاطع در ص ۲۱۱۵ هر دو سرواژه را دارد و همان بیت امیرخسرو دهلوی را که نورایی نقل کرده در حاشیه آورده است. پس ادعای نورایی درست است؛ فقط دو نکتهٔ کوچک: «نواده» و «نواسه» به‌دقت از nab (صورت فاعلی) نمی‌آیند بلکه از صورت‌های دیگرِ همان واژه‌اند، و ارجاع BQT:2117 صفحهٔ «نبیره» است، نه «نبس» که در ص ۲۱۱۵ آمده.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%88%D9%87\",\n            \"https://abadis.ir/fatofa/%D9%86%D8%A8%D8%B3%D9%87/\",\n            \"https://abadis.ir/fatofa/%D9%86%D9%88%D9%87/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2117\", \"status\": \"partial\", \"note\": \"Borhān-e Qāteʿ p. 2117 (incoming/BQT/BQT_v4_pages.txt leaf 199, tagged '[pdf page 200]', printed = pdf + 1917) is the نبی / نبیذ / نبیر / نبیره page: 'نبیره، بروزن صغیره، بمعنی فرزندزاده باشد عموماً - و پسرزاده را گویند خصوصاً؛ و بمعنی دخترزاده را هم گفته‌اند', with Mo'in's footnote 9 'پهلوی napīra (navīrak) «بهروچا ص ۳۲۳» از ریشهٔ nap (اوستایی napāt بمعنی فرزندزاده) … [رک: نواده، نوه، ناف]'. So p. 2117 supports نبیره (one of Nourai's script_extra words) and the Pahlavi→Persian link, but it is NOT the page for نبس/نبسه: those two headwords, with the Amīr Khosrow verse Nourai prints, are on p. 2115 (leaf 197, '[pdf page 198]'): 'نبس - بفتح اول و ثانی بر وزن هوس، دخترزاده را گویند … نبسه - … بمعنی نبی است که دخترزاده باشد … و بعضی گویند پسر دختر است که نبیره خوانند', footnote 'نواسه navāsa (در خراسان مستعمل است) (فرزند نوه) «فرهنگ نظام»؛ نواسی ← نبسه' and footnote 'صفت ذات او همین نه بس است / که رسول خدای را نبس است. امیرخسرو دهلوی در منقبت امام حسین. «فرهنگ نظام»'. Substance supported, page number off by two.\"},\n            {\"ref\": \"BQT:2208\", \"status\": \"supports\", \"note\": \"Borhān-e Qāteʿ p. 2208 (BQT_v4_pages.txt leaf 290, tagged '[pdf page 291]', 291+1917 = 2208): 'نوه - بفتح اول و ثانی، نبیره است که فرزندزاده باشد', with Mo'in's etymological footnote 8: 'همریشهٔ نواده، نبیره (م.). کردی nevî (فرزندزاده (پسر))؛ nevî «ژابا ص ۴۲۵»، سانسکریت و پارسی باستان napāt، اوستا napāt، … (ناف)، لاتینی nepos، بشتها ۷ ص ۹ و ج ۱۰'. This is precisely Nourai's arrow — نوه ← OP/Av. napāt-, cognate Lat. nepos.\"},\n            {\"ref\": \"HRN:234\", \"status\": \"supports\", \"note\": \"Horn, Grundriss der neupersischen Etymologie no. 1047, p. 234 (refs/HRN.txt leaf 255; leaf = printed + 21, and the page-foot numeral '— 235 —' appears at the end of the following entry): 'newāde \\\"Enkel\\\", newāse, newa (vergl. newāzade), nebīre, nehīr (Šāhn. I, 119 Vers 995). ap. napāt- \\\"Enkel\\\"; aw. napāt-; ai. nápāt. kurd. nevī, nevū, nehvō \\\"Enkel\\\"; afγ. LW. nwasai; bel. LW. nawasay; wāχ. napūs, sar. nabūs, šiγn. nabōs, nebōs.' Horn covers نوه، نواده، نواسه، نبیره (all four of Nourai's Persian forms) but does NOT list نبس.\"},\n            {\"ref\": \"IEC:836\", \"status\": \"supports\", \"note\": \"Mann p. 836 s.v. nepóts: 'Per. navade, id. beside nave, navāse, id., of various dial. origin' — Mann's phrase 'of various dial. origin' is the same observation Hübschmann makes about the different case-forms behind نوه/نواده/نواسه.\"},\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Fārsi, s.v. نوه: 'فرزندزاده، نبیره' (read via abadis.ir/fatofa/نوه/, archived); s.v. نبسه: 'نوه، فرزندزاده' (abadis.ir/fatofa/نبسه/, archived), where Dehkhodā adds 'مبدل و مخفف نواسه است'. Nourai cites MON without a page; the entries exist and say what he says.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien no. 1047 pp. 102-103 and §67 p. 176 (refs/HUB.txt leaves 112-113, 186)\", \"stance\": \"supports\", \"note\": \"'np. nava = jüd.-tat. newe \\\"Enkel\\\" … aus phl. *napak … geht auf den ap. Nominativ napā zurück; np. navāda = phl. *napāt'ak auf den ap. Acc. *napātam = zd. napātəm; np. navāsa (unbelegt) auf einen ap. Acc. *napātram (vgl. zd. naptārəm) zurück. Daneben nahasa \\\"Enkel\\\" JRAS. 1894, 489'; and in the sound-law section §67 (Ap. p = np. v und b): 'navāda \\\"Enkel\\\" neben nabasa (oben p. 103) und nabīra, ap. *napāt-, nom. napā'. Hübschmann is the source that explicitly licenses BOTH نواسه and نبسه as reflexes of the same Old Iranian form.\"},\n            {\"src\": \"BQT\", \"where\": \"pp. 2115, 2117, 2208 (Mo'in's footnotes)\", \"stance\": \"supports\", \"note\": \"see ref_check — Borhān has all of نبس، نبسه، نبیره، نوه as headwords, with Mo'in's etymological footnotes tying them to Av./OP napāt- and to one another.\"},\n            {\"src\": \"MON\", \"where\": \"vajehyab/abadis entries نوه and نبسه\", \"stance\": \"supports\", \"note\": \"Mo'in glosses نوه 'فرزندزاده، نبیره' and نبسه 'نوه، فرزندزاده'; Dehkhodā s.v. نبسه: 'مبدل و مخفف نواسه است' and glosses it 'دخترزاده', matching Nourai's gloss \\\"daughter's child\\\" for نبس.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Rišehā-ye hendo-orupāyi-ye zabān-e fārsi p. 505 s.v. «نوه، نواده» (incoming/ARY/ARY_pages.txt leaf 504)\", \"stance\": \"supports\", \"note\": \"The comparative table gives 'اوستایی: NAPĀ, NAPĀT / پارسی باستان: NAPĀT, NAPĀ / پهلوی: NAP / لاتین: NEPOS / انگلیسی کهن: NEFA' under the Persian headword نوه، نواده, with a cross-reference to Borhān-e Qāteʿ — the same chain Nourai draws. (Aryanpur uses the word again as his worked example of an inherited kinship term on p. 37.)\"},\n            {\"src\": \"PHD\", \"where\": \"p. 57\", \"stance\": \"supports\", \"note\": \"MacKenzie's own entry already gives the New Persian outcome: 'nab [np | N nawa] grandson'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"nepôs : grandson\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin nepōs, gen. nepōtis 'grandson, grandchild', from PIE nom. *népōts through Proto-Italic *nepōts, with the regular Italic simplification of the final -ts cluster to -s and rhotacism absent (the -t- surfacing in the oblique stem nepōt-). Its meaning is 'grandson, descendant' in Republican Latin; only in post-Augustan Latin (from about the 2nd c. AD, and in Christian Latin regularly) does it also mean 'sister's/brother's son, nephew' — Klein p. 1039: 'L. neputem, acc. of nepos, \\\"grandson\\\", in post-Augustan L. \\\"nephew\\\", in general (poet.) \\\"descendant\\\", which stands for nepot-s'. The feminine neptis 'granddaughter, later niece' is the same root's *neptī- refashioned on the Latin i-stems (Walde-Pokorny II 330), and it is neptis — not nepōs — that gives Vulgar Latin neptia > Old French niece > English niece, which matters for node #6. Nourai's node is correct as far as it goes; the semantic shift 'grandson' → 'nephew' inside Latin is the pivot that makes the English word mean what it does, and the chart does not mention it.\",\n          \"derivation_fa\": \"لاتینی nepōs (اضافی nepōtis) «نبیره، فرزندزاده» بازماندهٔ فاعلی هندواروپایی *népōts است که از راه ایتالیایی آغازین *nepōts آمده و خوشهٔ پایانی ‑ts در آن به ‑s ساده شده، و «ت» تنها در ستاک غیرفاعلی nepōt- پیدا می‌شود. معنای آن در لاتینی دورهٔ جمهوری «فرزندزاده، بازمانده» است و تنها در لاتینی پس از آوگوستوس (سدهٔ دوم میلادی به بعد) معنای «برادرزاده/خواهرزاده» را نیز می‌گیرد — کلاین ص ۱۰۳۹: «nepos «نبیره»، در لاتینی پس از آوگوستوس «برادرزاده»». مؤنث آن neptis «نبیرهٔ دختر، بعدها خواهرزاده» همان *neptī- است که بر قیاس ستاک‌های i بازساخته شده (والده-پوکورنی ج ۲ ص ۳۳۰)؛ و همین neptis — نه nepōs — سرچشمهٔ niece انگلیسی است، نکته‌ای که در گرهٔ ۶ اهمیت دارد. ادعای نورایی درست است، اما تحول معنایی «فرزندزاده» به «برادرزاده» در درون لاتینی، که کلید معنای امروزی واژهٔ انگلیسی است، در نمودار نیامده.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/nephew\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%A9p%C5%8Dts\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1039\", \"status\": \"supports\", \"note\": \"Klein s.v. 'nephew', p. 1039 (refs/KLN_1966.txt leaf 556): 'fr. L. neputem, acc. of nepos, \\\"grandson\\\", in post-Augustan L. \\\"nephew\\\", in general (poet.), \\\"descendant\\\", which stands for nepot-s and is cogn. with OI. nápat, Avestic napāt-, naptar-, OPers. napāt-'. Both the Latin form and its derivation from the IE nominative are exactly as the chart draws them.\"},\n            {\"ref\": \"POK:764\", \"status\": \"supports\", \"note\": \"Pokorny 764: 'Latin nepos, -tis \\\"grandchild, grandson\\\", later also \\\"nephew\\\"' — one of the primary descendants listed under the root, with 'References: WP. II 329 f., WH. II 161 f.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 329\", \"stance\": \"supports\", \"note\": \"'lat. nepōs, -tis \\\"Enkelkind, Enkel\\\", später auch \\\"Neffe\\\"' — same form, same gloss, same later semantic extension.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nepot-\", \"stance\": \"supports\", \"note\": \"'Latin nepos, grandson, nephew, and neptis, granddaughter, niece: NEPHEW, NEPOTISM, NIECE.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 2.48/2.49 and 2.53/2.54, pp. 111, 113\", \"stance\": \"supports\", \"note\": \"Buck's tables put 'Lat. nepos / neptis' under GRANDSON/GRANDDAUGHTER but 'Lat. frātris fīlius (a); sorōris fīlius (b)' under NEPHEW — direct evidence that classical Latin nepōs was primarily 'grandson' and that the Romance 'nephew' sense is secondary (It. nipote, Fr. neveu, Rum. nepot appear in both tables).\"},\n            {\"src\": \"KLN\", \"where\": \"p. 1039 and p. 1041 (s.v. niece)\", \"stance\": \"supports\", \"note\": \"see ref_check; Klein's 'niece' entry supplies the feminine half — 'fr. L. neptis, \\\"granddaughter\\\", in Late L. \\\"niece\\\", which is rel. to nepos, gen. nepotis'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Old French\",\n          \"words\": \"neveu : nephew\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old French neveu (Old North French nevu, also nevod/nevout in the oldest texts) 'grandson, descendant; nephew' continues the Latin ACCUSATIVE nepōtem, the case-form from which almost all French nouns descend: Vulgar Latin nepōtem > nevout/nevod (Latin intervocalic -p- lenited to -v- in Gallo-Romance, and -ō- diphthongised in the tonic syllable) > Old French neveu, modern French neveu. The word is already 'nephew' as well as 'grandson' in Old French because post-Augustan Latin nepōs had acquired that sense. Etymonline: 'nephew … c. 1300, from Old French neveu (Old North French nevu) \\\"grandson, descendant\\\", from Latin nepotem (nominative nepos) \\\"sister's son, grandson, descendant\\\", after c. 150 A.D.' Nourai's citation is simply 'AHD', whose root entry lists Latin nepos → NEPHEW without naming the Old French link explicitly; the link itself is uncontroversial and is spelled out identically by Klein, Skeat and Etymonline.\",\n          \"derivation_fa\": \"فرانسهٔ باستان neveu (در گویش شمالی nevu، و در کهن‌ترین متن‌ها nevod/nevout) «فرزندزاده، بازمانده؛ برادرزاده» بازماندهٔ صورت رایی لاتینی nepōtem است — همان حالتی که بیشترِ نام‌های فرانسوی از آن آمده‌اند. زنجیره: لاتینی عامیانه nepōtem > گالو‑رومی nevout/nevod («پ» میان‌واکه‌ای به «و» نرم شده و «ō» در هجای تکیه‌بر به مصوت مرکب بدل شده) > فرانسهٔ باستان neveu > فرانسهٔ امروز neveu. معنای «برادرزاده» را همان لاتینی پس از آوگوستوس به آن داده بود. اتیمانلاین: «nephew … حدود ۱۳۰۰، از فرانسهٔ باستان neveu، از لاتینی nepotem». نورایی تنها به AHD ارجاع داده که در مدخل ریشه به فرانسهٔ باستان اشاره‌ای نمی‌کند، ولی این حلقه در کلاین و اسکیت و اتیمانلاین یکسان و بی‌اختلاف آمده است؛ پس ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/neveu\",\n            \"https://www.etymonline.com/word/nephew\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. nepot- (refs/AHD_watkins1985.txt line 781) gives 'Latin nepos, grandson, nephew, and neptis, granddaughter, niece: NEPHEW, NEPOTISM, NIECE. [Pok. nepōt- 764.]'. The root entry therefore supports Latin → English NEPHEW but, in the compressed appendix style, never names Old French neveu; the intermediate step has to be taken from the AHD main-dictionary entry or from Klein/Skeat. The online appendix at ahdictionary.com/word/indoeurop.html was fetched but its served text stops before the letter n, so the 1985 Watkins text on disk was used.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 1039 s.v. nephew\", \"stance\": \"supports\", \"note\": \"'ME. neve, neveu, fr. OF. neveu, nevou (F. neveu), fr. L. neputem, acc. of nepos' — the Old French step and its Latin accusative source, exactly as drawn.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary p. 307 s.v. Nephew (refs/SKT.txt leaf 327)\", \"stance\": \"supports\", \"note\": \"'Nephew. (F.-L.) M.E. nevew (nevu). — O.F. neveu, \\\"a nephew\\\"; Cot. — L. nepotem, acc. of nepos, a grandson, also a nephew. + Skt. napāt, a grandson; A.S. nefa, a nephew; G. neffe, nephew.' Skeat also confirms the accusative as the source form.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 2.53 NEPHEW, p. 113\", \"stance\": \"supports\", \"note\": \"Buck's row 'Fr. neveu … ME neve, neveu … NE nephew' documents the same Romance-to-English transmission.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"nephew, niece\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NEPHEW is exactly as drawn: Old French neveu was borrowed into Middle English about 1300 as neve/nevew/nevou, first still meaning 'grandson, descendant'; the unetymological spelling with -ph- (on the model of Latin nepos, whose -p- English scribes restored after 1400) gradually pulled the pronunciation with it, and the sense narrowed to 'brother's or sister's son' in the 17th century. NIECE, however, does not come from OF neveu, which is what the single arrow implies. It comes from the FEMININE half of the root: Latin neptis 'granddaughter' > Vulgar Latin neptia > Old French niece (earlier niepce) > Middle English nece, nyce (c. 1300), also long meaning 'granddaughter, remote female descendant' until about 1600. Klein p. 1041 and Skeat p. 307 both state this route explicitly, and Watkins lists NIECE under Latin neptis, not nepos. So the node's two words are both correct English reflexes of the root box (which does head both Nepôt and Neptis), but niece is misplaced under the Old French neveu node; strictly it should hang from a Latin neptis / Old French niece branch. Verdict 'plausible' for that reason — one word confirmed, one attached to the wrong parent.\",\n          \"derivation_fa\": \"«nephew» درست همان است که نمودار می‌گوید: فرانسهٔ باستان neveu در حدود سال ۱۳۰۰ به انگلیسی میانه به صورت neve/nevew وام گرفته شد و نخست همچنان «فرزندزاده، بازمانده» معنا می‌داد؛ سپس از سدهٔ پانزدهم به بعد کاتبان، به قیاس لاتینی nepos، آن را با ph نوشتند و تلفظ نیز کم‌کم از این املا پیروی کرد، و در سدهٔ هفدهم معنای آن به «پسرِ برادر یا خواهر» محدود شد. اما «niece» از neveu نمی‌آید — چیزی که کمانِ یگانهٔ نمودار به آن اشاره می‌کند. این واژه از نیمهٔ مؤنث ریشه می‌آید: لاتینی neptis «نبیرهٔ دختر» > لاتینی عامیانه neptia > فرانسهٔ باستان niece (کهن‌تر niepce) > انگلیسی میانه nece, nyce (حدود ۱۳۰۰) که تا حدود ۱۶۰۰ همچنان «نبیرهٔ دختر» هم معنا می‌داد. کلاین (ص ۱۰۴۱) و اسکیت (ص ۳۰۷) هر دو همین راه را می‌آورند و واتکینز هم NIECE را زیر neptis می‌آورد نه nepos. پس هر دو واژه بازماندهٔ درستِ جعبهٔ ریشه‌اند (که خود هر دو سرواژهٔ Nepôt و Neptis را دارد)، ولی niece زیر گرهٔ نادرست نشسته است و باید از شاخهٔ لاتینی neptis / فرانسهٔ باستان niece بیاویزد. به همین سبب داوری «با احتیاط پذیرفتنی است».\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/nephew\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"The node carries no refs= in the book (refs=None); nothing of Nourai's own to check. The chain was verified against Klein, Skeat and Etymonline instead (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"pp. 1039-1040 s.v. nephew and p. 1041 s.v. niece (refs/KLN_1966.txt leaves 556, 560)\", \"stance\": \"partial\", \"note\": \"nephew: 'ME. neve, neveu, fr. OF. neveu … fr. L. neputem'. niece: 'ME. nece, neyce, fr. OF. niece (F. nièce), fr. VL. neptia (whence also OProvenç. nepsa \\\"niece\\\"), a var. of VL. nepta …, fr. L. neptis, \\\"granddaughter\\\", in Late L. \\\"niece\\\", which is rel. to nepos, gen. nepotis'. Klein confirms nephew's parent but gives niece a different one.\"},\n            {\"src\": \"SKT\", \"where\": \"p. 307 s.v. Nephew / niece\", \"stance\": \"partial\", \"note\": \"'niece. (F.-L.) M.E. nece, nyce. — O.F. niece (F. nièce). — Low L. neptia, a niece. — L. neptis, a grand-daughter, niece; used as fem. of L. nepos (above).' Same finding: niece via neptis/neptia, not via neveu.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nepot-\", \"stance\": \"partial\", \"note\": \"'Latin nepos … and neptis, granddaughter, niece: NEPHEW, NEPOTISM, NIECE' — NIECE is filed under neptis, confirming the separate feminine line.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 2.53/2.54, p. 113\", \"stance\": \"supports\", \"note\": \"'ME neve, neveu / NE nephew' and 'ME nyfte, nece / NE niece' — Buck's ME row for niece is nece (beside the inherited Germanic nyfte), matching the Old French niece route.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary (refs/FSD_vol3.txt)\", \"stance\": \"silent\", \"note\": \"grep -n '^nephew\\\\|^niece' FSD_vol3.txt returns no headword line (the OCR of this volume only yields 'nephew' inside a quotation at line 53448), so Funk & Wagnalls could not be used for this node. WEB_vol1.txt covers only A-M and is likewise silent (grep -n -i '^nephew' WEB_vol1.txt: no hits).\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-07T19:41:50.118Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-360.json (file state is current in your context — no need to Read it back)
```


## [2026-09-07T19:41:53.155Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-360.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 360"
}
```


### [2026-09-07T19:41:56.552Z] TOOL RESULT

```
JSON OK
nodes verified: 6/6
node verdicts: {'transcription_suspect': 1, 'confirmed': 4, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 11, 'not_checked': 2, 'partial': 2}
books consulted: {'partial': 6, 'supports': 17, 'silent': 1} | by book: {'SYN': 4, 'KLN': 3, 'WLD': 2, 'PHD': 2, 'HUB': 2, 'AHD': 2, 'SKT': 2, 'BRT': 1, 'KNT': 1, 'NYB': 1, 'BQT': 1, 'MON': 1, 'ARY': 1, 'FSD': 1}
```


## [2026-09-07T19:42:16.287Z] AGENT

Page 360 done — `data/verification/page-360.json`, `verify_check.py 360` reports 0 PROBLEM lines.

**Counts (PDF 360 / book 330, root "Nepôt, Neptis"; 3 redirect entries skipped)**
- Root verdicts: confirmed 1
- Node verdicts: confirmed 4, plausible 1, transcription_suspect 1 (6/6 nodes)
- Nourai's own refs: supports 11, partial 2, not_checked 2
- Other books consulted: supports 17, partial 6, silent 1 (POK, WLD, AHD/Watkins, IEC, SYN, KNT, BRT, PHD, NYB, HRN, HUB, BQT+Mo'in, MON, ARY, KLN, SKT, FSD/WEB)

**Flagged items**
- `transcription_suspect` — node #1 [Avestan / Old Persian] **naptis** "grand daughter": no such Avestan or Old Persian form. Bartholomae col. 1039, Walde-Pokorny II 329, Buck 2.49 and Klein (s.v. niece) all give Av. **naptī-** (= Skt. naptī-); the -s nominative *neptis* is specifically Latin, refashioned on the i-stems. `error_in: "book"` — the printed page (copied to `data/verification/sources/refs/ocr/BOOK/360.png`) shows "naptis", so the extraction is faithful; Nourai carried his Latin-shaped root label into the Iranian box. napât/napâ in the same node are confirmed exactly (Kent p. 193).
- `plausible` — node #6 [English] **niece**: correct English reflex of the root box, but hung under Old French *neveu*. Klein p. 1041, Skeat p. 307 and Watkins all route it Latin *neptis* > VL *neptia* > OF *niece* > ME *nece*, i.e. it belongs on a separate feminine branch. *nephew* itself is confirmed.
- Page-number slip (not a verdict change) — node #3 `BQT:2117` is Borhān's نبیر/نبیره page; **نبس / نبسه**, with the very Amīr Khosrow couplet Nourai prints, is on **p. 2115**. `BQT:2208` (نوه, with Mo'in's footnote citing Lat. nepos) is exact.
- `not_checked`: `MFL:102` (Oranskij in Keshavarz's Persian translation — only a 5-page image fragment exists online); node #6 has no refs in the book.

**No extraction errors** — the JSON matches the printed page throughout (including نواده ، نبیره ، نواسه ، نواشه and the نَبَس «نَبَسه» script). Useful finding for the owner: Hübschmann (Pers. Stud. 1047 + §67) explains all five Persian forms from three different Old Iranian case/stem forms — نوه < *napak (nom. napā), نواده < *napātak (obl. napāt-), نواسه/نواشه < naptar-, نبیره < MP *napīra, and نبس(ه) as the -b- variant of نواسه (Dehkhodā: «مبدل و مخفف نواسه»).
