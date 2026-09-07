# Verification process log — verify-page-362


## [2026-09-07T19:29:06.726Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 362 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-362.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-362.json. Write /home/sfmqrb/git/rishe/data/verification/page-362.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 362` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T19:29:08.824Z] AGENT

I'll start by reading the instructions and the input files.


## [2026-09-07T19:29:09.556Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T19:29:09.571Z] TOOL RESULT

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


## [2026-09-07T19:29:10.181Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-362.txt"
}
```


### [2026-09-07T19:29:10.204Z] TOOL RESULT

```
1	=== PDF page 362 (book page 332) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ner 2, Nerq, Sner, Snerq : to turn twist  (refs POK:975; KLN:1028)
4	#1 (parent #0) [Greek] refs=POK:975; KLN:1028; SKT:344; PRT:427 | narkĕ : cramp, numbness ; narkissos : a beautiful flower plant known for the seductive properties of its flowers
5	  #2 (parent #1) [Pahlavi] refs=BQT:2129 | narkis : narcissus
6	    #3 (parent #2) [Persian] refs=BQT:2129 | narges «نرگس» : narcissus ; nargeseh «نرگسه» : star, sky ; nargesî «نرگسی» : a food
7	#4 (parent #0) [Latin] refs=KLN:1028 | 
8	  #5 (parent #4) [English] refs=AHD:872 | narcissus
9	#6 (parent #0) [French] refs=None | 
10	  #7 (parent #6) [English] refs=None | narcotics
11	#8 (parent #0) [Germanic] refs=AHD | snarwa : cord, trap ; narwa : narrow
12	  #9 (parent #8) [English] refs=None | snare, narrow
13	--- entry 1 ---
14	ROOT Nerq -> redirect to Ner 2
15	--- entry 2 ---
16	ROOT [Indo-European] Nes 1 : to join, reunite, return, be safe  (refs POK:766)
17	#1 (parent #0) [Avestan] refs=POK:766 | asta 2 : home, residence
18	#2 (parent #0) [Greek] refs=POK:766 | naos : temple, sanctuary
19	  #3 (parent #2) [Syriac] refs=MON:4649 | nausâ : grave, cemetery
20	    #4 (parent #3) [Arabic] refs=MON:4649 | nâvŭs : tomb, underground cemetery
21	      #5 (parent #4) [Persian] refs=MON:4649; BQT:2086 | nâvŭs «ناووس ، ناوس ، ناؤوس» : cemetery, temple, church
22	#6 (parent #0) [Greek] refs=AHD | nostos : a return home
23	  #7 (parent #6) [English] refs=AHD | nostalgia
24	#8 (parent #0) [Germanic] refs=AHD | nas-ja : food for journey
25	  #9 (parent #8) [English] refs=AHD | harness
26	--- entry 3 ---
27	ROOT Nes 2 -> redirect to Ne 2
28	
```


## [2026-09-07T19:29:10.548Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-362.json"
}
```


### [2026-09-07T19:29:10.560Z] TOOL RESULT

```
1	{
2	  "pdf_page": 362,
3	  "book_page": 332,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Ner 2, Nerq, Sner, Snerq",
8	        "lang": "Indo-European",
9	        "refs": "POK:975; KLN:1028",
10	        "gloss": "to turn twist"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Greek",
17	          "refs": "POK:975; KLN:1028; SKT:344; PRT:427",
18	          "words": [
19	            {"translit": "narkĕ", "gloss": "cramp, numbness", "script": null},
20	            {"translit": "narkissos", "gloss": "a beautiful flower plant known for the seductive properties of its flowers", "script": null}
21	          ],
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Pahlavi",
29	          "refs": "BQT:2129",
30	          "words": [
31	            {"translit": "narkis", "gloss": "narcissus", "script": null}
32	          ],
33	          "note": null,
34	          "quote": null
35	        },
36	        {
37	          "id": 3,
38	          "parent": 2,
39	          "lang": "Persian",
40	          "refs": "BQT:2129",
41	          "words": [
42	            {"translit": "narges", "gloss": "narcissus", "script": "نرگس"},
43	            {"translit": "nargeseh", "gloss": "star, sky", "script": "نرگسه"},
44	            {"translit": "nargesî", "gloss": "a food", "script": "نرگسی"}
45	          ],
46	          "note": null,
47	          "quote": {"text": "گرد نرگس دان گردون بین هزاران نرگسه - هر طرف زین نرگسه صدگلستان آمد پدید", "poet": "A`mîd Lobakî"}
48	        },
49	        {
50	          "id": 4,
51	          "parent": 0,
52	          "lang": "Latin",
53	          "refs": "KLN:1028",
54	          "words": [],
55	          "note": null,
56	          "quote": null
57	        },
58	        {
59	          "id": 5,
60	          "parent": 4,
61	          "lang": "English",
62	          "refs": "AHD:872",
63	          "words": [
64	            {"translit": "narcissus", "gloss": null, "script": null}
65	          ],
66	          "note": null,
67	          "quote": null
68	        },
69	        {
70	          "id": 6,
71	          "parent": 0,
72	          "lang": "French",
73	          "refs": null,
74	          "words": [],
75	          "note": null,
76	          "quote": null
77	        },
78	        {
79	          "id": 7,
80	          "parent": 6,
81	          "lang": "English",
82	          "refs": null,
83	          "words": [
84	            {"translit": "narcotics", "gloss": null, "script": null}
85	          ],
86	          "note": null,
87	          "quote": null
88	        },
89	        {
90	          "id": 8,
91	          "parent": 0,
92	          "lang": "Germanic",
93	          "refs": "AHD",
94	          "words": [
95	            {"translit": "snarwa", "gloss": "cord, trap", "script": null},
96	            {"translit": "narwa", "gloss": "narrow", "script": null}
97	          ],
98	          "note": null,
99	          "quote": null
100	        },
101	        {
102	          "id": 9,
103	          "parent": 8,
104	          "lang": "English",
105	          "refs": null,
106	          "words": [
107	            {"translit": "snare, narrow", "gloss": null, "script": null}
108	          ],
109	          "note": null,
110	          "quote": null
111	        }
112	      ]
113	    },
114	    {
115	      "root": {"name": "Nerq", "redirect": "Ner 2"},
116	      "nodes": []
117	    },
118	    {
119	      "root": {
120	        "name": "Nes 1",
121	        "lang": "Indo-European",
122	        "refs": "POK:766",
123	        "gloss": "to join, reunite, return, be safe"
124	      },
125	      "nodes": [
126	        {
127	          "id": 1,
128	          "parent": 0,
129	          "lang": "Avestan",
130	          "refs": "POK:766",
131	          "words": [
132	            {"translit": "asta 2", "gloss": "home, residence", "script": null}
133	          ],
134	          "note": null,
135	          "quote": null
136	        },
137	        {
138	          "id": 2,
139	          "parent": 0,
140	          "lang": "Greek",
141	          "refs": "POK:766",
142	          "words": [
143	            {"translit": "naos", "gloss": "temple, sanctuary", "script": null}
144	          ],
145	          "note": null,
146	          "quote": null
147	        },
148	        {
149	          "id": 3,
150	          "parent": 2,
151	          "lang": "Syriac",
152	          "refs": "MON:4649",
153	          "words": [
154	            {"translit": "nausâ", "gloss": "grave, cemetery", "script": null}
155	          ],
156	          "note": null,
157	          "quote": null
158	        },
159	        {
160	          "id": 4,
161	          "parent": 3,
162	          "lang": "Arabic",
163	          "refs": "MON:4649",
164	          "words": [
165	            {"translit": "nâvŭs", "gloss": "tomb, underground cemetery", "script": null}
166	          ],
167	          "note": null,
168	          "quote": null
169	        },
170	        {
171	          "id": 5,
172	          "parent": 4,
173	          "lang": "Persian",
174	          "refs": "MON:4649; BQT:2086",
175	          "words": [
176	            {"translit": "nâvŭs", "gloss": "cemetery, temple, church", "script": "ناووس ، ناوس ، ناؤوس"}
177	          ],
178	          "note": null,
179	          "quote": {"text": "بسام ابرص و حربا و خنفسا و جعل - بجیفه گاه و بناووس و مستراح و خلاب", "poet": "Khâqânî"}
180	        },
181	        {
182	          "id": 6,
183	          "parent": 0,
184	          "lang": "Greek",
185	          "refs": "AHD",
186	          "words": [
187	            {"translit": "nostos", "gloss": "a return home", "script": null}
188	          ],
189	          "note": null,
190	          "quote": null
191	        },
192	        {
193	          "id": 7,
194	          "parent": 6,
195	          "lang": "English",
196	          "refs": "AHD",
197	          "words": [
198	            {"translit": "nostalgia", "gloss": null, "script": null}
199	          ],
200	          "note": null,
201	          "quote": null
202	        },
203	        {
204	          "id": 8,
205	          "parent": 0,
206	          "lang": "Germanic",
207	          "refs": "AHD",
208	          "words": [
209	            {"translit": "nas-ja", "gloss": "food for journey", "script": null}
210	          ],
211	          "note": null,
212	          "quote": null
213	        },
214	        {
215	          "id": 9,
216	          "parent": 8,
217	          "lang": "English",
218	          "refs": "AHD",
219	          "words": [
220	            {"translit": "harness", "gloss": null, "script": null}
221	          ],
222	          "note": null,
223	          "quote": null
224	        }
225	      ]
226	    },
227	    {
228	      "root": {"name": "Nes 2", "redirect": "Ne 2"},
229	      "nodes": []
230	    }
231	  ]
232	}
233	
```


## [2026-09-07T19:29:16.024Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"---MATRIX---\" && cat data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-07T19:29:16.082Z] TOOL RESULT

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
---MATRIX---
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


## [2026-09-07T19:29:17.802Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SKT','PRT','BQT','AHD','MON','WLD','IEC','SYN','BRT','KNT','PHD','NYB','HRN','HUB','CHEUNG','ARY','FVQ','AFM','PLA','FSD','WEB','LKT']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-07T19:29:19.097Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (al
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG MISSING
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
```


## [2026-09-07T19:29:26.074Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SKT','PRT','BQT','AHD','MON','WLD','IEC','SYN','BRT','PHD','NYB','HRN','HUB','AFM','FVQ','PLA','AFA','TAD','ARB','LKT','FSD','WEB','SKT']:\n    v=d.get(k)\n    if not v: continue\n    print('==',k, '| page_offset:', v.get('page_offset'), '| local:', v.get('local_file'), '| hint:', str(v.get('lookup_hint'))[:300])\n\""
}
```


## [2026-09-07T19:29:26.962Z] TOOL CALL #7: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -80 && echo --- && ls data/verification/sources/refs/ocr/ 2>/dev/null | head"
}
```


### [2026-09-07T19:29:27.321Z] TOOL RESULT

```
== POK | page_offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== KLN | page_offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== SKT | page_offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== PRT | page_offset: None | local: None | hint: Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q=<word>. Entries are alphabetical with numbered sub-senses.
== BQT | page_offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== AHD | page_offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== MON | page_offset: None | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== WLD | page_offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== IEC | page_offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== SYN | page_offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== BRT | page_offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== PHD | page_offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB | page_offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== HRN | page_offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== HUB | page_offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== AFM | page_offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] | hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
== FVQ | page_offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] | hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
== PLA | page_offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] | hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
== AFA | page_offset: leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt | hint: Arabic/Aramaic in script (not OCRed) with German glosses; grep the German meaning or transliteration.
== TAD | page_offset: 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt'] | hint: Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
== ARB | page_offset: None | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt'] | hint: Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.
== LKT | page_offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt | hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== FSD | page_offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== WEB | page_offset: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.
== SKT | page_offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
```


### [2026-09-07T19:29:27.364Z] TOOL RESULT

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
```


## [2026-09-07T19:29:33.402Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma:.*sner\" POK_full.txt | head -20; echo ---; grep -n \"lemma: nes\" POK_full.txt | head -20; echo ---; grep -n \"lemma: ner\" POK_full.txt | head"
}
```


### [2026-09-07T19:29:33.487Z] TOOL RESULT

```
---
62783:Root / lemma: nes- {*he- nes-) 
---
62647:Root / lemma: ner-1(t)-, aner- {aner-1) {*he- ner-1(t)-) 
62734:Root / lemma: ner-2{*he- ner-2) 
62751:Root / lemma: ner-3{*he- ner-3)
```


## [2026-09-07T19:29:35.185Z] TOOL CALL #9: Bash

```json
{
 "command": "pdftoppm -f 362 -l 362 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg362 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T19:29:36.947Z] TOOL RESULT

```
total 30644
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 15:29 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb  1579505 Sep  7 14:24 afm76.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1055262 Sep  7 14:23 afm77.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1297 Sep  7 15:29 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   153966 Sep  7 13:44 bqt2014_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb    46690 Sep  7 13:44 crop_av3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40759 Sep  7 13:44 crop_heb.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94819 Sep  7 13:44 crop_pers0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78732 Sep  7 13:40 ffd32.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    76202 Sep  7 15:29 pg362.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 13:36 queue.txt
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


## [2026-09-07T19:29:43.745Z] TOOL CALL #10: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg362.png"
}
```


## [2026-09-07T19:29:44.159Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '62734,62800p' POK_full.txt"
}
```


### [2026-09-07T19:29:44.197Z] TOOL RESULT

```

```


## [2026-09-07T19:29:44.192Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


### [2026-09-07T19:29:44.255Z] TOOL RESULT

```
Root / lemma: ner-2{*he- ner-2) 
Meaning: under 

Material: Gr. vsprspoq ' unterer, tieferer, unterirdischer ' (through hybridization with svspoi 
"the subterraneous, underground', s. S. 312 *en^\x\\ also £V£pT£po(;); V£p9£(v) (and again 
£V£p9£(v), Doric Aeolic £V£p9a) "from under'; V£ip6(; "the Unterste' ( *nerio-)\ Oscan nertrak 
" left hand ', Umbrian nertru^ left ' (= v£pT£po(;); zero grade Old Icelandic nordru. "north'. Old 
English norderra'more northern'. Old High German /70/r//'d/7/" northern' (The north is to the 
direction of the prayer to the east = on the left); 

possible kinship from n-er-wWh *n-ei- "low, base' (see 312). 

Maybe alb. Geg ner, alb. /7o'e/'" under' [common alb. n >/7o' shift] 

References: WP. II 333 f. 
Page(s): 765-766 

Root / lemma: ner-3{*he- ner-3) 

Meaning: to conceal, cover, hiding place, hollow 

Material: established only for the Balto-Slavic: Lithuanian neriu, nert/" immerse, swim through, 

flee, einschlijpfen ', nerisxw. "beaver', narasm. ' Taucherente ', nan/a' cell of the queen bee 

', Latvian n/'rt, n/rdaf submerge '; Old Church Slavic ntrg, n ret/" penetrate' , sloven, po- 

ndreti" submerge ', kir. po-nerty'6'we', Old Church Slavic nora^ (pu)kzd(;, a hiding-place, 

lurking-hole, covert, den ', russ. nora'\r\o\e, cave, pit, pothole'. Old Russian po-norovb^ 

earth worm ', serb. norac^ aquanaut '; auf a zero grade *n-br- ( *nor-to Indo Germanic *nor- 

) based on Slavic nyr-, nur- in russ. -Old Church Slavic nyrjati, " dip, immerse ', nura^ door| 

entrance ' (etc.); here probably FIN Old Prussian Narus, Lithuanian Nar-upe, lllyrian Napwv 

' Narenta ' = Scots Gaelic Abhainn Narunn^ Nairn '; Lithuanian Neris, Nerys, Nereta, Old 

Prussian Neria " spit, tongue of land ', russ. Neretva (to Bug). 

References: WP. II 334, Trautmann 196 f., Pokorny Urillyrier 3 f., 45; 

See also: perhaps to ner-2. 

Page(s): 766 



Root / lemma: nes- {*he- nes-) 

Meaning: to join with; to conceal oneself 

Material: Old Indie nasate^ unites, joins ', redupl. unthematic nimsate'^. PI. " sie berijhren 

lahe mit dem Korper, kiss ' {*ni-ns-ate), participle n/ms-ana- {o\6 Deponentien); GN 

Nasatyauxw. Dual. ' both helpers in need ', Proto Indie Nasattia, Avestan Narjhai&ya-, 

compare H. GiJntert, Weltkonig 259; 

zero grade Old Indie asta-, Avestan asta-v\. 'homeland, domicile'; gr. vsopai, Ionian 
VEupai " come happily, return iiome, journey bacl< home ', Negtcjop actually ' the always 
returning ', voaroq m. " iiome coming, returning iiome ', redupl. ep. viao|jai " go, come with' (*vi- 
vG-opai with preservation of -a- after unthematic forms as 2. 3. Sg. *vi-va-aai, -tqi); 
reduced grade vaiw, Fut. vaaaopai 'stay, dwell, inhiabit ', vaiEiau) "stay, dwell, inhiabit; be 
inhabited '; *vaa-F6(;: Doric Thessalian yabc,, lak. vc(Fo(;, Lesbian vauoc, (i.e. vaFFo(;), Ionian
```


## [2026-09-07T19:29:53.297Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '62800,62830p' POK_full.txt; echo \"=====SNER=====\"; grep -n \"Page(s): 97[0-9]\" POK_full.txt | head -20"
}
```


### [2026-09-07T19:29:53.358Z] TOOL RESULT

```
inhabited '; *vaa-F6(;: Doric Thessalian yabc,, lak. vc(Fo(;, Lesbian vauoc, (i.e. vaFFo(;), Ionian 
vr|6c;, Attic vsux; m. "( god's abode =) temple, shrine '; zero grade ao\xzyoc, ' gerettetj 
geborgen '; 

alb. knelem^ recover, be living again ' (prefix k-+ *nes-lo-)\ Gothic ^a-/7/sa/7"gerettet 
become, recover, recuperate ', Old High German Old Saxon g/-nesan ds., Old English ge- 
nesan' are saved, escape, survive ', Gothic ga-nists. Old High German Old Saxon gi-nist 
"recovery, salvation'; Kaus. Gothic nas/anl\t, make healthy'. Old High German nerian, 
nerren^ rescue, heal, cure', /75/7/'e/7 "nourish'. Old Saxon nerian. Old English nerian 
"rescue, shield ' (besides with e, dOld Icelandic /7^/'aand nora^ animate, refresh, 
nourish ', Swedish dial. /7c>/'5 "start a fire'); Old Icelandic aidr-narim. "( life preserver =) fire', 
Old Saxon iTf-narai. "nourishment, food'. Old English nerui. "salvation, nourishment, food'. 
Old High German nerf, narai. "salvation, nourishment, food'; latter meaning also in Old 
High German wega-nest, -nistu. " travel food ', Old English nestn. "nourishment, food', 
Old Icelandic nestn. " provision for a journeyl traveling allowance; money saved by soldiers, 
nourishment, food'; Tocharian A nas-, B nes-'be'; A /7a5i/- "friend'. 

References: WP. II 334 f., M. Leumann Homer. Worter, 191 ff. 
Page(s): 766-767 

Root / lemma: neu-6^- {*he- neu-dy-) 

Meaning: to yearn for smth. 

Material: Old High German niot^ eagerness ', Middle High German niet/iche'\N\t\r\ desire, 

with eagerness ', Modern High German niediicfi. Old Saxon niudm. "desire, yearning'. Old 



English med, neodi. "wish, longing, yearning, eagerness '; Gothic PN Neudis {*Niudeis); 
=====SNER=====
78562:Page(s): 970 
78584:Page(s): 970-971 
78666:Page(s): 971 
78672:Page(s): 971 
78800:Page(s): 971 
78822:Page(s): 972-973 
78888:Page(s): 971-972 
78893:Page(s): 974 
78931:Page(s): 974 
78948:Page(s): 974 
78967:Page(s): 977 
79008:Page(s): 975 
79083:Page(s): 975-977 
79111:Page(s): 977-978 
79129:Page(s): 978 
79153:Page(s): 978 
79159:Page(s): 977 
79179:Page(s): 973-974 
79190:Page(s): 974-975 
79225:Page(s): 977
```


## [2026-09-07T19:29:54.419Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: (s)ner\\|lemma: sner\\|lemma: snerk\\|lemma: snerg\\|lemma: ner-1\" POK_full.txt | head"
}
```


### [2026-09-07T19:29:54.491Z] TOOL RESULT

```
62647:Root / lemma: ner-1(t)-, aner- {aner-1) {*he- ner-1(t)-) 
78952:Root / lemma: (s)nerb- 
78969:Root /lemma: (s)ner-l, (s)nur- 
79010:Root / lemma: (s)ner-2
```


## [2026-09-07T19:29:57.859Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '78948,79040p' POK_full.txt"
}
```


### [2026-09-07T19:29:57.949Z] TOOL RESULT

```
Page(s): 974 



Root / lemma: (s)nerb- 
Meaning: to cut 

Material: Gr. voppsT svTapisTrai, voppa KaArj Hes. (as Modern High German 'schneidig'?); 

also Gothic at-snarpjan 'aniassen'7; Old Icelandic snarpr^ sharp, hart, uneven', snerpa' 

sharpen ', Dutch snerpen'b\te (from Wunden), ache', westfal. sn/rpsch ^ sharp (of wind)'; 

Old High German s/7eAi'&/7 'together pull, drag'; without s-: nisi, norpa' freeze '. 

References: WP. II 701; 

See also: whether to the above sner-b- {sner-2)7 

Page(s): 977 

Root /lemma: (s)ner-l, (s)nur- 
Meaning: to murmur, grumble 

Material: Gr. evupsv Eipiasv; svupnaeK; 9pr|vr|a£iq; ovupi^EOi 65up£Tai Hes.; Middle High 
German snarren^ burr, babble, chatter', snerren^ babble, chatter', s/7^/re/7 'sough, rustle, 
buzz, whirr', snurraere, snurrinc^ merrymaker, fool'. Modern High German schnarren, 
schnurren, Schnurre, engl. snarr growl ', Middle English snorin, nengl. snore 
'schnarchen'. Middle English sneren, nengl. sneer^ contemptibly laugh'; Middle English 
/7^/77e/7'hersagen', Swedish dial, noma, /7y/77a 'zuflij stern'. Old Icelandic norn 
'Schicksalsgottin', Middle High German narren, nerren^ growl ', Old High German narro 
'fool\ 

Lithuanian niurniu, n/urnef/" dror\e, grumble, growl '; Latvian nura'e'\r\ weinerlicher 
person', nurat'dror\e, grumble, spinnen as eine cat '. 

Auf -{//Middle English s/7i//Y//7 'schnarchen'. Middle High German 5/75/2- 'Schnarre, 
Wachtelkonig'; Latvian /7i/?D'e/ 'murmur, drone, grumble, growl '. 

Auf-p: Norwegian Swedish s/7e/'/ra'prusten, schnarchen', Swedish snurka' groan ', 
Middle Low German snorken, s/75/'/re/7 'schnarchen, pant, sniff, snort'. Middle High 
German snarchends.. Modern High German schnarchen, Norwegian nurka^creak, growl ', 
Dutch nurken 'dror\e, grumble, norgein'; Lithuanian snarglys^ nasal mucus ', Latvian 
snurgalasds. ('*rattling, clashing, groaning '); snirguoV sob; fauchen as die Ganse'; 
Latvian nrrgu6ties^\\b\\r\\sc\\ laugh', hu?gt'd\e Zahne show'; also probably Lithuanian 
/757y/K// "somewhat slowly tun' (meaning similarly as in Swiss norggen ' o\r\r\e Erfolg 
arbeiten'). 



Auf -A:" Old Icelandic sngrgia {*snarguldn) " groan ', Modern High German norgeln, 
nergeln^ inarticulate sprechen, with verdrieftlichem naselnden Tone tadein'; Lithuanian 
niurksau, -oti^ dismal or brijtend dasitzen', Latvian hurk'et, hurkstet, nurkset^ drone, 
grumble, murmur, growl ', ngrka'e\n weinerlicher person', /7aA/rse/"weinerlich sein, creak', 
n/rksfet' gnash, ein Gerausch make, as if etwas bricht', snirkt^ gnash '. 

Auf -p:0\6 Icelandic snarfla^ groan ', Norwegian Swedish snarva^ growl, die Zahne 
fletschen'. 

References: WP. II 698 f. 
Page(s): 975 

Root / lemma: (s)ner-2 

Meaning: to turn, wind, etc.. 

Note: perhaps extension to sne- ds. 

Material: Old Indie nrtyat/ ^tanzt', nrtf-i. " dance, game', /7/f^- "tanzend', narma-n., narma- 

m. " joke ', narfstai. ds., etc.; miran. nar- 'catch'(Persson Beitr. 816a 1); 

gr. vapva^ kiPu)t6(; Hes. (and inschriftlich), from which dissim. Aapva^ 'Kasten, hutch, 
vessel'; through Weitergreifen this dissim. Wandels also *vapKOc; (from the /r-extension, 
see below), still receive in vapKiov aoKoc, Hes., to AapKO(; "basket'; 

Old Saxon nam. Old English nearu, engl. /75/7'ow" narrow' {*nar-wa- actuaWy 
"zusammengeschnijrt'). Old Icelandic in Ngrva-sund ^G\bra\tar' (besides Mgrva-suncf and 
Modern High German Nehrung^ spit, tongue of land, schmale promontory ' from *ner-wa-). 
Old High German narwat, narwom. "scar' (i.e. "zusammengezogene Wundrander'), also 
"ansa, fibulatura'. Modern High German Narbe d\a\. also " agrafe, hook, clasp, Krampen an 
TiJren' as Norwegian norve' agrafe, hook, clasp, cramp' (and Latvian nars, nare' agrafe, 
hook, clasp '); 

Modern High German Bavarian der-narren' rigid become, particularly, specially, 
especially, particular: in particular, peculiarly, separately, extra, notably vor frost' ("*shrink 
up, -krampfen'), /75/7'"miftratene verschrumpfte fruit', narr{S\N\ss) krampfartige Spannung', 
narrennage/ ^uni6rm\g ausgewachsener Nagel'; zero grade (with s-) Modern High German 
schnurren, ein-schnurren, -schnorren ^s\\uye\ up, shrink', isl. snurda^knoi an a Faden, 
bildlich of NasenriJmpfen'; 

lengthened grade Old Icelandic nari^ groin ' ("Einschnurung of Leibes'), Middle High 
German naerlich ^conc\se, genau, young ' and with gradation Old Icelandic Nori
```


## [2026-09-07T19:30:01.929Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '79040,79115p' POK_full.txt"
}
```


### [2026-09-07T19:30:02.029Z] TOOL RESULT

```
German naerlich ^conc\se, genau, young ' and with gradation Old Icelandic Nori 



'Zwergname', norv\. "narrow bay, Sund', Danish Swedish /7c»/'"toddler, whole small kid, 
child"; 

probably Old High German snuor'cord, band, strap, rope, cable', Danish-Swedish snor 
6s., Gothic 5/70/70 "geflochtener basket'. Old English sner {* snorio) " string of a harp'. Old 
Icelandic sn0rix\. 'gedrehtes rope, band'; 

Lithuanian neriu, nerti^ submerge, einschlijpfen, einfadein', nyrli, preterit nirau, nirti 
"sich schlangein, ranken', /sn/rt/^s\c\r\ dislocate, luxate, crick ', naras' aquanaut ', narys' 
loop, noose, snare; joint, limb, member'; Latvian nars, nare^ agrafe, hook, clasp '; 

russ. neret, neret6^V\v\6 offish snaring net'; 

here belongs ner-3, above S. 766. 

extensions: 

5/7er-i&- with Germanic p. Norwegian dial. 5/70/775 stem V. ' shrivel, shrink due to excess 
dryness, wrinkle up, shrink up ', Old High German {bi-, fir-) snerfan^den Mund 
zusammenziehen, die Miene verfinstern'. Bavarian schnurfen's\c\r\ einziehen, shrink ' = 
Norwegian snurpa la\te\n, loose stitch up, sew together', Norwegian snerp'sk\n auf the 
milk'. 

sner-g-:0\6 English 5/70C»/r5/7 stem V. " shrivel, shrink due to excess dryness, wrinkle 
up ', Norwegian snerka, snyrkjads., snerk(e)xx\. "thin skin auf the milk'. Old Icelandic 
snerkja ( *snarkian) "pull together, furrow '. 

^5^/7e/"-Ar-; Armenian /70/'(goi/" tenuis, gracilis' ("*zusammengeschnurt or eingeschrumpft'); 

gr. vapKH "das solidification, cramp, Lahmung; Krampfrochen', vapKav " solidify, congeal 
' (see also above about vapKiov, AapKO(;); Old High German sner(a)han (stem V.) 
"schlingen, tie, bind, knot, bind'. Middle High German snerhen^ tie, bind, knot, bind, pull 
together'. Old High German snar{a)ha^ loop, noose, snare ', Old Icelandic snara 
{*snarhdn) "schlingen, tie, bind, knot, coil ', snarai. " loop, noose, snare ' (Scandinavian 
loanword is Old English snearei. " loop, noose, snare '), snarr^rash, hasty, sharp'. Middle 
Low German snarllken Mn . "quick, fast, bald'. Old English snierian^hurrY from *snarhian 
("quick, fast' from "was sich dreht, quick, fast wendet'). 

References: WP. II 699 ff., WH. II 165, Trautmann 197, Vasmer2, 213 f. 
Page(s): 975-977 



Root / lemma: sneu b^- {*sneu- b^-) 

Meaning: to woo, marry, nymph 

Note: 

Root/ lemma: snusos {* snousos): daughter-in-law : Root/ lemma: sneit'^-{*sneu-b'"-): to 

woo, marry, nymph, derived from a suffixed in -b^-format of Root/ lemma: sna- sna-(t-J, 
snau-, sn-eu-, sn-et-: to flow, swim; damp, nymph of waters. 

Material: Latin nubo, -ere, -psi, -ptum^ marry, from the wife, woman', pronuba' married 
woman who conducted the bride to the bridal chamber ', conubium {*co-snubiom) " 
marriage/wedlock; right to marry; act/ceremony of marriage (usu. pi.) '; 

russ. -Church Slavic snubiti^ couple ', Czech snoubiti^ woo, court, marry, betroth ' 
(Kaus. *snoub^eid); with secondary nasalization proto Slavic, dial. *sngb-; 

nasalized gr. vuijcpn "bride, virgin, nymph ', vuiJ(piO(; ' bridegroom ', vupcpsuw " betroth '; 

probably as *snusos^rorr\ the connection through marriage and extension to sneu-' 
Faden zusammendrehen. tie, bind, knot '. 

References: WP. II 697, WH. II 183 f., Trautmann 273, Vasmer2, 683. 
Page(s): 977-978 

Root / lemma: sneud(h)-1 

Meaning: drowsy, to drowse
```


## [2026-09-07T19:30:10.987Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^narcissus\\|^narcotic\\|^narrow\\|^snare\\|^narcosis\" KLN_1966.txt | head -20"
}
```


### [2026-09-07T19:30:11.035Z] TOOL RESULT

```
24979:narcosis,  n.,  state  of  unconsciousness  caused  by a  narcotic  (med.)  —  Medical  JL.,  fr.  Gk.  vap- x coai.p,  ‘a  benumbing’,  fr.  vapxouv,  ‘to  benumb’. See  narcotic  and  -osis.
24980:narcotic,  adj.,  producing  insensibility.  —  F.  nar- cotique,  introduced  into  French  in  1314  by  Mon- deville  fr.  ML.  narcoticus,  fr.  Gk.  vapxomxo ‘benumbing’,  fr.  vapxwxo?,  verbal  adj.  of  vap- xouv,  ‘to  benumb’,  fr.  vipxvj,  ‘numbness’, prop,  ‘a  cramp’,  fr.  I.-E.  *{s)ner-q-,  ‘to  turn, twist’,  whence  also  Arm.  nergev,  ‘fine,  thin, slender,  slim’,  prop,  ‘shriveled  up’;  see  Hof¬ mann,  EWG.,  pp.  211-12  s.v.  vapXT].  I.-E. *(s)ner-q-  is  a  -(/-enlargement  of  base  *(s)ner-, ‘to  turn,  twist,  bind  together’,  whence  OE. sneare,  ‘snare’,  nearu,  ‘narrow’.  See  snare  and cp.  narrow.  For  the  ending  of  narcotic  see  suff. -otic.
24988:narrow,  adj.,  of  small  breadth.  —  ME.  narewe, narwe,  naru,  fr.  OE.  nearu,  rel.  to  OS.  naro, MDu.  nare;  orig.  prob.  meaning  ‘twisted  up, shriveled  up’,  fr.  I.-E.  base  *(s)ner-,  ‘to  turn, twist,  bind  together’,  whence  also  OE.  sneare, ‘snare’.  See  snare  and  cp.  narcotic.
36722:narrow’,  axstvoc;,  ‘a  narrow  space’;  of  uncer¬ tain  origin.
```


## [2026-09-07T19:30:11.623Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^NARCISSUS\\|^NARCOTIC\\|^NARROW\\|^SNARE\" SKT.txt | head"
}
```


### [2026-09-07T19:30:11.667Z] TOOL RESULT

```
17603:SNARE,
```


## [2026-09-07T19:30:17.450Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"narcissus\" KLN_1966.txt | head -10; echo \"=== leafnum ===\"; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['narcissus,','narcotic,','narrow,  adj','snare,  n']:\n    i=t.find(pat)\n    print(pat, 'leaf', t[:i].count('\\f') if i>=0 else 'NF')\nEOF"
}
```


## [2026-09-07T19:30:18.051Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17595,17615p' SKT.txt; echo \"=== SKT NARC ===\"; grep -n -i \"narcissus\\|narcotic\\|^NARROW\" SKT.txt | head"
}
```


### [2026-09-07T19:30:19.001Z] TOOL RESULT

```
20366:jonquil,  n.,  1)  a  variety  of  narcissus ;  2)  its  bulb.  —
24969:—  G.  Narzissismus,  coined  by  the  Jewish  physi¬ cian  Sigmund  Freud  (1856-1939),  founder  of psychoanalysis,  fr.  Narcissus  and  suff.  -ism.
24972:Narcissus,  n.,  a  beautiful  Greek  youth  who  fell  in love  with  his  own  reflection.  He  pined  away  with desire  and  was  changed  into  the  flower  bearing his  name  (Greek  mythol.)  —  L.,  fr.  Gk.  Nap- xiaaoc,.  See  next  word.
24973:Narcissus,  n.,  a  genus  of  bulbous  plants  (hot.); ( not  cap.)  any  plant  of  this  genus.  —  L.  narcissus, fr.  Gk.  vapxiooop.  ‘narcissus’,  which  is  prob.  of Aegean  origin  but  was  assimilated  to  vdpxrj, ‘numbness’  (in  allusion  to  the  sedative  properties of  this  plant).  Cp.  prec.  word, narcolepsy,  n.,  recurring  attacks  of  sleep  (med.)
29430:polyandrous,  adj.,  1)  practicing  polyandry;  2) (bot.)  having  20  or  more  stamens.  —  G  k.  rcoXuav- 8po?.  See  next  word.  For  E.  -ous,  as  equivalent to  Gk.  -oq,  see  suff.  -ous. polyandry,  n.,  1)  the  condition  of  having  more than  one  husband  at  the  same  time;  2)  (bot.) the  presence  of  20  or  more  stamens  in  one flower.  —  Gk.  iroXuavSpia,  fr.  noX’javSpo;, ‘having  many  husbands’,  introduced  into  bot¬ any  by  Linnaeus  in  the  sense  of  ‘having  many stamens’;  compounded  of  nbkuq,  ‘much,  many’ and  avfjp,  geri.  avSp6?,  ‘man,  husband’.  See poly-,  andro-  and  -y  (representing  Gk.  -la), polyanthus,  n.,  1)  a  cultivated  variety  of  primrose; 2)  any  of  the  species  Narcissus  tazetta.  —  ModL., fr.  Gk.  7toXuavffop,  ‘abounding  in  flowers’,  fr. 7roXuq,  ‘much,  many',  and  civO-op,  ‘flower’.  See poly-  and  anther.
=== leafnum ===
narcissus, leaf 550
narcotic, leaf 550
narrow,  adj leaf 551
snare,  n leaf 593
```


### [2026-09-07T19:30:19.056Z] TOOL RESULT

```
L   was    '  nattened    with     the     hammer,'    or
^^L'  forged ;  *  from  a  lost  strong  verb  smtV-an, ^^Kto  forge  (pt.  t  smd^*,  pp.  smUen*^',  the j^^'form  smooth  being  due  to  the  pt.  t  smdtS  *. This  supposed  strong  verb  still  exists  in the  cognate  Swred,  dial.  smUa,  to  forge, pt.  t.  smed^  pp.  smidfH  (Rieti);    cf.  Dan.
I   smtdi,  to  forge,  smuU^,  malleable,  supple.
^^^^ft  Further  allied  to  G.  geschmeiiiix, ^^Kaalleable,  smooth,  Du.  smijMg,  malleable. ^^^  Der.  smoothtj  verb.
[  BTDith.    (E.)      A.  S.   /m*5,  a  worker
with  the  hammer.  — A.  S.  smiS-tn  •,  pp.  of lost  strong  verb  sml^n  •  (sec  above). +  Du. smui\  Ice!. /«/iV:    Don.  Swed.  .;#//(/ ;  G. schmied;  Goth,  smitha.       Cf.  Don.  smedt, Swcd.  jMid^.  to  forge;  Icel.  nff/fi,  smith's work,  from  an  Icel.  lost  strong  verb  cog- nate wilh  Swcd.  dial,  smida  (above).     Der. smithy.  A.  S.  smt^'^  Uccl.  smfti/a). Smother,  Smoulder;  see  Braell. Bmu^,  Smuggle :  sec  Smock. Smudge,  Smut ;  see  Smit«. J  Snack;  sec  Snatch,
^K   Snaffle ;  see  Snap. ^^K  Snag,  a  short  branch,  knot  on  a  stick, |^"^ftbnipt  projection.  (C)     A  sb.  from  prov. K.  snd^,  to  trim,  cnt  sm.ill   branches  from a  trie.  —  Gael,  snatch,  lo  hew^  cut  down, trim  trees  ;  Irish  snaigh^  a  hewing,  catting. Snail.  Snake;  see  Bneok. Snap.   verb.    (,Da.)       Ou.   wafprn,    to •nap,  snatch.  4- Dad.  snafpe,  Swcd.  stiappa, G.  s<hnappttt.      (Base   SNAP,  allied    to SXAK.)     See  Snatch.
neb.  beak,  nose.  (E.)  M.  E.  neb,  face. A  S.  neMi,  face.^Du  R<^,bill,  nib,  mouth ; Icel.  ntf,  nose ;  Dan  nab ;  Swed.  nahb. p.  Put  for  smb  • ;  cf.  Da  /«/i5.  bill,  beak  ; G.  schneppi,  nozzle;  G.  srhnaUL  bill. M.  H.  G.  tftabil,  from  M.  H.  C.  sftabtn,  to «p.  Y*  Ilcncc  sm^  is  for  m€p*\  from the  vetb  u  snaf.
SNARE,
nib.  point  of  a  pen.  <E,)  Aootbcrlba of  neb ;  see  above.
nipple,  a  teat.  (£.)  Formerly  «< (PaUgravc) ;  dimin.  of  nib  or  iw;  s above.     Dor.  nippU-wort.
snaffle.  (T>u.)    V\x\.iox  smtffit-pitftA nasc-piece.  — Du.  xwopc/,  a  har«e*s  mu O.  Do  sfiavtl,  sHobtl,  bill,  snoot.     Dun) of  O.  Du.  snabbe,  stiebbe.  bill. 'snapper;*  put  for  snapped,  from snappen,  to  snap  up  ;  see  Snap.
snip,  vb.   (Du.)     Dq.  snippen^ clip;  weakened  form  of  mapptn,  to* intercept;    see   8nap.  +  G.    tfAmppen, snap;  allied  lo  ti-Anapptn.      ^  Prob. fused  with  Nip.     Der.  inip,  sb a  smoJl  piece.  *•
snipe,  a  bird.  (Scaad.)    M.  E.  tnyfr. Icel.  sn/pa,  a  snipe:  Dan.  sn^ppr.  a  sniiic Swed.   sniippa,  a  sand-piper.  +  Do, snep,  O.   Du.  snippe,  tnrppei   G It  means  'a  snapper;*  cf.  O.  Do. beak,  lit.  crupper.     ^  See  aUo  Bnnb Snare,  a  noose.    (K.)     A.  S.  xttnsf, string,  noose. 4* Da.  moar,  a  string;  I snara;  D&n.  smtre \  Swcd. /rum;  O.M snarahha,    a    noose,      p.   The    O snarahka  shews  an  ong.   final the   sb.   is   from  a  strong  Tcrb, M.  H.  G.  s$urheM,  to  twist  tightly; a  base  SNARH  -  Aryan  VSN'AkK.w Gk.  rdptt;,  cramp;  sec   NarolasuB. ^SNAR,     lo    twist,     wind  :     see (below).      Y'  All  from   V^NA,  to spin ;  whence  L.  nert,  to  spin,  SkL sinew,  tendon.
enervate.     (L.)        From     pp.    of tner-uare,  to  deprive  of  nerre  or  tt —  L.  ;,  out  of;  mmus,  a  nenre  ;  see (below).
needle.  (E.)    Also  meld:  M.  £ also  nelde.     A.  S.  rt^t/r/. -fDu.  hlxaAV  >Ti naaM*)i    Icel.   n^iJ;    Dan.    na^t ;    S ffd/;  G.  ttadt/i  Goth.fwMi^     p.   AH  fr a  Tent,  lypc  NA-THLA,  i.  e.  srw-eT. fJ.\,  to  sew,  as  in  G.  mt/tfn,  to  sew,  L Gk.  irfi$ttv,  vietv,  to  5p,n ;  and  NA  i«  '" ^SNA,   OS    in    Irish    snatkad.  a snathaim,  I  string  together.  smudfU^ A  S.  sntar,  string,  snatc.    See  8
nerve.  (F.  -  L)     F.  mrf;  Cot Hiruum,   ace    of  neruus^  a  fioew,  -f  G wtvpoy,  a  sinew,  string ;  G.  stAmtr,  a cord,  tie.     Allied  to  Bn*i«.
neuralgia^  pain  in  the  ncrva* cm  Gk    ffv^f,   a  nerre.   an!  ^4 with    tu^    ^a.      The  Ci
From pain
SNARL.
cognate  with  L.  nentus ;  see  nerre (abovr'i,
=== SKT NARC ===
1376:Bong  (a),  a  narcotic  drug.  (FVn,) ban^.  Cf.  Skt.  bhangA,  hemp;  the being  mode  from  the  wild  hemp.
11028:monger,  a  feeding-trough.  (F-  —  L.) F.  manetoire.  —  F.  matter,  lo  eat  (above). Mandrake,  a  narcotic  ptant.  (L  —  Gk.) Short  for  mandragora,  Othello,  iii.  3.  Cf. F.  mattdragore,  Ital.  and  Span,  mandragora. —  L.  wumdragoras, -^  OV.  /«ai^pa7ufpai,  the mandrake.
11885:orphine,  the  narcotic  prin-
12160:narcissuo.  a  flower.    (L.  —  Ck.)    L. narcissus.  —  Gk.  yaptnocm ;   named  from it«  narxotic  properties. Ward,  an  unguent.  (F.  — L.  — Gk.  — Pen.
```


## [2026-09-07T19:30:34.077Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in (525,526,527,549,550,551):\n    p=pages[n]\n    # print first 200 chars and any 4-digit numbers\n    import re\n    nums=re.findall(r'\\b1[0-9]{3}\\b',p[:400]+p[-400:])\n    print('leaf',n,'|head:',' '.join(p.split())[:120])\n    print('   nums:',nums[:10])\nEOF"
}
```


### [2026-09-07T19:30:35.609Z] TOOL RESULT

```
leaf 525 |head: ere referred to. midst, n. — ME. middest, midest, formed with intensive suff. -t fr. middes, mides, adverbial gen. of mi
   nums: []
leaf 526 |head: ilesian, ‘Irish’, milk, n. — ME. melk, milke, fr. OE. meoluc, meolc, mile, rel. to OS. miluk, ON. mjolk , Swed. and Norw
   nums: []
leaf 527 |head: ter, Swed. mjelte, ‘spleen’, Norw. mjelte, ‘spleen; milt of fish’, OFris. milte, ‘spleen’, MDu. milte, Du. milt, ‘spleen
   nums: []
leaf 549 |head: l cured of leprosy by Elisha. — Heb. Na'aman, lit. ‘pleasantness’, from the stem of na'em ‘was pleasant or lovely’, when
   nums: []
leaf 550 |head: B hem, Hitt, laman (formed with dissim¬ ilation fr. *naman), Arm. a mm (gen. anuan), Gk. ovop.a (dial, form ovup.a), Alb
   nums: []
leaf 551 |head: of coconut shells, narial, adj., pertaining to the nares. — Formed fr. nares with suff. -ial. I nark,n., spy, informer, 
   nums: []
```


## [2026-09-07T19:30:48.838Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\n# find leaves with standalone 3-4 digit numbers\nfound=[]\nfor n,p in enumerate(pages):\n    for m in re.finditer(r'(?m)^\\s*(\\d{3,4})\\s*$',p):\n        found.append((n,m.group(1)))\nprint(len(found))\nfor f in found[:5]: print(f)\n# search near N\nprint([f for f in found if 520<=f[0]<=560][:20])\nEOF"
}
```


### [2026-09-07T19:30:50.446Z] TOOL RESULT

```
leaves 903
1040
(0, '1966')
(64, '100')
(64, '101')
(65, '102')
(65, '103')
[(520, '970'), (520, '971'), (521, '972'), (522, '974'), (523, '976'), (524, '977'), (524, '978'), (525, '979'), (525, '980'), (529, '986'), (529, '987'), (530, '988'), (530, '989'), (531, '990'), (531, '991'), (532, '992'), (532, '993'), (533, '994'), (535, '998'), (535, '999')]
```


## [2026-09-07T19:30:55.603Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in range(546,556):\n    print(n, re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$',pages[n]))\nEOF"
}
```


### [2026-09-07T19:30:56.939Z] TOOL RESULT

```
546 ['1021']
547 ['1022']
548 []
549 []
550 ['1028']
551 []
552 ['1033']
553 ['1035']
554 ['1036']
555 ['1039']
```


## [2026-09-07T19:31:10.073Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f,lab in [('SKT.txt','SKT')]:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    print('leaves',len(pages))\n    for n,p in enumerate(pages):\n        if 'narcissuo' in p or 'narcissus.  a  flower' in p or 'narcissus. a flower' in p:\n            print('narcissus leaf',n)\n        if 'SNARE,' in p: print('SNARE leaf',n)\nEOF"
}
```


### [2026-09-07T19:31:11.332Z] TOOL RESULT

```
leaves 657
narcissus leaf 325
SNARE leaf 472
```


## [2026-09-07T19:31:12.165Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c '' incoming/BQT/BQT_v4_pages.txt 2>/dev/null; python3 - <<'EOF'\nimport re\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nhits=[n for n,pg in enumerate(pages) if 'نرگس' in pg]\nprint('نرگس leaves',hits[:30])\nhits2=[n for n,pg in enumerate(pages) if 'ناووس' in pg]\nprint('ناووس leaves',hits2[:30])\nEOF"
}
```


### [2026-09-07T19:31:13.445Z] TOOL RESULT

```
22553
leaves 553
نرگس leaves []
ناووس leaves [193]
```


## [2026-09-07T19:31:25.900Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in range(320,332):\n    nums=re.findall(r'(?m)^\\s*(\\d{2,3})\\s*$',pages[n])\n    print(n,nums, ' '.join(pages[n].split())[:80])\nprint('---470s---')\nfor n in range(468,476):\n    nums=re.findall(r'(?m)^\\s*(\\d{2,3})\\s*$',pages[n])\n    print(n,nums, ' '.join(pages[n].split())[:80])\nEOF"
}
```


### [2026-09-07T19:31:27.152Z] TOOL RESULT

```
320 [] - tended from base MUR, as sc-en in G. murrtn, Iccl. murra^ to murmur, growl ; s
321 [] about in a r»ge Mnlny 6muk, * rushing in a &tatc of ftcoqr to the commission of 
322 ['198'] nt^ignoti, a slump. (Cf. E. trunnion -F. troigttOH^ dimin. of F. tram ^\x^. trom
323 [] ait Murder, Murther. (E.) M. morthrt. AS. ffK)rft<Jr.4-Goth. p. We also find A. 
324 ['300'] implying ' obligalion.* (£.) Only the pt. t. remains, which is now also used as 
325 [] r, (j) myrrh. its bitterness. 4* Heb. wJr, bltt Myrtle. ;F. - 1-. - Gk. - Pei my
326 [] to cat like a pig. 4* Low G. nask^ na&ty; Norw. M<ar^, greedy, naska, to champ. 
327 ['303'] No (i). Nasarite, a Jew who made vowi abstinence, &c. (Heb. ; zmtA Gk. juj Hcb. 
328 ['304'] a niece. «-L. Hiptis, a grand -daughter, niece; used OS fern, of L. nepoi (above
329 ['305'] n, tol fient into France by Nicoi Nicot is a personal name. Niece; sec Nephew. N
330 [] the ninth hour, Mk. xv. 33. « L. N^na, i. e, ninth hour, fern, of nauus^ ninth ^
331 [] not ; rfw, one. OS in fw-thinj^, no-body, by love ol nonpareu, malchlca. (F.' no
---470s---
468 [] put for sltdtktKts, lit- ' coach.' Blender, thin, feeble. (O.LowG.) sUndre. — O.
469 ['444'] /Zttiw, siisan, to slit; sec Slit Der. siiUt verb. Bliver, a splinter, twi^. (E.
470 [] slume, sb., slumber.* A. S. sluma, sb., slumber. 4-Du. sluimtren \ Dan. slumrt, 
471 ['445', '446'] liquefy j also lo tiiiitc it ichuamV smalt, blue enamel. (Ital. - O. H. G.) Ital
472 [] G. geschmeiiiix, ^^Kaalleable, smooth, Du. smijMg, malleable. ^^^ Der. smoothtj 
473 [] ish maij^, maieh» to creep. snail. (E.^ M. E. maytt, A.S. tntt^, tmgil, a snail 
474 [] the end cut off. anob, ^Scand.) Prov. E. snoh, a 'i-nlgar [Knon, aUo, % jouniey-
475 ['449', '450'] id. (E.) A. S. tSftt; also s/ju i.by tioo>. •f^ U. Sax. sdftii, adv., softl}' ;
```


## [2026-09-07T19:31:35.872Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in range(364,372):\n    nums=re.findall(r'(?m)^\\s*(\\d{2,3})\\s*$',pages[n])\n    print(n,nums, ' '.join(pages[n].split())[:150])\nEOF"
}
```


### [2026-09-07T19:31:37.928Z] TOOL RESULT

```
364 [] .) or M. E. aptchin^ to impeach, a of im^Jun, to impeach^ by the Bpa of prefix a- (L. ttJ) for im* ^L. ft impaaoh (.above). ^ftL iSpan.-Ital.-L. om^ G
365 [] cU' in a bu^, and peeped out, as re- prcscntcti in a MS. Cot. gives F. piper, ' to whistle, chirp like a bird, cousen, deceive, cheat, beguile;' pip/e
366 [] for Authorisco). We tind also Irish el. pinne, a pin, peg. spigot ; St tiyle, pen : Dq. /in. pin, p^, (r, a peg, Dan. pind, a (pointed) pinm, a pin, G
367 [] endt'cu/aru, according to ihe plumb-line, — L. pirptnditulum, a plnmmet. for careful measurement. — L. ffrNndtrt, to weigh or measure carclnlly. ^Uper
368 ['344'] k. ■J. throogh. (L. : tfr F. - L.) >ueh; whence K. /Vr-, t*ir-, Uea to Gk. ro/ia. beside; Ski. Ibftb,/aram, bcyoudj ^/rom. Itlate : see Amble. see Oap
369 [] I'ro]Jcrly pemwinkU^ Halliwell; t\.S. pinnt'int/a, a periwinkle, or sca-snail. % The A. S.pirte- IS from L.ptMaf a mussel. Pexjnre; lee Jury, Perk, to
370 ['345'] he lull derivation is iiovci pedi-^ ciude fonn [iWi 1 fool ; »ec Pedal. Petition. (F. - L.) F. pttiticn ; Cot. ' I ^ ace. fttiti^ntm^ from ftfitio, a 
371 ['547'] n adaptation of E. $piHfr\ Spelter. PH. Ph. Initial ph is distfnct from /, and has the sound of/"; it represents the Gk. ^. almost every word beginnin
```


## [2026-09-07T19:31:49.986Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in [192,193,194]:\n    print('=== leaf',n, repr(pages[n][:200]))\n# find all occurrences of 'رگس'\nhits=[n for n,pg in enumerate(pages) if 'رگس' in pg]\nprint('رگس leaves',hits[:40])\nEOF"
}
```


### [2026-09-07T19:31:51.403Z] TOOL RESULT

```
=== leaf 192 '[pdf page 193]\nنانوخیه ۱۱\nکه نان\u200cپز باشد ۱ #۰ - وهرچیزدرازمیان خالی\u200cرا هم کنته\u200cاند - وبمعنی\nنانوخیه ؟ - بنتح خای نقطه دار | رخنه و سوراخ هم\u200cآمده است - وکشتی و جهاز\nو تحتانی » بمعتی نانغواء است که زئیا'
=== leaf 193 '[pdf page 194]\n-۹۱۱۱- : ناروی\nباشد .3 بجای نون بای حهای نیز بنظرآه«ده است .\nناور ۱ - بر وزن خاور» بسسنی ممکن ناو ۱ - بفتح وار وسکونکاف؛مصفر\nباشد که در برابر واجب است . او امت - و لوعی از تیر باشد وآن '
=== leaf 194 '[pdf page 195]\nطوه -۹۱۱۲-\nوعبادت خالهٌ مجوی را کوبند ؛ ودراین زمان با | نالیدن وناله کردن هم\u200cهست *۱- وبمعنی\u200cخرامیدن\nيك واو لوستد مانند طاوی وکاوی . ورفتلری بنازهم آمده است۸ - وخم شدن ومانده\n\nناوه ۱ - '
رگس leaves [211]
```


## [2026-09-07T19:32:00.961Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\np=pages[211]\nprint('=== leaf 211 (printed 2129) ===')\nprint(p[:3000])\nEOF"
}
```


### [2026-09-07T19:32:02.218Z] TOOL RESULT

```
=== leaf 211 (printed 2129) ===
[pdf page 212]
-۱۳۹- برگی
پلنگه کوید ۱ وبعریی‌خجرالندو خوانند ۴ .هر فرگس نیم‌خواب - کنابه ازجعم
جراحت ی که ناسور شده باشد آبرا با آب بایند معشوق و محبوب است .
و بماش 0۱۱ پادگ ردو رهرزی که قددم انآ | افرگس وگل کنایه ازچنم وکوی
و ی
با خود دارد هیچ زن آزو بارنگیرد .۰ و زر مه ‎٩‏ بش رانم باعدکه
آی چا ات که عون عرش اند ۱ج با تفن کر موی کی ام
موی و ۳۳ | ویر مقف خانها نصب‌کنند - و برکی‌دانر نیز
نس ار موم :| کونند - وکنایه از ستاره‌های‌آسمانی امت ۷ -
ار ان ۹ - بح ول و تشدید و پروین را نی ز گفته‌اند - و زره ستف
ای کدابان ناهموار و درشت راگویند . ۳ 0
رگد ۴ « کدایان بیشرم و حراف چرخ کنایه از پروین باشد .
و زبردست راگویند . ذرگحی - بروزن مجلی ‏ جنسی از
فر گس * - بکسر کاف فارسی, کلی | جامه باشد که پوشند - و دوعی از طعام که
است معروف- وکنایه ازچشم معشوق هم هست. | خورند 3۸ .
() خم۱: آنرا بایند ویب بمالند ؛ چش : آنرا بآب بایند و بمالند .
() چش : نرکان ۰
۱ در : تروکه .۴ ار : تحفةً حکیم مومن : حجرالنمی.
۴ - جمع : نره (هم.) ۵ برکان .کدایان شوخ چشم پاشند . قربم‌الده رگفت :
آن که این شم نرکان گفته است زیر سیصد هزار تن خفته است.»
« لغت قرسی ی ۳۵۵ .
۴ - رك : نره لره. * - پهلوی 88738 « اونوالا۲ه » ازیونانی, 82۳19805
«ابا ص۸۱۸ معرب آن نرجسی.رك « دزی ج»ص۵ ۹۵ ۳ 8270188128 (لاتینی)
۳ 82۳61896 (فر ) ؛ رک ی کلی است ازتیره در کیها (11146653و۸702)
که در وسط کلش‌حلقه‌ای زرد دیده میشود » وآنرا درکن شهلا گویند. ودریضی
جنسها خو دگل لیز زرداست باگل سفید است ولی در وسط آن کلب کهای کوچك 1
سفید است » و آلرا نرکن مکی نکوبند « کل کلاب ص ۲۸۹ > :
بر فرق سر لرکس بر » زر دکلاه بر فرق سر چکاوه بك مشت گیاه .
منوچهری دامقانی ص ۰.۴۹۵۶
‎-٩‏ از : برکسی + ( پسوند سبت وشباهت ) ۳ برکك . رکسی
۷ - کرد ثرکی‌دا ن کردون بین هزاران ب رکه
مد رک ری ار بر
۸ - نام خورشی است که با تخم مرغ زده و پیاز خردکرده در روغن سرخ کرده میشود
وگاهی اسفناج هم ريخته میشودکه‌آنرا از جهت شبات اجزای وی بن رکس » بدرین‌ناممی نامتس
از پلو :
از رک پلو جون باد بود از نظم ترکسی دلشاد ‏
پحیی کاشی . رك : فرهنگه فظام.
```


## [2026-09-07T19:32:15.506Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in (168,169,170,193):\n    print('=== leaf',n,'printed',n+1+1917,'===')\n    print(pages[n][:1800])\n    print()\nEOF"
}
```


### [2026-09-07T19:32:18.042Z] TOOL RESULT

```
=== leaf 168 printed 2086 ===
[pdf page 169]
بلاببان -۲۰۸۹-
دراز دا و پپنا بعنی محل تیزی و درازی و است وغب تاريك .
پینی! .۲ ۸ نااوس ‎٩‏ بر وزن ناقوی , معید
تاانبای ۴ - بفتح همزه و بای ابجد ! ترسایان باشد - وآتشکده را نیز کوبند؛ وناووی
بال ف کشیده بروزن بادنجان » نی‌البان را کوبند | هم‌آمده اس ت که بجای همزه واو باشد.
وآن سازیت مشهور و معروف که نای‌البان هم ثاب ۱- بسکون بای ابجد » بسمتی‌لب
خوانندش ۷ ولباب وخالص وبی‌آمیزش وصاف و پاك و بیخش
نا ندیش ۴ - با دال ابجد بر وزن | باشد۷. - وناو راکویند عموماً و ناوی را که از
درویش » بممنی بدبپه باشد پمنی ظاهروروشن | فربهی بر کفل اسب و استر و امثال آن افتد
که احتیاج بفکر دارد چنانکه کوبند روزروشن | خصوصاً ۸ - ودرعربی چهاردندان .بیش (۱) سبع
() چش : پیش ۰
‎٩‏ بای , پسوندیت که برای ساختن اسم معتی(حاصل مصدر) بکاررود ویمعتی پوند
«ی» است . از نیز , نیزبا (نیزهای) * تیزی , از دراز » درازنا ( درازای ) ۳ درازی» از فراخ »
فراخنا ( فراخنای ) * فراخی » از تنگه » تنکنا ( تنگنای ) * تنگی - ۲ نیز ۷
۳ ازادات نفی‌وسلب است » اوستابی 38 ؛ هندی باستان 84 «اسشق ۱۰۱4 ور4:: دارمستتر.
تبعات ج ۱ص ۲۵۰ ؛کردی88 «زابا س ۶۱۳ ؛ وآن برای ترکیب صفات منفی » در اول اسم
و صفت درآید : ۷ امید » نابکار » ناخوب, ناچران » نابسود . ۳ بای اببان (هم.) <
بی‌آنبان ۰ ۴ - از دساتیر « فرهنکه دساتیر ص ۲۹۸ > 4- (عر ) ناووی >
ناژوی, خصوصاً بممتی دخمه و اطاقزیر زمینی اس ت که برای‌دفن میت بکار رود . جمع: نواویی.
حمزه اسفهاتی ( ‎2٩‏ ) کوید : « والفری لم تعرف القبور ؛ وانما کات نغیب الموتی فی‌الدهمات
والنواویس . > - قبن » آرامگاه ( مسیحیان ) . رك : دزی ج؟ س۷۳۷ . ( 2308 )۰ سربانی
۵ (نبی)[42 .2 .57 .1۵5 ,3۲0۵1222 رد: 621۲۵ 17۳۵ ,وهنطد110
و158 .0 1946 7167110۲4 ۷۷۵۲4۶۰ دعزع۸ ‎-٩‏ اوستا- 82870
زاز :8 ( برس کلممسبوق یدرف هصوت28) فی 8 (آب)] بممنی بدونآب » پرلوی 82
«.اسفق ۰۱۰۱۵ » ارمنی‌ع 2882026 (ناآميخته, خالس )۶ هوبشمان ۱*۱۰ » ورك : دارمستتر.
قبعات ج ۱ ۱۱۱ ۰۳*۹۰ ۷ - « ناب , خالص‌باشد بی‌غش . فرخی (سیستانی) کفت :
باب است 

=== leaf 169 printed 2087 ===
[pdf page 170]
سانه اطیولان
و هایم وچهاردندان بز رکه حبوانات باشد ۱ ناپنو؟ ۷ - بکسر ثاك وقتح بون وولو
وشتر پیو لزکار افتاده را نیز کوبند ‎٩‏ ۰ بالف کشیده, هرچیز را گوبن د که طایع شده باشد
ثاپای ۴ » با بای ابید بالف کشیده | و بکاری نیاید ۸ .
وییای حطی زده . بممنی محال باش د که درمقابل | ثاپود ‎٩‏ - بنم قالك وسکون واوو ال
ممکن است . ابجد . پمعتی معدوم باشد - و مقلس و پرشان
نا پروا ۴ - با بای فارسی وواو پروزن | شده را ای زگوبند .
پلبرجا » بمعنی‌سراسیمه - وبی‌فراغت - وبی‌طاقت نا پودهند *۱- بر وزن نامودمند ,
و بی‌آرام - وبی‌التفات - و بی‌تری و یم - و بی | ایمتی‌ساحب پریشانی واقلای که مقلس و پربشان
رغبت ومیل - وبی‌داش باشد . وققیر و بی‌ب رکه ونوا باشد. -
تابسود ؟ » بکر بای ابجد وسین نابهره ۱۱» بغتح ناك وسکون‌ها ورای
بی قطه بواوکشیده و بدال ابجد زده » هر چیز | بی‌ضطةٌ مفتوح . بمعتی بز رکه وعظیم باشد ۹۴
که آن لو باشد ودست زده ودست خورده نشده ‏ وفرومایه و دون وخسیس را نیز گوبند - وبمعنی
باشد 8 . تبهره نیزهت که زرقلب ناسره باشد۱۴- ویمعنی
نابسی ۱ - بنتح ثالك و سین بی قله | بوشیده وینهان هم‌آمدت است .
بتحتانی کشیده , بمعتی عدم باشد که در مقابل ناییوسان ۱۴ بنتم ناك و سای
وجود است . بواو رسیده و سین بی قطه بالف کشیده و بئون
۱ - ر4 : اقرب‌الموارد » محیطالمحیط - ۴ - از : ۷( فی )+ بای ( باستن)
از دساتیر « فرهنگه دساتیر ص ۰۲۹۸ ۴ - از : ۷( ی وسلب )+ پروا (ه.م.) +
« سراسیمه را باپروا کوبند. » « لفت فري ص 4 > ۴ - از :۷۰ (فی وسلب )+ بسود
( بسوده) * نابموده . رد : فپرست ولف +
* - دکر ایزدی هرچه بایست بود یکی سرخ باقوت بد نابود .
فردوسی طوسی « شاهنامهٌ بخ ج اس ۵۲۷ *.
٩-ظ‏ . پرساختهٌ فرقهٌ آذرکیوان . ۷ - از : ۷ (فی , سلب)۲+, ( حرف
اضافه )۳ نوا («م.)
۸ -کار مدد و کارکیا نابنوا شد زین یز بتر باشدشان نابنوایی +
: < منوچپری دامقالی ص ۸۳ >.
‎٩‏ - از : نا (فی » سلب )۳ بود ( یوده ) + *- از : نابود (هم.) ۳ مند
( پسوند اصاف ) . رشیدی هم‌آورده است . ظ. این ترکیب درست لیست .
۹۱ از : ۷ ( فی . سلب )۲ بهره (

=== leaf 170 printed 2088 ===
[pdf page 171]
فالراشیده ریت
زده » بمعنی چشم داغت وتوقع باشد - و بمعتی | آخای نقطه‌دار » تبرزین راکوبند وآن نوعی‌ازتبر
اگاه وغافل هم آمده است . است که سپاهیان بریهلوی زین‌اسب بندند؛ویتی
ناتر اشیده ۱ سکنایه از مردم درشت | کوبند سنانی‌است که سرآن‌دوشاخ باشد - ویزة
تاهموار و ناقبول و بی‌اسول و بی‌ادب باشد . کوچك را نی زکویند .
ناچار ۴ - با جیم فارسی بالف کشیدء ناجر مات ۴ - بنم جیم وسکون رای
وبرای می‌ضطة زده » نضیرلاید است پمنی چیزی | بی‌نقطه وفتح میم وکاف ساکن ۰ بمعشی دریشکده
که واجب ولازم بود ویی‌آن میسر نشود - وبتغانه شتن:باشد ؛ و بعی کوبند نام زاهدی
ناچخ ؟ < بفتح جیم فارسی و سکون است ترسا - ونام معبد ترمایان هم هست .3
<< یی
۱- از : ۷( فی . سلب )ل تراشیده ( آسم مفمول از « تراشیدن > ) +
۴ - از : با (نفی » سلب) ۳ چار ( چاره ) ؛ ناکزیر » قس : پهلوی 2287 « هنای سس
۶ از : 2 فی ۲ چار ] » کردی 237 - 88 ( بر خلاف میل » ناکزیر ) » ۵۵7- 86
( پسو ن كومك ) « ژابا س ۶۱۸ ۲ ۰ ۴ -قی : ساسکریت 3381028 ( مغرب »نابود
کننده , منتفل کننده ) « وبلیامز ۱:۵۳۸* : < و بودی که شیر ستیزه کارتر بودی , غلامان را
فرمودی (ممودغز لوی) تا درآهدندی و بشمشیر وناچخ پاره‌پارهکردندی .> « تارخ بیپقی مصحح
دکتر قیاض س ۱۲۹ > ۴ - خاقانی شروانی در قسیده مسیحاليهٌ خود کوید ( دبوان ص
که بفلط « بفراطیانم » ثبت شده ) :
من و ناجرمکی و دیر مخران در بفراطیانم جا و ملجا.
مینورسکی‌درشرح این بیت نوسد: ,۸۰۳017286808 204 ذُصفْوفْطکا ,0۲5 هذ۷.۸)
( .0.573 ,3 03۲ ,آ36 ۷۵1۰ .8505 در بارة 261 02۳از1 هیج تعبیری نکرده‌اند -
عقیدهة تین من آن بود که این کلمه را باید باجرمکی 12۳۳۵2161 - 0842 خواند و آنرا نام
یکی ازروحانیان سربانی منسوب به اسقف تشن مشهور باجرمق 182۳89 - 82 (شامل کر کوك
و فیره) داست . 88010 ۰ 84 ۰ موسی دی » یکی از سیزده تن‌آپای سربانی موب میشو دکه
در قرن پنجم با ششم مسیحی بگرجستان رفته اند » هرچند خود او از مر‌دم انطاکیه بود . برای
ترجمهٌ احوال او رك: ,060781685 8ز ۸160661005 4۰ ۵۸13086 016 ,۶02026
.516 .00 ,1928 ,6 زنط ه

=== leaf 193 printed 2111 ===
[pdf page 194]
-۹۱۱۱- : ناروی
باشد .3 بجای نون بای حهای نیز بنظرآه«ده است .
ناور ۱ - بر وزن خاور» بسسنی ممکن ناو ۱ - بفتح وار وسکونکاف؛مصفر
باشد که در برابر واجب است . او امت - و لوعی از تیر باشد وآن تیری امت
ناوران ؟ - بر وزن خاوران (۱) ۰ ی و بستی کویندا تیاس چوبین ومیان
کنات راکویند که جمم ناور باشد که بر | خالی که‌تیرتاوه را درمیان‌آن گذاشته می‌اندازند؛
همکن است ‏ و بع ی کویند ناوی باشد از آهن که تی رکوچکی
۰ ۳ درآن نهند و بهد ازآن در کمان گذاشته اندازند
ناورد « بفتح ثالك وسکون را ودال - 2 ‌
1 - و آلتی که از آن کندم و جو درکلوی آسبا
نقطه . جنگه وجدال وپیکاررا گونند- و بمعن, ۹
ی 7 24 8 بحعی .۷ ۸4 همان مشت | [ ۳
آمده ات ۴ ریزد ۴ - و <چوی یاف پشت ادمیرا نیز
رفتار هم مده است ۲ .
ناورد ۱۴ نکه کا کوندی
بمع اه امت ۳
ود5 ۱ - ببعنی + ناولد سحری (۲) -کنایه از دعای
چه:تاورد بمعنی جنگ و گاه بمعنی جا و مقام :
داشد - بد ونفرین باشد که درآخرهای شب‌کنند .
8 :۰ << ناه لک و امه ام ۶
ناو رف ر تقاش* - بسنی‌مسکن‌الوجود ناو ك قلوی «کنابه ازآء ته‌دلی باشد
است چه لاور بمعنی همکن و فرتاش وجود را - و هجو را نی زگویند که در مقابل مدح است.
آگوبند .3۴ ناو ناو ان * - با نون و وا دیگر
ناوسند * بروزن و معنی ایند است. | بروزن پادشاهان؛ بمعنی‌خرآمان وگرازان وجلوه
چه درفارسی با و واویهم تبدیل‌می‌بابند - ویممنی [ کنان باشد ۰
ضعیف ترکیب و لاغرهم کفته‌اند ؛ وباین معنی ناووس *۰۱ بروزن نافوی . آتشکده
() چش : خاروان . () خم۳ : سحر ؛ چش : صحری !
۱- برساختهٌ دساتیر * فرهنگه دساتیر س۲۹۹ ۲ ۴ - رك : ناور » وخ ۰۱
۴ نورد (خ.م.) * نبرد(ه.م.) ؛ معرب‌آن هم * ناورد » « دزی اج اس ۹۳۲ :
با بنده چه کینه است کردون را با پشه عقاب را چه ناورد است ؟
خاقانی شروانی « فرهنگه نظام > .
۴ - فرمود به‌پیر کای جواتمرد زین بیش هرا نماند ناورد -
نظامی کنجوی «کنجینه س ۰۹۱۵۳
8 - برساختهٌ دساثیر ۶ فرهنگه دسانیر س ۰.۴۲۹۹ ‎٩‏ از : ناو (ه.م.) ۳۲ که
(صفیر, نیت وشباهت) * اوه (ه.م.) ‏ ۷ ۳ ناو (.م.) ۸ رد4 :ح ۸ صفحه قبل .
‎٩‏ - از : ناو ( رك : ناو
```


## [2026-09-07T19:32:39.151Z] TOOL CALL #30: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2086 --image 2>&1 | tail -40"
}
```


## [2026-09-07T19:32:40.407Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o -n \"ناووس[^ ]*\" MON_part1.txt MON_part2.txt 2>/dev/null | head -20; echo \"=== part2 grep ===\"; grep -c \"ناووس\" MON_part1.txt MON_part2.txt"
}
```


### [2026-09-07T19:32:46.813Z] TOOL RESULT

```
REF: BQT:2086  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 169  OCR-lang: fas

بیان -۰۸۹-
دراز دا و پپنا بعنی محل تیزی و درازی و | است وشب تاريك .
پینی۹ ۴۰ 4 نااوس 48 بر وزن ناقوی ., معید
ناانبان ۴ - بفتح همزه و بای ایجد | ترسابان باشد - وآنشکده را نیز کویند؛ وناووی
بالف کشیده بروزن بادنجان » نی‌البان را کوبند هم‌آمده است که بجای همزه واو باشد.
وآن سازست مشهور و معروف که نای‌انبان هم ثاب ‎-٩‏ بسکون بای ایجد » بمعتی‌لب
خوانندی . ولباب وخالص وبی‌آمیزش وصاف و پاك و بیغش
نا! ندیش ی با دال ابجد بر وزن ‏ باشد۷. - وناو راگویند عموماً و ناوی را که از
#ا دروش » بمعنی بدیهه باشد یعنی ظاهروروشن | فرجهی بر کفل اسب و استر و امثال آن افتد
که احتیاج بفکر سارد چنانکه گوبند روزروشن خصوصاً ۸- ودرعربی چهاردندان .یش (۱) سبع
() چش : پیش .
‎٩‏ بای » پوندیت که برای ساختن اسم معتی(حاصل مصدر) بکاررود وبمعتی پسوند
«ی» است . از تیز » نیزبا (نیزای) ** تیزی , از دراز » درازنا ( درازای ) * درازی, از فراخ »
فراخنا ( فراخنای ) * فراخی » از تنشگه » تنکنا ( تنکنای ) *تنگی . ۲ نیز 2۷۶
۳ آزادات نفی‌وسلب است » اوستابی 28 ؛ هندی باستان 84 «اسشق ۱۰۱۶ ور4:: دارمستتر.
تتبعات ج اس ۲۵۰ ؛کردی88 «ژابا س 4۱۳ ؛ وآن برای تر کیب صفات منفی » در اول اسم
و صفت درآید : با امید » نایکار » ناخوبء ناچران » نابود . ۳ بای اببان (ه.م.)-
بی‌انبان .۰ ۴ - از دساثیر « فرهنگه دساتیر ص ۲۹۸ *. 5- (عر ) ناوون -
باژوی, خصوصاً بمعنی دخمه و اطاق‌زیر زمینی است که برای‌دفن میت بکار رود . جمع: نواویس.
حمزه اصفهانی ( ‎2٩‏ ) کوید : « والفری لم تعرف القبور » وانما کات تغیب الموتی فی‌الدغمات
والئواویس . » - قبر » آرامگاه ( مسیحیان ) . رك : دزی ج؟ ص۷۳۷ . ( 3208 )۰ سر‌بانی
2۵4۵ (قبر)[ 42 .2 .57 1۵2۰ ,3۲00610222 رد: لد۲ا ۲00 1۳۷۵ ,قصقنط22ه11
46 ,158 .0 (۱1946 1767110۲۵ ۷۷۵۲45۰ دهزع۸ ‎٩‏ - اوستا - 82870
[از :8 ( برس رکلمدمسبوق ,حرف مصوت 28) نفی 8-۳ (آب)] بمعنی بدون‌آب » پهلوی 820
«.اسشق ۱۰۱۵ > » ارمنی‌ع 288026 (0اآمیخته,. خالس )« هوبشمانه۱۰۱ > ورك : دارمستتر.
تبعات چ ۱ ۱۱۱ ۰۳*۹۰ ۷ - « ناب , خالص‌باشد بی‌غش - فرخی (سیستانی) گفت :
باب است هرآن چیز که آلوده لباشد زین روی تراکویم کازاده ای .»
« لغت فری ص ۲۳ ۶
۴- رشیدی کوید : «کوی (کودیی) که بر کنل‌اسب می‌افند از فربهی. > و مقصود وی
آدت که در میان دوکفل فربه اسپ کودیی پشکل ناو (کشتی ) پیدا میشود که بدان ناب (مبدل
قاو ) گوبند » اما شاهد نیاورده » شاید درعسر رشیدی که ملمانان هند در فارسی حرف میزدند
چنان اسطلاحی بوده. سرا جکوید : « خطی‌را که میان‌شمشیر باشد در طول » درهندوستان «ناب»
کوبند و ظاهراً آهم فارسی است » لیکن در اشمار استادان دیده نشده . > «فرهنکه نظام».
۵ لا اموا - پشم سوم » از: ا ( سلب )۳+ امید (هم.) ۳ نومید (هم.) ۳ نمید (هم.)
پهلوی 2۳8123861 ( تلف : +280128). فارسی جدید 8217361 ( ۶ افقانی ع 14 ))
شکل‌جدیدی است از: 28 و 12846 . قی 32173860 (فردوسی 1 :20۱۳۳ *۲) « هوبشمان
۴۳ و رك : اسشق ۳ آییی امید بدارد »کی که رجا ندارد » مأیون ۰
```


### [2026-09-07T19:32:46.890Z] TOOL RESULT

```
MON_part2.txt:54548:ناووس»
MON_part2.txt:73635:ناووس:
=== part2 grep ===
MON_part2.txt:2
MON_part1.txt:0
```


## [2026-09-07T19:33:04.019Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '54540,54556p' MON_part2.txt; echo \"======\"; sed -n '73625,73645p' MON_part2.txt"
}
```


### [2026-09-07T19:33:04.084Z] TOOL RESULT

```
دول. میه‌ای که باز بر آن نشیند و زنجیری 
دارد که بای باز را بدان بندند. 

مرور: 0۳0۲« (ع.] (مصل.) رفتن؛ گذشتن. 
مطالعةً سریع کتاب و رساله. مرور ایام 
مان کشت ری کاو: 

مرورنه. (می‌دجمتسنهد [قنن. مرغرن ] (1.) 
ناووس» مقبره ( کافران). 

مر وسند ه. (۵-)۱0۲۱5-2۸002 (افا.) عادت 

کننده به چیزی. 

مروف: ]12210 [ع.] (امف.) صاف کزده 


======
دسته کسه » تیپ دربایی (فره.) 

ناوناوان: ۱2۷-03۷-0 (ق. حال) خرامان» 
گرازان. 

ناوند: 25-20 [- نان‌وند - نان‌ند] (امر.) 
بالشچه‌ای که خمیر پهن کرده بر آن نهند و 
بر دیوار تنور تافته چسانند تانان بپزد؛ 
رفنده؛ نانند. 

ناووس: 5 [- ناوس - او وس؛ معر. 
قر؛ بو.] (.) اطاق زبر زمینی که برای دفن 
میت بکار برند؛ دخمه. قبر هر فرد غیر 
مسلمان» گور کافر. گورستان زردشتیان» 
قبرستان مجوس. 

ناوه: (-)۱2۷-2 [- ناوک ] (.) ناو خرد. 
نوعی تیر. ناوی که از آن گندم و جو از دول 
به گلوی آسیا ریزند. شیاری که در پشت 
آدمی است. شباری که در دانةٌ گندم و هستة
```


## [2026-09-07T19:33:04.308Z] TOOL CALL #33: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/ | tail -20"
}
```


### [2026-09-07T19:33:04.351Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb    3114 Sep  6 11:25 2417.txt
-rw-rw-r--  1 sfmqrb sfmqrb     561 Sep  6 11:25 2417.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  161891 Sep  6 11:16 2420.png
-rw-rw-r--  1 sfmqrb sfmqrb    3629 Sep  6 11:16 2420.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2009 Sep  6 11:17 2420.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  153589 Sep  5 16:27 2427.png
-rw-rw-r--  1 sfmqrb sfmqrb    3424 Sep  5 16:27 2427.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1757 Sep  5 16:28 2427.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    2615 Sep  4 15:28 31.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  512022 Sep  5 16:12 333.png
-rw-rw-r--  1 sfmqrb sfmqrb    1339 Sep  5 16:12 333.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1508 Sep  4 15:27 58.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1931 Sep  4 15:02 70.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1606 Sep  4 14:54 72.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  669351 Sep  5 01:38 733.png
-rw-rw-r--  1 sfmqrb sfmqrb    1152 Sep  5 01:39 733.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  726576 Sep  6 18:36 829.png
-rw-rw-r--  1 sfmqrb sfmqrb     981 Sep  6 18:36 829.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  624515 Sep  5 16:20 902.png
-rw-rw-r--  1 sfmqrb sfmqrb    1658 Sep  5 16:20 902.vision.txt
```


## [2026-09-07T19:33:14.481Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ('MON_part1.txt','MON_part2.txt'):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    print(f,'len',len(t),'pages(\\\\f)',t.count('\\f'))\n    nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$',t)\n    print(' standalone nums sample',nums[:10], nums[-10:] if nums else '')\nEOF"
}
```


### [2026-09-07T19:33:15.862Z] TOOL RESULT

```
MON_part1.txt len 2611770 pages(\f) 0
 standalone nums sample ['۱۳۲۷', '۱۳۳۳', '۱۰۳', '۱۰۷', '۱۰۹', '۱۱۰', '۱۲۱۱', '۱۱۴', '۱۲۱۸', '۱۲۱'] ['۹۷۹', '1۹۳', '٩٩۴', '۹۹۹', '۱۰۳', '۱۰۰', '۱۰۲', '۱۳۹۳', '۱۱۰۰', '۱۱۰۲']
MON_part2.txt len 2568024 pages(\f) 0
 standalone nums sample ['۱۳۸۱', '۱۱۰۹', '۱۱۵', '۱۱۳', '۱۱۰', '۱۱۵', '۱۱۴', '۱۱۵', '۳۳۹۲', '۱۱۵'] ['۳۰۷۸', '۳۰۸۹', '۳۱۱', '۳۱۹', '۲۳۱۷', '۳۱۳۷', '۳۲۱۱', '۳۱۳', '۱۱۴', '۲۱۹']
```


## [2026-09-07T19:34:21.945Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD (s)ner ===\"; grep -n -i \"^ *(s)ner\\|^ *ner-1\\|^ *nes-1\\|^ *nes-\\|snerk\\|nazjan\\|nestam\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T19:34:21.990Z] TOOL RESULT

```
=== AHD (s)ner ===
783:nes-'. To return safely home. 1. Germanic *nes-tam in Old English, Old High German (in composition), and Old Norse nest, food for a journey, akin to the possible Germanic source of Old French harnes, harness: HAR- NESS. 2. Suffixed o-grade form *nos-to- in Greek nostos, a return home: NosTatcla. [Pok. nes- 766.]
784:nes-2, Oblique cases of the personal pronoun of the first person plural. For the nominative see we-. 1. Zero-grade form *ns- in Germanic *uns in Old English ds, us (accu- sative): Us. 2. Suffixed (possessive) zero-grade form *ns-ero- in Germanic *unsara- in Old English dser, ire, our: OUR, OURS. 3. O-grade form *nos-, with suffixed (possessive) form *nos-t(e)ro-, in Latin nds, we, and noster, our: NOSTRUM; PATERNOSTER. [Pok. 3. ne- 758.] nétr-. Snake. Germanic *néthré- in Old English nédre, snake: ADDER. [Pok. né-tr- 767.]
975:(s)ner-. To wind, twist. 1. Suffixed extended zero-grade form *snork- in Germanic *snarh-6n- in: a. Old Norse snara, cord, noose, trap: SNARE}; b. Dutch snaar, string: SNARE?. 2. Proposed by some as a derivative of this root is Germanic *narwa- in Old English nearu, narrow: NARROW. 3. Extended variant form *(s)nark- in Greek narké, cramp, numbness: NARCO-, NARCOSIS, NARCOTIC. [Pok. 2. (s)ner- 975.] sneubh-. To marry. 1. Latin niibere, to marry, take a husband: NUBILE, NUPTIAL; CONNUBIAL. 2. Possibly nasalized zero-grade form *nu-m-bh- in Greek numphé, nymph, bride: NYMPH. [Pok. sneubh- 977.]
```


## [2026-09-07T19:34:22.426Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD nargis ===\"; grep -n -i \"nargis\\|narkis\\|nrgs\" PHD.txt PHD_mackenzie.txt | head; echo \"=== NYB ===\"; grep -n -i \"nargis\\|narkis\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-07T19:34:22.484Z] TOOL RESULT

```
=== PHD nargis ===
PHD.txt:499:nar [ZKL < A shr; nl | M nr, N ~] male, manly. nargis [nlgs | N ~] narcissus.
PHD.txt:2888:narcissus nargis.
PHD.txt:5171:walg wiréxtan wars nargis wircg wircz-! wirēxtan! wircz- waranigih waranig wurróyisn waran
PHD_mackenzie.txt:7127:more fray, freh, wes.                          narcissus nargis.
PHD_mackenzie.txt:10086:nargis                    ~,         nigcz-
=== NYB ===
```


## [2026-09-07T19:34:47.420Z] TOOL CALL #37: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 362 -l 362 -r 400 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg362hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg362hi.png'); print(im.size)\nw,h=im.size\n# Germanic snarwa box: approx x 0.22-0.36, y 0.30-0.36 of page  (from 1700x2200 view: x 360-560, y 690-780 of 2200 -> frac)\nim.crop((int(0.20*w),int(0.305*h),int(0.42*w),int(0.365*h))).resize((int(0.22*w*2),int(0.06*h*2))).save('$S/p362_germ1.png')\n# Germanic nas-ja box: y approx 1355-1400/2200 -> 0.615-0.645\nim.crop((int(0.18*w),int(0.598*h),int(0.42*w),int(0.645*h))).resize((int(0.24*w*2),int(0.047*h*2))).save('$S/p362_germ2.png')\n\""
}
```


### [2026-09-07T19:34:50.312Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-07T19:34:53.166Z] TOOL CALL #38: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p362_germ1.png"
}
```


### [2026-09-07T19:34:53.183Z] TOOL RESULT

```

```


## [2026-09-07T19:34:59.196Z] TOOL CALL #39: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg362hi.png'); w,h=im.size\nim.crop((int(0.20*w),int(0.345*h),int(0.40*w),int(0.395*h))).save('$S/p362_germ1.png')\nim.crop((int(0.18*w),int(0.665*h),int(0.40*w),int(0.700*h))).save('$S/p362_germ2.png')\n\""
}
```


### [2026-09-07T19:35:00.707Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T19:35:04.277Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p362_germ1.png"
}
```


### [2026-09-07T19:35:04.290Z] TOOL RESULT

```

```


## [2026-09-07T19:35:04.604Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p362_germ2.png"
}
```


### [2026-09-07T19:35:04.616Z] TOOL RESULT

```

```


## [2026-09-07T19:35:24.015Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT asta ===\"; grep -n \"asta-\" BRT.txt | head -20; echo; echo \"=== BRT Heimat ===\"; grep -n \"Heimat\" BRT.txt | head -10"
}
```


### [2026-09-07T19:35:24.088Z] TOOL RESULT

```
=== BRT asta ===
2552:direkte Rede  oder  Zitat;  a)  adjektivisch:  kochersoll  man  niederschlagen,  den  Kessel usia  ahmni  (usw.,  Y.4J-I)  ■  ■  ciit  °taya  sollen  sie  .  .,  den  Aufbau  ,  ."  V,(V.73f.; paiti.vaca paityümraoti  Y,2/,4;  ■ —  kini  zl  — ■  "//  jrVr.ji./  y^aratu  °i^  vasträ  i-iiv än4  (usw.,  Y.4Ö.6)  .,  'te  zT  väcö  ..  mazdä  katu  V.J.  19;  —  asta-ja  hz  'te  mazäayasna frii mrao tY.yi.i^t-jy. 4.  i^üZ.;- — arrum'a  °t»m  iristam  nidanzaym  "da  sollen  (sie) „afrJnSmi  ..'tarn  mq^nm  fradaisayöH ..  die  J/l  (ihn)  den  Toten  .,"  V.  6'.46;_;.  18, Yti4-46;  benutzt  Y'l4-9.  b)  substan-  5.13,  14,  41,  61,  6.7,  51'.  7-i2i  t''-S,  10, tivisch,  in  Kongruenz  mit  dem  Praedikat:  9.39',  '4-7,  iö-z,  12,  A.3.^  falsVok.?); am?mca  .,  Sfrlnämi  ..  'taSca  tivlcö  yöi  —  'tanhqm  astqmca  var»sqm:a  .,\.h;-; ".  .  und  das  sind  die  Worte,  die  .  ."  Yl  —  'te  ratavö  .  .  'ta£sqm  ra>wam  'S.i'o 14-46'.  1)    vorausweisend    (öfters   -82;  Vd.  2;    —    'ts  ja'iä  V.A16-22S;
2745:•  j.  aesmö.zasta-  Adj.  'Brennholz  in  der  Dat  'etwas  (Akk.)  haben  wollen,  begehren, Hand  haltend,  mit  Brennholz  in  der  Hand' :  erstreben  für  -':  yö  . .  tanuye  tsaite  >rä- yas3  ^WJ  .  .  frayazaite  "stö  Y.62.1;  V.  ^r^m  V.  ij,  19;  —  ä'irava  .  .  manmtam 3.1.  isimtiö  dalnayäi   am^m   iamnö  tanuye
3117:Superl.  aus  ^afryö.maii-masla-  Adj.,  durch  Ha- plol-,  lu  S  J0<^.  —  *maiay-  m,  'Brunst',  lum V.  mad.;  vgl.  ai.  mäda-  m.;  —  "masta-  PPfP. lum  V.  mad.  (sd.).  —  Pü.:  kÜ  an  i  mast ir/ryat  masilh.  —  i)  Bei  DsT.  in  drei  Wörter zerrissen.    S.  auch  Js.  Cama  Mem.  Val.  131.
3177:•  j.  a-]asta-  Adj.  'ungebeten'  sva,  'uner- wünscht, verhasst';  pailistälie  °taca  zöiz- distaöj  . .  xrafsira  Yt.  11.  i.
4374:•  j.  an-aäa-  Adj.  'nicht  gemahlen',  vom Getreide:  aiiaval  asanqm  {yavattqtn)  asta- vat  'ianam  V.  7.35,
4867:ayanho-zasta-
4868:•  j.  ayanhö.zasta-  Adj.  'mit  nietallenen (eisernen)  Klauen';  varäzahe  ('eines Ebers'; ayüahs^äiahe  'saslahe  Yt.  ro.  70.
5069:Zum  V.  Aä(j')-.    —    ai.  az-asana-   n.  'Zuende- Vd.  2.  gehen'.  —  Vgl.  'sasta-  und  Gdn.  BB.  15. 254.
5250:•  j.  avi.spasta-  Adj.,  PPfP.:  s.  's/as-.
5769:'asta-  2 1 1
5785:j.  'asta-  n.  'Heim,  Heimstätte':  *'tjm^'' ii^ra  fracarsnta pasvas^a  staoräca  masyäca "ein  Heim  schafften  sich  da  Kleinvieh  und Grossvieh  und  Menschen"  V.  2. 1 3.  a)  ins- bes,  von  der  Lagerstätte  der  Hunde:  duye nai^aiti  "tanqm  aiäityS.ai^Aarpi^ra/tqm  däi- tim  akmaiät  hanirsm  i:)r)nuyat"7.\<ie.\taa\ neuniig  nicht  gehörig  gepöegte  (Hunde) lagerstättcn  -  die  gehörige  Pflege  soll  er dafür  beschaffen"  V. /4.17.
5790:faiiä.hasta-.  —  J)  Die  ZerreiEsung  findet  ihre Erklärung  durch  V.  g.  48,  wo  riehtig;  yi&a fata  ahmSj  as;  Aä, .  ,
5791:•  j.  'asta-  Adj.  (fem.  'iä-),  PPfP.:  s.  'aA-. KompE.
6305:•  j.  aäavasta-  n.  'Besitz,  Erwerb  des (höchsten)  Anrechts':^»  "^wä yäsämahi havauhum  't*m?a  haosravaahftn  Imru- mauii  Yt  10.33;  —  yüimäkim  yasnäica paimaUa  yal  am3sanam  spmtanqm  a/imä- ifM    hmHiauhäica    °täica  yal  taosyantqm
6799:Ny.4.8;  —  srHvayamnat p<^*ti  'n'U  vatr-  „«„ds.  A««,af;  %.  aber  PQ.  -^)  In  Z«™- aHi/z-ü.  —  3>  ra.  hat  zu  oj^ömaiiilh  u  ra!d- maHilih  dieErl.:  lin  meiiük  *it  j^aläi  ii  äasta-Bar därcnd  pa  täs  i  H  "der  Geist,  auf  dessen Weg  man  den  Herrn  und  Lehrer  besitzt"; sie  sieht  also  in  ahumanl-  ralumanf-  eine Gottheit.  —  *)  NA.  aküm^-a  ruiüm^a,  aber gegen  K  7  a,  b  und  Pu.
6980:•  j.  a-x*asta-  Adj.  *nicht  gedroschen':  *!i  stllY.43.z\ — yakmya  3p5..^waxs3iite altavat  ifastaiiqm  (sd.)  aSavat  'tanqm  *3  iskafymT^  pouruttm^a  Yt/O.  14;  — {yavanqm)  V.  7,35.  paityaogit  (sd.)  ta  akmai  jassit . .  iaurSui
6984:•  j.  a-x^'asta-  Adj.  'ungekocht':  rattt/rif  a/araa^m  vahistfin  ä  ahüm  äbaraiti'2.24-, *paySbti  x^ästaii  'faisca  N.  57.  —  «3'?'«  (sd-)  '^  yatumanahe  j'asaiti  Y.  S.
7213:•  j.  a-x'asta-  Adj.  "nicht  gedroschen': agtavai  i^astanam  (sd.)  aSavat  "tanain {yavanqm)  ¥.7.35.
7217:•  j.  a-x'asta-  Adj,  "ungekocht':  ralu/ris
8546:•  ].,  g.  ustäna-zasta-  Adj.  'mit  (zum Gebet,  zur  Bitte)  ausgestreckten  Händen';

=== BRT Heimat ===
6365:•  j.  aSä-yaona-  Adj.  'wo  die  Heimat  des A.  ist' :  garS  nmätum . .  ravSAu  -n^m  Yt_j.  4.
9599:•)  Vgl.  Stein  IA.  15.  21.  Er  liegt  nach  Bd. /J,  16  pa  saiasIStt  'in  SaisiJn'.  —  •')  Aus  dem An'ischen  Königshaus,  als  dessen  Heimat  das Gebiet  des  A:-Sees  gilt,  Bd.  31.  7.  —  ••*)  Im See  K.  ruht,  von  gg^jgg /ra&awy  bewacht,  der Same  des  Zara%uitra,  aus  dem  dereinst  die Saoiyanl  entstehen  sollen,   vßl.  unter  xsudru-'i. ,
13812:*>   Vgl.    Bd.  74-  19:    J'^a^   (in    Aw.-Buchst.) i/  xärpuSt   (=  np.  xStpasi  'Igel')  i^änend',    lg. £Ü    gilt    der    Igel    als    .ipezi elter   Gegner    der Ameisen ;  iäiak  fa  AamislJriA  1  mör  i  i/änai  t:s da    eslel,    H^ön   xdwet   ku    iälai    Aar  *iärak  *i  1 andar  mar  xSHoi  i  mizet  (ü)  lOCO  mar  iaHft. KorapA.   —   Et.?    Vgl.    HORN   KZ.  J^.  437, 1 HBM.AGT.AI4l.VI!.Va/+»fl*fl.'derRch]imme Haken  (Stacheln)  hat'7  -  mp.  (Pü.):  iüSal;  np.  I £uia;  A3;similation  der  silbenanl.  Kons. ■  j.  duzakö.sayana-  Adj.  'wo  der  Auf- enthalt, dieHeimat  desIgels  isf :  i'alk^ntim (sd)  yim  -mm  V,  /.  9.
17822:sae^antätvirshraynaiY.  26. 10; — gSuicä hudätahs  gayehyäcä  mard^nB  .  .  °itm  Y. y-  7;  2j.  a,  26.  S,  Yt  13.  87;  —  «ÄM^ zar^uStrahe  ipitämahe  asaons  -sie  Y.  6S. 22;  3. 2,  4. 23, 16. 2,  23. 2,  24-  S,  7'-  2-  Vr. /ö,  2,  YtÄ  2,  J_J.  87,  Vd.(?;  —  ahe  nars aSaonS  'Jtm  yazamaide  yS  asmffj^ativä nqma  Yt,  /. 30;  13. 95 ff.  (oft),  Y. 23. 2, 26. 5% FrW.  2. 1,  3;  —  hvSuyä  asaonyä  'sim  Yt ''5-^39!  '39f-'*;  —  kanyä  *va}>uis  asaonya [. .]  °slm  Yt  13.  141 ;  141  f.'°;  —  auch  dem AÄM.  und  andern  Gottheiten  wird  eine Fr.  KUgeschrieben**':  vispanqmca  anAqm paoiryanqm  'Sinqm  .  .  °sm  avqm  yqm ahurahe  masda  .  .  °iay5  .  .  ya  ampsanqm spintanqm  .  .  yqmca  ährö  urväzistake  .  . yqmca  sraohhe..yqmca  alnSyqmca  apH.. YtJ^.  80-86;  Y.26.2i.,  V./»?.'4; — äyese yelti  *ä  *fravaM<y)'^  ahurahe  mazdä  am»- sanqm  sparUanqm  . .  Y.  25. 2 ;  —  gaom  (statt Gen.)  agvJS-dätahe  urunB  °Sim  S.2.  I2;i2; —  sogar  den  Fravalay  selber  (!) :  aSäunqm "sinqm  uyranqm  .  .  paoiryjJkaisanqm  'si- nqrrt  nabänazdistanqm  'ünqm  '/ayU  xihaiä ayantu  ahmya  nmaneYt.i3.1s6.  A)/ra- vaHnqm  a)  (näral,  mä)  heisst  der  i .  Monat  im Jahr^:  asäunqm  'sinqmY.i. 11.  ß)(näml, ayar?)  heisst  der  19,  Monatstag:  asäunam 'sinam  uyranam  S.j.  19;  vgl. 2. 19,  Y.10.5. •)*Nach  dem  GrBd.  (s,  DsT.  ZA.  3.  500, Blocket  RHR.J2. 104)  ist  der  Mensch  aus  fünf Bestandteilen lusammengesetit:  ian,yän,  nmän, äiinai  aad /ravakr.  Vom  letzten  heisst  es; y>ti- vahr  an  i  pcs  i  Öhrmazd  i  :^aiäl,  und  über  sein Verhältnis  mm  fiß/ö»  wird  geiagt:  ruvän  S/ra. vakr  pativast,  ku  iän  rm/ä»  marnjcmtan  ne  tiniän. S.  noch  DkB.  269  {218.  6):  io  (fravahr)  haf  lan yut  bavtt  lan  hil  lör  u  aiär  mänri.  Die  Schaffung der  fr.  (bei  West;  "prolotypes,  primary  ideas of  the  good  creations")  ist  nach  Bd.  /.  8, 34.  1 zu  Beginn  des  ersten  Mitleniums  erfolgt;  nach 2.  10  f.  entscheiden  sie  sich,  'lan  tariaiihä'  gegen die  Welt  der  Driig  zu  liämpfen.  Über  ihre,  ins- besondere  kiiegeiischeTäligkeitalsSchutzgeister und  Manen  gibt  das  ihnen  gewidmete  Yt  13 Auskunft.  Ihre  Zahl  wird  Yt.  13.  59  ff.  auf  99  999 eingegeben,  vgl.  jcludra-*)  and  Mx.  4g.  16,  52. 23,  29;  weniger  bestimmt  Yt.  13.  64,  66.  All- jährlich während  der  letzten  fünf  Tage  der sechsten  (letzten)  Jahreszeit  und  der  sich  an- schliessenden fünf  Schalttage  kommen  dieManen, ihre  frühere  Heimat  zu  besuchen  (Yt.  13.  49) und  werden  dann  besonders  gefeiert  (s.  hantas- pa%niae<iaya-)ii).  Vgl.  noch  Cld.  Totenverehrung 48,  BahadoorN.  D.  Khandalawala  Cama  Mem. Vol'  205,  JN.  GIrPh.  2.  643,  SÖDEftBLOM  RHR. 3g.  229,  373,  La  vie  future  7.  Das  Nichtauf- treten  der  fr.  in  den  (eig.)  Gä%äs  (s.  unten  No.  l) ist   bemerkenswert;    zum  Teil   aber   entspricht
20985:Stätte,  Heimat"*  (nur  Komp.).  erregen':    xsttütaheHt   a^itähe   .  .  mand
27827:*>  Ich  halte  es  fär  sicher,  dut  Zart&uSira eine  geichichtlicbe  PersöoUcbkeiE  ist,  sowie  dass die  Gä%äs  im  wesentlichen  auf  ihn  lurückgehen. TiELB  GeschRelAIt.'  3.  275  CTklärt  mit  Recht den  Zar.  des  jüngeren  Awesla  (ül  "eine  vSIlig mflhische  Person",  aber  dnss  er  «chon  in  den Gä%äs  "eine  legendarischc  Penon"  sei,  mnss ich  ihm  bestreiten.  Ich  finde  vielmehr,  dass er  uns  hier  darcba,as  körperlich  nnd  meaichlich entgegenicitt.  Sein  Reformationswcrli  ist  noch in  den  ersten  Anlangen  begriffen.  Nur  ent wenige  einflussreiche  Männer  sind  dafür  ge- wonnen, nm  es  aU  Soosyanl  {lA.)  zu  nnterstütien : SD  ausser  dem  Sohn  Iial.väslra{i.  lara^tütray- a) nnd  dem  Vitersbruder /ftiiyöt.m^wAa  inibeson- dere der  Fürst  yäiäipa,  sodann  Jämäiftt,  dessen Minister,  und  Fralaoslra,  deren  beider  Interesse durch  Knüpfung  verwandtschaftlicher  Bande  ge- festigt, wird  -  Zar,  beiratet  Frai.z  Tochter  und gibt  Jim.  seine  jüngste  Tochter  ßimraaslä lar  Ehe  -,  femer  der  TKrer  Fryäna-  (s.  Ntr.}. Auf  der  andern  Seite  setzen  die  den  alten Göttern  iäana-)  wie  Mi^ra,  Haoma  usw.  und ihrem  Kult  treu  bleibenden  Fürsten  {kaii)^-, säslar-)  nnd  Priesler-Lehrer  [kivapan;  uäg-')  wie Bindva,  Grlhma  dem  Neuerer  heftigen  Wider- sland entgegen,  lo  dass  er  häufig  genug  in  bittere Klagen  Bosbrieht  und  der  Besorgnis  Ausdruck gibt,  ob  er  seine  Mission  werde  fortfuhren  können (vgl.  iB.  Y.  46.  i).  Beieichnend  ßr  die  ■Wirk- lichkeit der  Verhältnisse,  unter  denen  die  (7ü^s entstanden  sind,  ist  die  Strophe  Y.Jf.  iz.  Haite ich  sonach  an  Zar.  als  historischer  Figur  durch- aus fest,  so  sehe  ich  doch  anderseits  jeden  Ver- such, die  Zeit  seines  Auftretens  genauer  zu  be- stimmen, für  aussichtslos  an.  Nach  der  heimischen Chronologie  (s.  West  SBE.  47.  xxvm)  würde Zar.%  Geburt  in  das  Jahr  660  v.  Chr.  fallen, und  Jh.  Zor.  174  hält  das  für  wesentlich treffend :  "the  period  . .  just  before  the  Achae- menian  power  [is]  the  approximate  date  of Zoroaster's  life".  Ich  glaube,  wir  werden  wesent- lich weiter  zurückzugreifen  haben,  und  urteile über  Jn.s  Ausführungen  wie  Tiele  GeschRelAlt.> 2.275,430.  Einer  Chronologie,  die  damit  rechnet, dass  ein  Lehrer  des  Glaubens,  der  als  erster 100  Schüler  um  sich  versammelte  (s.  ^sarna-\ 100  Jahre  nach  der  ersten  Verkündigung  der neuen  Lehre  geboren  wird  und  100  Jahre  att stirbt,  kann  ich  kein  Vertrauen  schenken.  S.  auch No.  I  zu  vüläspa-.  —  Die  Angabe,  Zar.  sei  im Weslen  von  Irin  geboren  (s.  rayay-),  ist  mit  der Tatsache,  das«  alle  entscheidenden  Stellen  de* Awesta  (insbes.  Yt.  ig.  66  f.)  auf  Entstehung  im Osten,  in  der  Gegend  des  //äiniinsees  hinweisen, keineswegs  unvereinbar.  Es  lisst  sieb  sehr  wohl begreifen,  dass  der  Reformator  seine  Heimat verlies!,  weil  er  keinen  Anklang  fand,  oder  auch verlassen  musite.  So  mag  sich  auch  seine  starke Betonung  wirtschaftlicher  Giundsätie  (s.  väilrya-) erklären.  Der  Westen  Irans  stand  zweifellos auf  einer  wirtschaftlich  wesentlich  höheren  Stufe als  der  Osten,   wo  man  sich  noch  lange   nicht
27828:eut  vollen  Sesshaftigkelt  duicbgemngen  hatte ; und  es  musste  Zar.  darum  zu  tun  sein,  den Segen  der  geordneten  Verhältnisse  in  seiner Heimat  nach  der  Statte  seines  Wirkens  zn  ver- pflanzen. Dabei  ist  es  gani  gut  denkbar,  dass VStäipa  als  einsichtiger  Fürst  gerade  nm  dieser Beitiebnngen  willen  dem  landfremden  Prediger seine  besondere  Gunst  und,  Unterstützung  an- gewendet hat.  —  Vgl.  im  Übrigen  die  Mono- graphie Jackson  Zoroaster;  femer  JusTi  PrJ.Af. 244,  Oldenbekc  Deutsche  Rundschau  14.  40S, EdvLehmann  Zaralbnstta  z.  1  ff.
28393:•  j.  layana-  n.  'Wohnstätte,  Aufenthalt,!  P-  '^y^™  *<>-  f-  gemeint  Ut  hyiHm,  s. HeimatC  Sp.  .717  o.  No.  ..
28429:•  j.  söidrya-  Adj.  'was  zur  Heimstätte gehört,  heimatlich';  'rya  (APn.)  apasca ztmasca  urvarasla  yatamaide  "was  lur Heimat  gehört,  das  Wasser  und  die  Erde und  die  Bäume  . ."  Vr.  16. 3.
```


## [2026-09-07T19:35:25.157Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN nargis ===\"; grep -n -i \"narkis\\|nargis\\|Narcisse\\|Narzisse\" HRN.txt HUB.txt | head; echo \"=== IEC ===\"; grep -n \"^nes-\\|^snerk\\|^sner-\\|^narwa\\|^nosto\" IEC.txt | head"
}
```


### [2026-09-07T19:35:25.224Z] TOOL RESULT

```
=== HRN nargis ===
HUB.txt:8531:ceptaculum aquarum' =^ arm. parken ; Lehnwort nargis aus
HUB.txt:8532:*narkis — syr. Dpi3 = gr. vu^f/.iaoog u. s. w. ; — avingdn
=== IEC ===
11675:nes- (2) (nínés-) ‘turn, return, recover, thrive, succeed, proceed'. Cf. néio WP II, 334 Skt. nase, mp. “approach; join; deviate; go wrong’; Hitt. nesh- ‘turn’; Tokh. A nas-, B nes- "be: Gk. néomai, neümai, Ion. nisomai (return'; cf. also ko-néo ‘hurry, attend” ?); Go. ga-nisan, sv. 5 ‘survive’; MHG ge-nésen, OHG gi-nésan, wd OE nesan, id. Cpd. in Arm. (?) nah-angem, v. ‘turn, divert, thwart' beside nahang, gs: -i, abs: -av ‘region’. Cf. also Gk. en-neós Cdeatmute, lit. 'introverted'?); Ir. neas, m. “potters wheel
11676:nes- (3) (?) Hitt. cf. nas-su, nas-ma “either; or: OLat. (Fest.) nesi, pr. ‘without’; Li. nes, cj. “for, as’. (Lat. nisi, for *ne, siét “lest it be’)
11681:nes- — neur- (nour-, nur-)
```


## [2026-09-07T19:35:38.904Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('\\n'.join(lines[8515:8545]))\n# leaf\nidx=t.find('Lehnwort nargis')\nprint('LEAF', t[:idx].count('\\f'), 'printed p =', t[:idx].count('\\f')-10)\nEOF"
}
```


## [2026-09-07T19:35:39.308Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN harness/snare/nostalgia/naos ===\"; grep -n \"^harness,\\|^snare,\\|^nostalgia,\\|^naos\\|^nave,\" KLN_1966.txt | head"
}
```


### [2026-09-07T19:35:40.153Z] TOOL RESULT

```
Goldschmied* etc., giinahgdr^ bazagar *Sunder, sitamgar
gewaltthatig' u. s. w. (Beispiele bei Vullers, Gram. p. 236);
-gird in Namen = arm, -kert^ zd. kereta-; sdgird 'Schiller
=- arm. asakert-, -gan Pluralendung der WSrter auf a =
phi. ak, z. B. bandagan = ap. bandakanam, gen. pi. von
banda = phi. bandak^ ap. bandaka-; -agan Suffix = arm.
akan = phi. akan: Adarbadagan = arm. Atrpatakan^ phi.
Aturpatakan = atropatisch' (d. i. Atropatene) von Alurpat— 239 —
■
= Atropates; Lehnwort lagan *Becken' = syr. NOp^ = gr.
Is^avrj u. s. w. ; — arg Citadelle*, gr. d()yanHzrj(; 'Burgherr ,
auch agyitnsvTjq, palmyr. XtODJlN ^^ pliJ. arkpat H. 73;
giirg Wolf* = zd. vehrka-; Gurgan ein Land = arm. Vt-Jcariy
ap. Vi'kana-; Gurgm N. pr. = arm. Vrken; harg 'Blatt'
--^ zd. vareka- ; kargas 'Geier = zd. kahrkasa- ; pargm re-
ceptaculum aquarum' =^ arm. parken ; Lehnwort nargis aus
*narkis — syr. Dpi3 = gr. vu^f/.iaoog u. s. w. ; — avingdn
'hangend' ^^ ap. ^d-vinkana- ptc. pr. med. der 7. CI. von
Wrzl. vik*^ (oben p. 10); palang 'Leopard', vgl. skr.prdaku-;
tang *enge', bal. tank zu skr. tatic, zd. taxma-, aber phi.
taiig 61. and Ind. 121 ; rang 'Bergschaf -^ skr. rankii- ;
angaram glaube, halte fur', arm. angarem, zd. hankaray^mi,
aber phi. angart Phi. Mm. p. 05, Z. 3, angarend 3. pL pr.
Gl. and Ind. 52.
Nach r erscheint k statt des zu erwartenden g in ArarA:
'Huhn , vgl. ossot. KarU fiir Uarg und die andern iran.
Formen mit k statt ^ bei Horn 848. Daneben steht np.
kurg, kas. karg und andere iran. Formen mit g, s. oben
p. 87. Nach Vokalen: sakav — sakkar *Zucker', das aber
indisches LW. ist; cakdd *ScheiteI, Gipfel' -- arm. cakat
LEAF 249 printed p = 239
```


### [2026-09-07T19:35:40.207Z] TOOL RESULT

```
=== KLN harness/snare/nostalgia/naos ===
17243:harness,  n.  —  ME.  harneis,  herneis,  fr.  OF.  har- neis,  herneis,  harnes  (F.  harnais),  fr.  ON.  *her- nest,  ‘provisions  for  the  army’.  The  first  ele¬ ment  is  rel.  to  OE.  here,  OHG.  heri,  ‘army’;  see harry  and  cp.  words  there  referred  to.  The  se¬ cond  element  is  rel.  to  OE.  nest,  ‘provisions’, and  to  OE.,  OS.,  OHG.  nerian,  MHG.  nerigen, nern,  G.  nahren,  Goth,  nasjan,  ‘to  nourish’,  lit.  ‘to cause  to  recover’,  fr.  OE.  genesan ,  resp.  OS., OHG.,  ginesan,  MHG.,  G.  genesen,  Goth. ganisan,  ‘to  recover’;  see  nostalgia.  MHG.  hor¬ niest,  harnas  (whence  G.  Hdrnisch),  ‘harness, armor’,  is  reborrowed  fr.  OF.  harnais. harness,  tr.  v.  —  ME.  harneisen,  fr.  harneis.  See harness,  n.
24942:naos,  n.,  1)  a  temple;  2)  the  cella  ( Greek  antiquity.
```


## [2026-09-07T19:35:57.094Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24942,24944p' KLN_1966.txt; echo \"=== nostalgia ===\"; grep -n \"nostalgia\" KLN_1966.txt | head -3; echo \"=== snare ===\"; grep -n \"^snare\" KLN_1966.txt | head -3"
}
```


### [2026-09-07T19:35:57.185Z] TOOL RESULT

```
naos,  n.,  1)  a  temple;  2)  the  cella  ( Greek  antiquity.
archit.)  —  ModL.,  fr.  Gk.  vao;  (Ion.  vtjoq, Att.  vemi;  ),  ‘temple;  the  inner  part  of  a  temple, the  shrine,  the  cella’,  which  is  of  uncertain  ori¬ gin.  It  stands  perh.  for  *va afot;  and  is  rel.  to vai6>  (for  *va aua),  ‘I  dwell’,  hence  prop,  de¬ notes  ‘the  dwelling  place  of  a  god’.  See  nostalgia and  cp.  pronaos.
nap,  intr.  v.,  to  have  a  short  sleep.  —  ME.  nappen, fr.  OE.  hnappian,  hnirppian,  rel.  to  OHG.  hnaffe- zan ,  MHG.  napfen.
=== nostalgia ===
17243:harness,  n.  —  ME.  harneis,  herneis,  fr.  OF.  har- neis,  herneis,  harnes  (F.  harnais),  fr.  ON.  *her- nest,  ‘provisions  for  the  army’.  The  first  ele¬ ment  is  rel.  to  OE.  here,  OHG.  heri,  ‘army’;  see harry  and  cp.  words  there  referred  to.  The  se¬ cond  element  is  rel.  to  OE.  nest,  ‘provisions’, and  to  OE.,  OS.,  OHG.  nerian,  MHG.  nerigen, nern,  G.  nahren,  Goth,  nasjan,  ‘to  nourish’,  lit.  ‘to cause  to  recover’,  fr.  OE.  genesan ,  resp.  OS., OHG.,  ginesan,  MHG.,  G.  genesen,  Goth. ganisan,  ‘to  recover’;  see  nostalgia.  MHG.  hor¬ niest,  harnas  (whence  G.  Hdrnisch),  ‘harness, armor’,  is  reborrowed  fr.  OF.  harnais. harness,  tr.  v.  —  ME.  harneisen,  fr.  harneis.  See harness,  n.
24943:archit.)  —  ModL.,  fr.  Gk.  vao;  (Ion.  vtjoq, Att.  vemi;  ),  ‘temple;  the  inner  part  of  a  temple, the  shrine,  the  cella’,  which  is  of  uncertain  ori¬ gin.  It  stands  perh.  for  *va afot;  and  is  rel.  to vai6>  (for  *va aua),  ‘I  dwell’,  hence  prop,  de¬ notes  ‘the  dwelling  place  of  a  god’.  See  nostalgia and  cp.  pronaos.
25633:Derivatives:  nosolog-ic-al,  adj .,  nosolog-ic-al-ly, adv.,  nosolog-ist,  n. nost-,  form  of  nosto-  before  a  vowel, nostalgia,  n.,  homesickness.  —  ModL.,  coined  in 1668  by  Johannes  Hofer  fr.  Gk.  v6avop,  ‘return home’,  and  -tzky'ux,  fr.  4Xyo<;,  ‘pain’.  The  first element  is  rel.  to  veopou  (for  *vEUop.ai),  ‘I  go, come  return’,  vauo  (for  *vxauo ) ,  ‘I  dwell’,  fr. I.-E.  base  *nes-,  *nos-,  ‘to  return;  to  unite’, whence  also  OI.  nasate,  ‘approaches,  joins’, Nasatya,  name  of  the  physicians  of  the  gods.
=== snare ===
```


## [2026-09-07T19:36:07.574Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in AFM_pages.txt AFA.txt TAD_pages.txt ARB_mo3rb.txt LKT.txt FVQ_pages.txt; do echo \"=== $f ناووس/نواويس ===\"; grep -n \"ناووس\\|نواويس\\|نرجس\" $f | head -5; done"
}
```


### [2026-09-07T19:36:08.885Z] TOOL RESULT

```
=== AFM_pages.txt ناووس/نواويس ===
664:( ايوس ) بصل ܢܬ بصل النرجس ܠ طاقات له كالبصل فارسيّتة بلبوس
=== AFA.txt ناووس/نواويس ===
=== TAD_pages.txt ناووس/نواويس ===
50:                      ‫مكتية نرجس ]‪21‬م‬
=== ARB_mo3rb.txt ناووس/نواويس ===
=== LKT.txt ناووس/نواويس ===
=== FVQ_pages.txt ناووس/نواويس ===
```


## [2026-09-07T19:36:10.150Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN narrow/temple ===\"; grep -n \"12.61 NARROW\\|NARROW\\b\" SYN.txt | head -5; echo; echo \"=== IEC sner ===\"; grep -n \"^sner\\|^snerk\\|narwa\" IEC.txt | head -8; echo \"=== WLD band3 narkissos/narke ===\"; grep -n \"vapx\\|νάρκη\\|narke\" WLD_band3.txt | head -5"
}
```


### [2026-09-07T19:36:10.236Z] TOOL RESULT

```
=== SYN narrow/temple ===
21160:Wipe, Broap NARROW
22597:12.62 NARROW

=== IEC sner ===
11855:noruos, å (1) ‘incision, groove, burrow, cut, mark, impression; character, habit'. Cf. en-, rouið, rouos, rüió OHG narwa, f. ‘scar; MHG narwe, nar, w. & sf, id.; LG nor, wf. id.; G Narbe, f. d EMSw. narf, Sw. narv, m. 'pockmark, pitted skin’; OCS nravü, m. ‘manner; OCz. nrav ‘custom’; Slovene nráv ‘nature’; R nòrov ‘habit, man- nerism'; Ukr. norov ‘temper’; cf. also Cz. po- nrava ‘larva’; Li. nařvas, narvà, m. f. “cell of honeycomb; cage’; cf. also (?) narávas, m. (*obstinacy'. See nor- (3) above). (For Hes. norbá ‘incision’: Go. at-snarpjan: Du. sner- pen; ON snerpa, see snorb- Supt)
16553:sneru-, variant of type sneuor-, q.v. in Oss. närv, Dig. nárwà (an undefined tanning implement); Lat. nerva, f. ‘sinew, nerve; OE sner, f. *harpstring; EMCz. sněř, s. 'brome- grass’; cf. Cz. (expressive initial) $nérovat, inf. ‘buckle, gird’
=== WLD band3 narkissos/narke ===
```


## [2026-09-07T19:36:18.139Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor n in (338,339,703,704):\n    print('=== leaf',n,'printed ~',n-5,'===')\n    print(pages[n][:1500])\n    print()\nEOF"
}
```


### [2026-09-07T19:36:19.390Z] TOOL RESULT

```
leaves 725
=== leaf 338 printed ~ 333 ===
334                                    ner-'   —   nes-



Aufrec&t-Kirchhoff II 102, 219)   tiefstufig aftord. yiordr n. „Norden« ags.
                                   ;


norSerra ^inehr nordlich^*, ahd. 'nordroni „nordlich“ (Norden ist bei der
Kichtung des Betenden nach Osten = Links, Bugge BB. 3, 1 05, Brugmann
IF. 11, 274; 13, 163, Bezzenberger BB. 27, 155 a 1, Ostboff MU. VI 174,
Falk-Torp \i,nord)\ arm. nerJcin „unterer‘' (Meillet Msl. 10, 275).
  tJber mogliche Verwandtschaft von n-er mit *n-€i „nieder“ s d.
   Gegen Anreihung von germ. Nerthus „terra mater“ = anord, Njordr
(Horeen Ltl. 209) s. Tick III ^ 295.    Unsicher ist Zugehorigkeit von ai.
ndrdka- m. „Unterwelt, Holle“ (z. B. Uhlenbeck Ai. Wb. 143 zw.; von Persson
Beitr. 222 zu ner~ „eindringen“ gestellt, was im letzten Grunde auf das
gleiche hinausliefe, wenn letzteres mit ncr~ „unten‘‘ zshinge).


, nor- „eindringen, untertauchen, Versteck, H6hle‘‘.
     Gesichert nur furs Balt.-Slav.:   lit.    neriu, nerti „untertauchen, einschlupfen“,
           sinerti „in die Schuhe hineinschlupfen“ (ahnlich apr. nurtue „Hemd“,
I Jcurpesl
vgl. zur Bildung lit. atihivas „Schuh“: auti „Schuhe anziehen“, Trautmann
Apr. 387), lit. ndras „Tauclierente“,     uznarve „Yersteck“ narva „ZelIe der
Bienenkonigin“, nartas „Ecke, Winkek", lett. nirt^ nirddt „untertauchen“
(zur Scheidung von lit. nerti „einfadeln, einschlangen“ usw. s. u. sner- „drehen“),
abg. mra^ nreti „eindringen“, sloven. pondrHi „untertauchen“, klr. ponerfy
„t

=== leaf 339 printed ~ 334 ===
                                               m, nei-                              335

des - 0- nach mit ai. nimsate vergleichharen unthem. Formen wie 2. 3. sg.
^vi-va^cai, -raif oder aus '^vt-vo'-ioixar, s. Brugmann BSGW. 1897, 196 Anm. 1,
Grdr.      3, 106)   reduktionsstufig (s. zuletzt Guntert Abl. 44,76 gegen
                       ;


Kretscliiners Gl. 3, 337 Abtrennungsversuch) ratco, fut. vdooojuac „wohnen,
sich befinden;  bewohnen, bewohnbar machen; ansiedeln“, vaierdco „wohTie;
bewohne    ;
            bewohnt sein“, *vao-j^6g dor. thess. vdog, lak. vdfogy lesb. vavog,
(d. L raffog), jon. vr]6g, att. vEcog „(G6tterwohnuDg =) Tempel, Heiligtum“;
schwundstufig dojuEvog „gerettet, geborgen'* (s. dazu u. sfjdd- ,j8u6‘‘); air.
ftiinim „gehe unter      (von der SonDe)“ (*7W-n€sd yyVJzo-vEEG&ai*' Tick II ^
194, Pedersen KG, II 526); sAh.Jcmtem „erhole mich, werde wieder leben-
dig“ (Praefix Jc-    ^nes^lo-; Jokl SBAk. Wien 168, 1 40); got. ganisan „ge-
nesen‘‘, ahd. as. ginesan „genesen, gerettet werden, am Leben bleiben“, ags.
genesan „gerettet werden, entkommen, iiberleben", got. ganists, ahd. as.
ginist „Genesung, HeiP; kans. got. nasjan „gesund machen“, ahd. nerimi,
nerrm „am Leben erhalten, retten, schutzen, ernahren” (nhd. ndhren) as.
nerian „retten“, ags. nerian „retten, schutzen“ (daneben mit e, d aisl. ncera
nnd fipra „beleben, erfnschen, emahren^, norw. nere, schwed. mdartl. nora
„Feueranmachen“) ; aisl. nara „Leben‘‘, aldr-nari m. „(Leben8erhalter =)
Feuer“, a

=== leaf 703 printed ~ 698 ===
                                           (s)ner-                            699

mengl. nur^g^nen „inurren“, nurhfh (ags. "^nyrTip) „Murren“; lit. niurhsau,
                                    nurhsau (?), -oti .,inurrisch, ubelgelaunt
^oti „du8ter oder briitend dasitzen^^,
aussehen", lett.      nurhstet, nurkset „bruinnien, murren, knurren", n^ka
„em    weinei^licher   Mensch,   ein   solches   Kind^^, narkMt „weinerlicli sein;
knarren‘‘, 'hirkstet „knirsclieii, ein     Gerauscb machen, als ob etwas bricht“,
snirkt „kmrschen“.
  Auf -g: norw. mdartl. snerka „prusten‘', schwed. snerka „prusten, schnar-
chen“, snurka „r6cheln“, mnd. snorken, snarken „schnarchen, schnauben“,
mhd. snarchen  ds.,  nhd. schnarchen\ norw. mirka „knarren, knurren^
ndl. nurkm „bruminen, norgeln“; lit. snargl^s „Nasensclileiin“, lett. snur^
galas ds. („*rasselnd, r6chelnd“), snirguot „weinend schluchzen; fauchen wie
die Ganse“; lett. nirguoties „b6hnisch lachen“, nurgt „die Zahne zeigen“; auch
wohl lit. nafglinu, -inti „etwa8 langsam tun‘^ (Bed. ahnlich wie in schweiz.
norggen „ohne Erfolg arbeiten“).
   Auf -d: mengl. sniirtin „scbnarclien“, mhd. snars „Schnarre, Wachtel-
komg“ (in der Bedeutung schwerlich vereinbares weitere beiFickIU^521);
lett. iiufdet „murren, brummen, knurr en".
    Auf -j): aisl. snarfla „rocheln“, norw, schwed. mdartl. snarva ^knurren,
die   Zahne fletschen“.
  Vgl. Fick     506, KZ. 43, 131   Fick III ^ 294 f., 520 f.; Persson IF. 35,
                                       

=== leaf 704 printed ~ 699 ===
700                                    (s)ner-



schnurren,    ein-schnurren,   -schnorren „zusammenschrumpfen‘*,     isl.   snurda
„Knoten an einem Faden, bildlich        vom Nasenriimpfen**;
  dehnstufig   aisl. nari „Weichen‘‘ („Einscliiiurung des Leibes‘‘), mhd. ncer-

lich  „knapp, genau, jimg‘‘ und mit Abtbnung aisl. nore „Zwergiiaine‘‘, nor
n. „Bucht mit enger Einfahrt, enger Sund“, dan. schwed. mdartl. wr
jjKnirps, ganz kleines Kind" (ahnliche Bedeutung in norw. mdartl. mirv
„kleine kurze verkruppelte Pigur", mengl. nurvil, nirvil „Zwerg");
   wahrscheinlich (s. Persson Wzerw. 63 f., Beitr. 823 f., auch Wood IP. 18y
24f., Bartholomae IP. 21, 348 Anm. 5) ahd. snuor „ScbDur, Band, Soil",
dan.-schwed. snor ds., got. snorjo „geflochtener Korb", ags. sner (^snorio)
„Saite einer Harfe", aisl. snpri n. „gedrehte8 Soil" (kaum ans *5Wd[M]-ro-
zu av. snavaro „Selme", ai. snavan-^ gr. vbvqov, Brugmann MU. 2, 225,
Pedersen KZ. 32, 247 sehen darin Wechsel von «- nnd r-St.). Ygl. zu
den germ. Wortem besonders Pick III^ 294, Persson Beitr. 576, 81 5 f. (Lit.),
Palk-Torp u. narOj snor, snerpe.
   Lit. neriu^ nerti „einfadeln, einschlangen, einzieben" nyru (s. Leskien
Abl. 337), prat, nirau^ nirti „sicb scblangeln, ranken", ismres „aus dem
Gelenk gekommen", narau, -yti „einen Knoten oder eine Schlinge machen,
in ein Gelenk einfugen, einrenken", ndras, narys „Sclilinge; Gelenk am
Korper, Glied einer Kette", narys „Knorren, Auswnchs, Geschwiir", ndgo
nar§s „Krankheit am Fu6e des Pferde
```


## [2026-09-07T19:36:29.818Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[338]\ni=p.find('nes-',600)\nprint(p[1500:3500])\nEOF"
}
```


### [2026-09-07T19:36:31.165Z] TOOL RESULT

```
auchen“, abg. nora           latibulum“, russ. nord „Loch, Hohle, Grube‘^
klr. nord „Erdloch, Quelle^, nor yea „Feldmaus, Engerling“, aruss. ponorovz
„Erdwurm“, poln. pandrow „Engerling“        (nicht zu (s)ner- „drehen“, s. d.),
skr. norac „Taucher“; auf einer Tiefstufe            (vgl. apr. nurtue) beruht
slav. nyr-, nur- in abg. nyrati, 7iyreti „8e iinmergere“, nura „janua“ (usw.,
s.   MiklosichEWb. 212 f.).
   Unsicher ai. ndraha- m. „Unterwelt, H6lle“ (s. u. ner- „unten“).
   Unannehmbar ist die Deutung von got. drighan „trinken“ usw. aus *nr-
enTc- („eintauchen“) durch Fick 111^21 If. (nicht wiederholt von Falk-Torp
. drik, drikke\ s. dhreg- „ziehen‘‘).
   Vgl. Fick I * 503 KZ. 43, 1 49 (aber N}]qsi% v7]q6v, vt]g[dag s. u. snd „flie8en‘^;
dgveo s. u. tier- „feuchten“; dgvsvnjg s. u. eras „flie6en''; ai. nird- „Wasser‘‘
ist unerklart), Persson Beitr. 222,    Vielleicht (s. Fick KZ. 43, 149) besteht
Zshang mit net'- „unten‘^ als ,,sich verkriechen, untertauchen“; wenn ai. nd-
raka- auf der Bed. „unten“ beruht, konnte ein erst bsl. Ausbau von ner-
„unten'‘ zu verbaler Verwendung vorliegen.


nes- „angenehm, gliicklich wohin gelangen“, auch                vom Geborgensein im
       schiitzenden Hause.
  Ai. tidsate „geht liebevoll heran, gesellt sich zu, vereinigt sich mit“,
redupl. unthematisch nimsate 3. pi. „sie beriihren nahe mit dem Korper,
kiissen^ (^ni-ns-ate), ptc. nims-ana- (alte Deponentien, vgl. gr. veo/am, vlao-
/iat Brugmann II ^ 3^ 684) schwundstufig ai. dsta-, av. asta- n. „Heimat,
                              ;

Wohnort" (Bartholomae KZ. 29, 483, vgl. mit anderen Yokalstufen gr. voorog,
ags. nest n.) gr. veopai „komme gliicklich heran an, kehre heim“ (genauer
                 ;

„werde heimkehren'*, punktuell, s. Brugmann 11^ 3, 745, Nioxcog eig. „der
ixnmer wiederkehrende^* (Kretschmer Gl. 4, 308 f.), voorog „Heimkehr“, redupl.
vloofim oder vJooop,ai ,,veouaC^ (entweder aus *vi-va-ojaai mit Bewahrung
```


## [2026-09-07T19:36:38.902Z] TOOL CALL #51: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T19:36:38.909Z] TOOL RESULT

```


```


## [2026-09-07T19:36:44.390Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BD%CE%AC%CF%81%CE%BA%CE%B9%CF%83%CF%83%CE%BF%CF%82",
 "prompt": "Give the full etymology section for Ancient Greek νάρκισσος: what origin do modern sources (Beekes, Chantraine) give, is the connection with νάρκη accepted or rejected, and any descendants (Latin, Syriac, Persian, Arabic)."
}
```


## [2026-09-07T19:36:45.657Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%B1%DA%AF%D8%B3",
 "prompt": "Give the etymology of Persian نرگس (narges) — the Middle Persian form, the route from Greek, any Syriac/Aramaic intermediary, and cited sources."
}
```


### [2026-09-07T19:36:49.525Z] TOOL RESULT

```
# Etymology of Ancient Greek νάρκισσος

**Origin:** According to Beekes, the suffix "clearly points to a Pre-Greek word." The connection with νάρκη (numbness) is rejected as "due to folk etymology."

**Descendants:** The word spread widely through ancient languages:
- **Latin:** narcissus (with further descendants)
- **Classical Syriac:** ܢܪܩܝܣ (narqīs)
- **Middle Persian:** nlgs /nargis/
- **Arabic:** نَرْجِس (narjis)
- **Persian:** نرگس (narges)
- **Old Armenian:** ներգիս (nergis)

The entry notably cites Beekes' 2010 *Etymological Dictionary of Greek* as the primary modern source, though it references Chantraine indirectly through the "Further reading" section linking to classical lexicographic works.
```


### [2026-09-07T19:36:50.438Z] TOOL RESULT

```
# Etymology of Persian نرگس (narges)

**Middle Persian Form:**
The term derives from Middle Persian with the form "nlgs /nargis/" according to the Wiktionary entry.

**Greek Origin:**
The ultimate source is Ancient Greek νάρκισσος (nárkissos), from which the Middle Persian form evolved.

**Route of Transmission:**
The documented path is: Ancient Greek → Middle Persian → Persian. The entry states the term was "Inherited from Middle Persian" and traces back to "Ancient Greek _νάρκισσος_ (nárkissos)."

**Syriac/Aramaic Intermediary:**
The provided content contains no reference to Syriac or Aramaic as intermediary languages in this etymological chain.

**Cited Sources:**
The Wiktionary article does not cite specific academic sources for the Middle Persian-to-Greek connection. It merely documents the inherited linguistic relationship without providing bibliographic references for the intermediate transmission stages.
```


## [2026-09-07T19:36:56.712Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%88%D9%88%D8%B3",
 "prompt": "Give the etymology and meaning of ناووس in Persian and/or Arabic — is it from Syriac ܢܘܣܐ / Greek ναός? List all language sections and the etymologies given."
}
```


## [2026-09-07T19:36:57.716Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/harness",
 "prompt": "Give the full etymology of \"harness\" — Old French harnois, the Old Norse *hernest hypothesis, and how confident the source is."
}
```


### [2026-09-07T19:37:02.848Z] TOOL RESULT

```
# Etymology of "Harness"

**Old French Origin:**
The word derives from Old French *harnois*, described as "a noun of broad meaning: 'arms, equipment; harness; male genitalia; tackle; household equipment'" dating to the 12th century.

**Old Norse Hypothesis:**
The proposed but uncertain origin suggests Old Norse *\*hernest* meaning "provisions for an army," composed of *herr* ("army") plus *nest* ("provisions"). However, the source explicitly states this etymology is "of uncertain origin" and presented as a hypothesis rather than confirmed fact.

**Confidence Level:**
The source expresses low confidence, using the qualifier "perhaps" when introducing the Old Norse theory. This indicates the etymological connection remains speculative. The ultimate origin of the Old French *harnois* itself remains unclear despite this proposed Germanic connection.

The modern non-military sense referring to "fittings for a beast of burden" emerged by the early 14th century, representing an application of the original equipment/armor meaning to animal gear.
```


### [2026-09-07T19:37:04.417Z] TOOL RESULT

```
# Etymology and Meaning of ناووس

## Language Sections
The Wiktionary entry contains **one language section: Arabic**. (The page title appears in 6 Wiktionary language editions, but only the Arabic section is documented in this content.)

## Etymology
According to the entry, the word derives from "perhaps both Classical Syriac ܢܘܫܐ (nawšã, 'coffin, sarcophagus; tomb, sepulchre') and ܢܘܣܐ (nawsā, 'charnel, repository for the dead'), derived from Ancient Greek ναός (nāós, 'innermost part of a temple, sanctuary, or shrine')."

The source notes this Greek term was historically applied by Greek scholars to describe burial chambers and sarcophagi found within pyramids.

## Meaning
The Arabic noun ناووس (nāwūs) carries two primary definitions:
1. A stone burial container—specifically "sarcophagus" or "coffin"
2. A burial site, including "tomb" or "Christian graveyard"

The word is masculine and follows standard Arabic declension patterns with both singular and plural forms.
```


## [2026-09-07T19:37:10.687Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/nes-",
 "prompt": "Give the reconstruction, gloss, and derived terms/descendants for PIE *nes- (Greek nostos, naos; Sanskrit asta; Germanic *nazjan, *nestaz). Quote the root gloss exactly."
}
```


## [2026-09-07T19:37:11.572Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/narrow",
 "prompt": "Give the etymology of English \"narrow\": Old English nearu, Proto-Germanic *narwaz, and the Proto-Indo-European root proposed. Also note any statement of uncertainty."
}
```


### [2026-09-07T19:37:15.012Z] TOOL RESULT

```
# Proto-Indo-European *nes-

**Reconstruction:** *nes-

**Gloss:** "to return home (safely)"

**Key Derived Terms and Descendants:**

- **Greek:** νόστος (nóstos), ναός (naós), νίσσομαι (níssomai)
- **Sanskrit:** नस् (nas, "to come together, be fraudulent")
- **Germanic:** *nazjaną, *nōzijaną
- **Tocharian:** A nas-, B nes-

The root demonstrates the PIE pattern of expressing the concept of homecoming and return, with reflexes preserved across multiple language families including Hellenic, Indo-Iranian, Germanic, and Tocharian branches.
```


### [2026-09-07T19:37:16.690Z] TOOL RESULT

```
# Etymology of "narrow"

According to the Wiktionary entry, "narrow" comes from Middle English *narow*, *narowe*, *narewe*, *narwe*, and *naru*, which descended from Old English *nearu* meaning "narrow, strait, confined, constricted."

The Old English term derived from Proto-West Germanic *\*naru*, which came from Proto-Germanic *\*narwaz* ("constricted, narrow"). The ultimate source is Proto-Indo-European *\*(s)ner-*, defined as "to turn, bend, twist, constrict."

**Note on uncertainty:** The entry indicates that the Proto-Indo-European root link is a "page does not exist," suggesting the connection to PIE *\*(s)ner-* represents a scholarly reconstruction rather than documented historical evidence.
```


## [2026-09-07T19:37:30.677Z] TOOL CALL #58: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%CE%BD%CE%AC%CF%81%CE%BA%CE%B9%CF%83%CF%83%CE%BF%CF%82\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%B1%DA%AF%D8%B3\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%88%D9%88%D8%B3\" \\\n \"https://www.etymonline.com/word/harness\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/nes-\" \\\n \"https://en.wiktionary.org/wiki/narrow\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 362 (Ner 2 / Nes 1): narkissos Pre-Greek, narges route, nawus Syriac>Arabic, harness *hernest, PIE nes-, narrow *narwaz\" 2>&1 | tail -2\ndone"
}
```


## [2026-09-07T19:37:32.223Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AFA naus/Grab ==\"; grep -n -i \"nawsa\\|nauso\\|Grabmal\\|naus\" AFA.txt | head -8; echo \"== FSD narcissus ==\"; grep -n \"^narcissus\" FSD_vol3.txt FSD_vol2.txt 2>/dev/null | head -3; echo \"== SYN 12.62 ==\"; sed -n '22597,22640p' SYN.txt"
}
```


### [2026-09-07T19:37:33.878Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/aac18a84d39cf3ee.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6a9ebb49094d15fe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4e391ee859dfb3d4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e987b7a5a0fc1038.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f1eb40e394615a67.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d6fc83765de5cdf9.txt
```


### [2026-09-07T19:37:33.960Z] TOOL RESULT

```
== AFA naus/Grab ==
115:Themas hinausgegangen, habe auch manchmal ein uner-
134:strengen Arabisten hinaus ein Orientalist darin gelegent-
== FSD narcissus ==
== SYN 12.62 ==
12.62 NARROW
z 4 ae Gath. aggwus Bh Saabs ankélas an, N rengr, engr ett. Saurs trl Dan. ed, trang, smal ChSl.  qziikit, tésnit boy Helo Sw. smal, trdng SCr. _uzak, tjesan estrecho, ango OE nearu, enge, smal Boh.  tizky, tésny rime, ing ae ME ___narowe, streit, smal Pol.  wazki, ciasny Oil, cumun NE narrow Russ. uzkij, tesnyj cumhang, he Du. nauw, smal, eng Skt.  anhu-, avistirna-
» CUfyng OHG engi, angi, smal Av. sm at
K, striz MHG enge, smal
NHG _ schmal, eng
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
it,
igitized by Arya Samaj Foundation Chennai and eGangotri
886
Most of the words for ‘narrow’ rest on the notion of ‘tight’ or ‘pressed’, while some are from ‘slender’ or ‘small’.
1. Derivs. of IE *angh- in Av. qz- ‘tie, oppress’, Grk. ax ‘throttle’, Lat. angere ‘throttle, distress, torment’, ChSl. qzite ‘crowd, straiten’. Walde-P. 1.62f. Er- nout-M. 51. Walde-H. 1.47.
Lat. angustus (> It. angusto, Sp. an- gosto, Rum. tngust); Br. enk, cpds. Ir. cum-ung, Nir. cumhang, W. cyf-yng; Goth. aggwus, ON ongr, OF enge, ange, OHG angi, engi, MHG enge, Du., NHG eng; Lith. ankstas; ChSl. qztki, SCr. uzak, Boh. tzky, Pol. wazki, Russ. uzkij; Skt. anhu- (only in comp. anhtyas- and in cpd.) beside arihas- ‘fear, oppression’, Av. qzah- ‘need, op- pression’; Arm. anjuk.
2. Grk. orevds, Jon. orewéds (fr. *crevpés), beside arevyypds ‘narrow’, etc., prob.: ON stinnr ‘stiff, firm, strong’, OE sith id. and ‘hard, severe’, with secondary sense in Gmc. develop- ment (cf. Grk. crevoywpia, Lat. angus- tiae, NHG enge, etc. ‘narrowness’ and ‘difficulty, distress’). Walde-P. 2.627. Boisacq 909. Falk-Torp 1168.
3. It. stretto, Fr. éroit, Sp. estrecho, Rum. strimi fr. Lat. strictus (*strinctus for Rum.) ‘drawn together, bound tight’, pple. of stringere ‘bind together’. REW 8305.
4. Ir. coil, Nir. caol, W. cul, also ‘slender, lean’, cf. OBr. culed ‘macies’, perh. : Lett. kails ‘naked, bald’, kaili Vaudis ‘childless couple’, in any case with Celtic extension of ‘slender’ to ‘narrow’. Walde-P. 1.455. Stokes 88.
Br. striz, fr. Lat. strictus (above, 3). Loth, Mots lat. 208.
5. ON prongr, Dan. trang, Sw. trang, cf. MLG drange, MHG gedrenge ‘stuffed full, tight’: ON pryngua, Dan. trenge, Sw. trdénga, OE pringan, NHG drdngen, etc., ‘press, crowd’, Lith. trankus ‘jolt-
SELECTED INDO-EUROPEAN SYNONYMS
ing, rough’, Av. 6razta- ‘close-packeg? (ranks), etc. Walde-P. 1.758 ¢. Falk. Torp 1279. 1293 f.
OE smal, ME smal, OHG, MHG, Dy smal, NHG schmal (largely also ‘slen- der’), Dan., Sw. smal (meaning ‘narrow’ fr. German), Gme. group in early period also or only ‘small’ (12.56).
Dan. snever : ON snefr, snefr ‘tight narrow, quick, swift’, snafugr ‘swift? without s- ON nefr, OSw. never ‘quick’, perh. Arm. nurb ‘narrow, slender, thin’, Walde-P. 2.698. Falk-Torp 1095.
OE nearu, ME narowe, NE narrow, OS naru : ON Norva-sund ‘Straits of Gi- braltar’, OHG narwa ‘scar’ (i.e. ‘closed wound’), prob. fr. a root meaning ‘draw together, tie’(?) in OHG snuor ‘band, string’, Lat. nervus ‘tendon’, ‘nerve’, etc. Walde-P. 2.699 f. (with 2.696), Falk- Torp 755.
ME streit, NE strait (still adj. for ‘narrow’ or ‘difficult’ in Bible, but now rare except in sb. Straits), fr. OFr. estreit (Fr. étroit, above, 3). NED s.v. strait.
Du. nauw:MLG nouwe ‘narrow, close, exact’, MHG adv. nouwe, genouwe ‘close, scarcely’ (NHG genau ‘exactly’), OE hnéaw ‘stingy’, etc., all prob. as ‘little’ fr. ‘crushed’: OHG Aniuwan, MHG niuwan ‘pound to pieces’, etc. Walde-P. 1.396. Franck-v. W. 542. Falk-Torp 785.
6. Lith. siauras, Lett. Saurs, etym.? Miihl.-Endz. 4.7.
7. ChSl. qztikt, etc., above, 1.
ChSI. t&snii (renders orevés Lk. 13.24, TeOAtupevos Mt. 7.14), SCr. tyesan, Boh. tésny, Pol. ciasny, Russ. tesnyj : ChSl tiskati ‘press’. Meeillet, Etudes 435. Briickner 60.
8. Skt. ahu-, above, ]. }
Skt. avistirna-, avistrta-, neg. of Use tirna-, vistrla~ ‘spread out, extenslve, wide’, pples. of vi-str- ‘spread out’.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Goth. ...\... ds ON pykkr ot pos, us Dan. tyk asus; (late) gree Sw. tjock 970880) anen® OE picce épats espes0 ME thikkee grueso, NE thick _ -9t08 Du. dick fiug, remor OHG  dicchi reamhar MHG  dicke NHG dick 20 Words for hick’ as applied to the di- ension through, as in a thick board, are m
glso or were Once used in the lea specific sense of coarse’ or ‘big, bulky’, or of per- sons ‘stout, fat’.
1, IB *bhengh-, esp. *bhnghu-. Walde- p, 2,151.
Here as ‘thick’ Grk. waxts, Lett. biezs, Skt, bahula- (also ‘abundant, much’ like bahu- = Grk. raxts) : Av. bazah-, basnu- ‘height, depth’, ON bingr ‘heap’, etc. 2.NG xovrpés, fr. class. Grk. xov- p's ‘granular, coarse (esp. of salt)’ be- side xév5pos ‘grain or lump (of salt), goats’: Lat. frendere ‘rub to pieces’, OE grindan, NE grind, etc. Walde-P. 1656. Boisacq 1066.
3, Lat. crassus, perh. ‘thick’ as ‘firm, wold’ fr. ‘firmly twisted together’ : aie Wicker-work’, Grk. x&prados ‘bas- il Skt. krt- ‘spin’. Walde-P. 1.421. ig 227f. Walde-H. 1.285 f.
al grossus (> It. grosso, Sp. aah um. gros; Fr. gros mostly ‘big, ete, (265). : Ir. bras(s) ‘large, big’, q Lion - Walde-P. 1.698. Walde- It,
thie =n ir. épais, Sp. espeso, also (264, ense’, fr. Lat. spissus ‘dense’
4 Tr V. x ne (Nix. ttugh only ‘dense’), He, (below, 5 ‘ON pykkr, OE picce,
SP ATIAL RELATIONS:
Digitized by Arya Samaj Foundation Chennai and eGangotri
PLACE, FORM, SIZE 887
12.68 THICK? (In Dimension)
Lith. storas
Lett. biezs, resns ChSl. debelit
```


## [2026-09-07T19:37:44.326Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON نرگس ===\"; grep -n -o \"نرگس:[^\\n]\\{0,180\\}\" MON_part2.txt | head -5; echo \"=== ARY ===\"; grep -n \"نرگس\\|ناووس\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== ARY latin ===\"; grep -n -i \"NARCISSUS\\|NARGES\" incoming/ARY/ARY_latin_index_pages.txt | head -5"
}
```


### [2026-09-07T19:37:45.528Z] TOOL RESULT

```
=== MON نرگس ===
21433:نرگس: 
67468:نرگس: (گْیا.) چیزیست که باغچة 
=== ARY ===
=== ARY latin ===
```


## [2026-09-07T19:37:49.284Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21425,21445p' MON_part2.txt; echo \"-----\"; sed -n '67460,67485p' MON_part2.txt"
}
```


### [2026-09-07T19:37:49.361Z] TOOL RESULT

```
کدو که دارای مبوه‌ای بزرگک و کروی است 
و رنگ میان بر آن زرد است و دانه‌های 
درشت دارد. طعم آن شیرین مزه است و در 
اکثر دهات ایران کشت می‌شود؛ بسیخ 
صیفی» بال قباغی» کدوی مربایی» میلبیون. 
کدوی حجام: کدویی کوچک و مدور که 
حجمان بعد از استره زدن بر زخم‌های 
حجامت چسانند تا خون را دکشد. کدوی 
مسمایی: (گیا.) کدو سفید. کدوی نرگس: 
کدویی که شراب نرگس را در آن نگهداری 
کنند. کوزه شراب که از حدوی خشکت 
کنند. ساغره پیاله. قلیان. (مج.) کاسة سر. 
کدورت: ا«ت0۵ (ع. . کدورة] (اسص.) 
هک تاریکی. آلودکّی؛ نابا کی؛ مق. صفاه 
صفوت. ملال. ملالت؛ ج. کدورات. 
کسد‌ونیمه: (0۸)0]-.۲ (امر.) کوزة 
شرابخوری» قنینه 
کده: (2۵۸66 [- کسد] (ا.) خانه» سرای. 
چوبی که در کلیدان فرو افتد تا در نگشاید؛ 
یت ی (پس.) به آخر اسم ملحق شود و 
سم مکان سازد: بتگده. 
-----
بنام پشم موسومند. موهای نرم‌تر این گونه 
دام‌ها که معمولا در زير بشمها قرار دارند 
موسوم‌به کرکث هستند که به مصرف تهیة 
پارچه‌ها گران‌قیمت و نرم می‌رسد: شعره 
موی. (پز.) موی سر. تر کیب اسمی: موی 
دماغ: (عم.) هر یک از موهای باریکی که 
در درون نی روید. ( کد.) (عم.) کسی که 
هميشه باعث زحمت دیگری شود؛ مزاحم. 
موی نرگس: (گْیا.) چیزیست که باغچة 
نرگس از قلم نرگس برمیآید و گل بر آن 
می‌باشد. یکك سر مو: (ق‌مر.) بسیار کم؛ 
بسیار اندک. ترکیبات فعلی: به مویی بند 
بودن چیزی: به مرحلةً حساس رسیدن آن؛ 


یمیت این ی رسد ع تفاس فسست :تسف سس دس سس 


مو ات 
مشرف به خطر بودن. مو (موی) از سر کسی 
ربودن: (کد.) نهایت تردستی و چستی و 
چالاکی نمودن. مو (موی) از کف بر آمدن: 
( کد.) محال بودن امر. مو (موی) (را) از 
ماست کشیدن: (عم.) حساب کاری را داشتن 
و به جزئیات آن رسیدگی کردن, در کارها 
دقیق بودن و همه چیز را در نظر داشتن
```


## [2026-09-07T19:37:55.033Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \".\\{0,60\\}نرگس.\\{0,200\\}\" incoming/MON/MON_2vol_Adena_v2_djvu.txt | grep -n \"نرگس\" | head -8"
}
```


### [2026-09-07T19:37:59.522Z] TOOL RESULT

```
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,200}
                         \___exceeds complexity limits
```


## [2026-09-07T19:38:04.102Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ('incoming/MON/MON_2vol_Adena_v2_djvu.txt','MON_part2.txt'):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for m in re.finditer('نرگس',t):\n        s=t[max(0,m.start()-90):m.start()+220].replace('\\n',' ')\n        if 'معر' in s or 'یون' in s or 'پهلوی' in s or 'گیا' in s:\n            print(f,'|',s)\n            print('---')\nEOF"
}
```


### [2026-09-07T19:38:05.530Z] TOOL RESULT

```
incoming/MON/MON_2vol_Adena_v2_djvu.txt |  د.  قد. ۱۳ مغرور.  بکدنده؛ کله شق  قدح: ملع | () کاس ج اقداح. قدح  زرین» زرین قدح: (کد.) نرگس. قدح زین:  (کد.) قاش زین. ه لاجوردی: (کن.)  آسمان. . قدح مریم؛ : (گیا ) گیاهی است دوایی  و آن نوعی از حی العالم است و برگک و بخ  آن سنگ مثائه را بر یزاند؛ زلائف‌المل وکک.  قدح بر سر کسی شکستن: او را رسوا کردن.  (تص.
---
incoming/MON/MON_2vol_Adena_v2_djvu.txt | از استره زدن بر زخم‌های  حجامت چسانند تا خون را دکشد. کدوی  مسمایی: (گیا.) کدو سفید. کدوی نرگس:  کدویی که شراب نرگس را در آن نگهداری  کنند. کوزه شراب که از حدوی خشکت  کنند. ساغره پیاله. قلیان. (مج.) کاسة سر.  کدورت: ا«ت0۵ (ع. . کدورة] (اسص.)  هک تاریکی. آلودکّی؛ نابا کی؛ مق. صفاه  صفوت. ملال. ملالت؛ ج. کدورات
---
incoming/MON/MON_2vol_Adena_v2_djvu.txt | ای  حجامت چسانند تا خون را دکشد. کدوی  مسمایی: (گیا.) کدو سفید. کدوی نرگس:  کدویی که شراب نرگس را در آن نگهداری  کنند. کوزه شراب که از حدوی خشکت  کنند. ساغره پیاله. قلیان. (مج.) کاسة سر.  کدورت: ا«ت0۵ (ع. . کدورة] (اسص.)  هک تاریکی. آلودکّی؛ نابا کی؛ مق. صفاه  صفوت. ملال. ملالت؛ ج. کدورات.  کسد‌ونیمه: (0۸)0]-
---
incoming/MON/MON_2vol_Adena_v2_djvu.txt | تر جس معر .] (.) ( کا.)    ۰ ۱۹۳  گیاهی است از رده تکث لیه‌ای‌ها که سر دستة  گیاهان تبرةٌ نرگس‌ها می‌باشد. اين گیاه مانند  زعفران دارای پیاز است و برگ‌هایش طویل  و از ريشه خارج می‌شوند. گل‌هایش منفرد و  در انتهای ساقه قرار دارند. تعداد  کلب رگ‌هایش سه عدد و سفید رنگند و  کاس رگک‌هایش نیز سه عددند که همرنگ  گل
---
incoming/MON/MON_2vol_Adena_v2_djvu.txt | یش سه عدد و سفید رنگند و  کاس رگک‌هایش نیز سه عددند که همرنگ  گلب رها می‌باشند. در وسط گل نرگس  معمو لا حلقه‌ای زرد رنگ دیده می‌شود که  زیبایی خاصی به گل این گیاه می‌دهد. در  بعضی گونه‌های نرگس خود گل نیز زرد  رنگ است؛ نرگس شهلاه نرجس» عبهر.  (کد.) چشم معشوق. ی بت (کن.)  توا رگس بینا: (کد.) چشم. نرگس  دزم: ( 
---
incoming/MON/MON_2vol_Adena_v2_djvu.txt | و لا حلقه‌ای زرد رنگ دیده می‌شود که  زیبایی خاصی به گل این گیاه می‌دهد. در  بعضی گونه‌های نرگس خود گل نیز زرد  رنگ است؛ نرگس شهلاه نرجس» عبهر.  (کد.) چشم معشوق. ی بت (کن.)  توا رگس بینا: (کد.) چشم. نرگس  دزم: ( کد.) ) چشم خشمگین. ۳9  (گی.) نسرین. ن گس ژوزفین: (گیاء) یکی از  گونه‌های برگس که بنام برونسویجی نیز
---
incoming/MON/MON_2vol_Adena_v2_djvu.txt | ود که  زیبایی خاصی به گل این گیاه می‌دهد. در  بعضی گونه‌های نرگس خود گل نیز زرد  رنگ است؛ نرگس شهلاه نرجس» عبهر.  (کد.) چشم معشوق. ی بت (کن.)  توا رگس بینا: (کد.) چشم. نرگس  دزم: ( کد.) ) چشم خشمگین. ۳9  (گی.) نسرین. ن گس ژوزفین: (گیاء) یکی از  گونه‌های برگس که بنام برونسویجی نیز  1 ترگس نیم خواب: (کد.) چشم  
---
incoming/MON/MON_2vol_Adena_v2_djvu.txt | د  رنگ است؛ نرگس شهلاه نرجس» عبهر.  (کد.) چشم معشوق. ی بت (کن.)  توا رگس بینا: (کد.) چشم. نرگس  دزم: ( کد.) ) چشم خشمگین. ۳9  (گی.) نسرین. ن گس ژوزفین: (گیاء) یکی از  گونه‌های برگس که بنام برونسویجی نیز  1 ترگس نیم خواب: (کد.) چشم  معشوق. نرگس و گل: (کد.) چشم و گوش  معشوق. ۰ نرگس بعقوبی: (گیا.) یکی از  گونه‌ه
---
incoming/MON/MON_2vol_Adena_v2_djvu.txt | ن: (گیاء) یکی از  گونه‌های برگس که بنام برونسویجی نیز  1 ترگس نیم خواب: (کد.) چشم  معشوق. نرگس و گل: (کد.) چشم و گوش  معشوق. ۰ نرگس بعقوبی: (گیا.) یکی از  گونه‌های نرگس که بنام زنبق یعقوبی نیز  مشهور است. نوعی پارچه» ن رگسی.  نرگسی: آ-6ع۱2 (ص‌سسه..) مسوب به  نرگس. نرگسی را بستن و فسفسی را باز  کردن: (عم.) (ک:
---
incoming/MON/MON_2vol_Adena_v2_djvu.txt | ام برونسویجی نیز  1 ترگس نیم خواب: (کد.) چشم  معشوق. نرگس و گل: (کد.) چشم و گوش  معشوق. ۰ نرگس بعقوبی: (گیا.) یکی از  گونه‌های نرگس که بنام زنبق یعقوبی نیز  مشهور است. نوعی پارچه» ن رگسی.  نرگسی: آ-6ع۱2 (ص‌سسه..) مسوب به  نرگس. نرگسی را بستن و فسفسی را باز  کردن: (عم.) (ک:.) به خواب رفتن  (فرعا.جما.) چشمکد. (
---
incoming/MON/MON_2vol_Adena_v2_djvu.txt | د.) چشم  معشوق. نرگس و گل: (کد.) چشم و گوش  معشوق. ۰ نرگس بعقوبی: (گیا.) یکی از  گونه‌های نرگس که بنام زنبق یعقوبی نیز  مشهور است. نوعی پارچه» ن رگسی.  نرگسی: آ-6ع۱2 (ص‌سسه..) مسوب به  نرگس. نرگسی را بستن و فسفسی را باز  کردن: (عم.) (ک:.) به خواب رفتن  (فرعا.جما.) چشمکد. (.) نوعی پارچه  لطیف گرانبها» نرگس. خو
---
incoming/MON/MON_2vol_Adena_v2_djvu.txt | بی: (گیا.) یکی از  گونه‌های نرگس که بنام زنبق یعقوبی نیز  مشهور است. نوعی پارچه» ن رگسی.  نرگسی: آ-6ع۱2 (ص‌سسه..) مسوب به  نرگس. نرگسی را بستن و فسفسی را باز  کردن: (عم.) (ک:.) به خواب رفتن  (فرعا.جما.) چشمکد. (.) نوعی پارچه  لطیف گرانبها» نرگس. خورشی است که با  تخم‌مرغ زده و پیاز خرد کرده در روغن  سرخ کرده ت
---
MON_part2.txt |  د.  قد. ۱۳ مغرور.  بکدنده؛ کله شق  قدح: ملع | () کاس ج اقداح. قدح  زرین» زرین قدح: (کد.) نرگس. قدح زین:  (کد.) قاش زین. ه لاجوردی: (کن.)  آسمان. . قدح مریم؛ : (گیا ) گیاهی است دوایی  و آن نوعی از حی العالم است و برگک و بخ  آن سنگ مثائه را بر یزاند؛ زلائف‌المل وکک.  قدح بر سر کسی شکستن: او را رسوا کردن.  (تص.
---
MON_part2.txt | از استره زدن بر زخم‌های  حجامت چسانند تا خون را دکشد. کدوی  مسمایی: (گیا.) کدو سفید. کدوی نرگس:  کدویی که شراب نرگس را در آن نگهداری  کنند. کوزه شراب که از حدوی خشکت  کنند. ساغره پیاله. قلیان. (مج.) کاسة سر.  کدورت: ا«ت0۵ (ع. . کدورة] (اسص.)  هک تاریکی. آلودکّی؛ نابا کی؛ مق. صفاه  صفوت. ملال. ملالت؛ ج. کدورات
---
MON_part2.txt | ای  حجامت چسانند تا خون را دکشد. کدوی  مسمایی: (گیا.) کدو سفید. کدوی نرگس:  کدویی که شراب نرگس را در آن نگهداری  کنند. کوزه شراب که از حدوی خشکت  کنند. ساغره پیاله. قلیان. (مج.) کاسة سر.  کدورت: ا«ت0۵ (ع. . کدورة] (اسص.)  هک تاریکی. آلودکّی؛ نابا کی؛ مق. صفاه  صفوت. ملال. ملالت؛ ج. کدورات.  کسد‌ونیمه: (0۸)0]-
---
MON_part2.txt | تر جس معر .] (.) ( کا.)    ۰ ۱۹۳  گیاهی است از رده تکث لیه‌ای‌ها که سر دستة  گیاهان تبرةٌ نرگس‌ها می‌باشد. اين گیاه مانند  زعفران دارای پیاز است و برگ‌هایش طویل  و از ريشه خارج می‌شوند. گل‌هایش منفرد و  در انتهای ساقه قرار دارند. تعداد  کلب رگ‌هایش سه عدد و سفید رنگند و  کاس رگک‌هایش نیز سه عددند که همرنگ  گل
---
MON_part2.txt | یش سه عدد و سفید رنگند و  کاس رگک‌هایش نیز سه عددند که همرنگ  گلب رها می‌باشند. در وسط گل نرگس  معمو لا حلقه‌ای زرد رنگ دیده می‌شود که  زیبایی خاصی به گل این گیاه می‌دهد. در  بعضی گونه‌های نرگس خود گل نیز زرد  رنگ است؛ نرگس شهلاه نرجس» عبهر.  (کد.) چشم معشوق. ی بت (کن.)  توا رگس بینا: (کد.) چشم. نرگس  دزم: ( 
---
MON_part2.txt | و لا حلقه‌ای زرد رنگ دیده می‌شود که  زیبایی خاصی به گل این گیاه می‌دهد. در  بعضی گونه‌های نرگس خود گل نیز زرد  رنگ است؛ نرگس شهلاه نرجس» عبهر.  (کد.) چشم معشوق. ی بت (کن.)  توا رگس بینا: (کد.) چشم. نرگس  دزم: ( کد.) ) چشم خشمگین. ۳9  (گی.) نسرین. ن گس ژوزفین: (گیاء) یکی از  گونه‌های برگس که بنام برونسویجی نیز
---
MON_part2.txt | ود که  زیبایی خاصی به گل این گیاه می‌دهد. در  بعضی گونه‌های نرگس خود گل نیز زرد  رنگ است؛ نرگس شهلاه نرجس» عبهر.  (کد.) چشم معشوق. ی بت (کن.)  توا رگس بینا: (کد.) چشم. نرگس  دزم: ( کد.) ) چشم خشمگین. ۳9  (گی.) نسرین. ن گس ژوزفین: (گیاء) یکی از  گونه‌های برگس که بنام برونسویجی نیز  1 ترگس نیم خواب: (کد.) چشم  
---
MON_part2.txt | د  رنگ است؛ نرگس شهلاه نرجس» عبهر.  (کد.) چشم معشوق. ی بت (کن.)  توا رگس بینا: (کد.) چشم. نرگس  دزم: ( کد.) ) چشم خشمگین. ۳9  (گی.) نسرین. ن گس ژوزفین: (گیاء) یکی از  گونه‌های برگس که بنام برونسویجی نیز  1 ترگس نیم خواب: (کد.) چشم  معشوق. نرگس و گل: (کد.) چشم و گوش  معشوق. ۰ نرگس بعقوبی: (گیا.) یکی از  گونه‌ه
---
MON_part2.txt | ن: (گیاء) یکی از  گونه‌های برگس که بنام برونسویجی نیز  1 ترگس نیم خواب: (کد.) چشم  معشوق. نرگس و گل: (کد.) چشم و گوش  معشوق. ۰ نرگس بعقوبی: (گیا.) یکی از  گونه‌های نرگس که بنام زنبق یعقوبی نیز  مشهور است. نوعی پارچه» ن رگسی.  نرگسی: آ-6ع۱2 (ص‌سسه..) مسوب به  نرگس. نرگسی را بستن و فسفسی را باز  کردن: (عم.) (ک:
---
MON_part2.txt | ام برونسویجی نیز  1 ترگس نیم خواب: (کد.) چشم  معشوق. نرگس و گل: (کد.) چشم و گوش  معشوق. ۰ نرگس بعقوبی: (گیا.) یکی از  گونه‌های نرگس که بنام زنبق یعقوبی نیز  مشهور است. نوعی پارچه» ن رگسی.  نرگسی: آ-6ع۱2 (ص‌سسه..) مسوب به  نرگس. نرگسی را بستن و فسفسی را باز  کردن: (عم.) (ک:.) به خواب رفتن  (فرعا.جما.) چشمکد. (
---
MON_part2.txt | د.) چشم  معشوق. نرگس و گل: (کد.) چشم و گوش  معشوق. ۰ نرگس بعقوبی: (گیا.) یکی از  گونه‌های نرگس که بنام زنبق یعقوبی نیز  مشهور است. نوعی پارچه» ن رگسی.  نرگسی: آ-6ع۱2 (ص‌سسه..) مسوب به  نرگس. نرگسی را بستن و فسفسی را باز  کردن: (عم.) (ک:.) به خواب رفتن  (فرعا.جما.) چشمکد. (.) نوعی پارچه  لطیف گرانبها» نرگس. خو
---
MON_part2.txt | بی: (گیا.) یکی از  گونه‌های نرگس که بنام زنبق یعقوبی نیز  مشهور است. نوعی پارچه» ن رگسی.  نرگسی: آ-6ع۱2 (ص‌سسه..) مسوب به  نرگس. نرگسی را بستن و فسفسی را باز  کردن: (عم.) (ک:.) به خواب رفتن  (فرعا.جما.) چشمکد. (.) نوعی پارچه  لطیف گرانبها» نرگس. خورشی است که با  تخم‌مرغ زده و پیاز خرد کرده در روغن  سرخ کرده ت
---
```


## [2026-09-07T19:38:19.314Z] TOOL CALL #64: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg362hi.png'); w,h=im.size\nim.crop((int(0.18*w),int(0.485*h),int(0.80*w),int(0.530*h))).save('$S/p362_empty.png')\n\""
}
```


### [2026-09-07T19:38:20.803Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T19:38:24.076Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p362_empty.png"
}
```


### [2026-09-07T19:38:24.137Z] TOOL RESULT

```

```


## [2026-09-07T19:38:24.135Z] INPUT

[Image: original 2108x198, displayed at 2000x188. Multiply coordinates by 1.05 to map to original image.]


## [2026-09-07T19:38:29.180Z] TOOL CALL #66: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-07T19:38:29.217Z] TOOL RESULT

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


## [2026-09-07T19:38:30.611Z] TOOL CALL #67: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg362.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/362.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/362.png"
}
```


### [2026-09-07T19:38:30.672Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 76202 Sep  7 15:38 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/362.png
```


## [2026-09-07T19:38:33.574Z] TOOL CALL #68: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-07T19:38:33.648Z] TOOL RESULT

```
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


## [2026-09-07T19:38:48.846Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"'asta-  n.  'Heim,  Heimst\")\nprint('found at',i, 'leaf', t[:i].count('\\f'))\nleaf=t[:i].count('\\f')\npages=t.split('\\f')\n# print numbers on that leaf and neighbours\nfor n in range(leaf-1,leaf+2):\n    print(n, re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$',pages[n])[:6], ' '.join(pages[n].split())[:100])\nEOF"
}
```


### [2026-09-07T19:38:50.151Z] TOOL RESULT

```
found at 609971 leaf 149
148 [] sla.. V.J. 20; Y. 3.16, S. 7.28, 2.28; — äat . . vazaite väiS . . avi 'sä avi /gi'irS ai-i karh'ä yä
149 ['314'] g'. — 1) Die hergebrachle Verbindung mii ai. iuna- n. "Leere' halle ich für weniger wahrscheinlich. 
150 [] vispäi dräjS dimänäi 'tayj ". .; sie, die! Gesellen im3> Haus der Drvg fUr alle Zeit" Y. 40. II. a)
```


## [2026-09-07T19:38:56.416Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5765,5795p' BRT.txt | cut -c1-200"
}
```


### [2026-09-07T19:38:56.465Z] TOOL RESULT

```
•  g.  a-siStay-"  f.  1) 'Verheissung  auf-' (Akk.):  iä^ä  mSt  yqm  yaoi  damam  yaoz- däm  yqm  *Aud3naos  paiüh  saüyat  xsa- %raAya  xnlvä  xsaira  %wSvqs  °tls  (AP.) mazda  "ob  mir  
Zum  V.  !3A-.  —  Zur  Et,  Bed.  und  zdSt.  s. Bthl.  AF.  2.  169,  3-  is,  Gdn.  BB.  /2.  99, JüSTI  PrJ.  SS.  234.  —  Pü.:  ti:,  fri  IH;  Ver- wechslung mit  äsisla-,  —  ')  Mit 
•  g.  a-süna-  Adj,  'erfolgreich':  a/  vs xsmaibya  'ttil  valda  sfarafyyl  (sd  )  vainlyä travä  Y.2Ä'.io.
Eig.  'der  beim  Erfolg  ist'i).  —  ai.  suiiä.  n. ■Erfolg".  —  Vßl.  sfä:  —  Pü.:  +a;«/o*(?)'), Sü.:  analasak  'fleissig'.  —  1)  Die  hergebrachle Verbindung  mii  ai.  iuna
'asta-  2 1 1
'iSsüa  (AP.)'"'  vans^sia  *mastrr}nasca  .  . z^mäoa  hqm.raiiiwayaii  Yt  to.jx;  —  fisii 'tarn  nSit  varsqm  pairi.späili  \.6.2q;   7;
—  yai  nsit  sün}  .  .  a3atf/iqm  °tqm  .  . bannhm  (sA.) /rafasqn  V,  6.46;  —  'ti'a (AP.)  gaonaca  *dmi}'iaca  Ytij.  11;  —  yS süne  .  .  'tanqm'-''  (als  Obj.)  ahmarslanqm da',
'<n'a.^/-p>/J/(sd.)V.^5o;  51.  a)  Sing. und  Plur.  'Knochenbau  des  Leibes':  "/J *hutal{lm  . .  lanvö  *huraomm  (sd.)  P.  4^;
—  vlsph  gaüäsca  tanvas.'a  atdiblsca  (als Obj.)  uitäiiqs^a  kihrpas^a  trvliJica  Y.  55, 1.  a)  überhaupt  'stofflicher  Leib'  im Gegensatz  zu  uUäna-  oder  baoriah-:  nöit "laca "  
KompA.;  Ableit.  —  Vgl.  'aslay-,  asimtäl:  — iFlei.  s.  %39r.  —  ai.  äslhi,  ixilhnäk;  mp.,  np. an.  ~  Pü.:  ait,  (lU  V.  4.  $0,  51  und  zu  a): Mn.  —  'I  Thein.  —  ') 
•  g.  a-süra-  Adj.  'unstark,  unvcnnögend': yj  anass»m  xsqnmJng  (sd.)  raditn  *vaHm n?ris  'rahya  V.2_9.<).
gr.  J*vii,-.  —  Vgl.  asis-iila-.  —  Pü.;  an apzar«!)  ™J,  Sü.;  aiäähaimlJyai. ^  i)  Vgl. nnler  iura-  No.  2.
•  j.  a-skvnda-  Adj.  (fem.  'da-)  'ohne körperlichen  Schaden,  ohne  Gebrechen': kanyqm  °dqm  anupayatqm  "ein  Mädchen ohne  Gebrechen,  das  noch  unberührt  ist" Y./^.iS.
Pü. :  aiiaiid,  erl. :  drusi  'gesund'.
•  j.  asCav-  m.  'Unterschenkel,  Wade'; dasitijm  (hSyum)  ks  °cüm'^  V.Ä63— 65*,
KompE.  —  Vgl.  gr.  4)^5;,  ann-  cj.fr.  —  ■) /  S  22  mit  No.  a,
•  j.,  g.  ast-  n.  'Knochen',  von  Menschen und  Tieren:  _>'J  °/j«"  upanh}r?zaUi  siinS vä  .  .  masyehe  vä  V.  t/.io;  5.1Ö,  F._y  i;  — kva  narqm  iriitanqm  azdibls  (als  Obj.
NA.  a
\.  "asta':  yezi  asta  asa  xrdiwa  yezt asia  gas>^aby3  V./?.39.
KachPü,  zii'<i^.{3SPrM.?):  hatar  ast  aAr.U-iA hiS  xral  iieu'ai  haJtar  asl  kai  5  gchän  ofe päii  iu  pa  fräröiith  däict,
j.  'asta-  n.  'Heim,  Heimstätte':  *'tjm^'' ii^ra  fracarsnta pasvas^a  staoräca  masyäca "ein  Heim  schafften  sich  da  Kleinvieh  und Grossvieh  und  Menschen"  V.  2. 1 3.  a)  ins- bes,  v
Zum  ai.  V.  tiasali;  BtHU  KZ.  29.  483.  —  ai. isla-  n.,  mp.  pah-asl'i,  GOR,  OK.  346,  Bthl. BB.  13.  7a.  —  Vgl.  a»ha:  —  Pü.  {lu  V.  14): /nArtj/"),  (zu  V.  2) :  cigön 
dby  Google
*asti.aoJah-
314
faiiä.hasta-.  —  J)  Die  ZerreiEsung  findet  ihre Erklärung  durch  V.  g.  48,  wo  riehtig;  yi&a fata  ahmSj  as;  Aä, .  ,
•  j.  'asta-  Adj.  (fem.  'iä-),  PPfP.:  s.  'aA-. KompE.
•  j.  astaena-  Adj.  'aus  Knochen,  aus Bein  gemacht,  beinern':  nlif  °naeiiya {hszanaäbya)  .  .  ratufriS  N.  /07.
Ableit  aus  as!-.  —  mp.  (Pü.):  asien.
•  ].,  g.  'astay-  m.  'Geselle,  Genosse'' aarahe  mainySus  'ti^(ä\  P.j2'*;  —  y} atsm  drygvaile  .  .  varilaitJ  vaahäu  vä tSi>ain  (sd)  'nm*>  \-33.2;  —  drüjö (bmitni  Aaüya 
li.  ve'-  ätilAay  m.  'Gast';  BtHL.  BB.  1$.   1°,
```


## [2026-09-07T19:41:05.984Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LAT/LEW narcissus ==\"; grep -n -i \"narcissus\" LAT.txt LEW_1910.txt | head -4; echo \"== HRN/HUB navus ==\"; grep -n -i \"nawus\\|navus\\|nāwūs\\|Grabmal\" HRN.txt HUB.txt | head -5; echo \"== FSD narcissus/harness ==\"; grep -n -i \"narcissus,  n\\|^harness\" FSD_vol3.txt FSD_vol2.txt | head -4; echo \"== WEB harness ==\"; grep -n \"^harness\" WEB_vol1.txt | head -3"
}
```


### [2026-09-07T19:41:06.121Z] TOOL RESULT

```
== LAT/LEW narcissus ==
== HRN/HUB navus ==
HUB.txt:9703:p. 74. Hier felilt up. (parsiscli!) sutoddn 'Grabmal*
== FSD narcissus/harness ==
FSD_vol3.txt:56540:Harness-irimmings, harm ss-iurniture 3. i'he uei or
FSD_vol3.txt:69226:harness of the horses - iin, over, oi in the n. of, lu Imme-
FSD_vol3.txt:206566:harnessed four abreast, hauled by four horses luirncvHed
FSD_vol2.txt:64552:harness,  about  18  Inches  above  which  project  sidewise  1 flexible  arms  of  wlialebone  or  rubber  to  which  the  bridle- reins  are  attached.— joct'ey-boot",  n.  A   top-boot.— j.» box,  71.  A   box  under  a   wagon-seat  for  carrying  small articles.— J. -cap,  n.  A   light  cap  with  a   long  vfeor.— j.«
== WEB harness ==
```


## [2026-09-07T19:43:36.088Z] AGENT

Now I'll write the verification file.


## [2026-09-07T19:51:35.513Z] TOOL CALL #72: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk362.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_NARK = \"https://en.wiktionary.org/wiki/%CE%BD%CE%AC%CF%81%CE%BA%CE%B9%CF%83%CF%83%CE%BF%CF%82\"\nW_NARG = \"https://en.wiktionary.org/wiki/%D9%86%D8%B1%DA%AF%D8%B3\"\nW_NAWU = \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%88%D9%88%D8%B3\"\nE_HARN = \"https://www.etymonline.com/word/harness\"\nW_NES  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/nes-\"\nW_NARROW = \"https://en.wiktionary.org/wiki/narrow\"\n\nPOK_SNER = (\"Pokorny, IEW pp. 975-977, 'Root/lemma: (s)ner-2, Meaning: to turn, wind, etc.' \"\n            \"(POK_full.txt line 79010; grep -n 'lemma: (s)ner-2')\")\nPOK_NES  = (\"Pokorny, IEW pp. 766-767, 'Root/lemma: nes-, Meaning: to join with; to conceal oneself' \"\n            \"(POK_full.txt line 62783; grep -n 'lemma: nes')\")\n\ndoc = {\n  \"pdf_page\": 362,\n  \"book_page\": 332,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ner 2, Nerq, Sner, Snerq\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *(s)ner- 'to turn, wind, twist, bind together', with the k-enlargement *(s)ner-k-/*(s)nor-k-\",\n      \"note\": (\"Pokorny 2. (s)ner- 'to turn, wind' pp. 975-977 (Nourai's POK:975 is its first page) and \"\n               \"Klein p. 1028 s.v. narcotic, which prints exactly Nourai's four-name set: 'fr. I.-E. *(s)ner-q-, \"\n               \"\\\"to turn, twist\\\" ... I.-E. *(s)ner-q- is a -q-enlargement of base *(s)ner-, \\\"to turn, twist, bind \"\n               \"together\\\", whence OE. sneare, \\\"snare\\\", nearu, \\\"narrow\\\"'. Root name, language label and gloss are \"\n               \"therefore all correct (Ner 2 = *ner-, Nerq = *nerk-, Sner = *sner-, Snerq = *snerk-). Watkins/AHD \"\n               \"gives the same root as '(s)ner-. To wind, twist.' One branch of the chart does NOT belong to it: the \"\n               \"flower name narkissos (nodes #1 second word, #2, #3, #4, #5) is a Pre-Greek plant name only \"\n               \"secondarily attached to narke by folk etymology (Beekes, Klein), so the whole narcissus/narges branch \"\n               \"hangs on that ancient folk etymology rather than on the IE root. Pokorny's own p. 975 also carries a \"\n               \"homophonous root (s)ner-1 'to murmur, grumble', which is not what Nourai means.\"),\n      \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *(s)ner- / *(s)nerk- به معنی «تابیدن، پیچیدن، تنگ کردن» است؛ پوکورنی آن را در \"\n                  \"صفحه‌های ۹۷۵ تا ۹۷۷ زیر «۲. (s)ner-: drehen, winden» آورده و کلاین (ص ۱۰۲۸) همان چهار صورتی را دارد که \"\n                  \"نورایی نام برده است: ستاک *(s)ner- و گسترش ‑q آن، یعنی *(s)ner-q-. پس نام ریشه، برچسب زبانی و معنای آن \"\n                  \"درست است و ادعای نورایی در این حد پذیرفتنی است. تنها ایراد بنیادی آن است که نام گل narkissos به این ریشه \"\n                  \"تعلق ندارد: بیکس آن را واژه‌ای پیش‌یونانی می‌شمارد و کلاین می‌گوید تنها «به narkē همگون شده است»، یعنی \"\n                  \"شاخهٔ نرگس بر ریشه‌شناسی عامیانه استوار است.\"),\n      \"sources\": [W_NARK, W_NARROW],\n      \"ref_check\": [\n        {\"ref\": \"POK:975\", \"status\": \"supports\",\n         \"note\": POK_SNER + \": 'Meaning: to turn, wind, etc.. Note: perhaps extension to sne- ds.' The entry contains \"\n                 \"the Germanic and Greek material Nourai uses (OE nearu 'narrow' *nar-wa- 'actually zusammengeschnuert'; \"\n                 \"gr. narke 'das solidification, cramp'; OHG snar(a)ha 'loop, noose, snare'). It does NOT mention narkissos.\"},\n        {\"ref\": \"KLN:1028\", \"status\": \"supports\",\n         \"note\": \"KLN_1966.txt leaf 550 (the leaf carries the printed numeral '1028'), s.v. narcotic: 'fr. vipx-i] \"\n                 \"[narke], \\\"numbness\\\", prop. \\\"a cramp\\\", fr. I.-E. *(s)ner-q-, \\\"to turn, twist\\\" ... a -q-enlargement of \"\n                 \"base *(s)ner-, \\\"to turn, twist, bind together\\\", whence OE. sneare, \\\"snare\\\", nearu, \\\"narrow\\\"'. Nourai's \"\n                 \"root name and gloss are lifted verbatim from this page.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II pp. 699-701 ((s)ner-)\", \"stance\": \"supports\",\n         \"note\": \"WLD_Bd2_pages.txt leaves 703-704: '(s)ner-' with 'ahd. snuor \\\"Schnur, Band, Seil\\\", got. snorjo \"\n                 \"\\\"geflochtener Korb\\\", ags. sner (*snorio) \\\"Saite einer Harfe\\\"' and the -k-/-g-/-p- extensions; Pokorny's \"\n                 \"'WP. II 699 ff.' reference checks out.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)ner-\", \"stance\": \"supports\",\n         \"note\": \"AHD_watkins1985.txt line 975: '(s)ner-. To wind, twist. 1. Suffixed extended zero-grade form *snork- \"\n                 \"in Germanic *snarh-on- ... 3. Extended variant form *(s)nark- in Greek narke, cramp, numbness: NARCO-, \"\n                 \"NARCOSIS, NARCOTIC. [Pok. 2. (s)ner- 975.]' Same root, same gloss; narcissus is absent.\"},\n        {\"src\": \"SYN\", \"where\": \"12.62 NARROW, p. 886\", \"stance\": \"partial\",\n         \"note\": \"Buck: 'OE nearu, ME narowe, NE narrow, OS naru : ON Norva-sund ..., OHG narwa \\\"scar\\\" (i.e. \\\"closed \"\n                 \"wound\\\"), prob. fr. a root meaning \\\"draw together, tie\\\"(?) in OHG snuor \\\"band, string\\\" ... Walde-P. \"\n                 \"2.699 f.' - same root, but Buck marks it with a question mark.\"},\n        {\"src\": \"IEC\", \"where\": \"s.v. noruos, sneru- (IEC.txt lines 11855, 16553)\", \"stance\": \"partial\",\n         \"note\": \"Mann files OHG narwa / MHG narwe 'scar' and Lith. narvas 'cell of honeycomb' under 'noruos \\\"incision, \"\n                 \"groove ... character, habit\\\"' and cross-refers snorb-; he does not set up Nourai's single root name.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Greek\",\n          \"words\": \"narke; narkissos\",\n          \"verdict\": \"disputed\",\n          \"derivation\": (\n            \"narke: Greek narke (nark-e) 'numbness, torpor, cramp' (Hippocrates, Aristotle; also the name of the electric \"\n            \"ray, 'Krampfrochen') is the regular *-k-/-q- enlargement of *(s)ner- 'to twist, constrict'. Pokorny 976-977 \"\n            \"files it under the extension '*sner-k-' beside Armenian nork'oy 'thin, slender' (< '*zusammengeschnuert') and \"\n            \"OHG snar(a)ha 'noose, snare', ON snara 'to twist, coil', the semantics running 'be drawn tight/constricted' > \"\n            \"'stiffness, cramp' > 'numbness'; the denominal verb narkoun/narkoo 'to benumb' and its verbal adjective \"\n            \"narkotikos are what feed Nourai's French/English narcotic branch. This word is confirmed. \"\n            \"narkissos: the flower name is a different matter and the chart's arrow is wrong. Neither Pokorny (in the whole \"\n            \"of 975-977) nor Watkins lists it under the root; Klein, on the very page Nourai cites, writes 'Gk. narkissos, \"\n            \"\\\"narcissus\\\", which is prob. of Aegean origin but was assimilated to narke, \\\"numbness\\\" (in allusion to the \"\n            \"sedative properties of this plant)'; Beekes (EDG s.v.) holds that the -issos suffix 'clearly points to a \"\n            \"Pre-Greek word' and that the narke connection is 'due to folk etymology' - an ancient one, already argued by \"\n            \"Plutarch and Pliny (NH 21.75) from the plant's narcotic scent. So narkissos is a pre-Greek (Aegean/Anatolian) \"\n            \"plant name, and everything Nourai hangs below it (Pahlavi narkis, Persian narges, Latin/English narcissus) is \"\n            \"a real chain of borrowings but not a chain of descent from *(s)ner-. Verdict for the node = the worse of the \"\n            \"two: disputed.\"),\n          \"derivation_fa\": (\n            \"یونانی νάρκη (narkē) «بی‌حسی، گرفتگی، کِزکردگی» بازماندهٔ منظم گسترش ‑k ریشهٔ *(s)ner- است؛ پوکورنی (ص ۹۷۶–۹۷۷) \"\n            \"آن را زیر «*sner-k-» در کنار ارمنی nork'oy «نازک» و آلمانی علیای باستان snar(a)ha «کمند» می‌آورد و تحول معنایی \"\n            \"آن «به‌هم‌کشیده شدن» → «گرفتگی» → «بی‌حسی» است؛ از فعل ναρκοῦν «بی‌حس کردن» صفت ναρκωτικός و از آن narcotic \"\n            \"بیرون آمده است. اما νάρκισσος چنین نیست: نه پوکورنی و نه واتکینز آن را زیر این ریشه نیاورده‌اند، کلاین در همان \"\n            \"صفحهٔ ۱۰۲۸ آن را «به احتمال از خاستگاه اژه‌ای» می‌داند که تنها «به narkē همگون شده است»، و بیکس پسوند ‑ισσος را \"\n            \"نشانهٔ روشن واژهٔ پیش‌یونانی می‌شمارد. پس پژوهش امروزی این حلقه را رد می‌کند و آن را ریشه‌شناسی عامیانه (که \"\n            \"پیشینه‌اش به پلوتارک و پلینی می‌رسد) می‌داند؛ زنجیرهٔ وام‌گیریِ پس از یونانی (پهلوی، فارسی، لاتینی، انگلیسی) درست \"\n            \"است ولی پیوند آن با ریشهٔ هندواروپایی نادرست.\"),\n          \"sources\": [W_NARK],\n          \"ref_check\": [\n            {\"ref\": \"POK:975\", \"status\": \"partial\",\n             \"note\": POK_SNER + \": has 'gr. varkh [narke] \\\"das solidification, cramp, Lahmung; Krampfrochen\\\"' under the \"\n                     \"*sner-k- extension (p. 976-977), i.e. it supports narke; a full-text read of the entry shows no \"\n                     \"narkissos, so it does not support the flower.\"},\n            {\"ref\": \"KLN:1028\", \"status\": \"partial\",\n             \"note\": \"KLN_1966.txt leaf 550: narcotic is derived 'fr. narke ... fr. I.-E. *(s)ner-q-' (supports), but the \"\n                     \"adjacent entry 'Narcissus, n., a genus of bulbous plants' reads 'L. narcissus, fr. Gk. narkissos, \"\n                     \"\\\"narcissus\\\", which is prob. of Aegean origin but was assimilated to narke' - Klein contradicts the \"\n                     \"flower's descent from the root.\"},\n            {\"ref\": \"SKT:344\", \"status\": \"partial\",\n             \"note\": \"Skeat does say what Nourai wants - s.v. 'narcissus, a flower. (L. - Gk.) L. narcissus. - Gk. \"\n                     \"narkissos; named from its narcotic properties' and s.v. SNARE 'a base SNARH = Aryan SNARK, cf. Gk. \"\n                     \"narke, cramp; see Narcissus' - but the page number does not fit the available edition: in the 1911 \"\n                     \"corrected impression (SKT.txt) narcissus falls on p. 301 (leaf 325) and Snare on p. 447 (leaf 472), \"\n                     \"while p. 344 (leaf 368) carries 'Per-, through / Petition'.\"},\n            {\"ref\": \"PRT:427\", \"status\": \"not_checked\",\n             \"note\": \"Partridge, Origins (1958) is lending-only on archive.org (refs_online.json kind=archive_restricted); \"\n                     \"no readable copy.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)ner-, para 3\", \"stance\": \"partial\",\n             \"note\": \"'Extended variant form *(s)nark- in Greek narke, cramp, numbness: NARCO-, NARCOSIS, NARCOTIC' - \"\n                     \"supports narke, and pointedly does not list NARCISSUS among the English words of this root.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 699 ff.\", \"stance\": \"partial\",\n             \"note\": \"The (s)ner- article gives the -k- extension material (snarken/snerka/snirkt etc.) and the 'cord' \"\n                     \"words but no Greek flower name; grep 'narkiss' in WLD_band3.txt and WLD_Bd2_pages.txt is silent.\"},\n            {\"src\": \"SKT\", \"where\": \"p. 301 s.v. narcissus; p. 447 s.v. Snare\", \"stance\": \"partial\",\n             \"note\": \"Skeat still holds the 19th-c. view ('named from its narcotic properties'), which is exactly the folk \"\n                     \"etymology modern Greek etymology (Beekes, Chantraine) rejects.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"narkis\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\n            \"Middle Persian nrgs, read nargis, 'narcissus' is attested and is a loan of Greek narkissos. MacKenzie, \"\n            \"A Concise Pahlavi Dictionary, prints 'nargis [nlgs | N ~] narcissus' (PHD.txt line 499), and Mo'in's \"\n            \"etymological footnote 6 to Borhan-e Qate' p. 2129 - the page Nourai cites - says in so many words 'Pahlavi \"\n            \"narkis ... from Greek narkissos; its Arabicized form is narjes; Latin narcissus, French narcisse'. The one \"\n            \"refinement modern work adds is a way-station: Huebschmann, Persische Studien p. 239, lists 'Lehnwort nargis \"\n            \"aus *narkis = syr. nrqys = gr. narkissos', i.e. the Greek word came into Iranian through Classical Syriac \"\n            \"narqis (as Wiktionary also has it, alongside Old Armenian nergis); Syriac qop is what Nourai's -k- reflects, \"\n            \"and it was voiced to -g- in Middle Persian (nargis), the spelling MacKenzie prints. Greek -o- of the \"\n            \"second-declension ending was simply dropped, and Greek -ss- simplified. So the Greek > Pahlavi arrow is right; \"\n            \"only the Aramaic middleman is missing from the chart.\"),\n          \"derivation_fa\": (\n            \"فارسی میانه (پهلوی) nrgs / nargis «نرگس» وام‌واژه‌ای است از یونانی νάρκισσος؛ مکنزی در فرهنگ کوچک پهلوی «nargis \"\n            \"[nlgs] narcissus» را می‌آورد و معین در حاشیهٔ برهان قاطع ص ۲۱۲۹ — همان صفحه‌ای که نورایی ارجاع داده — می‌نویسد \"\n            \"«پهلوی narkis ... از یونانی narkissos؛ معرّب آن نرجس». هوبشمان در پژوهش‌های فارسی ص ۲۳۹ راه وام‌گیری را دقیق‌تر \"\n            \"می‌کند: «vam-vāžeh nargis از *narkis = سریانی nrqys = یونانی νάρκισσος»، یعنی یونانی → سریانی narqīs → پهلوی؛ \"\n            \"قافِ سریانی همان ‑k نورایی است که در فارسی میانه به گ نرم شده و ‑ss‑ یونانی ساده شده است. ادعای نورایی درست است و \"\n            \"تنها ایستگاه سریانی در نمودار نیامده است.\"),\n          \"sources\": [W_NARG, W_NARK],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2129\", \"status\": \"supports\",\n             \"note\": \"Borhan-e Qate' vol. 4, printed p. 2129 = pdf page 212 (BQT_v4_pages.txt leaf 211; verified with \"\n                     \"tools/ref_page.py-style page arithmetic printed = pdf + 1917 and with the running-head numeral). \"\n                     \"Mo'in's footnote to the entry نرگس reads: «پهلوی narkis ... از یونانی narkissos ... معرب آن نرجس. \"\n                     \"رک: دزی ج۲ ص۵۹۵ ... narcissus (لاتینی) ... narcisse (فر)» - exactly Nourai's arrow, plus the Latin and \"\n                     \"French continuations he draws in nodes #4-#7.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p. 57 s.v. nargis (PHD.txt line 499)\", \"stance\": \"supports\",\n             \"note\": \"'nar [ZKL < A shr; nl | M nr, N ~] male, manly. nargis [nlgs | N ~] narcissus.' - the Pahlavi word \"\n                     \"exists, spelt nlgs, transliterated nargis (not narkis).\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p. 239 (HUB.txt leaf 249)\", \"stance\": \"partial\",\n             \"note\": \"'Lehnwort nargis aus *narkis = syr. [nrqys] = gr. varkiaaos u. s. w.' - supports the Greek origin but \"\n                     \"inserts Syriac, which Nourai's chart omits.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (Glossary)\", \"stance\": \"silent\",\n             \"note\": \"grep -n -i 'nargis|narkis' NYB_vol2_glossary.txt returns nothing; Nyberg's glossary covers only the \"\n                     \"texts he edits, so the flower name is absent.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"narges; nargeseh; nargesi\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\n            \"New Persian نرگس narges continues Middle Persian nargis with no change beyond the regular NP raising/lowering \"\n            \"of the short vowel in the second syllable. Borhan-e Qate' p. 2129 (the cited page) has all three of Nourai's \"\n            \"words: نرگس 'گلی است معروف ... و کنایه از چشم معشوق' (the flower; metaphorically the beloved's eye); نرگسه, \"\n            \"formed with the nominal suffix -eh, glossed 'و بر مقعر خانه‌ها نصب کنند ... و کنایه از ستاره‌های آسمانی است - و \"\n            \"پروین را نیز گفته‌اند' = 'ornamental stud; figuratively the stars of heaven, also the Pleiades', which is \"\n            \"Nourai's 'star, sky' and is exactly what the chart's verse by 'Amid Lobaki plays on (گرد نرگس‌دان گردون بین \"\n            \"هزاران نرگسه); and نرگسی 'جنسی از جامه باشد که پوشند - و نوعی از طعام که خورند', with Mo'in's footnote 8 \"\n            \"describing the dish - eggs beaten with chopped onion fried in oil, sometimes with spinach - 'named nargesi از \"\n            \"جهت شباهت اجزای وی به نرگس', i.e. from its resemblance to the flower's white-and-yellow eye. Mo'in's Farhang-e \"\n            \"Farsi s.v. نرگس marks نرجس as its Arabicized doublet and s.v. نرگسی gives both the fabric and the egg dish. All \"\n            \"three words, their language label and their glosses check out.\"),\n          \"derivation_fa\": (\n            \"«نرگس» فارسی نو همان nargis فارسی میانه است، بی هیچ دگرگونی آوایی چشمگیر. برهان قاطع (ص ۲۱۲۹) هر سه واژهٔ نمودار \"\n            \"را دارد: «نرگس» «گلی است معروف ... و کنایه از چشم معشوق»؛ «نرگسه» (با پسوند ‑ه) «کنایه از ستاره‌های آسمانی است - \"\n            \"و پروین را نیز گفته‌اند» که همان «ستاره، آسمان» نورایی است و بیت عمید لُبکی در نمودار بر همین بازی می‌کند؛ و \"\n            \"«نرگسی» «جنسی از جامه باشد که پوشند - و نوعی از طعام که خورند»، با این حاشیهٔ معین که آن خورش از تخم‌مرغ زده و \"\n            \"پیاز خردکردهٔ سرخ‌شده است و «از جهت شباهت اجزای وی به نرگس» چنین نام گرفته. معین در فرهنگ فارسی نیز «نرجس» را \"\n            \"معرّبِ آن و «نرگسی» را هم نام پارچه و هم نام همان خورش می‌آورد. ادعای نورایی درست است.\"),\n          \"sources\": [W_NARG],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2129\", \"status\": \"supports\",\n             \"note\": \"BQT_v4_pages.txt leaf 211 (= printed p. 2129): entry «نرگس» with «کنایه از چشم معشوق»; «نرگسه ... \"\n                     \"وکنایه از ستاره‌های آسمانی است - و پروین را نیز گفته‌اند»; «نرگسی - بروزن مجلسی، جنسی از جامه باشد که \"\n                     \"پوشند - و نوعی از طعام که خورند»; and footnote 7 prints the very verse the chart quotes.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. نرگس / نرگسی (MON_part2.txt; Adena 2-vol reprint)\", \"stance\": \"supports\",\n             \"note\": \"«[... نرجس معر.] (اِ.) (گیا.) گیاهی است از رده تک‌لپه‌ای‌ها ... نرگس شهلا، نرجس، عبهر. (کذ.) چشم معشوق» \"\n                     \"and «نرگسی: nargesī ... منسوب به نرگس ... (اِ.) نوعی پارچه لطیف گرانبها، نرگس. خورشی است که با تخم‌مرغ \"\n                     \"زده و پیاز خرد کرده در روغن سرخ کرده ...» - confirms both the fabric and the food sense.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p. 239\", \"stance\": \"supports\",\n             \"note\": \"lists NP nargis among the loanwords whose -g- goes back to a foreign -k-: 'Lehnwort nargis aus \"\n                     \"*narkis = syr. nrqys = gr. narkissos'.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha (ARY_pages.txt / ARY_latin_index_pages.txt)\", \"stance\": \"silent\",\n             \"note\": \"grep 'نرگس' and 'NARCISSUS/NARGES' in both Aryanpur files returns nothing - the book covers inherited \"\n                     \"IE vocabulary, not Greek loanwords.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie\", \"stance\": \"silent\",\n             \"note\": \"grep -n -i 'narkis|nargis|Narzisse' HRN.txt returns nothing.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": (\n            \"An empty pass-through box: it stands for Latin narcissus, the word the English node #5 below is drawn from. \"\n            \"Klein p. 1028 (Nourai's own reference here) gives it directly: 'L. narcissus, fr. Gk. narkissos, \\\"narcissus\\\"'; \"\n            \"the mythological name is likewise 'L., fr. Gk. Narkissos'. Latin took the name over with the plant in the late \"\n            \"Republic/early Empire (Vergil, Georgics 4.122 narcissi; Pliny, NH 21.25, 21.75), keeping the Greek stem and \"\n            \"substituting the Latin -us ending. Two reservations make this plausible rather than confirmed: (a) the arrow is \"\n            \"drawn straight from the Indo-European root, but Latin has no inherited reflex of *(s)ner- here - narcissus is \"\n            \"purely a Greek loan, and Walde-Hofmann/Ernout-Meillet do not treat it as Latin etymological material (grep \"\n            \"'narcissus' in LEW_1910.txt and LAT.txt is silent); (b) because narkissos itself is Pre-Greek, this whole \"\n            \"branch is attached to the root only by the ancient folk etymology with narke.\"),\n          \"derivation_fa\": (\n            \"این جعبهٔ خالیِ «لاتینی» جای narcissus لاتینی را دارد که گرهٔ انگلیسی بعدی از آن گرفته شده است. کلاین (ص ۱۰۲۸، \"\n            \"همان مرجع نورایی) می‌نویسد «L. narcissus, fr. Gk. narkissos»؛ لاتینی این نام را همراه خودِ گل در پایان دورهٔ \"\n            \"جمهوری و آغاز امپراتوری گرفت (ویرژیل، گئورگیکا ۴٫۱۲۲؛ پلینی ۲۱٫۲۵) و تنها پایانهٔ ‑us لاتینی را جانشین پایانهٔ \"\n            \"یونانی کرد. دو نکته آن را به «با احتیاط پذیرفتنی» فرومی‌کاهد: نخست اینکه پیکان یکسر از ریشه کشیده شده، حال آنکه \"\n            \"لاتینی این واژه را تنها به وام دارد (والده–هوفمان و ارنو–مه‌یه آن را مادهٔ ریشه‌شناختی لاتینی نمی‌دانند)؛ دوم اینکه \"\n            \"چون خودِ narkissos پیش‌یونانی است، پیوند این شاخه با ریشهٔ هندواروپایی بر ریشه‌شناسی عامیانه استوار است.\"),\n          \"sources\": [W_NARK],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1028\", \"status\": \"partial\",\n             \"note\": \"KLN_1966.txt leaf 550: 'Narcissus, n., a genus of bulbous plants (bot.) ... - L. narcissus, fr. Gk. \"\n                     \"narkissos' supports Greek > Latin, but the same sentence continues 'which is prob. of Aegean origin', \"\n                     \"so Klein does not support the arrow from the IE root.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etymologisches Woerterbuch (LEW_1910.txt)\", \"stance\": \"silent\",\n             \"note\": \"grep -n -i 'narcissus' LEW_1910.txt: no hit - the Latin etymological dictionaries do not treat this \"\n                     \"Greek loan.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (LAT.txt)\", \"stance\": \"silent\",\n             \"note\": \"grep -n -i 'narcissus' LAT.txt: no hit.\"},\n            {\"src\": \"SKT\", \"where\": \"p. 301 s.v. narcissus\", \"stance\": \"supports\",\n             \"note\": \"'narcissus, a flower. (L. - Gk.) L. narcissus. - Gk. narkissos' - confirms the Latin link (though \"\n                     \"Skeat's 'named from its narcotic properties' is the folk etymology).\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"narcissus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\n            \"English narcissus is taken straight from Latin: Klein, 'Narcissus, n., a genus of bulbous plants (bot.); (not \"\n            \"cap.) any plant of this genus. - L. narcissus, fr. Gk. narkissos'; the separate entry for the mythological \"\n            \"youth is 'L., fr. Gk. Narkissos ... He pined away with desire and was changed into the flower bearing his \"\n            \"name'. The plant name appears in English herbals from the mid-16th century (Turner, Names of Herbes, 1548) and \"\n            \"becomes the Linnaean genus name; the psychological derivative narcissism is G. Narzissismus, coined by Freud \"\n            \"(Klein, same leaf). The Latin > English step is uncontroversial; what remains disputed is only the ultimate \"\n            \"origin of the Greek word (see node #1).\"),\n          \"derivation_fa\": (\n            \"انگلیسی narcissus یکسره از لاتینی narcissus گرفته شده است — کلاین: «L. narcissus, fr. Gk. narkissos» — و از \"\n            \"میانهٔ سدهٔ شانزدهم در گیاه‌نامه‌های انگلیسی (تِرنر، ۱۵۴۸) دیده می‌شود و سپس نام جنسِ لینه‌ای گیاه شده است؛ نام \"\n            \"اسطوره‌ای Narcissus نیز از Νάρκισσος یونانی است و «نارسیسیزم» ساختهٔ فرویدِ آلمانی‌زبان. این حلقهٔ لاتینی → \"\n            \"انگلیسی بی‌گفت‌وگو درست است و ادعای نورایی در همین حد پذیرفتنی است؛ آنچه محل اختلاف است تنها خاستگاه نهاییِ \"\n            \"واژهٔ یونانی است (گرهٔ ۱).\"),\n          \"sources\": [W_NARK],\n          \"ref_check\": [\n            {\"ref\": \"AHD:872\", \"status\": \"not_checked\",\n             \"note\": \"AHD:872 is a page of the main American Heritage Dictionary (New College ed. 1975/76), which is not \"\n                     \"open online (refs_online.json: only the Indo-European appendix has an open surrogate). Checked the \"\n                     \"surrogate instead: AHD_watkins1985.txt s.v. (s)ner- lists NARCO-, NARCOSIS, NARCOTIC but NOT \"\n                     \"narcissus, consistent with the flower being handled only in the main dictionary.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"leaf 550 (printed p. 1028) s.v. Narcissus (both entries)\", \"stance\": \"supports\",\n             \"note\": \"'L. narcissus, fr. Gk. narkissos, \\\"narcissus\\\"' and 'Narcissus ... - L., fr. Gk. Narkissos.'\"},\n            {\"src\": \"SKT\", \"where\": \"p. 301 s.v. narcissus\", \"stance\": \"supports\",\n             \"note\": \"'narcissus, a flower. (L. - Gk.) L. narcissus. - Gk. narkissos.'\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls (FSD_vol3.txt)\", \"stance\": \"silent\",\n             \"note\": \"grep 'narcissus' in FSD_vol3.txt returns only running text inside other entries; the OCR of this \"\n                     \"volume is too degraded to quote a headword entry.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\n            \"An empty pass-through box standing for French narcotique, the source of English narcotic(s) in node #7. Klein \"\n            \"p. 1028 dates the borrowing exactly: 'F. narcotique, introduced into French in 1314 by Mondeville fr. ML. \"\n            \"narcoticus, fr. Gk. narkotikos, \\\"benumbing\\\", fr. narkoun, \\\"to benumb\\\", fr. narke, \\\"numbness\\\", prop. \\\"a \"\n            \"cramp\\\"'. Henri de Mondeville's surgical treatise is thus the first French attestation, and the word came in as \"\n            \"a medical Latinism, not by popular transmission. The chain root > Gk. narke > narkoun > narkotikos > ML \"\n            \"narcoticus > Fr. narcotique is sound; the chart's arrow straight from the root merely suppresses the Greek and \"\n            \"Medieval-Latin links, which its own node #1 supplies.\"),\n          \"derivation_fa\": (\n            \"این جعبهٔ خالیِ «فرانسوی» جای narcotique فرانسوی است. کلاین (ص ۱۰۲۸) تاریخ آن را هم می‌دهد: «در سال ۱۳۱۴ به دست \"\n            \"موندویل از لاتینی میانه narcoticus به فرانسوی درآمد»، و narcoticus خود از یونانی ναρκωτικός «بی‌حس‌کننده» از \"\n            \"ναρκοῦν از νάρκη است. یعنی واژه از راه لاتینیِ پزشکی وارد فرانسوی شده، نه از راه گفتاری. زنجیرهٔ ریشه → یونانی \"\n            \"→ لاتینی میانه → فرانسوی درست است و ادعای نورایی پذیرفتنی؛ نمودار تنها حلقه‌های یونانی و لاتینی میانه را \"\n            \"نانوشته گذاشته است.\"),\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n             \"note\": \"Nourai gives no reference for this node (refs=None). Checked Klein p. 1028 in its place - see \"\n                     \"consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"leaf 550 (printed p. 1028) s.v. narcotic\", \"stance\": \"supports\",\n             \"note\": \"'F. narcotique, introduced into French in 1314 by Mondeville fr. ML. narcoticus, fr. Gk. narkotikos \"\n                     \"\\\"benumbing\\\", fr. narkoun, \\\"to benumb\\\", fr. narke, \\\"numbness\\\"'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt\", \"stance\": \"silent\",\n             \"note\": \"Skeat's Concise has no separate 'narcotic' headword (grep -n -i 'narcotic' SKT.txt gives only \"\n                     \"incidental uses under bang, mandrake, morphine).\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"narcotics\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\n            \"English narcotic is a 14th-century loan from Old/Middle French narcotique (and its Medieval Latin source \"\n            \"narcoticus), first in Chaucer's Knight's Tale, c. 1385, 'narcotikes and opie of Thebes'; Klein p. 1028 traces \"\n            \"it 'F. narcotique ... fr. ML. narcoticus, fr. Gk. narkotikos' and notes 'For the ending of narcotic see suff. \"\n            \"-otic'. The plural noun narcotics as the name of a class of drugs (and later of the drug-enforcement sense) is \"\n            \"a much later specialisation of the substantivised adjective. Semantically the chain never leaves the sense of \"\n            \"narke: 'benumbing' > 'sleep-inducing drug' > 'illegal drug'. The French > English step is straightforward.\"),\n          \"derivation_fa\": (\n            \"انگلیسی narcotic وام‌واژه‌ای سدهٔ چهاردهمی از narcotique فرانسوی (و narcoticus لاتینی میانه) است و نخستین کاربرد \"\n            \"آن در «داستان شهسوار» چاسر (حدود ۱۳۸۵: «narcotikes and opie of Thebes») دیده می‌شود؛ کلاین ص ۱۰۲۸ همین زنجیره را \"\n            \"می‌دهد. صورت جمعِ اسمیِ narcotics به‌عنوان نام دسته‌ای از داروها (و سپس مواد مخدر) تخصیص معنایی متأخری است. تحول \"\n            \"معنایی هرگز از حوزهٔ νάρκη بیرون نمی‌رود: «بی‌حس‌کننده» → «داروی خواب‌آور» → «مادهٔ مخدر». ادعای نورایی درست است، \"\n            \"هرچند نمودار برای این گره مرجعی نمی‌دهد.\"),\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n             \"note\": \"refs=None for this node; checked Klein p. 1028 instead - see consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"leaf 550 (printed p. 1028) s.v. narcotic, narcosis\", \"stance\": \"supports\",\n             \"note\": \"'narcotic, adj., producing insensibility. - F. narcotique ... fr. ML. narcoticus, fr. Gk. \"\n                     \"narkotikos' and 'narcosis ... Medical L., fr. Gk. narkosis, \\\"a benumbing\\\", fr. narkoun'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)ner-\", \"stance\": \"supports\",\n             \"note\": \"the root entry's English derivatives are given as 'NARCO-, NARCOSIS, NARCOTIC', i.e. Watkins routes \"\n                     \"narcotic through Greek narke exactly as Nourai does.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Germanic\",\n          \"words\": \"snarwa; narwa\",\n          \"verdict\": \"plausible\",\n          \"derivation\": (\n            \"narwa is solid. Proto-Germanic *narwaz 'constricted, narrow' underlies OE nearu, OS naru, MDu. nare, OHG narwa \"\n            \"'scar' (i.e. 'drawn-together wound edges'), ON Norva-sund 'Straits of Gibraltar' and MHG naerlich 'concise'; \"\n            \"Pokorny 976 states it outright, '*nar-wa- actually \\\"zusammengeschnuert\\\"', and Buck 12.62 (p. 886) files the \"\n            \"same set 'prob. fr. a root meaning \\\"draw together, tie\\\"(?)'. snarwa 'cord, trap' is not, however, a form the \"\n            \"handbooks reconstruct. The s-mobile branch that yields 'cord/snare' is *snarho(n)- (ON snara 'noose, snare', \"\n            \"OHG snar(a)ha, and as a Norse loan OE sneare) beside *snoro (OHG snuor 'cord, band', Goth. snorjo 'plaited \"\n            \"basket', OE sner 'harp string'); Watkins - Nourai's own reference for this node - prints 'Suffixed extended \"\n            \"zero-grade form *snork- in Germanic *snarh-on-'. Nourai has evidently merged *snarh-on- 'snare' with *narwa- \"\n            \"'narrow' into a single s-mobile form *snarwa: the two are cognate but are different formations (-k- extension \"\n            \"vs. -wo- suffix). Verified on the printed page (300/400 dpi render of pdf p. 362, copy saved to \"\n            \"data/verification/sources/refs/ocr/BOOK/362.png): the book itself prints 'snarwa : cord, trap' and 'narwa : \"\n            \"narrow', so the JSON extraction is faithful and the looseness is the author's. A second, milder caveat: \"\n            \"Watkins hedges on narrow itself - 'Proposed by some as a derivative of this root is Germanic *narwa- in Old \"\n            \"English nearu, narrow'.\"),\n          \"derivation_fa\": (\n            \"*narwaz ژرمنی آغازین «تنگ، به‌هم‌فشرده» استوار است: انگلیسی باستان nearu، ساکسون باستان naru، آلمانی علیای باستان \"\n            \"narwa «جای زخم» (یعنی «لبه‌های به‌هم‌کشیدهٔ زخم») و نام Nǫrva-sund «تنگهٔ جبل‌الطارق» در نورس باستان؛ پوکورنی (ص \"\n            \"۹۷۶) صریحاً می‌گوید *nar-wa- «در اصل به‌هم‌بسته/فشرده» است و باک نیز (۱۲٫۶۲، ص ۸۸۶) همین را — با یک علامت پرسش — \"\n            \"می‌آورد. اما *snarwa «ریسمان، دام» صورتی نیست که فرهنگ‌ها بازسازی کنند: شاخهٔ دارای «س»ِ متحرک که «کمند» می‌دهد \"\n            \"*snarhō(n)- است (نورس باستان snara، آلمانی علیای باستان snar(a)ha، انگلیسی باستان snēare که خود وام نورسی است) \"\n            \"در کنار *snōrō (snuor «ریسمان»، گوتی snōrjō). واتکینز — همان مرجعی که نورایی برای این گره آورده — «Germanic \"\n            \"*snarh-ōn-» می‌نویسد. پس کتاب دو ساختِ هم‌ریشه ولی جدا (گسترش ‑k و پسوند ‑wo) را در یک صورت ادغام کرده است. \"\n            \"تصویر صفحهٔ چاپی بازبینی شد: خودِ کتاب «snarwa : cord, trap» چاپ کرده، پس خطای خوانش اسکن نیست و آسان‌گیریِ \"\n            \"مؤلف است. ادعا با احتیاط پذیرفتنی است.\"),\n          \"sources\": [W_NARROW],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\",\n             \"note\": \"AHD_watkins1985.txt s.v. (s)ner-: '1. Suffixed extended zero-grade form *snork- in Germanic \"\n                     \"*snarh-on- in: a. Old Norse snara, cord, noose, trap: SNARE(1); b. Dutch snaar, string: SNARE(2). \"\n                     \"2. Proposed by some as a derivative of this root is Germanic *narwa- in Old English nearu, narrow: \"\n                     \"NARROW.' - narwa is there (hedged); snarwa is not, the form being *snarh-on-, and its gloss 'cord, \"\n                     \"noose, trap' is exactly what Nourai reproduces, showing he collapsed the two entries.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW pp. 975-977 s.v. (s)ner-2\", \"stance\": \"partial\",\n             \"note\": \"'Old Saxon naru, Old English nearu, engl. narrow \\\"narrow\\\" (*nar-wa- actually \"\n                     \"\\\"zusammengeschnuert\\\")' and, under the *sner-k- extension, 'Old High German snar(a)ha \\\"loop, noose, \"\n                     \"snare\\\", Old Icelandic snara ... snara f. \\\"loop, noose, snare\\\" (Scandinavian loanword is Old \"\n                     \"English sneare)'. Supports narwa; gives *snarh-, not *snarwa.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 700\", \"stance\": \"partial\",\n             \"note\": \"'wahrscheinlich ... ahd. snuor \\\"Schnur, Band, Seil\\\", dan.-schwed. snor ds., got. snorjo \"\n                     \"\\\"geflochtener Korb\\\", ags. sner (*snorio) \\\"Saite einer Harfe\\\", aisl. snori n. \\\"gedrehtes Seil\\\"' - \"\n                     \"the 'cord' words are *snor-/*snarh-, not *snarwa.\"},\n            {\"src\": \"SYN\", \"where\": \"12.62 NARROW, p. 886\", \"stance\": \"partial\",\n             \"note\": \"'OE nearu, ME narowe, NE narrow, OS naru : ON Norva-sund ..., OHG narwa \\\"scar\\\" ..., prob. fr. a \"\n                     \"root meaning \\\"draw together, tie\\\"(?)'.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt line 11855 s.v. noruos\", \"stance\": \"partial\",\n             \"note\": \"Mann puts OHG narwa / MHG narwe 'scar' under 'noruos \\\"incision, groove ... character, habit\\\"', a \"\n                     \"different root label, while cross-referring the snarp-/snerp- family.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"snare, narrow\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\n            \"snare: ME snare comes from Old Norse snara 'noose, snare' (OE sneare, itself a Scandinavian loan per Pokorny \"\n            \"977, survives only marginally), from PGmc *snarho(n)- < *snork-, the zero-grade -k- extension of the root; \"\n            \"Watkins routes SNARE(1) through ON snara 'cord, noose, trap' and SNARE(2) 'the gut string of a drum' through \"\n            \"Dutch snaar 'string'. narrow: ME narewe/narwe/naru < OE nearu (adj.) 'narrow, strait, confined' < \"\n            \"Proto-West-Germanic *naru < PGmc *narwaz, i.e. the -wo- formation of the same root; Klein, 'narrow, adj. ... \"\n            \"fr. OE. nearu, rel. to OS. naro, MDu. nare; orig. prob. meaning \\\"twisted up, shriveled up\\\", fr. I.-E. base \"\n            \"*(s)ner- ... whence also OE. sneare, \\\"snare\\\"'. Skeat's SNARE entry makes the same connection to Greek narke \"\n            \"('a base SNARH = Aryan SNARK, cf. Gk. narke, cramp; see Narcissus'). Both English words and the arrow from the \"\n            \"Germanic node are right; the only softness is the general one that the narrow-to-root link is 'proposed by \"\n            \"some' (Watkins) rather than certain.\"),\n          \"derivation_fa\": (\n            \"snare انگلیسی از snara نورس باستان «کمند، دام» است — انگلیسی باستان snēare نیز خود وام‌واژه‌ای نورسی است — و به \"\n            \"*snarhō(n)- ژرمنی از درجهٔ صفرِ گسترشِ ‑k یعنی *snork- بازمی‌گردد؛ واتکینز SNARE(1) را از snara نورسی و \"\n            \"SNARE(2) («زهِ رویِ طبل») را از snaar هلندی می‌گیرد. narrow از nearu انگلیسی باستان < *naru ژرمنی غربی < *narwaz \"\n            \"ژرمنی است، یعنی ساختِ ‑wo همان ریشه؛ کلاین می‌نویسد «orig. prob. meaning \\\"twisted up, shriveled up\\\", fr. \"\n            \"I.-E. base *(s)ner-». اسکیت هم در مادهٔ SNARE همین ستاک SNARH را با νάρκη «گرفتگی» یونانی می‌سنجد و خواننده را \"\n            \"به مادهٔ Narcissus می‌فرستد. ادعای نورایی درست است؛ تنها تحفظ همان است که پیوند narrow با ریشه به گفتهٔ واتکینز \"\n            \"«نظر برخی» است، نه امری قطعی.\"),\n          \"sources\": [W_NARROW],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n             \"note\": \"refs=None for this node; checked Klein (s.v. narrow), Skeat (s.v. Snare) and Watkins s.v. (s)ner- \"\n                     \"instead - see consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"leaf 551 (printed p. 1029) s.v. narrow\", \"stance\": \"supports\",\n             \"note\": \"'narrow, adj., of small breadth. - ME. narewe, narwe, naru, fr. OE. nearu, rel. to OS. naro, MDu. \"\n                     \"nare; orig. prob. meaning \\\"twisted up, shriveled up\\\", fr. I.-E. base *(s)ner-, \\\"to turn, twist, \"\n                     \"bind together\\\", whence also OE. sneare, \\\"snare\\\". See snare and cp. narcotic.'\"},\n            {\"src\": \"SKT\", \"where\": \"p. 447 s.v. Snare\", \"stance\": \"supports\",\n             \"note\": \"'Snare, a noose. (E.) A.S. sneare, string, noose ... the sb. is from a strong verb, M.H.G. snerhen, \"\n                     \"to twist tightly; a base SNARH = Aryan SNARK, cf. Gk. narke, cramp; see Narcissus.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)ner-\", \"stance\": \"supports\",\n             \"note\": \"SNARE(1), SNARE(2) and NARROW are the English words Watkins lists for this root.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Nes 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *nes- 'to return home safely; to be safe/sheltered (in the house), to join'\",\n      \"note\": (\"Pokorny nes- pp. 766-767 (Nourai's POK:766 is its first page); Walde-Pokorny II 334 glosses it \"\n               \"'angenehm, gluecklich wohin gelangen, auch vom Geborgensein im schuetzenden Hause'; Watkins nes-(1) 'To \"\n               \"return safely home'; Wiktionary *nes- 'to return home (safely)'. Nourai's 'to join, reunite, return, be \"\n               \"safe' is a fair composite of Pokorny's 'sich vereinigen' side (Skt. nasate 'unites, joins', the divine \"\n               \"twins Nasatya-) and the Germanic 'be saved/recover' side (Goth. ganisan, nasjan), so the root, the \"\n               \"language label and the gloss are all right, and every branch drawn from it (Av. asta-, Gk. naos, nostos, \"\n               \"Gmc. nest-/nasjan) is one Pokorny and Watkins actually list. Note on the print: in the book a completely \"\n               \"blank box sits to the right of the Avestan node, joined to it by an arrow (verified on the page image); \"\n               \"it holds no text, and the JSON extraction correctly creates no node for it - a layout artefact, not lost \"\n               \"data.\"),\n      \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *nes- «به سلامت به خانه بازگشتن؛ در پناهِ خانه آسوده بودن؛ پیوستن» است. پوکورنی \"\n                  \"آن را در صفحه‌های ۷۶۶–۷۶۷ آورده (ارجاع POK:766 نورایی به صفحهٔ نخست آن می‌خورد)، والده–پوکورنی (ج ۲ ص ۳۳۴) \"\n                  \"معنایش را «angenehm, glücklich wohin gelangen, auch vom Geborgensein im schützenden Hause» می‌نویسد، \"\n                  \"واتکینز «to return safely home» و ویکی‌واژه «to return home (safely)». پس تعریف نورایی، که سنسکریت \"\n                  \"násate «می‌پیوندد» را با «رستن و سلامت یافتنِ» ژرمنی یک‌جا می‌آورد، درست است و همهٔ شاخه‌های نمودار \"\n                  \"(اوستایی asta-، یونانی naos و nostos، ژرمنی nest-/nasjan) در پوکورنی و واتکینز آمده‌اند. یادآوری دربارهٔ \"\n                  \"چاپ: در کتاب کنار جعبهٔ اوستایی کادری یکسره خالی نشسته است (تصویر صفحه بازبینی شد)؛ استخراج JSON به‌درستی \"\n                  \"برای آن گرهی نساخته و داده‌ای از دست نرفته است.\"),\n      \"sources\": [W_NES],\n      \"ref_check\": [\n        {\"ref\": \"POK:766\", \"status\": \"supports\",\n         \"note\": POK_NES + \": 'Material: Old Indic nasate \\\"unites, joins\\\" ... zero grade Old Indic asta-, Avestan asta- \"\n                 \"n. \\\"homeland, domicile\\\"; gr. neomai ... nostos m. \\\"home coming, returning home\\\" ... Gothic ga-nisan \"\n                 \"\\\"gerettet become, recover\\\" ... Kaus. Gothic nasjan \\\"to make healthy\\\" ... Old English nest n. \"\n                 \"\\\"nourishment, food\\\"'. Every node of the chart is in this one entry.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II pp. 334-335 s.v. nes- (WLD_Bd2_pages.txt leaves 338-339)\", \"stance\": \"supports\",\n         \"note\": \"'nes- \\\"angenehm, gluecklich wohin gelangen\\\", auch vom Geborgensein im schuetzenden Hause. Ai. nasate \"\n                 \"\\\"geht liebevoll heran, gesellt sich zu, vereinigt sich mit\\\" ... schwundstufig ai. asta-, av. asta- n. \"\n                 \"\\\"Heimat, Wohnort\\\" (Bartholomae KZ. 29, 483, vgl. mit anderen Vokalstufen gr. nostos, ags. nest n.)' - \"\n                 \"Pokorny's 'WP. II 334 f.' checks out and matches Nourai's gloss closely.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nes-(1) (AHD_watkins1985.txt line 783)\", \"stance\": \"supports\",\n         \"note\": \"'nes-(1). To return safely home. 1. Germanic *nes-tam in Old English, Old High German (in composition), \"\n                 \"and Old Norse nest, food for a journey, akin to the possible Germanic source of Old French harnes, \"\n                 \"harness: HARNESS. 2. Suffixed o-grade form *nos-to- in Greek nostos, a return home: NOSTALGIA. [Pok. \"\n                 \"nes- 766.]'\"},\n        {\"src\": \"IEC\", \"where\": \"IEC.txt line 11675 s.v. nes- (2)\", \"stance\": \"supports\",\n         \"note\": \"Mann: 'nes- (2) \\\"turn, return, recover, thrive, succeed, proceed\\\". Cf. WP II, 334 ... Gk. neomai, \"\n                 \"neumai, Ion. nisomai \\\"return\\\" ... Go. ga-nisan \\\"survive\\\"; MHG ge-nesen, OHG gi-nesan, OE nesan, id.'\"},\n        {\"src\": \"KLN\", \"where\": \"leaf 553 s.v. nostalgia\", \"stance\": \"supports\",\n         \"note\": \"'fr. I.-E. base *nes-, *nos-, \\\"to return; to unite\\\", whence also OI. nasate, \\\"approaches, joins\\\", \"\n                 \"Nasatya, name of the physicians of the gods' - Klein's gloss is almost word for word Nourai's.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"asta 2\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\n            \"Avestan asta- n. 'home, homestead' is real and is the standard Iranian reflex of this root. Bartholomae, \"\n            \"Altiranisches Woerterbuch col. 213, s.v. (1)asta-: \\\"j. (1)asta- n. 'Heim, Heimstaette': astem ... fracarenta \"\n            \"pasvasca staoraca masyaca 'ein Heim schafften sich da Kleinvieh und Grossvieh und Menschen' V. 2.13\\\", with a \"\n            \"special use of the sleeping-places of dogs (V. 14.17), and Bartholomae's own etymological note 'Zum ai. V. \"\n            \"nasati; Bthl. KZ. 29.483; ai. asta- n., mp. pah-ast'. Formally it is the zero grade *n-s-to- of *nes-, a \"\n            \"verbal noun 'the place one returns to' - identical with Sanskrit astam 'home' (whence the famous astam eti \"\n            \"'goes home' of the setting sun, hence 'sunset'), and standing to Greek nostos as zero grade to o-grade \"\n            \"(Walde-Pokorny II 334 says exactly this). Nourai's '2' in 'asta 2' is his own homograph number: Bartholomae \"\n            \"likewise distinguishes (1)asta- 'Heim' from (2)asta- (participle of ah-) and from ast- 'Knochen'.\"),\n          \"derivation_fa\": (\n            \"اوستایی asta- (نامِ خنثی) «خانه، خانمان» واژه‌ای واقعی و بازماندهٔ معیار این ریشه در ایرانی است: بارتولومه در \"\n            \"فرهنگ ایرانی باستان، ستون ۲۱۳، می‌نویسد «asta- n. 'Heim, Heimstätte'» و شاهدِ ویدیوداد ۲٫۱۳ را می‌آورد: «astəm \"\n            \"... fracarəṇta pasvasca staoraca masyāca» یعنی «آنجا گوسفند و گاو و مردم خانه‌ای برای خود ساختند»، و خود در \"\n            \"یادداشت ریشه‌شناسی به فعل násati سنسکریت و به KZ 29.483 ارجاع می‌دهد. از نظر ساخت، درجهٔ صفرِ *n̥s-to- از *nes- \"\n            \"است، یعنی اسمِ مصدرِ «جایی که آدمی به آن بازمی‌گردد»، و با اَستَم سنسکریت یکی است (همان که در astam eti «به خانه \"\n            \"می‌رود»، دربارهٔ خورشید = غروب، به‌کار می‌رود)؛ نسبتش با νόστος یونانی نسبتِ درجهٔ صفر به درجهٔ o است — چنانکه \"\n            \"والده–پوکورنی (ج ۲ ص ۳۳۴) صریحاً می‌گوید. شمارهٔ «۲» در «asta 2» شمارشِ خودِ نورایی برای جدا کردن این واژه از \"\n            \"asta- دیگر (اسم مفعولِ ah-) و ast- «استخوان» است. ادعای نورایی درست است.\"),\n          \"sources\": [W_NES],\n          \"ref_check\": [\n            {\"ref\": \"POK:766\", \"status\": \"supports\",\n             \"note\": POK_NES + \": 'zero grade Old Indic asta-, Avestan asta- n. \\\"homeland, domicile\\\"' stands on p. 766, \"\n                     \"the page Nourai cites.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Woerterbuch col. 213 s.v. (1)asta- (BRT.txt leaf 149, running head \"\n                                    \"\\\"asta-\\\" with column numeral, next leaf numbered 214)\", \"stance\": \"supports\",\n             \"note\": \"\\\"j. (1)asta- n. 'Heim, Heimstaette': ... 'ein Heim schafften sich da Kleinvieh und Grossvieh und \"\n                     \"Menschen' V. 2.13\\\", with the note 'Zum ai. V. nasati; Bthl. KZ. 29.483. - ai. asta- n., mp. pah-ast'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 334\", \"stance\": \"supports\",\n             \"note\": \"'schwundstufig ai. asta-, av. asta- n. \\\"Heimat, Wohnort\\\" (Bartholomae KZ. 29, 483, vgl. mit \"\n                     \"anderen Vokalstufen gr. nostos, ags. nest n.)'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nes-(1)\", \"stance\": \"silent\",\n             \"note\": \"Watkins lists only the Greek and Germanic branches (he restricts himself to roots with English \"\n                     \"derivatives), so the Avestan word is absent; not a contradiction.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Greek\",\n          \"words\": \"naos\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\n            \"Greek naos 'temple, sanctuary, the cella' appears dialectally as Doric/Thessalian naos, Laconian nawos, \"\n            \"Lesbian nauos (i.e. nawwos), Ionic neos, Attic neos - a spread that only makes sense from *nas-wo-. That is \"\n            \"the reduced grade of *nes- with the -wo- suffix, beside the verb naio (< *nas-yo) 'I dwell' and the future \"\n            \"nassomai; Pokorny 766-767 sets it out exactly so: 'reduced grade naio, Fut. nassomai \\\"stay, dwell, \"\n            \"inhabit\\\" ... *nas-wos: Doric Thessalian naos, lak. nawos, Lesbian nauos, Ionian neos, Attic neos m. \\\"( \"\n            \"god's abode =) temple, shrine\\\"', and Walde-Pokorny II 335 the same. The semantics are 'dwelling' > \"\n            \"'dwelling of a god' > 'temple, inner shrine'. Klein is more cautious - 'which is of uncertain origin. It \"\n            \"stands perh. for *naswos and is rel. to naio ... hence prop. denotes \\\"the dwelling place of a god\\\"' - but \"\n            \"the *nas-wo- analysis is the standard one in Chantraine and Beekes as well. Confirmed.\"),\n          \"derivation_fa\": (\n            \"یونانی νᾱός «پرستشگاه، حرم» در گویش‌ها به صورت‌های νᾱός (دوری/تسالیایی)، νᾱϝός (لاکونی)، ναῦος (لسبوسی)، νηός \"\n            \"(یونیایی) و νεώς (آتیک) دیده می‌شود و این تنوع تنها از *nas-wo- توضیح‌پذیر است: درجهٔ کاهیدهٔ *nes- با پسوند \"\n            \"‑wo، در کنار فعل ναίω (< *nas-yō) «سکنی می‌گزینم». پوکورنی (۷۶۶–۷۶۷) درست همین را می‌گوید و والده–پوکورنی (ج ۲ \"\n            \"ص ۳۳۵) نیز. تحول معنایی: «خانه» → «خانهٔ خدا» → «پرستشگاه، حرمِ اندرونی». کلاین محتاط‌تر است («خاستگاهش نامعلوم \"\n            \"است؛ شاید *νασϝός و هم‌ریشه با ναίω، پس در اصل جایگاه سکونتِ خدا») ولی تحلیل *nas-wo- در شانترن و بیکس هم معیار \"\n            \"است. ادعای نورایی درست است.\"),\n          \"sources\": [W_NES],\n          \"ref_check\": [\n            {\"ref\": \"POK:766\", \"status\": \"supports\",\n             \"note\": POK_NES + \": '*nas-wos: Doric Thessalian naos, lak. nawos, Lesbian nauos ..., Attic neos m. \\\"( \"\n                     \"god's abode =) temple, shrine\\\"' - on pp. 766-767 of the entry Nourai cites.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 335\", \"stance\": \"supports\",\n             \"note\": \"'*nas-wos dor. thess. naos, lak. nawos, lesb. nauos (d. i. nawwos), jon. neos, att. neos \"\n                     \"\\\"(Goetterwohnung =) Tempel, Heiligtum\\\"'.\"},\n            {\"src\": \"KLN\", \"where\": \"leaf 549 s.v. naos\", \"stance\": \"partial\",\n             \"note\": \"'ModL., fr. Gk. naos (Ion. neos, Att. neos), \\\"temple; the inner part of a temple, the shrine, the \"\n                     \"cella\\\", which is of uncertain origin. It stands perh. for *naswos and is rel. to naio (for \"\n                     \"*nasuo), \\\"I dwell\\\", hence prop. denotes \\\"the dwelling place of a god\\\". See nostalgia' - same \"\n                     \"analysis, but hedged.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt line 11675 s.v. nes- (2)\", \"stance\": \"partial\",\n             \"note\": \"Mann lists the verbal forms (Gk. neomai, neumai, nisomai) under nes- but not naos itself.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Syriac\",\n          \"words\": \"nausa\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\n            \"Classical Syriac nawsa (spelled nwsʾ) 'charnel house, repository for the dead, mausoleum', beside nawsa/nawsha \"\n            \"(nwshʾ) 'coffin, sarcophagus; tomb, sepulchre', is a loan of Greek naos - taken in the sense Greek writers \"\n            \"applied to sepulchral shrines and to the burial chambers and sarcophagi of Egypt. Mo'in's etymological \"\n            \"footnote on Borhan-e Qate' p. 2086 (the page cited on Nourai's Persian node) states it: 'Syriac nawsa (qabr) \"\n            \"[Brockelmann, Lexicon Syriacum]', with a cross-reference to Greek naos and to Dozy II 737. Wiktionary \"\n            \"(s.v. Arabic naawuus) gives the same two Syriac forms with the same Greek source. The semantic route is \"\n            \"'shrine/temple' > 'martyr's shrine, sepulchral chapel' > 'grave, Christian burial ground'; Nourai's spelling \"\n            \"'nausa' renders nawsa with -au- for Syriac -aw-. The Greek > Syriac arrow is right.\"),\n          \"derivation_fa\": (\n            \"سریانی ܢܘܣܐ nāwsā «دخمه، جای نهادن مردگان، آرامگاه» (در کنار ܢܘܫܐ nawšā «تابوت سنگی، گور») وام‌واژه‌ای است از \"\n            \"ναός یونانی، در همان معنایی که نویسندگان یونانی برای زیارتگاه‌های گور و اتاق‌های گور و تابوت‌های سنگی مصر به‌کار \"\n            \"می‌بردند. معین در حاشیهٔ برهان قاطع ص ۲۰۸۶ — همان صفحه‌ای که نورایی برای گرهٔ فارسی آورده — می‌نویسد «سریانی nāwsā \"\n            \"(قبر) [بروکلمان، فرهنگ سریانی]» و خواننده را به ναός یونانی و دُزی ج ۲ ص ۷۳۷ می‌فرستد؛ ویکی‌واژه نیز همین دو صورت \"\n            \"سریانی را با همان خاستگاه یونانی می‌آورد. تحول معنایی: «حرم، پرستشگاه» → «زیارتگاه شهید، نمازخانهٔ گورستان» → \"\n            \"«گور، گورستان مسیحیان». نگارشِ «nausâ» نورایی همان nāwsā است با ‑au‑ برای ‑āw‑ سریانی. ادعای نورایی درست است.\"),\n          \"sources\": [W_NAWU],\n          \"ref_check\": [\n            {\"ref\": \"MON:4649\", \"status\": \"partial\",\n             \"note\": \"Mo'in's Farhang-e Farsi has the entry (see consulted) and it agrees in substance, but the page \"\n                     \"number itself could not be checked: the only local copy is the 2-volume Adena reprint \"\n                     \"(MON_part1/2.txt, MON_2vol_Adena_*), whose pagination differs from the 6-volume Amir Kabir edition \"\n                     \"Nourai cites, and it carries no usable page markers. Mo'in's entry does not name Syriac; the Syriac \"\n                     \"etymology is in his Borhan footnote (BQT p. 2086), quoted below.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"vol. 4, printed p. 2086 = pdf p. 169 (BQT_v4_pages.txt leaf 168; re-OCRed with \"\n                                    \"tools/ref_page.py BQT:2086 --image)\", \"stance\": \"supports\",\n             \"note\": \"Mo'in's footnote 5 to the entry «نااوس»: «(عر) ناووس > ناژوس، خصوصاً بمعنی دخمه و اطاق زیرزمینی است \"\n                     \"که برای دفن میت بکار رود. جمع: نواویس ... قبر، آرامگاه (مسیحیان). رک: دزی ج۲ ص۷۳۷ ... سریانی nāwsā \"\n                     \"(قبر) [Brockelmann, Lex. Syr.] ...» - Syriac nawsa 'grave' with Brockelmann as authority, exactly \"\n                     \"Nourai's node.\"},\n            {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramaeischen Fremdwoerter im Arabischen (AFA.txt)\", \"stance\": \"silent\",\n             \"note\": \"grep -n -i 'nawsa|nauso|naus|Grabmal' AFA.txt returns nothing relevant; Fraenkel does not treat \"\n                     \"this word.\"},\n            {\"src\": \"KLN\", \"where\": \"leaf 549 s.v. naos\", \"stance\": \"partial\",\n             \"note\": \"documents the Greek source word and its 'inner part of a temple, the shrine, the cella' sense, \"\n                     \"which is the sense the Aramaic borrowing specialises.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Arabic\",\n          \"words\": \"nawus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\n            \"Arabic naawuus (ناووس), plural nawaawiis (نواويس), 'stone coffin, sarcophagus; tomb, Christian/non-Muslim \"\n            \"graveyard', is an Aramaic-Syriac loan of the Greek word: Syriac nawsa was rendered with alif + waaw for the \"\n            \"long a and the diphthong, and the plural was refitted to the Arabic pattern fawaa'iil. Mo'in's footnote on \"\n            \"Borhan p. 2086 tags the word '(عر)' = Arabic and quotes Hamza al-Isfahani (10th c.): «والفرس لم تعرف \"\n            \"القبور، وانما کانت تغیب الموتی فی الدخمات والنواویس» - 'the Persians did not know graves; they used to hide \"\n            \"the dead in dakhmas and nawaawiis' - which is a dated attestation of the Arabic plural in exactly this \"\n            \"sense, and it also shows how the word came to be used of Zoroastrian ossuaries. Note the direction: this is \"\n            \"a Greek word that reached Arabic through Aramaic, not a Persian word Arabicised, and not (as the chart might \"\n            \"suggest by omission) a direct Greek loan into Arabic. Wiktionary s.v. ناووس gives the same account.\"),\n          \"derivation_fa\": (\n            \"عربی ناووس (nāwūs)، جمع نواویس، «تابوت سنگی؛ گور، گورستان غیرمسلمانان»، وام‌واژه‌ای آرامی/سریانی از همان واژهٔ \"\n            \"یونانی است: آوای بلندِ سریانی با «ا + و» عربی نوشته شده و جمع بر وزنِ فواعیل ساخته شده است. حاشیهٔ معین بر برهان \"\n            \"قاطع ص ۲۰۸۶ واژه را «(عر)» می‌نامد و از حمزهٔ اصفهانی (سدهٔ چهارم هجری) نقل می‌کند: «والفرس لم تعرف القبور، وإنما \"\n            \"کانت تُغیّب الموتی فی الدخمات والنواویس» — گواهی تاریخ‌داری بر همین معنا، که نشان می‌دهد این واژه چگونه به \"\n            \"استودان‌های زردشتی هم گفته شده است. جهتِ وام‌گیری را باید روشن گفت: این واژهٔ یونانی است که از راه آرامی به عربی \"\n            \"رسیده، نه واژه‌ای فارسی که معرّب شده باشد. ویکی‌واژه نیز همین را می‌گوید. ادعای نورایی درست است.\"),\n          \"sources\": [W_NAWU],\n          \"ref_check\": [\n            {\"ref\": \"MON:4649\", \"status\": \"partial\",\n             \"note\": \"Mo'in's lexicon entry s.v. ناووس marks the word معرّب ('Arabicised') and glosses it as the \"\n                     \"underground burial chamber etc., which supports the Arabic stage; the cited page number cannot be \"\n                     \"verified because the local copy is the 2-volume Adena reprint with different pagination and no page \"\n                     \"markers.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"vol. 4, printed p. 2086, Mo'in's footnote 5\", \"stance\": \"supports\",\n             \"note\": \"«(عر) ناووس ... خصوصاً بمعنی دخمه و اطاق زیرزمینی است که برای دفن میت بکار رود. جمع: نواویس. حمزه \"\n                     \"اصفهانی گوید: والفرس لم تعرف القبور، وانما کانت تغیب الموتی فی الدخمات والنواویس».\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfaz al-Farisiyya al-Mu'arraba (AFM_pages.txt)\", \"stance\": \"silent\",\n             \"note\": \"grep 'ناووس' / 'نواويس' in AFM_pages.txt gives no headword (only النرجس incidentally, s.v. ايوس, \"\n                     \"leaf 664) - Addi Shir collects Persian, not Greek/Aramaic, loans, so its silence is expected.\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an (FVQ_pages.txt)\", \"stance\": \"silent\",\n             \"note\": \"grep 'ناووس' returns nothing - the word is not Qur'anic.\"},\n            {\"src\": \"TAD\", \"where\": \"al-Unaysi, Tafsir al-alfaz al-dakhila (TAD_pages.txt)\", \"stance\": \"silent\",\n             \"note\": \"grep 'ناووس' / 'نواويس' returns nothing usable (only a stray 'نرجس' at leaf 50).\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch (LKT.txt)\", \"stance\": \"silent\",\n             \"note\": \"grep 'ناووس' and 'nawus' returns nothing; Lokotsch covers oriental words that entered European \"\n                     \"languages, which this did not.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"nawus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\n            \"New Persian ناووس naavuus (also spelt ناوس and ناؤوس, all three of which the chart prints) 'tomb, ossuary; \"\n            \"temple/church of the Christians; Zoroastrian cemetery' came into Persian from Arabic. It is therefore a \"\n            \"Greek word that reached Persian by the Syriac > Arabic route, not through Middle Persian: there is no MP \"\n            \"*nawus, and Mo'in labels the Persian word معرّب. Borhan-e Qate' p. 2086, s.v. نااوس, glosses it «بر وزن \"\n            \"ناقوس، معبد ترسایان باشد - و آتشکده را نیز گویند؛ و ناووس هم آمده است که بجای همزه واو باشد» - 'on the \"\n            \"pattern of naaquus; a temple of the Christians, also said of a fire-temple; the form naavuus, with waaw for \"\n            \"the hamza, also occurs' - which accounts both for Nourai's three spellings and for his gloss 'cemetery, \"\n            \"temple, church'. Mo'in's Farhang defines it «اطاق زیرزمینی که برای دفن میت بکار برند؛ دخمه. قبر هر فرد \"\n            \"غیرمسلمان، گور کافر. گورستان زردشتیان، قبرستان مجوس». The chart's verse from Khaaqaani (12th c., \"\n            \"«بجیفه‌گاه و بناووس و مستراح و خلاب») uses it of a foul burial place. Confirmed.\"),\n          \"derivation_fa\": (\n            \"«ناووس» فارسی نو (نیز ناوس و ناؤوس — هر سه نگارشی که نمودار آورده) به معنی «گور، دخمه؛ پرستشگاه ترسایان؛ گورستان \"\n            \"زردشتیان» از عربی به فارسی آمده است؛ یعنی واژه‌ای یونانی است که از راه سریانی → عربی به فارسی رسیده، نه از راه \"\n            \"فارسی میانه — چنین صورتی در پهلوی نیست و معین آن را «معرّب» می‌داند. برهان قاطع (ص ۲۰۸۶، مادهٔ «نااوس») می‌نویسد \"\n            \"«بر وزن ناقوس، معبد ترسایان باشد - و آتشکده را نیز گویند؛ و ناووس هم آمده است که بجای همزه واو باشد»، که هم سه \"\n            \"نگارش و هم معنای «گورستان، پرستشگاه، کلیسا» را توضیح می‌دهد؛ معین در فرهنگ فارسی نیز «اطاق زیرزمینی که برای دفن \"\n            \"میت بکار برند؛ دخمه. قبر هر فرد غیرمسلمان، گور کافر. گورستان زردشتیان» می‌آورد. بیت خاقانی که در نمودار نقل شده \"\n            \"همین معنای گورِ پلید را دارد. ادعای نورایی درست است.\"),\n          \"sources\": [W_NAWU],\n          \"ref_check\": [\n            {\"ref\": \"MON:4649\", \"status\": \"partial\",\n             \"note\": \"Mo'in's entry (MON_part2.txt): «ناووس: [= ناوس - ناؤوس؛ معر.] (اِ.) اطاق زیر زمینی که برای دفن میت \"\n                     \"بکار برند؛ دخمه. قبر هر فرد غیرمسلمان، گور کافر. گورستان زردشتیان، قبرستان مجوس.» - supports the \"\n                     \"word, the three spellings and the Arabic mediation ('معر.' = Arabicised); the page number could not \"\n                     \"be verified (local copy = 2-vol Adena reprint, different pagination).\"},\n            {\"ref\": \"BQT:2086\", \"status\": \"supports\",\n             \"note\": \"BQT_v4_pages.txt leaf 168 = printed p. 2086 (running-head numeral confirmed; printed = pdf + 1917): \"\n                     \"«نااوس - بر وزن ناقوس، معبد ترسایان باشد - و آتشکده را نیز گویند؛ وناووس هم‌آمده است که بجای همزه واو \"\n                     \"باشد» plus the Arabic/Syriac footnote. Exactly the page and the content Nourai's node needs.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. ناووس (MON_part2.txt line 73635)\", \"stance\": \"supports\",\n             \"note\": \"«معر.» tag and the gloss 'underground chamber used to bury the dead; dakhma; the grave of any \"\n                     \"non-Muslim; the cemetery of the Zoroastrians'.\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 4 pp. 2086 and 2111\", \"stance\": \"supports\",\n             \"note\": \"Borhan has the word twice - as نااوس on p. 2086 and again as ناووس on p. 2111 ('بروزن ناقوس. \"\n                     \"آتشکده...'), i.e. the lexicographic tradition knows both spellings, as Nourai's node shows.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (HRN.txt)\", \"stance\": \"silent\",\n             \"note\": \"grep -n -i 'nawus|navus' HRN.txt: no hit - Horn deals with inherited Persian etymology, not Arabic \"\n                     \"loans.\"},\n            {\"src\": \"HUB\", \"where\": \"Huebschmann, Persische Studien (HUB.txt)\", \"stance\": \"silent\",\n             \"note\": \"grep -n -i 'nawus|navus' HUB.txt: no hit.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Greek\",\n          \"words\": \"nostos\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\n            \"Greek nostos m. 'return home, homecoming' - the word that gives the Odyssey its theme and the Nostoi their \"\n            \"title - is the suffixed o-grade *nos-to- of *nes-, built to the verb neomai/neumai 'I return home' (Pokorny \"\n            \"766: 'gr. neomai, Ionian neumai \\\"come happily, return home, journey back home\\\", Nestor actually \\\"the \"\n            \"always returning\\\", nostos m. \\\"home coming, returning home\\\"'). Watkins states the formation exactly: \"\n            \"'Suffixed o-grade form *nos-to- in Greek nostos, a return home: NOSTALGIA'. Nourai's node, its language \"\n            \"label and its gloss are all correct.\"),\n          \"derivation_fa\": (\n            \"یونانی νόστος «بازگشت به خانه» — همان درون‌مایهٔ اودیسه و نام حماسهٔ Nostoi — صورتِ پسوندیِ درجهٔ o یعنی \"\n            \"*nos-to- از *nes- است و بر فعل νέομαι «به خانه بازمی‌گردم» ساخته شده؛ پوکورنی (ص ۷۶۶) می‌نویسد «gr. neomai ... \"\n            \"Nestōr در اصل «همیشه‌بازگردنده»، nostos «بازگشت به خانه»» و واتکینز نیز صریحاً «Suffixed o-grade form *nos-to- \"\n            \"in Greek nostos, a return home: NOSTALGIA» می‌آورد. گره، برچسب زبانی و معنای آن هر سه درست است.\"),\n          \"sources\": [W_NES],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\",\n             \"note\": \"AHD_watkins1985.txt line 783 s.v. nes-(1): '2. Suffixed o-grade form *nos-to- in Greek nostos, a \"\n                     \"return home: NOSTALGIA. [Pok. nes- 766.]'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW p. 766 s.v. nes-\", \"stance\": \"supports\",\n             \"note\": \"'nostos m. \\\"home coming, returning home\\\"', beside neomai and Nestor 'the always returning'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 334\", \"stance\": \"supports\",\n             \"note\": \"'gr. neomai \\\"komme gluecklich heran an, kehre heim\\\" ... nostos \\\"Heimkehr\\\"'.\"},\n            {\"src\": \"KLN\", \"where\": \"leaf 553 s.v. nostalgia\", \"stance\": \"supports\",\n             \"note\": \"'Gk. nostos, \\\"return home\\\" ... rel. to neomai (for *neuomai), \\\"I go, come, return\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"nostalgia\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": (\n            \"nostalgia is a New Latin coinage, not an inherited word: the Swiss physician Johannes Hofer built it in his \"\n            \"Basel medical dissertation 'Dissertatio medica de nostalgia' (1688; Klein prints 1668) as a learned calque \"\n            \"of German Heimweh, from Greek nostos 'return home' + -algia, from algos 'pain'. It enters English about \"\n            \"1770 as a medical term for homesickness - initially a diagnosable, sometimes fatal disease of soldiers and \"\n            \"mercenaries - and only in the 20th century generalises to 'wistful longing for the past'. Watkins lists \"\n            \"NOSTALGIA as the English derivative of *nos-to-, and Klein gives the coinage and both Greek elements. So \"\n            \"the Greek > English arrow is right, with the proviso that the transmission is scholarly word-formation \"\n            \"rather than descent.\"),\n          \"derivation_fa\": (\n            \"nostalgia واژه‌ای ساختگیِ لاتینی نو است، نه واژه‌ای موروثی: یوهانس هوفرِ سوئیسی آن را در رسالهٔ پزشکی خود \"\n            \"«Dissertatio medica de nostalgia» (بازل، ۱۶۸۸؛ کلاین ۱۶۶۸ می‌نویسد) به‌عنوان گرته‌برداری از Heimweh آلمانی، از \"\n            \"νόστος «بازگشت به خانه» + ‑αλγία از ἄλγος «درد» ساخت. حدود ۱۷۷۰ به انگلیسی راه یافت، نخست به‌عنوان نام \"\n            \"بیماریِ دلتنگیِ وطن — که آن روزها بیماریِ سربازان و مزدوران و گاه کشنده شمرده می‌شد — و تنها در سدهٔ بیستم به \"\n            \"معنای «حسرتِ گذشته» گسترش یافت. واتکینز NOSTALGIA را بازماندهٔ انگلیسی *nos-to- می‌داند و کلاین هم تاریخ ساخت و \"\n            \"هر دو جزء یونانی را می‌آورد. پس ادعای نورایی درست است، با این یادآوری که این وام‌گیری ساختِ عالمانه است نه \"\n            \"تحولِ طبیعی.\"),\n          \"sources\": [W_NES],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\",\n             \"note\": \"AHD_watkins1985.txt line 783: NOSTALGIA is given as the English word derived from *nos-to- under \"\n                     \"nes-(1).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"leaf 553 s.v. nostalgia\", \"stance\": \"supports\",\n             \"note\": \"'nostalgia, n., homesickness. - ModL., coined in 1668 by Johannes Hofer fr. Gk. nostos, \\\"return \"\n                     \"home\\\", and -algia, fr. algos, \\\"pain\\\". The first element is rel. to neomai ... fr. I.-E. base \"\n                     \"*nes-, *nos-, \\\"to return; to unite\\\".'\"},\n            {\"src\": \"POK\", \"where\": \"IEW p. 766\", \"stance\": \"supports\",\n             \"note\": \"supplies the Greek base (nostos) that the modern coinage uses; the coinage itself is post-classical \"\n                     \"and so outside Pokorny's scope.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Germanic\",\n          \"words\": \"nas-ja\",\n          \"verdict\": \"plausible\",\n          \"derivation\": (\n            \"The form and the gloss belong to two different Germanic formations, and the chart has attached them to each \"\n            \"other. *nas-ja- (i.e. PGmc *nazjan-) is real: it is the causative 'to make well, save, keep alive, nourish' \"\n            \"- Gothic nasjan 'gesund machen', OHG nerian/nerren 'am Leben erhalten, retten, schuetzen, ernaehren' (NHG \"\n            \"naehren), OS/OE nerian 'to rescue, shield' (Walde-Pokorny II 335; Pokorny 767) - built to the strong verb \"\n            \"*nesan (Goth. ganisan 'to recover, be saved'). But 'food for a journey' is the meaning of the sister noun \"\n            \"*nes-tam / *nestaz: OE nest 'provisions', ON nest 'provisions for a journey', OHG wega-nest 'travel food'. \"\n            \"Watkins, Nourai's own reference for this node, prints precisely 'Germanic *nes-tam in Old English, Old High \"\n            \"German (in composition), and Old Norse nest, food for a journey'. So the node conflates *nazjan- with \"\n            \"*nes-tam - two cognate but distinct derivatives - and it is the latter, not the former, that leads to \"\n            \"harness in node #9. Checked on the printed page (render of pdf p. 362 at 400 dpi, saved as \"\n            \"data/verification/sources/refs/ocr/BOOK/362.png): the book itself prints 'nas-ja : food for journey', so the \"\n            \"JSON is a faithful extraction and the mismatch is the author's, not the scan's. Klein's harness entry may be \"\n            \"what led him there: it names both 'OE. nest, \\\"provisions\\\"' and 'Goth. nasjan, \\\"to nourish\\\"' in one \"\n            \"breath.\"),\n          \"derivation_fa\": (\n            \"در این گره، صورت و معنا به دو ساختِ جداگانهٔ ژرمنی تعلق دارند و کتاب آن‌ها را به هم چسبانده است. *nas-ja- \"\n            \"(یعنی *nazjan- ژرمنی آغازین) واقعی است: فعل سببیِ «سالم کردن، رهانیدن، زنده نگه داشتن، پروردن» — گوتی nasjan، \"\n            \"آلمانی علیای باستان nerian/nerren (آلمانی امروز nähren)، انگلیسی و ساکسون باستان nerian — که بر فعل قویِ \"\n            \"*nesan (گوتی ganisan «رستن، نجات یافتن») ساخته شده (والده–پوکورنی ج ۲ ص ۳۳۵؛ پوکورنی ۷۶۷). اما معنای «توشهٔ \"\n            \"راه» از آنِ نامِ همزادش *nes-tam / *nestaz است: انگلیسی باستان nest «توشه»، نورس باستان nest «توشهٔ سفر»، \"\n            \"آلمانی علیای باستان wega-nest «خوراکِ راه». همان AHD که نورایی به آن ارجاع داده می‌نویسد «Germanic *nes-tam \"\n            \"... nest, food for a journey». پس گره دو مشتقِ هم‌ریشه ولی جدا را در هم آمیخته و آنکه به harness می‌رسد \"\n            \"*nes-tam است نه *nazjan-. تصویر صفحهٔ چاپی بازبینی شد: خودِ کتاب «nas-ja : food for journey» چاپ کرده است، پس \"\n            \"این خطای کتاب است نه خطای خوانش اسکن. شاید مادهٔ harness در کلاین او را به این آمیختگی کشانده باشد، چون در یک \"\n            \"جمله هم «OE. nest, provisions» و هم «Goth. nasjan, to nourish» را نام می‌برد. ادعا با احتیاط پذیرفتنی است.\"),\n          \"sources\": [E_HARN, W_NES],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\",\n             \"note\": \"AHD_watkins1985.txt line 783 s.v. nes-(1): '1. Germanic *nes-tam in Old English, Old High German \"\n                     \"(in composition), and Old Norse nest, food for a journey, akin to the possible Germanic source of \"\n                     \"Old French harnes, harness: HARNESS.' The gloss 'food for a journey' is Watkins's, but his form is \"\n                     \"*nes-tam, not *nas-ja; Watkins has no *nasja at all.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 335\", \"stance\": \"partial\",\n             \"note\": \"'Kaus. got. nasjan \\\"gesund machen\\\", ahd. nerian, nerren \\\"am Leben erhalten, retten, schuetzen, \"\n                     \"ernaehren\\\" ... ags. nest n. \\\"Nahrung, Speise\\\" ... ahd. wega-nest \\\"Reisespeise\\\"' - both \"\n                     \"formations are here, and they are distinct.\"},\n            {\"src\": \"POK\", \"where\": \"IEW pp. 766-767 s.v. nes-\", \"stance\": \"partial\",\n             \"note\": \"'Kaus. Gothic nasjan \\\"to make healthy\\\" ... latter meaning also in Old High German wega-nest, \"\n                     \"-nistu \\\"travel food\\\", Old English nest n. \\\"nourishment, food\\\", Old Icelandic nest n. \"\n                     \"\\\"provision for a journey\\\"'.\"},\n            {\"src\": \"KLN\", \"where\": \"leaf ~318 s.v. harness (KLN_1966.txt line 17243)\", \"stance\": \"partial\",\n             \"note\": \"'The second element is rel. to OE. nest, \\\"provisions\\\", and to OE., OS., OHG. nerian ..., Goth. \"\n                     \"nasjan, \\\"to nourish\\\", lit. \\\"to cause to recover\\\"' - Klein names both, which is probably the \"\n                     \"source of Nourai's conflation.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"harness\",\n          \"verdict\": \"plausible\",\n          \"derivation\": (\n            \"English harness comes from Middle English harneis/herneis, from Old French harneis, herneis, harnes (12th \"\n            \"c.), a noun of broad meaning 'arms, equipment, tackle, household gear'; the sense 'gear of a draught animal' \"\n            \"is English, from the early 14th century. The Germanic etymology is a hypothesis, not a datum: Klein gives \"\n            \"'fr. ON. *hernest, \\\"provisions for the army\\\"', first element rel. to OE here, OHG heri 'army', second \"\n            \"element rel. to OE nest 'provisions'; Watkins is careful to write only 'akin to the possible Germanic source \"\n            \"of Old French harnes, harness'; Etymonline calls the word 'of uncertain origin' and prefixes the Norse \"\n            \"etymology with 'perhaps'. Note also that only the second element belongs to *nes-, and that the reconstructed \"\n            \"*hernest is unattested. Since no source affirms the chain outright and the immediate parent in the chart \"\n            \"(*nas-ja) is in any case the wrong Germanic formation (see node #8), plausible rather than confirmed. MHG \"\n            \"harnesch (> G. Harnisch) is a re-borrowing from French, which shows how far the word travelled.\"),\n          \"derivation_fa\": (\n            \"انگلیسی harness از harneis انگلیسی میانه و آن از harneis/herneis/harnes فرانسوی باستان (سدهٔ دوازدهم) به معنی \"\n            \"«ساز و برگ، سلاح، اسباب» است؛ معنای «یراقِ چارپا» انگلیسی و از اوایل سدهٔ چهاردهم است. ریشه‌شناسی ژرمنیِ آن حدس \"\n            \"است نه داده: کلاین «نورس باستان *hernest «توشهٔ سپاه»» می‌دهد، از herr «سپاه» + nest «توشه»؛ واتکینز محتاطانه \"\n            \"تنها می‌نویسد «هم‌ریشه با خاستگاهِ ژرمنیِ احتمالیِ harnes فرانسوی باستان»؛ و اتیمانلاین واژه را «of uncertain \"\n            \"origin» و فرضیهٔ نورسی را «perhaps» می‌خواند. افزون بر این، تنها جزء دومِ آن به *nes- می‌رسد و *hernest صورتی \"\n            \"بازسازی‌شده و بی‌گواه است. چون هیچ مرجعی این زنجیره را قطعی نمی‌داند و گرهٔ پدرِ آن در نمودار (*nas-ja) هم \"\n            \"ساختِ نادرستی است، این گره «با احتیاط پذیرفتنی» است نه «درست». آلمانی میانهٔ علیا harnesch (> Harnisch) دوباره \"\n            \"از فرانسوی وام گرفته شده است، که نشان می‌دهد واژه چه راهی پیموده است.\"),\n          \"sources\": [E_HARN],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\",\n             \"note\": \"AHD_watkins1985.txt line 783 s.v. nes-(1): Germanic *nes-tam '... akin to the possible Germanic \"\n                     \"source of Old French harnes, harness: HARNESS' - Watkins gives HARNESS under the root but flags the \"\n                     \"Germanic source as only possible.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 17243 s.v. harness\", \"stance\": \"partial\",\n             \"note\": \"'ME. harneis, herneis, fr. OF. harneis, herneis, harnes (F. harnais), fr. ON. *hernest, \"\n                     \"\\\"provisions for the army\\\". The first element is rel. to OE. here, OHG. heri, \\\"army\\\" ... The \"\n                     \"second element is rel. to OE. nest, \\\"provisions\\\" ... MHG. harnest, harnas (whence G. Harnisch) ... \"\n                     \"is reborrowed fr. OF. harnais.' Klein asserts the etymology but the ON form is starred.\"},\n            {\"src\": \"POK\", \"where\": \"IEW pp. 766-767 s.v. nes-\", \"stance\": \"silent\",\n             \"note\": \"Pokorny lists ON nest 'provision for a journey' but does not mention harness or *hernest.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls (FSD_vol2/3.txt)\", \"stance\": \"silent\",\n             \"note\": \"grep '^harness' in FSD_vol2.txt/FSD_vol3.txt returns only running text from other entries; the OCR \"\n                     \"is too degraded to quote the headword's bracketed etymology.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-362.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk362.py"
}
```


### [2026-09-07T19:51:39.722Z] TOOL RESULT

```
written
```


## [2026-09-07T19:51:43.640Z] TOOL CALL #73: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-362.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 362"
}
```


### [2026-09-07T19:51:45.004Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'disputed': 1, 'confirmed': 13, 'plausible': 4}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 10, 'not_checked': 5, 'supports': 7}
books consulted: {'partial': 15, 'supports': 24, 'silent': 17} | by book: {'KLN': 10, 'WLD': 6, 'SKT': 5, 'POK': 5, 'AHD': 4, 'HUB': 3, 'BQT': 3, 'MON': 2, 'HRN': 2, 'FSD': 2, 'IEC': 2, 'PHD': 1, 'NYB': 1, 'ARY': 1, 'LEW': 1, 'LAT': 1, 'SYN': 1, 'BRT': 1, 'AFA': 1, 'AFM': 1, 'FVQ': 1, 'TAD': 1, 'LKT': 1}
```


## [2026-09-07T19:52:00.395Z] AGENT

0 PROBLEM lines. Page 362 (book p. 332) verified.

**Counts** — 2 entries (2 redirects skipped: Nerq → Ner 2, Nes 2 → Ne 2); 18/18 nodes. Root verdicts: 2 confirmed. Node verdicts: 13 confirmed, 4 plausible, 1 disputed. Ref checks: 7 supports / 10 partial / 5 not_checked. 23 books consulted (24 supports / 15 partial / 17 silent).

**Disputed**
- Ner 2 #1 Greek `narkissos` — narkē is a good reflex of *(s)ner-k- (Pok. 976f.), but the flower name is Pre-Greek: Beekes says the -ισσος suffix "clearly points to a Pre-Greek word" and the narkē link is "folk etymology"; Klein, on Nourai's own cited p. 1028, calls it "prob. of Aegean origin but was assimilated to νάρκη". The whole narges/narcissus branch is a real borrowing chain but not descent from the root.

**Plausible (with corrections)**
- Ner 2 #8 Germanic `snarwa` — no handbook reconstructs *snarwa; AHD (Nourai's own ref) prints *snarh-ōn- for 'cord, noose, trap'. He merged *snarh-ōn- 'snare' with *narwa- 'narrow'. Book prints it; extraction faithful.
- Nes 1 #8 Germanic `nas-ja : food for journey` — form and gloss belong to different formations: *nazjan- is 'to save/nourish' (Goth. nasjan), while 'food for a journey' is *nes-tam (ON/OE nest), which is what AHD nes-¹ actually prints. **Book error, not extraction** — verified on the 400 dpi page render; page image saved to `data/verification/sources/refs/ocr/BOOK/362.png`.
- Ner 2 #4 Latin (empty box) and Nes 1 #9 English harness (*hernest is unattested; Etymonline "of uncertain origin", Watkins "possible Germanic source").

**Extraction errors for the owner** — none. Two book-side notes only: the empty box drawn beside the Avestan `asta 2` node is genuinely blank in the print (JSON correctly makes no node for it), and Nourai's `SKT:344` does not match the available Skeat impression (narcissus is p. 301, Snare p. 447; p. 344 is "Per-/Petition") though Skeat's content does back the narkē link. `BQT:2129`, `BQT:2086`, `POK:975`, `POK:766` and `KLN:1028` all landed exactly on the right pages; `MON:4649` could not be page-checked (local copy is the 2-vol Adena reprint) but its entry text agrees.
