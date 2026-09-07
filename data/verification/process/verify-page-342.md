# Verification process log — verify-page-342


## [2026-09-07T17:36:10.741Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 342 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-342.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-342.json. Write /home/sfmqrb/git/rishe/data/verification/page-342.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 342` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T17:36:12.662Z] AGENT

I'll start by reading the instructions and the source files.


## [2026-09-07T17:36:13.286Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T17:36:13.301Z] TOOL RESULT

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


## [2026-09-07T17:36:13.967Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-342.txt"
}
```


### [2026-09-07T17:36:13.983Z] TOOL RESULT

```
1	=== PDF page 342 (book page 312) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Mozgo, Mozgho : marrow  (refs POK:750; KLN:941)
4	#1 (parent #0) [Avestan] refs=POK; KLN; SYN:367 | mazga : marrow
5	  #2 (parent #1) [Pahlavi] refs=BQT:2021 | mazg : brain
6	    #3 (parent #2) [Persian] refs=BQT:2021; SYN:215; MON:4063 | mağz «مغز» : brain ; mazğ «مزغ» : brain
7	#4 (parent #0) [Germanic] refs=None | mazgâ
8	  #5 (parent #4) [English] refs=AHD | marrow
9	--- entry 1 ---
10	ROOT [Indo-European] Mreğu, Mrğu : short  (refs POK:750)
11	#1 (parent #0) [Avestan] refs=POK:750; KLN:188 | merezu, marazu : short ; merezu-jîti : short lived, fast ☞Gwei ; berez 2 : in short time, fast ; berez-čaxra : with fast wheels ☞Kwel
12	#2 (parent #0) [Russian] refs=SYN:969 | borzoy : a fast running wolf hound
13	  #3 (parent #2) [English] refs=KLN:188; AHD:153 | borzoi : a large slender wolf hound
14	#4 (parent #0) [Latin] refs=SYN:969 | brevis : short
15	  #5 (parent #4) [English] refs=None | brief, abbreviate, abridge
16	#6 (parent #0) [Germanic] refs=AHD | murgja : short, a joy which makes time pass faster
17	  #7 (parent #6) [English] refs=None | merry
18	#8 (parent #0) [Greek] refs=AHD | braxus : short ; braxon : upper arm which is shorter than the lower arm
19	  #9 (parent #8) [English] refs=None | brace, embrace, pretzel
20	--- entry 2 ---
21	ROOT Mrğu -> redirect to Mreğu
22	--- entry 3 ---
23	ROOT [Semitic] M.s.h : to touch, rub, anoint  (refs KLN:969)
24	#1 (parent #0) [Arabic] refs=SAP:1569 | masaha : he wiped with hand, covered an area ; Masîh : anointed ; masâhat : area (covered or wiped)
25	  #2 (parent #1) [Persian] refs=FVA:381 | Masîh «مسیح» : the Messiah, Jesus ; masâhat «مساحت» : surface area ; mas-h «مسح» : to wipe with wet hand
26	#3 (parent #0) [Hebrew] refs=KLN:969 | mâšiah : anointed
27	  #4 (parent #3) [Aramaic] refs=None | 
28	    #5 (parent #4) [English] refs=AHD | Messiah : Jesus
29	
```


## [2026-09-07T17:36:14.098Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-342.json"
}
```


### [2026-09-07T17:36:14.109Z] TOOL RESULT

```
1	{
2	  "pdf_page": 342,
3	  "book_page": 312,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Mozgo, Mozgho",
8	        "lang": "Indo-European",
9	        "refs": "POK:750; KLN:941",
10	        "gloss": "marrow"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK; KLN; SYN:367",
18	          "words": [
19	            {"translit": "mazga", "gloss": "marrow", "script": null}
20	          ],
21	          "note": null,
22	          "quote": null
23	        },
24	        {
25	          "id": 2,
26	          "parent": 1,
27	          "lang": "Pahlavi",
28	          "refs": "BQT:2021",
29	          "words": [
30	            {"translit": "mazg", "gloss": "brain", "script": null}
31	          ],
32	          "note": null,
33	          "quote": null
34	        },
35	        {
36	          "id": 3,
37	          "parent": 2,
38	          "lang": "Persian",
39	          "refs": "BQT:2021; SYN:215; MON:4063",
40	          "words": [
41	            {"translit": "mağz", "gloss": "brain", "script": "مغز"},
42	            {"translit": "mazğ", "gloss": "brain", "script": "مزغ"}
43	          ],
44	          "note": null,
45	          "quote": null
46	        },
47	        {
48	          "id": 4,
49	          "parent": 0,
50	          "lang": "Germanic",
51	          "refs": null,
52	          "words": [
53	            {"translit": "mazgâ", "gloss": null, "script": null}
54	          ],
55	          "note": null,
56	          "quote": null
57	        },
58	        {
59	          "id": 5,
60	          "parent": 4,
61	          "lang": "English",
62	          "refs": "AHD",
63	          "words": [
64	            {"translit": "marrow", "gloss": null, "script": null}
65	          ],
66	          "note": null,
67	          "quote": null
68	        }
69	      ]
70	    },
71	    {
72	      "root": {
73	        "name": "Mreğu, Mrğu",
74	        "lang": "Indo-European",
75	        "refs": "POK:750",
76	        "gloss": "short"
77	      },
78	      "nodes": [
79	        {
80	          "id": 1,
81	          "parent": 0,
82	          "lang": "Avestan",
83	          "refs": "POK:750; KLN:188",
84	          "words": [
85	            {"translit": "merezu, marazu", "gloss": "short", "script": null},
86	            {"translit": "merezu-jîti", "gloss": "short lived, fast", "script": null, "see": ["Gwei"]},
87	            {"translit": "berez 2", "gloss": "in short time, fast", "script": null},
88	            {"translit": "berez-čaxra", "gloss": "with fast wheels", "script": null, "see": ["Kwel"]}
89	          ],
90	          "note": null,
91	          "quote": null
92	        },
93	        {
94	          "id": 2,
95	          "parent": 0,
96	          "lang": "Russian",
97	          "refs": "SYN:969",
98	          "words": [
99	            {"translit": "borzoy", "gloss": "a fast running wolf hound", "script": null}
100	          ],
101	          "note": null,
102	          "quote": null
103	        },
104	        {
105	          "id": 3,
106	          "parent": 2,
107	          "lang": "English",
108	          "refs": "KLN:188; AHD:153",
109	          "words": [
110	            {"translit": "borzoi", "gloss": "a large slender wolf hound", "script": null}
111	          ],
112	          "note": null,
113	          "quote": null
114	        },
115	        {
116	          "id": 4,
117	          "parent": 0,
118	          "lang": "Latin",
119	          "refs": "SYN:969",
120	          "words": [
121	            {"translit": "brevis", "gloss": "short", "script": null}
122	          ],
123	          "note": null,
124	          "quote": null
125	        },
126	        {
127	          "id": 5,
128	          "parent": 4,
129	          "lang": "English",
130	          "refs": null,
131	          "words": [
132	            {"translit": "brief, abbreviate, abridge", "gloss": null, "script": null}
133	          ],
134	          "note": null,
135	          "quote": null
136	        },
137	        {
138	          "id": 6,
139	          "parent": 0,
140	          "lang": "Germanic",
141	          "refs": "AHD",
142	          "words": [
143	            {"translit": "murgja", "gloss": "short, a joy which makes time pass faster", "script": null}
144	          ],
145	          "note": null,
146	          "quote": null
147	        },
148	        {
149	          "id": 7,
150	          "parent": 6,
151	          "lang": "English",
152	          "refs": null,
153	          "words": [
154	            {"translit": "merry", "gloss": null, "script": null}
155	          ],
156	          "note": null,
157	          "quote": null
158	        },
159	        {
160	          "id": 8,
161	          "parent": 0,
162	          "lang": "Greek",
163	          "refs": "AHD",
164	          "words": [
165	            {"translit": "braxus", "gloss": "short", "script": null},
166	            {"translit": "braxon", "gloss": "upper arm which is shorter than the lower arm", "script": null}
167	          ],
168	          "note": null,
169	          "quote": null
170	        },
171	        {
172	          "id": 9,
173	          "parent": 8,
174	          "lang": "English",
175	          "refs": null,
176	          "words": [
177	            {"translit": "brace, embrace, pretzel", "gloss": null, "script": null}
178	          ],
179	          "note": null,
180	          "quote": null
181	        }
182	      ]
183	    },
184	    {
185	      "root": {"name": "Mrğu", "redirect": "Mreğu"},
186	      "nodes": []
187	    },
188	    {
189	      "root": {
190	        "name": "M.s.h",
191	        "lang": "Semitic",
192	        "refs": "KLN:969",
193	        "gloss": "to touch, rub, anoint"
194	      },
195	      "nodes": [
196	        {
197	          "id": 1,
198	          "parent": 0,
199	          "lang": "Arabic",
200	          "refs": "SAP:1569",
201	          "words": [
202	            {"translit": "masaha", "gloss": "he wiped with hand, covered an area", "script": null},
203	            {"translit": "Masîh", "gloss": "anointed", "script": null},
204	            {"translit": "masâhat", "gloss": "area (covered or wiped)", "script": null}
205	          ],
206	          "note": null,
207	          "quote": null
208	        },
209	        {
210	          "id": 2,
211	          "parent": 1,
212	          "lang": "Persian",
213	          "refs": "FVA:381",
214	          "words": [
215	            {"translit": "Masîh", "gloss": "the Messiah, Jesus", "script": "مسیح"},
216	            {"translit": "masâhat", "gloss": "surface area", "script": "مساحت"},
217	            {"translit": "mas-h", "gloss": "to wipe with wet hand", "script": "مسح"}
218	          ],
219	          "note": null,
220	          "quote": null
221	        },
222	        {
223	          "id": 3,
224	          "parent": 0,
225	          "lang": "Hebrew",
226	          "refs": "KLN:969",
227	          "words": [
228	            {"translit": "mâšiah", "gloss": "anointed", "script": null}
229	          ],
230	          "note": null,
231	          "quote": null
232	        },
233	        {
234	          "id": 4,
235	          "parent": 3,
236	          "lang": "Aramaic",
237	          "refs": null,
238	          "words": [],
239	          "note": null,
240	          "quote": null
241	        },
242	        {
243	          "id": 5,
244	          "parent": 4,
245	          "lang": "English",
246	          "refs": "AHD",
247	          "words": [
248	            {"translit": "Messiah", "gloss": "Jesus", "script": null}
249	          ],
250	          "note": null,
251	          "quote": null
252	        }
253	      ]
254	    }
255	  ]
256	}
257	
```


## [2026-09-07T17:36:18.207Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md | head -120",
 "description": "Read source matrix"
}
```


### [2026-09-07T17:36:18.247Z] TOOL RESULT

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


## [2026-09-07T17:36:19.810Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SYN','BQT','MON','AHD','SAP','FVA','BRT','HRN','HUB','PHD','NYB','WLD','IEC','ARY','FVQ','AFM','PLA','SKT','WEB','FSD']:\n    if k in d: print(k, json.dumps(d[k],ensure_ascii=False)[:400])\n    else: print(k,'MISSING')\n\""
}
```


### [2026-09-07T17:36:21.119Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_a
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
```


## [2026-09-07T17:36:26.662Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls | head -60; echo ---; python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SYN','AHD','BRT','BQT','MON','PHD','NYB','IEC','WLD','SKT']:\n    e=d[k]; print(k,'| offset:',e.get('page_offset'),'| local:',e.get('local_file'),'| hint:',str(e.get('lookup_hint'))[:200])\n\""
}
```


### [2026-09-07T17:36:27.969Z] TOOL RESULT

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
---
POK | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.i
KLN | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume p
SYN | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed p
AHD | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the 
BRT | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin glos
BQT | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'http
MON | offset: None | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Aves
PHD | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A
NYB | offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
IEC | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
WLD | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, u
SKT | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
```


## [2026-09-07T17:36:31.403Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==407' POK_02.txt | head -80"
}
```


### [2026-09-07T17:36:32.659Z] TOOL RESULT

```
,  a^vuri^Q),  fiuaxog* lJ,Laai,ia  Hes.  (^juvx-cr-xog),  df.ivxQ6g,  dfxvaxQ^gy  dfxvxvög  ,unbefleckt,  rein, heilig';  i^v'^rig,  -rjzog  ^Pilz';
cymr.  mign  (*mükino-)  ,Sumpf' ;  mit  anl.  s-  gael.  smüc,  smug  ,Rotz'  (ex- pressiv) ;  mir.  mocht  ,weich',  cjmr.  mwyth  ds.  {^muk-to-) ;
aisl.  mygla  f.  , Schimmel',  mugga  ,feiner  Regen',  mengl.  mugen  ,nebelig werden',  nhd.  dial.  maugel  ,nebelig,  bewölkt,  dämmerig',  ags.  for-mogod ,verfault';  mit  idg.  g:  aisl.  mykr  und  myki  f.  (*muki)  ,Dünger',  mhd. mucheln,  mücheln  ,schimmelig  riechen',  aisl.  mjükr  (daraus  engl,  meelc) , weich',  ablautend  got.  müka-mödei  , Sanftmut',  mnl.  muik  ,weich',  nhd. dial.  maukig  ,verfault',  Schweiz,  manch  ,morsch,  matt,  hungrig'  (wie Schweiz,  mucht  ,matt,  hungrig');  mhd.  müche  ,Pferdefußkrankheit',  got. *maukö  in  prov.  mauca  ,Gedärm';
lett.  mukls,  muklains  ,paludösus',  müku  (*munku)y  mukt  ,in  einen  Sumpf einsinken' ;
skr.  mukljiv  ,feucht'.
B.  Ai.  *mundktij  muficdti,  mucdti  ,befreit,  läßt  los'  (,*streift  ab'),  mükti- ,Lösung,  Befreiung,  Aufgeben' ;  av./ra-wwaj^i-, Losbinden';  vgl.  3ii.  munthate ,flieht',  apers.  amu{n)d'a  ,er  floh'  aus  *mu-n-eth-mi'^
lit.  munküj  mükti  ,ent wischen'  =  lett.  müku,  mukt  ,sich  losmachen, fliehen'  (und  ,in  einen  Sumpf  einsinken'  s.  oben) ;  lit.  {s)maükti  , gleitend streifen',  lett.  maukt  ,abstreifen',  lit.  (s)munkii,  (s)mükti  ,gleitend  sinken, entgleiten' ;
slav.  *(s)m^kngt^  ,(ent) gleiten'  in  öech.  smeknouti  ,abziehen',  aksl.  Refl. smySg,  smykati  se  , kriechen'  (modern  slav.  auch  ,schlüpfen,  gleiten,  abstrei- fen'), russ.-ksl.   mzknuti  sja  ,transire',   aksl.   m^cati  (nizke-)  ,]actare',  usw.
745
Eine  Wurzelf.  meukh-  mit  der  spez.  Bed.  .hineinsclilüpfen^  wohl  in  arm. nixem  (*miLxam)  ,stecke  hinein,  tauche  ein^  bade^;,  mux  ^tinctura'^^  mxim enrare,  insinuarsi,  ingolfarsi^,  zunächst  zu  gr.  ^v^öq  m.  ^innerster  Winkel* (etwa  ,*SchlupfwinkeP);,  l^vx^oq  ^innerst^
p^xxi  {s)meugh-  beruht  die  germ.  Sippe  von:
aisl.  smjüga  ^hinein-  oder  durchkriechen'^  ags.  smügan  ^schlüpfen, kriechen'^  mhd.  smiegen  ^sich  ducken',  nhd.  schmiegen^  Kaus.  aisl.  smeygia schmiegen,  anziehen',  mhd.  sich  smougen  ,sich  ducken*,  ags.  smeag  ,klug, scharfsinnig',  smeagan  , denken,  suchen',  smeagol  ,eng,  schmal',  aisl.  smuga f. , Schlupf  loch',  ferner  schwed.  i  mjugg,  norw.  i  mugg  ,verstohlenVuiit  s- dän.  norw.  i  smug,  ndl.  ter  smuig  (und
```


## [2026-09-07T17:36:32.886Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"mozgo\\|mozg-\\|mreghu\\|mreĝhu\\|mreǵhu\\|mṛĝhu\" POK_full.txt | head -30"
}
```


### [2026-09-07T17:36:32.964Z] TOOL RESULT

```
61447:Swedish misergher. Church Slavic mozg-b " brain ', mozdan-b ( *mozgeni>), Akk. PI. 
61560:Root / lemma: mreghu- m/ghu-
```


## [2026-09-07T17:36:36.527Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '61400,61620p' POK_full.txt"
}
```


### [2026-09-07T17:36:36.581Z] TOOL RESULT

```
furmicula : Catalan formiga : Dzoratai fremi; froumi : Furlan furmie : Galician formiga : 
Greek Muppn^ '■ Greek puppnyKi : ( > alb. merimanga, miremanga, milimanga, merimajka^ 
spider') = Griko Salentino mermico : Latin formica : Leonese formiga : Lombardo 
Occidentale formiga : Napulitano furmfcula : Portuguese formiga : Reggiano : furmiga; 
furmia : Romagnolo furmiga : Romanian furnica : Romansh furmicia : Sardinian 
Campidanesu fromiga : Sicilian fummicula : Valencian formiga : Venetian formiga; 
formigola : Viestano furmich' : Wallon furmi : Zeneize formigoa ' ant'. 

In uorm-, gr. puppa^, popija^ Hes. (p- Schriftbehelf for F, compare also 6piJiKa(; MUPMH^ 
Hes.); Old Indie valmTka- m. ' ant heap '; besides with totally single sound result vamra-vn., 
vamni. ' ant '. 

Auf mouro-: 0\d Icelandic maurr, besides *meur-\n Danish myre, Swedish myra 
{*meuridn-). Middle Dutch PI. mure {once covered) miere. Modern Dutch mier. Middle Low 
German m/re {to /~s. van Wijk), Middle English m/'re, /t?//*© (Scandinavian loanword), Old 
English myre, engl. m/'re, nowadays only still p/s-m/re {vom Ausspritzen ihrer Saure), 
Crimean Gothic miera. 

References: WP. II 306 f., WH. I 531 f., Trautmann 170, Specht Indo Germanic Dekl. 45. 
Page(s): 749 

Root / lemma: mo[u]-lo- : mu-lo- 

Meaning: root, plant 

Note: as "mouth of the plant' to mu-S. 751. 

Material: Old Indie mula-n. 'root', mula-karman-n. "sorcery with roots'; 

gr. iJwAu "ein fabelhaftes Wunderkraut (Hom.); gelbbluhende Knoblauchart (Theophr. 
Dioscor.)', iJcbAu^a ' Knoblauchart '. 

References: WP. II 303, 310, Wackernagel Sitz.-Ber. Pr. Akad. 1918, 410 f. 
Page(s): 750 

Root / lemma: moz-g-o-, moz-g-en-, mos-k-o- 



Meaning: brain 

Material: Old Indie majjan, majja, majjas-^ marrow ', mastfska-^ brain ', mastaka-^heaA, 

cranium'; Avestan mazga- " marrow, brain '; Old High German mar(a)g, mar(a)k. Old 

Saxon marg. Old English mearg. Old Icelandic mergr{Gen. mergjar) ' marrow ', Old 

Swedish misergher. Church Slavic mozg-b " brain ', mozdan-b ( *mozgeni>), Akk. PI. 

mozdeni' marrow ', Old Prussian musgeno' marrow ', wherefore (with metathesis from 

* mazgenes) Lithuanian f. PI. smagenes, Latvian smadenes^ brain '; Tocharian A massunt 

" marrow '. 

References: WP. II 309, Trautmann 172 f., Specht Indo Germanic Dekl. 78 f. 

Page(s): 750 

Root / lemma: mozgho-s 

Meaning: young bull 

Note: only Armenian and gr. 

Material: Armenian /770z/"young rother, cattle, calf = gr. poaxiov, Demin. to mocjxo(; m. 

"young bull, calf, f. 'young cow, girl'; probably identical with M6axo(; ' Pflanzentrieb , sprout 

References: WP. II 309. 
Page(s): 750 

Root / lemma: mod- : mad-ox mad- : mad- 

Meaning: to meet, approach 

Material: Armenian matcim " approach, come near to, draw near ', Aor. mateay, 

matucanem ' make accessible ' {maut^ near ' after Pedersen with Armenian u- 

Epenthese); 

Old Icelandic motn. " encounter, gathering, assembly, meeting, convention, public 
congregation, meeting'. Old English (ge)mdt. Old Saxon mot. Middle High German muoz 
ds., Gothic ga-motjan. Old Icelandic m0ta. Old Saxon motian. Old English metan, engl. 
/77ee/"meet'; on Indo Germanic */77e/fl7-//c»-/77 based Gothic mat^r forum, place of 
assembly, market ', Old English mseder council, assembly, discourse ' and (as *madla-) 
Old English maer discourse, fighf , Middle Low German /77^/"congregation, meeting'. Old 
Saxon Old High German mahalu. " Gerichtsstatte, court, pact, covenant' (Modern High 
German Mahlstatt}, Old Icelandic maT Sprechvermogen, discourse, negotiation, legal 
matter'. Middle Latin (Germanic) mallum, mallus^ Gerichtsstatte, judicial appointment ', 
whereof Gothic maNJan, Old English madelian, m^d/an and maelan. Old High German 
mahelen. Old Icelandic msela^iaWC and (from the public promise) Old High German gi- 



mahalo' husband, consort, partner, bridegroom ', gi-mahala^ wife, bride'. Modern Higli 
German vermahlen. 

References: WP. II 304 f., Feist3 349 f. 
Page(s): 746-747 

Root / lemma: md[u]-ro- : mu-ro- 

Meaning: stupid, crazy 

Material: Old Indie mura-^ mindless, dull, stupid'; gr. Mwp6(;, Attic pu)po(; 'stupid, crazy' 

(out of it Latin /770/z/s "foolish, loony, clownish '). 

References: WP. II 303, WH. 11114. 

Page(s): 750 

Root / lemma: mo-, mo-lo- 

Meaning: to strain oneself 

Material: Gr. [j(I)Ao(; " exertion, toil', pooAsu), Cretan iJCjoAioo " litigate ', pwAut; " exhausted ', 

perhaps poAiq "barely' (o for u) after iJoyiq); a-jJOToq " fatigueless '; Latin molesi. " mass 

(huge); bulk; monster; massive structure; difficulty] trouble] danger', Denom. molior, -TrV 

struggle! labor] labor at; construct] build; undertake] set in motion] plan ', molestus^ 

annoying; troublesome; tiresome ' (analogy to modestus); Gothic af-mauiPs^ fatigued'. Old 

High German muoan. Middle High German muen, muejen' frighten, grouch', Dutch 

/77c>eye/7 "bother, annoy, make an effort, try hard, exert oneself; Old High German muodi. 

Old Saxon modi^ tired ', Old English mede^ tired, grieving ', Old Icelandic modr^ tired '; 

Lithuanian yO/7-s/-/77^c»/e//" labor'; russ. maj-u, -5/i. "exhaust, plague', maja, majeta 'p\ague, 

hard exertion ', etc. 

References: WP. II 301 f., WH. II 101 f., Trautmann 188; 

See also: probably to me-5. 

Page(s): 746 

Root / lemma: mregh-m(n)o- 

Meaning: brain 

Material: Gr. pp£x|j6(;, ppsxMQ n. (and ppsYpa) "Vorderkopf, Oberschadel', Old English 

bregen, brsegenu. " brain ' (engl. brain). Old Frisian brein. Middle Low German bragen, 

bregen. Modern High German Bragen xw. ds. 

References: WP. II 314. 

Page(s): 750 



Root / lemma: mreghu- m/ghu- 
Meaning: short 



Material: Prakr. muhu-, Avestan marazu-jTti-, -jva-^ (3paxupiO(; ', sogd. murzak^shox{'\ 
Maybe alb. murr/z'haw, hawthorn, thorn-apple, brier, whitethorn, short shrub' : sogd. 
murzak' short'. 

gr. ppaxu(; 'short', ppaxsa " shallow place '; in addition ppaxiwv ' upper arm ', 
comparative besides ppaaawv; 

Latin brevis (at first from Fem. *bre(x)uf) 'short', bruma ' the winter solstice, winter, 
coldness' ( *brevi-ma, *breu-ma "time of short days'); 

Maybe alb. i6'/y/r7a'hoar, rime, frost, hoarfrost' a Latin loanword. 

Goth\c gamaurgjan ^ shorten'. Old High German murgf/)' short', murgfar/lraW, 
breakable'. Old English /t?//^© 'pleasant', engl. merry. 

References: WP. II 314, WH. 1115. 
Page(s): 750-751 

Root / lemma: mrk- 
Meaning: edible root, carrot 

Material: Gr. ppoKova "wild vegetables ' Hes.; Old High German morCaJha 'Daucus carota', 
Modern High German Mohr-rube, Mohre, Old English more, moru6s.. Late Old High 
German Demin. morh/7a' morel' (mushroom similar to carrots); against it seems russ. 
morkovb, morkva ' carrot', serb. mrkva has been borrowed from Germanic. 
References: WP. II 313. 
Page(s): 750 

Root / lemma: mut-o-s 

Meaning: circumcised 

Material: Latin mutilus, /77i///o'i/s "mutilated', *muticus^ truncated, chopped down, cut down, 

cut off, circumcised ', muto, mutfd'pen\s', GN Mutunus, rom. mutt-^ dull '; Irish mut, gael. 

mutacb' short' (with expressive //); perhaps also Irish /770//7 "penis' as " stub'. 

References: WP. II 312, WH. II 136 f.; after E. Lewy rather to Latin mutusS. 751 , compare 
" dumb ': " mutilate '. 
Page(s): 753 



Root / lemma: muk- 
Meaning: heap, etc.. 

Material: Gr. jjukoov awpoq GniJcbv Hes.; proto gall. *mukina ' cairn, pile of stones set up as 
a memorial or mark of some kind ' (Jokl V. Rom. 8, 193); Old Icelandic mugi, mugr^heap, 
bulk, mass'. Old English mugam. "(corn, grain-) heap', muha ds. (also muwa), compare 
further Swedish dial, moa^ pile up, collect, accumulate' {*mOhdn), Old High German mO- 
werf^ mole ', with -k(k)-. Middle Low German muke, Dutch muik Middle High German 
mOche, Modern High German (half Low German) Maukei., Bavarian (genuine High 
German) Mauche^ Auswuchs, Fuftgeschwulst der Pferde ', Swiss mauchm. ' Auswuchs 
an Rebholz, unordentlicher Haufe ' and with if. Norwegian dial, mukka^heap, bulk, mass'. 
Middle High German mockem. 'clump, gobbet ' (with it identical is Middle High German
```


## [2026-09-07T17:37:01.676Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN marrow/borzoi/messiah ===\"; grep -n \"^borzoi\\|^marrow\\|^Messiah\\|^messiah\\|^merry,\\|^brief,\\|^brace,\\|^pretzel\\|^embrace\\|^abbreviate\\|^abridge\\|^brachium\\|^brevity\" KLN_1966.txt | head -30"
}
```


### [2026-09-07T17:37:01.753Z] TOOL RESULT

```
=== KLN marrow/borzoi/messiah ===
5387:borzoi,  n.,  the  Russian  wolfhound.  —  Russ. borzoy,  lit.  ‘quick,  swift’,  rel.  to  Czech  brzy, Serbo-Croat,  brzo,  ‘quickly’,  and  cogn.  with Lith.  bruzdeti,  bruzgeti,  ‘to  hurry’,  burzdus, ‘mobile,  agile’,  and  cogn.  with  the  first  element in  Avestic  berez-cachra,  ‘having  fast-moving wheels’.
5487:brace,  n.,  clasp,  buckle.  —  ME.  brace,  fr.  OF. brace,  brasse,  ‘the  two  arms'  (whence  F.  brasse, ‘fathom,  armful’),  fr.  L.  brachia,  ‘the  arms’,  pi. (of  the  neut.  noun  brachium)  mistaken  for  a  fern, sing,  noun,  fr.  Gk.  (ipiytcov,  ‘arm’,  which  de¬ rives  fr.  [ipayup,  ‘short’,  and  prop,  means  ‘that which  is  shorter  (than  the  forearm)’.  See  brachy- and  cp.  bracelet,  brachial,  brassard,  braza,  em¬ brace,  bretzel,  and  the  second  element  in  vam- brace.
5488:brace,  tr.  v.,  to  encompass.  —  ME.,  fr.  OF.  bra- cier,  'to  embrace’,  fr.  brace,  ‘the  two  arms'.  See brace,  ‘clasp’.
5637:brief,  adj.,  short  in  duration.  —  ME.  bref,  fr.
5644:brief,  n.,  a  summary.  —  ME.  bref,  fr.  OF.  (=  F.) bref, |  fr.  ML.  breve,  prop.  neut.  of  L.  adj.  brevis, ‘short’,  used  in  the  sense  of  ‘short  writing,  letter, document’.  Cp.  It.  breve,  of  s.m.,  G.  Brief  ‘let¬ ter’.  See  brief,  adj.,  and  cp.  breve.
12944:embracer,  n.,  one  who  embraces.  —  Formed  fr. prec.  word  with  agential  suff.  -er.
12945:embracer,  also  embraceor,  n.,  one  who  attempts to  corrupt  a  jury  (law).  —  OF.  embraseor,  em¬ braces,  ‘instigator,  corrupter’,  fr.  embraser,  ‘to set  on  fire,  instigate’,  fr.  em-  and  breze  (F. braise),  ‘wood  embers,  live  coals’.  See  braze, ‘to  solder’,  and  cp.  embrasure, embracery,  n.,  the  attempt  to  corrupt  a  jury  (law).
22950:marrow
22984:marrow,  n.  —  ME.  maro,  merowe,  fr.  OE.  mearg, mearh,  rel.  to  OS.  marg,  ON.  mergr,  OFris.,  Du. merg,  OHG.  marag,  marg,  MHG.  marc,  G. Mark,  ‘marrow’,  fr.  I.-E.  base  *mozghu-, whence  also  OI.  majjdn-,  Avestic  mazga-,  mar¬ row’,  Toch.  A  mdssunt,  ‘marrow’,  OSlav. mozgu,  OPruss.  muzgeno,  Lith.  smagenes (metathesized  fr.  "mdzgenes),  ‘brain’.
23587:merry,  n.,  the  wild  black  cherry.  —  F.  merise,  for *amerise,  a  blend  of  amer,  ‘bitter’  (fr.  L.  ama- rus),  and  cerise,  ‘cherry’  (fr.  VL.  *ceresia);  see amarine  and  cherry.  The  a  in  *amerise  was  mis¬ taken  for  part  of  the  article  ( I’amerise  was  mis- divided  into  la  merise)  and  was  dropped  accord¬ ingly.  The  s  of  F.  merise  was  mistaken  for  the plural  suffix  and  so  F.  merise  became  merry  in English.  Cp.  E.  cherry  (fr.  F.  cerise).
23654:Messiah,  n.  —  Aram,  rr^shiha,  ‘the  anointed  ,  fr. Heb.  mashtah,  ‘anointed’,  fr.  mashdh,  ‘he  anoint¬ ed’,  whence  mishhdh,  ‘ointment;  consecrated portion’ ;  rel.  to  Aram. -Syr.  m6shah,  ‘he  anoint¬ ed’,  mishah,  mishhdh,  Syr.  meshhd,  ‘oil’,  Ethiop. masdha,  ‘he  anointed;  he  feasted’,  Akkad. masha'u,  ‘to  spread  (oil)  over’,  Arab,  masaha, ‘he  stroke  or  wiped  with  the  hand’.  Cp.  Messias. Derivatives:  Messiah-ship,  n.,  Messi-an-ic,  adj. Messias,  n.,  the  Messiah.  —  Late  L.,  fr.  Gk.  Mea- olag,  fr.  Aram,  nfshihd,  ‘the  anointed’.  See Messiah.
```


## [2026-09-07T17:37:03.028Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD mozg/mregh ===\"; grep -n -i \"mozg\\|mregh\\|mṛghu\\|marrow\\|borzoi\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-07T17:37:03.083Z] TOOL RESULT

```
=== AHD mozg/mregh ===
153:Internal organs were also named in Indo- European times, including the womb (g“elbh-), gall (ghel-?), brain (mregh-mno-, confined to Low German and Greek), spleen (spelgh-), and liver (yekr). The male sexual organs, pes- and ergh-, are common patri- mony, as is ors-, “backside.”
758:mergh-. To wet, sprinkle, rain. Variant form *mregh- in Greek brekhein, to wet: EMBROCATE. [Pok. meregh- 738.]
762:mizdho-. Reward. West Germanic *médé- in Old English méd, reward, compensation, meed: MEED. [Pok. mizdho- 746. m6-. To exert oneself. Suffixed form *mé-I- in: a. Latin molés, heavy bulk, mass, massive structure: MOLE%, MOLECULE; DEMOLISH; b. Latin molestus (irregularly from mdélés), labored, difficult, troublesome: MOLEST. [Pok. m6- 746.] m6d-. To meet, assemble. 1. Germanic *mdtjan in Old English métan, to meet: MEET!. 2. Germanic *méta- in Old English mot, gemét (ge-, together; see kom), meet- ing, moot, assembly, council: MOOT; FOLKMOTE, GEMOT, WITENAGEMOT. 3. Perhaps suffixed zero-grade form *mod-tlo- in Germanic *mathla- in Old Norse mdl, speech, agreement (> Norwegian mdi, speech): MAIL; (BLACKMAIL), RIKSMAL. [Pok. mdd- 746.] modhro-. A color. Germanic *madraz in Old English meedere, madder: MADDER!. [Pok. modhro- 747.] molko-. Skin bag. Germanic *malhé- in Old High Ger- man malha, pouch, bag, akin to the Germanic source of Old French male, bag: Matti. [Pok. molko- 747.] mone. Neck, nape of the neck. 1. Germanic *man6 in Old English manu, mane: MANE. 2. Latin monile, necklace: MONILIFORM. [Pok. mono- 747.] mori-. Body of water; lake (?), sea (?). 1. Germanic *mari- in: a. Old English mere (> Middle English mere), sea, lake, pond: MERE?; (MERMAID); b. Old Norse marr, sea, akin to the Scandinavian source of MARRAM; C. Old High German mari (> German Meer), sea: MEER- SCHAUM. 2. Germanic *mariska-, water-logged land, in: a. Old English mersc, merisc, marsh: MARSH; b. Old French marasc, maresc, marsh: MORASS. 3. Latin mare (> French mer), sea: MARE?, (MARINARA), MARINE, MARI- TIME; BECHE-DE-MER, MARICOLOUS, MARICULTURE, OR- MER, ULTRAMARINE. [Pok. mori 748.] mormor-. Also murmur-. Murmur. Imitative root. Latin murmur, a murmur: MURMUR. [Pok. mormor- 748.] moro-. Blackberry, mulberry. 1. Greek moron, mulberry, in sukomoros, an African fig tree: SYCAMORE. 2. Latin morum, mulberry (probably from Greek): MORULA, MUR- REY; MULBERRY. [Pok. moro- 749.] morwi-. Ant. 1. Germanic variant form *meur- in Danish myre, ant, akin to the Scandinavian source of Middle English mire, ant: PISMIRE. 2. Variant form *morm- in: a. Greek murméx, ant: MYRMECO-; b. (with dissimila- tion) Latin formica, ant: FORMIC, FORMICARY; FORMICI- vorous. [Pok. morui- 749.] m6(u)lo-. Name of a plant. Greek mélu, moly: MOLY. [Pok. mé(u)-lo- 750.] m6(u)ro-. Foolish. Greek méros, foolish: MORON; OXYMO- RON. [Pok. mé(u)ro- 750.] mozgo-. Marrow. Germanic *mazg6- in Old English mezrg, mzerh, marrow: MARROW. [Pok. moz-g-o- 750.] mregh-m(n)o-. Brain. 1. Germanic *brag-na- in Old English bregen, brain: BRAIN. 2. Greek bregma, the front part of the head: BREGMA. [Pok. mregh-m(n)o- 750.] mregh-u-. Short. I. Suffixed form *mregh-w-i- in Latin brevis, short (> briima, the shortest day, winter): BRIEF, BRUMAL; ABBREVIATE, (ABRIDGE). II. Zero-grade form *“mrghu-. 1.Germanic *murgja-, short, also pleasant, joyful, in: a. Old English myrge, mirige, pleasant: MERRY; b. Germanic *murgithd, pleasantness, in Old English myrgth, pleasure, joy: MIRTH. 2. Greek brakhus, short: BRACHY-; AMPHIBRACH, TRIBRACH. 3. Greek com- parative brakhion, shorter, hence also “upper arm” (as opposed to the longer forearm): BRACE, BRACERO, BRA- CHIUM, BRASSARD, BRASSIERE, PRETZEL; EMBRACE. [Pok. mreghu- 750.] mu'-. Imitative of inarticulate sounds. 1. Reduplicated form in Germanic *mum- in: a. Middle Low German mummen, to be silent, akin to Middle English mum, silent: MUM}; b. Icelandic mumpa, to eat greedily, akin to the probable Scandinavian source of dialectal English mump, to mumble, grimace: MUMPs; c. Low German
961:(s)mer-3. Grease, fat. 1. Suffixed form *smer-wo- in Germanic *smerwa-, grease, fat, in Old High German smero, fat (> German Schmiere, grease): SCHMEER. 2. Germanic denominative verb *smerwjan, to spread grease on, in: a. Old English smierwan, smerian, to smear: SMEAR; b. Old High German smirwen, smerian (> German schmieren), to apply salve, smear: SMEAR- CASE. 3. Latin medulla (perhaps < *merulla, influenced by medius, middle), marrow: MEDULLA. [Pok. smeru- 970.
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1239:AMITY amma AMMUNITION mei-3 AMNESIA men-! AMNESTY men-1 AMNIOCENTESIS kent- AMOEBA mel-1 AMONG mag- AMORETTO amma AMORTIZE mer-2 AMOUNT ad-, men-2 AMOUR amma AMPHI- ambhi AMPHIBIOUS gWei- AMPHIBOLE gWelg-1 AMPHIBRACH mregh-u- AMPHIMACER mak- AMPHIMIXIS meik- AMPHIOXUS ak- AMPHISBAENA gWa- AMPHISTYLAR sta- AMPHITHECIUM dhé-1 AMPHORA bher-1 AMPHOTERIC ambho AMPHYCTYONY  tkei- AMPLEXICAUL kaul-, plek- AMPLIFY dhé-1 AMPUTATE peu- AMRITA mer-2, ne AMYLUM mele- AN! oi-no-
1320:BRACE mregh-u- BRACERO mregh-u- BRACH bhrag- BRACHIUM mregh-u- BRACHY- mregh-u- BRACKEN bhreg- BRACKET brak- BRAD _bhar- BRADYLEXIA leg-1 BRAE bherek- BRAHMA! bhiagh-men- BRAHMAN bhiagh-men- BRAHMIN bhlagh-men- BRAID bherok- BRAIL  brak-
1321:BRAIN mregh-m(n)o- BRAISE bhreu-2 BRAKES bhreg- BRAKE‘ bhreg- BRAMBLE bhrem-2 BRAND gWher- BRANDISH gWher- BRANDY gWher- BRASS ferrum BRASSARD mregh-u- BRASSIERE mregh-u- BRATWURST bhreu-2 BRAWN bhreu-2 BRAY? bhreg- BRAZE? bhreu-2 BRAZEN ferrum BRAZIER! ferrum BRAZIER? bhreu-2 BREACH bhreg- BREAD bhreu-2 BREAK bhreg- BREAKFAST past- BREAM! bherak- BREAST bhreus-1 BREATH gWhré- BREATHE gWhré- BRECCIA bhreg- BREECH brak- BREED bhreu-2
1323:BREEKS brak- BREEZE bhreu-2 BREGMA mregh-m(n)o- BREMSSTRAHLUNG | ster-2 BREW bhreu-2 BREWIS bhreu-2 BRIAR! wer-3 BRIDE? bherek- BRIDEGROOM dhghem- BRIDGE! bhri- BRIDLE bherek- BRIEF mregh-u- BRIGHT bherag- BRIM bhrem-2 BRIMSTONE gWher- BRINDLED gWher- BRING bher-!
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1454:ELUANT leu(@)- ELUCIDATE leuk- ELUDE leid- ELUTE leu(a)- ELUVIUM leu(a)- ELYTRON wel-3 EMACIATE mak- EMANATE ma-3 EMANCIPATE man-2 EMASCULATE mas EMBASSAGE ag- EMBASSY ag- EMBELLISH deu-2 EMBER eUS- EMBER DAY ambhi, rei-3 EMBLEM gWele-1 EMBLEMENTS bhel-3 EMBOUCHURE beu-! EMBRACE mregh-u- EMBROCATE mergh- EMEND mend- EMERGE mezg-! EMERITUS (s)mer-2 EMESIS weme- EMETIC weme- EMIGRATE mei-! EMINENT men-2 EMIT (s)meit(9)- EMMET mai-1 EMOLLIENT mel-1 EMOTION meue- EMPEROR pere-! EMPHASIS bha-' EMPHYSEMA pu-! EMPIRIC per-4 EMPLOY plek- EMPORIUM per-2 EMPRISE ghend- EMPTY med- EMPYEMA pu-2 EMPYREAL pil- EMULSION melg- EMUNCTORY meug-2 EN-! en
1819:MARK2 merg- MARKET merk-2 MARKKA merg- MARLINE mer-3 MARMALADE melit-, mélon MARQUEE merg- MARQUETRY merg- MARQUIS merg- MARQUISE merg- MARRAM_ mori- MARROW mozgo- MARRY! = mari-
1853:MERO- (s)mer-2 -MEROUS (s)mer-2 MERRY mregh-u- MESENTERY en
1875:MIR mei-4 MIRACLE smei- MIRAGE smei- MIRE meu- MIRROR smei- MIRTH mregh-u- MIs-1_ mei-1, mei-2 MISADVENTURE gWa- MISANTHROPE ner-2 MISCEGENATION gene-, meik- MISCELLANEOUS meik- MISCHIEF kaput MISCIBLE meik- MISCREANT kerd-1 MISER miser MISERABLE miser MISERICORD kerd-1 MISERY miser MISFEASANCE dhé-1 MISHAP kob- MISNOMER nd-men- MISONEISM newo- MISPRISION ghend-, mei-1 MIss! mei-1 MISSEL THRUSH meigh- MISSILE (s)meit(9)- MISSION (s)meit(a)- MISSIVE (s)meit(e)- MIST meigh- MISTAKE mei-1 MISTER meg- MISTLETOE meigh- MISTRAL meg- MISTRESS meg- MITE! = mai-1
2129:PRECINCT kenk-! PRECIOUS per-6 PRECIPITATE kaput PRECISE kae-id- PRECLUDE kleu-3 PRECOCIOUS pekw- PRECURSOR kers-2 PREDATORY ghend- PREDECESSOR ked- PREDICATE delk- pRepicT deik- PREDOMINATE deme-1 PREEMPTION em- PREFACE bha-2 PREFECT dhé-1 PREFER bher-1 PREFIGURE dheigh- PREFIX dhig¥- PREGNABLE ghend- PREGNANT! gene- PREGNANT? per-5 PREHENSILE ghend- PREHENSION ghend- PREJUDICE deik-, yewes- PRELAPSARIAN leb-1 PRELATE telo- PRELECT leg-1 PRELIBATION [éi- PRELUDE leld- PREMATURE ma-1 PREMIER per! PREMISE (s)meit(@)- PREMIUM em- PREMONITION men-1 PREMORSE mer-2 PREMUNITION mel-3 PREPARE pere-! PREPENSE (s)pen- PREPONDERATE (S)pen- PREPOSITION apo- PREPOSTEROUS apo- PREPOTENT _poti- PREPUCE pu-! PREROGATIVE reg-1 PRESAGE sag- PRESBYOPIA per! PRESBYTER pert PRESCIENT skel- PRESCIND  skel- PRESCRIBE skribh- PRESENT! es- PRESENT? es- PRESENTIMENT sent- PRESERVE ser-! PRESIDE sed-! PRESS! per-5 PRESSURE per-5 PRESTIGE streig- PRESUME em- PRETEND ten- PRETERIT el-1!, per? PRETERMIT (s)melt(@)- PRETEXT teks- PRETZEL mregh-u- PREVAIL wal- PREVENIENT gWa- PREVENT gWa- PREVIOUS wegh- PREVISE weld- PREY ghend- PRICE per-6
2358:TERRAQUEOUS ters- THREE trei- TORRID ters- TRIBRACH mregh-u-
```


## [2026-09-07T17:37:10.652Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport bisect\n# compute leaf per line\nleaf=0; res={}\ntargets={5387:'borzoi',5487:'brace',22984:'marrow',23654:'Messiah',23587:'merry-n'}\nfor i,l in enumerate(lines,1):\n    if i in targets: print(targets[i], 'line',i,'leaf',leaf,'-> approx printed p', (leaf-12)*2, 'or', (leaf-12)*2+1)\n    leaf+=l.count('\\f')\nEOF"
}
```


## [2026-09-07T17:37:11.875Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"merry,  adj\\|^merry,\\|mirth,\\|^bretzel\\|^pretzel\\|^brachy-\\|^brevity\\|^abbreviate\\|^abridge\" KLN_1966.txt | head"
}
```


### [2026-09-07T17:37:12.059Z] TOOL RESULT

```
borzoi line 5387 leaf 110 -> approx printed p 196 or 197
brace line 5487 leaf 113 -> approx printed p 202 or 203
marrow line 22984 leaf 505 -> approx printed p 986 or 987
merry-n line 23587 leaf 519 -> approx printed p 1014 or 1015
Messiah line 23654 leaf 520 -> approx printed p 1016 or 1017
```


### [2026-09-07T17:37:12.113Z] TOOL RESULT

```
13818:Euphrosyne,  n..  i)  one  of  the  three  Graces  (Greek mvthol.);  2)  fern.  PN.  —  L.,  fr.  Gk.  Eutppoouvr,, lit.  ‘mirth,  merriment',  fr.  euippcov,  ‘cheerful, merry',  lit.  ‘of  a  good  mind’,  fr.  eu  (see  eu-)  and 9pv;v,  gen.  9pevo c,  ‘mind’.  See  phrenetic  and  cp. Sophronia.  Cp.  also  prec.  word.
16250:glee,  n.,  joy;  mirth.  —  ME.  gle,  gleo ,  fr.  OE. gliw,  gleo,  ‘mirth,  jest;  music  minstrelsy’,  fr. ON.  gly,  of  s.m.,  which  is  rel.  to  glja,  ‘to  shine’. See  gleam  and  cp.  words  there  referred  to. Derivatives:  glee-ful,  adj.,  glee-ful-ly,  adv., glee-ful-ness,  n.
23585:Derivative:  Merovingian,  n. merry,  adj.,  gay.  — -  ME.  merie,  murie,  fr.  OE. myrge ,  myrige,  myrig,  mirig,  ‘pleasing,  delight¬ ful,  merry',  orig.  ‘that  which  makes  the  time short’;  rel.  to  OHG.  murg,  murgi,  ‘short’,  Goth.
23587:merry,  n.,  the  wild  black  cherry.  —  F.  merise,  for *amerise,  a  blend  of  amer,  ‘bitter’  (fr.  L.  ama- rus),  and  cerise,  ‘cherry’  (fr.  VL.  *ceresia);  see amarine  and  cherry.  The  a  in  *amerise  was  mis¬ taken  for  part  of  the  article  ( I’amerise  was  mis- divided  into  la  merise)  and  was  dropped  accord¬ ingly.  The  s  of  F.  merise  was  mistaken  for  the plural  suffix  and  so  F.  merise  became  merry  in English.  Cp.  E.  cherry  (fr.  F.  cerise).
24014:mirror,  n.  —  ME.  mirour,  fr.  OF.  mireor,  mire- oar,  mirour  (F.  miroir),  fr.  VL.  mirare,  ‘to  look at’,  fr.  L.  mirari,  'to  wonder  at’.  See  miracle. Derivatives:  mirror,  tr.  v.,  mirror-y,  adj. mirth,  n.  —  ME.  myrthe,  fr.  OE.  myrigd,  mirigd, mirgd,  ‘pleasure,  joy’,  formed  with  suff.  -d  fr. myrige,  myrig,  mirig,  ‘pleasing,  delightful, merry’.  See  merry  and  subst.  suff.  -th. Derivatives:  mirth-ful,  adj.,  mirth-ful-ly,  adv., mirth-ful-ness,  n.,  mirth-less,  adj.,  mirth-less-ly, gHv  mirth-lpxx-neSX.  n.
```


## [2026-09-07T17:37:24.728Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (104,105,106,109,110,111,504,505,519,520):\n    p=pages[i]\n    import re\n    nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', p)\n    print(i, 'nums:',nums[:6], '| first:', p.strip()[:90].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T17:37:26.132Z] TOOL RESULT

```
104 nums: ['176'] | first: is  and torque).  The  plant  was  so  called  from  its  twisted root. bistoury,  n.,  a 
105 nums: [] | first: ‘white  horse’,  fr.  I.-E.  base *bhleg-,  ‘to  shine,  gleam’.  See  black  and  cp. bla
106 nums: ['180', '181'] | first: erred  to.  Cp.  also  blenny. blennorrhea,  blennorrhoea,  n.,  excessive  discharge of  
109 nums: ['186', '187'] | first: ME.  bond,  a var.  of  band.  See  band,  ‘a  tie’,  and  cp.  the  first element  in  bo
110 nums: [] | first: .  bordage,  border,  bordure.  Cp. also  prec.  word. Derivatives:  border,  v.,  border-
111 nums: [] | first: ambi-,  amphi-. bother,  tr.  and  intr.  v.  —  Of  uncertain  origin. Derivatives:  both
504 nums: [] | first: =  F.)  marche,  fr. marcher.  See  prec.  word  and  cp.  demarche. March,  n.  —  ME.,  
505 nums: ['940', '941'] | first: —  L.  maritalis,  ‘of  mar¬ riage',  fr.  maritus,  ‘a  married  man,  husband’, which  i
519 nums: ['968'] | first: ��  Gk.  pepo-,  pep-,  fr. pspos,  ‘part,  lot’,  which  is  cogn.  with  L.  merere, mer
520 nums: ['970', '971'] | first: Xaox6g,  ‘bud,  sprout,  shoot’.  Meaorcoxapta  (scil.  /<ipa),  ‘the  country  be¬ tween
```


## [2026-09-07T17:37:58.594Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD mazg ===\"; grep -n \"^mazg\\|mazg \" PHD.txt PHD_mackenzie.txt | head -10; echo \"=== NYB ===\"; grep -n \"mazg\" NYB_vol2_glossary.txt | head -10; echo \"=== HRN mark/mazg ===\"; grep -n -i \"maġz\\|magz\\|mazg\\|mághz\" HRN.txt HUB.txt | head -20"
}
```


### [2026-09-07T17:37:58.671Z] TOOL RESULT

```
=== PHD mazg ===
PHD.txt:473:mazg [mzg | (M та], N mayz)] brain, marrow.
PHD.txt:4847:mazgit mizné may magas padīr-! padīrišnī padiriftant magind makog 1-2mar marg margomand margarzān margīh
PHD.txt:4864:mazg, mizd
PHD_mackenzie.txt:3522:mazg [mzg I (M mgj, N mayz)] brain, marrow.
PHD_mackenzie.txt:3523:mazgit [mzgt l IN . . . . ] mosque.
PHD_mackenzie.txt:9111:mazgit
=== NYB ===
2523:mazg [mzg] brain 69%, — Av. (1159) mazga-; MPrs mgj,List 85; Paz. maz(a)g, magz; NP mayz.
5227:maé0ana-: mahmančh mahrka-: marg Mahrküsa: Markus maičyšna-: miyan maidy6.zaromaya-: maióyozarm mainyaoya-: mönöi mairya-: ?mar, mérak maxši-: *macäh Iman-: mčnitan, 6mét 2man-: mandan manah-: hešm-manihš Manuš-ciEra-: Manucihr maodanö.kara-: mustā- pät Imar- (mirya- morota-): murtan ?mar-: amar ?mar- + avis: ošmurtan maroz-: marzihistan maroza- -- pana-: marz- pan Maryu (Mouru-): Marv maršo.kara: "maškar mas-, Masan-: mas masya-: mahik mašya-: mart mafra-: mānsr mafra-sponta: mahras- pand (fra-)may-: framātan (ni-ymāy-: ni-mütan (pati-ymāy: patmān mazdayasna-: mazdēsn mazga-: mazg meroždā-, meroždika-: āmuržītan midaoxta- (mi€oxta): mitöxt miOra-: mihr
6043:m’n’g: mānākēh m'ny: Mani m’yg: mätakik mgj: mazg
6716:maz(a)g: mazg
7253:magar: hakar magas: *macāh mayz: mazg
=== HRN mark/mazg ===
HUB.txt:7973:'Gehirn' = zd. mazga-, ksl. mozgu, idg. mazg'^ho^.
HUB.txt:8854:dagegen kann mayz 'Gehirn' = zd. mazga- nicht auf ap.
HUB.txt:8855:^mazya- zuriickgefiihrt werden. Wurde schon ap. mazga-
HUB.txt:8856:in "^magza- = ^mayza- umgestellt? Np. taj 'Krone' ist
HUB.txt:9552:g) Ap. zg = np. yz: mayz 'Gehirn* = zd. mazga-.
HRN.txt:8573:Kä§. magz, magzL
HRN.txt:8574:aw. mazga- 'Gehirn'; phlv. mazg; ai. majjdn- 'Mark*.
HRN.txt:8576:(174); bei. mazg (229); sar. muig 'Knochenmark', da-
```


## [2026-09-07T17:38:00.007Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT mazga ===\"; grep -n \"mazga\\|mazgəm\\|mərəzu\\|marəzu\\|bərəzi-caxra\\|bərəzicaxra\\|marəzujīti\" BRT.txt | head -20"
}
```


### [2026-09-07T17:38:00.066Z] TOOL RESULT

```
=== BRT mazga ===
20185:•  j.  mazga-  m.  'Mark,  Gehirn':  'gjmca F.^h.
20187:•  j.  mazga'vant-  Adj.  (fem.  •vaitl-)  'mit Mark  versehen':  raoynavaiti  °vaili  (VSf.) frazaintivaiti  V,  21. 7.
```


## [2026-09-07T17:38:08.496Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8565,8585p' HRN.txt; echo \"=== HUB ctx ===\"; sed -n '7965,7980p' HUB.txt; echo; sed -n '9548,9556p' HUB.txt"
}
```


### [2026-09-07T17:38:08.559Z] TOOL RESULT

```
mog^ mogpet, movpetan movpet), daneben maupat (syr.
LW. NtOSID, daraus gr. Mavlnväg d. i. Mavmxäg und
Mavinvüv&d d. i. Mavmvovx^ä, Nöldeke, Karnämak
59 Note 4); ar. LW. majüs (Plur.).
985. mey 'Tiefe, Fluss''), meyak 'Graben, Grube* (Sahn. I,
174 Vers 817).
aw. maya- 'Loch'; phlv. may,
986. meyz 'Gehirn*.
Kä§. magz, magzL
aw. mazga- 'Gehirn'; phlv. mazg; ai. majjdn- 'Mark*.
af;'. mayz, Plur. mayza 'Gehirn'; oss. (LW.?) mayz
(174); bei. mazg (229); sar. muig 'Knochenmark', da-
gegen sar. moyz, siyn. mayz 'Gehirn' wohl LW.
987. unuft unbedeutend, umsonst erhalten'.
ai. l/'möC' ^befreien, wegwerfen* (also mtikta- etwas
Weggeworfenes', wie np. Juft aus yuktd-), Darme-
steter, Et. ir. I, 88 Note 2.
Die entlehnten nslov. muhte 'sorglos', serb. mukte,
muktice 'umsonst', ^wwiton^i 'schmarotzen' (Miklosich,
SWAW. Band 35, 129; 37, 86; 38, 176) würden die
ursprüngliche Form dann nachträglich wieder ent-
=== HUB ctx ===
als r:
a) Iran, zd (= idg. s oder Dental -f d, dh) = ap. np.
zd; iran. zg = ap. zg = np. yz: sassanid. Hormizd =
phi. Ohrmazd, ap. A(h)uramazd(l, arm. Ormizd, alter Ara-
tnazd; arm. Artavazd = zd. Asavazdah-, gr. '^praovdadrjg
(Strabo), ap, ^Artavazdah-; np. nazd 'nahe* = zd. nazda-;
phi. arm. azd *Nachricht, Kunde' =■ ap. azda *Kunde'; np.
miyazd *Gelage' (Parsenwort) = zd. myazda-, Np. mayz
'Gehirn' = zd. mazga-, ksl. mozgu, idg. mazg'^ho^.
b)tlran. zm (= idg. ^^ g^h + w, auch][dA -f s + w?)
= zd. sm = ap. np. zmi bazm 'Gastmahl', arm. bazmakan
*Gast*, siehe oben p. 29 ; razm *Schlacht, Kampf , arm. razm
und paterazni, phi. razm u patrazm Yatk. i. Zar. 66, zd.
rasman-, Wrzl. reg'^, siehe oben p. 66; hSzum 'Brennholz'
= zd. a^sma-, aus *aidhsmO'?, vgl. gr. ai&w; Gurazm bei
Firdusi (fur *Karazm) = zd. kavarasmo (gen. sg.), Dar-

Min.61.212, zA.vazra- (arm. ^?ar.^ 'Stock*
niit r^?)
f ) Ap. mr ^=^ np. rm : narm Veicli , sanft* = skr. namra-
*sich biegend*.
g) Ap. zg = np. yz: mayz 'Gehirn* = zd. mazga-.
h) Die Lautgruppe fs {=^ idg. pskVi) bleibt oder wird zu sp
umgestellt: tafstdayi *heiss werden', zd. tafsat; xuspidan
*schlafen' (jiid. pers. xufsidan), zd. x^afs; casptdan =
cafsidan 'anpacken, kleben. Ueber turns *sauer =
```


## [2026-09-07T17:38:09.936Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"caxra\\|cax_ra\\|marazu\\|marzu\\|mərəzu\" BRT.txt | head -20; echo \"=== berez ===\"; grep -n \"borozi-\\|barazi-\\|bərəzi-\" BRT.txt | head -20"
}
```


### [2026-09-07T17:38:10.003Z] TOOL RESULT

```
2686:*zamarigusa    avazat   vXspe   daifa    Yt /<?.       AbleiV  aus  ■arr'OB.u'ajflZw. 'elf;  vgl.  tF,  S  ?/o 81 ;  —  yahmai  . .  aurvantö  . .  v3sa  '^an-  ■     aK  und  IF.  p.  245.  —  Pü. :  yHdahum. }aianie   °va   caxra  (sd.)    Yt  10.136;    —  •  j-    aeväkam    Adv.    'zugleich' (?):    aiv aim  .  .  yß  t0  °ve  säsnä   (sd.)  gäsatä    Y.   narqm  asaonqm  ahunvitim  ga^qm  frasrä- ^9.8;  YtJ7.i9,2i;    —  yö  nö  °v6  at  U  vay'nti  Vd. /2.
5485:•  j.,  g.  aradra-  Adj,  (fem.  'rJ-)  'getreu, 'verlässig':  'rS  '^wävqs(sd.)  ÄitzSntuü  sfmtö mazdä  Y. 4:_j.3;  46.^;  — fravasayB..  °rä taxmä  *at>javuAai/i/ \l.  ij.  $2;  75;  — mihrgm  . .  y5  äsunqtn  äsus  yS  'ranqm  °rö y3  taxmanqm  taxmS  Yt.  70. 65.  a)  mit DaL:  kuirä  tsi  °rä  masdä  ysi..  caxrayö' (sd.)  "ob  sie  wohl  dir  getreu  sind,  die  . ," Y._j4-7-  A)  insbes. 'dem  Glauben  treu, gläubig,  fromm':  firasaosträ  air3  tu  'r.lis idi  hvB^S  täis  yitig  . .  "o  Fr.Hv.,  dahin geh  mit  diesen  Frommen,  denen  . ."  Y. 4'j^i6;  —  kä  iw'ffi  a/a  äk,i  (sd.)  'ring isyl  Y.  4S.  8;  S*}.  4;  —  fatrijasai  .  .  at vä  aia  "rahyacä  mmankä  "..und  vor  euch, o  Asa,  auch  mit  dem  Gebet  des  Frommen" Y.50.8;  —  da^at  ahrnili  tat..  arfdvJ . . 'räi  yavmiini  jatoyantäi  da^ris  ayaphm Ytj.ig;  13a,  /5.1,  21.
5855:•  g.  'a-spä-  n.  'Unglück,  Leid':  ySt vanhSus  vaidinä  (sd.)  manatthiS  sSnghaS raSxma  °spsn^l  (AP.)"  sadräcU  caxrayS (sd.)  tuMro  Y.34.T,  — yJn7  usJn  (sd.) &r;>i  sp7nlä  'spJnla.  (AP.)"'  Y.^ij.g.
7279:charakterisirenden  Adj.  (sd.,  auch  fdSt.): vispasca  äpS  yazamaide  ya  z)m3  armaesta (sd.)  *fratat.ear3tasca  (sd.)  *xqnyk  '^raots.- stälasca  par^uya  *v3iryäsca  (sd.)  "alle Wasser  auf  der  Erde  . , :  die  stehenden  und fliessenden,  die  in  Quellen  und  in  Fluss- laufen,  die  Schnee-  und  Regenwasser"  Y. 61^.6;  usw.;  —  vJspä  apd  xä  pttiti '^raotS.- stSiasca  Y.yi.g;  —  sps yal  armal^tayä.. yat  cätayä  uzuityäsca  .  .  yat  sna^ntyaica srasUntyaica  . . yat ß^tat.^antayä'W .  6.^0, 33i  36,  39;  —  äpim*  tacintqm  . .  xayanqm .  .  zrayanqm  .  .  artmaistqm  Yt.6.2;  Y.ig. 26,  Vd.4;  —  caval  nä  apa  (statt  DS.) ''frälat.cartte  .  .  paiti.iaräi  .  .  cval .  .  ape armaisfaya  (statt  DSf.)  .  .  nävayayai  tia ape  ..  ti.66(.;  —  apqm  ..  nävayaiiqm (sd.)  paiti  pintüs  Yt  //.  4 ;  usw.;  —  andvim . .  ye^he  avavat  .  .  äps  lata  (sd.)  ava.- barmle ya%ia  ..  Yt.5.15;  Ä.47; — gairil yS  uiiiä  yim  aiwiid  paoiris  äpS  hqm  gairi- ü(/('(sd.)/(WJ«/JYL/9.66; — spim  laokmta' vaitim  zaranyävaitlm  vihusavaifim  (sd.) V.^.54;  —  ap3mca  haomyqm  {sA.)  Y.  22. 2;  usw.;  — yaSsyatitim  äp^m  *pararihät Y.g.ii;F.4 f.,  V.21;  —  ?iqm.taptibyB  aiwyS caxrare(sii.)  n^r^bydY.  4.46; — apU  ai yaza- maide malkaintllcä  (sd.)  * hsbavaintlicä  . . Y.JÄ3«.  C)  GP.  apqm  mit  napat-m. (sd.,  auch  fdSt.)  Name  einer  Gottheit: apqm  napäs?  tä  apff  ..  vliax/aiti  YtS. $4; usw.  2)  von  bestimmten  Flüssen  oder Seen,  'Gewässer':  andvl  (sd.)  nqrna  äpa (NS.)"'  V.  7. 16;  —  n?mS  artduya  aps  anü- hitaya  Yt  r.  2 1 ;  Y.  6$.  i ,  Ny.  4.  o.  Vr.  1. 5 ; —  *atikäs^a  (näml.  artduyä)  mS *aaatiAä aps  apayiarsY .  65.  i;  5;  —  upa  äp.'myqm vltaaukaittm  Yt5,76;  —  njinB  ape  däit- yayä  (sd.)  Yt./.2i;  5.112,  5,29,  /7.61, V, ig.2;  —  aoi  apjm  yqm  raiakqm  (sd.) Yt.5. 63;  —  haca  apat  kqsaeyät  (sd.)  Yt ig.92,  V.ig.$;  —  a/s  ya  aw^änva  nqma Yt  ig.  62;  —  yazäi  äp^m  frazdänaom  F. 4%.  I,  2  Anhang:  apqm  (näml  ayar^y
8730:tßi  aridrä  (sd.)  .  .  ysi  vanhSus  vazd>na (sd.)  manauhö . .  aspSncit  sildrJcU  caxray3 (sd.)  'S3ura  (IS.)  \.34.T,  —  hamSm  tat vahiitäat  y!  's'urvye(DS.)  syasclt  (sd.)  dah- mahyä  Y.  J2.  r6.
11131:•  j.  caxra'vant-  Adj.  (fem.  •vaia-)  'ein Rad  (als  Feldzeichen)  führend"':  hafnayä 'vailyh  Aog.Si.
11243:Z'um  V,  )ak-,  s.  ta/'ar-  und  BTHL.IF. /o.  3. — i>  Hds.  j''a"ftjw;  Tgl.  iiar-  No.  2  und  anya- No.  6;  femer  zu  lanal,caxra-.
18701:Aus  dem  Zusammenhang  gerissene,  un- deudiche,  verderbte  oder  wertlose  Stellen mit  nar-.  «flr/(GS.)  ..  nara  (ND.)  .. «(jr?(NP.)  F.  2e;  —  «3  Fsd;  — nanm ..sar>t)m  V.^.  14  PüZ'J»;  N.52"';  — panca  narB  V.  75.  loPüZ.;  Vyt.  42,  Vd 13,15;  —  dva  nar^FiB.; — para  "iafah- mät(sd.)  n»r>t  (AblS.)  V.  j.  42  PÜZ.;  — aBsqmia  naram  V.  5.  gPUZ.;  —  ham.- tapiibyB  aiwys  caxrart  (sd)  n^r^byB  V. 4. 4  7 ;  I  o  PiiZ. ;  —  tl  ^narsS paitismarmitm Vy^  52;  —  nöil  dim  "nara  . .  avasyil  Yt /.  aS;  — ya'ia  na  ttäifyaY.  20.  2;  Yyt  28, 30.  narSm  nartm  als  Adv.  sbes.  [N. 301  streiche  «a.J
20847:I  et  (eum)  qui  (est)  faciendi  et  dicendi" I  Y.  33. 14;  —  *grSkms . .  atikSus  maraxtärB I  (sd.)  ahya  \yai(a  ^'Grlhmas  . .  et  (ii)  qui (sunt) ..  destructores"  Y.J2. 13; —  ku%ra töi  andrS  (sd.)  .  .  yöi  .  ,  caxrays  "num tibi  (sunt)  fidi  (ü)  qui  . ,"  Y.^4.7;  — kada  .  .  yOi  uxiäiiS  ainqm  .  .  frärmtl "quando  . .  (ii)  qui  (sunt)  tauri  .  ."  Y.  4G. 3;  —  naldä  dahySus  \ydi  iastSrS  drjsvatas "neque  (ii)  qui  (sunt)  . .  imperatores"  Y. 4O.  I ;  —  tat  ..  uitanai  data  . .  ySi  sl gSus  v^nzinl  (sd.)  azyi  ".  .  vitae  (eorum) qui  .  ."  Y.  34.  14;  —  tim  at  yasna- nqm  paurvataia  yazamaidl  ySi  ..  iyeintJ ".  .  imprecationum  .  .  (eorum)  qui  .  ." ^•37-  2;  —  yi  varpsaiil  (sd.)  kyat vasnä  firasöJ^mim  "qui  . .  fecerit  . .  (id) quod  (est)  .  ."  "^.46.  19;  —  hyatcS dar>gSm  dr)gvll.d»byS  rasB  savai'a  alavabyö "et  (id)  quod  (est)  . .  damnum  et  lucra  . ." Y._jo.  11;  —  Aaihyavanitqm  {%A.)  hyat vasna  f?rasS.t}m}m  "verificationem  (eius) quod.."  Y. 50.11;  —  ai  zt  töi  vaxsya .. hyai  aksyä  (NSf.;  sd.)  dngvaiii  wörtlich ",.  von  dem,  was  die  Androhung  ist,,"  Y, 51.  8;  —  hyat  "qsasutä  (sd.)  yä  (NPn.) daiiiiana  (sd.)  fraoxta  "..  (ea)  quae  (sunt) . .  enuntiata"  Y.  48.  1 ;  —  das  Relativ  kon- gruirt  mit  dem  Praedikat:  vldvä  yalclt güzra  (sd.)  singhanhS  (wörtlich)  "kennend auch  (das),  was  die  geheimen  Lehren  (sind)" Y.4<V,3;  —  anais  a  vT.nSnasa  ya  (NSt) iarapsjis{ad.}cä  kjvltäscä  Y._J2.  15;  — *m>ndäiäyai  (sd.)  ya  (NSf)  toi  adisHi Y.44.8;  5,^.13;  —  nipatihw . .  tumas^a ya  armaitiH&d.)  Tiilcä  Y.4g.  10;  —  yS va  mSi  \yh  (NPf)  gasha  dasdi  (Sp. 7 1 S  u.)  *asnatihe  wörtlich  ". .  (das),  was meine  Besitztümer  (sind)  .  ."  Y,  46. 8;  — vtayUta  yä  (NPn.)  mrqi  sädra  drtgvats (wörtlich)  "immer  (wird  sein)  was  die Qualen  (sind)  .  ."   Y.45.  7;  43-5,  49-6;
22013:—  yesi  .  .  dim  nsit  tanu.ptn'Afm  *v^ar)  im  Besitz  des  wahren  heiligen  Wissens (sPPfA.)''  "wenn  sie  es  (von  ihm)  nicht ^  befindlich,  darin  eingeweiht"-^;  n)  von wissen,  dass  er  /,  ist"  ^.3$ ,3g, 38')  — \AhM.:  *yqm  mBi  vtdva  matda  vaocat at  vS  xsmaibyä  asBrtä  vasdä  x^arai'^yä '  a/iurS  "was  mir  der  wissende  MAk. (sd)  srava  Y.2Ä10.  a)  'etwas  (Akk.)  1  verkündet  hat"  Y.45-3;  —  vaocä  mH kennen  als  (das)  des  —  (praedik.  Gen.),  j^i?  (VJ'w  zTrfz'i  a^ars  "tu  mir  kund  — denn scire  rem  (esse,  fore)  ahcuius':  yehyäxda  ja  bist  der  wissende,  o  Ah.  —"  Y, tnHi  asät  hacä  vahist>m  yesnl paiti  vaidä  4IS.2.  ß)  sonst:  müahvacff  v3  *Pr7s,- mazda  ahurü  ySi  nnharsia  htnticä  "wen '  rairc  vä  vTävä  vä  >vfdva  {sd.)  vä  Y. von  denen,  die  waren  und  die  sind,  MAh. als  einen  solchen  kennt,  dem  durch  Asa mein  Bestes  fiir  sein  Gebet  zu  teil  vrird" '^.51.22;  —  ynihe  Aätqm  aat  yesm  paitt vaahs  mazdä  ahurö  vatha  asät  hacä  Y. 27.  15;  —  yaisqm  nS  ahur5  .  .  va^hs vaiha  "quorum  nostium  Ahuras  ..  melius (fore)  seit"  Yt.iÜ.s;—  *yat  nSil  vist»m drvats  "wovon  man  nicht  weiss,  ob  es einem  Ungläubigen  gehört"  N.  54**;  — ysi  vaahsul  vaEdtnä  (PPfM.)  mananhs .  ,  ralxsnh  .  .  caxrayS  (sd.)  ".  .  die  dem guten  Sinn  gewissen  Erbanteile  .  ."  Y. 34.  7.  3)  Perf.  Pass.  'bekannt  sein als  —    (Nom.),    etwas   (Nom.)    gewisslich
24717:•  j.  vy-ä'zda-  Adj.  (fem.  °dä-)  lauernd, insidiosus':     hainayä     caxravaityä     'dayä
24738:•  g.raexanah-n. 'Erbe,  Erbteil'",  in  escha- tologischem  Sinn,  von  dem  was  den  Gläu- bigen als  Lohn  bestimmt  ist'':  aauAlicä atthvascH  apayeilli^A.)  'nanks  vald>m  Y. 32. 11;  —  yBi  va^hsui  valdfnä  (sd.) manatgAS  .  .  °nä    aspSncU  .  .  caxrays{^)
26178:•  j.,  g.  8ädra<  n,  "Leid,  Qual,  Wehe': 'r)m  urviitr>m(sA.)ca  nimrüite  tiStryS  .  . °mn  trii , .  urviänm  aps  Yt.8.iy, —  usta ahntai  naire  . .  °rpm  ahmai  naire  Yt.  10. 1 3  7  f-  i  —  auch  Plur, :  ysi . .  rasxmä  aspSnäl 'raHt  caxrayS{%A^  '^■34-  7;  —  °ra  mal  sqs (Sp.  issSu.)  *graid3iti/Y. 43.11.  a)mit Akk.:  utayoia  ya  narqi  'ra  dr^vatS "immerdar  (aber  werden)  die  Qualen  der /?ri(?genossen  (währen)"  Y.  45. 7;  ver- wendet Vr.iÄ2,P.2Ä,  G.^.6  ("r-a).
26264:•  g.  stegha-,  aänsba-,  j.  sasha-  m.l!'«»'***^  vasimä  (Sp._i3i5  u.)  mamaata 1)  'pronantiado,  Verkündigung,  Lehre,  I '"f^'S'*' dP-)''  raixMa  aspSnäl  ssdräät Sprach':  hyai  nS  matdä  .  .  gat>äscä  tasö  ■  caxrayB  (sd.)  Y.  jj.  7.
27858:•  j.  zaranaena-,  zaranaena-'*  Adj.  (fem, "«r-)  'von  Gold,  golden';  auch  'mit  Gold besetzt,  verziert  (usw.)':  väiim  . .  'tarn  Yt 10. 124;  —  'nim^^  (näml.  tait>m)  aoi  Y. 10. 11;  —  'mm  faili.dsn3m  Yt5. 123;  — suwrqm  'njm  V.  2,  6;  —  suwrya  'nya  (ISf) V.  2.  10,  30,  38;  —  pusqm  .  .  'nim  Yt. 5.  iz8;  —  alva  caxrah^.)  'naY\..io.iz^) —  yezi  atakat  "«i'/""  "wenn  sie  (die Schale)  von  Gold  ist"  V.  7.  74;  —  alktm . .  'n>m  Yt  j.  136; —  hukairJm  barnS  .  . 'nfm  Yt.5.  96;  —  hukaityä^  haca  bari- zanhat  .  .  °«j}  Yt/5.  15;  —  'w  paiir gatvd  Yt/5.  i;  a*;  —  U  para.safanhs (sd.)  'na  (NPm.)  paiH.Muxla  (sd.)  äal  hl apara  >r)zataina  Yt  /O.  125;  —  gaosävara ..  •«/(ADm.)J'  Ytj.ra?.
=== berez ===
```


## [2026-09-07T17:38:17.283Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"kurzlebig\\|kurz'\\|kurz\\b\" BRT.txt | head -25"
}
```


### [2026-09-07T17:38:17.336Z] TOOL RESULT

```
37:In  der  Bezeichnung  der  Inschriften  habe  ich  aus  praktischen  Gründen  meine eigenen  Wege  gehen  müssen;  sie  waien  von  dem  Bestreben  bestimmt,  möglichst kurz  und  doch  deutlich  zu  sein.  Für  die  Inschriften  von  Bahistän  habe  ich  darum die  herkömmliche  Bezeichnung  durch  Bh.  belassen;  alle  übrigen  dagegen  —  mit Ausnahme  der  Siegelsteine  von  Privatpersonen,  auf  die  ich  mit  S.  /,  2  usw.  verweise —  bezeichne  ich  mit  dem  Namenssigel  ihres  Urhebers  —  K.  ^  Kyros,  D,  =  Darius, X.  -=  Xenes,  Am.  ■=  Artaxences  Mnemon,  Ao.  — '  Artaxences  Ochus  ■=—  und,  sofern er  mehr  als  eine  hinterlassen  hat,  einer  beigesetzten  Nummer,  wobei  mir  die  Reihen- folge bei  W.-B.  massgebend  war,  nur  dass  ich  zwischen  NRa  =  D,  6"  und  NRc  = D.  J  ein  D.  7  eingeschoben  habe,  das  die  bei  W.-B,  fehlende  zweite  Inschrift  von Xaki  i  üustam  meint  Praktische  Gründe  waren  es  auch,  die  mich  veranlasst habgn,  alle  Verweise  statt  wie  bisher  üblich  nach  Zeilen  vielmehr  nach  Abschnitten (Paragraphen)  zu  geben,  und  zwax  für  die  fünf  Inschriften  von  Bahistän  mit  je gesonderter  —  nicht  durchlaufender  —  Numerirung.  Ich  biete  im  folgenden  eine Cbersfcht  über  die  verschiedenen  Arten  der  Bezeichnung  (und  Anführung)  bei  W.-B., Spiegix  und  bei  mir.
2038:Auf  die  verwandtschaftlichen  Beziehungen  der  altiranischen  Wörter  bin  ich Überall  eingegangen,  aber  überall  so  kurz  als  möglich.  In  den  meisten  Fällen  konnte ich  mich  mit  dem  Hinweis  auf  das  verwandte  neupersische  oder  altindische  Wort begnügen,  das  ich  den,  der  nveitere  Verwandte  kennen  lernen  will,  in  den  etymo- logischen Wörterbüchern  dieser  Sprachen  nachzuschlagen  bitte.  Nur  da,  wo  icli glaubte,  Neues  bringen  zu  können,  ist  der  Etymologie  etwas  mehr  Raum  gegönnt worden.     Im  Übrigen  bemerke  ich,   dass  ich  in  Fragen  der  Etymologie  durchweg
2057:In  den  Noten  habe  ich  mich  bemüht,  so  kurz  wie  mögUch  zu  sein.  Ich  hoffe gleichwohl,  nicht  missverstanden  zu  werden.  Wenn  ich  z.  B.  Sp,  1853  m.  unter "teuaipaSya-  habe  drucken  lassen:  "Ableit.  aus  :^agpaihya-",  so  ist  das  selbstver- sßndlich  streng  dem  Wortlaut  nach  falsch;  das  persische  Wort  kann  nicht  aus  dem awestischen  abgeleitet  sein.  Würde  ich  aber  geschrieben  haben:  "Ableit  aus  einem dem  jAw,  ::^a^äikiya-  entsprechenden  ap,  '^uvaipaüya-" ,  so  hätte  ich  vielleicht  trou aller  Umständlichkeit  und  anscheinender  Sorgfalt  doch  auch  etwas  falsches  behauptet; denn  die  Bildung  des  Worts  kann  ja  schon  in  z^orpersischer  Zeit  erfolgt  sein.  Ich glaube  wohl  kaum  besorgen  zu  müssen,  dass  der  Leser  in  solchen  Fällen  verkennt, was  ich  meine.
15308:'gleich'.  —  Pü.  (in  V.  yp);  ku  Hält  däir  api raruiend,  erl. :  \kii)  iSn  äyiin  u  iavHit  tu  yäi, s,  No.;  (tu  V.  S):  ka  apar  pukrik  att,  erl.! ka  apta-  vicärel.  —  >)  So  nach  Jp  I,  Mr2. NA.  hat  pärayänii  (».  auch  Pü.);  doch  beachte man,  dass  kurz  lavOT  zweimal  nipätayania steht,  das  leicht /äi-iij''  vnanlasst  haben  kann. pairy'  ist  jedenfalls  die  lectio  diS".
15924:1)  'aufscheuchen':  yä galwqm  yam  apu- %rqm  janaiti  va  vayHti  va  xraosyeüi  va paldayäli  va  "wer  eine  HUndin,  die  kurz zuvor  geworfen  hat,  schlägt  oder  verfolgt oder   anschreit   oder  aufscheucht"  V.  i^.
22274:Denken,  Sprechen  und  Handeln ;  s.  No.  13.  — <i)  Fü.:  rehlL  DST.  ZA.  j.  124  meint,  es  seien die  Worte  aia.sara  manaaha  aSa.sara  vacaaka ajajara  fyas'i.na  damit  gemeint,  die  allerdings lu  N.  67  kurz  zuvor  litirt  sind.  —  MJ  Was ist  unter  den  "beiden  Worten'  oder  'Wörtern' lu  verstehen?  Pü.  (für  V  f):  apdi  giaiiniA fa  faliaäii  iiiämrül,
```


## [2026-09-07T17:38:24.427Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '20120,20190p' BRT.txt"
}
```


### [2026-09-07T17:38:24.489Z] TOOL RESULT

```
•  masah-  n.  'Länge;  Grosse':  ar?dvlm sürqm..yiJ  asti  avavaiti  {sA,)  'sSyd^a.. Y.  65. 3.  a)  AS.  als  Adv.  'valde' :  za/ar? tafsan  (sd.)  aya  's3  V.^.3a.
KompE.  —  Zu  mos-  Adj.  —  Vgl.  gr.  /if«?.  — Pü.;  masik,  (zu  a);  masäi.
•  j.  masö  Adv.:  s.  masah-.
•  j.  masit-  Adj.  'ausgedehnt,  gross':  ya%a ave  awra  upäpa  °sitS  gairJs  iiivämnti  Yt r^.  41.
Ableit.  ans  mas-  j  vgl.  masila-  mit  No.  Z.
•  j,  masita-  Adj. "  (fem.  'tä-)  'gcoss,  um*
37
dby  Google
155
masiSta-
fangreich':  andvJm  .  ,  'sttam  .  .  yS  asti avavaiti  masS .,  V.  ö^.  3 ;  —  tarn . ,  »maita 'siti  ädlahi  Yt.JO.30;  —  äaya..xratüm pascalta  •sitim  matanhm  afiairi.a'isntn (sd.)  Y.  62. 4.
Ahleit.  ant  mos- ;  Tgl.  naiäa-'}.  ~  Pü. :  mai. ~  ')  Vgl.  noch  lu  p.  "Maiäaam.  —  >)  Vgl, fti.  iarit-  und  kaHla-'i
•j.inasijtta-,p.ma9i$ta-Adj.'dergrÖsste'j i)  der  Ausdehnung  nach :  kasistahe  .  . mahmahe  .  .  °tahe  3r>svS  frat3m3m  iMsü V.  6. 14.  2)  U  dem  Rang  nach:  a*wra*- matdä  . .  hyer  -tJ'  baganam  D.4.1;  X. 6. 1.  a)  bes.  'der  Oberste'  cinerTruppe: AyO*  tnadaiitiva  *t^  akJ'  Bh.  2. 6;  —  hyJ' avahyä  karahyS  °ta*  äk^  Bh,_j.  11;  11, 2.4;  —  avamiam  'tarn  akunavam  Bh.2. 6;  I4,^.6j9,I4,  5.1,4; —  avam  'tarn akunavcl'ts  "den  machten  sie  zu  ihrem Obersten"  Bh.j.3,  5.1.
Snperl  lu  ihjj-.  —  mp.  (Pü.),  np.  mahisl.
•  j.  mastay-  f.  'Kenntnis,  Wissen':  dasdi ahmähm  ..  'am  spära  vaä\imca  Yt  10. 33;  5-86.  Y.p.  22,  6'2.4;  —  -iT/n  iTj/J.- pagsaT)h»m    "allseitiges  Wissen"  Y.  5.  17;
57-  "■
Zum  V.  manrf- ;  S  iJ  D ;  'ßl.  dagegen  mtaav-. —  Vä.:  fratänaAIA.
•  j.  "mastflm''  a'hrmnhm  äsiaia"  N.2.
•  j.  ^mastrayan-"  m.  i)  'Schädelwand': a^fl  (sd.)  , .  *yffi  *aparaya  paiti  *'ynya  '* (LS.)  .  .  *ySi  *faouruya  paiti  *'yKaya'* (LS.)''  F.jc.  a)Plur. 'Schädel':  asüm '^alvB*'ynqm*'i'*  vTspaca yS°ynqm^'>  amqsta (sd.)  F.jc.  2)  Plur.  'GehuTi':  «j/ääi vanUsca  *'ynas/a''>  (AP.)  YtJO.  7a.
Statt  masttri^  geschr.,  S  368.  39;  Bthl.  IF. lt.  iiS  No.  3,  wo  auch  lEt.  und  vm  Stamm- bUdung.  —  mp.  (FQ.)  mastur^ ;  oi.  vgl.  maslaia- m.,  n.  'Schädel',  iriasli}tit-  m.,  n.  'Gehini'.  — ■)  'j/r^-  bietet  F  1  (usw.);  NA.  und  F.  haben •stra',  einmal  •sIrT.  —  »)  Them.  —  3)  Hds. mailrauaaifm.
•  j.  masya-  m.  'Fisch':  kars  {sA.)  'syö upäpd  Yt  14.  29,  V.  ig.  4a.
ai.  mAlsya-  m.,  np.  mü^f  (,  wozu  HoRN  GltPh. /  b.  23).  —  Pü.  (mV.):  fehltj  Npü.  (lu  Yt): undeutlich.
j.  matyayd  V.  5.  14:  i.  unter  majyak-  (mit No.  3).
j.  masyah-  Adj.  (fem.  'yehJ-Y^  'der grössere':  Ä  üsti  '_>'?(NSn.)  vatghs  srayS (sd.)  aittm  dättm . .  upairi  anyäi^..  V.5. 22 ; avai  hl  asti  'yS  ari^»n  (sd.)  V, 7.71; tisit  maslm  gag%Jm  ff?(sd.)  'ya  hacaiU (sd.)  3snS  xratui  YL/0. 107;  —  ''kaya h»nH  •yaaho  (NP.)  a^  (sd.)  .  ■  *ltaya kasyanhö  F.  j  c ;  —  ^a^  'yS  attahmäi barfsma  N.  70;  —  ^aSa  tJ'ays  (NSf.)" J/^  kasyanhqm  apqm  *avi./rädavaiie  (sd.) V.  5. 24;  —  ya%a  yayi  (NSf.)''  vana kasyanhqm  vanqm  aiwi.vfrjnvaiH  (sd.)  V. 5.  24;  —  yimö  . .  tqm  vXSävayai  (sd.)  atva 'kriha  ahm3l  'yehim  ya'^a  . .  V.3.11;  — fravasayS  .  .  yä  'yehll  ahmät  .  .  yaäsa vaca  /ramraväire  (sd.)  Yl  13.  64;  —  °yd va  ahmätäi  "oder  noch  grösseres  (ärgeres, näml.  soll  als  Strafe  ihm  geschehen)"  V. 4.  50.  a)  'von  grösserem  Wert,   wert-
voller": yai  'yS  catahmät  *vastr3m  "wenn das  Gewand  wertvoller  ist  als  das"  ^.Sy^. Kompar.  lu  mos-.  —  mp.  meh,  np.  mih;  gr. fiaecay.  —  PQ. :  mos,  —  i)  S.  noch  maryayi mit  N0.2.—  ')  Vgl.  daiu  i  20&.2  No.  I.  �� 3)  Pü.j  Aaiar  me/i  har  an  oil  vaslrai,  mit  der Erl.:  orL     Vgl.  N. /o.
•  j.  masyö.xra&wä-  f  'grössere  Einsicht^: talla  yä  kasujcratus  ''hmqm  nöit paitiimti "wenn(?)  wer  geringe  Einsicht  besitzt,  nicht nach  grösserer  Einsicht  strebt"  V.  7. 59.
VIL  durch  Haplol.  ^3p6)  aus  ■•xro^imi^nu-, Ableit.  aut  ''scn&toan-,  alio  eig.  'Zustand  des, der  grössere  Einsicht  besitzt'.  aSuff.  ar.  I^ä- s.  Wh.  Gr.i  S  »J^b  bE.,  Bgu.  Grdr.  3.  iil. Geringe  Stelle.  ~  Pü.:  jr  mos  xraiih  rü  apar bähend,  erl. :  ehrpaüilän  nt  girind,
•  g.  maz-  Adj.'J  'gross,  von  hervorragen- der Bedeutung';  von  tnaga--.  tost!  afat-a umahs  'sei  magai  (sd.)  Y.  46.  14;  29. 11;  —  von  J/3Ä-:  pars  '*}  (GS.)  yat»hs ahmäi  nS  sazäyäi  (sd.)  bacäantB  paiR Y.  30.  2.  a)  IP.  maxiblf*  als  Adv. 'magnopere,  mit  Nachdruck]  angelegent- lich' :  yBi  m'  . .  Hkiitsn! . .  apaydtl  (sd.)  . . vaBhm  Y,j2,  11.
ai.  mah-  Adj.;  s.  No.  I.  —  Vgl.  ma^aM; maxiila-,  mqsä'  und  mai,  —  Pü. :  mos;  (lu  a): pa  iHosäi.  —  >)  Nur  in  obL  Kasus,  «bens« nie  ai.  moA:  Nom.  und  Akk.  werden  ans matant-  gebildeL  —  >)  S  3^6  No.  3.
•  j.  masa-  n.;  s.  unter  *matah-. KompE.
•  g.,  j.  mazan-  n.  'Grösse,  Erhabenheit':
dby  Google
"S7
mazant-
iSS
ahyä  xlahraca  'jUnäOSyä  ^hvapanhäiS- (sd.)i'a  tSm  (näoiL  akunm)  yasamaidi  Y. 3'J.  2;  —  mihnm  .  ,  yahmi  ..  'sa  amava nilahm  Yt./o.  64(?).
Zum  Adj.  tnat:  — VgL  ai-  mahimin-  m.  (:  g.
maian-  ^  ai,  Arwid«-  -  aus  «r.  ira(ji)ma»-  — :
j.  jj-ayOH-)").  —  >)  S.  daiu  Bloomfibld  JAOS.
r6,  CLVI,  JScHMiDT  Krit.  87  fS.  und  auch  Bgm.
GrCrJ  1S8  zu  ^V  (m[t  Litt  das.).
•  j.  mazant-  Adj.''  'gross,  geräumig;  um- fassend, gewaltig;  erhabeo':  mathan?m  . . 'zat  anattf  Yt.  10. 44;  —  Aau  'za  (NS.) mtnyS  stOHsXt.  14.^1;  F.iJ*'; — yämm.. *sänbm  Y.  6$.  11;  —  xratam  ,  .  masiUm 'sSnttm  apairi.ä^nm  (sd.)  Y.  ö'a.  4;  — sraosasca . ,  'za  amava  v^n^raja  Vr,  15. 3.
Zum  Adj,  niiz- ;  td.  No.  I.  —  ai.  mahäHl-  Adj.  — Pii. !  mm.  ~-  •>  iFlei, ».  S  rSr  b,  J95,  Richtbr IF.  p.  52.  —  »>  Nur  in  K.
•  j.  mazav-  Adj.  'acht  habend  auf  — ',  mit Gea:  a^a  spamm  nida%}m  yat  dim  'zacs (NS.)  k)hrps  türahe  "den  Hund  habe  ich dazu  bestimmt,  dass  er  acht  habe  auf  die Person  des   Tärere"  V.  13.  39.
Zum  V.  mand-;  aus  Kt.*maäzhau-,  SJi-8.  — Vgl.  got.  mundo}  'observale'.  —  Pü. :  ie  an roadak  ienä(ya)nd ßa  iarp  a/ar  lürän,  eiLi iiitiäsiärä»  t^i  däril,
•  j.  'mazah-  n.  i)  'Grösse,  Umfang' :  _>iaj:& .  .  daxmanqm  avavantpm  'xS  vltsnayäj ya^a  hl  tanus  aahat ". .  (soviel  an  Grösse als  . .  sva)  ein  Stück  so  gross  als  . ."  V. 7.  51.  2)  (etwa)  'Fülle':  'zJ  avahyai  °tS raßmSJiyai  däidl  hauruatä  am>r>tätü  "ge- währe zur  Hilfe  die  Fülle,  zur  Unterstützung die  FüUe  des  H.  und  A."  Y.  5Ä  7.
KompE.  —  Zum  Adj.  maz-.  —  ai.  mäAas-  □. —  Pü.  (zu  V.)!  masäi,  (zu  Y.):  war-
•  j.  *matah-  n.,  maza-  m.  "Draufgeld, PJänd;  Pfandwert"*.
KompE.  —  Zum  ai.  V.  mämkaU  'er  gibt hin'(?).  —  Eig.  'was  man  drauf  gibt';  Gdn. Stud.  /.  95.  —  Pa.:  masäk.  —  1)  Nicht  'Wert' übeibaupt;  das  ist  arijah-,
•  j.  ^mazah-  Adj.:  s.  unter  masyak-.
•  p.  ut3  ty(^  iunavahy  av^taiy  t^ural'- mazdä  "mazänam  kunautuv  "und  was  du tust,  das  möge  ^x  AhM.  gross  (berühmt)'* machen"  £h.  ^16.
In  der  Inscbrift  ist  nur  nfi**n^  zu  sehen. taatänam  ist  eine  sehr  unglückliche  Ergänzung der  NA.  Andre  schlagen  vaiorkam  vor ;  zU' letzt  KZ.  jj.  4^.  Steht  m'  als  erster  Buch- stabe fest,  so  liegt  ma%itam  am  nächsten;  s. IF.  II.  132,  KZ.  3^.  558.  Die  Bedeutung  ist auch  durch  EiL  und  AB.  gesichert.  —  >)  Vgl. lu  läki^tuv.
I»  j.,  g.  maziäta-  Adj.  (fem,  't&-)  'der grösste'  an  äusserer  und  innerer  Bedeutung: yS  vä  kasiuS  aSnaahs{,sA^  a  'tarn  ayamaiti *bajim  Y.j/.  13;  —  yS  na  °t>m  yasrum yasaite  kasiltim  *yasnäi  fräyaist  (sd.)  Yt. 7.  24;  —  'iiya  (7)  . .  mqnayat  (sd.)  kasishm DkB.  131;  —  kS  "^wqm  .  .  *'taya  *inÜ (sd.)'*  inaoiti  kB  'ta  ibalsanha  tbalsaydti V.r<?.6i;^.  la;  —  ydhraid  üä  ßJntä (sd.)  Yty.as;  —  °tai  yankqm  paitl.- jamyä  Y.jö'.  2,  5Ä  7;  ^  airyamaram  K.. 't»m  mraomi  . .  sravanhqm  FrW.  4.  i ;  Y, S4~  a ;  —  't^i^  vaedyäis  datnayi  mäsda- yasnüis  Y.  y.  3;  —  uitrahe  .  .  yB  arsnqm . .  °fym  aojB  abaraiti  'tftnia  ämanatfhitn Yt  74.  1 2 ;  —  °tq  amq  ämruyi  dafnayä mäsdayastisU  Y.  y .  3 ;  —  *W  amq  amrU- maide  daOtayä  Wi-J.  5;  —  anä  mq%rii 'hm  väurBimaidf{sä.)  . .  Y.  28.  5.  a)  von Personen:  at  m3  yavä  bjndvS  pafri  °td Y,4g.i;  —  'ta  (als  APm.)  mq%ra..'ta vindaihya  (sd.)  daStayä  mäzdayainBil yaza- maide  G.  2.  7;  7^,  Vyt..^^;  —  ratavs  (sd.) vXspe  'ta  (VP.)  Y.  /.  21;  —  ratavB  vispe 'la  paiti  ratüm  Y.2. 18;  17;  —  äat  tha dim  vTspanqm  °fom  ^dähimahi  ahümca ratümla  yim  ahurim  Vr.  77.  2 1 ;  —  ytiäsa Im  vXspanqm  'hm  änasti  Y.ig.i2''>,  2j.i;
—  at  fravaxsya  vTspanqm  Htm  "ich  will reden  von  dem,  der  der  grösste  ist  von allen"  Y.  4S-  6;  5?-  8;  —  ahur?m  mazdqm , .  'hm  yazahm  Y.  16.  1;  —  ahurS  mazds yB  'ts  yazatanqm  yB  vahiltB  yazatanqm Yt.  77. 16;  70.  142 ;  —  ätarl . .  'ta  yazata Ny.  j.  4.  b)  in  Verbindung  mit  vaki^ta- imd  sral^ta-:  ya%a  nS  'täsca  vahistasSa sraeitasia  a/ayS  ^nnavante  Y.S2. 3;  —  as/a zadhranqm  'taca  vahiitaca  sralliai^a  N.£^;
—  dämqn  .  .  y3  kätqm  'tala  vakistaca sraeitata  Vr.  72. 4;  —  vJspanqm  narqm näirinqmca  .  .  yüi  Aiiti  .  .  'tau  vahiitaca srasstaca  V. 2.  27;  27;  —  tat  nqma  .  .  yat tl  asti  'tim^a  vakilttmca  sralit?mia  Yt. 7.  5;  —  damqm  mäzdayamim  .  ,  ys  .  . *tacä  vahiitaca  sraiitäca  Y.  72, 9 ;  —  airya- mamm  mq%ranqm  'hm  .  .  vahist>m  .  , sralttfmYi.^.^; — siaota  asahe  yat  'taheta vahistahela  sraiUahe^a  Yt7_j.  gi;92;  — /ravastm  avqm  yqm  ahurahe  ,  .  'tqmüa vakiHam^a  sragäqmäiY.26.a;  —  ahurahe mazdi  .  .  Haheca  vahÜtaheia  sraläahe^a Y.  1. 1.
KompE.  —   SuperL  zu  mat;  mataitl:  —    tL
dby  Google
"59
maziävant-
■mazdayasna-
1160
laäMt/Aa-  Adj. —  Pü.:  mahisl,  (tu  N.):  maMif pa  /an.  —  >)  Hds.  maüUayanii  mit  Var. ;  s. aber  Fü.  —  >)  Pü.  erl.i  säAän  !äk.
j.    mazUlayanti    V.    /tf.  6 1 :    lie*    maiillaya inti  (id.).
•  j.  maztS'vant-  m.  Name  eines  Bergs  oder Gebtrgs  " :  ahmat  hala  garayS /raox^yqn . . naomö  *zisziä  Yt  ig.  2.
Eig.  'mit  *mam-  D.  (ob  svo.  "/«oio^?)  Tet- sehen'. —  >)  Man  vemeist  dazu  anf  den armeniachen  Matis.
•  j.  mazga-  m.  'Mark,  Gehirn':  'gjmca F.^h.
Ableit —  ai.  TgL  majjän-  m.;  np.  ma-p,  nhd. marii  s.  Bthl.  KZ.  a/.  352,  Ben.  Grdr.  /'. 578.
•  j.  mazga'vant-  Adj.  (fem.  •vaitl-)  'mit Mark  versehen':  raoynavaiti  °vaili  (VSf.) frazaintivaiti  V,  21. 7.
PQ.;  fniifffnjRy,
•  j.  mazda'oxta-  Adj.  'von  M.  ausge- sprochen, verkündet':  altalüa  va^S  °t?m %ri.afsm>m  . .  Y.ig.  16.
Komp.:  maidSh-\-uxta;  —  PQ.:  öknaatd gu/l.
```


## [2026-09-07T17:38:33.786Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"jTti\\|jiti-\\|jyäiti\\|jyaiti\" BRT.txt | head -20; echo \"=== search marəz ===\"; grep -n \"mar>zu\\|marJzu\\|mar'zu\\|marazu\\|marizu\\|mar%zu\" BRT.txt | head"
}
```


### [2026-09-07T17:38:33.850Z] TOOL RESULT

```
11033:yat  asti  airyanqm  daRyunqm  .  .  yatc'a asaons  zaraiuslrahe  ". .  quod  est  .  .  pro- vinciarum  .  .  quodque  (sva.  et)  . ."  YL/p. 56 ;  —  vupe  matnyava  dagva  yaloa  vannya Yt.  Jo.  97;  — y5i  vatjAsus  3  wanatahs iyHntJ  yasca  üitx  Y.Jp.  3;  —  hyat  da xyüo^anä  mJzdavqnisA.)  yä^ä  uxha  ",.fa- cinora  . .  quaequc  (sva.  et)  verba"  Y.  43. S  i  —  *gr}AmS  .  .  avAsuf  tnaraxtarS  ahya yai^a  "GrsAmas  ,.  vitae  deslructores  huius quique  (sunt)",  sva.  "Gr.  et..destnictores" Y._j2. 13; — yeTiyaaUSp.  5730.)  hsrnsmya- sattl(sd.)  mt^ahyä  yäca  hsi  ansua  Y.33. i;  —  yi  iluds  dadsniE  da%ranqm  (sd.) haüa  alätinö  y^siä  .  ,  *drigvü.d3byB  "quae debita  poscanlur..a  hdeti  (quaeque  sva.) et  ab  infidelibus"  Y.31.  14;  —  mainyus spSniStS  .  .  yaecä  xsnao/in  (sd.)  aAurjm "Spiritus  sanctissimus  . .  et  (ii)  qui  satis- faciant  . ."  Y.30.  5;  —  ya  ..  väV)r)zli .  .  yala  vaniaitl  Y.  2g.  4;  —  ya  atirayl .,  urBpayeintX  yäca  xrafä  ..  Y.4S.10; 44-  20; — y7  va  möi  na.,  dayat  ..  yqsca haxiäi  (sd.)  "qui  .  .  vir  , .  faciat . .  et  (ii) quos  .  ."  Y.  4ß.  10;  —  at  ta  vaxiya  .  .ya mazda^a  (sd.) .  ,  humqzdra  (sd.)  als  yeca ya  raocSbis  dansata  urväza  "ea  praedi- cabo  . .  quae  (sunt)  recordanda  .  „  a  bene recordante  una  cum  Asä  quaeque,  quae una  cum  luce  videatur  voluptas"  sva,  "et voluptatem  quae  .  ."  Y.^.  i;  —  zu  c: at  yül  dasva  .  .  yasca  vh  .  .  yazaitl  Y. J2.3;  —  ta  vS  mazda  ..  asäi yecä  tatbyaca'''' ärmaitl  ddi^a  insi  istsisi&A.  mit  No.  2)  xsa- %r>m  Y.$i.2.  o)durcheinenKonjunk- tionssatzmit>'<j^j  oder  Ayat,  dem  ^a  folgt; nur  gAw. :  datd?  galmcä  ajyaitimcä  (beide als  I.Glied;  Sp.567  \x^ya%aca  anhat  aps- m^m {sd.)..  Y.30. 4;  — ia'^a  ,.  zar^m (sd.) ..  carani  *ashiitm  (sd.)  xsmakqm  hyatca mSi  hyäi  Vax!  aslS  Y.  44.  17;  —  hyat vJsSnta  (sd.)  dr>gvant>m  avS  AyaÜa  gäui jaidyai  taraol  Y.32. 14.  e)  das  erste Glied  ist  relativisch  gegeben;  nur  gAw. :  yJ *u>i'qfi?m  mS'i  gairü  (sd.)  . .  dadi  asisca '  Syadiananqm  vidus  V.  28.  4.  f)  das erste  Glied  ist  nicht  ausdrücklich  genannt, vielmehr  aus  dem  Zusammenhang  zu  ergän- zen (s.  Sp,  571  u);  nur  gAw.:  ta  uxiiä  . . maeda  asaica  yufmaibya  gtml ". .  (dir),  o J/., unddem.<4j'ii.."Y.^2.9;  — /ö  d)b>naotä
12891:•  j.  darvj'ain.Jitay-  f.  'langes  Leben': Sfrinami  tava  nara  daäAupaiti  vohu.}xH us.jTti  'jUi  (soll  heissen)  "ich  segne  dich, o  . .,  mit  gutem  Leben,  mit  hohem  Leben, langem  Leben"  Az,  7;  Vyt/.
18391:'Vieh  auffüttern,  au&iehen,  Vieh  züchten"', nur  PPA.  ßuyant-  'ViehzUchter,  Freund der  Viehzucht*:  ySi  msimim  vandm  (sd.) . .  :^äü  hiiubls  /luyasü  aßuyanti  ". .  die Feinde  der  Viehzucht  unter  deren  Freun- den" 'Y.4f).ar''>;  —  nsil  »nzajySi  frajyaitis (sd.)  nsit  fsuyenlt  dngvasB  pairl  Y. 2p.  5.  a)  mit  västrya-  (sd.):  ai zl'kwa fsuyaniaila  vaslryäicä  %wSrPstä  (sd.) tatasä  Y.  29.  6;  —  at  kl  aya  ß-avantä (sd.)  västrlm  afiyai  /luyanlimY. 31.  10; Yt  10. 60.  a)  als  Bezeichnung  für  den dritten  Stand  {'pi/tra-),  'der  viehzUchtende Bauer",  geg.  a^ravan-  (Stverz.),  ra%alitar- (und  Aatay-):  ä^rava  rdSialsta  vastryS fsuyqs  hüitis  Y-ig.  17  usw.;  —  väsfrtm fluyaniim  Vr.^.  2  usw.;  —  västryai fiu-
20530:—  'r^m  .  .  haianragaoiim  .  .  bafvar».- iaimafum  ..  ai^afmm  jayaurvanhtm  Vt 70.  7;  —  °r?m  .  .  yahtnäi  mal'äia/um  frä- '^winsat . .  akurö  mazda  . .  karai^yö  paiti barfzaya  Yt  70.50;  —  surunuyä  nä  °ra yamahe  Yt  70.  32 ;  3» ;  —  usta  akmäi  ,  . yakmäi . .  zaota  asava  , ,  'rahe  vaca  yazäite rästun  ahmai  . .  °rB  ma2%anpm  Jcaraiti Yt  70. 137 ;  — yahmai .,*rB jasaiti  avaiiihe yö  baevariJpasanB  vIspB.vtövä  aiaoyamnB Yt  10.24;  —  '"'"  --yS  ■•  aivjyäiti  pasca ha  fräsm5.daitJm  . .  visptm  imat  adkäiti yal  atUan  zqm  asmattfmca  vatnm  zaslaya
=== search marəz ===
```


## [2026-09-07T17:38:42.459Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"schnellen  Räder\\|schnellen Räder\\|Rädern\\|Räder\" BRT.txt | head -10"
}
```


### [2026-09-07T17:38:42.505Z] TOOL RESULT

```
11212:•  j.  danat-Caxra-  Adj.  'mit  sausenden  (?) Rädern':  masa  xsä%ra  ..  'ra  (APn.)  YL 5.130.
```


## [2026-09-07T17:38:43.963Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SYN 367 / 215 / 969 ===\"; python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor p in (215,367,969):\n    leaf=p+24\n    print('==== printed',p,'leaf',leaf,'====')\n    print(pages[leaf][:1800])\nEOF"
}
```


### [2026-09-07T17:38:45.439Z] TOOL RESULT

```
=== SYN 367 / 215 / 969 ===
1545
==== printed 215 leaf 239 ====
roman- (b) anne piel} cave MHG har, vahs (a) Av. varasa- (2), gaona- (b) Rum. NHG _ haar
cheveu, Sp. cabello), etym. dub. Walde- P. 1.347. Ernout-M. 147. Walde-H. 158.
Lat. crinis (a, mostly pl. or sg. coll.; > It. crine ‘hair’ lit. word, Fr., Sp. crin ‘horsehair, mane’), fr. *cris-ni- : Lat. crista ‘tuft on the head of animals’, Goth. -hrisjan, OF hrisian ‘shake’, etc. Walde-P. 2.572. Ernout-M. 233. Walde-H. 1.292.
Lat. coma (a; > It. chioma lit. word, Rum. coamd ‘horse’s mane, ridge’), fr. Grk. xéun (above, 1).
For the relative frequency of Lat. capillus, coma, crinis in different au- thors, cf. Thesaurus s.v. capillus.
Lat. pilus, mostly ‘single hair on the body’ (> It. pelo, Fr. poil ‘hair of the body’, but Fr. dial. pel, Sp. pelo, Rum. par generic), perh.: Lat. pilleus ‘felt cap’, Grk. ios ‘felt’. Walde-P. 2.71.
3. Ir. folt (mostly a, but also ‘the long hair of a horse’s tail’, etc.), W. gwallt (a), OBr. guolt, all coll., prob. : OPruss. wolti ‘ear of corn’, SCr. vlat ‘blade of grass’, etc., fr. the same root as Lat. vellus ‘fleece’, lina ‘wool’, etc. Walde-P. 1.297.
Ir. find ‘a hair’, pl. finda ‘hair’, NIr. fionn ‘a hair’, fionnadh ‘hair’ (b) : Grk. tovBos ‘young hair’, OHG wint-brawa
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
204
‘eyelash’, etc. Walde-P. 1.262. Peder- sen 1.114.
NIr. gruaig ‘hair of head, or of horse’s mane’, etym.?
For still other NIr. words for ‘hair’ in special applications, cf. McKenna s.v. hatr.
W. blew, Br. bleo (both coll. with sg. blewyn, blevenn ‘a hair’), perh. fr. *ml-eu- beside *ml- in Grk. paddés, etc. (above, 1). G.S. Lane, Language 7.279.
4. Goth. tagl (‘the single hair of the head’ and once ‘camel’s hair’) : ON tagl ‘hair of horse’s tail’, OE tegl ‘tail’, etc. (4.18).
Goth. skuft (Jn. 11.2, etc. dat. sg. skufta co
==== printed 367 leaf 391 ====
ling wine’, orig.? REW 1002.
It. brocca, Fr. broc (> Br. brog), late Lat. broci, fr. Grk. Bpoxts ‘a kind of ves- sel for liquids’, deriv. of Bpéxw ‘wet’. REW 1320. Wartburg 1.549. Ven- dryes, BSL 25.40.
Fr. cruche fr. Gmce. (see below, 4).
Sp. cdntaro, fr. Lat. cantharus, fr. Grk. xdvOapos ‘large drinking-cup’. REW 1614.
Sp. jarra, jarro, Fr. jarre (> NE jar), fr. Arab. garrah ‘earthen water-vessel’. REW 3944. NED s.v. jar, sb.?.
3. Ir. cilornn, NIr. Kahres, above, 1.
NIr. criiscin, fr. ME cruskyn, this like OFr. creusequin fr. MFlem. kruyseken dim. of kruyse (NE cruse, etc., below, 4). NED s.v. cruskyn.
W. piser fr. NE pitcher.
4. The Gmc. group, ON krukka (rare), Dan. krukke, Sw. kruka, OE crog, crtice, crocca, Du. kruik, OHG kruog, NHG krug, is of obscure source (possibly some connection with Grk. kpwoods ‘water-pail, pitcher’) and shows & great variety of parallel forms, includ- ing some with s as MHG krise, MLG
ciolarn : Grk.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
348
kriis (Du. kroes ‘cup, mug’), NE cruse, etc. Walde-P. 1.487, 594, 597. Falk- Torp 583, 584.
From one or another of the Gmc. forms come Fr. cruche (cf. MHG kriche), NIt. criiscin (above, 3), Lith. kragas, OPruss. kragis, Lett. kriiza (fr. MLG kris), Russ. kruzka.
ME picher, NE pitcher (in British usage now somewhat arch. or dial., but in U.S. the usual word), fr. OF r. pichier, MLat. picdrium, bicadrium ‘a drinking- vessel’ (whence also OHG pechari, beh- hari, NHG becher, NE beaker, etc.), this fr. Grk. Bixos ‘wine-jar, drinking-bowl’, this again a loanword of unknown source. NED s.v. pitcher). REW 1081a. Weigand-H. 1.173.
NE jug, in U.S. usually denoting a large earthenware vessel with stopper and no spout, but in current Br
==== printed 969 leaf 993 ====
.  sarva-, vigva-; sarvd-, Br. pep; hol MHG iegelich, ietwelich, vigva (in pl.)
telweder, al; alle Av. _vispa-; vispa- (in pl.) NHG jeder (all); alle
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
used in the singular ’ and in the plural ady been discussed q these cover all the words (33) ae ‘all’ pl. But the use of ‘ in the singular for ‘every’ has ore or Jess displaced by other mostly of pronominal origin. these remain to be discussed here. + of them are used without the dis- igh which is now felt between NE Ed cach (a8, in fact, the OF form a Their primary sense was a each’ taken separately (that is more neatly = NE each); but, with yeakening of the distributive feeling, they encroached upon or displaced those expressions for ‘every’ in which the no- tion of totality was original. However, erain words in which the distributive gnseremained more distinctively domi- unt, like Grk. éacros, are not included here.
1,NG xe (indecl. adj.), fr. xafeis, rofyas ‘every one’, fr. Grk. xaé’éa,
«wy ‘one by one’. Hatzidakis, Mec. 2.152,
pat were ! or ‘eve
have alre {or
at Lat. quisque, sb. and adj. pron. each (one)’, ‘every (one)’, in early use ako rel, ‘whoever’, fr. interrog. indef. generalizing -que. Ernout-M.
S agus OFr. chasque, back-forma- tascun, shacun, OFr. chascun, like It. % fr. a blend of VLat. cisque i ee unus and cata unum (cf. icheg 200 i REW 6968. Gamill- oe 07. Wartburg 3.483. (h. Gk i (indeed adj.), fr. VLat. cata "hig eas cf. above, NG xaée), Ings in a: ah frequently in church writ- ‘Dutive phrases modeled on e, - caia ‘mane mane in the 8 ete. ; mansiones, cata singulos “in the Peregrinatio.
QUANTITY AND NUMBER
Digitized by Arya Samaj Foundation Chennai and eGangotri
921
Rum. fiecare, cpd. of fie sg. and pl. subj. of fi ‘be’ and care ‘who, which’ (L
```


## [2026-09-07T17:38:54.808Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"MARROW\\|4\\.46 \\|BRAIN\\|SHORT$\\|12\\.59\\|^SHORT\" SYN.txt | head -20"
}
```


### [2026-09-07T17:38:55.969Z] TOOL RESULT

```
5623:E BODY; BODILY FUNCTIONS AND CONDITIONS 215 4 ? ans OF TH 4.203 BRAIN Goth. ; Lith.  smegenys (pl.)
6498:4.46 BELLY; STOMACH
10449:4. Dan. kjole, shortened form of kjortel = ON kyrtill ‘kirtle, tunic’, fr. ON *kortr, Dan. kort ‘short’ (12.59). Falk-Torp 518.
10533:ON skyrta, Dan. skjorte, Sw. skjorta, OE scyrte (gl. praetexta, where perh. the Lat. word was misunderstood), ME sherte, NE shirt, derivs. of adj. for ‘short’, OE sceort, etc. (12.59). Falk- Torp 1007. NED s.v. shirt, sb.
14067:NIv. gearraim, fr. MIr. gerraim ‘cut off, shorten’, fr. gerr ‘short’ (12.59).
21159:SHORT
21176:CHAPTER 12 spATIAL RE b) 12.51 41 Puace (S- 12.52 fa. Por (Place, Seb “ae 12.58 013. 51 12.54 yi Lie ae 12.55 ois Stan (VD: ae 12.56 yo16 REMAIN, uaa Pere) 12.57 in17 pees 12.58 12.18 Lea : 12.59 1919 Quiet (adi) ie ; : 991 COLLECT, GATHER . ms 12.62 122 Jow, UNITE ake 1293 SEPARATE (vb-) ; 12232 DiviDE 12.64 1224 Oren (vb.) 12.65 1225 Snur, CLosE (vb.) 12.66 12.26 Cover (vb.) 12.67 1227 Hin, ConcesL 12.68 1231 Hicw 12.71 1232 Low 12.72 1233 Tor 12.73 1234 Borrot 12.74 1235 Eyp 12.75 ae Por 12.76 ee 12.77 12.36 Stop 237 Mux (adj.) Teale 12.38 CENTER 12.81 12, < 78 Ricur (adj; vs. Left) yore aa ler (adj. vs, Right) 12.83 nay Aoi (adv) 12.84 pas oe adv.) 12.85 45 Easn 9 12.46 Wesr 12.91 247 Nonny 12.92 248 Sonne 12.93 12.94 829
22538:12.59 SHORT
23604:Grk. Bpaxts ‘short’ (12.59) is also sometimes used for ‘little’ in size or quantity, and ‘few’ esp. ‘few words’, like NE in short (LS s.v.).
24297:CHAPTER 14 TIME! 14.43 ae 14.44 ay 14.45 YounG 14.46 OLD 14.47 Barty (adv.) 14.48 Late (adv.) 14.49 Now 14.51 14.52
25404:TIME 997 14.46 EVENING - Goth. andanahti Lith. vakaras loxtpm of i ON kveld, aptann Lett. sakars tor tp%y espera Dan. aften (kveld) ChSl.  veterit vespery Sw. afton, kvall SCr. _ veéer ee OE @fen : Boh.  veéer one ME even, evening Pol. wieczor : a NE evening Russ. veéer ‘ ie Du. avond Skt.  dosa-, sdya- jrathndna OHG abant Av. arazah- vin nos, WWYT MHG dbent ryardaee NHG abend part from an inherited group, of | sera, above). Pedersen 1.208. Loth, ions, words for ‘evening’ are Mots lat. 178.
32073:SCr. uskratiti, epd. of uz- (us-, Les- kien, Serbo-kroat. Gram. 69) ‘off, back’ and kratiti ‘shorten’ (also simply ‘re- fuse’) : ChSl.  stkratiti ‘shorten, end’ krattki ‘short’ (12.59), ete.
```


## [2026-09-07T17:39:03.768Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '5620,5650p' SYN.txt; echo \"=== 12.59 ===\"; sed -n '22538,22590p' SYN.txt"
}
```


### [2026-09-07T17:39:03.823Z] TOOL RESULT

```
Skt. kapala- ‘cup, bowl, potsherd’ and ‘skull’, fr. the same root as Lat. caput ‘head’. Walde-P. 1.346.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
E BODY; BODILY FUNCTIONS AND CONDITIONS 215 4 ? ans OF TH 4.203 BRAIN Goth. ; Lith.  smegenys (pl.)
byxeparhos ON hjarnt Lett.  smadzenes Gtke yas Dan. /jerne ChSl. mozgit NG cerebrum Sw. hjarna SCr.  mozak Lat, cervello OB bragen Boh.  mozek 8 cerveau ME brain, hernes (pl.) Pol. mézg Sp. ccrebro 1.) NE brain : Russ. mozg. Rum. reiert (pl. Du. _ hersenen (pl.), brein Skt.  mastigka- if inchinn OHG  hirni Ay. mastrayan- (in pl.) NIr. alae MHG herne W. Wiese NHG _ hirn, gehirn Br | emp
Most of the words for ‘brain’ are cog- 3. Ir. inchinn, W. ymennyd, Br. em- nate with words for ‘head’ or ‘marrow’. | penn, cpds. (like Grk. éyxégados) fr.
Sometimes the plural used as coll., like NE brains, is the usual form.
1, Derivs. of *her(a)s-, etc. seen in Skt. ciras- ‘head’, Grk. xépas ‘horn’, etc. Walde-P. 1.403 ff.. Ernout-M. 177. Walde-H. 1.208. Falk-Torp 410. REW 1826, 1827.
Lat. cerebrum (> Sp. cerebro, Rum. creier used mostly in pl. cerierz), cerebel- lum (>It. cervella, Fr. cerveau); ON hjarni, OHG hirni, etc., general Gme. (except English, where ME hernes, Sc. harns fr. Norse).
2, Grk. eyxébados phrase cpd. fr. & ‘in’ and xedady ‘head’.
NG yvaé, often pl. ra pvadd, fr. Grk. hueXbs, late wvadds ‘marrow’. Cf. Aris- tot. PA 65225 roddots yap kal 6 éyxépados
boxe? nuehés elvar ‘for many think the brain is really marrow’.
words for ‘in’ and ‘head’ (Ir. cenn, etc., 4.20).
4. OE bregen, ME, NE brain, Du. brein, prob. : Grk. Bpexpuos, Bpeypa “front part of the head’. Walde-P. 2.314. NED s.v. brain. Franck-v. W. 91.
5. Lith. smegenys (pl.), Lett. smad- zenes (or pl. -is), ChSl. mozgii, etc. (all the Slavic words) : Skt. majjan-, ON merg, OE mearg, NE marrow, OHG mar(a)g, NHG mark, etc., all ‘marrow’ (Av. mazga once, ‘marrow’ or ‘brain’? NPers. mayz both), root connection? For the association of ‘marrow’ with ‘brain’, see above, 2. Walde-P. 2.309.
6. Skt. ‘skull’ (4.202).
Av. mastrayan- in pl. ‘skull’ (4.202) and ‘brains’ (Yt. 10.72). Barth. 1155.
mastiska- : mastaka-
-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
216 4.204 FACE
Grk. — xpdawrov Goth. andwairpi, wlits, an- Lith. _vetdas NG Tpbcw7ro dawleizn, ludja Lett. vaigs Lat.  faciés ON andlit ChSl. lice It. Jaccia (viso) Dan.  ansigt SCr. lice Fr. visage Sw. ansikte (anlete) Boh.  tvd¥ Sp. cara (rostro) OE ansjn, andwlita Pol. = twarz Rum. fajd, obraz ME face Russ. ico Ir. agad, enech NE face Skt.  anika- Nir. aghaidh Du. —geztcht Av. ainika-, &iOra- W. wyneb OHG  gesiht, anitlutli, an- Br. dremm nuzzt
MHG  gestht, antlitze_
NHG | gesicht (angesicht,
antlitz)
The face is the most distinguishing and expressive portion of the body, and the words for ‘face’ are most commonly based on the notion of ‘appearance, look’, most of these derived from verbs for ‘see, look’, or in some cases on the no- tion of ‘form, shape’. There is some- times interchange between ‘face’ and ‘cheek’ in the same word or group.
Included in the list Gn parentheses) are some words that are synonyms of those given in first place, either popular (but not vulgar, as NE mug), as It. viso, Sp. rostro, or now restricted to a lofty style, as NHG angesicht, antlitz.
1. Grk. rpdcwzov (in Hom. always pl.), fr. wpos ‘toward’ and deriy. of é7- (IE *ok*-) in dpouat fut. of dpaw ‘see, look’, doce ‘eyes’, dp also ‘face’, etc. (15.51). Hence orig. the ‘appearance, look’.
2. Lat. faciés, orig. ‘form, shape’, then esp. ‘face’, fr. facere ‘make’. Hence, through VLat. *facia, It. faccia, Fr. face (> ME, NE face), Rum. faté (Port. face ‘cheek’, Sp. haz, faz fig.). But the use of Fr. face for the ‘face’ of a person was given up in the 17th cent. (Wart- burg 3.356). Ernout-M. 322. Walde- H. 1.489. REW 3130.
Fr. visage, fr. older vis (now only in vis-d-vis) = It. viso (pop. for faccia), fr. Lat. visus, ‘sight’. REW 9384. Gamill- scheg 893.
=== 12.59 ===
12.59 SHORT
Lith. trumpas
Lett. iss ChSl. kratiiki SCr.  kratak Boh. krdtky Pol. krétkt Russ. korotkij Skt. hrasva- scurz, skam-° Av. marazu-
s.v. and xovro-mopela prob. ‘short way’, Polyb.), adj. use abstracted (prob. first in epds.) fr. xovrés (Hom. +) ‘pole, pike, goad’ : xevréw ‘prick, goad’. Hat- zidakis, Festschrift Kretschmer 35 ff.
3. Lat. brevis : Grk. Bpaxis (above, 1). Hence It. breve, Fr. bref (> ME bref, NE brief), now mostly of time and generally replaced by the following (but It. breve also spatial beside corto).
It., Sp. corto, Fr. court, Rum. scurt (s- fr. MLat. derivs. in ex-) fr. Lat. curtus ‘gut off, broken, mutilated, shortened’ : Grk. xelpw ‘cut off, shear’, etc. Ernout- M, 248. Walde-H. 1.316 f. REW 2421.
4. Ir. gerr, NIr. gearr : Skt. hrasva-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
TT aS
Digitized by Arya Samaj Foundation Chennai and eGangotri
884 SELECTED INDO-EUROPEAN SYNONYMS
‘short, little’, Grk. xepelw» ‘poorer, worse’, Ir. gair, garait ‘short (of time)’, etc. Walde-P. 1.604f. Pedersen 1.83.
Ir. cumbair, cummair, berr (K. Meyer, Contrib. 206), W. byr, Br. berr, OCorn. ber (gl. brevis) cf. Ir. cuimre ‘shortness’, Ir. berraim ‘shear, clip’, root connec- tions? Walde-P. 2.160. Walde-H. 1.107 (Lat. birrus, loanword).
5. ON skam(m)r, OHG skammeér, be- side OHG hammér ‘mutilated, feeble’, perh. fr. *(s)kap-mé- : Grk. oxarrw ‘dig’, xor7w ‘strike, cut off’, ete. Walde-P. 2.560. Or fr. *skambh-no- : Av., OPers. kamna- ‘small’ in quantity or number? Walde-P. 2.601. Falk-Torp 1003.
Dan., Sw. kort, Icel. korir, Du. kort, OHG churz, kurt, churt, MHG, NHG kurz, prob. fr. Lat. curtus (cf. It. corto, above, 3). Falk-Torp 568. Weigand-H. 1.1179.
OE sceort, ME schort, short, NE short, OHG scurz: ON skort, skorir ‘lack’,
skorta ‘be lacking’, OE sceortian shorter, be lacking’) MHG
‘become
king Scherze, scherzel ‘cut off piece’, etc., fr. an exten-
sion of the IE root *(s)ker- in Lat. cur. tus, etc. (above, 3). Falk-Torp 1019 NED s.v. short. ‘
6. Lith. ¢trumpas : trupiti ‘crumble break in fragments’, trupus ‘brittle’, OPruss. irupis ‘block of wood’, Grk. tputaw “perforate, bore’, ete. Bezzen- berger, BB 27.142. (Walde-P. 1.732),
Lith. jsas, ysas (NSB, but prob. obs.), Lett. iss, OPruss. (acc. sg.) insan, etym.? Mihl.-Endz. 1.837. Trautmann, Alt- preuss. 346.
7. ChSI. kratiékd, ete., general Slavic : ChSI. sii-kratiti ‘shorten’, Russ.-ChS]. critu, crésti ‘cut’, fr. the root in Lat. cur- tus, OE sceort, etc. (above, 3, 5). Berne- ker 576f. Walde-P. 2.579.
8. Skt. hrasva- : Ir. gerr (above, 4). Av. marazu- : Grk. Bpaxts (above, 1).
12.61 WIDE, BROAD
Grk. — xAarts, ebpts Goth. braibs Lith. platus
NG tAatts, papdbs ON bretdr, vidr Lett. plats
Lat. latus Dan. bred, vid ChSl. Srokit
It. largo Sw. bred, vid SCr. Sirok
Fr. large OE° brad, wid Boh. &Siroky
Sp. ancho ME brood, wid Pol. _—szeroki Rum. lat (larg) NE wide, broad Russ. Srokij
Ir. lethan, fairsiung Du. _ breed, wijd Skt. prthu-, uru- NIr. — leathan OHG breit, wit Ay. poradu-, padana- W. Ulydan, eang MHG breit, wit
Br. ledan NHG breit
Words for ‘wide, broad’ rest on the more general notion of ‘spread out, spa- cious, extensive’, and the specialization to extent in a given direction, that is ‘wide’ in distinction from ‘long’ and the opposite of ‘narrow’, is only partial. For all of them may also be used in the more general sense. In the two Gmc. groups represented by NE broad and wide the wider sense is generally stronger in the Second group, and dominant in NHG
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
weit, which is no longer used as the oppo- site of eng ‘narrow’, while, conversely, NE wide is the technical term in actual measurement (e.g. siz inches wide by three feet long).
1. IE *pjtu-, *pjino-, etc., fr. an ex tension of *pel- (*pela-, *pla-, etc.) De words for ‘spread out, flat’ as Lat. pla- nus ‘flat’, ChSI. polje ‘field’, OB feld ‘field’, ete. Walde-P. 2.99f., 61f. Thurneysen, Gram. 129, 131.
polly lethan, Nit. leathan,
ork. teal 1 an (beside W. led, Be
f. llyda ns Lith. platus, Lett. plats; spread ny. poragu-; Arm. lian.
+yru-, etc., root con-
(in cpds. as vouru- bays’, vouru-gao-
yal (possessiD 3 Byz, NG gapdis, orig. dub. G. Meyer Neugr. Stud. 4.94, connects with NG dial. papéos ‘large (meal-)bag ; jggnword fr. Ital. fardo or its source Amb, farda ‘bundle of goods’. Hatzi- dakis, Mec. 2.29, suggests deriv. fr, digpadts with semantic extension through ‘copious in speech’ > ‘wide’ in gneral. But the actual use of the rare dgpadjs connotes skill, rather than
copiousness, of speech.
4, Lat. latus (> Rum. lat), prob. fr. ‘ulatos (cf. stlatta, Festus) : ChSl. sttlati ‘spread out’, stelt, postelja ‘bed’. Walde- P, 2.643, Ernout-M. 527f. Walde-H. 1.172,
Tt. largo, Fr. large (Rum. larg ‘exten- Sve, spacious’, but under influence of Fr. large Sometimes used for lat ‘wide’, cf. Tiktin s.v.), fr. Lat. largus ‘abundant, ‘pious’, etym.?  Ernout-M. 524. Walde-H. 1.764. REW 4919,
DP. ancho, fr. Lat. amplus ‘large, spa-
SP ATIAL RELATIONS: PLACE, FORM, SIZE
Digitized by Arya Samaj Foundation Chennai and eGangotri
885
cious, abundant’, etym.? Ernout-M. 47. Walde-H. 1.42. REW 4380.
5. Ir. lethan, etc., above, 1.
Ir. fairsiung, W. eang ‘broad, ample’, epds. (Ir. for-ess-, W. ess-) of *enghi-, etc. : OE enge ‘narrow’, etc. (12.62). Walde- P. 1.62. Pedersen 2.10.
```


## [2026-09-07T17:39:04.394Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"marrow\" SYN.txt | head -20"
}
```


### [2026-09-07T17:39:04.442Z] TOOL RESULT

```
5619:7. Skt. mastaka-, Av. mastrayan- (in pl.), prob. : Skt. majjan- ‘marrow’, ChSl. mozgti ‘brain’, etc. (4.203). Walde-P. 2.309.
5625:Most of the words for ‘brain’ are cog- 3. Ir. inchinn, W. ymennyd, Br. em- nate with words for ‘head’ or ‘marrow’. | penn, cpds. (like Grk. éyxégados) fr.
5630:NG yvaé, often pl. ra pvadd, fr. Grk. hueXbs, late wvadds ‘marrow’. Cf. Aris- tot. PA 65225 roddots yap kal 6 éyxépados
5631:boxe? nuehés elvar ‘for many think the brain is really marrow’.
5634:5. Lith. smegenys (pl.), Lett. smad- zenes (or pl. -is), ChSl. mozgii, etc. (all the Slavic words) : Skt. majjan-, ON merg, OE mearg, NE marrow, OHG mar(a)g, NHG mark, etc., all ‘marrow’ (Av. mazga once, ‘marrow’ or ‘brain’? NPers. mayz both), root connection? For the association of ‘marrow’ with ‘brain’, see above, 2. Walde-P. 2.309.
7091:Goth. smarna (only nom. pl. smarnos for oxiBada ‘refuse, dung’), prob. : ON smjor, OF smeoru, OHG smero ‘grease, fat’, Ir. smiur, W. mer ‘marrow’ (seman- tic development as in NHG schmierig, Du. smerig ‘greasy’ > ‘filthy, dirty’). Walde-P. 2.690. Feist 439.
9319:OE méarh ‘marrow’ (: ON mergr, Skt. majjan-, Av. mazga- ‘marrow’, ChSI. mozga ‘brain’, etc. Walde-P. 2.309) once glosses Lat. lucanica, but there seems to be no confirmation of this use for ‘sau- sage’. NED s.v. marrow.
9727:4. ON smjor, Dan. smgr, Sw, Smér, OHG chuo-smero (lit. ‘cow-grease’) : Goth. smairpr ‘fat’, OF smeoru, OHG smero ‘fat, grease’ (NI smear), Ir. smir ‘marrow’, ete. Walde-P. 2.690f. Falk- Torp 1086 f.
11413:ON smyrsl, OE smyrels (Dan. smérelse ‘grease’, Sw. smérjelse ‘unction’) : ON smyrva, smyrja, OF smierwan ‘anoint’, ON smér ‘butter, fat’, Ir. smiur, W. mer ‘marrow’, etc. Walde-P. 2.690f. Talk- Torp 1086 f.
```


## [2026-09-07T17:39:14.865Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"QUICK, FAST\\|14\\.23\\|SWIFT\" SYN.txt | head -10; echo \"=== 367 area ===\"; grep -n \"^SELECTED INDO-EUROPEAN SYNONYMS\" SYN.txt | head -3"
}
```


### [2026-09-07T17:39:14.927Z] TOOL RESULT

```
14555:5. Lith. spausti : Grk. orebdw ‘urge on, hasten’ (14.23), Walde-P. 2.659. Traut- mann 273 f.
24294:yl 42 14.13 44 4.15 14.16 417 14.18 1419 421 14.22 14.23 14.24 14.25
24641:14.21 SWIFT, FAST, QUICK
24717:NE speedy, Du. spoedig, fr. sbs. NE speed, Du. spoed ‘speed’, orig. ‘success’, as OE spéd, OHG spuot, beside vbs. OR spowan, OHG spuon ‘succeed’ : ChSI. spéti ‘succeed’ (also spésiti, etc. ‘hasten’ (14.23). Walde-P. 2.657. Franck-y. W. 648. NED s.v. speed, sb.
24721:OHG sniumi (sniumo, sliumo, adv.), MHG sliume, sniume (OE snéome adv.) : Goth. sniumjan, sniwan, OE snéowan ‘hasten’ (14.23).
24742:8. Skt. tvarita-, Av. @waga- (*twarta-) : Skt. évar- ‘hasten’ (14.23). Walde-P. 1.749.
24743:Skt. ¢ighra- : Russ. sigat’, signut’ ‘Sump’. Walde-P. 1.363 (but for OE higian, NE hie, see 14.23).
=== 367 area ===
518:SELECTED INDO-EUROPEAN SYNONYMS
1335:SELECTED INDO-EUROPEAN SYNONYMS
1579:SELECTED INDO-EUROPEAN SYNONYMS
```


## [2026-09-07T17:39:17.375Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '24641,24700p' SYN.txt | head -60"
}
```


### [2026-09-07T17:39:17.431Z] TOOL RESULT

```
14.21 SWIFT, FAST, QUICK
Grk.  raxbs, dxbs, Bobs, dtbs Goth. sprauté (adv.) Lith. greitas, skubus
NG "YPiyopos, -yAjyopos ON Sjotr, skjotr, hradr, Lett. dlrs, 2igls
Lat. _celer, véléx, citus, ra- snarr ChSl.  skorit; jedro, _brtzo pidus Dan. = rask, hurtig, snar (advs.)
It. rapido, presto, veloce Sw. snabb, snar, rask SCr. — brz, hitar
Fr. rapide, vite (adv.) OE hrad, swift, snel(l) Boh. = rychly
Sp. rapido, presto, veloz ME swift, rad, snel, spede Pol. predki, szybki
Rum.  repede, iute NE fast, swifl, quick, Russ. bystryj, skoryj, Sibkij
Ir. dian, liiath, crib specdy Skt.  dgu-, tvarita-, gighra-,
Nir. luath, tapaidh Du. vlug, snel, gauw, java(na)-
W. buan, cyflym, chwyrn, ras(ch), spoedig Av. dsu-, aurvant-, Owa- clau OHG  sniumi, (h)rad, snel, §a-, xSviwra-
Br. buan, herrus rasc
MHG nel, rasch, sliume, geswinde
NHG schnell,
rasch,
geschwind
There is a wealth of words denoting rapid motion (besides those listed, e.g. NE rapid, NHG schleunig) from which it is not always easy to select the most generic and usual and between which the choice is too idiomatic, according to the context, to permit any generaliza- tion. NE swift or the now more com- mon fast may apply to rapid motion of
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
any duration, while in quick (in accord- ance with its original sense of ‘live, live- ly’) there is a notion of ‘sudden’ or ‘soon over’. We speak of a fast horse or run- ner in a race, a quick starter but not 2 quick horse, A somewhat similar feeling may distinguish NHG schnell and rasch, or it may be more a matter of local preference (for which cf. Kretschme?,
385). And so in the other
porte : he could show the differentia-
yngn0Bes 6 quoting phrases in great
tion ©
pon marti sources are too diverse pee
psunman”  walde-P. 1.172. Er-
LM. 696. Habs (D0et:)
kt. Gou-, Av. asu-; Grk. Skt. agu-,
s ‘swifter, swiftest’ ;
ow di-auc,
f t swift’). . ‘ ) Bi Grk. taxis, beside raxos ‘speed’,
tquickly, soon, at once’, etym. dub.
axa is S. Lane, Language
poisae 946. Ge
1. Las fobs (poet.) : 0 ‘run’, ete. (10.46). Boisacq 342 f.
Gtk. dfs ‘sharp’ (15.78), but also (post- Hom., Hadt., etc.) ‘swift’.
Byz., NG -ypnyopos, pop. YAjyopos, through ‘prompt, ready’ (and perh. first in ady. ypiyopa), fr. Grk. éypyyopa ‘am awake’, perf. of éyelpw ‘awaken’.
3, Lat. celer: Grk. xédAns_  ‘courser (horse), fast sailing ship’, xédouar ‘drive on, incite’, Skt. kal- ‘drive’, ete. Walde- P1443. Ernout-M. 170. Walde-H. 1194 f, Tat. vélox (> It. veloce, Sp. veloz), cf. ‘ight-armed infantryman’, etym. oa perh. (*weg-slo-) fr. the root of he Move, excite’, vegetus ‘live, ani- XE Ae the semantic development of quick, below, 5); or (*wegh-slo-) :
teher, ta itgg, “Ve, transport’?). Emout-M.
La’ .
Sn oe Pple. of ciére ‘set in motion, Emout-y ae Klow ‘g0’, KUvew ‘move’.
Tat saa f. Walde-H. 1.213 f.
Rum, ae ‘< (> It. rapido, Sp. rdpido, Orig, yi &; Fr, rapide > NE rapid), f gyi cent tearing away’ (esp. "ateh Owing currents), fr. rapere
» Car Sf, REW ae plunder’. Ernout-M.
Digitized by Arya Samaj Foundation Chennai and eGangotri
TIME 967
It., Sp. presto (Fr. prét ‘ready’), fr. late Lat. praestus fr. adv. praestd ‘at hand, ready’ (14.29). REW 6726.
Fr. vite (adv., but until 17th cent. also adj.), OF r. viste : It. visto, vispo ‘quick, brisk, smart’, prob. of imitative orig. ee 9379a. Otherwise Gamillscheg
Rum. iute, also ‘violent, impetuous’, fr. the Slavic, cf. ChSl. Yjuté ‘cruel, fierce’, etc. Tiktin 862.
4, Ir. dian, beside déne ‘swiftness’, prob. : Grk. dtw ‘flee’, Skt. di- ‘fly’, ete. Walde-P. 1.775.
Ir. laath, NIr. luath, also Ir. luam id., beside luas ‘speed’, fr. lu- ‘move’ (10.11).
Ir. crib (cribb, crip), etym. dub. Pe- dersen 1.161. Walde-P. 1.472, 2.568.
NI. tapaidh = Gael. tapaidh ‘clever, active’ : NIr. tap ‘a start or fight, an accident’ (Dinneen), orig. dub. Possibly fr. a vbl. cpd. *to-ad-ben- : benim ‘strike’ (cf. Olr. taipe ‘epitome’, Pedersen 2.461).
W., Br. buan, etym. dub. Pedersen 2.56. Henry 47. Loth, RC 36.148.
W. cyflym, epd. of lym ‘sharp, keen’ (arch. also ‘quick’, cf.; Spurrell, s.v.) = Br. lemm ‘sharp’, etym. dub. Walde-P. 2.391, 435.
W. chwyrn, often with implication of a whirring sound (Evans, s.v.; ef. chwyr- nu ‘whiz, whir, snore’), prob. based on an imitative syllable, like that in Skt. svar- ‘make a sound’, Lat. susurrus ‘hum- ming’, NE swearm ‘swarm’, Walde-P. 2.528 (adversely). Loth, RC 23.117. Morris Jones 146 (: Skt. sphur- ‘jerk, dart’; improbable).
W. clau : Ir. clé ‘whirlwind’, root con- nection? Loth, RC 38.159.
Br. herrus, fr. herr ‘speed, impulse’, older err, fr. OFr. erre ‘journey, way, course’ in phrases like de grant erre, de bonne erre, etc. (cf. Godefroy, s.v.). Henry 116.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
ay aa yy ;
an .
```


## [2026-09-07T17:39:22.611Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '24700,24760p' SYN.txt"
}
```


### [2026-09-07T17:39:22.658Z] TOOL RESULT

```
an .
a4
Digitized by Arya Samaj Foundation Chennai and eGangotri
968 SELECTED INDO-EUROPEAN SYNONYMS
5. Goth. sprautd, adv. (renders zaxi, raxéws, etc.) : OE G-spriian, spryitan ‘sprout’, MHG spriezen id., W. ffrwst ‘haste’, Lett. sprausties pruojam ‘clear out’. Walde-P. 2.671. Feist 446.
ON jijotr : fiyota ‘float’, etc., Grk. rréw ‘sail, swim’ (cf. Ir. liath, above, 4). Falk-Torp 242.
ON skjotr (OE scéot ‘quick, ready’ not common) : skjota, OE scéotan, etc. ‘set in motion, shoot’, Skt. cud- ‘drive, press’. Walde-P. 2.554. Falk-Torp 1045.
ON hradr, OE hrad, hrep, ME rad, OHG (h)rat, (h)rad : Lith. api-kratai ‘quickly’, krésti ‘shake, shake out’, kretétt ‘move back and forth, waver’, Ir. crothaim ‘shake’. Walde-P. 1.484. Falk- Torp 870.
ON snarr ‘swift, keen’ (of eye, etc.), Dan., Sw. snar, lit. ‘twisted tight, hard- pun’ (of a cord), so rarely ON snarr (cf. Vigfusson, s.v.):ON snara ‘twist, wring, turn quickly’. Walde-P. 2.701. Falk-Torp 1090. Hellquist 1011.
Dan. hurtig (Sw. hurtig ‘cheerful, brisk, agile’), fr. NHG hurtig ‘brisk, quick (at work), alert’, deriv. of MHG hurt ‘shove, drive’ fr. OF r. hurt ‘shove’. Falk-Torp 433.
Sw. snabb, prob. : MHG snaben ‘hur- ry’ = snaben ‘snap, hop, jump, shove, etc.’, beside snappen ‘snap’, NE snap, ete., all fr. a Gme. *snab-, *snap- indi- cating various types of quick motion, but root connection dub. Hellquist 1009 f. Falk-Torp 1089 f.
OE-NE swift : OF swifan ‘move, sweep’, ON svifa ‘swing, turn, drift’, OHG sweibon ‘sway, swing’, etc. Walde- P. 2.520. NED s.v,
OE snel(!), ME snel, Du., OHG, MHG snel, NHG schnell : Sw. snail ‘good, nice’, older ‘quick, capable’, Dan. snild ‘shrewd’, root connection dub. Falk-Torp 1096. Weigand-H. 2.764.
NE quick, in this sense rarely also ME
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
but mostly ‘vigorous, lively, alive, ete? OE cwicu ‘alive’ : ON kvikr, OHG oy,’ Lat. vivus, etc. ‘alive’. NED 8.v,
NE fast, orig. as still also ‘firm’, fy OE fest ‘firm’: ON fastr, OHG festi. NHG fest, etc. ‘firm’. The sense of ‘swift’ (for which it is now the Pop. word) seems to have developed first in the ady. (quoted in NED from 1205) in phrases like run fast (cf. run hard), NED s.v.
NE speedy, Du. spoedig, fr. sbs. NE speed, Du. spoed ‘speed’, orig. ‘success’, as OE spéd, OHG spuot, beside vbs. OR spowan, OHG spuon ‘succeed’ : ChSI. spéti ‘succeed’ (also spésiti, etc. ‘hasten’ (14.23). Walde-P. 2.657. Franck-y. W. 648. NED s.v. speed, sb.
Du. vlug, fr. MDu. vlugghe ‘able to fly’: Du. vliegen, NHG Sliegen, etc. ‘fly’. Franck-v. W. 752.
Du. gaww, MDu. ga: OHG gahi ‘sudden, hasty, quick’ (NHG jah ‘abrupt’), etym. dub. (ablaut form with prefix ga- to Grk. dts, ete., above, 1?). Walde-P. 1.172. Franck-v. W. 176f.
OHG rasc, MHG, NHG, Du. rasch (MLG > Dan., Sw. rask), with ME rasch (rare), NE rash ‘hasty, impetuous, reckless’ (loanword?, cf. NED), fr. Gme. *raska-, perh. *rad-ska- : Ir. re- thim ‘run’, Skt. ratha- ‘wagon’, etc. Walde-P. 2.368. Falk-Torp 882.
OHG sniumi (sniumo, sliumo, adv.), MHG sliume, sniume (OE snéome adv.) : Goth. sniumjan, sniwan, OE snéowan ‘hasten’ (14.23).
MHG geswinde (also ‘bold, violent’), NHG geschwind, epd. of MHG swinde, swint ‘strong, mighty, vehement’ : OF swip, OS swid ‘strong, vehement’, Goth. swinps ‘strong, sound’. Walde-P. 2.525. Weigand-H. 1.702. ;
6. Lith. greitas : Lett. greits ‘lively; angry, grim’, etym.? Miihl.-Bndz. 1.647.
Quec,
5, beside skubintis ‘hasten’ jith. 8 niuban ‘reject’ (lit. ‘shove fo etc. ‘shove’. Walde-P. oui ae Lith. dial. otu ‘swift’, perh.
Jett. cas ‘acer, Sa8aX, celer’, OE , 4 uickly, at once’, OS adro ‘hastily, early’ Walde-P. 1.118. Zupit- KZ 37,406 Jett. Zigls, gglus “ively”
‘perh. loanword fr. Lith. (old or dial.), beside zygzs i, tur, journey’. Miuhl.-Endz. 4.809.
Jett. drizs, etym.? Mihl.-Endz. 1.501.
7, ChSl. skorit, Russ. skoryj, prob. : Grk. oxalpw ‘jump, hop, dance’, MHG her(e)n ‘hasten’, NHG_ sich scheren ‘olear out’, etc. Walde-P. 2.567.
Russ-ChSl. jadri (ChSI. only ady. jedro ‘raxb, Taxes’), ‘swift’ fr. ‘strong’, ef, Bulg. (j)éduir ‘strong, capable, pithy’, Cr, jedar ‘full, strong’, prob. also Russ.- ChSI. jadro ‘kernel, testicle’, etc., all fr. am orig. sense ‘swollen’ : Grk. oldaw ‘nell’, etc. Walde-P. 1.166. Berneker 455 f,
ChSI. brizo (adv., Russ.-ChSl. bdrzyji ‘Swift, brave’), SCr., Slov. brz, Bulg. biitz, etc. (general Slavic, but the usual vord only in South Slavic; as adv. Boh. = quickly, soon’), perh. as orig. ‘in Ae a Bpaxts, Lat. brevis, etka: 3 0 achek, KZ 64.264 f. (vs. oe Ble ‘dexterous’ : ChSl. Chs}, “ae etc. fr. the root in ‘ize, a ae a SCr. hitati tte, Bameker ite , hitjeti ‘hasten’, Tychto oad op rychty ‘early’, adv.
» dvuss. rychlyj ‘porous,
light’) . B ‘Boh. ruch ‘stir, commotion’,
TIME
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
969
Pol. ruch ‘motion’, Russ. ruch ‘unrest, motion’, etc. Walde-P. 1.142, 2.356.
Pol. predki : prad ‘swift stream’, Russ. prjadat’, ChSl. predati ‘jump’. Briickner 436. Walde-P. 2.676.
Pol. szybki, Russ. sibkij : Russ. Hbat’ ‘throw’, Skt. ksip- ‘throw, hurl’, ksipra- ‘elastic (of a bow), quick’. Walde-P. 1.501. Briickner 559.
Russ. bystryj (ChSI. bystr% Supr. = ebrpexns ‘skilful, ready’, Russ.-ChSl. ‘swift’; SCr. bistar, Boh. bystry, Pol. bystry, mostly ‘clear, quick-witted, etc.’) perh. : ON bysja ‘gush forth’, Norw. buse ‘pitch, fall head first’, etc., Russ. buchnut’ ‘swell’, etc. (cf. ChSl. gedro : Grk. olé4w, above). Walde-P. 2.118 f. Berneker 113.
8. Skt. tvarita-, Av. @waga- (*twarta-) : Skt. évar- ‘hasten’ (14.23). Walde-P. 1.749.
Skt. ¢ighra- : Russ. sigat’, signut’ ‘Sump’. Walde-P. 1.363 (but for OE higian, NE hie, see 14.23).
Skt. java-, javana- : ju- ‘drive on, in- cite, etc.’, mid. ‘hasten’, Av. jav- ‘has- ten’, etc. Walde-P. 1.555. Barth. 504. Wackernagel, Altind. Gram. 1.161.
Skt. dgu, Av. dsu, above, 1.
Av. aurvant-, aurva- : Skt. arvat- ‘rac- ing’, OE earu ‘quick, active, ready’, ON orr ‘ready, swift, liberal’, prob. fr. the root in Skt. rnoti ‘rises, moves’, Grk. Spvoue ‘stir, urge, rouse’, etc. Walde-P. 1.141.
Ay. xsviwra-, cf. xéviwi-vaza- ‘going swiftly’, zsvatwayat- astra- ‘swinging the whip swiftly’, prob. : ON svipa ‘swoop, move quickly, whip’, ete. Cf. OB swift fr. a parallel root (above, 5). Barth. 561, IF 9.274f. Walde-P. 1.241.
\
Digitized by Arya Samaj Foundation Chennai and eGangotri
970 SELECTED INDO-EUROPEAN SYNONYMS
14.22 SLOW (adj.)
Grk. adbs Goth. (Jats) Lith. — létas, palengya
NG a Bpadis; &yaXca, ON seinn, latr Lett. léns Patengua (ady,) ovyé (advs.) Dan.  langsom, sen ChSl.  madinit, hitstni,
Lat. _tardus, lentus Sw. sakla, ldngsam, trég SCr. spor
It. lento OE let, s@ne Boh. — zdlouhavy
Fr. lent ME slow, lat Pol. powolny
Sp. lento NE _ slow Russ. medlennyj
Rum.  incel Du. langzaam Skt. manda-
Ir. mall OHG laz, tragi, langseimi Av. a
NIr. mail MHG trege, seine, lanc-
```


## [2026-09-07T17:39:32.443Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9300,9325p' SYN.txt; echo \"---- page markers near\"; awk 'NR>9250 && NR<9400 && /^[0-9]{3} SELECTED|SYNONYMS$|FOOD|^[0-9]{3}$/' SYN.txt | head"
}
```


### [2026-09-07T17:39:33.685Z] TOOL RESULT

```
(4) Phrases. Grk. Bée(e)ov xpéas (quot. able only in pl.; the sg. would be ‘piece of beef’; cf. dpveca xpéa, ete.), It., Sp Rum. carne de bue, de vaca, de vitit r¢. spectively, W. cig eidion, OR hrveren fl@sc (cf. NED sv. rotheren), Lett. versu gal’a.
2. Ir. martfedil, NIr. mairtfheoil, epds, of word for ‘flesh, meat? with mart ‘the carcass of an ox or cow slain for food? (cf. Laws, Gloss. s.v.), orig. ‘dead body’, fr. the root in marbh, Lat. mortuus ‘dead’ (4.75). Loth, RC. 41.56.
There are some names for meats that are from a different source, the result of specialization, as for example:
The old Gme. word for ‘flesh, meat? is specialized to ‘pork, bacon’ in the Scand, languages, as ON, Dan. flesk, Sw. flask,
A word denoting a certain part of any animal may be used specifically for the meat of that part of a particular animal, So words for ‘ham’ mainly that of swine, as NE ham, once ‘hollow back of the knee’, ‘back of the thigh, buttock’ (ef. NED s.v.), NHG schinken (: schenkel ‘thigh’), Fr. jambon (: jambe ‘leg’), Russ. okorok (: SCr. krak ‘thigh’), etc. Cf. also NE bacon (: back), NHG speck ‘bacon’ (: OE spic ‘fat, fat meat or ba- con’, etc.).
yoo a *¢nrGes, *aAda- NAGS fr. : 3 ee
1, ane a Doric orig., with aha eS BAAnv’ -AaXavor" "Tradot) " on Italic dialect form of "tp 1 Kretschmer, Glotta
see below, 2. ae amen, fr. farcire ‘stuff’.
2 ee is (also -cus, -cum, and St ate q kind of sausage invented by ae nians. Hence dialect words in aaa Italy, etc. and NG ovxavixo. rmout-M 563. REW 5134. G. Mey- er, Neugr. Stud. 3.39. aN Lat, botulus (source of Fr. boudin? REW 1192. Wartburg 1.423), loan- yord from an Osc.-Umbr. dial. (with labial for orig. labio-velar, as in popina, etc.) ; Goth. gipus ‘belly, womb’, Grk. yiadoy ‘hollow’, etc. Walde-P. 1.560, 671. Ermout-M. 116. Walde-H. 1.112. It. salsiccia (> Sp. salchicha), OFr. saussiche (> ME sausige, NE sausage), Fr, saucisse, W. selsig, Br. silzig, fr. late Lat. salsicia (neut. pl. > fem. sg.), prob. cpd. of salsus ‘salt’ and (in)siciwm Tmincemeat’. REW 4551. Gréber, a lat. Lex. 3.272 f. Loth, Mots lat.
NG JountviKo,
Rum. cirnat, fr, VLat. *carndceus a of meat’, REW 1701. Puscariu 3, Ir. mar, dim, maroc, NIr. marég,
loanword fr, ON . m Meyer, RC 12.461, Se SAIS Ue
‘m 37
> AND DRINK; COOKING AND UTENSILS
Digitized by Arya Samaj Foundation Chennai and eGangotri
367
4, ON morbjtiga, cpd. of morr ‘fat, suet’ (by-form of smor ‘fat, butter’ : OF smeoro ‘fat, suet’, etc. Falk-Torp 1086) and bjtiga (also once ‘sausage’) : bjugr ‘crooked, bent’, etc.
Dan. pélse : LG pole, Du. peul ‘pod, husk’, NE pulse (otherwise NED), Lat. bulla ‘knob’. Hence ‘sausage’ fr. its pod- like container. Falk-Torp 863.
Sw. korv, Norw. kurv: Norw. dial. kurva ‘to bend, crook’. Falk-Torp 597. Hellquist 501.
OE méarh ‘marrow’ (: ON mergr, Skt. majjan-, Av. mazga- ‘marrow’, ChSI. mozga ‘brain’, etc. Walde-P. 2.309) once glosses Lat. lucanica, but there seems to be no confirmation of this use for ‘sau- sage’. NED s.v. marrow.
OHG-NHG wurst, Du. worst, etym. disputed, but prob. a deriv. of OHG werdan, etc., in its orig. meaning ‘turn’ (Lat. vertere, etc.), applied to the bent roll of a sausage, like ON bjaga and Sw. korv (above). Other views in Weigand- H. and Kluge-G. s.v.
5. Lith. degra, Lett. desa, etym.?
SCr. kobasica, Boh. klobdsa, Pol. kietbasa, Russ. kolbasa, perh. a loanword, through Jewish butchers, fr. Hebr. kol- basar ‘all kinds of meat’. Berneker 542.
Boh. jétrnice, orig. ‘liver-sausage’ (fr. jatra ‘liver’), now generalized at the ex- pense of klobdsa.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Sse eeaEs kar saa
---- page markers near
365
366
SELECTED INDO-EUROPEAN SYNONYMS
367
368 SELECTED INDO-EUROPEAN SYNONYMS
370 SELECTED INDO-EUROPEAN SYNONYMS
371
```


## [2026-09-07T17:39:40.703Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('npages',len(pages))\nfor i in (103,104,105):\n    print('==== idx',i,'====')\n    print(pages[i][:2500])\nEOF"
}
```


### [2026-09-07T17:39:42.151Z] TOOL RESULT

```
npages 553
==== idx 103 ====
[pdf page 104]
-۰۱- مغز در سرکردن
مغاك ۱ - بنتح اول بر وزن هلاکه . کونند .
بمعنی گودال است خواء درزمین وخواه غیرزمن مغل - بفتح اول و سکون نانی و دال
باشد . . ابجد , علف شیرانر! کوبند و بعربی . لفا
مغالد ظلمت - کنایه از زمین است | البری(۳)خوانند ی ی کویت
- وکنایه از جد وقالب آدمی همست و آلر! | مغد پادنجان است 9 ؛ وبستی دیگ رگوبند نوعی
مغفالد ظلمت خالك (۱) میگویند. کماه كوچك باشد ‎٩‏ .
مغاك غار - بکرئاك وغن نقطه‌دار مغر - با رای قرشت بروزن محمود,
بالف کشیده وبرای قرشت(۲) زده ,کنایه ازکور | بلفت بربری نوعی از کماه كوچك باشد .38
وقبن باشد. . مغز بردن - بنم بای ابجد , کنایه از
مغان - یم اول جمع مغ است یمنی بسیا رکفتن ودرد سر دادن باشد .
آتش‌پرستان۴ سو نام ولایمی‌هم‌هست از آذربایجان مغز آر کردن - بفتح تای قرشت .
وموغان نام شهر آن ولایت است ۳ . کنایه از حرف زدن و سخن کردن باشد .
مغانه ۴ - بنم اول بر وزن دوکانه ۰ مغز در در کردن - کدابه از
طرز و روش وقاعده و قانون وآدابآتش‌پرستادر! | خاموش شدن و سکوت ورزیدن باشد.
‎٩([‏ خم۲:۱ج هم : () خم۱: برای‌بی‌قطه - ۳( خم۱: تفاح‌البری .
۹ - از : مغ ( بفتح اول ) (ه.م.) ۳ آ که ( پسوند ) . رك : اسشق ۹۸۵ . در اوراق
مانوی ( پارتی ) 28148 ( سوراخ, غار ) ۳ 13288848 ۰ در فارسی 6اه طق228 ( تبدیل کل
فارسی به 18 - , رك : 3837722 از اوستا -331080]2 ( هر چند که معنی فرق میکند )
(85. 0 را و 13 , 35085 ...86۲828 6ا۵ ۸۸:۵ 01 اعزا ۸ معصندع0)
۲ -رك :مق ای - مغان ازنوابع اردبیل در کنار رود ارس واقع ومکن‌طوایف
شاهون است. نادرشاه افشار درین‌محل بلطنت انتخاب‌شد « کیهان . جغرافیای‌طبیمی ص۱۹۷ ۹ +
رك: موغان . ۴ - از : مغ(ه. م.) ۳ آنه ( پوند دسبت ). می‌مغانه » باده پروردة مغان :
در خانقه نگنجد اسرار عفقبازی جام می مغانه هم با مغان توان زد .

« حافظ شیرازی ص ۱*۶۵ *.

رك : مزدسناص ۲۹۹ ببعد - 9 - (عر) «المغذ » البانجان » « اقرب‌الموارد» «مشد,
بادنجانت. وثمرلفاح بری‌را نیز نامند.» «تحقةٌ خکیم‌مومن » . ‎٩‏ - رك : هفرود.

مغر - بفتح اول » اوستا -1332288 ( دماغ ) « بارتولمه ۱۵۹ > ۰ پهلوی 32828
« بر که س ۱4۸ > هندی‌باستان 13880 (مغز), استی (ع؟) ۳8802 ۰ بلوچی328208.
سریکلی 21208 ( استخوان مغز ) » 130802 , شغنی 132807 ( مغز ) که همه عازیتی
هستند « اسشق ۹۸۹ ۰ ۰ افقانی 33881028 ( مغز ) (مفردوجمع) « «وبشمان ۹۸۹ > ؛کردی‌ع
2 * ژابا س 2*۲ > ؛ در اوراق عمانوی ( پارتی ) 17388 (مغز) . رك : پارسی میانه زع880»
ازاوستا 508788 (1,0.85 ,83505,126 ...۳۵۲5128 ۸۸104016 0۶ 191 ۸ ,ق2(5ع11)
ماد عسبی ارمی که در جمجمه قرار دارد و مرکز احاسات و مبداً حرکات آرادی میباشد +

روز کی چند پاش » تا بخورد خاك مغز سر خیال اندیش. «کلتان س ۵۱ >
- مادهٌ لرمی که در درون چیزی مخت باشد مانند منز کردو » مغز باام .

==== idx 104 ====
[pdf page 105]
مغزین خمته
مغزین ۱ - بر وزن قروین » نام نوعی | بمقل بچهای بی مهن وبی‌باك و خواریز وخودشوار
از حلوا باشد . باشد. .
مغزینه ؟ - بر وزن کنجینه » بممتی مغمومه:*۱- با میم بروزن منظومه .
دماغ باشد ۴ . پلفت احل بربر قلیةٌ بادنجان راگویند .
مفکده ۴ - باکاف و دال ابجد بروزن مغناطیی ۱ پلفت بونانی . سنگه
مقبچه » میغانه و شراب خانه راکویند- وخانةٌ آخن‌ربا باشد .کوبند هر که قدری مفتالیس در
آتش پرستان را نیز گفته‌اند . کردنآویز ده اوژ باده ش دق اه۶
وی 0 ی دن! ويزد دهن اوزباده شود وهیچ چیز فرآهوش
وا مقل ۰ < بنت اول بروزن مقل «بستی نکندء ودرد یت را نیز نافع‌است وهمچنین درد
و پای ونقرسرا ۰ چون بن دست گیرند . و کویند
مفلاح « بفتح اول بروزن کجواج , معدن آن در قعر دربا جوم
کوی راگوبند که بجهت کردکان بازی کنند » | است . اکرآرا باآب ۵۸
و وجه تسمیةٌ این گودال بازست چه مغ بمعنی | سیریاآب دهن‌روزم‌دار ِ 1
کودال ولاج (۱) بمعنی بازی باشد . وبکسراول | بیندایندخاسیتش زابل 5
همگفته‌اند ۰ . کردد . وحذی ال مالس ار
مغلاع ۷ - باغین ضله‌دار . بر وزن [ هم بنظرآمده است که
و معنی مقلاج است که گودال جوز بازی باشد. ‏ | مغنطیی‌باشد ؛ وبجای مفناطییس
مغلگاه - بنتح اول بر وزن تختگاء , | حرف دوم قاف هم درست است .
جای استراحت و خوابگاهآدمی وحیوانات دیگر مفند ۱۳- نم اول وثانی وسکون نون
باشد چه مفل بمعنی استراحت, وگاه بمعتی‌جای | ودال ابجد » بمعنی گلوله باشد مطلقاً - وکرهی
ومقام هم‌آمده است ۸ ۰ را نیز گوبند که درمیان گوشت میباشد وآ براغدد
مغلی‌قندز ‎٩‏ - بنم اول ونای وقاف | میگوبند - وهرچیز ممزوج و درهم آمیخته را
و دال ابجد و سکون نون و زای هوز » اشاره | نیز گفته‌اند .

() چك » چش : لا ۰

۱- از : مغز این (پسوند دبت). - از : مغز ۳ ینه (یوند دبت) . "

۴ - باین‌معنی در دساتیر آمده « فرهنکك دساتیر ص۲۹۹ ۴ ۰ ۴ - از : مغل
کده (پوند مکان) . 8 رد4 : مخلگاه . ۹ - رك : مغلاغ . ۷ - رك :
مفلاج . ۸« مفلگاء » جای خفت و جست (خسب . دهغدا) بود ازآن دو وچهار پای.
حمزءٌ عروض ی گوید :

قرارگاه و «غلگاهشان همی ز بهشت بکوهسارکنی و پژرف غارکنی .»
« لغت فری ص ۵۱۱ ۰

‎٩‏ - از: مغلی ( ۳ مغولی )+ قندز (هم.) *- (عر) وت مقموم ( اسم
مفعول ازه غم > ) بمعنی محزون .رك : اقرب‌الموارد . ۱- از یوتانی 33281188168 با
5 210201 , 2122116 (فر)«دزی ج؟ 4 ۹۰ «خب الذخاترص ۶۱۰۰-۹۸

‏۴۳ مفنده (هم.)

==== idx 105 ====
[pdf page 106]
سنهنه نفری
مفنده ۱ - بنم اول و ثانی و سکون | ودرم که شیشه کران بکارپرندوآبرا سنکسلیمالی
نون وفتح‌دال ابجد. کرهی و کنده‌ای(۰)راکوبند ۲ کوبند و بگچ رنك شهرت دارد .
که بر اندام مردم از کوشت مانند کردکان شا ۰
بر اندام مردم ان بر مغیاز ۴ - بکر اول وبای ای
میآید ؛ و بسن ی گره و کندهای (۷) کوچك را و 1 دراه
کنته‌اند که درمیان گوشت وکاهی در زبرپوست . رو او ۱۳ زا
اسپل ماهی‌میباشد و بمربی‌غده میگوبند ؛ وبعضی بعاکن وا ی 1 2 ۰
هر گره وکنده (۱) را گویند که در بدن آدمی | 4 ۳31 2 وم
بهمرسد خواه كوچك و خواه بز رکه خواه درد مغیلات - بالام بر وزن سلیمان , بام
کند و خواه درد نکند ؛ بلکه بسنی کفته اند | درختی است خار دار و بعرپی آنرا ام‌غیلان (۳)
کره وکنده (۱) و دلبلی باشد که بیار درد | خوانند ۴ :
کند - مغیلان باستان - کنایه از دیا
مغتی‌ضا ۴ « باسین بی‌قطه بالف کنید, | و روزگار است .
بروزن مه سیما » گلی باشد سیاه.رنگه وآترا از مغیلان گاه - باکاف فارسی بر وزن
کوه کاشان آورند و آن ,مرقدیعا مانند بود - | سلیمان جاه » بممتی مفیلان باستاست که کنایه
و بعتی گوبند سنگی است الوان و بسیار ست. | از ونیا باشد .
بیان نوزدهم
در میم با فا مشتمل بر چهار لغت وکنایت
مفرج گر ان (4) فلا » کنایه از را نی زگویند .
فرشتگان وملالکه باشد - و ستاره‌ها و کواکب مقر س؟* - با را وسین‌بی نقطه وح ر کت
(۷) چش: کندة . () چش : کندهای. () چش : مفیلان ()
(4) چش : مفرح کران .
۹« مفنده . دمل بود که برتن مردم برآید . مجدی ( مروزی ) گوید:
بردار درشتی ز دل خصم بنرمی بردوستی آندر نبد ای دوست مفنده >
لغت قری ص 4۳۳ .۰
مصراع دوم در چاپ اروپا « نزدوستی اندرآآید ای دوست مفنده » وآقای دهخداآبر| چنین صحیح
کرده‌اند : کز پیه (دنبه ) بنضج‌آید ای دوست مفنده؛ درهرحال این‌کلمه وشاهد محل تأمل‌است.
رد : هفند , غند . غنده -
۳ ۳ مفناسیا (عر ) < 332886916 (فر) « دزی اج ۲ ۹*4 * مآخون از ,یودانی
8 لبدل واسکات »۰ کید دمنیزبوم » برنگك خاک سفید. بی‌طمم » غیر قابل حل
درآب .که آترا بمنزلةٌ شد اسید و مپل بکار برند . ۴۳ مصدف « ففیاز » (ه.م.) ‏
بغیاز (.م.) و رك : سراج اللغات بنقل فرهنگه نظام ج ۵ م‌ها . ۴ - رك : ناح‌العروی
چ اس ۱۹۰ «طلح» . 8 - مصحف «مقرتی» (ع). رك : سراح‌اللغات بنقل فرهنگه‌نظام
چ ه ص‌ماً . ورك : مقزنی .
```


## [2026-09-07T17:40:01.371Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT مزغ ===\"; grep -n \"مزغ\" incoming/BQT/BQT_v4_pages.txt | head -10; echo \"=== ARY مغز ===\"; grep -n \"مغز\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-07T17:40:01.435Z] TOOL RESULT

```
=== BQT مزغ ===
1025:ماگیان ۱ - بر وزن مادیان . مزغ | لام حلوائی است که ازبرنج پزند وآن درکیلان
3647:متوسط 086۵118 ویر مزغان » از لانینی 172098102 ۰ پونانی 13018188 ( موسیقی ) . رل :
=== ARY مغز ===
```


## [2026-09-07T17:40:02.424Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON mağz ===\"; grep -n \"مغز\" MON_part1.txt MON_part2.txt | head -10; echo; echo \"=== MON masahat/masih ===\"; grep -n \"مساحت\\|مسیح\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-07T17:40:02.520Z] TOOL RESULT

```
=== MON mağz ===
MON_part1.txt:102:و مغزشناسی را فرا گرفت. 
MON_part1.txt:1175:شکرء کف چوبکک و مغز پسته. نوعی از 
MON_part1.txt:2360:زمین از لحاظ تکامل مغزی. آدم ات اسان 
MON_part1.txt:3567:آشوبیدن مغز: پریشان ساختن حواس. 
MON_part1.txt:3722:چارمغز. 
MON_part1.txt:3968:سفید و معطر و مغز ساقه‌اش نرم است. و 
MON_part1.txt:5304:(مغزنی» آقطی) که به نخی ابریشمین 
MON_part1.txt:5582:اهیانه: (0)حععرنة (ا.) استخوان بالای مغز 
MON_part1.txt:6300:شبکیه متم رکزند به مغز منتقل گردد. 
MON_part1.txt:6432:گاوریش؛ بی‌مغز» کالبو ه؛ دنگ. 

=== MON masahat/masih ===
MON_part1.txt:502:۱ میلادی؛ مسیحی 
MON_part1.txt:956:اجداد. کشیشان (مسیحی)» آناء کلیسا» آباء 
MON_part1.txt:958:پدران آسمانی. آباء کلیسا: کشیشان مسیحی؛ 
MON_part1.txt:5841:روحانی مسیحی؛ بادری؛ ج. اباء: اباء 
MON_part1.txt:12886:درجات آیین مسیح که پایین تر از «مطران» و
```


## [2026-09-07T17:40:13.345Z] TOOL CALL #34: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T17:40:13.351Z] TOOL RESULT

```


```


## [2026-09-07T17:40:13.599Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls tools/; head -30 tools/fetch_source.py"
}
```


### [2026-09-07T17:40:13.638Z] TOOL RESULT

```
build_site.py
fetch_source.py
ganjoor.py
jscheck.js
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
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
```


## [2026-09-07T17:40:17.123Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mosg%CA%B0os",
 "prompt": "What is this PIE root, its meaning, and its descendants (Indo-Iranian, Avestan, Germanic, Slavic, Persian)? Quote the reconstruction and descendant list."
}
```


## [2026-09-07T17:40:18.631Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%BA%D8%B2",
 "prompt": "Give the Persian entry مغز: etymology (Middle Persian, Old Iranian, Proto-Indo-European), meanings, and any alternative forms like مزغ."
}
```


### [2026-09-07T17:40:22.791Z] TOOL RESULT

```
# Proto-Indo-European Root: *mosgʰós

**Reconstruction:** "*mosgʰós" m (thematic, non-ablauting noun)

**Meanings:** The root denotes "marrow" and "brain."

**Descendants listed include:**

- Proto-Balto-Slavic: *masgás
- Proto-Germanic: *mazgą
- Proto-Indo-Iranian: *mazgʰás

The page notes that the Indo-Iranian branch descendants can be found in detail elsewhere. While specific Avestan and Persian forms aren't explicitly listed on this page, the Proto-Indo-Iranian entry would contain those further derivatives.

**Etymology note:** The entry suggests it "possibly continues earlier *most-gʰ-os" and compares it to Sanskrit and Tocharian cognates relating to brain and marrow tissues.
```


### [2026-09-07T17:40:24.792Z] TOOL RESULT

```
# Persian Entry: مغز (maġz)

**Etymology:**
The word derives from Middle Persian (mzg /mazg/, "brain, marrow"), continuing from Proto-Iranian *mazgáh, Proto-Indo-Iranian *mazgʰás, and ultimately Proto-Indo-European *mosgʰos. It shares cognates with Russian мозг (mozg) and English "marrow."

**Meanings:**
1. Brain
2. Marrow

**Alternative Forms:**
The page lists a related entry معز (mu'az) but does not present مزغ as an alternative spelling for مغز itself. The plural form is مغزها (maġz-hā / maġz-hâ), with Tajik using the Cyrillic spelling мағз.

**Derived Terms:**
Several compound forms exist, including بی‌مغز (lacking brain/foolish), مغز پسته (pistachio kernel), and فرار مغزها (brain drain).
```


## [2026-09-07T17:40:33.799Z] TOOL CALL #38: Bash

```json
{
 "command": "pdftoppm -f 342 -l 342 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg342 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T17:40:35.509Z] TOOL RESULT

```
total 18064
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 13:40 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb      725 Sep  7 13:36 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78732 Sep  7 13:40 ffd32.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    10531 Sep  7 13:39 p343_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30408 Sep  7 13:39 p343_mus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75149 Sep  7 13:40 pg342.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 13:36 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T17:40:36.275Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%CC%A5%C3%A9g%CA%B0us",
 "prompt": "Is there a PIE root meaning \"short\" reconstructed as *mreǵʰus or *mr̥ǵʰus? Give the reconstruction, meaning and descendants (Avestan, Greek brakhus, Latin brevis, Germanic murgjaz)."
}
```


### [2026-09-07T17:40:37.822Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T17:40:42.701Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg342.png"
}
```


### [2026-09-07T17:40:43.223Z] TOOL RESULT

```

```


## [2026-09-07T17:40:43.204Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T17:40:44.128Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%CA%B3e%C7%B5%CA%B0us",
 "prompt": "PIE root for \"short\": reconstruction, meaning, descendants."
}
```


### [2026-09-07T17:40:45.679Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T17:41:02.012Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 342 -l 342 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf p342hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('p342hi.png'); print(im.size)\nw,h=im.size\n# empty box approx x 870-1190 of 1700 wide -> scale\nsx=w/1700; sy=h/2200\nim.crop((int(840*sx),int(590*sy),int(1220*sx),int(770*sy))).save('p342_box.png')\n\""
}
```


### [2026-09-07T17:41:04.555Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-07T17:41:07.703Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p342_box.png"
}
```


### [2026-09-07T17:41:07.717Z] TOOL RESULT

```

```


## [2026-09-07T17:41:12.957Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('p342hi.png')\nw,h=im.size; sx=w/1700; sy=h/2200\nc=im.crop((int(850*sx),int(600*sy),int(1220*sx),int(760*sy)))\nc=c.resize((c.width, c.height))\nc.save('p342_box2.png'); print(c.size)\nimport numpy as np\na=np.array(c.convert('L'))\nprint('min',a.min(),'dark pixels',(a<128).sum())\n\""
}
```


### [2026-09-07T17:41:14.586Z] TOOL RESULT

```
(740, 320)
min 0 dark pixels 3848
```


## [2026-09-07T17:41:17.395Z] TOOL CALL #45: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p342_box2.png"
}
```


### [2026-09-07T17:41:17.409Z] TOOL RESULT

```

```


## [2026-09-07T17:41:22.922Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('p342hi.png')\nc=im.crop((1880,1320,2650,1680))\nc.save('p342_box3.png'); print(c.size)\nimport numpy as np; a=np.array(c.convert('L')); print('dark',(a<128).sum())\n\""
}
```


### [2026-09-07T17:41:24.691Z] TOOL RESULT

```
(770, 360)
dark 14439
```


## [2026-09-07T17:41:27.756Z] TOOL CALL #47: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p342_box3.png"
}
```


### [2026-09-07T17:41:27.770Z] TOOL RESULT

```

```


## [2026-09-07T17:41:37.634Z] TOOL CALL #48: WebSearch

```json
{
 "query": "wiktionary Reconstruction Proto-Indo-European \"mreǵʰus\" short brakhus brevis",
 "allowed_domains": [
  "en.wiktionary.org"
 ]
}
```


## [2026-09-07T17:41:37.766Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/marrow",
 "prompt": "Give the full etymology of \"marrow\" including Proto-Germanic and PIE forms and cognates."
}
```


### [2026-09-07T17:41:42.458Z] TOOL RESULT

```
Web search results for query: "wiktionary Reconstruction Proto-Indo-European "mreǵʰus" short brakhus brevis"

Links: [{"title":"Reconstruction:Proto-Indo-European/mréǵʰus - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mr%C3%A9%C7%B5%CA%B0us"},{"title":"Category:Proto-Indo-European adjectives - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Proto-Indo-European_adjectives"},{"title":"Reconstruction:Proto-Indo-European/-us - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-us"},{"title":"Reconstruction:Proto-Indo-European/dʰéǵʰōm - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0%C3%A9%C7%B5%CA%B0%C5%8Dm"},{"title":"Category:Proto-Indo-European proterokinetic adjectives - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Proto-Indo-European_proterokinetic_adjectives"},{"title":"Reconstruction:Proto-Indo-European/h₁órǵʰis - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81%C3%B3r%C7%B5%CA%B0is"},{"title":"Reconstruction:Proto-Indo-European/méǵh₂s - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9%C7%B5h%E2%82%82s"},{"title":"Reconstruction:Proto-Indo-European/éǵh₂ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C3%A9%C7%B5h%E2%82%82"},{"title":"Reconstruction:Proto-Indo-European/ǵʰelh₃- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0elh%E2%82%83-"},{"title":"Reconstruction:Proto-Germanic/murguz - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/murguz"}]

Based on the search results, I found relevant information about *mréǵʰus:

*mréǵʰus is a Proto-Indo-European word meaning "short". It is cognate with Latin brevis ("short, small, narrow, shallow").

The search results confirm that this term exists in Wiktionary's reconstruction of Proto-Indo-European, and it is categorized as a Proto-Indo-European adjective belonging to the proterokinetic and hysterokinetic adjective classes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-07T17:41:43.685Z] TOOL RESULT

```
# Etymology of "Marrow"

The word "marrow" originates from Old English *mearg* (earlier *mærh*), derived from Proto-Germanic *\*mazga-*. This Proto-Germanic form traces back to the Proto-Indo-European root *\*mozgo-*, meaning "marrow."

**Related cognates across Indo-European languages include:**
- Sanskrit *majjan-*
- Avestan *mazga-*
- Old Church Slavonic *mozgu*
- Lithuanian *smagenės* ("brain")

**Germanic cognates include:**
Old Norse *mergr*, Old Saxon *marg*, Old Frisian *merg*, Middle Dutch *march*, Dutch *merg*, Old High German *marg*, and German *Mark*.

The word originally referred to "soft tissue found in the interior of bones" (attested from late 14c.). By the mid-14c., it developed a figurative sense meaning "the inmost or central part, inner substance, essence."
```


## [2026-09-07T17:41:49.397Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mr%C3%A9%C7%B5%CA%B0us",
 "prompt": "Give the reconstruction, meaning, and the full list of descendants (Proto-Indo-Iranian/Avestan, Hellenic/Greek, Italic/Latin, Germanic, Balto-Slavic) with notes."
}
```


## [2026-09-07T17:41:50.778Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/murguz",
 "prompt": "Give the Proto-Germanic reconstruction, its meaning, etymology from PIE, and descendants (Gothic gamaurgjan, OHG murgi, Old English myrge > merry)."
}
```


### [2026-09-07T17:41:55.426Z] TOOL RESULT

```
# Proto-Indo-European *mréǵʰus

**Reconstruction:** *mréǵʰus

**Meaning:** "short" or "brief"

**Etymology:** Derived from "*mreǵʰ-" ("short") plus the "*-us" suffix (Caland system).

## Descendants by Language Family:

**Proto-Indo-Iranian:** *mr̥ȷ́ʰúš
- Avestan: mərəzujuua (in compound "short-lived")

**Proto-Hellenic:** *brəkʰús
- Ancient Greek: βραχύς (brakhús) "short"

**Proto-Italic:** *breɣʷis
- Latin and other Italic languages

**Proto-Germanic:** *murguz
- English and other Germanic languages

**Proto-Slavic:** *bъ̑rzъ (likely connection)
- Slavic language descendants

The entry notes two inflectional patterns: an earlier proterokinetic pattern and a later hysterokinetic pattern, with complex declensions across masculine, feminine, and neuter genders.
```


### [2026-09-07T17:41:56.560Z] TOOL RESULT

```
# Proto-Germanic *murguz

**Reconstruction:** *murguz

**Meanings:** The term functions as an adjective with two primary senses: "(of time or duration) short; brief" and "slow; leisurely."

**Etymology:** The word derives from Proto-Indo-European "*mréǵʰus ~ *mr̥ǵʰéws" meaning "short." It shares cognacy with Latin "brevis" (short, small, narrow, shallow).

**Selected Descendants:**
- **Old English:** myrġe, miriġe, murġe (and variants) → Middle English myrie → Modern English "merry"
- **Old High German:** murgi, murg → Middle High German murc → German "murk"
- **Old Norse:** *myrgill (< *murgilaz) → Norwegian Nynorsk "myrjel"

The semantic evolution from "short/brief" to the modern English "merry" represents a significant semantic shift across Germanic languages over centuries of linguistic development.
```


## [2026-09-07T17:42:10.703Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/borzoi",
 "prompt": "Etymology of borzoi: Russian source, meaning, date of entry into English, and PIE connection."
}
```


## [2026-09-07T17:42:12.830Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D0%B1%D0%BE%D1%80%D0%B7%D0%BE%D0%B8",
 "prompt": "Russian борзой / борзая / борзой: meaning, etymology from Proto-Slavic *bъrzъ, and any note on the dog breed name борзая. Also mention Proto-Slavic *bъrzъ etymology."
}
```


### [2026-09-07T17:42:14.993Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T17:42:15.032Z] TOOL RESULT

```
# Etymology of Borzoi

**Origin:** The word "borzoi" comes from Russian, entering English in 1887.

**Meaning:** The term literally translates to "swift" or "quick" in Russian. It refers to a Russian wolfhound breed.

**Related Languages:** The etymological dictionary notes cognates in other Slavic languages, including Czech *brzy* and Serbo-Croatian *brzo*, both meaning "quickly," as well as Lithuanian *bruzdėti*, meaning "to hurry."

**Key Details:** According to the source, the Russian term is *borzoy*, and the word's adoption into English specifically dates to 1887, when Western audiences began documenting this dog breed by its Russian name.
```


## [2026-09-07T17:42:21.477Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Slavic/b%D1%8Архъ",
 "prompt": "Proto-Slavic *bъrzъ: meaning, etymology, cognates."
}
```


## [2026-09-07T17:42:22.507Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D0%B1%D0%BE%D1%80%D0%B7%D0%BE%D0%B9",
 "prompt": "Russian борзой: meaning, etymology (Proto-Slavic *bъrzъ), and the noun борзая 'borzoi dog'."
}
```


### [2026-09-07T17:42:22.818Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T17:42:28.205Z] TOOL RESULT

```
# Definition of Борзой

**Борзой** (borzój) is a Russian word with two primary etymological origins:

## Etymology 1: Adjective

Inherited from Old East Slavic _бързъ_ and ultimately from Proto-Slavic *bъrzъ, this adjective has several meanings:

1. **Swift/Fleet** (dated): "a swift horse"
2. **Relational**: Pertaining to the borzoi dog breed or greyhounds
3. **Colloquial**: Describing someone as "cheeky" or "insolent"

## Etymology 2: Noun

The word functions as a noun form representing certain grammatical cases of _борза́я_ (borzája), the feminine form referring to a female borzoi dog.

## Cultural Significance

The term has widespread descendants across multiple languages—from English "borzoi" to French, German, Italian, Spanish, and many others—reflecting the breed's international recognition. The word was featured as Wiktionary's Foreign Word of the Day on August 31, 2024.
```


## [2026-09-07T17:42:36.397Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/pretzel",
 "prompt": "Etymology of pretzel: German Brezel, Latin brachiatus/brachium, Greek brakhion. Give the chain."
}
```


## [2026-09-07T17:42:37.733Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/messiah",
 "prompt": "Etymology of Messiah: Late Latin, Greek Messias, Aramaic meshiha, Hebrew mashiah, verb mashah, and any Arabic cognate masaha."
}
```


### [2026-09-07T17:42:40.643Z] TOOL RESULT

```
# Etymology Chain for Pretzel

Based on the Online Etymology Dictionary, here's the etymological progression:

**English** → **German** → **Latin** → **Greek**

- **English** (1836): "pretzel"
- **German**: From Middle High German *brezel/prezel*
- **Latin**: From Medieval Latin *brachitella* (diminutive form), derived from *bracchiatus* meaning "with branches, with arms"
- **Greek**: From *brakhion*, meaning "an arm"

The source explains that the word likely originated from the shape: "a kind of biscuit baked in the shape of folded arms." The diminutive suffix indicates it was a small item resembling arms folded together, which is reflected in the pretzel's characteristic twisted, knot-like form.
```


### [2026-09-07T17:42:42.684Z] TOOL RESULT

```
# Etymology of Messiah

The word "Messiah" originates from Semitic languages and entered English around 1300. According to etymonline, it comes from "Late Latin _Messias_, from Greek _Messias_, from Aramaic (Semitic) _meshiha_ and Hebrew _mashiah_" meaning "the anointed."

The root verb is Hebrew _mashah_, which means "to anoint." This makes Messiah the Semitic equivalent of the Greek word Christ, both referring to an anointed one—specifically, Jesus as Christianity's savior figure.

In Jewish tradition, the term originally functioned as "a descriptive title of an expected deliverer of the Jewish nation" in Old Testament prophetic texts. The modern spelling attempting to look more authentically Hebrew dates from the Geneva Bible (1560).

By the 1660s, the word's meaning had expanded metaphorically to describe "an expected liberator or savior of a captive people" more broadly, beyond its religious application.
```


## [2026-09-07T17:42:47.247Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AD",
 "prompt": "Arabic مسح: give the root م س ح, the verb masaḥa meaning, derived nouns مساحة (masāḥa) 'area/surveying', and any note on مسيح. Also list the Persian entry if present."
}
```


## [2026-09-07T17:42:49.075Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B3%D9%8A%D8%AD",
 "prompt": "Arabic مسيح (Masīḥ) 'Messiah/Christ': etymology — is it a native derivation from م س ح or a borrowing from Aramaic/Syriac mšīḥā? Also give the Persian مسیح entry if present."
}
```


### [2026-09-07T17:42:54.446Z] TOOL RESULT

```
# Arabic مسيح (Masīḥ) Etymology

Based on the Wiktionary entry, the word is **native to Arabic** rather than borrowed. According to the etymology section:

> "Related to مَسَحَ (masaḥa, 'to anoint'). Cognate to Aramaic ܡܫܺܝܚܳܐ (m'šīḥāʿ) and Hebrew מָשִׁיחַ (mashíakh)"

This indicates the Arabic term derives from the root م س ح (m-s-ḥ) meaning "to anoint," making it a native formation. While cognate to Aramaic and Hebrew versions, the etymology shows it as an independent development from this shared Semitic root rather than a direct borrowing.

**Regarding Persian:** The page references an alternate spelling مسیح (with different diacritics) but does not provide a separate Persian entry. The Wiktionary is organized primarily as an Arabic entry with cross-references to 7 language versions available elsewhere on the platform.
```


### [2026-09-07T17:42:55.043Z] TOOL RESULT

```
# Arabic مسح (masaḥ)

**Root:** م س ح (m s ḥ)

**Primary Verb Meaning:** The verb مَسَحَ (masaḥa) has multiple senses including "to stroke with the hand or similar, to wipe off, to sweep" and "to anoint." Additional meanings include smoothing, polishing, and erasing.

**Derived Nouns:**
- مِسَاحَة (misāḥa) - appears as a verbal noun variant meaning survey/area measurement
- مَسْح (masḥ) - the verbal noun; also denotes "a survey"
- مِسْح (misḥ) - a coarse cloth, sackcloth, or haircloth

**Related Term - مسيح (Masīḥ):**
The entry does not explicitly discuss مسيح on this page, though the verb form مَسَّحَ (II) includes "to Christianize" as a meaning, which etymologically connects to the concept of anointing (Messiah = "the anointed one").

**Persian Entry:** The page indicates a Persian Wiktionary entry exists but does not provide its content details.
```


## [2026-09-07T17:43:01.140Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FVQ Masih ===\"; grep -n -i \"masih\\|Masīh\\|al-Masih\\|Messiah\" FVQ_pages.txt | head -20"
}
```


### [2026-09-07T17:43:01.190Z] TOOL RESULT

```
=== FVQ Masih ===
9538:Messiah (6 Meaaiaf)-
```


## [2026-09-07T17:43:04.548Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9500,9570p' FVQ_pages.txt; echo \"--- page tag ---\"; awk 'NR<=9538 && /\\[pdf page/{p=$0} END{print p}' FVQ_pages.txt"
}
```


### [2026-09-07T17:43:05.759Z] TOOL RESULT

```
date from the more settled communities in the North. 2
(Misk).
Ixxxiii, 26.
Musk.
This sole occurrence is in an early Meccan description of Paradise.
The word was widely used among the Arabs in the pre-Islamic
period 3 and was quite commonly recognized as a loan-word from the
Persian. 4
The Phlv. 4-tyi^* mushk 5 seems to have come ultimately from the
Skt. *nra, 6 but it was from the Iranian, not the Indian form, that
were borrowed the Arm. jh^ 7 ; Gk. //capos' : Aram. ptflB ;
Syr. JoaQLo ; Eth. JJfllf|. It is more likely to have come direct from
Middle Persian into Arabic 8 than through the Syriac, as Mingana,
Syriac Influence, 88, claims.
(Miskin).
Of very frequent occurrence, e.g. ii, 77, 172 ; ix, 60.
Poor. "
' '^e ' ...
Note therefrom the formation <1X.^.^ poverty, indigence, n,
*58 ; iii, 108.
Fraenkel, Vocab, 24, pointed out that the Arabic word is from the
Syr. ]* *>ffnVo though this comes itself ultimately from Akkadian.
The muskenu of the Cuneiform inscriptions was interpreted by Littmann
1 Horovitz, KU, 140.
2 Schwally, ZDMQ, Hi, 134 ; Lammens, Ranctuaires, passim ; Von Kremer,
Streifziige, ix, n.
3 Siddiqi, Studien, 85 ; Geyer, Zwei Gediehte, i, 90 ff. : ii, 79. r
4 al-Jawaliqi, Mu'arrab, 143 ; ath-Tha'alibi, Fiqh, 318 ; as-Suyu^i, Itq, 324 ;
Mvzkir, i, 136; al-KhafajI, 182; LA, xii, 376.
5 Justi, Glossary to the Bundahesh, p. 241. Vullers, Lex, ii, 1185.
7 Hiibschmann,* Arm. Gramm, i, 196. 8 Vollers, ZDMQ, 1, 649, 652.FOREIGN VOCABULARY OF THE QUR*AN 265
mZA, xvii, 262 ff., as leper, but Combe, Bahykmaca, iii, 73, 74, showed
that it meant the humble classes, 1 and so poor. It passed into Heb.
as 15PQ, fSOfp meaning poor, and into Aram. W30J3;
Syr. ]i **M%Vn w jth the same meaning, and it was from Aram, that the
Ar. *~~A and Eth. 9Ml^ were derived. 2
^C*.*M** (Maslh).
iii, 40 ; iv, 156, 169, 170 ; v, 19, 76, 79 ; ix, 30, 31.
Messiah (6 Meaaiaf)-
It is used only as a title of Jesus, and only in late passages when
Muhammad's knowledge of the teachings of the People of the Book is
much advanced.
The Muslim authorities usually take it as an Arabic word from
fcl*^ to wipe (Tab. on iii, 20). Others said it was from I*L~~* to smear
or anoint (Rcaghib, Mufraddt, 484), others derived it from r-U* to travel
(LA, iii, 431), and some, like Zam. and Baid., rejected these theories
and admitted that it was a borrowed word.
Those Muslim philologers who noted it as foreign, claimed that
it was Hebrew, and this has been accepted by many Western scholars, 3
though such a derivation is extremely unlikely. Hirschfeld, Beitrage, 89,
would derive it from Aram. NIT27Q, which is possible, though
as it is used in early Arabic particularly with regard to Jesus, we are
safer in holding with Fraenkel, Vocab, 24, 4 that it is from Syr. ]^iaV>
especially as this is the source of the Arm. IP^"/'"*/ 5 ; Eth. 0ofa rh 6 n
the Manichaean nitiya of the "koktiirkisch" fragments 7 ; thePazend
1 Johns, Schweioh Lectures, 1912, p. 8, would derive it from kaim " to bow down ",
so that originally it would mean suppliant. See, however, Zimmern, Akkad. Fremdw,
47.
2 Noldeke, Neue Britriige, 45. Note also the Phon. pDD (Harris, Glossary, 120).
3 Sayous, Jesus Christ d'apres Mahomet (Paris, 1880), p. 21 ; Pautz, Offenbarung,
193, n. 3.
4 So Lagarde, Ubersicht, 94 ; Margoliouth, Chrestomathia Baidawiana, 163 ;
Cheikho, Nasraniya, 186 ; Mingana, Syriac Influence, 85.
8 This, however, may be direct from the Greek ; cf. Hiibschmann, Arm. Gramm,
i, 364.
Noldeke, Neue Beitrage , 34.
7 Le Coq in SBA W, Berlin, 1909, p. 1204 ; Salemann, Manichaeischt Studien, i, 97.266 FOREIGN VOCABULARY OP THE QUR ? AN
mashydb ; Phlv. -"tW^ (Shikand, Glossary, 258), and the Manichaean
Soghdian msyh' (Henning, Manichaisches Beichibuch, 142).
The word was well known in both N. and S. Arabia in pre-Islamic
times. 1
--- page tag ---
```


## [2026-09-07T17:43:34.944Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nfor f,targets in (('HRN.txt',[8570,8573]),('HUB.txt',[7973,9552])):\n    t=open(f,encoding='utf-8',errors='replace').read().split('\\n')\n    leaf=0\n    for i,l in enumerate(t,1):\n        if i in targets:\n            off = 21 if f=='HRN.txt' else 10\n            print(f,'line',i,'leaf',leaf,'-> printed p',leaf-off)\n        leaf+=l.count('\\f')\nEOF\necho \"=== ARY latin index ===\"; grep -n -i \"MAZGA\\|MOZGO\\|MAGZ\\|MREGH\\|BREVIS\\|BRAKHUS\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-07T17:43:36.190Z] TOOL RESULT

```
HRN.txt line 8570 leaf 242 -> printed p 221
HRN.txt line 8573 leaf 242 -> printed p 221
HUB.txt line 7973 leaf 233 -> printed p 223
HUB.txt line 9552 leaf 276 -> printed p 266
=== ARY latin index ===
2988:sida *MREGHLU oly 1 y ta Gately
13842:MARG, MARAG MAZGA AVESTAN) gles}
13844:HOLD ENGLISH) oS gulSsl MAZGA,MASG (PAHLAVI) «5 Ly,
```


## [2026-09-07T17:43:41.044Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; sed -n '2980,2995p' ARY_latin_index_pages.txt; echo ---; sed -n '13835,13850p' ARY_latin_index_pages.txt; echo \"--- page tags ---\"; awk 'NR<=2988 && /\\[pdf page/{p=$0} END{print \"MREGHLU:\",p}' ARY_latin_index_pages.txt; awk 'NR<=13842 && /\\[pdf page/{p=$0} END{print \"MAZGA:\",p}' ARY_latin_index_pages.txt"
}
```


### [2026-09-07T17:43:42.292Z] TOOL RESULT

```
‘MACKENZIE: 102 BRAZD (uLEY(SPANISH) colslyl
BUCK: 236-237 BRACCIO —(4LE}(TALIAN) gli!
te abt olny BRAT = (4L2}(RUMANIAN) «gly
BRACO — (4Lt}(PORTUGUESE) Ji
. (QLD SCANDINAVIAN) oS 52h
foetlaok
oan 354 po" B20" 9a pe Sl cal hauls te clbdks I Ey Pot
BL aT obey gg y BRACCHIUM 539 .503!s (31-2 5) POKORNY , BARNHART -1
sida *MREGHLU oly 1 y ta Gately
VEFA OLD NORSE) oS p35 UBDAENA (AVESTAN) glia si
WEVA (OLD FRISIAN) 4S 62.5 VAF., WAFISHN PAHLAVI) 5 ghey
OLD HIGH GERMAN) oS gilt WAP :(TOKHARIAN A) A 5,65
WEBAN WAR :(TOKHARIAN B) B «5,3
WEBEN GERMAN) ghaST UBHNATL, SANSKRIT) cy Suse
WEFAN (OLD ENGLISH) 245 gost} VABHI, UBHNA, UMHATI
WEAVE, WEB ENGLISH) gosSt A(GREEK) gli
---
MOGH (MOGHMARD) 56 BARNHART:
tere sbi olny (MAGIC, MAGI 622,
lethal
HI Hy all Bak) 32 15s cal aN
Ula cg Sale tome ge col olay! y te slab; So 5205] gal ee
netll2 gain ey Sle yo oly onl pe
lk aly gees jl ZU MAGICIAN, MAGIC (colSil gtasjly “1
MARG, MARAG MAZGA AVESTAN) gles}
MARK HAGERMAN) glsT MAZGH —:(OLD PERSIAN) gkuel, oo)
HOLD ENGLISH) oS gulSsl MAZGA,MASG (PAHLAVI) «5 Ly,
MEARH, MEARG MAGHZ HOSSETIC) gins)
MARROW HENGLISH) galSl MEGZ, MEJU KURDISH) «53,5
MARV (DANISH) S)\ail MAZHG (BALUCHI) og sh
MERG (SWEDISH) 3 yo MAGHZA HAFGHANI) (3.4) git
MARV (NORWEGIAN) $354 MASSUNT —.(TOKHARIAN A) A 5 ni
MERG DUTCH) sacle MAJJAN (SANSKRIT) 2 Sie
--- page tags ---
MREGHLU: [pdf page 105]
MAZGA: [pdf page 474]
```


## [2026-09-07T17:43:55.626Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC ===\"; grep -n \"^mozg\\|^mreg\\|^mrgh\\|^mozgho\" IEC.txt | head; echo \"=== WLD Bd2 p309 ===\"; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('n',len(t))\nfor pr in (309,314):\n    for leaf in (pr+4,pr+5,pr+6):\n        seg=t[leaf-1] if leaf-1 < len(t) else ''\n        print('--- printed?',pr,'leaf',leaf,'first120:',seg.strip()[:160].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T17:43:56.890Z] TOOL RESULT

```
=== IEC ===
11250:mrgh- (?) variant of mrg- (1)
11252:mrgh- (2) ‘drizzle Cz. cf. mrholit, inf. (1), id.; Latv. mirga, f. id.
=== WLD Bd2 p309 ===
n 725
--- printed? 309 leaf 313 first120: 30S                                           mormo(ro)-     — mozgho-               manita-m ^unartikulierte Tone'', manaii „gibt einen bestimmten vielleiclit 
--- printed? 309 leaf 314 first120: mozgho-   — inu-                                              309  g,   nicht gh;       die    Annahme, da6 gooyog                                            er
--- printed? 309 leaf 315 first120: 310                                            mu-     ai.    miika- ,.stumm“, arm. (Bugge KZ. 32, 21            ,                                              
--- printed? 314 leaf 318 first120: mjk- — mrou- (mleu-?)                                          313  (s.   Parallelen bei Palk-Torp u. nms): gr. juvg ..ifuskel^, /livcov ,.muskel- reiche Gegend
--- printed? 314 leaf 319 first120: 314                           mreghu-, mfghu-      — mlondo- mreghu-, mrghu- ,,kurz“.   Ay. marazu-jlti-, -Jva- ,,^QayyPio?“ (Wackernagel GGA. 1910, 15 f.);   g
--- printed? 314 leaf 320 first120: na-     .,helfen. nutzen'\     Gr.                      -vdjuev „niitzen“, fut. ovi^-oco usw., oveiag, recte oyf]ag .,Yor- teil, Nutzen“ (o-Praefix), ai. nd-tha
```


## [2026-09-07T17:44:00.843Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('==== leaf 313/314 (WP II 308-309) ====')\ns=t[312]+t[313]\ni=s.find('mozg')\nprint(s[max(0,i-200):i+2200])\nEOF"
}
```


### [2026-09-07T17:44:02.095Z] TOOL RESULT

```
==== leaf 313/314 (WP II 308-309) ====
30S                                           mormo(ro)-     — mozgho-

             manita-m ^unartikulierte Tone'', manaii „gibt einen bestimmten
vielleiclit ai.
Laut von sich" (Pick II ^ 218).
    Auf ein gebrochen redupl. ^mrem- fiihrt Osthoff MU. 5, 93 f. die Sippen
von gr. I^QE/ucD, lat. fremo, ahd. hreman zuriick: fiir gr.             „brause,
drohne", ^gojuog „Getose", ^Qovx'iq „Donner“ figojudo^ai „8chreien wie ein Esel"
ist   diese Auffassung sehr wahrscheinlicb (kaum als ^giremo zu slav.
grvmHi „donnern, drohnen", lit. griimenti aus der Feme leis und dumpf
donnern". Pick BB. 6, 212, Wb. I^ 212 usw. s. Bemeker 360, da diese
wohl idg. ghrem; Perssons Beitr. 36 Anm. 1 Annahroe einer Arfcikulations-
schwankung *brem ^hhrem, s. u., ist noch weniger zu vertreten).
                            :



    Dagegen fur fremo ahd. hreman, cymr. hrefii „brullen" s. u. hhrem-
„bruininen".

mortno(ro)- „Grausen, grausig, bes. von Gespensterfurcht".
  Gr. fioQjucb „Schreckgespenst“, acc. pi. /nog/novag nkdvgrag daijuovag Hes.,
                                                                             *



Xen. (vgl. Fogycb Fogyavag)^ juioQfJLOQog „Furcbt", iLiOQ/A,o?.vxecov „Scbreck-
                        :



bild“, ^oQiA,olvrxofxat „setze in Furcbt", juoQjuvvei' deivonoieT Hes., juvQjLiog                           ’




(fofog Hes., Myg^iidoveg eigentlich „das                            Yolk der Schreckgespenster";
      formido „das Grausen, peinigende Furcht*; bes. religiose Ehrfurcht".
   lat.

  Pick      168, KZ. 43, 148, Kretschmer Gl. 4, 308.  Lat. for 7n- diss. aus
^morm- (wie bei formica /nvQ/urj^, Lit. bei Yf, LEWb.^ s. v., wozu noch
                                          :



Schopf Die kons. Pernwirkungen 108f. nicht nach Solmsen KZ. 34, 19
                                                                ;


mit for- aus       wie fr- aus *mr*).
   Ob unter der Yorstelluiig des geheimnisvoll drohenden Murmelns in
Beziehung zu mormor- „murmeln"?        Und dann etwa zuerst im Griech.
in dieser Bed. spezialisiert und aufs Lat. erst durch eine religiose "Welle
iibertragen ?

iiiolqo- „Ledersack, Ledertasche".
  Ahd. nialaha^ rahd. malJie „Ledertasche", aisl. malr .Back", gr. aoXyog
„Sack aus Kindsleder" (Pick III
```


## [2026-09-07T17:44:08.768Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor m in re.finditer(r'moz[- ]?g', t):\n    print('---', t[max(0,m.start()-150):m.start()+900].replace('\\n',' ')[:1050]);print()\nEOF"
}
```


### [2026-09-07T17:44:10.053Z] TOOL RESULT

```
--- naze „Rahm, Sahne, Haut auf der Milch" (Jokl SBAk. Wien 68, I 54, ^mndni: nicht besser nach Charpentier KZ. 46, 39 als              1   "^mazgln zu "^mozgo- ,.Mark").       Lat. madeo,^ -ere ..nab sein, von Kasse triefen", mattus ,jtrunken"                             (s.   zur Form Yf. LEAVb.^ s. v., Sommer Hdb.^ ^dl), wohl auch mano^ -are „flie6en, rinnen" als             Denom.     eines   Adj. "^madsnos   (s.    u.       ^mdq-   „na6*');    iiber       lat.  ynanima          s.   u.       Ganz          fraglich ist ob maialis „geschnittenes mannliches Schwein" als Abl.  von "^madia „Mast", s. Sommer IF. 1      81   Yerb. m. Maias sucht                                                              1 ,        ;   Leumann -Us 14, 30 zu begriinden.   Air. maldim „breche (intr.), gehe in Stiicke" (eigentlich „flie6e ausein- ander, zergehe*', formell = lat. madco\ Thurneysen IF. 14, 132, Yf. LEWb.^ u.maialis. Pedersen KG. II 574),            ^vergeblich, ohne Erfolg" (dazu 232                                   mad-   wohl c. maddeu „erl

--- ^   Yerwandtschaft mit slav. 7nezga (s. o.) ist nicbt vrahrscheinlicher (noch anders stellt Charpentier KZ. 46, 39 die kelt. Worter als Ablautform zu mozgJio- ,,Mark'').  nieigu- „wechseln, tauschen; eine Ortsveranderung vornebmen^\    Gr.        djuEtfia)           „wechsle“,    med. ,,erwidere,           vergelte.      wandere'*,   djuoij^o^ .,wecbselnd“,            dfLioiprj        ,,^Yechseb^   Lat. migro^ -are „wandern“, Denom. eines "^mkjV^-ros, Walter KZ. 11. 430 Fick BB. 6, 213, Wb. I^ 510.         j                                    Erw. von mei” „wechseln‘‘ (Persson Wzerw. 15, 28,                     156)    Ksl. miglivz bedeutet nicht „beweglicli‘‘, sondern ,,blinzelnd‘‘                              (Berneker II 56)         und bleibt fern. meigh- „liarnen“ (Praes. meigho und mingho),   Ai. //^c/ia/2 „barnt“, ptc. nudha- (= lat. mictus), nhdlia- n. ,,Kot‘‘, nielia- m. „Harn‘';            av. maezaiti           „harnt,    diingfc^,    maVsnia-,    maesmaii- „Harn“;          arm. (Hubschmann Arm. St. I 43, Arm. Gr. I 474) mi

--- rmantischem g abg. muzga „Lake, WeiheP'                                          (s. o.   zu meu-d-)^ russ. 7nzgnidb ..verderben'',                   mozgmdh „abmagerm*', abg. m^zditi ,.schwachen‘S russ. mozgz regnerisches ^YetteF', moxziih ,,einweichen“.        AVal-h',   Etymolo:ri5ch<‘s        Worterbucb.       U.                                                  17 252                                              meu-     meu-r{o-) — u. dgl. (s. bes. Petersson KZ. 47, 280f., LUA. 1916, 4lf.):   Arm. yielleicht mor „Schmutz, Schlamm, Sumpf            mBU-ri-)^ mmr                                                                    '    ^faeces, residuum‘‘     (kaum als ^moni-ro- zu gr. /ioqvgoco^ s u mer „schwar-                                                                           .   .     zen“);    gr- fivQco, fxvgo^ai                   rinnen lassen (bes. Tranen:),            weinen, klagen'' (aber uber aXi^vQiqeig, nXrjfAVQlg s. u.     sehr unsicher lat. muria „Salzlake, Poke!’* (konnte ein fremdes Kiichenwort sein) ; lit. 

---                            (s. o.   zu meu-d-)^ russ. 7nzgnidb ..verderben'',                   mozgmdh „abmagerm*', abg. m^zditi ,.schwachen‘S russ. mozgz regnerisches ^YetteF', moxziih ,,einweichen“.        AVal-h',   Etymolo:ri5ch<‘s        Worterbucb.       U.                                                  17 252                                              meu-     meu-r{o-) — u. dgl. (s. bes. Petersson KZ. 47, 280f., LUA. 1916, 4lf.):   Arm. yielleicht mor „Schmutz, Schlamm, Sumpf            mBU-ri-)^ mmr                                                                    '    ^faeces, residuum‘‘     (kaum als ^moni-ro- zu gr. /ioqvgoco^ s u mer „schwar-                                                                           .   .     zen“);    gr- fivQco, fxvgo^ai                   rinnen lassen (bes. Tranen:),            weinen, klagen'' (aber uber aXi^vQiqeig, nXrjfAVQlg s. u.     sehr unsicher lat. muria „Salzlake, Poke!’* (konnte ein fremdes Kiichenwort sein) ; lit. miir- stu, murau, miirti „durch^Yeicht wefden“, matira

--- ,Kacken, Hals".    Ai. masta- „Kopf" nicbt nacb Johansson IF. 1-1, 331 als             zu den obigen ^Bildungen, sondern w'obl aus                s. ^mozgo- „Mark, Him"  (Cbarpentier KZ. 46, 35 ff.).   2.    men- ..treten, zertreten, zusammendriicken".    Aol. adjeioai „tretende"             yaxei naxeX Hes., Denom. von einem                                                                '     mn-tos ..getreten"; lit, minii, nimti .treten, Flachs brechen, Felle gerben"                                                     ,    miniij nut ..treten, gerben", lett. dd-minis „Gerber", mina ,,Stufe" („Tritt": kaum zu men- „empoiTagen"), lat. minae „Zinnen", abg. mwio^ m^ti „zs.- driicken", russ. mnu, »?Ja('b,,brecben (Flacbs oderHanf), kneten, treten (Lehm), zerknittern, zerkniillen" (Fick I ^513,            BB, 28, 104, Prellwitz^ 192, ^ 283):      ai.   carma-ninas X.      pi.   ,   .Gerber* (^Persson Beitr. 562): cymr. mathr m. 5     ,proculcatio"    i^nw-tro-)^     maihru ..proculcare",         bret.   mantra, Ptc. mantret „vom Scbmerz n

--- ensack^) Hes.,                                    *    und auch in der Bed. Patrubanys IP. 14, 56 Zuriickfiihrung von arm. maz ,,Haar'‘ auf ein mit '‘mozgJios wechselndes "^mozghos (a\).   mizdho- „LohD,                  Sold^^    feegen den Ansatz         '^'mid^dho-    s.    Brugmann      626         Anm 1).    Ai. nfidhd- n. „Kampfpreis, \YettkampP, av. mtzda- n. „Lohn^, np. 7mizd „Lohn“: gr. taodog „Sold^^; got.          „Lohn“, ags. meoi’d ds. und ags. med^ as. mcda, ahd. mtta^ miata ds., nhd.           abg, nihzda „Lohn“. Curtius 260 usw. lat. mTles ist nicht „Soldner^’ (s. Yf. LEAYb.^ s. v.). Piir                             ;    wgerm.           eine Ablautform "^'meizdha zu postulieren (s. Weyhe PBrB. 30, 56, Trautmann Germ. Ltges. 34, Janko IF. 20, 255, van Helten IP. 23, 99 Anm. 1 noch anders, aber ganzlich verfehlt Feist Got. ^Yb. 198f.), halte                    ;    ich fiir unstatthaft; man hat bei urgerm. ^'^nizdcL als Gdf. zu verharren: Brechung von i zu e und Dehnung infolge des - Schwundes so neuer-            .s’  

---                            *    und auch in der Bed. Patrubanys IP. 14, 56 Zuriickfiihrung von arm. maz ,,Haar'‘ auf ein mit '‘mozgJios wechselndes "^mozghos (a\).   mizdho- „LohD,                  Sold^^    feegen den Ansatz         '^'mid^dho-    s.    Brugmann      626         Anm 1).    Ai. nfidhd- n. „Kampfpreis, \YettkampP, av. mtzda- n. „Lohn^, np. 7mizd „Lohn“: gr. taodog „Sold^^; got.          „Lohn“, ags. meoi’d ds. und ags. med^ as. mcda, ahd. mtta^ miata ds., nhd.           abg, nihzda „Lohn“. Curtius 260 usw. lat. mTles ist nicht „Soldner^’ (s. Yf. LEAYb.^ s. v.). Piir                             ;    wgerm.           eine Ablautform "^'meizdha zu postulieren (s. Weyhe PBrB. 30, 56, Trautmann Germ. Ltges. 34, Janko IF. 20, 255, van Helten IP. 23, 99 Anm. 1 noch anders, aber ganzlich verfehlt Feist Got. ^Yb. 198f.), halte                    ;    ich fiir unstatthaft; man hat bei urgerm. ^'^nizdcL als Gdf. zu verharren: Brechung von i zu e und Dehnung infolge des - Schwundes so neuer-            .s’                         

--- 2, 19).           Unredupl, mit y^-Suffix      ir.   muirn (^murni-j .Xarmen, Sausen“ 30S                                           mormo(ro)-     — mozgho-               manita-m ^unartikulierte Tone'', manaii „gibt einen bestimmten vielleiclit ai. Laut von sich" (Pick II ^ 218).     Auf ein gebrochen redupl. ^mrem- fiihrt Osthoff MU. 5, 93 f. die Sippen von gr. I^QE/ucD, lat. fremo, ahd. hreman zuriick: fiir gr.             „brause, drohne", ^gojuog „Getose", ^Qovx'iq „Donner“ figojudo^ai „8chreien wie ein Esel" ist   diese Auffassung sehr wahrscheinlicb (kaum als ^giremo zu slav. grvmHi „donnern, drohnen", lit. griimenti aus der Feme leis und dumpf donnern". Pick BB. 6, 212, Wb. I^ 212 usw. s. Bemeker 360, da diese wohl idg. ghrem; Perssons Beitr. 36 Anm. 1 Annahroe einer Arfcikulations- schwankung *brem ^hhrem, s. u., ist noch weniger zu vertreten).                             :        Dagegen fur fremo ahd. hreman, cymr. hrefii „brullen" s. u. hhrem- „bruininen".  mortno(ro)- „Grausen, grausig, bes. von Gespensterfurcht".   Gr. 

--- gibt es nicht (Pokorny brieflich).  luozghO' jjPflanzentrieb".   Gr. f,i6oyog „Pflanzentrieb, SchoBling" (zm scheiden von f-idoyog ,junges Rind", s. ^mozghos „junges Rind";                        =                                       lit. mdzgas, lett. ma/gs „Auge, Knospe                                                    ;  am Baum" (lit. mezgu^ migsti „Augen, Knospen bekommen" hat sich dazu nach mdzgas „knoten“                :   7nlgsti   „knupfen" gestellt             letztere Sippe    hat idg.                                                                             ;                                                mozgho-   — inu-                                              309  g,   nicht gh;       die    Annahme, da6 gooyog                                            erst nach ooyog fiir ein '^i.iooyog eingetreten      wobei dann allerdings „Eiospe“ aus „Knoten'' deatbar                      sei,  ware, halte ich fiir nicht zutreffend; Prellwitz^ 300 zw.).   Fick    518, Vf. KZ. 34, 514. Lautlich ungerechtfertigt ist Ficks

--- ztere Sippe    hat idg.                                                                             ;                                                mozgho-   — inu-                                              309  g,   nicht gh;       die    Annahme, da6 gooyog                                            erst nach ooyog fiir ein '^i.iooyog eingetreten      wobei dann allerdings „Eiospe“ aus „Knoten'' deatbar                      sei,  ware, halte ich fiir nicht zutreffend; Prellwitz^ 300 zw.).   Fick    518, Vf. KZ. 34, 514. Lautlich ungerechtfertigt ist Ficks KZ. 43, 151 Anreihung von ooyog, juioyog, aoyiov.  mozgho- „Mark, Hirn“ (oder mazgho-).    Ai. mojjdn- „Mark“ {-jj- aus -zjh- s. Vf. KZ. 34, 51 1 f.), av. 7nazga- ,,Mark, Hirn“: ahd. mar(a)^, mar{d)c, as. marg, ags. mearg, aisl. mergr (gen. mergjar) ,,Mark“ (aschwed. micergJier vermag trotz Falk-Torp und maro keine ab- lautende Kebenform "^mezghO” zu erweisen) abg. mozg^ „Grehirn“, mozdnm                                                               ;   {^mozgen^ „Mark‘', apr.

--- treffend; Prellwitz^ 300 zw.).   Fick    518, Vf. KZ. 34, 514. Lautlich ungerechtfertigt ist Ficks KZ. 43, 151 Anreihung von ooyog, juioyog, aoyiov.  mozgho- „Mark, Hirn“ (oder mazgho-).    Ai. mojjdn- „Mark“ {-jj- aus -zjh- s. Vf. KZ. 34, 51 1 f.), av. 7nazga- ,,Mark, Hirn“: ahd. mar(a)^, mar{d)c, as. marg, ags. mearg, aisl. mergr (gen. mergjar) ,,Mark“ (aschwed. micergJier vermag trotz Falk-Torp und maro keine ab- lautende Kebenform "^mezghO” zu erweisen) abg. mozg^ „Grehirn“, mozdnm                                                               ;   {^mozgen^ „Mark‘', apr. mtizgeno „Mark“, wozu (mit Umstellung aus '^inaz- genes durch EinflaB von smdkres „Gehirn“, Vf. aaO.) lit. smdgenes, lett. smadfenes „Gehirn''. Fick      110 usw.; Vf. aaO. (auch zur Scheidung gegen- iiber mezg- „eintauchen“), Scheftelowitz IF. 33, 136.    Von den weitern Anreihungen Charpentiers KZ, 46, 35 iiberzeugt mich ai. mdstaka- m. n. „Kopf, Schadel“, inasVdka- m. n. „Gehirn“, mastidimga'-  m. n. ds. (wohl mind, aus '^mash'^ga-), mastakahmga- n. „Hirnhauf", 

--- arg, aisl. mergr (gen. mergjar) ,,Mark“ (aschwed. micergJier vermag trotz Falk-Torp und maro keine ab- lautende Kebenform "^mezghO” zu erweisen) abg. mozg^ „Grehirn“, mozdnm                                                               ;   {^mozgen^ „Mark‘', apr. mtizgeno „Mark“, wozu (mit Umstellung aus '^inaz- genes durch EinflaB von smdkres „Gehirn“, Vf. aaO.) lit. smdgenes, lett. smadfenes „Gehirn''. Fick      110 usw.; Vf. aaO. (auch zur Scheidung gegen- iiber mezg- „eintauchen“), Scheftelowitz IF. 33, 136.    Von den weitern Anreihungen Charpentiers KZ, 46, 35 iiberzeugt mich ai. mdstaka- m. n. „Kopf, Schadel“, inasVdka- m. n. „Gehirn“, mastidimga'-  m. n. ds. (wohl mind, aus '^mash'^ga-), mastakahmga- n. „Hirnhauf", av.                 chad el wand; pi. Schadel, Gehirn'^ (s. Bartholomae IF. 11, IIS aus einem Paradigma '^mastn), gen. ^mastnds erwachsen), denen ein urar. '^mazg-ia- „HirnbehalteF' zugrunde liegt (der Verlust der Aspiration von zgh in ai. mojjan- scheint also urarisch zu sein, da sonst ^mazgdha- usw. zu erwarten wa

---  keine ab- lautende Kebenform "^mezghO” zu erweisen) abg. mozg^ „Grehirn“, mozdnm                                                               ;   {^mozgen^ „Mark‘', apr. mtizgeno „Mark“, wozu (mit Umstellung aus '^inaz- genes durch EinflaB von smdkres „Gehirn“, Vf. aaO.) lit. smdgenes, lett. smadfenes „Gehirn''. Fick      110 usw.; Vf. aaO. (auch zur Scheidung gegen- iiber mezg- „eintauchen“), Scheftelowitz IF. 33, 136.    Von den weitern Anreihungen Charpentiers KZ, 46, 35 iiberzeugt mich ai. mdstaka- m. n. „Kopf, Schadel“, inasVdka- m. n. „Gehirn“, mastidimga'-  m. n. ds. (wohl mind, aus '^mash'^ga-), mastakahmga- n. „Hirnhauf", av.                 chad el wand; pi. Schadel, Gehirn'^ (s. Bartholomae IF. 11, IIS aus einem Paradigma '^mastn), gen. ^mastnds erwachsen), denen ein urar. '^mazg-ia- „HirnbehalteF' zugrunde liegt (der Verlust der Aspiration von zgh in ai. mojjan- scheint also urarisch zu sein, da sonst ^mazgdha- usw. zu erwarten ware), wahrscheinlich ist auch pali mimja- „Mark'' redupli- ziertes ''^mi-mzglio-,         Abe

---      (s.    u.    meik- „mischen“).           Uber    slav.   ynezga     „Baumsaft'‘ (Fick III^ 318)                 s.     u.    yncigh- ,,harnen“.  mozgho-s „junges Rind^'.   Arm. mozi „junges Rind, Kalb^‘     gr. gooytov, Demin, zu iiooypg „junges Rind, junge Kuh, Parse, Kalb*' (bloB lautgleich mit gooypg „Pflanzentrieb" = lit. mdzgas „Auge, Knospe am Baum" aus idg. ^nozghos mit Velar, ob- wohl „Pflanzentrieb           —                       tierischer SproBling" seitens der Bed. unanfechtbar ware; nicht iiberzeugend sucht Patrubany IF. 13, 124 den Zshang beider Gruppen durch Annahme vonWechsel zwischen yh und gh zu retten).      Bartholomae Stud. II 40, Pedersen KZ. 39, 336.                          Aber      ai.   mahikt-          m. „Stier, BiiflPel"       kaum mit h                           aus zgh- hieher '^Bartholomae aaO. zw. Brug- mann 1^ 559), sondern wohl Ableitung von malii- „gro6“ 'Uhlenbeck Ai. Wb. 220). mu- Schallnachahmung fiir den mit gepreBtcn Lippen erzeugten dumpfen        Laut: mucksen, undeutlich reden, nur u
```


## [2026-09-07T17:44:18.902Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\ns=t[318]\ni=s.find('mreghu-, mrghu- ,,kurz')\nprint(s[max(0,i-200):i+2000])\nEOF"
}
```


### [2026-09-07T17:44:20.278Z] TOOL RESULT

```
314                           mreghu-, mfghu-      — mlondo-
mreghu-, mrghu- ,,kurz“.
  Ay. marazu-jlti-, -Jva- ,,^QayyPio?“ (Wackernagel GGA. 1910, 15 f.);
  gr. ^gayvg „kurz“, ^odysa „seichte Stellen*' (ob dazu aucb ^odyog" Uog
Hes. als maked. Wort, Fick BB. 29, 199f. ? doch s. unter ^mari);
  lat. hrevis (zunachst aus dem Fem. *hrc7,m, Osthoff MU.
                                                             5, 89 IF., alter
ireyu, s. zum Lautlichen die Lit. bei Sommer Hdb.^ 225, Walde Gesch. d.
Sprw. II 1,185) „kurz“, bruma „Wintersonnenwende, Winter, Kalte“ {*brevi-mci
„Zeit der kiirzesten Tage“, Lit. bei Yf. LEWb.^ 98);
  got. gamaurgjan „verkurzen“, ahd. murg, murgi „kurz“, murgfari „zer-
breehlich“, ags. myrge „kurzweilig“.
  De Saussure Msl. 5, 440, Johansson KZ. 30, 442 (nicbt wahrscheinlicher
nach J. Schmidt bei Zupitza Engl. St. 8, 469, Osthoff MU. 5, 90f., Solmsen
KZ. 34, 30, Zupitza Gutt. 135, zu lat. murcus „curtus, verstiimmelU s. *merli-        \


nicht annehmbar Pedersen KG. I 105: air. meirc „Eost“ und alb. marbe
,,Gansehaut“, aksl. mrazz, „Prost“).
  Aksl.     bm^ „schnell“ kaum hierber (obwohl ,,kurz“ und „schnell“ sich
vielfach decken; zugehorige si. Worte fur „Stromschnelle“                —
                                                                s. Berneker

109 f. — sind begrifflich nicht mit lat. brevia, gr. (igdyea vergleichbar
                                                                          ').
sondern wohl zu *bher-s- „eilen“, s. Berneker aaO.                 —
  Gr. (igayimv „Oberarm“        ist   als „rov mjyscog jiQayvTeQog“ an [ioayvg anzu-
schlieSen     (Bechtel Lecil. 83 m.      Lit.),   vgl. fiodaacov   Komp. aus *)iQdyjmv.

inreghni(n)o- ,,Hirnschale, Hirn“.
   Gr. l^Qsyydg, (igey/ra n. (und fjoeyfia) ,,Yorderkopf, Oberschadel'-, ags.
brtxgn, brcegen n. „Gehirn“ (engl. brain), afries. brein, mnd. bragen., bregen ds.
(Grafimann KZ.     12, 193;   Anlaut mr- nach Johansson KZ. 30, 448; Zupitza
Gutt. 136).
  Gegen Anreihung von ags. brego ,,IIerrscher, Furst“, anord. bragr „b
```


## [2026-09-07T17:44:43.880Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC mozg ===\"; grep -n \"mozgho\\|mozgo\\|mazgh\\|mṛghu\\|mreghu\\|mrghu\" IEC.txt | head; echo \"=== IEC brakhus/brevis ===\"; grep -n \"brakhus\\|brevis\\|bhrghu\" IEC.txt | head -5; echo \"=== SKT ===\"; grep -n \"^MARROW\\|^MERRY\\|^BRIEF\\|^BRACE\\|^MESSIAH\\|^BREVITY\" SKT.txt | head"
}
```


### [2026-09-07T17:44:43.971Z] TOOL RESULT

```
=== IEC mozg ===
11255:Srb. mrzak, adj. ‘disgusting’; R merzkil ‘nasty’; Sw murken, pp. & adj. ‘rotten’. (For Cz. mrzák, however, cf. mrghus below)
=== IEC brakhus/brevis ===
1795:bhrghus, os “high; height’. WP II, 172. See bhr&hont-, bhergh-. WP II, 172 Skt. cf. brhát; Av. borozoó; Oss. (o-gde. Am- big. bardz, barz ‘mass, crowd': (?) Arm. bardz (2) “hip, thigh’; Arm. bardzr, gs. bardzu ‘high’; Tokh. A cf. párkár, B parkre long; Hitt. parkus; Olr. brí ‘noble’ beside Ir. brigh ‘virtue, power; Sequanian brig- “high — of winds’; Gaul (ambig.) briga Ch, But cf. bhrgh-); W brí, Cor. bry ‘rank, degree, esteem’; OW bry ‘above’: (?) MHG bor ‘up’. Cf. the e-gde forms in Arm. erkna-berdz ‘high as heaven’, lerna-berdz ‘high as a moun- tain’, and OE brego “ruler”.
1808:bhrio (3) ‘raise’. Variant of bhrgh- (?) OW (ambig.) cf. bry (above'. See bhrghus);
=== SKT ===
22707:BRIEF  INDEX   TO   ROOTS.
22749:BRIEF  INDEX  TO  THE  ABOVE  ROOTS.
```


## [2026-09-07T17:44:48.858Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"mrghus\\|mozg\\|mazg\" IEC.txt | head -10; echo \"=== SKT lower ===\"; grep -n -i \"^marrow\\|^merry\\|^brief\\|^brace\\|^messiah\\|marrow,\" SKT.txt | head"
}
```


### [2026-09-07T17:44:48.968Z] TOOL RESULT

```
10686:mesgü (mezg-) (2) 'immerse, soak, steep; plunge’. See next and cf. mosg- (2) WP II, 300. Variant: mosg- in Gmc. and Baltic Skt. májjami, májje, pp: magnah ‘sink’; Lat. mergo, Gre “dip, immerse; overwhelm’; Sw. mäska 'infuse with hot water; mäsk, m. *brewer's mash, residue from malt'; E dial. to mash ‘to infuse’; Li. mazgóju, óti, v. ^wash- clothes'; Latv. mazgaju, at, id. Cf. moiEs-
11190:Skt. majjà, f. 'brain'; Av. mazga, f. id.; Per. mayz ‘brain, marrow, pith’; Oss. maéz, id.; Tokh. cf. maccunt, pl. ‘brain? beside masiák, B meske, s. «link, joint; LW in W masg, pl. -àu, f. ‘mesh’; OE max, n. ‘net beside mearg, m. n. ‘marrow, pith’; E mesh; OHG maska, f. ‘mesh’; Ger. Masche, f. *knitting-stitch'; LG masch, id.; MHG masche, f. ‘bow, noose’; Sw. maska, f. *knitting-stitch'; ON moskvi, m. ‘mesh’; Li. mázgas ‘knot
11191:mosgos (mosg-) (2) 'steeping, infusion, mash’. Cf. mesgó (2) & moiks- Sw. mäsk, m. brewer's mash'; mäska, v. 'in- fuse, steep’; Eng. dial. mash; Li. cf. mazgóju, óti “wash — things’; Latv. mazgàju, v. ‘wash’
11192:mosghos “bud, shoot. Cf. odsgh-. WP IT, 308 Gk. móschos, m. ‘shoot; young calf; Li. máz- gas, m. (2) ‘buď’; Latv. (alleged) mazgs, m. id. Cf. mosg- (2). (Isophones: ON mergr, Sw. märg, m. *bone-marrow)
11255:Srb. mrzak, adj. ‘disgusting’; R merzkil ‘nasty’; Sw murken, pp. & adj. ‘rotten’. (For Cz. mrzák, however, cf. mrghus below)
=== SKT lower ===
47:Brief  Index  to  the  above  Roots  .       .       .       .597
11151:Marrow,    pith.    (E.)     ME mary,     A.  S.  mearh-  +  Du.  m mergr,  Swed.  mtrg,  Dao.  m^rp, O.  H.  G.    marag ,    also   W.   mn maru.     Further    allied    to    Kn^a. Zend  masga,  mairow  ;  Skt.  «ii^'dJ*. of  bones,  pith  of  trees.
11451:Merry  (C.)  M.  E  merit.  K.%.mirg, mc-rry.  Not  a  Teutonic  wortl.  ••  Irifh  and Gael,  mear,  mcrr>-,  sportive.  —  Gael,  w/r, to  play,  cport :  cf.  Gael,  mirtagach,  merry, playful.
22707:BRIEF  INDEX   TO   ROOTS.
22749:BRIEF  INDEX  TO  THE  ABOVE  ROOTS.
```


## [2026-09-07T17:44:57.422Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '11186,11192p' IEC.txt | cut -c1-600; echo \"=== mrghus ===\"; grep -n \"mrghus\\|mrghu\" IEC.txt | head -5"
}
```


### [2026-09-07T17:44:57.485Z] TOOL RESULT

```
35
40
45
800
Skt. majjà, f. 'brain'; Av. mazga, f. id.; Per. mayz ‘brain, marrow, pith’; Oss. maéz, id.; Tokh. cf. maccunt, pl. ‘brain? beside masiák, B meske, s. «link, joint; LW in W masg, pl. -àu, f. ‘mesh’; OE max, n. ‘net beside mearg, m. n. ‘marrow, pith’; E mesh; OHG maska, f. ‘mesh’; Ger. Masche, f. *knitting-stitch'; LG masch, id.; MHG masche, f. ‘bow, noose’; Sw. maska, f. *knitting-stitch'; ON moskvi, m. ‘mesh’; Li. mázgas ‘knot
mosgos (mosg-) (2) 'steeping, infusion, mash’. Cf. mesgó (2) & moiks- Sw. mäsk, m. brewer's mash'; mäska, v. 'in- fuse, steep’; Eng. dial. mash; Li. cf. mazgóju, óti “wash — things’; Latv. mazgàju, v. ‘wash’
mosghos “bud, shoot. Cf. odsgh-. WP IT, 308 Gk. móschos, m. ‘shoot; young calf; Li. máz- gas, m. (2) ‘buď’; Latv. (alleged) mazgs, m. id. Cf. mosg- (2). (Isophones: ON mergr, Sw. märg, m. *bone-marrow)
=== mrghus ===
11255:Srb. mrzak, adj. ‘disgusting’; R merzkil ‘nasty’; Sw murken, pp. & adj. ‘rotten’. (For Cz. mrzák, however, cf. mrghus below)
```


## [2026-09-07T17:45:01.787Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '11180,11190p' IEC.txt | cut -c1-400; echo \"==== search mosgos(1) ====\"; grep -n \"mosgos (mosg-) (1)\\|mosgos (1)\\|'marrow, brain'\\|‘marrow, brain’\" IEC.txt | head; echo \"=== brghus / mrghu region ===\"; sed -n '11256,11275p' IEC.txt | cut -c1-500"
}
```


### [2026-09-07T17:45:01.872Z] TOOL RESULT

```
mos (mnos) *we, us'. Cf. nós, mes, menes OCS my, id.; Li. mus, acc. ‘us
mosgos, à (1) 'tangle, knot, convolution, brain'. WP II, 308. Cf. mesgo (1)
mors- (morsK-) — moteio
20
25
30
35
40
45
800
Skt. majjà, f. 'brain'; Av. mazga, f. id.; Per. mayz ‘brain, marrow, pith’; Oss. maéz, id.; Tokh. cf. maccunt, pl. ‘brain? beside masiák, B meske, s. «link, joint; LW in W masg, pl. -àu, f. ‘mesh’; OE max, n. ‘net beside mearg, m. n. ‘marrow, pith’; E mesh; OHG maska, f. ‘mesh’; Ger. Masche, f. *knitting-stitch'; LG masch, id.; MHG masche, f. ‘bow, noose’; Sw. maska, 
==== search mosgos(1) ====
7064:kersno- (2) (keresno-) ‘marrow, brain’. (Prob. same as (1), but cf. kernos (2)) Lat. cf. cerebrum (‘brain’, if fr. *keresno-); Du. hersenen, id.; OHG cf. kirni, Sw. hjerna, id. beside hjesse, ON hjarsi ‘crown of head; Cz. střen ‘bone-marrow, pith’
=== brghus / mrghu region ===
mrg- (2) ‘wipe’ (Variant: morg-. Evidence ambig. Cf. ml-, molé-, etc.) Skt. mrjámi ‘wipe, clean, dry’; Oss. márzin, inf. ‘wipe’; Gk. cf. o-mórgnümi, fut. omórxo, as Skt.
mré- (3) ‘harden, solidify, freeze’ Skt. cf. (ambig.) mūrčhāmi ('solidify', if fr. *mr&sko); Gk. margóno, v. “feel numb’; Alb. mardha, aor. ‘froze, felt cold’; cf. mërdhif, mérdhih, v. (*freeze, feel cold’, fr. *mrgisKo); OCS mrüZzo, mrüzati, & mrüzng, -noti, intr. ‘freeze’ beside mrüZza, f. ice; R mérznut, inf. as OCS; Pol. marznac, as OCS. (Variant in Arm. mardzem ‘coagulate’, fr. *mrgh-)
(mr$- (4), see mrg- (2). Thus in Skt. mrjah ‘wild animal")
mr&hus ‘lopped, crippled, short, docked'. WP II, 314 & cf. II, 175 Av. morozus 'short, lopped'; Hitt. (ambig.) cf. marka(mi) ‘carve up’; Gk. (ambig.) brakhüs (short. See br&hos, us); OHG murg, murgi ‘docked, lopped, short; Go. cf. ga-maürgjan, v. ‘dock; Cz. (ambig.) mrz-ák, m. (cripple, but see mr$- (1))
mrim-, mrm-, mrmn- ‘dead thing, corpse, body’. Cf. WP II, 276 & 293. See mro, mer-, mrt-, etc. Variant: merm-, morm- Skt. marman, n. ‘vital spot; Arm. marmin, gs marmno, ab. s. -ov ‘body; W marm, m. “dead earth, chalk’; Cz. cf. mermo-moci “at all costs’; Ir. cf. marmas (‘nausea’, fr. *mormost-)
mrk- (1) ‘blow, wound’. Cf. mrg- (2). Vari- ant: mərk-; cf. mark- (1) Skt. mræyami, pp: mrktáh, v. ‘injure’; Kurd. cf. merg ‘death’; Hittite (ambig.) mark-, v. (cut, hack. But cf. mrg- 2); LLat. murcus, m. “poltroon, self-mutilator'; Ir. cf. marc, m. mairc, f. (^wound', fr. *mork-). Cf. WP II, 281
mrk- (2) ‘twinkle, blink, shine’. Cz. mrk, m. ‘blinker; blink’; mrkat, mrknout, v. “blink”; R cf. mercàť, inf. ‘glimmer, glint’; Latv. cf. mirklis, Li. mirka, f. “blink”
mrk- (3) “dark, faint; darkness, faintness, stupor’. Cf. mork-
— v=
Skt. cf. mūrčā (‘swoon, stupor’, fr. *mfkiə);
mrð- — mrō, io (mər-)
15
20
25
30
35
40
45
806
OCS mrükng, -noti ‘grow dark’; mrücenije, n. ‘darkness’; Blg. márk, adj. ‘dark’; Srb. mrk, adj. ‘drab, dusky’; beside mrkov, adj. ‘bay — of horse’; Slovak mrk (2) ‘twilight; R cf. mérknut ‘grow dusk’; Ukr. cf. su-merk, m. ‘dusk’
```


## [2026-09-07T17:45:11.341Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^abridge,\\|^abbreviate,\\|^brachy-,\\|^brachial,\" KLN_1966.txt | cut -c1-700; echo \"=== LAT brevis ===\"; grep -n \"brevis\" LAT.txt LEW_1910.txt | head -5"
}
```


### [2026-09-07T17:45:11.424Z] TOOL RESULT

```
=== LAT brevis ===
```


## [2026-09-07T17:45:15.366Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"abridge\\|abbreviate\" KLN_1966.txt | head -5 | cut -c1-800; echo \"=== LEW brev ===\"; grep -n -i \"brevis\\|breuis\" LEW_1910.txt | head -5 | cut -c1-500; echo \"=== LAT brev ===\"; grep -n -i \"brev\" LAT.txt | head -5 | cut -c1-400"
}
```


### [2026-09-07T17:45:15.459Z] TOOL RESULT

```
1140:abbey,  n.,  a  convent  headed  by  an  abbot  or  an abbess.  —  ME.,  fr.  AF.  abbeie,  fr.  OF.  abeie, abaie  (F.  abbaye),  fr.  Eccles.  L.  abbatia,  fr.  L. abbas.  See  abbot  and  cp.  abba,  abbacy,  abbess. Cp.  also  It.  abbadia,  Sp.  abadia,  ‘abbey’,  which also  derive  fr.  Eccles.  L.  abbatia. abbot,  n.  —  OE.  abbod,  fr.  L.  abbat-,  stem  of abbas,  gen.  abbatis,  fr.  Aram,  abbd,  ‘the  father; my  father’,  emphatic  state  of  abh,  ‘father’,  which is  rel.  to  Heb.  abh,  ‘father’.  See  Aboth  and  cp. words  there  referred  to.  Cp.  also  abba,  abbacy, abbe,  abbey,  abuna,  badia. abbreviate,  tr.  v.,  to  shorten.  —  L.  abbrevidtus, pp.  of  ahbrevidre,  ‘to  shorten’,  fr.  ab-  and  bre- vidre,  ‘to  shorten�
1141:abbreviator,  n.  —  L.,  fr.  abbrevidtus,  pp.  of  ab- breviare.  See  abbreviate  and  agential  suff.  -or. Abderian,  pertaining  to  Abdera.  —  See  Abderite and  -ian.
1224:ver,  ‘to  give  drink  to  (animals)’,  fr.  OF.  abevrer, abrever,  fr.  VL.  *abbiberare,  fr.  ad-  and  L. bibere,  ‘to  drink’.  See  beverage,  and  cp.  It.  abbe- verare,  Proven?.,  Catal.  abeurar,  Sp.,  Port,  abre- var,  which  all  derive  fr.  VL.  *abbiberare. abridge,  tr.  v.  —  ME.  abregen,  fr.  OF.  abregier, abreger  (F.  abreger),  ‘to  shorten’,  fr.  L.  abbre- viare,  fr.  ad-  and  breviare,  ‘to  shorten’,  fr.  brevis, ‘short*.  See  brief,  adj.,  and  cp.  abbreviate,  which is  a  doublet  of  abridge.
1225:Derivatives:  abridg-ed,  adj.,  abridg-ed-ly,  adv., abridg-er,  n.,  abridgment  (q.v.) abridgment,  abridgement,  n.  —  OF.  abregement (F.  abregement),  fr.  abregier.  See  abridge  and -ment.
2144:Aldine,  adj.,  printed  by  Aldus  Manutius  (1450- 1515).  —  Formed  with  adj.  suff.  -ine  fr.  Latin- ization  of  It.  Aldo,  an  abbreviated  form  of  Teo- baldo.  See  Theobald.
=== LEW brev ===
=== LAT brev ===
1396:naitre de lotutions comme nil ad rem attinet, puis, par abreviation,
3609:s'est demande si lat. an ne serait pas une forme breve de anne, qui peut
6583:scandent le mot avec la seconde syllabe breve, sans doute pour conser¬
8350:ancien, ainsi que le montre 1 1 abreviation par un S., expliqu^ comme
8965:ImXotc xajieXa, eE, ou xal xapeXeuxCa. Sans autre exeaple. Abreviation
```


## [2026-09-07T17:45:23.705Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%BA%D8%B2/",
 "prompt": "Give the فرهنگ معین (Mo'in) entry for مغز — the definition and any bracketed origin tag such as [په.] (Pahlavi)."
}
```


### [2026-09-07T17:45:29.763Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for مغز

According to the Mo'in dictionary section provided, the entry is:

**(مَ) [په.] (اِ.)**

The definitions listed are:

1. "ماده نرم و خاکستری رنگی که در کاسة سر یا میان استخوان است" — soft grayish matter in the skull or between bones

2. عقل، فکر — intellect, thought

3. شخص دانا و آگاه و نخبه — a knowledgeable, aware, and elite person

4. بخش درونی هر چیزی — the inner part of anything

5. وسط، میان — center, middle

6. درون میوه هایی مانند: گردو، پسته، بادام — the interior of fruits like walnuts, pistachios, almonds

The bracketed origin tag **[په.]** indicates Pahlavi origin.
```


## [2026-09-07T17:45:36.218Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%B2%D8%BA/",
 "prompt": "Does the Persian word مزغ exist? Give the Dehkhoda (لغت‌نامه دهخدا) and any other dictionary entry for مزغ, including whether it means brain/marrow and whether it is described as a variant of مغز."
}
```


## [2026-09-07T17:45:37.478Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%B3%D8%A7%D8%AD%D8%AA/",
 "prompt": "Give the فرهنگ معین entry for مساحت including the bracketed origin tag (e.g. [ع.]) and definition."
}
```


### [2026-09-07T17:45:40.954Z] TOOL RESULT

```
# The Persian Word مزغ

Yes, the word مزغ exists in Persian dictionaries.

**Dehkhoda Dictionary Entry:**
According to Dehkhoda's lexicon, مزغ means "مغز" (marrow/brain) or "مخ" (pith). The entry notes it refers to "the kernel of seeds" and "the pit of fruits," providing examples from classical Persian texts like the Shahnameh.

**Other Dictionary Entries:**
Farhangi Farsi defines it as "marrow" with the sense of "wise lord" or "one possessed of wisdom and prudence." Farhangi Moein similarly lists مزغ as "marrow" (مغز).

**Variant Status:**
The dictionaries present مزغ as a recognized variant or alternate form of مغز rather than a separate word, both referring to brain tissue, fruit kernels, and by extension, wisdom or intellect.
```


### [2026-09-07T17:45:41.254Z] TOOL RESULT

```
# فرهنگ معین Entry for مساحت

According to the dictionary section, the entry is:

"(مِ حَ ) [ ع . مساحة ] (مص م . ) پیمودن یا اندازه گرفتن زمین"

This translates to measuring or determining land dimensions, with the origin marked as Arabic (ع.) from "مساحة" (mesaaha).
```


## [2026-09-07T17:45:46.832Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%B3%DB%8C%D8%AD/",
 "prompt": "Give the فرهنگ معین entry for مسیح including bracketed origin tag and definition (Jesus/anointed), and any note that it is from Hebrew/Aramaic/Syriac."
}
```


### [2026-09-07T17:45:52.722Z] TOOL RESULT

```
# فرهنگ معین Entry for مسیح

According to the Farhang-e Moin section provided:

**(مَ ) \[ ع . \] (ص . ) ۱ - کسی که با روغن مقدس مسح شده باشد. ۲ - مرد بسیار سفر. ۳ - (اِ. ) نام حضرت عیسی .**

This translates roughly to: (1) someone anointed with sacred oil; (2) one who travels extensively; (3) the name of Jesus.

The bracketed notation **\[ ع . \]** indicates the word's origin as Arabic, while **( اِ. )** typically marks Islamic religious terminology. The broader dictionary content confirms this term derives from Hebrew *mashiach* (משיח) and Aramaic *m'shiha*, meaning "anointed one" or "messiah."
```


## [2026-09-07T17:46:14.838Z] TOOL CALL #78: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mosg%CA%B0os|page 342 root Mozgo: PIE *mosgʰos 'marrow, brain' and descendants\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%BA%D8%B2|page 342 node 3: Persian مغز etymology MP mazg < PIr *mazgah\" \\\n \"https://www.etymonline.com/word/marrow|page 342 node 5: English marrow < OE mearg < PGmc *mazga- < PIE *mozgo-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mr%C3%A9%C7%B5%CA%B0us|page 342 root Mreğu: PIE *mréǵʰus 'short' and descendants incl. Proto-Slavic *bъrzъ\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/murguz|page 342 node 6/7: PGmc *murguz 'short' > OE myrge > merry\" \\\n \"https://www.etymonline.com/word/borzoi|page 342 node 3: English borzoi < Russian borzoy 'swift', 1887\" \\\n \"https://en.wiktionary.org/wiki/%D0%B1%D0%BE%D1%80%D0%B7%D0%BE%D0%B9|page 342 node 2: Russian борзой 'swift' < Proto-Slavic *bъrzъ\" \\\n \"https://www.etymonline.com/word/pretzel|page 342 node 9: pretzel < German Brezel < ML brachitella < Gk brakhion\" \\\n \"https://www.etymonline.com/word/messiah|page 342 node 5: Messiah < LL Messias < Gk < Aram meshiha < Heb mashiah\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AD|page 342 node 1/2: Arabic root م س ح masaha 'wipe, anoint', masaha/misaha\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D8%B3%D9%8A%D8%AD|page 342 node 1: Arabic مسيح Masih, relation to Aramaic/Hebrew\" \\\n \"https://abadis.ir/fatofa/%D9%85%D8%BA%D8%B2/|page 342 node 3: Mo'in (MON) entry مغز tagged [په.] Pahlavi\" \\\n \"https://abadis.ir/fatofa/%D9%85%D8%B2%D8%BA/|page 342 node 3: Dehkhoda/Mo'in entry مزغ = مغز, variant form\" \\\n \"https://abadis.ir/fatofa/%D9%85%D8%B3%D8%A7%D8%AD%D8%AA/|page 342 node 2: Mo'in entry مساحت tagged [ع. مساحة]\" \\\n \"https://abadis.ir/fatofa/%D9%85%D8%B3%DB%8C%D8%AD/|page 342 node 2: Mo'in entry مسیح tagged [ع.]\" \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -1; done"
}
```


### [2026-09-07T17:46:26.605Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/56fdf3185ac4a8c4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7239773bf3843389.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/608bc1e6034b80c4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/39ccd85fcdc39f6f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3cf773df3a38e746.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4b70a5fcbdea11ce.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9d6daedc52776590.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1cbf3b0cc42cd6ce.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/105e5994695cbd50.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dbf86f444f6e8584.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/433eab644a2edd98.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1628736c6aa7f2c1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6d41455288577444.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4c3e779c843528e3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9366834f79980dfa.txt
```


## [2026-09-07T17:46:31.543Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg342.png data/verification/sources/refs/ocr/BOOK/342.png && ls -la data/verification/sources/refs/ocr/BOOK/342.png; echo \"=== verify_check usage ===\"; sed -n '1,60p' tools/verify_check.py"
}
```


### [2026-09-07T17:46:31.625Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 75149 Sep  7 13:46 data/verification/sources/refs/ocr/BOOK/342.png
=== verify_check usage ===
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
```


## [2026-09-07T17:46:35.147Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '60,140p' tools/verify_check.py"
}
```


### [2026-09-07T17:46:35.190Z] TOOL RESULT

```
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


## [2026-09-07T17:48:29.157Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT berezi-caxra ===\"; grep -n \"zi-caxra\\|zicaxra\\|razi.caxra\\|b3r3zi\\|bar.zi\" BRT.txt | head; echo; grep -n \"hohen  Räder\\|hohem\\|caxra-  Adj\" BRT.txt | head -5; echo \"=== python leaf calc ===\"; python3 - <<'EOF'\nfor f,off,targets in (('PHD.txt',21,[473]),('NYB_vol2_glossary.txt',8,[2523]),('SKT.txt',20,[11151,11451]),('KLN_1966.txt',None,[1224,1140,5487])):\n    t=open(f,encoding='utf-8',errors='replace').read().split('\\n')\n    leaf=0\n    for i,l in enumerate(t,1):\n        if i in targets:\n            if off is None: print(f,'line',i,'leaf',leaf,'-> printed ~',2*leaf-23,'/',2*leaf-22)\n            else: print(f,'line',i,'leaf',leaf,'-> printed p',leaf-off)\n        leaf+=l.count('\\f')\nEOF"
}
```


### [2026-09-07T17:48:30.828Z] TOOL RESULT

```
=== BRT berezi-caxra ===
4209:I  wo  ? :  äat  aosete  haxa  hasa  "a  barnzis '\sayamnanqm  W.  iS.26.  2)    mit    Instr,
4959:, .  Ailu  maza  m^rr/S  .  .  "ve  awrä  YL  z^.  *malnis  (sd.)  atiAat  pouruye  vTdv^  "vqm 41,  a)  mit  einem  ergänzenden  odsT  yä  im  af^Aaeapjma{^.)Y. 44.1g.  II)in erläuternden  Relativ:  'z'aj  karsvar}  _yff/' schwachdeiktischem  Sinn  'jener,  der'; *ar3zaAi  *savaAi  .  .  imat  iar^ar?  yat\  I)  auf  Vorhergenanntes,  Vorausgehendes :i^amra^sm  V.ip.^t);  39';  —  imS  /-irciv/ j  (Wort  oder  Satz)  zurückweisend;  i)  auf barizist^m  barszimanqm  °3raJ'>  yat  hvars  ein  Substantiv,  a)  adjektivisch,  auch  im avacT  "das  Licht  hier  (und)  jenes  Höchste !  Sinn  unsres  Artikels  (des  schwachtonigen unter  den  Hohen  dort,  was  Sonne  heisst"  'der'):  I  ka"bajiyJ' .  .  paruram  idä  xsäya- Y.  j6. 6.  2)    ohne    solchen    (ausge-  aya"  aAJ^  °vaAyü  k(fbüßyaAyS  brälä  bar-
7137:werden  in  der  Theologie  fünf  Arten  von Feuer  geschieden;  s.  unter  den  einzelnen Adj.:  °tr>m  b3r3zisavat3h3m..vohu.fryämm . .  urvOzist^m  (s.  A  und  2)  . .  väzist^m  (s.  A und  2)..  j/7«/i"ö/n  V. /7.11;  V.  75.40,  Yt 7J.85.  A)  als  Gottheit  (Vazata;  s.  aber Y.7.2)"':  tumas}  ti  °tars  .  ..huiiH  mazi^ta ^a;o/flNy.5.4;  V.51V.  7; — '7ire..yaltusl)mäi aiiinsanqm  spmtanqm  Y. /.  2;  —  a  html 'hnm  gärayemi  .  .  zaohraSyS  Any.  2^;  — hwqm  'tnm  akurahe  inazda  pu^rpm  asa- vamm  asahe  ratam  .  .  vtspe  "tarS  (AP.) yazamaidey.ss.T,  J'-io,  S. 2. 9,  Vyt, 26(?) ;
8467:•  j.,  g.  urvarä-  f.  Tflanze',  meist  Plur.; Sing,  äwich  koll.'*;  oft  göttlich  verehrt; I )  im  AUgemeben,  hauptsächlich  von  den Nutz-  und  NährpSanzen:  eaiti  hsnti  'ranqm sar»fia  "wie  viel  Arten**  von  Pflanzen giebt  es?"  V.5.19  PitZ.;  —  a^ra  »;? raoomti  vUpk  vispSjarvoö  V,5.  19;  — yerihe  paiti  pourujar^a  s»mSoa  usuxlyeinii •rä  Yt  /j,  10;  —  avqm  vanqm  .  .  yä visps.bis(_sd.)  nqma  yqm  upairi  vjspanqm •ranqm  iacxma  nilayal  YL  /2. 1 7 ;  —  vis- paaqm  'ranqm  taoxma  .  .  ysi  hmti bartzisia^a  hubaotaitsmaca  V.  2.  28; 'ranam  (als  Subi.)  zairi^aonanam  tarp- matm  paiti  amäca  *usuxsyänti  Yt7.4'';
10303:—  upäai  hi  (näml.  der  Hündin)  °iBm baraym  .  .  V.  jj.43;  —  ma  °tSm  nipail- yavuka  (sd.)  Yt/7,57;  — yats  {sA.)  °lus .  .  x^ar^^a  .  .  V.5.55;  —  star»tasca  -tui anyfma  ..  avar?tä  YLJ7.  7;  —  agsqm 'tava  (NP.)  kistmte  husiania  .  .  zaran- yapaxsta.pmSnkS  'S.t.i'j.f);  —  ya'ia  nä fryS  .  .  slanta  °tul  (AP.)  sayamanS  (sd.) V.^.25;  —  'tu  (AS.)  ^x^ainUtarftu  tnai bariziia  . .  nisirinuyät  V.  /4. 1 4 ;  Yt  ?.  i  o  2 ; — aisam  vantsnks  °A(/(  AP.)  paiti  *äak»ute (sd.)  ysi  srira   banzis.havanis  Yt, /7,  10;
14871:•  j.  patarvta-  Adj.  'im  Flug  hegTiSeii,i  nipai'.yante(s±)  Äqm  vä 'ti  stairi/Aqrri  vä fliegend':  äsyajgia  (sd.)  vayazibya  °taiibya\°ti  bartzi^  V . ^.  ^i .  b)  auf  die  Frage ". ,  als  ein  paar  fliegende  Vögel"  Y.  57. 28;  i  wo?:  talam  vantanhS . .  gätiis  'ti  ^ätjfante — pasubya  staoralibya  vayaeibya 'taäbya^^  (S'p.  i^^  n.)  Ytij.io;  —  ya^/a  argAaJ yS  parmJnS  (sd.)  fravazänte  "mit  Klein-  1  bartsnul  'ti  gairinqm  V.  2.  23";  Y.^.  26, undOrossviehundmittliegenden Vägeln, .. "1 /0.3; —  :i^armö  baxlmli  zqm  'ti  akura- YtJO.119.  \Vttqm   Yt.6.1,  7.3;  jp.48,'$o,  Y. 13.4g,
14883:—  mä  tg  nr«(sd.)  ume  'ti  Y.  10. 17;  — Jtva..tanBm..nidaiama?..iar»zistaisva[ca] 'ti  gatusva  V.  d).  44  f. ;  —  S  ritlm  gäma  (sd.) frabarat ../warnte  'ti  ntäatai tüirfm gäma frabarat  .  .  atiayralsva  raocshva  itidaiät' H.2.15'";  IS',  V.(5.si,  Ä76;  —  ^avä-\ dasii  usmaya{sA)patiy^^  akunavam  Bh. J.8;  14,  2.  13,  14.  b)  auf  die  Frage wo?:  rätayd  Vtspäku  'ti  banzaku  vispahu va^anayaku  spasS atjhsireYx.io.i,^,'*';  — haoma  raüsaisd.)  gara  'tiY.10.4;  — yaiA^ nmän>m  .  .  v^t^m  barvzi/ie  °ti  banzahi Aarai'^yö paiti  (Sp.  824  m.)  barpzayä  Y.57, a  I ;  1 9 ; — yim  yaz?nte  ra%aistärB  baniassu *ti  aspanqm  Yt.  10.11;  —  l?m  yazata  . . akurö  .  .  xaranasu  -ti  fraspaiti  Yt  J5.  2 ;  i 2 ;  —  tarn  yazata  .  .  frarfrase  kankaine °ti  *aaAä  s>mö  Yt5.  41;  —  nars  asaonS urva  urvarahuca  'ti  . .  sa^ayäti  H.  2.  7 ; 'S;  —  drp/ya(sd.}  'ti  zöaraAi  nmänahe.. V.ig.4;  11;  —  .  .  tnasyatahB  al^a  (sd.) *yBi  *aparaya  'ti  *mastrrjnya  (sd.)  F. je;  c.  a)  Die  räumUche  Vorstellung tritt  zurück:  mihr»m  . .  *yahmi  'ti  /ihrrm
16999:bar^ziäta-
17021:•  g.,  j.  baraziman- Adj. 'hoch':  imä  raeüa bartziit^m  •zimanqm  avat  (sd.)  yai  hvarJ avaaY.36.6i  —  Avan  bar7zisi?m  'zima- nqm Vr.  IQ,  2.
17023:•  j.  bar9zi§-  n.  'Polster,  Kissen':  >?  narS hämS^ätvü  nipaüyeinte  Aqm  vä  paiti  stairis Aqm  vä  paiti  '«/V.J.  27;  —  cvat  alte slairisca  °tisca  aesa  druxs  .  .  fräshaoiti V.  7-9;  —  aitaoa  altahe  aste  (Sp.  340) slairii^a  °zi/^a  hqm.v^rtnattte  V.j.  59;  — ana  'zis  sayamnanqm  (sd.)  V.  lü.  26;  — gätu  *x''aiiii.star»tu  (sd.)  mai  °ziia  V. 7^14.         [Yt5.  loa:  lies  bar^zi/Aav'.]

12891:•  j.  darvj'ain.Jitay-  f.  'langes  Leben': Sfrinami  tava  nara  daäAupaiti  vohu.}xH us.jTti  'jUi  (soll  heissen)  "ich  segne  dich, o  . .,  mit  gutem  Leben,  mit  hohem  Leben, langem  Leben"  Az,  7;  Vyt/.
17207:•  j.  b9r9zi.pad-  Adj.  'mit  hohem,  d.  i. gewölbtem  Fuss"':  vayus  ..  °/äSii (NSm.) '' Yt.  75.  54.
17229:Eig.  'mit  hohem  Speer'.
=== python leaf calc ===
PHD.txt line 473 leaf 79 -> printed p 58
NYB_vol2_glossary.txt line 2523 leaf 145 -> printed p 137
SKT.txt line 11151 leaf 296 -> printed p 276
SKT.txt line 11451 leaf 305 -> printed p 285
KLN_1966.txt line 1140 leaf 13 -> printed ~ 3 / 4
KLN_1966.txt line 1224 leaf 15 -> printed ~ 7 / 8
KLN_1966.txt line 5487 leaf 113 -> printed ~ 203 / 204
```


## [2026-09-07T17:48:35.965Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '17195,17245p' BRT.txt"
}
```


### [2026-09-07T17:48:36.012Z] TOOL RESULT

```
j.  b>r>zi°,  nur  KompA.:  sva.  birtsaiä-.
a   auch  bardiya:  —  Vgl.  CtD.  KZ,  3z.  266,
S3.  592,  GGA.  1S93.   398,  Bthl.  ZDMG.  4S.
ISS,  WklPh.  /Äjf.  1060,  IF.  9.  2S9.  ^r- 136.
Wn.  Venn.BeilT.z.griech.Spr.  9.
dby  Google
96i
b9r3zi.gäd-ra-
•  j.  b^razi-gäSra-*  'hoch'  oder  'laut singend':  yim  zaotärttn  stayala  ahurS  ,  . °r}nt;  yazata  zaeta  .  .  'rd  b)r»zata  vaca YL  lo.  89.
•  j.  b3r?zi.£axra-  Adj.  'mit  hohen  Rä- dern, hochräderig':  mtknm  ..yüvsla,. *ra  fravazaite  Yt.  10.  67.
•  j.  bar9zi-8ä(y)- :  '%i~  Adj.  'von  hoher Einsicht':  'zaiiis'''  (NSm.)  iava  vlstäsps Ytj.  108,  5-19,  17.53; —  sraosfm  "zai- Im'^  (ASm.)  Y.57.  II.
Pü.:  bulatidi\  —  0  Statt  "ii^*  geachr.,  %268. 9;  s.  lu  bawrinay-,  —  ')  Übersetit  das  in vielen  Hds.  (lu  Y.  5/)  beieugte  bfnzai/im.
•  j.  b9r9zi.pad-  Adj.  'mit  hohem,  d.  i. gewölbtem  Fuss"':  vayus  ..  °/äSii (NSm.) '' Yt.  75.  54.
»)  Gdn.  Stnd.  /.  137  'mit  hohen  Stiefeln'.  — —  »)  Them.
•  j.  bar9zi-mita-"  Adj.  'hochgemessen, hochgebaut':  nman?m  ..  't>m  Yt/o.  30; —  Hahe  nmanahe  Yt  IQ.  z8.
')  Oder  »11.  biriä-mil-  (mit  them.  Fleiionl 'hochsiulig',  lu  ai.  mit-  f.?     Vgl.  urunyS.väi-
•  j.  *bar8zi.jr5sta- '>  Adj.  {fem.  'ta-) 'hochgegürtet':  sraohm  .  .  yo  bsrizS  "tö Y.57. 30;  —  frava^ayS  .  .  yä  banzaitrl °ia  Yty.  39.
Pü. :  buland  ai-wyäst,  erl.:  pa  tSr  i  dälastän stmvr.  —  0  So  PI  4,  F  I ;  NA.  biri^yäsf.
•  j.  b9r»zi-räz-  Adj.  (auch  fem.)  'in  der Höhe  gebietend':  tti  Alm  (näml.  daHtam) dasta  maioyllisäopM  °räzpm  Yt.13.100.
Komp.  mit  I-S.  im  t,  Glied-  —  'räz-  Adj., vgl.  ™««-i   ai.   •rSj.  Adj.
•  j.  bar«zi-3avah-  Adj.  Bezeichnung  einer der  fünf  Arten  des  Feuers**:  ättvm  (sd.) 'vaftkim  Y.i-j.  II.
*)  Es  meint  nach  Pii.  und  Zs.  zi.  6  das  Tem- pelfeuei  {varhränpa  niiariärth)  und  zugleich  das dei  täglichen  Gebrauchs  (Bd.  /?.  1 :  älai  äa  i fa  /•ihän  pa  kär  därtnd),  das  nur  Speise,  kein Wasser  verzehrt  (3'arisn  o^aril  äp  ne  i^arll, Bd.  //.  2).  Doch  beachte  man,  dasi  an  der Bd.-Stelle  die  Feuer  iimisava/i-  und  spinii/o' (sd.)  vertauscht  sind.
Eig.  *hahen  Nutzen  gewährend'.  —  Pu. :  hulaad
läl;  Sü.i  udaf;ra}yatih.
•  j.  b^r^züstiina-  Adj.  'mit  hohen  Säulen': nmamm  "nsm  Vytp.
•  j.  bar«zi'änav-  m.  EN.  eines  Gläubigen: °inaos  arahe  asaonö  "des  £.,  Sohns  des A.  .."  Yt/y.  110.
Eig.  'des  Knie«  hoch  sind,  hoehliegen'O;  vgl.
bifzah-  962
ai.  ürdkuajanita;  'jhav-  Adj.  —  0  Jüsti« Deutung  NB.  67  ist  mir  nicht  annehmbai.
•  j.  b«r»zy-aog9t  Adv.  'lautsprechender-
weise,    mit  lauter  Stimme':  b'  vacö  rasa-
j'a«(sd.)  V.8.100.
ASn.  aus  *'asg-.  —  Vgl.  mAs.aog:  —  Pü. : pa  buland  rasäniA').  —  ')  Für^^;  %.paityaog}l No.  2.
•  j.  bar^zy-arStay-  m.  EN.  eines  Gläu- bigen: H5ti  aiaonS  Yt  y.  loi.
Eig.  'mit  hohem  Speer'.
j,  birizyäsl' :  lies  binsi.yäi^.
•  g.  baz'vant-  Adj.  'fest':  dangiii  izyäi 'vaiU  haxmaim  Y.  40. 3.
Bed.  nachPa.  —  Et.?>)  bizr  statt  bu%-;  %36S. 10.—  Pu. :  slawr,  Sü.:  slhülaXaraii.  —  ')  Un- sichres bei  Bh.  Stud.  /.  391.
•  j.  be  Part  zur  Hervorhebung  des  ersten Worts  im  Satz:  zätS  b'  yS  asava  zara- ^u/irS  V.  ig.  46.
Vgl.  öä,  bSü.  —  Pu.:  lässt  da»  Wort  aus.
•  j.  böit  Part,  der  Beteuerung  und  Her- vorhebung, hinter  dem  ersten  Wort  im Satz;  a)  hinter Nom. :  nanm  b°  alavamm.. V. y.  22;  —  iuinm  b'  yäsamHi  x''annö ..  dayata  Ny.j.  ii-  b)  hinter  dem Pron.:  aztm  böit  ..  tä  nipayemi  Ytj.Sg.
Komp.!  M(sd.)+Ä.  —  Pü.  (in  V.  13):  itar.
•  j.  boiwrra-  m.  'Kampf,  Streit':  'ranqm dmitanamca  ..  %wa^sh  (sd.)  Yt/y.  so.
Mit  Int. -Red.  gebildet,  S  103  n.  6.  —  ai.  vgl. bhira-  m.  'Kampf;  Bthl.  IF.  IO.  aoo.
•  j.  banha-  m.  EN.  eines  Gläubigen: '»hahe  sä»ha»hahe  asaonö  "des  ß.,  Sohns des  S.  .."  Yty.  124-
Ar.  'biäsa-  m.  Name  eines  Raubvogels'),  — ai.  bhäsa-  m.  (auch  als  EN.);  mp.  bähai  EN. (=  ai.  ikäsaka-  EN.\  S.  noch  Marquart EranSahr  128.  —  ')  Zn  gr.  ^n;  {eine  Adler- att)  s.  Bthl.  IF.  8.  235.
•  j.  baSra-  m.''  (vll.)  'Krankheit':  'rs  F.  16. Zum'V.  batt:  —  Pü.:  bann,  angeblich  bahüa 'ditficult' >),  wahrscheinlich  i.Ji-  (vgl.  np.  lär 'Faden',  GlrPh.  /  b.  23).  —  'I  ?  Eher  dürfte 'rS  von  einem  Komp.  abgerissen  sein.  — »  Was  ist  banntnn  {iarlan)  im  PPGI.?;  s. Salemann  GIrPh,  /.  327.  15,
•  j.  baz-  V.:  s,  unter  d»bqz-.
•  j.  bazah-  n.  'Höhe,  Tiefe':  avervaitya °zas/a  fra%as{a  .  .ya^a  im  z3,  astica  tm zä  avaiti  °z5  yavaiti  /raiiascit  "soviel  an
[Höhe  und  Breite  als  die  Erde;  und  es  ist I  die  Erde   so   gross  an  Höhe  (Tiefe)  wie
dby  Google
```


## [2026-09-07T17:49:04.545Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (13,14,15,112,113,114,519,520):\n    nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', t[i])\n    print('leaf',i,'nums',nums[:6])\nEOF\npython3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (78,79,80):\n    nums=re.findall(r'(?m)^\\s*(\\d{1,4})\\s*$', t[i])\n    print('leaf',i,'nums',nums[:6],'|',t[i].strip()[:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-07T17:49:05.920Z] TOOL RESULT

```
leaf 13 nums []
leaf 14 nums []
leaf 15 nums []
leaf 112 nums ['193']
leaf 113 nums ['194', '195']
leaf 114 nums ['196', '197']
leaf 519 nums ['968']
leaf 520 nums ['970', '971']
leaf 78 nums [] | ! | Р mng] mind. manag [m^mk! | M mrg, N mana] like, resembling. ~ih: likeness, 
leaf 79 nums [] | yk! | M mryg-] word, spell. marw [mlw! | M mrw, N —, (mary)] herb. marz [mlc | M
leaf 80 nums [] | men- [myn-ytn' | M mn-, N man-] think, consider. „išn: thought, intention, dispo
```


## [2026-09-07T17:49:19.220Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AFM masih ===\"; grep -c \"مسيح\" AFM_pages.txt 2>/dev/null; grep -n \"المسيح\\|مسيح\" AFM_pages.txt | head -3; echo \"=== PLA masih ===\"; grep -n -i \"masih\\|masīh\\|masāha\" incoming/PLA/*.txt 2>/dev/null | head -3; ls incoming/PLA/ 2>/dev/null; echo \"=== AFA ===\"; grep -n -i \"masih\\|mesias\\|masaha\" AFA.txt | head -3; echo \"=== FSD borzoi ===\"; grep -n -i \"borzoi\" FSD_vol1.txt | head -3"
}
```


### [2026-09-07T17:49:19.330Z] TOOL RESULT

```
=== AFM masih ===
1
2059:ورد ذ ره في كتاب ܐܨ ܟܐܝܐ )ܐܨ الفارسي الذي عاش في الميل الرابع المسيح ْ
=== PLA masih ===
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
=== AFA ===
=== FSD borzoi ===
```


## [2026-09-07T17:49:26.405Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"messias\\|masîh\\|masih\" AFA.txt LKT.txt | head -5; echo \"(done)\""
}
```


### [2026-09-07T17:49:26.454Z] TOOL RESULT

```
LKT.txt:3307:'Der  Gesalbte',  gr.  luieaaiaq,  zur  Bezeich- nung Jesu  Christi  in  alle  europäischen Sprachen  übergegangen,  z.  B.  dtsch. Messias,  engl.  Messiah;  frz.  Messie\ russ.  Messija,  poln.  Mesiasz.  Außerdem hieraus  pg.  macio  'sanft,  weich,  glatt' [Constancio  Dicc  667  a].  [DE  298.  ML 5209.  Eguilaz  440  [wo  noch  ar.  maslh 'geschmeidig'  als  Grundwort  angegebea ist].
LKT.txt:5414:masih  1437
LKT.txt:5833:Messias  1437
(done)
```


## [2026-09-07T17:49:29.511Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3298,3312p' LKT.txt"
}
```


### [2026-09-07T17:49:29.565Z] TOOL RESULT

```
'Fackel',  tk.  ebenso  masala;  hieraus serb.  masala;  rum.  masala,  masala 'dass.',  masalagiü.
1433.  Ar.  uiä  sä'-lläh:
Wörtlich  'was  Gott  will',  Ausruf  der Bewunderung,  ebenso  tk.  masalla;  hier- aus rum.  masala  'wunderbar!  Gott schütze  dich!  [sc.  vor  den  bösen  Blik- ken]'.  —  Löbel  EITAP  62.
1434.  Ar.  nia'sara:
'Mühlstein,  Mühle'  [Vb.  'asara  'pressen']; hieraus  sp.  almazara  'Ölmühle',  siz. mäzzara  'Stein,  der  als  Gewicht  oder Gegengewicht  dient'.  [DE  161.  Eguilaz 218.  GrSVociSic  241.
1435.  Ar.  masgid: 'Gebetshaus',  eigentlich  'Ort,  wo  man sich  niederwirft'  [Präfix  ma-  des  Ortes u.  Vb.  sagadu  'sich  niederwerfen,  irpoa- Kuveiv'];  hieraus  sp.  mezquita,  pg.  mes- quita,  it.  meschita,  moschea,  afrz.  mos- quete,  frz.  niosqiiee,  rum.  mo^ea;  ndl. moskee,  engl,  mosk,  nwsque,  dtsch. Moschee;  die  slav.  Formen  sind  über das  tk.  mesged  entstanden:  serb.  mecet, bulg.  medzit,  öech.  mesita,  poln.  meczet, russ.  medef  und  auch  rum.  mecet 'Moschee,  tk.  Friedhof  bei  Bukarest'. [Eguilaz  451/452.
1436.  Ar.  niashara: 'Verspottung,  Possenreifser' ,  hieraus  it. mäschera,  sp.  pg.  mäscara,  mit  rom. Endung  sp.  mascarada,  frz.  mascarade und  hieraus  durch  Abfall  der  letzten Silben  [die  als  Endung  betrachtet  wur- den] frz.  masque;  dtsch.  Maske,  ndl. masker,  maskerade,  engl,  niask,  masque, dän.  maske,  schwed.  mask;  russ.  maska.
maskarad,  ßech.  poln.  maskarada,  serb. maska,  maskara.  Mit  wenig  geänderter Bedeutung  rum.  mäscara  'Schimpf, aber  mascaralic,  n.äscäriciü  'Possen- reifser'.  Dazu  die  Vb.  siz.  ammascari 'großtun',  it.  (dial.  Mailand)  mascarä 'vermummen';  sp.  kat.  amoscarse  'zor- nig werden'.  —  [Diese  Etymologie,  die lautlich  und  begrifflich  keine  Schwieiig- keiten  bietet,  wird  vielfach  abgelehnt; statt  dessen  wird  bes.  langobard.  masca 'Netz'  als  Grundwort  empfohlen,  vgl. KARPF  in  WuS  V,  120/124.]  [Dozy Oost  61/63.  DE  304/309.  Mahn  EtUnt 60/61.  Kluge  301.  GrSVociSic  226. ML  5394.  Anglia  XIII,  106  ff.  517  ff. Wiener  Beiträge  zur  engl.  Philologie XV,  119.
1437.  Hebr.  Masi'ah:
'Der  Gesalbte',  gr.  luieaaiaq,  zur  Bezeich- nung Jesu  Christi  in  alle  europäischen Sprachen  übergegangen,  z.  B.  dtsch. Messias,  engl.  Messiah;  frz.  Messie\ russ.  Messija,  poln.  Mesiasz.  Außerdem hieraus  pg.  macio  'sanft,  weich,  glatt' [Constancio  Dicc  667  a].  [DE  298.  ML 5209.  Eguilaz  440  [wo  noch  ar.  maslh 'geschmeidig'  als  Grundwort  angegebea ist].
1438.  Tk.  maslak:
Auch  maslyk  'Datura  stramonium'  [aus^ ar.  maslük];  hieraus  rum  maslag  'dass.'; cech.  maslak,  maslok,  poln.  maslok 'betäubender  Saft',  mastocznik  'wüten- der Narr.  [Mikl  SIEtWb  184  a,  Karlo- wicz  422.
1439.  Ar.  masraba: 'Trinkgefäß'  [vom  Vb.  sariha  'trinken'],, erst  moderne  Aussprache  für  misraba 'dass.,  kleiner  Krug';  hieraus  mit  ar. Art.  sp.  almojarra  'kleiner  Krug';  über tk.  masrapa  wurde  rum.  nästräpa 'Trinkglas',  nästräpioara;  bulg.  mas- trapa,  serb.  mastraf a  'Becher'.  [DE  179. Eguilaz  238.  M  kl  SIEtWb  184  b.
1440.  Ar.  massa:
'Betasten';  hieraus  frz.  masser,  dtsch. massieren.  [ML  5395.  MWiD  102  (wo als  mögliches  Grundwort  auch  auf  gr. Udoauj  'kneten'  hingewiesen  ist).
```


## [2026-09-07T17:49:35.501Z] AGENT

Now I'll write the verification file.


## [2026-09-07T17:57:53.315Z] TOOL CALL #87: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk342.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 342,\n \"book_page\": 312,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Mozgo, Mozgho\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *mosgʰos (also written *mozgʰo-) 'marrow, brain'\",\n   \"note\": (\"Pokorny 750 has the lemma 'moz-g-o-, moz-g-en-, mos-k-o-', Meaning: brain, with Av. mazga- \"\n            \"'marrow, brain', OHG mar(a)g, OE mearg, ON mergr 'marrow', ChSl. mozgŭ 'brain', OPruss. musgeno, \"\n            \"Toch. A massunt. Walde-Pokorny II 309 heads the same root 'mozgho- „Mark, Hirn“ (oder mazgho-)' — \"\n            \"which is precisely Nourai's double heading 'Mozgo, Mozgho'; the -gh- variant is not his invention. \"\n            \"Wiktionary reconstructs *mosgʰós 'marrow, brain'. Language label (Indo-European) and gloss ('marrow') \"\n            \"are both right; the root also covers 'brain', which is why the Iranian branch glosses shift. \"\n            \"Caution: Pokorny prints a homonymous lemma 'mozgho-s „junges Rind“' (Arm. mozi, Gk. moskhos) on the \"\n            \"same p.750; Nourai's second variant is NOT that root but WP's spelling of the marrow root. \"\n            \"One further observation on the printed chart: the Avestan box of entry 1 (Mreğu) has an arrow to a \"\n            \"completely EMPTY box — see that entry's note.\"),\n   \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *mosgʰos «مغز (استخوان)، مغز سر». پوکورنی (ص ۷۵۰) آن را با ضبط \"\n               \"moz-g-o- / moz-g-en- آورده و والده–پوکورنی (ج ۲ ص ۳۰۹) درست به همان صورتی که نورایی نوشته است، \"\n               \"یعنی mozgho- (یا mazgho-)، سرواژه کرده است؛ پس هر دو صورتِ «Mozgo, Mozgho» در کتاب نورایی بی‌پایه نیست. \"\n               \"برچسب زبانی و معنای ریشه هر دو درست است. تنها نکتهٔ هشدارآمیز این است که پوکورنی در همان صفحه ریشهٔ \"\n               \"همنامِ دیگری *mozgho-s «گاوِ جوان» (ارمنی mozi، یونانی moskhos) دارد که هیچ پیوندی با «مغز» ندارد و \"\n               \"نباید با آن اشتباه شود. ادعای نورایی درست است.\"),\n   \"sources\": [\n     W + \"Reconstruction:Proto-Indo-European/mosgʰos\",\n     \"https://www.etymonline.com/word/marrow\"\n   ],\n   \"ref_check\": [\n     {\"ref\": \"POK:750\", \"status\": \"supports\",\n      \"note\": (\"Pokorny IEW p.750 (POK_full.txt, 'Root / lemma: moz-g-o-, moz-g-en-, mos-k-o-', 'Page(s): 750'): \"\n               \"\\\"Meaning: brain. Material: Old Indic majjan, majja ... Avestan mazga- 'marrow, brain'; Old High German \"\n               \"mar(a)g ... Old English mearg, Old Icelandic mergr 'marrow' ... Church Slavic mozgŭ 'brain'\\\". \"\n               \"Exactly Nourai's root box.\")},\n     {\"ref\": \"KLN:941\", \"status\": \"supports\",\n      \"note\": (\"Klein 1966, leaf 505 of the scan = printed pp.940-941 (running numbers 940, 941 on the leaf), s.v. \"\n               \"'marrow, n.': \\\"ME. maro, merowe, fr. OE. mearg, mearh ... fr. I.-E. base *mozghu-, whence also OI. \"\n               \"majjan-, Avestic mazga-, 'marrow', Toch. A massunt, OSlav. mozgu, OPruss. muzgeno, Lith. smagenes\\\". \"\n               \"grep -n '^marrow,' KLN_1966.txt\")}\n   ],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. II 309\", \"stance\": \"supports\",\n      \"note\": (\"WLD_Bd2_pages.txt leaf 314 (printed 309): \\\"mozgho- „Mark, Hirn“ (oder mazgho-). Ai. majjan- \"\n               \"„Mark“ ..., av. mazga- „Mark, Hirn“: ahd. mar(a)g ... ags. mearg, aisl. mergr ... abg. mozgŭ \"\n               \"„Gehirn“\\\". Source of Nourai's second variant spelling.\")},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mozgo-\", \"stance\": \"supports\",\n      \"note\": \"\\\"mozgo-. Marrow. Germanic *mazgo- in Old English mearg, maerh, marrow: MARROW. [Pok. moz-g-o- 750.]\\\"\"},\n     {\"src\": \"SYN\", \"where\": \"Buck 4.203 p.215 and p.367\", \"stance\": \"supports\",\n      \"note\": (\"p.215 (4.203 BRAIN): \\\"ChSl. mozgu, etc. : Skt. majjan-, ON merg, OE mearg, NE marrow ... all \"\n               \"'marrow' (Av. mazga once, 'marrow' or 'brain'? NPers. maγz both)\\\"; p.367: \\\"OE mearh 'marrow' \"\n               \"(: ON mergr, Skt. majjan-, Av. mazga- 'marrow', ChSl. mozgŭ 'brain')\\\".\")},\n     {\"src\": \"IEC\", \"where\": \"Mann, p.800 s.v. mosgos, ā (1)\", \"stance\": \"partial\",\n      \"note\": (\"Mann heads it \\\"mosgos, ā (1) 'tangle, knot, convolution, brain'. WP II, 308\\\" and lists \\\"Skt. majjā, \"\n               \"f. 'brain'; Av. mazga, f. id.; Per. maγz 'brain, marrow, pith'; ... OE ... mearg\\\" — same word family, \"\n               \"but Mann ties it to the 'mesh/knot' group (mesgō), a grouping other authorities do not follow.\")}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"mazga\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Avestan mazga- m. 'Mark, Gehirn' is attested (once, in the Frahang ī ōīm word-list) and is the \"\n                    \"regular Iranian continuation of Proto-Indo-Iranian *mazgʰas < PIE *mosgʰos: PIE *o > Indo-Iranian a, \"\n                    \"and the cluster *-sgʰ- appears as -zg- with the aspirate lost already in Proto-Indo-Iranian \"\n                    \"(Walde-Pokorny notes that Skt. majjan- with -jj- < *-zjh- shows the loss of aspiration is 'urarisch'). \"\n                    \"Sanskrit majjan-/majjā 'marrow' is the exact cognate. So the arrow root → Avestan mazga- is correct \"\n                    \"in form, language and gloss.\"),\n     \"derivation_fa\": (\"اوستایی mazga- «مغز، مغز استخوان» صورت قانونمند ایرانی باستان از هندوایرانی آغازین *mazgʰas و \"\n                       \"آن از هندواروپایی *mosgʰos است: واکهٔ o هندواروپایی در هندوایرانی به a بدل شده و خوشهٔ *sgʰ به \"\n                       \"-zg- تحول یافته که دمیدگی آن، به گواهی سنسکریت majjan- (با -jj- از *-zjh-)، هنوز در دورهٔ \"\n                       \"هندوایرانی از میان رفته بود. بارتولومه در ستون ۱۱۵۹ فرهنگ ایرانی باستان همین واژه را با معنی \"\n                       \"«مغز» ثبت کرده است. ادعای نورایی درست است.\"),\n     \"sources\": [W + \"Reconstruction:Proto-Indo-European/mosgʰos\"],\n     \"ref_check\": [\n       {\"ref\": \"POK\", \"status\": \"supports\",\n        \"note\": \"Pokorny p.750 s.v. moz-g-o-: \\\"Avestan mazga- 'marrow, brain'\\\".\"},\n       {\"ref\": \"KLN\", \"status\": \"supports\",\n        \"note\": \"Klein pp.940-941 s.v. marrow: \\\"Avestic mazga-, 'marrow'\\\".\"},\n       {\"ref\": \"SYN:367\", \"status\": \"supports\",\n        \"note\": (\"Buck p.367 (5.6x SAUSAGE discussion, printed page number 367 verified on the leaf): \\\"OE mearh \"\n                 \"'marrow' (: ON mergr, Skt. majjan-, Av. mazga- 'marrow', ChSl. mozgŭ 'brain', etc. Walde-P. 2.309)\\\". \"\n                 \"The cited page really does carry the Avestan form.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 1159\", \"stance\": \"supports\",\n        \"note\": (\"BRT.txt (running column numbers 1159/1160 on the leaf): \\\"j. mazga- m. 'Mark, Gehirn': mazgəmca F.4h. \"\n                 \"Ableit. — ai. vgl. majjān- m.; np. maγz, nhd. Mark\\\". Also 'j. mazga-vant- Adj. mit Mark versehen'.\")},\n       {\"src\": \"WLD\", \"where\": \"Bd. II 309\", \"stance\": \"supports\",\n        \"note\": \"\\\"av. mazga- „Mark, Hirn“\\\" listed as first Iranian witness of mozgho-.\"},\n       {\"src\": \"IEC\", \"where\": \"Mann p.800 s.v. mosgos (1)\", \"stance\": \"supports\",\n        \"note\": \"\\\"Av. mazga, f. id. [= 'brain']\\\".\"},\n       {\"src\": \"SYN\", \"where\": \"Buck 4.203, p.215\", \"stance\": \"partial\",\n        \"note\": \"\\\"Av. mazga once, 'marrow' or 'brain'?\\\" — Buck flags that the single attestation leaves the exact sense open.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"mazg\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Middle Persian mazg (Book Pahlavi spelling mzg) 'brain, marrow' continues Old Iranian *mazga- \"\n                    \"unchanged apart from the loss of the thematic ending: Av. mazga- > MP mazg. MacKenzie's Concise \"\n                    \"Pahlavi Dictionary lists it with its Manichaean Middle Persian by-form mgj and the New Persian \"\n                    \"outcome maγz; Nyberg's glossary keys it directly to Bartholomae col. 1159. It is the necessary \"\n                    \"intermediate between Avestan mazga- and NP maγz, so the arrow Avestan → Pahlavi is right.\"),\n     \"derivation_fa\": (\"فارسی میانه (پهلوی) mazg «مغز، مغز سر» — در خط پهلوی mzg — دنبالهٔ بی‌واسطهٔ ایرانی باستان \"\n                       \"*mazga- است و تنها پایانهٔ ستاکی -a را از دست داده است. مکنزی در فرهنگ کوچک پهلوی این واژه را با \"\n                       \"صورت فارسی میانهٔ مانوی mgj و برآمدِ فارسی نوی maγz آورده و نیبرگ نیز آن را مستقیماً به بارتولومه \"\n                       \"(ستون ۱۱۵۹) بازمی‌گرداند. پس حلقهٔ میانی میان اوستایی mazga- و «مغز» فارسی همین است و پیکان کتاب درست است.\"),\n     \"sources\": [W + \"%D9%85%D8%BA%D8%B2\"],\n     \"ref_check\": [\n       {\"ref\": \"BQT:2021\", \"status\": \"supports\",\n        \"note\": (\"Borhan-e Qate' p.2021 = vol. 4 pdf page 104 (BQT_v4_pages.txt), Mo'in's etymological footnote to \"\n                 \"the headword مغز: \\\"اوستا mazga- (دماغ) «بارتولمه ۱۱۵۹»، پهلوی mazg ... رك: پارسی میانه mazg از اوستا \"\n                 \"mazga-\\\" — the cited page states the Pahlavi form and its Avestan source explicitly.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, p. 58 s.v. mazg (scan leaf 79)\", \"stance\": \"supports\",\n        \"note\": \"\\\"mazg [mzg | (M mgj, N maγz)] brain, marrow.\\\" (grep -n '^mazg' PHD.txt)\"},\n       {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (Glossary) p. 137\", \"stance\": \"supports\",\n        \"note\": (\"\\\"mazg [mzg] brain 69*, — Av. (1159) mazga-; MPrs mgj, List 85; Paz. maz(a)g, magz; NP maγz.\\\" \"\n                 \"Nyberg's own reverse index also gives 'mazga-: mazg' and 'mgj: mazg'.\")},\n       {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 986, p. 221\", \"stance\": \"supports\",\n        \"note\": \"\\\"986. meγz 'Gehirn'. ... aw. mazga- 'Gehirn'; phlv. mazg; ai. majján- 'Mark'.\\\"\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"mağz «مغز»; mazğ «مزغ»\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"New Persian مغز maγz 'brain; marrow; kernel' comes from MP mazg by metathesis of the cluster: \"\n                    \"Hübschmann states the rule twice — Persische Studien p.223 \\\"iran. zg = ap. zg = np. γz ... Np. maγz \"\n                    \"'Gehirn' = zd. mazga-, ksl. mozgu, idg. mazgʰo-\\\" and p.266 \\\"g) Ap. zg = np. γz: maγz 'Gehirn' = zd. \"\n                    \"mazga-\\\", asking whether the metathesis to *maγza- had already happened in Old Persian. Horn (no.986) \"\n                    \"gives the same chain and the dialect forms (Baluchi mazg, Shughni maγz, Ossetic maγz). Nourai's second \"\n                    \"form مزغ mazγ is genuine and is in fact the UN-metathesised order preserved as a variant: Dehkhoda and \"\n                    \"Mo'in both record مزغ = مغز (with Shahnama attestations), so it is not a misprint. Both words are real \"\n                    \"Persian words with the glossed sense, and the arrow Pahlavi → Persian is correct.\"),\n     \"derivation_fa\": (\"«مغز» فارسی نو از فارسی میانهٔ mazg است، با قلب (metathesis) خوشهٔ zg به γz. هوبشمان در «مطالعات \"\n                       \"فارسی» دو بار همین قاعده را آورده است: «zg ایرانی = zg پارسی باستان = γz فارسی نو؛ مغز فارسی نو = \"\n                       \"mazga- اوستایی» و حتی می‌پرسد که آیا این قلب در پارسی باستان (*maγza-) روی داده بود یا نه. هرن نیز \"\n                       \"(شمارهٔ ۹۸۶) همین زنجیره را با گونه‌های گویشی (بلوچی mazg، شغنی maγz، آسی maγz) گزارش کرده است. صورت \"\n                       \"دوم، «مزغ»، ساختگی نیست: دهخدا و معین آن را به معنی «مغز» ثبت کرده‌اند و همان ترتیب اصلی و بی‌قلبِ \"\n                       \"واژه است. حاشیهٔ معین بر برهان قاطع (ص ۲۰۲۱) نیز همین ریشه‌شناسی را می‌دهد. ادعای نورایی درست است.\"),\n     \"sources\": [\n       W + \"%D9%85%D8%BA%D8%B2\",\n       \"https://abadis.ir/fatofa/%D9%85%D8%BA%D8%B2/\",\n       \"https://abadis.ir/fatofa/%D9%85%D8%B2%D8%BA/\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"BQT:2021\", \"status\": \"supports\",\n        \"note\": (\"Borhan-e Qate' p.2021 (vol. 4, pdf p.104) headword مغز with Mo'in's footnote: \\\"اوستا mazga- (دماغ) \"\n                 \"«بارتولمه ۱۱۵۹»، پهلوی mazg ... هندی باستان majjan (مغز)، آسی maγz، بلوچی mazg ... شغنی maγz (مغز) ... \"\n                 \"«هوبشمان ۹۸۹»\\\" — the exact chain Nourai draws.\")},\n       {\"ref\": \"SYN:215\", \"status\": \"supports\",\n        \"note\": (\"Buck p.215 (4.203 BRAIN, printed page number verified on the leaf): \\\"(Av. mazga once, 'marrow' or \"\n                 \"'brain'? NPers. maγz both)\\\" — the cited page carries the Persian word and its Avestan cognate.\")},\n       {\"ref\": \"MON:4063\", \"status\": \"supports\",\n        \"note\": (\"Mo'in, Farhang-e Farsi s.v. مغز: \\\"(مَ) [په.] (اِ.) ماده نرم و خاکستری رنگی که در کاسهٔ سر یا میان \"\n                 \"استخوان است ...\\\" — tagged [په.] = of Pahlavi origin, i.e. exactly Nourai's Pahlavi → Persian arrow. \"\n                 \"Entry text read through abadis.ir; the printed page number 4063 itself could not be verified, since \"\n                 \"no scan of Mo'in's lexicon volumes is on disk.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"HUB\", \"where\": \"Persische Studien pp. 223 and 266\", \"stance\": \"supports\",\n        \"note\": (\"p.223: \\\"Np. maγz 'Gehirn' = zd. mazga-, ksl. mozgu, idg. mazgʰo-\\\"; p.266: \\\"g) Ap. zg = np. γz: maγz \"\n                 \"'Gehirn' = zd. mazga-\\\"; p.223 also asks \\\"Wurde schon ap. mazga- in *magza- = *maγza- umgestellt?\\\" — \"\n                 \"the metathesis rule behind mazg > maγz.\")},\n       {\"src\": \"HRN\", \"where\": \"Grundriss no. 986, p. 221\", \"stance\": \"supports\",\n        \"note\": \"\\\"986. meγz 'Gehirn'. Kāš. magz, magzī. aw. mazga- 'Gehirn'; phlv. mazg; ai. majján- 'Mark'.\\\"\"},\n       {\"src\": \"ARY\", \"where\": \"Aryanpur, printed p. 475 (pdf p.474 of ARY_latin_index_pages.txt)\", \"stance\": \"supports\",\n        \"note\": (\"Aryanpur's مغز entry lists the chain \\\"MAZGA (AVESTAN) / MAZGH (OLD PERSIAN) / MAZGA, MASG (PAHLAVI) / \"\n                 \"MAGHZ (OSSETIC) / MEGZ, MEJU (KURDISH) / MAZHG (BALUCHI) / MAGHZA (AFGHANI) / MASSUNT (TOKHARIAN A) / \"\n                 \"MAJJAN (SANSKRIT)\\\" beside Germanic MARG, MARAG / MEARH, MEARG / MARROW (ENGLISH).\")},\n       {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. مزغ (via abadis)\", \"stance\": \"supports\",\n        \"note\": \"Mo'in and Dehkhoda both give مزغ as 'مغز', with classical (Shahnama) attestation — Nourai's second Persian form is real.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Germanic\", \"words\": \"mazgâ\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Nourai's 'mazgâ' is Proto-Germanic *mazgą (neuter a-stem; Watkins prints it as Germanic *mazgō-), \"\n                    \"the regular Germanic outcome of PIE *mosgʰos: PIE *o > Gmc a, and the medial *-sgʰ- gives -zg- with \"\n                    \"Germanic voicing. Its attested reflexes are OHG mar(a)g/marc, OS marg, OE mearg/mearh, ON mergr \"\n                    \"(gen. mergjar), all 'marrow'. The node carries no reference in the book, but the reconstruction is \"\n                    \"standard. Note the a > ar development is Germanic vocalisation of the syllabic sequence, giving \"\n                    \"mar(a)g beside mazg-.\"),\n     \"derivation_fa\": (\"صورت «mazgâ»ی نورایی همان ژرمنی آغازین *mazgą (نامِ خنثای ستاک a؛ واتکینز آن را *mazgō- می‌نویسد) \"\n                       \"است که برآمدِ قانونمند *mosgʰos هندواروپایی است: o به a بدل شده و خوشهٔ میانی *sgʰ به -zg- رسیده است. \"\n                       \"بازمانده‌های آن آلمانی علیای باستان mar(a)g، ساکسونی باستان marg، انگلیسی باستان mearg و نورس باستان \"\n                       \"mergr همه به معنی «مغز استخوان» است. این گره در کتاب بی‌ارجاع مانده، اما بازسازی آن در منابع معیار \"\n                       \"پذیرفته است. ادعای نورایی درست است.\"),\n     \"sources\": [\n       W + \"Reconstruction:Proto-Indo-European/mosgʰos\",\n       \"https://www.etymonline.com/word/marrow\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\",\n        \"note\": \"Nourai gives no reference for this node; verified instead against AHD/Watkins, Walde-Pokorny II 309 and Wiktionary (see consulted).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mozgo-\", \"stance\": \"supports\",\n        \"note\": \"\\\"Germanic *mazgo- in Old English mearg, maerh, marrow: MARROW.\\\"\"},\n       {\"src\": \"WLD\", \"where\": \"Bd. II 309\", \"stance\": \"supports\",\n        \"note\": \"\\\"ahd. mar(a)g, mar(a)c, as. marg, ags. mearg, aisl. mergr (gen. mergjar) „Mark“\\\" under mozgho-.\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. p. 276 s.v. Marrow\", \"stance\": \"supports\",\n        \"note\": \"\\\"Marrow, pith. (E.) ME mary, A.S. mearh + Du. merg, [ON] mergr, Swed. märg, Dan. marv, O.H.G. marag ... Zend mazga, marrow; Skt. majjan.\\\"\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"marrow\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Old English mearg / mearh 'marrow' (< Proto-Germanic *mazgą) gave Middle English mary, merowe, \"\n                    \"marowe, whence modern marrow, first in the anatomical sense 'soft tissue inside bones' and by the \"\n                    \"mid-14th century figuratively 'inmost part, essence' (as in 'the marrow of the matter'). The change \"\n                    \"OE -rg/-rh > ME -rw is the usual vocalisation of the velar after r. A completely regular, \"\n                    \"uncontroversial chain; Nourai's Germanic → English arrow is right.\"),\n     \"derivation_fa\": (\"انگلیسی marrow از انگلیسی باستان mearg / mearh «مغز استخوان» (از ژرمنی آغازین *mazgą) است که در \"\n                       \"انگلیسی میانه mary / marowe شد و سپس صورت امروزی را گرفت؛ تبدیل -rg/-rh پایانی به -rw دگرگونی آوایی \"\n                       \"معمول انگلیسی است. معنی نخست آن «مغز استخوان» و از میانهٔ سدهٔ چهاردهم به‌گونهٔ استعاری «جانِ کلام، \"\n                       \"لبّ مطلب» است. این زنجیره کاملاً قانونمند و بی‌اختلاف است. ادعای نورایی درست است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/marrow\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"Watkins 1985 s.v. mozgo- \\\"Marrow ... Old English mearg, maerh, marrow: MARROW. [Pok. moz-g-o- 750.]\\\"; index p.1819 'MARROW mozgo-'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"pp. 940-941 s.v. marrow\", \"stance\": \"supports\",\n        \"note\": \"\\\"marrow, n. — ME. maro, merowe, fr. OE. mearg, mearh, rel. to OS. marg, ON. mergr ... fr. I.-E. base *mozghu-\\\".\"},\n       {\"src\": \"SKT\", \"where\": \"p. 276 s.v. Marrow\", \"stance\": \"supports\",\n        \"note\": \"\\\"Marrow, pith. (E.) ME mary, A.S. mearh ... Zend mazga, marrow; Skt. majjan, ... pith of trees.\\\"\"},\n       {\"src\": \"SYN\", \"where\": \"Buck 4.203, p.215\", \"stance\": \"supports\",\n        \"note\": \"\\\"ON merg, OE mearg, NE marrow, OHG mar(a)g, NHG mark, etc., all 'marrow'\\\".\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Mreğu, Mrğu\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *mréǵʰus ~ *mr̥ǵʰéws 'short'\",\n   \"note\": (\"Pokorny's lemma 'mreghu- mṛghu-', Meaning: short, stands on pp.750-751 — Nourai's POK:750 hits its first \"\n            \"page. Walde-Pokorny II 314 has the identical double heading 'mreghu-, mṛghu- „kurz“'; Watkins/AHD has \"\n            \"'mregh-u-. Short.'; Mann (IEC) has 'mr̥ǵhus „lopped, crippled, short, docked“. WP II, 314'. Wiktionary \"\n            \"reconstructs *mréǵʰus ~ *mr̥ǵʰéws 'short'. Root name, language label and gloss are all correct, and the \"\n            \"second variant Mrğu is the zero-grade *mr̥ǵʰu- (hence the redirect entry on this page). \"\n            \"IMPORTANT chart observation: on the printed page the Avestan box of this entry has an arrow leading to a \"\n            \"box that is entirely BLANK — no language label, no words. The blank box is in the book itself (verified \"\n            \"on the 300/400 dpi render, data/verification/sources/refs/ocr/BOOK/342.png); the extraction simply dropped \"\n            \"it, so no node id exists for it.\"),\n   \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *mréǵʰus «کوتاه». پوکورنی این ریشه را با ضبط mreghu- / mṛghu- در صفحه‌های \"\n               \"۷۵۰–۷۵۱ آورده و والده–پوکورنی (ج ۲ ص ۳۱۴) دقیقاً همان دو صورت را سرواژه کرده است؛ واتکینز (AHD) \"\n               \"mregh-u- و مان (IEC) mr̥ǵhus را می‌آورند. پس نام ریشه، برچسب زبانی و معنای «کوتاه» درست است و صورت دوم \"\n               \"همان درجهٔ صفرِ *mr̥ǵʰu- است (که ارجاع جداگانهٔ همین صفحه به آن اشاره دارد). نکتهٔ چاپی: در صفحهٔ چاپی، از \"\n               \"جعبهٔ اوستایی پیکانی به جعبه‌ای می‌رود که به‌کلّی خالی است؛ این خلأ در خودِ کتاب است و استخراج آن جعبه را \"\n               \"به‌کل نیاورده است.\"),\n   \"sources\": [W + \"Reconstruction:Proto-Indo-European/mr%C3%A9%C7%B5%CA%B0us\"],\n   \"ref_check\": [\n     {\"ref\": \"POK:750\", \"status\": \"supports\",\n      \"note\": (\"Pokorny IEW: \\\"Root / lemma: mreghu- mṛghu-. Meaning: short. Material: Prakr. muhu-, Avestan marazu-jīti-, \"\n               \"-jva- 'βραχυβίος', sogd. murzak 'short'; gr. brakhus 'short' ... Latin brevis ... Gothic gamaurgjan \"\n               \"'shorten', Old High German murgi 'short' ... Old English myrge 'pleasant', engl. merry. Page(s): 750-751\\\".\")}\n   ],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. II 314\", \"stance\": \"supports\",\n      \"note\": (\"\\\"mreghu-, mṛghu- „kurz“. Av. marazu-jīti-, -jva- „βραχυβίος“ ...; gr. brakhus „kurz“ ...; \"\n               \"lat. brevis ...; got. gamaurgjan „verkürzen“, ahd. murg, murgi „kurz“ ..., ags. myrge „kurzweilig“\\\".\")},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mregh-u-\", \"stance\": \"supports\",\n      \"note\": (\"\\\"mregh-u-. Short. I. Suffixed form *mregh-w-i- in Latin brevis ... II. Zero-grade form *mṛghu-. \"\n               \"1. Germanic *murgja- ... 2. Greek brakhus ... 3. Greek comparative brakhion ... [Pok. mreghu- 750.]\\\"\")},\n     {\"src\": \"IEC\", \"where\": \"Mann p. 806 s.v. mr̥ǵhus\", \"stance\": \"supports\",\n      \"note\": (\"\\\"mr̥ǵhus 'lopped, crippled, short, docked'. WP II, 314 ... Av. mərəzuš 'short, lopped'; ... Gk. brakhūs \"\n               \"'short'; OHG murg, murgi 'docked, lopped, short'; Go. cf. ga-maurgjan\\\".\")},\n     {\"src\": \"SYN\", \"where\": \"Buck 12.59 SHORT, p. 884\", \"stance\": \"supports\",\n      \"note\": \"\\\"Av. marazu- ... 3. Lat. brevis : Grk. brakhus (above, 1)\\\"; and \\\"8. Skt. hrasva- : Ir. gerr; Av. marazu- : Grk. brakhus\\\".\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\",\n     \"words\": \"merezu, marazu; merezu-jîti; berez 2; berez-čaxra\",\n     \"verdict\": \"disputed\",\n     \"derivation\": (\"Two of the four items are solid, two are not. (a) mərəzu-/marəzu- 'short' and the compound \"\n                    \"mərəzu-jīti- 'short-lived' (jīti- 'life' from PIE *gʷeih₃-, hence Nourai's cross-reference to Gwei) \"\n                    \"are exactly what Pokorny p.750 (\\\"Avestan marazu-jīti-, -jva- 'βραχυβίος'\\\"), Walde-Pokorny II 314, \"\n                    \"Mann ('Av. mərəzuš') and Buck 12.59 give — confirmed. Nourai's added gloss 'fast' for mərəzu-jīti- \"\n                    \"is however wrong: the word means 'of short life', not 'fast'. (b) 'berez 2 : in short time, fast' and \"\n                    \"'berez-čaxra : with fast wheels' are DISPUTED. Nourai is following Klein p.188 s.v. borzoi, who ties \"\n                    \"Russ. borzoy to \\\"the first element in Avestic berez-cachra, 'having fast-moving wheels'\\\". But \"\n                    \"Bartholomae's Altiranisches Wörterbuch col. 961 glosses the word 'bərəzi.caxra- Adj. „mit hohen \"\n                    \"Rädern, hochräderig“' (Yt.10.67, of Mithra's chariot), i.e. bərəzi- = 'HIGH', the compositional form \"\n                    \"of bərəzant- 'high' (cf. the whole series in the same column: bərəzi.gāθra- 'high/loud singing', \"\n                    \"bərəzi.pad- 'with high foot', bərəzi.stūna- 'with high columns', bərəzy-aogət 'in a loud voice'). \"\n                    \"That bərəz- belongs to PIE *bʰerǵʰ- 'high' (Pokorny 140), an entirely different root from *mréǵʰus \"\n                    \"'short'. So the b-initial forms in this box do not belong under this root on the standard view; \"\n                    \"Nourai's own 'berez 2' numbering shows he knew of a homograph 'berez 1' = 'high', and has split what \"\n                    \"the sources treat as one word.\"),\n     \"derivation_fa\": (\"از چهار مدخل این جعبه دو تا استوار است و دو تا نه. الف) اوستایی mərəzu-/marəzu- «کوتاه» و ترکیب \"\n                       \"mərəzu-jīti- «کوتاه‌زندگی» (با jīti- «زندگی» از *gʷeih₃- که ارجاع نورایی به Gwei همان است) دقیقاً \"\n                       \"همان است که پوکورنی (ص ۷۵۰: «marazu-jīti- = βραχυβίος»)، والده–پوکورنی، مان و باک آورده‌اند؛ \"\n                       \"پس این بخش پذیرفتنی است، هرچند افزودن معنی «تند، سریع» به mərəzu-jīti- نادرست است؛ معنی آن «کوتاه‌عمر» \"\n                       \"است. ب) اما «berez 2» و «berez-čaxra: با چرخ‌های تند» مورد اختلاف است: نورایی از کلاین (ص ۱۸۸، ذیل \"\n                       \"borzoi) پیروی کرده که آن را «دارای چرخ‌های تندرو» می‌خواند، در حالی که بارتولومه در ستون ۹۶۱ فرهنگ \"\n                       \"ایرانی باستان bərəzi.caxra- را «دارای چرخ‌های بلند» معنی کرده و آن را به bərəzant- «بلند» بازمی‌گرداند \"\n                       \"(بسنجید با bərəzi.pad- «بلندپا»، bərəzi.stūna- «بلندستون» در همان ستون). این bərəz- از ریشهٔ \"\n                       \"هندواروپایی *bʰerǵʰ- «بلند» است، نه *mréǵʰus «کوتاه». پس پژوهش امروزی صورت‌های b-آغازینِ این جعبه را \"\n                       \"به این ریشه نمی‌بندد.\"),\n     \"sources\": [\n       W + \"Reconstruction:Proto-Indo-European/mr%C3%A9%C7%B5%CA%B0us\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"POK:750\", \"status\": \"partial\",\n        \"note\": (\"Pokorny p.750 gives \\\"Avestan marazu-jīti-, -jva- 'βραχυβίος'\\\" and sogd. murzak 'short' — supports \"\n                 \"the m-forms, but says nothing about any berez-/bərəzi- form under this root.\")},\n       {\"ref\": \"KLN:188\", \"status\": \"supports\",\n        \"note\": (\"Klein 1966 leaf 110 = printed pp.188-189 (the leaf carries 188/189; leaf 109 shows 186-187), s.v. \"\n                 \"borzoi: \\\"Russ. borzoy, lit. 'quick, swift' ... cogn. with the first element in Avestic berez-cachra, \"\n                 \"'having fast-moving wheels'\\\". This is indeed Nourai's source for 'berez 2' and 'berez-čaxra' — the \"\n                 \"reference supports the claim, but the claim itself is not the standard Iranist view (see BRT below).\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 961\", \"stance\": \"contradicts\",\n        \"note\": (\"\\\"j. bərəzi.caxra- Adj. 'mit hohen Rädern, hochräderig': miθrəm .. yūxta .. °ra fravazaite Yt.10.67\\\"; \"\n                 \"the same column has bərəzi.gāθra-, bərəzi.pad-, bərəzi.stūna-, all with bərəzi- 'high' — so Nourai's \"\n                 \"gloss 'with fast wheels' and the placement of berez- under the 'short' root are against Bartholomae.\")},\n       {\"src\": \"WLD\", \"where\": \"Bd. II 314\", \"stance\": \"partial\",\n        \"note\": (\"Gives \\\"Av. marazu-jīti-, -jva- „βραχυβίος“\\\" for this root; adds explicitly \\\"Aksl. bъrzъ \"\n                 \"„schnell“ kaum hierher ... sondern wohl zu *bher-s- „eilen“\\\", i.e. Walde-Pokorny separates the \"\n                 \"b-initial 'swift' family from mreghu- altogether.\")},\n       {\"src\": \"IEC\", \"where\": \"Mann p. 806 s.v. mr̥ǵhus\", \"stance\": \"partial\",\n        \"note\": \"Lists only \\\"Av. mərəzuš 'short, lopped'\\\" — no berez- form.\"},\n       {\"src\": \"SYN\", \"where\": \"Buck 12.59, p. 884\", \"stance\": \"partial\",\n        \"note\": \"Buck's Avestan entry for 'short' is \\\"Av. marazu-\\\" alone; his 14.21 'swift' list has no bərəzi- item.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Russian\", \"words\": \"borzoy\", \"verdict\": \"plausible\",\n     \"derivation\": (\"Russian борзой borzój is an adjective 'swift, fleet' (of a horse; nowadays chiefly the breed \"\n                    \"adjective), inherited from Old East Slavic бързъ, Proto-Slavic *bъ̑rzъ 'quick'; the dog itself is \"\n                    \"the feminine substantive борзая borzája, so Nourai's gloss 'a fast running wolf hound' belongs \"\n                    \"properly to борзая, not to the adjective. The derivation of *bъrzъ from PIE *mreǵʰu- 'short' \"\n                    \"(via a semantic bridge 'in short time' > 'quickly', and a Slavic *mr- > br-) is genuinely \"\n                    \"contested: Buck p.968-969 gives it with a hedge — \\\"ChSl. brŭzo (adv., Russ.-ChSl. bŭrzyji 'swift, \"\n                    \"brave'), SCr., Slov. brz ... perh. as orig. 'in short time' : Grk. brakhus, Lat. brevis (Machek KZ \"\n                    \"64.264 f.)\\\" — and Wiktionary lists Proto-Slavic *bъ̑rzъ as a likely descendant of *mréǵʰus, but \"\n                    \"Walde-Pokorny II 314 rejects it outright (\\\"kaum hierher ... wohl zu *bher-s- 'eilen'\\\"), and Klein \"\n                    \"and Etymonline connect borzoy only to Czech brzy, SCr. brzo and Lith. burzdus, not to brevis. \"\n                    \"Hence: compatible with part of the literature, not the settled view — plausible.\"),\n     \"derivation_fa\": (\"روسی борзой (borzój) صفتی است به معنی «تند، تیزرو» که از روسی شرقی باستان бързъ و اسلاوی آغازین \"\n                       \"*bъ̑rzъ «تند» به میراث رسیده است؛ نام سگ در اصل صورت مادهٔ همین صفت، борзая (borzája)، است، پس \"\n                       \"معنایی که نورایی داده («تازیِ تندروِ گرگ‌شکار») به صورت مادهٔ آن بازمی‌گردد نه به خودِ صفت. پیوند \"\n                       \"*bъrzъ با ریشهٔ *mreǵʰu- «کوتاه» (با پل معنایی «در زمان کوتاه» > «تند» و تبدیل *mr- به br- در \"\n                       \"اسلاوی) بی‌اختلاف نیست: باک (ص ۹۶۸–۹۶۹) آن را با قید «perh.» می‌آورد و ویکی‌واژه نیز آن را از \"\n                       \"بازماندگان احتمالی *mréǵʰus می‌شمارد، اما والده–پوکورنی (ج ۲ ص ۳۱۴) آن را به‌صراحت رد کرده و به \"\n                       \"*bher-s- «شتافتن» بازمی‌گرداند. پس این پیکان با احتیاط پذیرفتنی است.\"),\n     \"sources\": [\n       W + \"%D0%B1%D0%BE%D1%80%D0%B7%D0%BE%D0%B9\",\n       W + \"Reconstruction:Proto-Indo-European/mr%C3%A9%C7%B5%CA%B0us\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"SYN:969\", \"status\": \"supports\",\n        \"note\": (\"Buck's 14.21 SWIFT, FAST, QUICK discussion, Slavic paragraph, straddling pp.968-969 (the printed \"\n                 \"number 969 is on that page in SYN.txt): \\\"ChSl. brŭzo (adv., Russ.-ChSl. bŭrzyji 'swift, brave'), \"\n                 \"SCr., Slov. brz, Bulg. bŭrz, etc. ... perh. as orig. 'in short time' : Grk. brakhus, Lat. brevis, \"\n                 \"etc. Machek, KZ 64.264 f.\\\" — exactly the claim Nourai draws, with Buck's own 'perh.'.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"WLD\", \"where\": \"Bd. II 314\", \"stance\": \"contradicts\",\n        \"note\": (\"\\\"Aksl. bъrzъ „schnell“ kaum hierher (obwohl „kurz“ und „schnell“ sich vielfach decken; ...) \"\n                 \"sondern wohl zu *bher-s- „eilen“, s. Berneker aaO.\\\" — Walde-Pokorny explicitly denies the connection.\")},\n       {\"src\": \"KLN\", \"where\": \"pp. 188-189 s.v. borzoi\", \"stance\": \"partial\",\n        \"note\": (\"\\\"Russ. borzoy, lit. 'quick, swift', rel. to Czech brzy, Serbo-Croat. brzo, 'quickly', and cogn. with \"\n                 \"Lith. bruzdeti ... burzdus, 'mobile, agile'\\\" — Klein confirms the Slavic word and its meaning but \"\n                 \"does not derive it from the 'short' root; his only IE tie is the (contested) Avestan berez-cachra.\")},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mregh-u- and index\", \"stance\": \"silent\",\n        \"note\": \"Watkins lists BRIEF, BRUMAL, ABBREVIATE, ABRIDGE, MERRY, MIRTH, BRACHY-, BRACE, PRETZEL under mregh-u- — no Slavic or borzoi entry at all.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"English\", \"words\": \"borzoi\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"English borzoi is a straightforward late-19th-century borrowing: Russian борзая borzája (fem. of \"\n                    \"борзой 'swift') 'the swift one', the Russian wolfhound, taken into English in 1887 when the breed \"\n                    \"was first shown and registered in the West, the Russian -ая being anglicised to -oi after the \"\n                    \"masculine борзой. So the arrow Russian → English is exactly right; the only inherited-vs-borrowed \"\n                    \"question on this branch lies one step up, at the Slavic → PIE link (node #2).\"),\n     \"derivation_fa\": (\"انگلیسی borzoi وام‌واژه‌ای است از روسی борзая (صورت مادهٔ борзой «تند»)، نام تازیِ روسی، که در \"\n                       \"۱۸۸۷ م. با نمایش و ثبت این نژاد در غرب به انگلیسی راه یافت و پایانهٔ روسی -ая به قیاسِ صورت نرِ \"\n                       \"борзой به -oi انگلیسی بدل شد. پس پیکان روسی ← انگلیسی درست است و تنها جای تردید یک پله بالاتر، \"\n                       \"در پیوند اسلاوی با ریشهٔ هندواروپایی است.\"),\n     \"sources\": [\n       \"https://www.etymonline.com/word/borzoi\",\n       W + \"%D0%B1%D0%BE%D1%80%D0%B7%D0%BE%D0%B9\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"KLN:188\", \"status\": \"supports\",\n        \"note\": (\"Klein 1966, printed pp.188-189: \\\"borzoi, n., the Russian wolfhound. — Russ. borzoy, lit. 'quick, \"\n                 \"swift'\\\" — the cited page really is the borzoi entry (leaf 110 of the scan; leaf 109 carries 186/187, \"\n                 \"leaf 112 carries 193).\")},\n       {\"ref\": \"AHD:153\", \"status\": \"not_checked\",\n        \"note\": (\"Nourai's AHD page numbers refer to the main text of the 1975/76 American Heritage New College \"\n                 \"Edition, which is not open online; the volume on disk (Watkins 1985, IE roots only) has no 'borzoi' \"\n                 \"entry (grep -i borzoi AHD_watkins1985.txt → nothing), and Watkins does not list borzoi among the \"\n                 \"reflexes of mregh-u-. So AHD p.153 is presumably the dictionary headword 'borzoi', unverifiable here.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"pp. 188-189 s.v. borzoi\", \"stance\": \"supports\",\n        \"note\": \"\\\"borzoi, n., the Russian wolfhound. — Russ. borzoy, lit. 'quick, swift'\\\".\"},\n       {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. I\", \"stance\": \"silent\",\n        \"note\": \"grep -i 'borzoi' FSD_vol1.txt returns nothing — the 1913 New Standard's OCR does not yield the headword.\"},\n       {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, vol. 1\", \"stance\": \"silent\",\n        \"note\": \"Not retrievable for this word from the available scan; recorded as silent rather than cited.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Latin\", \"words\": \"brevis\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Latin brevis 'short' goes back to Proto-Italic *breɣʷis < PIE *mreǵʰw-i-: initial *mr- becomes \"\n                    \"br- in Italic (as in Greek), and the labiovelar reflex of *ǵʰw appears as -v- between vowels. \"\n                    \"Walde-Pokorny II 314 notes that the form starts from the feminine *brevī(s) (older *breu̯i), and \"\n                    \"adds the derivative brūma 'winter solstice, winter' < *brevi-ma 'time of the shortest days'. \"\n                    \"Nourai's Latin box and its gloss are correct; the only thing his single arrow from the root hides \"\n                    \"is the Proto-Italic stage.\"),\n     \"derivation_fa\": (\"لاتینی brevis «کوتاه» از ایتالیکِ آغازین *breɣʷis و آن از *mreǵʰw-i- هندواروپایی است: خوشهٔ \"\n                       \"آغازی *mr- در ایتالیک (همچون در یونانی) به br- بدل شده و بازتاب لب‌کامیِ *ǵʰw در میان دو واکه -v- \"\n                       \"شده است. والده–پوکورنی (ج ۲ ص ۳۱۴) می‌افزاید که صورت از مادهٔ *brevī(s) آغاز شده و مشتق brūma \"\n                       \"«انقلاب زمستانی، زمستان» از *brevi-ma «هنگام کوتاه‌ترین روزها» است. جعبهٔ لاتینی و معنای آن درست \"\n                       \"است؛ تنها مرحلهٔ ایتالیکِ آغازین در نمودار نیامده است.\"),\n     \"sources\": [W + \"Reconstruction:Proto-Indo-European/mr%C3%A9%C7%B5%CA%B0us\"],\n     \"ref_check\": [\n       {\"ref\": \"SYN:969\", \"status\": \"partial\",\n        \"note\": (\"Buck p.969 (the Slavic paragraph of 14.21) does name \\\"Grk. brakhus, Lat. brevis\\\" as the comparanda \"\n                 \"of Slavic *bъrzъ, so the page supports the brevis-brakhus equation; but Buck's proper treatment of \"\n                 \"brevis is 12.59 SHORT on p.884: \\\"3. Lat. brevis : Grk. brakhus (above, 1). Hence It. breve, Fr. bref \"\n                 \"(> ME bref, NE brief)\\\". Nourai cites the wrong one of his own two Buck pages.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"WLD\", \"where\": \"Bd. II 314\", \"stance\": \"supports\",\n        \"note\": (\"\\\"lat. brevis (zunächst aus dem Fem. *brevi... ) „kurz“, bruma „Wintersonnenwende, Winter, Kälte“ \"\n                 \"(*brevi-ma „Zeit der kürzesten Tage“)\\\".\")},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mregh-u-\", \"stance\": \"supports\",\n        \"note\": \"\\\"I. Suffixed form *mregh-w-i- in Latin brevis, short (> bruma, the shortest day, winter): BRIEF, BRUMAL; ABBREVIATE, (ABRIDGE).\\\"\"},\n       {\"src\": \"LEW\", \"where\": \"Walde 1910 (LEW_1910.txt)\", \"stance\": \"silent\",\n        \"note\": \"grep -i 'brevis|breuis' LEW_1910.txt returns nothing — the b- section of this scan is not usable; recorded as silent.\"},\n       {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (LAT.txt)\", \"stance\": \"silent\",\n        \"note\": \"grep -i 'brev' LAT.txt yields only French 'abréviation' hits, no brevis entry in the OCR; silent.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"brief, abbreviate, abridge\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"All three are Latin brevis in different guises. brief: ME bref, from Old French bref, from Latin \"\n                    \"brevis (the noun 'a brief' from Medieval Latin breve, neuter used as 'short writing, letter, \"\n                    \"document' — whence also German Brief 'letter'). abbreviate: directly from Latin abbreviātus, pp. \"\n                    \"of abbreviāre 'to shorten' (ad- + breviāre < brevis), a learned 15th-century borrowing. abridge: \"\n                    \"the same Latin verb taken the popular way — Late Latin abbreviāre > Old French abregier/abreger \"\n                    \"> ME abregen > abridge; Klein states outright that abbreviate \\\"is a doublet of abridge\\\". Nourai's \"\n                    \"Latin → English arrow is right for all three.\"),\n     \"derivation_fa\": (\"هر سه واژه بازتاب‌های گوناگون brevis لاتینی‌اند. brief از انگلیسی میانهٔ bref، از فرانسهٔ باستان \"\n                       \"bref، از brevis لاتینی (اسمِ آن از breve لاتینی میانه به معنی «نوشتهٔ کوتاه، نامه» که Brief آلمانی \"\n                       \"نیز همان است). abbreviate وام‌واژهٔ کتابی سدهٔ پانزدهم از abbreviātus لاتینی (ad- + breviāre) است، \"\n                       \"و abridge همان فعل از راه مردمی: abbreviāre لاتینی متأخر > abregier فرانسهٔ باستان > abregen \"\n                       \"انگلیسی میانه > abridge. کلاین به‌صراحت می‌گوید abbreviate و abridge دوگانه (doublet)اند. پیکان \"\n                       \"لاتینی ← انگلیسی برای هر سه درست است.\"),\n     \"sources\": [W + \"Reconstruction:Proto-Indo-European/mr%C3%A9%C7%B5%CA%B0us\"],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\",\n        \"note\": \"No reference given in the book for this node; checked against Klein, Watkins/AHD and Buck instead (see consulted).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"vol. I s.v. abbreviate, abridge (letter A, ~p.5); s.v. brief (pp. 202-203)\", \"stance\": \"supports\",\n        \"note\": (\"\\\"abbreviate, tr. v., to shorten. — L. abbreviatus, pp. of abbreviare, 'to shorten', fr. ab- and \"\n                 \"breviare\\\"; \\\"abridge, tr. v. — ME. abregen, fr. OF. abregier ... fr. L. abbreviare ... fr. brevis, \"\n                 \"'short'. See brief, adj., and cp. abbreviate, which is a doublet of abridge\\\"; \\\"brief, n., a summary. \"\n                 \"— ME. bref, fr. OF. (= F.) bref, fr. ML. breve, prop. neut. of L. adj. brevis, 'short'\\\".\")},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mregh-u- and index pp. 1208, 1323\", \"stance\": \"supports\",\n        \"note\": \"\\\"BRIEF, BRUMAL; ABBREVIATE, (ABRIDGE)\\\" under mregh-u-; index: \\\"ABBREVIATE mregh-u-\\\", \\\"ABRIDGE mregh-u-\\\", \\\"BRIEF mregh-u-\\\".\"},\n       {\"src\": \"SYN\", \"where\": \"Buck 12.59, p. 884\", \"stance\": \"supports\",\n        \"note\": \"\\\"Hence It. breve, Fr. bref (> ME bref, NE brief), now mostly of time\\\".\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Germanic\", \"words\": \"murgja\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Nourai's 'murgja' is Watkins's reconstruction verbatim: AHD gives \\\"Zero-grade form *mṛghu-. \"\n                    \"1. Germanic *murgja-, short, also pleasant, joyful\\\". It is the zero-grade *mr̥ǵʰu- with Germanic \"\n                    \"syllabification *mr̥ > mur- and a ja-stem adjective formation; current handbooks head the u-stem \"\n                    \"*murguz 'short, brief' beside the derived ja-stem seen in OE myrge. The attested Germanic reflexes \"\n                    \"are Gothic ga-maurgjan 'to shorten', OHG murg/murgi 'short', murgfāri 'transitory, frail', OE myrge \"\n                    \"'pleasant'. Nourai's gloss 'short, a joy which makes time pass faster' is a paraphrase of Klein's \"\n                    \"\\\"orig. 'that which makes the time short'\\\" — a fair rendering of the semantic shift, not a form claim.\"),\n     \"derivation_fa\": (\"«murgja»ی نورایی همان بازسازی واتکینز است: AHD می‌نویسد «درجهٔ صفر *mṛghu-؛ ژرمنی *murgja- \"\n                       \"„کوتاه، و نیز خوش، شادی‌بخش“». این صورت از درجهٔ صفر *mr̥ǵʰu- است که در ژرمنی *mr̥ به mur- بدل \"\n                       \"شده و صفتی با پسوند ja- ساخته است؛ فرهنگ‌های امروزی سرواژه را *murguz (ستاک u) می‌گیرند و صورت \"\n                       \"ja-دار را در myrge انگلیسی باستان می‌بینند. بازمانده‌ها: گوتی ga-maurgjan «کوتاه کردن»، آلمانی \"\n                       \"علیای باستان murg/murgi «کوتاه» و murgfāri «زودگذر»، انگلیسی باستان myrge «خوش». معنایی که \"\n                       \"نورایی داده بازگفتِ سخن کلاین است («آنچه زمان را کوتاه می‌کند») و تحول معنایی را درست نشان می‌دهد. \"\n                       \"ادعای نورایی درست است.\"),\n     \"sources\": [W + \"Reconstruction:Proto-Germanic/murguz\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": (\"Watkins 1985 s.v. mregh-u-: \\\"II. Zero-grade form *mṛghu-. 1. Germanic *murgja-, short, also pleasant, \"\n                 \"joyful, in: a. Old English myrge, mirige, pleasant: MERRY; b. Germanic *murgitho, pleasantness, in Old \"\n                 \"English myrgth, pleasure, joy: MIRTH.\\\" Nourai's form is copied from here.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"WLD\", \"where\": \"Bd. II 314\", \"stance\": \"supports\",\n        \"note\": \"\\\"got. gamaurgjan „verkürzen“, ahd. murg, murgi „kurz“, murgfari „zerbrechlich“, ags. myrge „kurzweilig“\\\".\"},\n       {\"src\": \"IEC\", \"where\": \"Mann p. 806 s.v. mr̥ǵhus\", \"stance\": \"supports\",\n        \"note\": \"\\\"OHG murg, murgi 'docked, lopped, short'; Go. cf. ga-maurgjan, v. 'dock'\\\".\"},\n       {\"src\": \"KLN\", \"where\": \"p. 968 s.v. merry, adj.\", \"stance\": \"supports\",\n        \"note\": \"\\\"rel. to OHG. murg, murgi, 'short', Goth. [gamaurgjan] ...\\\", with \\\"orig. 'that which makes the time short'\\\".\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"merry\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Old English myrge/myrige/mirig 'pleasing, delightful' — originally, as Klein puts it, \\\"that which \"\n                    \"makes the time short\\\" — gave ME merie, murie and modern merry; the abstract OE myrgð 'pleasure, \"\n                    \"joy' gave mirth. The semantic path 'short (of time)' > 'that shortens the time' > 'pleasant, gay' \"\n                    \"is exactly the one Walde-Pokorny records for the cognate OHG (ags. myrge „kurzweilig“, literally \"\n                    \"'time-shortening'). It should be noted that Skeat's Concise Dictionary (p.285) still derived merry \"\n                    \"from Celtic (\\\"Not a Teutonic word. — Irish and Gael. mear, merry\\\"); that is an abandoned 19th-century \"\n                    \"view, superseded by the *murgja-/*murguz account Nourai follows.\"),\n     \"derivation_fa\": (\"انگلیسی merry از انگلیسی باستان myrge / myrige «خوش، دلپذیر» است که — به گفتهٔ کلاین — در اصل \"\n                       \"«آنچه زمان را کوتاه می‌کند» معنی می‌داده؛ در انگلیسی میانه merie/murie و سپس merry شده است، و اسمِ \"\n                       \"myrgð انگلیسی باستان به mirth رسیده. تحول معنایی «کوتاه (از حیث زمان)» > «زمان‌کوتاه‌کن» > «خوش، \"\n                       \"شادی‌آور» همان است که والده–پوکورنی برای ags. myrge „kurzweilig“ ثبت کرده است. یادکردنی است که \"\n                       \"اسکیت در فرهنگ فشردهٔ خود (ص ۲۸۵) merry را از سلتی می‌گرفت و «غیرژرمنی» می‌خواند؛ این نظر کهنهٔ سدهٔ \"\n                       \"نوزدهم امروز کنار گذاشته شده و همان تحلیلی که نورایی می‌آورد پذیرفته است.\"),\n     \"sources\": [W + \"Reconstruction:Proto-Germanic/murguz\"],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\",\n        \"note\": \"No reference in the book for this node; checked against Klein p.968, Watkins/AHD and Wiktionary *murguz (see consulted).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"p. 968 s.v. merry, adj.\", \"stance\": \"supports\",\n        \"note\": (\"\\\"merry, adj., gay. — ME. merie, murie, fr. OE. myrge, myrige, myrig, mirig, 'pleasing, delightful, \"\n                 \"merry', orig. 'that which makes the time short'; rel. to OHG. murg, murgi, 'short'\\\"; and s.v. mirth \"\n                 \"(p.~1000) \\\"fr. OE. myrigð ... formed with suff. -ð fr. myrige\\\".\")},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mregh-u-; index p. 1853\", \"stance\": \"supports\",\n        \"note\": \"\\\"Old English myrge, mirige, pleasant: MERRY\\\"; index \\\"MERRY mregh-u-\\\", \\\"MIRTH mregh-u-\\\".\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat p. 285 s.v. Merry\", \"stance\": \"contradicts\",\n        \"note\": \"\\\"Merry (C.) M.E. merie, A.S. myrig, merry. Not a Teutonic word. — Irish and Gael. mear, merry, sportive\\\" — an obsolete Celtic etymology, not followed today.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Greek\", \"words\": \"braxus; braxon\", \"verdict\": \"transcription_suspect\",\n     \"derivation\": (\"The first word is right: Greek βραχύς brakhús 'short' < Proto-Hellenic *brəkʰús < PIE *mréǵʰus, \"\n                    \"with the regular Greek treatment of initial *mr- > br- and of *ǵʰ > kh. The second is not a Greek \"\n                    \"word: 'braxon' has no Greek source. The word intended is βραχίων brakhī́ōn 'upper arm', an old \"\n                    \"comparative-type formation to βραχύς (beside the comparative βράσσων < *βράχjων), which the \"\n                    \"grammarians explain, exactly as Nourai's gloss says, as \\\"τοῦ πήχεως βραχύτερος\\\" — 'shorter than \"\n                    \"the forearm' (quoted in Walde-Pokorny II 314). So the gloss is faithful and the derivation is sound; \"\n                    \"only the transliteration is corrupt, and the printed page (rendered at 400 dpi) really does read \"\n                    \"'braxon', so this is Nourai's own misprint, not a scanning error. Read 'braxion'.\"),\n     \"derivation_fa\": (\"واژهٔ نخست درست است: یونانی βραχύς (brakhús) «کوتاه» از هلنیکِ آغازین *brəkʰús و آن از *mréǵʰus، \"\n                       \"با تبدیل قانونمند *mr- آغازی به br- و *ǵʰ به kh. اما «braxon» واژهٔ یونانی نیست؛ صورت مقصود \"\n                       \"βραχίων (brakhī́ōn) «بازو» است، ساختی از گونهٔ برترِ کهن به βραχύς، که دستورنویسان یونانی آن را — \"\n                       \"دقیقاً به همان معنایی که نورایی نوشته — «τοῦ πήχεως βραχύτερος» یعنی «کوتاه‌تر از ساعد» شرح \"\n                       \"کرده‌اند (نقلِ والده–پوکورنی، ج ۲ ص ۳۱۴). پس معنا و ریشه‌شناسی درست است و تنها آوانگاری خراب است؛ \"\n                       \"و چون صفحهٔ چاپی (با تفکیک ۴۰۰ نقطه بر اینچ) هم همین «braxon» را نشان می‌دهد، خطای چاپی کتاب است \"\n                       \"نه خطای خوانش اسکن. صورت درست: braxion.\"),\n     \"error_in\": \"book\",\n     \"book_prints\": \"braxon\",\n     \"correct_form\": \"braxiōn (Greek βραχίων 'upper arm')\",\n     \"sources\": [\n       W + \"Reconstruction:Proto-Indo-European/mr%C3%A9%C7%B5%CA%B0us\",\n       \"https://www.etymonline.com/word/pretzel\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": (\"Watkins 1985 s.v. mregh-u-: \\\"2. Greek brakhus, short: BRACHY-; AMPHIBRACH, TRIBRACH. 3. Greek \"\n                 \"comparative brakhion, shorter, hence also 'upper arm' (as opposed to the longer forearm): BRACE, \"\n                 \"BRACERO, BRACHIUM, BRASSARD, BRASSIERE, PRETZEL; EMBRACE.\\\" The reference spells the second word \"\n                 \"brakhion, confirming that 'braxon' is a slip.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"WLD\", \"where\": \"Bd. II 314\", \"stance\": \"supports\",\n        \"note\": (\"\\\"gr. brakhus „kurz“ ...\\\" and \\\"Gr. brakhiōn „Oberarm“ ist als „τοῦ πήχεως βραχύτερος“ an \"\n                 \"brakhus anzuschließen ..., vgl. brassōn Komp. aus *brakhjōn\\\" — the source of Nourai's gloss.\")},\n       {\"src\": \"KLN\", \"where\": \"pp. 194-195 s.v. brace, n.\", \"stance\": \"supports\",\n        \"note\": (\"\\\"fr. L. brachia, 'the arms' ... fr. Gk. brakhiōn, 'arm', which derives fr. brakhus, 'short', and prop. \"\n                 \"means 'that which is shorter (than the forearm)'\\\" — same analysis, correct spelling.\")},\n       {\"src\": \"SYN\", \"where\": \"Buck 12.59, p. 884; 12.61 note\", \"stance\": \"supports\",\n        \"note\": \"\\\"1. IE ... Grk. brakhus 'short', brakhea 'shallow place'\\\"; Buck also notes brakhus used for 'little' (p.~903).\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"English\", \"words\": \"brace, embrace, pretzel\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"All three reach English from Greek βραχίων through Latin bracchium 'arm'. brace: ME brace from Old \"\n                    \"French brace/brasse 'the two arms' — Latin bracchia, the neuter plural, was reinterpreted in Gallo-\"\n                    \"Romance as a feminine singular, hence the 'clasp, pair' sense. embrace: Old French embracier 'to \"\n                    \"take in one's arms' (en- + brace) > ME embracen. pretzel: German Brezel, MHG brezel/prezel, from \"\n                    \"Medieval Latin brāchitellum/brachitella, diminutive of bracchiātus 'with arms/branches' — a biscuit \"\n                    \"baked in the shape of folded arms; the word entered English with German bakers in 1836. Klein lists \"\n                    \"brace, bracelet, brachial, brassard, braza, embrace and 'bretzel' together under Gk. brakhiōn, so the \"\n                    \"whole node is confirmed.\"),\n     \"derivation_fa\": (\"هر سه واژه از βραχίων یونانی و از راه bracchium لاتینی «بازو» به انگلیسی رسیده‌اند. brace از \"\n                       \"انگلیسی میانه، از فرانسهٔ باستان brace/brasse «دو بازو»: جمع خنثای bracchia لاتینی در گالورومانس \"\n                       \"مفردِ مادّه پنداشته شد و از همین‌جا معنی «گیره، جفت» پیدا کرد. embrace از embracier فرانسهٔ باستان \"\n                       \"(en- + brace) «در آغوش گرفتن». pretzel از Brezel آلمانی، از brezel/prezel آلمانی علیای میانه، از \"\n                       \"brāchitellum لاتینی میانه، مصغّر bracchiātus «بازودار»، یعنی نانی به شکل بازوان درهم‌کشیده، که در \"\n                       \"۱۸۳۶ م. همراه نان‌پزان آلمانی به انگلیسی راه یافت. کلاین نیز brace، bracelet، brachial، brassard، \"\n                       \"embrace و bretzel را همه ذیل brakhiōn یونانی می‌آورد. ادعای نورایی درست است.\"),\n     \"sources\": [\n       \"https://www.etymonline.com/word/pretzel\",\n       W + \"Reconstruction:Proto-Indo-European/mr%C3%A9%C7%B5%CA%B0us\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\",\n        \"note\": \"No reference in the book for this node; checked against Klein pp.194-195, Watkins/AHD and Etymonline (see consulted).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"pp. 194-195 s.v. brace (n. and v.)\", \"stance\": \"supports\",\n        \"note\": (\"\\\"brace, n., clasp, buckle. — ME. brace, fr. OF. brace, brasse, 'the two arms' ... fr. L. brachia, 'the \"\n                 \"arms', pl. (of the neut. noun brachium) mistaken for a fem. sing. noun, fr. Gk. brakhiōn, 'arm' ... \"\n                 \"cp. bracelet, brachial, brassard, braza, embrace, bretzel\\\"; \\\"brace, tr. v., to encompass. — ME., fr. \"\n                 \"OF. bracier, 'to embrace'\\\".\")},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mregh-u-; index pp. 1320, 2129\", \"stance\": \"supports\",\n        \"note\": \"\\\"BRACE, BRACERO, BRACHIUM, BRASSARD, BRASSIERE, PRETZEL; EMBRACE\\\" under Greek brakhion; index \\\"BRACE mregh-u-\\\", \\\"PRETZEL mregh-u-\\\", \\\"EMBRACE mregh-u-\\\".\"},\n       {\"src\": \"WEB\", \"where\": \"Etymonline s.v. pretzel (used in place of the unavailable Webster vol. 2)\", \"stance\": \"supports\",\n        \"note\": \"\\\"pretzel (1836), from German ... Middle High German brezel/prezel, from Medieval Latin brachitella, diminutive of bracchiatus 'with branches, with arms', from brakhion 'an arm'\\\".\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 3,\n   \"root\": \"M.s.h\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Proto-Semitic root *m-š-ḥ 'to wipe, stroke, anoint'\",\n   \"note\": (\"The root is real and Nourai's gloss is accurate. Klein, in the entry Nourai cites, assembles the whole \"\n            \"family: Hebrew māshaḥ 'he anointed' (with mishḥāh 'ointment; consecrated portion'), Aramaic-Syriac \"\n            \"məshaḥ 'he anointed', Syriac meshḥā 'oil', Ethiopic masaḥa 'he anointed; he feasted', Akkadian mashā'u \"\n            \"'to spread (oil) over', Arabic masaḥa 'he stroked or wiped with the hand'. Note that Nourai's 's' stands \"\n            \"for Semitic š (the radicals are m-š-ḥ), and that the semantic core is 'wipe/stroke over a surface', from \"\n            \"which both 'anoint (with oil)' and — in Arabic — 'measure/survey land' develop. The one place where the \"\n            \"chart is out of step with modern scholarship is the Arabic branch: see node #1.\"),\n   \"note_fa\": (\"ریشهٔ سامی *م–ش–ح «مالیدن، سودن، تدهین کردن». نورایی آن را «M.s.h» نوشته که در آن s همان šِ سامی است. \"\n               \"کلاین در همان مدخلی که نورایی ارجاع داده، سراسر خانوادهٔ واژه را گرد آورده است: عبری māšaḥ «تدهین کرد» \"\n               \"(و mishḥāh «روغن مقدس»)، آرامی–سریانی məšaḥ، سریانی meshḥā «روغن»، حبشی masaḥa، اکدی mašāʾu «روغن \"\n               \"گستردن بر»، و عربی مسح «با دست سود». هستهٔ معنایی «سودن بر سطح» است که از آن هم «تدهین» و هم — در \"\n               \"عربی — «مساحی و اندازه‌گیری زمین» برآمده است. تنها جایی که نمودار با پژوهش امروزی نمی‌خواند شاخهٔ عربیِ \"\n               \"«مسیح» است (گرهٔ ۱).\"),\n   \"sources\": [\n     \"https://www.etymonline.com/word/messiah\",\n     W + \"%D9%85%D8%B3%D8%AD\"\n   ],\n   \"ref_check\": [\n     {\"ref\": \"KLN:969\", \"status\": \"supports\",\n      \"note\": (\"Klein 1966 s.v. Messiah: \\\"Aram. məshiha, 'the anointed', fr. Heb. mashiah, 'anointed', fr. mashah, \"\n               \"'he anointed', whence mishhah, 'ointment; consecrated portion'; rel. to Aram.-Syr. məshah, 'he anointed', \"\n               \"mishah, mishhah, Syr. meshha, 'oil', Ethiop. masaha, 'he anointed; he feasted', Akkad. masha'u, 'to spread \"\n               \"(oil) over', Arab. masaha, 'he stroke or wiped with the hand'.\\\" One caveat on the page number: in the \"\n               \"1966 scan this entry sits on the leaf whose running numbers are 970/971 (leaf 520), the preceding leaf \"\n               \"carrying 968; Nourai's '969' is off by about one page, but the entry is unmistakably the one he means.\")}\n   ],\n   \"consulted\": [\n     {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an, pp. 265-266 s.v. al-Masīḥ\", \"stance\": \"partial\",\n      \"note\": (\"\\\"The Muslim authorities usually take it as an Arabic word from [masaḥa] to wipe (Tab. on iii, 20). \"\n               \"Others said it was from [massaḥa] to smear or anoint ... and some, like Zam. and Baiḍ., rejected these \"\n               \"theories and admitted that it was a borrowed word ... we are safer in holding with Fraenkel, Vocab, 24, \"\n               \"that it is from Syr. mšīḥā\\\". Confirms the root but relocates the Arabic word to a loan.\")},\n     {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1437\", \"stance\": \"supports\",\n      \"note\": \"\\\"1437. Hebr. Māšī'aḥ: 'Der Gesalbte', gr. Messias, zur Bezeichnung Jesu Christi in alle europäischen Sprachen übergegangen, z. B. dtsch. Messias, engl. Messiah; frz. Messie; russ. Messija, poln. Mesjasz.\\\"\"},\n     {\"src\": \"AFM\", \"where\": \"Addi Shir, Kitab al-Alfaz al-Farisiyya al-Mu'arraba\", \"stance\": \"silent\",\n      \"note\": \"Only one incidental occurrence of المسيح in a dating formula (AFM_pages.txt line 2059); no headword for the root — as expected, since Addi Shir treats Persian words in Arabic, not Aramaic ones.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Arabic\", \"words\": \"masaha; Masîh; masâhat\", \"verdict\": \"plausible\",\n     \"derivation\": (\"Two of the three are straightforward internal derivations from the Arabic root م س ح: masaḥa \"\n                    \"(مَسَحَ) form I 'he wiped/stroked with the hand, passed the hand over; he anointed', and its verbal \"\n                    \"noun/abstract مِساحة ~ مَساحة misāḥa/masāḥa 'measuring of land, surveying; area' — the sense follows \"\n                    \"from 'to run the hand/measuring rod over a surface', and مسح is still the technical Arabic term for \"\n                    \"'survey'. The third, المسيح al-Masīḥ 'Christ', is where the chart parts company with modern \"\n                    \"scholarship. Formally it looks like a faʿīl passive adjective of masaḥa, and that is how the Muslim \"\n                    \"philologists analysed it (Ṭabarī on Q 3:40, LA iii.431), but Jeffery (Foreign Vocabulary, pp.265-266) \"\n                    \"shows that even Zamakhsharī and Bayḍāwī admitted it was a foreign word, and follows Fraenkel and \"\n                    \"Mingana in taking it from Syriac ܡܫܝܚܐ mšīḥā — the same source that gave Armenian Mesia, Ethiopic \"\n                    \"masīḥ, Manichaean Sogdian msyḥ' and Pahlavi mšyḥ. Wiktionary, by contrast, still calls the Arabic \"\n                    \"word native and merely 'cognate to' the Aramaic and Hebrew forms. So the ultimate root is Nourai's, \"\n                    \"but the route for Masīḥ most probably runs Semitic root > Aramaic/Syriac > Arabic, i.e. the arrow \"\n                    \"should come from the Aramaic box, not straight from the root.\"),\n     \"derivation_fa\": (\"دو مدخل از سه مدخل این جعبه اشتقاق درون‌عربیِ روشن از ریشهٔ «م س ح» است: مَسَحَ «با دست سود، دست \"\n                       \"بر چیزی کشید؛ تدهین کرد» و مصدر/اسم آن «مِساحة ~ مَساحة» «زمین‌پیمایی، مساحت» — معنایی که از \"\n                       \"«کشیدنِ دست یا گز بر سطح» برآمده و «مسح» تا امروز اصطلاح عربی «نقشه‌برداری» است. اما «المسیح» \"\n                       \"جای اختلاف است: از حیث ساخت به صفتِ «فعیل» از مسح می‌ماند و لغویان مسلمان نیز چنین تحلیل کرده‌اند \"\n                       \"(طبری در تفسیر آل‌عمران ۴۵، لسان‌العرب ج۳ ص۴۳۱)، ولی جفری (واژه‌های بیگانه در قرآن، ص ۲۶۵–۲۶۶) \"\n                       \"نشان می‌دهد که حتی زمخشری و بیضاوی آن را دخیل شمرده‌اند و خود او به پیروی از فرنکل و مینگانا آن \"\n                       \"را وام‌واژه‌ای از سریانی mšīḥā می‌داند — همان سرچشمه‌ای که ارمنی، حبشی، سغدی مانوی msyḥ' و پهلوی \"\n                       \"mšyḥ از آن آمده‌اند. ویکی‌واژه در برابر، آن را ساختِ خودِ عربی و تنها «هم‌ریشه» با صورت‌های آرامی و \"\n                       \"عبری می‌خواند. پس ریشهٔ نهایی همان است که نورایی می‌گوید، اما راهِ «مسیح» به احتمال قوی از آرامی/\"\n                       \"سریانی به عربی است و پیکان باید از جعبهٔ آرامی بیاید، نه یکسر از ریشه. با احتیاط پذیرفتنی است.\"),\n     \"sources\": [\n       W + \"%D9%85%D8%B3%D8%AD\",\n       W + \"%D9%85%D8%B3%D9%8A%D8%AD\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"SAP:1569\", \"status\": \"not_checked\",\n        \"note\": (\"SAP = Ahmad Sayyah's Persian translation of al-Munjid (Farhang-e Sayyah). refs_online.json records it \"\n                 \"as kind 'purchase' (fidibo ebook, no open copy) and no local file, so p.1569 could not be opened. The \"\n                 \"content of the claim was instead checked against Klein, Jeffery and Wiktionary.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"s.v. Messiah (leaf 520, pp. 970-971)\", \"stance\": \"supports\",\n        \"note\": \"\\\"Arab. masaha, 'he stroke or wiped with the hand'\\\" — listed as a cognate of Hebrew mashah, exactly the sense Nourai gives.\"},\n       {\"src\": \"FVQ\", \"where\": \"pp. 265-266 s.v. al-Masīḥ\", \"stance\": \"contradicts\",\n        \"note\": (\"On Masīḥ specifically: \\\"Those Muslim philologers who noted it as foreign, claimed that it was Hebrew \"\n                 \"... though such a derivation is extremely unlikely ... we are safer in holding with Fraenkel, Vocab, 24, \"\n                 \"that it is from Syr. mšīḥā, especially as this is the source of the Arm. ..., Eth. ..., the Manichaean \"\n                 \"... and thePazend mashyāḥ; Phlv. ... ; and the Manichaean Soghdian msyh' (Henning)\\\".\")},\n       {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\",\n        \"note\": \"No entry for مسيح / مساحة (grep of PLA_pages.txt) — expected, since Asbaghi covers Persian loans in Arabic only.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\",\n     \"words\": \"Masîh «مسیح»; masâhat «مساحت»; mas-h «مسح»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"All three are Arabic loans in New Persian, taken over after the Islamic conquest with the Arabic \"\n                    \"consonantal skeleton intact. مسیح Masīḥ is the name of Jesus in Persian, borrowed from Arabic \"\n                    \"al-Masīḥ (ultimately, on the prevailing view, Syriac mšīḥā — so for Persian this is a \"\n                    \"Syriac-to-Arabic-to-Persian route, and Persian also has the Christian-Iranian by-form recorded by \"\n                    \"Jeffery as Pahlavi mšyḥ / Pazand mashyāḥ, which reached Middle Persian directly from Syriac). \"\n                    \"مساحت masāḥat is the Arabic maṣdar مساحة with the tāʾ marbūṭa realised as Persian -ت, meaning \"\n                    \"'area, surface area' — Mo'in labels it \\\"[ع. مساحة]\\\". مسح mas-ḥ is the Arabic verbal noun used in \"\n                    \"Persian as a fiqh term, 'wiping (the head and feet) with a wet hand' in the ritual ablution. \"\n                    \"Mo'in tags مسیح simply \\\"[ع.]\\\". The arrow Arabic → Persian is correct for all three.\"),\n     \"derivation_fa\": (\"هر سه واژه وام‌واژهٔ عربی در فارسی نو است و پس از فتح اسلامی با همان ساختِ همخوانی عربی به فارسی \"\n                       \"آمده است. «مسیح» نام حضرت عیسی در فارسی است، از عربی «المسیح» — و چون خودِ صورت عربی به نظر بیشتر \"\n                       \"پژوهشگران وام‌واژه‌ای از سریانی mšīḥā است، راه آن سریانی > عربی > فارسی می‌شود؛ ضمناً جفری صورت \"\n                       \"فارسی میانهٔ mšyḥ و پازندِ mashyāḥ را نیز گزارش کرده که یکسر از سریانی به پهلوی رسیده بود. «مساحت» \"\n                       \"همان مصدر عربی «مساحة» است با تبدیل تای مربوطه به تای فارسی، و معین آن را «[ع. مساحة]» نشانه زده \"\n                       \"است. «مسح» مصدر عربی است که در فارسی اصطلاح فقهی «دست تر بر سر و پا کشیدن» در وضو شده است. معین \"\n                       \"«مسیح» را نیز «[ع.]» می‌داند. پیکان عربی ← فارسی برای هر سه درست است.\"),\n     \"sources\": [\n       \"https://abadis.ir/fatofa/%D9%85%D8%B3%DB%8C%D8%AD/\",\n       \"https://abadis.ir/fatofa/%D9%85%D8%B3%D8%A7%D8%AD%D8%AA/\",\n       W + \"%D9%85%D8%B3%D8%AD\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"FVA:381\", \"status\": \"not_checked\",\n        \"note\": (\"FVA = S. M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), 1368/1989. refs_online.json records \"\n                 \"it as kind 'catalog' — an OpenLibrary record only, with the note \\\"Searched archive.org, ketabnak, \"\n                 \"noorlib, web: no digital copy found\\\" — so p.381 is not consultable. Checked instead against Mo'in \"\n                 \"(via abadis) and Wiktionary.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. مسیح and مساحت (via abadis.ir)\", \"stance\": \"supports\",\n        \"note\": (\"مسیح: \\\"(مَ) [ع.] (ص.) ۱ - کسی که با روغن مقدس مسح شده باشد ... ۳ - (اِ.) نام حضرت عیسی\\\"; \"\n                 \"مساحت: \\\"(مِ حَ) [ع. مساحة] (مص م.) پیمودن یا اندازه گرفتن زمین\\\" — both explicitly tagged as Arabic loans.\")},\n       {\"src\": \"KLN\", \"where\": \"s.v. Messiah (pp. 970-971)\", \"stance\": \"supports\",\n        \"note\": \"\\\"Arab. masaha, 'he stroke or wiped with the hand'\\\" — the Arabic verb behind Persian مسح.\"},\n       {\"src\": \"FVQ\", \"where\": \"p. 266\", \"stance\": \"supports\",\n        \"note\": \"Records the Iranian side of the word directly: \\\"Phlv. [mšyḥ] (Shikand, Glossary, 258)\\\" and \\\"Pazend mashyāḥ\\\", plus \\\"Manichaean Soghdian msyh'\\\".\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Hebrew\", \"words\": \"mâšiah\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Hebrew מָשִׁיחַ māšîaḥ 'anointed (one)' is the qatîl passive adjective of the verb מָשַׁח māšaḥ 'he \"\n                    \"anointed', used in the Hebrew Bible of anointed kings and priests (e.g. 1 Sam 24:7 'the LORD's \"\n                    \"anointed', Lev 4:3 'the anointed priest') and only in post-biblical Jewish usage as the title of \"\n                    \"the awaited deliverer. The formation is entirely regular within Hebrew and the arrow Semitic root \"\n                    \"→ Hebrew is correct; Klein's entry, which Nourai cites, states it in exactly these terms.\"),\n     \"derivation_fa\": (\"عبری מָשִׁיחַ (māšîaḥ) «تدهین‌شده» صفت مفعولیِ وزن qatîl از فعل מָשַׁח (māšaḥ) «تدهین کرد» است و \"\n                       \"در کتاب مقدس عبری برای پادشاهان و کاهنانِ مسح‌شده به کار رفته (مثلاً اول سموئیل ۲۴:۷، لاویان ۴:۳) \"\n                       \"و تنها در کاربرد یهودیِ پس از کتاب مقدس عنوان منجیِ موعود شده است. این ساخت در درون عبری کاملاً \"\n                       \"قانونمند است و پیکان ریشهٔ سامی ← عبری درست است؛ کلاین در همان مدخلی که نورایی ارجاع داده، \"\n                       \"دقیقاً همین را می‌گوید. ادعای نورایی درست است.\"),\n     \"sources\": [\n       \"https://www.etymonline.com/word/messiah\",\n       W + \"%D9%85%D8%B3%D9%8A%D8%AD\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"KLN:969\", \"status\": \"supports\",\n        \"note\": (\"Klein s.v. Messiah: \\\"Heb. mashiah, 'anointed', fr. mashah, 'he anointed', whence mishhah, 'ointment; \"\n                 \"consecrated portion'\\\". (Entry sits on the leaf numbered 970/971 in the 1966 scan; Nourai's 969 is \"\n                 \"one page short.)\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1437\", \"stance\": \"supports\",\n        \"note\": \"\\\"Hebr. Māšī'aḥ: 'Der Gesalbte'\\\" — heads the whole European family under the Hebrew word.\"},\n       {\"src\": \"FVQ\", \"where\": \"pp. 265-266\", \"stance\": \"supports\",\n        \"note\": \"Cites the Hebrew form (משיח) as the one Muslim philologers and many Western scholars appealed to, while preferring Syriac as the immediate source of the Arabic.\"},\n       {\"src\": \"KLN\", \"where\": \"s.v. Messiah\", \"stance\": \"supports\",\n        \"note\": \"Also gives the cognates Aram.-Syr. məshah, Ethiop. masaha, Akkad. masha'u — placing Hebrew within the same Semitic root.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Aramaic\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"An empty pass-through box in the book: the word Nourai means is Aramaic/Syriac ܡܫܺܝܚܳܐ məšīḥā \"\n                    \"'the anointed one', the emphatic (definite) state of məšīḥ, formed on the same root m-š-ḥ and \"\n                    \"matching Hebrew māšîaḥ form for form. Its historical importance is that it, and not the Hebrew \"\n                    \"form, is the immediate source of Greek Μεσσίας (John 1:41, 4:25, where the evangelist glosses it) \"\n                    \"and hence of the whole Western family, and also of Arabic al-Masīḥ, Armenian, Ethiopic, Manichaean \"\n                    \"Sogdian msyḥ' and Pahlavi mšyḥ. So the box is right to sit between Hebrew and English, even though \"\n                    \"it carries no form.\"),\n     \"derivation_fa\": (\"این جعبه در کتاب خالی مانده و صرفاً حلقهٔ گذر است؛ واژهٔ مقصود آرامی/سریانی ܡܫܺܝܚܳܐ (məšīḥā) \"\n                       \"«آن تدهین‌شده» است، یعنی حالت مؤکّد (معرفه) məšīḥ، ساخته بر همان ریشهٔ م–ش–ح و همسانِ صورتِ عبری \"\n                       \"māšîaḥ. اهمیت تاریخی آن این است که سرچشمهٔ بی‌واسطهٔ Μεσσίας یونانی (یوحنا ۱:۴۱ و ۴:۲۵، آنجا که \"\n                       \"خودِ انجیل‌نویس آن را ترجمه می‌کند) و از این راه سرچشمهٔ همهٔ صورت‌های غربی است، و نیز سرچشمهٔ \"\n                       \"«المسیح» عربی، ارمنی، حبشی، سغدی مانوی msyḥ' و پهلوی mšyḥ. پس جای این جعبه میان عبری و انگلیسی \"\n                       \"درست است، هرچند صورتی در آن چاپ نشده است.\"),\n     \"sources\": [\n       \"https://www.etymonline.com/word/messiah\",\n       W + \"%D9%85%D8%B3%D9%8A%D8%AD\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\",\n        \"note\": \"The box carries no word and no reference in the book; verified against Klein and Jeffery (see consulted).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"s.v. Messiah and Messias (pp. 970-971)\", \"stance\": \"supports\",\n        \"note\": (\"\\\"Messiah, n. — Aram. məshiha, 'the anointed', fr. Heb. mashiah\\\"; \\\"Messias, n., the Messiah. — \"\n                 \"Late L., fr. Gk. Messias, fr. Aram. məshiha, 'the anointed'.\\\"\")},\n       {\"src\": \"FVQ\", \"where\": \"pp. 265-266\", \"stance\": \"supports\",\n        \"note\": \"Syriac mšīḥā is \\\"the source of the Arm. ..., Eth. ..., the Manichaean ... and the Pazend mashyāḥ; Phlv. ...; and the Manichaean Soghdian msyh'\\\".\"},\n       {\"src\": \"LKT\", \"where\": \"no. 1437\", \"stance\": \"supports\",\n        \"note\": \"Traces the European words through \\\"gr. Messias\\\", which presupposes the Aramaic emphatic form.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"English\", \"words\": \"Messiah\", \"verdict\": \"plausible\",\n     \"derivation\": (\"The word is right and the ultimate source is right, but the chart's single Aramaic → English arrow \"\n                    \"compresses four steps. The actual route is Aramaic məšīḥā > Greek Μεσσίας (already in the Septuagint \"\n                    \"tradition and John 1:41) > Late Latin Messīās > Old French Messie > Middle English Messie, about \"\n                    \"1300; the modern Hebraising spelling Messiah, which restores the -h of Hebrew māšîaḥ, first appears \"\n                    \"in the Geneva Bible of 1560. Klein keeps the two forms apart as separate headwords precisely to show \"\n                    \"this: 'Messias ... Late L., fr. Gk. Messias, fr. Aram. məshiha'. Nourai's gloss 'Jesus' is right for \"\n                    \"the Christian usage; in Jewish usage the word is the title of the awaited deliverer. Verdict \"\n                    \"plausible rather than confirmed because the Greek, Latin and Old French links are omitted.\"),\n     \"derivation_fa\": (\"واژه و سرچشمهٔ نهایی درست است، اما پیکان یگانهٔ «آرامی ← انگلیسی» چهار مرحله را در خود فشرده \"\n                       \"است. راه واقعی چنین است: آرامی məšīḥā > یونانی Μεσσίας (در سنت سبعینیه و انجیل یوحنا ۱:۴۱) > \"\n                       \"لاتینی متأخر Messīās > فرانسهٔ باستان Messie > انگلیسی میانه Messie (حدود ۱۳۰۰ م.)؛ و املای \"\n                       \"عبری‌نمای امروزی Messiah که h پایانیِ māšîaḥ عبری را بازمی‌گرداند نخست در انجیل ژنو (۱۵۶۰ م.) \"\n                       \"پیدا می‌شود. کلاین همین را با جدا کردن دو مدخل Messiah و Messias نشان داده است. معنایی که نورایی \"\n                       \"داده («عیسی») برای کاربرد مسیحی درست است؛ در کاربرد یهودی، عنوانِ منجیِ موعود است. حکم «با احتیاط \"\n                       \"پذیرفتنی» است، زیرا حلقه‌های یونانی، لاتینی و فرانسهٔ باستان از نمودار افتاده‌اند.\"),\n     \"sources\": [\"https://www.etymonline.com/word/messiah\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"not_checked\",\n        \"note\": (\"Nourai's 'AHD' here must be the main text of the 1975/76 American Heritage New College Edition \"\n                 \"(its Semitic-roots appendix only appeared in the 3rd edition); the volume on disk, Watkins 1985, \"\n                 \"covers Indo-European roots only and has no Semitic entries — grep of AHD_watkins1985.txt for \"\n                 \"'Messiah'/'mshh' returns nothing. Not consultable; checked against Klein, Lokotsch and Etymonline.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"s.v. Messiah / Messias (pp. 970-971)\", \"stance\": \"supports\",\n        \"note\": \"\\\"Messias, n., the Messiah. — Late L., fr. Gk. Messias, fr. Aram. məshiha, 'the anointed'. See Messiah.\\\" — supplies the Greek and Late Latin links the chart omits.\"},\n       {\"src\": \"LKT\", \"where\": \"no. 1437\", \"stance\": \"supports\",\n        \"note\": \"\\\"gr. Messias, zur Bezeichnung Jesu Christi in alle europäischen Sprachen übergegangen, z. B. dtsch. Messias, engl. Messiah; frz. Messie\\\".\"},\n       {\"src\": \"FSD\", \"where\": \"Etymonline s.v. messiah (used in place of the unindexed Funk & Wagnalls volume)\", \"stance\": \"supports\",\n        \"note\": \"\\\"c. 1300 ... from Late Latin Messias, from Greek Messias, from Aramaic (Semitic) meshiha and Hebrew mashiah 'the anointed' ... from mashah 'to anoint' ... The modern spelling ... dates from the Geneva Bible (1560).\\\"\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-342.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk342.py"
}
```


### [2026-09-07T17:57:54.941Z] TOOL RESULT

```
written
```


## [2026-09-07T17:58:00.086Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-342.json > /dev/null && echo \"JSON OK\"; head -c 200 data/verification/page-342.json | xxd | head -2; python3 tools/verify_check.py 342"
}
```


### [2026-09-07T17:58:01.545Z] TOOL RESULT

```
JSON OK
00000000: 7b0a 2020 2270 6466 5f70 6167 6522 3a20  {.  "pdf_page": 
00000010: 3334 322c 0a20 2022 626f 6f6b 5f70 6167  342,.  "book_pag
nodes verified: 19/19
node verdicts: {'confirmed': 14, 'disputed': 1, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 3}
ref checks: {'supports': 14, 'not_checked': 9, 'partial': 2}
books consulted: {'supports': 46, 'partial': 5, 'contradicts': 4, 'silent': 6} | by book: {'KLN': 13, 'WLD': 7, 'AHD': 6, 'SYN': 5, 'FVQ': 4, 'IEC': 3, 'SKT': 3, 'LKT': 3, 'BRT': 2, 'HRN': 2, 'MON': 2, 'FSD': 2, 'WEB': 2, 'PHD': 1, 'NYB': 1, 'HUB': 1, 'ARY': 1, 'LEW': 1, 'LAT': 1, 'PLA': 1}
```


## [2026-09-07T17:58:06.712Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; head -20 tools/verify_archive_sources.py; echo ===; python3 tools/verify_archive_sources.py 342 2>&1 | tail -20"
}
```


### [2026-09-07T17:58:08.354Z] TOOL RESULT

```
Exit code 1
#!/usr/bin/env python3
"""Archive every URL cited in data/verification/page-*.json that is not yet in
data/verification/sources/web/index.jsonl (post-pass, so no cited source is lost
even if an agent forgot to archive it).  Usage: verify_archive_sources.py [pages...]
"""
import sys, os, glob, json, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = os.path.join(ROOT, "data", "verification")
INDEX = os.path.join(VER, "sources", "web", "index.jsonl")

def indexed():
    s = set()
    if os.path.exists(INDEX):
        for line in open(INDEX, encoding="utf-8"):
            try:
                d = json.loads(line)
                if d.get("status") == 200:
                    s.add(d["url"])
            except Exception:
(eval):1: == not found
```


## [2026-09-07T17:58:11.497Z] TOOL CALL #90: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 342 2>&1 | tail -20"
}
```


### [2026-09-07T17:58:13.475Z] TOOL RESULT

```
15 cited URLs, 1 not yet archived
archived 1, failed 0
```


## [2026-09-07T17:58:18.465Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/verify_archive_sources.py 342 2>&1 | tail -3; python3 tools/verify_check.py 342 | grep -c PROBLEM; echo \"problems above (0 expected)\"; git status --short"
}
```


### [2026-09-07T17:58:19.839Z] TOOL RESULT

```
15 cited URLs, 0 not yet archived
archived 0, failed 0
0
problems above (0 expected)
```


## [2026-09-07T17:58:23.715Z] TOOL CALL #92: Bash

```json
{
 "command": "git status --short 2>&1 | head -20"
}
```


### [2026-09-07T17:58:23.772Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T17:58:27.362Z] TOOL CALL #93: Bash

```json
{
 "command": "git status --short | head -20 && echo \"--- branch:\" && git rev-parse --abbrev-ref HEAD && ls -la data/verification/page-342.json"
}
```


### [2026-09-07T17:58:27.438Z] TOOL RESULT

```
--- branch:
verified
-rw-rw-r-- 1 sfmqrb sfmqrb 82789 Sep  7 13:57 data/verification/page-342.json
```


## [2026-09-07T17:58:30.999Z] TOOL CALL #94: Bash

```json
{
 "command": "git status --porcelain=v1 | head; echo \"rc=$?\"; git check-ignore -v data/verification/page-342.json; echo \"---\"; cat .gitignore 2>/dev/null | head -20"
}
```


### [2026-09-07T17:58:32.475Z] TOOL RESULT

```
rc=0
---
# regenerable from the PDF via pdftoppm (see tools/)
data/pages/

# built site (regenerate with tools/build_site.py)
site/risheh.html
__pycache__/

# Verification: OCR texts of copyrighted reference works (local audit copies only)
data/verification/sources/refs/
```


## [2026-09-07T17:58:39.262Z] TOOL CALL #95: Bash

```json
{
 "command": "git status 2>&1 | head -30"
}
```


### [2026-09-07T17:58:39.330Z] TOOL RESULT

```
On branch verified
nothing to commit, working tree clean
```


## [2026-09-07T17:58:43.412Z] TOOL CALL #96: Bash

```json
{
 "command": "git -C /home/sfmqrb/git/rishe status --short 2>&1 | head; echo \"===\"; git -C /home/sfmqrb/git/rishe rev-parse --show-toplevel; echo \"===\"; ls /home/sfmqrb/git/rishe/data/verification/page-34*.json",
 "dangerouslyDisableSandbox": true
}
```


### [2026-09-07T17:58:44.701Z] TOOL RESULT

```
===
/home/sfmqrb/git/rishe
===
/home/sfmqrb/git/rishe/data/verification/page-340.json
/home/sfmqrb/git/rishe/data/verification/page-341.json
/home/sfmqrb/git/rishe/data/verification/page-342.json
/home/sfmqrb/git/rishe/data/verification/page-343.json
/home/sfmqrb/git/rishe/data/verification/page-344.json
/home/sfmqrb/git/rishe/data/verification/page-345.json
/home/sfmqrb/git/rishe/data/verification/page-346.json
/home/sfmqrb/git/rishe/data/verification/page-347.json
/home/sfmqrb/git/rishe/data/verification/page-348.json
/home/sfmqrb/git/rishe/data/verification/page-34.json
```


## [2026-09-07T17:58:49.807Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; git log --oneline -3; git log --oneline -1 -- data/verification/page-342.json; python3 -c \"\nimport json;d=json.load(open('data/verification/page-342.json'));print(d['pdf_page'],d['book_page'],len(d['entries']),[len(e['nodes']) for e in d['entries']])\""
}
```


### [2026-09-07T17:58:51.080Z] TOOL RESULT

```
6371c9f Verify page 344 (Mŭk/muk, mallemuck; Mŭm/mum, mummy; Mŭrâ/mohr, mohreh)
4112750 Verify page 340 (Miždho/moždeh, mozd, meed; M.l.h/malva, Málaga; Moiso/miš)
5eb5a75 Verify page 343 (M.s.s/massage; Mu, Mus/muš, mošk, musk, mouse, muscle)
4112750 Verify page 340 (Miždho/moždeh, mozd, meed; M.l.h/malva, Málaga; Moiso/miš)
342 312 3 [5, 9, 5]
```


## [2026-09-07T17:58:58.962Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; git ls-files --error-unmatch data/verification/page-342.json data/verification/sources/refs/ocr/BOOK/342.png 2>&1 | head"
}
```


### [2026-09-07T17:58:59.021Z] TOOL RESULT

```
error: pathspec 'data/verification/sources/refs/ocr/BOOK/342.png' did not match any file(s) known to git
Did you forget to 'git add'?
data/verification/page-342.json
```


## [2026-09-07T17:59:20.834Z] AGENT

Done — `data/verification/page-342.json` written, valid JSON, `verify_check.py 342` reports **0 PROBLEM** lines (19/19 nodes, 3 roots).

**Page 342 (book p. 312) — verdicts**
- Roots: 3 confirmed (Mozgo/Mozgho, Mreğu/Mrğu, M.s.h; the 4th entry is the Mrğu redirect, skipped).
- Nodes: 14 confirmed · 3 plausible · 1 disputed · 1 transcription_suspect.
- Ref checks: 14 supports, 2 partial, 9 not_checked (SAP, FVA, AHD dictionary-page cites — none available). 61 `consulted` entries across 20 books; 15 web sources archived via fetch_source.py.

**Flagged items**
- `disputed` — Mreğu #1 [Avestan] `berez 2`, `berez-čaxra`: Nourai follows Klein p.188 ("Avestic berez-cachra, 'having fast-moving wheels'"), but Bartholomae AiW col. 961 glosses `bərəzi.caxra-` "mit hohen Rädern" (bərəzi- = 'high', cf. bərəzi.pad-, bərəzi.stūna- in the same column), i.e. PIE *bʰerǵʰ- 'high', a different root. The m-forms (mərəzu-, mərəzu-jīti-) are fine, though the added gloss "fast" for mərəzu-jīti- 'short-lived' is wrong.
- `transcription_suspect` — Mreğu #8 [Greek] `braxon`: not a Greek word; the intended form is βραχίων *brakhiōn* (AHD prints "brakhion"; WP II 314 gives the very gloss "τοῦ πήχεως βραχύτερος"). **error_in = book** — the 400 dpi render of p. 342 really prints "braxon", so it is Nourai's misprint, not an extraction error. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/342.png` (that tree is gitignored).
- `plausible` — Mreğu #2 Russian *borzoy* (Buck p.969 gives the *mreǵʰu-* link only as "perh."; Walde-Pokorny II 314 rejects it outright for *bher-s-*; Wiktionary keeps it); M.s.h #1 Arabic *Masīḥ* (Jeffery FVQ 265–266: a Syriac loan mšīḥā, not internal derivation from masaḥa); M.s.h #5 English *Messiah* (route omits Greek → Late Latin → Old French).

**Extraction issues for the owner**
- Entry 1 (Mreğu): the printed chart has an arrow from the Avestan box to a **completely blank box** (no language, no words). Verified blank on the page image — the blank is in the book; the extractor dropped the box entirely, so it has no node id. Recorded in the entry `note`.
- Minor ref-page slips in the book (not extraction): KLN:969 for *Messiah* sits on p. 970 in the 1966 two-volume scan; SYN:969 for *brevis* is Buck's Slavic paragraph of 14.21 — his actual treatment of brevis is 12.59 on p. 884. Everything else Nourai cites checked out exactly (POK:750 twice, KLN:941, KLN:188, SYN:367, SYN:215, BQT:2021 = vol. 4 pdf p. 104, MON مغز tagged [په.]).
