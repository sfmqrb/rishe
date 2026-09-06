# Verification process log — verify-page-272


## [2026-09-06T20:57:51.913Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 272 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-272.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-272.json. Write /home/sfmqrb/git/rishe/data/verification/page-272.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 272` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T20:57:53.346Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T20:57:54.131Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T20:57:54.146Z] TOOL RESULT

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


## [2026-09-06T20:57:54.661Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-272.txt"
}
```


### [2026-09-06T20:57:54.686Z] TOOL RESULT

```
1	=== PDF page 272 (book page 242) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Klou-ni : buttock, rump  (refs POK:607)
4	#1 (parent #0) [Avestan] refs=POK:607 | sraoni : buttock
5	  #2 (parent #1) [Pahlavi] refs=HRN:162 | sarŭk : buttock
6	    #3 (parent #2) [Persian] refs=BQT:1134 | sorŭn «سُرون ۲» : buttock | extra: سَرین
7	#4 (parent #0) [Old Persian] refs=POK:608 | slaunis : buttock
8	  #5 (parent #4) [None] refs=None | 
9	#6 (parent #0) [Latin] refs=POK:607 | clŭnis : buttock
10	--- entry 1 ---
11	ROOT Kmtom -> redirect to Dekm
12	--- entry 2 ---
13	ROOT Ko 1 -> redirect to Ak
14	--- entry 3 ---
15	ROOT Ko 2 -> redirect to Ki 2
16	--- entry 4 ---
17	ROOT Koi -> redirect to Ak
18	--- entry 5 ---
19	ROOT Koi-to -> redirect to Kei 4
20	--- entry 6 ---
21	ROOT Koksâ -> redirect to Kenk 1
22	--- entry 7 ---
23	ROOT Kolemâ -> redirect to Kolemos
24	--- entry 8 ---
25	ROOT [Indo-European] Kolemos, Kolemâ : grass, reed, cane  (refs POK:612)
26	#1 (parent #0) [Greek] refs=POK:612 | kalamos : a reed (used as a pen)
27	  #2 (parent #1) [Arabic] refs=TAD:57 | qalam : pen
28	    #3 (parent #2) [Persian] refs=MON:2715 | qalam «قلم» : pen, item | extra: اقلام
29	  #4 (parent #1) [Latin] refs=AHD:201 | calamus : reed, cane
30	    #5 (parent #4) [French] refs=AHD | caramel : burnt cane sugar
31	      #6 (parent #5) [Persian] refs=MON:2796 | kâramel «کارامل» : caramel
32	      #7 (parent #5) [English] refs=AHD | caramel
33	  #8 (parent #1) [Sanskrit] refs=POK:612 | kalama : pen
34	--- entry 9 ---
35	ROOT Kongar -> redirect to Kar 1
36	--- entry 10 ---
37	ROOT Kork -> redirect to Kerk
38	
```


## [2026-09-06T20:57:55.277Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-272.json"
}
```


### [2026-09-06T20:57:55.294Z] TOOL RESULT

```
1	{
2	  "pdf_page": 272,
3	  "book_page": 242,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Klou-ni",
8	        "lang": "Indo-European",
9	        "refs": "POK:607",
10	        "gloss": "buttock, rump"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK:607",
18	          "words": [
19	            {"translit": "sraoni", "gloss": "buttock", "script": null}
20	          ],
21	          "script_extra": null,
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Pahlavi",
29	          "refs": "HRN:162",
30	          "words": [
31	            {"translit": "sarŭk", "gloss": "buttock", "script": null}
32	          ],
33	          "script_extra": null,
34	          "note": null,
35	          "quote": null
36	        },
37	        {
38	          "id": 3,
39	          "parent": 2,
40	          "lang": "Persian",
41	          "refs": "BQT:1134",
42	          "words": [
43	            {"translit": "sorŭn", "gloss": "buttock", "script": "سُرون ۲"}
44	          ],
45	          "script_extra": "سَرین",
46	          "note": null,
47	          "quote": {
48	            "text": "چو نزدیک اسب اندر آمد ز راه - سَرونی بزد بر سَرین سیاه",
49	            "poet": "Ferdowsî"
50	          }
51	        },
52	        {
53	          "id": 4,
54	          "parent": 0,
55	          "lang": "Old Persian",
56	          "refs": "POK:608",
57	          "words": [
58	            {"translit": "slaunis", "gloss": "buttock", "script": null}
59	          ],
60	          "script_extra": null,
61	          "note": null,
62	          "quote": null
63	        },
64	        {
65	          "id": 5,
66	          "parent": 4,
67	          "lang": null,
68	          "refs": null,
69	          "words": [],
70	          "script_extra": null,
71	          "note": null,
72	          "quote": null
73	        },
74	        {
75	          "id": 6,
76	          "parent": 0,
77	          "lang": "Latin",
78	          "refs": "POK:607",
79	          "words": [
80	            {"translit": "clŭnis", "gloss": "buttock", "script": null}
81	          ],
82	          "script_extra": null,
83	          "note": null,
84	          "quote": null
85	        }
86	      ]
87	    },
88	    {"root": {"name": "Kmtom", "redirect": "Dekm"}, "nodes": []},
89	    {"root": {"name": "Ko 1", "redirect": "Ak"}, "nodes": []},
90	    {"root": {"name": "Ko 2", "redirect": "Ki 2"}, "nodes": []},
91	    {"root": {"name": "Koi", "redirect": "Ak"}, "nodes": []},
92	    {"root": {"name": "Koi-to", "redirect": "Kei 4"}, "nodes": []},
93	    {"root": {"name": "Koksâ", "redirect": "Kenk 1"}, "nodes": []},
94	    {"root": {"name": "Kolemâ", "redirect": "Kolemos"}, "nodes": []},
95	    {
96	      "root": {
97	        "name": "Kolemos, Kolemâ",
98	        "lang": "Indo-European",
99	        "refs": "POK:612",
100	        "gloss": "grass, reed, cane"
101	      },
102	      "nodes": [
103	        {
104	          "id": 1,
105	          "parent": 0,
106	          "lang": "Greek",
107	          "refs": "POK:612",
108	          "words": [
109	            {"translit": "kalamos", "gloss": "a reed (used as a pen)", "script": null}
110	          ],
111	          "script_extra": null,
112	          "note": null,
113	          "quote": null
114	        },
115	        {
116	          "id": 2,
117	          "parent": 1,
118	          "lang": "Arabic",
119	          "refs": "TAD:57",
120	          "words": [
121	            {"translit": "qalam", "gloss": "pen", "script": null}
122	          ],
123	          "script_extra": null,
124	          "note": null,
125	          "quote": null
126	        },
127	        {
128	          "id": 3,
129	          "parent": 2,
130	          "lang": "Persian",
131	          "refs": "MON:2715",
132	          "words": [
133	            {"translit": "qalam", "gloss": "pen, item", "script": "قلم"}
134	          ],
135	          "script_extra": "اقلام",
136	          "note": null,
137	          "quote": {
138	            "text": "خود قلم اندر نوشتن می‌شتافت - چون به عشق آمد قلم بر خود شکافت",
139	            "poet": "Molavî"
140	          }
141	        },
142	        {
143	          "id": 4,
144	          "parent": 1,
145	          "lang": "Latin",
146	          "refs": "AHD:201",
147	          "words": [
148	            {"translit": "calamus", "gloss": "reed, cane", "script": null}
149	          ],
150	          "script_extra": null,
151	          "note": null,
152	          "quote": null
153	        },
154	        {
155	          "id": 5,
156	          "parent": 4,
157	          "lang": "French",
158	          "refs": "AHD",
159	          "words": [
160	            {"translit": "caramel", "gloss": "burnt cane sugar", "script": null}
161	          ],
162	          "script_extra": null,
163	          "note": null,
164	          "quote": null
165	        },
166	        {
167	          "id": 6,
168	          "parent": 5,
169	          "lang": "Persian",
170	          "refs": "MON:2796",
171	          "words": [
172	            {"translit": "kâramel", "gloss": "caramel", "script": "کارامل"}
173	          ],
174	          "script_extra": null,
175	          "note": null,
176	          "quote": null
177	        },
178	        {
179	          "id": 7,
180	          "parent": 5,
181	          "lang": "English",
182	          "refs": "AHD",
183	          "words": [
184	            {"translit": "caramel", "gloss": null, "script": null}
185	          ],
186	          "script_extra": null,
187	          "note": null,
188	          "quote": null
189	        },
190	        {
191	          "id": 8,
192	          "parent": 1,
193	          "lang": "Sanskrit",
194	          "refs": "POK:612",
195	          "words": [
196	            {"translit": "kalama", "gloss": "pen", "script": null}
197	          ],
198	          "script_extra": null,
199	          "note": null,
200	          "quote": null
201	        }
202	      ]
203	    },
204	    {"root": {"name": "Kongar", "redirect": "Kar 1"}, "nodes": []},
205	    {"root": {"name": "Kork", "redirect": "Kerk"}, "nodes": []}
206	  ]
207	}
208	
```


## [2026-09-06T20:58:00.320Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T20:58:00.363Z] TOOL RESULT

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


## [2026-09-06T20:58:02.406Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','BQT','MON','TAD','AHD','WLD','BRT','KNT','PHD','NYB','HUB','ARY','IEC','SYN','KLN','SKT','FSD','WEB','FVQ','AFM','PLA','LKT','MAY','CHEUNG']:\n    if k in d: print(k, json.dumps(d[k],ensure_ascii=False)[:600])\n    else: print(k,'MISSING')\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-06T20:58:03.904Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
MAY MISSING
CHEUNG MISSING
```


## [2026-09-06T20:58:08.530Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['POK'],ensure_ascii=False,indent=1))\"",
 "description": "POK page offsets"
}
```


### [2026-09-06T20:58:10.175Z] TOOL RESULT

```
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
```


## [2026-09-06T20:58:10.309Z] TOOL CALL #7: Bash

```json
{
 "command": "grep -n \"klouni\\|kləuni\\|k'lō̆u\\|klōuni\\|sraoni\\|clunis\" data/verification/sources/refs/POK_full.txt | head -40",
 "description": "grep POK for klouni"
}
```


### [2026-09-06T20:58:10.358Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T20:58:13.508Z] TOOL CALL #8: Bash

```json
{
 "command": "cd data/verification/sources/refs; grep -n \"lemma: kl\" POK_full.txt | head -40; echo ---; grep -n \"Page(s): 60[5-9]\" POK_full.txt | head",
 "description": "grep POK_full for kl- lemmas"
}
```


### [2026-09-06T20:58:13.574Z] TOOL RESULT

```
47351:Root / lemma: klafH^ra 
47363:Root / lemma: kla- 
47396:Root / lemma: kleiR- 
47419:Root / lemma: klem-, klem-, kleUi- 
47453:Root/ lemma: kleng-a'c\6 klenk- 
47485:Root / lemma: kleno- 
47509:Root / lemma: klep- 
47526:Root / lemma: kleg-, klog- klag-, klang- kleg-, klog- kleig- kleik- 
47593:Root / lemma: klep- 
47599:Root/ lemma: klep-\ "to hold in the arms, in one's lap' derived from labial extensions 
47616:Root/ lemma: kleu- {a\so kleu-1) and klau- 
---
47705:Page(s): 608 
47719:Page(s): 608 
47754:Page(s): 608 
51524:Page(s): 605-607 
51568:Page(s): 607 
51591:Page(s): 607-608 
51843:Page(s): 609-610
```


## [2026-09-06T20:58:14.270Z] TOOL CALL #9: Bash

```json
{
 "command": "cd data/verification/sources/refs; grep -n \"lemma: kolem\\|lemma: kalam\\|kalamos\\|calamus\" POK_full.txt | head -20",
 "description": "grep POK_full for kalamos"
}
```


### [2026-09-06T20:58:14.317Z] TOOL RESULT

```
51625:Latin calamus^ reed', from which again cymr. etc. calafreed'. 
90893:"calamus Rotang' etc.;
```


## [2026-09-06T20:58:16.662Z] TOOL CALL #10: Bash

```json
{
 "command": "cd data/verification/sources/refs; sed -n '51560,51660p' POK_full.txt",
 "description": "Read POK_full around p.607-612"
}
```


### [2026-09-06T20:58:16.713Z] TOOL RESULT

```
" sweep, wash away '. 

Perhaps extension of *Rel- "humid, wet, damp', there also lie the consecutive roots of 
the basic: ^/ep-"humid, wet' (see there), klek-6s. (Lithuanian slaku, -e//"drip, trickle', slektl, 
sllknotr spray' etc.), kleg{h)- ds. (russ. s/eza "tears'. Old Church Slavic sIbzaAs.). If this 
applied, would be for kleu- : kel- the relation sreu-' flow ' : ser- either model or parallel. 

References: WP. I 495 f., WH. I 239 f., Trautmann 307. 
Page(s): 607 

Root / lemma: Rlou-nl- 
Meaning: hip 

Material: Old Indie sroni-m. f., Avestan sraonl-i. "buttock, hip, haunch'; 

Latin clOnls^ a buttock, haunch, rump of people and animals' {clunaculum^ small sword 
or dagger which one carries behind '); 

cymr. corn, clunt "hip, haunch', bret. M//? "buttock'; 



Old Icelandic hlaunx\. 'buttock'; 

Lithuanian slaunis^ femur, thigh, hip, haunch, ham ', Latvian s/auna'h'\p, haunch'; Old 
Prussian s/a^/7/5 'thigh'. 

The Lautform from gr. KAoviq, -loq ' coccyx, small triangular bone at the base of the 
spinal column ' is still unexplained. 

References: WP. I 499, WH. I 239, Trautmann 306, Specht Indo Germanic Dekl. 162. 
Page(s): 607-608 

Root / lemma: Roi-no- 

Meaning: grass 

Material: Gr. Koiva xopTO(; Hes. (perhaps Neutr. PI.); Lithuanian sienas, Latvian s/ens'hay' 

(Finnish loanword out of it signify 'hay, grass, herb'); Old Church Slavic seno^ any 

feeding-ground, pasturage, grass ', Serbo-Croatian s/jeno'hay', Old Czech seno ds. 

References: WP. I 455, MiJhlenbach-Endzelin Latvian-D. Wb. Ill 859, Trautmann 297. 

Page(s):610 

Root / lemma: Rolamo-s, Rolama 

Meaning: stalk; reed 

Material: Gr. KaAa|jO(;, KaAapn 'reed' (assimilated from koA-?); 

Latin culmus^ stem '; 

Old High German halm, halam. Old Norse halmr. Old English healm^ stem '; 

Old Prussian s5//77e 'straw', Latvian salms' straw '; 

Old Church Slavic slama {*solma, Indo Germanic *Rola-ma), russ. soloma, serb. slama 
'straw'; 

Tocharian A kulmamts- 'reed' (?). 

From gr. KaAaMO(; are borrowed Old Indie kalama- m. ' a kind of rice, writing pipe ' and 
Latin calamus^ reed', from which again cymr. etc. calafreed'. 

Maybe alb. kallam^ reed ' a Latin loanword. 
Maybe alb. kalli, kalliri^ ear of grain '. 



relationship to ^eAperliaps "tliin sliaft, arrow, stiff stem ' is wortli considering (see 552 
f.). 

References: WP. I 464, WH. I 136, 303 f., Trautmann 298. 
Page(s):612 

Root / lemma: Ronkho- 

Meaning: clamshell 

Material: Old Indie sa/jkha-m. " shell, temple, flattened region on either side of the 

forehead '; 

gr. KOYXOc;, koyxH " shell, measure of capacity '; KoxAoq, KOxAiac; " shell, snail shell, 
snail', maybe from *koyxA-; 

Latin cong/us' a measure for liquids ' is most likely a gr. loanword; 

doubtful Latvian sence' shell ', there zence seems the right form. 

References: WP. I 461 f., WH. I 260, J. B. Hofmann Gr. etym. Wb. 151. 
Page(s):614 

Root / lemma: konk- 

Meaning: to doubt; to sway 

Material: Old Indie sarjkate^ sways, doubts, is procured, fears ', sarjkita-^ anxiously,
```


## [2026-09-06T20:58:31.693Z] TOOL CALL #11: Bash

```json
{
 "command": "pdftoppm -f 272 -l 272 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg272 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render pdf page 272"
}
```


## [2026-09-06T20:58:32.943Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN leaf for p.162 (leaf=162+21=183) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==184' HRN.txt | head -60",
 "description": "Read Horn p.162"
}
```


### [2026-09-06T20:58:33.915Z] TOOL RESULT

```
total 2380
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 16:58 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    264 Sep  6 16:57 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb  95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb  25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb  43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb  23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb  10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb  10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb  24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb  63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb  11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb  10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb  19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb  19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb  12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb  14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb  25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb  17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb 105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb  84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb  92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb  13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb  69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb 122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb  68566 Sep  6 16:58 pg272.png
```


### [2026-09-06T20:58:35.885Z] TOOL RESULT

```
=== HRN leaf for p.162 (leaf=162+21=183) ===
— 162 -
732. siristen 'niisclien, vermengen; schaffen, bilden, sirls
{*sires)j siriäem 'Leim* *).
aw. l^sraes- , sraesyeiti 'sich an etwas hängen ;
phlv. sristan^ sresct (PPGh); ai. skr. [/^rres-^ (^les-^
rlisyatl Verbinden, zusammenfügen'.
sar. xlr/'am ^vermischen, mengen etc.'
733. sirUk "Tropfen .
aw. sraska- 'Hagel' (Justi); für srasc- nimmt
Geldner, KZ. 27, 252 die Grundbedeutung giessen*
an, aw. sraska- bedeutet vielleicht 'Reif, Nebel'.
Unsicher.
734. serTfy sm% serfm *Horn'.
aw. srvä' *Klaue, Hörn'; phlv. srüh (d.i. srtn^), snw.
bei. srunbe^ surum 'Huf (348) -).
7»>r>. suvTiden singen, Praes. seräy-em^ seräf/tden 'singen;
sprechen (Sahn. I, 70 Vers 156), seräyis^ siirüd Lied'.
aw. l'^sruv-, (^aus. srävayeüi; phlv. srüfan 'recitiren',
srayltan^ sräy(i)su^ srüt 'Gesang; ai. l/'grav-^ Caus.
^rävdyati.
wa/. sirav-am^ sar. nasrav-am 'recitiren*.
736. seröä 'Engel' (Vis und RämTn, S. 37, V. 4 v. u.).
aw. Sraosa-; phlv. Srös, vergl. asrös ungehorsam*
(aw. asraosa-),
737. snrTniy surtn 'Hinterbacken, Hinterer.
aw. sraoni- *Hüfte*; phlv. sarük, vd. 8 (178) (181),
sarin 'Hinterer (Bund.) , sar'mak (PPGl.) ; ai. grmü'
'Hinterbacke, Keule, Hüfte'; lit. szlaimis, lat. cliinis,
gr. XA0I7C,' (?), ahd. hlatm ^).
bei. saren 'Lenden, Hüften* (338, wohl in sarzn zu
ändern, vergl. Hübschmann, ZDMG. 44, 555 unter
No. 2) ; wa/. simj, siyn. saun, sar. xdiin,
738. seztden sich ziemen, passen, sezä, sezäyiden.
phlv. sacifan^ sacPt (päz. sazed, saSSd), sacäk.
*) Afy. LW. s(fle/ -, i<(dex'
^) Geiger wirft np. sum^ suub *Huf* fälschlich mit serüu *Horn*
zusammen; vergl. No. 745.
*) Arm. srunl^ ^Schienbeine, Waden', das auch seiner Bedeutung
nach nicht paast, gehört nicht liierher (Fl übschmann, No. 260).
```


## [2026-09-06T20:58:43.639Z] TOOL CALL #13: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg272.png"
}
```


### [2026-09-06T20:58:44.110Z] TOOL RESULT

```

```


## [2026-09-06T20:58:44.107Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T20:59:02.412Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; mkdir -p ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg272.png ocr/BOOK/272.png; echo copied\necho \"=== POK_02 leaf 263 (p.607) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==264' POK_02.txt | sed -n '1,80p'",
 "description": "Copy page PNG and read POK p.607"
}
```


## [2026-09-06T20:59:03.390Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD kleu-ni / kolem ===\"; grep -n -i \"klou-ni\\|kleu-ni\\|kolǝmo\\|kolemo\\|kola-mo\\|calamus\\|culmus\" AHD_watkins1985.txt | head -20",
 "description": "grep AHD Watkins"
}
```


### [2026-09-06T20:59:04.417Z] TOOL RESULT

```
copied
=== POK_02 leaf 263 (p.607) ===
len':
got.  hlifan  ,stehlen'  {Jiliftus  ,Dieb*);
mir.  cluain  (*klo'pni-)   f.  ,Betrug,  Schmeichelei',   cluainech   ,trügerisch* ;
apr.  auklipts  {^-kUptös)  ,verborgen' ;  s.  auch  unter  klep-.
Mit  anlaut.  sl-  aus   skl-  scheint  verwandt  \\i.  slejpiil,  slepti   ,verbergen*.
Die  Bedeutung  macht  wahrscheinKch,  daß  klep-  Erw.  von  kel-  ,Ter- bergen'  ist;  mhd.  hulft  ,K(3cher'  scheint  geradezu  Tiefstufe  unserer  Wurzel- form zu  sein,  wie  apr.  auklipts  ]  apr.  aukli'pts  zeigte  dann  westidg.  Guttural.
WP.  I  497,  WH.  I  232,   Trautmann  137.
klep-  ,mit  den  Armen  und  im  Schoß  zusammenhalten'?
Mhd.  läfter  , Klafter',  lett.  küpis  ,Schoß,  Schoßvoll',  lit.  kUbys  ,Arm-i weite,  Klafter,  Armvoll'  (b  vielleicht  nach  gUbys  ,Armvoir).
Anlautvariante  neben  lit.  gUbys^  nhd.  Klafter?  (s.  oben  S.  359  unter  ^«Z- ,ballen').  —  Ahd.  halftra  ,Halfter',  lit.  kilpa  , Schlinge,  Steigbügel*  (Persson) s.  unter  skel-  , spalten'.
WP.  I  498,  Büga  Kalba  ir  s.  I  71,  Mühlenbach-Endzelin  II  224.
kleu-  (auch  kUu-?)  und  kläu-,  vielleicht  eigentlich  , Haken,  krummes  Holz oder  Astgabel,  Pflöckchen',  verbal  einerseits  ,anhaken   (sich  anklam- mern), hemmen,  auch  von  hinkendem  Gange',  andrerseits  , durch  einen vorgesteckten  Haken,  Riegel,  ein  Pflöckchen  verschließen'. Gr.  ion.  -KXrftg  -TSog^  altatt.  yiXrjg,  att.  x^€/g,    dor.  ytXä'tg,  -tdog  ,Schltissel' (auch  ,Riegel;  hakenförmige  Öse;  Ruderdolle'),  dor.  sekund.  xAa^,  epidaur. Gen.  xAatjcog  ds.,  xAi^tw   (ion.),  xA^w  (altatt.),  yiXsLO)  (att.)  ,verschließe  mit einem   Balken,   einem   Riegel,   einem   Schlüssel',   ytXrj'L-d^gov   (ion.),    -aXrjd^QOv (altatt.),  yXeZdQOv  (att.)  , Verschluß';
lat.  clävis  , Schlüssel',  Demin.  cläviculae  ,Wickelranken  des  Weins', clävus  ,Nagel  (zum  nageln)  :  Steuerruder,  Ruderpflock',  claiidö,  -ere ,schließen,  sperren'  {*kläui-dö,  mit  präsensbildendem  d) ;  dazu  wohl  claudus ,.lahm,  hinkend'  (zu  clüdus,  clödus  s.  WH.  I  231),  claudeö,  -ere  ,hinken'. air.  clöj  PL  clöi  ,Nagel';  unklar  mcjmr.  clo  ra.  ,Riegel,  Verschluß',  PI. doeu  ,clavi',  mbret.  clou  ,ferrement'  (Ernault  RC.  37,  104 f.);
aus  dem  Germ,  wohl  hierher  (mit  beweglichem  s-)  ahd.  sliozan,  mnd. slüteuj  afries.  slüta  , schließen',  ahd.  sluzzil,  asächs.  slutil  , Schlüssel',  ahd. sloz  n.  ,S
```


### [2026-09-06T20:59:04.459Z] TOOL RESULT

```
=== AHD kleu-ni / kolem ===
642:h. Anglo-Norman aloper, to run away from one’s hus- band with a lover: ELOPE. kneigwh-. To lean on. 1. Latin cdnivére (< *con-niguére; com-, together; see kom), “to lean together” (said of eyelids), to close the eyes, be indulgent: CONNIVE. 2. Suf- fixed zero-grade form *knigvh-to- in Latin nictdre, to move the eyelids, wink: NICTITATE. 3. Uncertain preform in Latin niti, to lean forward, strive: NISUS; RENITENT. [Pok. knei-geh- 608.] knid-. Egg of a louse. Suffixed form *knid-d in Germanic *hnito in Old English hnitu, egg of a louse: NIT. [Pok. knid- 608.] ko-. Stem of demonstrative pronoun meaning “this.” I. Variant form *ki-. 1. Germanic *hi- in: a. Old English he, he: HE!; b. Old English him, him: HIM; c. Old English his, his: 1s; d. Old English hire, her: HER; e. Old English Ait, it: 1r. f. Old English hér, here: HERE; g. Old English heonane, heonon, from here: HENCE. 2. Suffixed form “ki-tro- in Germanic *hi-thra- in Old English hider, hither: HITHER. 3. Suffixed form *ki-s in Latin cis, on this side of: cis-. II. Variant form *ke-. 1. Preposed in *ke-etero- (*e-tero-, a second time, again; see i-) in Latin céterus (neuter plural cétera), the other part, that which remains: ET CETERA. 2. Latin -ce (see nu-). III. Attrib- uted by some to this root (but more likely of obscure origin) is Germanic root *hind-, behind. 1. Old English bihindan, in the rear, behind (bi, at; see ambhi): BE- HIND, HIND!. 2. Old High German hintar (> German hinter-), behind: HINTERLAND. 3. Germanic derivative verb *hindron, to keep back, in Old English hindrian, to check, hinder: HINDER}. [Pok. ko- 609.] k6-. To sharpen, whet. Contracted from *koo-. 1. Suffixed extended form “kooi-no- in Germanic *haind in Old English hdn, stone: HONE!. 2. Perhaps Greek kénos, cone, conical object (< “a sharp-pointed object”): CONE. [Pok. Aéi- 541.] kob-. To suit, fit, succeed. Germanic *hap- in Old Norse happ, chance, good luck: HAP, (HAPPEN), (HAPPY); (HAP- LEss), (MISHAP). [Pok. kob- 610.] [kokkos. Kermes berry, pit, grain. Greek noun of un- known origin: COCCID, COCCUS, COCHINEAL; MONO- COQUE.] koksa. Body part. Latin coxa, hip: Coxa, CUISSE, CUSH- ION. [Pok. koksd 611.] kolem-. Grass, reed. Suffixed form *kolsm-o-. 1. Ger- manic “*halmaz in Old English healm, halm, straw: HAULM. 2. Latin cudmus, stalk: CULM!. 3. Zero-grade form “kibpm-o- in Greek kalamos, a reed, straw: CALA- MITE, CALAMUS, CALUMET, CARAMEL, SHAWM. [Pok. kolomo-s 612.] koli-. Glue. Suffixed variant form *koly-a in Greek kolla, glue: COLLAGE, COLLO-, COLLODION; PROTOCOL. [Pok. Rolfeji- 612.] kom. Beside, near, by, with. 1. Germanic *ga-, together, with (collective and intensive prefix and marker of the past participle), in Old English ge-, with, also participial, collective, and intensive prefix: ENOUGH, HANDIWORK, YCLEPT. 2. Latin cum, co-, with: CUM; CONQUIAN. 3. Old Latin com, with (collective and intensive prefix): co-, com-. 4, Suffixed form *kom-trd in Latin contra, against, opposite: (CON!), CONTRA-, CONTRARY, (COUNTER!), COUNTER-, COUNTRY; ENCOUNTER. 5. Suffixed form *kom-yo- in Greek koinos, common, shared: COENO-; CENOBITE, EPICENE, KOINE. 6. Reduced form *ko- (see gher-', mei-', smei-). [Pok. kom 612.] konemo-. Shinbone, bone, Reduced form *kemmo- per- haps in Germanic *hamma in Old English hamm, ham, thigh: HAM. [Pok. konamo- 613.] konk-. To hang. 1. Germanic *hanhan in: a. Old English hon, to hang: HANG; b. Dutch (dialectal) hankeren, to long for; HANKER; ¢C. possibly Middle English he(e)ng, hinge, hinge (ultimately from the base of Old English hangian, to hang): HINGE. 2. Suffixed form *konk-t-d- in
1329:CAKE kak-2 CALAMITE kolem- CALAMITY kel-1 CALAMUS kolem- CALANDO ghé- CALDRON kele-1 CALENDAR kele-2 CALENDER skel-3 CALENDS kel@-2 CALENTURE kele-1 CALIBER ped-! CALIX kal-1
```


## [2026-09-06T20:59:14.816Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD klouni ===\"; grep -o -n \"klouni-[^]]*\\]\\|kleuni[^]]*\\]\" AHD_watkins1985.txt | head; grep -o \"kl.\\{0,4\\}ni-\\. [A-Za-z ,.\\\"“”*-]\\{0,300\\}\" AHD_watkins1985.txt | head -5\necho \"=== AHD caramel index ===\"; grep -o \"CARAMEL [a-z-]*\" AHD_watkins1985.txt | head",
 "description": "AHD klouni + caramel"
}
```


## [2026-09-06T20:59:15.408Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT sraoni ===\"; grep -n \"sraoni\" BRT.txt | head -20",
 "description": "grep Bartholomae sraoni"
}
```


### [2026-09-06T20:59:16.661Z] TOOL RESULT

```
=== AHD klouni ===
=== AHD caramel index ===
CARAMEL kolem-
```


### [2026-09-06T20:59:16.706Z] TOOL RESULT

```
=== BRT sraoni ===
15856:•  j.,  g.  pasav-  -.ßav-  m.  'Vieh,  domestizirtes vierfüssigcs  Tier,  Haustier',  Sing,  auch  kolL : azsm  .  .  tJ  nipayanl .  .  ya^a  'sßm  pasa.- vastr?m  (sd.)  Vtj.  89;  —  ki  mH  'sSui ^ mS  nä  >rat3  vists  .  .  axdä  (sd.)  .  .  Y. 50.1;  — /su  F.5(?)";  —  im  Gegensatz 2U  nar-  oder  vira-:  'svamca  naramca  Y. 4-  S  i  —  y^  "^J  'P^  •  ■  °fli»t  vä  narim vä  raiiyät  W. 13.^1;  32;  —  västryehys •sSui  vTräatiä  (sd.)  Y.  JJ.  1 5 ;  —  va/  virpt^ ahmäksng  frada^ai  (sd.)  J  Y.  4:5.  9;  — pairT  'sUs  pain  vlrSng  dadtmahl  Y.  JÄ 6.  a)  in  Dual  Verbindung  mit  vJra-  (sd., audi  fdSt):  -j*  vlra  *Yt.  y.  iz  usw.;  — 'Tirä  Wrayi  Vr.7.3usw,;  —  'subya  vTraäbya V.6.^2.  A)  insbes.  vom  Kleinvieh,  den Schafen  und  Ziegen,  im  Gegensatz  zu staora-  (sdj:  -svamca  staoranameä  masyl- nqmca  sünqmla  vayqmca  V.  2.8;  10,  Äiz, 13;  —  °vasca  (als  NP.)  staoräea . .  masyäca bmngra  Yt.5.89;  Äs,  V.2.8,  9,  11,5.5, 6,  15;  —  °sv5  (AP.)  staeräca  V.  p.  39=;  — •subya  staoralibya  vayafibya  patantaäbya (sd,)  YL  /o.  119;  —  's}ul*g?ribui  ysistahe (sd.)  A.J.  3;  — -pania-dasa  °svs  sraoni.masa F. 25b(?); —  *hvBiSa^a{&A.)  'sus./iva^'> N.  5>V;  —  mit  anumaya-  (sd.):  ustrahe  . . aspahe  .  .  gSuI .  .  mtfnumat  ap?r3näyBk»in yaoida^S  °sSul  ^g^nbus  anumayeke  V.  9. 38 ; 2.  24;  —  bis  hapta  "vö  (AP.)  anumaya  . . fiissrinuyäi  V,  i4- 16.  a)  spez.  als  Opfer- tier: zadhrä  hE ushärayfti .,'sum  hl pacaym
```


## [2026-09-06T20:59:22.897Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"sraon\\|Sraon\" BRT.txt | head -20; echo \"=== Hüfte ===\"; grep -n \"Hüfte\\|Hinterbacke\" BRT.txt | head -20",
 "description": "grep BRT sraon / Hüfte"
}
```


### [2026-09-06T20:59:22.957Z] TOOL RESULT

```
15856:•  j.,  g.  pasav-  -.ßav-  m.  'Vieh,  domestizirtes vierfüssigcs  Tier,  Haustier',  Sing,  auch  kolL : azsm  .  .  tJ  nipayanl .  .  ya^a  'sßm  pasa.- vastr?m  (sd.)  Vtj.  89;  —  ki  mH  'sSui ^ mS  nä  >rat3  vists  .  .  axdä  (sd.)  .  .  Y. 50.1;  — /su  F.5(?)";  —  im  Gegensatz 2U  nar-  oder  vira-:  'svamca  naramca  Y. 4-  S  i  —  y^  "^J  'P^  •  ■  °fli»t  vä  narim vä  raiiyät  W. 13.^1;  32;  —  västryehys •sSui  vTräatiä  (sd.)  Y.  JJ.  1 5 ;  —  va/  virpt^ ahmäksng  frada^ai  (sd.)  J  Y.  4:5.  9;  — pairT  'sUs  pain  vlrSng  dadtmahl  Y.  JÄ 6.  a)  in  Dual  Verbindung  mit  vJra-  (sd., audi  fdSt):  -j*  vlra  *Yt.  y.  iz  usw.;  — 'Tirä  Wrayi  Vr.7.3usw,;  —  'subya  vTraäbya V.6.^2.  A)  insbes.  vom  Kleinvieh,  den Schafen  und  Ziegen,  im  Gegensatz  zu staora-  (sdj:  -svamca  staoranameä  masyl- nqmca  sünqmla  vayqmca  V.  2.8;  10,  Äiz, 13;  —  °vasca  (als  NP.)  staoräea . .  masyäca bmngra  Yt.5.89;  Äs,  V.2.8,  9,  11,5.5, 6,  15;  —  °sv5  (AP.)  staeräca  V.  p.  39=;  — •subya  staoralibya  vayafibya  patantaäbya (sd,)  YL  /o.  119;  —  's}ul*g?ribui  ysistahe (sd.)  A.J.  3;  — -pania-dasa  °svs  sraoni.masa F. 25b(?); —  *hvBiSa^a{&A.)  'sus./iva^'> N.  5>V;  —  mit  anumaya-  (sd.):  ustrahe  . . aspahe  .  .  gSuI .  .  mtfnumat  ap?r3näyBk»in yaoida^S  °sSul  ^g^nbus  anumayeke  V.  9. 38 ; 2.  24;  —  bis  hapta  "vö  (AP.)  anumaya  . . fiissrinuyäi  V,  i4- 16.  a)  spez.  als  Opfer- tier: zadhrä  hE ushärayfti .,'sum  hl pacaym
27233:•  j.  sraonay-  f.  'Hinterbacken':  haoyam (bz.  dafin?m,  sd.)  'nJtn  V.  8.  56-58*, <).2of.';  —  '«/(ND.)  F.^g.
27235:•  j.  sraont.masah-  Adj.  'von  der  Grösse eines   Hinterbackens':    asttm  .  .   'sarpA^m
=== Hüfte ===
3987:■  j.  aiwylnhana-  n.  i)  'Gürtel,  Gürtel- schnur'*>:  'n^m  r3  aiwya»hayamnS  'mm bO/ayarnnS  (sd.)  Yti.iT,  —  /rä  i! mazdä  harat  ..  'n^m  ..  vanuhim  daSnqm mäzdayasnlm  "dir  (dem  Haoma)  brachte M.  einen  Gürtel  . .,  (näml.)  die  gute mazday.  Religion"  Y.9. 26'*;  —  yat  alle yö  mazdayasnS  ap^rmäyBks  avi  hs  hapta ■na  /rajasäiti . .  °nö "'  paitis  h!  maiayai bU)yamanS  avi  hlnara pascaili  tamauhmti 'wenn  dem  jungen  Masday.  sieben  Jahre vergangen  sind,  soll  man  ihm  den  Gürtel um  die  Hüften  legen,  worauf  ihn  die Männer  (als  ihresgleichen)  achten"  Vd, 18;  20'; — jairyö  °nö  ißjyamanff  "vieitem legt  man  (dem  Toten)  die  Gürtelschnur um"  Vd. /23),  a)  von  der  Schnur,  mit der  die  Barvsmanzvreigt  in  Bündel  zusam- mengebunden werden"":  a^a  'na  N. ioS(?).  2)  'Gewand,  Kleid';  ^5  iama *°«o"  aiitryia^qyanii  "wenn  zwei  gleiche Kleider  anziehen"  N.p4(?);  — yaii  tarasca 'na  aipi.vancainii'^.gs^); — bilyS  ant?ma 'nH  "zweitens  (soll  man  dem  Toten  mit- geben) das  Untergewand"  Vd./i>3'.
8587:'»  Nach  F.  z/b  islaiacorj)  die  iweite  Hüfte des  Tags  (im  Gegensatz  zur  Nacht),  die  ihrer- Mits  nieder  in  tajt&uän  und  uiayar'm  zerfallt ;
15095:•  j.  paiti-ätäna-,  "stana-**  n.  i)  'Stand- ort, \V'ohnstätte':  h5  imqm  dalnam  .  ./ra- pinaoiti  sattm  *°i'tananqm{G?.)''' hazannm faiti.daranqm  "der  bringt  diese  Religion zum  Gedeihen,  hundert  (neue)  Wohnstätten, tausend  (neue)  Aufentlialtsorte  (sinds  die er  ihr  schafft)"  V.^.3i)>.  2)  '(Gestell sva.)  Bein',  vom  Fuss  bis  zur  Hüfte:  'stäna F.Jg;  —  maihySi  'slUne  xräidisme  maiöyöi nars  vandusme  "bis  zur  Mitte  des  Beins (der  Beinhöhe)  in  hartem,  bis  zur  (Leibes)- mitte  eines  Mannes  in  weichem  Erdboden" V,Ä8;  *H.86.
16095:•  j.  p3r«9'u.sraoiiay-  Adj.  'mit  breiten Hüften':  vayuS  .  .  •nisYti5.54.
27233:•  j.  sraonay-  f.  'Hinterbacken':  haoyam (bz.  dafin?m,  sd.)  'nJtn  V.  8.  56-58*, <).2of.';  —  '«/(ND.)  F.^g.
27234:KompA.,  E.  —  ai.  ir.may-  ni,,  f.  'Hüfte',  np. snrün  'Hinterbacken,  -leJI'.  —  Pü. :  srenak, (zu  V.  9.  10) :  "sinak  'Brust'.
27235:•  j.  sraont.masah-  Adj.  'von  der  Grösse eines   Hinterbackens':    asttm  .  .   'sarpA^m
27510:•)  Das  »on  der  linken  Hüfte  über  die  rechte Schulter  lief  und  insbetondere  «um  Tragen  des Köchen  dienie:  TgL  auf  der  Inschrift  toq  Ba- Aiitän  die  Figur  dei  hinter  dem  KOnig  ctehen- den  renere.
27615:•  '}.  zaSah-,  zadah-  m.  ('Hinterbacken'), Du.  'Steiss':  frä  %wqm  'danha  paili uzuxiäne{%d.)  Yt/p.  50;  —  *tarf/ia-Y.3g.
28921:—  Pü.:  -ijj/t),  ^<x  F.  mit  der  np.  Glosse: sarmgäh  i  sanan.  —  ')  haxt-  nnd  ai.  säklh-i decken  sich  nicht;  s.  S  3.  i,  3^8.  3.  Urir. haxl-  mag  sein  t  dem  Eintluis  van  tat-  'Kno- chen', mpUty-  'Hüfte'  Tcrdanlteo.  —  >)  Kasus?
```


## [2026-09-06T20:59:24.041Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD sarug/sarin ===\"; grep -n \"sarūg\\|sarug\\|sarrūn\\|sarēn\\|sarin\\|buttock\\|haunch\" PHD.txt PHD_mackenzie.txt | head -30",
 "description": "grep MacKenzie for buttock"
}
```


### [2026-09-06T20:59:24.097Z] TOOL RESULT

```
=== PHD sarug/sarin ===
PHD.txt:396:hannàm [%7m | = M] = handām. Harborz [Albwic | N Alburz] the mountain range surrounding the world. harg [hlg | cf. M bie, Аг. xarj, xaraj] duty, tribute; work, effort. *harrób- [hlwp- | M hrwb-] collect, gather. —išn(ih): collection, gathering. har(w) [KRA < A АР; hl | M been, N har] all, each, every. harwin [%/wyx! | M hrwyn] pl. al. harwisp [Ahlwsp! | M hrwsp] all. ~in [-yn'] pl. all. harzag [hick! | N harza] loose, free. has®r [Ps] = Av. háóra-] a measure of time (unequal hour, ze of day- light); a measure of length (— frasang, or 1 frasang, 1 mile). haspin [hspyn! | = M] rest, repose. hast, ~ih [AY T!, -yh] = tast, ~ih. hašāģird [kP klt! | M APgyrd, N šāgtrd] disciple, pupil. hast [h#! | = M, N ~] eight. ~ad [80 | N ~] eighty. ~dah [лаһ | N ~, higdah] eighteen. lhàwan [h?wn! | N +] a mortar. *hawan [/?zn! = Av. háwani-] the morning gdh. hāwand [/?wnd | M ÞPw(y)nd] like, similar. ^h: likeness, similarity. hāwišt [h’wst'] disciple, pupil. ~ih: disciplehood. haxt [h()At'] thigh, haunch, hip. hāxtan, hàz- [/7htn', h'e-] lead, guide, persuade, convert. ~išn: persuasion, conversion. hazār [1,000, hel | M h?r, N ~] thousand. ~ag LEI | N ~a] millennium. hazzān [?/h2’n'] tomb, ossuary. hên [Ayn! | M hyyn] army. ~ih: attack, aggression. hérbed [%y/pt! | N hérbud] teacher-priest. ~ih: priestly office. hērbedestān [hylptst’n'] priestly school. ~ih: priestly studies. hérig [hylyk' | N h/xéri] iris, wallflower. hézag [Ayck! | (M hyjg), N лег] pail. hil-, —išn, v. histan. hindüg [Andwk! | M hyndwg, N hindi] Indian. ~ап [-°п!] India. hištan, hil-, (P hirz-) [S BKWN-tn! < A У #9; (hlc-) | M hyštn, hyl-, (P Ayrz-), N —] let, leave, abandon, pardon, set, appoint. ~išn: pardon, loosing. hixr [hyhl] excrement. hixtan, hanj- [Ayhtn', hne- | P hxt] draw (water).
PHD.txt:430:kē(x)šīdan, kū(x)š- [kz(4)$-ytn! | M htos-ydn, N kēšīdan) strive, struggle, endeavour. ~iSn: strife, combat. ~iSnig : energetic. Кбу [kwd | N ~] street, lane. ki [AYK < A’yk | M kw, N kū, hi] where; that; than, ~ Буар [N лија] where. ~ tā: so that. kūč(ak) [Awe(k!) | N kūčak] small. kak [kwk'] small, short. kulāčag [kwľck' | N kulīča] small, round bun. kulāf [kwl”5 | N kuláh] cap, bonnet. ~ak [-k!] | N ~hak] little cap; calyx. kulang [Ring | N ~] crane. kullag [kwlk'] locust. kumig [Awmyk'] stomach. kun-, -išn, v. kardan, kunišn. кар [STE < A *st-h; kwn! | N ~] rump, buttocks, anus. kundāģ [knd^k! | M qnd’-, N kunda] magician, soothsayer. ~ih: magic, astrology. kundur [kwndl | N ~] frankincense. kunišn [kwnsn' | M kwnyšn] action, deed. ~gar LA | M -gr] doer, performer. kunjid [ŠM% < А пг; kwnc(y)t! | N ~] sesame. kün-marz [Rzonmlc] sodomite; sodomy. kurkum [kwlkwm] saffron. kurrag [kwlk' | N ~a] foal, colt. 1kust [Ruwst!] side, direction; district. kust [kwst' | Ar. qust] costus. kustag [kwstk! | M Rwstg] = !kust. ~bed [-pt'] district-commander. kustig [kwstyk! | N ~i] sacred girdle. kuštan, kuš- [NK SWN-tn! < А V nks; kwi-tn! | M kwšt, kws-, N ~] kill.
PHD.txt:1128:buttock kin.
PHD.txt:2225:haunch haxt,
PHD_mackenzie.txt:2879:haxt [hC)ht l ] thigh, haunch, hip.
PHD_mackenzie.txt:3353:kiin [STE < A ·ft-h; kW1Z I IN,...,] rump, buttocks, anus.
PHD_mackenzie.txt:6126:breath damisn, wad, wen; short of --   buttock kun.
PHD_mackenzie.txt:6737:guilty, be""" of pesar budan.            haunch haxt.
```


## [2026-09-06T20:59:35.289Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== NYB srēn ===\"; grep -n \"srēn\\|srenak\\|sren\\b\\|sarēn\" NYB_vol2_glossary.txt | head -20",
 "description": "grep Nyberg for sren"
}
```


### [2026-09-06T20:59:35.342Z] TOOL RESULT

```
=== NYB srēn ===
```


## [2026-09-06T20:59:36.706Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT v2 pdf-page tags near printed 1134 ===\"; grep -n \"سرون\\|سُرون\\|سرين\" BQT_v2_pages.txt | head -20",
 "description": "grep Borhan v2 for سرون"
}
```


### [2026-09-06T20:59:36.760Z] TOOL RESULT

```
=== BQT v2 pdf-page tags near printed 1134 ===
520:   ‫‏‪۲ ۱ Jl andhara‬نونک للاسم رد‌عقاوم«باجنپ هدودح‪.‬یکسرون ‪ ۱۱ ۰۹۲4‬‏‪G.‬ها‪11‬خا‪_1‬‬
917:  ‫وجزیره ایت درمیان دربا؟‪ -۱‬و انسرون دهابرا‬          ‫تکلتمایی است که هوشنک درعلم حکمت‌عملی‬
4393:     ‫سرون آوردن آب وحر آن کنند‪-‬‬                            ‫کودی استوانه شکل عم‌قی که در زمن جهت‬                    ‫‪۱‬‬
10801:                                                          ‫حر بواز ‪ = ۳‬بکرثالث بروزن سروناز‪,‬‬
14533:                                                                          ‫سرونی‌درفهرست‬
14825:           ‫آن ازقاعده سرون نباشد (‪ - )۲‬ک‬                           ‫ونای فارسی بروژن زردوزی ‪ ۲‬نمعدی بوسه باشد‬
20975:                           ‫دوران سرون هم میگوبند ‪.‬‬                                                                                ‫است‬
20991:‫دروان سرون ‪ - ۲‬بممنی‌دوراسران‬                                                                                                   ‫باشد ‪-‬‬
21016:  ‫"‪« .‬دو؟ بمعنی دوغ‬                            ‫رك‪ :‬دودان سرون ‪.‬‬         ‫‪۶‬‬             ‫مأخوذ از (عر)‪. ‎‬‬                    ‫‪٩‬‬
27458:   ‫است کوشتخوار از نژادکر به که از تن اومایع معطری مشکبوی تراوش کند واز زبردم او سرون‬
29144:              ‫‪ - ۳‬زم [ کوشت ] درون وبسرون دهان باشد ‪ .‬رود کی (سمرقندی) گوید ‪:‬‬
30937:                  ‫چون غوره بخامی اسرون محکم ‪.‬‬               ‫چون ژاله بسردی اسرون موصوف‬             ‫‏*‬
33426:              ‫خواییده راکوبند ‪- ۷‬جو‬                  ‫شیر را یز ستاغ میگویند؟ و‪-‬بمعئی سرون‌هم‬
35195:                    ‫وسرهای آن از عمارت سرون باشد‪.‬‬                                                           ‫باريكك همواز راکوبند‪.‬‬
35688:   ‫فلروشته مشود ) دربهلری بمعنی شاخی (سروین)است « هوبشمان ‪ .۶۳۷۰‬ورك ‪ :‬سرون‪.‬‬                 ‫‪0‬‬
35887:‫که شاخ‬        ‫است‬   ‫سرون‬       ‫ثالث و تحتالی ‪« ۰‬معنی‬
35917:             ‫فظرسی «سرین» ‏ بلوچی ‪ 06725‬از ‪ # 6۳5‬و فارسی «سرون »از ‪ ۵ 00۲5‬بر‬
35919:               ‫گرچه برتابد آن میان وسرون‪.‬‬                      ‫کفش با سلاح بشکفتم‬
35922:   ‫‪ - ۷‬مصحفهسد که»‬                ‫‪ -‬رك‪ :‬سرون ‪٩‬‏ سرین ‪.‬‬            ‫‪ _ ۵‬رك ‪ :‬سرو ‪ ۰‬سرون ‪.‬‬
36099:    ‫‪ ۳‬سرون (ه‪.‬م‪.).‬‬     ‫‪۳‬‬           ‫رك ‪ :‬سلیقون ‏ زرفون‪.‬‬        ‫‪۴‬‬             ‫ره‬     ‫ارك‬
```


## [2026-09-06T20:59:42.210Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=35925 && /\\[pdf page/{p=$0; n=NR} END{}' BQT_v2_pages.txt; grep -n \"\\[pdf page\" BQT_v2_pages.txt | awk -F: '$1<35925' | tail -3; echo \"---- context ----\"; sed -n '35880,35930p' BQT_v2_pages.txt",
 "description": "Find BQT v2 page for سرون"
}
```


### [2026-09-06T20:59:43.922Z] TOOL RESULT

```
---- context ----
‫سوروبرا یزکوبند که شاخپای آن بهر طرف‬                    ‫بآرتش و مرداد براشجار وبافی سروشرابمحافظت‬
                                                       ‫آیچه در بل نام آن سروش مقرر ات ‪ -‬ونام‬
                                        ‫ماوزسیقی ‪.‬‬      ‫ن بدست‌اوست‬   ‫اند‬‫گست ب‬
                                                                             ‫ملکی دز هست که ربا‬
                                                       ‫و تدییر امور و مصالحی که در روز سروش وافع‬
   ‫کوون‬
      ‫سروق = بفتح اول وضم اسنی‬
‫که شاخ‬        ‫است‬   ‫سرون‬       ‫ثالث و تحتالی ‪« ۰‬معنی‬
                                                         ‫رموز حفدهم باشد‬
                                                                       ‫است ‪ -‬و نا‬     ‫لق‬
                                                                                       ‫عدو‬
                                                                                         ‫تب‬‫عود‬
                                                                                             ‫می‬
                                                       ‫از هرماه شمسی ‪ .‬نك است دراعن روزدعا کردن‬
‫ویضم اول سرین و کقل‬        ‫‪-‬‬    ‫کوسفند و کاوباشد ©‬
                                                                   ‫ونبشآکده رفتن و بافی امور بداست‪.‬‬
                                    ‫هرد وچاروا ‪٩‬‏ ‪.‬‬

‫سر و یس د بااول و تحتالی مجپول بر‬                        ‫وه ‪ = ۱‬بن اولوفتح شین‌رشت‪.‬‬
                                                                                  ‫سر ش‬
‫وزن نوکیسه » قوس قزح رکاویند ‪ - ۷‬ومهر‬                    ‫بممنی سروش است جکبهرئیل باشد خصوصاً ‪-‬‬
                    ‫های سنگین را هممیگوند ‪.‬‬                                   ‫وملائکةٌ دیگر عموماً ‪.‬‬
‫سر ‪ = ۵‬بفتح اول وثالی » زر رایج تمام‬                     ‫سر ول ‪ -‬بفتح اولبروزن ملول‪ ,‬بمعنی‬
 ‫تسف‬    ‫عبار باشد»وآن نقیض قلب است که اسره‬               ‫حقد باشد»‌وآن بدکوبی و غیبت مردم در خاطر‬
‫‪ -‬وآب عمیقی که از سر مردم بگذرد ‪ -‬و هر‬                   ‫نگاهداشتن است وطالب فرصت‌بدی کردن بودن‪.‬‬

 ‫چیزی لیکو و راست و بی عیب ‪ - ۸‬و خلاصه‬                   ‫سر ون = بفتح‌اول بروزن زبون » بمعنی‬

                     ‫‪:‬‬   ‫‪ :‬سرو‬    ‫رك‬    ‫‪۴‬‬        ‫ترديك لفط اوستابی «سروش» («‪.‬م‪۲ ).‬‬      ‫‪۱‬‬

               ‫سرولی است بر رسته‌چون کر گدن‪.‬‬                 ‫ز پیشانی هربك از مرد وزن‬
   ‫نظامی کنجوی‪ .‬ک«نجینه ‪۸۸۰‬‬
   ‫‪ = ۴‬سرین ( «م‪ » ) .‬اوستا ‪ ( 1002۳3 -‬تپیگاه ) » پهلی ‪)ras‬‏ ‪01۲25 ۰‬‬
   ‫(سرین)‪,‬هندی باستان ‪( 1۵۵۳9 -‬سرین‪ ,‬ران » تپیگاه) ل»توانی ‪ , 5101212۹‬لانینی ‪610016‬‬
   ‫بوتانی ‪ » )( »51061‬بلوچی ‪ ( 0۵۲25‬کمر ؛ تپیگاه ) «اسشق ‪ .۷۳۷0‬هوبشمان‌کوید ‪ :‬سیت‬
       ‫شن‬
        ‫دایومن‬
             ‫فظرسی «سرین» ‏ بلوچی ‪ 06725‬از ‪ # 6۳5‬و فارسی «سرون »از ‪ ۵ 00۲5‬بر‬
                                                                           ‫یت «حوبشمان ‪: ۷۳۲۷‬‬
               ‫گرچه برتابد آن میان وسرون‪.‬‬                      ‫کفش با سلاح بشکفتم‬
   ‫شهد بلخی‪«.‬لفت فرس ‪۹۷۳٩‬‏ ‪.‬‬
                                   ‫‏‪ « Cupressus sempervirens = ¢‬یتباث ‏‪. “AY‬‬
   ‫‪ - ۷‬مصحفهسد که»‬                ‫‪ -‬رك‪ :‬سرون ‪٩‬‏ سرین ‪.‬‬            ‫‪ _ ۵‬رك ‪ :‬سرو ‪ ۰‬سرون ‪.‬‬
                                                                              ‫س دکیس («‪.‬م‪۱ ).‬‬    ‫>‬

               ‫پیرزن کرک باشد‪ .‬او بره بود‪.‬‬                  ‫‪ - ۸‬مادرم کفت کو زلی سره بود‬
       ‫تظامی کنجوی‪ «.‬کنجینه‪»۸۸‬‬
   ‫(برهانقاطع ‪)۷۴۱‬‬
  ‫صری‬                                                                                 ‫ه‬
                                                                                      ‫ا‪۱‬‬‫‪۳۱‬‬
                                                                                         ‫‪-‬‬
```


## [2026-09-06T20:59:55.254Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"pdf page\" BQT_v2_pages.txt | head -3; echo ---; grep -c \"\" BQT_v2_pages.txt; echo \"=== nearest page markers before 35880 ===\"; grep -n \"^===\\|^\\[.*page\" BQT_v2_pages.txt | head -5",
 "description": "Inspect BQT_v2_pages structure"
}
```


### [2026-09-06T20:59:55.334Z] TOOL RESULT

```
---
41071
=== nearest page markers before 35880 ===
```


## [2026-09-06T20:59:59.323Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; head -5 BQT_v2_pages.txt | cat -A | head -5 | cut -c1-200; echo \"=== formfeeds ===\"; python3 -c \"\nd=open('BQT_v2_pages.txt',encoding='utf-8').read()\nprint('pages',d.count('\\f')+1)\nimport re\n# find offset of سرون footnote\ni=d.find('فظرسی')\nprint('idx',i)\nprint('page index', d[:i].count('\\f'))\n\"",
 "description": "Locate page index in BQT v2"
}
```


### [2026-09-06T21:00:01.214Z] TOOL RESULT

```
^L                                         M-bM-^@M-+M-bM-^@M-*7M-bM-^@M-,M-bM-^@M-,$
$
                          M-bM-^@M-+M-XM-1M-YM-^FM-bM-^@M-*M-[M-3M-bM-^@M-,M-bM-^@M-,$
    M-bM-^@M-+M-YM-^FM-XM-'M-XM-*M-bM-^@M-,$
      M-bM-^@M-+M-XM-' M-YM-^EM-bM-^@M-,$
=== formfeeds ===
pages 684
idx 2533814
page index 596
```


## [2026-09-06T21:00:04.783Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));import sys\nb=d['BQT']\nfor k,v in b.items():\n    print(k,':',str(v)[:900])\n\"",
 "description": "BQT offsets"
}
```


### [2026-09-06T21:00:06.317Z] TOOL RESULT

```
title : Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)
kind : archive_djvu+local_scan_ocr
url : https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.
lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only t
local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verific
page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017,
covers_etymology : True
notes : Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only
scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming
cites : page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material
```


## [2026-09-06T21:00:17.242Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nd=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in (590,591,592,593,594,595,596,597):\n    p=d[i]\n    print('--- leaf',i,'--- first 3 lines:')\n    print('\\n'.join([l for l in p.split(chr(10)) if l.strip()][:3]))\n\"",
 "description": "Check BQT v2 running heads"
}
```


### [2026-09-06T21:00:18.858Z] TOOL RESULT

```
--- leaf 590 --- first 3 lines:
    ‫اس‬
     ‫م‪۷‬‬                                                                                      ‫فرشکاهلی‬
                                                                                                    ‫س‬
--- leaf 591 --- first 3 lines:
                                                                                               ‫هه‬‫‪-‬‬
 ‫سر مو تثه دبا تای قر(شت‪)۱‬بروزن‬                       ‫وب‬
                                                       ‫رلکم‬
--- leaf 592 --- first 3 lines:
   ‫‪ ۳۱‬ات‬
 ‫و لبلابرا نیزکوبند‪,‬وآن‬    ‫حطی حم آمده است ‪-‬‬
                                                  ‫سر نامه = بروزن هتکامه ‪ ۰‬لجه‌بر سر‬
--- leaf 593 --- first 3 lines:
  ‫سروچ‬                                                                                                     ‫¬‬
‫ګوبند که راست رود وآن را ياين اعبار آزاد‬              ‫میباشد ‪ :‬مکی‌سروآزاد و دیگری سروسهی‌وسیم‬
 ‫کفته‌ادد که از ید کی و داراستی ویبوستن‌بشاخ‬                                  ‫سرو ناز وهر يك درجای خود‬
--- leaf 594 --- first 3 lines:
   ‫‪۰‬؟(‪-۳۱۱‬‬                               ‫‪o‬‏‬    ‫‪«.‬‬                                    ‫فاون‬
                                                    ‫وسر خای‬
                                                          ‫سرو خشت ب=فتح اول ک‬
--- leaf 595 --- first 3 lines:
                                                                                           ‫—‬     ‫لس‬
   ‫"روش‬
 ‫کال سال شممی بنام ابدان موسوم‌شده ‪» ۴‬وهر‬
--- leaf 596 --- first 3 lines:
  ‫‪۱۳‬‬                                                                                        ‫سروشه‬
                                                         ‫و مصالع آن رو" بدو مقرر است خودهم بتدبیر‬
 ‫وح‌اول بمعنی‌سرین است که شت‌گاه‌مردمان‬            ‫=‬     ‫ومصالح آن‌روز می‌پردازد‪ .‬بنابرآن بجهت‌شرف‬
--- leaf 597 --- first 3 lines:
  ‫صری‬                                                                                 ‫ه‬
                                                                                      ‫ا‪۱‬‬‫‪۳۱‬‬
                                                                                         ‫‪-‬‬
```


## [2026-09-06T21:00:34.264Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== TAD قلم ===\"; grep -n \"قلم\" TAD_pages.txt | head -20",
 "description": "grep TAD for qalam"
}
```


### [2026-09-06T21:00:34.311Z] TOOL RESULT

```
=== TAD قلم ===
121: ‫الاسمالذي لدأداتان عندهم و مل وأسن ‪ 115‬عقلمةق الحامض‬          ‫الل الاجر )غير‬
1696:‫‪#‬ناوغدء أي الموالة الماليةومنهممنعربهشلك أوشاك ونقلمنالافرنسيةالى‬
```


## [2026-09-06T21:00:34.698Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FVQ qalam ===\"; grep -n -i \"qalam\" FVQ_pages.txt | head -20",
 "description": "grep Jeffery for qalam"
}
```


### [2026-09-06T21:00:34.749Z] TOOL RESULT

```
=== FVQ qalam ===
8752:p (Qalam).
```


## [2026-09-06T21:00:38.387Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8740,8790p' FVQ_pages.txt",
 "description": "Read Jeffery qalam entry"
}
```


### [2026-09-06T21:00:38.450Z] TOOL RESULT

```
of the poets preserved exactly the vo welling of the Aram. 2
^>
Ji5 (Qufl).
xlvii, 26.
A lock.
Only in the plu. JU51, where al-Jawaliqi, Mu'arrab, 125, says it
is a borrowing from Persian. 3
^ V **
The verb IA5 is denominative 4 and the word cannot be
derived from an Arabic root. It is probably the Aram.
a fetter, or Syr. ]l2>ao, which translates the Gk. KAeWpov, and
would have been an early borrowing. 5
p (Qalam).
iii, 39 ; xxxi, 26 ; Ixviii, 1 ; xcvi, 4.
Pen, or the reed from which pens were made.
It means a pen in all the passages save iii, 39, where it refers to
the reeds which were cast to decide who should have care of the
maiden Maryam, and where the *j& I, of course, stands for the pa/38 ot,
of the Protev. Jacobi, ix. 8
Baid. gives this as the reading of Ya'qub.
Cf. Fraenkel, Fremdw, 150 ; Zimmcrn, Akkad. Frerwlw, 60.
So as-Suyutl, Itq, 323. al-Jawaliql is probably referring to the Pera. jl^\
Fraenkel, Fremdw, 16 ; Zimmern, Akkad. Fremdw, 35, gives it from the Aramaic.
Cf. Krauss, Oriechische Lehnworter, ii, 517, and ZDMG, xxvii, 623.
In Tischendorf, Evangdia Apocrypha, 1876, p. 18.FOREIGN VOCABULARY OF THE QUR*AN 243
X"X
The native authorities take the word from *\$ to cut (cf. LA,
xv t 392), but this is only folk-etymology, for the word is the Gk.
a reed and then a pen, 1 though coming through some Semitic
form. KaXa/JLO? was borrowed into Aram., where we find Olu?1p,
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
```


## [2026-09-06T21:00:39.271Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 900 python3 tools/ref_page.py TAD:57 --image 2>&1 | tail -40",
 "description": "Fetch TAD page 57"
}
```


### [2026-09-06T21:00:40.909Z] TOOL RESULT

```
no scan of TAD covers printed page 57 (see 'scans' in refs_online.json)
```


## [2026-09-06T21:00:49.062Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['TAD']\nfor k,v in d.items(): print(k,':',str(v)[:700])\n\"",
 "description": "TAD offsets"
}
```


## [2026-09-06T21:00:50.390Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN calamus/caramel ===\"; grep -n -i \"caramel\" KLN_1966.txt KLN_1971.txt | head -10; echo \"=== SKT ===\"; grep -n -i \"caramel\\|calamus\" SKT.txt | head -5",
 "description": "grep Klein/Skeat caramel"
}
```


### [2026-09-06T21:00:50.676Z] TOOL RESULT

```
title : Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR
kind : archive_djvu
url : https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640
lookup_hint : Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt']
page_offset : 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image
covers_etymology : True
notes : Arabic OCR fair. Nourai's exact edition unknown; the Beirut reprint reproduces the 1932 pagination.
```


### [2026-09-06T21:00:50.733Z] TOOL RESULT

```
=== KLN calamus/caramel ===
KLN_1971.txt:36935:element in calamint, caramel, 
KLN_1971.txt:38464:first element in canephorus, caramel. 
KLN_1971.txt:39393:caramel, n., burnt sugar. — F., fr. OSp. caramel 
KLN_1971.txt:39394:(now caramelo ), a blend of ML. cannamella, 
KLN_1971.txt:148158:lite, melilot, Melissa, molasses, mulse, caramel, 
KLN_1966.txt:6126:calamary,  n.,  squid.  —  L.  calamdrius,  ‘pertaining to  a  pen’,  fr.  calamus,  ‘reed,  pen’,  fr.  Gk.  y.diXa- p.0?,  prob.  an  assimilated  form  of  orig.  *x9X:x- jioc,  and,  accordingly,  cognate  with  L.  culmus, ‘stock,  stem’.  See  culm,  ‘stem  of  grasses’,  and cp.  words  there  referred  to.  Cp.  also  the  first element  in  calamint,  caramel, calamine,  n.,  a  kind  of  zinc  ore.  —  F.,  fr.  ML. calamina,  fr.  L.  cadmia,  fr.  Gk.  xxSfrsia,  ‘cala¬ mine’,  fr.  KiSixo;,  ‘Cadmus’,  the  founder  of Thebes ;  so  called  because  this  mineral  was  found first  in  the  vicinity  of  Thebes.  See  Cadmus, cadmium.
KLN_1966.txt:6344:nikin,  canon,  ‘rule’,  canonical,  canyon,  and  the first  element  in  canephorus,  caramel.
KLN_1966.txt:6492:caramel,  n.,  burnt  sugar.  —  F.,  fr.  OSp.  caramel (now  caramelo),  a  blend  of  ML.  cannamella, ‘sugar  cane’,  (see  cane  and  melliferous)  and  Sp. caramillo,  ‘reed’,  fr.  L.  calamellus,  dimin.  of calamus,  ‘reed’  (see  calamary).
KLN_1966.txt:23348:lit.  ‘honey  fly’,  (3X<.tto>  (for  *p.Xmc»),  ‘I  cut  out the  comb  of  bees’.  Alb.  mjai,  mjai te,  honey', OIr.  mil,  ‘honey’,  Ir.  mills,  ‘sweet ,  WBret.  mel, ‘honey’,  Goth,  milip,  ‘honey’,  OE.  mild  raw, ‘honeydew,  nectar’,  milisc,  ‘honeyed,  sweet’, OHG.  milsken,  ‘to  sweeten’.  See  mildew  and  cp. melliferous,  mellifluent.  Cp.  also  meliceris,  meli- Ute,  melilot,  Melissa,  molasses,  mulse,  caramel, hydromel,  oenomel.
=== SKT ===
```


## [2026-09-06T21:01:00.111Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON kâramel ===\"; grep -n \"کارامل\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10; echo \"=== MON qalam ===\"; grep -n \"قلم \\[\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10",
 "description": "grep Moin for قلم and کارامل"
}
```


### [2026-09-06T21:01:00.212Z] TOOL RESULT

```
=== MON kâramel ===
MON_part2.txt:15074:در حدود صد درجه حرارت به کارامل یا قند 
MON_part2.txt:17490:کارامل: 122061 (شیم.) ماده‌ای که در 
MON_part2.txt:17492:بدست آرند. کارامل قهوه و شکلات: 
MON_part2.txt:17510:قالب آهن سفید را چرب کرده و کارامل را 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:15074:در حدود صد درجه حرارت به کارامل یا قند 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:17490:کارامل: 122061 (شیم.) ماده‌ای که در 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:17492:بدست آرند. کارامل قهوه و شکلات: 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:17510:قالب آهن سفید را چرب کرده و کارامل را 
=== MON qalam ===
```


## [2026-09-06T21:01:02.242Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC ===\"; grep -n \"klounis\\|kolamos\\|kolemos\\|kolamā\" IEC.txt | head -10; echo \"=== SYN reed ===\"; grep -n \"kalamos\\|clunis\" SYN.txt | head -10; echo \"=== LKT caramel ===\"; grep -n -i \"caramel\" LKT.txt DEV.txt PHN.txt | head -10",
 "description": "grep Mann/Buck/Lokotsch"
}
```


### [2026-09-06T21:01:02.308Z] TOOL RESULT

```
=== IEC ===
=== SYN reed ===
=== LKT caramel ===
```


## [2026-09-06T21:01:05.435Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '17485,17515p' MON_part2.txt; echo \"=== MON قلم ===\"; grep -n \"^قلم\\|قلم(\" MON_part2.txt MON_part1.txt | head -20",
 "description": "Read Moin karamel + find qalam"
}
```


### [2026-09-06T21:01:05.507Z] TOOL RESULT

```
مصیبتی بدو رخ نموده باشد. 
کارافراری): (۲20۵ [- کارفرا - 
کارافزاینده] (ص‌فا.) آنکه کار و زحمت 
دیگری را افزون کند؛ کسی که مشغولیت 
دیگری را بیشتر سازد. مزاحم. پ رگو. 
کارامل: 122061 (شیم.) ماده‌ای که در 
حرارت‌های زیاد از ساکارز یا قند معمولی 
بدست آرند. کارامل قهوه و شکلات: 
شیرینیی است و طرز تهیه آن چنین است: 
۰ ۰ گرم قند را در آب زده همین که 
مرطوب شد در ظرف ریخته آب نصف 
لیموترش را هم بدان علاوه کنند و هموزن 
قند خامةٌ غلیظ و تازه روی آتش می‌پزند و 
هم می‌زنند. پس از ۵ دقیقه ۰ گرم قهوه با 


۰ گرم شکلات بدان مخلوط کنند. 


فرهنکگ فارسی معین 


کار آمد 
وقمی که خود را گرفت -یعنی گر قدری از 
آن در آب سرد بریزند؛ ببندد - سینی یا 
قالب آهن سفید را چرب کرده و کارامل را 
در آن ریزند و بصورت مربعات می‌برند. 
کاربر: ۲۲ [- کار بر نده] (ص‌فا.) آنکه 
زود امور را حل و فصل کند. کسی که به 
سرعت و خوبی کاری را انجام دهد. برهم 
زننده کار. 
=== MON قلم ===
MON_part1.txt:242:قلم هنری کربن) شماره ٩‏ از انتشارات دانشگاه تهران ۱۳۲ 
MON_part1.txt:78256:قلمدان و جلد کتاب و رحل قر آن و اوراق 
MON_part1.txt:78774:قلمتراش؛ ج. سکاکین. 
MON_part1.txt:85637:قلماتس» کلماتیس» ظیان یاسمن البر» یاسمن 
MON_part1.txt:93259:قلم. طوطی احب سلامتگو: طوطیی که او 
MON_part2.txt:586:قلم جدید است و آن خطی است با قلمی 
MON_part2.txt:10660:قلمکار سازد؛ قالب مخصوص آن نقش را 
MON_part2.txt:13442:قلمدان گذارند و سر قلم‌های معینی را با آن 
MON_part2.txt:14131:قلمان 
MON_part2.txt:14284:قلم: 7۱۸7۱ [معر. بو.] (.) آلتی نثین با چویین 
MON_part2.txt:14290:قلم فرنگی: دو ام اس : یکی آنکه با دسته 
MON_part2.txt:14297:قلم متعارف از درون خالی کرده چیزی که 
MON_part2.txt:14318:قلم‌مو معمولاً برای قلم‌گیری یکك نواخت و 
MON_part2.txt:14368:قلم تاکک: شاخ مو. قلم گل: شاخ گل. قلم 
MON_part2.txt:14397:قلم اول که عقل اول باشد ملک مقرب 
MON_part2.txt:14411:قلماش: ۵۳25« [تر.] (ص.) هرزه. بیهوده؛ 
MON_part2.txt:14432:قلماش 
MON_part2.txt:14444:قلمتراشنده] (ص ف. (.) چاقویی کو چکک که 
MON_part2.txt:14446:قلمداد کر دن: 7-۵2027020 [سمعر. ف.] 
MON_part2.txt:14448:قلمدان: 7-0 [معر. ف.] (امر.) آلشی
```


## [2026-09-06T21:01:08.150Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC kalamos ===\"; grep -n \"kalamos\\|kolamos\\|klōunis\\|klounis\" IEC.txt | head; echo \"=== IEC klou ===\"; grep -n \"klou\" IEC.txt | head; echo \"=== SYN buttock/reed ===\"; grep -n -i \"shlaunis\\|szlaunis\\|clunis\" SYN.txt LEW_1910.txt LAT.txt | head",
 "description": "grep Mann and Latin dicts"
}
```


### [2026-09-06T21:01:08.233Z] TOOL RESULT

```
=== IEC kalamos ===
=== IEC klou ===
7328:kleudos ‘defective’; kleuda ‘defect’. Cf. kleudo (2) (3) & WP I, 492 Lat. clūdus ‘lame’; W cf. achludd, pl. ion, m. ('stoppage', fr. apo-?); Sw. lytt ‘defective’; lyte, wn. ‘defect’; Li. kliáuda ‘defect’ (NB: The Lat. form claudus, as also claudo ‘shut appears to represent a variant of type *kloud-)
7335:kloueros, see kleuor-
7336:klouos, is (variant of type klau-, q.v.) “jam, stick, fasten, fix’. Cf. WP I, 492 Gk. cf. klojós “iron collar, dogcollar'; kloiós, id.; Br. klaw, kíaó & klav, pl. klawiu, klavier (sic) ‘bracket, spike, plowshare, knot’; W clau, adj. (?) “firm, steady’; Cz. cf. klov-aty ‘gummy’
7387:(kloud-, see kleud-)
7388:(klou-, see klàu- and cf. Gk. klóós *dogcol- lar’; Olr. cló ‘nail, spike’. WP I, 492. Vowel ambig.)
7393:klüd- "cover" (variant: kloud- 'shut') Lat. cf. claudo, ére, -clüdo, ére *shut'; Ir. clúd- aim “cover, thatch, clothe'; clúd, m. 'shelter; clothing; patch’; MHG lüs, lüze, f. ‘ambush, hide-out'; Li. cf. kliudyti ‘stop, block
8940:Kloios (2) Gk. kloiós, m. (*dog-collar'. Ambig. cf. klou- os); Li. 5lájos, -ai, f. & m. pl. ‘harness, tackle’. Cf. also klai- in Supt:K
14317:qusel- (2) ‘bridle, harness, traces’. Cf. quseið (2) Skt. cf. khalinam, n. “bridle-bit” (LW via Iran- ian? in Aeolic Gk. khálinnos ‘bridle’ beside khalinos, id.); Hitt. cf. (queried) sxiyal (for *sxel-?) (perhaps ‘bond, girthbelt); Gk. psé- lion, pséllion & psálion ‘bridle-chain’; R šlejà *breechband'; OCz. šle ‘traces, harness’; Pol. cf. szelki, pl. ‘braces’; Li. staat, mpl. (&breech- ing', but cf. Kloios (2), klai- (Supt) and klouos. Perh. a hybrid); Latv. slejas, fpl. ‘harness’. Variants in Ir. sealán, m. ‘halter, noose’; ON seli, sili, m. ‘harness’; Sw. sele, pl. selar, wd: LG selen, m. id.; G. Sill, Sille, Siele, f. “light harness’; pl. ‘braces’. (Loanword phonology combined with linguistic drift, from Indo- Iranian?, seems probable)
=== SYN buttock/reed ===
LAT.txt:12670:clunis, -is et clunes, -ium (usite surtout an pl. comme natis;
LAT.txt:82277:» 331, sons clunis, l.i et 7, 1. natis, nates.
```


## [2026-09-06T21:01:19.033Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON قلم entry ===\"; sed -n '14284,14300p' MON_part2.txt; echo; echo \"=== LAT clunis ===\"; sed -n '12665,12685p' LAT.txt",
 "description": "Read Moin qalam and Ernout clunis"
}
```


### [2026-09-06T21:01:19.097Z] TOOL RESULT

```
=== MON قلم entry ===
قلم: 7۱۸7۱ [معر. بو.] (.) آلتی نثین با چویین 
و با فلزی که به وسیلة آن با مرکت با جوهر 
روی کاغذ نو بسند»ه خامه» کلک؛ ج. اقللام. 
ترکیات اسمی: قلم سرب: قلم فرنگی. قلم 
فر انسه: قلمی که دارای دسته‌ای جوبی است 
واسر قم فرای بدان نصت ندز توریستن 
قلم فرنگی: دو ام اس : یکی آنکه با دسته 
ستاو آن را از سنگ یشم و بلور یا دندان 
ماهی و عاج يا چوب صندل سازند و آن 
احتیاج به مداد ندارد و حروفی که با آن 
نویسند در رنگ مشابه به سواد سرمه باشد و 
آن را اکثر بادشاهان هند و امرای بزرگک 
بکار می‌بردند. دوم آنکه چوبی را به قدر 
قلم متعارف از درون خالی کرده چیزی که 
بدان نوشته شود در آن پر کنند و بدان چیز 
نویسند؛ مداد. قلم فولاد: قلمی که نوک آن 
از فولاد است. قلم گندمی: (نق.) قلم مویی 

=== LAT clunis ===
figurait d'ordinaire au deuxifeme terne de composes. Il n'y a pas de
raison de croire que cluor rdponde A skr .grdvah, gr.xXe(p)oc "gloire";- 33i ~ coe(c)olobls
ce peut Stre une format ion proprement latine. - Les formes slaves et
baltiques n 1 enseignent rien pour le latin.,
Cluniae: folliculi hordei, P.F.48,15. V. glUma.
clunis, -is et clunes, -ium (usite surtout an pl. comme natis;
cf. toutefois Hor. S.3,8,91) a. et f., c£ Charisius, GLK I 101,4 clunes
feminino genere dixit Melissus... sed 7 errius flaccus masculino genere
dici probat, quoniam -nis syllaba terminata anima carentia nominatiuo
singulari masculina sunt, ut panis cinis crinis et similia: fesses,
croupe. Anci en, .populaire ou technique. Le plus sonyent synonyme de
nates, qooique Martial 3 , 53,3 emploie les denx mots en les diff^ren-
ciant; se dit des animanx comme de 1 'homme. Le sg. est sans donte
s econdaire.
D^riv^s: clunaclum (et clunabulum): cultrum sanguinarium dictum, uel
quia ad clunes dependet, uel quia clunes hostiarum diuidit, P.F.43,3;
cluhdlis (rare et tardif); cluniculus (-Ia?).
Cf., avec le meae sens, iri. cluain, gall. clun (f 4 m.), skr. gronih, av.
sraonis ( fem. ), lit. s launis (f6a.) et v. prass. slaunis, v.isl. hlaun
"fesse"(nentre). Le rapport avec gr. xXovtC "os sacrum", xXoviov* lOftCN,
payiC, ocxpuC n'est pas d^terminable.
```


## [2026-09-06T21:01:21.513Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC kolam/kalam ===\"; grep -n \"^kolam\\|^kalam\\|^kolem\\|kolamos\" IEC.txt | head; echo \"=== IEC klounis ===\"; grep -n \"klounis\\|klōunis\\|kloun\" IEC.txt | head; echo \"=== LEW calamus ===\"; grep -n \"calamus\" LEW_1910.txt | head -3; echo \"=== LEW clunis ===\"; grep -n \"clunis\" LEW_1910.txt | head -3",
 "description": "grep Mann and Walde Latin"
}
```


### [2026-09-06T21:01:21.592Z] TOOL RESULT

```
=== IEC kolam/kalam ===
=== IEC klounis ===
=== LEW calamus ===
=== LEW clunis ===
```


## [2026-09-06T21:01:29.635Z] TOOL CALL #39: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-06T21:01:29.643Z] TOOL RESULT

```


```


## [2026-09-06T21:01:32.926Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1lownis",
 "prompt": "Give the reconstruction, meaning, and the list of descendants (Avestan, Sanskrit, Latin, Lithuanian, Old Prussian, Old Norse, Celtic) verbatim."
}
```


## [2026-09-06T21:01:34.288Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D9%84%D9%85",
 "prompt": "Give the Arabic etymology of قلم (qalam) 'pen' verbatim, and also the Persian section etymology if present."
}
```


### [2026-09-06T21:01:35.012Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T21:01:40.311Z] TOOL RESULT

```
# Etymology of قلم (qalam) 'pen'

## Arabic Etymology

The Arabic noun قَلَم (qalam) is "derived from Ancient Greek κάλαμος (kálamos)" according to the entry. The detailed etymology explains it came through Ge'ez, with scholars debating whether the route was Greek → Ge'ez → Arabic or possibly Arabic → Ge'ez, though the Greek origin is established.

## Persian Etymology

The Persian section states that قلم (qalam) was "borrowed from Arabic قَلَم (qalam), from Ancient Greek κάλαμος (kálamos, 'reed')."

Both etymologies trace back to the Ancient Greek word for reed, demonstrating how this writing implement term traveled across languages and cultures through trade and linguistic contact.
```


## [2026-09-06T21:01:45.188Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CE%BB%CE%B1%CE%BC%CE%BF%CF%82",
 "prompt": "Give the Ancient Greek etymology of κάλαμος verbatim (PIE root, cognates Latin culmus, OE healm, OCS slama), and its descendants/borrowings (Latin calamus, Sanskrit, Arabic, Aramaic)."
}
```


## [2026-09-06T21:01:46.499Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/caramel",
 "prompt": "Give the full etymology of caramel verbatim, including the French, Spanish, Portuguese, Late Latin cannamella / calamellus discussion."
}
```


### [2026-09-06T21:01:52.761Z] TOOL RESULT

```
# Etymology and Descendants of κάλαμος

## Ancient Greek Etymology

The word derives from Proto-Indo-European *ḱélh₂m̥ ("reed, straw") through its "zero-grade stem (such as genitive *ḱl̥h₂mós, with a shift in accent to *ḱĺ̥h₂mos)."

**Cognates include:**
- Latin: *culmus*
- Old English: *healm* (becoming English *haulm*)
- Old Norse: *halmr*
- Russian: *solóma*

## Descendants and Borrowings

The term spread across multiple languages:

- **Latin:** *calamus* (which generated numerous Romance language descendants)
- **Arabic:** *qalam* (قَلَم) with further descendants
- **Hebrew:** *kulmus* (קולמוס) and *kalmarin* (קלמרין)
- **Sanskrit:** *kalama* (कलम)
- **Old Armenian:** *kalamon* (կալամոն)

Modern Greek preserves both the learned borrowing *κάλαμος* (kálamos) and the popular form *καλάμι* (kalámi), the latter continuing Byzantine Greek *καλάμιν*.
```


### [2026-09-06T21:01:53.200Z] TOOL RESULT

```
# Etymology of Caramel

Based on the Online Etymology Dictionary, here's the word's origin:

The term "caramel" entered English in 1725, deriving from French *caramel* meaning "burnt sugar" (17th century). The French word came from Old Spanish *caramel* (modern *caramelo*), whose precise origin remains uncertain.

The most traditional theory traces it through Medieval Latin *cannamellis*, proposed to combine Latin *canna* ("reed" or "cane") with *mellis* (genitive of *mel*, meaning "honey"). However, scholars propose alternative origins: some suggest an Arabic source for the Medieval Latin term, while others connect it to Latin *calamus* ("reed" or "cane").

By 1884, the word had extended to describe "a dark-colored creamy candy," and by 1909 it functioned as a color designation. The related verb *caramelize* emerged in 1837, with the adjectival form *carameled* appearing earlier in 1727.
```


## [2026-09-06T21:01:59.481Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%8B%E0%A4%A3%E0%A4%BF",
 "prompt": "Give the Sanskrit etymology of श्रोणि (śroṇi) 'hip, buttock' verbatim, including PIE reconstruction and cognates (Avestan, Latin clunis, Lithuanian šlaunis, Old Prussian slaunis, Old Norse hlaun, Welsh clun)."
}
```


## [2026-09-06T21:02:00.061Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/clunis",
 "prompt": "Give the Latin etymology of clunis verbatim: PIE reconstruction and cognates."
}
```


### [2026-09-06T21:02:05.340Z] TOOL RESULT

```
# Latin Etymology of *clunis*

**PIE Reconstruction:**
"*ḱlównis*" from Proto-Indo-European

**Derivation Path:**
From Proto-Italic "*klounis*," which descended from the PIE root noted above.

**Cognates:**
The entry identifies two related words: Lithuanian "*šlaunis*" and Sanskrit "*śróṇi*" (श्रोणि).
```


### [2026-09-06T21:02:07.632Z] TOOL RESULT

```
# Sanskrit Etymology of श्रोणि

Based on the Wiktionary content provided, here's the etymological chain:

The word derives from **Proto-Indo-Aryan *śráwniṣ**, which came from **Proto-Indo-Iranian *ćráwniš**, ultimately tracing back to **Proto-Indo-European *ḱlównis**.

## Documented Cognates

The page explicitly mentions two cognates:

1. **Avestan**: 𐬯𐬭𐬀𐬊𐬥𐬌 (sraoni)
2. **Latin**: *clūnis*

The etymology section states: "Cognate with Avestan 𐬯𐬭𐬀𐬊𐬥𐬌 (sraoni), Latin clūnis."

## Note on Additional Cognates

While you've referenced Lithuanian *šlaunis*, Old Prussian *slaunis*, Old Norse *hlaun*, and Welsh *clun*, **these specific cognates are not mentioned in the Wiktionary article provided**. The document only explicitly lists the Avestan and Latin forms, along with the full PIE reconstruction chain.
```


## [2026-09-06T21:02:18.114Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nd=open('TAD_pages.txt',encoding='utf-8').read().split('\\f')\nprint('leaves',len(d))\nfor i in range(58,66):\n    t=d[i]\n    print('=== leaf',i,'===')\n    print(t[:700])\n\" ",
 "description": "Print TAD leaves near p.57"
}
```


### [2026-09-06T21:02:19.889Z] TOOL RESULT

```
leaves 87
=== leaf 58 ===
                                      ‫سد‬    ‫اهم‬



                                           ‫‪2‬ك » وهو الحجل‬
                                                        ‫قب ‪ .-‬فارسي ك‬
     ‫معنأه حماس و ‪ 110 862‬ألاتزلاه‬   ‫قرس ل أخوة النحاسى ‏ لانيني امن‬

                                                                 ‫رسسي‬
                                                                    ‫بحا‬
                                                                      ‫أقين‬
                        ‫بعر يب ‪50]0/5‬ألء وهو اسممصر ف اليونانية‬
                                                              ‫قبط ت‬

 ‫ايطالي مطةالمةن معناه فى الاصل رئيس مرادقه ناك السفينة‬            ‫ق
=== leaf 59 ===
                                        ‫ده‬     ‫ااه‬



‫اراق « كرميل »عد الإل الال وهو تدناظري 'تحوت دينكم أي |‬
‫دودة ول أي حراء وهزاكوقة عراء كرن ف ‪:‬ضوف اقاء مو نف ابيقة ‪1‬‬
‫اوتستعها وهو نوسود ف نينا ‪١١‬‏‬
                            ‫ويقع على ورق شجرة بلوط القرمز وعلى أنه ) ب‬
  ‫والهند والككيك وسائرالبلدان الحارةفيجمعفىحينهويصبغ به ولونه أحر قانر‬
                                   ‫فنقل قرمر منالعر ببة الى لغات اوريا بلفظ و‪6‬ممه؟‪1‬‬

                                            ‫قرقة © ‪ --‬تركي( غورق عريهارنقاء‬
    ‫قرميبدد ‪ -‬بوناني ‪5112:2, 8‬نع‪ 21‬معناه تراب محروق أي طهيشنوي” وهو‬
                                                               ‫الخزف والفخار والاجر‬
   ‫و
=== leaf 60 ===
                                  ‫سالاع سد‬


 ‫اللانني شمعئاه حصن وقلعة‬        ‫‏‪ ٠‬عرني محض وهو الصرح أما مق‬

              ‫ومنه البلاط أي قصر الملك‬        ‫‪"3 00‬قِالأديية ا‬
                                                             ‫والقهعر‬

                     ‫قصدر ‪ -‬ونالى وم‪2‬ه‪1‬أ‪:55‬؟‪ 1‬وهو ممدن لين يطلى به‬
                                                                ‫ل‬
                       ‫ونه ‪ -‬فايليونانية ‪ 50421101‬معناه زنبيل من خلاف‬

 ‫غلاف اللكحلة ‏ فارسي مركب ون كف أي كلل ؤذا نوعو‬               ‫تدان ‪-‬‬

                                             ‫صيغة ظرف المكان تلصق بالاسياء‬
‫قفص ‪ -‬عرنيمحض وقفسالفارسي التركي مأخوذ منقفصالعربي و دومه)!‬
 
=== leaf 61 ===
                                                       ‫لوش ‪ -‬اطلب كالوش‬
                          ‫كظورنت‬
                               ‫قس وقومس ‪ -‬أمير ورجل شريف ‪ -‬ان‬
 ‫قاش ‪ -‬في الفارسية ك«ش » معناه نسيج من قطن شن ثمنقل قاش الى‬
                                                            ‫الفارسية بلفظة فاش‬
      ‫ترك « قامش ‪ 6‬معناه قضيب وقصب و ( فجي » معناه سوط‬                     ‫‪2‬‬

 ‫وفي اللغة‬             ‫في الايطالية *‪01‬مهه وفي اللاتينية الركيكة‬       ‫فض‬
‫كا فعي منقولة من اللاتمنية الى العربية والى السسربانية ايضا‬        ‫اللعزنطية ‪805‬‬

                                                                   ‫‪6 05 2‬‬
                                          
=== leaf 62 ===
                                      ‫د‬    ‫سابةاجم‬




   ‫عمعناه شمعة يستضاء مهامرادفه مصصباح وسراج‬            ‫قنديل ‪ -‬لانيى ‪84‬‬
                                                                              ‫‪1‬‬     ‫‪01‬‬

‫قعل ‪ 5‬ب لاتيبى امه معثاه مشتكاد وراد به فى زماننا تمثل الدولة‬

              ‫«الالنةرعاتون معناه مئوي من «اتاأهعء مائة‬            ‫قنطار لاتينى‬

 ‫متسوب الى ‪80:00212‬و]آ‬             ‫قنطارون وقنطورون ‪ -‬لاتق ‪82‬‬

‫قنطورس اليوناني وهو هولة اي هسك نصفه اسان ونصقه فرص ومعنى قنطورس‬

                             ‫افلييونانية تاخز الفرس وهو ابيحشيشة مر الطم‬
                  ‫قال ‪ 3-3‬لاسى ماله معذأه خجرى الماء مر أدقه وناة وبرعة‬

‫‪0‬قت ‪ -‬وون‪.‬ان
=== leaf 63 ===
                                    ‫ساي سم‬


    ‫وناتي ‪80‬م ومنه الانكيزي مو وهو الحندب البحري‬                     ‫قريدس‬

‫اليوناني ومعناه قرن صغير ويطلق على قرن‬             ‫دوعا‬     ‫ل‬          ‫قراط‬

‫الخرنوب وعلى حبة الخرنوب أيضا وكان الاقدمون يزئون الذهب بالقيراط أي‬
                                        ‫حبة الخرتوب وكل ‪5‬ح‪4‬بة نساوي أأوقية‬
      ‫معنأه مشمّم وبراد به مرحم ضمّد به‬               ‫بوناني ‪06‬‬      ‫قيروطي‬
                             ‫قينةسأي بنتنيةف الأضل العتراق ماعة ارائنة‬
                                     ‫دك »‬
                ‫كابلا ‪ -‬ايطالي ‪2‬ااعومهه معناء معبّد أيكنيسة صغيرة‬
‫كاتدرائية ‪ -‬منسوب الى ‪20060‬ادك اليونائي الذي مدا واس و‪ 1
=== leaf 64 ===
                               ‫‪ 2-0‬ل‬


                ‫فونانى ‪5169‬مم‪ !2‬عربيهالأصّيف م ى الزغر‬          ‫‪53-5‬‬

‫“سول الفيؤنانكه عار ولاموله طناسنة قارف ادراونة تن‬
                              ‫وهو قعيحشى من ملح الزئيق فيشعل البارودة‬
    ‫“كتهدا وكاغية حر ‪:‬وكتخا واه يهسقندالواليوكاتمسر"ه‬

‫«وتينا » وف اليونانية‬
                    ‫‪ - 8‬عبرانى ‪ » 65‬وى الارامية كم‬
‫للك ‪ 0‬وهو القميص من كتان وغيره الظاهر الها مشتقة من الكتان‬
                            ‫مادمها وهو نبات معروف تنسج من لهاءه الثياب‬
              ‫نالسران ‪ 3‬كر وق التونانة ددم‬             ‫‪71‬و‬
                                  ‫كرباج ب تر « ‪.‬قرباج » وهو السوط‬
‫فى ع اللكيمياوعنهكرنزنات‬     ‫يوطناسل
=== leaf 65 ===
              ‫معنا ودس ويارك ومازاً ‪1‬‬                ‫‪ 1‬ع ‪ -‬لانيي ‪1‬‬

                      ‫«رشف » وهو القطن‬
                                     ‫اتيف وكرفس‪ -‬فارسي ك‬
                              ‫فلارامية «كرفسا »( بات)‬
                                                    ‫كرفس ا‬
                               ‫نات )‬          ‫الآراية ناه‬            ‫"كر حاف‬
      ‫ايطالى فوعامج رونو معناة اونشوك نومامرادقه الجر الصحي‬                ‫ال‬

‫كرنيتة ‪7‬س ايطالى هااءد‪.‬ده معناه قرن صغير وهو بوق تحيف ينفخ فيْه‬
                                                                            ‫كازمارة‬

‫واروسميهة وكروبين وشارويين ‪ -‬فاىلعيرانية « كووب ‪3‬‬
```


## [2026-09-06T21:02:34.777Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"قلم\\|كالام\\|كلام\" TAD.txt | head -10; echo \"=== leaf61 full ===\"; python3 -c \"\nd=open('TAD_pages.txt',encoding='utf-8').read().split('\\f')\nprint(d[61])\n\"",
 "description": "Search TAD for qalam entry"
}
```


### [2026-09-06T21:02:37.092Z] TOOL RESULT

```
67:من أوضاع العرب فلا يخفى أن هذه الطريقة عتيقة لابزالالكلام معبانكرة وممهما 
96:الل الاجر ) غير الاسم الذي لدأداتان عندهم و مل وأسن 511 عقلمةق الحامض 
2543:استعولبا ابن بط أوطه في رحاته التبورة فى الكلام علي يلاد الك قال م امول المحية غر به 
3185:شناء الغييل فها ى كلام العرب من الدخيلتأليفنشهاب الدين دلجي 
3186:ليس فى كلام العرب لأني عبد الله الحسين المعروف يابن خالويه التحو 
=== leaf61 full ===
                                                       ‫لوش ‪ -‬اطلب كالوش‬
                          ‫كظورنت‬
                               ‫قس وقومس ‪ -‬أمير ورجل شريف ‪ -‬ان‬
 ‫قاش ‪ -‬في الفارسية ك«ش » معناه نسيج من قطن شن ثمنقل قاش الى‬
                                                            ‫الفارسية بلفظة فاش‬
      ‫ترك « قامش ‪ 6‬معناه قضيب وقصب و ( فجي » معناه سوط‬                     ‫‪2‬‬

 ‫وفي اللغة‬             ‫في الايطالية *‪01‬مهه وفي اللاتينية الركيكة‬       ‫فض‬
‫كا فعي منقولة من اللاتمنية الى العربية والى السسربانية ايضا‬        ‫اللعزنطية ‪805‬‬

                                                                   ‫‪6 05 2‬‬
                                                                           ‫َ ‪2‬‬
                             ‫قمهم‪ --‬فارسي «‪ ) 5‬وعرببه يعدروم‬
                    ‫معناه ‪1‬ون وموقد‬       ‫وق الخجام ب بوناني ‪5‬‬             ‫ثين‬

‫وفي اللاتينية دتاتاء معناه أعلىكل شيء مرادفه‬       ‫شه وهامة ‪ -‬بوناني ‪51‬‬
                                                                      ‫وك‬         ‫‪010‬‬

                                                            ‫قله وقلة وشعدفة‬
                                                                           ‫‪9‬‬

‫شريمتفازنى و كد ب و©أصل هذا النبات من بلاد الهند وفارس فتقل‬
             ‫الى اليونانية ونطهدسهة ومنها إلى الابطالية ‪#‬مقصد وسائر لغات اوربا‬
       ‫قكرذةف من المدفم مرادفهاقذيفة‬
                                   ‫قنبلةبتري « قومباره » وتهي‬
                                 ‫«ند» قرفن الب‬
                                             ‫ند ‪ -‬فارسي ك‬
 ‫فارسي «كندسك ‪ 6‬معنأه خصية الكاب وغو‬               ‫ا‬     ‫وفلدز دن‬          ‫‪5‬‬

                                          ‫كلب الماء وخصيته يقال لها جندييدستر‬
‫قندسة وكتدجة ‪ -‬فارسي «وكنده » وهوخشبة يستعملها البثساؤنفي‬
                                                                   ‫بنيان القناطر‬
```


## [2026-09-06T21:02:45.721Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB surin/srauni ===\"; grep -n \"surīn\\|surun\\|surūn\\|sraunī\\|srainī\\|Hinterbacken\" HUB.txt | head -10; echo \"=== ARY سرین ===\"; grep -n \"سرین\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== ARY قلم ===\"; grep -n \"قلم:\" incoming/ARY/ARY_pages.txt | head -5",
 "description": "grep Hübschmann and Aryanpur"
}
```


### [2026-09-06T21:02:45.800Z] TOOL RESULT

```
=== HUB surin/srauni ===
4976:Gl. 64 — zd. draonah-; surun (surln) 'Hinterbacken' = zd.
6098:singen', zd. srdvayeiti ; siiru {saru) 'Horn* = zd. srvd- ; surun
6099:[surtfi] 'Hinterbacken*, bal. saren, zd.sraoni-; supurdan (pr.
7570:srU'\ sardi *Palast* = ap. "^srada-; surun 'Hinterbacken* =
=== ARY سرین ===
10604:سرین» سرون (به چم "کبل" "نشستگاه» *تحت") / ۳۵۹
12034:چم اين واژه در زبان لاقین؛ کپل» سرین؛ باسن.
=== ARY قلم ===
2440:لانین (4770ا): 57001018 ,8ت 871013 آلبانی (۵2اامقلم: 5177517
2469:ال اند آلبانی (7لهالمقلم: 51۸
3927:۱ رومانی (/(۸4۸۸1۸)(شاید) ه82 آلبائی (۷لما(مقلم: 82
4587:ایسلندی کهن 5۳4/01047107 )+ آلبانی (/14مهقلم: ۳
4786:ایسلندی کهن (142 50/01۷۸ صاه): آلبانی ((۸المقلم: 10
```


## [2026-09-06T21:02:52.798Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nd=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\ntxt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['zd.sraoni-','surun \\'Hinterbacken* =']:\n    i=txt.find(pat)\n    print(pat,'leaf',txt[:i].count(chr(12)),'printed',txt[:i].count(chr(12))-10)\n\"\necho \"=== HUB leaf around 6098 ===\"; sed -n '6090,6105p' HUB.txt",
 "description": "Locate Hübschmann pages"
}
```


## [2026-09-06T21:02:54.189Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '10595,10615p' incoming/ARY/ARY_pages.txt; echo \"=== search ARY page 359-ish for سرین entry ===\"; grep -n \"سرون\" incoming/ARY/ARY_pages.txt | head",
 "description": "Read Aryanpur sarin entry"
}
```


### [2026-09-06T21:02:55.218Z] TOOL RESULT

```
zd.sraoni- leaf 182 printed 172
surun 'Hinterbacken* = leaf 223 printed 213
=== HUB leaf around 6098 ===
f) Einschub von u in: durod Segenswunsch' (vgl.
padrud *Lebewohl') = ^druvatdt-^ arm. druatHc; durudan
ernten* (pr. diravam), Wrzl. dru ; diirust 'ganz, vollstandig*
^= ^drusfa- (oben p. 61) ; durust 'rauh, grob' = "^drusta-
(oben p. 61); durdy [daroy) Xiige' -= ap. drauga-; xuros
'Hahn*, xuros 'Larm', skr. kroc ; furod {firod) *hinunter', paz.
fro$, skr. pravdtd; ftiroxtan Verkaufen* aus fra-^-vaxs;
surod 'Gesang, Lied' = zd. sraota-; surudan (pr. sardyam)
singen', zd. srdvayeiti ; siiru {saru) 'Horn* = zd. srvd- ; surun
[surtfi] 'Hinterbacken*, bal. saren, zd.sraoni-; supurdan (pr.
siparam) 'iibergeben', Wrzl. spar; supdr 'Pflug', afgh. spdra
fem. 'Pflugschar; supurz 'Milz* = zd. spereza; supus, supus- 173 —
*Laus' (auch sipis u. s. w.) = zd. spis; supoxtan [sip^xtan)
'heraustreiben = paz. spuxtan, arm. spuzel : sutudan (sitdyam)
'loben*, zd. stw, sutor ^Ross' = zd. staora-; siitun Saiile*
= zd. stuna-; sunudan (sinavam) *horen' (auch sinldan, as^
```


### [2026-09-06T21:02:55.263Z] TOOL RESULT

```
سانسکریت (84(/3777): ۰" ۰ ایسلندی کهن (۷070:۸010(ی5 صت0):
0۸ ,کف ات0 0
برنانی 08810): زا دا آلمانی کهن 0570/0/0 بلط ضز0): 13703۲
لاتین (77۸ها): اند رت آلمانی (لفال05): 10
فرانسه (۳814): ۰ 0028 انگلیسی کهن (87۵18/0 ۰:02 11080
اسپانیایی (6۸(//320): زان دراه انگلیسی (577لق8۸/0): 100
[pdf page 358]
لح
هر
سرین» سرون (به چم "کبل" "نشستگاه» *تحت") / ۳۵۹
دانمارکی (0۸//3]4): لد انا پسگشت‌ها 5
سوئدی (9۷82015): 10 ۳
[ نروژی ((08/801۵/: 100 1 ((1308) دا یت ان
ملدی (3ل۵70): 11000 8 ((1303) +28 اقلا(
ایرندی کهن (لول1# 2ا0): لاه 2209 لاه
سلتی (کلنی) (81-7/6): 00 8 (11080) :005
ولزی ((8ا2): له 7 (11080) 5
: برتونی ((8870): 0 برهان قاطع : ۰ و ۱۱۳۴
فرهنگ ممین : ۸ و۱۸۷۶ ۱
اوستایی (4897821): ایرلندی کهن (#لول#/ صا0): انتاتبه
3[ 87۸00 ولزی (4ک/78: .۰ هه
=== search ARY page 359-ish for سرین entry ===
10604:سرین» سرون (به چم "کبل" "نشستگاه» *تحت") / ۳۵۹
```


## [2026-09-06T21:03:06.430Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"sraoni\\|clunis\\|šlaunis\\|slaunis\" WLD_Bd1_pages.txt | head -10; echo \"=== kalamos ===\"; grep -n \"kalamos\\|xakafiog\\|culmus\" WLD_Bd1_pages.txt | head -10",
 "description": "grep Walde-Pokorny Bd1"
}
```


### [2026-09-06T21:03:06.490Z] TOOL RESULT

```
41065:weise konnte man z. B. kel- „neigen" als „biegen“ fassen und in lat. clunis ,
46579:crdvana          crona - „lahm“                 :   lat.   clunis      s.   u.   Jdounis und u. her- „versehren“).
46795:Wood IF. 18, 28       mit lat. clunis, aisl. Maun.                                           ai.             crTni-   unter einer            Wz.
47162:   Ai. eroni- m. f., av. sraoni- f. „Hinterbacke, Hiifte", lat. dunis „Hinter-
47166:Oberschenkel, Deichselarm", apr. slaunis „Oberschenkel". Die Lautform
=== kalamos ===
43967:390 f. nur fur anlautendes 6- zugestanden wird) lat. culmus „Halm“; ahd.         ;
```


## [2026-09-06T21:03:08.256Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC kalamo ===\"; grep -n \"kalamo\\|kolamo\\|kolama\" IEC.txt | head -10; echo \"=== SYN kalamos ===\"; grep -n -i \"kalamos\\|calamus\" SYN.txt | head -5; echo \"=== SYN buttock ===\"; grep -n -i \"buttock\" SYN.txt | head -5",
 "description": "grep Mann and Buck"
}
```


### [2026-09-06T21:03:08.333Z] TOOL RESULT

```
=== IEC kalamo ===
=== SYN kalamos ===
32474:18.57 Grk. = xa apos Goth. NG weve ON pennt Lat.  calamus (penna) Dan. pen It. penna Sw. penna Fr. plume OE ss feper Sp. pluma ME penne Rum. pand, condeiu NE pen Tr. penn Du. pen Nir. peann OHG fedara W. pin MHG veder(e) Br. pluenn NHG feder
32476:1. Grk. xédXapos (> Lat. calamus), lit. ‘reed’. Hence ChSIl. triisti renders xa\a- pos as ‘reed’ (Jagic, Entstehungsgesch. 398), and also as ‘pen’ (Psalt. p. 96 Geit- ler = Psalms 45.1).
=== SYN buttock ===
5551:-4, ON bak (Dan. bag, Sw. bak adv. ‘behind’ and in ecpds. for ‘hind-’), OE bec, ME bak, NE back, OHG bah (NHG hinterbacke ‘buttock’, Du. bakboord ‘lar- board’), outside connections dub., but perh. from a root meaning ‘bend’. Walde-P. 2.148. Falk-Torp 41.
8169:Lith. Slubas (whence slubuoti ‘limp’), Slumas, Lett. slums, history dub. Not directly : Skt. (RV) ¢réna- ‘lame’ (so W. Schulze, Berl. Sitzungsber. 1910 p. 801, Mithl.-Endz. 3.941), since this is rather a deriv. of ¢réni- ‘hip, buttock’ (name of the defect from the part of the body affected, cf. VLat. corus ‘lame’, above, 2). The Baltic words may be in- dependent derivatives of a root *fleu- ‘crack, break’(?) assumed as underlying the words for ‘hip’, Skt. crénz-, Lith. Slaunis, W. clun, etc. Walde-P. 1.499 f.
9304:A word denoting a certain part of any animal may be used specifically for the meat of that part of a particular animal, So words for ‘ham’ mainly that of swine, as NE ham, once ‘hollow back of the knee’, ‘back of the thigh, buttock’ (ef. NED s.v.), NHG schinken (: schenkel ‘thigh’), Fr. jambon (: jambe ‘leg’), Russ. okorok (: SCr. krak ‘thigh’), etc. Cf. also NE bacon (: back), NHG speck ‘bacon’ (: OE spic ‘fat, fat meat or ba- con’, etc.).
10665:Fr. culotte(s), now vulgar term, fr. cul ‘rump, buttocks’, (Lat. cilus). Gamill-
23143:ble, knob’ : Lett. bulis ‘buttocks’, MLG poll ‘knob, point’, Hast Fris. pol ‘round’, ete. Walde-P. 2.111, 115. REW 1385.
```


## [2026-09-06T21:03:17.872Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '47155,47175p' WLD_Bd1_pages.txt; echo \"=== page tag near 47162 ===\"; awk 'NR<=47162 && /pdf page/{l=$0} END{print l}' WLD_Bd1_pages.txt; echo \"=== 43960 area ===\"; sed -n '43958,43980p' WLD_Bd1_pages.txt; awk 'NR<=43967 && /pdf page/{l=$0} END{print l}' WLD_Bd1_pages.txt",
 "description": "Read WLD kloumi and kolamos"
}
```


### [2026-09-06T21:03:20.097Z] TOOL RESULT

```
glaublich ist die Ankniipfung an lit. Idibas „schlank, diinn", ksl. libim
„gracilis“ als „diinner Fladen" durch Wood MLN\ 24, 49, Berneker 389).
Lit. bei Yf.      LEWb         2
                                    u. llbum,   Berneker 389.

klou-nis „Hinterbacke, Hiifte".
   Ai. eroni- m. f., av. sraoni- f. „Hinterbacke, Hiifte", lat. dunis „Hinter-
backe, Hinterkeule, SteiB bei Menschen und Tieren" (elunacuhini „kleines
Schwert oder Dolch, das man hinten trug"), cymr. corn, chin             Hiifte",
hret. klun „Hinterbacke“, aisl. Maun n. ,,Hinterbacke“, lit. szl limits ..Hiifte,
Oberschenkel, Deichselarm", apr. slaunis „Oberschenkel". Die Lautform
von       gr. xlovig,..SteiBbein" (xkoviov „Hiifte", xXortargg
                            -tog                                 nagapgQtog                   •



p,a%aiQa Hes.)     weder aus *y.lo^-vig (Fick I 4 48), noch aus idg. Yokal-
                        ist

alternation (Pedersen KG. I 121), noch durch Annahme von w-Epenthese
=== page tag near 47162 ===

=== 43960 area ===
duktionsstufe zu             -ol-).     Fick I 4 389, Zupitza Gutt. 113.

koli- „junger Hund, Tierjunges“                       :    s.   u.   qd- „rufen“       am Schlusse.

kolaino-s, *kolaina „Halm, Rohr“.
   Gr. xaXajuog,             xaXd/ur]   „Rohr“ (aus kjomo-s ?
                                                Eher Assimilation in *xo-
Xaju-ov, -co,          und        obgleicb solcbe von J. Schmidt KZ. 32,
                              bes. in xaXa/ud,
390 f. nur fur anlautendes 6- zugestanden wird) lat. culmus „Halm“; ahd.         ;


halm, halani, anord. halmr, ags. healm ,Halm“; apr. salme „Stroh“, lett.
salms „Strohha]m“, aksl. slama, russ. soloma, serb. slama „Stroh“. Curtius 139,
Zupitza Gutt. 182, Trautmann Bsl. "Wb. 298, Miihlenbach-Endzelin III 675.
   Aus gr. xdXafxos entlehnt sind ai. kalama- m. „eine Reisart, Schreibrohr“
(8. Froehde BB. I, 328 f.), lat. calamus „Rohr“, woraus wieder (trotz Loth

Rc. 18, 90) cymr. usw. calaf „Rohr“.
  Beziehung zu kel- etwa „diinner Schaft,                                Pfeil,      steifer   Halm“ (Fick II 4
73) ist erwagenswert.

qos(e)lo- „IIasel“.
```


## [2026-09-06T21:03:34.708Z] TOOL CALL #54: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D9%82%D9%84%D9%85\" \"https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CE%BB%CE%B1%CE%BC%CE%BF%CF%82\" \"https://www.etymonline.com/word/caramel\" \"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%8B%E0%A4%A3%E0%A4%BF\" \"https://en.wiktionary.org/wiki/clunis\"; do python3 tools/fetch_source.py \"$u\" --note \"pdf page 272, roots Klou-ni / Kolemos: qalam<kalamos, kalamos<PIE, caramel, sroni/clunis PIE *klownis\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-06T21:03:38.384Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6deee4fafa8e6f12.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/670b46b6fde977ad.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7ffe55e08fb5b5b9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bac8667c6d33a6fb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7651b21107bb7048.txt
```


## [2026-09-06T21:03:45.378Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%B1%DB%8C%D9%86",
 "prompt": "Give the Persian etymology of سرین (sarin/sorin) 'buttock' verbatim: Middle Persian form, Proto-Iranian, Avestan cognate."
}
```


## [2026-09-06T21:03:45.738Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/caramel",
 "prompt": "Give the English etymology of caramel verbatim: French, Spanish, Portuguese, Late Latin calamellus / cannamella discussion."
}
```


### [2026-09-06T21:03:50.220Z] TOOL RESULT

```
# Persian Etymology of سرین (sarin/sorin)

Based on the Wiktionary entry, here is the etymological chain:

**Middle Persian form:** The entry states it comes "From Middle Persian [script needed] (srēnōg)"

**Proto-Iranian:** It derives from "Proto-Iranian *cráwniš"

**Proto-Indo-European:** The ultimate origin is "Proto-Indo-European *ḱlównis"

Unfortunately, the document does not provide an Avestan cognate for this term. The entry traces the word back through Middle Persian and Proto-Iranian to Proto-Indo-European, but does not include specific Avestan comparative data.
```


### [2026-09-06T21:03:51.645Z] TOOL RESULT

```
# English Etymology of Caramel

According to the Wiktionary entry, caramel was "Borrowed from French _caramel_, from Spanish _caramelo_, from Portuguese _caramelo_, dissimilated from Late Latin _calamellus_" (a diminutive of _calamus_ meaning "reed").

An alternative etymology suggests it may derive "from Medieval Latin _cannamellis_, which is a compound of _canna_ +‎ _mellis_."

The entry also notes that caramel is "a doublet of _chalumeau_ and _shawm_."
```


## [2026-09-06T21:04:18.741Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,120p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T21:04:18.778Z] TOOL RESULT

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


## [2026-09-06T21:09:46.936Z] TOOL CALL #58: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-272.json",
 "content": "{\n  \"pdf_page\": 272,\n  \"book_page\": 242,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Klou-ni\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ḱlównis (older notation *ḱlou-ni-) 'buttock, haunch, hip'\",\n      \"note\": \"Pokorny 607-608 has exactly the headword 'ḱlou-ni-' with the meaning 'hip' and the material Old Indic śroṇi-, Avestan sraoni-, Latin clūnis, Welsh/Cornish clun, Breton klun, Old Icelandic hlaun, Lithuanian šlaunis, Latvian slauna, Old Prussian slaunis. Walde-Pokorny I 499 has the same lemma 'klou-nis \\\"Hinterbacke, Hüfte\\\"'. Wiktionary reconstructs *ḱlównis. Nourai's root name, language label ('Indo-European') and gloss ('buttock, rump') are all correct. The one defect in this chart is node #4, where the printed book labels the Baltic form slaunis 'Old Persian'; POK:608, which Nourai himself cites there, gives it as Old Prussian (apr.).\",\n      \"note_fa\": \"ریشهٔ هندواروپاییِ آغازین *ḱlównis «تهیگاه، سرین، کپل» است که پوکورنی (ص ۶۰۷–۶۰۸) زیر سرواژهٔ ḱlou-ni- آورده و بازماندگان آن را سنسکریت śroṇi-، اوستایی sraoni-، لاتینی clūnis، ولزی clun، ایسلندی کهن hlaun، لیتوانیایی šlaunis و پروسی کهن slaunis شمرده است؛ والده-پوکورنی (ج ۱ ص ۴۹۹) نیز همین را دارد. پس نام ریشه، برچسب زبانی و معنایی که نورایی داده درست است. تنها ایراد این نمودار در گرهٔ ۴ است: صورت slaunis در کتاب «پارسی باستان» برچسب خورده، حال آنکه در همان صفحهٔ ۶۰۸ پوکورنی که نورایی به آن ارجاع می‌دهد، این واژه «پروسی کهن» است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/clunis\",\n        \"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%8B%E0%A4%A3%E0%A4%BF\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:607\", \"status\": \"supports\", \"note\": \"POK_full.txt (block 'Root / lemma: Ḱlou-nl-', 'Page(s): 607-608'): 'Meaning: hip … Old Indie sroni- m. f., Avestan sraonl- f. \\\"buttock, hip, haunch\\\"; Latin clūnis … Lithuanian slaunis … Old Prussian slaunis \\\"thigh\\\"'. Exactly Nourai's root and gloss.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 499 (incoming/WLD/WLD_Bd1_pages.txt line 47162)\", \"stance\": \"supports\", \"note\": \"'klou-nis \\\"Hinterbacke, Hüfte\\\". Ai. çroni- m. f., av. sraoni- f. \\\"Hinterbacke, Hüfte\\\", lat. clunis … lit. szlaunis \\\"Hüfte, Oberschenkel\\\", apr. slaunis \\\"Oberschenkel\\\".'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, IE roots appendix\", \"stance\": \"silent\", \"note\": \"grep of AHD_watkins1985.txt for 'klouni/kleuni' finds nothing — Watkins does not carry this root (no English reflex), so AHD is silent rather than contradicting.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 4.17 area, SYN.txt line 8169\", \"stance\": \"supports\", \"note\": \"'…words for \\\"hip\\\", Skt. çreṇi-, Lith. šlaunis, W. clun, etc. Walde-P. 1.499 f.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"sraoni\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Younger Avestan sraoni- (stem sraonay-) f. 'buttock, haunch' is the regular Iranian reflex of PIE *ḱlównis: PIE initial *ḱl- gives Indo-Iranian *ćr- (satem palatalisation of *ḱ, and *l > r), whence Av. sr-, exactly as in Sanskrit śroṇi-; the *-ou- diphthong is kept as Av. -ao-. Bartholomae's Altiranisches Wörterbuch col. 1634 lists 'j. sraonay- f. \\\"Hinterbacken\\\"' from Vd. 8.56-58 and 9.20 f., and compounds pərəθu.sraonay- 'with broad hips' (Yt. 5.54) and sraoni.masah- 'of the size of a haunch'. The gloss 'buttock' is right.\",\n          \"derivation_fa\": \"اوستایی متأخر sraoni- (ستاک sraonay-) به معنی «تهیگاه، سرین» بازماندهٔ منظمِ *ḱlównis هندواروپایی است: *ḱ آغازیِ کامی‌شده در شاخهٔ هندوایرانی به ć و سپس در اوستایی به s بدل شده و *l هندواروپایی در هندوایرانی همه‌جا به r تبدیل شده است؛ ازاین‌رو *ḱl- به sr- رسیده، درست مانند سنسکریت śroṇi-. مصوت مرکب *-ou- نیز در اوستایی به‌صورت -ao- مانده است. بارتولومه این واژه را از وندیداد ۸٫۵۶–۵۸ و ۹٫۲۰ و نیز در ترکیب‌های pərəθu.sraonay- «پهن‌تهیگاه» (یشت ۵٫۵۴) ثبت کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%8B%E0%A4%A3%E0%A4%BF\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:607\", \"status\": \"supports\", \"note\": \"POK_full.txt s.v. Ḱlou-nl- (Page(s) 607-608): 'Old Indie sroni- m. f., Avestan sraonl- f. \\\"buttock, hip, haunch\\\"'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt line 27233-27234 (col. ~1634)\", \"stance\": \"supports\", \"note\": \"'j. sraonay- f. \\\"Hinterbacken\\\": haoyam … V. 8.56-58, 9.20 f.' and in the following line 'ai. śroṇi- ni., f. \\\"Hüfte\\\", np. surūn \\\"Hinterbacken, -teil\\\". — Pū.: srēnak'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 499\", \"stance\": \"supports\", \"note\": \"'av. sraoni- f. \\\"Hinterbacke, Hüfte\\\"' listed directly under klou-nis.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. clunis (LAT.txt line 12670 ff.)\", \"stance\": \"supports\", \"note\": \"'Cf., avec le même sens, irl. cluain, gall. clun, skr. çroṇih, av. sraonis (fem.), lit. šlaunis (fém.) et v. pruss. slaunis, v.isl. hlaun \\\"fesse\\\".'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"sarŭk\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Pahlavi word is real: it is the Zand gloss on Vd. 8 (Pahlavi Vendidad), and Horn, Grundriss no. 737 (p. 162), which Nourai cites, prints exactly 'phlv. sarūk, vd. 8 (178)(181), sarīn \\\"Hinterer\\\" (Bund.), sarīnak (PPGl.)'. But 'sarūk' is Horn's 1893 reading of the Pahlavi spelling <slwk'>; modern Pahlavi lexicography reads the same graph srēn / srēnag (with the -ag/-ak diminutive-forming suffix, MP -ak > NP -a). Bartholomae already gives 'Pū.: srēnak', and Wiktionary reconstructs the New Persian word from Middle Persian srēnōg/srēnag. MacKenzie's Concise Pahlavi Dictionary does not list it at all (it glosses 'buttock' only with kun and 'haunch' with haxt). So the arrow Av. sraoni- → MP is sound, but the transcription 'sarŭk' is a superseded 19th-century reading rather than an error of the extraction.\",\n          \"derivation_fa\": \"واژهٔ پهلوی واقعی است و در زند وندیداد ۸ آمده؛ هرن در «مبانی ریشه‌شناسی فارسی نو» (شمارهٔ ۷۳۷، ص ۱۶۲) که نورایی به همان ارجاع داده، عیناً می‌نویسد: «phlv. sarūk, vd. 8، sarīn (بندهش)، sarīnak». اما sarūk خوانشِ هرن (۱۸۹۳) از نوشتار <slwk'> است؛ ایران‌شناسی امروزی همان نوشتار را srēn / srēnag می‌خواند (پسوند -ag/-ak پهلوی که در فارسی نو به «ه» بدل می‌شود). بارتولومه نیز صورت پهلوی را srēnak آورده و ویکی‌واژه فارسیِ «سرین» را از فارسی میانهٔ srēnōg می‌گیرد؛ مکنزی این واژه را اصلاً نیاورده است. پس پیوندِ اوستایی ← فارسی میانه درست است، ولی آوانویسیِ «sarŭk» خوانشی کهنه است، نه خطای اسکن. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B3%D8%B1%DB%8C%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:162\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 184 (= printed p. 162), no. 737: 'surīn, surūn \\\"Hinterbacken, Hinterer\\\". aw. sraoni- \\\"Hüfte\\\"; phlv. sarūk, vd. 8 (178)(181), sarīn \\\"Hinterer\\\" (Bund.), sarīnak (PPGl.); ai. śroṇī …; lit. szlaunis, lat. clunis, gr. κλόνις (?), ahd. hlaun.' Nourai's Pahlavi form and the whole chain come verbatim from this entry.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt line 27234 (s.v. sraonay-)\", \"stance\": \"partial\", \"note\": \"'— Pū.: srēnak, (zu V.9.10): sinak \\\"Brust\\\"' — same Pahlavi word, read srēnak, not sarūk.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, English index 'buttock'/'haunch' (PHD.txt lines 1128, 2225; PHD_mackenzie.txt lines 3353, 2879)\", \"stance\": \"silent\", \"note\": \"'buttock kun.' / 'haunch haxt.' — MacKenzie has no sarūg/srēn entry, so the Concise Pahlavi Dictionary neither confirms nor denies.\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt, grep 'srēn|sren|sarēn'\", \"stance\": \"silent\", \"note\": \"no hit — Nyberg's Manual glossary (limited to his text selection) does not contain the word.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien pp. 172-173 (HUB.txt leaf 223)\", \"stance\": \"partial\", \"note\": \"'surun [surīn] \\\"Hinterbacken\\\", bal. sarēn, zd. sraoni-' — Hübschmann goes straight from Avestan to New Persian, citing Baluchi sarēn, without an intermediate Pahlavi form.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"sorŭn «سُرون ۲»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP سرون sorūn/surūn 'buttock, rump', with the doublet سرین sarīn/sorīn given in the same box, continues Old Iranian *sraunī- and *srainī- respectively: Hübschmann (Persische Studien, quoted by Mo'in in the Borhān footnote) explicitly derives «سرین» (and Baluchi sarēn) from *srainī- and «سرون» from *sraunī-, i.e. two ablaut variants of the Avestan stem sraoni-. Phonetically Old Iranian sr- is kept in Middle Persian, the -ī of the feminine stem gives the NP -īn/-ūn ending, and the anaptyctic u of the cluster gives su-/so-. Ferdowsī's line quoted in the box («… سَرونی بزد بر سَرین سیاه») uses both members. The plural/variant سرین printed in the box is the standard modern word.\",\n          \"derivation_fa\": \"«سُرون» و همزادش «سَرین» که در همان جعبه آمده، دنبالهٔ ایرانی باستانِ *sraunī- و *srainī- اند؛ هوبشمان — که معین در حاشیهٔ برهان قاطع (ص ۱۱۳۴) نقلش می‌کند — به‌صراحت «سرین» (و بلوچی sarēn) را از *srainī- و «سرون» را از *sraunī- می‌گیرد، یعنی دو گونهٔ ابلاوتیِ همان ستاک اوستایی sraoni-. از نظر آوایی خوشهٔ sr- آغازی در فارسی میانه مانده و در فارسی نو با واکهٔ میانجی u/o شکسته شده (سُرون، سَرین)، و -ī ستاکِ مادینه به پایانهٔ -ūn/-īn انجامیده است. بیت فردوسی که نورایی آورده هر دو صورت را در کنار هم دارد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%D8%B1%DB%8C%D9%86\",\n            \"https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%8B%E0%A4%A3%E0%A4%BF\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1134\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 596 (printed ≈1134-1139; page number confirmed independently by Aryanpur, who cites 'برهان قاطع … و ۱۱۳۴' under his سرین/سرون entry). Mo'in's footnote 4 to سرون: «سرین (ه.م.). اوستا -sraoni (تهیگاه)، پهلوی srēn (سرین)، هندی باستان śroṇi- (سرین، ران، تهیگاه)، لیتوانی šlaunis، لاتینی clunis … بلوچی sarēn (کمر، تهیگاه) … هوبشمان گوید: فارسی «سرین» بلوچی sarēn از *srainī و فارسی «سرون» از *sraunī …» — precisely Nourai's arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Grundriss no. 737, p. 162\", \"stance\": \"supports\", \"note\": \"'surīn, surūn \\\"Hinterbacken, Hinterer\\\" … aw. sraoni-'.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien pp. 172-173\", \"stance\": \"supports\", \"note\": \"'surun [surīn] \\\"Hinterbacken\\\", bal. sarēn, zd. sraoni-'; also p. 64 area 'surun (surīn) \\\"Hinterbacken\\\" = zd. …'.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur p. 359 (incoming/ARY/ARY_pages.txt line 10604)\", \"stance\": \"supports\", \"note\": \"headword «سرین، سرون (به چم \\\"کپل\\\", \\\"نشستگاه\\\", \\\"تحت\\\")» with Avestan sraoni and Germanic/Celtic cognates, and the citations «برهان قاطع: … و ۱۱۳۴؛ فرهنگ معین: … و ۱۸۷۶» — independently confirms that BQT p.1134 is the سرون/سرین page.\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 2 leaf 596, entry سرون + Mo'in's footnote\", \"stance\": \"supports\", \"note\": \"see ref_check; the footnote also quotes Shahid Balkhi «گرچه برتابد آن میان و سرون» (Loghat-e Fors).\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Old Persian\",\n          \"words\": \"slaunis\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"There is no Old Persian word *slaunis: Old Persian has no initial sl- cluster at all, and the form is not in Kent's lexicon. The form slaunis is the OLD PRUSSIAN word 'thigh' (beside Lithuanian šlaunis), and it stands as such on the very page Nourai cites: Pokorny 608 ends the ḱlou-ni- article with 'Lithuanian šlaunis \\\"femur, thigh, hip\\\", Latvian slauna \\\"hip\\\"; Old Prussian slaunis \\\"thigh\\\"'. Walde-Pokorny I 499 has 'apr. slaunis \\\"Oberschenkel\\\"' and Ernout-Meillet s.v. clunis 'lit. šlaunis (fém.) et v. pruss. slaunis'. I rendered pdf page 272 at 200 dpi and read the box: the printed book itself says 'Old Persian ▯ POK:608 / slaunis : buttock', so this is Nourai's own misreading of 'Old Prussian' as 'Old Persian' (an easy slip in an English abbreviation list), not an extraction error. The word and the gloss are otherwise correct; only the language label is wrong.\",\n          \"derivation_fa\": \"واژه‌ای به‌نام *slaunis در پارسی باستان وجود ندارد؛ اصلاً خوشهٔ آغازیِ sl- در پارسی باستان ممکن نیست و کنت هم چنین سرواژه‌ای ندارد. slaunis واژهٔ «پروسیِ کهن» به معنی «ران» است (در کنار لیتوانیایی šlaunis) و درست در همان صفحهٔ ۶۰۸ پوکورنی که نورایی به آن ارجاع داده آمده است؛ والده-پوکورنی (ج ۱ ص ۴۹۹) نیز «apr. slaunis» دارد و ارنو-میه ذیل clunis «v. pruss. slaunis». تصویر صفحهٔ ۲۷۲ نسخهٔ پی‌دی‌اف را با دقت ۲۰۰ نقطه رندر و بازخوانی کردم: خودِ کتاب چاپی «Old Persian» نوشته است، پس این خطای چاپی/خوانشِ خودِ نورایی است («Old Prussian» را «Old Persian» خوانده)، نه خطای استخراج داده. واژه و معنایش درست است و تنها برچسب زبانی نادرست است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"Old Persian ▯ POK:608 | slaunis : buttock\",\n          \"correct_form\": \"Old Prussian slaunis 'thigh' (cf. Lithuanian šlaunis)\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/clunis\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:608\", \"status\": \"contradicts\", \"note\": \"POK_full.txt s.v. Ḱlou-nl- (Page(s) 607-608): 'Lithuanian slaunis \\\"femur, thigh, hip, haunch, ham\\\", Latvian slauna \\\"hip\\\"; Old Prussian slaunis \\\"thigh\\\".' Pokorny lists no Old Persian form anywhere in this article.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon pp. 164-215 (KNT.txt)\", \"stance\": \"silent\", \"note\": \"no headword slaunis / sraun- / *sl- of any kind; Old Persian permits no word-initial sl-.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 499\", \"stance\": \"contradicts\", \"note\": \"'lit. szlaunis \\\"Hüfte, Oberschenkel, Deichselarm\\\", apr. slaunis \\\"Oberschenkel\\\"' — the form is Old Prussian.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. clunis\", \"stance\": \"contradicts\", \"note\": \"'lit. šlaunis (fém.) et v. pruss. slaunis' — Baltic, not Iranian.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": null,\n          \"words\": \"\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"Empty pass-through box: on the printed page an arrow leaves the 'Old Persian slaunis' box and ends in a wide, completely blank rectangle to its right (verified on the 200 dpi render of pdf page 272). There is no language label, no reference and no word, so nothing can be checked; it is a layout artefact of Nourai's chart template (the slot where a Persian reflex would have gone), not a derivation. The extraction is faithful to the page.\",\n          \"derivation_fa\": \"این گره جعبه‌ای تهی است: در صفحهٔ چاپی پیکانی از جعبهٔ «Old Persian slaunis» بیرون می‌آید و به مستطیلی کاملاً خالی می‌رسد (روی تصویر ۲۰۰ نقطه‌ایِ صفحهٔ ۲۷۲ وارسی شد). نه برچسب زبانی دارد، نه ارجاع و نه واژه؛ پس چیزی برای راستی‌آزمایی نیست و تنها یک جای خالیِ قالبِ نمودار است (جایی که قاعدتاً بازتاب فارسی باید می‌آمد). استخراج داده با صفحهٔ چاپی مطابق است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 607-608 s.v. ḱlou-ni-\", \"stance\": \"silent\", \"note\": \"nothing further follows Old Prussian slaunis in Pokorny's article, so no candidate for the blank box.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Latin\",\n          \"words\": \"clŭnis\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin clūnis (m./f., usually plural clūnēs) 'buttock, haunch, rump of men and animals' is the direct Italic inheritance of PIE *ḱlównis, via Proto-Italic *klounis: PIE *ḱ gives Latin c-, and the diphthong *-ou- regularly monophthongises to Latin ū (as in *doukō > dūcō). Ernout-Meillet call it 'ancien, populaire ou technique', mostly synonymous with natēs, and derive clūnāculum 'small sacrificial knife (worn at the haunch)' from it. Note the quantity: the book prints clŭnis with a breve, but the vowel is long (clūnis) — that is the only quibble, and it is Nourai's diacritic, faithfully extracted.\",\n          \"derivation_fa\": \"لاتینی clūnis (بیشتر جمع clūnēs) «سرین، کپل، دنبالهٔ آدمی و جانور» بازماندهٔ مستقیم *ḱlównis هندواروپایی از راه ایتالیکِ آغازین *klounis است: *ḱ در لاتینی به c بدل شده و مصوت مرکب *-ou- طبق قاعده به ū بلند یک‌آوایی شده است (همان‌گونه که *doukō > dūcō). ارنو-میه آن را واژه‌ای «کهن، عامیانه یا فنی» و هم‌معنای natēs می‌خوانند و مشتق clūnāclum «کارد کوچک قربانی» را از آن می‌گیرند. تنها نکته آنکه کتاب clŭnis با علامت کوتاهی نوشته، حال آنکه واکهٔ آن بلند است (clūnis)؛ این خطای نشانه‌گذاریِ خودِ کتاب است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/clunis\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:607\", \"status\": \"supports\", \"note\": \"POK_full.txt s.v. Ḱlou-nl-: 'Latin clūnis \\\"a buttock, haunch, rump of people and animals\\\" (clunaculum \\\"small sword or dagger which one carries behind\\\")'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. clunis (LAT.txt line 12670 ff.)\", \"stance\": \"supports\", \"note\": \"'clunis, -is et clunes, -ium … fesses, croupe. Ancien, populaire ou technique … Cf., avec le même sens, irl. cluain, gall. clun, skr. çroṇih, av. sraonis, lit. šlaunis et v. pruss. slaunis, v.isl. hlaun \\\"fesse\\\".'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 499\", \"stance\": \"supports\", \"note\": \"'lat. clunis \\\"Hinterbacke, Hinterkeule, Steiß bei Menschen und Tieren\\\" (clunaculum …)'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck, SYN.txt line 8169\", \"stance\": \"supports\", \"note\": \"cites the same group ('words for \\\"hip\\\", Skt. çreṇi-, Lith. šlaunis, W. clun, etc. Walde-P. 1.499 f.').\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 8,\n      \"root\": \"Kolemos, Kolemâ\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ḱolh₂mos / *ḱolh₂meh₂ (Pokorny's *ḱolǝmo-s, *ḱolǝmā) 'stalk, reed, straw'\",\n      \"note\": \"Pokorny 612 has the headword 'Ḱolamo-s, Ḱolamā', meaning 'stalk; reed', with Gk. κάλαμος/καλάμη, Lat. culmus, OHG halm, ON halmr, OE healm, OPr. salme, Latv. salms, OCS slama, and Toch. A kulmäṃts. Watkins/AHD prints it 'kolem-. Grass, reed. … [Pok. ḱolǝmo-s 612.]'. Nourai's root name (which follows AHD's 'kolem-'), the Indo-European label and the gloss 'grass, reed, cane' are all correct. Wiktionary now sets it up as *ḱelh₂-m- with a zero-grade genitive *ḱl̥h₂mós giving Greek kálamos. The chart is right that Latin calamus and Sanskrit kalama are BORROWINGS from Greek (not inherited): Pokorny says so explicitly, so his arrows Greek→Latin and Greek→Sanskrit are the standard view; Latin culmus, not calamus, is the inherited Italic form.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی *ḱolh₂mos / *ḱolh₂meh₂ «ساقه، نی، کاه» است؛ پوکورنی (ص ۶۱۲) آن را زیر Ḱolamo-s, Ḱolamā با بازماندگان یونانی kálamos/kalámē، لاتینی culmus، آلمانی علیای کهن halm، انگلیسی کهن healm، پروسی کهن salme و اسلاوی کلیسایی کهن slama آورده، و واتکینز (AHD) به‌صورت kolem- «علف، نی». پس نام ریشه، برچسب زبانی و معنایی که نورایی داده درست است. ویکی‌واژه امروز آن را *ḱelh₂-m- بازسازی می‌کند که kálamos یونانی از گونهٔ صفرْدرجهٔ آن *ḱl̥h₂mós می‌آید. نکتهٔ مهم اینکه نمودار به‌درستی calamus لاتینی و kalama سنسکریت را «وام‌واژه» از یونانی نشان داده است، نه بازماندهٔ ارثی؛ صورت ارثیِ لاتینی culmus است. ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CE%BB%CE%B1%CE%BC%CE%BF%CF%82\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:612\", \"status\": \"supports\", \"note\": \"POK_full.txt, 'Root / lemma: Ḱolamo-s, Ḱolamā / Meaning: stalk; reed … Page(s): 612': 'Gr. κάλαμος, καλάμη \\\"reed\\\" (assimilated from kol-?); Latin culmus \\\"stem\\\"; Old High German halm … From gr. κάλαμος are borrowed Old Indic kalama- m. \\\"a kind of rice, writing pipe\\\" and Latin calamus \\\"reed\\\"'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. I p. 464 (incoming/WLD/WLD_Bd1_pages.txt line 43960 ff.)\", \"stance\": \"supports\", \"note\": \"'kolamo-s, *kolamā \\\"Halm, Rohr\\\". Gr. κάλαμος, καλάμη \\\"Rohr\\\" … lat. culmus \\\"Halm\\\"; ahd. halm … Aus gr. κάλαμος entlehnt sind ai. kalama- m. \\\"eine Reisart, Schreibrohr\\\", lat. calamus \\\"Rohr\\\".'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kolem-\", \"stance\": \"supports\", \"note\": \"'kolem-. Grass, reed. Suffixed form *kolǝm-o-. 1. Germanic *halmaz in Old English healm … 2. Latin culmus, stalk: CULM. 3. Zero-grade form *kl̥ǝm-o- in Greek kalamos, a reed, straw: CALAMITE, CALAMUS, CALUMET, CARAMEL, SHAWM. [Pok. ḱolǝmo-s 612.]'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 18.57 'pen' (SYN.txt line 32474-32476)\", \"stance\": \"supports\", \"note\": \"'Grk. κάλαμος (> Lat. calamus), lit. \\\"reed\\\". Hence ChSl. trŭstĭ renders κάλαμος as \\\"reed\\\" … and also as \\\"pen\\\".'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt (grep kolam/kalam/kolem)\", \"stance\": \"silent\", \"note\": \"no entry found for this lemma in the OCR of Mann's dictionary.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Greek\",\n          \"words\": \"kalamos\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek κάλαμος 'reed', and by metonymy 'reed-pen, fishing rod, shepherd's pipe', continues the zero-grade of the root: PIE *ḱl̥h₂mós > Greek kálamos, with the laryngeal vocalised as a and the accent retracted; Pokorny explains the initial ka- as assimilated from *kol- (κάλαμος beside καλάμη 'stalk, stubble'). It is the inherited Greek member of the same set as Latin culmus, OE healm 'straw' and OCS slama. The gloss 'a reed (used as a pen)' is exactly right: it is already 'pen' in Hellenistic Greek (e.g. 3 John 13 κάλαμος καὶ μέλαν).\",\n          \"derivation_fa\": \"یونانی باستان κάλαμος «نی» و به‌مجاز «قلمِ نی، چوب ماهیگیری، نایِ چوپانی» دنبالهٔ گونهٔ صفرْدرجهٔ ریشه است: *ḱl̥h₂mós هندواروپایی که در آن لارنگال به a بدل شده و تکیه پس رفته است. پوکورنی ka- آغازی را همگون‌شدهٔ *kol- می‌داند (κάλαμος در کنار καλάμη «ساقه، کُلَش»). این واژه هم‌ریشهٔ ارثیِ culmus لاتینی، healm انگلیسی کهن و slama اسلاوی کلیسایی کهن است. معنای «نی (که با آن می‌نوشتند)» درست است؛ در یونانیِ هلنیستی همان «قلم» است (رسالهٔ سوم یوحنا ۱۳: κάλαμος καὶ μέλαν).\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CE%BB%CE%B1%CE%BC%CE%BF%CF%82\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:612\", \"status\": \"supports\", \"note\": \"'Gr. κάλαμος, καλάμη \\\"reed\\\" (assimilated from kol-?)' — first item of the material under Ḱolamo-s.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 464\", \"stance\": \"supports\", \"note\": \"'Gr. κάλαμος, καλάμη \\\"Rohr\\\" (aus kḷomo-s? Eher Assimilation in *κολαμ-ον …)'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. kolem-\", \"stance\": \"supports\", \"note\": \"'Zero-grade form *kl̥ǝm-o- in Greek kalamos, a reed, straw'.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 18.57\", \"stance\": \"supports\", \"note\": \"'Grk. κάλαμος (> Lat. calamus), lit. \\\"reed\\\"' — listed as the Greek word for 'pen'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Arabic\",\n          \"words\": \"qalam\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Arabic قَلَم qalam 'reed-pen' is indeed of Greek origin — the native derivation from the root q-l-m 'to cut, pare' is folk etymology (the verb qalama is denominative) — but the borrowing was not direct from Greek. Jeffery, Foreign Vocabulary of the Qurʾān pp. 242-243, states it plainly: 'the word is the Gk. κάλαμος a reed and then a pen, though coming through some Semitic form. κάλαμος was borrowed into Aram., where we find qulmōs, Syr. qalmā, but it was from the Eth. ḳalam, as Nöldeke, Neue Beiträge 50, has shown, that the word came into Arabic. It was an early borrowing, for it is found both in the old poetry and in the S. Arabian inscriptions.' Wiktionary likewise routes it through Geʿez. So Nourai's Greek→Arabic arrow is right in origin but skips the Aramaic/Geʿez mediation, and the shape qalam (a > a, -os dropped) is Semitic, not Greek.\",\n          \"derivation_fa\": \"عربی «قَلَم» به‌راستی یونانی‌تبار است — اشتقاق آن از ریشهٔ ق‌ل‌م «بریدن» ریشه‌شناسی عامیانه است و فعل «قَلَمَ» خودْ مشتق از اسم است — اما وام‌گیری مستقیم از یونانی نبوده. آرتور جفری در «واژه‌های دخیل در قرآن» (ص ۲۴۲–۲۴۳) روشن می‌گوید: κάλαμος نخست به آرامی (قولموس) و سریانی (قَلما) رفته و سپس، چنان‌که نولدکه نشان داده، از راه گعزی (حبشی) وارد عربی شده است؛ وامی کهن است، چون هم در شعر جاهلی و هم در کتیبه‌های عربی جنوبی دیده می‌شود. ویکی‌واژه نیز همین مسیر گعزی را می‌آورد. پس پیکانِ «یونانی ← عربی» در اصلْ درست است ولی واسطهٔ آرامی/گعزی را نادیده گرفته؛ با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%82%D9%84%D9%85\"],\n          \"ref_check\": [\n            {\"ref\": \"TAD:57\", \"status\": \"not_found\", \"note\": \"TAD_pages.txt leaf 61 (printed ≈57, offset leaf−4..6) is the ق section running قاش … قفص … قنبلة … قند, i.e. exactly where قلم belongs, but the two-column Arabic OCR of that leaf is scrambled and the قلم entry cannot be read out of it; ref_page.py TAD:57 --image reports 'no scan of TAD covers printed page 57'. The neighbouring entries on the same leaves (قبطان, قرمز 'from Arabic into European', قرميد < κεραμίς, قصدير, قنديل < candela, قنطار < centenarium, قيراط < κεράτιον) show al-ʿUnaysī does give exactly this Greek/Latin-origin information, so the citation is of the right character, but I could not read the line itself.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾān pp. 242-243 s.v. قلم (FVQ_pages.txt lines 8752 ff.)\", \"stance\": \"partial\", \"note\": \"'The native authorities take the word from قلم to cut …, but this is only folk-etymology, for the word is the Gk. κάλαμος a reed and then a pen, though coming through some Semitic form. κάλαμος was borrowed into Aram. … Syr. qalmā, but it was from the Eth. ḳalam, as Nöldeke, Neue Beiträge, 50, has shown, that the word came into Arabic.'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. calamary/calamus (KLN_1966.txt line 6126)\", \"stance\": \"supports\", \"note\": \"'calamus, \\\"reed, pen\\\", fr. Gk. κάλαμος, prob. an assimilated form of orig. *κόλαμος, and, accordingly, cognate with L. culmus' — Klein confirms the Greek word behind the whole family.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (AFM.txt, grep قلم)\", \"stance\": \"silent\", \"note\": \"no entry — Addi Shir's book covers Persian loans in Arabic, and qalam is not claimed as Persian, which is itself consistent with the Greek etymology.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"qalam «قلم»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP قلم qalam 'pen; (by extension) an item, entry in a list' is a straightforward Arabic loan into New Persian, taken over with its Arabic broken plural اقلام aqlām, which is what the box's extra script gives. Moʿin marks the headword «قلم» explicitly '[معر. یو.]' = muʿarrab-e yūnānī, 'Arabicised from Greek', and lists 'ج. اقلام'. The secondary Persian sense 'item, entry (in an account)' is a book-keeping metonymy (each entry written with one stroke of the pen), well attested in Qajar-era administrative Persian. The Rumi couplet in the box («خود قلم اندر نوشتن می‌شتافت …») is genuine Masnavi material.\",\n          \"derivation_fa\": \"«قلم» در فارسی نو وام‌واژه‌ای عربی است که با جمع مکسّرِ عربیِ «اقلام» — همان که در جعبه آمده — به فارسی راه یافته است. معین در فرهنگ فارسی ذیل «قلم» تصریح می‌کند «[معر. یو.]» یعنی معرّبِ یونانی، و جمع آن را «اقلام» می‌آورد. پس زنجیرهٔ یونانی ← عربی ← فارسی که نورایی کشیده درست است و «قلم» فارسی وام‌واژه‌ای است که از راه عربی به فارسی رسیده، نه ارثیِ ایرانی. معنای دومِ «قلم» (= فقره، ردیف در سیاهه) تحول معنایی اداری-دفترداری است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%82%D9%84%D9%85\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:2715\", \"status\": \"supports\", \"note\": \"Moʿin, Farhang-e Fārsi s.v. قلم (MON_part2.txt line 14284): «قلم: [معر. یو.] (اِ.) آلتی نی‌ین یا چوبین یا فلزی که به وسیلهٔ آن با مرکب یا جوهر روی کاغذ نویسند؛ خامه، کلک؛ ج. اقلام.» The tag [معر. یو.] = 'Arabicised from Greek' is exactly Nourai's Greek→Arabic→Persian route, and 'ج. اقلام' is the box's extra form.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. قلم\", \"stance\": \"supports\", \"note\": \"see ref_check; Moʿin's origin tag [معر. یو.].\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 242-243\", \"stance\": \"supports\", \"note\": \"establishes the Arabic word itself as a Greek loan (via Aramaic/Geʿez), which is the source of the Persian.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā (incoming/ARY/ARY_pages.txt, grep قلم)\", \"stance\": \"silent\", \"note\": \"no headword قلم — Aryanpur's dictionary covers only inherited Indo-European Persian vocabulary, so an Arabic loan is (correctly) absent.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"calamus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin calamus 'reed, cane; reed-pen; reed-pipe' is a learned/technical borrowing from Greek κάλαμος, taken over in the Republican period along with much Greek writing and horticultural vocabulary; it is NOT inherited (the inherited Italic reflex of the root is culmus 'stalk'), and the a-vocalism betrays the loan. Pokorny 612 says so in as many words, and Klein s.v. calamary derives 'L. calamārius … fr. calamus, reed, pen, fr. Gk. κάλαμος'. From it come Welsh calaf 'reed' and the whole Romance family (It. calamo, Fr. chalumeau, Sp. caramillo). Nourai draws the arrow Greek→Latin, which is the standard view.\",\n          \"derivation_fa\": \"لاتینی calamus «نی، قلمِ نی، نایِ نی» وام‌واژه‌ای است از یونانی κάλαμος که در دورهٔ جمهوری همراه با انبوهی از واژگان نوشتاری و باغبانیِ یونانی به لاتین راه یافت؛ صورت ارثیِ همین ریشه در لاتین culmus «ساقه» است و همان a در calamus نشانهٔ وام‌بودن آن است. پوکورنی (ص ۶۱۲) صریحاً می‌گوید «از یونانی κάλαμος وام گرفته شده‌اند: سنسکریت kalama- و لاتینی calamus». کلاین نیز calamus را «از یونانی κάλαμος» می‌داند. از همین واژه ولزی calaf و خانوادهٔ رومانسِ آن (ایتالیایی calamo، فرانسوی chalumeau، اسپانیایی caramillo) برآمده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CE%BB%CE%B1%CE%BC%CE%BF%CF%82\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:201\", \"status\": \"supports\", \"note\": \"Nourai's AHD:201 is the main-dictionary page of the American Heritage Dictionary (New College ed.) carrying the headword 'calamus'; the corresponding Watkins appendix entry (AHD_watkins1985.txt s.v. kolem-) reads 'Zero-grade form *kl̥ǝm-o- in Greek kalamos, a reed, straw: CALAMITE, CALAMUS, CALUMET, CARAMEL, SHAWM', i.e. AHD does derive Latin/English calamus from Greek kalamos under this root.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 612 s.v. Ḱolamo-s\", \"stance\": \"supports\", \"note\": \"'From gr. κάλαμος are borrowed Old Indic kalama- … and Latin calamus \\\"reed\\\", from which again cymr. etc. calaf \\\"reed\\\".'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 464\", \"stance\": \"supports\", \"note\": \"'Aus gr. κάλαμος entlehnt sind ai. kalama- …, lat. calamus \\\"Rohr\\\", woraus wieder … cymr. usw. calaf \\\"Rohr\\\".'\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. calamary (KLN_1966.txt line 6126)\", \"stance\": \"supports\", \"note\": \"'calamary, n., squid. — L. calamārius, \\\"pertaining to a pen\\\", fr. calamus, \\\"reed, pen\\\", fr. Gk. κάλαμος, prob. an assimilated form of orig. *κόλαμος, and, accordingly, cognate with L. culmus.'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 18.57\", \"stance\": \"supports\", \"note\": \"'Grk. κάλαμος (> Lat. calamus)'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"French\",\n          \"words\": \"caramel\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"French caramel 'burnt sugar' (17th c.) does go back to Latin calamus, but not directly from Latin to French: it was borrowed from Spanish caramelo (older caramel), itself from Portuguese caramelo, which is generally taken to be a dissimilated Late Latin calamellus, the diminutive of calamus 'reed' (a stick of hardened sugar looking like a little reed / an icicle — Portuguese caramelo also means 'icicle'). A competing and older view (Klein, Etymonline) makes Old Spanish caramel a blend of Medieval Latin cannamella 'sugar-cane' (canna + mel 'honey') with Spanish caramillo 'reed' < Latin calamellus, and some derive the Medieval Latin word from Arabic. Watkins/AHD nevertheless files CARAMEL under kolem-, so the ultimate root is not in doubt; what Nourai's single Latin→French arrow hides is the Iberian mediation and the possible cannamella contamination.\",\n          \"derivation_fa\": \"فرانسویِ caramel «شکرِ سوخته» (سدهٔ ۱۷) سرانجام به calamus لاتینی بازمی‌گردد، اما نه یکراست: فرانسوی آن را از اسپانیایی caramelo (کهن‌تر caramel) وام گرفته، و آن خود از پرتغالی caramelo است که آن را دگرگون‌شدهٔ calamellus لاتینیِ متأخر، مصغّرِ calamus «نی»، می‌دانند (پرتغالی caramelo به معنی «قندیل یخ» هم هست). دیدگاه رقیب (کلاین و اتیمانلاین) caramel اسپانیایی کهن را آمیزه‌ای از cannamella لاتینیِ سده‌های میانه «نیشکر» (canna + mel «عسل») با caramillo اسپانیایی «نی» می‌شمارد و برخی cannamella را عربی‌تبار می‌دانند. با این‌همه واتکینز در پیوستِ AHD واژهٔ CARAMEL را زیر همین ریشهٔ kolem- می‌آورد؛ پس ریشهٔ نهایی محل تردید نیست و آنچه پیکانِ یکبارهٔ «لاتین ← فرانسه»ی نورایی پنهان می‌کند واسطهٔ ایبریایی و احتمال آمیختگی با cannamella است. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/caramel\",\n            \"https://en.wiktionary.org/wiki/caramel\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. kolem-: '… in Greek kalamos, a reed, straw: CALAMITE, CALAMUS, CALUMET, CARAMEL, SHAWM'; and the index line 'CARAMEL kolem-' (AHD_watkins1985.txt line 1329). AHD assigns caramel to this root, as Nourai's unpaginated 'AHD' citation claims.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. caramel (KLN_1966.txt line 6492)\", \"stance\": \"partial\", \"note\": \"'caramel, n., burnt sugar. — F., fr. OSp. caramel (now caramelo), a blend of ML. cannamella, \\\"sugar cane\\\", (see cane and melliferous) and Sp. caramillo, \\\"reed\\\", fr. L. calamellus, dimin. of calamus, \\\"reed\\\" (see calamary).' — Latin calamus is only one of two ingredients, and Spanish stands between Latin and French.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, SKT.txt (grep caramel/calamus)\", \"stance\": \"silent\", \"note\": \"no entry for caramel in the Concise Skeat.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic / Pihan / Lokotsch (DEV.txt, PHN.txt, LKT.txt, grep caramel)\", \"stance\": \"silent\", \"note\": \"none of the three dictionaries of French orientalisms treats caramel, so the 'Arabic cannamella' variant is not supported from that side.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"kâramel «کارامل»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian کارامل kārāmel is a 20th-century loan straight from French caramel, taken over through confectionery and chemistry vocabulary (like بیسکویت, شکلات, کاکائو); the Persian spelling with alef in both syllables (کا-را-مل) renders the French [kaʁaˈmɛl] with Persian long ā. Moʿin's Farhang-e Fārsi has the headword «کارامل» with the chemical definition 'ماده‌ای که در حرارت‌های زیاد از ساکارز یا قند معمولی بدست آرند' and a recipe for «کارامل قهوه و شکلات», i.e. it is registered as a modern European technical loan.\",\n          \"derivation_fa\": \"«کارامل» وام‌واژه‌ای است که در سدهٔ چهاردهم خورشیدی یکراست از فرانسویِ caramel، از راه واژگان قنادی و شیمی، وارد فارسی شده است (مانند «بیسکویت»، «شکلات»، «کاکائو»). املای فارسی با دو الف (کا-را-مل) تلفظ فرانسویِ [kaʁaˈmɛl] را با کشیدهٔ فارسی بازمی‌نمایاند. معین در فرهنگ فارسی سرواژهٔ «کارامل» را با تعریف شیمیایی «ماده‌ای که در حرارت‌های زیاد از ساکارز یا قند معمولی بدست آرند» و دستور «کارامل قهوه و شکلات» آورده است؛ یعنی آن را وام‌واژه‌ای نوی اروپایی می‌شناسد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/caramel\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:2796\", \"status\": \"supports\", \"note\": \"Moʿin, Farhang-e Fārsi s.v. کارامل (MON_part2.txt line 17490, between کارافزاینده and کاربر, i.e. the same alphabetical position as the cited p.2796): «کارامل: [caramel] (شیم.) ماده‌ای که در حرارت‌های زیاد از ساکارز یا قند معمولی بدست آرند. کارامل قهوه و شکلات: شیرینیی است …»; the Latin-script etymon in the bracket is garbled in the OCR but the slot is where Moʿin prints the European source-form.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. کارامل\", \"stance\": \"supports\", \"note\": \"see ref_check — entry present with a chemistry label and a Latin-script source form.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur (grep کارامل)\", \"stance\": \"silent\", \"note\": \"not in Aryanpur, which covers only inherited Indo-European Persian words, not modern French loans.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"caramel\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English caramel is first recorded in 1725 as a borrowing of French caramel 'burnt sugar', at first purely as a confectioner's and later a chemist's term ('caramelize' 1837, 'caramel' as a soft candy 1884, as a colour name 1909). The route French → English is uncontroversial; via French it goes back through Spanish/Portuguese caramelo to Late Latin calamellus, diminutive of calamus, which is why Watkins files CARAMEL under the root kolem-.\",\n          \"derivation_fa\": \"انگلیسیِ caramel نخستین‌بار در ۱۷۲۵ ثبت شده و وام‌واژه‌ای از فرانسویِ caramel «شکرِ سوخته» است؛ نخست اصطلاح قنادی و سپس شیمی بوده (caramelize در ۱۸۳۷، معنای «آب‌نباتِ نرم» در ۱۸۸۴، نام رنگ در ۱۹۰۹). مسیر «فرانسه ← انگلیسی» بی‌مناقشه است و از راه فرانسه به اسپانیایی/پرتغالی caramelo و سپس calamellus لاتینیِ متأخر، مصغّرِ calamus، می‌رسد؛ به همین سبب واتکینز CARAMEL را زیر ریشهٔ kolem- آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/caramel\",\n            \"https://en.wiktionary.org/wiki/caramel\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt index line 1329: 'CARAMEL kolem-', and s.v. kolem- '… Greek kalamos … : CALAMITE, CALAMUS, CALUMET, CARAMEL, SHAWM'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. caramel (KLN_1966.txt line 6492; also KLN_1971.txt line 39393)\", \"stance\": \"supports\", \"note\": \"'caramel, n., burnt sugar. — F., fr. OSp. caramel (now caramelo) …' — English from French, as drawn.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, SKT.txt\", \"stance\": \"silent\", \"note\": \"no entry (the Concise Skeat omits caramel).\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century vol. 1 (WEB_vol1.txt)\", \"stance\": \"silent\", \"note\": \"grep for caramel in the OCR of vol. 1 returned no usable entry.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"kalama\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit कलम kalama- m. is a borrowing from Greek κάλαμος, not an Indo-Aryan inheritance (an inherited form would show ś- from *ḱ, as in śroṇi- above, and would not keep the a-vocalism). It reached India in the Hellenistic aftermath of the Indo-Greek contacts, and is attested in two senses that mirror the Greek ones: 'a kind of rice' (the reed-like paddy) and 'reed-pen, writing reed' — Pokorny and Walde-Pokorny give exactly 'ai. kalama- m. \\\"eine Reisart, Schreibrohr\\\"' among the loans from Greek. Nourai's gloss 'pen' covers only the second sense but is correct for it.\",\n          \"derivation_fa\": \"سنسکریت कलम kalama- وام‌واژه‌ای است از یونانی κάλαμος، نه بازماندهٔ ارثیِ هندوآریایی؛ اگر ارثی می‌بود *ḱ آغازی می‌بایست مانند śroṇi- به ś بدل شده باشد و واکهٔ a نیز به این شکل نمی‌ماند. این واژه در پی تماس‌های دورهٔ هلنیستی و یونانیانِ باختری به هند رسیده و در دو معنا گواهی شده که هر دو بازتاب معانی یونانی است: «گونه‌ای برنج» (شالیِ نی‌مانند) و «قلمِ نی». پوکورنی و والده-پوکورنی هر دو عیناً می‌نویسند «ai. kalama- m. \\\"eine Reisart, Schreibrohr\\\"» و آن را در شمار وام‌های یونانی می‌آورند. معنایی که نورایی داده («قلم») تنها یکی از دو معناست، ولی درست است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%CE%BA%CE%AC%CE%BB%CE%B1%CE%BC%CE%BF%CF%82\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:612\", \"status\": \"supports\", \"note\": \"POK_full.txt s.v. Ḱolamo-s (Page(s) 612): 'From gr. κάλαμος are borrowed Old Indie kalama- m. \\\"a kind of rice, writing pipe\\\" and Latin calamus \\\"reed\\\"'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 464\", \"stance\": \"supports\", \"note\": \"'Aus gr. κάλαμος entlehnt sind ai. kalama- m. \\\"eine Reisart, Schreibrohr\\\" (s. Froehde BB. I, 328 f.)'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. kolem-\", \"stance\": \"silent\", \"note\": \"Watkins lists only the Greek, Latin and Germanic members (no Indic loan), since the appendix tracks English etyma.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 18.57 'pen'\", \"stance\": \"partial\", \"note\": \"Buck's 'pen' article gives Grk. κάλαμος > Lat. calamus but does not list the Sanskrit loan.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T21:09:46.965Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-272.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T21:09:51.311Z] TOOL CALL #59: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-272.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 272",
 "description": "Validate and run verify_check"
}
```


### [2026-09-06T21:09:53.263Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'confirmed': 9, 'plausible': 3, 'transcription_suspect': 1, 'unverified': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 11, 'contradicts': 1, 'not_checked': 1, 'not_found': 1}
books consulted: {'supports': 23, 'partial': 5, 'silent': 12, 'contradicts': 2} | by book: {'WLD': 6, 'SYN': 4, 'KLN': 4, 'LAT': 3, 'ARY': 3, 'BRT': 2, 'HUB': 2, 'POK': 2, 'AHD': 2, 'FVQ': 2, 'MON': 2, 'SKT': 2, 'PHD': 1, 'NYB': 1, 'HRN': 1, 'BQT': 1, 'KNT': 1, 'AFM': 1, 'DEV': 1, 'WEB': 1}
```


## [2026-09-06T21:10:13.908Z] AGENT

Done. `data/verification/page-272.json` written; `verify_check.py 272` shows 14/14 nodes, 0 PROBLEM lines.

**PDF page 272 (book p. 242) — 2 chart entries, 9 redirects skipped**

Verdicts: roots 2 confirmed; nodes 9 confirmed, 3 plausible, 1 transcription_suspect, 1 unverified.
Ref checks: 11 supports, 1 contradicts, 1 not_found, 1 not_checked. Books consulted: POK, WLD, AHD/Watkins, SYN (Buck), LAT (Ernout-Meillet), BRT, KNT, PHD, NYB, HRN, HUB, BQT, MON, ARY, FVQ, KLN, SKT, AFM, DEV/PHN/LKT, WEB.

- **transcription_suspect — Klou-ni #4 "Old Persian slaunis"**: there is no Old Persian *slaunis (no initial sl- in OP; absent from Kent). The form is **Old Prussian** *slaunis* 'thigh' (beside Lith. šlaunis), printed as such on the very page Nourai cites (POK 608), and in WLD I 499 and Ernout-Meillet s.v. clunis. I rendered pdf p.272 at 200 dpi: the **book itself prints "Old Persian"** — Nourai's own slip for "Old Prussian". `error_in: book`; the extraction is faithful. Page image saved to `data/verification/sources/refs/ocr/BOOK/272.png`.
- **plausible — Klou-ni #2 Pahlavi "sarŭk"**: real word (Zand of Vd. 8), and Horn no. 737 p.162 prints exactly `phlv. sarūk`, so Nourai copied his source correctly; but that is Horn's 1893 reading — Bartholomae reads `srēnak`, Wiktionary MP `srēnōg`, MacKenzie has no entry.
- **plausible — Kolemos #2 Arabic qalam**: Greek origin confirmed, but Jeffery (FVQ 242-243) shows the route was Greek → Aramaic/Syriac → Geʿez → Arabic, not direct.
- **plausible — Kolemos #5 French caramel**: goes back to calamus, but via Sp./Pt. caramelo < LL calamellus (Wiktionary), with Klein/Etymonline positing a blend with ML cannamella. AHD does file CARAMEL under kolem-.
- **not_found ref**: TAD:57 (al-ʿUnaysī) — leaf 61 is the right ق stretch but the two-column Arabic OCR is scrambled and no scan covers printed p.57 (`ref_page.py TAD:57 --image` refuses). Everything else checked out.

**No extraction errors found** — the JSON matches the printed page throughout, including the empty pass-through box (node #5) and the Persian script/quotes.

Useful side-finding: Aryanpur p.359 (سرین/سرون) cites "برهان قاطع … ۱۱۳۴", independently confirming Nourai's BQT:1134 page number, whose Moʿin footnote gives Av. sraoni-, Skt śroṇi-, Lith. šlaunis, Lat. clunis and Hübschmann's *srainī / *sraunī split.

5 web sources archived via `fetch_source.py` (Wiktionary قلم, κάλαμος, श्रोणि, clunis, caramel; Etymonline caramel).
