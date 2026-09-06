# Verification process log — verify-page-197


## [2026-09-06T02:14:40.054Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 197 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-197.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-197.json. Write /home/sfmqrb/git/rishe/data/verification/page-197.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 197` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T02:14:41.589Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T02:14:42.292Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T02:14:42.306Z] TOOL RESULT

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


## [2026-09-06T02:14:42.550Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-197.txt"
}
```


### [2026-09-06T02:14:42.576Z] TOOL RESULT

```
1	=== PDF page 197 (book page 167) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Glei, Greios : to swell, increase; expanse  (refs POK:401; KNT:192)
4	#1 (parent #0) [Old Persian] refs=POK:401; SYN:37 | drayah : sea
5	  #2 (parent #1) [Pahlavi] refs=MON:1730; BQT:847 | drai-âp : sea water, sea ☞Ab 1
6	    #3 (parent #2) [Persian] refs=MON:37; BQT:847; HRN:125; POK:401 | daryâ «دریا» : sea
7	#4 (parent #0) [Avestan] refs=POK:401; SYN:37 | zrayah, zarayah : body of water, sea
8	  #5 (parent #4) [Pahlavi] refs=MON:1730; BQT:1010 | zrě : sea
9	    #6 (parent #5) [Persian] refs=BQT:1010 | zrâh «زراه» : sea
10	  #7 (parent #4) [Sogdian] refs=SOD:465 | zry : sea
11	--- entry 1 ---
12	ROOT Glue -> redirect to Gel
13	
```


## [2026-09-06T02:14:46.081Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-197.json",
 "description": "Read page 197 source JSON"
}
```


### [2026-09-06T02:14:46.125Z] TOOL RESULT

```
{
  "pdf_page": 197,
  "book_page": 167,
  "entries": [
    {
      "root": {
        "name": "Glei, Greios",
        "lang": "Indo-European",
        "refs": "POK:401; KNT:192",
        "gloss": "to swell, increase; expanse"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:401; SYN:37",
          "words": [
            {"translit": "drayah", "gloss": "sea", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "MON:1730; BQT:847",
          "words": [
            {"translit": "drai-âp", "gloss": "sea water, sea", "script": null, "see": ["Ab 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:37; BQT:847; HRN:125; POK:401",
          "words": [
            {"translit": "daryâ", "gloss": "sea", "script": "دریا"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:401; SYN:37",
          "words": [
            {"translit": "zrayah, zarayah", "gloss": "body of water, sea", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Pahlavi",
          "refs": "MON:1730; BQT:1010",
          "words": [
            {"translit": "zrě", "gloss": "sea", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:1010",
          "words": [
            {"translit": "zrâh", "gloss": "sea", "script": "زراه"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "Sogdian",
          "refs": "SOD:465",
          "words": [
            {"translit": "zry", "gloss": "sea", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Glue",
        "redirect": "Gel"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-06T02:14:47.886Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','SYN','MON','BQT','HRN','SOD','WLD','AHD','PHD','NYB','HUB','CHEUNG','BRT','ARY','IEC']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-06T02:14:49.982Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

CHEUNG null

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open
```


## [2026-09-06T02:15:05.875Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80"
}
```


### [2026-09-06T02:15:05.922Z] TOOL RESULT

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
```


## [2026-09-06T02:15:07.343Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','SYN','BQT','MON','SOD','ARY']:\n    print('=====',k)\n    print(json.dumps(d.get(k),ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-06T02:15:08.909Z] TOOL RESULT

```
===== POK
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
===== KNT
{
 "title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953",
 "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/oldpers",
 "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt",
 "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.",
 "notes": "",
 "cites": "page number of Kent, Old Persian (1953); the lexicon starts p. 164"
}
===== SYN
{
 "title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949",
 "edition_found": "1949 (reprint scans, same pagination in all printings)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt",
 "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.",
 "notes": "Two other open copies: dictionaryofselectedsynonyms...buck_963_N, fock_a-dictionary-...; restricted: dictionaryofsele0000carl.",
 "cites": "page number of Buck, A Dictionary of Selected Synonyms (1949)"
}
===== BQT
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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
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
===== MON
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
===== SOD
{
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
 "cites": "entry number / page in Gharib's Sogdian dictionary"
}
===== ARY
{
 "title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.",
 "kind": "local_scan_ocr",
 "url": "",
 "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"
 ],
 "page_offset": "printed page = pdf page + 1",
 "scans": [
  {
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf",
   "first_printed": 1,
   "last_printed": 546,
   "pdf_offset": -1,
   "lang": "fas+eng",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"
  }
 ],
 "notes": "Image-only PDF provided by the owner (2026-09-04). Use as an additional modern source alongside Wiktionary/Cheung/Hasandust when judging Persian arrows; cite as ARY:<page>. | full OCR text fas+eng (headwords in Persian and Latin caps), printed = pdf+1 | Latin-only OCR (cleaner for transliterated headwords, root names, Pokorny numbers)"
}
```


## [2026-09-06T02:15:12.137Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==58' POK_02.txt | head -60"
}
```


## [2026-09-06T02:15:12.721Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 401\" -A3 -B40 POK_full.txt | head -120"
}
```


### [2026-09-06T02:15:13.805Z] TOOL RESULT

```
 :)  ydXa,  wonach  auch  ydlaytrog  statt  *yXa'KTÖg.  Die  Form  hom. yldyog  {TtsQiyXayrjg,  später  yXaydo)),  andrerseits  dissimiliert  kret.  xAdyog, oeht  vielleicht  auf  Nom.  "^ylccy  <  */Aax  zurück.
Lat.  lac,  lactis  vl.,  mit  dissimilatorischem  Schwund  des  anlaut.  Gutturals aus  *glact  =  gv.  ydXa ;  alt-  und  spätlat.  i-St.  lade,  vgl.  PL  lactes  f.  , Milch der  männlichen  Fische';  abgeleitet  delicus  (*de-lac-os)  ,der  Muttermilch entwöhnt'  ?
Über  altchin.  lac  {*glac)  aus  idg.  *galakt  s.  Karlgren  DLZ.  1926,  1960  f.
WP.  I  659,  WH.  I  337  f.,  741  f.
gleg'  , weich,  zart'.
Nasaliert  in  aisl.  klekkr  , weich,  biegsam,  nachgiebig,  sentimental'  (aus *klinkuaz),  aisl.  klekkva  , weich  werden,  Mutlosigkeit  oder  Trauer  zeigen, stöhnen',  scliwed.  kläcka  , erschrecken'  {*klinkwan),  adän.  kliunka  ds.,  dän. Uynke  , wimmern',  vgl.  dazu  das  Kausativ  anord.  klekkva  , weich  machen', schwed.  dial.  kläkka  , schmelzen'  (^klankicjan)'^  ndd.  klinker  ,zart,  schwach, mager';
lit.  gleznas  ,zart,  weich,  schlapp',  gleznüs  ds.,  gleztü,  glezau,  gleUi  , weich, schlaff,  welk  werden',  lett.  glezns]
bulg.  glezz,  glezil  ,  verziehe,  verzärtele',  razgUza  , Verderbtheit,  Unge- zogenheit'.
WP.  I  661.
glei-  ,anlaufen,  anstürmen'?   Nur  indoiranisch.
Ai.  jrdyatl  , stürmt  an,  läuft  an',  jrdyas-  n.  , Ungestüm,  Lauf,  Flußlauf', prthu-jrdya-  ,weit  laufend';
av.  zrayah-,  apers.  drayah-  ,See,   Meer',   mpers.   zray,  npers.   (mit  Um- stellung) daryä,  pdvdu-zrayah  ,über  weite  Wasserflächen  sich  erstreckend'. WP.  I  660,  WH.  I  608.
gleubh-  , schneiden,  klieben,  schnitzen,  abschälen'.
Gr.  ylvq)a)  , schnitze  aus,  meißle  aus,  graviere',  yXvcplg,  -iSog  f.  , Kerbe';
lat.  glühö,  -ere  , abschälen,  bes.  ein  Tier  abdecken',  glüma  , Hülse,  Schale, Balg  des  Getreides'  (Formans  -smä;  glühö  mit  ü  =  eu,  wie  nhd.  klieben)]
ahd.  kliohan,  ags.  cleöfan,  anord.  kljüfa  , spalten',  anord.  klauf  f.  ,Kluft, der  gespaltene  Huf,  schwundstuf,  anord.  klofna,  -ada  ,sich  spalten',  klyfia klufda  , spalten',  klof  n.  ,Kluft,  Spalt',  klofi  m.  , Türkloben,  Klemme',  = as.    klcibo   m.   , gespaltener    Stock,    Kloben    zum  Vogelfang'  =  ahd.    kloho
26
402
,gespaltener  Stock  zum  Einklemmen  oder  Fangen,  Kloben^   ags.  clofei ,Schnalle^    clufu    f.    ,Zwiebel^    ahd.    kloho-louh,    nhd.    mit    Dissimilation Knoblauch,  ahd.  Jduppa  L  , Zange,  gespaltenes  Holz  zum  Klemmen^  nh^^' Kluppe  {*kUihjön-),  anord.  klyf  f.  ,der  zweigeteilte  PacksatteP,  ahd.  klufi^ nhd.  Kluft-,    nach  Wissmann   (Nom.   postverb.    129 f.)    mit   expressiv  g^ dehnter
```


### [2026-09-06T02:15:13.869Z] TOOL RESULT

```
34210-
34211-yAoKKOv yaAa9r|v6v Hes., probably a Kinderwort with hypocoristic gemination as |jikk6(;), 
34212-
34213-further *yAa, with vocal development in monosyllabic word (probably in the child's mouth, 
34214-
34215-whence also die initial stress:) yaAa, whereupon also yaAaKTO(; instead of *yAaKT6(;. The 
34216-
34217-form hom. ykdyoc, (nspiyAaync;, later yAayaw), on the other hand dissimilated Cretan 
34218-
34219-KAayoc;, goes back perhaps to Nom. *yAay < *yAaK. 
34220-
34221-Latin lac, lactisu., with dissimilation reduction of aniaut. Gutturals from *glact= gr. yaAa; 
34222-old- and late Latin /-stem lacte, compare PI. lactesi. " milk of the male fish '; derived 
34223-delicus ( *de-lac-os) " put away from the breast, weaned; the weaned mother's milk '? 
34224-
34225-About altchin. lac{*glac)iroxr\ Indo Germanic *galakts. Karlgren DLZ. 1926, 1960 f. 
34226-
34227-References: WP. I 659, WH. I 337 f., 741 f. 
34228-Page(s): 400-401 
34229-
34230-Root / lemma: gleg- 
34231-
34232-Meaning: soft, tender 
34233-
34234-Material: Nasalized in Old Icelandic klokkr^ soft, pliable, flexible, sentimental ' (from 
34235-
34236-*klinkuaz). Old Icelandic klekkva^ become soft, show faintheartedness or grief, groan, 
34237-
34238-moan', Swedish /r/5c/ra "frighten' {*klinkwan). Old Danish kliunka6s., Danish klynke^ 
34239-
34240-whimper ', compare in addition the causative Old Norse klokkva' soW. make', Swedish dial. 
34241-
34242-/r/5/r/r5 'melt' {*klankwjan)\ ndd. k//nker^ tender, weak, lean '; 
34243-
34244-Lithuanian g/eznas ^tender, soft, flabby', gleznus ds., gl^ztu, glezau, glezti^ soft, slack, 
34245-become wilted ', Latvian glQzns, 
34246-
34247-Bulgarian glez-b, gleziT forgive, coddle ', razgleza^ corruptness, unmannerliness '. 
34248-
34249-References: WP. I 661. 
34250:Page(s): 401 
34251-
34252-Root / lemma: gleUd^- 
34253-
34254-
34255-
34256-Meaning: to cut, slice, pare 
34257-
34258-Material: Gr. yAucpu) ' carve from, carve out, cut out with a l<nife; engrave; to note down [on 
34259-tablets] ', Y^ucpic;, -i5o(;f. ' incisure, notched end of the arrow; but perh. of notches or 
34260-grooves for the fingers; poet, for the arrow itself; also in pi., notches in the arrow-head; 
34261-pen-knife; chisel; in Architecture, capitals of columns; in pi., a lurking-place, den, hole, 
34262-cave '; 
34263-
34264-Latin glubo, -ere "to deprive of its bark, to bark, peel; to cast off its shell or bark ', gluma 
34265-" a hull or husk, esp. of corn '(forms -sma; g/ut>d\N\t\r\ 0= eu, as Modern High German 
34266-klieben); 
34267-
34268-Old High German klioban. Old English cleofan. Old Norse /r^^/^ "split'. Old Norse klauf\. 
34269-"cleft, gap, the cloven hoof, zero grade Old Norse klofna, -ada'be split', k/yf/a k/ufda ^ spWV , 
34270-k/ofn. "cleft, gap, cleft, fissure', k/of/m. " door latch, clamp ', = Old Saxon k/obom. "cloven 
34271-stick, hook for fowling ' = Old High German k/obo " cloven stick for catching or capturing, 
34272-hook ', Old English clofei. " buckle ', clufui. "onion, bulb'. Old High German klobo-louh. 
34273-Modern High German with dissimilation Knoblauch, Old High German kluppai. " pliers, 
34274-tongs, split wood for clamping ', Modern High German Kluppe {*klubjdn-). Old Norse klyfi. 
34275-" the split packsaddle ', Old High German kluft. Modern High German Kluft, after 
34276-Wissmann (Nom. postverb. 129 f.) with expressive lengthened zero grade J.' Old High 
34277-German klubon^ to pick to pieces; defoliate ', Modern High German k/auben{\n addition 
34278-probably with Germanic intensive consonant increase Old Norse klypa^ clamp, nip, 
34279-pinch'); 
34280-
34281-Old Prussian gleuptene^ mouldboard, curved metal blade on the front of a plow which 
34282-loosens the earth '; but Lithuanian glaudyti^ take out its shell or pod ' has probably -o'from 
34283-gvaldyti^ take out its shell or pod, core ' referring, exactly in such a way, as gvalbyti6s. -b- 
34284-is covered by *glaubyti. 
34285-
34286-References: WP. I 661, WH. 1 610 f. 
34287:Page(s): 401-402 
34288-
34289-Root / lemma: glogh- : g/agh- 
34290-
--
38242-Slavic *gvezda (from *guaigzda, through dissimilation from *zuaigzda) in Old Church 
38243-Slavic dzvezda, Serbo-Croatian zvigezda, poln. gwiazda, russ. zvezdai. 'star'. 
38244-
38245-References: Trautmann 373 f., Pedersen La cinqunderdecl. Latin 74, Mikkola Urslav. Gr. 
38246-166 f. Probably inaccurate about gr. cpoTpoq etc. above 118. 
38247-Page(s): 495 
38248-
38249-Root / lemma: ghuolc-, ghuak"- 
38250-
38251-Meaning: to shine, shimmer 
38252-
38253-Material: Gr. Siacpaaasiv Siacpaivsiv Hes., cpdjijj cpaoc; Hes.; "rrapai-cpaaaei Tivaa-asi . . . 
38254-
38255-Hes., reduplicated Traicpaaaw ' dart, rush about, quiver, wave violently'; 
38256-
38257-Latin fax{o\6 faces), facisi. 'torch; agitator, inciter, troublemaker, fomenter ', Demin. 
38258-/^c^/a 'torch', /^ce/^s 'elegant, witty', facetia and -ae^ a jest, witticism; drollery, piece of 
38259-humor, a witty or clever thing in action or behavior. Wit, witty sayings '; 
38260-
38261-
38262-
38263-Lithuanian zi/a/re 'candle'. 
38264-
38265-References: WP. I 645, WH. I 438 f., 471, 864, Trautmann 374. 
38266-Page(s): 495 
38267-
38268-Root / lemma: glei- 
38269-
38270-Meaning: to run up to 
38271-
38272-Note: Only indoiranisch. 
38273-
38274-Material: Old Indie yr^ya//' onrushes, attacks, starts, activates \Jrayas-n. " 
38275-
38276-impetuousness, hastiness, run, flow, river flow ', prthu-Jraya-^ distant running '; 
38277-
38278-Avestan zrayah-. Old pers. drayah-^ sea ', Middle Persian zray, npers. (with metathesis) 
38279-darya, psreu-zrayah' wide water surface stretching above '.
```


## [2026-09-06T02:15:35.586Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK_full jrayati contexts ===\"; grep -n \"jrayas\\|Jrayas\\|jrayati\\|Jraya//\\|zrayah\" POK_full.txt | head -20; echo \"=== POK_02 zrayah ===\"; grep -n \"zrayah\\|drayah\\|dary\" POK_02.txt | head -20"
}
```


### [2026-09-06T02:15:35.685Z] TOOL RESULT

```
=== POK_full jrayati contexts ===
38274:Material: Old Indie yr^ya//' onrushes, attacks, starts, activates \Jrayas-n. " 
38278:Avestan zrayah-. Old pers. drayah-^ sea ', Middle Persian zray, npers. (with metathesis) 
38279:darya, psreu-zrayah' wide water surface stretching above '. 
=== POK_02 zrayah ===
807:av.  zrayah-,  apers.  drayah-  ,See,   Meer',   mpers.   zray,  npers.   (mit  Um- stellung) daryä,  pdvdu-zrayah  ,über  weite  Wasserflächen  sich  erstreckend'. WP.  I  660,  WH.  I  608.
4205:strittig,  ob  hierher:  got.  hindana  ,hinter,  jenseits',  ags.  asächs.  hindan^ ahd.  hintana  ,hinten',  anord.  handan  ,von  jener  Seite  her,  jenseits',  kompara- tivisch got.  hindary  ahd.  hintar  ,hinter',  superlativisch  got.  hindumists ,hinterster,  äußerster',  ags.  hindema  ,letzter*,  wobei  das  n  von  *ki-n-t-, *lco-n-t  dasselbe  wie  in  ahd.  hina  wäre;  oder  mit   gall.  Cintugnätos  ,Erst-
```


## [2026-09-06T02:15:37.036Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT drayah ===\"; grep -n \"drayah\\|draya-\" KNT.txt | head -20; echo; echo \"--- KNT leaf 207 (p.192) ---\"; awk 'BEGIN{RS=\"\\f\"} NR==208' KNT.txt | head -50"
}
```


### [2026-09-06T02:15:39.009Z] TOOL RESULT

```
=== KNT drayah ===
541:dtyhiysa = drayahiya XPh 23; elsewhere drayahyd. ah*üfay'a = ahiyaya XPb 17, XPd 12, XE 17,
706:drayahyd, drayahiya).
1657:Locatives with postpositive à: -di(y) became -dy- before the à, as in duvarayd from *dvarai + à, Aturáyü from *Адит + à. But the script does not show whether locatives in -i changed the 7 to y before d, or kept the vowel by analogy: drayahyü (once -hiyà) may repre- sent either -hj- or -háj-.
2194:J. The neuter formation with suffix -os in nom.- acc. sg., -es- in other forms: type Lt. gen-us gen- ет-18, Gk. *y&-os yév-e-os, Skt. ján-as 3án-as-as. OP has nom. rauta? ‘river’, Skt. srólas; nom.-aec. rauca? ‘day’, Av. raoco ‘light’, Skt. rócas ‘light’; асе. draya* ‘sea’ (and draiya*, §48), Av. zrayd, Skt. jráyas; асе. manaX-cà (§105), Av. mand, Skt. mdnas; acc. züra^ ‘evil’, Ау. 2070; асе. mita? ‘evil’. Inst. manahá, Skt. mánasà. Loc. drayahy-à (with added -2; also written drayahiyà, but whether the ~i- is syllabic cannot be determined), Skt. jrdyasz, ef. Av. manahi-cà. Inst. pl. raucabi$, probably for *raucatbiš, cf. Av. mandbis, Skt. mánobhzs: the -h from -s in certain sandhi positions here trans- ferred to the medial position before the consonant of the case-suffix, and then voiced before the voiced consonant and lost with the same products as when final in the respective languages.
2704:trance’; DB 2.76 pasávasim Hagmatinary uzmayā- patiy akunavam ‘afterwards I put him on the stake (= impaled him) at Ecbatana’; DB 1.15 уату drayahyü ‘(those) who (dwell) by the sea’ (not ‘islanders’, since the term denotes the sa- trapy of which Dascylium was the capital, JNES 2.304). With ‘king’, singular nouns are in the loca- tive, as in DB 1.2 xSéyatiya Pérsary ‘king in Persia’, though plurals are in the genitive (§250.C); similarly DB 1.81 zšaçam tya Babtrauy ‘the kingship in Babylon’. It is a substitute for the genitive in DB 2.23f hya Madaisuvd тайа dha ‘who was chief among the Medes’ (cf. §250.D).
3149:0816. Sryzistic Omissions occur in OP, es- pecially of the copula when there is a predicate adjective or phrase; cf. §275, §276. Examples: DB Lf Cišpäãiš pita (sc. cha) Hazàmanis; 1.9 VIII mand іаитӣуӣ (ве. dha") tyaty . . .; 1.10 adam (sc. amiy) navama; 1.13 ima (se. ha*tiy) dahydva tyaty ‚..} 1.15 tyaty drayahyá (ве. ha*tiy; or possibly daraya"tiy, сї. XPh 23f); 1.27 ima (sc. astiy) tya mand kartam (se. astty).
3157:DB 1.20 zšapa-vā rauca-pati-và ‘by either night or day’, in which zšapa- is gen. and rauca- is ace. DPe 13f tyaty utkahyà ula tyaiy drayahyd ‘those which are of the mainland and those which are beside the sea’, where a gen. in *-ahyd is paired
3474:15 Qura : Arabaya : Mudraya : tyaiy : drayahya : Sparda : Yauna : Mada : Armina : Kat 16 patuka : Parfava : Zraka : Haraiva : Uvárazmiy : Bāxtriš : Suguda : Gadara : Sa
4071:12 å : Armina : Katpatuka : Sparda : Ya 13 unà : tyaty : uskahya : uta : tya 14 iy : drayahyá : uta : dahyáva :t 15 yà : para : draya : Asagarta : Parfava : та
4214:DSe = Darius, Susa Е. 1 baga : vazraka : Auramazdà : hya : ima 2 т: bimim : adadé ; һуа : avam : as 3 татат : adadà : hya : martiyam : ad 4 ada : hya : &iyàülim : adad& : mart 5 iyahyü : hya : Darayavaum : XŠm : ak 6 unauš : айбат : parūvnām : XSm : a 7 шат : parüvnüm : framálàram : a 8 dam : Darayavaus : XS : vazraka : XS : XSy 9 anim : XS : dahyünám : vispazanü 10 nam : XS : ahyaya : bümiyà : vaz 11 rakàyà : düraiy : apiy : Vistas 12 pahyà : puça : HazamaniSya : Рат 13 sa : Pārsahyā : рисо : Ariya : Ari 14 ya : ciga : 08tiy : Dàrayavaus : XS : 15 уа&па : Auramazdaha : imá : dahy 16 āva : {уй : adam : agarbayam : apaia 17 ram : hacd : Parsa : adamsdm : pat 18 iyaxíayaty : manā : bajim : abara : 19 tyasam : hacéma : afahya : ava : aku 20 nava : datam : tya : mand : avadis : a 21 dáraya : Майа: Uja : Parðava : Haraiva : 22 Baatris : Suguda : Uvarazmis 23 : Zrdka : Наташайх : Bataguš : Maci 24 уй : Gadàra : Hidus : Зака : haumava 25 rgà : Saká : tigrazaudà : Babir 26 u$ : Авита : Arabéya : Мийгаа : 27 Armina : Katpatuka : Sparda : Yaun 28 à : аву : drayahya : ula : уа 29 y : paradraya : Skudra : Putayà : 30 Kuxiyd : Karka ; 6àtiy : Рата 31 yavau& : XS : vasiy : tya : duskarta 32 m : Gha : ava : naibam : akunavam : da 33 hyáva : ayauda : aniya : aniyam : 34 aja : ava : adam : akunavam : vašnā 39 : Auramazdaha : уаба : aniya : a 36 шуат : пау : jatiy : cind : gà 37 fava : kaSciy : astiy : дат : 38 tya : maná : haeá : avana : tarsat 39 y : улда : hya : tauviyd : tyam :s 40 kauéim : naiy : jatiy : naiy : vi 41 mardatiy : байу : Dérayavaus :
4578:23 : Mudraya : Yaunà : tya : drayahiyà : dà
5489:çay- vb. ‘lean’: Av. sray-, Skt. Sri-, Gk. кою, Lt. in-clinat, NEng. lean, pIE *flei- (§94). ni- + gay-, causative (8129, $215) ‘restore’; form influenced by ddraya- in Av. and OP (Ware, JAOS 44.285-7): niyacürayam 1st sg. imf. DB 1.64.
5524:Dérayava'u- sb. ‘Darius’ (I, son of Hystaspes, king 522-486 ».c.; IT, son of Artaxerxes I, king 426-04 в.с.): Elam da-ri-a-ma-u-ts, Akk. da-ri- ja-mus, Gk. Дарєюѕ (by haplology for *Aapetaios; Keiper, Acta Sem. Phil. Erlangen, 1.253). From pAr. *dháragat-, pic. to root in OP dar- (§162, §240), + pAr. *yasu asn. ‘the good’ (5158.1), see OP vau-: ‘He who holds firm the good’ (Hz. Arch. Hist. Iran 40, ApI 255, 267, takes as hypocoris- tie of *ddraya-vahu-manah- ‘Holder of Good Thought’; this is rejected by Nyberg, Rel. 361).
5579:drayah- sb. ‘sea’: Av. zrayah-, NPers. dáryà, ·
5580:Skt. jrdyas- ‘expanse’, pIE *órejos- (§88, $113, $128, $156.II). Decl, §185.1. See also para- draya. draya asn. DB 5.23; DPe 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27) XPh 23.

--- KNT leaf 207 (p.192) ---
3f, 57; XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 5.9. Ка&-сїу nsm. DB 149, 53; DSe 37. @& ciy asn. DB 1.58. paruvam-ciy DB 1.63, 67, 69. yaciy (q.v.) DNb 35, 36, 57. haw-cty DPe 23f. hakaram-ciy DNb 34f. [haca-cily DSf 23: vakna-|cily XPg 7f, less likely than vaknalptly, see under apiy. |
Citcizri- sb. ‘Cincikhri’, father of Martiya (§163.V): Elam. st-in-sa-ak-ri-1§, Akk. #-in-Sa- ah-ri-i& Cicizrais gsm. (§179.1V) DB 2.9.
сій adv. ‘so long’, correlative with уйій ‘un- til’: from ci- + suffix seen in Gk. ёте-та ‘then’ (8191.11; wrongly König, RuID 72, and Sen 40). DB 248, 63.
cica- sb. ‘seed, lineage’: Av. &6ra-, NPers. &hr ‘origin’ ($78, $148.IIT). In Ariyaciqa-, Ciça- іахта-.
Ciga"lazma- sb. ‘Cicantakhma’, а Sagartian
OLD PERSIAN
rebel: Elam. şi-iš-ša-an-tak-ma, Akk. -it-ra-an. — | lah-ma, Gk. Tpravraixuns. From ciga-(§9.n1) + | lazma- ‘brave’ ($9.11): ‘Brave-by-Lineage’ (§160,- Ie); the -zm- is Median ($163.II; Jacobsohn, KZ 54.261; Bv. BSLP 31.2.79). For the nasal end-
ing the prior element, see $159.n1. Cicatazma
пет. DB 2.79; 4.20; DBg 1f. Ciçatarmam asm, DB 2.871. Cicalaxmà ism. DB 2.86.
сіла] emphasizing adv. after neg., ‘at all’: , :
Av. cină ‘also, likewise’; perhaps isn. of ci-, cf.. 4 JAOS 58.116-7, 324, and Harl, KZ 63.2 (not ! eità], with Sen 134). DSe 36.
ciyăkara- (§53) adj. ‘how great’; nt. аз sb., ‘how great a thing’: *ciya(n)t-, cf. Skt. kiyat nsn. ‘how much, how many’, + kara- to root kar- ‘make’ ($160.19; Bthl. AiW 597; hardly to kara- ‘time’, cf. hakaram, as taken by MB Gr $293, Hz. ApI 101-3). ciyakaram nsn. (§259) DNa 39; ciyükaram DNb 50; ciyakaram-ca-maiy (written — : -"m*m*eur; $41, $51, $132, $138.I; Lg. 15.178, — | against Hz. ApI 240) DNb 51, 51f. 1
CiSpi- (so Schaeder, SbPAW 1931.641.n4; i Catišpi- acc. to Justi, INB 152, on the evidence of certain spellings in Greek) sb. "Teispes', King of Elam about 610 в.с., ancestor of Cyrus and Darius: Elam. $1-13-рї-1$, АКК. $-4f-pi-i$, Gk. Téergs (S117, 8124.3, §164.V). Стр nsm. (824, §179.IV) DB 1.5°; DBa 8. Cišpãiš gsm. (824, 8179.IV) DB 1.5f; Cišpaiš ($24, S170.IV) AmH 3; DBa 8.
ja*tar- sb. ‘smiter, slayer’: Av. Jantar-, Skt. hantdr-; pIE *g*hen-tor-, agent noun to OP root jan- ($154.11). Jat пзш. ($186.1) DB 4.58, 78.
jad- vb. ‘pray, ask’, with acc. of person and асс. of thing: Av. Jad- (gad-, Bthl. AIW 487), pres. faiya- (§214), Gk. aor. inf. mid. Өёосасдо:, pIE *g*hedh-. — jadiyümiy lst sg. ($226.1) DPd 21; DNa 54; XPh 59; XSc 4.
jan- vb. ‘strike; smite, defeat (enemy ш. battle); mould (brick)’: Av. Jan- (gan-, Bthl. AW
490), Skt. han-, Gk. бере ‘strikes’, dóvos ‘murder’, - |
Lt. dé-fendit ‘wards off’, pIE *g*hen- ($101, $110, 6208); see also jatar-.
јачу (Skt. hánii; 3208, $228.1) DSe 36, 40. ajanam Ist sg. imf. ($110, $122, $208) DB 1.89, 95; 2.69; 4.61; 5.25; XPh 34. аја" imf. (8101, $208) DB 2.26, 36, 41, 46, 55, 61, 87, 98°; 3.7, 18, 39,46,63, 68;.88; 6011) 05634. | ajaniya imf. pass.
LEXICON
(8220) DSf 29, jadiy (Skt. jaht; $101, $122, 8208, 6237.1) 2d sg. шу. DB 2331, 51; 3.15. ја 2d pl. imv. ($208, 5231) DB 2.21, 84; 3.58, 86.
ava- + jan- and ava- + à + jan- ‘smite down, slay’ (apparently ava- in avajata, ара-й- in avàjan- iyà, others ambiguous; cf. §206c, JAOS 62.274): avàjanam 1st sg. imf. ($226.IT) DB 1.57, 59, 73, 83; 2.5; 481; 5.13, 27°. арфа" imf, ($228.IT) DB 1.31 bis; 3.75.  avàjana" За pl. imf. ($208, $232. П) DB 2.13. avájantyü opt. (§206c, $2281, §228.1I) DB 1.51, 52 (858, JAOS 62.274; hardly with Foy, KZ 35.34). avajata nsm. past pte. pass. (8122, §242.1) DB 1.32 (error for avdjata, ace. to Gray AJP 21.13, Bthl. AW 491).
pali- + jan- ‘fight against’: patzyajatà imf. mid. ($140.П1, $208, $235.II) РМа 47.
fra- + jan- ‘cut off’: frájanam lst sg. imf. (§226.11) DB 2.74, 89.
vi- + jan- ‘shatter’: vijaná"tiy 3d pl. subj. ($208, $222.111, §232.1) A’Sa 5°, A?Ha 7° (conj. Kent).
Jav- vb. ‘press forward’:
```


## [2026-09-06T02:15:48.573Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{leaf=0} {n=gsub(/\\f/,\"\\f\"); if(NR==5579) print \"line 5579 is in leaf(0-based)=\"leaf; leaf+=n}' KNT.txt; echo \"---\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt',encoding='utf-8',errors='replace').read()\ni=t.find('drayah- sb.')\nprint('leaf0=',t[:i].count('\\f'))\nEOF"
}
```


## [2026-09-06T02:15:49.158Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN p.37 (leaf 61) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==62' SYN.txt | head -70"
}
```


### [2026-09-06T02:15:50.237Z] TOOL RESULT

```
line 5579 is in leaf(0-based)=215
---
leaf0= 215
```


### [2026-09-06T02:15:52.202Z] TOOL RESULT

```
=== SYN p.37 (leaf 61) ===
en. we- tenas; Alb. wé.
2. IE *akva- or *akwa-. Walde-P. 1.34f. Ernout-M. 64. Walde-H. 1.60. Feist 18 f. Lat. aqua with its Romance derivatives. Elsewhere mostly of ‘run- ning water’ in words for ‘river’, as Goth. ahwa, OF éa, etc. (1.46). Here Hitt. eku-, aku-, Toch. yok- ‘drink’?
3. IK *a@p-. Walde-P. 1.46. Skt. dp-, ap- mostly pl. dpas, used esp. of the per-
ceptions, groups of cog
sonified ‘Waters’, Av. ap-, ap- the reg. word for ‘water’, also freq. personified, OPers. api-, NPers. ab ‘water’. Else- where only of ‘running water’ in words for ‘river’, as Lith. upé, Lat. amnis, Ir. abann, etc. (1.46).
4, IB *wer-. Walde-P. 1.268f. Skt. var-, vari, ‘water’ (of all kinds), Toch. A war, B war ‘water’. Elsewhere in words for ‘rain water, rain’, as Av. var-, ON ar (1.75), or for ‘sea’ or ‘lake’, as Av. vairi-, Lith. jurés, etc. (1.32, 1.33). Also Grk. obpov, Lat. wrina ‘urine’ (cf. NE make water).
5. Miscellaneous:
NG vepé fr. veapov (tdwp) ‘fresh water’, through vypdv (cf. Phrynichus vypdv dep ui) elrgs), with regular change of ir to er (Hatzidakis, Mec. 2.598).
Ir. dobur (rare, but cf. dobur-chu ‘ot- ter’, lit. ‘water dog’), W. dwfr, Br. dour (Celt. *dubro-) : 60Bpis* @4hacoa Schol. Theocer. (prob. Illyr.), Alb. det ‘sea’, and these : W. dwfn, Goth. diups, ete. ‘deep’ (12.67), ChSl. dino ‘bottom’, dibri ‘val- ley’, etc. Pedersen 1.35f. Kretschmer, Glotta 22.216. Pokorny, Z. celt. Ph. 20.513. Otherwise (: Ir. dub ‘black’) Walde-P. 1.840.
Skt. jala-, the commonest word for ‘water’ : gal- ‘drip’, NHG quelle ‘spring’, etc. Walde-P. 1.690 ff.
Skt. ambhas- and ambu- : Grk. duBpos, Lat. imber ‘rainstorm’, Skt. abhra-
‘loud, rainy weather’, nabhas- ‘cloud, sky’, ete. Walde-P. 1.181.
ee. In Public Domain. Gurukul Kangri Collection, Haridwar
(Digitized by Arya Samaj Foundation Chennai andeGangoti }
igitized by Arya Samaj Foundation Chennai and eGangotri
36 SELECTED INDO-EUROPEAN SYNONYMS 1.32 SHA
GAs, 74 Goth. marei Lith. jira (mares) i ee ieee ON haf, ser (marr) Lett. jira NG Oédacca, téAayos Dan. hav (s4) ChSl. morje Lat. mare (aequor, etc.) Sw. hav (sjé) SCr. more It. mare OE s@ (mere, haf) Boh. moje Fr. mer ME _ see Pol. morze Sp. mar NE sea Russ. more Rum. mare Du. zee Skt. sdgara-, samudra-, Tr. muir, fairrge, ler OHG mari, séo etc. NIr.  fatrrge, muir, lear MHG mer, sé Av. zrayah-, OPers. W. mor NHG meer, see (fem.) drayah- Br. mor
‘Sea’ is understood here as covering the most general terms applied to large bodies of water and used in such a phrase as ‘by land and sea’. But between ‘sea’ and ‘lake’ there is no rigid demarcation (ei
```


## [2026-09-06T02:15:58.926Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==63' SYN.txt | head -60"
}
```


## [2026-09-06T02:15:59.622Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==216' KNT.txt | grep -n \"drayah\" -A6 -B3 | head -40"
}
```


### [2026-09-06T02:16:00.521Z] TOOL RESULT

```
ther by size, or as salt vs. fresh water), and the same word or related group may serve for either or both, or shift its pre- vailing application with changed physi- cal conditions. This is notably the case in the Gmc. languages, with the diver- gent distribution of the groups repre- sented by NE sea and NHG meer.
Special words for ‘ocean’ are mostly derived from Grk. dxeards and are not considered here.
The words for ‘sea’ reflect such no- tions as ‘deep’, ‘level’, ‘way’, ‘glisten- ing’(?), ‘salt’, or simply ‘water’,
1. IE *mari (or *mori). Walde-P. 2.234.  Ernout-M. 599. Walde-H. 2.39f. Root connection uncertain, but that with Grk. Hapuaipw ‘slisten’ the most likely. The wide distribution shows the existence of the word in the IE period, but cannot in itself determine whether what was denoted by it in that period was an ocean, or an inland sea like the Euxine or the Caspian, or even a fresh-water lake.
Lat. mare (> Romance words); Ir, muir, W., Br. mor; Goth. marei, ON marr (poet.), OHG mart, MHG mer,
G meer (OE mere rarely ‘sea’, sur- viving in NE mer-maid, but mostly
‘lake’, as also Du. meer) ; Lith. marés (now mostly in names of special seas, as the Black Sea, etc.; NSB s.v.), ChSl. morje, etc., general Slavic.
2. Grk. @4\acca, the main word at all periods, fr. *@4da-x-1a (ef. dadayxav’ $adhaccay Hesych., presumably a Maced. form) or the like : 94Xapos ‘inner room’, 96dos ‘vaulted room’, ChSI. dolt ‘pit’, Goth, dals ‘valley’, ete. Transition from ‘hollow, deep’, to ‘sea’. Cf. Lk. 5.4 els 70 Babos, OE on dypan ‘into the deep’, NE cross the deep, and the gloss 6bBpis: 94Xacca (prob. Illyr.), with Alb. det ‘sea’ : Goth. diups, ete. ‘deep’ (Kretschmer, Glotta 22.216). There is no need to as- sume, as is generally done, that 64racca is of pre-Greek origin. Buck, Class. Studies Presented to E. Capps 42 ff.
Grk. wévros, poet. or of a special sea (wévros  Etitevvos, Tlévros) : Skt. path-, nom. panthds ‘road, way’, ete. (10.71). Specialization of ‘way’ to ‘seaway’, like kehevOos ‘way’ in Hom. bypa xKédevOa, ixBudevra Kédevda, etc. Walde-P. 2.26.
Other poetical expressions are &s ‘salt’ used for ‘sea’; mé\ayos : Lat. planus ‘level, flat’, etc. (12.71) for the (flat sur- face of the) open sea.
3. Lat. (beside usual mare) poet. aequor : aequus ‘level, flat’, and pontus,
pelagus, loanwords fr. Greek.
4. Ir. foirrce, fairrge ‘ocean, sea’ (rare), NIr. Jairrge (Gael. fairge ‘sea’,
esp. ‘stormy sea, surge’, Manx Saarkey),
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
a Se ES
_ Digitized by Arya Samaj Foundation Chennai and eGangotri
| : | | | | |
THE PHYSICAL WORLD IN ITS LARGER ASPECTS 37
now the common generic word (muir prevailing in the name of special seas, as the Irish Sea, etc.) etym. disputed the old comparison with Ir. ferg ‘anger’ and the dxeavds Ovepyotvos of Ptolemy is phonetically difficult. Stokes 273. ’ Ber- gin, Eriu 3.86. Pedersen 2.669 f. Walde- P. 1.289. Perh. best taken as fr. *foirsge : fairsiung ‘wide’ (12.61). So Thurney- sen, Z. celt. Ph. 11.312, Gram. 95.
Ir. ler
```


### [2026-09-06T02:16:02.199Z] TOOL RESULT

```
16-dury, Skt. drógha- droha- ‘(malicious) injury’, pIE *dhrougho-, cf. NGm. Trug ‘deceit’, and OP duruj-, draujana-, draujiya- (870, 576.11, $101, $108.IV, $106, $122, $128, 5132.2, 3, $143.I, V). drauga nsm. DB 1.34, 434; DPd 20. draugà absm. DB 437; DPd 17f.
17-draujana- adj. ‘deceitful’, i.e. ‘adherent of the Lie’: deriv. of drauga- (§101, 5132.2, 5147.1), cf. GAv. drogvant- ‘adherent of the Dru? (Hz. Apl 140-1). draujana nsm. DB 4.38, 63, 68. drauja- nam asm. DNb 12.
18-draujiya- vb. ‘regard as a lie’, denom. to drauga- (S217). [Отау уау 2d sg. subj. (§222.11, §227.1) DB 4.43.
19:drayah- sb. ‘sea’: Av. zrayah-, NPers. dáryà, ·
20-Skt. jrdyas- ‘expanse’, pIE *órejos- (§88, $113, $128, $156.II). Decl, §185.1. See also para- draya. draya asn. DB 5.23; DP
```


## [2026-09-06T02:16:17.674Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i in range(203,220):\n    l=leaves[i]\n    nums=re.findall(r'\\b(1[5-9]\\d|2[0-2]\\d)\\b',l)\n    print(i, l[:60].replace('\\n',' '),'|| nums:',nums[:12])\nEOF"
}
```


### [2026-09-06T02:16:19.259Z] TOOL RESULT

```
203 ted by the OP writing. регу. of Iran. root *kas- (89.V, §87, || nums: ['164', '173', '163', '181', '153', '179', '164', '176', '155', '187', '213', '213']
204 , 66, 70f, 78f, 80, 91, 92; 3.1, 9, 11, 20, 21, 181 28, 29,  || nums: ['181', '171', '191', '182', '181', '162', '187', '210']
205  sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, || nums: ['227', '171', '208', '227', '208', '151', '227', '224', '227', '213', '150', '160']
206 n, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (con || nums: ['183', '161', '165', '179', '173', '217', '217', '184', '182', '225', '187', '205']
207 3f, 57; XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 5.9. Ка& || nums: ['163', '179', '160', '163', '159', '160', '178', '152', '164', '179', '154', '186']
208  Skt. jū- ‘press for- ward, impel quickly, excite, promote’, || nums: ['152', '215', '216', '229', '150', '229', '185', '196', '188', '155', '187', '187']
209 it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI  || nums: ['227', '153', '215', '212', '228', '215', '166', '161', '159', '170', '190', '210']
210 1) XPh 23. tyam asi. DB 4.70f; DPd 7. tya as asf. (856.V) Am || nums: ['187', '165', '158', '161', '204', '167', '167', '215', '222', '224']
211  word of uncertain meaning, Sb 3. Sanuvaniya- sb. ‘bowman’:  || nums: ['155', '188', '213', '220', '181', '222', '227', '203', '164', '154', '161', '165']
212 fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wa || nums: ['209', '218', '228', '160', '181', '154', '172', '164', '168', '152', '164', '216']
213 5-6). Dérayava'u- sb. ‘Darius’ (I, son of Hystaspes, king 52 || nums: ['162', '171', '201', '190', '221', '181', '208', '210', '228', '189']
214 Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42. Daha- adj. ‘ || nums: ['153', '166', '218', '226', '228', '195', '173', '166', '229', '191', '179']
215 rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far a || nums: ['214', '214', '218', '150', '156', '190', '191', '192', '186', '152', '160', '191']
216 e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as g || nums: ['207', '191', '221', '215', '215', '215', '223', '228', '188', '163', '187', '187']
217 n üv-nara- (§142). nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt. || nums: ['185', '191', '152', '194', '151', '214', '208', '226', '214', '211', '220', '218']
218 with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing || nums: ['166', '186', '195', '191', '186', '167', '183', '152', '179', '189']
219 ‘I pierce (as with a spit)’, Gt. faran ‘to travel’. рамо[т-  || nums: ['167', '178', '229', '191', '196', '150', '191', '191', '165', '161']
```


## [2026-09-06T02:16:35.537Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (214,215,216):\n    print('==== leaf',i)\n    print(repr(leaves[i][:300]))\n    print('...')\n    print(repr(leaves[i][-300:]))\nEOF"
}
```


### [2026-09-06T02:16:37.288Z] TOOL RESULT

```
==== leaf 214
'Hz. Ap! 136-8) nsn. as sb. ‘handiwork’, DSe 42.\nDaha- adj. ‘Dahian’; pl., a province of the Persian Empire: АКК. da-a-an, Gk. Aaa (§76.V; Lg. 18.298; Hz. AMI 8.72). Dahà npm. XPh 26.\ndahyu- sb. ‘land, province, district’: GAv. :\ndaltyu-, LAv. dahyu- daiphu-, NPers. dih ‘village’, Skt. ddsyu- ‘strang'
...
'f. dzpim asf. DB 4.42, 48, 70, 73, 77, 89; XV 22, 24. dipiyd lsf. (§179.V) DB 447.\ndug- vb., see hadugá-.\nDubála- sb. ‘Dubala’, a district in Baby- lonia: Elam. du-ib-ba--- ($6, $107). Dubala пет. DB 3.79.\ndūra- adj. ‘far (in time or space)’: Av. düra-, . NPers. dür, Skt. dürd- (5148.1). See also dü'
==== leaf 215
"rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré, LAv. duire, Skt. d'ré; $65, 6191.111) DNa 44. duraty apiy DSe 11, DZe 6, DE 18, XPa 9, XPb 18, XPe 8, XPd 13, XPf 13, XPh 10, XE 18, XV 14, A'Pa 14f°, A’He 17. düraiapiyy DNa 12, dürayapiy DNa 46 ($18, $136).\nduradasa "
...
'a- nam asm. DNb 12.\ndraujiya- vb. ‘regard as a lie’, denom. to drauga- (S217). [Отау уау 2d sg. subj. (§222.11, §227.1) DB 4.43.\ndrayah- sb. ‘sea’: Av. zrayah-, NPers. dáryà, ·\nSkt. jrdyas- ‘expanse’, pIE *órejos- (§88, $113, $128, $156.II). Decl, §185.1. See also para- draya. draya asn. DB 5.23; DP'
==== leaf 216
"e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27) XPh 23.\nnaiy adv. ‘not’: Av. 207, РЫ. në, Skt. ned; :\nfrom pIE *ne, Skt. na, Lt. ne-scio ‘I don't know’, -+ Эа, asn. of pron. i-, Lt. id, OP id-am, ete. (869, 884, $191.1, $291.1"
...
'.88°; 5.12. [ajnaya" 3d pl. imf. ($232.11) DB 5.28. anayatá imf. mid. as pass. ($235.П) DB 1.82, 2.73; 5.26". Some or all of these are possibly ànay-, from à + nay-. | fra- + nay- ‘lead forth, provide’: fránayam Ist sg. imf. ($226.11) DB 1.87.\nnar- sb. ‘man’: Av. Skt. nar-, Gk. дир, cf. Lt. Ner-6; i'
```


## [2026-09-06T02:16:49.087Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nimport re\nfor i in range(174,186):\n    print(i, repr(leaves[i][:150]))\nprint('--- end')\nfor i in range(228,236):\n    print(i, repr(leaves[i][:150]))\nEOF"
}
```


### [2026-09-06T02:16:50.754Z] TOOL RESULT

```
Exit code 1
232
174 'm :\n17 patiyaxsayaly : manā : bajim : abaraha : t\n18 yašām : пасата : aflahiya : ava : akunava : d\n19 абат :tya : mana : avadià : adáraya : Mada\n20 : '
175 'id, until I completed the work.\n&4d. 46-56. Thou who (shalt be) hereafter, if thou shalt think, “Happy may I be when living, and when dead may I be bl'
176 'zSaqam : Ша : атану : kartam\nХоть то XV: The entire line 25 is clearly legible in the photograph reproduced by Lehmann, SbPAW 1900.1.628 Taf. 2.\nTRANS'
177 'this palace, by the favor of Ahuramazda, I after- wards built (to completion).\nA’Sa = ARTAXERXES II, Susa А.\n1 Qty : Artaxfagà : XS : vazraka : XS : X'
178 ' : hya : Dārayavauš : XS : руё : Haxdmanigiya : Mitra : mam : paluv\nNore то АНЬ: Probably the demonstrative imam stood before apadānam at the beginnin'
179 '8. This is the Arab. 19. This is the Egyptian. 20. This is the Armenian.\n21. This is the Cappadocian. 22. This is the Sardian. 23. This is the Ionian.'
180 'd: LX (units) in weight.\n‚.. (= Wb ЕЎ).-\n157\nINSCRIPTIONS ON SEALS SDa = Darius, SEAL A: adam : Darayavaus XS SDb = Darius, SEAL B: adam : Dàrayavaus\n'
181 'sed him, him- self becoming now king in Parsua, later called Ратѕа. Arsames, however, was not put to death, but (as the OP inscriptions tell us) lived'
182 'he field of historical romance. See also PW 3A.710-2, s.v. Smerdis.\nIII. Tae HELPERS or DARIUS\nThe names of the six Persian noblemen who co- operated '
183 'rnment in Media and Persia, gathered an army of Medes and Persians and marched toward Babylon, passing near Elam. As he passed he sent orders to the E'
184 'I re- ject this interpretation of the series of sculptures, since it would oblige us to set the death of Frada at the very end of the series, dating h'
185 'ugh not mentioned in the Behistan inscription, must have followed in the same or the next year.\nV. THE ACCESSION OF XERXES.\nIn XPf, Xerxes gives us an'
--- end
228 'so a province of the Persian Empire, ‘Egypt’; тазе. sg. as sb., ‘Egypt’, a province: Elam. mu-is-sa-ri-ia, АКК. mi-sir (S6, §76.V).\n(1) ‘Egyptian’: Mu'
229 'd sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (O'
230 'am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2.\nгада- sb. ‘wagon’ (570.11, $148.11), see urata-.'
231 '1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi-'
Traceback (most recent call last):
  File "<stdin>", line 9, in <module>
IndexError: list index out of range
```


## [2026-09-06T02:17:30.472Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD zrēh/drayāb ===\"; grep -n -i \"zreh\\|zr[eē]h\\|dray\\|dlyʾ\\|ZRYA\" PHD.txt | head -20; echo \"=== PHD_mackenzie ===\"; grep -n -i \"zreh\\|dray\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-06T02:17:30.543Z] TOOL RESULT

```
=== PHD zrēh/drayāb ===
314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
1210:chatter (v.) drayidan.
2549:lake war, zrēh.
3540:sea drayā(b), zrēh.
3544:sea-shore drayà(b)-bàr.
3760:speak dranjidan, guftan, P wāxtan; (daevic) dawidan, drayidan.
5378:muy! Cst-! éstádant jagar ozan-t ózadant -gar dar, gar yal darr- draya dravābār dravāb draxt darāy
=== PHD_mackenzie ===
2051:dray-, .....,isn, ' v. drayidan.
2052:draya(b) [d1yd'(p) I M dry'b. N daryii(b)] sea.
2054:drayan-Joyisn [d1'd'n ywdfn ] one who speaks while eating.
2057:drayidan / drayistan, dray- [d1'd-ytn , -stn' I M dr'yst, dr'y-, N
5855:l zreh [zlyh I P zryh] sea, lake.
5856:Zzreh [zlyh I N zirih] armour.
5953:and ud, (u-).                             armour zen, zreh, gurdih.
6157:   temar.                               chatter (n.) drayisn.
6158:care for pahrextan.                     chatter (v.) drayidan.
6948:lake war, zreh.                           leek gandaniig.
7510:                                           sea draya(b), zreh.
7514:   omandj v. sorrowful.                    sea-shore drayii(b)-biir.
7658:    (daevic) dawidan, drayidan.           hambasn, hamtan.
10533:druwandih               ~\~        drayidan, grayidan      \,~
10588:drayii                      ~         judan                         \\~tt
10590:drayabiir
10592:drayiib
10606:drayistan
```


## [2026-09-06T02:17:31.681Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB ===\"; grep -n -i \"zr[eēě]h\\|zrayah\\|dray\" NYB_vol2_glossary.txt | head -20; echo \"=== BRT zrayah ===\"; grep -n \"zrayah\\|zrayaŋh\\|zray\" BRT.txt | head -25"
}
```


### [2026-09-06T02:17:31.782Z] TOOL RESULT

```
=== NYB ===
1341:drayäp [dly’p'] the sea 621. 211, 1131, — SW form of Av. (1701 sq.) zrayah (v. zrah, zrài): OP drayah- -+ dp; the com- pound was guite clear to those who created the Aram. expression used later as ideogr. (FrP 3): YMYMY^, i. e. yammé mayyä ‘seas of water’, a purely mechan- ical transposition of dray(ah)-āp ‘sea- waters’. MPrs dry’b (A-H I); Paz. daryäv; Ps. has the bizarre spelling dlyw*w (cf s. v. niyandar); NP daryä.
1744:gurtéh [gwltyh] a part of the warrior’s armour, *neck-protector’ 855. Skr ren- ders the series zen u zréh u ~ by sarva- sannüha- = tavoTaAta. — gurt- < *kur-t- from the root kur- discussed by Bailey, Nyberg Vol. 9-16: Av. (474) kuirit- (< kurit), nom. kwiris, Vd. 14°, following immediately after zräöö (v. zreh) in the enumeration of a Zoroastrian warrior’s armour, is rendered in Phl. by griv-pan ‘neck-protector’ with the gl. han i hac tarak apác 6 zre bast estet ‘that which is attached to the helmet at the back of the armour’. — Cf gri-kaft.
2774:niyandar [nyw’ndl; ny-BYN] inside, within 4216, 934, — Ps. nywndly, v. Barr s. V.; as to the spelling -yw- for -yy- before a vowel v.s. v. apyuxt (add Ps. dlyu”w = driyāv = drayāp, v. Barr s. v.).
3700:tài [D] a) until, b) as long as, as far as: A. prep., local and temporal: ~ [YM? =] rot danbY as far as to the bank of the River P 1:3; — nazd bam until daybreak 53; ~ nun until now 79; ~ sar carm bē haxt stripped his skin up to his head 321-1?; — ka? up to whom (does) Right- eousness (reach)? (— who is the origi- nator of Righteousness ?) 57! ; also govern- ing an inf.: 47M. 779; ~ 3 róc within three days 710; ~ zivandak drahnāt dur- ing the whole lifetime 6514; hac ... ~ from... to: hac pus ~ brat from son to brother, both sons and brothers 221; all men hac 10 säl — 80 sälak from ten to eighty years 20*; passim; — also ~ 6: ~ 6 drayäp 671; ~ 6 3 bar until three times 539-10. =. bē 6 asmün 9218; etc.; — han-tàa, v. this w.; — except(ed): sak ... u dalman ~ apārīk o apāyet xtartan dogs ... and eagles excepted, all the other (animals) may be eaten 9421-22; in frame preposi- tions: bé man ~ an kas nē except myself no one else 157; bē Zartuxšt ~ Z. ex- cepted 9313-14; apar 3 Sap ~ three nights ago 512-3, — B. conj. 1. final: in order that, with pres. ind. passim; with subju.: ~ rasāt 4125-26; m ... bavät 45"; governed by a vb.: framäyet ~ pätifräs . . . kunend
4564:zrāh [zh], zrai [zl?y, zPd] sea 622. 3212-19, 4617, 869-10, 8919, 9316.21.27, _ Av. (1701 sq.) zrayah-; MPrth zryh, zryy, adj. zrhyg; MPrs zryh (S) borrowed from NW, the
4567:authentic SW w. being OP drayah-, BP drayäp (q. v.); Paz. zrih, zreh; NP zurih, zarah. — BP zräi < the cas. rect. zray(ah) with lengthening of -a- after the final syllable had been dropped (then -āy alternating with -āk according to the common rule); zreh < cas. obl. zrayahö (or late *zrayahé) > *zrayah > zreh.
4570:zréh [zlyh], zré [zlyd] armour, harness 69, 2013-14, 8515, 12027, — Arm. lw. zrah-k‘; Syr. lw. zardä ‘coat of mail’, Talm zrd’, Telegdi 243, Arab. lw. zarad-; Paz. z(a)reh ; NP zirih, zarah: all these forms presup- pose *zrdda- and do not tally with Av. (1703) zrača- (Vd. 14? without variant; Phl. Vd. has zrāt evidently through the influence of the Av. form). Some im- portance should perhaps be attached to the curious gen. zaradvehe (1703) quoted from a fragment preserved in the Phl Vd. — NP zirih, Paz. zreh perhaps < cas. obl. *zrdóe.
4887:dipi-: dipivar draug-: druxtan draujana-: drdzan drauga-: drčg drayah-: zràh duruva-: druyist duvara-: dar duvitiya-: dit
5493:zrayah-: drayàp, zrah zyā-: zin-
5929:dry?b: drayap
6530:d(a)rog: drog darma(n): darman daru: darok daruand, darvand: druvand daruandi: druvandéh daryäv: drayäp daryös: drigūš dasti: apastčh dastur: dastavar daša(a): daxšak dašt: daštan, dar-: dawar: davr davar: dätavar deh: déh
6950:zarin: zarrén zindaa: zivandak zindan: zčndan zišt: zčšt zivastan: zivistan zreh, zrih: zrah zufaé: zahyäi zufr: ~ Zuhūdaa - Zuhūda | : Yahüd
7096:darayidan: drayitan
7102:daryä: drayäp
=== BRT zrayah ===
3508:•  j.  apa-j-zära-  m.  'Abfluss,  {Wasser)ab- zwejgung'  a)  des  VouruAasa:  srayä  vouru.- kasaya  .  .  yeäke  . .  Aazannm  -ranam  . . kasal  aSsqm  °ranqm  c(&war>.sat»m  ayan.- baranqm..*arihas(a  me  *afi:aAka  Spö 'rö *vt)asaiti  vispJis  aoi  karsvqn  Y.  65.  4  £; —  aija  käu  'rö  bvat  zrayanAs  vouru.- kaiahe  vairil  yH  Aaosravä  nqma  Yt  ig. 56;  —  zrayauhs  vouru.kasahe  ,  .  vTspJ rairi/  a^araiti  vlsp}sca..nimraoi!  vlspSsca srlr!  'äire (AP.)'> \i.8.i,f>;~ katiht kaüht •,lire(XS.)  Ytj.ioi.  b)  der  Ratfka:\ tipa  guoim  'r>m  ra»hayh  Yt/5. 27,  j
4128:•  j.  a-nhaiSya-  Adj.  'unlauter':  °^lm frafravayahi  tUm  yS  ahurS  maxdä  .  .  aoi zrayS  püitihm  "schwemmst  du  ,  .,  was unlauter  ist,  fort  . .  zum  See  .^.i^' V. 5. 76;
4585:•  j,  +antar«.ar98am ''  Adv,  ('zwischen  den Seiten',  sva.)  1) 'innerhalb',  mit  Gen.:  °äjw zrayanhB  V.5.19;  —  ''(am  nmänahe  "V-ff. 33,  Yt./7.6o.  2)  'diesseits':  yas;/  iava masda  kirpnaot  tacar)  *nSit  *tacar>  *'Mm'^ upairi  Avanxsaiüm  "dass  dir  M.  eine Bahn  bereite,  nicht  eine  Bahn  diesseits, (sondern)  Über  dem  Sonnenball"  YL  5, 90.
4678:maca  *frast3niite  .  .  ditSi  °iiye  (NPm.)  .  .  'nyeke  räkWB  V.  7.4.  I  i)  wiederholt *vaäsäz*/ramravainti..vTspa^qmia  aiwi.'  'Aex  eine  .  .  der  andere';  dsityB  *'inyS'^ srurwai/i  (sd.)  K.60;  —  aivB  pants  yB  havam  {^d^  *daityö  ^'inyB^  ya'ia  *va  . . a^ahe  vTspe  'nyalhm  apatitqm  {%A.)  \.y2.  li.107;  P.57;  —  yal  he  pukra  us^zaydi^e 11;  —  ^pasävi^  adam  käram  ..fraisayam  , .  .  tiaisB  'nys  .  .  aat  'iiyB  ,  .  Y.5. 10;  — hyt^  upa  mäm  äkJ* , .  hyJ^  °niyJ'  kärJ'  avi  *'iiy3^^  suruiiraiti  (statt  Du.)  nsil  'inyS ".  .  reliquus  exercitus  . ."  Bh.^.6;  —  eä  'S. 24;  — yay^  osH  'nyS  rasnus  razUtB asti  masyB  ..  an^rn  datpm  ..upairi'tiyai^'W.J^.^'PüZ.  (unvollst  Zitat);  — \,°myam sraväis  .  .  !  .  .  ya'^a  zrayB  vountJtahm '  (näml,  käram)  *ustrabilrim  akunavam upairi  °nyh  äpB  V. §.32{.;  —  vayaol . .  'myahyJ  aspilf^A^ paiiyariayatn^'Acnem^a taratatB  (Stverz.)  'tiysis  (als  APn.)  dämqtt  \  Teil  (des  Heers)  machte  ich  kamelberit- Y.22. 24;usw.; —  \' a^urcrmazdämaiy  upas-  ten  .  ."  Bh.7. 18'';  5. 4;  —  armaeflä  'iiyA
4813:mit  paiti  und  ava  'herabgehen,  -kommen hin  zu  — ',  mit  avi  und  Akk.;  äat  paitt avaiti  . .  tihryS  .  .  avi  zrayd  vourukahm YtÄao.
4958:•  j-i  g-i  P-  'ava-  Pron.  dem.  (fem.  'rJ-)";  einem  erläuternden  oder  ergänzenden  Re- 'jener';  I)  in  starkdeiktischer  Verwendung :  lativ,  i)  adjektivisch:  aom  stänm  yiiii 'jener,  der  dort,  dann',  von  dem  gebraucht, ! //ÄrJ»»  YLÄ50;  —  -ve  sfärö  y5i  Aaptö.- was  dem  Sprecher  entfernter  liegt;  1)  im  iringa  Yt  J2,  28;  29—32,  S.  2.  13  (wo ausgesprochenen  Gegensatz  zu  'a-,  ima-'  aoe)^'*;  —  "ve  strsul  yq  Aaptöiringa  Yt, (usw.),  adjektivisch:  äfl:*Kra*mff2(/J  Ay^  .S.ix;  13.60,  S.  2.  13  (wo  aoe)i^;  — imflm  bümlm  adct''  AyJ'  'vam  asmänam  -vai  karsvan  yal  fradariaßu  vTdmafsu ad^  D.  6.  I,  X.  /.  I,  6.  I,  Ao.  /.  1 ;  —  V.  ig.  39;  39';  —  'i-at  zrayS  yat  vouru- imqmca  zqm  ..  aomca  asmänsm  Yt  y.  kahm  Yti^j.  59;  ^-  aom  gairjm  .  .  yim 'S3>  2; —  aif'fAasca  ztmS 'vaiAhda  ahtS  usLdqm  Yt. /.  28;  —  avqm  vanqm  yqm Y./.16;  —  imqmca  zqm  'vaca  raocä  H. ' saiftaAt  yt/2.27;  —  mazdäi  'rat*'*  xsa- J.16;  yt70.85,89;  —  upa  AvaHj aiMa  "^nm  hyat . .  vaxsat  (sd.)  .  .  Y.^j/.ö;  — wmö  .  .  upa  °V€  stSrS  .  .  upa  aom  man- 1  aoin^  spä<am^  .  .  yä  ml  pasküt  vasaiie lum  Yt  72,22— 28— 33;  —  imat  ««««jm   Yt/4-S8.  2)  substantivisch:  kä  tSm..
5203:•  j.  avi,  aoi  I)  Praen.  1)  mitAkk.;  a)  'auf —  zu,  hin  zu  —  (auf  — ),  advcrsus',  a)  bes. bei  Wörtern  der  Bewegung:  tiltrim  . .  yö .  .  vazsite  'i-i  zrayS  .  .  ya>a  tifrii  yim anhat  irsxsö  .  .  airyd.x^ii>a(  ka>a  garöit x^anvanhtn  'vt  gairjm  YLÄ6;  H.  2.  i6^ Yt.5.85  ('oi),  132J  ('ei),  Ä33',  70.151, ;p.8z  2.  St.,  V,7.i8  PüZ.,  5,19',  <.V.i03, Y.  6^.  3  (°oiy,  —  nä  tai  frasusaiti  haca /qfnavö  raonqm  'vi  bansiiavS  gairinqm V.5.2;  i';  —  ^J  .  .  vTjasnt  vlspais  ''vi karh-qn  Yt/0.89;  64,  72.4*,  7^.94,  Y, O5.I  (Vi),  0,5.5  ('<»■>;  —para.aki  upa.- vazat3uha  °vi  nmärum  ..  V.  22, 7;  13, Y.57.23,  24,  Yt70.3o;  —  urvänB pärayänli '  °i7  ahurahi  .  ,  "vi  atmsanqm  .  ,  °vi'^ \gätvS  .  .  'i'i  gars   nmätam  Y.  1^.32;  —
5210:—  amjianqm  . .  avayatqm  'vi  zao^rh  Yt  ' ;j.84;  —  yai  .  .  frapayemi  'oi  zqm  .  .  ^ VI  nmJrum  Yt.5.63;  A38  ('ff);  —  < :fantß  frapim-aia  'vi  zrayS ..  Yt,  1^.51;  ■ 58;  —  yat  frsyatayat  .  .  'oi  zam  .  .  'ot nmltum  Yt.5.65;  V,22.i9*  {°vi);  —  srTrJ hiltaiti  .  .  kuyäirya  °vi   daiAhul  Yt  Ä  9 ;
6607:zrayJ  vouru-kalim  aps  asti  /lanjaymarwm   daxstanqm    ysi    hmti    a»rahe     mainySus
6862:■rahe  mazdä  Vr.  14.2;  — yeAh! hltqm  äat yesng  (sd)  paitl  vai)hd  mazdä  'rS  vag'iä Y.  27. 1 5 ;  —  äppm  zazahi  tarn  ys  °rS  mazdä zrayaahal ha'a  z'ouru.kas-lt ha'^ra  Täi?mca dunmqnca  V.5.  15;  isf.'.  60;  —  a'iä  Ml (sd.)  °rB  ma-id\  zard^ustr^m  aoaxsayaUa Y.  /2.  S ;  —  ar>dvlm  . .  yahmya  °rS  mazda ivaiiayal  Yt.  5.85;  —  imat  t!  saahat
7279:charakterisirenden  Adj.  (sd.,  auch  fdSt.): vispasca  äpS  yazamaide  ya  z)m3  armaesta (sd.)  *fratat.ear3tasca  (sd.)  *xqnyk  '^raots.- stälasca  par^uya  *v3iryäsca  (sd.)  "alle Wasser  auf  der  Erde  . , :  die  stehenden  und fliessenden,  die  in  Quellen  und  in  Fluss- laufen,  die  Schnee-  und  Regenwasser"  Y. 61^.6;  usw.;  —  vJspä  apd  xä  pttiti '^raotS.- stSiasca  Y.yi.g;  —  sps yal  armal^tayä.. yat  cätayä  uzuityäsca  .  .  yat  sna^ntyaica srasUntyaica  . . yat ß^tat.^antayä'W .  6.^0, 33i  36,  39;  —  äpim*  tacintqm  . .  xayanqm .  .  zrayanqm  .  .  artmaistqm  Yt.6.2;  Y.ig. 26,  Vd.4;  —  caval  nä  apa  (statt  DS.) ''frälat.cartte  .  .  paiti.iaräi  .  .  cval .  .  ape armaisfaya  (statt  DSf.)  .  .  nävayayai  tia ape  ..  ti.66(.;  —  apqm  ..  nävayaiiqm (sd.)  paiti  pintüs  Yt  //.  4 ;  usw.;  —  andvim . .  ye^he  avavat  .  .  äps  lata  (sd.)  ava.- barmle ya%ia  ..  Yt.5.15;  Ä.47; — gairil yS  uiiiä  yim  aiwiid  paoiris  äpS  hqm  gairi- ü(/('(sd.)/(WJ«/JYL/9.66; — spim  laokmta' vaitim  zaranyävaitlm  vihusavaifim  (sd.) V.^.54;  —  ap3mca  haomyqm  {sA.)  Y.  22. 2;  usw.;  — yaSsyatitim  äp^m  *pararihät Y.g.ii;F.4 f.,  V.21;  —  ?iqm.taptibyB  aiwyS caxrare(sii.)  n^r^bydY.  4.46; — apU  ai yaza- maide malkaintllcä  (sd.)  * hsbavaintlicä  . . Y.JÄ3«.  C)  GP.  apqm  mit  napat-m. (sd.,  auch  fdSt.)  Name  einer  Gottheit: apqm  napäs?  tä  apff  ..  vliax/aiti  YtS. $4; usw.  2)  von  bestimmten  Flüssen  oder Seen,  'Gewässer':  andvl  (sd.)  nqrna  äpa (NS.)"'  V.  7. 16;  —  n?mS  artduya  aps  anü- hitaya  Yt  r.  2 1 ;  Y.  6$.  i ,  Ny.  4.  o.  Vr.  1. 5 ; —  *atikäs^a  (näml.  artduyä)  mS *aaatiAä aps  apayiarsY .  65.  i;  5;  —  upa  äp.'myqm vltaaukaittm  Yt5,76;  —  njinB  ape  däit- yayä  (sd.)  Yt./.2i;  5.112,  5,29,  /7.61, V, ig.2;  —  aoi  apjm  yqm  raiakqm  (sd.) Yt.5. 63;  —  haca  apat  kqsaeyät  (sd.)  Yt ig.92,  V.ig.$;  —  a/s  ya  aw^änva  nqma Yt  ig.  62;  —  yazäi  äp^m  frazdänaom  F. 4%.  I,  2  Anhang:  apqm  (näml  ayar^y
7717:Kqsaoya^HümünySit.^^;   zrayD  yat  kqsaim .  .   avi    hm     avi.hantacaiii   .  .    "zica    Yt. IX)-  66  f. VU.  abgekürzt  aus  einem  Komp.  mit  iriü'.
8245:•  J->  S->  P-  UP^  1)  Praea  i)  mit  Akk.; a)  räumlich,  a)  "hin  -  zu':  mi%r)m  yO  .  . fravazaiU  Aaea  karsvar»  yat  arjsaAi  'pa karsvar»  yat  ifaniraitm  Yt  lO.  67;  — "iräyS  °pa  naz'a.paötm  (sd.)  asatUi ..bar^is V.9,11;  Vd.J2;  —  ui'trö  .  .  yS  kapm aipi.spayeiti  spaeitit^m  upa  vayoan»ni Auxmao%re  (sd.)  .  .  YL/4.13;  — para  te gaosp^nta  .  .  hao^asca  . .  *fraisyämaAi  naz- dista  upa  . .  raocä  . .  P.  34.  ß)  'bei, an':  ipanS yöi  hislmte  a:^arö  °pa  ^^anntjm V.  13.28;  —  tqm  yazata  ..  °pa  zrayi^ vouruJcaam  Ytf.iiö;  33,  38,  54,  72,  76, /2.16,  /5. 19,  27,  31';  —  *"/a  *mailUn (sd.)  barfsatiham  ^.3.20;  —  at-a  tu  anya mays  äitt  (sd.)  JasOit  .  .  paoirim  °pa mayiin  ..  tanüm  pairi.yaozdai^ita'^ .<).^\; 31',  Ö.38,  5.54;  —  minum  bara^ ..  aridvl
8355:tf.jo;  —  yS  .  .  °ri  kunartm  (sd.)  manB baraiY.^-].  a)  beim  Kompar.:  CB  asti masyö  . .  aS>M  dät?m  . .  'ri  anyäis  sravSis .  .  mqnaym  bä  . .  ya%a  zrayS  vouru.- iasJun  (aämL  asti  masyö  .  .)  °ri  anya af3  V.5.22C  3)  Praev.  (nur  mit  'ay, ^spä-yK  \y.S.2  lies:  /mW  ,  .  aZsayqn; —  Extr. /— ^  lies:  upatri^äf.]
8465:•  j.  uniyäp-  Adj.  'des  Wasser  sich  weit- hin erstreckt':  zrayaahs  vourukasahe  .  . ja/rahe  'iipaAt''>  \t.8.^6.
9248:sind"  YLi^,3;  —  upa yaozsnta  -na''  zraya  dämattam*k?r>fi.:^arqttt  k:-r?ß paiti  nisri-
9598:•  j.  ka,saoya-"  Adj.  (fem.  'yä-)  ^Werayak- 1 n.  oder  ap-  f.  Name  des  Ä7OTfi«-Sees*' : a:^ar}t»m  s^ar^nS  .  ,  yal  upanhacailt  ys\ avizoät  fraxsayäte  yaia  zrayS  yat  'saim'^  ■ haitumahm  ". .  den  (Jeden)***,  der  von dorther  seine  HerrschaJft  entfaltet,  wo  der . vom  Haitutnant[_-'¥\\iss.)  gebildete  See  K.  1 ist"  Yt. /p.66; — yat  astvat.srilS  fraxiläile' haca  apal  "jacjd^  Yt /p.92*"*'; — yahmät^ *us.sayäiti  saosyas  .  .  haca  apat  °saoyät^ V./5.5"".
10399:.So  die  bestbezeugle  I  csurR;  NA.  V,.4-!.T.  _  zrayai)/,:! 'rahe\X.ig.^\.  a) 'geheimniss- Red.  des  2.  Gliedes?  Im /»ito/.  finden  sich  voll,  wunderbar':  hifUt  anyäsat  asasca  .  . die  Praesenticn  Hliati,  liid/mii  'er  gehl'  und  srirSs'a  'nh'n  V,/.20;  — slära  'rfl(VP,) .'H,7// 'er  trocknet  ein',  -er  vermag'.  a/s"i:iravAs    V.  2/.  13;    —    mi>r)m    ..
10498:\,f).2Z;    —  mi^rS  graiits  upa.tbHtd  YL  !      niit  ä  Kaus.  'aufwallen  lassen':  hg srayS ro.'iS,  19,  39,  43J  23,  98,  \o();  —  ahurahe  ^•rii'iaydli  Yt.Ä3i. (näml.  niii-rahe)  grantahe'^l.i0.i>ii,^%-,\      mit  i'f  Kaus.   'auseinander,  tiberwallen —  varäsahe  ..  grantahe  Yt. /^ig.  lassen':  Jt3  zrayo  viyzr.ioayeiti  Yt.Ä3i,
10517:mit  J  Kaus.  'aufButen  lassen':  ks  zrays äyiärayeiti  Yt. A3:
10541:•  j.  xayana-  Adj.  (fem.  -na-)  'fontanus': apfm  °nqm  . .  apim  zrayanqm  "das  Quell- wasser .  ."  Yt,().2.
11818:mit^J  z  )'hervorfiiessen;  vorwärts,  weiter fliessen':  artdvlm  .  .  yä  amavaiti  /rata- caiti  .  .  aoi  zrayü  . .  V.65.3;  —  äps  yh t^nüt  faiti  /raiaätiH  "^.ßs-y,  —  äänus (sd.) . .  *Jrä  bunat  ta/in/i/QiSi)  Aog.  77
12246:spähe  kihrpa  aurusake  .  .  äal  paiti avaiti  .  .  avi  zrayS  vourukasttn  .  .  ä  äim paüi.yq^  nisdvaraili  daevS  yS  apaoiö aspahe  kfhrpa  iümahe .  .  kam  läcit  bäzus barats  . .  'ryaica  . .  -vasca .  .'täyüitya%ö  . . a    rapi^winfm    srvämm    ä    Mm    bavatli
13285:—  maisrake  sp3ntahi  .  .  'tahe  vidaivahe Y.  /.  13,  Yt.  11.  17,  b)  mit  zardiustray- Adj.  'das  von  Z.  gegebene  Gesetz':  dättm vTdSyüm  .  .  't?m  zara^usiri  Y.  2.  13;  — dälahe  vJdaivahe  .  .  'tahe  zara'kuitrsis  Y. i.  13;  —  kat  'tahe  zard^uärSiS  ^/i.  2;  Yt. //.  3.  c)  mit  vJdaeva-  und  sara'^ustray-: aufm  "hm  yim  vTdöyüm  zara'iustri  upatri anyäi^  sravSil .  .  yd^a  zrayö  vouruAasfM sipairi  anyä  apö  V.5.  23;  22,  24,  25;  — nisbayemi  vafiuhJm  dalHqm  mazdayasnim 'tim  vldöyam  *eara>ustri  V.  ig.  r6;  — 'l,U  Aala.dätäi  vTdaH-äi  "zara'iuüräi  Extr. ';  2,  _yj  —  'ta  (VS.)  haha.däta  vldaiva sara^u/iri  Extr.  4.  c)  I  im  Ap,:  'tarn tyJ*  mana  aitJ*  *aditriy  D.6.3;  —  imä dahyäva*  *tya  manä  'ta  (AP.)  ^apariyäy^ (sd.)  Bh.7.8.  ni)  'Regel,  Norm'  (nur Ableit).
15281:mit  fra  i)  intrans,;  mit  avi  und  Akk, 'hinschwellen,  -fli essen  zu  — ',  Med:  aaat :!fannS  frapinvata  avi  zrayS  vount.kai>m Yt.  ig.  5 1 '',  3)  traps,  'schwellen  machen, zum  Gedeihen  bringen',  Akt.:  yB  yaom kärayeiti..  hB  imam  daSnam . .  frapinaoiti V.J.  31-
```


## [2026-09-06T02:17:50.889Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf146 (p.125) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==147' HRN.txt | head -40; echo; echo \"=== HRN grep dary ===\"; grep -n \"daryâ\\|daryā\\|darjâ\\|darjā\\|zrayah\\|drayah\" HRN.txt | head -20"
}
```


## [2026-09-06T02:17:52.410Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB ===\"; grep -n \"zrayah\\|drayah\\|dary\\|zrāh\\|zrah\" HUB.txt | head -20; echo \"=== SOD zry ===\"; grep -n \"^465 \\|zry\" SOD_pages.txt | head -30"
}
```


### [2026-09-06T02:17:52.592Z] TOOL RESULT

```
=== HRN leaf146 (p.125) ===
- 125 —
wa/. i5ör, sar. öer.
Dazu got. dal 'Thal'; ksl. dolu 'Thar (ITorn, KZ.
32, 589 No. 26).
561. (lerj/ä *Meer; grosser Fluss', jüd.-pors. nxni (Is. 8,
23). '
ap. drayah'^) 'Meer*; aw. zrayah- 'Meer; plilv.
daryapj daryäk (Bund.), ^re; ai. jräyan-,
bei. zirih *Qnell\ zira *Meer (425).
LW. kurd. deryä; af/. daryäh; bei. darya (50);
yidg. däriyow Tluss*.
Die Form deryäb verdankt nur einer Anlehnung an
ah * Wasser ihre Entstehung. Phlv. zful ist entweder
dialektisch oder nur als ursprüngliche und dann weiter
gedrungene Umschreibung von aw. zrayah- anzu-
sehen; np. zeräh ist sicher Dialektforni.
5H2. derriden, deriden 'zerreissen*.
aw. {/'daV'^ dereta- 'spalten'; phlv. darltan bozw.
darritan ; ai. V^dar-^ ddrsi {dpuiti).
kurd. deriyän; af>'. dural; bei. dirag, dirray, n. diray,
dinay (78); sar. z-dard-änam (Caus.).
563. dix, diz, dez-) 'Burg, vergl. dizhäii-^), dlzdär (syr. LW.
n^nn).
ap. didä' Testung', vergl. ncwciduooi^' (No. 279);
aw. daf^za-; phlv. d(i)z (AV. ; Bund.); arm. vergl. dcz
•Jlaufe' (Hübschmann No. 82).
Die neupersischon Formen diz und dcz sind beide
gleich ursprünglich. Ap. dida- steht für dlöä- und
zwar entspricht das ap. d hier einem ar. fA ; in diesem
Falle wird es im Nenpersischen nicht zu y, Ascoli's
Erklärung von np. dwar 'Mauer aus ap. '^didavara-
\Stadtwair ist daher nicht wahrscheinlich, zumal die
ältere Form devar gewesen zu sein scheint, vergl.
No. 599.
») Bartholomae, ZDMa. 46, 29S No. XV.
2) Dez findet sich in einer ganzen Reilie trän soxanisch er
Ortsnamen, die Herr Prof. Nöldeke gesammelt liat und demnächst
anderswo mitteilen wird.
^) Ma\i^rr nl-Umerä.

=== HRN grep dary ===
5043:ap. drayah'^) 'Meer*; aw. zrayah- 'Meer; plilv.
5051:gedrungene Umschreibung von aw. zrayah- anzu-
```


### [2026-09-06T02:17:52.655Z] TOOL RESULT

```
=== HUB ===
2154:561. Aus ap. draya- oder drayah- wurde phi. drayaky
2157:ap. daryah- ware phi. *darydk = dBrdk (vgl. jiid. tat.
2174:*) Im Phi. und Paz. ersoheint daryoi (Min. GH. 55, 8hk. 241,
2435:zrah-fc zu lesen.
4597:jiingerer Zeit zusammenkanien : np. darya *Meer aus *draya,
4598:ap. drayah-; np. zaryun gelbfarbig = zd. zairigaona~.
4715:2reh Min. cap. 43, 7, phi. zrah?, arm. zrah-U, zd. ^^rdda-.
5326:padyavand kraftig H. 269; daya 'Amme H. 539; darya
6138:darya *Meer = ap. drayah-;farhih *fett' = zd.frapi&wo; far-
7028:phi. zrBh, arm. zrah-lc (5. Jhd.) == zd. zrada-, syr. NIIT,
7146:da sie h oder y fiir altes d bieten : zrah-fc = zd.
7844:%as; darj/a *Meer' = ap. dray a- (oder drayah- ZDM6. 46,
7845:298), zd. zrayah-, aber dial, zarah^); 9) ap. adam *ich' —
7917:zrahK 'Panzer, bazuk 'Arm*, vzruk^ vzurk gross', part€z
7944:np. darya 'Meer'
8887:= zd. zairigaona-; adaryun = ddargun *eine Blume*^), eigent-
8891:daryos arm' = daryos aus ^driyos- V ; birydn gebraten' aus
10393:darvBS, daryoi 62, 248.
=== SOD zry ===
4760:332 "wzryy ? M                                                      Hen. Tales. 476.7; EGSii 177n 1
5024:                                                                  azir ©<azrya~ ©intrans. v.; impf. rrHzyr
10519:                                                                   2334 >zryt- S(MD) «* zr>yt-
10542:2337 'zrync- S                        o^J'^ jT O-^ob*;
10543:     (o)zrenc ^zr'yt-, zr'ync-, zrync-                           2348 >zw-       B,S                            Q>fj*j<&-±j
33196:                                                                                                 wrzry B                                oJLfe^^zJ*
34342:         Dhu. 283; abl. wyzr>, C2, 12V17; wyzry(y),             10580 wzn' C         ju^j J-j- ^/^ <? <JJ*)oy{\ i<*~+* U&*+
34345:         2.751; wrzry, TSP 2.87a, wrzrw, TSP p276,
34346:         Dhy. 14, wrzrh, BSTBL, Vim. 27; wyrzry, TSP                  font
36434:          zyart ©<*zgaru =>zy>rt, zyrt, jyrt, 'zy'rt                    zayma- waPe ^zrys-*sy
36802:         STii 4.16, 46                                                     zraxs (zrys-) ©<*uz-raxsa        ^zr*ync-, zrxs-
36806:                                                                              539; zryrstywy TSP 2.526, AVS 73, 78
36809:                                                                           zrayd (zrxt-, }zryt-, zryt-) ©pt. st. ^zr'ync-
36828:      zpart-wat ©ob. -y                                                   zrenc ©<*uz-ranjaya- =»zrync-, >zrync-
36843:                                                       J^(^               zri/£s =^zrys-}sy, zrysty
36847:       BBB pl4a, W-Li 34                                                   TSP 9.104, 131; zryPs\ voc. C2, 51V26, "coming
36850:      zparyak ©f. n.; ob. -y                                              zres ©<*uz-raisaya ©trans, v. ^zrys-1
36857:                                                   <Ja»_^^ l^J&**         zris ©<*uz-risya- ©intrans. v. =*zrys-2
36867:11397 zrys-     B =» zr>ys-
36869:11398 zryt-     B, C «* zr>yt-
36872:11399 zryty C =* zr>yt-
36873:11400 zrywn B                                                         GMS 940; S W, RL 209 n 23; TSP 2.152, 324,
36880:11401 zrywn'k        S                                                Zurvan(M), Brahma(#)
36882:      zaryone        (zrywnyy) ©pi. zrYwnyyt                          VJ 913, 929, 934; TSP 5.100, 11.24; BSTBL, Dhy.
36888:11402 zrywnc        M                                   y^     11416 zrw>pyyy M            (^^U ^l^)Jjy,^       <£ jljjj
36890:       zaryone (zrywnch) ©f. adj. =»zrywn}k
36894:11403 zrywnch         B =» zrywnc
36896:11404 zrywnyy         M «=> zrywn*k
36924:11411 zrnq     C                                 ^>j<ob*i            zrayde (zryty) ©pp.; pi. -f
36929:                                                               11424 zry M                                            L,^
```


## [2026-09-06T02:18:12.941Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '36920,36960p' SOD_pages.txt"
}
```


### [2026-09-06T02:18:13.033Z] TOOL RESULT

```
11409 zrn'kh =* zrn'k*
                                                               11422 zrxt- =* zr'yt-
11410 zrng =» zrnq
                                                               11423 zrxty C                             jl^j <<^U^b*i
11411 zrnq     C                                 ^>j<ob*i            zrayde (zryty) ©pp.; pi. -f
      zrang (zrng)       ^zr'nk*                                     saved
      salvation
                                                                     C2, 61V 21: BSTii 910.51; STi 31.14
      BSTi A26; ob. zrnqy, C2, 57V3
                                                               11424 zry M                                            L,^
11412 zrnyh =» zrnyy                                                 zre ©<Av. zrayah Parth. zryh       ©ace. zryw
                                                                     sea
11413 zrnyy M                       wjc^* j\ m^
      zarne ? (zrnyh) ©Av. zairina ^zrn'k*                           Hen. BSOAS 12, Cosm. 309.22
                                                                                                                    466



 zrync-

 11425 zrync- M, C                                 o>bob*;              nom. sg^ ace. sg. t}m\ gen. sg. mn\ encl. -m,
       zrenc ©<*uz-rincaya—, *uz-ranfaya                                -my =^zw, c'm*, dW, prWCk)
            ^z^ync-, >zrync-                                          C2 gloss. p237-8; STi 5.1, 8.8, 10.13; GMS 85;
                                                                        Sund. AoFviii 1981 p220
          (to)save
          GMS 542, 600, 689; Hen. Tales. 469.7; Sund.           11437 zw C                              **& <6 j\jT <o^
            AoFi 1974, 8R7; C2, 66R1; BSTii 873.1; S W,
                                                                      zaw (5r}w)
            CLI pl81                                                  fame
                                                                     BSTii 88926; Benv. JA 1955, 311; "news,
 11426 zrys-1 M, C, B        o^J'^b ij> j<*ju> <j->^V>-                rumour" C2, 60R26, 68R3
       zres ©inf. -y; impf. zyrys ^zr'ys-1, zyrys-
       (to)destroy, OcOhurt                                    11438 zw- B                                         j^j
       BBB 514, zyrystw, Isg. mid. impf. GMS 381,                     zu(w), zaw 4zw-, jw-, >zw-
         598, 627; TSP 16.27; AVS 128
                                                                      GMS 264, 574; TSP 2.1164, 20.13; BSTBL, Padm.
                                                                      (to)live
 11427 zrys-2 C                          j^l^^jd,                       46
       z(o)ris ? ©<Av. irisant, IE *raizian-y Av.
         uz-rasta Sraz                                         11439 zw-   B                                  y
                                                                      z5 ©<Khot. dro\ Yaghn. darau =»zwy pwny
```


## [2026-09-06T02:18:14.045Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('nleaves',len(leaves))\ni=t.find('11424 zry')\nprint('leaf of 11424 zry =', t[:i].count('\\f'))\nEOF"
}
```


### [2026-09-06T02:18:15.657Z] TOOL RESULT

```
nleaves 645
leaf of 11424 zry = 532
```


## [2026-09-06T02:18:29.014Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==532' SOD_pages.txt | tail -25"
}
```


## [2026-09-06T02:18:30.002Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 305 306 307 308; do echo \"=== v2 leaf $L (printed ~$((L+540))) ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -25; done"
}
```


### [2026-09-06T02:18:30.877Z] TOOL RESULT

```
                                        cTJil'CJJ ^ ^^^
                                                                          zrencak/e
        zpart-watmenc                                                     saviour
        {of the)Uo\y Ghost
        STii 3.35; GMS 1103                                                Mack. AI 25 p425.14
                                                                    11393 zr'ys B
11381 zprtw'xs M
                                                       J^(^               zri/£s =^zrys-}sy, zrysty
      zpart-waxs
                                                                          cessation
      Holy Word                                                                                                                J^
       BBB pl4a, W-Li 34                                                   TSP 9.104, 131; zryPs\ voc. C2, 51V26, "coming
11382 zprty> C, M ^ z^rty*                                                   to an end" n p99
11383 zpry'q C                                                      11394 zr^ys-1 B      o-^ <a>^Vk5 ^^^y^ ti^J'^j^
      zparyak ©f. n.; ob. -y                                              zres ©<*uz-raisaya ©trans, v. ^zrys-1
      honour, reverence                   ©jp^S*                          (/<?)destroy, (r<?)interrupt
        GMS 1110; STi 45.9; C2 gloss. p237; BSTii                         TSP 2227, 1048, 1211, 1216, 6.1139, 9.128, 16.27,
          848.58, 881.16, 888.5, 905, 8, 15, 907.21,                        23.6; BSTBL, Vim. 6, 7, 55, Dhu. 161
          911.57; Sund. AoFviii 1981, 23R11
                                                                    11395 zr}ys-: B            jjii^LS <jxkJtf>> i&£«->\J-
11384 zpry'qyn C                                              f.
                                                   <Ja»_^^ l^J&**         zris ©<*uz-risya- ©intrans. v. =*zrys-2
      zparyaken ©pi. -r                                                   OcObe destroyed, (/^interrupted
      honoured, honourable                                                BSTBL, Dhy. 104, zr>ys>y, 3sg. opt4 TSP 2.745,
```


### [2026-09-06T02:18:32.905Z] TOOL RESULT

```
=== v2 leaf 305 (printed ~845) ===
  ‫دره‬                                                                                                                ‫ز‪6‬ح‬
                                                                                                                       ‫بی‬


 ‫کنابه ازشکم باشد © ‪ -‬و قوس قزح (‪- ۱ )۳‬‬                         ‫بشکل عقرب وببب آن درونج عفربی خوانندش‪.‬‬
 ‫کومان‌حلاجی رانیزکوبندا ؛ وم اول هم‌بدو‬                      ‫کرم وخشك‌است دردویم(‪ ۱)۰‬کز ندکی‌جانورانرا‬
  ‫ون‬
   ‫ک‪۳‬م)ا‬
       ‫معنی آخر است کقهوس قزح (‬                                ‫کوش اکر فدری از آن درمان‌خانه‬                         ‫افع است‬

                              ‫حلاجی ‪ ۷‬باشد ‪#.‬‬                  ‫بیاویزند از طاعون ایمن باشند‪ .‬و اکرسوراخ‬
                                                                ‫کنند ودرمیان هردوران زن حانملدهفآوریززند‬
 ‫درو لزه و درو یره ‪ ۵‬س با زای‬
                                                                                    ‫آن زن از آفتها محفوظ باشد ‪.‬‬
 ‫هوز و زای فارسی ‪ .‬هر دو آمده است برءزن‬
  ‫تحققه (‪ » )4‬بمعنی دربوزه کودایی باشد ‪9.‬‬                     ‫درو ند = بفتح‌اول بروزن فرزند »نام‬
                                                                ‫پهلوانی‌است ‪-‬ودام داروبی‌هم‌هست ‪ - ۱‬وچنکک‬
‫درو یش سلطان دل = شاره‌برور‬                                     ‫وقلاب رانیز کوبند وبعربی‌معالاق خوانند ‪ -‬وم‬
 ‫کاینات است که بیغمیر ما صلوات الهعله وآله‬                     ‫اول بده‌ذهب ونامقید وفاق‌را گویند بزیان زند‬
                               ‫وسلم باشد ‪.‬‬                                                                 ‫ویازند (‪ )۲‬؟ ‪.‬‬
 ‫دره = بفتح اول و تشدید الی» شکنبة‬                            ‫درون ‪۵‬کنآاربهه‌ازیداندرون وکینه‌ور‬
 ‫کوسفند وغیرء باشد ‪ -‬کوشادکی ميان ده کوه‬                                                                    ‫ومنافق باشد ‪.‬‬
‫رکاپریبزند ‪٩‬‏ ؛ویتخفیف ثالی از همین معنی‬                        ‫؛صفر‬
                                                                   ‫‪ -۳‬بروزن عروسك م‬                        ‫وك‬
                                                                                                            ‫نرل‬
=== v2 leaf 306 (printed ~846) ===
   ‫نت‬                                                                            ‫درة آسمان‬
‫همآمده است ‪ -‬و بکراول درفربی آلت ضرب | باشد وآن زرست‌رايج ووزنیاست معروف ‪.۷‬‬
‫بررزن سررشته» بمعنی‌جود‬     ‫رشت‬
                              ‫ه‬ ‫د‬                                              ‫وزدارا گوبند ‪.‬‬
                          ‫در آسمان ‏کنابهازکهکنانانت‪ | .‬وعطا وکرم باشد ‪#.‬‬
‫در هم بقلی ‪ = ۲‬مشهور أست ‪٠‬‏ وآن‬                                    ‫وآارا بعریی مجره خواند ‪.‬‬
‫زری بوده‌منتوب برای ‪,‬هودی کهآ را رای‌الیفل‬        ‫هرام » بروزن فرجام ؛ یمعنی درهم‬
                                                                                ‫د‬
                                     ‫رك‪ :‬بشلی ‪.‬‬    ‫‪۴‬‬         ‫‪ - ۱‬رك ‪ :‬درهم » درم ‪.‬‬

                                                                           ‫شه از صفسه ‪۵6۸‬‬

  ‫‪ #‬درهم ‪ -‬بفتح اول وسوم » از‪ :‬در (حرف اضافه) هم ؛ شوش ‪ .‬مختلط‪ .‬شوریده؛‬
      ‫دلتان ‪. ۳:۰‬‬
                ‫را) ونفی کنند تاچندین دزهم چرا گنت ک‬            ‫اد‬
                                                                 ‫شزیندش‬
                                                                      ‫(ودی‬
                                                                         ‫آشفته‪* :‬ملك فرم‬
          ‫(ك‪ :‬درم) ‪.‬‬
                   ‫وفتح (رکسر) سوم » معرب» واحد كوك نقره و واحد وزن ر‬                  ‫وکل‬
                                                                                         ‫رای‬
                                                                                           ‫م‬
  ‫‪ #‬ورویش ‪ .-‬شنح اول » پپلوی ‪hsöyird‬‏ ( فقیر؛ تھی دست ) « ای ‪> ۲: ۲۷۲‬‬
 ‫رتا‪00‬ع‪ . 120‬بازید ‪ . 05۵67780‬هردواز اوسا ‪« 11081۳-‬بارتولمه ‪ . ۷۷۷‬شک کلمه[ شکر‬
  ‫و رك‪ :‬اسشق وهوبشمان ‪ 4۵۵‬؛ دولف «تفس» اصلآ نرا ”در بیش بمعتی‬             ‫ست‪ .‬رك‪ :‬لبر که‬
=== v2 leaf 307 (printed ~847) ===
  ‫دربا‬                                                                                ‫==‬

‫عالمبدر گاءاومیامدندوزبان‌یکدیگر رالمیفهمیدند‬       ‫میکفتند و آن زر برابربك کف وستی (‪ )۱‬بوده‬
 ‫بهمن فرمود تا داشمندان زبان فارسی را وضع‬          ‫یمتی آلمقدا رکه چون دست راپهن سازند وآب‬
 ‫کردند و آدرا دری ام نهادند یعنی زبالیکه‬                     ‫بر کف دست بربزند پرایر ابستد ‪.‬‬
‫بدرگاه پادشاهان تکلمکنند ‪ ۳‬وحکم کرد تادر‬            ‫دری‪ = ۱‬بفتح اول بروزن پری » لفت‬
 ‫گوبند ؛ و جماعتی‬   ‫تمام عمالكث باين زبان سخن‬      ‫پارسی باستانی است » و وجه نة آلرا بسنی‬
  ‫بررآآند که وضع این زبان در زمان <مشید شد»‬        ‫بفصیح تعبیر کرده‌اند‪ ۱‬وحرلفتی که درآن نتصانی‬

 ‫وبستی دیگ رگوند درزمان بهرام ؛ ودری بدان‬           ‫لباشد دری‌می‌گوند همجو اشکم وشکم ویگوی‬
‫سبب خوانند که هرکس ازخانةٌ خود بیرون آبد‬            ‫ووی و بشنود وشنود اومثال ابنها پی اشکم‬
                                                                                         ‫ک‬
  ‫باین زبان منکلم شود (‪ )۵‬واين وجه خوبی‌تست‬         ‫وبگوی وبشنود دری باشد ؛ وجممی گویند لفت‬
 ‫چه برهر تقدیر کهفرض کنند آدرا واضمی‬               ‫ساکنان چند شهربوده است که آن بلخ و بخارا‬
  ‫میباید ووضع آلرا سببی درکاراست ‪ -‬و منوب‬           ‫وبدخشان ومرو است ؛ و بعضی گوبند دری زبان‬
 ‫پدر کوه را نیز کویند همچو كبك دری و این‬           ‫اهل بهشتاستکه(‪)۷‬رسرل سلی‌افعلیهوآ له(‪)۳‬‬
 ‫باعتبار خوش‌خوانی هم میتوان )‪(٩‬‏ بود که باشد‬       ‫فرموده اند که « لان اهل الجنة عربی او (‪)4‬‬
  ‫" زیراکه بهترین لفات فارسی زبان دری است =‬         ‫فارسی دری » وملاكة آسمان چپارم بلغت دری‬
 ‫وبا بای خطاب بممنی ظرف وظرفیت پاذد ‪۰ ۴‬‬             ‫تکلم میکنند ؛وطایفه‌ای‌بر آشد که مردمان گداره‬
  ‫در یا= ممروف‌است‌وبعریی‌بحرخوانند؟‬               ‫کیان بدان متکم‌میشده‌اند ؛ و گروهی کوبند که‬
 ‫وازد محقفین‌آشاره بذات یال واجب‌الوجود است ‪۰‬‬       ‫در زمان بهمن اسفندبار چون مردم از اطراف‬

            ‫(‪ )۳‬چك‪ :‬مله‌ال لام ‪.‬‬          ‫)‪ (1‬چيك‪ :‬چه ‪۰‬‬           ‫)‪ (۱‬چك‪ :‬بکفدستی ‪.‬‬
          ‫‏(‪ )٩‬چك ‪ :‬متوالك ‪.‬‬          ‫(ه) خم‪ :۱‬حرف زلف ‪.‬‬                  ‫(‪ )4‬چش ‪ :‬و‪.‬‬

=== v2 leaf 308 (printed ~848) ===
       ‫با‪1‬ه‬                                                                                       ‫دریاب‬
‫دبرای بصره «کنابه ازیبالًبز رکه‬                      ‫دیراب ه بروزن غرقاب» درباراگوبند‬
                          ‫پرشراب باشد ‪.‬‬              ‫کبهحبعررخبیواند‪٩‬‏ ‪ -‬وامرازدریافتن وفهمیدن‬
 ‫ذبرای سائله ‪ -‬کنابه از دربانی‬
 ‫است که مروارید داشته باشد ‪ -‬و شراب را یز‬            ‫دریا پار ‪ - ۴‬بابای ابجد (‪ )۱‬بروزن‬
                                          ‫کن‬          ‫پهنادار » دربای برزک رگوایند ‪ -‬و نام شهری‬
 ‫دریای لعل کنابهازیباله وسراحی۔‬                     ‫همهت ‪ -‬وولاسی را نز گوند که مر کناردر با‬
                            ‫وخم پرازذراب باشد ‪.‬‬                                                ‫‪۶.‬‬
                                                                                                ‫باشد ؟ ‪#‬‬
  ‫دریای قبره کنابه از شب تاريك ‪-‬‬                      ‫در باك ‪ = °‬بروزن ومعتی ترباك است‬
                           ‫ودوات پسریاهی باشد ‪.‬‬      ‫که افیون باشد ‪ -‬ودقع کنند؛ زهررا نیز گویند‬
‫در اشم = کنابه از مروارید بزرکه‬                                                ‫ومعربآن تراق است »‪:‬‬
 ‫است که بکدانة تاها در صدف باشد ‪ -‬کونانه‬
 ‫از حضرت رسالت یناه صلوات اه عليه وآله یز‬             ‫دریا «ککشنابه ازشراب‌خواری که‬
                                                                                     ‫‪۰‬‬    ‫شود ‪۹‬‬   ‫دير من‬
                                          ‫‪۰‬‬   ‫هست‬

  ‫در بيخ افتادن ک«نابه ازانت‬                         ‫ددمعتي دربا کش ات که‬       ‫۔‬   ‫در با نوش‬


   ‫ککهسی درمقام خرابی و استیصال کسی شود ‪.‬‬              ‫رود مت‬      ‫اعت که‬      ‫کنابه از شراب خواری‬

                                                                                                   ‫نشود ‪.‬‬
 ‫در بان د ببضرووزلن‌بریدن» بمعنی‬
 ‫درو دن باشد که بریدن غله است‪ - ۷‬وبفتح‌اول‬            ‫دربای اخضر ‪ -‬کنابه از آسمان‬
```


## [2026-09-06T02:18:41.756Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==308' BQT_v2_pages.txt | tail -20"
}
```


## [2026-09-06T02:18:42.899Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 469 470 471; do echo \"=== v2 leaf $L (printed ~$((L+540))) ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt; done 2>&1 | head -80"
}
```


### [2026-09-06T02:18:43.782Z] TOOL RESULT

```
         ‫‪ ۰‬داخل هنی ‪.‬‬    ‫درون هی‬     ‫ی‬                 ‫سی ودو ‪.‬‬    ‫‪ - ۳‬رك‪ :‬مقدمه‪ ,‬ص‪:‬‬
   ‫‪ = ۴‬در باب »در پهلوی ‪ 0812۳1‬از ‪ 02 + * 12۳1‬جزو اول از پارسی باستان‬
                                                                    ‫‪,‬راومتان ‪2۷12۳2‬‬          ‫‪۳‬‬
                                                                    ‫بارتولمه ‪> ۱۰۷۱‬‬       ‫‪«۵72‬‬
                                                                                             ‫—‬
                                                                     ‫بر کت ‪,»۵٩‬بلوچی‏ ‪01712‬‬
                                                                    ‫س(رچشمه )‪(8۲12 ۰‬دربا) ‪.‬‬
                                                                    ‫کردی ع ‪ayred‬‏ ‪ ۰‬اففانی‬
                                                                     ‫‪.‬بلوچى ‪edyrad.‬‏‬        ‫‪4‬‬
                                                                    ‫بودغا ع ‪( ۷01140‬رود) ‪-‬‬
                                                                    ‫رك‪ :‬اسشق و هوشمان ‪۰ ۱۹۵‬‬
                                                                  ‫کیلکی‪ 2‬لاکقافر بزلدی‪.‬بر ای‬
                                                                     ‫و طنزی ‪ ۵.۱ « 2/780‬ص‬
                                                                    ‫‪۵‬ان(بدیل [ بهلا) »‬
                                                                                     ‫ب‬
                         ‫منظرة دربا اثر میناسیان‬                      ‫ورك‪ :‬داگرة المعارف اعلام ‪:‬‬
         ‫و کرخراهی سلامت پر کناراست ۔‬                     ‫پدربا در منافع بیشمار است‬
    ‫«کلتان ‪۰ ۹۳۰‬‬
```


### [2026-09-06T02:18:45.617Z] TOOL RESULT

```
=== v2 leaf 469 (printed ~1009) ===
 ‫زدن‬                                                                                ‫و ‪—| ۵ ۵‬‬




‫چویکی باشد که سنادزهابدان سازنوازند ویعربی‬                                  ‫درخت رگاوند ‪۶.‬‬
                              ‫مراب خوانند ‪.‬‬      ‫زخم بریان س بمعنی دم پفت است‪.‬‬
‫رخناره ‪ = ۴‬بانون پروزن انگاره »‬                                      ‫‪۱‬‬   ‫وآن طعامی باشد معروف‬

      ‫بمعنی زخاره است که شاخ درخت باشد ‪۰‬‬         ‫زخم ناخ د بمنی باناخن رش‬
                                                 ‫ونابه از رفوم منجمان هم‌هت‪.‬‬
                                                                           ‫کردن باشد ک‬

                ‫وبی‌خرد وی‌خود شدن باشد ‪.‬‬



                                        ‫يان بنحم‬

                                                       ‫در زای نقطه دار با دال بی‬
‫بکر اول بر وزن جگر »‬          ‫ردر ‪= ۴‬‬            ‫ردای‪ = ۴‬بکر اول بر وزن فزای »‬
             ‫زدابنده و پاکیزه کننده را گویند ‪ -‬وامر | بمعنی درخور راق وسزاور باشد ‪.‬‬
‫رشن * = بروزن‌بدن‪.‬عمروف است ‪١-‬‏‬                  ‫بابن معنی هم هت بعنی بزدای وپاکیزه ساز‬
‫وکنابه از چیزی خوردن ‪ - ۷‬و مباشرت کردن‬           ‫و زدایدن وصان کردن وبا کیزه ساختن باشد ‪.‬‬

                                              ‫‪۰‬سوند اسم آلت) ‪:‬‬
                                                             ‫‪ -‬از ‪ :‬زخم (پ‬
    ‫رکه بدر آوازش‪.‬‬
                 ‫ناخوشتر از آواز‪ :‬م‬               ‫کفتی رکه جان میگلد زخمه‌ناسازش‬
  ‫«کلتان ‪۲۷‬‬
               ‫رك ‪ :‬از در ‪.‬‬    ‫‪۴‬‬        ‫رك ‪ :‬زدودن ‪.‬‬     ‫‪۴‬‬        ‫‏‪e‬‬
 ‫‪-‬هلوی ‪ 12122‬و ‪ 02682‬از رة ابرانیقدیم ‪. 2421 . [02 -‬ار ‪nag‬‏‬        ‫پ‬
 ‫که ‪ ۸۵۲‬بارسی‌باستان ر‪٫‬عةٌ‏ ‪ 0712032 ۰ [12-‬ک(شتن)‪ .‬هندی‌باستان‬
                                                             ‫د بارتولمه ‪ ۰۹4‬نربب‬
  ‫رثة ‪ ( 4261 . 022 -‬مضروب کردن‪ .‬کشتن ) قس‪ :‬ارمنی ‪( 028‬ضرب ‪ .‬تادب) و‪۳۳6088‬‬
 ‫(مضروب کردن ‪ ,‬كتك زدن) » کردی ‪( 8106012‬زدن (آش)‪ .‬تیر الداختن)» افقانی‪۵۷ |۳202-‬‬
 ‫‪ ..4‬بلوچی ‪ [8202‬و ‪. [18202‬ع ‪ 82022‬ر ‪ . 0821022‬شغنى ‪"1Z - 0۳2‬‏ ‪,‬سریکلی‬
 ‫[‪ « 1۷‬اسنق ‪ ۳۹۰۰‬طبری ‪ ( 20- 72112‬زدن ) « ساب طبری‬                  ‫‪0-102‬‬
                                                                        ‫و ‪12‬‬       ‫‏‪0-2am‬‬
                                                                                      ‫‪2‬‬
  ‫‪ -‬کوفتن» وارد آوردن‌صدمه‪,‬‬             ‫)‪( 2022-80 .‬بزند) ‪.‬‬        ‫ن‬
                                                                   ‫د(‬‫ز‪06‬‬
                                                                       ‫‪» ۶‬گیلکی ‪62‬‬
   ‫‪۳‬ه*‪.‬‬
      ‫ات»ن«‬
          ‫سراتکف‬
               ‫ل‌چ‬
                 ‫ضرب ‪ « :‬ملك فرمود بنزدش (شیاد را ) وفی کنند تا چندین دکرهم‬
                                    ‫‪ -‬اکنونکوبند ‪ :‬کیلاسی( مشروب ) بزیم ‪.‬‬
 ‫‪.‬هلوی ‪ 01522‬ب‪2‬ا‪. 01012‬کردی واففانی ‪ ۰ 0122‬بلوچی‬
                                               ‫اول پ‬                     ‫فمت‪-‬ح‬
                                                                             ‫بزخ‬
                                                                               ‫‪#‬‬
‫‪ 0‬و ‪( 7182‬شمشیر) «استق ‪ ۲04‬ورك ‪ :‬هوبشمان ابضاً ‏ گیلکی ‪ 00122‬؛ جراحتی که‬
                                ‫بوسیلةٌ آلات جارحه با ناخن ودتدان ومافند آن بهم رسد » رش‪:‬‬
         ‫‪.‬‬   ‫که تماید بچشم همردم دوست‬                        ‫ر خم دادان دشمتی شرت‬
 ‫«کلتان ‪۰۲۱٩‬‏ ‪.‬‬
                                               ‫‪ -‬ضرب ‪ ۰‬صدحه ‪ -‬شکستگی ‪ ۰‬کسر‬

=== v2 leaf 470 (printed ~1010) ===
‫—‬        ‫‪۵۵‬‬
                                                                                                      ‫زدوار‬

‫ردو نتن ‪» ۴‬با نون و تای قرشت مر‬                          ‫وجماغ باشد‪ -.‬و چون مرکب شود معنی بیار‬
‫وزن سبوشکن » بلغت زند و یازند (‪ )۱‬بمعنی‬                                                       ‫اهل‬         ‫دارو‬
                                       ‫خریدن باشث ‪.‬‬
                                                          ‫= بر وزن ومعنی‌جدواراست‬         ‫ردوار‪۱‬‬
‫زده ‪ - ۴‬بنتح‌اول وثالی» بمعنی خورده‬                                                  ‫که ماه پروین باشد ‪.‬‬
‫بداتکه ازچیزی خوردن است‪ -‬وآراسته ومزین‬
‫وزینت داده را هم‌میگویند‪ -‬وپبراسته وبربدرا‬                ‫ردودن ‌ ت بکراول بروزن‌فزودن»‬
‫نیز کوبند که از قطم کردن باشد ‪-‬‬
                                                          ‫بمعنیازالهکردن وبالساختن باشدعموماً چنانکه‬
                                                          ‫دل را از غم وآيعنه وشمشیر وامثال آنرا اززدگه‬
‫وهرچیزی کهنه وفرسوده راهمکفته‌اند ‪ -‬وچون‬
‫»مسعتییار دارد ‪.‬‬
               ‫ترکیب کنند بالفظدیگر ب‬                                    ‫واعضنا را اچزرك وملك را از فتنه ‪.‬‬


                                                  ‫بیان ششم‬
```


## [2026-09-06T02:19:05.810Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'زراه' in l or 'زرَاه' in l:\n        print('leaf',i,'printed',i+540)\nprint('---- زره ----')\nfor i,l in enumerate(leaves):\n    if 'زره' in l:\n        print('leaf',i,'printed',i+540, l.count('زره'))\nEOF"
}
```


### [2026-09-06T02:19:07.669Z] TOOL RESULT

```
leaf 13 printed 553
leaf 91 printed 631
leaf 444 printed 984
leaf 472 printed 1012
leaf 473 printed 1013
---- زره ----
leaf 17 printed 557 1
leaf 27 printed 567 1
leaf 39 printed 579 1
leaf 58 printed 598 4
leaf 102 printed 642 1
leaf 122 printed 662 3
leaf 237 printed 777 1
leaf 260 printed 800 1
leaf 299 printed 839 1
leaf 352 printed 892 1
leaf 393 printed 933 1
leaf 394 printed 934 1
leaf 403 printed 943 1
leaf 405 printed 945 1
leaf 473 printed 1013 1
leaf 475 printed 1015 1
leaf 480 printed 1020 1
leaf 481 printed 1021 5
leaf 510 printed 1050 1
leaf 514 printed 1054 2
leaf 526 printed 1066 1
leaf 533 printed 1073 1
leaf 578 printed 1118 2
leaf 653 printed 1193 1
leaf 678 printed 1218 1
```


## [2026-09-06T02:19:12.176Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 472 473; do echo \"=== leaf $L ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt; done 2>&1 | head -90"
}
```


### [2026-09-06T02:19:14.157Z] TOOL RESULT

```
=== leaf 472 ===
    ‫—‬        ‫)‪0‬‬
                                                                                                                       ‫زراوه‬

 ‫ونفس ناطفه ‪ -‬و عقل فلك عطارد ‪ -‬ونورمجرد‪-‬‬                                 ‫تام خوای ابت که آن دونوع میباشد ‪ :‬یکی‬
        ‫وعفل فعال ‪ -‬ورب‌النوع انان وراست کوی‬
                                                                          ‫را زراوند طوبل میگوبند یمتی‌دراز وآترا شجرة‬
‫رالیز گوبن دکه‬               ‫ورردشت‬              ‫و لور ردان باشف ‪۷‬‬        ‫رستم و قتاءالحیه میخوانند » وآن نر باشد و از‬
                      ‫یشرو ویشوایا شس برستان است ‪.‬‬                         ‫انگشت بر گنده‌تر »گرم است در سیمو خشك‬
 ‫زر لك س با ای قرشت بر وزن‬                                                ‫است دردویم ؛ ودیگربرا زراوند مدحرج خوانند‬
‫کل کاو شه‬               ‫وخق‬      ‫باشف ‪۰‬‬          ‫خق‬     ‫آب‬   ‫که ‪۰‬‬   ‫زرد‬
                                                                           ‫است‬     ‫روف‬
                                                                                     ‫عو‬‫مشد‬
                                                                                         ‫بعتی هدور ؛ وآن ماده ای ما‬
                                                                           ‫»آن‬
                                                                             ‫مشامی(‪ .)۱‬بهترین‌آن زرد زعفرانی باشد و‬
                                                       ‫را لیز گفته‌اند‪.‬‬           ‫ودیرم و خشك است درسیم ‪.‬‬
                                                                                                        ‫کرم ادست‬
‫«کر انی فووقانی و لام‬
                    ‫رترلی؟ ب‬                                               ‫زاروه = بروزن کجاوه ‪ .‬پهلوالی است‬
                        ‫‪٠‬‏ زر طلا را گونند ‪۰‬‬            ‫بحتالی رصیده‬


 ‫زرر = بفتح اول وکسر انی و سکون‬
                                                                                       ‫گوبند وبعربی بحر خوانند ‪.‬‬
 ‫‪,‬بك راگوبند و آن پرنده ایت‬
                          ‫جیم فارسی ك‬
                                                                          ‫زراه ‪| ۲‬کفوده ؟ ‪ .‬بفتح همزه‬
 ‫ابی‌و آن دوقم میباشد‪ :‬دری و غیر دری ؟‬
                                                                           ‫وسکون‌کاف وضم فا پروزن افزوده » دربای خزر‬
                   ‫و دری بزر کت از غبر دری میشود ‪.‬‬
                                                                          ‫اکفوده نامآن در با است همحر دربای‬           ‫باشف جه‬

 ‫در جامی »با جیم بر وزن بدنامی‪,‬‬                                                             ‫عمان ودربای فازم وامثال آن ‪۰‬‬

                                         ‫لومی از انگور باشد ‪.‬‬              ‫دکر !ول و الك و سکون‬
                                                                                              ‫زرا لو ب‬
 ‫زجرعفری « بکرنانی» طلای‌خالس‬                                             ‫وبوند را‬
                                                                                 ‫راب‬
                                                                                   ‫حتوانی مجهول وواو » نق‬
                                                                                                        ‫تنی‬
                                                                                                          ‫ثا‬
‫‪:‬‬           ‫پودمنسوب سعفر نامی کهکیمیا کر بوده اڪ‬                                                    ‫گوگ ‪.‬‬
 ‫وبعضی گوبند پیش ازجعفر برمکی زرقلب سکه‬                                   ‫را‬   ‫لب بروزن‌در بان» پیرسالشورده‬   ‫رربان‬

‫او وزير شد حکم فرمود که‬                                ‫میکردند چون‬        ‫گویند؟ ‪-‬ونام‌حضرت ابراهیمعله‌اللام‌است ‪۵‬؛‬
    ‫طلا را خالص کردند و سکه زدند و باو منسوپ‬                              ‫و باين معتی بجای بای ابجد فای سعقص و میم‬
                                                                    ‫قرف‬            ‫نیز آمده است که زرفان وزرمان باشد ‪۰‬‬
                                                                           ‫زر شت ‪٩‬‏ ‪ -‬بشم تای قرشت بوزرن‬
 ‫قطه‌دار وسکون شن وکاف » طلای خالص بی‌غل‬                                   ‫و نفس کل ‪-‬‬      ‫وبمعنی آفربدة اول ‪-‬‬    ‫‪۰‬‬    ‫ازنگشت‬


                                                                                            ‫(‪ )۱‬چش ‪ :‬بشاحی ‪.‬‬

             ‫اوستابی ‪2122‬‬                ‫‪۴‬‬                    ‫‪( 62100101510=2 ۱‬فر) « لك ‪ ۷‬ص ‪. » ۳۰۲‬‬
        ‫‪.‬‬    ‫‪ :‬اکفوده‬       ‫رك‬   ‫‪۴‬‬                     ‫(دربا) " پپلوی ‪ , 872‬بلوچی ‪ « 2۳12‬اسشق ‪۱٩۵‬‏ > ورك ‪ :‬درما ‪.‬‬
     ‫برائر وفق دادن نابجا‬                    ‫‪۴‬‬               ‫وك ‪ :‬زر » زال ‪۰‬‬
                                                                           ‫‪ - ۴‬مصحف «زرمان » (ه‪.‬م‪ ).‬ر‬
    ‫و تخلیط افکارابرالی بامعتقدات واساطیر سامی «زروان» ( که بهزر مان‌وزر بان صحصف شده) باابر اهیم‬

        ‫‪.‬‬      ‫زارت‬     ‫‪.‬‬    ‫زردشت‬   ‫‪:‬‬   ‫رك‬        ‫‪-‬‬   ‫‪۱‬‬            ‫‪. ۶۱۱‬‬
                                                                        ‫‪:‬زدستا ص ‪- ۳۱۱‬‬
                                                                                     ‫یپکنیداشته شده ‪ .‬رلا م‬
            ‫رکه ‪ :‬زرد کت » زرده‪.‬‬                 ‫‪۸‬‬               ‫ليه این معالی محمول است‪ .‬رك ‪ :‬زردشت‪.‬‬         ‫‪۷‬‬

                                                             ‫‏‪ ٩‬صحیح زر طلی وزر طلا است ‪ .‬ر کت‪ :‬زر طلی‪.‬‬

=== leaf 473 ===
       ‫زردشت‬                                                                        ‫‪۱‬‬

                            ‫ابتاده عبادت کرد ‪۰.‬‬                             ‫وغش راکونند ‪#. ۱‬‬
  ‫زرد خی بفتح اول وخای نقطه‌دار بر‬                ‫ازرداب ‪ - ۲‬بارالابجدبروزن غرقاب»‬
  ‫وزن مردرو » دام کیاعی است که بشتر در باغات‬      ‫نخالمطی است که بعربی صفرا کوبند ‪ -‬و آبی‬
                ‫روید و کلی زرد وخوشبوی دارد ‪.‬‬     ‫ککهااجزکیلره بوقت شستن آن برمی‌آید =‬
  ‫ررد رخ کنابه از شرمنده و متفعل‬                      ‫کوتایه ازشراب زعفرانی رنگه هم عدت ‪.‬‬
      ‫یه تارزسنده وترسناك همهست ‪.‬‬
                                ‫او‬‫کشدن ‪-‬‬
                                       ‫با‬         ‫ررذاب رهز ‪-‬کنابه ازخرن ریختن‬
  ‫زرد ساٹ مھ بکسرثالت وسین یی‌نقطه‬                ‫باشد ‪ -‬و کنابه ازغصه کردن وبدخویی لمودن ‪-‬‬
       ‫یی باآشدنکرها‬
                   ‫ا»‬‫لال‬
                       ‫طحد‬
                         ‫بالف کشیده و فت‬          ‫ودل‌خالی کردن از فهرونغضب هم‌هست‪ -‬وشخصی‬
                       ‫باشند‪۰‬‬   ‫لو ازکان وره‬
                                                          ‫که بدخوبی وقهر و غضب ونصه کند ‪.‬‬
      ‫د طلای دست‬       ‫افثار‬    ‫رردست‬
  ‫افشار مشهور است که خسرو پرویز داشت ومانتد‬
                                                  ‫زردان ‪ ۴‬بروزن مردان ‪ .‬یکی از‬
                                                   ‫اکابر مجوس امت واهل‌او را زردانیه ‪ ۴‬گوننده‬
      ‫موم ارم میشد و هرصورتی که از آن میخواست‬     ‫ئت که بزدان اشضاص مار از‬     ‫واعتقاد اشان آ‬
```


## [2026-09-06T02:19:57.574Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON_part1 دریا ===\"; grep -o \"دریا[^ ]* *\\[[^]]*\\][^.]\\{0,120\\}\" MON_part1.txt | head -10; echo \"=== MON grep زراه ===\"; grep -n \"زراه\" MON_part1.txt MON_part2.txt | head -5; echo \"=== MON زره ===\"; grep -o \"زره[^ ]* *\\[[^]]*\\][^.]\\{0,100\\}\" MON_part2.txt | head -10"
}
```


## [2026-09-06T02:19:59.426Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD Watkins ===\"; grep -n -i \"jrayas\\|drayah\\|zrayah\\|greios\\|expanse\" AHD_watkins1985.txt | head -20; echo \"=== IEC Mann ===\"; grep -n \"jrayas\\|zrayah\\|drayah\\|grei\" IEC.txt | head -20"
}
```


### [2026-09-06T02:20:02.657Z] TOOL RESULT

```
=== MON_part1 دریا ===
ugrep: error: error at position 933
8f][\x80-\xbf][\x80-\xbf]){0,120}
    exceeds complexity limits___/


=== MON grep زراه ===
MON_part1.txt:70846:ژزراه: 2:2 [- زره] (.) دربا؛ بحر. 
=== MON زره ===
ugrep: error: error at position 931
][\x80-\xbf][\x80-\xbf]){0,100}
  exceeds complexity limits___/
```


### [2026-09-06T02:20:02.729Z] TOOL RESULT

```
=== AHD Watkins ===
=== IEC Mann ===
2905:dhighros ‘fixed, certain, right, true’. Cf. dhightos and dhiĝh- Go. *digrs, in digrei ‘abundance’; MHG tiger, tigre ‘entirely’; OFris. diger ‘true, exact’; ON digr, acc. s. digran ‘big, stout; Sw. diger, id.; Ir. déar, déaghair ‘precise, immediate, instant; (Radical probably in Ir. deagh-, cpds. ‘good’:
4295:greg- ‘erode; erosion’ (?) W grai, pl. greioedd ‘blight’; R grëzy ‘deli- rium’; greZu, greziť, v. ‘gnaw’
4296:greiĝ- ‘athwart’. Cf. groig- (2) ON kríkar ‘groin’; Latv. greizs ‘awry’
4301:Tokh. B cf. krámp- (“be restrained" or sim.); NAIb. grémbc, grémg, m. (hook; anchor, fr. *grembhitio-); Ir. greim, pl. greammanna ‘grip, bite’; W grem ‘gnashing’; MHG krimme ‘cramp in bowels’; G cf. Krimmer ‘hawk’? greng- (greng-) (1) ‘plunge’. Cf. grengh- & grenĝos OE crincan ‘fall, succumb, die’; Cz. hřízit ‘immerse’ beside o-gde hroužit, hrouzit, id.; — se ‘sink’ (ambig. cf. grengho (3)) greng- (2) (?) “twist, knot OE crinc “buskin?; Du. cf. krinkel “twist, bend’; E crinkle; Blg. grež ‘knot in wood grenĝos, å, is “dirt, stain’ LG krink, id.; OCS ere, greza ‘mud’; R grjazi ‘mud, dirt’; Cz. cf. vy-hfez ‘excremenť gren£holos, io ‘round object’. See grongholos and next MHG kringel (circle; pretse; ON kringla “disk, circle, orb’; Li. grezule *wagon-pole'. (Variant in Latv. grizulis ‘eddy’, fr. *gringh-) gren£he, ið (1) ‘turn’ ON kringja ‘encircle’; Sw. cf. kring, prp. ‘round’; Li. greZiu, ti, v. “bore; return’, tr.; Latv. cf. gredzens “ring? (?) grengho, ið (2) “press, squeeze’ Fris. kringe, id.; Cz. cf. vy-hfeznout 'cram out (ambig. cf. greng-) Li. greZiu, ti (2) ‘wring’ greného, ið (3) ‘sink, fall’. Cf. greng- (greng-) OE cringan “fall in battle; yield”; cring, m. ‘downfall’; OCS greZo, grezëti ‘plunge, sink’, cf. Pol. gražyć (:OCS groZo, iti; Cz. hroužit, id. and tr. ‘immerse’ from an o-gde root *erongh-); Cz. hiíZit *immerse'; — se ‘sink’; R cf. grjaznut' (‘sink into mire’, influenced by grjazi, see grengos) (Note: Cz. variant hrouzit: hrouZit. A parallel root occurs in Li. gle£ztu, glezti («droop', fr. *gleng-, gleg-) grésó, ið (ghrés-?) *provoke, threaten'. (The evidence is ambig.) Mir gresim ‘urge’; Ir. greisim, greasaim, grío- saim ‘incite’; Li. gresiü, gresti ‘threaten’ greuó, ið “strike, hit, meet, find'. (Li. & Latv. ambig. Cf. ghreu-) Lesb. agréo, Thess. aggréo “take, seize, catch”, cf. agreutós, adj. (/caught', etc.); Lat. gruo, Gre ‘find’; con-gruo ‘meet’; in-gruo, Gre "at,
4313:gribhos, à (2) ‘spike; comb, rake’. Cf. ghrebh-, ghrib-. WP I, 595, 607 & 653-4. (Initial un- certain in Alb. Ir. and Sl.) Gk. cf. agriphée beside agreiphna ‘harrow, rake’; Alb. gribé ‘rake, ornamental comb’ (SI. LW? cf. the EW grebül oke MIr. & Ir. gríobh ‘claw, nail’; Fris. cf. kribje, v. ‘bicker’; LG cf. kribbeln ‘itch, tease; MHG kribeln ‘tickle’; Cz. (ambig.) hřeb “nail? beside hř- bílek ‘currycomb’, hřbet, hfibet ‘backbone’ (but hřeben ‘comb’); OCS cf. grebeni, gs. grebene: Cz. hřeben, where the vowel is Sei
4899:ghreibó, io ‘seize, clutch’. WP I, 647 Go. greipan; MHG sien: OE gripan; ON grípa, id.; Li. griebiu, -^ti, id.
4900:ghreiió (1) ‘grab’. Cf. ghreimn, ghres-, (ghrs-), ghreim- (1) Gk. cf. khráo, fut. khréso (1) ‘seize’, get: Du. graaien ‘filch, scrounge, scrabble’; Li. grieju, -ti (1) ‘grab’; cf. greitas ‘quick’
4903:OE cf. grin ‘snare’; Li. greimas ‘attack’ ghreim- (2) ‘surface, crust’. Cf. ghreiio (2) Gk. cf. khrima (Cunguent,, vbi. n. fr. khrío “touch, rub'); OE grima, m. (*mask, helmet, ghost’; cf. the o-gde form of Gk. khroiá *skin); EME grime “coating of soot, grime'; ON gríma
4904:“mask, visor’; Li. greimas ‘film, top skin (ghreio, ghreiio (?) “requirement, responsi- bility, need, debt, obligation. see ghrées-. The evidence is limited to Gk., cf. khr&, khreía, khreía, f. beside khréos, Do- ric: khréos, id., and khr&me, id. A possible iso- phone is Skt. hràsah ‘decrease, detriment’, of uncertain origin. Per. garàyam = ‘incline, tend' ghrem- (1) ‘roar, rage, rumble’. WP I, 655. Cf. guhrem- and next
4924:ghréso, ið (2), “provoke, threaten?. (Uncer- tain initial, see grésó and cf. ghros-) Olr. gresim, Ir. greisim, greasaim, griosaim (incite! *-e- & Sei Li. gresiü, gresti *threa- ten’; cf. gresme ‘threat’; R cf. grjànut na... “attack?
4955:ghroib- ‘seize; seizure; grasp; span” OHG greiphon; OE grapian, id.; grap ‘seizure, grip’; E grope; CN greip “span; grasp’; OCS cf. sü-grébajg, -ati ‘cramp, squeeze’; Li. graibüs “grabbing, light-fingered'; graibau, -yti ‘seize, scoop’; griebiu, griébti ‘snatch at; grope’, Sw. cf. grep *dungfork', beside grepan ‘handle’. (Li. griebti is ambig. *-ei- or *-oi-)
5527:guhrëið (guhroio) ‘heat, warm; get hot'. Cf. guhrét-, guher-, guhor-, etc. Alb. cf. n-grof, n-groh (^warm', fr. *guhresKo); Olr. grían, f. ‘sun’; W greio, denom. inf. ‘scorch’, fr. *guhroi-; cf. Olr. grís “burning, chafing’; Ir. gríos ('embers, fire, rash’, fr. *guh- rëst-); Br. gruez, f ‘heat’; short vowel in W gwres, id.; W cf. greian ‘sun’; OCS grějọ, gréti ‘heat’. WP I, 688. (For the semantics, cf. Skt. gharmáh "heat": Romani kham ‘sun’
```


## [2026-09-06T02:20:11.802Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ('MON_part1.txt',):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for m in re.finditer(r'دریا\\s*[:.]', t):\n        s=t[m.start()-40:m.start()+200].replace('\\n',' ')\n        print(f, '|', s)\n        print('---')\nEOF"
}
```


## [2026-09-06T02:20:13.385Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'دریا' in l and ('DARY' in l.upper() or 'drayah' in l or 'zrayah' in l.lower()):\n        print('pdf leaf',i,'printed',i+1)\n        print(l[:1500])\n        print('=====')\nEOF"
}
```


### [2026-09-06T02:20:13.415Z] TOOL RESULT

```
MON_part1.txt | استخره آیدان؛ غدبر»  بر که. مرداب. حوض. دریا: بحر. (زم.) تمام  پهنه‌ای که آب آن به یک رود ریزد. (فر ۵.)  ظرف آب و گلاب و عطرهای مایع» آبدان.  خادم حمام که آته دای ست و شه دهن:  آنکه سوراخ و درزهای ظروف فلزی مانند  سماور و آفتابه را با قلعی 
---
MON_part1.txt | ون: متععهه (- آذارافیون) (.)  (جاذ.) کف دریا.   اذاعه: (0-)2220 (ع. اذاعة] (مص‌م.) آشکار  کردن» فاش ساختن» براکندن (خبر).  ادافت: 223۳31 [ع. اداقف-۵] (مسصم.)  چشانیدن» جشاندن. به امتحان دادن چیزی  را. مکافات امری را کردن.   ادالت: 0 (ع. اذا
---
MON_part1.txt | درجه است. (جذ.) بلندی هر  جا نست به سطح دریا. عمق. (شعر) آن  است که صفتی را شروغ کنند و آن را با  اظهار چند چیز بالا برند. ارتفاع صوت:  (ق نع و ا راهان سوت ات ان  ارتفاع غله: حاصل آن» محصول آن»  برداشت غله. ارتفاغ قطب: (نج.) زاویه‌ای  است ک
---
MON_part1.txt | زها. . درهم شدن امواج دریا» جوش و  خروش دریا.   التحاء هه [ع. ف. التحا] (مسص‌ل.)  ریش برآوردن» لحیه پیدا کردن.  التحاد: ۵5 [ع.] (مصل.) از دین  و ی » ملحد شدن» بجسییدن از حق.  التحاق: 2 [ع.] (مص‌ل.) در رسیدن»  ملحق شدن.   التسحام: صقدهااه [ع
---
MON_part1.txt | عر. بست؛» بایین» ز بر ]  (.) ساحل» کنار دریا.   ایرمان: (.) مهمان» سهمان.  ایسرمان‌سرا(ی (2750:-. (امر.)  مهمانخانه» مهمانسرای. خانهُ عاربت. (کند.)  دنیا» این جهان.   ایز: ‏ (تر.] (4.) نشان قدم» اثر پ.   ایزار: ۶۲ (ع. ازار] (۱.) رومال» دستم
---
MON_part1.txt | مشیر» جوهر نیغ.   پلاز: 2 (.) ساحل مسطح دریا. گرمابة  دریایی که جای شناء حمام و تفریح است.   پلاس: 5 (- بلاس» معر.] (ا.) شمینه  ستبر که درویشان پوشند» نوعی از جام‌های    کم بها؛ گلیم درست و سطبرء گلیم بد»    کساء. قسطعه‌ای از بارچه و کهنه. 
---
MON_part1.txt |  کتنته: (جان.) کلنی  حیوانات کسبه تن در دریا. پولیپ بینی: (پز)  غده و بولسی که در داخل حفرة بینی از  رشد غیر طبیعی مخاط داخلی آن بوجود  آید؛ بواسیر لحمی بینی. پولیپ رحم: (پز.)  پولپی که در داخل رحم از رشد غیرطبیعی    مخاط آن بوجود میآیدء بچ
---
MON_part1.txt | . چشم سیاه: چشم سیاهرنگ.  چشم سیل روان: دریا. چشم شادی: چشمی  که از شوق و آرزوی خبری در بریدن باشد.  و ی ی  دید گستاخ» چشم بی‌حیا. ۰ سم مور: چشم  ند که زود اثر کند. . چشم عقل: دیده خرده  چشم باطن. چشم عنایت: دیدة عنایت» نظر  للف. ی او ترا و
---
MON_part1.txt | : ۷ (- دو لای» اف انوس ] (.)   اقیانوس. دریا.   دالبر: 021-۲ [ < دال بر بده» به شکل (۵)   بربده(؟)] (ص‌مف.) (خیا.) قسمی برش که به   شکل کنگرةٌ هلالی در حاشيةٌ جامه‌های زنان   و کودکان و پرده و غیره ایجاد کنند.   دال‌خال: اقباةد [- دار (درخت
---
MON_part1.txt |  درخشنده» درخشان, مانند در: کو کب دری.  دریا: وه [- دریاب] (.) آب زیادی که  محوطهٌ وسیعی را فراگرفته و به اقیانوس راه  دارد» بحر. (تص.) هستی» وجود (فرم. سح .)  دریابار: 0.۲ (امر .) کنار درباء ساحل.  شهری که در ساحل» دریا باشد)؛ بندر. باران 
---
MON_part1.txt |  تاریکی شب  تاریکی شکم ماهی» تاریکی قعر دریا.  (تص.) الف - کدورت طبعی» هوای نفسانی»  خاصیت حیوانی. ب - کدورت‌های طول و  عرض و عمق عالم سفلی.   ظسلمانی: 2010۱-501 [غ.] (ص‌نس.)  تاریکث» تار» تیره. بهترین نوع زمرد و آن  سبر سیر است و خفت وزن و
---
```


### [2026-09-06T02:20:15.157Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T02:20:20.236Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"DARYA\\|daryā\\|drayah\\|zrayah\\|jrayas\" ARY_latin_index_pages.txt ARY_pages.txt | head -20"
}
```


### [2026-09-06T02:20:20.287Z] TOOL RESULT

```
ARY_latin_index_pages.txt:7945:DARYAB, -DARGAY
```


## [2026-09-06T02:20:21.239Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD vol I 660 ===\"; ls | grep -i wld; ls incoming 2>/dev/null | head -30"
}
```


### [2026-09-06T02:20:21.300Z] TOOL RESULT

```
=== WLD vol I 660 ===
WLD_band3.txt
AHD
ARY
BLY
BQT
CEL
FFD
IRN
ISS
KGW
MAG
MFL
MON
OEW
PLA
PRT
_tessdata
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
```


## [2026-09-06T02:20:24.360Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nt=open('ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\ni=t.find('DARYAB, -DARGAY')\nlf=t[:i].count('\\f')\nprint('leaf',lf)\nprint(leaves[lf][:800])\nEOF; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD"
}
```


### [2026-09-06T02:20:26.093Z] TOOL RESULT

```
Exit code 1
leaf 274
[pdf page 275]
ty | We
‘REFERENCES beth (OLD HIGH GERMAN) gS gist
POKORNY ~*~*~S*~*~«S ‘TRIOGAN
BARNHART: yXDREAM) 300 TRUGEN (GERMAN) glJT
4 MACKENZIE: . (LIE) 121 DASTAK ARMENIAN) 5 \
DELAMARRE: (MAIN) 100 AIRDRECH —:(OLD IRISH) op 5432!
BUCK: 1169-1171 MIDDLE IRISH) he 53 p!
MALLORY & ADAMS: + DHROUGHOS AURDDRACH :
ARY-APE seb oy
letlasl
eed at ply gant 358 DREAM 545 AS) DREAM, JS sj} 94 Uber!
. cet le ed a U5 28S cal pF
: 139 6A aS 395 SF: AAT O45 22 Ss cal
Se ___—cmrecai ars
(SANSKRIT) Smile ZRAYAH, ZREH- —{AVESTAN) gus!
JRAYATI, JRAYAS (OLD PERSIAN) ileal sh,
DZOV (asLt}(ARMENIAN) 3) DRAYAHAB, ZREH
(PAHLAVI) «5 34
‘REFERENCES Weetheng ZRAY, DRAYAB, ZREH
OKO S*~*~SL | ERA (RURDISH) «52,5
MACKENZIE: (SEA) 131 {BALUCHD) sa
BUCK: 36-37 ZIRIH, ZIRA.
ary 1gbl dey (AFGHANI) (3-4) gli}
DARYA
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
NameError: name 'EOF' is not defined
```


## [2026-09-06T02:20:32.844Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 -c \"\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(leaves[274][:2500])\n\""
}
```


## [2026-09-06T02:20:33.302Z] TOOL CALL #38: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; echo ---; head -5 /home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt"
}
```


### [2026-09-06T02:20:34.366Z] TOOL RESULT

```
[pdf page 275]
۶ )وا
آلمانی کهن (027۸/49 ۲/07 صران): پسگشت‌ها شید درا
7106۸0 26 امین
آلمانی (7(ف054): لادنی ایا 300 (800 ار بر 270430
ارمنی (714/۷ل/۸70): 2۸87۸ 1 وقاتم مر گنه
ایرلندی کهن (#ذلقا ۵م): ۸7823805 0 (#تهیم :قاط
ایرلندی میانه (بالجا قاططز/م: انااسن اما ۸
۱ ها ۱ ری 15 :کلف ۸ ما تههد
برهان قاطع : ۸۴۳-۴
یادداشت,
۱ به احتمال زیاد واژه‌ی انگلیمی 03۸88 (انگلیسی کهن: نیز از همین واجریشه است.
۷ چم این واژه در زبان ایرلندی میانه: شبح. :
چم این واژه در زبان آلمانی: گول زدن؛ گمراه کردن. :
ی سس هد وروی ویو
اوستایی (/42574): -2861 بقل۸غ 78۸۷ سانسکریت (54۸/5877):
پارسی باستان (22814۸ 0ا0): ۸۸8[ ,ا۸7 م۶[
3 ,08۸۸1138 آرمنی (۸748۸//4/۷)(شاید) 20۷
پهلری (47اتله۴).

7 ,ق8قلا27۸ رتف7 پسگشت‌ها ارخ هراد
کردی (00015): ( 401 ونم
بلوچی (/81-۲767): 1 (هطظق) ار ی

ه 8 ,ق2187 3637 لاه
افغانی (پشتر) (/47017۸7). برهان قاطع ‏ ۸۳۷
6۸3 ,2۸33۸3
لا
```


### [2026-09-06T02:20:34.408Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
---
t—_ . = = — = 2 a 2 i a *
ROvERNMENT OF INDIA 'HZOLOGICAL SURVEY OF INDIA CENTRAL ARCH AOLOGICAL LIBRARY
| ACCESSION NO.90379 |
— = a — =
ALOIS WALDE
```


## [2026-09-06T02:20:39.614Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"zrayah\\|drayah\\|jrayas\\|jráyas\" WLD_Bd1_pages.txt | head -10"
}
```


### [2026-09-06T02:20:39.671Z] TOOL RESULT

```
62530:II 248 ff.); av zrayah-, ap. drayah- „See, Heer", mp. 2 ray. np. (mit Um-
```


## [2026-09-06T02:20:42.471Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '62500,62560p' WLD_Bd1_pages.txt; echo \"=== leaf ===\"; python3 -c \"\nt=open('WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('av zrayah-')\nprint('leaf0',t[:i].count(chr(12)))\n\""
}
```


### [2026-09-06T02:20:44.427Z] TOOL RESULT

```
„zureden, anrufen“, ags. grctan „behandeln, angreifen. zureden, griitien".
ahd. gruo^an m. „anreden, angehn“, nhd. grii/ien gehoren (idg. ghred-) nach
Fick I 4 56, 438, III 4 139, Falk-Torp u. grand (Lit. iiber andere Deutungen
(neben *ghrpd- steht *ghredh- in ags. gresdan „rufen, schreien“, s. Ilolt-
hausen KZ. 48, 239).
    W a d e Etymologisches Worterbuch.
          1           ,                                     I.                             43
                         .




660                                              ghladh      ghleu-


  Wiedemann BB. 27, 238 ff. (Lit.), Uhlenbeck PBrB. 30, 284                              (Lit.);   daB
letztere mit gr. q gd£co zu verbinden seien,                       also idg. g i)i- hatten, ist nicht
                                                                                   l




annehmbar.

ghladh- „glanzend,              glatt“,     s.   unter ghel- ,,glanzen“.


glei- „anlaufen, anstiirmen“?
  Ai. jrayati         „stiinnt        an,   lauft an“, jrdyas n.         „Ungestum, Hast, Anlauf,
Lauf, FluBlauf, Strom“, prthujraya „weit laufend" (s. Geldner Yed. Stud.
II 248 ff.); av zrayah-, ap. drayah- „See, Heer", mp. 2 ray. np. (mit Um-
                  .




stellung)    darya   Hiibschmann Pers. Stud. 62), parathuzruyah „iiber weite
                        (s.

lYasserflachen sich erstreckend" ;   lat. gliscere „unvermerkt zunehmen, an

Starke gewinnen, (vom Feuer) entglimmen", gliscerae mensae gliscentes, id      •




est crescentcs, per instmetionem epularnm scilicet.      Paul. Fest. 70 ThdP.
(? ;
     umstritten s. Yf. LEWb. 2 345, Solmsen Beitr. z. gr. Wortf. 226 ff.; der
gliscere zu gel- „ballen" und Sommer krit. Erl. 56, der es nacb alteren
Vorgangern        —
                  liber die man Vaniiek 2 92 vergleiche     zu ghel- „glanzen“ —
stellt).

   Fiek I 4 52, 216f., 433.
  Nicht zu beurteilen ist das von Fiek herangezogene gr. yki‘ tvxovov, ia-
yvQov lies., fernzuhalten (trotz J. Schmidt Vok. II 331, KZ. 25, 130) gr.
Pgiaooz.


ghleu- „frohlich              sein,    scherzen",         Erweiterung von <jhcl- ,,schreien“ oder
=== leaf ===
leaf0 668
```


## [2026-09-06T02:21:02.417Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (2154,4597,7844,6138):\n    print('--- line',ln)\n    print('\\n'.join(lines[ln-4:ln+8]))\n    # leaf\n    idx=sum(len(x)+1 for x in lines[:ln-1])\n    print('[leaf0=',t[:idx].count('\\f'),'printed=',t[:idx].count('\\f')-10,']')\nEOF"
}
```


### [2026-09-06T02:21:04.142Z] TOOL RESULT

```
--- line 2154
560. Wenn zd. darencL- zur Wzl. skr. dar 'bersten, spalten'
gehort (got. gatalran, hd. zehren, zerren), ware es von
got. dal = hd. Thai zu trennen.
561. Aus ap. draya- oder drayah- wurde phi. drayaky
daraus np. *draya, das mit Umstellung von ra zu ar
(vgl. farman aimframan u. s. w.) zu da/ryd wurde. Aus
ap. daryah- ware phi. *darydk = dBrdk (vgl. jiid. tat.
deiroh 'Meer, Miller p. 65) = np. *dera geworden.
562. Ap. *dartanaiy, pr. *drndmiy (skr. drnCtmi) wurde zu
mp. = *dartan : *dirram (vgl. bal. diray, dinay), daraus
*dartan : darram und mit Neubildung des Inf. naeh
dem Praesens: darrldan (dartdan): darram {dar am).
[leaf0= 72 printed= 62 ]
--- line 4597
impf. agrbaya); ptr alt' = ^piry- = *pirvy- = ^pxvya-
(ap. p(a)ruviya' 'friiher', skr. purvya-) ? Vgl. § 35, a.
Epenthese fand nicht statt, wenn r und y erst in
jiingerer Zeit zusammenkanien : np. darya *Meer aus *draya,
ap. drayah-; np. zaryun gelbfarbig = zd. zairigaona~.
TJeber dih = dth 'Dorf * aus *daAy u. s. w. siehe § 6, c.
§ 9. Ap. a wird zu CL:
a) Ap. -ard = paz. np. -CLl (im alteren Pehlevi ard,
im jiingeren al): sal 'Jahr = paz. sat, phi. sdl, d. i. die
9*— 132 ^
sassanidische Form fiir al teres "^sard =^ arm. -sard (in
navasard etc.), fiir das im urspriinglichen Pehlevi das semi-
[leaf0= 141 printed= 131 ]
--- line 7844
zered'^ zaredaya- (vd. 1,3), skr. Ard-, hrdaya-] 5) d(Js^
Treund' — dostar = ap. daustar-, vgl. zd. zaosa-, skr. y^/s ;
6) dahan 'Mund* = zd. zafan-^ 7) d^, df^ gestern = skr.
%as; darj/a *Meer' = ap. dray a- (oder drayah- ZDM6. 46,
298), zd. zrayah-, aber dial, zarah^); 9) ap. adam *ich' —
zd. a^g;M, skr. aham; 10) ap. adm^ *er nahm' = zd. zinat,
skr. jinati- 11) ap. ayadana- 'Tempel', zd. ya^ Verehren',
arm. yazem opfere , phi. paz. yazisn Terehrung; 12) ap.
gud Verbergen = zd. guz\ 13) ap. dida- Testung', vgl.
np. dizy diz^ dBz *Burg' aus "^diza-y ^daiza-, oben p. 62.
Dazu kommen die Falle, in denen np. I = ap. rd fiir
iran. rz steht: 14) np. gUa 'Klage', paz. gila Min. 61. 90
[leaf0= 230 printed= 220 ]
--- line 6138
der Doppelkonsonanten n ist.
Die Anlautsgruppen drd- und frd- werden im Paz. und
Np. (aber noch nicht im Phi.) umgestellt in dar- und far- :--- 174 ^
darya *Meer = ap. drayah-;farhih *fett' = zd.frapi&wo; far-
zCLna weise* = phi. frazdnak; farzand *Spross' = zd. fra-
zainti- ; farman ^Befehl* = arm. hraman, ap. framanCL- u. s. w.
Vgl. § 3.
§ 63. Der Vokalvorschlag und Einschub ist im Ganzen
eine junge Erscheinung, doch gehen einzelne Anfange bis
ins Altpersische zuriick. Vgl. altpersisch: duruxtam, erlogen ,
adurujiya log*, aber drauga- Xiige*, draujana- Xiigner ;
duruva- *unversehrt* = zd. drva- (d. i. druva-)-, syrisch:
[leaf0= 184 printed= 174 ]
```


## [2026-09-06T02:21:22.314Z] TOOL CALL #42: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T02:21:22.320Z] TOOL RESULT

```


```


## [2026-09-06T02:21:27.068Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%B1%DB%8C%D8%A7",
 "prompt": "Give the full Persian etymology section for دریا (daryâ) 'sea': the Middle Persian form(s) cited, Old Persian, Proto-Iranian and PIE reconstructions, cognates (Avestan, Sanskrit, Sogdian), and any note about metathesis or the -āb element. Quote exactly."
}
```


## [2026-09-06T02:21:28.535Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/dzray%C4%81h",
 "prompt": "Does this Proto-Iranian reconstruction page exist? If so give the reconstruction, meaning, PIE etymon and the descendants list (Avestan, Old Persian, Middle Persian, Sogdian, Persian)."
}
```


### [2026-09-06T02:21:30.368Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T02:21:33.572Z] TOOL RESULT

```
# Persian Etymology for دریا (daryâ)

Based on the Wiktionary content provided, here is the Persian etymology section:

**Middle Persian form:** The entry cites Middle Persian [script needed] (dlydʾp̄ /⁠drayāb⁠/, "sea")

**Old Persian:** 𐎭𐎼𐎹 (d-r-y /⁠draya⁠/, "ocean, sea")

**Etymology structure:** The word combines Old Persian *draya* + Middle Persian *āb* (water element)

**Notable feature:** The entry explicitly states the term is "Inherited from Middle Persian" and traces back through Old Persian, indicating a centuries-long linguistic continuity.

**Limitations of source:** The Wiktionary entry does not provide Proto-Iranian reconstructions, Proto-Indo-European reconstructions, Avestan cognates, Sanskrit cognates, Sogdian cognates, or detailed notes on metathesis. These elements are not included in the displayed content, though categories mention "Persian terms derived from Proto-Indo-European root *h₂ep- (water)" and "Proto-Iranian," suggesting such connections exist in the full etymological framework but aren't detailed in this particular section.
```


## [2026-09-06T02:21:44.476Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%90%8E%AD%F0%90%8E%BC%F0%90%8E%B9",
 "prompt": "Give the Old Persian entry for 𐎭𐎼𐎹 (draya) 'sea': etymology (Proto-Iranian / Proto-Indo-Iranian / PIE reconstruction), cognates listed (Avestan, Sanskrit), and descendants (Middle Persian, Persian). Quote exactly."
}
```


## [2026-09-06T02:21:44.696Z] TOOL CALL #46: WebSearch

```json
{
 "query": "Proto-Indo-Iranian *ȷ́ráyas \"expanse\" Avestan zrayah Old Persian drayah etymology reconstruction"
}
```


### [2026-09-06T02:21:49.648Z] TOOL RESULT

```
# Old Persian 𐎭𐎼𐎹 (draya) - 'sea'

**Etymology:**
The word derives from "Proto-Iranian *jráyah, from Proto-Indo-Iranian *ȷ́ráyas." Related terms include Avestan 𐬰𐬭𐬀𐬌𐬌𐬀𐬢𐬵 (zraiiaŋh, "sea") and Sanskrit ज्रयस् (jráyas, "expanse").

**Descendants:**
The entry shows the term evolved through Middle Persian forms into modern Persian دریا (daryâ). Lurish dialects also preserve related forms: Northern Luri and Bakhtiari both use دریا (diryā). Middle Persian attestations appear in both Manichaean script (𐫅𐫡𐫏𐫀𐫁) and Book Pahlavi script variants.
```


### [2026-09-06T02:21:53.619Z] TOOL RESULT

```
Web search results for query: "Proto-Indo-Iranian *ȷ́ráyas "expanse" Avestan zrayah Old Persian drayah etymology reconstruction"

Links: [{"title":"Reconstruction:Proto-Indo-Iranian/Áryas - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/%C3%81ryas"},{"title":"𐎠𐎼𐎡𐎹 - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%F0%90%8E%A0%F0%90%8E%BC%F0%90%8E%A1%F0%90%8E%B9"},{"title":"Airyanem Vaejah","url":"https://en.wikipedia.org/wiki/Airyanem_Vaejah"},{"title":"Avestan","url":"https://en.wikipedia.org/wiki/Avestan"},{"title":"DARYĀ - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/darya-1/"},{"title":"Airyanem Vaejah - Dharmapedia Wiki","url":"https://en.dharmapedia.net/wiki/Airyanem_Vaejah"},{"title":"Aryan — Grokipedia","url":"https://grokipedia.com/page/Aryan"},{"title":"graphsearch.epfl.ch","url":"https://graphsearch.epfl.ch/en/concept/173578"},{"title":"graphsearch.epfl.ch","url":"https://graphsearch.epfl.ch/en/concept/2359143/concepts?page=2"},{"title":"graphsearch.epfl.ch","url":"https://graphsearch.epfl.ch/en/concept/206341/concepts"}]

Based on the search results, I found relevant information about the etymology you inquired about. The results confirm the connection between these terms related to "water/expanse":

Old Persian drayah-, Middle Persian drayā, and Avestan zrayah- all mean "sea" or "river". These forms reflect a Proto-Indo-Iranian origin, though the search results did not specifically detail the reconstruction *ȷ́ráyas that you mentioned in your query.

The results do show how this etymological family appears in Zoroastrian religious texts. The Avestan term zrayah vourukaša referred to an external ocean encircling the earth, and Airyanem Vaejah means "expanse of the Aryans" or Iranians in Avestan, where the word "expanse" relates to this root.

The linguistic relationship confirms that the Old Persian and Avestan terms share a common Proto-Indo-Iranian ancestor, representing regular sound correspondences between the two ancient Iranian languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T02:21:58.381Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/darya-1/",
 "prompt": "Summarise the etymology given for Persian daryā: Old Persian, Avestan, Middle Persian forms, the -āb element, metathesis, and the word zrēh/zarah. Quote key sentences."
}
```


## [2026-09-06T02:21:59.949Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/jr%C3%A1yah",
 "prompt": "Give the reconstruction, meaning, ancestor (Proto-Indo-Iranian/PIE) and full descendant list (Avestan, Old Persian, Middle Persian, Parthian, Sogdian, Khotanese, Persian). Quote exactly."
}
```


### [2026-09-06T02:22:00.159Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T02:22:02.132Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T02:22:05.810Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%AC%B0%F0%AC%AD%F0%AC%80%F0%AC%8C%F0%AC%8C%F0%AC%80%F0%AC%A2%F0%AC%B5",
 "prompt": "Give the Avestan entry for zraiiaŋh (zrayah-) 'sea': etymology, Proto-Iranian/Proto-Indo-Iranian reconstruction, cognates, and descendants (Middle Persian, Parthian, Sogdian, Persian). Quote exactly."
}
```


### [2026-09-06T02:22:07.443Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T02:22:09.909Z] TOOL CALL #50: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AF%D8%B1%DB%8C%D8%A7' --note 'page 197, root Glei/Greios, node 3: Persian دریا etymology (MP drayāb < OP draya + āb)' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%F0%90%8E%AD%F0%90%8E%BC%F0%90%8E%B9' --note 'page 197, node 1: Old Persian draya- sea, from Proto-Iranian *jráyah, PIIr *ȷ́ráyas' 2>&1 | tail -3"
}
```


### [2026-09-06T02:22:12.365Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/ba4486403eefea4b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dcac08b2ac9b2c52.txt
```


## [2026-09-06T02:22:17.306Z] TOOL CALL #51: Bash

```json
{
 "command": "python3 -c \"\nimport urllib.parse\nfor w in ['𐬰𐬭𐬀𐬌𐬌𐬀𐬢𐬵','زره','زراه','𐫅𐫡𐫏𐫀𐫁']:\n    print(w, 'https://en.wiktionary.org/wiki/'+urllib.parse.quote(w))\n\""
}
```


### [2026-09-06T02:22:19.254Z] TOOL RESULT

```
𐬰𐬭𐬀𐬌𐬌𐬀𐬢𐬵 https://en.wiktionary.org/wiki/%F0%90%AC%B0%F0%90%AC%AD%F0%90%AC%80%F0%90%AC%8C%F0%90%AC%8C%F0%90%AC%80%F0%90%AC%A2%F0%90%AC%B5
زره https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D9%87
زراه https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D8%A7%D9%87
𐫅𐫡𐫏𐫀𐫁 https://en.wiktionary.org/wiki/%F0%90%AB%85%F0%90%AB%A1%F0%90%AB%8F%F0%90%AB%80%F0%90%AB%81
```


## [2026-09-06T02:22:22.778Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%90%AC%B0%F0%90%AC%AD%F0%90%AC%80%F0%90%AC%8C%F0%90%AC%8C%F0%90%AC%80%F0%90%AC%A2%F0%90%AC%B5",
 "prompt": "Give the Avestan entry for zraiiaŋh 'sea': etymology, Proto-Iranian/Proto-Indo-Iranian reconstruction, cognates, and descendants (Middle Persian, Parthian, Sogdian, Persian). Quote exactly."
}
```


## [2026-09-06T02:22:24.341Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D8%B1%D9%87",
 "prompt": "Is there a Persian entry زره meaning 'sea/lake' (zereh), distinct from زره 'armour'? Give its etymology (Middle Persian zrēh, Avestan zrayah-) if present. Quote exactly."
}
```


### [2026-09-06T02:22:28.138Z] TOOL RESULT

```
# Avestan Entry: zraiiaŋh (Sea)

**Etymology:**
The word derives from Proto-Iranian "*jráyah" and Proto-Indo-Iranian "*ȷ́ráyas". It shares cognate status with Persian "دریا" (daryâ), meaning "sea, great river".

**Reconstruction:**
- Proto-Iranian: "*jráyah"
- Proto-Indo-Iranian: "*ȷ́ráyas"

**Note on Descendants:**
The provided Wiktionary entry does not include information about descendants in Middle Persian, Parthian, Sogdian, or other Persian varieties. The page only documents the Avestan noun itself and traces its etymology backward to proto-languages, along with the Persian cognate.
```


### [2026-09-06T02:22:29.310Z] TOOL RESULT

```
# Response

Based on the Wiktionary article provided, **there is no Persian entry for زره meaning 'sea/lake'** listed on this page.

The article only documents زره with two meanings:
1. Armour
2. Coat of mail

The etymology section traces this word back to Middle Persian and Proto-Indo-European roots related to "sound" or "ring," not to any aquatic meaning. No alternative sense referring to water bodies is mentioned, nor are the etymologies you referenced (Middle Persian zrēh or Avestan zrayah-) presented in this article.

To find such an entry, you would need to consult a more comprehensive Persian dictionary or a different Wiktionary source.
```


## [2026-09-06T02:23:03.683Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zrayah-\\|zarayah\\|zaraya\" BRT.txt | head -20; echo \"=== leaf for col 1701 ===\"; python3 -c \"\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nimport re\ni=t.find('zrayah-')\nprint('found at leaf', t[:i].count(chr(12)) if i>0 else 'none')\n\""
}
```


### [2026-09-06T02:23:05.321Z] TOOL RESULT

```
16097:•  j.  parvd'u.zrayah-  Adj.  (auch  fem.) 'Qber  weite  Wasserflächen  sich  erstreckend' : ap3mca  'yaahim  (ASf)  Yt  8.  2.
16434:•  j.  püiti'ka-  Adj.  'zur  Läuterung  dienend', nur  mit  zrayah-  n.  Name  eines  Sees,  des  I Klärbeckens  für  alle  verunreinigtenWasser*':  ■ tä  ha%ra  frafrävayämi  avi  zrayS 'ktm;  K AUtmli  (sd.)  yian.ysanntti  *antan.an^m zrayanhS;  yaozdya  taiinti  äps  zrayarthat  1 kaia  'kSl  avi  zrays  vouru-kaitm  "das (alles)  schwemme  ich  auf  einmal  hin  zum See  P.\  .,  geläutert  fliessen  (dann)  diel Wasser  aus  dem  See  P.  zum  See  F."  V.  | 5. 18  f.  I
28316:•  j,  zrayah-'>,  p.  ''drayah-'*  n.  '(ausge- dehnte  Wasserfläche    sva.)    See,    Meer";
=== leaf for col 1701 ===
found at leaf 505
```


## [2026-09-06T02:23:07.416Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28310,28340p' BRT.txt"
}
```


### [2026-09-06T02:23:07.474Z] TOOL RESULT

```
•  j.  zarammna-  Adj.,  PPM,;  s.  xar-.
•  j.  zaranumana-  Adj,,  PPM.r  s.  xar-.
•  j.  zrayaoha-  m.  EN.  eines  Gläubigen, Bruders  (?)  des  SfifntSjera  (av-  '* :  'yanka (GD.)  sp?nts.xratva  aiaonä  Yty.  115,
Ableit.  aus  zrayaA;  also  etwa  'marüuis'.  ~ ')  Vgl.  Dk,  7-  7-  8
•  j.  zrayana-  Adj.  (fem,  °«J-)  'marinus': äp^m  xayanqtn  .  .  itffm  'nqm  ".  .  das Meerwasser"  Yt.  6.  2,
Ableit.  au$  stayaA-,  etwa  lu  NS.  a-ayö  oder IM  KasusFormcn  nach  der  a-Dekl,  (vgL  p. ärayani)  nach  Mustern  wie  v/üanana-.  —  PQ, : äp  i  zray.
•  j,  zrayah-'>,  p.  ''drayah-'*  n.  '(ausge- dehnte  Wasserfläche    sva.)    See,    Meer";
il  i)  im  Ap.T  intäm  yuviySm  (sd.)  .  .  abiy •ya^  /ya*  hals  parsa''  aifiy  \i.i-j.y,  — abiy  'yam^hS,^^  Bh.5.  4; — ^  im  Gegensatz zum  Festland;  yauna  (sd )  tyaiy  *uikaAyä Uta  tyaiy  *yakya  (LS.)"  D.  5,  a.  a)  tyaiy 'yaiy/f  'qui  in  mar!  (habttant)  sva.  Insel- bewohner' steht  unter  den  Provinzennamen des  Reichs  Darius  I.:  imä  dahyavJ'  . . arabnyt^  mudrsy<^  tyaiy  'yakyä  .  .  Bh. 1. 6.  2)  im  jAw.,  nur  von  bestimmten
Wasserbecken;  a)  mit  vQuru.kala-  (sd., auch  fdSt)  Name  des  Weltozeans:  'yö °s>m  Y.  Ö5. 3  usw.;  —  'yaiahs  *safa  V. 42.4  usw.;  —  'yatahat  kaca  'sätYtS.2^ usw.;  —  'yanhaha  hala  'Ist  Yt  Ä  47 ;  — •^«  (LS.)"  'saya  YL5.38,  ÄS;  —  'yä (LS.)«  •iaya  Y.(5'5.4;  —  ^^  'yH  (näml. °üm)  äyactayati  ¥1.^31;  31^;  —  6u»pm °yanks  (näml.  'sähe)  Yt/5. 51.  b)  mit poitiia-  (sd.)  Name  eines  mythischen  Sees: 'yB  'k)M  V,5. 18;  —  'yarihat  haca  'kät ^■5-  '9J  —  *antar3.ar}'i3m  'jaw/i^  (näml. 'kahe)  V.5. 19.  c)  mit  kasaoya-  (sd.) Name  des  /fJmffm-Sees:  'yS  yat  kasalm Yt  19. 66.
KompE. ;  Ableit.  —  ä.  j'räyai'  n.  'Fläche', mp.  (Pü.)  iray,  np.  daryä  (woiu  Hbm.  PSt 62).  —  ')  So  auch  y.  42. 4  au  lesen,  wo  NA. sarayö  neben  zrayaohö  bietet.  —  ')  NA.  da- ray'.  —  J)  Nach  der  o-Dekl  ;  aber  die  Form ist  nicht  sicher.  —  *)  FrMOllbr  WZKM.  //. 3S6  hat  ZDMG.  46-  298  jedenfalls  nicht  nach- geschlagen. —  i)  Wegen  der  LS.  traya,  srayä (so  Pt4  lu  Y.  55.  4,  F  I  ru  Yt.  J.  4.  *■  3"  J NA.  hat  auch  trayäi),  beides  verderbte  For- men, s.  Bthl.  ZDMG.  43.  668,  4S-  [49-  Anders FoY  IFAni.  3.  18.
•  j.  'zraz-dä-  kompV.  'vertrauen,  glauben'. Praes.  i  zrazda-.  —  Inf.  *sraiäatai-ia.
yä  ml  äamam  .  .  tras'a  dsi'*  apita aotäi  "dass  sie  an  meine  Reli^on  glaube und  sie  begreife"  Yt^.  26.
Aus  ar.  *iri^dhä~  durch  votkietj'mologischen Anschluis  an  sind-  'Heri';  s.  Cld,  KZ.  J/. 272,  woEU  JusTI  NB.  381.  Zur  trad.  Fassung (,  Bthl.  IF,  g,  277.  —  >i,  h-addhä-  'eredere'. —  >)  iTrenn.  s.  RV.  a.  12.  J  (u.  ö.),  ferner □nter  manä-,  mqtdä-,  yaoiää-.
•  g.  *^zraz-dä-''  Adj.  'gläubig,  gläubig ergeben':  ysi  'da  (NT.)  atffiTn  inatdäi "die  dem  M.  gläubig  ergeben  sind"  Y. 31.1.
KompE.;  Ableit  —  Zum  V.  trasda-,  —  au vgl.  iraddha-  Adj.  'credulus'.  —  Pü. ;  ranioi da^H,  SB.:  fravftHdäh.  —  ')  iSchr.  t.  BTHL.
ZDMG.  4S.  149,  Cld.  KZ.  sj-  461.
dby  Google
1703
'daeta-
1704
•  j-,  g.  'zrazdätay-''  i)  f.  'Vertrauen auf  -,  Glaube  an  -';  a)  mit  Akk.  oder Gen.  (obj.):  °ääittm  ma^nm  spjntjm  "den Glauben  an  das  heilige  Wort"  Y.  25.  6;  — 'dälSÜ  ma^rafte  spmtake  V.  22.25.  ^)  ™'^ Inf.:  sadra  mffi  sas  (sd.)  . .  •däUi!  tat vfmyddyai  hyal  .  .  Y.  43.  11.  LS, *'dätal-ca  als  Inf  sbes.  a)  Adj.  (auch fem.)  'vertrauend,  gläubig':  'datüit  aahuyat (sd.)  haca  Yt  10.  9.
Zum  V.  triada:  —  Vgl.  Urasdälay.  EN.  — Pü. :  rmaii  dahünlh.  —  i)  NA.  hat  bald  mrazd', bald  zratd'  (Vt.  14.  2,  Yt.  IQ.  51,  13. 91);  ■-  lu
•  j.  'zrazdätay-  m.  EN.  eines  Gläubigen: 'dätsi^  falsatavAs  asaonH  "des  Zr.,  Sohns des  P.  . ."  Yt  13. 1 1  s.
Vgl.  'ttaxda/ay.
•  j.  *zrazdätae-i-a "  Inf.  'zu  vertrauen auf—,  zu  glauben  an  — ':  yamaheca  hapia-
nhätöis  .  .  gr*  Vr.  1$.  3.
Zum  V.  iroßdä-;  vgl.  xriudälay:  —  Pü. ;  rmaäi  \ dahiinih.  —  <)  So  K;  a;  NA.  taraidälayaHa.  '
•  j.  zrazdä'tama-  Adj.  'der  gläubigste  \ an  — '  (Akk.):  yaäsra  narS  .  .  aiam  h3nti\ 'tgma  ". .  am  gläubigsten  an  das  heilige Recht"  Yt  13.25.  !
Superl.  aus  »'■»mWä-;  s.  äätama: — Vgl.  «»■(«- ;
•  g.  *zrazdiSta-''  Adj.  'der  gläubigste': 3i»/(sd.)  'dtüö  Y.5^.  7.
SuperL  zu  '*zr(adä-%  vgl.  iratdäiima-.  —  Pü.! rawel.  Sä.:  fira^arel  "loU  Torwarts  gehen".  —
```


## [2026-09-06T02:23:28.446Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('PHD_pages.txt',encoding='utf-8',errors='replace').read()\nfor pat in ('drayā(b)','draya(b)','zrēh','zreh'):\n    i=t.find(pat)\n    if i>0:\n        lf=t[:i].count('\\f')\n        print(pat,'leaf',lf,'printed',lf-21)\nEOF"
}
```


### [2026-09-06T02:23:30.123Z] TOOL RESULT

```
draya(b) leaf 48 printed 27
zreh leaf 120 printed 99
```


## [2026-09-06T02:23:30.209Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\nfor pat in ('drayäp [dly','zrāh [zh]','zrāh [z'):\n    i=t.find(pat)\n    print(pat, i, 'leaf', t[:i].count('\\f') if i>0 else None, 'printed', (t[:i].count('\\f')-8) if i>0 else None)\nEOF"
}
```


### [2026-09-06T02:23:32.130Z] TOOL RESULT

```
drayäp [dly 215196 leaf 77 printed 69
zrāh [zh] 784385 leaf 255 printed 247
zrāh [z 784385 leaf 255 printed 247
```


## [2026-09-06T02:23:39.860Z] TOOL CALL #58: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-06T02:23:39.922Z] TOOL RESULT

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


## [2026-09-06T02:23:41.719Z] TOOL CALL #59: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%F0%90%AC%B0%F0%90%AC%AD%F0%90%AC%80%F0%90%AC%8C%F0%90%AC%8C%F0%90%AC%80%F0%90%AC%A2%F0%90%AC%B5' --note 'page 197, node 4: Avestan zraiiaŋh sea, Proto-Iranian *jráyah, PIIr *ȷ́ráyas' 2>&1 | tail -2"
}
```


### [2026-09-06T02:23:43.917Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e2cec638635652e8.txt
```


## [2026-09-06T02:23:48.287Z] TOOL CALL #60: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-124.json'))\nprint(json.dumps({k:v for k,v in d.items() if k!='entries'},ensure_ascii=False))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:2000])\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:2500])\n\""
}
```


### [2026-09-06T02:24:09.502Z] TOOL RESULT

```
{"pdf_page": 124, "book_page": 94, "verified_by": "claude-opus-5", "verified_on": "2026-09-05"}
{
 "entry": 0,
 "root": "Dhě 2",
 "verdict": "confirmed",
 "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)",
 "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.",
 "note_fa": "خودِ ریشه کاملاً درست است: پوک
{
 "id": 1,
 "lang": "Avestan",
 "words": "ma[n]dz-dha; ahura-mazdha",
 "verdict": "confirmed",
 "derivation": "The Avestan words are mazdā- / mazdah- n. 'memory, wisdom' and the divine name ahura- mazdā- 'Lord Wisdom' (Ahura Mazda). The second member really is this root: the compound is Proto-Indo-Iranian *mns-dʰeh₁- 'to set (something) in mind, commit to memory', i.e. *men- 'think' + *dʰeh₁- 'put'; Pokorny treats it under mendʰ- (Page(s): 730): 'Avestan mazda, mazdah- n. „Gedächtnis“, mazdah- m. name of the highest God (*mazdʰa from *mn̥dʰ-ta)'. Nourai's odd transliteration 'ma[n]dz-dha / ahura-mazdha' is copied letter for letter from Klein s.v. Ormazd ('ma(n)dzdha-, ‘wise’, which is a compound formed from the I.-E. bases *men-dh- and *dhe- ‘to put, place’'); the actually attested Avestan spelling is mazdā-, so the -dh- here is Klein's etymologising respelling, not an Avestan form. The gloss 'done learning, wise' and the cross-reference to Men 1 are both correct.",
 "derivation_fa": "واژهٔ اوستایی mazdā- / mazdah- به معنی «خرد، یاد» و نام ایزدی ahura-mazdā- «سرورِ خرد» از ترکیب هندوایرانی آغازین *mns-dʰeh₁- «در یاد نهادن» ساخته شده است؛ یعنی ستاک *men- «اندیشیدن» به علاوهٔ همین ریشهٔ *dʰeh₁- «نهادن». پوکورنی این واژه را در صفحهٔ ۷۳۰ ذیل mendʰ- آورده (نه در صفحهٔ ۲۳۵ که نورایی ارجاع داده). املای غریبِ «ma[n]dz-dha» عیناً از کلاین (ذیل Ormazd) گرفته شده و صورت اوستایی واقعی mazdā- است. در مجموع ادعای نورایی درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Ahura_Mazda",
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-"
 ],
 "ref_check": [
  {
   "ref": "POK:235",
   "status": "partial",
   "note": "POK_full.txt lines 22276-22510: the lemma at 'Page(s): 235-239' is 'dʰe-2, Meaning: to put, place, say' and it does NOT mention mazdā anywhere. Pokorny discusses mazdā s.v. mendh- at 'Page(s): 730' (line 59307: 'Avestan mazda, mazdah- n. \"Gedächtnis\", mazdah- m. name of the highest God (*mazdʰa from *mn̥dʰ-ta)'). The -dhā element is this root, so the claim holds, but the cited page is the wrong one."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "p.730 s.v. mendh- (POK_full.txt line 59307)",
   "stance": "supports",
   "note": "'Avestan mazda, mazdah- n. \"Gedächtnis\", mazdah- m. name of the highest God (*mazdʰa from *mn̥dʰ-ta)' — the compound of *men-dh- + *dhē-."
  },
  {
   "src": "KLN",
   "where": "p.1096 s.v. Ormazd (KLN_1966.txt leaf 586)",
   "stance": "supports",
   "note": "'fr. Avestic Ah
```


## [2026-09-06T02:24:16.002Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zrayah\\|jrayas\\|drayah\" SYN.txt | head; echo \"---leaf63 tail---\"; awk 'BEGIN{RS=\"\\f\"} NR==64' SYN.txt | head -30"
}
```


### [2026-09-06T02:24:17.676Z] TOOL RESULT

```
1249:GAs, 74 Goth. marei Lith. jira (mares) i ee ieee ON haf, ser (marr) Lett. jira NG Oédacca, téAayos Dan. hav (s4) ChSl. morje Lat. mare (aequor, etc.) Sw. hav (sjé) SCr. more It. mare OE s@ (mere, haf) Boh. moje Fr. mer ME _ see Pol. morze Sp. mar NE sea Russ. more Rum. mare Du. zee Skt. sdgara-, samudra-, Tr. muir, fairrge, ler OHG mari, séo etc. NIr.  fatrrge, muir, lear MHG mer, sé Av. zrayah-, OPers. W. mor NHG meer, see (fem.) drayah- Br. mor
1278:Av. zrayah-, OPers. drayah- (NPers. darya ‘sea’ or ‘large river’) : Skt. (Vedic) jrayas- ‘flat surface’ (so BR), in which case one would compare the Iranian use with that of Grk. wé\ayos, Lat. aequor (above), but according to Geldner, Ved. Stud. 2.248 ff., ‘onset, onrush, course’, fr. jri- ‘rush upon’. Walde-P. 1.660.
---leaf63 tail---
 (gen. lir), NIv. lear also ‘flood, surge (of the sea)’, W. llyr ‘flood, sea’ (arch.), beside Iliant ‘flood, stream’, fr. the root in ChSI. lijatz ‘pour’, etc. (9.35). Loth, RC 50.70 ff.
5. The Gme. group, Goth. sazws ‘Jake’, ON seer (sjar, sjor) ‘sea’ (Dan. s¢, Sw. sjé, usually ‘lake’, but also ‘sea’ in phrases), OE s#, ME see, NE sea, Du. zee ‘sea’. OHG séo, MHG sé ‘sea’ or ‘lake’, NHG see fem. ‘sea’, masc. ‘lake’, all fr. a Gmc. *sazwi-, outside connec- tions wholly doubtful. Walde-P. 2.464. Feist 406f. Falk-Torp 1232.
ON haf, Sw., Dan. hav, OF hef (poet. and rare), MLG haf (> NHG haff in specialized application), is the same word as ON haf ‘lifting’ : Goth. hafjan, ON hefja ‘lift’, NE heave, etc. Walde-P. 1.343. Falk-Torp 385.- Development
through the notion of the convex sur- face of the high sea, or, more likely, that of the lifting, surging, of the waves.
6. Lith. jira or pl. jarés, Lett. jura, OPruss. jurin (acc. sg.) : Skt. var-, vari- ‘water’, Av. var- ‘rain’, vazri- ‘Jake’, ON ver ‘sea’ (poet.), OF weer ‘sea’ (rare), ON @r ‘fine rain’, etc. (1.31). Walde-P. 1.268.
7.. Skt. sdgara-, with secondary vrddhi fr. sa-gara-, with cop. sa- and gara- ‘drink, swallowing’, fr. gr- ‘swallow’. Conception of the sea as swallowing riv- ers. Walde-P. 1.682.
Skt. sam-udra- and uda-dhi : udan- ‘water’.
Skt. arnava- (freq. late term for ‘sea’, ef. BR s.v.), sb. of arnava- ‘flow- ing, rising’, fr. arnas- ‘wave, flood, stream’, this fr. 7- ‘move’. Uhlen- beck 18.
Av. zrayah-, OPers. drayah- (NPers. darya ‘sea’ or ‘large river’) : Skt. (Vedic) jrayas- ‘flat surface’ (so BR), in which case one would compare the Iranian use with that of Grk. wé\ayos, Lat. aequor (above), but according to Geldner, Ved. Stud. 2.248 ff., ‘onset, onrush, course’, fr. jri- ‘rush upon’. Walde-P. 1.660.
1.33 LAKE
oF en Goth. saiws, mari-saiws Lith. eZeras oe oa Chi. " us Dan. sf, indsd ChSl. jezero Ay tag Sw 8j6, insj6 SCr.  jezero rr oe OE mere, s@ Boh.  jezero Rum. lac NE tak Russ. aero. Ty. loch (lind) mE ae Skt. sara NIr. loch (Ii on Hess - aed + t (linn) OHG  séo, wac Av — me lyn MHG sé f
é lenn, loc’h, lagenn NHG see (masc.)
ew. In Public Domain. Gurukul Kangri Collection, Haridwar
igitized by Arya Samaj Foundation Chennai and eGangotri
38 SELECTED INDO-EUROPEAN SYNONYMS
The interchange between ‘lake’ and ‘sea’, notably in Germanic, has been dis- cussed under ‘sea’. On the other hand, there is no rigid line between ‘lake’ and ‘pond’ or ‘pool’. Several of the words listed here cover all these, and started from modest beginnings like ‘hole, de- pression’, so that ‘lake’ may be a glori- fied ‘water hole’ or ‘pond’. NE pond (the same word as pound for stray ani- mals) was formerly in New England the usual word for ‘lake’ (the familiar ponds of my boyhood are now mos
```


## [2026-09-06T02:25:39.225Z] AGENT

Now I have everything I need. Writing the verification file.


## [2026-09-06T02:32:58.114Z] TOOL CALL #62: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk197.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_FA  = \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%DB%8C%D8%A7\"\nW_OP  = \"https://en.wiktionary.org/wiki/%F0%90%8E%AD%F0%90%8E%BC%F0%90%8E%B9\"\nW_AV  = \"https://en.wiktionary.org/wiki/%F0%90%AC%B0%F0%90%AC%AD%F0%90%AC%80%F0%90%AC%8C%F0%90%AC%8C%F0%90%AC%80%F0%90%AC%A2%F0%90%AC%B5\"\n\ndoc = {\n \"pdf_page\": 197,\n \"book_page\": 167,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Glei, Greios\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Proto-Indo-Iranian *ȷ́ráyas- n. 'expanse' (> Proto-Iranian *jráyah-); Pokorny 401 'glei- „anlaufen, anstürmen“? Nur indoiranisch'; Kent p.192 pIE *ǵreyos-\",\n   \"note\": \"Both halves of Nourai's root name are real citations, and they are exactly the two pages he gives. POK_02.txt leaf 57 (= p.401) prints 'glei- „anlaufen, anstürmen“? Nur indoiranisch. Ai. jráyati „stürmt an, läuft an“, jráyas- n. „Ungestüm, Lauf, Flußlauf“ ...; av. zrayah-, apers. drayah- „See, Meer“, mpers. zray, npers. (mit Umstellung) daryä ... WP. I 660'; and Kent, Old Persian, p.192 s.v. drayah- has 'Av. zrayah-, NPers. daryā, Skt. jráyas- ‚expanse‘, pIE *ǵreyos-' — that reconstruction is Nourai's second root name 'Greios'. Three qualifications keep this from a straight 'confirmed'. (1) The language label. Pokorny's own note is 'Nur indoiranisch': outside Indo-Iranian the root has no secure witness, so this is a Proto-Indo-Iranian s-stem rather than a demonstrable Indo-European root; Watkins/AHD does not list it at all and Mann's Indo-European Comparative Dictionary has no such lemma (both silent). (2) The spelling with -l-. Pokorny's headword 'glei-' is inherited from Walde-Pokorny I 660, where the lemma still carried Latin gliscere 'unvermerkt zunehmen, an Stärke gewinnen' as its only non-Indo-Iranian member, marked '(?; umstritten)'. Pokorny 1959 dropped the Latin word and wrote 'Nur indoiranisch', but kept the alphabetical spelling, so the -l- is a fossil: the Indo-Iranian evidence (Skt. jr-, Av. zr-, OP dr-) points to *ǵr-, and Wiktionary today reconstructs Proto-Indo-Iranian *̝j́ráyas / Proto-Iranian *jráyah. (3) The gloss. 'to swell, increase' is the meaning of that abandoned Latin gliscere; the meanings actually attested for the root are 'rush on, run up' (Skt. jráyati) and, for the s-stem, 'expanse, flat surface' — Buck p.37: 'Skt. (Vedic) jrayas- ‚flat surface‘ (so BR) ... but according to Geldner, Ved. Stud. 2.248 ff., ‚onset, onrush, course‘, fr. jri- ‚rush upon‘'. So Nourai's 'expanse' is right and his 'to swell, increase' is a meaning modern scholarship no longer assigns to this root. The two branches of the chart (Old Persian dr- and Avestan zr-) are not two independent derivations from a root but the two dialectal shapes of one Old Iranian word, Proto-Iranian *jrayah- (OP d- vs Av. z- from Proto-Iranian *dz-, exactly as OP dasta- : Av. zasta- 'hand').\",\n   \"note_fa\": \"آنچه نورایی «Glei, Greios» نامیده در واقع دو ارجاع جداست: «Glei» مدخل glei- پوکورنی در صفحهٔ ۴۰۱ است و «Greios» بازسازیٔ کنت (صفحهٔ ۱۹۲) یعنی *ǵreyos- برپایهٔ سنسکریت jráyas- «پهنه». هر دو ارجاع درست است، امّا سه نکته را باید افزود. نخست آنکه خود پوکورنی می‌نویسد «Nur indoiranisch» یعنی این ریشه تنها در شاخهٔ هندوایرانی گواهی دارد؛ پس برچسب «هندواروپایی» برای آن دقیق نیست و بهتر است آن را ستاک هندوایرانی آغازین *̝j́ráyas- بدانیم. دوم آنکه لام در «glei-» یادگار والده–پوکورنی (جلد ۱، ص ۶۶۰) است که لاتین gliscere «افزودن» را — آن هم با تردید — به این ریشه بسته بود؛ پوکورنی در چاپ ۱۹۵۹ آن پیوند را کنار گذاشت ولی املای مدخل را نگاه داشت؛ گواهی‌های هندوایرانی (jr-، zr-، dr-) به *ǵr- راه می‌برند نه به *gl-. سوم آنکه معنای «ورم کردن، افزودن» همان معنای gliscereی متروک است؛ معنای گواهی‌شده «تاختن، شتافتن» (jráyati) و در اسم «پهنه، گستره» (jráyas) است. بنابراین ریشه واقعی است ولی برچسب زبان و نیمی از معنای آن با احتیاط پذیرفتنی است.\",\n   \"sources\": [W_OP, W_AV],\n   \"ref_check\": [\n    {\"ref\": \"POK:401\", \"status\": \"supports\",\n     \"note\": \"POK_02.txt leaf 57 (= printed p.401; offset leaf = p - 344): 'glei- „anlaufen, anstürmen“?  Nur indoiranisch. / Ai. jráyati „stürmt an, läuft an“, jráyas- n. „Ungestüm, Lauf, Flußlauf“, prthu-jráya- „weit laufend“; / av. zrayah-, apers. drayah- „See, Meer“, mpers. zray, npers. (mit Umstellung) daryä, pǝrǝu-zrayah „über weite Wasserflächen sich erstreckend“. WP. I 660'. POK_full.txt lines 38268-38279 give the same entry as 'Root / lemma: glei-, Meaning: to run up to, Note: Only indoiranisch'. The page is exactly right; the gloss 'to swell, increase' is not Pokorny's.\"},\n    {\"ref\": \"KNT:192\", \"status\": \"supports\",\n     \"note\": \"KNT.txt leaf 215 (the lexicon leaf that follows dūra-/drauga-; the scan's own numeral '157' on leaf 180 fixes printed = leaf − 23, i.e. p.192): 'drayah- sb. ‚sea‘: Av. zrayah-, NPers. dáryà, Skt. jráyas- ‚expanse‘, pIE *ǵrejos- (§88, §113, §128, §156.II). ... draya asn. DB 5.23; DPe 15; DZe 10. drayahya lsn. ... DB 1.15, DPe 14, DSe 28; drayahiyà XPh 23.' Kent's *ǵreyos- is Nourai's 'Greios'.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"p.401 s.v. glei- (POK_02.txt leaf 57; POK_full.txt l.38268)\", \"stance\": \"partial\",\n     \"note\": \"Has the root and the whole Iranian chain, but glosses it 'anlaufen, anstürmen' (to run up, rush at) and flags 'Nur indoiranisch' — not 'to swell, increase' and not securely Indo-European.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 660 (incoming/WLD/WLD_Bd1_pages.txt l.62530, leaf 668)\", \"stance\": \"partial\",\n     \"note\": \"'glei- „anlaufen, anstürmen“? Ai. jrayati ..., jráyas n. „Ungestüm, Hast, Anlauf, Lauf, Flußlauf, Strom“ ...; av. zrayah-, ap. drayah- „See, Meer“, mp. zray, np. (mit Umstellung) darya (s. Hübschmann Pers. Stud. 62) ...; lat. gliscere „unvermerkt zunehmen, an Stärke gewinnen“ ... (?; umstritten s. Wf. LEWb. 2 345 ...)'. This is where Nourai's gloss 'to swell, increase' comes from — and Walde-Pokorny already marks the Latin word 'umstritten'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, IE roots appendix (AHD_watkins1985.txt)\", \"stance\": \"silent\",\n     \"note\": \"grep for 'jrayas', 'drayah', 'zrayah', 'greios' returns nothing: the root has no English reflex and is absent from the appendix, consistent with its being Indo-Iranian only.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, An Indo-European Comparative Dictionary (IEC.txt, g-/ghr- section)\", \"stance\": \"silent\",\n     \"note\": \"grep 'jrayas|zrayah|drayah|grei' finds greiǵ-, greng-, ghreibō etc. but no lemma covering jráyas-/zrayah-; Mann too has no Indo-European lemma for it.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck p.37, section 1.32 SEA (SYN.txt leaf 63)\", \"stance\": \"supports\",\n     \"note\": \"'Av. zrayah-, OPers. drayah- (NPers. darya ‚sea‘ or ‚large river‘) : Skt. (Vedic) jrayas- ‚flat surface‘ (so BR), in which case one would compare the Iranian use with that of Grk. πέλαγος, Lat. aequor (above), but according to Geldner, Ved. Stud. 2.248 ff., ‚onset, onrush, course‘, fr. jri- ‚rush upon‘. Walde-P. 1.660.'\"}\n   ],\n   \"nodes\": []\n  }\n ]\n}\n\nnodes = doc[\"entries\"][0][\"nodes\"]\n\nnodes.append({\n \"id\": 1,\n \"lang\": \"Old Persian\",\n \"words\": \"drayah\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old Persian drayah- n. 'sea' is a genuine, well attested Achaemenid word: acc. draya DB 5.23, DPe 15, DZe 10, loc. drayahya DB 1.15 (tyaiy drayahyā 'those who dwell by the sea', the satrapy of Dascylium), DPe 14, DSe 28, drayahiyā XPh 23. It is an s-stem of the Indo-Iranian type nom.-acc. -as / oblique -as- (Kent §185.1), the exact counterpart of Vedic jráyas- 'expanse, flat surface' and Avestan zrayah-. The initial d- is not a separate derivation but the regular Old Persian reflex of Proto-Iranian *dz- (< PIE palatal *ǵ), where Avestan shows z-: compare OP dasta- : Av. zasta- 'hand', OP adanā : Av. zan- 'know'. So the two branches Nourai draws from the root (this node and node #4) are the southwestern and the Avestan shape of one Old Iranian word, Proto-Iranian *jráyah- (Wiktionary), and the arrow root → drayah- is correct. Semantically 'expanse (of water)' → 'sea', with the Old Persian word used both of the sea proper and, in DB 1.15/DPe 13f, in the standing contrast 'those of the mainland and those beside the sea'.\",\n \"derivation_fa\": \"«drayah-» در پارسی باستان اسمی است از گونهٔ ستاک‌های s دار که در سنگ‌نبشته‌های بیستون و شوش می‌آید (draya در DB 5.23 و DPe 15، در‌برایی drayahyā در DB 1.15) و هم‌ارز دقیق zrayah- اوستایی و jráyas- سنسکریت است. دال آغازین آن دگرگونی آوایی قاعده‌مند است: *dz ایرانی آغازین (از *ǵ هندواروپایی) در پارسی باستان به d و در اوستایی به z بدل می‌شود؛ نمونهٔ مشهور آن dasta- پارسی باستان در برابر zasta- اوستایی «دست» است. پس دو شاخهٔ نمودار در اصل دو صورت گویشی از یک واژهٔ ایرانی باستان *jráyah- اند. ادعای نورایی درست است؛ کنت، بارتولومه و باک هر سه همین را می‌گویند.\",\n \"sources\": [W_OP],\n \"ref_check\": [\n  {\"ref\": \"POK:401\", \"status\": \"supports\",\n   \"note\": \"POK_02.txt leaf 57 (p.401): 'av. zrayah-, apers. drayah- „See, Meer“' — the Old Persian word is listed under the root exactly as the chart draws it.\"},\n  {\"ref\": \"SYN:37\", \"status\": \"supports\",\n   \"note\": \"SYN.txt leaf 63 (= printed p.37, offset leaf = p + 26 in this stretch; the 1.32 SEA table itself is on p.36 and lists 'Av. zrayah-, OPers. drayah-'): 'Av. zrayah-, OPers. drayah- (NPers. darya ‚sea‘ or ‚large river‘) : Skt. (Vedic) jrayas- ‚flat surface‘ ... Walde-P. 1.660.'\"}\n ],\n \"consulted\": [\n  {\"src\": \"KNT\", \"where\": \"Kent p.192 s.v. drayah- (KNT.txt leaf 215)\", \"stance\": \"supports\",\n   \"note\": \"'drayah- sb. ‚sea‘: Av. zrayah-, NPers. dáryà, Skt. jráyas- ‚expanse‘, pIE *ǵrejos-'; attestations 'draya asn. DB 5.23; DPe 15; DZe 10. drayahya lsn. ... DB 1.15, DPe 14, DSe 28'. Kent §2194 (KNT.txt l.2194) also files it among the neuter s-stems: 'acc. draya ‚sea‘ (and draiya), Av. zrayō, Skt. jráyas'.\"},\n  {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiran. Wörterbuch col. 1701 s.v. zrayah- (BRT.txt l.28316, leaf 505)\", \"stance\": \"supports\",\n   \"note\": \"'j. zrayah-, p. drayah- n. ‚(ausgedehnte Wasserfläche sva.) See, Meer“' — Bartholomae files the Old Persian word as one headword with the Avestan, quoting DB 1.6 'imā dahyāva ... tyaiy drayahyā' and DPe. Ableit.: 'ai. jráyas- n. ‚Fläche“, mp. (Pü.) zray, np. daryā (wozu Hbm. PSt 62)'.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck p.37 (SYN.txt leaf 63)\", \"stance\": \"supports\",\n   \"note\": \"See ref_check; Buck gives the same equation and adds the semantic parallel with Gk. πέλαγος / Lat. aequor 'level (surface)'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 2,\n \"lang\": \"Pahlavi\",\n \"words\": \"drai-âp\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Book Pahlavi <dlydʾ(p)> drayā(b), Manichaean MP dryʾb, 'sea'. The Old Persian s-stem lost its ending (*drayah > drayā) and was reinforced with āb/āp 'water', giving the compound drayā-āp 'sea-water(s)' — exactly Nourai's 'drai-âp ... ☆Ab 1'. The best proof is the Aramaic heterogram: Sasanian scribes wrote the word YMYMYʾ, i.e. yammē mayyā 'seas of water', a word-for-word calque of dray(ah)-āp, which shows they analysed it just as the chart does (Nyberg II 69). MacKenzie p.27: 'drayā(b) [dlydʾ(p) | M dryʾb, N daryā(b)] sea', with the derivative drayā(b)-bār 'sea-shore'. Moʾin's own footnote in Borhān-e Qāṭeʿ (p.848, s.v. دریاب) states the same analysis: 'در پهلوی drayāp از *drayā + āp، جزو اول از پارسی باستان drayah'. One nuance to keep: Horn p.125 warns that the -b is secondary ('die Form deryāb verdankt nur einer Anlehnung an āb ‚Wasser‘ ihre Entstehung'), so the plain drayā and the extended drayāb coexisted in Middle Persian rather than the second replacing the first.\",\n \"derivation_fa\": \"در فارسی میانه واژه به صورت drayā(b) به‌کار می‌رفته (پهلوی کتابی <dlyʾ(p)>، مانویdryʾb): ستاک سایشی پارسی باستان drayah- پس از افتادن پایانه به drayā رسید و سپس با «آب» (ایرانی باستان āp-) ترکیب شد. بهترین گواه این تحلیل، هزوارش آرامی YMYMYʾ (yammē mayyā «دریاهای آب») است که ترجمهٔ لفظ‌به‌لفظ drayā-āp است (نیبرگ، جلد ۲، ص ۶۹). مکنزی (ص ۲۷) نیز همین را می‌آورد و معین در حاشیهٔ برهان قاطع (ص ۸۴۸، ذیل «دریاب») می‌نویسد «در پهلوی drayāp از *drayā + āp، جزو اول از پارسی باستان drayah». تنها نکته آنکه هرن (شمارهٔ ۵۶۱) جزء «آب» را افزوده‌ای ثانوی و نوعی ریشه‌شناسی عامیانه می‌داند. ادعای نورایی درست است.\",\n \"sources\": [W_FA],\n \"ref_check\": [\n  {\"ref\": \"MON:1730\", \"status\": \"not_checked\",\n   \"note\": \"Moʾin's six-volume Farhang-e Fārsi is not online in any form (refs_online.json MON notes a 2026-09 re-search of archive.org, Google Books, HathiTrust, noorlib, ketabnak: only the 2-vol Adena condensation exists), so page 1730 cannot be opened. The condensation (MON_part1.txt) does carry the substance: 'دریا: [= دریاب] (اِ.) آب زیادی که محوطهٔ وسیعی را فراگرفته ... بحر' — Moʾin equates دریا with دریاب, which is Nourai's arrow.\"},\n  {\"ref\": \"BQT:847\", \"status\": \"supports\",\n   \"note\": \"BQT_v2_pages.txt leaf 307 = printed p.847 (offset printed = leaf + 540; the leaf carries the headword 'دریا = معروف است و بعربی بحر خوانند'), and Moʾin's etymological footnote running at the foot of pp.847-848 reads (OCR, leaf 308): 'دریاب ، در پهلوی drayāp از *drayā + āp ، جزو اول از پارسی باستان drayah ... بارتولمه ۱۰۷۱ ... بلوچی zirih (سرچشمه) ... کردی derya ، افغانی daryāb ... رک: اشتقاق و هوبشمان ۱۹۵'. Exactly Nourai's claim, and Moʾin's own reference is Bartholomae col. 1071/1701.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.27 s.v. drayā(b) (PHD_pages.txt leaf 48)\", \"stance\": \"supports\",\n   \"note\": \"'drayā(b) [dlydʾ(p) | M dryʾb, N daryā(b)] sea. ~-bār [| N -bār] sea-shore.' MacKenzie's English index (p.'sea') gives 'sea drayā(b), zrēh', i.e. both Pahlavi words of this chart.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II p.69 s.v. drayāp (NYB_vol2_glossary.txt leaf 77)\", \"stance\": \"supports\",\n   \"note\": \"'drayāp [dlyʾpʹ] the sea 62:1, 21:1, 113:1 — SW form of Av. (1701 sq.) zrayah (v. zrah, zrāi): OP drayah- + āp; the compound was quite clear to those who created the Aram. expression used later as ideogr. (FrP 3): YMYMYʾ, i. e. yammē mayyā ‚seas of water‘, a purely mechanical transposition of dray(ah)-āp ‚sea-waters‘. MPrs dryʾb (A-H I); Paz. daryāv; Ps. has the bizarre spelling dlywʾw; NP daryā.'\"},\n  {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no.561, p.125 (HRN.txt leaf 146)\", \"stance\": \"partial\",\n   \"note\": \"Horn lists 'phlv. daryāp, daryāk (Bund.), zrē' but adds 'Die Form deryāb verdankt nur einer Anlehnung an āb ‚Wasser‘ ihre Entstehung' — the -b element is a secondary attachment, so drayā without -p is the older shape.\"}\n ]\n})\n\nnodes.append({\n \"id\": 3,\n \"lang\": \"Persian\",\n \"words\": \"daryâ «دریا»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian دریا daryā 'sea, great river' continues the Middle Persian word with one regular change: the initial cluster dr- before ā is metathesised to dar- in Pazand and New Persian, though not yet in Pahlavi. Hübschmann, Persische Studien p.62 (his note on Horn no.561): 'Aus ap. draya- oder drayah- wurde phl. drayak, daraus np. *draya, das mit Umstellung von ra zu ar (vgl. farmān aus framān) zu daryā wurde'; and §62, p.174: 'Die Anlautsgruppen drā- und frā- werden im Paz. und Np. (aber noch nicht im Phl.) umgestellt in dar- und far-: daryā ‚Meer‘ = ap. drayah-'. Pokorny p.401 notes the same thing in three words: 'npers. (mit Umstellung) daryā'. Wiktionary derives the Persian word exactly as Nourai's chart does — 'Inherited from Middle Persian dlyʾb (drayāb, ‚sea”), from Old Persian 𐎭𐎼𐎹 (draya) + āb' — and Moʾin heads his entry 'دریا [= دریاب]'. Horn p.125 records the word's spread: Judaeo-Persian דריא (Isaiah 8:23), Kurdish deryā, Pashto daryāh, Balochi darya, Yidgha dāriyow 'river'. The one point where the chart simplifies: since the -āb is secondary (Horn), New Persian daryā may just as well continue the plain MP drayā, with daryāb the by-form; either way the line OP drayah- → MP → NP daryā stands.\",\n \"derivation_fa\": \"«دریا» در فارسی نو دنبالهٔ همان واژهٔ فارسی میانه drayā(b) است با یک دگرگونی قاعده‌مند: قلب (metathesis) خوشهٔ آغازین drā- به dar-، همان‌گونه که framān به «فرمان» و frāzānak به «فرزانه» رسیده است. هوبشمان در پژوهش‌های فارسی (ص ۶۲) می‌نویسد که از drayah پارسی باستان، پهلوی drayak و از آن *drayaی فارسی پدید آمد که با قلب ra > ar به «دریا» بدل شد؛ پوکورنی نیز همین را با تعبیر «mit Umstellung» می‌آورد. ویکی‌واژه نیز عیناً همین زنجیره را می‌دهد. هرن (ش ۵۶۱) وام‌گیری‌های آن را هم می‌شمارد: یهودی‌فارسی، کردی derya، پشتو daryāh، بلوچی darya. تنها نکتهٔ باریک آنکه چون جزء «آب» ثانوی است، «دریا» می‌تواند مستقیماً دنبالهٔ drayāی ساده باشد و «دریاب» گونهٔ دیگر آن. در مجموع ادعای نورایی درست است.\",\n \"sources\": [W_FA, W_OP],\n \"ref_check\": [\n  {\"ref\": \"MON:37\", \"status\": \"not_checked\",\n   \"note\": \"The 6-vol Moʾin is not online (see node #2). The page number also looks wrong on its face: in an alphabetical Persian lexicon whose first volume opens with آ, p.37 cannot hold دریا (Nourai's other two Moʾin cites on this page are 1730). Content check in the 2-vol condensation (MON_part1.txt): 'دریا: [= دریاب] (اِ.) آب زیادی که محوطهٔ وسیعی را فراگرفته و به اقیانوس راه دارد، بحر' — supports the arrow, cannot confirm the page.\"},\n  {\"ref\": \"BQT:847\", \"status\": \"supports\",\n   \"note\": \"BQT_v2_pages.txt leaf 307 = p.847: headword 'در یا = معروف است وبعربی بحر خوانند'; Moʾin's footnote at the foot of the following column derives دریاب from Pahlavi drayāp < *drayā + āp < OP drayah.\"},\n  {\"ref\": \"HRN:125\", \"status\": \"supports\",\n   \"note\": \"HRN.txt leaf 146 = printed p.125 (the leaf opens '- 125 —'), entry '561. deryā ‚Meer; grosser Fluss‘, jüd.-pers. דריא (Is. 8,23). ap. drayah- ‚Meer‘; aw. zrayah- ‚Meer‘; phlv. daryāp, daryāk (Bund.), zrē; ai. jrāyas-; bel. zirih ‚Quell‘, zira ‚Meer‘. LW. kurd. deryā; afg. daryāh; bel. darya; yidg. dāriyow ‚Fluss‘.' Nourai's page is exact.\"},\n  {\"ref\": \"POK:401\", \"status\": \"supports\",\n   \"note\": \"POK_02.txt leaf 57 (p.401): 'mpers. zray, npers. (mit Umstellung) daryä' — Pokorny states the metathesis explicitly.\"}\n ],\n \"consulted\": [\n  {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.62 (no.561) and p.174 (§62) (HUB.txt ll.2154, 6138)\", \"stance\": \"supports\",\n   \"note\": \"p.62: 'Aus ap. draya- oder drayah- wurde phl. drayak, daraus np. *draya, das mit Umstellung von ra zu ar (vgl. farmān aus framān u. s. w.) zu daryā wurde.' p.174: 'Die Anlautsgruppen drā- und frā- werden im Paz. und Np. (aber noch nicht im Phl.) umgestellt in dar- und far-: daryā ‚Meer‘ = ap. drayah-.'\"},\n  {\"src\": \"HRN\", \"where\": \"Horn no.561, p.125\", \"stance\": \"supports\", \"note\": \"See ref_check; Horn's entry is the source both Moʾin's Borhān footnote ('رک: اشتقاق') and Bartholomae's cross-reference point to.\"},\n  {\"src\": \"MON\", \"where\": \"Moʾin (2-vol condensation) s.v. دریا (MON_part1.txt)\", \"stance\": \"supports\",\n   \"note\": \"'دریا: [= دریاب] (اِ.) آب زیادی که محوطهٔ وسیعی را فراگرفته و به اقیانوس راه دارد، بحر. ... دریابار (امر.) کنار دریا، ساحل'.\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur Kāshāni, Farhang-e Rishe-hā, p.275 s.v. دریا (incoming/ARY/ARY_latin_index_pages.txt leaf 274)\", \"stance\": \"supports\",\n   \"note\": \"The entry DARYA lists 'AVESTAN ZRAYAH, ZREH-; OLD PERSIAN DRAYAH; PAHLAVI ZRAY, DRAYAB, ZREH; SANSKRIT JRAYATI, JRAYAS; ARMENIAN DZOV; KURDISH DERYA; BALUCHI ZIRIH, ZIRA; AFGHANI DARYAB', with references 'MACKENZIE (SEA) 131, BUCK: 36-37' — an independent modern Persian source giving the whole chart, and citing the same Buck pages as Nourai.\"},\n  {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ ed. Moʾin, pp.847-848\", \"stance\": \"supports\", \"note\": \"See ref_check BQT:847.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4,\n \"lang\": \"Avestan\",\n \"words\": \"zrayah, zarayah\",\n \"verdict\": \"plausible\",\n \"derivation\": \"zrayah- (younger Avestan zraiiЩh / zrayō, gen. zrayaŋhō) n. 'sea, large body of water' is the standard Avestan word, used above all of the mythical waters: zrayah- vouru.kaša- 'the wide-shored sea' (the world ocean), zrayah- pūiti.ka- and zrayah- yat ka̱saoim (Lake Hamun) — Bartholomae col.1701. It is the Avestan match of OP drayah- (node #1), z- being the regular Avestan reflex of Proto-Iranian *dz-, so the chart's two branches are one Old Iranian s-stem *jráyah-. Wiktionary reconstructs 'Proto-Iranian *jráyah, from Proto-Indo-Iranian *̝j́ráyas', with Sanskrit ज्रयस् (jráyas, 'expanse') as the Indic cognate. The gloss 'body of water, sea' is right, and the derived forms confirm it: pǝrǝu-zrayah- 'stretching over wide water-surfaces' (Yt.8.2), zrayana- 'marinus' (āpǝm xānyanąm ... zrayananąm 'the water of the sea', Yt.6.2). The second form Nourai prints, 'zarayah', is the one weak point: it is not a headword anywhere, but a manuscript variant. Bartholomae's own note 1 to col.1701 says the word is to be read zrayah- 'auch Y.42.4 ... wo NA. zarayō neben zrayaŋhō bietet' — i.e. the tradition offers zarayō beside zrayaŋhō at Yasna 42.4, and Bartholomae (with note 5, 'beides verderbte Formen', on the locatives zraya/zrayā) treats such spellings as corruptions. So 'zrayah' is confirmed and 'zarayah' is at best a secondary/corrupt variant reading, which drags the node down to plausible.\",\n \"derivation_fa\": \"صورت اوستایی zrayah- (اوستای متأخر zrayō، اضافی zrayaŋhō) «دریا، پهنهٔ آب» کاملاً گواهی‌شده است، به‌ویژه در ترکیب zrayah- vouru.kaša- (فراخکرت، دریای جهانی) و zrayah- ka̱saoya- (دریاچهٔ هامون)؛ بارتولومه در ستون ۱۷۰۱ آن را با پارسی باستان drayah- یکجا می‌آورد. زای آغازین بازتاب قاعده‌مند *dz ایرانی باستان است، در برابر دال پارسی باستان. امّا صورت دومی که نورایی آورده (zarayah) مدخل مستقلی نیست؛ بارتولومه در پاورقی همان ستون می‌نویسد که در یسنا ۴۲:۴ دستنویس‌ها zarayō را در کنار zrayaŋhō آورده‌اند و وی همان zrayah- را درست می‌داند و این‌گونه صورت‌ها را «محرّف» می‌خواند. پس بخش نخست گفتهٔ نورایی درست و بخش دوم با احتیاط پذیرفتنی است.\",\n \"sources\": [W_AV, W_OP],\n \"ref_check\": [\n  {\"ref\": \"POK:401\", \"status\": \"supports\",\n   \"note\": \"POK_02.txt leaf 57 (p.401): 'av. zrayah-, apers. drayah- „See, Meer“ ... pǝrǝu-zrayah „über weite Wasserflächen sich erstreckend“'. Pokorny lists only zrayah-, not zarayah-.\"},\n  {\"ref\": \"SYN:37\", \"status\": \"supports\",\n   \"note\": \"SYN.txt leaf 63 (p.37): 'Av. zrayah-, OPers. drayah- (NPers. darya ‚sea‘ or ‚large river‘) : Skt. (Vedic) jrayas- ‚flat surface‘ ...'; the 1.32 SEA word-table on the facing page (p.36) lists 'Av. zrayah-, OPers. drayah-' as the Iranian entries.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiran. Wörterbuch col. 1701 (BRT.txt l.28316, leaf 505)\", \"stance\": \"partial\",\n   \"note\": \"Headword: 'j. zrayah-, p. drayah- n. ‚(ausgedehnte Wasserfläche sva.) See, Meer“', with the uses 'mit vouru.kaša- Name des Weltozeans', 'mit pūiti.ka- Name eines mythischen Sees', 'mit ka̱saoya- Name des Hāmūn-Sees'; 'Ableit. — ai. jráyas- n. ‚Fläche“, mp. (Pü.) zray, np. daryā (wozu Hbm. PSt 62)'. Note 1: 'So auch Y. 42.4 zu lesen, wo NA. zarayō neben zrayaŋhō bietet'; note 5 calls the variant locatives 'beides verderbte Formen'. Supports zrayah-, and shows zarayō/zarayah is only a variant reading.\"},\n  {\"src\": \"KNT\", \"where\": \"Kent p.192 s.v. drayah- and §2194 (KNT.txt)\", \"stance\": \"supports\",\n   \"note\": \"'drayah- sb. ‚sea‘: Av. zrayah-, NPers. dáryà, Skt. jráyas- ‚expanse‘'; and in the s-stem paradigm list 'acc. draya ‚sea‘ ..., Av. zrayō, Skt. jráyas'.\"},\n  {\"src\": \"POK\", \"where\": \"p.401\", \"stance\": \"supports\", \"note\": \"See ref_check.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5,\n \"lang\": \"Pahlavi\",\n \"words\": \"zrě\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian zrē(h), written <zlyh> in Book Pahlavi and zryh in Manichaean/Psalter, 'sea, lake'. It is the same Old Iranian s-stem as node #4 in its northwestern (Avestan/Parthian) shape, with z- not d-. Nyberg II 247 sets out the morphology precisely: 'zrāh [zlh], zrāi [zlʾy, zlʾd] sea ... Av. (1701 sq.) zrayah-; MPrth zryh, zryy, adj. zrhyg; MPrs zryh (S) borrowed from NW, the authentic SW w. being OP drayah-, BP drayāp (q. v.); Paz. zrih, zreh; NP zurih, zarah. — BP zrāi < the cas. rect. zray(ah) with lengthening of -a- after the final syllable had been dropped ...; zrēh < cas. obl. zrayahō (or late *zrayahē) > *zrayah > zrēh.' So zrēh is the oblique-stem form of Avestan zrayah- exactly as the chart's arrow says. MacKenzie p.99: 'zrēh [zlyh | P zryh] sea, lake' (kept apart in his dictionary from the homograph zrēh 'armour', which belongs to Av. zrāða-). Horn p.125 gives the same form under deryā ('phlv. ... zrē') and adds the caution 'Phlv. zrē ist entweder dialektisch oder nur als ursprüngliche und dann weiter gedrungene Umschreibung von aw. zrayah- anzusehen'. Nourai's transliteration zrě is Horn's zrē letter for letter. The only refinement to the arrow is that in Middle Persian proper this is a northwestern (Parthian) form beside the native drayāp, not a straight southwestern continuation.\",\n \"derivation_fa\": \"صورت پهلوی zrēh (پهلوی کتابی <zlyh>، مانوی و زبوری zryh) «دریا، دریاچه» همان ستاک zrayah- اوستایی است. نیبرگ (جلد ۲، ص ۲۴۷) روند را روشن می‌کند: zrāh/zrāi از حالت فاعلی zray(ah) و zrēh از حالت وابستگی zrayahō > *zrayah > zrēh پدید آمده است. مکنزی (ص ۹۹) نیز «zrēh [zlyh | P zryh] sea, lake» دارد و آن را از هم‌نگاشتش zrēh «زره، جوشن» (از zrāða- اوستایی) جدا می‌کند. هرن هم در شمارهٔ ۵۶۱ همین zrē را می‌آورد. تنها نکتهٔ افزودنی آنکه به باور نیبرگ این صورت در فارسی میانه وام‌واژه‌ای شمال‌غربی (پارتی zryh) است در کنار صورت بومی drayāp. ادعای نورایی درست است.\",\n \"sources\": [W_AV],\n \"ref_check\": [\n  {\"ref\": \"MON:1730\", \"status\": \"not_checked\",\n   \"note\": \"6-vol Moʾin not available online (see node #2). The 2-vol condensation has the Persian outcome but no Pahlavi form: 'زراه: [= زره] (اِ.) دریا؛ بحر' (MON_part1.txt l.70846).\"},\n  {\"ref\": \"BQT:1010\", \"status\": \"supports\",\n   \"note\": \"The Borhān headword زراه sits on BQT_v2_pages.txt leaf 472; the +540 offset that puts دریا on the p.847 Nourai cites gives printed ≈ 1012 here, i.e. Nourai's 1010 within the 2-3 page drift of this scan. Moʾin's footnote on that page reads (OCR): '(دریا) پهلوی zrē، بلوچی zirih، اشتقاق ۱۹۵، و رک: دریا' — precisely the Pahlavi zrē of this node, cross-referred to دریا.\"}\n ],\n \"consulted\": [\n  {\"src\": \"NYB\", \"where\": \"Nyberg II p.247 s.v. zrāh / zrāi (NYB_vol2_glossary.txt leaf 255)\", \"stance\": \"supports\",\n   \"note\": \"'zrāh [zlh], zrāi [zlʾy, zlʾd] sea ... Av. (1701 sq.) zrayah-; MPrth zryh, zryy, adj. zrhyg; MPrs zryh (S) borrowed from NW, the authentic SW w. being OP drayah-, BP drayāp (q. v.); Paz. zrih, zreh; NP zurih, zarah. — ... zrēh < cas. obl. zrayahō (or late *zrayahē) > *zrayah > zrēh.' Nyberg's index also has the equation 'drayah-: zrāh' and 'zrayah-: drayāp, zrah'.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie p.99 s.v. zrēh (PHD_pages.txt leaf 120)\", \"stance\": \"supports\",\n   \"note\": \"'zrēh [zlyh | P zryh] sea, lake' — immediately followed by the distinct homograph 'zrēh [zlyh | N zirih] armour'; his English index gives 'lake war, zrēh' and 'sea drayā(b), zrēh'.\"},\n  {\"src\": \"HRN\", \"where\": \"Horn no.561, p.125 (HRN.txt leaf 146)\", \"stance\": \"supports\",\n   \"note\": \"'phlv. daryāp, daryāk (Bund.), zrē' and 'Phlv. zrē ist entweder dialektisch oder nur als ursprüngliche und dann weiter gedrungene Umschreibung von aw. zrayah- anzusehen.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 6,\n \"lang\": \"Persian\",\n \"words\": \"zrâh «زراه»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"زراه (zarāh / zerāh) 'sea' is a real Persian word, but a rare, dialectal and largely lexicographers' one, not the ordinary reflex. It is a headword in Borhān-e Qāṭeʿ, glossed there simply as the sea ('... و بعربی بحر خوانند'), with Moʾin's footnote '(دریا) پهلوی zrē، بلوچی zirih ... و رک: دریا', and Moʾin's own Farhang has 'زراه: [= زره] (اِ.) دریا؛ بحر'. Horn p.125 judges it explicitly: 'np. zerāh ist sicher Dialektform', and Hübschmann p.220 lists it the same way, 'daryā ‚Meer‘ = ap. draya- ..., zd. zrayah-, aber dial. zarah'. Two qualifications keep this from 'confirmed'. (1) The normal New Persian continuation of MP zrēh is زره zereh (Nyberg's 'Paz. zrih, zreh; NP zurih, zarah'; Balochi zirih), and زراه with -ā- is a by-form. (2) On Nyberg's account the -ā- form does not come from zrēh at all but from the parallel Book Pahlavi zrāh/zrāi, built on the nominative zray(ah) (with lengthening of -a- after loss of the final syllable), whereas zrēh continues the oblique zrayahō. So the arrow zrē → زراه is one step off: زره zereh descends from zrēh, and زراه zarāh rather from zrāh. Both belong to this root, and Nourai's Persian script and gloss are correct as printed — no transcription problem.\",\n \"derivation_fa\": \"«زراه» واژه‌ای واقعی ولی کمیاب و گویشی است: مدخلی در برهان قاطع دارد و معین در حاشیه می‌نویسد «(دریا) پهلوی zrē، بلوچی zirih ... و رک: دریا»؛ در فرهنگ معین نیز «زراه: [= زره] (اِ.) دریا؛ بحر» آمده است. هرن (ص ۱۲۵) صریحاً می‌گوید «np. zerāh قطعاً گونهٔ گویشی است» و هوبشمان (ص ۲۲۰) نیز آن را «dial. zarah» می‌نامد. دو نکته موجب می‌شود این پیکان را فقط «با احتیاط پذیرفتنی» بدانیم: نخست آنکه دنبالهٔ معمول zrēh در فارسی «زره» (zereh) است نه «زراه»؛ دوم آنکه به باور نیبرگ گونهٔ با الف از zrāh پهلوی (برساخته از حالت فاعلی zray(ah)) می‌آید نه از zrēh که برساختهٔ حالت وابستگی است. با این حال هر دو صورت از همین ستاک‌اند و ضبط فارسی و معنای نورایی درست است (خطای چاپی یا خطای خوانش در کار نیست).\",\n \"sources\": [W_AV],\n \"ref_check\": [\n  {\"ref\": \"BQT:1010\", \"status\": \"supports\",\n   \"note\": \"BQT_v2_pages.txt leaf 472 carries the headword 'زراه' (with the definition column '... وبعربی بحر خوانند'), footnote: '(دریا) پهلوی zrē ، بلوچی zirih ، اشتقاق ۱۹۵ ، و رک : دریا'. The +540 offset (verified at leaf 307 = p.847 دریا, the page Nourai himself cites) makes this printed ≈ p.1012; the Borhān scan drifts by 2-3 pages in this stretch, so Nourai's 1010 is effectively right.\"}\n ],\n \"consulted\": [\n  {\"src\": \"HRN\", \"where\": \"Horn no.561, p.125 (HRN.txt leaf 146)\", \"stance\": \"supports\",\n   \"note\": \"'np. zerāh ist sicher Dialektform' — Horn knows the word and calls it a dialect form; he also lists Balochi zirih 'Quell', zira 'Meer'.\"},\n  {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.220 (HUB.txt l.7844)\", \"stance\": \"supports\",\n   \"note\": \"'daryā ‚Meer‘ = ap. draya- (oder drayah- ZDMG. 46, 298), zd. zrayah-, aber dial. zarah' — the -a- form is expressly the dialectal variant of this same word.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg II p.247 s.v. zrāh\", \"stance\": \"partial\",\n   \"note\": \"'Paz. zrih, zreh; NP zurih, zarah ... BP zrāi < the cas. rect. zray(ah) ...; zrēh < cas. obl. zrayahō' — confirms the Persian word but assigns the ā-form to the nominative stem zrāh rather than to zrēh.\"},\n  {\"src\": \"MON\", \"where\": \"Moʾin (2-vol condensation), s.v. زراه (MON_part1.txt l.70846)\", \"stance\": \"supports\",\n   \"note\": \"'زراه: [= زره] (اِ.) دریا؛ بحر.' Moʾin keeps the headword and refers it to زره.\"},\n  {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ, printed ≈ p.1012 s.v. زراه\", \"stance\": \"supports\", \"note\": \"See ref_check.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7,\n \"lang\": \"Sogdian\",\n \"words\": \"zry\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sogdian zry (Manichaean script), read zrē/zrayē, 'sea', accusative zryw. Gharib's Sogdian Dictionary entry 11424 gives it with the etymology the chart draws: 'zrē < Av. zrayah, Parth. zryh; acc. zryw; sea', citing Henning, BSOAS 12 and the Manichaean Cosmogony text (Cosm. 309.22). Strictly the Sogdian word is not descended from Avestan but is its eastern sister: both continue Proto-Iranian *jráyah- (Wiktionary), Sogdian keeping the z- of the northern and eastern Iranian languages exactly as Avestan and Parthian do, and losing the s-stem ending as everywhere in Middle Iranian. Gharib's own '<Av.' is the usual shorthand of Iranian dictionaries for 'from the Old Iranian word represented by Avestan', so the arrow is right as an ancestry statement.\",\n \"derivation_fa\": \"صورت سغدی zry (به خط مانوی، خوانش zrē) «دریا» با رایی zryw در فرهنگ سغدی قریب (مدخل ۱۱۴۲۴) با همین ریشه‌شناسی آمده است: «zrē < اوستایی zrayah، پارتی zryh»، با استناد به هنینگ و متن کیهان‌زایی مانوی. دقیق‌تر آنکه سغدی برگرفته از اوستایی نیست بلکه هم‌ریشهٔ آن است و هر دو از ایرانی آغازین *jráyah- می‌آیند؛ زای آغازین در سغدی و پارتی و اوستایی یکسان است و پایانهٔ ستاک s دار در دورهٔ میانه افتاده است. ادعای نورایی درست است.\",\n \"sources\": [W_AV],\n \"ref_check\": [\n  {\"ref\": \"SOD:465\", \"status\": \"supports\",\n   \"note\": \"SOD_pages.txt leaf 532 (printed ≈ 466 on the leaf − 66 offset, and the numeral '466' is printed in that very block, so Nourai's 465 is one page out or the entry straddles the opening): '11424 zry M / zre ©<Av. zrayah Parth. zryh ©acc. zryw / sea / Hen. BSOAS 12, Cosm. 309.22'. Gharib gives exactly the derivation Nourai's arrow draws.\"}\n ],\n \"consulted\": [\n  {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary, entry 11424 (SOD_pages.txt leaf 532)\", \"stance\": \"supports\",\n   \"note\": \"See ref_check; the neighbouring entries 11425 zrync-, 11426 zrys- are unrelated verbs, so the sea-word is the isolated one.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg II p.247 s.v. zrāh\", \"stance\": \"supports\",\n   \"note\": \"'MPrth zryh, zryy, adj. zrhyg' — the Parthian form Gharib compares, showing the z-form is the northern/eastern Iranian shape shared by Parthian, Sogdian and Avestan.\"},\n  {\"src\": \"BRT\", \"where\": \"Bartholomae col. 1701\", \"stance\": \"supports\",\n   \"note\": \"Gives the Old Iranian etymon zrayah- from which the Sogdian word descends.\"}\n ]\n})\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-197.json','w',encoding='utf-8') as f:\n    json.dump(doc,f,ensure_ascii=False,indent=1)\n    f.write('\\n')\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk197.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-197.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 197"
}
```


### [2026-09-06T02:33:00.788Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 7/7
node verdicts: {'confirmed': 5, 'plausible': 2}
root verdicts: {'plausible': 1}
ref checks: {'supports': 11, 'not_checked': 3}
books consulted: {'supports': 22, 'partial': 3} | by book: {'NYB': 4, 'HRN': 4, 'BRT': 3, 'KNT': 2, 'PHD': 2, 'HUB': 2, 'MON': 2, 'BQT': 2, 'SYN': 1, 'ARY': 1, 'POK': 1, 'SOD': 1}
```


## [2026-09-06T02:33:07.496Z] TOOL CALL #63: Bash

```json
{
 "command": "grep -n \"Щ\" data/verification/page-197.json; python3 - <<'EOF'\nimport json,re\np='/home/sfmqrb/git/rishe/data/verification/page-197.json'\ns=open(p,encoding='utf-8').read()\ns=s.replace('zraiiaЩh','zraiiaŋh')\nopen(p,'w',encoding='utf-8').write(s)\n# report any remaining Cyrillic\nfor m in set(re.findall(r'[Ѐ-ӿ]', s)):\n    print('cyrillic left:', m)\nEOF\npython3 -m json.tool data/verification/page-197.json >/dev/null && echo OK && python3 tools/verify_check.py 197 | tail -6"
}
```


### [2026-09-06T02:33:09.530Z] TOOL RESULT

```
220:     "derivation": "zrayah- (younger Avestan zraiiЩh / zrayō, gen. zrayaŋhō) n. 'sea, large body of water' is the standard Avestan word, used above all of the mythical waters: zrayah- vouru.kaša- 'the wide-shored sea' (the world ocean), zrayah- pūiti.ka- and zrayah- yat ka̱saoim (Lake Hamun) — Bartholomae col.1701. It is the Avestan match of OP drayah- (node #1), z- being the regular Avestan reflex of Proto-Iranian *dz-, so the chart's two branches are one Old Iranian s-stem *jráyah-. Wiktionary reconstructs 'Proto-Iranian *jráyah, from Proto-Indo-Iranian *̝j́ráyas', with Sanskrit ज्रयस् (jráyas, 'expanse') as the Indic cognate. The gloss 'body of water, sea' is right, and the derived forms confirm it: pǝrǝu-zrayah- 'stretching over wide water-surfaces' (Yt.8.2), zrayana- 'marinus' (āpǝm xānyanąm ... zrayananąm 'the water of the sea', Yt.6.2). The second form Nourai prints, 'zarayah', is the one weak point: it is not a headword anywhere, but a manuscript variant. Bartholomae's own note 1 to col.1701 says the word is to be read zrayah- 'auch Y.42.4 ... wo NA. zarayō neben zrayaŋhō bietet' — i.e. the tradition offers zarayō beside zrayaŋhō at Yasna 42.4, and Bartholomae (with note 5, 'beides verderbte Formen', on the locatives zraya/zrayā) treats such spellings as corruptions. So 'zrayah' is confirmed and 'zarayah' is at best a secondary/corrupt variant reading, which drags the node down to plausible.",
cyrillic left: Щ
OK
nodes verified: 7/7
node verdicts: {'confirmed': 5, 'plausible': 2}
root verdicts: {'plausible': 1}
ref checks: {'supports': 11, 'not_checked': 3}
books consulted: {'supports': 22, 'partial': 3} | by book: {'NYB': 4, 'HRN': 4, 'BRT': 3, 'KNT': 2, 'PHD': 2, 'HUB': 2, 'MON': 2, 'BQT': 2, 'SYN': 1, 'ARY': 1, 'POK': 1, 'SOD': 1}
```


## [2026-09-06T02:33:18.822Z] TOOL CALL #64: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport re\np='data/verification/page-197.json'\ns=open(p,encoding='utf-8').read()\ni=s.find('zraiia')\nprint(repr(s[i:i+12]))\ns2=re.sub(r'[Ѐ-ӿ]','ŋ',s)\nopen(p,'w',encoding='utf-8').write(s2)\ni=s2.find('zraiia'); print(repr(s2[i:i+12]))\nprint('cyrillic remaining:', re.findall(r'[Ѐ-ӿ]',s2))\nEOF\npython3 -m json.tool data/verification/page-197.json >/dev/null && python3 tools/verify_check.py 197"
}
```


### [2026-09-06T02:33:20.629Z] TOOL RESULT

```
''
''
cyrillic remaining: []
nodes verified: 7/7
node verdicts: {'confirmed': 5, 'plausible': 2}
root verdicts: {'plausible': 1}
ref checks: {'supports': 11, 'not_checked': 3}
books consulted: {'supports': 22, 'partial': 3} | by book: {'NYB': 4, 'HRN': 4, 'BRT': 3, 'KNT': 2, 'PHD': 2, 'HUB': 2, 'MON': 2, 'BQT': 2, 'SYN': 1, 'ARY': 1, 'POK': 1, 'SOD': 1}
```


## [2026-09-06T02:33:29.671Z] TOOL CALL #65: Bash

```json
{
 "command": "python3 - <<'EOF'\np='data/verification/page-197.json'\ns=open(p,encoding='utf-8').read()\nprint(s.count('zraiiŋh'), s.count('zraiiaŋh'))\ns=s.replace('zraiiŋh','zraiiaŋh')\nopen(p,'w',encoding='utf-8').write(s)\ni=s.find('zraiia'); print(repr(s[i-30:i+30]))\nEOF\npython3 -m json.tool data/verification/page-197.json >/dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 197"
}
```


### [2026-09-06T02:33:31.818Z] TOOL RESULT

```
1 0
'n": "zrayah- (younger Avestan zraiiaŋh / zrayō, gen. zrayaŋh'
JSON OK
nodes verified: 7/7
node verdicts: {'confirmed': 5, 'plausible': 2}
root verdicts: {'plausible': 1}
ref checks: {'supports': 11, 'not_checked': 3}
books consulted: {'supports': 22, 'partial': 3} | by book: {'NYB': 4, 'HRN': 4, 'BRT': 3, 'KNT': 2, 'PHD': 2, 'HUB': 2, 'MON': 2, 'BQT': 2, 'SYN': 1, 'ARY': 1, 'POK': 1, 'SOD': 1}
```


## [2026-09-06T02:33:52.312Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-197.json` written; `verify_check.py 197` reports 7/7 nodes, 0 PROBLEM lines.

**Page 197 (book p.167) — one real entry (`Glei, Greios`, "sea"); entry 1 is the `Glue → Gel` redirect, skipped.**

- Verdicts: root `plausible`; nodes 5 `confirmed`, 2 `plausible`, 0 disputed, 0 transcription_suspect.
- Ref checks: 11 `supports`, 3 `not_checked` (all three are Moʾin's 6-vol Farhang, still not online).
- Books consulted: POK, WLD, AHD, IEC, SYN, KNT, BRT, PHD, NYB, HRN, HUB, MON, BQT, ARY, SOD (25 entries).

Notes on the two non-`confirmed` items:
- **ROOT `Glei, Greios` — plausible.** Both citations are exact (Pokorny p.401 lemma `glei-`; Kent p.192 `pIE *ǵreyos-`), but Pokorny's own note is "Nur indoiranisch", so the "Indo-European" label overreaches (Watkins/AHD and Mann are silent); the `-l-` of the lemma is a fossil of Walde-Pokorny I 660's disputed link with Latin *gliscere*, which Pokorny 1959 dropped — and that abandoned link is where Nourai's gloss "to swell, increase" comes from. Attested senses: 'rush on' (Skt. *jráyati*) / 'expanse' (*jráyas*).
- **#4 Avestan `zrayah, zarayah` — plausible.** `zrayah-` confirmed (Bartholomae col.1701); `zarayah` is not a headword anywhere — it is the manuscript variant *zarayō* at Yasna 42.4 that Bartholomae records in n.1 and treats as corrupt.
- **#6 Persian `zrâh «زراه»` — plausible.** The word is real (Borhān headword + Moʾin's footnote "پهلوی zrē"; Horn: "np. zerāh ist sicher Dialektform"), but it is a dialectal by-form; the regular reflex of MP *zrēh* is زره *zereh*, and Nyberg traces the ā-form to BP *zrāh* (nom. stem) rather than to *zrēh*.

Page-number issues in Nourai's citations (no data fix needed, JSON matches the book):
- `MON:37` on node #3 cannot be right — p.37 of an alphabetical Persian lexicon opening with آ cannot hold دریا (his other Moʾin cites here are 1730); unverifiable anyway.
- `SOD:465` → Gharib's entry 11424 `zry` is printed on p.466 (one off).
- `BQT:1010` → the زراه headword maps to printed ≈1012 on the offset verified by دریا at p.847; within the scan's 2–3 page drift.

No extraction errors found: every form in the JSON (incl. `drai-âp`, `zrě`, «زراه») matches an attested form in Horn/Nyberg/MacKenzie/Borhān, so nothing needs correcting in `data/extracted/batch/page-197.json`.
