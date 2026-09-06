# Verification process log — verify-page-309


## [2026-09-06T23:09:56.908Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 309 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-309.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-309.json. Write /home/sfmqrb/git/rishe/data/verification/page-309.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 309` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T23:09:58.224Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T23:09:58.986Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T23:09:59.006Z] TOOL RESULT

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


## [2026-09-06T23:09:59.574Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-309.txt"
}
```


### [2026-09-06T23:09:59.589Z] TOOL RESULT

```
1	=== PDF page 309 (book page 279) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Lěk, Lak; Lakt, Lakat : to tear; rag, scrap  (refs POK:674; IEC:660,661)
4	#1 (parent #0) [Persian] refs=IEC:661; MON:3563,3573 | laxt «لَخت ( لَت )» : scrap, piece, rag | NOTE: See "Letro" for another possible root.
5	#2 (parent #0) [Armenian] refs=IEC:661 | lat : cloth, rag
6	#3 (parent #0) [Latin] refs=AHD:1526 | lacer : torn
7	  #4 (parent #3) [English] refs=AHD | lacerate
8	#5 (parent #0) [Greek] refs=IEC:660 | lakis : rag
9	  #6 (parent #5) [Sanskrit] refs=IEC:661 | laktakah : rag
10	--- entry 1 ---
11	ROOT Leng -> redirect to Longos
12	--- entry 2 ---
13	ROOT Lenghô -> redirect to Longos
14	--- entry 3 ---
15	ROOT [Indo-European] Lep; Lepos; Lap-aro : to peel; flap, skin; soft, friendly  (refs IEC:680; POK:678; AHD:1526)
16	#1 (parent #0) [Persian] refs=IEC:680; MON:3518,3530 | lâf «لاف» : using soft and friendly words, bragging ; lâbeh «لابه» : flattery
17	#2 (parent #0) [Latin] refs=IEC:680 | lepos : wit
18	#3 (parent #0) [Greek] refs=AHD:1526 | laparos : soft
19	  #4 (parent #3) [English] refs=AHD | laparotomy : surgical incision into abdominal wall
20	--- entry 4 ---
21	ROOT Lepos -> redirect to Lep
22	--- entry 5 ---
23	ROOT [Indo-European] Lěs, Lěsâ, Lěsos, Lesiom : place, space, area  (refs IEC:680)
24	#1 (parent #0) [Persian] refs=IEC:680; MON:3522 | lâx «ـلاخ» : a suffix meaning place of | extra: سنگلاخ ، هندولاخ
25	#2 (parent #0) [Old High German] refs=IEC:680 | gi-lâri : room, dwelling
26	--- entry 6 ---
27	ROOT Lěsâ -> redirect to Lěs
28	--- entry 7 ---
29	ROOT Lesiom -> redirect to Lěs
30	
```


## [2026-09-06T23:10:00.129Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-309.json"
}
```


### [2026-09-06T23:10:00.144Z] TOOL RESULT

```
1	{
2	  "pdf_page": 309,
3	  "book_page": 279,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Lěk, Lak; Lakt, Lakat",
8	        "lang": "Indo-European",
9	        "refs": "POK:674; IEC:660,661",
10	        "gloss": "to tear; rag, scrap"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Persian",
17	          "refs": "IEC:661; MON:3563,3573",
18	          "words": [
19	            {"translit": "laxt", "gloss": "scrap, piece, rag", "script": "لَخت ( لَت )"}
20	          ],
21	          "script_extra": null,
22	          "note": "See \"Letro\" for another possible root.",
23	          "quote": {"text": "همان تخت پیروزه ده لَخت بود - جهان روشن از فَرّ آن تخت بود", "poet": "Ferdowsî"}
24	        },
25	        {
26	          "id": 2,
27	          "parent": 0,
28	          "lang": "Armenian",
29	          "refs": "IEC:661",
30	          "words": [
31	            {"translit": "lat", "gloss": "cloth, rag", "script": null}
32	          ],
33	          "script_extra": null,
34	          "note": null,
35	          "quote": null
36	        },
37	        {
38	          "id": 3,
39	          "parent": 0,
40	          "lang": "Latin",
41	          "refs": "AHD:1526",
42	          "words": [
43	            {"translit": "lacer", "gloss": "torn", "script": null}
44	          ],
45	          "script_extra": null,
46	          "note": null,
47	          "quote": null
48	        },
49	        {
50	          "id": 4,
51	          "parent": 3,
52	          "lang": "English",
53	          "refs": "AHD",
54	          "words": [
55	            {"translit": "lacerate", "gloss": null, "script": null}
56	          ],
57	          "script_extra": null,
58	          "note": null,
59	          "quote": null
60	        },
61	        {
62	          "id": 5,
63	          "parent": 0,
64	          "lang": "Greek",
65	          "refs": "IEC:660",
66	          "words": [
67	            {"translit": "lakis", "gloss": "rag", "script": null}
68	          ],
69	          "script_extra": null,
70	          "note": null,
71	          "quote": null
72	        },
73	        {
74	          "id": 6,
75	          "parent": 5,
76	          "lang": "Sanskrit",
77	          "refs": "IEC:661",
78	          "words": [
79	            {"translit": "laktakah", "gloss": "rag", "script": null}
80	          ],
81	          "script_extra": null,
82	          "note": null,
83	          "quote": null
84	        }
85	      ]
86	    },
87	    {
88	      "root": {
89	        "name": "Leng",
90	        "redirect": "Longos"
91	      },
92	      "nodes": []
93	    },
94	    {
95	      "root": {
96	        "name": "Lenghô",
97	        "redirect": "Longos"
98	      },
99	      "nodes": []
100	    },
101	    {
102	      "root": {
103	        "name": "Lep; Lepos; Lap-aro",
104	        "lang": "Indo-European",
105	        "refs": "IEC:680; POK:678; AHD:1526",
106	        "gloss": "to peel; flap, skin; soft, friendly"
107	      },
108	      "nodes": [
109	        {
110	          "id": 1,
111	          "parent": 0,
112	          "lang": "Persian",
113	          "refs": "IEC:680; MON:3518,3530",
114	          "words": [
115	            {"translit": "lâf", "gloss": "using soft and friendly words, bragging", "script": "لاف"},
116	            {"translit": "lâbeh", "gloss": "flattery", "script": "لابه"}
117	          ],
118	          "script_extra": null,
119	          "note": null,
120	          "quote": {"text": "در آن نامه سوگند های گران - فریبنده چون لابهٔ مادران", "poet": "Nezâmî"}
121	        },
122	        {
123	          "id": 2,
124	          "parent": 0,
125	          "lang": "Latin",
126	          "refs": "IEC:680",
127	          "words": [
128	            {"translit": "lepos", "gloss": "wit", "script": null}
129	          ],
130	          "script_extra": null,
131	          "note": null,
132	          "quote": null
133	        },
134	        {
135	          "id": 3,
136	          "parent": 0,
137	          "lang": "Greek",
138	          "refs": "AHD:1526",
139	          "words": [
140	            {"translit": "laparos", "gloss": "soft", "script": null}
141	          ],
142	          "script_extra": null,
143	          "note": null,
144	          "quote": null
145	        },
146	        {
147	          "id": 4,
148	          "parent": 3,
149	          "lang": "English",
150	          "refs": "AHD",
151	          "words": [
152	            {"translit": "laparotomy", "gloss": "surgical incision into abdominal wall", "script": null}
153	          ],
154	          "script_extra": null,
155	          "note": null,
156	          "quote": null
157	        }
158	      ]
159	    },
160	    {
161	      "root": {
162	        "name": "Lepos",
163	        "redirect": "Lep"
164	      },
165	      "nodes": []
166	    },
167	    {
168	      "root": {
169	        "name": "Lěs, Lěsâ, Lěsos, Lesiom",
170	        "lang": "Indo-European",
171	        "refs": "IEC:680",
172	        "gloss": "place, space, area"
173	      },
174	      "nodes": [
175	        {
176	          "id": 1,
177	          "parent": 0,
178	          "lang": "Persian",
179	          "refs": "IEC:680; MON:3522",
180	          "words": [
181	            {"translit": "lâx", "gloss": "a suffix meaning place of", "script": "ـلاخ"}
182	          ],
183	          "script_extra": "سنگلاخ ، هندولاخ",
184	          "note": null,
185	          "quote": null
186	        },
187	        {
188	          "id": 2,
189	          "parent": 0,
190	          "lang": "Old High German",
191	          "refs": "IEC:680",
192	          "words": [
193	            {"translit": "gi-lâri", "gloss": "room, dwelling", "script": null}
194	          ],
195	          "script_extra": null,
196	          "note": null,
197	          "quote": null
198	        }
199	      ]
200	    },
201	    {
202	      "root": {
203	        "name": "Lěsâ",
204	        "redirect": "Lěs"
205	      },
206	      "nodes": []
207	    },
208	    {
209	      "root": {
210	        "name": "Lesiom",
211	        "redirect": "Lěs"
212	      },
213	      "nodes": []
214	    }
215	  ]
216	}
217	
```


## [2026-09-06T23:10:04.896Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md | head -120",
 "description": "Read source matrix"
}
```


### [2026-09-06T23:10:04.937Z] TOOL RESULT

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


## [2026-09-06T23:10:06.105Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','AHD','MON','WLD','SYN','KLN','HRN','HUB','BQT','ARY','SKT','PHD','NYB']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-06T23:10:07.982Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
```


## [2026-09-06T23:10:11.471Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','AHD','MON']:\n    e=d[k]\n    print('==',k)\n    for f in ['local_file','page_offset','lookup_hint','scans']:\n        print(' ',f,':',str(e.get(f))[:600])\n\""
}
```


### [2026-09-06T23:10:13.141Z] TOOL RESULT

```
== POK
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
  page_offset : POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
  scans : None
== IEC
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
  page_offset : TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  lookup_hint : Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
  scans : None
== AHD
  local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
  page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
  lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves 
  scans : None
== MON
  local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
  page_offset : None
  lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded a
  scans : None
```


## [2026-09-06T23:10:17.543Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^Root / lemma: l[eēĕa]k\" POK_full.txt | head -30\necho \"-----\"\ngrep -n \"^Root / lemma: lep\" POK_full.txt | head -30\necho \"----- pages 674 678\"\ngrep -n \"Page(s): 67[0-9]\" POK_full.txt | head -40"
}
```


### [2026-09-06T23:10:17.622Z] TOOL RESULT

```
51285:Root / lemma: lak-2 
53684:Root / lemma: laku- {*lehuk-) 
53749:Root / lemma: lak- {*lehuk^ 
56672:Root / lemma: lek-2\ lak- 
-----
55367:Root / lemma: lep-1 {* lehup-) 
55398:Root / lemma: lep-2{*lehup-) 
----- pages 674 678
54900:Page(s): 670-671 
54920:Page(s): 671 
54951:Page(s): 671 
54987:Page(s): 672 
55008:Page(s): 672 
55026:Page(s): 672-673 
55044:Page(s): 673 
55080:Page(s): 673 
55130:Page(s): 674 
55156:Page(s): 675 
55188:Page(s): 675 
55215:Page(s): 675 
55236:Page(s): 675 
55256:Page(s): 676 
55283:Page(s): 676 
55322:Page(s): 676-677 
55365:Page(s): 677 
55396:Page(s): 677-678 
55439:Page(s): 678 
55459:Page(s): 678 
55481:Page(s): 679 
55499:Page(s): 679 
56668:Page(s): 673-674 
56719:Page(s): 674 
56753:Page(s): 679
```


## [2026-09-06T23:10:20.739Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== 56660-56760 (lek-2/lak-)\"; sed -n '56660,56760p' POK_full.txt\necho \"=== 55100,55160 (page 674 area)\"; sed -n '55100,55160p' POK_full.txt"
}
```


### [2026-09-06T23:10:20.805Z] TOOL RESULT

```
=== 56660-56760 (lek-2/lak-)

Maybe alb. /a/r"trap, snare, rope' a Latin loanword. 

Old English /se/{a)'bN\g, branch, lash, scourge, bullwhip, horsewhip; spur, mark from a 
blow' ( 75/7//-)? 

References: WP. II 421 f., WH. I 744 f. 
See also: Perhaps to /ek-2. 
Page(s): 673-674 



Root / lemma: lek-2\ lak- 

Meaning: to tear, fell, fur, leather, bark, outer covering of a tree, pod 

Comments: 

Root/ lemma: lehk-1: lahk-\ trap' : Root/ lemma: lehk-2. lahk-\ to tear, fell, fur, leather, 

bark, outer covering of a tree, pod ' derived from *nak{u), laH^U) of Root / lemma: nohg"-, 

nohg''ohd(h)oh- nohg^-noh- : naked'. 

Material: Gr. AaKi(; 'scrap, shred', AaKO(; n. ds. (AoKri paKr|. Kpf|T£(; Hes.), AoKi^w "tear, 

rend' ansAriKa ansppwYQ. Kunpioi Hes.; 

alb. /a/r^/*" naked', lekure, //kureleW, fur, leather, bark, outer covering of a tree, pod '; 

Maybe alb. /akur/'q' bat ' 

Notes: 

' bat ' in Baltic Languages: Latvian "siksparnis" = "leather wing", Lithuanian "siksnosparnis" 

= "leather wing", Celtic Languages: Breton "askell-groc'hen" = "skin wing", Irish (A) 

"sciathan leathair" = "leather wing", Welsh "ystlum" = "a flitch of (bacon)", "slumyn" = "a 

flitch of (bacon)"; "ystlumyn bacwn" = "a flitch of bacon". 

Albanian /akuriq// nates' bat of the night [literally (the naked skin of the night)] ' derived 

from Albanian lakura' skin, leather ', lakuriq' naked skin, stark naked ' which was a 

translation of Celtic, Baltic names for bat. Suspended from the ceiling on hooks, skins are 

reminiscent of the way that "bats" hang when roosting. 

Latin lacer, -era, -erum' to tear to pieces, mangle, rend, mutilate, lacerate ', lacerna' a 
cloak worn over the toga, hooded shawl, lacerna, travelling-cloak, military cloak ', laciniai. 
" a lappet, flap, edge, hem '; lancino, -are "tear, rend, squander, dissipate '; 

poln. iach, russ. /ochma'scrap, shred' (express, ch), etc. 

Maybe alb. //okma'scrap, shred' a Slavic loanword. 

References: WP. II 419 f., WH. I 742 f. 
Page(s): 674 

Root / lemma: /ehp- lohp- lahp- 

Meaning: flat 

Material: Kurdish lapk' paw '; 



Gothic /d/^rn., Old Icelandic ldfixr\. 'flat hand'; Middle Low German Middle English lof 
Windseite ', actually " big rudder with which the ship was held to the wind '; changing 
through ablaut geminated Old High German laffai.. Middle High German and dial. Modern 
High German laffe^i\a\. hand, shoulder', Old High German lappom. 'flat hand, rudder 
blade ' (also in Modern High German Barlapp^\)/co'^o6\\}vc\'), Norwegian Swedish /abbm., 
Danish /ab^ paw ', isl. /oppi. < Modern High German dial, /aff' dandelion '; with /7^forms 
Norwegian dial. /0/77' paw ' {*/dbma-), band/dm ^ pa\m' , isl. /umma'b\g, giant hand'; 

Latvian /^pai. ' paw; Huflattig ', also " water lily, lotus plant ' (compare above Modern 
High German /aff^ dandelion '); ablaut. East Latvian fuopa, through derailment of ablaut 
Latvian /apa, Lithuanian /opa^ paw '; also Lithuanian /apasleaV, Latvian /apa6s.; 

russ. etc. /apa' paw', poln. fapads., fap/n/ec' lycopodium, type of plant, clubmoss '; 
Czech t/apa, Slovak, cf/aba'paw', poln. /aba= /apa; 

Lithuanian /opeta 'shoveV, Latvian /40S/5 "shovel, spade, scapula'. Old Prussian /opto 
"spade'; with other forms and ablaut 9: 

Old Bulgarian /opata' throw shovel ', russ. /Oyoa/5 "shovel', /0/oa//ra "scapula', /opat/na' 
rudder, helm '; 

Maybe alb. /opa/e "shovel' a Slavic loanword. 

References: WP. II 428, Trautmann 149 f., 160. 
Page(s): 679 

Root / lemma: /ehs. lahs- 

Meaning: weak, feeble 

Note: extension to le(i)- " slacken ' 

=== 55100,55160 (page 674 area)
livrizds., mcymr. llyveithin^^eaV! {*lemekt-)\ 

perhaps alb. leme, Geg lame, Tosc leme^ threshing floor, oil grinder ' = russ. lom\ 

Old High German Old Saxon lam{*lom-). Old Icelandic /5/77/"lame, crippled ', Old High 
German lemmen, asachs. lemmian^ lame, cripple, disable ', Old English lemian^ds., tame 
(a horse)'. Old Icelandic lemia^hW., smash to pieces; hinder', o-grade Old High German 
/i/o/77/ "faint, languid, nachgiebig, mild'. Middle High German luemen, A/c»/77e/7 "languish', 
reduced grade Old Icelandic luma^ release, let go, free, set free ', Alemannian lumme^ 
become slack ', Modern High German dial. /i//77/r7 "slack', in addition Modern High German 
Lummef, Middle High German lunzen^ drowse lightly ', East Frisian /d/77" lamed, lame, 
faint, languid', Swedish loma " be stiff or clumsy '; 

e-grade: Norwegian /aa/77"lame'; 

Latvian I'imstu, I'imt, Lithuanian //mt/"break down under a load ', Old Prussian limtwei 
"break, rupture'; Lithuanian /e/77// "decide, settle, govern, condition, reserve, ordain, 
destine, determine, fate, doom, augur', Latvian /e/77/"decide, define, ordain, determine, 
adjudicate'; Lithuanian laminti, causative /5/77oy// "train, coach, guide'; in addition probably 
also Lithuanian luomas " estate, caste '; 

Old Bulgarian loml'Jg, /om/t/"break, rupture', -s^" struggle, come to grips with, put in a 
great effort, go to a lot of trouble ', russ. /om "break', PI. /amy' rhumatic pains ' etc.; Old 
Bulgarian pre/amat/^ break, rupture' etc.; 

e-grade in Upper Serbian /em/c'break, rupture', probably also Church Slavic lemesb 
"plough' (from an es-stem, as vu)A£|j£(;), Latvian lemesis^ plowshare '; with e-grade Serbo- 
Croatian ITJemam, liJemati^bW!. 

References: WP. II 433 f., WH. I 760, Loth RC 39, 67 f., Liden Mel. Vising 378. 
Page(s): 674 

Root / lemma: lehm-2{*lehum-) 
Meaning: open jaws (?) 



Material: Gr. ka\}oq "gullet", ka\^\a N. PI. " Erdschiunci ', Aapia " cannibal, human being that 
eats human flesh ' (Latin loanword lamia^ a witch, sorceress, vampire ', /am/um'dead- 
nettle' as "figwort, scrophularia, snapdragon '; also Bulgarian lamija, /5/77a "snake' from ngr. 
Aapiia), Aaijup6(; " voracious, greedy '; 

Latin lemures^ night spirits, ghosts; souls of the dead '; 

Note: 

The inanimate suffix -ur- . Latin /e/77^/'es 'ghosts' : UAupioi , oi, lllyrians, 'lAAupia , n, lllyria, 
also 'lAAupi^ , n. Adj. 'lAAupiKO? , n, 6v, lllyrian: -kp), the region or province of lllyria, UAupi^U) 
, speak the lllyrian language, 'IAAupla:--hence Adv. 'lAAupiaii. 

cymr. //e/" voice', mcymr. //e/fe//7"cry', bret. /e/7K "clamor, lament'; 

Lithuanian lemotT pant for, long for, desire ', Latvian /a/77a/ "inveigh, scold, chide', 
lamatas " mousetrap '. 

References: WP. II 434, WH. I 755, 781 f., Trautmann 162. 
Page(s): 675 

Root / lemma: lehrvS^-1 {* lehund^ > *lehunA^) 

Meaning: liquid, spring
```


## [2026-09-06T23:10:26.040Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '55360,55450p' POK_full.txt"
}
```


### [2026-09-06T23:10:26.092Z] TOOL RESULT

```
iinniru. 'snake', (under the influence of common Celtic -ns-, -nt- > -nn-), poet. ' tree, 
celebration ', iinn-ormr' dragon' = Old High German iindwurm' lindworm, wingless dragon, 
dragon '. 

References: WP. II 437 f., WH. I 784 f. 
Page(s): 677 

Root / lemma: lep-1 {* lehup-) 

Meaning: expr. root, onomatopoeic words 

Material: Old Indie iapati^ chats, whispers, wails, talks', rapatids., pam. iowam, iewam^ 

speak, say', np. iaba, /an/a 'flattery, insincere compliments'; 

Maybe truncated alb. //S/O'chat, talk, speak'. 



It seems that from Root / lemma: plab-\ (to babble, etc..) derived Root/ lemma: lep-1\ 

"chat, talk, speak'. 

presumably as *lepagi-^ sayerof a magic spell ', Old Irish ^a/^ (disyllabic). Gen. lego 
{*IT-ago) 'physician, medicine man' (keinesfalls to Gothic lekeis); 

russ. lepetatb^ stammer, babble, chatter, babble ', Old Bulgarian lopotiv-b^ stammering, 
stuttering ', russ. lopotatb " babble, rant, roister, gossip ', with somewhat other meaning 
Serbo-Croatian /epe/a// "flutter'. 

Maybe alb. llomotiC babble ' a Slavic loanword. 

Perhaps based on the onomatopoeic words, but with a-vocalism, gr. Aani^w " swagger, 
rodomontade ', AaTTiaTri(; " swaggerer, bragger ' and AaTAaip "whirlwind' (as " howling '). 

References: WP. II 429. 
Page(s): 677-678 

Root / lemma: lep-2{*lehup-) 

Meaning: to peel, flay 

Material: Gr. Asnu) " exfoliate, remove in layers, peel off in thin sections', ktuoc, n., Kotxoc, 

m. "bowl, bark, skin' (oAonru) "schale ab'), Kzmc,, Komc,i. " scale, husk, bowl, bark', Aoirag 

!lat dish or plate, in which food was served, shell-fish ', Kzi^dc, "einschalige shell, 
slapfschnecke', Asnupov n. "bowl, husk', £AAo4J epithet the Fische (actually "in Schuppen 
being'), Asirpa " leprosy ' ("*sich schuppende skin'); Kzu^bc, "enthijlst (from Kornern); fine, 
thin, dainty, weak', Asniuvoo "hulse from; make thin', Aanap6(; "fragile, flimsy, thin' 
(*A£nap6(;); lengthened grade {d)\ Acbnri "wrapping, sleeve, garment, Ledermantel' 
("*abgezogenes f ell, fur' or at m ost from "abgetrennten rag'), Aoon oq n. ds. , Aibijj xAaMUc 



alb. Ijape^ peritoneum of animal for slaughter ', lepfj^ chisel, cut ', /a/e "small axe, hack, 
mattock, hoe' ( *lapta); 

Latin lepidus^ pleasant, agreeable, charming, fine, elegant, neat ' (compare above 
KzT\i6<^), /e/Ods "fineness, pleasantness, agreeableness, bright witticism '; presumably also 
lapit^ to turn into stone, make hard like stone, to petrify, harden ' {*leP-)\ 

Old English Isefer, leberi. " bulrush, reed ', engl. PI. levers. Old High German leber^ 
bulrush'. Old English /d/m. " headband, head fascia' (= Lithuanian lopas); 



Lithuanian lopas^ patch, vamp, clout, rag', lopau, -ytr patch ', Latvian laps^ patch, 
vamp, clout ', /a/?/7' patch '; 

Lithuanian lepus^ mushy, softish, delicate, mollycoddle ', lepautrbe minxish, wanton', 
lepintr spoil, pamper', Latvian /e'yO/75 "pride'; 

sloven. /epen'\eaV, Upper Serbian changing through ablaut fopjenon. "leaf; russ. 
lepenb ( Veptnt) "shred, scrap, shred', /epest^ag; petal ' (further formations of es-stem 
*/epes-= gr. to KzTToq), /epucha' leprosy ' (as gr. Asnpa); o-grade (as gr. Awnn) russ. 
lapotb ( Vapttb) m. " Bastschuh ', lapitb " patch ', etc. 

References: WP. II 429 ff., WH. I 785 f., Trautmann 149 f. 
Page(s): 678 

Root / lemma: lehp-3{*lehup^ 

Meaning: stone, rock 

Material: Gr. Ktuac, n. (only N. Akk. Sg.) " bare rock, stone', Kzuaxoc, " rocky'; Latin lapis, - 

/d/s'stone'; Umbrian vaperef\b\. Sg., vapersus No\. PI. "seat' (of stone?); Latin a\s 

understood as a reduplication-vowel a
```


## [2026-09-06T23:10:47.275Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK lemma les\"; grep -n \"^Root / lemma: l[eē]s\" POK_full.txt | head\necho \"=== POK gilari\"; grep -n -i \"gilari\\|gi-lari\\|g\\bilari\" POK_full.txt | head\necho \"=== IEC lakt/lak\"; grep -n \"^lak\\|^lakt\\|^laktak\" IEC.txt | head -30"
}
```


### [2026-09-06T23:10:47.348Z] TOOL RESULT

```
=== POK lemma les
=== POK gilari
=== IEC lakt/lak
9437:lak- (1) ‘têar, rag’. Cf. lakt- (1) Gk. lakís, f. ‘rag, rip, têar’; Lat. cf. lacer, adj. ‘tearing, torn, ragged’; cf. lacinia (2) ‘rag’; Li. laka f. (?) “hole, opening’; cf. lakatas ‘rag’; lakišiai, pl. (a pricky planť; Latv. cf. lakats *kerchief, shawl
9438:lak- (2) ‘kick’. Cf. lakt- (2) Gk. cf. láx (^with the heel". Ambig. cf. lag-); laktízo ‘kick’; Per. cf. lakd, s. ‘kick’; Lat. cf. lacertus “lizard?
9439:lak- (3) “lap up, gulp, gobble’. WP II, 380 Arm. lakem, id.; lak ‘porridge, pap’; W (long- gde) llawg, f. ‘gulp’; OCS loco, lokati ‘lap’; R inf. lokàt, id.; Cz. lokat, id.; lok, m. ‘gulp’; Li. laku, làkti “lap up’; Latv. loku, lakt, id. (pres. tense fr. *lank-); laka ‘swill, mash’. (The composition of Gk. ko-lax, gs -lakos ‘flatterer’ is uncertain)
9440:lak- (4) ‘shout, bawl, abuse’ Gk. aor. élakon, fut. lakēsomai ‘bark, shout, din’; OHG, OS lahan “abuse, scold’; OE lean, p.t. loh, log ‘blame’; cf. OE leahtor, m. ‘vice, evil’; Du. lachter, id. (beside OHG lastar, n. cf. also prob. Gk. lásthé ‘mockery, insult. Cf. also ON lostr “evil, wrong, harm")
9441:lak- (or laK-? Cf. lako. Gk. ambig.) Gk. lēkéō ^womanize'; lëkó, gs lekoüs *phal- lus’; Skt. cf. raka ‘goddess of fertility’. (Doric: -à-)
9442:laks- (?) jump; lumping horse’ It. lacca “leg, haunch’; cf. Lat. lacertus ‘fore- arm; leg-muscle; lizard, newt? (?); Sw. lägg, m. pl. -ar ‘calf, thigh-bone'; Ukr. cf. loSak, m. ‘colt, foal; loša ‘filly’; Latv. cf. lakstu, -it Sump’.
9444:laksos, us ‘loose, slack, limp, flabby’. WP IL, 712 Lat. laxus “loose; wide; open’; W Hac limp! m.
9447:lakstis, à (lakt-) ‘stick, stem, branch, bar. Cf. variant slaKtis Prakritic, Pali latthi ‘stick’ (cf. Skt. lakutah *cudgel); Arm. laxt, Let ‘stick; cudgel’; Gk. laktis, gs -os, f. ‘pestle’; Alb. las&, Ilasë ^wash- ing-stick'; Sw. läckt, pl. -er, m. ‘stick, slat, lath’; Blg. lost, m. Char, bolt. LW in Mod. Gk. lostós, id.); Li. lakstà, laktà ‘perch’; Latvian laksts, m. ‘shoot, sucker’ beside lakta “perch?
9448:lakt-, lakot- “rag, scrap, tatter'. Cf. lak- (1) Skt. (dim. type) laktakah ‘rag’; Per. laxt, laxd ‘scrap’; Arm. lať ‘garment, cloth, rag! beside lati ‘scrap’; Li. lákatas ‘rag’: Latv. lakats "ker. chief; cf. also Li. lákStas ‘sheet of paper, quire’
9449:lakt- (2), see lak- (2) ‘kick and cf. slak-
9450:lakús, lakuos ‘lake, pool, puddle, pond’. WP II, 380 Gk. lákkos, m. ‘pit, puddle, tank’; Lat. lacus, gs. -üs, id.; Olr. lac, Ir. lag, m. *water-hole, pooľ beside (augmentative) lagán ‘puddle’; Br. Cor. cf. lagen, pl. lagennu, lagennow, f. ‘marsh, pond’; OE lagu, m. n. (lake, flood’; pl. ‘surface of the sea’); OS cf. lagu-stróm ‘waters’; ON lọgr, gs. lagar, ds legi, m. ‘sea, water; OCS loky, gs loküve, m. ‘puddle’; lokva, f. ‘rain’; Blg. lókva, Srb. lókva ‘puddle’
9452:lakstis, à (lakt-) — làmos, a (ulàm- ?)
9460:lako, ið (variant: las-) jump, dance’. Cf. laKosos, laKüs, (lakitio) Skt. cf. (variant) lasāmi (2) ‘dance’; lásayami, id. (and “cause to dance; ply an art'. The se- cond form given also as lasSayami); Oss. lásín (drag, lead; take; weigh". Semantics obscure); Gk. lekáo (‘dance to music’; vulg. ‘coire’); Alb. los, v. (play, fr. lakið); Pol. tasic ‘swirl, twirl; R dial lásit', id.; Li. lóSiu, ti ‘play’; cf. at-si-losti “rear, jump up”. Variants include Romani loSanav man ‘rejoice’ (with -š- for IE *-K-); Latv. lakstit, inf. “jump”; cf. perh. Lat. lacerta ‘lizard’? beside lacri-müusa ‘green li- zard’; Gk. lakáo Churst Cf. G springen in this sense) beside Hes. *lakertizo (misspelt lik- jump?)
9462:laküs, (aka, laKitio) ‘bounding animal, weasel’. Cf. laKo, laKosos Per. rāsū ‘weasel’; Srb. lasa, id.; OCS. Cz. lasica, lasice, id. (an echo of this root may be present in Li. lašvaras "rout?
```


## [2026-09-06T23:10:48.726Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD lacer/lek\"; grep -n -i \"lacerate\\|^lek-\\|lakis\" AHD_watkins1985.txt | head -20\necho \"=== AHD laparos\"; grep -n -i \"laparo\\|^lep-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T23:10:48.788Z] TOOL RESULT

```
=== AHD lacer/lek
679:lek-. To leap, fly. Possibly suffixed o-grade form */ok-ost- in Latin locusta, locusta, a marine shellfish, lobster: LOBSTER, Locust. [Pok. 2. lek- 673.]
680:lék-. To tear. Zero-grade form *bk- becoming Jak-. 1. Latin dacinia, flap of a garment: LACINIATE. 2. Suf- fixed form *lak-ero- in Latin lacer, torn: LACERATE. [Pok. 2. lék- 674.]
1726:LAAGER legh- LABEL leb-! LABELLUM leb-2 LABIAL leb-2 LABILE leb-1 LABIUM leb-2 LABOR leb-1 LABRET leb-2 LABRUM leb-2 Lac! reg-3 LACCOLITH laku- LACERATE |@k- LACHRYMAL dakru- LACINIATE l@k- LACK leg-2 LACROSSE ger-2 LACTATE melg- LACTEAL melg- LACTESCENT melg- LACTO- melg- LADDER Klei- LADE kla-
=== AHD laparos
687:lep-'. To peel. 1. Greek lepein, to peel (> lemma, husk): LEMMA?2, LEPTO-, LEPTON!; SARCOLEMMA. 2. Suffixed form *lep-i- in Greek lepis, lepos, a scale: LEPER, LEPI- DO-, LEPIDOTE. 3. Suffixed variant form */ap-aro- in Greek /aparos, soft: LAPAROTOMY. 4. O-grade form “Jop- in Greek elops, ellops, a fish (< *en-lopos, having scales; en-, in; see en): ELAPID. [Pok. 2. lep- 678.]
688:lep-2. To be flat; palm, sole, shoulder blade. Lengthened o-grade form */ép- in Germanic */6f6 in: a. Germanic *gal6fo (*ga-, collective prefix; see kom), “covering for the hand,” in Old English gl6f, glove: GLOVE; b. Middle Dutch “doef, windward side of a ship, akin to the prob- able Germanic source of Old French lof, spar: LUFF. [Pok. 2. lép- 679.]
1730:LAPS |ab- LAPAROTOMY lep-1 LAPSE leb-1 LAPWING klou- LARCENY [é-1 LARK? leig-3 LASCIVIOUS las- LASSITUDE [é-2 LAST! |@-2
```


## [2026-09-06T23:11:02.789Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nimport re\nlines=t.split('\\n')\n# map line no -> leaf\ndef leaf_of_line(ln):\n    return t.count('\\f','',0) # placeholder\n# build offsets\npos=0\nleafstarts=[]\nfor i,ch in enumerate(t):\n    pass\nEOF\nawk 'BEGIN{RS=\"\\f\"} {n=NR; while((getline line)>0){}}' /dev/null 2>/dev/null\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nleaf=0\nfor i,l in enumerate(lines,1):\n    if i in (9437,9438,9448,9462):\n        print('line',i,'leaf(0-based)',leaf, '-> approx printed pp', (leaf-15)*2, (leaf-15)*2+1)\n    leaf += l.count('\\f')\nEOF"
}
```


### [2026-09-06T23:11:05.542Z] TOOL RESULT

```
line 9437 leaf(0-based) 372 -> approx printed pp 714 715
line 9438 leaf(0-based) 372 -> approx printed pp 714 715
line 9448 leaf(0-based) 372 -> approx printed pp 714 715
line 9462 leaf(0-based) 373 -> approx printed pp 716 717
```


## [2026-09-06T23:11:12.324Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==373' IEC.txt | head -5\necho \"=== leaf 346\"\nawk 'BEGIN{RS=\"\\f\"} NR==346' IEC.txt | head -5\necho \"=== leaf 347\"\nawk 'BEGIN{RS=\"\\f\"} NR==347' IEC.txt | head -5"
}
```


### [2026-09-06T23:11:14.242Z] TOOL RESULT

```
o, ati, id. and com. Sl.; Li. loju, loti, id. Nominal forms: R laj, Blg. laj ‘barking, scolding’; Ukr. taja, id.; Cz. láje, f. ‘mob, pack’; Li. lojà “abuse”
láiskð (lasK-) (variant of laio, q.v.) Hitt. sar-lesk- ‘cry up, praise’; Alb. leh, lef ‘bark’; Gk. lásko, v. ‘howl, bay’
lak- (1) ‘têar, rag’. Cf. lakt- (1) Gk. lakís, f. ‘rag, rip, têar’; Lat. cf. lacer, adj. ‘tearing, torn, ragged’; cf. lacinia (2) ‘rag’; Li. laka f. (?) “hole, opening’; cf. lakatas ‘rag’; lakišiai, pl. (a pricky planť; Latv. cf. lakats *kerchief, shawl
lak- (2) ‘kick’. Cf. lakt- (2) Gk. cf. láx (^with the heel". Ambig. cf. lag-); laktízo ‘kick’; Per. cf. lakd, s. ‘kick’; Lat. cf. lacertus “lizard?
lak- (3) “lap up, gulp, gobble’. WP II, 380 Arm. lakem, id.; lak ‘porridge, pap’; W (long- gde) llawg, f. ‘gulp’; OCS loco, lokati ‘lap’; R inf. lokàt, id.; Cz. lokat, id.; lok, m. ‘gulp’; Li. laku, làkti “lap up’; Latv. loku, lakt, id. (pres. tense fr. *lank-); laka ‘swill, mash’. (The composition of Gk. ko-lax, gs -lakos ‘flatterer’ is uncertain)
=== leaf 346
�speak, order’; Ober, cf. 0àtiy, 3s ‘says’; a-0aham ‘I said’; Arm. asem, osem (‘say, speak, tel. Phonology obscure); Tokh. A känts- ‘vow, admit’; Alb. thom, them, 3s. thotë ‘say’; Lat. censeo, Gre ‘consider, think’; OFris. (?) henzia “approve, ratify’; OCS (defec- tive) sétü “he says?
Kensos, à, us 'utterance, opinion, state- ment. Cf. Kens- (and Kés-). WP I, 403 Skt. $ámsab ‘pronouncement, cal? beside $asah “order”; Per. cf. fa-sana ‘fable’; Lat. cén- sus, gs -us 'polltax, census’; LW in Gk. kén- sos, id.; Osc. cf. censaum, inf. ‘to vote, ad-
609 judge’; Alb. cf. e thânë, f, (“saying”, fr. a type *Kons-)
Kent- ‘prick, point, spike’. WP I, 402. Cf. Kentrom Oss. síndz, Dig. sindzä ‘thorn, splinter beside síngin, Dig. singin, adj. ‘prickly’; Gk. cf. ken- táð, kentéð, v. ‘prick’; Alb. thind ‘beak’; Br. cf. kentel, pl. -téliu, f. ‘point, time, hour, les- son’; MHG cf. hint-ber ‘raspberry’; G Him- beer, id.; OE hind-berge, EME hind-berry, id. (Isophones: Gaul. cintu- “first; OW cynt, W cyn ‘before’; Ir. céad- cpds. “first-?; céadamh “of the first of May’: W cyntaf ‘first’; Go. hindum-, beside hindana, OHG hintana ‘be- hind’; OE hindema ‘hindmost’, doubtfully also to Lat. re-cēns, -centis ‘recent’. See WH: LEW)
Kentrom, à (Kütr-) ‘point, spike, spur’. Cf. Kent-. WP I, 402 Arm. santr, gs santer (‘comb’, fr. Kütrə, but gs vocalism obscure); Gk. kéntron ‘spur, prickle, goad, sting’; LW in LLat. centria ‘sting’; Alb. thundër, f. (hoof, heel, talon, thorny plant’, fr. *Kntrá); Gaul. centron (part of a mountain- name); Br. kentr, pl. -u, f. ‘spur’; Cor. kentr, pl. ow, f. ‘spike’; Olr. centir, cintir ‘spur’; Du. (?) hinder, m. ‘annoyance’; Fris. ‘obstacle, catch’; Sw. hinder, n. id. (Gmc. cognates doubtful)
=== leaf 347
atera-, Gk. krétér, krátér (mixing bowl". LW in Lat. cràter, crà- tera); OHG hruorjan, OS hrorjan, OE hreran ‘stir, shake’; OE, OS hror “active, lively’, cf. E dial. a roosing fire (paroxytonic prototype)
Kerd- (Kerdis, à, io) “heart, core, centre’. Cf. Krd-. WP I, 424 Vedic $ardih, f. (mng. uncertain, cf. AV 18, 3, 16); Go. hairto, OHG hérza, OS hérta, ON hjarta, pl. hjortu, n. ‘heart’; Cz. střed ‘middle’; OCS sréda, id.; Li. šerdis, -iés, f. (core, pith; bell-clapper'. Gp: Serdü. Also: "heart of a tree”); Latv. serde ‘pith, marrow?
Kerdhos, à “herd, crowd, drove'. Cf. Ker- ‘head’. WP I, 424 Skt. Sardhah “host, army? beside $ardhas, n. id.; Av. saroóo (2) ‘kind, sort’; Go. haírda, f. ‘herd’, wm. ‘herdsman’; OE heord, f., hierde, wm. as Go.; OHG hërta, f., hirti, m. as Go.; ON hjoró, f. ‘herd’; hirðir, gs hiróis, m. ‘herdsman’, cf. hirð, f. ‘bodyguard’. (Gk. kór- thus, f. ‘pile’, and W cordd, m. pl. -ion ‘circle; tribe’ are no more than potential o-gde iso- phones, despite FK: EWDS 17: Herde. OCS éréda (2) “herd” and Li. kerdZius, m. 'shep- herd? are Germanic LWs because of the initial.
611
SF:GEW regards Gmc. Sl. ànd Li. forms as cognate, and omits Indo-Iranian)
```


## [2026-09-06T23:11:23.559Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 382 383 384; do echo \"=== awk NR=$n (0-based leaf $((n-1)), pp $(( (n-1-346)*2+609 ))-$(( (n-1-346)*2+610 )))\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' IEC.txt | grep -n \"^l\" | head -40; done"
}
```


### [2026-09-06T23:11:25.421Z] TOOL RESULT

```
=== awk NR=382 (0-based leaf 381, pp 679-680)
3:leið (li-) (1) ‘pour’. See leiió and (variant) hio (1)
5:lëið (3) ‘release’. Cf. leuio (2) and linuo Skt. riye, mp. inf: retum ‘release, sever’ beside rinàmi, riņími, id.: MHG lån, sv. 7 ‘release’; Hitt. cf. lai (for *I), 3sg ‘looses, unharnesses’
6:leio (4) “stir, move” Oss. ráin, Dig. irajun ('seethe, surge; rejoice’ in phr: mà zàárdá rat ‘my heart rejoices’); Alb. luej, luaj, tr. ‘move’. Isophonic (but ambig.) Du. laaien, laien, v. ‘blaze, flame’
7:leið (lin-) (5) “be, lie, remain’. See next, and cf. liio (4), linuó Skt. Hyámi, Dee ‘remain; lie, cower’; Arm. cf. linim, inf. linel, v. ‘be, become’; MHG lan, sv. 7 (2) lie’. Cf. Go. af-linnan, OHG bi-linnan, OE linnan, sv 3 'depart; give way; desist
8:léios, a “lying, repose, prostration, flatness' Skt. (ambig.) láyah ‘repose; death’; MHG là, sf. ‘marsh, ley’; Fris. leije ‘drainage ditch’; E ley; cf. MHG lan, sv. 7 (2) lie’; ON lá, f. pl. lár ‘shore-line, shoal-line’; Latv. lej$ Jow- lying’; leja “valley”; Srb. 18ja (‘garden-bed’. But for OCS lëxa, id. see *lēs-)
9:lek- (1) (?) Cf. laK- Ir. cf. leicte, adj. “smart, active’; Li. lekiü,
10:leiu- — lembos
18:lékti ‘fly’; lékes, fpl. ‘husks of oats’; Latv. lecu, lēkt Jump”, cf. lekts ‘rise, sunrise’; lēkme, f. ‘attack’; OCS cf. Ičkù (a game: jumping?)
19:lék- (2) (?) Lat. cf. il-lecebrae, per" ‘traps’, but cf. lacio, ære “ensnare), cf. also Lat. licinus ‘with up- turned horns’; Li. cf. lekétas *cotton-winder. With long vowel cf. Br. likaui, inf. “cheat, wangle, wheedle’; W ilith, pl. -iau, f. (lure, bait”, fr. *lekti-)
20:léks- (lek-) “flat surface, slab, plate’. Cf. plek- (pleks-). Celt. ambig. Gk. lékos, gs -eos, n. ‘dish, pan’; cf. lék-ithos (prob. ‘scrambled eggs? lit. quick-dish"); Ir. (ambig.) leac “slab, slate’; W (ambig.) Iech, pl. au. -i, f. id.; Cor. legh, pl. -ow, f. id.; cf. leghen, f. ‘shale, slate’; R cf. lescadi, f. ‘flagstone’; Li. cf. lekSnas, lekstas, adj. “flat”; lek3te, f. ‘platter, pan”; Per. cf. lakan, Kurd. legen *basin'
21:lel- (1) ‘sway, hurtle' Hitt. cf. lelas, lilas (a festival); lili-wahhi, leli- wahhi, v. ‘hasten’; OCz. leleti sé ‘rock, sway’; lelek ‘nightjar’; Li. lélis, m. id. Cf. Skt. (short vowel) lalàmi “dally, play’. See next
22:lel- (2) ‘pet, darling, fool, doll’. Cf. WP II 377 & 395 Skt. cf. lalakah, lalikah “court fool; pet, darl- ing”; lalayami ‘fondle’; W Hill, pl. od f. ‘pet goat; OCS, Blg. lélja ‘maternal aunt’; SI. LW in Alb. lalë, def. -a “elder brother’; lale, f. ‘larva’; Pol. lala ‘doll’; cf. Ukr. lelijaty, v. ‘fondle’; Li. lele, Latv. lele, lelle and lellis ‘doll’
23:lel- (3) ‘marked, stained, discoloured'. Cf. WP II, 422 Skt. cf. lalamah, adj. ‘marked with paint’; Arm. ley, Let ‘yellowish’ beside leyi, gs -vo, abls. -eav ‘gall, bile’ (here?); OE læl, f., læla, m. ‘weal, bruise’; læl-ian, v. ‘turn livid’;
24:léleió, s
=== awk NR=383 (0-based leaf 382, pp 681-682)
2:lem-, see lemo, ið
3:lembos ‘weak, limp’. Cf. (lamb- and) lomb- beside slamb- Skt. lamb-, cpds. ‘hanging’; MIr. & Ir. leamh ‘impotent; insipid; silly; OHG cf. limphen, limphin (sic); MHG limpfen, v. ‘limp’; E limp, adj. and vb. (but cf. *kImb- for possible ini- tial *k-); Li. lembüs, adj. “fluid; unbleached’.
6:lembhos, à 'strip, stripe, edge' Skt. rambhaà *loin-string, dhoti'; Lat. limbus, gs -i ‘seam, edging’; OHG cf. limbel, limmel, n. “strip, strap’. (Cz. lem “border, hem’ is ap- parently of Lat. origin, as also EME limb 'rim")
7:lemo, io, lemo- (lém-, lom-, lom-) “break, snap, cut, cut off. WP II, 434 Skt. (alleged) ramnami 'strike'; Av. ram-, id.; Li. lemiü, lémti ‘decide’; lémtas, pp. as adj. ‘downright, forthright'; Latv. lemju, lemt “determine; Ir. (*-&-) líomnaim ‘impute’; Hitt. (*-o- or *-o-) lammar, gs lamnas ‘period, time- sector”; (z-gde in) Li. limstu, limti, intr. “break, snap’; cf. also OCS lemest, m. ‘plough’; Latv. lemesis 'plowshare'.. (Isophonic;: ON lámr, m. “hand, paw’ best as an isophone w. *-&-; Li. lemiu, lemti (2) ‘announce’; leméjas ‘herald’; Srb. lemati, inf. *thrash")
8:lendhà ‘wrapping; wrap’ Ir. leann, f. ‘mantle’; Sw. linda, f. (2) ‘swaddle- band, bandage’
9:lendhô ‘go, creep’. Cf. lent- Tokh. AB (ambig.) lánt-, lät-; B lant-, lat- *de- part; OHG (ambig.) cf. lint, m. (/snake': G Lind-wurm); ON linnr, m. as OHG; Li. lendü, listi, pf. lindau ‘creep; penetrate; sprout’; Latv. liedu, list ‘creep’
10:lendhos, à, om ‘fallow; fallow land’. (Variant: Indh-). Celtic ambig. Sw. linda (1) “field, pasture'; Pol. lad, m. “mainland, stretch of territory”; Cz. lado, lada, n. sg. & pl. “fallow land'; R (alleged in NW dialects) 1jàda, ljadà beside ljadina, id.; R-gde or z-gde in Gk. lantháno ((1) Turk”, lit. "Det: Br. lann- (in place-names: land"); lannou and Janneier, pl. (“rough land”, whence Fr. landes); lannek, dim. type “area sown with rush or coarse grass for winter fodder; ley'; O-gde in OHG lant, Go. land, n. (land? and com. Gmc.). (NB. Ir. lann “floor; church’, and W llan, m. ‘church; town? are ambig. cf. *pladno-.
11:lembhos, à — lēnis, os
22:lengho (1) “stretch, reach, advance, lunge, dart, project’. Cf. longhos and ingh-. WP I, 436 Skt. langhami “leap upon; waste’; langhe, mp. ‘cross’; ranghe "run cf. also ranghas, n. ‘speed’; Av. rag- (zero-gde?) ‘jump; lift; Gk. cf. (*-ñ-) lagkháno, pf. (*-o-) iélogkba; aor. (-n-) élakhon (*'cast', hence “acquire by luck"), cf. lógkhe (lit. ‘casting’, hence ot); MIr. & Ir (ambig. lingim (eap, dash’, but cf. *plenK-); OHG gi-lingan “proceed; succeed’; MHG cf. linge, f. ‘luck’; adj. ‘rapid’; R ljagát, ljagnùť ‘kick’; cf. dial. ljàga ‘thigb’; Z-gde in Latv. linga ‘sling’; o-gde in OHG lang (Clong', and com. Gmc.) and in Lat. longus
23:lenghó (2) “reject, rebut, rebuff Gk. cf. elégkho “rebut, rebuff; Latv. liedzu, liegt “forbid, deny, refuse'; cf. o-gde langaju, at “call names, abuse”
24:lengho (3) “trail, lie limp, pine’ (?) (Variant: leng-, long-. Si. Li. ambig.) (Per. langam, langidan, inf. “limp? is from a variant of type *leng- in view of Skt. langami, id.; langah lame); OCS 1ego, lẹšti “lie down’; Pol. cf. leg, m. ‘brood’; legnac, intr. ‘hatch out’; Li. cf. lengstu, lengti, v. ‘languish’. (For Lat. langueo, see slangueio. WH & EM un- tenable)
25:lenguhos (variant of type elnguhos, elnghus, q.v.) lightweight Av. cf. renj-, v. ‘be lightweight; Gk. (from Phryg. or Thrac?) lémbos, m. ('skiff. The ex- pected G
=== awk NR=384 (0-based leaf 383, pp 683-684)
2:lenis, os *easy, soft, pliant, docile; thigh, waist, loin’. Cf. WP II, 395 Av. rānō, m. ‘thigh’; Per. ran, id.; Gk. lenís, f. Ctrollop', whence Lat. leno, -onis, m. ‘pimp’, if not fr. *slen-, q. v.); Lat. lēnis “gentle, soft, easygoing’; LLat. lēne, n. ‘ointment, salve’; (Ir. cf. léan, m. ‘loin’ & cf. the semantics of G Weiche ‘flank’. Ir. fr. *lein-); OE læne ‘frail, poor, perishable’; OCS lënü “lazy”; lëni, f. ‘laziness’; Cz. cf. je mi lé ‘I am disinclined’; Li. lēnas ‘tame, quiet, slow; Latv. lēns, id. (For Per. lin, Ir. léan, MHG Iin & Li. leinas,
5:lënið, lið ‘soften, ease, weaken; be soft, be easy”, etc. See lenis Lat. lénio, īre ease, allay’; OCS lénjo se, -iti se “lounge, laze’; Cz. leniti, inf. id. (Icel. iso- phone: læna, f. ‘brook’; v. *flood")
6:lenkKtis (lenKis), io (?) ‘spot, freckle; lenti. Cf. WP II, 437 Lat. lēns, gs lentis, f. lentil’; OCS lesta, id.; Srb. leća, leće, f. & n. id. (and ‘freckle’); Latv. cf. lēca (“lentil”, for *lieca in a dialectal form? Cf. also lecenes, pl. *measles"). Simplex in Li. lésis & lefisis, m. "lentil'
7:lenquó, ið “bend, turn, twist'. Cf. lonqu-, Inqu-. WP II, 435 Skt. cf. rankutih, f. ‘vetch’; OCS lẹkọ, lesti “bend, turn, twist", beside leto, lecati, denom. *ensnare'; Li. lenkiü, leükti ‘bend’, cf. also lenkmuó, eps m. “bend of elbow or knee’; lenke, f. “valley”; Latv. liecu, liekt “bend” be- side lencu, lenkt ‘go round; haunt’
8:lentā ‘timber, wood (Variant of elntā, q. v.). WP II, 437 Alb. låndë, T lëndë, f. “timber; material; ON lindi, f. limetree; shield or spear of lime (fr *lentis or *lentio); Srb. letva ‘lath’; Li. lentà ‘board’; Latv. (?) lieta ( (thing, matter’. Cf. semantics of Lat. materies)
9:lentos, ios ‘easygoing, slack, slow, smooth, mild, calm. WP II, 437. See next Lt. lentus ‘slow, sluggish, gentle, pliant’; Br. lent ‘timid, feeble’ beside landar ('sluggish', fr. *lentero-, see next); OHG lindi, MHG lin- de, lint “soft, mild, smooth, tender”; lint, gs lindes, m. (snake'. Cf. G Lindwurm); OE lipe, as MHG, beside lióre ((2) *'slothful, confused with type lyóre ‘evil: G Diederich ‘wanton’, see leut- (2); EME lither “slothfuP; cf. OE
12:lentris, ios, (lentoros) ‘sluggish, slow; slow boat" (?). See lentos Lat. (?) linter, gs lintris, f. ‘small boat’; Br. landar, adj. ‘sluggish’, fr. *lentoro-; OE lióre (*'sluggish': EME lither, id.)
13:lënið, iið — les- (lësla, ós, ióm)
21:lenuos, see linuos
22:lepos (1) ‘small, fine, dainty, trivial’. WP II, 430 Per. cf. laf ‘swagger beside làbah ‘flattery: desire’; Myc. cf. repoto- (lepto- ‘fine’: Gk. lep- tós, id.); Lat. cf. lepos, gs Ons, m. “wit, mirth’; cf. lepidus ‘dainty, pretty, witty, plea- sant’; Li. lepùs, id. (& ‘finicky’) beside lëpnas, id.; Latv. lepns ‘haughty’, cf. lepoties, refl. ‘swagger’. (NB. For OCS lépü ‘decent’; Cz. lepý ‘dainty’; Slovene iép “handsome; Blg. lëp, id. see loipos (1) in view of Latv. laipns ‘friendly, kind’). Cf. MIr. leos (‘radiance’, fr. *|epost-)
23:lepos (2) “leaf, petal, peel’. Cf. lop- Gk. lépos, gs -eos, n. & lepís, f. “scale, shell", cf. also Hes. lepastís, f. ‘scale; limpet': R lè- Dest, f. “strip; petal; leprós ‘scaly’; lépo, v. (peel. Adj: leptós Ou: lépra ‘leprosy’; LLat. (Ps. Apul)
```


## [2026-09-06T23:11:33.661Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==384' IEC.txt | cat -n | sed -n '1,40p'"
}
```


### [2026-09-06T23:11:35.489Z] TOOL RESULT

```
     1	k. form wd. be *lemph-); Li. lefigvas & lengvus "lightweight, easy’; Latv. liegs, id. (For MHG linge “rapid”, see lengho (1))
     2	lenis, os *easy, soft, pliant, docile; thigh, waist, loin’. Cf. WP II, 395 Av. rānō, m. ‘thigh’; Per. ran, id.; Gk. lenís, f. Ctrollop', whence Lat. leno, -onis, m. ‘pimp’, if not fr. *slen-, q. v.); Lat. lēnis “gentle, soft, easygoing’; LLat. lēne, n. ‘ointment, salve’; (Ir. cf. léan, m. ‘loin’ & cf. the semantics of G Weiche ‘flank’. Ir. fr. *lein-); OE læne ‘frail, poor, perishable’; OCS lënü “lazy”; lëni, f. ‘laziness’; Cz. cf. je mi lé ‘I am disinclined’; Li. lēnas ‘tame, quiet, slow; Latv. lēns, id. (For Per. lin, Ir. léan, MHG Iin & Li. leinas,
     3	679
     4	see leinos). See next.
     5	lënið, lið ‘soften, ease, weaken; be soft, be easy”, etc. See lenis Lat. lénio, īre ease, allay’; OCS lénjo se, -iti se “lounge, laze’; Cz. leniti, inf. id. (Icel. iso- phone: læna, f. ‘brook’; v. *flood")
     6	lenkKtis (lenKis), io (?) ‘spot, freckle; lenti. Cf. WP II, 437 Lat. lēns, gs lentis, f. lentil’; OCS lesta, id.; Srb. leća, leće, f. & n. id. (and ‘freckle’); Latv. cf. lēca (“lentil”, for *lieca in a dialectal form? Cf. also lecenes, pl. *measles"). Simplex in Li. lésis & lefisis, m. "lentil'
     7	lenquó, ið “bend, turn, twist'. Cf. lonqu-, Inqu-. WP II, 435 Skt. cf. rankutih, f. ‘vetch’; OCS lẹkọ, lesti “bend, turn, twist", beside leto, lecati, denom. *ensnare'; Li. lenkiü, leükti ‘bend’, cf. also lenkmuó, eps m. “bend of elbow or knee’; lenke, f. “valley”; Latv. liecu, liekt “bend” be- side lencu, lenkt ‘go round; haunt’
     8	lentā ‘timber, wood (Variant of elntā, q. v.). WP II, 437 Alb. låndë, T lëndë, f. “timber; material; ON lindi, f. limetree; shield or spear of lime (fr *lentis or *lentio); Srb. letva ‘lath’; Li. lentà ‘board’; Latv. (?) lieta ( (thing, matter’. Cf. semantics of Lat. materies)
     9	lentos, ios ‘easygoing, slack, slow, smooth, mild, calm. WP II, 437. See next Lt. lentus ‘slow, sluggish, gentle, pliant’; Br. lent ‘timid, feeble’ beside landar ('sluggish', fr. *lentero-, see next); OHG lindi, MHG lin- de, lint “soft, mild, smooth, tender”; lint, gs lindes, m. (snake'. Cf. G Lindwurm); OE lipe, as MHG, beside lióre ((2) *'slothful, confused with type lyóre ‘evil: G Diederich ‘wanton’, see leut- (2); EME lither “slothfuP; cf. OE
    10	hóercian ‘smooth, flatter’; ON linnr, m. .
    11	‘snake’; Li. (Zemaité) lefitas (*calm, quiet. Lalis). Denom. in Lat. lentere ‘dawdle’ and Br. cf. landréi, landréa, id. (fr. *lentor-). Cf. Vedic rántyah “at ease’
    12	lentris, ios, (lentoros) ‘sluggish, slow; slow boat" (?). See lentos Lat. (?) linter, gs lintris, f. ‘small boat’; Br. landar, adj. ‘sluggish’, fr. *lentoro-; OE lióre (*'sluggish': EME lither, id.)
    13	lënið, iið — les- (lësla, ós, ióm)
    14	15
    15	20
    16	25
    17	30
    18	40
    19	45
    20	680
    21	lenuos, see linuos
    22	lepos (1) ‘small, fine, dainty, trivial’. WP II, 430 Per. cf. laf ‘swagger beside làbah ‘flattery: desire’; Myc. cf. repoto- (lepto- ‘fine’: Gk. lep- tós, id.); Lat. cf. lepos, gs Ons, m. “wit, mirth’; cf. lepidus ‘dainty, pretty, witty, plea- sant’; Li. lepùs, id. (& ‘finicky’) beside lëpnas, id.; Latv. lepns ‘haughty’, cf. lepoties, refl. ‘swagger’. (NB. For OCS lépü ‘decent’; Cz. lepý ‘dainty’; Slovene iép “handsome; Blg. lëp, id. see loipos (1) in view of Latv. laipns ‘friendly, kind’). Cf. MIr. leos (‘radiance’, fr. *|epost-)
    23	lepos (2) “leaf, petal, peel’. Cf. lop- Gk. lépos, gs -eos, n. & lepís, f. “scale, shell", cf. also Hes. lepastís, f. ‘scale; limpet': R lè- Dest, f. “strip; petal; leprós ‘scaly’; lépo, v. (peel. Adj: leptós Ou: lépra ‘leprosy’; LLat. (Ps. Apul)
```


## [2026-09-06T23:11:45.342Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==385' IEC.txt | cat -n | sed -n '1,30p'"
}
```


### [2026-09-06T23:11:48.851Z] TOOL RESULT

```
     1	cf. penplepios 'spurge-laurel, lit. “five leaves', from its terminal cluster; Ir. leo, m. ‘film, esp. of oil on water’; Slovene f. lepen, m. “leaf”; R cf lépestt, f. “strip; petal; Srb. cf. lepetati, inf. ‘flutter’
     2	lép- (?) MHG lāb if distinct from là, gs lawes, see leuis (1) “mild, of weather’; Li. lépis, m. *dawdler'; lepti, inf.; lepstà 1sg. ‘flag, be limp’; cf. Latv. lépot, inf. ‘dawdle’ (with expressive initial ]-)
     3	lerdos (?) ‘clumsy, awkward’. Cf. lurd-. (Variant: lordos ?) Sp. lerdo ‘ponderous, clumsy, heavy’; MHG lërz “awkward, left-handed' beside lérzen, v. ‘stammer’. Cf. (?) Gk. lordós “bent?
     4	lergo (?) Per. larzidan, inf. ‘tremble’; larze, s. ‘tremor’; MHG, MLG lérken, lirken ‘stammer’. (Iso- phonic Icel. lerkaóur is ‘bruised, sore. MHG lérc & lirc is "left-hand; lame). Ir. learg is “plain, track, road; slope”, and leirg, f. is “path; reason?)
     5	lés- (lesa, ós, ióm) (?) “place, space, area, room” Per. -lax, cpds. “-place'; OHG cf. gi-lari, n. ‘room, dwelling’; Icel. lár *ditty-box'; Sw. lår, m. ‘box, drawer’; LW in R lari; Latv. lēsa ‘ayot, mudfiat'. (Isophonic: ON láss ‘lock; arrow,
     6	681
     7	bolt’: Sw. lås, n. ‘lock’)
     8	leskos (ledskos ?) ‘feeble, limp’. Cf. los-quos (Iks-) Ir. leasc, adj. id.; OW & W llesg ‘feeble, slug- gish’; llesgu, tr. ‘weaken? OHG lëskan, sv A ‘die out; MHG léschen, sv 4, id. (FK: EWDS: lóschen untenable)
     9	leso, ið ‘peck, pick, gather, read WP II, 440 Skt. rasàmi, rasyāmi (taste, feel, sample’. Ambig.); Go. lisan, sv. 5 “gather”; MHG lésen, sv 5 “gather, choose, read, tell’; OE lesan ‘pick, glean’; ON lesa ‘pick; catch; read”; Li. lesu, lésti ‘peck, pick’; Latv. lešu, lest ‘reckon, count? beside (o-gde) sa-lasit, inf. ‘gather up’; sa-lasas, fpl. ‘scraps, gleanings'
    10	letos, is (let-) “free, Easy; ease’ ; Skt. ratáh *bestowed"; ratih ‘generous, favour- able’; Br. līt, lid, pl. -u, m. “fate; joy; caress’; Go. cf. un-léps, -léds “poor, disowned'; un- ledi, n. ‘poverty’; OE un-ldéd “abandoned, stray’; un-lædu (w. non-historic -u, f. *mis- ery’); OCS læti, phr: — jesti “it is allowed’; lótije, n. ‘facility’; Li. lētas ‘slow, easygoing, soft, quiet, meek’; Latv. lēts ‘cheap’; short vowel in MHG lëdig ‘free’; LW in Finnish: lieto “soft, tender, gentle". (The background of Lat. laetus ‘fortunate’ and lētum ‘death’ is uncertain, as also that of OCS lëto ‘sum- mer’. LLat. laetus ‘liege’, as also OFr. lige, id. is a Gmc. type *leþigas: G ledig). The iso- phone OE Leo n. ‘county division’; ON láð, n. ‘land’; G Lehde, f. ‘upland, high plateau? is reflected in the LLat. LW leta *court-leet". Blg. letăv ‘horizontal’ is without an etym.)
    11	letros, å ‘piece, strip, skin”; letró, io ‘strip, flay, têar’. WP II, 428 Per. latre ‘part, fragment’; Gk. cf. ko-letráo (‘trample’, if ko- is a px.); Ir. leathar, m. “skin, hide’; W lledr, m. id. (and “leather?); Br. ler, lezr, m. id.; Mir. cf. letraim, v. ‘mangle, téar'; MHG léder, n.; OE -leóer, leóer-, cpds. ‘eather’; MHG cf. l&deren, lideren, v. ‘tan’
    12	leubh, leubhi ‘rather, or’. See next Osc. loufi, loufir, cj. "or": MHG liebe, adv. ‘willingly’; E dial. lief, d: Pol. lub, cj. "or: lubo, cj. “though?
    13	leubho (lubh-) ‘desire’. WP II, 419. See next
    14	leskos (ledskos ?) — leudhis
    15	10
    16	I5
    17	20
    18	25
    19	30
    20	35
    21	40
    22	45
    23	682
    24	and cf. leubh Skt. lobháyami, tübhyàmi 'excite desire’; Hes. cf. Iuptá (^whore': Skt. lubdháb, a 'avid"); Lat. lubet, libet, 3s impers. ‘pleases’; Osc. loufir, 3s. id.; OHG liuben, impers. w. dat. id.; OE l&ofian "become dear’; OCS ljubljo, ljubiti Jove’; Cz. líbit se, w. dat. �
```


## [2026-09-06T23:12:09.959Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON files head\"; head -3 MON_part1.txt | cut -c1-200; wc -l MON_part1.txt MON_part2.txt\necho \"=== grep لخت in MON\"; grep -n \"لخت\" MON_part1.txt MON_part2.txt | head -10\necho \"=== grep لاف\"; grep -n \"لاف\\b\" MON_part2.txt | head -5\necho \"=== HRN laxt\"; grep -n -i \"laxt\\|lacht\\|lāf\\|laba\\|lābe\" HRN.txt | head -20"
}
```


### [2026-09-06T23:12:10.060Z] TOOL RESULT

```
=== MON files head
0 
2 

  99339 MON_part1.txt
  94500 MON_part2.txt
 193839 total
=== grep لخت in MON
MON_part1.txt:16844:استعمال شود). زن شلخته و بد سر و وضع 
MON_part1.txt:17886:شب)» بوست انداختن. جامه کندن» لخت 
MON_part1.txt:22215:لخت. حصه؛ حظ» نصیت. 
MON_part1.txt:22920:ببس رهنه: ۶006 (ص.) لخت» عریان. 
MON_part1.txt:24206:برخی » لختی. گروهی از مر دم. ضح.- بعض 
MON_part1.txt:26532:لخت‌های برف که از کوه به تاش آفتاب» 
MON_part1.txt:28057:پارچه» جزو» بخش» برخ» لخت» ترکیبات: 
MON_part1.txt:28091:لخت‌دوزء لاحخه‌دوز» وصله گر. تن پرست. 
MON_part1.txt:29423:روت لخت» عور: بایتی. آشکار. دوغ بتی: 
MON_part1.txt:29468:شلخته» بنتی» دنس» بلشت» قدر. قبیح» 
=== grep لاف
804:سطح بدن موجودند و بیشتر به داخل غلاف 
1185:منشاء آنان اختلاف است؛ غربال‌بند» کولی؛ 
1842:کردن, بند خالص ندادن. ظاهر کردن خلاف 
1844:اظهار خلاف نهانی. خیانت. تقلب» تثزویر. 
2174:غلاف: ۸۰ ,۵۱8۲( [ع.] () پوشش چیزی 
=== HRN laxt
5450:zu aw. rasman- 'Schlachtreihe', ai. ragmän-^ racmi'^
5467:612. rezm 'Schlacht, Kampf.
5468:aw. vergl. areza- 'Schlacht'; arm. LW. paterazm
5470:An Ableitung von aw. rasman- 'Schlachtreihe' zu
7244:834. kär[»är 'Kampf, Schlachtfeld*, vergl. karJ 'Kämpfer.
7455:n. ßusay 'todten, scli lachten (207).
10178:85. aMr 'Dolch, Schlachtmesser (des Priesters), Pferde-
```


## [2026-09-06T23:12:12.114Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB\"; grep -n -i \"laḫt\\|lacht\\|lāf\" HUB.txt | head -20\necho \"=== PHD lex\"; grep -n -i \"^lah\\|laxt\\|lab\\b\" PHD_mackenzie.txt | head -20\necho \"=== SYN rag\"; grep -n -i \"lakis\\|lacer\\b\" SYN.txt | head -10\necho \"=== KLN lacerate\"; grep -n -i \"lacerate\\|laparotomy\" KLN_1966.txt | head -10\necho \"=== SKT\"; grep -n -i \"lacerate\" SKT.txt | head -5"
}
```


### [2026-09-06T23:12:12.223Z] TOOL RESULT

```
=== HUB
1214:Schlacht' (vgl. np. razm *Kampf ') , entsprechend im
2321:612. Np. razm 'Schlacht' ist = ap. "^razma = zd. rasma
2322:'Schlachtreihe (von Wzl. raz = idg. reg^, vgl. skr.
2323:raju *Reihe'). Der Ubergang von 'Schlachtreihe' zu
2324:'Schlacht' ist, meine ich, begreiflich und iiberdies be-
2326:Schlachtreibe, Schlacht'. Fiir idg. g^m, g^hm erscheint
3686:(larmend, schreiend, tosend, Wettstreit, Schlacht' bei
4681:Zar. 66, Anm. 61 = arm. paterazm 'Krieg, Kampf, Schlacht'
7976:*Gast*, siehe oben p. 29 ; razm *Schlacht, Kampf , arm. razm
=== PHD lex
675:lahar [QDM < A qdm; )pil M )br, N bar] up; on, over.
3376:lab [lp I M lb, N -] lip.
4696:stiin(ag)                                                        lab-
4744:lAb                                79                           liftenall
4745:lAb [MLKA < A mlk); Ih 1M I)h, N -] king.
4746:  -an lAb [MLKAn MLKA IN ......] king of kings.
4751:lahr [Itr l I M Ihr, N -] land, country; city.
4756:lahryar [Itr'd)ll M Ihry)r, N ......] lord, sovereign, ruler.
7003:lip lab.
8712:panlaxtan       \\~V             parahum                 --G~tl>
9348:lab                              ~     1--2ro d
11359:lahziir
=== SYN rag
4968:4, Lith. lokys, Lett. ldcis, OPruss, clokis, all fr. *tlakis, this perh. as ‘hairy, shaggy’ : SCr. dlaka ‘hair’. Briickner, KZ 46, 207. Miuhl.-Endz. 2.434. Other- wise Meillet, Ling. hist. 284.
10391:115. erh. fr. lacer ‘torn, as S oe ne ‘rag’, Aaxifw ‘tear ‘ lochma ‘rag’. WaldeP. 2.419 £. Walde-H. tae: Frnout-M. 515 (“only pop. etym.”).
21225:care OE settan, lecgan SCr.  metnuti, postaviti, : mellre, poser, placer ME  sette, leye, pute klastt th poner, colocar NE put, place, set, lay Boh.  postaviti, poloziti, ae ee biiga Du. zelten, plaatsen, leggen klasti
21250:Fr. placer, deriv. of place ‘place’ (12.11).
21275:NE place, prob. fr. sb. place (12.11), rather than direct from Fr. placer.
27829:dptoxw, avdavw Goth. (ga)letkan Lith. (pa)tikti dptow ON lika, hugna Lett. (pa)tikt placére Dan. _behage ChSl.  ugoditt piacere Sw. behaga SCr. dopasti se plaire OE (ge)lician, (ge)cwée- Boh.  libiti se placer, agradar, man Pol. podobaé sie gustar ME plaise, like, (i)queme Russ. nravit/sja » plicea NE please Skt. pri-, tarpaya- lollanaigur, tolnur Du. behagen Av. vot (inf.) ie ee OHG  (gi)léhhen ra au, boddio MHG (be)hagen, gelichen Piyjoul NHG = gefallen Verbs fo
27831:2. Lat. placére (> It. piacere, OFr. plaisir, Fr. plaire, Sp. placer, Rum. pld- cea) : placadre ‘reconcile, soothe’, placi- dus ‘gentle, quiet, calm’, prob. as orig. ‘make smooth, flatten out’ : Grk. ride ‘flat surface’, ete. Cf. also Toch. A
27878:NE pleasure with spelling after measure, etc.), Sp. placer, Rum. pldcere, NHG gefallen, Skt. prwti-. Or other words meaning orig. satisfaction, as NHG vergniigen, Du. genoegen (: NHG genug ‘enough’, etc.), Russ. wdovol’sivie (cf. udovol'stovat’ ‘satisfy’, dovol’sivie ‘suffi- ciency, abundance, ease’ : dovol’no, ChSI. dovolino ‘enough’, this : volja ‘will’, etc.). So Goth. gabaurjopus (renders #6ovy, be- side adv. gabaurjaba = }béws, #dtcra) : OF gebyrian ‘pertain to, happen’, etc. (Feist 175; for formation, cf. F. Metzger, Lan- guage 21.971f.). NHG lust, orig. ‘strong desire’ (: Goth. lustus, OE lust, etc.) now common for the simple ‘pleas- ure’. Lat. volupids the most distinctive word for ‘pleasure’, beside neut. adj. volup ‘pleasant, agreeable’ : Lat. velle ‘wish’, Grk. é\is ‘hope’, etc.
27883:Sp. alegria, fr. alegre ‘lively, merry, joyful’ = It. allegro id., fr. Lat. alacer ‘lively’, also ‘joyful, merry’ (joined with laetus in Cic.), perh. : Goth. aljan ‘zeal’, OE ellen ‘strength, valor’, etc. Walde-P. 1.156. Walde-H. 1.25. Otherwise G Lat. amb-uldre) Ernout-M. 31.
28759:Goth. aljan (renders fos as ‘jeal- ousy’, Rom. 13.13, otherwise ‘zeal’) = ON eljan ‘energy, endurance’, OE ellen ‘strength, vigor, courage’, OHG ellen ‘zeal, strength’, etc., etym. dub., perh. : Lat. alacer ‘lively, eager, glad’. Walde- P. 1.156. Falk-Torp 188. Feist 38. Walde-H. 1.25.
=== KLN lacerate
11416:Derivative:  dik-er,  dyk-er,  n. diksha,  n.,  initiation  preceding  certain  cere¬ monies  (Hinduism).  —  OI.  diksd  (for  *didk-sa), ‘initiation’,  rel.  to  dakfah,  ‘apt,  clever’,  disti,  ‘he honors’,  fr.  I.-E.  base  *dek-,  *dok-,  ‘to  take, receive,  accept;  acceptable,  becoming,  good’, whence  also  L.  decere,  ‘to  be  seemly  or  fitting’. See  decent  and  cp.  words  there  referred  to. dilacerate,  tr.  v.,  to  tear  to  pieces.  —  L.  dilace- ratus,  pp.  of  dilacerare,  fr.  di-,  ‘asunder’,  and lacerare,  'to  tear  to  pieces,  to  rend’.  See lacerate.
20949:liovlgc,  ‘Lacedaemonian,  Spartan’,  fr.  Aazs- Saijiuv,  ‘Lacedaemon,  Sparta’.  Cp.  Laconic, lacerable,  adj.  —  Late  L.  lacerabilis,  ‘that  can  be easily  lacerated’,  fr.  L.  lacer,  ‘torn’.  See  lacerate and  -able.
20950:Derivative:  lacer abil-ity,  n. lacerate,  adj.  —  L.  laceratus,  ‘torn’,  pp.  of  lace- rare,  ‘to  tear  to  pieces’.  See  lacerate,  v. Derivative:  lacerate-ly,  adv. lacerate,  tr.  v.,  to  tear.  —  L.  laceratus,  pp.  of  lace- rare,  ‘to  tear  to  pieces,  rend,  lacerate’,  fr.  lacer, ‘torn’,  fr.  I.-E.  base  *leq-,  *llq-,  ‘to  rend’,  whence also  Gk.  Xa vie,,  ‘tatter,  rag’,  Xaxt^eiv,  ‘to  tear to  pieces,  lacerate’,  Alb.  I'akur,  ‘naked’,  Vekure, I’ikure,  ‘hide,  leather,  rind’.  Cp.  Iacinia,  lancina- te.  For  the  ending  see  verbal  suff.  -ate. Derivatives:  lacerat-ed,  adj.,  laceration  (q.v.) laceration,  n.  —  L.  laceratio,  gen.  -dnis,  ‘a  tearing, rending,  laceration’,  fr.  laceratus,  pp.  of  lacerare. See  prec.  word  and  -ion.
21088:lancinate,  tr.  v.,  to  tear.  —  L.  lancindtus,  pp.  of lancinare,  ‘to  tear  to  pieces,  rend,  lacerate’, which  is  rel.  to  lacerare,  of  s.m.  See  lacerate.
21133:laparotomy,  n.,  incision  into  the  abdominal  wall (surgery).  —  Coined  by  the  English  surgeon  Sir Thomas  Bryant  (1828-1914)  fr.  laparo-  and  Gk. -xopix,  ‘cutting  of’,  fr.  -ropd),  ‘a  cutting,  sec¬ tion’.  See  -tomy.
=== SKT
```


## [2026-09-06T23:12:25.130Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN laparo-\"; grep -n \"laparo-\\|lacinia,\" KLN_1966.txt | head -5\necho \"=== SYN 10380-10395\"; sed -n '10380,10395p' SYN.txt\necho \"=== ARY exists?\"; ls incoming/ARY/ 2>/dev/null\necho \"=== ARY grep\"; grep -n \"لخت\\|لاف\\|لابه\\|لاخ\" incoming/ARY/ARY_pages.txt | head -20"
}
```


### [2026-09-06T23:12:25.226Z] TOOL RESULT

```
=== KLN laparo-
21131:Derivative :  lap,  tr.  and  intr.  v.,  to  wrap,  enfold, lap,  tr.  v.,  to  lick  up;  intr.  v.,  to  lick  up  a  liquid. —  ME.  lapen,  lappen,  fr.  OE.  lapian,  ‘to  lick, lap  up,  sup’,  rel.  to  Swed.  lapa,  ‘to  drink,  lap’, OHG.  laffan,  ‘to  lick’,  OS.  lepil,  MLG.,  Du. lepel,  OHG.  leffil,  MHG.  leffel,  G.  Lojfel, ‘spoon’,  OE.  kepeldre,  ‘pot’,  and  cogn.  withGk. XirrxEiv,  ‘to  sip,  lick’,  Xaepuacretv,  ‘to  swallow greedily,  gulp  down’,  Arm.  lap'el,  L.  lambere, ‘to  lick’.  All  these  words  derive  from  the  I.-E. imitative  base  *tab-,  *lap(h)-.  Cp.  lambent. Derivatives:  tap,  n.,  the  act  of  lapping,  lapp-er,  n. lapar-,  form  of  laparo-  before  a  vowel, laparectomy,  n.,  surgical  removal  of  a  part  of  the abdominal  wall.  —  Compounded  of  lapar-  and Gk.  -exTopta,  ‘a  cutting  out  of’,  fr.  kx.-op.-t),  ‘a cutting  out'.  See  -ectomy.
21132:laparo-,  before  a  vowel  lapar-,  combining  form denoting  the  flank  or,  less  exactly,  the  abdominal wall  (anat.)  —  Fr.  Gk.  Xanapa,  ‘the  flank,  loins’, which  is  rel.  to  Xx7tap6?,  ‘soft,  flaccid,  hollow’, Xomdqeiv,  Xxnxaasiv,  ‘to  empty’,  and  in  gra¬ dational  relationship  to  Xe7xxq?,  ‘fine,  thin, small'.  See  lepto-.
21133:laparotomy,  n.,  incision  into  the  abdominal  wall (surgery).  —  Coined  by  the  English  surgeon  Sir Thomas  Bryant  (1828-1914)  fr.  laparo-  and  Gk. -xopix,  ‘cutting  of’,  fr.  -ropd),  ‘a  cutting,  sec¬ tion’.  See  -tomy.
=== SYN 10380-10395
orrm mm
a”
<n ne <a ee
=Zw
eS EM ST a i a wet a te)
opoTH 10
il, sb." 5), perh. NED s.V- ae rrowing fr. Grk.
uate pall Va a de-P. 2.58. Ernout- oves:
THs rk. gawéda (Rhin- on pac gawddns (by meta- | pap., etc.), this thesis ‘g pright-colored or shin-
: ‘light-bringing,
+ pawvones ve forth, reveal’.
115. erh. fr. lacer ‘torn, as S oe ne ‘rag’, Aaxifw ‘tear ‘ lochma ‘rag’. WaldeP. 2.419 £. Walde-H. tae: Frnout-M. 515 (“only pop. etym.”).
Late Lat. mantellum, dim. of a Celto- Iberian mantum, whence Sp. manto. Hence It. mantello, OF r. mantel (> ME nantel, NE mantle), Fr. manteau (> Rum. manta); Ir. mattal, matal (fr. ON moltull), W., Br. mantell (Loth, Mots lat. 184); ON mottull, OE mentel, OHG mantal, Du.. MHG, NHG mantel (>Sw. mantel, Lith. mantelis; Lett. mételis through ORuss. mjatili; also Slavic words, most in specialized sense. Emout-M. 589. Walde-H. 2.32 f. REW 5326, 5828. Berneker 2.17. we oe capa, te late Lat. cappa Mia ists fc overing’ (Isid.), whence vith caput ied (6.55), connection kappe, Sy a dub. Hence also Dan. Another = aA poet MLG kappe). ‘dpa, Dan, kaabe ie ee ON
’ cape, NE cope, OFr. cape). Ernout- i 1162. REW 1642. etym,? eee lenn, Gall. linna),
It, Nin bray roe, Stokes 252, Tedesen ig), Pt ‘cloth’ (6,21),
+ Coe,
=== ARY exists?
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
ARY_pages.txt.pages
=== ARY grep
923:گرایش به تجاوز از حریم‌های فانونی و ستنی که اغلب موجب برخورد و اختلاف آنان با سران
1172:نخستین به زبان‌های اوستایی و پارسی کهن و پهلوی و بالاخره فارسی نوین است. همانطو رکه در پیش
3888:پهلوی (1ماللم): 7 ,817۳۸۵ انگلیسی کین (لاخلاه2 هزم ,850
6411:1 ایرلندی کهن (لافتگا ۰:0۵ 65۸ ,610
7545:چم این واژه در زبان انگلیسی امروز: آهسته جاری شدن» (خون) آمدن؛ گل و لای» خون نیمه لخته.
10701:در مورد پیگیری سیر تطور این واژه میان دانشمندان اختلاف عقیده وجرد دارد (8۸3۷0111۸337 :240-341).
13178:04 ملافغانمتی 53516 عناق
14110:بلو چی (الل۲ناتهه): 2 دانمارکی [ لاخ ۸ ۸
14211:آلمانی ((682(4۸): 8 ات۸1۳7 ایرندی کهن (لافلقا صاه): 1
15894:برنانی 0888/0): ۰ ۸88۲۰۸3۸۲ ,لافآژگ۸ برهان قاطع + ۳۱۳۳
```


## [2026-09-06T23:12:34.183Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt; do echo \"--- $f\"; ls -la $f 2>/dev/null | awk '{print $5}'; grep -c \"لاف\" $f 2>/dev/null; done\necho \"=== v4 first/last page tags\"; grep -o \"\\[pdf page [0-9]*\\]\" incoming/BQT/BQT_v4_pages.txt | head -2; grep -o \"\\[pdf page [0-9]*\\]\" incoming/BQT/BQT_v4_pages.txt | tail -2"
}
```


### [2026-09-06T23:12:36.099Z] TOOL RESULT

```
--- BQT_v1_pages.txt
2247721
90
--- BQT_v2_pages.txt
4339896
79
--- incoming/BQT/BQT_v3_pages.txt
2499427
93
--- incoming/BQT/BQT_v4_pages.txt
2055176
68
--- incoming/BQT/BQT_v5_pages.txt
723928
31
=== v4 first/last page tags
[pdf page 1]
[pdf page 2]
[pdf page 552]
[pdf page 553]
```


## [2026-09-06T23:12:41.861Z] TOOL CALL #21: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T23:12:41.868Z] TOOL RESULT

```


```


## [2026-09-06T23:12:45.919Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%AE%D8%AA",
 "prompt": "Give the full Persian entry for لخت: etymologies, meanings (piece/scrap/rag/naked), Middle Persian forms, and any cited sources (Hasandust, Cheung, MacKenzie)."
}
```


## [2026-09-06T23:12:47.139Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%A7%D9%81",
 "prompt": "Give the Persian entry for لاف: etymology, meaning (boast/brag), and any related words such as لابه."
}
```


### [2026-09-06T23:12:55.159Z] TOOL RESULT

```
# Persian Entry for لخت

Based on the Wiktionary content provided, here's the complete entry:

## Etymologies & Meanings

**Etymology 1** (Adjective - naked/nude):
- Possibly related to Proto-Indo-European *reu-
- Transcription: *loxt*
- Meaning: "naked, nude"
- Synonyms: برهنه (berahne), عریان (oryân)

**Etymology 2** (Adjective - sleek):
- Derived from لخشیدن (laxšidan, "to slide")
- Transcription: *laxt*
- Meaning: sleek hair (Iranian Persian context)

**Etymology 3** (Noun - piece):
- Imitative element from dialects
- Transcription: *laxt*
- Meaning: "piece, portion"
- Related terms include: لخته (laxte, "clot"), لخشک (laxšak, "noodle")

**Etymology 4** (Noun - club):
- Related to Sanskrit लकुट (lakuṭa) and Persian لگد (lagad)
- Transcription: *laxt*
- Meaning: "club, mace" (archaic)
- Descendants: Middle Armenian լախտ (laxt) → Armenian; Georgian ლახტი (laxṭi)

## Sources Cited
The entry references Pokorny (1959) and Monchi-Zadeh (1990), but the specific cited authorities you mentioned are not present in this document.
```


### [2026-09-06T23:12:57.173Z] TOOL RESULT

```
# Persian Entry for لاف

**Etymology:** The word derives from Proto-Iranian origins, with cognates in Pashto and Sanskrit. It's related to Pashto *laudal* ("to say, tell") and Sanskrit *lapati* ("chatter").

**Meanings:** The primary definitions include "boast" and "bluff," capturing concepts of exaggeration or deceptive speech.

**Related Words:** Alternative forms include *لابه* (lâbe) and *لاوه* (lâve). Derived terms encompass *لاف زدن* (lâf zadan) and *لافزن* (lâfzan), both relating to the action of boasting.

**Note:** A colloquial secondary usage exists where لاف serves as an alternative form of *لحاف* (lehâf), meaning "blanket."

The word has traveled through Ottoman Turkish into numerous Balkan and Eastern European languages, including Albanian, Bulgarian, and Romanian variants.
```


## [2026-09-06T23:13:04.581Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad 2>/dev/null || cd /tmp\nfor w in \"%D9%84%D8%A7%D9%81\" \"%D9%84%D8%A7%D8%A8%D9%87\" \"%D9%84%D8%AE%D8%AA\" \"%D9%84%D8%A7%D8%AE\"; do\necho \"############ $w\"\ncurl -s -H 'User-Agent: rishe-verify/1.0' \"https://en.wiktionary.org/w/index.php?title=$w&action=raw\" | head -120\ndone"
}
```


### [2026-09-06T23:13:07.595Z] TOOL RESULT

```
############ %D9%84%D8%A7%D9%81
{{also|لاق}}

==Ottoman Turkish==

===Etymology===
{{bor+|ota|fa|لاف|tr=lâf}}.

===Noun===
{{head|ota|n|tr=lâf}}

# [[word]]
#: {{syn|ota|سوز|tr1=söz}}
# [[conversation]], [[chat]]
#: {{syn|ota|لقردی|tr1=lakırdı}}
#: {{coi|ota|'''لاف''' ایتمك|tr='''lâf''' etmek|to talk, converse}}
# [[babble]], [[chatter]], [[chit-chat]]
#: {{coi|ota|'''لاف''' آتمق|tr='''lâf''' atmak|to chatter, babble}}
# [[boastfulness]], [[bragging]]
#: {{coi|ota|'''لاف''' اورمق|tr='''lâf''' urmak|to boast}}

====Related terms====
{{col|ota|لافزن<tr:lâfazan>}}

====Descendants====
* {{desc|tr|laf}}
* {{desc|sq|llaf|bor=1}}
* {{desc|hy|լաֆ|bor=1}}
* {{desc|rup|lafi//lafe|bor=1}}
* {{desc|bg|лаф|bor=1}}
* {{desc|mk|лаф|bor=1}}
* {{desc|ro|laf|bor=1}}

===References===
* {{R:ota:Kelekian|page=1072a}}
* {{R:ota:Redhouse|page=1619b}}

==Persian==

===Etymology 1===
From {{inh|fa|ira-pro}}, cognate with {{cog|ps|لودل|tr=laudal|t=to say, tell}}, and {{cog|sa|लपति|t=chatter}}.

====Pronunciation====
{{fa-IPA|lāf}}

====Noun====
{{fa-noun|tr=lâf}}

# [[boast]]
# [[bluff]]

=====Alternative forms=====
* {{alt|fa|لابه|لاوه|tr=lâbe|tr2=lâve}}

=====Derived terms=====
{{col|fa|لافزن<tr:lâfzan>|لاف زدن<tr:lâf zadan>}}

=====Descendants=====
* {{desctree|ota|لاف|tr=laf|bor=1}}
* {{desc|tk|lap|bor=1}}

====References====
* {{R:fa:Horn|pages=212}}
* {{R:Dehkhoda|لاف}}

===Etymology 2===
{{nonlemma}}

====Noun====
{{fa-noun|tr=lâf}}

# {{lb|fa|colloquial}} {{alternative form of|fa|لحاف|t=blanket|tr=lehâf}}

==Tunisian Arabic==

===Etymology===
From {{inh|aeb|ar|آلَافٌ}}

===Pronunciation===
* {{IPA|aeb|[le̞ːf]}}

===Noun===
# {{plural of|aeb|ألف}}############ %D9%84%D8%A7%D8%A8%D9%87
{{also|لابة}}
==Persian==

===Etymology===
{{inh+|fa|pal|sc=Phlv|tr=lʾpk'|ts=lābag}}. Compare {{cog|kmr|lava}}.

===Pronunciation===
{{fa-IPA|lāˈba}}

===Noun===
{{fa-noun|tr=lâbe}}

# [[humble]] [[supplication]]; [[entreaty]]
#* {{quote-book|fa|title=fa:شاهنامه|trans-title={{w|Shahnameh|Book of Kings}}|year=c. 1011|author={{w|Ferdowsi|Abu'l-Qāsim Firdawsī}}|chapter=The Tale of Rustam and Isfandiyār|url=https://ganjoor.net/ferdousi/shahname/esfandyar/sh28|text=بدانست رستم که '''لابه''' به کار<br>نیاید همی پیش اسفندیار<br>کمان را به زه کرد و آن تیر گز<br>که پیکانش را داده بد آب رز<br>همی راند تیر گز اندر کمان|tr=bidānist rustam ki '''lāba''' ba kār<br>nay-āyad hamē pēš-i isfandiyār<br>kamān rā ba zih kard u ān tīr-i gaz<br>ki paykān-aš rā dāda bud āb-i raz<br>hamē rānd tīr-i gaz andar kamān|t=Rustam understood that '''humble entreaty'''<br>Was of no use before Isfandiyār.<br>He strung his bow, and that tamarisk arrow<br>Whose arrowpoint he had dipped in wine:<br>He was running that arrow upon the bow.|footer=(Classical Persian romanization)}}############ %D9%84%D8%AE%D8%AA
==Persian==

===Etymology 1===
{{ety|fa|id=naked}}
Possibly related to {{uder|fa|ine-pro|*reu-}}.<ref>{{R:ine:IEW|pages=868-871}}</ref> Compare the classical form {{m|fa|رت|tr=rot}} with the same meaning.

====Adjective====
{{fa-regional|لخت|لخت|лухт}}
{{fa-adj|tr=loxt}}

# [[naked]], [[nude]]
#: {{syn|fa|برهنه|tr1=berahne|عریان|tr2=oryân}}

===Etymology 2===
{{ety|fa|id=sleek}}
From {{m|fa|لخشیدن|tr=laxšidan||to slide}}.

====Adjective====
{{fa-adj|tr=laxt}}

# {{lb|fa|Iran|of hair}} [[sleek]]

===Etymology 3===
{{ety|fa|id=piece}}
An imitative element borrowed from dialects.<ref>{{R:fa:Monchi-Zadeh:1990|page=115 Nr. 336}}</ref>

====Noun====
{{fa-regional|لخت|لخت|лахт}}
{{fa-adj|tr=laxt}}

# [[piece]], [[portion]]

=====Related terms=====
{{col|fa
|لخشک<tr:laxšak><t:noodle>
|لک<tr:lak><t:stain><id:stain>
|⁧سنگلاخ⁩<tr:sanglâx><t:stony>
|لخته<tr:laxte><t:clot>
|لق<tr:laq>,لغ<tr:laġ><t:an addle egg>
|لخت<tr:laxt><t:club, mace><id:club>
}}

===Etymology 4===
{{ety|fa|id=club}}
Related to {{m|sa|लकुट|t=club}} and {{m|fa|لگد|tr=lagad|t=kick; recoil}}.

====Noun====
{{fa-regional|لخت|لخت|лахт}}
{{fa-adj|tr=laxt}}

# {{lb|fa|archaic}} [[club]], [[mace]]

=====Descendants=====
* {{desctree|axm|լախտ|bor=1}}
* {{desc|ka|ლახტი|bor=1}}

===References===
{{reflist}}

{{C|fa|Weapons}}############ %D9%84%D8%A7%D8%AE
==Persian==

===Pronunciation===
{{fa-IPA|lāx}}

===Noun===
{{fa-noun|tr=lâx}}

# [[lock]] (of hair)
```


## [2026-09-06T23:13:17.991Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 233 (printed p.212)\"; awk 'BEGIN{RS=\"\\f\"} NR==234' HRN.txt | head -60"
}
```


## [2026-09-06T23:13:19.689Z] TOOL CALL #26: Bash

```json
{
 "command": "for w in \"-%D9%84%D8%A7%D8%AE\" \"%D8%B3%D9%86%DA%AF%D9%84%D8%A7%D8%AE\"; do echo \"###### $w\"; curl -s -H 'User-Agent: rishe-verify/1.0' \"https://en.wiktionary.org/w/index.php?title=$w&action=raw\" | head -60; done"
}
```


### [2026-09-06T23:13:20.639Z] TOOL RESULT

```
=== HRN leaf 233 (printed p.212)
— 212 —
949. (feU ^Welt\
aw. ga^^ya- 'irdisch'; phlv. getlk^).
Mot savant; die den Lautgesetzen entsprechende
neupersische Form ist gehän (No. 951).
950. ges, gesü 'Locken, öelock'.
aw. ga^sa- 'in zwei oder drei (sc. Locken) geord-
netes Haar (ZBÖL); phlv. g^s^ arm. syr. LW. ges,
ü^: *Haar\
oss. d. yesä, t. qts *Borste*.
951. gehän *Welt\ arab. LW. ßhan, jehän^),
aw. gae^ä' (gaf.&anqm); phlv. gehän, vergl. tahn.
r:} (de La gar de, Semitica I, 59).
L.
952. lfrJ)e, läwe 'Schmeichelei, Bitte', lähidefi,, laf 'Prahlerei*.
skr. l^lap' (ai. rap-), Idpati 'schwatzen', vergl.
ud + lap' 'liebkosen .
siyn. I6w-am, sar. lew-am 'reden, sprechen, sagc^n';
af/. laudal 'sagen, erzählen'.
953. leh 'Lippe*, vergl. lefj^ leföe.
Käs. lew; kauk.-bergjüd. low,
phlv. lap; lat. labium; nhd. lAppe (vgl. Kluge,
Etymolog. Wörterbuch s. v.).
kurd. liw 'Lippe'; bei. lap (216); wa;^. law^ lafc,
sangl. law,
954. listen 'lecken*, Praes. les-em, lestden.
Kää. Z. bSles,
phlv. listan, l(i)stan (AV.); ap. l/^*lais- {V^leig^h- + ,<?);
vergl. ai. [/'reh-^ rehmi, skr. teÄ-, lehnii 'ich lecke*;
arm. lizeniy lizum etc. (H. No. 123); wa/. li/'am.
^) Die Syrer schreiben nach Mitteilung des Herrn Prof. Nöldeke
gethih, und so ist also wohl auch im Pehlevl get(Ofi zu lesen. Np. geil
geht aber jedenfalls auf ein, dann allerdings falsches, phlv. ge Ik zurück.
Ist get(i)h etwa von st(Oh beeinflusst?
*) Eine persische Etymologie (von jehlden) siehe Vis und Rämln,
Seite 83 Vers 17.
```


### [2026-09-06T23:13:22.637Z] TOOL RESULT

```
###### -%D9%84%D8%A7%D8%AE
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Not Found</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1100 cp1100, Varnish XID 749698176<br>Upstream caches: cp1100 int<br>Error: 404, Not Found at Sun, 06 Sep 2026 23:13:22 GMT<br><details><summary>Sensitive client information</summary>IP address: 187.15.139.71</details></code></p>
</div>
</html>
###### %D8%B3%D9%86%DA%AF%D9%84%D8%A7%D8%AE
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Not Found</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1100 cp1100, Varnish XID 699299682<br>Upstream caches: cp1100 int<br>Error: 404, Not Found at Sun, 06 Sep 2026 23:13:22 GMT<br><details><summary>Sensitive client information</summary>IP address: 187.15.139.71</details></code></p>
</div>
</html>
```


## [2026-09-06T23:13:43.455Z] TOOL CALL #27: WebSearch

```json
{
 "query": "پسوند «لاخ» ریشه‌شناسی سنگلاخ دیولاخ حسن‌دوست پسوند مکان"
}
```


## [2026-09-06T23:13:44.094Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/lacerate",
 "prompt": "Give the etymology of \"lacerate\" including the PIE root and Greek cognates."
}
```


### [2026-09-06T23:13:50.985Z] TOOL RESULT

```
# Etymology of "Lacerate"

**Origin:** The verb lacerate entered English in the early 15c. from Latin *laceratus*, the past participle of *lacerare*, meaning "tear to pieces, mangle."

**PIE Root:** The Latin term derives from the Proto-Indo-European root "*l**ē**k-," which means "to rend, tear."

**Greek Cognates:** Related Greek words include *lakis* (meaning "tatter, rag") and *lakizein* (meaning "to tear to pieces"). These demonstrate how the root spread across ancient languages to express similar concepts of tearing and breaking apart.

The word's meaning expanded figuratively in English by the 1640s to encompass emotional harm, such as "torture" or "harrow" the feelings.
```


### [2026-09-06T23:13:53.128Z] TOOL RESULT

```
Web search results for query: "پسوند «لاخ» ریشه‌شناسی سنگلاخ دیولاخ حسن‌دوست پسوند مکان"

Links: [{"title":"معنی لاخ | لغت‌نامه دهخدا","url":"https://www.vajehyab.com/dehkhoda/%D9%84%D8%A7%D8%AE"},{"title":"سنگلاخ به انگلیسی - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatoen/%D8%B3%D9%86%DA%AF%D9%84%D8%A7%D8%AE/"},{"title":"سنگلاخ - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%B3%D9%86%DA%AF%D9%84%D8%A7%D8%AE/"},{"title":"لاخ - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D9%84%D8%A7%D8%AE/"},{"title":"لاخ | در فرهنگ لغات ها (دهخدا،معین و ... ) + سایر منابع اطلاعاتی | جدول یاب","url":"https://www.jadvalyab.ir/fa2fa/%D9%84%D8%A7%D8%AE"},{"title":"دیولق دهکده باستانی من","url":"http://divlagh.com/"},{"title":"سنگلاخ یعنی چه ? - مجله نورگرام","url":"https://mag.noorgram.ir/1402/01/04/%D8%B3%D9%86%DA%AF%D9%84%D8%A7%D8%AE-%DB%8C%D8%B9%D9%86%DB%8C-%DA%86%D9%87/"}]

بر اساس نتایج جستجو، در اینجا اطلاعات مرتبط با پسوند «لاخ» و ریشه‌شناسی آن آمده است:

## تعریف پسوند «لاخ»

پسوند «لاخ» از ادات محل است که به آخر کلماتی چون نمکلاخ، دیولاخ، سنگلاخ، اهرمن‌لاخ، رودلاخ، آتش‌لاخ، هندولاخ، کلوخ‌لاخ و غیره می‌پیوندد.

## معنی پسوند

پسوند «لاخ» به معنی جای و مقام است، اما بدون ترکیب گفته نمی‌شود؛ مثلاً سنگلاخ، دیولاخ و رودلاخ به ترتیب به معنی جای سنگ، جای دیو و جای رود هستند.

## مثال‌ها

«سنگلاخ» به معنی زمین پر از سنگ است، و مشابه آن در ترکی «دیولاخ» به معنی مکان دیو یا جایی که محل زندگی دیو است.

## ریشه‌شناسی

درباره ریشه‌شناسی این پسوند، پسوند مکانی «لاخ» با واژگان «لای» و «لایه» در زبان پارسی از یک بن و ریشه است.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T23:14:05.666Z] TOOL CALL #29: WebSearch

```json
{
 "query": "Persian suffix -lāx sanglāx origin Turkic -laq place suffix etymology Iranian"
}
```


## [2026-09-06T23:14:06.163Z] TOOL CALL #30: WebSearch

```json
{
 "query": "Old High German \"gilari\" \"Gelärre\" etymology -lar place names Wetzlar Goslar Suffix Bedeutung"
}
```


### [2026-09-06T23:14:12.486Z] TOOL RESULT

```
Web search results for query: "Persian suffix -lāx sanglāx origin Turkic -laq place suffix etymology Iranian"

Links: [{"title":"Etymology of Persian suffix ان-/-ân, (Not its plural marker sense) | WordReference Forums","url":"https://forum.wordreference.com/threads/etymology-of-persian-suffix-%D8%A7%D9%86-%C3%A2n-not-its-plural-marker-sense.3637663/"},{"title":"(PDF) THE PERSIAN SUFFIX -(e)stān ‘THE LAND OF’","url":"https://www.academia.edu/98399275/THE_PERSIAN_SUFFIX_e_st%C4%81n_THE_LAND_OF_"},{"title":"Annotating Cognates and Etymological Origin in Turkic Languages","url":"https://arxiv.org/pdf/1501.03191"},{"title":"۲۰. Suffixes – دستورِ زبانِ پارسی","url":"https://www.dastur.info/persian-grammar/20-suffixes/"},{"title":"Persian affixes in Turkish - AfBo 2.0","url":"https://afbo.info/pairs/107"},{"title":"-shat","url":"https://en.wikipedia.org/wiki/-shat"},{"title":"Ajem-Turkic","url":"https://en.wikipedia.org/wiki/Ajem-Turkic"},{"title":"List of geographic names of Iranian origin","url":"https://en.wikipedia.org/wiki/List_of_geographic_names_of_Iranian_origin"}]

Based on the search results, I found information about Persian place suffixes, but the search didn't return specific information about the "-lāx" suffix, "sanglāx," or a direct connection between the Persian "-lāx" and the Turkic "-laq" suffix. 

The results do provide relevant context about Persian place-naming suffixes:

A common locative suffix in Middle Persian was -ān, derived from Iranian *-āna, which is used in place names. However, this appears to be distinct from the "-lāx" suffix you're asking about.

The search results don't contain specific information about:
- The etymology of the Persian suffix "-lāx" in words like "sanglāx"
- Whether it has Turkic origins
- A direct etymological connection to the Turkic "-laq" place suffix

To get more targeted information about this specific suffix and its cross-linguistic etymology, you might want to consult specialized etymological dictionaries or academic papers focused on Persian-Turkic linguistic contacts and suffix borrowing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-06T23:14:24.625Z] TOOL RESULT

```
Web search results for query: "Old High German "gilari" "Gelärre" etymology -lar place names Wetzlar Goslar Suffix Bedeutung"

Links: [{"title":"Old High German Submitted Names - Behind the Name","url":"https://www.behindthename.com/submit/names/usage/old-high-german"},{"title":"Aach (toponymy)","url":"https://en.wikipedia.org/wiki/Aach_(toponymy)"},{"title":"High Germany","url":"https://en.wikipedia.org/wiki/High_Germany"},{"title":"Adalbero","url":"https://en.wikipedia.org/wiki/Adalbero"},{"title":"List of people, clan, and place names in Germanic heroic legend","url":"https://en.wikipedia.org/wiki/List_of_people,_clan,_and_place_names_in_Germanic_heroic_legend"},{"title":"Gernot","url":"https://en.wikipedia.org/wiki/Gernot"},{"title":"Old High German declension","url":"https://en.wikipedia.org/wiki/Old_High_German_declension"},{"title":"R%C3%BCti","url":"https://en.wikipedia.org/wiki/R%C3%BCti"},{"title":"Category:Old High German given names - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Old_High_German_given_names"}]

Let me search more specifically for the terms and place names you mentioned:

Links: [{"title":"Wetzlar","url":"https://en.wikipedia.org/wiki/Wetzlar"},{"title":"German place name suffixes - German to English translation on #KudoZ Term Help Network.","url":"https://www.proz.com/kudoz/german-to-english/geography/513088-german-place-name-suffixes.html"},{"title":"Laber","url":"https://en.wikipedia.org/wiki/Laber"},{"title":"Goslar (disambiguation)","url":"https://en.wikipedia.org/wiki/Goslar_(disambiguation)"},{"title":"Goslar","url":"https://en.wikipedia.org/wiki/Goslar"},{"title":"Goslar (district)","url":"https://en.wikipedia.org/wiki/Goslar_(district)"},{"title":"Oker (Goslar)","url":"https://en.wikipedia.org/wiki/Oker_(Goslar)"},{"title":"German placename etymology - Academic Kids","url":"https://academickids.com/encyclopedia/index.php/German_placename_etymology"}]

Let me search more specifically for the historical Germanic terms you mentioned:

Links: [{"title":"An Etymological Dictionary of the German Language/Annotated/T (full text) - Wikisource, the free online library","url":"https://en.wikisource.org/wiki/An_Etymological_Dictionary_of_the_German_Language/Annotated/T_(full_text)"},{"title":"Old High German Elements - Behind the Name","url":"https://www.behindthename.com/elements/usage/old-high-german"},{"title":"forest clearance - Sierterm UEM | Terminología trilingüe","url":"https://www.sierterm.es/content/forest-clearance/?lang=en"},{"title":"Old High German","url":"https://en.wikipedia.org/wiki/Old_High_German"},{"title":"An Etymological Dictionary of the German Language/Annotated/Wald - Wikisource, the free online library","url":"https://en.wikisource.org/wiki/An_Etymological_Dictionary_of_the_German_Language/Annotated/Wald"},{"title":"Clearing (geography)","url":"https://en.wikipedia.org/wiki/Clearing_(geography)"},{"title":"Browse Submitted Names - Behind the Name","url":"https://www.behindthename.com/submit/names/usage/ancient-germanic/meaning/forest"}]

Links: [{"title":"Geldern (definition and history)","url":"https://www.wisdomlib.org/cities/geldern-15257"},{"title":"Gelre - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Gelre"},{"title":"Gelderen - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Gelderen"},{"title":"Landscape - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/landscape"},{"title":"German Forest","url":"https://en.wikipedia.org/wiki/German_Forest"},{"title":"glade Definition & Meaning - English Dictionary - DictClub","url":"https://dictclub.com/dictionary/glade"},{"title":"Landschaft - Translation in English - Langenscheidt dictionary German-English","url":"https://en.langenscheidt.com/german-english/landschaft"},{"title":"etymologies - landscape theory - WordPress.com","url":"https://landscapetheory1.wordpress.com/category/profession/definitions/etymologies/"},{"title":"G%C3%A4u","url":"https://en.wikipedia.org/wiki/G%C3%A4u"},{"title":"H%C3%BCgelland","url":"https://en.wikipedia.org/wiki/H%C3%BCgelland"}]

Let me try one more specific search for the -lar place name suffix:

Links: [{"title":"R%C3%BCti","url":"https://en.wikipedia.org/wiki/R%C3%BCti"},{"title":"Laber","url":"https://en.wikipedia.org/wiki/Laber"},{"title":"Aach (toponymy)","url":"https://en.wikipedia.org/wiki/Aach_(toponymy)"},{"title":"German place name suffixes - German to English translation on #KudoZ Term Help Network.","url":"https://www.proz.com/kudoz/german-to-english/geography/513088-german-place-name-suffixes.html"},{"title":"High Germany","url":"https://en.wikipedia.org/wiki/High_Germany"},{"title":"Old High German declension","url":"https://en.wikipedia.org/wiki/Old_High_German_declension"},{"title":"Churl","url":"https://en.wikipedia.org/wiki/Churl"},{"title":"German toponymy — Grokipedia","url":"https://grokipedia.com/page/German_toponymy"}]

Based on my web search results, I was unable to find specific information about the Old High German terms "gilari" or "Gelärre," their etymology, or the "-lar" suffix you mentioned in relation to place names like Wetzlar and Goslar.

However, I did find some related information about Germanic place name suffixes and clearing terminology:

Rüti comes from the Old High German word riod, meaning "clearing", demonstrating that Old High German did have vocabulary related to forest clearings used in place names. Additionally, the suffix -roda (or -rode, as in Wernigerode) stems from the German word "roden" meaning to clear a forest, indicating that originally someone cleared the forest.

Unfortunately, the specific etymological terms and place name suffix you're asking about ("gilari," "Gelärre," and "-lar") do not appear in readily available English-language sources online. These may be specialized historical linguistic terms found primarily in German etymological or place name dictionaries. I would recommend consulting:

- Specialized German etymological dictionaries
- Academic works on Old High German toponymy
- Regional historical place name studies focusing on areas like Wetzlar and Goslar

Would you like me to search for information about specific aspects of these place names, or would you like to provide more context about where you encountered these terms?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T23:14:36.783Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^Root / lemma: /?e[hs]*s\\|lemma: les\\|lemma: /es\" POK_full.txt | head\necho \"--- search sammeln lisan\"\ngrep -n \"lisan\" POK_full.txt | head\necho \"--- around page 680\"\ngrep -n \"Page(s): 680\\|Page(s): 681\" POK_full.txt | head"
}
```


### [2026-09-06T23:14:36.858Z] TOOL RESULT

```
--- search sammeln lisan
55504:Material: Gothic lisans\.exx\ V. " compile, collect, reap'. Old Icelandic /es5 "gather, collect, 
--- around page 680
55519:Page(s): 680 
55534:Page(s): 680 
55550:Page(s): 681 
56179:Page(s): 681 
56279:Page(s): 681-682 
56783:Page(s): 680 
56798:Page(s): 680
```


## [2026-09-06T23:14:38.812Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '55495,55555p' POK_full.txt"
}
```


### [2026-09-06T23:14:38.864Z] TOOL RESULT

```
in addition Modern High German Lurch, ndd. lork {* lehurgh^l 

References: WP. II 439. S. still Vo/yo- "stick". 
Page(s): 679 

Root / lemma: lehs- {*lehu^ 
Meaning: to gather, pick up 

Material: Gothic lisans\.exx\ V. " compile, collect, reap'. Old Icelandic /es5 "gather, collect, 
compile, work in ', later (through Modern High German influence) " read (a book)'. Old 
English /esa/7 "gather, collect'. Old Saxon Old High German lesan^ pick up, select ' and 
(after the double meaning from Latin legere) " read (a book)'; here also Old Icelandic lesa. 
Middle High German (Modern High German dial.) lismen^ knit ', Old High German lesa. 
Middle High German /ese" a kind of clothes material ', Old Icelandic lesnr a kind of head 
stuff '; 

Lithuanian lesu, lestl {* /ehusfl}' peck, pick ', Iter, ap-lasytr peck out, pick out, sort, 
choose '; 

whether here Old Irish lestar, loanword from cymr. Ilestr 'vesseV, acorn, lester, bret. lestr 
"ship'? basic meaning would be " vessel for collecting of berries '. 

References: WP. II 440, Trautmann 160. 
Page(s): 680 

Root /lemma: lehtoh- lehtih- lehtoh- ldhtoh-{*lehutoh-) 
Meaning: heat 



Material: Mcymr. aelet{*ad-leht-) "pain", Ilet-gynt6s., lengthened grade ////, tra-M'rage, 
fury', ncymr. ///dm. ds., with gradation //an/o'" rutting, heat' = Middle Irish /at/im. ds.; 
mcymr. ae/awt'6'\n, fuss, noise, pain' = Old Irish a/adn. 'wound' {*ad-/dhtoh-), cymr. tra- 
//od'd'm, fuss, noise, pain'; 

kir. //?f. 'rutting, heat', ///j//j/' impregnate, fertilize '. 

References: WP. II 428, Ifor Williams Et. Celt. 4, 391. 
Page(s): 680 

Root / lemma: lehtro- {*lehutro-) 

Meaning: leather 

Material: Old Irish /et/iar, cymr. //edr, bret. /ezr'leather' = Old High German /eder. Old 

English /et^er{ev\Q\. /eat/iei). Old Icelandic /edru. 'leather'. Is the Germanic word old 

borrowing from Celtic and latter as "pAe-Z/TO related to Latin pe///s etc. (see peh/-^sk\n')7 S. 

Pedersen KG. II 45. 

References: WP. II 428. 

Page(s): 681 

Root / lemma: /ehit'^- 

Meaning: to care for, love
```


## [2026-09-06T23:14:53.762Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/leer",
 "prompt": "Give the German entry for \"leer\": etymology, Old High German form lāri, Proto-West Germanic / Proto-Germanic reconstruction, and the PIE root it is traced to."
}
```


## [2026-09-06T23:14:55.029Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://www.vajehyab.com/dehkhoda/%D9%84%D8%A7%D8%AE",
 "prompt": "Give the full Dehkhoda entry text for لاخ, especially the description of it as a suffix of place (ادات محل) and the examples given."
}
```


### [2026-09-06T23:14:59.145Z] TOOL RESULT

```
# German Entry for "Leer"

**Etymology:** From Middle High German _lēr_, _lēre_, _lǣre_, derived from Old High German _lāri_, which traces back through Proto-West Germanic _*lāʀi_ and Proto-Germanic _*lēziz_.

**Old High German Form:** _lāri_

**Proto-West Germanic:** _*lāʀi_

**Proto-Germanic:** _*lēziz_

**PIE Root:** The entry does not explicitly state a Proto-Indo-European root for this particular German word. However, it notes cognates with Dutch _laar_ ("clearing in woods") and English _leer_, suggesting a shared Germanic origin related to concepts of emptiness or clearness.
```


### [2026-09-06T23:15:02.423Z] TOOL RESULT

```
# Dehkhoda Dictionary Entry for لاخ

The entry describes لاخ as "a suffix of place" that attaches to words like نمکلاخ, دیولاخ, سنگلاخ, and رودلاخ.

## Primary Meaning
"جای . معدن" (place, location, mine). The dictionary notes it means location or position but "is not used independently" except in compound forms.

## Key Examples of Compounds
The entry lists these place-related compounds:
- **سنگلاخ** - rocky/stony place
- **دیولاخ** - demon's place (desolate/dangerous location)
- **رودلاخ** - riverside area
- **نمکلاخ** - salt marsh/lake
- **آتش لاخ** - fire location
- **اهرمن لاخ** - evil place

## Supporting Evidence
The dictionary includes poetic citations from Nezami and Amir Khosrow demonstrating usage, such as references to "دیولاخهای رباط کرنان" (wastelands of caravanserais) in Beihaki's historical text.

The suffix functions similarly to Turkic "-lik" constructions, indicating it's a place-marking morpheme in Persian compound formation.
```


## [2026-09-06T23:15:12.430Z] TOOL CALL #35: Bash

```json
{
 "command": "pdftoppm -f 309 -l 309 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg309 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg309.png"
}
```


## [2026-09-06T23:15:13.760Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%84%D8%AE%D8%AA/",
 "prompt": "Give the Mo'in (فرهنگ معین) and Dehkhoda entries for لخت, including any bracketed origin tag (e.g. [په.]) and the senses 'piece, portion, scrap' and 'naked'."
}
```


### [2026-09-06T23:15:14.352Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 72781 Sep  6 19:15 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg309.png
```


### [2026-09-06T23:15:21.705Z] TOOL RESULT

```
# Lexicographic Entries for لخت

## Mo'in Dictionary (فرهنگ معین)

Under the (لَ) pronunciation mark with (اِ.) notation:
"جزو، نوع ، قسم" (a component, type, or category)

The entry also includes (لُ) pronunciation: "برهنه ، عریان" (naked or bare)

## Dehkhoda Dictionary (لغت نامه دهخدا)

The second major entry under (لَ) with (اِ.) marking lists:
"جزو. بعض. برخ. بهر. بخش. قسم. پرگاله. قدر. مقدار. حصه. قطعه. پاره" 

This catalogs meanings related to portions and fragments, illustrated through classical Persian poetry citations featuring the term in contexts describing pieces or portions of objects.
```


## [2026-09-06T23:15:23.965Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg309.png"
}
```


### [2026-09-06T23:15:24.330Z] TOOL RESULT

```

```


## [2026-09-06T23:15:24.325Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T23:15:49.052Z] TOOL CALL #38: Bash

```json
{
 "command": "for w in \"%D5%AC%D5%A1%D5%A9\" \"%E0%A4%B2%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%95\" \"lacer\" \"%CE%BB%CE%B1%CE%BA%CE%AF%CF%82\" \"%CE%BB%CE%B1%CF%80%CE%B1%CF%81%CF%8C%CF%82\" \"lepos\"; do echo \"###### $w\"; curl -s -H 'User-Agent: rishe-verify/1.0' \"https://en.wiktionary.org/w/index.php?title=$w&action=raw\" | head -70; echo; done"
}
```


### [2026-09-06T23:15:52.104Z] TOOL RESULT

```
###### %D5%AC%D5%A1%D5%A9
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Not Found</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1100 cp1100, Varnish XID 613051332<br>Upstream caches: cp1100 int<br>Error: 404, Not Found at Sun, 06 Sep 2026 23:15:51 GMT<br><details><summary>Sensitive client information</summary>IP address: 187.15.139.71</details></code></p>
</div>
</html>

###### %E0%A4%B2%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%95
<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>Wikimedia Error</title>
<style>
* { margin: 0; padding: 0; }
body { background: #fff; font: 15px/1.6 sans-serif; color: #333; }
.content { margin: 7% auto 0; padding: 2em 1em 1em; max-width: 640px; display: flex; flex-direction: row; flex-wrap: wrap; }
.footer { clear: both; margin-top: 14%; border-top: 1px solid #e5e5e5; background: #f9f9f9; padding: 2em 0; font-size: 0.8em; text-align: center; }
img { margin: 0 2em 2em 0; }
a img { border: 0; }
h1 { margin-top: 1em; font-size: 1.2em; }
.content-text { flex: 1; }
p { margin: 0.7em 0 1em 0; }
a { color: #0645ad; text-decoration: none; }
a:hover { text-decoration: underline; }
code { font-family: sans-serif; }
summary { font-weight: bold; cursor: pointer; }
details[open] { background: #970302; color: #dfdedd; }
.text-muted { color: #777; }
@media (prefers-color-scheme: dark) {
  a { color: #9e9eff; }
  body { background: transparent; color: #ddd; }
  .footer { border-top: 1px solid #444; background: #060606; }
  #logo { filter: invert(1) hue-rotate(180deg); }
  .text-muted { color: #888; }
}
</style>
<meta name="color-scheme" content="light dark">
<div class="content" role="main">
<a href="https://www.wikimedia.org"><img id="logo" src="https://www.wikimedia.org/static/images/wmf-logo.png" srcset="https://www.wikimedia.org/static/images/wmf-logo-2x.png 2x" alt="Wikimedia" width="135" height="101">
</a>
<div class="content-text">
<h1>Error</h1>

<p>Not Found</p>
</div>
</div>
<div class="footer"><p>If you report this error to the Wikimedia System Administrators, please include the details below.</p><p class="text-muted"><code>Request served via cp1100 cp1100, Varnish XID 894861515<br>Upstream caches: cp1100 int<br>Error: 404, Not Found at Sun, 06 Sep 2026 23:15:51 GMT<br><details><summary>Sensitive client information</summary>IP address: 187.15.139.71</details></code></p>
</div>
</html>

###### lacer
==English==

===Etymology===
{{ety|en|:af|lace|-er<id:agent noun>|text=+|tree=1}}

===Pronunciation===
* {{IPA|en|/ˈleɪs.ə(ɹ)/|a=UK}}
* {{audio|en|LL-Q1860 (eng)-Vealhurl-lacer.wav|a=Southern England}}
* {{rhymes|en|eɪsə(ɹ)|s=2}}
* {{homophones|en|laser}} {{qualifier|Etymology 2}}

===Noun===
{{en-noun}}

# A person or thing that [[lace#Verb|lace]]s.

====Derived terms====
{{col|en|tightlacer
}}

====Translations====
{{trans-top|one who laces}}
* Turkish: {{t+|tr|oyacı}}
*: Ottoman Turkish: {{t|ota|اویاجی|tr=oyacı}}
{{trans-bottom}}

===Anagrams===
* {{anagrams|en|a=acelr|Carle|'clare|Clare|Clear|Caler|Carel|carle|recal|clear}}

==French==

===Etymology===
{{inh+|fr|frm|lacer}}, from {{inh|fr|fro|lacier}}, from {{inh|fr|la|laqueo|laqueare}}.

===Pronunciation===
* {{fr-IPA|pos=v}}
* {{audio|fr|LL-Q150 (fra)-LoquaxFR-lacer.wav|a=<<France>> (<<Vosges>>)}}
* {{audio|fr|LL-Q150 (fra)-DSwissK-lacer.wav|a=<<Switzerland>> (<<Valais>>)}}
* {{audio|fr|LL-Q150 (fra)-Lyokoï-lacer.wav|a=<<France>> (<<Lyon>>)}}
* {{audio|fr|LL-Q150 (fra)-Poslovitch-lacer.wav|a=<<France>> (<<Vosges>>)}}
* {{audio|fr|LL-Q150 (fra)-WikiLucas00-lacer.wav|a=<<France>> (<<Lyon>>)}}
* {{audio|fr|LL-Q150 (fra)-Jérémy-Günther-Heinz Jähnick-lacer.wav|a=<<France>> (<<Somain>>)}}
* {{homophones|fr|laçai|lacé|lacée|lacées|lacés|lacez|qq6=general|;|lassai|lassé|lassée|lassées|lasser|lassés|lassez|qq13=with {{IPAchar|/a/}}}}

===Verb===
{{fr-verb}}

# to [[lace]], to [[lace up]]

====Conjugation====
{{fr-conj-auto}}

====Related terms====
* {{l|fr|lacs}}
* {{l|fr|lacet}}

===Further reading===
* {{R:fr:TLFi}}

===Anagrams===
* {{l|fr|caler}}, {{l|fr|racle}}, {{l|fr|raclé}}

==Latin==

===Etymology===
{{ety|la|:inh|itc-pro:*lakeros<ety:inh<ine-pro:*leh₂-<id:bark><alt:*leh₂k->>>|text=++|tree=1}} Cognate with {{m|la|lancinō}}, {{cog|grc|λᾰκίς|t=rending, tatters}}, {{cog|sla-pro|*laxъ|t=rags}} (whence {{cog|pl|łach|t=id}}).<ref>{{R:itc:EDL|head=lacer|pages=320-1}}</ref>

===Pronunciation===
* {{la-IPA|lacer}}


###### %CE%BB%CE%B1%CE%BA%CE%AF%CF%82
==Ancient Greek==

===Etymology===
From {{inh|grc|grk-pro|*lakíds}}, from {{der|grc|ine-pro|*leh₂-|*leh₂k-|to tear}}. Cognate with {{cog|la|lacer}} and {{m|la|lancinō}}.

===Pronunciation===
{{grc-IPA|λᾰκί˘ς}}

===Noun===
{{grc-noun|λᾰκῐ́ς|λᾰκῐ́δος|f|third}}

# {{lb|grc|often in the plural}} [[rent]], [[rend]]ing, [[tatter]]s

====Declension====
{{grc-decl|λᾰκῐ́ς|λᾰκῐ́δος|form=F}}

====Derived terms====
{{col2|grc|λᾰκῐδόω|λᾰκῐ́ζω}}

===Further reading===
* {{R:grc:LSJ}}
* {{R:grc:Bailly}}
* {{R:grc:Beekes}}
###### %CE%BB%CE%B1%CF%80%CE%B1%CF%81%CF%8C%CF%82
==Ancient Greek==

===Etymology===
{{etymid|grc|id=slack}}
The formation is similar to {{m|grc|λαγαρός}}, {{m|grc|πλαδαρός}} and {{m|grc|χαλαρός}}. A basic primary verb may have been retained in {{m|grc|ἔλαψα||weakened, destroyed}}. It is usually assumed that {{m|grc|λαπάσσω}} is an extension of this, perhaps after {{m|grc|μαλάσσω||to make soft}}. In the sense ''to destroy'', {{m|grc|λαπάσσω}} agrees with {{m|grc|ἀλαπάζω||to destroy}}, suggesting a {{der|grc|qsb-grc|-}} origin in view of the prothetic vowel. Close to Albanian {{m|sq|laps}}.

===Pronunciation===
{{grc-IPA|λᾰπᾰρός}}

===Adjective===
{{grc-adj-1&2|head=λᾰπᾰρός|λᾰπᾰρᾱ́|λᾰπᾰρόν}}

# [[slack]], [[loose]] (of the bowels)
# [[hollow]]

====Inflection====
{{grc-adecl|λᾰπᾰρός|λᾰπᾰρᾱ́}}

====Derived terms====
{{col3|grc|λαπακτικός|λάπαξις|λαπάρα|λαπαρότης|λαπάσσω}}

===Further reading===
* {{R:grc:LSJ}}
* {{R:grc:Middle Liddell}}
* {{R:grc:Bailly}}
* {{R:grc:Beekes}}
###### lepos
==Latin==

===Alternative forms===
* {{alter|la|lepor}}

===Etymology===
From {{af|la||alt1=*lep-|-or|alt2=-ōs|pos2=suffix forming abstract nouns}}, related to the suffixed adjective {{m|la|lepidus|t=pleasant, charming}}. The origin of the root is {{unk|la|unknown}}. 

Based purely on form, it has been compared with {{noncog|grc|λεπτός}} and {{m|grc|λέπω|t=to peel}}, but because of the different meanings, this connection is uncertain and rejected by Ernout and Meillet 1985.<ref name="EM">{{R:la:EM|page=352}}</ref> De Vaan 2008 is skeptical, but suggests a change from "what has been peeled" to "refinement" is thinkable.<ref>{{R:itc:EDL|head=lepōs|page=335}}</ref>

[[w:Václav Machek (linguist)|Machek]] considers a connection with {{noncog|sla-pro|*lěpъ|t=beautiful}}.<ref>V. Machek. Graeco-slavica. LP 5, 1955, 69.</ref>

===Pronunciation===
* {{la-IPA|lepōs}}

===Noun===
{{la-noun|lepōs/lepōr<3>|g=m}}

# [[pleasantness]], [[charm]], [[attractiveness]], [[agreeableness]]
# [[politeness]], [[grace]]
# [[pleasantry]], [[wit]], [[humor]]
# {{q|term of endearment}} [[delight]]

====Declension====
{{la-ndecl|lepōs/lepōr<3>}}

====Related terms====
* {{l|la|lepidē}}
* {{l|la|lepidus}}

====Descendants====
* {{desc|it|lepore|bor=1}}

===References===
{{reflist}}

===Further reading===
* {{R:la:L&S}}
* {{R:la:Elementary Lewis}}
* {{R:la:Gaffiot}}
* {{R:la:M&A}}

{{cln|la|endearing terms}}
```


## [2026-09-06T23:16:06.885Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.sanskritdictionary.com/?q=laktaka",
 "prompt": "Give the Monier-Williams and Apte entries for laktaka (लक्तक): meanings such as 'rag, tattered garment' and 'lac'."
}
```


## [2026-09-06T23:16:07.647Z] TOOL CALL #40: WebSearch

```json
{
 "query": "Armenian լաթ latʿ \"rag, cloth\" etymology Acharyan Iranian loanword"
}
```


### [2026-09-06T23:16:09.054Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T23:16:16.839Z] TOOL RESULT

```
Web search results for query: "Armenian լաթ latʿ "rag, cloth" etymology Acharyan Iranian loanword"

Links: [{"title":"IRANIAN AND HITTITE-LUWIAN PARALLELS OF THE ARMENIAN WORDS TAPAST-'CARPET' AND TAPAST- 'A KIND OF DEADLY PAIN, DISEASE'","url":"https://zenodo.org/records/6540028"},{"title":"Armenian Textile Terminology - UNL Digital Commons","url":"https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1011&context=texterm"},{"title":"(PDF) Studies in Armenian Etymology (1-30)","url":"https://www.academia.edu/11812795/Studies_in_Armenian_Etymology_1_30_"},{"title":"20 words in Russian that surprisingly have Persian origins","url":"https://aspirantum.com/blog/persian-loan-words-in-russian"},{"title":"ARMENIA AND IRAN iv. Iranian influences in Armenian Language - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/armenia-iv/"},{"title":"Turkic loanwords in Armenian","url":"https://en.wikipedia.org/wiki/Turkic_loanwords_in_Armenian"},{"title":"STUDIES IN ARMENIAN ETYMOLOGY WITH SPECIAL EMPHASIS ON DIALECTS AND CULTURE","url":"https://vahagnakanch.wordpress.com/wp-content/uploads/2011/04/armenian-etymologies.pdf"},{"title":"dash.harvard.edu","url":"https://dash.harvard.edu/server/api/core/bitstreams/7312037d-1b9f-6bd4-e053-0100007fdf3b/content"},{"title":"Greek, Syriac and Iranian Loanwords in Ancient Armenian: Reflexes of Voiceless Stops in Word-Initial Position","url":"https://unimi.academia.edu/AndreaScala"}]

I've performed the web search for your query about the Armenian word "latʿ" (լաթ) meaning "rag, cloth" and its etymology according to Acharyan as an Iranian loanword. 

The search results provide information about Iranian loanwords in Armenian and Armenian etymology more broadly, though the specific etymology for the word "latʿ" was not directly found in these particular results. However, the results do confirm the general context:

According to Acharyan's etymological dictionary (1928-35), 4014 words in Armenian are registered as loanwords, mainly Iranian, and Armenian is characterized from the very beginning of its literary documentation by a large number of Iranian loanwords.

The search results show that Parthian was one of the source languages for many Armenian borrowings, which is relevant to understanding the Iranian loanword layers in Armenian.

If you're looking for more specific information about the etymology of "latʿ," you might want to consult Acharyan's etymological dictionary directly or specialized studies on Armenian textile terminology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T23:16:23.580Z] TOOL CALL #41: Bash

```json
{
 "command": "curl -s -H 'User-Agent: rishe-verify/1.0' \"https://en.wiktionary.org/w/api.php?action=query&list=search&srsearch=lat%CA%BF%20rag%20Armenian&format=json&srlimit=8\" | head -c 2000\necho; echo \"==== try լաթ page exists?\"\ncurl -s -o /dev/null -w \"%{http_code}\\n\" -H 'User-Agent: rishe-verify/1.0' \"https://en.wiktionary.org/wiki/%D5%AC%D5%A1%D5%A9\"\necho \"==== hy wiktionary\"\ncurl -s -H 'User-Agent: rishe-verify/1.0' \"https://hy.wiktionary.org/w/index.php?title=%D5%AC%D5%A1%D5%A9&action=raw\" | head -40"
}
```


## [2026-09-06T23:16:25.450Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.wisdomlib.org/definition/laktaka",
 "prompt": "Give the Sanskrit dictionary definitions of laktaka (लक्तक) — Monier-Williams / Apte / Shabda-Sagara entries, especially 'a rag, tattered garment' and 'lac / red dye'."
}
```


### [2026-09-06T23:16:26.404Z] TOOL RESULT

```
{"batchcomplete":"","query":{"searchinfo":{"totalhits":4},"search":[{"ns":0,"title":"rag","pageid":62433,"size":24378,"wordcount":2141,"snippet":"bull, red <span class=\"searchmatch\">rag</span> shag-<span class=\"searchmatch\">rag</span> shakerag shaving <span class=\"searchmatch\">rag</span> shitrag smell of an oily <span class=\"searchmatch\">rag</span> snotrag, snot <span class=\"searchmatch\">rag</span> stab-<span class=\"searchmatch\">rag</span> stone-<span class=\"searchmatch\">rag</span> tag and <span class=\"searchmatch\">rag</span> tag-<span class=\"searchmatch\">rag</span> toe <span class=\"searchmatch\">rag</span>, toe-<span class=\"searchmatch\">rag</span>, toerag","timestamp":"2026-08-24T03:19:38Z"},{"ns":0,"title":"\u0433\u043e\u0440\u0433\u0430\u043c","pageid":7040881,"size":1184,"wordcount":144,"snippet":"(germi). IPA(key): /\u02c8\u0261or\u0261am/ \u0433\u043e\u0440\u0433\u0430\u043c \u2022 (gorgam)\u00a0class jj floorcloth (dialectal) <span class=\"searchmatch\">rag</span> for cleaning the gun after lubrication Synonym: \u0447\u04cf\u0443\u0440\u0430\u043c (\u010d\u02bcuram) adjectives","timestamp":"2026-04-02T22:42:45Z"},{"ns":0,"title":"tag","pageid":54163,"size":28516,"wordcount":2932,"snippet":"these proteins. Something mean and paltry; the rabble, originally refer to <span class=\"searchmatch\">rag</span> as torn cloth. 1596 (date written; published 1633), Edmund Spenser, A Vewe","timestamp":"2026-09-04T22:15:03Z"},{"ns":0,"title":"baba","pageid":33484,"size":75823,"wordcount":10660,"snippet":"as a term for various family members: father: Albanian, Arabic, Western <span class=\"searchmatch\">Armenian</span>, Chinese, Hindi, Urdu, Punjabi, Bengali, Greek, Marathi, Marshallese, Mingrelian","timestamp":"2026-09-06T03:10:01Z"}]}}
==== try լաթ page exists?
404
==== hy wiktionary
{{-hy-}}
{{hy-pron}}
{{why|}}
{{վանկեր|լաթ}}
== Ստուգաբանություն ==
Փոխառություն՝ պարսկերեն lat:
{{-hy-գո-}}
# կտոր, կերպաս, գործված կտոր, կտավեղեն, շոր {{օրն|Մեկը {{ընդգծել|լաթ}} է, մեկը արդուկ։|ԵՉ}} {{օրն|Բառերն իրենց ձեռներուն մեջ այնքան արժեք ունին, որչափ {{ընդգծել|լաթին}} մը կտոր դերձակներու քով։|ՀՊ}}
# առանձնապեստ սպիտակեղենի կտոր, սպիտակեղեն {{օրն|Ճերմակ {{ընդգծել|լաթերով}} դաշտի մշակներ, եկեք ունկնդրել իմ երգիս|ՄՄ}}
# զգեստ, հագուստ {{օրն|Ես ալ տուն կերթամ {{ընդգծել|լաթ}} փոխելու։|ՀՊ}}
# շորի ծվեն, պատառ
# մաշված, պատառոտված զգեստ, ցնցոտի
# քուրջ, փոշելաթ, ջնջոց {{օրն|Թաց {{ընդգծել|լաթով}} մը սանդուղին առաջին աստիճանն սրբել սկսավ։|ՀՊ}}
# անկողին, տեղաշոր {{օրն|Խոր քուն եմ մտել աղտոտ {{ընդգծել|լաթերում}}։|ՇԿ}}
# կաշենման կտոր, որով երբեմն կազմում են գրքերը, պաստառում են դռները, սեղանների երեսները և այլն
# կոլենկոր
# {{փխբ}} կամազուրկ, անգործունյա մարդ, փալաս 
# {{նորբ}} շոր, փալաս  
==== Հոմանիշներ ====
# կտոր, կտավեղեն, կտավ
# զգեստ, հագուստ, շոր
# տե՛ս [[ծվեն]]
# տե՛ս [[ցնցոտի]]
# տե՛ս [[ջնջոց]], [[փոշելաթ]]
==== Արտահայտություններ ====

{{der-top}}
* [[լաթակազմ]]
* [[լաթահավաք]]
* [[լաթային]]
* [[լաթաշեն]]
* [[լաթապատ]]
* [[լաթապատել]]
* [[լաթապատվել]]
* [[լաթապատում]]
* [[լաթավաճառ]]
* [[լաթավոր]]
* [[լաթե]]
* [[լաթեղեն]]
* [[լաթերես]]
```


### [2026-09-06T23:16:32.262Z] TOOL RESULT

```
# Sanskrit Dictionary Definitions of Laktaka (लक्तक)

## Primary Meanings

**Monier-Williams Dictionary:**
The entry indicates laktaka means "a dirty and tattered cloth, a rag" and possibly "lac, the red dye."

**Apte's Practical Sanskrit-English Dictionary:**
This source provides two main definitions: "Lac" and "A tattered cloth, a rag."

**Shabda-Sagara Dictionary:**
According to this reference, laktaka denotes "Old and tattered cloth, a rag or rags" as well as "Lac, the dye."

## Summary

Across multiple authoritative Sanskrit lexicons, laktaka consistently refers to worn fabric scraps or pieces of cloth. The term also designates lac, the resinous substance used as a red colorant. The etymology traces to the verb root *lak* (to obtain), with grammatical affixes *kta* and *kan* appended.
```


## [2026-09-06T23:16:48.649Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v4 grep لخت\"; grep -n \"لخت\" incoming/BQT/BQT_v4_pages.txt | head -20\necho \"=== v4 grep لابه/لاف\"; grep -n \"لابه\\|سنگلاخ\\|دیولاخ\" incoming/BQT/BQT_v4_pages.txt | head -20\necho \"=== v3 grep سنگلاخ\"; grep -n \"سنگلاخ\" incoming/BQT/BQT_v3_pages.txt | head -10"
}
```


### [2026-09-06T23:16:48.725Z] TOOL RESULT

```
=== v4 grep لخت
1376:روشنایی ۰ آب وآتش نطهیرکننده که‌آنالر| بنام پنج مهرسیند با دکرده‌اند. آنگاه اسان لختین
1378:برخود بسته بود - شد. چون اسان لختین دشمن را زورمند دید » عناصر نورانی خویش را بدو
4656:مملخت ۲ » بنتح اول بروزن بدبخت, | و بلام زده » منع ازدرنکه دمودن وتأخی رکردن
4657:کفش و پای افزار باشد ؛ و باین معنی هملخت | باشد یمنی درلگه وتأخیرمکن » چه مول بممنی
4673:۴ - مسحف «فیلخت» (۸.م.) ۰ ۴ - هز. 38۳98 ۰ 2)1(۳88 ,38۳22
11403:جزه : لخت لی 8 جزئی ( پرفیکس » پیشاوند ) است بمعنی فرود و پایین که درسرلغات بهقتن
13480:بالوی جغرافی نوبسان عرب » 8136 - 101- 010 جینیان » لختین بار اط بطلمیوی آمده
14000:واو عطف را اصلی پنداشته‌اند.» ۸« رشیدی > رل : رت * روت * لفت‌نامه : لخت » * روده (۶م)
15296:لخت فری ص ۳۰۷
17193:خرد یافت لختی و شد کاروان هشیوار و با هنگه و بسیاردان.
17579:تاکران این زمین را ببخشیدند و بهفت بهر کردند , وهر بهری را یکی کشور خواندند : لختین
18509:‏۴ - « هملخت » چرم موزه وکفش پای افزاربود . کسائی (مروزی) کوید :
18513:‏وگرخلا فکنی طمع را وهم بروی بدرد ار بمثل آهنین بود هیلخت . >
18516:معرب کلمه « هیلخت » وجمع « هملختات » ( این کلمه دوبار درمقدسی آهده ) ولیز درتعریب
20708:واییب خلال باشد .> «لخت فری ص2۲۹ .۰
=== v4 grep لابه/لاف
4613:مثال كانبي از سنگلاخ وادی فقر ملنگه‌واربیابان (بپابان . دهغدا) برءاین‌طریق وملنکه.
15558:وآن کلابه‌ایست که بردیرارمالند و بربالای آن وق * - بنتح اول و ضم ثالی وسکون
=== v3 grep سنگلاخ
8350:۴ - سدرای‌سنگه روی و که سنگلاخ را
49742:‏نمك لاخ » دیولاخ , سنگلاخ , اهرمن لاخ ۰
```


## [2026-09-06T23:16:49.836Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%84%D8%A7%D8%A8%D9%87/",
 "prompt": "Give the Mo'in (فرهنگ معین) entry for لابه including any bracketed origin tag such as [په.] (Pahlavi), and the Dehkhoda gloss."
}
```


### [2026-09-06T23:16:55.514Z] TOOL RESULT

```
# Mo'in Entry for لابه

According to **Farhang-e Mo'in**, the entry reads:

"(بِ ) (اِ. ) ۱ - عجز، نیاز. ۲ - التماس ، زاری . ۳ - خودستایی ، تکبر."

This translates to three primary meanings: helplessness/need; supplication/lamentation; and self-praise/arrogance.

# Dehkhoda Glossary Entry

The Dehkhoda section provides an extensive classical treatment, defining لابه as supplication coupled with complete submission and sincerity. The entry emphasizes its use in Persian literature, particularly through numerous citations from Ferdowsi's works demonstrating contexts of entreaty, humility, and earnest pleading.
```


## [2026-09-06T23:17:01.243Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '49730,49760p' incoming/BQT/BQT_v3_pages.txt\necho \"--- page tag\"\nawk 'NR<=49742 && /\\[pdf page [0-9]+\\]/ {p=$0} END{print p}' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T23:17:03.105Z] TOOL RESULT

```
از ‎SIT ys‏ بر بالای هم گذارند۸ - ویممتی
دیبای نازل وتنك ولطیف وخوض قماش باشده ؛
و درعربی نیز همین معنی دارد ‎-٩*‏ و ‎Pale‏
‏میگویند وبعربی تراب ‎Waals‏ - ومخففلادن
‎Fou a‏ وآن نوعی از مشمومات است بعنی
بوی کردنیها - و نام شهر لار بوده است در قدییم
و درین زمان دال برا تبدیل یافته است ۱۴-وهر
کل و شکوفه را نیز کویند 9۴- وبمعنی] بادانی
هم آمده است که درمقابل خرابی است - وقلمه

‏را نیز گویند .

‏نمك لاخ » دیولاخ , سنگلاخ , اهرمن لاخ ۰

‏رود لاخ ‎ST.‏ لاخ , هندولاح » کلوغ لاخ و غیره پیوندد : « واین بحیرء ( پختگان ) ‎EVA‏

‏است. » « فارسنامه. این‌البلخی س ۱۵۳ ۰

‏۴ - درموارد دیگرهم آعده .)4 ‎Nee‏

‏. ورگ : دارمستتر . شبعات ج ۱ ص ۲۹۷ .

‎masse ‏لا کشت س لا کشه‎ m= P

‏لا که = لخشکه << الاخته «الطبیخ ص۷۹ »؛ نوعی رشته , رشته‌ای که لوزی برند . آش یکه

‏از ‎oT‏ پزند . رك ‎cab‏ نامه : لاخشه .

‏۴ هس لاخشته ‎(p.m)‏

‎. * ‏نامه‎ cab « ‏؛ که ازآن گل ولای خیزد‎ (os) ‏از: لا (لای) + خیز‎ O°
--- page tag
[pdf page 672]
```


## [2026-09-06T23:17:10.827Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps({k:d[k] for k in d if k in ('page_offset','lookup_hint','scans','local_file')},ensure_ascii=False,indent=1)[:2000])\""
}
```


### [2026-09-06T23:17:12.514Z] TOOL RESULT

```
{
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
  "/home/sfmqrb/git/rishe/data/verification/
```


## [2026-09-06T23:17:18.914Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\np='incoming/BQT/BQT_v3_pages.txt'\ntxt=open(p,encoding='utf-8',errors='replace').read().split('\\n')\npage=None\nfor i,l in enumerate(txt,1):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: page=m.group(1)\n    for w in ('لخت','لاف ','لابه','ولاف'):\n        if w in l:\n            print(page, i, l.strip()[:160])\n            break\nEOF"
}
```


### [2026-09-06T23:17:21.021Z] TOOL RESULT

```
31 2001 باشد لیکن برخلاف ‎old‏ .
50 3580 ‏شخشیدن ۴ = بروزن ومعنی‌لختیدن
79 5893 ‏شلخته - با اول و ثالی مفتوح وسکون
79 5900 شلخت بحذف‌ها نیز گفته اند و کاهی ازروی‌قپر
79 5925 ‏۴ - در تداول امروز «شلخته» شخص بد سلیقه ولاابالی را گویند .
81 6057 که کرسته ولافر باشد . و بعضی چاروای فربه
81 6064 وجای تنگ و تنگنا ‎ath‏ - وبمعنی لخت‌جامه
89 6699 است اختلاف در دال ورا شده است ۳ .
92 6973 ‏در غلاف طولالی دراز منکون شود ‎OT,‏ غلاف را
102 7832 هم هت - وبمعنی لخت جامه عنی بك توپ
122 9363 ‏‘ - روزلخت چون‌دمرندی زدیم رمشق
140 10524 واين نام را درسکه‌های امپهبدان (اخلاف ‎Gy srl (GULL‏ پهلوی وهمچنین درمسکوکات حکام
158 11755 ودمیدن ضی صورت گیرد . دربارة ابدال اين حرف » ‎By‏ : لخت نامه.
174 12853 ‏۱ - جمع علوی » موب به «علو» (مثلثه) بالای خاله » خلاف سفل « منتهی‌الارب ‎٩‏
202 14462 ‏حوضها وته تالابها وجویها میباشد .
202 14467 آن بدشواری بر آید - و لختك را نیز گوند
202 14474 ‏بائد که در بن و ته حرضها وتالابها میباشد .
209 14925 کاری باشد بر خلاف مراد و توقع .
210 15079 فارسی اختلاف دارند - تکلم کنند « داثةالمعارف اسلام : افغانستان . طبع فراسوی‌ج۱ ‎Never‏
212 15193 که در ته حوضها و جویها و تالابها بهم رسد
219 15742 Veg ‏غلاف پنبهراگویند که هنوز .با‎
220 15791 که ‎oh‏ درخت پنبه و غلاف پنبه است ‎JN‏
227 16345 ‏مزروع شود برخلاف زمین دیمه که پاآب باران
238 17241 نظامی گتجوی ( لت نامه : لاف زدن ).
244 17709 ‏معجزه و اعجاز باشد » و اعجاز خلاف عادتی‌است
261 18872 ف ‎Galt‏ * - درین لت خلاف است.
288 20871 . ‏میکند و لاف میزند‎
288 20887 بروزن سلیمان, بمعنی قخر وتفاخر ولافو کزاف
288 20891 ‎ow‏ فقاع گشودن است که کنابه از لاف زدن
290 21033 ‏قالان ‎abe OWS‏ ازلاف ‎GS,‏
293 21355 سرخ و طمش تلغ و نباش ‎mh‏ ذرمی و بر کش مثل بر که ‎tb‏ وکلش سفید و غلاف ‎shee‏
324 23548 و ‎alt‏ بالف کشیده و ‎lly‏ حطی زدء » بلخت
341 24885 احتباس غیر طبیمی حاصل شود و درد آرد وگاه قوی کردد و بکقد بخلاف صداع «بحرالجواهر»
349 25377 وکردنی هرت ۸ - وشیشةٌ صلابه کرده را نیز
350 25452 کاشی است» وآن سفالی باشد که شبشةٌ صلابه
364 26564 ولاف است چه از کاف مراد گزاف و ازلام لاف
376 27380 ‏از لاف زدن 6 وحکایت وسخنان گذشته گفتن وبر
385 28064 کنند نافم است و بسن ی ‎ain ST‏ بلخت سریالی‌نام
421 30890 ‏هم مهچة لوای ترا آسمان غلاف هم تشکر علو تر" لامکانکرنگه .
428 31422 حرف‌الدال ( ای باب‌الاف فی‌اولالکلمة وحرف‌الدال فیآخرها ) آورد» است وبرهان فاطع نیز
443 32503 واين برخلاف آونکگ است ۴ .
453 33256 از چند روز از غلاف بر میآید و ‎AT‏ بعریی
459 33704 ‎٩‏ -«کلابه , چرخه‌ای
459 33706 ‏زلی را بشکند میخ کلابه . »
462 33895 ‎OWT‏ ۵ - بر وزن و ممنی کلابه
464 34090 ‏۴ -ظ. مسحف:« کلاو» = کلاو . 8 _قی: کلالاموش. ۲ ۶ کلابه < کلافه(«م.) .
476 34912 شده - ولختهای ‎yes‏ افتاده و خاك برهم‌چبیدء
488 35877 کمریا ‎٩‏ .بر وزن ‎Ll‏ . بلخت ‎wz‏
501 36901 زهر جوی"شهر آب دروی بتلخت .
529 38767 آ ترا که بامکویو کلابه‌بودشمار بربط کجا شناسدوچنگ وچفانهرا.»
535 39159 و غلاف پنبه را کوبند - و کوکنار که غلاف
536 39207 کوشواره , حسه و پاره ولختی از کوه را کویند
558 40877 برکی دیگراطلاق نکنند برخلاف خدایگان.
561 41078 ‎SUP‏ = بروزن و منی لاف است که
571 41843 ‎(PMs aw‏ عربیوبهمان‌معنی» ودرتر کیه‌نیزه کور» کوبند, و آن‌اصلابه‌منی مطلق مشرلوبیرون‌از
577 42182 پپنی باشد که در غلاف کنند و همراه داشته
588 43088 نوشته مبشد (برخلاف قول رشید یکهگوید کاغذ مریست ) :
594 43491 وبمعنیلاف و ‎GIS‏ لیز آمده‌است- واسیر و ‎HIS‏
594 43508 و کنابه ولاف زدن وسرزش کردن و ‎PEAS‏
607 44613 گز اف ۴ ‎Ge‏ اول ‎Oia»‏ خلاف »
620 45550 نیز کنته‌اند اما برخلاف قیاس است ‎٩‏ .
650 48114 ‏نقطه‌دار » غوزه و غلاف پنبه رااگویند و معرب‎
651 48151 نوشخند ۰ سخنان لاف ‎jy,‏ ودرو غ‌را گویند.
651 48187 خای نقطمدار , غلاف گل خرما راگویند.
655 48509 و ‎OT‏ غلاف مروارید ‎ol‏ - و پیاله ای را نیز
667 49455 نام ناحیتی صورت ۷8۲612 آمده و خاورشناسان در ‎usd‏ محل ‎OT‏ اختلاف دارند . طبق سنت
670 49623 +۷ (طبقه) . ۴ « لاف ‎gal.‏ ع 1818. 18۳۵(خودستابی ۰ ‎SY) fuk ۰ GG‏
670 49627 © - تواورا کنیلابه فردا به پیش فدا داری او را تن و جان خوش .
671 49649 ‏انگفتر سازند و صلابه کرده بجپت مذهبان
671 49672 ‎٩‏ - بلابه گت شبی میرمجلی نو شوم شنم برغبت خوبشش کمین غلام وشد .
671 49674 ۴ از : لاب ( لابه )-یدن ( پسوند مصدری ) ؛ لابه کردن :
671 49679 ۵ قاری : لابه ‎(Henning , A list of Middle Persian ... , 8505 , IX,‏
673 49865 ‎gy ‏رك: لابه‎ ٩
675 49966 لختر ‎Jy‏ ( 126087101 ) و قد ‏ کرناها من اصناف البتوع .» در بسض نخ ‎ate‏ ابن الببطار
675 49972 - ابا ز بیم زبانم لژ دکشته ‎Slay‏ کجا شد آنیمه دعوی و لاف وآنهمه ژاژ ؟
678 50131 ‏کنند ۴ - وبمعنی لاف و کزان هم کفته‌اند9 -
678 50138 و بمعنی لاف وکزاف هم بنظر آمده است ۸ .
678 50144 و گزاف و دروغ باشد ‎٩‏ - و چایلوی و لابه
678 50167 ‏که با لام سبه پوشان ‎als‏ لاف و لامانی :
680 50292 کهآ را کلابه سازند وخانه را بدان‌سفی دکنند ۵
680 50333 راکه ‎oT,‏ زد مقلاة خوانند ۱ - و بععنی‌لابه
680 50341 لاف لگ - بر وزن
680 50352 ۷ ح لاور س لابه ص لاپ :
683 50517 و جمم لب همهت که لبپا باشد برخلاف قیای.
684 50593 سخن و کفتگویلاف و گزاف ‎ath‏ واشاره‌بشاعی
686 50726 ‎a‏ « لت لت » بمنی‌پاره ‎gh‏ ولخت لخت ‎٩‏
686 50766 قرشت , بممنی لخت لخت و پاره ‎Push ob‏ .
687 50832 وکولابها و جوبهای ‎OT‏ می باشد ۸ - و بلفت
687 50861 پیش دست تو مگر لاف سضا زد » ورله ‎pluie gene bn‏
688 50920 است همچو لخت کوء ولخت جکر یعنی ‎hake‏
688 50928 ‏۴ -قس : 6 . لخت .
688 50943 ‏دساتیر ص ۲۹۵ » وجبع ‎OT‏ لختان ‎Cpe)‏ ور 4 : لختیها .
689 50946 لختان
689 50954 لخقان ۴ بروزن بخدان, جمم‌لخت
689 50957 لخت دود ‎pine‏ لاخه دوز است
689 50961 why ‏لخت‎ gine ‏بروزن تخته؛‎ = Gad
689 50991 و لوغی از آش آرد هم همست که ‎Lil‏ لختك
689 51010 ‏از تشگدلی جامه کند لخته و پاره.
689 51017 ‏لختیآسمانها . ۹ لنج
689 51020 ‏: لخته شدن خون و غیره » بستن ودلمه ‎Tyas‏
689 51021 ‏۵ -جمع > لختی » برساختة دساتیر . ره ‎Kaa gs‏
689 51025 ‎۰ ‏لخت‎ :
689 51036 ‎(pm) ‏لخته‎ 4
691 51128 کل و لای تیره و ‎le‏ را کویند که درته‌حوضها | کل سیاء ته حوضها و ‎GY‏ بن تالابها باشد #
692 51152 و ماه است که در ته تالابها و بن حوضها بهم و بمعنی شبتم هم‌آمده است و ‎OT‏ رطوبتی باشد
```


## [2026-09-06T23:17:30.225Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== لاف p.670\"; sed -n '49610,49635p' incoming/BQT/BQT_v3_pages.txt\necho; echo \"=== لابه p.671\"; sed -n '49660,49685p' incoming/BQT/BQT_v3_pages.txt\necho; echo \"=== لخت p.688-689\"; sed -n '50900,50945p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T23:17:30.302Z] TOOL RESULT

```
=== لاف p.670
بسن اسطر است » و اسطر نم پادشاهی بوده از

لا ۴ 2 بروزن تابه. بمعنی سخن‌باند

- و اظهار اخلاس با نیاز تمام را کویند- وبمعنی
چرب زبانی و چاپلوسی و تملق و ‎ID‏ وعجز

و یاز و خواهش هم‌هست ۵ - و فریب و بازی
۵ ل ( لام ) - حرف بیست و هفتم از الفبای فارسی وحرف بیست وسوم آزالفبای عربی
‎(on!)‏ و در حاب جمل ‎onl Soe WIT‏ حرف به «ر * ( رلك : ص بط مقدمهةٌ ملف )

بدل شود. ۱ ۰۷۰ اسم فاعل مرخم ‎col‏ در کلمات مر کب: ‎Vege‏ ژاژلا. رك:لاییدن.
۳ _ فقه‌اللَةٌ عامیانه. رك : اسطرلاب . ۴ - از: لا (طبغه) ‎H‏ بر(بمعنی‌علی‌عربی)
+۷ (طبقه) . ۴ « لاف ‎gal.‏ ع 1818. 18۳۵(خودستابی ۰ ‎SY) fuk ۰ GG‏

زن ) ) از ‎our‏ 120 ۵ . رك : هوبشمان ‎Mov‏ و رك : اسشق ‎tat‏ : کردی 1260
( استدعا « درخواست ) « ژابا س ۳۷۵ » ورك : لابیدن .
© - تواورا کنیلابه فردا به پیش فدا داری او را تن و جان خوش .
فردوسی طوسی « لفت نامه > .
[pdf page 671]
" لایدن - ۱۸۷5
دادن را هم میگویند ۱ - و چیزی ‎jth‏ گویند
که از سر تا بیای چیزی به پیچند .

لا بیفن ۲ ه بروزن و معنی لافیدن(۱)
است که سخنان زیاده از حد خودگفتن باشد -

=== لابه p.671
‏لاچور دنه خم یمعنی لاجوردی
سقف است که کنابه ازآسمان باشد .

‎ge‏ ۷ - بر وزن کاچی , قاقله باشد
‎Je WT,‏ وهیل نیز گوبند و داخل ادوبهُ حاره
در طعامکنند.

‎EY‏ « بروزن ‎Gale ch‏ رشوت است
- و بمعنی برهنه و عربان باشد ‏ - وسگه‌عاده
را یز کویند ۵ ۱
لاچ ‎be‏ جیم فارسی» بمعنی‌بازی وفریب
() چش : لایدن .
‎٩‏ - بلابه گت شبی میرمجلی نو شوم شنم برغبت خوبشش کمین غلام وشد .
‎bile «‏ شیرازی صس ۱۱ > .
۴ از : لاب ( لابه )-یدن ( پسوند مصدری ) ؛ لابه کردن :
بدار دیا چون برفروخت ‎ST‏ ظلم سکار آن بجهنم همی‌خورد چو ظلیم
چوخون ورب بپالوده خیره از مردم بدوزخ اندرلاید که‌خون‌دهندش وریم.
سوزنی سمرقندی ۶ لفت نامه *.
دراوراق مانوی ( پارنی ) ‎PB‏ ( نامیدن . دعاکردن 1 درخواست کردن ‎ )‏ پارسی ‎she‏ (پهلوی)
۵ قاری : لابه ‎(Henning , A list of Middle Persian ... , 8505 , IX,‏
‎ae .) 1, ۲ 4‏ 167-800 , سریکلی ‎lew_am‏ (گفتگ و کردن + سخ نکفتن ) « اسشق

‏۲
‏۴ - دست و زبان بدو ترسد کس را آری بماه بر نرسد لاتو .
فرخی سیستالی « لفت ‎fab‏
‏۴ - بر سرلور عشق بینی تاج ابر آن دم که عشق بینی لاج .

=== لخت p.688-689

‎FA‏ نم اول و سکون ‎ot‏ «بمعنی
کخ ‎OT, col‏ علفی باشد که درآب رومد 5559
دارد ‎OT mys‏ مانتدپشم چیزی جمع شدم آنرا
داخل آهك رسیده کنند و در حوضها ‎Ke‏ برد
و از ‎oT‏ علف حصیر بافند و در خراسان با آن
خریزه ‎GT‏ کنند و در هتدوستان بخورد فیل
‎«ian‏

‎pe - Pld‏ اول بروزن سضا ۰ کف

‏و کنایت
و ‎ch‏ افزار وسرموزه را کوبند .

‎OS‏ بروزن سخت » بمعنی ز باشد
که بعربی عمود کوبند ۴ - و کلاه خود آهنین
را 55 گفته‌اند - و بمعنی بال و کوپال هم‌آمده
است - وکفش و پای افزار وموزه و سرموزه را
یز کوبند 6 - و بمعنی ‎IT‏ وشلاق هم‌هست -
و بمعنی پارچه و حصه وبرخ و جزو ۱ و پاره
است همچو لخت کوء ولخت جکر یعنی ‎hake‏

‏۱ - بقتح اول و دوم مخفف ( و یز مشدد ) > ‎cad‏ نامه » .

‏۴ - لوخ رخ روخ (هم.) :
کفت یکه بترسد زهمه خلق سنائی
آن مست زمستی‌بنترسد له زمردی

‏۴ -قس : 6 . لخت .

‏۴ - چو ‎gal‏ شد از دشمن و ناج و تخت

‎vd: ‏رك‎  *

‏پاسخ شنو ارچند ‎cle‏ در خور ‎Gok‏
‏ورنه بخرد یز خطی شمرد لح -
‎Si?‏ غزلوی ص ۷۷۱ *

‏بکژی ‎cad the‏ ب رکشت بخت .
فردوسی طوسی « لفت نامه >

‎aw - 1‏ > < جزو » مقابل کل برساختة دسانیراست « فرهنگه

‏دساتیر ص ۲۹۵ » وجبع ‎OT‏ لختان ‎Cpe)‏ ور 4 : لختیها .
۰ لحیتای - ,4 : ‎old‏ متفرقة پایان ‎AT‏
[pdf page 689]
```


## [2026-09-06T23:17:49.115Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB Schmeichelei/Prahler\"; grep -n -i \"Schmeichelei\\|Prahlerei\" HUB.txt | head -10\necho \"=== CHEUNG lab\"; grep -n -i \"\\*lab\\|lābīdan\\|labidan\" CHEUNG.txt | head -10\necho \"=== PHD lab/lābag\"; grep -n -i \"l)p\\|lab\\b\\|lābag\" PHD.txt | head -20\necho \"=== NYB lab\"; grep -n -i \"lʾp\\|lab \\|lābak\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-06T23:17:49.195Z] TOOL RESULT

```
=== HUB Schmeichelei/Prahler
6215:lava = Idba *Schmeichelei' H. 952 ; tdv = tdb 'Glanz, Hitze,
6312:*Prahlerei' (H. 952, oben p. 96) neben lava^ laba 'Schmeichelei*
6544:s. p. 184, laf Trahlerei', wenn es zu laba, lava *Schmeichelei*
=== CHEUNG lab
=== PHD lab/lābag
164:abarmān [5/mn'] in charge. abarmānd ['pín?nd] inheritance, privilege. abarmānīģ [%n?nyk!] noble. abar-menišn Pf/myn$n'!] proud, haughty. abarón Pf*/xwn! | N wárün] contrary, wrong, sinful. ~ih: sin. abar-6z PóPeoc] stronger. ~ih: mastery. abar-tan [Pltn'] arrogant. ~th: arrogance. abarwēz Pfltvyc | (M *bruyj, N parwéz)] triumphant, victorious. ~ih: triumph, victory. abarzén, v. zmašk, abaxs [hš] repentant; regret. ~ЛЬ : repentance. abaxšāwand [5hP^wnd] regretful. abaxšāyīdan, abaxšāy- [5APd-ytn! | М ?bxPy-, N baxšūdan, baxšāy-) forgive, have mercy on. ~išn: mercy, forgiveness. ~i&nig : forgiving, merciful. labāxtar [*5?*4tl | M 7b’xtr] planet. žabāxtar [PP’htl | (N bāxtar ‘west’)] north. abaydag Pyrťk', v. paydag | M ?byd?g] invisible. ~th: invisibility. abày- : abayéd ['yt' | M Maud, N bāyad] it is necessary, fitting; must (+ infinitive). ~ist Pf?dst' | N bāyist] it was necessary. ~istan [?P?dstn!] be necessary, fitting; desire, want. ~išn: necessity. ~išnīg : necessary, fitting, seemly. abāz [L AWHL < A lI2(w)hr;?Pc | М Рс, N baz, wa] back, again, re-. ~ айдап б: attribute, ascribe to. 7 appoint t= ~ dāštan: withhold, restrain, prevent. ~ ēstādan az: abandon, desist from. — kardan: open. — kardan az: disengage from, wean. ~ mándan: remain behind. ~ pádan: remain, stay. — raftan : issue, go forth. ~ waštan O: turn into, become. ~ wirāstan: rearrange. abāzsār [LAWHLs'I] rebellious. ~ih: rebellion. āb-čihrag [$ cyhlk'] holding the seed, essence of water. abd [>24 | М "Gd J ?bd-] wonderful. ~ sahistan: seem wonderful (to) > marvel.
402:ILY, ZY- < À zy | M ‘y(g), N i] relative pronoun, who, which; connective particle. -idan [-ytn! | M -ydn, N ~] suffix forming secondary infinitives. -16 [-yk! | M -yg, N -i] suffix forming adjectives of relation, etc. -ih Lab | M ab, -yy, N -i] suffix forming abstract nouns. -īhā [-y/? | = M, N -hà] suffix forming adverbs; later, plurals. -Ih-istan [-yh-stn' | M -y%-ystn) suffixes forming passive and intrangitive denominative verbs. im [LZNE < A l-znh;?m | M ‘ym, N ~] this. ~ Cim ray: for this reason. ^ rÓz : today.
431:lab [lp | M lb, N ~] lip. labag [Pk | (M ? b), P РЬ, N laba] supplication. lābakkar [Pfkkl] suppliant.
2643:lip lab.
4914:lab «rubāy- lipī, rabih rapihwin
=== NYB lab
4633:A-H III = Mitteliranische Manichaica aus Chinesisch-Turkestan III. Von F.C. Andreas(f) aus dem NachlaB herausgegeben von Dr. W. Henning in Berlin. Sitzungsberichte ete., Phil.-hist. Kl. 1934, XXVII, pp. 848-911.
```


## [2026-09-06T23:17:56.131Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6305,6320p' HUB.txt; echo \"-----\"; sed -n '6538,6552p' HUB.txt; echo \"----- 6210\"; sed -n '6210,6220p' HUB.txt"
}
```


### [2026-09-06T23:17:56.189Z] TOOL RESULT

```
np. sag gegen medisch spaka- {andyt-u bei Hero dot), ka§.
esbdf espd, semn. esbe, g. saba, zd. spa (nom. sg.), afgh. spai.
Fiir 6; v aus p erscheint unregelmassig / in kasaf
*Schildkr5te' neben kaSav (bei Vullers) = zd. kasyapa-y
afgh. kasap ; fdm *Schuld* = vam s. § 66 ; afranjan = avran-
jan = abratijan §72; afdum letzter (fiir afdum, oben p. 8)
= paz. awadum, phi. *ap'tum^ ap. *apatama? Vgl. auch laf
*Prahlerei' (H. 952, oben p. 96) neben lava^ laba 'Schmeichelei*
(afgh. laf a und Idpa boasting')?
Ueber die Lautgruppen urspr. p + nty n^ r, ^, s u. s. w.
siehe unter m, n, /.
') Ueber asb siehe Blochmann, JASB. XXXYII, 1, 54.— 179 —
§ 72. Im Armenischen erscheint regelmassig p fur
ap. phi. p:
Aparasxarh (EliSe) = Aprsahr (Sebeos) = np.
AbarSahr (NSldeke, Alexanderroman 15, s. oben § 22);
-----
kaf *Spalt* von iran. kaf = kaph neben gr. xdnsTog, ksl.
kopati.
Wo indessen / fiir urspr. p oder bh nur im Np. be-
zeugt ist, wie in den zuletzt genannten WSrtern, bleibt noch
zu untersuchen , ob dieses / nicht secundar im Np. ent-
standen sein kann ^). So bei guSof 'dissipatio* neben *gic§db,
s. p. 184, laf Trahlerei', wenn es zu laba, lava *Schmeichelei*
gehOrt etc.
Vgl. auch kasaf 'SchildkrSte* = zd. kasyapa- (§ 71).
Dunkel ist das Verhaltniss von np. farr 'Glanz, Maje-
stat* == ap. farnah' (in VindafarnO) zu dem gleichbedeuten-
den np. xurrah = zd. xwarenah- (s. oben p. 83).
§ 81. Ap. / vor t^ 5, s, r (= idg. p) ist immer =
np. /: haft *sieben' = zd. hapta, iran. *hafta, u. s. w. ;
tafsldan *heiss werden*, zd. tafsaf, lat. tepesco, u. s. w.; dirafs
----- 6210
vdda 'Enkel' neben nabasa (oben p. 103) und nablra, ap.
*7}apdt', nom. napd; nivistan — nibistan (JRAS. 1894, p. 430)
*schreiben', ap. nipistanaii/; kdbln *Mitgift* = kdvm JRAS.
1894, p. 479, arm. kapen-U 'Lohn (der Hure); dvard *Kampf,
navard = nabard 'Kampf, phi. n(i)part Gl. and Ind. 233;
lava = Idba *Schmeichelei' H. 952 ; tdv = tdb 'Glanz, Hitze,
Zorn, Qual* H. 372; tdva = tdba *Pfanne*, phi. tdpak; ta-
vidan — tdbldan *drehen, spinnen' H. 372, vgl. oben p. 46 ;
tavar — tabar *Beir, arm. tapar; rev *Betrug, List': Jir^
*Betrug\ firevdmdan *to seduce* JRAS. 1894, p. 478, skr. rip:
-vdn = 'ban liiitend' = phi. -pdn, z. B. stiturvdn 'Kameel-
```


## [2026-09-06T23:18:38.118Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg309.png')\nprint(im.size)\nim.crop((330,540,900,660)).resize((1710,360)).save('crop_gs.png')\n\""
}
```


### [2026-09-06T23:18:40.170Z] TOOL RESULT

```
(1700, 2200)
```


## [2026-09-06T23:18:42.521Z] TOOL CALL #52: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_gs.png"
}
```


### [2026-09-06T23:18:42.549Z] TOOL RESULT

```

```


## [2026-09-06T23:18:58.424Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D9%84%D8%AE%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%D9%84%D8%A7%D9%81\" \\\n \"https://en.wiktionary.org/wiki/%D9%84%D8%A7%D8%A8%D9%87\" \\\n \"https://en.wiktionary.org/wiki/lacer\" \\\n \"https://en.wiktionary.org/wiki/%CE%BB%CE%B1%CE%BA%CE%AF%CF%82\" \\\n \"https://en.wiktionary.org/wiki/%CE%BB%CE%B1%CF%80%CE%B1%CF%81%CF%8C%CF%82\" \\\n \"https://en.wiktionary.org/wiki/lepos\" \\\n \"https://en.wiktionary.org/wiki/leer\" \\\n \"https://hy.wiktionary.org/wiki/%D5%AC%D5%A1%D5%A9\" \\\n \"https://www.etymonline.com/word/lacerate\" \\\n \"https://www.vajehyab.com/dehkhoda/%D9%84%D8%A7%D8%AE\" \\\n \"https://abadis.ir/fatofa/%D9%84%D8%AE%D8%AA/\" \\\n \"https://abadis.ir/fatofa/%D9%84%D8%A7%D8%A8%D9%87/\" \\\n \"https://www.wisdomlib.org/definition/laktaka\" \\\n ; do python3 tools/fetch_source.py \"$u\" --note \"page 309 (book 279), roots Lek/Lep/Les: verification of laxt, lat, lacer, lakis, laktaka, laf/labe, lepos, laparos, gi-lari, -lax\" 2>&1 | tail -2; done"
}
```


### [2026-09-06T23:19:09.118Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/57265db911436a17.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/77a210b344782a6f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/544a3cce37d69654.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d8eaa91a4157fc4a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bfc98b40372defed.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bfec2ce5d8d0a207.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2736110b3846f382.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d9e5865695af5d0b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0894ddafa3cb6612.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ab00cff15b7daa85.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/65d405ca87356ad3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/49d6cf2e194bb384.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eda8172e505bfddd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b07c775e391bcb38.txt
```


## [2026-09-06T23:19:12.094Z] TOOL CALL #54: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T23:19:12.140Z] TOOL RESULT

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


## [2026-09-06T23:19:20.259Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nls\npython3 - <<'EOF'\nimport re\np='WLD_Bd2_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npg=None\nhits=[]\nfor i,l in enumerate(lines,1):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: pg=m.group(1)\n    if re.search(r'lakis|Aaxi|lacer|laktaka', l):\n        hits.append((pg,i,l.strip()[:200]))\nfor h in hits[:25]: print(h)\nEOF"
}
```


### [2026-09-06T23:19:22.132Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
(None, 5829, 'ahd. frao, fro, fratver „strenuus, alacer (GI); froh“, wovon ahd. frottwen,')
(None, 14054, '„flammen, gluhen“, ags. blceceryi, blacern „Leuchter“ aisl. blakra „blinken“;')
(None, 25709, 'lacertus usw.         —')
(None, 27845, 'lat.        lacer,     -era,    -enim    ,,zerfetzt,               zerrissen,          zerfieischt,      korperlich      ver-')
(None, 27849, '160.   liber das von Pick II" 238 mit lacerna vgl. air. leine „Hemd‘\', s. u.')
(None, 27865, "laktaka- m. „Lappen'‘ (Preliwitz^ 258) widerspricht im Ablaut.")
(None, 27899, 'hansson IF. 8, 164, formell ahnlich mit lat. lacertus^ gr. hxeQilCav; Bed.')
(None, 27920, 'lat. lacertiis^ meist           PL „die Muskeln, bes. der Oberarm“, lacerta „Eidechse“')
(None, 27926, '349 als „strafF, muskulos^^, an der  Zugehorigkeit    von   lacerta  wie auch von')
(None, 27978, '95 f., KZ. 40, 264 f. 41, 396, Yf. LEWb.^ u. lacertus.')
(None, 28399, 'n. fil. 24, 300, KG. I 381, 1121; wegen bret. les nicht als Hegsa zu lacer-')
(None, 29764, 'doch zweifelnd). Dagegen stammeo ir. sdi (gl. lacerna^ tunica)^ cymr. sae,')
(None, 44337, 'leicht abg. prgziti^ prqzati „lacerare" (Persson Beitr. 869, doch in Yerb. ra.')
```


## [2026-09-06T23:19:24.842Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '27838,27875p' WLD_Bd2_pages.txt"
}
```


### [2026-09-06T23:19:24.890Z] TOOL RESULT

```
leq-     :    loq- „zerrei6en”         (iil-'t       s.    u.k
   Gr. kayJg „Fetzen'', kdxog                        n. ds. {?Ay}]          '
                                                                                Qdx}],        Kogzeg Hes.), laxl^oj „zer-
rei8e“, djiiXyxa' djiiggcoya. Kvjigiot Hes,;
   lat.        lacer,     -era,    -enim    ,,zerfetzt,               zerrissen,          zerfieischt,      korperlich      ver-
                                   Uberwurf, lacinia ,,Zipfel, Besatz oder
stiimmelt*', lacefna ..mantelartiger
Pransen am Kleid, limbus; Teilc von Herden, Ackern u. dgl'' (Curtius^
160.   liber das von Pick II" 238 mit lacerna vgl. air. leine „Hemd‘', s. u.
lino- „Lein‘0'       (Jokl SBAk. Wien 168, I 46 Anm. 1) Vahur ,,nackt-‘,
Vekure^ Vikure j,Pell, Leder, Baumrinde, Schote'l
420                                   leq-   ( :   ieq-), leq- : leq-



   Die von Solmsen KZ. 37, 580 f. als *laq-s- (: Xdxog n.) angereihte slav.
Sippe von klruss. inch, iacha „luinpiges, zerfetztes Kleid“, poln. tach^ tach-
man „ Lumpen, Lappen“, mss. lachom „Lappen, Fetzen*‘, Idchma „Luinpen‘*
u. dgh (wofiir Berneker 685 f. noch eher Yerdrangung von                  *lak-
durch die Kurzformbildung *lof:hr. Hack- erwagen mochte), ist weit wahr-
scheinlicher (s. Berneker aaO.) mit mnd, Jas „keilf6riniger Lappen“, dan.
norw. Zas, lase „Lumpen'‘, mhd. lasche „Lappen, Lasche“ zu verbinden.
   Jedenfalis fernzuhalten ist abg. Iqcq^ -iti „trennen“ (Fick     531), da zu
"^Itnq- „biegen“ (Berneker 738, v. d. Osten-Saeken IF. 33, 220 f.).         Ai.         —
laktaka- m. „Lappen'‘ (Preliwitz^ 258) widerspricht im Ablaut.
   TJrsprgl. Anl. ul-^ so da6 uleq-, 'f^kq- Erw. zu nel „brechen, rei6en“ (Ya-
nicek 268 fiF., Johansson Beitr. 71 f) ist nur denkbar, wenn mir. len „Wunde‘^
{*lakno-l Fick II 244) femzubalten ist (iiber dl-leg- j.vernichten^ ibd., s.
vielmehr u. leg- „tr6pfeln“). Andrerseits suchen Kluge Wb.® u. Schlag,
Hirt Abl. 91 Yerbindung mit got. slahan usw. j,schlagen“, der Bedeutungs-
farbung wenig entsprechend.


leq-     (:       und leq- leq- in Worten fiir „Gliedma6en“ und fur „lebhaft
              leq-)             :
```


## [2026-09-06T23:19:34.849Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\ngrep -n \"lapar\\|lepos\\|Xarcaqog\\|laf \\|laba\" WLD_Bd2_pages.txt | sed -n '1,30p'\necho \"=== find leq/lep page 429/430 area\"\ngrep -n \"^430\\|^429\\|^431\" WLD_Bd2_pages.txt | head"
}
```


### [2026-09-06T23:19:34.910Z] TOOL RESULT

```
24812:murmeP, kakdCco, kakayeco ,,schwatze“, lat. lallo, -are „in den Schlaf singenA
24816:Schlaf lullen*'.
24817:  Ahnliche Lallworte fiir „in den Schlaf singen, einlullen, einwiegen,
24821:hdut „Yerwohnen‘*, nhd. hdlen, engl. lull „in den Schlaf singen‘‘, ai. lolntl
24830:       lett. lelut^ Iclut ^Kinder in den Schlaf wiegen'^, lelis „schlafFer, un-
25305:384                           laba^(u)g-, -ug-   ;   laba^(u)g-, -ug-
26735:got. liiba f., aisL leif^ ahd. leipa^ ags. laf „tJberbieibser'; got.
28543:    Lat. lepidus „zierlich, niedlich, allerliebst (vgl. oben XsTixog)^ lepos jjFein-
28752:                                        zunachst von holl. laf „matt, schlaff,
28763:ahd. slaf m. nhd. „Schldfe“; mnd. ndl. slap „schlaff", ahd. slaf (“^-), nhd.
37704:   lit.-zem. paTctrsti^        Praet. paVirdo „aus          dem    Schlaf auffahren" (Zupitza
41858:miegis „Schlaf auf dem Bauch, mit in die Hohe gestrecktem Hintern*^, tur-
47429:bei labare „wanken'‘ usw. (AYz. leb-) ebenso wie lat. Idbes, das Curtius 369
=== find leq/lep page 429/430 area
16088:430 Fick BB. 6, 213, Wb. I^ 510.
29911:431; Palk-Torp 941 f.). tTber sap-no vgl. unten.
33030:430,   Falk-Torp  u. sind (Lit. iiber unhaltbare Kombinationen), Yf.            b.-                                        LEY
```


## [2026-09-06T23:19:38.638Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '28510,28560p' WLD_Bd2_pages.txt\necho \"===== search lap-aro\"\ngrep -n \"Xanaqog\\|kanagog\\|lapdssein\\|lapass\" WLD_Bd2_pages.txt | head"
}
```


### [2026-09-06T23:19:38.701Z] TOOL RESULT

```
kaniCco „benehme mich ubermiitig^', Xamox'gg „Aufschneider, Prahler‘‘ (deren
Verb, mit lepiiS „ubermutig, verwohnt^, lepduti „ubermutig sein“, lepinti
^,verzarteln“, leti. lep^is .,Stolz'‘ durch Fick I^ 536, Prellwitz^ 260 durch die
Bed. „verzarteln, verwohnt'" sehr in Frage gestellt wird; ZsflieBen einer zu
Xeno), lepidus Wz. lep- „abschalen“ gehorigen Reihe mit Worten von unserer
Schallwz. ist freilich erwagenswert; iiber Xandl^co s. u,              und XdiXaip
„Sturmwind'‘ (als „heulend“; PreUwitz ^ 257).

3. lep- „abscbalen, abhauten, abspalten‘^
  Gr. XsTicD „8chale ab'‘, Xinog n., /.onog m. „Schale, Rinde, Haut“ {pXoTtico
„schale ab“), Xemg^ Xomg „Schuppe, Schale, Rinde“, Xojidg „fiaches Geschirr“,
/.endg „(*Schale),          einschalige Muschel, Napfschnecke“ (nicht nach Boisacq
s.   V.   von Xe:i:ag „Stein“;     iiber lat.   Lehnformen s. Yf. LEWb.^ u. Ia2)is,               le-
pista)^     XiTii'Qov   „ Schale, Hulse“,     Beiwort der Fische (eigen tl. „m
                                                eXXoyj
Schuppen seiend“, Fick BB. 26, 239, KZ. 44, 343), Xinga „Aussatz“ („*sich
schuppende Haut“); XeTtzog „enthulst (von Kornern); fein, diinn, zierlich,
schwach'^ (vgl. lat. lepidus; Fick I* 536; wegen der Bed. „enthulst‘‘ nicht
als „schla£f'‘ zu hb-, lep- „schlafF‘), Xstztvvco „hulse aus; mache dunn“ (iiber
/.ajiagog „schmachtig, diinn'' s. aber u. *(dp- „klein"); dehnstufig (o)
„Hulle, Gewand, Ledermantel" (^,,abgezogenes Fell" oder allenfalls aus
„abgetrennten Lappen" oder nach Meringer IF. 17, 161 „Gewand aus Rinde"),
?,d>7zog n. da., Xojip* xXauvg Hes.

   Alb. rape f. „Lappen, Fetzen" (: dt. Lappen'i G. Meyer Alb, Wb. 237),
430                                                                   lep-


Vjape „Bauclifell von Schlachttieren“ (vgl. deq^a : deQCo)^ Vepij „inei61e“,
Vats ,kleine Axt, Hacke‘* (^lapta\ Jold SBAk. Wien 168, I 46).
             5


    Lat. lepidus „zierlich, niedlich, allerliebst (vgl. oben XsTixog)^ lepos jjFein-
heit,        Anmut, heiterer Witz‘‘; vermutlicb auch                                  lapit „dolore   afBcit“ (^lep- ;
Wood Cl. Phil. 3, 82, Yf. LEWb.^ s. v.; vgl. zur Bed. lit. lupti „schalen“:
gr. XvjTTj),  Ags. lof m. „ 8 tirnband, Kopf binde“ (wenn o, so daS        lit. 16-                         =
pas    Holthausen IF. 32, 340)*
         \


   Lit. lopas „Flick, Lappen“, lopau^ -yti „flicken“, lopisz'^s^ lops^ys „Hange-
vpiege, urspri. aus Weidenzweigen oder Bast gefiochtener Korb‘‘ (Traut-
mann BB. 29, 308), lett, laps^ e-laps „Plick“;
    lit.         Idpas „Blatt“,                lett,   lapa   ds. ;    wohl anch        (vgl. kenxog^   lepidus)    lit.

lepus „weicblich, verzartelt, iibennutig", lepduti „ubermutig sein“,                                            lepinti
„verzarteln “5                lett.   lepus „Stolz“ (Mischung mit                     Formen von der Schaliwz.
lep-^ s. d.?)

    Sloven, l^en „Blatt“, osorb. nsorb. ablautend lopjeno „Blatt^‘; russ. lepem
===== search lap-aro
```


## [2026-09-06T23:19:51.422Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '28480,28515p' WLD_Bd2_pages.txt"
}
```


### [2026-09-06T23:19:51.470Z] TOOL RESULT

```
     Idfa    nicht nach Meringer          IF. 17, 161      zu   gi\   Xchnif}   „Gewand, das zu
lep-      „abschalen“.      — Air. gen. luce       (s.   Thurneysen lA.
                                                        26, 25), mir. lua
                                       Stokes [lA. 1, 185] Fickll^ 252 f.,
.jSteuerruder^^, cymr. usw. llyw ds. (von
als lo\p\ujo~ angereiht) sind nach Pedersen KG. I 61 f, Ableitnngen von
^pluuo-^ zu nXoog „Schiffahrt“ usw.


1.    lep- Schallwz.
     Ai. Idpati „schwatzt,        fliistert,   wehklagt,   redet^',   rdpati     ds.,   pam. lowam^
lewam „rede, spreche,             sage“, np. laha, lawa „Sclimeichelei^'; russ. lepetdih
„stamineln, schwatzen, lallen“, klr. iepetdty „lallen, plarren“,                        abg. lopotiv^
„stanimelnd, stotternd“, russ. lopoidth „platschern, larmen, klatschen‘‘, UpoH
jjGeschwatz, Larm“,         „platzen“, mdartl. „prugeln; fressen“ (wobl Ver-
quickung mit der auf einer ahnlichen Schallvorstellung berubenden Sippe
Hap- „lecken, scbliirfen'* usw., vgl, auch bg. Idpam „fresse, sclilinge“, skr.
Idpnem ds., Japcem^ Idptati „vomHunde: lechzen, keuchea“, sloven. Idpati
„sclinappen“, aber auch „schwatzen“), mit etwas anderer Bed.- Wen dung skr.
lepetati „fiattern“, poln. mdartl, lepietac sie „sich stolBen,   anschlagen, klap-
pern'';      cymr.   lief        Persson Wzerw. 216 Anm. 2 ex 215) „Stimme%
                             (^lepo-
mcymr. llefein „schreien‘", bret. lenv gemissement, pleurs, cri, douleur“,
vermutlich als Hcpagi- „Besprecher“, ir. I'laig (2 silbig), Gen. lega (Ht-aga)
„Arzt“ (daraus          —
                     ?? — Pedersen KG. I 311, got. leJceis^ ahd. lacJii, ags. l^ce
„Arzt“, trotz Feist 179 nicht mit llaig urverwandt; s. noch Falk-Torp u.
Icege m. Lit.).   S. auch S. 422!
   S. Uhlenbeck Ai. Wb. 258, Fick II ^ 248, Berneker 690, 702, 732.
   Yielleicht auf ders. Schallvorstellung, aber mit a-Vokalismus, beruht gr.
kaniCco „benehme mich ubermiitig^', Xamox'gg „Aufschneider, Prahler‘‘ (deren
Verb, mit lepiiS „ubermutig, verwohnt^, lepduti „ubermutig sein“, lepinti
^,verzarteln“, leti. lep^is .,Stolz'‘ durch Fick I^ 536, Prellwitz^ 260 durch die
Bed. „verzarteln, verwohnt'" sehr in Frage gestellt wird; ZsflieBen einer zu
Xeno), lepidus Wz. lep- „abschalen“ gehorigen Reihe mit Worten von unserer
Schallwz. ist freilich erwagenswert; iiber Xandl^co s. u,              und XdiXaip
```


## [2026-09-06T23:20:02.805Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW lacer\"; grep -n \"lacer,\" LEW_1910.txt | head -5\necho \"=== LEW lepos\"; grep -n \"lepos\\|lepidus\" LEW_1910.txt | head -5\necho \"=== LAT lacer\"; grep -n \"lacer\\b\\|lacer,\" LAT.txt | head -5\necho \"=== LAT lepos\"; grep -n \"lepos\\|lepidus\" LAT.txt | head -5"
}
```


### [2026-09-06T23:20:02.885Z] TOOL RESULT

```
=== LEW lacer
=== LEW lepos
=== LAT lacer
75:present ouvrage ne se propose pas de le remplacer -, et aussi
1932:ration"; et "epoque, temps". - Terme courant qui tend A remplacer
2184:lifere a tendn A remplacer agere par son frequentatif agitare.
2485:toutefois de a bref conserve dans les memes conditions que dans alacer,
2556:alacer (et alacris), -crls (et alacer) -e; vif, plein d'ardeur, ou
=== LAT lepos
33286:lepidus: v. lepos.
33291:lepos (lepor), -oris m.: grace, charme. - urbanitas elegans et
33294:Derives: lepidus: gracieux, joli; lepidulus, Lepidus,-dius; ille¬
33296:Lepos ne semble plus atteste aprfes Ciceron; lepidus, fr^quent dans
33298:k 1 '£poque imperiale (un ex. de lepidus dans Hor.A.P. 373 , de lepide
```


## [2026-09-06T23:20:05.439Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '33286,33320p' LAT.txt\necho \"=== LAT lacer headword\"; grep -n \"^lacer\\|^ *lacer\" LAT.txt | head -8"
}
```


### [2026-09-06T23:20:05.524Z] TOOL RESULT

```
lepidus: v. lepos.
lepista ( lepesta, lepasta, lepistra, Gloss.),-ae f.: genus uasis
aquarii, P.F.103,14. Emprunt au gr. AemxoTr|. Mot ancien, vite disparu;
v. Varron, L.L.5,133.637
lStum
lepos (lepor), -oris m.: grace, charme. - urbanitas elegans et
mollis ac faceta; unde homines tales lepidi uocantur, Gl„ Plac. CGL
V 30,17.
Derives: lepidus: gracieux, joli; lepidulus, Lepidus,-dius; ille¬
pidus.
Lepos ne semble plus atteste aprfes Ciceron; lepidus, fr^quent dans
la langue de la com^die, est rare d 4 jX dans Cic., et a peine atteste
k 1 '£poque imperiale (un ex. de lepidus dans Hor.A.P. 373 , de lepide
dans 1 'archalsant Aulu"Gelle 13,10,3).
On rapproche souvent gr. Xe 7 tT 0 S "minee, menu"; mais cet adj ectif
appartient evidemment X Xeroo "j 'ecale", et ceci <?carte le rapproche¬
ment; pour le rapprochement avec (F)eXTOO, lat. uolup , v.Benveniste,
Formation, p.iSS*
lepos, leptls: y.nepSs.
lepra, -ae f. : lfepre. Emprunt au gr. Xe7ipcx, atteste depuis Pline.
R^pandu par la 1 . de 1 'dtglise, d'ou leprosus, et passe dans les 1 .
romanes, M.L.4989-90.
lepus, -oris c.: i" libvre, hase; 3 0 Le Lievre (constellation);
3° leporis auricula, non d'une piante (= dictamnus); 4° aplysie, mol-
lusque. - Ancien (Pl. Cat. ),' usuel. Panroman. M,L.4yyi.
Derivas: lepusculus: levraut; leporarius; et subst. leporaria: viande
de lievre, leporarium: garenne (attestes en vieil italien, cf.M.L.
4y87~4y88); leporinus.
Emprunt a une langue nediterraneenne; cet animal n'a pas de nom
indo-europeen; peut*-etre parce qu'il 4 tait de mauvais augure et qu'on
4 vitait de le nominer (v. Vaillant, Slavia, y, p.4y7, avec le renvoi
a Schrader-Nehring, Reallexikon, sous Hase). Cf., en grec, Xe( 3 T]pl.S "la-
pin" (v. Boisacq, Dict.; sous Xe^pLC, avec les renvois, et B.A.Terra-
cini, Archiv.Glott. Italiano, 30,isqq.).La flexion du mot 1 'isole en
latin. Serait sicilien d'apres Varron, L.L.5,101: lepus, quod Sicu<li
=== LAT lacer headword
31750:lacer (lacerus cite par Prisc. GLK II 534,7), -a, -um: ddchire,
31776:lacerna, -ae f.: manteau ample a capuchon, ouvert en avant, et
31783:lacerta, -ae f. ; lacertus, -I f. (les deux formes sont egalement
31787:lacertus, -J m.(surtout usite au pl. lacerti; n. collectif lacerta
48146:lacer, enlacer. Ancien (Pl.), technique et rare; ni dans Cic. ni dans
64331:lacer. Se dit non seulement de la toile, mais de tout ouvrage dont
```


## [2026-09-06T23:20:10.176Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '31750,31782p' LAT.txt"
}
```


### [2026-09-06T23:20:10.234Z] TOOL RESULT

```
lacer (lacerus cite par Prisc. GLK II 534,7), -a, -um: ddchire,
lacdre, et aussi "qui ddchire" (Ov. M.8,880). Sens special donne par
les gloses "curtatis auribus ", cf. plus bas dans P.F., et Thes. Glos.,
s.u. - Ancien {laceri est dans Enn.),ni dans Cic.,Jtii dans Cesar.
Surtout po^tique, et de la prose imperiale. II est difficile de dire
si lacero est le denominatif de lacer, ou si au contraire lacer (us)
en est le postverbal. Verbe: lacero,-as: dechirer, lacerer, mettre
en pieces (sens physique et moral) lacerare bona, cf. gr. hom. ^pruAa-ro.lacerna
- SyC "
£ap 5 (X 7 CTei,v. Ancien, usuel et classique (Cic.).Non roman. Derives et
composes: lacer ati 5 ,-abi lis, -amentum,-ator,-dtrix,-atura (tardif);
dilacero, collaceratus, illacerabilis (Sil. = acmapoocTOS). Festus
reunit dans une meme famille lacer, lanius, lacinia, lacerna', cf.
P.F., 105,4, lacerare, diuidere, comminuere est; ex quo dictus est
lanius, qui disci<n>dendo lacerat pectora; lacinia quod pars uestimenti
est; lacerna, quod minus capitio est; lacer, quod auribus curtatis
est, et lacerum, quodcumque est in corpore imminutum. Cf. lancino.
- Lacero peut etre form^ comme tolerfi, lamberS; et lacer (us) etre
un postverbal de lac er 5 .
La coexistence de la forme a nasale infixee lancino et de lacer
montre qu'il s'agit d'une vieille famille de mots (cf. sancio: sacer).
Le grec a en effet \<xx—, X<xx— , dans a.7teXT]>ccf a7ieppwya Ku7ipt,o i ■ Hes.
et att. XcotoC "dechirure, lambeau", d'ou Xaxi^o) "je dechire"; aussi
Xcocr)’ pajoq Rpr^Tec Hes. - En supposant le sl. x issu d'une forme popu-
laire a. kh, on rapproche de plus pol. lah "haillon", russe loxma "hail¬
lon" .
lacerna, -ae f.: manteau ample a capuchon, ouvert en avant, et
attache par une boucle sous la gorge. Le mot, de caractere populaire,
oppose par Ciceron a toga (Phil.a,30,76), ne semble pas atteste avant
la fin de la r^publique. - Derivas: lacernatus; lacernula.
La plupart des mota en -erna sont populaires; souvent suspects
d'etre empruntes a 1 'etrusque. Le rattachement a lacer n 1 est qu’une
< 5 tymologie populaire.
```


## [2026-09-06T23:21:38.523Z] AGENT

Now I'll write the verification file.


## [2026-09-06T23:21:39.938Z] TOOL CALL #63: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && echo ok"
}
```


### [2026-09-06T23:21:39.978Z] TOOL RESULT

```
ok
```


## [2026-09-06T23:28:41.387Z] TOOL CALL #64: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-309.json",
 "content": "{\n  \"pdf_page\": 309,\n  \"book_page\": 279,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Lěk, Lak; Lakt, Lakat\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *leh₂k- (traditional *lēk- : *lək-) 'to tear, rend', with a t-extension *lakt-/*lakat- 'rag, scrap'\",\n      \"note\": \"The root itself is standard. Pokorny 674 has 'lēk-2 : lak-, Meaning: to tear, fell, fur, leather, bark' with Gr. λακίς, λακίζω and Lat. lacer, lacerna, lacinia; Walde-Pokorny II 419 f. has the same as 'lēq- : lǝq- zerreißen'; Watkins/AHD has 'lēk-. To tear. Zero-grade form *lək- becoming *lak- … Latin lacer, torn: LACERATE. [Pok. 2. lēk- 674]'. The language label 'Indo-European' and the gloss 'to tear; rag, scrap' are right. The second half of the root box, the t-stem 'Lakt, Lakat', is Mann's alone (IEC 660-661 'lakt-, lakot- rag, scrap, tatter'), built on Lith. lãkatas, Latv. lakats, Pers. laxt, Arm. latʿ and Skt. laktaka-; Pokorny and Walde-Pokorny do not set up such a stem, and WP II 420 explicitly rejects the Sanskrit member. Modern laryngealist handbooks (de Vaan, EDL 320-1) reconstruct the root as *leh₂(k)- 'bark, tear'.\",\n      \"note_fa\": \"ریشهٔ بازسازی‌شدهٔ هندواروپایی آغازین *leh₂k- (در سنت قدیم *lēk-/*lək-) به معنی «دریدن، پاره کردن» ریشه‌ای شناخته و پذیرفته است: پوکورنی (ص ۶۷۴) آن را با یونانی λακίς «پاره، ژنده» و لاتینی lacer «دریده» می‌آورد و واتکینز در پیوست فرهنگ American Heritage نیز همان را دارد. برچسب زبانی و معنای ریشه در نمودار نورایی درست است. اما بخش دوم جعبهٔ ریشه، یعنی ستاک *lakt-/*lakat-، تنها از آنِ مان (فرهنگ تطبیقی هندواروپایی، ص ۶۶۰–۶۶۱) است و پوکورنی و والده-پوکورنی چنین ستاکی نمی‌سازند؛ والده-پوکورنی (ج ۲ ص ۴۲۰) حتی واژهٔ سنسکریت laktaka- را به دلیل ناسازگاری در نظام آواگردان (ablaut) از این خانواده بیرون می‌گذارد. رویِ‌هم ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n      \"sources\": [\n        \"https://www.etymonline.com/word/lacerate\",\n        \"https://en.wiktionary.org/wiki/lacer\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:674\", \"status\": \"supports\", \"note\": \"POK_full.txt line 56672 ff.: 'Root / lemma: lek-2 : lak-  Meaning: to tear, fell, fur, leather, bark…  Material: Gr. λακίς \\\"scrap, shred\\\" … Latin lacer, -era, -erum \\\"to tear to pieces, mangle, rend\\\" … References: WP. II 419 f., WH. I 742 f.  Page(s): 674'. The printed page number Nourai cites is exactly right.\"},\n        {\"ref\": \"IEC:660,661\", \"status\": \"supports\", \"note\": \"IEC.txt, form-feed leaf 372 (awk NR==373; the leaf carries printed pp. 660-661): 'lak- (1) \\\"tear, rag\\\". Cf. lakt- (1)  Gk. lakís, f. \\\"rag, rip, tear\\\"; Lat. cf. lacer …' and 'lakt-, lakot- \\\"rag, scrap, tatter\\\". Cf. lak- (1)  Skt. (dim. type) laktakah \\\"rag\\\"; Per. laxt, laxd \\\"scrap\\\"; Arm. latʿ \\\"garment, cloth, rag\\\" beside lati \\\"scrap\\\"; Li. lákatas \\\"rag\\\"'. Every node of the chart comes from these two Mann entries.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II 419-420 s.v. 'lēq- : lǝq- zerreißen'\", \"stance\": \"supports\", \"note\": \"grep 'lacer,' in incoming/WLD/WLD_Bd2_pages.txt line 27845: 'Gr. λακίς \\\"Fetzen\\\", λάκος n. ds. …, λακίζω \\\"zerreiße\\\" …; lat. lacer, -era, -erum \\\"zerfetzt, zerrissen, zerfleischt\\\" …'. Same root, same members — but line 27865 adds 'Ai. laktaka- m. \\\"Lappen\\\" (Prellwitz² 258) widerspricht im Ablaut.'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 p. 33 (AHD_watkins1985.txt line 680) s.v. lēk-\", \"stance\": \"supports\", \"note\": \"'lēk-. To tear. Zero-grade form *lək- becoming *lak-. 1. Latin lacinia, flap of a garment: LACINIATE. 2. Suffixed form *lak-ero- in Latin lacer, torn: LACERATE. [Pok. 2. lēk- 674.]'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck, ch. 6.21 'rag' (SYN.txt line 10391)\", \"stance\": \"partial\", \"note\": \"'…erh. fr. lacer \\\"torn\\\" … λακίς \\\"rag\\\", λακίζω \\\"tear\\\" … WaldeP. 2.419 f.' — Buck cites the same root for Latin lacinia/lacer but discusses no Iranian or Indic member.\"},\n        {\"src\": \"KLN\", \"where\": \"vol. 2 s.v. 'lacerate' (KLN_1966.txt line 20950)\", \"stance\": \"supports\", \"note\": \"'fr. lacer, \\\"torn\\\", fr. I.-E. base *leq-, *lq-, \\\"to rend\\\", whence also Gk. λακίς, \\\"tatter, rag\\\", λακίζειν, \\\"to tear to pieces\\\", Alb. lakur, \\\"naked\\\"…'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"laxt «لَخت ( لَت )»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP لَخت laxt 'piece, portion, fragment, scrap' is a real and old word — Ferdowsi's line quoted in the chart (deh laxt 'ten pieces') is genuine, and Borhan-e Qateʿ s.v. لخت glosses it 'و بمعنی پارچه و حصه و برخ و جزو و پاره است همچو لخت کوه و لخت جگر' (v. 3, pdf p. 688), Moʿin 'جزو، نوع، قسم'. The variant لَت lat printed in parentheses is the short doublet ('a piece; a blow'), cf. Borhan v. 3 p. 686 'لت لت بمعنی پاره پاره و لخت لخت'. Formally Nourai's derivation is unobjectionable: an Old Iranian *lakta- would give Middle/New Persian laxt regularly (Ir. *-kt- > *-xt-, as in *saxta- > saxt, *duxta- > duxt), and Mann (IEC 661) lists 'Per. laxt, laxd \\\"scrap\\\"' beside Lith. lãkatas and Arm. latʿ under *lakt-. But there is no Avestan, Old Persian or attested Middle Persian antecedent (MacKenzie's CPD has no laxt), Pokorny records no Iranian reflex of *lēk- at all, and en.wiktionary, following Monchi-Zadeh 1990 p. 115 no. 336, calls laxt 'an imitative element borrowed from dialects', i.e. denies the inherited IE pedigree. So: right word, right meaning, derivation accepted by Mann (and hence by Nourai) but not independently established.\",\n          \"derivation_fa\": \"واژهٔ «لَخت» به معنی «پاره، تکه، جزء» واژه‌ای اصیل و کهن در فارسی دری است؛ بیت فردوسی که نورایی آورده («همان تخت پیروزه ده لَخت بود») درست است و برهان قاطع (چاپ معین، ج ۳) ذیل «لخت» می‌نویسد: «و بمعنی پارچه و حصه و برخ و جزو و پاره است همچو لخت کوه و لخت جگر»؛ معین نیز «جزو، نوع، قسم» آورده است. صورت «لَت» که در پرانتز آمده دوگانهٔ کوتاه‌شدهٔ همان واژه است. از نظر آوایی هم اشکالی در کار نیست: خوشهٔ ایرانی باستان ‎*-kt-‎ در فارسی میانه و نو به ‎-xt-‎ بدل می‌شود (مانند *saxta- > سخت)، پس *lakta- ← لخت پذیرفتنی است و مان (IEC ص ۶۶۱) نیز همین را کنار لیتوانیایی lãkatas و ارمنی latʿ آورده است. با این حال هیچ صورت اوستایی یا پهلوی گواهی‌شده‌ای در دست نیست (مکنزی «laxt» ندارد) و پوکورنی هیچ بازماندهٔ ایرانی برای این ریشه نمی‌آورد؛ ویکی‌واژه به پیروی از مونشی‌زاده آن را عنصری «آوابنیاد و برگرفته از گویش‌ها» می‌داند. بنابراین ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%84%D8%AE%D8%AA\",\n            \"https://abadis.ir/fatofa/%D9%84%D8%AE%D8%AA/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:661\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 372 s.v. 'lakt-, lakot-': '… Per. laxt, laxd \\\"scrap\\\"; Arm. latʿ \\\"garment, cloth, rag\\\" beside lati \\\"scrap\\\" …' — exactly Nourai's arrow.\"},\n            {\"ref\": \"MON:3563,3573\", \"status\": \"partial\", \"note\": \"Only the online Moʿin text (abadis.ir/fatofa/لخت) is accessible and it has both headwords with Nourai's senses — لَخت (اِ.) 'جزو، نوع، قسم' and لُخت 'برهنه، عریان' — but the online version carries no page numbers, so pp. 3563/3573 of the 6-vol. print could not be verified.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"vol. 3 (Moʿin ed.), pdf p. 688 s.v. لخت\", \"stance\": \"supports\", \"note\": \"grep 'لخت' in incoming/BQT/BQT_v3_pages.txt line 50920: 'و بمعنی پارچه و حصه و برخ و جزو ‌و پاره است همچو لخت کوه و لخت جگر' — the sense 'scrap, piece' that Nourai gives; the footnotes give only Persian cross-references, no IE etymology.\"},\n            {\"src\": \"MON\", \"where\": \"abadis.ir Moʿin s.v. لخت\", \"stance\": \"supports\", \"note\": \"'(لَ) (اِ.) جزو، نوع، قسم' and separately '(لُ) برهنه، عریان' — no origin tag ([په.] etc.), i.e. Moʿin claims no Pahlavi antecedent.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD — searched PHD.txt / PHD_mackenzie.txt for 'laxt', 'lht'\", \"stance\": \"silent\", \"note\": \"no Middle Persian laxt is recorded; the only l-a-b/l-a-h entries are lab 'lip', lābag 'supplication', šahr etc. So the word first surfaces in New Persian.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (HRN.txt), searched 'laxt', 'lacht'\", \"stance\": \"silent\", \"note\": \"Horn has no entry for laxt (his L-section, nos. 952-954, covers only lābe/lāf, leb, lēstan).\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt, grep 'لخت'\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-roots dictionary has no headword لخت.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Armenian\",\n          \"words\": \"lat\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Armenian լաթ latʿ 'cloth, rag, garment, tatter' (beside լաթի latʿi 'scrap') is a real word with exactly the meaning given, and Mann (IEC 661) lists it under *lakt- as a cognate of Persian laxt. Armenian lexicography, however, treats it as a loan rather than an inheritance: hy.wiktionary s.v. լաթ says flatly 'Փոխառություն՝ պարսկերեն lat' ('a borrowing from Persian lat'), which is also what the form suggests — an inherited *lakto- should have left a trace of the velar, whereas the bare latʿ matches New Persian lat one-for-one, in the same way as the many Persian textile terms borrowed into Armenian. Pokorny and Walde-Pokorny record no Armenian member of this root. So the word belongs to the family, but the arrow 'straight from the IE root' is probably an arrow through Persian.\",\n          \"derivation_fa\": \"واژهٔ ارمنی լաթ (latʿ) به معنی «پارچه، کهنه، جامه» واقعی است و معنایی که نورایی داده درست است؛ مان (IEC ص ۶۶۱) آن را همراه با «لخت» فارسی زیر ستاک *lakt- آورده است. اما فرهنگ‌های ارمنی آن را وام‌واژه می‌دانند نه میراث مستقیم: ویکی‌واژهٔ ارمنی ذیل լաթ می‌نویسد «وام‌گرفته از فارسی lat». صورت واژه هم همین را تأیید می‌کند، زیرا اگر از *lakto- به ارث رسیده بود انتظار بازتابی از همخوان کامی می‌رفت، حال آنکه latʿ دقیقاً برابرِ «لَت» فارسی است — همانند بسیاری از نام‌های پارچه و جامه که از ایرانی به ارمنی رفته‌اند. پوکورنی و والده-پوکورنی هیچ عضو ارمنی برای این ریشه نمی‌آورند. پس واژه به همین خانواده تعلق دارد، ولی پیکان نمودار (مستقیم از ریشه) به احتمال زیاد باید از راه فارسی بگذرد.\",\n          \"sources\": [\n            \"https://hy.wiktionary.org/wiki/%D5%AC%D5%A1%D5%A9\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:661\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 372 s.v. 'lakt-, lakot-': 'Arm. latʿ \\\"garment, cloth, rag\\\" beside lati \\\"scrap\\\"' — Mann does give the word here, with Nourai's gloss.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_full.txt s.v. lek-2 : lak- (p. 674)\", \"stance\": \"silent\", \"note\": \"Pokorny's material for this root is Greek, Albanian, Latin and Slavic only; no Armenian form is listed.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 419-420\", \"stance\": \"silent\", \"note\": \"grep 'lacer,' / 'laktaka' in WLD_Bd2_pages.txt: the entry lists Gr., Lat., Alb. and Slavic; no Armenian latʿ.\"},\n            {\"src\": \"hy.wiktionary\", \"where\": \"hy.wiktionary.org/wiki/լաթ, section Ստուգաբանություն\", \"stance\": \"partial\", \"note\": \"'Փոխառություն՝ պարսկերեն lat:' = 'Borrowing from Persian lat' — the word is in the family but via Persian, not directly from the IE root.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"lacer\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Lat. lacer, -era, -erum 'torn, mangled' (already in Ennius, then chiefly poetic and imperial prose), with the denominative lacerāre 'to tear to pieces'. It goes back to Proto-Italic *lakeros from the zero grade of PIE *leh₂k-/*lēk-, the suffix being *-ero- (Watkins: 'Suffixed form *lak-ero- in Latin lacer, torn'). The antiquity of the family within Latin is shown by the nasal-infixed doublet lancinō 'to rend' beside lacer — Ernout-Meillet, s.v. lacer: 'La coexistence de la forme à nasale infixée lancinō et de lacer montre qu'il s'agit d'une vieille famille de mots (cf. sanciō : sacer). Le grec a en effet λακ- … λακίς \\\"déchirure, lambeau\\\", d'où λακίζω \\\"je déchire\\\"'. The arrow root→Latin is exactly what Pokorny 674, WP II 419 and AHD draw.\",\n          \"derivation_fa\": \"صفت لاتینی lacer «دریده، پاره» (نخست در انیوس، سپس بیشتر در شعر و نثر دورهٔ امپراتوری) با فعل برساختهٔ lacerāre «پاره‌پاره کردن» از پایهٔ صفر ریشهٔ هندواروپایی *leh₂k-/*lēk- با پسوند ‎*-ero-‎ ساخته شده است؛ واتکینز صریحاً می‌نویسد «صورت پسوندی *lak-ero- در لاتینی lacer «دریده»». کهنگی این خانواده در لاتینی از وجود صورت هم‌ریشهٔ دارای میان‌نشین خیشومی lancinō در کنار lacer پیداست، چنان‌که ارنو و مه‌یه می‌گویند این هم‌زیستی نشان می‌دهد «با خانوادهٔ واژگانی کهنی سروکار داریم (قس sanciō : sacer)» و یونانی λακίς و λακίζω را هم‌ریشهٔ آن می‌شمارند. پیکان «ریشه ← لاتینی» در نمودار دقیقاً همان است که پوکورنی (۶۷۴)، والده-پوکورنی (ج ۲ ص ۴۱۹) و فرهنگ American Heritage می‌کشند: ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/lacer\",\n            \"https://www.etymonline.com/word/lacerate\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1526\", \"status\": \"supports\", \"note\": \"Nourai's page is the 1976 AHD appendix (not open online), but the same Watkins entry stands in AHD_watkins1985.txt line 680: 'lēk-. To tear … 2. Suffixed form *lak-ero- in Latin lacer, torn: LACERATE. [Pok. 2. lēk- 674.]'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. lacer (LAT.txt line 31750 ff.)\", \"stance\": \"supports\", \"note\": \"'lacer … déchiré, lacéré … La coexistence de la forme à nasale infixée lancino et de lacer montre qu'il s'agit d'une vieille famille de mots … Le grec a en effet λακ-, dans … λακίς \\\"déchirure, lambeau\\\", d'où λακίζω \\\"je déchire\\\".'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 419 (WLD_Bd2_pages.txt line 27845)\", \"stance\": \"supports\", \"note\": \"'lat. lacer, -era, -erum \\\"zerfetzt, zerrissen, zerfleischt, körperlich verstümmelt\\\", lacerna …, lacinia …' listed directly under 'lēq- : lǝq- zerreißen'.\"},\n            {\"src\": \"POK\", \"where\": \"p. 674 s.v. lek-2 : lak-\", \"stance\": \"supports\", \"note\": \"'Latin lacer, -era, -erum \\\"to tear to pieces, mangle, rend, mutilate, lacerate\\\", lacerna …, lacinia … lancino, -are \\\"tear, rend\\\"'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. lacerate (KLN_1966.txt line 20950)\", \"stance\": \"supports\", \"note\": \"'L. laceratus, pp. of lacerare … fr. lacer, \\\"torn\\\", fr. I.-E. base *leq-, *lq-, \\\"to rend\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"lacerate\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English lacerate is a learned Latinism: Lat. lacerātus, past participle of lacerāre 'to tear to pieces, rend', taken into English in the early 15th century (first in the physical sense 'tear the flesh', extended figuratively to 'harrow the feelings' by the 1640s — Etymonline). There is no French intermediary of substance; the verb was formed on the participial stem in the usual humanist way, and the noun laceration follows Lat. lacerātiō. Watkins lists LACERATE among the English derivatives of lēk-, and Klein s.v. lacerate gives the same chain.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی lacerate یک وام‌واژهٔ دانشورانه از لاتینی است: از lacerātus، اسم مفعول فعل lacerāre «پاره‌پاره کردن»، که در آغاز سدهٔ پانزدهم میلادی نخست در معنای فیزیکی «دریدن گوشت و پوست» وارد انگلیسی شد و از دههٔ ۱۶۴۰ معنای مجازی «آزردن و ریش کردن دل» نیز گرفت (اتیمانلاین). واسطهٔ فرانسوی در کار نیست؛ فعل به شیوهٔ معمول نوزایی از ستاک اسم مفعول ساخته شده و اسم laceration نیز بر lacerātiō لاتینی است. واتکینز LACERATE را در فهرست مشتقات انگلیسی ریشهٔ *lēk- می‌آورد و کلاین نیز همین زنجیره را می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/lacerate\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 1726, English index: 'LACERATE lēk-'; and line 680 lists LACERATE under lēk- via Latin lacer.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. lacerate, v. (KLN_1966.txt line 20950)\", \"stance\": \"supports\", \"note\": \"'lacerate, tr. v., to tear. — L. laceratus, pp. of lacerare, \\\"to tear to pieces, rend, lacerate\\\", fr. lacer, \\\"torn\\\"…'; also dilacerate (line 11416) and lancinate (21088) in the same family.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/lacerate\", \"stance\": \"supports\", \"note\": \"'early 15c., from Latin laceratus, pp. of lacerare \\\"tear to pieces, mangle\\\" … from PIE root *lēk- \\\"to rend, tear\\\" (source also of Greek lakis \\\"tatter, rag\\\", lakizein \\\"to tear to pieces\\\")'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (SKT.txt), grep 'lacerate'\", \"stance\": \"silent\", \"note\": \"the concise Skeat has no entry for lacerate.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Greek\",\n          \"words\": \"lakis\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Ancient Greek λακίς, -ίδος f. 'rent, rending, tatters' (usually plural, in Aeschylus and Euripides), with the denominative λακίζω 'tear to pieces' and λακιδόω. It continues Proto-Hellenic *lakíds from the zero grade *lh₂k- of PIE *leh₂k-, Greek showing the regular vocalisation of the laryngeal as α before the root consonant; it is the exact formal counterpart of the Latin family lacer / lancinō, as Pokorny 674, WP II 419, Ernout-Meillet and Klein all state. Nourai's gloss 'rag' and the arrow root→Greek are correct; note that Greek is a sister of Latin here, not its source, which is how the chart draws it.\",\n          \"derivation_fa\": \"واژهٔ یونانی باستان λακίς (مؤنث، حالت اضافی λακίδος) به معنی «پارگی، ژنده، تکه‌های دریده» است (بیشتر به صورت جمع، در آیسخولوس و اوریپید) و از آن فعل λακίζω «پاره کردن» ساخته شده. این واژه بازماندهٔ هلنی آغازین *lakíds از پایهٔ صفر *lh₂k- ریشهٔ *leh₂k- است؛ حنجره‌ای در یونانی به شیوهٔ قاعده‌مند پیش از همخوان ریشه به α بدل شده است. λακίς دقیقاً همتای صوریِ خانوادهٔ لاتینی lacer/lancinō است، چنان‌که پوکورنی (۶۷۴)، والده-پوکورنی (ج ۲ ص ۴۱۹)، ارنو-مه‌یه و کلاین هر چهار می‌گویند. معنایی که نورایی داده و پیکان «ریشه ← یونانی» درست است؛ توجه شود که یونانی در اینجا خواهرِ لاتینی است نه سرچشمهٔ آن، و نمودار هم همین را نشان می‌دهد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%BB%CE%B1%CE%BA%CE%AF%CF%82\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:660\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 372 s.v. 'lak- (1) \\\"tear, rag\\\"': 'Gk. lakís, f. \\\"rag, rip, tear\\\"; Lat. cf. lacer, adj. \\\"tearing, torn, ragged\\\"' — exactly the chart's Greek node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 674 s.v. lek-2 : lak-\", \"stance\": \"supports\", \"note\": \"'Gr. λακίς \\\"scrap, shred\\\", λάκος n. ds. …, λακίζω \\\"tear, rend\\\"' heads the material of the root.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 419\", \"stance\": \"supports\", \"note\": \"'Gr. λακίς \\\"Fetzen\\\", λάκος n. ds. …, λακίζω \\\"zerreiße\\\"'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. lacerate (KLN_1966.txt line 20950)\", \"stance\": \"supports\", \"note\": \"'…whence also Gk. λακίς, \\\"tatter, rag\\\", λακίζειν, \\\"to tear to pieces\\\"'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/λακίς\", \"stance\": \"supports\", \"note\": \"'From Proto-Hellenic *lakíds, from PIE *leh₂-/*leh₂k- \\\"to tear\\\". Cognate with Latin lacer and lancinō.'\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"laktakah\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The word is real: Skt. laktaka- 'a dirty and tattered cloth, a rag' (Monier-Williams; Apte 'lac; a tattered cloth, a rag'; Shabda-Sagara 'old and tattered cloth, a rag or rags; lac, the dye'). What is wrong is the arrow: the chart derives it from Greek λακίς (parent #5). That is impossible — Classical Sanskrit borrows nothing of this kind from Greek (the handful of Greek loans are technical, astronomical and late, e.g. horā, kendra), and a Greek stem lakid- could not surface as laktaka- with an unexplained -t-. Nourai's own source does not say it either: Mann (IEC 661) lists 'Skt. (dim. type) laktakah \\\"rag\\\"' as a sister member of the t-stem *lakt-, alongside Per. laxt and Arm. latʿ, not as a Greek derivative. And the standard handbooks reject the equation altogether: Walde-Pokorny II 420 says 'Ai. laktaka- m. \\\"Lappen\\\" (Prellwitz² 258) widerspricht im Ablaut' — the ablaut grade does not fit — and Pokorny 674 lists no Indic reflex at all. The Indian grammatical tradition analyses laktaka- as lakta- + -ka, tied to lākṣā 'lac dye' (the cloth sense arising from the red-dyed rag). So the node should at best be an independent branch off the root, and even that is disputed.\",\n          \"derivation_fa\": \"خودِ واژه واقعی است: در سنسکریت laktaka- به معنی «کهنه‌پارچهٔ چرکین، ژنده» (مونیر-ویلیامز) و نیز «لاک، رنگ سرخ» (آپته و شبدَه‌ساگَره). آنچه نادرست است پیکانِ نمودار است: نورایی این واژه را از یونانی λακίς می‌گیرد. چنین وام‌گیری‌ای ممکن نیست، زیرا سنسکریت کلاسیک از یونانی جز چند اصطلاح فنی و اخترشناختی متأخر (مانند horā و kendra) وام نگرفته است و ستاک یونانی lakid- به هیچ روی نمی‌تواند به صورت laktaka- با ‎-t-‎ توضیح‌ناپذیر درآید. خودِ منبع نورایی هم چنین نمی‌گوید: مان (IEC ص ۶۶۱) laktakah را در کنار «لخت» فارسی و latʿ ارمنی به عنوان هم‌ریشهٔ ستاک *lakt- می‌آورد، نه بازماندهٔ یونانی. افزون بر این، والده-پوکورنی (ج ۲ ص ۴۲۰) این هم‌ریشگی را یکسره رد می‌کند: «Ai. laktaka- «ژنده» از نظر آواگردان ناسازگار است»، و پوکورنی هیچ بازماندهٔ هندی برای این ریشه نمی‌آورد؛ سنت دستوری هند نیز آن را lakta- + پسوند ‎-ka‎ و مربوط به lākṣā «لاک، رنگ سرخ» می‌داند. پس پژوهش امروزی این پیکان را رد می‌کند.\",\n          \"sources\": [\n            \"https://www.wisdomlib.org/definition/laktaka\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:661\", \"status\": \"partial\", \"note\": \"IEC.txt leaf 372 s.v. 'lakt-, lakot- \\\"rag, scrap, tatter\\\"' does have 'Skt. (dim. type) laktakah \\\"rag\\\"', but as a co-ordinate cognate of Per. laxt / Arm. latʿ / Li. lákatas under the IE t-stem — Mann nowhere derives it from Greek λακίς.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II 420 (WLD_Bd2_pages.txt line 27865)\", \"stance\": \"contradicts\", \"note\": \"'Ai. laktaka- m. \\\"Lappen\\\" (Prellwitz² 258) widerspricht im Ablaut.' — Walde-Pokorny expressly exclude the Sanskrit word from this root.\"},\n            {\"src\": \"POK\", \"where\": \"p. 674 s.v. lek-2 : lak-\", \"stance\": \"silent\", \"note\": \"Pokorny's material is Greek, Albanian, Latin, Slavic; no Indo-Aryan member is cited, confirming that the Sanskrit link is not part of the standard account.\"},\n            {\"src\": \"Monier-Williams / Apte\", \"where\": \"wisdomlib.org/definition/laktaka\", \"stance\": \"partial\", \"note\": \"'a dirty and tattered cloth, a rag' and 'lac, the red dye'; the Indian analysis is lakta- + -ka, i.e. tied to the lac-dye word, not to a verb 'tear'.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"Lep; Lepos; Lap-aro\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *lep- 'to peel, flay' (Pokorny 2. lep- 678; Watkins lep-1), here conflated with the homophonous onomatopoeic *lep- 'to chatter, babble' (Pokorny 1. lep- 677-678)\",\n      \"note\": \"Half of this root box is standard and half is a merger. *lep- 'to peel, flay' is real: POK 678 'lep-2 Meaning: to peel, flay — Gr. λέπω \\\"exfoliate, peel off\\\", λέπος/λοπός \\\"bark, skin\\\", λεπίς \\\"scale\\\", λέπρα \\\"leprosy\\\" … Latin lepidus \\\"pleasant, elegant\\\", lepos'; AHD 'lep-1. To peel. 1. Greek lepein … 3. Suffixed variant form *lap-aro- in Greek laparos, soft: LAPAROTOMY. [Pok. 2. lep- 678]'. So 'to peel; flap, skin' is right, and both Latin lepos and Gk. laparos are placed there by Pokorny and Watkins. The added gloss 'soft, friendly', which is what carries the Persian node, belongs in the standard handbooks to a DIFFERENT root — Pokorny's '1. lep- expr. root, onomatopoeic words: Old Indic lapati \\\"chats, whispers, wails, talks\\\" … np. laba, lawa \\\"flattery, insincere compliments\\\"' (677-678) = WP II 429 '1. lep- Schallwz.'. Nourai follows Mann, who does merge them: IEC 680 'lepos (1) \\\"small, fine, dainty, trivial\\\". WP II, 430  Per. cf. lāf \\\"swagger\\\" beside lābah \\\"flattery; desire\\\"; … Lat. cf. lepos … \\\"wit, mirth\\\"'. WP II 429 itself concedes the merger 'ist freilich erwägenswert'. So: root real, gloss partly over-extended.\",\n      \"note_fa\": \"نیمی از این جعبهٔ ریشه استاندارد است و نیمی دیگر ادغامِ دو ریشه. ریشهٔ *lep- «پوست کندن، لایه‌برداشتن» واقعی است: پوکورنی (ص ۶۷۸، «lep-2») آن را با یونانی λέπω «پوست می‌کنم»، λεπίς «فلس»، λέπρα «جذام» و لاتینی lepidus/lepos می‌آورد و واتکینز نیز همان را دارد و λαπαρός را هم صورتی با واکهٔ a از همین ریشه می‌شمارد. پس «پوست کندن؛ پوسته، پوست» درست است. اما معنای افزودهٔ «نرم، دوستانه» که پایهٔ گرهِ فارسی است، در فرهنگ‌های معیار به ریشهٔ دیگری تعلق دارد: پوکورنی «lep-1» (ص ۶۷۷–۶۷۸) که ریشه‌ای آوابنیاد است و صراحتاً «np. laba, lawa «چاپلوسی»» را زیر آن می‌آورد، و والده-پوکورنی (ج ۲ ص ۴۲۹) نیز همان را «Schallwurzel» می‌نامد. نورایی در اینجا از مان پیروی می‌کند که این دو را یکی گرفته است (IEC ص ۶۸۰). والده-پوکورنی خود می‌پذیرد که درآمیختن این دو خانواده «درخور تأمل است». پس: ریشه درست، ولی معنای ریشه اندکی گسترده‌تر از آنچه منابع می‌دهند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D9%84%D8%A7%D9%81\",\n        \"https://en.wiktionary.org/wiki/lepos\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:678\", \"status\": \"partial\", \"note\": \"POK_full.txt line 55398 ff.: 'Root / lemma: lep-2  Meaning: to peel, flay … Page(s): 678' — supports 'to peel; flap, skin' (and includes λαπαρός). But the immediately preceding lemma 'lep-1, expr. root, onomatopoeic … np. laba, lawa \\\"flattery, insincere compliments\\\" … Page(s): 677-678' is where Pokorny actually files the Persian words, i.e. p. 678 covers both but as two separate roots.\"},\n        {\"ref\": \"IEC:680\", \"status\": \"supports\", \"note\": \"IEC.txt leaf 383 (page marker '680' printed on the leaf, awk NR==384 line 22): 'lepos (1) \\\"small, fine, dainty, trivial\\\". WP II, 430  Per. cf. lāf \\\"swagger\\\" beside lābah \\\"flattery; desire\\\"; Myc. cf. repoto- …; Lat. cf. lepos, gs -ōris, m. \\\"wit, mirth\\\"; cf. lepidus …' — Nourai's page number and his merger both come straight from Mann.\"},\n        {\"ref\": \"AHD:1526\", \"status\": \"supports\", \"note\": \"Nourai's 1976-appendix page is not open, but the same entry is AHD_watkins1985.txt line 687: 'lep-1. To peel. 1. Greek lepein, to peel … 3. Suffixed variant form *lap-aro- in Greek laparos, soft: LAPAROTOMY. [Pok. 2. lep- 678.]'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II 429-430 (WLD_Bd2_pages.txt lines 28489, 28518)\", \"stance\": \"partial\", \"note\": \"Two separate roots: '1. lep- Schallwz.  Ai. lápati \\\"schwatzt, flüstert, wehklagt, redet\\\" … np. laba, lawa \\\"Schmeichelei\\\"' and '3. lep- \\\"abschalen, abhäuten, abspalten\\\"  Gr. λέπω … Lat. lepidus …, lepos \\\"Feinheit, Anmut, heiterer Witz\\\"'. WP does add, of the two families, 'Zusammenfließen … ist freilich erwägenswert'.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. lep-1 (line 687)\", \"stance\": \"supports\", \"note\": \"'lep-1. To peel.' with Greek lepein, lepis, laparos; a separate lep-2 'to be flat; palm, sole, shoulder blade' [Pok. 2. lēp- 679] — no 'friendly' sense anywhere.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"lâf «لاف»; lâbeh «لابه»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both words are real and old, and they are one word. NP لابه lāba 'humble entreaty, flattery, coaxing' continues Middle Persian lābag, written l'pk' (MacKenzie, CPD p. 431: 'lābag [l'pk' | (M l'b), P l'b, N lāba] supplication. lābakkar [l'pkkl] suppliant'), and behind it stands Manichaean Parthian l'b 'to call upon, pray, request', which Moʿin's footnote to Borhan-e Qateʿ cites from Henning, 'A list of Middle-Persian and Parthian words', BSOS IX (Borhan v. 3, pdf p. 671, note 5), together with Sarikoli lew-am 'to speak'. MP intervocalic -b- gives NP -b- (lāba) with the common variant -v- (lāva); لاف lāf is the same stem with the sporadic New Persian shift of final -b/-p to -f, as Hübschmann sets out (Persische Studien p. 179 and p. 184: 'laf \\\"Prahlerei\\\" (H. 952) neben lava, lāba \\\"Schmeichelei\\\" (afgh. lāfa und lāpa \\\"boasting\\\")'), whence the semantic split 'coaxing speech' → 'bragging'. Horn no. 952 (p. 212) groups lābe, lāwe, lābīdan and lāf and connects them to Skt. lap-/lāpati 'chatter', Shughni/Sarikoli lēw-am 'speak', Pashto laudal 'to say' — that is Pokorny's onomatopoeic *lep-1, not *lep- 'to peel'. So the Iranian history is confirmed and the two words do belong together; only the attachment to Nourai's 'peel/soft' root is Mann's minority view.\",\n          \"derivation_fa\": \"هر دو واژه اصیل و کهن‌اند و در اصل یک واژه‌اند. «لابه» به معنی «زاری، تضرع، چرب‌زبانی» دنبالهٔ فارسی میانهٔ lābag (نوشتار پهلوی l'pk') است — مکنزی در فرهنگ کوچک پهلوی (ص ۴۳۱) می‌آورد: «lābag … supplication؛ lābakkar suppliant» — و پشتِ آن پارتی مانوی l'b «خواندن، دعا کردن، درخواست کردن» قرار دارد که معین در حاشیهٔ برهان قاطع (ج ۳) به نقل از هنینگ (BSOS، ج ۹) همراه با سریکلی lew-am «سخن گفتن» آورده است. «ب» میان‌واکه‌ای فارسی میانه در فارسی نو حفظ شده (لابه) و گونهٔ «لاوه» نیز رایج بوده است؛ «لاف» همان ستاک است با ابدال ‎b/p‎ پایانی به ‎f‎ که هوبشمان در «مطالعات فارسی» (ص ۱۷۹ و ۱۸۴) نشان می‌دهد: «laf «لاف‌زنی» در کنار lava، lāba «چاپلوسی» (افغانی lāfa و lāpa)». تحول معنایی نیز روشن است: «سخن نرم و چاپلوسانه» ← «گزاف‌گویی». هرن (شمارهٔ ۹۵۲، ص ۲۱۲) لابه، لاوه، لابیدن و لاف را یکجا می‌آورد و به سنسکریت lap-/lāpati «وراجی کردن»، شغنی/سریکلی lēw-am و پشتو laudal «گفتن» می‌پیوندد — یعنی ریشهٔ آوابنیادِ پوکورنی (lep-1)، نه ریشهٔ «پوست کندن». پس تاریخچهٔ ایرانی واژه‌ها تأیید می‌شود و پیوند دو واژه با یکدیگر درست است؛ تنها بستنِ آن‌ها به ریشهٔ «Lep: پوست کندن/نرم» دیدگاه اقلیتِ مان است و با احتیاط پذیرفتنی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%84%D8%A7%D9%81\",\n            \"https://en.wiktionary.org/wiki/%D9%84%D8%A7%D8%A8%D9%87\",\n            \"https://abadis.ir/fatofa/%D9%84%D8%A7%D8%A8%D9%87/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:680\", \"status\": \"supports\", \"note\": \"IEC.txt leaf with printed page marker '680': 'lepos (1) \\\"small, fine, dainty, trivial\\\". WP II, 430  Per. cf. lāf \\\"swagger\\\" beside lābah \\\"flattery; desire\\\" …' — literally Nourai's node, page and all.\"},\n            {\"ref\": \"MON:3518,3530\", \"status\": \"partial\", \"note\": \"The online Moʿin (abadis.ir/fatofa/لابه) gives 'لابه (بِ) (اِ.) ۱- عجز، نیاز. ۲- التماس، زاری. ۳- خودستایی، تکبر' and لاف 'خودستایی، گزاف‌گویی', i.e. Nourai's glosses; page numbers of the 6-vol. print cannot be checked online.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 431 (PHD.txt line 431)\", \"stance\": \"supports\", \"note\": \"'lab [lp | M lb, N ~] lip. lābag [l'pk' | (M l'b), P l'b, N lāba] supplication. lābakkar [l'pkkl] suppliant.' — a solid Middle Persian antecedent for لابه.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 952, p. 212 (HRN.txt, form-feed leaf 233)\", \"stance\": \"partial\", \"note\": \"'952. lābe, lāwe \\\"Schmeichelei, Bitte\\\", lābīden, lāf \\\"Prahlerei\\\". skr. √lap (ai. rap-), lāpati \\\"schwatzen\\\" … sign. lēw-am, sar. lew-am \\\"reden, sprechen, sagen\\\"; afg. laudal \\\"sagen, erzählen\\\".' Horn joins lāf and lāba, but to the 'speak' root, not to 'peel'.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien pp. 179 and 184 (HUB.txt lines 6312, 6544)\", \"stance\": \"supports\", \"note\": \"'Vgl. auch laf \\\"Prahlerei\\\" (H. 952, oben p. 96) neben lava, lāba \\\"Schmeichelei\\\" (afgh. lāfa und lāpa \\\"boasting\\\")?' and 'laf \\\"Prahlerei\\\", wenn es zu laba, lava \\\"Schmeichelei\\\" gehört' — the -f is a secondary New Persian development of -b/-p.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ ed. Moʿin, vol. 3, pdf pp. 670-671 (footnotes to لاف and لابه)\", \"stance\": \"supports\", \"note\": \"footnote to لابه: 'در اوراق مانوی (پارتی) l'b (نامیدن، دعا کردن، درخواست کردن)؛ پارسی میانه … لابه (Henning, A list of Middle Persian …, BSOS IX), سریکلی lew_am (گفتگو کردن، سخن گفتن)'; footnote to لاف cross-refers to Hübschmann.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 429 s.v. '1. lep- Schallwz.'\", \"stance\": \"contradicts\", \"note\": \"'Ai. lápati \\\"schwatzt, flüstert, wehklagt, redet\\\", rápati ds., pam. lowam, lewam \\\"rede, spreche, sage\\\", np. laba, lawa \\\"Schmeichelei\\\"' — the Persian words are placed under the onomatopoeic root, not under lep- 'abschalen'.\"},\n            {\"src\": \"POK\", \"where\": \"p. 677-678 s.v. lep-1\", \"stance\": \"contradicts\", \"note\": \"'Root / lemma: lep-1  Meaning: expr. root, onomatopoeic words  Material: Old Indic lapati \\\"chats, whispers, wails, talks\\\", rapati ds., pam. lowam, lewam \\\"speak, say\\\", np. laba, larla [= lawa] \\\"flattery, insincere compliments\\\"' — same verdict as WP.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt, grep '*lab', 'lābīdan'\", \"stance\": \"silent\", \"note\": \"Cheung's Etymological Dictionary of the Iranian Verb has no entry for the lāb-/lāf- family.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Latin\",\n          \"words\": \"lepos\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Lat. lepōs (older lepor), -ōris m. 'charm, grace, pleasantry, wit', with the adjective lepidus 'charming, witty' — a word of the comic poets and Cicero that dies out after him (Ernout-Meillet: 'Lepos ne semble plus attesté après Cicéron'). Pokorny 678 and WP II 430 file it under lep- 'to peel' by way of Greek λεπτός 'peeled, hence fine, thin, dainty': 'peeled/husked' → 'fine, delicate' → 'refined, charming, witty'; Mann (IEC 680) does the same. But Ernout-Meillet reject the equation outright: 'On rapproche souvent gr. λεπτός \\\"mince, menu\\\"; mais cet adjectif appartient évidemment à λέπω \\\"j'écale\\\", et ceci écarte le rapprochement' (LAT s.v. lepos), and de Vaan (EDL 335) calls the root origin unknown while allowing that a shift 'what has been peeled' → 'refinement' is thinkable. So: real word, right gloss, derivation from *lep- 'peel' accepted by some (Pokorny, Mann, Watkins) and rejected by others.\",\n          \"derivation_fa\": \"واژهٔ لاتینی lepōs (صورت کهن‌تر lepor) به معنی «لطف، ظرافت، بذله و نمکِ سخن» با صفت lepidus «بانمک، ظریف» واژه‌ای است از زبان کمدی‌نویسان و سیسرون که پس از او تقریباً از میان می‌رود. پوکورنی (ص ۶۷۸) و والده-پوکورنی (ج ۲ ص ۴۳۰) آن را زیر ریشهٔ lep- «پوست کندن» می‌آورند و راه تحول معنایی را از یونانی λεπτός «پوست‌کنده ← نازک، ظریف» می‌گیرند: «پوست‌کنده» ← «نازک و لطیف» ← «ظریف و بذله‌گو»؛ مان نیز همین را می‌گوید. اما ارنو و مه‌یه این هم‌ریشگی را رد می‌کنند: «غالباً آن را با λεπτός یونانی مقایسه می‌کنند؛ ولی این صفت آشکارا به λέπω «پوست می‌کنم» تعلق دارد و همین مقایسه را منتفی می‌سازد»، و دِ فان نیز خاستگاه ریشه را نامعلوم می‌داند هرچند تحول «پوست‌کنده ← ظرافت» را ناممکن نمی‌شمارد. پس واژه و معنا درست است ولی اشتقاق آن از ریشهٔ «پوست کندن» مورد اختلاف است: با احتیاط پذیرفتنی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/lepos\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:680\", \"status\": \"supports\", \"note\": \"IEC.txt s.v. 'lepos (1)': 'Lat. cf. lepos, gs -ōris, m. \\\"wit, mirth\\\"; cf. lepidus \\\"dainty, pretty, witty, pleasant\\\"' — Mann's gloss 'wit' is exactly Nourai's.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II 430 (WLD_Bd2_pages.txt line 28543)\", \"stance\": \"supports\", \"note\": \"'Lat. lepidus \\\"zierlich, niedlich, allerliebst\\\" (vgl. oben λεπτός), lepos \\\"Feinheit, Anmut, heiterer Witz\\\"' — under '3. lep- abschalen'.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. lepos (LAT.txt line 33291 ff.)\", \"stance\": \"contradicts\", \"note\": \"'On rapproche souvent gr. λεπτός \\\"mince, menu\\\"; mais cet adjectif appartient évidemment à λέπω \\\"j'écale\\\", et ceci écarte le rapprochement.'\"},\n            {\"src\": \"POK\", \"where\": \"p. 678 s.v. lep-2\", \"stance\": \"supports\", \"note\": \"'Latin lepidus \\\"pleasant, agreeable, charming, fine, elegant, neat\\\" (compare above λεπτός), lepos \\\"fineness, pleasantness, agreeableness, bright witticism\\\"'.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/lepos (Latin)\", \"stance\": \"partial\", \"note\": \"'The origin of the root is unknown. Based purely on form, it has been compared with λεπτός and λέπω \\\"to peel\\\", but because of the different meanings, this connection is uncertain and rejected by Ernout and Meillet 1985. De Vaan 2008 is skeptical, but suggests a change from \\\"what has been peeled\\\" to \\\"refinement\\\" is thinkable.'\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Greek\",\n          \"words\": \"laparos\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Gk. λαπαρός 'slack, loose (of the bowels), soft, hollow', with the substantive λαπάρα 'the flank, loins' and the verb λαπάσσω 'to empty, evacuate'. Watkins puts it exactly where Nourai does: 'Suffixed variant form *lap-aro- in Greek laparos, soft: LAPAROTOMY. [Pok. 2. lep- 678]', and Pokorny 678 includes it under lep-2 as '*λεπαρός', i.e. an a-vocalism variant of the 'peel → thin, fine' family (cf. λεπτός). But this is not the only view: Walde-Pokorny II 429 explicitly refers λαπαρός away — 'über λαπαρός \\\"schmächtig, dünn\\\" s. aber u. *lap- \\\"klein\\\"' — to a separate root, and current Greek etymology (Beekes, followed by en.wiktionary) groups λαπαρός with λαγαρός, πλαδαρός, χαλαρός and, because of the prothetic vowel of ἀλαπάζω, suspects Pre-Greek substrate origin. So the node is right in form and meaning but the attachment to *lep- is one of at least three competing accounts.\",\n          \"derivation_fa\": \"صفت یونانی λαπαρός به معنی «شل، نرم، تهی، گودشده (به‌ویژه دربارهٔ شکم)» است، با اسم λαπάρα «تهیگاه، پهلو» و فعل λαπάσσω «تهی کردن». واتکینز آن را دقیقاً در همان جایی می‌گذارد که نورایی می‌گذارد: «صورت پسوندی گونه‌دار *lap-aro- در یونانی laparos «نرم»: LAPAROTOMY»، و پوکورنی (ص ۶۷۸) نیز آن را ذیل lep-2 به شکل ‎*λεπαρός‎ می‌آورد، یعنی گونه‌ای با واکهٔ a از همان خانوادهٔ «پوست کندن ← نازک و ظریف» (قس λεπτός). ولی این تنها دیدگاه نیست: والده-پوکورنی (ج ۲ ص ۴۲۹) صراحتاً λαπαρός را به ریشهٔ جداگانهٔ *lap- «خرد، کوچک» حواله می‌دهد، و ریشه‌شناسی امروزی یونانی (بیکس و به پیروی او ویکی‌واژه) آن را در کنار λαγαρός و χαλαρός می‌نشاند و به سبب واکهٔ پیشین در ἀλαπάζω احتمال خاستگاه پیشایونانی (زیرلایه) می‌دهد. پس صورت و معنای گره درست است ولی انتساب آن به ریشهٔ *lep- تنها یکی از دست‌کم سه تبیین رقیب است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%BB%CE%B1%CF%80%CE%B1%CF%81%CF%8C%CF%82\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1526\", \"status\": \"supports\", \"note\": \"Same entry in AHD_watkins1985.txt line 687: 'lep-1. To peel. … 3. Suffixed variant form *lap-aro- in Greek laparos, soft: LAPAROTOMY. [Pok. 2. lep- 678.]' — Nourai's gloss 'soft' is Watkins's own word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 678 s.v. lep-2\", \"stance\": \"supports\", \"note\": \"'…λαπαρός \\\"fragile, flimsy, thin\\\" (*λεπαρός)' listed among the Greek material of lep- 'to peel, flay'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 429 (WLD_Bd2_pages.txt line 28527)\", \"stance\": \"contradicts\", \"note\": \"'(über λαπαρός \\\"schmächtig, dünn\\\" s. aber u. *lap- \\\"klein\\\")' — Walde-Pokorny remove it from lep- 'abschalen' to a different root.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. laparo- (KLN_1966.txt line 21132)\", \"stance\": \"partial\", \"note\": \"'Fr. Gk. λαπάρα, \\\"the flank, loins\\\", which is rel. to λαπαρός, \\\"soft, flaccid, hollow\\\", λαπάσσειν \\\"to empty\\\", and in gradational relationship to λεπτός, \\\"fine, thin, small\\\". See lepto-.' — Klein keeps the link to λεπτός but only as an ablaut relation.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"laparotomy\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A 19th-century medical coinage, not an inherited word: Klein s.v. laparotomy — 'Coined by the English surgeon Sir Thomas Bryant (1828-1914) fr. laparo- and Gk. -τομία, \\\"cutting of\\\", fr. -τομή, \\\"a cutting, section\\\"', where laparo- (before a vowel lapar-) is the combining form of Gk. λαπάρα 'the flank, loins' (so also laparectomy, laparoscopy). The gloss on the chart, 'surgical incision into abdominal wall', is exactly the technical sense, and the semantic step is Greek 'flank, soft part of the body' → the anatomical 'abdominal wall'. Watkins lists LAPAROTOMY under lep-1, i.e. the same chain the chart draws (root → Greek laparos → English).\",\n          \"derivation_fa\": \"این واژه یک برساختهٔ پزشکیِ سدهٔ نوزدهم است نه واژه‌ای موروثی: کلاین ذیل laparotomy می‌نویسد که آن را جراح انگلیسی سِر توماس برایانت (۱۸۲۸–۱۹۱۴) از laparo- و یونانی ‎-τομία‎ «بریدن» ساخته است؛ و laparo- (پیش از واکه lapar-) صورت ترکیبی λαπάρα یونانی «تهیگاه، پهلو» است (چنان‌که در laparectomy و laparoscopy). معنایی که در نمودار آمده («شکافِ جراحیِ دیوارهٔ شکم») دقیقاً همان معنای فنی است و گام معنایی از «پهلو، بخش نرم تن» در یونانی به «دیوارهٔ شکم» در اصطلاح تشریحی است. واتکینز نیز LAPAROTOMY را ذیل ریشهٔ lep-1 می‌آورد، یعنی همان زنجیرهٔ «ریشه ← یونانی laparos ← انگلیسی» که نمودار می‌کشد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 1730 (English index): 'LAPAROTOMY lep-1'; line 687 lists it under lep-1 via Greek laparos.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. laparotomy and laparo- (KLN_1966.txt lines 21132-21133)\", \"stance\": \"supports\", \"note\": \"'laparotomy, n., incision into the abdominal wall (surgery). — Coined by the English surgeon Sir Thomas Bryant (1828-1914) fr. laparo- and Gk. -τομία…'; 'laparo-, before a vowel lapar-, combining form denoting the flank or, less exactly, the abdominal wall (anat.) — Fr. Gk. λαπάρα, \\\"the flank, loins\\\"'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. lep-1\", \"stance\": \"supports\", \"note\": \"the derivative list under lep-1 ends '3. Suffixed variant form *lap-aro- in Greek laparos, soft: LAPAROTOMY'.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 5,\n      \"root\": \"Lěs, Lěsâ, Lěsos, Lesiom\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Mann's *lés- (lēsā, -ós, -ióm) 'place, space, area, room' — a reconstruction found in no other handbook, and queried by Mann himself\",\n      \"note\": \"Nourai's root box reproduces Mann exactly, down to the four stem-shapes: IEC (leaf with printed page 680) 'lés- (lēsā, ós, ióm) (?) \\\"place, space, area, room\\\"  Per. -lax, cpds. \\\"-place\\\"; OHG cf. gi-lari, n. \\\"room, dwelling\\\"; Icel. lár \\\"ditty-box\\\"; Sw. lår, m. \\\"box, drawer\\\"; LW in R lari; Latv. lēsa \\\"ayot, mudflat\\\"'. But the '(?)' is Mann's own, and no other authority sets up such a root. Pokorny's page 680 does have a lēs- — but with the meaning 'to gather, pick up' (Goth. lisan, OHG lesan, Lith. lèsti; WP II 440), which is a different root; there is no PIE root 'place, space' in Pokorny, Walde-Pokorny or Watkins/AHD. The two witnesses Nourai cites also have better-established separate etymologies (see the nodes). So the root is not a forgery, but it rests on one scholar's tentative proposal.\",\n      \"note_fa\": \"جعبهٔ ریشه در نمودار نورایی عیناً از مان گرفته شده است، حتی چهار صورت ستاک: مان (IEC، ص ۶۸۰) می‌نویسد «‎lés- (lēsā, ós, ióm) (?) «جا، فضا، ناحیه، اتاق»؛ فارسی ‎-lax‎ در ترکیب‌ها «-جا»؛ آلمانی علیای باستان gi-lari «اتاق، مسکن» …». اما آن علامت پرسش از خودِ مان است و هیچ مرجع دیگری چنین ریشه‌ای نمی‌سازد. صفحهٔ ۶۸۰ پوکورنی نیز ریشه‌ای به شکل lēs- دارد ولی به معنی «گرد آوردن، برچیدن» (گوتی lisan، آلمانی علیای باستان lesan، لیتوانیایی lèsti)، که ریشهٔ دیگری است؛ در پوکورنی، والده-پوکورنی و واتکینز هیچ ریشهٔ هندواروپایی به معنی «جا، فضا» وجود ندارد. دو گواه این ریشه نیز هر یک ریشه‌شناسی جاافتاده‌تری دارند (نگاه کنید به گره‌ها). پس این ریشه ساختگی نیست ولی تنها بر پیشنهاد محتاطانهٔ یک پژوهشگر استوار است: با احتیاط پذیرفتنی.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/leer\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"IEC:680\", \"status\": \"supports\", \"note\": \"IEC.txt, awk NR==385 line 5 (the page marker '681' follows on line 6, so this is printed p. 680): 'lés- (lēsa, ós, ióm) (?) \\\"place, space, area, room\\\"  Per. -lax, cpds. \\\"-place\\\"; OHG cf. gi-lari, n. \\\"room, dwelling\\\"; Icel. lár \\\"ditty-box\\\"; Sw. lår, m. \\\"box, drawer\\\"; LW in R lari; Latv. lēsa \\\"ayot, mudflat\\\"'. Nourai's page number, root shapes, gloss and both nodes come verbatim from here — including nothing Mann does not say. The '(?)' Nourai silently drops.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"p. 680 s.v. lēs- (POK_full.txt line 55503 ff.)\", \"stance\": \"contradicts\", \"note\": \"'Root / lemma: lēs-  Meaning: to gather, pick up  Material: Gothic lisan … Old High German lesan \\\"pick up, select\\\" … Lithuanian lesu, lesti \\\"peck, pick\\\" … References: WP. II 440 … Page(s): 680' — Pokorny's root of this shape means 'gather', not 'place'; he has no root 'place, space'.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II 440 (the source Pokorny cites for lēs-)\", \"stance\": \"silent\", \"note\": \"grep of WLD_Bd2_pages.txt turns up no root glossed 'Ort, Raum'; only the 'sammeln' family.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, roots in les- (AHD_watkins1985.txt)\", \"stance\": \"silent\", \"note\": \"Watkins has no root *les- of any meaning in the appendix; neither Persian -lāx nor OHG gilāri appears.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Persian\",\n          \"words\": \"lâx «ـلاخ»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Persian facts are exactly as the chart gives them. -lāx is a bound denominal suffix of place, never used alone: Dehkhoda s.v. لاخ 'ادات محل … جای، معدن … بی‌ترکیب گفته نشود', with سنگلاخ 'stony ground', دیولاخ 'demons' waste', رودلاخ, نمکلاخ; Moʿin's own footnote in Borhan-e Qateʿ (vol. 3, pdf p. 672) lists 'نمک‌لاخ، دیولاخ، سنگلاخ، اهرمن‌لاخ، رودلاخ، آتش‌لاخ، هندولاخ، کلوخ‌لاخ' — i.e. both of Nourai's examples, سنگلاخ and هندولاخ, are the lexicographers' own. What is not established is the origin. Mann's *lés- (IEC 680) is his own tentative proposal and Nourai's only authority; no Old or Middle Iranian antecedent of the suffix is attested (it is not in MacKenzie or Nyberg), and it becomes frequent only in later New Persian. Competing accounts exist: en.wiktionary files سنگلاخ among the derivatives of لخت laxt 'piece' (i.e. 'ground made of stone-pieces'), and the shape invites comparison with the productive Turkic denominal place-suffix -laq/-lıq (qıšlaq, otlaq) that Persian was in heavy contact with from the 11th century on. So: word and gloss confirmed, IE derivation unproven.\",\n          \"derivation_fa\": \"داده‌های فارسی دقیقاً همان است که در نمودار آمده. «ـلاخ» پسوندِ مکانِ وابسته است و هرگز تنها به کار نمی‌رود؛ دهخدا ذیل «لاخ» می‌نویسد: «ادات محل … جای، معدن … بی‌ترکیب گفته نشود» و نمونه‌های سنگلاخ، دیولاخ، رودلاخ و نمکلاخ را می‌آورد. معین نیز در حاشیهٔ برهان قاطع (ج ۳) فهرست می‌کند: «نمک‌لاخ، دیولاخ، سنگلاخ، اهرمن‌لاخ، رودلاخ، آتش‌لاخ، هندولاخ، کلوخ‌لاخ» — یعنی هر دو نمونهٔ نورایی («سنگلاخ» و «هندولاخ») از خودِ فرهنگ‌نویسان است. آنچه اثبات نشده خاستگاه پسوند است: ریشهٔ *lés- مان (IEC ص ۶۸۰) پیشنهادی محتاطانه و تنها مأخذ نورایی است؛ هیچ صورت ایرانی باستان یا فارسی میانه‌ای برای این پسوند گواهی نشده (نه در مکنزی و نه در نیبرگ) و کاربرد آن تنها در فارسی نوِ متأخر فراوان می‌شود. تبیین‌های رقیب هم هست: ویکی‌واژه «سنگلاخ» را در شمار مشتقات «لخت» (تکه، پاره) می‌آورد، و شکل پسوند مقایسه با پسوند مکانیِ زایای ترکی ‎-laq/-lıq‎ (قشلاق، اوتلاق) را پیش می‌کشد که از سدهٔ پنجم هجری به بعد در تماس گستردهٔ فارسی بوده است. پس واژه و معنا تأیید می‌شود ولی اشتقاق هندواروپایی اثبات‌نشده است.\",\n          \"sources\": [\n            \"https://www.vajehyab.com/dehkhoda/%D9%84%D8%A7%D8%AE\",\n            \"https://en.wiktionary.org/wiki/%D9%84%D8%AE%D8%AA\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:680\", \"status\": \"supports\", \"note\": \"IEC.txt s.v. 'lés- … \\\"place, space, area, room\\\"': 'Per. -lax, cpds. \\\"-place\\\"' — Mann's wording is Nourai's gloss 'a suffix meaning place of', verbatim.\"},\n            {\"ref\": \"MON:3522\", \"status\": \"partial\", \"note\": \"Moʿin's dictionary does carry لاخ as a suffix of place, and his footnote in the Borhan (v.3 pdf p. 672) gives exactly the compound list; the 6-vol. page number 3522 cannot be checked in the online text, which has no pagination.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ ed. Moʿin, vol. 3, pdf p. 672, s.v. لاخ\", \"stance\": \"supports\", \"note\": \"grep 'سنگلاخ' in incoming/BQT/BQT_v3_pages.txt line 49742: 'نمك لاخ ، دیولاخ ، سنگلاخ ، اهرمن لاخ ، رود لاخ ، آتش لاخ ، هندولاخ ، کلوخ لاخ و غیره پیوندد' — both of Nourai's examples, but no IE etymology is offered.\"},\n            {\"src\": \"MON\", \"where\": \"Dehkhoda/Moʿin via vajehyab.com/dehkhoda/لاخ\", \"stance\": \"supports\", \"note\": \"'ادات محل است که به آخر کلماتی چون نمکلاخ، دیولاخ، سنگلاخ، رودلاخ می‌پیوندد … جای، معدن … بی‌ترکیب گفته نشود' — confirms the gloss 'a suffix meaning place of'.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD (PHD.txt), searched for a Pahlavi -lāx/-l'h suffix\", \"stance\": \"silent\", \"note\": \"no such suffix is recorded for Middle Persian, so the chart's arrow has no attested Middle Iranian stage.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt, grep 'لاخ'\", \"stance\": \"silent\", \"note\": \"Aryanpur's dictionary of IE roots in Persian has no entry for the suffix.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/لخت, Etymology 3, 'Related terms'\", \"stance\": \"partial\", \"note\": \"سنگلاخ is listed among the relatives of لخت laxt 'piece' (itself called 'an imitative element borrowed from dialects'), i.e. a rival account of the suffix that has nothing to do with a root 'place'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Old High German\",\n          \"words\": \"gi-lâri\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"OHG gilāri n. 'room, dwelling' is a real word, and Mann (IEC 680) does cite it with just this gloss. Its normal Germanic etymology, however, does not need a PIE root 'place': gilāri is a ga-collective of OHG lāri 'empty' (MHG lære > NHG leer), from Proto-West Germanic *lāʀi, Proto-Germanic *lēziz — the same base that gives Dutch laar 'clearing in a wood' and the -lar of Wetzlar, Goslar, Fritzlar. And the adjective *lēziz is itself usually attached to the verbal root *lēs- 'to gather, glean' (Goth. lisan, OHG lesan; Pokorny 680, WP II 440), the sense running 'gleaned, harvested' → 'empty' → 'empty space, room'. That is to say: Mann's 'lés- place, space, area' is a re-labelling of exactly the material that everyone else derives from lēs- 'gather', with the derived meaning promoted to the root. The form and gloss are right; the direction of the derivation is the disputable part.\",\n          \"derivation_fa\": \"واژهٔ gilāri در آلمانی علیای باستان به معنی «اتاق، جای زیست» واقعی است و مان (IEC ص ۶۸۰) نیز آن را با همین معنا آورده است. اما ریشه‌شناسی متعارف ژرمنی برای آن نیازی به ریشه‌ای هندواروپایی به معنی «جا» ندارد: gilāri صورتِ جمعی‌ساز با پیشوند ga- از صفت lāri «تهی» است (آلمانی میانه lære، آلمانی نو leer) که به ژرمنی باختری آغازین ‎*lāʀi‎ و ژرمنی آغازین ‎*lēziz‎ می‌رسد — همان پایه‌ای که هلندی laar «جای گشوده در جنگل» و جزء ‎-lar‎ در نام‌جاهای Wetzlar و Goslar و Fritzlar از آن است. خودِ ‎*lēziz‎ را نیز معمولاً به ریشهٔ فعلی ‎*lēs-‎ «گرد آوردن، برچیدن» (گوتی lisan، آلمانی علیای باستان lesan؛ پوکورنی ص ۶۸۰) می‌بندند، با این سیر معنایی: «برچیده، دروشده» ← «تهی» ← «فضای تهی، اتاق». به سخن دیگر، ریشهٔ «جا، فضا»ی مان بازنام‌گذاریِ همان موادی است که دیگران از ‎lēs-‎ «گرد آوردن» می‌گیرند، با ارتقای معنای ثانوی به معنای ریشه. صورت و معنای گره درست است؛ آنچه محل بحث است جهت اشتقاق است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/leer\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:680\", \"status\": \"supports\", \"note\": \"IEC.txt s.v. 'lés-': 'OHG cf. gi-lari, n. \\\"room, dwelling\\\"' — word, gender and gloss exactly as on the chart.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 680 s.v. lēs- 'to gather, pick up'\", \"stance\": \"partial\", \"note\": \"'Old Saxon Old High German lesan \\\"pick up, select\\\" and (after the double meaning from Latin legere) \\\"read (a book)\\\" … References: WP. II 440' — the Germanic family of this shape is the 'gather' one; Pokorny records no gilāri.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/leer (German)\", \"stance\": \"partial\", \"note\": \"'From Middle High German lēr, lēre, lǣre, from Old High German lāri, from Proto-West Germanic *lāʀi, from Proto-Germanic *lēziz'; cognates given are Dutch laar 'clearing in woods' and English leer — i.e. the OHG base of gi-lāri means 'empty', not 'place'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 440 (the 'sammeln' root)\", \"stance\": \"silent\", \"note\": \"grep of WLD_Bd2_pages.txt for 'gilari'/'gi-lari' returns nothing; Walde-Pokorny do not discuss the compound.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T23:28:41.424Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-309.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T23:28:45.308Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-309.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 309"
}
```


### [2026-09-06T23:28:51.005Z] TOOL RESULT

```
JSON OK
nodes verified: 12/12
node verdicts: {'plausible': 7, 'confirmed': 4, 'disputed': 1}
root verdicts: {'confirmed': 1, 'plausible': 2}
ref checks: {'supports': 11, 'partial': 4}
books consulted: {'supports': 22, 'silent': 11, 'partial': 8, 'contradicts': 5} | by book: {'POK': 8, 'WLD': 8, 'KLN': 5, 'Wiktionary': 4, 'BQT': 3, 'PHD': 3, 'MON': 2, 'HRN': 2, 'ARY': 2, 'LAT': 2, 'hy.wiktionary': 1, 'Etymonline': 1, 'SKT': 1, 'Monier-Williams / Apte': 1, 'HUB': 1, 'CHEUNG': 1, 'AHD': 1}
```


## [2026-09-06T23:29:13.679Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-309.json` written; `verify_check.py 309` reports 12/12 nodes, 0 PROBLEM lines.

**Page 309 (book p. 279) — 3 non-redirect entries, 12 nodes (4 redirects skipped)**

- Node verdicts: 4 confirmed, 7 plausible, 1 disputed. Root verdicts: 1 confirmed (Lěk), 2 plausible (Lep, Lěs).
- Ref checks: 11 supports, 4 partial (all four are MON page numbers — the 6-vol. Moʿin pagination is not checkable online; the entries themselves are right).

**Disputed**
- *Lěk* #6 Sanskrit `laktakah` "rag" — the chart derives it from Greek *lakis*. Impossible route (no Greek→Classical Sanskrit borrowing of this kind, and Gk. *lakid-* cannot give *-kt-*). Nourai's own source, Mann IEC 661, lists it as a sister cognate under \*lakt-, not a Greek derivative; Walde-Pokorny II 420 rejects the equation outright ("Ai. laktaka- … widerspricht im Ablaut"); Pokorny 674 lists no Indic reflex.

**Main "plausible" reasons (not errors, but worth the owner knowing)**
- *Lep* root + Persian node: Nourai merges two Pokorny roots. POK/WP/Horn 952 (p. 212)/Wiktionary all put NP لاف/لابه under the onomatopoeic \*lep- "chatter" (Skt. *lapati*), not \*lep- "peel". The Iranian chain itself is solidly confirmed: MP *lābag* (MacKenzie CPD 431) < Parthian *lʾb*, with lāf < lāb by the NP -b/-p > -f shift (Hübschmann pp. 179/184). Nourai follows Mann IEC 680, who does merge them.
- *Lěs* root exists only in Mann, who himself marks it "(?)". Pokorny's p. 680 lēs- means "to gather", not "place". Persian ـلاخ and OHG *gi-lāri* are both correct in form/meaning (Dehkhoda; Moʿin's Borhan footnote v.3 pdf p.672 lists سنگلاخ and هندولاخ verbatim), but OHG *gilāri* is normally from *lāri* "empty" (< PGmc \*lēziz, cf. Du. *laar*, -lar of Wetzlar), and ـلاخ has no attested Old/Middle Iranian antecedent.
- Latin *lepos* (Ernout-Meillet reject the λεπτός/λέπω link) and Greek *laparos* (WP II 429 sends it to \*lap- "klein"; Beekes/Wiktionary suspect Pre-Greek) — AHD/Pokorny support Nourai, others don't.
- Armenian *lat* is treated by Armenian lexicography (hy.wiktionary) as a borrowing from Persian *lat*, not a direct IE inheritance.

**Extraction errors: none.** I rendered PDF p. 309 and checked every box, including the Greek→Sanskrit arrow and the Persian scripts «لَخت ( لَت )», «لاف»، «لابه»، «ـلاخ» + extra «سنگلاخ ، هندولاخ» — the JSON is faithful to the printed page.

14 web sources archived via `fetch_source.py`; all local-book quotes carry file/line or pdf-page references (POK_full, WLD Bd2, IEC leaf 372/384/385, AHD_watkins1985, KLN_1966, LAT, HRN leaf 233, HUB, PHD, BQT_v3 pdf pp. 670-672, 688).
