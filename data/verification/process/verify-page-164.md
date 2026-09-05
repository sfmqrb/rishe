# Verification process log — verify-page-164


## [2026-09-05T20:32:21.563Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 164 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-164.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-164.json. Write /home/sfmqrb/git/rishe/data/verification/page-164.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 164` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:32:23.066Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:32:23.757Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:32:23.772Z] TOOL RESULT

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


## [2026-09-05T20:32:24.198Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-164.txt"
}
```


### [2026-09-05T20:32:24.210Z] TOOL RESULT

```
1	=== PDF page 164 (book page 134) ===
2	--- entry 0 ---
3	ROOT [Old French] Frankon : free people, conquerors, referring to the Germanic tribe which conquered Gaul about 500 AD.  (refs AHD:522,1515)
4	#1 (parent #0) [Old French] refs=AHD:522 | franc : free ; France : land of free people
5	  #2 (parent #1) [Persian] refs=MON:2528 | Farânseh «فرانسه» : France | extra: فرانک ، فرانکلین
6	  #3 (parent #1) [Arabic] refs=HJB:352 | faranji, al-faranji : French, European
7	    #4 (parent #3) [Persian] refs=BQT:1471 | farangî «فرنگ» : European | extra: فرنگستان ، افرنجی
8	  #5 (parent #1) [English] refs=AHD; KLN:614 | Frank, Franc, France, Franklin, franchise
9	--- entry 1 ---
10	ROOT [Old Persian] Fra-sanga : a distance of about five kilometers  (refs HRN:182)
11	#1 (parent #0) [Pahlavi] refs=BQT:1462 | farsang
12	  #2 (parent #1) [Persian] refs=MON:743,2517; BQT:1462 | farsang «فرسنگ» : a distance of about 5 kilometers ; farsax «فرسخ» : Arabic pronunciation of "farsang" | extra: پرسنگ
13	#3 (parent #0) [Greek] refs=KLN:1127 | parsanges
14	  #4 (parent #3) [Latin] refs=AHD:952 | parsanga
15	    #5 (parent #4) [English] refs=AHD:952 | parsang : an ancient Persian unit of distance (3.5 miles)
16	
```


## [2026-09-05T20:32:27.355Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-164.json",
 "description": "Read source JSON for page 164"
}
```


### [2026-09-05T20:32:27.391Z] TOOL RESULT

```
{
  "pdf_page": 164,
  "book_page": 134,
  "entries": [
    {
      "root": {
        "name": "Frankon",
        "lang": "Old French",
        "refs": "AHD:522,1515",
        "gloss": "free people, conquerors, referring to the Germanic tribe which conquered Gaul about 500 AD.",
        "note": "This is a Frankish word."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old French",
          "refs": "AHD:522",
          "words": [
            {"translit": "franc", "gloss": "free", "script": null},
            {"translit": "France", "gloss": "land of free people", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:2528",
          "words": [
            {"translit": "Farânseh", "gloss": "France", "script": "فرانسه"}
          ],
          "script_extra": "فرانک ، فرانکلین",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Arabic",
          "refs": "HJB:352",
          "words": [
            {"translit": "faranji, al-faranji", "gloss": "French, European", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:1471",
          "words": [
            {"translit": "farangî", "gloss": "European", "script": "فرنگ"}
          ],
          "script_extra": "فرنگستان ، افرنجی",
          "note": null,
          "quote": {
            "text": "زی فرنگستان سه کرت شاه ایران راند خنگ - خواست تا ایران شود همچون فرنگستان قشنگ",
            "poet": "Bahâr"
          }
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "English",
          "refs": "AHD; KLN:614",
          "words": [
            {"translit": "Frank, Franc, France, Franklin, franchise", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Fra-sanga",
        "lang": "Old Persian",
        "refs": "HRN:182",
        "gloss": "a distance of about five kilometers"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT:1462",
          "words": [
            {"translit": "farsang", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:743,2517; BQT:1462",
          "words": [
            {"translit": "farsang", "gloss": "a distance of about 5 kilometers", "script": "فرسنگ"},
            {"translit": "farsax", "gloss": "Arabic pronunciation of \"farsang\"", "script": "فرسخ"}
          ],
          "script_extra": "پرسنگ",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:1127",
          "words": [
            {"translit": "parsanges", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Latin",
          "refs": "AHD:952",
          "words": [
            {"translit": "parsanga", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:952",
          "words": [
            {"translit": "parsang", "gloss": "an ancient Persian unit of distance (3.5 miles)", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:32:27.641Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:32:27.681Z] TOOL RESULT

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


## [2026-09-05T20:32:47.005Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AHD','MON','HJB','BQT','KLN','HRN']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:900]); print('---')\n\"",
 "description": "Check refs_online entries"
}
```


## [2026-09-05T20:32:48.709Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"=== recent example ===\" && python3 -c \"\nimport json;d=json.load(open('data/verification/page-124.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\"",
 "description": "List verification dir and sample file"
}
```


### [2026-09-05T20:32:49.113Z] TOOL RESULT

```
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
---
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
---
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online a
---
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
---
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
---
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
---
```


### [2026-09-05T20:32:50.653Z] TOOL RESULT

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
page-311.json
page-31.json
page-32.json
=== recent example ===
{
 "entry": 0,
 "root": "Dhě 2",
 "verdict": "confirmed",
 "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)",
 "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.",
 "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را از ریشهٔ daṇs-/dąh- «آموختن» می‌گیرند. نکتهٔ کوچک‌تر آنکه معنای «دادن» در خانهٔ ۱۱ متعلق به ریشهٔ دیگر *deh₃- است و ابوالقاسمی در همان FFD:52 این دو را جدا کرده است. در مجموع، ادعای نورایی دربارهٔ خودِ ریشه درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-"
 ],
 "ref_check": [
  {
   "ref": "AHD:1512",
   "status": "supports",
   "note": "Watkins's Indo-European appendix (local file AHD_watkins1985.txt line 375): 'dhē-¹. To set, put. Contracted from *dheə ...
```


## [2026-09-05T20:32:56.032Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb && pdftoppm -f 164 -l 164 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg164 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render printed page 164"
}
```


### [2026-09-05T20:32:57.849Z] TOOL RESULT

```
Exit code 1
I/O Error: Couldn't open file 'EtymologicalDictionary-persian-english.pdf': No such file or directory.
```


## [2026-09-05T20:32:58.137Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN parasang ===\"; grep -n -i 'parasang' KLN_1966.txt | head -20; echo \"=== KLN Frank ===\"; grep -n \"^Frank\" KLN_1966.txt | head -20; echo \"=== SKT ===\"; grep -n -i 'parasang\\|^franc\\|^frank' SKT.txt | head -20",
 "description": "Grep Klein and Skeat"
}
```


### [2026-09-05T20:32:58.239Z] TOOL RESULT

```
=== KLN parasang ===
27341:paraplegia,  n.,  paralysis  of  the  lower  half  of  the body  on  both  sides  (med.)  —  Medical  L.,  fr.  Gk. 7tapa7rXf]Yia,  ‘hemiplegia’,  fr.  7tapar:X7)<j(jEiv, ‘to  strike  at  the  side’,  fr.  rrapa  (see  para-)  and rrXYjcCTEiv,  ‘to  strike’,  which  is  rel.  to  nXrjyf], ‘stroke’,  7tXi)Y[xa,  ‘blow’.  See  plague  and  1st  -ia. Derivatives:  parapleg-ic,  adj.  and  n. parapraxis,  n.,  faulty  action,  blunder  (psycho¬ analysis).  —  ModL.,  coined  fr.  para-,  ‘beside’, and  Gk.  n:pa^G,‘a  doing,  transaction,  business’, from  the  stem  of  npaxTEiv,  ‘to  do’.  See  practical, parapsychology,  n.,  that  branch  of  psychology which  deals  with  psychic  phenomena,  as  extra¬ sensory  perception ;  psychical  research.  —  Coin¬ ed  fr.  para-,  ‘beside’,  and  psychology, parapsychosis,  n.,  abnormal  psychosis.  —  ModL., coined  fr.  para-,  ‘beside’,  and  psychosis, parasang,  n.,  a  Persian  measure  of  length,  equal to  about  3  2/5  miles.  —  L.  parasanga,  fr.  Gk. rtapaaayyT)?,  ‘parasang’,  which  is  of  Iranian origin.  Cp.  Pehlevi  frasang,  farsang,  ModPers. ferseng.
=== KLN Frank ===
435:Frankel,  Siegmund,  Die  aramaischen  Fremdworter  im  Arabischen,  Leyden,  1886. Gamillscheg,  E.,  Etymologisches  Worterbuch  der  franzosischen  Sprache,  Heidelberg,  1926-28. Hehn,  V.,  Kulturpflanzen  und  Haustiere  in  ihrem  Ubergang  aus  Asien  nach  Griechenland  und Italien,  8.  Auflage,  neu  herausgegeben  von  O.  Schrader,  Berlin,  1911.
15326:Frank.
15331:Frank,  n.,  member  of  a  West  Teutonic  people.  — OHG.  Franko,  rel.  to  OE.  Franca.  See  frank, adj.
15335:Frankland  (1825-99).  For  the  ending  see  subst. suff.  -ite.
16831:Frankish  *witan,  ‘to  show’  (whence  also  OProv¬ eng.  guidar,  guizar).  Cp.  OS.  wisian,  ON.  visa, Dan.  vise,  Swed.,  Norw.  visa,  OFris.  wisa, MDu.  wisen,  Du.  wijzen,  OHG.,  MHG.  wiser, G.  weisen,  ‘to  show,  point  out’,  OE.  witan,  ‘to see’.  See  wise,  adj.  and  n.,  wit,  v.,  and  cp.  guise. Cp.  also  guidone,  guy,  ‘rope’,  Guy. guide,  n.  —  F.,  fr.  OProveng.  or  It.  guida,  ‘guide, leader’,  fr.  OProveng.  guidar,  ‘to  lead’.  See guide,  v.
=== SKT ===
33:FRANKLIN    SQUARE 1900
24052:Frankalmoign,  the  \\%'. by  which  most  cbnich-landb  at -OH  G.  and  L.-Gk,^     Lit. ^f .franc,  free;  Anglo- F,  mim^mi almosfUt  alms.    See  Frank  and
```


## [2026-09-05T20:33:02.856Z] TOOL CALL #9: Bash

```json
{
 "command": "ls *.pdf 2>/dev/null; ls site/pages/164.jpg 2>/dev/null; find . -maxdepth 2 -iname '*.pdf' | head",
 "description": "Locate the dictionary PDF"
}
```


### [2026-09-05T20:33:02.935Z] TOOL RESULT

```
EtymologicalDictionary-persian-english.pdf
site/pages/164.jpg
./EtymologicalDictionary-persian-english.pdf
```


## [2026-09-05T20:33:04.534Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN frank adj ===\"; sed -n '15320,15340p' KLN_1966.txt; echo \"=== AHD watkins ===\"; grep -n -i 'frank\\|parasang' AHD_watkins1985.txt | head -20",
 "description": "Klein frank entry and AHD"
}
```


### [2026-09-05T20:33:04.609Z] TOOL RESULT

```
=== KLN frank adj ===
Franciscan,  adj.,  pertaining  to  St.  Francis  of Assisi.  —  See  next  word.
Franciscan,  n.,  a  friar  of  the  Franciscan  order.  — Formed  with  suff.  -an  fr.  Franciscus,  ML.  name of  St.  Francis  of  Assisi  (l  182-1226),  who  estab¬ lished  this  order.
francium,  n.,  name  of  a  chemical  element.  — ModL.,  coined  by  the  French  chemist  Mile. Marguerite  Perey  (1909-  )  on  analogy  of  the names  of  many  chemical  elements  ending  in -ium  fr.  Francia,  Latinized  name  of  France,  her native  land.
franckeite,  n.,  a  complex  sulfide  (mineral.)  —
Named  after  the  German  mining  engineers  Carl and  Ernest  Francke.  For  the  ending  see  subst. suff.  -ite.
Franco-,  combining  form  meaning  1)  Frankish; 2)  French.  —  Fr.  ML.  Francus,  ‘a  Frank’.  See
Frank.
francolin,  n.,  name  of  various  genera  of  par¬ tridges.  —  F.,  fr.  It.  francolino,  which  is  of  un¬ certain  etymology.
francolite,  n.,  a  variety  of  apatite  (mineral.)  — Named  after  Wheal  Franco  in  Devonshire,  For the  ending  see  combining  form  -life. Francophile,  Francophil,  n.,  a  friend  of  France or  the  French.  —  Compounded  of  Franco-  and Gk.  91X01;,  ‘friend’.  See  -phile,  -phil. Francophobe,  n.,  one  who  fears  or  hates  France or  the  French.  —  Compounded  of  Franco-  and Gk.  -9'jfjo<;,  fr.  96^0?,  ‘fear’.  See  -phobe. Francophobia,  n.,  fear  or  hatred  of  France  or  the French.  —  Compounded  of  Franco-  and  Gk. -90^(5,  ‘fear  of’,  fr.  96^05,  ‘fear’.  See  -phobia, franc-tireur,  n.,  a  sharpshooter  of  the  irregular infantry.  —  F.,  lit.  ‘free  shooter’,  fr  .franc,  ‘free’, and  lireur ,  ‘shooter’,  fr.  tirer,  ‘to  draw;  to shoot’.  See  frank,  adj.,  and  tire,  ‘to  puli’, frangible,  adj.,  breakable;  fragile.  —  OF.,  fr.  L. frangere,  ‘to  break’.  See  fraction  and  -ible. Derivatives:  fragibil-ity,  n.,  fragible-ness,  n. frangipane,  frangipani,  n.,  a  kind  of  pastry  cream.
—  From  the  Italian  family  name  Frangipani. frank,  adj.  —  OF.  (=  F.)  franc,  ‘free’,  fr.  ML.
Francus,  ‘Frank’,  fr.  Frankish  *Frank,  ‘a  Frank’ (rel.  to  OHG.  Franko,  OE.  Franca,  of  s.m.), whence  also  F.  France,  orig.  ‘the  land  of  the Franks’.  In  the  territory  formerly  called  Gaul the  Franks  were  looked  upon  as  the  free  nation par  excellence  (whence  the  sense  development of  F.  franc).  Cp.  franc,  franchise.  Franco-,  Frank, French.  Cp.  also  frankalmoign,  franklin. Derivatives:  frank-ty,  adv. ,  frank-ness,  n.
Frank,  n.,  member  of  a  West  Teutonic  people.  — OHG.  Franko,  rel.  to  OE.  Franca.  See  frank, adj.
frank,  tr.  v.,  to  free  (whence  to  frank  a  letter,  lit. ‘to  exempt  a  letter  from  charge’).  —  Fr.  frank, adj.
frank,  n.,  signature  showing  that  a  letter  is  free of  charge.  —  Fr.  prec.  word, frankalmoign,  ftankalmoigne,  frankalmoin,  n., perpetual  tenure  of  land  by  a  religious  cor¬ poration. —  AF .  franke  almoigne,  lit.  ‘free  alms’. AF.  franke  is  fern,  of  frank,  which  corresponds to  OF.  franc.  See  frank,  adj.  AF.  almoigne  cor¬ responds  to  OF.  almosne,  F.  aumone.  See  alms. Frankenstein,  n.  —  Name  of  hero  in  a  novel  by Mary  Wollstonecraft  Shelley  (1818),  who  creates a  monster  which  kills  him. frankincense,  n.  —  OF.  franc  encens,  fr.  franc, ‘free’  (here  used  in  the  sense  of  ‘pure’),  and encens,  ‘incense’.  See  frank,  adj.,  and  incense, franklandite,  n.,  sodium  calcium  borate  (mineral.)
—  Named  after  the  English  chemist  Sir  Edward
Frankland  (1825-99).  For  the  ending  see  subst. suff.  -ite.
franklin,  n.,  a  small  landowner.  —  ME.  fran- kelein  (cp.  ML.  franchilanus),  formed  fr.  frank, ‘free’,  and  -lein,  a  suff.  of  Teut.  origin  (occurring also  in  ME.  chamberlein,  ‘chamberlain’).  See frank,  adj.,  and  -ling.
franklinite,  n.,  a  magnetic  oxide  of  iron  (mineral.) —  Named  after  Franklin  Furnace  in  New  Jer¬ sey,  where  it  was  discovered.  For  the  ending  see subst.  suff.  -ite.
frankpledge,  n„  a  system  by  which  the  members of  a  tithing  were  made  responsible  for  one  an¬ other’s  behavior.  —  AF.  franc  plege,  lit.  ‘free pledge’,  mistranslation  of  OE.  fridborh,  ‘peace pledge’,  in  which  the  first  element  was  confused with  OE.  freo,  ‘free’.  See  belfry  and  pledge, frantic,  adj.,  1)  insane  (archaic)',  2)  frenzied; furious.  —  ME.  f renet  ike,  frantik ,  fr.  OF.  frene- tique  (F.  frenetique),  fr.  L.  phreneticus,  fr.  Gk. 9psvmx6i;,  ‘mad,  delirious,  frantic’.  See  phre¬ netic.
Derivatives :  frantic-al-ly,  frantic-ly,  adv.,  fran- tic-ness,  n.
frap,  tr.  v.,  to  bind  firmly  (naut.)  —  OF.  fraper (F.  frapper),  ‘to  strike;  to  bind  firmly,  trap’, prob.  of  imitative  origin.  Cp.  next  word, frappe,  adj.,  iced,  frozen  (said  of  beverages).  — F.,  pp.  of  frapper,  ‘to  strike’.  See  prec.  word. Frasera,  n.,  a  genus  of  plants  of  the  gentian family  ( bot .)  —  ModL.,  named  after  the  Scottish botanist  John  Fraser,  (1750-1811). frass,  n.,  refuse  or  excrement  left  by  insect  lar¬ vae.  —  G.  Frass,  ‘a  devouring’,  in  gradational relationship  to  G.fressen,  ‘to  devour’.  See  fret, ‘to  eat  away’.
=== AHD watkins ===
321:yawn, gape: BAY2, BEVEL; ABASH, ABEYANCE. 2. Possibly Vulgar Latin *abbaidre (> Old French (a)baiier), to bay: BAY‘*.] [battuere. To beat. Latin verb of unknown origin. (BATE?), BATTER!, (BATTER’), (BATTERY), BATTLE; ABATE, COMBAT, DEBATE, (RABBET), (REBATE?), (RE- BATO).] bel-. Strong. 1. Suffixed o-grade form *bol-iyo- in Russian bol’shoi, large: BOLSHEVIK. 2. Prefixed form *dé-bel-i- (dé-, privative prefix; see de-), “without strength,” in Latin débilis, weak: DEBILITATE, DEBILITY. [Pok. 2. bel- 96.] bend-. Protruding point. 1. Germanic *pannja-, “struc- ture of stakes,” in Old English penn, pen for cattle: PEN2. 2. Germanic *pund- possibly in Old English pund- (> Middle English pound), pundfald, enclosure for stray animals: POND, POUND3; IMPOUND, PINFOLD. 3. Germanic *pin- in Old English pintel, penis: PINTLE. [Pok. bend- 96.) beu-'. Also bheu-. Appears in words loosely associated with the notion “to swell.” I. Root form *beu-. 1. Ger- manic *puk- in: a. Old English pocc, pustule: POCK; b. Old French po(u)che and Old North French poke, bag: POACH!, POCKET, POKE3, POUCH, (PUCKER). 2. Old Eng- lish pyffan, to blow out: puFF. 3. Old English -piite, “fish with large head” (in aele-piite, eelpout): pouT?. II. Root form *bheu- with various Germanic derivatives. 1. Old English bdsm, bosom: Bosom. 2. Old English biic, belly, pitcher: BUCKBOARD. 3. Frankish *biak (> Old French buc), trunk of the body: TREBUCHET. 4. Old English bye), pustule: BorL?. 5. German dialectal baustern, to swell, akin to the source of Middle English bost, a bragging: BoasT!. III. Root form *beu-. 1. Latin bulla, bubble, round object, amulet (> Old French boule and Spanish bola, ball): BILL!, BILLET!, BOLA, BOULE?, BOWL’, (BULL?2), BULLA, BULLATE, BULLET, (BULLETIN); BOULE- VERSEMENT. 2. Latin bullire (> French bouiller), to bubble, boil: BOIL!, BOUILLON, BUDGE!, (BULLION), BULLY?; BOUILLABAISSE, EBULLIENCE, GARBOIL, PAR- BOIL. 3. Possibly Latin bucca (> Old French boucle, buckle, curl, and Spanish boca, mouth), (inflated) cheek: BOCACCIO, BOUCLE, BUCCAL, BUCKLE!, BUCKLE?; DE- BOUCH, DISEMBOGUE, EMBOUCHURE. 4. Greek boubén, groin, swollen gland: BUBO. [Pok. 2. beu- 98.] beu-2. Root imitative of muffled sounds. 1. Latin bitié (perhaps > Old French butor), bittern: BITTERN!. 2. Latin bited, a kind of hawk: BUZZARD. [Pok. 1. b(e)u- 97.] bha-'. To shine. Contracted from *bhas-. 1. Germanic *baukna-, beacon, signal, in: a. Old English béac(e)n, beacon: BEACON; b. Old English denominative bécnan, biecnan, to make a sign, beckon: BECKON. 2. Perhaps Germanic *bazja-, berry (< “bright-colored fruit”), in Old English berie, berige, berry: BERRY. 3. Germanic *bandwa-, “identifying sign,” banner, standard, sash, also “company united under a (particular) banner,” in: a. Spanish banda, sash: BANDOLEER; b. Late Latin ban- dum, banner, standard: BANNER, (BANNERET). 4. Suf- fixed form *bhaw-es- in Greek phds (stem phét-), light: PHOS-, PHOT, PHOTO-; PHOSPHORUS. 5. Extended and suffixed form *bhan-yo- in Greek phainein, “to bring to light,” cause to appear, show, and phainesthai (passive), “to be brought to light,” appear: FANTASY, (PANT), PHANTASM, (PHANTOM), PHASE, PHENO-, PHENOMENON; DIAPHANOUS, EMPHASIS, EPIPHANY, HIEROPHANT, PHAN- EROGAM, (PHANTASMAGORIA), PHOSPHENE, SYCOPHANT, THEOPHANY, (TIFFANY). [Pok. 1 bha@- 104.] bha-2. To speak. Contracted from *bhaa-. 1. Latin fari, to speak: FATE; AFFABLE, (FANTOCCINI), INEFFABLE, IN- FANT, (INFANTRY), PREFACE. 2. Greek phanai, to speak: -PHASIA; PROPHET. 3. Suffixed form in Germanic *ban- wan, *bannan, to speak publicly (used of particular kinds of proclamation in feudal or prefeudal custom; “to proclaim under penalty, summon to the levy, declare
474:(Frankon-. Frank (member of a Germanic tribe), “jave- lin.” Germanic root. 1. Frankish *Frank-, Frank, bor- rowed into Late Latin as Francus, Frank: (FRANK}), FRANK. 2. Derivative adjective *frankiskaz, of the Franks, in Old English frencisc, French: FRENCH.]
484:géi-'. To sprout, split open. Contracted from *geoi-. Zero-grade form *gi- (< *gis-) in: a. Germanic *ki-nan in Old English cine, cinu, cleft, ravine cut by a stream: CHINK}; b. Germanic *ki-ddn- in Frankish *kid-, sprout, young shoot, in Old French cion, shoot: scron. [Pok. géi- 355.]
494:vine, grape: GRAPE; c. Old French grapon, grapnel: GRAPNEL; d. Old French grape, a hook: GRAPPLE; e. Ital- ian dialectal grappa, vine stem, brandy: GRAPPA. 2. Old English crump, crumb, crooked, bent, stooping: CRUM- MIE, CRUMPET, (CRUMPLE). 3. Low German krimpen, to wrinkle: CRIMP!. 4. Middle Dutch crampe, hook, and Frankish *kramp, hook: cramMpP?. 5.Old High German krampfo, a cramp, akin to the Germanic source of Old French crampe, cramp: CRAMP!. 6. Old English crypel, a cripple: CRIPPLE. 7. Germanic *kreupan in Old English créopan, to creep: CREEP. 8. Middle Low German krink, a ring: CRINGLE. 9. Germanic *krengan in Old English cringan, to yield: CRINGE. 10. Middle Dutch crinkelen, akin to Middle English crinkelen, to make kinks in: CRINKLE. 11. Old Norse kriki, a bend, nook: CREEK. 12. Old Norse krékr, a hook: cRooOK. 13. Frankish *krok- (> Old French croc), a hook: CROCHET, (CROCKET), (CROQUET), (CROUCH); ENCROACH. 14. Old English crycc, (bent) staff, crutch: CRUTCH. 15. Old French crosse, crook: CROSIER, LACROSSE. 16. Middle Dutch crulle, curly: CRULLER, CURL. 17. Old English cranc-(stzf), a weaving implement: CRANK}. 18. Norwegian krake, a sickly beast, akin to the source of Middle English crok, an old ewe: cRocK3, 19. Old Norse karpa, to boast: CaRP!, 20. Middle Dutch kroes, curled, akin to the source of Old French grosele, gooseberry: GROSSULARITE. II. Words meaning ‘“‘a rounded mass, collection; a round object, vessel, container.” 1. Old English cruma, a frag- ment: CRUMB. 2. Frankish *kruppa, rump, akin to the Germanic source of Old French croup, rump: CROUP?, (CROUPIER), CRUPPER. 3. Old English cropp, cluster, bunch, ear of corn: crop. 4. Italian gruppo, an assem- blage: Group. 5. Old English crocc, pot: CROCK}. 6, Mid- dle Dutch cruyse, pot: CRUSE. 7. Old English cribb, manger: CRIB. 8. Old English cradel, cradle: CRADLE. 9. Frankish *kripja, cradle, akin to the Germanic source of Old French cre(s)che, crib: CRECHE. 10. Old English creet and Old Norse kartr, wagon: CART. 11. Old English croft, small enclosed field: crort. [Pok. 3. ger- 385.] gerbh-. To scratch. 1. Germanic *kerban in Old English ceorfan, to cut: CARVE. 2. Zero-grade Germanic form *kurbiz in Old English cyrf, a cutting (off): KERF. 3. Variant form *grebh- in: a. Germanic *krab(b)- in Old English crabba, a crab: CRAB}; b. Germanic *krabiz- in Old French crevise, crayfish: CRAYFISH; C. perhaps Ger- manic *krab- in Old Norse krafla, to crawl: CRAWL. 4. Zero-grade form *grbh- in Greek graphein, to scratch, draw, write, and gramma (< *grbh-mn), a picture, writ- ten letter, piece of writing, and grammé, a line: GRAF- FITO, GRAM!, -GRAM, GRAMMAR, GRAPH, -GRAPH, -GRAPHER, GRAPHIC, -GRAPHY; AGRAPHA, AGRAPHIA, DIAGRAM, EPIGRAM, (EPIGRAPH), GRAPHITE, ICONOGRA- PHY, PARAGRAPH, PROGRAM, PSEUDEPIGRAPHA, TETRA- GRAMMATON, TOPOGRAPHY. [Pok. gerebh- 392.] [gerere. To carry, carry on, act, do. Latin verb of un- known origin. Oldest form ges-, past participle gestus. GERENT, GERUND, (GEST), GESTATION, (GESTICULATE), GESTURE, JEST; ARMIGER, BELLIGERENT, (CONGERIES), CONGEST, DIGEST, EGEST, INGEST, REGISTER, SUGGEST, VELIGER.] gere-'. To grow old. 1. Suffixed lengthened-grade form *géro-s- in Greek géras, old age: AGERATUM, CALOYER, GERIATRICS. 2. Suffixed form “gera-ont- in Greek geron (stem geront-), old man: GERONTO-. [Pok. ger- 390.] gere-2. To cry hoarsely; also the name of the crane. I, Words meaning “‘to cry hoarsely”; also words denoting the crow. 1, Germanic *kré- in: a. Old English crawe, a crow: CROW}; b. Old English crdwan, to crow: CROW?; c. Old English cracian, to resound: CRACK; d. Middle Dutch krdken, to crack: CRACKNEL; @. Old Norse kraka, a crow: CRAKE. f. Middle Dutch krdnen, to groan, la- ment: CROON. 2. Possibly (but more likely imitative) Germanic *kur(r)- in Old Norse kurra, to growl, akin to Middle English curre, cur: cur. II. Words denoting a
583:heard, hard: HARD; b. Frankish *hard, hard, perhaps the source of Old French estandard, rallying place: STAN- DARD; Cc. Old French hardir, to make hard: HARDY}. 2. Extended zero-grade form *krt-es- in Greek kratos, strength, might, power: -cracy. II. Basic form *kar- in derivatives referring to things with hard shells. 1. Possi- bly Latin carina, keel of a ship, nutshell: CAREEN, CARINA. 2. Possibly Greek karuon, nut: KARYO-; EU- CARYOTE, GILLYFLOWER, SYNKARYON. 3. Reduplicated form *kar-kr-o dissimilated to Latin cancer, crab: CAN- CER, CANKER, CHANCRE. 4. Suffixed form *kar-k-ino- in Greek karkinos, cancer, crab: CARCINO-, CARCINOMA; (CARCINOGEN). [Pok. 3. kar- 531.]
606:small hollow: HAUGH; e. Dutch holster, holster, (< “that which covers”): HOLSTER. 2. Suffixed Germanic form *hulfti- in Medieval Latin hultia, protective covering: HOUSING?. 3. Suffixed form *kl-to- in Latin occultus (see III. 5. below). 4. Extended form *kld (< *kl-) in Latin clam, in secret: CLANDESTINE. 5. Suffixed variant form *kal-up-yo- in Greek kaluptein, to cover, conceal: Ca- LYPSO, CALYPTRA; APOCALYPSE, EUCALYPTUS. III. Full-grade form *kel-. 1. Germanic *helmaz, “‘protec- tive covering,” in: a. Old English helm, protection, cover- ing: HELM?; b. Frankish *helm, helmet, akin to the source of Middle English helmet, helmet: HELMET. 2. Latin occulere (part participle occultus; see Il. 4. above), to cover over (ob-, over; see epi): OCCULT. 3. Suf- fixed form *kel-os- in Latin color, color, hue (< “that which covers”): COLOR. 4. Suffixed form *kel-nd in Latin cella, storeroom, chamber: CELL, CELLA, CELLAR, CELLARER; (RATHSKELLER). 5. Suffixed form *kel-yo- in Latin cilium, lower eyelid: CILIUM, SEEL; SUPERCILIOUS, (SUPERCILIUM). IV. Lengthened-grade form *kél-d- in Latin céldre, to hide: CONCEAL. See extension klep-. [Pok. 4. kel- 553.] kel-3. To drive, set in swift motion. Hypothetical base of various loosely connected derivatives. 1. Extended form *kelt- or *keldh- possibly in Germanic *haldan, to drive flocks, keep or pasture cattle, in: a. Old English healdan, to hold, retain: HOLD!; b. Old High German haltan, to stop, hold back: HALT!; c. Middle Dutch houden, to hold: AVAST. 2. Suffixed form*kel-es- in: a. Latin celer, swift: CELERITY; ACCELERATE; b. possibly further suffixed form *keles-ri- in Latin celeber, (of a place) much fre- quented, hence famous: CELEBRATE, CELEBRITY. 3. Suf- fixed zero-grade form *kl-on- in Greek klonos, turmoil, agitation: CLONUS. [Pok. 5. kel- 548.] kel-4. To lean, tilt. Germanic *halthjan in Old English hieldan, to tilt: HEEL2. [Pok. 2. kel- 552.] kel-5. Gray, black, dark. Suffixed form *kel-omb(h)- in Latin columba, dove, pigeon: COLUMBA, COLUMBARIUM, COLUMBINE, CULVER. [Pok. 4. kel- 547.] kel-*, To be prominent; hill. 1. Zero-grade form *k/- in: a. suffixed Germanic form hul-ni- in Old English hyll, hill: HILL; b. suffixed Germanic form *hul-ma- in Old Norse holmr, islet in a bay, meadow: HOLM. 2. Suffixed form *kel-d- in Latin excellere, to raise up, elevate, also to be eminent (ex-, up out of; see eghs): EXCEL. 3. O-grade form *kol- in: a. Greek kolophén, summit: COLOPHON; b. suffixed form *kol(u)men- in Latin culmen, top, summit: CULMINATE; C. extended and suffixed form *kolumna in Latin columna, a projecting object, column: COLONEL, COLONNADE, COLUMN. [Pok. 1. kel- 544.] kel-7. To prick. Germanic *hulin- in Old English holen, holly (from its spiny leaves): HOLLY. [Pok. 2. kel- 545.] kel-®. To deceive, trick. Extended form *kelu-, variant *kalu-, in: a. Latin calvi, to deceive, trick: CALUMNY, CHALLENGE; b. Latin cavilla (< *calvilla), a jeering: CAVIL. [Pok. Rél- 551.] kelb-. To help. Germanic *helpan in Old English helpan, to help: HELP. [Pok. kelb- 554.] kele-1. Warm. Variant *klé-, contracted from *kleo-. 1. Suffixed variant form *k/é-wo- in Germanic *hléwaz in Old English hléo, hléow, covering, protection (as from cold): LEE. 2. Suffixed zero-grade form *kip-é- in: a. Lat- in calére, to be warm: CALENTURE, CHAFE; DECALES- CENCE, NONCHALANT, RECALESCENCE; Db. Latin derivative adjective calidus, warm (> French chaud, warm): CALDRON, CAUDLE, (CHOWDER); CHAUDFROID, SCALD'. 3, Suffixed zero-grade form *fl-os- in Latin calor, heat: CALORIC, CALORIE; CALORECEPTOR, CALO- RIFIC, CALORIMETER, CALORIMETRY. [Pok. 1. kel- 551.] kele-2. To shout. I. Variant form *kld- (< *klaa-). 1. Ger- manic Aljé- in Old English hléwan, to roar, low: Low?. 2. Suffixed form *k/d-mé- in Latin clamare, to call, cry out: CLAIM, CLAMANT, CLAMOR; ACCLAIM, DECLAIM, EXCLAIM, PROCLAIM, RECLAIM. II. O-grade form *kob-.
757:merg-. Boundary, border. 1. Germanic *mark-, bound- ary, border territory; also to mark out a boundary by walking around it (ceremonially “beating the bounds”); also a landmark, boundary marker, and a mark in general (and in particular a mark on a metal currency bar, hence a unit of currency); these various meanings are widely represented in Germanic descendants and in Romance borrowings: a. Old English mearc, boundary, landmark, sign, trace: MARK}; b. Middle Dutch mark, border: MAR- GRAVE; ¢. Old French marc, marche, border country: MARCH?, (MARQUEE), MARQUIS, (MARQUISE); d. Late and Medieval Latin marca, boundary, border: MARCHIONESS; e. Old Italian marcare, to mark out: DEMARCATION; f. Old English marc and Middle High German marke, a mark of weight or money: MARK?; g. Swedish mark, a mark of money: MARKKA. 2. Germanic *markja-, mark, border, in Old Norse merki, a mark, possible source of Old French marque, a mark: MARQUETRY; REMARK. 3. Germanic denominative verb *mark6dn in Frankish *markoén, to mark out (> Old French march(iJer, to trample): MARC, MARCH!, 4, Latin margo, border, edge: MARGIN. [Pok. mereg- 738.]
904:saus-. Dry. 1. Extended form *sauso- in Germanic *sau- saz in: a. Old English séar, withered: SEAR!, SERE!; b. Frankish *saur, dry, whence Old French saur, sor, red-brown: SORREL?; SURMULLET. 2. Suffixed form *saus-t- in Greek austéros, harsh: AUSTERE. [Pok. saus- 880.]
940:*skerb(h)-, *skreb(h)-. 1. Germanic *skarpaz, cutting, sharp, in: a. Old English scearp, sharp: SHARP; b. Gothic skarp6, pointed object, akin to the possible Germanic source of Italian scarpa, embankment: scarp. 2. Ger- manic *skrap- in: a. Old Norse skrap, “pieces,” remains: SCRAP!; b. Old Norse skrapa, to scratch: SCRAPE. 3. Ger- manic skrab- in: a. Middle Dutch schrabben, to scrape: SCRABBLE; b. Middle Dutch schrobben, to scrape: SCRUB!. 4, Germanic *skrub- in Old English scrybb, shrub (< “rough plant”): SHRUB. 5. Latin scrobis, trench, ditch: SCROBICULATE. 6. Latin scrdfa, a sow (< “rooter, digger”): SCREW, SCROFULA. [Pok. 4. sker-, Section I. 938.] sker-2. To leap, jump about. Perhaps same root as sker-3. 1. Extended form “skerd- in Germanic *skert- in Middle High German scherzen, to leap with joy: SCHERZO. 2. O-grade variant form *kor- in Latin coruscdre, to vibrate, glisten, glitter: coRUSCATE. [Pok. 2. (s)ker- 933.] sker-3. Also ker-. To turn, bend. Presumed base of a number of distantly related derivatives. 1. Extended form *(s)kreg- in nasalized form *(s)kre-n-g- in: a. Ger- manic *skrink- in Old English scrincan, to wither, shrivel up: SHRINK; b. variant *kre-n-g- in Germanic *hrunk- in (i) Old Norse hrukka, a crease, fold: RUCK? (ii) Frankish *hrunkjan, to wrinkle (> Old French fronce, pleat): FLOUNCE!, 2, Extended form *(s)kregh- in nasalized form *skre-n-gh- in Germanic *hringaz, something curved, circle, in: a. Old English Aring, a ring: RING!; b. Old French renc, reng, line, row: RANCH, RANGE, RANK}, RINK; ARRANGE, DERANGE; C. Middle Dutch rinc (com- bining form ring-), a ring: RINGHALS. 3. Extended form *kreuk- in Germanic “*hrugjaz in: a. Old English hrycg, spine, ridge: RIDGE; b. Old High German hrukki, back: RUCKSACK. 4. Suffixed variant form *kur-wo- in Latin curvus, bent, curved: CURB, CURVATURE, CURVE, CUR- vET. 5. Suffixed extended form kris-ni- in Latin crinis (< *crisnis), hair: CRINITE; CRINOLINE. 6. Suffixed ex- tended form *kris-td- in Latin crista, tuft, crest: CREST, CRISTA, CRISTATE. 7. Suffixed extended form *krip-so- in Latin crispus (metathesized from *cripsus), curly: CREPE, CRISP, CRISPATE. 8. Extended expressive form *kriss- in Latin crisdre, (of women) to wiggle the hips during copulation: crissuM. 9. Perhaps reduplicated form *ki-kr-o- metathesized into Greek krikos, a ring (> Latin circus, ring, circle): CIRCA, CIRCLE, CIRCUM-, SEARCH; CRICOID. 10. Suffixed o-grade form *kor-6no- in Greek kordnos, curved: (CORONA), CROWN; CORONOID. 11. Suffixed variant form *kur-to- in Greek kurtos, bent: KURTOSIS. [Pok. 3. (s)ker- 935.] sker-4. Excrement, dung. Extension of sek-, “to cut, separate,” hence “to void excrement.” 1. Form *sk-6r- in Greek skdr (genitive skatos < *sk-nt-), dung: SCATO-, SCORIA, SKATOLE. 2. Extended form “skert- in taboo metathesis *sterk-os- in: a. Latin stercus, dung: STERCO- RACEOUsS; b. variant forms *(s)terg-, *(s)treg- in Germanic *threkka- in Middle High German dréc, dung: DRECK. [Pok. sker-d- 947; 8. (s)ter- 1031.] skerbh-. Also skerb-. To turn, bend. Extension of sker-3. 1. Variant form *skreb- in Germanic *skrip- in Old Norse skreppa, to slip, and derivative Old Norse skorpna, to shrink, be shriveled, akin to the probable Scandinavian source of Middle English scorchen, to scorch: SCORCH. 2. Nasalized variant form *(s)kre-m-b- in: a. Germanic *hrimp-, *hrump- in (i) Old English hrympel, wrinkle, fold: RIMPLE (ii) Middle Dutch rom- pelen, to wrinkle: RUMPLE (iii) Old French ramper, to climb, rear up: RAMP?; b. Germanic *skrimp- in (i) Mid- dle Low German schrempen, to shrink, wrinkle, perhaps akin to the possible Low German source of Middle English shrimp, pygmy, shrimp: SHRIMP (ii) Swedish skrympa, to shrink, perhaps akin to the possible Scandi- navian source of SCRIMP. 3. Variant form *kramb- in Greek krambé, cabbage (having wrinkled, shrunken
1172:*wer-ald., “life or age of man” (*-ald-, age; see al-3), in Old English weorold, world: woRLD; c. Frankish *wer- wulf, “man-wolf” (*wulf, wolf; see wikvo-), in French garou, werewolf: LOUP-GAROU. 2. Latin vir, man: VI- RAGO, VIRILE, VIRTUE, (VIRTUOSA), (VIRTUOSO); DECEM- VIR, DUUMVIR, TRIUMVIR. 3. Possibly Latin ciria, curia, court, if regarded as from *co-vir, “men together” (co-, together; see kom): CURIA. [Pok. uiro-s 1177.] wleik-. To flow, run. Zero-grade form *wlik-. 1. Adjective *wlik-u-, wet, in: a. suffixed form *wlik-w-d- in Latin liquare, to dissolve: LIQUATE; b. suffixed form *wlik-w-é- in Latin liquére, to be liquid: LIQUESCENT, LIQUID, LIQUOR; DELIQUESCE, LIQUEFY. 2. Suffixed form *wlik-s- in: a. Latin lixa, lye: LIXIVIATE; b. Latin prélixus, poured forth, stretched out in front, extended (pro-, forth; see per’): PROLIX. [In Pok. leiku- 669.] wlkwo-. Wolf. 1. Germanic *wulfaz in: a. Old English wulf, wolf: WOLF; b. Middle Dutch wolf, wulf, wolf: AARDWOLF; Cc. Old High German wolf, wolf, in German Wolfram, tungsten: WOLFRAM; d. Frankish *wulf, wolf (see wi-ro-). 2. Taboo variant */upo- in Latin lupus, wolf: LOBO, LUPINE!, LUPINE?; LOUP-GAROU. 3. Taboo variant *luko- in: a. Greek lukos, wolf: LYCANTHROPE, LYCOPO- piuM; b. Suffixed form */uk’-ya in Greek lussa, martial rage, madness, rabies (“wolf-ness”): LYTTA; ALYSSUM. [Pok. ulkvos 1178.] wip-6-. Fox. 1. Latin vulpés, fox: VULPINE. 2. Taboo variant *slépek- in Greek alépéx, fox: ALOPECIA. [Pok. ulp-, lup- 1179.] wogYh-ni-. Plowshare, wedge. 1. Probably Germanic *wagjaz in Old English wecg, wedge: WEDGE. 2. Prob- ably Latin vdmer, plowshare: vOMER. [Pok. wog¢hni-s 1179.] wokso-. Wax. Related to weg-!. Germanic *wahsam in Old English wex, weax, wax: WAX!. [Pok. uokso- 1180.] wopsa. Wasp. Metathesized form *wospd. 1. Germanic *wosp- in Old English wesp, weps, wasp: wAsP. 2. Latin vespa, wasp: VESPIARY. [Pok. yobhsd 1179.] wos. You (plural). Latin vds (> Old French vous), you: RENDEZVOUS. [In Pok. 1. iu- 513.] wrad-. Branch, root. I. Basic form *wrdd- in Germanic *wrét- in Old Norse rét, root: ROOT!; RUTABAGA. II. Zero-grade form *wred-. 1. Germanic *wurtiz in: a. Old English wyrt, plant, herb: wort; b. German Wurzel (< *wurzwala, rootstock; *-wala, a roll, round stem; see wel-3), root: MANGELWURZEL. 2. Latin rddix, root: RACE3, RADICAL, RADICLE, RADISH, RADIX; DERACI- NATE, ERADICATE. 3. Suffixed form *wrod-mo- in Latin rdmus, branch: RAMOSE, RAMUS; RAMIFY. 4. Suffixed reduced form *wr(e)d-ya perhaps in Greek rhiza, root: RHIZO-, RHIZOME; COLEORHIZA, LICORICE, MYCORRHIZA. [Pok. ufe)rad- 1167.] wragh-. Thorn, tip. Greek rhakhis, ridge, spine: RACHIS. [Pok. 1. uragh- 1180.] wreg-. To push, shove, drive, track down. I. Basic form *wreg- in Germanic *wrekan in: a. Old English wrecan, to drive, expel: WREAK; b. Old Norse rek (older form urek), wreckage, akin to the Scandinavian source of Anglo-Norman wrec, wreck: WRECK. II. O-grade form *wrog-. 1. Germanic *wrakjén-, “pursuer, one pursued,” in: a. Old English wrecca, exile: WRETCH; b. Frankish *wrakjo, “one pursued, an exile,” perhaps in French garce, a girl: GASKET. 2.Germanic *wrakaz in: a. Old English wrzc, exile, punishment, and Middle Dutch wrak, wreckage: WRACK}; b. Swedish rak, wreckage, akin to the source of Middle English rak, mass of driven clouds: RackK®. III. Zero-grade form “wrg-eyo-, “urg-eyo- in Latin urgére, to urge, drive: URGE. [Pok. ureg- 1181.] wrég-. To break. Suffixed form *wrég-nu- in Greek rhégnunai, to burst forth: -RRHAGIA. [Pok. urég- 1181.] [wrod-. Rose. A word (not common Indo-European) of unknown origin. 1. Suffixed form *wrod-o- in Greek rhodon, rose: RHODO-; (RHODIUM). 2. Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa, rose:
1537:Fra _bhrater- FRACTED bhreg- FRACTION bhreg- FRACTIOUS bhreg- FRACTURE bhreg- FRAGILE bhreg- FRAGMENT bhreg- FRAGRANT bhrag- FRAIL! bhreg- FRANGIBLE bhreg- FRANK! Frankon- FRANK Frankon- FRANTIC gWhren- FRATERNAL bhrater- FRATRICIDE bhrater- Frau pert FRAUGHT @ik- FRAULEIN pert FRAXINELLA bhereg- FRAY? bhréi- FRECKLE (S)preg- FREE pri-
1538:FREEZE preus- FREIGHT 6@ik- FREMITUS bhrem-1 FRENCH Frankon- FRENETIC gWhren- FRENULUM ghrendh- FRENUM ghrendh- FRENZY gWhren- FREQUENT bhrekw- FRET! ed-
```


## [2026-09-05T20:33:20.273Z] TOOL CALL #11: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 164 -l 164 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg164 && ls -la $S/",
 "description": "Render page 164"
}
```


## [2026-09-05T20:33:21.841Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN farsang ===\"; grep -n -i 'farsang\\|frasang\\|parasang' HRN.txt | head -20; echo \"=== PHD ===\"; grep -n -i 'frasang\\|frasang' PHD.txt PHD_mackenzie.txt | head -20; echo \"=== HUB ===\"; grep -n -i 'farsang\\|frasang' HUB.txt | head",
 "description": "Grep Horn, MacKenzie, Hübschmann for farsang"
}
```


### [2026-09-05T20:33:22.667Z] TOOL RESULT

```
total 15908
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:33 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 1032029 Sep  5 16:13 bqt362_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66991 Sep  5 16:16 pg135.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60631 Sep  5 16:11 pg147.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


### [2026-09-05T20:33:22.735Z] TOOL RESULT

```
=== HRN farsang ===
7128:818. ferseng 'Parasange', arab. LW. farsax»
7129:ap. 7Taf)f((r(iyy7j; phl. frasang bezw. farsany (Men.,
=== PHD ===
PHD.txt:324:farr- ER frasang
PHD.txt:325:farr-, v. xwarrah. Farrūbāģ [plwb(’)g] the first major Fire of Sasanian Eran, that of priests and nobles. farrox [plhw' | M prwx, N ~] fortunate, blessed, happy. ~ih: fortune, joy, happiness. filāsūfā [pyPswkp!y] philosopher. frabih [plpyh | (P frbyw), N farbih] fat, stout. Fradadafš [pldtpš = Av. fradašafšū-| the south-eastern continent of the earth. fradág [MHL < A mhr; ИРА! | N farda] tomorrow. frādahišnīh [pP dhšnyh] increase, progress. fradom [AWLA < Ar. !?wD; pltwm | (M prtwm)] first. ~th: first, beginning. fragan [plk?n'] base, foundation; origin. fragandan, fragan- [plkn-dn'} lay foundations. frahang [pl’hng | N farhang] education; knowledge. --estàn [-st?n!] school. frahanj-, v. frahixtan. frahist [p/h(y)st! | (M pryst)] most (superlative of freh), frahixtag [plhhtk' | N farhixta] educated, trained, skilled. frahixtan, frahanj- [plhhtn', pDhnc- | P frhynj-, N far~] educate, teach, instruct. framādār [рж?РЦ commander, ruler, chief. framān [pim^n! | M frmn, N farman] order, command; a minor degree of sin. ~-burdar [-bwlt?l | N -bardār] obedient, submissive. framāy-, ~išn, v. framüdan. framds [bl(?)mwš | M pr’mws, N farámos] forgotten. framošidan [plmwšytn'] = framuštan. framüdan, framāy- [plmwin', plm'd- | M prm'dn, prmy-, N far~] order, command. — $n: order, commandment. frāmuštan, frāmēš- [pl(?)mws-in' | M prhmwst, pr’mwi-, N fard~] forget. franaftan, *franam- [pinptn!, *plnm- | M prnpt, prnm-] go, proceed, depart. franāftan, franām- [pin!ptn!, pli m- | P fri m-] 1. lead, conduct, re- move, promote; 2. profess, propagate (faith). ~išn: removal, promotion, profession. frarast [p/”Pst'] a cubit (18 in.). fràrón [p lwn'] righteous, honest. ~ih : righteousness, honesty. frasang [plsng | N farsang) parasang (4 Roman miles).
PHD.txt:396:hannàm [%7m | = M] = handām. Harborz [Albwic | N Alburz] the mountain range surrounding the world. harg [hlg | cf. M bie, Аг. xarj, xaraj] duty, tribute; work, effort. *harrób- [hlwp- | M hrwb-] collect, gather. —išn(ih): collection, gathering. har(w) [KRA < A АР; hl | M been, N har] all, each, every. harwin [%/wyx! | M hrwyn] pl. al. harwisp [Ahlwsp! | M hrwsp] all. ~in [-yn'] pl. all. harzag [hick! | N harza] loose, free. has®r [Ps] = Av. háóra-] a measure of time (unequal hour, ze of day- light); a measure of length (— frasang, or 1 frasang, 1 mile). haspin [hspyn! | = M] rest, repose. hast, ~ih [AY T!, -yh] = tast, ~ih. hašāģird [kP klt! | M APgyrd, N šāgtrd] disciple, pupil. hast [h#! | = M, N ~] eight. ~ad [80 | N ~] eighty. ~dah [лаһ | N ~, higdah] eighteen. lhàwan [h?wn! | N +] a mortar. *hawan [/?zn! = Av. háwani-] the morning gdh. hāwand [/?wnd | M ÞPw(y)nd] like, similar. ^h: likeness, similarity. hāwišt [h’wst'] disciple, pupil. ~ih: disciplehood. haxt [h()At'] thigh, haunch, hip. hāxtan, hàz- [/7htn', h'e-] lead, guide, persuade, convert. ~išn: persuasion, conversion. hazār [1,000, hel | M h?r, N ~] thousand. ~ag LEI | N ~a] millennium. hazzān [?/h2’n'] tomb, ossuary. hên [Ayn! | M hyyn] army. ~ih: attack, aggression. hérbed [%y/pt! | N hérbud] teacher-priest. ~ih: priestly office. hērbedestān [hylptst’n'] priestly school. ~ih: priestly studies. hérig [hylyk' | N h/xéri] iris, wallflower. hézag [Ayck! | (M hyjg), N лег] pail. hil-, —išn, v. histan. hindüg [Andwk! | M hyndwg, N hindi] Indian. ~ап [-°п!] India. hištan, hil-, (P hirz-) [S BKWN-tn! < A У #9; (hlc-) | M hyštn, hyl-, (P Ayrz-), N —] let, leave, abandon, pardon, set, appoint. ~išn: pardon, loosing. hixr [hyhl] excrement. hixtan, hanj- [Ayhtn', hne- | P hxt] draw (water).
PHD.txt:3040:parasang frasang.
PHD.txt:4434:ii. = frasang
PHD.txt:4435:I frasang == 4 ‘miles’ ‘parasang’
PHD.txt:4682:frasang parragig pargan- parwar pargandan pargüd frég, parig frest- fréstadan fréstidan pargast fréstag fréb
PHD_mackenzie.txt:2865:   light); a measure of length (= frasang, or 1- frasang, I mile).
PHD_mackenzie.txt:7243:parasang frasang.                         (u)spurrig.
PHD_mackenzie.txt:8076:                       ii.       = frasang
PHD_mackenzie.txt:8077:            I frasang            = 4 'miles'              'parasang'
PHD_mackenzie.txt:8659:frawahr                      ~~Q)        frasang                       -,~Q)
=== HUB ===
7473:=-• zd. duy^ saite; farsang = phi. frasang naQaaiyyric,
```


## [2026-09-05T20:33:31.504Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN 818 ===\"; sed -n '7120,7140p' HRN.txt; echo; echo \"=== HRN leaf for line 7128 ===\"; python3 -c \"\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=sum(len(l)+1 for l in lines[:7127])\nprint('leaf(0-based)=',t[:idx].count('\\f'))\n\"; echo \"=== HUB ctx ===\"; sed -n '7465,7480p' HUB.txt",
 "description": "Horn 818 and Hübschmann context"
}
```


## [2026-09-05T20:33:32.745Z] TOOL CALL #14: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg164.png"
}
```


### [2026-09-05T20:33:33.716Z] TOOL RESULT

```
=== HRN 818 ===
scheint im Pehlevi noch /ra-, nicht schon far- gesprochen zu sein.
Das Päzend lässt beide Möglichkeiten offen.
'j Justi' Thema /raj9J/M- *Füllc' rauss also fallen.- 182 -
817. fiv'i stallen 'schicken*.
ap. *fra + [^sta-, vergl. a.i. pra -\- l^stho- (Causat.)
'entsenden, entlassen'.
vergl. Sit'/, (ififcwul 'senden'; bei. sastay ^ n. sastay
(363).
818. ferseng 'Parasange', arab. LW. farsax»
ap. 7Taf)f((r(iyy7j; phl. frasang bezw. farsany (Men.,
Bund.).
819. firisfe 'Bote.
phlv. firisfak (Dat. d. 3, 15); chald. LVV. vXpnonp
(das de Lagarde fälschlich = np. pereste setzt) und
NOPIDI.?« (Ezra 4, 9), Hoffmann, Zeitschr. f. Assy-
riologie II, 55 (danach Ezra 5, 6 und 7, 6 zu emen-
diren).
Zu np. ßristäden (No. 817), vergl. skr. prasthita-
aufgebrochen, der sich aufgemacht hat'. Ein aw.
^frcfsfa- (aus ar. *prasth'td', vergl. KZ. 25, 56) ist
etwa als Grundform anzunehmen ^).

=== HRN leaf for line 7128 ===
leaf(0-based)= 203
=== HUB ctx ===
sal Mahr = zd. sareda-; surx Voth* = zd. suxra-,
ap. &uxra'; suxun^ suxan *Wort* aus iran. "^saxvan- = ap.
*&a(h)uvan' von &ah *sprechen, skr. gq^, zd. satlh; sang
*Stein, ap. a&angaina- *steinern ; sard 'kalt' = zd. sareta-;
saya *Schatten' = skr. chdya- (mit ch aus idg. k%) u. s. w.
Vgl. Horn 688 — 765. Ebenso in Zusammensetzungen :
afsan *Wetzstein , afsar 'Krone', pdsux *Antwort\ pasand
'angenehm' (oben p. 41), dsiidan ruhen*, duvSst *zweihundert'
=-• zd. duy^ saite; farsang = phi. frasang naQaaiyyric,
u. s. w.
Im Arm., Phi. und Paz. erscheint hier gleichfalls
stets 5.
Da es nicht wahrscheinlich ist, dass das aus iran. s
entstandene ap. d- schon im altesten Phi. wieder in s iiber-
ging, da vielmehr das im Phi. Paz. und Np. anlautende s
= iran. s ein ap. s voraussetzt, so ergiebt sich, dass hier
```


### [2026-09-05T20:33:34.069Z] TOOL RESULT

```

```


## [2026-09-05T20:33:34.067Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:33:59.157Z] TOOL CALL #15: Bash

```json
{
 "command": "echo \"=== KNT ===\"; grep -n -i 'frasang\\|parasang\\|Fra-sanga' data/verification/sources/refs/KNT.txt | head; echo \"=== BRT ===\"; grep -n -i 'frasa\\|parasang' data/verification/sources/refs/BRT.txt | head; echo \"=== HJB 352 area / FIRINGHEE ===\"; grep -n -i 'FIRINGHEE\\|Frank, s\\|^FRANK' data/verification/sources/refs/HJB.txt | head -20",
 "description": "Grep Kent, Bartholomae, Hobson-Jobson"
}
```


### [2026-09-05T20:33:59.253Z] TOOL RESULT

```
=== KNT ===
=== BRT ===
2729:Sing,  in  kollekt.  Sinn');  'ma  frasaocayähi\     Lavaquellen  enthaltend".    VgL   Bthl.IF.j. V.  *.  7  5 ;  /4-  7 ;  —  a  -man  y'äsamiha  V.  i8.       ■  24-  -  •>  NS.,  S  ^5- »9;  5-z;  — "'«ff  ■■  ^<»"  Y.J.2;  — '«ffJ'Taj«  j.    aezah-    n.    'Verlangen':     "zö    (AS.) baolulmca  Y.^'i,  7.26,  Äi,  22.3;  —  ''ma  J'isatim    aisahe   "sie  (beide)   kamen
3525:den  ist's  yü  andusat  *'tat'>  ajayaunia (sd.)  N.  54;  —  caiti  ta  syadhna  varlta .  .  fraSa  'ta  ■'  anusvarsta  aiAhat  hala I  syaohnavar»za  (sd.)  ,  .  "wie  vielfach  sind die  getanen  Taten  . .  —  begangen  (sind sie),  nicht  beglichen,  nicht  wieder  gut gemacht—:  es  werden  . ."  Y.i$.\.
4680:■jpB  k^rinaol  frasa  •iiyil  fralacat  (sd.)  Yt. 5.78.  a)  NS.  mit  folg.  obl.  Kasus  'ein- ander', mit  part.  Gen.:  asa  vi  'nyS  'inim vXvBnghaiR  "einer  von  euch  soll  den  andern an  Gerechtigkeit  zu  Übertreffen  suchen" Y.5J.  s;  —  am>sanqm  sp^ntanqm  ..yaeiqm 'iiiyS  'inyehe  urväntm  ami.vaenaiü  Yt y-84>  —  vgl.  aiiyd.anya:  2)  Du.  in Verbindung  mit  agta-  Du.  'hie  et  alter': yB  . .  amqsia  (sd.)  *x^ar5.a^aya  *alU  'nye (ADn.)'>  ^cikayatB  ". .  hoc  et  alterum  . ." ^'3  c;  —  atitari  *ha>:r>mcit  *<7Ä^(ADn.) 'nya  (ADm.)»>  itpaisat  "innerhalb  eines H.  soll  man  dies  (barfsman-  n.)  und  jenes (alsma-  m.)  suchen"  N.  log.  I  a)  mit
5368:"ka''  ski^  avam  *''ufrasatam  aparsam  Bh. /.8;  —  pasavJ'  karJ'  'ka"  abavJ'  Bh. /.  10.
6264:lich bezeichneten  Personen:  frasaoslrs ''Opa  Y.7/.1;  —  'sava  jämäspö  N.Ä9; —  "hraMaomm  "Az/a»?«  FrW.  2. 2 ;  i;  — gayehe  mary^nH  °s'aonSY.26.5,  Yt/J.87; 95-138'",  Y.7J.7,  2(7.5';  —  Vä«m tu'taspa  Vyt.  4s;  ~-  hvüvi  'laoni  Y\..i6. 'S; —  kt^yä  'saonyä  Yt./^.  139;  139— 141'*;  —  »nsvä  sräts.sps(,a  'saonä  {GD.} YL/^.  115;  115,124, 125,127'.  A)insbes. von  Zara'^ustra  (Spitama):  zatS  bl  yö '!ai-a  sara'inus'tre  V.  75.46;  3,  4,  10,  Yl. i.104,  7J.41,  74.28,  Vr.  77. 19,  Y.77.13, ^■43^'t  Vyt  70;  — yS  'sava  zara%u/trd Y.72.6; —  'iäva  yäia  zara%ustre  Yyl..  2, Az.4;  —  *savat>3m  i:ara%ui'inm  V.1O.2, 71.1,  2,  Yt,5.i8,  76.15,  ^5-79.  81  (statt I^om.),  V.5.21;  —  *saonö  zar^uHrahe Y.^23,  76".  2,  27.1,  24.5,2S.o,S7.S,08. «.  77.2,  P.5Ö,   Vr.76.2,  Yt«2,  y.62,
6869:Ikät^  'rynt    masdqm..aat  mr€oH^Xvtxz.,\ jnier  I  1)    "rö  mazda  V.  2.  if.;  usw.;    — j  dim  p9r^sat  sarai^uslrS  -rahe  (statt  Akk.) ' masdi    Nile  i ;    —    wii    mraot  (Stverz-,  [ nnter  1  3)      °rJ    masdä    V.iS.i;  usw.;  — miinm    .  .  y5   gimatte    'rät    mazdai  Yt. ' '''■53;    8.  to',   — frSmraot  °rS  mazda  Y. M.  1; — jiimäi ..paoiryS  maiyänqm  apsnse^ oum    y3     "rö    mazdä    V.  2.  2;  1 ;    —    äat ioxta   *rj  masds  V.  2.  21,  40,  42;  31,  Vr. 3.  3,  Y,  10.  9;  — paiti  sS  aoxta  'rS  mazds A.4.6,  H./.  2,  7,  P.27,  FrW./o.40,  Nik. 2;  —   aite  sl  vä^ . .  "rS  mazdn  främraot zara^ultrai  Y.  7/,  14;  ig.  i,  15;  —  rätayS ..*yqm    °rv  mazdil  xaraisuiträi /ravavaca frä    tara^uitrS  gaiHäiyö  ..  Y,6§.g;  — ja'ia    dim    isat    °rS    mazdh    V.2.32;  — jaia  . .  zaois  mana  yat  °rahe  masdä  Yt. ir).%z;    &35;    —    xmaoi:ra    (sd,    auch fdSt.)   'rahe  masdä  Yt.  7.0,  usw.;  — j;As- maitie  'rahe  mazda  Y._^.  i,  22.4,  23;  — frasasti  °rah*  mazdil  Y.  S.  i;  —  staotala .  .  yat  a^a  'rahe  mazda  Vt.i}.  6;  —  /ava 'ra  mazda  yasrum  . .  vahm>mca  Vr.  21.  a; P._3P;    —    ramasf    ti  'ra    mazda    "hrlsHt pars  anyäis  ääman  Ny,  /.  i ;  Y.6S.X2,  Yt. 7.1,  V.ig.25;    —  fumahl  iyiJmS    *'ra.- wiazdä'"'*    Y.  5>y.  3;    —   yat   zaota    'rsm ma-uiam  yazäiti  N.  70;  Y,  25. 4,  57.  a,  V. 7q.  19,  Vt  6.  4,  77. 18,  Vr.  jj.  I,  i8. 1,  23. 1, G.5.S;usw,;  —  kö  mqm  staoiti  yim  'r^m mazdqm  H.7. 3;    —    'rai  mazdäi  haomq äJoAayamahi  Y.  24- 1 ;  Vr.  //.  16,12.1;  — zbayamahi    JrJnämahi     mqm    ytm     °r>m mazdqm     Yt/2.3(?);    Vyt2.^(;    —    'nm mazdqm    danyo.yas/fmca  (si)    hqm.parl- timca  H-2, 14;    —    ks  itvqm  yim  °rgm mazdqm  . .  mazista  ibaisatiha  tbaisayeiti  V. /iS'.6i*;zitY.(?.8PiiZ.; — mä  zl  ahmt  nmane . .  fnm  i-aocata   mqm  yim  'nm  mazdqm yaia  ..  P.  17;    —    i^a    dim  ^ara-cinasti yim    'nm    mazdqm     .  .    damabyS    Y.  ig. la.        a)  in  Verbindung  mit  andern  Gott- heiten: 'rahe  mazda  . .  varahSus  mananks ..asahe  vahisiahe  .  ,  xia^rahe  vairyehe.. tpmtayB    ärmatöil .  .  haurvatä  amir^täta  , . .  ^ui  urune  gSUs    lalne  .  .  ä^re  °rahe  1 mazda  Y.  70.  z;  /.  if,,  57.24,  Vr.  i/.  16,  j ^-  5-  5«  V.  7p,  1 1 ;  —  -räica  mazdäi  srao- , s.Wa    a^.li    rasnvalta    razilläi   mt^räica Vr.  //.  6;  Y.  4. 2,  Vyt  i4;  —  «Äu  me  'ra , mazda   uäa    üpS  urvar&sca  usia  daine  .  . , VlÄ  29;  23.  a.)  bes.  häufig  mit  den
6982:•  j.  a-x'^Sra- Adj.  (fem. '■?-,l-)  'unbequem,  ä  frabarBit  V.J.  14  PüZ.;  7.25';  —  3ai lästig':  drux^  "re  (VSf.)  JVirszike  V.  /<S'.  yimS  fraläsairaoca  3  upa  rapüwqm  (sd.) 30,  36.  V.2.20; — frasa  fi-aya  vahist?m  ä  ahüm
6996:(sd)  a  manafiAs  \.4S-9-  T)  des  Be- treffs 'von  wegen':  tat  "kwa  p)r3sa  .  . mmanAs  a  ydha  n^m}  (sd.)  xlmavats  Y. 44.1,  S)  ahmst  *a  adv.-artige  Verb,, sbes.  b)  '(bis)  hin  zu  — ,  usque  ad  —'; a)  fäxioi&f^:  frasa  fraysit..a  zangaafyas- äj  äp3  a  inuiyasal  V.  6.27;  27*;  —  ajvT? a  ir/sas  (sd)  pa'kS  Y.J^-S-  a)  s  mit
7130:^yt.4;  Az.6  (wo  Uanm);  —  äat .  .  Im sä  iat-at  p3r»ne  .  .  ''hrqmta  suxrqm  (sd.) iaocintam  V.  2.8;  Vd.V;  —  asaocaniat paiti  '%räiS>  No*;  A.4.S,  V.g.$6  (wo °^rai);  —  Aaoa  'traii&yö''^  sao^ayantaäliyö Vd.p;  —  nixiata  ahinat  vazata  'tars  yS upa.suxtd  YL  to.  127;  —  hfya  .  .  '/rv//i aiti.barqn  avi  . .  nmätum  yaf  . .  na  fara.- ; iri^ytlJV.^.4i;  42f.; — yexi  nsit  mirika' (näml.  (i^ravaiti)  'trtm  atwi-valftai  (sd.)  | .  .'%re  (für  Gen.)  *raoxsnqm  paiti. dHyät  (sd,)  \ y.i0'.2i  —  avi  t/im  (n'iatL  vanqm)  aiwi.- rM/ayaü  (s±)  °^rffV.^.2; — ' '"kra  fra- vaiim^a  (sd.)  N.  65;  V.5.37;  —  von  Un- gläubigen mit  verpöntem  Material  genährt: yal  . .  dam)ayäzQ  avi  -irsm  äbarsiiti  .  . aO^m  aämitn  yS  vaoce  ^lumatka  nqma Yt  74. 5  5 ;  —  durch  Missbrauch  geschändet : yal  .  .  matdayasna  ,  .  'tnm  noiupäkfm (sd.)  /ra/atqn  .  .  '^raj  haca  . .  aismq frasaöcayähi  (sd.)  .  ,  yat  va  a?t»fn  "inm u%äarpza  (sd.)  .  .  vlca  barSil  vlca  sävaySit\ ya^a  äsiit-m  frävaySit'^ .S.T^-ty,  76,81';
7141:fravasayS . . yqmca  °'^ra  urvitzistahe  (s.  1  d) Hp>ntake  lyäxanahe  yqmca  sraelyeke  .  . yqmca  nairyS.sar?hahe  (sd.) . .  Yt.  7j.  8  5 ;  — °tar^  äfrJnämi  . .  tax'a  ahuräne  iifrinämi  Y. ÖÄ14;  — s.nochV.A:8o,7<V.26,Y.fo.7-io (oben  Sp.312);  —  als  besondrer  Gegner des  AiayDahäka*'':  sp?nlö  mainyus  aUym (sd)  frarf/tancayat  vohuca  manö  ahmca vahistfm  °trjmca . .  a»rS  maiiiyu^ , ,  akimca mano  alsimimca  .  .  a'sTmca  dakäk}m  Yt. 75.46;  —  dlilt  frasa  hqm.razayata  'tars..
=== HJB 352 area / FIRINGHEE ===
9641:FIRINGHEE.
9643:firinghee:.
16603:syphilis ;  the  whole  body  bein^ covered  with  ulcers,  while  the  sufferer rapidly  declines  in  strength.  It  seems to  arise  from  insufficient  diet,  and  to be  analogous  to  the  pellagra  which causes  havoc  among  the  peasants  of S.  Europe.  The  word  is  apparentlv firinghee,  *■  European,'  or  (in  S.  India) *  Portuguese  * ;  and  this  would  point perhaps  to  association  with  syphilis.
25128:3496 Ffarcuttee,  8106 Ff  uckeer,  8476 Filoeofo,  3476 Fir^hd^nga,  1466 Firefly,  351a Firinghee,   Dhatura,
```


## [2026-09-05T20:34:00.051Z] TOOL CALL #16: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:1462 2>&1 | head -60",
 "description": "Fetch Borhan-e Qate page 1462"
}
```


### [2026-09-05T20:34:07.979Z] TOOL RESULT

```
REF: BQT:1462  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 255  OCR-lang: fas

فرسنافه -۱:۹۲-
گویبند ۹ خرچنگه‌دار ۰ علامتیر| گوبند که درراهها بجهت
گررسناقه - بکر اول و فتح آخر که | داستن مقدار فرسنگه سازند - وسنگه چیتی‌را
فا پاشد , سعنی فرسناف است که شب نوروز نیز گفته‌اند که در راهها برای نشان راه‌کنند .
باشد ۲ فرس نهادن - بنتح اولونانی, کنابه
قرسنداج ؟ - بفتم‌اول والك‌وسکون ۲ از مغلوب شدن و عاجز آمدن باشد .#۸
نانی و نون و دال بی نقطه بالف کشیده و بجیم فرسوده ۱ - باسین بی نقطه بر وزن
فارسی زده . مطلق امت را کویند. بمنی‌امت * | فرموده » چیزی راکوبند که بفایت کهنه و ازهم
یغمب رکه باشد . ربخته وپایمال کردیده و افرده شده باشد .
فرسنگ ؟ - بنتح اول وثالك بروزت فرش - بنم اول و سکون تانی و شین
سرجنگه(۱). قدری‌باشد ممین از راء وآن‌بمفداد. [ قرشت . آغوز و فله راکویند وآن غیری باشد
سه میل است و هرمیلی چهارهزا رک ز کهمجموع | که از حیوان بوزاییده دوشند . وجون برآتش
فرسنکه دوازده هزارکز باشد و طول هرکزی تهند مانند پنیر بته شود ۷ - و بفتح اول, در
بفدر پیست و چهار الگشت دست باشد که بمرض | عریی کسترانیدن و فراخ شدن میان پای شتر و
در پهلوی هم گذارند ون شش قبضه است بمنی ‌ هر چیز که کستردنی باشد همچو حصیر و پلای
و و قالی و مانند آن - وچارواییر! نیز کوبن د که
فرسنگار * م باسین بی‌نقطه‌پروزن | غبرازخوردن‌را نشایید - و شتربچه‌ای که قابل بار
(۱) چك : سرسنگه .
۹ > فرسنافه : فرسناف بخت تو نوروز ( فیروز ) باد
شبان سیه بر تو چون روز باد .
فردوسی طوسی ۶ رشیدی > * فرهنکه:ظام *
ولی این لغت در فپرست شاهنامهٌ ولف نیامده . رك : فرسنافه .
۳ فرسناف :
شب قدر وصلت ز فرخندکی فرح بخش تر از فرستافه است .
رودکی سمرقندی « رشیدی »
۴ - برساختهٌ دساتیر ۸« قاب۱٩‏ : 4۷ > فرهنگه دساتین ۲۵۷ » ۰
۴ - پهلوی 5۳389888 ( مقیای طول)» پارسی باستان 02785481281265 ( بونانی‌شدة
كلمةٌ پارسی باستان - 82882 - 0۶۳2) ؛ فارمی جدید ۶2۳988080 از 1۳25288 ارمنی ع
ععرب « فرسخ > * نیب رکه ۷۳ > «اسشق - هوبشمان ۸۱۸ : * برسید بر کنار آبی
که سنگه از صلابت او برسنگه همی‌آمد و صربرش بفرسنگه همی رفت .> «کلتان ۱۱۷*.
8 _- از : فرسنکه سار (حدس) ۱ پوند مکان). [ هه اسم‌مقعول از«فرسودن».
۷ ه فرشه (ه.م.) ۰
2 فرسودن - بفتح اول وپنجم < فرساییدن از ۲2-58 ؛ اوستا 5288 - 1۳3(محو
و نابود کردن) « پارتولمه ۱۶*۱ > « نیب رکه ۷۳ : 11382۷2800 > ؛ سودن » سایدن -.
مالیدن » زدودن - ساییده شدن -کهنه شدن - پیرشدن - پوسیدن .
```


## [2026-09-05T20:34:18.583Z] TOOL CALL #17: Bash

```json
{
 "command": "sed -n '9630,9700p' /home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt",
 "description": "Read Hobson-Jobson FIRINGHEE entry"
}
```


### [2026-09-05T20:34:18.677Z] TOOL RESULT

```
HAer,  ed.  1844,  i.  258.
1865.— ''The  bushes  literally  swarm  with fireflies,  which  flash  out  their  intermittent light  almost  contemporaneously ;  the  effect beinff  that  for  an  instant  the  exact  outline of  aU  the  bushes  stands  prominently  for- ward, as  if  lit  up  with  electric  sparks,  and next  moment  all  is  jetty  dark— darker  from the  momentary  illumination  that  preceded. These  flashes  succeed  one  another  every  8 or  4  seconds  for  about  10  minutes,  when  an interval  of  similar  duration  takes  place  ; as  if  to  allow  the  insects  to  regain  their electric  or  phosphoric  vigour." — Camercn Our  Tropical  Poueuiont  in  Malayan  India. 80-81.
The  passage  quoted  from  Mr. Cameron^s  book  was  read  at  the Entom.  Soc.  of  London  in  May  1865, by  the  Rev.  Handet  Clarke,  who  added that:
"Though  he  was  utterly  unable  to  give an  explanation  of  the  Dfaenomenon,  he could  so  far  corroborate  Mr.  Cameron  as to  say  that  he  had  himself  witnessed  this simultaneous  flashing  ;  he  had  a  vivid recollection  of  a  particular  glen  in  the Organ  Mountains  where  he  had  on  several occasions  noticed  the  contemporaneous  exhi- bition of  their  light  by  numerous  individuals, as  if  they  were  acting  in  concert."
Mr.  McLachlan  then  suggested  that this  might  be  caused  by  currents  of wind,  which  by  inducing  a  number of  the  insects  simultaneously  to  chance the  direction  of  their  flight,  might occasion  a  momentary  concealment  of their  light.
Mr.  Bates  had  never  in  his  experi- ence received  the  impression  of  any simultaneous  flashing.  ...  he  regarded the  contemporaneous  flashing  as  an illusion  produced  probably  by  the swarms  of  insects  flym^^  among  f oli£^ and  beinff  continually,  but  omy momentarily,  hidden  behind  the  leaves. —Proe.  Eniom.  Soc.  of  London^  1865,  pp. 94-96.
Fifteen  years  later  at  the  same Society :
'*Sir  Sidney  Saunders  stated  that  in  th» South  of  Europe  (Corfu  and  Albania)  the simultaneous  flasning  of  Lueiola  ttaliea, with  intervals  of  complete  darkness  for some  seconds,  was  constantly  witnessed  in the  dark  summer  nights,  when  swarming- myriads  were  to  be  seen.  •  .  .  He  did  n<^ concur  in  the  hypothesis  nropounded  by BCr.  McLachlan  .  .  .  the  muhes  are  cer- tainly intermittent  .  .  .  the  simultaneous character  of  these  coruscations  among  vast swarms  would  seem  to  depend  upon  an instinctive  impulse  to  emit  their  ught  at certain  intervals  as  a  protective  influence, which  intervals  became  assimilated  to  each other  by  imitative  emulation.  But  what* ever  be  the  causes  .  .  .  the  fact  itself  waa incontestable."— /6u2.  for  1880,  Feby.  24,. p.  ii. ;  see  also  p.  vii.
1868.— "At  Singapore  ...  the  Uttl» luminous  beetle  commonlv  known  as  the flrefly  (Lampvris,  sp.  ign.)  is  common  .  .  • clustered  in  the  foliage  of  the  trees,  instead of  keeping  up  an  irregular  twinkle,  every individual  shines  simultaneously  at  regular intervals,  as  though  bv  a  common  impulse ; so  that  their  light  pulsates,  as  it  were,  and the  tree  is  for  one  moment  illuminated  by a  hundred  brilliant  points,  and  the  next  la almost  in  total  darkness.  The  intervals have  about  the  duration  of  a  second,  and during  the  intermission  only  one  or  two remain  luminous." — CoUingtoood,  RambUa  of a  Naturalitt,  p.  255.
1880.— "Harbingbbs  of  thb  Monsoon. — One  of  the  surest  indications  of  the  ap> proach  of  the  monsoon  is  the  spectacle  pre- sented nightlv  in  the  Mawul  taluka,  that is,  at  Ehandalla  and  Lanoli,  where  the  trees are  filled  with  myriads  of  flrvfliei,  which flash  their  phosphoric  light  simultaneously. Each  tree  suddenly  flashes  from  bottom  to top.  Thousands  of  trees  presenting  this appearance  simultaneously,  afford  a  spectacle beautiful,  if  not  grand,  beyond  conception. This  little  insect,  the  female  of  its  Idnd, only  appears  and  displays  its  brilliant  light immediately  before  the  monsoon." — Doxan Herald.    (From  Pioneer  Mail^  June  17).
FIBINGHEE,  s.  Per&  Farangl, Firingi;  Ar.  Ai-Faranjy  Ifranfi,  Firanjt^ i.e.  a  Frank.  This  term  for  a  European is  very  old  in  Asia,  but  when  now employed  by  natives  in  India  is  either applied  (especiiJlv  in  the  South)  speci- fically to  the  Indian-bom  Portuguese, or,  when  used  more  generally,  for 'European,'  implies  something  of hostihty  or  oisparagement.  (See Sonnerat  and  Elpkindone  below.^  In South  India  the  Tamil  Farangi^  the Singhalese  Parangi,  mean  only  '  Portu- guese,' [or  natives  convertea  by  the Portuguese,  or  by  Mahommedana,  any
FIRINGHEE.
353
firinghee:.
European  {Madras  GUm.  s.v.).  St. Thomafi's  Mount  is  called  in  Tarn. Parangi  Malai,  from  the  ori^al Portuguese  settlement!  Piringi  is  in TcL = *  cannon,'  (C.  B.  P.X  just  as  in  the medieval  Mahommedan  historians  we find  certain  mangonels  for  sie«;es  called vnaghribi  or  *  Westerns.*  [And  so Farluingi  or  Phirangt  is  used  for  the straight  cut  and  thrust  swords  intro- duce by  the  Portuguese  into  India,  or made  there  in  imitation  of  the  foreign weapon  {Sir  W.  EUioty  Ind.  Antiq,  xv. 30)1  And  it  ma^  be  added  that Baber,  in  describing  the  battle  of P&nipat  (1526)  calls  his  artillery Faran^ha  (see  Aviob,  by  Leyden  and Erskine,  p.  306,  note.  See  also  paper by  Gen.  II.  Maclagan,  R.E.,  on  early Asiatic  fire- weapons,  in  J.A.S.  Beng. xlv.  Pt.  i.  pp.  66-67X
c.  980.— "The  Afranjah  ar«  of  aU  those nationa  the  most  wulike  .  .  .  the  best organised,  the  most  sabmissiTe  to  the authority  of  their  nUera/'—Mof^Mdl,  iii.  66.
c.  1340.—"  They  caU  Ftaaohi  aU  the Christians  of  these  parts  from  Romania westward."— P^ofotfi,  in  Cathay,  kc,  292.
c  1850.—"   Franks.     For   so  they
term  ns,  not  indeed  from  France,  but  from Frank-land  (non  a  Francid  sed  a  Franquid). " —MarignoUi,  ibid.  886.
In  a  Chinese  notice  of  the  same  age the  horses  carried  by  MarignoUi  as  a present  from  the  Pope  to  the  Great Khan  are  called  "horses  of  the  kingdom of  Fnlaog,"  i.e,  of  Farang  or  Europe.
18S4.— "E  quelle  nominare  Ftaachl  pro- cede  da'  Franoeschi,  che  tutti  ci  appelLano Franoeschi"— /Veico6aMi,  Viaggio,  p.  28.
I486.— "At  which  time,  talking  of  Caiaic, he  told  me  howe  the  chief  of  that  Princes corte  knewe  weU  enough  what  the  Franohl were.  .  .  .  Thou  knowest,  said  he,  how neere  wee  bee  unto  CSapha,  and  that  we practise  thither  continually  .  .  .  adding  this further,  We  Cataini  have  twoo  eyes,  and yo^  Tnncitd  one,  whereas  yo^  (tomeng him  towards  the  Tartares  that  were  w^  him) have  neuer  a  one.  .  .  ." — Barbcaro,  Hak. Soc.58.
c.  1440.  —  "  Hi  noe  Ftaaoos  appellant, ainntqne  cum  ceteras  gentes  coecas  vooent, se  duobis  ocnlia,  nos  unico  esse,  superiores ezistimantes  se  esse  prudentiA" — Conti,  in Poggius,  de  Var.  Fortunae,  iy.
1496.— "And  when  he  heard  this  he  said that  such  people  could  be  none  other  than Fraaoos,  for  so  they  call  us  in  those  parts." —RoUiro  deV.da  Oama,  97.
1660.—"  Habitfto  aqui  (Tabriz)  duas  na^Oes de  ChristSos  .  .  .  e  huns  delles  a  qui  ohamSo P^aaililM,  estee  tern  o  costume  e  f^,  oomo Z
nos  .  .  .  e  outros  sSo  Armeno8."^A»  Ten- reirOf  Itinerario,  ch.  xv.
1565. — "  Suddenly  news  came  from  Thatta that  the  Firingls  had  passed  Lahori  Bandar, and  attacked  the  dty, '—TaHihri-Tdkiri,  in Elliot,  I  276.
c.  1610. — "La  renomm^  des  Francis  a eet6  telle  par  leur  conquestes  en  Orient,
2ue  leur  nom  y  est  demeur^  pour  memoire temelle,  en  ce  qu'enoore  aujourd'huy  par toute  TAsie  et  Afrique  on  appelle  du  nom de  Fzaogfai  tons  ceux  qui  viennent  d'Occi- denV^—Moequet,  24.
[1614. — ".  .  .  including  us  within  the word  Franqneis."— ^of^,  Letters,  ii.  299.]
1616.—".  .  .  alii  Cc^fret  et  C^ams  eos dicunt,  alii  TniMM,  quo  nomine  omnes passim  Christiani  .  .  .  dicuntur." — Jarric, Thetaurus,  iii.  217.
[1628.— "Franohl,  or  Christians."— P. dtlla  Voile,  Hak.  Soc.  ii.  251.]
1682.—".  .  .  he  shew'd  two  Passes  from the  Portugals  which  they  call  by  the  name of  Fringes."— fF.  Bruton,  in  Hakluyt,  ���.  32. 1648.—"  Mais  en  ce  repas-l&  tout  fut  bien aooommod^  et  il  y  a  apparence  Qu'un  oui- sinier  J^raagni  s'en  estoitm€16." — Tavemier, V.  det  Indes,  iii.  ch.  22 ;  [ed.  Ball,  ii.  885].
1658.  — "  Frenk  signifie  en  Turq  vn Europpeen,  ou  plustost  m  Chrestien  ayant des  cheueuz  et  tu  chapeau  comma  les Francois,  Anglois.  .  .  ." — De  la  Baullaye-le- Oma,  ed.  1657,  588.
c.  1660.— "The  same  Fathers  say  that  this Kiog  (Jehan-Guire),  to  begin  in  eood  earnest to  countenance  the  Christian  Religion,  de- signed  to  put  the  whole  Court  into  the  habit of  the  Fnuumi,  and  that  after  he  had  .  .  . even  dressed  himself  in  that  fashion,  he called  to  him  one  of  the  chief  Omrahs  .  .  . this  Omrah  .  .  .  having  answered  him  very seriously,  that  it  was  a  very  dangerous  thin^, he  thought  himself  obliged  to  change  his mind,  and  turned  all  to  raillery." — Bemier, KT.  92 ;  [ed.  Constable,  287 ;  also  see  p.  3]. 1678.— "The  Artillery  in  which  the  Fringls are  Listed  ;  formerly  for  good  Pay,  now  very ordinary,  having  not  above  80  or  40  Rupees a  month."— JVyer,  195.
1682.—".  .  .  whether  I  had  been  in Turky  and  Arabia  (as  he  was  informed) and  could  speak  those  languages  .  .  .  with which  they  were  pleased,  and  admired  to hear  from  a  Frenge  (as  they  call  us)."— Sedgeg,  Diary,  Oct  29 ;  [Hak.  Soc.  i.  44].
1712. —  '*  Johaii  Whelo,  Serdaar  Pren- giaan,  or  Captain  of  the  Europeans  in  the Emperor's  service.  .  .  ." — Valentijn,  iv. (Suratte)  295.
1755.— "By  Feringy  I  mean  all  the  black muMtee  (see  BuTSTEES)  Portuguese  Christians residing  in  the  settlement  as  a  people  distinct from  uie  natural  and  proper  subjects  of Portugal ;  and  as  a  people  who  sprung originally  from  Hindoos  or  Mussulman." — Holwell,  in  Long,  59.
1774.— "He  said  it  was  true,  but  every- body was  afraid  of  the  Firiogles." — Bogle, in  MarkhanCs  Tibet,  176.
FIRM  A  UN.
354
FISCAL.
1782. — "Ainai  on  European  eat  tout  oe que  lee  Indians  oonncdaMnt  de  plus  m^pria- able  :  ila  le  nomment  ParaogUy  nom  qu'ila donnerent  aox  Portugaia,  loraque  oeux-oi abord^rent  dans  lenr  pajs,  et  c'est  un  terme qui  marque  le  aouyenun  m^pria  qu'ila  ont pour  toutea  lea  nationa  de  I'Europe." — SonnenU^l  102.
1791. — ".  .  .  il  demande  k  la  paaaer  (la nuit)  dana  un  dea  logemena  de  la  pagoda: maia  on  lui  refuaa  d'y  coucher,  k  cause  qu'il ^toit  finuuruL"— J),  de  SL  Pierre^  Chaumiirt liuiienney2\.
1794. — "Fcringee.  The  name  given  by the  natiyea  of  the  Deean  to  Europeana  in general,  but  generally  understood  by  the English  to  be  confined  to  the  Portugueae." — Moor*$  Narraliwt  604.
[1820.—"  In  the  aouthem  quarter  (of fiabkeigunje)  there  atill  exiat  aeveral  original Portugpiese  colonies.  .  .  .  They  are  a  meagre, puny,  imbecile  race,  blacker  than  the  natiyea, who  hold  them  in  the  utmoat  contempt^ and  designate  them  by  the  appellation  of Ckiula  FerenghiM,  or  black  Europeana."— Hamilton,  Descr.  of  MindotiaTt,  i.  183;  for an  account  of  the  Feringhis  of  Sibpur,  see Beveridge,  Bdkarganj,  110.]
1824.— "* Now  Hajji,'  aaid  the  ambas- sador. .  .  .  *The  Aranks  are  composed  of many,  many  nations.  As  fast  as  I  hear  of one  hog,  another  begins  to  grunt,  and  then another  and  another,  until  I  find  that  there is  a  whole  herd  of  them.'"— iTom  BaJba,  ed. 1886,  p.  482.
1826. — "Europeans^  too,  are  very  little known  here,  and  I  heard  the  <»iildren continually  calling  out  to  us,  as  we  passed through  the  yillages,  'F«ringhee,  ve  Farin- ffheer"-J5re6«rrii.48.
1828. — "Mr.  Elphinstone  adds  in  a  note that  in  India  it  is  a  positive  afifront  to  call an  Englishman  a  F«ringhee."— 2^e  qf  B. ii.  207.
c.  1861.- "  There  goes  my  lord  the  Ferlnghee,  who talks  so  civil  and  bland, But  raves  like  a  soul  in  Jehannum  if  I
don't  quite  understand — He  begins  by  calling  me  Sahib,  and  ends by  calling  me  fool.  .  .  ."
Sir  A.  C,  Lyall,  The  Old  Pindaree.
The  Tibetans  are  said  to  have  cor- rupjted  Fiiinghee  into  Pelong  (or Philin),  But  Jaeschke  disputes  this origin  of  Pelong,
FIBMAUN,  s.  Pers.  farmdn^  'an order,  patent,  or  pas^rt,'  der.  from farmildML  *to  order.*  Sir  T.  Roe  below calls  it  jvrma^  as  if  suggestive  of  the Italian  for  'signature.'
[16<n.— ".  .  .  wrote  him  a  letter  called Firmao.  .  .    "—CattanMa,  Bk.  viii.  ch.  99.
[1602.— "They  aaid  that  he  had  a  Firmao of  the  Grand  Turk  to  go  overland  to  the
Kingdom  of  (Fdrtogal).  .  .  ."--Omto^  Dee. viHTch.  15.]  ^      ^    '  '
1606. — ''We  made  our  journey  having  a Firman  {FimUUi)  of  safe  oonduot  from  the same  Soltan  of  Shiraa." — Oouvea,  t  140&u
[1614.— "But  if  poadble,  bring  their  ofaapi, their  Firms,  for  what  they  say  or  promise.'* —FoHer,  Letten,  ii.  28.]
1616.— "Then  I  moued  him  for  his  eavoar for  an  English  Factor^r  to  be  resident  in  the Towne,  which  hee  willingly  granted,  and gave  present  order  to  the  Buxy  to  draw  a Flzma  ...  for  their  residence." — Sir  7*. Roe,  in  Pwckas,  I  641 ;  [Hak.  Soc  i.  98 ; also  see  i.  47].
1648.— "The  21st  April  the  Baasa  sent  me a  Firman  or  Letter  of  credentials  to  all  his lords  and  Governors." — T.  Van  den  Broeeke, 32.
1673.— "Our  Ussffe  by  the  Phaxmannd (or  charters^  grantea  successively  from  their Emperors,  is  kind  enough,  but  the  better because  our  Naval  Power  curbs  them." — Fryer,  115.
1683.— "They  (the  English) complain,  and not  without  a  Cause;  they  having  a  Phlr- mannd,  and  Hodgee  Sophee  Oaun's  Per- vxmnai  thereon,  in  tneir  hajids,  which  cleared them  thereof ;  and  to  pay  CustcMne  now  tiiey will  not  consent,  but  will  rather  withdraw their  trading.  Wherefore  their  desire  is that  for  3,000  rup.  PiaeaMk  (as  they  paid formerly  at  Hugly)  and  2,000  r.  more  yeariy on  account  of  Jldgea,  which  they  are  willhig to  pay,  they  may  on  that  condition  have  a grant  to  bcCustome  Free."— iVa(o6*tf  Letter to  Vizier  (MS.V,  in  Hedges'  Diary,  July  18 ; [Hak.  Soc.  i.  101].
1689.—".  .  .  by  her  came  Bengal  Peons who  brought  in  several  letters  and  a  fixmaim from  the  new  Nabob  of  BetuoLi  "—Wheeler, i.  213.
c.  1690.— "Now  we  may  see  the  Mogul's Stile  in  his  Phixmaimd  to  be  sent  to  Surat, as  it  stands  translated  by  the  Company's Interpreter."—^.  ffamilUm,  i.  227 ;  [ed. 1744,  i.  290].
FISCAL,  &  Dutch  Fisoaal;  used in  Ceylon  for  *  Sheriff' ;  a  relic  of  the Dutch  rule  in  the  island.  Fit  was  also used  in  the  Dutch  settlenients  in Bengal  (see  quotation  from  Hed^et^ below).  "  In  l^alabar  the  Fiscal  was  a Dutch  Superintendent  of  Police,  Justice of  the  Peace  and  Attorney  General  in criminal  cases.  The  office  and  title of  Fiscal  was  retained  in  British  Cochin till  1860,  when  the  designation  was changed  into  Tahsildar  and  Sub- Magistrate."  —  {Logatiy  Malabar^  iii Gloss,  av.)]
[1684.--".  ..  the  late  Dutdi  FlnalTs Budgero.  .  .  . " — See  oaotataon  from  Sedges, under  DEVIL'S  EKArtH]
FLORICAN,  FLORIKIN.         3fi6
FLY,
FLOBICAN,  FLOBIKIN,  s.     A
name  applied  in  India  to  two  species of  small  bustard,  the  'Ben^l  Florican' {Syj^ieoUdes  hmgcUennSj  Gmelin),  and the  Lesser  Florican  (5.  aurUtUj  Latham), the  Ukh  of  Hind.,  a  word  which  is  not in  the  dictionaries.  [In  the  N.W.P. the  common  name  for  the  Bengal  Flori- can is  ehanu,  P.  charz.  The  name  Cur- moor  in  Bombay  (see  quotation  from Forbei  below)  seems  to  be  khar-mor,  the 'grass  peacock/  Another  Mahr.  name, tanamora,  has  the  same  meaning.]  The oriffin  of  the  word  Florican  is  exceed- ingly obscure  ;  see  Jerdon  below.  It loolts  like  Dutch.  {Th^N.E.D,  suggests a  connection  with  Flanderkiny  a  native of  Flanders.]  Littr^  has:  *' Florican .  .  *  Nom  &  Ceylon  d'un  grand  ^has- sier  <^ue  Pon  presume  €tre  un  grue." This  IS  probably  mere  misapprehension in  his  authority.
```


## [2026-09-05T20:34:19.529Z] TOOL CALL #18: Bash

```json
{
 "command": "timeout 400 python3 tools/ref_page.py BQT:1471 2>&1 | head -60",
 "description": "Fetch Borhan page 1471"
}
```


### [2026-09-05T20:34:28.446Z] TOOL RESULT

```
REF: BQT:1471  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 264  OCR-lang: fas

-۱۱۷۱- فرنجه
فرناس ۱ « بفتح اول بروزن کرپای » | وسکون تالك وکاف , کابوس و عبدالجنهراکوبند .
بمعتی غاعل و نادان باشد - و غفلت و نادانی را | وآن‌گرانی و سنگینیی باش د که درخواب‌برمردم
نیز گفتهاند - و بمعنی نیم خواب و خواب آلود آفند وحکما کونند سبب آن ماد سوداوی است
هم‌آمده است - و خواب اندك را نی زکوبند ۲ و درخواب چنان مینماید ‎٩‏ ؛ و بکسر اول‌وئانی
و بکس اول, در عریی شیر درددء سطبر کردن | هم آمده است؛ و درموبدالفضلا باین معنی‌باقاف
باشد؟۴ . نوشته‌اند .
فرفج - بنم اول و ثانی و سکون نون فر نجمشات ۱ - بنتح اول و شممیم:
وجیم . پیرامون واطراف دهانراکویند۴ -وشاخ | بمعنی افراجمشك است که بالنگوی صحرالی
بزرگیرا نی ز کفته‌اند که چونآترا ببرندشاخهای | باشد وعوام آنرا بالنگوی کنده کوبند و بعریی
کوچك از اطراف‌آن برآید ؛ و بفتح اول وثانی | بقلةالشب خوانند . بواسیررا نافع و مخغفف منی
ویکس اول و ضم نانی هم آمده است. باشد .
فر زج - بتتم اول وثالی وجیم فرنجه ۷ - بنتح اول و ثانی و جیم
۱- هندی باستان -8869 0۳2 ( غایب وناپدید شدن ) » ساسکربت - 80۳88262
( تمام شدن , خاموش شدن ) « اسشق - هوبشمان ۸۲۲ >:
گفت نقاش چونکه نشناسم که ته دبوانه ونه فرناسم. ‏ عنصری بلخی«لغت فرس۱۹۲*.
۳ -<-وق30۲۳ , 50۲08۵ (تهرانی وکیلکی )( خر ویفی که شخص‌خوایده کند).
۴ - (عر) «فرنای » بالکر رئیی ومهتر روستابیان - و شیر سطبرکردن و سخت
دلیر۰» ۸« منتهی‌الارب » . ۴ - « فرنج » پیرامن دهان باشد . رودکی (سمرقندی) کوید :
سر فروبردم میان آبخور از فرنج منش خشم آمد مگر.» « لغت فری ۵۸ >.
« این لفظ را مخغفف « فرهانج > هم نوشته ورشدی مخغف « فرنجك > هم . اما هیچکدام‌شاهد
تیاورده و درصورت صحت درهردو باید بافتح اول ودوم باشد. » « فرهنگه نظام >.
۵ <* فرونجك.قی:فدرنجك,درفنجك, برفنجك. فرهانح؛ وآلرابختك وخرخجیون‌نامند:
فريجك وارشان بگرفته آن دیو که سربانی است نامش خرخجیون .
خاقالی شروانی « فرهنگه نظام >.
‎٩‏ - بفتح اول و دوم وچهارم وضم پنجم . دزی‌آنرا به « مشکه فرانکها [ فرنگیان]»
ترجمه میکند < برنجمعك * فلنجمعك (ه.م.) ۳21116 ۶207 (فی) > 01150000000
«زی‌ج ص۲۹۲ :۲*. فرنجمشك < ۸6118992 ازتیرة نمناعیان 1201668 که بر‌کپای ناهموار
و دندانه‌بی دارد وگلپای آن سفید مایل بزردیت وگلها و برکها و دانه‌های آن متعمل‌است
«دگلگلاب 4۷ . ما کی‌مایرهوف کوید : «این لغت عربی ( فلنجمعك ) ازفارسی ماخوذاست.
و فولری (آ:*۱۱) در مادة « افرنج - مغك ( مشکه فرنگیان ) > و در ماد پلنکه - مشکه
(۳۷۹,۲)( مشکه پلنگه ) [ ببب رنگارنگی وعطرگیاه مزبور ] آنرا شرح داده.21816۳]
فقط وجه اخیر را پذیرفته است « عقار4۷ > موْبد نظر اخيرکلمه پهلوی 02120800501 است.
رك: پلنگشکه. ۷- مخفف «افرنجه» (ه.م.)[ * افرنگه * فرنکه] معرب۲ ۰۳۳۵۵
لانینی 17386015 فرانوی۳720 (قوم ژرمان ی که درقدیم در جوار رود 141118 سکوت‌داشتند)
و بمنلکت فراده نیز اطلاق شود . رك : نضبة الدهر دمدقی فهرست ام 2212۳ .
```


## [2026-09-05T20:34:44.928Z] TOOL CALL #19: Bash

```json
{
 "command": "timeout 400 python3 tools/ref_page.py BQT:1472 2>&1 | head -45",
 "description": "Fetch Borhan page 1472"
}
```


## [2026-09-05T20:34:46.667Z] TOOL CALL #20: Bash

```json
{
 "command": "head -40 tools/fetch_source.py; echo \"=== web index sample ===\"; ls data/verification/sources/web | head -5; ls data/verification/sources/web | wc -l",
 "description": "Inspect fetch_source tool"
}
```


### [2026-09-05T20:35:12.065Z] TOOL RESULT

```
REF: BQT:1472  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 265  OCR-lang: fas

فرید -۱۱۷۲-
و کون ثالك » لام ولایتی وبندری‌است پرساحل | ثالث وکاف فارسی پتختانی کشیده وبسین‌بی له
دربای فرنگه؛ وبکسراول بروّلان شکنجه‌همآمده ‏ زده » نام دخش افراسیاب است و او درعقدنکاج
است (۱). 3 سیاوش بود و کیخسرو پسراوست ؛ و درمویدالفنلا

. فرفد ۱ - بنتح اول و انانی واسکون | بجای نون بای حطی لوشته اند .
تال ودال ابجد, جوهر تیغ وشمشیر راکویند؛ فرفود * < بر وزن مقصود: بممنی
وبکس اول هم کفته‌اند . برهان ودلیل باشد .

فرتف - بفتح اول وثانی بروزن‌شرنگه» فر نودسار ۹ - با سین بی‌نقطه بالف
ممروق است ۴ :وبعریی‌تصاری ۴ کوبنسوبکس | کنیده بروزن انگورزار » نام کتایست درجمیم
اول وسکون نانی بر وزن خشتك. بلزبچهٌ اطفال | فنون حکمت و معنی آن برهانستان و دلیلستان
بلشد » وآن چوبکی است پهن ومدو رکه پایین | باشد چه فرنود بمعنی دلیل وبرهان وسار بمعنی
آنرا تیز سازند و بالای آنرا یعنی بلندی آترا | جاو مقام بود"
آشدر کنند که بدو انگشت کرفته توان قرفه ۷ ۰« بفتح اول وثالك . بمعنی‌لمنت
کردالید ۴ وتفرین باشد .
: فر نگیس - بنتح اول و ثانی و سکون قرو « بفتح اول وثانی بواو رسیده. نوعی

(۷) چك : - است .

۹ - ۲1۳100 << 1۳۲180 معرب «پرند» (تفی) » استاد هنینگك این «فرند» را: با*فرند»
معرب « پرند > که اسلا بمعنی حر بر کلدار بوده امست از يك ربشه مبداند . رل :

۱25-7 .2 و ۷۵:۵8 ۸20 ۲6۱۲۳۵۱ 10 , ۲1۵/۱۵۵

« الفر‌ندی‌کالافرندی, نسبة الی‌الفرند او الافرند» وهوجوهرالسیف ووشیه . وسمی‌بذلك‌لمایری علی
و جههمن مثل عذاالوشی» « نخب ص ۷۱ح >. ۴ -رك : فرنجه .

۴ - ضاری بسیجیان اطلاق شود و فرنگه بقوم فرانکه ( و توسماً اروپابیان ) خواه
میحی وخواه غیر میحی باشد؛ وچون غالب اروپابیان میحی‌اند من‌باب‌اطلاق کل بجزء بنصاری
تیزاطلاق شده: «(نورالدین محمود زنگی) هم «زین‌سال بغز و کفار فرنگه اقدام نموده بین‌الجانیین
جنگی صمب اتفاق افتاده .> « حبیب‌السیر جزو چهارم از جلد دویم ص۱۹۹ چاپ تهران > ونیز
فرنگه را بجای فرنگی بکار برده به «فرنگان» جمم بسته اند :

بدین‌سفت که توبی در شجاعت ومردی اگر پدر بفرستد ترا بجنگه فرنگه,
صلیب بشکنی و دارها زنی چو صلیب "تن فرنگان از دار ها کنی آونگه .
معزی نیشاپوری ۵۳۵ .

۴ -قس : افرنجیه (عر) که بنوعی ماغین جنگی اطلاق شود ۶ دزی اج اص ۲:۲۹۲.

8 برساختهٌ دساتین « فاب۱: 2۷ »> فرهنگك دساتیر ص ۲۵۷ نی

‎٩‏ - برساختهٌ دساتیو . ۷ - مصحف «فربه» « سراح‌اللغات بنقل فرهنکه نظام
```


### [2026-09-05T20:35:12.150Z] TOOL RESULT

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
=== web index sample ===
0013bab04a208776.txt
003529da0fded286.txt
00446da837c05ca7.txt
0070109655be6e11.txt
00738e15ee065d37.txt
1516
```


## [2026-09-05T20:35:34.031Z] TOOL CALL #21: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/frank\" \\\n \"https://www.etymonline.com/word/parasang\" \\\n \"https://en.wiktionary.org/wiki/parasang\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B3%D9%86%DA%AF\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D9%86%DA%AF\" \\\n \"https://en.wiktionary.org/wiki/%D8%A5%D9%81%D8%B1%D9%86%D8%AC%D9%8A\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%87\" ; do\n echo \"### $u\"; timeout 90 python3 tools/fetch_source.py \"$u\" --note \"pdf page 164: Frankon / Fra-sanga verification\" 2>&1 | tail -2; done",
 "description": "Archive web sources batch 1"
}
```


### [2026-09-05T20:35:39.095Z] TOOL RESULT

```
### https://www.etymonline.com/word/frank
/home/sfmqrb/git/rishe/data/verification/sources/web/cd86323d71443092.txt
### https://www.etymonline.com/word/parasang
/home/sfmqrb/git/rishe/data/verification/sources/web/68dec7f6cd00384c.txt
### https://en.wiktionary.org/wiki/parasang
/home/sfmqrb/git/rishe/data/verification/sources/web/9b15a4610fae692d.txt
### https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B3%D9%86%DA%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/5f43029d34370d4f.txt
### https://en.wiktionary.org/wiki/%D9%81%D8%B1%D9%86%DA%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/3da86dfad99e809b.txt
### https://en.wiktionary.org/wiki/%D8%A5%D9%81%D8%B1%D9%86%D8%AC%D9%8A
/home/sfmqrb/git/rishe/data/verification/sources/web/7faa2456d366e478.txt
### https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/ab6e921b7f3cfad7.txt
```


## [2026-09-05T20:35:42.924Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in cd86323d71443092 68dec7f6cd00384c; do echo \"##### $f\"; grep -n -A12 -i 'frank (adj\\|frank (n\\|parasang (n' $f.txt | head -60; done",
 "description": "Read etymonline extracts"
}
```


## [2026-09-05T20:35:43.554Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 9b15a4610fae692d 5f43029d34370d4f; do echo \"##### $f\"; sed -n '1,200p' $f.txt | grep -n -i -B3 -A12 'etymology' | head -70; done",
 "description": "Read wiktionary parasang and farsang"
}
```


### [2026-09-05T20:35:44.656Z] TOOL RESULT

```
##### cd86323d71443092
23: frank (adj.) 
24-
25- c. 1300, "free, liberal, generous;" 1540s, "outspoken," from Old French franc "free (not servile); without hindrance, exempt from; sincere, genuine, open, gracious, generous; worthy, noble, illustrious" (12c.), from Medieval Latin francus "free, at liberty, exempt from service," as a noun, "a freeman, a Frank" (see Frank ).
26-
27- Frank , literally, 
28- free ; the freedom may be in regard to one's own opinions, which is the same as 
29- openness , or in regard to things belonging to others, where the freedom may go so far as to be unpleasant, or it may disregard conventional ideas as to reticence. Hence, while 
30- openness is consistent with timidity, 
31- frankness implies some degree of boldness. [Century Dictionary] 
32-
33- A generalization of the tribal name; the connection is that Franks, as the conquering class, alone had the status of freemen in a world that knew only free, captive, or slave. For sense connection of "being one of the nation" and "free," compare Latin liber "free," from the same root as German Leute "nation, people" (see liberal (adj.)) and Slavic "free" words (Old Church Slavonic svobodi , Polish swobodny , Serbo-Croatian slobodan ) which are cognates of the first element in English sibling "brother, sister" (in Old English used more generally: "relative, kinsman"). For the later sense development, compare ingenuity .
34- also from c. 1300 
35-
36: frank (n.) 
37-
38- short for frankfurter , by 1916, American English. Franks and beans attested by 1953.
39- also from 1916 
40-
41: Frank (n.) 
42-
43- one of the Germanic tribal people (Salian Franks) situated on the lower Rhine from 3c. that conquered Romano-Celtic northern Gaul c.500 C.E.; from their territory and partly from their language grew modern France and French. Old English franc , franca "freeman, noble; Frank, Frenchman," from Medieval Latin francus , a Late Latin borrowing of Frankish *Frank , the people's self-designation (cognate with Old High German Franko , the Latin word also is the source of Spanish and Italian names Franco ).
44-
45: The origin of the ethnic name is uncertain; it traditionally is said to be from the old Germanic word *frankon "javelin, lance" (compare Old English franca "lance, javelin"), their preferred weapon, but the reverse may be the case. Compare also Saxon , traditionally from root of Old English seax "knife." The adjectival sense of "free, at liberty" (see frank (adj.)) probably developed from the tribal name, not the other way round. It was noted by 1680s that, in the Levant, this was the name given to anyone of Western nationality (compare Feringhee and lingua franca ).
46-
47- frank (v.) 
48-
49- "to free a letter for carriage or an article for publication, to send by public conveyance free of expense," 1708, from shortened form of French affranchir , from a- "to" + franchir "to free" (see franchise (v.)). A British parliamentary privilege from 1660-1840; in U.S. Congress, technically abolished 1873. Related: Franked ; franking . As a noun, "signature of one entitled to send letters for free," from 1713.
50- also from 1708 
51-
52- Entries linking to frank 
53-
54- Feringhee (n.) 
55-
56- name used in India for "European; Englishman; Portuguese," 1630s, from Persian Farangi , from Arabic Faranji (10c.), from Old French Franc "Frank" (see Frank ) + Arabic ethnic suffix -i . The fr- sound is impossible in Arabic.
57-
--
60: late 14c., "to make free," from Old French franchiss- , past participle stem of franchir "to free" (12c.), from franc "free" (see frank (adj.)). Franchising is from 1570s; the commercial licensing sense is from 1966. Related: Franchisee ; franchiser ; franchisor .
61-
62- frankfurter 
63- ingenuity 
64- liberal 
65- lingua franca 
66- Saxon 
67- sibling 
68- farang 
69- franc 
70- France 
71- Francis 
72- franc-tireur 
##### 68dec7f6cd00384c
```


### [2026-09-05T20:35:46.288Z] TOOL RESULT

```
##### 9b15a4610fae692d
59- Toggle English subsection 
60-
61- 1.1 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Translations 
72-
73- 1.4 
74- References 
--
82- Toggle Romanian subsection 
83-
84- 2.1 
85: Etymology 
86-
87- 2.2 
88- Noun 
89-
90- 2.2.1 
91- Declension 
92-
93- 2.3 
94- References 
95-
96- Toggle the table of contents 
97-
--
164-
165- Wikipedia 
166-
167: Etymology
168- [ edit ] 
169-
170- From Latin parasanga , from Ancient Greek παρασάγγης ( parasángēs ) , from unattested Old Persian *frasanhvah [ 1 ] (indigenously attested only in Middle Iranian onwards); compare Middle Persian [script needed] ( frasang /⁠plsng⁠/ , “ frasang (4 Roman miles ) ” ) (whence Persian فرسنگ ( farsang ) ). Doublet of farsang and farsakh .
171-
172- Pronunciation
173- [ edit ] 
174-
175- ( UK ) IPA ( key ) : /ˈpaɹəsaŋ/ 
176-
177- ( US ) IPA ( key ) : /ˈpɛɹəsæŋ/ 
178-
179- Noun
##### 5f43029d34370d4f
62- Alternative forms 
63-
64- 1.2 
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Descendants 
75-
76- 1.5 
77- References 
--
146-
147- فرسخ ( farsax ) 
148-
149: Etymology
150- [ edit ] 
151-
152- From Middle Persian [Book Pahlavi needed] ( plsng /⁠frasang⁠/ , “ parasang ” ) . Compare the Iranian borrowings: Ancient Greek παρασάγγης ( parasángēs ) , Latin parasanga , Old Armenian հրասախ ( hrasax ) , Arabic فَرْسَخ ( farsaḵ ) , Aramaic פַּרְסָה , פַּרְסָא ( parsâ ) , Mishnaic Aramaic פָּרָשָׁה ( pārāšâ ) , Classical Syriac ܦܪܣܚܐ ( prsḥʾ /⁠parsḥā⁠/ ) .
153-
154- Pronunciation
155- [ edit ] 
156-
157- ( Classical Persian ) IPA ( key ) : /far.ˈsanɡ/ 
158-
159- ( Dari, formal ) IPA ( key ) : [fäɾ.sáŋɡ] 
160-
161- ( Dari, formal ) IPA ( key ) : [fäɾ.sáŋɡ]
```


## [2026-09-05T20:35:56.867Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 3da86dfad99e809b 7faa2456d366e478 ab6e921b7f3cfad7; do echo \"##### $f\"; awk '/^Etymology$/{c=1} c{print} ' $f.txt | head -25; echo; done",
 "description": "Read wiktionary farang, ifranji, faranse"
}
```


### [2026-09-05T20:35:58.965Z] TOOL RESULT

```
##### 3da86dfad99e809b

##### 7faa2456d366e478

##### ab6e921b7f3cfad7
```


## [2026-09-05T20:36:00.878Z] TOOL CALL #25: Bash

```json
{
 "command": "for u in \"https://www.iranicaonline.org/articles/farsak\" \"https://en.wiktionary.org/wiki/%CF%80%CE%B1%CF%81%CE%B1%CF%83%CE%AC%CE%B3%CE%B3%CE%B7%CF%82\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Germanic/Frank\" \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B3%D8%AE\"; do echo \"### $u\"; timeout 90 python3 tools/fetch_source.py \"$u\" --note \"pdf page 164: Frankon / Fra-sanga verification\" 2>&1 | tail -2; done",
 "description": "Archive web sources batch 2"
}
```


### [2026-09-05T20:36:08.056Z] TOOL RESULT

```
### https://www.iranicaonline.org/articles/farsak
/home/sfmqrb/git/rishe/data/verification/sources/web/e6173c9424680e45.txt
### https://en.wiktionary.org/wiki/%CF%80%CE%B1%CF%81%CE%B1%CF%83%CE%AC%CE%B3%CE%B3%CE%B7%CF%82
/home/sfmqrb/git/rishe/data/verification/sources/web/e7ecd9b7bc4d2809.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Germanic/Frank
/home/sfmqrb/git/rishe/data/verification/sources/web/bfa8c52e87764f41.txt
### https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B3%D8%AE
/home/sfmqrb/git/rishe/data/verification/sources/web/5ad6ae9d67049765.txt
```


## [2026-09-05T20:36:10.959Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 3da86dfad99e809b 7faa2456d366e478 ab6e921b7f3cfad7; do echo \"##### $f  ($(wc -c <$f.txt) bytes)\"; grep -n -i -A8 'Etymology' $f.txt | head -40; echo; done",
 "description": "Re-read wiktionary pages"
}
```


### [2026-09-05T20:36:12.826Z] TOOL RESULT

```
##### 3da86dfad99e809b  (7036 bytes)
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
--
167: Etymology
168- [ edit ] 
169-
170: Etymology tree
171-
172- Proto-Germanic *frankô 
173- Frankish *Frankō bor. 
174- Latin francus 
175- Old French franc bor. 
176- Persian فرنگ 
177-
178- Borrowed from Old French franc .
--
324: Pages with etymology trees 
325: Persian entries with etymology trees 
326: Persian entries with etymology texts 
327- Pages using etymon with no ID 
328- Pages with entries 
329- Pages with 1 entry 
330- Requests for translations of Persian quotations 
331- Undetermined language links 
332- Undetermined term requests 
333-
334- This page was last edited on 5 September 2026, at 00:33.

##### 7faa2456d366e478  (11577 bytes)
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
--
147: Etymology
148- [ edit ] 
149-
150: Etymology tree
151-
152- Proto-Germanic *frankô 
153- Frankish *Frankō bor. 
154- Latin francus 
155- Old French franc bor. 
156- Arabic إفرنجي 
157-
158- Borrowed from Old French franc . First attested in 1895.
--
744: Pages with etymology trees 
745: Arabic entries with etymology trees 
746: Arabic entries with etymology texts 
747- Pages using etymon with no ID 
748- Pages with entries 
749- Pages with 1 entry 
750-
751- This page was last edited on 5 September 2026, at 01:14.
752-
753- Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
754-

##### ab6e921b7f3cfad7  (6215 bytes)
79: Etymology 
80-
81- 2.3 
82- Pronunciation 
83-
84- 2.4 
85- Proper noun 
86-
87- 3 
--
93: Etymology 
94-
95- 3.2 
96- Pronunciation 
97-
98- 3.3 
99- Proper noun 
100-
101- 3.3.1 
--
226: Etymology
227- [ edit ] 
228-
229- Borrowed from Persian فرانسه ( farânse ) .
230-
231- Pronunciation
232- [ edit ] 
233-
234- IPA ( key ) : /ɸr.ɑn.sa/ 
--
254: Etymology
255- [ edit ] 
256-
257: Etymology tree
258-
259- Proto-Germanic *frankô 
260- Frankish *Frankō bor. 
261- Latin francus 
262-
263- Proto-Indo-European *-(i)yós
```


## [2026-09-05T20:36:20.553Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '250,300p' ab6e921b7f3cfad7.txt; echo \"=== IRANICA farsakh ===\"; sed -n '1,120p' e6173c9424680e45.txt | grep -v '^\\s*$' | head -60",
 "description": "Read faranse Persian section and Iranica farsakh"
}
```


### [2026-09-05T20:36:22.154Z] TOOL RESULT

```
 Persian Wikipedia has an article on: فرانسه 

 Wikipedia fa 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Germanic *frankô 
 Frankish *Frankō bor. 
 Latin francus 

 Proto-Indo-European *-(i)yós 
 Proto-Italic *-ijos 
 Proto-Italic *-ios 
 Old Latin -ios 
 Latin -ius 
 Latin -ia 

 Late Latin Francia der. 
 Persian فرانسه 

 Ultimately from Late Latin Francia ( “ land of the Franks ” ) . Likely transmitted via intermediary languages; compare Arabic فَرَنْسَا ( faransā ) and Italian Francia /ˈfran.t͡ʃa/.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /fa.raːn.ˈsa/ 

 ( Dari, formal ) IPA ( key ) : [fä.ɾɑːn.sá] 

 ( Dari, formal ) IPA ( key ) : [fä.ɾɑːn.sá] 
 ( Kabuli ) IPA ( key ) : [fä.ɾɑːn.sá] 

 ( Hazaragi ) IPA ( key ) : [fä.ɾɔːn.sá] 

 ( Iran, formal ) IPA ( key ) : [fæ.ɹɒːn.sé] 

 ( Tajik, formal ) IPA ( key ) : [fä.ɾɔn.sá] 

 Rhymes: -a 

 Readings

 Classical reading ? 

 farānsa

 Dari reading ? 

=== IRANICA farsakh ===
URL: https://www.iranicaonline.org/articles/farsak
FETCHED: 2026-09-05T20:36:05Z
STATUS: -1
TITLE: 
FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-05T20:36:34.937Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM فرسخ / افرنج ===\"; grep -n 'فرسخ\\|فرسنگ\\|افرنج' AFM.txt | head -10; echo \"=== LKT ===\"; grep -n -i 'parasang\\|farsang\\|frank\\b\\|ifrang\\|firengi' LKT.txt | head -20; echo \"=== PLA ===\"; grep -n -i 'farsa\\|frasang' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10",
 "description": "Grep Addi Shir, Lokotsch, Asbaghi"
}
```


### [2026-09-05T20:36:35.013Z] TOOL RESULT

```
=== AFM فرسخ / افرنج ===
=== LKT ===
1886:Eine  Pflanze  aus  der  Familie  der  Legu- minosen, aus  dem  Orient  nach  Frank- reich gebracht  und  als  sainfoin  alhagi, Alhagi  maurorum,  im  Jahre  1537  von RAUWOLF  beschrieben;  die  ganze  Fa- milie heißt  frz.  alhagees.  [Devic  DEt 19.    Lammens  Rem  14.
=== PLA ===
4138:Es ist eine Nebenform v. a farsah pers. iu; farsang 2, 
8657:od. farsak "Pfirsichkerne" gefüllt sind z. B.: mazafbäan "Marzipan", 
15079:zb - faräsih: Pl. v. > farsah a. v. 
15204:> - farsah: "Parasange,; ein persisches Maß, ungefähr 6232 mt pers. 
15205:Li farsang > mp. sd o frasang ap. *frasanga "a parasang" 6, 
15208:Bw - farsak: "Pfirsich", dtsch. Pfirsich s. mazad ıl, 
18100:Persipan: aus , farsak "Pfirsich" + sb Fänid.
```


## [2026-09-05T20:36:37.104Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB frasang ===\"; grep -n -i 'frasang' NYB_vol2_glossary.txt | head; echo \"=== SKT parasang ===\"; grep -n -i 'parasang' SKT.txt FSD_vol*.txt WEB_vol1.txt 2>/dev/null | head; echo \"=== ARY ===\"; grep -n 'فرسنگ' incoming/ARY/ARY_pages.txt | head",
 "description": "Grep Nyberg, Skeat, FSD, Webster, Aryanpur"
}
```


### [2026-09-05T20:36:37.193Z] TOOL RESULT

```
=== NYB frasang ===
394:of; o pattākēh ~ to appear 513, 1081; 6 patirak ~ to meet 8%. 731.20-21, ete.; 6 en kustak rón towards this district 715; — with hac: from 184 ete. [hac ... be 6 ... ~ to be converted from... to... PR 945]; hac ... ywvatük away from 747-8, 7667; — with pat: on (a path) ibd. ; — with prev.: andar — to come forth, to appear 87?5; to be handed down 10818-19; — apāc ~ to become again 104?*; apdc 6 to return to 5) (v. bälist). 818-19, 914, 12]9-10; hac ... apāc ~ to return from 991; — apar ~ to shoot up 9573-4; to be allotted to 98*; apértar apar āyēt ku surpas- ses 641%; — hac varten beron be ämat got off the chariot 20?3; (coursers) ke pat róc-6 70  frasang bē āyēnd- (h)b who are always riding a dis- tance of 70 parasangs in one day 6! (v.s.v. h-); hān<i>druž (be) āyēt the space which the Drug will cover 96?3, 9818; bé + the pres. of ~ regularly denotes the fut.: 24"; if the vb. takes the prep. 6 the order is always be 6: 9725, 985-6, 9912-13, 1046-7; — fröt ~ to come down, to descend (hac...6...) 104°; — ul ~ to rise 86°; šuhr pat post ul āmat the sperm rose to the skin 547°. — āmatan < *ā-gmatanai from à + Av. (493 sqq.) OP gam-, cf OP (par)ägmata- ‘gone forth’; äy- < à + Av. (147 sqq.) OP ay-; MPrs ’mdn ”y-; Paz. NP dmadan dy-. This vb. is characteristic of the SW dialects, as against NW āgatan,
1541:frasang [plsng] a parasang, the Persian league, estimated at an average of 6232 m., but varying in length (31/,-4 English miles): 719. 89.6, 7225, 937-11, 9623, 9817, 11471. — OP *frasanga- borrowed in Gr as rapacodyyns, Paz. NP farsang; NW form *frasaxa-, Arm. lw. hrasax, Syr. lw. prsh’, Talm prse, Mand prs’, Arab fjarsax-. V. Christensen, Iranier 283; How and Wells, Comm. on Herodotus Y, 161; EI? II, 832.
2018:~ kunom kū I make (it) in order to symbolize 120 passim; pat cim + kārēcār ~ kart constructed it to represent the - conditions of a battle 1198; — about: kötak 7-sälak ~ about seven years old 264°; 40-sālak ~ 119; € frasang ~ 7275-28, — « *ham-manak, with ha- > ho- because of the labial, v. s. v. mänäk(k)äi; Paz. humana; NP hamänä, cf zamänä ‘rival’. homanikčh [hwm’n’kyh],  homanač [hwm’n’y 9219] resemblance: ~ % én hàn hast i ket ... guft this is suggestive of what the diviner said 173; api-š — čton cigön it resembles 921%. — hwm’n’y is in other places to be read homänäi = homänäk, but in 92!? the abstr. is necessary.
2431:imar [ml] calculation, number, comput- ation: pat han 4 cašm vibarišn ~ paitäk visible by calculating the range of sight = far and wide, as far as eye can reach 382; pat héc ~ -ic ... nē by no calculation 71821; y frasang ~ vēš x parasangs and more, and upwards (properly: the number
2576:miyàn [myd’n'] 1. the middle, the centre: bun ...miyün... frazdm 81; x"atài 4 ~ i asmān 78; han-tāi 6 ~ van to the middle of the tree 415; andar ~ 4 asmän 865; hac ~ dp from the middle of the water 564; — pat ~ kartan to make manifest to all, splendid 67°; 6 ~ apa- kandan to spread, disseminate 10715, — 2. prep. between: + smäh u oan damik i 30 frasang 8%; vimand i ~ Eran u Türän 4519-311; in the middle of 4815, 865. — Av. (1115 sq.) Tmaiöya-, (116 sq.) matčyčna-; MPrth mdyn; MPrs my; Paz. NP myàn.
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
4005:frasang many parasangs 7%; ~ simén, ~ asp névak 1965; — with a personal subst.: —-än martöm (cas. obl.) 418, but also ~ frazänak martom (cas. obl.) 455; ~ āzātān u vazurgän (cas. obl.) 16°; ~-dn vazurg-spāsān (for cas. rect.) 1061; — less often placed after its subst. without or with the izGfat: névakéh ~ 351; anākēh ~ 95* (as against pat ~ andkéh 761); hesm i ~ 4815; gāvān + ~ 483-26; aspān i ~ 4013, — 2. as a pred.: numerous, great 41, 201? sq. 871; — in a compound: hesm ~ quick to anger 1074. — 3. subst. pl. cas. obl: 6 ~-dn to many people 3643 and passim. — 4. adv. very: ~ vazurg 8’; ~ pahréc 55°; — ka —-ic however much 463, 8122-23, 9112. — OP vasiy; MPrthPrs ws; Paz. vas; NP bas.
7133:farāmēš: frāmēš faräx, frax": faraz: frac farda: fratak farhanjidan: frahaxtan Faridün: Fréton farjam: frazäm farman: framan farmudan, farmay-: framatan farrah: x"arrah farrux: farraxu farsang: frasang farsüdan, farsäy: apa- sutak farvardgän, faravardigän: fravartikän faryäd: friyät farzänah: frazänak farzand: frazand
=== SKT parasang ===
FSD_vol3.txt:19590:- parasangisa
FSD_vol3.txt:25119:Persia * 3 geog m parasang;. ■“agasche;. agasha;.
FSD_vol4.txt:3611:Schem'nitz,  1   ^em'nlts  2Bh6m'nIts,  n   A   city  in  8   Czecho- slovak Republic,  has  gold,  silver,  and  other  mines Schcnck,  1   skeok,  2   scCok,  Robert  Ouiiiming  (W/<1809- Vm1890)  An  American  general  and  diplomat scheiie,  1   skin,  2   seen,  n   An  antlcnt  Lgyptlan  measure  of length,  of  about  4   English  miles,  or  nearly  equal  to  the Persian  parasang  said  to  be  the  distance  traveled  by  a   relay of  men  towing  a   boat  up  the  Nile  [<  L   schcenus  (<  Gr schoinos),  measure  ]
=== ARY ===
```


## [2026-09-05T20:36:50.353Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndef leafof(path, lineno):\n    t=open(path,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    idx=sum(len(l)+1 for l in lines[:lineno-1])\n    return t[:idx].count('\\f')\nfor p,l in [('KLN_1966.txt',15326),('KLN_1966.txt',27341),('NYB_vol2_glossary.txt',1541),('incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt',15204),('HJB.txt',9641),('AHD_watkins1985.txt',474),('AHD_watkins1985.txt',1537)]:\n    print(p,l,'leaf',leafof(p,l))\nEOF",
 "description": "Compute leaf numbers for cited lines"
}
```


### [2026-09-05T20:36:52.531Z] TOOL RESULT

```
KLN_1966.txt 15326 leaf 335
KLN_1966.txt 27341 leaf 602
NYB_vol2_glossary.txt 1541 leaf 88
incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt 15204 leaf 0
HJB.txt 9641 leaf 405
AHD_watkins1985.txt 474 leaf 47
AHD_watkins1985.txt 1537 leaf 122
```


## [2026-09-05T20:37:42.074Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in (178,335,602):\n    print('--- leaf',n,'first 200 chars:',repr(pages[n][:200]))\nEOF",
 "description": "Inspect Klein leaves"
}
```


### [2026-09-05T20:37:44.161Z] TOOL RESULT

```
--- leaf 178 first 200 chars: ' coeno-).  Cp.  1st  con-,  contra-, count,  ‘title  of  nobility’.  Cp.  also  y-. coma,  n.,  a  state  of  insensibility.  —  ModL.,  fr. Gk.  xolpta,  ‘a  deep  sleep,  lethargy’,  which  is  prob'
--- leaf 335 first 200 chars: 'f  two  old  French  coins,  one  of gold  and  the  other  of  silver;  now  the  monetary unit  of  France.  —  F.,  from  the  ML.  legend  on the  first  coin:  Francorum  rex  (‘king  of  the Fra'
--- leaf 602 first 200 chars: ' parametrium (med.)  —  Medical  L.  See  next  word  and  -itis. Derivative:  parametrit-ic,  adj. parametrium,  n.,  the  connective  tissue  around  the uterus  (anat.)  —  ModL.,  fr.  Gk.  7tapa '
```


## [2026-09-05T20:37:55.027Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in (335,602):\n    p=pages[n]\n    print('=== leaf',n,'len',len(p))\n    print(repr(p[-300:]))\n    print('digits found:', re.findall(r'\\b(\\d{3,4})\\b', p)[:20])\nEOF",
 "description": "Look for printed page numbers in Klein leaves"
}
```


### [2026-09-05T20:37:56.903Z] TOOL RESULT

```
=== leaf 335 len 11493
'and  intr.  v.,  to  fray;  to  reduce  to  tat¬ ters.  —  A  blend  of  fray,  ‘to  wear  out  by  rub¬ bing’,  and  G.  faseln,  ‘to  separate  the  fibers,  to ravel  out’,  which  is  rel.  to  G.  Faser,  ‘thread, fiber,  filament’,  OE.  fees,  ‘fringe’,  and  to  obsol. E.  feaze,  ‘to  unrav'
digits found: ['182', '1226', '1909', '1818', '1825', '1750', '1811', '1787', '1826']
=== leaf 602 len 10897
"tapaa'JvffsaK ‘formation  from  a  compound’. See  para-,  ‘beside’,  and  synthesis, parasynthetic,  adj.,  pertaining  to,  or  formed  by, parasynthesis.  —  Fr.  Gk.  napaouvffeTop,  ‘form¬ ed  from  a  compound’.  See  para-  and  synthetic, paratactic,  adj.,  pertaining  to  parataxis.  —  Fo"
digits found: ['0197', '1126']
```


## [2026-09-05T20:38:14.293Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WEB parasang ===\"; grep -n -i 'parasang' WEB_vol1.txt | head -5; echo \"=== MON فرسنگ ===\"; grep -n 'فرسنگ' incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -5; echo \"=== MON فرانسه ===\"; grep -n 'فرانسه' incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -5; echo \"=== MON فرنگ ===\"; grep -n 'فرنگ ' incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -5",
 "description": "Grep Webster and Mo'in"
}
```


### [2026-09-05T20:38:14.388Z] TOOL RESULT

```
=== WEB parasang ===
=== MON فرسنگ ===
12122:(نظ. قد.) مکانی بلند قریب یکث فرسنگ 
22602:رشیدی به معنی ثلث فرسنگ (که یک میل 
70622:۰ گام (قدم و سپس فرسنگ) در 
88639:ایران باستان و آن معادل یک فرسنگ و 
88640:یک فرسنگ معادل هزار گام و هر گام 
=== MON فرانسه ===
5811:فرانکك فرانسه که قبل از دوگل معمول بود و 
5814:(فرانسه): معادل صد فرانکك قدیم است و 
19520:در فرانسه و ایتالیا به فراوانی کشت و تربیت 
20557:کتاب زرد در فرانسه» کتاب خاکستری در 
22596:حوزه کر ومانیون (فرانسه) بدست آمده. 
=== MON فرنگ ===
1377:موسیقی. . فرنگ و غریو؛ آه و اله و فر باد. 
18670:کاغذ اطفال. کاغذ بتی: کاغذی که در فرنگ 
18820:بت پرست. کافر فرنگ: مردم فرنگ به دینی 
85943:فرنگ برقرار گردید» (الماثر و الاثار.
```


## [2026-09-05T20:38:16.925Z] TOOL CALL #34: Bash

```json
{
 "command": "for u in \"https://vajehyab.com/moein/%D9%81%D8%B1%D8%B3%D9%86%DA%AF\" \"https://vajehyab.com/moein/%D9%81%D8%B1%D9%86%DA%AF\" \"https://www.etymonline.com/word/franchise\" \"https://en.wiktionary.org/wiki/farang\"; do echo \"### $u\"; timeout 90 python3 tools/fetch_source.py \"$u\" --note \"pdf page 164: Frankon / Fra-sanga verification\" 2>&1 | tail -1; done",
 "description": "Archive Mo'in online and etymonline franchise"
}
```


### [2026-09-05T20:38:20.523Z] TOOL RESULT

```
### https://vajehyab.com/moein/%D9%81%D8%B1%D8%B3%D9%86%DA%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/c89772e9c2948798.txt
### https://vajehyab.com/moein/%D9%81%D8%B1%D9%86%DA%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/eca4ba0c3afbe28b.txt
### https://www.etymonline.com/word/franchise
/home/sfmqrb/git/rishe/data/verification/sources/web/834efad5db143412.txt
### https://en.wiktionary.org/wiki/farang
/home/sfmqrb/git/rishe/data/verification/sources/web/500947c5e05d3b45.txt
```


## [2026-09-05T20:38:23.353Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in c89772e9c2948798 eca4ba0c3afbe28b; do echo \"##### $f\"; grep -n 'فرسنگ\\|فرنگ\\|په\\.\\|فر\\.' $f.txt | head -12; done; echo \"=== franchise ===\"; grep -n -A4 'franchise (n' 834efad5db143412.txt | head -20",
 "description": "Read vajehyab Mo'in entries and etymonline franchise"
}
```


### [2026-09-05T20:38:44.960Z] TOOL RESULT

```
##### c89772e9c2948798
4:TITLE: معنی فرسنگ | فرهنگ انتشارات معین | واژه یاب
9: معنی فرسنگ | فرهنگ انتشارات معین | واژه یاب 
17: فرسنگ
##### eca4ba0c3afbe28b
4:TITLE: معنی فرنگ | فرهنگ انتشارات معین | واژه یاب
9: معنی فرنگ | فرهنگ انتشارات معین | واژه یاب 
17: فرنگ
20: (فَ رَ) [ فر. ] (اِ.) 1 - نام عمومی هر یک از کشورهای اروپا و گاهی آمریکا. 2 - کشور فرانسه که مسکن قوم فرانک (قبیله ای از نژاد ژرمن ) است .
=== franchise ===
23: franchise (n.) 
24-
25- c. 1300, fraunchise , "a special right or privilege (by grant of a sovereign or government);" also "national sovereignty; nobility of character, generosity; the king's authority; the collective rights claimed by a people or town or religious institution," also used of the state of Adam and Eve before the Fall, from Old French franchise "freedom, exemption; right, privilege" (12c.), from variant stem of franc "free" (see frank (adj.)).
26-
27- From late 14c. as "freedom; not being in servitude; social status of a freeman;" early 15c. as "citizenship, membership in a community or town; membership in a craft or guild." The "special right" sense narrowed 18c. to "particular legal privilege," then "right to vote" (1790). From mid-15c. as "right to buy or sell," also "right to exclude others from buying or selling, a monopoly;" meaning "authorization by a company to sell its products or services" is from 1959.
```


## [2026-09-05T20:38:58.944Z] TOOL CALL #36: Bash

```json
{
 "command": "timeout 400 python3 tools/ref_page.py BQT:1462 --image 2>&1 | tail -8",
 "description": "Render Borhan page 1462 image"
}
```


### [2026-09-05T20:39:00.972Z] TOOL RESULT

```
ععرب « فرسخ > * نیب رکه ۷۳ > «اسشق - هوبشمان ۸۱۸ : * برسید بر کنار آبی
که سنگه از صلابت او برسنگه همی‌آمد و صربرش بفرسنگه همی رفت .> «کلتان ۱۱۷*.
8 _- از : فرسنکه سار (حدس) ۱ پوند مکان). [ هه اسم‌مقعول از«فرسودن».
۷ ه فرشه (ه.م.) ۰
2 فرسودن - بفتح اول وپنجم < فرساییدن از ۲2-58 ؛ اوستا 5288 - 1۳3(محو
و نابود کردن) « پارتولمه ۱۶*۱ > « نیب رکه ۷۳ : 11382۷2800 > ؛ سودن » سایدن -.
مالیدن » زدودن - ساییده شدن -کهنه شدن - پیرشدن - پوسیدن .
```


## [2026-09-05T20:39:01.846Z] TOOL CALL #37: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D9%81%D8%B1%D8%B3%D9%86%DA%AF/\" \"https://abadis.ir/fatofa/%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%87/\"; do echo \"### $u\"; timeout 90 python3 tools/fetch_source.py \"$u\" --note \"pdf page 164: MON check for فرسنگ / فرانسه\" 2>&1 | tail -1; done",
 "description": "Archive abadis Mo'in entries"
}
```


### [2026-09-05T20:39:06.760Z] TOOL RESULT

```
### https://abadis.ir/fatofa/%D9%81%D8%B1%D8%B3%D9%86%DA%AF/
/home/sfmqrb/git/rishe/data/verification/sources/web/20c6b00e70b068db.txt
### https://abadis.ir/fatofa/%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%87/
/home/sfmqrb/git/rishe/data/verification/sources/web/3ea863581416675c.txt
```


## [2026-09-05T20:39:09.298Z] TOOL CALL #38: Bash

```json
{
 "command": "ls -la data/verification/sources/refs/ocr/BQT/ 2>/dev/null | grep 1462",
 "description": "Locate cached BQT page image"
}
```


### [2026-09-05T20:39:09.354Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb 384649 Sep  5 16:34 1462.png
-rw-rw-r--  1 sfmqrb sfmqrb   3664 Sep  5 16:34 1462.txt
```


## [2026-09-05T20:39:10.857Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### farsang abadis\"; grep -n -i 'معین\\|پهلوی\\|فرسنگ' 20c6b00e70b068db.txt | head -15; echo; echo \"### faranse abadis\"; grep -n -i 'معین\\|فرانسه' 3ea863581416675c.txt | head -12",
 "description": "Read abadis entries"
}
```


### [2026-09-05T20:39:10.917Z] TOOL RESULT

```
### farsang abadis
4:TITLE: فرسنگ - معنی در دیکشنری آبادیس
6:فرسنگ - معنی در دیکشنری آبادیس 
10: فرسنگ
13: مترادف فرسنگ : فرسخ
20: فرسنگ. [ ف َ س َ ] ( اِ ) پهلوی فرسنگ ( مقیاس طول )، پارسی باستان ظاهراً فرسنگا و صورت یونانی شده آن پراساغس و معرب آن فرسخ است. ( از حاشیه برهان چ معین ). قدری باشد معین از راه و آن به مقدار سه میل است و هر میلی چهارهزار گز باشد و طول هرگزی به قدر بیست وچهار انگشت دست باشد که به عرض در پهلوی هم گذارند و آن شش قبضه است یعنی شش مشت. ( برهان ). فرسنگ ایرانی قدیم برابر با چهارهزار و چهارصد و سی وسه یا سی ودو گز بوده است. ( از ایران باستان پیرنیا جدول اندازه ها در ج 1 ص 166 ). هر فرسنگی سه میل باشد و هر میلی چهارهزار و پانصد ارش به ذراع مرسل وسه هزار ارش به ذراع سلطان و هر ذراعی سی وشش انگشت که هر یکی به مقدار شش جو از پهنا به هم برنهاده. ( مجمل التواریخ و القصص ). مقدار طولی که امروز یک فرسنگ یا فرسخ به شمار میرود شش کیلومتر است : 
21:تهمتن دو فرسنگ با او برفت 
23:دو فرسنگ چون اژدهای دژم 
25:به دور از دو فرسنگ هر کس بدید
28:نه فرسنگی و نه فرسنگساری. لبیبی.
30:از دل ابدال بگریزد به یک فرسنگ سنگ. منوچهری.
32:بیست فرسنگ زمین بیش بود لشکرگاه. منوچهری.
33:چون فرسنگی کنار رود برفت آب پایاب داشت. ( تاریخ بیهقی ).
35:تو از اودور شو به صد فرسنگ. ناصرخسرو.
37:چند بسیار تاختی فرسنگ. ناصرخسرو.
38:صحرای دلم هزار فرسنگ 

### faranse abadis
4:TITLE: فرانسه - معنی در دیکشنری آبادیس
6:فرانسه - معنی در دیکشنری آبادیس 
10: فرانسه
19: ( فرانسة ) فرانسة. [ ف َ ن ِ س َ ] ( ع اِ ) ج ِ فرناس که به معنی رئیس دهاقین است. ( منتهی الارب ) ( از اقرب الموارد ). فرانسه. [ ف َ س ِ ] ( فرانسوی ، اِ ) نام زبانی است که مردم کشور فرانسه بدان گفتگو کنند. رجوع به فرانسه و فرانسوی شود.
20: فرانسه. [ ف َ س ِ ] ( اِخ ) کشوری است که در آخرین قسمتهای غربی قاره اروپا بین 51 درجه و 9 دقیقه تا 42 درجه و 23 دقیقه عرض شمالی واقع است و طول جغرافیایی آن از 4 درجه و 38 دقیقه غرب گرینویچ تا 8 درجه و 10 دقیقه شرق آن نصف النهار است. وسعت خاکش 212721 میل مربع و پس از اتحاد جماهیر شوروی ، بزرگترین کشور اروپاست. درازترین قطر آن از دنکرک در ساحل شمالی ، تا پیرنه در حدود 621 میل میشود و بلندترین قطر عرضی آن هم در همین حدود است. این کشور تقریباً از همه طرف ، به جز مرز بلژیک ، با مناظر طبیعی ازقبیل کوه ، دریا و رودخانه احاطه شده است. پستی وبلندی های این سرزمین در دوران های مختلف زمین شناسی تحولات فراوانی به خود دیده است. رشته های آلپ و پیرنه از آثار دوران سوم است. خاک فرانسه تقریباً به طور مساوی به دشتهای مسطح و تپه ها وکوهستانها تقسیم شده است و بلندترین قسمتهای مرتفع آن منطقه کوهستانی آلپ است که در جنوب شرقی آن قراردارد و بلندی آن در خاک فرانسه گاه به بیش از ده هزار پا از سطح دریا میرسد ( بلندترین قله آلپ ، مُن بلان 15781 پا ارتفاع دارد ).
21:سرزمین فرانسه از نظر ساختمان طبیعی به حوزه های مختلف تقسیم میشود که هر کدام به نام بزرگترین شهرستان آن حوزه خوانده میشوند و عبارتند از حوزه های : پاریس ، نرماندی ، بریتانی ، لوار ، دشت های جنوب غربی ، ماسیف سانترال ، پیرنه ، کنارهای مدیترانه ، ناحیه آلپ ، ژورا ،دره راین و ووژ . سواحل مدیترانه قسمت عمده ای از محصولات طبیعی فرانسه را پرورش میدهد. زیتون ، انگور، انواع توت و میوه های دیگر در این قسمت به دست می آیند. حیواناتی که در این کشور زندگی میکنند بسیار متنوع اند. بالغ بر 90 گونه پستاندار از وحشی و اهلی در جنگل ها و روستاهای فرانسه دیده میشود. مطالعات زمین شناسی نشان میدهد که روزی در حوزه رود رن و حتی در ناحیه پاریس حیواناتی از قبیل ماموت ها میزیسته اند و سنگواره های آنها را زمین شناسان به دست آورده اند. آب و هوای فرانسه در همه جا یکسان نیست و در این سرزمین دو نوع آب و هوای متفاوت و ممتاز از هم دیده میشود.قسمت ساحلی مغرب که مجاور اقیانوس اطلس است بارانی و متغیر است. کوهستانها رگبارهای شدید دارد. در شمال و مغرب فرانسه که همان کناره اقیانوس است بادهای موسمی شدیدی در فصل زمستان میوزد که نظیر آن در قسمتهایی که آب و هوای اروپایی دارد دیده نمیشود. در این سرزمین از حدود سال 500 م. پادشاهی مستقل به وجود آمد و دولتی جدا از سازمان امپراتوری رم تشکیل شد. نخستین خاندانی که بر این کشور حکمرانی کرده اند به «مروانژیان » معروفند. مؤسس این سلسله شخصی به نام کلویس بود که پس از مرگش متصرفات او به چهار پادشاهی کوچکتر تقسیم شد. خاندان دیگر «کارولینژیان » هستند که از معروفترین پادشاهان آنها شارل مارتل است. شارلمانْی پادشاه معروف فرانسه از افراد این خانواده است. بیشتر بخوانید ... 
25: در اصطح متداول به معنی زبان فرانسوی بکار میرود و آن یکی از شعب زبانهای تینی ( هند و اروپایی ) است . این زبان در عهد قاجاریه نخستین زبان خارجی ( اروپایی ) برای ایرانیان محسوب میشد و این امر تا آغاز جنگ جهانی دوم ادامه داشت و اکنون هم یکی از مهمترین زبانهای خارجی متداول در ایران بشمار میرود . توضیح در عهد قاجاریه نخست [ زبان فرانسه ] ( یعنی زبان کشور فرانسه ) مصطلح بود : [ مسیوریشار سرتیپ معلم زبان فرانسه ] ( مر آه البلدان ج ۱ ضمیمه ص ۲۶ ) و بعد [ زبان ] را حذف کردند و [ فرانسه ] گفتند .
30: ۱. از مردم فرانسه.
31:۲. زبان مردم فرانسه: کلاس فرانسه. 
35: [ویکی شیعه] فرانسه کشوری در غرب اروپا که مسلمانان از قرون اولیه و به دنبال حضورشان در اندلس، در فرانسه نیز حضور دارند. شیعیان نیز در این کشور حضور فعالی دارند و بنابر برخی آمار، جمعیتی بیش از ۳۵۰.۰۰۰ نفر شیعه در این کشور فعال است. شیعیان لبنان، ایران، عراق، پاکستان و همچنین فرانسوی الاصل از مهم ترین گروه های شیعی این کشور هستند.
36:فَرانسه با عنوان رسمی جمهوری فرانسه یکی از کشورهای واقع شده در اروپای غربی می باشد که دارای چند منطقه تحت حاکمیت نیز است. فرانسه یکی از سه کشوری است که دارای سواحی هم در دریای مدیترانه و اقیانوس اطلس دارد (دو کشور دیگر عبارتند از اسپانیا و مراکش). بخاطر ظاهر این کشور، در زبان فرانسوی به آن لقب l’Hexagone (معنی: شش ضلعی) را داده اند.
37:بر اساس مساحت، فرانسه بزرگ ترین کشور اروپای غربی و اتحادیه اروپا و همچنین سومین کشور بزرگ در کل قاره اروپا بشمار می آید. جمعیت فرانسه در حال عبور از مرز ۶۷ میلیون نفر است که با این رقم، فرانسه در رتبه دومین کشور پرجمعیت اتحادیه اروپا قرار می گیرد. مرکز فرانسه، شهر پاریس است. پاریس بزرگ ترین شهر این کشور و مرکز اصلی تجارت و فرهنگ فرانسه است. wikishia: فرانسه
```


## [2026-09-05T20:39:45.441Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AFM افرنج/فرنج ==\"; grep -n 'فرنج\\|فرنك\\|فرنگ' AFM.txt | head -8; echo \"== TAD ==\"; grep -n 'فرنج\\|إفرنج\\|افرنج\\|فرسخ' TAD.txt | head -8; echo \"== ARB ==\"; grep -n 'فرسخ\\|إفرنج\\|افرنج' ARB_mo3rb.txt ARB_abdulraheem.txt 2>/dev/null | head -8; echo \"== FVQ farsakh ==\"; grep -n -i 'farsakh\\|farsax\\|ifranj' FVQ.txt | head -5",
 "description": "Grep Arabic loan dictionaries"
}
```


### [2026-09-05T20:39:45.556Z] TOOL RESULT

```
== AFM افرنج/فرنج ==
415:و 5.5 1ل يك »هيع (فرنكل ض : \ \ ¥) 
1350:(فرنكل ص:5١1١)‏ 
1684:روسة 19 فرنكل ( ܟ : \ ܘ) 1 خمفة من ܐܟܐܠ 0 اي المرجان ٠‏ 
2575:والماندوي ܓܪܐܡܟܐ ( طالع فرنكل ص 07 
3198:( حيط المحيط ) واب فرنكل (ص: : 87) فيجعلها معربة عن ( ܨ ܐ واصل معناها 
3309:فرنكل ص :^« 
4420:فك الصفر ألا بها <٠‏ واجع 08 فرنكل ܩܨ : ܘ \ \ ) ‹ ܬܝ )ܩܢ 77 ܣ ܣܨ 
4692:2001/0 (راجع فرنكل:ص: 7385 ) : ̣ 
== TAD ==
== ARB ==
== FVQ farsakh ==
```


## [2026-09-05T20:39:50.219Z] TOOL CALL #41: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py",
 "description": "Read verify_check tool"
}
```


### [2026-09-05T20:39:50.255Z] TOOL RESULT

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


## [2026-09-05T20:39:52.114Z] TOOL CALL #42: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py",
 "description": "Read rest of verify_check"
}
```


### [2026-09-05T20:39:52.152Z] TOOL RESULT

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


## [2026-09-05T20:41:04.585Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== etymonline parasang ===\"; sed -n '1,60p' 68dec7f6cd00384c.txt | grep -v '^\\s*$' | head -25; echo; cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY فرانسه/فرنگ ===\"; grep -n 'فرانسه\\|فرنگ' incoming/ARY/ARY_pages.txt | head -5; echo \"=== BQT_v3 فرانسه ===\"; grep -n 'فرانسه' incoming/BQT/BQT_v3_pages.txt | head -3",
 "description": "Check etymonline parasang and Aryanpur"
}
```


### [2026-09-05T20:41:06.645Z] TOOL RESULT

```
=== etymonline parasang ===
URL: https://www.etymonline.com/word/parasang
FETCHED: 2026-09-05T20:35:36Z
STATUS: 200
TITLE: Etymonline - Online Etymology Dictionary
Etymonline - Online Etymology Dictionary 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.
 About
 Who Did This 
 Sources 
 Introduction 
 Links 
 Support
 Premium 
 Patreon 
 Donate with PayPal 
 Merch 
 Apps

=== ARY فرانسه/فرنگ ===
207:واژهی «صده معمولاً حاوی حرف «7ق) است.(مثلاً در فرانسه ۳3۸۲7 و یا انگلیسی ۰171-30822
264:می‌شوند و زبانهای پیرامون بیشتر محافظه کارند و دارای واژه‌های کهن تراند. مثلاً زبان فرانسه‌ی رایج
266:در ایالت کبک در کانادا (یک زبان پیرامون) از زبان فرانسه‌ی رایج د رکشور فرانسه کمتر تغیی رکرده
348:باختری فرانسه تکلم می‌شود در گذشته بخش عمده‌ی اسپانیا را زیر پوشش داشته است. شواهد فراوان
401:از این خانواده‌ها شامل چند زبان‌اند. مثلاً خانواده‌ی لاتین شامل ایتالیایی و فرانسه و اسپانیایی و
=== BQT_v3 فرانسه ===
```


## [2026-09-05T20:41:11.894Z] TOOL CALL #44: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg164.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/164.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Archive page image for audit"
}
```


### [2026-09-05T20:41:11.967Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T20:49:32.613Z] TOOL CALL #45: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build164.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 164,\n \"book_page\": 134,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Frankon\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Germanic (Frankish) *Frank-, *Frankō 'a Frank', tribal self-designation; traditionally connected with Germanic *frankōn- 'javelin, lance' (OE franca)\",\n   \"note\": \"The etymon itself is real and is exactly the headword of Nourai's own reference: Watkins's Indo-European appendix has '[Frankon-. Frank (member of a Germanic tribe), “javelin.” Germanic root. 1. Frankish *Frank-, Frank, borrowed into Late Latin as Francus, Frank: (FRANK1), FRANK. 2. Derivative adjective *frankiskaz, of the Franks, in Old English frencisc, French: FRENCH.]'. Two things in the root box are wrong, and Nourai half-admits the first himself in the box's footnote 'This is a Frankish word'. (1) The language label 'Old French' is wrong: *Frankon- is a Germanic/Frankish root, and AHD brackets it precisely because it is a Germanic, not an Indo-European, reconstruction; Old French franc is already the third stage (Frankish > Medieval Latin francus > OF franc). (2) The gloss 'free people' inverts the semantics. AHD glosses the root 'javelin'; Klein (s.v. frank, adj.) says 'In the territory formerly called Gaul the Franks were looked upon as the free nation par excellence (whence the sense development of F. franc)', and Etymonline states flatly that 'The adjectival sense of “free, at liberty” ... probably developed from the tribal name, not the other way round.' So the Franks were not 'the free people' who gave their name to a nation; the nation's name gave Romance its word for 'free'. 'Conquerors ... which conquered Gaul about 500 AD' is correct (Salian Franks, Clovis, c. 486–511). Everything hanging below the root — Old French franc/France, Arabic al-faranji, Persian farang, the English family — is sound; only the root box's language tag and the direction of its gloss need correcting.\",\n   \"note_fa\": \"خود این ریشه واقعی است و عیناً مدخلِ مرجعی است که نورایی خود آورده: واتکینز در پیوست فرهنگ American Heritage مادهٔ Frankon- را «ریشهٔ ژرمنی، به معنای زوبین» آورده است. دو لغزش در خانهٔ ریشه هست: ۱) برچسب زبانی «فرانسوی کهن» نادرست است؛ *Frank- واژه‌ای ژرمنی (فرانکی) است که نخست به لاتینی متأخر francus و سپس به فرانسوی کهن franc راه یافته است (خود نورایی هم در حاشیهٔ خانه می‌نویسد «واژه‌ای فرانکی است»). ۲) معنای «مردمان آزاد» جهت تحول معنایی را وارونه می‌کند: کلاین و اتیمولاین هر دو می‌گویند معنای «آزاد» پس از نام قوم پدید آمده، زیرا در گالِ فتح‌شده تنها فرانک‌ها مردمان آزاد شمرده می‌شدند، نه آنکه قوم را از پیش «آزادگان» خوانده باشند. در مجموع ریشه با احتیاط پذیرفتنی است و همهٔ شاخه‌های زیر آن درست است.\",\n   \"sources\": [\n    \"https://www.etymonline.com/word/frank\",\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Germanic/Frank\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"AHD:1515\", \"status\": \"partial\", \"note\": \"The IE-roots appendix Nourai cites (p.1515 of the New College Edition = the entry preserved verbatim in Watkins 1985, local AHD_watkins1985.txt leaf 47, line 474): '[Frankon-. Frank (member of a Germanic tribe), “javelin.” Germanic root. 1. Frankish *Frank-, Frank, borrowed into Late Latin as Francus, Frank: (FRANK1), FRANK. 2. Derivative adjective *frankiskaz, of the Franks, in Old English frencisc, French: FRENCH.]' — the headword and the tribal reference are Nourai's, but AHD calls it a GERMANIC root (bracketed, i.e. not Indo-European) and glosses it 'javelin', not 'free people'. The index page confirms 'FRANK1 Frankon- / FRANK Frankon- / FRENCH Frankon-' (leaf 122).\"},\n    {\"ref\": \"AHD:522\", \"status\": \"not_checked\", \"note\": \"p.522 is the main-dictionary page of the AHD New College Edition (s.v. frank / Frank); only the Indo-European appendix of that edition is on disk (AHD_watkins1985.txt), so the body-of-the-dictionary page could not be read.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt leaf 47 (appendix s.v. Frankon-)\", \"stance\": \"partial\", \"note\": \"'Frankon-. Frank (member of a Germanic tribe), “javelin.” Germanic root.' — same etymon, but Germanic and glossed 'javelin'.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 335 s.v. frank, adj.\", \"stance\": \"partial\", \"note\": \"'OF. (= F.) franc, “free”, fr. ML. Francus, “Frank”, fr. Frankish *Frank, “a Frank” (rel. to OHG. Franko, OE. Franca ...). In the territory formerly called Gaul the Franks were looked upon as the free nation par excellence (whence the sense development of F. franc).' — Klein makes 'free' the derived, later sense.\"},\n    {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/frank, s.v. Frank (n.)\", \"stance\": \"contradicts\", \"note\": \"'The origin of the ethnic name is uncertain; it traditionally is said to be from the old Germanic word *frankon “javelin, lance” ..., their preferred weapon, but the reverse may be the case. ... The adjectival sense of “free, at liberty” ... probably developed from the tribal name, not the other way round.'\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt s.v. Frankalmoign\", \"stance\": \"partial\", \"note\": \"'Lit. ... F. franc, free; Anglo-F. almoigne, alms. See Frank and ...' — Skeat too treats franc 'free' as the adjective belonging with the tribal name Frank.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Old French\",\n     \"words\": \"franc; France\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Frankish *Frank (self-designation of the Salian Franks on the lower Rhine from the 3rd c.) was taken into Late/Medieval Latin as Francus 'a Frank', and, because in post-Roman Gaul only the conquering Franks held the status of freemen, Francus acquired the adjectival sense 'free, exempt from service'. From that Medieval Latin adjective comes Old French franc (12th c.) 'free (not servile); without hindrance, exempt from; sincere, open, generous'. The country name is Late Latin Francia 'land of the Franks' (Latin -ia forming territorial names), which by regular Gallo-Romance loss of the intervocalic velar and of the final unstressed vowel gives Old French France. Nourai's gloss 'land of free people' is a gloss of the second stage: etymologically Francia is 'land of the Franks', and only secondarily of 'the free'.\",\n     \"derivation_fa\": \"واژهٔ فرانکی *Frank (نامی که فرانک‌های سالی در کرانهٔ پایینی راین از سدهٔ سوم میلادی بر خود نهاده بودند) به لاتینی متأخر Francus وام داده شد و چون در گالِ پس‌ازرومی تنها فرانک‌ها از منزلت آزادمردی برخوردار بودند، همین واژه معنای «آزاد، معاف از خدمت» گرفت و در فرانسوی کهن (سدهٔ ۱۲م) franc شد. نام کشور از Francia لاتینی «سرزمین فرانک‌ها» با پسوند جای‌نام‌ساز -ia است که با دگرگونی‌های آوایی معمول گالورومانی به France رسیده است؛ پس «سرزمین مردمان آزاد» معنای ثانوی است نه ریشه‌شناختی. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/frank\", \"https://www.etymonline.com/word/franchise\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:522\", \"status\": \"not_checked\", \"note\": \"p.522 of the AHD New College Edition (main dictionary, s.v. frank/Frank/France) is not on disk; only the Indo-European appendix of that edition (Watkins) is, and it confirms only 'Frankish *Frank-, Frank, borrowed into Late Latin as Francus'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 335 s.v. frank, adj.\", \"stance\": \"supports\", \"note\": \"'OF. (= F.) franc, “free”, fr. ML. Francus, “Frank”, fr. Frankish *Frank ..., whence also F. France, orig. “the land of the Franks”.' — both of Nourai's Old French words, from the same source.\"},\n      {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/frank s.v. frank (adj.)\", \"stance\": \"supports\", \"note\": \"'from Old French franc “free (not servile); without hindrance, exempt from; sincere, genuine, open ...” (12c.), from Medieval Latin francus “free, at liberty, exempt from service”, as a noun, “a freeman, a Frank”.'\"},\n      {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt leaf 47\", \"stance\": \"partial\", \"note\": \"'Frankish *Frank-, Frank, borrowed into Late Latin as Francus' — the appendix stops at Latin and does not name Old French franc.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"Farânseh «فرانسه»; (extra) فرانک ، فرانکلین\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Persian فرانسه farānse is a modern, Qajar-period name for the country, not an Old French loan: it goes back to Late Latin Francia through a modern intermediary. Wiktionary: 'Ultimately from Late Latin Francia (“land of the Franks”). Likely transmitted via intermediary languages; compare Arabic فَرَنْسَا (faransā) and Italian Francia'; the final ه ‑e of فرانسه renders exactly the -a/-e of Francia / Ottoman-Arabic فرانسه, not the mute -e of Modern French France. Dehkhoda records that under the Qajars the phrase was first زبان فرانسه 'the language of the country France' and only later فرانسه alone. The two 'extra' words are later still and do not come from Old French: فرانک ferānk/ferānk is the 20th-c. loan of Modern French franc, the coin, itself named from the medieval legend Francorum rex on the first gold coin (Klein s.v. franc), and فرانکلین Fārānklin is the English surname Franklin (ME frankelein 'small landowner'), reaching Persian through English/French, not from Old French France.\",\n     \"derivation_fa\": \"«فرانسه» وام‌واژه‌ای نو و متعلق به دورهٔ قاجار است، نه وام‌گیری از فرانسوی کهن. سرچشمهٔ نهایی آن Francia ی لاتینی متأخر «سرزمین فرانک‌ها» است که احتمالاً از راه زبان‌های میانجی (عربی فرنسا، ایتالیایی Francia، یا ترکی عثمانی) به فارسی رسیده است؛ هٔ پایانی دقیقاً همان -aی لاتینی/عربی را می‌نمایاند نه هٔ خاموش فرانسوی نو را. دو واژهٔ افزوده نیز از فرانسوی کهن نیامده‌اند: «فرانک» نام سکهٔ فرانسه (از کتیبهٔ لاتینی Francorum rex بر نخستین سکهٔ زرین) و «فرانکلین» نام‌خانوادگی انگلیسی (از انگلیسی میانه frankelein «خرده‌مالک») است. پس ادعای نورایی دربارهٔ خاستگاه نهایی درست ، ولی دربارهٔ راهِ وام‌گیری با احتیاط پذیرفتنی است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%87\", \"https://abadis.ir/fatofa/%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%87/\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:2528\", \"status\": \"not_checked\", \"note\": \"Mo'in's Farhang-e Farsi vols 5-6 (the a'lām volumes, where فرانسه as a country name belongs) are not on disk, and the online Mo'in at vajehyab/abadis carries no page numbers, so p.2528 could not be opened. The Mo'in text that is online for فرنگ does gloss it 'کشور فرانسه که مسکن قوم فرانک (قبیله‌ای از نژاد ژرمن) است', i.e. the same Frankish connection.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org s.v. فرانسه (Persian)\", \"stance\": \"partial\", \"note\": \"'Ultimately from Late Latin Francia (“land of the Franks”). Likely transmitted via intermediary languages; compare Arabic فَرَنْسَا (faransā) and Italian Francia' — same ultimate origin, but no Old French step.\"},\n      {\"src\": \"MON\", \"where\": \"abadis.ir/fatofa/فرانسه (Dehkhoda + Mo'in)\", \"stance\": \"partial\", \"note\": \"'در عهد قاجاریه نخست [زبان فرانسه] (یعنی زبان کشور فرانسه) مصطلح بود ... و بعد [زبان] را حذف کردند' — a Qajar-era word, and the Persian lexica treat it as the name of the modern country, not an Old French inheritance.\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 335 s.v. franc\", \"stance\": \"supports\", \"note\": \"For the 'extra' فرانک: 'franc, n., name of two old French coins ... F., from the ML. legend on the first coin: Francorum rex (“king of the Franks”)'; and s.v. franklin, 'ME. frankelein ..., formed fr. frank, “free”, and -lein' — both are English/French words of the modern period, not Old French France.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Arabic\",\n     \"words\": \"faranji, al-faranji\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic إفرنجي ifranjī / فرنجي faranjī 'Frankish, European', collective الإفرنج al-ifranj 'the Franks, the Europeans', is a Romance loan of the Crusading and pre-Crusading centuries: Medieval Latin / Old French Franc, franc was taken over with the Arabic nisba suffix -ī. Because Arabic phonotactics do not admit an initial fr- cluster, the word had to be repaired — either by a prosthetic hamza plus i (إفرنج) or by an anaptyctic vowel (فَرَنج) — which is why the Arabic reflex has the extra vowel the Romance form lacks; the g of Frank is rendered by ج (jīm), the ordinary Arabic substitute for a foreign g. The word is well attested by c. 980, when al-Mas'ūdī writes of 'the Afranjah' (Hobson-Jobson p.352, quoting Murūj iii.66). Nourai's two forms are exactly the two Hobson-Jobson prints on the cited page.\",\n     \"derivation_fa\": \"عربی «إفرنجی / فرنجی» و جمع «الإفرنج» وام‌واژه‌ای رومانسی است، از لاتینی میانه/فرانسوی کهن Franc با پسوند نسبت عربی ي‌. چون در عربی خوشهٔ آغازین fr- ممکن نیست، یا همزهٔ وصل و یِ آغازین افزوده شده (إفرنج) یا واکهٔ میانجی (فَرَنج)؛ g بیگانه نیز طبق معمول به جیم بدل شده است. این واژه دست‌کم از حدود ۹۸۰ میلادی در مروج‌الذهب مسعودی به صورت «الأفرنجة» آمده است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/frank\", \"https://en.wiktionary.org/wiki/%D8%A5%D9%81%D8%B1%D9%86%D8%AC%D9%8A\"],\n     \"ref_check\": [\n      {\"ref\": \"HJB:352\", \"status\": \"supports\", \"note\": \"Hobson-Jobson p.352 (local HJB.txt leaf 405, printed pp.352-353): 'FIRINGHEE, s. Pers. Farangī, Firingī; Ar. Al-Faranjī, Ifranjī, Firanjī, i.e. a Frank. This term for a European is very old in Asia ...', with the c.980 citation 'The Afranjah are of all those nations the most warlike' (Mas'udi iii.66). Nourai's 'faranji, al-faranji' are verbatim from this page.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/frank s.v. Feringhee (n.)\", \"stance\": \"supports\", \"note\": \"'from Persian Farangi, from Arabic Faranji (10c.), from Old French Franc “Frank” + Arabic ethnic suffix -i. The fr- sound is impossible in Arabic.' — exactly Nourai's Old French > Arabic > Persian chain.\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org s.v. إفرنجي (Arabic)\", \"stance\": \"supports\", \"note\": \"Etymology tree 'Proto-Germanic *frankō > Frankish *Frankō > Latin francus > Old French franc > Arabic إفرنجي'; 'Borrowed from Old French franc.'\"},\n      {\"src\": \"AFM\", \"where\": \"AFM.txt, grep 'فرنج'\", \"stance\": \"silent\", \"note\": \"Addi Shir's list of Persian words Arabicized has no إفرنج entry (the only hits are citations of 'فرنكل' = Fraenkel) — consistent, since this is a European, not a Persian, loan into Arabic.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Persian\",\n     \"words\": \"farangî «فرنگ»; (extra) فرنگستان ، افرنجی\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian فرنگ farang 'Europe, the Frankish lands' and its nisba فرنگی farangī 'European' come from the Arabic collective إفرنج ifranj / افرنجه ifranja by dropping the prosthetic اِ- and substituting the Persian velar گ for the Arabic ج that had itself stood for a foreign g — an Arabic-mediated round trip in which the g of Frank is restored in Persian. That is precisely what Mo'in says in his footnote to Borhān-e Qāte' on the very page Nourai cites. فرنگستان farangestān is the ordinary Persian place-name formation with the suffix -estān, and افرنجی afranjī is the unassimilated Arabic form kept alongside it (Borhān cross-refers فرنگ to فرنجه). The Bahār couplet the chart quotes ('زی فرنگستان سه کرت شاه ایران راند خنگ') illustrates the 19th-c. sense 'Europe'. One small inconsistency inside the box: the transliteration reads 'farangî' while the Persian script gives فرنگ farang; the printed page (p.134) confirms the mismatch is Nourai's, not the extraction's.\",\n     \"derivation_fa\": \"«فرنگ» و صفت نسبی «فرنگی» از عربی «إفرنج / افرنجه» گرفته شده است؛ فارسی همزهٔ آغازین را انداخته و جیم عربی را دوباره به گ برگردانده است — نمونه‌ای از معرّب‌شدن و بازگشت. معین در حاشیهٔ برهان قاطع (ذیل «فرنجه»، ص ۱۴۷۱) می‌نویسد: «مخفف افرنجه … معرّب … لاتینی Francus، فرانسوی Franc (قوم ژرمنی که در قدیم در جوار رود راین سکونت داشتند)». «فرنگستان» با پسوند جای‌نام‌ساز ‌ستان ساخته شده و «افرنجی» صورت عربی دست‌نخورده است. ادعای نورایی درست است؛ تنها آوانویسی «farangî» با متن فارسی «فرنگ» ناهماهنگ است.\",\n     \"sources\": [\"https://vajehyab.com/moein/%D9%81%D8%B1%D9%86%DA%AF\", \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D9%86%DA%AF\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1471\", \"status\": \"supports\", \"note\": \"Borhān-e Qāte' ed. Mo'in p.1471 (fetched with tools/ref_page.py BQT:1471 = BQT_v3_picofile.pdf p.264), footnote 7 to فرنجه: 'مخفف «افرنجه» (ه.م.) [افرنگ > فرنگ] معرب ... لاتینی Francus فرانسوی Franc (قوم ژرمنی که در قدیم در جوار رود Rhine سکونت داشتند) و بمملکت فرانسه نیز اطلاق شود'. The headword فرنگ itself stands on the next page (p.1472) and refers back with 'رک: فرنجه', its own footnote 4 adding 'فرنگ بقوم فرانک (و توسعاً اروپاییان) ... اطلاق شود'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"vajehyab.com/moein/فرنگ\", \"stance\": \"supports\", \"note\": \"'(فَ رَ) [فر.] (اِ.) ۱- نام عمومی هر یک از کشورهای اروپا و گاهی آمریکا. ۲- کشور فرانسه که مسکن قوم فرانک (قبیله‌ای از نژاد ژرمن) است.' Mo'in's origin tag is [فر.] = French rather than Arabic, but the referent is the same Frankish tribe.\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org s.v. فرنگ (Persian)\", \"stance\": \"partial\", \"note\": \"'Borrowed from Old French franc', tree 'Proto-Germanic *frankō > Frankish *Frankō > Latin francus > Old French franc > Persian فرنگ' — same origin, but Wiktionary omits the Arabic intermediary that Borhān, Hobson-Jobson and Etymonline all record.\"},\n      {\"src\": \"HJB\", \"where\": \"HJB.txt leaf 405, printed p.352 s.v. FIRINGHEE\", \"stance\": \"supports\", \"note\": \"'Pers. Farangī, Firingī; Ar. Al-Faranjī, Ifranjī ... i.e. a Frank' — the Persian word is listed as the reflex of the Arabic one.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"Frank, Franc, France, Franklin, franchise\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All five are the English end of the same chain. Frank 'member of the Germanic people' is Old English franc, franca 'freeman, noble; Frank', reinforced by Medieval Latin Francus. franc, the coin, is French franc, named from the Medieval Latin legend Francorum rex 'king of the Franks' struck on the first gold piece (1360). France is Old French France < Late Latin Francia. franchise is Middle English fraunchise (c.1300) 'a special right or privilege', from Old French franchise 'freedom, exemption', from the stem of franc 'free'. Franklin is Middle English frankelein 'a small landowner' (cf. Medieval Latin franchilanus), frank 'free' + the Germanic suffix -lein, i.e. a freeholder below the rank of gentry. Only the routes differ in date, not in origin, and all four post-Frankish words come through Old French exactly as the chart draws them.\",\n     \"derivation_fa\": \"هر پنج واژه پایانهٔ انگلیسی همین زنجیره‌اند: Frank از انگلیسی کهن franc/franca «آزادمرد، فرانک»؛ franc نام سکه از کتیبهٔ Francorum rex بر نخستین سکهٔ زرین (۱۳۶۰ م)؛ France از فرانسوی کهن و لاتینی Francia؛ franchise از انگلیسی میانه fraunchise و فرانسوی کهن franchise «آزادی، معافیت»؛ Franklin از انگلیسی میانه frankelein «خرده‌مالک آزاد». ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/frank\", \"https://www.etymonline.com/word/franchise\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:614\", \"status\": \"supports\", \"note\": \"Klein has all five together on one page (local KLN_1966.txt leaf 335, the F-section leaf that carries franc through frankpledge): 'franc, n., name of two old French coins ... F., from the ML. legend on the first coin: Francorum rex (“king of the Franks”)'; 'Frank, n., member of a West Teutonic people. — OHG. Franko, rel. to OE. Franca. See frank, adj.'; 'franklin, n., a small landowner. — ME. frankelein (cp. ML. franchilanus), formed fr. frank, “free”, and -lein'; 'frank, adj. — OF. (= F.) franc ... whence also F. France ... Cp. franc, franchise, Franco-, Frank, French.' (The local scan carries no printed folios, so Nourai's exact page 614 could not be matched leaf-for-leaf; the entries are certainly Klein's.)\"},\n      {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Cited without a page. Watkins's appendix (AHD_watkins1985.txt leaf 47) covers only FRANK1, FRANK and FRENCH under Frankon-; franc, France, Franklin and franchise are not in the appendix, and the index leaf 122 lists 'FRANK1 Frankon- / FRANK Frankon-' only.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/frank and /word/franchise\", \"stance\": \"supports\", \"note\": \"'Frank (n.) one of the Germanic tribal people (Salian Franks) situated on the lower Rhine from 3c. ... Old English franc, franca “freeman, noble; Frank, Frenchman”, from Medieval Latin francus'; 'franchise (n.) c.1300, fraunchise ... from Old French franchise “freedom, exemption; right, privilege” (12c.), from variant stem of franc “free”.'\"},\n      {\"src\": \"SKT\", \"where\": \"SKT.txt s.v. Frankalmoign\", \"stance\": \"partial\", \"note\": \"'Lit. F. franc, free; Anglo-F. almoigne, alms. See Frank and ...' — Skeat treats the whole English frank-family as one, from Old French franc.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 1,\n   \"root\": \"Fra-sanga\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Old Iranian / Old Persian *frasanga- (unattested; also reconstructed *frasanhvah / NW Iranian *frasaxa-), 'parasang', a road measure of c. 5.5-6.2 km\",\n   \"note\": \"The etymon is right and is the standard reconstruction, but it is a reconstruction, not an attested Old Persian word, and Nourai's box does not say so. Nyberg (Manual of Pahlavi II, glossary s.v. frasang) states it plainly: 'OP *frasanga- borrowed in Gr as παρασάγγης, Paz. NP farsang; NW form *frasaxa-, Arm. lw. hrasax, Syr. lw. prshʾ, Talm prse, Mand prsʾ, Arab farsax.' Asbaghi (Persische Lehnwörter im Arabischen s.v. farsah) has the same: 'pers. farsang > mp. frasang, ap. *frasanga “a parasang”'. Mo'in's footnote in Borhān-e Qāte' — the very page Nourai cites for the Pahlavi node — reads 'پهلوی فرسنگ (مقیاس طول)، پارسی باستان ظاهراً فرسنگا و صورت یونانی‌شده آن پراساغس و معرّب آن فرسخ است' — note the 'ظاهراً' ('apparently'), the same hedge. Kent's Old Persian lexicon has no such entry, as expected for an unattested form; Wiktionary's parasang article reconstructs *frasanhvah instead and says the word is 'indigenously attested only in Middle Iranian onwards'. The gloss is a little short: the classical parasang is usually put at 5.6-6.2 km (Nyberg: 'an average of 6232 m., but varying'; Borhān: three miles = 12,000 gaz), so 'about five kilometers' is at the low end but not wrong. The chart's three Western nodes all print the form without the second a (parsanges, parsanga, parsang); that is Nourai's own misprint on p.134, not an extraction error — see the nodes.\",\n   \"note_fa\": \"ریشه درست است ولی باید توجه داشت که صورت پارسی باستان در سنگ‌نوشته‌ها گواهی نشده و بازسازی است: نیبرگ در واژه‌نامهٔ پهلوی خود می‌نویسد «OP *frasanga- borrowed in Gr as παρασάγγης ... NW form *frasaxa-» و معین در حاشیهٔ برهان قاطع (ص ۱۴۶۲) می‌گوید «پارسی باستان ظاهراً فرسنگا» — همین «ظاهراً» گویای بازسازی بودن آن است. کنت در واژه‌نامهٔ پارسی باستان چنین مدخلی ندارد. اندازهٔ «حدود پنج کیلومتر» نیز کمی کمتر از برآورد معمول (۵/۶ تا ۶/۲ کیلومتر) است. سه خانهٔ یونانی و لاتینی و انگلیسی نمودار هر سه بدون الف دوم چاپ شده‌اند که خطای چاپی خود کتاب است نه خطای خوانش اسکن.\",\n   \"sources\": [\"https://en.wiktionary.org/wiki/parasang\", \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B3%D9%86%DA%AF\"],\n   \"ref_check\": [\n    {\"ref\": \"HRN:182\", \"status\": \"partial\", \"note\": \"Horn, Grundriss der neupersischen Etymologie p.182 (local HRN.txt leaf 203, entry no. 818): 'ferseng ‚Parasange‘, arab. LW. farsax; [a]p. παρασάγγης; phl. frasang bezw. farsang (Men., Bund.).' Horn gives the Greek and the two Pahlavi readings and calls Arabic farsax a loanword, but he prints no Old Persian *fra-sanga-; the reconstruction Nourai puts in the root box is not on the page he cites for it.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt leaf 88 s.v. frasang\", \"stance\": \"supports\", \"note\": \"'frasang [plsng] a parasang, the Persian league, estimated at an average of 6232 m., but varying in length (3½-4 English miles) ... — OP *frasanga- borrowed in Gr as παρασάγγης, Paz. NP farsang; NW form *frasaxa-, Arm. lw. hrasax, Syr. lw. prshʾ, Talm prse, Mand prsʾ, Arab farsax.'\"},\n    {\"src\": \"KNT\", \"where\": \"KNT.txt, grep 'frasang|parasang|Fra-sanga'\", \"stance\": \"silent\", \"note\": \"Kent's Old Persian lexicon has no entry — confirming that the form is not attested in the Achaemenid inscriptions and exists only as a reconstruction.\"},\n    {\"src\": \"PLA\", \"where\": \"PLA_asbaghi_1988_ia_djvu.txt s.v. farsah\", \"stance\": \"supports\", \"note\": \"'farsah: ‚Parasange, ein persisches Maß, ungefähr 6232 mt‘ pers. farsang > mp. frasang ap. *frasanga ‚a parasang‘.'\"},\n    {\"src\": \"HUB\", \"where\": \"HUB.txt (Persische Studien, chapter on s)\", \"stance\": \"supports\", \"note\": \"'farsang = phl. frasang παρασάγγης' — Hübschmann sets the New Persian, Pahlavi and Greek forms in the same equation.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"farsang\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian, written plsng in Book Pahlavi, is normalised frasang by MacKenzie ('frasang [plsng | N farsang] parasang (4 Roman miles)') and by Nyberg; the Pahlavi spelling has no vowel signs, so both readings frasang and farsang are defensible and Horn's entry 818 explicitly allows both ('phl. frasang bezw. farsang (Men., Bund.)', i.e. as read in the Mēnōg ī Xrad and the Bundahišn). The step from the Old Iranian ancestor is simply the loss of the final vowel of *frasanga- and the fixing of the word as a road-measure of about 4 Roman miles; the metathesis-like fra- > far- that gives New Persian farsang belongs to the next stage, so writing the Pahlavi box 'farsang' anticipates it slightly. The word is common in the Pahlavi books (Nyberg cites Kārnāmag and Bundahišn passages, e.g. horses that cover 70 frasang in a day).\",\n     \"derivation_fa\": \"فارسی میانه در خط پهلوی plsng نوشته می‌شود و مکنزی آن را frasang «فرسنگ (چهار میل رومی)» خوانده است. چون خط پهلوی واکه را نمی‌نویسد، هر دو خوانش frasang و farsang روا است و هرن (شمارهٔ ۸۱۸) صریحاً می‌گوید «phl. frasang bezw. farsang». دگرگونی fra- به far- درستی به مرحلهٔ فارسی نو تعلق دارد، پس نوشتن «farsang» در خانهٔ پهلوی اندکی زودهنگام است. در متون پهلوی (مینوی خرد، بندهش) فراوان به کار رفته است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B3%D9%86%DA%AF\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1462\", \"status\": \"supports\", \"note\": \"Borhān-e Qāte' ed. Mo'in p.1462 (tools/ref_page.py BQT:1462 = BQT_v3_picofile.pdf p.255), footnote 5 to فرسنگ, read in the clean Persian transcript Dehkhoda gives of the same footnote: 'پهلوی فرسنگ (مقیاس طول)، پارسی باستان ظاهراً فرسنگا و صورت یونانی‌شده آن پراساغس و معرب آن فرسخ است. (از حاشیه برهان چ معین)'; the page image itself shows the Latin-script forms and the references 'نیبرگ ۷۳' and 'هوبشمان ۸۱۸'. Exactly Nourai's Pahlavi node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"PHD.txt s.v. frasang (MacKenzie p.33)\", \"stance\": \"supports\", \"note\": \"'frasang [plsng | N farsang] parasang (4 Roman miles)'; also s.v. hasēr, 'a measure of length (= frasang, or ½ frasang, 1 mile)'.\"},\n      {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt leaf 88 s.v. frasang\", \"stance\": \"supports\", \"note\": \"'frasang [plsng] a parasang, the Persian league, estimated at an average of 6232 m. ... 71⁹, 89.6, 72²⁵, 93⁷⁻¹¹ ...' with references to the Pahlavi texts.\"},\n      {\"src\": \"HRN\", \"where\": \"HRN.txt leaf 203, no. 818 (printed p.182)\", \"stance\": \"supports\", \"note\": \"'phl. frasang bezw. farsang (Men., Bund.)' — Horn admits precisely the reading Nourai prints.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"farsang «فرسنگ»; farsax «فرسخ»; (extra) پرسنگ\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"فرسنگ farsang continues Middle Persian frasang directly, with the ordinary New Persian resolution of the initial fra- cluster into far- (compare frāmōš- > فراموش, framan > فرمان); Borhān defines it as three miles = 12,000 gaz, and the modern Iranian farsang is fixed at 6 km. The variant پرسنگ parsang, which Nourai puts in the box as an 'extra', is the older p-initial shape also reflected in Greek παρα-. فرسخ farsax is where the chart needs qualifying. Mo'in's footnote does say 'معرب آن فرسخ است', which is Nourai's 'Arabic pronunciation of farsang', and Horn no.818 calls farsax an Arabic loanword; but Nyberg, followed by most Iranists, derives Arabic فَرْسَخ farsaḫ not from Persian farsang at all but from a Northwest Iranian (Parthian) *frasaxa-, the same form that gave Armenian hrasax, Syriac prsḥʾ, Talmudic parsā and Mandaic prsʾ. On that view farsax is a sister of farsang through Parthian and Aramaic, not a distorted pronunciation of it, and Persian فرسخ is then a re-borrowing back from Arabic. Nourai's own chart lets فرسخ hang under Persian farsang, which is the traditional but not the best-supported account.\",\n     \"derivation_fa\": \"«فرسنگ» دنبالهٔ مستقیم frasang فارسی میانه است با دگرگونی معمول fra- به far- (قیاس کنید: frāmōš > فراموش، framān > فرمان). برهان قاطع آن را سه میل یعنی دوازده هزار گز دانسته و امروز شش کیلومتر است. صورت «پرسنگ» همان شکل کهنه‌تر با پ است که در para-ی یونانی هم بازتابیده است. دربارهٔ «فرسخ» باید احتیاط کرد: معین و هرن آن را معرّب فرسنگ می‌دانند (همان چیزی که نورایی می‌گوید)، اما نیبرگ و بیشتر ایران‌شناسان عربی فَرْسَخ را از صورت ایرانی شمال غربی (پارتی) *frasaxa- می‌گیرند — همان که ارمنی hrasax و سریانی parsḥā و آرامی parsā از آن آمده — پس «فرسخ» هم‌ریشهٔ فرسنگ است نه تلفظ عربی آن، و در فارسی نو از عربی وام گرفته شده است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B3%D9%86%DA%AF\", \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B3%D8%AE\", \"https://abadis.ir/fatofa/%D9%81%D8%B1%D8%B3%D9%86%DA%AF/\"],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1462\", \"status\": \"supports\", \"note\": \"Borhān p.1462 s.v. فرسنگ: 'قدری باشد معین از راه و آن بمقدار سه میل است و هر میلی چهارهزار گز که مجموع فرسنگ دوازده هزار گز باشد', with Mo'in's footnote '... و معرب آن فرسخ است' — both of Nourai's Persian words and the 'Arabic pronunciation' claim for فرسخ.\"},\n      {\"ref\": \"MON:743,2517\", \"status\": \"not_checked\", \"note\": \"Mo'in's Farhang-e Farsi is on disk only as the two-volume Adena abridgement with different pagination, and the online Mo'in (vajehyab/abadis) carries no folios, so pp.743 and 2517 could not be opened. The online Mo'in/Dehkhoda article for فرسنگ reproduces the Borhān footnote verbatim and gives 'مترادف فرسنگ: فرسخ', consistent with the node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"HRN.txt leaf 203, no. 818 (printed p.182)\", \"stance\": \"supports\", \"note\": \"'ferseng ‚Parasange‘, arab. LW. farsax' — Horn labels farsax an Arabic loanword of the Persian word, i.e. Nourai's reading.\"},\n      {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt leaf 88 s.v. frasang\", \"stance\": \"partial\", \"note\": \"'NW form *frasaxa-, Arm. lw. hrasax, Syr. lw. prshʾ, Talm prse, Mand prsʾ, Arab farsax' — Arabic farsax is traced to a Northwest Iranian by-form, not to New Persian farsang.\"},\n      {\"src\": \"PLA\", \"where\": \"PLA_asbaghi_1988_ia_djvu.txt s.v. farsah / farasīh\", \"stance\": \"supports\", \"note\": \"'farsah: ‚Parasange, ein persisches Maß, ungefähr 6232 mt‘ pers. farsang > mp. frasang ap. *frasanga'; Asbaghi lists it among the Persian loans in Arabic, with 'Es ist eine Nebenform v. farsah pers. farsang'.\"},\n      {\"src\": \"MON\", \"where\": \"abadis.ir/fatofa/فرسنگ (Dehkhoda quoting حاشیه برهان چ معین)\", \"stance\": \"supports\", \"note\": \"'فرسنگ. [فَ سَ] (اِ) پهلوی فرسنگ (مقیاس طول)، پارسی باستان ظاهراً فرسنگا و صورت یونانی‌شده آن پراساغس و معرب آن فرسخ است ... مقدار طولی که امروز یک فرسنگ یا فرسخ به شمار میرود شش کیلومتر است.'\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Greek\",\n     \"words\": \"parsanges\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"parsanges\",\n     \"correct_form\": \"parasangēs (παρασάγγης)\",\n     \"derivation\": \"The Greek word is παρασάγγης parasangēs, used by Herodotus (2.6, 5.53, 6.42) and made famous by Xenophon's Anabasis, where the march is counted in parasangs; it is a fifth-century BCE administrative borrowing of the Iranian road-measure along with the Persian royal road itself, the Iranian cluster fra- being resolved by Greek into para- and the Iranian -a stem receiving the Greek masculine ending -ης. The chart's form 'parsanges' lacks that second a. I rendered PDF page 164 at 200 dpi (copy kept at data/verification/sources/refs/ocr/BOOK/164.png): the printed box on book page 134 reads 'parsanges', so the extraction is faithful and the missing a is Nourai's own misprint. Klein, the reference Nourai cites for this very node, spells it παρασάγγης, as do Nyberg, Hübschmann and Mo'in.\",\n     \"derivation_fa\": \"صورت یونانی این واژه παρασάγγης (parasangēs) است که هرودوت در سدهٔ پنجم پیش از میلاد و سپس گزنوفون در «آنابازیس» به کار برده‌اند؛ یونانی خوشهٔ fra-ی ایرانی را به para- گشوده و پایانهٔ مذکر -ης افزوده است. صورت «parsanges» که در نمودار آمده الف دوم را ندارد. تصویر صفحهٔ ۱۳۴ کتاب را دیدم: در خود کتاب هم «parsanges» چاپ شده؛ پس خطای خوانش اسکن نیست و خطای چاپی خود نورایی است؛ کلاین که مرجع همین خانه است، مانند نیبرگ و هوبشمان و معین، παρασάγγης می‌نویسد.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/parasang\", \"https://en.wiktionary.org/wiki/%CF%80%CE%B1%CF%81%CE%B1%CF%83%CE%AC%CE%B3%CE%B3%CE%B7%CF%82\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1127\", \"status\": \"supports\", \"note\": \"Klein s.v. parasang (local KLN_1966.txt leaf 602): 'parasang, n., a Persian measure of length, equal to about 3 2/5 miles. — L. parasanga, fr. Gk. παρασάγγης, “parasang”, which is of Iranian origin. Cp. Pehlevi frasang, farsang, ModPers. ferseng.' The arrow Iranian > Greek is exactly Klein's; only the spelling in Nourai's box differs from Klein's παρασάγγης. (The local scan has no printed folios, so p.1127 could not be matched leaf-for-leaf.)\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt leaf 88 s.v. frasang\", \"stance\": \"supports\", \"note\": \"'OP *frasanga- borrowed in Gr as παρασάγγης' — the borrowing itself confirmed, the form spelled with the second a.\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org s.v. parasang\", \"stance\": \"supports\", \"note\": \"'From Latin parasanga, from Ancient Greek παρασάγγης (parasangēs), from unattested Old Persian *frasanhvah (indigenously attested only in Middle Iranian onwards).'\"},\n      {\"src\": \"HUB\", \"where\": \"HUB.txt (Persische Studien)\", \"stance\": \"supports\", \"note\": \"'farsang = phl. frasang παρασάγγης'.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Latin\",\n     \"words\": \"parsanga\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"parsanga\",\n     \"correct_form\": \"parasanga\",\n     \"derivation\": \"Latin took the measure from Greek as parasanga (Pliny, Naturalis Historia 6.30, and the Latin translations of Xenophon), the Greek nominative in -ης being replaced by the Latin first-declension -a. That is the form Klein prints ('L. parasanga, fr. Gk. παρασάγγης') and the form Wiktionary lemmatises. The chart's 'parsanga' again drops the second a; the 200-dpi rendering of PDF page 164 shows the printed box really does read 'parsanga', so this is Nourai's misprint carried consistently through his Greek, Latin and English boxes, not an extraction error. The Greek > Latin arrow itself is correct and uncontroversial.\",\n     \"derivation_fa\": \"لاتینی این مقیاس را از یونانی به صورت parasanga وام گرفت (پلینی، تاریخ طبیعی ۶،۳۰)؛ پایانهٔ یونانی -ης جای خود را به -aی صرف نخست لاتینی داد. کلاین هم می‌نویسد «L. parasanga, fr. Gk. παρασάγγης». صورت «parsanga» در نمودار خطای چاپی خود کتاب است (تصویر صفحهٔ ۱۳۴ دیده شد)، نه خطای استخراج داده. خود پیکان یونانی ← لاتینی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/parasang\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:952\", \"status\": \"not_checked\", \"note\": \"p.952 of the AHD New College Edition is a main-dictionary page (s.v. parasang); only the Indo-European appendix of that edition is on disk, and parasang is not an Indo-European-root entry, so the cited page could not be read.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 602 s.v. parasang\", \"stance\": \"supports\", \"note\": \"'— L. parasanga, fr. Gk. παρασάγγης, “parasang”, which is of Iranian origin.'\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org s.v. parasang\", \"stance\": \"supports\", \"note\": \"'From Latin parasanga, from Ancient Greek παρασάγγης' — the Latin lemma is parasanga.\"},\n      {\"src\": \"FSD\", \"where\": \"FSD_vol4.txt s.v. schene\", \"stance\": \"partial\", \"note\": \"'An ancient Egyptian measure of length, of about 4 English miles, or nearly equal to the Persian parasang' — Funk & Wagnalls knows the word only in the spelling parasang.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"parsang\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"parsang\",\n     \"correct_form\": \"parasang\",\n     \"derivation\": \"The English word is parasang, in use from the 16th century in translations of Xenophon and Herodotus and taken straight from Latin parasanga; the dictionaries define it as Nourai does, 'a Persian measure of length, equal to about 3 2/5 miles' (Klein) — the chart's '3.5 miles' is the same figure rounded. The chain Iranian > Greek > Latin > English is correct; only the headword form in the box is wrong, and the 200-dpi rendering of PDF page 164 shows that the printed book itself reads 'parsang', so this is the author's misprint and not an extraction fault. No English dictionary knows a form 'parsang'.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی parasang است که از سدهٔ شانزدهم در ترجمهٔ گزنوفون و هرودوت به کار رفته و یکسره از لاتینی parasanga گرفته شده است؛ کلاین آن را «مقیاس طول ایرانی، حدود ۳ و ۲/۵ میل» می‌داند که با «۳/۵ میل» نمودار یکی است. زنجیرهٔ ایرانی ← یونانی ← لاتینی ← انگلیسی درست است، ولی صورت «parsang» در هیچ فرهنگ انگلیسی نیست؛ این هم خطای چاپی کتاب است (از روی تصویر صفحهٔ ۱۳۴ ارزیابی شد)، نه خطای استخراج.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/parasang\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:952\", \"status\": \"not_checked\", \"note\": \"The New College Edition's main dictionary (where the English headword parasang stands on p.952) is not on disk; the Watkins appendix that is on disk has no parasang entry, the word being an Iranian loan and not an Indo-European-root derivative.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 602 s.v. parasang\", \"stance\": \"supports\", \"note\": \"'parasang, n., a Persian measure of length, equal to about 3 2/5 miles. — L. parasanga, fr. Gk. παρασάγγης ... Cp. Pehlevi frasang, farsang, ModPers. ferseng.' Klein's headword is parasang, and his definition is Nourai's.\"},\n      {\"src\": \"FSD\", \"where\": \"FSD_vol3.txt / FSD_vol4.txt, grep 'parasang'\", \"stance\": \"partial\", \"note\": \"Funk & Wagnalls uses 'the Persian parasang' as a gloss (s.v. schene) and lists 'parasang' in its Persian geographical vocabulary; no entry spelled 'parsang'.\"},\n      {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt, grep -i 'parasang'\", \"stance\": \"silent\", \"note\": \"The available Webster volume (A-...) does not reach P, so it neither confirms nor denies.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-164.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write('\\n')\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build164.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-164.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 164",
 "description": "Write and validate page-164.json"
}
```


### [2026-09-05T20:49:35.078Z] TOOL RESULT

```
written
JSON OK
nodes verified: 10/10
node verdicts: {'confirmed': 5, 'plausible': 2, 'transcription_suspect': 3}
root verdicts: {'plausible': 2}
ref checks: {'not_checked': 5, 'supports': 6, 'partial': 1}
books consulted: {'supports': 20, 'partial': 8, 'silent': 2} | by book: {'WIKT': 5, 'KLN': 4, 'ETYMONLINE': 3, 'MON': 3, 'NYB': 3, 'HRN': 2, 'FSD': 2, 'AHD': 1, 'AFM': 1, 'HJB': 1, 'SKT': 1, 'PHD': 1, 'PLA': 1, 'HUB': 1, 'WEB': 1}
```


## [2026-09-05T20:49:52.634Z] AGENT

Page 164 (book p. 134) verified: `/home/sfmqrb/git/rishe/data/verification/page-164.json`. `verify_check.py 164` → 10/10 nodes, **0 PROBLEM lines**.

Counts: node verdicts 5 confirmed / 2 plausible / 3 transcription_suspect; both roots plausible. Ref checks: 6 supports, 1 partial, 5 not_checked. 30 `consulted` entries across 15 books.

- **transcription_suspect — Fra-sanga #3 Greek "parsanges"**: should be παρασάγγης *parasangēs*. `error_in: book` — the 200-dpi render of p.134 shows the book itself prints "parsanges".
- **transcription_suspect — Fra-sanga #4 Latin "parsanga"**: should be *parasanga* (Klein, Wiktionary). `error_in: book`.
- **transcription_suspect — Fra-sanga #5 English "parsang"**: the English word is *parasang*; no dictionary has "parsang". `error_in: book`. All three are one consistent authorial misprint; page image archived at `data/verification/sources/refs/ocr/BOOK/164.png`.
- **Root Frankon (plausible)**: two corrections. The language label "Old French" is wrong — Nourai's own reference (AHD appendix, local `AHD_watkins1985.txt` leaf 47) has "[Frankon-. Frank …, 'javelin.' **Germanic root**]"; and the gloss inverts the semantics — Klein and Etymonline both make "free" a sense that developed *from* the tribal name, not the source of it.
- **Root Fra-sanga (plausible)**: correct as a reconstruction, but unattested in Old Persian (Kent has no entry); Nyberg and Asbaghi give OP *\*frasanga-*, Mo'in hedges "پارسی باستان **ظاهراً** فرسنگا", Wiktionary prefers *\*frasanhvah*. HRN:182 (Horn no. 818) is only `partial` — it gives Greek and Pahlavi but no Old Persian form.
- **#2 farsax (plausible)**: Nourai's "Arabic pronunciation of farsang" follows Mo'in/Horn, but Nyberg derives Arabic فرسخ from NW Iranian *\*frasaxa-* (whence Arm. hrasax, Syr. prsḥʾ), i.e. a sister form, not a distorted pronunciation.
- **#2 Farânseh (plausible)**: a Qajar-era loan of Late Latin/Romance *Francia* via an intermediary, not from Old French; the extras فرانک and فرانکلین come via modern French/English.

No extraction errors found — the JSON matches the printed page exactly, including the three misprinted parasang forms. Strong finds: BQT:1471 and BQT:1462 both `supports` verbatim (fetched via `ref_page.py`), and HJB:352 prints Nourai's "faranji, al-faranji" word for word.
