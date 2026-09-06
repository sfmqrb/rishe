# Verification process log — verify-page-229


## [2026-09-06T15:26:09.578Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 229 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-229.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-229.json. Write /home/sfmqrb/git/rishe/data/verification/page-229.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 229` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:26:11.286Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:26:12.114Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


## [2026-09-06T15:26:12.122Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-229.txt"
}
```


### [2026-09-06T15:26:12.157Z] TOOL RESULT

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


### [2026-09-06T15:26:12.163Z] TOOL RESULT

```
1	=== PDF page 229 (book page 199) ===
2	--- entry 0 ---
3	ROOT [Semitic] J.b.l : mountain  (refs KLN:169)
4	#1 (parent #0) [Arabic] refs=KLN:170; FVA:68 | j.b.l, jabal : mountain ; jabal-al-târiq : mountain of Târiq. | NOTE: Tariq invaded Spain in 711.
5	  #2 (parent #1) [Persian] refs=FVA:68 | jabal «جَبَل» : mountain ; jabal-ottâreq «جبل الطارق» : Gibraltar | extra: جِبال
6	  #3 (parent #1) [English] refs=KLN:655 | Gibraltar
7	#4 (parent #0) [Hebrew] refs=KLN:169 | gebhal : mountain, frontier town, a Phoenician port where papyrus was sold
8	  #5 (parent #4) [Greek] refs=KLN:169; NAT:110 | bublos : Greek name of the "Gebhal" port, assimilated from Hebrew word "Gebhal". Rolled paper from Gebhal. ; bibua : collection of writings, book
9	    #6 (parent #5) [Latin] refs=KLN:169 | biblia : book
10	      #7 (parent #6) [English] refs=KLN:169; AHD:129 | Bible, biblical bibliography
11	
```


## [2026-09-06T15:26:14.794Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-229.json",
 "description": "Read source JSON page 229"
}
```


### [2026-09-06T15:26:14.824Z] TOOL RESULT

```
{
  "pdf_page": 229,
  "book_page": 199,
  "entries": [
    {
      "root": {
        "name": "J.b.l",
        "lang": "Semitic",
        "refs": "KLN:169",
        "gloss": "mountain"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:170; FVA:68",
          "words": [
            {"translit": "j.b.l, jabal", "gloss": "mountain", "script": null},
            {"translit": "jabal-al-târiq", "gloss": "mountain of Târiq.", "script": null}
          ],
          "script_extra": null,
          "note": "Tariq invaded Spain in 711.",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:68",
          "words": [
            {"translit": "jabal", "gloss": "mountain", "script": "جَبَل"},
            {"translit": "jabal-ottâreq", "gloss": "Gibraltar", "script": "جبل الطارق"}
          ],
          "script_extra": "جِبال",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "English",
          "refs": "KLN:655",
          "words": [
            {"translit": "Gibraltar", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:169",
          "words": [
            {"translit": "gebhal", "gloss": "mountain, frontier town, a Phoenician port where papyrus was sold", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Greek",
          "refs": "KLN:169; NAT:110",
          "words": [
            {"translit": "bublos", "gloss": "Greek name of the \"Gebhal\" port, assimilated from Hebrew word \"Gebhal\". Rolled paper from Gebhal.", "script": null},
            {"translit": "bibua", "gloss": "collection of writings, book", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Latin",
          "refs": "KLN:169",
          "words": [
            {"translit": "biblia", "gloss": "book", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "KLN:169; AHD:129",
          "words": [
            {"translit": "Bible, biblical bibliography", "gloss": null, "script": null}
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


## [2026-09-06T15:26:16.995Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','FVA','AHD','NAT','FVQ','AFM','PLA','AFA','LKT','SKT','WEB','FSD','MON','BQT','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\"",
 "description": "Check refs_online for needed abbreviations"
}
```


### [2026-09-06T15:26:18.556Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
NAT {"title": "C. Berlitz, Native Tongues, New York 1982", "edition_found": "2005 Castle Books reprint (open); 1982 original lending-only (nativetongues00berl)", "kind": "archive_djvu", "url": "https://archive.org/details/native-tongues-charles-berlitz-book-sales-ca-1997-3-printing-2005-castle-books-9", "identifier": "native-tongues-charles-berlitz-book-sales-ca-1997-3-printing-2005-castle-books-9", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NAT_2005.txt", "page_offset": "2005 reprint: leaf = printed + 15 (e.g. leaf 17 = p.2); reprint pagination may differ slightly from 1
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-09-06T15:26:35.980Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo ---; python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['KLN','NAT','AHD']:\n    print(k, json.dumps(d[k], ensure_ascii=False))\n    print()\n\"",
 "description": "List local refs and print KLN/NAT/AHD entries"
}
```


### [2026-09-06T15:26:37.958Z] TOOL RESULT

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
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)", "local_files": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"], "cites": "page number, continuous across the two volumes (1966–67)"}

NAT {"title": "C. Berlitz, Native Tongues, New York 1982", "edition_found": "2005 Castle Books reprint (open); 1982 original lending-only (nativetongues00berl)", "kind": "archive_djvu", "url": "https://archive.org/details/native-tongues-charles-berlitz-book-sales-ca-1997-3-printing-2005-castle-books-9", "identifier": "native-tongues-charles-berlitz-book-sales-ca-1997-3-printing-2005-castle-books-9", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NAT_2005.txt", "page_offset": "2005 reprint: leaf = printed + 15 (e.g. leaf 17 = p.2); reprint pagination may differ slightly from 1982. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Popular book, prose chapters; grep the word.", "notes": ""}

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).", "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.", "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"}
```


## [2026-09-06T15:26:38.555Z] TOOL CALL #6: Bash

```json
{
 "command": "pdftoppm -f 229 -l 229 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg229 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render printed page 229"
}
```


### [2026-09-06T15:26:40.748Z] TOOL RESULT

```
total 4220
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:26 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    572 Sep  6 11:26 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb  69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb  81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb   2071 Sep  6 11:26 c_ijlak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb 111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb  11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb   2303 Sep  6 11:25 j.json
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb  37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb  77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb  61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb  80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb  17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb  50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb  17907 Sep  6 11:25 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb  54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb  53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb 141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb 194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb  76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb 147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb 118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb  90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb 161218 Sep  6 11:26 pg226hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb  52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb  42112 Sep  6 11:26 pg229.png
-rw-rw-r-- 1 sfmqrb sfmqrb 147680 Sep  6 11:20 sns167.jpg
```


## [2026-09-06T15:26:44.792Z] TOOL CALL #7: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg229.png"
}
```


### [2026-09-06T15:26:45.213Z] TOOL RESULT

```

```


## [2026-09-06T15:26:45.210Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:26:58.382Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 229 -l 229 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg229hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg229hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(0.24*w),int(0.29*h),int(0.52*w),int(0.34*h))).save('c229_greek.png')\nim.crop((int(0.50*w),int(0.13*h),int(0.80*w),int(0.19*h))).save('c229_persian.png')\n\"",
 "description": "Crop Greek and Persian boxes at 400dpi"
}
```


### [2026-09-06T15:27:01.576Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-06T15:27:03.331Z] TOOL CALL #9: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c229_greek.png"
}
```


### [2026-09-06T15:27:03.347Z] TOOL RESULT

```

```


## [2026-09-06T15:27:06.761Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg229hi.png'); w,h=im.size\nim.crop((int(0.24*w),int(0.335*h),int(0.52*w),int(0.365*h))).resize((int(0.28*w*2),int(0.03*h*2))).save('c229_bibua.png')\n\"",
 "description": "Crop bibua line"
}
```


### [2026-09-06T15:27:08.787Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:27:10.634Z] TOOL CALL #11: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c229_bibua.png"
}
```


### [2026-09-06T15:27:10.650Z] TOOL RESULT

```

```


## [2026-09-06T15:27:17.655Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^Bible\" KLN_1966.txt | head; echo ---; grep -n \"Byblos\\|byblos\\|bublos\\|Gebhal\\|gebhal\" KLN_1966.txt | head -30",
 "description": "Grep Klein 1966 for Bible/Byblos/Gebhal"
}
```


### [2026-09-06T15:27:17.716Z] TOOL RESULT

```
2326:Bible,  prob.  the  sandalwood  (the  first  form  oc¬ curs  I  Kings  10:11-12,  the  second  11  Chron. 2:7  and  9:10-11).  —  Heb.  almuggtm,  resp.  al- gummfm  (pi.).  The  singular  of  these  words  must be  almdgh,  resp.  algdm,  so  that  the  forms almug  and  algum  are  incorrect.  They  should  be replaced  by  almog,  resp.  algom. alnage,  n.,  measurement  by  the  ell.  —  OF.  aul- nage  (F.  aunage),  fr.  aulne,  ‘ell’,  fr.  Frankish *alina,  prop,  ‘forearm’,  which  is  rel.  to  OHG. elina,  OE.  eln,  ‘ell’.  See  ell  and  -age.
4908:Bible,  n.  —  ME.  bible,  fr.  OF.  (  —  F.)  bible,  fr.  L. biblia,  fr.  Gk.  fkpxia,  ‘collection  of  writings’, pi.  of  [hpXtov,  ‘paper,  scroll,  book’.  This  is  the dimin.  of  JiLpXog,  (luJiXog,  ‘the  inner  bark  of papyrus;  book’,  fr.  BupXog,  Greek  name  of  the famous  Phoen  transit  port,  whence  the  Greeks obtained  the  Egyptian  papyrus,  Gk.  BufSXog  has been  assimilated  fr.  Gebhdl,  the  Heb.-Phoen.
---
4911:name  of  the  city  (lit.  ‘frontier  town’;  cp.  Heb. glbhul,  ‘frontier,  boundary’,  Arab .jabal,  ‘moun¬ tain’,  and  see  javali).  Cp.  Jubayl,  the  actual Arabic  name  of  ancient  Gebhal.  ( Jubayl  prop, is  a  dimin.  formed  from  the  original  name  of  the city.)  For  the  sense  development  of  Bible  fr. Byblos  cp.  parchment.
```


## [2026-09-06T15:27:18.758Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Gibraltar\" KLN_1966.txt | head -10; echo ---JEBEL---; grep -n \"jebel\\|Jebel\\|jabal\\|Jabal\" KLN_1966.txt | head -20",
 "description": "Grep Klein for Gibraltar and jebel"
}
```


### [2026-09-06T15:27:18.827Z] TOOL RESULT

```
16118:Gibraltar,  n.,  name  of  the  Rock  at  the  western entrance  to  the  Mediterranean.  —  Fr.  Arab. jabal  (in  vulgar  pronunciation  jebel)  al  Tdriq, ‘mount  of  Tariq’,  named  after  Tariq,  the  Mos¬ lem  invader  of  Spain  who  landed  there  in  71 1. See  javali  and  cp.  Bible.
16119:gibraltar,  n.,  American  name  of  a  hard  (‘rocky’) candy.  —  Named  after  the  fortress  Gibraltar. See  prec.  word.
20193:Derivatives:  jaunti-ly,  adv.,  jaunti-ness,  n. jaup,  intr.  and  tr.  v.,  to  splash  (Scot,  and  N.  of England).  —  Of  imitative  origin, javali,  n.,  the  collared  peccary.  —  Amer.  Sp. javali,  fr.  Sp.  jabali,  ‘wild  boar’,  fr.  Arab,  jabalt, ‘pertaining  to  the  mountains,  inhabitant  of mountains’,  adj.,  formed  fr.  jabal,  ‘mountain’, which  is  rel.  to  Heb.  g(bhul,  ‘frontier,  bound¬ ary’,  orig.  ‘earth  wall  or  mountain  serving  as boundary’.  Cp.  Bible  and  the  first  element  in Gibraltar.
---JEBEL---
3675:assassin,  n.,  murderer.  —  F.,  fr.  It.  assassino,  fr. Arab,  hashshashln,  ‘drinkers  of  hashish',  fr. hashish,  ‘hemp’ ;  see  hashish.  The  first  assassins were  the  fanatic  followers  of  the  Shaykh-ul- Jabal  (the  Old  Man  of  the  Mountains),  who committed  their  murders  under  the  intoxication of  hashish.  The  plural  suff.  -in  in  assassin  was mistaken  for  part  of  the  word.  Cp.  Bedouin. Derivatives:  assassin-ate,  tr.  v.,  assassin-at- ion,  n.
4911:name  of  the  city  (lit.  ‘frontier  town’;  cp.  Heb. glbhul,  ‘frontier,  boundary’,  Arab .jabal,  ‘moun¬ tain’,  and  see  javali).  Cp.  Jubayl,  the  actual Arabic  name  of  ancient  Gebhal.  ( Jubayl  prop, is  a  dimin.  formed  from  the  original  name  of  the city.)  For  the  sense  development  of  Bible  fr. Byblos  cp.  parchment.
16118:Gibraltar,  n.,  name  of  the  Rock  at  the  western entrance  to  the  Mediterranean.  —  Fr.  Arab. jabal  (in  vulgar  pronunciation  jebel)  al  Tdriq, ‘mount  of  Tariq’,  named  after  Tariq,  the  Mos¬ lem  invader  of  Spain  who  landed  there  in  71 1. See  javali  and  cp.  Bible.
20193:Derivatives:  jaunti-ly,  adv.,  jaunti-ness,  n. jaup,  intr.  and  tr.  v.,  to  splash  (Scot,  and  N.  of England).  —  Of  imitative  origin, javali,  n.,  the  collared  peccary.  —  Amer.  Sp. javali,  fr.  Sp.  jabali,  ‘wild  boar’,  fr.  Arab,  jabalt, ‘pertaining  to  the  mountains,  inhabitant  of mountains’,  adj.,  formed  fr.  jabal,  ‘mountain’, which  is  rel.  to  Heb.  g(bhul,  ‘frontier,  bound¬ ary’,  orig.  ‘earth  wall  or  mountain  serving  as boundary’.  Cp.  Bible  and  the  first  element  in Gibraltar.
24897:nadir,  n.,  the  point  opposite  the  zenith;  the  point directly  under  one’s  feet ;  the  lowest  point.  — ME.,  fr.  OF.  (=  F.),  fr.  Arab,  naqtr  in  the  term naqfr  assamt,  lit.  ‘(the  point)  opposite  to  the  zen¬ ith’,  fr.  ndzara,  ‘he  looked  at ;  he  considered,  ex¬ amined’,  which  is  rel.  to  Heb.  natzar,  ‘he  watch¬ ed  over,  guarded’,  Aram.-Syr.  tftar,  of  s.m., Ethi¬ op.  na}dra,  ‘he  looked  at,  observed’,  Akkad. nafaru,  ‘to  watch  over,  protect’.  Cp.  nazir. nadorite,  n.,  a  lead  chloride  and  stibnite  (mineral.) —  Named  after  Jebel  Nador  in  the  department of  Constantine  in  Algeria.  For  the  ending  see subst.  suff.  -ite. naevus,  n.  —  See  nevus.
```


## [2026-09-06T15:27:27.056Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport sys\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# map line no -> leaf\ntargets=[2326,4908,4911,16118,20193]\nimport bisect\nleaf=0; res={}\nfor i,l in enumerate(lines,1):\n    if '\\f' in l: leaf+=l.count('\\f')\n    if i in targets: res[i]=leaf\nprint(res)\n\"",
 "description": "Compute leaf numbers for Klein hits"
}
```


### [2026-09-06T15:27:28.618Z] TOOL RESULT

```
{2326: 41, 4908: 100, 4911: 100, 16118: 354, 20193: 446}
```


## [2026-09-06T15:27:33.239Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==101' KLN_1966.txt | head -20; echo \"=== leaf 355 (Gibraltar) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==355' KLN_1966.txt | head -8",
 "description": "Print leaf content around Bible and Gibraltar"
}
```


### [2026-09-06T15:27:35.005Z] TOOL RESULT

```
��,  fr.  beurre,  ‘butter’. See  prec.  word.
bevel,  n.,  inclination  of  a  surface.  —  OF.  "baivel (whence  F.  beveau,  biveau),  ‘bevel  rule’,  fr.  OF. baif,  ‘with  an  open  mouth’,  fr.  baer,  beer,  ‘to gape’.  See  bay,  ‘part  in  the  wall’,  and  cp.  words there  referred  to.
Derivatives:  bevel,  tr.  v.  bevel(l)-ed,  adj.,  be- vel(l)-er,  n.
beverage,  n.  —  OF.  bevrage,  bovrage  (F.  breu- vage),  fr.  beivre,  boivre  (F.  boire),  ‘to  drink’,  fr. L.  bibere.  See  bibulous  and  -age  and  cp.  bevy, abreuvoir.
bevue,  n.,  error,  blunder.  —  F.  bevue,  ‘blunder, mistake,  slip’,  fr.  OF.  bes-vue,  lit.  ‘an  erroneous vue’,  fr.  pejorative  pref.  bes-,  which  derives  fr. L.  bis,  ‘twice’  (see  bis-;  for  sense  development  cp. OF.  bes-torne,  ‘badly  turned’,  lit.  ‘twice  turned’), and  fr.  vue,  ‘sight’,  prop.  fern.  pp.  of  voir,  ‘to
166
169
see’,  fr.  L.  videre,  ‘to  see’.  See  vision  and  cp. words  there  referred  to.
bevy,  n.,  i)  a  flock  of  birds;  2)  a  company,  esp.  of women.  —  F.  bevee,  ‘a  flock  of  larks  or  quails’, fr.  It.  beva.  The  orig.  meaning  was  prob.  ‘a  com¬ pany  of  drinking  birds’,  fr.  It.  bevere,  ‘to  drink', fr.  L.  bibere.  See  bibulous  and  cp.  prec.  word, bewail,  tr.  v.  —  Formed  fr.  be-  and  wail, beware,  intr.  and  tr.  v.  —  Formed  fr.  be-  and ware,  adj.
bewilder,  tr.  v.  —  Formed  fr.  be-  and  wilder. Derivatives:  bewilder-ed,  adj.,  bewilder-ed-ly, adv.,  bewilder-ed-rtess,  n.,  bewilder-ing,  adj.,  he- wilder-ing-ly,  adv.
bewitch,  tr,  v.  —  Formed  fr.  be-  and  witch. Derivatives:  bewitch-ed,  adj.,  bewitch-ing,  adj., bewitch-ing-ly,  adv.
bewray,  tr.  v.,  to  reveal,  divulge  ( archaic )  — ME.  bewreien,  bewreyen,  ‘to  reveal’,  fr.  be-  and OE.  wregan,  ‘to  accuse’,  which  is  rel.  to  OS. wrogian,  OFris.  wrogia,  OHG.  ruogen,  MHG. riiegen,  ‘to  accuse’,  G.  riigen,  ‘to  censure’,  Goth, wrohjan,  ‘to  accuse’,  ON.  rcegja,  ‘to  slander,  de¬ fame’,  Du.  wroegen,  ‘to  prick’  (said  of  con¬ science),  OE.,  OS.  wrdht,  OFris.  wrogie,  MHG. ruoge,  riiege,  Goth,  wrohs,  ‘accusation’,  G.  Riige, ‘censure’,  ON.  rog,  ‘quarrel,  slander’, bey,  n.,  1)  governor  of  a  district  in  Turkey;  2)  a Turkish  title  of  honor.  —  Osmanli  equivalent of  Turk.  beg.  Cp.  beg,  ‘bey’,  begum, beylic,  beylik,  n.  —  Turk.,  formed  fr.  bey  and -lik,  a  suff.  expressing  quality.  Cp.  pashalik. beyond,  adv.  and  prep.  —  ME.  biyeonde,  biyonde, fr.  OE.  begeondan,  ‘beyond’,  fr.  be-  and  geond, ‘yond,  yonder’.  See  yon,  yond,  yonder. Derivative:  beyond,  n.
bezant,  n.,  a  gold  coin.  —  Orig.  ‘coin  of  Byzan¬ tium’,  fr.  OF.  besan,  besant,  fr.  L.  byzantius. short  for  Byzantius  nummus,  ‘Byzantine  coin’. See  Byzantine.
bezel,  n.,  a  sloping  edge.  —  OF.  bezel  (F.  biseau ), ‘a  sloping  edge,  bevel,  prob.  orig.  meaning  "a stone  with  two  angles’;  fr.  VL.  *bis-alus,  ‘hav¬ ing  two  angles’,  fr.  L.  bis,  ‘twice’,  and  ala,  ‘wing, side’.  See  bis-  and  ala.
bezesteen,  n.,  a  bazaar.  —  Pers.  bezestan,  formed fr.  bez  (whence  Arab,  bazz),  ‘flax,  linen  clothes’, and  -stan,  a  suff.  denoting  place,  which  is  rel, to  Avestic  stana-  (in  compounds),  ‘place’,  lit. ‘a  place  where  to  stand’.  See  Hindustani, bezetta,  bezette,  n.,  a  dyeing  material  made  by dipping  linen  rags  into  certain  coloring  matters. —  It.  pezzetta,  dimin.  of  pezza,  ‘piece  of  cloth’, a  word  of  Gaulish  origin.  See  piece  and  -ette. bezique,  n.,  a  card  game.  —  F.  besigue,  of  un¬ known  origin.
bezoar,  n.,  orig.  a  term  for  antidote-,  later  used for  concoctions  found  in  the  stomach  or  in¬ testines  of  certain  animals  and  thought  to  have antidotal  properties.  —  F.  bezoard,  fr.  Sp.  be¬ zoar  (cp.  Port,  bezuar),  fr.  Arab,  badizdhr,  often shortened  into  bazahr  (see  Freytag,  Lexicon
I
Arabico-Latinum,  I,  79a  and  b),  ult.  fr.  Pers. badzahr,  padzahr,  ‘counterpoison,  bezoar  stone’, lit.  ‘protecting  (against)  poison’,  fr.  pad,  ‘pro¬ tecting,  guarding;  guardian,  lord,  master’,  and zahr,  ‘poison’.  For  the  first  element  see  padi- shah.  The  second  element  is  rel.  to  Pers.  zehre, ‘gall,  bile’,  Pahlavi  zahr,  ‘poison’,  Avestic  zara-, ‘gall,  bile’,  and  cogn.  with  Gk.  yoXf],  ‘gall,  bile’. See  choler.
bezonian,  n.,  knave,  rascal.  —  Formed  with  suff. -ian,  fr.  It.  bisogno,  ‘want,  need’,  which  is  rel.  to F.  besogne,  ‘work,  task,  job’,  besoin,  ‘want, need’,  OProveng.  bezonh,  ‘want’,  bezonha,  ‘want, work,  task’.  These  words  prob.  derive  fr.  Fran¬ kish  *bisunnia,  which  is  formed  fr.  hi-,  ‘by’,  be¬ side’  (see  be-),  and  *sunnia  (rel.  to  OS.  sunned), ‘care’,  whence  Olt.  sogna,  F.  soin,  OProveng. sonh,  sonha,  ‘care’.  See  Dauzat,  DELF.,  p.85 s.v.  besogne.
bezzle,  tr.  v.,  to  plunder,  consume;  intr.  v.,  to revel  (dial.  English).  — -  OF.  besillier,  ‘to  tor¬ ment’,  freq.  of  beser,  ‘to  be  scared,  be  startled’ (said  of  cows  stung  by  gadflies),  fr.  OHG.  615- 3an,  ‘to  bite,  sting’;  see  bite  and  cp.  embezzle. See  R.  Grandsaignes  d'Hauterive,  Dictionnaire d’ancien  frangais,  Paris,  1947,  p.62  s.v.  besillier.
=== leaf 355 (Gibraltar) ===
 by  the English  poet  William  Wordsworth  (1770-1850). giant,  n.  —  ME.  geant,  fr.  OF.  geant  (F.  geant), fr.  earlier  jaiant,  fr.  VL.  *gagantem,  acc.  of *gagas,  assimilated  vr.  L.  gigas,  ‘a  giant’,  fr. Gk.  ytya q,  ‘a  giant’,  fr.  I’tyat;,  'any  of  the  sons of  the  Earth  and  Tartarus’,  which  is  prob.  a pre-Hellenic  word.  Cp.  gigantic.
Derivatives:  giant,  adj.,  giant-ess,  n.,  giantism (q.v.),  giant-like,  adj.
giantism,  n.,  pathological  condition  characterized by  abnormal  tallness  (med.)  —  A  hybrid  formed from  prec.  word  with  -ism,  a  suff.  of  Greek  ori¬ gin.  The  correct  form  is  gigantism  (q.v.) giaour,  n.,  a  term  applied  by  the  Turks  to  all  non- Mohammedans.  —  Turk,  giaur,  ‘infidel’,  fr. Pers.  gaur,  a  variant  of  gabr,  ‘fireworshipper’. See  Gheber.
gib,  n.,  a  tomcat.  —  From  Gib,  pet  form  of  the name  Gilbert.
gib,  n.,  a  hook.  —  Of  uncertain  origin, gibbar,  n.,  a  finback  whale  ( obsol .)  —  F.,  fr.  Arab. jabbdr,  ‘giant,  tyrant’,  which  is  rel.  to  Heb.  gibbdr, ‘strong,  mighty;  mighty  man,  hero’.  See  Gabriel, gibber,  intr.  v.,  to  speak  unintelligibly.  —  Of  imi¬ tative  origin.  Cp.  jabber, gibberish,  n.,  unintelligible  talk.  —  Formed  from prec.  word  with  adj.  suff.  -ish. gibbet,  n.,  gallows.  —  ME.  gibet,  fr.  OF.  (=  F.) gibet,  ‘gallows;  a  bent  stick’,  dimin.  of  OF. gibe,  ‘staff,  stick’,  which  is  perh.  of  Teut.  origin; see  Bloch-Wartburg,  DELF.,  p.281  s.v.  gibet. Cp.  jib,  ‘the  projecting  arm  of  a  crane’. Derivative:  gibbet,  tr.  v.
gibbon,  n.,  a  small,  long-armed  ape.  —  F.,  a  name of  Indian  origin  brought  to  Europe  by  the Marquis  Joseph-Frangois  Dupleix  (1697-1763), governor-general  of  the  French  possessions  in India  (1742-54).
gibbose,  adj.,  gibbous.  —  See  gibbous, gibbosity,  n.  —  F.  gibbosite.  See  next  word  and -ity.
gibbous,  adj.  —  L.  gibbosus,  ‘humpbacked’,  fr. gibbus,  ‘hump’,  which  is  of  uncertain  origin.  It
```


## [2026-09-06T15:27:53.189Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==355' KLN_1966.txt | grep -nE '^\\s*[0-9]{2,4}\\s*$'; echo \"---leaf101 nums---\"; awk 'BEGIN{RS=\"\\f\"} NR==101' KLN_1966.txt | grep -nE '^\\s*[0-9]{2,4}\\s*$'; echo \"---leaf447 (javali)---\"; awk 'BEGIN{RS=\"\\f\"} NR==447' KLN_1966.txt | grep -nE '^\\s*[0-9]{2,4}\\s*$'",
 "description": "Find printed page numbers on relevant leaves"
}
```


### [2026-09-06T15:27:55.091Z] TOOL RESULT

```
---leaf101 nums---
6:166
7:169
---leaf447 (javali)---
23:826
43:827
```


## [2026-09-06T15:28:06.760Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 353 354 355 356 357 102 103; do echo \"leaf $n:\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' KLN_1966.txt | grep -nE '^\\s*[0-9]{2,4}\\s*$' | tr '\\n' ' '; echo; done",
 "description": "Page numbers on neighbouring leaves"
}
```


### [2026-09-06T15:28:08.638Z] TOOL RESULT

```
leaf 353:

leaf 354:
18:033 
leaf 355:

leaf 356:
30:658 
leaf 357:
3:659 44:660 
leaf 102:
8:170 9:171 
leaf 103:
10:172 11:173 62:174
```


## [2026-09-06T15:28:15.765Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==102' KLN_1966.txt | head -14",
 "description": "Print leaf 102 (pp.170-171)"
}
```


### [2026-09-06T15:28:17.518Z] TOOL RESULT

```
ip  of  the Bible.  —  Compounded  of  biblio-  and  Gk. -Xarpeia,  -Xarpla,  fr.  Xa-rpela,  ‘hired  labor,  wor¬ ship’.  See  -latry.
bibliomancy,  n.,  divination  by  opening  a  book, esp.  by  opening  the  Bible.  —  Compounded  of biblio-  and  Gk.  fravreta,  ‘oracle,  divination’. See  -mancy.
biblomania,  n.,  book  madness.  —  Compounded of  biblio-  and  Gk.  pavia,  ‘madness,  frenzy’.  See
-mania.
biblomaniac,  adj.  —  Compounded  of  biblio-  and ML.  maniacus,  ‘maniac’.  See  maniac, bibliophil,  bibliophile,  n.  a  lover  of  books.  —  F. bibliophile,  ‘lover  of  books’,  compounded  of biblio-  and  Gk.  91X0?,  ‘friend’.  See  -phil. Derivatives:  bibliophil-ic,  adj.,  bibliophil-ism,  n., bibliophil-ist,  n.,  bibliophil-y ,  n. bibliopole,  n.,  bookseller.  —  L.  bibliopola,  fr.  Gk. (3i[iXio77coXy;p,  ‘bookseller’,  which  is  compounded of  [kfJXtov,  ‘book’  (see  biblio-),  and  tccoXy]<;, ‘merchant,  seller’,  which  derives  fr.  I.-E.  base *pel-,  ‘to  sell,  purchase,  barter,  gain’.  See monopoly.
bibliotheca,  n.,  a  library.  —  L.  bibliotheca,  fr. Gk.  BiSXiofHjxr;,  lit.  ‘a  case  for  books’,  which is  compounded  of  pipXiov,  ‘book’,  h^xr,,  ‘case, chest,  sheath’.  See  biblio-  and  theca. Derivative:  bibliothec-al,  adj. bibliothecary,  n.,  a  librarian  —  L.  bibliothecdrius, fr.  bibliotheca.  See  prec.  word  and  subst.  suff. -ary.
Derivative:  bibliothecar-ial,  adj. bibulous,  adj.,  fond  of  drink;  spongy.  —  L.  bi-
170
171
bulus,  ‘drinking  readily’,  fr.  bibere  ‘to  drink’, assimilated  fr.  *pibere,  which  is  cogn.,  with  OI. plbati,  ‘drinks’,  OIr.  if  ‘drink!’,  OW.  iben,  ‘we drink’;  from  the  reduplication  of  I.-E.  base  *pi-, *pd(i)-,  ‘to  drink’,  whence  OI.  pdti,  ‘drinks’, pdyayati,payate,  ‘gives  to  drink*,  pdtiam,  ‘bev¬ erage’,  Arm.  lmpem,  ‘I  drink’,  Gk.  -rrfvetv,  ‘to drink’,  716014,  ‘a  drink’,  716x04,  ‘a  drinking,  a drinking  bout’,  L.  potare,  ‘to  drink’,  potio,  ‘a draft,  drink’,  OSlav.  pijQ,  piti,  ‘to  drink’.  See potion  and  cp.  words  there  referred  to.  Cp.  also abreuvoir,  beverage,  bevy,  bib,  ‘to  drink’,  bib, ‘piece  of  cloth’,  biberon,  imbibe,  imbrue.  For  E. -ous,  as  equivalent  to  L.  -us,  see  -ous. Derivatives:  bibulous-ly,  adv.,  bibulous-ness,  n. bicameral,  adj.  having  two  chambers  (said  of legislative  bodies).  —  Formed  fr.  bi-,  camera and  adj.  suff.  -al.
bicarbonate,  n.  ( chem .)  —  Formed  fr.  bi-  and
carbonate.
bice,  n.,  blue  or  green  pigment.  —  F.  bis,  ‘brown, tawny’,  rel.  to  OProven?.  bis,  It.  bigio;  of  un¬ known  origin.
bicentenary,  adj.,  pertaining  to  a  period  of  two hundred  years;  n.,  a  bicentennial.  —  Formed fr.  bi-  and  centenary.
```


## [2026-09-06T15:28:29.897Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && sed -n '1,120p' SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T15:28:29.937Z] TOOL RESULT

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


## [2026-09-06T15:28:31.983Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && sed -n '120,260p' SOURCE_MATRIX.md",
 "description": "Rest of source matrix"
}
```


### [2026-09-06T15:28:32.020Z] TOOL RESULT

```
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


## [2026-09-06T15:28:40.874Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT Bible ===\"; grep -n \"BIBLE\\|^Bible\\|Byblos\" SKT.txt | head -5; echo \"=== SKT Gibraltar ===\"; grep -n \"Gibraltar\" SKT.txt | head -3; echo \"=== LKT jabal/Gibraltar ===\"; grep -n -i \"gibraltar\\|dschebel\\|ǧabal\\|gabal\" LKT.txt | head -10; echo \"=== DEV ===\"; grep -n -i \"gibraltar\\|djebel\" DEV.txt | head -8; echo \"=== PHN ===\"; grep -n -i \"gibraltar\\|djebel\" PHN.txt | head -8",
 "description": "Grep Skeat, Lokotsch, Devic, Pihan"
}
```


### [2026-09-06T15:28:40.970Z] TOOL RESULT

```
=== SKT Bible ===
1752:BIBLE.
=== SKT Gibraltar ===
=== LKT jabal/Gibraltar ===
1570:627.  Ar.  gaball :
1571:Adj.  zu  ar.  gabal  'Berg',  vollständig hinzir  gabali  'Berg-,  Wildschwein';  hier- aus sp.  jabali  'Eber',  in  Südamerika Pekari  Dicotyles  torquatus  Cuv.,  jaba- li na  'wilde  Sau',  jabato  'Eberferkel',  pg. javali,  frz.  javari,  javaris  'amerikani- scher Eber'.  [DE  288.  Eguilaz  425. ML  3940.
=== DEV ===
1653:-  C'est  ainsi  que  d'anciens  actes  en  latin  interprètent  par  centummices, cent  noix,  le  nom  du  village  de  Sannois,  près  Paris.  Les  Portugais,  trou- vant dans  le  royaume  d'Adel  une  montagne  nommée  djebel  al-Jîl,  montagne de  l'éléphant,  l'appelèrent  Monte-Fctice.  Le  voyageur  Poncet  nomme  le monastère  de  Bisan,  on  Abyssinie,  monaslère  dr  hi  Vision.  (Voy.  Bruce, édit.  Panckouke,  t.  l",  5of),  et  t.  II,  160.)
=== PHN ===
701:qui prend sa source dans le Djebel echcheikh ou Antiliban,
1120:de Gibraltar, entre Ceuta et Tanger, vis-à-vis de Tarif, h
1572:de Gibraltar et vinrent en Espagne, dont ils subjuguèrent tout
1777:Aussi i;:>U;X J^A^ [djebel ^arafât] signifie-t-il montagne de la re-
1890:appelé SjJi' ^^ [chéikk eldjebel] le Vieux de la Montagne, se
1897:eldjebel, en 1190. Les assassins de la Perse furent détraits
5293:réellement un nom propre. Or gibel (et mieux djebel) veut dire
5295:volcan, appelé en arabe jUJt J^ks^ [djebel ennâr]^ c'est-à-dire
```


## [2026-09-06T15:28:41.983Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NAT p110 area ===\"; grep -n -i \"byblos\\|gebal\\|papyrus\" NAT_2005.txt | head -20",
 "description": "Grep Berlitz Native Tongues"
}
```


### [2026-09-06T15:28:42.044Z] TOOL RESULT

```
=== NAT p110 area ===
795:The first true, not syllabic, alphabet is generally accepted as one found in Byblos in Phoenicia, dating from 1000 BC or earlier. Byblos was a port from which papyrus, for use in writing, was exported to Egypt, where pictorial hieroglyphic (not alphabetic) writing had already been in use for thousands of years. Byblos has been immortalized in the original Greek word for “rolled book,” biblion, from which Western languages get the words “‘bible,” “‘bibliophile,”’ “bibliography.”
798:In spite of the honor accorded to Byblos as the first known place where a close-to-pure alphabet was used, evidence that alphabetic symbols or letters were used in many other parts of the ancient Mediterranean world has surfaced in discoveries in Italy, central France, western Spain and Portugal, western North Africa, and the islands of the Mediterranean. This evidence suggests that some form of alphabetical writing was used more generally and earlier than previously estimated. Its use was doubtless spread by early Cretan or Phoenician seafarers, who either got it from an earlier culture or who evolved a nonrepetitive sign alphabet for marking days in keeping track of the duration of long sea voyages.
948:European travelers to Egypt up to about 1800 often wondered whether the hieroglyphics which they saw on obelisks, the walls of temples and tombs, mummy cases, and sheets of papyrus were writing, pictures, or just decoration. One student of ancient history, the French Abbé Tandeau de Saint-Nicholas, proclaimed, even while Egyptologists were attempting to decipher the hieroglyphics: “It is as clear as day that the hieroglyphics are purely ornamental.”
```


## [2026-09-06T15:28:47.945Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\ntxt=open('NAT_2005.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=0\nfor i,l in enumerate(txt,1):\n    leaf+=l.count('\\f')\n    if i in (795,798): print(i,'leaf',leaf)\n\"; echo \"=== SKT BIBLE ctx ===\"; sed -n '1748,1760p' SKT.txt; echo \"=== PHN 5290-5300 ===\"; sed -n '5288,5300p' PHN.txt",
 "description": "Locate NAT leaf, print Skeat and Pihan context"
}
```


### [2026-09-06T15:28:49.530Z] TOOL RESULT

```
795 leaf 127
798 leaf 128
=== SKT BIBLE ctx ===
imbrue,  embrew,  to  moisten,  drench. (F.  —  L.)  O.  F.  embryer;  x'embrutr,  '10 imbrue  or  bcdaUe  himself  with;*  Cot. — F.  em-  (ih  in,  in) ;  and  a  causal  verb 'bez'rer,  to  give  to  drink,  turned  into  -hrfver in  the  iOlh  cent.,  nrid  then  into  -hmer\  sec F.  abrtHver  in  Urachcl.  —  0.  F.  bevre  (F. boire),  to  drink.  — L.  bibert.
imbue,  to  cause  to  drink  in,  tinge deeply.  (L.)  L.  imbuett,  to  cauie  to drink  in;  i%hcrc  buere  is  a  causal  form, allied  to  bibtre.  to  dnnk.
I
38
BIBLE.
Biblo.  (F,-L.-Gk)  M.E.  WW/.-F. hbii.^V,.  /^td/ia. ~Gk.  0t8Kia,  collection  of writings,  pi.  of  $i$\iov,  httle  book,  dimin. of  Biti\ot,  a  book.^Gk.  ^u0Aot,  Ej^yprUn pApvnis :  hence,  a  bonk.
bibliography.  (Gk.)  Gk.  ^ii9X/o-,  for 0i0y,tiir  ;  and  yr^tiv^  Xo  write.
bibliomania  (Gk.)    Gk.  d.^xio.,  for $i$kia9 ;  and  Mania. Bioe.    <F.)     Properly  •  grayish  ; '  hence, grayish  blue— F.  6ut,  fern,  of  bit,  du&ky. CI.  It-il.  big^io,  gray.     Origin  unkuown. Bicker,  to  skirmish.  (C.)     See  Peak. Bid  (i),  to  pray.  (E.>     Nearly  obsolete; ireserved  in  &tJ,iinf-^/ixyfr,  ami  in  to  ^tJ (pray  prayers).     M  E.  hidden.     A.  S. \hU4iin.  +  Uo.    bidden  ;    G.  HtUn  ;    Goth.
oaad.  (E.>  Orig.  '  a  prayer ; '  hence  a perforated  ball,  for  counting  prayerv  M.  E. otde,  a  prayer,  a  bead.  A.S.  btd,  gehed, ApmycT.^  A.S.  btddan,  to  pray.4-G.^^/; ^Dti.  mr,  abed.
beg.  (£.)  Frequentative  of  Ai*/.  M.  E. l^tj^en,  A.S.  btdecian,  to  beg;  frequent. ^oipiiMan,  to  pray.     Cf.  Goth,  bidagwa,  a
;gar ;  G.  btttUr,  a  b^gar,  from  bitttn.
lid  (j\  to  command.  (K.)  M.  E.  M/^n. •-A.S.  htSdan,  to  command. +  0  b\ettH\ Goth,  ana-hiudan ;  Skt.  Mhaya,  to  inform, Cfluial  of  hndh,  to  awake,  understand. (VJinUDII.)    Confnseil  withBid(i).
beadle.  (F.  -  Tent.)  M.  E.  bedtt.  - O  F  bedel^  F.  bedeau,  a  bca'lle;  lit.  *  pro- claimer,*  or  *mes«<^igcr.' —  G.  bitten,  Du. bitdeH\  co^atc  wilb  A.S.  bttUan,  to  bid. Cf.  A.  S.  byUl^  a  beadle,  from  Mdan.
=== PHN 5290-5300 ===
de l'Etna, volcan célèbre, situé sur la côte orientale de la Si-
cile, dans la province de Catane. Mais ils ont tort d'employer
devant le mot arabe son correspondant français mont, car le
la .180 GIB
lecteur peut croire que Gibel, écrit avec une majuscule, est
réellement un nom propre. Or gibel (et mieux djebel) veut dire
tout simplement montagne et ne peut à lui seul désigner un
volcan, appelé en arabe jUJt J^ks^ [djebel ennâr]^ c'est-à-dire
montagne de feu. Cette dernière dénomination , appliquée au
mont Etna, est tout à fait orientale; et, si l'usage a fait consi-
dérer jusqu a présent Gibel comme un nom propre, il serait
plus conforme à la raison d'écrire le Gibel (c'est-à-dire le
Mont)^ et non pas le mont Gibel, pléonasme que le bon sens
```


## [2026-09-06T15:29:00.327Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHN GIBRALTAR entry ===\"; grep -n \"GIBRALTAR\\|Gibraltar,\" PHN.txt | head; echo; sed -n '5300,5330p' PHN.txt; echo \"=== SKT leaf ===\"; python3 -c \"\nt=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nleaf=0\nfor i,l in enumerate(t,1):\n    leaf+=l.count('\\f')\n    if i==1752: print('leaf',leaf)\n\"",
 "description": "Pihan Gibraltar entry and Skeat leaf"
}
```


## [2026-09-06T15:29:01.841Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD Bible ===\"; grep -n \"Byblos\\|By'blos\" FSD_vol1.txt | head -5; echo \"=== WEB ===\"; grep -n \"Byblos\" WEB_vol1.txt | head -5; echo \"=== RCH jabal ===\"; grep -n \"jabal\\|Jabal\" RCH.txt | head -10",
 "description": "Grep FSD, WEB, Richardson"
}
```


### [2026-09-06T15:29:02.223Z] TOOL RESULT

```
=== PHN GIBRALTAR entry ===
1120:de Gibraltar, entre Ceuta et Tanger, vis-à-vis de Tarif, h
5302:GIBRALTAR, n. pr. composé, (a.)
10546:Gibraltar, n. pr. composé, (a.)

Mont)^ et non pas le mont Gibel, pléonasme que le bon sens
réprouve.
GIBRALTAR, n. pr. composé, (a.)
(^yo Ju^ [djébel [ou gibel) t^âriq] et ^Jj^lLit J.^ [djebel at^U-
riq] montagne de Tank, ou montagne du rôdeur nocturne, suivant
le sens du mot iâriq en arabe. — Le promontoire appelé Gi-
braltar domine la Méditerranée ; il est situé dans l'Andalousie ,
et forme avec le promontoire de Ceuta , qui lui fait face sur la
côte de Barbarie, à la distance d'environ cinq lieues, l'entrée
orientale du détroit qui porte aussi le nom de Gibraltar. Ces
deux montagnes étaient appelées Calpi et Abyla chez les an-
ciens, et aussi colonnes d'Hercule. — Les Arabes désignent le
détroit de Gibraltar par les mots ^|^^I v^ [^àb elà9wâq\ , ou
forte des marchés, probablement à cause des relations commer-
ciales que ce détroit établit entre l'océan Atlantique et la
Méditerranée. — Au pied de Gibraltar est bâtie une ville du
même nom et qui appartient aux Anglais depuis 170/i, époque
à laquelle ils se sont emparés de ses fortifications par surpriseGIR 181
et sont devenus, par le fait, seuls mattres du détroit. — On
prétend que Gibraltar doit son nom au général sarrasin Tarik
ben Ziad, qui prit possession de cette montagne, l'an 710 de
notre ère, sous le règne de Walid, fils d'Abd elmalek, sixième
khalife Omayyade, pendant que ftfousâ ben Nasir faisait la con-
quête de la Sardaigne.
GILET, s. m. (a.)
ùds^ [djild et djtlid] peau, cuir d'un animal, dont on se sert pour
confectionner des vêtements. — Le gilet est une sorte de cami-
sole de laine ou de coton que l'on porte habituellement soit
par-dessous, soit par-dessus la chemise. Dans certaines con-
trées, on en fait encore aujourd'hui avec des peaux de bétes;
et cet usage remonte sans doute aux premiers temps du monde,
=== SKT leaf ===
leaf 58
```


### [2026-09-06T15:29:02.292Z] TOOL RESULT

```
=== FSD Bible ===
=== WEB ===
=== RCH jabal ===
14423:The  gate  of  the  way,  the  Straits  of  Gibraltar ;   which  last  name is  a   corruption  of  Jabalu’ t   Tarak,  The  mountain  of  Tarak ;   that being  the  spot  where  this  Arabian  general  first  landed,  in  his descent  upon  Spain  from  the  African  shore,  in  the  year  710.
14868:A   f^bb  Batimyah^  The  Batanians,  Ismaelians,  or  Assas- sins,” of  whom  mention  is  so  often  made  in  the  history  of  the Crusades.  The  founder  of  this  sect  of  enthusiasts  was  Hasan Saba,  Shayku’l  jabal  (literally.  Old  man  of  the  mountain,  but  in fact  Sultan,  or  Prince  of  Persian  Irak,  otherwise  named  Jabal, on  account  of  its  mountainous  situation,  the  sovereignty  of  which he  usurped  about  the  year  1090).  His  subjects  were,  upon  re- ligious grounds,  so  entirely  devoted  to  his  service,  that  they  put themselves  to  death  without  hesitation  the  moment  he  gave  the command;  and,  it  may  be  easily  supposed,  were  equally  ready, fearless  of  danger,  to  assassinate  those  whom  lla8an>Saba,  from motives  of  policy,  avarice,,  or  vengeance,  chose  to  number  with the  dead.  This  despotic  and  most  singular  influence  over  his followers  rendered  him  so  dreadfully  formidable  that  he  forced tribute  from  most  of  the  neighbouring  princelj  many  of  whom kept  bodi^qp  of  Ktanists  in  their  pay,  in  order  to  despatch  those who  were  dangerous  to  their  power;  in  consequence  of  which several  Khalifs,  Sultans,  Generals,  Vazirs,  and  other  eminent leaders,  fell  under  the  daggers  of  those  most  determined  villains.
15224:A   <U:AJt  al  hasantyaiy  Betlianian  wheat,  and  in  general  ail wheat  grown  on  plains,  (in  contradistinction  jaballyat
29220:p   ^jt/ijb\^Jabilu8jJabaluSj  or  Jabulusj  A   flatterer,  a   wheedler. A   muleteer,  ^^\9y^jabulus  kardan^  To  flatter,  to  fawn, p   jdbulusty  Flattery,  adulation.  *
29618:The  wrist.  The^bint  of  the  fore-foot  (of  a   camel  or  horse).  A   J^jabl  (from  J-^),  Creating,  forming.  Jabaly  A   moun-
54693:Sifdhdn  also  Isfahan,  The  metropolis  of  Jabal  or Persian  Irak  (the  ancient  Parthia).  It  is  said  to  have  been founded  above  800  years  before  the  Christian  era,  and  derives its  name,  as  supposed,  from  Ispahan  or  Sipahan  (cavalry),  that being  the  principal  station  for  the  Persian  armies,  which,  in  all times,  have  consisted  chiefly  of  horse.  It  was  before  the  reign of  Cyrus  the  capital  of  the  Persian  empire;  but  Pcrsepoli8,Susa, Madain  (Ctesiphon),  and  other  cities,  having  afterwards  alter- nately shared  that  honour,  it  was  not  restored  to  its  former  dig- nity till  the  eleventh  century  of  the  Christian  era,  under  the  Sel- jukian  dynasty.  On  the  fall  of  that  family,  however,  the  dynasty of  Muzaflarians  (conquerors)  attached  themselves  to  Shiraz, which  continued  to  be  the  seal  of  government  till  the  elevation  of the  Safi  family  in  the  sixteenth  century,  by  whom,  but  particularly by  Shah  Abbas  the  Great  (or  the  Cruel),  TspaliSh  was  rendered the  most  extensive  and  most  magnificent  city  of  Asia.
60924:and  hearts  as  the  repositories  of  secrets.  An  iiistruinent  which separates  or  cards  cotton,  ^rnjjjdb  (or  ^a^ijabal)^  Slander- ous, locjiincious,  a   re  viler.
```


## [2026-09-06T15:29:14.572Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON جبل ===\"; grep -n \"جبل\" MON_part1.txt MON_part2.txt | head -20",
 "description": "Grep Mo'in for جبل"
}
```


### [2026-09-06T15:29:14.642Z] TOOL RESULT

```
=== MON جبل ===
MON_part2.txt:1574:غر یز ه. طبیعی ؛ داتی» جبلی؛ فطری. حرارت 
MON_part2.txt:3610:عحجبل ان" ۰-۱ [. ی نت عب‌داننده ] 
MON_part2.txt:15173:قنفذ جبلی: (جان.) ته تشی را گویند که بنام 
MON_part2.txt:15176:خارپشت جبلی و دلدل نیز موسوم است. 
MON_part2.txt:16351:که منمون جبله» فعل» صفت قید و کلمات 
MON_part2.txt:21599:کراوية رومی» کراويةٌ جبلی. 
MON_part2.txt:22092:می‌شود؛ کرفس جبلی؛ کرفس الجبل» داغ 
MON_part2.txt:22910:می‌شود؛ موسوم به جبل زهره. در قسمت 
MON_part2.txt:26384:معنی): کمر کوه: ميانةٌ کوه» وسط جبل. کمر 
MON_part2.txt:26574:الجبل. کمون ملوکی: (گیا.) نانخواه. 
MON_part2.txt:37581:الف - (لغت عربی) جبل ( کوه). ب - (نج. 
MON_part2.txt:39170:به لدن؛ فطری» جبلی. علم لدنی: دانشی که 
MON_part2.txt:53174:اروپاو آفریقا می‌روید؛ فودنج جبلی» 
MON_part2.txt:60412:تعجبل کننده. 
MON_part2.txt:72500:صفتی با کاری: جبلی و فطری بودن آن 
MON_part2.txt:91762:خالقالفهد» ارنیکای جبلیه؛ تتبااکوی کوهی» 
MON_part2.txt:92621:است. غده زیر مغزی» جبل رمادی دماغ. 
MON_part1.txt:33049:فودنج جبلی» فو تنج بری. (یز.) عرق بودینه: 
MON_part1.txt:47153:جبل: اه« (ع.| (ا.) کوه؛ ج. جبال» اجبال. 
MON_part1.txt:47154:جبل جبلت: ۰00 (ع. جبلة] ()
```


## [2026-09-06T15:29:16.068Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v2 جبل ===\"; grep -n \"جبل\" BQT_v2_pages.txt | head -15; echo \"=== AFM ===\"; grep -n \"جبل\" AFM_pages.txt | head -8; echo \"=== FVQ jabal ===\"; grep -n -i \"jabal\\|djabal\" FVQ.txt | head -8",
 "description": "Grep BQT, AFM, FVQ"
}
```


### [2026-09-06T15:29:16.143Z] TOOL RESULT

```
=== BQT v2 جبل ===
1036: ‫جبلاج ‪ -‬بکر اول ولام والفہ پروزن‬
1043:  ‫بروزن لك لك » سخت شن‬        ‫س‬           ‫جبلك‬                  ‫جبر آهنگ » براای قرشت والف‬
1046: ‫۔ با ها برورن اسفرنگه‪,‬‬       ‫جبلهنگ‬
1059:   ‫© ‪ -‬لاینی ‪« 7115۳6‬کازر >‬                                       ‫‪,‬‬   ‫جبلاهنگه‬   ‫‪,‬‬       ‫جبلهنکگ‬   ‫‪:‬‬   ‫رك‬    ‫‪۴‬‬
2183:                ‫جلویز‪ ,‬جلیز ‪.‬‬    ‫‪۷‬ك‪:‬‬ ‫ر‬         ‫و رك‪ :‬جبر آهنکه‪ ,‬جبلهنگه‪.‬‬  ‫و ‪ ۰۲‬ولك ‪ ۱‬ص ‪۵۳‬‬
2188:‫را از آن جلق‬         ‫هزار وهشتاد قسم کنند وهرقسمی‬             ‫ات که بعربی حماض جبلی‌خوانند‪ .‬درد مفاصل‬
2193:                                                                              ‫جبلنحتلح‌‬
3026: ‫(بین سقز و ساوجبلاغ) ها » در کرمانجی‌سنندج ‪10‬ز وھ‪1‬ه ز‪0‬ز ‪ ,‬در کرمانجی کردستان‬
7809:         ‫‏(‪ )٤‬کوه کروابند وبعربی جبل خوانند ‪.‬‬
12352: ‫وهی است وبعریی جبل خوانند ‪ -‬وبضم اول‬
15275:     ‫«جبلتش برصفت ذمیمة کبر وانالیت وخویشتن داری مجبول‌بود» « حبیب‌السیر ج ‪۳‬‬
19294:  ‫بسیار مقام میکرد و ازینرو بدین نام خوانده شد ‪ -‬ویز دسکره قربه‌ایست مقابل جبل (بفتح اول‬
22729:                      ‫ی‌ججبل‌‬
23237:    ‫ست‪ * .‬اسشق‪ :»۰۱‬کخرادرنج»ببرون کرد ‪-‬ن دکقردعنه اغراجبلدکردن‪ ,‬مرکدورددن۔‬
27856:                            ‫‪ -0‬از ‪ :‬زر( آب ‪.‬‬                  ‫و کوههای مرتفع بینفید وجبلین‪ ,‬پادشده ‪.‬‬
=== AFM ===
364:ܡܠ 100 » وقمل انه اسم رنحان جبلي ورقه - ورق الريحان ورائحته
876:وهو من مننولات البلتم ويعرف بعشب الجبل .£
3112:وهو ارق وهو انواع بري وبستاني وجبلي ونهري ٠‏ والنهري منة يقال ` 3 :
=== FVQ jabal ===
```


## [2026-09-06T15:29:24.426Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '47150,47160p' MON_part1.txt; echo \"=== الطارق ===\"; grep -n \"الطارق\" MON_part1.txt MON_part2.txt | head -10; echo \"=== جبل الط ===\"; grep -rn \"جبل الطارق\\|جبل‌الطارق\" . --include=*.txt 2>/dev/null | head -10",
 "description": "Mo'in jabal context and Gibraltar in Persian sources"
}
```


### [2026-09-06T15:29:24.512Z] TOOL RESULT

```
هر چیز آکنده از پشم و پنبه مانند توشک و 
بالش. 

جبل: اه« (ع.| (ا.) کوه؛ ج. جبال» اجبال. 
جبل جبلت: ۰00 (ع. جبلة] () 
طیعت» سرشت, فطرت» اصل. 


جین: ۰ 1008 [ع ۰](.) ۳ بددلی. 
جبه. (۵-)0092] [ع. . جبه ] (.) جامهٌ کشاد و 
بلند که فراز جامه‌های ( ۳ پوشند. جبه 
=== الطارق ===
=== جبل الط ===
(eval):1: no matches found: --include=*.txt
```


## [2026-09-06T15:29:31.723Z] TOOL CALL #29: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T15:29:31.730Z] TOOL RESULT

```


```


## [2026-09-06T15:29:34.934Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/gabal-",
 "prompt": "Give the full reconstruction entry: meaning of *gabal-, and the descendants listed (Arabic, Hebrew, Phoenician, Ugaritic, Akkadian, Aramaic). Quote exactly."
}
```


## [2026-09-06T15:29:35.330Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Bible",
 "prompt": "Quote the full etymology of Bible, including any mention of Byblos, Gebal, papyrus, biblia, biblion."
}
```


### [2026-09-06T15:29:36.843Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:29:42.588Z] TOOL RESULT

```
# Etymology of Bible

Based on the provided content, here is the full etymology:

The term "Bible" entered English in the early 14th century from Anglo-Latin *biblia* and Old French *bible*. It derives from Medieval and Late Latin *biblia* (a neuter plural interpreted as feminine singular), which came from the phrase *biblia sacra* meaning "holy books"—a translation of Greek *ta biblia to hagia* with the same meaning.

The Latin term traces to Greek *biblion*, meaning "paper, scroll" or "a book as a division of a larger work." The Christian scriptures were called *Ta Biblia* in Greek as early as circa 223 CE.

**Notable point:** The etymology provided does not mention Byblos, Gebal, or papyrus explicitly. The connection to *biblion* (Greek for "paper, scroll") is the closest reference to papyrus materials, though the content does not trace the etymology back to those ancient locations or materials directly.

The word *Bible* eventually replaced the Old English *biblioðece* (from Latin *bibliotheca*) as the standard term for the Christian scriptures.
```


## [2026-09-06T15:29:51.500Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/biblio-",
 "prompt": "Quote the entry for biblio- in full, especially anything about byblos, Byblos, Jebeil, Phoenician port, papyrus, and whether the place name might come from the word rather than vice versa."
}
```


## [2026-09-06T15:29:53.724Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B2%CF%8D%CE%B2%CE%BB%CE%BF%CF%82",
 "prompt": "Quote the Ancient Greek entry βύβλος: its meaning, etymology section (any mention of Byblos/Gebal/Egyptian origin, Beekes), and derived terms βιβλίον, βιβλία."
}
```


### [2026-09-06T15:29:56.884Z] TOOL RESULT

```
# Etymology of Biblio-

The prefix originates from Greek *biblion* meaning "paper, scroll" or "a book as a division of a larger work," which was originally a diminutive form of *byblos* (Egyptian papyrus).

## The Byblos Connection

The entry explains two competing theories about the relationship between the Greek word and the place name:

**Theory 1 (Greek from place):** The word may derive from "Byblos, the Phoenician port from which Egyptian papyrus was exported to Greece (modern Jebeil, in Lebanon)."

**Theory 2 (Place from Greek):** Alternatively, "the place name might be from the Greek word, which then would be probably of Egyptian origin."

This represents genuine etymological uncertainty—scholars cannot definitively determine whether the port city's name generated the Greek term for papyrus/books, or whether the reverse occurred. The lexicographer notes this ambiguity without favoring either explanation, acknowledging that the ultimate origin remains obscure.
```


### [2026-09-06T15:29:59.147Z] TOOL RESULT

```
# Ancient Greek Entry: βύβλος

**Meaning:**
The term refers to "(1) papyrus (both in reference to the plant and writings using the paper-like material derived from the plant) [and] (2) book."

**Etymology:**
According to the entry, the word is "traditionally derived from _Βύβλος_ (Búblos, 'Byblos (ancient city)')" from which it was imported. However, scholars propose an alternative: "the town was named after this word rather than the other way around...and that the word is of Pre-Greek origin." The reference cites "Beekes, Robert S. P. (2010)" in his *Etymological Dictionary of Greek*.

**Derived Terms:**
Two related words are listed:
- βύβλινος (bŭ́blĭnos)
- βυβλίον (bŭblĭ́on)
```


## [2026-09-06T15:30:04.773Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D8%A8%D9%84",
 "prompt": "Quote the Arabic entry جبل (jabal): etymology (Proto-Semitic reconstruction, cognates Hebrew גְּבוּל, Phoenician, Ugaritic, Aramaic), meaning, plural جبال. Also quote the Persian section if present."
}
```


## [2026-09-06T15:30:06.489Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Gibraltar",
 "prompt": "Quote the etymology of Gibraltar: Arabic جَبَل طَارِق (jabal ṭāriq), Tariq ibn Ziyad, date, and the phonetic development into Spanish/English."
}
```


### [2026-09-06T15:30:13.622Z] TOOL RESULT

```
# Etymology of Gibraltar

**Arabic Origin:**
The name derives from Arabic *جَبَل طَارِق* (jabal ṭāriq), meaning "Mount Tariq."

**Historical Figure:**
It was named after Tariq ibn Ziyad, who "led the Umayyad conquest of Hispania, starting in 711."

**Linguistic Development:**
The term passed through Spanish *Gibraltar* before entering English, replacing the earlier Latin designation *Mons Calpe* ("Mount Calpe") for the landmass and *Columnae Herculis* (the classical "Pillars of Hercules") for the strait.

**Pronunciation Evolution:**
The modern English pronunciation /dʒɪˈbɹɔːltə(ɹ)/ reflects the phonetic adaptation of the Arabic-Spanish form into English phonological patterns, with the initial Arabic *j* sound evolving into the English affricate sound.
```


### [2026-09-06T15:30:13.675Z] TOOL RESULT

```
# جبل (Jabal) - Dictionary Entry

## Arabic Etymology and Meaning

The word جبل (jabal) comes from the Semitic root ج ب ل (j b l). It shares cognates with **"Biblical Hebrew גְּבוּל (gəḇūl, 'border')"** and Ugaritic forms.

**Primary meaning:** "mountain" or "mountains, mountain range"

**Plural forms:** جِبَال (jibāl) or أَجْبَال (ʔajbāl)

The entry also documents a verb form jabala meaning to mold, form, shape, knead, or create, with the verbal noun جَبْل (jabl) representing creation, formation, and kneading.

## Persian Usage

In Persian, جبل (jabal) translates to **"mountain,"** though the synonymous کوه (kuh) is noted as more commonly used. The word was borrowed from Arabic into Persian and subsequently into other languages like Sindhi and Urdu, demonstrating its widespread linguistic influence across the Middle East and South Asia.
```


## [2026-09-06T15:30:18.501Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Byblos",
 "prompt": "Quote the etymology of Byblos: relation to Phoenician 𐤂𐤁𐤋 (Gebal), Hebrew גְּבַל, Akkadian Gubla, Greek Βύβλος, and any note on the connection with βύβλος 'papyrus'."
}
```


## [2026-09-06T15:30:19.645Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/biblia",
 "prompt": "Quote the Latin entry biblia: etymology (from Ancient Greek βιβλία, plural of βιβλίον), gender/declension (neuter plural reinterpreted as feminine singular), meaning, and descendants."
}
```


### [2026-09-06T15:30:23.858Z] TOOL RESULT

```
# Etymology of Byblos

According to the Wiktionary entry, Byblos traces back through multiple ancient languages. The English term was "Borrowed from Latin _Byblos_, from Ancient Greek _Βύβλος_ (Búblos), from Phoenician _𐤂𐤁𐤋_ (gbl /⁠Gebal⁠/)."

The page identifies it as a "Doublet of _Jubail_," reflecting the shared Phoenician origin. The Latin entry confirms the Greek borrowing, which itself came "from Phoenician _𐤂𐤁𐤋_ (gbl)."

The entry does not explicitly discuss connections to Hebrew גְּבַל (gval), Akkadian Gubla, or the Greek word for papyrus (βύβλος). However, the related term Jubail suggests these cognate relationships exist across Semitic languages sharing the same root.
```


### [2026-09-06T15:30:27.744Z] TOOL RESULT

```
# Latin Entry: *biblia*

**Etymology:**
From Ancient Greek *[βιβλία](/wiki/%CE%B2%CE%B9%CE%B2%CE%BB%CE%AF%CE%B1#Ancient_Greek "βιβλία")* (biblía), which is the plural of *[βιβλίον](/wiki/%CE%B2%CE%B9%CE%B2%CE%BB%CE%AF%CE%BF%CE%BD#Ancient_Greek "βιβλίον")* (biblíon, "book").

**Gender/Declension:**
The word appears in two forms in Latin:
1. **Ecclesiastical Latin**: A neuter plural noun in the second declension (genitive *bibliōrum*)
2. **Very Late Latin**: A feminine singular noun in the first declension (genitive *bibliae*)

This represents a reanalysis where the Greek neuter plural was reinterpreted as a feminine singular in later usage.

**Meaning:**
An alternative lowercase form of *Biblia*, meaning "the Bible."

**Descendants:**
The entry shows this Latin term influenced numerous Romance and other languages, including Spanish, Finnish, Hungarian, Esperanto, and Swahili, all of which adopted the word for "bible."
```


## [2026-09-06T15:30:35.037Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD1 bible ===\"; grep -n -i \"biblion\\|Bib'li-on\\|bib.li.a\" FSD_vol1.txt | head -6; echo \"=== WEB1 biblion ===\"; grep -n -i \"biblion\\|Gibraltar\" WEB_vol1.txt | head -6; echo \"=== PEI ===\"; grep -n -i \"byblos\\|biblion\" PEI.txt | head -6",
 "description": "Grep Funk&Wagnalls, Webster, Pei"
}
```


### [2026-09-06T15:30:35.120Z] TOOL RESULT

```
=== FSD1 bible ===
41268:Bulletin  U.  S.  Nat.  Mus.  No.  27,  E.  p.  292.  [gov.  ptg.  orr.  1884.] 6.  [b-]  Any'  important  book,  record,  or  history.  7f. [b-]  A   military  engine  for  throwing  stones.  [F.,  <   LL. biblia,  <   Gr.  biblia,  pi.  of  biblion,  dim.  of  biblos,  byblos, book,  papyrus.]  —   Adulterous  Bible,  same  as  Wicked Bible,  1   —   Altken  B.,  the  first  printed  in  English  In  Amer- ica by  Robert  Aitken  of  PMladelphia  in  1782.  Bamberg
41282:Mb'Ii-o-,  1   bib'h-o-;  2   blb'li-o-.  FYom  Gr.  biblion ,   book (see  Bible)  :   a   combining  form  signifying  of  or  per- taining to  books,  especially  the  Bible.—  blb"II-o-chre'sIs, n.  The  use  of  books.—  blbll-o-clasm,  n.  The  mutilation or  destroying  of  books,  or  (specifically)  of  the  Bible  —   blb'll- o-c!ast,  n.  One  who  mutilates  or  destroys  books.—  blb"ll- o-gen'e-sls,  n.  A   creation  of  books  or  literature.
41286:bib"JI-og'o-ny,  n.  The  production  of  books. bIb"II-og'ra-phcr> 11  bib’'h-og,ra-far;  2   bft/li-Sg'ra-fer, bib"ll-og'ra-fer8,  J   n.  X.  One  who  writes  about  or  is skilled  in  bibliography.  2t-  A   writer  or  copyist  of books;  a   Bcribe.  [   <   Gr.  bibliographos,  <   biblion  (see Bible)  -f*  grapho,  write.)  bib'li-o-graplij. blb'll-o-grapb'lc,  \   1   bib'U-o-graf'Vk;  2   blb'H-o-gr&f'ic, blb"II-o-*graf'ic8,  J   a.  Of  or  pertaining  to  bibliog- raphy. blb"II-o-graph'I-cai;.—  -Iy,  adv. blb"li-0g'ra-phlze,  1   bib’h-og'ro-fniz;  2   bib  "li-og'ra- flz,  t/.  [-phiz ed ;   -phiz  *ing.)  To  make  a   bibliog- raphy of.  {M.J
41321:[F.,  <   Gr.  biblion  (seo  Bible)  +   phllos.  loving.)  bib'-  bl-chro'ma-tlze, )   1   bai-kro'mo-taiz;  2   bl-cro'ma-tlz,  vl.
41328:Hawthokne BlUh'daleRomanct  ch.  17.  p.  174.  |o.  a   co.  1874.)  bf-t  lr'clold,  1   boi-sOr'kleid;  2   bl-cIr'clBid,  n.  An  cpioy- )   <   Xi.  bibhopoln,  <   Gr.  bibhopbles,  <   biblion,  book,  +   cloid.  f   <   bi-  circle  +   -oid.) pOleb,  sell.)  -   blb"ll-0-pol'lc,  a.  Pertaining  to  or  char-  bl-clr'cu-Iar,  a.  1.  Formed  by  or  related  to  two  circles, acteristic  of  booksellers;  dealing  in  books.  bIb"II-o-  2.  Math.  Relating  to  those  curves  of  the  fourth  degree
41346:[L.,  <   Gr.  bibliotheke,  <   biblion  (see  Bible)  -f-  theke, case,  <   tlthSmi,  place.)  bIb"II-o-the'ket.—  blb"J!-o- the'cal  (xiu),  a   —   b!b"H-o-the-ca'ri-an.  I.  a.  Per- taining to  a   library  or  a   librarian.  II.  n.  A   librarian.— bIb"II-oth'e-ca-ry.  I.  a.  Blbllothecarian.  II.  n.  J.  A librarian.  2t.  A   library,  blb^ll-otli'c-carf. blb"ll-o-thet'lc,  \   bib*U-o-fhet'ik;  2   blb*lI-o-th6t'lc,  a.  Per- taining to  the  arrangement  of  books  on  the  shelves  of  a
=== WEB1 biblion ===
12883:At-lan’tis, n. [L.; Gr.] a legendary island or continent supposed to have existed in the Atlantic west of Gibraltar and to have been sunk by an earthquake.
15875:Barbary ape; a tailless ape, easily trained, found in northern Africa and on the Rock of Gibraltar.
19072:Ing ealize m Gr. biblion, a book.] a combin- pitgeitle €aning: (a) book, of books; (b) of cially aR m, 7. a type of microfilm used espe- bi libraries otographing rare or fragile books
19085:books. bib-li-oph/i-list, n. a bibliophile. bib/li-o-ph6/bi-a, n. (biblio-, and Gr. phobia, fear.] a dread of or distaste for books. bib/li-6-pole, n. same as bibliopolist. bib"li-o-pol/ic, bib-li-op’ō-lär, a. pertaining to bookselling. 5 bib-li-op/6-lism, n. the business of buying and selling books. i sag bib-li-op’6-list, n. [L. bibliopola, Gr. biblio- poles: biblion, a book, and polein, to sell.] a ookseller, especially one who deals in rare or curious books. E ae 5 bib-li-op:6-lis’tic, a. relating to bibliopolism. bib-li-op’6-ly, n. bookselling. ae pib/li-o-taph, bib-li-ot’a-phist, n. [biblio-, and Gr. taphos, from taphein, to bury.] one who stows away or hides books. bib/li-d-thec, n. one who has charge of a col- lection of books; a librarian; also, a library. bibli-d-thé’ca, n. [L. bibliotheca; Gr. biblio- thēkē, a library, bookcase; biblion, a book, and théké, from tithenai, to place.)
81739:b’fish, n. a male salmon. [Brit. Dial.] ift, v.t.: gifted, pl - giftin # L to 5 ib/ing-ly, adv. in a gibing manner; scornfully : £ confer Lea ERE Scot.) a (see ee eel etc.) and -le, freq. suffix.] to also spelled jibingly. j i 2. to endow with a gift or with any power eet ty oS series of uncontrollable, rapid, ib’let, a, made of giblets; as, a giblet pie. or faculty. Wl Nae sounds, suggestive of foolish- pib/let, n. [ME. gibelet; OFr. gibelet, stew made gift/ed, a. endowed with a natural ability or DaS HELV OUSHESS: etc.; to titter, of fowls.] aptitude; talented. gig/gle, n. a kind of laugh, with rapid, high- 1. an internal edible part of a fowl, such as ___ Some divinely gifted man. — Tennyson. pitched sounds, suggestive of foolishness, the heart, liver, or gizzard, which has been re- gift’ed-ness, 7. the state of being gifted CES Sec to ‘moved before cooking, and is often served gift rope, [probably altered from guess rope.) in gig’glēr, n. one who giggles or titters. separately in a sauce or pie: chiefly used in seamen’s language, a rope attached to a boat gig’gly, a. given to giggling. Hi mara id Mende (Dist) gi towing it. [Obs.] ( D gig’got, n. a gigot. [Obs.] fe .} odds and ends. jal. (’-wrap, v.l. to wrap (a gift) attractively, gi Net, gig’l a wo ‘ ee A Gi-bral/ tir, n. rock candy: called also Gibraltar With decorative wrapping, ribbon, etc. ae ERMC a, ae pees on rock, in allusion to the Rock of Gibraltar, a gig, n. a dart or harpoon; a fishgig. 5i/95-10,, Fr eE Seas sg ; fort belonging to Great Britain at the en- ig, v.i. to fish with a gig or fishgig. Big SEA Mia rom, gigólette, -a prostitui T, of the Mediterranean. gig, v.t. to spear (a fish) with a gig. fain geek ee oes io gin, chee SoG Fi i i fi i . [ME. gig vhirligi inni . . : “1egecd, 1 art, agh, Ieg, _ pastel, ees gil of the 1890's as &' B eens whirligig, spinning top; from giguer, to dance, jig, from gigue, a fiddle] p y na Gibson, P 2 N. 1. a man who is paid to be a danci ġib’stàff, n. [OFr. gibbe, a sort of arm.] a staff 1, a light, two-wheeled, open carriage ner or escort for ome o be a Ce to gauge water or to push a boat. drawn by one horse., 2. a man supported by a prostitute a e en Er alier thenameof -py 3 Jong. light ship's boat with oars and gigrót, n [Fr., irom OFr. gi f f mutt “the 19th-c. inventor.] an opera hat; a collaps- sail, usually reserved for the commanding “dim fot oiie a fiddle] el, lee ae
=== PEI ===
```


## [2026-09-06T15:30:43.952Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntargets={'FSD_vol1.txt':[41268],'WEB_vol1.txt':[19072],'PHN.txt':[5302],'RCH.txt':[29618,14423],'LKT.txt':[1570],'MON_part1.txt':[47153],'NAT_2005.txt':[795],'SKT.txt':[1752],'BQT_v2_pages.txt':[7809,12352]}\nfor f,ts in targets.items():\n    leaf=0\n    for i,l in enumerate(open(f,encoding='utf-8',errors='replace'),1):\n        leaf+=l.count('\\f')\n        if i in ts: print(f,i,'leaf',leaf)\nEOF",
 "description": "Compute leaf numbers for all hits"
}
```


### [2026-09-06T15:30:46.667Z] TOOL RESULT

```
FSD_vol1.txt 41268 leaf 320
WEB_vol1.txt 19072 leaf 202
PHN.txt 5302 leaf 211
RCH.txt 14423 leaf 320
RCH.txt 29618 leaf 588
LKT.txt 1570 leaf 77
MON_part1.txt 47153 leaf 0
NAT_2005.txt 795 leaf 127
SKT.txt 1752 leaf 58
BQT_v2_pages.txt 7809 leaf 133
BQT_v2_pages.txt 12352 leaf 210
```


## [2026-09-06T15:30:52.682Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 7809 12352; do echo \"--- line $L ---\"; awk -v L=$L 'NR<=L && /\\[pdf page/ {p=$0} NR==L{print \"tag:\",p; print \"txt:\",$0}' BQT_v2_pages.txt; done",
 "description": "Find BQT page tags"
}
```


### [2026-09-06T15:30:54.577Z] TOOL RESULT

```
--- line 7809 ---
tag: 
txt:          ‫‏(‪ )٤‬کوه کروابند وبعربی جبل خوانند ‪.‬‬
--- line 12352 ---
tag: 
txt:  ‫وهی است وبعریی جبل خوانند ‪ -‬وبضم اول‬
```


## [2026-09-06T15:30:57.677Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" BQT_v2_pages.txt | head -3; echo ...; awk 'NR<=7809 && /pdf page/{p=$0; n=NR} END{}' BQT_v2_pages.txt; grep -n \"pdf page\" BQT_v2_pages.txt | awk -F: '$1<7809' | tail -2",
 "description": "Locate pdf page tag before line 7809"
}
```


### [2026-09-06T15:30:59.823Z] TOOL RESULT

```
...
```


## [2026-09-06T15:31:08.884Z] TOOL CALL #42: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/Bible\" \"https://www.etymonline.com/word/biblio-\" \"https://en.wiktionary.org/wiki/%CE%B2%CF%8D%CE%B2%CE%BB%CE%BF%CF%82\" \"https://en.wiktionary.org/wiki/%D8%AC%D8%A8%D9%84\" \"https://en.wiktionary.org/wiki/Gibraltar\" \"https://en.wiktionary.org/wiki/Byblos\" \"https://en.wiktionary.org/wiki/biblia\"; do python3 tools/fetch_source.py \"$u\" --note \"page 229, root J.b.l (jabal/Gibraltar/Bible), verifying Semitic root, Arabic jabal, Greek byblos/biblia chain\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-06T15:31:13.909Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/001da4205f642d09.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/65998926d95afe09.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3c3611110df00bd8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1219b3e2b2db3672.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cccf4c9fece25584.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/884f0b921702870c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/010b543eeadbec46.txt
```


## [2026-09-06T15:31:19.533Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%92%D7%91%D7%95%D7%9C",
 "prompt": "Quote the Hebrew entry גבול (gəvul): meaning 'border, boundary', etymology, root ג־ב־ל, and any cognates with Arabic جبل or Phoenician."
}
```


### [2026-09-06T15:31:25.755Z] TOOL RESULT

```
# גבול (gəvul) - Hebrew Entry

**Primary Meaning:**
According to Wiktionary, גבול signifies "a border, a boundary, a limit, a line" dividing territories or regions.

**Etymology & Root:**
The entry documents the Semitic root **ג־ב־ל** (g-b-l), from which this term derives. The word follows the Hebrew pattern קְטוּל.

**Grammatical Details:**
The noun is masculine, with the form גְּבוּל. Its plural is גְּבוּלוֹת (g'vulót).

**Extended Senses:**
Beyond geographical boundaries, גבול encompasses "the area within a set of borders" and figuratively denotes "an edge, an end, a limit"—exemplified in the phrase *gvúl khayáv* (end of his life).

**Note on Cognates:**
The provided Wiktionary content does not mention Arabic جبل or Phoenician cognates, so I cannot address those linguistic connections based on this source material.
```


## [2026-09-06T15:31:29.141Z] TOOL CALL #44: Bash

```json
{
 "command": "python3 /home/sfmqrb/git/rishe/tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D7%92%D7%91%D7%95%D7%9C\" --note \"page 229, root J.b.l: Hebrew gəvul 'border' root g-b-l\" 2>&1 | tail -1; echo ---; sed -n '1,60p' /home/sfmqrb/git/rishe/data/verification/page-205.json 2>/dev/null | head -30",
 "description": "Archive Hebrew source; peek at a prior page file format"
}
```


### [2026-09-06T15:31:31.513Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/39e6c0398f12e5d2.txt
---
{
  "pdf_page": 205,
  "book_page": 175,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Gwei",
      "verdict": "confirmed",
      "modern_form": "PIE *gʷeyh₃- (Pokorny 'gʷei-3, gʷeiə-, gʷii̯ē-, gʷi̯ō-, gʷī-, frequent, often with -u̯- extended') 'to live'",
      "note": "The root box is right on all three counts. Pokorny's lemma reads 'Root/lemma: gʷei-3 and gʷeiə-: gʷii̯ē-: gʷi̯ō-: gʷī-, frequent, often with -u̯- extended. Meaning: to live', with 'Page(s): 467-469', so Nourai's 'Gwei : to live' with POK:467 reproduces Pokorny's own heading and page; Watkins in the AHD appendix has 'gʷei-. Also gʷeiə-. To live ... [Pok. 3. gʷei- 467]'; Wiktionary reconstructs *gʷeyh₃- 'to live' (alternative *gʷyeh₃-); Cheung, for the Iranian verb, writes '*jaiH2 ... «PIE *gʷeiH₃-, *gʷieH₃-/*gʷih₃- \"to live\" © LIV: 215 f. | Pok.: 467 f.'. What is striking about this chart is how much of it is simply Pokorny's own article rearranged: pages 467-469 contain, in order, Avestan gaya- and gaēθā-/Old Persian gaiθā, Avestan jīti- and jīra-, Old Persian jīva-/Avestan jva-, Greek bios, zōḗ, zōion and hygiḗs, Latin vīvus/vīvō/vīta, and Old English cwicu / OHG queh — that is, every branch of the page except the modern coinages. Klein's article 'quick' (p.1288, Nourai's own citation on node 1) carries the same set in one paragraph. Three things need qualifying rather than correcting: the Avestan citation forms in node 1 ('jîta', 'merezu-jîta' for jīti-, mərəzu-jīti-/-jva-); the gloss 'to exist' given to the noun gaēθā- in node 8; and the presence of two 19th/20th-century neologisms ('mikro-bios' in the Greek box, 'vitamine' in the French box) among inherited words. Everything on the Iranian side — zīwistan/zīwandag → زیستن/زنده/ژیوه, the Arabic round trip زیبق, gayō.marətan- → کیومرث, gaēθanąm → gēhān → گیتی/کیهان/جهان, jīra- → زیرک/آژیر — checks out against Horn, Hübschmann, MacKenzie, Nyberg, Bartholomae, Asbaghi and Moʿin's footnotes on the very Borhān pages Nourai cites.",
      "note_fa": "جعبهٔ ریشه از هر سه جهت درست است: پوکورنی مادّهٔ «gʷei-3 و gʷeiə-…» را با معنای «زیستن» در صفحات ۴۶۷–۴۶۹ آورده، پس هم صورت و هم برچسبِ زبان و هم معنا و هم شمارهٔ صفحه‌ای که نورایی داده دقیق است؛ واتکینز نیز همین را می‌گوید و ویکی‌واژه آن را *gʷeyh₃- بازسازی می‌کند و چونگ در فرهنگِ فعلِ ایرانی ذیل *jaiH₂ همین ریشه را می‌آورد. نکتهٔ چشمگیر این است که بیشترِ نمودار در واقع بازچینشِ همان مقالهٔ پوکورنی است: اوستایی gaya- و gaēθā-، پارسی باستان gaiθā، jīti- و jīra-، jīva-/jva-، یونانی bios و zōḗ و hygiḗs، لاتین vīvus و vīta، و انگلیسی کهن cwicu همه در همان سه صفحه‌اند. سه نکته باید روشن شود، نه اصلاح: صورت‌های اوستاییِ گرهٔ ۱ («jîta» به‌جای jīti-)، معنای نادرستِ «to exist» برای اسمِ gaēθā- در گرهٔ ۸، و حضورِ دو نوواژهٔ سدهٔ نوزدهم و بیستم (mikro-bios و vitamine) در کنارِ واژه‌های موروثی. تمامِ بخشِ ایرانیِ نمودار — از zīwistan تا «زیستن» و «زنده» و «ژیوه»، چرخهٔ «زیبق»، gayō.marətan- تا «کیومرث»، gaēθanąm تا «گیهان/گیتی/کیهان/جهان»، و jīra- تا «زیرک/آژیر» — با هرن، هوبشمان، مکنزی، نیبرگ، بارتولمه، اصباغی و حواشیِ معین بر همان صفحاتِ برهانِ قاطع که نورایی ارجاع داده می‌خواند.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7eyh%E2%82%83-"
      ],
      "ref_check": [
        {
          "ref": "POK:467",
          "status": "supports",
          "note": "POK_full.txt lines 38677-38790: 'Root / lemma: gʷei-3 and gʷeiə-: gʷii̯ē-: gʷi̯ō-: gʷī-, frequent, often with -u̯- extended || Meaning: to live || Material: A. from *gʷei-: Old Indic jīvatu-ḥ \"life\", gaya-ḥ \"house, courtyard\" ... Avestan gaēθā, Old pers. gaiθā \"entity, house and courtyard\" ... References: WP. I 668 ff. ... Page(s): 467-469.' Exactly the root box as drawn."
        }
      ],
      "consulted": [
        {
          "src": "AHD",
          "where": "Watkins 1985, IE roots appendix s.v. gʷei- (AHD_watkins1985.txt line 540)",
          "stance": "supports",
          "note": "'gʷei-. Also gʷeiə-. To live. I. Suffixed zero-grade form *gʷi-wo-, *gʷī-wo- ... [Pok. 3. gʷei- 467.]' — the same root, gloss and Pokorny page."
        },
```


## [2026-09-06T15:31:34.741Z] TOOL CALL #45: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T15:31:34.783Z] TOOL RESULT

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


## [2026-09-06T15:31:59.154Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFA gabal/gbl ===\"; grep -n -i \"gabal\\|ǧabal\\|Gebal\\|Byblos\" AFA.txt | head -5; echo \"=== AKD ===\"; grep -n -i \"gabal\\|Gubla\\|Byblos\" AKD.txt | head -5; echo \"=== FVQ Byblos ===\"; grep -n -i \"byblos\\|gebal\" FVQ.txt | head -5; echo \"=== LKT bibel ===\"; grep -n -i \"bibel\\|byblos\" LKT.txt | head -5; echo \"=== DEV gibraltar ===\"; grep -n -i \"gibraltar\" DEV.txt LAM.txt DOZ.txt | head -5",
 "description": "Grep Fraenkel, Zimmern, Jeffery, Lokotsch, Devic"
}
```


### [2026-09-06T15:31:59.271Z] TOOL RESULT

```
=== AFA gabal/gbl ===
=== AKD ===
=== FVQ Byblos ===
=== LKT bibel ===
=== DEV gibraltar ===
```


## [2026-09-06T15:32:02.900Z] TOOL CALL #47: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg229.png data/verification/sources/refs/ocr/BOOK/229.png && ls -la data/verification/sources/refs/ocr/BOOK/ | tail -5",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-06T15:32:02.991Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T15:32:04.449Z] AGENT

Now I'll write the verification file.


## [2026-09-06T15:37:15.608Z] TOOL CALL #48: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk229.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 229,\n \"book_page\": 199,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"J.b.l\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Proto-Semitic / Central Semitic √g-b-l (Arabic ج ب ل) 'mountain; boundary, border'\",\n   \"note\": \"The root box is right. A Semitic triliteral g-b-l is genuinely reconstructed with the meaning 'mountain / boundary' (the two senses are one: a mountain ridge as a natural frontier). Arabic realises the initial *g as jīm (ج), hence j-b-l, jabal 'mountain'; Hebrew has gəḇūl 'border, boundary' and the place name Gəḇal (Byblos); Ugaritic and Phoenician have gbl. Nourai's label 'Semitic' and gloss 'mountain' follow Klein, who at p.169 (s.v. Bible) and p.826 (s.v. javali) writes that Arabic jabal 'mountain' 'is rel. to Heb. gḗbhul, \\\"frontier, boundary\\\", orig. \\\"earth wall or mountain serving as boundary\\\"'. Two nuances the chart hides: (a) the sense 'mountain' is specifically Arabic — in Hebrew/Phoenician the root means 'border' and the city name; (b) the Greek-Latin-English branch of this chart hangs on the traditional (Klein's) derivation of Gk. búblos from the port name, which Beekes 2010 now questions (see node #5).\",\n   \"note_fa\": \"جعبهٔ ریشه درست است. ریشهٔ سه‌حرفیٔ سامی ‏g-b-l‏ به معنای «کوه؛ مرز و حد» بازسازی می‌شود و این دو معنا یکی است، زیرا رشته‌کوه مرز طبیعی است. در عربی ‏*g‏ آغازین به جیم بدل شده و جَبَل «کوه» داده، در عبری گَبُول «مرز» و نام‌جای گَبَل (بیبلوس)، و در اوگاریتی و فنیقی gbl. کلاین (ص ۱۶۹ و ۸۲۶) همین پیوند را می‌آورد و ادعای نورایی درست است؛ فقط باید دانست که معنای «کوه» ویژهٔ عربی است و در عبری و فنیقی این ریشه معنای «مرز» دارد.\",\n   \"sources\": [\n    W + \"%D8%AC%D8%A8%D9%84\",\n    W + \"%D7%92%D7%91%D7%95%D7%9C\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"KLN:169\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 101 (printed pp.168/169), s.v. Bible: 'Gk. Bυβλος has been assimilated fr. Gebhḁl, the Heb.-Phoen. name of the city (lit. “frontier town”; cp. Heb. gḗbhul, “frontier, boundary”, Arab. jabal, “mountain”, and see javali).' Klein does put Arabic jabal and Hebrew gḗbhul under one Semitic root, exactly as the root box claims.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 20193, leaf 447 = printed p.826, s.v. javali\", \"stance\": \"supports\",\n     \"note\": \"'fr. Arab. jabali, “pertaining to the mountains” ... formed fr. jabal, “mountain”, which is rel. to Heb. g(bhul, “frontier, boundary”, orig. “earth wall or mountain serving as boundary”.' — the fullest statement of Nourai's root.\"},\n    {\"src\": \"AFA\", \"where\": \"AFA.txt, grep -i 'gabal|Gebal|Byblos'\", \"stance\": \"silent\",\n     \"note\": \"Fraenkel's Aramaic loanwords in Arabic has no entry for jabal — unsurprising, since jabal is inherited Semitic, not an Aramaic loan; the silence is itself mild support for treating it as native.\"},\n    {\"src\": \"AKD\", \"where\": \"AKD.txt, grep -i 'gabal|Gubla|Byblos'\", \"stance\": \"silent\",\n     \"note\": \"Zimmern's Akkadian loanwords lists nothing under this root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Arabic\",\n     \"words\": \"j.b.l, jabal; jabal-al-târiq\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic جَبَل jabal 'mountain', pl. جِبَال jibāl / أَجْبَال ajbāl, is the regular Arabic reflex of the Central Semitic root g-b-l (Proto-Semitic *g > Arabic jīm ج). The compound جَبَل طَارِق jabal Ṭāriq 'the mountain of Ṭāriq' is a genuine 8th-c. toponym: Ṭāriq ibn Ziyād, the Berber freedman of Mūsā ibn Nuṣayr, landed on the rock in 711 and it took his name; Nourai's chart note 'Tariq invaded Spain in 711' is correct (Pihan and Richardson give 710 for the landing, 711 for the campaign proper). Klein separately notes that the town beside the rock has the vulgar pronunciation jebel al-Ṭāriq, which is the form the Romance languages heard.\",\n     \"derivation_fa\": \"جَبَل در عربی بازماندهٔ منظم ریشهٔ سامی ‏g-b-l‏ است (‏*g‏ سامی در عربی به جیم بدل می‌شود)، جمع مکسر آن جِبال و أجبال است. ترکیب «جبل طارق» نام‌جایی است از سدهٔ دوم هجری: طارق بن زیاد، سردار بربر؛ آزادکردهٔ موسی بن نصیر، در سال ۷۱۱ میلادی در آن صخره پیاده شد و نام او بر کوه ماند. یادداشت نورایی (۷۱۱) درست است؛ پیان و ریچاردسون سال پیاده‌شدن را ۷۱۰ می‌دهند.\",\n     \"sources\": [W + \"%D8%AC%D8%A8%D9%84\", W + \"Gibraltar\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:170\", \"status\": \"not_found\",\n       \"note\": \"KLN_1966.txt leaf 102 = printed pp.170/171 carries only the biblio- compounds (bibliolatry, bibliomancy, bibliophil, bibliopole, bibliotheca ... bibulous); there is nothing about Arabic jabal on p.170. The claim Nourai attaches here is actually on p.169 (s.v. Bible), p.655 (s.v. Gibraltar) and p.826 (s.v. javali). Page slip, not a substantive error.\"},\n      {\"ref\": \"FVA:68\", \"status\": \"not_checked\",\n       \"note\": \"Nahvi, Farhang-e Vāzhehā-ye ʿArabi dar Fārsi — refs_online.json records no digital copy on any permitted platform (re-searched 2026-09).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"leaf 355 = printed p.655, s.v. Gibraltar\", \"stance\": \"supports\",\n       \"note\": \"'Fr. Arab. jabal (in vulgar pronunciation jebel) al Tḁriq, “mount of Tariq”, named after Tariq, the Moslem invader of Spain who landed there in 711.'\"},\n      {\"src\": \"PHN\", \"where\": \"PHN.txt leaf 211 = printed pp.180-181, s.v. GIBRALTAR\", \"stance\": \"supports\",\n       \"note\": \"'جبل طارق [djébel (ou gibel) ṭâriq] ... montagne de Tarik ... On prétend que Gibraltar doit son nom au général sarrasin Tarik ben Ziad, qui prit possession de cette montagne, l'an 710 de notre ère'; and p.180 'Or gibel (et mieux djebel) veut dire tout simplement montagne'.\"},\n      {\"src\": \"LKT\", \"where\": \"LKT.txt line 1570, leaf 77 = printed p.51, entry no. 627 'Ar. gabali'\", \"stance\": \"supports\",\n       \"note\": \"'Adj. zu ar. gabal ‚Berg‘, vollständig hinzir gabali ‚Berg-, Wildschwein‘; hieraus sp. jabali ‚Eber‘' — Lokotsch's transcription gabal (not jabal) for the same Arabic word, glossed 'Berg'.\"},\n      {\"src\": \"RCH\", \"where\": \"RCH.txt line 29618, leaf 588\", \"stance\": \"supports\",\n       \"note\": \"Richardson's Persian-Arabic-English dictionary: 'A جبل jabl (from ...), Creating, forming. Jabal, A moun[tain]' — both Arabic homographs, jabl 'to mould/create' and jabal 'mountain', are listed under جبل.\"},\n      {\"src\": \"AFM\", \"where\": \"AFM_pages.txt, grep 'جبل'\", \"stance\": \"silent\",\n       \"note\": \"Addi Shir lists only adjectival jabalī in plant names (e.g. 'عشب الجبل'); he has no entry for jabal itself, which is correct — his book covers Persian words Arabised, and jabal is native Arabic.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"jabal «جَبَل»; jabal-ottâreq «جبل الطارق»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"جَبَل jabal is a straightforward Arabic loanword in New Persian, taken over after the Islamic conquest with its Arabic broken plural جِبال jibāl (the form the chart shows in parentheses); Moʿin marks it '[ع.]' (Arabic) and glosses it simply کوه. It is a bookish word: Persian's own کوه kūh (< MP kŏf, OIr. *kaufa-) remains the ordinary term, and jabal survives mainly in compounds, geographical names and Arabic-style plurals (جبال ، سلسله‌جبال). جبل الطارق is the same Arabic phrase read with the Persian pronunciation of the Arabic article assimilated to the sun-letter ط: al-Ṭāriq > aṭ-Ṭāreq, hence Nourai's 'jabal-ottâreq' — the normal Persian name of Gibraltar to this day, not a borrowing back from European Gibraltar.\",\n     \"derivation_fa\": \"«جَبَل» وام‌واژه‌ای عربی است که پس از اسلام به فارسی دری راه یافته، همراه با جمع مکسر عربی‌اش «جِبال» که در داخل پرانتز نمودار آمده است. معین در فرهنگ فارسی می‌نویسد: «جبل (ع.) (ا.) کوه؛ ج. جبال، اجبال». این واژه در فارسی کتابی است و واژهٔ بومی «کوه» (از فارسی میانهٔ kōf، ایرانی باستان ‏*kaufa-‏) همچنان رایج مانده است. «جبل‌الطارق» همان ترکیب عربی است با ادغام لام تعریف در حرف شمسی ط (‏al-Ṭāriq > aṭ-Ṭāreq‏) و نام رایج فارسی جبل‌الطارق است، نه وام‌گیری از Gibraltar اروپایی. ادعای نورایی درست است.\",\n     \"sources\": [W + \"%D8%AC%D8%A8%D9%84\"],\n     \"ref_check\": [\n      {\"ref\": \"FVA:68\", \"status\": \"not_checked\",\n       \"note\": \"Same as node #1: Nahvi's dictionary of Arabic words in Persian has no digital copy (refs_online.json, re-searched 2026-09). The claim it is asked to support — that Persian jabal is the Arabic word — is independently confirmed by Moʿin (see consulted).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"MON_part1.txt line 47153\", \"stance\": \"supports\",\n       \"note\": \"'جبل: [ع.] (ا.) کوه؛ ج. جبال، اجبال.' — Moʿin tags the word Arabic, glosses it کوه, and gives exactly the plural جبال that the chart prints in parentheses. (He separately lists جبل/جبلت 'طبیعت، سرشت' from the other Arabic root j-b-l 'to mould'.)\"},\n      {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt lines 7809 and 12352 (leaves 133 and 210)\", \"stance\": \"partial\",\n       \"note\": \"Borhān-e Qāṭeʿ has no headword جبل (it is a dictionary of Persian, and excludes plain Arabic), but glosses Persian entries with it: 'کوه ... و بعربی جبل خوانند' ('a mountain ... in Arabic they call it jabal'), which confirms the word's status in Persian as the Arabic equivalent of کوه.\"},\n      {\"src\": \"RCH\", \"where\": \"RCH.txt line 29618, leaf 588\", \"stance\": \"supports\",\n       \"note\": \"Richardson marks the entry 'A' (Arabic) within a Persian-Arabic dictionary: 'A جبل ... Jabal, A moun[tain]', i.e. current in Persian usage as an Arabic word.\"},\n      {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"Aryanpur's dictionary covers only the Indo-European stratum of Persian, so an Arabic loan such as جبل is by design absent.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"English\",\n     \"words\": \"Gibraltar\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English Gibraltar comes from Spanish Gibraltar, itself from Arabic جَبَل طَارِق jabal Ṭāriq (vulgar jebel Ṭāriq) 'mount of Ṭāriq', with the whole phrase univerbated and the Arabic definite article of jabal al-Ṭāriq lost: jabal-ṭāriq > Sp. Gibraltar, Arabic jīm rendered by Old Spanish /ʒ/ (later /x/, English /dʒ/), the unstressed medial vowel syncopated (-bal ṭa- > -bral- by metathesis of the liquid), and the Arabic emphatic ṭ de-emphasised to /t/. The rock replaced Roman Mons Calpe as the name of the promontory, and by extension named the strait. Nourai draws the arrow straight from Arabic to English; the Spanish intermediary is omitted but is not in doubt.\",\n     \"derivation_fa\": \"انگلیسی Gibraltar از راه اسپانیایی Gibraltar به عربی «جبل طارق» می‌رسد. در این راه جیم عربی در اسپانیایی کهن به ‏/ʒ/‏ بدل شده، لام تعریف افتاده، واکهٔ میانی ساکت شده و با قلب (metathesis) ‏-balṭa-‏ به ‏-bralta-‏ دگرگون شده، و طای مطبق عربی به ‏/t/‏ ساده بدل شده است. نورایی حلقهٔ اسپانیایی را نیاورده، ولی اصل ادعا درست است.\",\n     \"sources\": [W + \"Gibraltar\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:655\", \"status\": \"supports\",\n       \"note\": \"Verified by page marker: KLN_1966.txt leaf 355 sits between the leaves carrying printed 658 (leaf 356) and 659/660 (leaf 357), i.e. printed pp. 654/655, and it contains 'Gibraltar, n., name of the Rock at the western entrance to the Mediterranean. — Fr. Arab. jabal (in vulgar pronunciation jebel) al Tḁriq, “mount of Tariq” ... who landed there in 711. See javali and cp. Bible.' Nourai's page is exact and Klein even cross-links the two branches of this chart.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHN\", \"where\": \"PHN.txt leaf 211 = printed pp.180-181, s.v. GIBRALTAR\", \"stance\": \"supports\",\n       \"note\": \"Pihan gives the Arabic جبل طارق for the French/European name and the history of Tarik ben Ziad; he also warns against 'le mont Gibel', a pleonasm, because gibel/djebel already means 'montagne'.\"},\n      {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 81739, leaf 202+ (G section)\", \"stance\": \"partial\",\n       \"note\": \"Webster's 2nd ed. has 'Gi-bral/tar, n. rock candy: called also Gibraltar rock, in allusion to the Rock of Gibraltar, a fort belonging to Great Britain at the en[trance] of the Mediterranean' — the derived sense only; the proper name is in the gazetteer, not the word list.\"},\n      {\"src\": \"RCH\", \"where\": \"RCH.txt line 14423, leaf 320\", \"stance\": \"supports\",\n       \"note\": \"'the Straits of Gibraltar; which last name is a corruption of Jabalu’t Tarak, The mountain of Tarak; that being the spot where this Arabian general first landed, in his descent upon Spain from the African shore, in the year 710.'\"},\n      {\"src\": \"LKT\", \"where\": \"LKT.txt, grep -i 'gibraltar'\", \"stance\": \"silent\",\n       \"note\": \"Lokotsch's dictionary of European words of oriental origin has no Gibraltar entry (he excludes proper names); his no. 627 covers only Arabic gabal via Spanish jabali.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Hebrew\",\n     \"words\": \"gebhal\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Nourai's node reproduces Klein p.169 word for word, and Klein is a reliable Semitist here: Gəḇal (گَّبَל — Heb. גְּבַל, Ezekiel 27:9 'the elders of Gebal'; Phoenician 𐤂𐤁𐤋 gbl; Amarna Akkadian Gubla) is the Canaanite name of the port later called Byblos and today Jubayl (جُبَیل, an Arabic diminutive of the same name), and it is literally 'frontier town', from the root g-b-l seen in Hebrew גְּבוּל gəḇūl 'border, boundary, limit'. Two corrections to the box: (a) the gloss 'mountain' is not a Hebrew meaning — in Hebrew the root yields only 'border/boundary' and the place name, and 'mountain' is the Arabic development; (b) papyrus was not grown at Gebal but imported from Egypt and re-exported through it to the Aegean, which is why the Greeks associated the port with the writing material. Hence plausible rather than confirmed.\",\n     \"derivation_fa\": \"این گره عیناً نقل کلاین (ص ۱۶۹) است: گَبَل (عبری גְּבַל، در حزقیال ۲۷:۹؛ فنیقی gbl؛ در الواح عمارنه Gubla) نام کنعانی بندری است که یونانیان بیبلوس خواندند و امروز جُبَیل (مصغّر عربی همان نام) نام دارد، و معنای تحت‌اللفظی‌اش «شهر مرزی» است، از همان ریشهٔ ‏g-b-l‏ که در گَبُول «حد، مرز» دیده می‌شود. دو اصلاح لازم است: نخست آنکه معنای «کوه» معنای عبری این واژه نیست و تنها در عربی پدید آمده؛ دوم آنکه پاپیروس در گبل نمی‌رویید بلکه از مصر می‌آمد و از آن بندر به یونان صادر می‌شد. پس ادعا «با احتیاط پذیرفتنی» است.\",\n     \"sources\": [W + \"Byblos\", W + \"%D7%92%D7%91%D7%95%D7%9C\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:169\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt line 4911 (leaf 101 = printed p.169): 'fr. Gebhḁl, the Heb.-Phoen. name of the city (lit. “frontier town”; cp. Heb. gḗbhul, “frontier, boundary”, Arab. jabal, “mountain”, and see javali). Cp. Jubayl, the actual Arabic name of ancient Gebhal.' Klein's spelling 'Gebhḁl' is exactly the chart's 'gebhal'; note that Klein glosses it 'frontier town', never 'mountain'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"leaf 447 = printed p.826, s.v. javali\", \"stance\": \"partial\",\n       \"note\": \"Klein's fuller statement 'Heb. g(bhul, “frontier, boundary”, orig. “earth wall or mountain serving as boundary”' shows the 'mountain' sense as the etymological background of the root, not as a Hebrew meaning — supporting the correction made above.\"},\n      {\"src\": \"AFA\", \"where\": \"AFA.txt, grep -i 'Gebal|Byblos'\", \"stance\": \"silent\",\n       \"note\": \"Fraenkel has no entry for the toponym.\"},\n      {\"src\": \"NAT\", \"where\": \"NAT_2005.txt leaf 127 (2005 reprint p.112; Nourai's NAT:110 is the 1982 pagination)\", \"stance\": \"supports\",\n       \"note\": \"Berlitz: 'Byblos was a port from which papyrus, for use in writing, was exported to Egypt' — he has the trade direction backwards (papyrus came FROM Egypt), but he confirms the port-and-papyrus link that this node rests on.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Greek\",\n     \"words\": \"bublos; bibua\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"bibua\",\n     \"correct_form\": \"biblia\",\n     \"derivation\": \"The second word in this box is printed 'bibua' in the book (page 199, PNG copied to data/verification/sources/refs/ocr/BOOK/229.png); there is no Greek word bibua. It is Nourai's misprint — or rather a dropped 'l' — for βιβλία biblia 'collection of writings', the plural of βιβλίον biblion; the gloss he prints, 'collection of writings, book', is verbatim Klein's gloss for βιβλία on p.169, which proves the intended form. The extraction is faithful to the page, so the fault is in the printed book. The first word is right: βύβλος búblos 'Egyptian papyrus; the inner bark of papyrus; book', with the by-form βίβλος bíblos (u > i by assimilation to the following iota), diminutive βυβλίον/βιβλίον. On the derivation itself the chart follows the traditional view (Klein, Skeat, Berlitz): Βύβλος the Greek name of Gebal, assimilated from Semitic Gəḇal with g > b, was transferred to the papyrus the Greeks bought there. Modern scholarship treats this as uncertain in the reverse direction: Beekes (Etymological Dictionary of Greek, 2010) holds βύβλος to be a Pre-Greek word and the town to have been named after it, and Etymonline records both possibilities ('the place name might be from the Greek word, which then would probably be of Egyptian origin'). So the arrow Hebrew > Greek is possible but no longer the consensus.\",\n     \"derivation_fa\": \"واژهٔ دوم این جعبه در کتاب به صورت bibua چاپ شده است و چنین واژه‌ای در یونانی وجود ندارد؛ این خطای چاپی کتاب است برای βιβλία (biblia) جمع βιβλίον، زیرا معنایی که نورایی می‌دهد («مجموعهٔ نوشته‌ها») عیناً معنایی است که کلاین در ص ۱۶۹ برای βιβλία می‌آورد. خوانش اسکن درست است و خطا از کتاب است. واژهٔ نخست، βύβλος، درست است: «پاپیروس؛ پوست درونی نی، کتاب»، با گونهٔ βίβλος و مصغّر βιβλίον. دربارهٔ خود اشتقاق، نورایی رأی سنتی (کلاین و اسکیت) را می‌آورد که نام بندر گبل به یونانی بیبلوس شده و سپس بر کاغذ پاپیروس اطلاق گشته؛ اما بیکس (۲۰۱۰) βύβλος را واژه‌ای پیشایونانی می‌داند و معتقد است نام شهر از روی این واژه نهاده شده است، نه برعکس.\",\n     \"sources\": [W + \"%CE%B2%CF%8D%CE%B2%CE%BB%CE%BF%CF%82\", \"https://www.etymonline.com/word/biblio-\", W + \"Byblos\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:169\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt line 4908 (leaf 101 = printed p.169), s.v. Bible: '... fr. Gk. βιβλία, “collection of writings”, pl. of βιβλίον, “paper, scroll, book”. This is the dimin. of βίβλος, βύβλος, “the inner bark of papyrus; book”, fr. Βύβλος, Greek name of the famous Phoen. transit port, whence the Greeks obtained the Egyptian papyrus. Gk. Βύβλος has been assimilated fr. Gebhḁl...' — word for word the source of this box, including the phrase 'collection of writings' that the misprint 'bibua' carries.\"},\n      {\"ref\": \"NAT:110\", \"status\": \"supports\",\n       \"note\": \"NAT_2005.txt leaf 127 (= p.112 of the 2005 reprint; Nourai cites the 1982 pagination, p.110): 'Byblos has been immortalized in the original Greek word for “rolled book,” biblion, from which Western languages get the words “bible,” “bibliophile,” “bibliography.”' This is also the source of the chart's odd phrase 'Rolled paper from Gebhal'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"SKT.txt line 1752, leaf 58 = printed p.38, s.v. Bible\", \"stance\": \"partial\",\n       \"note\": \"'M.E. bibel. — F. bible. — L. biblia. — Gk. βιβλία, collection of writings, pl. of βιβλίον, little book, dimin. of βίβλος, a book. — Gk. βύβλος, Egyptian papyrus: hence, a book.' Skeat has the whole Greek-Latin-English chain but stops at 'Egyptian papyrus' and says nothing of Gebal — confirming the reading 'biblia' for 'bibua' but not the Semitic link.\"},\n      {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt line 41268, leaf 320, s.v. Bible\", \"stance\": \"partial\",\n       \"note\": \"'[F., < LL. biblia, < Gr. biblia, pl. of biblion, dim. of biblos, byblos, book, papyrus.]' — same chain, again silent on the Phoenician port.\"},\n      {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 19072, leaf 202, s.v. biblio-\", \"stance\": \"partial\",\n       \"note\": \"'Gr. biblion, a book ... a combining form meaning (a) book, of books; (b) of libraries' — Webster derives the prefix from biblion without a Semitic etymon.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Latin\",\n     \"words\": \"biblia\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Late/Ecclesiastical Latin biblia was borrowed from Greek βιβλία biblia, the neuter plural of βιβλίον biblion 'book, scroll'; the Christian scriptures were already called τὰ βιβλία τὰ ἁγια 'the holy books' in Greek by c.223 CE, and the calque biblia sacra passed into Latin. In Latin the -a of the neuter plural was reanalysed as a first-declension feminine singular (gen. bibliae), so that 'the books' became 'the Book' — the shift that makes Nourai's gloss 'book' (singular) correct for the Latin stage though not for the Greek one. Ecclesiastical Latin keeps both: neuter pl. biblia, bibliōrum, and very late fem. sg. biblia, bibliae.\",\n     \"derivation_fa\": \"لاتین متأخر/کلیسایی biblia وام‌گرفته از یونانی βιβλία است، جمع خنثای βιβλίον «کتاب، طومار». از حدود سال ۲۲۳ میلادی مسیحیان یونانی‌زبان کتاب مقدس را τὰ βιβλία τὰ ἁγια می‌خواندند و این ترکیب به لاتین biblia sacra ترجمه شد. در لاتین پایانهٔ ‏-a‏ را به جای جمع خنثا، مفرد مؤنث گرفتند (تحلیل دوباره/reanalysis) و از این‌رو «کتاب‌ها» به «کتاب» بدل شد؛ پس معنای مفردی که نورایی برای لاتین می‌دهد درست است.\",\n     \"sources\": [W + \"biblia\", \"https://www.etymonline.com/word/Bible\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:169\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt line 4908 (printed p.169): 'Bible, n. — ME. bible, fr. OF. (= F.) bible, fr. L. biblia, fr. Gk. βιβλία, “collection of writings”, pl. of βιβλίον' — the Latin link exactly as drawn.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"SKT.txt line 1752, leaf 58 = printed p.38\", \"stance\": \"supports\",\n       \"note\": \"'M.E. bibel. — F. bible. — L. biblia. — Gk. βιβλία' — same Latin stage.\"},\n      {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt line 41268, leaf 320\", \"stance\": \"supports\",\n       \"note\": \"'[F., < LL. biblia, < Gr. biblia]' — Funk & Wagnalls marks it Late Latin, which is right: classical Latin has no biblia.\"},\n      {\"src\": \"LAT\", \"where\": \"LAT.txt (Ernout-Meillet), grep 'biblia'\", \"stance\": \"silent\",\n       \"note\": \"Ernout-Meillet covers the classical lexicon and has no entry for the ecclesiastical loan biblia.\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"English\",\n     \"words\": \"Bible, biblical bibliography\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English Bible is first attested c.1300 as ME bible, from Old French bible, from Latin biblia (see node #6); biblical is a 17th-c. formation on Latin biblicus with the English adjective suffix -al; bibliography is a learned 17th–18th-c. compound of Greek βιβλίο-/biblio- (the combining form of βιβλίον) with -γραφία -graphia 'writing', which reached English through French bibliographie — so the last two are formed on the Greek stem in modern European learned usage rather than inherited through Latin biblia, a distinction the single arrow blurs. (The book prints 'Bible, biblical' and 'bibliography' on two lines; the JSON runs them together as one comma-less string, which is why the words field reads oddly.)\",\n     \"derivation_fa\": \"انگلیسی Bible از حدود سال ۱۳۰۰ میلادی به صورت bible در انگلیسی میانه دیده می‌شود، از فرانسهٔ کهن bible و آن از لاتین biblia. صفت biblical ساختهٔ سدهٔ ۱۷ میلادی از biblicus لاتینی با پسوند ‏-al‏ است، و bibliography ترکیبی عالمانه از ستاک یونانی biblio- و ‏-graphia‏ که از راه فرانسهٔ bibliographie وارد انگلیسی شده است؛ پس این دو مستقیماً از biblia لاتینی نیامده‌اند، هرچند همه به یک ستاک می‌رسند. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/Bible\", \"https://www.etymonline.com/word/biblio-\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:169\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt line 4908 (printed p.169): 'Bible, n. — ME. bible, fr. OF. (= F.) bible, fr. L. biblia' — and Klein's derivatives run bibli-al, biblic-al on the same page, with bibliography on p.170.\"},\n      {\"ref\": \"AHD:129\", \"status\": \"not_checked\",\n       \"note\": \"Nourai's AHD page numbers are the 1975/76 New College Edition; p.129 falls in the main B word list (Bible / biblio-), not in the Indo-European appendix (pp.1505-1550), and no open scan of that edition exists — refs_online.json lists only lending copies. The local proxy AHD_watkins1985.txt is the IE-roots appendix only and has no Semitic entries.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"SKT.txt line 1752, leaf 58 = printed p.38\", \"stance\": \"supports\",\n       \"note\": \"Skeat gives all three under one head: 'Bible. (F.-L.-Gk.) M.E. bibel...'; 'bibliography. (Gk.) Gk. βιβλιο-, for βιβλίον; and γράφειν, to write.' — note that he too takes bibliography straight from Greek, not through Latin biblia.\"},\n      {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt lines 41268-41286, leaf 320\", \"stance\": \"supports\",\n       \"note\": \"'bib\\\"li-og'ra-pher ... [< Gr. bibliographos, < biblion (see Bible) + grapho, write]' — same analysis.\"},\n      {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 19072, leaf 202\", \"stance\": \"supports\",\n       \"note\": \"Webster's biblio- entry: 'Gr. biblion, a book ... a combining form meaning (a) book, of books; (b) of libraries'.\"},\n      {\"src\": \"NAT\", \"where\": \"NAT_2005.txt leaf 127 (p.112 of the reprint)\", \"stance\": \"supports\",\n       \"note\": \"'from which Western languages get the words “bible,” “bibliophile,” “bibliography”' — Berlitz names exactly the derivatives in this box.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-229.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk229.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-229.json > /dev/null && echo \"valid json\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 229",
 "description": "Write and validate page-229.json"
}
```


### [2026-09-06T15:37:17.764Z] TOOL RESULT

```
ok
valid json
nodes verified: 7/7
node verdicts: {'confirmed': 5, 'plausible': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'not_found': 1, 'not_checked': 3, 'supports': 6}
books consulted: {'supports': 15, 'silent': 5, 'partial': 6} | by book: {'RCH': 3, 'WEB': 3, 'SKT': 3, 'FSD': 3, 'KLN': 2, 'PHN': 2, 'LKT': 2, 'NAT': 2, 'AFM': 1, 'MON': 1, 'BQT': 1, 'ARY': 1, 'AFA': 1, 'LAT': 1}
```


## [2026-09-06T15:37:22.110Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"LAT biblia:\"; grep -c -i \"biblia\" LAT.txt; echo \"ARY جبل:\"; grep -c \"جبل\" incoming/ARY/ARY_pages.txt",
 "description": "Verify claimed silent greps"
}
```


### [2026-09-06T15:37:22.171Z] TOOL RESULT

```
LAT biblia:
0
ARY جبل:
0
```


## [2026-09-06T15:37:35.905Z] AGENT

Both "silent" claims verified. Page 229 done.

**Page 229 (book p. 199) — one entry, root `J.b.l` (Semitic "mountain"), 7 nodes**

- Root verdict: **confirmed** (1)
- Node verdicts: **confirmed 5, plausible 1, transcription_suspect 1**
- Ref checks: supports 6, not_found 1, not_checked 3 · Books consulted: 26 entries across KLN, SKT, FSD, WEB, PHN, LKT, RCH, NAT, MON, BQT, AFM, ARY, AFA, AKD, LAT

Flagged items:
- **transcription_suspect — node #5 Greek `bibua`**: no such Greek word. The printed page itself reads `bibua` (verified on the 300/400-dpi render; PNG saved to `data/verification/sources/refs/ocr/BOOK/229.png`), so `error_in: "book"` — Nourai dropped an `l` from βιβλία *biblia*. Proof: his gloss "collection of writings, book" is verbatim Klein p.169's gloss for βιβλία. **The extraction is faithful; no data fix needed.**
- **plausible — node #4 Hebrew `gebhal`**: faithful to Klein p.169, but the gloss "mountain" is not a Hebrew sense — Hebrew has only גְּבוּל *gəḇūl* "border, boundary" and the toponym Gəḇal (= Byblos, mod. Jubayl); "mountain" is the Arabic development. Also, papyrus was imported from Egypt and re-exported via Gebal, not produced there.
- Not a separate flag, but noted in node #5: the Hebrew→Greek arrow follows the traditional view (Klein/Skeat/Berlitz); Beekes 2010 holds βύβλος to be Pre-Greek with the *town* named after the word, and Etymonline records both directions.
- **Nourai page slip**: node #1 cites `KLN:170`, but Klein p.170 carries only the *biblio-* compounds; the Arabic *jabal* claim is on pp. 169, 655 and 826. Recorded as `not_found`.
- `FVA:68` (both Arabic and Persian nodes) and `AHD:129` remain `not_checked` — no digital copy of Nahvi, and no open scan of the 1975/76 AHD New College Edition (p.129 is the main word list, not the IE appendix). Both claims are independently confirmed by Moʿin (جبل [ع.] کوه؛ ج. جبال) and Klein/Skeat respectively.

No extraction errors to fix. `verify_check.py 229`: 7/7 nodes, **0 PROBLEM lines**.
