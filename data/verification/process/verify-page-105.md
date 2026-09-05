# Verification process log — verify-page-105


## [2026-09-05T14:53:43.145Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 105 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-105.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-105.json. Write /home/sfmqrb/git/rishe/data/verification/page-105.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 105` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T14:53:44.319Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T14:53:45.768Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


## [2026-09-05T14:53:45.780Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-105.txt"
}
```


### [2026-09-05T14:53:45.798Z] TOOL RESULT

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


### [2026-09-05T14:53:45.801Z] TOOL RESULT

```
1	=== PDF page 105 (book page 75) ===
2	--- entry 0 ---
3	ROOT Carya -> redirect to Čirya
4	--- entry 1 ---
5	ROOT Čĕxara -> redirect to Čîxâ
6	--- entry 2 ---
7	ROOT Char -> redirect to Čar
8	--- entry 3 ---
9	ROOT [Chinese] Chiang-yu : soybean oil  (refs KLN:1479; AHD:1237)
10	#1 (parent #0) [Dutch] refs=KLN:1479 | soja : soybean | NOTE: OXF:406 claims this word entered Dutch through Japanese "shôyŭ".
11	  #2 (parent #1) [French] refs=None | 
12	    #3 (parent #2) [Persian] refs=VOP:224 | soyâ «سویا» : soya
13	  #4 (parent #1) [English] refs=OXF:406 | soya, soy
14	--- entry 4 ---
15	ROOT [Chinese] Chou-shu, Shu-shu : millet  (refs SIN:565)
16	#1 (parent #0) [Mongolian] refs=SIN:565 | 
17	  #2 (parent #1) [Persian] refs=MON:2089; BQT:1309 | šošo, šŭšŭ «شوشو» : millet | NOTE: "bagnî" and "baxsom" are juices or wines extracted from seeds
18	--- entry 5 ---
19	ROOT [Pahlavi] Cîrâğ : lamp  (refs PLA:157)
20	#1 (parent #0) [Persian] refs=BQT:626 | čerâğ «چراغ» : lamp, light, illumination, guiding light
21	#2 (parent #0) [Arabic] refs=PLA:157 | ešrâğ : illumination, intuition ; šarq : east (where sun rises) | NOTE: PLA suggests this as a possible derivation but is not certain.
22	  #3 (parent #2) [Persian] refs=FVA:211 | ešrâğ «اشراق» : illumination, intuition ; šarq «شرق» : east (when sun rises) | extra: شارق، استشراق؛ مشرق، مستشرق
23	  #4 (parent #2) [Arabic] refs=AHD:1152 | šarqîyîn : easterners
24	    #5 (parent #4) [Greek] refs=AHD:1152 | Sarakěnos
25	      #6 (parent #5) [Latin] refs=AHD:1152 | Saracěnus
26	        #7 (parent #6) [Old French] refs=AHD:1152 | Saracin
27	          #8 (parent #7) [English] refs=AHD:1152; KLN:1383 | Saracen : an Arab
28	#9 (parent #0) [Aramaic] refs=PLA:157 | 
29	  #10 (parent #9) [Arabic] refs=PLA:157; FVQ:166; SDQ:72 | sîrâj : lamp
30	    #11 (parent #10) [Persian] refs=FVA:188 | serâj «سراج» : lamp
31	
```


## [2026-09-05T14:53:48.820Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-105.json | head -200",
 "description": "Read source JSON for page 105"
}
```


## [2026-09-05T14:53:49.649Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T14:53:50.521Z] TOOL RESULT

```
{
    "pdf_page": 105,
    "book_page": 75,
    "entries": [
        {
            "root": {
                "name": "Carya",
                "redirect": "\u010cirya"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "\u010c\u0115xara",
                "redirect": "\u010c\u00eex\u00e2"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Char",
                "redirect": "\u010car"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Chiang-yu",
                "lang": "Chinese",
                "refs": "KLN:1479; AHD:1237",
                "gloss": "soybean oil",
                "note": "Entered Japanese as \"sh\u00f4y\u016d\""
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Dutch",
                    "refs": "KLN:1479",
                    "words": [
                        {
                            "translit": "soja",
                            "gloss": "soybean",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": "OXF:406 claims this word entered Dutch through Japanese \"sh\u00f4y\u016d\".",
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "French",
                    "refs": null,
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Persian",
                    "refs": "VOP:224",
                    "words": [
                        {
                            "translit": "soy\u00e2",
                            "gloss": "soya",
                            "script": "\u0633\u0648\u06cc\u0627"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 1,
                    "lang": "English",
                    "refs": "OXF:406",
                    "words": [
                        {
                            "translit": "soya, soy",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Chou-shu, Shu-shu",
                "lang": "Chinese",
                "refs": "SIN:565",
                "gloss": "millet"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Mongolian",
                    "refs": "SIN:565",
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "MON:2089; BQT:1309",
                    "words": [
                        {
                            "translit": "\u0161o\u0161o, \u0161\u016d\u0161\u016d",
                            "gloss": "millet",
                            "script": "\u0634\u0648\u0634\u0648"
                        }
                    ],
                    "script_extra": null,
                    "note": "\"bagn\u00ee\" and \"baxsom\" are juices or wines extracted from seeds",
                    "quote": {
                        "text": "\u062e\u0631\u06cc \u06a9\u0647 \u0622\u0628\u062e\u0648\u0631\u0634 \u0632\u06cc\u0631 \u0646\u0627\u0648\u062f\u0627\u0646 \u0639\u0635\u06cc\u0631 - \u0639\u0644\u0641 \u0639\u0635\u0627\u0631\u0647\u0654 \u0628\u064e\u06af\u0646\u06cc \u0648\u064e\u0628\u064e\u062e\u0633\u064f\u0645 \u0648\u0634\u0648\u0634\u0648",
                        "poet": "S\u016dzan\u00ee"
                    }
                }
            ]
        },
        {
            "root": {
                "name": "C\u00eer\u00e2\u011f",
                "lang": "Pahlavi",
                "refs": "PLA:157",
                "gloss": "lamp"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Persian",
                    "refs": "BQT:626",
                    "words": [
                        {
                            "translit": "\u010der\u00e2\u011f",
                            "gloss": "lamp, light, illumination, guiding light",
                            "script": "\u0686\u0631\u0627\u063a"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": {
                        "text": "\u062f\u0631\u0648\u0646\u0647\u0627 \u062a\u06cc\u0631\u0647 \u0634\u062f \u0628\u0627\u0634\u062f \u06a9\u0647 \u0627\u0632 \u063a\u06cc\u0628 - \u0686\u0631\u0627\u063a\u06cc \u0628\u0631\u06a9\u0646\u064e\u062f \u062e\u0644\u0648\u062a \u0646\u0634\u06cc\u0646\u06cc",
                        "poet": "H\u00e2fez"
                    }
                },
                {
                    "id": 2,
                    "parent": 0,
                    "lang": "Arabic",
                    "refs": "PLA:157",
                    "words": [
                        {
                            "translit": "e\u0161r\u00e2\u011f",
                            "gloss": "illumination, intuition",
                            "script": null
                        },
                        {
                            "translit": "\u0161arq",
                            "gloss": "east (where sun rises)",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": "PLA suggests this as a possible derivation but is not certain.",
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Persian",
                    "refs": "FVA:211",
                    "words": [
                        {
                            "translit": "e\u0161r\u00e2\u011f",
                            "gloss": "illumination, intuition",
                            "script": "\u0627\u0634\u0631\u0627\u0642"
                        },
                        {
                            "translit": "\u0161arq",
                            "gloss": "east (when sun rises)",
                            "script": "\u0634\u0631\u0642"
                        }
                    ],
                    "script_extra": "\u0634\u0627\u0631\u0642\u060c \u0627\u0633\u062a\u0634\u0631\u0627\u0642\u061b \u0645\u0634\u0631\u0642\u060c \u0645\u0633\u062a\u0634\u0631\u0642",
                    "note": null,
```


### [2026-09-05T14:53:50.551Z] TOOL RESULT

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
- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt`
- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt`
- **RCH** — J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt`
- **NAT** — C. Berlitz, Native Tongues, New York 1982
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NAT_2005.txt`
- **PEI** — M. Pei, The Families of Words, New York 1962
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PEI.txt`

## Turkic / Mongolian

- **TTS** — H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
- **VIE** — M.A. Sajjadiyyeh, Vazheha-ye Irani dar Zaban-e Engelisi, Bonyad-e Neyshabur 1364/1985
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_sajjadieh1364_parsianjoman.pdf`

## Sanskrit / Hindustani

- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt`
- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt`
- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt`
```


## [2026-09-05T14:53:55.415Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-105.json'))\nprint(json.dumps(d['entries'][5],ensure_ascii=False,indent=1))\n\"",
 "description": "Show entry 5 of JSON"
}
```


## [2026-09-05T14:53:56.897Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','AHD','OXF','VOP','SIN','MON','BQT','PLA','FVA','FVQ','SDQ']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Look up ref metadata"
}
```


### [2026-09-05T14:53:57.097Z] TOOL RESULT

```
{
 "root": {
  "name": "Cîrâğ",
  "lang": "Pahlavi",
  "refs": "PLA:157",
  "gloss": "lamp"
 },
 "nodes": [
  {
   "id": 1,
   "parent": 0,
   "lang": "Persian",
   "refs": "BQT:626",
   "words": [
    {
     "translit": "čerâğ",
     "gloss": "lamp, light, illumination, guiding light",
     "script": "چراغ"
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": {
    "text": "درونها تیره شد باشد که از غیب - چراغی برکنَد خلوت نشینی",
    "poet": "Hâfez"
   }
  },
  {
   "id": 2,
   "parent": 0,
   "lang": "Arabic",
   "refs": "PLA:157",
   "words": [
    {
     "translit": "ešrâğ",
     "gloss": "illumination, intuition",
     "script": null
    },
    {
     "translit": "šarq",
     "gloss": "east (where sun rises)",
     "script": null
    }
   ],
   "script_extra": null,
   "note": "PLA suggests this as a possible derivation but is not certain.",
   "quote": null
  },
  {
   "id": 3,
   "parent": 2,
   "lang": "Persian",
   "refs": "FVA:211",
   "words": [
    {
     "translit": "ešrâğ",
     "gloss": "illumination, intuition",
     "script": "اشراق"
    },
    {
     "translit": "šarq",
     "gloss": "east (when sun rises)",
     "script": "شرق"
    }
   ],
   "script_extra": "شارق، استشراق؛ مشرق، مستشرق",
   "note": null,
   "quote": {
    "text": "چو آفتاب می از مشرق پیاله برآید - زباغ عارض ساقی هزار لاله برآید",
    "poet": "Hâfez"
   }
  },
  {
   "id": 4,
   "parent": 2,
   "lang": "Arabic",
   "refs": "AHD:1152",
   "words": [
    {
     "translit": "šarqîyîn",
     "gloss": "easterners",
     "script": null
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  },
  {
   "id": 5,
   "parent": 4,
   "lang": "Greek",
   "refs": "AHD:1152",
   "words": [
    {
     "translit": "Sarakěnos",
     "gloss": null,
     "script": null
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  },
  {
   "id": 6,
   "parent": 5,
   "lang": "Latin",
   "refs": "AHD:1152",
   "words": [
    {
     "translit": "Saracěnus",
     "gloss": null,
     "script": null
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  },
  {
   "id": 7,
   "parent": 6,
   "lang": "Old French",
   "refs": "AHD:1152",
   "words": [
    {
     "translit": "Saracin",
     "gloss": null,
     "script": null
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  },
  {
   "id": 8,
   "parent": 7,
   "lang": "English",
   "refs": "AHD:1152; KLN:1383",
   "words": [
    {
     "translit": "Saracen",
     "gloss": "an Arab",
     "script": null
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  },
  {
   "id": 9,
   "parent": 0,
   "lang": "Aramaic",
   "refs": "PLA:157",
   "words": [],
   "script_extra": null,
   "note": null,
   "quote": null
  },
  {
   "id": 10,
   "parent": 9,
   "lang": "Arabic",
   "refs": "PLA:157; FVQ:166; SDQ:72",
   "words": [
    {
     "translit": "sîrâj",
     "gloss": "lamp",
     "script": null
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  },
  {
   "id": 11,
   "parent": 10,
   "lang": "Persian",
   "refs": "FVA:188",
   "words": [
    {
     "translit": "serâj",
     "gloss": "lamp",
     "script": "سراج"
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  }
 ]
}
```


### [2026-09-05T14:53:58.729Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

OXF {"title": "J. Speake, Oxford Dictionary of Foreign Words and Phrases, New York 1997", "edition_found": "1997 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/oxforddictionary00spea ; isbn_9780965016070 (lending) ; Google Nvu17oLIQNgC = 2008 2nd ed. preview only", "identifier": "oxforddictionary00spea (also isbn_9780965016070)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search ?q=<word>.", "notes": "RE-SEARCH 2026-09: borrowable only."}

VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}

SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "loo

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

SDQ {"title": "A. Siddiqi, Studien über die persischen Fremdwörter im klassischen Arabisch, Göttingen 1919", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/studienberdiep00sidd", "identifier": "studienberdiep00sidd", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SDQ.txt", "page_offset": "leaf = printed + 14..15 (e.g. leaf 16 = p.1/2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Arabic words in transliteration
```


## [2026-09-05T14:54:15.437Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i -m5 'chiang-yu\\|shoyu\\|shôyŭ' KLN_1966.txt KLN_1971.txt AHD_watkins1985.txt 2>/dev/null | head -20\necho \"=== soja/soy in KLN\"\ngrep -n -i -m8 '^soy\\|soy-bean\\|soya' KLN_1966.txt | head -20",
 "description": "Grep Klein for soy"
}
```


### [2026-09-05T14:54:15.515Z] TOOL RESULT

```
KLN_1966.txt:36036:sowens,  n.  pi.,  porridge  made  from  the  bran  or husks  of  oats.  —  Gael,  siighan,  name  of  the  liq¬ uid  used  to  make  sowens,  fr.  siigh,  ‘juice’, which  is  cogn.  with  OE.  socian,  ‘to  soak’,  sucan, ‘to  suck'.  See  soak,  suck, sown,  pp.  of  sow.  —  ME.  sowe(n),  fr.  OE.  ge- sdwen,  pp.  of  sawan.  See  sow,  v. soy,  n.,  1)  a  Chinese  or  Japanese  sauce  for  fish made  from  soybean;  2)  soybeans.  — Jap.  shoyu, fr.  Chin,  chiang-vu,  lit.  ‘soybean  oil", soybean,  soya-bean,  n.  —  See  prec.  word, sozin,  n.,  protein  defending  the  animal  body against  bacteria  and  their  toxic  products ( biochem .)  —  Coined  fr.  Gk.  aoj^civ,  ‘to  save’. See  Soter  and  -in.
KLN_1971.txt:227271:made from soybean ; 2) soybeans. — Jap. shoyu, 
KLN_1971.txt:227272:fr. Chin, chiang-yu, lit. ‘soybean oil’, 
=== soja/soy in KLN
11531:—  ModL.,  fr.  Gk.  Siijxxxo;,  ‘teasel’,  rel.  to  Soya, ‘thirst’,  &u})7)v,  ‘to  thirst’;  so  called  in  allusion to  the  water  contained  in  the  cup-shaped  bases of  the  leaves.  See  dipsosis.
35905:Derivative:  somnolent-ly,  adv. son,  n.  —  ME.  sune,  sone,  fr.  OE.  sunu,  rel.  to OS.,  OFris.  sunu,  ON.  sour,  Dan.  sen,  Swed.  son, MDu.  sone,  Du.  zoon,  OHG.  sum,  sun,  MHG. sun,  G.  Sohn,  Goth,  sunus,  ‘son’,  and  cogn.  with OI.  suniih,  Avestic  hunush,  OSlav.  synu,  Lith. sunus,  ‘son’,  and — without  n-formativc  ele¬ ment — with  Toch.  B  soya,  A  se,  Gk.  ui6?,  ‘son’, Arm.  ustr,  ‘son’  (influenced  in  form  by  dustr, ‘daughter’),  OI.  sulah,  ‘son’,  sute,  siyate,  savati, ‘begets,  procreates’,  OIr.  suth  (for  su-tu),  ‘fetus’. All  these  words  derive  fr.  I.-E.  base  *seu-,  *su-, ‘to  bear,  bring  forth ;  birth’, sonance,  sonancy,  n.  —  Formed  from  next  word with  suff.  -ce,  resp.  -cy.  Cp.  assonance,  conso¬ nance,  dissonance,  resonance, sonant,  adj.  and  n.  —  L.  sonans,  gen.  -antis,  pres, part,  of  sonare,  ‘to  sound’,  which  stands  for *swenare  and  is  rel.  to  sonus  (for  *swonos), ‘sound’,  fr.  base  *swen-,  ‘to  sound'.  See  sound, ‘noise’,  and  cp.  assonant,  consonant,  dissonant, resonant,  resound,  sonata,  sonnet,  sound,  ‘noise’, and  the  second  element  in  unison.  For  the  ending see  suff.  -ant.
36036:sowens,  n.  pi.,  porridge  made  from  the  bran  or husks  of  oats.  —  Gael,  siighan,  name  of  the  liq¬ uid  used  to  make  sowens,  fr.  siigh,  ‘juice’, which  is  cogn.  with  OE.  socian,  ‘to  soak’,  sucan, ‘to  suck'.  See  soak,  suck, sown,  pp.  of  sow.  —  ME.  sowe(n),  fr.  OE.  ge- sdwen,  pp.  of  sawan.  See  sow,  v. soy,  n.,  1)  a  Chinese  or  Japanese  sauce  for  fish made  from  soybean;  2)  soybeans.  — Jap.  shoyu, fr.  Chin,  chiang-vu,  lit.  ‘soybean  oil", soybean,  soya-bean,  n.  —  See  prec.  word, sozin,  n.,  protein  defending  the  animal  body against  bacteria  and  their  toxic  products ( biochem .)  —  Coined  fr.  Gk.  aoj^civ,  ‘to  save’. See  Soter  and  -in.
```


## [2026-09-05T14:54:17.453Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SIN millet shu\"\ngrep -n -i -m20 'shu-shu\\|chou-shu\\|šušu\\|shushu' SIN.txt | head -20\necho \"=== SIN 565 leaf\"\nawk 'BEGIN{RS=\"\\f\"} NR==393' SIN.txt | head -60",
 "description": "Grep Sino-Iranica for millet"
}
```


### [2026-09-05T14:54:19.098Z] TOOL RESULT

```
=== SIN millet shu
=== SIN 565 leaf
 safe-conduct,  permits  of  requisition,  according  to the  rank  of  the  bearer,  made  of  silver,  brass,  iron,  etc.  They  were taken  over  by  the  Mongols  from  the  Liao  and  Kin,4  and  are  mentioned by  Rubruck,  Marco  Polo,6  and  Rasid-eddin.
27.  Titles  like  wan  :£  ("king,  prince"),  Vai  wan  J£  zE  ("great prince"),  kao  wan  iti  EE  ("great  general"),  Vai  huJ^Jn  ("empress"), fu  Sen  (Persian  fucln)  ;£  A  (title  for  women  of  rank),  and  kun  cu fe  ^  ("princess")  were  likewise  adopted  in  Mongol  Persia.6  Persian jinksdnak,  title  of  a  Mongol  prefect  or  governor,  transcribes  Chinese Ven  sian  2&  $[  ("minister  of  state ")A
28.  From  Turkish  tribes  the  Persians  have  adopted  the  word  toy
1  T'oung  Pao,  1916,  p.  481.
2  Ch.  79,  p.  7.
3  Cf.  J.  Tobar,  Inscriptions  juives  de  K'ai-fong-fou,  pp.  78,  86,  96  (note  2).
4  Chavannes,  Journal  asiatique,  1898,  I,  p.  396.
6  Yule's  edition,  Vol.  I,  p.  351,  which  consult  for  a  history  of  the  p'ai-tse;  see, further,  Laufer,  Keleti  Szemle,  1907,  pp.  195-196;  Zamtsarano,  Paiza  among  the Mongols  at  the  Present  Time  (Zapiski  Oriental  Section  Russian  Archceol.  Soc, Vol.  XXII,  1914,  pp.  155-159).
6  E.  Blochet,  Introduction  a  l'histoire  des  Mongols  de  Rashid  Ed-din,  p.  183; and  Djami  el-TeVarikh,  p.  473.  Regarding  the  title  wan,  see  also  J.  J.  Modi,  Asiatic Papers,  p.  251.
7  Cf.  my  notes  in  T'oung  Pao,  1916,  p.  528.
Irano-Sinica — Chinese  Loan-Words  in  Persian  565
(togh)  or  tuy,1  which  designates  the  tassels  of  horse-hair  attached  to  the
points  of  a  standard  or  to  the  helmet  of  a  Pasha  (in  the  latter  case  a
sign  of  rank).    Among  the  Turks  of  Central  Asia,  the  standard  of  a
high  military  officer  is  formed  by  a  yak's  tail  fastened  at  the  top  of  a
pole.    This  is  said  also  to  mark  the  graves  of  saintly  personages.2    In
the  language  of  the  Uigur,  the  word  is  tuk.z  As  correctly  recognized  by
Abel-Remusat,4  who  had  recourse  only  to  Osmanli,  the  Turkish  word
is  derived  from  Chinese  jfl  tu,  anciently  *duk,  that  occurs  at  an  early
l  date  in  the  Cou  li  and  TsHen  Han  £#.   Originally  it  denoted  a  banner
.  carried  in  funeral  processions;  under  the  Han,  it  was  the  standard  of  the
commander-in-chief  of  the  army,  which,  according  to  Ts'ai  Yun  $%  §
(a.d.  133-192),  was  made  of  yak-tails.6    Yak-tails  (Sanskrit  cdmara,
Anglo-Indian  chowry)  were  anciently  used  in  India  and  Central  Asia  as
i  insignia  of  royalty  or  rank.6
29.  The  Cou  iw7  states  that  in  respect  to  the  five  cereals  and  the :  fauna  Persia  agrees  with  China,  save  that  rice  and  millet  are  lacking
in  Persia.  The  term  "millet"  is  expressed  by  the  compound  iu  lu W?  fflt;  that  is,  the  glutinous  variety  of
```


## [2026-09-05T14:54:23.484Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==394' SIN.txt | head -40",
 "description": "SIN page 566"
}
```


### [2026-09-05T14:54:25.178Z] TOOL RESULT

```
Panicum  miliaceum  and  the glutinous  variety  of  the  spiked  millet  (Setaria  italica  glutinosa) .  Now, we  find  in  Persian  a  word  &*£«  in  the  sense  of  "millet."  It  remains to  study  the  history  of  this  word,  in  order  to  ascertain  whether  it  might be  a  Chinese  loan-word.
Schlimmer8  notes  erzen  as  Persian  word  for  Panicum  miliaceum.
30.  Persian  (also  Osmanli)  tank  ("a  harp  or  guitar,  particularly played  by  women")  is  probably  derived  from  Chinese  Zen  ^  ("a harpsichord  with  twelve  brass  strings").
31.  One  of  the  most  interesting  Chinese  loan-words  in  Persian  is xutu  (khutu),  from  Chinese  ku-tu  (written  in  various  ways),  principally denoting  the  ivory  tooth  of  the  walrus.    This  subject  has  been  dis-
x  In  Sugnan,  a  Pamir  language,  it  occurs  as  tux  (Salemann,  in  Vostocnye  Za- m'atki,  p.  286).
2  Shaw,  Turkl  Language,  Vol.  II,  p.  76.
s  Radloff,  Wort,  der  Turk-Dial.,  Vol.  Ill,  col.  1425.
*  Recherches  sur  les  langues  tatares,  p.  303.
*  See  K'an-hi  sub  jfe.
8  Yule,  Hobson-Jobson,  p.  214.  Under  the  Emirs  of  the  Khanat  Bukhara there  was  the  title  toksaba:  he  who  received  this  title  had  the  privilege  of  having  a tug  carried  before  him;  hence  the  origin  of  the  word  toksaba  (Veliaminof-Zernof, Melanges  asiatiques,  Vol.  VIII,  p.  576).  Cf.  also  a  brief  note  by  Parker  (China Review,  Vol.  XVII,  p.  300).
7  Ch.  50,  p.  6.
8  Terminologie,  p.  420.
566  Sino-Iranica
cussed  by  me  in  two  articles.1  Vullers2  gives  no  less  than  seven definitions  of  the  Persian  word:  (i)  cornu  bovis  cuiusdam  Sinensis; (2)  secundum  alios  cornu  rhinocerotis;  (3)  secundum  alios  cornu  avis cuiusdam  permagnae  in  regno  vastato,  quod  inter  Chinam  et  Aethiopiam situm  est,  degentis,  e  quo  conficiunt  anulos  osseos  et  manubria  cultri et  quo  res  venenatae  dignosci  possunt;  (4)  secundum  alios  cornu  ser- pentis,  quod  mille  annos  natus  profert;  (5)  secundum  alios  cornu viperae;  (6)  secundum  alios  cornu  piscis  annosi;  (7)  secundum  alios dentes  animalis  cuiusdam.  Of  these  explanations,  No.  3  is  that  of al-Akfani,  and  the  bird  in  question  is  the  buceros.  No.  4  is  a  reproduc- tion of  the  definition  of  ku-tu-si  in  the  Liao  Annals  ("the  horn  of  a thousand-years-old  snake").  How  the  Persians  and  Arabs  arrived  at the  other  definitions  will  be  easily  understood  from  my  former  dis- cussion of  the  subject.  In  the  Ethiopic  version  of  the  Alexander  Ro- mance are  mentioned,  among  the  gifts  sent  to  Alexander  by  the  king  of China,  twenty  (in  the  Syriac  version,  ten)  snakes'  horns,  each  a  cubit long.3
Meanwhile  I  have  succeeded  in  tracing  a  new  Chinese  definition of  ku-tu.  Cou  Mi  Ml  $?  (1 230-1320),  in  his  Ci  ya  Van  tsa  Pao*  states, "According  to  Po-ki  fS  ^,5  what  is  now  styled  ku-tu  si  #  $§  JP  is a  horn  of  the  earth  (ti  kio  i&  m,  'a  horn  found  underground'?)."  He refers  again  to  its  property  of  neutralizing  poison  and  to  knife-hilts made  of  the  substance.
In  the  edition  of  the  K
```


## [2026-09-05T14:54:37.044Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SIN grep susu/millet\"\ngrep -n -i 'millet' SIN.txt | head -30",
 "description": "Grep SIN for millet"
}
```


### [2026-09-05T14:54:37.089Z] TOOL RESULT

```
=== SIN grep susu/millet
1413:the  reproduction  of  a  foreign  k;  but  the  character  yu  in  transcriptions usually  answers  to  *ut,  ud.  The  whole  theory,  however,  is  exposed  to much  graver  objections.  The  Chinese  themselves  do  not  admit  that yii-kin  represents  a  foreign  word;  nowhere  do  they  say  that  yii-kin  is Persian,  Sanskrit,  or  anything  of  the  sort;  on  the  contrary,  they  regard it  as  an  element  of  their  own  language.  Moreover,  if  yii-kin  should originally  designate  the  saffron,  how,  then,  did  it  happen  that  this  alleged Persian  word  was  transferred  to  the  genus  Curcuma,  some  species  of which  are  even  indigenous  to  China,  and  which,  at  any  rate,  has  been acclimated  there  for  a  long  period?  The  case,  indeed,  is  not  simple,  and requires  closer  study.  Let  us  see  what  the  Chinese  have  to  say  con- cerning the  word  yii-kin.  Pelliot1  has  already  clearly,  though  briefly, outlined  the  general  situation  by  calling  attention  to  the  fact  that  as early  as  the  beginning  of  the  second  century,  yii-kin  is  mentioned  in the  dictionary  Swo  wen  as  the  name  of  an  odoriferous  plant,  offered  as tribute  by  the  people  of  Yu,  the  present  Yu-lin  in  Kwan-si  Province; hence  he  inferred  that  the  sense  of  the  word  should  be  "gold  of  Yu," in  allusion  to  the  yellow  color  of  the  product.  We  read  in  the  Swi  kin lu  *K  %  W  as  follows:  "The  district  Kwei-lin  &  #  M  of  the  Ts'in dynasty  had  its  name  changed  into  the  Yu-lin  district  ^  ^  fP  in  the sixth  year  of  the  period  Yuan-tin  (in  b.c.)  of  the  Emperor  Wu  of  the Han  dynasty.  Wan  Mail  made  it  into  the  Yu-p'ih  district  Wt  ZP.  Yin Sao  J®  S{5  [second  century  a.d.],  in  his  work  Ti  li  fun  su  ki  ife  S  M, f&wE,  says,  'The  Cou  li  speaks  of  the  yii  Zen&K  ('officials  in  charge  of the  plant  yu'),  who  have  charge  of  the  jars  serving  for  libations;  when- ever libations  are  necessary  for  sacrifices  or  for  the  reception  of  guests, they  attend  to  the  blending  of  the  plant  yii  with  the  odoriferous  wine lKan,  pour  it  into  the  sacred  vases,  and  arrange  them  in  their  place.'3 Yii  is  a  fragrant  plant.  Flowers  of  manifold  plants  are  boiled  and  mixed with  wine  fermented  by  means  of  black  millet  as  an  offering  to  the spirits:  this  is  regarded  by  some  as  what  is  now  called  yii-kin  hian W  4£  #  (Curcuma) ;  while  others  contend  that  it  was  brought  as tribute  by  the  people  of  Yu,  thus  connecting  the  name  of  the  plant with  that  of  the  clan  and  district  of  Yii."  The  latter  is  the  explanation
1886:26.  While  rice  is  at  present  a  common  article  of  food  of  the  Persian people,  being  particularly  enjoyed  as  pilau,1  it  was  entirely  unknown in  the  days  of  Iranian  antiquity.  No  word  for  "rice"  appears  in  the Avesta.2  Herodotus3  mentions  only  wheat  as  the  staple  food  of  the Persians  at  the  time  of  Cambyses.  This  negative  evidence  is  signally confirmed  by  the  Chinese  annals,  which  positively  state  that  there  is no  rice  or  millet  in  Sasanian  Persia;4  and  on  this  point  Chinese  testi- mony carries  weight,  since  the  Chinese  as  a  rice-eating  nation  were always  anxious  to  ascertain  whether  rice  was  grown  and  consumed  by foreign  peoples.  Indeed,  the  first  question  a  travelling  Chinese  will ask  on  arrival  at  a  new  place  will  invariably  refer  to  rice,  its  qualities and  valuations.  This  is  conspicuous  in  the  memoirs  of  Can  K'ien, the  first  Chinese  who  travelled  extensively  across  Iranian  territory, and  carefully  noted  the  cultivation  of  rice  in  Fergana  (Ta-yuan),  fur- ther for  Parthia  (An-si),  and  T'iao-ci  (Chaldaea).  The  two  last-named countries,  however,  he  did  not  visit  himself,  but  reported  what  he  had heard  about  them.  In  the  Sasanian  epoch,  Chinese  records  tell  us that  rice  was  plentiful  in  Kuca,  Kasgar  (Su-lek),  Khotan,  and  Ts'ao (Jagucfe)  north  of  the  Ts'un-lin;8  also  in  Si  (Tashkend).6  On  the other  hand,  Aristobulus,  a  companion  of  Alexander  on  his  expedition in  Asia  and  author  of  an  Alexander  biography  written  after  285  B.C., states  that  rice  grows  in  Bactriana,  Babylonia,  Susis,  and  in  lower Syria;7  and  Diodorus8  likewise  emphasizes  the  abundance  of  rice  in  Susi-
3850:29.  The  Cou  iw7  states  that  in  respect  to  the  five  cereals  and  the :  fauna  Persia  agrees  with  China,  save  that  rice  and  millet  are  lacking
3851:in  Persia.  The  term  "millet"  is  expressed  by  the  compound  iu  lu W?  fflt;  that  is,  the  glutinous  variety  of  Panicum  miliaceum  and  the glutinous  variety  of  the  spiked  millet  (Setaria  italica  glutinosa) .  Now, we  find  in  Persian  a  word  &*£«  in  the  sense  of  "millet."  It  remains to  study  the  history  of  this  word,  in  order  to  ascertain  whether  it  might be  a  Chinese  loan-word.
3942:11.  Mongol  bodso,  an  alcoholic  beverage  made  from  barley-meal or  milk,  is  connected  by  Kovalevski  in  his  Mongol  Dictionary  with Persian  boza,  a  beverage  made  from  rice,  millet,  or  barley.
4830:506,  507,  509,  547.  559- Miao  tribes,  familiar  with  Ricinus,  404. Migeon,  G.,  492. Miklosich,  F.,  501. Miller,  W.,  256,  415. Millet,  in  Persia  and  China,  565. Min  siao  ki,  536. Min  Su,  394,  396. Min  hiah  p'u,  363. Min  hwan  tsa  lu,  517. Min  Si,  264,  390,  562. Min  wu  ci,  256  note  6. Mint,  193,  194,  198.
```


## [2026-09-05T14:54:39.916Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON شوشو\"\ngrep -n 'شوشو' MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10\necho \"=== BQT شوشو\"\ngrep -n 'شوشو' BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head -10\necho \"=== بگنی\"\ngrep -rn 'بگنی\\|بخسم' BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null | head -5",
 "description": "Grep Persian dictionaries for shusho"
}
```


### [2026-09-05T14:54:40.033Z] TOOL RESULT

```
=== MON شوشو
=== BQT شوشو
BQT_v1_pages.txt:4099:۴ الب مطا لب متن بر هانمهم و مفشوشو ناقص‌مینما ید.
incoming/BQT/BQT_v3_pages.txt:7703:‏علف مصارة بگنی‌وبخم وشوشو.
=== بگنی
incoming/BQT/BQT_v3_pages.txt:7703:‏علف مصارة بگنی‌وبخم وشوشو.
```


## [2026-09-05T14:54:45.926Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=7703 && /\\[pdf page/ {p=$0; n=NR} END{}' incoming/BQT/BQT_v3_pages.txt\ngrep -n '\\[pdf page' incoming/BQT/BQT_v3_pages.txt | awk -F: '$1<7703' | tail -3\necho \"--- context ---\"\nsed -n '7680,7730p' incoming/BQT/BQT_v3_pages.txt",
 "description": "Locate BQT v3 page for shusho"
}
```


### [2026-09-05T14:54:47.436Z] TOOL RESULT

```
7480:[pdf page 98]
7555:[pdf page 99]
7633:[pdf page 100]
--- context ---
‎Yow‏ شوغاره ( ۲ ) است که جای خوایدن

‎. ‏شوغار‎ : dhe (x)

‏۸ شاشك « رشیدی» «شوشك » ‎hy‏ چپار رودی باشد . فرخی (سیتانی) کوید :

‏گهی سماع زمالی وگاه بربط وچنك

‏۴ از چینی ‎shU‏ (ارزن) . ره :
خری که آبخورش زبر ناودان‌صیر

‏۴ شفده ‎(pe)‏ شیوشه («م.) .

‏۴ - دمد لاله از ‎De Leys‏ من

‏خواجوی ‎SOS‏ .۶ رشیدی».
بسته کف «ست و کف پای‌شوغ

‏کهی چناله وطنبور وشوشك ‎Wing‏ . »
« لت فری ‎LOWE‏

‎Laufer , Sino - Iranica, p . 565

‏علف مصارة بگنی‌وبخم وشوشو.
سوزلی سمرقندی.«رشیدی*. ۰

‏کیا روید ازکوشة خاك من .

‎are ©‏ )4.0( « لت فری ۰۲۳۷ شوغه ‎Gow)‏ :
پشت فروچفته(خفته . دهضدا) چوپشت شمن.

‏کایی مروزی. «لفت‌فری۲۳۳» رفس چاپ هرن ص۸ه.

‎(ee) ‏سر‎ ٩

‎al - ۷‏ آنجاکه شب کنرانند . محل بیتونه ‎a‏ شبفا ‎Com)‏

‏? رشیدی ‎(pn poem glare‏ « رشیدی » ۳ شوگاء (ه.م.) = شوفار(ه.م.) ‏ شوفاره(«.م.)

‏شوغاه ‎Cem)‏ .
‎ye ۸‏ ک رکه دزد کیرد قصد شوقا

‎dy - ٩‏ : شوغا. شوفاره,شوفاه» شوگاه.

‎. ‏شبان افند بنوضا‎ jail Obs
+ ‏رشیدی»‎ « ahd
. ‏راك :شوغا» شوفاه , شوغار» شوگار‎ VO

‏۱ - ره : شوفا : « الاستپساد , شوغاه ساختن کوسفند » « ناح‌المصادر ‎Fee‏
[pdf page 101]
۳
```


## [2026-09-05T14:54:55.877Z] TOOL CALL #13: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\n\"",
 "description": "BQT offsets"
}
```


### [2026-09-05T14:54:57.791Z] TOOL RESULT

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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209",
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


## [2026-09-05T14:55:07.350Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA offset\"\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))['PLA']\nprint(d.get('page_offset'), '|', d.get('lookup_hint'))\n\"\necho \"=== PLA cirag/siraj\"\ngrep -n -i 'čirāγ\\|cirag\\|sirāǧ\\|sirag\\|Leuchte\\|širāǧ' incoming/PLA/PLA_pages.txt | head -20",
 "description": "Grep Asbaghi for cirag"
}
```


## [2026-09-05T14:55:09.174Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ siraj\"\ngrep -n -i 'sirāj\\|siraj\\|sirāǧ' FVQ_pages.txt | head -20\necho \"=== SDQ siraj\"\ngrep -n -i 'sirāǧ\\|siraj\\|sirag' SDQ.txt | head -20",
 "description": "Grep Jeffery and Siddiqi for siraj"
}
```


### [2026-09-05T14:55:09.360Z] TOOL RESULT

```
=== PLA offset
301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
=== PLA cirag/siraj
1350:gi - ’isräß:                          "erleuchten"                          5. glu siraß.
1558:ae             - ”idräg:             "erleuchten",              eventuell                 aus    dem   pers.           Le        tirag   s.    siräß.
8869:sw    -       sadaq’:        "terleuchtete                Festnacht"              aus    pers.     «..   sade   em.»           sad     7,
8888:Sse-          sadag? : "erleuchtete                       Festnacht"              _      sadaq
8910:&--        siräg:           "Laterne,                 Lampe,             Leuchter;           Sonne"       aus      pers.    elr Siräg         mp.
10139:aan            -       Sam°dän:                 "Leuchter"               pers.           11             eigentlich          nur   eine     arabisch-
```


### [2026-09-05T14:55:09.418Z] TOOL RESULT

```
=== FVQ siraj
=== SDQ siraj
```


## [2026-09-05T14:55:15.009Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1540,1575p' incoming/PLA/PLA_pages.txt\necho \"########\"\nsed -n '8895,8935p' incoming/PLA/PLA_pages.txt",
 "description": "Read PLA context"
}
```


### [2026-09-05T14:55:15.066Z] TOOL RESULT

```
1.    al-Marfa°                         Ss.       Ve,           al-MuCarrab              Ss.   Vv
2.    Brockelmann                             s.          v.
3.    LD.             s.          v.
4.    Mackenzie                         S.        v.
5. al-Marfa®                            s. v.,                  Mu°&am al-Wasit                 s. v.
6.    Nyberg                      Bd.     IIs.                  v.
7.    ebda.
8.    Brockelmann                             s.          v.
9. LD.                s. v.,              ’insäb                    s. v.
10.       Addai                   Scher           s.       v.
11.       FN.             s.       v.
"ußturgäz                                                                    21                                                               > asatin

JuzEr - ’ußturgäz:                              "Distel"         pers.       1, mand.             adtargan             (p. or)                2,

ob ri - "ußturgän = "ußturgäz s. "usturpäz °.

ae             - ”idräg:             "erleuchten",              eventuell                 aus    dem   pers.           Le        tirag   s.    siräß.

     .   4                                                                        .

zol-
2                 ’ asres
                    aßraz:       "Löwe"           aus    dem     pers.        „;.
                                                                             om           Sarza
                                                                                          BAI2a     "wild"         4           wahrscheinlich       aus
              dem    mp.»v Sagr "Löwe".

     Pr]
vi - "aßras:                     "wild"           = ’alraz s. ’aßraz 5

 Z1- ’ubdag:
Gr'-  ussag                     "Gumma Ammoniat                  pers.       © ?, syr.“ol                  7.

     35
########
 1.   Fremdwörterbuch                     s.    v.
 2. Muhlt s. v.,                    Addai       Scher        s. v.
3.    al-Mu’arrab                 s.     v.
4. Mubit          s.     v.,        Addai       Scher        s.    v.
 5.   Wahrmund
            s. v.
6.    ebda.
7.    Mackenzie              8.     v.
8.    Addai       Scher           s.     v.
9.    Wahrmund           s.       v.
saräbil                                                                          157                                                         sarbäl


Je              saräbil:                 Pl.     v. Si. sarbäl                   q. v.

&--        siräg:           "Laterne,                 Lampe,             Leuchter;           Sonne"       aus      pers.    elr Siräg         mp.
       „Ja Liräg                    1 aram.,               syr.          Ale,        mand.     Sraga 2,
      siräß:           das          Wort        siräg          tritt          mehrmals        im    Qur’än         auf,    Fraenkel         zufolge
      ist       das        Wort          aus     pers.          eir &iräg              entlehnt          worden.      Die     aram.        syr.     Form
      heißt Yo=®.
      Vielleicht                    stammt auch das Wort.y- Sarg "Orient"                                            vom fLe&irag.

Glan       -    sarädig:                  "Türvorhang"                   befindet        sich       auch      im    Mandäischen,            Sein
      pers.          Ursprung                  (vgl.       Nöldeke             mand.     Gramm.          S.   31)    geht     bis     zu    pers.
      L              sarädar               zurück.             *.
      Jeffery              nimmt           dagegen             die       Abteilung           aus    pers.          s»z 1    saräparde             als
      richtig              an mp.»                        sara          ap.          sarasa        5, mand.         sradga,      jüd.       p. 7419 v®


bie _ sirät                = sirat              q.    v.


Jrls - saräwil:                          PL. v. Öl.                     sarwäl       gq. v.

Wh» - saräwin                        = saräwil                 q. v.

sl“- saräy:                 "Schloß,                 Palast"             7 MP.           ed»          sräitan              ap.   srasa.
      Dtsch.           Serail:                 "Palast"             <     pers.       >>tk.         8,


Li     - säräayä:                   fem.        v.ccl- saray                   a. v.
```


## [2026-09-05T14:55:34.679Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ leaf 183 (p.166)\"\nawk 'BEGIN{RS=\"\\f\"} NR==183' FVQ_pages.txt | head -50",
 "description": "FVQ page 166"
}
```


## [2026-09-05T14:55:36.250Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SDQ leaf 86/87\"\nawk 'BEGIN{RS=\"\\f\"} NR==87' SDQ.txt | head -40\necho \"##### PHD cirag\"\ngrep -n -i 'čirāγ\\|cirag\\|čirāġ\\|lamp' PHD.txt PHD_mackenzie.txt | head -20",
 "description": "SDQ page 72 and PHD lamp"
}
```


### [2026-09-05T14:55:44.465Z] TOOL RESULT

```
=== FVQ leaf 183 (p.166)
FOREIGN VOCABULARY OF THE QUR*AN 165
Persian it passed directly into Arabic. Grimme, ZA, xxvi, 164, 165,
suggests S. Arabian influence, but there seems nothing to support
this.
IxxxSi, 7, 8.
The early authorities differed widely as to what the Sijjln of this
eschatological passage might be. It was generally agreed that it
was a place, but some said it meant the lowest earth <U> LJ' (j*J)* '
or a name for hell, or a rock under which the records of men's deeds
are kept, or a prison. 1 The Qur'an itself seems to indicate that it
means a document *j5 * ^J, so as-Suyiiti, Mutaw, 46, 2 tells
us that some thought it was a Persian word meaning day (tablet).
Grimme, ZA, xxvi, 163, thinks that it refers to the material on which
the records arc written, and compares with the Eth. ft" 17*1 or
Xrn-1 meaning clay writing tablets. It is very probable, however,
as Noldeke, Sketches, 38, suggested long ago, that the word is simply
an invention of Muhammad himself. If this is so, then *j* * cy UJ
is probably an explanatory gloss that has crept into the text.
Ci- (Suht).
v, 46, 67, 68.
Unlawful.
The reference is to usury and to forbidden foods. It is clearly
a technical term, and the passages, it will be noted, are of the latest
Madinan group.
Sprenger, Leben, iii, 40, n., suggested that it was a technical term
borrowed from the Jews, and there certainly is an interesting parallel
from the Talmud, Shabb, 1406, where PHS? is used in this technical
sense. It is, however, the Syr. lA^O* depravity, corruption, etc.,
1 See Vacca, El, sub voc., who suggests that it was this idea that the word was
connected with /*.- that gave rise to the theory that it was a place in the nethermost
earth where the books were kept, rather than the books themselves.
2 See also Itq, 321.
```


### [2026-09-05T14:55:46.202Z] TOOL RESULT

```
=== SDQ leaf 86/87
 Glied  vor- kommende ^^  (käla)  ^)  entstanden  ist.  [Hier  wäre also    auch   ein   p   an   ein  persisches  Wort   angetreten.
1)  IQutAk.  532;  Ibn  Duraid  (G.  105).  Daß  die  Perser  das .jCjm«.£  von  den  Arabern  als  .jCw^i  übernahmen  (Fraeak.  239),  kann schon  wegen  des  (ji,  nicht  richtig  sein.  Das  .^m*.£  ist  auch  im  Per- sischen tatsächlich  aslcar  gehlieben  und  nicht  etwa  *laskar  oder  *askar geworden.
FN.  (s.  V.)  will  Ji^li  aus  ^^j  „Stück"  ableiten.  Wenn  der Übergang  der  Bedeutung  „Stück",  „Teil" ;  „Abteilung"  —  „Truppe" auch  nicht  unmöglich  ist,  so  bleibt  doch  die  Endung  unerklärt.
2)  Das  arab.  ö  hat  also  nichts  mit  diesem  o  zu  tun,  wie  Fraenkel S.  237  annimmt.
3)  Vgl.  Bemerkungen  von  Andreas  über  ^ÜA^b'  MVAsG.  1807, Heft  I,  S.   124  flg.;  Schwarzl.  130  u.  133.
—     71     —
Die  Gründe  für  die  Entstehung  dieses  c.  sind  nicht  mit Sicherheit  zu  erkennen.  Vielleicht  ist  es  durch  ^  be- einflußt.   L.]
Das  c  in  i^xS^  ist  schon  im  aram.  JIä^.o  (p.  ^\^)  vor- handen. J^*J  (eine  jüngere  Entlehnung)  ^)  ist  womöglich von  den  Persern  selbst  mit  c  geschrieben  worden,  um S^  {^3t.l)  „Rubin",  welches  Wort  übrigens  ins  Arabische übergegangen  war,  von  S^  „rot"  zu  unterscheiden"^).
6.  Persisches  i_j  wird   durch  o  oder   auch  durch  v-j
wiedergegeben:  ^j^^li  (=  p.  ij^J^S),  ^^i  (=  p.  _^^J),  (J^^J> neben  /  ijLj  (=  mp.  parvänak  >  ^^i^^-j) ,    «Ai^-i   neben   uX.i^
(=  p.  cXi-j  „Glanz  des  Schwertes  u.  s.w.").
7.  Eür  persisches  o  erscheint  auch  _b,  vielleicht  ein
1)  Das  Wort  fehlt  bei  Gauhari.
2)  Einige  schreiben,  nach  Gauhari  (s.  v.  Xäa«),  in  medizinischen Schriften  JCäao  für  .Äx*«,  um  es  (wenn  ohne  Punkte  geschrieben)  von jj^nXi  unterscheiden  zu  können.  [Man  darf  jedoch  nicht  vergessen, daß  die  Aussprache  satar  vorgekomme
##### PHD cirag
PHD.txt:300:“гау [c”y | P сер, N ~] lamp.
PHD.txt:2556:lamp čirāy.
PHD_mackenzie.txt:1798:elrAy [cl'" I P cr'g, N ,...,] lamp.
PHD_mackenzie.txt:6956:lamp ciray.                               leopard palang; hunting""'" yoz.
```


## [2026-09-05T14:55:56.104Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ leaf 184\"\nawk 'BEGIN{RS=\"\\f\"} NR==184' FVQ_pages.txt | head -60",
 "description": "FVQ leaf 184"
}
```


## [2026-09-05T14:55:56.594Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SDQ leaf 88\"\nawk 'BEGIN{RS=\"\\f\"} NR==88' SDQ.txt | head -40",
 "description": "SDQ leaf 88"
}
```


### [2026-09-05T14:55:57.712Z] TOOL RESULT

```
=== FVQ leaf 184
166 FOREIGN VOCABULARY OF THE QUR'AN
which gives us a nominal form from which C^t-*- may have been
derived.
x-x x
j*^* (Sahara).
vii, 113, 129 ; xxm, 91.
To enchant, bewitch, use sorcery.
Besides the verb there are used in the Qur'an the nouns j>\**,
plu. "*jz*+* and J^^>-v , vii, 109, 110, etc., sorcerer ; jl_st a great
magician, xxvi, 36 \j>y* enchantment, sorcery, v, 110 ; vi, 7, etc.;
bewitched, x\i\, 50, 103, etc. ; J>^^A bewitched, xxvi, 153, 185.
The verb is denominative, formed either from the noun j**\+* or
, which was the borrowed term.
It would seem that the word came to the Arabs from Mesopotamia,
which was ever to them the home of sorcery and magic (see the
Lexicons under J^y). Zimmern, therefore, 1 would derive it from the
Akk. sdhiru, sorcerer, magician. If this is so it may have been a very
early borrowing direct from Mesopotamia, though a borrowing through
the Aramaic is more probable. 2
*> I"
^W" (Sim;).
xxv, 62 ; xxxiii, 45 ; Ixxi, 15 ; Ixxviii, 13.
A lamp or torch.
The Muslim authorities take it as pure Arabic, not realizing that
the verb from which they derive it is denominative.
Fraenkel, Vocab, 7, pointed out that it was from Aram. JWDttf =
Syr. hr. These forms are, however, borrowed from the Pers.
\j>- and in Fremdw, 95, he suggests that it probably came directly
1 Akkadische Fremdworter, 67.
2 X"1HD as used on the incantation bowls is significant ; cf. Montgomery,
Aramaic Incantation Texts, Glossary, 297.
```


### [2026-09-05T14:55:59.299Z] TOOL RESULT

```
=== SDQ leaf 88
n  sein  mag ;  dann  würde  sich Jotw  und  .Äjua  nicht  nur  graphisch  unterscheiden.  L.]  Das  echt persische  AVort  sikl  „hundert"  schreibt  der  Perser  konsequent  mit (jo ,    damit    es    von   dem   arab.  lA^   unterschieden   wird  (? !).     Ferner
i*i  „sechzig"  (BQ.  bezeichnet  es  „arabisiert"  !)  und  vj^.^^^  „Strick"
(>  arabisiert  (j^a^i)  u.  m.  a.  Echt  ist  dagegen  das  c  in  xxJl3»  „Eh- rengewand", welches  kein  Fremdwort  ist,  wie  Völlers  ZDMG.  50  S.  630 u.  647  annimmt.  Vgl.  BQ.  (Append.)  s.v.  Als  Zeichen  der  höchsten Ehre  wurde  vom  Kaiser  ein  von  ihm  getragenes  (also  ^^ausgezogenes"') Kleid  verliehen.  Bald  verlor  das  Wort  seine  eigentliche  Bedeutung und  hieß  nur  „Ehrengewand".  Um  nun  das  W^ort  in  seiner  ursprüng- lichen Bedeutung  zu  gebrauchen  ward  man  gezwungen  andere  Bestim- mungen hinzuzufügen.  So  gab  es  am  Hofe  der  Großmoguls  in  Indien verschiedene    Klassen   von   hü'at:    ^jols>   i^j.Aa    o*.xJl>    „das    von
seiner  Majestät  getragene  Ebrengewand"  zur  ganz  außergewöhnlichen Auszeichnung,  meist  für  die  dem  Kaiser  nahestehenden  Würdenträger ; dann  kamen  die  ordentlichen  hil'ats:  Ä:r-.Lj  c>»-ä^  c>^*J^i>  „die  Eh- renkleidung bestehend  aus  sieben  Stücken"  u.  s.  w.
—     72     —
Versuch  das  unaspirierte  persische  t  wiederzugeben,  da ja  der  Araber  das  o  leicht  aspiriert  spricht.
8.  Ein  arabisches  3  vertritt  das  alte  postvokalische persische  d  ^),  wofür  auch  im  Neupersischen  früher  ein  ö geschrieben  wurde  und  erst  später  das  ö  eintrat.
9.  Persisches  _  (c)  wird  durch  ^jw^,  wie  auch  im Aramäischen,  zuweilen  aber  auch  durch  jä  wiedergegeben :
^Jjo  „Harfe'"'    (=  p.  <3^ä=^)"),    r-ij^-*^   neben  ,V5,Lw  (=  p.
«il^^L^),  ^"i^y^  (=  p.  e^^^j-^  >  o^=^^^  >  ü'-^^^)-  ^^^ Wort  -Sjm  (=  p.  £^j=;i-)  ist  über  das  Aramäische  gekom- men (i^^"!"©).  Das  tt  ist  dadurch  zu  erklären ,  daß
```


## [2026-09-05T14:56:14.117Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ leaf 185\"\nawk 'BEGIN{RS=\"\\f\"} NR==185' FVQ_pages.txt | head -25\necho \"##### DOZ soja\"\ngrep -n -i 'soja\\|soya' DOZ.txt LKT.txt | head -20",
 "description": "FVQ 167 and Dozy/Lokotsch soja"
}
```


## [2026-09-05T14:56:15.593Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN Saracen\"\ngrep -n -i -m3 'Saracen' KLN_1966.txt | head -5\necho \"=== SKT Saracen\"\ngrep -n -i -m3 'Saracen' SKT.txt | head -5\necho \"=== WEB Saracen\"\ngrep -n -i -m3 'Saracen' WEB_vol1.txt | head -5",
 "description": "Grep for Saracen"
}
```


### [2026-09-05T14:56:16.685Z] TOOL RESULT

```
=== FVQ leaf 185
FOREIGN VOCABULARY OF THE QUR*AN 167
into Arabic from an Iranian source, a theory also put forward by
Sachau in his notes to the Mu'arrdb, p. 21. This is of course possible,
since the Arm. zfyiui^ is from the Iranian, as also the Ossetian dray, 1
but Syr. L^ was a very commonly used word with many derivatives
(PSm, 4325), and Vollers, ZDMG, 1, 613, is doubtless right in deriving
the Arabic word from the Syriac.
(Surddiq).
xviii, 28.
An awning, tent cover.
The passage is eschatological, descriptive of the torments of the
wicked, for whom is prepared a fire " whose awning shall enwrap
them ". The exegetes got the general sense of the word from the
passage, but were not very sure of its exact meaning as we see from
Bail's comment on the verse. .
It was very generally recognized as a foreign word. Raghib,
Mufraddt, 229, notes that the form of the word is not Arabic, and
al- Jawaliql, Mu'arrab, 90, classes it as a Persian word, 2 though he is not
very certain as to what was the original form. Some derived it from
.pl^r-j, meaning an antechamber, others from a^ jjj~* curtains, others
from LJu^^r-'j 3 an( i 7 et others from Aj-1^. 4
Pers. a^ j'J j~ is the form from which we must work. It is defined
by Vullers as " velum magnum s. auleum, quod parietis loco circum
tentorium expandunt ", 5 and is formed from *5 J^ a veil or curtain
(Vullers, i, 340), and an O.Pers. \AmSa, 6 from which came the
##### DOZ soja
```


### [2026-09-05T14:56:16.769Z] TOOL RESULT

```
=== KLN Saracen
33732:Saracen,  n.,  1)  an  Arab;  2)  a  Moslem.  —  ML. Saraceni  (pi.),  fr.  Late  Gk.  Zapaxrjvoi  (pi.),  fr. Arab,  sharqiyin,  pi.  acc.  of  sharqiy,  ‘Eastern’,  fr. sharq,  ‘east’,  fr.  sharaqa,  ‘he  cleft,  dissected ;  rose (said  of  the  sun)’.  Cp.  sarcenet,  sarsen,  siroc¬ co.
33733:Derivative;  Saracen-ic,  adj.
33736:sarbacane,  n.,  a  blowgun.  —  F.,  changed  under the  influence  of  canne,  ,‘cane,  reed’,  fr.  sarbatane (still  used  in  1798  by  the  French  Academy),  fr. Sp.  cerbatana,  zarbatana,  fr.  VArab.  zarbatanJ ’, fr.  Arab.  zabatanah,  ult.  fr.  Malay  sumpitan,  of s.m.,  fr.  sumpit,  ‘narrow’.  Cp.  sumpit. sarc-,  form  of  sarco-  before  a  vowel, sarcasm,  n.,  a  taunting  remark;  an  ironical  jibe. —  F.  sarcasme,  fr.  L.  sarcasmos,  fr.  Gk. oapxaopios,  ‘jest,  taunt,  mockery’,  fr.  oap- iv,  ‘to  tear  flesh  like  dogs;  to  bite  the  lips  in rage;  to  speak  bitterly,  sneer’,  fr.  aotp5,  gen. aiy.py.be,  ‘flesh’.  See  sarco-. sarcastic,  adj.  —  Gk.  oapxaa-ixoi;,  fr.  oap- xa^civ.  See  prec.  word  and  adj.  suff.  -ic. Derivatives:  sarcastic-ness,  n.,  sarcastic-al,  adj., sarcastic-al-ly,  adv.,  sarcastic-al-ness,  n. sarcenet,  sarsenet,  n.,  a  fine  silk  material.  —  Late ME.  sarsenet,  fr.  AF.  sarzinet,  dimin.  of  ME. sarzin,  ‘Saracen’.  See  Saracen.
=== SKT Saracen
16488:saroenet.  sarsnet,  a  thin  silk. L.-Arab.)  OF.  satxenet.  a  stufl by  the  Saracens.  —  Low  L.  sar^i sarcenet. —L.  Sarxscentu,  Saracen  ( airooco,  a  hot  wind.  (Itai.  - Ztal.  sirvcco^  south  cast  wind.  «•  Arab ca-it  V above).
19417:(VTAR.) itermlno.  ( F.  —  L.>  O.  F.  deUrminer. '  dttfrminart,  to  bound,  end.— L.  d£, U  fully ;  ttrminare,  to  bound,  from inus  ^abovc),  "Dvt.  prt-detcrmine, ;tenaiiiate.  (L.)  From  pp.  of  L. mimare,  to  put  or  diivc  beyond  bounds. £ff,  out ;  ttrmintu,  boundary. rmination.  (K,  —  L.)  F.  termina- »Lh  ojCc  ttrminationtm^  A  bounding, )g,_L.  terminatWt  pp.  of  itrminare, lund,  end.  —L.  ttrvtinus^  boundary. nninPB.end.(L.)L./frfflriwwj(abQve). nnA£:aiit.  (F.  •  Itnl.  -  L.)  M.  £. tagant^  %  (supposed)  Saracen  idol, t  %  raoting  character  in  old  moralities «}.  and  6nalty  a  scolding  woman.— .  TV/T.J.cifrt/.  7€rvaj;an,  a  (supposed) Sen  idol.«>IlaL  7rhng\inte,  the  same »to,  xii.  59).  Probably  for  Triva- },  the  moon,  wanderiri^  under  the  three Ef  of  StUnt  (or  Luna)  in  heaven, mis  {Diana)  in  earth,  rentthone Hrfina')  in  the  lower  world.  — L./^, e ;  magant;  stem  of  prcs.  pt.  of  uagari, LTHler.
=== WEB Saracen
10386:pointed, and Saracenic arches. Second, they are named specifically according to the Curve the intrados assumes, when that curve js the section of any of the geometrical solids- ae segmental, semicircular, cycloidal, elliptical
32274:the Fair Labor Standards Act of 1938, is 16 (n hazardous occupations, 18), but this standard is not observed by all States. child’less, a. having no children or offspring. cpio eee n. the state of having no chil- ren. childlike, a. resembling a child, or that which belongs to children; becoming a child; meek; submissive; dutiful; as, childlike obedience. child/ly, a. childlike; childish. [Rare.] child/ly, adv. in the manner of a child. child’ness, n. the character or nature of a child. [Obs.] å child psy-chol’6-Zy (sy-) the branch of psychol- ogy that deals with the behavior and men- tal processes of children. chil’dren, n., plural of child. chil’dren of Is’ra-el, the Jews; the Hebrews. Children’s Crusade’, either of two ill-fated crusades for the recovery of Jerusalem from the Saracens, undertaken in 1212 by thou- sands of French and German children: in the first, those who reached the Mediterranean were sold into slavery; the survivors of the second turned back after crossing the Alps. ba eben n. the condition of being a child. are. child’s play, any very simple task. chil’é, n. same as chili. Chil’/é@-4n, a. pertaining to Chile, its people, or culture: also spelled Chilian. i Chil’/é@-4n, n. 1. a native or inhabitant of Chile. 2. Spanish as spoken in Chile. chile con car/né, a pungent Mexican dish made usually of beans, red peppers, spices, and meat. chil’i, n.; pl. chil’ies, [Sp., from native Mex. name.]
84134:gray’wethér, grey’weth€r, n. a kind of stone found in England, bearing a resem- blance to a gray sheep: called also druid stone, Saracen stone, and sarsen stone.
```


## [2026-09-05T14:56:32.779Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN page markers near soy/Saracen\"\ngrep -n '^\\s*1479\\s*$\\|^\\s*1383\\s*$' KLN_1966.txt | head\nawk 'NR>=33700 && NR<=33740 && /^[0-9]{3,4}$/{print NR\": \"$0}' KLN_1966.txt | head\necho \"--- looking for page-ish lines around 33732 ---\"\nsed -n '33725,33735p' KLN_1966.txt | cut -c1-120",
 "description": "Check KLN page markers"
}
```


## [2026-09-05T14:56:33.702Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 leaf 83 چراغ\"\ngrep -n 'چراغ' BQT_v2_pages.txt | head -20\necho \"=== DOZ file check\"\nls -la DOZ.txt; head -c 300 DOZ.txt",
 "description": "BQT cheragh and DOZ check"
}
```


### [2026-09-05T14:56:34.648Z] TOOL RESULT

```
=== KLN page markers near soy/Saracen
36025:1479
--- looking for page-ish lines around 33732 ---
Derivative:  Sapphic,  n.,  a  Sapphic  verse, sapphire,  n.  —  ME.  safir,  saphir,  fr.  OF.  safir  (F. saphir ), 
saprogenic,  saprogenous,  adj.,  producing  putre¬ faction.  —  Compounded  of  sapro-  and  -genic, resp.  -genous.
saprolite,  n.,  disintegrated  rock  (petrogr.)  — Compounded  of  sapro-  and  Gk.  XiS-ot;,  ‘stone’. See  -lif
Derivative:  saprolit-ic,  adj. saprophagous,  adj.,  feeding  on  decaying  matter. —  Compounded  of  sapro-  and  G
sapsago,  n.,  a  kind  of  hard  Swiss  cheese.  —  Cor¬ ruption  of  G.  Schabzieger,  which  is  compound¬ ed  of
saraband,  n.,  a  slow  Spanish  dance.  —  F.  sara- bande,  fr.  Sp.  zarabanda,  borrowed  fr.  Persian
serbend,  ‘a  kind  of  dance’,  through  the  medium of  Arabic.
Saracen,  n.,  1)  an  Arab;  2)  a  Moslem.  —  ML. Saraceni  (pi.),  fr.  Late  Gk.  Zapaxrjvoi  (pi.),  fr. Arab,  
Derivative;  Saracen-ic,  adj.
Sarah,  also  Sara,  1)  fem.  PN. ;  2)  in  the  Bible,  the wife  of  Abraham  and  the  mother  of  Isaac.  — Lit.
Saratoga  trunk  a  large  traveling  trunk.  —  Named after  Saratoga  Springs,  a  summer  resort  near New  York.
```


### [2026-09-05T14:56:34.699Z] TOOL RESULT

```
=== BQT v2 leaf 83 چراغ
1357:      ‫و بمعنی چراغ وچراغدان همآ مده است‪.‬‬
1396:                                  ‫چراغ باشد ‪.‬‬         ‫چر هر ‪ = ۵‬بفتح اول و ضم میم بروزن‬
2310: ‫نیز گوبند ‪ -‬و نامشخصی بوده که کربهبیاری‬                     ‫جلو ند = بر وزن فرزند ' بمعنی چراغ‬
4491:                                                                    ‫جاع ؟ ‪ -‬بکسر اول بروزن چراغ »‬
4806:                ‫چراغ ‪ -‬بروزن‌فراغ؛‬                                              ‫برروی شر دد ‪.‬‬
4808:                 ‫و روغن و امثال آن‬         ‫چربی‬                               ‫ومعنی چراغ است ‪.‬‬
4825:   ‫‪-‬ك ‪ :‬چراغ ‪.‬‬                                 ‫شهمیرزادی ‪۰ ۲ .4« 8766‬‬
4830:   ‫اصاف ومکان)‪ ,‬رك‪:‬چراغ بره » چراغ واره‪ - ۸ .‬رك‪ :‬چراخوار ‪ :‬خرسند شدی بخوردکیتی‪-‬‬
4836:   ‫ادی‌شیر (‪ )۹۸‬میخواهد کلمة فارسی چراغ را از سریانی مأخوذبداند ولی این امراکل‌ازففاست ‪.‬‬
4839:   ‫چراغله‬                                                                                                         ‫‪۲۷‬‬
4846: ‫نقطه دار زده‪ ,‬فالوی وچیزی که محافظت چراغ‬                         ‫و کنانه‬     ‫رهنما رایز کوبند ‪-‬‬       ‫را _‪١‬‏ ویرومرشد‬
4851: ‫چراغ چشم‪ -‬بکس رابع ‪.‬کنایه از‬
4854: ‫کنابه ازآفتاب وهاه‬          ‫سیهر ‏‬      ‫چراغ‬
4864:                                                                  ‫چراغیاله = بمه‌نی چراغهاست ‪ .‬بعنی‬
4865: ‫(‪ )۲‬جر اغات ه مسفرچراغ باشد ‪ -‬وکرم‬                                                        ‫اسب هر دودست خود را ؟ ‪.‬‬
4867: ‫خوانند ‪ .‬گویند چون سٽارة سهیل طالع شود او‬                        ‫مشکوة‬        ‫بعری‬   ‫و‬    ‫فوند‪,‬‬    ‫چراغدانرا‬         ‫فرشت‬
4872:                        ‫چبر ا‬                                        ‫چراغ پرهیز ‪ -‬بنتحف بااریسی‬
4875:                            ‫رلك ‪ :‬چراغ‪ ,‬چراغیابه ‪۰‬‬         ‫‪- ۳‬‬           ‫‪ :‬چراغپا چوراغپابه ‪.‬‬          ‫رك‬
4877:   ‫‪5‬‬    ‫‪ 2‬چراغ ‪ +‬بر (بردن) ‪+‬‬             ‫‪ ۴‬از‬                                 ‫چراغ »چراغپا ‪.‬‬          ‫و‬
4878:       ‫‪ _ ۵‬نظیر«قرة العین؟ درعربى‪.‬‬                     ‫واره (ه‪.‬م‪).‬‬     ‫چراخ‬    ‫چراغ واره («‪.‬م ( ‪-‬‬        ‫=‬       ‫(يوندآات)‬
=== DOZ file check
-rw-rw-r-- 1 sfmqrb sfmqrb 143939 Sep  4 14:06 DOZ.txt
This is a digital copy of a book that was preserved for generations on library shelves bef ore it was carefully scanned by Google as part of a project
to make the world's books discoverable online.
It has survived long enough for the copyright to expire and the book to enter the public domain. A pub
```


## [2026-09-05T14:56:47.728Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt'\nlines=open(p,encoding='utf-8',errors='replace').read().split('\\n')\nff=0\nfor i,l in enumerate(lines,1):\n    if '\\f' in l: ff+=1\n    if i in (1357,4806,4836,4839):\n        print(i, 'leaf(0-based ff count)=',ff, 'printed~', ff+543)\nEOF\nsed -n '4800,4845p' BQT_v2_pages.txt | cut -c1-200",
 "description": "Locate BQT v2 cheragh page"
}
```


## [2026-09-05T14:56:49.421Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c . MON_part1.txt MON_part2.txt 2>/dev/null\necho \"=== try shosho variants in MON\"\ngrep -n 'شوش' MON_part1.txt MON_part2.txt | head -20",
 "description": "Grep Mo'in for shusho"
}
```


### [2026-09-05T14:56:49.875Z] TOOL RESULT

```
1357 leaf(0-based ff count)= 26 printed~ 569
4806 leaf(0-based ff count)= 84 printed~ 627
4836 leaf(0-based ff count)= 84 printed~ 627
4839 leaf(0-based ff count)= 85 printed~ 628
  ‫فراخور‪ .‬بمعنی‌چراخوارباشد‪ 4‬که چراگاه‌است‪.‬‬
  ‫جراسك = باسین بی‌نقطه بروزن‌|تايك‪,‬‬                                                     ‫گویند ‪.‬‬
                                                     ‫بفتح اول بر وزن سرا بمعنی‬      ‫جرا‬
                ‫حیوانی است کوچکتر از ملح‬
                                                     ‫چریدن‌باشد؟ ‪ -‬وبکر ارل‌یمعنی ازیرای‌چه؟ ‪.‬‬
                 ‫و شبها بانگه طولانی کند ‪.‬‬          ‫چرابه ت بر وزن قرابه » قیمافی که‬
                ‫چراغ ‪ -‬بروزن‌فراغ؛‬                                              ‫برروی شر دد ‪.‬‬
                ‫فتیله ای باشد که آنرا با‬             ‫چراخ ‪ ۴‬س با خای نقطه‌دار » بر وزن‬
                 ‫و روغن و امثال آن‬         ‫چربی‬                               ‫ومعنی چراغ است ‪.‬‬
                 ‫‪٩‬‏ ‪-‬‬    ‫روشن کرده باشند‬              ‫چراجوار * ‪ -‬با واومعدوله بروزن‬
                 ‫و بمعنی چرا و چراکردن هم‬                        ‫‪۳‬‬   ‫هوادار ‪ ۰‬بمعنی چراگاه باشد ‪۹‬‬


                                                     ‫بکراولوفتح رای‬         ‫جراخ و اره‬
‫‪۱‬رو‪-‬غنی ا‪۲‬و‪۳‬ل‪-‬کنفلتیی»‪6--‬برقی(الکتر )‪۰‬‬
  ‫بشاب‬    ‫در اراك ( سلطان آباد ) ‪۲06‬‬          ‫هم‬     ‫(ه‬     ‫ول‬
                                                             ‫چ‪ ۰‬م‬
                                                                ‫)( ھ‬
                                                                   ‫چل‬             ‫‏‪= ١‬‬
  ‫مکی نژاد)؛ چره ) بتشدید دوم)‬     ‫‪ ۳‬ادرار را گوبند و ‪nãdroc‬‏ مثانه و ‪nadîroc‬‏ شاشمدن را‬

                 ‫رك ‪ :‬چره ‪.‬‬   ‫‪.‬‬   ‫(‪fA‬‏‬   ‫د حفتایی‬   ‫درتر کی آلت تناسل نرینه از جانوران است ‪.‬‬
  ‫‪ - ۴‬از ‪ :‬چر(چربدن) ‪ (۱ +‬مصدری ) ‪ .‬پهلوی ‪ ( 12۳20‬چراگاه )‏ افغانی ‪۲4٥‬‏‬
   ‫(چربدن) « هوشمان ‪ » 4۳:۰‬سمنانی ‪ 8۲82۰‬منگری‪ 6‬و ‪ ,6۲66‬سرخه‌بی ولاسگردی‪,8۲66‬‬
             ‫‪-‬ز ‪ :‬چە ‪ +‬را (= برای)‪ ۴ .‬ر‬
   ‫‪-‬ك ‪ :‬چراغ ‪.‬‬                                 ‫شهمیرزادی ‪۰ ۲ .4« 8766‬‬
                                      ‫ص‪ ۴ . ۷۹۱‬ا‬
  ‫® ‪-‬طبری‪( 4۳20 - ۵۷2 ۲‬مرتم) « صاب طبری‪ .»۲۸۲‬رك ‪ :‬چراخور ‪ .‬نعت فاعلی امت و لغة‬
  ‫بممنی خورندة چرا(علف خوار)است‪ .‬درینجا اطلاق حال بمحل شده ‪-« ۱ .‬باد غیس خرم ترین‬
   ‫چرا خوارهای خراسان وعراقاست‪( ».‬چهار مفاله ‪ -۷ .)۱۳‬از‪:‬چراخ (چراع) ‪ +‬واره ( یوند‬
   ‫اصاف ومکان)‪ ,‬رك‪:‬چراغ بره » چراغ واره‪ - ۸ .‬رك‪ :‬چراخوار ‪ :‬خرسند شدی بخوردکیتی‪-‬‬
  ‫زبرانوخری‌جهان چراخور‪ . .‬ناصرخسروبلخی‪.‬بسنااص‪۲۲۱‬ح؟»‪ .‬ورك‪:‬دبوان‌ناصرخروص‪) ۵۱ 4‬‬
   ‫‏‪ - ٩‬کلم فارسی‌است که در آرامی و سربانی ویزعربی (سراح) وارد شده ( قرآن»سورءة‬
  ‫یوره ) ‪ .‬استی ‪ 091( 082۳16‬و ‪mmarG . , 1‬‏ ‪ )۰۵۲۲۸‬جفری گوبد ‪:‬‬
                                                            ‫غ‪۷‬‏‬
                                                              ‫‪. ۵‬به ‪٩‬‬
   ‫ادی‌شیر (‪ )۹۸‬میخواهد کلمة فارسی چراغ را از سریانی مأخوذبداند ولی این امراکل‌ازففاست ‪.‬‬
   ‫«جفری ‪ .۷۱- ۹۹۱‬شکل پپلوی آن ‪ »08271‬است ‪ « .‬بنا‪٩ ۲ :۲۳۱‬‏ کرستنسن کلمه‬
   ‫یه در صفحهٌ ‪۷۲٩‬‏‬
   ‫چراغله‬                                                                                                         ‫‪۲۷‬‬



 ‫وسکون رای قرشت وها بتحتالی رسیده و بزای‬                          ‫خود‬    ‫و برداشتن اسب هر دو دست‬                 ‫آمده اس
```


### [2026-09-05T14:56:49.958Z] TOOL RESULT

```
MON_part2.txt:75975
MON_part1.txt:78085
=== try shosho variants in MON
MON_part2.txt:28981:افتادن: ناراحت شدن» مشوش گردبدن. 
MON_part2.txt:39831:لف و نشر مشوش: 
MON_part2.txt:39832:«لف و نشر مشوش آنرا دان 
MON_part2.txt:58121:مشوش: ۱00۹۸۹۸ (ع. (امف.) بریشان 
MON_part2.txt:58123:مشوش: 110۹/۷۵ [ع. (افا.) 1 
MON_part2.txt:61676:مسفغشوش: کتگنس [ع.] (امسف.) امخته 
MON_part2.txt:65587:رامهرمز - ۲۵ کیلوگرم. - در شوشت 
MON_part2.txt:66550:«بال» نامند؛ شوشه (فره.) منشور قایم: (هت.) 
MON_part2.txt:71252:مغشوش. شهوی» زنا کار. 
MON_part2.txt:71409:که خالص نباشد» مغشوش)؛ مق. خالص. 
MON_part2.txt:71696:مضطرب» مشوش. عصبانی. 
MON_part2.txt:72206:عیبنا کك» ناقص. قلب» مغشوش؛ مق. سره. 
MON_part2.txt:72711:عنبر مغشوش (خصوصا). 
MON_part2.txt:73336:مشوش: نانی سیار نازک و رقیق که در اعیاد 
MON_part2.txt:74225:مسغشوش (عموما). دون» فرومایه, ست. 
MON_part2.txt:78519:نقش شوشتر: گویا به معنی نقش دیبای 
MON_part2.txt:79138:بسنند ۵. تأمل کننده. منتظر. ناراحت» مشوش. 
MON_part2.txt:80578:فرشوشتر و او برادر جاماسپ و او وزیرکی 
MON_part2.txt:84273:کند و مشوش می‌شود و بکباره می‌ایستد؛ 
MON_part2.txt:90376:چیز درهم و برهم» مفشوش.
```


## [2026-09-05T14:57:07.551Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'شوش' MON_part1.txt | head -20\necho \"=== ranges\"\nhead -3 MON_part1.txt; echo ---; head -3 MON_part2.txt",
 "description": "Grep MON part1"
}
```


### [2026-09-05T14:57:07.613Z] TOOL RESULT

```
1474:می‌نهادند (در حفریات شوش از این ایزن‌ها 
3367:(ص.) مضطرب» پریشان» مشوش؛ آشفته. 
4377:الفتن: «هة (مصم.) آشفتن» مشوش 
13997:انداختن: مشوش کردن» برشان ساختن. 
20157:بها» مغشوش» نبهره. زبان باردار: (پز.) زبانی 
20962:پالوش] (.) کافور مغشوش. 
22911:مسسجتمع. . شسوریده» مشوش. بریشان» 
22912:مضطرب. ۳ و برهم: شوریده و مشوش. 
25501:مشوش شدم. . بند قنا کشیدن: کشادن بند قا. 
31654:مشوش. ناگوار» تلخ. سست» ضعیف. 
34139:مشوش» بی آرام» به سبب دردی يا اندوهی 
34157:مضطرب ساختن» مشوش کردن. بمجاندن 
40961:تشوشص: 305 ([ع.] (مص‌ل.) شوریده 
42654:ساخته شود؛ جنس قلب» قلابی» مغشوش: 
45288:در شا ستاو ادن شوش (افتاد[: 
47868:جعشوش: کتک 0[ [ع] رص. ۱.) کدا. مرد 
56964:خفجچه: : (60-)۵662 (.) شوشه زر و سیم مللا 
58142:شوش ‌سساب: 1.۳ آف. ع.] 
64616:مفشوش» مضطرب؛ شور یده. 
72748:پایین و بالا شدن (کردن)؛ مشوش و درهم 
=== ranges
0 
2 

---
معین» محمد» ۱۲۹۱ ۱۳۵۰.
```


## [2026-09-05T14:57:10.318Z] TOOL CALL #28: Bash

```json
{
 "command": "pdftoppm -f 105 -l 105 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg105 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 105"
}
```


### [2026-09-05T14:57:12.817Z] TOOL RESULT

```
total 32392
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 10:57 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb   189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   513902 Sep  5 02:15 bqt440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5214 Sep  5 02:23 build82a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    53401 Sep  5 02:29 build82b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    19831 Sep  5 02:31 build82c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48417 Sep  5 10:19 build93.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59425 Sep  5 10:54 build98.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2950 Sep  5 10:15 c_anth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2661 Sep  5 10:15 c_armonica.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9603 Sep  5 10:50 c_byz2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11328 Sep  5 10:49 c_byz_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3138 Sep  5 10:50 c_heb1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4953 Sep  5 10:50 c_heb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4845 Sep  5 10:50 c_root3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1795 Sep  5 10:50 c_scyth2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2953 Sep  5 10:50 c_scyth3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4885 Sep  5 10:49 c_scyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3019 Sep  5 10:15 c_sus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33345 Sep  5 10:55 e0.102.json
-rw-rw-r-- 1 sfmqrb sfmqrb    38686 Sep  5 10:34 e0.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    26175 Sep  5 10:38 e1.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb      456 Sep  5 10:56 g.py
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    49033 Sep  5 10:53 mk100.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17464 Sep  5 10:55 mk102b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    21655 Sep  5 10:53 mk102.py
-rw-rw-r-- 1 sfmqrb sfmqrb    40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb    78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52793 Sep  5 02:18 mk79.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57729 Sep  5 02:31 mk81.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58379 Sep  5 02:39 mk83.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76819 Sep  5 02:39 mk84.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25181 Sep  5 02:44 mk86.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67712 Sep  5 10:03 mk87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66054 Sep  5 10:10 mk89.py
-rw-rw-r-- 1 sfmqrb sfmqrb    70790 Sep  5 10:04 mk90.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48553 Sep  5 10:03 mk91.py
-rw-rw-r-- 1 sfmqrb sfmqrb    27206 Sep  5 10:38 mk95b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    39501 Sep  5 10:34 mk95.py
-rw-rw-r-- 1 sfmqrb sfmqrb    49433 Sep  5 10:35 mk96.py
-rw-rw-r-- 1 sfmqrb sfmqrb    54149 Sep  5 10:47 mk97.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61159 Sep  5 10:50 mk99.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71589 Sep  5 10:41 pg100.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68145 Sep  5 10:44 pg102.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114170 Sep  5 10:49 pg103_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79623 Sep  5 10:49 pg103.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82500 Sep  5 10:57 pg105.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb   155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58953 Sep  5 02:08 pg80.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99904 Sep  5 02:15 pg81.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29321 Sep  5 02:20 pg82_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74477 Sep  5 02:20 pg82.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56108 Sep  5 02:20 pg82_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   154129 Sep  5 02:25 pg83_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7123 Sep  5 02:26 pg83_apac.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4363 Sep  5 02:26 pg83_bohyah.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67094 Sep  5 02:25 pg83.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82358 Sep  5 02:23 pg84.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63329 Sep  5 02:25 pg85.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31530 Sep  5 02:35 pg86.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79874 Sep  5 09:47 pg87.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134852 Sep  5 09:54 pg88_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11747 Sep  5 09:54 pg88_e0spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31391 Sep  5 09:55 pg88_join.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98452 Sep  5 09:54 pg88.png
-rw-rw-r-- 1 sfmqrb sfmqrb    26700 Sep  5 09:54 pg88_spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb   171528 Sep  5 02:45 pg89_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4628 Sep  5 02:45 pg89_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4924 Sep  5 02:45 pg89_berijan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80984 Sep  5 09:49 pg89.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77182 Sep  5 09:48 pg90.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63799 Sep  5 09:55 pg91.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157177 Sep  5 10:09 pg92_500.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8494 Sep  5 10:09 pg92_avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3476 Sep  5 10:09 pg92_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90918 Sep  5 10:07 pg92.png
-rw-rw-r-- 1 sfmqrb sfmqrb    93420 Sep  5 10:15 pg94.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44047 Sep  5 10:16 pg94_sogd.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49714 Sep  5 10:16 pg94_urvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78178 Sep  5 10:11 pg95.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163439 Sep  5 10:15 pg96_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72929 Sep  5 10:15 pg96.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101597 Sep  5 10:41 pg99_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8738 Sep  5 10:41 pg99_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65608 Sep  5 10:40 pg99.png
```


## [2026-09-05T14:57:16.186Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg105.png"
}
```


### [2026-09-05T14:57:16.547Z] TOOL RESULT

```

```


## [2026-09-05T14:57:16.545Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T14:57:26.606Z] TOOL CALL #30: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py",
 "description": "Inspect fetch_source tool"
}
```


### [2026-09-05T14:57:26.641Z] TOOL RESULT

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


## [2026-09-05T14:57:31.666Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%DA%86%D8%B1%D8%A7%D8%BA\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%A7%D8%AC\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D8%B1%D9%82\" \\\n \"https://www.etymonline.com/word/Saracen\" \\\n \"https://www.etymonline.com/word/soy\" ; do\n  python3 tools/fetch_source.py \"$u\" --note \"page 105 verification (Cîrâğ / Chiang-yu roots)\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-05T14:57:36.128Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/aab5e5692825f204.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/07fbd11449f9d7a8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b72cc012ea3476d4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d6418b07671b1447.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/05a271aafb1a0bff.txt
```


## [2026-09-05T14:57:39.511Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== cheragh\"\ngrep -n -i -A6 'Etymology' aab5e5692825f204.txt | head -60",
 "description": "Read cheragh wiktionary"
}
```


### [2026-09-05T14:57:39.558Z] TOOL RESULT

```
=== cheragh
76: Etymology 
77-
78- 2.3 
79- Pronunciation 
80-
81- 2.4 
82- Noun 
--
102: Etymology 
103-
104- 3.2 
105- Noun 
106-
107- 3.3 
108- References 
--
116: Etymology 
117-
118- 4.2 
119- Pronunciation 
120-
121- 4.3 
122- Noun 
--
139: Etymology 
140-
141- 5.2 
142- Pronunciation 
143-
144- 5.3 
145- Noun 
--
299: Etymology
300- [ edit ] 
301-
302- Borrowed from Classical Persian چراغ ( čirāġ, čarāġ ) , itself from Parthian 𐫝𐫡𐫀𐫃 ( crʾg /⁠čirāγ⁠/ , “ lamp ” ) . Doublet of سراج ( sirâc , “ lamp ” ) .
303-
304- Pronunciation
305- [ edit ] 
--
361: Etymology
362- [ edit ] 
363-
364- Borrowed from Classical Persian چراغ ( čirāġ ) .
365-
366- Noun
367- [ edit ] 
--
383: Etymology
384- [ edit ] 
385-
386- Borrowed from Parthian 𐫝𐫡𐫀𐫃 ( crʾg /⁠čirāγ⁠/ , “ lamp ” ) . Compare Middle Persian [Book Pahlavi needed] ( clʾγ ) , 𐫝𐫡𐫀𐫍 ( crʾh /⁠čirāγ⁠/ , “ lamp ” ) , Sogdian [script needed] ( crʾʾγ /⁠čarāγ⁠/ ) , Ossetian цырагъ ( cyraǧ ) . Iranian borrowings: Old Armenian ճրագ ( črag ) , Classical Syriac ܫܪܓܐ ( šərāḡāʾ ) , Arabic سِرَاج ( sirāj ) .
387-
388: This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium . 
389-Particularly: “Related to Proto-Indo-Iranian *čitrás ( “ bright, shining ” ) ?”
390-
391- Pronunciation
392- [ edit ] 
393-
394- ( Classical Persian ) IPA ( key ) : /t͡ʃi.ˈraːɣ/ , /t͡ʃa.ˈraːɣ/
```


## [2026-09-05T14:57:40.668Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== siraj\"\ngrep -n -i -B2 -A10 'Etymology' 07fbd11449f9d7a8.txt | head -60\necho \"=== sharq\"\ngrep -n -i -B2 -A10 'Etymology' b72cc012ea3476d4.txt | head -50",
 "description": "Read siraj and sharq wiktionary"
}
```


### [2026-09-05T14:57:40.730Z] TOOL RESULT

```
=== siraj
60-
61- 1.1 
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Noun 
69-
70- 1.1.2.1 
71- Declension 
72-
--
75-
76- 1.2 
77: Etymology 2 
78-
79- 1.2.1 
80- Pronunciation 
81-
82- 1.2.2 
83- Noun 
84-
85- 1.2.2.1 
86- Declension 
87-
--
101-
102- 2.1 
103: Etymology 1 
104-
105- 2.1.1 
106- Noun 
107-
108- 2.1.1.1 
109- Derived terms 
110-
111- 2.1.2 
112- Further reading 
113-
114- 2.2 
115: Etymology 2 
116-
117- 2.2.1 
118- Noun 
119-
120- 2.2.1.1 
121- Derived terms 
122-
123- 2.2.1.2 
124- Descendants 
125-
--
196- [ edit ] 
197-
198: Etymology 1
199- [ edit ] 
200-
201- Root 
=== sharq
60-
61- 1.1 
62: Etymology 1.1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Noun 
69-
70- 1.1.2.1 
71- Declension 
72-
--
78-
79- 1.2 
80: Etymology 1.2 
81-
82- 1.2.1 
83- Verb 
84-
85- 1.2.1.1 
86- Conjugation 
87-
88- 1.3 
89: Etymology 2.1 
90-
91- 1.3.1 
92- Verb 
93-
94- 1.3.1.1 
95- Conjugation 
96-
97- 1.4 
98: Etymology 2.2 
99-
100- 1.4.1 
101- Noun 
102-
103- 1.4.1.1 
104- Declension 
105-
106- 1.5 
107- References 
108-
--
121-
122- 3.1 
123: Etymology 1 
124-
```


## [2026-09-05T14:57:48.246Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '190,320p' 07fbd11449f9d7a8.txt",
 "description": "Read siraj Arabic section"
}
```


### [2026-09-05T14:57:48.286Z] TOOL RESULT

```
 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Arabic
 [ edit ] 

 Etymology 1
 [ edit ] 

 Root 

 س ر ج ( s r j ) 

 4 terms 

 Borrowed from Aramaic שְׁרָגָא ( šerāgā ) (in Classical Syriac ܫܪܳܓܳܐ ), from Parthian *𐫢𐫡𐫀𐫄 ( *šrʾɣ /⁠širāɣ⁠/ ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /si.raːd͡ʒ/ 

 Rhymes: -aːd͡ʒ 

 Noun
 [ edit ] 

 سِرَاج • ( sirāj )  m ( plural سُرُج ( suruj ) ) 

 lamp , luminary , lantern 

 used as a part of plant-names 

 Declension
 [ edit ] 

 Declension of noun سِرَاج ( sirāj )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 سِرَاج 
 sirāj 

 السِّرَاج 
 as-sirāj 

 سِرَاج 
 sirāj 

 nominative

 سِرَاجٌ 
 sirājun 

 السِّرَاجُ 
 as-sirāju 

 سِرَاجُ 
 sirāju 

 accusative

 سِرَاجًا 
 sirājan 

 السِّرَاجَ 
 as-sirāja 

 سِرَاجَ 
 sirāja 

 genitive

 سِرَاجٍ 
 sirājin 

 السِّرَاجِ 
 as-sirāji 

 سِرَاجِ 
 sirāji 

 dual

 indefinite

 definite

 construct

 informal

 سِرَاجَيْن 
 sirājayn 

 السِّرَاجَيْن 
 as-sirājayn 

 سِرَاجَيْ 
 sirājay 

 nominative

 سِرَاجَانِ 
 sirājāni 

 السِّرَاجَانِ 
 as-sirājāni 

 سِرَاجَا 
 sirājā 

 accusative

 سِرَاجَيْنِ 
 sirājayni 

 السِّرَاجَيْنِ 
 as-sirājayni
```


## [2026-09-05T14:57:52.123Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '150,260p' b72cc012ea3476d4.txt",
 "description": "Read sharq wiktionary Arabic"
}
```


### [2026-09-05T14:57:52.164Z] TOOL RESULT

```
 4.1 
 Etymology 

 4.2 
 Pronunciation 

 4.3 
 Noun 

 4.3.1 
 Derived terms 

 4.3.2 
 See also 

 5 
 North Levantine Arabic 

 Toggle North Levantine Arabic subsection 

 5.1 
 Etymology 

 5.2 
 Pronunciation 

 5.3 
 Noun 

 5.3.1 
 See also 

 6 
 Ottoman Turkish 

 Toggle Ottoman Turkish subsection 

 6.1 
 Etymology 

 6.2 
 Noun 

 6.2.1 
 Derived terms 

 6.2.2 
 Descendants 

 6.3 
 Further reading 

 7 
 Persian 

 Toggle Persian subsection 

 7.1 
 Etymology 

 7.2 
 Pronunciation 

 7.3 
 Noun 

 7.3.1 
 Coordinate terms 

 7.3.2 
 Derived terms 

 8 
 South Levantine Arabic 

 Toggle South Levantine Arabic subsection 

 8.1 
 Etymology 

 8.2 
 Pronunciation 

 8.3 
 Noun 

 8.3.1 
 Derived terms 

 8.3.2 
 See also 

 Toggle the table of contents 

 شرق 

 21 languages 

 العربية 
 Azərbaycanca 
 Deutsch 
 Español 
 فارسی 
 Français 
 Magyar 
 Bahasa Indonesia 
 ಕನ್ನಡ 
 Kurdî 
 Lietuvių 
 Malagasy
```


## [2026-09-05T14:57:55.138Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nawk 'NR>270 && NR<520' b72cc012ea3476d4.txt | grep -n -A4 'Root\\|Borrowed\\|From \\|Semitic' | head -60",
 "description": "Find sharq etymology text"
}
```


### [2026-09-05T14:57:56.982Z] TOOL RESULT

```
51: From Wiktionary, the free dictionary
52-
53- See also: سرف , شرف , سرق , and سرڤ 
54-
55- Arabic
--
58: Root 
59-
60- ش ر ق ( š r q ) 
61-
62- 11 terms
```


## [2026-09-05T14:57:59.451Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '330,420p' b72cc012ea3476d4.txt",
 "description": "sharq Arabic entry body"
}
```


### [2026-09-05T14:57:59.495Z] TOOL RESULT

```
 ش ر ق ( š r q ) 

 11 terms 

 Etymology 1.1
 [ edit ] 

 Compare Hebrew מִזְרָח ( mizrákh , “ east ” ) , Hebrew זָרַח ( zarákh , “ to shine, to rise ” ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ʃarq/ 

 Audio : ( file ) 

 Noun
 [ edit ] 

 شَرْق • ( šarq )  m 

 east ; Orient 

 Declension
 [ edit ] 

 Declension of noun شَرْق ( šarq )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 شَرْق 
 šarq 

 الشَّرْق 
 aš-šarq 

 شَرْق 
 šarq 

 nominative

 شَرْقٌ 
 šarqun 

 الشَّرْقُ 
 aš-šarqu 

 شَرْقُ 
 šarqu 

 accusative

 شَرْقًا 
 šarqan 

 الشَّرْقَ 
 aš-šarqa 

 شَرْقَ 
 šarqa 

 genitive

 شَرْقٍ 
 šarqin 

 الشَّرْقِ 
 aš-šarqi 

 شَرْقِ 
 šarqi 

 Coordinate terms
 [ edit ] 

 compass points : اِتِّجَاهَات الْبَوْصَلَةِ ( ittijāhāt al-bawṣalati ) :  [ edit ] 

 شَمَال غَرْبِيّ ( šamāl ḡarbiyy ) 

 شَمَال ( šamāl )
```


## [2026-09-05T14:58:08.237Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== Saracen\"\ngrep -n -i -m2 -A12 'Saracen (n' d6418b07671b1447.txt | head -40\necho \"=== raw grep\"\ngrep -n -i 'Ptolemy\\|Sarakenoi\\|sharqiyin\\|unknown origin' d6418b07671b1447.txt | head",
 "description": "Read etymonline Saracen"
}
```


### [2026-09-05T14:58:08.294Z] TOOL RESULT

```
=== Saracen
23: Saracen (n.) 
24-
25- Middle English Saracene , Sarcene , Sarazyn , Sarasine , "a Turk; an Arab; a Muslim," from Old English (in translations from Latin), from Old French Saracin, Sarrasine or Medieval Latin Saracenus , from Greek sarakenos. This usually is said to be from Arabic sharquiyin , accusative plural of sharqiy "eastern," from sharq "east, sunrise," but this is not certain. In medieval times the name was associated with that of Biblical Sarah (q.v.).
26-
27- Peple þat cleped hem self Saracenys, as þogh þey were i-come of Sarra [Ranulph Higden’s "Polychronicon," mid-14c., John Trevisa's translation, 1380s ]
28-
29- It was the name Greeks and Romans gave to the nomads of the Syrian and Arabian deserts and the inhabitants of Arabia Felix, in the West it took on a sense of "Middle Eastern Muslim" from the Crusades. It also could be applied to any non-Christian people against whom a crusade was preached (the pagan Lithuanians), and in Middle English it was used generally for "one who is not a Christian or Jew; heathen, pagan" (mid-13c.). From c. 1300 as an adjective. Related: Saracenic ; Sarcenism ("Islam"), and compare sarsen . Sarsinrie , "the Saracen people or country," is attested in mid-15c.
30-
31- Entries linking to Saracen 
32-
33- Sarah 
34-
35- fem. proper name, Biblical wife of Abraham and mother of Isaac, from Hebrew, literally "princess," from sarah, fem. of sar "prince," from sarar "he ruled," which is related to Akkadian sharratu "queen." A popular as a name for girls born in U.S. in 1870s and 1978-2000.
=== raw grep
```


## [2026-09-05T14:58:09.479Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== soy\"\ngrep -n -i -B2 -A12 'soy (n' 05a271aafb1a0bff.txt | head -40",
 "description": "Read etymonline soy"
}
```


### [2026-09-05T14:58:09.529Z] TOOL RESULT

```
=== soy
54- Origin and history of soy 
55-
56: soy (n.) 
57-
58- 1670s, saio "soybean-based Asian fish sauce," from Dutch soya , from Japanese soyu , variant of shoyu "soy," from Chinese shi-yu, from shi "fermented soy beans" + yu "oil." The etymology reflects Dutch presence in Japan before English and American merchants began to trade there. Soy sauce is attested from 1795.
59- also from 1670s 
60-
61- Entries linking to soy 
62-
63- soya (n.) 
64-
65- "soy," 1670s; see soy . Soyaburger is attested from 1953.
66-
67- soybean (n.) 
68-
```


## [2026-09-05T14:58:28.735Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD soy\"\ngrep -n -o -i 'soy,[^|]\\{0,200\\}' FSD_vol4.txt | head -5\ngrep -n -o -i 'soy-bean[^|]\\{0,150\\}' FSD_vol4.txt | head -3\necho \"=== WEB soy\"\ngrep -n -o -i 'soy, n[^|]\\{0,200\\}' WEB_vol1.txt | head -3\necho \"=== SKT soy\"\ngrep -n -o -i 'soy\\.[^|]\\{0,200\\}' SKT.txt | head -3",
 "description": "Grep English dictionaries for soy"
}
```


### [2026-09-05T14:58:30.472Z] TOOL RESULT

```
=== FSD soy
10074:soy,  1   .   *
64763:soy,  pad'yu-a-sol,  E   E   7   57  TF,  1, 3.  5.  C,  7.  9.  12.  14  15.  16.  20,  21.  22.  23,  24, 26,— pad  yu-a-sel',  IFr ,   8 pageant,  paj'ont  E*  E   57*  TF*  TFr*.  1*,  2, 3   5*  7,  
605:soy-bean 8a-htil%  1   se-hwr,  2   sa-hw/,  n   A   marmoset sa'l,  1   sn'l,  2   sa'I  n   (3raz  I   1.  A   ceblne  monkey  2.  A bright-blue  hoaey-’cce
15596:soy-bean  with  other  ingredi- ents generally  known  as  Japan  soy  or  Chinese  soy.  2. The  soy-bean  or  -pea  a   small  erect  herb  (Cfycfnc  hlspid
=== WEB soy
=== SKT soy
17871:SOY.
```


## [2026-09-05T14:58:30.657Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFA (Fraenkel) siraj\"\ngrep -n -i 'sirag\\|sirāg\\|Lampe' AFA.txt | head -15\necho \"=== AFM Addi Shir cheragh p98\"\ngrep -n 'چراغ\\|سراج' AFM_pages.txt | head -10",
 "description": "Grep Fraenkel and Addi Shir"
}
```


### [2026-09-05T14:58:30.717Z] TOOL RESULT

```
=== AFA (Fraenkel) siraj
=== AFM Addi Shir cheragh p98
1038:+ ( الجيرون ) ܓ يبت 9 وهو السراج
2439:± ( ܐܚܰܐ ܨ ) أثر دخان السراج معرب ܝܰܢ وهو الوسيخ
```


## [2026-09-05T14:58:37.972Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD soy entry\"\nsed -n '15596p' FSD_vol4.txt | cut -c1-700\necho; echo \"=== SKT soy\"\nsed -n '17868,17876p' SKT.txt | cut -c1-400\necho; echo \"=== AFA check\"\nhead -c 200 AFA.txt; echo; grep -c . AFA.txt\ngrep -n -i 'schragha\\|šrāgā\\|Sirāǧ\\|siräg' AFA.txt | head",
 "description": "Read FSD soy, SKT soy, check AFA"
}
```


### [2026-09-05T14:58:38.072Z] TOOL RESULT

```
=== FSD soy entry
sow'ther,  1   sau'thar,  2   sow'ther  rt  &   ri  [Pro^  Eng]  To sow'»tUs''He,  1   sau'-thlsT  2   sow'-thlsH,  n   Any  species  of Soncfius  (see  SocHUS),  especially  5   oleracctis,  the  com- mon sow*thlstle,  a   coarse  annual  weed,  2   to  3   feet  high, with  heads  of  yellow  flowers  and  leaves  with  soft  spinj teeth  also.  5   ojprr  the  spiny-leaved  sow-thlstle  — corn  or field  sow»thIstle,  a   kindred  species  {Soneftus  arrmrii) BOX,  1   seks  2   sdks  n   pi  [CoUoq  U   S   ]   See  sock,  n   1 Boyi,  1   sol,  2   BOy,  n   1   A   sauce  or  Uauld  condiment  prepared in  China  and  Japan  from  the  soy-bean  with  other  ingredi- ents generally

=== SKT soy
lUuough ;  wMat€,  to  sound,  from  soatu.
1
(L.)    From  stem  of  prat.  pt. 1   Tf-soHart,    to    sound    back,   echo,
SOY.
453
Olind.  (F.  —  L.)  O.  F.  rttenmr cent.).— L.  rtsonare  (above), ntet  (Ital.«-L)  Ital.wiM/d.a  sound* ■OOflta.  From  the  fent.  of  pp.  of  Ital, V^  to  sound.  — L.  tonart,  to  sound, tuj,  sound.
fit.    (F.-Ilal.-L.)     F.   nmme.~
He,  a  ftonnet,  can/onel ;  dimin.  of
A    aomid,   lane.  —  L.  ronum,   ace    of

=== AFA check
Google
This is a digital copy of a book that was prcscrvod for gcncrations on library shclvcs bcforc it was carcfully scannod by Google as pari of a projcct
to make the world's books discoverablc onli
17458
```


## [2026-09-05T14:58:48.662Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFA page 7 area\"\nawk 'BEGIN{RS=\"\\f\"} NR>=20 && NR<=24' AFA.txt | grep -n -i 'lamp\\|leucht\\|sarag\\|sirag\\|شراج\\|سراج' | head\necho \"=== AFA grep chirag\"\ngrep -n -i 'čirāγ\\|tschirag\\|čirāġ\\|persischen  Lampe' AFA.txt | head\necho \"=== SKT soy context\"\ngrep -n -i -o 'Japanese[^|]\\{0,120\\}' SKT.txt | head -5",
 "description": "AFA and SKT checks"
}
```


### [2026-09-05T14:58:50.305Z] TOOL RESULT

```
=== AFA page 7 area
=== AFA grep chirag
=== SKT soy context
17916:Japanese.)  Also  soojtt^ 'which  has  been  corrupted  intoii^';*  Eog. CfcL    JapoQcae  lAJymt  so^,  ttnnb  \  V\un^
```


## [2026-09-05T14:58:52.198Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://www.ahdictionary.com/word/search.html?q=Saracen' --note 'page 105, Saracen node, AHD:1152 online check' 2>&1|tail -1\npython3 tools/fetch_source.py 'https://vajehyab.com/?q=%D8%B4%D9%88%D8%B4%D9%88&d=moein' --note 'page 105, MON:2089 shosho millet' 2>&1|tail -1\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/soy' --note 'page 105, soy/soja Dutch-Japanese-Chinese route' 2>&1|tail -1",
 "description": "Fetch AHD, vajehyab, wiktionary soy"
}
```


### [2026-09-05T14:58:55.334Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/16d2f66aea778b19.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2cbebb2fd375ff22.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0fa547e391100612.txt
```


## [2026-09-05T14:58:59.622Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '17910,17920p' SKT.txt | cut -c1-600",
 "description": "Read Skeat soy full"
}
```


### [2026-09-05T14:58:59.666Z] TOOL RESULT

```
Sovereign;  sec  Sub-.//^.
Sow  (1),  to  scattei  seed.  (E.)  A.  S. /theufl,  pL  L  f/i>Uf,  pp.  silwen.  ^  Du. laai/fn,  Icel.  xd,  Dan.  i(uu,  Swe<l.  id. O.  II.  G.  xair^rt,  G.  siun,  Goth  saian.  + W,  Mau^  Lith.  teti,  Russ.  sUi43^4,  L.  j^/rnr (pt.  t.  U'Ui,  pp.  ja-/««m),  to  sow.  (V^A, to  cast.)
seed.  (£.)  A.  S.  ii*/,  seed.  -  A.  S. nhvan,  to  sow.  -^  Du.  sotu/,  Icel.  Ar8/, j<ifi,  Dan.  j<»/.  Swed.  /fl«i^  G.  joat.
Sow  (3),  a  female  pig.  ^E.)  Also ■tpplicd  to  oblong  pieces  orroelted  metal, whence  smaller  pieces  branch  out,  called /i(f7.  M.  £■  xffUK,  A.  S.  xugu,  alj»o  fi^. +  Du.  Kjf,  Icel.  jyr,  Dan.  so,  Swed.  /<», xuj^,  G.  sau.  4-  ^V.  ^uv.),  Irish  sttij^,  h, sut,  Gk.  i%,  avi,  a  sow ;  Zend  hu,  a  bonr. LiL  *  producer,'  from  the  prolific  nature  of the  sow.     ( ^SU,  to  produce.)
BoU  (a\  to  defile.  (F.  -  L.)  M.  E. ioiUn,  [Not  allied  to  M.  £.  xwi^n,  E. /»//f  ]  — O.  F.  soiUtfr,  F.  stmiiicr^  to  soil; St  souithr^  to  wallow  as  a  sow  —  O.  F. soil,  soHxf,  '  the  soile  of  a  wild  boare,  the mire  wherein  he  hath  wallowed;'  Cot. [Cf.  ProT.  svihar,  to  »oil,  solh,  mire,  nt/^a, a  sow;  plainly  from  L.  siwu/a,  a  young sow,  dimin-  of  sus,  a  sow.]  — L,  suUlus, Bilj.,  lielonging  to  swine. —  L.  sus,  a  suw. Der.  soUt  sb.,  a  stain ;  quite  distinct  from soii,  ground.
swine,  a  sow.  pig,  pigs.  (E.)  M.  E swin,  both  sing,  and  pV  A-  S.  swin,  a pig;  pi,  stt/in,  swine.  +  Du.  iwij'h,  a swine,  hug;  Iccl.  jr/»,  pi.  tvin,  Dan. sviin,  pi.  sviiH,  Swed.  jvim,  G.  sckuftM, O.  H.  G.  rufin ;  Goth,  sweitt,  neut.  sb. sini;.  So  also  Kuss.  svintya,  a  swine, jvinka,  a  pig,  sinfuHt  swinish.  All  orig. ad]ccti\*al  fonns,  like  L,  suinus  (Varto), related  to  swine,  formed  from  i«i-,  crude form  of  ius,  a  sow.
Soy,  a  sauce.  (Japanese.)  Also  soojtt^ 'which  has  been  corrupted  intoii^';*  Eog. CfcL    JapoQcae  lAJymt  so^,  ttnnb  \  V\un^
454
SPA.
the  name  is  now  given  to  the  bean  [DolUHot ioja)  whence  soy  is  mnde. Spa,  a  place  where  is  a  spring  of  mineral water.  (Belgium.)  Named  after  Sj*a,  S.W. of  Liige,  in  Belgium. Space.  (F.—  U)  F.  esfaee.^l^  spatium, a  space;  'lit  that  which  is  drawn  out.' (V^I'A,  to  draw  out)  Cf.  Gk.  a»A-€(i',  to draw.    Der.  spac-i-otu.
expatiate.  (L.^  From  pp.  of  L. exfatiari^  better  txspatiari,  to  wander.— L.  tXt  out ;  sfatiari,  to  roam,  from spaiium^  spnce. Spade.  (E.)  A.  S.  spadu,  spada^  a  spade. +  Dq.  sptuie^  IceL  spdHi,  Dnn  Swed. spade,  G.  spatt,  spattn;  Gk.  ffvd^,  liro.-id blade,  sword-blade,  spathc  of  a  flower (whence  L.  spatha,  F.  ///f).  From  its flat  surface.  (^SFA,  to  draw  out.)  Der. spaddlt,  a  paddle:  spadiUe,  ace  of  spades. 1-.  spadilU,  Span,  espadiifa,  small  sword, ace  of  spades,  dimin.  of  Span,  tpada^  a spade  ( ■  L.  spatha  =  Gk.  eri
```


## [2026-09-05T14:59:01.394Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== AHD Saracen\"\ngrep -n -i -A6 'Saracen' 16d2f66aea778b19.txt | head -30\necho \"=== vajehyab shosho\"\ngrep -n -i -B2 -A6 'شوشو' 2cbebb2fd375ff22.txt | head -30\necho \"=== wikt soy\"\ngrep -n -i -A6 'Etymology' 0fa547e391100612.txt | sed -n '1,40p'",
 "description": "Read fetched pages"
}
```


### [2026-09-05T14:59:01.457Z] TOOL RESULT

```
=== AHD Saracen
1:URL: https://www.ahdictionary.com/word/search.html?q=Saracen
2-FETCHED: 2026-09-05T14:58:54Z
3-STATUS: 200
4:TITLE: American Heritage Dictionary Entry: Saracen
5-
6:American Heritage Dictionary Entry: Saracen 
7-
8- HOW TO USE THE DICTIONARY
9- To look up an entry in The American Heritage Dictionary of the English Language, use the search window above. For best results, after typing in the word, click on the “Search” button instead of using the “enter” key.
10- Some compound words (like bus rapid transit, dog whistle, or identity theft ) don’t appear on the drop-down list when you type them in the search bar. For best results with compound words, place a quotation mark before the compound word in the search window.
11- guide to the dictionary 
12-
=== vajehyab shosho
2-FETCHED: 2026-09-05T14:58:54Z
3-STATUS: 200
4:TITLE: معنی شوشو | واژه یاب
5-
6-'
7- />
8-
9: معنی شوشو | واژه یاب 
10-
11- 26 فرهنگ 
12-
13- همه دیکشنری مترادف طیفی آزاد + 
14-
15- همه دقیق مشابه آوا متن آغاز قافیه 
16-
17: «شوشو» پیدا نشد!
18- منظور شما این بود؟ a,a, 
19- شکل سادهٔ لغت را بدون نوشتن وندها و ضمایر متصل بنویسید.
20- برای این واژه یک معنی پیشنهاد دهید. 
21-
22- خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره
=== wikt soy
62: Etymology 
63-
64- 1.2 
65- Symbol 
66-
67- 1.3 
68- See also 
--
79: Etymology 1 
80-
81- 2.2.1 
82- Noun 
83-
84- 2.2.1.1 
85- Alternative forms 
--
103: Etymology 2 
104-
105- 2.3.1 
106- Noun 
107-
108- 2.3.1.1 
109- Usage notes 
--
123: Etymology 
124-
125- 3.2 
126- Pronunciation 
127-
128- 3.3 
129- Noun 
--
155: Etymology 
156-
157- 4.3 
158- Pronunciation 
159-
160- 4.4 
161- Noun 
--
```


## [2026-09-05T14:59:12.270Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -i 'sharqiy\\|shark\\|Sarakenos\\|Ptolemy' 16d2f66aea778b19.txt | head\necho \"=== wikt soy english etym\"\ngrep -n -i 'shōyu\\|shoyu\\|Dutch\\|Japanese' 0fa547e391100612.txt | head -20",
 "description": "Check AHD and wiktionary soy details"
}
```


### [2026-09-05T14:59:12.331Z] TOOL RESULT

```
=== wikt soy english etym
371: Japanese 醤油 
372: Japanese そや bor. 
373: Dutch soja bor. 
376: 1670s; borrowed from Dutch soja , from the Satsuma pronunciation of Japanese 醤油 ( soi ) , variant of the standard Japanese 醤油 ( shōyu ) . Doublet of shoyu , orthographic borrowing from Middle Chinese 醬油 ( tsjàng-yuw ) , from 醬 ( tsjang H , “ bean paste ” ) + 油 ( “ oil ” ) .
470: Japanese: 大豆   (ja) ( だいず, daizu ) 
1419: English terms borrowed from Dutch 
1420: English terms derived from Japanese 
1421: English terms derived from Dutch 
1514: Terms with Japanese translations
```


## [2026-09-05T14:59:27.528Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN cheragh\"\ngrep -n -i -o '.\\{0,80\\}[cč]ir[aā][gġγ].\\{0,150\\}' HRN.txt | head -8\necho \"=== HUB\"\ngrep -n -i -o '.\\{0,80\\}[cč]ir[aā][gġγ].\\{0,150\\}' HUB.txt | head -8\necho \"=== NYB\"\ngrep -n -i -o '.\\{0,60\\}[cč]ir[aā].\\{0,120\\}' NYB_vol2_glossary.txt | head -8",
 "description": "Grep Horn, Hübschmann, Nyberg for chirag"
}
```


### [2026-09-05T14:59:34.490Z] TOOL RESULT

```
=== HRN cheragh
ugrep: error: error at position 164
xbf][\x80-\xbf]*){0,150}
                        \___exceeds complexity limits


=== HUB
ugrep: error: error at position 164
xbf][\x80-\xbf]*){0,150}
                        \___exceeds complexity limits


=== NYB
ugrep: error: error at position 124
xbf][\x80-\xbf]*){0,120}
                        \___exceeds complexity limits
```


## [2026-09-05T14:59:39.130Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in HRN.txt HUB.txt NYB_vol2_glossary.txt; do\necho \"=== $f\"\ngrep -n -i 'čirāġ\\|čirāγ\\|cirag\\|čarāġ\\|tširāġ\\|čirâġ' \"$f\" | head -6\ndone\necho \"=== HRN grep Lampe\"\ngrep -n -i 'Lampe' HRN.txt | head -8",
 "description": "Grep for chirag in Iranian refs"
}
```


### [2026-09-05T14:59:40.670Z] TOOL RESULT

```
=== HRN.txt
=== HUB.txt
=== NYB_vol2_glossary.txt
=== HRN grep Lampe
```


## [2026-09-05T14:59:46.495Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'چراغ' HRN.txt HUB.txt | head -6\necho \"=== NYB clʾγ\"\ngrep -n -i \"clʾg\\|cl'g\\|clʾγ\" NYB_vol2_glossary.txt PHD.txt | head -6\necho \"=== SOD sogdian crag\"\ngrep -n -i 'čarāγ\\|crʾʾγ\\|چراغ' SOD.txt | head -6",
 "description": "More greps"
}
```


### [2026-09-05T14:59:46.568Z] TOOL RESULT

```
=== NYB clʾγ
=== SOD sogdian crag
```


## [2026-09-05T14:59:58.775Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TTS Hirse\"\ngrep -n -i 'Hirse' incoming/TTS/TTS_pages.txt | head -10\necho \"=== LKT Hirse/soja\"\ngrep -n -i 'Hirse' LKT.txt | head -5",
 "description": "Grep Vambery/Lokotsch for millet"
}
```


### [2026-09-05T14:59:58.839Z] TOOL RESULT

```
=== TTS Hirse
=== LKT Hirse/soja
1026:'Hirse  MiUum'  aus  der  Familie  der Gramineen,  tk.  hüza,  böza  'eine  Art Hirsenbier'  [über  die  Bestandteile  und Bereitung  s.  Silv.  de  Sacy,  Relation  de l'Egypte  par  Abd-Allatif  S.  572].  Hier- aus rum.  bozan  'eine  Art  Bier';  russ. serb.  cech.  poln.  buza,  bulg.  boza  'dass.'; frz.  hoiiza,  bosan  'tk.  Hirsentrank',  dtsch. Busa;  sp.  ps^.  buza.  [Bern  SlEtWb  104. DE  243/244.  Devic  DEt  70.  ZDMG XVni,  705,  Anm.  2.
1407:.551.  Ar.  durra: 'Moorhirse,  Sorghum  vulgare';  hieraus it.  sorgo,  frz.  sorgo,  sorgho;  dtsch.  Sorg- iveizen  [mit  volksetymologischer  An- lehnung an  'Sorge'].  —  [Nach  SPITZER in  WuS  IV,  140ff.  allerdings  eher  aus lat.  *syricum,  m.  E.  jedoch  fraglich.]
```


## [2026-09-05T15:00:12.601Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7633,7705p' incoming/BQT/BQT_v3_pages.txt",
 "description": "Full BQT v3 pdf page 100"
}
```


### [2026-09-05T15:00:12.648Z] TOOL RESULT

```
[pdf page 100]
ات

‎Cle ge‏ » بر وزن موشك » طنبور
‎ly‏ چپار تار راکویند ۱ - وبیمنی تیهولیز
آمدء است ‎Oly‏ عرغی است کوچکتر از کبك.

‏شوشمیر = با میم ‎Vian‏ موش گیر ۰
بمعنی ‎im‏ باشد و بعربی قاقلةٌ مغار و خیربوا
خوالند .

‏شوشی ۲ » بنم هردوشین و سکون‌هر
دو واو » بمعنی کاورس و ارزن باشد ۴ .

‏شوشه ۴ © بروزن‌خوشه. شفشه‌وسبیکةً
طلا و نقره و امثال آن را گوند , وآن جد
کداخته باشدکه در ‎gel bey‏ ریزند - وهر
چیز ‎Vb‏ و کوتاء را لیز گویند مانند لوح
مزار ۴ و محراب مجد وتختهٌ حمام وامثال آن
- وشان وتلامتی را ‎ga‏ کوبند که برسر قبر
شهدا برپای کنند - وريزة حرچیز رالیز گفه‌اند
وهر پخته و بلتدی را گویند ‎ihe, bye‏
‎y‏ خاشاك را خصوصا .

‏(۱) چك : گوسیندان .

‏فوغله

‏شوع » بر وزن دوغ ۰ پینه و آبله را
کرد که ‎cory‏ وپا بسبب‌کارکردن ورامرفتن
بهم رسد ‎٩‏ - وچ رک یکه بربدن وجامه‌شینه ‎٩‏
‏- و بسعنی شوخ هم‌آمد هکه بی‌شرم وبی‌حیاویی
با ‎Vast‏

‎YE gs‏ = بفتح اول بروزن خوغاء,حسار:
رمحرطه ای را گویند که شبها کارانو کوسفندان
وچپار پایان دیگر درآنجا باشند ۵ .

‏شوغار = بنتح ارل بروزن شبکاربیمنی
شوفاست که جای خواییدن چار پایان باشد ‎go‏
‏شب ‎٩‏ - و بضم اول زاج سفید را کوبند ۰

‏شوغاره ۱۳ » بنتح‌اود بروزن‌انگاره»
بدمنی شوفار است که جای خوابیدن کوسفند(۱)
باشد در شپ .

‏شوغاه "۷ ‎Cae‏ اول بروژن خ ‎WS‏
‎Yow‏ شوغاره ( ۲ ) است که جای خوایدن

‎. ‏شوغار‎ : dhe (x)

‏۸ شاشك « رشیدی» «شوشك » ‎hy‏ چپار رودی باشد . فرخی (سیتانی) کوید :

‏گهی سماع زمالی وگاه بربط وچنك

‏۴ از چینی ‎shU‏ (ارزن) . ره :
خری که آبخورش زبر ناودان‌صیر

‏۴ شفده ‎(pe)‏ شیوشه («م.) .

‏۴ - دمد لاله از ‎De Leys‏ من

‏خواجوی ‎SOS‏ .۶ رشیدی».
بسته کف «ست و کف پای‌شوغ

‏کهی چناله وطنبور وشوشك ‎Wing‏ . »
« لت فری ‎LOWE‏

‎Laufer , Sino - Iranica, p . 565

‏علف مصارة بگنی‌وبخم وشوشو.
سوزلی سمرقندی.«رشیدی*. ۰
```


## [2026-09-05T15:00:49.210Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>33600 && NR<33800 && /^[0-9]{3,4}[[:space:]]*$/{print NR\": [\"$0\"]\"}' KLN_1966.txt | head\necho \"---\"\nawk 'NR>35900 && NR<36100 && /^[0-9]{3,4}[[:space:]]*$/{print NR\": [\"$0\"]\"}' KLN_1966.txt | head",
 "description": "Find KLN page numbers"
}
```


### [2026-09-05T15:00:51.125Z] TOOL RESULT

```
---
```


## [2026-09-05T15:00:55.032Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n '^1479$\\|^1383$\\|^1382$\\|^1384$' KLN_1966.txt | head\necho \"--- lines 36020-36030\"\nsed -n '36020,36030p' KLN_1966.txt | cut -c1-100\necho \"--- search 1383 anywhere near\"\nawk 'NR>33500 && NR<33900 && /138[0-9]/{print NR\": \"substr($0,1,80)}' KLN_1966.txt | head",
 "description": "KLN page markers"
}
```


### [2026-09-05T15:00:58.231Z] TOOL RESULT

```
33701:1382
36025:1479
--- lines 36020-36030
source,  n.  —  ME.  sours,  fr.  OF.  sorse,  surse, sorce  (later  source),  fern,  of  sors,  p
souse,  tr.  v.,  1)  to  pickle;  2)  to  soak,  drench;  intr. v.,  to  be  or  become  soaked.  �
Derivative:  souse,  intr.  v.,  to  swoop  down, soutache,  n.,  braid.  —  F.,  fr.  Hung,  sujt
soutane,  n.,  a  cassock  worn  by  Roman  Catholic priests.  —  F.,  fr.  earlier  sottane,  fr.
1478  "
1479
pensatory  lengthening  of  the  vowel — fr.  Old Teut.  *sunp-,  whence  also  OS.,  OFris.  suth
Derivatives:  south,  adj.,  n.,  and  intr.  v.,  south- er-ly,  adj.,  southern  (q.v.),  south-in
Derivatives:  southern-er,  n.,  southern-ize  tr.  v. southron,  n.,  inhabitant  of  the  southern
southward,  southwards,  adv.  —  Compounded  of south  and  adv.  suff.  -ward,  -wards, souvenir
Derivatives:  sovereign-iy,  adv.,  sovereign-ness, n.,  sovereignty  (q.v.)
--- search 1383 anywhere near
33669: 1380'
33701: 1382
33846: 1388  '
```


## [2026-09-05T15:01:05.046Z] TOOL CALL #55: Bash

```json
{
 "command": "cat tools/verify_check.py",
 "description": "Read verify_check tool"
}
```


### [2026-09-05T15:01:05.078Z] TOOL RESULT

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


## [2026-09-05T15:02:26.944Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json\nd=json.load(open('data/verification/page-104.json')) if __import__('os').path.exists('data/verification/page-104.json') else json.load(open('data/verification/page-103.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3500])\n\" 2>&1 | head -60\nls data/verification/*.json | tail -5",
 "description": "Look at prior verification file style"
}
```


### [2026-09-05T15:02:32.971Z] TOOL RESULT

```
Traceback (most recent call last):
  File "<string>", line 3, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'data/verification/page-103.json'
data/verification/page-95.json
data/verification/page-96.json
data/verification/page-97.json
data/verification/page-98.json
data/verification/page-99.json
```


## [2026-09-05T15:02:36.318Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json\nd=json.load(open('data/verification/page-99.json'))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1))\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1))\n\"",
 "description": "Sample prior entry"
}
```


### [2026-09-05T15:02:37.758Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Bistak",
 "verdict": "plausible",
 "modern_form": "Middle Persian pstk' = pistag 'pistachio nut' (< Old Persian *pistaka-, attested in Elamite pi-iš-tuk-ka₄)",
 "note": "The root box is real and the gloss is right: MacKenzie reads the Pahlavi spelling <pstk'> as pistag 'pistachio nut' (A Concise Pahlavi Dictionary p. 74), and Laufer reconstructs Middle Persian *pistak from Old Iranian *pistaka (Sino-Iranica p. 251). The only issue is the transliteration of the root name: Pahlavi book script does not distinguish p from b, so <pstk'> can be read either way, and Nourai (following Unvala and the older transcription practice, and probably influenced by the Greek by-form βιστάκιον recorded by Nicander) prints Bistak; Asbaghi likewise transcribes mp. bistag. The reading accepted today is pistag, guaranteed by Elamite pi-iš-tuk-ka₄ and by New Persian پسته with p-. Hence 'plausible' rather than 'confirmed' — real word, right language, right meaning, non-standard reading of the initial consonant. Further back the word is probably Proto-Iranian *pištaka- 'crushed', from PIE *peys- 'to grind, crush' (Pokorny 796 peis-1), i.e. 'the nut one cracks'.",
 "note_fa": "خانهٔ ریشه «Bistak» در واقع همان واژهٔ فارسی میانه است که در دبیرهٔ پهلوی <pstk'> نوشته می‌شود؛ مکنزی آن را pistag «پسته» می‌خواند (فرهنگ کوچک پهلوی، ص ۷۴) و لاوفر در «سینو-ایرانیکا» (ص ۲۵۱) صورت ایرانی باستان *pistaka و فارسی میانهٔ *pistak را بازسازی می‌کند. چون در خط پهلوی «پ» و «ب» یک نشانه دارند، خواندن bistak نادرست نیست، ولی خوانش پذیرفتهٔ امروزی pistag است، زیرا صورت ایلامی pi-iš-tuk-ka₄ و «پسته»ی فارسی نو هر دو پ دارند. دورتر، این واژه احتمالاً از ایرانی آغازین *pištaka- «کوبیده، شکسته» و ریشهٔ هندواروپایی *peys- «کوفتن، ساییدن» است. نتیجه: ادعای نورایی در اصل درست است، اما آوانویسی آغازهٔ واژه با «ب» با معیار امروزی نمی‌خواند.",
 "sources": [
  "https://en.wiktionary.org/wiki/pstk%27",
  "https://ahdictionary.com/word/search.html?q=pistachio",
  "https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D8%AA%D9%87"
 ],
 "ref_check": [
  {
   "ref": "UNV:78",
   "status": "not_checked",
   "note": "Only the 1917 Heidelberg dissertation of Unvala's 'Der Pahlavi-Text Der König Husrav und sein Knabe' is on disk (refs/UNV.txt, 47 form-feed leaves, printed pp. ≲46), so p. 78 of the 1963 Paris edition (which carries the fuller glossary) could not be reached. The corresponding text passage IS in the scan: §51 'Die hyrkanische Pistaziennuß, wenn man sie auf einem Bräter röstet' and §53 'die frische Pistaziennuß' (UNV.txt lines 608-609), with footnote 51.1 'Ich nehme … und in §52 gleich np. ‘Pistaziennuß’' — i.e. Unvala does gloss the Pahlavi word as the pistachio nut, which is what Nourai cites him for."
  }
 ],
 "consulted": [
  {
   "src": "PHD",
   "where": "p. 74 (leaf 95 of refs/PHD.txt)",
   "stance": "supports",
   "note": "MacKenzie: \"pistag [pstk' | N pista] pistachio nut\"; also in the English-Pahlavi index \"pistachio nut pistag; ~ tree wan ī gurgānīg\" (PHD.txt line 3131). Same word, same gloss, but read with p-."
  },
  {
   "src": "SIN",
   "where": "pp. 246, 251",
   "stance": "supports",
   "note": "Laufer, Sino-Iranica: \"Persian pista, from Old Iranian *pistaka, Middle Persian *pistak, from which is derived Greek βιστάκιον, φιττάκιον, πιστάκιον or ψιττάκιον, Latin psittacium, and our pistacia or pistachio\" (SIN.txt line 726; index s.v. '*pistak 251'). Note that Laufer records the Greek by-form with β-, which is the nearest thing to Nourai's 'Bistak'."
  },
  {
   "src": "NYB",
   "where": "Glossary (vol. II), grep 'pistak|pistag|Pistazie'",
   "stance": "silent",
   "note": "Nyberg's Pahlavi glossary has no entry for the pistachio (only nipištak 'written'); the word does not occur in the texts he glosses."
  },
  {
   "src": "PLA",
   "where": "p. 210 (leaf 225)",
   "stance": "partial",
   "note": "Asbaghi cites the Middle Persian etymon of Arabic fustuq as 'bistag' — the same b-reading Nourai uses — but for her the immediate source is NP peste, not a Pahlavi root box."
  }
 ]
}
{
 "id": 1,
 "lang": "Persian",
 "words": "pesteh",
 "verdict": "confirmed",
 "derivation": "New Persian پسته pesta/peste continues Middle Persian pistag <pstk'> directly: Pahlavi -ag regularly gives NP -a/-e (cf. MP nāmag > NP نامه nāme), so pistag > pista > modern peste. Behind it stand Old Persian *pistaka-, guaranteed by the Elamite Persepolis-tablet spelling pi-iš-tuk-ka₄ /pistaka/ 'pistachio nut', and probably Proto-Iranian *pištaka- 'crushed' (PIE *peys- 'grind, crush'), the tree being native to Sogdiana, Khorasan and Kerman (Laufer, Sino-Iranica 246). The figurative sense 'the beloved's (smiling) lips' that Nourai gives is a standard image of classical Persian poetry — the half-open shell of the ripe pistachio — and is exactly what the Hāfez line quoted in the box plays on («جان فدای شکرین پستهٔ خاموشش باد»: the 'silent pistachio' is the mouth that will not speak).",
 "derivation_fa": "«پسته» در فارسی نو دنبالهٔ مستقیم فارسی میانهٔ pistag (نوشتهٔ پهلوی <pstk'>) است؛ پسوند ـag پهلوی در فارسی نو به ـه بدل می‌شود (مانند nāmag > نامه)، پس pistag > پسته. پیش از آن ایرانی باستان *pistaka- را داریم که صورت ایلامی pi-iš-tuk-ka₄ در گِل‌نبشته‌های تخت‌جمشید گواه آن است، و احتمالاً از ایرانی آغازین *pištaka- «کوبیده» از ریشهٔ هندواروپایی *peys- «ساییدن، کوفتن». کاربرد مجازی «پسته» برای لبِ خندانِ معشوق نیز از تصویرهای رایج شعر فارسی است (پوستِ نیم‌شکافتهٔ پستهٔ رسیده)، چنان‌که در بیت حافظِ همین خانه «پستهٔ خاموش» یعنی دهانِ فروبستهٔ یار. نتیجه: ادعای نورایی درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D8%AA%D9%87",
  "https://en.wiktionary.org/wiki/pstk%27",
  "https://ahdictionary.com/word/search.html?q=pistachio"
 ],
 "ref_check": [
  {
   "ref": "PLA:210",
   "status": "supports",
   "note": "Asbaghi, Persische Lehnwörter im Arabischen p. 210 (leaf 225 of PLA_pages.txt), s.v. fustuq: \"fustuq: 'Pistazie' … pers. peste … mp. … bistag … Pistazie pers. > griech. > lat. > frz. pistache\" — the Persian word peste is the starting point of her chain, as in Nourai's chart."
  },
  {
   "ref": "AHD:998",
   "status": "supports",
   "note": "AHD s.v. pistachio: \"…from Greek pistakē, pistachio tree, of Iranian origin; akin to Middle Persian pistag\" (ahdictionary.com/word/search.html?q=pistachio) — the Iranian word is the source, as Nourai draws it."
  }
 ],
 "consulted": [
  {
   "src": "BQT",
   "where": "vol. 1, Mo'in's footnote 5 s.v. پسته (BQT_v1_pages.txt line 25742, leaf 630)",
   "stance": "partial",
   "note": "«پسته: بکسر اول و سکون سوم، در تازی فستق از آرامی فستقا (بکسر اول)، چه منشأ آن شام (سوریه) است و به یونانی نقل شد pistakion و از آن به دیگر زبانهای اروپایی داخل شد. در ایتالیایی pistacchio…» — Mo'in has the Persian word but sends the Arabic (and through it the Greek) back to Aramaic, i.e. he does not derive the European words from Persian."
  },
  {
   "src": "MON",
   "where": "s.v. پسته (MON_part1.txt line 31751)",
   "stance": "partial",
   "note": "«پسته: [آرا. فستقا] (اِ.) (گیا.) درختی از تیرهٔ سماقی‌ها…» — Mo'in tags the headword as Aramaic فستقا, not as an inherited Iranian word; he has the tree native to Syria/Afghanistan/Khorasan."
  },
  {
   "src": "SIN",
   "where": "pp. 246-251",
   "stance": "supports",
   "note": "\"The pistachio (Pistacia vera) in particular is indigenous to ancient Sogdiana and Khorasan\"; \"Persian pista, from Old Iranian *pistaka, Middle Persian *pistak, from which is derived Greek βιστάκιον … πιστάκιον\" — Persian is the source, not the borrower."
  },
  {
   "src": "PHD",
   "where": "p. 74",
   "stance": "supports",
   "note": "\"pistag [pstk' | N pista] pistachio nut\" — MacKenzie himself equates the Pahlavi word with New Persian pista."
  },
  {
   "src": "HRN",
   "where": "grep 'pista|piste' in HRN.txt",
   "stance": "silent",
   "note": "Horn's Grundriss has no entry for پسته (only the unrelated nipištan 'write' and a passing 'wilde Pistazie (?)' at no. 133); a fruit-name of this kind fell outside his selection."
  }
 ]
}
```


## [2026-09-05T15:02:43.999Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FRS shosho\"; grep -n 'شوشو' FRS_pages.txt FSF_pages.txt 2>/dev/null | head -5\necho \"=== RCH shusho\"; grep -n -i 'shushu\\|shúshú\\|shusho' RCH.txt | head -5\necho \"=== PHN/DEV soja\"; grep -n -i 'soja\\|soya' PHN.txt DEV.txt LAM.txt 2>/dev/null | head -5\necho \"=== ARY sowya\"; grep -n 'سویا' incoming/ARY/ARY_pages.txt 2>/dev/null | head -3\necho \"=== MON soya\"; grep -n 'سویا' MON_part1.txt MON_part2.txt | head -5",
 "description": "Final local greps"
}
```


### [2026-09-05T15:02:44.128Z] TOOL RESULT

```
=== FRS shosho
=== RCH shusho
53424:pyAy.!  shushuy  Millet.
85409:A   mashush  (also j^\  mashushuH  ghamari)y  A
=== PHN/DEV soja
=== ARY sowya
=== MON soya
MON_part2.txt:40714:فول‌صویه؛ سویا. لوییای سبز: (گیا.) قسمی 
MON_part2.txt:68065:سخت (از قبل دانه‌ها و حسویات و غیره) 
MON_part2.txt:76577:نصرانی؛ عیسویان؛ مسیحیان. ضح.- در 
MON_part2.txt:79478:رسویات در ضمن چین خوردگی‌ها وجود 
MON_part2.txt:93447:کسویال» زورسندی (فرعا.جما.) یال و
```


## [2026-09-05T15:02:48.022Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://vajehyab.com/?q=%D8%B3%D9%88%DB%8C%D8%A7&d=moein' --note 'page 105, Persian سویا loanword check (Moin)' 2>&1|tail -1\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/%C4%8Dir%C4%81%C4%8Dah' --note 'page 105, Proto-Iranian chirag check' 2>&1|tail -1\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/soya' --note 'page 105, soya English' 2>&1|tail -1",
 "description": "Fetch remaining web sources"
}
```


### [2026-09-05T15:02:51.111Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/123cc88dc937f12a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5e0b29b559b719f2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b920ef231df0d1fb.txt
```


## [2026-09-05T15:02:56.664Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '53420,53428p' RCH.txt | cut -c1-300\necho \"=== MON 40714\"\nsed -n '40710,40718p' MON_part2.txt",
 "description": "Richardson and Moin context"
}
```


### [2026-09-05T15:02:56.731Z] TOOL RESULT

```
A   L.>^AyA  shazBshaby  A   scorpion.  An  ant. p Shushtary  Name  of  a   city  in  Khuzistan. p   shuskady  Sepulchral  stones.  Chips,  rubbish.  A   heap
of  sand.  Gold  or  silver  thread.
p   C^J^yL  shaxeshak  or  shushaky  A   kind  of  violin,  with  a   large belly,  long  neck,  and  four  strings.  A   sort  of  partridge.
p shushmishlr  (or  shushfntr)y  Cardamum,
pyAy.!  shushuy  Millet.
A   j^yA  shu^shu^ay  A   word  used  in  calling  an  ass. p   AJ^y^  shushaky  An  ingot  of  gold  or  silver.  Gold  or  silver thread.  Chips,  rubbish,  filth.  A   heap  of  sand.  A   grave-stone. A   particle,  a   part.  iJLyit  shusha^i  khurmdy  A   branch  or
bunch  of  dates.*
A   (jflyA  shazos  also  shazoas  (from  ^y.il»).  Cleaning,  washing, rubbing.  Doing  or  holding  a   thing  right.  Having  the  tooth- ache. Leaping  in  the  womb  (a  foetus).
A   shazesaty  A   puffiness  of  the  skin  above  the  ribs.
=== MON 40714
اهمست فراوانی که در تغدبه انسان دارد در 
غالب نقاط کشت می‌شود؛ لویبای چنی؛ 


فول‌صویه؛ سویا. لوییای سبز: (گیا.) قسمی 
لوییا که فقط به منظور استفاده از میوه‌اش در 
حالی که هنوز دانه‌ها نارس می‌باشند کشت 
می‌شود. میوةٌ نارس لوبیا که به شکل میوة 
ساقلا سبز رنگ است در اغذبه مصرت
```


## [2026-09-05T15:02:58.883Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== vajehyab soya\"; sed -n '1,40p' 123cc88dc937f12a.txt | grep -n 'سویا\\|پیدا نشد\\|معین' | head -10\necho \"=== proto-iranian\"; head -8 5e0b29b559b719f2.txt\necho \"=== etymonline soya\"; grep -n -A4 'soya (n' b920ef231df0d1fb.txt | head -12",
 "description": "Check fetched pages"
}
```


### [2026-09-05T15:02:58.948Z] TOOL RESULT

```
=== vajehyab soya
4:TITLE: معنی سویا | واژه یاب
9: معنی سویا | واژه یاب 
18: سویا
30: سویا
31: فرهنگ انتشارات معین
37: فرهنگ انتشارات معین
38: (سُ) [ فر. ] (اِ.) از انواع فرآورده های گوشتی است که از گوشت چرخ کردة بسیار ریز و چربی و سویا درست شده است و با روکش نایلونی استوانه ای شکل عرضه می شود.
=== proto-iranian
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/%C4%8Dir%C4%81%C4%8Dah
FETCHED: 2026-09-05T15:02:50Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found=== etymonline soya
23: soya (n.) 
24-
25- "soy," 1670s; see soy . Soyaburger is attested from 1953.
26- also from 1670s 
27-
```


## [2026-09-05T15:03:08.320Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '15,70p' 123cc88dc937f12a.txt",
 "description": "Read vajehyab soya page"
}
```


### [2026-09-05T15:03:08.363Z] TOOL RESULT

```
 همه دقیق مشابه آوا متن آغاز قافیه 

 سویا
 soyā
 معنی

 ۱. گیاهی با برگ‌های درشت، گل‌های سفید یا بنفش، و ساقه‌های پوشیده از تارهای سفید که بلندیش تا یک متر می‌رسد.
۲. دانه‌های این گیاه که به درشتی لوبیا، به رنگ زرد، سرخ، یا سفید که در غلافی شبیه غلاف لوبیا جا دارد و دارای مواد غذایی بسیار مفید است؛ نخود چینی؛ خلر چینی.
 دیکشنری

 soybean

 جست‌وجوی دقیق

 سویا
 فرهنگ انتشارات معین
 (سُ) [ انگ / فر. ] (اِ.) گیاهی علفی و یکساله از تیرة پروانه واران با ساقه های پوشیده از تارهای سفید، برگ های متناوب و مرکب از سه برگچه ، گل های سفید مایل به بنف

 جست‌وجوی متن

 سوسیس
 فرهنگ انتشارات معین
 (سُ) [ فر. ] (اِ.) از انواع فرآورده های گوشتی است که از گوشت چرخ کردة بسیار ریز و چربی و سویا درست شده است و با روکش نایلونی استوانه ای شکل عرضه می شود.

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره
```


## [2026-09-05T15:05:20.956Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON اشراق\"; grep -n 'اشراق' MON_part1.txt | head -4\necho \"=== MON مستشرق\"; grep -n 'مستشرق' MON_part2.txt | head -3\necho \"=== BQT اشراق\"; grep -n 'اشراق' BQT_v1_pages.txt | head -4",
 "description": "Grep for eshraq in Persian dicts"
}
```


### [2026-09-05T15:05:21.037Z] TOOL RESULT

```
=== MON اشراق
247:۲ - حکمت اشراق و فرهنگ ایران (از انتشارات مجلةٌ آموزش و پرورش 
13363:اشراق: 2 [ع.] (مصل.) تافتن» تابیدن» 
13366:حکمت اشراق: فلسفه‌ای که در اسلام مروج 
13368:اشراقات. 
=== MON مستشرق
56159:مق. مستشرق؛ ج. مستغر بین. 
=== BQT اشراق
1899:اشراقیابران و وخشوران باستان بیان میکند - دیگ رکتاب موسوم به «چشمةٌ زندکی» و « زنده
26969:«اسشق ۰.۳۶۲ ۴ رث: حکمت اشراق تألف نگارنده ص ۱۰ .  *‏ رك : بهلوی.
```


## [2026-09-05T15:05:26.614Z] TOOL CALL #64: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg105.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/105.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Archive page image"
}
```


### [2026-09-05T15:05:26.682Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T15:05:29.111Z] TOOL CALL #65: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/105.png",
 "description": "Confirm copy"
}
```


### [2026-09-05T15:05:29.148Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/105.png
```


## [2026-09-05T15:05:30.847Z] AGENT

Now I'll write the verification file.


## [2026-09-05T17:21:26.399Z] AGENT

I'll write the verification file now.


## [2026-09-05T17:24:55.466Z] TOOL CALL #66: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk105.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_CHERAGH = \"https://en.wiktionary.org/wiki/%DA%86%D8%B1%D8%A7%D8%BA\"\nW_SIRAJ   = \"https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%A7%D8%AC\"\nW_SHARQ   = \"https://en.wiktionary.org/wiki/%D8%B4%D8%B1%D9%82\"\nE_SARACEN = \"https://www.etymonline.com/word/Saracen\"\nE_SOY     = \"https://www.etymonline.com/word/soy\"\nE_SOYA    = \"https://www.etymonline.com/word/soya\"\nW_SOY     = \"https://en.wiktionary.org/wiki/soy\"\nV_SOYA    = \"https://vajehyab.com/?q=%D8%B3%D9%88%DB%8C%D8%A7&d=moein\"\nV_SHOSHO  = \"https://vajehyab.com/?q=%D8%B4%D9%88%D8%B4%D9%88&d=moein\"\n\ndoc = {\n \"pdf_page\": 105,\n \"book_page\": 75,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": []\n}\n\n# ---------------------------------------------------------------- entry 3\ne3 = {\n \"entry\": 3,\n \"root\": \"Chiang-yu\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Chinese 醬油 jiàng-yóu (Middle Chinese tsjàng-yuw) 'soy sauce', literally '(fermented) bean-paste oil' = 醬 jiàng 'bean paste, sauce' + 油 yóu 'oil'\",\n \"note\": \"The root box is real and is copied verbatim from the reference Nourai cites: Klein p.1479 s.v. soy has \\\"Jap. shoyu, fr. Chin. chiang-yu, lit. 'soybean oil'\\\". The compound is Mandarin 醬油 jiàngyóu, still the ordinary word for soy sauce, and Japanese 醤油 shōyu is an orthographic borrowing of it (Middle Chinese tsjàng-yuw); the literal sense is better rendered 'bean-paste oil' than 'soybean oil', since 醬 is the fermented paste, not the bean. Etymonline offers a competing analysis of which Chinese compound the Japanese word renders — the southern 豉油 shi-yu 'fermented-soybean oil' (Cantonese si-yau) — but both analyses agree that the European words go back through Japanese to a Chinese X-油 'oil' compound, so the root box stands. What the chart under-states is the Japanese stage: it is relegated to the root's own side-note ('Entered Japanese as shôyŭ') and to the OXF note on the Dutch box, instead of being a node (see #1).\",\n \"note_fa\": \"خانهٔ ریشه درست است و عیناً از منبعی که نورایی یاد کرده گرفته شده: کلاین در ص ۱۴۷۹ ذیل soy می‌نویسد «ژاپنی shoyu، از چینی chiang-yu به معنی تحت‌اللفظی روغن سویا». صورت چینی همان 醬油 jiàng-yóu است (چینی میانه tsjàng-yuw) که هنوز واژهٔ رایج «سس سویا» است و ژاپنی 醤油 shōyu وام‌گیریِ نوشتاری همان است؛ معنای تحت‌اللفظی دقیق‌تر «روغنِ خمیرِ لوبیای تخمیری» است نه «روغن سویا»، چون 醬 همان خمیر تخمیری است. اتیمانلاین صورت جنوبی 豉油 shi-yu را پیشنهاد می‌کند، ولی هر دو تحلیل بر سر چینی‌بودن سرچشمه و میانجی‌بودن ژاپنی هم‌داستان‌اند. نتیجه: ادعای نورایی درست است، جز آنکه مرحلهٔ ژاپنی را به جای گره، در حاشیه آورده است.\",\n \"sources\": [E_SOY, W_SOY],\n \"ref_check\": [\n   {\"ref\": \"KLN:1479\", \"status\": \"supports\",\n    \"note\": \"Klein 1966 ed., page marker '1479' at KLN_1966.txt line 36025, entry at line 36036: \\\"soy, n., 1) a Chinese or Japanese sauce for fish made from soybean; 2) soybeans. — Jap. shoyu, fr. Chin. chiang-yu, lit. 'soybean oil'. soybean, soya-bean, n. — See prec. word.\\\" Root name, language and gloss are Klein's own words.\"},\n   {\"ref\": \"AHD:1237\", \"status\": \"not_checked\",\n    \"note\": \"AHD:1237 is a page of the main word-list of the New College edition (1975/76), not of the Indo-European appendix; only Watkins' 1985 IE-roots volume is on disk (AHD_watkins1985.txt), and the New College scans on archive.org are lending-only. The online AHD search page for 'soy' returns only the site's JavaScript boilerplate to a plain fetch.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1479 s.v. soy\", \"stance\": \"supports\",\n    \"note\": \"\\\"Jap. shoyu, fr. Chin. chiang-yu, lit. 'soybean oil'\\\" — the exact wording Nourai's root box reproduces.\"},\n   {\"src\": \"SKT\", \"where\": \"p. 453 s.v. Soy (SKT.txt lines 17916-17917)\", \"stance\": \"partial\",\n    \"note\": \"Skeat: \\\"Soy, a sauce. (Japanese.) Also sooju … Japanese shôyu, soy … the name is now given to the bean (Dolichos soja) whence soy is made.\\\" Skeat stops at Japanese and does not name the Chinese compound.\"},\n   {\"src\": \"FSD\", \"where\": \"vol. 4 s.v. soy (FSD_vol4.txt line 15596)\", \"stance\": \"silent\",\n    \"note\": \"Funk & Wagnalls defines \\\"Soy: A sauce or liquid condiment prepared in China and Japan from the soy-bean with other ingredients, generally known as Japan soy or Chinese soy\\\", but the bracketed etymology is lost in the OCR of this column; no etymological statement recoverable.\"},\n   {\"src\": \"LKT\", \"where\": \"grep 'soja|soya' in LKT.txt\", \"stance\": \"silent\",\n    \"note\": \"Lokotsch's dictionary of European words of Oriental origin has no soja/soya entry — his 'Orient' is the Semitic/Turco-Persian one, not the Far East.\"}\n ],\n \"nodes\": []\n}\n\ne3[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Dutch\", \"words\": \"soja\", \"verdict\": \"plausible\",\n \"derivation\": \"Dutch soja is real (17th c.) but is not taken straight from Chinese as the arrow draws: it is a Japanese loan, brought home by the Dutch East India Company, whose Deshima factory was the only European trading post in Japan from 1641. The immediate source is the Satsuma/Kyushu pronunciation of Japanese 醤油 (soi, beside standard shōyu), which the Dutch spelled soja; 醤油 in turn is the orthographic borrowing of Chinese 醬油. Klein, the reference cited on this very box, has exactly that order (chiang-yu > Jap. shoyu > Eng. soy) and knows no Dutch step at all, while OXF:406 — quoted in Nourai's own note here — supplies the missing Japanese stage. Etymonline states the route and the reason: \\\"from Dutch soya, from Japanese soyu, variant of shoyu … The etymology reflects Dutch presence in Japan before English and American merchants began to trade there.\\\" So: right word, right language, right ultimate origin, one stage omitted; the NOTE in the box is correct and modern scholarship sides with it.\",\n \"derivation_fa\": \"«soja»ی هلندی واژه‌ای اصیل از سدهٔ ۱۷ م است، اما آن‌گونه که پیکان نمودار نشان می‌دهد یکسره از چینی گرفته نشده؛ وام‌واژه‌ای ژاپنی است که کمپانی هند شرقی هلند از تجارتگاه دِشیما (تنها پایگاه اروپایی در ژاپن از ۱۶۴۱ م) به اروپا برد. خاستگاه بی‌واسطهٔ آن تلفظ ساتسوما/کیوشوی 醤油 ژاپنی یعنی soi است (در برابر گونهٔ معیار shōyu) که هلندی‌ها soja نوشتند، و خودِ 醤油 وام‌گیریِ نوشتاری 醬油 چینی است. جالب آنکه کلاین، همان مرجعی که نورایی برای این خانه آورده، اصلاً نامی از هلندی نمی‌برد و زنجیره را چینی › ژاپنی › انگلیسی می‌داند، و یادداشت خودِ نورایی (به نقل از OXF:۴۰۶) همین حلقهٔ ژاپنی را می‌افزاید. نتیجه: با احتیاط پذیرفتنی است؛ واژه و زبان درست‌اند ولی یک مرحله (ژاپنی) از نمودار افتاده است و حاشیهٔ خودِ کتاب حق دارد.\",\n \"sources\": [E_SOY, W_SOY],\n \"ref_check\": [\n   {\"ref\": \"KLN:1479\", \"status\": \"partial\",\n    \"note\": \"Klein p.1479 has the Chinese and the Japanese but no Dutch: \\\"soy … — Jap. shoyu, fr. Chin. chiang-yu\\\". He therefore supports the Chinese etymon of the box but not the arrow Chinese→Dutch drawn here.\"}\n ],\n \"consulted\": [\n   {\"src\": \"DOZ\", \"where\": \"grep 'soja|soya' in DOZ.txt\", \"stance\": \"silent\",\n    \"note\": \"Dozy's 'Oosterlingen' — a list of exactly this kind, Dutch words of Eastern origin — has no soja entry; his scope is Arabic/Hebrew/Persian/Turkish, not Japanese.\"},\n   {\"src\": \"LKT\", \"where\": \"grep 'soja|soya' in LKT.txt\", \"stance\": \"silent\",\n    \"note\": \"No entry in Lokotsch either.\"},\n   {\"src\": \"SKT\", \"where\": \"p. 453 s.v. Soy\", \"stance\": \"partial\",\n    \"note\": \"\\\"Soy, a sauce. (Japanese.)\\\" — Skeat labels the word Japanese, i.e. agrees with the OXF note on this box against the direct Chinese→Dutch arrow.\"},\n   {\"src\": \"WEB\", \"where\": \"grep 'soy, n' in WEB_vol1.txt\", \"stance\": \"silent\",\n    \"note\": \"The available Webster volume does not cover the S-range of the word list; nothing found.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 2, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"plausible\",\n \"derivation\": \"An empty pass-through box, and a reasonable one: French soja (also soya) is a borrowing of the Dutch word, spread through botany — Linnaeus' binomial Dolichos soja / Glycine soja is built on the Dutch form — and it is the French shape of the word, with its final vowel, that stands behind modern Persian سویا rather than English soy. The book gives no reference at all for this box, so nothing of Nourai's own could be checked; the arrow is judged plausible on the strength of Mo'in, who tags Persian سویا '[انگ / فر.]', i.e. English or French, thereby allowing but not compelling the French route.\",\n \"derivation_fa\": \"این خانه گذرگاهی و بی‌واژه است و پذیرفتنی می‌نماید: soja/soya در فرانسه وام‌واژه‌ای از هلندی است که از راه گیاه‌شناسی گسترش یافت — نام دوجزئی لینه، Dolichos soja و Glycine soja، بر پایهٔ همان صورت هلندی ساخته شده — و همین صورت فرانسوی با واکهٔ پایانی است که پشتوانهٔ «سویا»ی فارسی امروز است، نه soy انگلیسی. کتاب برای این خانه هیچ مأخذی نیاورده، پس ادعای خودِ نویسنده وارسی‌شدنی نبود؛ داوری «با احتیاط پذیرفتنی» بر پایهٔ فرهنگ معین است که «سویا» را [انگ / فر.] برچسب می‌زند، یعنی راه فرانسوی را ممکن می‌داند ولی الزامی نمی‌کند.\",\n \"sources\": [V_SOYA],\n \"ref_check\": [\n   {\"ref\": \"(none printed in the box)\", \"status\": \"not_checked\",\n    \"note\": \"The French box carries no refs= at all in the book (confirmed on the page image, data/verification/sources/refs/ocr/BOOK/105.png), so there is no citation of Nourai's to test.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. سویا (vajehyab.com/?q=سویا&d=moein)\", \"stance\": \"partial\",\n    \"note\": \"«سویا (سُ) [ انگ / فر. ] (اِ.) گیاهی علفی و یکساله از تیرهٔ پروانه‌واران…» — Mo'in tags the word English *or* French, so French is one of the two routes Persian lexicography records, not the only one.\"},\n   {\"src\": \"PHN\", \"where\": \"grep 'soja|soya' in PHN.txt\", \"stance\": \"silent\",\n    \"note\": \"Pihan's dictionary of French words from Arabic/Persian/Turkish has no soja — as expected, the word is not Oriental in his sense.\"},\n   {\"src\": \"DEV\", \"where\": \"grep 'soja|soya' in DEV.txt\", \"stance\": \"silent\",\n    \"note\": \"Devic likewise has no entry.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"soyâ\", \"verdict\": \"plausible\",\n \"derivation\": \"Persian سویا soyâ is a twentieth-century European loanword — the plant (Glycine max) reached Iranian agriculture only in the modern period, and the word travels with the crop and the food industry, not with any older trade route. Mo'in's Farhang tags the headword «سویا (سُ) [ انگ / فر. ] (اِ.)», i.e. from English or from French, so the French arrow Nourai draws is one of the two possibilities Persian lexicography records; the spelling with final ـا (soyâ, not *soy) does point to the French/Latin-botanical form soja/soya rather than to English soy, which is a small argument in Nourai's favour. Mo'in elsewhere also glosses the bean as «لوبیای چینی؛ فول‌صویه؛ سویا». VOP:224 — Moshiri's dictionary of European words in Persian — is precisely the right authority for this box, but no digital copy of it exists anywhere (see refs_online.json), so Nourai's own citation could not be tested.\",\n \"derivation_fa\": \"«سویا» در فارسی وام‌واژه‌ای اروپایی از سدهٔ چهاردهم خورشیدی است؛ خودِ گیاه (Glycine max) نیز تازه در دورهٔ نو وارد کشاورزی ایران شد و واژه همراه محصول و صنعت غذایی آمده است، نه از راه بازرگانی کهن. معین در فرهنگ خود سرواژه را «سویا (سُ) [ انگ / فر. ] (اِ.)» می‌نویسد، یعنی وام‌گرفته از انگلیسی یا فرانسوی؛ پس راه فرانسوی که نورایی کشیده یکی از دو راهی است که فرهنگ‌نویسی فارسی می‌شناسد. املای واژه با «ا»ی پایانی (سویا، نه *سوی) به صورت فرانسوی/گیاه‌شناسیِ لاتینی soja/soya می‌ماند نه به soy انگلیسی، و این نکته اندکی به سود نورایی است. مأخذ خودِ او (VOP:۲۲۴، فرهنگ واژه‌های اروپایی در فارسیِ مشیری) هیچ نسخهٔ دیجیتالی ندارد و وارسی‌نشدنی ماند.\",\n \"sources\": [V_SOYA, W_SOY],\n \"ref_check\": [\n   {\"ref\": \"VOP:224\", \"status\": \"not_checked\",\n    \"note\": \"Mahshid Moshiri, Farhang-e Vāžehā-ye Orupāyi dar Fārsi (Alborz 1371/1992): refs_online.json records kind='none' — searched archive.org, ketabnak, noorlib and the open web, no scan and no ebook exists; only second-hand purchase. Nothing of this citation could be checked.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. سویا (vajehyab, Farhang-e Mo'in) and s.v. لوبیا (MON_part2.txt line 40714)\", \"stance\": \"supports\",\n    \"note\": \"«سویا (سُ) [ انگ / فر. ] (اِ.)» — a European loan, English or French; and under the bean «…لوبیای چینی؛ فول‌صویه؛ سویا». Mo'in confirms both the word and its European origin, though he leaves English open beside French.\"},\n   {\"src\": \"ARY\", \"where\": \"grep 'سویا' in ARY_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur's dictionary of Indo-European roots of Persian has no entry — it treats inherited vocabulary, and a modern European loan falls outside it.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"soya, soy\", \"verdict\": \"confirmed\",\n \"derivation\": \"English soy is first recorded in the 1670s (as saio, of the Asian fish sauce) and comes from Dutch soja, exactly as the chart draws; soya is the same borrowing keeping the Dutch final vowel, and is the form that supplies soya bean, soya milk. Etymonline: \\\"1670s, saio 'soybean-based Asian fish sauce', from Dutch soya, from Japanese soyu, variant of shoyu 'soy', from Chinese … The etymology reflects Dutch presence in Japan before English and American merchants began to trade there\\\"; Wiktionary agrees, \\\"borrowed from Dutch soja, from the Satsuma pronunciation of Japanese 醤油 (soi)\\\". Klein, by contrast, takes English soy straight from Japanese shoyu with no Dutch step, so Nourai's Dutch→English arrow follows OXF rather than KLN — and OXF is right. Soy sauce is attested from 1795.\",\n \"derivation_fa\": \"«soy» انگلیسی نخستین‌بار در دههٔ ۱۶۷۰ م (به صورت saio، نامِ سسِ ماهیِ خاور دور) ثبت شده و از هلندیِ soja گرفته شده است — دقیقاً همان پیکانی که نورایی کشیده؛ گونهٔ soya همان وام‌واژه است با واکهٔ پایانیِ هلندی، و ترکیب‌هایی چون soya bean از آن ساخته شده. اتیمانلاین می‌نویسد: «از هلندیِ soya، از ژاپنیِ soyu، گونهٔ shoyu … این ریشه‌شناسی بازتاب حضور هلندی‌ها در ژاپن پیش از بازرگانان انگلیسی و آمریکایی است»، و ویکی‌واژه نیز آن را «وام‌گرفته از هلندیِ soja، از تلفظ ساتسومایِ 醤油 ژاپنی (soi)» می‌داند. کلاین در برابر، soy انگلیسی را یکسره از ژاپنی می‌گیرد و هلندی را نادیده می‌نهد؛ پس نورایی در اینجا از OXF پیروی کرده و حق با اوست. نتیجه: ادعای نورایی درست است.\",\n \"sources\": [E_SOY, E_SOYA, W_SOY],\n \"ref_check\": [\n   {\"ref\": \"OXF:406\", \"status\": \"not_checked\",\n    \"note\": \"J. Speake, Oxford Dictionary of Foreign Words and Phrases (1997): refs_online.json marks it archive_restricted — borrowable only (oxforddictionary00spea), no full text obtainable. Its claim as reported in the box (Dutch via Japanese shōyu) is independently confirmed by Etymonline and Wiktionary, so the citation is at least substantively right.\"},\n   {\"ref\": \"AHD:1152\", \"status\": \"not_checked\",\n    \"note\": \"Not cited on this node; listed here only for completeness — no AHD reference appears on the English soy box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1479 s.v. soy\", \"stance\": \"partial\",\n    \"note\": \"\\\"soy … — Jap. shoyu, fr. Chin. chiang-yu\\\" — Klein derives the English word directly from Japanese, omitting the Dutch intermediary that Nourai (with OXF) draws.\"},\n   {\"src\": \"SKT\", \"where\": \"p. 453 s.v. Soy\", \"stance\": \"partial\",\n    \"note\": \"\\\"Soy, a sauce. (Japanese.) … the name is now given to the bean (Dolichos soja) whence soy is made\\\" — Japanese source, no Dutch step, but note that Skeat's bean-name soja is the Dutch/Latin form.\"},\n   {\"src\": \"FSD\", \"where\": \"vol. 4 s.v. soy\", \"stance\": \"silent\",\n    \"note\": \"Definition only ('a sauce or liquid condiment prepared in China and Japan from the soy-bean…'); the etymology bracket is illegible in the OCR.\"}\n ]\n})\n\ndoc[\"entries\"].append(e3)\n\n# ---------------------------------------------------------------- entry 4\ne4 = {\n \"entry\": 4,\n \"root\": \"Chou-shu, Shu-shu\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Chinese 黍 shǔ 'broomcorn millet (Panicum miliaceum)'; the compound Laufer actually prints on the cited page is šu-lu, not a reduplicated *shu-shu\",\n \"note\": \"The Chinese element is real — 黍 shǔ is the classical word for broomcorn millet — and Mo'in states the loan flatly: in his footnote 4 to Borhan-e Qāṭeʿ p.1309 he writes «۴ از چینی shū (ارزن). ره: Laufer, Sino-Iranica, p. 565». But Laufer himself, on that very page, is far more guarded and gives no such headword. His §29 (SIN pp.565-566) reads: \\\"The Cou li states that in respect to the five cereals … rice and millet are lacking in Persia. The term 'millet' is expressed by the compound šu-lu; that is, the glutinous variety of Panicum miliaceum and the glutinous variety of the spiked millet (Setaria italica glutinosa). Now, we find in Persian a word [شوشو] in the sense of 'millet'. It remains to study the history of this word, in order to ascertain whether it might be a Chinese loan-word.\\\" So Laufer neither prints 'Chou-shu, Shu-shu' nor asserts the derivation; a reduplicated Chinese *shu-shu is not otherwise attested, and the doubling may as easily have happened inside Persian. Real Chinese material, right general idea, but the root box as a Chinese lexeme is Nourai's (or Mo'in's) construct, and the loan is unproven at source — hence 'plausible'.\",\n \"note_fa\": \"عنصر چینی واقعی است — 黍 (shǔ) واژهٔ کلاسیک «ارزن» است — و معین در حاشیهٔ ۴ بر برهان قاطع ص ۱۳۰۹ صریح می‌نویسد: «۴ از چینی shū (ارزن). ره: Laufer, Sino-Iranica, p. 565». اما خودِ لاوفر در همان صفحه بسیار محتاط‌تر است و چنین سرواژه‌ای ندارد: در بند ۲۹ (صص ۵۶۵–۵۶۶) ترکیبِ چینیِ «ارزن» را šu-lu می‌آورد و دربارهٔ واژهٔ فارسی تنها می‌نویسد «تاریخ این واژه هنوز باید بررسی شود تا روشن گردد آیا وام‌واژه‌ای چینی است یا نه». پس نه صورت «Chou-shu, Shu-shu» در آن صفحه هست و نه حکمی قطعی؛ صورت مضاعفِ چینی *shu-shu نیز جای دیگر گواهی ندارد و دوگان‌سازی می‌تواند در خودِ فارسی رخ داده باشد. نتیجه: با احتیاط پذیرفتنی است؛ مایهٔ چینی درست است اما خانهٔ ریشه ساختهٔ نویسنده (یا برگرفته از حاشیهٔ معین) است و وام‌گیری در سرچشمه اثبات‌نشده مانده.\",\n \"sources\": [V_SHOSHO],\n \"ref_check\": [\n   {\"ref\": \"SIN:565\", \"status\": \"partial\",\n    \"note\": \"Laufer, Sino-Iranica p.565-566 (leaves 393-394 of refs/SIN.txt; leaf = printed − 172), §29: \\\"The term 'millet' is expressed by the compound šu-lu … Now, we find in Persian a word [شوشو] in the sense of 'millet.' It remains to study the history of this word, in order to ascertain whether it might be a Chinese loan-word.\\\" The page has the Persian word and the Chinese millet vocabulary, but neither the form 'Chou-shu, Shu-shu' nor an assertion that the Persian word is Chinese.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol. 3 printed p. 1309 = pdf page 100 (incoming/BQT/BQT_v3_pages.txt line 7703 and the footnote block above it)\", \"stance\": \"supports\",\n    \"note\": \"Mo'in's footnote 4 on the شوشو entry: «۴ از چینی shU (ارزن) . ره : Laufer , Sino - Iranica, p . 565» — Mo'in does affirm the Chinese origin, and cites exactly the Laufer page Nourai cites.\"},\n   {\"src\": \"SIN\", \"where\": \"pp. 565-566, §29\", \"stance\": \"partial\",\n    \"note\": \"See ref_check: Laufer raises the question and leaves it open; he also notes Schlimmer's erzen as the Persian word for Panicum miliaceum.\"},\n   {\"src\": \"MON\", \"where\": \"vajehyab.com/?q=شوشو&d=moein; grep 'شوشو' in MON_part1/part2 and the Adena 2-vol djvu\", \"stance\": \"silent\",\n    \"note\": \"«شوشو» پیدا نشد! — the online Farhang-e Mo'in has no such headword, and the local OCR of Mo'in does not contain the string either.\"},\n   {\"src\": \"LKT\", \"where\": \"grep 'Hirse' in LKT.txt\", \"stance\": \"silent\",\n    \"note\": \"Lokotsch's millet entries (s.v. boza, durra) concern Turkic and Arabic grain words; nothing on a Chinese/Mongol šušu.\"}\n ],\n \"nodes\": []\n}\n\ne4[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Mongolian\", \"words\": \"\", \"verdict\": \"disputed\",\n \"derivation\": \"An empty pass-through box asserting Mongol transmission of the Chinese word into Persian. The idea is superficially attractive — the Ilkhanid period is exactly when the Chinese loans Laufer discusses on these same pages (p'ai-tse 'passport', jinksānak, xutu 'walrus ivory', §§26-31) entered Persian — but no source supports it and two things tell against it. First, the cited page carries no Mongolian step at all: SIN 565-566 §29 goes straight from the Chinese compound to the Persian word, its Mongol material being §27 (Mongol court titles) and its Turkic material §28 (tuγ 'horse-tail standard'); Laufer's one Mongol/Persian grain word, bodso ~ boza, is a different item on a different page (SIN.txt line 3942). Second, Mo'in's footnote takes the word directly «از چینی shū», with no intermediary. Third and most damaging, the word's earliest attestation is the verse of Sūzanī of Samarqand (d. c. 1173), a generation before the Mongol conquest of Khwarazm — so Persian had شوشو before there were Mongols in Iran to bring it. Modern scholarship, in so far as it says anything, therefore prefers a direct Chinese (or unknown) source over a Mongol vector.\",\n \"derivation_fa\": \"این خانهٔ گذرگاهیِ بی‌واژه مدعی است که واژهٔ چینی از راه مغولی به فارسی رسیده است. اندیشه در نگاه نخست دلپذیر است — دورهٔ ایلخانی همان زمانی است که وام‌واژه‌های چینیِ موردبحث لاوفر در همین صفحات (پایزه، جینکسانک، خُتو) وارد فارسی شدند — اما هیچ منبعی آن را تأیید نمی‌کند و سه نکته بر ضد آن است. نخست، صفحهٔ یادشده اصلاً حلقهٔ مغولی ندارد: بند ۲۹ سینو-ایرانیکا یکراست از ترکیب چینی به واژهٔ فارسی می‌رود و مطالب مغولیِ لاوفر در بند ۲۷ (القاب دربار مغول) و ترکیِ او در بند ۲۸ (تُغ) است. دوم، حاشیهٔ معین واژه را بی‌واسطه «از چینی shū» می‌داند. سوم و مهم‌تر از همه، کهن‌ترین گواهِ واژه بیتِ سوزنی سمرقندی (درگذشتهٔ حدود ۵۶۹ ق) است، یعنی یک نسل پیش از هجوم مغول؛ پس «شوشو» پیش از آنکه مغولی در ایران باشد در فارسی به کار می‌رفته. نتیجه: پژوهش امروزی این حلقه را نمی‌پذیرد و منشأ مستقیم چینی (یا نامعلوم) را ترجیح می‌دهد.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SIN:565\", \"status\": \"not_found\",\n    \"note\": \"Read leaves 393-394 of refs/SIN.txt (= printed pp. 565-566) in full: §29, the millet paragraph, contains no Mongolian word, form or intermediary. The Mongol content on the page is §27, on titles (wan, t'ai wan, jinksānak); the only Mongol grain word in the book, 'Mongol bodso … connected by Kovalevski … with Persian boza' (SIN.txt line 3942), is elsewhere and is a different word.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol. 3 p. 1309, Mo'in's footnote 4\", \"stance\": \"contradicts\",\n    \"note\": \"«از چینی shU (ارزن)» — Mo'in derives the Persian word straight from Chinese, with no Mongolian stage, while citing the same Laufer page.\"},\n   {\"src\": \"SIN\", \"where\": \"pp. 565-566\", \"stance\": \"partial\",\n    \"note\": \"Discusses the word but supplies no Mongolian link; see ref_check.\"},\n   {\"src\": \"TTS\", \"where\": \"grep 'Hirse' in incoming/TTS/TTS_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"Vámbéry's Turco-Tatar etymological dictionary yields no millet word of this shape.\"},\n   {\"src\": \"LKT\", \"where\": \"grep 'Hirse' in LKT.txt\", \"stance\": \"silent\",\n    \"note\": \"Nothing comparable.\"}\n ]\n})\n\ne4[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"šošo, šŭšŭ\", \"verdict\": \"plausible\",\n \"derivation\": \"The Persian word is genuine and well attested. Borhan-e Qāṭeʿ p.1309 has the headword with its vocalisation and gloss: «شوشو ـ بضم هر دو شین و سکون هر دو واو، بمعنی گاورس و ارزن باشد» ('with ḍamma on both šīns and sukūn on both wāws, meaning gāvars and arzan', i.e. Setaria/Panicum millet) — which is precisely Nourai's double reading šošo / šūšū — and quotes as shāhed, via the Farhang-e Rašidi, the verse of Sūzanī of Samarqand printed in the box: «خری که آبخورش زیر ناودان عصیر ـ علف عصارهٔ بَگنی وَبَخسُم وشوشو». Richardson's Persian-Arabic-English dictionary (1829) independently lists «شوشو shushu, Millet» (RCH.txt line 53424). Nourai's own note in the box is right: bagnī and baxsom in that line are grain-liquors/must, so the donkey's fodder and drink are all by-products of grain. The origin from Chinese 黍 shǔ is Mo'in's (following Laufer's suggestion) and is phonetically easy for the first syllable, but the reduplication šu-šu is unexplained on the Chinese side, and Laufer expressly left the case open — hence 'plausible' rather than 'confirmed'.\",\n \"derivation_fa\": \"واژهٔ فارسی اصیل و خوش‌گواه است. برهان قاطع در ص ۱۳۰۹ سرواژه را با ضبط و معنی می‌آورد: «شوشو ـ بضم هر دو شین و سکون هر دو واو، بمعنی گاورس و ارزن باشد» — همان دو خوانشِ šošo / šūšū که نورایی داده — و به نقل از فرهنگ رشیدی بیت سوزنی سمرقندی را شاهد می‌گیرد: «خری که آبخورش زیر ناودان عصیر ـ علف عصارهٔ بَگنی وَبَخسُم وشوشو». ریچاردسون نیز در فرهنگ فارسی-عربی-انگلیسی خود (۱۸۲۹ م) مستقلاً «شوشو shushu, Millet» را ثبت کرده است. یادداشت خودِ نورایی هم درست است: «بگنی» و «بخسم» در آن بیت شراب و شیرهٔ دانه‌اند، پس خوراک و آبخورد خر هر دو پس‌ماندهٔ غله است. اما گرفتن آن از 黍 (shǔ) چینی رأی معین (به پیروی از پیشنهاد لاوفر) است و اگرچه هجای نخست آسان می‌نشیند، دوگان‌سازیِ šu-šu در سوی چینی توضیح‌ناپذیر مانده و لاوفر خود پرونده را باز گذاشته است؛ از این رو «با احتیاط پذیرفتنی».\",\n \"sources\": [V_SHOSHO],\n \"ref_check\": [\n   {\"ref\": \"BQT:1309\", \"status\": \"supports\",\n    \"note\": \"Exact page: BQT vol. 3 pdf page 100 = printed 1309 (offset printed ≈ pdf + 1209 at the start of the volume), incoming/BQT/BQT_v3_pages.txt lines 7633-7705. Headword «شوشو … بمعنی گاورس و ارزن باشد ۴», footnote «۴ از چینی shU (ارزن) . ره : Laufer , Sino - Iranica, p . 565», and on the same page the Sūzanī verse «علف عصارة بگنی‌وبخسم وشوشو . سوزنی سمرقندی. «رشیدی»» — headword, gloss, etymology and shāhed all as Nourai gives them.\"},\n   {\"ref\": \"MON:2089\", \"status\": \"not_found\",\n    \"note\": \"No شوشو in Mo'in's Farhang: vajehyab returns «شوشو» پیدا نشد! and greps of MON_part1.txt, MON_part2.txt and the Adena two-volume djvu find no occurrence. The Borhan footnote (BQT:1309), which is also Mo'in's, carries the claim instead.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol. 3 p. 1309\", \"stance\": \"supports\",\n    \"note\": \"See ref_check — headword, vocalisation, gloss «گاورس و ارزن», Chinese etymology and the Sūzanī shāhed.\"},\n   {\"src\": \"RCH\", \"where\": \"Richardson-Johnson 1829, s.v. (RCH.txt line 53424)\", \"stance\": \"supports\",\n    \"note\": \"«p شوشو shushu, Millet.» — an independent 19th-c. attestation of the word and its meaning, marked 'p' (Persian).\"},\n   {\"src\": \"SIN\", \"where\": \"pp. 565-566\", \"stance\": \"partial\",\n    \"note\": \"Laufer has the Persian word in the sense 'millet' but declines to pronounce on its origin.\"},\n   {\"src\": \"MON\", \"where\": \"vajehyab and local OCR\", \"stance\": \"silent\", \"note\": \"No entry (see ref_check MON:2089).\"},\n   {\"src\": \"FRS\", \"where\": \"grep 'شوشو' in FRS_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"Asadi's Loghat-e Fors does not have the word, though it is the kind of eastern-Persian rarity he collects.\"}\n ]\n})\n\ndoc[\"entries\"].append(e4)\njson.dump(doc, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part1.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(doc[\"entries\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk105.py",
 "description": "Build entries 3 and 4"
}
```


### [2026-09-05T17:24:58.610Z] TOOL RESULT

```
ok 2
```


## [2026-09-05T17:30:10.929Z] TOOL CALL #67: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk105b.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_CHERAGH = \"https://en.wiktionary.org/wiki/%DA%86%D8%B1%D8%A7%D8%BA\"\nW_SIRAJ   = \"https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%A7%D8%AC\"\nW_SHARQ   = \"https://en.wiktionary.org/wiki/%D8%B4%D8%B1%D9%82\"\nE_SARACEN = \"https://www.etymonline.com/word/Saracen\"\n\ndoc = json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part1.json'))\n\nPLA157 = (\"Asbaghi, Persische Lehnwoerter im Arabischen p.157 (running head '157' on that leaf of \"\n          \"incoming/PLA/PLA_pages.txt, printed = leaf − 15), s.v. siraj: \\\"siräg: 'Laterne, Lampe, Leuchter; \"\n          \"Sonne' aus pers. čirāγ, mp. čirāγ, aram., syr. šrāgā, mand. šraga. … das Wort sirāǧ tritt mehrmals \"\n          \"im Qur'ān auf, Fraenkel zufolge ist das Wort aus pers. čirāγ entlehnt worden. Die aram. syr. Form \"\n          \"heißt šrāgā. Vielleicht stammt auch das Wort šarq 'Orient' vom čirāγ.\\\"\")\n\ne5 = {\n \"entry\": 5,\n \"root\": \"Cîrâğ\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Middle Persian / Parthian čirāγ 'lamp' (Book Pahlavi <cylʾg>, Manichaean Parthian 𐫝𐫡𐫀𐫃 crʾg)\",\n \"note\": \"The root box is right in language, form and gloss. MacKenzie's Concise Pahlavi Dictionary has \\\"čirāγ [cylʾg | P crʾg, N چراغ] lamp\\\" (PHD_mackenzie.txt line 1798; English-Pahlavi index, 'lamp čirāγ', line 6956), and Asbaghi p.157 starts her sirāj article from 'pers. čirāγ, mp. čirāγ'. Mo'in says the same in Borhan-e Qāṭeʿ: «شکل پهلوی آن čirāγ است». One nuance modern work adds: Wiktionary treats New Persian چراغ as a borrowing from Parthian črʾg rather than the inherited Middle Persian form (Middle Persian is separately attested as <clʾγ>, crʾh), and flags the further Iranian etymology — a possible link with Proto-Indo-Iranian *čitrás 'bright, shining' — as unsettled. That does not affect any arrow on this page; the box is a real word of the right period and meaning, and everything below it hangs together.\",\n \"note_fa\": \"خانهٔ ریشه از نظر زبان، صورت و معنی درست است. مکنزی در «فرهنگ کوچک پهلوی» می‌آورد: čirāγ [cylʾg | P crʾg, N چراغ] «چراغ»، و اصبغی در ص ۱۵۷ مقالهٔ سراج را از «pers. čirāγ, mp. čirāγ» آغاز می‌کند. معین نیز در حاشیهٔ برهان قاطع می‌نویسد «شکل پهلوی آن čirāγ است». یک نکتهٔ باریک که پژوهش امروزی می‌افزاید: ویکی‌واژه «چراغ» فارسی نو را وام‌واژه‌ای از پارتیِ črʾg می‌داند نه دنبالهٔ مستقیم صورت فارسی میانه (که خود جداگانه به شکل <clʾγ> و crʾh گواهی شده)، و ریشه‌شناسی دورترِ آن — پیوند احتمالی با هندوایرانیِ آغازین *čitrás «روشن، درخشان» — را ناروشن می‌شمارد. این نکته هیچ‌یک از پیکان‌های این صفحه را دگرگون نمی‌کند. نتیجه: ادعای نورایی دربارهٔ ریشه درست است.\",\n \"sources\": [W_CHERAGH],\n \"ref_check\": [\n   {\"ref\": \"PLA:157\", \"status\": \"supports\",\n    \"note\": PLA157 + \" — the head of Asbaghi's chain is exactly Nourai's root box: Pahlavi/Persian čirāγ.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"s.v. čirāγ (PHD_mackenzie.txt line 1798; PHD.txt line 300; English index line 6956)\", \"stance\": \"supports\",\n    \"note\": \"\\\"čirāγ [cylʾg | P crʾg, N چراغ] lamp\\\" — MacKenzie gives the Book Pahlavi spelling, the Parthian by-form and the New Persian continuation in one line.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 2, s.v. چراغ, Mo'in's footnote 9 (BQT_v2_pages.txt leaf 84 ≈ printed p. 627, lines 4834-4838)\", \"stance\": \"supports\",\n    \"note\": \"«شکل پهلوی آن čirāγ است» — Mo'in names the same Pahlavi form as the root box.\"},\n   {\"src\": \"NYB\", \"where\": \"grep 'čirā|clʾγ|Lampe' in NYB_vol2_glossary.txt\", \"stance\": \"silent\",\n    \"note\": \"Nyberg's glossary is keyed to the texts he edits; the word does not occur in them.\"},\n   {\"src\": \"HRN\", \"where\": \"grep 'čirāġ|cirag|Lampe|چراغ' in HRN.txt\", \"stance\": \"silent\",\n    \"note\": \"Horn's Grundriss has no article on چراغ (his selection is inherited vocabulary with Avestan/Old Persian anchors).\"},\n   {\"src\": \"HUB\", \"where\": \"grep 'čirāġ|cirag|چراغ' in HUB.txt\", \"stance\": \"silent\",\n    \"note\": \"Hübschmann's Persische Studien likewise has nothing.\"},\n   {\"src\": \"SOD\", \"where\": \"grep 'čarāγ|crʾʾγ' in SOD.txt\", \"stance\": \"silent\",\n    \"note\": \"Gharib's Sogdian dictionary yields no hit in this OCR, though Wiktionary cites a Sogdian crʾʾγ /čarāγ/ as a cognate.\"}\n ],\n \"nodes\": []\n}\n\nN = e5[\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"čerâğ\", \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian چراغ čerāγ continues Middle Persian / Parthian čirāγ directly and without complication: the short i of the first syllable is lowered to e as regularly in New Persian (MP dil > del, MP pistag > peste), and the final Iranian -γ is kept both in writing (غ) and, classically, in pronunciation; classical Persian still shows both čirāġ and čarāġ (Wiktionary). MacKenzie's entry itself ends '… N چراغ'. The point at which this box matters for the rest of the chart is the direction of borrowing, and Mo'in states it explicitly in his footnote 9 to the Borhan entry: «کلمهٔ فارسی است که در آرامی و سریانی و نیز عربی (سراج) وارد شده (قرآن، سورهٔ نور) … ادی‌شیر (۹۸) میخواهد کلمهٔ فارسی چراغ را از سریانی مأخوذ بداند ولی این امر مشکل است» — the Persian word went out into Aramaic, Syriac and Arabic, and Addi Shir's attempt to reverse the arrow is rejected. The gloss chain 'lamp > light > illumination > guiding light' is ordinary Persian usage, and the Hāfez bayt in the box («…چراغی برکند خلوت‌نشینی») plays on exactly that extension.\",\n \"derivation_fa\": \"«چراغ» فارسی نو دنبالهٔ بی‌واسطهٔ čirāγ فارسی میانه/پارتی است: «i» کوتاهِ هجای نخست، چنان‌که قاعدهٔ فارسی نو است، به «e» فروکاسته شده (مانند dil > دل، pistag > پسته) و «غ» پایانیِ ایرانی هم در نوشتار و هم در تلفظ کلاسیک برجای مانده است؛ در فارسی دری هنوز هر دو گونهٔ čirāġ و čarāġ ثبت است. مکنزی خود مدخل پهلوی را با «N چراغ» می‌بندد. آنچه این خانه را برای بقیهٔ نمودار مهم می‌کند سویِ وام‌گیری است، و معین در حاشیهٔ ۹ برهان قاطع صریح می‌گوید: «کلمهٔ فارسی است که در آرامی و سریانی و نیز عربی (سراج) وارد شده (قرآن، سورهٔ نور) … ادی‌شیر (۹۸) میخواهد کلمهٔ فارسی چراغ را از سریانی مأخوذ بداند ولی این امر مشکل است» — یعنی واژه از فارسی بیرون رفته و کوشش ادی‌شیر برای وارونه‌کردن پیکان رد شده است. گسترش معنایی «چراغ ← روشنایی ← اشراق ← چراغ راه» نیز کاربرد عادی فارسی است و بیت حافظِ درون خانه بر همان بازی می‌کند. نتیجه: ادعای نورایی درست است.\",\n \"sources\": [W_CHERAGH],\n \"ref_check\": [\n   {\"ref\": \"BQT:626\", \"status\": \"supports\",\n    \"note\": \"Found at BQT_v2_pages.txt leaf 84 (printed ≈ 627 on the leaf+543 offset, i.e. Nourai's 626 within the ±3 drift of that volume): headword «چراغ ـ بروزن فراغ؛ فتیله‌ای باشد که آنرا با چربی و روغن و امثال آن روشن کرده باشند», footnote 9 «کلمهٔ فارسی است که در آرامی و سریانی و نیز عربی (سراج) وارد شده (قرآن، سورهٔ نور)… ادی‌شیر (۹۸) میخواهد کلمهٔ فارسی چراغ را از سریانی مأخوذبداند ولی این امر مشکل است… «جفری ۱۹۹-۱۷۱» شکل پهلوی آن čirāγ است.» Exactly the derivation the arrow draws.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"s.v. čirāγ\", \"stance\": \"supports\",\n    \"note\": \"\\\"čirāγ [cylʾg | P crʾg, N چراغ] lamp\\\" — MacKenzie equates the Pahlavi word with New Persian چراغ himself.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 2 p. 626/627, Mo'in's footnote 9\", \"stance\": \"supports\",\n    \"note\": \"See ref_check; note in particular that Mo'in rejects Addi Shir's Syriac-to-Persian direction.\"},\n   {\"src\": \"HRN\", \"where\": \"grep 'چراغ|čirāġ' in HRN.txt\", \"stance\": \"silent\", \"note\": \"No article.\"},\n   {\"src\": \"HUB\", \"where\": \"grep 'چراغ|čirāġ' in HUB.txt\", \"stance\": \"silent\", \"note\": \"No article.\"}\n ]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Arabic\", \"words\": \"ešrâğ; šarq\", \"verdict\": \"disputed\",\n \"derivation\": \"Both words exist, but neither comes from Persian čirāγ. Arabic شَرْق šarq 'east, sunrise' and إشراق ʾišrāq 'radiance, illumination' (the form-IV verbal noun of أشرق ʾašraqa 'to rise, shine') sit on the native Semitic root š-r-q, with a full triliteral paradigm — šaraqa, ʾašraqa, šāriq, mašriq, mustašriq — and Semitic cognates: Wiktionary compares Hebrew זָרַח zāraḥ 'to shine, rise' and מִזְרָח mizrāḥ 'east', and Klein, s.v. Saracen, derives sharq 'east' from sharaqa 'he cleft, dissected; rose (said of the sun)'. A borrowed noun cannot generate that verbal system. The derivation is also phonetically impossible: the real Arabic reflex of Persian čirāγ is سراج sirāj — Iranian č appears as Arabic s (via Aramaic š), and Iranian -γ as ج — which is exactly what Siddiqi §9 sets out and what node #10 shows; a second reflex with š- and a root-final qāf is not a possible outcome. What Nourai reports is nevertheless a fair report of his source: Asbaghi does print the guess, twice, but hedged both times — p.157 'Vielleicht stammt auch das Wort šarq \\\"Orient\\\" vom čirāγ', and p.21 s.v. ʾišrāq \\\"'erleuchten', eventuell aus dem pers. čirāγ, s. sirāǧ\\\". The box's own note ('PLA suggests this as a possible derivation but is not certain') is therefore accurate, and modern scholarship comes down against the suggestion: it is a semantic attraction ('lamp/light' ~ 'sunrise/illumination'), i.e. folk etymology.\",\n \"derivation_fa\": \"هر دو واژه در عربی هست، اما هیچ‌کدام از «چراغ» فارسی نیامده است. «شَرْق» (خاور، برآمدن آفتاب) و «إشراق» (تابش، مصدر باب افعال از أشرق) بر ریشهٔ سامیِ اصیل ش‌ر‌ق نشسته‌اند و دستگاه کاملی از مشتقات سه‌حرفی دارند — شَرَقَ، أشرق، شارق، مشرق، مستشرق — و هم‌ریشه‌های سامی نیز دارند: ویکی‌واژه عبریِ זָרַח (زاراح، «درخشیدن، برآمدن») و מִזְרָח (میزراح، «خاور») را می‌سنجد و کلاین ذیل Saracen، sharq را از sharaqa «برآمدن خورشید» می‌گیرد. اسمی وام‌گرفته چنین دستگاه فعلی‌ای نمی‌زاید. از نظر آوایی نیز ناممکن است: بازتاب واقعی «چراغ» فارسی در عربی «سراج» است — «چ» ایرانی از راه «ش» آرامی به «س» عربی و «غ» به «ج» — همان که صدیقی در بند ۹ نشان داده و گرهٔ ۱۰ همین نمودار گواه آن است؛ بازتاب دومی با «ش» و «ق» پایانی شدنی نیست. با این همه، گزارش نورایی از منبعش امانت‌دارانه است: اصبغی این حدس را دو بار، هر بار با احتیاط، آورده است («Vielleicht…» در ص ۱۵۷ و «eventuell aus dem pers. čirāγ» در ص ۲۱). پس یادداشت خودِ خانه درست است و پژوهش امروزی این پیشنهاد را رد می‌کند و آن را ریشه‌شناسی عامیانه‌ای برخاسته از کشش معنایی («چراغ/روشنایی» ~ «طلوع/اشراق») می‌شمارد.\",\n \"sources\": [W_SHARQ, E_SARACEN],\n \"ref_check\": [\n   {\"ref\": \"PLA:157\", \"status\": \"partial\",\n    \"note\": PLA157 + \" — the last line of the article is Nourai's source, but Asbaghi writes 'Vielleicht' (perhaps) and repeats it as 'eventuell' at p.21 s.v. ʾišrāq (PLA_pages.txt line 1558: \\\"'idräg [= ʾišrāq]: 'erleuchten', eventuell aus dem pers. čirāg s. siräß\\\"). The reference does say it, but only as a hedged guess, not as the flat derivation the arrow draws.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1383 s.v. Saracen\", \"stance\": \"contradicts\",\n    \"note\": \"\\\"fr. Arab. sharqiyin, pl. acc. of sharqiy, 'Eastern', fr. sharq, 'east', fr. sharaqa, 'he cleft, dissected; rose (said of the sun)'\\\" — Klein derives šarq inside Arabic, from a native verb.\"},\n   {\"src\": \"PLA\", \"where\": \"pp. 21 and 157\", \"stance\": \"partial\", \"note\": \"See ref_check: the guess is there, twice, hedged both times.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, The Foreign Vocabulary of the Qur'an, pp. 166-167 and index\", \"stance\": \"silent\",\n    \"note\": \"Jeffery treats سراج as a foreign word of the Qur'an but has no article on شرق / إشراق — he did not regard them as loans, though شرق and its derivatives are common in the Qur'an.\"},\n   {\"src\": \"AFM\", \"where\": \"grep 'شرق|اشراق' in AFM_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"Addi Shir's list of Persian words arabised has no شرق/إشراق entry (his چراغ material, reported by Mo'in at Borhan p.626 fn. 9, concerns سراج only).\"}\n ]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"ešrâğ; šarq\", \"verdict\": \"plausible\",\n \"derivation\": \"The arrow itself — Arabic into Persian — is correct and unremarkable: اشراق ešrāq and شرق šarq are ordinary Arabic loans in Persian, taken over ready-made with the whole family the box lists in its extra line, شارق (active participle I, 'the rising sun'), استشراق estešrāq (form-X verbal noun, the modern coinage 'Orientalism'), مشرق mašreq (noun of place, 'place of sunrise, the East') and مستشرق mostašreq ('Orientalist'). Mo'in tags the headword «اشراق: [ع.] (مصدر لازم) تافتن، تابیدن» — Arabic — and gives «حکمت اشراق» its own entry, the Illuminationist philosophy of Suhrawardī (d. 1191), which is where ešrāq acquired in Persian the second sense Nourai glosses, 'intuition'. The Hāfez bayt in the box uses مشرق («چو آفتاب می از مشرق پیاله برآید»). What is wrong is not this arrow but the box above it: since Arabic šarq/ʾišrāq are not from Persian čirāγ (node #2), the Persian → Arabic → Persian round trip the chart draws here does not exist; these are simply Arabic words borrowed into Persian, not Persian words come home. Hence 'plausible': the immediate step is right, the chain behind it is not.\",\n \"derivation_fa\": \"خودِ پیکان — از عربی به فارسی — درست و بی‌مسئله است: «اشراق» و «شرق» وام‌واژه‌های عادی عربی در فارسی‌اند و همراه با همان خانوادهٔ آماده‌ای که خانهٔ نمودار در سطر افزوده‌اش برشمرده وارد شده‌اند: «شارق» (اسم فاعل باب اول)، «استشراق» (مصدر باب استفعال، ساختِ نوِ «خاورشناسی»)، «مشرق» (اسم مکان) و «مستشرق» («خاورشناس»). معین سرواژه را «اشراق: [ع.] (مص‌ل.) تافتن، تابیدن» برچسب می‌زند و «حکمت اشراق» را مدخلی جداگانه می‌دهد؛ همان فلسفهٔ سهروردی (مقتول ۵۸۷ ق) است که «اشراق» در فارسی معنی دومِ موردنظر نورایی، یعنی «شهود»، را از آن گرفته است. بیت حافظِ درون خانه نیز «مشرق» را به کار برده است. آنچه نادرست است این پیکان نیست، بلکه خانهٔ بالای آن است: چون «شرق/إشراق» عربی از «چراغ» فارسی نیامده (گرهٔ ۲)، آن رفت‌وبرگشتِ فارسی › عربی › فارسی که نمودار در اینجا می‌کشد وجود ندارد؛ اینها فقط واژه‌های عربیِ وام‌گرفته در فارسی‌اند، نه واژه‌های فارسیِ بازگشته. نتیجه: حلقهٔ نزدیک درست است، زنجیرهٔ پشتِ آن نه.\",\n \"sources\": [W_SHARQ],\n \"ref_check\": [\n   {\"ref\": \"FVA:211\", \"status\": \"not_checked\",\n    \"note\": \"S.M. Nahvi, Farhang-e Vāžehā-ye Arabi dar Fārsi (1368/1989): refs_online.json records kind='catalog' — an OpenLibrary record only, no scan on archive.org, ketabnak, noorlib or the open web. Nothing of this citation could be tested.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. اشراق and حکمت اشراق (MON_part1.txt lines 13363, 13366); s.v. مستشرق (MON_part2.txt line 56159)\", \"stance\": \"supports\",\n    \"note\": \"«اشراق: [ع.] (مص‌ل.) تافتن، تابیدن»; «حکمت اشراق: فلسفه‌ای که در اسلام مروج …» — Mo'in marks the words as Arabic loans in Persian, which is what this arrow claims, and registers the derivatives Nourai lists.\"},\n   {\"src\": \"BQT\", \"where\": \"grep 'اشراق' in BQT_v1_pages.txt (line 26969 and Mo'in's cross-references)\", \"stance\": \"partial\",\n    \"note\": \"Borhan's material on اشراق is Mo'in's own note referring to his «حکمت اشراق تألیف نگارنده ص ۱۰» — the Illuminationist term, treated as Arabic; nothing on any Iranian origin.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1383 s.v. Saracen\", \"stance\": \"contradicts\",\n    \"note\": \"Relevant here only for the upstream link: Klein's sharq < sharaqa makes these Persian loans Arabic in origin, not repatriated Persian.\"}\n ]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"Arabic\", \"words\": \"šarqîyîn\", \"verdict\": \"confirmed\",\n \"derivation\": \"The form is exactly right: شرقيين šarqiyyīn is the genitive/accusative plural of the nisba adjective شرقي šarqiyy 'eastern', regularly derived from شرق šarq 'east' with the relative suffix -iyy and the sound masculine plural -īn (oblique) beside -ūn (nominative). Klein p.1383, the analysis behind Nourai's whole Saracen branch, has it word for word: \\\"fr. Arab. sharqiyin, pl. acc. of sharqiy, 'Eastern', fr. sharq, 'east'\\\", and the gloss 'easterners' is what the substantivised nisba means. The word and the arrow Arabic šarq → Arabic šarqiyyīn are therefore confirmed; whether this Arabic form is in turn the source of the Greek ethnonym is a separate and much weaker claim, treated at node #5.\",\n \"derivation_fa\": \"صورت دقیقاً درست است: «شرقیین» حالت جرّی/نصبیِ جمعِ مذکر سالمِ صفت نسبیِ «شرقی» است که به قاعده از «شرق» با پسوند نسبت ـیّ و جمعِ ـین (در برابر ـون در حالت رفعی) ساخته می‌شود. کلاین در ص ۱۳۸۳ — همان تحلیلی که کل شاخهٔ Saracen نورایی بر آن استوار است — عیناً می‌نویسد: «از عربی sharqiyin، جمعِ منصوبِ sharqiy «خاوری»، از sharq «خاور»»، و معنیِ «خاوریان» همان کاربرد اسمی‌شدهٔ صفت نسبی است. پس واژه و پیکانِ «شرق ← شرقیین» در درون عربی درست است؛ اما اینکه همین صورت عربی سرچشمهٔ نام قومیِ یونانی باشد ادعایی جداگانه و بسیار سست‌تر است که در گرهٔ ۵ بررسی شده. نتیجه: ادعای نورایی دربارهٔ خودِ این صورت درست است.\",\n \"sources\": [E_SARACEN, W_SHARQ],\n \"ref_check\": [\n   {\"ref\": \"AHD:1152\", \"status\": \"not_checked\",\n    \"note\": \"AHD:1152 is a page of the New College main word-list (the Saracen entry), not of the Indo-European appendix; only Watkins' 1985 IE-roots volume is on disk, and the New College scans on archive.org are lending-only. A plain fetch of ahdictionary.com/word/search.html?q=Saracen returns only the site's boilerplate, no entry text. The parallel citation KLN:1383 was checked instead and gives the same analysis AHD is being cited for.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1383 s.v. Saracen (KLN_1966.txt line 33732; page marker '1382' at line 33701)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Saracen, n., 1) an Arab; 2) a Moslem. — ML. Saraceni (pl.), fr. Late Gk. Σαρακηνοί (pl.), fr. Arab. sharqiyin, pl. acc. of sharqiy, 'Eastern', fr. sharq, 'east', fr. sharaqa …\\\" — form, case, number and gloss as in the box.\"},\n   {\"src\": \"FVQ\", \"where\": \"grep in FVQ_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"Jeffery has no article on شرقي; not a Qur'anic loanword question.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. sarcenet (SKT.txt line 16488)\", \"stance\": \"silent\",\n    \"note\": \"Skeat's Concise reaches the family only through sarcenet 'a thin silk … made by the Saracens — Low L. sarcenetum — L. Saracenus' and gives no Arabic form.\"}\n ]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"Greek\", \"words\": \"Sarakěnos\", \"verdict\": \"disputed\",\n \"derivation\": \"The Greek word is real — Σαρακηνός, pl. Σαρακηνοί, with long ē (η); the breve the book prints on 'Sarakěnos' is Nourai's transliteration habit, not a claim about quantity — but the arrow into it from Arabic šarqiyyīn is the weak link of the whole branch. Σαρακηνοί is already in Ptolemy's Geography (c. 150 CE) as the name of a people of north-western Arabia and the Sinai, and recurs in Stephanus of Byzantium and in the fourth-century Latin of Ammianus Marcellinus; that is four to five centuries before Greek was in a position to take ethnonyms from Arabic, and it is the standing objection to the šarqiyyīn etymology. Etymonline states it plainly: \\\"from Greek sarakenos. This usually is said to be from Arabic sharquiyin, accusative plural of sharqiy 'eastern', from sharq 'east, sunrise', but this is not certain\\\", adding that \\\"in medieval times the name was associated with that of Biblical Sarah\\\" — i.e. the ancients themselves were guessing. Klein and the 1975 AHD, Nourai's two references here, print the Arabic derivation without a caveat, which is why the chart has it; modern handbooks treat it as unproven and probably a learned back-formation. Verdict: the Greek node is a real word, the derivation drawn into it is disputed.\",\n \"derivation_fa\": \"واژهٔ یونانی واقعی است — Σαρακηνός، جمعِ Σαρακηνοί، با «ē»ی بلند (η)؛ نشانهٔ کوتاهی که کتاب روی «Sarakěnos» گذاشته شیوهٔ آوانگاریِ خودِ نورایی است نه ادعایی دربارهٔ کمیّت واکه — اما پیکانی که از «شرقیین» عربی به آن کشیده شده سست‌ترین حلقهٔ این شاخه است. «Σαρακηνοί» پیش‌تر در «جغرافیا»ی بطلمیوس (حدود ۱۵۰ م) نام مردمی در شمال‌باختر عربستان و سینا است و در استفانوس بیزانسی و در لاتینِ آمیانوس مارکلینوس (سدهٔ ۴ م) نیز آمده؛ یعنی چهار تا پنج سده پیش از آنکه یونانی بتواند نام قومی از عربی وام گیرد، و همین ایراد اصلی بر ریشه‌شناسیِ «شرقیین» است. اتیمانلاین صریح می‌گوید: «از یونانیِ sarakenos. معمولاً آن را از عربیِ sharquiyin … می‌دانند، اما این قطعی نیست» و می‌افزاید که در سده‌های میانه نام را با «سارهٔ» تورات نیز پیوند می‌دادند — یعنی خودِ پیشینیان هم حدس می‌زدند. کلاین و AHD ۱۹۷۵ (دو مأخذ نورایی در همین‌جا) ریشهٔ عربی را بی‌هیچ قید می‌آورند و نمودار از آنها پیروی کرده است؛ کتاب‌های امروزی آن را اثبات‌نشده و به احتمال زیاد ساختی عالمانه و پسین می‌دانند. نتیجه: واژهٔ یونانی هست، ولی پژوهش امروزی این اشتقاق را نمی‌پذیرد.\",\n \"sources\": [E_SARACEN],\n \"ref_check\": [\n   {\"ref\": \"AHD:1152\", \"status\": \"not_checked\",\n    \"note\": \"New College main word-list page (s.v. Saracen), not the IE appendix; unavailable as explained at node #4. Klein p.1383, cited on the English node of the same chain, prints the identical derivation, so what AHD is being cited for is at least attested in the sister reference.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1383 s.v. Saracen\", \"stance\": \"supports\",\n    \"note\": \"\\\"ML. Saraceni (pl.), fr. Late Gk. Σαρακηνοί (pl.), fr. Arab. sharqiyin\\\" — Klein gives Nourai's chain without any reservation; he is a 1966 authority repeating the traditional account.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. sarcenet\", \"stance\": \"silent\",\n    \"note\": \"Skeat's Concise offers no etymology of the ethnonym itself.\"},\n   {\"src\": \"FSD\", \"where\": \"grep 'Saracen' in FSD_vol1-4\", \"stance\": \"silent\",\n    \"note\": \"The Funk & Wagnalls columns that would carry the entry are not recoverable from this OCR.\"},\n   {\"src\": \"WEB\", \"where\": \"grep 'Saracen' in WEB_vol1.txt\", \"stance\": \"silent\",\n    \"note\": \"Webster's hits are all incidental uses ('Saracenic arches', 'Children's Crusade', 'Saracen stone'), never the etymological entry.\"}\n ]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"Latin\", \"words\": \"Saracěnus\", \"verdict\": \"confirmed\",\n \"derivation\": \"Late Latin Saracēnus, pl. Saracēnī (again long ē, rendering Greek η), is the ordinary Latin transposition of the Greek ethnonym and is in use from the fourth century — Ammianus Marcellinus writes of the 'Saraceni' of the Syrian and Arabian steppe — passing thence into the Latin of the Church and of the chroniclers. Klein routes the English word through the medieval Latin plural: \\\"ML. Saraceni (pl.), fr. Late Gk. Σαρακηνοί (pl.)\\\"; Etymonline lists 'Medieval Latin Saracenus' beside Old French as the possible immediate source of the English word. The box is a straightforward and uncontroversial link.\",\n \"derivation_fa\": \"«Saracēnus» لاتینیِ متأخر (جمعِ Saracēnī، باز با «ē»ی بلند که برابر η یونانی است) برگردان عادی همان نام قومیِ یونانی است و از سدهٔ چهارم م به کار می‌رود — آمیانوس مارکلینوس از «Saraceni»های بادیهٔ شام و عربستان سخن می‌گوید — و از آنجا به لاتینِ کلیسا و تواریخ راه یافته است. کلاین واژهٔ انگلیسی را از جمعِ لاتینیِ سده‌های میانه می‌گیرد («ML. Saraceni، از یونانی متأخر Σαρακηνοί») و اتیمانلاین «Medieval Latin Saracenus» را در کنار فرانسهٔ کهن، سرچشمهٔ بی‌واسطهٔ واژهٔ انگلیسی می‌شمارد. این حلقه ساده و بی‌اختلاف است. نتیجه: ادعای نورایی درست است.\",\n \"sources\": [E_SARACEN],\n \"ref_check\": [\n   {\"ref\": \"AHD:1152\", \"status\": \"not_checked\",\n    \"note\": \"See node #4 — the New College main word-list page is not obtainable; the parallel KLN:1383 was checked and carries the Latin step.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1383 s.v. Saracen\", \"stance\": \"supports\",\n    \"note\": \"\\\"ML. Saraceni (pl.), fr. Late Gk. Σαρακηνοί (pl.)\\\" — the Greek→Latin step exactly as drawn.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. sarcenet (SKT.txt line 16488)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Low L. sarcenetum … — L. Saracenus, Saracen\\\" — Skeat has the Latin form.\"}\n ]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"Old French\", \"words\": \"Saracin\", \"verdict\": \"confirmed\",\n \"derivation\": \"Old French Saracin, more usually written Sarrazin / Sarrasin, from Latin Saracēnus: the Latin -c- before the front vowel is assibilated, the ending -ēnus reduced to -in, and the r doubled in the commonest spelling. Etymonline gives this as the route into English: 'from Old English (in translations from Latin), from Old French Saracin, Sarrasine or Medieval Latin Saracenus'. The Anglo-French diminutive of the same word, sarzinet, yields English sarcenet/sarsenet 'a fine silk' — Klein: 'Late ME. sarsenet, fr. AF. sarzinet, dimin. of ME. sarzin, Saracen' — which independently attests the French form in the right shape. Klein himself sends English straight to Medieval Latin, so the Old French box follows Etymonline/OED rather than KLN; that is the better account.\",\n \"derivation_fa\": \"«Saracin» فرانسهٔ کهن — که بیشتر Sarrazin/Sarrasin نوشته می‌شود — از «Saracēnus» لاتینی است: «c» لاتینی پیش از واکهٔ پیشین سایشی شده، پایانهٔ ـēnus به ـin فروکاسته و «ر» در املای رایج مشدد شده است. اتیمانلاین همین را راهِ ورود به انگلیسی می‌داند: «از انگلیسی کهن (در ترجمه‌ها از لاتین)، از فرانسهٔ کهن Saracin/Sarrasine یا لاتینیِ سده‌های میانه Saracenus». مصغّرِ آنگلونورمنِ همین واژه، sarzinet، واژهٔ انگلیسی sarcenet/sarsenet «پارچهٔ ابریشمی نازک» را داده است — کلاین: «انگلیسی میانهٔ متأخر sarsenet، از آنگلوفرانسهٔ sarzinet، مصغّر sarzin «ساراسن»» — و این خود گواهِ مستقلی بر صورت فرانسوی است. کلاین انگلیسی را یکراست از لاتینیِ میانه می‌گیرد، پس این خانه از اتیمانلاین/OED پیروی می‌کند که روایت بهتری است. نتیجه: ادعای نورایی درست است.\",\n \"sources\": [E_SARACEN],\n \"ref_check\": [\n   {\"ref\": \"AHD:1152\", \"status\": \"not_checked\", \"note\": \"See node #4; page unavailable.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1383 s.vv. Saracen, sarcenet\", \"stance\": \"partial\",\n    \"note\": \"Klein takes English Saracen from Medieval Latin without an Old French step, but his sarcenet article — \\\"Late ME. sarsenet, fr. AF. sarzinet, dimin. of ME. sarzin, 'Saracen'\\\" — presupposes exactly the French form this box posits.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. sarcenet\", \"stance\": \"supports\",\n    \"note\": \"\\\"OF. sarcenet, a stuff [made] by the Saracens — Low L. sarcenetum\\\" — the French shape of the word is Skeat's starting point too.\"}\n ]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"English\", \"words\": \"Saracen\", \"verdict\": \"confirmed\",\n \"derivation\": \"English Saracen goes back to Old English Sarasin, borrowed in translations from Latin, and appears in Middle English as Saracene, Sarcene, Sarazyn, Sarasine 'a Turk; an Arab; a Muslim' (Etymonline), adjectival from c. 1300. Nourai's gloss 'an Arab' is right for the original reference — the name was what Greeks and Romans gave to the nomads of the Syrian and Arabian deserts and to the inhabitants of Arabia Felix — though in Middle English it widened, under the Crusades, to 'Middle Eastern Muslim' and then to 'any non-Christian'. Klein p.1383, the second reference on the box, gives the two senses in that order: '1) an Arab; 2) a Moslem'. Derivatives: Saracenic; sarcenet 'fine silk'; sarsen (stone).\",\n \"derivation_fa\": \"«Saracen» انگلیسی به «Sarasin» انگلیسی کهن بازمی‌گردد که در ترجمه‌ها از لاتین وام گرفته شده، و در انگلیسی میانه به صورت‌های Saracene، Sarcene، Sarazyn، Sarasine به معنی «ترک؛ عرب؛ مسلمان» دیده می‌شود و از حدود ۱۳۰۰ م صفت نیز هست. معنیِ «یک عرب» که نورایی داده برای کاربرد نخستین درست است — یونانیان و رومیان این نام را به کوچ‌نشینان بادیهٔ شام و عربستان و به مردم «عربستان خوشبخت» می‌دادند — اگرچه در انگلیسی میانه و زیر تأثیر جنگ‌های صلیبی نخست به «مسلمان خاورمیانه‌ای» و سپس به «هر ناـمسیحی» گسترش یافت. کلاین در ص ۱۳۸۳، مأخذ دوم این خانه، همین دو معنی را به همین ترتیب می‌آورد: «۱) یک عرب؛ ۲) یک مسلمان». مشتقات: Saracenic؛ sarcenet «ابریشم نازک»؛ sarsen (سنگ). نتیجه: ادعای نورایی درست است.\",\n \"sources\": [E_SARACEN],\n \"ref_check\": [\n   {\"ref\": \"KLN:1383\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt line 33732 (page marker '1382' at line 33701, so the entry stands on p.1383): \\\"Saracen, n., 1) an Arab; 2) a Moslem. — ML. Saraceni (pl.), fr. Late Gk. Σαρακηνοί (pl.), fr. Arab. sharqiyin … Derivative: Saracen-ic, adj.\\\" — word, gloss and chain as in the box.\"},\n   {\"ref\": \"AHD:1152\", \"status\": \"not_checked\", \"note\": \"See node #4; the New College page is not obtainable and the AHD website returns no entry text to a plain fetch.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1383 s.v. Saracen\", \"stance\": \"supports\", \"note\": \"See ref_check.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. sarcenet\", \"stance\": \"partial\",\n    \"note\": \"Skeat's Concise has no Saracen headword, only the derived cloth-name, from which the ethnonym is reached: \\\"a stuff [made] by the Saracens … L. Saracenus, Saracen\\\".\"},\n   {\"src\": \"WEB\", \"where\": \"grep 'Saracen' in WEB_vol1.txt\", \"stance\": \"silent\",\n    \"note\": \"Only incidental uses of the word in other entries; no etymology.\"}\n ]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"Aramaic\", \"words\": \"\", \"verdict\": \"confirmed\",\n \"derivation\": \"An empty pass-through box, and the crucial one for this branch: the Iranian word reached Arabic through Aramaic, not directly. The Aramaic form is שְׁרָגָא šərāgā, Classical Syriac ܫܪܳܓܳܐ šrāḡā, Mandaic šraga, 'lamp'. Wiktionary derives it from Parthian *𐫢𐫡𐫀𐫄 *šrʾγ /širāγ/ and makes Arabic sirāj a borrowing from the Aramaic; Asbaghi p.157 sets out the same three-member chain, 'aus pers. čirāγ, mp. čirāγ, aram., syr. šrāgā, mand. šraga'; Siddiqi p.72 §9, in his section on how Persian č is rendered in Arabic, says outright that 'the word sirāj (= Pers. čirāγ) came through Aramaic (שרגא)'. The sound substitution is regular: Aramaic has no affricate č and replaces it with š, while Iranian -γ- is taken as g. Nourai's box is therefore right, and right to be a stage rather than a gloss.\",\n \"derivation_fa\": \"این خانهٔ گذرگاهیِ بی‌واژه، حلقهٔ کلیدیِ این شاخه است: واژهٔ ایرانی نه بی‌واسطه، بلکه از راه آرامی به عربی رسیده است. صورت آرامی שְׁרָגָא (šərāgā)، سریانی کلاسیک ܫܪܳܓܳܐ (šrāḡā) و مندایی šraga به معنی «چراغ» است. ویکی‌واژه آن را از پارتیِ *šrʾγ می‌گیرد و «سراج» عربی را وام‌گرفته از همین صورت آرامی می‌داند؛ اصبغی در ص ۱۵۷ همان زنجیرهٔ سه‌حلقه‌ای را می‌آورد: «از فارسیِ čirāγ، فارسی میانهٔ čirāγ، آرامی و سریانی šrāgā، مندایی šraga»؛ و صدیقی در ص ۷۲ بند ۹، در بخشِ چگونگیِ بازتاب «چ» فارسی در عربی، صریح می‌نویسد که «واژهٔ سراج (= فارسیِ چراغ) از راه آرامی آمده است (שרגא)». جانشینی آوایی قاعده‌مند است: آرامی واکهٔ سایشی-انسدادیِ «چ» ندارد و آن را «ش» می‌گذارد و «غ» ایرانی را «گ» می‌گیرد. نتیجه: این خانهٔ نورایی درست است و به‌جا مرحله‌ای مستقل شمرده شده.\",\n \"sources\": [W_SIRAJ, W_CHERAGH],\n \"ref_check\": [\n   {\"ref\": \"PLA:157\", \"status\": \"supports\",\n    \"note\": PLA157 + \" — the Aramaic/Syriac/Mandaic members stand between Persian and Arabic exactly as this box requires.\"}\n ],\n \"consulted\": [\n   {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 166-167, s.v. سراج (FVQ_pages.txt leaves 184-185, printed = leaf − 18)\", \"stance\": \"supports\",\n    \"note\": \"\\\"Fraenkel, Vocab, 7, pointed out that it was from Aram. שרגא = Syr. šrāgā. These forms are, however, borrowed from the Pers. چراغ\\\"; and p.167 \\\"Vollers, ZDMG, l, 613, is doubtless right in deriving the Arabic word from the Syriac.\\\" Jeffery expressly prefers the Aramaic/Syriac route over a direct Iranian borrowing.\"},\n   {\"src\": \"SDQ\", \"where\": \"Siddiqi p. 72 §9 (SDQ.txt leaf 88, after the running number '— 72 —')\", \"stance\": \"supports\",\n    \"note\": \"\\\"9. Persisches č wird durch س … zuweilen aber auch durch ج wiedergegeben … Das Wort سراج (= p. چراغ) ist über das Aramäische gekommen (שרגא).\\\"\"},\n   {\"src\": \"AFA\", \"where\": \"grep 'Lampe|sirag|šrāgā' in AFA.txt\", \"stance\": \"silent\",\n    \"note\": \"Fraenkel's Aramäische Fremdwörter is on disk but this Google scan's OCR of the relevant pages yields nothing searchable; his statement is available only at second hand through Jeffery, quoted above.\"}\n ]\n})\n\nN.append({\n \"id\": 10, \"lang\": \"Arabic\", \"words\": \"sîrâj\", \"verdict\": \"confirmed\",\n \"derivation\": \"Arabic سِرَاج sirāj 'lamp, luminary, lantern' (pl. سُرُج suruj) is a well-known Iranian loan, four times in the Qur'an — 25:61, 33:45, 71:16, 78:13, where the sun is وَجَعَلَ ٱلشَّمْسَ سِرَاجًا 'and He made the sun a lamp'. Jeffery pp.166-167: 'The Muslim authorities take it as pure Arabic, not realizing that the verb from which they derive it is denominative. Fraenkel, Vocab. 7, pointed out that it was from Aram. שרגא = Syr. šrāgā. These forms are, however, borrowed from the Pers. چراغ … Vollers, ZDMG l, 613, is doubtless right in deriving the Arabic word from the Syriac' — that is, Persian ultimately, Syriac immediately, which is exactly the two-step route the chart draws through node #9. Siddiqi p.72 §9 and Asbaghi p.157 say the same. The substitutions are the regular ones: Iranian č → Aramaic š → Arabic s (Arabic keeping š for its own root š-r-q, which is why sirāj and šarq cannot be the same word), Iranian -γ → g → Arabic ج j. Note that the Arabic denominative verb sarraja 'to light a lamp' is secondary, built on the loan — which is Jeffery's point against the native etymology.\",\n \"derivation_fa\": \"«سِراج» عربی به معنی «چراغ، روشنایی، فانوس» (جمع: سُرُج) وام‌واژه‌ای ایرانی و شناخته‌شده است و چهار بار در قرآن آمده — ۲۵:۶۱، ۳۳:۴۵، ۷۱:۱۶ و ۷۸:۱۳، آنجا که خورشید «وَجَعَلَ ٱلشَّمْسَ سِرَاجًا» خوانده شده. جفری در صص ۱۶۶–۱۶۷ می‌نویسد: «عالمان مسلمان آن را عربیِ سره می‌شمارند و درنمی‌یابند که فعلی که از آن مشتق می‌گیرند خودْ برساخته از اسم است. فرنکل نشان داد که واژه از آرامیِ שרגא = سریانیِ šrāgā است. اما این صورت‌ها خود از فارسیِ چراغ وام گرفته شده‌اند … و فولرس بی‌گمان حق دارد که واژهٔ عربی را از سریانی می‌گیرد» — یعنی سرچشمهٔ دور فارسی و سرچشمهٔ نزدیک سریانی، دقیقاً همان دو مرحله‌ای که نمودار با گرهٔ ۹ کشیده است. صدیقی (ص ۷۲ بند ۹) و اصبغی (ص ۱۵۷) نیز همین را می‌گویند. جانشینی‌ها قاعده‌مندند: «چ» ایرانی ← «ش» آرامی ← «س» عربی (عربی «ش» را برای ریشهٔ خودش ش‌ر‌ق نگاه می‌دارد، و همین است که «سراج» و «شرق» نمی‌توانند یک واژه باشند)، و «غ» ایرانی ← «گ» ← «ج» عربی. فعلِ «سَرَّجَ» عربی نیز ثانوی و برساخته از همین وام‌واژه است. نتیجه: ادعای نورایی درست است.\",\n \"sources\": [W_SIRAJ],\n \"ref_check\": [\n   {\"ref\": \"PLA:157\", \"status\": \"supports\", \"note\": PLA157},\n   {\"ref\": \"FVQ:166\", \"status\": \"supports\",\n    \"note\": \"Jeffery, Foreign Vocabulary of the Qur'an p.166 (FVQ_pages.txt leaf 184, whose running head reads '166'), s.v. سراج: \\\"xxv, 62; xxxiii, 45; lxxi, 15; lxxviii, 13. A lamp or torch. The Muslim authorities take it as pure Arabic, not realizing that the verb from which they derive it is denominative. Fraenkel, Vocab, 7, pointed out that it was from Aram. שרגא = Syr. šrāgā. These forms are, however, borrowed from the Pers. چراغ.\\\" Page and content match Nourai's citation exactly.\"},\n   {\"ref\": \"SDQ:72\", \"status\": \"supports\",\n    \"note\": \"Siddiqi, Studien über die persischen Fremdwörter im klassischen Arabisch p.72 (SDQ.txt leaf 88, immediately after the printed '— 72 —'), §9: \\\"Persisches č wird durch س, wie auch im Aramäischen, zuweilen aber auch durch ج wiedergegeben … Das Wort سراج (= p. چراغ) ist über das Aramäische gekommen (שרגא).\\\"\"}\n ],\n \"consulted\": [\n   {\"src\": \"FVQ\", \"where\": \"pp. 166-167\", \"stance\": \"supports\", \"note\": \"See ref_check; p.167 adds Vollers' preference for Syriac as the immediate donor.\"},\n   {\"src\": \"SDQ\", \"where\": \"p. 72 §9\", \"stance\": \"supports\", \"note\": \"See ref_check.\"},\n   {\"src\": \"PLA\", \"where\": \"p. 157 s.v. sirāj\", \"stance\": \"supports\", \"note\": \"See ref_check.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 2 p. 626/627, Mo'in's footnote 9 to چراغ\", \"stance\": \"supports\",\n    \"note\": \"«کلمهٔ فارسی است که در آرامی و سریانی و نیز عربی (سراج) وارد شده (قرآن، سورهٔ نور)» — Mo'in states the same outward route, and rejects Addi Shir's attempt (AFM p.98) to reverse it.\"},\n   {\"src\": \"AFM\", \"where\": \"grep 'سراج' in AFM_pages.txt (lines 1038, 2439)\", \"stance\": \"silent\",\n    \"note\": \"Addi Shir's السراج occurrences in this OCR are incidental (in other entries' glosses); his p.98 article, which Mo'in reports as deriving Persian چراغ from Syriac, could not be located in the scanned text.\"}\n ]\n})\n\nN.append({\n \"id\": 11, \"lang\": \"Persian\", \"words\": \"serâj\", \"verdict\": \"confirmed\",\n \"derivation\": \"The closing link of a textbook Persian → Aramaic → Arabic → Persian round trip: Persian سراج serāj 'lamp' is the Arabic sirāj re-borrowed into Persian, where it lives in the learned and Qur'anic register (سراج منیر, and the very common name and laqab سراج‌الدین, besides the takhalluṣ Serāj) alongside the inherited چراغ, which never left. Wiktionary makes the relation explicit under چراغ: 'Borrowed from Classical Persian چراغ (čirāġ, čarāġ), itself from Parthian crʾg … Doublet of سراج (sirâc, \"lamp\")' — a doublet is precisely what a round trip produces. The Arabic shape is kept unchanged in Persian (س for the original č, ج for the original γ), which is why the two members of the doublet are no longer recognisable as one word.\",\n \"derivation_fa\": \"این حلقهٔ پایانیِ یک رفت‌وبرگشتِ نمونه‌وارِ فارسی › آرامی › عربی › فارسی است: «سراج» فارسی همان «سِراج» عربی است که دوباره به فارسی وام داده شده و در لایهٔ فاضلانه و قرآنی به کار می‌رود (سراج منیر؛ نام و لقب پربسامد سراج‌الدین؛ تخلص «سراج»)، در کنار «چراغِ» موروثی که هرگز از فارسی نرفته بود. ویکی‌واژه این نسبت را ذیل «چراغ» صریح آورده است: «وام‌گرفته از فارسی کلاسیک چراغ (čirāġ/čarāġ)، خود از پارتیِ črʾg … دوگانهٔ سراج». دوگانه (doublet) درست همان چیزی است که چنین رفت‌وبرگشتی پدید می‌آورد. صورت عربی در فارسی دست‌نخورده مانده («س» به جای «چ» اصلی و «ج» به جای «غ» اصلی)، و به همین سبب است که دو عضو این دوگانه دیگر یک واژه به نظر نمی‌رسند. نتیجه: ادعای نورایی درست است.\",\n \"sources\": [W_CHERAGH, W_SIRAJ],\n \"ref_check\": [\n   {\"ref\": \"FVA:188\", \"status\": \"not_checked\",\n    \"note\": \"S.M. Nahvi, Farhang-e Vāžehā-ye Arabi dar Fārsi (1368/1989): no digital copy exists on any permitted platform (refs_online.json, kind='catalog'), so the citation could not be tested. The claim itself — that Persian سراج is the Arabic word — is uncontroversial and is confirmed by Wiktionary's 'Doublet of سراج' note under چراغ.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol. 2 p. 626/627, Mo'in's footnote 9\", \"stance\": \"supports\",\n    \"note\": \"«…و نیز عربی (سراج) وارد شده (قرآن، سورهٔ نور)» — Mo'in names the Arabic form as the outward-bound shape of the Persian word, which is what comes back in this box.\"},\n   {\"src\": \"PLA\", \"where\": \"p. 157 s.v. sirāj\", \"stance\": \"supports\",\n    \"note\": \"Asbaghi's whole article is written from the Persian side: 'sirāǧ … aus pers. čirāγ', so the Arabic word is by definition available for re-borrowing into Persian.\"},\n   {\"src\": \"FVQ\", \"where\": \"pp. 166-167\", \"stance\": \"supports\",\n    \"note\": \"Establishes سراج as the Arabic (Qur'anic) form of the word, the form Persian took back.\"}\n ]\n})\n\ndoc[\"entries\"].append(e5)\njson.dump(doc, open('/home/sfmqrb/git/rishe/data/verification/page-105.json','w'), ensure_ascii=False, indent=1)\nprint(\"written\", sum(len(e[\"nodes\"]) for e in doc[\"entries\"]), \"nodes\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk105b.py\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-105.json > /dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 105",
 "description": "Build entry 5, write file, run check"
}
```


### [2026-09-05T17:30:17.865Z] TOOL RESULT

```
  File "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk105b.py", line 242
    "derivation": "The closing link of a textbook Persian → Aramaic → Arabic → Persian round trip: Persian سراج serāj 'lamp' is the Arabic sirāj re-borrowed into Persian, where it lives in the learned and Qur'anic register (سراج منیر, and the very common name and laqab سراج‌الدین, besides the takhalluṣ Serāj) alongside the inherited چراغ, which never left. Wiktionary makes the relation explicit under چراغ: 'Borrowed from Classical Persian چراغ (čirāġ, čarāġ), itself from Parthian crʾg … Doublet of سراج (sirâc, "lamp")' — a doublet is precisely what a round trip produces. The Arabic shape is kept unchanged in Persian (س for the original č, ج for the original γ), which is why the two members of the doublet are no longer recognisable as one word.",
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
usage: python -m json.tool [-h] [--sort-keys] [--no-ensure-ascii]
                           [--json-lines]
                           [--indent INDENT | --tab | --no-indent | --compact]
                           [infile] [outfile]
python -m json.tool: error: argument infile: can't open '/home/sfmqrb/git/rishe/data/verification/page-105.json': [Errno 2] No such file or directory: '/home/sfmqrb/git/rishe/data/verification/page-105.json'
nodes verified: 0/17
node verdicts: {}
root verdicts: {}
ref checks: {}
books consulted: {} | by book: {}
pages without verification (1): 105
```


## [2026-09-05T17:30:25.442Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npython3 - <<'EOF'\np='mk105b.py'\ns=open(p,encoding='utf-8').read()\nbad='(sirâc, \"lamp\")'\ngood='(sirâc, «lamp»)'\nassert bad in s\ns=s.replace(bad,good)\nopen(p,'w',encoding='utf-8').write(s)\nprint('patched')\nEOF\npython3 mk105b.py\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-105.json > /dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 105",
 "description": "Fix quoting and rebuild"
}
```


### [2026-09-05T17:30:27.693Z] TOOL RESULT

```
patched
written 17 nodes
JSON OK
nodes verified: 17/17
node verdicts: {'plausible': 5, 'confirmed': 9, 'disputed': 3}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'partial': 2, 'not_checked': 11, 'not_found': 2, 'supports': 7}
books consulted: {'silent': 23, 'partial': 10, 'supports': 21, 'contradicts': 3} | by book: {'KLN': 8, 'SKT': 7, 'BQT': 6, 'FVQ': 5, 'MON': 4, 'WEB': 3, 'PLA': 3, 'LKT': 2, 'FSD': 2, 'SIN': 2, 'AFM': 2, 'SDQ': 2, 'DOZ': 1, 'PHN': 1, 'DEV': 1, 'ARY': 1, 'TTS': 1, 'RCH': 1, 'FRS': 1, 'PHD': 1, 'HRN': 1, 'HUB': 1, 'AFA': 1}
```


## [2026-09-05T17:30:46.291Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json\np='data/verification/page-105.json'\nd=json.load(open(p,encoding='utf-8'))\n\n# 1. entry 3 node 4: drop the stray AHD:1152 ref_check (not cited on that box)\ne3=[e for e in d['entries'] if e['entry']==3][0]\nn4=[n for n in e3['nodes'] if n['id']==4][0]\nbefore=len(n4['ref_check'])\nn4['ref_check']=[r for r in n4['ref_check'] if r['ref']!='AHD:1152']\nassert len(n4['ref_check'])==before-1\n\n# 2. fix FVQ leaf/page arithmetic wording\ndef fix(s):\n    return (s.replace(\"FVQ_pages.txt leaf 184, whose running head reads '166'\",\n                      \"FVQ_pages.txt leaf 184 counted 1-based over form-feeds, whose running head reads '166'\")\n             .replace(\"FVQ_pages.txt leaves 184-185, printed = leaf − 18\",\n                      \"FVQ_pages.txt leaves 184-185 counted 1-based over form-feeds; their running heads read '166' and '167'\"))\n\ndef walk(o):\n    if isinstance(o,dict):\n        return {k:(fix(v) if isinstance(v,str) else walk(v)) for k,v in o.items()}\n    if isinstance(o,list):\n        return [walk(x) for x in o]\n    return o\nd=walk(d)\njson.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)\nprint('patched')\nEOF\npython3 -m json.tool data/verification/page-105.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 105",
 "description": "Patch stray ref and leaf arithmetic"
}
```


### [2026-09-05T17:30:48.261Z] TOOL RESULT

```
patched
JSON OK
nodes verified: 17/17
node verdicts: {'plausible': 5, 'confirmed': 9, 'disputed': 3}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'partial': 2, 'not_checked': 10, 'not_found': 2, 'supports': 7}
books consulted: {'silent': 23, 'partial': 10, 'supports': 21, 'contradicts': 3} | by book: {'KLN': 8, 'SKT': 7, 'BQT': 6, 'FVQ': 5, 'MON': 4, 'WEB': 3, 'PLA': 3, 'LKT': 2, 'FSD': 2, 'SIN': 2, 'AFM': 2, 'SDQ': 2, 'DOZ': 1, 'PHN': 1, 'DEV': 1, 'ARY': 1, 'TTS': 1, 'RCH': 1, 'FRS': 1, 'PHD': 1, 'HRN': 1, 'HUB': 1, 'AFA': 1}
```


## [2026-09-05T17:30:52.856Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nhead -c 3 data/verification/page-105.json | xxd | head -1\nls -la data/verification/page-105.json data/verification/sources/refs/ocr/BOOK/105.png\ngit status --short | head -20",
 "description": "Final sanity checks"
}
```


### [2026-09-05T17:30:54.817Z] TOOL RESULT

```
00000000: 7b0a 20                                  {. 
-rw-rw-r-- 1 sfmqrb sfmqrb 83639 Sep  5 13:30 data/verification/page-105.json
-rw-rw-r-- 1 sfmqrb sfmqrb 82500 Sep  5 11:05 data/verification/sources/refs/ocr/BOOK/105.png
 M data/verification/sources/web/index.jsonl
?? data/verification/page-104.json
?? data/verification/page-105.json
?? data/verification/sources/web/651164bf608d9841.txt
?? data/verification/sources/web/b0d1e89d8f080549.txt
?? data/verification/sources/web/bcecc17eaa4b1885.txt
?? data/verification/sources/web/f8da4bf6b856d076.txt
?? data/verification/sources/web/ff55c7ac46891403.txt
```


## [2026-09-05T17:31:03.976Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in aab5e5692825f204 07fbd11449f9d7a8 b72cc012ea3476d4 d6418b07671b1447 05a271aafb1a0bff 0fa547e391100612 123cc88dc937f12a 2cbebb2fd375ff22 b920ef231df0d1fb; do\n  [ -f \"$f.txt\" ] && echo \"OK $f\" || echo \"MISSING $f\"\ndone\necho \"--- index entries for page 105 ---\"\ngrep -c 'page 105' index.jsonl",
 "description": "Verify archived sources"
}
```


### [2026-09-05T17:31:05.817Z] TOOL RESULT

```
OK aab5e5692825f204
OK 07fbd11449f9d7a8
OK b72cc012ea3476d4
OK d6418b07671b1447
OK 05a271aafb1a0bff
OK 0fa547e391100612
OK 123cc88dc937f12a
OK 2cbebb2fd375ff22
OK b920ef231df0d1fb
--- index entries for page 105 ---
11
```


## [2026-09-05T17:31:27.851Z] AGENT

All archived sources are present and `verify_check.py 105` reports **0 PROBLEM lines**.

## Page 105 (book p. 75) — summary

3 redirect entries skipped (Carya, Čĕxara, Char). 3 entries, 17 nodes verified.

**Root verdicts:** confirmed 2 (Chiang-yu, Cîrâğ), plausible 1 (Chou-shu/Shu-shu)
**Node verdicts:** confirmed 9, plausible 5, disputed 3
**Ref checks:** supports 7, partial 2, not_found 2, not_checked 10

### Disputed
- **Cîrâğ #2 (Arabic ešrâğ, šarq)** — Arabic شرق/إشراق sit on the native Semitic root š-r-q (Wiktionary cites Hebrew זָרַח/מִזְרָח; Klein derives sharq from sharaqa). Asbaghi does print the guess, but hedged twice ("Vielleicht" p.157, "eventuell" p.21). Phonetically impossible: the real reflex of čirāγ is سراج (node #10), not a doublet with š- and qāf plus a full verbal paradigm. Nourai's own box note is accurate.
- **Cîrâğ #5 (Greek Sarakěnos)** — Σαρακηνοί is in Ptolemy (c. 150 CE), centuries before Greek could take an ethnonym from Arabic; Etymonline: "usually said to be from Arabic sharquiyin … but this is not certain." Klein/AHD 1975 (Nourai's refs) print it without caveat.
- **Chou-shu #1 (Mongolian)** — no source for a Mongol vector: SIN 565-566 §29 has no Mongolian step, Mo'in takes the word straight «از چینی shū», and the earliest attestation (Sūzanī of Samarqand, d. c. 1173) is pre-Mongol.

### Notable ref findings
- **BQT:1309 exact hit** — vol. 3 pdf p.100 = printed 1309: headword «شوشو … بمعنی گاورس و ارزن باشد» + Mo'in's fn. 4 «از چینی shū (ارزن). ره: Laufer, Sino-Iranica, p. 565» + the Sūzanī verse in Nourai's box.
- **SIN:565 partial** — Laufer only asks the question: "It remains to study the history of this word, in order to ascertain whether it might be a Chinese loan-word." The form "Chou-shu, Shu-shu" is not on the page (he gives šu-lu).
- **MON:2089 not_found** — شوشو is absent from Mo'in's Farhang (vajehyab + local OCR); the claim actually lives in his Borhan footnote.
- **PLA:157, FVQ:166, SDQ:72, BQT:626 all support** — the Pahlavi čirāγ → Aramaic šrāgā → Arabic sirāj → Persian سراج round trip is solid; Mo'in explicitly rejects Addi Shir's reverse (Syriac → Persian) derivation.
- **Chiang-yu #1 (Dutch soja) plausible** — the arrow skips Japanese; Dutch soja is from Satsuma Japanese soi (醤油), as Nourai's own OXF note says. Modern scholarship sides with the note.

### Extraction errors
None. The JSON is faithful to the printed page (image archived at `data/verification/sources/refs/ocr/BOOK/105.png`). The breves in "Sarakěnos / Saracěnus" are Nourai's own transliteration habit, not misreads — the Greek/Latin vowel is long ē.

Unavailable references (recorded as `not_checked`): VOP:224 and FVA:188/211 (no digital copy exists), OXF:406 (IA lending-only), AHD:1152/1237 (New College main word-list, not the local IE appendix; ahdictionary.com returns no entry text to a plain fetch).
