# Verification process log — verify-page-150


## [2026-09-05T20:23:05.110Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 150 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-150.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-150.json. Write /home/sfmqrb/git/rishe/data/verification/page-150.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 150` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:23:07.001Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:23:07.716Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:23:07.731Z] TOOL RESULT

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


## [2026-09-05T20:23:07.916Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-150.txt"
}
```


### [2026-09-05T20:23:07.931Z] TOOL RESULT

```
1	=== PDF page 150 (book page 120) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Eis 2 : ice  (refs POK:301)
4	#1 (parent #0) [Avestan] refs=HRN:252; POK:301 | isav : frosty ; aěxa : ice
5	  #2 (parent #1) [Persian] refs=BQT:2427 | yax «یخ» : ice
6	#3 (parent #0) [Old Persian] refs=SOD:452 | viyaxna : ice
7	#4 (parent #0) [Sogdian] refs=SOD:452 | yxn : ice
8	#5 (parent #0) [Germanic] refs=AHD | îs : ice
9	  #6 (parent #5) [English] refs=None | ice
10	
```


## [2026-09-05T20:23:10.868Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-150.json",
 "description": "Read page 150 source JSON"
}
```


### [2026-09-05T20:23:10.907Z] TOOL RESULT

```
{
  "pdf_page": 150,
  "book_page": 120,
  "entries": [
    {
      "root": {
        "name": "Eis 2",
        "lang": "Indo-European",
        "refs": "POK:301",
        "gloss": "ice"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:252; POK:301",
          "words": [
            {"translit": "isav", "gloss": "frosty", "script": null},
            {"translit": "aěxa", "gloss": "ice", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2427",
          "words": [
            {"translit": "yax", "gloss": "ice", "script": "یخ"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "SOD:452",
          "words": [
            {"translit": "viyaxna", "gloss": "ice", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:452",
          "words": [
            {"translit": "yxn", "gloss": "ice", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "îs", "gloss": "ice", "script": null}
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
            {"translit": "ice", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:23:12.907Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','SOD','AHD','BQT','MON','ARY','WLD','KLN','SKT','PHD','NYB','BRT','KNT','HUB','IEC','SYN','CHEUNG','FSD','WEB']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-05T20:23:14.606Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
CHEUNG null
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
```


## [2026-09-05T20:23:30.401Z] TOOL CALL #5: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80; echo ---; sed -n 1,120p /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-05T20:23:30.451Z] TOOL RESULT

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


## [2026-09-05T20:23:31.055Z] TOOL CALL #6: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/ | head -40; echo ---; ls /home/sfmqrb/git/rishe/tools/"
}
```


### [2026-09-05T20:23:31.099Z] TOOL RESULT

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
page-129.json
page-138.json
page-146.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
---
build_site.py
fetch_source.py
ganjoor.py
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
```


## [2026-09-05T20:23:37.445Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,60p data/verification/page-127.json; echo ===; sed -n 1,80p tools/verify_check.py"
}
```


### [2026-09-05T20:23:37.485Z] TOOL RESULT

```
Exit code 1
{
 "pdf_page": 127,
 "book_page": 97,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
  {
   "entry": 0,
   "root": "Dhem",
   "verdict": "confirmed",
   "modern_form": "PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'",
   "note": "Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \"stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\"', so Nourai's language label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.",
   "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» (LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» (گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.",
   "sources": [
    "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86",
    "https://en.wiktionary.org/wiki/%D8%AF%D9%85"
   ],
   "ref_check": [
    {
     "ref": "POK:247",
     "status": "supports",
     "note": "POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; the page continues 'Ai. dhámati ,bläst', av. daδmainya- …, npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug''. Exactly the root box as drawn."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I 851 f. (WLD_Bd1 djvu line 53642)",
     "stance": "supports",
     "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)“. Bedeutungsumfang wie bei Wz. *dheu- „stieben“.' — the source Pokorny 247 abridges."
    },
    {
     "src": "CHEUNG",
     "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)",
     "stance": "supports",
     "note": "'*damH³ \"to blow, breathe; to swell\" … «PIE *dʰmeH- \"to blow\" > LIV: 153 | Pok.: 247 f.»'"
    },
    {
     "src": "AHD",
     "where": "Watkins 1985, d-list (AHD_watkins1985.txt line 377)",
     "stance": "silent",
     "note": "the appendix runs 'dhembh-. To bury. … [Pok. (dhembh-), dhmbh- 248.] dhen-¹. To run, flow.' — no dhem- entry at all, since no English word descends from it via Latin/Greek."
    },
    {
     "src": "IEC",
     "where": "Mann, d-section (grep 'dhem' in IEC.txt)",
     "stance": "silent",
     "note": "Mann has dhen- (2) 'forehead', dhenguhó, dhinió etc. but no *dhem- 'blow, smoke' headword."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Avestan",
     "words": "dam; da-dhmainya",
     "verdict": "plausible",
     "derivation": "The Avestan language has no attested finite verb dam- 'to blow': Bartholomae, Altiranisches Wörterbuch 731 f., knows only the Young-Avestan present participle daδmainiia- 'sich aufblasend, -blähend', said of (tree-)frogs at Vd. 14.5 and 18.73, which he analyses as 'ein Praes. auf -ainya- mit Inl.-Red.' and compares directly with 'ai. dhámati \"er bläst\", np. damīdan \"blasen\"'. Nourai's 'da-dhmainya' is that very word in his own transcription — he writes Avestan δ as dh and marks off the reduplication syllable da- with a hyphen — so the form is faithful; but his gloss 'I inflate, breathe' is wrong: it is an adjective/participle 'puffing itself up', not a 1sg verb. 'dam' is the root abstracted from that participle, i.e. Proto-Iranian *damH- 'to blow, breathe; to swell' (Cheung 2007 s.v. *damH³), which is real and is the ancestor of the Persian words in node 2; it is simply not an Avestan word-form. Hence plausible rather than confirmed: right root, misdescribed gloss, and one of the two 'words' is a root citation.",
     "derivation_fa": "در اوستا هیچ فعلِ صرف‌شدهٔ dam- «دمیدن» به‌جا نمانده است؛ بارتولومه در فرهنگ ایرانی باستان (ستون ۷۳۱ به بعد) تنها اسمِ فاعلِ جوان‌اوستاییِ daδmainiia- «باد کرده، خود را باد کننده» را می‌آورد که دربارهٔ قورباغه‌ها به کار رفته (وندیداد ۱۴٫۵ و ۱۸٫۷۳) و آن را ستاکِ حالِ پسوندِ -ainya- با تکرارِ درونی می‌داند و مستقیماً با «dhámati سنسکریت» و «دمیدنِ فارسی» می‌سنجد. صورتِ «da-dhmainya» در کتاب نورایی همان واژه است (او ذالِ اوستایی را dh می‌نویسد و هجای تکرارِ da- را با خط تیره جدا می‌کند)، پس خوانشِ کتاب درست است؛ اما معنایی که به آن داده («من می‌دمم») نادرست است، چون این صورت صفت/اسمِ فاعل است نه فعلِ اول‌شخص. «dam» هم واژهٔ اوستایی نیست بلکه ریشهٔ ایرانیِ باستانِ *damH- «دمیدن، باد کردن» است (چونگ، ذیل *damH³). بنابراین ریشه درست است ولی معنا و صورت‌بندیِ گره با احتیاط پذیرفتنی است.",
     "sources": [
      "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86"
(eval):1: == not found
```


## [2026-09-05T20:23:38.869Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"eis-\" POK_full.txt | sed -n 1,40p; echo === ; grep -n \"aēxa\\|aexa\\|aeχa\\|isav\" POK_full.txt POK_01.txt POK_02.txt POK_03.txt | head -30"
}
```


### [2026-09-05T20:23:38.927Z] TOOL RESULT

```
Exit code 1
3187:Root/ lemma: aios-: 'metal (copper; iron)' derived from Root/ lemma: eis-1: 'to move 
4730:Differently - because of Indo Germanic meis-, mois-, mis- - Schrader Sprcompare^ 367, 
7936:and probably as " whirl, swing in the circle ' to *ueis-' turn '); 
9037:Maybe but here gr. iaivu) "warms up ' from *HJ)-anJd\ see below eis-V move, shake 
14319:b^leis-:0\6 Icelandic b/Isfra 'b\o\N, whistle'? (compare Gothic -b/esan under b^eA, b'^fe)/- 
22999:Germanic -s- > -r-] of Root / lemma: ueis-2\ "to turn, bend'. 
24633:Root / lemma: eis-1 
24639:Root/ lemma: aios-\ 'metal (copper; iron)' : Root/ lemma: eis-1 \ 'to move rapidly, 
24782:Root / lemma: ei-s-2, ei-n- {*heis-) 
29107:other under *eis- " move violently, fast ' discussed words; 
29993:geis- : 
32613:Root / lemma: gheis- and gheiz-d- 
34907:Root / lemma: geis- 
36147:B. gheis- ' wound, hurt ': 
36159:See also: compare still gheis-, gheizd-^ be angry, furious ', as well as ghaiso- 
36583:ghleis-: 
37589:gheis-:\s\. gisinn^ leaking, cracked from dryness ' (participle from *gfsa=) Norwegian 
44575:Root / lemma: keis- 
52527:root extension k^eis-, A'"i9/lC- (compare above Old Indie cit, citi-)\ 
52529:Old Irish ad-cT{*k"is-e-t) " sees ', cTall\. "reason' = cymr. pwyll, bret. poellAs. {*k"eis-la), 
58146:See also: s. also under meis-. 
65150:Root / lemma: {peis-'H) : pis- 
65176:Root / lemma: peis-2, speis- 
65180:Material: With s-/ Latin spTro, -are'b\o\N, breathe, breathe' {*speis-), spTritus, -Js "breath, 
66739:antique ' {*preis-ko-, compare Armenian erec. Gen. ericu^ the oldest, the priest ', *preis- 
70786:e. reup- ^ausre'\Q>en, tear, break, rupture'; roupa-^ho\e, aperture ', rupeis-xocV! . 
74447:Germanic -s- > -r-\ of Root / lemma: ueis-2\ "to turn, bend'. 
87731:Note: = tueis- 'sparkle, glitter', da "lebhafte Bewegung -flicker, sparkle, glitter' ein common 
87752:participle aicbv (: Old Indie a-tvis-ata), az\a\xa, az\a\\6c, " tremor, Erdbeben'; from a *tueis- 
87757:besides *tueis-ro-) + yaAoc;, perhaps "vonfunkelnder brightness ' to analysieren 
89644:ueis-2)\ Old Church Slavic i/e/7i.C6 "Kranz'; probably Old English wine-wincia {bes\6es 
89750:See also: relationship to ueis-^ deliquesce ' is probable. 
89906:Root / lemma: ueis-1 
89925:Root / lemma: ueis-2 
89989:Root / lemma: ueis-3 
90004:i/Veic/isei {irom Old Prussian *Vfl<sia, older *VFsl<la, from Pre Baltic *l/?s//5 from *ueis-tla), 
91617:extension of Root/ lemma: ueis-2\ 'to turn, bend' [common Latin Germanic -s- > -/"-]. 
91639:Germanic -s- > -r-]. of Root / lemma: ueis-2\ 'to turn, bend'. 
92397:Hittite {*hueis-) huis-^ live, am Leben bleiben', {*hueisa-) /7^/sa-" mirror'. 
(eval):1: == not found
```


## [2026-09-05T20:23:44.400Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '24775,24830p' POK_full.txt"
}
```


### [2026-09-05T20:23:44.456Z] TOOL RESULT

```
Old Prussian FIN Instrutis^ Inster ' and thrak. "lorpoqfrom *lnstr-\ yet one could explain 
"laTpo(; from *ls-ro-s\ 

References: WP. I 106 f., WH. I 717 f., Schwyzer Gr. Gr. I 282, 4825, 491, 679^, 681, 694, 
700, 823. 
Page(s): 299-301 

Root / lemma: ei-s-2, ei-n- {*heis-) 
Meaning: ice 

Material: Avestan isu-^ icy', aexa- n. "coldness', pamir. /s'coldness', osset. yex, /A-'ice', 
afghan. asa/'frost' (if from inchoative formation *is-sR-l\ different Specht Dekl. 18, 201, 
234); 

Old Norse fss, PI. fssarm. 'ice'. Old English /sn.. Old Saxon Old High German Middle 
High German /sn. "ice'; 

Balto Slavic *//7/a-m. and Tmia-vn. " hoarfrost ' in Church Slavic inej, //7y" snow flurry', 
russ. fnejm. and Old Czech y//7/en. " hoarfrost ', Lithuanian yn/sm. (also fem. /-stem). 

References: WP. I 108, Trautmann 104. 
Page(s): 301 

Root / lemma: ei- {*hei-) 

Meaning: to go 

Note: extended eZ-d^-, ei-gh-, i-ta-3indj-a-,j-e-.jd-.j9- 

Material: Old Indie emi, eti, imah, yant/' go', Avestan ae/t/, yeinti. Old pers. a/t/y 'goes', 
themat. Med. Old Indie aya-teetc. (apparent lengthened grade of Old Indie a/'t/, Avestan 
a/t/" goes to, comes to, comes up to, approaches, draws near ' is *a-a/t/, with prefix a); 



Note: 

Reduplicated initial laryngeal in h2™ahre- > Avestan ae- 

gr. horn, sipii " will go ', £? ( *eisi), z\a\ (Doric eIti), PI. ipev, it£, laoi (neologism for *'i£ai 
instead of hiai, *h£VTi, Indo Germanic *i-enti. Old Indie yanti); Impf. Attic nia (neologism for 
*na = Old Indie ayamX Konj. lu) (instead of *£U), Indo Germanic *eid. Old Indie 3. Sg. ayat)\ 
Opt. £ir| (instead of *ir|, Indo Germanic *//e/, Old Indie iyat), Imper. £^-£i (Latin /; Lithuanian 
ei-K), 101 (Old Indie ihf, Hittite i-i-t); 

Maybe zero grade alb. {e)ik-i: Lithuanian e/-/r" go ' 

Latin ed'go' (*e/-dforathemat. *ei-mi). Is, it, PI. Tmus, /?/s (neologism as Lithuanian ei- 
me), eunt{*eJ-onti\ox previous *J-entJ), Imper. /"( *eJ), particle present /e/7s instead of *iens = 
Old Indie y5/7, Gen. yat-ahi^J-nt-es, compare gr. Eniaaaa), Old Lithuanian ent- (instead of 
*Jent-); Perf. n{*li-ar. Old Indie iy-ay-a), secondary Tvf, 

Paelignian eite= "you go, walk, ride, sail, fly, move, pass', Umbrian etu= 'to go, walk, 
ride, sail, fly, move, pass' {ampr-ehtu, apretu^ ambit, circuitous route', en-etu= in-Tto), etu- 
/^ "he/she shall go, walk, ride, sail, fly, move, pass ', eest, es/'he/she will go, walk, ride, 
sail, fly, move, pass ' {*ei-seti), /er'be going away ' (demonstrates a Perf. */ec/), etc.;
```


## [2026-09-05T20:23:45.777Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Eis, Frost\\|jaki\\|isarn.*Eis\\|npers. ja\" POK_01.txt POK_02.txt POK_03.txt | head -20"
}
```


### [2026-09-05T20:23:45.831Z] TOOL RESULT

```
POK_03.txt:3477:aisl.  stjaki  ,Pfahl,  Stange*  =  ahd.  stehho  ,Knüttel,  Pfahl,  Stecken,  PfiocJ^**  t (mit  expressiver  Gemination  stekko):  aschwed.  staki  , Stange,  Spieß', ^jjjji^  " staca  ds.,  mnd.  stake  ds.,  ahd.  stach  , Spießhirsch';
POK_03.txt:3525:*steg-  , Stange'  (z.  B.  aisl.  stjaki  m.  ,Pfosten'),  mit  denen  sich  die  Gruppe
POK_03.txt:3528:Stecken*  (letzteres  aber  zugleich  auch  =  aisl.  stjaki),  aisl.  stik  n.  , Pfahl';
POK_01.txt:4370:vielleicht  hierher   gall.   Isarno-   PN,   isarno-dori  ,ferrei  ostii*,   air. mir.  larann   n.,   cymr.    haiarn   (erfordert   t-),    acorn.    hoern,   bret.   tio"^ , Eisen'  als  das  ,starke  Metall'  im  Gegensatz  zur  weicheren  Bronze;   -l
POK_01.txt:4371:germ.  *isarnan  n.,  got.  eisarn,  ahd.  as.  anord.  isarn  ,Eisen'  ist  we« des  l-  vielleicht  aus  ven.-illyr.  *eisarnon  vor  dem  germ.  Wandel  von  ei l  entlehnt;  vgl.  den  ven.  FIN  ^ladqaq,  später  Isarcusj  nhd.  Eisack  (Tii
POK_02.txt:2383:Altnord,  jaki  m.  {^ehan-  <  *jekan-)  ^Eisstück',  vgl.  Schweiz,  jäch,  gicht
```


## [2026-09-05T20:23:53.644Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '2370,2395p' POK_02.txt"
}
```


### [2026-09-05T20:23:53.683Z] TOOL RESULT

```
aksl.  jama  ,Grube*  (ursprüngl.  Anlaut  j-  erwiesen  durch  das  Abg.  und durch  das  dial.  russ.  nama,  erwachsen  aus  *v^n-jame,  ^jamq).
WP.  I  198  f.,  Berneker  444.
iäm  s.  oben  S.  285.
ie- :  i9-,  mit  -k-  erweitert  lek-,  idk-  ,werfen,  machen,  tun*.
Gr.   %ri^i  (Inf.  livai,   Fut.   f/Vw,   Aor.   s-rjy.a^  ^xa)   ,setze  in  Bewegung,  | werfe,  sende*  (Hi-ie-mi)-^  ^[.la  n.  ,Wurf*;
lat.  iaciö,  ieci,  iactum,  iacere  ,werfe,  schleudere;  streue  aus,  verbreite*;
hitt.  i-ja-mi  ,ich  mache*,  pi-ja-mi  ,schicke  hin*,  u-i-ja-mi  ,schicke  her*; hierher  luw.  a-i-ja-ru  (aus  H-ja-ru?)  ,soll  gemacht  werden*?;
toch.  A  ya-  ,machen*,  suppliert  durch  y-pa-,  im  Prät.  durch  yäm-,  das in  B  im  ganzen  Paradigma  durchgeführt  worden  ist;  nach  Van  Windekens (Lexique  167)  hierher  auch  AB  yäk-  ,vernachlässigen*  ?
Pedersen  stellt  auch  hierher  gr.  laTtzco  ,sende,  schicke'.
Gegen  Herleitung  von  gr.  trjfxi,  aus  *si-se-mi  mit  guten  Gründen  WH.  I 667,  EM  468.  Zweifelnd  Schwyzer  Gr.  Gr.  I  686,  741.  Frisk  (Eranos  41, 49 f.)  entscheidet  sich  wegen  arm.  Mmn  ,Grundlage*  (,*das  Geworfene?*  = lat.  semen)  für  *si-se-mi.
WP.  I  199,  n  460,  WH.  I  667,  Pedersen  Hitt.  129,  198,  Toch.  166, 191,  Lykisch  u.  Hitt.  30.
503 0b-  s.  oben  S.  298.
feg-  ^Eis^;  nur  germ.  und  kelt.
Altnord,  jaki  m.  {^ehan-  <  *jekan-)  ^Eisstück',  vgl.  Schweiz,  jäch,  gicht
(=  gejicht)  ,Reif,  gefrorener  Tau  auf  Bäumen^;   demin.  Bildung  altnord.
jghull  m.  ^herabhängender  Eiszapfen,  Gletscher^;  ags.  gicel(a)  m.  ^Eiszapfen,
Eisscholle^,  engl,  icicle  =  ags.  Ises  gicelj  anord.  ichilla  ,stiria',  ndd.  isJiekely
Jäkel  ,Eiszapfen^  (mnd.  jokele  ds.  dürfte  aus   dem  Nord,  stammen) ;    ahd.
ihilla  (=  *jichilla)  ,stiria' ;
mir.  aig  t  (Gen.  ega)  ,Eis^  (*iegi-s),  cymr.  lä  m.  ds.,  iaen  (^ieginä) ,glacicula^,  acorn.  iey  gl.  glaties,  iein  gl.  frigus,  mcorn.  yeyn,  yen  ,kalt^, br.  ien  ,kalt^.
Das  a  in  mir.  aig  ist  aus  e  vor  palat.  g  entstanden,  das  a  in  den  brit. Formen  hingegen  durch  den  Wandel  von  anlaut.  Je-  zu  ja-  zu  erklären; vgl.  unter  iet-j
über  hitt.  e-ku-na-s  ,kalt^  vgl.  Pedersen  Hitt.  171.
WP.  I  206;   Schweiz.  Idiotikon  II  112  f.,  1120,  III  5,  IV  1010.
ieg^ä  ,Kraft,  Jugendkraft^
Gr.  fjßr]  ,Jugendkraft,  Mannbarkeit^,  fjßdo)  ,bin  mannbar^,  'fjßday.ü)  ,werde m.^,  e(p-rjßog  ,Jüngling^  (jS^-  i^-ccQyvQog)  j
lit.  nuo-y  pa-jegä  ,Kraft,  Vermögen^,  jegiil,  ßgti  ,vermögen,  stark  sein^, lett.Je^a  , Verstand^,  Je^^  , fassen,  verstehen^ ;  ob  hierher  das  isolierte  russ. dial.  jdglyj  ,heftig;  eifrig;  geschwind^?  (s.  Berneker  443).
```


## [2026-09-05T20:23:54.605Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"aexa\\|aēxa\\|aöxa\\|isu-\" POK_01.txt | head; echo \"----\"; grep -n \"301\" POK_01.txt | sed -n 1,5p"
}
```


### [2026-09-05T20:23:54.664Z] TOOL RESULT

```
4380:hierher  auch  ai.  isu-,  av.  i^m-  m.  ,Pfeil';  gr.  fdg  ds.  aus  *lsii-os,  vgl. zur  Bed.  olaTog]
4384:Av.  isu-  ,eisig*,  aexa-  n.  ,Kälte*,  pämir.  i§  , Kälte',  osset.  yex,  ix  ,Eis', afghan.  asai  ,Frost'  (ob  aus  Inchoativbildung  Hs-sk-?-,  anders  Specht  Dekl. 18,  201,  234);
----
605:In   der  Bed.  ,Wurm,  Made^  und   mit  r-Suffix   (vgl.  oben  üfißr^gig  usw.):; ahd.    angar    ,Kornmade^    eugirinc    ,Larve^,    nhd.    Engerling,   lit.    anksfirai ,Maden,  Engerlinge'  (und  ähnliche  Formen,  s.  Trautmann  Apr.  301),  lett.  ; anksteri   ,Maden,   Engerlinge",   apr.    anxdris   (d.   i.    anxtris)    aber   ,Natter^ (über  das  -st-  dieser  halt.  Formen  vgl.  Mühlenbach-Endzelin  Lett.-D.  Wb.  I  ; 71),  russ.  ug{o)rh  , Hitzblatter,    Finne^    (auch    ,AaP,    s.  oben),   poln.    icagry ,Schweinsfinnen'  (Bezzenberger  GGA.  1874,  1236,  BB.  2,  154;  nicht  besser über  angar,  ugorh  ders.   GGA.  1898,  554 f.).  i
862:Über  das  von  Uhlenbeck  KZ.  40,  552,  560  herangezogene  lit.  ärzuolas, qzuolas,  dial.  duzuolas,  ostlit.  dial.  üzolas  , Eiche',  s.  vielmehr  Bezzenberger KZ.  42,  263,  Trautmann  Apr.  301,  wonach  anz-  (vgl,  apr.  ansonis)  die ursprüngliche   Form  ist   (anders   Zupitza   KZ.  36,  QQ,   Germ.    Gutt.   214).
3289:3.  Multiplikativadverb:  duis  ^zweimal' :  ai.  dvih  (ved.  auch  d^ivif^'^^  ^v bis,  gr.  dlg^  alat.  diäs,  lat.  bis,  mhd.  zioir  ^zweinoial-  (aber  iiir.  fo-di  =  ^ n.  dve,  Pedersen  KG.  I  301,  II  127),  germ.    mjth.  PN  Tuüto   ,Zwitter^.
4378:301
4402:WP.  I  113,  WH.  I  412  f.,  862,  Trautmann  72,   Schwyzer  Gr.  Gr.  I  68 301,  351,  499.  '
```


## [2026-09-05T20:24:05.761Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '4376,4392p' POK_01.txt"
}
```


### [2026-09-05T20:24:05.801Z] TOOL RESULT

```
auf  *oi5-  gehen  zurück  wruss.  Jesa  (urlit.  *aisa),  lit.  Äise\  unklar  ist, ob  trotz  des  Anlauts  ^laagog  (Bruttium),  ven.  Aesontius  >  Isonzo,  umbr. AesiSj  Äesiniis  hierher  gestellt  werden  dürfen;  ;'
F
301
anord.  eisa  (*oiV)  ^einlierstürmen',  norw.  FIN  Eisand,  wozu  ags.  ofost, g^.  o$«5^  ;Eile_,  Eifer^  aus  *oS-a^5^;
hierher  auch  ai.  isu-,  av.  i^m-  m.  ,Pfeil';  gr.  fdg  ds.  aus  *lsii-os,  vgl. zur  Bed.  olaTog]
etrusk.  aesar  ,Gott',  ital.  *aiso-,  *am-  ds.  sind  fern  zu  halten  und kaum  mit  gr.  legög  gleichzusetzen.
WP.  I  106  f.,  WH.  I  717  f.,  Schwyzer  Gr.  Gr.  I  282,  482^^  491,  679^, 681;  694,  700,  823.
j.  eis-,  ei-n-  ,Eis,  Frost'.
Av.  isu-  ,eisig*,  aexa-  n.  ,Kälte*,  pämir.  i§  , Kälte',  osset.  yex,  ix  ,Eis', afghan.  asai  ,Frost'  (ob  aus  Inchoativbildung  Hs-sk-?-,  anders  Specht  Dekl. 18,  201,  234);
anord.  iss,  PL  issar  m.  ,Eis',  ags.  is  n.,  as.  ahd.  mhd.  is  n.  ,Eis';
bsl.  *«ma-  m.  und  Hniia-  m.  ,Reif'  in  ksl.  inej,  inij  , Schneegestöber', russ.  inej  m.  und  acech.  jinie  n.  ,Reif',  lit.  ynis  m.  (auch  fem.  z-St.).
WP.  I  108,  Trautmann  104.
ekuO'S  ,Pferd*.
Ai.  dsva-hj  av.  asjpa-  apers.  asa-  ,Pferd'^;  über  osset.  yäfs  s.  unten ;
gr.  'iTtTTog  ds.  m.  f.  (ursprüngl.  ohne  Asper:  ^'Al-^-iitTcog  usw.);
thrak.  PN  BBiaomog^  OvTaGrtioq,  Auteshisj  Eshenus,  lyk.  Kaytaaßog] über  lyk.  esbe-di  ,Reiterei'  (P^^ryg.  Lw.?)  s.  Pedersen  Lyk.  und  Hitt.  51, 67  (*eJmno-m?)]
lat.  equus  (vgl.  die  osk.  Namen  Epius,  Epidius,  Epetinus,  doch  s.  Schulze EN  220%  355);
```


## [2026-09-05T20:24:06.468Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"viyax\\|Viyaxna\" KNT.txt | head -20"
}
```


### [2026-09-05T20:24:06.526Z] TOOL RESULT

```
622:a. Regularly in the -ahyà genitive of the month name, before mahyd: Viyaxnahyd тауа DB 1.37; other examples 1.42, 96; 2.26, 36, 41, 56, 61, 69, 98; 3.7f, 18, 39, 46, 63, 68; and re- stored in 1.89, 3.88.
1577:The month-names  Adukanaisa-, Andmake-, Viyaxna-; for two other month-names cer- tainly have it (see above).
3488:36 sdva : І martiya : magus : dha : Gaumáta : пата : hauv : udapatatà : hacd : Рай 37 yduvadaya : Arakadri$ : n&ma : Каша : hacd : avadaSa : Viyaxnahya : mah
3641:98 m : aja : vasiy : Viyaxnahya : máhyà : X XII : raucabis : Sakata : dha : avatáSám : hamaranam : kartam
3747:65 yàparam : hamiciya : hagmatà : paraità : patiš : Vivanam : hamaranam : cartana 66 iy : Gadutava : nàmà& : dahyáus : avadd : hamaranam : akunava : Auramazdima 67 iy : upastam : abara : vasnà : Auramazdāha : kira : һуа : mana : avam : káram : t 68 yam : hamigiyam : aja : vasiy ; Viyaxnahya : mahya : ҮП : raucabié : ðakatā :
```


## [2026-09-05T20:24:11.153Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Viyaxna-\" KNT.txt | head -20; echo \"----lexicon----\"; grep -n \"viyaxna\" -i KNT.txt | sed -n 1,40p"
}
```


### [2026-09-05T20:24:11.216Z] TOOL RESULT

```
1577:The month-names  Adukanaisa-, Andmake-, Viyaxna-; for two other month-names cer- tainly have it (see above).
----lexicon----
622:a. Regularly in the -ahyà genitive of the month name, before mahyd: Viyaxnahyd тауа DB 1.37; other examples 1.42, 96; 2.26, 36, 41, 56, 61, 69, 98; 3.7f, 18, 39, 46, 63, 68; and re- stored in 1.89, 3.88.
1577:The month-names  Adukanaisa-, Andmake-, Viyaxna-; for two other month-names cer- tainly have it (see above).
3488:36 sdva : І martiya : magus : dha : Gaumáta : пата : hauv : udapatatà : hacd : Рай 37 yduvadaya : Arakadri$ : n&ma : Каша : hacd : avadaSa : Viyaxnahya : mah
3641:98 m : aja : vasiy : Viyaxnahya : máhyà : X XII : raucabis : Sakata : dha : avatáSám : hamaranam : kartam
3747:65 yàparam : hamiciya : hagmatà : paraità : patiš : Vivanam : hamaranam : cartana 66 iy : Gadutava : nàmà& : dahyáus : avadd : hamaranam : akunava : Auramazdima 67 iy : upastam : abara : vasnà : Auramazdāha : kira : һуа : mana : avam : káram : t 68 yam : hamigiyam : aja : vasiy ; Viyaxnahya : mahya : ҮП : raucabié : ðakatā :
```


## [2026-09-05T20:24:11.301Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"aexa\\|aeχa\\|aēxa\" BRT.txt | head -20"
}
```


### [2026-09-05T20:24:11.352Z] TOOL RESULT

```
8471:'  'um  "ranqm  uzuxfyenlinam  srlranqm zairi^aoiianqm  vaxsA  (sd.)  apayasaite  V. /Ä63;  Yt. /Ä6;  —  at  aRyäi  (näml.  dem Rind)  mazdä.  'rä  vaxiaj  (sd.)  Y.4S.6;  — avi  racynyq/H  varauhmt  azuitlmca  'ranam Yt.  ^2.3;  —  nima  'vaire  (VS.)  varMhi masdaöäte  asaone'V.  ig.ii;  Vyt.22,  N.7/, f)7.  a)  Plut.,  im  Gegens.  zu  alxa-  Plur., 'pflanzenbewachsener Boden';  ahond  una 'rlhuca  paiti  *baooisca  vTdtnanmnS  saoa- yäti  . .  ärvatS  urva  *aexahuea  (sd.) . .  "der Seele  des  Gläubigen  ist  es  so,  als  ob  sie auf  Wiesengiund  (stehe)  und  Wohlgerüche empfinde,  .."H.  2. 7— 25.  b)  sva, 'Baum', a)  im  Gegens.  zu  var^ä-.  pairi  van>'>iJ- byasca  'räbyas^a  atsmaiibyS  (sd.)  V.  16. s.  ß)  sonst:  v3r»ynahe  . .  yS  .  .  sainif marisat  'ranqm  ". .  der ..  im  Flug  der  Bäume Wipfel  streift'"  Yt./.4.2i''.  c)  'Pflanzen- Stengel,  Reis':  yavat  akmUi  paitinqm •ranqm  aetavat . .  "so  viel  es  ihm  einzelne Reiser  gibt,  (als  ob)  er  so  viel  .  ."  V.  iV. 86,  a)  bes.    der   zum  Barisman    ge-
24738:•  g.raexanah-n. 'Erbe,  Erbteil'",  in  escha- tologischem  Sinn,  von  dem  was  den  Gläu- bigen als  Lohn  bestimmt  ist'':  aauAlicä atthvascH  apayeilli^A.)  'nanks  vald>m  Y. 32. 11;  —  yBi  va^hsui  valdfnä  (sd.) manatgAS  .  .  °nä    aspSncU  .  .  caxrays{^)
```


## [2026-09-05T20:24:19.427Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Kälte\" BRT.txt | head -20"
}
```


### [2026-09-05T20:24:19.486Z] TOOL RESULT

```
2517:np.^n*  'Eis',  vgl.  PDs.  jj  'Kälte';  Bthl.  ZDMG.  durch  den  Zusammenhang  Angedeutetes  — , 50.697.  — Pu.:  snixr;  s.  No.  I.  —  ')  So,  suit  Zuvotgesagtcs  (Wort  odcr  Satz)  zurück-
2934:•  j.  aota-  i)  Adj.  'kalt':  °tB  vätö  ..gar^mS Yt  10, 50;  V. 2. 5;  — garfm>mca{^A.)  väUm *lmia  Yt^.io.  a)  n.  'Kälte,  Frost': yimaht  xiakre  nsil  'Um  Staha  nöif  gan-
2942:•  j-,  g.  aodar-  n.  'Kälte':  'd}r»m  (GS.) zdihnll  vaaa  (sd.)  Y. 57.12;  —  aodra  (IS.) N.  ,5:
4421:•  j.  an-ä'druxtay-  f.  1)  'Nichtliigen':  yeMe xsahräüa  nsit  aot?m  ai)ha  nSit .  .  para HSit  "unter  des  Herrschaft  es  nicht  Kälte gab  noch  . .,  vordem  dass  er  log"  Yt.  ig. 33".  a)'Nichtverletzen  des  Vertrags,  Ver- tragstreue'(?) :  yä  (näml.  data)  dahmaya vaahuyh  'tsU  Y.  70. 3.
6580:änkar?  Y.  2j.  1;  —  yava  alte  a»Afm  Anhang  zu  Z,  3.  3)  mit  Dat.  a)  'da- (3p,)'*>  F.4e(?); — kadä yavä  hvS  anhat  sein,  vorhanden,  bestimmt  sein,  gelten  für r7.."wann  wird  der  einmal  sein,  der,."  Jemand,  ihm  zu  teil  werden';  B)  im  Awr.r Y.25.9;  J/.  16;  —  Xit^V.  yimahe xsa'^re . .  Amfi">  bloa  mävayacit  ca%7V3rS  arsana »Sit  aot3in  änha  . .  "unter  K's  Herrschaft  "es  sind  auch  für  mich  vier  Männer  da"  V. gab  es  nicht  Kälte.. "V.5. 5;  5.  a,b)  vT-  iS.ii-*N.2Qy,^yaliiyasca  iJi  ä(s±)yji^ ip>m  S  a/imät  yat  alte  narS  '^var»ßva  altbyS  3  ar^kfn  Y.^g.i;  — garS  timJtipm otiA^n  "so  lang  als  die  Männer  im  ■  Var  '"n?rpyö  asti  a/ävaoyS  "das  Paradies  ist  für sind"  V.2.  28.  Z)    mit  Gen.  'sein  der  die    Gläubigen    (bestimmt)"  Yt.j.4;  Vyt.
7980:Zu  einem  Praes.  14  (Inkoh.)  'isaili  'es  friert, es  gibt  Eis';  vgl.  af7.  jjj» 'Froal',  PDs.  li 'Kälte',  ahd.  is  'Eis'.  —  lEi.  s.  Bthl.  ZDMG. SO.  697.  —  Pa.:  sniii^mand.
20010:*)  Wenn  300  Jahre  vom  Millennium  des UxsyiUjnta  vergangen  sind,  wird  dei  Zauberer M.  durch  Schnee  und  Kälte  in  drei  J&hren  fast die  ganie  Menschheit  Temichten.  Dann  soll Yima*  Vor  (sd.)  ge&fTnet  nnd  10  die  Erde  neu bevölkert  werden:  worauf  das  Millennium  des l/xiyal.nimaA  beginnt.  Vgl.  SBE.  4^.  9,  108, rS.  1Ö9,  479,  DST.  ZA.  a.  19,  SÖDERBLOM  La vie  future  iSi  nnd  tu  ir/a-  No.  i.
23601:•  ].,  g.  väza-  1)  Adj.  'fahrend,  fliegend' | (nur  Komp.).  3)  m.  a)  'Ziehen,  Zug' (nur  Komp.  in  Ableit).  b)  'Zugtier'":' zara%uftnm  spitUmim  hyat  ahm!  urü- raost  asts  hyat  höi  Tm  caratatla  aodinlca ziHitnü  'iä  (ND.)  "den  Zar.  Sp.,  indem, er  es  ihm  verwehrte,  bei  ihm  Unterkunft  i zu  nehmen,  und,  als  sie  zu  ihm  kamen,  1 (auch)  dessen  vor  Kälte  schaudernden ' Zugtieren"  Y.5J,  i2'>,  j
26114:•  j.  sar«-i)ä-  'gelidus,  Kälte  bringend' maioydirim (söl)  °Mm'>  Vr.2.a;  —  matöyäh yehe  'la/te^^  Vr./.  sj  —  'lahe'^  mhM FrW.  8. 1  (?).
26115:*iar-  t  'Kälte,  Frost';  vgl.  sanla-.    —    Bed. nach  Pü.  —  Pü. :  iorlik,  er). :  pa  sarl  iavll. <)  Tben.
```


## [2026-09-05T20:24:19.993Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"isav\\|isu-\" BRT.txt | head -20"
}
```


### [2026-09-05T20:24:20.067Z] TOOL RESULT

```
6397:'janJ  bavaiti   (sUtt  Plur.)  Yt. /O.40;  40.     |      '>  NA.  gelrennL  —  >)  D.  i.  Y.  ?/.  14. .  j.  a-wranö.vid-   Adj.  'das  Ziel   nicht'»  J-  !:^Sf''^«"-  ■^'*;i-  'der  sich  das  Aia, erreichend,  verfehlend' :  isavasUt  aisam . .  i  ^^s  (höchste)  Anrecht  verdient,  erworben jya.jaib^hs    voM^mna  'viiü   bavaiti    (statt  ^^*-  P<^otryqn  £kais5 .  .  'a»h3nS  mq^rs.-
7137:werden  in  der  Theologie  fünf  Arten  von Feuer  geschieden;  s.  unter  den  einzelnen Adj.:  °tr>m  b3r3zisavat3h3m..vohu.fryämm . .  urvOzist^m  (s.  A  und  2)  . .  väzist^m  (s.  A und  2)..  j/7«/i"ö/n  V. /7.11;  V.  75.40,  Yt 7J.85.  A)  als  Gottheit  (Vazata;  s.  aber Y.7.2)"':  tumas}  ti  °tars  .  ..huiiH  mazi^ta ^a;o/flNy.5.4;  V.51V.  7; — '7ire..yaltusl)mäi aiiinsanqm  spmtanqm  Y. /.  2;  —  a  html 'hnm  gärayemi  .  .  zaohraSyS  Any.  2^;  — hwqm  'tnm  akurahe  inazda  pu^rpm  asa- vamm  asahe  ratam  .  .  vtspe  "tarS  (AP.) yazamaidey.ss.T,  J'-io,  S. 2. 9,  Vyt, 26(?) ;
7721:•  j.  «rszifyö.parana-  Adj.  'mit  Adler- fedem  besetzt":  isavasca  'na  V.  77.9;  Yt. /0.39,   lOI.
7979:•  j.  isav-  Adj.  'frostig,  eisig";  pasia  "saos Z3mö  aiwi.gaitTm  "nach  Eintritt  des  eisigen Winters"  V.9.6.
8066:•  j.  (jVa-'*  m.:  sva.  isav-.
11360:—  jvasHt  nSit  bvat  asava  vnsasHp  tüSti bax/aiti (sd.)  vahistahe  at3kSusY.^,6i;  — fraia  fraydit  . .  ä  sangaäbyasa^  apn  ä inubyoicit  .  .  3  matiyqnas^t . .  ä  ripr^m- zasät  äpS  Y.6.aj;  —  isavasHt  al^qm  .. ar/tayascit  .  .  zarstvaat  . .  kantacit . .  va- zracit  . .  Yt.  10.  39  f.  a)  das  zweite  ^ steht  unregelmässig:  kasSusÜli  nä  ..  isvä- (sd.)(?i/'*  hqs  paraos  Y.  47.  4.  Anhang, lU  wechselt  mit  iS:  tä^^.,vasfml  anyäüä vTduyl  Y.  44. 4.         2)  wie   bei   I ;    aber
11687:•  j.  Jya-Jata-  Adj,  Von  der  (Bogen)sehoe getroffen,  geschnellt:  isavasal  . .  'tanhi vaamna  "die  Pfeile,  die  von  der  Sehne geschnellt  dahinfliegen"  Yt.  10. 39.
12288:Zam  oi.  V.  fl'oioft'  •beisst'.  —  Vgl.  iarilöjiiisav- und  ai.  ddmhika-;  ferner  zu  täi.dnslra:  — Pü.:  (ef  dandän.
13660:A  hyiin  53.  PeRMOK  Wurielerw   i54,  .59.  ^  >      '""  ^ie  strittigen  Wörter  a Vii.:  pa  frfpiin.  —  •)  iEl  s.  Gds,  BB.  /*  13.   •  j-  dujTO.va-   f.  EN.   der  Frau  Pouru- .  j.  disav-  m.  Name  eines  nächtlichen  t ^^^-^   ^^    ^^fV  /«^f**^";    "'^ Raubtieres:/«ifJÄ?(nämL  ist  der  Hund)  l'!"^"'{''"   »"'"^'"fr''*^  (sd-)    mä  pouru- ya>a  'su/V.ij.at,  473;  —  atH  SiAami""/"^  '7  2^'\F^^^t>      ■  ^^,-
14275:•  j.  9'anvaii-,  S-anvar-  n.  'Bogen',  als Waffe  zumSchiessen:  hukaxtai  ha^a  'vanat YtiO.39;  —  aritayasca  kantayasca  'vanca (NP.)  isavasca  V.  ly.  9.  a)  Plur.  'Schiess- geiät',  d.  i.  Bogen  mit  Zubehör :  yailqm sayanam  ra%Sisti  .  .  tüirya  'van  (NP.) V.  14'.^.
15813:ai.  J>ariav-  f. »),  —  Vgl.  firisav-.  —  Pü. :  fahWi.
16071:KompE.;  Ableit.  (s.  hupir>%-uiya^.  —  Zum  V. ^par-.  —  kurd.  ptrd,  np,  vgL  pal  (s.  dazu GlrPh.  /  b.  387).  —  VgL  pisav-.  —  PO.:  vi- tarai,  (lU  2]i  vilarai  i  xaMostän,  (tu  3  a): eayak  vilarai.  —  1)  Im  Komp.;  ßi»  Suaplei ist  das  Geschlecht  nicht  (icher  festtutteUen; s.  aber  ffSav-.  —  ')  Gramm,  mangelhaft.
16757:—  isavasat  .  .  a£>mnS.vl^S  (sd.)  bavaitt (stattPlur.)  Yt70.39;  39 f.^;  —  nSiipaiti.- tava  bavaitt  "er  vermag  keinen  Wder- stand  zu  erheben"  Yt  10. 48.  4)  in gleicher  Bedeutung  auch  mit  Inf.,  uzw. a)  mit  lok.:  yavat  alte  spana  bii  hapta tttnana  *pairiialahi  (sd.)  bavan  V.  7J.  45 ;
16826:raiti"^  %wyqm^a  "er  bringt  Verderben Über  sie  und  Angst"  Yt  70,37.  a) 'ver- teilen an  -'  (Akk.):  avi  dll  alm  .  .  ha- md^a  (sd,)  baraiti  isavS  Yt/o.  101.
17216:*)  Es  meint  nach  Pii.  und  Zs.  zi.  6  das  Tem- pelfeuei  {varhränpa  niiariärth)  und  zugleich  das dei  täglichen  Gebrauchs  (Bd.  /?.  1 :  älai  äa  i fa  /•ihän  pa  kär  därtnd),  das  nur  Speise,  kein Wasser  verzehrt  (3'arisn  o^aril  äp  ne  i^arll, Bd.  //.  2).  Doch  beachte  man,  dasi  an  der Bd.-Stelle  die  Feuer  iimisava/i-  und  spinii/o' (sd.)  vertauscht  sind.
19697:*paiü.fTasa-  m.  'Erwiderung  auf  die  Frage'. Vgl.  mai-f<üH.p>r>sav-  und  zur  Sache  ntat.- pitisav: —  Pü.;  apik  apäi ptirsihüh  i  mrang,
19699:*)  Ich  verstehe  unter  den  'Fragen'  jene  nicht erhaltenen  Stücke  (in  Prosa),  die  den  Zusammen- hang zwischen  den  verschiedenen  Teilen  der einzelnen  GS^ä  herstellten.  Der  folgende  über- lieferte Text  enthält  die  Antwort  darauf;  »gL m  iU.paiti.pfrisav:
21136:aham  Bh.4>  13-  c)  im  jAw.:  isavascit
22164:—  ai.  veiä-  m.  —  Vgl.  vaisav-.  —  Pu. ;  tranukr. Weiteres  bei  DsT.  ZA.  3.  206.  —  »)  Im  Gegen- satz ztl  pairyiitlar;
24608:•  j,  visavi-  f.  Du.  Name  eines  Bergs  Y.5?.  2;  —  d.iidx  ta  armaiti  'pai  is»m oderGebirgs:  aAma}  haca garays fraoxsyan  '^  (sd.)  maibylca  Y.  -28.  7;  —  ySvaranS  kavä -■  'i>ai':a  Yt.  jp.4.  ,°/j  Y.  ;2.  7;  —  biritams  kava   'pS  Vt.
```


## [2026-09-05T20:24:29.415Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '2505,2520p' BRT.txt; echo \"@@@@\"; sed -n '7975,7984p' BRT.txt"
}
```


### [2026-09-05T20:24:29.478Z] TOOL RESULT

```
»  Gegen  S  2;-0.4.— =)  Pü.:  oflrfar  J«-u=Än.  i  ^™'"«"'    ^"^^      ''■  >
Der  Verf.  braucht  'a-,  weil  et  sich  die  leliten        KompA.  ;^  AbleiL  (s.  aea.\.  —  Vgl.  af/aimäcaB..
Dinge  vergegenwärtigt,—  a  Pü,:  an  i  amäiJ      ~    S'-  <"";■   ^e'-  «'"»f,    "i"»,     noslt.    oi';w;
—  *)  Stammt  wohl  aus  Yt.  r.  18.  —  S)  Man       ^thl.  IE  12.  136.  —  Pü  1  ditauin. verlangte  das  Fem. ;  s.  aber  i«  i^,>,i>,.  No.  i  '  ,    ■   ^^^  ^^_  p         j         (^  ,
—  6)  Konstruktion  nach  dem  Sinn.  —  7)  Nach,  ,,.■'       ,  „  .    "^  .      ■    .   .,    ■     ,       „  . PüErl.  freUich  vielmehr  ,:arat»si  u  Aävisiän  i,  dieser"  I)  in  starkdeiküscherV erwendung zaratuii.  —  *)  So  alle  guten  Hds.  NA.  aouht  \  'der  hier,  jetzt',  von  dem,  was  dem  Spre- nachPü.!   J«  <  ander  «^  iati.  —   9)  Pü.:'cheiiden  Vor  Augen  liegt:  i)  adjektivisch, «,«(,  ^y/a^)    alsoiuflj.,,*-:-  .0)  Pü.:  /^^.^             'dieser  mein,    unser" r    ^c^arata
avisn  i    E.   noch    No.   19  und    lU  aii  Adv.     —  !  _    ^  ,+_.,.,        ,  _        ,    ,
■')  Pü.:  Ä  apumäyai  an  fan  i  :^ii.  ~  „) -^'^.snaro 'Um  myazdiin  yot.dim  hatfluma  (sd.) ai,  erl.!  ä  *"n.  —  13)  Pü,!  im  'ich  bin'.  —  Y. Äs;  —  '/il  yasrta  'ta  vahma  .  .  ava.- M)  Attraktion?  Pü.:  ic res iräyinä . . ä üän.  —  \jasa  . .  aot  sam  "um  dieses  (meines)  Ge- .s)Pü.:/«,.».«i^a«.-  .6)P(i.:,-ii_..;b  (g  ^iji        ;„  Yt5.i32  (s.  s);  —  am
an  OS  raff&a.  —  ';)  Hds.  aja-fourvaya;  s.  aber  ,       =  .  ^  •',    "^      ,       -.-  ,,
Pü.—  '»)S.  Cld.  Pron.  46.—  ig)  ALe  guten  ' '"'^  ''''?)'"  saoirayn  frar»uharois  Yt.5.91; Hd».;  NA.  ^a&J/i.     Pü,:  Jn /a  nitirUn-,   vgl.    92,  93   (wo  'tayäsal);  —   "/d  »rtiü   maoa- No.  10.  — ") Ungeschickte  Nachahmung  von  jrtw/id    a^i   j/^^'a   sindayartha   (sd.)    Vr-Ä "  -^^^  '5"  i(?).       a)  auf  die  a.  Person  bezogen:  =/«
-  g.  'a-  Pron,  ident.  'ich,  du,  er  selbst',  humata  'ta'  ..  aat  mam  narö  paskat  ya- nur  NS. :  yi  maibya  yaos  (sd.)  akmai  astu  g3„ie . .  "um  dieses  (deines)  guten  Denkens vakUta  mahyä  isfois  voha  eöihm  mananM  willen  .  ."  H.2.14''.        2)  substantivisch: ".  .  dem  verspreche   auch  ich  selber  das  ,  ^tai  ti  .  .  avayam  *danmaM  Y.  öS.  i  '>;  — beste  meines  Besitzes  durch  VM."  y.4''-   am  yasna  .  .  ''ta  patti    ava.jasa  .  .  aoi \Z;    —    ai   -3    vaocal  ahurö  mazda    ''da  zam  ".  .    um    dessentwülen  (was  hier  ge- sprach er  selbst,  ^/iM."  Y.sp.ö.  [schiebt)    komm  . ."  Yt. 5.132  (s.  i);   — zBed._s.  Gdn.  GIrPh.   '  52      Ich   '^'^^<=^'^^'- -faimat puir.lt  (sUtt  AS.)  Kimar^xsaf^u/ia dass  f.  as'  aus  einerrart.  idg.  'n  'selber  er-    ,    ,  ,   ,.,       .,•.,..'        ,     .  ,        „ wachsen  ist,  die  in  aUi;  (aus  'a-u-r,  wie , (sd-)    damit  (was  ich  dir  gebe)  such  ..' eJroiaus*jn-H-/°)steckl.Dochs.B(;M,GrGr.3244-    V.  1^.  14;  —  in  Kongruenz  mit  dem  Prae-
—  ¥ä.:  pa  la»;  pa  daAän.  a-päf-A.:  3?'i!.         ;  dikat;    'th;>    tS   *atar}    zaoira   "das  hier
•  j.  acxa-  n.  'Frost,  Eis':  kam.stirittm'^^^^  ..  deine  Z"  N.  Ö5.  a)  in  Verbin- 'sam  . .  dalum  apaohm  "den  erstarrenden  düng  mit  dem  Relativum:  *yH  He  . .  nöit Frost  .  ."  Yt.  /tf.  2 ;  6.  a)  Plur.  'Eis-  * srävayeinti  "qiii  ibi  . ."  N.  25  3).  H)  in felder":  *''xakuca'''"''  patti  *gaintis7a  rX-  schwachdeiktischer  Verwendung  'dieser, di'iänmnö  H.2.25.                                        der,  er":   I)  aufVorhergenanntes  —  oder
np.^n*  'Eis',  vgl.  PDs.  jj  'Kälte';  Bthl.  ZDMG.  durch  den  Zusammenhang  Angedeutetes  — , 50.697.  — Pu.:  snixr;  s.  No.  I.  —  ')  So,  suit  Zuvotgesagtcs  (Wort  odcr  Satz)  zurück-
f^  "a  d';  "rn/KV'^^o'l.r'  °,^v^Af  weisend,  I)  auf  ein  Substantiv  oder  subst 650.     Anders  Gd.n.  KZ.  jo.  514,  —  ')  Vel.  iF.   „  1     j-  ,    ■  •    1         _,     ,  1
sV^.3d,  Pronomen;  a)  adjektivisch;  aae  (3.43)  ..
.].  «to  Adv.  i_)  'dann,  alsdann' 1  zaota  ,  ,  i.,aniö  *'te  asar-o  a^tn  ^.108;  V'.  2. giu,  ..^fra^harott  mrmti  (^A.)  'ta  zaota   ^g  Äi2;6-.47,  /v44,  45;  -  ■^■"«
@@@@
•  j.  isat-västra'  m.  EN.  des  ältesten  Sohns ZaraHuäras  (aus  erster  Ehe)*':  'rahe zara>uitröis  asaons  Yt. /y.98,  Y.sö.  5;2j. 2;  —  'raAe  ^arai^ultröis  rumS  N._yi'>.
*)  Vgl.  Bd.  32.  y.  ha/i-äsir  äsraz-än  ml  mav patan  mavpat  iül,  IQO  säl  fas  (Aar)  den  lilarl. Eig.  'nach  Weiden  verlangend'.    —    ')  Hds. $al.v';  vgl.  Bd.  ja   10.
•  j.  isant-  Adj.,  PPA.:  s.  ^aii-.
KompA.   —  Vgl.  isa-,
•  j.  isav-  Adj.  'frostig,  eisig";  pasia  "saos Z3mö  aiwi.gaitTm  "nach  Eintritt  des  eisigen Winters"  V.9.6.
Zu  einem  Praes.  14  (Inkoh.)  'isaili  'es  friert, es  gibt  Eis';  vgl.  af7.  jjj» 'Froal',  PDs.  li 'Kälte',  ahd.  is  'Eis'.  —  lEi.  s.  Bthl.  ZDMG. SO.  697.  —  Pa.:  sniii^mand.
•  ).  isäna-  Adj.,  PPM.:  s.  als-.
•  j.  isv-KSadra-  Adj.  'nach  der  Herrschaft
dby  Google
373
```


## [2026-09-05T20:24:42.983Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"jaḫ\\|jach\\|jax\\|yaḫ\" HRN.txt | head -20; echo \"@@@\"; awk 'BEGIN{RS=\"\\f\"} NR==273' HRN.txt | head -60"
}
```


### [2026-09-05T20:24:44.883Z] TOOL RESULT

```
@@@
\
— 251 —
aber ohne Erfolg, da er np. yärwer nicht kennt.
Dieses ist etwa wie np. döstdär zn beurteilen ; yüwer
ist aus yürwer entstanden.
Darmesteter's (Et. ir. I, 73) Erklärung des
Suffixes -yär - vergl. beytyür 'glücklich* , hösyär
Verständig', däwyär * Jäger , sehrydr 'Herrscher u.
a. m., sowie den Eigennamen hfendyär etc., auch
talniudisches imriN (de Lagarde, Ges. Abh. 71) —
aus altem -data- auf lautlichem Weife ist natürlich
ganz unmöglich; dieselben gehen vielmehr auf *-(/6lrw-
zurück, wie phlv. satrdarän der Inschriften beweist
(vergl. Bartholomae, Litbl. f. or. Phil. I, 16)^). Bei
Isfendydr u. a., wo direkt eine ältere Form auf -data-
vorhanden ist, ist das np. r nur durch Verschreibung
aus (/ entstanden. Nöldeke weist (Pers. Stud. II, 7
Anm. 2) aus arabischen Schriftstellern noch richtig
Ishendyäd nach.
^122. yäxdeh elf, yanzdeh,
aw. af.vadasa- 'elfter; phlv. yclcdahnm-).
kurd. LW. ydnzdeh ; af>'. yölas.
1123. yase (eyase) *Wunsch, Begierde'^).
aw. *ayäs((k(i' 'Wunsch, Begehren', vergl. d -| yäs-,
yäsanuha 'wünschen, verlangen*.
1124. yäften 'erlangen, erreichen, erfinden*, Praes. yah-em,
..-\*^'' ••i:5n^ (Jer. 2, 24).
aw. vergl. ayapta- 'Belohnung; phlv. äyäftan
(Yasna, Spiegel, Trad. Lit. 439), yaftan (Bund.),
vergl. äyaft,
oss. d. ba]yafun, t. ba]yafin einholen, erreichen'
(145).
») 'Dar steht daneben in hösdär (Sahn. I, 234 Vers 1882). Das
Suffix -yär ist generell jünger als -r/är, doch erscheint dieses letztere
auch häufig in neuen Bildungen.
2) Vergl. Seite 128 Note 6.
*) Der bei Vullers s. v. mitgeteilte Vers Fürbehä Jäml's ist
nach dem FR als Beleg bedenklich, da eine andere Lesart yäse'l
Xünrä laute und yäse — türk. yaso^ yesäq sei (Vullers 1, yäsp).
```


## [2026-09-05T20:24:49.372Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==274' HRN.txt"
}
```


### [2026-09-05T20:24:51.259Z] TOOL RESULT

```
— 252 —
\l2i>'^^ f/än *liimmlische Offenbarung, Gesicht' (mystischer
t. t., den ich nicht zu belegen vermag).
ap. f/ana- *6abe, Gnadengabe' ^) ; aw. yäna; phlv.
yün (Hörn).
Li 125. yaver, ydr-) 'Stössel (des Mörsers)*.
^(;^\j^'^ aw. f/avarenii' ^StösseF (Geldner, Studien I, 50).
\ii26. i/^x *Eis' i/e/ce *Hagel\
i aw. af/a- *Eis', (de Lagard e, Beitr. z. altb. Lex.
i 4"^)), oder Trost* (Bartholomae, Studien II, 55);
päz. yah (L 19)^).
kurd. aty. LW. ye/; oss. d. ye/, t. Jx Eis, Hagel'
^ (148); wa/. yi/.
'il27, yexdan 'Gott*.
,J^o. ^ aw. yazatanqm; phlv. yaztün, yazdän , yaz<i\d\n
^{^y""'"" (Gemmen, Hörn, Mitteilungen Heft IV, 24 No. 2),
yazdaii (Bücher); vergl. ~ized (No. 141).
V4128. yek *ein*.
X Kä^- V. yav, ikt, Q. y, l, ik.
C"--' ap. ^aivaka-, vergl. am/- 'ein'; aw. a^oa-; phlv.
rwak, ev, phlv.-päz. yak (PPGL), ai. eka-,
kurd. Iki jemand' (H.-Sch.), yek (LW.); af;'. yö;
oss. d. yeii, t. yu *ein' (146); bei. eyök einzeln (171);
wa/. li\ ^, sij n. ylv, yu, yä, yi, sar. iv, f, ivj 'einzig,
allein*, ya/n. 7, minj. yao, sangl. vak.
Aus a/?;a- *ein' ist auch das yä-l validet -e ent-
standen.
- 1129. yöz *Jagdleopard' (Vis und Kamin, Seite 40 Vers 12'^).
vergl. arm. yoizlc *das Suchen', yuzem 'suchen, unter-
suchen' (daneben luiben beide Worte noch die Be-
M Zu \ !/((m- ßartholomae, BB. X, 278J.
*) Im FU finden sich drei Belegvorse au8 Nizäri.
*) Scythisches *amalchius* — vergl. Plinius IV, 94: 'septentriotialis
oceanus, amalchiiim cum Hecalaeus appellat a Parapaniso amne, qua
Scythiam adluit^ (juod nomen eius gettfta linyua significat conyelaium*
— 80, wie das Wort dasteht, heranzuziehen, ist bedenklich.
*) Men. 7, 27; K 48 hat snehr *Schnec*, vergl. unter * Verlorenes
Sprachgut*.
^) Keimt auf röz. Felis jubata Schreb., Blanford, Seite 35.
```


## [2026-09-05T20:25:11.096Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== SOD grep yxn\"; grep -n \"yxn\\|yγn\\|yɣn\\|ice\" SOD.txt | head -30; echo \"== SOD_pages 452\"; grep -n \"^\\[pdf page 45[0-9]\\]\" SOD_pages.txt | head"
}
```


### [2026-09-05T20:25:11.162Z] TOOL RESULT

```
== SOD grep yxn
3622:Indices,  which  were  extracted  by  computer,  edited  and  beneficially  used  in  better 
3647:English  Indices.  The  latter  incorporate  entries  of 
3958:twice  in  connection  with  the  Sakas:  Sakaibis  tyaiy 
4579:Pelliot  noticed  that  many  Buddhist  translators 
4613:most  of  the  Paris  manuscripts  in  facsimile  in  Codices 
4918:German  with  glossary,  notes  and  appendices,  arc 
5207:84.  Juridiceskie  Dokumenty  i  Pis' ma,  Moscow  1961 
5223:Word  for  advice  and  some  Mug  Documents",  CAJ  1962, 
5264:has  been  lately  noticed.  It  is  bilingual  (Sogdian- 
5330:94.  First  noticed  in  1906  by  a  British  missionary. 
5398:most  defective.  It  docs  not  distinguish  the  voiceless 
5399:spirants  from  their  voiced  counterparts.  In  other 
5404:voiced  sibilants  Izl  and  III  are  not  differentiated. 
5410:distinguishes  the  voiced  stops  from  the  voiceless102, 
5411:and  the  voiced  spirants  from  the  voiceless,  except 
5440:102.  Voiced  stops  are  generally  analysed  as  allophonic 
5444:a  language  which  distinguished  the  voiced  and 
5445:voiceless  stops  phonemically. 
5453:materials,  distinguishes  all  the  voiceless  sprirants, 
5454:including  /0/,  from  the  voiced.  However,  the  voiced 
5455:stops  are  not  differentiated  from  the  voiced  spirants, 
5473:particularly  noticeable  in  the  Buddhist  texts.  The 
5554:only  the  voiced  stops.  Nevertheless,  as  these 
5860:2)  HI  Voiceless  dental  stop  <  *f: 
5869:3)  /c/  Voiceless  palatal  affricate: 
5884:III)  The  voiceless  spirants  //,  #,  x/  <  Olr.  spirants  /*/, 
5887:1)  ///  Voiceless  labial  spirant  <  *f: 
5914:2)  /#/  Voiceless  dental  spirant 
5977:4)  /£/  Voiceless  velar  stop  <  *k: 
5985:II)  The  voiced  spirants  /#  <?,  y/  reflect  the  Olr. 
== SOD_pages 452
```


## [2026-09-05T20:25:11.881Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== PHD yax\"; grep -n \"yax\\b\" PHD.txt PHD_mackenzie.txt | head -20; echo \"== NYB\"; grep -n \"yax\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-05T20:25:11.942Z] TOOL RESULT

```
== PHD yax
== NYB
1004:rarudenc; patron. Prth 1. 28 = Prs 1. 24 bythškn, Gr. v. rırıdıyav; Paikuli = KZS. Arm. lw. bdeašx (Hübschmann, AG 119 sg.). Georg: Armazi bilinguis (Nyberg, Eranos 44, 1946, 228-243; 233 sqq.) bthš, Gr v. nırıadEng also on gems found there (l.c.; v. also Eränsahr 169), Armazi “Aram.” inscr. (Altheim & Stiel, FuF 35, 1961, 172-178) pyihš; native K art'veli patiaxsi, pitiaxši (Hübschmann, Tschen- keli). Syr. lw. ptahšā, ptakša (often faultily vocalized), aftakšā (Hoffmann, Auszüge p. 34 n. 275). Amm. Marc. XXIII, 6: 14 vitaxae (“id est magistri equitum"), Gr. Hesych. Btorač, read Birač. In dealing with its etymology the indigenous form bythš should; as a matter of course, be given preference before any deviating forms in foreign languages. In its oldest form it is, however, found in Arm bdea&r < *bdiaxs: -d- must be secondary (an original d would have given 7) and go back to a f, voiced because of its proximity to the preceding b, which consequently must be the original initial consonant, not p (pt- would have re- mained); this phonetic state is cogently conclusive in favour of an original form "bitiyaxši-. The first element is *bitīya- ‘the second’, NW form of "dvitiya; Av. (963 sg.) bitya-, MPrth. bdyg (Nyberg, l. e. 237 n. 2; Henning, Iranistik 62 n. 2); the second element has been explained by Pagliaro (RSO XII, 1929, 164 sqq.) as *axsi- ‘eye’ (in Av. derivatives, v. also apaxš); *bītīya-axši- ‘the second eye’ of the King, based on the idea, well attested by the classical authors. and well ana- lysed by P., of the King’s officials as his “eyes”. Thus any etymology starting from initial ptt- is peremptorily excluded; pit- for bit- must be due to a secondary development in the borrowing languages. Pagliaro, l.c. 160-168; Eilers IIJ V, 1962, 209 sq. (quotes Armazi pythé, but ignores bihš!); Benveniste, Titres 65; Rundgren, OrSu XII (1963), 1964, 89-98 (oh!); ete.
4046:lyaxš [whš] word, message 44%. — Av. (1339) vaxša-. On the psychological notion vaxš v. de Menasce, SGV p. 75. V. vaxš-var.
4054:lyaxšitan to grow 40". — Av. (1337 sq.) Iyaxs-, v. also varšišn.
```


## [2026-09-05T20:25:17.401Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; wc -l SOD.txt SOD_pages.txt PHD.txt PHD_mackenzie.txt; echo \"== ice in PHD\"; grep -n \"ice$\\|ice\\b\" PHD.txt | grep -i \"ice\" | head -20"
}
```


### [2026-09-05T20:25:19.069Z] TOOL RESULT

```
 111423 SOD.txt
  45615 SOD_pages.txt
   5578 PHD.txt
  12397 PHD_mackenzie.txt
 175013 total
== ice in PHD
29:been adopted, eclectically, and grateful acknowledgement is hereby made to all whose discoveries have been assimilated within. Nevertheless, I must retain responsibility for the choice as a whole and for readings and interpretations unclaimed or un- published elsewhere.
40:It is common practice to distinguish the Semitic ideograms in Pahlavi, from the Iranian elements, by transliterating them in capital letters. Thus the same letters va are transliterated lhyk' when they stand for rahig ‘child’, but LHYK! when they represent the ideogram for dür 'far'. However, as the ideograms are often much distorted and disguised forms of the original Aramaic words, it is sufficient for practical purposes to trans- literate them by means of a simplified system.
125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
290:lbrinj [binc | N birinj] rice.
306:īdabr [dpi] sinner, deceiver. *dabr [dpl] *dark-coloured. dad [dt' | M dd, N ~] wild animal. 1ааа [d't! | M d?d, N ~] law, justice; those scriptures dealing with legal matters. даа [d’t' | N ~] age. зааа [d>1!] tooth. tdād, v. ahlaw-dād. dādan, dah- [YH BWN-tn! < A Vyhb; d*tn!, dh- | M d'dn, (dy-), P dh- N ~, dih-] 1. give; 2. create. —išn [dh(y)sn'] giving, donation; creation. dādār [d’t?l | N ~] creator. -- ih : creatorship. dādestān [DYNA < А dyn; d'ts?n! | M d'(d)ys?n, N dá(de)stan] judgement, justice, law; case, process. dàd-gàh [2^? gs] proper place, fire temple; = daxmag. dādīg [d'tyk'] legal, concerned with the Law. dad-meh (d"tms] adult, elder. dādwar [d?twbl | (M d^ywr, P d'dbr), N da(d)war] judge. ~ih: judgement. daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. «dišn: breath. daftar [dptl | N —] register, account-book. dagr [AL YK < А ryk; dgl | M dgr > dur, N dër] long. dagrand [дата | N dërand] long. ~«xwaday [-hwt’y] eternal, of long dominion. daģr|-pattāy [dgl pt'd] long-lasting. -—-zamáàn [-2т?п!] a long time. ^-zi(w)isn [-zywsn'] long-lived. dah [ro, ASLY A < A ә | M dh, N ~] ten. dah-, —išn, v. dádan. Юаһаӣр [dř k' | (N Dahàk)] = Azdahág. dahān [РИМЕ < A p(w)m-h | M dhyn, N даһап] mouth. dahibed [dhywpt! | M dhybyd] ruler, lord of the land.
388:h- [HWE- < A d hwh; h- | M h-] be (defective verb). !had [HWEt! ! = Av. Gat] now, then; that is (= à). *hàd [/?t!] a section of the Yasna. hàdamaàns?r [/Ptkmnsl = Av. hača.mādra-| those scriptures dealing with ritual matters. ~ig [-yk'] concerned with the above. - hādēxt [W#twht! = Av. hadaoxta-] certain scriptural texts; a particular sacrifice. haft [лб | M Apt, N ~] seven. ~ad [7o | M hpt'd, N ~] seventy. ~ag [-À! | N hafta] week. —šn [-”x!] the seven planets. haftàr [h5tl | (N kaftār !)] hyena. haftdah [%tdh | N ~, hifdah] seventeen. Haftóring [kftw(k)lng = Av. haptóiringa-] astr. the Great Bear. hagriz [hkic | M hgryc, N hargiz] ever; (with a negative) never. halag [Alz'] foolish, imprudent. ~th: folly, madness. halām [Pm | N ~] potted meat. halilag [hlylk' | N ~a] myrobalan. ham [hm | = M, N ~] also; same; v. 6. —ih: association, union, harmony. hamābēr [hm’fyl | M 72m°byr] storehouse. hamāģ [hm’k' | M Pwg, N hama] all. ~-dén [-dyn'] a complete religious ceremony. hamagih [hmkyh | N —i] totality, universality. hamahl [4(*)4[] = hamāl. hamāl [ml | N ~] equal, peer; comrade, hambadig [hmbtyk'] opponent, adversary. hambah-, v. *hambastan. hambāh-, ~išn, v. hambástan. hambān [hmb’n' | N anbán(a)] skin bag. hamband [hmbnd] connected. ~ih: connection. hamband-, —išn, v. 'hambastan.
392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
396:hannàm [%7m | = M] = handām. Harborz [Albwic | N Alburz] the mountain range surrounding the world. harg [hlg | cf. M bie, Аг. xarj, xaraj] duty, tribute; work, effort. *harrób- [hlwp- | M hrwb-] collect, gather. —išn(ih): collection, gathering. har(w) [KRA < A АР; hl | M been, N har] all, each, every. harwin [%/wyx! | M hrwyn] pl. al. harwisp [Ahlwsp! | M hrwsp] all. ~in [-yn'] pl. all. harzag [hick! | N harza] loose, free. has®r [Ps] = Av. háóra-] a measure of time (unequal hour, ze of day- light); a measure of length (— frasang, or 1 frasang, 1 mile). haspin [hspyn! | = M] rest, repose. hast, ~ih [AY T!, -yh] = tast, ~ih. hašāģird [kP klt! | M APgyrd, N šāgtrd] disciple, pupil. hast [h#! | = M, N ~] eight. ~ad [80 | N ~] eighty. ~dah [лаһ | N ~, higdah] eighteen. lhàwan [h?wn! | N +] a mortar. *hawan [/?zn! = Av. háwani-] the morning gdh. hāwand [/?wnd | M ÞPw(y)nd] like, similar. ^h: likeness, similarity. hāwišt [h’wst'] disciple, pupil. ~ih: disciplehood. haxt [h()At'] thigh, haunch, hip. hāxtan, hàz- [/7htn', h'e-] lead, guide, persuade, convert. ~išn: persuasion, conversion. hazār [1,000, hel | M h?r, N ~] thousand. ~ag LEI | N ~a] millennium. hazzān [?/h2’n'] tomb, ossuary. hên [Ayn! | M hyyn] army. ~ih: attack, aggression. hérbed [%y/pt! | N hérbud] teacher-priest. ~ih: priestly office. hērbedestān [hylptst’n'] priestly school. ~ih: priestly studies. hérig [hylyk' | N h/xéri] iris, wallflower. hézag [Ayck! | (M hyjg), N лег] pail. hil-, —išn, v. histan. hindüg [Andwk! | M hyndwg, N hindi] Indian. ~ап [-°п!] India. hištan, hil-, (P hirz-) [S BKWN-tn! < A У #9; (hlc-) | M hyštn, hyl-, (P Ayrz-), N —] let, leave, abandon, pardon, set, appoint. ~išn: pardon, loosing. hixr [hyhl] excrement. hixtan, hanj- [Ayhtn', hne- | P hxt] draw (water).
398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Ногааа [hwrdt' | M hrwd'd, N Xurdād] Perfection, the fifth Amahra- spand, guardian of water; cal. 3rd month; 6th day. hdsag [hwsk' | М лое, N xēša] ear of corn, cluster; astr. Spica, Virgo. hēšēnīdan, hoSen- [hwsyn-ytn'] (cause to) wither. hēšīdan, hēš- [hws-ytn' | M hwi-, N x~] dry up, wither. héy(ag) [hwy, -k! | M hwy] left(-hand). Hróm [hlwm | M hrwm, N Рат] Byzantium, Rome. ~ayig [-dyk'] Greek, Byzantine, Roman. hu- [hw- | = M] good-, well-. ~ih: good, goodness. hu-bóy [hwbwd] sweet-smelling, fragrant. ~th: fragrance. hu-čašm [hwesm] unenvious, benevolent. ~ih: benevolence. hu-čihr [hweyhl | M hweyhr, (N xujir)] fair, beautiful. hudà(ha)g [hwa?(h)k' = Av. hudàáh-] good, beneficent. ~th: beneficence. hu-|-dast [hwdst'] skilful. ~-dén [-dyn'] of good (i.e. Mazdean) religion. ~-ddsSag [-dušk'] very pleasing. m-ēwāz [-"yw'c] of good speech, affable. —-ëwàzih : affability. ~-fraward [-plwit'] blessed, the late. hugar [hwgl] easy; beneficent. hu-|-&ówisn [hwgwbsn'] of good speech. ~-gugar [-gwk’l] easily digestible. ~-kunign [-kwnsn'] of good behaviour. „-mānīh [-m’nyh] good-mindedness, benevolence. humat [hwmt' = Av. humata-] good thought. humāy [hwm’y | N ~] a bird of good omen; eagle. hu-menišn [hwmynsn'] of good thought. hu-murwāģ [Awmwlw’k'] auspicious. hunar [hwal | M hwnr, N ~] virtue, ability, skill. hunarāwand [kwn wnd | M hwnr'wynd] skilled, virtuous. ~th: skill, virtue. hunarómand [kwn wmnd | N hunarmand] = hunarāwand. hunidan [kwnytn'] extract, express (juice). huniyág [/sonyd?k! | N xunyá] delightful. ~th: delight, entertainment.
428:kem [kym] less, fewer; v. kam. кёп [kyn' | = M, N kīn(a)] hate, malice, revenge. ~ig [-yR'] malicious, vengeful. kennār [Rl] lyre, harp. ~-sray [-sPd] harpist. kénwar [kynwl | (M kynw’r), N kinawar] vengeful, vindictive. ««īh: vindictiveness. kër [kyl | N ~] penis. kēsar [kysl] Caesar. këš [kyš | = M, N ~] dogma, faith (especially non-Mazdean). ~-dar [-d’/] sectary, non-Mazdean. keSidan, keš- [k(y)$-ytn! | (M kr$-), N kafidan] pull, draw. Kēwān [kyw’n! | Ar. kaywān] astr. Saturn. kēwūd [kypwt! | M R'ywd] box, ark. kilēl [R]yl | N ktlīd)] key. kirb [klp | M kyrb] body, form. kirbag [krpk' | M kyrbg, N Аја] virtue, good deed. ~ig [-y%!] virtuous, pious. kirbakkar [krpkkl | M kyrbkr] beneficent. ~ih: beneficence. kirih- [OBYDWNyh-, v. kardan, kiyh- | M kyryh-] be done, made. kirm [kim | M krm, N —] worm, serpent. kirrénidan, kirrén- [klyn-ytn'] rend; create (daevic). kirróg [k(y)lwk! | M grwg] artisan, craftsman; skilled. ~th: arts, crafts, craftsmanship, skill. kiš [k(y)š | M АЎ, N ~] furrow, line. kišnīz [kšnyc] = gi$niz. kištan, kar- [ZL Y TWN-tn! < А У ar; kyštn!, Pl- | M kyšt, kis- N ~] till, furrow; sow. kištār [ZLY TW NTt'l] tillage. kišw, ~4n [kysw', x! | P Аун] tillage. ~(an)zar [-c?/ | (N kištzār)] field. ki$war [Rystol | M kyswr, N ~] region, clime, continent. kišwzār, v. kišwānzār. kūb-, v. koftan. kódak [kxwtk! | M gwdk, N ~] young, small; baby. kof [kwp | = M, N koh] hill, mountain; hump. ~ag [-4! | N Абла] saddle. ~ig [-yk! | N kēkī] wild, mountain-. koftan, kūb- [kwp-tn' | N ~] beat, pound, crush. kör [kwl | M kar, N ~] blind. ~-dil [-dyl | M -dyl, N ~] blind-hearted, incorrigible. kūstan [kwstn' | = M, N ~] beat, pound. kūš-, v. kóx&-. kēšk [how fA! | N ~] pavilion, palace, kiosk.
455:mand [mnd | = M] house. miindag [m?ndk! | M m'ndg, N ~a] tired; remiss; fault, sin. “Аһ: tiredness. māndan, !màn- [K TLWN-tn! < A У ktr | M mnd, N ~] stay, remain; v. also % *mán-. mang [mng] henbane. mänig [mnyk'] household member. mānistan [{KTLWNstn'] = mandan. māništ [m?nyst!] abode, dwelling. ~ag [-k'] sedentary, settled. mānsār [mnsl = Av. ma0ra-] (holy) word, spell. -~-bar [-b/] priest. ~spand [-spnd = Av. spanta-] holy word; v. máraspand. imar [ml | M mr, N ~] number, reckoning, account; class. *mar [m/] scoundrel, felon. таг [ml | N ~] snake. mār-, —išn, v. mārdan., тагар [mik!] number. тпагар [mPk!] perceptive, sensitive. Māraspand [mrspnd | N ~] (= máns?rspand), cal. 29th day. *martabuk [mic”5wk'] brave, valiant. ~ith: bravery, valour. mard [GBRA < A gbr; mlt' | M m(y)rd, N ~) man. mārdan, màr- [ml-tn'] perceive, notice, feel. ~i$n: perception. „išnūmaud [-£rwmnd] perceptive. mardanag [mit?nk! | N ~a] manly, brave. ~ih: manliness, bravery. mardóm [ANŠWTA < A?niwt?; mltwm | M mrdwhm, N mardum] man, mankind, people. ~th: humanity, humanness. mardóm-zàádag [mltwm 2tk' | N mardum-zād] human being. ~ih: humanity. marģ [mlg | M mrg, N ~] death. ~-arzan [-lc’n'] deserving death. ~ih: = marg. --0mand [-”wmnd] mortal. mārīģ [m'Lyk! | M mryg-] word, spell. marw [mlw! | M mrw, N —, (mary)] herb. marz [mlc | M mrz, N ~] boundary, march; astr. term. marzanģēūš [mlengws | N ~] marjoram. marzidan, marz- [mlc-ytn! | М mrzyst, mrz-] copulate. išn(īh): copulation, fornication. marz(o)bàn [mlcp’n' | № ~] margrave, warden of the marches. -masāy [-ms'd] suffix, -sized. mast [mst! | = M, N ~] bemused, intoxicated.
524:ó$murdan, ó$már-, (6šmur-) [MN YTWN-tn! < A * тп; ^wsmwltn', *wšml- | M '(w)šmr-, N šumurdan, šumar-] count, reckon; consider, notice, remember, study.
538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
```


## [2026-09-05T20:25:29.610Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"pdf page\" SOD_pages.txt | tail -5; echo \"@@\"; grep -n \"yxn\\|yγn\\|yɣn\\|yyn\\|'yxn\" SOD_pages.txt | head -20"
}
```


### [2026-09-05T20:25:29.673Z] TOOL RESULT

```
@@
290:jj j ©jLi ojlaUl^ ^wcJ^Jt j swYSyynk *-* *jX j£^—/ >» j ft-J^T
7231:     anxez ©caus. st. ^'ny'yz-, 'nx^z-, }nzyynt-                          AVS 74
7351:1246 'nzyynt-           S, C                     j^yi
8869:1766 'sn'ych ? =* yyn'ynch ?
9653:                oxan ©pret. ywyxnyz
9766:     ozyan ©<*ava-zayana-, fzan-\ MP }wzyyn;
10115:      enakuc ? ©ena <haina ? (+kuc) =^(yyn,^wc
10453:     ozPar ? <DAv. uzban Parth. 'wzbry                                            ^'nzyynt-, 'nzyst-
10696:2391 'spync M                             (e^).^UIJ-r-jU^                 2406 'yn'kwc =» 'yyn'kwc
10798: 2429 'yyn'kwc M                             f      .
11205:     Pay-nawe ©abl. -nw)      =^pyynwy(y)                   2592 pypwryst =* Pypwryst
11282:2607 pyynwy(y)         M                            (>^/-^)>U
12324:                                                                                          Pe/ond (pyynd-) ©<*bandaya- =»Pst-, Pynt-
12398:     farther                                                   3057 pyynd- =* pynd-
14542:      MDii pl04; Hen. BSOAS 28, 1965, 253                             3823 6yyn      M =* Syn
15761:4216 yrp'ky' B, M, S          (jy^ ^^ jj)^\fl<jjh                  yarPene (yrpyyny(y)) ©pi. -r
15818:4241 yrpyyny(y)         M =* yrP^n'k                        [j^U^               Yrft'yct
16649: 4526 yyn{>) B                                         O'^jj          SCE 251, 267
16654: 4527 yyntwh B                               ^i~(<^>/-i0              later, afterwards
17055: 187                                                                                                              kpnyyn
```


## [2026-09-05T20:25:30.495Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \" yax \\|yax '\\|yax,\\|'yax'\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head"
}
```


### [2026-09-05T20:25:30.544Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:25:41.818Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; head -5 SOD_pages.txt; echo \"@@ formfeeds:\"; python3 -c \"\ns=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nprint(s.count('\\f'))\nimport re\nprint(re.findall(r'\\[[^]\\n]{0,30}page[^]\\n]{0,20}\\]', s)[:10])\n\"; echo \"@@ ice word\"; grep -nw \"ice\" SOD.txt | head -20"
}
```


### [2026-09-05T20:25:44.624Z] TOOL RESULT

```
 SOGDIAN
DICTIONARY
Sogdian - Persian - English


@@ formfeeds:
644
[]
@@ ice word
68838:Sudashan(/?n/ice  who  becomes  Buddha,  having 
82572:icy,  (o/)ice 
83337:ice 
90585:ice  10993,  11097
```


## [2026-09-05T20:25:47.017Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '82565,82580p;83330,83345p;90580,90590p' SOD.txt"
}
```


### [2026-09-05T20:25:47.073Z] TOOL RESULT

```
MDii  p21,  Nov.  3  R  4,  12,  15,  18,  21,  VI  p23 
Nov.  4  V7 

10993  ynyyn'k   B  (kj^^l 
yanxene   (y^yn'k)  =*yxn(w),  yy8yn 

icy,  (o/)ice 

TSP  9.29,  -w,  Benv.  n  p220 

10994  ynm'cy   C  =  y-  +nm,c  =»  y-,  nm*c 

10995  ynt>  =»  yzt>  ? 

10996  yntwk'ny  C  ^jua 
yuzdahr   ©<MP  ywjdhr 

holy 
KG  509 

11097  yxn(w)   S  ^ 
yaxn   ©OP  viyaxna  «^yy5yn,  ynyy^k,  yxnyy 
ice 

Sund.  MHC  p26  n33  38.8  V3 

11098  yxnyy   M  (^^JoxU^IJ^^^^Up 
yaxne  ©OP  viyaxna  -»*y>Yn>k,  yxn(w) 

left  over(food) 

I 


I  2347 

ice  10993,  11097 

icebox  11118 

icy  10993
```


## [2026-09-05T20:25:59.229Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\nlines=open('SOD.txt',encoding='utf-8',errors='replace').read().split('\\n')\nimport sys\n# find page index by counting formfeeds before line\nfor target in (82572,83337,90585):\n    txt='\\n'.join(lines[:target])\n    print(target, txt.count('\\f')+1)\n\"; echo \"@@ KNT\"; grep -n \"iyaxna\\|yaxna\" KNT.txt | head -20"
}
```


### [2026-09-05T20:26:00.823Z] TOOL RESULT

```
82572 1
83337 1
90585 1
@@ KNT
622:a. Regularly in the -ahyà genitive of the month name, before mahyd: Viyaxnahyd тауа DB 1.37; other examples 1.42, 96; 2.26, 36, 41, 56, 61, 69, 98; 3.7f, 18, 39, 46, 63, 68; and re- stored in 1.89, 3.88.
1577:The month-names  Adukanaisa-, Andmake-, Viyaxna-; for two other month-names cer- tainly have it (see above).
3488:36 sdva : І martiya : magus : dha : Gaumáta : пата : hauv : udapatatà : hacd : Рай 37 yduvadaya : Arakadri$ : n&ma : Каша : hacd : avadaSa : Viyaxnahya : mah
3641:98 m : aja : vasiy : Viyaxnahya : máhyà : X XII : raucabis : Sakata : dha : avatáSám : hamaranam : kartam
3747:65 yàparam : hamiciya : hagmatà : paraità : patiš : Vivanam : hamaranam : cartana 66 iy : Gadutava : nàmà& : dahyáus : avadd : hamaranam : akunava : Auramazdima 67 iy : upastam : abara : vasnà : Auramazdāha : kira : һуа : mana : avam : káram : t 68 yam : hamigiyam : aja : vasiy ; Viyaxnahya : mahya : ҮП : raucabié : ðakatā :
```


## [2026-09-05T20:26:07.701Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"12th month\\|month name\\|name of a month\\|twelfth month\" KNT.txt | head -20"
}
```


## [2026-09-05T20:26:07.743Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"11097\\|10993\" SOD_pages.txt | head"
}
```


### [2026-09-05T20:26:07.772Z] TOOL RESULT

```
622:a. Regularly in the -ahyà genitive of the month name, before mahyd: Viyaxnahyd тауа DB 1.37; other examples 1.42, 96; 2.26, 36, 41, 56, 61, 69, 98; 3.7f, 18, 39, 46, 63, 68; and re- stored in 1.89, 3.88.
1820:1. Primary, in the following: dar-ma- in per- sonal name Upa-darma-, gar-ma- in month name Garma-pada-, fem. tau-mà-, ad]. taz-ma- in per- sonal names (see Lex.), hau-ma- in hauma-varga-. On dubious атат, see Lex.
1833:І. Stems in --: асе. робат, bdj-im; йй- in per- sonal name Afiy-dbausna-; dip-i-; uša-bār-i-; Aci- extended from *atr-in hypocoristic personal name Aci-na- and in month name Aci-yddiya-; personal names Dédar§-1-, month names @dzgarc-i-, Baga- yüd-i-; secondary in adjective yduman-t-; loan- word skauf-i-.
```


### [2026-09-05T20:26:07.802Z] TOOL RESULT

```
35581:                                                                10993 ynyyn'k     B                                (kj^^l
35959: 11097 yxn(w) S                                                        BSOAS 1979, 339
38555:    how well        9822                        ice 10993, 11097
38559:    Hsien-yang     2117                         icy 10993                                important    5699
```


## [2026-09-05T20:26:11.486Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\ns=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=s.split('\\n')\nfor t in (35581,35959):\n    print(t, '\\n'.join(lines[:t]).count('\\f')+1)\nprint(repr(s[:300]))\n\""
}
```


### [2026-09-05T20:26:13.115Z] TOOL RESULT

```
35581 515
35959 520
' SOGDIAN\nDICTIONARY\nSogdian - Persian - English\n\n\n\n\n      B.Gharib\n\n\n\n\n   FARHANGAN   PUBLICATIONS\n\x0cSogdian Dictionary (Sogdian-Persian-English)\nby B. Gharib\neditorial supervisor: A. Mansouri\neditor: S. Fotouhi\n© 1995, Farhangan Publications\n2/52. Shahid-e Said Street, Tehran 15916, Iran.\nTel: 64600'
```


## [2026-09-05T20:26:17.673Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==520' SOD_pages.txt | head -60"
}
```


### [2026-09-05T20:26:19.277Z] TOOL RESULT

```
                                                                                                                     452

 ywxtyy

            c5
                                                              11106 yxwn-        M                                   dy>-
 11093 ywxtyy       M =» ywxty                                       y(a)xun ©<xu(r)n\ <Av. vohunila- ©ace.
 11094 ywys-       B                                                   yxwny; nom. ob. -y =»ywxn-, yYwn(w),
                                                  *>W
          ywes ? =#yw}st-                                              wYrn-(h), yxwrn-, xwrn-
          (to)keep aloof                                             blood
                                                                     GMS 209, 513, 1168 n 1; BBB f59, 494, 763;
          GMS 22a, TSP 19.1; BSTBL, Dhy. 189
                                                                       GMS 951
 11095 yw ywtr                                       jCjC
                                                              11107 yxwng cyqy'h       M              SSjs c^t^aJ*^
          yu-yutar =»yw2
          one by one                                                 (y)ixwang-cikya
                                                                     discernment
          STi 42.6, STii 6.17; ob. ywtry, C2, 48V17; ywyw,
                                                                     Sogdica. 31.7; GMS 1014
            STii 5.34
                                                              11108 yxwngptz^ky^         M                  cJl^ijA-^x
 11096 ywztxr S                                       Jb*
                                                                     (y)ixwang-patzanakya
       yuzdahr
       holy    ©<MP ywjdhr                                           discernment
                                                                     Sogdica. 35.5 n p36; pi. yxwng ptz^nyt,
       KG 509
                                                                       "discerning" Sogdica. 35.4; C2, 13V17; S W,
 11097 yxn(w) S                                                        BSOAS 1979, 339
                                               ^
       yaxn ©OP viyaxna «^yy5yn, ynyy^k, yxnyy               11109 yxwnk kr'wny        S                     S^t^aJ^:
       ice
                                                                     (y)ixwang-karune
                                                                     discernment
       Sund. MHC      p26 n33 38.8 V3
11098 yxnyy       M              (^^JoxU^IJ^^^^Up                  MSP b 112-3
       yaxne ©OP viyaxna -»*y>Yn>k, yxn(w)                   11110 yxwnq n* ptz'ny C                          uaJ^u j>u
       left over(food)                                             (y)ixwang na patzane ©f. voc.
                                                                   undiscerning
       Hen. Tales. 467, 56, 469 n 3

11099 yxs> M                                      *Xii«^           C2, 13V17
      yaxs (yxsh)                                            11111 yxwnng M                                  S^i^aJhJX
      musk
                                                                     (y)ixwang, yoxung ©<*wi-xwanaka-
      Anc. Lett. 2.58; Hen. Texts. 727.174; GMS 827                    <*wi-xwahanaka «*ywxnq ptz>ny, yYwnk
                                                                     discernment
11100 yxs'mnty C                                    j*}jm            GMS 121, 245, 976; Sogdica. 35.8; Hen. Texts.
      yaxsamande ©ace. yxs'mntw
                                                                       718.300
      reproach
                                                             11112 yxwrn-        M                                   oy-
      C2, 56R6
                                                                    y(a)xurn, y(a)xurn ©ace. -w -»yxwn-, xwrn-,
11101 yxsh       S=» yxs>
                                                                      ywxn-, wYrn-(h)
11102 yxspy*      C = y- +xspy* =* xspw                             blood
11103 yxw'q C                               %yr <c~»-J nA£          GMS 391, 492; BBB 763
```


## [2026-09-05T20:26:39.407Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== AHD\"; grep -n \"^eis\\|eis-2\\|eis-1\\|\\bIce\\b\" AHD_watkins1985.txt | head -20; echo \"== AHD ice\"; grep -n \"ICE\\|Ice\\.\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T20:26:39.473Z] TOOL RESULT

```
<persisted-output>
Output too large (45.8KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b6shy1qcc.txt

Preview (first 2KB):
== AHD
431:eis-1. In words denoting passion. 1. Suffixed form “eis-d- in Latin ira, anger: IRASCIBLE, IRATE, IRE. 2. Suffixed zero-grade form “is-(a)ro-, powerful, holy, in Greek hie- ros, “filled with the divine,” holy: HIERATIC, HIERO-; HIERARCH, (HIERARCHY), HIEROGLYPHIC, HIEROPHANT. 3. Germanic *isarno-, “holy metal” (possibly from Celtic), in Old English ise(r)n, iren, iron: IRON. 4. Suf- fixed o-grade form *ois-tro-, madness, in Greek oistros, gadfly, goad, anything causing madness: ESTRUS; (ES- TRONE). [Pok. 1. eis- 299.]
432:eis-2. Ice, frost. Germanic *is- in Old English is, ice: ICE; ICICLE. [Pok. 2. ei-s- 301.]
828:fixed o-grade form *pozk-itd in Germanic *faihithé in Old French faida, hostility, feud: FEUD!. [Pok. 2. peig-795.] peis-'. To crush. 1. Suffixed zero-grade form *pis-to- in Latin pistillum, pestle: PESTLE, PISTIL. 2. Nasalized zero-grade form *pi-n-s- in Latin pinsdre, to pound: PISTON. 3. Possibly suffixed form *pis-lo- in Latin pilum, javelin, pestle: PILE?. 4. Perhaps Greek ptissein (pt- for p-), to crush, peel: PTISAN, (TISANE). [Pok. 1. (peis-2), pis- 796. peis-2. To blow. Germanic “fis- in Old Norse fisa, to fart, akin to the Scandinavian source of Middle English fise, fart: F1zGIG. [Pok. 2. peis- 796.] peisk-. Fish. Zero-grade form *pisk-. 1. Suffixed Ger- manic form “fisk-a- in: a. Old English fisc, fish: FISH; b. Middle Dutch vische, vis, fish: WEAKFISH. 2. Suffixed form “pisk-i- in Latin piscis, fish: PISCARY, PISCATORIAL, PISCES, PISCI-, PISCINA, PISCINE; GRAMPUS, PORPOISE. [Pok. peisk- 796.] pek-'. To make pretty. 1. Possibly Germanic “fagra- in Old English feger, beautiful: FAIR}. 2. Possibly Germanic *fagin-, *fagan-, to enjoy, in Old English fegen, joyful, glad (> fagnian, to rejoice): FAIN, FAWN}. [Pok. 1. pek- 796.] pek-?. To pluck the hair, fleece, comb. 1. Extended form *pekt- in Germanic *fehtan, to fight, in Old English feohtan, to fight: FIGHT. 2. Suffixed extended form *pekt-en- in: a. Latin pecten, a comb: PECTEN; b. ze
...
</persisted-output>
```


## [2026-09-05T20:26:40.821Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== SYN ice\"; grep -n \"1\\.7[0-9] ICE\\|ICE\\b\" SYN.txt | head -20; echo \"== IEC\"; grep -n \"^eis\\|eisos\\|eiso-\\|iso- \" IEC.txt | head -20"
}
```


### [2026-09-05T20:26:40.887Z] TOOL RESULT

```
== SYN ice
2029:ICE Lith. ledas Lett. ledus ChSl. led SCr. led Boh. led Pol. léd Russ. led Skt. hima- Av. aéxa-
13094:RICE Lith. rysat Lett. risz ChSl. aes SCr. __riza, oriz Boh. ryze Pol. ryz Russ. ris Skt. vriht- Av.
21043:the th nch along 11.87 PRICE oth. wairp, andawairpt Lith. kaina
31450:18.11 WOICE (sb.)
== IEC
1409:bhlós- (bhloi-) “flower, bloom’. Cf. bhloros Lat. flos, gp. florum; Osc. cf. Fluusaí ‘to Flora’; W cf. blóen, blóyn ‘bloom’; OE blosa, id.; MHG cf. bluo, blüe, id. & Du. bloei, id. Variants: Br. bloen (‘blossom’, coll.): W bloden, pl. blodau; MHG bluost, G Bluest; Du. bloesem, beside OE blostm, blostma (*bhlot-, *bhlost-, *bhlos(t)m-); (Li. cf. bluostas “flash, blink, glimpse, nap” for iso- phonic equivalent)
2565:düdul- ‘swing, sway; jaunty; cocky person" Arm. cf. totyey *moor-buzzard'; Du. tuitelen ‘totter’; Fris. cf. tütel ‘sweetheart’; Latv. iso- phone in dūdulis ‘horn, for playing
3371:dhuél- ‘languish, expire, gasp’. See dhuol-, dhul-, dhul- OHG twélan; MHG er-, vertwëln ‘expire’; (z-gde in Li. dvylu, dvilti ‘wane, pine’; OE dwolma ‘chaos’; Norw. cf. dolmen ‘faint’ be- side ON dylminn ‘indolent. (Long-grade iso- phone in Li. dvēlē 'spirit). Av. dvar- ‘rush, as demons’ is ambig. Cf. Skt. a-dhvaráh re, ligious ceremony’. Cf. also OHG twala, OS dwala “hesitate?
3477:eiså, io (ois-) ‘go, dash, impetus, outburst’. Cf. eismn-, oisá, eimi Skt. (ambig.) éSa ‘search; desire’; Lat. (ambig.) ira ‘anger’; Icel. cf. írafár *overhaste'; Li. cf. eislùs ‘going’; eisena ‘gait’
3479:eisio ‘shall go’. Cf. eimi Skt. esyàmi; Gk. eið (pres. subj.); Li. eisu, ei- siu; Latv. iešu (The Li. form eisu is that of the Bible translation)
3480:eisios (eiso-, eito-) (a cpd. pronoun) Skt. cf. esab, -a, neut. etat ‘this’; Osc. eíseís “his; etus’; eise (loc. sg. ‘in him, her, it"); Umb. erer, m., erar, f. “his, her
3481:eisk- (eisK-) ‘request, demand, search". WP I, 12. Cf. aisK- Umb. cf. eiscurent “they shall demand": W wysg (adj. ‘proceeding’; s. ‘procedure, trend"); OSC isto, iskati & isko, ati zeck: Li. ieškau, ieškoti, id.
3482:eismn- (eimn-) “going, movement. Cf. ei-mi and cpds., oi-m- Skt. cf. éman “path, course Ir. éimh, adj. ‘swift; ON ima ‘conflict, strife’; Li. eismas ‘going, traffic, movement; (o-gde in Hom. oima 'dash"). Variants: Li. eisena ‘gait’; W wys (‘mobility’, fr. *eist-)
3488:eisio — eks, eKs- (əKs, Ks)
4324:griuos, à “neck, nape; throat, open jaws' (?). WP I, 683 Skt. grivah, grīvā ‘neck’; Av. grivo ‘nape’; OCS griva ‘mane’; Latv. griva ‘estuary’ beside (iso- phonic) grīvis ‘rank grass’. Adjectival in OCS grivínü, grivína ‘necklace’. (For R. grivna, Cz. hřivna ‘talent-weighť see guru- and cpds., esp. guriu-).
4770:bhos for Ir. and Sl.) Arm. gab ‘mouth’; Ir. (ambig.) gob ‘mouth, snout, beak’; LG gaw, m. ‘mouthful’. (Gk. kóphos queried: “basket? appears to be iso- phonic)
4904:“mask, visor’; Li. greimas ‘film, top skin (ghreio, ghreiio (?) “requirement, responsi- bility, need, debt, obligation. see ghrées-. The evidence is limited to Gk., cf. khr&, khreía, khreía, f. beside khréos, Do- ric: khréos, id., and khr&me, id. A possible iso- phone is Skt. hràsah ‘decrease, detriment’, of uncertain origin. Per. garàyam = ‘incline, tend' ghrem- (1) ‘roar, rage, rumble’. WP I, 655. Cf. guhrem- and next
6643:kakulos /(dung-like, soft. Cf. kakā (iso- phone: kakolos) Arm. kakuy, gs kakyo "soft Lat. cacula 'camp- boy’; ON (?) haell, m. (!) 'soldier's widow’
6694:kam- (1) ‘tire, worry’ Gk. cf. kámno, id.; Li. kamuoti, id.; Latv. ka- mot, id. (and 'torment). (For Mod. Gk. kámo ‘do’, and Gk. kmētós ‘made, wrought", see Kam-. Br. kanv, kaun 'sorrow' may be iso- phonic)
6775:kaptos (kapitos, a) “held, captive; hold, hol- der, slave'. Cf. kap-, etc. WP I, 342 Arm. kot (“handle”, fr. *kaptus, phonol. of ko- toy ‘column, obelisk’ fr. Lat. capitulum); kajt', i-st. (2) ‘basket’; Lat. captus, adj. captus, üs, m.; Ir. cacht ‘servant’; Mir also ‘shackle’ (f.); Br. kaut, kavut, v. inf. “have, hold, find"; m. <‘ possession”: W LW? caeth ‘enslaved; slave’; Go. hafts ‘having’; OHG haft ‘caught, held; captive’; MHG (‘bond, fetter; f. ‘capture’, also as OHG); OHG (variant) habid, habida, MHG hebede ‘possession’; ON haftr, f: hafta ‘pri- soner’; hepti ‘haft; OE hæft, m. ‘bond; priso- ner’; haft, n. ‘haft (adj. ‘captive’); Latv. kāpt, inf. ‘to take? (beside iz-kapts, gp -kapčću, f. (‘scythe:. Of ambig. phonology, cf. kop-). De- nom. in Fris. heftsje, Du. hechten, Sw. häfta, Norw. hefte, etc.; variant in Ir. caist. f. ‘deceit, guile’; W cast, pl. iau, m. ‘trick’ (fr. *kapstis). See kaptio for further exx.
8677:Kerdhos, à “herd, crowd, drove'. Cf. Ker- ‘head’. WP I, 424 Skt. Sardhah “host, army? beside $ardhas, n. id.; Av. saroóo (2) ‘kind, sort’; Go. haírda, f. ‘herd’, wm. ‘herdsman’; OE heord, f., hierde, wm. as Go.; OHG hërta, f., hirti, m. as Go.; ON hjoró, f. ‘herd’; hirðir, gs hiróis, m. ‘herdsman’, cf. hirð, f. ‘bodyguard’. (Gk. kór- thus, f. ‘pile’, and W cordd, m. pl. -ion ‘circle; tribe’ are no more than potential o-gde iso- phones, despite FK: EWDS 17: Herde. OCS éréda (2) “herd” and Li. kerdZius, m. 'shep- herd? are Germanic LWs because of the initial.
9490:lápos, à,*ios ‘paw, palm, hand’. WP II, 428 OE lof ‘palm of hand’; ON lófi, m. id.; Sw. love, wm. id.; cf. ON lófatak 'handshake'; OCS lapa *bear's foot’; R lapa ‘paw’; Pol. tapa, id.; Li. lópa, id.; Latv. cf. lāpsta ‘shovel, spade, blade’; cf. ON (with var. vowel) lafó, f. ‘breadth of palm" (*lept-). (Apparent iso- phones occur in Lat. lappa ‘burr, burdock’; Li. lópas ‘patch, flap, patch of land’ etc., with expressive variants. Cf. also Latv. làps, m. ‘patch’; lāpa, f. ‘torch’; OE lefe ‘limp’, etc.)
9536:légo ‘slump, slacken, fai. Cf. sleg-. Arm. ambig. *leg- or *slég- Arm. Ikim, v. id.; (Gk. légo “cease, abate’; aor. éllexa, with JL indicates a prototype *sleg-); Li. lestu, legti, intr. ‘abate, diminish’. (The iso- phonic MHG lachen, sn. ‘medicine’; lachen- tuom ‘Ieechdom’ is of obscure origin, as also MHG lache, lachene, wf. ‘notch, mark on tree, boundary mark?)
9611:leisos (leisros ?) “thin, slim, slight'. Cf. WP II, 388 Gk. cf. (ambig.) leirós ‘slim; soft; wan; OHG Itso, adv. (*slowly, softly, lightly’: G leise); Li. (ambig.) liesas (“lean”, cf. laisinti ‘grow lean"); Latv. liess, adj. as Li: Sw. cf. lisa, v. ‘modify’
9667:lënið, lið ‘soften, ease, weaken; be soft, be easy”, etc. See lenis Lat. lénio, īre ease, allay’; OCS lénjo se, -iti se “lounge, laze’; Cz. leniti, inf. id. (Icel. iso- phone: læna, f. ‘brook’; v. *flood")
```


## [2026-09-05T20:26:47.893Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '2020,2045p' SYN.txt"
}
```


### [2026-09-05T20:26:47.939Z] TOOL RESULT

```
: Kpbos “icy cold, hard surface, shell, make hard, thicken’,
Digitized by Arya Samaj Foundation Chennai and eGangotri
E PHYSICAL WORLD IN ITS LARGER ASPECTS 69
no trace of meaning ‘snow’, Skt. snzh- ‘be sticky’, sneha- ‘stickiness’.
2. Grk. xiv, NG xd = xexpav ‘win- ter’, Arm. jiun ‘snow’, Skt. hzma- ‘snow, ice, winter’, Av. zyqm, Lat. hiems, Lith. Zema, ChSl. zima ‘winter’ (1.76). Walde-P. 1.546 ff.
3. Rum. zépadd, loanword fr. Slavic, cf. ChSl. za-pastz ‘fall’, ChSI. zapadi specialized to ‘going down of the sun, sunset, west’, while a parallel *zapada was specialized in Rumanian to ‘fall of
snow’, then ‘snow’ in general. Tiktin 1792. Cf. Rum. dial. omédt, némete, fr.
Slavic o-(na-)metati ‘heap up’, hence ‘heap of snow, snow’. Tiktin 1032, 1088. 4. W. eira, Corn. er, Br. erc’h : Ir. arg ‘drop’, Lat. spargere ‘strew, sprinkle’, etc. Walde-P. 2.674. Pedersen 1.104. 5. Av. vafra-, rare but confirmed by
Pahl. vafr, NPers. barf ‘snow’, etym.? Barth. 1347.
ICE Lith. ledas Lett. ledus ChSl. led SCr. led Boh. led Pol. léd Russ. led Skt. hima- Av. aéxa-
Av. xruézdra-, xraozdva- ‘hard’, all fr. *krus-, *krus-t, *kruz-d, with the com- mon notion of ‘hard, hard surface’, whence ‘ice’ in xpicraddos and second- arily ‘icy cold’ in xpios. Further con- nection with the group meaning ‘bloody, raw, raw flesh’ (Skt. Kravis, Grk. xpéas, Lat. cruor, etc.), if actual, is more re- mote. Walde-P. 1.479.
ae In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
70 SELECTED INDO-EUROPEAN SYNONYMS
Grk. zayos ‘frost’ (also ‘rocky hill’), sometimes ‘ice’, as NG rayos ‘ice’ (also mwaywrd ‘ice cream’) : ryyvupe ‘fix, make solid, freeze’.
2. Lat. glaciés (VLat. glacia > It. ghi- accia, now ghiaccio, Fr. glace, Rum. ghiatd) : gelu ‘icy cold’ (> Sp. hielo ‘ice’), adj. gelidus, Goth. kalds ‘cold’, ete. (15.86). Walde-P. 1.622, 612. Er- nout-M. 412, 423. REW 3718, 3771.
3. Ir. aig, aigred, NIv. oighreadh, W. ta: ON jaki ‘piece of ice’, dim. jokull ‘icicle, glazier’, OF gicel ‘icicle’ (zses gicel > NE icicle). Walde-P. 1.206. Peder- sen 1.65.
W. rhew (now more usual for ‘ice’ than ia), rewi ‘freeze’, Br. reo ‘frost’, riou ‘cold’, riel ‘thin ice’, Ir. reod ‘frost’,
perh. : Lat. prutna ‘frost’, OE fréosan ‘freeze’, etc. Henry 232 with query, Morris Jones 103f. (Not included in Walde-P. 2.88). Otherwise Stokes 231.
Br. sko(u)rn, etym.? Henry 248.
4. ON iss, OE is, etc., general Gmce., prob. : Av. aéza- ‘frost, ice’, isu- ‘frosty, icy’, NPers. yak ‘ice’, Afghan asai ‘frost’, root connection? Walde-P. 1.108. Falk-Torp 468, 1490. Barth. 372,
5. Lith. ledas, OPruss. ladis, Lett, ledus, ChSl. ledii, etc., general Balto- Slavic, outside connections? Walde-P. 2.428. Berneker 699.
6. Skt. hzma- ‘ice, snow, winter’ : Grk. xiwy ‘snow’, Lat. hiems ‘winter’, ete. (1.76).
Av. aéxa-, above, 4.
1.78 WEATHER
Grin a5 2 Goth Lith. oras NG Katpés ON vedr Lett. laiks Lat.  tempestas, caelum Dan.  vejr ChSl .... It. tempo Sw. vader SCr. _vrijeme Fr. temps OE weder Boh. potast Sp. tiempo ME weder Pol. czas, pogoda Rum. timp, vreme NE weather Russ. pogoda Tr. sin Du. weder, weer Skt. kala-(?) NIr. ston, aimsir OHG  welar Av. es
```


## [2026-09-05T20:26:48.602Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"‘ice'\\|'ice’\\|“ice\\|‘ice’\" IEC.txt | head -20"
}
```


### [2026-09-05T20:26:48.663Z] TOOL RESULT

```
339:akl- (?) “ice? Alb. akull; ON éi- in él-kaldr
2265:dibhaio (denom. of *dībhā) “dash, plunge, hurtle'. Gk. dipháo ‘dive after; seek; Ir. díobhaim (die out; tr. (consume, destroy); W difa “consume, waste’; Icel. tifa ‘trip along’; Swiss cf. Zibe “ice-track” did- (expr. didd-) ‘teat’. WP I, 704 Oss. cf. dzidzi, id.; Arm. tit; LLat. dida; Mir & Ir. did; OE titt; MHG zitze, id. (For Gk. titthós, titthe, see dhiddh-)
3936:gel- ‘freeze; frost; frozen’. WP I, 622 Skt. jadah, adj. ((1) ‘cool, cold”, fr. *geldios, cf. Lat. gelidus); Per. Zale *frost'; Siculian Gk. géla “ice”; Lat. gelu, n.; gelo, are, v. gelidus, adj.; OE ceolas, mpl. ‘cold winds’; Du. kil ‘cold, chill; MHG kéllen, v. ‘freeze’; OCS Zlédica (ffrost" or 'ice"); (o-gde in Sw. källa “spring, well’; ON kelda, (Dan. kilde!) in view of Finn. LW kaltio, id.; cf. o-gde also in ON kala, v. ‘freeze’; OCS golüti, mf. “ice'); Li. cf. pa-gelüs ‘raw cold’; pa-gelà, -geluó, s. id.; gelumà ‘sharp frost’. (Oss. dzälarä “blob of fat” seems to be isophonic)
4222:golətis (golt-) “chill, cold, frost’. cf. gel-, geldios, golos MHG kelte, id.; OCS goloti “ice”
4410:grümos (1) “piece, bit. WP I, 597 Hes. cf. grüméa ‘trash’; Lat. grümus (2) ‘clot, lump’; Alb. (ambig.) grimë (‘crumb, speck’, but if < Alb. grij, v. ‘mince’, cf. guhriio); Ir. grúm “icefloe*; LG krūme ‘crumb’; Du. kruim, id.; OE cf. cruma, id. with *-ü- and MHG krume, krumme, id.; Li. cf. grumtas ‘clod’
4954:ghródos, io “ice, hail, crust:. Cf. ghrud- Vedic Skt. cf. hrádunih “hail'; OCS gradü, graZda, id.; Srb. grád; OCz. hrad, id.; R cf. gra- dobitie ‘hailstorm’; Li. grüodas *hardfrozen ice; scaly-foot in horses’; gruodis ‘December’
6187:iĝ- (?) “ice? W ia; Swiss Jäch; Li. íZas “floating ice’; OE cf. gicel, gicela, m. “icicle*; ON jokull, id. (dim. type). The vocalism of Mir aig, gs ega "ice is obscure
6243:is- (1) (ois-?) “hard or crystalline substance, ice". WP I, 108 Av. isis, m. ‘ice’; aexa (*frost,, fr. *ois-?); Per. yax ‘ice’; Oss. Ix, Dig. jex ‘ice, hail; MHG. OE 1s, ON íss, id. (W ia “ice” is of uncertain derivn. Slovene i-mje, i-nje, Srb. inje, OCS inij, inije, m. and n. *hoarfrost appears to be a synth. cpd.)
6325:iaĝos, ios ‘ice’? Cf. Is-. (The Welsh evidence is ambig.) ' W ia; ON jaki “icefloe?. For the consonant, cf. Li. iZas, a, mf. “thin ice?
8012:krous- (2) ‘collapse, fall, crumble’. (Prob. same root as krous- (1)) ON hreysar, fpl. ‘heap of stones’; hreysi, n. “cairn, cave’; (mod. “hovel'); Sw. rósa, v. ‘pile up’; OCS kruxü ‘crumb’; OCz. kruch “frag- ment’; Blg. krux ‘grain of salt’; Ukr. kruxyj, Cz. kruchý ‘brittle, crumbly’; Pol. kruchy, id.; cf. kruszec, m. ‘ore’. E-gde in OE hrēosan (2) “collapse, sink, fal’; Li. kriauSius (e- or o-gde: “steep bank"). Isophonic: ON hrjósa, sv. 2. (e-gde: “horrify*); see krous- (1). Z-gde in Gk. krüos, n. ‘ice’. See krus-. Extn. in ON hraustr “brave, strong"; hreysti, f. ‘valour’
8016:krügos, å “crust O: hrúkr, m. ‘scab, crust’; Ukr. kryha “ice- fake, ice-sheet
8707:Kersnos, om, ios, à (Ker?sno-) “crust of snow or ice’. WP I, 409 Arm. sarn, gs sarin, absg -amb “ice, frost’; ON hjarn, n. “hard snow'; OHG cf. (zero-gde) horn ‘January’ and G Hornung ‘February’ be- side Ger. Harsch, Harst ‘crust of snow’; OCS srénü ‘hoary, frosty’; Slovene sren, m. “crust of snow? and sre$ ‘tartar’; Slovak srieň, m. *hoarfrost'; Latv. sersnis “crust on snow’; Li. (with implied glottal stop) Serk$nas, Serk$nà ‘crust of snow, rime’
8787:Kinis, om ‘grey, blue, hoary; hoarfrost, grey or white matter" Skt. cf. $inám ‘ice’; Lat. cinis, gs erg, m. f. *ash, ember’; Alb. thinjé, adj. 'grey-haired'; fpl. ‘grey hair’; OCS sint, adj. ‘blue’; R sini, f. ‘blue’; sinij, adj. id.
11150:mor- (3) (moros, à, io) “chill, frost; frosty, cold". Cf. mr&- (3) Alb. mardhé, f. ‘chill, frost; OCS mrazü, m. id. (and com. S1.)); (z-gde in) Mod. Gk. mar- góno ‘be stiff with cold’; OCS mrüZa, f. “ice”
13004:plak-, plakt-, variant of type plākst- in OCS plasa, f. ‘belt’; Cz. ‘strip of land”; Blg. ‘chip, shaving’; Srb. “icefloe'; cf. also R plast, m. “layer, slice’; Cz. plást, plástev, f. “honey- comb’ beside ná-plast, f. (“sticking-plaster”, inf. by Gk. ém-plastron)
```


## [2026-09-05T20:27:10.306Z] TOOL CALL #38: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T20:27:10.313Z] TOOL RESULT

```


```


## [2026-09-05T20:27:10.730Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; grep -n \"یخ\" ARY_pages.txt | head -20"
}
```


### [2026-09-05T20:27:10.776Z] TOOL RESULT

```
88:کوج کردهاند. طی این کوج‌های متوالی؛ آریایی‌ه با بومیان هر محل درآمیختند و در نتیجه پاک و
89:برتری نژادی آنها کم شد. هر چه اين کوچگران از آلمان دورتر شدند؛ میزان آمیختگی خون آنها با
176:بررسی جنبش‌های کوچگرانه‌ی دیگر در دوران‌های تاریخی الگوی کلی این کوج‌ها و پيامدهای
201:۱ ۱ سیار زباد باشد (تارد یخ‌های فوق میلادی هستند).
286:آن. بررسی واژگان هند و اروپایی و شواهد تاریخی و اسطوره‌ای و باستانشناسی نشان می‌دهد که ۱
311:صادق است. واژه‌ی «یخچالء (چاله‌ی یخ) را برای ابزار سرد ساز برقی بکار می‌پریم. واژه‌ی «سپر» را ۰۹ 48۶
429:برخی از آنان که فرهیخته تر بودند با شگفتی دریافتند که شباهت عجیبی میان سانسکریت و زبانهای
612:میخی (/۲112331۳03) و به زبان‌های هتیت‌کهن (حدود ۲۰۰۰ تا ۱۵۰۰ پیش از میلاد) و هتیت.
641:و ایرانی در زبان‌های مردم پین‌النهرین بسیار نادراند ولی پس از آن تاریخ شمار این واژه‌ها کم کم
702:وجرد دارد. ضمناً سیر قفقاز در دوران‌های تاریخی نیز توسط یک قوم ایرانی دیگر؛ سکاها
713:را وابسته به خود زرتشت می‌دانند و تاریخ حدود ۹۰۰ سال پیش از میلاد را برای زرتشت و کتابش
715:حدود ۱۰۰۰ تا ۱۲۰۰ سال پیش از میلاد (یعنی تاریخ احتمالی کوج ایرانیان) است. خویشی بسیار
735:اطلاع موثفی درباره کوچ هندو اروپائیان به اروپا و تاریخ آن در دست نیست. ۱
749:آثار فلسفی و تاریخ ی گوناگون. زبان یونانیکلاسیکه به ندریج تبدیل به یونانی نوین شد. سخنگویان
798:که به تدریج با مهاجمان آمیخته شدند. در نتیجه‌ی این آمپزش» ملت انگلیس و زبان انگلیس ی کهن به
820:نگاشته شده‌اند. این دو زبان که متون و آثار تاریخی وابسته به آنها حدود صد سال پیش در ترکمنستان
830:احتمال زیاد تاریخ این کوج حدود ۹۰۰ تا ۸۰۰ سال پیش از میلاد بود. در حدود 3۰۰ ميلادي ‏
844:و از باختر تا مرز باختری لهستان و از جنوب تا بلفارستان و مقدونیه را تصرف کردند. تاریخ احتمالی
857:تاریخی» وجود همریشه‌های بالتیکی (به ویژه لیتوانی) از اهمیت خاصی پرخوردار است.
982:بودکه می‌توان برای تراضی خدایان قربانی کرد. در زمانهای تاریخی نیز رسم قربانی کردن انسان در
```


## [2026-09-05T20:27:15.915Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; grep -n \"یخ (\\|یخ:\\|یَخ\\|^یخ\" ARY_pages.txt | head -20; echo \"@@ latin\"; grep -n -i \"YAKH\\|YAX\" ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-05T20:27:16.052Z] TOOL RESULT

```
@@ latin
10730:HAR ‘(OLD NORSE) oS 39 YAXSHTI, SHAKHA :(AVESTAN) gs!
15721:YNIs LITHUANIAN) ly) ASAI, YEX, YAKH
```


## [2026-09-05T20:27:20.231Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; sed -n '15700,15740p' ARY_latin_index_pages.txt; echo \"@@@ page tag\"; awk 'NR<=15721 && /\\[pdf page/ {p=$0} END{}' ARY_latin_index_pages.txt; grep -n \"\\[pdf page\" ARY_latin_index_pages.txt | awk -F'[][]' '$0!=\"\"' | awk 'NR>0' | python3 -c \"\nimport sys\nlines=[l for l in sys.stdin]\nprev=None\nfor l in lines:\n    n=int(l.split(':')[0])\n    if n>15721:\n        print('prev',prev,'next',l.strip()); break\n    prev=l.strip()\n\""
}
```


### [2026-09-05T20:27:22.142Z] TOOL RESULT

```
ODINNADTSAT —-(RUSSIAN) «yu UNDICI H(ITALIAN) ids
JEDENACT CZECH) Se UNSPREZECE —{RUMANIAN) sly
EDYNAYESET — (BULGARIAN) «5 ONZE (PORTUGUESE) 5 »
JEDENAST (SLOVAK) 51 jh AINLIF (GOTHIC) S55
NJEMBEDHJETE  -(ALVANIAN) UT :(OLD SCANDINAVIAN) AS 5-t0\
ELLIFU
[pdf page 538]
EEE ES
.
‘MACKENZIE: (ELEVEN) 112 REFERENCES beth,
SKEAT: (ELEVEN) 190“ PoKoRWy, 286, 91
rr sbi dby BARNHART: (ELEVEN) 321
DELAMARRE: 209, 214
[a re 8]
[nea ee
Is (NORWEGIAN) (5535 AEX, AEXA, ISU. :(AVESTAN) glows)
yc DUTCH) acl YAH (434) PAHLAVY hy
HOLD CHURCH SLAVIC) pS «5331 YEX, IX HOSSETIC) «eh
INEJ, INI YEX (KURDISH) «53,5
fNEy ARUSSIAN) ges YEX ABALUCHI) «ge sy
JfNIE CZECH) Soy AFGHAN) (4) gliil
YNIs LITHUANIAN) ly) ASAI, YEX, YAKH
HOLD SCANDINAVIAN) (x45 510!
‘REFERENCES: beth ISS, ISSAR
| POKORNY. SSSSSC«SL Ts HOLD SAXON) 5 gi pS
BARNHART: (ICE) 503 Is OLD FRISIAN) oS 52.3
DELAMARRE: (GLACE) 182 TS {OLD HIGH GERMAN) 4S, gt
BUCK: 69-70 (GERMAN) glsT
ONIONS: (ICE) 458 iB HOLD ENGLISH) SS
SKEAT: (ICE) 285 ICE ENGLISH) SS}
MALLORY & ADAMS: HEIHX Is (DANISH) SRE
very ight oly Is on (SWEDISH) ga
ay
YAZTAN, YAZDAN, YAZD YAZATA HAVESTAN) glow gh
EZDAN (RURDISH) «52,5 PAHLAVI) 6 shay
[pdf page 539]
(Lenght AAS jl pty) tang | OF s
REFERENCES Wetk,| —  YEZDAN HBALUCHD) gx Se
POKORNY: = —~SOS*~*~*~*«* SANSKRIT) cy Se
MACKENZIE: yh : GOD) 116 YAJATI, YASTA., IJVA, YAIVA-, YAJAS-
JMINDARGV: , * (eon) 231 AGIOS, AHIOS GREEK) gly
@@@ page tag
prev 15706:[pdf page 538] next 15735:[pdf page 539]
```


## [2026-09-05T20:27:33.991Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; awk '/\\[pdf page 538\\]/{f=1} /\\[pdf page 539\\]/{f=0} f' ARY_pages.txt | head -40"
}
```


### [2026-09-05T20:27:35.699Z] TOOL RESULT

```
[pdf page 538]
نا اک اک وم
۰
بیغ / ۵۳۹ ۱
پسگشت‌ها ار هرد دا 2 (۲ظ8۲۳۷) اد ۱21۵
191 86 ۶0/0/0 0 ۳۵ ت35
41 (8]۵۷8) +82۷7 برهان قاطع : ادف
4 ,208 05/۸722
اوستایی (4۲8974/4): ۰ -1817 بشلاتل۸ بلاقلشه نروژی (0/07۷80147: 15
پهلری (41ا/(۳۸): (پازند) 3 هلندی (لع077): 7
اوستی (05838716): با اسلاوی گهن (ع۲7بما5 تال ۵10+
کردی (70/57): 1 17ج[ ,1۳۳3
بلرچی (ابلتال8۸): 1 روسی (/789314): الا ]
افغانی (پشتر) (//۸70۸): چکه (7ل28)): زد ان
7 ۷ بل۸8۸ لیترانی (/۸(/14لا771لا): انیا
ایسلندی گهن (500/010474(0 0صا0):
,185 پسگشت‌ها ری رد
ساکسرنی کهن (54260(0 0ا0): 58 ان را
فریزی کهن (۲7/3142 صا0): ۱ 3 (1۴8) ان
آلمانی کهن ((052244 ۷104( 80ا0): قا 2 (۸68ا) :ما۸5
آلمانی (058244(۷): 5 6970 ملعتاظ
انگلیسی کهن (5(701/8 ظا0): 15 8 (1۴8) 005
انگلیسی (6۸/87): لنش 5 (068) :7 ۱
ی وانمارکی (بزوال(مط): 15 17 ای دا رد مد هن
سوئدی (81752154): 8 15 برهان قاطع + ۳۴۳۷
1*۹
اوستایی (/4۷2974۸): ۷۸۸ 0 ۷۸20۸ ۷۸2۲20
پهلری (1مال۳۸): کردی (ل70/5/): 120۸7
```


## [2026-09-05T20:27:42.247Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:2427 --image 2>&1 | tail -40",
 "description": "Fetch Borhan-e Qate page 2427"
}
```


### [2026-09-05T20:27:49.022Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 510; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2427.png
REF: BQT:2427  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 510  OCR-lang: fas

بیان چهارم
در بای حطی با خای نقطه دار مشتمل بر چهار لفت وکنایت
یخچه! - بنتح ارل وجیم فارسی | هرچیزی باشد ازمال و اسباب و غله وحبوبات
وسکون ثانی, ژاله وتگرك را کویند. وفیرهم که آلرا نگاهدارند تا بوقت حاجت بکار
بخ در بهشت - نوعی ازحلوا باعد ؛ آید۴ (۱) - وگوشت پخته شده وکرم وسردرا
ویعی گوبند نوعی ازحلوای براج ات۳ .۰ نیز کوینده ای
یخی - بنتح اول وسکون ثالی و نون بعْ « بفتع دو بای حطی و سکون
بتحتالی کشیدم, بممنی پخته باشد که در مقابل | دوخای نقطه‌دار » کلمه‌ایست که ساریانان دروقت
خام است۴ - وبمعنی‌ذخیره هم آمده است وآن | خواییدن شترکوبند .
[ 69 خم۱: بکار برند .
۱ از: بخ ۳+ چه (پسوند تصفیر) «بخچه » تگر که باشد. رود کی (سمرقندی) گوید :
بخچه بارید و پای من بفرد ورغ بر بند بخچه را از فلك .
هم رود کی کوید :
بخچه می بارید از ابر سیاه چون ستاره بر زمین از آسمان.»
«لفت فری ص100
۴ - نام حلوائی است که ازشاسته وشیر وشکر وکلاب پخته میشود «فرهنکه نظام» .
۳ ‌- رد ها ۰
ی - مخور غم زصیدی که با کرده‌ای که بخنی بود آنجه با خورده‌ای.
نظامی کنجوی «جهانگیری» « کنجينهٌ کنجرّی‌س۱۹۹*.
- بخنی, گوشت مهرا پخته ومعروفت «فرهنکه دیوان اطعمةٌ بحاق چاپ استالبول
ص۸۶ - بخنی» درخراسان بفمی‌پل و که درآ ن گوشت درنه دیکه گذاشته میشود ولفظ دیگرش
ته چین است (اطلاق کنند) «فرهنکه نظام» وآ درا بخنی پلو کوبنه « کنابادی» ورك: مادة الحیوة
در «فرهنگه ایران زمین» ۳:۱ ص۲۳۱.
2 وخ - بفتحاول؛ ارستا-2678 (یخ) (1۸3.4 .2110 .2 .36107 , 16تفوها ع0)
با بخ بندان (55 ,[1 5400160 ‎ )88740010286,‏ پازند 80 کر دی واففانی ع ۰635
استی ۷67 ۰ 1۳ (یخ» نگرکه). وخیکذلا «اسشق ۱۱۲۹ کیلکی 25لا . رك: بخجال, رخچه؛
آب منجمد پرائی سردی پسیار :
چنان شد که کفتی طراز لخ است و با پیش آتش نهاده بخ است .
فردوسی طوسی «شاهنامةٌ بخ ج۳ س۵۳۲ .۰
- لیز بم‌عنی برف مرادف ثلج عریی. رلك: التفهیم بیرولی. مقدمه ص۲۵۱
۵ وعجال - بفتح اول, ازیخ + چال (۸.م.) ؛ گودالی که در آن بخ دگاهداری کنند
برای‌فضصل کرما. کودالی که بهنگام زمتان درآنآب بندند با منجمد کردد وجورت پخ درآید -
بخچال برقی» آلنی که بوسيلةٌ الكکتريك تولید بخ کند. ومایعات واشیاة را سرد نگاهدارد .
2 -کرببان ر4: بقه. - نومی نان رك: پوخه .
```


## [2026-09-05T20:28:04.953Z] TOOL CALL #44: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2427.png"
}
```


### [2026-09-05T20:28:05.490Z] TOOL RESULT

```

```


## [2026-09-05T20:28:05.487Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-05T20:28:40.759Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; cat > data/verification/sources/refs/ocr/BQT/2427.vision.txt <<'EOF'\n[BQT:2427 = Borhan-e Qate', ed. Mo'in, vol. 4, pdf page 510 (offset +1917); read from the page image\n data/verification/sources/refs/ocr/BQT/2427.png by vision, 2026-09-05. Section header:\n «بیان چهارم — در یای حطی با خای نقطه‌دار مشتمل بر چهار لغت و کنایت»]\n\nHeadwords on the page: یخچه، یخ در بهشت، یخنی، یخ یخ.\n\nMo'in's etymological footnote no. 5 (bottom of the page), verbatim as printed:\n\n«۵ یخ ـ بفتح اول، اوستا aēxa (یخ) (de Lagarde, Beitr. 2. altb. Lex. 4)\n یا یخ بندان (Bartholomae, Studien II, 55)، پازند yah، کردی و افغانی yex،\n استی yex ، îx (یخ، تگرگ)، وخی yix، «اشتقاق ۱۱۲۶»، گیلکی yax.\n رك: یخچال، یخچه؛ آب منجمد برائر سردی بسیار:\n چنان شد که گفتی طراز یخ است / و یا پیش آتش نهاده یخ است.\n فردوسی طوسی «شاهنامهٔ یخ ج۳ ص۵۳۲».\n ـ نیز بمعنی برف مرادف ثلج عربی. رك: التفهیم بیرونی، مقدمه ص۲۵۱»\n\n«۵ یخچال ـ بفتح اول، از یخ + چال (ه.م.)؛ گودالی که در آن یخ نگاهداری کنند برای فصل گرما …»\n«۱ … از: یخ + چه (پسوند تصغیر) «یخچه»، تگرگ که باشد. رودکی (سمرقندی) گوید: …»\n\n[Note: «اشتقاق ۱۱۲۶» is Mo'in's abbreviation for P. Horn, Grundriss der neupersischen\n Etymologie, entry no. 1126 (= printed p. 252), i.e. Nourai's HRN:252.\n The printed page number itself is not visible on the scan; the page is identified by the\n offset (+1917) and by its position in the alphabet (یخ near the end of vol. 4).]\nEOF\nls -l data/verification/sources/refs/ocr/BQT/2427.vision.txt"
}
```


### [2026-09-05T20:28:40.818Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 1757 Sep  5 16:28 data/verification/sources/refs/ocr/BQT/2427.vision.txt
```


## [2026-09-05T20:28:42.386Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DB%8C%D8%AE",
 "prompt": "Give the full Persian etymology section for یخ (yax) 'ice' — the proto-forms cited, the PIE root, cognates, and any references (Hasandust, Cheung, etc.)."
}
```


### [2026-09-05T20:28:48.554Z] TOOL RESULT

```
# Persian Etymology for یخ (yax) 'ice'

## Proto-Forms and Root

The term derives from "Proto-Iranian *Háyxam," which ultimately traces back to "Proto-Indo-European *h₁eyH-."

## Cognates

The Wiktionary entry lists several related words across Indo-European languages:

- Ossetian: *их* (ix)
- Pashto: *يخ* (yax)
- Lithuanian: *ýnis* ("glazed frost")
- Russian: *и́ней* (ínej, "hoarfrost")
- German: *Eis*
- English: *ice*

## Descendants

The word spread into Hindustani languages, with Hindi preserving *यख़* (yax) and Urdu maintaining *یَخ* (yax).

## Notes

The entry does not cite specific scholarly references like Hasandust or Cheung. The etymology section provides comparative linguistic evidence but relies on the Wiktionary reconstruction framework rather than detailed academic citations.
```


## [2026-09-05T20:29:02.270Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C3%A1yxam",
 "prompt": "Give the reconstruction page in full: the PIE root cited, the meaning, all descendants listed (Avestan, Persian, Ossetian, Pashto, Sogdian, Khotanese...), and any notes on the initial y- of Persian yax."
}
```


## [2026-09-05T20:29:03.279Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ice",
 "prompt": "Give the full etymology of \"ice\": Old English, Proto-Germanic form, and any Avestan/Iranian cognates or PIE root mentioned."
}
```


### [2026-09-05T20:29:09.083Z] TOOL RESULT

```
# Etymology of "Ice"

**Old English:** *is* ("ice, piece of ice")

**Proto-Germanic:** *\*is-* (source also of Old Norse *iss*, Old Frisian *is*, Dutch *ijs*, German *Eis*)

**Origin:** The word has "uncertain origin," though possible relatives include:
- Avestan *aexa-* ("frost, ice") and *isu-* ("frosty, icy")
- Afghan *asai* ("frost")

**PIE Root:** The document does not explicitly identify a Proto-Indo-European root for "ice" itself, though it notes the uncertain origins and suggests these scattered cognates across language families. The modern spelling emerged in the 15th century, giving the word a more French appearance.
```


### [2026-09-05T20:29:10.186Z] TOOL RESULT

```
# Proto-Iranian *Háyxam - Reconstruction Summary

## PIE Root
The term derives from Proto-Indo-European *h₁eyg- ("ice, frost") plus the suffix *-s, reconstructed as *h₁óyg-s ~ *h₁ig-s-és.

## Meaning
"Ice, frost"

## Key Descendants

**Central Iranian:**
- Younger Avestan: aēxəm

**Northeastern Iranian:**
- Ossetian (Digor): ex; (Iron): ix
- Khwarezmian: ʾyx, yyx
- Sogdian: yxnw (yaxn, "ice")
- Yaghnobi: ӣх, ех

**Southeastern Iranian:**
- Pashto: asáy ("hoar-frost; fog; mist")
- Yidgha: yāx ("cold")
- Shughni/Roshani: īš

**Northwestern Iranian:**
- Gilaki: yəx ("ice")
- Mazanderani: yax ("ice")

**Southwestern Iranian:**
- Middle Persian: yax (ēx, "ice")
- Persian: yax ("ice")

## Note on Initial y-
The Persian y- represents the regular phonetic development from Proto-Iranian *H-, which underwent lenition and vocalization to become the glide y- in descendants like Persian yax.
```


## [2026-09-05T20:29:24.628Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"yax\" KNT.txt | head -20; echo \"== v section\"; grep -n \"vi-yax\\|Vi-yax\\|viyax\" -i KNT.txt | head"
}
```


### [2026-09-05T20:29:24.690Z] TOOL RESULT

```
358:67. Тнк Mepran Рглгест was the language of the great Median Empire, which at the death of Cyaxares in 594 extended from the Indus to the Aegean Sea; the last Median ruler was Astyages, son of Cyaxares, who in' 559 was conquered and deposed by his grandson Cyrus, son of Cambyses King of Persis and of Mandane daughter of Astyages. The new ruler naturally took over the Median chancellery and the Median royal titles, and their influence is still seen in the language of the OP inscriptions of Darius and his followers.
382:Uvarsira ‘Cyaxares’, a king of the Median line, with {т retained after a sibilant.
622:a. Regularly in the -ahyà genitive of the month name, before mahyd: Viyaxnahyd тауа DB 1.37; other examples 1.42, 96; 2.26, 36, 41, 56, 61, 69, 98; 3.7f, 18, 39, 46, 63, 68; and re- stored in 1.89, 3.88.
1103:679. РАН. ir AFTER SPIRANTS (including the sibilants) appears unchanged in Avestan. This seems to have been the development also in Median, as in the name of the Меде Uvaz&tra- ‘Cyaxares’, Elam. ma-ak-i§-ta-ra, АКК. ú-ma-ku- iš-tar. The name of the northeastern province Bactria, Gk. Béxrpa, likewise shows a non-OP form in Bazirig, Elam. ba-ik-tur-ri-i$, АКК. ba-ab- lar; but à pure OP *Büz&s or *Báxgis is attested by the alternative Elam. ba-ak-&i-i$. Finally, OP uSa-bari- ‘camel-borne’, by comparison with Av. ustra- ‘camel’, shows that in OP, even after a spirant or a sibilant, tr became ør and then ç, and that after š the с was assimilated to that preceding š.
1577:The month-names  Adukanaisa-, Andmake-, Viyaxna-; for two other month-names cer- tainly have it (see above).
1962:Perhaps with vriddhi in prefix: Vi-yax-na- (radi- cal element uncertain). .
3488:36 sdva : І martiya : magus : dha : Gaumáta : пата : hauv : udapatatà : hacd : Рай 37 yduvadaya : Arakadri$ : n&ma : Каша : hacd : avadaSa : Viyaxnahya : mah
3641:98 m : aja : vasiy : Viyaxnahya : máhyà : X XII : raucabis : Sakata : dha : avatáSám : hamaranam : kartam
3657:$24. 2.18-7. Saith Darius the King: One man, by name Phraortes, а Median—he rose up in Media. To the people thus he said, "I am Khsha- thrita, of the family of Cyaxares." Thereafter the Median army which (was) in the palace, became rebellious from me, (and) went over to that Phraortes. He became king in Media.
3683:§33. 2.78-91. Saith Darius the King: One man by name Cicantakhma, a Sagartian—he became rebellious to me; thus he said to the people, “I am king in Sagartia, of the family of Cyaxares.” Thereupon І sent off a Persian and Median army; a Mede by name Takhmaspada, my subject—
3747:65 yàparam : hamiciya : hagmatà : paraità : patiš : Vivanam : hamaranam : cartana 66 iy : Gadutava : nàmà& : dahyáus : avadd : hamaranam : akunava : Auramazdima 67 iy : upastam : abara : vasnà : Auramazdāha : kira : һуа : mana : avam : káram : t 68 yam : hamigiyam : aja : vasiy ; Viyaxnahya : mahya : ҮП : raucabié : ðakatā :
3906:and the same year after that I became king. XIX battles I fought; by the favor of Ahuramazda I smote them and took prisoner IX. kings. One was Gaumata by name, a Magian; he lied; thus he said: ^I am Smerdis, the son of Cyrus;" he made Persia rebellious. One, Agina by name, an Elamite; he lied; thus he said: “I am king in Elam;" he made Elam rebellious. One, Nidintu- Bel by name, а Babylonian; he lied; thus he said: “Т am Nebuchadrezzar, the son of Nabonidus;" he made Babylon rebellious. One, Martiya by name, a Persian; he lied; thus he said: "I am Imanish, king in Elam;" he made Elam rebellious. One, Phraortes by name, à Mede; he lied; thus he said: "I am Khshathrita, of the family of Cyaxares;" he made Media rebelhous. One, Cicantakhma by name, a Sagartian; he lied; thus he said: "I am king in Sagartia, of the family of Cyaxares;” he made Sagartia rebellious. Опе, Frada by name, a Margian; he lied; thus he said: “I am king in Margiana;" he made Margiana rebellious. One, Vahyazdata by name, a Persian; he lied; thus he said: “I am Smerdis, the son of Cyrus;” he made Persia rebellious. One, Arkha by name, an Armenian; he lied; thus he said: “T am Nebuchadrezzar, the son of Nabonidus;” he made Babylon rebellious.
4103:Tux Inscriptions or NaAQS-1-RugTAM. DNa = Darius, Nags-1-RustaMm A. 1 baga : vazraka : Auramazda : һуа : im 2 ām :bümtm :adà : hya : avam : asm 9 апат :adà : һуа : martiyam :adà : h 4 ya : Siyatim :adā : martiyahyà 5 :hya : D&rayavaum :xšāyaðiyam : ak 6 unau$ : aivam : parüvnàm : xSdyaé 7 iyam :aivam : parüvnàm : framátà 8 ram : adam : DarayavauS : xsayatiya : va 9 zraka : xSàyafiya : xSdyafiyanim 10 : xSdyaiya : dahyünàm : vispazaná 11 nam : х$йуайуа :abyáyà : шт ` 12 уа :уалаКауй : diiraiapiyf: Vistas 13 pahyà : puça : Haximanisiya : Parsa : P 14 àrsahyà : риса : Ariya : Ariya : ei 15 с̧а :0atiy : Darayavaus : xsaya 16 fiya : vašnā : Auramazdaha : ima : 17 dahyáva : {уй : adam : agarbáyam : 18 apataram : haeà : Ратѕа : adamsàm : 19 patiyaxSayaiy : manā : bàjim : abara 20 ha : tyasàm : hacdma :afahya :ava : a 21 kunava : dàtam : tya : mani : avadis : 22 adaraiya : Mada : Uvja : Parfava : Harai 23 va : Bàxtri$ : Suguda : Üvürazm 24 i$ : Zraka : Harauvatis : Gatagus : Ga 25 dara : Hidug : Saki : haumavargà : Sa 26 kā : tigraxaudà : Bābiruš : A 27 Gura : Arabàya : Mudràya : Armina
4214:DSe = Darius, Susa Е. 1 baga : vazraka : Auramazdà : hya : ima 2 т: bimim : adadé ; һуа : avam : as 3 татат : adadà : hya : martiyam : ad 4 ada : hya : &iyàülim : adad& : mart 5 iyahyü : hya : Darayavaum : XŠm : ak 6 unauš : айбат : parūvnām : XSm : a 7 шат : parüvnüm : framálàram : a 8 dam : Darayavaus : XS : vazraka : XS : XSy 9 anim : XS : dahyünám : vispazanü 10 nam : XS : ahyaya : bümiyà : vaz 11 rakàyà : düraiy : apiy : Vistas 12 pahyà : puça : HazamaniSya : Рат 13 sa : Pārsahyā : рисо : Ariya : Ari 14 ya : ciga : 08tiy : Dàrayavaus : XS : 15 уа&па : Auramazdaha : imá : dahy 16 āva : {уй : adam : agarbayam : apaia 17 ram : hacd : Parsa : adamsdm : pat 18 iyaxíayaty : manā : bajim : abara : 19 tyasam : hacéma : afahya : ava : aku 20 nava : datam : tya : mand : avadis : a 21 dáraya : Майа: Uja : Parðava : Haraiva : 22 Baatris : Suguda : Uvarazmis 23 : Zrdka : Наташайх : Bataguš : Maci 24 уй : Gadàra : Hidus : Зака : haumava 25 rgà : Saká : tigrazaudà : Babir 26 u$ : Авита : Arabéya : Мийгаа : 27 Armina : Katpatuka : Sparda : Yaun 28 à : аву : drayahya : ula : уа 29 y : paradraya : Skudra : Putayà : 30 Kuxiyd : Karka ; 6àtiy : Рата 31 yavau& : XS : vasiy : tya : duskarta 32 m : Gha : ava : naibam : akunavam : da 33 hyáva : ayauda : aniya : aniyam : 34 aja : ava : adam : akunavam : vašnā 39 : Auramazdaha : уаба : aniya : a 36 шуат : пау : jatiy : cind : gà 37 fava : kaSciy : astiy : дат : 38 tya : maná : haeá : avana : tarsat 39 y : улда : hya : tauviyd : tyam :s 40 kauéim : naiy : jatiy : naiy : vi 41 mardatiy : байу : Dérayavaus :
4572:17 patiyaxsayaly : manā : bajim : abaraha : t
4881:Phraortes, claiming to be Khshathrita, of the family of Cyaxares, had made himself king of a great part of the Empire ($21). Darius’s first step was to send Vaumisa, a Persian officer, against the rebels in Armenia; he must have sent Vaumisa early in the Babylonian campaign, for Vaumisa, on the way north, was met by the rebels at [zala in Assyria, on X 15. What forces Vaumisa had at his disposal is not stated, but no mention 1s made of sending troops with him; presumably he gathered up loyal troops on the way. By,this battle Vaumisa
4890:hered to Phraortes, declared himself King in Sagartia, a distriet of northern Media; he claimed to be of the family of Cyaxares. Darius sent а force of Medes and Persians under Takhmaspada, a Median officer, who defeated and captured Cicantakhma, bringing him to Darius. Darius mu- tilated him and put him to death with torture, at Arbela ($33). Thus ended rebellion in Media (884) ; but there was still a strong rebel force in Armenia, against which Darius sent an Armenian officer named Dadarshi. Dadarshi, thrice attacked by the rebels, defeated them successively at Zuzaya on II 8 (§26), at Tigra on II 18 (§27), and at Uyama on III 9, whereafter he waited for Darius to come and make final governmental dispositions (828). This third battle by Dadarshi was only nine days after Vaumisa in а second engagement beat off the other force of Armenian rebels in the dis- trict of Autiyara, on IT 30; after which he also awaited Darius’s arrival (530). There was по fur- ther fighting in Armenia.
5205:‘UvaaStra- sb. ‘Cyaxares’, former King of Media: Elam. ma-ak-tš-tar-ra, АКК. ú-ma-ku-iš- lar, Gk. Kva£ápys. From u- ‘good’ + varštra- ‘growth’ ($9.11, $79, $148.11), to vaxi-, Av. vazš-, Skt. vaks-, Gm. wachsen, N Eng. wax ($102): 'Hav- ing good growth’ ($164.11, IV). So ВЫ. AiW 1836; but Hz. АрІ 209 interprets ‘having good oversight’, to Av. aiwy-axrstrat (dat.) ‘oversight’ (otherwise Hüsing, OLZ 2.139-40). Стах аһу gsm. DB 2.15f, 81.  Uvaxstrahya (S86.IVb) DB 4.19, 22; DBe 7; ОВр 9f.
== v section
622:a. Regularly in the -ahyà genitive of the month name, before mahyd: Viyaxnahyd тауа DB 1.37; other examples 1.42, 96; 2.26, 36, 41, 56, 61, 69, 98; 3.7f, 18, 39, 46, 63, 68; and re- stored in 1.89, 3.88.
1577:The month-names  Adukanaisa-, Andmake-, Viyaxna-; for two other month-names cer- tainly have it (see above).
1962:Perhaps with vriddhi in prefix: Vi-yax-na- (radi- cal element uncertain). .
3488:36 sdva : І martiya : magus : dha : Gaumáta : пата : hauv : udapatatà : hacd : Рай 37 yduvadaya : Arakadri$ : n&ma : Каша : hacd : avadaSa : Viyaxnahya : mah
3641:98 m : aja : vasiy : Viyaxnahya : máhyà : X XII : raucabis : Sakata : dha : avatáSám : hamaranam : kartam
3747:65 yàparam : hamiciya : hagmatà : paraità : patiš : Vivanam : hamaranam : cartana 66 iy : Gadutava : nàmà& : dahyáus : avadd : hamaranam : akunava : Auramazdima 67 iy : upastam : abara : vasnà : Auramazdāha : kira : һуа : mana : avam : káram : t 68 yam : hamigiyam : aja : vasiy ; Viyaxnahya : mahya : ҮП : raucabié : ðakatā :
```


## [2026-09-05T20:29:24.949Z] TOOL CALL #50: WebSearch

```json
{
 "query": "Old Persian month Viyaxna etymology \"ice\" Sogdian yaxn Achaemenid calendar"
}
```


### [2026-09-05T20:29:33.367Z] TOOL RESULT

```
Web search results for query: "Old Persian month Viyaxna etymology "ice" Sogdian yaxn Achaemenid calendar"

Links: [{"title":"(PDF) The Old Persian month name viyax(a)na-, Avestan viiāx(a)na- ‘eloquent, bragging’ and Ossetic festivals.","url":"https://www.academia.edu/2068497/The_Old_Persian_month_name_viyax_a_na_Avestan_vii%C4%81x_a_na_eloquent_bragging_and_Ossetic_festivals"},{"title":"The Old Persian Month Name Viyax (A) Na-, Avestan Viiāx (A) Na - Eloquent, Bragging' and Ossetic Festivals | PDF | Sanskrit | Languages","url":"https://www.scribd.com/document/217278780/The-Old-Persian-Month-Name-Viyax-A-Na-Avestan-Vii%C4%81x-A-Na-Eloquent-Bragging-and-Ossetic-Festivals"},{"title":"The Old Persian month name viyax(a)na-, Avestan viiāx(a)na","url":"https://scholarlypublications.universiteitleiden.nl/access/item:2882943/view"},{"title":"Zoroastrianism - The Old Iranian Calendars, Part 6","url":"https://www.hinduwebsite.com/zoroastrianism/calendar6.asp"},{"title":"Who Used Darius the Great to divide Persian and Medes (Kurds) People?","url":"https://theinsightinternational.com/mismas/articles/misc2013/5/state7088.htm"},{"title":"Sogdia","url":"https://en.wikipedia.org/wiki/Sogdia"},{"title":"CALENDARS - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/calendars/"},{"title":"Nana (Bactrian goddess)","url":"https://en.wikipedia.org/wiki/Nana_(Bactrian_goddess)"},{"title":"Persian Months, ORIGIN OF THE NAMES » IranOnline.com","url":"https://www.iranonline.com/festivals/persian-months-origin-of-the-names/"}]

Based on the search results, I found relevant information about the Old Persian month Viyaxna and its etymology:

The twelfth and last month of the Old Persian calendar, corresponding to Akkadian Addāru (February-March), appears in the Behistun inscription as v i -i-y-x-n-. 

Regarding the etymology, Viyaxna is translated as "Ice-Melt" and corresponds to Esfand (February/March). This confirms the connection to "ice" mentioned in your query.

The search results also reference scholarly work examining the Old Persian month name viyax(a)na- alongside its Avestan equivalent viiāx(a)na-, though the specific connection to Sogdian "yaxn" was not detailed in these particular results. The results do indicate that the month names were seasonal in nature, with the Old Persian month names reminding one of the Gathic Gāhānbār and the Vedic Calendar festivals and months, all named after seasonal activities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:29:45.696Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://scholarlypublications.universiteitleiden.nl/access/item:2882943/view",
 "prompt": "Who is the author, what journal/year, and what is the argument about the Old Persian month name viyax(a)na-? Does the paper reject the connection with 'ice' (Sogdian yaxn) and propose Avestan viiāx(a)na- 'eloquent, bragging' instead? Quote the abstract or key sentences."
}
```


### [2026-09-05T20:29:55.145Z] TOOL RESULT

```
I apologize, but I cannot extract the requested information from the provided content. The web page appears to be a PDF document rendered as corrupted or binary data, making it impossible to read the actual text content, author information, journal details, or any arguments about Old Persian month names.

To properly answer your question about the author, journal/year, and the argument regarding viyax(a)na- and its connection to Sogdian yaxn or Avestan viiāx(a)na-, I would need:

1. A readable version of the document
2. Access to the article's metadata (author, publication details)
3. Clear text containing the abstract or relevant sections

Please provide the document in a readable format (plain text, properly rendered PDF, or a link to the source) so I can give you an accurate response.

[Binary content (application/pdf, 249.1KB) also saved to /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/webfetch-1788640191754-2pb8ri.pdf]
```


## [2026-09-05T20:29:58.087Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; F=/home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/webfetch-1788640191754-2pb8ri.pdf; (pdftotext \"$F\" - 2>/dev/null || echo NOPDFTOTEXT) | head -80"
}
```


### [2026-09-05T20:29:59.747Z] TOOL RESULT

```
The Old Persian month name viyax(a)na-, Avestan
viiāx(a)na- ‘eloquent, bragging’ and Ossetic
festivals.
Lubotsky, A.M.; Sadovski Velizar, Stifter David

Citation
Lubotsky, A. M. (2012). The Old Persian month name viyax(a)na-,
Avestan viiāx(a)na- ‘eloquent, bragging’ and Ossetic festivals. In
S. D. Sadovski Velizar (Ed.), Iranistische und indogermanistische
Beiträge in Memoriam Jochem Schindler (1944-1994) (pp.
95-106). Wien: Verlag der Österreichischen Akademie der
Wissenschaften. Retrieved from
https://hdl.handle.net/1887/20056
Version:

Not Applicable (or Unknown)

License:

Leiden University Non-exclusive license

Downloaded from:

https://hdl.handle.net/1887/20056

Note: To cite this publication please use the final published
version (if applicable).

THE OLD PERSIAN MONTH NAME VIYAX(A)NA-, AVESTAN
VIIĀX(A)NA- ‘ELOQUENT, BRAGGING’ AND OSSETIC FESTIVALS
Alexander LUBOTSKY (Leiden)

1. The twelfth and last month of the Old Persian (OP) calendar, corresponding to Akkadian Addāru (February – March), appears in the Behistun
inscription as vi-i-y-x-n-. Its Elamite equivalent is spelled in the same inscription Mi-ya-kán-na-iš (DB II 72, III 29) and Mi-kán-na-iš (DB I 28). On
the Persepolis tablets we find sixteen different spellings of this Elamite
word, the most frequent ones being Mi-ya-kán-na-iš/-aš, Mi-ya-kán-na-, Mikán-na-iš, Mi-kán-na- (Schmitt 2003: 24). The Elamite spellings indicate
that OP vi-i-y-x-n- must be read as viyax(a)na-, while the shorter form Mikán ̊ points to the later (already in the time of Xerxes) OP contraction -iya> -ī-, for which cf. Kent 1953: 13.
In the above-mentioned publication, Schmitt (p. 43) goes even further
and argues that “die weit überwiegenden Schreibungen mit -kán- ... und die
Schreibungen mit -qa-na- lassen zwingend darauf schließen, daß die Sequenz altpers. -x-n- als /-xan-/ zu verstehen ist”. It seems to me, however,
that these spellings can only indicate that the Elamites heard [viyaxana] or
[viyaxəna], which does not necessarily mean that the OP word had a phonemic vowel between x and n. We shall return to this point below.
Schmitt (p. 44) further discusses the etymologies that have been proposed
for OP Viyax(a)na- and discards them all. On the whole, his criticism is justified, but, in my opinion, the etymological suggestion by Oettinger deserves
more credit. In a footnote, Oettinger (1983: 258, fn. 38) remarked that “viyaxana- wahrscheinlich ‘(Monat der) Versammlung’ heißt und zu av. viiāxana- (vermutlich: ‘Versammlung’) gehört”, but Schmitt considers this unlikely for formal (long ā in Avestan) and semantic reasons: “Avest. viiāxanaselbst kommt nur als Personenbezeichnung vor, etwa “beredt”; andererseits
aber ist für die Adjektivform, wie sie für den Monatsnamen benötigt wird,

96

Alexander Lubotsky

avest. viiāxa- 1 nicht der richtige Ausgangspunkt, und schließlich führt der
Vergleich dieser Wortfamilie auch im Semasiologischen nicht weiter.” In the
following I shall try to show that Oettinger’s connection of OP Viyax(a)nawith Av. viiāxana- is both formally and semantically cogent.
2. The discrepancy in the vocalism between OP Viyax(a)na- and Av. viiāxana- can easily be accounted for by the well-known Avestan lengthening
of short a in the position after , cf. aiβiiāma- ‘offensive’, aiβiiāuuah- ‘assistance’, viiāxti- ‘make-up’, viiārəθa- ‘misused’, etc. (Hoffmann – Forssman 1996: 57). As is shown by de Vaan (2003: 31ff.), this lengthening only
occurs when the preceding C goes back to *Ci. In other words, the rule is
*Cia > Cā. This means that viiāxana- can go back to *iaxana- 2.
Another point is the original form of the Avestan word, which is attested
in two spellings, viiāxna- and viiāxana-. Kuiper (1960: 243ff.) meticulously
studied the manuscript tradition and concluded that the reading viiāxanamust be the original manuscript reading. Also the metrical passages of the
Yashts seem to point in this direction. There are three passages (Yt 10.25,
10.61, 13.85) where the word must be scanned in four syllables and five passages (Yt 5.73, 10.61, 13.16, 52, Ny 3.10) where the word must be scanned
in three syllables. The most straightforward way to account for these facts is
that the poets used either [vyāxana-] or [viyāxana-], according to the metrical needs (thus already Geldner 1887: 31, 39; Kuiper 1960: 244).
Nevertheless, Kuiper was reluctant to assume an original Avestan form
viiāxana-, because such a form can only be explained as a derivative of an
Iranian root *()kh-, and the prospective of reconstructing a root with a
voiceless aspirate is not very inviting, indeed. Therefore, he preferred to explain viiāxana- in terms of an anaptyctic vowel, similar to š́ iiaoθ(a)na- n.
‘action’, which is written š́ iiaoθna- in the Yashts and the Vendidad, wheras
the Yasna text always has š́ iiaoθana-. The latter form is not only written, but
also scanned a few times in three syllables. This analysis of viiāx(a)na- has
the advantage of providing us with an option to explain Iranian -xn- from an
earlier *-kn-.

1

2

As a matter of fact, Av. viiāxa- does not exist, Gāh 2.8 viiāxəmca being a corruption of
```


## [2026-09-05T20:30:07.895Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; F=/home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/webfetch-1788640191754-2pb8ri.pdf; pdftotext \"$F\" - | grep -n -i \"ice\\|yaxn\\|frost\\|Eis\\b\" | head -20; echo \"=== conclusion\"; pdftotext \"$F\" - | sed -n '/^10\\./,$p' | head -40"
}
```


### [2026-09-05T20:30:09.844Z] TOOL RESULT

```
18:License:
20:Leiden University Non-exclusive license
69:voiceless aspirate is not very inviting, indeed. Therefore, he preferred to explain viiāxana- in terms of an anaptyctic vowel, similar to š́ iiaoθ(a)na- n.
224:practiced during the Tutyr in the Digor gorge are exactly the same as the
257:on Sunday and lasting one or two weeks. The night from Monday to Tuesday of the first week (Wastyrǯi ’xsæv) was the most essential part of the festival, when a goat was sacrificed to the saint. During this night every family
259:wherever it may live and however poor it may be, always celebrates this festival with an animal sacrifice because Wastyrǯi is the most revered Ossetic
=== conclusion
10.61, 13.85) where the word must be scanned in four syllables and five passages (Yt 5.73, 10.61, 13.16, 52, Ny 3.10) where the word must be scanned
in three syllables. The most straightforward way to account for these facts is
that the poets used either [vyāxana-] or [viyāxana-], according to the metrical needs (thus already Geldner 1887: 31, 39; Kuiper 1960: 244).
Nevertheless, Kuiper was reluctant to assume an original Avestan form
viiāxana-, because such a form can only be explained as a derivative of an
Iranian root *()kh-, and the prospective of reconstructing a root with a
voiceless aspirate is not very inviting, indeed. Therefore, he preferred to explain viiāxana- in terms of an anaptyctic vowel, similar to š́ iiaoθ(a)na- n.
‘action’, which is written š́ iiaoθna- in the Yashts and the Vendidad, wheras
the Yasna text always has š́ iiaoθana-. The latter form is not only written, but
also scanned a few times in three syllables. This analysis of viiāx(a)na- has
the advantage of providing us with an option to explain Iranian -xn- from an
earlier *-kn-.

1

2

As a matter of fact, Av. viiāxa- does not exist, Gāh 2.8 viiāxəmca being a corruption of
viiāxmaca, as was demonstrated by Kuiper 1960: 245.
The same lengthening is attested in the cognate Avestan words viiāxman- ‘ceremonial
meeting’, viiāxmaniieiti ‘speaks in a contest’, for which see below.

Old Persian viyax(a)na-, Avestan viiāx(a)na- and Ossetic Festivals

97

3. Whatever the explanation for the -a- in Avestan viiāx(a)na-, it is clear
that the connection with OP viyax(a)na- is formally impeccable. Before we
discuss the etymology of this word, let us first turn to the meaning of
Avestan viiāxana-. Kuiper (1960: 247ff.) has demonstrated (developing the
ideas of Benveniste in Benveniste – Renou 1934: 44, fn. 3) that viiāx(a)nais an adjective qualifying a warrior as ‘eloquent, victorious in the verbal
contests’. As a typical example of the contexts where it is used I here give
the beginning of Yt 13.16 with Kuiper’s translation:

ŋhąm raiia xvarənaŋhaca

us.nā zaiieiti viiāxanō
viiāxmōhu gūšaiia.uxδō
yō bauuaiti xratu.kātō
yō nāidiiŋhō gaotəmahe
```


## [2026-09-05T20:30:20.797Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HUB\"; grep -n \"jax\\|yax\\|Eis'\" HUB.txt | head -20; echo \"== NYB grep ice\"; grep -n \"'ice'\\|ice,\" NYB_vol2_glossary.txt | head -5; echo \"== KLN ice\"; grep -n \"^ice\\b\\|ice, n\\.\" KLN_1966.txt | head -10"
}
```


### [2026-09-05T20:30:20.913Z] TOOL RESULT

```
== HUB
3518:miyaxd zu sprecben.
4967:yax *Eis, osset. yex, ix^ zd. a^a;a-; yoA: 'ein*, paz. yak, phi.
5318:In yak ein und yax *Eis' geht ya- auf ai- zuriick. So-
5352:stets / ausser in yak ein', yax *Eis', ya- (mit Personalsuffix) als
5356:yak, yax, yazdahum (mit ya- aus e-, s. § 30) und ya- (neben i
7000:semitische Aequivalent yaxsenun- gesetzt), Bdh. Gl. 135 be-
== NYB grep ice
279:a-dātistānēh [’d’tst’nyh; >-DYN?’-yh] in- justice, unfairness 32’, 6213, — V. dätistän. a-dātistānihā [’d’tst’nyh’] unjustly 942. Adbil [’dbyl] the town of Dwin in Ar- menia 1179. — Untenable Cat. 211° sq. Arab. Dabil, Yàqut 1,548 sqq., v. Nyberg, Karlgren Vol. 325 sq.
340:of -h; thus it cannot be connected with dkas (q. v.), which also differs in meaning. From Olr *ā-kāda-, derived through. the suff. -0a- (OInd -tha-) from *kä-, Skr cäyati ‘to notice, to be aware’ (v.s.v. cašm-kāi). As ws. formed by the suff. -tha- are abstracts we have to explain *ā-kāda- as ‘being with information, having good information’. cf Skr ā-manas- ‘being of favorable mind’. As to the spelling, cf
518:apar-kär [”*plk”1] sovereign 5823. — ‘Whose work (office, kär) is supreme’.
557:urvar har cé ne ~ (se. hösitan) à nē hošet 9612-13, 9810-11; — apāyet būtan it is bound to happen, of predestination, explains jäyisn 271, brihenisn 16°; used itself as a nominal expression of Predestination: apäyet-bütan rād 16!!; — b) taking a v. n. as its complement: -šān ... gošt z"arisneh ne — it is not allowed for them to eat meat 10420-21; — e) governing a subordinate clause introduced by kū 8!. 1181-14 by ka 56?? (gl); without an introductory particle, with the governed vb. in ind. or in Subju.: ~ stdyé thou shalt profess 596; bē ~ apesihät 4419-19, v.s. v. apa- sistan. — MPrs ’b’yd with inf. (A-H II); Paz. āwāyastan āwāyad; āwāyastaa ‘re- quisite, desire’ (SGV); NP bäyistan, bā- yad; andar-vdi ‘desire, need (cf above no. 3; to be distinguished from andarvāt ‘atmosphere’, g. v.). Den. of OIr *updya- < *upa-aya- ‘that which comes upon, is imposed upon, affects a p.' = 1. need, 2. duty, cf Av. (150) upa-ay-, v. HP II, 17 sg.; Verbum 168; Ghilain 48. apāyišnīk ['p'dányk] proper, fit, fitting, handsome, nice, exquisite, comp. ~-tar, 33-5. 422, etc. passim; pl. cas. obl. ~-dn the qualified ones 1052,
802:collected and the members of his family acquired — (when it) is lost and gone PT 16613-15; — common theological term ex- pressing the nothingness of Ahriman and the evil powers, especially from an escha- tological point of view: ~ -éh $ Ganäk menči DkM 852, v. also ~ -büteh; andar višuft- A hrimaneh, ~-druzéh), apasihit deveh u nést-paitiyarakéh in a state where Ahriman has been destroyed, the drugs defeated, the devs annihilated, and there are no adversaries DD 798-?; den. vb. avinnitan [>wbynytn']: opt. avinnēš DkM 83811; avinnitäreh DD 7514; avinnenitan, pass. avinnihistan ibd. 765-5; etc.]. — Paz. avin, Skr v. an-upakärin ‘doing no service, useless, fruitless’ (Mx), vikala ‘defective, impaired’ (SGV). FrP ch. 25 gives full evidence as to sense and etymology of this w.: "wbyn'. ’yen. L'YT'.nyst'. heš. heyš (var. hes!, ?zy$), Paz. óbin (K öbin). ēzin (var. aizin, Arab letters ’zyn, ’yzn) rwid nist aziš (var. ajiš), the lemma being: ^wbyn': écin (LYT' =) nast haciš; com- mentary: — l. &in < *atva-cina ‘even one thing’, with neg. ‘no one thing, nothing at all’: Av. (594) -cina encl. emphasizing part. in neg. sentences, (595) cina- ‘whoever’, (595, 762) dväcina ‘two men whoever they may be’, (24) aēvā- cina in obscure context ;. 2. L“YT' glossed by nēst, and ambiguous keš elucidated; 3. the lemma says: *wbyn' means: ‘no one thing comes from it, there is no gain from it’. The reading is almost self-evi- dent: a-vinn <  "a-vinda- from Av. (1318 sqq.) *vaéd- ‘to find, to acquire, to share, to gain’, thus ‘not gaining’; also representing Av. (348) o-vindan- ‘left without any share' (of the food, of dogs Vd. 1378). As to the assimilation of -nd- > -nn-, common in SW, cf MPrs bn = bann < band; BP apa-sinn- (v. s. v. apa- sistan), nivinn- < ni-vind- (g. v.). — This etymology was already given in HP II, and I maintain it firmly. The most un- happy idea of Geiger (WZKM XL, 107), taking ^wbyn as an Aram. ideogr. and
== KLN ice
18583:ice,  n.  —  ME.  is,  fr.  OE.  is,  rel.  to  ON.  iss,  OS., OFris.,  MLG.,  OHG.,  MHG.  is,  Dan.,  Swed. is,  Du.  ijs,  G.  Eis.  Outside  Teut.  cp.  Avestic isav-,  ‘frosty’,  aexa-,  ‘ice’,  Afghanic  asai,  ‘frost’. Cp.  iceberg,  icicle,  Isold.
```


## [2026-09-05T20:30:22.038Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/calendars/",
 "prompt": "What does the article say about the Old Persian month name Viyax(a)na- (the 12th month, Feb-March)? Is any meaning or etymology given for it?"
}
```


### [2026-09-05T20:30:24.011Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T20:30:33.823Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 -c \"\ns=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=s.split('\\n')\nfor t in (4967,5318,5352):\n    leaf='\\n'.join(lines[:t]).count('\\f')+1\n    print(t,'leaf',leaf,'printed',leaf-10)\n\"; echo \"--- context 4960-4970\"; sed -n '4960,4970p' HUB.txt; echo \"--- 5314-5322\"; sed -n '5314,5322p' HUB.txt"
}
```


### [2026-09-05T20:30:35.788Z] TOOL RESULT

```
4967 leaf 153 printed 143
5318 leaf 162 printed 152
5352 leaf 163 printed 153
--- context 4960-4970
zinhdr *Schutz, Sicherheit, gieb Acht! hiite dichf = zinhar
[ztnehar); istadan stehn' ^= np. paz. estddan. Vgl. § 12 und
27 und Sal. Shuk. Gram. p. 15, Dazu hirun = herUn
aussen, heraus* (s. oben p. 33), pindastan 'dafiir halten' ^^
mp. pa in daStan; si *diei' = paz. se (s^) = zd. d^rayqm;
ki Ver, alter k\ paz. he = ap. *kai/a?
Dagegen wird ap. ai im Anlaut zu paz. np. ya- in:
yax *Eis, osset. yex, ix^ zd. a^a;a-; yoA: 'ein*, paz. yak, phi.
evai aus aiva -\~ ka (neben -e ein* = paz. ew-, ev- in Zu-
sammensetzungen Shk. 243 = ap. aiva-).
Kapitel 6: ap. au.
--- 5314-5322
ayadinldan *to remember Shk. 235, np. y(ld\ paz. ay do oder,
np. yd; paz. aydr helper Min. Gl. 27, Shk. 235, np. ydr\
paz. aydftan *to obtain', aydft a favour' Min. Gl. 27, np.
yaftafiy aber zd. dyapta-l
In yak ein und yax *Eis' geht ya- auf ai- zuriick. So-
mit steht np. y fiir urspr. anlaut. y in echtpersischen WQrtem
nur in sehr wenig Fallen. In diesen kdnnte es vielleicht
aus alterem sonantischen y (^) hervorgegangen sein wie np. J
aus alterem spirantischen y, Vgl. § 55.
```


## [2026-09-05T20:30:49.626Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/150.jpg 2>/dev/null || (pdftoppm -f 150 -l 150 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg150 && echo made)"
}
```


### [2026-09-05T20:30:51.411Z] TOOL RESULT

```
site/pages/150.jpg
```


## [2026-09-05T20:30:55.732Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DB%8C%D8%AE' --note 'page 150, root Eis 2, node 2: Persian یخ yax etymology (Proto-Iranian *Háyxam, PIE *h₁eyH-/*h₁eyg-)' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C3%A1yxam' --note 'page 150, root Eis 2: Proto-Iranian *Háyxam ice/frost, descendants Av. aēxəm, Sogd. yxnw yaxn, MP yax, NP yax, Oss. ix' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/ice' --note 'page 150, nodes 5-6: English ice < OE is < PGmc *is-, cf. Av. aexa-, isu-' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://scholarlypublications.universiteitleiden.nl/access/item:2882943/view' --note 'page 150, node 3: Lubotsky 2012 on OP month name viyax(a)na- = Av. viiaxana- eloquent/assembly, not ice' 2>&1 | tail -3"
}
```


### [2026-09-05T20:31:00.395Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/554c060b1225249a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/79cd3e9ffd762724.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4b8cdf160fe6cb50.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c0f6f3efade99040.txt
```


## [2026-09-05T20:31:02.692Z] TOOL CALL #59: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/150.jpg"
}
```


### [2026-09-05T20:31:02.721Z] TOOL RESULT

```

```


## [2026-09-05T20:31:16.079Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,120p tools/verify_check.py"
}
```


### [2026-09-05T20:31:16.116Z] TOOL RESULT

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


## [2026-09-05T20:31:22.546Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== SKT\"; grep -n \"^ICE\\|ICE, frozen\\|ICE\\.\" SKT.txt | head; grep -n \"Icel. iss\\|A.S. is, ice\\|is, ice\" SKT.txt | head"
}
```


### [2026-09-05T20:31:22.614Z] TOOL RESULT

```
== SKT
76:ICELANDIC.    Thia  language  abounds  in  somewhat  similar  vowel- tfciiigcs,  but  very  few  of  these  appear  in  English.     But  we  must  not )U9  ow  the  frequent  formation  of  derivatives  from  the  past  tenses or  plural)  and  tiie  past  participles  of  stronpf  verbs.     Thus btUa,  lit  *  to  cause  to  bite,'  is  the  causal  of  6ffay  to  bite ;  its 17  be  explained  by  the  fact  that  the  pt.  L  of  bUa  is  beii, \,  as  regards  the  Romance  languages,  especially  French,  it borne  in  mind  that  they  also  are  subject  10  phonetic  laws, is  bctUT  known  since  these  laws  have  been  sufficiently  illus- ?**«!  iu  Mr.  Kitchin's   translation  of   Brachet's   Historical    French >oimar.   In  particular,  I  may  note  that  most  French  substantives  are from  Latin  aausativfs ;  and  that  to  derive  bounly  from  botiitas \  or  honour  from  Lat.  honor  (nom.),  is  simply  impossible. Dot  a  litdc  surprising  that  many  etymological  dictionaries ignore  thti^e  most  significant,  elementary,  and  essential  facts. and  very  worthy  exception  is  £.  ^Killer's  Etymologisctics icli  der  Knglischen  Sprache. )in  a  key  to  the  plan  of  the  work,  and  a  list  of  abbrcviatioiiB.
9540:JUICE.
14677:PRACTICE.
```


## [2026-09-05T20:31:23.656Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"aexa\\|isu-\\|yex, ix\\|asai\" WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-05T20:31:23.710Z] TOOL RESULT

```
3089:auf *undher- : *udher -, deren Kasai doch wurzelhaft sein muB, also den 
6493:haben; *po-i zu poe. Und lit. tasai usw. — nur im nom. sg. m. — als 
6969:*o->so[u]-n6s : *isu- „Pfeil“ — vicovog : vlvg, yeimvij : yj/.vg \ oimog , oiazog 
7000:Plierher auch ai. isu-, av. isn- m. „Pfoil u , gr. tog ds. aus '*isu-os (Curtius 5 
8358:ai. nagati , av. nasaiti, ai. nalsati „erreicht, erlangt“, Desid. inaksati 
11078:Ai. (leu- ,,schnell“, Komp. (inyirn. Sup. unstha-, av. Cisu- „schnell“, Komp. 
12552:haufigen Bedeutungsverhaltnis „verlangen : jagen" zu av. yasaiti „langt, 
12642:av. yasaiti ,, wonach langen, verlangen. streben; erbitteiv, mit apa- ,weg- 
12988:drierare (wohl aus -iouesd-, s. Yf. LEWb 2 u. pciero: ein tiefstufiges *iiisu- 
13229:yarn-, yasaite , ap. impf. ayasatcL , Ptc. av. ynta- „halten", yfita- „zugewiesener
```


## [2026-09-05T20:31:28.868Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"eisig\\|Reif“\\|inej\" WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-05T20:31:28.939Z] TOOL RESULT

```
15340:(st. V.) „schwingen, winden“, mnd. wip „Quaste, Reisigbesen, Strohwisch" 
19640:einwickeln ‘, mnd. tease „Reisigbundel, Faschine“, mengl. tease ds. (Fick 
25772:Schnee", andrerseits ksl srem . : weiB (von Pferden)"; lit. sefksnas „Reif“, 
26365:,,Reisig, Buschwerk 1 ', Falk-Torp u. rust II, wobei „Rost aus Flechtwerk 1- 
26367:als ..Reisig zum Yerbrennen 11 unserer Sippe zuzuteilen). 
26566:werk, Rost" harsta „Rost“, mnd. harst ds., „Reisig, Gebiisch, Rost" (wovon 
26570:Siitterlins, IF. 25,61 Vergleich von Horst mit ksl. chvrastije „Reisig" — 
27048:salna „Reif“ (lett. sahvt), pamlas „gefrorene Erde“ = apr. passalis „Frost“, 
27537:47, 302), Demin. xXrjpazig bes. PI. ,,Reisig“; y.Xqgog, dor. y.Xdoog m. ,.Holz- 
29098:kor- „Reiserbesen (und damit fegen); Reisigbiindel (als Fischreuse, als
```


## [2026-09-05T20:31:34.786Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"ahd. is \\|as. ahd. is\\|aisl. iss\\|anord. iss\\|ags. is \" WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"@@ pages file\"; grep -n \"aisl. iss\\|iss, Pl\\|isu- „eisig\" WLD_Bd1_pages.txt | head"
}
```


### [2026-09-05T20:31:34.868Z] TOOL RESULT

```
7019:Altn. tss, pi. Isar m. „Eis“, ags. is n., mnd. Is n., ahd. mhd. is n. dss. 
@@ pages file
```


## [2026-09-05T20:31:37.358Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '7008,7030p' WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T20:31:37.412Z] TOOL RESULT

```
10S 


eis- — eu-, eua- 


2. cis- „Eis“. 

Altn. tss, pi. Isar m. „Eis“, ags. is n., mnd. Is n., ahd. mhd. is n. dss. 
Moglicherweise verwandt mit av. aeya- „Frost, Eis“, isu „kalt“ (von einer 
Inchoativbildung *is-sk-). Ygl. Geiger, Etym. u. Lautl. d. Afghan. 7. Bar- 
tholoniae ZDMG. 50, 697, Fick III 4 28, Falk-Torp 468, 1490. 

Uhlenbeck PBBeitr. 26, 294 f. stellt germ. Isa weniger iiberzeugend zu 
ai. Usati (s. eis „sieh heftig bewegen“). Yerwandtschaft mit „Eisen“ (Kluge 
EWb.) ganz unglaubhaft. 

1. eu-, eua- „mangeln; leer“, bes. in partizipialen wo-Bildungen. 

Ai. und-, av. ana- „unzureichend, ermangelnd a , av. uyamna- „ungeniigend,
```


## [2026-09-05T20:32:14.949Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== BRT viiaxana\"; grep -n \"vyaxana\\|viyaxana\\|vlyaxana\\|vyaxna\\|beredt\" BRT.txt | head -10; echo \"== SKT ice\"; grep -n -i \"icicle\" SKT.txt | head -5; echo \"== ISS\"; grep -n \"yaxn\\|'ice'\" ISS_alt_DKS.txt | head -5"
}
```


### [2026-09-05T20:32:15.055Z] TOOL RESULT

```
== BRT viiaxana
5680:•  j.  arsya-  m.  EN.  eines  Gläubigen: vatihsui  '^ehe  asaonS . .  'syehe  vyilxanake yJsi)rJsi)maAe  mazdayasnanqm  "des  V., Sohns  des  A. . .,  des  beredten  Ä. . ."  Yt. ij.  loS.
24681:•  j.  vyaxana-  Adj.  (fem.  '«J-)  'in  der Versammlung  sprechend,  ihr  Rat  erteilend, beredt  (ayoySTrijf  und  ßo^k^^ipa?)' ;  a)  von Menschen:  us  nä  saya/i(&d.)  'nS  vysxmsku (sd.)  gasaya/.uxo0  Yt.  13.16;  —  narqm  .. stähyanqm  'nanqm  Ny.j.  10;  YL  l^.  53; —  danavS  türa  'na  Ytj.  73;  —  hulä»- hsm  *''/^m'^  .  .yaha  "urväx/aAe  Az.^;  — ariyeke  'nahe  Yt/J.  108;  —  ß-azainllm karls.räzqm  'nqm  Y.öz.y,  F.j;  —  Jra- santsis  ..  'nayä  Yt.  yj.  134.  b)  von Göttern:  3%rS  urvasUtahe  ..  'nahe  Yt, /J. 85;  —  mi^r)m  .  ,  tpasitn  taxmim  'mm karsB.raiatshim  'mm  Yl/o.öi;  7,  25;  — miknm  . .  ys  'nanqm  °nS  Ytio.  65;  — nairyö.sar»hB  °n5  Y .22.1  y, —  nairya  satiha 'na  V.  22.  7.
30093:•  j.  hizuxda-  Adj.  'beredt''':  yvänS  . . yS  .  ,  danrS  .  .  'os  Yt.  15. 40.
== SKT ice
9065:idele.    ^E.)      M.  \L.  > from   M.  E.  ys,  ice.  i'i»/.  a  ; A.  S.  Isgicei,  an  icicle;    al-r ^V//,  where  //er   is  the  gen.  case.     1 is  a  dimin  form,  meaning  *a  «m»t!  |»(e ice;'  cf.  In  '•■■•■  •  4-
== ISS
2262:gyagarrá 'liver', Z 20°35 kye üri birstd suyä gyagarrd rrüva nätca ' whose belly burst, lungs, liver, intestines outside’; Z 2055 spuljei rrüva syī jatärrä bilga ysärä 'spleen, intestines, lungs, liver, kidneys, heart’; и 86:104 jarra vi; ibid. 104 jara vi; 1 187, 105v4 jarä BS yakrt; 1 147, 57У3 u jari āchanai hame 'and his liver becomes diseased’, from jarä with yi; 111 86:99 jarrä bimdä, ти 86-102 jarä bimdäşțä ‘upon the liver’; adjective, ш 86-100 сӣ buri va jaramña acha de ' whatever liver diseases there are'. From *yahrt, *yaknah 'liver', Av. yäākara, possibly Ли-уйупа- 'com- panion’, see W, Krause, Zeitschrift für vergleichenden Sprachforschung 56, 1929, 304, but to be explained as -уйупа- from *-уйхпа-, with variation of y and x, as in the name suya- beside ғихба- ‘Sogdian’ (where however -y- is older); Zor.P. yakar, N.Pers. jigar, Orm. jdir (dz); from yaxn-, Pasto ута, yina, yanna, yena, па; Yidya y&ysn, to IE Pok, so4 jk'-r(t) O.Ind. ya&ft, yaknds; Lit. jēknos, jáknos, Lat. iecur, iecoris, recinoris, Greek Trap,fyrevos, Armen. leard, lerdi. Here -arrá, -árrd, -arra, -ara from older -r#, but узага ‘heart’ from zrd-.
7126:vyachi si buddhaksitrd-vyüha ndsphae ' he who so realizes all dltarma-elements to be without self, without a being, without an individual, he produces the display (BS vyüha-) of the DBuddha-ksetrus', BS yah subhüte bodhisattvo nirütmüno dharma itv adhimucyate, Ryetra-vyBühàn nispáda- уйуйті; u1 28, оби bavsüra-vüysaina harbisä dharma vyachüid 'by the bodhisattva all dharma-elements must be realized’, BS sarva-dharma jiatavyá drastaoya adhi- moktavyāh; її 5:69 eyachara batysista ' may you (plural) realize bodhi-knowledge'; П 5°72 vyachīva j: jsām beysüsta ‘may you realize bodhi-knowledge'; ; K 50, 3374 тупас yudà ida; Ж. 61, 39r4 vyache yüda idi; Manj. зоо dharma- dhattu uyacha ‘ће realizes the dharma-dhàtu (cosmos of the dharma-elements)'; 3 plur. Мап). 142-3 Ha Ha vyach(i)da harbasa dharma tt(ujà 'so they realize all dharma-elements to be empty; K 1127375 butte à vyachai 'understands or realizes’; K 151:35 aysd vyachtmem (-em =-e) rastyüm (-bn =-е), vasoq daya ртага ‘тау I realize the right pure nature of the dharma-doctrine'; K 5о:5:1 vyachime dasau bhūmä ‘may I realize the ten stages! (DS bhümi-), Manj, 351 vyachai tva daya ksütta ‘тау he realize this dlarma-ksünti- (readiness)! ; Manj. 320 sa тазша vyachida prrara ‘тау they realize the pure nature’ (—BS svabháva-); 2 sing. К. 136:862-3 thu... ттаз{а sarva-dharma vyachyai ' may you realize. . . rightly in all-elements! (loc. plur. -và); participle, K. 138:932 vyachata-sareadharmàrm gyastānä baysüná' of those having realized all dharma-elements, the deva Buddhas’; K.150:27 vyachaua-dàva pyasta bemysq hamidi ‘the deva Buddhas having realized thedharma-doctrine together’; K. 137:906- 7 vyacha-sarva dharma; JS 39v4 baiysūstä uyichime ‘тау I realize bodhi-knowledge'; v 324:162 (with-c-) samaham vyac(a)ka üfari 'the teacher (BS й��йгуа-) realizing samüdhüna-trance'; п 106-145 пагойпоа fara vyachāmdä ‘they realized the joy (= BS sri) of nirvàna'; Bed 56r3 aysi uyachimi kusala carya uvāra 'may I realize it, the good exalted course’, BS naámayami vara-bhadra-cariye. The second meaning ' cease', triadic П 103: 5.4 vyachāmai paravaritümai (BS parivartaya-) пата 'cessation, change, quiescence’, rr 45:11 vyachiyas paravarttayai; К. т4зтобо pila akala-marapai vyachüme parivarttàme vira tsimde ‘may the calamities (BS рта) (and) untimely deaths (BS akala-) go to cessation, change for him’; JS 2vi vyachimde Ёўїга üchü pile 'may diseases, calamities (BS pidà) cease іп the land’; v 252:843 jsīnai hustye pilai vyachznde ‘may life advance-for- him, may calarnities cease for him’ ; K 93790 зла hist pilai uyechide; K 5277:10 vyachide harbaisá pile, upadravi (BS wpadrava-) acha hastye 'may all calamities cease, troubles, diseases, sorrows’. From base vyax- (that is, vyakA-) palatalized to vyach- 'to come to, reach’, glossed by BS adhi-mok-, *come to realization! and ‘to come to an end’, to Av. vyax- in vyüxa-, vyaxna-, туйхапа-, vyüxman- (variant туйхтап-) 'place of coming to, encounter, (hostile) meeting" ‚ in a context with araza-, glossed Zor.P. artik ‘attack’ and kàür&ar ‘battlefield’; the Zor.P. gloss is hanjaman ' coming together’; Av. adjective, vyāxainya-, Zor.P. hanfamanmik; from ham-gam- came also Zor.P. hangüm ‘end’. A connexion with the specialized sense fto be contained! of vyak-:eik- Zor.P. vinč, N.Pers.
```


## [2026-09-05T20:32:32.039Z] TOOL CALL #67: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && pdftoppm -f 150 -l 150 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf data/verification/sources/refs/ocr/BOOK/150 && ls -l data/verification/sources/refs/ocr/BOOK/150.png",
 "description": "Render page 150 PNG for audit"
}
```


### [2026-09-05T20:32:34.705Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 31185 Sep  5 16:32 data/verification/sources/refs/ocr/BOOK/150.png
```


## [2026-09-05T20:36:22.568Z] TOOL CALL #68: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-150.json <<'JSONEOF'\n{\n \"pdf_page\": 150,\n \"book_page\": 120,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Eis 2\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₁eyH- / *h₁ey-s- 'ice, frost' (Pokorny IEW 301 '2. ei-s-, ei-n- \\\"Eis, Frost\\\"'; Watkins/AHD 'eis-²')\",\n   \"note\": \"Nourai's root box reproduces Pokorny exactly: IEW p.301 heads the lemma '2. eis-, ei-n- ,Eis, Frost'' and lists 'Av. isu- ,eisig', aexa- n. ,Kälte', pämir. iš ,Kälte', osset. yex, ix ,Eis', afghan. asai ,Frost'; anord. iss … ags. is n., as. ahd. mhd. is n. ,Eis'; bsl. *inia- ,Reif''. The label 'Indo-European', the numbering 'Eis 2' (Pokorny's second eis-) and the gloss 'ice' are therefore all correct; Nourai's 'Eis' is simply Pokorny's German headword taken over as a root name. Modern reconstruction writes the root with the laryngeal, *h₁eyH- (Wiktionary, Proto-Iranian *Háyxam < PIE *h₁eyg-/*h₁eyH-), and the older handbooks are cautious about whether the Iranian and Germanic words really belong together: Walde-Pokorny I 108 says only 'Möglicherweise verwandt mit av. aēxa- \\\"Frost, Eis\\\", isu \\\"kalt\\\"', Buck 1.77 writes 'prob. : Av. aēxa- … NPers. yax … root connection?', and Etymonline still calls the Germanic word 'of uncertain origin'. That caution concerns the depth of the reconstruction, not the Iranian-Germanic equation itself, which every source on the page repeats. One purely graphic point: the printed page also carries an EMPTY box to the right of the Old Persian box, joined to it by an arrow; it is blank in the book (no language, no word), and the JSON extraction simply omits it.\",\n   \"note_fa\": \"جعبهٔ ریشهٔ این نمودار همان مدخل دوم پوکورنی در صفحهٔ ۳۰۱ فرهنگ ریشه‌شناسی هندواروپایی است: «‎2. eis-, ei-n- ,Eis, Frost'‎» با نمونه‌های اوستایی isu- «یخین»، aēxa- «سرما»، آسی yex/ix، پشتوی asai و ژرمنی īs. پس برچسب «هندواروپایی»، شمارهٔ «Eis 2» و معنای «یخ» هر سه درست‌اند و ادعای نورایی در حدّ جعبهٔ ریشه پذیرفتنی است. بازسازی امروزی این ریشه را با حنجره‌ای می‌نویسند: *h₁eyH-‎ (ویکی‌واژه: ایرانی آغازین *Háyxam از *h₁eyg-/*h₁eyH-). تنها نکته آنکه والده ـ پوکورنی (جلد ۱ ص ۱۰۸) و باک (بند ۱٫۷۷) پیوند واژه‌های ایرانی و ژرمنی را با تردید («شاید هم‌ریشه») می‌آورند، و این تردید دربارهٔ ژرفای بازسازی است نه دربارهٔ خودِ برابری ایرانی ـ ژرمنی. در صفحهٔ چاپی یک جعبهٔ خالی هم در کنار جعبهٔ «پارسی باستان» کشیده شده که در خودِ کتاب تهی است و در داده‌های استخراج‌شده نیامده است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C3%A1yxam\",\n    \"https://www.etymonline.com/word/ice\"\n   ],\n   \"ref_check\": [\n    {\n     \"ref\": \"POK:301\",\n     \"status\": \"supports\",\n     \"note\": \"POK_01.txt: the page marker '301' stands at line 4378 and the lemma follows at line 4383: 'z. eis-, ei-n- ,Eis, Frost'. Av. isu- ,eisig*, aexa- n. ,Kälte*, pämir. iš ,Kälte', osset. yex, ix ,Eis', afghan. asai ,Frost' … anord. iss, Pl. issar m. ,Eis', ags. is n., as. ahd. mhd. is n. ,Eis' … WP. I 108, Trautmann 104.' (grep -n 'aexa' POK_01.txt). The English Pokorny database (POK_full.txt line 24782) has the same lemma as 'Root/lemma: ei-s-2, ei-n- (*heis-), Meaning: ice … Page(s): 301'. Root, language and gloss are exactly as drawn.\"\n    }\n   ],\n   \"consulted\": [\n    {\n     \"src\": \"WLD\",\n     \"where\": \"Bd. I p. 108 (incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt line 7008 ff.)\",\n     \"stance\": \"partial\",\n     \"note\": \"'2. eis- „Eis“. Altn. íss, pl. ísar m. „Eis“, ags. īs n., mnd. īs n., ahd. mhd. īs n. dss. Möglicherweise verwandt mit av. aēxa- „Frost, Eis“, isu „kalt“ (von einer Inchoativbildung *is-sk-). Vgl. … Bartholomae ZDMG. 50, 697 …' — the same root, but the Iranian-Germanic equation is given as merely 'possible', and no Persian form is cited.\"\n    },\n    {\n     \"src\": \"AHD\",\n     \"where\": \"Watkins 1985, e-list (AHD_watkins1985.txt line 432)\",\n     \"stance\": \"supports\",\n     \"note\": \"'eis-2. Ice, frost. Germanic *is- in Old English is, ice: ICE; ICICLE. [Pok. 2. ei-s- 301.]' — the root name Nourai uses, the gloss 'ice', and the Pokorny page all agree.\"\n    },\n    {\n     \"src\": \"IEC\",\n     \"where\": \"Mann, s.v. is- (1) (IEC.txt line 6243)\",\n     \"stance\": \"supports\",\n     \"note\": \"'is- (1) (ois-?) \\\"hard or crystalline substance, ice\\\". WP I, 108. Av. isis, m. \\\"ice\\\"; aexa (\\\"frost\\\", fr. *ois-?); Per. yax \\\"ice\\\"; Oss. Ix, Dig. jex \\\"ice, hail\\\"; MHG, OE īs, ON íss, id.' — Mann collects the same set, and unlike Pokorny he explicitly includes Persian yax.\"\n    },\n    {\n     \"src\": \"SYN\",\n     \"where\": \"Buck 1.77 ICE, §4 (SYN.txt line 2029 ff., printed pp. 69-70)\",\n     \"stance\": \"partial\",\n     \"note\": \"'ON íss, OE is, etc., general Gmc., prob. : Av. aēxa- \\\"frost, ice\\\", isu- \\\"frosty, icy\\\", NPers. yaχ \\\"ice\\\", Afghan asai \\\"frost\\\", root connection? Walde-P. 1.108 … Barth. 372.' — same family, but Buck queries the ultimate root connection.\"\n    }\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"isav; aěxa\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Both forms are real Young Avestan words and both are cited by Pokorny on the very page Nourai gives. (a) isav- is the strong stem of the u-stem adjective isu- 'frosty, icy': Bartholomae, Altiranisches Wörterbuch (BRT.txt line 7979) 'j. isav- Adj. \\\"frostig, eisig\\\"; pasča isaoš zəmō aiwi.gaitīm \\\"nach Eintritt des eisigen Winters\\\" V. 9.6', with the etymological note 'Zu einem Praes. (Inkoh.) *isaiti \\\"es friert, es gibt Eis\\\"; vgl. afγ. asai \\\"Frost\\\", ahd. is \\\"Eis\\\"'. Nourai's 'isav' is thus the dictionary stem, not a misprint, and his gloss 'frosty' is Bartholomae's 'frostig' verbatim. (b) aěxa is Nourai's transcription of aēxa- (he writes the long ē of the diphthong with a breve, as he does throughout for Avestan aē-): Bartholomae (BRT.txt line 2517 area) 'j. aēxa- n. \\\"Frost, Eis\\\": kə̄m.stərətəm … aēxa- \\\"den erstarrenden Frost\\\" Yt. 10.2; a) Plur. \\\"Eisfelder\\\" … H. 2.25', with the note 'np. یخ \\\"Eis\\\" … Bthl. ZDMG. 50.697.' Pokorny 301 glosses it 'Kälte', Bartholomae 'Frost, Eis'; Nourai's 'ice' follows Bartholomae and is defensible. Phonologically Av. aēxa- < Proto-Iranian *(H)aixa- < *h₁ey-k-o- (Wiktionary *Háyxam), the -x- being the regular Iranian outcome of *k before the following consonant/in this formation; isu- is the zero grade *is-u- of the same root with the inchoative present *is-sk-. Both derive from the root box as drawn.\",\n     \"derivation_fa\": \"هر دو صورت واقعاً اوستایی‌اند و هر دو در همان صفحهٔ ۳۰۱ پوکورنی آمده‌اند. نخست isav- ستاکِ قویِ صفتِ u-ستاکِ isu- «یخین، سرمازده» است؛ بارتولومه در فرهنگ ایرانی باستان می‌نویسد: «j. isav- Adj. ,frostig, eisig‘» با شاهدِ وندیداد ۹٫۶ «pasča isaoš zəmō aiwi.gaitīm» یعنی «پس از فرارسیدنِ زمستانِ یخین»؛ پس «isav» خطای چاپی نیست بلکه همان ستاکِ فرهنگ‌نامه‌ای است و معنای «frosty» ترجمهٔ دقیقِ «frostig» بارتولومه است. دوم، «aěxa» همان aēxa-‎ است (نورایی ای‌کشیدهٔ دوواکهٔ اوستایی را با علامتِ کوتاه می‌نویسد)؛ بارتولومه آن را «aēxa- n. ,Frost, Eis‘» می‌آورد (یشت ۱۰٫۲) و در جمعْ «یخ‌زارها». پوکورنی معنای «سرما» و بارتولومه «یخ، یخ‌بندان» می‌دهد و برگردانِ نورایی («یخ») با بارتولومه می‌خواند. از نظر آوایی aēxa-‎ از ایرانی باستانِ ‎*(H)aixa-‎ و isu-‎ از پایهٔ صفرِ همان ریشه با ستاکِ حالِ آغازیِ ‎*is-sk-‎ است. بنابراین ادعای نورایی در این گره درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C3%A1yxam\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"HRN:252\",\n       \"status\": \"supports\",\n       \"note\": \"Horn, Grundriss der neupersischen Etymologie, no. 1126, printed p. 252 (HRN.txt leaf 274 = printed + 21): 'yax \\\"Eis\\\", yexe \\\"Hagel\\\". aw. aēxa- \\\"Eis\\\" (de Lagarde, Beitr. z. altb. Lex. 47), oder \\\"Frost\\\" (Bartholomae, Studien II, 55); pāz. yah. kurd. afγ. LW. yex; oss. d. yex, i. ix \\\"Eis, Hagel\\\"; waχ. yiχ.' Horn thus gives the Avestan etymon of the Persian word, i.e. exactly the arrow #1 → #2.\"\n      },\n      {\n       \"ref\": \"POK:301\",\n       \"status\": \"supports\",\n       \"note\": \"POK_01.txt line 4384 (page 301): 'Av. isu- ,eisig*, aexa- n. ,Kälte*' — both of the node's words stand in Pokorny's entry, though he glosses aēxa- 'Kälte' rather than 'ice'.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"BRT\",\n       \"where\": \"Altiranisches Wörterbuch s.v. aēxa- (BRT.txt line 2517) and s.v. isav- (line 7979; the page ends '373', so the column Buck cites as 'Barth. 372')\",\n       \"stance\": \"supports\",\n       \"note\": \"'j. aēxa- n. \\\"Frost, Eis\\\" … a) Plur. \\\"Eisfelder\\\"' with 'np. یخ \\\"Eis\\\" … Bthl. ZDMG. 50.697'; and 'j. isav- Adj. \\\"frostig, eisig\\\" … V. 9.6' with 'Zu einem Praes. (Inkoh.) *isaiti \\\"es friert, es gibt Eis\\\"'.\"\n      },\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein s.v. ice (KLN_1966.txt line 18583)\",\n       \"stance\": \"supports\",\n       \"note\": \"'ice, n. — ME. is, fr. OE. is … Outside Teut. cp. Avestic isav-, \\\"frosty\\\", aexa-, \\\"ice\\\", Afghanic asai, \\\"frost\\\".' Klein uses the same stem form 'isav-' Nourai prints, and glosses aexa- 'ice' as Nourai does.\"\n      },\n      {\n       \"src\": \"SYN\",\n       \"where\": \"Buck 1.77 ICE §4 (SYN.txt line 2029 ff.)\",\n       \"stance\": \"supports\",\n       \"note\": \"'prob. : Av. aēxa- \\\"frost, ice\\\", isu- \\\"frosty, icy\\\", NPers. yaχ \\\"ice\\\" … Barth. 372.'\"\n      }\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"yax «یخ»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP یخ yax 'ice' continues Old Iranian *(H)aixa- (= Av. aēxa-) through Middle Persian yax (also read ēx). The one point that needs explaining is the initial ya-, and it is a known regular development, not an obstacle: Hübschmann, Persische Studien p. 143, lists it under 'Dagegen wird ap. ai im Anlaut zu paz. np. ya-' with the two examples 'yax \\\"Eis\\\", osset. yex, ix; zd. aēxa-' and 'yak \\\"ein\\\"', and repeats on p. 152 'In yak \\\"ein\\\" und yax \\\"Eis\\\" geht ya- auf ai- zurück' — i.e. Old Persian/Old Iranian initial ai- gives Pāzand/New Persian ya-. Horn no. 1126 and Mo'in's footnote in Borhan-e Qateʿ give the same chain and add the dialect cognates (Pāzand yah, Kurdish and Afghan yex, Ossetic yex/īx 'ice, hail', Wakhi yix, Gilaki yax); Wiktionary reconstructs Proto-Iranian *Háyxam with the descendants MP yax, NP yax, Gilaki yəx, Mazanderani yax, Ossetic ix, Sogdian yaxn. Strictly the Persian word is not descended FROM Avestan but is the sister continuation of the same Old Iranian etymon; Nourai (like Horn and Mo'in) uses the Avestan box as the Old Iranian stage, which is his standard convention. First attested in NP in Ferdowsi (Šāh-nāme, quoted by Mo'in: 'čenān šod ke goftī tarāz yax ast'). Semantics unchanged: 'ice' throughout.\",\n     \"derivation_fa\": \"واژهٔ «یخ» دنبالهٔ ایرانی باستانِ ‎*(H)aixa-‎ (همان aēxa-‎ اوستایی) است که از راه فارسی میانهٔ yax (خوانشِ دیگر ēx) به فارسی نو رسیده است. تنها نکتهٔ آوایی، «یـ» آغازین است و آن هم دگرگونیِ قاعده‌مندی است: هوبشمان در «مطالعات فارسی» ص ۱۴۳ زیر عنوانِ «ai آغازینِ پارسی باستان در پازند و فارسی نو به ya- بدل می‌شود» دو نمونه می‌آورد: «yax ,Eis‘، آسی yex، ix؛ اوستایی aēxa-» و «yak ,ein‘»، و در ص ۱۵۲ باز می‌گوید «در yak و yax، ya- از ai- آمده است». هرن (شمارهٔ ۱۱۲۶) و حاشیهٔ معین بر برهان قاطع (ص ۲۴۲۷) همین زنجیره را می‌دهند و هم‌ریشه‌های گویشی را می‌افزایند: پازند yah، کردی و افغانی yex، آسی yex/îx «یخ، تگرگ»، وخی yix، گیلکی yax. ویکی‌واژه نیز ایرانی آغازینِ ‎*Háyxam‎ را بازسازی می‌کند با بازماندگانِ فارسی میانه yax، فارسی yax، گیلکی yəx و سغدی yaxn. به‌دقت باید گفت «یخ» از اوستایی گرفته نشده، بلکه هم‌ریشه و هم‌ردیفِ آن از یک ستاکِ ایرانی باستان است؛ نورایی ــ مانند هرن و معین ــ جعبهٔ اوستایی را نمایندهٔ مرحلهٔ ایرانی باستان گرفته است. کهن‌ترین شاهدِ فارسیِ آن در شاهنامه است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%DB%8C%D8%AE\",\n      \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C3%A1yxam\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"BQT:2427\",\n       \"status\": \"supports\",\n       \"note\": \"Borhan-e Qateʿ ed. Moʿin, p. 2427 (vol. 4, pdf p. 510; rendered to data/verification/sources/refs/ocr/BQT/2427.png, read by vision and saved to 2427.vision.txt). Moʿin's etymological footnote no. 5: «یخ ـ بفتح اول، اوستا aēxa (یخ) (de Lagarde, Beitr. 2. altb. Lex. 4) یا یخ بندان (Bartholomae, Studien II, 55)، پازند yah، کردی و افغانی yex، استی yex، îx (یخ، تگرگ)، وخی yix، «اشتقاق ۱۱۲۶»، گیلکی yax» — i.e. exactly Nourai's arrow, and «اشتقاق ۱۱۲۶» is Moʿin's reference to Horn's Grundriss no. 1126 (= HRN:252). The printed page number is not visible on the scan; the page is fixed by the tool's offset (+1917) and by the alphabetical position (یخچه، یخ در بهشت، یخنی on the same page).\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"HUB\",\n       \"where\": \"Hübschmann, Persische Studien pp. 143 and 152 (HUB.txt lines 4967 and 5318; leaf = printed + 10)\",\n       \"stance\": \"supports\",\n       \"note\": \"p. 143: 'Dagegen wird ap. ai im Anlaut zu paz. np. ya- in: yax \\\"Eis\\\", osset. yex, ix; zd. aēxa-; yak \\\"ein\\\" …'; p. 152: 'In yak \\\"ein\\\" und yax \\\"Eis\\\" geht ya- auf ai- zurück.' This is the phonological justification for the arrow.\"\n      },\n      {\n       \"src\": \"HRN\",\n       \"where\": \"Horn no. 1126, p. 252 (HRN.txt leaf 274)\",\n       \"stance\": \"supports\",\n       \"note\": \"'yax \\\"Eis\\\", yexe \\\"Hagel\\\". aw. aēxa- \\\"Eis\\\" … oder \\\"Frost\\\" (Bartholomae, Studien II, 55); pāz. yah; kurd. afγ. LW. yex; oss. d. yex, i. ix \\\"Eis, Hagel\\\"; waχ. yiχ.'\"\n      },\n      {\n       \"src\": \"ARY\",\n       \"where\": \"Aryanpur, Farhang-e riše-hā-ye hend-o-orupāyi, pdf page 538 (incoming/ARY/ARY_latin_index_pages.txt line 15706 ff.)\",\n       \"stance\": \"supports\",\n       \"note\": \"The یخ entry groups AVESTAN 'AEX, AEXA, ISU', PAHLAVI 'YAH', OSSETIC 'YEX, IX', KURDISH 'YEX', BALUCHI 'YEX', AFGHAN 'ASAI', OLD ENGLISH 'IS', ENGLISH 'ICE', GERMAN 'EIS', with references 'POKORNY (301) … BUCK: 69-70 … SKEAT: (ICE) 285 … MALLORY & ADAMS: *H₁EIHX-' — an independent modern Persian handbook drawing exactly Nourai's chart.\"\n      },\n      {\n       \"src\": \"PHD\",\n       \"where\": \"MacKenzie, A Concise Pahlavi Dictionary (PHD.txt, PHD_mackenzie.txt; grep 'yax')\",\n       \"stance\": \"silent\",\n       \"note\": \"MacKenzie has no entry yax 'ice' (only yaxš 'word' in Nyberg, a different word); the Middle Persian form is known from Manichaean/Pāzand material rather than from the Book-Pahlavi corpus MacKenzie glosses, so his silence is not a disagreement.\"\n      },\n      {\n       \"src\": \"IEC\",\n       \"where\": \"Mann s.v. is- (1) (IEC.txt line 6243)\",\n       \"stance\": \"supports\",\n       \"note\": \"'Per. yax \\\"ice\\\"' listed beside 'Av. isis … aexa' and 'Oss. Ix, Dig. jex', all under one root.\"\n      }\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Old Persian\",\n     \"words\": \"viyaxna\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"OP viyax(a)na- is not an attested Old Persian noun meaning 'ice': it is the name of the twelfth Achaemenid month (Feb.-March, Akkadian Addāru), known only from the genitive Viyaxnahyā māhyā 'in the month V.' in Darius' Bisotun inscription (DB 1.37, 1.42, 1.96, 2.26 etc.) and from Elamite Mi-ya-kán-na-iš on the Persepolis tablets. Nourai's gloss 'ice' comes from his source: Gharib's Sogdian Dictionary entry 11097 cross-refers the Sogdian word for 'ice' to 'OP viyaxna'. But that is a guess about the month name, not a translation of an attested word, and it is not what the Old Persian specialists say. Kent, Old Persian §, on the -na- formations: 'Perhaps with vriddhi in prefix: Vi-yax-na- (radical element uncertain)' — he refuses to give a meaning. Schmitt (2003) reviewed all proposed etymologies of the month name and discarded them all, and Lubotsky (2012, 'The Old Persian month name viyax(a)na-, Avestan viiāx(a)na- \\\"eloquent, bragging\\\" and Ossetic festivals', in the Schindler memorial volume, pp. 95-106) argues that OP viyax(a)na- is formally identical with Avestan viiāxana- 'speaking in the assembly, eloquent' (Bartholomae: 'j. vyāxana- Adj. \\\"in der Versammlung sprechend, ihr Rat erteilend, beredt\\\"'), the Avestan ā being the regular lengthening after *Ci-, so that the month is the month of the (verbal-contest) assembly — an Ossetic-style late-winter festival. Formally the 'ice' etymology is also awkward: the Iranian word is *(H)aix-/*yax- with no prefix, whereas viyax(a)na- has the preverb vi- and a -na- suffix. Verdict: the form is genuine Old Persian and correctly transcribed, but the gloss 'ice' and the attachment to this root are rejected by current scholarship.\",\n     \"derivation_fa\": \"‏viyax(a)na-‎ واژه‌ای پارسی باستان به معنای «یخ» نیست؛ نامِ دوازدهمین ماهِ گاه‌شمارِ هخامنشی (اسفند، برابرِ Addāru اکدی) است که تنها در حالتِ اضافیِ «Viyaxnahyā māhyā» در سنگ‌نبشتهٔ بیستون (بندهای ۱٫۳۷، ۱٫۴۲، ۲٫۲۶ و …) و در صورتِ عیلامیِ Mi-ya-kán-na-iš در گل‌نبشته‌های تخت‌جمشید آمده است. معنای «یخ» را نورایی از مأخذِ خود گرفته: قریب در فرهنگ سغدی (مدخل ۱۱۰۹۷) واژهٔ سغدیِ «یخ» را با «OP viyaxna» می‌سنجد؛ ولی این تنها حدسی دربارهٔ نامِ ماه است نه ترجمهٔ واژه‌ای گواهی‌شده. کنت در «پارسی باستان» می‌نویسد: «شاید با وریدی در پیشوند: Vi-yax-na-‎ (عنصرِ ریشه‌ایِ آن نامعلوم است)». اشمیت (۲۰۰۳) همهٔ ریشه‌شناسی‌های پیشنهادی این نامِ ماه را رد کرده و لوبوتسکی (۲۰۱۲) نشان داده که این واژه از نظر صورت همان viiāxana-‎ اوستایی «سخنورِ انجمن، بلیغ» است (بارتولومه: «در انجمن سخن‌گوینده، رای‌دهنده، بلیغ»)، و کشیدگیِ ā در اوستایی پس از ‎*Ci-‎ قاعده‌مند است؛ پس این ماه، ماهِ انجمن و مسابقهٔ سخنوری بوده است. از نظر ساخت هم واژهٔ ایرانیِ «یخ» ‎*(H)aix-/*yax-‎ است و پیشوند و پسوند ندارد، حال آنکه viyaxna-‎ پیشوندِ vi- و پسوندِ ‎-na-‎ دارد. خلاصه: خوانشِ صورت درست است، اما معنای «یخ» و بستنِ آن به این ریشه را پژوهشِ امروزی رد می‌کند.\",\n     \"sources\": [\n      \"https://scholarlypublications.universiteitleiden.nl/access/item:2882943/view\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"SOD:452\",\n       \"status\": \"partial\",\n       \"note\": \"Gharib, Sogdian Dictionary, printed p. 452 (SOD_pages.txt scan page 520, which carries the printed number '452'), entry '11097 yxn(w) S — yaxn ©OP viyaxna ⇒ yγδyn, γnγyn'k, yxnyy — ice — Sund. MHC p26 n33 38.8 V3'. The page does make Nourai's connection, but it makes it as a bare comparandum ('©OP viyaxna') attached to the SOGDIAN headword; Gharib nowhere states that the Old Persian month name means 'ice'.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KNT\",\n       \"where\": \"Kent, Old Persian, formation of -na- stems (KNT.txt line 1962) and DB citations (line 622)\",\n       \"stance\": \"partial\",\n       \"note\": \"'Perhaps with vriddhi in prefix: Vi-yax-na- (radical element uncertain).' and 'Regularly in the -ahyā genitive of the month name, before māhyā: Viyaxnahyā māhyā DB 1.37; other examples 1.42, 96; 2.26 …'. Kent confirms the form and that it is a month name, but explicitly declines to identify the root — so he does not support the gloss 'ice'.\"\n      },\n      {\n       \"src\": \"BRT\",\n       \"where\": \"Bartholomae s.v. vyāxana- (BRT.txt line 24681)\",\n       \"stance\": \"contradicts\",\n       \"note\": \"'j. vyāxana- Adj. (fem. -ī-) \\\"in der Versammlung sprechend, ihr Rat erteilend, beredt\\\" … Yt. 13.16, Yt. 10.61, 10.65, Ny. 3.10 …' — the Avestan word that Lubotsky equates with the OP month name; it has nothing to do with ice.\"\n      },\n      {\n       \"src\": \"ISS\",\n       \"where\": \"Bailey, Indo-Scythian Studies / Khotanese dictionary (ISS_alt_DKS.txt line 7126, s.v. vyach-)\",\n       \"stance\": \"contradicts\",\n       \"note\": \"'to Av. vyax- in vyāxa-, vyaxna-, vyāxana-, vyāxman- (variant vyaxman-) \\\"place of coming to, encounter, (hostile) meeting\\\" … the Zor.P. gloss is hanjaman \\\"coming together\\\"' — Bailey too puts vyaxna- in the 'assembly/encounter' family, not with 'ice'.\"\n      },\n      {\n       \"src\": \"POK\",\n       \"where\": \"IEW p. 301 (POK_01.txt line 4384)\",\n       \"stance\": \"silent\",\n       \"note\": \"Pokorny's eis-2 entry lists Avestan, Pamir, Ossetic and Pashto forms but no Old Persian word at all.\"\n      }\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Sogdian\",\n     \"words\": \"yxn\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Sogdian yxn(w) (Sundermann's Manichaean text; read yaxn) 'ice' is the same Iranian etymon as Persian yax, extended by the common Sogdian noun suffix -n (< *-na-): Proto-Iranian *(H)aixa- / *yaxa- + -na- > yaxn. Gharib's dictionary gives it with the variants yγδyn and γnγyn'k 'icy, of ice' (entry 10993, from TSP 9.29) and yxnyy, and cross-refers it to OP viyaxna; Wiktionary's Proto-Iranian *Háyxam page lists 'Sogdian yxnw (yaxn, \\\"ice\\\")' beside Khwarezmian ʾyx/yyx and Yaghnobi ix/ex as the north-eastern Iranian continuations. Nourai's transliteration 'yxn' is the consonantal skeleton as written in the Sogdian script (Gharib prints yxn(w), the -w being the graphic ending); attaching it directly to the root box rather than under the Avestan box is right, since Sogdian is an East Iranian language and not a descendant of Avestan.\",\n     \"derivation_fa\": \"واژهٔ سغدیِ yxn(w) (خوانده yaxn) «یخ» همان ستاکِ ایرانیِ «یخ» است با پسوندِ اسم‌سازِ ‎-n‎ (از ‎*-na-‎): ایرانی آغازینِ ‎*(H)aixa-/*yaxa-‎ + ‎-na-‎ ← yaxn. قریب در فرهنگ سغدی (مدخل ۱۱۰۹۷، ص ۴۵۲) آن را با گونه‌های yγδyn و γnγyn'k «یخین» (مدخل ۱۰۹۹۳) و yxnyy می‌آورد و با «viyaxna»ی پارسی باستان می‌سنجد؛ ویکی‌واژه نیز در مدخلِ ایرانی آغازینِ ‎*Háyxam‎ «سغدی yxnw (yaxn) یخ» را در کنارِ خوارزمیِ ʾyx و یغنابیِ ix می‌نشاند. آوانگاریِ «yxn» در کتاب همان پیکرهٔ بی‌واکهٔ خطِ سغدی است. اینکه نورایی این گره را یکراست به جعبهٔ ریشه بسته و زیرِ اوستایی نبرده، درست است، زیرا سغدی زبانی ایرانیِ خاوری است و بازماندهٔ اوستایی نیست. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C3%A1yxam\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"SOD:452\",\n       \"status\": \"supports\",\n       \"note\": \"Gharib p. 452 (scan page 520 of SOD_pages.txt, printed number '452' at the head of the page): '11097 yxn(w) S — yaxn ©OP viyaxna ⇒ yγδyn, γnγyn'k, yxnyy — ice — Sund. MHC p26 n33 38.8 V3'; the same page has '11098 yxnyy M — yaxne ©OP viyaxna'. The English index (SOD.txt line 90585) confirms 'ice 10993, 11097'.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"SOD\",\n       \"where\": \"Gharib entry 10993 (SOD.txt line 82572)\",\n       \"stance\": \"supports\",\n       \"note\": \"'10993 γnγyn'k B — yanxene (γnγyn'k) ⇒ yxn(w), yγδyn — icy, (of) ice — TSP 9.29, Benv. II p220' — the derived adjective of the same stem, confirming the word is well attested in Sogdian.\"\n      },\n      {\n       \"src\": \"ISS\",\n       \"where\": \"Bailey, Khotanese (ISS_alt_DKS.txt; grep 'yaxn')\",\n       \"stance\": \"silent\",\n       \"note\": \"Bailey's Khotanese material has no 'ice' word from this stem (his 'yaxn-' citations belong to *yakar 'liver'); no Khotanese cognate is claimed by the chart either.\"\n      },\n      {\n       \"src\": \"POK\",\n       \"where\": \"IEW 301 (POK_01.txt line 4384)\",\n       \"stance\": \"silent\",\n       \"note\": \"Pokorny lists Pamir iš and Ossetic yex/ix but no Sogdian form; Sogdian material was not in his sources for this lemma.\"\n      }\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Germanic\",\n     \"words\": \"îs\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *īsa- n. 'ice' (Nourai's 'îs' is the OHG/OE spelling of the same form) continues the root's *ei-s- grade: Pokorny 301 'anord. íss, Pl. íssar m. \\\"Eis\\\", ags. is n., as. ahd. mhd. is n. \\\"Eis\\\"'; Walde-Pokorny I 108 the same. Watkins/AHD summarises it as 'eis-². Ice, frost. Germanic *is- in Old English is, ice: ICE; ICICLE. [Pok. 2. ei-s- 301.]', which is precisely the reference (AHD) printed in this box. The word survives in every Germanic language (ON íss, OFris. is, Du. ijs, Ger. Eis, Dan./Swed. is) and gave the rune-name īsaz; it is also the source of the Germanic word for the season-metaphor in icicle (OE īses gicel). The connection with the Iranian branch is the one Pokorny, Klein and Buck all state, with Walde-Pokorny's caveat 'möglicherweise'.\",\n     \"derivation_fa\": \"ژرمنیِ آغازینِ ‎*īsa-‎ «یخ» (صورتِ «îs» در کتاب همان املای آلمانیِ علیای باستان/انگلیسی باستان است) دنبالهٔ پایهٔ ‎*ei-s-‎ همین ریشه است؛ پوکورنی در ص ۳۰۱ می‌آورد: «anord. íss … ags. is n., as. ahd. mhd. is n. ,Eis‘» و والده ـ پوکورنی (ج ۱ ص ۱۰۸) همان را. واتکینز در پیوستِ ریشه‌های هندواروپاییِ فرهنگ American Heritage ــ یعنی همان مأخذی که در این جعبه آمده ــ می‌نویسد: «eis-²‎. یخ، سرما. ژرمنیِ ‎*is-‎ در انگلیسی باستانِ is: ICE; ICICLE». این واژه در همهٔ زبان‌های ژرمنی مانده است (ایسلندی íss، هلندی ijs، آلمانی Eis، دانمارکی/سوئدی is). پیوندِ آن با شاخهٔ ایرانی همان است که پوکورنی، کلاین و باک می‌گویند (با احتیاطِ «شاید» در والده ـ پوکورنی). ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/ice\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"AHD\",\n       \"status\": \"supports\",\n       \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 432): 'eis-2. Ice, frost. Germanic *is- in Old English is, ice: ICE; ICICLE. [Pok. 2. ei-s- 301.]' — the box's only reference, and it says exactly what the arrow says (root → Germanic *is- → English ice).\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"POK\",\n       \"where\": \"IEW 301 (POK_01.txt line 4386)\",\n       \"stance\": \"supports\",\n       \"note\": \"'anord. iss, Pl. issar m. ,Eis', ags. is n., as. ahd. mhd. is n. ,Eis''.\"\n      },\n      {\n       \"src\": \"WLD\",\n       \"where\": \"Bd. I 108 (incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt line 7010)\",\n       \"stance\": \"supports\",\n       \"note\": \"'Altn. íss, pl. ísar m. „Eis“, ags. īs n., mnd. īs n., ahd. mhd. īs n. dss.'\"\n      },\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein s.v. ice (KLN_1966.txt line 18583)\",\n       \"stance\": \"supports\",\n       \"note\": \"'rel. to ON. iss, OS., OFris., MLG., OHG., MHG. is, Dan., Swed. is, Du. ijs, G. Eis.'\"\n      }\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"English\",\n     \"words\": \"ice\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English ice < Middle English is, ijs, ise < Old English īs 'ice, piece of ice' < Proto-Germanic *īsa-, i.e. the node's parent. The modern spelling with -ce dates from the 15th century, when French-influenced orthography replaced final -s to keep the /s/ from being read as /z/ (Etymonline); the same word gives icicle (OE īses gicel 'icicle of ice', with gicel from the unrelated root *yeg-, Pokorny 503). No reference is printed in this box, but the chain is one of the least controversial in the book and is given identically by Klein and Etymonline.\",\n     \"derivation_fa\": \"واژهٔ انگلیسیِ ice از انگلیسیِ میانهٔ is/ise و آن از انگلیسیِ باستانِ īs «یخ، تکه‌یخ» است، یعنی درست از همان گرهِ پدر (ژرمنیِ ‎*īsa-‎). املای امروزیِ با ‎-ce‎ از سدهٔ پانزدهم است تا «س» پایانی به‌صورت «ز» خوانده نشود (اتیمانلاین). همین واژه در icicle «قندیلِ یخ» هم هست (انگلیسی باستان: īses gicel) که جزءِ دومش از ریشهٔ دیگری (‎*yeg-‎، پوکورنی ص ۵۰۳) است. این جعبه در کتاب مأخذی ندارد، ولی زنجیره از بی‌مناقشه‌ترین بخش‌های کتاب است و کلاین و اتیمانلاین همین را می‌گویند. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/ice\"\n     ],\n     \"ref_check\": [\n      {\n       \"ref\": \"(none printed)\",\n       \"status\": \"not_checked\",\n       \"note\": \"The English box carries no reference in the book (refs=None); the parent box's AHD reference covers the chain ('Germanic *is- in Old English is, ice: ICE; ICICLE'), and Klein and Etymonline were consulted instead — see 'consulted'.\"\n      }\n     ],\n     \"consulted\": [\n      {\n       \"src\": \"KLN\",\n       \"where\": \"Klein s.v. ice (KLN_1966.txt line 18583)\",\n       \"stance\": \"supports\",\n       \"note\": \"'ice, n. — ME. is, fr. OE. is, rel. to ON. iss … Cp. iceberg, icicle, Isold.'\"\n      },\n      {\n       \"src\": \"AHD\",\n       \"where\": \"Watkins 1985, s.v. eis-2 (AHD_watkins1985.txt line 432)\",\n       \"stance\": \"supports\",\n       \"note\": \"'Germanic *is- in Old English is, ice: ICE; ICICLE.'\"\n      },\n      {\n       \"src\": \"SKT\",\n       \"where\": \"Skeat s.v. icicle (SKT.txt line 9065; the ICE entry itself is badly OCR'd)\",\n       \"stance\": \"supports\",\n       \"note\": \"'… fr. M.E. ys, ice … A.S. ises gicel, an icicle … a dimin. form, meaning \\\"a small piece of ice\\\"' — the OE ancestor of NE ice as Klein gives it.\"\n      }\n     ]\n    }\n   ]\n  }\n ]\n}\nJSONEOF\ncd /home/sfmqrb && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-150.json > /dev/null && echo JSON_OK"
}
```


### [2026-09-05T20:36:25.112Z] TOOL RESULT

```
JSON_OK
```


## [2026-09-05T20:36:28.970Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 tools/verify_check.py 150"
}
```


### [2026-09-05T20:36:30.726Z] TOOL RESULT

```
nodes verified: 6/6
node verdicts: {'confirmed': 5, 'disputed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 5, 'partial': 1, 'not_checked': 1}
books consulted: {'supports': 14, 'silent': 4, 'partial': 1, 'contradicts': 2} | by book: {'KLN': 3, 'POK': 3, 'BRT': 2, 'ISS': 2, 'SYN': 1, 'HUB': 1, 'HRN': 1, 'ARY': 1, 'PHD': 1, 'IEC': 1, 'KNT': 1, 'SOD': 1, 'WLD': 1, 'AHD': 1, 'SKT': 1}
```


## [2026-09-05T20:36:45.492Z] AGENT

Page 150 (book p. 120) verified — `data/verification/page-150.json`; `verify_check.py 150` shows 0 PROBLEM lines.

**Counts** — 1 entry (root "Eis 2"), 6 nodes: root `confirmed`; nodes 5 `confirmed`, 1 `disputed`. Ref checks: 5 supports, 1 partial, 1 not_checked (English box cites nothing). 15 books consulted.

**Disputed**
- **#3 Old Persian `viyaxna` "ice"** — not an attested OP noun for ice but the 12th Achaemenid month name (DB *Viyaxnahyā māhyā*). Kent: "Vi-yax-na- (radical element uncertain)"; Schmitt 2003 discards all etymologies; Lubotsky 2012 equates it with Av. *viiāxana-* "eloquent, speaking in the assembly" (Bartholomae col. s.v. *vyāxana-*; Bailey likewise puts *vyaxna-* in the "assembly/encounter" family). The 'ice' gloss comes only from Gharib's bare cross-reference "©OP viyaxna" under Sogdian *yaxn* — so SOD:452 is `partial`, not support.

**Notable confirmations** — Pokorny 301 ("2. eis-, ei-n- 'Eis, Frost'") matches the root box word for word; Bartholomae has both *isav-* "frostig, eisig" (V. 9.6) and *aēxa-* n. "Frost, Eis" with an explicit "np. یخ" note; Hübschmann pp. 143/152 supplies the phonology for the Persian node ("In *yak* und *yax* geht ya- auf ai- zurück"); Moʿin's footnote at BQT:2427 reproduces Horn no. 1126 verbatim; Gharib p. 452 entry 11097 has the Sogdian word; Watkins/AHD "eis-2" covers Germanic→English.

**No extraction errors**, one cosmetic difference: the printed chart has a **blank box** to the right of the Old Persian box (arrow drawn into it) that the JSON omits — it is empty in the book itself, so no data fix is needed unless you want the empty node recorded.

Artifacts saved: `sources/refs/ocr/BQT/2427.png` + `2427.vision.txt` (Moʿin's footnote transcribed), `sources/refs/ocr/BOOK/150.png`, and 4 archived web pages (Wiktionary یخ, Proto-Iranian *Háyxam, Etymonline *ice*, Lubotsky 2012 PDF).
