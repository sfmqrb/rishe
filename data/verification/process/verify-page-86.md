# Verification process log — verify-page-86


## [2026-09-05T06:32:42.003Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 86 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-86.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-86.json. Write /home/sfmqrb/git/rishe/data/verification/page-86.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 86` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T06:32:43.701Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T06:32:44.375Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T06:32:44.392Z] TOOL RESULT

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


## [2026-09-05T06:32:44.451Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-86.txt"
}
```


### [2026-09-05T06:32:44.476Z] TOOL RESULT

```
1	=== PDF page 86 (book page 56) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bhen : to strike  (refs POK:126)
4	#1 (parent #0) [Avestan] refs=KLN:145; SYN:304 | ban : to be sick ; banta : sick ; banay : to make sick
5	  #2 (parent #1) [None] refs=None | 
6	#3 (parent #0) [Germanic] refs=AHD | banon : to strike
7	  #4 (parent #3) [Middle German] refs=None | bane : path cut through woods, road
8	    #5 (parent #4) [German] refs=AHD | auto-bahn : highway
9	      #6 (parent #5) [Persian] refs=None | otobân «اتوبان»
10	      #7 (parent #5) [English] refs=None | autobahn
11	
```


## [2026-09-05T06:32:47.427Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-86.json",
 "description": "Read source JSON for page 86"
}
```


### [2026-09-05T06:32:47.456Z] TOOL RESULT

```
{
  "pdf_page": 86,
  "book_page": 56,
  "entries": [
    {
      "root": {
        "name": "Bhen",
        "lang": "Indo-European",
        "refs": "POK:126",
        "gloss": "to strike"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KLN:145; SYN:304",
          "words": [
            {"translit": "ban", "gloss": "to be sick", "script": null},
            {"translit": "banta", "gloss": "sick", "script": null},
            {"translit": "banay", "gloss": "to make sick", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "banon", "gloss": "to strike", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Middle German",
          "refs": null,
          "words": [
            {"translit": "bane", "gloss": "path cut through woods, road", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "German",
          "refs": "AHD",
          "words": [
            {"translit": "auto-bahn", "gloss": "highway", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "otobân", "gloss": null, "script": "اتوبان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "autobahn", "gloss": null, "script": null}
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


## [2026-09-05T06:32:48.297Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T06:32:48.334Z] TOOL RESULT

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


## [2026-09-05T06:33:06.459Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"autobahn\" AHD_watkins1985.txt KLN_1966.txt KLN_1971.txt SKT.txt WEB_vol1.txt FSD_vol1.txt 2>/dev/null | head -40",
 "description": "grep autobahn in western refs"
}
```


### [2026-09-05T06:33:06.516Z] TOOL RESULT

```
AHD_watkins1985.txt:545:sive reduplicated form *gr-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITA- TION; INGURGITATE, REGURGITATE. 4. Extended form *gwr6- (< *geroa-) in Greek br6- in: a. suffixed redupli- cated form bi-bré-sko- in Greek bibréskein, to eat: HELLEBORE; b. nasalized variant form *bro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRON- CHUS; C. suffixed form *gvré-mn in Greek bréma, food: THEOBROMINE; d. suffixed form *gvr6-ti- in Greek bro- sis, eating: ABROSIA. [Pok. 1. gver- 474.] gwes-. To extinguish. Suffixed variant form *sgves-nu- in Greek sbennunai, to extinguish: ASBESTOS. [Pok. g¥es- 479.] g”et-'. Resin (?). Only in Germanic and Celtic. Suffixed form *gvet-u- in: a. Germanic *kwithu- in Old English cwudu, cwidu, cudu, resin, mastic gum, “that which is chewed,” cud: CUD, QUID!; b. Celtic *betu-, birch, birch resin, in Latin bitumen, resin (Gaulish loanword): BITU- MEN. [Pok. 1. g¥et- 480.] gwet-2. To say, speak. Germanic *kwithan in Old English cwethan, becwethan, to say, speak: BEQUEATH, BEQUEST, QUOTH. [Pok. 2. g¥et- 480.] gvet-3. Intestine. Suffixed o-grade form *gvot-olo- in Latin botulus, intestine, sausage: BOTULINUM, BOTULISM, BOWEL; (BOTULIN). [Pok. gvet- 481.] ghedh-. To ask, pray. 1. Germanic *bidjan, to entreat, in Old English biddan, to ask, pray: BID. 2. Germanic *bidam, entreaty in Old English gebed (ge-, intensive and collective prefix; see kom), prayer: BEAD. [Pok. gehedh- 488, 2. bhedh- 114.] gvhen-'. To strike, kill. 1. O-grade *gvhon- in Germanic suffixed form *ban-6n- in: a. Old English bana, slayer, cause of ruin or destruction: BANE; b. Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN. 2. Suffixed zero-grade form *ghn-tyd- in Germanic *gundjé, war, battle, in: a. Old Norse gunnr, war: GUN; b. compound *gund-fanon-, “battle flag” (fandn-, flag; see pan-), in Italian gonfalone, standard: GONFALON. 3. Suffixed form *gvhen-do- in: a. Latin défendere, to ward off (dé-, away; see de-): DEFEND, (DEFENSE), (FENCE); b. Latin offen- dere, to strike against, be offensive, offend (ob-, against; see epi): OFFEND, (OFFENSE). 4. Suffixed zero-grade form *gvhn-tro- in Persian zahr, poison: BEZOAR. [Pok. 2. gthen-(2)- 491, bhen- 126.] g”hen-2. To swell, abound. Suffixed form *gvhen-eyo- in Greek euthenein (eu-, well; see esu-), to flourish: EU- THENICS. [Pok. 1. gthen- 491.] g’her-. To heat, warm. 1. Zero-grade *gvhr- with nasal suffix and analogical vocalism in Germanic *brenw-, to burn, forming *brennan (intransitive) and brannjan (transitive) in: a. Old English beornan, byrnan (intransi- tive) and bérnan (transitive), to burn: BURN}; b. late Old English brynstan, “burning mineral,” sulfur (stan, stone; see stei): BRIMSTONE. 2. Germanic *brandaz, a burning,
AHD_watkins1985.txt:1270:AUSPICE awi-, spek- AUSTERE saus- AUTACOID y@k- AUTARCHY arkhein AUTARKY arek- AUTHOR aug-! AUTHORIZE aug-! AUTOBAHN g*hen-* AUTOCHTHON dhghem- AUTOECIOUS weik-1 AUTOGIRO géu- AUTOMATIC men-1 AUTONOMOUS nem-
```


## [2026-09-05T06:33:07.376Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"bhen\" AHD_watkins1985.txt | head -20; echo ---; grep -n \"bhen-\" POK_full.txt | head -20",
 "description": "grep bhen in AHD and POK"
}
```


### [2026-09-05T06:33:07.433Z] TOOL RESULT

```
184:Another aspect of the function of sover- eignty is the sphere of the law. There is an old word, yewes-, probably for “religious law,” in Latin jus. Latin léx is also ancient (leg-'), though the details of its etymology are uncertain. In a society that emphasized the principle of exchange and reciprocity, it is scarcely surprising that the notion of con- tractual obligation should be well repre- sented. Several roots specify the notion of “bond”: bhendh-, ned-, leig-', all of which have derivatives with technical legal mean- ings in various languages. The word for “a pledge,” wadh-', exists in western Indo- European, whence the English verb for mak- ing a particular kind of contract, WED. An oath then as now was important: the roots *serk- and oito- are found in Celtic and Ger- manic. The verb k”ei-' meant “to pay com- pensation for an injury.” Its derivative noun, *k“oind, was borrowed from Doric Greek into the most ancient Roman law as Latin poena, punire, whence English PUNISH and a host of legal terms. The Greek word for jus- tice, diké, is derived from the notion of “boundary marker” (deik-; compare also ter-, “termen-).
330:3. O-grade form *bhol- in Germanic *ball- in: a. Old English beallucas, testicles: BOLLIX; b. Old Norse bdllr, ball: BALL; c. Danish bolle, round roll, akin to the probable Scandinavian source of BILBERRY; d. Middle High German baile (> Italian balla, palla), ball: BAL- LOON, BALLOT; PALL-MALL; e. French baile, ball: BAL- LOTTEMENT; f. Old French baie, rolled-up bundle: BALE!. 4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in: a. Old English bald, beald, bold: BOLD; b. Old High German bald, bold: BAWD. 5. Suffixed o-grade form *bhol-n- in Latin follis, bellows, inflated ball: FOLLICLE, FOOL!; (FOLLICULITIS). 6. Possibly Greek phalaina, whale: BALEEN. 7. Conceivably (but more likely unrelated) Greek phellos, cork, cork oak: PHEL- LEM; PHELLODERM, PHELLOGEN. (The following deriva- tives of this root are entered separately: bhel-?, bhelgh-, bhlei-, bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Germanic *bladaz in Old English bled, leaf, blade: BLADE. [Pok. 4. bhel- 122.] bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to bellow, bark, roar: BELL?; b. Old English belle, a bell: BELL!; c, Old English belgan, bylgan, to become enraged: BELLOW; d. perhaps Old English bealcan, *b(iJelcan, to utter, belch forth: BELCH; e. Middle High German buldern, boldern, to make noise: POLTERGEIST; f. Icelandic baula, to low, akin to the Scandinavian source of Middle English baulen, to howl: BAWL. [Pok. 6. bhel- 123.] bheld-. To knock, strike. Zero-grade form *bhid- in Germanic *bult-, missile, in Old English bolt, heavy arrow, bolt: BouT!. [Pok. bheld- 124.] bhelg-. Also bhelk-. A plank, beam. 1. Germanic *balku- in Old English balc(a), ridge: BALK. 2. Germanic *balk6n- in: a. Old French bauch, beam: DEBAUCH; b. Old Italian balcone, scaffold: BALCONY. 3. Suffixed zero-grade form *bhik-yo- in Latin fulcire, to prop up, support: FULCRUM. 4. Possibly Greek phalanx, beam, finger bone, line of battle: PHALANGE, PHALANX. [Pok. 5. bhel- 123.] bhelgh-. To swell. Extension of bhel-2. 1. Germanic *balgiz in Old English bel(ijg, belig, purse, bellows: BELLOWS, BELLY. 2. Germanic *bulgjan in Old Norse bylgja, a wave: BILLOW. 3. Germanic *bolgstraz in Old English bolster, cushion: BOLSTER. 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.) bhelu-. To harm. Germanic *balwaz in Old English bealo, b(e)alu, harm, ruin, bale: BALE?. [Pok. bheleu- 125.] bhendh-. To bind. 1. Germanic *bindan in Old English bindan, to bind: BIND; WOODBINE. 2. O-grade form *bhondh- in Germanic *band- in: a. Old English bend, band, ribbon, akin to the Germanic source of Old French bende, band: BEND?; b. Old English bendan, to bend: BEND!; c. Old Norse band, band, fetter: BAND!, BOND; d. Old French bande, bond, tie, link: BAND!. 3. Zero-
332:grade form *bhndh- in Germanic *bund- in: a. Middle High German bunt, league: BUND?; b. Middle Dutch bondel, sheaf of papers, bundle: BUNDLE. 4. Suffixed form *bhendh-na-, “tied structure” (as of wicker), in Celtic *benna, manger, in Old English binn(e), manger: BIN. 5. Persian band, band, bandage, also a river levee: BUND!; CUMMERBUND. 6. Sanskrit badhndti (Sanskrit root bandh-), he ties: BANDANNA. [Pok. bhendh- 127.] bhengh-. Thick, fat. Extended zero-grade form *bhnghu- in Greek pakhus, thick, fat: PACHYDERM, PACHYSANDRA. [Pok. bhengh- 127.]
545:sive reduplicated form *gr-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITA- TION; INGURGITATE, REGURGITATE. 4. Extended form *gwr6- (< *geroa-) in Greek br6- in: a. suffixed redupli- cated form bi-bré-sko- in Greek bibréskein, to eat: HELLEBORE; b. nasalized variant form *bro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRON- CHUS; C. suffixed form *gvré-mn in Greek bréma, food: THEOBROMINE; d. suffixed form *gvr6-ti- in Greek bro- sis, eating: ABROSIA. [Pok. 1. gver- 474.] gwes-. To extinguish. Suffixed variant form *sgves-nu- in Greek sbennunai, to extinguish: ASBESTOS. [Pok. g¥es- 479.] g”et-'. Resin (?). Only in Germanic and Celtic. Suffixed form *gvet-u- in: a. Germanic *kwithu- in Old English cwudu, cwidu, cudu, resin, mastic gum, “that which is chewed,” cud: CUD, QUID!; b. Celtic *betu-, birch, birch resin, in Latin bitumen, resin (Gaulish loanword): BITU- MEN. [Pok. 1. g¥et- 480.] gwet-2. To say, speak. Germanic *kwithan in Old English cwethan, becwethan, to say, speak: BEQUEATH, BEQUEST, QUOTH. [Pok. 2. g¥et- 480.] gvet-3. Intestine. Suffixed o-grade form *gvot-olo- in Latin botulus, intestine, sausage: BOTULINUM, BOTULISM, BOWEL; (BOTULIN). [Pok. gvet- 481.] ghedh-. To ask, pray. 1. Germanic *bidjan, to entreat, in Old English biddan, to ask, pray: BID. 2. Germanic *bidam, entreaty in Old English gebed (ge-, intensive and collective prefix; see kom), prayer: BEAD. [Pok. gehedh- 488, 2. bhedh- 114.] gvhen-'. To strike, kill. 1. O-grade *gvhon- in Germanic suffixed form *ban-6n- in: a. Old English bana, slayer, cause of ruin or destruction: BANE; b. Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN. 2. Suffixed zero-grade form *ghn-tyd- in Germanic *gundjé, war, battle, in: a. Old Norse gunnr, war: GUN; b. compound *gund-fanon-, “battle flag” (fandn-, flag; see pan-), in Italian gonfalone, standard: GONFALON. 3. Suffixed form *gvhen-do- in: a. Latin défendere, to ward off (dé-, away; see de-): DEFEND, (DEFENSE), (FENCE); b. Latin offen- dere, to strike against, be offensive, offend (ob-, against; see epi): OFFEND, (OFFENSE). 4. Suffixed zero-grade form *gvhn-tro- in Persian zahr, poison: BEZOAR. [Pok. 2. gthen-(2)- 491, bhen- 126.] g”hen-2. To swell, abound. Suffixed form *gvhen-eyo- in Greek euthenein (eu-, well; see esu-), to flourish: EU- THENICS. [Pok. 1. gthen- 491.] g’her-. To heat, warm. 1. Zero-grade *gvhr- with nasal suffix and analogical vocalism in Germanic *brenw-, to burn, forming *brennan (intransitive) and brannjan (transitive) in: a. Old English beornan, byrnan (intransi- tive) and bérnan (transitive), to burn: BURN}; b. late Old English brynstan, “burning mineral,” sulfur (stan, stone; see stei): BRIMSTONE. 2. Germanic *brandaz, a burning,
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1288:BEND! bhendh- BEND? bhendh- BENEATH ni BENEDICTION deik-
1299:BILBERRY bhel-2 BILINGUAL dnghi BILIRUBIN reudh-1 BILIVERDIN virére BILL! beu-1 BILL? bhei-2 BILLS = bhei-2 BILLET! beu-1 BILLET-DOUX = dik-u- BILLOW bhelgh- BILTONG bhel-2, dnghi BIMESTRIAL mé-2 BIN bhendh- BINAL dwo- BINARY dwo- BIND bhendh- BINNACLE ghabh- BINOMIAL nem- BIO- gW¥ei-
1313:BOLD bhel-2 BOLE! bhel-2 BOLL bhel-2 BOLLIX bhel-2 BOLOMETER gW¥ele-1 BOLSHEVIK bel- BOLSTER bhelgh- BOLT! bheld- BOMB bamb- BOMBARD bamb- BONANZA deu-2 BONBON deu-2 BOND bhendh- BONDAGE bheue- BONHOMIE deu-2, dhghem- BONITO deu-2 BONNE deu-2 BONNYCLABBER band- BONTEBOK bhugo- BONUS deu-2 BOOBY baba- BOODLE bheue- BOOK bhago-
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
2031:PACHISI penkwe, wikmti PACHYDERM bhengh- PACHYSANDRA bhengh- PACIFIC pag- PACIFY pag-
---
```


## [2026-09-05T06:33:17.846Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"== $f\"; grep -n \"schlagen, verwunden\" $f | head; done",
 "description": "grep Pokorny bhen entry"
}
```


## [2026-09-05T06:33:18.975Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"banta\" BRT.txt | head -20; echo \"=== ban- BRT\"; grep -n \"krank sein\" BRT.txt | head -20",
 "description": "grep Bartholomae for Avestan ban-"
}
```


### [2026-09-05T06:33:19.239Z] TOOL RESULT

```
== POK_01.txt
== POK_02.txt
== POK_03.txt
== POK_full.txt
```


### [2026-09-05T06:33:19.295Z] TOOL RESULT

```
3771:•  j.  a-banta-"',  a-vanta-'*  Adj.  (fem.  °tä-) "nicht  krank,  gesund':  'Umcit  bandayeifi\ bantimät  (sd.)  drüm  hrmaoili  V.  22.5;! —  pasulca  . .  'ta  (NSf.)  airista  N.  56;  —  ' yat  fräyatayat  . .  aei  nmämm  .  .  drBm  1 't)nt  airistsm  (sd.)  YL5.65.  1
4368:•  j,  an-^azdya-  Adj.  'nicht  fett,  mager*: nSit  pasusLO  (statt  IS.)  iazda  nsi/  irista (sd.)  {nOit)  °ya  ratufris  abanta  airista *asdya  .  .  N.  ^6;  —  ratufrii  *paysbis  . . ^azdyäisca  *'\\iuca'^^  .  .  pitus  .  .  *atdysii n5it*°yäis'K.  mskSmua  rTzuüa..  *asdyäif näit *'y3is'> N.5 7 ; — ratufris  carTmanqmca pasv.vastranqmca  .  .  *asdyanqm  nSit *'yanqm ''    (nämL   pasunqm)  ^     "r.    wird
15638:•  j.  pairiSta-Bhara-  Adj.  'von  ausge- suchter Wohlgeoährtheit,  auserlesen  feisf : neil  pastiica  (statt  IS.)  . .  irista  (sd.)  riüu- frÜ  abanta  airiäa  *aiäya  'ra  raiußis S.56.
16696:•  j.  banta-  Adj.  (fem.  °tä-)  'erkrankt; krank,  siech':  ä/riti  .  .  yä  .  .  avanhmHt bandayeiti  'hmca  drSm  k»rmaoiH  ".  .  die den  Nichtkranken  krank  werden  lässt  und den  Kranken  gesund  macht"  V.  22.  s  ;  — fravalayS  .  .  yä  .  ,  dä%rT/  'iäi  drvatättm Vl/J.  24;  —  Ha  F.  16.
16712:bqnaya-'\  —  PPfP.  banta-  (sbes.).  •  j.    (,   p.)   banda-    m.  'Bande,    Fessel':
16817:a)  '(Kleider)  herabziehen  sva,  von oben  her,  über  den  Kopf  her  anlegen'; yS  vastra  vastnm  *aiwyaithaysrii  *itzba- rmti  (sd.)  . .  uparat  ftaOnai  ava-bannti  . . N.pJ.  a)  'hinzu-,  herzubringen,  ver- schafien':  *yaoxHayS  ava-bantam  (statt Hur.)  F.  4  g;  —  cvat  gaonahe  (sd.)  ava.- barat  N.  65.  a)  mit  Angabe  des  wohin? oder  wem?,  a)  durch  avi  mit  Abi.:  ya^a ..amirjxtim  ava,baram  avi  mazdä  däma- iysYt.g.^;  9.  ß)durchGen.:  ya  vTspa- nqm  hairisinqm  .  .  rähwim  paima  ava.- baraiti  Y.  65.  2.  y)  «n^^-  Gen.-DaL  des Pron.:  ava  hl  gatam  baraym  afryeAe  (sd.) va  ..  V.  Ä  8;  —  Uta  hi  astunt  xratQm avaJiaraiti  vanma  (sd.)  Yt  //.  a;  V.  16. II.  3)  'etwas  anbringen  an—'  iupa mit  Akk.):  ava  hl  baraym  .  .  dsuru(sd.) Ufa  . .  manae^rfm  V.  13.  30.  4)  'etwas
17025:•  ].,  g.  baraziäta-  Adj.  'der  höchste,  hüchst- gelegene':  'te paiti  bantaAi  Aaraiiyg paiti bansayä  Y.  57.  19;  —  'taiibyS  gairibyö V. 2. 22;  —  'laihiaia  paiti  gätuha  V, 6^.45;  —  urvaranqm  .  ■  ysi  hftiii ..  'taca V.  2.  28; —  imä  raoiä  't?m  bar»zimanqm
17049:•  j.  bazda-  Adj.  'erkrankt,  krank,  siech'; nüii  pasuSca  (statt  IS.)  •da  nsit  irilta  (sA) . .  abanta  airista  N.56.
27973:•  j.  ■'"zaramaya-''  Adj.  'venius':  :far3~ %anam  hi  bantam  'yehe  raofnahe  (sd.) H.2'i8.
28965:yS  yimS  x!aUS . .  Aukairyat  A'  bantankat
=== ban- BRT
```


## [2026-09-05T06:33:23.216Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16690,16720p' BRT.txt",
 "description": "Read Bartholomae ban- context"
}
```


### [2026-09-05T06:33:23.261Z] TOOL RESULT

```
VgL  iSiirav-.
•  j.  bawrinay-  Adj,  'vom  Biber  stammend, Biber"';  'wraini'^  (APn.)  vasträ  .  ,  Sma- tanam  bauiranqtn  (sd.)  Yt.5.  129.
Ableit.  aus  bawra-.  —  Vgl.  lit  bibrinis  {io- Stamm).  —  ')  Statt  •■wrim  geschr.,  S  ^S.  9. (S.  noch  ipmaiiil,  liispö .tailü,  iailayc^
•  j.  'baoha-,  bangha-''>  m,  i)  Name einer  Pflanze*'  (und  deren  Saft),  die  auch zur  Kind  sab  treibung  benutzt  wurde:  asia kana  frabaraiti  'him  vä  iaffym  vü  .  . kqmcii  Vä  vTtaananqtn  urvaranqm  V.  i^. 14.  z)  Name  eines  aus  jener  Pflanze hergestellten  Narkotikums '>  und  zugleich
dvär^nts  yä  bqnayitt  ahüm  maniSnS  "zu- sammen gingen  sie  darauf  zu  A.  über, durch  den  sie  das  Leben  der  Menschen krank  machen"  Y.^jo.ö".
Vgl.  got.Äoiy o 'Wunde',  ahd.  *a«fl' Verderben'». —  S.  auch  'band-.  —  Pü.;  vimärhtilan,  erl. : ähökcmian.  —  ■>  S  3g6.  3.  —  ')  Vgl.  dagegen IQ  ^aAümM-.  —  j)  Doch  a.  Zupitza  Gu(t,  30.
•  j.  banta-  Adj.  (fem.  °tä-)  'erkrankt; krank,  siech':  ä/riti  .  .  yä  .  .  avanhmHt bandayeiti  'hmca  drSm  k»rmaoiH  ".  .  die den  Nichtkranken  krank  werden  lässt  und den  Kranken  gesund  macht"  V.  22.  s  ;  — fravalayS  .  .  yä  .  ,  dä%rT/  'iäi  drvatättm Vl/J.  24;  —  Ha  F.  16.
KompE.  (fl*%  av).  —  PHP.  wm  V,  ian-,  — Vgl.  bazda-.  —  Pfi.:  vimär.
•  j.,  p. "band- V, 'binden'.  Pr^es.  8  *ba»ad-z band-'\  34  bandaya-.  —  PPfP.  basta-'^.
r)  'binden,  fesseln':  is'ar  pasca  puxl>m bandum  (sd.)  bandyät^''  Vd./3;  —  dazdi tm  .  .  ydha  .  .  bandayem  .  .  franrasyämm Uta  basttm  vätayeni  uta  bastfm  upana-
\yeni  bast?m  ,  .  Yt.5,  '^J  —  haosrava  .  .
\frat3rasyamm  bandayat  Yt  Jp-  77 ;  Y.  //.  7;
—  mä  SiCiä  haomS  bandayat  ya'ha  . .  Y. II.  7;  —  astä.vioStu/ diin  bandayati  vayS dim  bastitn  hayeiti  V.5.  8; — yat  bastS at?hal  hiit>mnB  Yt.  1$.  52;  52',  2.  i4(?);
—  D  hauv  basta^  anayatä  abty  mäm  Bh. /.  17;  —  duvarayämaiy  basta*  adäriy Bh.  2.  13,  14;  1  —  %wqmäi  "drvfimca *banadämi''^  .  .  niyne  .  .  nUbanm  Vt  4. 5.  z)  Med.  'sich  etwas  an-,  um-,  fest- binden': upairi  pusqm  (sd.)  bandayata YL5.  is8.  3)  'zusammenbinden,  an einander  befestigen':  *hqm.ivqmca  (sd.) smqmea    simSt^rqmca    dargta    huktnta
upairi.späta    aka    bastqm    (APn.?)    Yt.
Bezeichnung  des  dadurch  hervorgerufenen
Betäubungszustandes 3'  (nur  Komp,).  i'"-»^s-    ^
KompE. ;  Ableit.  -  ai.  rgl.  b/rnAgä-  f.  i)  'HanP, )  "■  i-adknaU,  baddhäh,  mi,  batdhau ;  np.  bandad, a)  ■Narttotittum  aus  Hanf  J) ;  np.  bang  'Bilsen- 1  *"'■"■  —  ^^-  ■  *'"'""■  —  ''  Beide  Stammformen kraut'.  —  Pii. !  mang-*),  erL :  /  vihäspi».  —  hBchst  unsicher;  s.  No.  3  und  4-  —  •>  S  53  H- t)  «h,  «gk  statt  ng,  TgL  S  36S.  47,  46  und  .  —  "  Es  wird  wohl  bandayat  gememl  sein.  — die  Var.  lo  V.  ig.  20.  41,  Yt.  13.  124,  femer  1,  «  So  F  1 ;  iSPA.  mit  Ibem.  Ausgang;  vgl.  b,ba- sparnka-,  pisöHngka:     —     ")  Vgl.  dazu  JUSTI ,      '"'""'•     NA.  bandämi.
HB.  254.  — 3)  VgL  ai.oidi/fl-' Rauschtrank' und  •  j.  »band- V. 'kranken'.  Praes  30  (Kaus.) •Rausch'.  -  :.)  S.  dazu  West  Av.-Gloss,  220.  \  bandaya-.  —  PPfP.  bazda-  (sbes.).
•  j.  'baaha-  Adj,  'narkotisirt,  trunken':^  Kaus.'krankmachen':4*<'f(.._v^..aj'<M- damm  kundsm  -hftn  vJ.banh^  (sd.)  "^ .  t?mcit  bandayeiti  bant>mca(%t.)  drüm  km- '5-41-  naoiti  V.  22.  g-
Ableit  aus  OawAa-.  —  Pü.r  ntasl.  I      a'.i.'Erweitening'ausAan..  — Pü.{: aj'ÜOTörMaa«,
•  i-.g.ban-V. 'kranken'.  Praes.  30  (Kaus.)  '     ü«):  vimäreiiUa«;  %.  va  ban-.
bqnaya-'\  —  PPfP.  banta-  (sbes.).  •  j.    (,   p.)   banda-    m.  'Bande,    Fessel':
Kaus.  'krank  machen':  at  aEsam^m  hSr^-   *spayeiti  .  .   dafita    mäsdayasnil  nars  ,  .
dby  Google
927  bay-  —  bav-  2  928
'dim  V..J.41;  — »(/JCNP.)  Y.16.        a)  in|Yt(?.a;  2.  a)    mit  einer  örtlichen  Be-
Vd. 'Verbindung':  tiar  pasca puxofm 'd»m  Stimmung  durch   a)  Lok,,  auch  sva.  'sich
banäyät    ya%a    ali<a    anguftqm    .  .    (soll  (wo)   einstelien':    kva  ta  ää'hra  {%A.)    ba-
heissen)    "sofort    soll    man    alsdann    dis\vainti  V. 79. 27;  \%.i8.^   {bavaiti'f);  —
ftinfTache  VerbinduDg  herstellen,   nämhch '  buylt  ahmt  nmsne  gSusca  va'hwa  "es  soll
```


## [2026-09-05T06:33:31.304Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"banja\" POK_full.txt | head -20; echo \"=== files\"; ls -la POK_*.txt; echo; grep -n \"bhen\" POK_full.txt | head -20",
 "description": "grep Pokorny for banja / bhen"
}
```


### [2026-09-05T06:33:31.367Z] TOOL RESULT

```
=== files
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt

9653:Root / lemma: band- {*bhend-) 
9661:band- {* bhend-): "drop' derived from a zero grade of Root/ lemma: au(e)-9, aued-, auer-
```


## [2026-09-05T06:33:35.451Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: bhen\" POK_full.txt | head; echo ===; grep -n \"Page(s): 126\" POK_full.txt | head; echo === ; grep -n \"^Root / lemma: bhe\" POK_full.txt | head -30",
 "description": "find bhen- in POK_full"
}
```


### [2026-09-05T06:33:35.500Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-05T06:33:38.339Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: bhen\" POK_full.txt | head -20; echo \"-----\"; grep -n \"Page(s): 126\" POK_full.txt | head -20; echo \"-----\"; grep -n \"Root / lemma: bhe\" POK_full.txt | head -40",
 "description": "find bhen in POK_full"
}
```


### [2026-09-05T06:33:38.410Z] TOOL RESULT

```
-----
12126:Page(s): 126-127 
-----
10965:Root / lemma: bhedh_/(bhedh-i > *b^e6^-r) 
11116:Root / lemma: bheigr"- 
11748:Root / lemma: bhe/-2( > *bhel-(e)-n-)
```


## [2026-09-05T06:33:40.473Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12080,12135p' POK_full.txt",
 "description": "Read POK page 126 area"
}
```


### [2026-09-05T06:33:40.522Z] TOOL RESULT

```
Latin offendimentum, offendix^ the knot of a band, or the band itself, chin strap under 
priest's cap, apex ( a Roman priest's cap), fastened with two strings or bands'; 



gall. benna'V\u6 of vehicle', Galatian Zsuc; Bsvvioq, cymr. /7e/7/7 "wagon, cart' (out of it Old 
English binn, and through roman. mediation Modern High German dial, it*©/?/?© "carriage 
boxes', Dutch i?e/7 "basket, trough'; basic form *b^en6'^-na)\ Middle Irish bu/nne'strap, 
bangle ' {*b^on6^/a); (common Celtic -ns-, -nt- > -nn-). 

Gothic Old English b/ndan, Old Icelandic b/nda, Old High German b/nfan^b\n6', Gothic 
andbundnan "\s unfastened ', Gothic band/ etc see above; 

Lithuanian bendras ^partner, comrade' (formant associated with gr. nEvGspoq), banda' 
herd of cattle ' (actually "the tied (down) cattle, the bound cattle '). 

Here also Gothic banstsm. "barn' {*b^on6^-str, compare in other meaning Old Frisian 
bosf^ matrimonial union' from *b^on6^-stu- 'bond'; 

ndd. banse' silo, garner, barn'. Old English *bds, engl. i^oose "cattle shed'. Old English 
bos/'g' cnb', Old Icelandic bassm. "room for keeping, cattle stall' {*band-sa-); 

jut. bende^ divided off room in cattle shed' erases probably every doubt about the 
relationship of above group with binden. 

References: WP. II 152, WH. I 102, Feist 79, 80 f., 93. 
Page(s): 127 



Root / lemma: b^end- 

Meaning: to sing, rejoice 

Material: Old Indie bhandate 'rece'wes cheering shout, is praised, glares, gleams', 

bhandistha-h^ in loudest cheering, shrilly, screaming, best of all praising ', 

t>handana-h ^ cheenng' , bhandana ' merry tintinnabulation, cheer' (doubts the meaning 

partly); zero grade Old Irish Middle Irish i7//7o' "melodic', abret. /7a/7/7 'melodious, 

harmonious', (common Celtic -ns-, -nt- > -nn-). 

References: WP. 111 51 f. 

Page(s): 126-127 

Root/ lemma: b^engh-, b^Qgh-{M]. b^pghu-s) 
Meaning: thick, fat 

Material: Old Indie bahu-'der\se, rich, much, a lot of "compounds Sup. barhhlyas-, 
batfihistha- {= gr. naxu(;); 

bahula-^Mck, dense, vast, spacious, big, large, rich, much, a lot of (= gr. naxuAwq Adv. 
by Aristot., if these not newer formation); bambate {ur\covered) ' increase, multiply ',
```


## [2026-09-05T06:33:44.365Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: b\\^en\" POK_full.txt | head -20; echo \"-----\"; grep -n \"Page(s): 126 \" POK_full.txt | head -20",
 "description": "find b^en- lemma"
}
```


### [2026-09-05T06:33:44.425Z] TOOL RESULT

```
11066:lemma: b'^eg-, b'^eng-: "to break', Root/ lemma: b^engh-, b'^pgh-iM]. b'^pghu-s) : "thick, 
12033:Root / lemma: b^en6^- 
12110:Root / lemma: b^end- 
12128:Root/ lemma: b^engh-, b^Qgh-{M]. b^pghu-s) 
-----
```


## [2026-09-05T06:33:49.970Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Meaning: to strike\" POK_full.txt | head -20; echo \"-----\"; grep -n -i \"banja\\|bania\\|ban/a\" POK_full.txt POK_01.txt POK_02.txt POK_03.txt | head -20",
 "description": "search Pokorny for banja / to strike"
}
```


### [2026-09-05T06:33:50.032Z] TOOL RESULT

```
15527:Meaning: to strike; to throw 
-----
POK_01.txt:1774:bhen-  ,schlagen,   verwunden';    auch  von    durch    den   Schlag   böser   Geister bewirkter  Krankheit  (avest.;  vgl.  zu  diesem  Aberglauben  Havers  IF. 25,  380  f.) Av.  bqnaydn  ,sie  machen  krank',  banta-  , erkrankt,  siech'; got.  banja  , Schlag,  Wunde,  Geschwür',  aisl.  ben,  ags.  benn  f.,  as.  beni- tüunda   ,Wunde';    aisl.  bani   m.  ,Tod;    Mörder',   ags.  bana^    ahd.    as.  bano ,Totschläger,  Mörder',  ahd.  bano,  mhd.  hane,  ban  ,Tod,  Verderben';    viel- leicht auch  mhd.  bane,  ban  f.  und  m.  ,Bahn,  Weg'  als  ,*Durchhau  durch einen  Wald'  oder  ,*festgeschlagener  Weg';   mir.  epit  f.  , Hippe'  aus  *ek8- bhen-tl-  corn.  bony  ,Axt';  aber  cymr.  &on-cZws^ , Ohrfeige' enthält  bon  , Stock'. Av.  bata-j  wenn  ,geschrotet,  vom  Getreide',  könnte  als  *bhn-to-  verwandt sein,  ist  aber  wegen  der  unsichern  Bed.  nur  mit  Vorbehalt  zu  nennen. WP.  II  149,  Feist  80.
POK_full.txt:37:Albanian 
POK_full.txt:1256:Albanian is another unique and distant branch of Indo-European, and also preserves some 
POK_full.txt:2088:French aisselle : Calabrese ma-scidda; sciddra; titiddra; titilla : Albanian Geg sqetlla, Tosc 
POK_full.txt:2147:(desonarized ((e)knedd Albanian Geg kinxh, Tosc qengj 
POK_full.txt:2570:The old laryngeal in centum languages h- > a-, e- : Slavic y- : Albanian k- : Italic /?-. 
POK_full.txt:2888:common Hittite p/77e- : Slavic p/7jo- : Albanian p/7ia- > pe- prefix. 
POK_full.txt:3314:Maybe alb. zero grade {*ccipitei) skifter^ hawk', shqiptar' eagle-man, Albanian ', 
POK_full.txt:3315:shqiponje^ e3iq\e\ Shq/per/land of the eagles, Albania', 5/7(7//? 'language of the eagle-men, 
POK_full.txt:3316:Albanian language'. 
POK_full.txt:3321:agucidn da testa : Romanian {*{a)ghimpe) ghimpe : Albanian glemb, gjemb " sting ' from 
POK_full.txt:3331:Albanian Geg gjyi-pane, Tosc gjil-pere 
POK_full.txt:4985:Albanian -a feminine ending proves the lllyrian origin. 
POK_full.txt:5017:Bresciano nedra, Reggiano nader; nadra, Greek gr. vnaaa, Boeotian vaaaa, Albanian 
POK_full.txt:5223:Maybe from Greek lllyrian syxsAuc; " eel ' > alb. ngja/e' eel ' [common Albanian Slavic yx- 
POK_full.txt:5948:Albanian. 
POK_full.txt:6318:Maybe alb. {*herg-) Jarge "white saliva' Common h- > j- Slavic Albanian; h- >j-, y- Old Indie 
POK_full.txt:6341:Maybe Albanian argjend: Bresciano arzent: Romagnolo arzent: Zeneize arzento 'sWver' 
POK_full.txt:7303:It seems Albanian cognate has wrong etymology. 
POK_full.txt:7305:Maybe Basque N egunsenti: Estonian : N agu: Albanian : N agu, agim: Turkish : N
```


## [2026-09-05T06:33:59.052Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1755,1790p' POK_01.txt",
 "description": "Read POK_01 around bhen entry"
}
```


### [2026-09-05T06:33:59.094Z] TOOL RESULT

```
Acorn.  bal  f.,  pl.  -ow  ,Krankheit',  mbr.  baluent]
got.  balwa-ivesei  jy.ay.la\  balwjan  ,quälen',  ags.  bealo  ,übel,  böse',  aisl. bql,  Dat.  bglve  ,Unglück',  ahd.  balo,  Gen.  öaZazües  , Verderben' ;  got.  bligg- tcan  (*bleuiian)  ,schlagen',  ahd.  bliuwan,  nhd.  bleuen  ds.,  mengl.  blowe ,Schlag',  aisl.  blegde  m.  (*blauuiäan-)  ,Keil';
abg.  boh  ,Kranker',  boUti  , krank  sein'.
Über  nhd.  Block  usw.  s.  unter  5.  bhel-.
WP.  II  189,  Hirt  Idg.  Gr.  II  150,  Feist  79,  100,  Specht  Dekl.  133.
Daneben  eine  Wzf.  bhleii-  :  bhhu-  :  bJilü-,  s.  dort.
bbelgh'  ,schwellen;    Balg   (aufgeblasene   Tierhaut),    Kissen,  Polster'  (Erw.
von  bhel-  ,aufblasen'  usw.).
Ai.    barhü'   n.   ,Streu,    Opferstreu'  =  av.  bardzis-  n.  ,Polster,    Kissen'
npers.  bälis  , Kissen';   ai.  upa-bdrhana-m,   npa-bdrhanl  f.  , Decke,  Polster';
Ob  mit  Asp.-Diss.  gegen  das  Formans  -ha-  hierher  ai.  bdrjaha-h  , Euter'?
ir.    bolgaim    ,schwelle',    bolg   f.   ,Blase',    bolg  m.   ,Sack,    Bauch,    Hülse,
126  '
,  Hose',  mir.  holgach  f.  ,Beule,  Blase,  Blatter;  Pocken',  bolgamm  ,Schlucl^^ cymr.  hol,  bola,  holy  ,Bauch,  Sack',  hui  ,Sainenhülse'  (PL  von  holy),  bret; holc'h  ,cosse  de  lin',  vann.  pehl-en  (aus  *pehl-)  ds.,  gall.  bulga  ,Ledersac]i< (daraus  ahd.  hulga  ,lederner  Wasserbehälter*);  gall.  Belgae  ,die  Zornigen^
got.  balgs  ra.  ,Sclilauch',  aisl.  belgi^  m.  ,abgestreifte  Tierhaut,  Balg Bauch',  ahd.  mhd.  balg  ,Balg,  Schlauch,  Blasebalg,  Schwertscheide',  agg, bielg,  byl{i)g  ,Balg,  Beutel',  engl,  belly  ,Bauch',  bellows  ,Blasebalg'  (germ. *balii-  m.,  vgl.  apr.  balsinis]  vielleicht  hat  auch  ai.  barhls-j  av.  barezii, idg.  -i-s-  als  Erw.  dieses  i-St.);  .
aisl.  Partiz.  bolginn  ,geschwollen',  Kaus.  belgja  , aufschwellen  machen' as.  ags.  belgan  St.-V.  ,zornig  sein',  ahd.  belgan  ,aufschwellen',  refl.  ,zö^ nen',  afries.  Partiz.  ovirbulgen  ,erzürnt';
aisl.  bylgja  ,Woge',  mnd.  bidge  ds. ;  *bul{h)stra-  in  aisl.  bolstr  m.  ,Kisseii' ags.  bolster  n.  ,Polsteri  Kissen',  ahd.  bolstar  ds.,  ndl.  bolster , Fruchtbalg,  Hülse'
apr.  balsinis  ,Kissen'  (*bholghi-nos),  pobalso  , Pfühl',  lett.  pabälsts ,Kopfkissen'  (und  , Stütze',  s.  oben  S.  123);  slov.  blazina  ,Kissen,  Matratze] Bettpfühl;  Fuß-  oder  Handballen'  (und  , Dachbalken,  Querbaum  des* Schlittens,  Rungstock',  s.  oben  S.  123),  skr.  blazina  , Kopfkissen,  Polster^ti Federbett';  russ.  bolozem,  m.  , Schwiele,  Beule,  Leichdorn,  Hühnerauge^! (aber  russ.  dial.  bölozno  , dickes  Brett').  Hierher  wohl  als  ven.-ill.  Lw.^t apr.  balgnan  n.,  alit.  balgnas,  lit.  balnas  , Sattel'  (wohl  aus  ,Kissen').  Weitere  ' baltoslav.  Formen  s.  oben  S.  123.  -|
WP.  II  182  f.,  WH.  I  122.  Vgl.  über  gr.  nolyog  ,Ledersack'  Vendryes BSL.  41,  134  f.
bhen-  ,schlagen,   verwunden';    auch  von    durch    den   Schlag   böser   Geister bewirkter  Krankheit  (avest.;  vgl.  zu  diesem  Aberglauben  Havers  IF. 25,  380  f.) Av.  bqnaydn  ,sie  machen  krank',  banta-  , erkrankt,  siech'; got.  banja  , Schlag,  Wunde,  Geschwür',  aisl.  ben,  ags.  benn  f.,  as.  beni- tüunda   ,Wunde';    aisl.  bani   m.  ,Tod;    Mörder',   ags.  bana^    ahd.    as.  bano ,Totschläger,  Mörder',  ahd.  bano,  mhd.  hane,  ban  ,Tod,  Verderben';    viel- leicht auch  mhd.  bane,  ban  f.  und  m.  ,Bahn,  Weg'  als  ,*Durchhau  durch einen  Wald'  oder  ,*festgeschlagener  Weg';   mir.  epit  f.  , Hippe'  aus  *ek8- bhen-tl-  corn.  bony  ,Axt';  aber  cymr.  &on-cZws^ , Ohrfeige' enthält  bon  , Stock'. Av.  bata-j  wenn  ,geschrotet,  vom  Getreide',  könnte  als  *bhn-to-  verwandt sein,  ist  aber  wegen  der  unsichern  Bed.  nur  mit  Vorbehalt  zu  nennen. WP.  II  149,  Feist  80.
bbend'  etwa  ,singen,  schön  klingen,  jauchzen'.
Ai.  bhandate  , empfängt  jauchzenden  Zuruf,  wird  gepriesen,  glänzt', bhdndi§tha-h  ,am  lautesten  jauchzend,  gellend,  am  besten  preisend',  bhan-
w
127
. ,  ^,^    jauchzend^,  bhanddnä  , lustiges  Tönen,  Jauchzen^  (die  Bedeutungen T    bezweifelt);    schwundstufig    air.   mir.   bind    , melodisch^,    abret.  bann
canora^ '    WP.  II  151  f.
^eadh'  ,binden^
;^i.  hadhnäti,  erst  später  bandhati  ,bindet,  fesselt,  nimmt  gefangen, i\\iri  zus/,  av.  bandayaiti  , bindet',  Partiz.  ai.  baddhd-,  av.  ap.  basta-,  ai. hdndhana-  n.  ,das  Binden',  bandkd-h  m.  ,das  Binden,  Band',  av.  banda-  m. Bande  Fessel'  (:  aisl.  as.  bant,  ahd.  bant  n.,  nhd.  Band ;  got.  bandi,  ags. l^end  f.  ds.;  lit.  Jant^a , Vieh',  s.  unten);  ai.  bdndhu-h  m.  ,Verwandter'  (wie jfsydsQÖg).
Gr.  ftstcfia  ,Tau,  Seil'  (aus  *7tsv^a^a,  Schwyzer  Gr.  Gr.  I  287,  vgl. Bru<^mann  IF.  11,  104 f.,  auch  für  jtsa^ia  und  rcdafia),  ^tev&SQog  , Schwieger- vater* (*,durch  Heirat  verbunden') ;  hierher  nach  Pedersen  (REtlE.  1,  192) auch  ftdaxo)  , leide'  als  , werde  gebunden,  verstrickt',  wie  auch  lat.  offendö o-erate  ins  Unglück,  stoße  an',  defendö  ,lÖse  aus  der  Verstrickung';  Ttd&vr] (spät  belegt,  aber  alt),  mit  Hauchumstellung  hom.  att.  cpdrvr]  , Krippe' (Hhndh-nä'j  unter  einer  Gdbed.  ,geflochtener  Korb'  wie  kelt.  benna ,Wagenkorb');  thrak.  ßevd-  ,binden'  (vgl.  Kretschmer  Einl.  236);  alb.  bese , Vertrag;  Glaube,  Waffenstillstand';  lat.  offendimentum,  offendix  ,das  Kinn- band an  der  Priestermütze';  gall.  benna  ,genus  vehiculi',  galat.  Zeig  Biv- yiogj  cymr.  benn  ,Fuhrwerk'  (daraus  ags.  binn,  und  durch  roman.  Vermitt- lung nhd.  dial.  benne  , Wagenkasten',  ndl.  ben  ,Korb,  Mulde';  Gdf.  Hhendh- nä)'j  mir.  buinne  ,Band,  (Arm)reif'  (*bhondhia)]
got.  ags.  bindanj  aisl.  binda,  ahd.  bintan  ,binden',  got.  andbundnan  ,ge- löst  werden',  got.  bandi  usw.  s.  oben;  lit.  bendras  ,Teilhaber,  Genosse' (formantisch  gr.  Ttsvd-SQÖg  nahestehend),  bandä  ,Viehherde'  (eig.  ,das  an- gebundene Vieh').
Hierher  auch  got.  bansts  m.  , Scheuer'  (*bhondh-sti]  vgl.  in  anderer  Bed. afries.  böst  , eheliche  Verbindung'  aus  *bhondh-stu-  , Bindung';  ndd.  banse ,Kornraum,  Scheune',  ags.  *5ös,  engl,  boose  ,Viehstall',  ags.  bösig  ,Krippe', aisl.  bäss  m.  ,Raum  zum  Aufbewahren,  Viehstand'  {*band-sa-)',  jüt.  bende ,abgeteilter  Raum  im  Viehstall'  schließt  wohl  jeden  Zweifel  an  der  Ver- wandtschaft obiger  Gruppe  mit  binden  aus.
WP.  II  152,  WH.  I  102,  Feist  79,  80  f.,  93.
bbcngh-,  bhngh-  (Adj.  bbngbü-s)  ,dick,  dicht,  feist'.
Ai.  baJiü-  , dicht,  reichlich,  viel'  ,Komp.  Sup.  bamhlyas-,  bamhistha-  (= gr.  Ttaxvg)]    bahuld-  ,dick,  dicht,  ausgedehnt,  groß^  reichlich,  viel' (=  gr.
128
rtaxvKbg   Adv.  bei    Aristot.,    wenn   dies   nicht   jüngere    Bildung);    hdniha^'i (unbelegt)  ,mebrt  sich',  hhdrhhayate  ^befestigt,  stärkt';
```


## [2026-09-05T06:34:19.014Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"Av\\. banta\\|banta-\\|bqnay\\|banay\" SYN.txt KLN_1966.txt KLN_1971.txt IEC.txt WLD_band3.txt 2>/dev/null | head -20",
 "description": "grep banta in Buck, Klein, Mann"
}
```


### [2026-09-05T06:34:19.075Z] TOOL RESULT

```
SYN.txt:7694:300 4.83 WELL; HEALTH Grk. is} bylea Goth. hails ; Lith sveikas; sveikaig NG oe yepos; byela ON heill; hetlsa Lett. —_vesels, Sveiks; veseliba Lat. sdnus, etc.; sdnilas, Dan. ask, sund; helbred, ChSl. stidravit, célii; stidra. ete. sundhed vije It. sano; salute Sw. frisk, sund; hdlsa, SCr. _zdrav; zdravlje Fr. sain; santé sundhet Boh. zdravy; zdravs Sp. sano; salud (sanidad) OE hal, gesund; hal, Pol. zdrowy; zdrowie Rum.  sédndlos; sdndtate h@lu Russ. zdorovyj; zdoroy! rs Tr. slan; slantu ME hole (hale), (i)sunde; Skt. svastha-, kugalin-; Nir. _ slan, follain; slainte helthe kugala-, aroga-, W. tach; techyd NE well, healthy; health ete. Br. yac’h; yec’hed Du. gezond; gezondheid Av. drva-, abanta-; dryq- OHG heil, gisunti; heili, lat- gisunii MHG heil, gesunt; heil, ge- sunde NHG  gesund; gesundheit
SYN.txt:7727:Av. abanta- epd. of a-privative and banta- ‘sick’ (4.84).
SYN.txt:7732:302 4.84 SICK; SICKNESS Grk.  da8evijs; vbcos, dodivaa Goth. stuks; siuket, sauhts | Lith.  sergas, nesveilas; Yj. NG = ppworos (aoderis); ON  sjttkr; sétl, sjikleiki 99, sirgimas apphoria (acdivea, (-démr) Lett. slims, nevesels; slim; véaos) Dan. syg; sygdom ba, neveseliba, liga Lat. ager; morbus Sw. sjuk; sjukdom ChSl.  boltnii; boléznt, nedq- It. malato; malattia OE séoc; suht, séocness, git, jedza Fy. malade; maladie ddl : SCr. _ bolestan; nemocan; Sp. enfermo; enfermidad ME stk(e), sek(e); sik- bolest, nemoé Rum. _ bolnav; boala ness, disese Boh. nemocnij; nemoc Ir. lobur; serg NE sick, ill; sickness, ill- Pol. — chory; choroba Nir. finn, breoidhte; tin- ness Russ. _bol’noj; bolezn' neas, aicid Du. ztek, krank; ziekte Skt. asvastha-, dlura-; vyd- W. claf; clefyd OHG _ sioh; stohi, suht dhi-, roga~ Br. klaniv; klerived MHG ssiech; suht(s), siech- Av. banta-, bazda; yaska- tuom (-heit. -lac) NHG_skrank; krankheit
SYN.txt:7792:Av. banta-, pass. pple. of ban- ‘be sick’ in caus. banaya- ‘make sick’ (also bazda-, pass. pple. of band- id.) : Goth, banja, ON ben, etc. ‘wound’, OE bang ‘murderer’, OHG bano ‘death, mur- derer’. Walde-P. 2.149. Barth. 996,
SYN.txt:7827:4. Goth. banja (renders r\ny4 ‘blow, wound’ and @xos ‘sore’), ON, OE ben : ON bani ‘death’, OE bana, OHG bano ‘murderer’, Av. banta- ‘sick’ (4.841), etc., all prob. fr. a root *bhen- ‘strike’. Walde-P. 2.149. Feist 80.
KLN_1971.txt:25571:Avestic banta, ‘ill’, bqnay e n , ‘they make sick 
KLN_1966.txt:4378:bane,  n.  —  OE.  bana,  ‘murderer,  slayer’,  rel.  to OE.  benn,  ‘wound’,  OS.  bano,  OFris.  bona. OHG.  bano,  ‘murderer’,  OHG.  bana,  ‘murder", ON.  bani,  ‘murderer,  murder,  death’,  ben. ‘wound’,  Dan.,  Swed.  bane,  ‘death,  murder’, Goth,  banja,  ‘stroke,  wound’,  and  cogn.  with Avestic  banta,  ‘ill’,  bqnayen,  ‘they  make  sick Derivatives:  bane-ful,  adj.,  bane-ful-ly,  adv., bane-ful-ness,  n.
```


## [2026-09-05T06:34:19.725Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"^bane\\|bane, n\\|bane (\" KLN_1966.txt | head -20; echo \"-----\"; grep -n \"banja\" KLN_1966.txt SKT.txt | head -20",
 "description": "grep Klein bane"
}
```


### [2026-09-05T06:34:19.809Z] TOOL RESULT

```
3115:Apocynaceae,  n.  pi.,  a  family  of  plants,  the  dog¬ bane  family  (bot.)  —  ModL.,  formed  with  suff. -aceae  fr.  Apocynum  (q.v.) apocynaceous,  adj.  —  See  prec.  word  and  -aceous. Apocynum,  n.,  a  genus  of  plants;  the  dogbane (bot.)  —  ModL.,  fr.  Gk.  ootoxuvov,  ‘dogbane’, fr.  ino  (see  apo-)  and  xutov,  gen.  xuv6 ‘dog’. See  cyno-.
4378:bane,  n.  —  OE.  bana,  ‘murderer,  slayer’,  rel.  to OE.  benn,  ‘wound’,  OS.  bano,  OFris.  bona. OHG.  bano,  ‘murderer’,  OHG.  bana,  ‘murder", ON.  bani,  ‘murderer,  murder,  death’,  ben. ‘wound’,  Dan.,  Swed.  bane,  ‘death,  murder’, Goth,  banja,  ‘stroke,  wound’,  and  cogn.  with Avestic  banta,  ‘ill’,  bqnayen,  ‘they  make  sick Derivatives:  bane-ful,  adj.,  bane-ful-ly,  adv., bane-ful-ness,  n.
13552:morning',  and  -y^vekx,  fr.  ysv-,  stem  of  y£yvea- ffai,  ‘to  become,  be  bom’.  See  ere  and  genus. Erigeron,  n.,  a  genus  of  plants,  the  daisy  fleabane (bot.)  —  ModL.,  fr.  Gk.  r)pty£pcov,  ‘groundsel’, which  is  compounded  of  )jpi,  ‘early’  and  yeptov, ‘an  old  man’  (see  Erigenia  and  geronto-);  so called  in  allusion  to  the  hoariness  of  some species.
18447:hyoid,  adj.,  designating  a  bone  at  the  base  of  the tongue  (anat.  and  zool.)  —  F.  hyoide,  fr.  Gk. uoet8ir;p,  ‘shaped  like  the  Greek  letter  T’,  which stands  for  (-oeiSt;;  and  is  compounded  of  the letter  V  and  -oeiSrjc,  ‘like’,  fr.  eI8o;,  ‘form, shape’:  see  -oid.  The  letter  was  called  later  u psihn  (lit.  ‘mere  or  simple  y’).  See  ypsilon. Derivative:  hyoid,  n.,  the  hyoid  bone, hyoscine,  hyoscin,  n.,  a  poisonous  alkaloid  (cltem.) —  See  Hyoscyamus  and  chem.  sulT.  -in(e). Hyoscyamus,  n.,  a  genus  of  plants,  the  henbane (1 bot .)  -  ModL.,  fr.  Gk.  uooxuapoc,  ‘henbane’, compounded  of  up,  gen.  bot;,  ‘hog,  pig’,  which is  cogn.  with  L.  stis  (see  sow,  ‘female  pig’),  and of  x-japoc,  ‘bean’,  a  word  of  foreign  origin.  The name  prop,  means  ‘poisonous  to  swine’.  Cp. hyoscine.
29201:Pluchea,  n.,  a  genus  of  plants,  the  marsh  fleabane (bot.)  —  ModL.,  named  after  the  French  Abbe N.-A.  Pluche  (1688-1761). pluck,  tr.  and  intr.  v.  —  ME.  plucken,  fr.  OE. pluccian,  ploccian,  fr.  VL.  *piluccare,  ‘to  deprive of  hair’  (whence  also  MHG.,  G.  pfliicken,  MDu. plucken,  plocken,  Du.  plukken,  ON.  plukka, plokka,  Dan  .plukka,  Swed.  plocka),  fr.  L  .pilare, ‘deprive  of  hair’,  fr.  pilus,  ‘hair’.  It.  piluccare,  ‘to pluck  grapes’.  Proven?,  pelucar,  ‘to  pluck  out’,
-----
KLN_1966.txt:4378:bane,  n.  —  OE.  bana,  ‘murderer,  slayer’,  rel.  to OE.  benn,  ‘wound’,  OS.  bano,  OFris.  bona. OHG.  bano,  ‘murderer’,  OHG.  bana,  ‘murder", ON.  bani,  ‘murderer,  murder,  death’,  ben. ‘wound’,  Dan.,  Swed.  bane,  ‘death,  murder’, Goth,  banja,  ‘stroke,  wound’,  and  cogn.  with Avestic  banta,  ‘ill’,  bqnayen,  ‘they  make  sick Derivatives:  bane-ful,  adj.,  bane-ful-ly,  adv., bane-ful-ness,  n.
KLN_1966.txt:5663:brinjarry,  also  binjarree,  n.,  a  dealer  in  grain  and salt  (Anglo-Ind.)  —  Hind,  banjara,  lit.  ‘one  who carries  on  trade’,  fr.  OI.  vanijya,  ‘trade,  traffic’ (fr.  van//',  ‘merchant’),  and  karah,  ‘doer’,  which is  rel.  to  kfnoti,  ‘he  does,  makes,  accomplishes’. See  Sanskrit  and  cp.  Chamar.  The  word  brinjarry was  influenced  in  form  by  Pers.  birinj,  ‘rice’.
```


## [2026-09-05T06:34:27.958Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^30[0-9] \\|^30[0-9]$\" SYN.txt | sed -n '1,40p'; echo \"-----\"; sed -n '7780,7800p' SYN.txt; echo \"----- 7815-7830\"; sed -n '7815,7830p' SYN.txt",
 "description": "Buck page context"
}
```


### [2026-09-05T06:34:29.646Z] TOOL RESULT

```
7694:300 4.83 WELL; HEALTH Grk. is} bylea Goth. hails ; Lith sveikas; sveikaig NG oe yepos; byela ON heill; hetlsa Lett. —_vesels, Sveiks; veseliba Lat. sdnus, etc.; sdnilas, Dan. ask, sund; helbred, ChSl. stidravit, célii; stidra. ete. sundhed vije It. sano; salute Sw. frisk, sund; hdlsa, SCr. _zdrav; zdravlje Fr. sain; santé sundhet Boh. zdravy; zdravs Sp. sano; salud (sanidad) OE hal, gesund; hal, Pol. zdrowy; zdrowie Rum.  sédndlos; sdndtate h@lu Russ. zdorovyj; zdoroy! rs Tr. slan; slantu ME hole (hale), (i)sunde; Skt. svastha-, kugalin-; Nir. _ slan, follain; slainte helthe kugala-, aroga-, W. tach; techyd NE well, healthy; health ete. Br. yac’h; yec’hed Du. gezond; gezondheid Av. drva-, abanta-; dryq- OHG heil, gisunti; heili, lat- gisunii MHG heil, gesunt; heil, ge- sunde NHG  gesund; gesundheit
7732:302 4.84 SICK; SICKNESS Grk.  da8evijs; vbcos, dodivaa Goth. stuks; siuket, sauhts | Lith.  sergas, nesveilas; Yj. NG = ppworos (aoderis); ON  sjttkr; sétl, sjikleiki 99, sirgimas apphoria (acdivea, (-démr) Lett. slims, nevesels; slim; véaos) Dan. syg; sygdom ba, neveseliba, liga Lat. ager; morbus Sw. sjuk; sjukdom ChSl.  boltnii; boléznt, nedq- It. malato; malattia OE séoc; suht, séocness, git, jedza Fy. malade; maladie ddl : SCr. _ bolestan; nemocan; Sp. enfermo; enfermidad ME stk(e), sek(e); sik- bolest, nemoé Rum. _ bolnav; boala ness, disese Boh. nemocnij; nemoc Ir. lobur; serg NE sick, ill; sickness, ill- Pol. — chory; choroba Nir. finn, breoidhte; tin- ness Russ. _bol’noj; bolezn' neas, aicid Du. ztek, krank; ziekte Skt. asvastha-, dlura-; vyd- W. claf; clefyd OHG _ sioh; stohi, suht dhi-, roga~ Br. klaniv; klerived MHG ssiech; suht(s), siech- Av. banta-, bazda; yaska- tuom (-heit. -lac) NHG_skrank; krankheit
7783:304
7835:306 SELECTED INDO-EUROPEAN SYNONYMS
7894:308 SELECTED INDO-EUROPEAN SYNONYMS
-----
SCr. nemocan, Boh. nemocny (ChSI. nemocinti for acberjs ‘weak’), neg. epds.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
i ee SS Digitized by Arya Samaj Foundation Chennai and eGangotri
304
of mocan, mocny ‘mighty, strong’ (as sbs. nemoé, nemoc fr. moé, moc ‘might’; ChSl. nemostt late for ‘sickness’, Jagié, op. cit. 327).
Pol. chory (Boh. chory, churavy, Russ. chvoryj ‘sickly’): Av. z*ara- ‘wound’, OHG sweran ‘pain, fester, swell’, OHG sb. swero ‘pain, sore, boil’ (NHG ge- schwiir), etc. Berneker 409. Briickner 183.
7. Skt. asvastha- (hence sb. asvdsthya- ‘sickness’), neg. cpd. of svastha- ‘well’ (4.84).
Skt. atura-, cpd. of prefix a- and tura- ‘hurt’ (RV) : Grk. zeipw ‘rub, exhaust’, Lat. terere ‘rub’, etc. Walde-P. 1.728 f.
Skt. vyadhi- ‘sickness’, lit. ‘displace-
SELECTED INDO-EUROPEAN SYNONYMS
ment’, cpd. of vi-a- and dha- ‘place, put) Uhlenbeck 299, ;
Skt. roga- ‘sickness’ (hence rogin- rogarta- ‘sick’), also ruj- ‘pain, sicknesg’ ; ruj- ‘break, cause pain’, Lat, liigére ‘mourn’, ete. Walde-P. 2.412. Walde. H. 1.830.
Av. banta-, pass. pple. of ban- ‘be sick’ in caus. banaya- ‘make sick’ (also bazda-, pass. pple. of band- id.) : Goth, banja, ON ben, etc. ‘wound’, OE bang ‘murderer’, OHG bano ‘death, mur- derer’. Walde-P. 2.149. Barth. 996,
Av. yaska- ‘sickness’, perh. for *yaks- ka- : Skt. yaksma- ‘an emaciating dis. ease, consumption’, further connection obscure. Walde-P. 1.10. Barth. 1269,
4.85 WOUND (sb.)
Grk. — rpadya, Akos, dredy Goth. banja Lith.  Zaitsda, rona
NG mAny7, AaBwparid ON sar, und, ben Lett. vals, ievainuojums Lat. vulnus Dan.  saar ChSl.  strupit, jazva, rana It. ferita Sw. sdr SCr.  rana
Fr. blessure, plate OE wund, ben Boh.  _rdna
Sp. herida ME wound Pol. rana
Rum. rand NE wound Russ. rana
Tr. crécht, cned Du. wond Skt. vrana-, ksata- NIr. goin, cneadh, créacht OHG wunta Ay. z*ara-
----- 7815-7830
145. ae a yulnus (earlier volnus), W. gueli, Br. gouli : Ir. furl ‘blood’, fudl bloody wounds’, Grk. otd7 ‘scar’, ON valr ‘corpses of the slain’, OHG wuol ‘defeat, pestilence’, OPruss. ulint ‘fight’, Hitt. walh- ‘strike, defeat, destroy’ (Sturtevant, Hitt. Gloss. 75 f.), Toch. A wal- ‘die’. All fr. a root *wel- (ultimate- ly the same as in Lat. vellere ‘pluck, tear out’, etc.?). Walde-P. 1.304 f. Er- nout-M, 1129,
It. ferita, Sp. herida, fr. It. ferire, Sp. CH ‘wound, hit’, fr. Lat. fertre ‘strike, eat’,
Fr, blessure, fr. vb. blesser ‘wound’, Olt. blecier ‘bruise, crush, injure, Wound’, fr. deriv. of a Frank. *bléa Uf eobleto in Lex Salica ‘running wound’?) : OHG bleizea gl. livor, OR blat ‘livid, bruise’ or “vound’ fr. its
115, Wartburg 1.406. um, Tana, fr. Slavic (below, 6). , crécht, NIr. créacht : W. crei- T. creizenn, NBr. kleizenn ‘scar’, ‘ ae NE scar fr. i ab’) : skra@ ‘dry piece Gs Li a ete, (Falk-Torp 1021), ir ae oe 13.28 f. rape, ar, : Ir. cneadh : Grk. xvite atch’, ON hrita ‘strike,
Digitized by Arya Samaj Foundation Chennai and eGangotri
7 THE BODY; BODILY FUNCTIONS AND CONDITIONS 305
wound to death’, OE hnitan ‘strike, thrust’, etc. Walde-P. 1.395.
NIr. goin : Ir. guin ‘a wounding’, vbl. n. of gonim ‘wound, kill’ (4.76),
W. archoll, prob. (with irregular mu- tation) epd. of ar- ‘fore-’ and coll ‘de- struction, loss’ : Goth. halts, OE healt, etc. ‘lame’ (4.94). Morris Jones 264.
W. gweli, Br. gouli, Corn. goly : Lat. vulnus, above, 2.
W. briw, Corn. brew, prob. fr. some form of the root seen in Ir. brium, OE . brysan ‘crush, bruise’. Pedersen 1.54 f. But cf. also Loth, RC 42.74 f.
Br. gloaz = W. gloes ‘pang, ache’, etym.?
4. Goth. banja (renders r\ny4 ‘blow, wound’ and @xos ‘sore’), ON, OE ben : ON bani ‘death’, OE bana, OHG bano ‘murderer’, Av. banta- ‘sick’ (4.841), etc., all prob. fr. a root *bhen- ‘strike’. Walde-P. 2.149. Feist 80.
ON sar, Dan. saar, Sw. sér = OE sar ‘pain, sore’, rarely ‘wound’ (ME, NE sore also sometimes ‘wound’, now only in dial.), Goth. sair, OHG, OS sér ‘pain’, ro-formation to a root *sai- in Ir. sdeth injury, trouble, sickness’, Lat. saevus ‘raging, fierce’. Walde-P. 2.445. Falk- Torp 941.
ON und, OE wund, etc., general Gmc. words (with adjs. Goth. wunds, OE, OHG, etc. wund ‘wounded’), prob. : W. gwanu ‘pierce, thrust, stab’, ym-wan ‘fight’, fr. IE *wen- beside *wa- in Grk. aren etc. (above, 1). Walde-P. 1.212. Falk-Torp 1399.
5. Lith. Zaisda perh.: Ir. goite ‘wounded’ (*ghoizd-), Skt. Aizis- ‘injure’, fr. IE *gheis-, extension of the root in Skt. hi- ‘set in motion, hurl’. Walde-P. 1.546.
```


## [2026-09-05T06:34:40.071Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=4360 && NR<=4380' KLN_1966.txt | grep -n \"^1[0-9][0-9]$\\|^ *14[0-9]\" ; echo \"--- page markers style:\"; grep -c \"\" KLN_1966.txt; sed -n '4370,4380p' KLN_1966.txt | cut -c1-200",
 "description": "Check Klein page markers"
}
```


## [2026-09-05T06:34:41.082Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"banja\\|bqnay\\|banta\" incoming/WLD/WLD_Bd2_pages.txt | head -10",
 "description": "grep Walde-Pokorny Bd2"
}
```


### [2026-09-05T06:34:41.607Z] TOOL RESULT

```
--- page markers style:
41263
bandog,  n.,  a  dog  kept  tied  up  as  a  watchdog  or because  of  its  ferocity;  a  mastiff  or  bloodhound. —  Contracted  fr.  band-dog  (see  band,  ‘a  tie’, and  dog).  For  sense  de
with  a  leash’,  fr.  Hem,  ancient  form  of  lien, ‘band’.
bandoleer,  also  bandolier,  n.,  a  shoulder  belt.  —
F.  bandouliere,  fr.  Sp.  bandolero,  fr.  banda, ‘scarf,  sash’,  which  is  a  Teut.  loan  word.  See
band,  ‘tie’.
Derivative:  bandoleer-ed,  bandolier-ed,  adj. bandore,  n.,  a  stringed  musical  instrument.  — Port,  bandurra,  fr.  L .pandura,  fr.  Gk.  rtavSoupa,
‘a  musical  instrument  of  three  strings’.  See  pan- dore  and  cp.  banjo.  Cp.  also  mandolin, bandy,  tr.  v.,  to  toss.  —  F.  bander,  ‘to  bind,  bend, bandy’,  of  Teut.  origi
bandy,  n.,  1)  a  form  of  hockey;  2)  the  bent  stick used  in  this  game.  —  F.  bande,  pp.  of  bander. See  prec.  and  cp.  next  word, bandy,  adj.,  bent,  crooked,  bandy-legged.  �
bane,  n.  —  OE.  bana,  ‘murderer,  slayer’,  rel.  to OE.  benn,  ‘wound’,  OS.  bano,  OFris.  bona. OHG.  bano,  ‘murderer’,  OHG.  bana,  ‘murder", ON.  bani,  ‘murderer,  murd
bang,  tr.  and  intr.  v.  —  Of.  Scand.  origin.  Cp. ON.  banga,  ‘to  hammer’,  Swed.  banga,  to  make a  noise’,  Icel.  banga,  Dan.  banke,  ‘to  beat’,  Cp also  Lith.  burigat, 
Derivative:  bang,  n.
```


### [2026-09-05T06:34:41.648Z] TOOL RESULT

```
8932:got. banja „Schlag,            Wunde, Geschwiir^^ usw. s. u. blien- „scblagen“).
9712:   Av. bqnayon „sie machen krank“, hanta- erkrankt, siech^^;
9713:   got. banja „Schlag, Wunde, Geschwur“, aisl. ags. ben, as. beni-ivunda
```


## [2026-09-05T06:34:49.825Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9700,9725p' incoming/WLD/WLD_Bd2_pages.txt; echo \"=== page tag:\"; awk 'NR<=9712 && /\\[pdf page [0-9]+\\]/ {p=$0} END{}' incoming/WLD/WLD_Bd2_pages.txt; awk 'NR<=9712 && /pdf page/ {p=NR\": \"$0} END{print p}' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "WLD bhen entry and page"
}
```


### [2026-09-05T06:34:51.492Z] TOOL RESULT

```
'^"^bheueg'^Qi)          (Hirt Abl. 135, Keichelt KZ. 39, 46) ist lautiich (Labiovelar in
letzterer      Gruppe?) wie in der Bed. scblecht gestiitzt, da letztere Gruppe
ursprgl. „biegen, daber ausbiegen,     sich in weitem Bogen um eine Gefahr
herumdrucken‘* bedeutet.

bheu- „sclilagen, verwunden“; auch von durch den Schlag boser Geister
    bewirkter Krankheit (avest. vgl. zu diesem Aberglauben Havers IF.
                                                             ;



        25, 380 f.;.
   Av. bqnayon „sie machen krank“, hanta- erkrankt, siech^^;
   got. banja „Schlag, Wunde, Geschwur“, aisl. ags. ben, as. beni-ivunda
„Wunde“ aisl. bani m. „Tod Morder^^, ags. bana, ahd. as. bano „Tot-
               ;                                         ;


schlager, M6rder‘‘, ahd. bajio, mhd. bane, ban „Tod, Yerderben“; vielleicht
auch mhd. bane, ban f. und m. „Bahn, Weg“ als *, ,Durchhau durch einen
Wald“ Oder %,festgeschlagener Weg'' (s. Kluge® und Weigand-Hirt s. v.).
Bthl. Airan. Wb. 925 f., Havers aaO. 382 A. 3.
   Nicht vrahrscheinlicher halt Zup. G. 30 f. (auch Berneker 117) germ.
fiir Ablautneubildung (zunachst im Praet.) zu einem Praes. "^bino aus idg.

          (: lat. perfinare, ir. benim) von der Wz. bhei- „schlagen“; wieder
=== page tag:
```


## [2026-09-05T06:34:57.435Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"pdf page\" incoming/WLD/WLD_Bd2_pages.txt; grep -n \"pdf page\" incoming/WLD/WLD_Bd2_pages.txt | head -3; echo \"---- nearest page number lines\"; awk 'NR>=9640 && NR<=9712 && /^ *1[0-9][0-9] *$/ {print NR\": \"$0}' incoming/WLD/WLD_Bd2_pages.txt | tail -5",
 "description": "check WLD page tags"
}
```


### [2026-09-05T06:34:58.911Z] TOOL RESULT

```
0
---- nearest page number lines
```


## [2026-09-05T06:35:06.408Z] TOOL CALL #24: Bash

```json
{
 "command": "pdftoppm -f 86 -l 86 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg86\" && ls -la \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/\"",
 "description": "Render PDF page 86"
}
```


### [2026-09-05T06:35:08.227Z] TOOL RESULT

```
total 29040
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 02:35 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb    78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52793 Sep  5 02:18 mk79.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57729 Sep  5 02:31 mk81.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
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
```


## [2026-09-05T06:35:09.244Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC bhen\"; grep -n \"bhen-\\|banja\" IEC.txt | head -10; echo \"=== ARY autoban\"; grep -n \"اتوبان\" incoming/ARY/ARY_pages.txt MON_part1.txt MON_part2.txt BQT_v1_pages.txt 2>/dev/null | head -10; echo \"=== otoban latin\"; grep -n -i \"autobahn\\|otoban\" incoming/ARY/ARY_latin_index_pages.txt incoming/VIE/VIE_pages.txt 2>/dev/null | head",
 "description": "grep Mann, Aryanpur, Moin for autobahn"
}
```


### [2026-09-05T06:35:09.333Z] TOOL RESULT

```
=== IEC bhen
18371:ten, ið (1) stretch, pull, extend’. Cf. tento, tentos, tenmn-, tenso, etc. WP I, 723 Skt. tanómi, v. id.; Av. tan-, v. id. (and 'lead"); tanyo, adj. ‘extended’; Per. tanide, s. (‘spin- ning’, fr. *tenità); Gk. teíno, v. “extend; tight- en'; ténos, gs: -eos, n. “stretched material, band”; ténón, -ontos, m. ‘tendon, sinew’; cf. tén-agos (“shallow waters”, cf. pél-agos ‘pleine mer); Alb. teje, tojë, f. (cord, thong, band, garter, ligament, fr. *tenio, *tenjo); ndej, v. tr. Cstretch', fr. *en-tenjo); Lat. cf. tenus, gs: tenoris, n. ‘snare’; Cor. cf. ten, pl. tennow, m. “pull, draw’ beside tenna, v., pp: tennys, v. id. (fr. *tend- or *tent-, but cf. tenmn- for the noun); Br. tenn, pl. -u, m. (“pulP, etc., see tenmn- above); ON cf. pinull, m. “guy- rope of net; pin-urr, m. (2) bow'; OCS tenüta, f. tent’, perh. hybridized w. Lat. tentorium); Cz. cf. teneto, pl: tenata, m. ‘fowling- or hunt- ing-net'; (o-gde in) Go. uf-banjan, OS then- jan, Sw. tänja, v. ('stretch', fr. *toneið); (z- gde in) OE bunian, v. (1) “stand out, stand erect, stiffen o's' (fr. *tnio) (but see (2))
=== ARY autoban
=== otoban latin
```


## [2026-09-05T06:35:12.195Z] TOOL CALL #26: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg86.png"
}
```


### [2026-09-05T06:35:12.631Z] TOOL RESULT

```

```


## [2026-09-05T06:35:12.629Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T06:35:24.093Z] TOOL CALL #27: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','SYN','POK','AHD','WLD','BRT','MON','ARY','IEC']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Check refs_online entries"
}
```


## [2026-09-05T06:35:24.388Z] TOOL CALL #28: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T06:35:25.727Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open
```


### [2026-09-05T06:35:25.736Z] TOOL RESULT

```


```


## [2026-09-05T06:35:29.056Z] TOOL CALL #29: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\n\"",
 "description": "KLN ref details"
}
```


### [2026-09-05T06:35:30.676Z] TOOL RESULT

```
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
```


## [2026-09-05T06:35:34.285Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=4378{n+=gsub(/\\f/,\"\")} END{print \"leaf index (0-based) =\", n}' KLN_1966.txt",
 "description": "Compute leaf for Klein bane"
}
```


### [2026-09-05T06:35:35.933Z] TOOL RESULT

```
leaf index (0-based) = 88
```


## [2026-09-05T06:35:42.913Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==89' KLN_1966.txt | head -6 | cut -c1-300; echo \"=== leaf 85 (0-based 84):\"; awk 'BEGIN{RS=\"\\f\"} NR==85' KLN_1966.txt | head -4 | cut -c1-200",
 "description": "Inspect Klein leaves"
}
```


### [2026-09-05T06:35:45.361Z] TOOL RESULT

```
e  banner  and cp.  prec.  word.
bandhava,  n.,  a  kinsman  (Hindu  law).  —  OI. bdndhavah,  rel.  to  bandhuh  ‘relationship,  kins¬ man’.  See  next  word.
bandhu,  n.,  related  through  females.  —  OI.  bdn¬ dh  uh,  ‘relationship,  kinsman’,  rel.  to  bandhdh,  ‘  a binding;  band,  tie’,  fr.  I.-E.  base  *bendh-,  ‘to bind'.  See  band,  ‘tie’.
bandicoot,  n.,  a  kind  of  a  large  rat.  —  Telegu pandi  kokku,  lit.  ‘pig  rat’, bandit,  n.  —  F.,  fr.  It.  bandito,  prop.  pp.  of  ban- dire,  ‘to  banish’,  which  arose  from  a  blend  of Frankish  *bannjan ,  ‘to  banish’  (whence  F.  ban- nir,  E.  banish),  and 
banditi,  n.  pi.,  sometimes  used  as  sing.,  bandits; bandits  collectively.  —  It.,  pi.  of  bandito.  See prec.  word.
bandog,  n.,  a  dog  kept  tied  up  as  a  watchdog  or because  of  its  ferocity;  a  mastiff  or  bloodhound. —  Contracted  fr.  band-dog  (see  band,  ‘a  tie’, and  dog).  For  sense  development  cp.  F.  limier, ‘bloodhound;  sleuthhound’,  lit.  ‘a  dog  held
=== leaf 85 (0-based 84):
zorite  (q.v.),  azot-ize , tr.  v.
azote,  n.,  a  whip.  —  Sp.,  fr.  Arab,  as-saut,  lit., ‘the  whip’,  fr.  as-,  assimilated  form  of  al-,  ‘the’, and  saut,  ‘whip’,  which  is  rel.  to  Heb.  shot, Aram,  shot
azotea,  n.,  a  flat  roof.  —  Sp.,  fr.  Arab,  as-sath, lit.  ‘the  roof’,  fr.  as-,  assimilated  form  of  a!-, ‘the’,  and  sath,  ‘roof’,  fr.  sataha,  ‘he  spread  out’,
|
```


## [2026-09-05T06:35:58.486Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 84 85 86 87 88 89 90; do echo \"--- leaf(1-based) $n:\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' KLN_1966.txt | grep -oE \"\\b1[0-9][0-9]\\b\" | head -6 | tr '\\n' ' '; echo; done",
 "description": "Look for printed page numbers in Klein leaves"
}
```


### [2026-09-05T06:36:00.053Z] TOOL RESULT

```
--- leaf(1-based) 84:
135 136 137 
--- leaf(1-based) 85:

--- leaf(1-based) 86:
140 141 134 137 
--- leaf(1-based) 87:
142 143 
--- leaf(1-based) 88:
144 145 176 
--- leaf(1-based) 89:
146 
--- leaf(1-based) 90:
148 149
```


## [2026-09-05T06:36:08.464Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==88' KLN_1966.txt | grep -nE \"^[a-z]\" | head -3; echo \"...tail:\"; awk 'BEGIN{RS=\"\\f\"} NR==88' KLN_1966.txt | grep -nE \"^[a-z]\" | tail -3; echo \"=== leaf 89 head/tail\"; awk 'BEGIN{RS=\"\\f\"} NR==89' KLN_1966.txt | grep -nE \"^[a-z]\" | head -3; awk 'BEGIN{RS=\"\\f\"} NR==89' KLN_1966.txt | grep -nE \"^[a-z]\" | tail -3; echo \"=== where is 145 and 146 in leaf88/89\"; awk 'BEGIN{RS=\"\\f\"} NR==88' KLN_1966.txt | grep -n \"145\" | cut -c1-150",
 "description": "Klein leaf boundaries"
}
```


### [2026-09-05T06:36:10.064Z] TOOL RESULT

```
2:balladry,  n.,  ballad  poetry.  —  Formed  fr.  ballad with  suff.  -ry.
3:ballast,  n.,  heavy  material  used  to  steady  a  ship. —  Dan.  and  Swed.,  assimilated  fr.  earlier  bar- last  lit.  ‘bare  load’.  The  first  element  of  this
4:compound  is  rel.  to  the  E.  adjective  bare;  the second  is  rel.  to  last,  a  unit  of  weight. Derivatives:  ballast-er,  n.,  ballast-ing,  n. ballerina,  a  woman  ballet  dancer.  —  It.,  fr.  bal¬ lare,  ‘to  dance’.  See  ball,  ‘party  for  dancing’, ballet,  n.  —  F.,  fr.  It.  balletto ,  dimin.  of  ballo, ‘dance’.  See  ball  ‘party  for  dancing’,  and  -et. Derivative:  ballet,  tr.  v.
...tail:
36:bandage,  n.  —  F„  fr.  bande,  fr.  OF.  bende,  fr. ML.  benda,  ‘a  band’,  fr.  Goth.  *binda,  which  is rel.  to  E.  band,  ‘tie’  (q.v.)  For  the  ending  see suff.  -age.
38:bandanna,  bandana,  n.,  a  colored  and  spotted handkerchief.  —  Hind,  bandhnu,  ‘a  mode  of dyeing  in  which  the  cloth  is  tied  in  various places  to  prevent  these  places  from  receiving the  dye’,  rel.  to  bandhdh,  ‘a  tying,  fastening; band,  bandage’.  See  bind  and  cp.  band,  ‘tie’. Cp.  also  bandhu,  pandal. bandeau,  n.,  a  narrow  band,  fillet.  —  F.,  fr.  earlier bandel,  dimin.  of  bande,  ‘band,  ribbon’,  of  Teut. origin.  See  band,  ‘tie’.
39:banderilla,  n.,  a  small  dart  with  a  streamer  thrust into  the  bull  by  the  banderillo.  —  Sp.,  dimin.  of bandera,  ‘banner’.  See  banner  and  cp.  next  word, banderole,  banderol,  n.,  a  small  streamer  at¬ tached  to  a  lance.  —  F.  banderole,  dimin.  of bandore,  banniere,  ‘banner’.  Se
=== leaf 89 head/tail
1:e  banner  and cp.  prec.  word.
2:bandhava,  n.,  a  kinsman  (Hindu  law).  —  OI. bdndhavah,  rel.  to  bandhuh  ‘relationship,  kins¬ man’.  See  next  word.
3:bandhu,  n.,  related  through  females.  —  OI.  bdn¬ dh  uh,  ‘relationship,  kinsman’,  rel.  to  bandhdh,  ‘  a binding;  band,  tie’,  fr.  I.-E.  base  *bendh-,  ‘to bind'.  See  band,  ‘tie’.
50:baptism,  n.  —  ME.  bapteme,  fr.  OE.  baptesme (F.  bapteme),  fr.  Eccles.  L.  baptisma,  fr.  Gk. Pa7tTicrpa,  ‘a  dipping  in  water’,  in  Eccles.  Gk. ‘baptism’,  fr.  paTrriCetv,  ‘to  dip’,  in  Eccles.  Gk. ‘to  baptize’,  fr.  pdbrmv,  ‘to  dip,  steep,  dye, color’,  which  is  rel.  to  (3a<pf),  ‘a  dyeing’,  and cogn.  with  ON.  kvefja,  ‘to  plunge’,  OSwed.  kvaf, ‘a  deep  place’.  For  sense  development  it  should be  borne  in  mind  that  baptism  orig.  consisted in  immersion.  E.  baptism  has  been  refashioned after  Eccles.  L.  baptisma,  Gk.  piimopia.  For the  ending  see  suff.  -ism.  Cp.  Baphia,  Baptisia, baptist,  baptistery,  baptize  and  the  second  ele¬ ment  in  phlobaphene.
52:baptism  and  -ist.
53:baptistery,  baptistry,  n.  —  OF.  baptisterie  (F.  bap- tistire),  fr.  Eccles.  L.  baptisterium,  fr.  Gk.  pctrt- Tiafripiov,  ‘bathing  place’,  in  Eccles.  Gk.,  bap¬ tistery'.  See  baptist  and  -ery,  resp.  -ry. baptize,  tr.  and  intr.  v.  —  ME.  baptisen,  fr.  F. baptiser,  fr.  Eccles.  L.  baptizare,  ‘to  baptize’,  fr. Gk.  parrrifeiv.  See  baptism  and  -ize. bar,  rod  of  metal  or  wood.  —  ME.  barrc,  fr.  OF. (=  F.)  barre,  fr.  VL.  *barra,  a  word  of  Gaulish origin.  See  forum  and  cp.  barrier,  barrister,  bar- rulet,  debar,  disbar,  embargo,  embarrass, bar,  tr.  v.  —  ME.  barren,  fr.  OF.  barrer,  fr.  barre. See  prec.  word  and  cp.  barrage.
=== where is 145 and 146 in leaf88/89
24:145
```


## [2026-09-05T06:36:25.570Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Bahn",
 "prompt": "Give the full German etymology section for Bahn: Middle High German bane/ban, Old High German forms, the reconstructed Proto-Germanic and PIE root, and whether the connection to a root meaning \"to strike\" (\"path hewn through woods\") is stated or doubted."
}
```


## [2026-09-05T06:36:26.883Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/ban%C3%B4",
 "prompt": "Give the full entry: meaning of Proto-Germanic *banô, its PIE root, descendants (Gothic banja, Old English bana, Old High German bano, Old Norse bani), and any related *banō entries."
}
```


### [2026-09-05T06:36:31.226Z] TOOL RESULT

```
# German Etymology of Bahn

Based on the Wiktionary entry, here is the etymological path:

**Middle High German:** _ban_

**Old High German:** _*bana_ (reconstructed form)

**Proto-West Germanic:** _*banu_ (reconstructed form)

**Proto-Germanic:** _*banō_ (reconstructed form)

The entry traces the word through these historical language stages but does not explicitly discuss or reference any connection to a root meaning "to strike" or the interpretation of "path hewn through woods." The etymology section provided focuses on the phonetic evolution across language families without addressing semantic theories about the word's original meaning.

The article does note cognates in related languages, including Luxembourgish _Bunn_ and Dutch _baan_, demonstrating the word's distribution across Germanic languages.
```


### [2026-09-05T06:36:33.770Z] TOOL RESULT

```
# Proto-Germanic *banô

## Meaning
The term denotes "murderer, killer, slayer" or alternatively "bane, death."

## PIE Root
The word likely derives from Proto-Indo-European *gʷʰon-ō, described as "an individualizing n-stem derivative" of *gʷʰonós (one who strikes down), ultimately from the root *gʷʰen- meaning "to strike, kill." The sound change from *gʷʰ to *b in word-initial position is considered controversial but apparently regular.

## Descendants
The entry documents a rich descendant chain:
- **Old English**: bana, bona → Modern English *bane*
- **Old Frisian**: bona
- **Old Saxon**: bano → Middle Low German bāne
- **Old High German**: bano → Middle High German forms
- **Old Norse**: bani → Icelandic, Faroese, Swedish, Danish, Norwegian variants

## Related Terms
The entry cross-references *banjō, *banō, and *gunþiz as related terms, though the specific Gothic *banja you mentioned doesn't appear in this particular entry's descendants list.
```


## [2026-09-05T06:36:42.080Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/ban%C5%8D",
 "prompt": "Full entry for Proto-Germanic *banō: meaning, etymology (which PIE root, any note about \"path hewn/struck through a forest\"), and descendants (Old High German, Middle High German, German Bahn, Dutch baan)."
}
```


## [2026-09-05T06:36:42.829Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/autobahn",
 "prompt": "Give the English etymology of autobahn: from German Autobahn, its components Auto + Bahn, and the date of borrowing into English."
}
```


### [2026-09-05T06:36:48.532Z] TOOL RESULT

```
# Proto-Germanic *banō

**Meaning:** This reconstructed noun denotes "battlefield," "clearing," "open space," "cleared way," "path," or "track."

**Etymology:** Scholars trace *banō* to Proto-Indo-European *gʷʰon-eh₂, derived from the root *gʷʰen- meaning "to strike, kill." However, the entry notes that "This etymology is missing or incomplete," requesting additional sources and noting skepticism from certain scholars.

**Descendants include:**

- **German:** *Bahn* (from Middle High German *bane*)
- **Dutch:** *baan* (through Old Dutch and Middle Dutch)
- **Frisian varieties:** West Frisian *baan*, Saterland Frisian *Boan*
- **Scandinavian:** Norwegian and Swedish *bane/bana* (from Middle Low German)
- **Other Germanic languages:** Luxembourgish *Bunn*, Yiddish *ban*, Afrikaans *baan*

The word also influenced non-Germanic languages like Finnish *baana* and Indonesian *ban* through borrowing.
```


### [2026-09-05T06:36:48.637Z] TOOL RESULT

```
# English Etymology of Autobahn

**Origin:** The word "autobahn" was "Borrowed from German _Autobahn_" according to Wiktionary.

**Components:** The German term combines:
- **Auto** (from "Automobil," meaning automobile)
- **Bahn** (meaning path or track, derived from Proto-Germanic *banō)

**Date of Borrowing:** The Wiktionary article does not specify when this term entered English usage.
```


## [2026-09-05T06:36:52.880Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%AA%D9%88%D8%A8%D8%A7%D9%86",
 "prompt": "Give the Persian entry for اتوبان: transliteration, meaning, and etymology (which language it was borrowed from — German Autobahn or French)."
}
```


## [2026-09-05T06:36:54.144Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/autobahn",
 "prompt": "Give the etymology of autobahn as stated: German source, date of first English use, and the etymology of Bahn (Old High German bahn, \"path hewn through\", PIE root)."
}
```


### [2026-09-05T06:36:55.881Z] TOOL RESULT

```
# Persian Entry: اتوبان

**Transliteration:** otobân

**Meaning:** "motorway" or "freeway"

**Etymology:** The word was "Borrowed from German _Autobahn_." It is not borrowed from French.
```


### [2026-09-05T06:36:59.208Z] TOOL RESULT

```
# Etymology of Autobahn

**German Source & Date of First English Use:**
The word entered English in 1937 from German *Autobahn* (1930s). It combines *auto* (automobile) with *bahn* (path, road).

**Etymology of Bahn:**
According to the source, *bahn* derives from Middle High German *ban*, *bane* meaning "way, road," with a literal sense of "strike" (as in "a swath cut through"). This traces back to the Proto-Indo-European root *\*gwhen-*, which means "to strike, kill."

**Summary:**
The term is a compound of two German elements: *auto* (motor car) and *bahn* (road), where *bahn* itself originates from an ancient root denoting the striking or cutting action that creates a path.
```


## [2026-09-05T06:37:05.995Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-",
 "prompt": "Full entry for PIE *gʷʰen-: meaning, derived terms and descendants; does it list Avestan banta-/ban- 'sick', Proto-Germanic *banô/*banō, and does it mention a competing root *bʰen-?"
}
```


## [2026-09-05T06:37:07.544Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%90%AC%A5%F0%90%AC%8C%F0%90%AC%99%F0%90%AC%8C",
 "prompt": "Is there an Avestan entry for banta- (sick)? If the page does not exist, say so."
}
```


### [2026-09-05T06:37:09.343Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T06:37:11.277Z] TOOL RESULT

```
# Analysis of PIE *gʷʰen- Entry

**Avestan banta-/ban-:** Not listed. The entry shows Avestan forms like "nijaγnəṇte" and "auuajaγnat̰" derived from the reduplicated aorist, but no Avestan banta-/ban- entry appears.

**Proto-Germanic *banô/*banō:** Yes, both are mentioned. The entry states: *gʷʰón-ō derives to "Proto-Germanic: *banô ("murderer")" and *gʷʰon-éh₂ derives to "Proto-Germanic: *banō ("cleared path; battlefield")."

**Competing root *bʰen-:** No mention. The entry lists synonymous roots (*bʰerH-, *bʰeyh₂-, *dʰebʰ-) but does not reference a competing *bʰen- root for similar meanings.
```


## [2026-09-05T06:37:17.142Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/bane",
 "prompt": "Give the etymology of bane: Old English bana, Proto-Germanic *banon, the PIE root cited, and whether Avestan banta- 'sick' or banaya- is mentioned."
}
```


### [2026-09-05T06:37:22.324Z] TOOL RESULT

```
# Etymology of Bane

**Old English Origin:** The word comes from "bana" meaning "killer, slayer, murderer, a worker of death."

**Proto-Germanic Root:** It derives from Proto-Germanic *banon, which is cognate with *banja- meaning "wound."

**PIE Root:** The entry states the word has "no certain IE etymology," though related words suggest a connection to Indo-European *gwhen- meaning "to strike, kill."

**Avestan Connection:** The document does not mention Avestan banta- or banaya-. However, it does reference Persian and Old Iranian origins in the related entry for "bezoar," which traces back to PIE *gwhen- "to strike, kill," the same root associated with bane's cognates.

The primary semantic evolution moved from literal killing/death to "that which causes ruin or woe," attested from the 1570s.
```


## [2026-09-05T06:37:28.278Z] TOOL CALL #43: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Bahn' --note 'page 86, root Bhen, node 4/5: German Bahn < MHG bane/ban < PGmc *banō' 2>&1 | tail -3 && python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/ban%C3%B4' --note 'page 86, root Bhen, node 3: PGmc *banô \"slayer\" < PIE *gʷʰen-' 2>&1 | tail -3 && python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/ban%C5%8D' --note 'page 86, root Bhen, node 4: PGmc *banō \"cleared path, battlefield\" > MHG bane > German Bahn' 2>&1 | tail -3 && python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/autobahn' --note 'page 86, node 7: English autobahn < German Autobahn' 2>&1 | tail -3",
 "description": "Archive web sources part 1"
}
```


### [2026-09-05T06:37:31.369Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/162df6b2cabd51b9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1a591d8c2210403f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/545b9ac492430ccb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/243799bc2f97f54a.txt
```


## [2026-09-05T06:37:38.537Z] TOOL CALL #44: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A7%D8%AA%D9%88%D8%A8%D8%A7%D9%86' --note 'page 86, node 6: Persian اتوبان otobân borrowed from German Autobahn' 2>&1 | tail -2 && python3 tools/fetch_source.py 'https://www.etymonline.com/word/autobahn' --note 'page 86, nodes 5-7: autobahn 1937 from German, Bahn < MHG ban \"way\", PIE *gwhen-' 2>&1 | tail -2 && python3 tools/fetch_source.py 'https://www.etymonline.com/word/bane' --note 'page 86, node 3: bane < OE bana < PGmc *banon, IE etymology uncertain / *gwhen-' 2>&1 | tail -2 && python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-' --note 'page 86, root Bhen: modern Wiktionary assigns *banô/*banō to *gʷʰen-, not *bʰen-' 2>&1 | tail -2",
 "description": "Archive web sources part 2"
}
```


### [2026-09-05T06:37:41.760Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b55bf8de5026ddd2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/67c0d83a8387afcf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a3ac5b520392c030.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8f4a4c4d0f4d87ee.txt
```


## [2026-09-05T06:37:57.885Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT bane\"; grep -n \"^bane\\|BANE\" SKT.txt | head -5; echo \"=== Bahn in KLN/WEB/FSD\"; grep -n -i \"autobahn\\|Bahn,\" KLN_1966.txt KLN_1971.txt WEB_vol1.txt FSD_vol1.txt SKT.txt 2>/dev/null | head -10; echo \"=== ARY variants\"; grep -n \"اتوبا\\|اتوب\" incoming/ARY/ARY_pages.txt MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10",
 "description": "More local greps"
}
```


### [2026-09-05T06:37:57.997Z] TOOL RESULT

```
=== SKT bane
=== Bahn in KLN/WEB/FSD
SKT.txt:1351:tike  football. -O.  F.  bahn,  *k  little  ball, or  pack :  a.  football  or  baloon : '  Cot Mod.  K.  batloH  :  Span,  halon  \  Ital.  pal- lout  \  aagmentative  form  of  F.  balU,  &c^ a  ball.
WEB_vol1.txt:13717:Au’tō- bähn, 7.; pl. Au/td-bahn-en, Au’t6- bahns, [G.; auto (contr. of automobil, auto- mobile) and bahn, a course, highway.] in Germany, a four-lane highway for fast driv- ing, with a strip of grass, etc. down the middle to separate traffic bound in opposite direc- ions.
=== ARY variants
incoming/MON/MON_2vol_Adena_v2_djvu.txt:20683:اتوبوس و غیره): (نو.) (عم. ) مانند کتاب (در 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:67717:تولید نیرو کند. موتور اتومبیل (اتوبوس): 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:67719:اتومبیل (اتوبوس) به حرکت درمی‌آید. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:78798:گاری اتوبوس و غیره. بارکش (فره.) نقلیة 
MON_part1.txt:6968:اتوبوس: ۵۱0-۳5 (.) نوعی از اتومسل با 
MON_part1.txt:6971:کسان بکار می‌رود. اتوبوس دو طبقه: 
MON_part1.txt:6975:اتوبوس شهری: اتوبوسی که در شهر رفت و 
MON_part1.txt:6983:بجایی. شغل آنکه اتوبوس می‌راند. شرکت 
MON_part1.txt:6985:اتوبوس‌رانی از جایی بجایی را به عهده 
MON_part1.txt:19250:توقف وسایط نقلیه (اتومبیل» اتوبوس
```


## [2026-09-05T06:38:06.464Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%AA%D9%88%D8%A8%D8%A7%D9%86/",
 "prompt": "What do the Persian dictionaries (فرهنگ فارسی معین، لغت‌نامه دهخدا، فرهنگ عمید) say for اتوبان — definition and stated origin/language tag (e.g. [آلمانی] / [فر.])?"
}
```


### [2026-09-05T06:38:14.499Z] TOOL RESULT

```
Based on the webpage content, here's what the Persian dictionaries state about اتوبان:

**Farhang-e Faarsi (Moein):**
The entry shows: "(اُ ) [ آلما. ] جادة پهن ماشین رو دو طرفه ، آزادراه ، بزرگ راه"

This indicates the word originates from German ([آلما] = Almani/German) and defines it as "a wide two-way motorway for vehicles; freeway; highway."

**Loghат-naameh Dehkhoda & Farhang-e Omid:**
These dictionaries are mentioned in the page's general description of Abadis' content, but specific entries for اتوبان from these sources are not separately detailed in the provided excerpt.

The page emphasizes that اتوبان entered Persian from a German automobile (a Mercedes-Benz 500K gifted to Reza Shah in 1934), establishing its modern usage for intercity highways and expressways in contemporary Persian.
```


## [2026-09-05T06:38:23.084Z] TOOL CALL #47: Bash

```json
{
 "command": "python3 /home/sfmqrb/git/rishe/tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%A7%D8%AA%D9%88%D8%A8%D8%A7%D9%86/' --note 'page 86, node 6: Mo^in via abadis tags اتوبان as [آلما.] German, \"آزادراه، بزرگ‌راه\"' 2>&1 | tail -2; mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg86.png\" /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/86.png && echo copied",
 "description": "Archive abadis and copy page image"
}
```


## [2026-09-05T06:38:23.739Z] TOOL CALL #48: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T06:38:26.140Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5665803247c98df2.txt
copied
```


### [2026-09-05T06:38:26.185Z] TOOL RESULT

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


## [2026-09-05T06:38:28.802Z] TOOL CALL #49: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Rest of verify_check.py"
}
```


### [2026-09-05T06:38:28.836Z] TOOL RESULT

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


## [2026-09-05T06:44:06.469Z] TOOL CALL #50: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk86.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 86,\n \"book_page\": 56,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Bhen\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"PIE *bʰen- 'to strike, wound' (Pokorny 126) — today generally merged into *gʷʰen- 'to strike, kill'\",\n   \"note\": (\"Pokorny IEW p. 126 really has 'bhen- ‚schlagen, verwunden‘; auch von durch den Schlag böser \"\n     \"Geister bewirkter Krankheit (avest.)', with exactly the two branches Nourai draws: Av. bǎanayən / banta- and \"\n     \"Gothic banja, ON bani, OE bana, OHG bano, plus 'vielleicht auch mhd. bane, ban ... ‚Bahn, Weg‘ als \"\n     \"‚*Durchhau durch einen Wald‘'. So the language label ('Indo-European'), the shape of the root and the gloss \"\n     \"'to strike' are Pokorny's own. What has changed since 1959: Watkins (AHD app.) files the whole Germanic family under \"\n     \"gʷhen-¹ 'to strike, kill' (bracket: '[Pok. 2. gʷhen-(2)- 491, bhen- 126]'), and Wiktionary/Kroonen derive \"\n     \"PGmc *banô 'slayer' from *gʷʰon-ō, *banō 'cleared path' from *gʷʰon-eh₂, since word-initial \"\n     \"*gʷʰ- regularly gives Germanic b-. Under that analysis a separate *bʰen- is not needed, and Etymonline \"\n     \"says bane has 'no certain IE etymology'. The root box is therefore correct as Pokorny, but superseded.\"),\n   \"note_fa\": (\"«Bhen» ریشه‌ای است که پوکورنی در صفحهٔ ۱۲۶ فرهنگ ریشه‌شناسی هندواروپایی خود با معنای \"\n     \"«زدن، زخم کردن» آورده است؛ گواه‌های آن تنها اوستایی (ban- «بیمار شدن») و ژرمنی \"\n     \"(گوتی banja «زخم، ضربه») است، و پوکورنی خود معنای «بیماری» را به باور کهن ایرانی دربارهٔ \"\n     \"«ضربهٔ دیوان» بازمی‌گرداند. ریشه‌شناسی امروزی (واتکینز در پیوست AHD، ویکی‌واژه، کرونن) \"\n     \"مواد ژرمنی را ذیل ریشهٔ *gʷʰen- «زدن، کشتن» می‌نهد، زیرا *gʷʰ- آغازین در ژرمنی به b بدل می‌شود؛ \"\n     \"بدین‌سان به ریشهٔ جداگانهٔ *bʰen- نیازی نیست. پس عنوان و معنای ریشه با پوکورنی می‌خواند، \"\n     \"اما پژوهش امروزی آن را در ریشه‌ای دیگر ادغام کرده است؛ ادعای نورایی با احتیاط پذیرفتنی است.\"),\n   \"sources\": [\n     W + \"Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-\",\n     \"https://www.etymonline.com/word/bane\"\n   ],\n   \"ref_check\": [\n     {\"ref\": \"POK:126\", \"status\": \"supports\",\n      \"note\": (\"POK_01.txt line 1774 (leaf = p+8, the '126' page marker stands a few lines above): 'bhen- ‚schlagen, \"\n        \"verwunden‘; auch von durch den Schlag böser Geister bewirkter Krankheit (avest.) ... Av. bqnayan ‚sie machen \"\n        \"krank‘, banta- ‚erkrankt, siech‘; got. banja ‚Schlag, Wunde, Geschwür‘ ... vielleicht auch mhd. bane, ban \"\n        \"... ‚Bahn, Weg‘ ... WP. II 149'. Root, language and gloss are exactly Nourai's.\")}\n   ],\n   \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"IEW p. 126 (POK_01.txt:1774)\", \"stance\": \"supports\",\n      \"note\": \"'bhen- ‚schlagen, verwunden‘' with the Avestan, Germanic and MHG material of the whole chart.\"},\n     {\"src\": \"WLD\", \"where\": \"Bd. II p. 149 (WLD_Bd2_pages.txt:9706-9716, OCR reads the lemma as 'bheu-')\", \"stance\": \"supports\",\n      \"note\": \"Same article as Pokorny's, Walde-Pokorny's own wording: 'Av. bqnayon ‚sie machen krank‘ ... got. banja ... vielleicht auch mhd. bane, ban ... ‚Durchhau durch einen Wald‘ (s. Kluge und Weigand-Hirt s. v.). Bthl. Airan. Wb. 925 f.'\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. gʷhen-¹ (AHD_watkins1985.txt:545)\", \"stance\": \"partial\",\n      \"note\": \"'gʷhen-¹. To strike, kill. 1. O-grade *gʷhon- in Germanic suffixed form *ban-ōn- in: a. Old English bana ... BANE; b. Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN ... [Pok. 2. gʷhen-(2)- 491, bhen- 126.]' — same material, but filed under gʷhen-, with Pokorny's bhen- 126 only cross-referenced.\"},\n     {\"src\": \"SYN\", \"where\": \"Buck p. 304-305, §4.85 WOUND\", \"stance\": \"supports\",\n      \"note\": \"'Goth. banja ... ON bani ‚death‘, OE bana, OHG bano ‚murderer‘, Av. banta- ‚sick‘ (4.841), etc., all prob. fr. a root *bhen- ‚strike‘. Walde-P. 2.149. Feist 80.'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"ban; banta; banay\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"All three forms are genuine Younger-Avestan: Bartholomae lemmatises 'j., g. ban- V. ‚kranken‘. Praes. 30 \"\n       \"(Kaus.) bǎanaya-. — PPfP. banta-', i.e. a root ban- 'be sick' whose only attested finite form is the causative \"\n       \"3pl. bǎanayən 'they make sick' (Y. 30.6) and whose past participle banta- 'erkrankt, siech' appears in Vd. 22.5 \"\n       \"and Yt. 13.24; the negated a-banta- 'healthy' is Buck's 4.83 entry. Nourai's 'banay' is that causative stem bǎanaya-, \"\n       \"so the three glosses ('to be sick', 'sick', 'to make sick') are exact. The semantic bridge to a root 'strike' is \"\n       \"Pokorny's: sickness is conceived as a blow struck by evil spirits (he cites Havers IF 25, 380f.), and Bartholomae \"\n       \"himself ends the entry 'Vgl. got. banja ‚Wunde‘, ahd. bana ‚Verderben‘'. The reservation: Avestan reflects PIE \"\n       \"*gʷʰen- as jan- / ɣn- (jaini, avən), never as b-, so if the Germanic words are from *gʷʰen- (Watkins, \"\n       \"Wiktionary, Kroonen) then Av. ban- can no longer be their cognate and stands alone. The node is right in Pokorny's \"\n       \"framework, unsupported in the current one.\"),\n     \"derivation_fa\": (\"هر سه صورت اوستایی است: بارتولومه (ستون ۹۲۵ و پس از آن) ریشهٔ ban- «بیمار شدن» را \"\n       \"با ستاک سببی bǎanaya- «بیمار کردن» (صیغهٔ bǎanayən در یسنا ۳۰، بند ۶) و صفت مفعولی banta- \"\n       \"«بیمار، رنجور» ثبت کرده است؛ پس «banay» چارت همان ستاک سببی است و هر سه معنا درست است. \"\n       \"پیوند معنایی با ریشهٔ «زدن» از پوکورنی و باک است: بیماری را ضربهٔ دیوان می‌دانستند، و بارتولومه نیز \"\n       \"خود آن را با گوتی banja «زخم» مقایسه کرده است. اما در تحلیل امروزی بازتاب اوستایی *gʷʰen- همواره jan-/ɣn- \"\n       \"است نه b-؛ پس اگر واژه‌های ژرمنی از *gʷʰen- باشند، خانوادهٔ اوستایی دیگر هم‌ریشهٔ آنها نیست. \"\n       \"با احتیاط پذیرفتنی است.\"),\n     \"sources\": [W + \"Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:145\", \"status\": \"partial\",\n        \"note\": (\"Klein 1966 s.v. 'bane, n.': 'OE. bana ‚murderer, slayer‘ ... Goth. banja ‚stroke, wound‘, and cogn. with \"\n          \"Avestic banta, ‚ill‘, bqnayen, ‚they make sick‘' — substantively exactly Nourai's arrow (KLN_1966.txt:4378). \"\n          \"But the page is off by one: that line sits on leaf 89 of the scan (printed pp. 146/147); leaf 88 carries the \"\n          \"printed numbers 144 and 145 and runs 'balladry ... banderole', so p.145 has no 'bane'.\")},\n       {\"ref\": \"SYN:304\", \"status\": \"supports\",\n        \"note\": (\"Buck p. 304 (§4.84 SICK), SYN.txt:7792: 'Av. banta-, pass. pple. of ban- ‚be sick‘ in caus. banaya- \"\n          \"‚make sick‘ (also bazda-, pass. pple. of band- id.) : Goth. banja, ON ben, etc. ‚wound‘, OE bana ‚murderer‘, \"\n          \"OHG bano ‚death, murderer‘. Walde-P. 2.149. Barth. 996.' — all three Avestan forms and the Germanic link, on \"\n          \"the very page Nourai cites.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 925 f. (BRT.txt:16712, 16696)\", \"stance\": \"supports\",\n        \"note\": \"'j., g. ban- V. ‚kranken‘. Praes. 30 (Kaus.) bqnaya-. — PPfP. banta- (sbes.). Kaus. ‚krank machen‘ ...'; 'j. banta- Adj. (fem. °tā-) ‚erkrankt; krank, siech‘'; the article closes 'Vgl. got. banja ‚Wunde‘, ahd. bana ‚Verderben‘'.\"},\n       {\"src\": \"SYN\", \"where\": \"Buck pp. 302-305, §§4.83-4.85 (SYN.txt:7694, 7727, 7792, 7827)\", \"stance\": \"supports\",\n        \"note\": \"Table 4.84 gives 'Av. banta-, bazda' for 'sick'; 4.83 'Av. drva-, abanta-' for 'well', with 'Av. abanta- cpd. of a-privative and banta- ‚sick‘ (4.84)'.\"},\n       {\"src\": \"POK\", \"where\": \"IEW p. 126 (POK_01.txt:1774)\", \"stance\": \"supports\",\n        \"note\": \"'Av. bqnayan ‚sie machen krank‘, banta- ‚erkrankt, siech‘' heads the bhen- article.\"},\n       {\"src\": \"KLN\", \"where\": \"s.v. bane (KLN_1966.txt:4378, printed p.146)\", \"stance\": \"supports\",\n        \"note\": \"'... cogn. with Avestic banta, ‚ill‘, bqnayen, ‚they make sick‘'.\"},\n       {\"src\": \"CHEUNG\", \"where\": \"grep 'ban-', 'banta' in CHEUNG.txt\", \"stance\": \"silent\",\n        \"note\": \"Cheung's Etymological Dictionary of the Iranian Verb has no entry for this Avestan root in the local text.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": None,\n     \"words\": \"\",\n     \"verdict\": \"unverified\",\n     \"derivation\": (\"Pass-through/empty node: on the printed page (book p. 56 = pdf p. 86) an arrow leaves the Avestan box \"\n       \"and ends in a large box that is completely blank — no language header, no word, no reference. The extraction is \"\n       \"faithful (lang, refs and words are all null/empty in the JSON exactly as in the book); the empty frame is Nourai's \"\n       \"own unfilled placeholder, probably where an English 'bane'-type descendant was meant to go, since Pokorny's and \"\n       \"Klein's Germanic material is what the Avestan box is normally paired with. There is nothing to verify.\"),\n     \"derivation_fa\": (\"این جعبه در متن چاپی کتاب (صفحهٔ ۵۶، برابر صفحهٔ ۸۶ پی‌دی‌اف) کاملاً خالی است؛ تنها \"\n       \"پیکانی از جعبهٔ اوستایی به آن کشیده شده و نه نام زبان دارد نه واژه و نه مأخذ. پس خطای خوانش اسکن \"\n       \"نیست، بلکه جای خالی پرنشده‌ای در خود کتاب است و چیزی برای راستی‌آزمایی در آن وجود ندارد.\"),\n     \"sources\": [],\n     \"book_prints\": \"(an empty box, no text at all)\",\n     \"ref_check\": [\n       {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"the node carries no references in the book (empty box).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"IEW p. 126\", \"stance\": \"silent\",\n        \"note\": \"Nothing in the bhen- article is left over that would fill a fourth Avestan-descended box.\"},\n       {\"src\": \"BRT\", \"where\": \"col. 925 f.\", \"stance\": \"silent\",\n        \"note\": \"Bartholomae's ban- article lists only bqnaya- and banta-, i.e. exactly the words already in node #1.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Germanic\",\n     \"words\": \"banon\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"Proto-Germanic *banōn- is a real reconstruction, but it is a masculine n-stem NOUN 'slayer, killer, \"\n       \"bane' — OE bana, OFris. bona, OS/OHG bano, ON bani 'death; killer' — not a verb 'to strike' as the chart glosses \"\n       \"it; the verb sense belongs to the root, not to this stem. Watkins reconstructs precisely 'Germanic suffixed form \"\n       \"*ban-ōn-' but from o-grade *gʷhon-, and Wiktionary/Kroonen make *banô < *gʷʰon-ō, an individualising \"\n       \"n-stem of *gʷʰonós 'one who strikes down', the initial *gʷʰ > b being the regular (if debated) Germanic \"\n       \"outcome. Klein and Pokorny keep the same Germanic set under *bhen- and expressly link it to Av. banta-. So the form \"\n       \"is right and its membership in this family is right; the gloss 'to strike' and the ultimate root assignment are what \"\n       \"modern handbooks change.\"),\n     \"derivation_fa\": (\"ژرمنی آغازین *banōn- در حقیقت اسم است به معنای «کشنده، مایهٔ هلاک» (انگلیسی کهن bana، \"\n       \"آلمانی علیای کهن bano، نورسی باستان bani)، نه فعل «زدن» چنان‌که چارت معنی کرده است. \"\n       \"کلاین (ذیل bane) و پوکورنی همین گروه را ذیل *bʰen- و هم‌ریشه با اوستایی banta- می‌دانند؛ اما \"\n       \"واتکینز و ویکی‌واژه آن را از *gʷʰon-ō (ریشهٔ *gʷʰen-) می‌گیرند، با این دگرگونی آوایی که \"\n       \"*gʷʰ آغازین در ژرمنی به b بدل می‌شود. صورت واژه درست است ولی معنای «to strike» نادرست.\"),\n     \"sources\": [\n       W + \"Reconstruction:Proto-Germanic/ban%C3%B4\",\n       \"https://www.etymonline.com/word/bane\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"partial\",\n        \"note\": (\"Watkins 1985 (AHD_watkins1985.txt:545) does give 'Germanic suffixed form *ban-ōn-' — Nourai's 'banon' — \"\n          \"but under 'gʷhen-¹. To strike, kill', with '[Pok. 2. gʷhen-(2)- 491, bhen- 126.]'; the index line 1270 reads \"\n          \"'AUTOBAHN g*hen-*'. So AHD supports the form and the family but not the filing under Bhen.\")}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"s.v. bane, printed p.146 (KLN_1966.txt:4378)\", \"stance\": \"supports\",\n        \"note\": \"'OE. bana, ‚murderer, slayer‘, rel. to OE. benn, ‚wound‘, OS. bano, OFris. bona, OHG. bano, ‚murderer‘, OHG. bana, ‚murder‘, ON. bani ... Goth. banja, ‚stroke, wound‘' — the Germanic set, but always as nouns.\"},\n       {\"src\": \"POK\", \"where\": \"IEW p. 126\", \"stance\": \"supports\",\n        \"note\": \"'got. banja ‚Schlag, Wunde, Geschwür‘ ... aisl. bani m. ‚Tod; Mörder‘, ags. bana, ahd. as. bano ‚Totschläger, Mörder‘' — nouns under bhen-.\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷhen-¹\", \"stance\": \"partial\",\n        \"note\": \"Same *ban-ōn- but from o-grade *gʷhon-.\"},\n       {\"src\": \"SKT\", \"where\": \"grep '^bane', 'banja' in SKT.txt\", \"stance\": \"silent\",\n        \"note\": \"Skeat's Concise has no 'bane' entry in the local OCR.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Middle German\",\n     \"words\": \"bane\",\n     \"verdict\": \"plausible\",\n     \"derivation\": (\"'Middle German' is Nourai's label for Middle High German. MHG bane / ban f. and m. 'way, road, open \"\n       \"track' is well attested (whence NHG Bahn, Du. baan, Yiddish באַן), and continues a feminine PGmc *banō \"\n       \"'battlefield, cleared space, cleared way' — the ā-stem beside the n-stem *banô of node #3, so the two are \"\n       \"morphological siblings rather than one from the other. The gloss 'path cut through woods' is Pokorny's own \"\n       \"paraphrase, but he marks the whole connection as merely possible: 'vielleicht auch mhd. bane, ban f. und m. ‚Bahn, \"\n       \"Weg‘ als ‚*Durchhau durch einen Wald‘ oder ‚*festgeschlagener Weg‘' (IEW 126); Watkins likewise brackets it \"\n       \"'(? < “path hewn through woods”)' and Wiktionary flags the *banō etymology as incomplete and doubted. Hence \"\n       \"plausible, not confirmed: 'Bahn' may equally be an old term of the cleared battlefield or a 'beaten track'.\"),\n     \"derivation_fa\": (\"برچسب «Middle German» در کتاب همان آلمانی میانهٔ علیا (MHG) است. صورت bane / ban \"\n       \"«راه، گذرگاه» از صورت مادینهٔ ژرمنی آغازین *banō «میدان نبرد، جای پاک‌شده، راه گشوده» \"\n       \"می‌آید — یعنی هم‌پایهٔ *banô گرهٔ پیشین، نه برآمده از آن. پوکورنی (ص ۱۲۶) خود این پیوند را \"\n       \"با قید «شاید» (vielleicht) می‌آورد: «*بریدگی در جنگل» یا «*راه کوبیده‌شده»؛ واتکینز نیز آن را درون \"\n       \"پرانتز پرسشی می‌نویسد. پس واژه و معنا درست است ولی پیوند آن با ریشهٔ «زدن» فرضی است؛ \"\n       \"با احتیاط پذیرفتنی است.\"),\n     \"sources\": [\n       W + \"Bahn\",\n       W + \"Reconstruction:Proto-Germanic/ban%C5%8D\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"none\", \"status\": \"not_checked\",\n        \"note\": \"the book prints no reference on this box; the claim is however covered by the root's POK:126 and by the AHD box on the German node.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"IEW p. 126 (POK_01.txt:1774)\", \"stance\": \"partial\",\n        \"note\": \"'vielleicht auch mhd. bane, ban f. und m. ‚Bahn, Weg‘ als ‚*Durchhau durch einen Wald‘ oder ‚*festgeschlagener Weg‘' — Nourai's gloss verbatim, but hedged with 'vielleicht'.\"},\n       {\"src\": \"WLD\", \"where\": \"Bd. II p. 149 (WLD_Bd2_pages.txt:9714-9716)\", \"stance\": \"partial\",\n        \"note\": \"Same sentence with the added source note '(s. Kluge und Weigand-Hirt s. v.)'.\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷhen-¹ (AHD_watkins1985.txt:545)\", \"stance\": \"partial\",\n        \"note\": \"'Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN' — the same chain, question-marked.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"German\",\n     \"words\": \"auto-bahn\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"German Autobahn f. 'motorway' is a 20th-century compound coined for the Reich motorway programme of \"\n       \"the 1930s: Auto (clipped from Automobil) + Bahn 'way, track', the direct continuation of MHG bane of node #4 \"\n       \"(MHG bane > early NHG ban(e) > NHG Bahn, with the usual lengthening of the stem vowel in open syllable and loss of \"\n       \"the final -e). Webster's Twentieth Century gives the parsing explicitly, and Watkins ends his gʷhen-¹ Germanic \"\n       \"sub-entry with 'AUTOBAHN'. The gloss 'highway' is right (a divided, limited-access motorway).\"),\n     \"derivation_fa\": (\"آلمانی Autobahn «بزرگ‌راه» ترکیبی نوساخته از دههٔ ۱۹۳۰ م. است: Auto (کوتاه‌شدهٔ \"\n       \"Automobil) + Bahn «راه، خط»، و Bahn دنبالهٔ مستقیم همان bane آلمانی میانه است (با کشیده شدن واکه در \"\n       \"هجای باز و افتادن -e پایانی). وبستر و پیوست AHD همین تجزیه را می‌آورند. ادعای نورایی درست است.\"),\n     \"sources\": [\n       \"https://www.etymonline.com/word/autobahn\",\n       W + \"Bahn\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"Watkins 1985 (AHD_watkins1985.txt:545): 'Middle High German ban, bane (> German Bahn), way, road ...: AUTOBAHN'; index (line 1270) 'AUTOBAHN g*hen-*'. The MHG > German Bahn > Autobahn step is exactly Nourai's.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. Autobahn (WEB_vol1.txt:13717)\", \"stance\": \"supports\",\n        \"note\": \"'Au’tō-bahn, n.; pl. Au’tō-bahn-en, Au’tō-bahns, [G.; auto (contr. of automobil, automobile) and bahn, a course, highway.] in Germany, a four-lane highway for fast driving ...'\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷhen-¹\", \"stance\": \"supports\",\n        \"note\": \"AUTOBAHN is the headword the MHG bane branch feeds.\"},\n       {\"src\": \"KLN\", \"where\": \"grep 'autobahn' in KLN_1966/KLN_1971\", \"stance\": \"silent\",\n        \"note\": \"Klein has no Autobahn entry (the word is not naturalised English enough for his 1966 lemma list).\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Persian\",\n     \"words\": \"otobân «اتوبان»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"Persian اتوبان otobān 'motorway, freeway' is a direct 20th-century loan of German Autobahn, not a \"\n       \"French mediation (French says autoroute). Mo'in's Farhang-e Fārsi marks it '[آلما.]' (= آلمانی, German) and \"\n       \"defines it 'جادهٔ پهن ماشین‌رو دو‌طرفه، آزادراه، بزرگ‌راه'. Phonetically German [aʊ] is rendered by \"\n       \"Persian او /o(w)/ in the first syllable (as in اتومبیل, اتوبوس) and German -ahn [aːn] by ان -ān, giving otobān; \"\n       \"the word spread in Iran with the motorway building of the 1960s-70s, which is why the printed Mo'in (1363/1984) \"\n       \"lexicon volumes and Borhan-e Qate' have no such lemma while the modern online Mo'in does. Transliteration and script \"\n       \"in the JSON match the printed box.\"),\n     \"derivation_fa\": (\"«اتوبان» وام‌واژه‌ای است مستقیم از آلمانی Autobahn، نه از راه فرانسه (در فرانسه \"\n       \"autoroute می‌گویند). فرهنگ فارسی معین آن را با نشان [آلما.] و معنای «جادهٔ پهن ماشین‌رو \"\n       \"دو‌طرفه، آزادراه، بزرگ‌راه» آورده است. در وام‌گیری، مصوت مرکب آلمانی au به «او» و -ahn به \"\n       \"«ان» بدل شده است (مانند اتومبیل و اتوبوس). این واژه از دههٔ ۱۳۴۰ ش. به بعد رایج شد، و به همین \"\n       \"سبب در متن چاپی معین (۱۳۶۳) و برهان قاطع مدخلی ندارد. ادعای نورایی درست است.\"),\n     \"sources\": [\n       W + \"%D8%A7%D8%AA%D9%88%D8%A8%D8%A7%D9%86\",\n       \"https://abadis.ir/fatofa/%D8%A7%D8%AA%D9%88%D8%A8%D8%A7%D9%86/\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"the book prints no reference on the Persian box.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. اتوبان, via abadis.ir\", \"stance\": \"supports\",\n        \"note\": \"'(اُ ) [ آلما. ] جادة پهن ماشین رو دو طرفه ، آزادراه ، بزرگ راه' — the tag [آلما.] is Mo'in's mark for German.\"},\n       {\"src\": \"MON\", \"where\": \"grep 'اتوبان' in MON_part1/part2 and MON_2vol_Adena\", \"stance\": \"silent\",\n        \"note\": \"The printed lexicon scans have اتوبوس and اتومبیل but no اتوبان — the word post-dates that lemma list.\"},\n       {\"src\": \"BQT\", \"where\": \"grep 'اتوبان' in BQT_v1/v2_pages.txt\", \"stance\": \"silent\",\n        \"note\": \"Borhan-e Qate' (a 17th-c. dictionary) naturally has no modern European loan of this kind.\"},\n       {\"src\": \"ARY\", \"where\": \"grep 'اتوبان' / 'autobahn' in ARY_pages.txt and ARY_latin_index_pages.txt\", \"stance\": \"silent\",\n        \"note\": \"Aryanpur's IE-roots dictionary of Persian does not list the word.\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"English\",\n     \"words\": \"autobahn\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": (\"English autobahn is an unassimilated 20th-century borrowing of German Autobahn, first recorded in \"\n       \"English in 1937, when the Reichsautobahnen were international news; it keeps German stress and even the German \"\n       \"plural beside the anglicised one (Webster's: 'pl. Autobahnen, autobahns'). Meaning unchanged, 'German motorway', \"\n       \"later generalised to any European motorway. Nourai's arrow German → English is correct and uncontroversial.\"),\n     \"derivation_fa\": (\"انگلیسی autobahn وام‌واژهٔ مستقیم آلمانی است که نخستین کاربرد آن در انگلیسی به \"\n       \"۱۹۳۷ م. بازمی‌گردد (اتیم‌آن‌لاین)؛ واژه حتی جمع آلمانی Autobahnen را نگاه داشته است (وبستر). \"\n       \"معنا دگرگون نشده است. ادعای نورایی درست است.\"),\n     \"sources\": [\n       \"https://www.etymonline.com/word/autobahn\",\n       W + \"autobahn\"\n     ],\n     \"ref_check\": [\n       {\"ref\": \"none\", \"status\": \"not_checked\", \"note\": \"the book prints no reference on the English box; the AHD box on the German node covers the headword AUTOBAHN.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. Autobahn (WEB_vol1.txt:13717)\", \"stance\": \"supports\",\n        \"note\": \"Entered as an English headword with the etymology '[G.; auto ... and bahn, a course, highway.]' and the double plural.\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985, index line 1270\", \"stance\": \"supports\",\n        \"note\": \"'AUTOBAHN g*hen-*' — listed as an English word derived through the Germanic branch.\"},\n       {\"src\": \"KLN\", \"where\": \"grep 'autobahn' in KLN_1966/KLN_1971\", \"stance\": \"silent\",\n        \"note\": \"Not a Klein lemma.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-86.json', 'w', encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk86.py",
 "description": "Write page-86.json"
}
```


### [2026-09-05T06:44:08.938Z] TOOL RESULT

```
ok
```


## [2026-09-05T06:44:12.140Z] TOOL CALL #51: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-86.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 86",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T06:44:14.033Z] TOOL RESULT

```
JSON OK
nodes verified: 7/7
node verdicts: {'plausible': 3, 'unverified': 1, 'confirmed': 3}
root verdicts: {'plausible': 1}
ref checks: {'partial': 2, 'supports': 2, 'not_checked': 4}
books consulted: {'supports': 11, 'silent': 9, 'partial': 4} | by book: {'POK': 4, 'KLN': 4, 'AHD': 4, 'BRT': 2, 'WEB': 2, 'MON': 2, 'SYN': 1, 'CHEUNG': 1, 'SKT': 1, 'WLD': 1, 'BQT': 1, 'ARY': 1}
```


## [2026-09-05T06:44:29.161Z] AGENT

Page 86 (book p. 56) verified — one entry (root **Bhen**, 7 nodes). `verify_check.py 86`: 7/7 nodes, 0 PROBLEM lines.

**Verdicts** — root: 1 plausible. Nodes: 3 confirmed (#5 German auto-bahn, #6 Persian اتوبان, #7 English autobahn), 3 plausible (#1 Avestan, #3 Germanic, #4 Middle German), 1 unverified (#2, the empty box).

**Key findings**
- Root: POK:126 checks out verbatim (`bhen- ‚schlagen, verwunden‘`, with the Avestan, Germanic and MHG material of the whole chart). Downgraded to *plausible* because Watkins/AHD, Wiktionary and Kroonen now file all the Germanic forms under *gʷʰen-* "strike, kill" (`*gʷʰ- > b-` in Germanic) and Etymonline says *bane* has "no certain IE etymology" — a separate *bʰen-* is no longer needed.
- #1 Avestan `ban / banta / banay`: forms and glosses exact (Bartholomae col. 925 f.; Buck p. 304 quotes all three). Plausible only because Avestan reflects *gʷʰen-* as *jan-/ɣn-*, so under the modern root the Avestan family can't be the Germanic cognate.
- #3 `banon` "to strike": PGmc *banōn-* is a **noun** ("slayer, bane"), not a verb — Nourai's gloss is wrong; the form itself is right.
- #4 MHG `bane`: Pokorny's own link is hedged ("vielleicht … *Durchhau durch einen Wald"), Watkins brackets it "(? …)", Wiktionary calls the *banō* etymology doubted.

**No transcription/extraction errors.** Node #2 is genuinely a blank box on the printed page (checked the 300→200 dpi render, copied to `data/verification/sources/refs/ocr/BOOK/86.png`) — Nourai's own unfilled placeholder; the JSON is faithful.

**Ref-check note (minor, not a data fix):** `KLN:145` is off by one page — Klein's `bane` entry sits on printed p. 146 (leaf 89); p. 145 ends at *banderole*. Content fully supports the arrow.

8 web pages archived via `fetch_source.py` (Wiktionary Bahn / *banô / *banō / autobahn / اتوبان / *gʷʰen-, Etymonline autobahn + bane, abadis Mo'in).
