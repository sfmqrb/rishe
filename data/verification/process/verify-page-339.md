# Verification process log — verify-page-339


## [2026-09-07T17:36:02.444Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 339 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-339.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-339.json. Write /home/sfmqrb/git/rishe/data/verification/page-339.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 339` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T17:36:04.225Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T17:36:04.883Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T17:36:04.915Z] TOOL RESULT

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


## [2026-09-07T17:36:05.589Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-339.txt"
}
```


### [2026-09-07T17:36:05.611Z] TOOL RESULT

```
1	=== PDF page 339 (book page 309) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Meuk : scratch, rub  (refs POK:745)
4	#1 (parent #0) [Avestan] refs=POK:745 | mušti : fist
5	  #2 (parent #1) [Persian] refs=BQT:2010; HRN:220 | mošt «مشت ۱» : fist
6	#3 (parent #0) [Latin] refs=POK:745 | mucrô : sharp point
7	  #4 (parent #3) [English] refs=AHD:860 | mucro : sharp point of plants
8	--- entry 1 ---
9	ROOT [Indo-European] Meuk : stocking, boot  (refs IEC:1643)
10	#1 (parent #0) [Avestan] refs=HRN:223 | maoč : shoe, boot
11	  #2 (parent #1) [Pahlavi] refs=BQT:2051 | môzag, mŭčak : shoe, boot
12	    #3 (parent #2) [Persian] refs=MON:4432 | mŭzeh «موزه ۲» : boot, shoe
13	  #4 (parent #1) [Avestan] refs=SNS:247; HRN:223 | paitiš-muxtâ : to put on (shoes) ☞Per 3 ; fra-muxti : to take out (shoes) ☞Per 1
14	#5 (parent #0) [Sanskrit] refs=HRN:223 | môč : shoe
15	#6 (parent #0) [Old English] refs=IEC:1643 | měo, měon : shoe sole
16	--- entry 2 ---
17	ROOT [Indo-European] Mew, Meu 2 : to push away, move  (refs POK:743)
18	#1 (parent #0) [Avestan] refs=POK:743; ISS:331 | mivâmahi : (we) eliminate ; a-muyamnô : not movable ☞Ne 1
19	  #2 (parent #1) [Pahlavi] refs=ISS:331 | mŭtak : move ; parmŭtan : to move
20	#3 (parent #0) [Latin] refs=AHD | movêre : to move
21	  #4 (parent #3) [English] refs=AHD | mobile, momentum, motion, motive, motor, move, commotion, emotion, promote, remote, remove
22	
```


## [2026-09-07T17:36:05.781Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-339.json"
}
```


### [2026-09-07T17:36:05.792Z] TOOL RESULT

```
1	{
2	  "pdf_page": 339,
3	  "book_page": 309,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Meuk",
8	        "lang": "Indo-European",
9	        "refs": "POK:745",
10	        "gloss": "scratch, rub"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK:745",
18	          "words": [
19	            {"translit": "mušti", "gloss": "fist", "script": null}
20	          ],
21	          "note": null,
22	          "quote": null
23	        },
24	        {
25	          "id": 2,
26	          "parent": 1,
27	          "lang": "Persian",
28	          "refs": "BQT:2010; HRN:220",
29	          "words": [
30	            {"translit": "mošt", "gloss": "fist", "script": "مشت ۱"}
31	          ],
32	          "note": null,
33	          "quote": null
34	        },
35	        {
36	          "id": 3,
37	          "parent": 0,
38	          "lang": "Latin",
39	          "refs": "POK:745",
40	          "words": [
41	            {"translit": "mucrô", "gloss": "sharp point", "script": null}
42	          ],
43	          "note": null,
44	          "quote": null
45	        },
46	        {
47	          "id": 4,
48	          "parent": 3,
49	          "lang": "English",
50	          "refs": "AHD:860",
51	          "words": [
52	            {"translit": "mucro", "gloss": "sharp point of plants", "script": null}
53	          ],
54	          "note": null,
55	          "quote": null
56	        }
57	      ]
58	    },
59	    {
60	      "root": {
61	        "name": "Meuk",
62	        "lang": "Indo-European",
63	        "refs": "IEC:1643",
64	        "gloss": "stocking, boot"
65	      },
66	      "nodes": [
67	        {
68	          "id": 1,
69	          "parent": 0,
70	          "lang": "Avestan",
71	          "refs": "HRN:223",
72	          "words": [
73	            {"translit": "maoč", "gloss": "shoe, boot", "script": null}
74	          ],
75	          "note": null,
76	          "quote": null
77	        },
78	        {
79	          "id": 2,
80	          "parent": 1,
81	          "lang": "Pahlavi",
82	          "refs": "BQT:2051",
83	          "words": [
84	            {"translit": "môzag, mŭčak", "gloss": "shoe, boot", "script": null}
85	          ],
86	          "note": null,
87	          "quote": null
88	        },
89	        {
90	          "id": 3,
91	          "parent": 2,
92	          "lang": "Persian",
93	          "refs": "MON:4432",
94	          "words": [
95	            {"translit": "mŭzeh", "gloss": "boot, shoe", "script": "موزه ۲"}
96	          ],
97	          "note": null,
98	          "quote": {
99	            "text": "همیشه به یک ساق موزه درون - یکی خنجری داشتی آبگون",
100	            "poet": "Ferdowsî"
101	          }
102	        },
103	        {
104	          "id": 4,
105	          "parent": 1,
106	          "lang": "Avestan",
107	          "refs": "SNS:247; HRN:223",
108	          "words": [
109	            {"translit": "paitiš-muxtâ", "gloss": "to put on (shoes)", "script": null, "see": ["Per 3"]},
110	            {"translit": "fra-muxti", "gloss": "to take out (shoes)", "script": null, "see": ["Per 1"]}
111	          ],
112	          "note": null,
113	          "quote": null
114	        },
115	        {
116	          "id": 5,
117	          "parent": 0,
118	          "lang": "Sanskrit",
119	          "refs": "HRN:223",
120	          "words": [
121	            {"translit": "môč", "gloss": "shoe", "script": null}
122	          ],
123	          "note": null,
124	          "quote": null
125	        },
126	        {
127	          "id": 6,
128	          "parent": 0,
129	          "lang": "Old English",
130	          "refs": "IEC:1643",
131	          "words": [
132	            {"translit": "měo, měon", "gloss": "shoe sole", "script": null}
133	          ],
134	          "note": null,
135	          "quote": null
136	        }
137	      ]
138	    },
139	    {
140	      "root": {
141	        "name": "Mew, Meu 2",
142	        "lang": "Indo-European",
143	        "refs": "POK:743",
144	        "gloss": "to push away, move"
145	      },
146	      "nodes": [
147	        {
148	          "id": 1,
149	          "parent": 0,
150	          "lang": "Avestan",
151	          "refs": "POK:743; ISS:331",
152	          "words": [
153	            {"translit": "mivâmahi", "gloss": "(we) eliminate", "script": null},
154	            {"translit": "a-muyamnô", "gloss": "not movable", "script": null, "see": ["Ne 1"]}
155	          ],
156	          "note": null,
157	          "quote": null
158	        },
159	        {
160	          "id": 2,
161	          "parent": 1,
162	          "lang": "Pahlavi",
163	          "refs": "ISS:331",
164	          "words": [
165	            {"translit": "mŭtak", "gloss": "move", "script": null},
166	            {"translit": "parmŭtan", "gloss": "to move", "script": null}
167	          ],
168	          "note": null,
169	          "quote": null
170	        },
171	        {
172	          "id": 3,
173	          "parent": 0,
174	          "lang": "Latin",
175	          "refs": "AHD",
176	          "words": [
177	            {"translit": "movêre", "gloss": "to move", "script": null}
178	          ],
179	          "note": null,
180	          "quote": null
181	        },
182	        {
183	          "id": 4,
184	          "parent": 3,
185	          "lang": "English",
186	          "refs": "AHD",
187	          "words": [
188	            {"translit": "mobile, momentum, motion, motive, motor, move, commotion, emotion, promote, remote, remove", "gloss": null, "script": null}
189	          ],
190	          "note": null,
191	          "quote": null
192	        }
193	      ]
194	    }
195	  ]
196	}
197	
```


## [2026-09-07T17:36:10.314Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"---MATRIX---\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and read source matrix"
}
```


### [2026-09-07T17:36:10.368Z] TOOL RESULT

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


## [2026-09-07T17:36:12.761Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','HRN','BQT','MON','AHD','ISS','SNS','KLN','WLD','BRT','PHD','NYB','SYN','ARY','HUB','CHEUNG','SKT']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-07T17:36:13.999Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

CHEUNG null

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
```


## [2026-09-07T17:36:29.541Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['mucro','mucrō','muk-','meuk','meu-','movere','movēre','mušti','musti']:\n    idxs=[m.start() for m in re.finditer(re.escape(pat),t)]\n    print(pat, len(idxs))\nEOF",
 "description": "Grep Pokorny full text for keywords"
}
```


### [2026-09-07T17:36:30.995Z] TOOL RESULT

```
mucro 1
mucrō 0
muk- 2
meuk 4
meu- 14
movere 2
movēre 0
mušti 0
musti 3
```


## [2026-09-07T17:36:31.092Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80 && echo \"---\" && ls ocr 2>/dev/null | head",
 "description": "List refs dir"
}
```


### [2026-09-07T17:36:31.154Z] TOOL RESULT

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
HRN
IRN
PLA
SNS
SOD
TAD
```


## [2026-09-07T17:36:35.187Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['mucro','meuk','musti']:\n    for m in re.finditer(re.escape(pat),t):\n        print('=== ',pat, m.start())\n        print(t[max(0,m.start()-1500):m.start()+900])\n        print()\nEOF",
 "description": "Print Pokorny context for mucro, meuk, musti"
}
```


### [2026-09-07T17:36:36.437Z] TOOL RESULT

```
===  mucro 2524690
rro\N, tight, slim, slender, thin ', Old Icelandic 
smugat " loop hole; hiding place ', further Swedish i mjugg, Norwegian i mugg^ furtive '. 

with 5- Danish Norwegian i smug, Dutch ter smuig {ter smuik) ds., Danish Norwegian 
smughander illicit trade ', ndd. smuggein. Modern High German (out of it) schmuggein 
(with A/Dutch smokkelen 6s.)\ probably also Modern High German mogein. Low German 
mogelen, muggelen^ heimliches, betrijgerisches Spiel treiben '; with Germanic k{k): 
Norwegian dial, smokia, smuk/alurk, creep forward ', Swiss schmauchen^ steal secretly, 
nibble '; in the meaning ' nestle, cuddle, snuggle' Middle High German smuck^ nestlling 
up, jewellery', smucken. Middle Low German smucken^ nestle, snuggle, apparel, adorn'. 
Old High German smocco; Old English s/77c»c/r "shirt'. Old Icelandic smokkrm. " 
Frauenbrustlatz ', Middle Low German smuk{-ck-) ' sleek, smart, neat ', Middle High 
German gesmuckef slim '; 

-g-o\ -gh-\w Latvian smaugs^ slim ', Lithuanian smaugiT throttle, strangle ', Latvian 
smudzi, smudzT mosquito, small fly ', poln. smug, s/77^^5 (besides smuk) ' defile, narrow 
passage between mountains, bottleneck, narrow stripe '. 

References: WP. II 253 ff., WH. I 402 f., Trautmann 189 f., 271, Kuiper Nasalpras. 124 f., 

129. 

Page(s): 744-745 



Root / lemma: meuR- 

Meaning: to scratch, tear 

Material: Gr. apuKaAai ai qkiSec; twv peAwv, rrapa to ajjuaosiv Hes., ajjuoou), Attic apuTTU) 

" split, scratch ', a'puxn 'crack, scratch ', etc.; Latin mucro^ a sharp point, edge, sword's 

point '; perhaps to Old English ^e-/77ysc5A7 "plague, deform' {*muhskjan) and Lithuanian 

/77^5//"hit'; perhaps also Old Indie mustfi., Avestan must/-l\st'7 

References: WP. II 255, WH. II 117 f. 

Page(s): 745 

Root/ lemma: meu-1, meue-. mu- 

Meaning: wet; dirt; to wash, etc.. 

Material: A. Old Indie mutra-n. "urine', Avestan mu^ra-n. " filth, smut' (: Middle Low 

German modder e\.c.); 

Maybe alb. mut, mutra{p\) 'excrement, dirt' 

Armenian -/77oy/7 "wash in the pot' {*mou-no-)\ 

gr. Cypriot [juAaaaaGai "be washed', Hes. {*mu-dlo-)\ 

Middle Irish munm. "urine'; mur'sWme, mud'; 

perhaps (?) Dutch moo/, mnl. moy, Low German /77c»//'e'y' "beautiful' {*mou-/o-' washed, 
made clean '); 

Latvian maut^ submerge, swim, swig ', Old Prussian aumusnan^ wash, cleansing ', 
causative (Iterat.) Lithuanian maudyti, Latvian maudaV bathe somebody ', Lithu

===  meuk 2519579
ers, forgives '; Armenian moranam ^iorqei' (Meillet, 
Esquisse2 40); Gothic marzjan ^ anger' , Old English mierran. Old Saxon merrian. Old 
Frisian meria. Old High German marren, /77e/7'e/7 'hinder, disturb, bother'; Old English a- 
m/erran'spoW, Old Frisian mere'ban6, strap, manacle'; Lithuanian marsas^ oblivion ', in 
addition marsus^ forgetful ', Latvian aiz-marsai. 'forgetfulness'; Lithuanian mirstu, mifsti 
(only with uz-, pa-) and Latvian aiz-mirstu, a/z-m/rst lorgotten' , Lithuanian Kaus. mars/nt/" 
make forget '. 

References: WP. II 279, Trautmann 187. 
Page(s): 737-738 

Root / lemma: met- 

See also: see above S. 703 f. under me-2 and me-3. 

Page(s): 741 

Root / lemma: meug-1 

Meaning: to take by surprise, wily 

Material: Latin muger^ der Falschspieler beim WiJrfelspiel ' {*mug-ro-s^ lurking '); 

Old High German muhhari, muhh(e)o^ highwayman, mugger, footpad, thief, muhhon^ 
lurk secretly, attack ', Middle High German vermuchen^ heimlich auf die Seite schaffen ', 
late-Old High German muhhilari {{o *muchildn). Modern High German Meuchler, Middle 
High German miucher secret ', Old High German muh-heimo^ cricket, leaping insect 
which is related to the grasshopper ', ablaut. Middle High German mocken^ lie hidden, 
concealed ', Middle English /77/c/7e/''thief, engl. dial, /o/t?/^/? 'hidden, concealed sein, 
steal'. 

Maybe alb. mih' dig, hoe '. 

References: WP. II 255, Wissmann Nom. postverb. 137; probably to Folgendem. 
Page(s): 743-744 

Root / lemma: meug-2, meuk- 

Meaning: to slide, slip 

Note: also with aniaut. 5- 

Material: A. Latin /77Jci/s 'mucus', mucor^ mildew ', e-mungo, -ere^ to wipe the nose, blow 

the nose, to cheat, swindle '; mugilvn. ' mullet '; 

Maybe alb. myku^ fungus ' a Latin loanword. 



gr. aiTo-iJuaaoo " blowing one's nose, clear one's nasal passages by forcible exhalation; 
cheat, deceive, swindle; betray, be disloyal; gull, fool', ano-pu^ic; ' the blowing one's nose ' 
(: Latin e-m undid), puKirip 'nose, nostril '. 

Maybe Greek (s)MUKTrip "nose, nostril ' > Basque {*smuktor) sudur^ nose' : Albanian 
{*smukta) hunde, hunda^ nose', hundor^ nasal'. 

gr. \x\}%a 'mucus, nose' (based on *fjuK-a-6(; 'slimy', as also:) mu^O(;, jju^Tvoc;, jju^ojv ' 
mullet ' (also apu^wv with ani. 5- as by Hes. also apuaasTai, apuKirip), \x\}gkoc, piaaija 
Hes. (*[JUK-a-KOc;), a|Juoxp6(;, ajjuxvoc; ' unsoiled; untainted, pure, holy'; |J

===  meuk 2522412
iddle High German muchein, mucheln^ moldy smell'. Old Icelandic mjukr{o\A 
of it engl. meek) 'soft', changing through ablaut Gothic muka-mode'r gentleness, softness, 
kindness ', mnl. muik^soii'. Modern High German dial, maukig^ decayed ', Swiss mauch^ 
rotten, decayed, decomposed; brittle, faint, languid, hungry' (as Swiss mucMla\nt, 
languid, hungry'); Middle High German muche' quitter, infection of the hoof, Gothic 
*maukd in prov. mauca ' intestines '; 

Latvian mukis, muklams^ fenny, boggy, marshy ', muku {*munku), mukV sink into a 
marsh '; 

Serbo-Croatian /77£/A^/V' humid, wet'. 

B. Old Indie *munakti, muncati, mucatr releases, allows to loose', mukti-^ lysis, 
dissolution, disintegration, release, abandonment '; Avestan fra-muxti-^ loosening '; 
compare Old Indie munthate ' flees ', Old pers. amu(n)&a ' he fled ' from * mu-n-eth-m'r, 

Lithuanian munku, muktT escape; to get away ' = Latvian muku, mukV get free, flee' 
(and ' sink into a marsh ' see above); Lithuanian (s)mauktr wander stealthily ', Latvian 
maukV strip, wipe ', Lithuanian (s)munku, (s)mukti^ sink sliding, slip '; 



Slavic *(s)m-bkngtr slip, slide' in Czech smeknoutF withdraw from, take away ', Old 
Church Slavic Refl. smycg, smykati sg^ grovel, truckle, creep ' (modern Slavic also " slip, 
stumble, glide, slide, strip, wipe '), russ. -Church Slavic nrbknuti sja^ go over, go across, 
cross over, pass over, pass by, pass ', Old Church Slavic mhcati {nrbke-) " throw, cast, 
hurl ', etc. 

A root form meukh-W\Vc\ the specific meaning ' slip into ' probably in Armenian mxem 
{*muxam) " stick in, stick into, put in, dive, bathe ', /77i/A' "dyeing', mxim^ enrare, insinuarsi, 
ingolfarsi ', at first to gr. |jux6(; m. " internal angle ' (perhaps "*hiding place, nook, bolt- 
hole'), Muxioc; " innermost, inmost, located farthest within '. 

Auf (sjmeugh- based on the Germanic family: 

Old Icelandic smjuga' creep into or crawl through ', Old English smugan' slip, slide; 
stumble, grovel, truckle, creep ', Middle High German smiegen^ crouch ', Modern High 
German schmiegen, Kaus. Old Icelandic smeygia^ nestle, cuddle, snuggle, lure, tempt ', 
Middle High German sich smougen' crouch ', Old English 5/77ea^ 'smart, sharp witted, 
shrewd', s/77e5^5/7 "think, seek ', smeagorv\arro\N, tight, slim, slender, thin ', Old Icelandic 
smugat " loop hole; hiding place ', further Swedish i mjugg, Norwegian

===  meuk 2527927
d Indie mudira-m. "cloud', lex. also "frog'; in addition Old Indie m6date^\s funny', 
moda-m., modana-n. "lust, cheerfulness ', Avestan maodano-karana-^ causing lust ', Old 
Indie /77^o''//a "blithe, glad', Avestan a-h§musta- {*a-sam-musta-) " disgusting, unsavory, 
distasteful'. Old Indie mud-, mudalust, pleasure, joy', mudra-' funny '; 



gr. |ju^w {*mudjd) "suck', [juSoc; m. " damp, decay ', puSau) "be humid, wet, decayed ', 
Mu5aA£0(; "humid, wet' (hom. u: through metr. lengthening, whereupon newer puSaivoj " 
irrigate '); 

Latin mundus {see above meu-)\ 

Middle Irish muad {*moudo-) "pure, stout, proud'; 

Middle Low German muten^ wash the face ', Old High German muzzan^c\eav\\ 
Swedish dial, muta^ fine rain', Dutch /77c»/"fine rain'; 

with ani. 5-engl. smut^ smirch, stain, splotch ', Middle High German smuz. Modern High 
German Schmutz, Middle English smotten, smoteren " befoul '; 

Lithuanian mudrus, Latvian mudrs^a\ert, awake, smart' (: Old Indie mudra-), Lithuanian 
mudrinti, Latvian mudfV set in motion '. 

From in -es-stem m(e)udes-\\3Ne derived: 

Latin mustus {*muds-to-s) " young, new, fresh ' (originally "damp, humid, wet'); gr. puao(; 
(*|ju5ao(;) n. " maculation, blemish'; [juaap6(; " dishonorable '; Old Irish /77c»ss5c/7 "impure, 
unclean' {*mud-s-ako-), cymr. mws, bret. mous ds.; ndd. muss/g'd\(iy, filthy'; russ. muslitb 
" drool, drivel, slaver ', musljaki, " dribbler, unclean person'. 

Maybe alb. /77i/s/7/"must, new wine' a Latin loanword. 

2. meug-, meuk-^ slippery ' see below esp. headword. 



3. meu-r(o)-e\.c.: 

Armenian /770/''smut, swamp, marsh' {*m9u-ri-l), mrur^ deposit ' {*murui)\ gr. pupco 
(*[jupju)), pupofjai " let flow, weep, cry', aAi-|Jupn£ic; ' flowing to the sea '; whether here 
Mupio(; " eternal, infinite, endless ', [jupioi '10.000'? Latin muria' brine, pickle '? Lithuanian 
murstu, murtr become soppy ', m. PI. mauraf duckweed, stemless water plant ', Latvian 
maursm. 'lawn', Lithuanian /77a^/'as 'slime, mud', ablaut, murasxu. 'smut', Latvian murfV 
befoul '; russ. murvn. muravat ' oat-grass, false oat, tall oatgrass ', dial. ' mildew ', muryj' 
dark grey ', etc.; compare S. 741 Middle Irish mur^sWme, mud'. 

4. meus-, musos, from which mus, musos, root nouns ' moss, mildew '. 

Old High German Old English mosn. ' moss, swamp, marsh'. Old Icelandic mos/m. ds., 
zero grade Old High German m/os, Old English meos' mo

===  meuk 3291995
sinnen', Dutch m/jmeren'deep nachsinnen'; Gothic maurnan. Old 
English murnan. Old High German mornen'care for, worry, anxiously worry about'; 

Old Lithuanian meref/^care for, worry', lengthened grade serb. mar/f/^s\c\r\ kijmmern 
um', etc. {*mdr-)\ 

2. as "sinnen, sinnend dastehen' = 'hesitate' probably die group Latin morat "Verzug, 
delay'. Old Irish mar{a)/m' stay '; corn. bret. mar'6oubt'; 

3. here as "jemanden wherewith consider, versorgen; Zugedachtes' also gr. pEipopai 
{*o[iZQ\o[ia\) 'erhalte allotment ', poTpa ' allotment, fate, destiny' {*sm-, compare hom. Kara 
MpoTpav), Perf. hom. eppops "hatAnteil', ei'papTai (*o£-apapTai) "es is durchs lot, fate 
zugeteilt', sipapiJEvr) "fate, destiny', [^tpoq n., [j£pi(;f. " allotment, part', pspi^u) "divide', 
M6po(; m. "lot, fate, fate, destiny, person's lot in life', Kaapopo(; 5uaTr|vo(; Hes. 
{*Kaio[}opoq; Koppopo^Od. is newer formation), hom. appopoc; "unteilhaftig', nijopic; 
za^zpr\[^tvr\ Hes., lak. popa "dividing off, partitioning off of spartanischen Heeres', [jopiov 
"part'; probably also afjapravu) "verfehle' due to eines *a-/7ijapT0(; "unteilhaftig'; Latin 
mereo, -ereav\6 mereor, -erf earn, acquire ' (i.e. "erhalte allotment ', "erwerbe mir meinen 
allotment '), merenda "Vesperbrot, Mahlzeit the animal' ("*wherewith person and animal to 
consider is'). 

References: WP. II 689 f., WH. II 67 f., 110, W. Oehl IF. 57, 2 ff.; Vendryes Et. Celt 2, 133 
f., DuvalEt Celt 6,219 ff. 
Page(s): 969-970 

Root / lemma: (s)meukh-, (s)meug- (s)meugh- 

Meaning: to smoke, smoke n. 

Material: Armenian mux. Gen. /77A'c>y "smoke'; gr. apuxw (x = kh or gfr, sopuynv from the g- 

form) "allow verschwelen; in langsamem fire consume'; Irish /77i7c/7 "smoke', cymr. mwg 

(with alternation 0: u), corn. mok6s., bret. moug, mogl\re', moged'smoke' {-kh- or -k-); 

with -g. gr. opuynvai; Armenian murk. Gen. /77/'/roy"sengend' {*smugro-); 

Old English smeocan ^ smoke' , mnl. sm/eken and smu/ken 'smoke'; Kaus. Old English 
sm/iecan' smoke, fume ', Middle Low German s/77d/re/7"schmauchen, fume, through Rauch 
choke'; Old English smTecm. "smoke'. Middle High German s/77c»£/c/7 "smoke, haze, mist'; 
Old English smocam. 'smoke', s/77c»c/a/7 "smoke, fume '; 



Lithuanian smaugiu, smaugtr choke; suppress, crush (originally through smoke), 
strangulate '; perhaps russ. smuglyj, kir. smuhfyj^ brownish black ' ("smoke-color '); 

===  musti 1064728
ing drug, posion, medicine, herb' similar to Sanskrit a/a- "poison', 
obviously alb. has preserved the old laryngeal /?-. 

clearly alb. shows that from Root/ lemma: al-2\ (to grow; to bear; grove) derived Root/ 
lemma: el-3: ol-\ (to rot, poison). 

guttural extension lies before in: 

Old Indie „/7/sa-/7" viscous, smooth, slippery ', Latin alga\. " seaweed, kelp ' from * Jga 
(compare Old English m/os "slime, mud, dampness ': engl. m/cos "seaweed') and very 
numerous Germanic, esp. Scandinavian-isl. forms, as: Norwegian dial, ulka' fester. 



disgust ', refl. " start to rot ', ulka^ mildew, adiiesive mucus; repulsive, unclean woman', 
etc. hereupon also Danish ulk^ bullhead ', Norwegian ulk^ toadfish ', further Norwegian 
dial, olga " feel disgust, nausea ', elgja " want to vomit ' etc., isl. also sela ( *alhian)\ 
Norwegian dial, alka^ pollute, litter ', ndd. alken^ touch impure things, step on dirt '; -sk 
show Danish dial, alske^ pollute ', ndd. alschen, Frisian alsk, a/s/r'impure, unclean, spoil' 
etc. 

Maybe alb. aike, a/Aa "floating cream, wool fat, dirt, stain' : Old Indie alaka-^ poison '. 

That Latin ulva ( *oleua) " swamp-grass, sedge ' moreover belongs, is very probably; 
Lithuanian a//rs/75 'puddle' could go back to *olg-sna. 

Dental extension appears in: 

Armenian ait {^ Id-) "smut, filth ', aitiur, eit/ur {under elteur) " damp lowland, depression'. 
In addition Old Norse uldna^ mildew ', Old High German oltar^ dirt crumb ', probably also 
Old Norse ylda^ mustiness smell '. 

/7^formant is found in: 

Norwegian dial, ulma^ mildew ', ndd. East Frisian olm, ulm^ decay, esp. in wood'. 
Middle Low German ulmich^ fretted from decay ', Middle High German u/m/c6s.; 
Lithuanian elmes, almens " the liquid flowing from the corpse '. 

b'^-extension lies in Armenian aib^ filth ' before. 

Maybe in b^- suffix alb. C/ia/b) ka/b' rot, decay ', qe/b' pus' common alb. /?- > k-. 

References: WP. I 152 f., WH. I 28 f., Petersson Heterokl. 165 f. 
Page(s): 305 

Root / lemma: eM, ol- 

Meaning: expressive root, onomatopoeic words 

Material: Armenian afmuk'6\n, fuss, noise, agitation etc' {*Jmo), alavt'-k'^ imploration', 

o/t* "lament', o/o/r' "urgent request'; 

gr. okokuq "lamenter, effeminate person', oAoAuyn " wailing, lament ', 6Ao(pu5v6(; " 
lamenting', oAocpupopai " lament '; perhaps also Ekzyoq n. "dirge', zKzoq m., later n. "pity'; 

asl.y5//77/'

===  musti 1710293
dersen KG. I 108, ©through the 
influence of /esds.); /"from Old Irish ^/Ts'fire', grJsaid^ fires, stimulates ' probably from 
*ghrenso-, in spite of Thurneysen Gr. 130. 

References: WP. I 687 ff., WH. I 532 ff., Trautmann 79, 102. 
Page(s): 493-495 

Root / lemma: g''hdei(9)- 

Meaning: to perish, destroy 

Material: Old Indie ksinati, ksindti{ : gr. *(p9ivF-u)), ksayat/" destroyes, allows to pass ', 

participle ksita-h "exhausted' (= gr. (p9iT6(;; srava-h aksitam = gr. Kktoq acpGiTOv 

"indestructible fame'), ksTna-h6s., ksTyate^ schwindet hin, nimmt ein Ende ', ksaya-h' 

decline, reduction, ruin' (: gr. cpGon f.), /rs/if/-/? "crime, ruin' (= gr. cpOiaK; and -?- Latin s/f/s; 

compare -tu-stem Latin s/'tus); [common Old Indie g"'/!- > ks- : gr. g^h- > ph- : Latin ks- > s-] 

prakr. ajjhitah- (= acp0iTO(;),y/7/77a- (= Old Indie ksTna-); 



Avestan ayzonvamnam^ sich nicht mindernd ' (Kuiper Nasalpras. 65''); 

gr. ep. cpGlvoj, Attic cpOIvw (*(p6ivF(jo, see above) "destroy', mostly intr. " decay, wane, 
perish ', cpGivu-Gu) " decay, wane, make disappear', Fut. cpGEiau) (Attic dnocpGiau)), Aor. 
scpGsiaa (Attic anscpGTaa), scpGijjnv, (pGip£vo(; "destroy'. Pass, "be destroyed, perish', 
participle Perf. Pass. cpGiToq, cpGori "consumption, tuberculosis', cpGiaic; ds. (see above); 
about perhaps old double forms, as njivsaGai, njiva^siv " allow to drop, lose flowers or fruits 
', ijjioK; aTTcbAsia Hes., s. Schwyzer Gr. Gr. I 326. 

From Latin probably situs, -us' rust, mould, mustiness, dust, dirt, filthiness of the body, 
neglect, idleness, absence of use, a rusting, moulding, a wasting away, dulness, inactivity ' 
and s/f/s' thirst ' (if actually "*decline, languishing'). 



Maybe alb. et' thirst ' : Italian sete, Spanish sed, Catalan set, Croatian zed, Czech zfzen, 
Furlan set, Galician sede, Leonese sede, Portuguese sede, Romanian sete, Sardinian 
Campidanesu sidi, Valencian se/" thirst ' < Latin sitis^ thirst '. 
References: WP. I 505 f., Schwyzer Gr. Gr. I 326, Benveniste BSL. 38, 139 ff. 
Page(s): 487 

Root / lemma: g^hder- 
Meaning: to run, flow 
Note: (or better g^'der-ll) 

Material: Old Indie ksarati^ streams, flows out, melts away, disappears ', ksara-m^\Na\.er', 
ksarayat/" allows to flow ', ksa/ayat/" washes away ' (compare Wackernagel Old Indie Gr. 
I 241); Avestan yzara/t/" streams, boils up ', yzaraye/t/ ^aWows to flow ', with i//- "allows 

===  musti 2541299
mlicht' cow's milk '): Old Irish *to-in-uss-mlig- " to 
bring forward publicly, propose openly, publish, promulgate '; causative Middle Irish bluigid 
"milks, blackmails, mulcts '; cymr. blithm. "milk; producing milk ' {*mJg-ti-)\ gallorom. 
*Mig/ica/'e"milk'; 

alb. miel, miT milk ' ( *melg-)\ 

Old High German milchu, melchan. Old English melcan'rcviWC (stem V.; against it Old 
English meolcian. Old Icelandic /77/c»//ra Denominative from *meluk-''(r\\\V! see below). Old 
High German chumelktra' a milking-pail, milkpail ' (perhaps replicated Latin mulctra). Old 
Norse mjaltr' producing milk ' {*melkta-)\ with zero grade Old English molcen. Middle High 
German molchen, molken' thick milk'. Modern High German Molken, and Old Icelandic 
schw. V. molka'vnWV!, mylkja' suckle '; 



because of second of the vowel controversial is the original affiliation from Gothic 
miluks. Old High German miluh. Old English meolc, mioluc. Old Icelandic mjglk^ rr\\\V!\ /■ 
extension in Old English milcav\6 Modern High German Hessian melx {*mili-k-)\ after 
Specht (Indo Germanic Dekl. 126) must be assumed is generally a dissyllabic root; from 
West Germanic probably Latin melcat " sour milk '; 

Lithuanian melzu, milzti, participle milztas{= Old Indie mrsta-, Latin mulctus) "milk'; 
Iterat. malzytr, russ. -Church Slavic m-blzu, mlesti^mWV!, Slavic *me/z/vo'\n Slovak, miezivo, 
russ. molozivo (etc.) " beestings '; 

with o-grade: serb. m/azm. ' Milchstrahl ' by milking (the glottal stop from serb. musti = 
*mlz-ti\s wrapped from the old lengthened grade of Inf. mlesti= Lithuanian melzti); 

Tocharian A malklune " the milking '; A maike, B malk-wer^ vnWV! . 

References: WP. II 298 f., WH. I 741 f., II 62 f., 121 f., Trautmann 178, Specht Indo 

Germanic Dekl. 147 f.; 

See also: compare also /77e/Ar-and merg-. 

Page(s): 722-723 

Root / lemma: melo-, smelo- 

Meaning: small animal 

Note: 

Root/ lemma: melo-, smelo-: small animal, derived from Root/ lemma: mel-6, mele- : 

dark colour (black, dirty, etc..) 

Material: Gr. pnAov n. "small cattle, sheep'; Old Irish /77/7n. "(small) animal', cymr. mil, 
acorn, bret. /77//"animar; Germanic in /77a/5(Lex Salica), Dutch /77aa/"young cow'. Old 
Germanic Mr|Ai-pOKOv opoc; "the resin'; changing through ablaut Armenian /77a/"sheep, 
aries, ram'. 

There "small cattle' could be an old nominalization of an Adj. meaning "small', one 
compare
```


## [2026-09-07T17:36:50.491Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'Page\\(s\\): 74[1-6]',t):\n    seg=t[max(0,m.start()-4000):m.start()+40]\n    # find root lemma start\n    i=seg.rfind('Root / lemma')\n    if i<0: i=seg.rfind('Root/ lemma')\n    print('#####')\n    print(seg[i:] if i>=0 else seg[-800:])\n    print()\nEOF",
 "description": "Print Pokorny roots on pages 741-746"
}
```


### [2026-09-07T17:36:51.815Z] TOOL RESULT

```
#####
Root / lemma: meug-1 

Me

#####
Root / lemma: meug-2,

#####
Root / lemma: meuR-

#####
Root / lemma: meuR- 

Meaning: to scratch, tear 

Material: Gr. apuKaAai ai qkiSec; twv peAwv, rrapa to ajjuaosiv Hes., ajjuoou), Attic apuTTU) 

" split, scratch ', a'puxn 'crack, scratch ', etc.; Latin mucro^ a sharp point, edge, sword's 

point '; perhaps to Old English ^e-/77ysc5A7 "plague, deform' {*muhskjan) and Lithuanian 

/77^5//"hit'; perhaps also Old Indie mustfi., Avestan must/-l\st'7 

References: WP. II 255, WH. II 117 f. 

Page(s): 745 

Root/ lemma: meu-1, meue-

#####
Root / lemma: meu-s- 

#####
Root / lemma: meu-2, meua

#####
Root / lemma: mezg-1 
Mea

#####
Root / lemma: mezg-2 

#####
Root / lemma: megh- 

Mea

#####
Root / lemma: meuA^-, mauA^-, mud'^- 
Meaning: to complain or care about smth. 

Material: Npers. moja^ lament' (-/from -cf-, compare:) must' lament ' (-s/-from -d'^sf); gr. 
|j09o(; m. ' discourse ', nuGsopai ' speak, think; consider'; Gothic maudjan, ga-maudjan' 
remind sb'; Lithuanian maudziu, mausti' long, want strongly ', apmaudas' displeasure, 
care '; Old Bulgarian mysib 'thought, notion' ( *mud-slio-)\ perhaps nir. smuainidh' thinks '. 
References: WP. II 255 f., Trautmann 171 f. 
Page(s): 743 

Root/ lemma: ma-r. Gen. m

#####
Root / lemma: mod'^ro-or 

#####
Root / lemma: md[u]-r

#####
Root / lemma: mregh-m(n)o
```


## [2026-09-07T17:36:56.842Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\ni=t.find('Root / lemma: meu-2, meua')\nprint(t[i:i+3000])\nEOF",
 "description": "Print Pokorny meu-2 entry"
}
```


### [2026-09-07T17:36:58.079Z] TOOL RESULT

```
Root / lemma: meu-2, meua- 

Meaning: to move 

Note: (Aryan partly also mjeua- : mTu-) 

Material: Old Indie /77/Va// "shoves, throngs, moves' = Avestan ava-mivamahi^ we remove, 

take away ', Avestan a-muyamno' unbeweglich, woven nicht abzubringen ', Old Indie 

kama-muta-^ moved by love ', mura- " pushing, hurrying'; 

gr. apEuaaaOai " advance, excel, surpass ', gortyn. a|j£Fuaaa0ai "trade drive, push', 
aijuvw " ward off, drive back, Med. " verteidige mich ', aiJuvTOjp "Abwehrer, avenger', 
MuvaaOai " plead, allege ', puvri " alleged reason, avoidance, excuse, escaping, fleeing '; 
compare Old Irish /77J/7-" direct, guide ' (E. Lewy); 

Latin moved, -o/io" to move, stir, set in motion, shake, disturb, remove ', participle motus 
( *movi-to-s) = Umbrian comohota f\b\. Sg. f. " a moving, motion '; 

Lithuanian mauju, mautT aufstreifen, anstreifen (e.g. a ring to a finger)', uzmova^ gN 
was aufgestreift wird ', rankiq uzmova " muff '; Middle Low German mouwei. " muff ' 
Modern High German hemds-mauen " shirt sleeve '. 



A s-extension seems *meu-s-\n Old Indie musnati, /77dsa//"stiehlt', mosa-^ robber, 
thief, Franconian (Lex salica) chreo-mosido^ corpse spoliation '; see below S. 753 under 
mus. 

References: WP. II 252 f., WH. II 116, Trautmann 172. 
Page(s): 743 

Root / lemma: mezg-1 
Meaning: to plunge 

Material: Old Indie majjati^ disappears, goes down ' (particle Perf. Pass, magna- from 
*mazgna-), Kaus. majjayati^ sinks '; Latin mergo, -ere^ to dip, dip in, immerse, plunge, 
sink, bury ', therefrom mergusm. " a diver (a water-fowl) ': Baltic iterative *mazgaid' dive 
several times, wash' in Lithuanian mazgoti, Latvian mazgat^\Nas\\\ compare Estonian 
moskma, Mordovian musloms, Samojed /77as^ Hungarian mosn/^ wash', etc.; doubtful, 
whether here gr. (jIgyu) 'mix, mingle' from *mi-mzgd\ different above S. 714. 
References: WP. II 100 f., WH. II 76 f., Trautmann 173, H. GiJntert Kalypso 51. 
Page(s): 745-746 

Root / lemma: mezg-2 

Meaning: to bind, attach 

Material: Old High German Old Saxon masca. Old English max, maescr' stitch ', Old 

Icelandic mQskvi^s:, 

Lithuanian mezgu, megsti^ tie, bind, knot, knit ', mazgas, Latvian mazgs^Vx\o{\ 
Lithuanian mazgytiWer. " knit ', makstyt/l\ax, wattle, braid', Latvian mezget, mizgef 
dislocate, luxate, crick ', mezgJV grow around, entwine itself around ' (russ. mazgart " 
spider'? s. Berneker II 28). 

References: WP. II 301, Trautmann 172. 
Page(s): 746 

Root / lemma: megh- 

Meaning: well-disposed, friendly 

Material: Gr. n£pi-r||J£KT£U) 'be unwilling ' (from *a-|j£KTOc; " unwilling '?); Gothic megs, 

Swedish mag^ son in law, husband of the daughter ' (compare French belle-mere). Old 

Icelandic /77ag/'" kinsman, relative through marriage'. Old English m^g. Old Saxon Old 

High German /77ag "kinsman, relative', etc.; Lithuanian megstu and megml, megtr like, be 

fond of ', megintr assay, try ', Latvian megV be good for, be suitable for '. 



References: WP. II 256, WH. II 5; Hj. Frisk Er
```


## [2026-09-07T17:37:10.039Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN musti/most ===\" && grep -n -i -E 'mušt|musti|mušti|most\\b' HRN.txt | head -30\necho \"=== HRN moza/muza ===\"; grep -n -i -E 'mōza|moza|mūza|muza|maoč|maok|mōzag|muc' HRN.txt | head -40",
 "description": "Grep Horn for musti and muza"
}
```


### [2026-09-07T17:37:10.103Z] TOOL RESULT

```
=== HRN musti/most ===
8412:kurd. mOsT Tisch*; LW. bei. muhi, n. mdhhj, mahty
8542:aw. musti.[masah' 'faustgross* ; phlv. must (vd. 17
8543:(18) Gl.) 2), mtistih (AV.), must (PPGl.); ai. musti-,
=== HRN moza/muza ===
577:ist; heraz 'Schmuck', beräztdeM (No. 193) können wegen
864:lit. (d. i. ö) arischem ä entspricht. Skr. ä + [/"muC'
983:61. äytn 'Sitte, Schmuck*, äJTw-); aöme^ adme 'Freitag*.
1574:133. öreng 'Schmuck (z. B. Vis und Rämin S. 24 Vers 4
2098:193. herä» *Schmuck, Schönheit*, berüzlden, berOzis^),
2112:buräh oder beräh 'Schmuck* Vor, das in den Wörterbüchern (FR, FJ,
3070:In Indien spricht man piser ; die nämUche Aussprache soll auch
3345:{zaranyö.pis-^ paesah- [pa^sa-) 'Schmuck', pacsa- *bunt
3347:ai. pe^aS' 'Schmuck, Zierrat'.
```


## [2026-09-07T17:37:11.816Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC meuk ===\"; grep -n -i -E 'meuk|meuq|mūk|meu-k' IEC.txt | head -40\necho \"=== IEC meo/meon ===\"; grep -n -E '\\bmēo\\b|meon|mēon' IEC.txt | head -20",
 "description": "Grep Mann IEC"
}
```


### [2026-09-07T17:37:11.931Z] TOOL RESULT

```
=== IEC meuk ===
10247:måà2- (2) “make, shape, prepare, cook, boil". WP II, 226 & 268 Gk. cf. magis, gs -ídos, f. ‘dough’; mág-eiros, m. (cook: LG macker, m. companion"); mák- tra ‘kneading-trough’; maktós, adj. (kneaded, pulped'. To másso, v.); OHG mahhon ‘make, prepare’; OE macian ‘shape; prepare; arrange; use; fare; compare; transform’; mec, adj. ‘suitable; friendly; equal; matched'; maecca, mf ‘mate’; Du. maken, v. ‘make’; mak, adj. ‘docile’; (long-gde in) meuken ‘soak, simmer, stew’; G machen, ge-mach, etc: ON makr, adj. ‘amenable, suitable; maka, pl. mokur “mate, wife’, maki, m. ‘match’; mok, npl. *in- tercourse'; LG cf. mack, ad]. ‘tame’; Sw. mak, n. ‘comfort; make, wm. ‘equal, match’; maka, f. ‘wife’ beside maka, v. “inch forward’;
11350:‘release, let fly’; mükno, -noti, v. tr. ‘remove’; intr. ‘pass, move’; R mču, mčať “carry off, remove’; -sa ‘escape’; Pol. mknac sie ‘flee’; Cz. cf. s-mekat, -meknout ‘remove — the haft’; Li. munkù, mùkti ‘slip away, steal away”; Latv. müku, mukt, v. (1) ‘escape. (Isophone: Latv. mūku, mukt ‘get stuck, bogged down’ & cf. Blg. mákna “drag'). See next
11351:mūk- (1) “grow dark, get filthy, become foul; foul, murky; foulness, murk?. (Variant: muk-. Gk. W forms ambig., cf. smug-) Skt. cf. mukah “smell of cowdung'; Gk. mükes, pl mükai, m. ‘fungus; Hes. míükos ‘foul’; Alb. myk, m. ‘mildew’; mykem "eet mil- dewed'; Lat. müceo, ere, v. ‘get mouldy’ be- side OLat. muccus ((snot, whence OFr. moche) beside Lat. mücus, m. id.; lr. müchaim, v. ‘stifle, obscure, extinguish’; múch, f. ‘smoke, gloom, grief; müchna, adj. “dark”; W (short vowel) mwg, m. ‘smoke’; mwci, m. (1) ‘fog’ beside (long vowel) migen, f. ‘bog; Br. mug, muk “purple dye-mollusc, murex’; Li. muküs ‘slimy, boggy’; Latv. cf. müku, mukt, v. ('squelch, get bogged down’, but cf. muk- above); cf. mukls, adj. ‘boggy and see muklos (2) WP II, 310 Gk. mükáomai, id.; Alb. cf. (short vowel) mukoj, id.; W mig, pl. ion, f. beside migiad, m. (“hoot; hooting’, fr. *müki-, *mükjot-); OHG mühen, v. ‘moo’; R myCàt, inf. id.; Li. mükiü, mükti & mükioju, -ioti, id.
11364:mükóo(n) (mükró-) “pike, spike, peak, pile’. WP II, 311 Per. mūk ‘sting’; Hes. mükon ‘pile’; Lat. cf. (variant) mücro, gs -onis, m. (“point of sword". Cf. (?) Hes. mókron 'sharp); OE müha, müga, wm “pile, rick’. (Not also R mys ‘headland’ if *-k- as in Per. mük)
11374:muktos ‘left, freed, abandoned, loose, dash- ing, rapid’. Cf. muk-. WP II, 254 Skt. muktáh, pp. ‘freed, loose’; Romani muklo ‘freed, allowed; It. cf. motta, f. ‘subsidence’ beside mucciare, v. ‘run away’ (background uncertain), W mwth, adj. ‘rapid’; cf. chwi- mwth, id. (fr. *su1-9; Li. müktas, pp. of mun- kü, mùkti ‘slip, fall, dash, run’; Latv. mukts, pp. of mukt, 1sg. pres. mūku (1) “be absolved, get free, escape’; Cz. cf. (obs.) mektati se ‘fluc- tuate'. (Isophonic: Arm. mtem ‘gather’, but phon. ambig.)
11375:(müktos, see mūk- (1) & (3))
=== IEC meo/meon ===
4532:ghabh- (1) ‘seize, hold’. WP I, 344. (Variant: ghabh-) Skt. cf. Vedic gabhastib “arm, hand”; Lat. habeo; Osc. cf. hafieist 3s. ‘shall have’; ni hipid, 3s. pres. subj. “shall not have'; Umb. haf-; Mir gabim ‘seize, hold’; Ir. gabhaim, id. (and 'receive); W cf. gafael, f.n. “hold, grasp’; Go. gabei ‘wealth’; cf. gabeigs: OHG (Alemannic) kepic ‘rich’ (LW in OCS gobizü, id.). Variant *ghābh- in OCS gabina ‘produce’; Slovak habať ‘seize’; Blg. gabam ( ‘dupe’, lit. “have? someone). Further: Li. gábas ‘miser’; gabštůùs ‘greedy’, cf. gabenù, -énti ‘fetch’, be- sides gobiuos, gobētis ‘covet’
6512:ioteros ‘whichever (of two); either; other (of two)’. Cf. quoteros, totero- Vedic yatarah; Av. yataro; Cypr. óteros; Alb. jatér ‘other’; OCS jeterü ‘some, any; a certain; someone’.
11651:néquis (néquoios); néquid (anybody, no- body; anything, nothing. Cf. nequos & quis, quid, quod Skt. (Vedic) nákis ‘nobody; not, never’; Av. cf. naecis ‘nobody’; Oss. cf. nići, Dig. neke ‘nobody’; nici, Dig. neci ‘nothing’ (fr. nei-?); Lat. (ut) nequis; Umb. ne. . .phim (sic: acc. sg.); OCS cf. nékyj ‘somebody’; adj. "a cer- tain. . ?; něčij, prn. (someone's, and com. SI.)
11743:-nəm (-nm) a reinforcing particle added to pronouns as in Gk. ti-ná ‘someone’; Lat. quid- nam, inter. & rel. ‘what’
14229:quoteros, à, compar. extn. of type quo-, q.v. *which of two, which, who; either' WP I, 521 Skt. kataráh “which of two”; Av. katàro, id.; Oss. kadär ‘someone’; Gk. póteros, dial. kó- teros, as Skt.; Lat. uter, fn: utra, utrum, (by ‘false’ division of necuter ‘neither’), as Skt.; Osc. cf. pútúrús-pid, mpl. (^whoever', fr. *quo- teros-quid); Umb. cf. -podruh- beside putres; Olr. cf. cechtar, Ir. ceachtar (‘either of two, each; any’ fr. *quis-, quid^); Go. hwapar, as Skt.; OE hwaóer, id.; OFris. hwedder, id.; ON hvárr, id. (also "each of two"); OHG cf.
18436:-teros, à, om, comparative suffix; pronomi- nal extn. Skt. ut-tarab, à, am ‘outer’; cf. itara, invar. ‘other’; kataráh “which, of two’; Av. cf. kataro, prn. id.; Oss. kadär, Iron. Cídár ‘someone’; Per. bih-tar, bah-tar (Cbetter', see uesus); bad- tar, bat-tar ‘worse’; Tokh. lyu-tàr, prn. ‘more’; Hitt. kat-taras lower; Gk. hüs-teros (“last': Skt. uttarah); Alb. ja-tér “other”, tje-tër, id.; Lat. de-ter ‘bad, weak? exter & exterus ‘foreign’; MIr. air-ther, adj. (front, eastern": Lat. prac- ter "before, beyond, beside"); Go. (and com. Gmc.) hva-par (^which, of two’. See quoteros); OE hwæðer, id. beside hider, pider “hither, thither’; OCS vü-torü ‘other’; Cz. úterý (*den) ‘Tuesday’; OCS koteryí, kotoryí, prn. ‘which’; Li. añ-tras ‘other’; katràs, à ‘which, of two'; Latv. otrs, adj. "other": katrs, adj. "each", Cf. quoteros (ioteros)
```


## [2026-09-07T17:37:21.455Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in range(834,840):\n    print('=========== leaf',i)\n    print(t[i][:2500])\nEOF",
 "description": "Print IEC leaves around p.1643"
}
```


### [2026-09-07T17:37:22.711Z] TOOL RESULT

```
858
=========== leaf 834
) joy’; OE wynn, f. ‘delight’; cf. wyn-sum ‘winsome’. (FK:EWDS untenable: Wonne). See next
1515
uénskKó ‘desire’. Cf. uenos, -es-, and uén- (1). WP I, 259 Skt. vafncami, v. id.; Du. wenschen, mod. wensen, v. id.; wens, m. id.; (zero-gde in G wünschen)
uenter- (uentor-) (uemster-?) *wickerwork, basket" (?); ‘bag, net? (?) Av. cf. vafita, f. ‘wicker’; Lat. venter, gs: ven- tris, m. (abdomen, stomach, womb'. Fig. sense of *bread-basket (?), cf. pàn-tex ‘paunch’, if a cpd. of panis "bread", and cf. E. dial. breadbasket = *'abdomen); Li. vénteris, gs: vénterio, m. *bownet, fishtrap', Latv. ven- teris ( fish-trap, fish-basket' or '-pot"); but cf. also Icel. vinstur, pl. vinstrar, f. “fourth stom- ach of ruminant'. See Supt: U: uemstr-
uéntos (*uéntos) ‘blow, blowing, wind, gust’. WP I, 220. Cf. ueio (“uëið) Tokh. want, wànt, B yente (sic), id.; Hitt. huwantas, pl. huwantes, id.; Lat. ventus, gs: 4, m. ‘wind, storm’; Ir. (?) fead, mf. whistle’, only if for *féad); W gwynt, pl. -oedd, m. *wind'; Br. gwent, m. id.; Cor. gwyns, pl. -ow, m. id.; OHG wint, i-st. & o-st. m. id.; OE, Du. wind, m. id.; OE winde, adj. ‘windy’; ON vindr, m. “wind, air”
uequó (uequmi, uiuéqumi) “call, say, speak, ask’. Cf. uoóqu-. WP I, 245 Skt. vátmi, vakmi, vívakmi, 2, 3s: vaksi, vakti, *say, speak, tell, name, call, announce, des- cribe, reproach’; pp: uktáh, inf: váktum; Av. vað-, v. ‘talk’; Per. güvam, inf: guftan, v. ‘say’; Tokh. B wek-, v. ‘say, speak’; Arm. (?) goéem, v. Cer, if to Skt. vivaksami ‘wish to say"); Gk. eípo, v. ‘say’; Olr. cf. in-fét, 3s. ‘tells’; pf: in-féccid (sic) “he told’; OCz. vece Che said”: inf: vecéti); OPr. wack-, v. ‘cal? (de- nom.?). Nominal types: Skt. vacas, n. “speech, word"; Av. vačō, obl. vacáh-, n. id.; Gk. épos, gs: -eos, n. id.; Hitt. cf. wekuwar, n. ‘request’; Arm. (?) gov, s. ‘praise’; OR. cf. véCe, n. ‘coun- cil, commons'. Extn. of type *uequtis beside *uoqutis, *uqutis in Skt. vaktih, f. “speech; Av. cf. uxtis, z-gde, f. 'expression'; Arm. cf. (?) goCiwn, s. 'shout' (but Iran. LW in Arm. uxt, Lët vow); Cz. (?) od-vet, mf. ‘retaliation’; o-veta, id. (Gmc. LW?)
uequtió cf. uequó
uénsKó — uerbos, -es- (uorb-, urb-); uerbà
10
15
20
25
30
35
40
45
1516
Alb. cf. p-ves & pyes, aor: p-veta, pyeta, v. (ask', fr. apo-°); Ir. cf. fachtaim, v. id.
uer- (1) (uero, io, uro, ið) open, close’. WP I, 280 Skt. várami, v. pp: vrtab, id.; Av. var-, v. ‘cover; Lat. cf. ambig. ap-erio, erte, v. ‘open’; cop- erio, -erire, v. ‘close, cover, hide’; Li. veriü, vérti, v. 
=========== leaf 835
ņemt, v. ‘take heed’;
uer- (3) (uero, ið) ‘speak’. Cf. ueru-, uoru-. WP I, 283 Hitt. weriyami, v. “call, invite’; Gk. eíro, v. “say, speak, tell; éromai, v. "ask
uer- (4) (?) *up, upon' Per. bar, adv. & prp. id.; Arm. ger, cpds: gera-, id.; Lat. (?) cf. the hapax: verones plum- bei ‘sheets of lead”
uër- (1) ‘charm, favour”, etc.; (2) ‘true, right", etc. See ueros (1) & (2)
uerbos, -es- (uorb-, urb-); uerba ‘stick, withy’ Lat. verber, gs: verberis, n. ‘stick, lash’; OE (o-gde) wearp, n. ‘twig, osier’; OCS (and com. Sl.) vrüba, f. ‘withy, willow’; Li. verbà ‘sallow, palm-spray'; (z-gde in) vifbas, m. ‘twig, stick".
1517
See next
uerbo (uorb-, urb-) ‘twist, lash, fling’. WP I, 275. Cf. uerbos above and cf. urb- as a sepa- rate entry OHG wérfan, wérphan sv. 3. ‘throw’; OE weor- pan, Du. werpen, ON verpa, v. id.; Sw. várpa, v. “lay — eggs’; Li. (z-gde) virbu, eti, v. ‘move, twist, tremble’; cf. also OE weorp, n. ‘dash; castings, rubbish?
uerbhos, à  'farm-animal'. uer- (2) and -bhos Olr. ferb, f. ‘cow’; Ir. fearbh, f. ‘doe, deer, cow"; OE weorf, n. *farm-animal, beast of burden’
ueredh- (uerdh-) 'seethe, boil, stir, rouse, rile, anger Gk. erétho, erethízo, v. ‘rile’; OCS vrézdo, vréditi, v. “harm, injure’; vréZdajo, -ati, v. id.; vrédü, m. ‘wound, sore, harm’; R veredit, v. “Tile? beside vèred, m. ‘boil, abscess’; Ukr. cf. veredlivyj ‘harmful’; Cz. cf. vřed, Pol. wrodek, m. ‘boil, sore; MHG wirt, m. ‘eddy in seg’. (But for Go. fra-wardjan; OE for-wierdan 'des- troy’; OHG *wartjan, werten ‘harm’, see uert-; uort-, in view of Go. fra-wairpan ‘perish’, etc. Li. cf. vérdu, inf. virti, Latv. verdu, virt, v. “boil” where -d- occurs only in the pres. t.)
(uereiKa ‘heather’, see uroiK-)
uereio “look, watch, observe, care for’. Cf. uer- (2) and WP I, 284 Tokh. wár-, B war-, v. ‘sense, feel’; Lat. vereor, vereri “regard, revere'; Srb. verem se, verati se, v. ‘keep watch: Latv. cf. veros, vérties, v. “look, watch’; Gk. (z-gde) cf. eüron “have found' Cf. uor- (2)
(uereios, à, see uer- (1))
uergho, io (1) “annoy, plague, torture’. Cf. uorgh- Skt. cf. upa-valhami, v. & válhe, mp. ‘quizz’; Ir. feargaim, v. "be angry” (here?); MHG wér- gen, sv. 3. ‘strangle’ beside (o-gde) wergen, wv. ('téar', fr. *uorghejo); Li. vérgiu, ti, v. *en- slave’. Nominal types: Ir. fearg, f. (anger. Here?); Li. vérgas, m., vérge, f. ‘slave’; Latv. vérgs, m. id.
uergho (2) (?) ‘come, go’ Gk. érkhomai, v. ‘come’; Lat. (?) vergo, ére, v. ‘incline’
uergo, io (1) “tie, twist, squeeze, strain,
Cf. uereio,
=========== leaf 836
‘work’; (denom. in) OHG wérkon, w&rchon, v. "work do’; Swiss werchen, id.; Du. werken, id.; OE weorcan, id. beside (z-gde) wyrcan, id.; ON verka, v. ‘work’; Alb. virdhem, v. ‘gain a skill, win sympathy’, mp. fr. *uergemoi or sim.. Nomi- nal types: Pahl. varz, s. “practice, work? (Per. id. fr. Pahl.); cf. also Per. barz-gar, s. 'farm-labou- rer’; Arm. (e- or o-gde), o-st. "work act, fact’; Myc. we(r)k-, cpds. *draught-, work": cf. were- kara- (“tooP or sim.); Gk. érgon, n. "work op- eration, deed, act, necessity; MIr. ferg, f. (battle; fury; warrior, but cons. ambig. Cf. uerg-, uergh-, etc.); Ir. fearg, f. (anger, am- big.); OBr. guerg, adj. ‘effective’; OHG wérk, wérch, n. ‘work, deed’; Du. werk, id.; OE weorc, n. id.; ON verk, n. id. cf. virki, n. id. (and ‘stronghold’, mod. Icel. *saddleframe"); ON cf. also virkr, adj. ^working-; mod. ver- kur, pl. verkir, m. ‘pain’; Sw. värk, m. id.; värka, f. ‘hurt
uerĝh-, alternative to uerĝ- (1), q.v. (Balto- Slav. ambig.). Cf. uergho (1) ON virgill, m. ‘halter; MHG wergel, m. (Cstrangler, fr. *uorghil-); Blg. vrěž, vrěža, f. ‘tendril’; Li. verzle, f. 'screw-nut'; verZe- klis, m. id.; Latv. verzeles, pl. ‘trappings’; Finn. LW verkko ‘net, web’. (Isophones:
1519
MHG wérc, n. ‘tow’; Latv. verzes, pl. ‘bog- myrtle’)
uerĝh-, uergh-, see Supt: U and uerghō (2)
uëriiom ‘grave’. Evidence ambig. Cf. uermn- (2) and uer- (2) Gk. éríon, n. id.; Alb. vorr, T. varr, m. id.
uérinos ‘true, loyal, just. Cf. uëros (2) Mir. firen, adj. “just, fair; Ir. firian, id.; W gwirin, id.; OCS and com. Sl. vérínü, adj. *loyal
(uerió “open, shut”, see uer- (1) and WP I, 280)
uério 'verify, authenticate, aver'. Cf. uéros (2) Ir. fíoraim, v. ‘come true; W (denom.) gwirio, inf. ‘authenticate’; Go. cf. tuz-werjan, v. (doubt, fr. *dus-^); OCS vérjo, věriti and com. SI. “believe?
uerkio (uerksKo) ‘squeal, cry, utter, say” Skt. valkayami, v. ‘speak’; valkah, m. ‘speaker’; OCS cf. vrëëto -ati, v. (cry, squeal, fr. *uerks- ko); Cz. vfiskat & vřeštět “cry, whimper’; Ukr. verescaty, inf. ‘scream’; Li. verk, verkti, v. ‘cry’; cf. verk3nà, mf. *crybaby'
uerks- (urKs-) (1) ‘young animal". Cf. WP I, 269 & 278. Cf. uers- (2), uersén- Skt. cf. (z-gde) vr$ah beside vrsah, m. “small animal’; cf. vr$Cikah, m. ‘scorpion’; Li. vetsSis, gs: -io, m. ‘calf’; Latv. vērsis, m. "ox
uerks- (2) ‘top’. Cf. urks- (4). WP I, 267 Skt. cf. várgman, n. id.; W cf. gwerchyr, pl. iau, m. ‘lid’; Ir. cf. feirc, pl. -eanna, f. “peak, bulge'
uermis (uorm-, urm-) 'twisting creature, worm,
=========== leaf 837
nus ‘barrier’; Br. gwern, pl. -iu, f. 'ship's mast’; W gwernen, pl. gwerni, f. id.; Cor. gwern, pl. gwernow, f. id.; ON vorn, f. beside vernd, f. ‘defence’; Sw. värn, n. id.; Finn. (LW) varras, s. ‘spit, pole, shaft
uern- (1), see uermn- (2)
uern- (2) (uernà, is, ios) ‘withy, shoot, suck- er; alder. WP I, 292 Gk. érnos, n. ‘young plant, sucker, shoot’; Alb. verr, m. “alder, white poplar’; Gaul. verna, f. ‘alder; LW in Fr. verne, vergne, id.; Ir. fearn, gs: -a, m. ‘alder’; Br. gwern, pl. gwer- nennu, m. id.; W gwern, coll. id.; Cor. gwern, id.
ueró, ueros, see uer- (1)
(uerógh-, see Supt: U)
uéros, à (1) ‘goodwill, grace, charm, favour, fortune' Skt. varah, m. “treasure”; -varah, cpds.; Av. vàro, m. ‘will, goodwill, gift, grace’; Hom. Gk. ēra, acc. sg. id.; Lat. cf. (?) se-vérus ‘harsh, exacting’; Go. cf. un-wéerei, f. ‘reluctance’; OHG cf. ala-wari, mite-wari, adj. ‘amicable, favourable’; ON vert, adj. ‘snug, peaceful. (Isophonic: Latv. veris ‘deciduous forest; vera, adv. “into notice, prominently’: OE wär, adj.)
uéros, ios (2) “true, right, proper. WP I, 268 Lat. verus, id.; MIr. fir, Ir. fior, id.; Br. W gwir, Cor. gwyr, id.; OBr. guir, id.; OHG war, wāri, id. beside wara, f. (truth, loyalty’: Sl. véra); MHG were, adj. ‘true, loyal’; OCS (and com. Sl.) věra, f. (faith: OHG wara)
uéros (3) ‘watchful; watch" OE waer, adj. *watchful'; Latv. cf. vera, adv. ‘into notice’; cf. MHG o-gde ge-war, adj. *aware'; f. “awareness”
1521
(uerpó, see Supt: U and cf. urpo (2), urpol-; uerpos, à, see uorp- (2))
uers- (1) ‘droplet, sprinkling, shower, dew, rain’. WP I, 269. Cf. uersó (1) Skt. varsáh, -Á, Am. mfn. “rain, shower’; Av. cf. varo&-, v. ‘sprinkle’; Per. baris “rain”; Hitt. warsas (queried), id.; Gk. hérse, hérsé, f. (1) ‘dew’; Olr. cf. feraim, v. ‘pour, rain? beside Mir, fear-thuinn, Ir. fearthain, vbl. n. f. ‘raining’ (vocalism obscure in Olr. fross, f. “shower, downpour’, fr. *urost-?); Li. cf. versmas, m. ‘eruption’; versme, f. ‘spring, source’
uers- (2) ‘young of animal’. Cf. uerks- and uersën-. WP I, 269. (Skt. urs-) Skt. cf. (z-gde) vrsah, m. ‘young male, esp. bullock’; Gk. hérse, hérse, f. (2) “young ani- mal, lamb”; cf. also (?) Hes. errás, usu. érraos, m. (cram, wild boar’. A synthetic cpd.?); Lat. verres, gs: verris, m. ‘boar’; Li. cf. versis, gs: -io, m. ‘calf’; Latv. versis & véersens, m. “ox; Finn. LW varsa (ffoal, fr. Iranian — Joki)
uers- (3) 'growth, hard skin' Lat. cf. verr-üca, f. ‘wart; hillock’; OE wearr, m. *callouse'; OFris. cf. (?) wersene 
=========== leaf 838
ag’; Lat. verro, ére, OLat. vorro ('drag, trail; sweep, brush”,
uerpo — uertos
15
20
25
30
35
40
45
1522
but a type *uris- is possible for verro in the sense of 'sweep^); Latv. cf. (?) verSuü, vērst, v. ‘direct’; vērsties, refl. ‘go, wend’; cf. ver- stuve, f. ‘plowtail’. See next
uerstis (urst-) ‘turn’. Cf. uert-, uort-, urt- and extns. Av. varstis, f., varstvom, n. ‘deed’; OW gwers, f. ‘while’; R cf. izobrësti, inf. 'invent'; z-gde in Skt. vrttib, f. ‘course, mode’; OCS vrüstí & vrüsta, f. 'age'; Croat vrst, f. “kind, sort; R verstà, f. (about a km.); Li. versti, inf. ‘to turn’
uertenos, ā, is ‘turn, roll, roller, axle-tree, cart’. Cf. uerto. WP I, 274 Skt. vartaníh, f. ‘felloe of wheel’; Oss. wär- don, pl. wärdättä, s. Ceart LW in Romani vardon, id.); Per. vardāne, s. ‘rolling-pin’; (z- gde in) Gk. rhatánē, f. (/stirring-stick'. fr. *ur- tona); Lat. cf. Vertumnus, m. ‘god of change: LLat. vertumnum, n. *ironwort, heliotrope'; OCS (and com. Sl.) vréteno, n. ‘spindle’; LW in Finn. värttinä, id.
uertitos, à, io, cf. uertó, etc. Skt. vartitah, adj. ‘turned, revolved'; OBr. guirtitou, pl. ‘spindles’; Br. gwerzid, pl. -i, f. id. (and *banister); W gwerthyd, pl. -au, f. ‘spindle, axis’; Cor. gwerthys, pl. gwerthyjow, f. id.; Go. cf. and-waírpis, adv. “at, against". A type *uertis arises in Arm. geh, i-st. (ditch, depression": Ir. feirt (and feart), m. (2) ‘trench, tomb")
uertó, io (urtið) ‘turn’. WP I, 274. Cf. uer- (1) and extns. of uert-; o-gde uort-, and z-gde urt- Skt. vártami, várte, v. ‘turn’; OLat. vorto, Lat. verto, ére, v. id.; cf. also (?) op-ortet (“is neces- sary’, if fr. *op-uert-, -uort-); Umb. cf. vurtus, 2s. ‘shalt turn’; Go. waírpan, sv. 3. “become, happen’; OHG wérdan; OE weorpan; ON ver- ða, sv. id.; (z-gde in) OCS (and com. SI.) vrüsto, vrütéti, v. ‘turn’; Li. verciü, vefsti, v. ‘turn, roll, convert, translate’ beside vertaju, Eti, v. troll
uertos, is (1) ‘turn’. Cf. uerstis, uertitos (uer- tis) and uerten-. Radical: uert- (uort-, urt-) Skt. vartih, f. ‘roll; wick; rim; streak’; vartis, n. ‘circuit’; Icel. cf. verður, pl. -ir, m. ‘meal’
uertos (2) *worth; value
1523
Lat. cf. op-ortet (“it is necessary’, if fr. *op- uert-, but cf. uerto for a possible alternative of sense); Ir. feart, m. ‘worth, power’; W. Cor. gwerth, mf. “value, price, sale’; Br. gwerz, f. ‘sale’; Go. waírps, adj. ‘worth’; OHG wérd, adj. & s. n. id.; MHG wért, gs: wérdes, sm. & n. “price, value’; adj. ‘worth’; OE weorp, n. id.; ON verð, n. id. (and ‘price’); Li. veř- tas, a
=========== leaf 839
a dike’; G Werd, m. “island, coastal strip’; Ukr. vereta, f. ‘blanket. (Go. wairdus, G Wirt, m. “host, entertainer’, fr. *uer-tüs?, but *ues- "be, dwell" for Lat. verna, mf. “household slave). See next
uerut- (2) (?) ‘crowd, group, team’ Skt. cf. varütham, n. (2) 'swarm, crowd; Tokh. A wartsi, B wertsya, -tsyo, f. ‘crowd, retinue’; OE werod, n. (1) ‘team, band, troop’
ueru- (1) “din, confusion, strife'. Cf. uoru-. Verbal type (also): ‘utter, blab? Skt. cf. (*-e- or *-o-) varvarah, adj. (1) fstam- mering’; Gk. eréo, eró, v. “will speak’; éris, gs: éridos, f. ‘strife’; Lat. cf. verv-ex, -ecis, mf. ‘wether; ewe Ir. fearb, f. “ox, cow; doe; bel- lows’; cf. the cpd. in Gk. éri-phos, mf. (Ckid', lit. *bleater); Blg. vréva, f. ‘brawl, shouting, roar’; Srb. id. (and ‘crowd, swarm); Cz. vřava
uertulos (uertolos, uort-, urt-) — ues-
20
25
30
35
40
45
1524
‘brawl’; Slovak cf. (o-gde) vrava, f. ‘speech’; vravet, inf. ‘speak, say”; Li. verventi, inf. “bark, yap’; vervü, čti, v. (‘whine for, plead, beg; bark’: Hom. éromai, v. ask: Latv. cf. verve- leju, v. jabber’. Variant in Skt. brávimi, v. ‘say, speak’. WP I, 283. Cf. uoru-
ueru- (2) ‘tie, knot’. WP II, 499 Gk. cf. eíro, v. (1) ‘tie, knot, weave, knit; R cf. verévka, f. ‘string’; Latv. cf. vervelains, adj. ‘knotty — of wood Li. cf. vervente, f. ‘speedwell
ueru- (3) “of sheep; woolly; wool’. Same as Ø) (?) Hitt. warhwis, gs: -hwayas, adj. ‘shaggy’; Myc. we(r)wjo-, adj. ‘woollen’; Gk. eiros, eírion, érion, n. ‘wool’; eréa, f. id.; (Lat. ambiguously here, or to ueru- (1): vervex ‘wether; ewe")
ueru- (4) ‘furrow, groove, line’. Cf. uoruos (2) Lat. cf. verv-actum, n. ‘newly turned fallow’; Ir. fearb, f. (3) 'stripe, welt beside (o-gde) forba, m. 'glebe-land'. (Isophones: Skt. var- vah, m. or -am, n. ‘a coin’; varvih, adj. ‘glut- tonous'; Gk. erüo, v. ‘snatch’)
ues- (1) ‘put, place, give, offer, sell’. Cf. uosn-, uesnom. WP I, 311 Skt. (vowel ambig.) vasnám, n. ‘price, value’; Tokh. AB wäs-, B was-, v. ‘give’; Hitt. was-, 2s: wasti, v. 'buy' beside usniyami, id.; Per. cf. far-üSam, fir-ü$am, inf: -üxtan, v. ‘sell’; Lat. cf. venum dare, v. "sell" beside vendére, id.; Umb. cf. ues- ‘liberate’
ues- (2) ‘be, dwell’. WP I, 306 Skt. vásāmi, v. ‘dwelľ; Av. váhai(mi), v. ‘stay, dwell’; Per. bāšīdan, inf. ‘dwell, be’; Tokh. B wäs-, wsask-, v. “lie, rest, be'; Oss. win, wn, Dig. un, inf. ‘be’; Arm. cf. gom, v. "Tam": geri, s. & adj. ‘slave; enslaved’; Hitt. (?) hwes- (mi), v. dive; Gk. cf. á-esa núkta, v. “have spent the night'; Lat
```


## [2026-09-07T17:37:42.503Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nleaves=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\n# find leaves containing standalone numbers 1640-1650\nfor i,l in enumerate(leaves):\n    for n in re.findall(r'(?m)^\\s*(1[56]\\d\\d)\\s*$',l):\n        if 1630<=int(n)<=1660:\n            print(i,n)\nprint('---- last leaves numbers ----')\nfor i in range(840,858):\n    nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$',leaves[i])\n    print(i,nums[:6], leaves[i][:80].replace('\\n',' '))\nEOF",
 "description": "Locate IEC printed page numbers"
}
```


### [2026-09-07T17:37:43.849Z] TOOL RESULT

```
---- last leaves numbers ----
840 ['1526', '1527'] , wasami, wasiyami, wasemi, v. ‘put on — clothes’; Gk. Ion. heimai, 2s: héssai, 
841 ['1528', '1529']  id. cf. Li. ve-du, id. ues- (2) “breath, air, breeze, cool, fragrance’. WP I, 2
842 ['1530']  Cf. ues- (2). WP I, 222 Skt. vasanam, n. ‘fumigation, scenting'; Gk. cf. á-ëma,
843 ['1531', '1532'] r-old, annual; yearling'. Cf. uetos. WP I, 251 Skt. vatsáh, m. ‘calf, young anim
844 ['1533', '1534'] ‘crossbar, bail’ beside LLat. vibra, id.; W gwif, pl. -ion, m. "lever, bar; LG w
845 ['1535']  v. “become visible’. Cf. type *uidoi! in Gk. idoú! ‘behold’ and OCz. vedé! id.;
846 ['1536', '1537'] ow in middie of elephants forehead’; Li. vidüs, m. ‘middle; room, cham- ` ber”; 
847 ['1538', '1539'] ��: Latv. videnis *torso, rump' and Li. Latv. vidus, m. *middle) uig-, uigl- (1)
848 ['1540', '1541'] f. *filigree-gold'; MHG wiere, f. id.; OE wir, m. ‘wire; filigree; creeper’; Du.
849 ['1542']  cf. am- usin, s. (spouse, fr. *som-uiKin-, cf. Lat. uxor, if fr. *uoiK-sor-); A
850 ['1543', '1544'] WP I, 259 & 577 Gk. mus, s: -ios, mf. ‘son, daughter’; Lat. cf. vin-dex, gs: -di
851 ['1545', '1546'] “man, husband, hero’. WP I, 314 Skt. viráh “man, hero’; Av. viro ‘man’; Tokh. A 
852 ['1547', '1548'] rul-entus ‘poisonous’. Cf. OE wode-wistle ‘hemlock’. (Isophonic: Mir fial ‘modes
853 ['1549', '1550'] - sure, acceptance'. Cf. uoit- (2) Skt. vitáh, adj. (2) id.; vitíb, f. ‘pleasure
854 ['1551'] Skt. vívakmi, v. ‘say, speak, tell beside vávak- mi, id.; (Hitt. wewakhi, v. see
855 ['1552', '1553'] Lat. liquor, gs: -óris, m. ‘fluid’; MIr. & Ir. fliuch *wet'; OBr. gulip & guilp,
856 ['1554'] bulga is ambig. Skt. várgā ‘sect, class’ seems to be unrelated) (ulio (1) ‘wind,
857 [] (1) only in Skt. ürnómi, v. ‘envelop’; (2) only in Gmc. cf. Go. wulan and OE wyl
```


## [2026-09-07T17:37:53.647Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"shoe\" IEC.txt | head -40",
 "description": "Grep IEC for shoe"
}
```


### [2026-09-07T17:37:53.696Z] TOOL RESULT

```
741:artüno, artáo, ham-artë; OLat. artus ‘close’; arte, adv.; cf. also ars, gs. artis ‘art’; artus, üs "ont beside artu, n. id.; Br. cf. arz-, px. (near beside eh-arz, id. (*eKs-art-); Li. artüs, arti (adj. adv. "close: ap-árte “shoe- string”
1539:bhosos, us, uos ‘bare’. WP II, 189 Arm. cf. bok (‘barefoot’, fr. *bhosukos, cf. Cz. bosky, adv. id.); MHG barer, barwer “bare” beside er-barwen, -berwen (“lay bare”, cf. also OE barian, id. and Cz. bosit *'unshoe"); OE bær; OCS bosü ‘barefoot’; R cf. bosvà “bare sole’; Li básas, Latv. bass ‘barefoot’
3616:Alb. mbath “put on shoes; OE in-feccan *fetch in'
3773:Lat. cf. ex-uviae ‘spoils’; OCS cf. ob-uví “foot- wear'; Li. cf. áp-avas, id.; Latv. apavi, mpl. id. euuó, ið (euo, euno) ‘put on garment, shoes; wear Lat. md. ex-uo, -uére; OCS ob-ujo, -uti, freq. -uvajo ‘put on footwear’; iz-ujo etc. ‘take off (shoes); Li. cf. aunü, aŭti, pf. aviaü ‘put on shoes’; aviù, -êti “have on (shoes); Latv. aunu, aut (as Lith.)
3805:ononti-, see enonti (en, eni, anti, ono, onti) Gk. cf. ánanta ‘uphill’, anántes, adj. id.; OCS onosta ‘shoe, sock’; Cz. onuce, pl. *puttees'
4223:(golg-, see gelg-. O-gde in OCS *glazü “eye” in glaz-atü ‘eyed’; R glaz, pl. glazà, id. The sense of Cypriot Gólgoi ‘temple of Cupid and Venus’ is not clear. Isophonic: Sw. kälke “iron shoe, glide")
6899:titi, Cz. kutit “fashion, contrive’; Cz. cf. po- kuta (‘penalty’: Ukr. = 'penance"); Srb. cf. kucam ‘hit’; Li. cf. káustyti ‘forge, shoe a horse’
7462:knouos, ios 'pinching, tight; pinch, con- straint, strait’ Gk. knóos, knoŭs (mng. uncertain: ‘creak of shoes??); cf. kno- in certain synthetic cpds: knódàx ((cotter' or “linchpin': odàx “bite?); knodon, gs -dontos (‘two-pronged imple- ment; cotter, U-bearing; sabre: odoús 'tooth"); Hes. knóos (‘total silence’: oüs “ear”); knóps (*blind': ops); OE hnēaw, adj. ‘stingy, close-fisted; MHG nouwe “close, narrow, tight'; Du. nauw, Fris. nau, id.; cf. G ge-nau; ON hnóggr, ob. hnóggva- ‘stingy’; e-gde in OE hneowan (alleged) ‘pinch’; MHG niuwen beside nüwen, id.
7590:koltos ((1) ambig. cf. kalt- (2)) ‘club, stump’ Skt. katah (3) ‘corpse’; Cz. klát ‘log’; Slovak klát ‘stump, hive’; Li. cf. káltas — infl. of *kal-/ kol- ‘strike’? — ‘chisel, graver’; Latv. kalts ‘chisel; crowbar’, cf. kalatas , fpl. 'shoemaker's last’
7978:kroiuos (2) ‘case, body, enclosure’. Cf. WP I1, 577 W cru, m. ‘hollow bulge, rotundity’; OS hrêo, gs hrëwes n. ‘corpse’; MHG rē, gs rēwes (1) ‘corpse’; OE hræw, hràw, m. n. ‘body, corpse’; OCS črěvň, m. & črěvo, gs -ese, n. ‘womb, beliy’; črěvij, m. (shoe, adjectival form of črěvo); Cz. střevo "eut
8112:krpiios (krpios, io, krpitio) 'foot-wrapping, clout, shoe’. WP I, 425. (Loanword movement had distorted some of the expected phono- logy) (1) cf. Gk. karpaía (a Thessalonian dance); krēpís (shoe'. LW in Lat. crepida “sandal”, via Etrusc.); LLat. carpia lint? beside *scarpa in It. ‘shoe’; LW in W carp, pl. iau, m. ‘clout, rag’; Ir. cf. caire-amh, m. ‘shoemaker’; Br. céré- ur, id.; W crydd, pl. ion, m. id.; Cor. cf. kerija, v. “mend shoes’; OCS krüpa “cloth, textile’; Srb. Slovene, Blg. krpa, krápa, kárpa ‘rag’ beside Blg. krăpka ‘patch’ and Srb. ktplje, fpl., Slovene: kfplja, f. and Cz. krpě ‘snow- shoe’; R kórpija "Int" (2) For the extn. in *krpitio cf. Skt. karpatam (o-gde: ‘rag’) (LW in Gk. kárpasos, f. “linen, hemp’; cf. karpátinai ‘rawhide shoes? beside karbátinai); Alb. LW in këpucë ‘shoe’; various LW forms in Lat. carpisculum *kind of snow- shoe’; LLat. carpasia ‘shoe’; Sard. crappitta, f. (Cshoe', via Etrusc.? since Gk. -d- repre- sented by -tt-); MIr. ceirt, f. ‘rag? beside es- cart ('tow', fr. *peds-karpt- or sim.); W carth, pl ion, m. ‘hemp, tow, oakum'; Cz. krpec *bast- or hide-shoe"; Pol. kierpce f. id.; Slovene krpica ‘rag’. A ^wanderword' of uncertain pro- venance, w. variant vocalism in the radical (*krp-: *korp- or *karp-). A further variant vo- calism is indicated in Li. kurpe ‘slipper’; Latv. kurpe ‘shoe’ beside karpà *offcut of cloth’; Sw. harva ‘shred, strand’; LW fr. Li. in Pol. kurp 'bast-shoe'. Cz. kfáp ‘slipper’ indicates a nasal infix.
8598:Káuos, Káuio (2) Arm. (?) sawl (shoe'. Semantics of Cz. stfevic ‘shoe’: střevo "eut: Myc. cf. kowiro- (part of atrade-name); Gk. koilos, adj. ‘hollow’; koilía, f. id.; W caul, pl. ceulion, m. ((1) ‘maw’. In sense of ‘rennet’, a LW from Lat. coagulum); Cor. cowl, pl. -ow, m. ‘maw; fishgut'. (Br. koelé 'rennef' fr. Lat.)
10141:ladle, spoon'. WP II, 414 & 711 Illyr. (alleged) Loügeon (name of a marsh); Alb. lug, pl. lugje, m. “channel, groove, hol- low; lugë, f. *spoon'; Gaul. cf. Lug-dunum (placename); Ir. log, m. ‘hollow, ditch’; cf. luigín, m. dim. id.; OHG lobh, n. “hole? be- side lucka, f. ‘gap’; Sw. lucka, f. ‘trapdoor’; (long-gde in) ON lúka ‘hollow of the hand’; OCS lüza, f. (channel, canal, fr. *lugio), cf. also lúZica ‘spoon’; R cf. 10Z-ka, f. ‘spoon’; beside R (and com. Sl.) lyZa "ek and Pol. tyzwa ‘ski; punt’; Li. lügë ‘skate’; Latv. luge ‘snowshoe’ beside Li. lúgas ‘marsh’ and liugas ‘puddle, mire’
11604:neksos, us (1) “bond, tie’. Cf. nekstos, naskos & neKsos. Variant: nesk- Tokh. (?) nasu ‘friend’; Lat. nexus, gs: -üs, m. ‘tie, band, bale’; Ir. neasc, m. id. (beside nasc ‘collar’: Br. nask); W nais, pl. neisiau, m. id. beside naith, pl. neithion, m. ((2) “betrothal, fr. *nekt- or *nekst-); G. cf. Nistel, f. 'band- age; buckle-beit; lace; shoestring’ (beside Nestel, id. fr. *nast- or *nakst-); ON nist, nisti, n. "brooch: pin” beside nezla, f. (“button- hole”, i. e. *netsla! perh. fr. *nakstila). (Fr. nasse *fish-basket! is a LW, perh. Gallo-Lat.). Cf. Av. nasko, m. ‘chapter, section’
11606:nekstos (nektos), variants of type neksos (1) above. Cf. neKs- Lat. cf. necto, Ere, pf. nexi, sup. nexum “join; knit; spin; frame’; W nais, pl. neisiau, m. (band, De fr. *nektios) beside naith, pl. nei- thion m. ((2) *betrothal, fr. *nektis); OE cf. nestan, v. (^spin'. Phonol. uncertain); ON nist, nisti, n. "brooch, pin’; cf. G Nistel, f. "band. age, belt, shoestring'. (For the variant Nestel, Du. nestel, see nast-. W ambig.)
12388:oudh- (3) ‘shoe’. Cf. oudh- (2) (?)
12389:Gk. (Phrygian) oudon, gs: -ónos, m. “felt shoe; Arm. awd, Let ‘shoe’; cf. Lat. odo, üdo, m. (/shoe'. LW via Gk.)
12407:outós ‘woven; weave, textile, wrapping’. Cf. ouuo. WP I, 109 Skt. autáh, ótah, pp. & adj. *woven'; cf. ótuh, m. *woof'; otum, inf. 'to weave'; Lat. cf. ex- utum, ind-ütum, sup. ‘taken off, put on’; OCS cf. obusta, f. (footwear, fr. *-outio); on-usta, f. Cputtee', fr. San R cf. ob-à€, inf., Cz. ob-out ‘put on — shoes’; R onüéa, Cz. onuce ‘puttee’; cf. also OCS usmü ‘dress’; Li. aütas, m. *foot-wrapping'; Latv. auts, pl. auti, m. id. (and pl. *puttees")
12408:outrom (oudhlom, io) ‘footwear. Cf. ouuo, oufós, ousm- Av. aothrom, n. ‘shoe’; Arm. cf. awd, Let id.; SWG cf. óden, v. “tap, heel — shoes; Ódt, f. *heeltap'; Li. aükle, f. “legging, puttee'; Latv. aukla, f. ‘string
12409:ouuo (ouo, ið) ‘bind, tie, weave, wrap, swathe'. Cf. outós, ousm-, outrom Lat. cf. ind-, ex-uo, -uére don: doff; odo, udo (shoe: Arm. awd, Get id.); ómen-tum, n. (*caul, membrane’. See ousm-); Umb. cf. an- ouihimu, v. imperat. “let us get dressed; OCS Ob-, iz-ujo, -uti, v. ‘put on, take off — shoes’; Li. aunu, inf. auti, id.; Latv. aunu, aut, id.; Cf. also Cz. obuv, f. i-st. footwear
12575:pedol-, pedul- ‘fetter, bond, thong’. Cf. ped-, péd- and pod-. (Var. pedil-) Hitt. petulas, petuliyas ‘noose, loop’; Gk. (variant) pedilon ‘shoe, sandal, fetter, fetlock'; Lat. cf. pedülis, adj. 'foot-; MIr. íall, Ir. iall, gs: éille, f. (thong, fr. *pedla); OHG fezzil, m. (G Fessel, f. ‘fetter, shackle’); OE fetel, m. ‘belt; ME fetel, s. ‘strap’; ON fetill, pl: fetlar, m. ‘strap, thong’ (all Gmc. forms from *podil-); cf. also EME to fettle, v. ‘tackle — a job’; Li. pëdulas, adj. ‘flat-footed, broad- footed'
12576:pedor- “fix, establish, build; footing, basis, base Skt. padrab, m. “village, community, land, ground’; Oss. (formally) fádil postp. ‘after’; Gk. pedairo, v. ‘raise’; OHG fezaron, v. ‘fetter’; O Fris. fiteria, v. id.; OE feterian, id. beside fiter-sticca *tentpeg'; Du. cf. veter, m. (^shoe- lace’: E fetter); ON fjoturr, m. id.; Sw. fjátter, m. id.
13701:prt- (3) (prtos, om, io) “piece, patch" Per. pül, s. ‘money’; Gk. prasía, f. 'garden- plot; Lat. pratum, n. ‘meadow’; OCS prütü, m. ‘rag’; OR port, m. ‘garment’; Slovene prt, m. ‘sheet’; Lusat. cf. porémo, n. ‘lap of coat’; R cf. portnój ‘tailor’; Cz. cf. prták, m. ‘cobbler’; prtati, inf. ‘mend — shoes’. (Skt. patih, f. “strip of cloth’, hence E ‘puttee’, is ambig. cf. pelt-)
15210:ter”; OE sinc, n. ('treasure', lit. “holding, pos- session"); Icel. sinka, f. ('avarice', lit. 'posses- siveness"); cf. sinkill, pl. sinklar, m. ‘clamp’; OCS po-sego, -sesti, v. ‘touch’ beside segati, segnoti, inf. “reach, grasp’ (and com. SI.). No- minal types also in Skt. sangah, m. ‘hitch, catch; association’; Per. hang (*wisdom, lit. *grasp); Cz. sáh, m. ‘fathom; cord; faggot’; Pol. siag, m. id.; cf. also Cz. ob-sah ‘contents’; Ukr. cf. sjažení ‘fathom’; Sw. also sinka, v. (1) “fit, join, mend'; (o-gde): cf. G Senkel, s. (shoelace', fr. *songil-)
15418:siüið (siüuo) ‘sew’. WP II, 515. Cf. siü-dhlom, siüio, siütós and next Skt. sivyàmi, pp: syutáb, id.; Oss. xwin, Dig. xujun, pp: xud, id.; Gk. cf. kas-süo, v. (‘sew together, « *Kmt-. Here Ainsworth 1736: suo: *kassüo for katasuó?); cf. pisuggos (/shoe- maker’, fr. *ped-suuo-, with pi- for *pe- before *su-, cf. písures); Lat. suo, ére, id.; Go. siujan; OHG siuwen; OS siuwian; OE seowan & séo- wian; Sw. sy, id.; OCS (and com. Sl.) So, Siti, id.; Li. siüvu, siūti, id.; Latv. Sum, šūt, id.
15746:skoip- (sKoip-) ‘cut, crosscut; crosspiece, thwart’. Variant: sKoip-. WP II, 545. Cz. Stípat “cut, split, chop’; Pol. szczepac, id.; Li. skiepiü, - ti, v. ‘rip up, unsew'. Nominal types: Hes. skoipos, m. ‘rafter; ON skeifr, adj. ‘awry, oblique’; skeifa, f. ‘horseshoe’; OE cf. scaf-fot, adj. fsplayfooted'; Cz. Stép, m. “split; graft; Pol. szczep, m. id. beside szczepa, f. ‘lath’;
16027:skütor- “horror, shudder Av. cf. skutaro, m. ‘tormentor’; Arm. xrtnum, xrtčim, v. ‘shudder, start; MHG (Lower Rhen- ish) schüdern, v. id.; G schaudern, id.; ME schuderen, shoderen, v. ‘shudder’. Eng. forms ambig. cf. skudhros as a preferable alternative. (Isophones: Oss. Kütür, Kotür ‘shrub’; LLat. scutrum 'shoelace")
16029:skütos (1) ‘scraped, shaved, pared, dressed; shaving, paring, skin, pelt’. Cf. skuto (sku-, skun-) and WP II, 23 & 549 Oss. skud, adj. ‘tattered’; s. ‘rag’; Gk. skütos, eos, n. ‘hide’; Ir. scúth, scüith, m. ‘peel, flake, scale, rind, bark’; W cf. e-sgid, pl. -iau, f. (“shoe”, fr. *ped-sküt-); Li. skütas, dial. skütas, m. ‘shred, rag? beside skutà, f. ‘leather’; cf. skustuvas, m. ‘razor’; Latv. cf. skutenis, id.
16265:slibros (sliboros, slibrikos) ‘slippery, gliding, dragging, slimy; hanging, loose, free’. WP II, 393. Cf. slibó, slibnos, slubrikos Arm. cf. lpir$, adj. (lewd; impudent': Dan. slibrig, for com. Scand. sliprig, id.); Gk. librós, adj. ‘bright’; Ir. sliobar, adj. ‘pendant; udder; mire’; W Ilyfr, m. (2) ^wheel-drag, shoe’; OHG slëffar, adj. ‘slippery’; MHG cf. slipf, sliff, gs: sliffes, sm. “slip, fall; slipfec ‘slippery’, cf. E dial. slippy, id.; LG (in Ger.) Schlipper, m. ‘sour milk’; OE slipor, adj. ‘slippery, slimy, filthy’; E slipper “house-shoe; drag on wheel; Sw. cf. slipprig ‘slippery’; Hes. cf. o-librós, id.; OBr. libiriou, pl ‘sleds’; Cor. cf. levryth, m. ‘sweet milk’; adj. ‘sweet — of milk
16663:Arm. hoy, o-st. “soil, earth’; Gk. cf. hedólion, n. (seat, dwelling’, fr. *sed-soliio-; also = “bench, quarter-deck"); Lat. solum, n. ‘soil, ground, bottom, sole of foot; solium, n. “seat, throne: solea, f. ‘sole of foot’; cf. also solidus, adj. (/solid, full, entire’. Not as WH); OHG sala, f.; OE sæl, pl. salu, n. ‘hall’; sele, m. id. (and 'dwelling); ON salr, npl. salir, m. “room, floor, ball" beside sel, pl. -ja, n. ‘hut’; OS seli, Let. m. “room, house” beside selida, f. ‘dwelling’; Go. salipwa, f. id. (Lë *hostelry^); OE sælp, f. ‘dwelling’; (the source of OCS selitva *hostelry' and its vocalism un- explained); Blg. (*-0-) sal, pl. -ove, m. ‘raft; Li. salà, f. (2) “village”; cf. át-sala, f. *mud- fla? beside (*-0-) sáolas, m. ‘bench’; Latv. sols, m. id.; solis, s. ‘footstep’. (ON soit, m. ‘sole of shoe’ may be a LW)
16725:panion, tracker, track, procedure”. Cf. sequ- (1), soqu- (1), etc. Skt. sakkah, sakkih, m. ‘companion’; Av. haxa, nom. sg. m., pl: haxaya, id.; Ober haxa-, cpds. id.; Gk. ópson, n. 'food eaten 'cum pane"; cf. opúō and opüio, v. “marry” beside a-Ossæð, v. ‘help’; Lat. cf. socius, m. 'com- panion, ally; OS seg, i-st., OE secg, ON seggr, pl. -ir, m. ‘man, warrior’ (fr. *soquís); OCz. cf. sok, m. ‘rival’. Here also Av. haxo, m. ‘sole of foot’; Arm. ak, Let, leg’; Phryg. (DW?) sükhos, m. “sandal; Lat. (LCW?) soccus, gs: A. m. ‘shoe, sandal’
17518:*firm-'; OE stalu, f. (1) “bar, strut’; EME stale, s. (rung of ladder; mod. dial. “handle of broom’; cf. also OE stæl, m. ‘place’; steal, n. ‘framework’; OCS stolü, m. "base, throne"; R stol, Cz. stůl, m. ‘table’; (LW in) Hung. asztal, id.; Ukr. cf. po-stoly 'bast-shoes'; Latv. cf. pa-stala, f. *hide-shoe"; (LW in) Li. stalas ‘table’; OPr. cf. stalit, v. ‘stand’
17538:sthántio ‘standing’. Radical: sthà-, q. v. and cpds. EMAIb. shtansé, mod. shtáz8&, shtazë, f. ‘beast’; LLat. stantia, f. “place, situation’; (class. cpds: in-, con-?); Latv. stote, f. ‘fluke on horseshoe; seam; braid'; cf. (variant en- dings) MHG stant, gs: standes, sm. ‘status’; stande, wf. 'still-cask'
18137:suol- ‘tread, sole; threshold’. WP II, 532. (Variant: suel-) Arm. Kajl, Let ‘step, pace’; kalem, Kajlem, v. ‘march’; Lat. solea, f. ‘shoe, sandal’; OHG swelli, s. threshold; MHG schwelle, s & wf. ‘beam; threshold’; ON svalar, fpl. ‘balcony’; Sw. svale, wm. ‘entrance to cellar’. MHG swel,
20286:uiĝ- (1) “twist, bend; crooked, bent; strand, rush, withy, shred, bast, rope’ Ir. fighim, v. ‘weave’; Dog, s. (rush? — bot.); MHG wicken, v. (1) ‘wrap’; Sw. vicka (2) and vecka, v. ‘fold, pleat’; veck, n. ‘fold’; ME wik- ke, s. (*evi', whence E wicked); Li. vyžà, f. *bast-shoe'; dial. vyZas, m. id.; vyZtu, -ti, v. ‘twist — rope’; Latv. vize, f. &bast-shoe'. Extn.
```


## [2026-09-07T17:37:56.636Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nleaves=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in [410,411,412,413]:\n    nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$',leaves[i])\n    print(i,nums[:6], leaves[i][:100].replace('\\n',' '))\n# where does muk- appear (leaf index)\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\ni=t.find('mūkóo(n)')\nprint('leaf of mukoon:', t[:i].count('\\f'))\nEOF",
 "description": "Check IEC leaf numbering"
}
```


### [2026-09-07T17:37:57.892Z] TOOL RESULT

```
410 ['728', '129']  Slovene mákati, inf. ‘wet; dip; dive’; R makàt, inf. ‘dip’; Latv. cf. mākonis, mákulis *cloud'; (sh
411 ['730', '731'] �� mālos, om (3) “apple; cheek’. WP II, 296 Tokh. A mal- ‘cheek’; Gk. mëlon, Doric: -ã- (*apple'; pl
412 ['732'] ra- tion’. Cf. mana, mens, mëno(n), mon-, WP II, 233, and mànió above Skt. manah, m. (1) ‘jealousy, 
413 ['133', '734'] d.; OE mere, 133 m. id. (and “lake, pond"); ON marr, gs marar, m. id.; OCS morje, n. id. (and com. 8
leaf of mukoon: 857
```


## [2026-09-07T17:38:06.285Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nleaves=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nl=leaves[857]\nprint('len',len(l))\nnums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$',l)\nprint('nums sample',nums[:40], nums[-20:] if len(nums)>40 else '')\ni=l.find('mūkóo(n)')\nprint('idx',i)\nprint(l[max(0,i-4000):i+2500])\nEOF",
 "description": "Inspect IEC supplement leaf"
}
```


### [2026-09-07T17:38:07.696Z] TOOL RESULT

```
len 743
nums sample [] 
idx -1
(1) only in Skt. ürnómi, v. ‘envelop’; (2) only in Gmc. cf. Go. wulan and OE wylian 'seethe? beside wyllan, v. id. (fr. *ulnio)
ulquátis, os *tearer, devourer, killer’. Cf. ul- quos (1) Skt. vrkátih, m. ‘robber, murderer’; Slovene volkác ‘Alsatian dog’; Li. vilkátas, m. *wer- wolf; Late vilkatis, vilkacs, id.
ulquio ‘she-wolf’. Cf. ulquos (1) Skt. vrkih, id.; OE welt id. MHG (Upper Ger) wülpe, id.; ON ylgr, ds: ylgi, id.; Li. vilke, id.
ulquó, ið (ambiguous consonantism, unless related to type ulquos, etc. see next). Skt. varke, mp. ((seize', but cf. type *uelk-) beside vrkah (2) '(plough'; Srb. vučem, v. ‘drag’; cf. OCS (hapax) vlüci, s. (Ccaltrop? or sim.); Li. vilkiu, eti, v. ‘wear — a garment’; cf. vilktas, m. (tech. *priming); L
```


## [2026-09-07T17:38:17.898Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nlines=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\n')\nff=0\nfor n,l in enumerate(lines,1):\n    ff+=l.count('\\f')\n    if n in (11350,11364,11374):\n        print(n,'leaf',ff)\n# print surrounding lines of 11364 area for context of page numbers\nfor n in range(11340,11395):\n    s=lines[n-1]\n    print(n, s[:200])\nEOF",
 "description": "Find leaf of IEC muk entries"
}
```


### [2026-09-07T17:38:19.229Z] TOOL RESULT

```
11350 leaf 455
11364 leaf 456
11374 leaf 457
11340 45
11341  
11342 812
11343 cayed'
11344 mügh- (3) “dark; darkness. (Arm. & Gk. ambig. Cf. smugh-) Arm. (ambig. mujg "dark brown’; Gk. (ambig.) mukhós, pl. a m. “darkness; dark corner’; mükhios, adj. ‘inmost’; ON cf. mug- gu-veór (‘muggy wea
11345 mughis, io “fly, insect Kurd. moz fhorsefly' (*$h?); Alb. mizë, f. “fly; insect'; Lat. cf. mülio gs -onis, m. (2) 'gnat, fr. *muhlio-); MHG mügge, mücke, wf. ('fly'. Mod. G Mücke fr. Upper Ger.); OS m
11346 mughlio ‘grow mouldy’. Cf. mug- (1) and mugh- (2) and (3) Skt. (ambig.) muhirah ‘fool; mühyami, v. (be confused'. Prob. fr. *mudhlos q.v); Arm. mglim, v. ‘grow mouldy’; Ir. (ambig.) mogall, m. murk’. 
11347 mio, ið ‘howl, roar, bellow, murmur, mut- ter, grumble’. WP II, 310. Variant: müg- Skt. múj- radical form of müfijami, mójami, v. ‘din, resound’; Arm. cf. (variant) mgt'am, v. (fume, rage’, fr. *mugst
11348 muk- (mük-, munk-) ‘leave’. WP II, 254 Skt. mucámi, muficámi, pp: muktáh “leave, re- lease; Romani mukav, pp: muklo ‘leave, let, allow’; Av. muč- ‘let, release; Tokh. A muk-, mok-, B mauk., v. leave; 
11349 813
11350 ‘release, let fly’; mükno, -noti, v. tr. ‘remove’; intr. ‘pass, move’; R mču, mčať “carry off, remove’; -sa ‘escape’; Pol. mknac sie ‘flee’; Cz. cf. s-mekat, -meknout ‘remove — the haft’; Li. munkù, m
11351 mūk- (1) “grow dark, get filthy, become foul; foul, murky; foulness, murk?. (Variant: muk-. Gk. W forms ambig., cf. smug-) Skt. cf. mukah “smell of cowdung'; Gk. mükes, pl mükai, m. ‘fungus; Hes. míük
11352 mük- (3) (mükaio, eio) ‘clamp, shut fast, fasten, lock Skt. cf. mükah (*dumb', “lit. ‘tied, bound" — Mn-Wms.); Mir müchaim, v. (1) ‘squeeze, strangle’; Cz. za-mykat, inf. ‘lock; ode-mykat, inf. ‘unloc
11353 muklos (mukulos?) (1) *stammering, jabber- ing; stammer, gibberish; gibberer Gk. müklos, m. (2) ‘jackass’; Li. muklus (2) ‘stammering’; OCS cf. (?) pomüklt, f. (que- ried: ‘restraint? or 'silence). (S
11354 mük- — muksó
11355 15
11356 20
11357 29
11358 30
11359 39
11360 40
11361 45
11362 814
11363 muklos, us (2) ‘messy; mess, sludge, marsh, murk’. Cf. WP II, 253 Gk. müklos, m. (1) ‘smear; debauchee'; Li. mukluüs ‘miry, marshy, oozy’; Latv. mukls, id.
11364 mükóo(n) (mükró-) “pike, spike, peak, pile’. WP II, 311 Per. mūk ‘sting’; Hes. mükon ‘pile’; Lat. cf. (variant) mücro, gs -onis, m. (“point of sword". Cf. (?) Hes. mókron 'sharp); OE müha, müga, wm “p
11365 muks- (1) ‘snout; pig; grunt, murmur’. Cf. WP II, 310 Skt. mükbam, n. ‘snout, mouth’; Gk. Hes. cf. mukós “silent, soundless'; Ir. muc, f. ‘sow’; W moch, m., Br. mōch, m. coll. ‘pigs’; (Celt. LW in G M
11366 muks- (2) ‘worthless, rejected, ba? It. moscio ‘flabby’; Cor. mogh ‘fruitless’; OE cf. myscan, v. ‘injure, offend’; OCS cf. müselü "gotten gain’; Ukr. cf. (?) pry-mxy, pl. (^whims' but see next)
11367 muksa, io ‘fly, midge’. Cf. muksitio, musio, muska Lat. musca, id.; G Mucks, m. ‘midge’; OE mysci, pl. ‘flies’; OCS cf. müsica f. dim. ‘gnat’; R cf. mó$ka, f. dim. id. Cf. (?) Ukr. pry-mxy, pl. “whims
11368 muksità, iə “small fly, midge, insect. Cf. muksà, etc. (Variant mukst-) OE mohpe, mopbe, f. ‘moth’; Late MHG motte, f.; Du. mot, f. id.; OCS música ‘gnat, midge’; It. moschetta, id. (beside moschetto:
11369 mukso, ið (1) ‘thrust, plunge, insert, force’. Li. ambig. Cf. müK-, muKtis Arm. mxem, v. tr. id.; mux ‘tempered’ beside mxun, id., cf. also mxlCem, v. (plunge, thrust’, fr. *mukslitio or sim.); Ir. cf
11370 muksó (2) (?) Gk. cf. müxa 'snot; Lat. muccare, v. inf. ‘snort’; cf. also Gk. mukteér, s. ‘nostril’. (OCS
11371 815
11372 müselt or míseli, m. ‘substance’; Cz. o-mšelý 'tattered” suggest a prototype *miKs-l-, q. v.)
11373 müksos 'smoke' Arm. mux, gs mxo, ost, id.; cf. mxam, v. ‘smoke’; Ir. múch, f. ‘smoke; gloom’; cf. mú- chaim, v. (1) ‘suffocate’
11374 muktos ‘left, freed, abandoned, loose, dash- ing, rapid’. Cf. muk-. WP II, 254 Skt. muktáh, pp. ‘freed, loose’; Romani muklo ‘freed, allowed; It. cf. motta, f. ‘subsidence’ beside mucciare, v. ‘run aw
11375 (müktos, see mūk- (1) & (3))
11376 mük- ‘beat, thrash, strike’; muktis ‘fist, blow’. (Variant of type muks-, q. v.). Cf. WP IL, 255 Oss. mūs, Dig. mos 'threshing-floor'; Li. mü- Sis, gs -io, m., müsa, f. s. "Debt: cf. also Skt. mustib,
11377 mulio (1) ‘grind, crush'. Cf. mulos, mio (Arm. variant *mulo). WP II, 285 Arm. myem, v. “press, force? beside myum, id. (fr. *mulümi); Gk. müllo, v. ‘grind’; W (am- big.) cf. mwl, m. ‘chaff from thres
11378 mulio (2) ‘pout, mouth, keep mum’. Cf. mülom Arm. mlem, v. ‘pout; Gk. múllo (2) ‘grimace, mouth; cf. hai-mülos, -mülios (^wily; simper- ing, lit. ^wry-mouthed', fr. *uai-; Go. cf. faür-müuljan, v. ‘po
11379 mülió (3) "be crazed, be dumbfounded’. Cf. muülos R mlét, inf. "be dumbstruck'; Li. mulstu,
11380 müksos — mumió, mumulio
11381 15
11382 20
11383 25
11384 30
11385 35
11386 40
11387 45
11388 816
11389 mulst, v. ‘go crazy’; (long-vowel in) Cz. mýlit se ‘be mistaken’; o-myl ‘error’; Ukr. o-mylja- ty ‘delude’
11390 mulmulið ‘murmur’. Cf. murmur-, murmul-, etc. and mulió (2) Icel. cf. muldra, v. ‘rumble’; Sw. multra, id.; Blg. málmólja, id.; Latv. cf. muldet, inf. ‘twaddle’
11391 mülom, à, iom ‘muzzle, snouť. Cf. mulið (2). Gmc. only as noun OHG mül, n., müla, f. id.; Du. muil, m. id. beside (LW fr. Frisian) moel, id., ON müli, m. id. beside mod. müll, m. ‘halter, muzzle’
11392 mulos, à, iom, is ‘grinding, milling; grind- stone, millstone’. WP II, 285. Cf. mulið (1) Gk. mülos, m. "upper millstone; mill; müle, f. lower millstone; mill; millings, barley’; W mwl, m. ‘chaff, dus
11393 mülos “heavy, dull; weight Skt. müráh (ambig. (2) ‘dull, stupid; ON mell, gs myls, m. “stone, ball, weight: mod. Icel. müli, m. ‘beetling cliff; Sw. cf. mulen ‘murky, gloomy’. (Isophone: OCS mylo *mea
11394 muluó, mluuó ‘noise, chatter, utter, speak’. (Indo-Iran. phonol. obscure) Ir. cf. molbhta, adj. ‘extolled’; molbhtach ‘praiseworthy’; molmhar, adj. ‘noisy’; OCS mlüvljo, mlüviti ‘din, resound’; mlüva,
```


## [2026-09-07T17:39:02.703Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT musti ===\"; grep -n -E 'mušti|musti' BRT.txt | head -20\necho \"=== BRT maoka/muk ===\"; grep -n -E 'maoča|maoka|muk-|muč|maod' BRT.txt | head -30\necho \"=== BRT miva ===\"; grep -n -E 'mivāmahi|mivāmaide|miva|muyamna' BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-07T17:39:02.781Z] TOOL RESULT

```
=== BRT musti ===
10651:•  j.  xrü-  f.  'blutiges,  rohes  Fleisch':  musti.- masaah»m  xrüm  "ein  fausigrosses  Stück Fleisch""  Yt.  14.  33.  3)  'Grauen,  Graus' (nur  Ableit.)-  a)  Name  eines  Da^'a: psrme  xrB  (statt  AS.)  V.  /;.  9.
20598:•  j.  musti.masah-  i)  n.  'Grösse  einer Faust':  *°sl^  F.^jg''.  2)  Adj.  (auch fem.)  'faustgross':  'sat3h>m  (ASf.)  xrStn (sd.)  Yt./<^.33.
=== BRT maoka/muk ===
=== BRT miva ===
5815:•  j.  a-st9n»ta-  Adj.  'nicht  niederzuwerfen': 'taca  amuyamna  yazamaide  Vr.  7.  i.
19935:—  al  Tgl.  mivatU-  Adj.    —    Pfi.  (lu  Y.  44^:
24450:•  j.,  g.  vispäiS  Adv.  i)  'allzeit,  immer- dar'; är5i  (Sp.  185  o.)  »i  huähnhi  v° masdä  xsmivasB  saveY.34.^.  2)  'fiir alle  Zeit,  für  imnier'(?):  paotryan  Ikais} . . V  *vaaAus  vanftusans  {s6.)  W.13.1%1.
25241:•  ].,  g.  raziita-  Adj.  (fem.  *ta-)  'der  ge- radeste, richtigste,  rechtlichste,  gerechteste': *ya%a  *äis  lä  J  vansaitl  yä  data  ataJau! paouruyehyä  ratüi  iyaohana  °tä  (APn.) dngvata^ä  hya^cä  *aiäomye^aca . .  "wie es  den  Gesetzen  fiir  das  erste  Leben  ge- mäss ist,  so  wird  er  (näml.  Zara^u/tra) als  Richter  in  gerechtestem  Tun  gegen den  27rt(fgenossen  verfahren  und  gegen den,  bei  dem . ."  Y.j;^.  i''.  a)  von^an- tay-  (usw.) :  °öw  pantqm  daoaiti  ätars  . . ySi  ftißirym  lUfil  aiwidruzinÜ  "den  ge- radesten Pfad  gibt  (weist)  A.  .  .  denen, die  . ."  Yt  /o.  3;  —  mit  3  und  Abi.  oder Akk.  'hin  —  zu':  'tah^  pa%S .  .yS  asti  't3 j  aiäi  vahist)m!a  oASrn  asaonqm  "des geradesten  Pfeds  . .,  der  der  geradeste  ist hin  zu  Asa  und  zum  besten  Leben  der Gerechten"  Y.  6Ä  13.  a)  ahatpantay- (usw.),  das  aber  hinzuzudenken  ist:  yö dai^hsus  rqxlyqi^yh para  •/Jfnäml^a^i) baraiti  Yt.  io,  37*';  —  äid3?ar?nä  nastö •ta  (näml.  /a^a)  ". .  der  vom  geradesten Weg  abgegangen  ist"  Yt.  10. 105^';  — amuyamna  (sd.)  'tanqm  (näml.  pa^qm) Vi.17.1j;  13.3s-  b)  von  rainav-  m. (Stverz):  rar'hus 'tH  V.  13.  g  PUZ.jusw.;  — 'tfm,  'tat,  •iahe,  'ta  (VS.).  A)  mit  asts-  f. (Stverz.)  Name  einer  Gottheit:  °ta  ästa \'t.i6.7  usw.;   —  'tqm,  'taya,  'te  (VSf.).
28706:.  j.  'haeni-  C  'Geschoss':  liHrM . . ytiiht ''"""^  '''^  '""">''  'i'^'^  El"-.?.'. »»OTo(  (Sp.  931  o.)  ■nmam  *miva  saläil,  1'  ':'\^-  "'  —  "■*>;"«■««*  .  .  iäi-m Imza^rmia   '. .  dem  Ge'schoi«   zu   t^\/rä<!;y'f  ■ -hauv  klrJ- ^RyavJ'  l,am mAcn  900  und  1000"  YtJ.  no'l.  \frluli'yii'  Bh.j.911.         p)  substimtivischt
28878:•  j.  hakat  Adv.  'auf  ein  Mal,  zu  gleicher Zeit':  da'käni  ti..  h°  hasaar>m  aspanam V.25.3;  F.2b,  FrG.,  S1..V.22(?);  —  yai ioa  anaityä  dai5hus'  h'  usca  us./rävayStf Yt.  Jp.  68;  —  h°  niginptaäbya  angustatibya uig»rppta!ibya{s^) pa^nalibya  V.S.  70,  71; — y3  h'  astisla  varfsSsla . .  Ktitaia  hqm.- ralhwaydii  Yt  10.  72;  13.  78;  —  yai  h' *amruts  N.  24;  24-  «)  bei  den  Wörtern für  'beide'  und  'alle';  h'  vaim  ava.miva- mahi  hievasca  pivas(sd.)&  V.  iS.  55;  — h'  vTspa  aipiAirtntaiH  Yl  10.  7  s ;  —  ha vUpftn  ahom  astvarit»m  h* . .  nü^abdayaii V./<y,i6.
30509:I  gegeben,    gehörig  verkündet':    saauhasca \paiti  °taya  . .  amuyamnaya  . .  avarwnnayä Yty.133. I      ')   So   NA.   nach   Mf3;    aber  F  I,  J  10  usw.
```


## [2026-09-07T17:39:04.943Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD mucro/meuk ===\"; grep -n -i -E 'mucro|meuk|meug' AHD_watkins1985.txt | head -20\necho \"=== PHD mozag/mut ===\"; grep -n -E 'm(ō|o)zag|mwc|mūzag|mwck|mūdan|mūtak' PHD.txt PHD_mackenzie.txt | head -20",
 "description": "Grep Watkins and MacKenzie"
}
```


### [2026-09-07T17:39:05.024Z] TOOL RESULT

```
=== AHD mucro/meuk ===
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
=== PHD mozag/mut ===
PHD.txt:392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
PHD.txt:547:~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
PHD.txt:3634:shoe kafš, még, mozag.
PHD.txt:3642:show nimūdan.
PHD.txt:4857:mustgar Se F” ^ ale mozag ^ de 96 "пик
PHD_mackenzie.txt:2764:hammOxtan, hammOz- [ALPWN-tn' < A '" 'lp; hmwhtn ' , hmwc-,
PHD_mackenzie.txt:3594:moz [mwc I N --] banana.
PHD_mackenzie.txt:3595:mozag [mwck , N moza] shoe.
PHD_mackenzie.txt:4156:paymoxtan, paymoz- [ptmwhtn 1, ptmwc- I M pymwxt, pymwc-] don,
PHD_mackenzie.txt:4158:paymozan [ptmwcn l 1M pymwcn] garment, dress.
PHD_mackenzie.txt:7556:separate (y.) wextan, wisandan,           shoe kafs, mog, mozag.
PHD_mackenzie.txt:9135:                           AI~      mozag                    \~'\~
```


## [2026-09-07T17:39:28.769Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor leaf in (241,242,243,244,245):\n    print('======= leaf',leaf,'~ printed p.',leaf-21)\n    print(t[leaf][:3000])\nEOF",
 "description": "Print Horn leaves 241-245"
}
```


### [2026-09-07T17:39:30.075Z] TOOL RESULT

```
leaves 412
======= leaf 241 ~ printed p. 220
— 220 —
kurd. miMnk, mizl, mujüal (H.-Sch.) ^Augenwimpern';
bei. micäc, n. misäs ^Augenwimpern*, daneben LW.
mizayän (236).
ai. nimis' 'Blinzeln, Zwinkern des Auges*, skr. nMsa-,
das Bartholomae ZDMG. 44, 553 vergleicht, stimmt
lautlich nicht zu np. kurd. i, g. /, bei. c (für letzteres
erscheint im nb. regulär s, vergl. Geiger, Dialekt-
spaltung, 83).
981. ^nest 'betrunken* 0-
aw. vergl. mada- 'Kausch trank* ; phlv. mast (PV.);
ai. mattd- 'trunken', vergl. |/"fwad-, mddati 'froh sein,
sich berauschen'.
Allgemein entlehnt; oss. d. mast, t. mäsf 'Galle,
Zorn' (181) ist wegen des Bedeutungswechsels un-
sicher.
982. ^nust 'Faust*.
mäz. mis (*nitist).
aw. musti.[masah' 'faustgross* ; phlv. must (vd. 17
(18) Gl.) 2), mtistih (AV.), must (PPGl.); ai. musti-,
kurd. mist, miste/c; af/. mmt^ müt; bei. LW. mtist
(172) ; wa;k'. mösty sar. mut
983. tniiSten 'reiben*.
aw. [/^marz-j marezaiti *fegen'; phlv. mmt^ mmt
(vd. 4 (7) (26) für aw. marsta-); ai. l/'mar/-, mdrsfi
'abwischen'.
kurd. mistin 'fegen'; af/. mu/al; bei. musag, n. musay
'reiben*, kratzen, streichen, salben, mahlen' (244).
Eine Doublette zu np. maltden (No. 962).
984. muy, möy 'Magier, Feueranbeter*^), möbed,
ap. magu-; aw. -moyu- in moyu.fbis-? (vergl. Geldner,
*) Irgendjemand hat, wie mir Herr Prof. Nöldeke sagt, irgendwo
(die SteUe war augenblicklich nicht aufzufinden) das als arabisch geltende
medhüs 'sinnlos* für ein persisches Wort (|/ mad' + hös 'Verstand, 8inn*J
erklärt. Ich denke aber, dann könnte es nur mesthös lauten.
') Ganz falsch war natürlich meine Bemerkung ZDMG. 48, 36
Note 34.
') Im späteren Neupersisch ist der Magier zum '(ohristl.) Mönch*
und besonders zum 'Kneipwirt, Zecher* geworden (H ä f i ? häufig), vergl.
auch muybece^ muyän u. a. m.
======= leaf 242 ~ printed p. 221
— 221 —
Ved. Stud. II, 19); phlv. magu, magupat (arm. LW.
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
wickelt haben.
Unsicher.
988. meger 'wenn nicht, ausser, vielleicht'.
me nicht' + eger (No. 106), päz. ma agar (Aog.).
989. meges 'Fliege', jüd.-pers. Mo (Is. 7, 18)«).
aw. vergl. ma/si- 'Fliege, Mücke' ; phlv. magas (vd. 1
^) Den aus dem F§ bei Vullers abgedruckten Sahnämevers
konnte mir Herr Dr. Landauer nicht nachweisen.
') Z statt 8 findet sich dialektisch häufig: z. B. besbäs (AM. 55),
bezhäz oder semärüy, zemärüy oder kusbura^ kuzbura(YvL\\eT8); sepes
(jüd.-pers.) statt zi pes, vergl. si pester (Vullers); Käs. üzü d. i. an
8än; kauk.-bergjüd. zürnai sonst sürnm u. v. a. m. Umgekehrt steht
8 für z im ar. LW. sauswjird *ein Tuch', wörtlich *nadelgefertigt*
(sözengird), de Goeje, Bibl. geogr. arab. IV, 266. Ebenso wechseln
z und s, z. B. /äksi^ -/äkkl (Vullers, vergl. auch ebenda s. v. j^vhe und
======= leaf 243 ~ printed p. 222
— 222 ~
(16)), makas (Bahmyt.), mo/s (nur Umschreibung des
Awesta Wortes) ; ai. vergl. mäksa-j mdksikä-.
kurd. mis (LW. magäs'BiQne'); bei. makask, magisk,
n. mahisk 'Fliege, Mücke' (222) ; wa;^'- ^clcs, minj. moya,
np. meges ist wie die sämmtlichen anderen neu-
iranischen Worte ausser kurd. mis nicht direct mit
aw. ma/si-, ai. mdksa' (^2«) vereinbar.
990. mul Wein'.
ai. fn^d[vtka- 'Weintraube' (Hübschmann, ZDM6.
35, 133 Note 2).
niele% 'Heuschrecke' (Öähn. I, 188 Vers 1059) s. meig
(No. 1010).
991. {\)fnen *ich', men^ 'Eigenliebe, Übermut'.
ap. manä meiner (Gen. sg.); aw. mana; ksl. mene.
991**^ {2)men 'ein Gewicht' ^), ar. LW. mann,
skr. vergl. niäna- 'Maass (ganz allgemein), Maass-
stab, Gewicht', dann auch ein bestimmtes Gewicht'.
Oder zu ai. mand- 'ein best. Gewicht (Gold)', gr. ^«v«,
lat. mina, die semitische LW. sind, vergl. akkad. mana
(Schrader, Sprachvergl. und Urgesch.- 206 folg., 252)?
992. meniS, menisn (Wörterbücher) 'Sinn, Charakter,
vergl. dus[men, rr^^DirilD (Is. 12, 1).
ap. vergl. 'Jlpiaj/LisvTjg (Plutarch); aw. manah-^ dm-
manah-; phlv. dusman, vergl. men(i)sn; ai. rndnas-,
skr. durmanas.
993. mör 'Ameise', mürce-),
g. möirik 'schwarze Ameise'; Käs. V. möröund,
aw. maoiri- 'Ameise'; phlv. mör.
LW. (?) kurd. mürt^ merü (vergl. np. mtrük, nicht
belegt); afy. bei. (248) mör, n. möHk "Ameise*, vergl.
auch mörag 'Korn an der Flinte' (?); echt yidg. mur-
yäh (BB. Vn, 198).
^) Genaue Angaben über die verschiedenen gebräuchlichen Mens
findet man bei F. Stolze und F. C. Andreas, Die Handelsverhältnisse
Persiens (Petermann^s Mitteilungen, Ergänzungsheft Ko. 77), S. 83.
*) Keimt auf hör fäähn. I, 508 Vers 135), vergl. auch das reimende
hemcü mör bezör.
======= leaf 244 ~ printed p. 223
~ 223 —
Eine Sonderstellung nimmt im Iranischen — vergl.
auch arm. mrjimn, mrjiun (H. No. 207) — oss. d.
nniljvg, t. mäljig 'Ameise' ein.
994. tnöze 'Schuh', arab. LW. manzaj.
aw. [/^maoc^ mit paiti 'anziehen (sc. Schuhe)*, vergl.
framv/ti' *das Ausziehen (der Schuhe)'; phlv. tnööak
(Men. ; arm. LW. muöak), vergl. mök (chald. LW.
NpID), auch patmö/tan 'anziehen'; ai. [/^möö- mit ä,
prati anziehen (irgend ein Kleidungsstück)*, mit upa
*Schuhe anziehen*.
LW. afy. möza ; bei. müzag, n. mözay 'Socken, Stiefel,
Beinkleider* (174).
995. ninS *Maus*.
g. muSk,
ai. müs~, skr. müsaka-, mfisika- *Maus, Ratte*; arm.
mvkn 'Maus' (H. No. 206).
kurd. fni§ik, misk; Si{y. mayak, maya 'Ratte', maya-
küfai 'Maus, junge Ratte*; oss. d. miste, t. mist (189);
bei. musk, n. milsk (245).
996. möT 'Haar' ^).
g. mld.
phlv. mö, möd bezw. möf; bei. müd^ mtd, n. mi^
'Haar (eines Menschen), Ziegenhaar' (247).
i tritt sonst dialektisch im Np. nur für ursprüng-
liches ü, nicht für ö ein, doch giebt es Ausnahmen;
man wird also trotz g. bei. mtd doch eine ap. Grund-
form *mauda- annehmen müssen 2).
997. möye 'Weinen, Klage', möylden,
aw. vergl. amayavä' 'Leid'; phlv. wöyaÄ:; ai. vergl.
dmtvä'.
Die von Darmesteter, Et. ir. H. 169, ver-
glichenen aw. ai. Worte lassen sich mit np. möye
lautlich nicht vereinigen, und auch Bartholomae,
») Reimt auf röt, 8ähn. III, 1074 Vers 161, auf jöi, Vis und
RAmln, Seite 84 Yers 16.
*j Ganz unmöglich ist Spiegel 's Erklärung, Ar. Per. 61 (vergl.
Bartholomae, ZDMG. 42, 155^.
======= leaf 245 ~ printed p. 224
— 224 —
Studien, II, 178, befriedigt nicht, da er müye^ nicht
7nöye, als np. Form ansieht.
Fr. Müller, (WZKM. 5, 65) construirt eine *[/maud-
mit einem ap. "^matida-- als Grundform und identi-
ficirt np. möye mit arm. moir 'Bettelei', eigentlich
Torjammern', moiracik 'bettelnd' ; dazu auch np. mit st
*Klage*, mustmeud,
998. me (geschrieben meh) nicht* (prohibitiv).
ap. aw. ai. ma 'nicht' (fifj); päz. mo ; arm. mi 'dass
nicht* (H. No. 200).
kurd. me-; afy. ma-; oss. d. t. ma- nicht' (prohi-
bitiv) (173).
999. mih gross*, mehist ^), mihtnj mihter.
g. mas gross*, master.
ap. vergl. ma&ista- grösster*; aw. masyao grösser*;
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
*j Darmesteter, 6t. ir. I, 93 Note 3 (sehr unsicher).
```


## [2026-09-07T17:39:55.056Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ISS_alt_DKS muk ===\"; grep -n -E 'mūtak|parmūtan|mūt-|myaus|mūy' ISS_alt_DKS.txt | head -20\necho \"=== DKS mov ===\"; grep -n -i -E 'mivāmahi|amuyamna|muyamna' ISS_alt_DKS.txt CHEUNG.txt | head -20\necho \"=== CHEUNG muk ===\"; grep -n -E '\\*mauk|mōzag|muk|\\bmuč' CHEUNG.txt | head -30",
 "description": "Grep Bailey DKS and Cheung"
}
```


### [2026-09-07T17:39:55.137Z] TOOL RESULT

```
=== ISS_alt_DKS muk ===
827:хай a derivation from *ahaka- ‘ashes’ is proposed by G. Morgenstierne, МТЗ 12, 1942, 266, with Рагаё Лау. ayauttye, K 156:17 for *ayaunye written possibly dyaunnye, iw from BS ayaneya-, ајапеуа- "well-born', HI 64:20 üyünye beaiysye jsina (with m, not ñ) paba, K 156717 Итататруе ayau*nye jsia paba, її 10352 bvaiysyai ttravargyai jsīña paba 'three-divisioned well-born life continuum’. The adjective is also in JS 27vi afe yai üyüni rrumde subhadrre ‘уои were the horse well-born of king Subhadra’. ВӘ àjüneya-, ayangya-, Pali ajantya-, üjüniya-, ajañña-, and compound assájaniya-, see JRAS 1955, I4. For -tty- replacing -пу- see v 64743 samattyau. üyoys- 'be agitated’, participle ayosfa-, K дуд bisánu üyoysünu jánümata 'dispelling of all troubles'; K 8, Srg-vi cu buri aysmū üyauysána satva üyauysüri, и hivi aysmii vasvatte jsa và vasusindá ' whatever things trouble the beings with trouble of mind and they purify their own mind with purity"; contrast of ayauysa- and purity also in K ss, 1712; later form K. 55, 17r2 áyamysá. Participle üyosla- Z 4101 dyosla aphida ütca 'agitated disturbed water’; K 8, 5v2 ttye aysmii ayaustá ‘his mind agitated’; Sid. зог2 cu гїтй йіса se tavadye jenüka, cu йуаш а u pirüda ‘what is water gushing out, that removes bile, what is turbid and full of worms. ..', BS Ralusa-, Tib. sñog-čin; Manj. 89 йуаиз{а bajaiia utca ' water tossed in a pail’, From d-yauz-, Ау. yaoz- ‘һе in commotion’, O.Pers. yaud- (ayauda), Sogd. "y'wz, 'ушд, verbal "y'wz-: yk, compound "y'ws-hr'h, and pty'wzw ‘trouble’; Zor.P. ayüzitam, rendering Av. yaoz-, with gloss bë hüftenitan, N.Pers. justan, M.Parth.T. ушл-, uit, "yuz-, "ушй, noun 'ушх, second component rem- ywz; Pahlavi Psalter ywd-, but M.Pers.T. yws-, pdywa- from Parthian; Armen. lw уоух, youzem; Balo&i Juzay ‘to move, go, walk’, participle JusiBa, 2 plur. imperative }илїй, juzl£n- ‘to move the head’, fuzóx ‘walker’, IE Pok. 512 jeug- in Iranian, Germanic Got. Jiukan ‘to fight’, and Tokhara А yok-, AB yuk- 'to conquer’. See also myauys-:nyausa- ‘to be overthrown’, myausca, BS рагӣјауа- ‘defeat’.
=== DKS mov ===
ISS_alt_DKS.txt:6838:vamüda- 'move away Гот’, 2 24'116 Ёй vamüdandd cakkrä pvastañä ‘all evaded the terrible discus’, to base mür- ‘move’, see mvir- < *mür-y-, with -r- to base Av, imyav-, :miv- 'remove', O.Ind. mivati. ТЕ Pok, 743 meu- ‘thrust away', O.Ind. mio-:mü-, mivati, müta-, Av. amuyamna-, O.Ind. mürd- 'pressing, hastening’, Greek &yeu-, брери-, vea, Lat, moueó, mótus, Lit. тацји, mduti ‘put on (ring on finger)’,
=== CHEUNG muk ===
18219:away’, Latv. muku ‘I free, flee’, appear to point to a root with a non-palatal velar
```


## [2026-09-07T17:40:08.253Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E '.{300}(parmūd|parmüd|parmud|mūtak|mütak|mutak).{300}' ISS_alt_DKS.txt | head -10\necho \"=== PHD/NYB ===\"; grep -n -E 'parmūd|parmud|mūtak' PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head",
 "description": "Search for parmutan/mutak"
}
```


## [2026-09-07T17:40:10.145Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON موزه ===\"; grep -n -o -E '.{0,120}موزه.{0,200}' MON_part1.txt MON_part2.txt | head -20\necho \"=== MON مشت ===\"; grep -c 'مشت' MON_part1.txt MON_part2.txt",
 "description": "Grep Moin for muze"
}
```


### [2026-09-07T17:40:12.983Z] TOOL RESULT

```
=== PHD/NYB ===
NYB_vol2_glossary.txt:727:2aš [^5] the independent form of the cas. obl. 3d p. sg. = enel. -$ (g. v.); always preceding the w. to which it belongs; used 1. anaphorically in the interior of a sentence after a part of the sentence which has been placed first for emphasis: andar han Zartuxst | aš hac miyān Gp i hömikän burt || u pat uléh Zartuxšt | aš han i dašn paitištān hac Osan rote burt 5615-1? (Markwart's reading, Cat. 114 n. 1, is a failure); õi (pron.) mar | aš 6 pasčh gàv apāc rānēnīt 485; — not anaphorically: Ot (prep.) fravahr + Zartuxst | aš (viz. the snake) zafar frac zat 4012-13; purr-x"arrahéh i ax" à astómand | aš hac tan xYarrah from his (viz. Zartuxšt's) bodily splendour 377-8; — taking up an encl. -§ at the beginning of the sentence, after a part of the sen- tence which carries a lengthy attribute: api-š hamäk damik i-š apar rāh bit | aš *perävanihit kart 3316-17; — after an ad- verbial phrase beginning the sentence: adak apar pat jamän | aš hanjamanénit mūtak :61° (where aš anticipates mūtak, cf. s. v. -š). — 2. to introduce the apo- dosis (as api-$, adak-i8): after kakar 31?! ; after ka 327. 3319. 341. 565. 5717. 924. after a relative clause 3219, 9824, 100?7— 101?. — Probably identical with MPrthPrs š, written as an independent w. with two dots above (another explanation of this § v. A-H III, Gloss s. v.; ? in a fragmentary context [S] is obscure). Cf am, at, atün, asän.
NYB_vol2_glossary.txt:1993:the opposite of Vahuman 654-5; Srēš his chief adversary 665. 7711, 2516, 2814 v.s. v. distak; — his epithets: mūtak and tanäpuhrak 619%; zürdrus 7211-12, 103977; v. these ws. — Av. (35 sq.) aēšma- (Asmodatos, Book of Tobit 3:8 Av. ačšmo.dačva-); MPrth ‘smg’n ‘devils of wrath’; MPrs xysm; Paz. NP rašm, zism.
```


### [2026-09-07T17:40:16.751Z] TOOL RESULT

```
=== MON موزه ===
ugrep: error: error at position 86
-\xbf][\x80-\xbf]*){0,200}
                          \___exceeds complexity limits


=== MON مشت ===
MON_part1.txt:149
MON_part2.txt:226
```


## [2026-09-07T17:40:21.742Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'mūtak' NYB_vol2_glossary.txt | head -20",
 "description": "Find NYB mutak entry"
}
```


### [2026-09-07T17:40:21.790Z] TOOL RESULT

```
727:2aš [^5] the independent form of the cas. obl. 3d p. sg. = enel. -$ (g. v.); always preceding the w. to which it belongs; used 1. anaphorically in the interior of a sentence after a part of the sentence which has been placed first for emphasis: andar han Zartuxst | aš hac miyān Gp i hömikän burt || u pat uléh Zartuxšt | aš han i dašn paitištān hac Osan rote burt 5615-1? (Markwart's reading, Cat. 114 n. 1, is a failure); õi (pron.) mar | aš 6 pasčh gàv apāc rānēnīt 485; — not anaphorically: Ot (prep.) fravahr + Zartuxst | aš (viz. the snake) zafar frac zat 4012-13; purr-x"arrahéh i ax" à astómand | aš hac tan xYarrah from his (viz. Zartuxšt's) bodily splendour 377-8; — taking up an encl. -§ at the beginning of the sentence, after a part of the sen- tence which carries a lengthy attribute: api-š hamäk damik i-š apar rāh bit | aš *perävanihit kart 3316-17; — after an ad- verbial phrase beginning the sentence: adak apar pat jamän | aš hanjamanénit mūtak :61° (where aš anticipates mūtak, cf. s. v. -š). — 2. to introduce the apo- dosis (as api-$, adak-i8): after kakar 31?! ; after ka 327. 3319. 341. 565. 5717. 924. after a relative clause 3219, 9824, 100?7— 101?. — Probably identical with MPrthPrs š, written as an independent w. with two dots above (another explanation of this § v. A-H III, Gloss s. v.; ? in a fragmentary context [S] is obscure). Cf am, at, atün, asän.
1993:the opposite of Vahuman 654-5; Srēš his chief adversary 665. 7711, 2516, 2814 v.s. v. distak; — his epithets: mūtak and tanäpuhrak 619%; zürdrus 7211-12, 103977; v. these ws. — Av. (35 sq.) aēšma- (Asmodatos, Book of Tobit 3:8 Av. ačšmo.dačva-); MPrth ‘smg’n ‘devils of wrath’; MPrs xysm; Paz. NP rašm, zism.
```


## [2026-09-07T17:40:22.793Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'موزه' MON_part1.txt MON_part2.txt | head -20",
 "description": "Grep Moin for موزه simple"
}
```


### [2026-09-07T17:40:22.850Z] TOOL RESULT

```
MON_part1.txt:127:کتابخانه‌ها و موزه‌های لندن و پاریس نیز مطالعاتی بعمل آورد. 
MON_part1.txt:160:دانشکد؛ ادبیات (سرین) و سخنرانی دیگری در موزه کیمه به دعوت انجمن 
MON_part1.txt:168:در کتابخانه‌ها و موزه‌های بلژیک و هلند به مطالعه پرداخت. در سال ۱۳۴۲ 
MON_part1.txt:18829:موزه‌ای که از بوست پشمدار بدوزند» 
MON_part1.txt:27473:کقش و موزه و امثال آن» بایوش. 
MON_part1.txt:54843:امر.) کفشی که روی موزه به پا کنند؛ 
MON_part1.txt:55750:خراز: 2( [ع.] (ص.) دوزندهة درز موزه 
MON_part1.txt:56911:موزه. سپل شتر. سم شترمرغ؛ ج. اخفاف» 
MON_part1.txt:56931:کفش‌دوز» موزه‌ها. 
MON_part1.txt:61639:دست‌موزه: (022)6. (امر.) تحفه» 
MON_part1.txt:65970:گرفته, آموخته» دست آموزه انسی؛ مق. 
MON_part1.txt:66307:ستوران» توسن. (ص.) دست آموزه رام. 
MON_part1.txt:74210:موزه: سا چکمه. ترکیبات فعلی: ساق بر 
MON_part1.txt:76178:موزه. 
MON_part1.txt:80552:در موزه افتادن: (کد.) اقاست کردن در 
MON_part1.txt:86278:میان درز کفش و موزه ویراق زین اسب 
MON_part1.txt:94114:واقت به دقایق و رموزه آ گاه. (تص.) آنکه 
MON_part2.txt:10791:موزه‌های سلطنتی ارو با می‌بینیم. . نمونه‌ای از 
MON_part2.txt:17975:(دانش آموزه دانشجو) اختصاص دهند و در 
MON_part2.txt:18222:کفشگران و موزه‌دوزان بر سر سوزن کشند
```


## [2026-09-07T17:40:32.728Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -B3 -A6 '^موزه' MON_part1.txt MON_part2.txt | head -60\necho \"=== check page markers ===\"; grep -n -m5 '\\[pdf page' MON_part1.txt | head",
 "description": "Find Moin headword muze"
}
```


### [2026-09-07T17:40:32.802Z] TOOL RESULT

```
MON_part2.txt-10788-شامان برای اهداء به سلاطین خارجی 
MON_part2.txt-10789-می‌بافته‌اند و به همین دلیل است که این گو نه 
MON_part2.txt-10790-فرش‌های ابریشمی و زربفت را غالبا در 
MON_part2.txt:10791:موزه‌های سلطنتی ارو با می‌بینیم. . نمونه‌ای از 
MON_part2.txt-10792-این قالی هم اکنون در موز ویکتوریا آلبرت 
MON_part2.txt-10793-انکلستان وجود دارد. این نوع قالی‌ها را از 
MON_part2.txt-10794-آن جهت لهستانی می‌گویند که در گذشته 
MON_part2.txt-10795-تصور می‌کردند قالی‌های مزبور به وسیله 
MON_part2.txt-10796-بافندگان ایرانی در لهستان بافته می‌شود. قالی 
MON_part2.txt-10797-میر: نقشهٌ آن بوته‌های ترمه‌یی است. این 
--
MON_part2.txt-67939-شده» سنجده. دارای وزن (شعر)؟ مق. 
MON_part2.txt-67940-ناموزون. متناسب. طبع مورون: قر بح 
MON_part2.txt-67941-شاعرانه مستقیم که اوزان دلیسند آفر بند. 
MON_part2.txt:67942:موزه: (۵-)2۸ [- معر. موزج] (.) نوعی 
MON_part2.txt-67943-پاافزار که تا ساق پا و زیر زانو را فرا گیرد؛ 
MON_part2.txt-67944-چکمه. موزه در گل ماندن: ( کد.) درمانده 
MON_part2.txt-67945-شدن» بیجاره گشتن؛ مىتلی شدن. 
MON_part2.txt-67946-
MON_part2.txt-67947-مو ره. 6 (.) مسجمو عه آثار هنری و 
MON_part2.txt-67948-باستانی. محل حفظ و نمایش آثار هنری و 
MON_part1.txt-18826-اوفی: (.«ه) ,2۳15 [ع.] 0 
MON_part1.txt-18827-بیماندار تر» وفادار تر. 
MON_part1.txt-18828-اوی: (-.۷۸ه) ,سد [- او غ. تسر. مف.] (.) 
MON_part1.txt:18829:موزه‌ای که از بوست پشمدار بدوزند» 
MON_part1.txt-18830-چم پشمین. چوب‌های فوقانی آلاچیق. 
MON_part1.txt-18831-اوقات: .0۳ ,اتاسه [غ.] (۰) ج. وقت»؛ 
MON_part1.txt-18832-هنگام‌ها؛ روزکارها ساعات» ازمنه. اوقات 
MON_part1.txt-18833-
MON_part1.txt-18834-
MON_part1.txt-18835-اوقات فرهنگگ فارسی معین ۰ ۲۱۵ 
--
MON_part1.txt-56908-
MON_part1.txt-56909-خف: 01)0*(ع.] (ص.) سبکث» خفیف. 
MON_part1.txt-56910-صف: )/۲0 [ع.] (.) کفش» بای‌افزار» 
MON_part1.txt:56911:موزه. سپل شتر. سم شترمرغ؛ ج. اخفاف» 
MON_part1.txt-56912-خفاف. 
MON_part1.txt-56913-
MON_part1.txt-56914-خفاء: 0 .ف. خفا] (مصل.) بوشیده 
MON_part1.txt-56915-شدن» نهفته گشتن. (امص.) تشد کم 
MON_part1.txt-56916-نهانی» نهفتگی؛ مق. ظهور. 
MON_part1.txt-56917-
--
MON_part1.txt-74207-چنار. ساق چناری: به رنگ ساقةٌ چنار» سبز 
MON_part1.txt-74208-روشن. ساق عرش: پایةٌ عرش الهی. ساق 
MON_part1.txt-74209-عروس (عروسان): نوعی شیرینی. ساق 
MON_part1.txt:74210:موزه: سا چکمه. ترکیبات فعلی: ساق بر 
MON_part1.txt-74211-ساق مالیدن: دست و با زدن در حال مرگ. 
MON_part1.txt-74212-ساق بر مالیدن: آماده رفتن شدن. 
MON_part1.txt-74213-
MON_part1.txt-74214-ساق: ب«جّه [تر .] (ص.) سالم. ساق و سلامت: 
MON_part1.txt-74215-صحیح و سالم. تندر ست. 
MON_part1.txt-74216-
--
MON_part1.txt-76175-۵ فرع. سج.) 
MON_part1.txt-76176-
MON_part1.txt-76177-سر: 907 (.) کفشی که از ریسمان بافند؛ 
MON_part1.txt:76178:موزه. 
MON_part1.txt-76179-
MON_part1.txt-76180-سر: »۵0 [- سرخ ] (ص.) سرخ» سرخ رنکگ. 
=== check page markers ===
```


## [2026-09-07T17:40:46.290Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '67900,67960p' MON_part2.txt | cat -n | sed -n '1,60p'\necho \"=== nearby headers ===\"; awk 'NR>67700 && NR<68200 && /معین/' MON_part2.txt | head -20",
 "description": "Context around Moin muze entry"
}
```


### [2026-09-07T17:40:47.606Z] TOOL RESULT

```
     1	سار بزرگ وصویل ی شوب و گاهی طول 
     2	یک برگک به رل سردوز مرس 
     3	هر برگ در راستای ؛ بیشترین پهنه از ۱۰ 
     4	و تیمتر نیز تجاوز می‌کند . گل‌هایش بطور 
     5	فراهم در غلافی جای می‌گیرند و گل 
     6	آذینش شبیه خرما است. شو‌هاشن کوشت وا 
     7	و مطبوع و خوراکی است و مجموع میوه‌ها 
     8	خوشه‌ای را بوجود می آورند که رژیم نامیده 
     9	می‌شود. . درخت موز در اکثر نقاط گرم دنیا 
    10	کاشته می‌شود و اخیرا در نواحی جنوبی 
    11	ایران به کشت آن مبادرت کرده‌اند؛ طلره 
    12	بتان. 
    13	
    14	موزانسیک: 1 (.) مجموعه 
    15	مکعب‌های کو چکث رنگارنگ از مرمر یا 
    16	اسمالت که رسمی هندسی را تشکیل می‌دهد 
    17	و در سیمان کار گذاشته شده. نوعی آجر که 
    18	با سیمان و شن‌های رنگین ساخته شود. 
    19	
    20	جانم ارق: 
    21	
    22	مورر: )02 [نام سازنده تفگ ] 
    23	1( تفنگی که در سال ۲ ۱۸۷ م. . در آلمان 
    24	متداول شد و بعدها مکرر تکمیل گردید. 
    25	پیاده نظام آلمان تا سال ۱۹۴۵ م. آن را 
    26	ر میبردند. این سسلاح 
    27	
    28	
    29	۱۸۵۰ فرهنگ فارسی معین موز ع 
    30	
    31	
    32	توسطار تش‌های‌مختلف اروپایی پدیرفته و 
    33	متداول گر دید. تبانجه‌ای که نوع عالی ۳ 
    34	قنداق چوین هر مرج 
    35	نبز هست ‏ سوار می‌شو د. (تتکسیر ۳۵۳). 
    36	موزع: عععسوس [ع.] (افا.) توزیع کتنتده: 
    37	بخش کننده؛ جع مور عین. 
    38	
    39	موزود: (-02۱۳۷۲2۲۱۱۱)۵۵0۱۷] [ع.] (امسف.) وزن 
    40	شده» سنجده. دارای وزن (شعر)؟ مق. 
    41	ناموزون. متناسب. طبع مورون: قر بح 
    42	شاعرانه مستقیم که اوزان دلیسند آفر بند. 
    43	موزه: (۵-)2۸ [- معر. موزج] (.) نوعی 
    44	پاافزار که تا ساق پا و زیر زانو را فرا گیرد؛ 
    45	چکمه. موزه در گل ماندن: ( کد.) درمانده 
    46	شدن» بیجاره گشتن؛ مىتلی شدن. 
    47	
    48	مو ره. 6 (.) مسجمو عه آثار هنری و 
    49	باستانی. محل حفظ و نمایش آثار هنری و 
    50	باستانی و محموعه‌های مختلف. 
    51	مسسسسو زیسین: مامتان (رص. .) 
    52	مسوستی‌دان» نوازنده. هصسح.- احتراز از 
    53	استعمال این کلمة بیگانه اولی است. 
    54	موزیک: ۲ (.) موسیقی. 
    55	مسوزیکال: 722 (ص.) مروط به 
    56	موسیقی. 
    57	
    58	موز: : 712 [قس. موی؛ مو ب | ( ی 
    59	موز: : (2)0۳62تا (۱.) تالات؛ ۳ 
    60	موژیک: ۶ روسی: دهقان 
=== nearby headers ===
فرهنگ فارسی معین 
۱۸۵۰ فرهنگ فارسی معین موز ع 
فر هنک فاررسی معین 
موشح فرهنگ فارسی معین تسیل
```


## [2026-09-07T17:41:01.001Z] TOOL CALL #29: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py",
 "description": "Read ref_page.py header"
}
```


### [2026-09-07T17:41:01.058Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Fetch ONE cited page of a scanned reference, on demand.

    python3 tools/ref_page.py BQT:918          # printed page 918 of Borhan-e Qate'
    python3 tools/ref_page.py IRN:119 --image  # also print the path of the page image
    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping

Looks up the reference in data/verification/sources/refs_online.json
(`scans`: list of {file, first_printed, last_printed, pdf_offset, lang}), renders the
matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
the reference's language(s), caches both under
data/verification/sources/refs/ocr/<ABBR>/<printed page>.{png,txt}, and prints the
OCR text. Only the cited page is ever processed — never the whole book.

`pdf_offset` means: pdf page index (1-based) = printed page + pdf_offset.

If the OCR is too poor and you transcribe the relevant passage(s) from the PNG yourself,
save that transcription as <printed page>.vision.txt next to the .txt; from then on this
tool prints the transcription instead of the OCR, so no page is ever read twice.
"""
import sys, os, json, subprocess, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "verification", "sources")
TABLE = os.path.join(SRC, "refs_online.json")
REFS = os.path.join(SRC, "refs")
OCR = os.path.join(REFS, "ocr")
TESSDATA = os.path.join(REFS, "tessdata")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    m = re.match(r"^([A-Z]+)(\d*):(\d+)$", args[0])
    if not m:
        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
    abbr, vol, page = m.group(1), m.group(2), int(m.group(3))
    table = json.load(open(TABLE, encoding="utf-8"))
    ref = table.get(abbr, {})
    scans = ref.get("scans") or []
    if vol:
        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
    scan = None
    for s in scans:
        if s.get("requires_volume") and not vol:
            continue
        if s.get("first_printed", 0) <= page <= s.get("last_printed", 10**9):
            scan = s; break
    if "--pdf-page" in argv:
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
```


## [2026-09-07T17:41:03.936Z] TOOL CALL #30: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2010 --image 2>&1 | head -60",
 "description": "Fetch Borhan page 2010"
}
```


### [2026-09-07T17:41:05.148Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 93; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2010.png
REF: BQT:2010  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 93  OCR-lang: fas

مینیون ۱
مینیون ۱)- بفتح اول‌وثانی بتحتانی] زده » بلفت پونانی شنجرف را کوبند که مسوران
رسیده و کسر نون وبای حطی بواو کشیده وبنون | ولقاشان بکار برند .
بیان پانزدهم
در میم با شین نقطه دار مشتمل برهفتاد و دو لغت و کنایت
مشاش - بنتح اول و ثانی بالف کشیده بمعنی آنبوه و بسیار وپر و لبریز وسطین وکنده
و بشین نقطه دار زده » انگبیته (۲) را کوبند | وغلیظ باشد ۴ - ونام قربه‌ایست ازبلوکات غزئین
وآن علی‌باشد قوام داده که برطبق ریزند وپهن | تزديك بموضع مکانه کهآنهم ازقرای‌تزنین است
"کنند تا سرد شود وسخت گردد و دروقت‌خوردن - و جنم اول » معروف است که کر ه کردن پنجةٌ
دندان گیر باشد ۱ - و منع از شاشیدن و بول دست باشد وجمع نمودن انگشتان چنانچه پنجهٌ
کردن هم هت ۴ - و بنم اول» درعربی زمین ۱ دست ظرفیت بهم رساند 8 - و مردم کم و قلیل
نرم ونفی وطبیعت و استخوانهای نرمی که وان | وکروه الاك را نیز کوبند ‎٩‏ - و بمعنی مالید
خوردن ۴ . هم آمده است که ماضی مالیدن باشد چه مشتن
مشبت قلعه - کنایه ازمجمره و عود بمعنی مالیدن است ۷ - و بیخ‌گیاهی هم هت
سوز است - وکنایه ازآسمان هم هت . خوشبوی که‌تخمآ ترا نودری‌خوانند ۸‏ وپعربی‌سعد
مشت - بفتح اول وسکون ثانی وفوقانی | کوبند ‎٩‏ .
(۱) چك » چش : هسینون . (۷) چش : آبگینه .
۱« مشخته . حلوایی بود صافی و درشت . بتازی آنرا ماش خوانند . چین درچین
بود .» « لغفت فری ص 20۸ * » ولی در قاموسهای عربی دیده نشد . رك : مشخنه » انگبینه .
۴ ر4:شاشیدن . ۴ - رك : منتهی‌الارب » اقرب‌الموارد .
۴ -کردی 150 ( فراوان ) « ژابا صس ۳۹۹ * : در اراك ( سلطان] باد ) 1325121 و
5 ( پر ولیریز ) ۸« مکی‌نزاد » :
ازرقی دیو چهر بز مژه رنگه از بدی مشت و از هجیری ونگه.
شیخ سووان « جهانگیری »۸« رشیدی ».
6 - پهلوی 33151 (مشت . قوت) « نیب رکك ص۱۵۳ ۰ اوستا 7۳05۳811 ( 1018811
48 ) [ باندازء يك قبضه ] «* بارتولمه ۱۱۸۹ > هندی باستان- ]1215121 ۰ مازندرالی
8 . افقانی ۳981 ۰ 1301 ۰ بلوچی ع 32158 ۰ وخی 13081 » سربکلی 1311 «اسشق
۲ آرمنی ع 2916 ( دسته » بته ) ۰ قی : پهلوی 27۳015116 « هوبشمان ۹۸۲
کردی 7081 ( مشت ) « ژابا س ۳۹۸ ؛کردی ع 1 ( معت ) « ژاباص ۳۹۹ *.
‎٩‏ -کگوبند : يك مشت مردم بیچاره و ملس . ۷ - رك : هشتن .
۸ -رك: مت . مسته . ‎٩‏ -مفت بکراول » جوی آب :
باز جهان گشت چو خرم بهشت خوبد دمید از دو بناگوش هعت .
« منوچهری دامغانی ص ۱۳۹ » ورك : جهانگیری » رشبدی .
( برهان قاطع ۲6۴ )
```


## [2026-09-07T17:41:14.117Z] TOOL CALL #31: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2051 --image 2>&1 | head -60",
 "description": "Fetch Borhan page 2051"
}
```


### [2026-09-07T17:41:21.926Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 134; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2051.png
REF: BQT:2051  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 134  OCR-lang: fas

سس مه موزم
موز - بنتح اول و سکون ثانی و زای | که نیردان و نرکس که کل معروف باشد بنظن
قطه‌دار » میوه‌ایست . درمصر ویمن وهتدوستان | آهده است ؛ و میتواند بودکه هردو غلط باشد
بسیار میباشد و ۶ برکش » باشد یمتی بر که درخت موز را
رد رم ۵ و مود میگکویتد رتسیف خران کرد پاش .
آن سه چهار ال 1 و اه اعلم .
کزطول‌وزیاده هم هم همق - با زای فارسی بروزن سوز , غم
بر لیم گزعرضش ۹۷ واندوه و مصیبت‌را کوبند ۴ - و با ثانی مجهول,
دارد ویکال نی بمعنی تالاب وآ بگیر وآب انبار باشد 6 .
بیشتن پارندهد موژران ۱ - با زای فارسی‌وتانیمجهول
وهرسال ازییخ ۳1 بروزن طوفان » چشم پر كرشمه شهلا را گویند
میبرند و باز 1 1 - و چشم خواب آلود را هم کفته‌اند - و ثرکس
۰ ۳ ۹ 0 ۰ ۰ 8 8

بلند میشود لزید نیم شکفته را لیزمیگوبند - وبمعنی‌شخص‌خواب
ومیوه میدهد / س آلود هم‌آمده است ؛ و باین‌ممانی با زای هوزهم
و آنرا پزبان ۳ | درست است..
هندی کیله موز دو نس ۷ ه با زای هوز و دال
پروزن حیله بالا: درخت‌موز. پایین‌میوه موز | ابجد و نون و تای قرشت بروزن غرشگو فکن.
خواند ؛ و بشم اول هم آمده است و او باندام بلغفت زند وپازند(۱) بمعنی فروختن باشد که در
ماه پنج شبه است ۱ ؛ وموز مکی ۴ به بزرکی | مقابل خربدن است .

بادنجان میشود؛ ودربسی‌ازدخها بمعنی‌ت رکش ۴ موزه #. یم اول بروزن‌بوزه» معروف

(۱) چك : ژند و پاژند - :

۹ - موز 022826 (فض) میوة درخت موز 0887246۲ (فر) ( 51062919 352 )
است . رك : ستوده ص ۷۹-۷۸ ؛ وآن از کیاهان يك لپه است. ۴ - ۸ موز ... میوه‌ای
بود درمص معروف, وموز مکی چون باتنگانی بود . طیان (مرغزی) کوید :

موز مکی اکرچه دارد تام بکننش چوشکر اسر جام. > « لغت فری ص ۱۸۸ >

۴ - موز تر کش بود » « لغت فرسی ص ۱۸۸ ». ظ. تراکش مصحف « نرکس > است
که بعد درمتن برهان ذ کرشده و« ب رکش »> هم که موْلف کمان برده آهم ظ. مصحف همین‌کلمه
است » وگوبا اصل « نرکس موژان > بوده . رك : موژان » موجان .

۴ - قن : موی » موبه . ورك : موژه . - رك : موژه :

چو زلف خوبان در جوبهاش مرزنگوش چو خطخوبان بر موژهاش سیسنی.
فرخی سیستّانی « جهالگیری >.
ولی دردیوان فرخی چاپ عبدالرسولی (س ۱۳۲) بجای موژهاشی « مرزهاش >آمده .

‎٩‏ - رك : موجان. ۷ - هز. 12)8(2016۵8)1(128. پهلوی ۶۳۵2127 (فروختن)
« پوتکر س ۰۱۱۷ ۸- اوستا -ع1۳20 با اه ( پودیدن [ کفش ] ) » فقس :
- [1180202:1 ( بیرون آوردن [ کفش ] ) ؛ پپلوی 1320026 , ارمنی اع ۰32026 قسی
6 ,0213267120 ( پوشیدن )» هندی باستان -3366 با 2 » 87811 ( پوشیدن [هرقطعه
جامه] ). با 1202 (پوشیدن کفش)» کلمات‌ع : اففانی3-822 ۰ بلوچی328۵788 ۰ 12020860
( جوراب » چکمه . پاپوش ) « اسشق۹۹4 ۰ معرب آن موزج « این درید » «تفس» .
```


## [2026-09-07T17:41:44.304Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS muxt ===\"; grep -n -E 'muxt|mvc|mōč|mucak' SNS.txt SNS_pages.txt | head -20\necho \"=== BRT framuxti/paitismuxta ===\"; grep -n -E 'framuxti|fra-muxti|paitis.muxta|paitismuxta|muxti' BRT.txt | head -20\necho \"=== LEW mucro ===\"; grep -n -E 'mucro' LEW_1910.txt LAT.txt | head -10",
 "description": "Grep SNS, BRT, LEW"
}
```


### [2026-09-07T17:41:44.386Z] TOOL RESULT

```
=== SNS muxt ===
SNS.txt:13851:A paitiSmuxta-, paitiSmuxta- - .«- /"«*»' iWh 
SNS.txt:13921:, ft paitismuxta-, paitiSmuxta- = . e ^'^ 
SNS_pages.txt:9799:         paitiSmuxta-, paitiSmuxta-
SNS_pages.txt:9871:        paitismuxta-, paitiSmuxta-                =    .
=== BRT framuxti/paitismuxta ===
2945:•  j.  aoSra-  n.  'Schuhwerk,  Schuhzeug': *zannya  °ärii(IS.)  *paiti,smuxia  yä  vupö.- pTsa  bamya  "mit  goldenem  Schuhzeug  an- getan, mit  reichverziertem,  glänzendem" Yt5.78;  64;  —  mal  '%ranqm  framuxti . .  upa.mqnaytn  "mit  Ablegung  ihres  Schuh- zeugs  sollen  sie  . ."  V.  ö.  27,
=== LEW mucro ===
LAT.txt:20804:cuspis auctior in mucrone* fastigata, ou "qni va en pente" (en consi¬
```


## [2026-09-07T17:41:46.202Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD/WEB mucro ===\"; grep -n -o -E '.{0,80}[Mm]ucro.{0,200}' FSD_vol3.txt WEB_vol1.txt 2>/dev/null | head -10\necho \"=== KLN mucro ===\"; grep -n -o -E '.{0,100}mucro.{0,250}' KLN_1966.txt | head -6",
 "description": "Grep English dictionaries for mucro"
}
```


### [2026-09-07T17:41:51.645Z] TOOL RESULT

```
=== FSD/WEB mucro ===
=== KLN mucro ===
ugrep: error: error at position 83
bf][\x80-\xbf]*){0,250}
                       \___exceeds complexity limits
```


## [2026-09-07T17:42:02.219Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E 'muxt' BRT.txt | head -20\necho \"=== BRT muc root ===\"; grep -n -E \"^\\s*•?\\s*[a-z]*\\s*muc|'?muc-|muč\" BRT.txt | head -20",
 "description": "Grep BRT for muxt and muc"
}
```


### [2026-09-07T17:42:02.341Z] TOOL RESULT

```
2945:•  j.  aoSra-  n.  'Schuhwerk,  Schuhzeug': *zannya  °ärii(IS.)  *paiti,smuxia  yä  vupö.- pTsa  bamya  "mit  goldenem  Schuhzeug  an- getan, mit  reichverziertem,  glänzendem" Yt5.78;  64;  —  mal  '%ranqm  framuxti . .  upa.mqnaytn  "mit  Ablegung  ihres  Schuh- zeugs  sollen  sie  . ."  V.  ö.  27,
15097:•  j.  paiti.ämuxta-'),  *piiti.Smiixta-" " Adj.  (fem.  °/ä-)  'mit  Fusszeug  bekleidet,  be- schuht': ar?dvl  ißra  . .  tiismga  (sd.)  aoira *'ta  (NSf.)  zaranySMrvtxina  Yt  5.  64; 78.  a)    vom    Hufbcschlag:    tt  para.-
15965:•  j.  '^päiti.Smuxta-  Adj. :  s.  unter  paiti.- smuxta-.
17743:•  j.  fra-muxtay-  f.  'Losbinden,  Ausziehen (des  Schuhwerks)':  mal  ao^ranam  'ti  V. 6.  =7.
27918:•  j.  zaranyö.tuvix&na- Adj. 'mit  goldener Verschnüning':  andvl . .  ao%ra  *päili. smuxta  'na  ". .  mit  Schuhwerk  angetan, das  mit  goldenen  SchnUrbändem  befestigt ist"  Yt.5.  64.
=== BRT muc root ===
```


## [2026-09-07T17:42:11.588Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=9700 && NR<=9900' SNS_pages.txt | grep -n 'pdf page' | head\necho \"---- context ----\"; sed -n '9780,9815p' SNS_pages.txt\necho \"==== find pdf page tag before 9799 ====\"; awk 'NR<=9799 && /pdf page/{p=$0} END{}' SNS_pages.txt; grep -n 'pdf page' SNS_pages.txt | awk -F: '$1<9799' | tail -3",
 "description": "Locate SNS page for paitismuxta"
}
```


### [2026-09-07T17:42:12.896Z] TOOL RESULT

```
---- context ----




(•

                                                                                                                                                                        •*> :cfi:MH               :   >* :rf
                                                                     ca:jii-              cih:t MiW>. 588)cit:^j^- cit/cis                                                                        :fc-

                                                                 .                                                                    (6Yf jte^o-L/)                        ci     ,          ell hn?
                                                                 i
                                                                                              H-l/^^ -TY/IY^                             ir/A^                (tA-* « ft**- 1) 4f                 (0
                                                           iWh       -Yr-ff -aA-af-u-rr-vY^ -r/i** .^j^u.^u*. i^
                                                .«- /"«*»'                                                                                                                                            T)
                                                                                                                                                                                          .




         paitiSmuxta-, paitiSmuxta-
                                                                                                                                                                                                  (
                                           -

     A                                                                    6/6^ -IT/f^ .YW\-Y/r^                                           H-1.Y-1.?M—AI-AA-Ad-^r
                                                                                                                              ,




                                 U; c-^^ "^ *jV
                                                                                                                                    .—_,, L~          C^U **L Ojl)                                            m
ETV
                                                                                                   •   *J*^ •   W       « ***• >.i fyj --»
                                                                                                                                                 «
                                                                                                                                                     o 'jj *Sj>
                                                                                                                                                         I
==== find pdf page tag before 9799 ====
```


## [2026-09-07T17:42:19.240Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nff=0\nfor n,l in enumerate(lines,1):\n    if n==9799: print('leaf for 9799:',ff)\n    ff+=l.count('\\f')\nprint('total leaves', t.count('\\f')+1)\nimport re\nprint(re.findall(r'\\[pdf page \\d+\\]',t)[:5])\nEOF\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['SNS'],ensure_ascii=False,indent=1))\"",
 "description": "SNS leaf mapping"
}
```


### [2026-09-07T17:42:20.545Z] TOOL RESULT

```
leaf for 9799: 140
total leaves 243
[]
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
```


## [2026-09-07T17:42:28.873Z] TOOL CALL #37: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T17:42:28.880Z] TOOL RESULT

```


```


## [2026-09-07T17:42:32.165Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B4%D8%AA",
 "prompt": "Give the Persian entry for مشت (mošt) \"fist\": its full etymology (Middle Persian, Proto-Iranian, Proto-Indo-Iranian, PIE reconstruction) and cognates, verbatim."
}
```


## [2026-09-07T17:42:33.897Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B2%D9%87",
 "prompt": "Give the Persian entry for موزه (mūza/mūze) \"boot\": its etymology (Middle Persian, Proto-Iranian, PIE root), cognates, and any Arabic borrowing mentioned, verbatim."
}
```


### [2026-09-07T17:42:37.510Z] TOOL RESULT

```
# Persian Entry for مشت (mošt) "Fist"

## Etymology

The word derives from Middle Persian (mwšt' /mušt/, "fist"), which came from Proto-Indo-Iranian *muštíš ("fist").

## Cognates

The entry lists several related words across languages:

- **Avestan**: 𐬨𐬎𐬱𐬙𐬌 (mušti)
- **Sanskrit**: मुष्टि (muṣṭi)
- **Old Armenian**: մշտիկ (mštik) — noted as "an Iranian borrowing"

## Descendants

The Persian term influenced multiple languages:
- Classical Azerbaijani: müşt
- Middle Georgian: მუშტი (mušṭi), which subsequently entered Armenian as մուշտի (mušti)
- Kashmiri: مُش (muś)
- Kazakh: мұш (muš)
- Ottoman Turkish: مشت (muşt), which developed into modern Turkish muşt
```


### [2026-09-07T17:42:39.498Z] TOOL RESULT

```
# Persian Entry for موزه (Boot)

## Etymology
The word derives from **Middle Persian *mwck'* (mōzag, "shoe")**, which came from **Proto-Iranian *\*hmáwčati* ("to clothe")**.

## Cognates
Related terms appear across Iranian languages:
- Middle Persian (Pazend): mōža ("stocking, boot")
- Parthian: mōžag
- Baluchi: mōzag, mōžaġ ("boot, legging")
- Pashto: mōza ("stocking, boot, covering for the legs")

## Borrowings into Other Languages
The word was borrowed into several non-Iranian languages:
- Old Armenian: մուճակ (mučak)
- **Arabic: مَوْزَج (mawzaj)**
- Byzantine Greek: μουζάκιον (mouzákion, "boots")

The last borrowings possibly came through Armenian intermediaries.
```


## [2026-09-07T17:42:45.985Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/mucro",
 "prompt": "Give the Latin entry mucro: meaning and etymology (including any PIE reconstruction and cited authorities such as de Vaan), and also any English entry \"mucro\" with its definition."
}
```


## [2026-09-07T17:42:47.454Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mewk-",
 "prompt": "What does this reconstruction page say: the root's meaning, derived terms, and descendants (especially Indo-Iranian: Avestan, Sanskrit muc-, and any word for shoe)?"
}
```


### [2026-09-07T17:42:51.812Z] TOOL RESULT

```
# Mucro: Latin and English Entries

## Latin Entry

**Meaning:** The Latin *mūcrō* has three definitions: "a sharp point, especially the point of a sword"; figuratively, "a sword"; and "a sharp edge."

**Etymology:** The etymology is uncertain. According to the article, it may derive from a Proto-Italic *\*meuk-ro-* or *\*mouk-ro-*, which traces to a Proto-Indo-European root *\*h₂mewḱ-*. This root appears in Ancient Greek terms meaning "to tear" and "arrowtips," and possibly in Lithuanian *mušti* ("strike"). However, scholar Michiel de Vaan suggests the Latin and Greek terms could alternatively stem from "an otherwise unknown substrate language."

## English Entry

**Definition:** In botany and zoology, a *mucro* refers to "a pointed end, often sharp, abruptly terminating an organ," such as a leaf projection, the posterior tip of a cuttlebone, or the distal part of the furcula in springtails (Collembola).

The English term was borrowed from Latin beginning in the 17th century. Related terms include *mucronate* and *mucronule*.
```


### [2026-09-07T17:42:54.387Z] TOOL RESULT

```
# Proto-Indo-European *(s)mewk- Root

## Meaning
The root carries two related senses: "to let loose; to release" and "to slip away; to escape; to flee." It's classified as a perfective verb.

## Key Derived Terms
The page documents multiple grammatical formations, including:
- Thematic present: *sméwk-eti
- Athematic aorist: *méwk-t ~ muk-ént
- Desiderative: *méwk-se-ti
- Nasal-infix present: *mu-n-ék-ti ~ *mu-n-k-énti
- Reduplicated desiderative: *mí-muk-(h₁)se-ti
- Participle: *muk-tó-s ("released; discharged")

## Major Descendants
**Sanskrit** dominates the documentation with forms like *muñcáti* ("to free; to let loose") and *muktá* ("discharged; freed").

**Baltic-Slavic** shows Lithuanian *mùkti* and Latvian *mukt* ("to slip").

**Iranian** descendants include Sogdian forms related to clothing.

Notably, the page contains **no mentions of Avestan or any word specifically meaning "shoe,"** despite your question suggesting such content.
```


## [2026-09-07T17:43:07.047Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/moveo",
 "prompt": "Give the Latin entry moveō: etymology in full, including the PIE root reconstruction, cognates (Sanskrit, Avestan, Lithuanian), and descendants/derived English words."
}
```


## [2026-09-07T17:43:08.260Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/mu%C5%A1t%C3%AD%C5%A1",
 "prompt": "What is the reconstruction, meaning, etymology (any PIE root given or \"unknown\"), and descendants of Proto-Indo-Iranian *muštíš?"
}
```


### [2026-09-07T17:43:12.264Z] TOOL RESULT

```
# Latin Entry: moveō

## Etymology

**PIE Root:** The entry traces moveō to Proto-Indo-European "*m(y)ewh₁-" meaning "to move." The word developed through Proto-Italic "*moweō" before arriving at Latin moveō.

## Etymology Chain

The progression follows: "Proto-Indo-European *m(y)ewh₁-" → "Proto-Italic *moweō" → "Latin moveō"

## Cognates

The Wiktionary entry provided does not list Sanskrit, Avestan, or Lithuanian cognates. It focuses primarily on Romance language descendants rather than broader Indo-European comparisons.

## Key Descendants

**English:** move (via Old French movoir → Middle English moven)

**Romance languages:** 
- French: mouvoir
- Spanish: mover
- Italian: muovere
- Portuguese: mover
- Catalan: moure

## Derived English Words

The entry does not explicitly list English derivatives beyond "move" itself, though Latin-derived terms like "motion," "momentum," and "motor" are implicit in the related terms section.
```


### [2026-09-07T17:43:14.743Z] TOOL RESULT

```
# Proto-Indo-Iranian *muštíš

**Reconstruction:** *muštíš (masculine i-stem noun)

**Meaning:** "Fist"

**Etymology:** Derived from Proto-Indo-European *méws-ti-s ~ *mus-téy-s ("fist"), ultimately from the PIE root *mews- ("shut"). The word is cognate with Tocharian B maśce ("fist") and possibly Ancient Greek amustí. An alternative theory suggests origin from PIE *mewḱ- ("to scratch, tear"), though this etymology is considered dubious.

**Major Descendants:**
- Sanskrit: muṣṭí (मुष्टि)
- Avestan: mušti
- Persian: mošt (مشت)
- Tajik: mušt
- Central Kurdish: mist (مست)
- Georgian: mušṭi (borrowed)
- Ossetian: mustuḱ'i

The term shows consistent development across Indo-Aryan and Iranian branches with regular sound changes.
```


## [2026-09-07T17:43:25.385Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://bosworthtoller.com/023053",
 "prompt": "What Old English headword is this and what does it mean? Looking for the entry \"meo\" (a sock/shoe). Quote the entry."
}
```


## [2026-09-07T17:43:25.909Z] TOOL CALL #45: WebSearch

```json
{
 "query": "Old English \"meo\" \"meon\" shoe sock Bosworth Toller gloss"
}
```


### [2026-09-07T17:43:29.745Z] TOOL RESULT

```
The Old English headword shown is **módigian**, a weak verb meaning "to be or become proud, to glory, exult."

However, the entry you're looking for—"meo" (a sock/shoe)—is **not present** in this webpage. The page displays only the entry for "módigian" and does not contain any information about "meo."
```


### [2026-09-07T17:43:31.876Z] TOOL RESULT

```
Web search results for query: "Old English "meo" "meon" shoe sock Bosworth Toller gloss"

Links: [{"title":"Bosworth–Toller Anglo-Saxon - Apps on Google Play","url":"https://play.google.com/store/apps/details?id=net.mdln.englisc&hl=en"},{"title":"Thomas Northcote Toller","url":"https://en.wikipedia.org/wiki/Thomas_Northcote_Toller"},{"title":"Bosworth-Toller's Anglo-Saxon Dictionary online","url":"https://bosworthtoller.com/"},{"title":"An Anglo-Saxon Dictionary","url":"https://en.wikipedia.org/wiki/An_Anglo-Saxon_Dictionary"},{"title":"sock, n.¹ meanings, etymology and more | Oxford English Dictionary","url":"https://www.oed.com/dictionary/sock_n1"},{"title":"Sock - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/sock"},{"title":"Bosworth-Toller Anglo-Saxon Dictionary online","url":"https://bosworthtoller.com/3140"},{"title":"Old English Dictionary | Search Anglo-Saxon Words & Meanings","url":"https://oldenglishtranslators.com/old-english-dictionary"},{"title":"Bosworth-Toller Anglo-Saxon Dictionary – Medieval Digital Resources","url":"https://mdr-maa.org/resource/bosworth-toller-anglo-saxon-dictionary/"}]

The search results provide information about the Bosworth-Toller Anglo-Saxon Dictionary but do not contain specific information about the Old English words "meo" or "meon" or their glosses relating to shoes or socks. The results show that An Anglo-Saxon Dictionary is a dictionary of Old English compiled by Joseph Bosworth and Thomas Northcote Toller in the nineteenth century, and that it is today the largest complete dictionary of Old English. However, the specific entries for "meo" and "meon" are not included in these search results.

To find the specific glosses for these Old English words, you may want to consult the Bosworth-Toller dictionary directly at bosworthtoller.com or search for more specialized Old English linguistic sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T17:43:34.872Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://bosworthtoller.com/search?q=meo",
 "prompt": "List headwords matching \"meo\" — is there an entry méo / méon meaning a shoe, sock, or sole? Quote it."
}
```


### [2026-09-07T17:43:39.447Z] TOOL RESULT

```
# Entry for méo/méon

Yes, there is an entry for **méo/méon** meaning a shoe or sock. Here is the relevant quote:

"A shoe or sock covering the foot _Meó_ pedula, Wrt. Voc. i. 26, 2. _Meón_ pedulos"

The dictionary also notes that méon can refer to a covering for the foot, with references to related terms like "pedules, pars caligarum que pedem capit, a vampey: pedulus a pynson, or a sok."
```


## [2026-09-07T17:43:56.739Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E '.{0,150}(mütak|mutak|mūtak|mütan|mūtan).{0,250}' NYB_vol2_glossary.txt | head -20\necho \"=== PHD framudan/parmudan ===\"; grep -n -E 'framūdan|framud|parmān' PHD_mackenzie.txt | head",
 "description": "NYB mutak lookup"
}
```


## [2026-09-07T17:43:56.769Z] TOOL CALL #48: WebSearch

```json
{
 "query": "Old English \"méo\" pedule etymology Holthausen shoe sock Germanic"
}
```


### [2026-09-07T17:43:59.976Z] TOOL RESULT

```
ugrep: error: error at position 113
k|mütan|mūtan)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,250}
                      exceeds complexity limits___/


=== PHD framudan/parmudan ===
3199:   ...... framudan: put to use.
7198:order (v.) framudan; win(n)ardan.      particular ewazig, waspuhragan; in---
```


### [2026-09-07T17:44:05.981Z] TOOL RESULT

```
Web search results for query: "Old English "méo" pedule etymology Holthausen shoe sock Germanic"

Links: [{"title":"sock, n.¹ meanings, etymology and more | Oxford English Dictionary","url":"https://www.oed.com/dictionary/sock_n1"},{"title":"sock - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/sock"},{"title":"Shoe - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/shoe"},{"title":"Sock - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/sock"},{"title":"The History & Development of Socks","url":"https://www.heddels.com/2023/09/the-history-development-of-socks/"},{"title":"Sox - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/sox"},{"title":"Boots (or rather, shoes) on the ground | OUPblog","url":"https://blog.oup.com/2026/09/boots-or-rather-shoes-on-the-ground/"},{"title":"Ferdinand Holthausen","url":"https://en.wikipedia.org/wiki/Ferdinand_Holthausen"},{"title":"Shoe etymology in English","url":"https://cooljugator.com/etymology/en/shoe"}]

I found relevant information about sock etymology and Ferdinand Holthausen, but the search results don't specifically contain information about Old English "méo" and its connection to pedule, shoe, or sock. The search results do confirm that Ferdinand Holthausen was a German scholar of English and old Germanic languages, which is relevant to your query.

The results show that Old English socc comes from Latin soccus, a light low-heeled shoe or slipper, and shares the same origin as Old High German soch, soc, and other Germanic cognates.

However, the specific etymology of Old English "méo" and its relation to "pedule" that you mentioned in your search query does not appear in these results. If you're looking for Holthausen's specific etymological work on this term, you may need to consult his scholarly publications directly or search for more specialized etymological references.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T17:44:13.135Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['NYB_vol2_glossary.txt','ISS_alt_DKS.txt','PHD.txt','UNV.txt','SNS.txt']:\n    try: t=open(f,encoding='utf-8',errors='replace').read()\n    except: continue\n    for pat in ['mūtak','mutak','mütak','parmūt','parmut','parmüt']:\n        for m in re.finditer(pat,t):\n            print('###',f,pat)\n            print(t[max(0,m.start()-350):m.start()+350].replace('\\n',' '))\n            print()\nEOF",
 "description": "Search local Pahlavi sources for mutak / parmutan"
}
```


### [2026-09-07T17:44:14.599Z] TOOL RESULT

```
### NYB_vol2_glossary.txt mūtak
hac tan xYarrah from his (viz. Zartuxšt's) bodily splendour 377-8; — taking up an encl. -§ at the beginning of the sentence, after a part of the sen- tence which carries a lengthy attribute: api-š hamäk damik i-š apar rāh bit | aš *perävanihit kart 3316-17; — after an ad- verbial phrase beginning the sentence: adak apar pat jamän | aš hanjamanénit mūtak :61° (where aš anticipates mūtak, cf. s. v. -š). — 2. to introduce the apo- dosis (as api-$, adak-i8): after kakar 31?! ; after ka 327. 3319. 341. 565. 5717. 924. after a relative clause 3219, 9824, 100?7— 101?. — Probably identical with MPrthPrs š, written as an independent w. with two dots above (another explanation of this § v. A-H III, Gl

### NYB_vol2_glossary.txt mūtak
rtuxšt's) bodily splendour 377-8; — taking up an encl. -§ at the beginning of the sentence, after a part of the sen- tence which carries a lengthy attribute: api-š hamäk damik i-š apar rāh bit | aš *perävanihit kart 3316-17; — after an ad- verbial phrase beginning the sentence: adak apar pat jamän | aš hanjamanénit mūtak :61° (where aš anticipates mūtak, cf. s. v. -š). — 2. to introduce the apo- dosis (as api-$, adak-i8): after kakar 31?! ; after ka 327. 3319. 341. 565. 5717. 924. after a relative clause 3219, 9824, 100?7— 101?. — Probably identical with MPrthPrs š, written as an independent w. with two dots above (another explanation of this § v. A-H III, Gloss s. v.; ? in a fragmentary con

### NYB_vol2_glossary.txt mūtak
des 6817-18; the work of Ahriman is ~ u kén u anästeh 7822; ~ u ken räd 14%; - personified as a demon, one of the chief evil powers: ~ dev 6123: equal to Ahri- man 68%; in company with Az 103°; www.parsianjoman.org | col wok 7% hesm 100 ho the opposite of Vahuman 654-5; Srēš his chief adversary 665. 7711, 2516, 2814 v.s. v. distak; — his epithets: mūtak and tanäpuhrak 619%; zürdrus 7211-12, 103977; v. these ws. — Av. (35 sq.) aēšma- (Asmodatos, Book of Tobit 3:8 Av. ačšmo.dačva-); MPrth ‘smg’n ‘devils of wrath’; MPrs xysm; Paz. NP rašm, zism. — Paz. hčšmakan [hyšmkn'] angry 1422. abstr. x(a)šmagami Antià 1235. hešmēh [hšmyh] an outburst of fury 6815. — Probably only kēšm + the indef. art. -€

### NYB_vol2_glossary.txt mutak
sensual plea- sure’, (280) ahömusta- < *a-ham-musta- ‘disgusting’. mustömand [mwst’wmnd] outraged, vio- lated, pl. cas. obl. ~-dn 8?9. — ‘Exposed to must? (g. v.); NP mustmvand ‘poor, wretched’. Cf in active sense must-kar ‘defecting from (hac) his sovereign, re- bellious’ KnS IV, 2. mütak [mwtk'] *destructive, of Hēšm 619. — FrO XI: mruta (Av.) = mutak; Vd. 272 mütak of the winter, with the www .parsianjoman.org | col wok mitak gl. kū ciš tapāh kunēt ‘that is: it destroys everything’, rendering Av. (1197) mrüra-. *mutfan [mwtpn'] *a pair, a couple: ~ kartan to come together as a married couple 1012. — I believe it is the Av. (1182) mi@wana- ‘forming a pair (man -n (inscr., Pers) encl. pers.

### NYB_vol2_glossary.txt mutak
Maryu (Mouru-): Marv maršo.kara: "maškar mas-, Masan-: mas masya-: mahik mašya-: mart mafra-: mānsr mafra-sponta: mahras- pand (fra-)may-: framātan (ni-ymāy-: ni-mütan (pati-ymāy: patmān mazdayasna-: mazdēsn mazga-: mazg meroždā-, meroždika-: āmuržītan midaoxta- (mi€oxta): mitöxt miOra-: mihr miOwana-: *mutfan mižda-: mizd moyu-tbis-: magü mrura-: mutak načma-: nčm načza: nčzak nàirl- (nàirikà-): näirik Nairyo.sagha: Narsah, Nčrosang apa-nam-: ayaftan fra-nam-: franaftan naman-: nam namra.vaxs-: *a-namr- tom napat-: nap nas-: anä-vinast Inas-: vinasitan ?nas-: panäh naska-: nask nasu-: nasai (ava-)nay-: Önitan nazdista-: nazdist nazdy6: nazd nomah-: namše nomata-: namat nidäti-: nihan nčit: 

### NYB_vol2_glossary.txt mütak
form. murvčeak [mwlwyck'] chicken 92%. — Demin. of !murv. murv-niš [mwlwnyš] soothsayer fore- telling the future by the flight or other tokens of the birds, an augur, pl. cas. obl. ~-dn 535. — murv + niš, the pres. st. of MPrs nyyšydn, nyyš- ‘to see’ (A-H I, Verbum 168); cf nišan. Musrkin [mwslk?n'] a people 1154, - Arab masrugän; Cat. 71-73. 134 mütak must [mwst', inscr. mwsty] violation, outrage: ~ u gilak 761; api-š ... must u dróg andar nést and there is no violation and no lie (fraud) in it (= in the passage, i.e., to be feared when passing over the bridge) F:7; [~ u adātihā i-Sän patiš kunénd violation and iniguities which they commit against them (viz. water and fire) JN 16%]. — Paz.

### NYB_vol2_glossary.txt mütak
te *to be delighted', whenee Av. (1109) maodanö.kara- ‘affording sensual plea- sure’, (280) ahömusta- < *a-ham-musta- ‘disgusting’. mustömand [mwst’wmnd] outraged, vio- lated, pl. cas. obl. ~-dn 8?9. — ‘Exposed to must? (g. v.); NP mustmvand ‘poor, wretched’. Cf in active sense must-kar ‘defecting from (hac) his sovereign, re- bellious’ KnS IV, 2. mütak [mwtk'] *destructive, of Hēšm 619. — FrO XI: mruta (Av.) = mutak; Vd. 272 mütak of the winter, with the www .parsianjoman.org | col wok mitak gl. kū ciš tapāh kunēt ‘that is: it destroys everything’, rendering Av. (1197) mrüra-. *mutfan [mwtpn'] *a pair, a couple: ~ kartan to come together as a married couple 1012. — I believe it is the Av. (

### NYB_vol2_glossary.txt mütak
ure’, (280) ahömusta- < *a-ham-musta- ‘disgusting’. mustömand [mwst’wmnd] outraged, vio- lated, pl. cas. obl. ~-dn 8?9. — ‘Exposed to must? (g. v.); NP mustmvand ‘poor, wretched’. Cf in active sense must-kar ‘defecting from (hac) his sovereign, re- bellious’ KnS IV, 2. mütak [mwtk'] *destructive, of Hēšm 619. — FrO XI: mruta (Av.) = mutak; Vd. 272 mütak of the winter, with the www .parsianjoman.org | col wok mitak gl. kū ciš tapāh kunēt ‘that is: it destroys everything’, rendering Av. (1197) mrüra-. *mutfan [mwtpn'] *a pair, a couple: ~ kartan to come together as a married couple 1012. — I believe it is the Av. (1182) mi@wana- ‘forming a pair (man -n (inscr., Pers) encl. pers. pron. 1 p. pl.

### ISS_alt_DKS.txt mütak
. Base nä-, IE Pok. 754, O.Ind. ndtha- 'protector', Greek óvivnut ‘serve, be useful’. Possibly Sogd. ''2'2, if read "n't (КТ vt os) ‘exactly’. ánaba 'moistened (?)' їп 84-53 па-йпаһйт dui priyi татнагӣ gviha rüm tcerai ‘it (a paimdaka-poultice) must be made without moistening with two frZya-measures of butter (cow oil)”; Ш 92:237 u na-ánaha anarva mütaká ісетӣ ‘апа it (the paindaka-) must be made with un- moistened unbroken máfaka-plant'. Possibly compound (with na- for an-) to base naf- (nap-, nabh-) 'be moist’, Av. aiwi-nap- 'pour upon’, nepta- 'moistened', Zor.P. nam, namb ‘moist’, nambet, nambitan (gloss to Av. haek- t pour out’), naft, N.Pers. nam ‘moist’. To IE Pok. 315-16 enebh- ‘mois

### ISS_alt_DKS.txt mütak
 stroum, O.Engl. str&am, Lit. sraviù, sravéti ‘flow’, O.Slav. struja 'stream- : ing'. For -laiga-, see also välaiga ‘citron’, Оаа. mütulunga-, Zor.P. vatarang; palaigä, BS lw palanka- ‘cross-legged’. māva ‘basic matter (?)', Manj. 8o ttyā māva byadi bvāña 'the basis of these (klesa-afflictions) is to be known to be incuria' (=BŠ pramada- to Zor.P. mütak ‘hbase’, mütak-war 'particular', matakdar (m'tyyl) 'steward', Armen, lw matakarar, N.Pers. mayah; rather than mäta 'mother' note ш 20, 163-4 prajüa-parama baysünd mata ' the wisdom-perfection mother of Buddhas’. mnáva ‘mother’, see mata, Manj. 243 m(a)va, K 15211 тӣой rīnä ‘mother and queen’; acc. sing. K 47:54 тйшата, āva ' bee, fly', see ma

### ISS_alt_DKS.txt mütak
. str&am, Lit. sraviù, sravéti ‘flow’, O.Slav. struja 'stream- : ing'. For -laiga-, see also välaiga ‘citron’, Оаа. mütulunga-, Zor.P. vatarang; palaigä, BS lw palanka- ‘cross-legged’. māva ‘basic matter (?)', Manj. 8o ttyā māva byadi bvāña 'the basis of these (klesa-afflictions) is to be known to be incuria' (=BŠ pramada- to Zor.P. mütak ‘hbase’, mütak-war 'particular', matakdar (m'tyyl) 'steward', Armen, lw matakarar, N.Pers. mayah; rather than mäta 'mother' note ш 20, 163-4 prajüa-parama baysünd mata ' the wisdom-perfection mother of Buddhas’. mnáva ‘mother’, see mata, Manj. 243 m(a)va, K 15211 тӣой rīnä ‘mother and queen’; acc. sing. K 47:54 тйшата, āva ' bee, fly', see mata, má. mävu ‘o
```


## [2026-09-07T17:44:29.144Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('ISS_alt_DKS.txt',encoding='utf-8',errors='replace').read()\nfor pat in [\"base mūr-\",\"mvīr\",\"mür- ‘move\",\"prmwt\",\"Zor.P. mūt\",\"framūta\"]:\n    for m in re.finditer(re.escape(pat),t):\n        print('###',pat)\n        print(t[max(0,m.start()-600):m.start()+700].replace('\\n',' '))\n        print()\nEOF",
 "description": "DKS base mur- move"
}
```


### [2026-09-07T17:44:30.633Z] TOOL RESULT

```
### mvīr
, kudi, kūdai ' hole’. mvar- 'to move’, K 109:314 khu ja йїа mvara nai u nai шї pachaisidi ‘аз the sky (BS àkaía-) has no movement and the wits do, not work’, See mür- ‘to move’, and mvir-. mvarye ‘way of acting’ Manj. 291 së mvarye tta hasta bvàría ' this course of action is so to be known as the best’, Here mvarye ' movement, behaviour, course’ glosses BS caryü ‘movement, course of action’, hence from base mvar-, older mür- 'to move’, see also zara ' movement’. In form muarye is from older *müriya- or *mürikà- with nom. sing. -ye. See mür-, vamüda-. myvir- ' to move’, Sid. 150r3 khoysamdā u mvīramdā vijisde ‘he sees moving and shifting things’, BS calavila-, Tib. 8-yo-ba dau lo-lon-por srau-ba yin-no ; Мап). 92 samvadrra ne пе khauysda na ja và тоға ' the sea does not move nor make motion’; Manj. 31 cu yadrradd mvirau hhauysda ‘what framed thing moves and (-au «-e u) shifts’ (the body as a yantra- ‘ ате’); Sid. r44v4 simakyi bañāñä khu và ni mvire ' the simakya-ligature (BS sima-) is to be bound so that it does not move', Tib. mi mgul-bar dban- du byas-te (mgul' move’, dban ' power"). From mvar-: mür- müry- »muir-, see mür-, vamida-. mvaisá 'sometimes, now. . .now. . .', II 81-41, see multa. mveásdalalaka ‘almoner or the 1ке", “11145; sob1,3; see s.v. iraudrii ‘pragmaticus’. Po

### mür- ‘move
s-imis, I. üada- ymys ‘skilled; skilled work, poetry’ (for second syllable -i-, -у- « -à-, note also D. äntäsun, L. äntysyn ‘succeed’; D. dnt'irun I. dnt'üryn 'drive away"). See also hamas- 'to enjoy' (K. 73:38). vamáda ' weary', 1t 5:75 (see vamiida-) dyadic, sta zamada ‘tired, weary’. See also pümiida-. уай (or va тй), JS 29v #rhá vamiü valmīkä ste ysürri ‘well (the poet) Vülmiki praised the golden bone ( — body) of the golden goose (Pali suvanna-vanna hamsa-)'. See s.v. mū for cognates. vamüda- 'move away Гот’, 2 24'116 Ёй vamüdandd cakkrä pvastañä ‘all evaded the terrible discus’, to base mür- ‘move’, see mvir- < *mür-y-, with -r- to base Av, imyav-, :miv- 'remove', O.Ind. mivati. ТЕ Pok, 743 meu- ‘thrust away', O.Ind. mio-:mü-, mivati, müta-, Av. amuyamna-, O.Ind. mürd- 'pressing, hastening’, Greek &yeu-, брери-, vea, Lat, moueó, mótus, Lit. тацји, mduti ‘put on (ring on finger)’, vamur- 'destroy, remove’, dyadic, JS 32v2 sümmam khenām vamurüke jenüke 'destroyer, annihilator of enemies’ laughs; Ir 54:13 harbifüp rrümdam hye vamu- така ' destroyer of all kings’. See base mür- in vamüda-. vamurr- ‘crush’, Bed 52v1 Alesam hauva tua bid vamu- rrdá yinime 'I can crush the whole power of the klesa- afflictions’, BS Alefa-balam. parimardayamáünah. From base mar- 'crush' with presen
```


## [2026-09-07T17:44:42.876Z] TOOL CALL #51: Bash

```json
{
 "command": "ls site/pages/339.jpg 2>/dev/null; pdftoppm -f 339 -l 339 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg339 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Render PDF page 339"
}
```


### [2026-09-07T17:44:44.681Z] TOOL RESULT

```
site/pages/339.jpg
total 18992
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 13:44 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb   153966 Sep  7 13:44 bqt2014_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:42 navak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3021 Sep  7 13:42 navak.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    63922 Sep  7 13:44 pg339.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:44 pg340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75149 Sep  7 13:40 pg342.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60735 Sep  7 13:42 pg344.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168870 Sep  7 13:42 pg346hi.png
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


## [2026-09-07T17:44:48.496Z] TOOL CALL #52: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg339.png"
}
```


### [2026-09-07T17:44:48.880Z] TOOL RESULT

```

```


## [2026-09-07T17:44:48.878Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T17:45:12.456Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('ISS_alt_DKS.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r\"mūr- ' ?to move|mür- 'to move'\",t):\n    print('###',m.start())\n    print(t[max(0,m.start()-200):m.start()+2000].replace('\\n',' '))\n    print()\nEOF",
 "description": "Print DKS mur- entry"
}
```


## [2026-09-07T17:45:12.514Z] TOOL CALL #54: WebSearch

```json
{
 "query": "Pahlavi \"parmūtan\" OR \"parmutan\" move Bailey Indo-Scythian Studies"
}
```


### [2026-09-07T17:45:13.729Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-07T17:45:20.000Z] TOOL RESULT

```
Web search results for query: "Pahlavi "parmūtan" OR "parmutan" move Bailey Indo-Scythian Studies"

Links: [{"title":"H.W. Bailey (Author of Indo-Scythian Studies)","url":"https://www.goodreads.com/author/show/1407056.H_W_Bailey"},{"title":"H. W. Bailey (ed.): Indo-Scythian studies; being Khotanese texts, Vols. iv–v. viii, 192 pp., 2 plates; xiii, 395 pp. Cambridge: University Press, 1961, 1963. 50, £6. | Bulletin of SOAS | Cambridge Core","url":"https://www.cambridge.org/core/product/identifier/S0041977X00100497/type/journal_article"},{"title":"BAILEY, HAROLD WALTER - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/bailey-harold-walter-1/"},{"title":"Amazon.com: Indo-Scythian Studies: Being Khotanese Texts Volume VII: 9780521118736: Bailey, H. W.: Books","url":"https://www.amazon.com/Indo-Scythian-Studies-Being-Khotanese-Texts/dp/0521118735"},{"title":"Amazon.com: Indo-Scythian Studies: Being Khotanese Texts Volume V: Volume 5: 9780521119948: Bailey, H. W.: Books","url":"https://www.amazon.com/Indo-Scythian-Studies-Being-Khotanese-Texts/dp/0521119944"},{"title":"Bailey, H.W. - KHOTANESE.ORG","url":"https://articles.khotanese.org/bailey,-h.w/"},{"title":"Numismatic References, Indo-Parthian - Indo-Scythian","url":"https://grifterrec.rasmir.com/reference/reference-indoscy.html"},{"title":"Chronological Bibliography - KHOTANESE.ORG","url":"https://articles.khotanese.org/chronological-bibliography/"}]

The search results provide information about H.W. Bailey and his Indo-Scythian Studies work, but they don't contain specific information about the Pahlavi word "parmūtan" or "parmutan" and its meaning related to "move." The results show that H.W. Bailey studied and interpreted the northern area of Indian Buddhist culture in the Khotan Saka documents of Central Asia dated between the fifth and tenth centuries AD, but the specific linguistic detail you're asking about is not included in these results.

To find information specifically about the word "parmūtan"/"parmutan" and its meaning in Bailey's Indo-Scythian Studies, you may need to consult the actual texts directly or search for more specialized academic sources that discuss specific Pahlavi vocabulary from Bailey's work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T17:45:45.255Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 mucro/mušti ===\"; grep -n -o -E '.{0,200}mucro.{0,300}' incoming/WLD/WLD_Bd2_pages.txt | head -5\necho \"=== WLD Bd2 miv ===\"; grep -n -o -E '.{0,200}mivati.{0,300}' incoming/WLD/WLD_Bd2_pages.txt | head -5",
 "description": "Grep Walde-Pokorny Bd2"
}
```


## [2026-09-07T17:45:46.576Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN fist ===\"; grep -n -o -E '.{0,150}\\bfist\\b.{0,250}' SYN.txt | head -8\necho \"=== SYN move ===\"; grep -n -o -E '.{0,100}4\\.2[0-9] .{0,120}' SYN.txt | head -5",
 "description": "Grep Buck for fist"
}
```


### [2026-09-07T17:45:50.690Z] TOOL RESULT

```
=== WLD Bd2 mucro/mušti ===
ugrep: error: error at position 83
bf][\x80-\xbf]*){0,300}
                       \___exceeds complexity limits


=== WLD Bd2 miv ===
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,300}
                        \___exceeds complexity limits
```


### [2026-09-07T17:46:06.642Z] TOOL RESULT

```
=== SYN fist ===
5458:l ‘bone, knuckle’ (> Dan. knokkel, knogle ‘bone’), ME knokel, NE knuckle, NHG knéchel ‘knuckle’: ON knjikr ‘round summit’, Lith. gniaudzti ‘close the fist’, etc. Walde-P. 1.582. Falk-Torp 69. The meaning ‘knuckle’ is the more general and earlier, whence ‘bone’ only by later extension (not ‘knuckle’ from ‘bone’, asin NED).
6153:of the words for ‘hand’ are from roots meaning ‘seize, take, collect’ or the like. Some are from words mean- ing orig. a part of the hand, ‘palm’ or ‘fist’. Several are without any clear root connection. For extension of ‘hand’ to ‘arm’, cf. 4.31.
6167:Br. dourn = Corn. dorn, W. dwrn, Ir. dorn ‘fist’ : Lett. dire, daris ‘fist’, orig. ‘fist’ in striking, fr. dirt ‘sting, thrust’
6168:(cf. Lat. pugnus ‘fist’ : pungere ‘sting’, orig.
7028:6. ON fisa, Dan. fise, Sw. fisa, OE sb. fisting, ME vb. fyste (cf. NED s.v. fist, sb.?, vb.?), Du. veesten, MHG visten, visten, NHG fisten, of imitative orig., prob. through ‘blow’ (cf. also Lat. spirare ‘breathe’, ChSIl. piskati ‘whistle’). Walde-P. 2.11. Falk-Torp 220 f.
12821:W. dyrnu, Br. dourna, orig. ‘beat with the hand’, fr. W. dwrn ‘fist’, Br. dourn ‘hand’ (4.33).
18103:Pol. pehaé, Russ. pichat’ : ChSl. pi- chati ‘strike’ (with the fist or the foot), Boh. pichati ‘prick’, Skt. pis-, Lat. pinsere ‘pound, crush’. Walde-P. 2.1. Ernout-M. 770f. Briickner 401.
18890:maim, f Btagp, Clutch, ete . glac ‘half-open fist,
=== SYN move ===
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,120}
                            \___exceeds complexity limits
```


## [2026-09-07T17:46:15.433Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/s.py <<'EOF'\nimport sys,re\nf=sys.argv[1]; pats=sys.argv[2].split('|'); w=int(sys.argv[3]) if len(sys.argv)>3 else 300\nt=open(f,encoding='utf-8',errors='replace').read()\nfor p in pats:\n    for m in list(re.finditer(re.escape(p),t))[:4]:\n        print('###',f,p,m.start())\n        print(t[max(0,m.start()-w):m.start()+w].replace('\\n',' '))\n        print()\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/s.py incoming/WLD/WLD_Bd2_pages.txt 'mucro|mušti|musti-|mivati' 400",
 "description": "Search Walde-Pokorny Bd2"
}
```


### [2026-09-07T17:46:16.812Z] TOOL RESULT

```
### incoming/WLD/WLD_Bd2_pages.txt mucro 964181
Gruppe B. denkt Fick aaO. an Beziehnng zu 7ncii- „schieben“).   Vgl. bes* Johansson PBrB. 15,235, Zupitza Gutt. 136, t3Sf. (Lit), 164.  ineuk- „kratzen, ritzen".   gr.   duvyMXm   *                       at dxideg tcov ^sko)v Tiagd to djuvoosiv Hes.,           djLivoaco, att.  d/LWiTco „ritze, zerkratze“,             Schvamme*^, d/uv^j^og ds., djuvy/na, djbtvyjnog „das Zerraufen (der Haare)“; lat mucro „scharfe Spitze, z. B. der Zahne, der Klanen, der Pflugschar, eines Kometen, bes. des Speeres oder Schwertes, dieses selbst'; vielleicht lit musdi „schlagen“ (wenn ursprgl. etwa „gewalttatig reiBen, verkratzen“). Curtins^ 546, weitere Lit bei Vf. LEWb.^ 497 {miicro lycht besser nach Zupitza GG. 138f. zu anord. smjuga ,;hindurchkriechen, schliipten, auch durchbohren“).    Lit muszti konnte au

### incoming/WLD/WLD_Bd2_pages.txt musti- 964638
flugschar, eines Kometen, bes. des Speeres oder Schwertes, dieses selbst'; vielleicht lit musdi „schlagen“ (wenn ursprgl. etwa „gewalttatig reiBen, verkratzen“). Curtins^ 546, weitere Lit bei Vf. LEWb.^ 497 {miicro lycht besser nach Zupitza GG. 138f. zu anord. smjuga ,;hindurchkriechen, schliipten, auch durchbohren“).    Lit muszti konnte auch ursprgl. „boxen“ gewesen sein; dann vielleicht zu ai. musti-h,            ,,Faust“ (Uhlenbeck KZ. 39, 260 f. GiintertsKZ. 45, 193 ff.,                                                               ;   Ankniipfung an 7niis „Maus, Muskeh' ist bei der Seltenheit von auf Sub- stantiven beruhenden ^ -Nomina                             2              —                                       vergleichbar ware hochstens der Typus ir. elit ,,Reh“ aus
```


## [2026-09-07T17:46:29.085Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/s.py\npython3 $S incoming/WLD/WLD_Bd2_pages.txt 'wegschieben' 500 | head -40",
 "description": "WLD meu- wegschieben"
}
```


## [2026-09-07T17:46:30.494Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/s.py\nfor f in FSD_vol3.txt WEB_vol1.txt KLN_1966.txt SKT.txt; do python3 $S $f 'mucro' 300; done | head -40",
 "description": "Search English dicts for mucro"
}
```


### [2026-09-07T17:46:30.529Z] TOOL RESULT

```
### incoming/WLD/WLD_Bd2_pages.txt wegschieben 2120236
  Bed.-Umfang die wohl verwandten (Persson Wzerw. 90, Wood Min.     21, 228) Wzln. sqeud- „werfen, schieBen", skai- ds.; dagegen liegt     qseiibk- .jSchwanken" in der Bed. weiter ab, als daB Yereinigung der     Anlaute durch Umstellung zu befiirworten ware.    Lit. skiibti „eilen", skuhinti „beeilen“, skiihus, skubnis ..flink, eilig"    (aber abg. skubq^ skubati „zupfen,                reiBen" weiB ich in der Bed. nicht zu ver- einigen;    s.   u.   sqeup- „Buscheb Schopf");    got. afskiuban „wegschieben, verstoBen", ags. see ofan  und salfan „schie- ben", ahd. scioban „schieben" (hat nhd. auch die Bed. „eilig gehn"), aisL skiifuj -ada und skyfa „schieben, fortstofien", Intensiv mhd. nhd. schupfen^ norw. mdartl. sktippa ds., ahd. sciipha, scopha ,,Schaukelbrett" ; ahd. scu- f{a)la „Schaufel"             (kein ganz sicherer Zeuge fur eine idg. Wzf. sqeu-p-; vielleicht aus *skuh-pld assimiliert), scubla ds., ags. scofl ds.,                  mnd. scliuppe^ ndl. schop       f.     aus -j
```


### [2026-09-07T17:46:32.240Z] TOOL RESULT

```
### FSD_vol3.txt mucro 1226450
largement of tho head m«g''a-lo-ce-pha'li-ai.— meg''a-loe'er-OB, n. Paleon. The extinct Irish elk — meg'^lo-cbi'roUB, a. AnaX & Zool Having large liuiids or homologous ports — meg^a- lo-co-nid'i-um, n I-i-a. pl.\ Sot. A noii-sexual sporo In fungi. Intermediate In size tyetweeu a mlcroctmidlum and a mucrocutiUlluiii — meg''a-l(i-c'or'D«-a, n Unusual slse of llic cornea of the eve — meg'a-io-cyto, b A large red blood-corpuscle found lii hutniin blood In cases of anemia. - meg’'a-l«»-ry-to'ai8, n Pathol The morhUl state in which unusually large red blood-corpuscles are present ' - nieg^a-lti-dac-

### FSD_vol3.txt mucro 2755479
 The hemlock-spruee (Tsuga mertensiana) of the Paclflc States 2. lL.ocal, Eng ] Hame as lovaur - m. -herring, n Tho Rocky mountain whltcflsh (Coregonus wiltiamsoni) ~ m. -hickory* n A largo hardswood acacia (Acacia pennlnervis), native to Aus- tralia — m. -holly* R A much-branched shrub (Jlieioidez mucroitata) of the holly family, with dry, red berries- m.- hummer* r. a humming-bird (genus Oreotroehilus) ot great altitudes - m.-lruu wort* n A European mint (Stderitis montana) — m.-Ivy* n Hame as mountain* laurel -m.-larrh, r. a Rocky mounuln larch (Larix lyaUit) — m.-laurel, a. 1. In the easte

### FSD_vol3.txt mucro 2836799
astrium of un Insi'ci when dirrcrcniliucd by elevation H«* Ulus under oiiTi-rTKD (2> Bot A short, straight, stiff, and sharp tmliil, os of a leaf IL . sharp point.] ttitt'*cn»-na'tlont. inu'ena-nate, l min'kro-nct. 2 mfi'ero-nAt, a Ending al>- ruptly In u short, sharp point or spine, tlptNHl with a mucro, as. a rnurronate shell or leaf (< J, mueronatun < muero, sharp iKilnt) mu'cr»-nat''edt; mu^criHUirer-ouatt tiiu-croii'l-ronnt.- ttiu'cro-nate*l|, ndc - niu-cnin'u- latts a. Minutely mucronuto. inu-cron'u-la-ti>UNL niu'cro-niile, l niliTkro*nini, 2 mfl'cro'iini.n A small mucro. mu'cu-lcntt* a 

### FSD_vol3.txt mucro 2836988
'ena-nate, l min'kro-nct. 2 mfi'ero-nAt, a Ending al>- ruptly In u short, sharp point or spine, tlptNHl with a mucro, as. a rnurronate shell or leaf (< J, mueronatun < muero, sharp iKilnt) mu'cr»-nat''edt; mu^criHUirer-ouatt tiiu-croii'l-ronnt.- ttiu'cro-nate*l|, ndc - niu-cnin'u- latts a. Minutely mucronuto. inu-cron'u-la-ti>UNL niu'cro-niile, l niliTkro*nini, 2 mfl'cro'iini.n A small mucro. mu'cu-lcntt* a Resembling mucus, slimy, viscid, glairy. Mu*cu'ua, 1 mlij-kl 'iih, ;j m i-rtiMia. n llirazll ) BtH A genus of tropical climbing nr twining plants of the beau fuiiillv, with trlfoiloluic Icu

### KLN_1966.txt mucro 6196640
cus. mucosity,  n.  —  Formed  with  suff.  -ity  fr.  L. mucosus,  ‘slimy,  mucous’,  fr.  mucus.  See  prec. word.  , mucoso-,  combining  form  meaning  ‘mucous  . L.  mucoso-,  fr.  mucosus.  See  next  word, mucous,  adj.  —  L.  mucosus,  ‘slimy,  mucous  ,  fr. mucus.  See  mucus  and  -ous. mucro,  n.,  a  sharp  point  or  tip  (bot.  and  zool.)  — 1011 Mugilidae L.  mucro,  ‘point  of  a  sword’,  standing  for  *mu- kros,  ‘pointed’,  and  possibly  cogn.  with  Gk.  ap.u- xaXxi  (Hesychius)  ‘arrowheads’,  a|xuaaco, Att.  ajiuTTw  (for  *a[x6xici) ) ,  ‘I  scratch,  tear’, and  wi

### KLN_1966.txt mucro 6196720
ous’,  fr.  mucus.  See  prec. word.  , mucoso-,  combining  form  meaning  ‘mucous  . L.  mucoso-,  fr.  mucosus.  See  next  word, mucous,  adj.  —  L.  mucosus,  ‘slimy,  mucous  ,  fr. mucus.  See  mucus  and  -ous. mucro,  n.,  a  sharp  point  or  tip  (bot.  and  zool.)  — 1011 Mugilidae L.  mucro,  ‘point  of  a  sword’,  standing  for  *mu- kros,  ‘pointed’,  and  possibly  cogn.  with  Gk.  ap.u- xaXxi  (Hesychius)  ‘arrowheads’,  a|xuaaco, Att.  ajiuTTw  (for  *a[x6xici) ) ,  ‘I  scratch,  tear’, and  with  Lith.  musu,  milsti,  ‘to  strike’. Derivatives:  mucron-ate(d),  adj.,  mu

### KLN_1966.txt mucro 6196995
.)  — 1011 Mugilidae L.  mucro,  ‘point  of  a  sword’,  standing  for  *mu- kros,  ‘pointed’,  and  possibly  cogn.  with  Gk.  ap.u- xaXxi  (Hesychius)  ‘arrowheads’,  a|xuaaco, Att.  ajiuTTw  (for  *a[x6xici) ) ,  ‘I  scratch,  tear’, and  with  Lith.  musu,  milsti,  ‘to  strike’. Derivatives:  mucron-ate(d),  adj.,  mucron-ate-ly , adv.,  mucron-ation,  n. mucus,  n.,  a  viscid  secretion  of  the  mucous  mem¬ branes.  —  L.  mucus,  ‘mucus  of  the  nose’,  rel.  to mucor,  ‘mold,  moldiness’,  mungere,  emungere, ‘to  blow  the  nose’,  fr.  I.-E.  base  *(s)meuq-, *(s)meug-,  ‘to  sl

### KLN_1966.txt mucro 6197018
  mucro,  ‘point  of  a  sword’,  standing  for  *mu- kros,  ‘pointed’,  and  possibly  cogn.  with  Gk.  ap.u- xaXxi  (Hesychius)  ‘arrowheads’,  a|xuaaco, Att.  ajiuTTw  (for  *a[x6xici) ) ,  ‘I  scratch,  tear’, and  with  Lith.  musu,  milsti,  ‘to  strike’. Derivatives:  mucron-ate(d),  adj.,  mucron-ate-ly , adv.,  mucron-ation,  n. mucus,  n.,  a  viscid  secretion  of  the  mucous  mem¬ branes.  —  L.  mucus,  ‘mucus  of  the  nose’,  rel.  to mucor,  ‘mold,  moldiness’,  mungere,  emungere, ‘to  blow  the  nose’,  fr.  I.-E.  base  *(s)meuq-, *(s)meug-,  ‘to  slip;  slippery,  slime’,
```


## [2026-09-07T17:46:42.067Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'MOSHT\\|MUZE\\|MUZEH\\|MOOZ' incoming/ARY/ARY_latin_index_pages.txt | head -10\necho \"=== ARY pages مشت ===\"; grep -n 'مشت' incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY pages موزه ===\"; grep -n 'موزه' incoming/ARY/ARY_pages.txt | head -10",
 "description": "Grep Aryanpur"
}
```


### [2026-09-07T17:46:42.138Z] TOOL RESULT

```
13436:MUZE (BOHEMIAN) gua y MAN HENGLISH) .5J6it
13827:MOG, MOSHTI MAGICE, MAGUS ALATIN) ya
=== ARY pages مشت ===
116:نکات زیر درستی دیدمان فوق را مورد تردید قرار می‌دهد: ۱- کردستان وارمشتان و نواحی
172:زبان‌های گوناگون شد. (وجود واژه‌های مشترک میان هند و اروپایی و زبان سامی آغازین
221:نبست. دلیل دیگر» واژه‌ی «ماره در اکثر زبانهای «ستتم» مشترکك است (لاتین: ۵1۸712 ایرلندی
293:است. واژه‌های همریشه‌ی دیگر نیز در شناخت ماهیت هند و اروپائیان سودمنداند: واژه‌های مشترک
521:از سرچشمه‌ی مشترکی ناشی شده‌اند که شاید امروزه از بین رفته باشد. دلیل مشابهی :
522:وجود دارد که شاید گوتیک و سلتیک هم... پا سانسکریت دارای ریشه‌ی مشترکی
525:بر ویلیام جونز به ریشه‌ی مشترک این زبانها اشاره کرد ولی او هم مانند جیمز پارسونز به
573:اروپایی پیشرفت بسیاری کرده است و دانشمندان ریشه مشترکك اکثر واژه‌های هند و آروپایی را (از
818:این زبانها که امروزه معدوم هستند؛ مشتمل‌اند بر تخاری ۸ (۸ 10017۸/87۸1) و تخاری 8
870:دوران باستان در همین سرزمین رواج داشته» مشتق شده باشد. امروزه حدود شش میلیون نفر به ان
=== ARY pages موزه ===
351:آورده بودند که آثار هنری آن در بسْیاری از موزه‌ها دیده می‌شود. ورود هند و اروپائیان از شمال.
```


## [2026-09-07T17:46:50.351Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c 'مادر' incoming/ARY/ARY_pages.txt; grep -n 'مشت' incoming/ARY/ARY_pages.txt | wc -l; grep -n 'مو زه\\|مو‌زه' incoming/ARY/ARY_pages.txt | head -3; grep -n '^مشت\\|^موزه' incoming/ARY/ARY_pages.txt | head",
 "description": "Check ARY coverage"
}
```


### [2026-09-07T17:46:50.459Z] TOOL RESULT

```
13
28
930:مشترکك هند و اروپائیان را مشخص می‌کنند. مثلاً واژه‌ی : گوسفند» در چند زبان هند و اروپایی چنین.
13975:مشتن شده‌اند.
```


## [2026-09-07T17:46:56.894Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13960,13990p' incoming/ARY/ARY_pages.txt; echo \"--- pdf page tags near ---\"; awk 'NR<=13975 && /pdf page/{p=$0;n=NR} END{print n\": \"p}' incoming/ARY/ARY_pages.txt",
 "description": "ARY context"
}
```


### [2026-09-07T17:46:58.148Z] TOOL RESULT

```
فرانسه (74ع۳۸۷): لاله انا چکهد (280)): الا ان
اسپانیایی (5۸۸//370): 07 اسلوا کی (51.01/4): 0
ایتالیایی (ماله7)): 10 هتیت (4177178): ان ان ابا ای ی ۱۱
۱ رومانی ((#۸4۸24): ند ال رد انا
۱ پرتغالی (۳077101532): 0 پسگشت‌ها اه دا
ایسلندی کهن 509/010۸400 صا0): 6 ۶0022
۱۸ 2 (قاقعهه) ای انا
آلمانی کهن (0270/۸2 ۷۲04 2ا0): 5 (318ه۸۸) :010275
,1۸417 1 (8آ01۸38) وا
آلمانی (0870/۸۷): لابند انا 2 راهان منکن آ یداب
انگلیسی کهن (ل9لا22/0 صا0): فرهنگ معین : ۳:۳۵
0 ,ف۸ 2۸73 برهان قاطع : ۱۹۹۶
یادداشت:
۱ چم این واژه در سانمکریت و هثیت: کوبیده» خُرد شده.
۲ برخی واجریشه شناسان معتقدند که شکل‌های کنونی این واژه در اکثر زبان‌ها از واژه‌ی یرنانی 218331۸7305
مشتن شده‌اند.
اوستایی (48874۷): 10۸ کردی (678057): 270
پهلوی (7/لتله): 0 ,11170 سانسکریت (5(757877):
اوستی (05987/6): ,31120 31102۸ ,211073
[pdf page 470]
1
مزدا /] ۴۷۱
یونانی (02270): ۱۳5 روسی (/#78514): 20۸
گوتبک (007710): 205 چکد (لل280)): ۸20۸
۱ ایسلندی گهن (010۸0۷/نفی5 صا0): برهمی (/80748(4140): ۱ 120۸
۸ ,3/50۸ اسلوا کی (851-07430): 220۸
ساکسرنی کهن (/54240 00): ۰ 3/80۸
فریزی کهن (0مادل7# طا0): 0 پسگشت‌ها هراد دی
آلمانی کهن (/057040 08 بط صا): 6 ۸00500
۷۸۸ ,۸157۸ 8 (۸1850) ای ام ان
آلمانی (/058۵4): دا بدا نا :28( ها
--- pdf page tags near ---
13952: [pdf page 469]
```


## [2026-09-07T17:47:10.234Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/s.py\necho \"=== HUB ===\"; python3 $S HUB.txt 'musti|mozag|möza|Faust' 300 | head -30\necho \"=== FSF موزه ===\"; grep -n 'موزه' FSF.txt FSF_pages.txt FRS.txt | head -10",
 "description": "Grep Hubschmann and Shahnameh glossaries"
}
```


### [2026-09-07T17:47:11.685Z] TOOL RESULT

```
=== HUB ===
### HUB.txt musti 173690
oflfenbar fiir *mTnidan, 997. Horn verwirft die von der Tradition allerdings em- pfohlene Etymologie mit Recht, da zd. amayavd im Phi. *amcvak u. dgl. lauten miisste. Fr. Miiller (WZKM. 8, 182) fiihrt moya auf ein ap. ^mauda- zuriick, zu dem np. must 'Klage, Betriibniss' wohl gehoren k5nnte (= ap. *musti aus "^mud-ti). Ob arm. moir 'das Betteln* (als LW.) = ap. "^mauda^ ist, bleibt wegen der Bedeutung zweifelhaft. - Im Armen. ist iibrigens muracik zu lesen. 999. Zu paz. meh lautet der Superl. mahest, maMst (Min. 61. 132, Shk. 257) == ap. madista-, Dazu kurd. rndstir 'grosser (So ein, kurd. Sam

### HUB.txt musti 435638
sw5. War die iran. Grundform des;»letzteren *fsa- = zd. aresa-^ so sollte man im Np. *xis erwarten, wie umgekehrt np. xirs eher auf iran. *fsa- (als fsa-) weist. § 130. Idg. st (nach i, u etc.) und kH = iran. ap. st = np. st und s^:' a) = s^ : mw6^^ Taust' = zd. rmdU-, arm. msrtfc 'Bundel* = phi. "^mustik; angust 'Finger, Zehe' = zd. angusta"; ustur 'KameeV = zd. uistra--, pust 'Rucken* = zd. parsfi-, skr. prstha-; mustan reiben, skr. mrsta-, Wrzl. m&t'g'^\ hihist 'Paradies' == zd. vahista-; xist 'ZiegeF, skr. istako-; ristan *spinnen, pr. resam, Wrzl. reik^; nivistan 'schreiben* = ap. nipista

### HUB.txt Faust 37821
e Pehleviform war naturlich nur vadar (PPGl. 2 und 232), nicht badar, das eine Unform ist. Ap. abddaris gehort keinesfalls hierher und bleibt im Uebrigen nach wie vor dunkel. 167. Dazu kurd. ia^rftawd 'Armband' fSocin, Kurd. Samml. II, 284), np. bazuband, afgh. LW. bdzuband Arm- band', arm. bazpan 'Fausthandschuh* (= *Arm-schutzer ). Zu den LW. geh5rt auch afgh. bazu pi. bazugan *the side of a bedstead, the arm, the fold of a door, vgl. np. hd»u 1) Arm, 2) Thiirpfosten, kurd. bozk, bask 'Seite, Pfeifenrohr* (Socin, a. a. 0.). Rathselhaft bleiben die angefuhrten Dialectformen, welche auf bahu (

### HUB.txt Faust 157418
 iran. I, p. 288. Ueber dial, kine s. Mann, ZDMG. 47, 705. 871. Np. hutdh oder kdtah (nach dem afgh. LW. kdtah) heisst eigentlich 'kurz* (nicht 'klein*) und ist von np. kddak *Kind' = phi. kotak *a child, an infant' Gl. and Ind. 201, arm. LW. kotak *der Eleine' (Beiname des armen. Konigs Xoarov bei Faust us von Byz.) zu trennen. Letzteres ist durch Suffix ak von *kOt = ap. ^kauta- abgeleitet, zu dem das auf schwachster Wurzelstufe stehende zd. ktUaka- *klein* gehSrt. Horn's Erklarung von kodak aus ^kvataka- (vom Pronominal stamm kva-, ku"?) ist mir unverstandlich. 872. Np. fcil^a 'irdene Krug,

### HUB.txt Faust 262878
sp ZDMG. 44, 655), np. Adar-cjusnasp Tab. p. 388, bei Firdusi— 149 — adargusasp] Atrpatakan (Elise, Laz. Pharp. etc.) = phi. Aturpdtakan (West, PT. I, 120), np. A8arhaieg(l7i\ Vrkan *Hyrkanien (Elise, Laz. Pharp., Sebeos etc.) = np. Gurgdny ap. vrkwna-, zd. vehrkdna- gr. YpxaWa^); Vrken N. pr. bei Faust us v. Byz. = np. Gurgin; grtak *Laib Brot* = np. girda; krpak 'Werkstatt, Laden' (Apg. 28, 15) = np. kurba *Laden , arab. kurbaj. In letzter Silbe musste ur, ir als solches bleiben, daher : vziirk, vzruk gross* (5. Jhd., Elise 20, 5) = np. buzurg, phi. inschr. vzrkan (s. oben), ap. vazrka-. In

### HUB.txt Faust 263635
qn (5. Jhd., ZDMG. 43, 409, 414), phi. Gurgan Phi. Vend, p. 4, Z. 2, 3 V. u. ; Gurgan N. pr. (Joh. Kath., Thorn. Artsr., Steph. A sol. etc.) = alterem Vrhen, np. Gurgin; pursisn *Verh6r, Prozess' (Elise, ed. Johanniseanc p. 144) = phi. pursisn, np. pur sis Trage*; pustipan oder pstipan 'Leibwachter Faustus v. Byz. p. 164, 207, EliSe p. 49, 104, Laz. Pharp. 390 etc. = np. pustibctn 'Beschiitzer, Stiitze', phi. pustikpansolar 'Befehlshaber der Garde* BB. 4, 62, pusttkpanakih *Schutz' Phi. Min. p. 46, Z. 14. Die oben angefuhrten alteren Lehnworter (z. B. Vrkan) lassen es unentschieden, ob im alte

=== FSF موزه ===
FSF.txt:256:از این گذشته. در نسخۀ موزهُ بریتانیا دستبرد دیگری شده است. در این نسخه 
FSF.txt:412:تنها در نسخه موزه بریتانیا به معنی ابر. در 
FSF.txt:3133:قبا و موزه و رانینش بر تن 
FSF.txt:29288:موزه 
FSF.txt:29319:موزه (بر وزن کوزه) 
FSF.txt:29326:همیشه به یک ساق موزه درون 
FSF_pages.txt:262: ‫از این گذشته‪ .‬در نسخۀ موزهُ بریتانیا دستبرد دیگری شده است‪ .‬در این نسخه‬
FSF_pages.txt:443: ‫به حوض دگر بینمت آبخور‬                        ‫سخه موزه بریتانیا به معنی ابر‪ .‬در‬
FSF_pages.txt:2387:               ‫قبا و موزه و رانینش بر تن‬                             ‫بیامد هم اندر زمان پیش اوی‬
FSF_pages.txt:20632:‫موزه‬
```


## [2026-09-07T17:47:20.426Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29280,29340p' FSF.txt",
 "description": "Read FSF muze entry"
}
```


### [2026-09-07T17:47:20.469Z] TOOL RESULT

```
منش بر گذشته ز چرخ بلند 
(۵۲۸-۱۱۱-۱) 
میانجی نخواهی جز از تیغ و گرز 
مش برز داری و بالای برز 
)0-1-۴ 
(ویس ۱۷۵-۱۱۸): 


موزه 


.. منش بر آسمان دارد به کشی 
منشور (با زبر اول -تازی) 
فرمان: 
به گیتی جز از پاک یزدان نماند 
که منشور تیغ تو را برنخواند 
(۲۳۰-۱۵۵-۲) 
موبد 
۱-پیشوای اس زردشتی: 
(دقیقی 2۴-۶۹-۶) 
[گشتاسپ] پراگند اندرجهان موبدان 
نهاداز بر اذران گبدان 
۲-دانشمند. فرزانه. حکیم: 
چنین گفت موبد که یک روز طوس 
بدانگه که برخحاست بانگ خروس 
(۲۰-۰۷-۳) 
۳-آموزگار: 
منذر برای بهرام گور: 
سه موبد نگه کرد فرهنگ جوی 
که در شورستان بودشان آبروی 
یکی تادبیری بیاموزدش 
دل از تسیرگی‌ها بیفروزدش 
دگر آنک دانستن باز و یوز 
بیاموزدش كان بود دلفروز 
و دیگر که چوگان و تیر و کمان 
همان گردش رزم با بدگمان 
چنین موبدان پیش منذر شدند 
ز هر دانشی داستان‌ها زدند 
(۱۶-۱۱۱-۲۷۰۲۸۷) 
موزه (بر وزن کوزه) 
چکمه (ترکی از چکماک -کشیدن): 


مولش 


همیشه به یک ساق موزه درون 
یکی خنجری داشتی آبگون 
(۲۸۵-۲۵-۵) 
مولش (بر وزن پوشش) 
(اسم مصدر از مولیدن) درنگ. دست‌به 
دست کردن. تاخیر تعویق: 


ز مولش سزد گر بمانی شگفت 
(۴۷۲-۱۴۵-۴) 

مولیدن 
درنگ کردن دست سه‌دست کردن.
```


## [2026-09-07T17:47:36.040Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A5%A4%E0%A5%A4",
 "prompt": "ignore"
}
```


## [2026-09-07T17:47:36.440Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/move",
 "prompt": "Give the etymology of English \"move\" verbatim, including the Latin and PIE root given."
}
```


### [2026-09-07T17:47:37.646Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T17:47:41.792Z] TOOL RESULT

```
# Etymology of "Move"

The verb "move" entered English in the late 13th century from Anglo-French *mover* and Old French *movoir*. It derives from Latin *movere* "move, set in motion; remove; disturb," with past participle *motus* and frequentative *motare*. 

The ultimate source is the Proto-Indo-European root *meue- "to push away."
```


## [2026-09-07T17:47:47.341Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc/getWord.php?key=moj%C4%81",
 "prompt": "What does Monier-Williams give for mojā?"
}
```


## [2026-09-07T17:47:47.729Z] TOOL CALL #68: WebSearch

```json
{
 "query": "Sanskrit \"mojā\" boot stocking Monier-Williams Persian loanword mūza"
}
```


### [2026-09-07T17:47:49.011Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T17:47:55.964Z] TOOL RESULT

```
Web search results for query: "Sanskrit "mojā" boot stocking Monier-Williams Persian loanword mūza"

Links: [{"title":"मोज़ा - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A5%8B%E0%A4%9C%E0%A4%BC%E0%A4%BE"},{"title":"মোজা - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E0%A6%AE%E0%A7%8B%E0%A6%9C%E0%A6%BE"},{"title":"Monier-Williams: A Sanskrit-English Dictionary (1872)","url":"https://gretil.sub.uni-goettingen.de/gretil/6_sres/2_dict/mwse72_u.htm"},{"title":"A Sanskrit English Dictionary: M. Monier - Williams: 9789390064649: Amazon.com: Books","url":"https://www.amazon.com/Sanskrit-English-Dictionary-Monier-Williams/dp/9390064643"},{"title":"A Sanskrit English Dictionary : Monier-williams, Monier, Sir : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/in.ernet.dli.2015.31959"},{"title":"Moja, Mōja: 8 definitions","url":"https://www.wisdomlib.org/definition/moja"},{"title":"Sanskrit Dictionary - Monier Williams | PDF","url":"https://www.scribd.com/doc/315325893/SANSKRIT-DICTIONARY-MONIER-WILLIAMS"},{"title":"Monier-Williams: A Sanskrit-English Dictionary","url":"https://gretil.sub.uni-goettingen.de/gretil/6_sres/2_dict/mwse_u.htm"},{"title":"Monier Williams Sanskrit-English Dictionary","url":"https://www.monierwilliams.com/"},{"title":"List of loanwords in Malay language","url":"https://en.wikipedia.org/wiki/List_of_loanwords_in_Malay_language"}]

Based on the search results, I found relevant information about this Sanskrit-Persian loanword connection:

The Sanskrit word mojā is borrowed from Classical Persian موزه (mōza). In Marathi, mōjā (मोजा) means "a stocking or sock", and cognate forms appear across multiple South and East Asian languages including Assamese, Bengali, Gujarati, Marathi, and Nepali.

The etymology traces back further: the Persian mōza derives from Middle Persian mōzag, ultimately from Proto-Iranian *hmáwčakah (literally "that which is let loose"), nominalized from *hmáwčati ("to let loose, release").

While the search results confirm Monier-Williams' dictionary exists and discuss Sanskrit-English lexicography, they don't contain the specific entry details from his dictionary on this word. However, the etymological information you're asking about—the Persian loanword origin of mūza/mojā—is clearly documented in contemporary lexicographical sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-07T17:48:28.324Z] TOOL CALL #69: Bash

```json
{
 "command": "cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg339.png data/verification/sources/refs/ocr/BOOK/339.png && echo copied\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%85%D8%B4%D8%AA' --note 'page 339, root Meuk (scratch), node 2: Persian mošt < MP mušt < PII *muštíš' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B2%D9%87' --note 'page 339, root Meuk (boot), node 3: Persian muzeh < MP mozag < PIr *hmawcati; Arabic mawzaj' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/mucro' --note 'page 339, root Meuk (scratch), nodes 3-4: Latin mucro etymology (de Vaan), English mucro bot./zool.' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mewk-' --note 'page 339, root Meuk (boot): PIE *(s)mewk- to let loose/release' 2>&1 | tail -2",
 "description": "Archive web sources part 1"
}
```


### [2026-09-07T17:48:30.563Z] TOOL RESULT

```
copied
/home/sfmqrb/git/rishe/data/verification/sources/web/a5b9172a0eb5de79.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/93a4b15fc5b6bcc3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9fa3f718ed28638a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/89f04884870b01a6.txt
```


## [2026-09-07T17:48:39.698Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/moveo' --note 'page 339, root Mew/Meu 2: Latin moveo < PIE *m(y)ewh1-' 2>&1 | tail -1\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/mu%C5%A1t%C3%AD%C5%A1' --note 'page 339, root Meuk (scratch), node 1: PII *mustis fist, from *mews- not *mewk- (dubious)' 2>&1 | tail -1\npython3 tools/fetch_source.py 'https://bosworthtoller.com/search?q=meo' --note 'page 339, root Meuk (boot), node 6: OE meo/meon a shoe or sock, gl. pedula' 2>&1 | tail -1\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/move' --note 'page 339, root Mew/Meu 2, node 4: English move < OFr movoir < L movere, PIE *meue- push away' 2>&1 | tail -1\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A5%8B%E0%A4%9C%E0%A4%BC%E0%A4%BE' --note 'page 339, root Meuk (boot), node 5: Indic moja stocking is a loan from Persian moza' 2>&1 | tail -1",
 "description": "Archive web sources part 2"
}
```


### [2026-09-07T17:48:45.061Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/bd3b64367a48fc93.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fabbb24907e37982.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b7c5ebbe201befbf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1f5e14dc99d81f14.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/616fb09f55c40e56.txt
```


## [2026-09-07T17:48:48.619Z] TOOL CALL #71: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T17:48:48.656Z] TOOL RESULT

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


## [2026-09-07T17:49:47.506Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/s.py\necho \"=== POK meo ===\"; python3 $S POK_full.txt 'meo,|méo' 200 | head -12\necho \"=== KLN move ===\"; python3 $S KLN_1966.txt 'move, intr. and tr' 400 | head -8\npython3 $S KLN_1966.txt 'movere' 300 | head -12",
 "description": "Check POK for OE meo and Klein for move"
}
```


### [2026-09-07T17:49:49.058Z] TOOL RESULT

```
=== POK meo ===
### POK_full.txt meo, 2435374
below mei-g"-, mei-R-, mei-t(h)-.   References: WP. II 240 f., WH. I 254 f., II 128, Berneker II 48 f., Trautmann 175 f.  Page(s):710   Root / lemma: meih-3   Meaning: to wander, go   Material: Latin meo, -are^ to go, pass' (perhaps previous a-verb =) poln. mijam, mijac,   Czech mfjfm, mfjeti^ pass, elapse, avoid '; on this basis could also be based *meia- na-   present *mi-nami : Old Bulgarian mi

### POK_full.txt meo, 3752167
f OiTgo'd\e natijrliche dampness of Bodens'), uvor, -oris' dampness, damp ',     uvesco, -e/"© "humid, wet become, sich betrinken', Ji/e/7s "humid, wet, damp' (place a  *Ji/c»sfrom *J^"'c»-s ahead); umeo, -eAe "humid, wet sein', umor^ dampness ', umecto  "befeuchte' (based on auf *ug"'smos)\ Middle Irish fuar urine ' {*uog"-lo-)\   Old Icelandic vgkr{f\Vk. vgkuan) "humid, wet', vgkvixw., vgkvat " 

=== KLN move ===
### KLN_1966.txt movere 2003800
nis  or  Gk.  xotvr;  x'(a8-/jai?. commonsensical,  adj.  —  Formed  fr.  common sense  on  analogy  of  nonsensical. Derivative:  commonsensical-ly,  adv. commotion,  n.  —  F.,  fr.  L.  commotionem,  acc.  of commotio,  ‘violent  movement,  agitation,  excite¬ ment’,  fr.  commotus,  pp.  of  commovere,  ‘to  put in  violent  motion,  stir,  move’,  fr.  com-  and  mo- vere,  ‘to  move’.  See  motion. Derivative;  commotion-al,  adj. commove,  tr.  v.  —  ME.  commoeven,  commeven, fr.  OF.  comovoir,  fr.  L.  commovere.  See  prec. word. communal,  adj.  —  Late  L.  communalis,  fr.  com

### KLN_1966.txt movere 2004023
‘violent  movement,  agitation,  excite¬ ment’,  fr.  commotus,  pp.  of  commovere,  ‘to  put in  violent  motion,  stir,  move’,  fr.  com-  and  mo- vere,  ‘to  move’.  See  motion. Derivative;  commotion-al,  adj. commove,  tr.  v.  —  ME.  commoeven,  commeven, fr.  OF.  comovoir,  fr.  L.  commovere.  See  prec. word. communal,  adj.  —  Late  L.  communalis,  fr.  com- muna ,  ‘a  commune’.  See  commune,  ‘a  small  poli¬ tical  district',  and  adj.  suff.  -al. Derivatives',  communal-ism,  n.,  communal-ist,  n., communal-ist-ic,  adj.,  commtmal-ize,  tr.  v.,  enm- munaliz-ation, 

### KLN_1966.txt movere 3182003
cp.  Emys. Derivative:  emetic,  n.,  a  substance  that  causes vomiting. emeto-,  before  a  vowel  emet-,  combining  form meaning  1)  vomiting;  2)  emetic  (med.)  —  Fr. Gk.  Spcexot;,  ‘vomiting’.  See  emetic, emeute,  n.,  a  riot.  —  F.,  ‘riot’,  fr.  VL.  *exmorita, fern.  pp.  of  *exmovere,  ‘to  set  in  motion’,  used as  a  noun,  fr.  1st  ex-  and  movere,  ‘to  move’. See  move. -emia,  -aemia,  suff.  denoting  a  certain,  usually diseased,  condition  of  the  blood,  as  in  hydremia, leukemia  (med.)  —  Gk.  -atpia,  fr.  aljra,  gen. aEptocrot ;,  ‘blood’.  See  he

### KLN_1966.txt movere 3182075
g. emeto-,  before  a  vowel  emet-,  combining  form meaning  1)  vomiting;  2)  emetic  (med.)  —  Fr. Gk.  Spcexot;,  ‘vomiting’.  See  emetic, emeute,  n.,  a  riot.  —  F.,  ‘riot’,  fr.  VL.  *exmorita, fern.  pp.  of  *exmovere,  ‘to  set  in  motion’,  used as  a  noun,  fr.  1st  ex-  and  movere,  ‘to  move’. See  move. -emia,  -aemia,  suff.  denoting  a  certain,  usually diseased,  condition  of  the  blood,  as  in  hydremia, leukemia  (med.)  —  Gk.  -atpia,  fr.  aljra,  gen. aEptocrot ;,  ‘blood’.  See  hemal  and  -ia. emiction,  n.,  urination.  —  Formed  fr.  e-  and mictu
```


## [2026-09-07T17:49:56.608Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/s.py\npython3 $S KLN_1966.txt 'mivati' 700 | head -20",
 "description": "Klein move entry with IE base"
}
```


### [2026-09-07T17:49:57.962Z] TOOL RESULT

```
### KLN_1966.txt mivati 6191477
outh-i-Iy,  adv.,  mouth-i-ness,  n. moutonnee 1010 moutonnee,  adj., ‘shaped  like  the  back  of  a  sheep  , said  of  a  rock  (geology).  —  F.,  (in  roche  mou¬ tonnee),  fem.  pp.  of  moutonner,  ‘to  make  similar to  a  sheep;  to  make  woolly  or  fleecy’,  fr.  mou- ton ,  ‘sheep’.  See  mutton. movable,  adj.  —  ME.,  fr.  OF.,  fr.  moveir,  movoir, ‘to  move'.  See  move  and  -able. Derivatives:  movabil-ity,  n.,  movable,  n.,  mov- able-ness,  n.,  movabl-y,  adv. move,  tr.  and  intr.  v.  —  ME.  moven,  fr.  AF. mover,  corresponding  to  OF.  moveir,  movoir  (F. mouvoir),  fr.  L.  movere  (pp.  motus),  ‘to  move, set  in  motion’,  which  is  prob.  cogn.  OI.  mivati, ‘pushes,  moves’,  kama-mutah,  ‘moved  by  love’, Toch.  AB  mus-,  ‘to  move’,  Gk.  £p.euaixaffat., ‘to  surpass,  outstrip’,  ap,uvsiv,  ‘to  keep  off, ward  off,  defend’,  Lith.  mauju,  mauti,  ‘to  strip off’.  Cp.  commove,  remove.  Cp.  also  emeute, mob,  ‘rabble’,  mobile,  moment,  MotacUlidae, motatorious,  motion,  motive,  motor,  mutiny, promote,  remote. Derivatives:  move,  n.,  mov-er,  n.,  mov-ing,  adj., mov-ing-ly,  adv. movement,  n.  —  Late  ME.,  fr.  OF.  movement  (F. mouvement),  fr.  ML.  movimentum,  fr.  L.  movere. See  move  and  -ment  and  cp.  moment, movies,  n.  pi.,  moving  pictures  (colloq.)  —  Con¬ traction  of  moving  pictures. mow,
```


## [2026-09-07T17:58:09.131Z] TOOL CALL #74: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-339.json",
 "content": "{\n  \"pdf_page\": 339,\n  \"book_page\": 309,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Meuk\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *meuk- 'to scratch, tear' (Pokorny 745; = *h₂mewḱ- in the modern notation, on the strength of Gk. ἀμύσσω / ἀμυκαλαί)\",\n      \"note\": \"Pokorny IEW 745 really does have a root 'meuk-' with the meaning 'kratzen, reißen' = 'to scratch, tear'; the language label (Indo-European) and the page are exact. Nourai's gloss 'scratch, rub' renders 'reißen' ('tear') as 'rub', which is the one inaccuracy. Pokorny's whole material is: Gk. ἀμυκαλαί 'arrow-tips' (Hes.), ἀμύσσω / Att. ἀμύττω 'I split, scratch', ἀμυχή 'scratch'; Lat. mucrō; 'perhaps' OE ge-myscan and Lith. mušti 'hit'; 'perhaps also' OInd. muṣṭi-, Av. mušti- 'fist'. Both of the branches Nourai draws (the fist word and mucrō) are therefore in Pokorny, but the fist branch carries Pokorny's own 'vielleicht'. Note that this page prints TWO homonymous roots called 'Meuk': this one (POK:745, 'scratch') and entry 1 ('stocking, boot'), which is in fact Pokorny's separate root meug-2, meuk- 'to slide, slip' on p. 744 — a reference Nourai does not give.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *meuk- «خراشیدن، دریدن» در فرهنگ ریشه‌شناختی پوکورنی (ص ۷۴۵) به همین صورت آمده است؛ پس برچسب زبانی و شمارهٔ صفحهٔ نورایی درست است. تنها ایراد در معنی است: پوکورنی «kratzen, reißen» یعنی «خراشیدن، دریدن» آورده و نورایی «دریدن» را «مالیدن (rub)» ترجمه کرده است. مادهٔ اصلی این ریشه در یونانی ἀμύσσω «خراشیدن» و در لاتین mucrō «نوک تیز» است؛ پیوند «مشت» با این ریشه در خود پوکورنی با قید «شاید (vielleicht)» آمده است. توجه شود که در این صفحه دو ریشهٔ هم‌نام «Meuk» چاپ شده و ریشهٔ دوم (بند ۱) در حقیقت ریشهٔ جداگانهٔ meug-2/meuk- «لغزیدن، سُریدن» در ص ۷۴۴ پوکورنی است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/mucro\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/mu%C5%A1t%C3%AD%C5%A1\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:745\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: meuR- [OCR for meuk-] | Meaning: to scratch, tear | Material: Gr. ἀμυκαλαί … ἀμύσσω, Attic ἀμύττω \\\"split, scratch\\\", ἀμυχή \\\"crack, scratch\\\" …; Latin mucro \\\"a sharp point, edge, sword's point\\\"; perhaps to Old English ge-myscan …; perhaps also Old Indic musti-, Avestan musti- … | References: WP. II 255, WH. II 117 f. | Page(s): 745'. Exactly Nourai's root, page and material.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II 255 (WLD_Bd2_pages.txt, s.v. 'meuk- „kratzen, ritzen\\\"')\", \"stance\": \"supports\", \"note\": \"'meuk- „kratzen, ritzen\\\". gr. ἀμυκαλαί … ἀμύσσω, att. ἀμύττω „ritze, zerkratze\\\" …; lat. mucro „scharfe Spitze … bes. des Speeres oder Schwertes\\\"; vielleicht lit. mušti „schlagen\\\"' — the root exists in Walde-Pokorny with the same content, but WP adds two escape clauses (see the node notes).\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt (Watkins, IE roots)\", \"stance\": \"silent\", \"note\": \"Watkins' list has no root 'meuk- to scratch'; the neighbouring entries are meug-1 'to act surreptitiously', meug-2 'slimy, slippery' [Pok. 2. meug- 744] and meuə- 'to push away' [Pok. 2. meu- 743]. Watkins simply does not recognise Pokorny's meuk- 745.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. mūkóo(n) (mūkró-) 'pike, spike, peak, pile' (IEC.txt line 11364, printed p. 814)\", \"stance\": \"partial\", \"note\": \"'mūkóo(n) (mūkró-) \\\"pike, spike, peak, pile\\\". WP II, 311 Per. mūk \\\"sting\\\"; Hes. mūkon \\\"pile\\\"; Lat. cf. (variant) mūcro … \\\"point of sword\\\"' — Mann keeps Lat. mucrō but under a noun-root 'spike', not under a verb 'scratch'; the fist word he puts under a separate 'mūk- \\\"beat, thrash, strike\\\"; muktis \\\"fist, blow\\\"' (line 11376).\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"mušti\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Av. mušti- f. 'fist' is a real, well-attested word, but only inside the compound mušti.masah- 'of the size of a fist' (Bartholomae, Altiran. Wb. col. 1189: 'musti.masah- 1) n. \\\"Grösse einer Faust\\\"; 2) Adj. \\\"faustgross\\\": mušti.masaŋhəm xrūm \\\"a piece of raw meat the size of a fist\\\", Yt. 14.33'). What is disputed is the ARROW, i.e. its descent from a root *meuk- 'scratch': Pokorny himself only writes 'vielleicht auch ai. muṣṭi-, aw. mušti-', and Walde-Pokorny II 255 hedges twice over ('Lit. mušti könnte auch ursprgl. \\\"boxen\\\" gewesen sein; dann vielleicht zu ai. muṣṭi-ḥ \\\"Faust\\\"'), i.e. the fist word reaches *meuk- only through the Lithuanian verb mušti 'to strike'. Modern reconstruction takes the word back to Proto-Indo-Iranian *muštíš 'fist' < PIE *méws-ti-s ~ *mus-téy-s, from the root *mews- 'to shut, close (the hand)', with Tocharian B maśce 'fist' as the decisive comparandum; the derivation from *mewḱ- 'to scratch, tear' is expressly labelled dubious. Mann (IEC) likewise files Skt. muṣṭi- not under his 'spike' root but under 'mūk- \\\"beat, thrash, strike\\\"; muktis \\\"fist, blow\\\"'. So: the word and the Avestan label are right, the parent root is probably wrong.\",\n          \"derivation_fa\": \"واژهٔ اوستایی mušti- «مشت» واقعی است، ولی در اوستا تنها در ترکیب mušti.masah- «به اندازهٔ یک مشت» گواهی شده است (بارتولمه، فرهنگ ایرانی باستان، ستون ۱۱۸۹). آنچه محل تردید است خودِ پیکان است، یعنی وابستگی این واژه به ریشهٔ *meuk- «خراشیدن»: پوکورنی خود با قید «شاید» می‌نویسد و والده‑پوکورنی (ج ۲ ص ۲۵۵) دو بار احتیاط می‌کند و پیوند را تنها از راه فعل لیتوانیایی mušti «زدن» برقرار می‌سازد. ریشه‌شناسی امروزی این واژه را از هندوایرانی آغازین *muštíš، از هندواروپایی آغازین *méws-ti-s و ریشهٔ *mews- «بستن (دست)» می‌گیرد و هم‌ریشهٔ تخاری maśce «مشت» را گواه می‌آورد؛ همان منابع، اشتقاق از *mewḱ- را «مشکوک» می‌خوانند. پس واژه و برچسب زبان درست است اما ریشهٔ پیشنهادی نورایی را پژوهش امروزی رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/mu%C5%A1t%C3%AD%C5%A1\",\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%B4%D8%AA\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:745\", \"status\": \"partial\", \"note\": \"Pokorny p. 745 does list the word, but explicitly as a guess: 'perhaps also Old Indic musti-, Avestan musti-' (POK_full.txt, s.v. meuk-). Nourai draws it as a plain arrow with no hedge.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 1189 (BRT.txt line 20598)\", \"stance\": \"partial\", \"note\": \"'j. mušti.masah- 1) n. \\\"Grösse einer Faust\\\": … 2) Adj. (auch fem.) \\\"faustgross\\\": [mušti.masa]ŋhəm (ASf.) xrūm Yt. 14.33' — confirms the Avestan word (only in this compound), says nothing about a PIE root.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 255 (WLD_Bd2_pages.txt, s.v. meuk-)\", \"stance\": \"partial\", \"note\": \"'Lit. mušti konnte auch ursprgl. „boxen\\\" gewesen sein; dann vielleicht zu ai. muṣṭi-ḥ „Faust\\\" (Uhlenbeck KZ. 39, 260 f., Güntert KZ. 45, 193 ff.)' — a conditional inside a conditional.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, s.v. mūk- 'beat, thrash, strike'; muktis 'fist, blow' (IEC.txt line 11376)\", \"stance\": \"contradicts\", \"note\": \"'mūk- \\\"beat, thrash, strike\\\"; muktis \\\"fist, blow\\\". (Variant of type muks-, q.v.) … Oss. mūs, Dig. mos \\\"threshing-floor\\\"; … cf. also Skt. muṣṭib[muṣṭiḥ]' — Mann derives the fist word from a 'beat' root, not from the 'scratch' root that carries mucrō.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p. 2010, Mo'in's footnote 6 (ocr/BQT/2010.txt)\", \"stance\": \"supports\", \"note\": \"Mo'in: 'پهلوی mušt (مشت، قوت) «نیبرگ ص ۱۵۳»، اوستا mušti- (mušti-masah- [به اندازهٔ یک قبضه]) «بارتولمه ۱۱۸۹»، هندی باستان muṣṭi-' — supports the Avestan→Persian chain and gives Bartholomae 1189, but offers no PIE root.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"mošt «مشت ۱»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP مشت mošt 'fist' continues Old Iranian *mušti- (Av. mušti-, in mušti.masah-) through Middle Persian mušt, written <mwšt'>, which Nyberg (Manual of Pahlavi II, p. 153, cited by Mo'in) and the Pahlavi Vd. 17(18) glosses attest, beside the abstract muštīh in the Ardā Wirāz-nāmag. Phonologically the chain is trivially regular: the Indo-Iranian cluster -št- is one of the clusters Persian keeps unchanged, and short u before it stays (Hübschmann, Persische Studien §130 puts mušt 'Faust' = Av. mušti- at the head of exactly that sound-law, next to angušt 'finger' = Av. angušta-, pušt 'back' = Av. paršti-, xišt 'brick'); the New Persian pronunciation mošt is only the regular later lowering of ĭ/ŭ. Cognates: Skt. muṣṭí-, Kurd. mist/mistek, Pashto mut/mūt, Wakhi mōst, Sarikoli mut, Baluchi mušt (a loan from Persian); Old Armenian mštik is an Iranian borrowing. The word passed on into Ottoman Turkish muşt, Georgian mušṭi and Kashmiri muś.\",\n          \"derivation_fa\": \"«مشت» فارسی نو بازماندهٔ ایرانی باستان *mušti- (اوستایی mušti- در ترکیب mušti.masah-) است که از راه فارسی میانهٔ mušt (نوشتار <mwšt'>؛ نیبرگ ج ۲ ص ۱۵۳ و حاشیهٔ پهلوی وندیداد ۱۷) به دری رسیده است. تحول آوایی بسیار ساده است: خوشهٔ -št- هندوایرانی در فارسی دست‌نخورده می‌ماند و هوبشمان در «پژوهش‌های فارسی» (بند ۱۳۰) همین واژه را نمونهٔ نخست این قانون آوایی آورده و در کنار آن angušt = اوستایی angušta-، pušt = اوستایی paršti- و xišt را نشانده است؛ mošt امروزی تنها حاصل باز شدن منظم واکهٔ کوتاه u به o در فارسی نو است. هم‌ریشه‌ها: سنسکریت muṣṭí-، کردی mist، پشتو mut، وخی mōst؛ ارمنی mštik وام‌واژهٔ ایرانی است. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D8%B4%D8%AA\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/mu%C5%A1t%C3%AD%C5%A1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2010\", \"status\": \"supports\", \"note\": \"Fetched with tools/ref_page.py BQT:2010 (BQT_v4 pdf p. 93; the page ends '( برهان قاطع ۲۰۱۰ )'). The headword مشت is there, and Mo'in's etymological footnote 6 reads: 'پهلوی mušt (مشت . قوت) «نیبرگ ص ۱۵۳» ، اوستا mušti- ( mušti-masah- ) [باندازهٔ یک قبضه] «بارتولمه ۱۱۸۹» ، هندی باستان muṣṭi- ، مازندرانی … افغانی mut, mūt ، بلوچی mušt ، وخی mōst ، سریکلی mut … ارمنی mštik (دسته، بته)'. Exactly Nourai's arrow.\"},\n            {\"ref\": \"HRN:220\", \"status\": \"supports\", \"note\": \"Horn, Grundriss der neupersischen Etymologie, no. 982 on p. 220 (HRN.txt leaf 241): '982. mušt \\\"Faust\\\". māz. mus (*mušt). aw. mušti.[masah-] \\\"faustgross\\\"; phlv. must (vd. 17(18) Gl.), muštīh (AV.), must (PPGl.); ai. muṣṭi-, kurd. mist, mistek; afγ. mut, mūt; bel. LW. mušt; waχ. mōst, sar. mut'. The cited page is exact.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien §130 (HUB.txt, char. 435638)\", \"stance\": \"supports\", \"note\": \"'§ 130. Idg. st (nach i, u etc.) und kt = iran. ap. st = np. št und st: a) = št: mušt \\\"Faust\\\" = zd. mušti-, arm. mštik \\\"Bündel\\\" = phl. *muštik; angušt \\\"Finger, Zehe\\\" = zd. angušta-; … pušt \\\"Rücken\\\" = zd. paršti-, skr. pṛṣṭha-' — Hübschmann uses the very word as the type-case of the sound law.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD_mackenzie.txt)\", \"stance\": \"silent\", \"note\": \"grep 'mušt' / 'must' in PHD.txt and PHD_mackenzie.txt returns only must 'violation' and mustgar; MacKenzie's short dictionary happens not to list the noun mušt 'fist' (Nyberg does, p. 153, as quoted by Mo'in).\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha (incoming/ARY/ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep 'مشت' in ARY_pages.txt gives only running-text hits (مشترک، مشتق, and the footnote 'مشتن شده‌اند' on pdf p. 469-470, where the م section is at مزدا); Aryanpur has no headword for مشت.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"mucrô\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Lat. mūcrō, gen. mūcrōnis m. 'a sharp point, esp. the point of a sword; (fig.) a sword; a sharp edge' is a real classical word, and Pokorny p. 745 does put it under meuk- 'to scratch, tear' beside Gk. ἀμύσσω 'I scratch, tear' and ἀμυκαλαί 'arrow-tips' (a formation *mūk-rōn-, an -n-stem to an adjective *mūk-ro- 'pointed'; Walde-Hofmann II 117 f. is Pokorny's authority). But the derivation is not secure: (a) Walde-Pokorny II 255 itself remarks in brackets that 'mucro rückt besser nach Zupitza GG. 138 f. zu anord. smjúga \\\"hindurchkriechen, schlüpfen, auch durchbohren\\\"', i.e. to the 'slip' root meug-2; (b) Klein calls the Greek comparison only 'possibly cogn.'; (c) de Vaan's Etymological Dictionary of Latin allows Proto-Italic *meuk-ro-/*mouk-ro- from *h₂mewḱ- but adds that the Latin and the Greek words may equally come from an otherwise unknown substrate language, since the ā/ū vocalism and the -kr- cluster are irregular. Hence 'plausible', not 'confirmed': same root as the chart, but the modern handbooks flag it.\",\n          \"derivation_fa\": \"واژهٔ لاتین mūcrō (اضافی mūcrōnis) «نوک تیز، به‌ویژه نوک شمشیر» واژه‌ای کلاسیک و واقعی است و پوکورنی (ص ۷۴۵) آن را در کنار یونانی ἀμύσσω «خراشیدن» زیر ریشهٔ meuk- می‌نشاند؛ ساخت آن ستاک ‑n بر پایهٔ صفت *mūk-ro- «تیز» است. اما این اشتقاق قطعی نیست: خودِ والده‑پوکورنی (ج ۲ ص ۲۵۵) در قوس می‌افزاید که «mucro بهتر است بنا بر زوپیتزا با نورس باستان smjúga «سُریدن، فرو رفتن» سنجیده شود»؛ کلاین آن را تنها «شاید هم‌ریشه» می‌داند؛ و دِوان در فرهنگ ریشه‌شناختی لاتین احتمال می‌دهد که واژهٔ لاتین و یونانی هر دو از زبانی زیرلایه‌ای (substrate) وام گرفته شده باشند، زیرا واکه و خوشهٔ ‑kr‑ بی‌قاعده است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/mucro\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:745\", \"status\": \"supports\", \"note\": \"POK_full.txt s.v. meuk- 'to scratch, tear': '… Latin mucro \\\"a sharp point, edge, sword's point\\\" …', with 'References: WP. II 255, WH. II 117 f.' and 'Page(s): 745'. The cited page carries exactly this claim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II 255 (WLD_Bd2_pages.txt s.v. meuk-)\", \"stance\": \"partial\", \"note\": \"'lat. mucro „scharfe Spitze, z. B. der Zähne, der Klauen, der Pflugschar, eines Kometen, bes. des Speeres oder Schwertes, dieses selbst\\\" … (mucro rückt besser nach Zupitza GG. 138 f. zu anord. smjuga „hindurchkriechen, schlüpfen, auch durchbohren\\\")' — the parent handbook keeps the word here but prefers another root in the same breath.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein, Comprehensive Etym. Dict. p. 1011 s.v. mucro (KLN_1966.txt)\", \"stance\": \"partial\", \"note\": \"'mucro, n., a sharp point or tip (bot. and zool.) — L. mucro, \\\"point of a sword\\\", standing for *mukros, \\\"pointed\\\", and possibly cogn. with Gk. ἀμυκαλαί (Hesychius) \\\"arrowheads\\\", ἀμύσσω, Att. ἀμύττω … \\\"I scratch, tear\\\", and with Lith. mušu, mušti, \\\"to strike\\\".' Same root, but 'possibly'.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. mūkóo(n) (mūkró-) 'pike, spike, peak, pile' (IEC.txt line 11364)\", \"stance\": \"partial\", \"note\": \"'WP II, 311 Per. mūk \\\"sting\\\"; Hes. mūkon \\\"pile\\\"; Lat. cf. (variant) mūcro, gs -onis, m. (\\\"point of sword\\\". Cf. (?) Hes. mókron \\\"sharp\\\"); OE mūha, mūga, wm \\\"pile, rick\\\"' — Mann sets up a noun root 'spike' instead of the verb 'scratch'.\"},\n            {\"src\": \"LEW\", \"where\": \"Walde, Lat. etym. Wb. (LEW_1910.txt); Ernout-Meillet (LAT.txt)\", \"stance\": \"silent\", \"note\": \"grep 'mucro' in LEW_1910.txt returns nothing (the OCR of the m- fascicle is defective) and in LAT.txt only a Latin citation quoted under another entry ('cuspis auctior in mucrone fastigata'), not a mucrō lemma.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"mucro\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English mucro (pl. mucrones) is a straight learned borrowing of Lat. mūcrō, taken into scientific English in the 17th century and still used in botany and zoology for 'a short, straight, stiff, sharp point abruptly terminating an organ' — a leaf tip, the posterior tip of a cuttlebone, the distal part of the furcula in springtails; hence the derivatives mucronate(d), mucronately, mucronation, mucronule. There is no sound change to describe: the nominative was simply adopted unaltered (the oblique stem mucrōn- survives in mucronate < mucronātus). Nourai's gloss 'sharp point of plants' is the botanical half of the definition.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی mucro وام‌واژه‌ای دانشورانه و بی‌واسطه از لاتین mūcrō است که در سدهٔ هفدهم به انگلیسی علمی راه یافت و امروز در گیاه‌شناسی و جانورشناسی به معنی «نوک کوتاه، سخت و تیزی که اندامی را ناگهان به پایان می‌رساند» (نوک برگ، نوک صدف) به کار می‌رود؛ مشتق‌های آن mucronate و mucronule است. هیچ دگرگونی آوایی در میان نیست: صورت فاعلی لاتین دست‌نخورده وام گرفته شده و ستاک اضافی mucrōn- در mucronate بازمانده است. معنی‌ای که نورایی می‌دهد («نوک تیز گیاهان») نیمهٔ گیاه‌شناختی همان تعریف است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/mucro\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:860\", \"status\": \"not_checked\", \"note\": \"AHD:860 is a page of the main A-Z text of the American Heritage Dictionary, New College Edition (1975/76), which is not on disk; the only local AHD file is AHD_watkins1985.txt, i.e. Watkins' Indo-European Roots appendix, and that appendix has no meuk-/mucro entry at all (its neighbours are meuə- 743, meug-1 743, meug-2 744). The page number is at least plausible for m-words in a 1610-page dictionary. Klein and Funk & Wagnalls (below) were used instead.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein p. 1011 s.v. mucro (KLN_1966.txt)\", \"stance\": \"supports\", \"note\": \"'mucro, n., a sharp point or tip (bot. and zool.) — L. mucro, \\\"point of a sword\\\" …' — the English lemma, the Latin source and Nourai's 'of plants' restriction all agree.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary, vol. 3 s.v. mucro (FSD_vol3.txt char. 2836799)\", \"stance\": \"supports\", \"note\": \"'… (2) Bot. A short, straight, stiff, and sharp point, as of a leaf. [L. … sharp point.]' with 'mucronate … Ending abruptly in a short, sharp point or spine, tipped with a mucro, as a mucronate shell or leaf (< L. mucronatus < mucro, sharp point)'.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary vol. 1 (WEB_vol1.txt)\", \"stance\": \"silent\", \"note\": \"grep 'mucro' finds no entry in the volume on disk (A-M is split; the m- range is defective in this OCR).\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Meuk\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *(s)mewk- 'to let loose, release; slip off/on' (Pokorny 744 meug-2, meuk- 'to slide, slip'); the 'boot' sense belongs only to the derived Iranian noun *mauka- > MP mōzag\",\n      \"note\": \"The root box is right in substance and wrong in labelling. There IS a PIE root behind this family, but it means 'to slip, let loose, strip off': Pokorny prints it on p. 744 as 'meug-2, meuk- : to slide, slip', and quotes there precisely 'Old Indic *munakti, muñcati, mucati \\\"releases, allows to loose\\\", mukti- \\\"release\\\"; Avestan fra-muxti- \\\"loosening\\\"'. Wiktionary's reconstruction page for *(s)mewk- gives the same root with the meaning 'to let loose; to release / to slip away'. 'Stocking, boot' is not a root meaning at all: it is the meaning of one Iranian nominal derivative, Proto-Iranian *mauka-/*hmawčakah 'that which is let loose (from the foot)' > MP mōzag. Nourai also gives no Pokorny reference here (only IEC:1643, which is in the part of Mann's dictionary missing from the local scan), so the reader is not told that this 'Meuk' is a different root from the 'Meuk' of entry 0. Every individual node below is right or nearly right; it is the root's gloss, and the noun-glosses Nourai gives to two verbal roots (nodes 1 and 5), that need correcting.\",\n      \"note_fa\": \"جعبهٔ ریشه در محتوا درست و در برچسب نادرست است. ریشهٔ هندواروپاییِ این خانواده وجود دارد، اما معنای آن «رها کردن، سُریدن، از تن/پا در آوردن» است: پوکورنی آن را در ص ۷۴۴ به صورت «meug-2, meuk- : لغزیدن، سُریدن» چاپ کرده و درست در همان جا «هندی باستان muñcati «رها می‌کند»، mukti- «رهایی»؛ اوستایی fra-muxti- «باز کردن»» را آورده است؛ ویکی‌واژه نیز ریشهٔ *(s)mewk- «رها کردن» را با همین مواد بازسازی می‌کند. «چکمه، جوراب» هرگز معنای ریشه نیست، بلکه معنای یک مشتق نامیِ ایرانی است: ایرانی آغازین *mauka- / *hmawčakah «آنچه (از پا) گشوده می‌شود» که به فارسی میانهٔ mōzag رسیده است. نورایی در اینجا هیچ ارجاعی به پوکورنی نمی‌دهد و تنها IEC:1643 را می‌آورد، و به همین سبب خواننده نمی‌داند که این «Meuk» با «Meuk» بند پیشین یکی نیست. ادعای نورایی با احتیاط پذیرفتنی است: زنجیرهٔ واژه‌ها درست است، معنی ریشه و دو معنیِ نامیِ گره‌های ۱ و ۵ نادرست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mewk-\",\n        \"https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B2%D9%87\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"IEC:1643\", \"status\": \"not_checked\", \"note\": \"Mann's Indo-European Comparative Dictionary is on disk as IEC.txt, but the OCR breaks off at printed p. ~1554 (leaf 856 carries '1554', leaf 857 ends in the ul-/w- entries); the Supplement, in which p. 1643 falls, is not in the scan. The m- section of the main dictionary (pp. 812-816, leaves 455-457) contains muk- (mūk-, munk-) 'leave' and mūkóo(n) 'pike, spike', but no 'shoe' root, so p. 1643 must be a supplement entry. Not verifiable locally; archive.org item mann-an-indo-european-comparative-dictionary-1984-1987 would have to be paged image by image.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"IEW 744, s.v. meug-2, meuk- 'to slide, slip' (POK_full.txt)\", \"stance\": \"partial\", \"note\": \"'B. Old Indic *munakti, muñcati, mucati \\\"releases, allows to loose\\\", mukti- \\\"lysis, dissolution, release\\\"; Avestan fra-muxti- \\\"loosening\\\"; … Lithuanian munku, mukti \\\"escape; to get away\\\"' — Pokorny has the root and the Indo-Iranian material Nourai's tree hangs on it, but on p. 744 and with the meaning 'slide, slip', not 'stocking, boot'.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins, s.v. meug-2 'Slimy, slippery' [Pok. 2. meug- 744] (AHD_watkins1985.txt)\", \"stance\": \"silent\", \"note\": \"Watkins keeps only the 'slimy' half of Pokorny's meug-2/meuk- (mucus, meek, smuggle, mold) and lists no Iranian 'boot' derivative; nothing here for or against a root 'stocking, boot'.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. muk- (mūk-, munk-) 'leave' (IEC.txt line 11348, printed p. 812-813)\", \"stance\": \"supports\", \"note\": \"'muk- (mūk-, munk-) \\\"leave\\\". WP II, 254 Skt. mucámi, muñcámi, pp: muktáh \\\"leave, release\\\"; Romani mukav … \\\"leave, let, allow\\\"; Av. muč- \\\"let, release\\\"; Tokh. A muk-, mok-, B mauk-, v. \\\"leave\\\"' — Mann's own main-dictionary root for this family is a verb 'leave, release' with Av. muč-, which is what the tree really descends from.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"maoč\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"There is no Avestan NOUN maoč 'shoe, boot'. Nourai's source, Horn no. 994 (p. 223), writes 'aw. √maoč mit paiti \\\"anziehen (sc. Schuhe)\\\"' — the square-root sign marks a VERBAL ROOT, cited in the older full-grade convention as maoč- (= muč-), 'to put on / strip off (footwear)'. Bartholomae's Altiranisches Wörterbuch has no lemma maoča-: the Avestan noun for footwear is aoθra- n. 'Schuhwerk, Schuhzeug' (col. 42), and the root shows up only in the participial and abstract forms paiti.smuxta- and fra-muxtay- (node 4). Mo'in's footnote to Borhan-e Qate' 2051 writes the root correctly as 'اوستا muč- با paiti (پوشیدن [کفش])'. So the arrow itself is sound — the Iranian 'boot' word is built on this root, Proto-Iranian *hmawč- 'to clothe, let loose', with the nominal *mauka-/*hmawčakah 'footwear' — but the node's part of speech and gloss are Nourai's own error, carried over from misreading Horn's √ sign. The printed page (pdf 339) does read 'maoč : shoe, boot', so this is the book's error, not the extraction's.\",\n          \"derivation_fa\": \"در اوستا نامی به صورت maoč «کفش» وجود ندارد. مأخذ نورایی، هرن (شمارهٔ ۹۹۴، ص ۲۲۳)، نوشته است: «اوستایی √maoč با پیشوند paiti «پوشیدن (کفش)»» و نشانهٔ √ یعنی این صورت یک ریشهٔ فعلی است که به شیوهٔ کهن با درجهٔ کامل maoč- (=muč-) نقل شده است. در فرهنگ بارتولمه هیچ مادهٔ maoča- نیست؛ نامِ اوستاییِ پاافزار aoθra- «کفش، پاپوش» است و این ریشه تنها در صورت‌های paiti.smuxta- و fra-muxtay- (گرهٔ ۴) گواهی شده است. معین نیز در حاشیهٔ برهان قاطع ص ۲۰۵۱ ریشه را درست به صورت «اوستا muč- با paiti» آورده است. پس خودِ پیکان درست است — واژهٔ ایرانی «موزه» بر همین ریشه (ایرانی آغازین *hmawč-) با پسوند نامی *-ka- ساخته شده — ولی مقولهٔ دستوری و معنی این گره خطای خود نورایی در خواندن نشانهٔ √ هرن است. تصویر صفحهٔ چاپی نشان می‌دهد که کتاب نیز همین «maoč : shoe, boot» را چاپ کرده است؛ پس خطا از کتاب است نه از استخراج.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B2%D9%87\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mewk-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:223\", \"status\": \"partial\", \"note\": \"Horn p. 223 (HRN.txt leaf 244) no. 994: 'mōze \\\"Schuh\\\", arab. LW. mūzaj. aw. √maoč mit paiti \\\"anziehen (sc. Schuhe)\\\", vergl. framuxti- \\\"das Ausziehen (der Schuhe)\\\"; phlv. mōčak (Men.; arm. LW. mučak), vergl. mōk …, auch patmōxtan \\\"anziehen\\\"; ai. √mōč- mit ā, prati \\\"anziehen (irgend ein Kleidungsstück)\\\", mit upa \\\"Schuhe anziehen\\\"'. The page is right and the arrow is right, but Horn gives a verbal root with '√', not a noun 'shoe, boot'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 42 s.v. aoθra- (BRT.txt line 2945)\", \"stance\": \"contradicts\", \"note\": \"'j. aoθra- n. \\\"Schuhwerk, Schuhzeug\\\": zaranya °āiri paiti.smuxta yā vīδō.pīsa bāmya …; hat aoθranąm framuxti .. upa.mąnayən \\\"mit Ablegung ihres Schuhzeugs sollen sie ..\\\" V. 6.27' — Bartholomae's word for footwear is aoθra-, and there is no lemma maoča- anywhere in the dictionary (grep 'maoča|maoka' = nothing).\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p. 2051, Mo'in's footnote 8 (ocr/BQT/2051.txt)\", \"stance\": \"partial\", \"note\": \"'اوستا muč- با paiti (پوشیدن [کفش])، قس: fra-muxti- (بیرون آوردن [کفش])؛ پهلوی mōčak، ارمنی mučak …' — Mo'in writes the Avestan item as the verbal root muč-, confirming that Nourai's 'maoč : shoe' is a mis-glossing.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"môzag, mŭčak\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"MacKenzie's Concise Pahlavi Dictionary has 'mōzag [mwck | N mōza] shoe' (and, in the English index, 'shoe kafš, mōg, mōzag'), i.e. two Middle Persian forms: the -ag derivative mōzag < Proto-Iranian *hmawčaka- 'footwear' (literally 'the thing slipped on/off', a -ka- noun on the root muč- of node 1), and the bare stem mōg < *mauka-. The Book-Pahlavi spelling <mwck'> is ambiguous between -č- and -z-: Horn and Mo'in read it mōčak (Horn: 'phlv. mōčak (Mēnōg-ī Xrad); arm. LW. mučak'), MacKenzie normalises mōzag with the regular Middle Persian voicing/spirantisation of intervocalic -k- > -g and the -č- > -z- of the New Persian outcome. Nourai's double entry 'môzag, mŭčak' is exactly those two readings of the one word, and the Old Armenian loan mučak proves the -č- reading was current in Sasanian times. Diphthong *au > MP ō is regular (cf. *rauča- > rōz).\",\n          \"derivation_fa\": \"در فرهنگ پهلوی مکنزی آمده است: «mōzag [mwck] کفش، فارسی نو موزه»، و در فهرست انگلیسی–پهلوی نیز «shoe: kafš, mōg, mōzag». پس فارسی میانه دو صورت دارد: mōzag با پسوند نامی ‑ak/‑ag از ایرانی آغازین *hmawčaka- «آنچه (از پا) گشوده می‌شود»، و ستاک ساده mōg از *mauka-. نگارش پهلوی کتابی <mwck'> میان ‑č‑ و ‑z‑ دوپهلو است: هرن و معین آن را mōčak می‌خوانند («پهلوی mōčak (منوچهر خرد)؛ وام ارمنی mučak») و مکنزی به قاعدهٔ نرم‌شدن ‑k‑ میان‌واکه‌ای به ‑g، صورت mōzag را برمی‌گزیند. دو صورتی که نورایی می‌آورد («môzag, mŭčak») همان دو خوانش یک واژه است و وام‌واژهٔ ارمنی mučak گواه رواج خوانش ‑č‑ در دوران ساسانی است. تبدیل مصوت مرکب *au به ō در فارسی میانه قاعده‌مند است (قس *rauča- > rōz). ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B2%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2051\", \"status\": \"supports\", \"note\": \"Fetched with tools/ref_page.py BQT:2051 (BQT_v4 pdf p. 134): the entry موزه is there and Mo'in's footnote 8 gives the whole chain: 'اوستا muč- با paiti (پوشیدن [کفش])، قس fra-muxti- (بیرون آوردن [کفش])؛ پهلوی mōčak، ارمنی mučak، قس *paitmōxtan (پوشیدن)، هندی باستان mōč- با ā, prati …، کلمات ع: افغانی mōza، بلوچی mūzag, mōzay (جوراب، چکمه، پاپوش) «اسشق ۹۹۴» [= Horn no. 994]، معرب آن موزج «ابن درید»'. Exactly Nourai's Pahlavi node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD_mackenzie.txt lines 3594-3595 and 7556)\", \"stance\": \"supports\", \"note\": \"'mōz [mwc | N --] banana. mōzag [mwck, N mōza] shoe.' and, in the English-Pahlavi part, 'shoe kafs, mōg, mōzag'.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn no. 994, p. 223 (HRN.txt leaf 244)\", \"stance\": \"supports\", \"note\": \"'phlv. mōčak (Men.; arm. LW. mučak), vergl. mōk (chald. LW. מוק), auch patmōxtan \\\"anziehen\\\"' — both of Nourai's Pahlavi forms, plus the Aramaic and Armenian loans.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt)\", \"stance\": \"silent\", \"note\": \"grep 'mōzag/mwck/mōčak' in the glossary finds nothing — Nyberg's glossary covers only the texts he edits, which do not contain the word.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"mŭzeh «موزه ۲»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP موزه mōza/mūza 'boot, high shoe reaching up the calf' is the regular continuation of MP mōzag: final -ag > -a/-e in New Persian (cf. bandag > banda, xānag > xāna), and the Book-Pahlavi -č-/-z- ambiguity resolves as -z-. Borhan-e Qate' and Mo'in both define it as چکمه 'boot', and Noushin's Farhang-e Šāhnāma s.v. موزه ('بر وزن کوزه … چکمه') quotes precisely Ferdowsi's line that Nourai prints, 'همیشه به یک ساق موزه درون / یکی خنجری داشتی آبگون'. The word had a lively career outside Persian: Arabic borrowed it as مَوْزَج mawzaj (already in Ibn Durayd, as Mo'in notes), and Mo'in's own bracket in Farhang-e Fārsi tags the New Persian form '[- معر. موزج]', i.e. he takes the modern spelling to be a re-borrowing of the Arabicised مَوْزَج — a Persian → Arabic → Persian round trip; Byzantine Greek μουζάκιον and Old Armenian մուճակ mučak (both possibly through Armenian) and Indic mojā 'stocking' are further loans from the same source. Nourai's tree, with the Pahlavi node in between, is right.\",\n          \"derivation_fa\": \"«موزه» فارسی نو ادامهٔ قاعده‌مند فارسی میانهٔ mōzag است: پسوند پایانی ‑ag در فارسی نو به ‑a/‑e بدل می‌شود (قس bandag > بنده، xānag > خانه) و دوپهلویی ‑č‑/‑z‑ نگارش پهلوی به سود ‑z‑ حل شده است. برهان قاطع و معین هر دو آن را «چکمه» معنی کرده‌اند و نوشین در «فرهنگ شاهنامه» زیر «موزه (بر وزن کوزه): چکمه» همان بیت فردوسی را می‌آورد که نورایی نقل کرده است: «همیشه به یک ساق موزه درون / یکی خنجری داشتی آبگون». این واژه سفر پرماجرایی داشته: عربی آن را مَوْزَج معرَّب کرد (به گفتهٔ معین از ابن درید) و معین در «فرهنگ فارسی» خودِ صورت فارسی نو را «[- معر. موزج]» برچسب می‌زند، یعنی آن را بازوام‌گیری از معرّب می‌داند — یک رفت‌وبرگشت فارسی › عربی › فارسی؛ یونانی بیزانسی μουζάκιον، ارمنی mučak و هندی mojā «جوراب» نیز وام از همین سرچشمه‌اند. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B2%D9%87\",\n            \"https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A5%8B%E0%A4%9C%E0%A4%BC%E0%A4%BE\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:4432\", \"status\": \"supports\", \"note\": \"Mo'in's entry located in MON_part2.txt line 67942 (the running head of the local scan reads '۱۸۵۰ فرهنگ فارسی معین' — this reprint is paginated differently from the 6-vol. Amir Kabir edition Nourai cites, in which vol. 3 reaches p. ~4500, so p. 4432 for a م headword is consistent): 'موزه: (mūze) [- معر. موزج] (ا.) نوعی پاافزار که تا ساق پا و زیر زانو را فرا گیرد؛ چکمه. موزه در گل ماندن: (کد.) درمانده شدن، بیچاره گشتن'. Supports the word, the sense 'boot' and the Arabic-mediated shape; Mo'in gives no Pahlavi tag here (that is in his Borhan footnote, BQT:2051).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FSF\", \"where\": \"Noushin, Vāžanāmak / Farhang-e Šāhnāma s.v. موزه (FSF.txt lines 29319-29327)\", \"stance\": \"supports\", \"note\": \"'موزه (بر وزن کوزه) چکمه … همیشه به یک ساق موزه درون / یکی خنجری داشتی آبگون (۲۸۵-۲۵-۵)' — the identical Ferdowsi verse quoted in the chart, with the gloss چکمه.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p. 2051 (ocr/BQT/2051.txt)\", \"stance\": \"supports\", \"note\": \"'موزه - بضم اول بروزن بوزه، معروف …' with Mo'in's footnote 8 tracing it to Av. muč-, Pahl. mōčak and noting 'معرب آن موزج «ابن درید»'.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi, entry موزه (MON_part2.txt line 67942)\", \"stance\": \"supports\", \"note\": \"See ref_check: 'نوعی پاافزار که تا ساق پا و زیر زانو را فرا گیرد؛ چکمه'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Avestan\",\n          \"words\": \"paitiš-muxtâ; fra-muxti\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both forms are genuine Younger Avestan and both are built on the root muč-/muxta- of node 1, i.e. exactly where the chart puts them. (a) paiti.smuxta- (Nourai's 'paitiš-muxtâ'; the -s- is the sandhi of paitiš + muxta-) is an adjective 'mit Fusszeug bekleidet, beschuht' = 'shod, wearing footwear', attested of Arədvī Sūrā Anāhitā in Yašt 5.64 and 5.78: 'aoθra paiti.smuxta zaranyō.tuvixšna' — 'shod with footwear fastened with golden laces'. (b) fra-muxtay- f. is the abstract 'Losbinden, Ausziehen (des Schuhwerks)' = 'the unfastening, taking off (of footwear)', attested at Vidēvdād 6.27 (Bartholomae's numbering; 5.27 in the alternative division) 'hat aoθranąm framuxti .. upa.mąnayən'. Morphologically muxta- is the zero-grade participle *mukta- of muč- (Indo-Iranian *muk-tá-, cf. Skt. muktá- 'released'), with the regular Avestan k > x before t. Nourai's glosses 'to put on (shoes)' / 'to take out (shoes)' translate Horn's German loosely — the first is an adjective, the second a verbal noun, not infinitives — but the semantics and the parentage are right.\",\n          \"derivation_fa\": \"هر دو صورت اوستایی نوِ اصیل‌اند و هر دو بر همان ریشهٔ muč-/muxta- گرهٔ ۱ ساخته شده‌اند، یعنی درست همان جایی که نورایی نشانده است. نخست paiti.smuxta- (که نورایی «paitiš-muxtâ» می‌نویسد؛ ‑s‑ حاصل همنشینی paitiš + muxta- است) صفتی است به معنی «کفش‌پوشیده، نعل‌کرده» و در یشت ۵ بندهای ۶۴ و ۷۸ در وصف اردویسور آناهیتا آمده: «aoθra paiti.smuxta zaranyō.tuvixšna» یعنی «با پاافزاری که با بندهای زرین بسته شده». دوم fra-muxtay- نامِ مصدری مادینه به معنی «باز کردن و از پا در آوردن (کفش)» است و در وندیداد ۶ بند ۲۷ گواهی شده. از دید ساخت‌واژه، muxta- صفت مفعولی درجهٔ صفر ریشهٔ muč- است (هندوایرانی *muk-tá-، قس سنسکریت muktá- «رهاشده») با تبدیل قاعده‌مند k به x پیش از t در اوستایی. معنی‌هایی که نورایی می‌دهد ترجمهٔ آزاد آلمانیِ هرن است — نخستین صفت است و دومی نامِ مصدر، نه مصدر — ولی معنا و نسب درست است. ادعای نورایی پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mewk-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:223\", \"status\": \"supports\", \"note\": \"Horn p. 223 no. 994: 'aw. √maoč mit paiti \\\"anziehen (sc. Schuhe)\\\", vergl. framuxti- \\\"das Ausziehen (der Schuhe)\\\"' — both of Nourai's words with these very glosses, on the cited page.\"},\n            {\"ref\": \"SNS:247\", \"status\": \"partial\", \"note\": \"Tavoosi's Glossary of Šāyast nē Šāyast is on disk only as a very poor Persian OCR (SNS_pages.txt / SNS.txt, 243 leaves, printed page numbers unreadable). The Latin transliterations are legible, and the lemma 'paitišmuxta-, paitišmuxta-' does occur twice, at SNS_pages.txt lines 9799 and 9871 (leaves 140-141), on a page whose printed number OCRs as 'ETV' (plausibly ۲۴۷). So the cited page almost certainly does carry the word, but the OCR is too poor to read the entry itself; the Avestan facts were checked in Bartholomae instead.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch cols. 42, 826, 1002, 1682 (BRT.txt lines 2945, 15097, 17743, 27918)\", \"stance\": \"supports\", \"note\": \"'j. paiti.smuxta-, *paitiš.muxta- Adj. (fem. °tā-) \\\"mit Fusszeug bekleidet, beschuht\\\": arədvī sūra .. aoθra °ta (NSf.) zaranyō.tuvixšna Yt. 5.64; 78' and 'j. fra-muxtay- f. \\\"Losbinden, Ausziehen (des Schuhwerks)\\\": hat aoθranąm °ti V. 6.27'. Bartholomae even prints Nourai's variant spelling *paitiš.muxta-.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 744, s.v. meug-2, meuk- (POK_full.txt)\", \"stance\": \"supports\", \"note\": \"'Avestan fra-muxti- \\\"loosening\\\"' stands there beside OInd. muñcati 'releases' — confirming both the form and the derivation from the 'slip/release' root.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"môč\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"As with node 1, this is a verbal root turned into a noun by mistake. Horn p. 223 writes 'ai. √mōč- mit ā, prati \\\"anziehen (irgend ein Kleidungsstück)\\\", mit upa \\\"Schuhe anziehen\\\"' — the Old Indic root muc-/moc- 'to release, let loose', which with the preverbs ā-, prati- means 'to put on (a garment)' and with upa- 'to put on shoes'. Sanskrit has no noun môč 'shoe'. The Indic noun that does mean 'boot, stocking', मोजा mojā (Marathi mōjā, Bengali/Gujarati/Nepali mojā), is a late borrowing FROM Persian موزه mōza, i.e. the arrow would have to point the other way; and मोच mocá is 'the banana tree'. The root itself is genuine and is indeed the Indic match of Av. muč- (PIE *(s)mewk- 'to let loose, release'; Skt. muñcáti, muktá- 'released' = Av. muxta-), so the comparison Nourai intends is correct — only the part of speech and the gloss are Nourai's error, taken over from misreading Horn's √ sign. The printed page confirms the book prints 'môč : shoe'.\",\n          \"derivation_fa\": \"مانند گرهٔ ۱، اینجا نیز ریشه‌ای فعلی به اشتباه نام شده است. هرن در ص ۲۲۳ نوشته: «هندی باستان √mōč- با ā و prati «پوشیدن (هر قطعه جامه)»، با upa «کفش پوشیدن»» — یعنی ریشهٔ سنسکریت muc-/moc- «رها کردن» که با این پیشوندها معنی «پوشیدن» می‌گیرد. در سنسکریت نامی به صورت môč به معنی «کفش» وجود ندارد؛ واژهٔ هندیِ «جوراب/چکمه»، یعنی मोजा mojā (مراتی mōjā، بنگالی mojā)، وام‌واژه‌ای متأخر از فارسیِ «موزه» است، پس پیکان باید در جهت مخالف کشیده شود؛ و मोच mocá در سنسکریت «درخت موز» است. با این همه، خودِ ریشه اصیل است و همتای هندیِ muč- اوستایی است (هندواروپایی *(s)mewk-؛ سنسکریت muñcáti و muktá- «رهاشده» = اوستایی muxta-)، پس سنجشی که نورایی در نظر داشته درست است و تنها مقولهٔ دستوری و معنی نادرست است؛ این خطای کتاب است، نه خطای خوانش اسکن.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A5%8B%E0%A4%9C%E0%A4%BC%E0%A4%BE\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mewk-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:223\", \"status\": \"partial\", \"note\": \"Horn p. 223 no. 994 (HRN.txt leaf 244): 'ai. √mōč- mit ā, prati \\\"anziehen (irgend ein Kleidungsstück)\\\", mit upa \\\"Schuhe anziehen\\\"'. The page carries the item, but as a verbal root with preverbs, not as a noun glossed 'shoe'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 744, s.v. meug-2, meuk- (POK_full.txt)\", \"stance\": \"supports\", \"note\": \"'B. Old Indic *munakti, muñcati, mucati \\\"releases, allows to loose\\\", mukti- \\\"release, abandonment\\\"' — the Sanskrit item in this family is the verb, exactly as Horn has it.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, s.v. muk- (mūk-, munk-) 'leave' (IEC.txt line 11348)\", \"stance\": \"supports\", \"note\": \"'Skt. mucámi, muñcámi, pp: muktáh \\\"leave, release\\\"; … Av. muč- \\\"let, release\\\"' — Sanskrit and Avestan are paired as verbs, with no 'shoe' noun.\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson (HJB.txt) / Wiktionary मोज़ा\", \"stance\": \"contradicts\", \"note\": \"The Indic word for a stocking/boot, mojā, is a borrowing from Classical Persian موزه mōza (< MP mōzag < PIr *hmáwčakah), attested across Assamese, Bengali, Gujarati, Marathi and Nepali — so an Indic 'shoe' word cannot be the sibling source Nourai's tree implies.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Old English\",\n          \"words\": \"měo, měon\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"The Old English word is real: Bosworth-Toller has 'méo, méon: a shoe or sock covering the foot — Meó pedula, Wrt. Voc. i. 26, 2. Meón pedulos', i.e. it glosses Latin pedula/pedulis, the part of the hose or boot that covers the foot; Nourai's gloss 'shoe sole' is a shade too narrow ('sock, foot-covering' is better). What could not be verified is the ARROW. Mann (IEC:1643) is Nourai's only authority, and that page falls in the part of Mann's dictionary missing from the local scan; no other book on disk connects méo with this root — Pokorny's meug-2/meuk- (744) and meuk- (745) list no Old English méo, Walde-Pokorny II 253-255 likewise not, and Watkins' appendix has nothing. Phonologically the link is not obvious either: PIE *meuk- should give Germanic *meuk- > OE *méoc/mȳc, not a vowel-final méo, so Mann's comparison would require a suffixless *meu-(n)- beside the *meuk- of the Iranian branch. Given that méo is a gloss word appearing only in Latin-English glossaries, a borrowing or a substrate origin is at least as likely. Reported as unverified rather than disputed because no source was found that argues either way.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی کهن واقعی است: فرهنگ بازورث–تالر آورده «méo, méon: کفش یا جورابی که روی پا را می‌پوشاند — Meó pedula … Meón pedulos»، یعنی برگردان لاتینی pedula «آن بخش از ساق‌پوش که پا را می‌پوشاند»؛ معنی‌ای که نورایی می‌دهد («کفِ کفش») کمی تنگ‌تر از معنای اصلی است. آنچه تأیید نشد خودِ پیکان است: تنها مأخذ نورایی مان (IEC:1643) است و آن صفحه در بخشی از فرهنگ مان است که در نسخهٔ اسکن‌شدهٔ کتابخانهٔ محلی نیست؛ هیچ کتاب دیگری این واژه را به این ریشه نمی‌بندد — پوکورنی (۷۴۴ و ۷۴۵)، والده‑پوکورنی و واتکینز هیچ méo انگلیسی کهن نمی‌آورند. از دید آوایی نیز پیوند بدیهی نیست: *meuk- هندواروپایی در ژرمنی باید *meuk- و در انگلیسی کهن *méoc شود، نه méo، پس سنجش مان صورتی بی‌پسوند *meu-(n)- می‌طلبد. چون méo تنها در واژه‌نامه‌های لاتینی–انگلیسی دیده می‌شود، وام‌گیری هم به همان اندازه محتمل است. داوری: ناتأییدشده، نه ردشده.\",\n          \"sources\": [\n            \"https://bosworthtoller.com/search?q=meo\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:1643\", \"status\": \"not_checked\", \"note\": \"The local OCR of Mann (IEC.txt) stops at printed p. ~1554 (leaf 856 = '1554'); p. 1643 belongs to the Supplement, which the scan does not include. Checked the m- range of the main dictionary (leaves 455-457, pp. 812-816): it has muk- 'leave', mūk- (1) 'grow dark', mūk- (3) 'clamp', mūkóo(n) 'pike', muktos 'left, freed' and mūk- 'beat' — no 'shoe' root and no OE méo.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 744-745, s.vv. meug-2/meuk- and meuk- (POK_full.txt)\", \"stance\": \"silent\", \"note\": \"Both roots list Germanic material (OE smoc, smugan, ON mjúkr, OE ge-myscan) but no OE méo/méon; grep 'méo' in POK_full.txt returns only Latin meo 'to go' and OE meos 'moss' under meus-.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein (KLN_1966.txt) and Skeat (SKT.txt)\", \"stance\": \"silent\", \"note\": \"Neither has an entry for the OE gloss word méo (it left no Modern English descendant), so they cannot speak to the root.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins appendix (AHD_watkins1985.txt)\", \"stance\": \"silent\", \"note\": \"No 'shoe' root, and no Old English méo anywhere in the appendix.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Mew, Meu 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *meu-2, *meu̯ə- 'to move, push away' (Pokorny 743; Watkins meuə-; modern notation *m(y)ewh₁-)\",\n      \"note\": \"Pokorny IEW 743 has exactly this root: 'Root/lemma: meu-2, meuə- | Meaning: to move | Note: (Aryan partly also mi̯euə- : mīu-) | Material: Old Indic mīvati \\\"shoves, throngs, moves\\\" = Avestan ava-mivāmahi \\\"we remove, take away\\\", Avestan a-muyamna- \\\"unbeweglich\\\" …; Latin moveō, -ēre \\\"to move, stir, set in motion\\\", participle motus (*movi-to-s) = Umbrian comohota …'. Watkins gives the same root as 'meuə-. To push away.' with the whole English word-list that Nourai copies, and Etymonline still cites PIE '*meue- \\\"to push away\\\"' for move. Nourai's numbering 'Mew, Meu 2' matches Pokorny's 'meu-2'; the gloss 'to push away, move' is Watkins' wording plus Pokorny's. Modern reconstruction writes the root with a laryngeal, *m(y)ewh₁-, which is why Latin has moveō with -v- and Sanskrit mīvati; nothing in the chart is affected by that notational change. All four nodes are right except that the Avestan form is only attested with the preverb ava- (node 1) and the Pahlavi forms of node 2 could not be traced (see there).\",\n      \"note_fa\": \"پوکورنی در ص ۷۴۳ همین ریشه را دارد: «meu-2, meuə- : جنبیدن، پیش راندن»، با این مواد: «هندی باستان mīvati «می‌راند، می‌جنباند» = اوستایی ava-mivāmahi «دور می‌کنیم»، اوستایی a-muyamna- «بی‌حرکت»؛ لاتین moveō با صفت مفعولی motus». واتکینز نیز همین ریشه را «meuə- : پیش راندن، دور کردن» می‌آورد و همان فهرست واژه‌های انگلیسی را که نورایی نقل کرده است می‌دهد، و اتیمانلاین هنوز برای move ریشهٔ *meue- «پیش راندن» را می‌آورد. شمارهٔ «Meu 2» نورایی با «meu-2» پوکورنی می‌خواند و معنی نیز درست است. بازسازی امروزی این ریشه را با حنجره‌ای می‌نویسد، *m(y)ewh₁-، که همان چیزی است که ‑v‑ لاتین moveō و mīvati سنسکریت را توضیح می‌دهد؛ این تغییر نگارشی در هیچ‌کدام از پیکان‌های نمودار اثری ندارد. ادعای نورایی در جعبهٔ ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/moveo\",\n        \"https://www.etymonline.com/word/move\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:743\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: meu-2, meua- | Meaning: to move | Material: Old Indic mīvati \\\"shoves, throngs, moves\\\" = Avestan ava-mivāmahi \\\"we remove, take away\\\", Avestan a-muyamnō \\\"unbeweglich\\\" …; Latin moveo, -ēre \\\"to move, stir, set in motion\\\", participle motus (*movi-to-s) = Umbrian comohota … | References: WP. II 252 f., WH. II 116 | Page(s): 743'. Root, page, gloss and both branches of Nourai's chart.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins, s.v. meuə- (AHD_watkins1985.txt line 760)\", \"stance\": \"supports\", \"note\": \"'meuə-. To push away. Latin movēre, to move (> mobilis, neuter mobile, fickle, changeable): MOB, MOBILE, MOMENT, (MOMENTOUS), MOMENTUM, MOSSO, (MOTIF), MOTION, MOTIVE, MOTOR, MOVE, MOVEMENT; COMMOTION, EMOTION, PROMOTE, (REMOTE), (REMOVE). [Pok. 2. meu- 743.]' — Nourai's gloss and his English list both come from here.\"},\n        {\"src\": \"ISS\", \"where\": \"Bailey, Dictionary of Khotan Saka s.v. vamūda- (ISS_alt_DKS.txt char. 6838)\", \"stance\": \"supports\", \"note\": \"'vamūda- \\\"move away from\\\" … to base mūr- \\\"move\\\", see mvīr- < *mūr-y-, with -r- to base Av. amyav-, :miv- \\\"remove\\\", O.Ind. mīvati. IE Pok. 743 meu- \\\"thrust away\\\", O.Ind. mīv-:mū-, mīvati, mūta-, Av. amuyamna-, … Lat. moueō, mōtus, Lit. mauju, mauti \\\"put on (ring on finger)\\\"'. Bailey's own presentation of the root, with Nourai's Avestan forms.\"},\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 252 f. (cited by Pokorny 743 as 'WP. II 252 f.')\", \"stance\": \"supports\", \"note\": \"Pokorny's reference for this root is WP II 252 f.; the local WLD_Bd2_pages.txt OCR of that stretch is legible only in patches (the 'wegschieben' hit at char. 2120236 belongs to a different root, sqeud-), so WLD is recorded here as the source Pokorny himself compiles from rather than as an independent re-reading.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"mivâmahi; a-muyamnô\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both Avestan forms are genuine and both belong to this root, as Pokorny 743 states in so many words. (a) mivāmahi is the 1st pl. pres. act. of miv- 'to push, remove', but it is attested only with the preverb ava-: Vidēvdād 18.55 'hakat vaēm ava.mivāmahi hiiavasca pivasca' ('together we remove …'), quoted by Bartholomae s.v. hakat; so the bare 'mivâmahi' of the chart is an abstraction from ava.mivāmahi, and Nourai's gloss '(we) eliminate' is the sense of the compound. Skt. mīvati 'shoves, moves' is the exact Indic match, i.e. Indo-Iranian *miu̯- < PIE *m(y)ewh₁-. (b) a-muyamna- is the negated middle participle 'not to be moved, immovable', a-priv. + muyamna- (a -mna- participle of the same root with the regular Avestan development *muu̯- > muy-), attested at Vidēvdād 17.13 and 13.35 of the 'straightest path' (razišta- pantā-) and at Yasna 71.13 / Vīsprad 7.1 ('°tāca amuyamna yazamaide'), all listed in Bartholomae. Bailey brings the two together under the same root when explaining Khotanese vamūda-.\",\n          \"derivation_fa\": \"هر دو صورت اوستایی اصیل‌اند و هر دو به همین ریشه بازمی‌گردند، چنان‌که پوکورنی در ص ۷۴۳ صریحاً می‌گوید. نخست mivāmahi صیغهٔ اول‌شخص جمع حال از ریشهٔ miv- «راندن، دور کردن» است، ولی تنها با پیشوند ava- گواهی شده: وندیداد ۱۸ بند ۵۵ «hakat vaēm ava.mivāmahi …»، که بارتولمه زیر hakat نقل کرده است؛ پس صورت بی‌پیشوندِ نمودار انتزاعی از ava.mivāmahi است و معنی‌ای که نورایی می‌دهد معنی همان ترکیب است. همتای دقیق هندی آن mīvati است، یعنی هندوایرانی *miu̯- از هندواروپایی *m(y)ewh₁-. دوم a-muyamna- صفت فاعلی میانهٔ منفی به معنی «جنبانیدنی‌نیست، بی‌حرکت» است: پیشوند نفی a- به‌علاوهٔ muyamna- (صفت ‑mna- از همان ریشه، با تحول قاعده‌مند *muu̯- به muy- در اوستایی) که در وندیداد ۱۷ بند ۱۳ و ۱۳ بند ۳۵ در توصیف «راست‌ترین راه» و در یسنا ۷۱ بند ۱۳ آمده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/moveo\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:743\", \"status\": \"supports\", \"note\": \"'Old Indic mīvati \\\"shoves, throngs, moves\\\" = Avestan ava-mivāmahi \\\"we remove, take away\\\", Avestan a-muyamno \\\"unbeweglich, wovon nicht abzubringen\\\"' (POK_full.txt s.v. meu-2). Note Pokorny gives the Avestan verb with ava-.\"},\n            {\"ref\": \"ISS:331\", \"status\": \"not_checked\", \"note\": \"Bailey, Indo-Scythian Studies VI (Prolexis to the Book of Zambasta), Cambridge 1967 is not available online (HathiTrust mdp.39015034317936 is search-only; archive.org khotanesetexts0103bail has vols I-III only, lending). The substitute on disk is Bailey's Dictionary of Khotan Saka (1979) = ISS_alt_DKS.txt, whose entry vamūda- carries the same doctrine and the same Avestan forms (see 'consulted').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, s.vv. hakat (col. 1738; BRT.txt line 28878), a-stənəta- (line 5815), razišta- (line 25241), °taya (line 30509)\", \"stance\": \"supports\", \"note\": \"'hakat … α) bei den Wörtern für \\\"beide\\\" und \\\"alle\\\": h° vaēm ava.mivāmahi hiiavasca pivasca V. 18.55' and 'amuyamna °tanąm (näml. paθąm) V. 17.13; 13.35', '°tāca amuyamna yazamaide Vr. 7.1'. Both forms attested, the verb only with ava-.\"},\n            {\"src\": \"ISS\", \"where\": \"Bailey, DKS s.v. vamūda- (ISS_alt_DKS.txt char. 6838)\", \"stance\": \"supports\", \"note\": \"'to base mūr- \\\"move\\\" … to base Av. amyav-, :miv- \\\"remove\\\", O.Ind. mīvati. IE Pok. 743 meu- \\\"thrust away\\\", … Av. amuyamna-, … Lat. moueō, mōtus'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. meuə- (AHD_watkins1985.txt)\", \"stance\": \"silent\", \"note\": \"Watkins' entry keeps only the Latin branch; no Avestan material, so it neither supports nor contradicts this node.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"mŭtak; parmŭtan\",\n          \"verdict\": \"unverified\",\n          \"derivation\": \"Neither form could be confirmed as a Middle Persian word for 'move'. MacKenzie's Concise Pahlavi Dictionary has no mūtak and no parmūdan/parmūtan (its nearest items are framūdan 'to command, put to use' — a different root, fra-mā- 'to measure, order' — and paymōxtan 'to don'). Nyberg's Manual of Pahlavi II does have a lemma 'mūtak [mwtk'] *destructive, of Hēšm 61.9. — FrO XI: mrūta (Av.) = mūtak; Vd. 272 mūtak of the winter, with the gloss kū čiš tapāh kunēt \\\"that is: it destroys everything\\\", rendering Av. mrūra-' — i.e. a completely different word, mūtak 'destructive' < Av. mrūra-, not 'move'; and Bailey's DKS gives mātak 'base, matter' (Khotanese māva). Bailey's Khotanese forms for this root are mūr-/mvar-/mvīr- 'to move' and vamūda- 'move away from', not Pahlavi. The likeliest reading is that Nourai took over from ISS:331 a pair of Pahlavi Vidēvdād glosses rendering Av. ava-miv- (a past stem *mūt- with a preverb, i.e. *(a)par-mūtan 'to remove'), which Bailey read from the Pahlavi translation; since Indo-Scythian Studies VI is not obtainable, and since neither MacKenzie nor Nyberg nor any other dictionary on disk knows such a verb, the node stands unverified. The printed page (pdf 339) reads 'mŭtak : move / parmŭtan : to move' under 'Pahlavi ISS:331', so the JSON is a faithful extraction — this is not a scanning error.\",\n          \"derivation_fa\": \"هیچ‌یک از دو صورت را نتوانستم به عنوان واژهٔ فارسی میانه به معنی «جنبیدن» تأیید کنم. در فرهنگ پهلوی مکنزی نه mūtak هست و نه parmūdan/parmūtan (نزدیک‌ترین واژه‌ها framūdan «فرمودن، به کار بستن» از ریشهٔ دیگر fra-mā-، و paymōxtan «پوشیدن» است). نیبرگ در «راهنمای پهلوی» مدخل «mūtak [mwtk'] ویران‌کننده، صفت هَشم» را دارد که برگردان اوستایی mrūra- است و هیچ پیوندی با «جنبیدن» ندارد؛ و بیلی در فرهنگ ختنی mātak «پایه، مادّه» را می‌آورد. صورت‌هایی که بیلی برای این ریشه می‌دهد ختنی‌اند نه پهلوی: mūr-, mvar-, mvīr- «جنبیدن» و vamūda- «دور شدن از». احتمال قوی این است که نورایی از ص ۳۳۱ کتاب «مطالعات هندوسکایی» بیلی دو صورت از حواشی پهلویِ وندیداد را گرفته است که ava-miv- اوستایی را ترجمه می‌کنند (ستاک گذشتهٔ *mūt- با پیشوند، یعنی *(a)par-mūtan «دور کردن»)؛ اما چون جلد ششم آن کتاب در دسترس نیست و هیچ فرهنگ پهلوی موجود چنین فعلی را نمی‌شناسد، این گره «ناتأییدشده» می‌ماند. تصویر صفحهٔ چاپی نشان می‌دهد که کتاب همین صورت‌ها را چاپ کرده است؛ پس خطای خوانش اسکن در میان نیست.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"ISS:331\", \"status\": \"not_checked\", \"note\": \"Indo-Scythian Studies: Khotanese Texts VI (1967) is not obtainable (see node 1). Searched the substitute, Bailey's Dictionary of Khotan Saka (ISS_alt_DKS.txt), for 'parmūt', 'parmud', 'mūtak', 'mutak': the only hits are mātak 'base, matter' and, for this root, the Khotanese forms mūr-/mvar-/mvīr- 'to move' and vamūda- — no Pahlavi mūtak/parmūtan.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD.txt, PHD_mackenzie.txt)\", \"stance\": \"silent\", \"note\": \"grep 'mūtak', 'parmūd', 'parmut' finds nothing; MacKenzie's only fra-/pati- verbs of this shape are 'framūdan: put to use' (< fra-mā-) and 'paymōxtan, paymōz- … don, wear'. No Middle Persian verb 'to move' from *mav-.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, Glossary s.v. mūtak (NYB_vol2_glossary.txt)\", \"stance\": \"contradicts\", \"note\": \"'mūtak [mwtk'] *destructive, of Hēšm 61.9. — FrO XI: mrūta (Av.) = mūtak; Vd. 272 mūtak of the winter, with the gloss kū čiš tapāh kunēt \\\"that is: it destroys everything\\\", rendering Av. (1197) mrūra-.' The one Pahlavi mūtak on record means 'destructive' and comes from Av. mrūra-, not from *mav- 'to move'.\"},\n            {\"src\": \"ISS\", \"where\": \"Bailey, DKS s.vv. mvar-, mvīr-, vamūda- (ISS_alt_DKS.txt)\", \"stance\": \"partial\", \"note\": \"'mvar- \\\"to move\\\" … See mūr- \\\"to move\\\", and mvīr-'; 'mvīr- \\\"to move\\\" … From mvar-: mūr- mūry- > mvir-'; 'vamūda- \\\"move away from\\\" … to base mūr- \\\"move\\\"'. Bailey does have a *mūt-/mūr- family for this root — but in Khotanese, not in Pahlavi.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"movêre\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Lat. moveō, movēre, mōvī, mōtum 'to move, set in motion, stir, remove, disturb' is the Italic reflex of this root: Proto-Italic *moweō < PIE *m(y)ewh₁- (Pokorny's meu-2), with the participle mōtus for *movi-tos (the same formation as Umbrian comohota 'a moving'), and the frequentative mōtāre behind motion-words. Nourai's parent (the IE root) and gloss are both what Pokorny 743, Watkins and Klein give; Klein s.v. move calls Latin movēre 'prob. cogn. OI mīvati, \\\"pushes, moves\\\", kāma-mūtaḥ \\\"moved by love\\\", Toch. AB mus- \\\"to move\\\", Gk. ἀμεύσασθαι \\\"to surpass, outstrip\\\", ἀμύνειν \\\"to keep off\\\", Lith. mauju, mauti \\\"to strip off\\\"'.\",\n          \"derivation_fa\": \"فعل لاتین moveō / movēre (صفت مفعولی mōtum) «جنباندن، به حرکت آوردن، دور کردن» بازتاب ایتالیکِ همین ریشه است: ایتالیک آغازین *moweō از هندواروپایی *m(y)ewh₁- (همان meu-2 پوکورنی)، با صفت مفعولی mōtus از *movi-tos — همان ساختی که در اومبریایی comohota دیده می‌شود — و فعل تکراری mōtāre که واژه‌های خانوادهٔ motion از آن است. پیکان و معنیِ نورایی هر دو با پوکورنی ص ۷۴۳، واتکینز و کلاین می‌خواند؛ کلاین زیر move می‌نویسد که movēre «احتمالاً هم‌ریشه با سنسکریت mīvati «می‌راند»، تخاری mus- «جنبیدن»، یونانی ἀμύνειν «دور راندن» و لیتوانیایی mauti است». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/moveo\",\n            \"https://www.etymonline.com/word/move\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins (AHD_watkins1985.txt line 760): 'meuə-. To push away. Latin movēre, to move (> mobilis, neuter mobile, fickle, changeable) … [Pok. 2. meu- 743.]' Nourai cites 'AHD' without a page; the appendix entry is exactly this.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 743, s.v. meu-2 (POK_full.txt)\", \"stance\": \"supports\", \"note\": \"'Latin moveō, -ēre \\\"to move, stir, set in motion, shake, disturb, remove\\\", participle motus (*movi-to-s) = Umbrian comohota Abl. Sg. f. \\\"a moving, motion\\\"'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein p. 1010 s.v. move (KLN_1966.txt)\", \"stance\": \"supports\", \"note\": \"'move, tr. and intr. v. — ME. moven, fr. AF. mover, corresponding to OF. moveir, movoir (F. mouvoir), fr. L. movēre (pp. motus), \\\"to move, set in motion\\\", which is prob. cogn. OI. mīvati, \\\"pushes, moves\\\", kāma-mūtaḥ, \\\"moved by love\\\", Toch. AB mus-, \\\"to move\\\", Gk. ἀμεύσασθαι …, ἀμύνειν …, Lith. mauju, mauti, \\\"to strip off\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"mobile, momentum, motion, motive, motor, move, commotion, emotion, promote, remote, remove\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All eleven words are Latin-based and all go back to movēre or its participle mōtus. The inherited-looking one, move, came in through French: ME moven < Anglo-French mover / Old French movoir (Modern French mouvoir) < movēre, first attested late 13th c. The rest are learned or French borrowings of Latin derivatives: mobile < mobilis (< *movi-bilis) 'movable'; momentum < mōmentum (< *movi-mentum) 'movement, moment'; motion < mōtiōnem; motive < Late Latin mōtīvus; motor < mōtor 'mover'; remove < Old French removoir < removēre; remote < remōtus 'removed, far off'; promote < prōmōtus 'moved forward'; commotion < commōtiōnem (com- + movēre) 'violent movement, agitation'; emotion < French émotion < ēmovēre 'to move out, stir up'. Klein s.v. move cross-refers to exactly this set (mob, mobile, moment, motion, motive, motor, promote, remote, commove, remove) and Watkins' appendix prints the same list under meuə-. Nourai's list is a proper subset of Watkins' (he omits MOB, MOMENT(OUS), MOSSO, MOTIF, MOVEMENT), so nothing in it is unsupported.\",\n          \"derivation_fa\": \"همهٔ این یازده واژه لاتینی‌تبارند و همه به movēre یا صفت مفعولی mōtus بازمی‌گردند. تنها واژه‌ای که کهن به نظر می‌رسد، move، از راه فرانسه آمده است: انگلیسی میانه moven از انگلونرمان mover / فرانسهٔ کهن movoir از movēre، با نخستین گواهی در پایان سدهٔ سیزدهم. بقیه وام‌واژه‌های دانشورانه یا فرانسویِ مشتق‌های لاتین‌اند: mobile از mobilis «جنبنده»، momentum از mōmentum، motion از mōtiōnem، motive از mōtīvus لاتینی متأخر، motor از mōtor «جنباننده»، remove از removēre، remote از remōtus «دورشده»، promote از prōmōtus، commotion از commōtiōnem «جنبش سخت، آشفتگی» و emotion از فرانسهٔ émotion از ēmovēre. کلاین زیر move به همین مجموعه ارجاع می‌دهد و واتکینز نیز همان فهرست را زیر meuə- چاپ کرده است؛ فهرست نورایی زیرمجموعهٔ فهرست واتکینز است، پس هیچ عضوی از آن بی‌پشتوانه نیست. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/move\",\n            \"https://en.wiktionary.org/wiki/moveo\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. meuə- lists 'MOB, MOBILE, MOMENT, (MOMENTOUS), MOMENTUM, MOSSO, (MOTIF), MOTION, MOTIVE, MOTOR, MOVE, MOVEMENT; COMMOTION, EMOTION, PROMOTE, (REMOTE), (REMOVE)' — every one of Nourai's eleven words is in this list (the AHD index confirms each: 'MOTION meue-', 'EMOTION meue-', 'MOBILE' etc.).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein pp. 1010 (move), 366 (commotion), 508 f. (emotion) (KLN_1966.txt)\", \"stance\": \"supports\", \"note\": \"'commotion, n. — F., fr. L. commotionem, acc. of commotio, \\\"violent movement, agitation, excitement\\\", fr. commotus, pp. of commovere … fr. com- and movere, \\\"to move\\\"'; s.v. move: 'Cp. also emeute, mob, \\\"rabble\\\", mobile, moment, Motacillidae, motatorious, motion, motive, motor, mutiny, promote, remote'.\"},\n            {\"src\": \"SKT\", \"where\": \"Etymonline s.v. move (archived) as the modern equivalent of Skeat\", \"stance\": \"supports\", \"note\": \"'The verb \\\"move\\\" entered English in the late 13th century from Anglo-French mover and Old French movoir, from Latin movere \\\"move, set in motion; remove; disturb\\\", past participle motus, frequentative motare. The ultimate source is the Proto-Indo-European root *meue- \\\"to push away\\\".'\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-07T17:58:09.158Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-339.json (file state is current in your context — no need to Read it back)
```


## [2026-09-07T17:58:13.399Z] TOOL CALL #75: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-339.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 339",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-07T17:58:14.897Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'disputed': 1, 'confirmed': 8, 'plausible': 3, 'unverified': 2}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'partial': 4, 'supports': 9, 'not_checked': 4}
books consulted: {'partial': 7, 'contradicts': 4, 'supports': 19, 'silent': 10} | by book: {'KLN': 5, 'BRT': 4, 'POK': 4, 'IEC': 3, 'BQT': 3, 'PHD': 3, 'WLD': 2, 'NYB': 2, 'AHD': 2, 'ISS': 2, 'HUB': 1, 'ARY': 1, 'LEW': 1, 'FSD': 1, 'WEB': 1, 'HRN': 1, 'FSF': 1, 'MON': 1, 'HJB': 1, 'SKT': 1}
```


## [2026-09-07T17:58:37.241Z] AGENT

Done. `python3 tools/verify_check.py 339` → 14/14 nodes, **0 PROBLEM lines**.

**Page 339 (book p. 309) — 3 entries, 14 nodes**

Verdicts: nodes — 8 confirmed, 3 plausible, 1 disputed, 2 unverified. Roots — 2 confirmed, 1 plausible. Ref checks: 9 supports, 4 partial, 4 not_checked.

Flagged items:
- **disputed** — *Meuk* (scratch) #1 Av. `mušti` "fist": word is real (Bartholomae col. 1189, only in `mušti.masah-`), but Pokorny 745 attaches it only with "vielleicht" and WP II 255 hedges twice; modern view takes it to PIE *méws-ti-s (root *mews- "shut", Toch. B maśce), calling *mewḱ- dubious. Mann files it under a separate root *mūk- "beat".
- **plausible** — root *Meuk* "stocking, boot": the root is real but is Pokorny's *meug-2/meuk-* "to slide, slip" (p. 744, uncited by Nourai); "stocking, boot" is the sense of the Iranian noun *mauka-*, not of the root.
- **plausible** — #1 Av. `maoč` "shoe, boot" and #5 Skt. `môč` "shoe": Nourai misread Horn's "√maoč" / "√mōč-" (verbal roots "to put on/strip off (shoes)") as nouns. No Av. noun *maoča-* exists (footwear = `aoθra-`); the Indic noun `mojā` "stocking" is a loan *from* Persian. Book's error, extraction faithful (page image checked).
- **plausible** — Lat. `mucrō`: Pokorny 745 supports, but WP II 255 itself prefers Zupitza's link to ON *smjúga*, and de Vaan allows a substrate origin.
- **unverified** — *Mew/Meu 2* #2 Pahlavi `mŭtak` "move", `parmŭtan` "to move": absent from MacKenzie; Nyberg's only `mūtak` means "destructive" (< Av. *mrūra-*); Bailey's forms for this root are Khotanese (`mūr-/mvar-/mvīr-`, `vamūda-`). Cited ISS:331 (Indo-Scythian Studies VI) is not obtainable.
- **unverified** — #6 OE `měo, měon`: word confirmed via Bosworth-Toller ("a shoe or sock…, gl. *pedula*"; gloss "shoe sole" too narrow), but the root attachment rests solely on IEC:1643, which falls in Mann's Supplement — missing from the local OCR (ends at printed p. ~1554).

Highlights of positive checks: BQT:2010 and BQT:2051 fetched with `ref_page.py` — Mo'in's footnotes support both the `مشت` and `موزه` chains verbatim (incl. Bartholomae 1189, Nyberg 153, Horn 994, Arabic معرب موزج from Ibn Durayd); HRN:220/223 exact; MON:4432 entry located; Bartholomae confirms `paiti.smuxta-` (Yt 5.64/78) and `fra-muxtay-` (V 6.27); FSF has the identical Ferdowsi verse; AHD/Watkins *meuə-* supplies Nourai's whole English list.

**Extraction errors: none.** The printed page matches the JSON on every node (page image copied to `data/verification/sources/refs/ocr/BOOK/339.png`). 9 web pages archived via `fetch_source.py`.
