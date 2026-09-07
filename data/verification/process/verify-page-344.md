# Verification process log — verify-page-344


## [2026-09-07T17:36:16.119Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 344 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-344.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-344.json. Write /home/sfmqrb/git/rishe/data/verification/page-344.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 344` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T17:36:17.896Z] AGENT

I'll start by reading the instructions and the input files.


## [2026-09-07T17:36:18.618Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T17:36:18.632Z] TOOL RESULT

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


## [2026-09-07T17:36:19.324Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-344.txt"
}
```


### [2026-09-07T17:36:19.345Z] TOOL RESULT

```
1	=== PDF page 344 (book page 314) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Mŭk : pile, peak, spike  (refs POK:752; IEC:814)
4	#1 (parent #0) [Persian] refs=IEC:814; MON:4445 | mŭk «موک» : sting
5	#2 (parent #0) [Germanic] refs=AHD:1530 | mŭgôn, mŭhôn : heap
6	  #3 (parent #2) [English] refs=AHD | mow : heap of grain
7	#4 (parent #0) [Old Norse] refs=AHD:1530 | mŭgi : heap
8	  #5 (parent #4) [English] refs=AHD | mogul : a mound on a ski slope
9	#6 (parent #0) [Dutch] refs=AHD:1530 | mocke : thing ; male-mocke : "silly thing", a bird
10	  #7 (parent #6) [English] refs=AHD | mallemuck : a kind of bird
11	--- entry 1 ---
12	ROOT [Persian] Mŭm : wax  (refs BQT:2055)
13	#1 (parent #0) [Arabic] refs=PLA:254; AFM:148 | mŭmîya : wax used in embalming
14	  #2 (parent #1) [Latin] refs=SKT:340 | mumia
15	    #3 (parent #2) [French] refs=None | 
16	      #4 (parent #3) [English] refs=KLN:1014 | mummy, mummery
17	--- entry 2 ---
18	ROOT [Indo-Schythian] Mŭrâ : seal, coin, jewel  (refs ISS:283)
19	#1 (parent #0) [Pahlavi] refs=KLN:993; ISS:284 | mutrâk, mudrâk : ring ; mudar, muhr : seal
20	  #2 (parent #1) [Persian] refs=HRN:224; BQT:2062,2068; ISS:284 | mohr «مُهر ( ممهور ، مهره )» : seal, coin
21	#3 (parent #0) [Sogdian] refs=ISS:284 | mwhrg`n
22	#4 (parent #0) [Sanskrit] refs=KLN:993 | mŭdrâ : coin, seal
23	
```


## [2026-09-07T17:36:19.569Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-344.json"
}
```


### [2026-09-07T17:36:19.582Z] TOOL RESULT

```
1	{
2	  "pdf_page": 344,
3	  "book_page": 314,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Mŭk",
8	        "lang": "Indo-European",
9	        "refs": "POK:752; IEC:814",
10	        "gloss": "pile, peak, spike"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Persian",
17	          "refs": "IEC:814; MON:4445",
18	          "words": [
19	            {
20	              "translit": "mŭk",
21	              "gloss": "sting",
22	              "script": "موک"
23	            }
24	          ],
25	          "script_extra": null,
26	          "note": null,
27	          "quote": null
28	        },
29	        {
30	          "id": 2,
31	          "parent": 0,
32	          "lang": "Germanic",
33	          "refs": "AHD:1530",
34	          "words": [
35	            {
36	              "translit": "mŭgôn, mŭhôn",
37	              "gloss": "heap",
38	              "script": null
39	            }
40	          ],
41	          "script_extra": null,
42	          "note": null,
43	          "quote": null
44	        },
45	        {
46	          "id": 3,
47	          "parent": 2,
48	          "lang": "English",
49	          "refs": "AHD",
50	          "words": [
51	            {
52	              "translit": "mow",
53	              "gloss": "heap of grain",
54	              "script": null
55	            }
56	          ],
57	          "script_extra": null,
58	          "note": null,
59	          "quote": null
60	        },
61	        {
62	          "id": 4,
63	          "parent": 0,
64	          "lang": "Old Norse",
65	          "refs": "AHD:1530",
66	          "words": [
67	            {
68	              "translit": "mŭgi",
69	              "gloss": "heap",
70	              "script": null
71	            }
72	          ],
73	          "script_extra": null,
74	          "note": null,
75	          "quote": null
76	        },
77	        {
78	          "id": 5,
79	          "parent": 4,
80	          "lang": "English",
81	          "refs": "AHD",
82	          "words": [
83	            {
84	              "translit": "mogul",
85	              "gloss": "a mound on a ski slope",
86	              "script": null
87	            }
88	          ],
89	          "script_extra": null,
90	          "note": null,
91	          "quote": null
92	        },
93	        {
94	          "id": 6,
95	          "parent": 0,
96	          "lang": "Dutch",
97	          "refs": "AHD:1530",
98	          "words": [
99	            {
100	              "translit": "mocke",
101	              "gloss": "thing",
102	              "script": null
103	            },
104	            {
105	              "translit": "male-mocke",
106	              "gloss": "\"silly thing\", a bird",
107	              "script": null
108	            }
109	          ],
110	          "script_extra": null,
111	          "note": null,
112	          "quote": null
113	        },
114	        {
115	          "id": 7,
116	          "parent": 6,
117	          "lang": "English",
118	          "refs": "AHD",
119	          "words": [
120	            {
121	              "translit": "mallemuck",
122	              "gloss": "a kind of bird",
123	              "script": null
124	            }
125	          ],
126	          "script_extra": null,
127	          "note": null,
128	          "quote": null
129	        }
130	      ]
131	    },
132	    {
133	      "root": {
134	        "name": "Mŭm",
135	        "lang": "Persian",
136	        "refs": "BQT:2055",
137	        "gloss": "wax"
138	      },
139	      "nodes": [
140	        {
141	          "id": 1,
142	          "parent": 0,
143	          "lang": "Arabic",
144	          "refs": "PLA:254; AFM:148",
145	          "words": [
146	            {
147	              "translit": "mŭmîya",
148	              "gloss": "wax used in embalming",
149	              "script": null
150	            }
151	          ],
152	          "script_extra": null,
153	          "note": null,
154	          "quote": null
155	        },
156	        {
157	          "id": 2,
158	          "parent": 1,
159	          "lang": "Latin",
160	          "refs": "SKT:340",
161	          "words": [
162	            {
163	              "translit": "mumia",
164	              "gloss": null,
165	              "script": null
166	            }
167	          ],
168	          "script_extra": null,
169	          "note": null,
170	          "quote": null
171	        },
172	        {
173	          "id": 3,
174	          "parent": 2,
175	          "lang": "French",
176	          "refs": null,
177	          "words": [],
178	          "script_extra": null,
179	          "note": null,
180	          "quote": null
181	        },
182	        {
183	          "id": 4,
184	          "parent": 3,
185	          "lang": "English",
186	          "refs": "KLN:1014",
187	          "words": [
188	            {
189	              "translit": "mummy, mummery",
190	              "gloss": null,
191	              "script": null
192	            }
193	          ],
194	          "script_extra": null,
195	          "note": null,
196	          "quote": null
197	        }
198	      ]
199	    },
200	    {
201	      "root": {
202	        "name": "Mŭrâ",
203	        "lang": "Indo-Schythian",
204	        "refs": "ISS:283",
205	        "gloss": "seal, coin, jewel"
206	      },
207	      "nodes": [
208	        {
209	          "id": 1,
210	          "parent": 0,
211	          "lang": "Pahlavi",
212	          "refs": "KLN:993; ISS:284",
213	          "words": [
214	            {
215	              "translit": "mutrâk, mudrâk",
216	              "gloss": "ring",
217	              "script": null
218	            },
219	            {
220	              "translit": "mudar, muhr",
221	              "gloss": "seal",
222	              "script": null
223	            }
224	          ],
225	          "script_extra": null,
226	          "note": null,
227	          "quote": null
228	        },
229	        {
230	          "id": 2,
231	          "parent": 1,
232	          "lang": "Persian",
233	          "refs": "HRN:224; BQT:2062,2068; ISS:284",
234	          "words": [
235	            {
236	              "translit": "mohr",
237	              "gloss": "seal, coin",
238	              "script": "مُهر ( ممهور ، مهره )"
239	            }
240	          ],
241	          "script_extra": null,
242	          "note": null,
243	          "quote": {
244	            "text": "بسان سوسن اگر ده زبان شود حافظ - چو غنچه پیش تواش مُهر بر زبان باشد",
245	            "poet": "Hâfez"
246	          }
247	        },
248	        {
249	          "id": 3,
250	          "parent": 0,
251	          "lang": "Sogdian",
252	          "refs": "ISS:284",
253	          "words": [
254	            {
255	              "translit": "mwhrg`n",
256	              "gloss": null,
257	              "script": null
258	            }
259	          ],
260	          "script_extra": null,
261	          "note": null,
262	          "quote": null
263	        },
264	        {
265	          "id": 4,
266	          "parent": 0,
267	          "lang": "Sanskrit",
268	          "refs": "KLN:993",
269	          "words": [
270	            {
271	              "translit": "mŭdrâ",
272	              "gloss": "coin, seal",
273	              "script": null
274	            }
275	          ],
276	          "script_extra": null,
277	          "note": null,
278	          "quote": null
279	        }
280	      ]
281	    }
282	  ]
283	}
284	
```


## [2026-09-07T17:36:23.703Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md | head -120",
 "description": "Read source matrix"
}
```


### [2026-09-07T17:36:23.755Z] TOOL RESULT

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


## [2026-09-07T17:36:26.151Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','MON','AHD','BQT','PLA','AFM','SKT','KLN','ISS','HRN','WLD','SYN','PHD','NYB','SOD','ARY','LKT','FVQ','AFA','WEB','FSD','HJB','ISS_alt_DKS']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False)[:600])\n    else: print(k,'MISSING')\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-07T17:36:27.416Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4
ISS_alt_DKS MISSING
```


## [2026-09-07T17:36:46.398Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD mow/mogul/mallemuck ===\"\ngrep -n -i \"mallemuck\\|mogul\\|mūgôn\\|mugon\\|muhon\" AHD_watkins1985.txt | head -30\necho \"=== AHD meug/muk root ===\"\ngrep -n -i \"^meug\\|^muk\\|meug-\\|mūk\" AHD_watkins1985.txt | head -30",
 "description": "Grep AHD for muk root"
}
```


### [2026-09-07T17:36:46.462Z] TOOL RESULT

```
=== AHD mow/mogul/mallemuck ===
736:Latin micturire, to want to urinate (desiderative of meiere, to urinate): MICTURATE. [Pok. meigh- 713.] meik-. To mix. 1. Variant form *meig- in Greek mig- nunai, to mix: AMPHIMIXIS, APOMIXIS, PANMICTIC, PAN- MIXIS. 2. Suffixed zero-grade form *mik-sk- in Latin miscére (past participle mixtus), to mix: MEDDLE, (MED- LEY), (MELANGE), MESTIZO, MISCELLANEOUS, MISCIBLE, MIX, MIXTURE; ADMIX, COMMIX, IMMIX, MISCEGENATION, (PELL-MELL), PROMISCUOUS. 3. Possibly a Germanic form *maisk- in Old English mdsc, macs, mdx, mashed malt: MASH. [Pok. meik- 714.] mei-no-. Opinion, intention. 1. Germanic *main- in Old English *mdn, opinion, complaint (> Middle English mone, complaint): MOAN; (BEMOAN). 2. Germanic *main- Jan in Old English ménan, to signify, tell, complain of, moan: MEAN}, [Pok. mei-no- 714.] mel-1, Soft; with derivatives referring to soft or softened materials of various kinds. I. Extended form *meld-. 1. Germanic *meltan in Old English meltan, to melt: MELT. 2. Possibly Germanic *miltja- in Old English milte, spleen, and Middle Dutch milte, milt: mit. 3. Possibly Germanic *malta- in Old English mealt, malt: MALT. 4. Suffixed variant form *mled-sno- in Greek blennos, slime, also a name for the blenny: BLENNY. 5. Suffixed zero-grade form *mid-wi- in Latin mollis, soft: MOIL, MOLLIFY, MOLLUSK, MOUILLE; EMOLLIENT; 6. Possibly nasalized variant form *mlad- in Latin blandus, smooth, caressing, flattering, soft-spoken: BLAND, BLANDISH. II. Variant form *smeld-. Germanic *smelt- in: a. Middle Dutch and Middle Low German smelten, to smelt: SMELT!; b. Old High German smalz, animal fat: SCHMALTZ; C. Italian smalto, melted glass: SMALT; d. Old French esmail, enamel: ENAMEL; e. perhaps Old English smelt, smylt, a marine fish, smelt: SMELT?. III. Extended form *meldh-. 1. Germanic *mildja- in Old English milde, mild MILD. 2. Possibly Greek maltha, a mixture of wax and pitch: MALTHA. IV. Suffixed form *mel-sko- in Ger- manic *mil-sk- in Old English melfi)sc, mylsc, mild, mellow (> Middle English melsche, friable): MULCH. V. Extended form *mfk- in Greek malakos, soft: CHON- DROMALACIA, MALACOLOGY, OSTEOMALACIA. VI. Possi- bly Celtic *molto-, sheep, in Old French moton, sheep: MUTTON. VII. Suffixed zero-grade form *()ml-u- in Greek amblus, blunt, dull, dim: AMBLYGONITE, AMBLY- opiA. [Pok. 1. mel- 716.] mel-2, Of a darkish color. 1. Greek melas, black: MEL- ANO-; MELANCHOLY, PSILOMELANE. 2. Greek mullos, a marine fish: MULLET; (SURMULLET). 3. Latin mulleus, reddish purple (used only to designate a ceremonial shoe worn by Roman magistrates): MULE. 4. Perhaps Ger- manic *mal- in Middle Dutch malen, to paint: MAUL- STICK. [Pok. 6. mel- 720.] mel-3. A limb. Greek melos, limb, hence a musical member or phrase, hence music, song, melody: MELISMA; ACRO- MELIC, MELODRAMA, MELODY. [Pok. 5. mel- 720.] mel-4. Strong, great. 1. Suffixed (comparative) form *mel-yos- in Latin melior, better: (AMELIORATE), MELIO- RATE, MELIORISM. 2. Suffixed zero-grade form *m/J-to- in Latin multus (neuter multum), much, many: MOLTO, MULTI-, MULTITUDE. [Pok. 4. mel- 720.] mel-5. Bad. Latin malus, bad, and male, ill (> malignus, harmful): MAL-, MALICE, MALIGN; DISMAL, MALADY, MALEDICT, MALEFACTOR, MALEVOLENT, MALVERSATION. [Pok. mélo- 724.] mel-€, Wool. Possibly suffixed zero-grade form *ml-no- in Greek mallos, wool. [Pok. 2. mel- 719.] mel-?. To miss, deceive. Germanic *mai- in Middle Dutch mal, foolish, silly: MALLEMUCK. [Pok. 2. mel- 719.] meldh-. To pray, speak words to a deity. Germanic *meld- in Old High German meldén, to proclaim, reveal: MELD}. [Pok. 1. meldh- 722.] mele-. Also mel-. To crush, grind; with derivatives referring to various ground or crumbling substances (such as flour) and to instruments for grinding or crush-
763:mops, fool, also pug dog (> German Mops, pug dog): ROLLMoPsS; d. Old French momer, to act (in dumb show): MuM2, 2, Germanic *mut- in Old Norse mudhla, akin to the source of Middle English muteren, muttren, to mut- ter: MUTTER. 3. Latin muttire, to mutter: MOT, MOTTO. 4. Lengthened-grade form *mi- in Latin miius, silent, dumb: MuTE. 5. Greek muein, to close the eyes (< “to close the lips”): MIOSIS, MYOPIA, MYSTERY!, (MYSTIC). [Pok. 1. mii- 751.] mu-2, Gnat, fly. Imitative root. 1. Germanic *mukjé- in Old English mycg, midge: MIDGE. 2. Suffixed form *mus-ka in Latin musca, a fly: Mosquito, Musca, MUSCARINE, MUSH?, MUSKET. 3. Suffixed form *mus-ya in Greek muia, mua, a fly: mytasis. [Pok. 2. mi- 752.] mik-. A heap. Germanic *miigén-, *mihon- in: a. Old English miga, miiha, miiwa, heap of grain: Mow}; b. Old Norse migi, heap, akin to the probable Scandinavian source of MOGUL}. [Pok. mitk- 752.] [mundus. Women’s cosmetics, also world (probably by a calque on Greek kosmos, order, feminine adornment, world-order, universe). Latin noun of unknown origin; possibly from Etruscan. MUNDANE; ULTRAMUNDANE.] miis-. A mouse; also a muscle (from the resemblance of a flexing muscle to the movements of a mouse). 1. Ger- manic *mis- (plural *misiz) in Old English mis (plural
1806:MALIGN gene-, mel-5 MALLEABLE mele- MALLEMUCK mel-7 MALLET melo- MALLEUS mele- MALLOW malakhé MALM mela-
1879:MITOCHONDRION ghrendh-, mei-4 MITOSIS mei-4 MITTEN medhyo- MITTIMUS (s)meit(a)- MIX meik- MIXTURE meik- MIZZEN medhyo- MIZZLE meigh- MNEMONIC men-! MNEMOSYNE men-1 MOAN mei-no- MOB meue- MOBILE meue- MODAL med- MODE med- MODEL med- MODERATE med- MODERN med- MODEST med- MODICUM med- MODIFY dhé-1, med- MODIOLUS med- MODULATE med- MODULE med- MODULUS med- MOGUL! miik- MOIETY medhyo- MOIL mel-1
=== AHD meug/muk root ===
760:merk-'. To decay. Latin marcére, to decay, wither: MARCESCENT. [Pok. 1. merk- 739.] [merk-2. Italic root, possibly from Etruscan, referring to aspects of commerce. 1. Latin merx (stem merc-), mer- chandise (> mercdri, to trade): MARKET, (MART), MER- CER, MERCHANT; COMMERCE. 2. Latin merces, pay, reward, price: MERCENARY, MERCY. 3. Probably Latin Mercurius, the god of (inter alia) commerce: MERCURY. [In Pok. merk- 739.]] [merph-. Form. Greek root of unknown origin. 1. Suf- fixed o-grade form *morph-G- in Greek morphé, form, beauty, outward appearance: -MORPH, MORPHEME, MOR- PHO-, MORPHOSIS. 2. Possibly borrowed from Greek morphé, via Etruscan, is Latin forma, form, shape, contour, appearance, beauty: FORM, FORMAL, FORMULA; CONFORM, CORACIIFORM, DEFORM. [In Pok. 2. mer- 733.]] mers-. To trouble. Suffixed o-grade form mors-eyo- in Germanic *marzjan in Old English merran, mierran, to impede: MAR. [Pok. 6. mer- 737.] meu-. Damp; with derivatives referring to swampy ground and vegetation and to figurative qualities of wetness. 1. Extended form *meus- in Germanic *meus-, *mus- in: a. Old English mos, bog: Moss; b. Old Norse mosi, bog, moss, akin to the Scandinavian source of LITMUS. 2. Germanic suffixed form *meuz-i- in Old Norse myrr, bog: MIRE; (QUAGMIRE). 3. Suffixed zero-grade form *mus-to- in Latin mustus, new, newborn (< “wet”): MUST’, MUSTARD. 4. Possibly suffixed extended zero-grade form *mii-ro- in Greek murios, countless (< “flowing, endless”): MYRIAD. 5. Possibly suffixed ex- tended zero-grade form *mud-so- in Greek musos, un- cleanness: MYSOPHILIA, MYSOPHOBIA. [Pok. 1. meu- 741.] meue-. To push away. Latin movére, to move (> mobilis, neuter mobile, fickle, changeable): MOB, MOBILE, MO- MENT, (MOMENTOUS), MOMENTUM, MOSSO, (MOTIF), MO- TION, MOTIVE, MOTOR, MOVE, MOVEMENT; COMMOTION, EMOTION, PROMOTE, (REMOTE), (REMOVE). [Pok. 2. meu- 743.) meug-'. To act surreptitiously. Germanic *muk- or Celtic *mug- in Old French muchier, to skulk: MOOCH. [Pok. 1. meug- 743.] meug-2. Slimy, slippery; with derivatives referring to various wet or slimy substances and conditions. Enlarged form of meu-. 1. Nasalized form *mu-n-g- in Latin mungere, to blow the nose: EMUNCTORY. 2. Possibly Germanic *(s)mug-, referring to wetness and also to figurative slipperiness: a. Old English smoc, shirt: smock; b. Middle High German smuck, “clothing,” adornment, jewel: scHmMuCK; c. Old Norse mugga, driz- zle, akin to the source of Middle English muggen, to drizzle: MuGGY; d. Low German smukkelen, smuggeln, to smuggle (< “to slip contraband through”): SMUGGLE; e. Middle Low German smucken, to adorn (< “to make sleek”): SMUG; f. Old Norse mygla, mold, mildew, akin to the source of Middle English molde, mold: MOLD®. 3. Ger- manic *meuk- in Old Norse mjikr, soft: MEEK. 4. Variant form *meuk- in Latin miicus, mucus: MOIST, MUCILAGE, MUCO-, MUCUS, (MUSTY). 5. Zero-grade variant form *muk- in: a. Greek mukés, fungus, mushroom: -MYCETE, MYCO-; STREPTOMYCES, (STREPTOMYCIN); b. suffixed form *muk-so- in Greek muxa, mucus, lamp wick (< “nozzle of a lamp” < “nostril”): MATCH2, Myxo-. [Pok. 2. meug- 744.] mezg-'. To dip, plunge. 1. Latin mergere, to dip, dive: MERGE; EMERGE, IMMERSE, SUBMERGE. 2. Latin mergus, diver (water bird): MERGANSER. [Pok. 1. mezg- 745.] mezg-*. To knit. Germanic “mésk- in Middle Dutch a maesche, knitted fabric: MESH. [Pok. 2. mezg- 746. [mimos. A mime. Greek noun of unknown origin. MIME, MIMESIS, MIMIC.] [miser. Wretched, unfortunate. Latin adjective of un- known origin. MISER, MISERABLE, MISERY; COMMISER- ATE.]
963:smeug-. To smoke; smoke. Germanic *smuk- in Old English smoca, smoke: SMOKE. [Pok. (s)meukh-, (s)meug-, (s)meugh- 971.]
1454:ELUANT leu(@)- ELUCIDATE leuk- ELUDE leid- ELUTE leu(a)- ELUVIUM leu(a)- ELYTRON wel-3 EMACIATE mak- EMANATE ma-3 EMANCIPATE man-2 EMASCULATE mas EMBASSAGE ag- EMBASSY ag- EMBELLISH deu-2 EMBER eUS- EMBER DAY ambhi, rei-3 EMBLEM gWele-1 EMBLEMENTS bhel-3 EMBOUCHURE beu-! EMBRACE mregh-u- EMBROCATE mergh- EMEND mend- EMERGE mezg-! EMERITUS (s)mer-2 EMESIS weme- EMETIC weme- EMIGRATE mei-! EMINENT men-2 EMIT (s)meit(9)- EMMET mai-1 EMOLLIENT mel-1 EMOTION meue- EMPEROR pere-! EMPHASIS bha-' EMPHYSEMA pu-! EMPIRIC per-4 EMPLOY plek- EMPORIUM per-2 EMPRISE ghend- EMPTY med- EMPYEMA pu-2 EMPYREAL pil- EMULSION melg- EMUNCTORY meug-2 EN-! en
1829:MATCH2 meug-2 MATE! mad- MATELOTE neud- MATER miater- MATERIAL miater- MATERNAL miater- MATERNITY méater- MATHEMATICAL mendh-1 MATHEMATICS mendh-! MATINEE méa-1 MATINS ma-1 MATRICLINOUS  klel- MATRICULATE miter- MATRIMONY miater- MATRIX miater- MATRON miater- MATTER méater- MATTOCK mat- MATURE ma-1 MATUTINAL ma-1 MAUL mele- MAULSTICK mel-2 MAUVE malakhé MAW mak-2
1842:MEEK meug-2 MEERSCHAUM mori-, (s)keu- MEET! mdéd-
1880:MOIST meug-2 MOLAR? mela- MOLASSES melit- MOLD! med- MOLD2 meug-2 MOLD? mela- MOLDER mele-, mai-2 MOLE! mai-2 MOLE? mo-
1882:MOLTO mel-4 MOLY md6(u)lo- MOLYBDENUM plumbum MOMENT meue- MOMENTOUS meue- MOMENTUM meue- MONAD men-4 MONANTHOUS = andh- MONASTERY men-4 MONAXON aks- MonpDay mé-2 MONEY men-! MONGER meng- MONGREL mag- MONILIFORM mon- MONISH men-1 MONITION men-1 MONITOR men-1 MONK men-4 MONO- men-4 MONOCLE oOkw- MONOCLINIC klei- MONOCLINOUS klei- MONOCOQUE kokkos MONODY wed-2 MONOECIOUS weik-! MONOMER (s)mer-2 MOoNOPHYSITE bheue- MONOPODIUM ped-1 MONOPOLY pel-5 MONOTREME tere-1 MONS men-2 MONSTER men-1 MONTAGNARD men-2 MONTANE men-2 MONTE men-2 MONTH mé-2 MONTICULE men-2 MONUMENT men-! MOOCH meug-! MOOD! mé-1 MOOD? med- MOON mé-2
1895:MOTE? med- MOTH math- MOTHER! miter- MOTIF meue- MOTION meue- MOTIVE meue- MOTOR meue- MOTTO mul- MOUILLE mel-1 MOULAGE med- MOULIN mele- MOUNT! men-2 MOUNT? men-2 MOUNTAIN men-2 MOURN (s)mer-1 MOUSE mius- MOUTH men-2 MOVE meue- MOVEMENT meue- mow! mik- Mow? mé-4 MUCH meg- MUCILAGE meug-2 MUCO- meug-2 MUCUS meug-2 MUGGY meug-2 MULBERRY moro- MULCH mel-1 MULE? mel-2 MULEY mai-1 MULL? mele- MULLET mel-2 MULLION medhyo- MULTI- mel-4 MULTIFARIOUS dhé-1 MULTIPLE pel-3 MULTIPLEX plek- MULTITUDE mel-4 MUM! mul- MUM2 mul- MUMPS mul- MUNDANE mundus
1898:MUSTARD meu- MUSTELINE mis- MUSTER men-! MUSTY meug-2 MUTATE mei-1 MUTCHKIN med- MUTE mul- MUTILATE mut- MUTTER mul- MUTTON mel-1 MUTUAL mei-1 MUZHIK man-1 MUZZLE musum MY me-1 MYCELIUM walso- -MYCETE meug-2 MYCO- meug-2 MYCORRHIZA wrad- MYELO- mis- MYIASIS § mu-2 MYLONITE mele- MYNA mad- MYNHEER me-1 MYO- mis- MYOCARDIUM kerd-1 MYOPIA mut-, okw- MYOSOTIS miis-, ous- MYRIAD meu- MYRMECO- morwi- MYROBALAN gWel@-2 MYSELF me-! MYSOPHILIA meu- MYSOPHOBIA meu- MYSTAGOGUE ag- MYSTERY! mut- MYSTERY? mei-2 MYSTIC mul- MYSTICETE miis- MYTHOPOEIC kWeij-2 MYXO- meug-2
2225:SCHISM skei- SCHIST skei- SCHIZO-  skei- SCHIZONT es- SCHLEP |leij- SCHLIEREN sleu- SCHLOCK | slak- SCHMALTZ mel-1 SCHMEER (s)mer-3 SCHMUCK meug-2 SCHNAUZER snu- SCHNITZEL sneit- SCHNORRER sner- SCHNOZZLE snu- SCHOLAR segh- SCHOLASTIC segh- SCHOLIUM segh- SCHOOL! segh- SCHOOL? §skel-1 SCHUss skeud- SCIENCE skei- SCILICET skei- SCINTILLA skeei- SCINTILLATE skeei- SCIOLISM skei- SCION géi-1 SCIRE FACIAS dhé-1, skei- SCISSION  skei- SCISSORS kae-id- SCLERA skele- SCLERO- skele- SCLEROMA §skela- SCLEROSIS skela- SCLEROTIC skelo- SCLEROTIUM skela- SCLEROTIZATION skela- SCLEROUS skelo- SCOFF skeubh- SCOLD sekw-3 SCOLEX skel-3 SCOLIOSIS skel-3 SCONCE? dhé-1 SCONE keu-! SCOOP skep- Scop skeubh- -SCOPE spek- -SCOPY spek- SCORCH skerbh- SCORE sker-1 SCORIA_ sker-4 scoT skeud- SCOT AND LOT skeud- SCOTOMA  skot- SCOUR! cira SCOUR2 kéwero- SCOURGE reig-1 SCOUT! ous- scouT? skeud- SCRABBLE  sker-! SCRAG gWere-4 SCRAP!  sker-1 SCRAPE sker-1 SCRATCH grat- SCREAK ker-2 SCREAM ker-2 SCREECH ker-2 SCREED skreu- SCREEN sker-1 SCREW sker-! SCRIBBLE skribh- SCRIBE skribh- SCRIMP_ skerbh- SCRIPT skribh- SCRIPTORIUM skribh- ScRIPTURE  skribh- SCROBICULATE sker-1 SCROD skreu- SCROFULA  sker-1 SCROLL skreu- SCROTUM skreu- SCRUB!  sker-1 SCRUTINY skreu- SCUDO skei- SCUFF skeubh- SCUFFLE! skeubh- SCUFFLE? skeubh- SCULPTURE skel-1 SCUM (s)keu- SCUTCH kwét- SCUTTLE! skeud- SCUTUM  skei- SCYPHISTOMA skep-, ste-men- SCYPHOZOAN skep- SCYTHE sek- SEAL! sekw-1 SEAL? selk- SEAM syi- SEANCE sed-! SEAR! saus-
2271:SLOE slii- SLOGAN gar-, sloug- SLOOP sleubh- SLOP! sleubh- sLop2  sleubh- SLUG? sleu- SLUGGARD §sleu- SLUMBER sleu- SLUMGULLION leb-1 SLUMP leb-1 SLURP srebh- SLUSH sleu- SLY slak- SMACK! smeg- SMACK? smeg- SMALL mélo- SMALT mel-1 SMART smerd- SMEAR (s)mer-3 SMEARCASE (s)mer-3 SMELT! mel-1 SMELT2 mel-1 SMILE smei- SMIRK smei- SMITE smé- SMITH smi- SMITHY smi- SMOCK meug-2 SMOKE smeug- SMORGASBORD _ bherdh- SMUG meug-2 SMUGGLE meug-2 SNAIL sneg- SNAKE sneg- SNAP snu- SNARE! (s)ner- SNARE? (s)ner- SNARL!  sner- SNATCH snu- SNEER sner- SNEEZE pneu-
2319:STOVE! staup- sTow sta- STRABISMUS streb(h)- STRABOTOMY streb(h)- STRAIN! | streig- STRAIN?  ster-2 STRAIT  streig- STRANGE eghs STRANGLE strenk- STRANGLEs  strenk- STRANGULATE _ strenk- STRANGURY strenk- STRATAGEM ag-, ster-2 STRATH ster-2 STRATOCRACY  ster-2 STRATUS  ster-2 STRAW ster-2 STREAK streig- STREAM sreu- STREET  ster-2 STRENGTH  strenk- STREPTO-  streb(h)- STREPTOMYCES meug-2 STREPTOMYCIN meug-2 STREPTOTHRICIN  thrix STREUSEL ster-2 STREW ster-2
```


## [2026-09-07T17:36:47.991Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK page 752 area: find mūk ===\"\ngrep -n \"mūk-\\|meuk-\\|mū̆k-\" POK_full.txt | head -40",
 "description": "Grep Pokorny for muk"
}
```


### [2026-09-07T17:36:48.043Z] TOOL RESULT

```
=== POK page 752 area: find mūk ===
60355:Root / lemma: meug-2, meuk- 
60548:2. meug-, meuk-^ slippery ' see below esp. headword.
```


## [2026-09-07T17:37:06.935Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Root / lemma: mū\" POK_full.txt | head -30\necho \"---- page 752 context ----\"\ngrep -n \"752\" POK_full.txt | grep -i \"page\\|mū\" | head -20",
 "description": "Find Pokorny mu roots"
}
```


### [2026-09-07T17:37:07.012Z] TOOL RESULT

```
---- page 752 context ----
61624:Page(s): 752 
61690:Page(s): 751-752 
61705:Page(s): 752 
61738:Page(s): 752-753
```


## [2026-09-07T17:37:08.365Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC leaf for p.814: leaf = 814/2+15 = 422 ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==422' IEC.txt | head -80",
 "description": "Print IEC leaf 422"
}
```


### [2026-09-07T17:37:09.676Z] TOOL RESULT

```
=== IEC leaf for p.814: leaf = 814/2+15 = 422 ===
tc. mist, m. ‘dung’, be- side OS mehs, n., OE meox, mex, mix, n. id.; Du. mest, m. id.; Li. cf. méslas, -ai, m. id.; Latv. mesls, mesli, m. id.
meK-? Cf. māk- (3) and maK-, maĝ-, me?- Only thus in Hitt. mekkis ‘big, great. Note -kk-, but cf. mag-, etc. W maith, adj. ample, long’ and Lat. mactus ‘extolled’ are ambig. A formula of type *meKhis (máKh-) is no more than an attempt to reconcile the Hittite form mekkis, cpds: mak- “big, great" with Gk. mégas, Pamphylian méas, obl. meiálo-, from an al- leged mheial- according to A. Heubeck, with the forms represented by Skt. máhih, Av. maz-, Tokh. mak-, Phryg. maz-, Alb. i madh, and Lat. magis, maior, cf. *ekho (aKh-), *Khe- nus, *dhukhtër, etc.)
(mel- (1) & (2). See Supt: M)
mél- (1) ‘stain, mark, esp. blue stain, blue; dark, stained, blue’. WP I, 293 MIr. miol, adj. (yellow (?!) but cf. Ir. míol- chú 'greyhound")); W mill, pl. (^violets', but cf. OBr. mell-hionou, id.); Go. mel, n. (2) “mark, sign’: MHG mal, OE mæl, n. id. beside OE ml, e adj. “marked, stained, dyed'; ON mál, n. (3) *inlay'; Li. melis, gs -io, m. “blue- colour; mélüs, adj. ‘blue’; Latv. mēļš, adj. ‘violet’; mēles, pl. ‘woad’
mel- (2) ‘time, period, measure’. Germanic only in this sense Go. mel, n. (1) ‘time, hour’; mela, m. ‘bushel; MHG mal n. (time, point, meal’. Cf. G Mal, Mahl-zeit, Merk-mal); OE měl ‘time; mea- sure, meal; Du. maal, Fris. miel, n. ‘time; meal’; ON mál, n. (2) ‘measure, time, meal máli, m. “contract; pay’; mælir, m. ‘measure’; Sw. mål, n. as ON. (Isophones: Latv. mele ‘tongue’; cf. ON mál, n. ‘speech, tale’; Sw. mål, id. and ‘voice’)
mel- (?) (3) Skt. mālā, f. *wreath'; malih, f. ‘creeper’; Hitt. cf. màhlas “vine?
mel- (4) “creature, animal". WP II, 296 Arm. cf. mluk (bug, fr. *meluk-, but ambig.); Gk. mélon, Dor. id. ‘creature, small animal; Mir mil, Ir. miol, pl. -ta, m. id.; W mil, pl. -0d, m. id. Br. mil, pl. -ed, m. f. id.; Cor. myi, pl. ag, m. ‘wild animal'. (An alleged Du. maal,
749
f. ‘heifer’ is untraceable)
meldo, io (1) ‘crush, destroy. Cf. WP II, 284 Skt. (ambig.) márdàmi (“crush?, but cf. merd-); MIr. millim, Ir. millim, v. ‘destroy, ruin”
meldo, ið (2) ‘soften’. Cf.. meldh- (2) Tokh. B melt- ‘dung’; Gk. méldo, méldomai *melt, soften, liquefy'; Lat. cf. melligo *mil- dew’; MIr. meall, adj. ‘sweet, pleasant; OE. meltan, sv. 3 "melt beside mieltan, wv (tr: ‘melt, dissolve, digest, refine’, fr. *moldeio, o-gde as in MHG malz, adj. ‘feeble, ailing’); Sw. mjält, adj. ‘gay, motley’. (Uncertainly Lat. oblique: melli-, see melit. Isophonic: MHG milz, Du. milt, OE milte, ON milti, Sw. mjälte ‘milt’)
meldh- (meldho, io) ‘address, pronounce, declare, accost, beseech’. WP II, 289. Cpd. in Lat. pro-mello: MHG ver-melden & Li. pra-meldZiü. See pro-? Hitt. malta(hi), maldiya(mi) “pray, recite’; Ir. millim ‘bewitch’; MHG mélden, wv. 'de- nounce'; G ‘announce’; cf. MHG máélde, f. ‘denunciation’; OE meldian, wv ‘report’; meld, f. id.; Du. melden, v. id.; Li. meldZiü, melsti “beg, pray’; (o-gde in) pa-malda “prayer”. Variants in Arm. maytem ('pray, beg; wish, long’, fr. (7) meldhsKo); cf. Hitt. malcki(mi) ‘pray’ and Li. melstinas, adj. ‘prayerful, ear- nest
meldhos (1) “soft, tender’. WP II, 275, 288 Lat. (?) melli- (oblique form of mel *honey); Olr. mell “pleasant; Go. -mildeis, cpds. *gentle, mild'; MHG milte, OE milde, id.; Icel. cf. mjóll, cpds. mjall- “loose snow'; (ambig.) Slovene mleden ‘weak’
meldhos (2) ‘ball, boss, hump, dome’. Cf. WP II, 291 Mir. mell, Ir. meall, m. id.; meille, f. ‘orach’; Gaul. mello- (in name); Br. mell, pl. -u, m. “ball, joint" beside mellez, f. ‘crown of head’; OHG melda, MHG mélde, Du. melde, f.; OE tun-m
```


## [2026-09-07T17:37:17.298Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^814$\\|^813$\\|^815$\" IEC.txt | head\necho \"--- leaf numbers ---\"\nawk 'BEGIN{RS=\"\\f\"} /^814$|\\n814\\n/{print NR\": leaf\"}' IEC.txt | head",
 "description": "Locate IEC page 814"
}
```


## [2026-09-07T17:37:17.698Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '61600,61760p' POK_full.txt",
 "description": "Read Pokorny page 752 region"
}
```


### [2026-09-07T17:37:18.596Z] TOOL RESULT

```
11349:813
11362:814
11371:815
--- leaf numbers ---
457: leaf
```


### [2026-09-07T17:37:18.641Z] TOOL RESULT

```
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
mocke^ Zuchtsau '); Old Icelandic /770s//' 'big, giant bulk, mass' {*muh-stra-)\ unique 
lengthened grade form in Old English meagor {*\\}'(r\py , massive ' =) 'tight, firm, strong'. 
References: WP. 11311; after Hubschmid ZnPh. 66, 33 f. not Indo Germanic 
Page(s): 752 

Root / lemma: mu-1 

Meaning: to murmur, moo (expr.) 

Material: 1 . Gr. |ju, pu ' cry of pain ', Latin mu facere, mutmut facere 'stir, move, budge '. 

2. Old Indie muka-^ dumb ', Armenian munj^ dumb ', gr. jjOko^, jjutk;, [jutt6(;, puSoq, 
|juvap6(;, Hes. fjuv56(; ' dumb ', Latin mutus^ dumb '; compare also Old Danish mue, 
Norwegian mua^ keep mum, keep quiet, remain silent, do not mutter, mumble '; Old High 
German mawen^cry', Latvian maunu, mawu, maut'roar, bellow', Czech myjat/" moo'; here 
also Modern High German Mowe, Old English m^w, mew, Old Icelandic mar{P\. mavai). 
Old Saxon meu6s. 

3. [Old Indie mukha-n. 'mouth' derives from Dravidian]; gr. puAAov 'lip'; puAAaivu) 
'verzieheden mouth, cut, bite Gesichter' (fjuara^ ' upper lip, whisker, moustache', s. 
Boisacq m. Lithuanian), Old High German mu/at, Middle High German mu/n. 'muzzle'. 
Middle Low German /t?^/©' muzzle, snout'. Old Icelandic /77J// "muzzle, esp. upper lip of an 
animal, bulging crag ', Gothic faurmuljan ' das Maul zubinden ' (whether with ani. s- in 
addition Norwegian smaul, Latvian s/77a^/e 'muzzle'??); s. also under mou-lo-S. 750. 

4. With dental formant: 



Latin muttio, -ire^ mutter, mumble ', muttum nullum^ keinen Muckser' (compare above 
mutmut); Old High German /77i////d/7 'mumble, murmur, trickle ', musse^ spring ', Old 



Icelandic mud/a 'mumb\e, murmur', besides with Germanic t. Norwegian dial, mutra, 
Middle English muteren, engl. mutterds.; Lithuanian /77i//e "muzzle'. 

5. guttural extensions (compare above 2.): 

With A:;gr. pOKaopai " bellow', puxOi^w "snort, spotte'. Middle High German muhen, 
mugen, muwen'roar, bellow'. Old Bulgarian mykh' bellowing, braying, roar', russ. mycatb 
"roar, bellow', Serbo-Croatian slov. Czech mukat/^roar, bellow'. 

With g:0\6 Indie munjati, moJat/^gWes einen Ton from sich' (Dhatup.); mucchana' 
growing sound, tone'; gr. |ju^u) "bringe with closed Lippen einen sound hervor, stohne' (out 
of it Latin mussare^ mutter/whisper (discontently); hum (bee); keep quiet (about); 
hem/haw; hesitate '), |Juymo<; "sigh'; 

Latin mugio, -Ire 'roar, bellow', conmugento' convocanto ', mugmor' loiter] dally ' (also " 
nugarlet quasi tarde conari '), Umbrian /77^/e/o"muttTtum ', mugatu' muttlto ', Latin 
mugilareoi Naturlaut of Esels; Old High German muckazzen' talk quietly, mutter, mumble 
', Modern High German Middle Low German mucken' talk with half-open mouth ' {kk\s 
expressive). East Frisian muk'V\ss\ 

6. s-extension: gr. pOu) "sich shut, from den Lippen and den Augen' (hence ^juojijj "die 
Augen zusammenkneifend, shortsighted '; puaco "bite die Lippen together'; from *jjuaT6$ 

verschwiegen': puaTr|<; "in die Mysterien Eingeweihter', puaTiK6(; "die Mysterien 
betreffend', puarripiov " mystery, secret Zeremonie', compare also pusTv "in die Mysterien 
einweihen'; Norwegian mysa'to screw up one's eyes'; from Germanic here also Middle 
Low German mummelen, engl. /77^/77i6'/e "mumble, murmur', mump, Norwegian mumpaAs.; 
Middle High German mupf, muff' Verziehung des Mundes ', mupfen, muffen. Middle Low 
German mopen, engl. mope'ga\Nk', engl. /770/? "grimace'; perhaps Modern High German 
Bavarian /t?^^©/? "ruminate' ; 

Latvian mus/nat'\Nh\sper, mumble, murmur'; Hittite mu-u-ga-a-mi {mugami) " spreche 
Klagegebete '. 

References: WP. Il309ff., WH. II 117, 119 f., 135, 139 f., Trautmann 188. 
Page(s): 751-752 

Root / lemma: mu-2, mus- 
Meaning: fly n. 



Material: Armenian mun, Gen. mnoy^a mosquito, gnat ' {*mus- or *mu-no-); alb. mu-ze, 
/77/-ze(ze diminutive suffix) ' mosquito '; gr. puTa (*[juaja) "fly'; Latin musca; Old Icelandic 
/77j/n. ( *muja-) " mosquito '; Swedish mygg, mygga. Old English mycg. Old Saxon muggia. 
Old High German mucka " mosquito ' ( *mukja)\ 

with -5-gotland. mausa{*musa), Flemish meuzie{*musT}\ Lithuanian muse. Old Prussian 
muso, Latvian musa, musal\Y'; Old Bulgarian muchal\y' {*mousa), m-bsica^ mosquito '. 
References: WP. II 311, WH. II 133, Trautmann 191, Specht Indo Germanic Dekl. 43. 
Page(s): 752 

Root / lemma: mus 

Meaning: mouse 

Note: (older *mus, musosirovn *meus, musos) 

Material: Old Indie mus-m. ' mouse, rat', np. mus^ mouse '; 

Armenian mu-kn^ mouse, muscle '; gr. \x\ic, {\x\ibc,, puv after ho,, Clxioc,, uv) " mouse ', 
also " muscle '; alb. ml miu' mouse ' {*miusTn) 

Alb. Geg mini, min/{P\) " the mouse ' 

Latin mOsm. " mouse ' {munnus: Middle High German miusTn'ofthe mouse'); Old High 
German Middle High German Old Saxon Middle Low German Old Icelandic Old English 
mOs' mouse, muscle ' (consonant-stem); Old Bulgarian mysbt ' mouse '. 

Often applied on body parts: Armenian mukn' muscle ', gr. \^0q " muscle ', jjucbv 
'muskelreiche region of Leibes' (from which also " voluptuous woman' in gr. (juojvia), pua^, 
-aKO(; m. " mussel, spoon': Latin mOrex' Mediterranean sea snail, snail emitting purple dye 
'; Latin muscuius6s., " muscle ', Old High German etc. mOs^ muscle, esp. of the upper 
arm'. Middle Low German mOs esp. 'the spherical flesh of thumbs'. Modern High German 
Maus, i\/1ausciien. Old Bulgarian mystca ' (3paxiwv '; on the other hand Old Indie muska- 
m. 'testicle, vulva', npers. musk^ castor, beaver' (from Pers. derives gr. [joaxoc;. Modern 
High German A^c»sc/7^s 'musk'); gr. [juaxov ' genitals '; 

Maybe alb. Geg /77i/s/ri//'muscle', /77i/5M 'shoulder', musi7keni'\ungs'. 

probably to Old Indie musnati' steals, robs ' etc., see below meu-2'push away '. 

References: WP. II 312 f., WH. II 132 f., Trautmann 191, Specht Indo Germanic Dekl. 40 f. 
Page(s): 752-753 



Root / lemma: meni- 

Meaning: a kind offish 

Material: Gr. paivn (out of it Latin maena), \ia\v'\Q, "a small sea fish', Slavic *m-bnb, russ. 

menb etc. 'toad '; but Old Indie mma- m. "fish' (whereof mainika-, mainala- " fisherman ') is 

of dravid. origin; perhaps here Old High German muniwa. Old English myne, engl. minnow 

'minnow, small freshwater fish, a fish', (under the influence of common Celtic -ns-, -nt- > - 

nn-). 

References: WP. II 267 f.; 

See also: belongs probably to men-4. 

Page(s): 731
```


## [2026-09-07T17:37:27.478Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11330,11375p' IEC.txt",
 "description": "Read IEC page 814"
}
```


### [2026-09-07T17:37:27.522Z] TOOL RESULT

```
mugulos, à (mugol-) ‘excrescence’. (Variant: mukul-) Skt. cf. (variant) mukulah, am. m. n. ‘bud’; Alb. muügull, m. ‘shoot, bud'; Rum. substrate múgur, m. id.; Ir. mógali, m. ‘globe, apple of eye, bunch’; W ml, pl. od m. “lump”; Du. mokkel, m. f. ‘plump person’; Li. mugulis, m. 'fumbler, plodder'; (Finn. LW mukula, mu- kura “lump, gnur?; Estonian LW mugulas, id.; Marian (Cheremiss) mügylis, mükle, as Finn.; mügyr ‘hump’. LWs); Latv. cf. mugura, f. (back, whence Marian mügyr. Toivonen non- committal)
mügh- (1) ‘press, squeeze, pound’ Gk. cf. a-mukhé ‘laceration’; a-múttō, v. Cla, cerate’, fr. *sm-mughio); Myc. cf. (queried) mutewe(s) (“manglers? or ‘beaters’ of skins); cf. also Gk. pro-mütto ‘squeeze’; epi-mútto ‘mangle’; muttoteúð ‘hack; ON múgr, m. ‘crowd, mob’; múgi, m. ‘swath, crowd’; Norw. muge ‘crowd’; cf. ON mýgja, v. w. dat. "op: press’; Blg. cf. mágan, m. ‘hemp-beater — tooľ; Li. cf. muginti, inf. ‘drive, urge’
mugh- (2) ‘destroy; fail, fall Skt. mühyami “err, stray, collapse’; Ir. mu- ghaim, v. “destroy”; OE cf. for-mogod, pp. "de
mug- — muk- (mük-, munk-)
10
20
25
30
35
40
45
 
812
cayed'
mügh- (3) “dark; darkness. (Arm. & Gk. ambig. Cf. smugh-) Arm. (ambig. mujg "dark brown’; Gk. (ambig.) mukhós, pl. a m. “darkness; dark corner’; mükhios, adj. ‘inmost’; ON cf. mug- gu-veór (‘muggy weather. E muggy fr. ON); Norw. mugge, v. (fret, grumble’; mugne, v. “get musty’; muggen, adj. ‘musty’. Cf. mughlio
mughis, io “fly, insect Kurd. moz fhorsefly' (*$h?); Alb. mizë, f. “fly; insect'; Lat. cf. mülio gs -onis, m. (2) 'gnat, fr. *muhlio-); MHG mügge, mücke, wf. ('fly'. Mod. G Mücke fr. Upper Ger.); OS muggja, id.; OE mycg, m. ‘midge’; Sw. mygg, n. & mygga, f. ‘fly’; Latv. müdzis (fly; pl. "ver, min")
mughlio ‘grow mouldy’. Cf. mug- (1) and mugh- (2) and (3) Skt. (ambig.) muhirah ‘fool; mühyami, v. (be confused'. Prob. fr. *mudhlos q.v); Arm. mglim, v. ‘grow mouldy’; Ir. (ambig.) mogall, m. murk’. Cf. mug- (1); W mwll, f: moll, adj. 'sultry; LG mogeln, be-mogeln, v. Ccheat Cf. sense of E obfuscate); LG cf. also muggelich (‘dainty, cosy’. Semantics ob- scure); Upper G sich an-mugeln ‘snuggle up to; ON mygla ‘grow mouldy’; mygla, f. ‘mould, mustiness'; Sw. mögel, n. id.
mio, ið ‘howl, roar, bellow, murmur, mut- ter, grumble’. WP II, 310. Variant: müg- Skt. múj- radical form of müfijami, mójami, v. ‘din, resound’; Arm. cf. (variant) mgt'am, v. (fume, rage’, fr. *mugsthaio); Hitt. mugahi ‘lament’; Gk. müzo, v. ‘murmur’; vbi. n. mug- mós, m. id.; Lat. mügio, īre ‘roar’; Umb. cf. mugatu (“let him murmur or sim.); OHG cf. ir-muccazen, v. id.; G mucken *mutter, mur- mur; Du. mokken, id.; Norw. mukke, Sw. mucka as G. (For Fr. se moquer de; OFr. moquier ‘to mock’, OFr. also ‘to pull faces’, cf. LG mucken, v. (2) ‘sulk, pout’: Du. mok- ken, v. id. as a LW)
muk- (mük-, munk-) ‘leave’. WP II, 254 Skt. mucámi, muficámi, pp: muktáh “leave, re- lease; Romani mukav, pp: muklo ‘leave, let, allow’; Av. muč- ‘let, release; Tokh. A muk-, mok-, B mauk., v. leave; OCS müécg, ati
813
‘release, let fly’; mükno, -noti, v. tr. ‘remove’; intr. ‘pass, move’; R mču, mčať “carry off, remove’; -sa ‘escape’; Pol. mknac sie ‘flee’; Cz. cf. s-mekat, -meknout ‘remove — the haft’; Li. munkù, mùkti ‘slip away, steal away”; Latv. müku, mukt, v. (1) ‘escape. (Isophone: Latv. mūku, mukt ‘get stuck, bogged down’ & cf. Blg. mákna “drag'). See next
mūk- (1) “grow dark, get filthy, become foul; foul, murky; foulness, murk?. (Variant: muk-. Gk. W forms ambig., cf. smug-) Skt. cf. mukah “smell of cowdung'; Gk. mükes, pl mükai, m. ‘fungus; Hes. míükos ‘foul’; Alb. myk, m. ‘mildew’; mykem "eet mil- dewed'; Lat. müceo, ere, v. ‘get mouldy’ be- side OLat. muccus ((snot, whence OFr. moche) beside Lat. mücus, m. id.; lr. müchaim, v. ‘stifle, obscure, extinguish’; múch, f. ‘smoke, gloom, grief; müchna, adj. “dark”; W (short vowel) mwg, m. ‘smoke’; mwci, m. (1) ‘fog’ beside (long vowel) migen, f. ‘bog; Br. mug, muk “purple dye-mollusc, murex’; Li. muküs ‘slimy, boggy’; Latv. cf. müku, mukt, v. ('squelch, get bogged down’, but cf. muk- above); cf. mukls, adj. ‘boggy and see muklos (2) WP II, 310 Gk. mükáomai, id.; Alb. cf. (short vowel) mukoj, id.; W mig, pl. ion, f. beside migiad, m. (“hoot; hooting’, fr. *müki-, *mükjot-); OHG mühen, v. ‘moo’; R myCàt, inf. id.; Li. mükiü, mükti & mükioju, -ioti, id.
mük- (3) (mükaio, eio) ‘clamp, shut fast, fasten, lock Skt. cf. mükah (*dumb', “lit. ‘tied, bound" — Mn-Wms.); Mir müchaim, v. (1) ‘squeeze, strangle’; Cz. za-mykat, inf. ‘lock; ode-mykat, inf. ‘unlock; OCS cf. (short vowel) po-mča, po-müca, f. ‘snare’; Latv. cf. mükét, v. open w. a skeleton key” (!)
muklos (mukulos?) (1) *stammering, jabber- ing; stammer, gibberish; gibberer Gk. müklos, m. (2) ‘jackass’; Li. muklus (2) ‘stammering’; OCS cf. (?) pomüklt, f. (que- ried: ‘restraint? or 'silence). (Skt. mukulah ‘with one eye closed" and mukurah ‘mirror appear to be mere isophones, cf. mük- (3))
mük- — muksó
15
20
29
30
39
40
45
814
muklos, us (2) ‘messy; mess, sludge, marsh, murk’. Cf. WP II, 253 Gk. müklos, m. (1) ‘smear; debauchee'; Li. mukluüs ‘miry, marshy, oozy’; Latv. mukls, id.
mükóo(n) (mükró-) “pike, spike, peak, pile’. WP II, 311 Per. mūk ‘sting’; Hes. mükon ‘pile’; Lat. cf. (variant) mücro, gs -onis, m. (“point of sword". Cf. (?) Hes. mókron 'sharp); OE müha, müga, wm “pile, rick’. (Not also R mys ‘headland’ if *-k- as in Per. mük)
muks- (1) ‘snout; pig; grunt, murmur’. Cf. WP II, 310 Skt. mükbam, n. ‘snout, mouth’; Gk. Hes. cf. mukós “silent, soundless'; Ir. muc, f. ‘sow’; W moch, m., Br. mōch, m. coll. ‘pigs’; (Celt. LW in G Mocke ‘breeding sow); G cf. muck- sen, v. ‘make a faint sound, squeak’
muks- (2) ‘worthless, rejected, ba? It. moscio ‘flabby’; Cor. mogh ‘fruitless’; OE cf. myscan, v. ‘injure, offend’; OCS cf. müselü "gotten gain’; Ukr. cf. (?) pry-mxy, pl. (^whims' but see next)
muksa, io ‘fly, midge’. Cf. muksitio, musio, muska Lat. musca, id.; G Mucks, m. ‘midge’; OE mysci, pl. ‘flies’; OCS cf. müsica f. dim. ‘gnat’; R cf. mó$ka, f. dim. id. Cf. (?) Ukr. pry-mxy, pl. “whims but see maks- (2). For Mod. Icel. my ‘gnats: Gk. mua ‘fiy’, see musio)
muksità, iə “small fly, midge, insect. Cf. muksà, etc. (Variant mukst-) OE mohpe, mopbe, f. ‘moth’; Late MHG motte, f.; Du. mot, f. id.; OCS música ‘gnat, midge’; It. moschetta, id. (beside moschetto: Sp. mosquito)
mukso, ið (1) ‘thrust, plunge, insert, force’. Li. ambig. Cf. müK-, muKtis Arm. mxem, v. tr. id.; mux ‘tempered’ beside mxun, id., cf. also mxlCem, v. (plunge, thrust’, fr. *mukslitio or sim.); Ir. cf. müchaim, v. ‘suppress, destroy’; Li. mùšiu, müsti, v. “beat, strike, shatter; mūšis, m. “battle, fight". Cf. mük- below, & cf. MHG müschen (jog; bat- ter”, fr. *muskio); OE myscan, v. "hurt
muksó (2) (?) Gk. cf. müxa 'snot; Lat. muccare, v. inf. ‘snort’; cf. also Gk. mukteér, s. ‘nostril’. (OCS
815
müselt or míseli, m. ‘substance’; Cz. o-mšelý 'tattered” suggest a prototype *miKs-l-, q. v.)
müksos 'smoke' Arm. mux, gs mxo, ost, id.; cf. mxam, v. ‘smoke’; Ir. múch, f. ‘smoke; gloom’; cf. mú- chaim, v. (1) ‘suffocate’
muktos ‘left, freed, abandoned, loose, dash- ing, rapid’. Cf. muk-. WP II, 254 Skt. muktáh, pp. ‘freed, loose’; Romani muklo ‘freed, allowed; It. cf. motta, f. ‘subsidence’ beside mucciare, v. ‘run away’ (background uncertain), W mwth, adj. ‘rapid’; cf. chwi- mwth, id. (fr. *su1-9; Li. müktas, pp. of mun- kü, mùkti ‘slip, fall, dash, run’; Latv. mukts, pp. of mukt, 1sg. pres. mūku (1) “be absolved, get free, escape’; Cz. cf. (obs.) mektati se ‘fluc- tuate'. (Isophonic: Arm. mtem ‘gather’, but phon. ambig.)
(müktos, see mūk- (1) & (3))
```


## [2026-09-07T17:37:40.008Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON grep موک ===\"\ngrep -n \"موک\" MON_part1.txt MON_part2.txt 2>/dev/null | head -20\necho \"=== BQT موک ===\"\ngrep -n \"موک\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head -20\necho \"=== ARY موک ===\"\ngrep -n \"موک\" incoming/ARY/ARY_pages.txt 2>/dev/null | head",
 "description": "Grep Persian sources for موک"
}
```


### [2026-09-07T17:37:40.111Z] TOOL RESULT

```
=== MON grep موک ===
MON_part1.txt:6916:تویل. تسلیم شدن. اتال به خدا: موکل 
MON_part1.txt:13130:اسموکینگ: 8و (.) نوعی جامه 
MON_part1.txt:17014:آویختن» معلق کردن. موکول کردن» منوط 
MON_part1.txt:18949:جنبش. (.) آواز و فریاد موکب. (مس.) 
MON_part1.txt:24723:اگر مقام مقتضی تأ کید است کلام موکد 
MON_part1.txt:25522:سردار قشون» سالار. گم رکجی. موکل اخذ 
MON_part1.txt:30785:علت حملة یکث نوع فارچ 0 موکورمیکوز 
MON_part1.txt:32393:گرداه فررموکث. 
MON_part1.txt:33764:فرموکث» گر دنای. 
MON_part1.txt:34400:( کد.) رضوان» فرشته موکل بر بهشت. پیر 
MON_part1.txt:43679:تموک: ۱۵۳16 )٩(‏ قسمی تیر که دارای 
MON_part1.txt:45485:تیر : ۱1 (.) (اخ.) فرشته‌ای که موکل است 
MON_part1.txt:57991:آفتاب. (.) فرشتة موکل بر خورشید. روز 
MON_part1.txt:63014:دموکراسی علاقمند به حکومت ملی. 
MON_part1.txt:63016:طرفدار به دموکرات وابستهبه حکومت ملی. 
MON_part1.txt:63017:دموکراسی: 0۵0027 (امر .) حکومتی 
MON_part1.txt:67222:مسمکلت: رژیم دموکراسی رژیم 
MON_part1.txt:68155:نگاهبان. پاسبان. موکل. رقیب دست چپ: 
MON_part1.txt:68156:فرشتةٌ موکل بر اعمال بد شخص. رقیب 
MON_part1.txt:68157:دست راست: فرشتهة موکل بر اعمال نبکك 
=== BQT موک ===
incoming/BQT/BQT_v5_pages.txt:329:برموکردن . درفارسی کلمات مختوم چه 3ج تیرتالوظ جح بد. آن و در
incoming/BQT/BQT_v5_pages.txt:6347:صید‌کنان موکب نوشیروان دور شد از کوکبهٌ خسروان
incoming/BQT/BQT_v4_pages.txt:616:نشتن ‎٩‏ - ول ملکی باشد (۱) که موکل‌است ماراقسان ۷ - باهمزءبروزن‌آتشدان,
incoming/BQT/BQT_v4_pages.txt:628:شمی - ونام فرشتةٌ موکل بر آب - و نام پدو ( اس - یکی دی
incoming/BQT/BQT_v4_pages.txt:1457:هاه - پروزن شاه ۰ بممتی‌بیر اسفرات | هم هت که موکل است برجرم قمر یمتی‌فرس
incoming/BQT/BQT_v4_pages.txt:2545:نام فرشته ایست موکل بر قصل زمستان و ندبیر بازی نرد که مغرء در آن خانه در ششدر باهقدر
incoming/BQT/BQT_v4_pages.txt:5119:تا موکل نشنود برها جهد خود سخن درگوشآن سلطان‌برد.
incoming/BQT/BQT_v4_pages.txt:5446:۴ - « موکه . بواو معروف » در برهان نیش عقرب و امتال آن لیکن در کتب معتبره
incoming/BQT/BQT_v4_pages.txt:5448:اللفات بنقل « فرهنگه نظام ج وس ما ». 3 موکه » میش بود .»۸« لغت قری‌س ۳۰۳ > وشاهدی
incoming/BQT/BQT_v4_pages.txt:5450:کروه سواره . رك : شرح قاموی . ۹ - جمع جوکبی » منسوب به « موکب » (هم.)
incoming/BQT/BQT_v4_pages.txt:5452:۷ - اشتینگای کوید : موکده مصحف‌کلمةٌ عربی « موکدهء > است .
incoming/BQT/BQT_v4_pages.txt:5668:او سیاه و دم او سفید باشد . قرشت » لام فرشته است موکل بمهر و محبت
incoming/BQT/BQT_v4_pages.txt:5793:پادشاهان هندوستان است وهندوان او را مغاراج | نام ملکی وفرخته‌است موکل برآب وتدبیرامور
incoming/BQT/BQT_v4_pages.txt:7588:نامه ه : ِ ۱ بالنده وه نموکننده باشد .۸
incoming/BQT/BQT_v4_pages.txt:17157:۹ - اسم مفعول از «هشتن» (۸م.) ۴ - رضوان,نام‌فوشتهٌ موکل‌بهشت. وبهشت.
incoming/BQT/BQT_v4_pages.txt:19672:زرنشت بمنوان فرشته‌ای معرفی "شده موکل برفديةٌ هوم (کیاه مزبور). دربندهای ‎۸٩‏ و۹۶ مهرد
incoming/BQT/BQT_v4_pages.txt:20417:() خم۳:۱وموکنان .
BQT_v1_pages.txt:5933:نیز هت که موکل ‏ ست . گویند : اکر درین
BQT_v1_pages.txt:7151:فرشته‌ییت موکل بر آتش و پیوسته در آتش
BQT_v1_pages.txt:12171:دانت - و نام فرشته است موکل بر ییشپا و
=== ARY موک ===
2790:آدارموک" هم ممکن است از همین ربشه باشد گواینکه امروزه معنی آن عوض شده است.
```


## [2026-09-07T17:37:42.522Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN mummy ===\"\ngrep -n -i \"mummy\\|mummery\\|mumia\\|mūmiyā\\|mumiya\" KLN_1966.txt | head -20\necho \"=== SKT mummy ===\"\ngrep -n -i \"mummy\\|mumia\" SKT.txt | head -10\necho \"=== LKT mumiya ===\"\ngrep -n -i \"mumia\\|mūmiyā\\|mumie\" LKT.txt | head -10",
 "description": "Grep Klein/Skeat/Lokotsch for mummy"
}
```


### [2026-09-07T17:37:42.603Z] TOOL RESULT

```
=== KLN mummy ===
24653:mum,  intr.  v.,  to  act  in  dumb  show.  —  ME. mommen,  fr.  OF.  momer,  mommer,  ‘to  mask oneself’  (whence  OF.  momon,  ‘mask’,  F.  mo- meric,  ‘mummery’),  which  prob.  derives  fr.  the child’s  word  momo,  expressing  astonishment. Cp.  G.  Mumme  ( now  obsol.),  ‘mask’  whence mummen  (now  einmummen,  vermummen),  ‘to muffle’.  Cp.  also  Sp.  and  Port,  momo,  ‘grimace’. Cp.  also  mummery.
24655:Mumbo  Jumbo,  1)  name  of  an  African  idol;  2) {not  cap.)  an  object  of  superstitious  fear.  — Corruption  of  Mama  Dyumbo,  from  Mandingo, a  West  African  Negro  dialect, mummer,  n.,  an  actor  in  a  dumb  show.  —  MF. momeur,  mommeur,  fr.  momer,  mommer,  ‘to mask  oneself’.  See  mum,  ‘to  act  in  dumb  show’, mummery,  n.,  a  dumb  show.  —  MF.  (=  F.) momerie,  fr.  OF.  momeur.  See  prec.  word  and  -y (representing  OF.  -ie).
24656:mummification,  n.  —  See  mummify  and  -ation. mummiform,  adj.,  shaped  like  a  mummy.  —  Com¬ pounded  of  mummy  and  -form, mummify,  tr.  v.,  to  make  into  a  mummy;  intr.  v., to  become  like  a  mummy,  to  dry  up,  shrivel.  — F.  momifier,  compounded  of  momie,  ‘mummy’, and  -fier,  ‘to  make  into’,  fr.  L.  -  fiedre,  fr. facere,  ‘to  make,  do’.  See  mummy  and  -fy. mummy,  n.,  an  embalmed  body.  —  ME.  mummie, fr.  OF.  (=  F.)  momie,  fr.  ML.  mumia,  fr.  Arab. mumiyah,  ‘mummy’,  fr.  Pers.  mum,  ‘wax’. Derivative:  mummy,  tr.  v..  to  mummify, mump,  intr.  v.,  to  mumble;  to  whine  like  a  beg¬ gar.  —  Obsol.  Du.  mompen,  ‘to  cheat,  deceive’, orig.  prob.  ‘to  mumble,  whine’  (cp.  Du.  mom¬ melen,  mompelen,  ‘to  mutter,  mumble’);  of  imi¬ tative  origin  Cp.  mumble, mump,  n.,  a  grimace  {obsol.)  —  Fr.  prec.  word, mump,  n.,  mumps.  —  See  mumps, mumper,  n.,  a  deceitful  beggar.  —  Formed  fr.
35411:skclctology,  n.,  the  study  of  the  skeleton.  —  Com¬ pounded  of  skeleto-  and  Gk.  -Xoyia,  fr.  -Xoyoq, ‘one  who  speaks  (in  a  certain  manner) ;  one  who deals  (with  a  certain  topic)’.  See  -logy, skeleton,  n.  —  ModL.,  fr.  Gk.  axeXeTov,  ‘mum¬ my,  skeleton’,  a  loan  word  fr.  Syr.  sheiadda, ‘skeleton’,  fr.  Akkad,  shalamdu,  shalamtu,  prop, meaning  ‘the  whole  (corpse)’,  fr.  shalamu,  ‘to  be complete’,  which  is  rel.  to  Heb.  shalam,  ‘was complete’;  see  shalom.  See  W.  Muss-Arnolt  in Transactions  of  the  American  Philological  As¬ sociation,  Vol.  XXIII,  p.  148.  The  explanation of  Gk.  axeXeTov,  ‘mummy,  skeleton’,  as  used elliptically  for  ctxeXctov  aojux,  supposed  to mean  ‘dried  up  body’  (as  if  axcXe tov,  were  the neut.  verbal  adj.  of  axeXXciv,  ‘to  dry  up’)  is  folk etymology.  Cp.  endoskeleton,  exoskeleton. Derivatives:  skeleton-ic,  adj.,  skeleton-ize,  tr.  v., skeleton-iz-ation,  n.,  skeleton-iz-er,  n.,  skeleton- y,  adj.
=== SKT mummy ===
12023:Mummy.  (F.  -  Ital.  -  Per».)  O.  F. mumit,  a  mummy.»Ita].  mummia.^Vcn, MtimJyiff*  A  mummy,  embalmed  body.«> Vcn,  m^rrf  wax,  much  used  in  embalming.
=== LKT mumiya ===
3473:'Wachs',  ebenso  tk.  niiim  'dass.,  Kerze', hieraus  serb.  nium  'Kerze',  [über  tk. tnumgi/]  rum.  mungiü,  munger  'Kerzen- fabrikaiit',  m!<H.9?/7f 'Keizenfabrik',  kat. sp.  nioniia  'Pech  und  Asphalt',  apg. muminha  'Mischung  vou  Pech  und Quecksilber',  bes.  die  harzige  Masse,  die aus  den  der  Sonne  ausgesetzten  Mumien floß  und  als  heilkräftig  galt.  —  Ar.
3474:mümija  'einbalsamierter  Leichnam'  ist in  dieser  Bedeutung  in  alle  europäischen Sprachen  übergegangen:  it.  mummia, fvz.  motnie,  mimiie,  sp.  momia,  pg.mumia, Adj.  sp.  momio  'abgemagert',  vam.mumie 'Mumie',  momie,  nioniue  'Vogelscheuche, Popanz';  engl,  tmunrny,  ndl.  mummie, dtsch.  Mumie;  russ.  murniju.  [Eguilaz 457.    ML  5743.    Kluge  317.
5851:Uli Moslem  1516  a Jtfoi^e  1520 Muezzin  1485 Mtf^i  1493 Jlf;(Ä-cr  1507 M««//  1381 Mumie  1510 Müsch  1515  a Muselmann  1516  a Muskat  1515  a Muskete  1520 Muslim  1516  a Musseline  1484 JfM<Äe  1520
6627:mumie  1-^10
```


## [2026-09-07T17:37:56.458Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT leaf 360 (p.340) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==360' SKT.txt | head -60",
 "description": "Skeat page 340"
}
```


## [2026-09-07T17:37:56.693Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3460,3480p' LKT.txt",
 "description": "Lokotsch mumiya entry"
}
```


### [2026-09-07T17:37:57.710Z] TOOL RESULT

```
=== SKT leaf 360 (p.340) ===
/vz/m/r,  a  patent  ;  so  called  because open  to  general  inspection.  —  O.Y,  pa/^nt (fern.  pcUenie),  patent,  wide  open.  —  L. pattnt-,  stem  of  pr.  pt.  of  patert,  to  lie open.  Cf.  Gk.  vtrafrv/u,  1  spread  out. (VPAT.)
compass.  (F.  *  L.)  F.  compos,  a  cir- cuit, cirde,  limit ;  also,  a  pair  of  com- pas»3.  — Low  L.campassus,  m  circuit.  — L. com-  {cum),  with ;  passta,  a  pace,  step, passage,  route ;  so  that  cempassus  —  m,  route that  joins  together,  circuit.  See  pace (below).  Der.  compass,  verb;  compasses, %.  pL,  an  instrument  for  drawing  circles.
•xpand.  (L.)  L.  cxfandcre  ^pp.  ex- f<uwu),  CO  spread  out.  -  L.  tx,  oat ;  panJ
PATERNAU
grtt  to  spread  out :  caosai  froi lie  open.     Uer.  txpaxjc.
pace,  a  step.  (F.— L.)    M. pas.  —  L.  possum,   ace.  of  past pace,  lit.  a  stretch,  distance  betwa feet  in  walking.  — L. /a»«/,  pp. to  stretch:  sec  above.
pail.  {F.  -  L.)    M.  E, pac/e,  a  kind   of  pin   (ijtt polclla^   a   small    pan,   dish   fo dimm.  oi  patera,  flat  disb.  san< to    Gk.    iraruKij,    a  .flat    dish; ( below V     p.  "But    now    IrtleH as  (E.).      From    A.   S.    pag formerly   misprinted    «cu^/. viii.  450.
paes,  to  move  onwanL  (P.. passen.  —  ¥.  passer.  —  Low  U^ paiS.  —  L,  pasruSt  a  step ;  see  paoe  \i p.  Dicz  takes  Low  L.  passart  to frequent,  form  oi  panJcre,  to  strel comes  to  much  the  same  thing.
passage.  (F.  -  L.)  F./fungt. h,  passa/icu/M,  a  right  of  passage^/ 'L.passare ;  see  above.
passport.    (F.  -  L.)     F. written  permission  to  pass  ifarc &c.  —  r. passer,  to  pass;  fvrUp^ L.  porta  ;  see  Port  (3).
paatlme.    (F.  ••  1. ;  m/td pass  and  time.
paten.  (F.  -  L.  -  Gk.) {Cot.). ^L. patina, p^itena,  a  flat  dish waray^,  a  flat  (open)  dish.     Sec  PW
surpass.   {¥.  —  L)     F, excel.— F.  jur  (L.  jai/rrl, to  pass  ;  sec  p»a«  (above).
trespass.  (F.  —  U)  F. exceed,  pass  beyond  i,henoe. —  F.  /rw-,  L.  //tiff/,  beyond; pa&s;  see  paai  (above). Paternal  (F.-L.)  F, L.  paiemaUs,  fatherly.  — fatherly.-  L/tf/#r,  father,  Ut. "  gttl formed  with  suffix  -fer  of  the  aKB VFA.  to  feed,  guar^.     See  Psttll
expatriate.  (L.)  From  p^  4 L.  cjcpafn'are,  tu  banish. *L  iT,<i patria,  imtive  country,  from  paiti-^ form  of /iz//r.  father.
parrioide.  (1)  themurdcjcrofs' (s>  murder  of  *  father.  i;F.  •(•i The  former  is  the  oHg.  tease,  w'  * to  F.  parricide,  I-  ptrriciM^  •  O' of  a  father.  — L.  parri ,  for  >•"*> form  of  pattr ;  mitrt^  to  uU  (1i 'CiJa,  a  slayerV     9.  The
PATH.
L.  fnirricidium,  the  morckr  of
the  same  sb.  aod  verb. vulvar  dialect  of  French.  <F. fatois,  country  talk ;  which older  form  patrois  (Diez, <ow  L.  fctritnns,  a  native; ijing  to  llie  natives.  *  L. t  counlry.  — L.  patriu  crude ;  a  father.
(F.-U-Gk.)  O.F.^rS'
9afn'a/rAa.  —  Gle,  rar/na^xiS
cc  or  tribe.  *Gk.  iror^u-d,  a
to  rule.     See  Aroh-  {prtjix\
.  a  Roman  ooblenian.     |,L.)
b  suffix  -aw,  from  L-  patncius,
Moeodant   of  the  /iairtt,  i.c.
Ithen  of  the  stale.
tty.  (F.  -  L)     M.  E.  fa/ri-
patrimmtu.''h.  /atri/ficHittm,
••L.  pairi;  crude  form  of
;  with  su&x  -mcniHrn  (Aiy.tD
(F.  *  Low  U  -  Gk.)    O.  F. L.  patriota.  —  Gk.  iroT/Mumjr, Uow-couMtryman.*Gk.  varpiii. vorpi-,  for  irar^^  a  father.     % <A patrioi  arose  in  Ftrrnh. pertaining  to  the  fathei^  of .— L.)  F./tt/rij/iyM*  ( Lituc). h,  parn'-f  crade  fonn  Qi pater, coined  ;    /r/-  lieing  Greek.) F.  — L,)     F.  /«j/«w.-L.  /o- of  fatromw.   a    protector ; Item  of /aUr,  father. (F.  -  L.  -  Gk.)     O.  F. I*,  fat r en y miens.  •  Gk. belonging    to    the    father's var/xkwv/uo,    a    name    t akeii ET.  «Ck<  war^  ,  for  war^p,  a [,  a  naina  ;  Ke  Nam«. an  example,  model  to  work M.  E.  /a/Mm  ;  tihe  old  s|>ell 'a  patron  . .  aUu  a  pattern. See  patron  (.above). ).  to  rc*ort  to.  U'"-L)     ^^ haunt ;  Cot.     Older  fonn  rt' ).-*L.  rtpQtriart,  to  repair .mIj.  r«-,  back ; /^/Wi2, f^  from  fniri;  crude  form  of
^]r,  tmk.   (E.)     A.  a  /*ff,
/n$/i-).  a  paih>  way,  also  a
■T*r,5kt    /Wi/^a
thkef  on  tbc
```


### [2026-09-07T17:37:57.748Z] TOOL RESULT

```
121
[Ar.  mulitasib.
ar.  tnihjat  'Nadel'  [Präfix  mi-  des  Werk- zeugs und  hait  'Faden',  s.  hier  Nr.  78(>] zurückgeführt  werden.
1503.  Ar.  niuhtasib: 'Eichmeister';  hieraus  sp.  almotacen,  pg. almotacel    'Marktpolizeimeister',  auch aveiiez.    matasej)    'justiciarius,  Markt- nieister'.    [DE  177.    Eguilaz  237.
1504.  Ar.  miikaddam : 'Befehiihaber',  bes.  eines  Schiffes;  hier- aus asp.  almocaden,  apg.  almocadem, p|r.  mocadäo  [nicht  mocadao,  wie  Eguilaz 455  hat;  s.  Constancio  Dicc  697c],  kat. almogaden  'Patron  einer  Barke'.  [DE 315.    Eguilaz  'H'llß'lS.
1505.  Ar.  inukallid: 'Spaßmacher  '  [Part,  praes.  act.  des  Vbs. kalada  II  'nachalimen,  iiachäffen'] ;  hier- aus rum.  mucalit  'dass.,  Hofnarr',  auch als  Adj.,  mucalitUc  'Possenhaftigkeit'.
15GÖ.  Ar.  imikautura: Astronomischer  Fachausdruck  zur  Be- zeichnung der  Himnielskreise,  die  dem Horizont  parallel  laufen  [von  kantara 'Brücke',  s.  hier  Nr.  1057],  plr.  mukan- farät;  hieraus  mit  ar.  Art.  sp.  almocan- tarat,  almicanturad,  pg.  ahnicantarat , frz.  ahnucantarat,  almicantarat  'dass.'. [Eguilaz  2-22.    Devic  DEt  26.
1507.  Ar.  liiuhäri: 'Maullieitreiber',  der  Maultiere,  aber auch  Pferde,  Est],  Kamele  zu  vei mieten hat  [vom  Vh.  karä  'mieten',  s.  hier Nr.  1181,  pait.  praes.  act.  III];  hieraus apg.  ahnoqueire,  sp.  almocrebe,  pg.  al- mocreve,  frz.  moucre,  dtsch.  (gelegentlich in  Reisebeschreibui^gen)  Muker  'Tier- verleiher'. [DE  169.  Eguilaz  230/231. Devic  DEl  169.
1508.  Ar.  iiiitka^wä: 'PappdickiP   [eit;eiithch  'gestärkl.',  da pari.  pass.  II  von  kawt  'siark,  kräftig'], tk.  ebenso;  hieraus  hw\^.  mokawa ;  rum. mucava  'dass.'.
löOSa  bis  1517a  folgen  nach 1517.
1509.  Ar.  mulk:
'Grundstück,  Liegenschaft',  ebenso  tk. niiilk,  mülük;  hieraus  r\im.nuieag'd3iSS.\
1510.  Pcrg.  uifini:
'Wachs',  ebenso  tk.  niiim  'dass.,  Kerze', hieraus  serb.  nium  'Kerze',  [über  tk. tnumgi/]  rum.  mungiü,  munger  'Kerzen- fabrikaiit',  m!<H.9?/7f 'Keizenfabrik',  kat. sp.  nioniia  'Pech  und  Asphalt',  apg. muminha  'Mischung  vou  Pech  und Quecksilber',  bes.  die  harzige  Masse,  die aus  den  der  Sonne  ausgesetzten  Mumien floß  und  als  heilkräftig  galt.  —  Ar.
mümija  'einbalsamierter  Leichnam'  ist in  dieser  Bedeutung  in  alle  europäischen Sprachen  übergegangen:  it.  mummia, fvz.  motnie,  mimiie,  sp.  momia,  pg.mumia, Adj.  sp.  momio  'abgemagert',  vam.mumie 'Mumie',  momie,  nioniue  'Vogelscheuche, Popanz';  engl,  tmunrny,  ndl.  mummie, dtsch.  Mumie;  russ.  murniju.  [Eguilaz 457.    ML  5743.    Kluge  317.
151 1.  Ar.  iiiunädija: 'Versteigerung'  [vom  Vb.  nadä  'rufen' III,  eigentlich  munäda  'Ort,  wo  man veisteigeit',  also  synonym  zu  sük]; hieraus  sp.almoneda,  pg- «^woec?« 'dass.'. [DE  172/174.  EguÜHZ  236.   ML  5655.
1512.  Ar.  iitiui§T: 'Briefschreiber,  Korrespondent'  [part. praes.  act.  des  Vbs.  nasa'a  IV  'erziehen, Briefe  und  Dokumente  aufsetzen'],  ebenso hind.  munnhi  'Interpret,  Schreiber,  Se- kretär'; hieraus  anglomd.  engl. moonshee 'eingeborener  Sprachlehrer',  bes.  für Arabisch,  Persisch  und  Urdu.  In  kauf- männischen Geschäften  hat  man  meistens einen  moonshi  zur  Entzifferung  der  oft Schwei-  lesbaien  Hiindschriflen  in  orien- talisch geschriebenen  Briefen.  [Hobson- Jobson  581.
1513.  Ar.  miinti«:
'Stinkend,  faulend';  hieraus  siz.  »HmiiM« 'stinkendes  Wasser,  das  aus  den  Schwefel- quellen herausflie.ßl'.    [GrSVociSic  241.
1514.  Per.»^.  uiiir:
'Glasur,  Email';  hieraus  russ.  mur 'Glasurmasse',  murawa  'Glasur'.
```


## [2026-09-07T17:38:13.126Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=12023' SKT.txt | grep -c $'\\f'\necho \"--- context of mummy entry ---\"\nsed -n '12010,12030p' SKT.txt",
 "description": "Find SKT leaf of mummy entry"
}
```


### [2026-09-07T17:38:14.399Z] TOOL RESULT

```
309
--- context of mummy entry ---
muIti£ariou8.  (L.)  L.  multifanus, manifold ;  the  orig.  sense  seems  to  be '  many  speaking,*  l.e.  speaking  on  many subjcctfi.vL.  multi-,  for  muUux,  majiy ; fori,  to  speak :  see  Fate.
multiply.  (F.-L.)  F,  mu/tip/itr.»L. muitifi/icare.  —  V,,  muitiplU-,  from  multi- plex, nuny'fold  ;  cf.  plic-^t,  to  fold.  Sec Plait.
MuZQl  silence!  (E.)  M.  £.  mam,  mum, to  express  the  least  sound  made  with  clo<>cd lips.     Cf.  L.  mu,  Gk.  ftv  (the  Mime).
mumble,  to  speak  indistinctly.  (£.) Put  for  mummU.  M.E.  memtltn,  mameUti, to  speak  indistinctly :  frequent  form  due  to M.  £.  mem,  mum  (abo\-e).
mummer,  a  masker,  buffoon.  (F.  —  Du.) O.  F.  mcmmeur,  'a  mummer,  one  that goes  a*mttmmiQg  i'  Cot.  — O.  Du.  minMivrrA, to  go  a-mnmming ;  cf.  mom-aaisieht,  a mummer's  mask ;  Low.  G.  mummi,  a  mask, p.  The  word  is  imitative,  from  the  sound mum  or  mopi,  used  by  nurses  to  frighten or  amuse  children,  at  (he  same  time  pre- tending to  cover  their  faces.  Cf.  G.  mum- mrl,  a  bug-bear.  Der.  mtumtntr-'y,  O.  F, mommerie.
mump,  to  mamble,  nlk,  beg.  (D«.) A  mumper  was  a  cant  term  Cot  ^\k^jgu.<*
1-3
198
MUMBLE.
N ^
Du.  memptn,  to  mump,  cheat  (Scwcl)  ;  cf. tnommiUn,  mompeltn^  to  mamble  tHex- liain).  Tlius  mump  is  merely  jlq  emphntic form  of  mun,  O.  Da.  mommtn^  to  say mum,  also  to  mask.  Cf.  Goth,  bi-mamfy'an^ to  deride :  likewise  of  imitmtlve  origin.
miimpB.  (Du.)  'To  have  the  mumfs* or  *  to  be  in  the  mumps  '  was  to  be  sulky or  sullen  ;  hence  it  was  transferred  to  the disease  which  gave  one  a  stillcn  i4>pcafance. From  mump  i  above).
Mumble,  Mummer;  see  Hum.
Mummy.  (F.  -  Ital.  -  Per».)  O.  F. mumit,  a  mummy.»Ita].  mummia.^Vcn, MtimJyiff*  A  mummy,  embalmed  body.«> Vcn,  m^rrf  wax,  much  used  in  embalming.
Mump.  MumpB ;  see  Mum.
Munch,  to  chew.  (E.)  M.  E.  monchen (Chaucer).  Doubtless  an  imitative  word, like  mumblt.  %  It  cannot  be  from  F. martyr  (  =  L.  mandttcare).
Mundane,  worldly.  (F.  -  L)  M.  E. mottJain.  »  F.  monJain-  «  L.  mumfanus, ndi.  from  mundm,  tlic  world  (lit.  order).— L.  muf$dus,  clean,  adorned ;  cf.  Skt.  mand, toadom.     (VMAND.)
■upramundane.  (L.)  L.  supra, above  ;  mundus ;  the  world.
Municipal.  (F.*L.)  F.  munin'pa/." L.  mMnui'pa/:!,  relating  to  a  town-ship.  —  \.. muftidpium^  a  township  which  had  the rights  of  Roman  citizenship,  whilst  retain- ing its  own  laws.  — L.  municip-,  stem  of municfps,  a  free  citizen,  one  who  under- takes duties.  —  L.  muni-f  for  munus,  obliga- tion, duty;  capere.  lo  take.     (^MU.)
munificence,  liberality.  (F.  —  L.)  F. munificence.  —  L.  munificmtia\  formed  from mumficus,  bountiful.  —  L.  muni-,  for  munus, ft  duly,  also  a  present;  ^-,  (or/act/t,  to moke.
remunerata,  to  recompenoe.  (L.) From  pp.  of  rtmunerart,  remunerari, lo  rewanl.- L.  »-,  again;  munerari^  to discharge  an  office,  from  mun'r-,  stem  of mttnus,  an  nfTice  (above).
```


## [2026-09-07T17:38:14.719Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM موميا / مومياء ===\"\ngrep -n \"مومي\\|موميا\\|الموم\\|( موم\" AFM_pages.txt 2>/dev/null | head -20\nls | head -50",
 "description": "Grep Addi Shir for mumiya"
}
```


### [2026-09-07T17:38:14.776Z] TOOL RESULT

```
=== AFM موميا / مومياء ===
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


## [2026-09-07T17:38:33.115Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM.txt mumiya ===\"\ngrep -n \"مومي\\|المومي\\|موميا\" AFM.txt AFM_alt.txt 2>/dev/null | head -20\necho \"=== AFM_pages 148 area ===\"\npython3 - <<'EOF'\nimport re\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt'\ns=open(p,encoding='utf-8',errors='replace').read()\ni=s.find('موميا')\nprint('idx',i)\nfor m in re.finditer('مومي',s):\n    print(m.start(), s[max(0,m.start()-200):m.start()+300].replace('\\n',' | '))\n    print('---')\nEOF",
 "description": "Search Addi Shir for mumiya"
}
```


## [2026-09-07T17:38:34.503Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['PLA','AFM','ISS']:\n    print(k, json.dumps(d[k],ensure_ascii=False,indent=1))\n\"",
 "description": "Full refs entries for PLA AFM ISS"
}
```


### [2026-09-07T17:38:34.544Z] TOOL RESULT

```
=== AFM.txt mumiya ===
=== AFM_pages 148 area ===
idx -1
```


### [2026-09-07T17:38:35.881Z] TOOL RESULT

```
PLA {
 "title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988",
 "edition_found": null,
 "kind": "archive_djvu",
 "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)",
 "identifier": null,
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"
 ],
 "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).",
 "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "notes": "Open full text obtained. Alphabetical Arabic headwords with Persian/MP etyma; OCR fair (German + transliteration), Arabic script mostly garbled. Provenance: a user upload of an in-copyright 1988 Harrassowitz book — grey copy; publisher sells it (harrassowitz-verlag.de).",
 "scans": [
  {
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf",
   "first_printed": 1,
   "last_printed": 300,
   "pdf_offset": 0,
   "lang": "deu+ara"
  }
 ],
 "cites": "page number of Asbaghi, Persische Lehnwörter im Arabischen (1988), alphabetical by Arabic word"
}
AFM {
 "title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)",
 "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"
 ],
 "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.",
 "cites": "page number of Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (1908)"
}
ISS {
 "title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967",
 "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute",
 "kind": "google_books_preview+archive_restricted",
 "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)",
 "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only",
 "local_file": null,
 "page_offset": "DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Khotanese Texts VI itself is not online. Nourai's ISS page numbers cannot be checked directly; the Dictionary of Khotan Saka (headword at line start, Khotanese in transliteration, with 'Pok.' refs) covers the same etymological material and can verify the substance of a claim.",
 "notes": "Tried IA ('indo-scythian', 'zambasta', 'khotanese texts'), Google Books API. || RE-SEARCH 2026-09: preview only (Google Books partial view of the 2009 reprint — usable for spot checks); no open full text. A dokumen.pub upload exists (not used)."
}
```


## [2026-09-07T17:38:41.230Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA mumiya ===\"\ngrep -n -i \"mumiya\\|mūmiyā\\|mūmiyā\\|mumiyā\\|mūm\\b\\|mum '\" incoming/PLA/PLA_pages.txt | head -20\necho \"=== PLA leaf 269 (p.254) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==269' incoming/PLA/PLA_pages.txt | head -60",
 "description": "Asbaghi p.254"
}
```


### [2026-09-07T17:38:42.566Z] TOOL RESULT

```
=== PLA mumiya ===
14242:       «Le, mumiya Ppers.(» müm "Wachs"                                                 ©.
14247:ade     -       umiyya:              s.     mumiya.
=== PLA leaf 269 (p.254) ===
müg                                                                            254                                                      maybuhtag


Or - müg:             "Überstiefel"                      pers.         I zus      pers.       5, mug mp.                3     mok        "Schuhe"
                aw.        paiti-Smuxta                    "beschuhen",               paz.     mok        ist   ein    weit-
      verbreitetes                     Lehnwort,                vgl.        talm.,     syr.          Ko;        Pin,        ar.        3r °.


e>-     müm:          "Wachs"             pers.          3, mand.            mumia     4      syr.        D%>,


lu.     -       umiyä:            "Mumie"             aus       pers.       müm      "eine     durch        Austrocknen                od.   Ein-
       balsamieren                   vor       der       Verwesung             geschützte           Leiche"             it.       mumia           ar,

       «Le, mumiya Ppers.(» müm "Wachs"                                                 ©.
       Mumie: —                 pers,          >ar.             it.
       Davon         Mumifikation                     "Einbalsamierung"                            pers.        > er.       >, lat.
       mumifizieren:                      "einbalsamieren"T pers. ar.                                           —>lat.             .

ade     -       umiyya:              s.     mumiya.


=      - mawizag:                     "Rosinen"             aus        pers.      =       mawiz       ®     —mp. s\oss mizuk                  2
       syr.      u” 0                10,


wol         - mayadin:                 Pl.       v.      all, maidän              q. v.

Ge          -   maybuhtaß:                  "Sirup"             aus     pers.        An        mai-poxte          11          mp.»s mad
       "Wein"                   aw.       masa        12    + poxtag            pass.        Pt.     v.     ww poxtan             "kochen"        13,
       syr. \Anks» (pers.                             Koss)             14,



1. Muhit s. v.
2.    Nyberg         Bd.        II     s.      v.
3.    Wahrmund             s.     v.
4.    Macuch          s.    Vv.
5.    Brockelmann                 s.      v.
6.    Wahrig          2566,          Lokotsch              S.    121.
7.    Fremdwörterbuch                       s.      v.
8. Muhit         s. v.
9.    pahl.-paz.                S.     v.
10.    Brockelmann                   s.     v.
11.    BQ.      s.     v.,        Addai          Scher          s.     v.

12.    Nyberg          Bd.        II      s.     v.
13.    Mackenzie                s.     v.
14.    Brockelmann                   s.     v.
```


## [2026-09-07T17:38:42.827Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN mudra / muhr / seal ===\"\ngrep -n -i \"mudra\\|muhr\\|mudrā\" KLN_1966.txt | head -20\necho \"=== HRN muhr ===\"\ngrep -n -i \"muhr\\|mohr\" HRN.txt | head -20",
 "description": "Klein mudra, Horn muhr"
}
```


### [2026-09-07T17:38:42.893Z] TOOL RESULT

```
=== KLN mudra / muhr / seal ===
24166:Mohock,  n.,  a  member  of  a  gang  of  aristocratic ruffians.  —  A  var.  of  Mohawk, mohur,  n.,  formerly,  a  gold  coin  of  India.  —  Hind. muhur,  muhr,  fr.  Pers.  muhr,  ‘seal,  coin’,  fr.  01. mudra,  ‘seal,  coin’.
=== HRN muhr ===
8703:1001. muhr 'Siegel; Siegelring,
8705:mudrak 'B,ing'(?), vd. 2 (18) Gl.^), nmdar, muhr 'Siegel'
16432:muhr 1001.
```


## [2026-09-07T17:38:54.741Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8690,8730p' HRN.txt\necho \"=== leaf of line 8703 ===\"\nawk 'NR<=8703' HRN.txt | grep -c $'\\f'",
 "description": "Horn entry 1001 muhr"
}
```


### [2026-09-07T17:38:55.889Z] TOOL RESULT

```
phlv. mas gross, grösser, grössest', masist, mas(i)st,
vergl. 7nas[mayan *Grossmagier (AlbSnlnl), masTh%
mahist, päz. meh (PPGL); arm. vergl. mec gross' (H.
No. 191).
af/. masar 'älter, Herr*.
Vergl. zu bih (No. 241).
1000. mihr *Sonne; Liebe', mihr[ban 'freundlich, wohl-
wollend*.
ap. Mid^ra^, vergl. Vaulmisa-; aw. Mi&ra-, mi&ra^
'Vertrag*; phlv. mür, päz. mihir (vergl. Meherdates,
Tac, MsQfiBQorig^ Proc, skr. LW. mihird- *Sonne');
ai. Mitrd", mitrd- 'Freund*.
minj. mira 'Sonne.
1001. muhr 'Siegel; Siegelring,
skr. mudrd- 'Siegel, Siegelring; phlv. mutrOk d. i.
mudrak 'B,ing'(?), vd. 2 (18) Gl.^), nmdar, muhr 'Siegel'
(PPGL), chald. LW. piniD, arm. LW. murhak.
LW. kurd. mör (H.-Sch.); oss. mi/ur; bei. vergl.
murdan, murdänay 'Finger* (No. 242).
^) Belege aus dem äähnäme (Maoan) bei Noldeke, ZDMO.,
46, 139.
*) P.-Vend. masäi (vergl. dräjlh^ No. 547).
*j Darmesteter, 6t. ir. I, 93 Note 3 (sehr unsicher).- 225 —
Weber, Sitzber. BAW. 1887, PärasTprakäija S. 5,
erklärt skr. mudrä" für *egyptisch*, aus ap. Mudräya-
entlehnt.
10O2. mih/mmfj mlhman (*mehman) 'Gast, Hausfreund'.
aw. i/^ma^f' , mi&naiti 'weilen , bleiben' — das np.
mihman lautlich genau entsprechende aw. ma^dman-
bedeutet nur 'Belegung (einer Hündin)'; phlv. mShmatt
Gast', m^hmänlh ; ai. vergl. mithds 'zusammen, gemein-
schaftlich'.
kurd. mevan 'Gast'; afy. nwlmana (Darmesteter);
sar. LW. meimdn,
1003. mei 'Wein, jüd.-pers., ^^O.
In np. mei, phlv. mai, vd. 5 (132), sind aw. madv-
'Honig', ai. mädhu- süss; Honig, Meth' und aw. maSa-
'Rauschtrank', ai. indda- das. zusammengefallen; vergl.
ksl. wedü 'Honig, Wein', nhd. Meth etc.
Hierher gehört auch np. meivlz {*meive2?) 'Rosine'
(AM. 174 Zeile 5 und 1 v. u.), gewöhnlich mevlZy
=== leaf of line 8703 ===
238
```


## [2026-09-07T17:38:57.270Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD muhr ===\"\ngrep -n -i \"muhr\\|mudr\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB muhr ===\"\ngrep -n -i \"muhr\\|mudr\" NYB_vol2_glossary.txt | head -20\necho \"=== SOD mwhrg / mudr ===\"\ngrep -n -i \"mwhr\\|muhr\\|mwdr\" SOD_pages.txt SOD.txt | head -20",
 "description": "MacKenzie, Nyberg, Gharib for muhr"
}
```


### [2026-09-07T17:38:57.348Z] TOOL RESULT

```
=== PHD muhr ===
PHD.txt:491:méx [myh | P myx, N ~] peg, nail. ~ ī gàh: astr. Polaris, pole star. 1-3méz-, v. mézidan, mëzišn, mistan. mēzd [my()zd | № тёз] offering, meal. „bān [-p’n' | N ~] host. mézidan, 'méz- [myc-ytn!] suck. *mézisn [myckn'] blinking, twinkling. mih [mt!] false, contrary, opposite. mihēxt [mytwht!] falsehood. imihr [mtr! | M myhr, N —] Mithra; sun; cal. 7th month; 16th day. tmihr [mtr!, etc.] contract, bond. šmihr [mtr!, etc.] love, friendship. mihrbān [mtr'p?n! | Р myhrb’n, N ~] friendly, kind. mihr-dróz [mtr'dhwc] = mihródruj. mihródruj [mtr?w-, mtrwk-diwe = Av. mitlyo.drujim] contract-breaker. ~th: breaking faith. mihr-zan [mtr'zn'] = mihródruj. mij(ag) [myc(k') | N muz(a)] eyelid; eyelash. mijüg (myc-, myšwk! | IN mizü] lentil. mir-, v. murdan. mistan, 3mëz- [mstn', myc- | N mézidan] urinate. -i$n(ih): urination. mizag [m(y)ck! | N maza] taste. ~darih [-d’lyh] (sense of) taste. ~ӧтапа [отпа] tasty. mizd [m(y)zd | N muzd] reward, hire, pay. ~war [-wbl | N -àr] hireling. *mizné [m(y)znydy] mist, dew. mög [mwk!] shoe. 5 *moy-mard [mgw-mit', -gGBRA | N muy) magus. mör [mwl | N <) ant. mórd [mwlt! | N ~] myrtle. morwārīd [mwlw'lyt! | M mwrwryd, N ~] pearl. *mowbed [mgwpt' | N móbad] Mazdean priest. móy [mwd | N ~] hair. móya$ [mwdk' | N méya] lamentation. móyen [mwdyn'] (made of) hair. moz [mwe | N ~] banana. mózag [mzvck! | N тоха] shoe. *mūdag [mwtk'} spoilt, destroyed. muy [DKRA < А dgP | N mux] date-palm. muhr [muwdl | M mwhr, N ~] seal. Сар [mwhlk! | P mwhrg, N ~a] bead, vertebra, piece (in backgammon, etc.). *muhrišn [*mwtl$n!] excrement. mulān [mwi?n'] belly (daevic).
PHD.txt:944:bead muhrag.
PHD.txt:1830:excrement gūh, hixr, muhrišn.
PHD.txt:3122:piece  pürag; (backgammon, muhrag.
PHD.txt:3541:seal (n.) muhr.
PHD.txt:4205:vertebra muhrag.
PHD.txt:4860:muhrign
PHD.txt:4871:1 az! muhrag mang, moy saxwanī moyén tis’, cis! tis-izt moyag muhr osmar-t бёгпагї$пї O$murdan! ket murdar mog
PHD_mackenzie.txt:3600:muhr [mwdll M mwhr, N -] seal.
PHD_mackenzie.txt:3604:·muhri~n [mwtlln l ] excrement.
PHD_mackenzie.txt:6024: bead muhrag.                                between andarag, mayan.
PHD_mackenzie.txt:6549:excrement guh, hixr, muhrisn.                      fan damenag.
PHD_mackenzie.txt:7280:   muhrag.                                 poll-tax gazidag.
PHD_mackenzie.txt:7511:sable samor.                               seal (n.) muhr.
PHD_mackenzie.txt:7901:vertebra muhrag.                         wallflower herig.
PHD_mackenzie.txt:9144:man:-                     -~        muhrisn                '~t"rG
PHD_mackenzie.txt:9164:muhrag                   \~(6        mezd, mizd                    ~
PHD_mackenzie.txt:9176:muhr                      ~r6        laharI
=== NYB muhr ===
895:bahr [b’hl] lot, share, portion 692°. 9019.11; (the part played by the priest in the service =) ministry 5319-1? (v.s. v. arzä- nikénitan), a synonym of yazisn (q. v.); this sense is confirmed by Zsprm XII, 6: Pourusäsp bahr o öi hilāi ke-š patiš aržānīkēh ‘P. shall leave the bahr to the one who has the qualification for it’, corresponding to (Pourusäsp...) yazišn 6 yastärän *hārēfūt (v. hareftan), with the gl. kū 6 yazāt kē apāyet yaštan 5314-15; — happiness, prosperity: tan ~ bodily beauty 22%, — Av. (923) baxadra-; Ps bhly; MPrth bhr ’*ate’; MPrs bhr (A-H I), h’mbhr "having the same share’ (A-H II); Paz. bahar, Skr. v. vibhäga and samrddhi; NP barx. [It would be tempt- ing to connect (čan) bahr with Skr bhadra- ‘beautiful, happy’; phonetically there is no difficulty, cf Skr mudrā: muhr ‘seal’ ; Av. baóra- is attested in hu-baóra- (1828) ‘happy’; thus Bailey in A. M., N.S. IT: 1, 1952, 32].
1571:Frāx'-kart [~-krt'] the name of a myth- ical lake; later: the great ocean 461. 9316.22, _ A translation of Av. (1429) Vouru.kaša- (< *-karta-) ‘(the lake) with vast bays’, v. früx". Mx transliterates Var-kaš, Skr. v. ksira-samudra.
2589:muhrak [mwhlk'] draughtsman (in the tric-trac game) 1208-16, — NP muhrah.
2625:muzrayik [mwel’dyk] Egyptian, of Alex- ander the Great 1075-12, - OP mudräya-, SW form presupposing a NW form muz-.
3988:vartišn [wltšn'] the act of turning: 1. han i avdom ~ the last turn, of the end of the world and the fraškart (q. v.) 4619; ~ 4 axtarün u gartišn 4 spahr the revolu- tion of the fixed stars and the rotation of the sphere 1205-5; ~ u gartišn + muhrak the moving and transposing of the draughtsmen 12015, — 2. pred.: turned, became 41??, — V. vastan.
4914:magu-: magū manā: man martiya-: mart Margu-: Marv ni-māy-: nimūtan mayūxa-: mēx mudräya-: muzräyik
7257:mih (mahist): mas mihmän: mahmančh mir: mérak miyànji: miyànjikeh mizd, muzd: mizd mčbad: magu-pat mü, müy: mod muhrah: muhrak müq: mök
=== SOD mwhrg / mudr ===
SOD.txt:44645:5523  mwhrdyb   M  *A>j$* 
SOD.txt:44646:muhr-5ip  ©*mwdr\  Parth.  ©ob.  -yy 
SOD_pages.txt:19537:     GMS 408-, Anc. Lett. 4.6; Sund. AoFviii 1981             5523 mwhrdyb M                                        *A>j$*
SOD_pages.txt:19538:       p2l6, 2aV2                                                  muhr-5ip ©*mwdr\ Parth. ©ob. -yy
```


## [2026-09-07T17:39:16.795Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD mwhr all ===\"\ngrep -n \"mwhr\" SOD.txt | head -20\necho \"=== DKS mura / mudra ===\"\ngrep -n -i \"mura-\\|mudra\\|muhr\" ISS_alt_DKS.txt | head -30",
 "description": "Sogdian and Bailey lookups"
}
```


### [2026-09-07T17:39:16.851Z] TOOL RESULT

```
=== SOD mwhr all ===
44645:5523  mwhrdyb   M  *A>j$* 
=== DKS mura / mudra ===
336:amga-' limb", Sid. 2v4; Sid. 128v4 aga-, from ang-' to bend’, in Ау, amura- of zairimyanura- 'with covered limbs’ epithet of the tortoise; to amgusta-, Oss. D. Tuong, jong, I. uäng, uong, ong, plur. ибпвій 'limb' (from *vivanga- or secondary iu-, j-, u-). Zor.P. zarimangur has -ng- for Av. -m-. The BS loan-word is in amga-prattyamga v 32723. See agalaka, s.v. asaulaka.
525:aysmüra- 'sound, noise', 11 3416 aysmüryau jühanai süüida pavanaka ‘amorous with sounds they raise the pollens', == 46:26 amysmüryau jühanai sañida pavinaka, = HI3TII dmysmüryau juhaunai 5014 pavánaka. From uys- with base mür-, mvir- ' to sound, sing’ see s.v. mura- ‘speech’,
700:ahürnurgyatete ‘not forgetfulness’, K 2, 135v2-3 аййти- rgyatete küdanai; K. т, 14814 ahümurgyatetinà paga, Tib. mi brjed-pahi stobs ‘power of mot forgetting’. See ahaumaurrjd, From hamura-.
809:ümura- ‘short’, contrasting with dára- ‘long’, V 299, 2rI
810:: āmuro jsino ' short life’; v 297, Mac. а, bẹ karma ісатёпа hog ümur(d) 'the act (karma) by which a man (gets) a short (life)'. From a with mura- to Ау. mūra- ‘defective’, müraka- beside dahaka-. IE Pok. 751-3 mū- in Khotan Saka muta ‘dumb’, O.Ind. miüka-, Celtic Ir. mut ‘short’, Lat. mutilus, тих, Greek uuxós, Norw. mua ‘be silent’.
1089:ditcá- ‘water’, nom. sing. v 263, 89v1 атгіїја піса narámd, BS С 37, 7721 amrtodaham pravahati, Tib. bdud-réihi ¿hu byun-no 'the water of amrta-elixir issues'; acc. sing., Z 2:16 ütco, K 29:204 hīyā utca, =K 38:139 nisà ta utci ‘she poured out the water’; gen. sing. Z üce, йсе jsa; loc. sing. Z ica; plur. Z 20-5 ütce; later Sid. логу utca, Sid. 131V5 utce, 135У2 ісе jsa, 8v1 ütci, 6v4 utci, 14112 исе jsa, 1343 lice jsa, 124V4 fici jsa, 9г2 uci jsa; loc. sing. 11 50:58 sa khil dai aca pasüste t as fire burns in water’, Manj. 287 dai ace pasva ' fire burning in water’ ; gen. sing. I1163:134— 5 cu maistye dai byauca së cu mista utca cu mistye иса руаиса së cu bäysyā fara hawvi ' as to the cure for a great fire, that is a great water, as to the cure for a great water, that is strength in the arms (for swimming)'; acc. sing. v 215, 702 khu hwü-cai ütca ne byehi (not mye) ‘when Hvü-cai(?) does not get water’, ibid. 5 kamalajd піса parāmdä ' they sold water for individuals(?)'. With suffix Z 342 ütcäka puvàta vasuta ' cool pure water’. Adjectives, ficaa-, Sid. 19vt fica nimva ' salt from water’, BS samudra-, Tib. méhohi lan-chva; 1 161, 76v4 исӣ namva; n1 37:30 asna ttā tciraukd п Ната йсй müraká ' pigeons, then ducks and partridges, water birds’; Z 1:87 (р:'351) samu kho hhavà ücai bätäva ' like watery foam, lightning’; ücinaa-, SuvO. 2477 йсїпєї djdvdsd, BS saliloraga- ' water snake', JS 19v4 itcinai garkhä pasë ‘heavy load of water’ with negative, 11 85:27 agiütcd mau "liquor without water’; ш 80°30 utcála kauysá ' water-jar', Compounds, Sid. 132v4 ucümkatüm astamna satta hiya gusta, Tib. čhu-na gnas- pahi srog-£hags iia-la sogs-pahi ѓа ' flesh of beings living in the water’; K 106:256 utca-kaná Ната nai natsatme ‘a drop of water does not quench thirst’. As second com- ponent, I 153, 63v5 gürütca ' juice of grapes’, 1 189, 11111 riysütcana ' rice-water', Sid. r3rrr fetutcd 'curds', Tib. do kha-éhu, 1 169, 8sv4. fitvütca, 1 171, 87r4 barütcana ' rain water’, 1 171, 87r3 khavarutcana ' water of khavara-
1264:aurggá-, orgà- ‘reverence’, Ш 4, 1015 aurgga Туй muhu jsa punosari jsa biiéüni gyastand balysünd halaiyasta ‘тау there be reverence from me from Punosari towards all the deva Buddhas’; 111 20, 3b2 orga í harbisünd gyastānä baysünd и baudhisatuám hàlaiyastá; nx 58-1 aurga t Шуе halai ‘тау there be reverence to it’; acc. sing, SuvO. 5474 Шапи aurgo tsutä hámáte, BS namas-krtva, ‘Һе has come to reverence to them; later Sid. 2v1 Jarbifa-bvakye hàlai аита tsue ‘һе сате to reverence to the all-knowing one’; Tib. kun-mkhyen phyag béal-te; K 139:952 amjalä dastyau jsa aurga yude ‘with hands in anjali-position he made reverence’; dyadic K 155:59 ttanai tsū aurga sakaca jsāmne sand 'therefore to him І come to reverence, bowing, honouring’; gen. sing. Bed 46v2 aurgyi tsüme jsa pajsam disëme jsa, BS vandana-püjana-desanataya. Hence not as proposed earlier inst. sing. to orga-. Adjective aurgautya-, V 246, 13a1 caittyd māñadä hime aurgaviya ' is to be revered like a caitya-shrine', = K 97:198-9 caitye mañada hami aurgaviya, BS vandaniya-. From archaic ü-barga, retaining -rg-, unlike mura- ‘bird’ (*mrga-), to barg- 'to reverence’, see cognates s.v, bulj-.
1267:M grand , see Zoroastrian Problems, ed. 2, 1971, vii- . For orr- from a different frai- 'to question', see pA See parssa- ' venerable'; and frafa-, s.v. mura-.
1317:kan- 'cut, engrave', see s.v. hatcan- (not in Khotan Saka), N.Pers. kandan ' engrave', muhr-kan ‘engraver of seals’, Armen. lw Å'andak ‘engraving’, Sogd. Bud. infinitive siut.
1319:Капй- ‘гор (of water)’, V 247, 16a3-4 tta tta mi khu tcahora mahäsamudrra ${йте пса jsa hambada ttyam hamada псі hiyam kanam hakhiysd pamāka hame 'just so a5 there are four great seas filled with water, of those in- deed the number of drops of water is countable', BS yatha catoüro mahāsamudrä udaka-paripürnà bhaveyuh, tatra ekaika-vindum sakyam ganayitum (kanam gen. plur., BS vindu- *drop'); K 106-256 utca Капа ttara nai naisaime ta drop of water does not quench thirst'; 1 179, 98v3 hauda kani ' seven drops’; 111 85:63 Asi kanai ' six drops'; 22-118 kho ggard sumird $fasvand haste pata mahüsamudrá sšo- Rana utca baña 'as mustard appears in relation to Mount Sumeru, water in one drop (compound adjective) in relation to the great sea’; Z 2:108 inst. plur. hanyau. With suffix -aka-, K 9o:750 khu mahüsamudra äna së kanaka üska usthamjá ‘as from the great sea he draws up
2494:naiyi ‘he may not have’, see s.v. hámura- (IK. 144, 1v4).
2756:teada ‘vicinity, surroundings’, K 29:194 Sika vara naista südana tcada vivsájai ‘опе there sat Sudhana beside the pool’, К. 38132-3 basi nestä т küsdi vari tcáda vivsümje ‘in the grove he sat there beside the pool of the palace’; ш 69:95 murrdāņmdä disa vi tcadà ‘еу ranged over the district around '; п 74:62 hai tha mürd kakva jastiña mūra ka tcadà māhāsamāmdrä 'O you bird kakva (ducki), celestial bird if beside the great sea’ (BS mahasamudra-). From base kar- ‘to surround’, karā ‘circle’, adjective kara- ‘surrounding’, to *čartu-, Av. caratu-.
2777:tcalca- ‘boundary, shore, side’, SuvO. 56r mahü-samumdrá tcalcünu "edges, shores of the great sea’, BS samudra- paryanta-, parallel to K 40*10 mahā-simumdri ramja ‘on the shore of the great sea’; Z 6:9 kho rru rrasta tcalca hárünu "like the straight shore of things’; Z 6-43 cu rro pamjinu skandhànu tcalca ‘which is the boundary of the skandha-masses' ; Z 20:5 ütce pastüte ysarrüiie tcalce jahe ‘waters arisen, green borders, fountains’; 2 4:46 ci tcaíco ggamgye samudri o tcalco sáddhábaysüre' when they come to the bank of the Ganga, of the sea or the bank of the Sindhu’; K g, 4313 me ttuto tcalco (so), пе ttaro, и ne myüiio ' not this border and not that and not the middle one’; V 245, gar audá ustamamjsye tcaci bure kusta ha-cá ysyáte, = K 96:171-2 *auda ustamajsye (ha for mà) tceca büre küsta hüs[a vsyüve 'up to the utmost boundary wherever he is born’; K бт, 39v3 fira ісаса. From *£art-Cà- (-Ic- from -ғ16), to base kart- ‘to cut off’, like O.Slav. kraji ‘border’, to Russ. kroj, kroiti to cut’, IE Рок, 946 skeri-, skri- 'to cut’, base 938-47 (s)ker-, Greek Kepa.
3116:dāra- ‘long’, v 115, баг пе dáru йй ‘it is not long’, BS na cirena hi; V 131, 52, 1b4 dyadic, atë dāru bulysu 'very long’; Sid. aors (dà)ra-jsina ' long-lived', Tib. éhe rin-bar byed-do; SuvO. 5v3 düra-jsinyausu 'long life', BS dirghayugkatü-; K 100283 sadarma {йа düra-vastu hamüve ' may the teaching of the good dharma be long- enduring’ (BS vastu- 'thing"); fem. K 90°745 u jsinai dàra-vastva hime ' and may his life be long'. With buru ‘in measure’, I 255, 170vi dürburu 'long', BS ciram; K 138:926 dár-buru, Tib. rin-bu; Sid. 13815 dara buri va neca hame ‘it is long kept low? (neca = nesta ‘set low"), ВЗ nimno, Tib. dar hdug-pa ' to remain a little’; K 148-66 daura-baimana hamüvai 'may he be of long fortune’. From darga- Чопа’, as āra- ' price’ from arga-, but mura- ‘bird’ from mrga-; O.Pers. darga-, Av. daraga-, daraya-, drüfitta-, drājō; Pahlavi Psalter dely, Zor.P. dgr dyr *dayr, dër, dralma8, N .Pers. dër, diräz, Вај ё dër‘ long, late;time, duration’. IE Pok. 196-7 del-, dlšgh-, O.Ind. dirghd-, drüghistha- ; Greek BoAryós, tv&eAeyris, Got. tulgus ' stead- fast’, O Slav. dlugü, Hitt. daluga-, Lit. ваз.
3417:namva ‘salt’, Sid. 19vr патта, Tib. lan-dhua, Sid. 19v1 nimua, Bid. 130v2 pamjsa nemve ‘the five salts’, listed Sid. 19r5 namvā hiya ni(ske)ci uysdisám ' we expound the list o£ salts’, Tib. lan-révahi bye-brag bsad-de; gen. sing. К. Sar латте hroi raysd 'taste of salt’ (DS rasa-), inst. sing. Ш 92:227 namvena; adjective, 11 88:155 namviimje uci jsá' with salt water", Sid. 8rs namvtje uci jsa, BS lauana-, Tib. lan-dhoa ¿huhi nan-du. "Тһе five salts are named Sid. 19r3 sida-lūm, BS saindhava-, spaju, BS sauvarcala-, bida-linn BS vida-, ттӣја-патга, BS lomaka-, йсй nimva, BS samudra-, This патта can be traced to *namadà (-v- as in рӣоаі ‘his nerves’ beside Sogd. 38m"). Hence to Sogd. Bud. пт’ ВЕ, Man. adjective nm' òk’ ynch, M. Pers. T. umyhg, Zor.P. nmk, N.Pers. namak, Yidya nəmalyo (-o < -d), Sanglēči ләтёу8, Sarikoli samo], nimaðj, Pašto malga, ba-lmanga ' saltless', Рагай namá. Note M.Parth.T. wi ‘salt’, (Av. uru-?), with O.Ind. lavana-.
3519:паѕсуа ‘епі’, JS тзгт ada tvà samudra-nascya 'this earth ending at the sea’, see nesta, näsasta-,
3675:nisas- ' to end’, 2 5:83 kalpä nátastá' the kalpa-period ends’; v 55, 2v5 sa [sina nastá ' the life ends’; noun, K. r, 13515 nátaskya ‘епі’, Tib. уоюѕ-ғи bri-bar; Z 24:252 ndsaskya; Z 6-2 loc. sing. nitasca ‘at the епа’; K 3, 138v2-3 astanu ndgaskye jsa draifu vate ‘һе memorised the beginning with end’, ibid. 138rs-vr ne thatau harbi(su) ttu даш dstanu näşaskye jsa draiu vätu yanindd, Tib. thams-cad čhub-par vsla-ba ma yin-noy JS стагі samudrra-ngscya tending with sea’ (parallel to BS samudra-paryanta-); Bid. 156v5 jsiti nastyāñä padimüre 'they put an end to life’, Tib. srog-la yaw hbab-par byed-pas-na (hbab 'sink, fall’); Sid. 3v4 s£ nascyt pasalamjsya rva ' end o£ spring season’; п 89:48 Jamarrimji nesti maji ‘епа of month Hamürrimja! (3rd spring month). With negative a-, Bed 57v1 anescya, BS ananta- ‘endless’, JS 39v3 aniscyá rasa ‘endless sovereignty’, JS 39r4 amescyand, К. 5164. anüstye. See above v 90, rb2 пайӣ 'end', adjective, 1 177, 93v5 asmarya-müttra, сӣ va utca ñasya hami ' the disease of afmari-miütra ('stone urine’) which has water checked’, BS asmari-krcchra-, from *nišas-ya-. For the participle ‘ended’, the form is ndsata-, SuvO. svz
3842:nvi ‘pledge’, v 11:2 a tta noi oi püri pasateg 'I sent my son as a pledge’; ibid. 5 ta tta not ртазсййй himari 'so (the mura-coins) must be distributed as a pledge’, see gvasc-, Possibly *nipa-, *nipiya- *nuviya- > nvi, to base ти-рй- ‘to deposit, pledge’, Zor.P. ОКМ 717-3; 4 np'k "раё 'pledge', Sogd. Man. np'q, Chorasmian nibzk; with BS трайа- (JRAS 1955, 19; SDTV 56-7), and O.Ind. zivi-, nivi- ' pledge'. See pã- ‘protect’,
3939:pamjusta- 'ünger-ring', Z 13:137 куйе pamjusta parremá küdai pharu nuäsa yidandi 'the cita-ornaments, rings, parrema-ornaments made greatly many noises for him’; K 29:202-3 sh(au)daka jsü ttu pajüsta pharaña diste 'unnoticed he threw that ring into the water-jar', = К. 38:138 taña ha pharirid ратуй! nitaue ' into her pot he threw the ring’, parallel Divyävadāna 458:1 anguli- mudra; K 29:204 khua dya sa pajüsja ' when she saw the ring’, =K 38:139-40 tanauhari pamjñsii дуй ‘Manohar saw the ring’; HI 35727 pajüsta and ш 106:38 pajüsia. From Ppari-anguita- "being around the finger’, Waxi plöngöšt, Yidya parguščë, Munjānīi parguikyiy, Yazg. pary^axt, porg^axt (like Yazg. parast ' bracelet"), Khowar lw ршиприўи. See hamgusta- ' finger', and дт 'thumb'.
3951:baysyau jsa hvata 'spoken by former numberless deva Buddhas’; K 68-201-2 padamjsyau skamdhyau; K 59, 3311 padāmjs aysmü, ibid. 3312 ustamāmjsī, ibid. 33r2 heysdā- mjsüm 'frst оўйапа-, last, present’; Z 4/3 padàmjsi, Z 3°117 padamjsiye; adjective suffix -auysa-, Sid. 103v2 padauysá, Tib. dan-po ' first', Z 20-70 padoysá; inst. sing. Manj. 205 padauyssa, inst. plur. К. 1:35:855 ttyānä padauysyau mistyau mahüsauyau 'with those foremost great mahà-irüvakas ('listeners")'; 11 табың ¿yau padauysyau Буа @ vse(ryau) ‘with those first sixty thousands’; abstract -auza-, K 156'9 padauysauia jsa ‘beginning with'; K 14720 padauysamiia jsa, parallel to BS -adi-, with suffix -ya-kva-, K 145, 3v1 padausikyi mürakyà hivt guttairá ‘the first gotra- family of seals’ (BS mudraka-), K. 144, 2r4 si padausikyi pichastü. simüdhüna devattd jayama sje 'the first (finger) is the meditation (= BS dhyana) of the epiphanous trance-deity'. With au «üm, Manj. 215 padaujsi hera usta 'first thing (and) last’, =Z 5:69 cu váte cu na ro hámare; also -(am)-, Manj. 221 pad(am)jsyt; Manj. 229 padajsi. Compound, Z 6:1 bis-badà, Z 1r2 bi-padaàka 'first of all', SuvO. 54v7 bis-padà. . .nasá ' first part’, BS agra-bhàga-, beside Sid. r42r4 бій pada, Tib. 1Лор-та. Uncertain, K. 110333 pajsa ge vira раййјий “іп the five gati-stages first (?)'. From base fra-— par-, pada < *partah, adjective padata «"partüka-, Zor.P. plt'k *fratük, N.Pers. farda 'to- morrow’, fardáà as bāmdāð ‘dawn’; see below hatáma- ‘foremost’, Av. fratema-; O.Iran. тторбснс-, Adjective padauysa- from "parta(R)-auxa- ' moving in front’, base vagz- or with suffix -auza- (as Oss, D. k'abozä 'twig!). See cognates s.v. ha~, ha, határa-.
4245:paśtä ‘епа, lowest part', paste, JS 38r1 s£ tvünai bàjsinai mahasamudrre апо vara nauhq ce bümne paste па byaide 'this your great sea (BS smaha-samudra-) of merits (buljsà) there without top, in which no bottom is found (dyadic with buna-)'; L, 97:32-3 ttye hivya pastā; ibid. 34 ll[pastà byehe ‘he attains the end’, Tib. mthar phyin-te *coming to the end’; ibid. 34 harbáfsünu avaranünu (BS avarana-) pastà byehe ‘Һе reaches the end of all hind- rances’, Tib, sgrib-pa thams-éad zad-nas (hdzad ' cease"). From *pa(ti)-sti- (or *pa(ti)-sta- ?), to Zor.P. pastak' end. Not with palsti-' back of body’ nor pastā- ‘pool’, For -sti- see ggüsta- 'flesh'.
4422:100-208 paría yanau ‘то do service’; H 115:32 pārsa tta dàsii ' I complete the service’. See above parsa and parysa-. párssa-, pürsa- ‘reverend’, Ш 24, 22a1 cittye manaqulá sa disa parsa hamá ‘like а caitya-shrine this region becomes worshipful', BS caitya-bhüto vandaniyas ca; K 97, 198-9 caitye māñada hami aurgaviya, =V 246, 1321 caittyd mäñadä hime aurgaviya ' like a caitya, becomes reverend’; K 8:55 sā byatarja ttirä buri uvāra pürssa puñauda татрайуа 'that memory is so exalted (BS udaüra-) admirable, meritorious (BS punyavant-), auspicious’ (BS mangaliya-). The atmosphere of reverence and awe would suit a con- nexion with *parsa- beside O.Pers., Av. frasa- (as hatáma- "first! < *fratama-, beside тгар@сна-, pada, parramaa- above) and with the metathesis as in the title pAarsavata- 'judge(?)' from *frafa-pati-. Then frasa-, and *paría pürssa- (keeping secondary -ri-). For Av. fraía-, the traditional Parsi-Persian rendering of frasagar is Arabic- Pers. zāhir- ‘conspicuous, manifest’, which the analysis by base par-i- 'appear, be conspicuous, admirable', IE par- "appear! par-&- whence prk-s-, Iran. frai-, O.Ind. RV prks-, fully confirms (see Zoroastrian Problems, ed. 2, vii-xv), to IE Pok. 789 par-, Greek merapeiv 'show forth’ єйфрастоу: ссе 'clear', Lat. päreo, аррӣтеб, compürea 'appear'. The Parsi-Persian gloss zëhir 'con- spicuous', is for the compound frsgr, see J. J. Modi, The Persian Farziát-Námeh and Kholáseh-i din of Dastur Рага Páhlan 1924, p. 92 of the Kholáseh-i din in Parsi- Persian nam i frigr ma'ni 'st gahir. Тһе same text without the gloss is in E. К. Antia, Pázend Texts, 1909, p. 337. For the developed meaning 'appear, be conspicuous, admirable, wonderful', note also Pindaros, Pythian Ode 6:2 Өатутёу рёусроу 'splendid hall’; Үаупаы yaxi- ‘о appear’,  O.Ind. RV yahksd- 'wonderful apparition’ (Indo-Iranian Journal rr, 1958, 152-6); Bed 48r3 Khotan Saka baysdyamdai gloss to BS pesala- (Tib. des-pa ‘fine, noble’); SuvO. 567 dyana-, BS äsvādanīya-, SuvO, 36v2 dhyàna-, BS rucira-, Zor.P. sahīk with afd ‘conspicuous, admirable’, N.Pers. saht 'lofty (of a tree); admirable (of а queen)’; Celtic O.Ir. airdirc, erdairc "illustrious, celebrated’ (J. Vendryès, Lexique étymologique de l'irlandais ancien, 1959, A 41) For ‘wonder’ duskara- occurs in Buddhist contexts, HI 25, 25a2 dughare jsa 'with wonder’, BS ascarya-. See also above N 17536 айтта ‘admirable’ from *à-frasata- through *à-vrrata- (with orr- < *afri-). The long -2- before two consonants can be seen in parysa- beside parysa- ‘servant’ and karra- ' deaf! < *karua-, but ttarra- ‘herb’ < *trna-. For frai-, see also s.v. mura-, párssa- 'antidote', v 87г6 и hamdāra рага aggadá £üstandá 'and others prepared the antidote, the medicine' (BS agada-), here dyadic; 2 24:213 ttrāmū фйгууа datinau yindà рришр 'so he puts the antidote of the dharma- doctrine into your ears’. From *fati-raxi-a- *pa-raxi-a- > *pürii-a-, base raxi- tto protect, be ready against’, Oss. D. aräxsun, І. araxsyn, aráxst ' be able, ready’, gárz- aráxst ' skilled with tools’ (but not D. aräxässun, L ardxsyn 'repair"); Armen. Iw eraixi- ' guarantee’ (E. Benveniste, TPS 1945, 71); possibly Pazand raxfafui (E. К. Antia, Pazend Texts 83:16). IE Pok. 32 alek- ' keep of’, O.Ind. rdhsati, raksitd-, Greek &A£&co, O.Engl. ealgian ‘protect’,
4471:pimmá “а medicament’, їп go'192 guar, rahi рйппй, siya bghauyd, not identified. Possibly compare Sid. r48v4 samāmdrri phimnd, BS samudra-phena-, 'Tib. rgya- méhohi sbu-ba (' foam”),
4976:baj- ‘be injured, destroyed’, causative bajev-, bajautta-, present, 3 sing. Z 24:47 bajäte; optative, 3 sing. Z 13:78 ko balysi baji pusso mida ' if the Buddha were injured, he would at once die’; v 76, 44r1 bajätä, BS G 37, 3303 nasto; oblique present participle absolutive, J5 18v2 dukhya bajattye ttuite tsu тї orga 'to you sad, injured, I come, with reverence’; 3 plur. Z 24:395 bajeoindd; adjective, SuvO, 27v6 bajevüka, BS pranasaka-; 3 sing. present п 36:94 tta таи 514 paryati pirstà khu ni bajaittá ‘so the mau-wine is, deign to keep it covered, so that it is not spoiled’; = 37, 1223 (corrected numbering SD'TV 36; 39) и tti jsām tta mau sid paryati pirtá khu na bajaittá; ш 24; 204-2111 baysand sabhaugi ttaramdarü anauşkājsī ha(yá) na bajaitti 'the Buddha's sambhogika- non-eternal body may not be injured’ (BS kaya-); 11 28, 4123-4 khu ha uysnaurüpa bulwmand ni bajaitti адата hà yanári o Barkhustánü 'so that the beings’ esteem may not be harmed; do respect (BS ádara-) or reverence’. Preterite to bajev-, Z 15:9 bajottandá; Bid. зог hvāşä jsa bijautta '(water) spoiled by vegetation’, BS fevala-dügita-, Tib. йа-@р yod-de; V 336, 34v6-35r1 Ауе ha(nd hve) ce fina dastána mahà-samudr bajauttu yaná “whoever is the man who can with one hand destroy the great sea’, BS G 37, 31b6—7 asti punah sarvasura kaš cit satvo ya eka-pani- tülena samudram ksapayet, =V 74, 41v4—5 astá sarvastüra ce hand hve ce {па dastána mahü-samumdrru  bajauttu yaná; JS x4vi cu ra hsira bürd ni pastë itīma bajautta
5115:basta- ‘bound’, participle to bait-, ш 20, 4b3 bastd palamgá ‘fixed in paryanka-posture', BS paryankam abhujya; JS 34V4 dyüma-basta 'intent upon ravening (lion)'; v 150, as [[[vátà bastá 'bound upon’; K 67:174 ham vi basti ‘always bound’, =K ут, 8r2 ha vi basta; 3 sing, fem. K 47757 cala basta 'she bound clothes (on him)’; ur 68-70 brriye jsa basta vistáta 'they became bound by love’; Manj. 187 hirvā aysmva basta ' mind bound іп things’; Manj. 410 basta. . ,güva ‘bound. . .loosed'; 3 plur. Manj. 124 bastāda pade ашйуа 'they closed the road to ruins’ (BS apaya-); K. 42:118 Латіхаї va sambaji bastádá 'they formed a plot against him'; K. то, grs pranihäna bastāndä indi 'they made pranidhana-vows'; participle *bastaka-, Manj. 241 beht bastau tta hhot samvadrra. ‘exceedingly continuous so as the wave in the sea' (BS samudra-); =Z, 5:83 pabasto khoiyd samudru.
5996:marsygrü ‘forgive, forget’, JS 3v2 2 plur. imperative, тайа-у 118 marsyarä ürrü 'now forget my fault’. For ‘forget’, see hamura- (*framri-) hence archaic or dialectal suari-:mpi retaining -ri-. From тағ, Orm.
6133:suttaca- "having a golden fine skin (ivac-)', Jātakamālā, text 128, verse 4 uttapta-cümikara-samniküsam Srimad тарий ‘beautiful body like refined gold'. See ysürra- ‘golden’ < *zarnv-a-. Base meu-:mu-, see mura- ‘speech, word' for cagnates.
6159:mutä ‘dumb, mute’, N 169:1 hand kārrä mutä ' blind, deaf, mute’, Prom mau-:mu-, IE Pok. 751-2 mi-, mu- ‘of murmured speech’, O.Ind. müka- ‘dumb’, Greek pükós, Mimis, uuv6óçs ‘dumb’, Lat. mütus, See also sv. mura- ‘word’, and muka-.
6172:muyi 'tiger', v 210°36‹1 muyi salya ‘іл the tiger year, п 145 [[|byüsti muyi ‘3-5 a.m. are the dawn, the tiger's period’ (Chinese Һогагу period); п 116737 mauya hiya viysama salt ' the year of the tiger unfavourab/e ; 11 116-39 mauya salya ‘in the tiger year’. From *mauya- > *miüya-, muyi, mauya-, Sogd. Bud. myw ‘рег’, Tokhara B mewiyo (H. Lüders, SBAW 1933, 1021), the third year in the animal cycle (BSOAS, то, 1937, 928). Possibly to base meu-:mu- ‘to make noise, roar’, IE Pok. 751-2 mil ‘of murmured, roared sound’, See s.v. mü (or vamii JS 29v1), mura- ‘word’, rather than Chinese miau (K. 620:3) ‘cat’:
6182:mür- ' to swarm, teem’, Z 20:41 kye pära jsahera mürindi ‘in whose belly worms swarm’; Ш 76:244 huiyasā agapya йаа bidä ѕатитагӣ khu mürīmdä sam 'as unclean con- temptible human-like beasts swarm just upon the great sea’ (BS maha-samudra-). See mvir- ‘to move', K 109:314. mvara ‘movement’, possibly base mau- mu- thence *mvar-:mūr-, beside mvir- < *mvar-y-.
```


## [2026-09-07T17:39:28.082Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^mura-\\|^mūra-\\|mura- 'seal\\|mūra- ‘seal\\|mura- ‘seal\" ISS_alt_DKS.txt | head\necho \"---\"\ngrep -n \"mūra\" ISS_alt_DKS.txt | head -20",
 "description": "Bailey DKS mura seal headword"
}
```


### [2026-09-07T17:39:28.138Z] TOOL RESULT

```
6183:mura- 'speech, word’, п 114-119 рӣїса-т va dümvam jsa hau:rá murä şte 'then for them from the Düm people there is report, word’; п go*68 и haurüm mura jsa ije va prramiüi pudümdd ‘апі with reports, words, they offered promises to one another’; 11 75:50 haurä таи mam ni iniryau ' they were not making to me report, word’, ш 123:62 haura mümra padimai ‘һе makes speeches, words’, BS alápam karayati; V 314, 3-424 hürau mūrau йа. The word haura- is in п 113:94. hauri ām salā ni bijese ‘ће did not utter word, or speech’ with sala ‘word’ (BS samlàüpa-) in place of mura-. From base mau-:inu- tto make sounds’, thence mu-ar-:mur- (form like phur-, phüde 'foods', and Oss. D. K'udrun k'uärt, I. &'üryn, k'ürd 'to push"). Without -r-, see JS 26v1 mi (or оатӣ) ‘he praised’, to IE Pok. тӣ- ‘to utter murmured sounds’, Hittite mugami 'to utter prayers of lamentation’, OHG māwen о cry out’ (note similarly vās-, s.v. basa-); Oss. D. murd ‘bell’; тоо ‘jaw’, І. muk'u, ТЕ a form men- existed beside men- (as O.Ind. bhanati beside Greek qà-, above bütd "ће spoke’; BS aha), then "Greek" poŭoa, Doric рса, Aiolic potoa ‘goddess of song and poetry’ belongs here. For 'speak' and 'praise', note O.Pers. gaub-, N.Pers göy- “to speak’ beside Sogd. Bud. ywf- tto praise’, Armen. lw govem. For ysürra- 'golden' < *датпта- see below, Ау. zaranu- 'golden', Zor.P., N.Pers. dàl- in dāl-man 'eagle', Av. zaranu-mainis. See below mīvāra-, and аузтйтй- ‘sound’.
---
810:: āmuro jsino ' short life’; v 297, Mac. а, bẹ karma ісатёпа hog ümur(d) 'the act (karma) by which a man (gets) a short (life)'. From a with mura- to Ау. mūra- ‘defective’, müraka- beside dahaka-. IE Pok. 751-3 mū- in Khotan Saka muta ‘dumb’, O.Ind. miüka-, Celtic Ir. mut ‘short’, Lat. mutilus, тих, Greek uuxós, Norw. mua ‘be silent’.
855:ära 'value, price’, п 0:155 #201 mūra āra ‘value copper mürā’, п 9:157 іа pvaica ата ‘value of опе pvaica- covering’, I1 77:24 dvāsa {аса āra ' value twelve saci (silk pieces)", п 77-24—5 drrai saca āra. See VI 440 and SDTV 32, 155. Possibly HI 71:143 ara hanaste ‘Һе lost worth’, or ‘he got worth’ (if not BS adara- ' respect). Base arg- ‘be worth, Av. araj- "be worth’, arajah- ‘value, price’, Sogd. "ry, Oss. DI. ary ‘price’, Zor.P. ar$- 'be worth’, N.Pers. arsān, arz, arj, arjmand, Armen. lw атап ‘worthy’, are ‘is worth’, IE Pok. 32-3 aig*h-, O.Ind.
864:атта ‘beat, flap or spread’, п 75:62-3 hai tha mūrä kakva jastūña mūra Ка tcadà māhāsamāmdrä müfiamda krrimgä аттё para sesahá daraujsa * О you bird kakva (partridge ?),
1297:ysyama (-ya- for -ü-), = 11i 46:16 kakva tcirauka u papüska bimjakye, = u1 34:8 kakva tcirüka и papüskya bejakyá, with diferent ш 37:29-30 stürye papüsakyd bidye baijakye ysümá ‘starling, kakva, hoopoe, sparrow, ysüma-', beside tcirauka 'anas casarca, BS cakraváka-, and bīdye ' pecker, BS ріка-(?)'. The further passage ш 96:6 [[/(mü)ra kakye mūra sye mūra hayarida nva kşama àsaijvà ће... birds, the ka&ya-birds, the geese sport themselves at will in the pools’, and the passage t1 75:62 hai tha mürd kakva jastüfia mūra ka tcadá mahasamümdrá ' О you bird kakva, celestial bird, if beside the great sea’, both would suit for kakua the meaning ‘duck’, Two connexions are possible, 1. kakva ‘duck’ as the ' quacking' bird, to be associated with O.Ind. koka- ' duck, cakravaka-', or 2. Zor.P. kpg *kafig, N.Pers. kabg, Greek коккерт, Eastern Pers. kauk ' partridge’. Tokhara A has kok- lw from O.Ind. &oka-. For Waxi kik, kīk ' wild dog’, cf. O.Ind. koka- ‘wolf’.
2756:teada ‘vicinity, surroundings’, K 29:194 Sika vara naista südana tcada vivsájai ‘опе there sat Sudhana beside the pool’, К. 38132-3 basi nestä т küsdi vari tcáda vivsümje ‘in the grove he sat there beside the pool of the palace’; ш 69:95 murrdāņmdä disa vi tcadà ‘еу ranged over the district around '; п 74:62 hai tha mürd kakva jastiña mūra ka tcadà māhāsamāmdrä 'O you bird kakva (ducki), celestial bird if beside the great sea’ (BS mahasamudra-). From base kar- ‘to surround’, karā ‘circle’, adjective kara- ‘surrounding’, to *čartu-, Av. caratu-.
6183:mura- 'speech, word’, п 114-119 рӣїса-т va dümvam jsa hau:rá murä şte 'then for them from the Düm people there is report, word’; п go*68 и haurüm mura jsa ije va prramiüi pudümdd ‘апі with reports, words, they offered promises to one another’; 11 75:50 haurä таи mam ni iniryau ' they were not making to me report, word’, ш 123:62 haura mümra padimai ‘һе makes speeches, words’, BS alápam karayati; V 314, 3-424 hürau mūrau йа. The word haura- is in п 113:94. hauri ām salā ni bijese ‘ће did not utter word, or speech’ with sala ‘word’ (BS samlàüpa-) in place of mura-. From base mau-:inu- tto make sounds’, thence mu-ar-:mur- (form like phur-, phüde 'foods', and Oss. D. K'udrun k'uärt, I. &'üryn, k'ürd 'to push"). Without -r-, see JS 26v1 mi (or оатӣ) ‘he praised’, to IE Pok. тӣ- ‘to utter murmured sounds’, Hittite mugami 'to utter prayers of lamentation’, OHG māwen о cry out’ (note similarly vās-, s.v. basa-); Oss. D. murd ‘bell’; тоо ‘jaw’, І. muk'u, ТЕ a form men- existed beside men- (as O.Ind. bhanati beside Greek qà-, above bütd "ће spoke’; BS aha), then "Greek" poŭoa, Doric рса, Aiolic potoa ‘goddess of song and poetry’ belongs here. For 'speak' and 'praise', note O.Pers. gaub-, N.Pers göy- “to speak’ beside Sogd. Bud. ywf- tto praise’, Armen. lw govem. For ysürra- 'golden' < *датпта- see below, Ау. zaranu- 'golden', Zor.P., N.Pers. dàl- in dāl-man 'eagle', Av. zaranu-mainis. See below mīvāra-, and аузтйтй- ‘sound’.
6185:za 'eggs of birds living on dry land’; v 246, 1321 davau murām, = K 97:199 mürau davau ‘of birds (and) wild beasts’, BS mrga-paksinam; JS 29r4 mura data ‘birds, wild beasts', K бо, 3774 mura data (not bura); п 75:62 hai tha mūrä kakva jastūña mūra (read mūra ka), see s.v. ürrá ‘Варз’; K. 4031-2 mura astá kūnāla пата ' there is a bird called kunala-' (= K 43:149); Manj. 286-7 mvarà pve avasa vira ' the birds’ footstep in the sky’ (BS a&aía-), the cliché, пирата simile, Pali Dhammapada g2 йЁйзе va sakuntünam padam; BS  Udàünavarga 29:26 йЁйїаїйа fakuntünüm padam (28 gatis), Tib. nam-mkhah-la ni bya rjes báin. With -ka-, Z 208 murka date ' birds, beasts’, ur 108-6 müraka. From *mrga- 'wild creature’, Av. maraya-, Zor.P. тшш *тиго, N.Pers. тигу, M.Parth.T. mwrg, М.Регѕ.Т. mwrw ‘bird’, тоги", mwrw' ‘omen’; Sogd. Bud., Man. тту; plur. Bud., mry'st, Chorasmian '"my* *amya ‘bird’, Oss. DI. mary, márytá 'bird', D. mályà; D. málg, málgità, Y. málg, málgytá ‘peacock’, D. borämälyä, Y. burdmály, bulámáry ‘nightingale’; Pasto marya, plur. mārya, fem. marya, Armen. lw marg in sira-marg ‘peacock’, Georg. p'aría-mang-i 'peacock', Zor.P. plimwlu *fraš-muru, M.Pers.T. priymwrw *frašē- тиги ‘peacock’, see Zoroastrian Problems, ed. 2, vri-xvi for frafa- 'conspicuous, wonderful'; for the compound frafagar Parsi-Persian sühir ‘conspicuous’, and s.v. aurrta "admired! above; Armen. lw mul in fir-mul 'ostrich!, N.Pers. Sutur-mury. ТЕ Pok. 734 merg*- 'dark', perhaps O.Ind. mygd- 'bird, wild beast’ (RV ‘bird’; of elephant). See s.v. aurria and parssa-. mürá- т. ‘name of a coin’, and 2. ' jewel', plural тїїгє, later mura, muri, murai, corresponding to the Chinese small copper coin ts'ien (К. 1072:5), frequent in the documents . (see КТ ту бо). п 9:155 #201 mūra ara ‘copper coin in value’, Z 22:248 ffatimgye mire ' coins of copper! (see s.v. sāva-); acc. sing. Z 22:251 kye ífau mūro hatüro kuru yüdandá “һо made formerly one false coin’; oblique Z az250 {уе mvire; V 276, 8b6 mürau tta himya 8000; adjective mürinaa-, Z 22:248 kuvā mürina ' heaps of coins’ (in the context) or ' heaps of jewels’, For müra- ‘jewel or precious thing’, SuvO. 5314 müryau ‘with jewels’, BS mapi-; п 8o'16 rang mürd ' precious stones (BS ratna-) and (-Z) jewels’; rz 128:1-2 baisi ysamthi vastam Ha hiya dastem тапа camdāvaña тайгі тайата himamde ‘in every birth throughout for them (-am) may their (-em) hands be like precious stones, the cintü-mani jewels’, with dyadic use of mürz- to translate the mani- of the cinta- mapi- "wishing jewel';:1v 23:17 (verse 28) sam khu Ji camdāvañä тӯтӣ 'like the cintü-mani jewel’; ш 128, 8-9 узт djsq тарта mura mirühe ' gold, silver, precious stones, jewels, pearls’; Manj. 209-10 khu cadávasia тата ‘like the czntümani jewel’ (da, not гуй); v 303, 224 camdātañā тїї. Adjective, Z 22:139 mürhngye...stune ‘jewelled pillars’, parallel BS sapta-ratnamayam yüpam ‘pillar of seven jewels (precious stones)’. Compound, 1 63 F2 mira- haurā hvamdi ' men who pay in miürü-coins', This müra- is from mudrä- ‘seal’, Zor.P. mwdl, mwhlk #тидг, *muhrak, N.Pers. muhr, muhrah, M.Pers.T. тшт ‘seal’, For O.Ind. mudrā, see H. Junker, Indogermanische For- . schungen 35, 1915, 273-88; H. Lüders, SBAW 1919, 734—766. With -ka-, müraka- ‘seal’ is used to render
6733:rya ‘youths’, v 52:2 и halai rya hvamdä siha u ysüda hvamdi “апа half-grown men, children and old тел’; ibid. 7 u hàlai rya hvamdá 5 mūra hame 2000 ‘and half-grown men 5 mürü-coins amounts to 2000'. To base rai- in *raita-, Armen. lw erita-sard ' young man’, Zor.P. r&tak, N.Pers. raidak ' youth, beardless youth’; Sarikoli reydz ‘he-goat ‘3—4 years old (*rai-éa-)'; see also hūrī ‘page at court' from *hu-raita-. IE Pok. 330 rei-, O.Ind. rindti, rina-, rīti- ‘stream’, rétas- 'pouring, stream’, Greek óptvoo ‘move’, ёрі ‘strife’, Lat. orior, origo, riuus ‘stream’, O.Engl. rid ‘stream’, О.Захоп гїї, Lit. rýtas 'morning', O.Slav. iz-rojt ' pouring out’, réka ‘river’.
6986:vāra- 'share, portion’, IV 1:8 yaudarä hiye ойга mūri dor уй dvi-sa pamjsäsi ' Yaudara's share mūrā-coins 2250'; II 35, 845 sau visnadatti һуа таға ‘share of sau Visnudatta' ; II 38, 1373 Aharamurrai va vàri 'shares of Kharamurrai'; v 207 t7'1 thaunai vüra ksa müre 'share of silk-cloth, six mürü-coins'; v 208-5 ойга ksa и nau cha 'share six and nine feet'; v 12, 4:3 phemdūkä thaunakd haudä 1 vürai 100[[] ' Pherndüks gave silk-cloth 1 portion, тоо mūra- coins)’; v 16:22 váraji (adjective, or ойға ji ( >). From var- ' to distribute’, keeping older v- (or vvar- < vi-var-?), Sogd. Bud. yw'r (separated' =) 'but' (*vivara-), Oss. D. iñarun, jurst, І. ñaryn, ñórst, a-jüaryn, ba-juárst ' to distri- bute’, D. idarcá, I. üárst ‘distribution’ (*or-var-), Yidya wür-am preterite шйї-әт, wet-sm ‘о separate’, wòdyo 'separate', participle to wär-.
7034:Tib. de-b3in-gsegs-pa ma gtogs-par gáan-gyis (‘aparı from tathagata!); Bed 52v2 vinau hauva yinime ' 1 act without power', BS abalam karamünmah; Sid. 1 bis r4 vinau mātsarä ' without jealousy! (= BS matsarya-); ut 84551 vinau gachükam ' without inner parts’, = п 88:133 vina gichükaüm; Z 4:102 vinau parikalpá jsa kire mūra canda- vand упай “ће cintā-mani jewel effects works without parikalpa-imagination'; Z 2:81 vino mamá nisti nä tründ (BS trüpa-) ‘apart from me there is for them no refuge'. From vi-na- with -au as in anau ‘without’, Greek vev, to vina ‘without’,
7203:small vessel'; of coins, П g^155 u ca га haiysdu faci mūra üra haira ya 'and whar things were present worth a copper coin’ (translation SDTV 28), Z 22248 Аита mürinà daindä sšāiīmje maje müre 'they see heaps of эпйтй-з (precious stones, = DS ratna-, or possibly müra- coins) our copper zrd-coins'. From syüva- 'dark in colour’, Av. sydva-, M.Parth.T. sy'w, sy'wg, Armen. bw seau, gen. seuay, Sogd. Bud. fw, Oss. DI. sau, Zor.P. syüh, N.Pers. siyah, Sangle&i fui, Waxi Ни, fü, #0, xui, Khowar lw ša; also Oss. D. sajnág st'alu, . sau st'alf ! dark star', and *зрагК'. IE Pok. 540-1 Aei-, ki-eu- ‘dark’, O.Ind. syavd-, iyamd-, Lit. £yvas ' whitish’, iémas ‘blue’. See also s.v. sarāti ' plant пате"; also below £air-chá.
7664:siyā- 'goose', K 5, r4avr tramu kho siyanu rre bárühátá ' as the king of geese (—BS raja-hamsa-) soars up’, Tib. man-pahi rgyal-po b3in-du bar-snan-la hphags-te, Chinese Ten uang (K. 24374; 1298-1) ' king of wild geese’, translation E. Lamotte 244: ‘je m'élevais dans les airs pareil au roi des cygnes (rdja-hamsa-)'; Sid. туут sya pa ‘flesh of goose’, BS lamsa-, Tib. bya sav-pahi ta; plural, Z 7'45 siye, sing. Z 17:44 sya; Z 17:20 sye; Z 22:135 sye varata tcirau üce ' geese there, ducks, water-birds', ш 96:6 kakye mūra sye mura 'partridges, geese’; gen. plur. JS 26r2 syānä rre ‘king of geese’, From зуй, with Sogd. Bud. syčh (*siyaca-) ‘duck’ with different suffix, like Sogd. Виа. Ay&'kh 'worm' beside Ваібёт kitak ‘small insect’, to Av. ka&ta-, O.Ind. &ifa- 'worm' (secondary -t- < -t-). To base sai-:sí- 'of grey colour’ Sogd. Bud. 'ps'ynk' ‘mottled’, Syriac fsyng-' "king of birds’ with Armen. Iw sira-marg (marg North Iranian < mrpa-, as Oss, mary) ‘peacock’. See s.v. jarüti, IE Pok. s4o Ёеѓ- of white, blue, grey, brown, dark’.
7899:hamgga- ‘total’, v 174a1 tti buri và müra патра phemüsta gūñä haudä ‘these so many müra-coins in total, he gave sacks (giid, Kroraina goni) for (taking to) Pherna'; тп 'the bodhisattva must not go there; altogether he must not remain calmly’ (yi ‘by him’ with future participle); H 6524-3 tti mūri h(v)ada hamgi pusa hauda ‘these mürd-coins altogether do you at once give for the men’; п 66, баз [[[ji mūra hamgä риза v 204, sar [[[müri hamgi darmadattá vara uja]ll ' the total müra-coins, to Dharma- Чаба and. . .'; Z 4:43 aysmü ni pide gyadina väpāka (BS jada-, vipüka-) nā hamggá vicitrá ‘their mind is filled with ignorance; their ripening is altogether various'.
8541:háürau ‘with statements’, v 314, 324 hürau mürau jsa ' with statements, reports! (uncertain syllables), see Лаиға- ‘talk’ and mūra- ‘бајк.
```


## [2026-09-07T17:39:45.961Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD 'seal' ===\"\ngrep -n -i \"seal\\b\" SOD.txt | head -20\necho \"=== SOD mwxr / mwdr ===\"\ngrep -n \"mwxr\\|mwðr\\|mwδr\\|mwrt\\|muxr\" SOD.txt | head -20\necho \"=== SOD entry 5523 context ===\"\nsed -n '44635,44660p' SOD.txt",
 "description": "Gharib Sogdian seal"
}
```


### [2026-09-07T17:39:46.040Z] TOOL RESULT

```
=== SOD 'seal' ===
44668:seal  of  letter 
45268:seal 
72072:(to)seal 
72081:seal 
72475:(to)burn,  (to)seal 
93375:seal  5610, 9485 
93384:(fo)seal    9484,  9547 
93388:seal  of  letter    5523 
=== SOD mwxr / mwdr ===
11630:640  'Spz'mwrty  J—f  J1  •*>• 
11631:(o)8paza-murtc   =»8Pz'mwrty,  ,t8Pz>mwrlk 
19532:1810  >tSpz>mwrtk   B  J^f  $<»s 
19533:(3)5pza-murte   ^^pz'mwrty 
29205:3276  csn'mwrtk   B  JLx  jl  *>s 
30881:3525  Spz'mwrty    B  J^f  ji  ^ 
30882:5paza~murtc   =»Spz-,  'SPz'mwrty 
38175:^mwrt'jw'ndyy,  jwndyy/h 
43887:mwrtk(y) 
44135:mo/urt   ©pt.  st.  ^myr-,  mrt't  rwc,  mwrt- 
44174:martat-roc   ^mwrt't  rwc,  'mrtch,  mrt- 
44726:5534  mwrt-   B,  M,  C 
44731:5535  mwrt*  M 
44736:5536  mwrt'jw'ndyy   M 
44737:murta-zwande   (mwrt'jwndy)  ^mwrt'zw'nty, 
44740:mwrtk  (y) 
44749:mwrt^zw^ntyk^k,  jw'ndyCy) 
44753:mwrtyjwndyy  pryy,  Sogdica.  52.7,  53 
44755:5537  mwrt'jwndy  =>  mwrt'jw'ndyy 
44757:5538  mwrt'k  S(MD)  =*  mwrtk,  mwrty 
=== SOD entry 5523 context ===
BSTii  851.6,  843.41,  50,  850.1,  872.4;  C2  gloss. 
p215 

5521  mwyztw   M 
muy-zatu   ©*magu-zati 
magian  killing,  magophonia 
Hen.  Magi.  138.27,  135f 

5522  mwhbt1  =»  mwypt(w) 

5523  mwhrdyb   M  *A>j$* 
muhr-5ip  ©*mwdr\  Parth.  ©ob.  -yy 


l^jPXfi 


jLi>ta  lijlJLfi 


^f 


^m
```


## [2026-09-07T17:39:53.454Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^5610\\|^9485\\|^9484\\|^9547\" SOD.txt\necho \"---\"\nfor n in 5610 9485 9484 9547; do echo \"### $n\"; grep -n -A6 \"^$n  \" SOD.txt | head -12; done\necho \"=== mwhrg ===\"\ngrep -n \"mwhrg\\|mwxrk\\|mwhrk\" SOD.txt SOD_pages.txt | head",
 "description": "Gharib seal entries"
}
```


### [2026-09-07T17:39:55.183Z] TOOL RESULT

```
45266:5610  my6r(y)  S 
72070:9484  t*p-   C,  M,  S  ^JfJ*  <^->-**  l&£  j** 
72078:9485  tyk(h)  S  J> 
72472:9547tpt-BfS  ^J^id^jjr 
---
### 5610
45266:5610  my6r(y)  S 
45267-mi5r? 
45268-seal 
45269-
45270-MDii  p62,  7;MDiii  pl23 
45271-
45272-561 1  my5ry  ywt*k   B         ^j±>*k  0uf  < S y  *  [j&**  *lf 
### 9485
72078:9485  tyk(h)  S  J> 
72079-tape   (t>py(y))  ©ace.  -w 
72080-
72081-seal 
72082-
72083-BSTii  880.12,  13:  C2,  77R13,  26R21,  55R23  p62; 
72084-
### 9484
72070:9484  t*p-   C,  M,  S  ^JfJ*  <^->-**  l&£  j** 
72071-tap  ©ftap-,  *tapaya-  ©pt.  tfit  =»tpt- 
72072-(to)seal 
72073-
72074-BSTii:  C2,  77R12;  Frag.  Len.  61.3;  Hen.  Tales. 
72075-47827;  MDii  A- 16.9;  perf.  typdyr,  BSTi  276,  typ 
72076-xypOpr  clyb;  Weber.  IF  80,  1975,  90;  AVS  106 
### 9547
=== mwhrg ===
```


## [2026-09-07T17:40:04.841Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6185,6190p' ISS_alt_DKS.txt | cut -c1-6000 | tail -c 3000",
 "description": "DKS mura entry continuation"
}
```


### [2026-09-07T17:40:04.893Z] TOOL RESULT

```
byahi ša; Z 22-117 bussanei hwassaká rrvittà kho ju ggadaya pádà murāsā ' the scented herb grows, like the colour on the neck of the peacock’. From mura- < *müra- (as dura- 'far* from düra-), with suffix of fauna, -àsa-, as rrüoasa- ‘jackal’, Oss, D. robas, I. rubas, ruvas ох’, O.Ind. lopasa-; Greek &Аоәтг&; Av. kahrkása- 'eagle', Zor.P. harkas, Sogd. Bud. cris, Oss. DI. cárgás (from kark- ‘to strike', see kalj-). To Pašto mór, myawr, but other Iranian M.Pers.T. priymtorw, Zor.P. Jrasiurv, Georgian lw p'arša-mang-i ‘wonderful bird’, see s.v. mura- іга’. This name murāsa- may contain as first component a colour name of 'brown, purple, red’, Oss. D. mora, I. morä ‘brown’, Georgian lw mura ' dark brown colour’, mura c'xeni ‘brown horse’, muri ' (brown) rust’; Тарих (from Alanian) mora ' brown! (and muorá); Hittite marruga- ' red, muri ' (red?) grapes’, to IE Pok. qor, Greek paupós, kucupós ‘dark’, O.Norse meyrr ‘decayed’, Slav. Russ. smuryj, тигу] ' dark gray’. Then comparison with O.Ind. mayüra- in RV 3:451 hdribhir yühl maytira-romabhih ' come (Indra) with the red, brown- haired (horses)'; and RV 8:r-25 hdri maytira-fepya siti- prsthá ‘the two red brown-tailed white-backed horses’ (of Indra); and as an epithet of birds, RV 1-191°14 mayfiryah ' peahens!, later mayüra- ‘peacock’, suggest a secondary mayür- «*myür- from the colour-name *müra-, Khotan Saka mura- (in murasa-). For intruse -y-, see BSOAS зо, 1957, 58-9. See also murau.
murau 'plant пате", Sid. 1814, BS maluka-, Tib. maluka; II 90187 huska murau ‘dry mürau', BS müluka-, for mülüka- 'ocimum sanctum’ (see Memorial. . ..Menasce, 372 'ocimum basilicum', which is white with purple tinge). The name murau is then from the colour name mura- “dark, purple, red, brown’ with suffix -au «-üva-, as niro, nīrau ‘cassia’ from mira- ‘blue’, See cognates s.v. murāsa-. The ocimum. sanctum is the BS tulasi.
murka 'birds', Z 20:8 murka date ' birds, beasts’, see s.v. mura-.
müla- “та? 1111416 padauysa mula mulá salya ‘first the Rat, in the Rat year’ (the first year of the animal cycle) (see В8ОА5 8, 1937, 928-30); ш 13:173 //[pasà mula ' the evening, the rat period’ o£ the day in the Chinese system то p.m.; v 62:9 mīla Байа midi ‘іп the presidency of the Rat (year) he dies! (with ibid. 12 pásd salya ‘іп the Hog year’, for büy-:büsta- ‘lead’, see HI r3'1 verso salya- baya ' year-presidents"). From mii- with suffix -/а-, hence *mūžš-la-> mūla- or тша-. To Ау. тїї (only тїй pairika ће female demoness Mu$', glossed by Zor.P. пірат? (see Gr. Bund. (TD2) 188-4 mis parīk), glossed by Parsi-Sanskrit zü-nmmi rükgast; Zor.P., N.Pers. тӣї ‘mouse, rat', Sogd. Bud. mws, Yayn. müs, Pašto зпа$аЁ. ‘mouse’, maa ‘габ, Balāčīi mušk, Oss. D. mist (-i- «--), І. myst, Kurd. mišk. To IE Pok. 752-3 müs-,
```


## [2026-09-07T17:40:11.544Z] TOOL CALL #30: Bash

```json
{
 "command": "ls tools/ && python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1)[:2500])\n\"",
 "description": "MON and BQT ref details"
}
```


### [2026-09-07T17:40:12.827Z] TOOL RESULT

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
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)",
  "/home/sfmqrb/git/rishe/data/
```


## [2026-09-07T17:40:23.539Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"موکه\" incoming/BQT/BQT_v4_pages.txt | head -20\necho \"=== context line 5440-5460 ===\"\nsed -n '5440,5460p' incoming/BQT/BQT_v4_pages.txt",
 "description": "Borhan موکه entry"
}
```


### [2026-09-07T17:40:23.597Z] TOOL RESULT

```
5446:۴ - « موکه . بواو معروف » در برهان نیش عقرب و امتال آن لیکن در کتب معتبره
5448:اللفات بنقل « فرهنگه نظام ج وس ما ». 3 موکه » میش بود .»۸« لغت قری‌س ۳۰۳ > وشاهدی
=== context line 5440-5460 ===
س ش کت

عمع (هم.) ۳ - ر4 : مغان +

۴ - « موفیون نوعی از سموم قربب به بیش است » « تحفةٌ حکیم موّمن >.

۴ - « موکه . بواو معروف » در برهان نیش عقرب و امتال آن لیکن در کتب معتبره
بعمنی « میش » است یمیم که جانوری‌است معروف » درین صورت تحربف درمعنی کرده. > سراج
اللفات بنقل « فرهنگه نظام ج وس ما ». 3 موکه » میش بود .»۸« لغت قری‌س ۳۰۳ > وشاهدی
از عجدی آورده که درست لمی‌نماید - 8 - عربی است بروزن مجلی (بکسرسوم) بمعنی
کروه سواره . رك : شرح قاموی . ۹ - جمع جوکبی » منسوب به « موکب » (هم.)

۷ - اشتینگای کوید : موکده مصحف‌کلمةٌ عربی « موکدهء > است .

۸ -رك : مولی . ‎«۸-٩‏ مول » درنگه‌باشد . گوبند ممول یعنی درنگه مکن.»
۶ لغت فری سس ۳۱۵ رك : مولیدن . *- رك : مولیدن .

۱- طبری ۳301 ( زسل زا [ حرامزاده ] ) « واژه‌نامه ۰۷۳۷ کیلکی نیز 22۵1
( حرامزاده ). ۴ ر4 : محیطالمحیط » اقرب‌الموارد .

۴ از : مول ۱ ( واسطه )۳ مول (قس : سراسر , دمادم »کشاکش ).
```


## [2026-09-07T17:40:37.626Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"نیش عقرب\" incoming/BQT/BQT_v4_pages.txt | head\necho \"=== search موک with pdf page tags ===\"\nawk '/\\[pdf page/{p=$0} /موکه|نیش عقرب/{print NR\": \"p\" :: \"$0}' incoming/BQT/BQT_v4_pages.txt | head",
 "description": "Find Borhan mukeh headword"
}
```


## [2026-09-07T17:40:37.979Z] TOOL CALL #33: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2055 --image 2>&1 | tail -40",
 "description": "Fetch Borhan page 2055"
}
```


### [2026-09-07T17:40:38.858Z] TOOL RESULT

```
5434:تیش‌راکوبند خواء نیش عقرب باشد وخواه نیش | وسرمایه را .
5446:۴ - « موکه . بواو معروف » در برهان نیش عقرب و امتال آن لیکن در کتب معتبره
=== search موک with pdf page tags ===
5434: [pdf page 137] :: تیش‌راکوبند خواء نیش عقرب باشد وخواه نیش | وسرمایه را .
5446: [pdf page 137] :: ۴ - « موکه . بواو معروف » در برهان نیش عقرب و امتال آن لیکن در کتب معتبره
5448: [pdf page 137] :: اللفات بنقل « فرهنگه نظام ج وس ما ». 3 موکه » میش بود .»۸« لغت قری‌س ۳۰۳ > وشاهدی
```


### [2026-09-07T17:40:45.264Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2055.png
REF: BQT:2055  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 138  OCR-lang: fas

خومو << مومیاگی
وتأخیروتأتی کردن درکارها باشد . کهآ ترا حرمل عربی گویند وخارسی صندل دانه
مولنجه - بختح ناك و جیم بر وزن | خوانند . بول وحیض را براند - وبهندی ترب‌را
سوزاده , شیشه راگویند وآن کرمی است که:دور | کوبند و با طعام خورند.؟ - وزن معشوقه‌دار را
اببار غله افتد وتمام‌را ضایم کند . نی زکقته‌ان ۴ - ودرنگه وتأخیر۴ - ونازوغمزه
مولو <- بنم اول‌ولام وسکون ثانی‌وواوء کننده را هم میگویند ی 0
شاخ آهوبی باشد که قلندران وجو کیان هندوستان مو لیدن * « بروزن خوریدن » بممنی
نوازند ؛ ویحی گویند نیی باشد که کشیغان ور | خزبدن ولغفزیدن - وبا زکردیدن وبا زکردالیدن
کلیا نوازند 9 ؛ وبعضی دیگر کوبند مولوزنگی - و دیر ماندن و درنگك کردن و تأخیر نمودن
و حلقةٌ چندی است از آهن که زاهدان ترسا ور | باشدگ#*
درون دیر نوازند و حلقه‌های آهن را جنبانند - مومول(۱) - بنم هردو میم و سکون
و ناقوس را لی زگفته‌اند . هردو واو ولام درآخر: نام علتی است که درچشم
مولی * با اول بثانی رسیده وثالك | بیدا میشود .**
بتختانی کشیده , بلغت یونانی دوای باشد سفید موهیا نی ۷ - با میم بروزن روستاتی,
69 چش : مومو (0)
۹ - روم ناقوی بوسم زین تحکم شوم زدار بندم زین تمدا ...
هرا بینند اندر کنج غاری شده مولو زن وپوشیده چوخا.
« خاقانی شروانی ص ۲۲ >.
۴ - « مولی » بهندی فجل است > « تحفةٌ حکیم موّمن > .
۳ - از : مول (ه.م.) ی (سبت) . ۴ - از : مول (و.م.) مد یدن ( پسوند
مصدری ) :
۵- بمولیم ( تمولیم . فرهنگه نظام) تا تزد خییروشوم بدرگاه او لشکری نو شویم ."
فردوسی طوسی 2 لغت فرس ص ۳۱۵ :؛.
‎-۹٩‏ تیرتو مفتاح شد درکار فتح قلمه‌ها تدرتو مومول شد در دیده‌های دیده بان .
عجدی مروزی « لغت فرس ص۳۳۲ >.
۷ - مومیائی » شکل فارسی‌کلمه بونانی 120121218 است ( فولرس ]1 ۰ ۱۲۳۱ ؛ دزی
‎)٩۳۰ . 1‏ ۳ 0۳۵6 (فر) و نام مومیا مشتق از «موم» (ه.م.) فارسی است « عقار ۳4 ف >.
در عرهی « مومیا » بمعنی داروی حنوط و لیز اجاد حنوط شده کار رود ( رك : اقرب‌الموارده
محیط المحیط ) و * مومیائی خوالمومية القبورية » « عقار ۲۳4 > مصربان قدیم در تحنیط اجاد
مردگان مهارت تام داشتند و طربقهٌ حلوط کردن این بود که نت نعش میت را شکافته امعاءه
بقیه در حاشيهٌ صفحهٌ ۷*۵۹
۲ موم - پم اول ۰ کردی 12812 ( شمع ) « ژاباص 2*۹ * » طبری 1211 (موم)
« واژه نامه ۷۶۹ » کیلکی 12017 (موم) در عربی نیز موم : « موم » خوالشمم‌الاسفر > « عقار
4 موم نام فارسی 6176 (موم) و 616786 ( شمع مومی ) [فر] است « عقار ۲44 اف » ؛
مادهٌ نرم ی که با عل مخلوط است و بوسيلةٌ تصفیه‌آنرا از عل جداکنند .:
2 مومیا - رك : مومیائی .
```


## [2026-09-07T17:40:56.305Z] TOOL CALL #34: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:2062 --image 2>&1 | tail -45",
 "description": "Borhan page 2062"
}
```


### [2026-09-07T17:41:03.226Z] TOOL RESULT

```
مهرا ۱ هن
وتدییر مور ومصالحی که درماه مه رکه ماه هفتم و محبت لیزهست - و مردارا هم میگوبند که
ازسال شصی وروز مهر که شانزدهم هرماه باشد | در مقابل زیستن است ۴ - و نام کیاهی باشد که
بدومتملق‌است. وحساب وشمارخلق‌ازئواب وعقاب | آبرا بفارسی مردم گیا و بعربی بمروج الستم ۴
بست اوست - وبکی ازنامهای آفتاب عالمتاب | خوانند ۴ - وسنگه سرخ را نی زکوبند - و نام
هم‌هت - همچنین نام ماه هفتم باشد از سال که | آتشکده‌ای هم‌هت 9 - و قبةٌ زربن ی که برسر
آن بودن آفتاب است در برج میزان - ونام روز | چتروعلم فصب‌کنند - ونام قسبه‌ایست درهندوستان
شاتزدهم از هرماه شصی » و ینابر قاعدهٌ کلی که | - ولام مردی که برزنی ماه نام عاشق بوده وقصةٌ
میان فان یمتی آتش‌پرستان متعارف‌است که‌چون ۲ ایشان مشپور است - وبفتح اول» درعربی بمعنی
نام ماه وروز موافق آید آبروز را عید‌کنند این کابین است و آن نقد و جنسی باش د که در وقت
روز را ازین ماه بفات بز رکه و مبارك دانند عقد (۱) نکاح مقررکنند ‎٩‏ .

وجشن‌سازند وعید کنندویمهر گان‌موسوم‌دارند۱ . مهر! - بنم اول وفتح ثانی ورای مشدد
ليك است درین روز نام بر کودك نهادن و کودك | بالف کشیده » تيك پخته شده و مضمحل گردیده
را ازشیر با زکردن - وبمعنی رحم وشفقت ومهر | راکوبند ۷ - و بکسر اول و رای بی تشدید »

() چش :۳ و.

۱ ر4 : مهرکان . ۴ اين معنی را از فقه‌اللغهٌ عامیانه « مهرکان > ساخته‌اند .
رك : مه رکان ؛ « میر > [ درم رکه ومیر] بدین معنی‌است . ۴ - صحیح «یبروح السنم» با
حای‌حطی است . ر4: ,یروج [() ۴ - وآنرا « مهرگیاه » (ه.م.) هم کوبند .

8 - مماید متعدد در اببران باستان و ممالك دیگر بنام «مهر» برپا کرده بودند ؛ درینجا
ظ . مراد ۶ آذر برزین مهر > است که یکی ازسه آتشکده عمدء دوران ساسانی بود و محل آن
ربوند ( خراسان ) بود . رك : مزدیسناص ۲۱۵ ببعد . ورك :آذر برزین .۰

‎٩‏ - مهر ( بشم اول ) . ماسکربت -73214۳8 ( مهر , خاتم , حلقةٌ خاتم ) » پهلوی
6 .۰ ق000۳ ( حلقه ؟ ) , 1087 , 33187 ( مغر ) » ارمنی ع 6اهط 2۱ ۰
استی ۳۵217 » قس : بلوچی 20۲048 » 2۳04882 ( انگدت ) « اسشق ۰۲۱۶۶۱
کردی 11۳017 ( مهر ) ۰ ۳3007 ( مهر ) » 2012۳ ( مهر ) « ژابا ص 4۱۶-4۹ ؛ قطعهٌ
سنگه با فلز با عقیق که برآن نام کسی با نقشی وارونه کنده باشند ودرموقع لزومآن را بم رکب
یا جوهر مالند و برروی کاغذ قشار دهند , نام پا نقش برصحیفه منقوش کردد -

‏۷ - باین معنی مأٌخوذ از « مهرء » ( پم اول وفتح دوم وسوم مشدد ) عربی است» اسم
مفعول از تهرئه ( نيك پختن گوشت وجزآن ) . « منتهی‌الارب > « شرح قاموی > .
بقیه ازحاشية صفحهٌ ۲۰۹۱

‏همان اورمزد وهمان روز مهر بشوید باب خرد جان وچهر .
و منمود سعد سلمان کوید :
روز مغروماه مهر وجشن فرخ‌مه رکان مهریفزای ای نگارماه چهر مهربان!
مهربانی کن بجشن مهرکان وروز مهر مهربانی به بروزمهر وجشن‌مه رکان.
دیوان مسمود سمد ص۹۹۳ .۰
و ر4 : روز شماری بقلم نگارنده ی 4۲-4۰ ؛ ورك : مهرگان .
```


## [2026-09-07T17:41:13.543Z] TOOL CALL #35: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:2068 --image 2>&1 | tail -40",
 "description": "Borhan page 2068"
}
```


### [2026-09-07T17:41:20.015Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2068.png
REF: BQT:2068  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 151  OCR-lang: fas

مهره اهنا
مهره ۱« بنم اول و قح نالك , چند مهره در طاس افکندن * و
ممنی دارد : یکی ازآن چکش وبنك آهنگری مهره در طاس| ند اختن- بمعنی مهره
وهسکری است ؛ وباقی‌معلوم است که‌مهرة دبواد | ور جام افکندن است - و درین زمان کنایه از
و مهرهٌ پشت و معرءة (۱) کردن ومغرة (۱)کاغذ گوزبدن باشد .
5۶()) گلوبند ست سُد و غنره مات ارو ۷ 1
و مهر بند ودست بند و غیره باشد در ۹ شد.. -
و بترکی علتی است مشش را . مهره ددگردن جمع شدن
کنایه از شکتن کردن باشد .
مهرهای سیماً ی -کنابه‌ا زکواکب
وستاره‌های آسمالی‌است؛ ودر موْبدالفطلا مهرهای ۱ مهره دد - کنابه از آفتاب عالمتاب
سلیمانی نوشته بودند . س
۵ مهرة دس پا کنایه آزماه - وهر يك
سیماییست که کنایه از ستارکان باشد . .۰ نان اما اس
مهرخ جاند اد - بیمنی مار مهره مره سیمالبی + کنایه ازماء است
است که پازهباشد وعربان حجرالنیی‌خواندچ .| ادلی ۳
مهرخ خاك . کنابه از کر؛ زمین همهرة گلین - بدمنی مهرة خاك است
است - و کنایه از قالب او جد آدمی زاد هم | که کنایه ا زکرء زمین - و بدن و جند آدمی
مهره درجام افکندن «فهره ] , مهر و لاچو رد - کنایه از آسمان
۰ ۰ ست ماعتا ۰
درجام انداختن؟ «گونند که دزمان : ار کبودی
کیان رسم چنان بود که جامی ازهفت جوش بر «هره مشکین - با غین نقطه دار :
پپلوی فیلی‌می‌بته‌اند وچون پادشاه سوارمیشده» کنایه ا زکرءٌ زمین است - و دلیا و عالم را نیز
مهره‌ای نیز از هفت جوش در میان آن جام هی گویند .
انداخته‌اند واز آن صدای عظیمی‌برهیآمده وهردم مهره و حقه «کنابه اززمین‌وآسمان
خبردار شده سوار میشده‌اند ۰ : است .
مهره درششدرد بودن - کنابه مهری - بکر اول وسکون ثانی‌ونالث
از محبوس بودن و عاجز شدن باشد . بتحتابی کشیده . لوعی ازچنگه باشد وآن سازی
ز 69 چش : ههر .۰
۱ -* مهر(ه.م.). قس: پهلوی 5211۳26, 320۲2 (حلقه) » ارمنی‌ع 12210۳۳086
۰ اسشق ۱۶۶۱ ؛کردی ۲۳۹۵۲2 ( مهره پشت ) : 10۷12۳6 ( مهره ) « ژاپا ص *2۱ ۴
معرب‌آن « مپرق ؟ « ژابا ص 4*۸ >. ۲ - قطعه‌ای از سنکه یا فلز با استخوان باچوب
وجز آلها » مثل مهرة نرد ومهرة شطرنج ومهرة پشت وغیره -
۴ - بهترین جایی‌بدست بدترین‌تومی کزاو ‏ مهرء جاندارو اندر مغز ثمبان دیده‌اند.
۶ خافالی شروالی ص ۱۶۱ *.
۴ -قي: مهره در طای افکندن . ‎٩‏ - رك : بهار عجم .
```


## [2026-09-07T17:41:26.390Z] TOOL CALL #36: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-07T17:41:26.397Z] TOOL RESULT

```


```


## [2026-09-07T17:41:29.994Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%87%D8%B1",
 "prompt": "Give the Persian etymology sections for مهر, especially \"mohr\" meaning seal/stamp: what Middle Persian, Old Iranian, Sanskrit or other origin is given? Quote the etymology text."
}
```


## [2026-09-07T17:41:33.100Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A5%81%E0%A4%A6%E0%A5%8D%E0%A4%B0%E0%A4%BE",
 "prompt": "Give the Sanskrit etymology of मुद्रा (mudrā) 'seal': what origin is proposed (Iranian? Semitic? native)? Quote the etymology text and any references (Mayrhofer, Lubotsky)."
}
```


### [2026-09-07T17:41:36.838Z] TOOL RESULT

```
# Persian Etymology for مهر (Seal/Stamp Meaning)

Based on the Wiktionary content, the Persian word **مهر** (muhr, meaning "seal") has the following etymology:

## Source Languages

The term derives from **Middle Persian** _mtr'_ (muhr, "seal"), which came from **Old Persian** _𐎷𐎡𐎰𐎼_ (mi-i-θ-r /Miθraʰ/). This Old Persian form traces back to **Avestan** _𐬨𐬌𐬚𐬭𐬋_ (miθrō, "covenant, contract, oath").

## Proto-Language Origins

The Avestan term ultimately derives from **Proto-Iranian** _*miθráh_, which comes from **Proto-Indo-Iranian** _*mitra_ ("covenant, treaty, agreement, promise").

## Comparative Evidence

The article notes cognates in **Sanskrit** _मित्र_ (mitra), establishing the Indo-Iranian connection. However, the entry also suggests "a possible layer of phono-semantic matching with the Semitic root regarding business contracts and reception," indicating complex etymological interactions between language families.

The fundamental meaning across these forms centers on concepts of **covenant, contract, and binding agreement**, which semantically evolved to include the physical seal used to authenticate such contracts.
```


### [2026-09-07T17:41:38.528Z] TOOL RESULT

```
# Sanskrit Etymology of मुद्रा (mudrā)

## Proposed Origin

The word is proposed to have **Iranian origins**, possibly from Semitic languages ultimately.

## Etymology Quote

According to the Wiktionary source: "Possibly an Iranian borrowing, from Proto-Iranian *mudrā, possibly ultimately from Akkadian mušarû ('object bearing a royal inscription'), from Sumerian mu-sar, from mu ('name, fame') + sar ('to write')."

## Referenced Scholars

The "Further reading" section cites **Manfred Mayrhofer's** etymological works on Old Indo-Aryan (2001 and 1963 editions), though the specific details of his conclusions are not quoted in the provided text. Ralph Lilley Turner's comparative Indo-Aryan dictionary is also referenced but without detailed commentary on the etymology itself.
```


## [2026-09-07T17:41:45.468Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mummy",
 "prompt": "Quote the full etymology of \"mummy\" (the embalmed body) and of \"mummery\" if present. What are the intermediate forms (Medieval Latin, Arabic, Persian)?"
}
```


## [2026-09-07T17:41:46.827Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mogul",
 "prompt": "Quote the etymology of \"mogul\" — both the Mughal sense and the ski-bump sense (Scandinavian muge/mugi 'heap'?)."
}
```


### [2026-09-07T17:41:50.970Z] TOOL RESULT

```
# Etymology of "Mummy" (Embalmed Body)

**Full Etymology:**
"late 14c., _mummie_, 'medicinal substance prepared from mummy tissue,' from Medieval Latin _mumia_, which is perhaps from Greek _moumia_ or directly from Arabic _mumiyah_ 'embalmed body,' from Persian _mumiya_ 'asphalt,' from _mum_ 'wax.'"

**Intermediate Forms:**
- Persian: _mumiya_ (asphalt)
- Arabic: _mumiyah_ (embalmed body)
- Greek: _moumia_ (possible route)
- Medieval Latin: _mumia_

The sense evolved from the medieval belief that Egyptian mummies contained asphalt, which was valued medicinally. The modern meaning of "dead human body embalmed and dried after the manner of the ancient Egyptians" appears in English from the 1610s onward.

## Note on "Mummery"

The provided content does not include a separate etymology entry for "mummery," though it appears in the nearby dictionary entries list. Only the "mummy" entries are detailed in this source.
```


### [2026-09-07T17:41:51.180Z] TOOL RESULT

```
# Etymology of "Mogul"

**Mughal Sense (n.1):**
"powerful person," 1670s, from _Great Mogul_ (1580s), the common designation among Europeans for the Mongol emperor of India after the conquest of 1520s, from Persian and Arabic _mughal_, _mughul_, alteration of Mongol.

**Ski-Bump Sense (n.2):**
"elevation on a ski slope," 1961, probably from Scandinavian sources (compare dialectal Norwegian _mugje_, feminine _muga_, meaning "a heap, a mound"), or from southern German dialect _mugel_ with the same meaning.
```


## [2026-09-07T17:41:55.481Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mummery",
 "prompt": "Quote the etymology of \"mummery\" and \"mummer\". Is it related to \"mummy\" (embalmed body)?"
}
```


## [2026-09-07T17:41:56.282Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/mallemuck",
 "prompt": "Quote the etymology of \"mallemuck\": what Dutch words is it from (mal, mok)? What does mok mean and where does it come from?"
}
```


### [2026-09-07T17:41:59.866Z] TOOL RESULT

```
I cannot provide the etymology information you've requested based on the webpage content provided. The Wiktionary entry for "mallemuck" does not include an etymology section explaining its origins from Dutch words like "mal" and "mok," nor does it define what "mok" means or its linguistic source.

To find this etymological information, you would need to consult a more comprehensive dictionary or linguistic resource that includes detailed word origins.
```


### [2026-09-07T17:42:00.546Z] TOOL RESULT

```
# Etymology of "Mummery" and "Mummer"

**Mummery** (noun, 1520s): "a show or performance of mumming," derived from Old French *mommerie*. The sense shifted to mean "ridiculous ceremony or ritual" by the 1540s.

**Mummer** (noun, early 15c.): "one who performs in a mumming, actor in a dumb show," likely combining Old French *momeur* and Middle English *mommen* "to mutter, be silent."

## Relationship to "Mummy"

Based on the provided content, **there is no documented connection** between these terms and "mummy" (an embalmed body). The etymologies for mummery and mummer trace back to Old French words meaning "to mask oneself" and relate to silent performance traditions. The entry for "mummy" appears in the neighboring dictionary entries list but is not discussed as sharing a common origin with mummery.
```


## [2026-09-07T17:42:07.029Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD mallemuck ===\"\ngrep -n -i \"mallemuck\\|mallemoke\" FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt WEB*.txt 2>/dev/null | head\necho \"=== KLN mallemuck ===\"\ngrep -n -i \"mallemuck\" KLN_1966.txt KLN_1971.txt | head\necho \"=== KLN mow ===\"\ngrep -n -i \"mow,  n\\.\\|mow, n\\.\" KLN_1966.txt | head",
 "description": "Search for mallemuck and mow"
}
```


### [2026-09-07T17:42:07.119Z] TOOL RESULT

```
=== FSD mallemuck ===
WEB_vol1.txt:111849:ish, and mok, a gull ] cies of large ocean bir tross; especiaily, t written mallemock, mallemoke mal’len-dérs, 7.p/. same as malanders.
=== KLN mallemuck ===
KLN_1971.txt:143614:mallemuck, mallemock, mallemoke, n., fulmar, 
KLN_1966.txt:22680:mallemuck,  mallemock,  maUemoke,  n.,  fulmar.
=== KLN mow ===
24545:mow,  n.,  a  stack  of  hay.  —  ME.  mo  we,  mow,  fr. OE.  miiga,  muha,  ‘a  heap,  pile’,  rel.  to  ON. mugi ,  miigr,  of  s.m.,  ON.  mostr  (for  *muhstr), ‘crowd’,  Swed.  moa,  ‘to  crowd  together’,  and prob.  cogn.  with  Gk.  [xuxcav  (Hesychius),  heap  .
24548:mow,  n.,  a  grimace.  —  ME.  mouwe,  move,  fr.  OF. moe,  moue  (F.  moue)  ‘pout,  grimace  ,  fr.  Frankish *mauwa,  restored  after  the  Dutch  phrase  mouwe maken,  ‘to  pout,  make  a  wry  face’;  prob.  of imitative  origin.
```


## [2026-09-07T17:42:13.217Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '22680,22684p' KLN_1966.txt\necho \"=== WEB context ===\"\nsed -n '111845,111852p' WEB_vol1.txt",
 "description": "Klein and Webster mallemuck"
}
```


### [2026-09-07T17:42:13.297Z] TOOL RESULT

```
mallemuck,  mallemock,  maUemoke,  n.,  fulmar.
928
petrel.  —  Du.  mallemok,  compounded  of  mat, ‘foolish’,  and  mok,  ‘gull,  seamew’;  so  called  be¬ cause  it  is  easily  caught.
malleolus,  n.,  one  of  the  two  rounded  projecting bones  on  each  side  of  the  ankle  (anal.)  —  L.,  ‘a small  hammer',  dimin.  of  malleus,  ‘hammer’; first  used  in  anatomy  by  Andreas  Vesalius  (1514- 64),  it  orig.  denoted  simply  a  bony  eminence. See  malleus  and  dimin.  suff.  -ole.
Derivative:  malleol-ar,  adj. mallet,  n.,  a  hammer  with  a  heavy  wooden  head. —  ME.  maillet,  fr.  MF.  (=  F.)  maillet,  fr.  OF., lit.  ‘a  small  hammer’,  dimin.  of  mail,  fr.  L. malleus,  ‘hammer’.  See  next  word  and  -et. Derivative:  mallet,  tr.  v.
=== WEB context ===
orma, form.] h
mallēin, 7. a e g lus: used to diagnose the disease.
mal/lé-muck, 2. [D. mallemok, from mal, fool- ]
| any one of several spe- dation. as the petrel or alba- he Fulmarus glacialis: also
ish, and mok, a gull ] cies of large ocean bir tross; especiaily, t written mallemock, mallemoke mal’len-dérs, 7.p/. same as malanders.
malleolus or the malleo
aving the form of a hammer. culture of the glanders baccil- of malic acid.
malenic acid; a colorless, crystalline, dibasic acid, C:-H:04, derived from malic acid by oxi-
```


## [2026-09-07T17:42:23.852Z] TOOL CALL #45: Bash

```json
{
 "command": "pdftoppm -f 344 -l 344 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg344 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Render PDF page 344"
}
```


### [2026-09-07T17:42:25.457Z] TOOL RESULT

```
total 18244
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 13:42 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb     1525 Sep  7 13:41 p342_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1759 Sep  7 13:41 p342_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1703 Sep  7 13:41 p342_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108903 Sep  7 13:41 p342hi.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    60735 Sep  7 13:42 pg344.png
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


## [2026-09-07T17:42:28.473Z] TOOL CALL #46: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg344.png"
}
```


### [2026-09-07T17:42:28.811Z] TOOL RESULT

```

```


## [2026-09-07T17:42:28.808Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T17:42:43.593Z] TOOL CALL #47: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py BQT:2054 --image 2>&1 | tail -45",
 "description": "Borhan page 2054"
}
```


### [2026-09-07T17:42:51.007Z] TOOL RESULT

```
کشید. و برای بی نقطهٌ زده » غلیواج:راگوبند | از فرشته‌ای چند است که در شب معراج همراه
که زغن است .. بیغمبر صلوات‌انة علیه وآله بودند .
موع ۱ - بروزن دوغ » مغ راکوبند هو کده ۷ - بر وزن موصده , بمعنی
که آش پرست باشد . مطلق است که در مقابل مضاف باشد .
موغان - بر وزن سوهان » جمع موغ مول - جنم اول ونانی مجپول بر وزن
اس ت که آتش پرستان باشند - ونام شهرست در غول » معشوق زن راگوبند ۸ - و بممنی بودن
آنربایجان . کوبند دشتی وصحرائی‌دارد درنهایت و درنگه و تأخیر کردن در کارها و باز ایستادن
صفا و نزهت وخرمی ۴ ؛ و باین معنی بجای باشد ‎٩‏ - وأمی باین معانی هم هست پعنی باش
غین نقطه‌دار قاف هم بنظرآمده است. ویجایی(۱) مرو و مول (۲) مول پعتی‌پاش باش*۱
. هو‌قیون ۴ - با اول بنانی‌رسید. وف | - وبمعنی‌با زگشت هم‌آمده اس که کنایه ازتوبه
۰ باشد - وناز و غمرزه ران : :
فا و تحتای بواوکهیده وینون زده ۰ نومی‌انزد ] حرام زاده همست ۹۱ و بزبان هدی قیمت
باغد وژورآن ماند زور بیش‌است » وعلاج آنرا حرام زاده هم - و بر ۳ +
مانند علاح پیش پاید کرد . وبهای هرچیز باشد - وبزبان عربی عنکبوت را
2 اد 9 1 خوانند (۳) - وبفتح اول هم درعی‌بی مال‌واسباب
مق اس ول‌بروزن غوك4 » مطلق وسامان راگو, ۴۳ ودرهندی پیخ نباقات ومایه
بیش‌راکوبند خواء نیش عقرب باشد وخواء نیش | وسرمابه را .
جزهای دی مولامول ۱۴- مانند. لت پیش با
مو کب ۰ بفتح ول بروزن م رکب. زبادتی‌الف ومول دیگر, بمعنی تأخهر ازپی‌تأخیر
بمعمنی لشکر وسپاه باشد . ودرنگه از پی درنگه باشد .
مو کبیان ۱ سحر- بکریون, کنایه مو لش ۱۴ - بروزن کوش . درنگه
: (۱) چش : بجای . () چش : صول (۱) (۳) چش : گوبند .
و0 سح

۱ دمغ (هم.) ۴ - رك : مغان .

۴ - ۶ موفیون نوعی از سموم قربب به بیش است > « تحفةٌ حکیم موْمن >.

۴ - « موککه . بواو معروف » در برهان نیش عقرب و امثال آن لیکن در کتب معتبره
بمعنی ۸ میش ؟ است بمیم که جانوری‌است معروف » درین صورت تحربف درمعنی کرده. > سراج
اللغات بنقل « فرهنگه نظام ج وس ما ». ۶ موکه » میش بود .> « لغت فری‌س ۳۰۳ > وشاهدی
از صجدی آورد ه که درست لمی‌نماید .8 - عریی است بروزن مجلی (بکسرسوم) بمعنی
کروه سواره . رك : شرح قاموی . ‎٩‏ - جمع موکبی » متوب به « موکب » (ه.م.)

۷ - اشتینگای کوید : موکده مصحف‌کلمهٌ عربی « موکده > است .

۸ -رك : مولی . ‎٩‏ - ۸« مول » درنگه‌باشد . گوبند ممول یعنی درنگه مکن.»
۰ لغت فری ص ۳۱۵ رك : مولیدن . 4 رك : مولیدن .
( حرامزاده (. ۱ رد : محیطالمحیط ۰ اقرب‌الموارد ۰

۴ از : مول ۱-۳ ( واسطه + مول (قس : سراسر » دمادم کعا کش (

بکار دهر پمولش کرچه بد نیت ولی تاخیر کردن از خرد لیست .
۱ آپوشکور بلخی « رودکی . نقیسی ج ۳ ۰۱۲۵۳
```


## [2026-09-07T17:43:09.378Z] TOOL CALL #48: Bash

```json
{
 "command": "timeout 900 python3 tools/ref_page.py AFM:148 --image 2>&1 | tail -40",
 "description": "Addi Shir page 148"
}
```


### [2026-09-07T17:43:10.631Z] TOOL RESULT

```
no scan of AFM covers printed page 148 (see 'scans' in refs_online.json)
```


## [2026-09-07T17:43:16.075Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 154 155 156 157 158; do echo \"=== leaf $L ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' AFM_pages.txt | head -30; done",
 "description": "Addi Shir leaves around p.148"
}
```


### [2026-09-07T17:43:17.311Z] TOOL RESULT

```
=== leaf 154 ===
هه 00 ܐܓ
أن طاف اقطار المسكونة اتتهى الى اذور 9 وأعر 43" 0.33
حل عالتفى اعلهة الشرقية منة عرش مرضع .2 لس نا به الملوكة ووضع على رأسه
تاج المرضع ܬܐܨ النفيسة وجاس على العرش امنصوب له ܶܪ | طلعث الشمس
فضر بث ܣ التابم 057 امنتلاً ذلك الوضع نورًا وضماء ٠‏ فاستبدع :3
المدظر فاستسغدوا ܛ || ܐܕܬ ا نورورًا ܥ انه يوم ܶܕ ܠܐܒ ܐܬܐ £
« شبد £ باللغة المهاوية تطلق على الشعاع أضافوها لى اسم ` كثالوا ܝܟܝܠ ٠‏
0 وروز ܐܟ فهو اليوم السادس من سهر « فروردين » الذي" ܠ ܨܢ « ܢܐܪ ¢
5 7 تسسته بنوزوذ اخاضة أن 33 0 على ضر يذ ©
استدعى اليه جيع اركان _ وخواض دادرة ساطنته د عليهم قواعءد ܓܗ - ܢ
وقوانين مستحسنة . فاستصوبوا ¥ -( ذلك 9.41 3 ويروى ايضاً
8 اعيان الفرس في الايام السنّة التى بين نوروز 3 ܣ 3 يحيبون الى
سؤل جميع الحتاجين و يطلقرن الحموسين ܣ مع ذلك يتعكفهون على !ܠ ܐܙ اث
والعشرة ܕ ومن الفارسي وروز مأخوذ السر إلى ܢܘܣܪܕܐ واضافوه الى ܐܢܠ
ذالوا مه هد » مل ان عيد الله وهو لي طقس © يان الشرقيين الأحد 0
فم الس ليم ١‏
( النرْق) اليد ( شفاء الغذيل ) ٠‏ معرب نزخ وهعناه السعد والرونق
١‏ النارَمْسْك ) ܙܘ ضغيرة مفتحة كأنها وردّة لونها الى الساض ‹1 ܠܟܕ والضترة
في ذسطها نوار لونة كذالك وطعمة نض وراتة طيية ومعناها بالفارسيّة هسك
ا زهان
( | ܕ ) اللين ܐܐܬܐ ܩܢ مريب ܝܝ هُ الكردي زم
ܨ ܟܝܢ هن اللسمون معرب نارناك واصل معناة 3 ر اللون ܀ وفتة ܘ
ܫܫ 3 0
+ ( ×« © 815 تصن ين لزه
١‏ 363 ܝ القصيد تعريب يزه والتيزق لغة فيه ومنة فعل ترك اي طعن
بالنيرك ٠‏ ومنه الاراعي. ܨ =
+ ( الشيسب) ܐܟܟ بق ن الواضح الستقيم او ما وجد 7 الطريق ܥܕ !$
=== leaf 155 ===
ل ܕܙܘ | شت
الصحاج :« والذي تراه كالطر يق من النمل نفسها ٠»‏ والنمل اذا جاء منها واحد في
39 0 ܕܟܐ ܨ ܠܐܝܐ والميّة. ܢ الواضح : معربان عن
÷ ن اي ` الأو
$ 6 نات 98 7( 3:77 ونون يقترن
391 ܕܐ لهُ بالتركية « اغسطوس كلى ܙܝ ܐܥ كل ».وان كان زهره ابيض قيل
له « اق كل » وان كان اي ` كل 0
ل داوس 03 قوي © |( الأزهري : ولا أدري
355 ام لا ܐܝܝ وهو فارسي 209 نسْرين ويقال له ;± « وان كلى ومصر
0
( ܬܐܨ ) ܘܬܒܘ ܐܝܬ ذات طعم جامض حاد ورف تكبريت الدخان وملح
57 00 في البرهان القاطع :« النشادر ضر بان معدلي 0-0
فالمعدلي. مصلل عله في 5 من جبال سمرقند وفي 55035 - | بر
دمندان في كمان اذ يخْرج من تلك المغارة جار نظير الدخان فيجمد في اطراف 0
مثل ܠ وهو نادر عزيز الوجود . والمصنوع يعمل من سواد الدخان الجتمع في ١تون‏
الام وهو نافع من < العين ومن الدمعة 3 وهو 5 نشادر بالتركة
والكردنة و ط18ط11311131 باأروسة
1 1 ܐܳܢ ܝܨ ܝ 5 واصل العنى فيه | ܐܨ ܟ
0 23 ليِمضِمَةُ ثم يبلعة٠وقالوا‏ فيه نشْوّرت الدابة من |
نشْوَارًا اي أبقت من علفها
ْ || الَمَأْ) ما يستخرح ܀ من ܐ 9 حتى تلين ومست حق ܐܝܐ‎ ١
ܕ( كان 7 0 ٠وفي الصحاح: « النّمَأْ ܬ و ܣ فارسي متا لق‎
شطره 0:6 قالوا 535 57 القرى 05 ܓ‎
0 ا اراممة الاصا 3 من ܢܫܝܦܐ اي
ܫܦ اي ܨ ܢܨ وطهر
* ܒ = مأخوذ 5 3 اي شرب
2
فوا وهو مثتق من
܀ ܟ
=== leaf 156 ===
حا ¿ © ܐ ܘܡܐ
* 5 السكران ܐ :¥97 اي سكر ومن بان (ويقال .50
وان» أي صاحب
5 بقل طيّب 3[ 1:3 وهو ايضاً ® بالتركيّة وك
بالكردة و سكع بالاراميّة و سلح» بالسريائّة الدارجة او ܝܐ بوورون
باليونانة 1161111329 بالرومسة 11111119 بالاتكايرنة وع111611 بالفرنسة و 1111176
بالكرمانية و 111@1112 بالايطا ® و اوباب لارى بالارمنمة
0ه فحّة ) وعاء المسك اي ܐܙܪ ا ٠‏ تعر يبب 0
1 + 0 لمك فان المسك جشمع حول مرعها اتات
اليد ) ¬ فيه تعريب انيور ܙ ܕܐܐ الارامي” ܫܝܦܘܪܐ ܙ البوق
ܠ .0 ܐܒܨ 2 وونة 107 ܐ ° ܒܘܩܝܢܐ
9 السراويل الموضع 0 من معرب 0
ܟ (الشكر ) الداهي الفطن تعريب كران حذف شطره نحفيفاً ٠‏ ونكران
1 01 وهو اسم نال مق ( 0057 30
ܣ اي الدهاء والفطنة لل عدذلك
الك ) ܐ :1:3 ܚܒ انك رين اي * اللحية 3
لاك
_ كن ) 9 > قلبة عل رأسة وتجمل أسفل «اغلاء 39057 43
وهو فارسي | الاصل ܨܚ( وهو تين بخ انسار وهو مر ܝ ܢܝ اي مقاوب
ومعكوس ومن 8 5 راس ܒ مقاوب الرأس
ܨ (الثلك) ش 1 ܝܐ الإعرور 3 تلك وهو الزعرود ويقربه الفرنسي
101
د10 ) 0:6410 ܐܚܠܬ متك وفسر - بالزعرور. يقال
له بالتركية آلو بالو
( انرق والنئرقة ) فسرت بالوساحة الصناة نشكا علنها لد الا 70004
فوق الرحل مأخوذة من 2 وهو ܒܐ على كل سي ء ابن ناعم لطيف
* ( مش ) نم وكذب مأخوذ من فش اي المكر وا-قديعة
=== leaf 157 ===
ܚܝܚ © ܘ | كك
11 ‫ 0[ )3 معرب وده
(3) الكتات الذي 4 فيه تعريب ثامه وبنوا.منة فملا وقالوا غقّ
3 6 الاراعى ` ܢܡܩܐ و شربه اليونالي 94 اي الناموس
جد ( العا 096 ܦ £ حجم الخردل .0 (08(8421¶÷ 0 2 93
106 ) تعريب 3( اللبز. والمب المذكور سني به لاه
ܝܣ
(التوردجة ) الضميمة وما أف من كل شىء ء 5 لورده
(التَاوق ) الطنشمة المنقؤرة التى يري فيها الماء في الدواليب 3 تاوه
00 ال لتيل اشىء مث عرس نذلاة ونان 99890
3 .
( | ܢܗ ) 6 تنشبه السحر ولست محقيقته وو( ܣ ܢ . ٠و‏ 1
الخر” راسكف ده ود 2 اأزجل اختلف اقالا ܐ وكذا في ܨܚ ܩ
النميمة والمثي بها 0 ذلك راجع الى معنى اككلمة الفارسية ܡ ܢܐܚ ومعناها 15
والمكر والسحر 6000 للدم 397 مر ةيه 1 لو رولك انل اللرن الال اذ الم
الحديدة ܨ يذ 112 8 با لسا نسكر ܚ ٠ومئها‏ 383 بالعبرائة 51
التَيِرّح ) بعنى القوي او القوة اذ يقال ريح نيرج اي عاصف فعرب عن ܕ ومعناها
القوة ٠و(‏ التَيْرج» بمنى ܘ ܐܝܐ ܐܚ فالظاهر اله مأخوذ من الارائي مش" وهو
القدوم ( راجع اضيا ل ا
79 نبات العظلم 'يصّغ به ازرق فارسلتةُ نيل وهو مشتق من نيلى و ©
بالسنسكر 3 اي ازرق ولعصيره يقال نيه بالفارسية ومنة انيلع ` ?: دخان
الغ حم يمَالج به 9 الوم وهو 2 ܨ د من ܠ ܫܝ بالماء
7 ما عليه من الزرقة و يرك الماء فيرسب النيلج اسفله كالطين ܐ (4&¬0
ويدف
܇ ‏ + من الزياحين تت في !1 الزاكدة 2 أصل
كامزر وساق أملس يعاول بجسب عق الماء فاذا ساوى سطاحة أَوْرّق وأزْهر واذا بلغ
يسقط عن رأسه ع داخله ܥ اسود ٠‏ 2 9 ܫܡ مركت دن نيل وهو الذي
ܐ
ܐ ܐ
=== leaf 158 ===
ܢܐ }ܘ ܐ ܝܝ
:3 تر
يصبغ به ومن ܨ وهو اسم »ܓ 21 فل ܗ بنيل لان الورقة | مضموغة
الحنا حين ( حيط المحبظ ) ٠‏ وقال صاحب البيغان القاطع :« النيلوفر ورد معروف يظلهر
في طلوع الشمس فوق الماء ويزهر وفي غرويها يع في 2( وقيل اله عند وقوعه
في الاء يلقي طائر ويسقظ مكانة ويقم 2 مسترياً الى ان يظهر النيساوفر فيطير
ܫܠ ܝ € ٠‏ ومئه الفرسي 7 و شر به المونالي )ܐ
(النم» ' ̈ܡ ;© لبن وورق صغار وله £
حامض > 0 وحلا وهو يؤكل ( اقرب الموارد ) فارسَّهُ نم وفشر بشجر
مع | = ار اند صغير وكير زهره نظير عنقود كأنة حسمن كنن من البنفشة
وسطه اضفر لذيذ 3 وبعي - 9[ ' الفرو القصيد الى الصدر
ܪ 5-5 وهو مر كل م :ديه اي نصف ومن هاء التتخصيص وهو م 1106
(النئبرشت) الذي شوئ لصف ܝܨ ا ܝ 2 اي نصف ومن رسن
اي نثوى
التاى ) ܐܨ مخض وهو المزفار
م جب 7
0
# (المنّق) اتتكثير اعدمق ٠‏ وفيا القاموس الأحمى الضعيف والاشي بالدبيسة
ܘܗܒ 1 4 4091 المنافق السفيه ܨܭ 33 لغتان شه
8 (المازق) ܡ الغليان .‫ نبا 4:0 البق 5 15
لغات ܦ
: فقال فيه الشاعر الفارسى‎ )١(
` بكذرى شى بساغى 22 كش نياوفر‎ 1
ܐܐܟ ,ܝ ܳܐ برارد شدارد رق مث افا ست
```


## [2026-09-07T17:43:26.374Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ns=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=s.split('\\f')\nfor i,p in enumerate(pages,1):\n    if 'موم' in p or 'مومي' in p:\n        print('leaf',i)\n        for m in re.finditer('موم',p):\n            print('   ...',p[max(0,m.start()-150):m.start()+200].replace('\\n',' | '))\nEOF",
 "description": "Search Addi Shir for موم"
}
```


### [2026-09-07T17:43:27.629Z] TOOL RESULT

```
leaf 11
   ...  « طاق وطءك » 5 له ` ® ܐܢ̈ܕܐ وشجرة 3 | ܝܬ للك واختلف كثيرًا في ماهيّة هذا الشجر. وقد قن اراي اكه مر ون | سجر الشييخ عاص لاد الفرس ورقة ܠܝܬ ورق الدذا لى مسموم قاتل اللموانات. | فقيل ان شجر «طاق » هو .الشجر المسى 96 «سكبيك اغاجى © ويعد شير ] | للنار وناره ܗܣ ويقال له ` ® غضا » ٠‏ وكتاب الفرائد 2 الطموع في | بيردت ܝ بالافرنسية ° 11125 | 2 307 تعر يب راس وهما < ٠‏
leaf 16
   ...  > 0 بيك | ܡܠ 100 » وقمل انه اسم رنحان جبلي ورقه - ورق الريحان ورائحته | تضارع رانحة الاترجج » | ( الباوزكر والبأزهر) حجر ينسّب اليه قوى غريبة في مقاومة السموم وهر | ܐ | ب لاف
leaf 26
   ... لبشغ ) الطر - 37 وهو 3 = ¬ 23:0 | فيها | » (البتم ) التّخمة والسّامة قيل اليثم لبها خاصة دقيل هو مخصوص بالدسم | اي 01 من طعام ديم ٠‏ وقيل ܟܘ 10 .2 2 عه المغموم ويطآق | 8 على الطعام الثقيل ܐܟ ٠‏ ٠وقالوا‏ فمه = 3 بم | شد ( اليشّام ) بح ܡ الرائحة ورقة 3 ܙ ܢܚ يعمد أنه 2 | عند الصمادلة 3 1 ܐܝ ܨ 2 يشام ܢܐܐ ان الكلمة 37 ̈ܝܚܐ | دعه دوع وهو القيصوم او عبرانة دناه دوهي 2 
leaf 30
   ...  وقالوا فيه بق تعر يب ينيك | (البنك» فارسى ححض وهو اصل الثىء ومنة الكردي بن | (البنكام » ܓ < ܒ في البيهان القاطع > ` | باككاف الفارسيّة على وزن سندان يطلق سموماً على القدح والكاس وخصوصاً على | 0 من النحاس متعارف بين فلاحي الهند يتقاسمون به !ܬܐ ٠‏ وذلك انْ اصعاب | تكروم والزروع والبساتين يتمعون في راس المقسم ٠‏ فيلقون الطاس في الماء 9 | ماء من ܗ الى ان يمتلى ]ܦ
leaf 35
   ...  | وهو سم قائل 10 له ܗܗ يلدرجين 5 ( 5 ) 3( 033 ܒ | 0 0 معناه فارة السسش وهو حيوان يشبه الفارة يسكن في اصل !+ ٠‏ وفي | المثل : اعجب من .فازة الميش تتخدّى السموم وتعش | ( السيك) 5 الات المناء ذو 2-6 0 تدحت به ¬ ܨ ييك | ® ( نيط المحيط ) . ! في لم !( هذه بار ذلعلها تصحيف اليونالي | 676 | ܝܚܘ مركب من بيار اي مر يض ومن ستان اي حل ويقال له بالتركة | خسثه خا نه | 003 ضرب هن
leaf 59
   ... ܗ 3 0 3 0 24 000 ܟ خم ١‏ 3 اميد | + ( الها ) تعتى البسرث المحفور نحت 00 المعو اب : 9 خم رهي | = السكنى في !ܠ ْ | 17 - ` 0355( 3 79 | القوس | + ( انا ردث )© المذموم كان 5-8 من 3 7 اي الردي الدم | ( | ܨ ܨ تعر يب له وهو 3 :2 ܨܝ توضع شه الدخيرة 0 | 0 الفارسي مأخوذ من ܨ ` ܒܝܬܐ ,ܐ || 0 خابية (طالع فرن | 4 \ )( | 0 ¢ الكر نه ܐܨ ܨܝ مر خون اي دم ومن سلس اي ردي | = | * ( ادش ) ات
leaf 105
   ... الشتهيرة ) 31 1 وفيها 2ه 3 0 ܟ | $ رهي مركّة من ܚܘ أي كميرة ومن بر 5 ,1 ܪ | ١‏ لكرج 5 نبات نافع ودقة وبزدهُ للجرب =( شاه نه | 1 سلطان المقول | «ܙܽ«#-ܓ«ܓ+× > رمومة فارسة مهد | * (الكهدر) ,الثلام المتحرك ما بين ثلاث شتين الى ست سنييين مركب مم | سه اي ثلاث ومن دار اي صاحب بتقدير سال اي سئة .و ينوا 0 فعالًا وقالوا | 0 | 0 ( الشهدارة ) الفاحش ,| ` ܨܝ ܝܝ ܨ اي صهيل ومن د
leaf 162
   ...  والفضّة 3 ومئة ارمغان بالتركيّة ܦ 23 | (اليرَنًا) المناء 0 ® | ( 35 رتس الصس ومن يراق من 30493 56306 966 | اخيش وتطآق ܢܒܐ على المارس ܐܝܠ ܕܟ | (التاسمين )«مششموم معروف قال الأعثى :« ويشاهسترم والايي وز مر © | ܝܟܢ معرب ٠‏ ܘܕܨ قال ܐܕܘܢ يجمل واحده ياسما او ناببما. فارسِكه باسبان | وياسمون دياسم وياسمّن ٠‏ ومئه ܐܐܐܠ 0.7" 0.1 ܕܣܡܒܐ وهو ياسمين | 31 ܕ !ܠ ܕ + و 01$11111
```


## [2026-09-07T17:43:41.919Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"مومي\\|موميا\\|مومياء\" AFM_alt.txt AFM.txt 2>/dev/null | head\necho \"=== leaf 150-153 heads ===\"\nfor L in 150 151 152 153; do echo \"--- $L\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' AFM_pages.txt | head -8; done",
 "description": "Check AFM alt and leaves 150-153"
}
```


### [2026-09-07T17:43:43.123Z] TOOL RESULT

```
=== leaf 150-153 heads ===
--- 150
د < 35
3010 رةه كامت النساء 3 1011 لعة فيها ܐܠܝ تمر يبب هر رهي
خرزة لوا ` كاون المرجان
ܢ مره
# ( مضل ) 5 5 مركب من مه اي كبير وسالي لي .مسن
1 ܨܝ § البأورة تعريب مما وهو حجر شه 5 وقيل هر ܐܐ تبه
ملو ول يوان فقيه الفرس ܠ المجوس 3:5( وججعة
ܨ
--- 151
_ 4¿ ܙ -
وا لندة 80( 3 اما فرتكل 5 ان اللاندة تعريب 1 `
(ص: ܥ )
6( بالياء 9 بهمزة ܓ 5( فيها الماء والمثقب ويقال
2 وصفها ابن السكيت والفراء وابو حاتم ٠‏ وفي التهذيب عن ابن الاعرابي : ويقال
اللمازاب 3 0 يتقديم الراء المهمة وتاخيرها ونقله الليث وجساعة ( اقرب
الوارد» :قات ان ܐܠ ܐܢ ܨ ܝܢ من ܘܬ اي بول ومن آب اي ماء ܕܝܙܝ النسمية
ظاهر (راجع ` لكل :4 )
--- 152
ܢ ܀ © | ܝܝܚ
لغتان فيه ٠‏ والظاهر ان الافظة ارامية الاصل ذعي ܐܢܒܘܒܐ باللغة البابليَة
ܕ ܐܝܟ ܨܐܬ و > دنه حدم ܐܬܐ .ܕ % ܨܝ ܨ ܝܨ 811 )ܙ(
ومعئاها الأننوبة والمزمار ܨ ܐ من ܢܒܒ اي صرخ وتخ ٠‏ .وان ܒܝܒܐ
و ܒܘܒܝܐ اى المجرى والة: ناة 885 | ܗ ܐܐ ܨ ]711 (راجع كلمة
ندب في هذا ܐܐܝ “راجع @ فرئكل ص 7١:‏ )
ܨ عر شجرة 0 و يم عاد ܐܒ وتفاحي مكلك انع
(الأنار) فارسي محض اي 21( واصل 0 المت ومنسة الارائئ”
--- 153
ܒ ܙ( ܘ | --
+ (الكراز) الشرف المتكير واعلبان 35 ` 72410 97 }܆
المهذار ܐܬܐ
ܣܣ معرب مرك ومنة 0 0
01200010004 واللاتيني 05 والفرة سي 15 و الايطاليالي 1121150
والاتكايزي 115 واطرمالي 11 ܥ و ككردي ܥ والارائي
ܢܪܩܝܣ ܙܝ ܢܪܩܘܣ والارمنى /7///404 0 عر 5 كس وان
دان اي وعاء الأرجس :
```


## [2026-09-07T17:43:52.209Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D9%88%DA%A9%D9%87/",
 "prompt": "What do Dehkhoda and Farhang-e Mo'in say about موکه (mūkeh)? Does it mean \"sting\" (نیش) or \"ewe\" (میش)? Quote the entries."
}
```


## [2026-09-07T17:43:53.591Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%88%D9%85",
 "prompt": "Give the Persian etymology of موم (mum) 'wax': what Middle Persian / Old Iranian origin, and any note about Arabic mūmiyā or borrowings into other languages? Quote the etymology."
}
```


### [2026-09-07T17:43:56.175Z] TOOL RESULT

```
I cannot answer your question based on the provided content. The web page is from Abadis Dictionary and mentions that موکه means "mother" in Sistani language ("به زبان سیستانی به مادر میگویند موکه"). However, the page does not include actual entries or definitions from Dehkhoda Dictionary or Farhang-e Mo'in regarding whether موکه means "sting" (نیش) or "ewe" (میش). To answer your question, I would need access to those specific dictionary sources.
```


### [2026-09-07T17:44:00.281Z] TOOL RESULT

```
# Persian Etymology of موم (mum)

## Middle Persian Origin

The word derives from Middle Persian with the following etymology:

**"From Middle Persian [Term?] (/⁠*mōm⁠/)"**

The exact Middle Persian form is not fully preserved in the Wiktionary entry, indicated by the bracketed "[Term?]" notation.

## Related Languages and Uncertain Ultimate Origin

The entry notes cognates across Iranian languages: Northern Kurdish *mûm*, Central Kurdish *مۆم*, and Southern Kurdish *موم* all meaning "candle" or "wax." Additionally, Old Armenian *մոմ* (mom) is identified as an Iranian borrowing.

Regarding ultimate origin, the source states: **"Perhaps a borrowing from a Semitic language, from Proto-Semitic *māy- ('water, liquid, sap')"** with comparison to Akkadian *mū*. The etymology suggests the final *-m* could derive from a plural suffix or reduplication, similar to Hebrew *מים* (mayim, "waters").

## Note on mūmiyā

The entry lists *مومیا* (mumiyā) as a derived Persian term, though it doesn't explicitly discuss whether Arabic *mūmiyā* influenced or derives from Persian *mum*.
```


## [2026-09-07T17:44:07.013Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://vajehyab.com/dehkhoda/%D9%85%D9%88%DA%A9%D9%87",
 "prompt": "Quote Dehkhoda's entry for موکه — what meanings are given (نیش? میش?) and which sources (برهان قاطع، فرهنگ نظام، لغت فرس) are cited?"
}
```


### [2026-09-07T17:44:08.596Z] TOOL RESULT

```
The server returned HTTP 500 Internal Server Error.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T17:44:13.160Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.parsi.wiki/fa/wiki/topicdetail/1e5e4f1e1e5b4f16b3a5a4b0f6ee6f4a",
 "prompt": "Does this page cover موکه? If not, say so."
}
```


## [2026-09-07T17:44:13.458Z] TOOL CALL #56: WebSearch

```json
{
 "query": "دهخدا \"موکه\" نیش عقرب برهان قاطع میش"
}
```


### [2026-09-07T17:44:18.594Z] TOOL RESULT

```
No, this page does not cover موکه (mokeh/mocha). 

The page displays a search interface for Parsi Wiki (a Persian dictionary), but shows the message "هیج کلمه ای برای جستجو وارد نشده است" (no word has been entered for search). No actual dictionary entries or definitions are presented, so there is no content about موکه or any other specific word on this particular page.
```


### [2026-09-07T17:44:21.227Z] TOOL RESULT

```
Web search results for query: "دهخدا "موکه" نیش عقرب برهان قاطع میش"

Links: [{"title":"معنی خر | لغت‌نامه دهخدا","url":"http://www.vajehyab.com/dehkhoda/%D8%AE%D8%B1"},{"title":"نیش عقرب نه از ره کین است اقتضای طبیعتش این است - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D9%86%DB%8C%D8%B4-%D8%B9%D9%82%D8%B1%D8%A8-%D9%86%D9%87-%D8%A7%D8%B2-%D8%B1%D9%87-%DA%A9%DB%8C%D9%86-%D8%A7%D8%B3%D8%AA-%D8%A7%D9%82%D8%AA%D8%B6%D8%A7%DB%8C-%D8%B7%D8%A8%DB%8C%D8%B9%D8%AA%D8%B4-%D8%A7%DB%8C%D9%86-%D8%A7%D8%B3%D8%AA/"},{"title":"نیش عقرب نه از ره کین است","url":"https://hawzah.net/fa/goharenab/View/53426/%D9%86%DB%8C%D8%B4-%D8%B9%D9%82%D8%B1%D8%A8-%D9%86%D9%87-%D8%A7%D8%B2-%D8%B1%D9%87-%DA%A9%DB%8C%D9%86-%D8%A7%D8%B3%D8%AA"},{"title":"گنجور » سعدی » بوستان » باب اول در عدل و تدبیر و رای » بخش ۱۹ - گفتار اندر نکوکاری و بدکاری و عاقبت آنها","url":"https://ganjoor.net/saadi/boostan/bab1/sh19"},{"title":"ما در این عقرب سرا هر لحظه از سر تا به پا نیشِ ماران","url":"https://www.facebook.com/shafiqshafaq61/posts/%D9%85%D8%A7-%D8%AF%D8%B1-%D8%A7%DB%8C%D9%86-%D8%B9%D9%82%D8%B1%D8%A8-%D8%B3%D8%B1%D8%A7-%D9%87%D8%B1-%D9%84%D8%AD%D8%B8%D9%87-%D8%A7%D8%B2-%D8%B3%D8%B1-%D8%AA%D8%A7-%D8%A8%D9%87-%D9%BE%D8%A7-%D9%86%DB%8C%D8%B4%D9%90-%D9%85%D8%A7%D8%B1%D8%A7%D9%86-%D9%86%DB%8C%D8%B4%D9%90-%DB%8C%D8%A7%D8%B1%D8%A7%D9%86-%D9%86%DB%8C%D8%B4%D9%90-%D8%AC%D8%A7%D9%86%D8%A7%D9%86-%D8%AE%D9%88%D8%B1%D8%AF%D9%87/1483311442105297/"},{"title":"معنی موک در زبان مازندرانی | جدول یاب","url":"https://jadvalyab.ir/mazani/موک"},{"title":"معنی ضرب المثل \" نیش عقرب نه از ره کین است، اقتضای طبیعتش این است \" - دانشچی","url":"https://www.daneshchi.ir/%D9%85%D8%B9%D9%86%DB%8C-%D8%B6%D8%B1%D8%A8-%D8%A7%D9%84%D9%85%D8%AB%D9%84-%D9%86%DB%8C%D8%B4-%D8%B9%D9%82%D8%B1%D8%A8-%D9%86%D9%87-%D8%A7%D8%B2-%D8%B1%D9%87-%DA%A9%DB%8C%D9%86-%D8%A7%D8%B3%D8%AA/"}]

Based on the search results, here's what I found about your query:

According to Dehkhoda Dictionary, "موک" (mok) refers to the sting of venomous animals like scorpions, and it can also mean sting whether it's a scorpion's sting or the sting of other creatures.

Regarding the phrase "نیش عقرب" (scorpion's sting), the saying "nīsh-e ʿaqrab nah az rāh-e kīn ast, iqtīzā-ye ṭabīʿat-ash īn ast" (the scorpion's sting is not out of malice; it's the requirement of its nature) refers to someone or something that is inherently and unintentionally harmful, troublesome, and unchangeable.

The search results also show citations from "Burhan" (برهان قاطع - Burhan-e Qāte'), which is referenced as a Persian lexicographic source, confirming these definitions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T17:44:26.171Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D9%88%DA%A9/",
 "prompt": "Quote what Dehkhoda (لغت‌نامه دهخدا) and Farhang-e Mo'in (فرهنگ معین) say for موک: meanings and cited sources (برهان قاطع، ناظم الاطباء، etc.)."
}
```


### [2026-09-07T17:44:32.319Z] TOOL RESULT

```
# موک (Muk) - Dehkhoda and Mo'in Definitions

## Dehkhoda Dictionary (لغت‌نامه دهخدا)

**Primary meaning:** "نیش جانوران گزنده مانند کژدم" (sting of venomous animals like snakes)

**Cited sources:**
- **Nazem al-Atebba** (ناظم الاطباء): defines it as the sting of biting creatures
- **Burhan** (برهان): "نیش را گویند خواه نیش عقرب باشد و خواه نیش چیزهای دیگر" (sting generally, whether scorpion or other creatures)
- **Asadi Farhang** (فرهنگ اسدی): provides a disputed poetic example from Asjadi

The Dehkhoda entry notes considerable debate about whether موک means sting (نیش), tooth (میش), or something else, with the author arguing the sting definition is most defensible.

## Farhang-e Mo'in (فرهنگ معین)

**Definition:** "میش" (tooth/fang)

This represents the alternative interpretation to Dehkhoda's preferred sting meaning.
```


## [2026-09-07T17:44:47.866Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/mudr%C4%81",
 "prompt": "Give the reconstruction page content for Proto-Iranian *mudrā: meaning, origin, and the list of descendants (Middle Persian, Khotanese, Sogdian, Persian, Sanskrit borrowing)."
}
```


### [2026-09-07T17:44:49.579Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T17:44:52.298Z] TOOL CALL #59: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D9%85%D9%87%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A5%81%E0%A4%A6%E0%A5%8D%E0%A4%B0%E0%A4%BE' \\\n 'https://www.etymonline.com/word/mummy' \\\n 'https://www.etymonline.com/word/mogul' \\\n 'https://www.etymonline.com/word/mummery' \\\n 'https://en.wiktionary.org/wiki/%D9%85%D9%88%D9%85' \\\n 'https://abadis.ir/fatofa/%D9%85%D9%88%DA%A9/' ; do\n timeout 180 python3 tools/fetch_source.py \"$u\" --note 'page 344 verification (Muk / Mum / Mura)' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-07T17:44:56.941Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/575d3fb94b2360ed.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1806e8dbaa8d5d0a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/20c3ddcb6dabba92.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a6ef1ba98021fc49.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cb5dab25a4446468.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3b639979e37768a3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2fb82861e8117088.txt
```


## [2026-09-07T17:45:04.977Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/muhr",
 "prompt": "Is there a Middle Persian entry for muhr 'seal'? Quote its etymology and descendants. Also any Hindi/Urdu muhr entry etymology."
}
```


### [2026-09-07T17:45:06.599Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T17:45:13.526Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\ns=open('575d3fb94b2360ed.txt',encoding='utf-8',errors='replace').read()\ni=s.find('Etymology')\nprint(s[:200])\nimport re\n# print all etymology sections\nfor m in re.finditer(r'Etymology \\d', s):\n    print('=====', s[m.start():m.start()+900].replace('\\n',' '))\nEOF",
 "description": "Read archived Wiktionary مهر"
}
```


### [2026-09-07T17:45:15.022Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%D9%85%D9%87%D8%B1
FETCHED: 2026-09-07T16:00:30Z
STATUS: 200
TITLE: مهر - Wiktionary, the free dictionary

مهر - Wiktionary, the free dictionary 

 Jump to content 
===== Etymology 1    1.1.1   Verb    1.1.1.1   Conjugation    1.1.2   Noun    1.1.2.1   Declension    1.1.2.2   Descendants    1.2   Etymology 2    1.2.1   Noun    1.2.1.1   Declension    1.2.1.2   Descendants    1.2.2   Verb    1.2.2.1   Conjugation    1.2.3   Noun    1.2.3.1   Declension    1.2.4   Related terms    1.3   Etymology 3    1.3.1   Verb    1.3.1.1   Conjugation    1.4   Etymology 4    1.4.1   Noun    1.4.1.1   Declension    2   Ottoman Turkish    Toggle Ottoman Turkish subsection    2.1   Etymology 1    2.1.1   Alternative forms    2.1.2   Noun    2.1.2.1   Derived terms    2.1.2.2   Descendants    2.1.3   Further reading    2.2   Etymology 2    2.2.1   Noun    2.2.1.1   Derived terms    2.2.1.2   Descendants    2.2.2   Further reading    3   Persian    Toggle Persian subsection    3.1   Etymology 1    3.1.1   Pronunciation    3.1.2   Noun    3.1.2.1   Synonyms    3.2   Etymology
===== Etymology 2    1.2.1   Noun    1.2.1.1   Declension    1.2.1.2   Descendants    1.2.2   Verb    1.2.2.1   Conjugation    1.2.3   Noun    1.2.3.1   Declension    1.2.4   Related terms    1.3   Etymology 3    1.3.1   Verb    1.3.1.1   Conjugation    1.4   Etymology 4    1.4.1   Noun    1.4.1.1   Declension    2   Ottoman Turkish    Toggle Ottoman Turkish subsection    2.1   Etymology 1    2.1.1   Alternative forms    2.1.2   Noun    2.1.2.1   Derived terms    2.1.2.2   Descendants    2.1.3   Further reading    2.2   Etymology 2    2.2.1   Noun    2.2.1.1   Derived terms    2.2.1.2   Descendants    2.2.2   Further reading    3   Persian    Toggle Persian subsection    3.1   Etymology 1    3.1.1   Pronunciation    3.1.2   Noun    3.1.2.1   Synonyms    3.2   Etymology 2    3.2.1   Pronunciation    3.2.2   Noun    3.2.2.1   Derived terms    3.2.2.2   Descendants    3.2.3   Proper noun    3.2.3
===== Etymology 3    1.3.1   Verb    1.3.1.1   Conjugation    1.4   Etymology 4    1.4.1   Noun    1.4.1.1   Declension    2   Ottoman Turkish    Toggle Ottoman Turkish subsection    2.1   Etymology 1    2.1.1   Alternative forms    2.1.2   Noun    2.1.2.1   Derived terms    2.1.2.2   Descendants    2.1.3   Further reading    2.2   Etymology 2    2.2.1   Noun    2.2.1.1   Derived terms    2.2.1.2   Descendants    2.2.2   Further reading    3   Persian    Toggle Persian subsection    3.1   Etymology 1    3.1.1   Pronunciation    3.1.2   Noun    3.1.2.1   Synonyms    3.2   Etymology 2    3.2.1   Pronunciation    3.2.2   Noun    3.2.2.1   Derived terms    3.2.2.2   Descendants    3.2.3   Proper noun    3.2.3.1   Derived terms    3.2.3.2   Related terms    3.2.3.3   Descendants    3.2.4   Coordinate terms    3.2.5   See also    3.3   Etymology 3    3.3.1   Pronunciation    3.3.2   Noun    3.3.2.1 
===== Etymology 4    1.4.1   Noun    1.4.1.1   Declension    2   Ottoman Turkish    Toggle Ottoman Turkish subsection    2.1   Etymology 1    2.1.1   Alternative forms    2.1.2   Noun    2.1.2.1   Derived terms    2.1.2.2   Descendants    2.1.3   Further reading    2.2   Etymology 2    2.2.1   Noun    2.2.1.1   Derived terms    2.2.1.2   Descendants    2.2.2   Further reading    3   Persian    Toggle Persian subsection    3.1   Etymology 1    3.1.1   Pronunciation    3.1.2   Noun    3.1.2.1   Synonyms    3.2   Etymology 2    3.2.1   Pronunciation    3.2.2   Noun    3.2.2.1   Derived terms    3.2.2.2   Descendants    3.2.3   Proper noun    3.2.3.1   Derived terms    3.2.3.2   Related terms    3.2.3.3   Descendants    3.2.4   Coordinate terms    3.2.5   See also    3.3   Etymology 3    3.3.1   Pronunciation    3.3.2   Noun    3.3.2.1   Derived terms    3.3.2.2   Related terms    3.3.2.3   Descen
===== Etymology 1    2.1.1   Alternative forms    2.1.2   Noun    2.1.2.1   Derived terms    2.1.2.2   Descendants    2.1.3   Further reading    2.2   Etymology 2    2.2.1   Noun    2.2.1.1   Derived terms    2.2.1.2   Descendants    2.2.2   Further reading    3   Persian    Toggle Persian subsection    3.1   Etymology 1    3.1.1   Pronunciation    3.1.2   Noun    3.1.2.1   Synonyms    3.2   Etymology 2    3.2.1   Pronunciation    3.2.2   Noun    3.2.2.1   Derived terms    3.2.2.2   Descendants    3.2.3   Proper noun    3.2.3.1   Derived terms    3.2.3.2   Related terms    3.2.3.3   Descendants    3.2.4   Coordinate terms    3.2.5   See also    3.3   Etymology 3    3.3.1   Pronunciation    3.3.2   Noun    3.3.2.1   Derived terms    3.3.2.2   Related terms    3.3.2.3   Descendants    3.3.3   See also    3.4   Anagrams    Toggle the table of contents    مهر    12 languages    فارسی   Français   
===== Etymology 2    2.2.1   Noun    2.2.1.1   Derived terms    2.2.1.2   Descendants    2.2.2   Further reading    3   Persian    Toggle Persian subsection    3.1   Etymology 1    3.1.1   Pronunciation    3.1.2   Noun    3.1.2.1   Synonyms    3.2   Etymology 2    3.2.1   Pronunciation    3.2.2   Noun    3.2.2.1   Derived terms    3.2.2.2   Descendants    3.2.3   Proper noun    3.2.3.1   Derived terms    3.2.3.2   Related terms    3.2.3.3   Descendants    3.2.4   Coordinate terms    3.2.5   See also    3.3   Etymology 3    3.3.1   Pronunciation    3.3.2   Noun    3.3.2.1   Derived terms    3.3.2.2   Related terms    3.3.2.3   Descendants    3.3.3   See also    3.4   Anagrams    Toggle the table of contents    مهر    12 languages    فارسی   Français   Magyar   Kurdî   Lietuvių   Malagasy   Nederlands   Polski   Русский   Svenska   Türkçe   中文    Entry    Discussion    English    Read    Edit   
===== Etymology 1    3.1.1   Pronunciation    3.1.2   Noun    3.1.2.1   Synonyms    3.2   Etymology 2    3.2.1   Pronunciation    3.2.2   Noun    3.2.2.1   Derived terms    3.2.2.2   Descendants    3.2.3   Proper noun    3.2.3.1   Derived terms    3.2.3.2   Related terms    3.2.3.3   Descendants    3.2.4   Coordinate terms    3.2.5   See also    3.3   Etymology 3    3.3.1   Pronunciation    3.3.2   Noun    3.3.2.1   Derived terms    3.3.2.2   Related terms    3.3.2.3   Descendants    3.3.3   See also    3.4   Anagrams    Toggle the table of contents    مهر    12 languages    فارسی   Français   Magyar   Kurdî   Lietuvių   Malagasy   Nederlands   Polski   Русский   Svenska   Türkçe   中文    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file 
===== Etymology 2    3.2.1   Pronunciation    3.2.2   Noun    3.2.2.1   Derived terms    3.2.2.2   Descendants    3.2.3   Proper noun    3.2.3.1   Derived terms    3.2.3.2   Related terms    3.2.3.3   Descendants    3.2.4   Coordinate terms    3.2.5   See also    3.3   Etymology 3    3.3.1   Pronunciation    3.3.2   Noun    3.3.2.1   Derived terms    3.3.2.2   Related terms    3.3.2.3   Descendants    3.3.3   See also    3.4   Anagrams    Toggle the table of contents    مهر    12 languages    فارسی   Français   Magyar   Kurdî   Lietuvių   Malagasy   Nederlands   Polski   Русский   Svenska   Türkçe   中文    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/ex
===== Etymology 3    3.3.1   Pronunciation    3.3.2   Noun    3.3.2.1   Derived terms    3.3.2.2   Related terms    3.3.2.3   Descendants    3.3.3   See also    3.4   Anagrams    Toggle the table of contents    مهر    12 languages    فارسی   Français   Magyar   Kurdî   Lietuvių   Malagasy   Nederlands   Polski   Русский   Svenska   Türkçe   中文    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From Wiktionary, the free dictionary   See also: مہر    Arabic  [ edit ]    Etymology 1  [ edit ]    Common West Semitic term; compare Ugaritic
===== Etymology 1  [ edit ]    Common West Semitic term; compare Ugaritic 𐎎𐎅𐎗 ( mhr ) , Old South Arabian 𐩣𐩠𐩧𐩩 ( mhrt , “ wealth, possessions, commodities, goods ” ) , Biblical Hebrew מָהַר ( mahar , “ to acquire by exchange, to barter, to purchase ” ) , Biblical Hebrew מֹהַר ( mṓhar , “ bridal payment, purchasing price ” ) , Classical Syriac ܡܗܪܐ ( “ bride-price ” ) , Nabataean 𐢓𐢇𐢛 ( mohar ) . Uncertain connection to highly productive Akkadian 𒈠𒄩𒀸 ( maḫārum , “ to face or meet; to accept, to receive; to conduct; to do business, to shift commodities, to transact; to accept valuables, staples, or persons; to take in or collect offers, to take in women by dowries ” ) and Soqotri móḥor ( “ to offer ” ) , as the sound change complicates the semantic overlaps. Comparison to Middle Persian mtr' ( /⁠mihr⁠/ , “ contract, bond ” ) is fundamentally coincidental.   Verb  [ edit ]    مَهَرَ • ( mahara ) I
===== Etymology 2  [ edit ]    From Middle Persian [Book Pahlavi needed] ( mwdl ) , 𐫖𐫇𐫍𐫡 ( mwhr /⁠muhr⁠/ , “ seal ” ) , and denominal verb.   Noun  [ edit ]    مُهْر • ( muhr )  m    seal ; signet ; stamp    Declension  [ edit ]    Declension of noun مُهْر ( muhr )   singular   basic singular triptote    indefinite   definite   construct   informal   مُهْر   muhr    الْمُهْر   al-muhr    مُهْر   muhr    nominative   مُهْرٌ   muhrun    الْمُهْرُ   al-muhru    مُهْرُ   muhru    accusative   مُهْرًا   muhran    الْمُهْرَ   al-muhra    مُهْرَ   muhra    genitive   مُهْرٍ   muhrin    الْمُهْرِ   al-muhri    مُهْرِ   muhri    Descendants  [ edit ]    → Swahili: muhuri    Verb  [ edit ]    مَهَرَ • ( mahara ) I ( non-past يَمْهَرُ ( yamharu ) , verbal noun ? )    to stamp , to imprint    Conjugation  [ edit ]    Conjugation of مَهَرَ (I, sound, a ~ a, full passive (?) , verbal noun ? )   verbal noun 
===== Etymology 3  [ edit ]    From Proto-Semitic *mahir- / *marw- ( “ (young) man; still fast and physically useful ” ) , possibly further Proto-Afroasiatic *ma(hi)r- ( “ servant, slave ” ) , potentially related to Arabic مَرْء ( marʔ ) . Compare Akkadian 𒌉 ( mārum , “ young man, son; subordinate, deployable man, service man, usable worker, hireling for a service ” ) , Ugaritic 𐎎𐎅𐎗 ( mhr , “ warrior, man, troop; skilled, expert, trained; exceptional, faster, better, or heroic ” ) , Sabaean 𐩩𐩣𐩠𐩧𐩩 ( tmhrt , “ contingent of Bedouin mercenaries; specialty troops, proficient at handling camels and desert warfare ” ) , Aramaic מהר , Hebrew מָהִיר , Hebrew מַהֵר , Phoenician 𐤌𐤄𐤓 ( mhr ) , Classical Syriac ܡܗܪ ( “ to instruct, to be instructed, to learn, to excel ” ) , Ge'ez ምሁረ ( məhurä /⁠məhur⁠/ , “ trained ” ) .   Verb  [ edit ]    مَهَرَ • ( mahara ) I ( non-past يَمْهُرُ ( yamhuru ) or يَمْهَرُ 
===== Etymology 4  [ edit ]    Inherited from Proto-Semitic *muhr- .   Noun  [ edit ]    مُهْر • ( muhr )  m ( plural أَمْهَار ( ʔamhār ) or مِهَارَة ( mihāra ) , feminine مُهْرَة ( muhra ) )    foal , colt    Declension  [ edit ]    Declension of noun مُهْر ( muhr )   singular   basic singular triptote    indefinite   definite   construct   informal   مُهْر   muhr    الْمُهْر   al-muhr    مُهْر   muhr    nominative   مُهْرٌ   muhrun    الْمُهْرُ   al-muhru    مُهْرُ   muhru    accusative   مُهْرًا   muhran    الْمُهْرَ   al-muhra    مُهْرَ   muhra    genitive   مُهْرٍ   muhrin    الْمُهْرِ   al-muhri    مُهْرِ   muhri    dual   indefinite   definite   construct   informal   مُهْرَيْن   muhrayn    الْمُهْرَيْن   al-muhrayn    مُهْرَيْ   muhray    nominative   مُهْرَانِ   muhrāni    الْمُهْرَانِ   al-muhrāni    مُهْرَا   muhrā    accusative   مُهْرَيْنِ   muhrayni    الْمُهْرَيْنِ   al-muhrayni
===== Etymology 1  [ edit ]    Borrowed from Classical Persian مهر ( muhr , “ seal ” ) , from Middle Persian 𐫖𐫇𐫍𐫡 ( mwhr /⁠muhr⁠/ , “ seal ” ) .   Alternative forms  [ edit ]    միւհր ( mühr ) , միւհիւր ( mühür ) — Armeno-Turkish    Noun  [ edit ]    مهر • ( mühr or mühür ) ( definite accusative مهری ( mührü ) , plural مهرلر ( mührler, mühürler ) )    seal , a stamp used to impress a design on a soft substance   Synonym: خاتم ( hatem )    the impression of such stamp on a material used for sealing   Synonym: خاتم ( hatem )    Derived terms  [ edit ]    مهر اورمق ( mühür urmak , “ to seal ” )   مهر باصمق ( mühür basmak , “ to seal ” )   مهر خم ( mühr-i hum , “ seal impressed on the mouth of a jar ” )   مهر ذاتی ( mühr-i zatî , “ kind of seal ” )   مهر سلیمان ( mühr-i süleimân , “ Solomon's seal ” )   مهر سوكمك ( mühür sökmek , “ to annul one's promise ” )   مهر فكی ( mühür fekki , “ breaking of
===== Etymology 2  [ edit ]    Borrowed from Arabic مَهْر ( mahr , “ dowry, dower ” ) .   Noun  [ edit ]    مهر • ( mehr ) ( definite accusative مهری ( mehri ) , plural مهور ( mühur ) )    ( Islam ) mahr , a pre-negotiated and mandatory gift from the groom to the bride , usually money    Derived terms  [ edit ]    مهر مؤجل ( mehr-i müeccel , “ bride price given at the wedding ” )   مهر معجل ( mehr-i muʼaccel , “ bride price given in case of divorce ” )    Descendants  [ edit ]    Turkish: mehir , mehr , mihr    Further reading  [ edit ]    click to expand   Barbier de Meynard, Charles ( 1886 ), “ مهر ”, in Dictionnaire turc-français , volume II, Paris: E. Leroux, page 802    Çağbayır, Yaşar ( 2007 ), “ mehir1 ”, in Ötüken Türkçe Sözlük (in Turkish), volume 3, Istanbul: Ötüken Neşriyat, page 3114    Devellioğlu, Ferit ( 1962 ), “mehr”, in Osmanlıca-Türkçe Ansiklopedik Lûgat ‎ [ Ottoman–Turkish 
===== Etymology 1  [ edit ]    The first sense borrowed from Arabic مَهْر ( mahr , “ dowry ” ) , from the verb مَهَرَ ( mahara , “ to contract, to give a dowry ” ) ; see above. The remaining senses inherited from Middle Persian mtr' ( mihr , “ bond, contract ” ) , from Old Persian 𐎷𐎡𐎰𐎼 ( mi-i-θ-r /⁠Miθraʰ⁠/ ) , from Avestan 𐬨𐬌𐬚𐬭𐬋 ( miθrō , “ covenant, contract, oath ” ) , from Proto-Iranian *miθráh , from Proto-Indo-Iranian *mitra ( “ covenant, treaty, agreement, promise ” ) . Compare Sanskrit मित्र ( mitra ) and the above for a possible layer of phono-semantic matching with the Semitic root regarding business contracts and reception.   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ˈmahr/    ( Dari, formal ) IPA ( key ) : [mäɦɾ]    ( Dari, formal ) IPA ( key ) : [mäɦɾ]   ( Kabuli ) IPA ( key ) : [mɒːɾ]    ( Hazaragi ) IPA ( key ) : [mɔːɾ]    ( Iran, formal ) IPA ( key ) : [mæ
===== Etymology 2  [ edit ]    From Middle Persian mtr' ( Mihr ) , from Old Persian 𐎷𐎡𐎰𐎼 ( Miθraʰ ) , from Avestan 𐬨𐬌𐬚𐬭𐬀 ( miθra , “ covenant, contract, oath ” ) , from Proto-Indo-Iranian *mitra ( “ covenant, treaty, agreement, promise ” ) . Compare Sanskrit मित्र ( mitra ) , Ancient Greek μεσίτης ( mesítēs ) . Doublet of میترا ( mitrā , personal name ) .   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ˈmihr/    ( Dari, formal ) IPA ( key ) : [me̞ɦɾ]    ( Dari, formal ) IPA ( key ) : [me̞ɦɾ]   ( Kabuli ) IPA ( key ) : [meːɾ]    ( Hazaragi ) IPA ( key ) : [miɾ]    ( Iran, formal ) IPA ( key ) : [meɦɹ]    ( Tajik, formal ) IPA ( key ) : [meɦɾ]    Rhymes: -ihr    Readings   Classical reading ?    mihr   Dari reading ?    mehr   Iranian reading ?    mehr   Tajik reading ?    mehr   Audio ( Iran ) : ( file )    Audio ( Iran ) : ( file )    Noun  [ edit ]    مهر • ( mihr / mehr ) (
===== Etymology 3  [ edit ]    From Middle Persian [Book Pahlavi needed] ( mwdl ) , 𐫖𐫇𐫍𐫡 ( mwhr /⁠muhr⁠/ , “ seal ” ) (compare Parthian 𐫖𐫇𐫍𐫡 ( mwhr /⁠muhr⁠/ , “ seal ” ) , and Bactrian μολρο ( molro ) ); possibly cognate with words above, otherwise from Akkadian 𒈬𒊬 ( mušarû , “ object bearing a royal inscription ” ) , from Sumerian 𒈬𒊬 ( mu-sar /⁠musar⁠/ ) , from 𒈬 ( mu , “ name, fame ” ) + 𒊬 ( sar , “ to write ” ) ; cf. the many descendants of Sumerian 𒁾 ( dub , “ tablet; cylinder seal ” ) including دیوان ( divân ) , دف ( daf ) , دفتر ( daftar ) , Arabic أَدَب ( ʔadab ) , طُوب ( ṭūb ) , طَابَع ( ṭābaʕ ) , ذَبْر ( ḏabr , “ a writing on palm-leaves, a book ” ) , ذَبَرَ ( ḏabara , “ to write, to point; to read thoroughly; to understand well ” ) .   مُهر   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ˈmuhr/    ( Dari, formal ) IPA ( key ) : [mo̞ɦɾ]    ( Dari, formal ) IPA ( key
```


## [2026-09-07T17:46:17.679Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nls\npython3 - <<'EOF'\ns=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=s.split('\\f')\nprint('leaves',len(pages))\nimport re\nfor i,p in enumerate(pages):\n    if re.search(r'muga|m[uū]k-|mocke|Haufe', p) and re.search(r'muga|mugr|mūk', p):\n        print('=== leaf',i)\n        print(p[:2500])\n        break\nEOF",
 "description": "Search Walde-Pokorny Bd2 for muk"
}
```


### [2026-09-07T17:46:18.943Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
leaves 725
=== leaf 259
                            meuk          meudh-, maudh-, mudh-                          255

liat vielleicht nach ihnen auBergerm. Entsprechung an lett. smaugs „schlank‘‘
(wie mhd. gesmilcket), poln. smug^ smuga (neben smuJc) „Engpa6, schmaler
Streifen^.
  Gemeinsamer Ausgangspunkt beider Gruppen, A. undB., ist trotz Fickl^
            wohl moglich; „schlupfriges Zeug, schliipfen*', woraus einer-
104, 520 sehr
seits j.schleimig, Schleim^', andrerseits ,,gleiten, dariiber streichen, schliefen“.
Erweiterung von men- j,feucht, netzen, scbmieren“ (fiir Gruppe B. denkt
Fick aaO. an Beziehnng zu 7ncii- „schieben“).
  Vgl. bes* Johansson PBrB. 15,235, Zupitza Gutt. 136, t3Sf. (Lit), 164.

ineuk- „kratzen, ritzen".
  gr.   duvyMXm   *
                      at dxideg tcov ^sko)v Tiagd to djuvoosiv Hes.,           djLivoaco, att.

d/LWiTco „ritze, zerkratze“,             Schvamme*^, d/uv^j^og ds., djuvy/na,
djbtvyjnog „das Zerraufen (der Haare)“; lat mucro „scharfe Spitze, z. B. der
Zahne, der Klanen, der Pflugschar, eines Kometen, bes. des Speeres oder
Schwertes, dieses selbst'; vielleicht lit musdi „schlagen“ (wenn ursprgl.
etwa „gewalttatig reiBen, verkratzen“). Curtins^ 546, weitere Lit bei Vf.
LEWb.^ 497 {miicro lycht besser nach Zupitza GG. 138f. zu anord. smjuga
,;hindurchkriechen, schliipten, auch durchbohren“).
   Lit muszti konnte auch ursprgl. „boxen“ gewesen sein; dann vielleicht zu ai.
musti-h,            ,,Faust“ (Uhlenbeck KZ. 39, 260 f. GiintertsKZ. 45, 193 ff.,
                                                              ;


Ankniipfung an 7niis „Maus, Muskeh' ist bei der Seltenheit von auf Sub-
stantiven beruhenden ^ -Nomina
                            2              —
                                      vergleichbar ware hochstens der Typus
ir. elit ,,Reh“ aus          s. Brugmannll^ 1, 421, 439            —
                                                            nicht vorzuziehen)
und (??) cymr. migwrn „Kn6cbel“, bret. migourn „Knorpel“ (Pick II ^ 419;
liber den Wortausgang s. Pedersen KG. II 53, nicht besser Foy IF. 8, 202).
DaB damit auch die obigen gr. und lat, Worte in der Weise verwandt seien,
daB jjSpitze zum Kratzen, Ritzen“ aus „Boxfaust mit spitz vorgestrecktem
Knochel des Mittelfingers'' die Gdbed. gewesen sei, verlore sich ins durch-
aus unbeweisbare.

nieug- „heimlich und tiickisch            lauern‘‘.
  Lat. 7niiger „der Falschspieler          beim Wiirfelspiel^ (Zupitza Gutt. 216; Vf-
LEWb.2 s. V.);
   air. formiiigihe, form
```


## [2026-09-07T17:46:24.755Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\ns=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=s.split('\\f')\nfor i in (314,315,316):\n    print('=== leaf',i)\n    print(pages[i][:3000])\nEOF",
 "description": "Walde-Pokorny Bd2 p.311"
}
```


### [2026-09-07T17:46:26.062Z] TOOL RESULT

```
=== leaf 314
310                                            mu-


  ai.    miika- ,.stumm“, arm. (Bugge KZ. 32, 21            ,
                                                                        Scheftelowitz BB. 29, 31)
mnnj „stumm“,         gr. jjtvKog^ fLimig, juvirog, juvdog, juvragog,         Hes. /iivvddg. Soph.
„8tumm^ lat. muh(s „stumm^^;                  anch (Falk^Torp
                                           vgl.                               u.   muMe K) alter
dan. mite, norw. mua            „schweigen, nicht mucksen^.
  Nicht iiberzengend, nimmt Brugmann Pestschr. f. Thomsen 6 fiir ai. muha-
(auch mura- „stumpf8innig, dumm“, doch s. mo[ii\ro-) lat. mutus, gr. juvrig
nach Analogie von stiimm: stumpf eine ursprgl. Bed. ,,stumpf“ an unter
Anknhpfung an lat. miitilus (s. wut-) und deutet Holthausen KZ. 46, 178
von mutus „*stumpf aus auch muto „pems^^ als „Stummer' (s. u. muk^Sr
                            '



„gesfeutzt“);
   ahd. mawen ,,schreien“, lett. maimu, mdivii, maid ,,briillen'', cech. myjati
„miihen“;
   ai. muhJia- n. „Mund‘' (mit Formans -Bia-, s. Parallelen bei Petersson

KZ. 47, 284; nicht nach Bugge KZ, 32, 20 als „Eingang“ zu gr. juv/og; hber
jLtvoTai „Oberlippe, Schnurbart“ s. Boisacq m. Lit.), ahd. mrda f., mhd.
mfd n. ,,Maul“, ags. mille „Maul, Schnauze*', aisl mfdi „MaiiI, bes. Ober-
lippe   an Tieren, hervorragende Felsspitze'', got. faur midjan .,das Maul
zubinden“ (fiir Delters ZfdA. 42, 59 Herleitung aus "^mfdlo- besteht kein
AnlaS; unrichtig Wood IP. 18, 33), gr. /uvlXov, pvlkog ,,Lippe'‘, /uidkoj ,,80^1666“
die Lippen“; juvlkalvco „verziehe unwillig den Mund, schneide Gesiehter“
(ob mit anl. s- dazu norw. smauJ, lett. smaide ,,MauP?? Pick IDA 329 f).
   Mit dentalen Formantien, bzw. Wzerw. wohl gr.                    :       „Wort,
Rede“ (anders u. metidJi- ,,worauf bedacht sein'' Tiber das seiner Herkunft
                                                                ;


und Bed. nach ganz unklare lat. Schimpfwort mtifrius s. Vf. LEWb.^ s. v.);
   lat. muttio, -tre „mucksen“, muttum nullum „keinen Muckser'* (vgl. o.
mutmid) lett. mute „Mund“ ahd. mxdilon „murmeln, rieseln^', musse „Quelle‘'
            \                       ;


(z. B. Koreen Ltl. 191j, aisl.        „murmeln“, daneben mit germ, t norw.
mdartl.   mutra, mengl.  mideren, engi.   mutter ds.
   Guttur ale rweiter ungen                :



   Mit          gr. pvyAo^iai „brulle^',   mhd. mfdien, mfigen, mawen „brullen^’, abg.
myH „Gebruir', russ. mycdh „brullen'', skr. slov. cech. muJcatl „brullen“.
   Mit g: ai.muyljati, inojati „gibt einen bestimmten Ton von sich'* (Dhatup.);
gr.  pivl^co „bringe mit geschlossenen Lippen einen Laut hervor, stohne‘"

(daraus lat. mussCtre^ s. Yf. LEWb.^ s. v.), j.iv]\u6g ,,Seufzer^;
   lat. mugio, -Ire „brullen^', conmugento „convocanto‘‘, muginor j.murmelo

laut, brause“ (auch „nugari et quari tarde conarP;, umbr. miiieio „muttitum^^
mugatu „muttitoA lat. mugilare vom Yaturlaut des Esels: ahd. muckazzen
,,leise reden,
=== leaf 315
                                      mu-, mus          mugli-so,   -&I0-, -sko-                            311

   Zugehorige Schallworte aus dem Germ» sind auch mnd. mtimmelen, engl.
mumble    j.niurmein, knaupeln'', engl. mtmp, norw. mumpa ds. (Ficklll^
323, Falk-Torp u, mtimle); mhd. mtipf, mw;^\,Verziehung des Mundes'‘,
mupfen^ muffen, mnd. mopen, engl. mope ,,galFen'', engl. mop „Fratze''
(Fick III^ 323 f., Falk-Torp u. maahe)\ vielleicht nhd. bair. mduen ,,wieder-
kauen‘‘ u. dgl. (Fick        323, Falk-Torp u. maiiJe),
  Vgl. Curtins 336, Yanuek LEWb.^ 205, 222, Fick           104, 511, 11^ 219,
III^ 323f., 326f., 531 (sucht wie Falk-Torp u. S7nile einen Zshang mit smeu
= S7nei j.lacheln^'; nicht iiberzeugend), Prellwitz u. juv^co, nv, Uhlenbeck
PBrB. 27, 118, usw.

mu-, mus- in Worten fiir „Mucke, FUege'*.
  Arm. (Bugge KZ. 32, 20, Hiibsclimann Arm. Gr. I 476)                                         7nim, gen. m7ioy
„Steclimucke“ (Gdf. mws-, oder mu-7io-)',
  alb. mi-^e {ze Diminutivsuffix) „Mucke'' (G. Meyer BB. 8, 1 90, Alb Wb. 281);
     gr.   i^ivTa     {^pvoia) „F]iege“;         lat.    musca „Fiiege^^;              aisl.   my n.   (^miija-)
„Mucke“; schwed. mygg^                            ags. mycg, as. muggia, ahd, mncka „Mucke“
{-ggj'     aus      -ivj-1   ob   lett.   smiidzi „kleine Fliegen, Miicken'', Endzelin IF, 33,
126, altes          Formans g erweise,
                                  ist jedenfalls fraglich ist es trotz des anl,    ;



s- germ. Lw.?); mit - 5 - gotland. mausa (^mfisa), flam, mmzie (^mus1)\ lit.
muse^ apr. 7nuso^ lett. miisa, 7nusclia „Fiiege“ abg. mucha „Fliege“ (mousa)^
                                                                     ;


m^^ica „Mucke“.
  Ygl. Curtius 336, Bugge aaO., Falk-Torp u. myg, Es liegt das Summen
malendes 7nu, 7ns zugrunde, Prellwitz u. avTa, Uhlenbeck Ai. Wb. M^maMa-h.
Nicht nach Pedersen IF. 5, 34 zu mus „Maus'' als „kleine Mause“.

mukeii- „Haufe'' und Zubehor.
  Gr. uvxmv* ocooog d7]jud)v Hes. nach Persson Beitr. 221 f. = aisl. mitgi
„Haufen (Heu), groBe Menge (Menschen)", (auch magr), ags. muga „(Korn-)
Haufen*^  muha ds. (auch 7}iuwa), vgl. AN^eiter schwed. mdartl. 7noa „zu-
sammenhaufeii'' i^'muhdfi), ahd. mu-iverf ,,Maulwurf‘‘, mit -h{]i)- aus -/jn'-
mnd. 7nake, ndl. muik, mhd. mache, nhd. (halb nd.) Maitke, bair. (edit
hochd.) 7naticlie „Auswuchs, FuBgeschwulst der Pferde“, schweiz. 7nauch
m. j.kropfiger Auswuchs am aiten Kebholz. unordentlicher Haufe, KIoB-
chen‘* und mit ii norw.-mdartl. mukka „Haufen, Menge‘‘, mhd. mocke m.
„Klumpen, Brocken*' (damit identisch ist mhd. mocke ..Zuchtsau", Johansson
KZ. 36, 375, wozu aber im Yokal nicht stimmen air, mticc^ cymr. moch
,,Schw^ein“ gall. Mocco EN., s. u. meuk- „schlupfrig“)     aisl. mosir „gro6e          ;


Menge" {"^muhstra-, Sverdrup IF. 35, 55); einzige Hochstufenform in
                                                               1


ags. mUagol ,,(*klumpig, massig'* ==) ,,fest, stark" (Holthausen IF. 20,317
=== leaf 316
312                                                   mut-os   — nius
   phokaisch           fxvy^Aog       jjZuclitesel,      Springesek^ Hes.                    alter    mugh-
sJos)   =   lat.     mfdtis    5
                                   ,MauIesel, Maultier“,          Demin,   muscell-iis,   -a mit volks-
sprachlich               aus "^muxellus (^muxlo4o-s)\ vielleicht auch gr.
                     Umstellung
j.ivoxloi‘      01    oxoXioi Hes
                           („pervers“; vermutlich Vermischung von "^mugh-
slo- mit ^mugh-sqo-,  Niedermann    Mel. Meillet 1902, 101 fF.);
   Alb. niiish „Manlesel“ (Gr. Meyer Alb. Wb. 293, IF. 1, 322 f. mit Erorte-
riing der N'amen des Tieres in                            den Balkansprachen;         Gdf.    aber     nichfc
          sondern mtigh-sqos).
''^'miis-hos,

   S. noch Yf. LEWb.2 u. mUhis.
   Sehr gewagt ware die Yermutung, daB vom Begriff des Tierbastarda
iiberhanpt, und soldier von Ziegen nnd Schafen im besondern aucb lat.
mufro ^jnubro und (fremdes) rmismo (s. Yf. LEWb.^ ii. mtifro) verwandt,
also auf mugh-srO’, -smo- zuriickzufuhren seien.


iimt-os       ,,gestutzt‘'.

   Lat. 7nutilns „verstummelf',                      mttiims ..gestutzt, abgestutzt'’ (Arista); ir.
7mtt, scbott. fmitach „kurz^'                    (Thurneysen KR. 67, Stokes IF. 2, 173, Zupitza
KZ 36, 243;                   aus    -ifw-?).

   Hesychs                           (Curtms717, Fick I^ 520) ist wohl Um-
                     fxvxtkog „verstummelt-^
stellung aus juiTvkog ds.     mai4- „hauen'').
                                           (s.

   Ai. miidgara „Hammer^^ wofiir Scheftelowitz IF. 33, 146 Entsteliung aus
"^mut-ga-ra- erwagt, ist von seiten der Bed. ein ganz vager Yergleich.
   Moglicherweise ist ir. moth ,,penis“ als ..Stummek' anzureihen; damit
verbindet Strachan KZ. 33, 304, Holthausen KZ. 46, 17Sf., lat. mato, mutto,
mutonimn, Aus ds., die aber wegen des Lucilius moetino sulrectoque signo
doch wohl ft aus oi haben (: ai. methi-li „Pfeiler, Pfosten“?? Fay AsPh.
34, 3001; s. u, mei- „Pfahl*‘).
   tJber lat. mutus und andere von Brugmann Festschrift f. Thomsen 6
und Holthausen aaO. angereihte AYorte fiir ,,stumm“ (angeblich aus .,sturapf*‘)
s. u. 7nu- Schallwort.                —
                           Dt. 31oite usw. (s. u. mat- „beiBendes Gewlirm'*)
hat trotz Falk-Torp.                  u.   marh III fernzubleiben.

muro- ..groBe Anzahl“.
                   viel, unendlich*. fAvoioi ,,10 000*' nach Stokes BE. 19,
   Gv, uvQiog ,,sehr
97, KZ. 40. 249 zu dem  zwar sparlich belegten, aber doch wohl gesicherten
mir. ynar „Uberfiu6" (cymr.                      myrdd 10000 ist lat. myria-s.        -dem,    s.    Peder-
sen II 131 >


nius „Maus“.
   Ai. mas- „Maus, Eatte“ {muia-, musaha-^ mtmka- m. ds.), np. mus „Maus“;
   arm. ynu-kn „Mau&" (Hiibschmann Arm.                             St. I 44,   Arm. Gr. I 475, Brug-
mann IP L 4S3);
  gr. yvg „Maus“ {yvbg^ nvv nach eg, ""vog, bv)', alb. mi „Mau
```


## [2026-09-07T17:46:51.147Z] TOOL CALL #64: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T17:46:51.190Z] TOOL RESULT

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


## [2026-09-07T17:46:58.698Z] AGENT

Now I'll write the verification file.


## [2026-09-07T17:47:01.577Z] TOOL CALL #65: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg344.png data/verification/sources/refs/ocr/BOOK/344.png && ls -la data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-07T17:47:01.643Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-07T17:57:47.591Z] TOOL CALL #66: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk344.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_MOHR = \"https://en.wiktionary.org/wiki/%D9%85%D9%87%D8%B1\"\nW_MUDRA = \"https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A5%81%E0%A4%A6%E0%A5%8D%E0%A4%B0%E0%A4%BE\"\nW_MUM = \"https://en.wiktionary.org/wiki/%D9%85%D9%88%D9%85\"\nE_MUMMY = \"https://www.etymonline.com/word/mummy\"\nE_MOGUL = \"https://www.etymonline.com/word/mogul\"\nE_MUMMERY = \"https://www.etymonline.com/word/mummery\"\nA_MUK = \"https://abadis.ir/fatofa/%D9%85%D9%88%DA%A9/\"\n\ndata = {\n \"pdf_page\": 344,\n \"book_page\": 314,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": []\n}\n\n# ---------------- ENTRY 0 : Muk ----------------\ne0 = {\n \"entry\": 0,\n \"root\": \"Mŭk\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE (marginal) *mūk- 'heap, lump' (Pokorny 752; Walde-Pokorny II 311 s.v. mūkeu-); Mann's *mūkō(n) / *mūkró- 'pike, spike, peak, pile' (IEC 814)\",\n \"note\": (\"The root box is a faithful merger of Nourai's two citations. Pokorny p.752 has 'Root/lemma: mūk-, \"\n   \"Meaning: heap, etc.', built only on the Hesychian gloss Gr. μυκών · σωρός ἀχύρων 'heap of chaff' plus Germanic \"\n   \"(ON mūgi/mūgr, OE mūga/mūha/mūwa, MLG mūke, Du. muik, MHG mūche/mocke, Norw. mukka, ON mūstr, OE mēagol) and a Gaulish \"\n   \"place-name element *mukina 'cairn'; Pokorny ends 'after Hubschmid ZrPh. 66, 33 f. NOT Indo-Germanic'. Watkins/AHD nevertheless \"\n   \"keeps it ('mūk-. A heap.'). The 'peak, spike' half of Nourai's gloss comes from Mann alone, who reconstructs *mūkō(n)/*mūkró- \"\n   \"'pike, spike, peak, pile' and adds Lat. mūcrō 'sword-point' and Persian mūk 'sting'. So: the root is real in the cited \"\n   \"literature and the language label 'Indo-European' is what POK/AHD/IEC assert, but it is a lexically thin, chiefly Germanic \"\n   \"root whose IE antiquity is expressly contested, and the semantic bridge 'heap' <-> 'spike' is Mann's own. Verdict plausible, not confirmed.\"),\n \"note_fa\": (\"این ریشه در پوکورنی (ص ۷۵۲) به صورت *mūk- به معنای «توده، انبوه» آمده و تنها بر پایهٔ یک واژهٔ یونانی \"\n   \"در فرهنگ هزیخیوس (μυκών «تودهٔ کاه») و چند واژهٔ جرمنی استوار شده است؛ خود پوکورنی در پایان می‌نویسد به نوشتهٔ \"\n   \"هوبشمید این ریشه هندواروپایی نیست. معنایی که نورایی می‌دهد («توده، قله، نیش») دقیقاً از فرهنگ مقایسه‌ای من (IEC ۸۱۴) \"\n   \"گرفته شده که ستاک *mūkō(n) را بازسازی می‌کند. پس: ادعای نورایی با احتیاط پذیرفتنی است؛ ریشه در منابع او \"\n   \"وجود دارد ولی اعتبار هندواروپایی‌بودنش مورد تردید است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:752\", \"status\": \"supports\",\n    \"note\": (\"POK_full.txt (grep 'Root / lemma: muk-'): \\\"Root / lemma: muk- | Meaning: heap, etc.. Material: Gr. μυκών σωρός \"\n      \"ἀχύρων Hes.; ... Old Icelandic mugi, mugr 'heap'... Old English muga m. '(corn, grain-) heap', muha ds. (also muwa) ... \"\n      \"Middle High German mocke m. 'clump, gobbet' ... References: WP. II 311; after Hubschmid ZnPh. 66, 33 f. not Indo Germanic. Page(s): 752\\\". \"\n      \"Page number exact; gloss is 'heap', not 'pile, peak, spike'.\")},\n   {\"ref\": \"IEC:814\", \"status\": \"supports\",\n    \"note\": (\"IEC.txt printed p.814 (page marker line 11362): \\\"mūkóo(n) (mūkró-) 'pike, spike, peak, pile'. WP II, 311  Per. mūk 'sting'; \"\n      \"Hes. mūkon 'pile'; Lat. cf. (variant) mūcro ... 'point of sword'; OE mūha, mūga, wm 'pile, rick'. (Not also R mys 'headland' if *-k- as in Per. mūk)\\\". \"\n      \"This is verbatim the source of Nourai's root gloss AND of his Persian node.\")}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II p.311 (WLD_Bd2_pages.txt leaf 315)\", \"stance\": \"supports\",\n    \"note\": (\"\\\"mūkeu- 'Haufe' und Zubehör. Gr. μυκών · σωρός ἀχύρων Hes. nach Persson Beitr. 221 f. = aisl. mūgi 'Haufen (Heu), große Menge \"\n      \"(Menschen)', (auch mūgr), ags. mūga '(Korn-)Haufen', mūha ds. (auch mūwa) ... mnd. mūke, ndl. muik, mhd. mūche, nhd. Mauke ... mhd. mocke m. \"\n      \"'Klumpen, Brocken'\\\" — same material as Pokorny, gloss 'Haufe' (heap) only; no Persian and no 'spike'.\")},\n   {\"src\": \"AHD\", \"where\": \"Watkins appendix s.v. mūk- (AHD_watkins1985.txt line 763)\", \"stance\": \"supports\",\n    \"note\": (\"\\\"mūk-. A heap. Germanic *mūgōn-, *mūhōn- in: a. Old English mūga, mūha, mūwa, heap of grain: MOW1; b. Old Norse mūgi, heap, \"\n      \"akin to the probable Scandinavian source of MOGUL1. [Pok. mūk- 752.]\\\" — keeps the root but glosses it only 'a heap'.\")},\n   {\"src\": \"IEC\", \"where\": \"p.814 s.v. mūkóo(n)\", \"stance\": \"supports\",\n    \"note\": \"Mann is the only one of the four who gives the 'pike, spike, peak, pile' gloss and who puts Persian mūk in the group.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"mūk\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Nourai's Persian موک mūk 'sting' is taken straight from Mann, IEC 814, who lists 'Per. mūk \\\"sting\\\"' beside OE mūha/mūga 'pile, rick' \"\n   \"and Lat. mūcrō 'sword-point' under *mūkō(n)/*mūkró- 'pike, spike'. The Persian word itself is a lexicographers' word, not a textually secure one: \"\n   \"Borhan-e Qate' (BQT p.2054) enters it as موکه mūka — 'بضم اول بروزن غوک، مطلق نیش را گویند خواه نیش عقرب باشد و خواه نیش چیزهای دیگر' \"\n   \"(any sting, of a scorpion or of anything else) — and Mo'in's footnote to that very page says the reliable lexica read the word as میش \"\n   \"'ewe' (with mīm) and that Borhan has corrupted the meaning, and that the single shāhid, from ʿAjdi, 'does not look right'. Dehkhoda keeps \"\n   \"'sting' (citing Borhan and Nāẓem al-Aṭebbā), Mo'in's own Farhang gives 'میش'. Even if the word is genuine, no independent Iranist derives it \"\n   \"from the Germanic 'heap' root; a New Persian mūk would have to go back to Old Iranian *mūka-, for which there is no Avestan/Old Persian or \"\n   \"Middle Persian witness. So the arrow rests on Mann alone.\"),\n \"derivation_fa\": (\"واژهٔ «موک» به معنای «نیش» تنها از راه فرهنگ‌نامه‌ها به ما رسیده است: برهان قاطع (ص ۲۰۵۴) سرمدخل را \"\n   \"«موکه» می‌آورد و معنی می‌کند «مطلق نیش، خواه نیش عقرب باشد و خواه نیش چیزهای دیگر»؛ امّا معین در حاشیهٔ همان صفحه \"\n   \"می‌نویسد در کتب معتبره این واژه به معنی «میش» (با میم) است و برهان در معنا تحریف کرده و شاهد عجدی هم درست \"\n   \"نمی‌نماید. دهخدا معنی «نیش» را نگاه داشته و فرهنگ معین «میش» داده است. پیوند این واژه با ریشهٔ جرمنی \"\n   \"«توده» تنها حدس من (IEC) است؛ نه صورتی اوستایی/پارسی باستان و نه فارسی میانه‌ای برای آن در دست است. \"\n   \"بنابراین ادعای نورایی با احتیاط پذیرفتنی است.\"),\n \"sources\": [A_MUK],\n \"ref_check\": [\n   {\"ref\": \"IEC:814\", \"status\": \"supports\",\n    \"note\": \"IEC p.814: \\\"mūkóo(n) (mūkró-) 'pike, spike, peak, pile'. WP II, 311  Per. mūk 'sting'\\\" — Nourai's node is Mann verbatim.\"},\n   {\"ref\": \"MON:4445\", \"status\": \"not_checked\",\n    \"note\": (\"Mo'in's 6-volume Farhang-e Farsi is not online in any page-mappable form (refs_online.json MON: only the 2-vol Adena condensation, no page breaks), \"\n      \"so p.4445 cannot be located. Grepping MON_part1/2.txt for موک returned only موکل/موکب/دموکراسی etc., no headword موک. abadis.ir reports Mo'in's gloss for موک as 'میش'.\")}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"p.2054 headword موکه + Mo'in's footnote 4 on the same page (ref_page.py BQT:2054, pdf p.137)\", \"stance\": \"partial\",\n    \"note\": (\"Text: 'موکه بضم اول بروزن غوک، مطلق نیش را گویند خواه نیش عقرب باشد و خواه نیش چیزهای دیگر'. Mo'in's note: \"\n      \"'«موکه. بواو معروف» در برهان نیش عقرب و امثال آن، لیکن در کتب معتبره بمعنی «میش» است بمیم که جانوری است معروف، درین \"\n      \"صورت تحریف در معنی کرده ... «موکه» میش بود «لغت فرس ۳۰۳» و شاهدی از عجدی آورده که درست نمی‌نماید.' — i.e. the \"\n      \"form is موکه and the 'sting' sense is judged a corruption of 'میش' (ewe).\")},\n   {\"src\": \"MON\", \"where\": \"via abadis.ir/fatofa/موک (فرهنگ معین section) and Dehkhoda on the same page\", \"stance\": \"partial\",\n    \"note\": (\"Dehkhoda s.v. موک: 'نیش جانوران گزنده مانند کژدم' citing نازم الاطبا and برهان, with the note that the reading نیش vs میش is disputed; \"\n      \"Farhang-e Mo'in there gives 'میش'. Confirms the word exists in the Persian lexica but not its meaning.\")},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'muk'/'mūk'\", \"stance\": \"silent\",\n    \"note\": \"Horn's Grundriss has no entry for a Persian mūk 'sting' (nos. 1000-1003 cover mihr, muhr, mihmān, mei); the word is absent from his New Persian etymological corpus.\"},\n   {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt, grep موک\", \"stance\": \"silent\",\n    \"note\": \"Aryanpur's Persian IE-roots dictionary has no موک headword (only the unrelated آدارموک line).\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Germanic\", \"words\": \"mūgôn, mūhôn\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Proto-Germanic *mūgōn- / *mūhōn- 'heap' is exactly the pair Watkins prints under mūk- in the AHD appendix, the -g- ~ -h- doublet \"\n   \"being the regular Germanic outcome of intervocalic PIE *-k- after a long vowel by Verner's law variation (*mūkón- > *mūgôn-, unaccented, \"\n   \"vs. *mūḳ-ón- > *mūhôn-). The forms are reconstructed from OE mūga / mūha / mūwa 'heap of corn', ON mūgi / mūgr 'heap of hay, crowd', \"\n   \"Swedish dial. moa 'to pile up' (< *mūhōn), OHG mū-werf 'mole' (lit. 'heap-thrower').\"),\n \"derivation_fa\": (\"صورت جرمنی آغازین *mūgōn-/*mūhōn- به معنی «توده» همان است که واتکینز در پیوست ریشه‌های هندواروپایی AHD زیر \"\n   \"*mūk- می‌آورد؛ دوگانگی g ~ h پیامد قانون ورنر است. گواه‌ها: انگلیسی کهن mūga/mūha، نورسی کهن mūgi/mūgr و \"\n   \"سوئدی گویشی moa. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD:1530\", \"status\": \"supports\",\n    \"note\": (\"Watkins/AHD s.v. mūk-: \\\"Germanic *mūgōn-, *mūhōn- in: a. Old English mūga, mūha, mūwa, heap of grain: MOW1; b. Old Norse mūgi, heap...\\\" \"\n      \"(AHD_watkins1985.txt line 763). p.1530 is the right neighbourhood of the m- roots in the New College Edition appendix (pp.1505-1550).\")}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p.752 s.v. mūk-\", \"stance\": \"supports\",\n    \"note\": \"\\\"Old Icelandic mugi, mugr 'heap, bulk, mass'. Old English muga m. '(corn, grain-) heap', muha ds. (also muwa), compare further Swedish dial. moa 'pile up' (*mōhōn), Old High German mū-werf 'mole'\\\".\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p.311 s.v. mūkeu-\", \"stance\": \"supports\",\n    \"note\": \"\\\"aisl. mūgi 'Haufen (Heu), große Menge (Menschen)', (auch mūgr), ags. mūga '(Korn-)Haufen', mūha ds. (auch mūwa), vgl. weiter schwed. mdartl. moa 'zusammenhäufen' (*mūhōn)\\\".\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. mow 'a stack of hay' (KLN_1966.txt line 24545)\", \"stance\": \"supports\",\n    \"note\": \"\\\"fr. OE. mūga, mūha, 'a heap, pile', rel. to ON. mūgi, mūgr, of s.m., ON. mūstr (for *mūhstr), 'crowd', Swed. moa, 'to crowd together'\\\".\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"English\", \"words\": \"mow\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English mow(2) 'heap of grain, hay stored in a barn' descends by straight inheritance from OE mūga (also mūha, mūwa) 'heap', \"\n   \"Middle English mowe / mow; the -g-/-h- was lost between vowels in late OE and the vowel was later diphthongised to /ou/ in the \"\n   \"Great Vowel Shift, giving modern /mou/. It is a homograph of, but unrelated to, mow 'to cut grass' (OE māwan, PIE *mē-) and mow \"\n   \"'grimace' (OF moe). Nourai's arrow Germanic > English is the standard one; only the intermediate step 'Old English mūga' is omitted from the chart.\"),\n \"derivation_fa\": (\"واژهٔ انگلیسی mow به معنی «تودهٔ غلّه در انبار» مستقیماً از انگلیسی کهن mūga/mūha برجا مانده است: همخوان \"\n   \"میان‌واکه‌ای افتاد و واکهٔ کشیده در تحول بزرگ واکه‌ها به /ou/ بدل شد. باید توجه داشت که این واژه با mow «درو کردن» \"\n   \"(از ریشهٔ *mē-) هم‌ریشه نیست. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD appendix s.v. mūk-: \\\"Old English mūga, mūha, mūwa, heap of grain: MOW1\\\"; the AHD index line confirms \\\"mow! mūk-\\\" (AHD_watkins1985.txt line 1895).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. mow, n., 'a stack of hay'\", \"stance\": \"supports\",\n    \"note\": \"\\\"ME. mowe, mow, fr. OE. mūga, mūha, 'a heap, pile' ... prob. cogn. with Gk. μυκῶν (Hesychius), 'heap'\\\".\"},\n   {\"src\": \"POK\", \"where\": \"p.752\", \"stance\": \"supports\",\n    \"note\": \"\\\"Old English muga m. '(corn, grain-) heap', muha ds. (also muwa)\\\" — the OE ancestor of mow.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Old Norse\", \"words\": \"mūgi\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Old Norse mūgi m. 'swath, heap (of hay)', beside mūgr 'crowd, throng', is the West-Norse reflex of Proto-Germanic *mūgōn-, \"\n   \"so a sister of OE mūga rather than a separate branch of the root; Nourai draws it straight from the root box, which AHD also does \"\n   \"(it lists ON mūgi under mūk- alongside the Germanic forms). ON mūstr 'great crowd' (< *mūh-stra-) shows the -h- variant in the same paradigm.\"),\n \"derivation_fa\": (\"نورسی کهن mūgi «تودهٔ کاه/گیاه» و mūgr «انبوه مردم» بازماندهٔ همان *mūgōn- جرمنی است؛ پس در حقیقت خواهرِ \"\n   \"mūgaی انگلیسی کهن است نه شاخه‌ای جداگانه از ریشه. پوکورنی، والدهٔ-پوکورنی و AHD هر سه این صورت را اینجا \"\n   \"می‌آورند. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD:1530\", \"status\": \"supports\",\n    \"note\": \"\\\"b. Old Norse mūgi, heap, akin to the probable Scandinavian source of MOGUL1. [Pok. mūk- 752.]\\\" — exactly Nourai's node and its child.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p.752\", \"stance\": \"supports\", \"note\": \"\\\"Old Icelandic mugi, mugr 'heap, bulk, mass' ... Old Icelandic mūstr 'big, giant bulk, mass' (*muh-stra-)\\\".\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p.311\", \"stance\": \"supports\", \"note\": \"\\\"aisl. mūgi 'Haufen (Heu), große Menge (Menschen)', (auch mūgr)\\\".\"},\n   {\"src\": \"IEC\", \"where\": \"p.812 s.v. mūgh- (1)\", \"stance\": \"partial\",\n    \"note\": \"Mann puts \\\"ON mūgr, m. 'crowd, mob'; mūgi, m. 'swath, crowd'; Norw. muge 'crowd'\\\" under a different root, *mūgh- 'press, squeeze, pound', not under his mūkóo(n) — so the Norse word's root assignment is not uniform even inside Nourai's own sources.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"mogul\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"English mogul 'a hard mound of snow on a ski slope' is first recorded in 1961 in American skiing jargon; it is generally \"\n   \"taken from a Scandinavian or Bavarian dialect word for 'mound' — Norwegian dial. mugje f., muga 'a heap, a mound' (the modern \"\n   \"continuation of ON mūgi) or South German dial. Mugel 'hillock'. Nourai's arrow Old Norse mūgi > English mogul is therefore right in \"\n   \"substance but compressed: the transmission is not from Old Norse into English but from a living 20th-c. Norwegian (or Alpine German) \"\n   \"dialect word into ski vocabulary, and AHD itself hedges — 'akin to the PROBABLE Scandinavian source of MOGUL1'. Homonymous mogul \"\n   \"'magnate' (< Pers./Ar. muḡal 'Mongol') is unrelated.\"),\n \"derivation_fa\": (\"mogul در انگلیسی به معنی «پشتهٔ برف در پیستِ اسکی» نخستین بار در ۱۹۶۱ در زبان اسکی‌بازان امریکایی ثبت شده و \"\n   \"معمولاً وام‌واژه‌ای از گویشِ نروژی mugje/muga «توده، پشته» (بازماندهٔ همان mūgi نورسی کهن) یا از آلمانی جنوبی \"\n   \"Mugel دانسته می‌شود. پس پیکانِ نورایی در ماده درست است ولی مسیر وام‌گیری را خلاصه کرده؛ خود AHD هم «احتمالاً» \"\n   \"می‌گوید. با احتیاط پذیرفتنی است.\"),\n \"sources\": [E_MOGUL],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": (\"AHD appendix s.v. mūk-: \\\"Old Norse mūgi, heap, AKIN TO THE PROBABLE Scandinavian source of MOGUL1\\\"; index \\\"MOGUL! mūk-\\\". \"\n      \"So AHD assigns the word to the root but marks the Scandinavian source as merely probable and does not derive it from ON directly.\")}\n ],\n \"consulted\": [\n   {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/mogul (mogul n.2)\", \"stance\": \"partial\",\n    \"note\": \"\\\"'elevation on a ski slope,' 1961, probably from Scandinavian sources (compare dialectal Norwegian mugje, feminine muga, meaning 'a heap, a mound'), or from southern German dialect mugel with the same meaning.\\\"\"},\n   {\"src\": \"POK\", \"where\": \"p.752\", \"stance\": \"silent\", \"note\": \"Pokorny lists Norwegian dial. mukka 'heap, bulk, mass' and Swiss mauch 'unordentlicher Haufe' under the root, but of course says nothing about the English ski term.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6, \"lang\": \"Dutch\", \"words\": \"mocke; male-mocke\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"The Dutch node as drawn cannot be sustained. (a) A Dutch/Middle High German mocke does belong to this root — Pokorny p.752 \"\n   \"lists 'Middle Low German muke, Dutch muik, Middle High German mūche ... Middle High German mocke m. \\\"clump, gobbet\\\"' — but its \"\n   \"meaning is 'lump, clod, excrescence', never the vague 'thing' Nourai prints. (b) The compound 'male-mocke = \\\"silly thing\\\", a bird' is \"\n   \"not a Dutch word at all: the bird-name is Dutch mallemok, and every independent authority analyses it as mal 'foolish, silly' + mok \"\n   \"'gull, seamew', i.e. 'silly GULL', not 'silly thing'. Klein: \\\"Du. mallemok, compounded of mal, 'foolish', and mok, 'gull, seamew'; \"\n   \"so called because it is easily caught\\\"; Webster's 2nd: \\\"[D. mallemok, from mal, foolish, and mok, a gull]\\\". (c) Watkins/AHD, \"\n   \"Nourai's own cited authority, assigns MALLEMUCK not to mūk- but to root mel-7 'to miss, deceive' via Middle Dutch mal 'foolish'. \"\n   \"The 'thing' gloss looks like a misreading of a dictionary entry in which mok was glossed separately.\"),\n \"derivation_fa\": (\"این گره پذیرفتنی نیست. درست است که واژه‌ای هلندی/آلمانی میانه mocke/muik به معنی «گلوله، \"\n   \"تکه، برآمدگی» زیر این ریشه در پوکورنی (ص ۷۵۲) آمده است، امّا معنای «چیز» برای آن در هیچ منبعی نیست. \"\n   \"نام آن مرغ در هلندی mallemok است و همهٔ منابع مستقل (کلاین، وبستر، AHD) آن را mal «احمق» + mok «مرغ دریایی، \"\n   \"کاکایی» تحلیل می‌کنند، یعنی «کاکاییِ احمق» نه «چیزِ احمق». پژوهش امروزی این ادعا را رد می‌کند.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD:1530\", \"status\": \"contradicts\",\n    \"note\": (\"The AHD entry for mūk- on that page contains no Dutch word at all: \\\"mūk-. A heap. Germanic *mūgōn-, *mūhōn- in: a. Old English mūga ...: MOW1; \"\n      \"b. Old Norse mūgi, heap, akin to the probable Scandinavian source of MOGUL1.\\\" Instead AHD prints \\\"mel-7. To miss, deceive. Germanic *mal- in \"\n      \"Middle Dutch mal, foolish, silly: MALLEMUCK. [Pok. 2. mel- 719.]\\\" and its index reads \\\"MALLEMUCK mel-7\\\" (AHD_watkins1985.txt lines 763, 736, 1806).\")}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p.752 s.v. mūk-\", \"stance\": \"partial\",\n    \"note\": \"\\\"Middle Low German muke, Dutch muik, Middle High German mūche, Modern High German Mauke ... Middle High German mocke m. 'clump, gobbet' (with it identical is Middle High German mocke 'Zuchtsau')\\\" — a Dutch/German mocke 'lump' exists here, but glossed 'clump', and no compound with mal.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. mallemuck (KLN_1966.txt line 22680, printed p.928)\", \"stance\": \"contradicts\",\n    \"note\": \"\\\"mallemuck, mallemock, mallemoke, n., fulmar, petrel. — Du. mallemok, compounded of mal, 'foolish', and mok, 'gull, seamew'; so called because it is easily caught.\\\"\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict., vol. 1 s.v. mallemuck\", \"stance\": \"contradicts\",\n    \"note\": \"\\\"mal'le-muck, n. [D. mallemok, from mal, foolish, and mok, a gull] any one of several species of large ocean bird ... also written mallemock, mallemoke.\\\"\"},\n   {\"src\": \"IEC\", \"where\": \"p.815 s.v. muks- (1)\", \"stance\": \"partial\",\n    \"note\": \"Mann puts German \\\"Mocke 'breeding sow'\\\" under muks- 'snout; pig' as a Celtic loanword — again not under his mūkóo(n), and again nothing about a bird.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 7, \"lang\": \"English\", \"words\": \"mallemuck\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"English mallemuck (also mallemock, mallemoke) 'fulmar, albatross' is a 17th-19th c. sailors' borrowing of Dutch mallemok, \"\n   \"picked up in the Arctic whaling trade; the Dutch compound is mal 'foolish' + mok 'gull', the bird being called silly because it was so \"\n   \"easily caught. The second element is therefore Dutch mok 'gull', which no source connects with the 'heap' root; Watkins assigns the \"\n   \"English word to PIE mel-7 'to miss, deceive' on account of the FIRST element. Nourai's chain mūk- 'pile' > Dutch mocke 'thing' > \"\n   \"mallemuck is thus wrong at both links, though the word itself and its Dutch source are correctly identified.\"),\n \"derivation_fa\": (\"mallemuck در انگلیسی نام مرغی دریایی (فولمار/آلباتروس) و وام‌واژه‌ای از هلندی mallemok است که \"\n   \"دریانوردان در شکار نهنگ در شمال فراگرفتند؛ این ترکیب از mal «احمق» و mok «کاکایی» ساخته شده، زیرا این مرغ \"\n   \"به‌آسانی به دام می‌افتاد. واتکینز این واژه را به ریشهٔ mel-7 «فریب دادن» منسوب می‌کند، نه به *mūk-. \"\n   \"پژوهش امروزی زنجیرهٔ نورایی را رد می‌کند.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"contradicts\",\n    \"note\": \"AHD index: \\\"MALLEMUCK mel-7\\\"; entry mel-7: \\\"To miss, deceive. Germanic *mal- in Middle Dutch mal, foolish, silly: MALLEMUCK. [Pok. 2. mel- 719.]\\\" — not under mūk-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. mallemuck\", \"stance\": \"contradicts\",\n    \"note\": \"\\\"Du. mallemok, compounded of mal, 'foolish', and mok, 'gull, seamew'\\\" — the second element is 'gull', so the word has no link to a 'heap/pile' root.\"},\n   {\"src\": \"WEB\", \"where\": \"vol. 1 s.v. mallemuck\", \"stance\": \"contradicts\",\n    \"note\": \"\\\"[D. mallemok, from mal, foolish, and mok, a gull]\\\".\"},\n   {\"src\": \"POK\", \"where\": \"p.752\", \"stance\": \"silent\", \"note\": \"Pokorny's mūk- article knows no bird-name and no Dutch mallemok.\"}\n ]\n})\n\ndata[\"entries\"].append(e0)\n\n# ---------------- ENTRY 1 : Mum ----------------\ne1 = {\n \"entry\": 1,\n \"root\": \"Mŭm\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"New Persian موم mūm 'wax' < Middle Persian *mōm\",\n \"note\": (\"The root box is right: موم mūm is the ordinary Persian word for 'wax' (and for a wax candle), continued in Kurdish mūm, \"\n   \"Mazandarani/Tabari and Gilaki mūm, and borrowed into Armenian (mom), Ottoman Turkish (mum 'candle') and Arabic (mūm 'yellow wax'). \"\n   \"Mo'in's footnote to BQT p.2055 gives exactly this dossier. Its own ultimate origin is unsettled — Wiktionary derives it from Middle \"\n   \"Persian *mōm and floats a Semitic source (Proto-Semitic *māy- 'water, liquid, sap', cf. Akkadian mū) — but that does not affect any arrow \"\n   \"on this chart, which starts from Persian.\"),\n \"note_fa\": (\"ریشهٔ این نمودار درست است: «موم» واژهٔ فارسی معمول برای شمع و موم است و در کردی، طبری و گیلکی نیز \"\n   \"همین صورت را دارد؛ معین در حاشیهٔ برهان قاطع (ص ۲۰۵۵) همین شواهد را می‌آورد و می‌افزاید که در عربی نیز \"\n   \"«موم هو الشمع الاصفر». از فارسی میانهٔ *mōm برجا مانده است؛ دربارهٔ خاستگاه دورترِ آن (احتمال وام‌گیری \"\n   \"از سامی) اختلاف هست، ولی به پیکان‌های این نمودار ربطی ندارد. ادعای نورایی درست است.\"),\n \"sources\": [W_MUM],\n \"ref_check\": [\n   {\"ref\": \"BQT:2055\", \"status\": \"supports\",\n    \"note\": (\"ref_page.py BQT:2055 (BQT_v4 pdf p.138), Mo'in's footnote 2: 'موم - بضم اول، کردی mūm (شمع) «ژابا ص ۲۶۹»، طبری mūm (موم) \"\n      \"«واژه‌نامه ۷۶۹»، گیلکی mūm (موم)؛ در عربی نیز موم: «موم هو الشمع الاصفر» ... مادهٔ نرمی که با عسل مخلوط است و \"\n      \"بوسیلهٔ تصفیه آن را از عسل جدا کنند'. Page number exact and the sense 'wax' confirmed.\")}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"p.2055 footnote 7 (مومیائی)\", \"stance\": \"supports\",\n    \"note\": \"'و نام مومیا مشتق از «موم» (ه.م.) فارسی است «عقار ۲۴۴ ف»' — Mo'in himself derives mūmiyā from Persian mūm, i.e. the next arrow of the chart.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1510 (LKT.txt line 3473)\", \"stance\": \"supports\",\n    \"note\": \"\\\"1510. Pers. mūm: 'Wachs', ebenso tk. mūm 'dass., Kerze', hieraus serb. mum 'Kerze' ... kat. sp. momia 'Pech und Asphalt'\\\".\"},\n   {\"src\": \"PLA\", \"where\": \"p.254 (leaf 269 of PLA_pages.txt)\", \"stance\": \"supports\",\n    \"note\": \"\\\"mūm: 'Wachs' pers. ...\\\" heads the entry immediately before mūmiyā, Asbaghi treating mūm as the Persian base.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Arabic\", \"words\": \"mŭmîya\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Persian مومیا mūmiyā (مومیایی mūmiyāʾī), a -iyā derivative of موم mūm 'wax', denoted the bituminous drug (pissasphalt, \"\n   \"'mineral pitch') believed to exude from corpses preserved in mountain caves and used as a wound-drug and embalming material; it was \"\n   \"taken into Arabic as مومیا / مومیاء mūmiyā(ʾ) with the shifted sense 'embalmed corpse, mummy' and a by-form umiyya. Asbaghi's \"\n   \"Persische Lehnwörter im Arabischen p.254 states it flatly: \\\"mūmiyā: 'Mumie' aus pers. mūm ... ar. mūmiyā < pers. mūm 'Wachs'\\\", with \"\n   \"Mandaic mumia and Syriac cognate loans; the Arabic form is then the immediate source of Medieval Latin mumia. Mo'in (BQT p.2055 n.7) \"\n   \"says the same and adds that in Arabic مومیا means 'داروی حنوط' and مومیائی 'al-mūmiya al-qubūriyya'.\"),\n \"derivation_fa\": (\"«مومیا» و «مومیایی» در فارسی مشتقی از «موم» است و به قیرِ معدنی و دارویی گفته می‌شد که می‌پنداشتند از \"\n   \"پیکرهای مانده در غارها می‌تراود؛ همین واژه به عربی راه یافت (مومیا / مومیاء) و در آن زبان تحول معنایی یافت \"\n   \"و بر «جسد حنوط‌شده» دلالت کرد. اسباغی (ص ۲۵۴) و حاشیهٔ معین بر برهان قاطع (ص ۲۰۵۵) هر دو همین را \"\n   \"می‌گویند. ادعای نورایی درست است.\"),\n \"sources\": [E_MUMMY],\n \"ref_check\": [\n   {\"ref\": \"PLA:254\", \"status\": \"supports\",\n    \"note\": (\"PLA_pages.txt leaf 269 = printed p.254 (header 'mūg ... 254 ... maybuhtag'): \\\"- umiyā: 'Mumie' aus pers. mūm 'eine durch Austrocknen od. \"\n      \"Einbalsamieren vor der Verwesung geschützte Leiche' ... ar. mūmiya < pers. mūm 'Wachs'. Mumie: pers. > ar. > it.\\\" — page exact, claim exact.\")},\n   {\"ref\": \"AFM:148\", \"status\": \"not_found\",\n    \"note\": (\"Addi Shir's al-Alfāẓ al-fārisiyya al-muʿarraba: searched AFM_pages.txt and AFM.txt for موم/مومیا/مومیاء — no hit; the Arabic OCR of this scan is \"\n      \"heavily corrupted (Syriac glyph substitutions) and the leaves that correspond to printed p.148 (leaves 154-158) are in the نون section \"\n      \"(نارمشک، نشادر، نیل، نیلوفر), so either the offset or the citation is off by a few pages. ref_page.py reports no scan covering AFM:148.\")}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no. 1510\", \"stance\": \"supports\",\n    \"note\": \"\\\"Ar. mūmija 'einbalsamierter Leichnam' ist in dieser Bedeutung in alle europäischen Sprachen übergegangen: it. mummia, frz. momie, mumie, sp. momia, pg. mumia ... engl. mummy, ndl. mummie, dtsch. Mumie; russ. mumija.\\\"\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. mummy (KLN_1966.txt line 24656, printed p.1014)\", \"stance\": \"supports\",\n    \"note\": \"\\\"mummy, n., an embalmed body. — ME. mummie, fr. OF. (= F.) momie, fr. ML. mumia, fr. Arab. mumiyah, 'mummy', fr. Pers. mum, 'wax'.\\\"\"},\n   {\"src\": \"BQT\", \"where\": \"p.2055 footnote 7\", \"stance\": \"supports\",\n    \"note\": \"'و نام مومیا مشتق از «موم» فارسی است ... در عربی «مومیا» بمعنی داروی حنوط و نیز اجساد حنوط‌شده بکار رود'.\"},\n   {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/mummy\", \"stance\": \"supports\",\n    \"note\": \"\\\"from Medieval Latin mumia, which is perhaps from Greek moumia or directly from Arabic mumiyah 'embalmed body,' from Persian mumiya 'asphalt,' from mum 'wax.'\\\"\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Latin\", \"words\": \"mumia\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The Latin link is real but it is MEDIEVAL Latin, not classical: the drug reached the West through Arabic medical writing \"\n   \"(Ibn Sīnā, al-Rāzī) in the 11th-13th c. Latin translations, where mumia denotes the bituminous medicine; from it come Italian mummia, \"\n   \"Old French mumie/momie, Middle English mummie 'medicinal substance prepared from mummy tissue' (late 14c.). Klein and Etymonline both \"\n   \"route the word through ML mumia, so Nourai's [Latin] box is defensible; but his cited authority, Skeat, does not say Latin — Skeat goes \"\n   \"'O.F. mumie ... Ital. mummia ... Pers. mūmiyā ... Pers. mūm', i.e. via Italian. Hence plausible rather than confirmed, and the box \"\n   \"should read 'Medieval Latin'.\"),\n \"derivation_fa\": (\"حلقهٔ لاتین وجود دارد امّا لاتینِ قرون وسطاست نه لاتین کلاسیک: این دارو از راه ترجمهٔ لاتینیِ \"\n   \"کتاب‌های پزشکی عربی (ابن‌سینا، رازی) در سدهٔ ۵-۷ قمری/۱۱-۱۳ میلادی به اروپا رفت و به صورت mumia \"\n   \"درآمد؛ از آن ایتالیایی mummia و فرانسوی قدیم momie برآمده است. کلاین و اتیمولانلاین همین مسیر را \"\n   \"می‌دهند، ولی اسکیت — منبعی که نورایی ارجاع داده — ایتالیایی می‌آورد نه لاتین. پس با احتیاط پذیرفتنی است \"\n   \"و برچسب درستِ جعبه «لاتینیِ میانه» است.\"),\n \"sources\": [E_MUMMY],\n \"ref_check\": [\n   {\"ref\": \"SKT:340\", \"status\": \"partial\",\n    \"note\": (\"Skeat, s.v. Mummy (SKT.txt line 12023): \\\"Mummy. (F. - Ital. - Pers.) O.F. mumie, a mummy. — Ital. mummia. — Pers. mūmiyā, a mummy, embalmed \"\n      \"body. — Pers. mūm, wax, much used in embalming.\\\" So Skeat supports the Persian > Arabic-mediated > Romance chain but inserts ITALIAN, not Latin. \"\n      \"Note also that in the local scan (aconciseetymolo01skeagoog) this entry sits on the leaf whose running page number reads 198, not 340, so Nourai's \"\n      \"page number belongs to a differently paginated impression of the Concise.\")}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. mummy\", \"stance\": \"supports\",\n    \"note\": \"\\\"fr. OF. (= F.) momie, fr. ML. mumia, fr. Arab. mumiyah\\\" — Medieval Latin mumia is exactly Nourai's box, one step above French.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1510\", \"stance\": \"partial\",\n    \"note\": \"Lokotsch takes the Arabic word straight into the Romance languages (\\\"it. mummia, frz. momie ... engl. mummy\\\") without naming a Latin stage.\"},\n   {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/mummy\", \"stance\": \"supports\",\n    \"note\": \"\\\"late 14c., mummie ... from Medieval Latin mumia\\\".\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"A pass-through box with no word printed; the form intended is Old French mumie, later French momie 'mummy' (13c. as a drug \"\n   \"name, 16c. of the Egyptian corpses), taken from Medieval Latin mumia. French momie is the immediate source of Middle English mummie.\"),\n \"derivation_fa\": (\"این جعبه در کتاب بدون واژه است؛ صورت مورد نظر فرانسوی قدیم mumie و فرانسوی نو momie \"\n   \"است که از لاتینیِ میانه mumia گرفته شده و خود منشأِ مستقیمِ mummie در انگلیسی میانه است. ادعا درست است.\"),\n \"sources\": [E_MUMMY],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None); nothing of Nourai's to check.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. mummy and mummify\", \"stance\": \"supports\",\n    \"note\": \"\\\"ME. mummie, fr. OF. (= F.) momie\\\"; and s.v. mummify \\\"F. momifier, compounded of momie, 'mummy'\\\".\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1510\", \"stance\": \"supports\", \"note\": \"\\\"frz. momie, mumie\\\" listed among the Romance reflexes of Ar. mūmija.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"mummy, mummery\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"Two words, two different verdicts. MUMMY is confirmed: ME mummie (late 14c.) 'the bituminous drug', from OF/F momie, \"\n   \"sense 'embalmed Egyptian corpse' from the 1610s — Klein p.1014 s.v. mummy gives precisely Nourai's chain back to Pers. mūm. MUMMERY is \"\n   \"disputed and does not belong on this chart: it is MF/F momerie 'a dumb show, masquerade', from OF momeur 'mummer', from momer / mommer \"\n   \"'to mask oneself', of onomatopoeic origin (the nursery syllable mom/mum used to hush or frighten children) — the same family as mum, \"\n   \"mumble, mummer. Klein treats it in a separate article on the SAME page ('mummery, n., a dumb show. — MF. (= F.) momerie, fr. OF. momeur. \"\n   \"See prec. word', i.e. mum 'to act in dumb show'), and Etymonline likewise records no connection with mummy. The resemblance of \"\n   \"mummy / mummery is accidental and Nourai's chart makes it a folk-etymological merger.\"),\n \"derivation_fa\": (\"در این جعبه دو واژه گنجانده شده است. mummy درست است: انگلیسی میانه mummie (سدهٔ ۱۴م) از \"\n   \"فرانسوی momie و از همان زنجیرهٔ فارسی>عربی>لاتینیِ میانه. امّا mummery ربطی به «موم» ندارد: از \"\n   \"فرانسوی میانه momerie «نمایش بی‌زبان، نقاب‌بازی» از momer «نقاب بر چهره زدن» و از خانوادهٔ \"\n   \"واژگانِ آواواره mum/mumble است. کلاین هم در همان صفحه دو مدخلِ جداگانه دارد. پژوهش امروزی پیوند \"\n   \"mummery را با موم رد می‌کند و آن را ریشه‌شناسی عامیانه می‌داند.\"),\n \"sources\": [E_MUMMY, E_MUMMERY],\n \"ref_check\": [\n   {\"ref\": \"KLN:1014\", \"status\": \"partial\",\n    \"note\": (\"Klein p.1014 carries BOTH articles, and they are unrelated to each other: \\\"mummy, n., an embalmed body. — ME. mummie, fr. OF. (= F.) momie, \"\n      \"fr. ML. mumia, fr. Arab. mumiyah, 'mummy', fr. Pers. mum, 'wax'\\\" — supports mummy; and \\\"mummery, n., a dumb show. — MF. (= F.) momerie, fr. OF. \"\n      \"momeur. See prec. word\\\" (= mummer < momer 'to mask oneself'; Klein s.v. mum: \\\"prob. derives fr. the child's word momo, expressing astonishment\\\") \"\n      \"— contradicts mummery. So the reference supports one word of the node and refutes the other.\")}\n ],\n \"consulted\": [\n   {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/mummery and /word/mummy\", \"stance\": \"contradicts\",\n    \"note\": \"\\\"Mummery (noun, 1520s): 'a show or performance of mumming,' derived from Old French mommerie\\\"; the entry records no connection with mummy 'embalmed body'.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. Mummer / Mummy (SKT.txt lines 12016, 12023)\", \"stance\": \"contradicts\",\n    \"note\": \"Skeat keeps them apart too: \\\"mummer, a masker, buffoon. (F. — Du.) O.F. mommeur ... Der. mummer-y, O.F. mommerie\\\" under Mum, while Mummy is a separate article of Persian origin.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1510\", \"stance\": \"partial\",\n    \"note\": \"Lokotsch lists engl. mummy among the Arabic-Persian loans but not mummery.\"}\n ]\n})\n\ndata[\"entries\"].append(e1)\n\n# ---------------- ENTRY 2 : Mura ----------------\ne2 = {\n \"entry\": 2,\n \"root\": \"Mŭrâ\",\n \"verdict\": \"disputed\",\n \"modern_form\": \"Old/Proto-Iranian *mudrā- 'seal'; Khotanese Saka mūrā- 'coin; jewel' is a DESCENDANT of it, not its source\",\n \"note\": (\"The word in the root box is genuine and Nourai's gloss matches Bailey almost word for word — Bailey, Dictionary of Khotan Saka \"\n   \"(the accessible counterpart of Indo-Scythian Studies VI): \\\"mūrā- 1. 'name of a coin', and 2. 'jewel' ... corresponding to the Chinese \"\n   \"small copper coin ts'ien\\\", and 'Indo-Schythian' is Bailey's own label for Khotanese Saka. What is wrong is the DIRECTION. Bailey \"\n   \"continues in the same article: \\\"This mūra- is from mudrā- 'seal', Zor.P. mwdl, mwhlk *mudr, *muhrak, N.Pers. muhr, muhrah, M.Pers.T. \"\n   \"mwhr 'seal'\\\". Khotanese regularly loses the stop in such clusters (Bailey's own parallels in the neighbouring articles: mūra- 'bird' < \"\n   \"*mrga-, dāra- 'long' < *darga-, āra- 'price' < *arga-), so mūrā is the youngest, not the oldest, member of the family. The modern \"\n   \"reconstruction is Old Iranian *mudrā- 'seal', whence MP mwdl/muhr, Skt. mudrā- (a loanword: Junker IF 35, 1915, 273-88; Weber, cited by \"\n   \"Horn, already called Skt. mudrā 'Egyptian' and derived it from OP Mudrāya-), and Khotanese mūrā-; the ultimate source is probably not \"\n   \"Indo-European at all but Akkadian mušarû 'object bearing a royal inscription' < Sumerian mu-sar. The chart should therefore be inverted, \"\n   \"with an Old Iranian *mudrā- box at the top and Khotanese mūrā as one more branch.\"),\n \"note_fa\": (\"واژهٔ جعبهٔ ریشه واقعی است: بیلی در فرهنگ ختنیِ سکایی می‌نویسد mūrā- ۱) نام سکّه، ۲) گوهر؛ و \"\n   \"«هندوسکایی» هم نامی است که خود بیلی بر ختنی می‌نهاد. امّا سوی پیکان‌ها وارونه است: بیلی در همان مدخل \"\n   \"می‌افزاید که این mūra- از mudrā- «مهر» آمده است، زیرا در ختنی خوشهٔ -dr- به -r- کاهش می‌یابد (مانند \"\n   \"mūra- «مرغ» از *mrga- و dāra- «دراز» از *darga-). بازسازی امروزی ایرانی باستان *mudrā- است که فارسی میانهٔ \"\n   \"muhr، سنسکریتِ mudrā (وام‌واژه) و ختنی mūrā- از آن برآمده‌اند؛ خاستگاه دورتر احتمالاً اکدی mušarû و \"\n   \"سومری mu-sar است. پژوهش امروزی این جهت‌گذاری را رد می‌کند و نمودار باید وارونه شود.\"),\n \"sources\": [W_MOHR, W_MUDRA],\n \"ref_check\": [\n   {\"ref\": \"ISS:283\", \"status\": \"partial\",\n    \"note\": (\"Khotanese Texts VI itself is not online (refs_online.json ISS), so the exact page cannot be opened; the substance was checked in Bailey's own \"\n      \"Dictionary of Khotan Saka (ISS_alt_DKS.txt line 6185): \\\"mūrā- 1. 'name of a coin', and 2. 'jewel', plural mūre, later mura, muri, murai, \"\n      \"corresponding to the Chinese small copper coin ts'ien ... For mūra- 'jewel or precious thing', SuvO. 53r4 mūryau 'with jewels', BS maṇi- ... \"\n      \"This mūra- is from mudrā- 'seal', Zor.P. mwdl, mwhlk *mudr, *muhrak, N.Pers. muhr, muhrah, M.Pers.T. mwhr 'seal'.\\\" The word and gloss are \"\n      \"Bailey's; the claim that it is the SOURCE of the Iranian and Indian forms is not.\")}\n ],\n \"consulted\": [\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS s.v. mūrā- (and s.v. mūra- 'bird', dāra-, āra-)\", \"stance\": \"contradicts\",\n    \"note\": (\"Besides \\\"This mūra- is from mudrā- 'seal'\\\", Bailey's phonology in the surrounding entries makes the direction unmistakable: \\\"From *mrga- \"\n      \"'wild creature'\\\" (mūra- 'bird'), \\\"From darga- 'long', as āra- 'price' from arga-, but mūra- 'bird' from mrga-\\\" (dāra-). Khotanese simplifies \"\n      \"the cluster; it does not create -dr-.\")},\n   {\"src\": \"HRN\", \"where\": \"no. 1001, pp.224-225\", \"stance\": \"contradicts\",\n    \"note\": (\"Horn puts Sanskrit and Pahlavi at the top and knows nothing of a Khotanese source: \\\"1001. muhr 'Siegel; Siegelring'. skr. mudrā- 'Siegel, \"\n      \"Siegelring'; phlv. mutrōk d. i. mudrak 'Ring'(?) ... mudar, muhr 'Siegel' (PPGL)\\\"; and he adds \\\"Weber ... erklärt skr. mudrā für 'egyptisch', \"\n      \"aus ap. Mudrāya- entlehnt.\\\"\")},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. bahr and muhrak\", \"stance\": \"partial\",\n    \"note\": \"\\\"cf Skr mudrā : muhr 'seal'\\\" (under bahr) — Nyberg treats Skt mudrā and MP muhr as the pair to be compared, again with no Khotanese intermediary.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in's footnote 6 to BQT p.2062\", \"stance\": \"contradicts\",\n    \"note\": \"'مهر (بضم اول). سانسکریت mudrā (مهر، خاتم، حلقهٔ خاتم)، پهلوی mutrōk / mudrōk (حلقه؟)، mudar، muhr (مهر)، ارمنی murhak، آستی mysur ...' — the Iranian/Indian forms, no Khotanese ancestor.\"}\n ],\n \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"mutrâk, mudrâk; mudar, muhr\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"All four forms are real and Nourai has copied them, glosses included, from Horn no. 1001: 'phlv. mutrōk d. i. mudrak \"\n   \"\\\"Ring\\\"(?), vd. 2 (18) Gl.; mudar, muhr \\\"Siegel\\\" (PPGL)'. In Book Pahlavi spelling MacKenzie prints muhr [mwdl] 'seal' — the \"\n   \"graphic <d> beside the read /h/ is precisely the fossilised *mudr- — and muhrag [mwhlk'] 'bead, vertebra, piece (in backgammon)', \"\n   \"Manichaean MP and Parthian mwhr. Phonetically OIr. *mudra- > MP *mudr > muhr by the well-known Middle Persian change of intervocalic/\"\n   \"preconsonantal -d- to -h- before r (cf. MP māh < *mās-, and the doublet mudar ~ muhr which shows the two stages side by side); \"\n   \"mudrak / muhrak is the same stem with the diminutive/nominal suffix -ak. What is not plausible is the arrow: these Pahlavi forms are \"\n   \"the ancestors of, not the descendants of, Khotanese mūrā (see the root note). Horn himself flags 'Ring' with a question mark, and \"\n   \"MacKenzie glosses muhrag 'bead, vertebra, draughtsman' rather than 'ring', so that gloss is the weakest part of the box.\"),\n \"derivation_fa\": (\"هر چهار صورت واقعی اند و نورایی آن‌ها را عیناً از هرن (شمارهٔ ۱۰۰۱، ص ۲۲۴-۲۲۵) گرفته است. در \"\n   \"خط پهلوی کتابی مکنزی muhr را <mwdl> می‌نویسد که همان بازماندهٔ نوشتاریِ *mudr- است، و muhrag <mwhlk'> \"\n   \"«مهره، مهرهٔ پشت، مهرهٔ نرد». در فارسی میانه d در خوشهٔ -dr- به h بدل شده (دوگانهٔ mudar ~ muhr دو پلّهٔ \"\n   \"این دگرگونی را کنار هم نشان می‌دهد) و -ak پسوند است. ولی جهتِ پیکان وارونه است: این صورت‌های پهلوی \"\n   \"نیاکانِ mūrāی ختنی‌اند نه بازماندهٔ آن. معنی «حلقه» هم نامطمئن است: خود هرن پهلوی آن علامت سؤال \"\n   \"گذاشته است.\"),\n \"sources\": [W_MOHR],\n \"ref_check\": [\n   {\"ref\": \"KLN:993\", \"status\": \"contradicts\",\n    \"note\": (\"Klein p.993 s.v. mohur: \\\"Hind. muhur, muhr, fr. Pers. muhr, 'seal, coin', fr. OI. mudra, 'seal, coin'.\\\" Klein thus derives the Persian/Pahlavi \"\n      \"word FROM Sanskrit mudrā, i.e. he makes Nourai's Pahlavi box a borrowing from Nourai's Sanskrit box, and he knows no Khotanese/'Indo-Scythian' root at all.\")},\n   {\"ref\": \"ISS:284\", \"status\": \"partial\",\n    \"note\": \"Khotanese Texts VI p.284 is not accessible; Bailey's DKS article on mūrā- cites exactly these Pahlavi forms — \\\"Zor.P. mwdl, mwhlk *mudr, *muhrak, N.Pers. muhr, muhrah, M.Pers.T. mwhr 'seal'\\\" — but as the SOURCE of Khotanese mūra-, not as its offspring.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 1001, pp.224-225 (HRN.txt line 8703, leaf 238)\", \"stance\": \"supports\",\n    \"note\": \"\\\"1001. muhr 'Siegel; Siegelring'. skr. mudrā- 'Siegel, Siegelring'; phlv. mutrōk d. i. mudrak 'Ring'(?), vd. 2 (18) Gl.; mudar, muhr 'Siegel' (PPGL), chald. LW., arm. LW. murhak. LW. kurd. mōr; oss. mysur\\\" — the exact source of Nourai's four forms and their glosses.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.56 s.v. muhr / muhrag\", \"stance\": \"supports\",\n    \"note\": \"\\\"muhr [mwdl | M mwhr, N ~] seal.\\\" and \\\"muhrag [mwhlk' | P mwhrg, N ~a] bead, vertebra, piece (in backgammon, etc.).\\\" — confirms the forms; glosses muhrag as 'bead/vertebra/draughtsman', not 'ring'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.v. muhrak\", \"stance\": \"supports\",\n    \"note\": \"\\\"muhrak [mwhlk'] draughtsman (in the tric-trac game) 120¸16, — NP muhrah\\\" (and in the index 'muhrah: muhrak').\"},\n   {\"src\": \"BQT\", \"where\": \"Mo'in's footnote 6 to p.2062\", \"stance\": \"supports\",\n    \"note\": \"'پهلوی mutrōk، mudrōk (حلقه؟)، mudar، muhr (مهر)' — Mo'in reproduces Horn's Pahlavi dossier, question mark and all.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"mohr\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"New Persian مُهر mohr 'seal, signet; the impression it makes; (hence) a stamped gold coin' is the regular continuation of \"\n   \"Middle Persian muhr [mwdl], with the Book-Pahlavi spelling still showing the older *mudr; the same stem with -ak gives MP muhrak > \"\n   \"NP مهره mohreh 'bead, vertebra, draughtsman'. ممهور mamhūr 'sealed' is a genuine Arabic-Persian round trip: Arabic borrowed the \"\n   \"Middle Persian word as مُهْر muhr 'seal' and built a denominal verb مهر mahara 'to stamp' on it, whose passive participle ممهور \"\n   \"came back into Persian. The word must be kept apart from the homograph مهر mehr 'Mithra, sun, love' (< Av. miθra-) and from Arabic \"\n   \"مهر mahr 'bride-price' (Semitic *mahara), with both of which Persian orthography and popular etymology have long confused it. The \"\n   \"Hāfez couplet in the box uses mohr in the sense 'seal (on the tongue)', which is the primary meaning.\"),\n \"derivation_fa\": (\"«مُهر» فارسی نو بازماندهٔ منطقیِ فارسی میانهٔ muhr است که در خط پهلوی <mwdl> نوشته می‌شد و همان \"\n   \"*mudra- ایرانی باستان است؛ با پسوند -ak به «مهره» رسیده است. «ممهور» نمونهٔ روشنی از رفت‌وبرگشت از راه \"\n   \"عربی است: عربی مُهْر را از فارسی میانه وام گرفت، فعل مهر را از آن ساخت و اسم مفعولِ ممهور باز به فارسی \"\n   \"بازگشت. این واژه را باید از «مِهر» (میترا، خورشید، محبت؛ از اوستایی miθra-) و از مَهرِ عربی (کابین) جدا \"\n   \"داشت؛ ریشه‌شناسی عامیانه همیشه این سه را به هم آمیخته است. ادعای نورایی دربارهٔ این گره درست است.\"),\n \"sources\": [W_MOHR],\n \"ref_check\": [\n   {\"ref\": \"HRN:224\", \"status\": \"supports\",\n    \"note\": \"Horn no. 1001 straddles pp.224-225 (HRN.txt leaf 238 ends with the page break '- 225 -'): \\\"1001. muhr 'Siegel; Siegelring' ... phlv. ... mudar, muhr 'Siegel'\\\". Nourai's page number is right and the MP > NP step is Horn's own.\"},\n   {\"ref\": \"BQT:2062,2068\", \"status\": \"supports\",\n    \"note\": (\"BQT p.2062 (ref_page.py, BQT_v4 pdf p.145) footnote 6: 'مهر (بضم اول). سانسکریت mudrā (مهر، خاتم، حلقهٔ خاتم)، پهلوی mutrōk، \"\n      \"mudrōk (حلقه؟)، mudar، muhr (مهر)، ارمنی murhak، آستی mysur، قس: بلوچی murdān، murdānag (انگشت)، کردی muhr، mūr، mōr ... قطعهٔ سنگ یا فلز یا \"\n      \"عقیق که برآن نام کسی یا نقشی وارونه کنده باشند'. BQT p.2068 (pdf p.151) footnote 1 to مهره: 'مهره ← مهر (ه.م.). قس: پهلوی muhrak، \"\n      \"muhrag (حلقه)، ارمنی murhak ... کردی muhre (مهرهٔ پشت)'. Both page numbers are exact and both support the node, مهره included.\")},\n   {\"ref\": \"ISS:284\", \"status\": \"partial\",\n    \"note\": \"Not openable (Khotanese Texts VI is not online); Bailey's DKS mūrā- article does cite \\\"N.Pers. muhr, muhrah\\\", so the Persian forms are indeed in Bailey — but as cognates/ancestors of the Khotanese word.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. muhr\", \"stance\": \"supports\",\n    \"note\": \"\\\"muhr [mwdl | M mwhr, N ~] seal\\\" — 'N ~' means New Persian has the same form; the Middle Persian > New Persian step is explicit.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in's footnote 6 to BQT p.2062\", \"stance\": \"supports\",\n    \"note\": \"Gives the Kurdish, Ossetic, Armenian and Balochi cognates and defines mohr as the engraved stone/metal used to stamp — the sense in the chart.\"},\n   {\"src\": \"HUB\", \"where\": \"HUB.txt, grep muhr/mohr\", \"stance\": \"silent\",\n    \"note\": \"Hübschmann's Persische Studien has no article on muhr; the word is treated by Horn instead.\"},\n   {\"src\": \"WIKTIONARY\", \"where\": \"en.wiktionary.org/wiki/مهر, Persian Etymology 3\", \"stance\": \"supports\",\n    \"note\": (\"\\\"From Middle Persian [Book Pahlavi needed] (mwdl), 𐣖𐣇𐣍𐣡 (mwhr /muhr/, 'seal') (compare Parthian mwhr 'seal', and Bactrian μολρο); \"\n      \"possibly cognate with words above, otherwise from Akkadian mušarû 'object bearing a royal inscription', from Sumerian mu-sar.\\\" The Arabic section of \"\n      \"the same page has \\\"Etymology 2: From Middle Persian (mwdl), mwhr 'seal', and denominal verb\\\" for مُهْر / مهر mahara 'to stamp' — confirming the ممهور round trip.\")}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Sogdian\", \"words\": \"mwhrg`n\",\n \"verdict\": \"unverified\",\n \"derivation\": (\"A Sogdian reflex of *mudra- 'seal' certainly exists, but the exact form Nourai prints could not be confirmed. Gharib's \"\n   \"Sogdian Dictionary, the standard lexicon, has entry 5523 mwhrδyb (Manichaean) muhr-δīp, indexed 'seal of letter', with the note \"\n   \"'*mwdr', Parth. δb-', and entry 5610 myδr(y) (secular documents) 'seal'; a headword mwhrg'n / mwhrk'n is not in her dictionary \"\n   \"(grep 'mwhr' returns only 5523). Nourai's form looks like a plural or -kān derivative *muhrakān 'seals', and his source is \"\n   \"Bailey ISS:284, which is not available online, so it cannot be checked; the printed page of Nourai (verified against the PDF image) \"\n   \"does read 'mwhrg`n', so the extraction is faithful. Whatever the form, the arrow's direction is wrong for the same reason as the \"\n   \"other nodes: Sogdian mwhr- continues Old Iranian *mudra-, it does not come from Khotanese mūrā.\"),\n \"derivation_fa\": (\"بازماندهٔ سغدیِ *mudra- قطعاً وجود دارد، امّا صورتی که نورایی می‌آورد تأیید نشد. در فرهنگ \"\n   \"سغدیِ بدرالزمان قریب (مدخل ۵۵۲۳) mwhrδyb «مهرِ نامه» با یادداشتِ *mwdr' و (مدخل ۵۶۱۰) myδr(y) «مهر» آمده \"\n   \"است، ولی مدخلی به شکل mwhrg'n در آن نیست؛ شاید جمع یا مشتقِ -kān باشد. منبع نورایی (بیلی، ISS ۲۸۴) در \"\n   \"دسترس نیست. متن چاپی کتاب را با تصویر صفحه سنجیدم: در استخراج خطایی رخ نداده است. به هر حال جهتِ پیکان \"\n   \"درست نیست: سغدی نیز از *mudra- ایرانی باستان می‌آید نه از ختنی.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"ISS:284\", \"status\": \"not_checked\",\n    \"note\": \"Bailey, Indo-Scythian Studies VI is not online (refs_online.json ISS: Google Books partial preview only, HathiTrust search-only); p.284 could not be opened, and Bailey's DKS substitute article on mūrā- cites Middle Persian and Parthian but no Sogdian form.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary, entries 5523 and 5610 (SOD.txt lines 44645, 45266; English index lines 93375, 93388)\", \"stance\": \"partial\",\n    \"note\": \"\\\"5523 mwhrδyb M | muhr-δip ©*mwdr', Parth. ©δb. -yy\\\" indexed as 'seal of letter 5523'; \\\"5610 myδr(y) S | miδr? | seal\\\". A Sogdian 'seal' word from *mudra- is thus attested, but not in the shape mwhrg'n; grep 'mwhrg|mwhrk' in SOD.txt/SOD_pages.txt returns nothing.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS s.v. mūrā-\", \"stance\": \"silent\",\n    \"note\": \"Bailey's own dictionary article lists Zor. Pahlavi, Manichaean MP and New Persian reflexes of mudrā- but no Sogdian form, so it cannot corroborate mwhrg'n either.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Sanskrit\", \"words\": \"mŭdrâ\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Sanskrit मुद्रा mudrā- 'seal, signet, stamped coin' (later also 'ritual hand-gesture') is a real word with exactly Nourai's \"\n   \"glosses, and the consensus since Weber (1887) and Junker (IF 35, 1915, 273-88) is that it is NOT inherited Indo-Aryan but a loan from \"\n   \"Iranian — Weber, quoted by Horn ad no. 1001, called it 'Egyptian', borrowed from Old Persian Mudrāya- (the OP name of Egypt; cf. MP \"\n   \"muzrāyik 'Egyptian' in Nyberg), while the current formulation (Wiktionary, following Mayrhofer/Lubotsky) is 'possibly an Iranian \"\n   \"borrowing, from Proto-Iranian *mudrā, possibly ultimately from Akkadian mušarû \\\"object bearing a royal inscription\\\", from Sumerian \"\n   \"mu-sar'. So an arrow into Sanskrit from an Iranian source is right in spirit; what is wrong is the particular donor, since the \"\n   \"donor cannot be Khotanese mūrā (a much later form, and one that has already lost the -d-). Note also that Nourai's own reference \"\n   \"goes the other way: Klein p.993 derives Persian muhr from Sanskrit mudrā.\"),\n \"derivation_fa\": (\"مُدرا (mudrā-) در سنسکریت به معنی «مهر، خاتم، سکّهٔ مهرخورده» (و بعدها «حالت آیینی دست») \"\n   \"واژه‌ای واقعی است، ولی از زمان وبر (۱۸۸۷) و یونکر (۱۹۱۵) می‌دانند که وام‌واژه‌ای ایرانی است نه میراثِ \"\n   \"هندوآریایی؛ وبر آن را از پارسی باستان Mudrāya- (نام مصر) گرفته و بیانِ امروزیِ آن بازسازیِ ایرانی آغازین \"\n   \"*mudrā و سرانجام اکدی mušarû / سومری mu-sar است. پس پیکان از یک سرچشمهٔ ایرانی به سنسکریت درست است، \"\n   \"امّا آن سرچشمه ختنیِ mūrā نمی‌تواند بود. با احتیاط پذیرفتنی است.\"),\n \"sources\": [W_MUDRA, W_MOHR],\n \"ref_check\": [\n   {\"ref\": \"KLN:993\", \"status\": \"contradicts\",\n    \"note\": \"Klein p.993 s.v. mohur: \\\"Hind. muhur, muhr, fr. Pers. muhr, 'seal, coin', fr. OI. mudra, 'seal, coin'.\\\" Klein has the word but makes Sanskrit the ULTIMATE source and Persian the borrower — the reverse of the arrow Nourai draws from his Indo-Scythian root into Sanskrit.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 1001, p.225\", \"stance\": \"supports\",\n    \"note\": \"\\\"Weber, Sitzber. BAW. 1887, Pārasīprakāśa S. 5, erklärt skr. mudrā für 'egyptisch', aus ap. Mudrāya- entlehnt\\\" — Sanskrit mudrā as an Iranian loan.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. muzrāyik and bahr\", \"stance\": \"supports\",\n    \"note\": \"\\\"muzrāyik [mwzl'dyk] Egyptian, of Alexander the Great, — OP mudrāya-\\\"; and under bahr \\\"cf Skr mudrā : muhr 'seal'\\\" — the Sanskrit/Iranian pairing and the OP Mudrāya- that Weber invoked.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS s.v. mūrā-\", \"stance\": \"supports\",\n    \"note\": \"\\\"For O.Ind. mudrā, see H. Junker, Indogermanische Forschungen 35, 1915, 273-88; H. Lüders, SBAW 1919, 734-766\\\" — Bailey refers the Sanskrit word to the loanword literature, not to Khotanese.\"},\n   {\"src\": \"WIKTIONARY\", \"where\": \"en.wiktionary.org/wiki/मुद्रा\", \"stance\": \"supports\",\n    \"note\": \"\\\"Possibly an Iranian borrowing, from Proto-Iranian *mudrā, possibly ultimately from Akkadian mušarû ('object bearing a royal inscription'), from Sumerian mu-sar\\\" (further reading: Mayrhofer, EWAia; Turner, CDIAL).\"}\n ]\n})\n\ndata[\"entries\"].append(e2)\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-344.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk344.py",
 "description": "Write page-344.json"
}
```


### [2026-09-07T17:57:49.044Z] TOOL RESULT

```
written
```


## [2026-09-07T17:57:55.430Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-344.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 344",
 "description": "Validate and run verify_check"
}
```


### [2026-09-07T17:57:57.031Z] TOOL RESULT

```
JSON OK
nodes verified: 15/15
node verdicts: {'plausible': 5, 'confirmed': 6, 'disputed': 3, 'unverified': 1}
root verdicts: {'plausible': 1, 'confirmed': 1, 'disputed': 1}
ref checks: {'supports': 7, 'not_checked': 3, 'partial': 5, 'contradicts': 4, 'not_found': 1}
books consulted: {'partial': 9, 'silent': 6, 'supports': 26, 'contradicts': 6} | by book: {'KLN': 7, 'POK': 6, 'ETYMONLINE': 4, 'LKT': 4, 'BQT': 3, 'HRN': 3, 'MON': 2, 'WLD': 2, 'IEC': 2, 'WEB': 2, 'PHD': 2, 'NYB': 2, 'WIKTIONARY': 2, 'ISS_alt_DKS': 2, 'ARY': 1, 'SKT': 1, 'HUB': 1, 'SOD': 1}
```


## [2026-09-07T17:58:00.421Z] TOOL CALL #68: Bash

```json
{
 "command": "timeout 300 python3 tools/verify_archive_sources.py 344 2>&1 | tail -20 || true",
 "description": "Check archived sources"
}
```


### [2026-09-07T17:58:01.732Z] TOOL RESULT

```
7 cited URLs, 0 not yet archived
archived 0, failed 0
```


## [2026-09-07T17:58:21.747Z] AGENT

All done: `data/verification/page-344.json` written, valid JSON, `verify_check.py 344` → 15/15 nodes, **0 PROBLEM lines**; all 7 cited URLs archived.

**Page 344 (book p. 314) — 3 entries, 15 nodes**

Verdicts: nodes — 6 confirmed, 5 plausible, 3 disputed, 1 unverified. Roots — 1 confirmed (Mŭm), 1 plausible (Mŭk), 1 disputed (Mŭrâ).

Disputed / unverified items:
- **Mŭk, #6 Dutch `mocke` "thing" / `male-mocke`** — no such compound exists; the bird-name is Du. *mallemok* = *mal* "foolish" + *mok* "gull" (Klein p.928, Webster). AHD p.1530's `mūk-` article contains no Dutch word at all.
- **Mŭk, #7 English `mallemuck`** — Watkins/AHD, Nourai's own cited source, files it under root `mel-⁷` "to miss, deceive" (via Du. *mal*), not under `mūk-`.
- **Mŭm, #4 English `mummy, mummery`** — *mummy* confirmed (Klein p.1014, chain back to Pers. *mūm*), but *mummery* is from MF *momerie* < *momer* "to mask oneself" (Klein's separate article on the same page; Etymonline). Folk-etymological merger.
- **ROOT Mŭrâ (Indo-Scythian, ISS:283)** — word and gloss are genuinely Bailey's ("mūrā- 1. name of a coin, 2. jewel"), but the direction is inverted: Bailey himself writes "This mūra- is from mudrā- 'seal', Zor.P. mwdl, mwhlk… N.Pers. muhr". Khotanese regularly drops the stop (*mrga- > mūra- "bird"). Modern reconstruction: Old Iranian *mudrā-, ultimately probably Akkadian *mušarû* < Sumerian *mu-sar*. Chart should be inverted.
- **Mŭrâ, #3 Sogdian `mwhrg`n`** — unverified: Gharib has 5523 *mwhrδyb* "seal of letter" (note "*mwdr'") and 5610 *myδr(y)* "seal", but no *mwhrg'n*; ISS:284 is not obtainable online.

Other notable ref findings: POK:752 supports `mūk-` "heap" but ends "after Hubschmid… not Indo-Germanic"; the "peak, spike" gloss and Persian *mūk* are Mann's alone (IEC:814 verbatim). Borhan (BQT p.2054) enters the Persian word as **موکه** and Mo'in's footnote there calls the "sting" sense a corruption of **میش** "ewe" — so node #1 is only plausible. KLN:993 contradicts entry 2 twice (derives Pers. *muhr* **from** Skt *mudrā*). SKT:340 is partial (Skeat routes via Italian *mummia*, not Latin; in the local scan the entry sits on printed p.198, so Nourai's page is from a differently paginated impression). AFM:148 not_found (Arabic OCR corrupt; those leaves are in the ن section). MON:4445 not_checked (6-vol Mo'in has no page-mappable copy).

No extraction errors: I rendered PDF p. 344 at 200 dpi and the JSON matches the printed page exactly (including «موک», «مُهر ( ممهور ، مهره )», `mwhrg`n`, and the Dutch box). Page image copied to `data/verification/sources/refs/ocr/BOOK/344.png`; BQT pages 2054/2055/2062/2068 cached under `refs/ocr/BQT/`.
