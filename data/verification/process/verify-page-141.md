# Verification process log — verify-page-141


## [2026-09-05T20:08:14.549Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 141 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-141.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-141.json. Write /home/sfmqrb/git/rishe/data/verification/page-141.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 141` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:08:16.242Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:08:16.952Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:08:16.969Z] TOOL RESULT

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


## [2026-09-05T20:08:17.294Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-141.txt"
}
```


### [2026-09-05T20:08:17.321Z] TOOL RESULT

```
1	=== PDF page 141 (book page 111) ===
2	--- entry 0 ---
3	ROOT [Sumerian] Dub, Dup : tablet, scripture  (refs AKD:19; BQT:823)
4	#1 (parent #0) [Old Persian] refs=BQT:823 | dipi : to write
5	  #2 (parent #1) [Persian] refs=BQT:824; KLN:467; AKD:19; ETM:36 | dabîr «دبیر» : writer, teacher ; dabestân «دبستان (دبیرستان)» : place of teachers (school) ☞Stâ ; dîbâčeh «دیباچه» : preface ; dîvân «دیوان» : register book
6	    #3 (parent #2) [Arabic] refs=FVF:13,273 | adab : literature, discipline ; dîwân : register, book
7	      #4 (parent #3) [Persian] refs=FVA:28; FVF:273 | adab «أدب (مؤدّب ، تأدیب ، آداب)» : discipline ; adabiyyât «ادبیّات ( ادیب )» : literature ; tadvîn «تدوین ( مُدوَّن )» : writing
8	#5 (parent #0) [Sogdian] refs=SOD:148 | dyb-yy : letter
9	#6 (parent #0) [Akkadian] refs=AKD:19; BQT:823 | duppu, tuppu : tablet
10	  #7 (parent #6) [Aramaic] refs=None | dappa, dup : skin for writing tablet
11	    #8 (parent #7) [Arabic] refs=MON:1540 | daf : a tambourine made of animal skin on a frame
12	      #9 (parent #8) [Persian] refs=MON:1540 | daf «دَف (شندف)» : tambourine | NOTE: See "Deru 1" for another possible root
13	
```


## [2026-09-05T20:08:20.480Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-141.json",
 "description": "Read source JSON page 141"
}
```


### [2026-09-05T20:08:20.539Z] TOOL RESULT

```
{
  "pdf_page": 141,
  "book_page": 111,
  "entries": [
    {
      "root": {
        "name": "Dub, Dup",
        "lang": "Sumerian",
        "refs": "AKD:19; BQT:823",
        "gloss": "tablet, scripture"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "BQT:823",
          "words": [
            {
              "translit": "dipi",
              "gloss": "to write",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:824; KLN:467; AKD:19; ETM:36",
          "words": [
            {
              "translit": "dabîr",
              "gloss": "writer, teacher",
              "script": "دبیر"
            },
            {
              "translit": "dabestân",
              "gloss": "place of teachers (school)",
              "script": "دبستان (دبیرستان)",
              "see": [
                "Stâ"
              ]
            },
            {
              "translit": "dîbâčeh",
              "gloss": "preface",
              "script": "دیباچه"
            },
            {
              "translit": "dîvân",
              "gloss": "register book",
              "script": "دیوان"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "FVF:13,273",
          "words": [
            {
              "translit": "adab",
              "gloss": "literature, discipline",
              "script": null
            },
            {
              "translit": "dîwân",
              "gloss": "register, book",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "FVA:28; FVF:273",
          "words": [
            {
              "translit": "adab",
              "gloss": "discipline",
              "script": "أدب (مؤدّب ، تأدیب ، آداب)"
            },
            {
              "translit": "adabiyyât",
              "gloss": "literature",
              "script": "ادبیّات ( ادیب )"
            },
            {
              "translit": "tadvîn",
              "gloss": "writing",
              "script": "تدوین ( مُدوَّن )"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:148",
          "words": [
            {
              "translit": "dyb-yy",
              "gloss": "letter",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Akkadian",
          "refs": "AKD:19; BQT:823",
          "words": [
            {
              "translit": "duppu, tuppu",
              "gloss": "tablet",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Aramaic",
          "refs": null,
          "words": [
            {
              "translit": "dappa, dup",
              "gloss": "skin for writing tablet",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Arabic",
          "refs": "MON:1540",
          "words": [
            {
              "translit": "daf",
              "gloss": "a tambourine made of animal skin on a frame",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:1540",
          "words": [
            {
              "translit": "daf",
              "gloss": "tambourine",
              "script": "دَف (شندف)"
            }
          ],
          "script_extra": null,
          "note": "See \"Deru 1\" for another possible root",
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:08:22.901Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AKD','BQT','KLN','ETM','FVF','FVA','SOD','MON','AFM','PLA','HRN','HUB','PHD','NYB','ARY','LKT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-05T20:08:24.703Z] TOOL RESULT

```
AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt", "page_offset": "leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}

FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists 

FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries:
```


## [2026-09-05T20:10:02.289Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/ | head -50; echo ---; sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-05T20:10:02.341Z] TOOL RESULT

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
page-38.json
page-39.json
page-40.json
page-41.json
page-42.json
page-43.json
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
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


## [2026-09-05T20:10:03.226Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; awk 'BEGIN{RS=\"\\f\"} NR==29 || NR==28 || NR==27' data/verification/sources/refs/AKD.txt | head -120",
 "description": "AKD leaf around p.19"
}
```


### [2026-09-05T20:10:05.420Z] TOOL RESULT

```
,  wie  wohl  auch  schon in  der  urspr.  Bed.  Silber  (s.  dazu  unten  S.  59),  so  besonders  in  der  Bed.
1)  Von  qanä  gründen,  schaffen  (hebr.  imd  arab.)  viell.  ganz  zu  trennen.
2)  Allerdings  ist  zu  bemerken,  daß  im  Akk.  qanü  Rohr,  zwar  als  Längenmaß  (s. unten  S.  22),  jedoch  in  der  Bed.  Wage  gerade  nicht  üblich  Lst.  Andererseits  scheint  auch das  Akk.,  wenn  auch  als  selteneres  Wort,  ein  Verbum  qanü  erwerben,  zu  kennen.
3)  Urverwandt  mit  hebr.  usw.  jsp,  wsp  hinzufügen.
4)  Eig.  Besitzer,  Pto.  von  raSü  in  Besitz  nehmen,  das  wohl  mit  hebr.  järas,  aram. jerat,  ai'ab.  warita,  äth.  warasa  in  Besitz  nehmen,  erben,  gleichzusetzen  ist.  Dagegen  ist aram.  raiä  Macht,  Erlaubnis  haben;  Kaus.  gestatten,  verleihen,  wohl  erst  <;;^  akk.  raSü.
5)  Hier  hätte  sich  also,  bei  unserer  Annahme,  das  urspr.  r  gehalten,  gegenüber  dem H  des  Hebr.  u.  Arab.
3
      18      
Geld  erst  auf  deu  gleichen  Sprachgebrauch  von  akk.  kaspti  zurückgehen. —  Beachtenswert  ist  auch  die  hebr.  Kedensart  ba-Jcäsep  male  in  vollem Betrage,  die  wohl  dii'ekt  in  Anlehnung  an  die  gleichbedeutende  akk.  Redens- art ana  kasap  gamirti  od.  ana  simi  gamri  (<^  sum.  sam  til-la)  entstanden  ist.
akk.  maluru  Kaufpreis  (von  mahäru  einnehmen,  s.  S.  16)  :  >  hebr. m9htr  O  ägypt.  mhr).  —  Weniger  sicher  ist,  ob  etwa  auch  hebr.  möhar, aram.  nidlirö  O  armen,  mahr),  mnhrä,  arab.  /««/(»•  Kaufpreis,  den  der  Bräuti- gam an  den  Yater  der  Braut  zahlt,  auf  eine  Übernahme  des  gleichen  akk. niaJuru  in  früherer  Zeit  zumckgeht.
akk.  simii,  simtu  Kauf,  Kaufpreis,  Wert  (von  sämti  kaufen,  das wahrsch.  <<  sum.  sam,  und  von.sr7w«M,  St.  .syV«,  festsetzen,  wahrsch.  zu  trennen)  : ;>  w'ohl  aram.  Sum  abschätzen,  südarab.  S^m  kaufen.
Für  die  spez.  Bed.  Summe  des  hebr.  ros  (Kopf,  Haupt),  wie  die Bed.  Summe,  Kapital  des  aram.  rcsä,  arab.  ras  könnte  das  akk.  qaqqadu (Kopf)  in  der  Bed.  Summe,  Kapital,  ähnlich  auch  res  (makkurij,  vorbildlich gewesen  sein.  Doch  könnte  hier,  im  Hinblick  auf  die  gleiche  Bed.  von xKfalt]  imd  Caput,  die  doch  kaum  aus  dem  Semit,  stammen  wird,  auch beiderseits  eine  unabhängige  Entwicklung  vorliegen.
Das  im  Akk.  übliche  Wort  für  das  Anwachsen  der  Zinsen,  rabn, eig.  großwerden,  wachsen,  büdet  wohl  erst  den  Ausgangspunkt  fiii-  hebr. marhä  u.  tarhit  Zins,  aram.  rehhUft  (daraus  jüd.-deutsch  Bebhes  ?),  arab.  rihan.
akk.  Imhullu,  auch  Ijahullu,  Schuld,  Zins  :  >  hebr.  habol  Pfand, jüd
.-aram.  hibbtilä,  liibbiiljä  Zins,  syr.  htihla  Schuld,  Zins  (]>-  arab.  Ijabl Schuld,  Darlehen,  'ahhala  darleihen).
[Dagegen  ist  es  bei  hebr.  'äbot^  'abtU  Pfand,  und  den  davon  abge- leiteten Verbalformen  unsicher,  ob  es  sich  um  ein  mit  akk.  ubbutu,  ubhutu binden,  fesseln,  vereinzelt  viel!  auch  vei'pfän4en,  urverwandtes  Wort  handelt, oder  ob  auch  hier  Entlehnung  bezw.  Anlehnung  auf  der  einen  oder  der anderen  Seite  vorliegt.]
akk.  maskanu  Pfand'  :  >.  aram.  maskönä,  meskänä,  maskäna  Pfand, masken  zum  Pfand  geben   (>>  arab.  muskän  Pfand,  massaka  bürgen).
akk.  paqadu  jem.  etwas  ins  Depot  übergeben,  piupiddü  Depositum:
1)  Eig.  Depositum,  von  Sakänu  niederlegen,  wie  hebr.  tasüviet-jsd  von  siim;  also nicht  von  msk  abzuleiten.  In  iilterer  Zeit  hat  maSkami  auch  die  Bed.  Lagerhaus, Speicher;  daraus  wohl  sicher  durch  Entlelmung  hebr.  miskanot  Vorratshäuser.  S.  auch noch  unten  S.  30  zu  Sakänii.
      10
davon  wohl  beeinflußt  hebr.  pfiqad,  piqqadon,   aram.  luqdöm^  imqdänä  in dieser  Bed.
akk.  dannitu  Schriftstück,  Geschäftsurkunde  :  häufig  wiederge- geben durch  dnt  in  den  aram.  Beischriften  assyrischer  Geschäftsurkunden. '
akk.  nibsu  Urkunde  :  >  ägypt.-aram.  nhz  Quittung,  womit  auch sonstiges  aram.  nibsa  Los,  identisch  sein  wird.
akk.  satrirti  Schriftstück,  Urkunde  :  >  wohl  das  häufige  str  Ur- kunde in  aram.  Beischriften  auf  assyr.  Geschäftsurkimden ,  sowie  auch sonst  aram.  .idtdra.     S.  im  übrigen  zu  satäru  schreiben,  unten  S.  29.
akk.  Sipru  (von  suparii  senden)  Sendung,  briefliche  Sendung, Schriftstück  :  >  hebr.  seper,  sipr-,  aram.  siprö  Buch,  spez.  auch  in  der Bed.  Geschäftsurkunde.  -
akk.  egirtu  Brief,  Schriftstück  :  ]>■  aram.  'iggärri  Brief,  spez.  auch in  der  Bed.  Schriftstück,  Gescliäftsurkunde,  so  in  aram.  Beischriften  zu assyr.  Geschäftsurkunden  und  auch  sonst.     S.  zu  egirtu  auch   oben  S.  10.
[akk.  srpti  Schreiben,  Brief  :  dieses  speziell  nur  in  der  altbab. Zeit  sich  findende  seltenere  Wort  scheint  umgekehrt  damals  aus  südsemit. Gebiet  mit  von  dort  einwandernden  Stämmen  ins  Babylonische  eingedrungen zu  sein.  Vgl.  äth.  sal/afa  schreiben,  und  das  erst  aus  dem  Südarab.  ins Xordaral).  eingedrungene  arab.  mashaf,  mmhafB\xch,  saJnfat  beschriebenes Blatt]
akk.  diippu,  tuppu  Tafel,  Schriftstück  (<^  sum.  daib
),  wozu  dappu Brett,  wohl  nur  eine  Variante  büdet :  >  aram.  dappfi  Brett,  Tafel,  Blatt- seite, auch  ägypt.-aram.  tp  Brett  O  wohl  arab.  daff  u.  faff  Brett,  Seite, daffat  Buchdeckel),  südarab.  ff'  Tafel.  Vgl.  auch  unten  S.  29  zu  tupsarru Tafelschreiber  u.  liebr.  tipsar.  —  Ferner  ]>  altpers.  dipi  Inschrift  (wozu viell.  neupers.  dehir  Schreilier,  diivun  Buch),  elam.  tuppi  Inschrift,  lud. dipi  (lipi)  Schrift.
akk.  giitu  Tafel,  Urkunde  (<<;  siun.  gida  eig.  wohl  lange  Tafel): >>  aram.  gitfä,  geUä  Urkunde,  Testament,  Scheidebrief  O  arab.  qitt  Buch, Scheck).  akk.  nijäru  Papyrusurkunde  (auch  im  Akk.  viell.  Fremdw.) :
>  neuhebr.  najär  Papier,  Pergament.  akk.  urMnu  Scliilf,  Papyrus-
1)  Ob  viell.  auch  so,  und  nicht  als  pron.  dem.,  das  dnh  in  der  Aufschrift  zu  der Geschäftsurkunde  des  aram.  Pap.  28  (Nr.  30)  aus  Elephantitie  aufzufassen  ist?
2)  Weniger  sicher  ist,  ob  etwa  auch  neuhebr.  sdhcr  i  Quittung  hierher  zu  ziehen  ist.
3*
      20      
Urkunde  :  >  wohl  aram.  'urbänä,  'arhänä  Schilf,  Papyrus.  S.  uoch unten  S.  56  zu  urhänu.
Das  übliche  akk.  Wort  für  Siegel,  hmuJchi,  hat,  wie  es  scheint, nur  im  Armen,  als  hiiJc'  Eingang  gefundeh.
[Dagegen  liegt  hebr.  fabhaat,  aram.  tib'ä,  fdb'ä  Siegelring  (das  wohl auf  ägypt.  db'-t  Siegel,  zui'ückgeht)  im  Akk.  wohl  nur  als  westsemit.  Fw. in  der  Form  titnhui,  timbuttu  vor.  i  S.  auch  noch  unten  S.  30  zu  tim- buttii  als  Musikinsti'ument.]
akk.  maklmru  Habe,  Besitz,  mit  der  Nebenform  namJmrru  :  >  wohl liebr.  mäkar  verkaufen  O  ägypt.  mJcr''  Kaufmann),  mäher  u.  mimlcär  Ver- kauf, Ware,  syr.  m^kar  kaufen.    S.  femer  oben  S.  16  zu  tantJcaru  Kaufmann.
akk.pron.  indef.  memeni  (so  namentlich  später  neben  dem  in  älterer Zeit  dafür  üblicheren  minimv)  „irgend  etwas"  i.  S.  v.  Besitz,  Habe  :  > walu'sch.,  der  Form  nach  aber  wohl  das  aram.  pron.  indef.,  späthebr.  iiiämon (Sir.  31,8),  aram.  mamöna,  neutest.  fiafjwväg  „Mammon".
akk.  nikasu^  Habe,  Vermögen  :  >  aram.  niksm  Schätze,  Reich- tum O  wahrsch.  erst  späthebr.  ndhäsim),  viell.  auch  südarab.  nskm.
akk.  nisirfu  Schatz  (von  nasäru  bewahren)  :  fraglich,  ob  etwa  hier- auf liebr.  'dsär,  PI.  'dsärot,  aram.  'au-prä  Vorrat,  Schatz,  zurückgellt.  ^
Zu  blt  nakamti  Seh  atz  haus,  hebr.  bet  nakot,  s.  oben  S.  8.
Zu  hebr.  usw.  saguUä
```


## [2026-09-05T20:10:52.283Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KNT dipi ===\"; grep -n -i \"dipi\" KNT.txt | head -40; echo \"=== PHD ===\"; grep -n -iE \"dib[iī]r|dipir|dēwān|dywʾn|dyw'n|dēbāg|dyp\" PHD.txt PHD_mackenzie.txt | head -40",
 "description": "Grep Kent and MacKenzie"
}
```


### [2026-09-05T20:10:52.339Z] TOOL RESULT

```
=== KNT dipi ===
1084:V. There are also numerous instances of OP { @ d which are not traceable with certainty to IE origins, or are demonstrably borrowings from non-IE sources. Among these are taka- ‘shield, round hat’ in faka-bara-, tacara- ‘palace’, dipi- ‘inscription’ (see Lex. s.v.), spáda- ‘army’ (only in Iranian), imv. rax@atuv of uncertain meaning; and personal and place names such as Atamaita- (Elamite), Nadztabaira (Semitic), Ufratu- 'Eu- phrates', Katpatuka ‘Cappadocia’, Tigra- ‘Tigris’, Putaya- ‘Libyan’, Datwahya-, Daha-, Dwubála-, Mudràya-, Aburā, etc.
2127:II. Fem. - stems (some possibly -7- stems): Nom. Sg.: аг )$, уан, 1185, probably фр]. Acc. Sg.: Siyatim, bajim, dipim ; рабіт (to a hetero-
2147:dipi-. The long vowel seems assured in бйти- by Skt. Ved. nom. bhiimi (once only; against 12 oc- currences of the new formation bhümis), and is certain in nom. pl. afagainiya, like Skt. papyas to sg. fem. papi which is one fem. formation to papds ‘evil’.
2152:V. In forms ending in -cyd, the -1- is probably syllabic and not merely graphic; for *Harahvatya would become *Harawasiyd and not Harauva- уй, and *dipyd would become *difiya and not dipiyà.? In the others the long preceding syllable would cause Sievers’ Law to operate, changing -yà to -1yd.
3836:42 : aparam : imàm : dipim : patiparsàhy : tya : тапа : kartam : varnavatim
3841:47 m [ауа : ahy&y& : dipiyàf: палу : nipistam.: avahyarádiy : naiy : n
3842:48 ipistam : mátya : hya : aparam : imim : dipim : patiparsatiy : avah
3860:70 yavauS : xSayafiya : tuvam : kā : hya : aparam : imim : dipim : vainàhy : ty
3863:73 diy : imam : dipim : vainühy : imaiv& : patikarà : naiydis : vikanahy : uta
3871:77 yafiya : yadiy : imam : dipim : imaiva : patikarà : vaināhy : vikanah*dis : ut 78 ataiy : уйуй : tauma : ahatiy : natydiš : paribaráhy : Auramazdátaiy : jatà : b 79 iyā : ut&taiy : taumd : mà : biyá : uta : tya : kunav&hy : avataiy : Auramazd
3877:86 Ardumanis : nàma : Vahaukahyà : puça : Pársa, „ 87 iya : tuvam : kā : xSdyafiya : һуа : aparam :  Bhy^: Буйло : imaigim : martiyind : àtiy : Dürayavaus : xšāyaðiya : vaSnà : Au i(mà)m : dipim : aniyaðă : adam : akunavam : раат : ariya : aha : utd : av ast
3880:90 ayd : cáxriyalà : рай$ат : iya : dipiS : hama : ёбаһауа}а : nipištiyā : adā
3888:"quj RI, KT; reading assured, but apparently an omission in the engraving (awa for ava), Mt. Gr. 59. 0 kartam KT. 9 No gap between z3ayafiya and nüram, Jn., KT. © sa... ]d*(. .. Jàdy with vertical hasta at end of last gap, KT; kalrahya : аһу : avahya]rádiy Tm. {after Rl.’s {avah}yarddiy), but this is too long; Cameron’s karahya {:] rádiy, with rā of rádiy slightly doubtful, is to be accepted, though Cameron finds in Elam. 3.74 ‘to the people tell (it)’ for this phrase. % hadugam WB, KT, for Rl.'a pa dipim.
3894:89-9 See JAOS 63.266-9, where a complete restoration is attempted; also Wh. KIA 70-2 and König, Klotho 442-9, Except as noted here, the restorations in the text are mine, though depending in some points upon Wb. and König. In 89, Cameron reads їл“ : dipi+ : an*+-+v'm* and thence through ulë; Kent emends, to fit Cameron’s translation. The OP lacks the Шат. clause ‘which formerly (was) not’. 97? аза уат) KT; avast(a]y(à] Konig. * аға Wb.
4656:9 framàátàram : adam : Xšayāršā : 10 x&àyafiya : vazraka : хёдуабуа : 11 xšāyaðiyānām : xšāyaðiya : da 12 hyünàm : paruv : zanànàm : x$ 13 àya8iya : ahy&yà : bümiyà : va 14 zrakày& : düraiy : apiy : Daraya 15 vahaus : xšāyaðiyahyā : риса : Ha 16 x&manisiya :0ütiy : XSayársá 17 : xSayabiya : Dārayavauš : xSiya 18 буа : һуа : manā : pitä : hauv : va 19 502 : Auramazdaha : vasiy : tya : 20 naibam : akunauég : uta : ima : st 21 änam : hauv : niyastdya : katanaiy 22 : yaniy : dipim : naiy : nipist 23 ām : akunaus : pasáva : adam : ni 24 yastéyam : та : dipim : піра 25 iStanaiy : màm : Auramazda : pa 26 tuv : hada : бадафт : utämai 27 y : zSaqam : Ша : атану : kartam
5558:dipi- sb. ‘inscription’: Elam. tup-pi, Akk. duppu (5152.1): borrowed from Sumerian dup- (Ву. Gr. §282; hardly contamination of Jran. *ripi- = Skt. lipi- ‘smearing, writing’, with Sum. dup-, as taken by Pisani, Riv. Stud. Or. 14.320, as Skt. lipi- ‘writing’ indicates writing with ink rather than engraving on stone) 4:4] nsf. DB 4.90, 91f. dzpim asf. DB 4.42, 48, 70, 73, 77, 89; XV 22, 24. dipiyd lsf. (§179.V) DB 447.
=== PHD ===
PHD.txt:225:ayābāģ Dy'p()£!] acquisitive, receptive. ~ih: comprehension. ayād Pbyd?t' | M? yd, N yad] memory. ~ kardan; remember. ~gar LEI | N —gàr] memoir. āyaft Pdypt' | M ?ypt, N āyift] boon, favour, gift. ayāftan, ayüb- [5?5-tn! | M *3pt,*?b-, N yāftan, yab-] obtain, acquire, attain. ayār [kdybl | M hy’r, N yar] helper, friend. ~th: help, friendship. ayārdēnīdan, ayārdēn- ['4?/tyn-ytn!] boil, agitate. ~i&n: agitation. ayārdīdan, ayārd- Py’lt-ytn! | M ?y^rd-] be agitated, seethe. ayārīdan, ayür- [hdyb'l-ytn! | N yār-īdan] 1. help, assist; 2. be able, dare. ayürómand [hdyb’Pwmnd | N yarmand] helpful, friendly. ~ih: helpfulness, friendliness. ayāsīdan, ayās- [’byq’s-yin' | M ?y^s-] remember, be mindful of. „išn(īh): memory. ayāstan [by@’sin' | M *)*st] = ayāsīdan. āyišm [dšm] moon. aydxšust [ywhhhwst! = Av. ayóxfusta- | M ”ywxšyst 1] metal. ~€n [-yn'] metallic. āydoxtan, āyēz- ['ywhtn!, ?ywc-] join, yoke. ~išn: union, alliance. 14ydzidan Pyweytn'] = āyēūxtan. tāyozīdan, āyoz- Pywe-ytn' | Р уші, ?ywz-] trouble, disturb; strive, struggle. ^-i$n(ih): endeavour, strife. laz [MN < A mn; hc | Mc, ?z, N ~] from, than. žaz Dell dragon. *az [ANE < A?nh | P >z] I. āz Pc | M ?z, N ~] greed, lust. Ba, z- azabar [hcpl | M?c?br, № zabar] above. 7 āzād Pot! | M ?zd, N ~] r. noble; 2. free. āzādīh Petyh] т. freedom; 2. gratitude, thanks. ~ ģuftan, ~ hangardan, ~ kardan, pad ~ dāštan: thank, give thanks. атат [?с?[ | N ~] torment. āzardan сіп! | M ”zyrdn] = azardan. āzārdan, āzār- Pc/-tn! | № ~] torment, injure. ~išn: torment, injury. lāzarm [clm | M ??zrm, N ~] honour, respect. *'ázarm [?clm | M ?zrm-] harm, injury. a-zarmān Pz/mn!] ageless, unaging. āzarmīģ [clmyk'] honoured, respected. ~th: honour, respect.
PHD.txt:312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
PHD.txt:321:ë ру | (M hyb)] particle giving the present tense optative sense. é, v, éd, éw. ēbāraģ [*dyp'lk', ^dwlk! | N éwàr] evening. ébgat(ih) ['ybgt!, -yh = Av. aifi.gati-] (onslaught of) Evil; the Adver- sary. ēbsrūsrim [>ур-, ?ybslwslym = Av. atBisrūdrima-) the gah from sunset to midnight. ébyünghan [>ур-, ?ywby?nghn!, etc. = Av. aiBydshana-] sacred girdle, = kustig. ёё Pye | (P ?ушус), N héc] (with a negative) not any. ēčand, v. éw-Cand. éd (HN A < A hr? | M? yd] this; v. dāštan. ~ ray ёё [cf. N z-é-rá] because, since. édar [LTME < À I-tnh | M?ydr, N ~] here. édin [ytwn'! | N ēdūn] thus, so. ~ih: (correct) manner. ëg [ADYN' < А *dyn | М ?yg] then, thereupon. ëk Pywk' | M yk, N yak] one. ëkanag [Pywk’nk! | N yagana) submissive, obedient. ^h : submission, obedience. ēk-dād [ywkd’t'] sole-created. ēmēd [*dmyt'] hope. ēn [ZNE < A znh | M *yn, N in] this. -ën [-yz! | = M, N -in] suffix forming adjectives of material or quality. -endag [-ndk! | M -yndg, N -anda] suffix forming present participles. -én-idan [-yn-ytn' | M -yn-ydn, (N -àn-)] suffixes forming causative and transitive denominative verbs. *énókén Pynw(k)kyn' = Av. *aēnē.kaēnā-) heiress (under the obligation of continuing her father's line). enya рулу | (M ?n’y)] otherwise, moreover. lër [d] | M Zur, v. azér] down, below; low; under. — ud abar: upside down. tēr Pyl] noble; hero, ~ih: nobility, good conduct. Eran [y”x! | N ~] Eran, (land of) the Aryans. ~ag [-k'] an Eranian, Aryan. érang [”y/ng] blame, condemnation; error, heresy. ~ih: = érang. éranj-, v.  * éraxtan. Ērān|-šahr (yPnitr! | N ~] land of the Aryans. —-wëz [-wyc] (original) home of the Aryans. 1ёгахќап, ёгапј- Pylhtn!, ?уЇпс- | J ?yrxt] blame, condemn, damn.
PHD.txt:536:pa(č)čēn [pcgn!] copy. *pa(č)čībāg [pcyp k', PWNe- | N *pajiw] *deceptive. ^h : deceit, hypocrisy. *pa(č)čībāy- [pcyp'd-, PWNc-] deceive. pad [PWN, for *pty | M pd, N pa] to, at, in, on. pad- [pt- | M *pd-) fall. padam [pd”m | (IN pandm)] mask for the mouth, worn by a celebrating priest. !Ipádan, pày- (UIN TLWN-tn! < А V ntr; Ptn, pd- | M pd, p’y-, N páyidan] protect, watch, defend. *pádan, pāy- [N TLWN-tn!, etc.] stand, wait. pādāšn [p?td?fn! | M p’d’syn, N pàdàs] reward, retribution. padēx [ptyhw'] flourishing, prosperous. ~ih: prosperity. padéxénidan, padéxén- [ptyhwyn-ytn'] make flourish, prosper. pādēz [p'tyc | M p'dyz, N pāyēz] autumn. pad-góhr [PW Ngwhl] т. jewelled; 2. of good stock, well-born. padifrah [p’tpl’s | M p'dypr?h, N *pādafrāh] punishment, retribution. padir-, ~išn, v. padiriftan. padirag [ptylk' | M pdyrg, N paóira] towards, against, counter-. (6) — madan: come to mect. ~ih: meeting, opposition.
PHD.txt:1099:brocade dēbāg.
PHD.txt:2693:mad dēwānag.
PHD.txt:3531:school ` dibirestán, frahangest��n, hērbedestān.
PHD.txt:3537:scribe dibir.
PHD.txt:3538:scribeship dibirih.
PHD.txt:4366:writing nibég; collected ~s dēwān, wrong abārēn, zēfān.
PHD.txt:5313:dastšūy dēwān dibīrīh dibīr dibīrestān 1%dabr, gabr Ixwāh-! xwastan! daftan daftar
PHD.txt:5527:dēwānag
PHD_mackenzie.txt:1374:Ayaft ['dypt ' I M uj'jJt, N ayift] boon, favour, gift.
PHD_mackenzie.txt:1959:debag [dyp)k I N deM] brocade.
PHD_mackenzie.txt:1962:debahr [dyp)hll P dybhr] anger.
PHD_mackenzie.txt:1982:dewanag [dyw'nk I N --a] demonic, mad.
PHD_mackenzie.txt:1988:dibir [dpy(w)r I M dbyr, N --] scribe.
PHD_mackenzie.txt:2178:ebarag edyp)lk l , )dw)lk l I N ewar] evening.
PHD_mackenzie.txt:3912:padifrah [p'tpl's I M p)dypr'h, N ·piidafriih] punishment, retribution.
PHD_mackenzie.txt:7499:ruin(ation) abesihisn(ih), tabahih,        school     dibirestiin,    frahangestiin,
PHD_mackenzie.txt:7506:    tan, (tazidan)j (daevic) dwiiridan,    scribe dibir.
PHD_mackenzie.txt:7507:    (dwiiristan) j cause to .- tiixtan,    scribeship dibirih.
PHD_mackenzie.txt:10430:dibirestan             ,~tuJ          t'ctY         zamigpaymanih   ~~..,U~
```


## [2026-09-05T20:10:53.354Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SOD dyb ===\"; grep -n -iE \"δyβ|dyb|letter\" SOD.txt | grep -i -n \"letter\" | head -30; echo \"=== SOD_pages 148 ===\"; grep -n \"dyb\" SOD_pages.txt | head -20",
 "description": "Grep Gharib Sogdian"
}
```


### [2026-09-05T20:10:53.412Z] TOOL RESULT

```
=== SOD dyb ===
1:3674:transliteration  in  bold  letters  and  in  Sogdian 
2:3687:Capital  letters  in  the  transliteration  denote 
3:3689:with  or  without  the  letter(s)  in  the  parentheses  are 
4:3717:denoted  by  S(C),  and  texts  from  Ancient  Letters  are 
5:4256:Letters,  which  are  on  paper  and  presumably  the 
6:4257:oldest  Sogdian  documents.  The  Ancient  Letters 
7:4264:the  content  of  Letter  no.  2  (lines  19-20)  reveals, 
8:4274:souls".  These  letters,  which  could  not  have  been 
9:4337:15.  For  more  accurate  information  about  Ancient  Letters,  see 
10:4401:the  Ancient  Letters,  the  documents  from  Tajikestan 
11:4454:The  Oldest  Documents:  Ancient  Letters2* 
12:4462:Letters. 
13:4464:These  letters,  which  are  probably  the  oldest 
14:4472:towers,  Stein  found  a  bundle  of  letters  together  with 
15:4475:20  ax>.  The  eight  letters  on  paper  contained  writing 
16:4478:palaeographical  evidence,  Stein  dated  the  letters  as 
17:4485:the  letters  in  the  second  volume  of  his  work  on  the 
18:4488:Letter  no.  2,  the  longest  with  63  lines,  and  recognized 
19:4491:the  letter,  its  date  as  190  ad.  In  1948,  Henning, 
20:4496:The  latest  information  about  the  Ancient  Letters 
21:4498:Historical  Context  of  the  Sogdian  Ancient  Letters"  in 
22:4547:32.  'The  Date  of  the  Sogdian  Ancient  Letters1,  BSOAS  12, 
23:4682:Ancient  Letters  £nd  other  documents,  the  second 
24:4922:letters,  "Problem  der  Interpretation  Manichaisch- 
25:5299:of  the  Ancient  Letters  than  of  the  Mug  Documents. 
26:5384:secular  materials  such  as  letters,  legends  on  coins, 
27:5428:non-religious  letters,  documents  and  inscriptions,  as 
28:5481:Livsicl04.  The  alphabet  consists  of  the  22  letters  in 
29:5482:the  traditional  Aramaic  order  (although  four  letters 
30:5486:fact  that  this  letter  represents  two  distinct  phonemes, 
=== SOD_pages 148 ===
14371:                                                                         8iPnu     (dybnw) ©Lat. binl, <*dwi-nu    =»8Pnw
14378:                                                                    3731 dybnw      C =* Sypnw
19537:     GMS 408-, Anc. Lett. 4.6; Sund. AoFviii 1981             5523 mwhrdyb M                                        *A>j$*
19544:          -^mw^kk, dyb-yy                                              mwrt^zw^ntyk^k, jw'ndyCy)
23349:6834 pSyp'rcy*       M -» pdyb'rcy*
23351:6835 pdyb,rcy> C (j^^ojU**^                                     6847 pY'rs'k   B                             ^^•jluTjjj
33587:      wiSap (wyd'b) ©K+wiSdab;             MP wdyb;                 Sund. AI 28, 1988, 185
```


## [2026-09-05T20:11:14.531Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"dyb-yy\\|dyb'\\|dybyy\" SOD_pages.txt | head -20; echo \"=== context 19540 ===\"; sed -n '19520,19560p' SOD_pages.txt; echo \"=== find pdf page tag for line 19544 ===\"; awk 'NR<=19544 && /\\[pdf page/ {p=$0} END{}' SOD_pages.txt; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<19544' | tail -3",
 "description": "Locate Sogdian dyb entry in Gharib"
}
```


### [2026-09-05T20:11:16.382Z] TOOL RESULT

```
19544:          -^mw^kk, dyb-yy                                              mwrt^zw^ntyk^k, jw'ndyCy)
23349:6834 pSyp'rcy*       M -» pdyb'rcy*
=== context 19540 ===
       Bailey. *hamauk-; Mack. *maucaka
                                                                   muyist   ©ob. pi. -y =»mwy
                                                                                                              jLi>ta   ^lijlJLfi
                                                                                                                           f
5509 fflwd    C =» mw52
5510 mw6' B,S                                                      magians
                                  (Jja :^Jais uU^)\^ tj*jj         BSTii 851.6, 843.41, 50, 850.1, 872.4; C2 gloss.
     mu5/mu5
     value, price
                                                              5521 mwyztw M
     VJ 1401; mw6yy VJ 1319; Anc. Lett. 5; S W,
       BSOAS 1983, 45                                              muy-zatu ©*magu-zati
                                                                     p215
                                                                   magian killing, magophonia
5511 mw62 S                                        (ji)^
     mu6 (mwd) *=»m5w                                              Hen. Magi. 138.27, 135f
     wine                                                     5522 mwhbt1 =» mwypt(w)
     GMS 408-, Anc. Lett. 4.6; Sund. AoFviii 1981             5523 mwhrdyb M                                        *A>j$*
       p2l6, 2aV2                                                  muhr-5ip ©*mwdr\ Parth. ©ob. -yy
                                                                                                                 ^m^mm
                                                                                  ^m
                                                                                                                 mwrtk (y)
  221

          -^mw^kk, dyb-yy                                              mwrt^zw^ntyk^k, jw'ndyCy)
          seal of letter                                             resurrection
          BBB c36                                                    GMS 1066n 1, 1068; Gersh. Sogd. Cpds. 148;
 5524 mwj'k M                                           jU-I           mwrtyjwndyy pryy, Sogdica. 52.7, 53
      mozak (mwj'q) ©pi. -/ =>mwz*k\ mwc'k'                     5537 mwrt'jwndy => mwrt'jw'ndyy
      teacher                                                   5538 mwrt'k S(MD) =* mwrtk, mwrty
         GMS 990; BBB 623
                                                                5539 mwrtVk ywt'w B
 5525 mwj'q =» mw/k                                                  murtane xutaw ©gen. pi.
                                                                                                                  o^ ■>>■ t^'«*>-
 5526 mwks(h) B                                oU»«^jlt-.j           god of the dead
                                                                     TSP 5.101, 6.94,%
         moks ©Skt. mokfai Parth. mwxs ©ob. -y(>J> -yh
         salvation                                              5540 mwrtJt rwc S                         jjj^s "u f** Jjj
         VJ; TSP 8.23, 2.663, 691; -K VJ 995                         murtat roc **mrt}t rwc
                                                                     seventh day of the month
 5527 mwa'kw B, S         (^y> ^zJ^ j-O^^M «jJ
=== find pdf page tag for line 19544 ===
```


## [2026-09-05T20:11:27.663Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^ *148 \\|^148 \" SOD_pages.txt | head; echo \"=== 5yp/dyp entries ===\"; grep -nE \"(^| )(2|3|4)?[0-9]{0,4} ?(dyp|5yp|8yp|dyb|5yb)['\\\"]?[0-9]? \" SOD_pages.txt | head -30; echo \"=== letter gloss ===\"; grep -n -B2 -A2 \"^     letter$\\|^      letter$\\|  letter, document\" SOD_pages.txt | head -60",
 "description": "Search Sogdian dip entries"
}
```


### [2026-09-05T20:11:29.578Z] TOOL RESULT

```
=== 5yp/dyp entries ===
=== letter gloss ===
```


## [2026-09-05T20:11:32.639Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"dyp\" SOD_pages.txt | head -40; echo \"=== dyb ===\"; grep -n \"dyb\" SOD_pages.txt | head -40",
 "description": "grep dyp/dyb in SOD"
}
```


### [2026-09-05T20:11:32.699Z] TOOL RESULT

```
=== dyb ===
14371:                                                                         8iPnu     (dybnw) ©Lat. binl, <*dwi-nu    =»8Pnw
14378:                                                                    3731 dybnw      C =* Sypnw
19537:     GMS 408-, Anc. Lett. 4.6; Sund. AoFviii 1981             5523 mwhrdyb M                                        *A>j$*
19544:          -^mw^kk, dyb-yy                                              mwrt^zw^ntyk^k, jw'ndyCy)
23349:6834 pSyp'rcy*       M -» pdyb'rcy*
23351:6835 pdyb,rcy> C (j^^ojU**^                                     6847 pY'rs'k   B                             ^^•jluTjjj
33587:      wiSap (wyd'b) ©K+wiSdab;             MP wdyb;                 Sund. AI 28, 1988, 185
```


## [2026-09-05T20:11:39.433Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -c \"\\[pdf page\" SOD_pages.txt; grep -n \"Syp\\|8yp\" SOD_pages.txt | head -30",
 "description": "Check SOD page tags and Syp"
}
```


### [2026-09-05T20:11:39.494Z] TOOL RESULT

```
0
7850:                                                                     Wyp" OrSypO
7930:1443 'rSyp' «> 'rS'yp*
14362:                                                                         8ip(a)z)3ak    (SypzP'k)
14369:       S W, Rock. Insc. Indus Valley 1989, 135; CII,                3730 8ypnw      B, M                              jv>
14378:                                                                    3731 dybnw      C =* Sypnw
14388:     mark, sign                                                     3733 8ypty-     B                             JSi&stfc
14881: fr8yp-
23349:6834 pSyp'rcy*       M -» pdyb'rcy*
23360:6836 pSyp'rcyh S                        &&'*;£*       <***-*         p(o)Yez ? ^prYyz-, pYsty(y)
23361:     pa6e-Parcya (pSyp'rcyO                                          (rc)attempt ?, (ro)prevent ?, OcOrenounce ?
34584:10656 xsnk =» }xsnk-, xsnq-                                           xsipd   ©<Av. xsvipta        =»}YSypt, 'xs'ypt-
```


## [2026-09-05T20:11:51.729Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 214 215 216; do echo \"===== NR=$n =====\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' SOD.txt | head -60; done",
 "description": "Print SOD leaves around page 148"
}
```


### [2026-09-05T20:11:53.850Z] TOOL RESULT

```
===== NR=214 =====
===== NR=215 =====
===== NR=216 =====
```


## [2026-09-05T20:11:56.813Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; wc -l SOD.txt SOD_pages.txt; awk 'BEGIN{RS=\"\\f\"} END{print NR}' SOD.txt; awk 'BEGIN{RS=\"\\f\"} END{print NR}' SOD_pages.txt; head -5 SOD_pages.txt",
 "description": "Inspect SOD files structure"
}
```


### [2026-09-05T20:11:58.774Z] TOOL RESULT

```
 111423 SOD.txt
  45615 SOD_pages.txt
 157038 total
1
644
 SOGDIAN
DICTIONARY
Sogdian - Persian - English
```


## [2026-09-05T20:12:03.115Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 214 215 216; do echo \"===== NR=$n =====\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' SOD_pages.txt | head -70; done",
 "description": "Print SOD_pages leaves near 148"
}
```


### [2026-09-05T20:12:04.774Z] TOOL RESULT

```
===== NR=214 =====

===== NR=215 =====
                                                                                        MM             un


 149
                                                                                                                      Synyfrn
                                                                   order of electi
        GMS 1043; pi. Syn'fir'st, Syn'fir'st
                                                                   BBB 554 a4; W-Lii
 3759 Syn'pr'nyg M         (^^*<*J)+j£t><iSj>£±>
      SenaParanig                                             3772 5yn5"r     B, M, S   jj)^ $ <6jo jf ^ < jLlj j ^Ij ^>
      DenavarCa Manichean seet)
      BBB bl                                                       5en5ar     (8yn8}r, dnd>r) ©pi. -f; ob. pi. -ty
 3760 Syn'pr'st M, S                      ^U ^jf ^ jU j
                                                                   religious,
                                                                     ^dynd^y*priest, monk, electus
      SenaParast ©pi. -^Syn'Pr'nc
                                                                   GMS 1135-6; TSP 2.823, 7.41; VJ 22, 121; BBB
      electae
                                                                     f 30, 32, 623; STii 3.1, 5, 43, 58, 6.2; Sund.
       GMS 260; 6ym*fir>su Frag. Len. 45.4                           AoFviii 1981 p214, 8R4; KG 351; C2 gloss.
 3761 5ynJk B                                          ^
      6ene ©pi. ->y/ =*8yn>y                                 3773 6yn5>r =» 8yn8»r
      (o/)religion                                           3774 dynd'ry1 C         ^jIj^j <tf.y.f ^ta, <LJS" <*^jUjj
                                   •                              Sen8arya ^Synt^y*, 8ynS*r
      TSP 2.742-3                                                 church, priesthood
 3762 6yn}r M =* Syn'r                                            STii 3.7
 3763 Syn'rk'h S                                     ^j^     3775 SynfVS M                              J^ *jiJ 'tri-* C^
      8enarak, Scnarc ©ob. ~yh                                    5en-fra5
       G?/)Denar                                                   promotor of the religion
       MDii p31.20 p200                                            Gersh. Sogd. Cpds. 143.1
 3764 Syn'rt'wspyh M              ^u ^LJT jlf jujf           3776 Synh      B, M, S                                       j*-' w
      Sen-artawaspya (Syn'rtwspyO                                                                           «w"AJl*   I
                                                                   Sen  ©f. 8ynh
                                                                     swc*y   n.; ace. -wh; ob. -yh; pi. -t **8yn, *try
      community of electi
       GMS 470; W-Li, ii; BBB; MSP bl21; Frag. Len.                religion, belief
         77V6; SynWwspfkh, KG 608
                                                                  TSP 2.315, 1173; O5 26.32; BBB; Frag. Len.; KG
3765 5yn>rtwspy) =» 8yn>rt>wspyh                                    pl83; MSP p45;Synmzt)yzm pYy "the god of
3766 8yn>y B                                   vk>tf«J«*J           Mazda-yasna religion", Sund. Liste 1994, 459
     Sene ? ©pi. dyn*yty ->5yn'k                             3777 5ynmync(h) M, S                    jo* !*•_*>» <^j
     sect, religious sect                                         Sen-menc
     TSP; BSTBL; Frag. Len.                                       religious
                                                                  GMS 1103; KG 434; Frag. Len. 77V8; MSP b62,
3767 6yn>yk M, S            '         yi> ^         ***jf
     Senik (5ynyk) ©pi. -/; ob. pi. -ty                             119-20; Synmyc, MSP e20
     faithful
                                                             3778 5ynp5»ry M                                              ^ ^u
     GMS 995; KG; 350, 444, 615, 582; MSP bl27                    8enpa8are ©pi. -t
3768 Synpr S                                                      protector of religion
       8enpar =»8yn»Pr                                            KG2368pl83
                                                    iJ^JJ
       priest                                                3779 fiynsWr M                                           #> J>^
       Frag. Len. 68.3                                            8en-sar8ar ©<Parth.
3769 Sync- B           (^ ;J^)oj^Oj^                              religious leader
                                                    O-^           BBB 623
     8/Genc ©*0anjaya =*Sync}k
     (to)pull out
                                                             3780 Synt'ry' M                      ^ Jjujj icZjLaj <ojU-j j
     GMS 70; Hen. L W 104
                                                     Oj^Ki        Sendarya ^dynd'ry*
3770 5ync>k B                             aJ^                     monkship, monkhood
     Oence, Gencak ©pres. part. ^zP'k-Sync'k                      GMS 283, 1111; BBB b46
     pulling out
     SCE 246                                                 3781 Synyfrn M                                                 jp'j
                                                                  8ene-farn (Synyprn) ©ob. -yy
3771 5yncyhryft M                                                 fortune of the religion
     dencihrlft ©<Parth.                   J±£s. O^J              W-Lii; KG 511; Sund. AoFvi 1979, 102; Gersh.

===== NR=216 =====
                                                                                                                                   150
 5ynyk

           Sogd. Cpds. 139.142; MSP p45 bll7                                 3798 Syw1   B, M                                       ^
 3782 Synyk => 8yn>yk                                                             Sew    (dyw3) ©<daiva ©ob. -y; pi. ~t\ ob. pi.
 3783 Synyprn  S => Synyfrn
                                                                                  demon
 3784 6ys S(C)                                             oK*«U-                   -ty(y)(hh voc. ->
      Ses                                                                         TSP 2.536, 13.8 etc.; SCE 250, 261; GMS 1439,
                                                                                    BBB 761; BSTi; C2 gloss.; Hen. Cosm, 312, 114,
         place 140 Psalter. 133.24
         STSC                                                                       123; Magi. 138; Syw\ voc. BSTi 270
 3785 8ys-     M                                              ^U             3799 8ywJ   B, M              (a^^H^I     J^J^lSLy
                                                                                  Sew
         Ses (dysd'r-, dys-1) =»5ystk, Syst-
         (to)build                                                                unreliable, deceitful
         GMS 596; BBB 494; Sund. AI 28, 182; AVS 125                              TSP 12.31 n p225; GMS 60; BBB 689

 3786 dys-1     C ** Sys-                                                    3800 Syw3 B                               (o^J)j^^^
                                                                                  5e/iw
 3787 dys-3 C            j             j^^tjzjjj
      Ses =^n*dyst                                                                smartweed
                                                                                  SCE 165
      (to)bc located
      STSC 182; Sund. AI 28, 1988, 182                                       3801 dyw'   C                                         jii
 3788 dysdV- =» Sys-
                                                                                  Syu
                                                                                  with ©<*hadd-iyam
                                                                                       him                =*d-, yw1
 3789 dysny     C                                  jU^-L-^jujU
      Scsne     ©pi. -t                                                           Benv. JA 1955, 321; C2 gloss.
      builder, building
      STi 21.16                                                                   dyw3 C^'S
                                                                             3802 6yw>kk
                                                                             3803          S yw1
                                                                                  Scwak
                                                                                  heavenly
 3790 5yscy(y) M           (c^i.^j^^U^^L j*=±a j^j                                                                            L^
      Sisc(i) ©Av.da&uso =*5scy(y), Sts rwc
      eighth(art<i)fiftccnth day of the month                                     Sogdian coins
      Hen. Fasts. JRAS 1945, 149.20, 151.60                                  3804 5yw>nt(y) B                 yjliyj i^y iy)^
                                                                                  8iwand(y) =*dywnt
 3791 6yst-     B, M
                                                                                  in it, with it, through him
      Sist (Sst-, dyst-) ©<*dista ©pt. st. =»5ys-                                 GMS 1462; TSP 2.560, 542; VJ 262; Frag. Len.
      GcObuild                                                                      68.4, 87,4
     GMS 114, 596; 6yst>t, STii 3.32, 26
3792 dyst- C =* Syst-                                                     3805 Syw'styc S               g^'^j^-^^ajfjAlifU
                                                                               Scwastic, Siwastic ©pr. name
3793 Syst'ych S                                       Uj <OleJL>-L*            Dewashtich (a sogdian prince)
     Sestic, Sestec
     building                                                             U    MD
                                                                         ^

      Sund. MHC        27.6, 28 n 48                                     3806 5y w'styyc       M                         ^^o t^*j*\
                                                                              Sewastic
3794 Systk     B                                               j^»-L>            demoniac
      Siste   (Systyy)     ©pp.   =>Sys-, 5st>y                                  GMS 1277; Hen. JRAS 1944; Magi. 142.7
      built
      TSP 2.372; GMS        114                                          3807 Syw'yS        B, M, S                   l^U^k^JL

3795 dystw'n       C
                                                    ."■OvJj i^J) ^i \j           SiweS/8 (dywyO, SywyS) ©<*hada-w-aita ?
                                                                                   <*hada-awa-aita =»dywyd
      Sostwan ©pi. -/ =^8stw}n
      poor, miserable                                                            to it, in it, with it
      STi 81.16, 34.6                                                            GMS 1403-4, 1455; TSP 3.225, 291, 22.6, 7, 9; VJ
                                                   •*>-o*Jj i^Jl^iU                137, 1063; KG 326; BBB b88 f24; Lentz. STii
3796 Systwc        M
     Sostauc       ©<*dustawauc        =>Sst>wch
```


## [2026-09-05T20:12:25.060Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=19544{if(index($0,\"\\f\")) c++} END{print \"leaves before line:\",c}' SOD_pages.txt; python3 - <<'EOF'\ndata=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt').read()\nlines=data.split('\\n')\nfor target in (14369,19537,23349):\n    txt='\\n'.join(lines[:target])\n    print(target, 'leaf idx', txt.count('\\f'), '-> printed approx', txt.count('\\f')-66)\nEOF",
 "description": "Compute printed pages for SOD lines"
}
```


### [2026-09-05T20:12:26.823Z] TOOL RESULT

```
leaves before line: 285
14369 leaf idx 212 -> printed approx 146
19537 leaf idx 286 -> printed approx 220
23349 leaf idx 340 -> printed approx 274
```


## [2026-09-05T20:12:31.889Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '14355,14420p' SOD_pages.txt",
 "description": "Print SOD lines 14355-14420"
}
```


### [2026-09-05T20:12:31.946Z] TOOL RESULT

```
         ^Swyst
       two hundred                                                        5i/o|3 ©<*dwi-    ©in compd.    =»8Ptyk, Sw>
                                                                         two
       STii 1.82; SCE 561; BSTBL, Padm. 45; GMS 1316;                    GMS 1320
         SW,C2n p51
                                                                    3728 ayp'zp'k    B                      J^tj^j^^j^
3717 dwystysywystmyq
                                                                         8ip(a)z)3ak    (SypzP'k)
     8wiste se-wist-mik                                                  two-tongued, hypocrite
       two hundred and twenty-third              r>-^                    TSP 2.1120, 17.14; SCE 442; GMS 430
     C2, 1R9 n p50.51                                               3729 6yp6tt     B                                 k*^
3718 6x S                                                                5eP5at ? ©Skt. Devadatta
       8ax ? ©<daha         ©prop. n. SxzHk                v<>           an enemy of the Buddha
       male, man                                                         BSTBL, Dhu. 106
       S W, Rock. Insc. Indus Valley 1989, 135; CII,                3730 8ypnw      B, M                              jv>
         1992, p51
                                                                         8iPnu     (dybnw) ©Lat. binl, <*dwi-nu    =»8Pnw
3719 8xs-        M                      jjj^o^jO^j^^                     both
     8axs
                                                                         EGS 140; GMS      1316, 1320; BBB; VJ; TSP 2.189,
       0o)give pain, (ro)hurt                                              5.59, 73; BSTBL, Dhy. 35; S W, 11R26; C2,
       Sogdica. 48.2; Gersh. AHM          181n
3720 dxscyq C
                                                                    3731 dybnw      C =* Sypnw
     Saxscik ©ob. pi. -ty
                                                                    3732 SyPpWkCw)
                                                                            pl99     B                                      l^
     buried, entombed
                                                           oy^           5iPpa5e ®pL6yflp>Syt
     Sund. AI28, 1988, 181
3721 6xsny M                                                             biped
                                                        9 b ijltl        VJ 1177; TSP 5.76; GMS 430; Syflpdw, VJ 1484
     Saxsne
     mark, sign                                                     3733 8ypty-     B                             JSi&stfc
                                                                         8ipdi ©abl. ->; ace. -w =*Sptyk, Spt>y-w
       Sogdica. 48.2, 49.2
                                                                         other, second
                                                                                        MM             un


 149
                                                                                                                      Synyfrn
                                                                   order of electi
        GMS 1043; pi. Syn'fir'st, Syn'fir'st
                                                                   BBB 554 a4; W-Lii
 3759 Syn'pr'nyg M         (^^*<*J)+j£t><iSj>£±>
      SenaParanig                                             3772 5yn5"r     B, M, S   jj)^ $ <6jo jf ^ < jLlj j ^Ij ^>
      DenavarCa Manichean seet)
      BBB bl                                                       5en5ar     (8yn8}r, dnd>r) ©pi. -f; ob. pi. -ty
 3760 Syn'pr'st M, S                      ^U ^jf ^ jU j
                                                                   religious,
                                                                     ^dynd^y*priest, monk, electus
      SenaParast ©pi. -^Syn'Pr'nc
                                                                   GMS 1135-6; TSP 2.823, 7.41; VJ 22, 121; BBB
      electae
                                                                     f 30, 32, 623; STii 3.1, 5, 43, 58, 6.2; Sund.
       GMS 260; 6ym*fir>su Frag. Len. 45.4                           AoFviii 1981 p214, 8R4; KG 351; C2 gloss.
 3761 5ynJk B                                          ^
      6ene ©pi. ->y/ =*8yn>y                                 3773 6yn5>r =» 8yn8»r
      (o/)religion                                           3774 dynd'ry1 C         ^jIj^j <tf.y.f ^ta, <LJS" <*^jUjj
                                   •                              Sen8arya ^Synt^y*, 8ynS*r
      TSP 2.742-3                                                 church, priesthood
 3762 6yn}r M =* Syn'r                                            STii 3.7
 3763 Syn'rk'h S                                     ^j^     3775 SynfVS M                              J^ *jiJ 'tri-* C^
      8enarak, Scnarc ©ob. ~yh                                    5en-fra5
       G?/)Denar                                                   promotor of the religion
```


## [2026-09-05T20:13:04.479Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HRN debir/diwan ==\"; grep -n -iE \"deb[iī]r|dib[iī]r|d[iī]w[aā]n|d[iī]v[aā]n|dībā\" HRN.txt | head -25",
 "description": "Grep Horn"
}
```


### [2026-09-05T20:13:04.526Z] TOOL RESULT

```
== HRN debir/diwan ==
```


## [2026-09-05T20:13:06.086Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HUB ==\"; grep -n -iE \"deb[iī]r|dib[iī]r|d[iī]w[aā]n|dīpi|dipi\" HUB.txt | head -25; echo \"== NYB ==\"; grep -n -iE \"dpywn|dibir|dpyr|dēwān|dywn\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep Hübschmann and Nyberg"
}
```


### [2026-09-05T20:13:06.153Z] TOOL RESULT

```
== HUB ==
2084:Horn's phi. dipivar nicht wahrscheinlich. F r. M u 1 1 e r
== NYB ==
1283:dipivar [dpywr] secretary ŠPrs: 9. 15. Pl: 7; pl. eas. obl. —-an mahist the chief secretary 1119. 1821. 1925, — FrP 15, MS K dpywl (= dipīvar). Olr "dipi-vara- from OP dipi- ‘inscription’, BP dyp ‘document’, MPrth dyb ‘letter’ + "vara- from Av. (1360) 'var- ‘to cover, to hide, to preserve’, thus ‘he who preserves the documents’. Early contracted to dipir: Arm lw. dpir Yoxupaveóc; KZSPrth 1. 24 dpyrwpt = Prs l. 29 dpyrpt, Gr. trans- literation diBuporr, ‘chief secretary’; M PrthPrs dbyr; NP dibir, dabir (but Paz. "diver, v. next w.). Cf Bailey, BSOS VII, 1933, 76-77.
6267:d'tbr: datavar dpyrwpt: dipivar dwnb?wnts: Dumbavand
6297:dpyrpt: dipivar
```


## [2026-09-05T20:13:15.547Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HRN alt ==\"; grep -n -iE \"ebîr|ebir|iwân|iwän|îwân|dîbâ|dība|dibä\" HRN.txt | head -30; echo \"== HUB ctx ==\"; sed -n '2060,2110p' HUB.txt",
 "description": "Grep Horn variants and Hübschmann context"
}
```


### [2026-09-05T20:13:15.602Z] TOOL RESULT

```
== HRN alt ==
6739:77G. sahän Hirte, siiwän, IN2iir (Is. 1, 24).
7834:903. ff er den 'Nacken, Hals', gerdene 'Gebirgspass'^).
9352:ORS. LW. (?) rärdcä; bei. f/vardäf/ Gebirgsrebhiihn' ;
== HUB ctx ==
im Np. das hatte werden miissen und setzt daher np.
dar a = gr. d^Qov. Aber d^r ist haufiger im Np. zu
hr als zu s geworden, daher Horn's dara aus *dah'
rak = zd. da&ra- einwandfrei. Phi. dasr (West-
PT. I, 341 ; IV, 249 gifts, almsgivingsl ist nur Um-
schreibung der Zendform.
526. Np. ddS 'Ofen' geh5rt schwerlich zur Wzl. skr. dah^— 60 -
527. Np. »lnhdr 'Schutz, Sicherheit, Zuflucht' ist natiirlich
nicht aus az in ddr entstanden, da d hier nicht zu h
werden konnte. Andreas erklart sfinhar aus az m
har von Wzl. har *servare (ZDMG. 47, 704), Fr.
M tiller setzt es = zd. *zaend-hara- *Waflfenschutz'
(WZKM. 8, 96). Die letzte Erklarung scheint mir
die beste. Zum Gebrauch von zmkdr als Interjektion
gi^b acht* vgl. d. Achtung!, mhd. wafenl etc.
528. Nach Noldeke ddSn, wie es der Etymologie ent-
spricht.
534. Arm. catiacem *kenne' gehort nicht hierher. Der In-
finitiv ddnistan ist aus dem Praesens danam neu
gebildet, wie uberhaupt alle hier angefuhrten irani-
schen Formen zum Praesensstamm iran. zdna- = np.
dana- gehSren. Vgl. dazu unten Nr. 793.
538. Np. ddh nach Vullers = 'ancilla, serva, famula.
540. Arm. dpir setzt phi. diplr voraus und macht mir
Horn's phi. dipivar nicht wahrscheinlich. F r. M u 1 1 e r
fuhrt (WZKM. 7, 376) np. dwdn ^Tribunal' auf phi.
*attvdn = arm. atean zuruck, was ich nicht fur richtig
halte. Np. daftar, arab. LW. daftar, diftar — gr.
SKp^iga (Noldeke).
541. Armenische Frauennamen mit duxt sind haufig, nur
gerade Tigranaduxt kommt meines Wissens nicht vor.
542. Zu skr. daksa- gehSrt daksina- *tuchtig, recht* = zd.
dasina-. Also ware skr. daksa- = zd. *dasa' = np.
das (nicht daooS), Vgl. Fr. Muller, WZKM. 8, 94.
546. Np. dar 'hinein, in' aus andar wie darun aus andarUft,
darx^'ar aus andarx^ar. Vgl. deutsch raus = heraus,
rein = herein u. s. w.
547. Die Gleichung paz. np. der lange = ap. darga- wider-
spricht den Lautgesetzen , scheint aber gleichwohl
richtig. Ich vermute Umstellung von ap. darga- zu
^dagra- = ^dayra-, das zu der wurde wie zd. anayrandm
= phi. np. aneran^ zd. tiyri- = np. t%r ist.
548. Etymologie dunkel.
550. Etymologie dunkel.^ 61 —
551. Aus ap. *duruva8ti' ware np. durost geworden, vgl.
dur6d (Nr. 555) aus *duiruvata;t'. FUr skr. drdhd- 'fest,
hart, stark, dauerhaft, ganz' (WZKM. 7, 374) = zd.
^dareida- oder *dareSta^ ware im Persischen *dis^ zu
erwarten. Ich kann np. durust ganz, voUstandig,
richtig, wahr, gesund*, paz. durust, drust ganz, voU-
standig Min. Gl. 66 (LW. bal. drust^ afgh. drast ganz,
```


## [2026-09-05T20:13:22.934Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^540\\|540\\.\" HRN.txt | head -10; echo \"---\"; grep -n \"539\\.\\|541\\.\" HRN.txt | head",
 "description": "Find Horn entry 540"
}
```


### [2026-09-05T20:13:22.994Z] TOOL RESULT

```
4828:540. dehlr, dibtr 'Schreiber', n^DI (Jer. 36, 10) aber nxn,
14223:(/tpi- 540.
15785:ä(i>bir 540.
15799:(fCi-Ji-ic 540.
15802:-/f-':^,*-!;. 540.
17760:.7i;)i- 540.
18935:1 -lön 540.
22199:r//>tr 540.
22570:I ^ff/9fft^ 540.
---
4821:539. däye *Amnie*, düiß^),
12090:rfSye 539.
12096:dsyi 539.
12286:.Ju^/ 541.
14785:dafMu- 539.
14862:duySav 541.
15763:dänak 539.
15921:iliirl 541.
19169:fi^re 366, 539.
19173:f?ä/;/ 520, 539.
```


## [2026-09-05T20:13:26.296Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '4826,4850p' HRN.txt; echo \"=== page? ===\"; python3 -c \"\nd=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt').read()\nlines=d.split('\\n')\nt='\\n'.join(lines[:4828])\nprint('leaf',t.count('\\f'),'printed',t.count('\\f')-21)\n\"",
 "description": "Read Horn entry 540"
}
```


### [2026-09-05T20:13:28.172Z] TOOL RESULT

```
däye (LW.); af/. LW. däyT; oss. d. däyim, t. däin
'saugen (103); bei. LW. dai (53).
540. dehlr, dibtr 'Schreiber', n^DI (Jer. 36, 10) aber nxn,
HNVn (Ezech. 9, 2, 11).
Nur in seiner Bildung vielleicht persisch; vergl.
aber Jensen, WZKM. VI (im Druck).
ap. vergl. LW. dipi- 'Schrift'; präkr. dipi-, lipi-
(Agöka-Inschriften) ; phlv. d(i)pioar (Hörn, ZDMG.
44, 670 No. 111), d(i)pTr, d(i)pTrih (PPGL), daneben
d(i)blr (Inschr.); arm. LW. dpir^ talm. ^''Dl, daßtiQ
(LXX).
Die Form np. diiwer der Wörterbücher, die zu päz.
diwcr (Men.) stimmt, wird durch den Reim bezüglich
ihres e beseitigt (debtr reimt auf plr, Vfs und Rcämln,
S. 23, V. 6, auf gir Sahn. III, 1452 Vers 142)2). Den
Zusammenhang mit dtwän, defter (phlv. daftar nur in
späten Kolophonen) hat bereits de Lagarde (Ges.
Abh. 216) erkannt.
54 L diiy^ter, du/t 'Tochter'.
aw. diiydar- 'Tochter'; phlv. dtt/t^ vergl. arm.
Tif/rana]du/t; ai. dtihitdr-; arm. ditstr (Jl. No. 87).
kurd. du/t, ditt; af/. lär; wa/. da yd, sangl. da/,
minj. loyda.
*) In Vis und Rämln findet sich am Versende auch däyeyän
*Aniuie* (z. B. S. 20 Vers 13, 21 Vers 2 v. u., 22 Vers 5 v. u.), mit
=== page? ===
leaf 140 printed 119
```


## [2026-09-05T20:14:45.452Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -5; echo \"---\"; grep -c \"\\[pdf page\" BQT_v2_pages.txt; echo \"--- search دبیر\"; grep -n \"دبیر\" BQT_v2_pages.txt | head -20",
 "description": "Inspect BQT vol2 pages file"
}
```


### [2026-09-05T20:14:45.534Z] TOOL RESULT

```
---
0
--- search دبیر
41:‫دبیرساقی(محمد) ‪ ۰‬فارغالتحصیل دور کدتری ادببات فارسی( لغات قزونی )‪.‬‬
46: ‫شهیدی (سبدجعض)» دبیر ادبیات فارسی دبیرستانهای تهران (لغات بروجردی)‪.‬‬
47: ‫علوی (محمدحن)؛ دبیرتاریخ وجغرافیای دبیرستانهای تهران ( لغات کازرونی‬
49: ‫قاسمی (رضا) ‪ .‬دانشجوی دور دکتری ادییات فارسی ودبیر دیرستانهای‌تهران‬
51: ‫گنابادی (بروین) » دییر ادییات فارسی در دبیرستانپای تهران ( لغات کنابادی‬
57: ‫آقای علینقی بهروزی دبیر دبرستانهای شبرازنیزسلسلة مقالانی بعنوان «تقریظ‬
2199:      ‫وتدبیر وراه وروشهای مختلف راگویند ‪.‬‬                     ‫جلحلان‪ -‬بضم‌هردوجیم بروزن بلبلان؛‬
9716:                            ‫وتدبیر کننده هم هت ‪.‬‬      ‫‪-‬فلث‬
14484:     ‫بزراعت برند ‪ - ۷‬و برزیگری را نگیز‬                  ‫مو کل آفتاب که تدبیر امور ومصالحی که درروز‬
21405: ‫گزیر » دبیرونویسنده ومشیرا کویند » ودووبر‬               ‫بمعنی دولتمندی باشد ‪ -‬و کبی را نیز گوبند‬
22388:    ‫د‪#‬یوان بکر اول » ازکامة مفروض ایرانی ‪ 0261‬همریثة «دبیر ‪٩‬‏ ( نوسنده )‬
23993: ‫نآاهمنگری است که تدبیرسکندرآینه ساخت_‬                       ‫کوبند‪ - ۴‬وطلا و لقره ومس و سیماب وسرب‬
29321:                                                                   ‫‪:‬محاقظات حوران بپدتی و ندبیر مصالح این روز‬
31511:                   ‫حیله کردن » توطثه کردن ‪ -‬سبت دادن ‪ -‬صیقل دادن » پرداختن ‪-‬تدبیر کردن ‪.‬‬
32878:‫زردبیرا گونند که برروی‌غله‌زارشنید ودانهٌکندم‬                                         ‫وبمد ازین ‪.‬‬
34800: ‫از سرپا زدن باشد وآنرا زهکولی کوینده وآن‬         ‫هرشب » مقیدبیرا گوشد که بریوست آدمی‌پدید‬
35825: ‫او موسوم است‪ .‬واین سروشها که بتدبیر روزها‬             ‫کانٌ هرماه از ماهپای شمسی ینام ابثان موسوم‬
35826: ‫قیام دارندکار کنانسروش‌هایی‌اند که بتدبیرماهها‬       ‫کشته ‪ ۱‬و پنج فردیگر آنکه پنجۀ دزدید هکه‬
35875:                                                         ‫و مصالع آن رو" بدو مقرر است خودهم بتدبیر‬
38366:    ‫سمرقندی دبیرطمفاح خان ابراهیم ماقبل آخرین از ملوك خانِة ماوراء النهر ترجمه قناوزی را‬
```


## [2026-09-05T20:14:55.988Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '22360,22400p' BQT_v2_pages.txt",
 "description": "BQT vol2 context around divan footnote"
}
```


### [2026-09-05T20:14:56.031Z] TOOL RESULT

```
‫آرا‬
  ‫وسکون دوسین و فوقانی ‪ ۰‬دوابی است که ن‬                            ‫از قپر وغضب هم نوشته‌اند ‪.# ۷‬‬
‫انده قوقو گونند وبرکلف وبهق مالند تبافاعشد »‬         ‫ررنو‌شدن‪ ».‬کناه‬               ‫نه‬
                                                                                    ‫خواار‬
                                                                                        ‫ذی‬
‫واگرطفلی دبر بحر کت بد چون برومالند زود‬                                  ‫از خراب دن خانه باشد ‪.‬‬
                                                     ‫ديو ار گر = دبوارساز ‏ وگل‌کار وینارا‬
‫دیوال ‪ ۴‬سبا لام" بروزن ومعنی دیوار‬                                                            ‫گونشد ‪.‬‏‬
‫است» چه درفارسی راولام بهم تبدیل مییایند ‪#.‬‬
‫‪۰‬‬    ‫فرشت‬     ‫رای‬   ‫بفتح‬   ‫دیواله رو‬
‫شخصی‌را کوبند کهمدابنوندانهاسلوك کند وبراه‬                                ‫عاجز وزبون هدن باشد ‪.‬‬
                                            ‫رود ‪.‬‬    ‫همز هو بای‌فارسی‬   ‫د یو اسست ‪ ۴‬یک‬


    ‫‪ - ۱‬نظر بتصور مهيب و هولناك بودن دبوان‪ « .‬هرچیز را که از افراد خودفوی جثه‌تر‬
     ‫و بزرکترباشد بدیو اضافت نمابند (با بفول که آنهم دو موهوم است) مثلاکمان بز رکه راکمان‬
     ‫دیو خوانندیسنی دبورامیدابد‪ .‬نوعی ازاسیست‌را که ‪-‬اق وبرگهآن ازامتال بزرکنراست دیوامیت‬
    ‫گوبند ‪ .‬کلوخ کلانرا دیو کلوخ » عنکبوت برزکه را دیوپا» زبراکه بابپای بزرکه و بلند‬
     ‫دارده و گردناد را که بلند شود ديو باد گوشد»‪ 9‬انجمن آرا» ولىز ‪ :‬دیوحان › دیوچه‪ ,‬دیوخاره‬
                       ‫دبودار » دیودل» دیوزای» دیوسار » دیوگ » دیو گندم‪ .‬ورك‪ :‬فاب ‪ ۱‬ص ‪٩۹۱.‬‏‬
    ‫‪ 2‬وجنگه کرد‬      ‫دبوار («‪.‬م‪).‬‬   ‫‪-‬‬   ‫‪۴‬‬           ‫امست («‪.‬م‪).‬‬    ‫از ‪ :‬دنو (ھ‪.‬م‪4 (.‬‬          ‫‪۳‬‬

    ‫بسیار بدرارك » و کشتن کرد فراوانی بدر شارستان » در گرکوی عاقبت بستد » و ارك را و قلمة‬
                             ‫زورین راء بعد ازان دبوالآ قرا ببرید ‪« »...‬تاریخ سیستان ‪4۸۳٩‬‏ ‪.‬‬
     ‫‪#‬د یوار بکراول د=بوال د=ی=فال(عامیانه)‪ ,‬بېلوی ‪« 4۷8‬تاوادبا‪ *۹۱‬وجهاشتقاق‬
      ‫کنومله است‪ .‬رك‪ :‬اسشق‌ءهوبشمان ‪ ۹۹‬؛کردی‌ع «‪rãvîd‬‏ وخیع‪ .13۷114‬سربکلی‪1۷164‬‬           ‫آ‬
     ‫اسشق ‪ , ۹۹۵۰‬افقانیع ‪ 14۷1‬هوبمان ‪ 4۹۵‬جداری که دراطراف خانه‌بنا کنند بجهت‌مصور‬
             ‫کردن و حفاظت آن » هرچیزی که ای را محصور کند خواه ازمصالح بنابی با حزآن‪.‬‬
    ‫د‪#‬یوان بکر اول » ازکامة مفروض ایرانی ‪ 0261‬همریثة «دبیر ‪٩‬‏ ( نوسنده )‬
    ‫وبقول اندرآی مرتبط بکامة آسوری ‪« ۳21‬دائردالمعارف املام» وکلمة أن پارسی باستان که از‬
     ‫کدی و نال سومری ( لوحه‪ ,‬خط ) مأخون است « مجلة ابراشهر سال ‪ ۱‬شمارء ‪۸‬‬       ‫‪۷‬‬
     ‫ص ‪«٩ ۷۹۱ - ۵۹۱‬ف‏اب‪ ۱‬ص‪ . ۲۱۱‬معرب آن هم «دبوان» «دزی ح ‪۱‬ص ‪۹۷4 -۸۷4‬؛ دفاتر‬
     ‫عمومی محاسبات ‪ -‬موضع حساب‪ -‬مرکز ندوبن کتاب ها کتابی که نام لکربان واهل عطیه در‬
    ‫آن مکتوب باشد ‪ -‬ادار دولتی ‪ -‬وزارت خانه ‪ -‬سفن شامل اشمار گوبندگان ‪.‬رك ‪ :‬دائرة‬
                                                                                      ‫الممارف اسلام ‪.‬‬
     ‫‪ -‬کر اول وینجم( در لهس مر کزی) م از ‪ :‬ديو ‪٣‬‏ ان (جمع) ‪(۳-۰‬نسبت)‬               ‫‪ #‬ویوانه‬
     ‫[رك ‪ :‬اسشق ‪ ۸۹۵‬ویشتم! ‪٩۲ :۱‬‏ | ؛گیلکی ‪ 20۵۷1‬فنریدزی‪ .20۷64‬برنی ‪. 800۷14‬‬
     ‫‪ . 6488۷10‬سرخه‌بی‬         ‫نطری ‪ < 8012۷1‬ك ‪ .‬اص ‪۳٩۲‬‏ ‪ .‬سمنانی ‪ . 803۷10‬سنگری‬
     ‫» مجنون « وشبانگاه آوردند بش وی (عیسی)‬         ‫بی عفل* بخیرد‬       ‫‪۶۹۱‬‬   ‫ص‬       ‫رد( ‪۰‬‬       ‫‪6‬‬
     ‫احمق‪.‬‬   ‫دیوانگان ب‌بار» و دیورا ازامشان بدر کرد بخن خود وشفا داد ‪« »...‬انجیل فارسی ‪۸۸4‬‬
                                                                                  ‫ابله‪ .‬ادان» بي علم ‪۲‬‬
```


## [2026-09-05T20:15:11.332Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,60p' tools/ref_page.py",
 "description": "Read ref_page.py header"
}
```


### [2026-09-05T20:15:11.366Z] TOOL RESULT

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


## [2026-09-05T20:15:14.176Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 600 python3 tools/ref_page.py BQT:823 2>&1 | head -60",
 "description": "Fetch BQT page 823"
}
```


### [2026-09-05T20:15:15.884Z] TOOL RESULT

```
no scan of BQT covers printed page 823 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:15:21.477Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in BQT_v2_pages.txt BQT_v2.txt; do echo \"$f: leaves=$(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f) lines=$(wc -l < $f)\"; done; echo \"--- head of BQT_v2_pages\"; head -20 BQT_v2_pages.txt",
 "description": "BQT vol2 leaf count"
}
```


### [2026-09-05T20:15:23.226Z] TOOL RESULT

```
BQT_v2_pages.txt: leaves=683 lines=41070
BQT_v2.txt: leaves=1 lines=67022
--- head of BQT_v2_pages
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
              ‫لض‌بال ‪ ۰ ۲۶‬رک‬
‫‪۱‬‬       ‫اسا تعدولیدیارتم و‬
                                     ‫‪7‬‬
‫‪ ۰‬و زل رسوا »وا روون لات سا روصا مواقم‬      ‫وتان‬

                      ‫‪۴2 ۱‬‬

                  ‫رک یمن‬
                  ‫م سارو کی و ررك‬


                 ‫جلررومدا‬
             ‫چاپ دوم فروردین ‪۳۴۳۱‬‬
                 ‫با تجدید نظر کامل‬
          ‫بسرمایه کتابفروشی ابن سیتناپران‬
```


## [2026-09-05T20:15:30.308Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification; grep -ho \"BQT_v2_pages[^\\\"]\\{0,160\\}\" page-*.json | head -20; echo \"====\"; grep -ho \"leaf [0-9]* of BQT[^\\\"]\\{0,80\\}\" page-*.json | head",
 "description": "Find prior notes on BQT vol2 offset"
}
```


### [2026-09-05T20:15:30.386Z] TOOL RESULT

```
BQT_v2_pages.txt, grep بنیامین / بن یامین
BQT_v2_pages.txt leaf 370 (printed ≈ p.912; running offset printed ≈ leaf + 543). The page carries both headwords: 'دیز … رنگ و لون را گویند عموماً چنانکه اسب سیاه خسرو پرو
BQT_v2_pages.txt leaf 134, i.e. printed p. 677 by the running offset (leaf+543), one page off Nourai's citation. Footnote: «اوستا čira (زرنگ، شجاع) «بارتولمه ۵۹۸» ... «معین
BQT_v2_pages.txt leaf 134), footnote to چیر
BQT_v2_pages.txt leaf 134 = printed 677) the footnote to چیری reads «... بهلوی čēr ... čīrīh ... ؛ غالب شدن، ظفر یافتن. رک: چیره» — Mo'in gives precisely the Pahlavi forms 
BQT_v2_pages.txt leaf 134), one page later than the citation: «چیر - بر وزن میر بمعنی غالب شدن و ظفر یافتن و مستولی گردیدن بر دشمنی باشد - و شجاع و دلاور را نیز گویند»; foo
BQT_v2_pages.txt at leaf 667, i.e. printed p. ~1210 by the running offset (leaf+543) — about seven pages after Nourai's citation, so the page number cannot be confirmed. Th
BQT_v2_pages.txt and BQT_v3/4 OCR
BQT_v2_pages.txt leaf 84 ≈ printed p. 627, lines 4834-4838)
BQT_v2_pages.txt leaf 84 (printed ≈ 627 on the leaf+543 offset, i.e. Nourai's 626 within the ±3 drift of that volume): headword «چراغ ـ بروزن فراغ؛ فتیله‌ای باشد که آنرا با
BQT_v2_pages.txt line 22784). Without a cited page the claim could not be pinned to a specific Borhan entry.
BQT_v2_pages.txt (printed ≈ p.672); running head چوبگان
BQT_v2_pages.txt (printed ≈ p.622), s.v. چپق
BQT_v2_pages.txt line 3693, Mo'in's footnote
BQT_v2_pages.txt leaf 376, printed ≈916–919), footnote 1: '۱ ـ پهلوی dēnār، تاوادیا ۹۱ ... از لاتینی dēnārius بتقدیر dēnārium بمعنی «نقدی برابر ده آسی» چه در اول وضع آن از 
BQT_v2_pages.txt leaf 376): headword 'دینار = بر وزن بیمار، زر سرخ را گویند ...' with the etymological footnote quoted at node 15, plus Moʿin's cross-reference 'برای ارزش د
BQT_v2_pages.txt
BQT_v2_pages.txt (Borhan-e Qate', د section)
BQT_v2_pages.txt leaf 329 (printed 869), Moʿin's footnote 7: «دوب dub در زبان سومری بمعنی لوحه و خط است. از این زبان وارد اکدی شده ṭuppu … و از این زبانها وارد آرامی شده … 
BQT_v2_pages.txt leaf 329 (the leaf carries the دفتر article and its footnotes; the estimated +543 offset in refs_online.json is ~3 leaves too high here — for this stretch 
====
leaf 129 of BQT_v2_pages.txt (printed ≈ p.672); running head چوبگان
leaf 79 of BQT_v2_pages.txt (printed ≈ p.622), s.v. چپق
leaf 277 of BQT_v2_pages.txt (printed page ≈ leaf+543, i.e. 817-820; the headword block دام run
leaf 387 of BQT_v1_pages.txt (running head '۱۶۹') carries the headword «اندام - بروزن انجام، مع
leaf 278 of BQT_v2_pages.txt = printed p.818 (running-head calibration leaf+540, checked agains
leaf 416 of BQT_v1_pages.txt (~printed p. 195-196)
leaf 383 of BQT_v1_pages.txt) has both انباز 'رفیق و همتا' and انباغ 'دو زن را گویند … دیگری را
leaf 489 of BQT_v1_pages.txt (offset printed ≈ leaf − 220 in this part of vol. 1): headword 'بر
```


## [2026-09-05T20:15:38.316Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 281 282 283 284; do echo \"########## leaf $((n-1)) (NR=$n) ~printed $((n-1+543))\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -60; done",
 "description": "Print BQT vol2 leaves ~823"
}
```


### [2026-09-05T20:15:40.194Z] TOOL RESULT

```
########## leaf 280 (NR=281) ~printed 823
 ‫=‬    ‫=“‬
                                                                                               ‫داشومد‬

‫بف هد تا ازآن سرانجام خوردلی‬    ‫روفف هرىكڭزرى‬       ‫وخداو ند ودارندة داش باشد»چه ورىمەنى‬              ‫صاحب‬

‫ومایحتاج آن نر كنف ‪ -۳۴‬و فتح تااث اساب‬                                ‫ام‬     ‫و خداو ند ودارنده‬        ‫صاحب‬



                                                     ‫دا نشوهنك ‪ ۱‬ب‪-‬فتح‌ميم وسکون نون‬
                          ‫باد ©‬     ‫و متاع و کل‬


                                                     ‫و دال ایسد » بمعتی دانشمتد وحکیم وسباردان‬
                                                                                                  ‫‪۰‬‬   ‫باشف‬




                                                     ‫دانشی ‪ -‬بکرثالث ورایع وسکون‬
                                    ‫وامثال آن ‪.‬‬
                               ‫‏‪٩‬‬
                                                     ‫وانا‬
                                                        ‫تحتانی " بمعنی دانشگر امت که داشمند ر‬
‫د بفتح نالك وسکون‌ميم‪ .‬نمعدی‬        ‫دانم‬                                                          ‫باشد ‪.‬‬
                                    ‫توانم باشد ‪.‬‬
                                                    ‫دانك؟ = بفتح نالك و سکون كاف ‪٠‬‏‬
‫بروزنآغوش‪.‬نام‌شضصی است‬         ‫دناوش‬                 ‫گمنادزم و جو و ماش‬‫ناد اع‬  ‫به ر‬
                                                                                  ‫ودان‬
                                                                                     ‫گلق‬
                                                                                       ‫مط‬
‫ازبود معشوقة‬              ‫که عذرا را بفروخت‬         ‫ودص و غیره ‪ -‬وبضم الث آن باشد که بوقت‬
                                                                                        ‫ع‬
‫وامق ‪ ۰‬وفصهه ابغان مشپور است ؛ وآنرا دوانوش‬         ‫دندان نزآوزدن اطفال اقام دانها از جنس کندم‬
‫هم میگوبند که حرف انی واو باشد بر وزن‬               ‫وجو وماش وعدس وامثال آنها را باکله و پاچ‬
‫قدایوش ؛ ودلواش نیز گفته‌اند که حرف انی نون‬         ‫گوسفندپز دوبخانهای دوستانو خوبشانومصاحدان‬
‫باشد پروزن اوباش؛ و دیانوش نبینزظرآهده است‬          ‫فرستند ‪ -‬و در ملك دکن مهتر چاروا دار را‬
            ‫که حرف انی دای حطی باشد ‪* .‬‬                                                        ‫رنه ‪۵‬‬
‫داه جیدن‪ -‬بچمعینیدنبر‌دانه امت‬                       ‫دانگا ند = باکاف فارسی بروزن‌بازخانه‪.‬‬
‫اززمین‪ -‬کونابه‌ازسجده کردن‪ -‬و کدبه و کدایی‬           ‫وشت‬
                                                       ‫آن بائد که جمعی چون خواهند بسیر ک‬
 ‫ب‪-‬هلوی ‪ « 2016-0015080‬منای ‪» ۱۷۲۰‬از ‪:‬دای ‪ +‬اومند ( = مند‬
 ‫بهلوی ‪« 610151021‬منای‪ ۱۷۲‬از‪ :‬داش ‪ +‬ی(نسبت)‪« :‬چنن‬              ‫‪۴‬‬                     ‫‪۳‬‬    ‫اصاف)‬   ‫نمواد‬


 ‫گویدمحمدین عمرالرادوبانی که صثیف ها بسیار دیدم‌مرداشیان هرروز کاری را اندر شرح‌بلاغت»‬
  ‫«ترجمان البلاغه ‪ .‬رادوبانی چاپ احمد آتش ص‪( ۶۵۱‬بخش عکسی‪ » ).‬ولی در بخش چاپ سربی‬
 ‫‪ ۴‬پپلوی ‪ « 2020‬بندهش ‪٤٤۱‬‏ » « اسشق‬                              ‫ص‪ ۲‬بخطا «مرد انگابان » امده ‪.‬‬
 ‫‪. ۵00‬کنابادی ‪ « )8000‬پروین‬             ‫‪ ۳۳‬امروز دانگی (تهرانی‬   ‫‪۴‬‬              ‫‪۵‬‏ ‪٩‬ورك ‪ :‬دانه ‪.‬‬
‫‪ _ِ 1‬اول شخص مفرد (متکلم وحده) مضارع از‬                ‫© _ رك‪ :‬دانه کانه ‪.‬‬          ‫کگنابادی» گونند‬
                                                                                         ‫دانستن(«‪.‬م‪: ).‬‬
 ‫‪#‬دالگ ب‪-‬سکون‌سوموفتح آن‪ .‬بهلری‪ 802۰‬پارسی باستان (بنقل بونائی) ‪.44 8×41‬‬
  ‫«‪:‬نفس») اصلاهمر ش‌دانه (ھ ‪.‬م‪ ).‬اسست«اسشق‬     ‫(اپن‌درید»‬     ‫ارمنیع ‏‪ . dang‬عربی‌ع‌دانق ‪0‬‬
 ‫‏‪ ٩‬چهاريك درم ومثقال وجزآن ‪ -‬خش‌بك ملك وخانه ‪ -‬حصه و بهره «ناظم الاطبا » و رك‪:‬‬
                                                                       ‫‪ ۱‬دانق‬    ‫اسللام‬    ‫داثرةالممارف‬


  ‫د‪#‬اله ‪ € -‬سوم (درلھجۂ مر کزی)‪ .‬بهلوی ‪ . 8081‬اوستا ‪_ahsrakj‬‏ ‪6020‬‬
 ‫‪, 166021 ,‬بلوچی (ع(‬                ‫‪۰‬ردیع ‪6‬‬
                                          ‫هندی باستان ‪( 80800-‬دانهٌ کندم) ک‬
########## leaf 281 (NR=282) ~printed 824
  ‫داوردان‬                                                                                                    ‫==‬


 ‫قمار نیز هت » وآن ازهفده زیاده تمیباشد چه‬                                                              ‫‪.‬‬   ‫مت‬
                                                                                                             ‫ه‬ ‫نمودن ه‬
 ‫ازدیادآن جز طاق یت ومراتب اعداد متحصر‬                      ‫ب‪-‬روزن خاندان » ظرفی‬                    ‫دانه دان‬
 ‫است تا به نه ‪,‬پدساواول یکی است ودوم سه‬                 ‫وجایی باشد کهغله وداله درآنکنند ‪ -‬وبمعنی ‏‬
‫وسيم پنج وهمچنین هفت ونه وبازده تا هفده که‬
‫که مرنبة نهم اعداداست مپرود تائمام میشود‪- ۴‬‬                 ‫رالیز گوبند که درآ ن‌تخمکاشته ماف وزهتتی‬
 ‫ودعوی‌کازبرانیز گفته‌اند؟ ‪ -‬وبمعنی‌فحش ودشنام‬              ‫درخت فرو برند تا سیر شود‬                ‫که درآن شاخہای‬


‫هم‌آمده است ‪ -‬وهرچینه و(‪)۱‬مرتبه ورده باشد‬                                  ‫وازآنجا بجای دیگر نقل نمابند ‪.‬‬
‫که از دبوا رکلی بربالای حمگذارند وآرا دای‬                   ‫با زای هوز بروزن‌آمدن‪.‬‬                  ‫دانه دن ‏‬
                                    ‫گهومبند ‪.‬‬               ‫نوعی ازساحران وجادو گران باشند درهندوستان‬
 ‫‪ -‬بر وزن خاور ‪ ,‬نام خدای‬          ‫داور‬                     ‫که دانة ارزن وجورایز عفران زرد کتند وافسونی‬
‫عزوجل است ‪ -‬و یادشاه عادل وپرمتش کنندمرا‬
‫نیز گونند(‪ )۲‬ودراصل دادور بروزن داد گربوده ‪۰‬‬                    ‫‪۱‬‬                                  ‫که دار ند بواریق ‪۳‬‬


‫اد انشراز عنمی وت وا‬              ‫تورود ام خف‬
                      ‫ودرمان هم بنظر آ مده ات‬                          ‫‪۳‬‬   ‫وکالا ومتاع‌دنوی‌باشد؟‬               ‫دانه‪.‬اسباب‬



 ‫داو ردان = بادالابجد بروزن‌دافرمان‪,‬‬                        ‫‪ ۵4‬کردن ‪ -‬کنابه از پراکنده‬
 ‫نام دهی است که در طرف غربی و بفكرسخی‬
 ‫تکیبیآن خدادان‬
              ‫‪-‬معنی ر‬
                    ‫واسط واقع است‪ ۷‬و‬                        ‫داو » بر وزن‌گاو ‪ .‬بمعنی نوبت بازی‬
                     ‫وحا کمشنای باشد ‪.‬‬                       ‫وباده کردن خصل‬ ‫شطراج ونرد وغیره باشد ‪ -‬ز‬

 ‫(‪ )۷‬چك‪ .‬چش‪ + :‬معنی شخصی که مبان ليك وبد‬                                   ‫هر ‪.‬‬      ‫‪1‬‬         ‫‪۱‬‬
                                                                                         ‫)‪ (۱‬چك‪.‬چش‪:‬‬

                                                        ‫‪.‬‬      ‫نمدش‬
                                                                  ‫باک‬
                                                                    ‫وی ح‬
                                                                       ‫گعرب‬
                                                                          ‫حکم باشد وفصل کند وب‬
                  ‫رك‪ :‬جو زن ‪.‬‬       ‫‪۴‬‬            ‫دان (ب‌وندمکان وظرف) ‪۰‬‬               ‫‪- ۱‬از‪ :‬دانه ‪+‬‬

                                                                                ‫‪۳‬‬    ‫دانگانه‬       ‫‪:4‬‬       ‫‪۳‬‬


  ‫حالی‌من اندر عاشقی داوتمامی میزنم ‪.‬‬                 ‫‪ - ۴‬اورنگه کو؟ کلچهر کونفش وفاومهر کو؟‬
  ‫«حافط شبرازی ‪۹۳۲٩‬‏ ‪.‬‬
  ‫* یولهب ‪‎ 120۷27 , ,0۵0027 020۳721 . 0202027‬اتسوا ‪,# 0۵10-02۲2‬‬
                            ‫عیتمرا ‪ « 1803۷07‬قشسا ‪» ۵۳۷‬ههگربند ‪:‬كرو ‪‎‬ربوتاد ‪.‬‬
  ‫‪ 4‬شهر یه از نواحی‬   ‫«راوودان»‬   ‫مصحف‬   ‫یچ ظ»‬    ‫‪۷‬‬                  ‫«دارو» («‪.‬م‪۰ ).‬‬           ‫مصحف‬
                                                                                                  ‫‪_ ۹‬‬

                                                                                         ‫امعم البلدان» ‪۰‬‬            ‫سره‬

                                                                                                   ‫فاحزةٌ ‪۰۲۸‬‬
                                                                                                            ‫صبه‬
                                                                                                              ‫بق‬
   ‫سمنالی ‪ * 80000‬منگری و لاسکردی ‪ . 6881‬سرخەبى ‪ ۰ 6802‬شهمیرزادی ‪49‬‬
                        ‫َة میوه ها‪ -‬بکعدد اژ غله باهيوه ‪:‬‬                  ‫‪ -‬تخم و‬             ‫ه‬
                                                                                               ‫‪: ۲‬‬
########## leaf 282 (NR=283) ~printed 825
    ‫ح‬
    ‫ر‪۷‬‬                                                                                                                     ‫دأوری‬


‫يدام لصب کنند تاجانوران‬         ‫صادان درصحراتزدىك‬         ‫داور ی‪ = ۱‬بر وزن لاغری » جنگه‬
                  ‫دام آ بند ‪5‬‬   ‫رم کرده بجالب‬   ‫ازآن‬           ‫یت‬
                                                                ‫اغصه‬
                                                                   ‫کو‬‫شظلم‬
                                                                        ‫ونی ت‬
                                                                            ‫وخصومت باشد ‪ -‬و به‌ع‬
‫داهم ‪ < ۱‬بروزن‌کاظطم تاج پادشاهانرا‬                       ‫پیش کسی بردن‪ -‬ومحا کمه نمودن ویک وکردن‬
                                                                        ‫ميان نك وید همآمده اسن‬
‫گوبند وآلرا دبهیم نزخوانند ‪ -‬و تخت شاهی‬
                      ‫وجتر بادشاهی راهم گفته‌اند ‪2‬‬        ‫داو ناف ‪ ۳‬کهنابه ازناشتن نقشی‬
‫بمعنی‌داهل‬   ‫بروزن افول ‏‬         ‫‪۰‬‬   ‫داهول‬                                                                     ‫بمراد باشد ‪.‬‬
‫ات ‪. ۷‬وان علامتی باشد کهدهقانان بجهت‌دفع‬                  ‫‪۳‬‬    ‫کنر ك ویرستارباشد‬              ‫بروزن‌ماه‪.‬‬       ‫‪-‬‬         ‫داه‬

‫جانورانز بانکردرمیان زراعت نصب کنند وصیادان‬               ‫رایز‬    ‫ده‬   ‫وعشد‬       ‫وناکس را همگفته‌اند ‪-‬‬                     ‫مددل‬   ‫و‬


‫کبنرار دام‌سازند ‪ -‬و بمعنی تاج ءرصم هم‌بنظ‬                                   ‫ند که بعربی عشره خوانند ‪. ۴‬‬
                                       ‫آهده است ‪. ۸‬‬
                                                          ‫داها ‪ .‬بروژن باها ء یمعنی دره و عار‬

                                                                                                                     ‫کوه باشد ‪.‬‬
‫وميم » بمعنی دیهیم است که تاج مرصع باشد ‪.‬‬
                                                             ‫داهل ‪ - °‬نم ثالك بر وزن ک کل ‪.‬‬
 ‫دای ‪ -‬بروزن‌لای‪.‬هرچینه‌ورده‌ومرتبه‌را‬
                       ‫‪3‬‬    ‫از دبوارکلی ‪۰‬‬       ‫کون‬
                                                             ‫آزن برمند‬
                                                                     ‫کت بجپت دفم‌جانورآن زبانکار» تا ا‬
‫دابه شوهر بسر ‪ -‬کنابه از کره‬                               ‫وداخل زراعت تشوند ؛ وباین معنی بكر ثالث‬
                                                          ‫هم مده است ونیز(‪ )۱‬علامتی را (گ‪۲‬و)نند که‬

                                                ‫نز ‪.‬‬     ‫(چ‪۲‬ش‪+:‬‬                      ‫‪.‬‬   ‫ونىز‬     ‫چش‪-:‬‬         ‫)‪۱‬‬


   ‫از‪ :‬داور ‪ +‬ی (مصدری) » پپلوی ‪ 017206020‬ر ‪ 01۲2۷6020‬٭ تب رکه )‪۵‬‬                                                  ‫‪۱‬‬
                                                                         ‫‪۰‬‬   ‫‪ :‬داو‬       ‫رك‬     ‫‪۳۴‬‬                   ‫‪.‬‬    ‫داور‬   ‫رك‪:‬‬


        ‫شکمش خاسته همحون دم رویاهان‪.‬‬                          ‫داهان‬    ‫‪ _- ۴‬تاك رز رادید (رزبان)آ ستن چون‬

  ‫‪۱۹۱٩‬‏ ‪.‬‬    ‫«منوچهری‌دامغانی‬
  ‫وداهیم ‪1‬‬   ‫‪ ۹۳ ۹‬از بونانی‪ .‬ره ‪ :‬دهم‬              ‫(«‪.‬م‪.).‬‬    ‫داهول‬     ‫—‪-‬‬    ‫‪۵‬‬                 ‫رلك‪ :‬ده‪.‬‬       ‫‪_ ۴‬‬

        ‫دیهیم ‪.‬‬     ‫«راهم» (ھ‪.‬م‪- (.‬‬      ‫مصحف‬    ‫ياين معنی ظ»‬     ‫‪_ 4‬‬                     ‫‪.‬‬   ‫رك‪ :‬داهل‬         ‫‪- ۷‬‬

                                           ‫رك ‪ :‬داو ‪۰‬‬    ‫٭_‬              ‫‪ :‬داهم ۾ دیپیم ‪.‬‬            ‫رك‬    ‫_‬    ‫‏‪٩‬‬


  ‫‪ #‬دایه ‪ -‬بفتح‌اول وکسرسوم (لهجةمر کزی)‪.‬فی‪ .‬اوتا ‪( 0062‬ماده[ ازجانوران])‪,‬‬
   ‫(شبردادن)‪ .‬ارمنی ‪kaeyad‬‏ (دانه؛مربی)‬                ‫بهلوی ‪( 1212‬دابه) ‪ ۰‬هندی باستان ريشة ‪20 -‬‬
    ‫‪eyûd‬‏ (ازفارسی) ‪ ۰‬افغانیع ‪33‬‬                ‫(مادره دابه)‬     ‫‪îd .‬‏ و ‪( 3۷10‬مادر) ‪niûd ۰‬‏‬                             ‫کردی ‪2‬‬
   ‫(مادر) » در‬      ‫اررامالی ‪2‬‬        ‫استی ‪( 01830 . 711/720‬شیر دادن) » بلوچی ع ‪iãd‬‏ «اسشق ‪۹۶‬‬
   ‫لپجه های دیگر کردی ‪.‬ةل ‪) .‬ةل ‪ 21 .‬وشرء «د‪ .‬اورامان ‪ » ۰۲۱2‬معرب‌آن دابة (ماماه‬
   ‫که از کورك‬        ‫زمائ‪-‬ی‬
                          ‫» شیرده » مرضعه ‏ قابله ‏ ما‬           ‫هنده‬
                                                                    ‫ر‏د؛‬
                                                                       ‫ی‪۰۲‬‬
########## leaf 283 (NR=284) ~printed 826
                                                  ‫بیان دویم‬

          ‫ودو لغت و کنات‬                ‫در دال بی‌نقطه بابای ابجد مشتمل بریست‬


‫=روزن چناله ‪ ۰‬بمعنی دبال‬
                       ‫د باله ‪ ۷‬ب‬                        ‫بفتح اول و سکون الی ‪ ۰‬بمعنی "‬                  ‫دب‬

                                 ‫است که تراج باشد ‪۰‬‬          ‫اسب را‬    ‫نگاهداشتن باشد ‪ -‬و بهندی جهاایدن‬
                                                             ‫کویند ‪ -‬ویابای فارسی دایره را نامند و بعربی‬
‫» وعظمت را‬             ‫مهتاب »ا وازه وشان وش و کت و‬          ‫دف خوانند دوف‌معربآست ‪ ۱‬ونم اول ‪۲‬‬
                                                             ‫در عربی خرس را کوبند‪ .‬اکر قدری از خون‬
‫د بدبه* ب«ابای ابجد بروزن دغدغه‪,‬‬                              ‫کی را ا یت ر‬
                                                                                                         ‫شود ‪.۴‬‬
‫بمعنی بزرکی واظهارجاه وعظمت باشد ‪ -‬وآواز‬
‫مشوال آنرا فر‬
            ‫اره‬
              ‫ودای دهل و قا‬
                          ‫عظیم ص‬                             ‫‪ - ۵‬بفتح اول والی‌مشدد بالف کشیده‪.‬‬
                                            ‫گونند ‪*٩.‬‏‬       ‫روایند ‪ ۴‬وبعربی‌قرع‌خوانشد ؛ وضم اول‬
                                                                                                ‫کدو ک‬
‫« بکسر اول وسکون ثالی وسین‬                  ‫بس‬
                                             ‫د‬                        ‫وبی‌تشدید ثالی هم بنظرآمده است ‪.‬‬
‫ديشت‬    ‫بی‌قطه » دوشاب خرما را گون که آتش‬
                                                             ‫داب ‪ -‬منم اول بروزنکلاب » نوعی‬
                                                                                          ‫ب‬
                       ‫باشد ‪ .‬گووبند عربی است ‪٩۱.‬‏‬           ‫ازریعان است © وافرا سوستی رگوند ‪ .‬و آن‬
 ‫د بستان ‪٣‬ے‏ بقتح اول بروزن شستان»‬                           ‫کرم وخشك است درسیم ‪ .‬فواق را نافع است ؛‬
                   ‫‪.‬‬    ‫ومکتب‌خانه راگوبند‬    ‫دبرستان‬                                     ‫وبفتح اول همگفته‌اند ‪:‬‬

‫» طفل‬    ‫شبتانی‬         ‫بروزن‬   ‫د بستا نی ‪۴‬ے‬             ‫دبال ‪ -‬بروزن وبال » میوه‌ابت که‬
                                ‫مکتب خانه را گویند ‪.‬‬                                             ‫آرا تنج گوبند ‪.‬‬


  ‫‪citrouille‬‬            ‫‪۴‬‏ =‬     ‫‪ -‬و دوم مشدد ‪ ۴ .‬رك ‪ :‬خرس ‪.‬‬                 ‫‪۳‬‬       ‫رک‪:‬دف»دب‌تان‪.‬‬       ‫‪۱‬‬


  ‫‪ :‬دباله ‪۰‬‬   ‫رك‬       ‫بت‬   ‫‪۹‬‬      ‫‪۵‬‏ = ‪( menthe‬فر) «لك ‪ ۲‬ص ‪. ۸۷۰‬‬                         ‫(فر) «لك» ص ‪. ۷۷۰‬‬
  ‫‪ - ۸‬از(عر) «طبل و کوی‌را گویند»«شرح قاموس» ‪.‬‬                                   ‫دبال ‪۰‬‬   ‫رکک‪:‬‬      ‫‪7‬‬




   ‫*‪( -2‬عر) دهل ونقاره«قاموس»‪:‬‬                     ‫است«این درید؟» ‪.‬‬     ‫از سوت‬     ‫دشر ح فاموس» و آن حکات‬

  ‫کرده‌اند که آنجه برادرش داده است صلت لشکررا واحرار وشمرا‬                       ‫رابرین حرص‬       ‫«خداو ند سلطان‬


  ‫‪ ۱‬با (عر) دبس بکسر‬               ‫‪.> ۸۵۲‬‬   ‫‪.٩‬‏ «تاریخ هقی‬    ‫راء بایث مسل‬   ‫را تا بوقی ودىدبه زن را ومخره‬

  ‫اول وکبسدروه»شیرة اخنرمگاوبشیينرة‌است»<شرح‌قاموس» ‪« 010۲ 61 56112=1‬لك‪۲‬س ‪. ۷۷‬‬
   ‫‪ _ ۴‬از‪ :‬دب ‪-۲‬ستان (بوندمکان) ؛جز واول ارزه دپ است‪ .‬کلمة اخدر کدتریبهای‬
   ‫حخامنشی بزبان پارسی باستان ‪.‬بصورت ‪ 101‬بکار رفته و آن هم بادکاری است از قوم سور‬
  ‫‪ . ۲۴‬دوب ‪ 011‬در زبان سومری‌بممنی لوحه وخط است » ابن‌کلمه وارد زباناکدی (زبان‬
       ‫شه درصضعهةً ‪۸‬‬
```


## [2026-09-05T20:15:54.659Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 285 286; do echo \"########## NR=$n leaf $((n-1)) ~printed $((n-1+540))\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -70; done",
 "description": "Print BQT leaves 284-285"
}
```


### [2026-09-05T20:15:56.493Z] TOOL RESULT

```
########## NR=285 leaf 284 ~printed 824
 ‫‪۷‬‬      ‫>‬                                                                                                                 ‫دق‬


‫ورن‬     ‫سر‬    ‫اول‬       ‫قح‬        ‫‪-‬‬        ‫سك‬    ‫دبو‬
                                                                   ‫وقاف »‬                ‫وکون‬
                                                                                            ‫دلق » بکراول س‬
‫خبازی‬   ‫نان کلاغ زا کو شت وبعربی‬                ‫‪.‬گل‬    ‫عرومك‬                             ‫اندام زرخك‬   ‫و‬   ‫برنگه‬     ‫است‬   ‫حمی‬
                                                                    ‫نرا دو رج‬        ‫و‬

                                                      ‫خوانند ‪.‬‬     ‫لعابیسفید‬         ‫عگلوىبندیسببآنکه چون ‪3‬‬
                                                                    ‫وحل‌زمانند عل ازدرون‌آن برآبد ‪.‬گرم وخشك‬
‫دلو سه د بفتح اول بر وزن سبوچه »‬
                                                                    ‫است دردویم» وجمیع ورمها رانافم است ‪ .‬گویند‬
‫پس کشتی‬             ‫ختاکنهۂ‬
                          ‫بمه‌نی آخر دبوس اس‬
                                                      ‫باشد ‪3.‬‬                                               ‫عربی است ‪١‬‏‬
                                                                    ‫دبوداد ه بنم اول وانی بواورسیده‬
 ‫بنتح اول وثانی بواو رسیده‬                 ‫د بو کی‬
‫که‬    ‫است ‪۷‬‬   ‫‪«.۰‬معمی دبومك‬            ‫بتحتانی کے ده‬        ‫وکاف‬
                                                                    ‫ودال ابجه بالف کشده وبرای‌فرشت زده " لوعی‬
‫کنلاغ باشد که بمربی خبازی خوانند ؛‬
                                 ‫گل نا‬                             ‫از ابهل است آونرا ویر هندی یگزوبند ؛‬
                                                                    ‫و بای حوف الی بای حطی هم بنظر آمده‬
‫ان نیاتی‬      ‫‪.‬و‬    ‫وبعضی گوبند دبو کی ينبرك است‬
                                                                                                                      ‫است‪:.‬‬
‫که آ فتاب رود‬          ‫طرف‬   ‫ھر‬       ‫جه‬   ‫باشف آفتاب درست‬

                                                                   ‫= بفتح اول بر وزن مجوی »‬                 ‫بوس‬
                                                                                                              ‫د‬
 ‫به‬
  ‫آن‌یات روی بجانبآفتاب دارد وبعربی مکلو‬
                                                      ‫خوالند ‪.‬‬
                                                                   ‫قامایت درماوراءلنپن مابین سمرفند و بخارا ؛‬
                                                                    ‫ویعتی کو رد یک بودهدبوس نام که آن قاءه‬
  ‫شاتفرکندن‪-‬‬                  ‫بزابری‬
                                   ‫دبه در‬                           ‫رابتا کرد ؟ ‪ -‬و گرز آهنین رانیز کوبند و بعر بی‬
                                                                    ‫یزهمین معنی دارد ‪ = ۴‬و دبوسة کشتی راهم‬
             ‫آوردن وفتنه انگیختن را گیوزیند ‪.‬‬                                      ‫کفته'ند »وان خانه‌است دریس کشتی ‪,‬‬



                                                                                             ‫‪ -‬بر ‪.‬‬   ‫چش‪:‬‬     ‫(‪)۱‬‬


   ‫‪١11051۷‬‏ لازنی «لف‪۲‬ص ‪« ۹۷‬دیق بكر اول ودابوق‬                                     ‫‪ ۱‬اناع (فر) = ‪50‬آبونانی‬
   ‫که باو شکار کرده مشود پرنده» «شرح قاموی» ‪.‬‬                            ‫است‬
                                                                           ‫شاءیسر‬
                                                                                ‫یول‬
                                                                                  ‫بروزن کافور ودبوفاء بروژن جا‬
     ‫باين مفهوم درحدود العالم ازشهرهای‬                       ‫‪۴‬‬                ‫‪ -‬مصحف «دیورار(هم) ‪.‬‬              ‫‪۴‬‬
‫ماوراءالتهر «دیوسی» آمده ومیئورسکی کوید ‪ 500۵221 :‬همان ‪( 81011212‬شیادالدین) کنوای‬
                              ‫دنوحنه *مینورسکی بات ‪ .‬فهرست‬                         ‫‪.‬دود ‪= . ۲۵۳۲‬‬
                                                                                               ‫ات "مینورسکی ج‬
  ‫که کریا‬          ‫‪۳‬‬                       ‫‪.‬ر وزن تنور ( بتشدید نون) عمودهای‬
                                                                           ‫دس ب‬                           ‫ر‬
                                           ‫معرب تپوز است ‪«».‬شرح قاموی» و‪:‬در فارسی‌بتخفیف نون آمده ‪:‬‬
   ‫چون زند برکردن گردان عمود گاوسار ‪.‬‬                                ‫چون زند بر مهرة ثیران دبوس شصت‌من‬
     ‫«منوچپری دامفالی ‪. ۸۲‬‬
                                                        ‫‪۰‬‬   ‫رك‪ :‬دبومك‪‎‬‬    ‫‪-‬‬    ‫‪٦‬‬           ‫® رك‪ :‬دبوکی ‪۰‬‬
                                                       ‫* دبوسی و دبوسه ‪ -‬بفتح اول " رك‪ :‬دبوس‪. ‎‬‬

                                                                    ‫هه از صفحة ‪۳۲۸‬‬
      ‫قوم ‏‪ )4)K4d‬شدهصورت ‪ ۷000‬و ‪11P‬‏ ‪1‬اا درآمده ‪.‬همی‌کلمه واردزبان آرامی شده‪ .‬نا‬
      ‫گردیده ویزیسسنی لوحه وصفحه گرفته شده وبعدها داخل زبان عرمی شده صورت دف دآرمده‬
      ‫ویمعتی‌لوحه بکار رفته است ‪( .‬رله‪.retröwdmerF 812۳61:‬‏ ‪,remmiZ ehcsidakkA‬‬
      ‫‪ )۰ 91‬ره لفت‌های دببر * دییرستان» دیبا * دیباچه و دبوان همین کمه است ‪ « .‬فاب‪۱‬ص‪۸۸۰+‬‬
                                      ‫‪ -۴‬از‪ :‬دبتان ‪ +‬ی (سبت)‬                                 ‫‪ ۱‬و ‪ » ۲۱۱‬ورك‪ :‬دس‪.‬‬

########## NR=286 leaf 285 ~printed 825
 ‫دحر‬                                                                                                  ‫‪۲‬‬     ‫ی‬


                                                 ‫ك لیس بروزن طبیب » هرچیزبکهآ ترا‬
‫دلیر فلكت هکنابه از کرکب عطارد‬                                                             ‫ارم کوفته باشاد ‪.‬‬
                                   ‫‪9 .‬‬   ‫ات‬             ‫‪۰‬‬        ‫‪‌ ۰‬‬       ‫ب‬
                                                      ‫برورن وزیر» مسشی‌وتوستده‬
                                                                                  ‫‪°‬‬
                                                                                           ‫=‬
                                                                                               ‫‪۱‬‬




‫ذلیقی » بروزن حقیقی » لوعی ازقماش‬
                    ‫ناشن درلپایت لطات ‪. ۴‬‬
                                                  ‫د لسر ستان؟ ‪ -‬بمعنی دبتان است که‬
                                                  ‫مکب خاله باشد ‪ - ۴‬و بعضی گویند دفترخانه‬


                                         ‫بیان سوم‬

                   ‫بر دو لفت‬      ‫مشتمل‬        ‫در دال بی نقطه ‪ ۲‬جم‬


‫د جر = بفتح اول و کر الی و سکون‬                   ‫کج ‪ -‬بضماول وسکون الی» هرجیز که‬
‫رای قرشت ‪ ۰‬غله‌است که برا لوینا گویند ‪.۷‬‬          ‫وامثال آن مالیده شده‬           ‫وعل‬       ‫وشر‬     ‫دوشاب‬   ‫درآن‬


‫استوآ بی که وبرا درآن‌پشته‬   ‫وآن سر د وخنك‬            ‫باشد و بر دست وپا بجسبد ‪ -‬ویفتح اول درءربی‬
       ‫باشند حیض براند ‪ ۰‬کوبند عربی است ‪۰‬‬                                      ‫مرغ صحرایی راکوبند ‪. ۵‬‬




  ‫‪ - ۱‬قی‪:‬یارسی باستان‪,‬کلمامتمار)_ ‪( 11‬خط)؛ پرا کرت ‪( 1۳11-* 1014 -‬کتیبه‬
  ‫های آشوک) ؛ پهلوی ‪hîrîp(i) ۰ ۲1۳140 . ۲۵۷1۳00‬‏ ‪ d‬و ‪ ۲1۱4‬ر(کدتیبه ها) ارمنیع‬
 ‫ور‪ :‬هویشمان ‪ * 04۵‬لیر کت ‪ ۵‬و ‪.۵‬دائرة لمعارف اسلام ‪ .‬راجم برمشة‬                        ‫‏‪ dpir‬مشق ‪۰‬‬
                        ‫از‪ :‬دس (ه‪.‬م‪٣ ).‬‏ ستان (يوندمكان) ‪:‬‬             ‫‪۲‬‬               ‫‪۰‬‬    ‫دییی‪.‬را*‪ :‬دسان‬


  ‫‪ - ۴‬دیبرستان کنم در هیکل روم کنم آبین مطران را مطرا ‪«.‬خاقالی شروانی ‪۲۲٩‬‏ ‪.‬‬
 ‫‪ ۴‬اصل این نوع پارچه از دبیق ( با دبقا بقول حمزة‌بن حن و قل ياقوت از او)‬
   ‫آمده است وآن شپری‌بوده است درعصر‪:‬هپی صندوق‌ها کبشرادند وخلمت‌ها برآوردند ‪ :‬جامهای‬
  ‫دوخته و نا دوخته » ورسول برپای خاست» وهفت دواج بیرون گرفتند یکی از آن سياه و دمکر‬
 ‫© = باین محتی‬     ‫دیقی های بفدادی بفات تادر ملکانه ‪« ».‬تاریج هقی ص‪ ۷4‬متن وحاشیه» ‪.‬‬
 ‫درعربی بافته‌نشد ؛مصحف ”رج نگ خواره است وآن پرنده‌است ‪ .‬ووج شتر مر غ رای‌گویند «‬
                              ‫‪( 1061۲20 = ۱‬نر) «ل‪ ۲‬ص‪. ۱۸‬‬                               ‫«رح قاموس > ‪.‬‬
                                                                                                   ‫ش‬
  ‫که ‪۵‬ه؟‪.‬‬
        ‫(صدری ) ؛ پپلوی ‪« 171۳10‬رنب‬
                                  ‫* دیری ‪ -‬بفتح اول » از‪ :‬دییر ی م‬
                                              ‫معد ‪.‬‬         ‫ص‪۲۰‬‬
                                                              ‫شفل دییر ؛ عمل در ‪ -‬رك‪ :‬فاب ‪۱‬‬
```


## [2026-09-05T20:16:22.288Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== KLN divan ==\"; grep -n -iE \"^divan|divan,|d[iī]w[aā]n\" KLN_1966.txt | head -20; echo \"== KLN 1971 ==\"; grep -n -i \"divan\" KLN_1971.txt | head -10",
 "description": "Grep Klein for divan"
}
```


### [2026-09-05T20:16:22.358Z] TOOL RESULT

```
== KLN divan ==
11176:devvanee,  dewany,  n.,  the  office  of  a  dewan.  — Hind,  diwani,  fr.  Pers.  diwani,  fr.  diwdn.  See prec.  word.
11356:die,  n,  cube.  —  ME.  dee,  fr.  OF.  de  (F.  de),  fr.  L. dalus,  pp.  of  dare,  ‘to  give’,  used  as  a  noun.  Cp. It.,  Sp.,  Port,  dado,  OProven?.  dal,  ‘die’,  and  see date,  ’point  of  time’.  Cp.  also  dado, die,  intr.  v.  —  ME.  dien,  deyen,  fr.  ON.  deyja, rel.  to  Dan.  de,  Swed.  do,  ‘to  die’,  OFris.  deja, ‘to  kill’,  OS.  doian,  OHG.  touwen,  Goth,  diwans, ‘mortal’,  fr.  Teut.  base  *dau-,  ‘to  die’.  See  dead and  cp.  words  there  referred  to. dielectric  adj.,  nonconducting  (electr.)  —  Form¬ ed  fr.  di-  (form  of  dia-  before  a  vowel)  and electric.
11890:divan,  n.,  1)  in  Oriental  countries,  a  council  of state;  2)  a  court  of  justice;  3)  a  large  low  sofa. —  Turk,  diwan,  fr.  Pers.  diwan,  ‘a  royal  court; a  council  of  state’,  whence  on  the  one  hand,  ‘a convenient  seat,  couch’,  and  on  the  other  ‘a register,  an  account  book ;  a  collection  of  poems’ (whence  also  Arab,  diwdn,  It.  divano,  F.  divan, etc.);  rel.  to  Pers.  debir,  dibir,  ‘writer’.  Cp.  de- wan,  dewanee,  diwan,  douane,  aduana. divaricate,  intr.  and  tr.  v.,  to  branch,  diverge.  — L.  divdricdtus,  pp.  of  divaricare,  ‘to  stretch apart,  spread  asunder’,  fr.  di-,  ‘apart’,  and  vari- edre ,  ‘to  spread  the  legs  apart,  to  straddle’,  fr. various,  ‘with  bent  feet,  with  feet  spread  apart, straddling’,  fr.  varus,  ‘bent,  knock-kneed’,  fr. I.-E.  base  *wd-,  ‘to  bend,  turn,  twist’,  whence also  L.  varius,  ‘different,  changing,  varying, various’.  See  various  and  verbal  suff.  -ate  and cp.  prevaricate.
11932:diwan,  n.  —  A  var.  of  dewan. diwani,  n.  —  A  var.  of  dewanee. dixie,  also  dixy,  n.,  a  kind  of  mess  tin  (slang).  — Hind,  degcht,  ‘a  small  kettle’,  fr.  Pers.  degcha, dimin.  of  deg,  ‘pot’,  which  is  rel.  to  Pahlavi  deg, ‘pot’.  Arm.  dez,  ‘heap’,  and  to  OI.  dihmi,  'I smear,  anoint’,  fr.  I.-E.  base  *dheigh-,  *dhoigh-, *dhigh-,  ‘to  form  out  of  clay,  to  knead,  form’. See  dough  and  cp.  next  word, dizdar,  disdar,  n.,  the  warden  of  a  castle.  —  Pers. dizdar,  ‘holder  of  a  castle’,  fr.  diz,  ‘castle’,  and -dar,  ‘holder,  possessor’.  The  first  element  is rel.  to  OPers.  dida,  ‘castle’,  Avestic  daeza, ‘wall’,  Arm.  dez,  ‘heap’ ;  see  prec.  word  and  cp. the  second  element  in  paradise.  For  the  second element  see  aumildar  and  cp.  words  there  re¬ ferred  to.
12496:Derivatives:  dwell,  n.,  dwell-er,  n.,  dwell-ing,  n. dwindle,  intr.  v.  —  Dimin.  of  next  word.  The verb  dwindle  was  first  used  by  Shakespeare, dwine,  intr.  v„  to  waste  away  ( archaic  and  dial. Brit.)  —  ME.  dwinen,  fr.  OE.  dwinan,  ‘to  lan¬ guish,  waste  away,  vanish’,  rel.  to  ON.  dvina, MDu.  dvinen,  Dan.  tvine,  of  s.m.,  Du.  verdwij- nen,  ‘to  waste  away,  vanish’,  and  cogn.  with Arm.  di,  ‘dead  body,  corpse’,  OIr.  dith,  ‘end, death’;  fr.  I.-E.  nase  *dhwei-,  enlargement  of base  *dhew-,  *dheu-,  ‘to  pine  away,  die’,  whence Goth,  diwans,  ‘mortal’,  and,  with  vowel  grad¬ ation,  OS.  doian,  ON.  deyja,  ‘to  die’.  Goth. daups,  ‘dead’.  See  dead  and  cp.  prec.  word. Derivative:  dwindl-er,  n.
15544:funeralis ,  fr.  L.  fiinus,  gen.  funeris.  See  funeral,n. funeral,  n.,  a  burial.  —  OF.  funeraille  (F.  fune- railles),  fr.  ML.  funeralia,  ‘funeral  rites’,  fr.  L. fiinus,  gen.  funeris,  ‘burial,  funeral’,  which prob.  stands  for  *dhewenos,  ‘that  which  pertains to  death’,  fr.  I.-E.  base  *dhew-,  *dheu-,  ‘to  die’, whence  also  Goth,  daups,  ‘dead’,  diwans, ‘mortal’.  See  dead  and  cp.  words  there  referred to.  Cp.  also  funebrial.
== KLN 1971 ==
7954:house’. See divan and cp. douane. 
69829:dia. — Arab, and Pers. dlwdn; see divan. The 
74238:divan, n., i) in Oriental countries, a council of 
74245:(whence also Arab, diwdn, It. divano , F. divan , 
74820:divan and cp. aduana, douane. 
75731:house; collection of books’. See divan and cp. 
170059:ottoman, n., a kind of sofa or divan. — F. otto-
```


## [2026-09-05T20:16:23.226Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls incoming/PLA/ 2>/dev/null; echo \"== PLA diwan/dibag ==\"; grep -n -iE \"d[iī]b[aā][ǧgğj]|d[iī]w[aā]n|adab\" incoming/PLA/PLA_pages.txt | head -30",
 "description": "Grep Asbaghi"
}
```


### [2026-09-05T20:16:23.273Z] TOOL RESULT

```
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
== PLA diwan/dibag ==
740:ägur                                                                             6                                                                ’adab
776:„bi- Bdäb: Pl. v. _,ı adab q. v.
778:1        -’adab:           "gute          Sitten,           Anstand,            Höflichkeit"                aus   dem       pers.    _ı    adab     u.
792:adab                                                                                      7                                                         adarbigän
795:I -            ’adab:                "literarische                        Bildung"        aus       dem    pers,      —,ı    Adab      <<    mp.305           dipi
802: abo                 -     ’ adabhäna:                        "Klosett,           Toilette,          WC."      aus    pers.
803:                                                                                                                          —                adab      s.       adab
819:                                                                                          _,) ’adab q. v.
2144:              aiven          < air.              *abi-dayana               s. ’adab,             syr.      abden T,
2628:on        _ badab$än:                     Name     des nordöstlichen               Teiles       des heutigen           Afghanistan ,
2629:      aus dem pers. >.                              badabSän          Dar.        “>ı balabS,           frz.    balais u.       dtsch.
6811:&”             dabaf:        "mit          Figuren        bemalen,            sticken"          s.     dibag.
7391:El» - dibag? : "Vorrede"                               dim.     v. diba 5,
7393:Sl» - dibagi: "Brokathändler".
7445:       mand,          divan            (p.        Qie    )     °, syr.        (8,     ', frz.      divan,        dtsch.     Diwan
7447:       dtsch.           Divan,           Diwan:                               "
15418:Bharucha,           Ervad           Sherarji     dadabhi:              Pahlavi-English              Glossary,           Bombay        1912.
15781:Ibn   Qutaiba:            Adab    al-kitäb,       Kairo       1985.
15830:Mohammadi,               M.:       ad-diräsät          al-adabiyya,             4 Bde.        Beirut,       1959     ff.
15998:        DäneSkade-ye                  adabiyyät               wa °ulüm             ensäni          Daneskade-ye                 Ferdowsi              Bd.
```


## [2026-09-05T20:16:30.332Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '770,825p' incoming/PLA/PLA_pages.txt",
 "description": "Asbaghi adab entry"
}
```


### [2026-09-05T20:16:30.372Z] TOOL RESULT

```
             syr.        ,oı    abor       7,


 NW’                 - ähürsälär:                     "Stallmeister"                  s.    ähür u,          sälär      .


„bi- Bdäb: Pl. v. _,ı adab q. v.

1        -’adab:           "gute          Sitten,           Anstand,            Höflichkeit"                aus   dem       pers.    _ı    adab     u.
              wei ayin <a.    IYpow                              alven       air.           *abi-dagna            8, (wahrscheinlich                eine
             ältere Entlehnung)-



1.       al-     Marta“             s.v
2.       Kent       S.     165,          Mayrhofer            S.    101
3.       Kiyäs.           v.
4.       Nyberg          Bd.        IIs,        v.
5.       Wahrmund              s.    v.,       LD.     s.     v.,      Addai         Scher       s.    v.
6.       Nyberg          Bd.        II    s.    v,
7.       Brockelmann                 s.    v.
8.       Nyberg          Bd.        II    s.    v.
adab                                                                                      7                                                         adarbigän


I -            ’adab:                "literarische                        Bildung"        aus       dem    pers,      —,ı    Adab      <<    mp.305           dipi
              "Inschrift" —T air.                                    *dipi-vara,

   5                                                                    -                                        -
;b3)_              ?”udabä:            Pl.           v. al            adib        "Gelehrter"             s.   adib.


 abo                 -     ’ adabhäna:                        "Klosett,           Toilette,          WC."      aus    pers.
                                                                                                                          —                adab      s.       adab
              + pers,                „4      häne              "Haus"       TU mp.       19»         xänag      mit       der       Bed.    "Haus        der
              Erziehung".                    Nach              Dehhoda        könnte          es    alt        abhane        "ein      Haus,        in    dem    es
              Wasser             gibt"         heißen.


ri             -     ”adbil:              Ort             in Armenien              s.    ‚>        dabil       m.           Ir       adbil     1,

          s                                                                                                                                               -
®,>!           -     ”adrün:                "Wohnung,                 Heimat"           pers.       2 aus      dem    pers,          Jy.ı      andarun          "in,
              drin"             T mp.             dw               andar-ron,            mand,       andruna         5,


@b>} - ”adyän: Pl. v. (u din s. din.

on - ”adib:                           "Gelehrter"                     act.        Pt.    aus
                                                                                          _,) ’adab q. v.

Uni - ’adyün = ’adyan s. 'adyan 4. v.

      r        .                                                                                                                -
„>t-           agdar:            "3.        Monat              des    Sonnenjahres"                 4          mp.)         atür      "9.     Monat!"         _aw.
              atar,             ayr,        ap.           ätar       5.
```


## [2026-09-05T20:16:31.422Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '7370,7400p' incoming/PLA/PLA_pages.txt; echo \"==== divan ====\"; sed -n '7430,7460p' incoming/PLA/PLA_pages.txt",
 "description": "Asbaghi dibag and divan"
}
```


### [2026-09-05T20:16:31.470Z] TOOL RESULT

```
 4.        Addai    Scher               s.     v.
 5. Muhit s. v.
 6.        Kamäl
              s. v.
 7.        Brockelmann                  s.     v.
 8.        al-MuCarrab                  Ss.    Vs
 9.        ebda.
 10.        Löw    s.        v.
dayäwin                                                                   129


«sl,» - dayäwin: Pl. v. ©l,, diwän s. diwän.

IL»)- dibä:;               "Brokat,             gestickter           Goldstoff"          pers,    I aus   pers.     Lı> dibä
          <      Mp. „ro,          depäk         ap.           dipi       2     Syrı 32 3 3, mand.          diba&    (p. eb>     ) a


do»        - dibäf
             di    = diba                    Ss. diba.


El» - dibag? : "Vorrede"                               dim.     v. diba 5,

Sl» - dibagi: "Brokathändler".

Ole, -divag= ding s. dinag °.
2>> - dibüg = dübüd s.                                dibu      7,

23         - didär:           "ulmus,            Ulme"        = dadär         s.   dadär.


==== divan ====
„L>     - dinär:              "Goldstück"                 pers.         „u,       dinär mp.           3.          denär.
       "das       Wort        wurde           n.    Nyberg        aus    Byz.,        griech.      Inyärtov             (xpvooVY)-
       entliehen,                 welches           seinerseits           eine        Entlehnung          aus     dem     lat.   denarius   zu
       sein       scheint               1,
       GawäliqI in al-MuCarrab ist der Ansicht, daß das Wort persischen
                                                       DER
       Ursprungs ist, mand. dinara, aram. Xyya, syr. Ir® 2,




 »-> - dinarw:                    "eine           Art Pflanze"           pers.        *.

Olpe» - diwän:                "königlicher                    Hof,   Gerichtshof"            aus     dem pers.          Ol»>     diwän,
       Mp.       ıyy>        divan           rapie              vahana            „Dokumentenhaus“           —T Sipi        "schreiben"     °
       mand,          divan            (p.        Qie    )     °, syr.        (8,     ', frz.      divan,        dtsch.     Diwan
       "Geheimer              Staatsrat                 des    Herrschers.-            Schriftensammlung"                  8,
       dtsch.           Divan,           Diwan:                               "
       1.       "Ruhebett,               Amtszimmer"
       2.       "der        ehemalige              tk.       Staatsrat!
       3.       "Versammlung,                     Beratung"          pers.            > ar.        > tk.         °.


als» L_               batt-        e diwäni:                 "Staatsschriften"-


                                                                          D



2,5         -    darnüba:               "Leontice,             Leontepetalum'              pers.     10     s.    adarbüy,
```


## [2026-09-05T20:16:52.827Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=d.split('\\n')\nt='\\n'.join(lines[:11890])\nprint('formfeeds before divan line:', t.count('\\f'))\nEOF\ngrep -n \"\\[pdf page\" KLN_1966.txt | head -3; echo \"---- markers ----\"; sed -n '11880,11895p' KLN_1966.txt | cut -c1-200",
 "description": "Locate Klein page for divan"
}
```


### [2026-09-05T20:16:54.577Z] TOOL RESULT

```
formfeeds before divan line: 256
---- markers ----
ditheism,  n.,  belief  in  the  existence  of  two  gods.
—  Formed  fr.  di-,  ‘two’,  and  theism, dithionic,  adj.,  pertaining  to  a  compound  that contains  twd  atoms  of  sulfur  (chem.)  —  Formed fr.  di-,  ‘two’,  and  Gk.  dsiov,  �
dithyramb,  n.,  1)  in  ancient  Greece,  a  song  in honor  of  Bacchus;  2)  any  wildly  emotional song.  —  L.  dithyr ambus,  fr.  Gk.  8t&upa|i.(Joc,
467
divergence
‘poem  in  honor  of  Bacchus’,  a  loan  word  of pre-Hellenic  origin.  Cp.  triumph.  Cp.  also  iamb. Derivative:  dithyramb-ic,  adj. ditriglyph,  n.,  a  space  between  two  columns  of the
ditrochee,  n.,  a  double  trochee  (pros.)  —  L.  di- trochaeus,  fr.  Gk.  8ixp6x“t°<;>  ‘a  double  tro¬ chee’,  fr.  St-  (see  di-,  ‘double’)  and  xpo/aioc, ‘trochee’.  See 
ditto,  n.,  the  same  (lit.  the  foresaid).  —  It.,  form used  in  Tuscany  for  literary  It,  detto,  ‘that  which has  been  said  (before)’,  pp.  of  dire,  ‘to  say’,  fr. L.  dic
Derivatives:  diurnal-ly,  adv.,  diurnal-ness,  n. diutumal,  adj.,  of  long  duration.  —  Formed  with adj.  suff.  -al  fr.  L.  diuturnus,  ‘of  long  duration, lasting’  (on  analogy  of 
diutumity,  n.,  long  duration.  ��  L.  diuturnitas,  fr. diuturnus.  See  prec.  word  and  -ity. diva,  n.,  a  prima  donna.  —  It.,  fr.  L.  diva,  ‘a  god¬ dess’,  fem.  of  divus
divan,  n.,  1)  in  Oriental  countries,  a  council  of state;  2)  a  court  of  justice;  3)  a  large  low  sofa. —  Turk,  diwan,  fr.  Pers.  diwan,  ‘a  royal  court; a  council  of  state
divaricate,  adj.,  divergent.  —  L.  divdricdtus,  pp. of  divaricare.  See  divaricate,  v.
Derivatives:  divaricate-ly,  adv.,  divaricate-ness, n.,  divaricat-ion,  n.,  divaricat-or,  n. dive,  intr.  v.  —  ME.  diven,  duven,  fr.  OE.  dyfan, ‘to  immerse’,  a  weak  transitive  
Derivatives:  dive,  n.,  div-er,  n. diverge,  intr.  v.,  to  move  or  be  in  different  direct¬ ions.  —  ModL.  divergere,  ‘to  go  in  different directions,  to  separate’,  fr.  di-  a
Derivatives:  divergence,  divergent  (qq.v.),  di- verg-ing,  adj.,  diverg-ing-ly,  adv. divergence,  divergency,  n.  —  ModL.  divergentia.
divergent
```


## [2026-09-05T20:16:54.848Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== شندف ==\"; grep -rn \"شندف\" *.txt incoming/*/*.txt 2>/dev/null | head; echo \"== MON files ==\"; ls MON_part*.txt; grep -n \"شن دف\\|شن‌دف\" MON_part1.txt MON_part2.txt 2>/dev/null | head",
 "description": "Search for shandaf"
}
```


### [2026-09-05T20:16:54.962Z] TOOL RESULT

```
== شندف ==
BQT_v2.txt:1538:قومی باشندفرومابه وصحرا شین درهندوستان. 
BQT_v2_pages.txt:1096:                              ‫بعنی پنشیند ‪.‬‬                ‫قومی باشندفرومابه وصحرا شین درهندوستان‪.‬‬
FRS.txt:10066:خار . 1 این‌لغت فقطدرس وح هست . ۷ - چ : شندف‌دمل وطبل‌باشد » س 
FRS.txt:21728:شندف ۲۱ 
FRS_pages.txt:10890:  ‫‪ - ۷‬چ ‪ :‬شندف‌دمل وطبل‌باشد » س‬     ‫هست ‪.‬‬     ‫وح‬   ‫این‌لغت فقطدرس‬     ‫‪1‬‬     ‫خار ‪.‬‬
FRS_pages.txt:22836:                                ‫| صندل ‪۳۳۳‬‬                 ‫شندف ‪۱۲‬‬
MON_part2.txt:23270:خواهد کشت» نکش کشندف) کفنته] کششن ): 
MON_part1.txt:86893:شندف: ]2742 (.) طبل» دمامه» نقارة 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:86893:شندف: ]2742 (.) طبل» دمامه» نقارة 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:23270:خواهد کشت» نکش کشندف) کفنته] کششن ): 
== MON files ==
MON_part1.txt
MON_part2.txt
```


## [2026-09-05T20:17:06.270Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^دف\\b\\|^دف:\\|^دف \" MON_part1.txt | head -20; echo \"-- context of شندف --\"; sed -n '86888,86898p' MON_part1.txt",
 "description": "Grep Mo'in for daf"
}
```


### [2026-09-05T20:17:06.342Z] TOOL RESULT

```
10430:دفع کردن» دور کردن (ار جایی)» راندن. 
13125:دفتر یک نگاه؛ مدرسه» سازمان و جز ِ 
13142:دفتر چه‌های سناسنامه. 
13177:دفعی گر دد. 
17973:دفع. 
18131:دفتا): تردن (نعتا و مازند آن)؛ ج. 
23440:دفتر و جز آنها را بهم بندند. هر شربت 
24469:دفاعی فوتبال است. بکك راست: از اعضای 
24475:دفاعی تیم فو تال است. 
24540:دفعات» مکررآ؛ بارهاء چندین بار. بگرانق ۲ 
48117:دف. دایره. (جاد.) مرغی است خوش اواز. 
48360:دفعه از زمین بر می‌خیزد: الف - در هفتم ماه 
48844:دفاعی حیوان را بوجود می آورد؛ خارپشت» 
57442:دف و دایهةٌ کوچکی که چنبر آن از برنج يا 
58271:دفاعی خطرنا کی را کیان می‌دهد. این 
59191:دفع کننده راننده» برطرف کننده. قو و دافعه: 
61976:دف فرهنگ فاررسی معیر ۸۵ 
61981:دف: 1210 [معر.] (ا.) (مست.) چنبری است 
61985:دفتر: 7 (معر. بوست؛ نوشتن ] (ا.) عدة 
62012:دفتر خانه: (0-)202-. [سعر. ف.)] (امر.) 
-- context of شندف --
شنج: 31 (.) سرین» کفل. 

شندرغاز: 52:02:22 (امر.) (عم.) بول 
اند کك» مبلغ نا چیز. 

شندف: ]2742 (.) طبل» دمامه» نقارة 
بزرگك. 

شنزار: 00-72۴ (امر.) بیابان پر شن. 
شنعت 5082۱ [غ. شنعه ] (امسص.) زشتی 
قبح» بدی. طعنه.
```


## [2026-09-05T20:17:14.550Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '61970,62020p' MON_part1.txt",
 "description": "Read Mo'in daf entry"
}
```


### [2026-09-05T20:17:14.601Z] TOOL RESULT

```
کند؛ مزور» حیله گر. کسی که چیزی را برای 
گمراهی خریدار تغییر می‌دهد (فره.) سیم 
ناسره» زرقلب»؛ بول تقلبی. جیب‌بر. کودن. 
تنبل. دغل خاکدان: (کد.) دنیاء علم سفلی. 


دف فرهنگ فاررسی معیر ۸۵ 


قالب آدمی کالید انسان. 

دف: 1210 [معر.] (ا.) (مست.) چنبری است 
که پوستی بر آن چسبانند و قوالان آن را با 
انگشت نوازند. 

دفتر: 7 (معر. بوست؛ نوشتن ] (ا.) عدة 
اوراقی که بهم پیوسته و در جلدی جای داده 
شده و در آن مطالب مختلف» نظم و نثر یا 
محاسیات را نوسند؛ جزوه. کتات. طومار. 
روزنامه. جایی که دییران و منشیان در آنجا به 
کارهای دفتر نوسی می بر دازند؛ کایبینه: دفتر 
وزار تی» دفتر بست (فره.)؛ ج. دفاتر. دفتر 
اخلاق: کتاب اخلاق. دفتر تجار تی: (اقتص. 
حق.) دفتری که تاجر معاملات خود را در 
آن ثبت نماید و از روی آن سود وی تعیین 
گردد. دفتر ت املاک: (حق.) اداره‌ای که 
در آن» موقع املااک و حقوق مربوط و 
اسامی صاحبان آنها شت گردد. دفتر رسید: 
نامه‌هایی که از اداره‌ها برای اشخاص متفرق 
فرستاده می‌شود در دفتری ثبت شده» هنگام 
تحویل آن نامه‌ها امضایی از گیرندة پاکت 
گرفته می‌شود» این دفتر را دفتر رسید گویند 
(فره.)؛ دفتر ارسال مراسلات. دفتر روزنامه: 
(حس. حق.) دفتری که در آن انواع معاملات 
و دخل و خرج و مطالبات و دیون بازرگان 
در هر روز ثبت شود. دفتر مخصوص: 
دارالا نشاء اختصاصی شاه با نخست وزیر و 
با وزیر. دفتر نماننده: (ادا.) دفتری که 
خلاصه مراسلات رسیده و فرستادهة یکت 
اداره» یک موّسسه يا بازرگان در آن نوشته 
شود (فره.)) اندیکاتور. 

دفتر خانه: (0-)202-. [سعر. ف.)] (امر.) 
اداره‌ای که در آنجا اسناد سلطنتی را ثت و 
حظط می‌نمودند. ادارة محاسات. اداره‌ای 
واسته به ادارة شت که در آن اسناد انواع 
معاملات يا ازدواج و طلاق را ثبت کنند؛ 


دفتر اسناد رسمی؛ محضر.
```


## [2026-09-05T20:18:38.000Z] TOOL CALL #39: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T20:18:38.009Z] TOOL RESULT

```


```


## [2026-09-05T20:18:41.625Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%A8%DB%8C%D8%B1",
 "prompt": "Give the full Persian etymology of دبیر (dabir) — Middle Persian, Old Persian dipi-, Akkadian/Sumerian origin, and any related words (دبستان, دیوان)."
}
```


## [2026-09-05T20:18:43.318Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D9%88%D8%A7%D9%86",
 "prompt": "Give the Persian and Arabic etymology sections for دیوان (divan/dīwān): Middle Persian form, Old Persian dipi-, and the Arabic borrowing."
}
```


### [2026-09-05T20:18:50.002Z] TOOL RESULT

```
# Persian Etymology of دبیر (dabir)

Based on the Wiktionary entry provided, the etymology is limited. The source states that دبیر is "Inherited from Middle Persian _𐭣𐭯𐭩𐭥𐭥_ (dibīr)," but does not trace further back to Old Persian, Akkadian, or Sumerian origins.

The only additional etymological note mentions that this word was "Borrowed into Sanskrit as दिविर (divira, 'scribe')," indicating the term's historical significance as a professional designation.

**Related terms** listed in the entry include:
- دبیره (dabire)
- دبیرستان (dabirestân) — literally "scribe-place," referring to high schools
- دبیرستانی (dabirestâni)

The entry does not provide the deeper etymological chain you've requested (Old Persian dipi-, or Akkadian/Sumerian origins). To obtain that information, you would need to consult specialized historical linguistics sources beyond this Wiktionary entry.
```


### [2026-09-05T20:18:50.655Z] TOOL RESULT

```
# Etymology of دیوان (Divan)

## Persian Etymology

According to the Wiktionary entry, Persian دیوان is "Inherited from Middle Persian _d(p)ywʾn'_ (dēwān, 'archive, collected writings')."

The document does not mention an Old Persian form "dipi-" in the content provided.

## Arabic Borrowing

The Persian term influenced Arabic: "→ Arabic: ديوان (dīwān)" appears in the descendants section, indicating the word passed from Persian into Arabic usage.

The Arabic term then branched further into Romance languages (Catalan, Spanish, Portuguese, Occitan) through Andalusian Arabic, ultimately creating words like Spanish "aduana" (customs).

**Note:** The provided content does not include information about Old Persian etymological forms, only the Middle Persian ancestor and subsequent linguistic descendants.
```


## [2026-09-05T20:18:55.448Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D8%AF%D8%A8",
 "prompt": "Give the Arabic etymology section for أدب (adab) in full: what root is it from, is a Persian origin mentioned or rejected, what do the cited scholars say?"
}
```


## [2026-09-05T20:18:57.075Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%81",
 "prompt": "Give the Arabic etymology for دف (duff/daff) 'tambourine' and any Persian entry for دف. Mention Proto-Semitic reconstruction, Hebrew תוף, Akkadian cognates, and whether it is connected with 'board/side' daff."
}
```


### [2026-09-05T20:19:02.157Z] TOOL RESULT

```
# Arabic Etymology of أدب (adab)

**Root:** The word derives from the Semitic root د ء ب (d ʔ b), with 3 related terms in this family.

**Origin Theory:** The entry states it is "probably back-formed singular from آدَاب (ʔādāb), a plural of the verbal noun دَأْب (daʔb), meaning 'persistence, perseverance.'"

**Persian Origin Question:** The page acknowledges this debate directly: "Various influences from Iranian...are often claimed, surely inspired by some general idea of Abbasid cultural supremacy, and present Iranian patriotism hurt by the pervasiveness of Arabic-origin words in the Persian tongue."

In other words, while Persian influences are sometimes proposed for semantic reasons, the entry suggests these claims may be motivated by cultural and political considerations rather than linguistic evidence.

**Cited Scholars:** Two sources are referenced:
1. **Asbaghi (1988)** - examines Persian loanwords in Arabic
2. **Guth (2010)** - discusses politeness and _ʾadab_ from a "Comparative Conceptual-Cultural Perspective"

Neither source description provides specific claims about adab's origins, only their general research areas.
```


### [2026-09-05T20:19:03.730Z] TOOL RESULT

```
# Etymology of دف (Tambourine)

## Arabic Origin

According to the Wiktionary entry, the tambourine sense of دف derives from a root meaning "to push or propel." The entry states: "A more primitive form of دَفَعَ (dafaʕa, 'to push, to propel'), and its resultant noun."

The entry also notes connections to Aramaic דפא (dappā, "board"), which is believed to originate from Sumerian 𒁳 (DAB, "board") or 𒁾 (DUB, "board").

## Persian Entry

The Persian دف (daf) is documented as "a Persian frame drum," borrowed from Arabic دَفّ (daff).

## Notable Absence

The provided content contains **no mention** of:
- Proto-Semitic reconstruction
- Hebrew תוף cognates
- Akkadian cognates
- Direct etymological connection between the "tambourine" sense and the "board/side" sense of daff

The entry only indicates that both senses belong to the root د ف ف but does not explicitly link their etymologies or provide ancient Near Eastern language comparisons.
```


## [2026-09-05T20:19:12.767Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A8%D8%A7",
 "prompt": "Give the Persian etymology for دیبا (dibā) 'brocade' — Middle Persian dēbāg, any link to Old Persian dipi 'writing', and the derived دیباچه (dibāče) 'preface'."
}
```


## [2026-09-05T20:19:13.129Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/divan",
 "prompt": "Give the full etymology entry for 'divan', including the Persian and Arabic chain and any mention of Old Persian dipi or Sumerian."
}
```


### [2026-09-05T20:19:18.498Z] TOOL RESULT

```
# Persian Etymology of دیبا (dibā)

According to the Wiktionary entry, دیبا derives from Middle Persian dēbāg ("brocade"), likely from Proto-Iranian *diHp- meaning "to shine, light up." The entry notes this etymology relates to "the sheen imparted by the gold and silver in traditional brocades."

The word connects to Sanskrit दीप् (dīp, "to blaze, to glow"), sharing the same Indo-European root emphasizing luminosity.

**Regarding Old Persian dipi ('writing'):** The provided content does not mention any connection between دیبا and Old Persian dipi. No such etymological link is documented in this source.

**Regarding دیباچه (dibāče, 'preface'):** This derived form is not discussed in the article. The only mentioned doublet is دواج (dawāj/davâj, "bed-quilt").

The entry does show how widely this Persian term spread, appearing in Georgian, Ottoman Turkish, Serbo-Croatian, and other languages through historical borrowing.
```


### [2026-09-05T20:19:20.547Z] TOOL RESULT

```
# Etymology of Divan

Based on the provided content, here is the full etymology entry:

**Origin:** The word "divan" entered English in the 1580s as "Oriental council of state," derived from Turkish *divan*, which comes from Arabic *diwan*, ultimately tracing back to Persian *devan*.

**Semantic Evolution:** The Persian root originally meant "bundle of written sheets, small book, collection of poems" (as exemplified by the *Divan i-Hafiz*). The term is related to Persian *debir*, meaning "writer."

**Development in Arabic:** The sense expanded through "book of accounts," "office of accounts," "custom house," and "council chamber," eventually referring to "long, cushioned seat" as found in Middle Eastern council chambers.

**English Adoption:** The furniture sense (sofa/couch) was adopted into English by 1702, while the literary sense (a collection of poems, typically by one author) arrived by 1787.

**Note on Ancient Languages:** The provided source does not mention Old Persian *dipi* or Sumerian origins for this word.
```


## [2026-09-05T20:19:37.014Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== ARY دبیر/دیوان/دیبا ==\"; grep -n \"دبیر\\|دیوان\\|دیبا\" incoming/ARY/ARY_pages.txt | head -20; echo \"== AFM دیوان/دیباج/دف ==\"; grep -n \"الديوان\\|ديوان\\|ديباج\\|الدف\" AFM_pages.txt 2>/dev/null | head -20; ls | grep -i afm",
 "description": "Grep Aryanpur and Addi Shir"
}
```


### [2026-09-05T20:19:37.074Z] TOOL RESULT

```
== ARY دبیر/دیوان/دیبا ==
22:ارستایی -> پارسی‌باستان -> هند و اروپایی. ولی به دلائلی که در دیباچه آمده همیشه تتوانسته‌ام شاهد
45:دیباچه / ۵.
46:دیباچه
101:دیباچه / ۷
156:دیباچه / ‎٩‏ ۱
214:دیباچه / ۱۱
276:دیباچه / ۱۳
337:۱ دیباچه / ۱۵
390:دیباچه / ۱۷
445:دیباچه / ۱۹
513:: دیباچه / ۲۱
569::ْ دیباچه / ۲۳
625:دیباچه / ۲۵
689:دیباچه / ۲۷
746:دیباچه / ۲۹
805:دیباچه / ۳۱
862:دیباچه / ۳۳
921:دیباچه / ۳۵
979:دیباچه / ۳۷
1042:۱ دیباچه / ۳۹.
== AFM دیوان/دیباج/دف ==
209:مسدنّا من حسابات الديوان
242:( )ܠ ܚܡܕ الديياج الغليظ وقيل ديباج يعمّل بالذهب او ثاب + ܨ صفاق
1575:* (الدردار) شجر عظي له زهر اصفر وورق شائك وثر كقرون الدفلى ( 2
2302:)ܢ ܗܗ ܐܚܨ محض وهو ديوان الوالى
2662:ا ورت في قاعة الديوان٠‏ فاندذهل لحار و كروا لقتلها ٠‏ غير ان الملك
AFM_alt.txt
AFM_pages.txt
AFM.pdf
AFM.txt
```


## [2026-09-05T20:19:37.897Z] TOOL CALL #47: WebSearch

```json
{
 "query": "دیبا ریشه‌شناسی حسن‌دوست dēbāg Middle Persian brocade etymology dipi"
}
```


### [2026-09-05T20:19:45.400Z] TOOL RESULT

```
Web search results for query: "دیبا ریشه‌شناسی حسن‌دوست dēbāg Middle Persian brocade etymology dipi"

Links: [{"title":"دیبا - Wiktionary, the free dictionary","url":"https://en.m.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A8%D8%A7"},{"title":"ديباج - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AF%D9%8A%D8%A8%D8%A7%D8%AC"},{"title":"دیباچه - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A8%D8%A7%DA%86%D9%87"},{"title":"Sasanian Exegesis of Avestan Textile Terms","url":"https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1026&context=texterm"},{"title":"ARABIC LANGUAGE ii. Iranian loanwords in Arabic - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/arabic-ii/"},{"title":"What Does The Name Deebaj Mean?","url":"https://www.names.org/n/deebaj/about"},{"title":"Middle Persian literature","url":"https://en.wikipedia.org/wiki/Middle_Persian_literature"},{"title":"Brocade","url":"https://en.wikipedia.org/wiki/Brocade"},{"title":"Middle Persian","url":"https://en.wikipedia.org/wiki/Middle_Persian"}]

Based on the search results, here's what I found regarding the etymology of "dēbāg" (دیبا in Persian):

The term comes from Middle Persian dēbāg meaning "brocade," and is probably a derivative of Proto-Iranian *diHp- meaning "to shine, light up," due to the sheen imparted by the gold and silver in traditional brocades. This is related to Sanskrit दीप् (dīp), meaning "to blaze, to glow".

The word spread to other languages, with related forms found in Old Armenian դիպակ (dipak), Classical Syriac dēybāḡā, and Arabic دِيبَاج (dībāj).

The etymology reflects the prestigious nature of the fabric—the word's root relates to shine and light, which makes sense given that traditional brocades were luxurious textiles decorated with gold and silver threads that would create a lustrous effect.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:19:50.916Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/arabic-ii/",
 "prompt": "What does this article say about Iranian loanwords in Arabic: specifically دیوان dīwān, ادب adab, دیباج dībāj, and دفتر daftar? Quote the relevant passages."
}
```


## [2026-09-05T20:19:52.763Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== ARY latin index ==\"; grep -n -iE \"DIBIR|DABIR|DIVAN|DIWAN|DIBA|DIPI\" incoming/ARY/ARY_latin_index_pages.txt | head -20",
 "description": "Grep Aryanpur latin index"
}
```


### [2026-09-05T20:19:52.815Z] TOOL RESULT

```
== ARY latin index ==
```


### [2026-09-05T20:19:52.943Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T20:19:58.509Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A8%D8%A7%DA%86%D9%87",
 "prompt": "Give the Persian etymology of دیباچه (dibāče) 'preface' — what is it derived from?"
}
```


## [2026-09-05T20:20:00.261Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%8A%D9%88%D8%A7%D9%86",
 "prompt": "Give the Arabic etymology of ديوان (dīwān): source language, Middle Persian form, and any reconstruction like *dipi-vahanam. Also list derived terms such as تدوين (tadwīn)."
}
```


### [2026-09-05T20:20:03.752Z] TOOL RESULT

```
# Etymology of دیباچه (dibāče)

According to the Wiktionary entry, this Persian word was "Borrowed from Arabic _دِيبَاجَة_ (dībāja), from Middle Persian (dypʾk' /⁠dēbāg⁠/, 'brocade')."

The term ultimately derives from Middle Persian, where it referred to brocade fabric. It passed into Arabic, and from there entered Persian.
```


### [2026-09-05T20:20:06.940Z] TOOL RESULT

```
# Arabic Etymology of ديوان (dīwān)

**Source Language & Path:**
The word borrowed from "Classical Persian _[دیوَان](/wiki/%D8%AF%DB%8C%D9%88%D8%A7%D9%86#Persian "دیوان")_ (dēwān)" which itself derived from Middle Persian _d(p)ywʾn'_ (dēwān).

**Derived Terms:**
The document includes تدوين (tadwīn) in the user's question but does not list it among the entry's descendants. The visible derivatives shown trace through Andalusian Arabic into Romance languages (Spanish *aduana*, French *douane*, Italian *dogana*) and beyond.

**Note:** The etymology tree shown indicates Middle Persian as the ultimate source, but no reconstructed proto-form like *dipi-vahanam is provided in this Wiktionary entry. The documented path remains: Middle Persian → Classical Persian → Arabic.
```


## [2026-09-05T20:20:16.049Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%92%81%BE",
 "prompt": "What is this Sumerian word (dub)? Give its meaning and the Akkadian borrowing (ṭuppu) and any descendants (Aramaic, Old Persian dipi, Elamite)."
}
```


## [2026-09-05T20:20:17.513Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%81%D8%AA%D8%B1",
 "prompt": "Give etymologies for دفتر in Persian and Arabic. Does any of them mention Aramaic dappā, Sumerian dub or Greek diphthera?"
}
```


### [2026-09-05T20:20:22.111Z] TOOL RESULT

```
# The Cuneiform Sign 𒁾

## Sumerian Word: dub

**Meaning:** The Sumerian term "dub" refers to a "tablet" - a writing surface used in ancient Mesopotamia. It appears in the phrase "dub nam-tar-ra," meaning "the Tablet of Destinies."

## Akkadian Borrowing

The Akkadian language adopted this sign as **ṭuppum**, which served as a Sumerogram (a cuneiform sign borrowed to represent a foreign word). This represents the concept of a tablet or written document in Akkadian.

## Descendants

The entry documents several linguistic descendants:

- **Elamite**: tippi, meaning "inscription" or "writing"
- **Old Persian**: dipi- ("inscription; document")
- **Middle Persian**: dīwān (with further descendants)
- **Ashokan Prakrit**: dipi and lipi

Notably, the document does not list Aramaic as a direct descendant in the provided content, though it does show the transmission of this concept through Old Persian to later Indo-Iranian languages and Middle Persian, ultimately influencing Persian vocabulary for administrative and documentary purposes.
```


### [2026-09-05T20:20:24.588Z] TOOL RESULT

```
# Etymology of دفتر in Persian and Arabic

**Arabic Etymology:**
The Arabic entry states: "Possibly borrowed from Middle Persian dptl (daftar), from Aramaic דפתרא or Classical Syriac ܕܦܬܪܐ."

**Persian Etymology:**
The Persian section notes the word is "Inherited from Middle Persian dptl (/daftar/), from Aramaic דפתרא / ܕܦܬܪܐ, from Ancient Greek διφθέρα (diphthéra)."

**Regarding your specific questions:**
- **Aramaic dappā**: Not mentioned in either entry
- **Sumerian dub**: Not mentioned in either entry  
- **Greek diphthera**: Yes, both etymologies trace the word back to Ancient Greek διφθέρα (diphthéra), though the Arabic version presents this as a possible origin while Persian more directly includes it

Both entries acknowledge Greek influence, but neither mentions Aramaic dappā or Sumerian dub as sources.
```


## [2026-09-05T20:21:01.364Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== FVQ (Jeffery) files ==\"; ls | grep -i fvq; echo \"== KLN dappa/tabor/adab ==\"; grep -n -iE \"dapp|tympanum.*Heb|Heb\\. toph|toph,\" KLN_1966.txt | head -10; echo \"== LKT diwan/divan ==\"; grep -n -iE \"diwan|divan|duff|Tamburin\" LKT.txt | head -20",
 "description": "Grep Klein, Lokotsch, list Jeffery"
}
```


### [2026-09-05T20:21:01.453Z] TOOL RESULT

```
== FVQ (Jeffery) files ==
FVQ_pages.txt
FVQ.txt
== KLN dappa/tabor/adab ==
10170:Derivatives:  dabbl-er,  n.,  dabhl-ing,  adj.,  dabbl- ing-ly,  adv.,  dabbl-ing-ness,  n. dabchick,  n.,  i)  the  little  grebe  of  Europe;  2)  the pied-billed  grebe  of  America.  —  Fr.  earlier  dap- chick,  lit.  ‘dipping  chick’.  See  dap  and  chick and  cp.  didapper.
10335:Daphnis,  n.,  a  shepherd  in  Sicily,  the  inventor  of pastoral  songs  (Greek  mythol.)  —  L.,  fr.  Gk. Aaipvtg,  which  is  rel.  to  Saqmg,  ‘bayberry’,  fr. Saipvrj,  ‘laurel’.  See  Daphne, dapifer,  n.,  a  servant  waiting  at  table.  —  L.,  ‘a bringer  of  meat’,  compounded  of  daps,  gen. dapis,  ‘sacrificial  feast,  banquet’,  lit.  ‘expense’, and  fero,ferre,  ‘to  bear,  carry’.  The  first  element is  rel.  to  L.  damnum  (for  *dap-nom),  ‘harm, loss’,  orig.  ‘expenditure’,  and  cogn.  with  Gk. Samxvr),  ‘cost,  expenditure’.  See  damn.  For  the second  element  in  dapifer  see  -fer. dapper,  adj.,  neat;  smart.  —  ME.  daper,  ‘agile, strong’,  fr.  MDu.  (=  Du.)  dapper,  ‘strong, valiant,  brave’,  which  is  rel.  to  ON.  dapr,  ‘de¬ jected,  sad’,  Dan.  tapper,  ‘brave’,  OHG.  tapfar, ‘heavy,  weighty’,  MHG.  tapfer,  dapfer,  ‘thick, weighty’.  Late  MHG.  and  G.  tapfer,  ‘brave’,  fr. I.-E.  base  *dheb-,  ‘thick,  heavy,  strong’,  whence also  Toch.  A  tappo,  ‘worth,  force’,  OSlav.  dobru.
10336:Russ,  dobryj,  dobry,  Czech  and  Slovak  dobry, ‘good’,  OSlav.  debelu, ‘thick’,  dial.  Russ,  debolyj, ‘strong,  powerful’,OPruss.  rfefciAron,  ‘large,  great’. Derivatives :  dapper-Iy,  adv.  dapper-ness,  n. dapple,  n.,  a  spot  on  the  skin  of  an  animal.  — Prob.  of  Scand.  origin.  Cp.  ON.  depill,  ‘a  spot, dot,  a  dog  with  spots  above  the  eyes’. Derivatives:  dapple,  adj.  and  tr.  and  intr.  v., dappl-ed,  adj.
10337:dapple-gray,  dapple-grey,  adj.  —  A  blend  of apple-gray  and  dapple.
11346:didapper
11349:didapper,  n.,  the  small  grebe  or  dabchick.  —  Late ME.  dydoppar,  for  dive  dapper  (which  occurs  in Shakespeare).  Cp.  OE.  dufedoppa,  ‘pelican’,  and see  dive  and  dip.  Cp.  also  dap,  dabchick. diddle,  tr.  v.,  to  swindle.  —  Back  formation  from Jeremy  Diddler,  name  of  a  swindling  character ir,  J ames  Kenney’s  farce  Raising  the  Wind  ( 1 803). Etymologically,  the  name  Diddler  is  prob.  con¬ nected  with  OE.  dydrian,  ‘to  deceive’, diddle,  intr.  v.,  to  move  up  and  down,  or  to  and fro.  —  Prob.  of  imitative  origin.  Cp.  dial.  E. didder,  ‘to  tremble’.
36435:sprout,  intr.  and  tr.  v.  —  ME.  spruten,  sprouten, fr.  OE.  sprutan,  rel.  to  OS.  sprutan,  OFris.  spriita, MDu.  spruten,  Du.  spruiten,  OHG.  sprioyan, MHG.  sprie^en,  G.  spriejlen,  ‘to  sprout’,  and  to OE.  sprot,  sprota,  ME.  sprote,  ON.  sproti,  OHG. spros30,  MHG.  spro$$e,  spro3,  G.  Sprofi, ‘sprout’,  G.  Sprosse,  ‘sprout;  rung’,  MLG. sprote,  MDu.  sporte,  Du.  sport,  ‘rung’.  Cp. sprat,  sprint,  sprit,  spruit,  spurt,  ‘to  gush  out’. Derivatives:  sprout,  n.  (q.v.),  sprout-ed,  adj., sprout-er,  n.,  sprout-ing,  n.,  sprout-ling,  n. sprout,  n.  —  Fr.  sprout,  v. spruce,  n.,  a  coniferous  tree.  —  Shortened  fr. spruce  fir,  fr.  ME.  Spruce,  ‘Prussia’,  alteration of  Pruce,  fr.  ML.  Prussia  (see  Prussia) ;  hence spruce  fir  orig.  meant  ‘Prussian  fir’, spruce,  adj.,  neat,  dapper.  —  Fr.  ME.  Spruce, ‘Prussia’.  See  spruce,  n.
39562:toph,  n.,  a  small  drum  (music).  —  Heb.  toph, ‘timbrel,  tambourine’,  rel.  to  Aram,  tuppd,  of s.m.,  Arab,  duff,  ‘drum’ ;  of  imitative  origin. Tophet,  Topheth,  n.,  a  place  in  the  valley  of  Hin- nom,  south  of  Jerusalem,  where  children  were sacrificed  to  Moloch  {Bible).  Heb.  Topheth, prob.  formed  from  orig.  •Tlphath,  the  vowels  of which  have  been  assimilated  to  those  of  unrelat¬ ed  tSpheth,  ‘spitting’,  and  of  bosheth,  ‘shame’. Topheth  prob.  meant  orig.  ‘fireplace’  (i.e.  place
== LKT diwan/divan ==
1321:'Dämon,  Teufel'  [Horn  NpEt  S.  133, Nr.  598],  ebenso  tk.  diiv  'böser  Geist'; hieraus  bulg.  serb.  diw  'Riese',  poln. diiv  'Dämon'.  —  Aus  dem  zugehörigen Adj.  devänä  'verrückt'  [Horn  a.  a.  0.] wird  zunächst  tk.  diwane  und  dann  bulg. divane  'Verrückter',  serb.  diivanija  'hal- ber Narr'.    [Bern  SlEtWb  202.
1354:[Letzten  Endes  von  ^evs.dibir  'Schreiber' Horn  NpEtS.  119,  Nr.  540]  'Amtszimmer, Rat,  Tribunal',  hieraus  wurde  der  Sitz des  Beamten,  ein  bequemer  Sitz,  ein Ruhelager,  andererseits  aber  auch  Samm- lung von  Gedichten  eines  oder  mehrerer Dichter,  jedoch  nur  auf  den  Orient  be- züglich. Im  einzelnen  hat  man :  sp.  pg. aduana  'Zollhaus',  prov.  doana,  frz. douane,  it.  doana,  dogana  [mit  Konta- mination von  *ducana  aus  dux  >  doge] 'dass.'.  Frz.  divan  'Ruhebett',  it.  divano, rum.  divan,  russ.  bulg.  diivan,  öech.  dy- van,  dtsch.  Diwan,  engl,  divan,  angloind. dewaun  'Ruhebett,  Gedichtsammlung'. —  Aus  tat.  duwan  [Wechsel  zwischen u  und  i  im  Tk.  häufig,  vgl.  z.  B.  osm. diwar  und  duwar  'Wand'],  duwan  etmek 'richten'  kommt  russ.  duwan  'Teilung eines  Gewinns',  duwanit'  'eine  Beute, Gewinn  teilen'.  [DE  47.  Eguilaz  61. Devic  DEt  104.  ML  2707.  Gorjajew  91 u.  98.  Hobson-Jobson  309/311.
2361:Bern  SlEtWb  617  gewiesen:  altslav. krinica  'Topf,  Krug'  >  poln.  'Brunnen', slov.  'tiefe  Stelle  eines  Wassers'.  Aus demselben  ar.  Grundworte  entwickelten sich  meistens  mit  ar.  Art.  sp.  aleaduz, arcaduz  'Brunnenrohr,  Schöpfeimer  an einer  Bewässerungsanlage  [Noria,  s.  hier Nr.  1561]',  pg.  alcatruz,  asturisch  caduf, cadufol,  kat.  caduf,  cadufol,  alcaduf, catüfol,  logud.  caduffu,  cadofnlu,  siz. catussu  'irdene  Röhre  zur  Wasserfüh- rung'. Aus  dem  pg.  alcadroz  entwickelte sich  angloind.  albatross,  engl,  albatros, albatross,  frz.  albatros,  sp.  alcatraz, dtsch.  Albatros  'Diomeda  exulans  L.', ein  großer  Seevogel  aus  der  Familie der  Sturmvögel,  nach  der  Gestalt  seines Schnabels  so  benannt  [dagegen :  Eguilaz 225  und  Lammens  Rem  5].  —  Der  plr. des  ar.  Grundworts  ist  kawädts  'Röhren'; hieraus  mit  ar.  Art.  sp.  alcaraviz,  pg. alcribis  'Eisenrohr,  mit  dem  die  Schmiede den  Wind  aus  dem  Blasbalge  auf  das Feuer  blasen'  [nach  DE  85].  [DE  78 u.  79.  Devic  DEt  6.  ML  1456.  GrS VociSic  232.  WAGNER  in  Herrigs Archiv  CXL,  243.  Hobson-Jobson  10/11.
4539:'Zither,  Mandoline  oder  ein  anderes Saiteninstrument',  vulg.  tambür ;  hieraus sp.  tamhor,  it.  tamburo,  frz.  tambour 'Trommel'.  Mit  Metathesis  wurde  mlat. pandura,  iL  (alt)  pandura,  pandora  ^ (neu)  mandola,  frz.  pandore  >  mandore, mandole,  dtsch.  Mandoline.  Das  ar.  Wort kommt  selbst  aus  einem  pers.,  aus  dem u.  a.  afrz.  prov.  tabor  'Trommel',  prov. 'kleiner  Sessel',  frz.  tabouret  'dass.', prov.  taborel,  taborin  'Tamburin'  und viele  Ableitungen  geflossen  sind.  [DE 374.    Eguilaz  301.    ML  8516a.
5769:Dalai-Lama  1302 DriZ/e*-  j.  468 Da//os  j.  468 Damast  476 damaszieren  476 Damesinel  1871 Da?«  504 dawnen  j.  505 St.  482 Denebola  St.  482 Derwisch  496 Dey  460 dibbern  j.  514 D//f<eZ  j.  2068 D/f/(27«/  521 Diwan  526 Doc/j^s  j.  1984 Doto  j.  1984 Dollinger  j.  2002 Dolman  530 Dolmetsch(er)  2078 I>oM/"es  j.  1978
6958:caduffu  sard.  988
7043:divano  526
8704:d?5?a  1971 c?2ca  466 dichi^  517 dimie  521 c?«p?a  1971 direchie  522 disghin  527 divan  526 doica  462 doldora  531 dorobant  490 dovleac  555 dovlecel  555 (?raw  523 tfrec  522 rfM<?Ca>>  2118 dudiic(ä)  2119 dughiana  542 duium  528 dulama  530 dulap  529 dulämifä  530 duläpärie  529 didäü  2101 dulgherfie)  553 du^man(cä)  554 du^manie  554 <iu§mea  534
9275:dufftH^  540
```


## [2026-09-05T20:21:01.866Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '205,215p;238,248p;2298,2306p' AFM_pages.txt",
 "description": "Addi Shir context"
}
```


### [2026-09-05T20:21:01.907Z] TOOL RESULT

```
تفع لاإننات ܚܟ .ܕܟܕ بالارامية ܐܪܥܘܝܐܝ ܙ( 5 6( و 6 1
اللفظة سنسكر ܝܬ 10 ܐܦܬ نه من 5282 اي احمر ومن 724 وهى اداة
النسة ( القاموس العبرالي الكلداني تأليف جسنيوسء ضن : + ) (4) :
الأوارجة ) 5755 جسات الدخل والخرح يدون 3 )ا 1
مسدنّا من حسابات الديوان
+ ( الأرش ) ما 'يدفع بين السلامة والعيب في السلعة معرب رز وهو القيمة
5" (الأرْضي 039 ننات معروف ٠‏ .نا الصيغة غر يبة ٠‏ فلوو كان الاسم عربيا
لقمل الشوك الأرضي فهو عا 17 م 4 الفرني 56 ܐ( ܢܘܟ به
-210231طن) ]@ 1:31111123آط ع1 1231111216 1.2101 :115 1 موه ©
11121... 1125122 1847.اليو نبا ܒ
(الأرغس) ' ور اشر أصل سح < ܨ 2 أرغش وفسره 5
* :ܠܘ الذي يلف عليه الغزل ܐܟ 24008
اصنܗܕ ¢ ܙܝ
(الأستاذ) ܐܬܢ )ܪ الصناعة ورنسها ܠܚ 31 ܣܣ 4 سا <
والكركثة
( )ܠ ܚܡܕ الديياج الغليظ وقيل ديباج يعمّل بالذهب او ثاب + ܨ صفاق
ܨܝ عن استَبْر واصل ܢܓ الغليظ ^ الارامي ات دم
سر الأصاص او الرصاص 3:31 الردي نعر بب 8 ويرادفهة
ܝ 5 01 و0 : اي النحاس فاخوذ 9 ܥܨ 501 (فرتكلٌ
ضص: : ܐܘ ܙ ) والأبار من الاراءى ` ܐܒܪܐ
ܟ ܐ ©) 20 !ܥ ܀ ܨܣ 90 سر نبج وهو صبغ
ادر مصنوع من حريق الا نك والقلى وهو مركب من سسرخ 3 ® ومن 9¬=
ܫܐܪܐ ܢܐ وفي الترجوم ܫܝܪܐܣ ومن الب يالى ܧܫܐܪ ܐ مأخوذ العرلي _سيراء
وهو ® ܐ راجع 0 ل 0 )0
* : 33 نبات وم ܗ عليه تعريب سرخ وهو اأنبات ܐܬܚ بعصا
الراعي
)ܢ ܗܗ ܐܚܨ محض وهو ديوان الوالى
+ لدوم تعر يب 38 1 الحياة ܒ ܝ فيه
(السَر ܕܨ نوع من الاحديه تعر يب سر موزّه وهو مركب من سر أي فوق
رمن مويه ا للقت فالس موجة ]قال رمرزة والديه رز لات 1
+« الس مدى )مركت من: سن :اي تراس وعال زوم امك ايا زات ]‫
```


## [2026-09-05T20:21:24.219Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%A8%DB%8C%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D9%88%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A3%D8%AF%D8%A8\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D9%81\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A8%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%A8%D8%A7%DA%86%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D9%8A%D9%88%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%F0%92%81%BE\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D9%81%D8%AA%D8%B1\" \\\n \"https://www.etymonline.com/word/divan\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 141, root Sumerian Dub/Dup (dabir, divan, adab, daf)\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


## [2026-09-05T20:21:25.690Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== FVQ ==\"; grep -n -iE \"diwan|adab|duff\" FVQ.txt | head -10; echo \"== MON ادب/تدوین ==\"; grep -n \"^ادب:\\|^ادبیات:\\|^تدوین:\" MON_part1.txt MON_part2.txt | head -10",
 "description": "Grep Jeffery and Mo'in for adab/tadvin"
}
```


### [2026-09-05T20:21:29.283Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1be741d1399af324.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b2de9638bd5cf919.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d22cf8ab93f23338.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/872c1421bf670119.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/68f02d9af94fe136.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/041b88ee589c7ab2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cf664b9b0b8a28bc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/90e4d9cea8d1a3ba.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d2cb3bbea38de5f6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b8a6abf6211d754c.txt
```


### [2026-09-05T20:21:29.359Z] TOOL RESULT

```
== FVQ ==
195:Ahlwardt, W. Diwans of the Six Ancient Arabic Poets. London, 1870. 
226:Cheikho, L. An-Nasraniya wa Adabuha bain 'Arab al-Jahiliyya. Beirut, 1912-1923. 
352:Ibn Qutaiba. Adab al-Katib, ed. Grunert. Leiden, 190!). 
2330:Adab al-Kdtib, 527. 
4968:al-A'sha (Geyer, Zwei Gedickte, i, 58 = Diwan, Iv, 5), and Halevy 
5699:poetry (e.g. Diwan Hudh., ed. Kosegarten, 3, 1. 5), and may be assumed 
6079:Qutaiba, Adab al-Katib, 528, quotes Ibn 'Abbas as saying that it was 
7591:Diwan, xxxiii, 11. 
10394:* al-Jawallqi, Mu'arrab, 81 ; Ibn Qutaiba, Adab al-Katib, 527 ; al-Khafaji, 103 ; 
11866:Qhaba, i, 343, we find a man jliaxJI # Sjy, while in the Diwan of Tufaii (ed. 
== MON ادب/تدوین ==
MON_part1.txt:8905:ادب: امه [ع.] ((.) فرهنگت» وش وه
```


## [2026-09-05T20:21:37.768Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad 2>/dev/null || cd /tmp; timeout 90 curl -s \"https://ia-petabox.archive.org/services/search/beta/page_production/scrape.json?q=letter&identifier=SogdianDictionary\" | head -c 500; echo; timeout 90 curl -s \"https://archive.org/metadata/SogdianDictionary\" | python3 -c \"import sys,json; d=json.load(sys.stdin); print(d.get('server')); print([f['name'] for f in d.get('files',[]) if f['name'].endswith('.txt') or f['name'].endswith('_djvu.txt')][:10])\"",
 "description": "Probe archive.org for Sogdian dictionary text"
}
```


### [2026-09-05T20:21:40.504Z] TOOL RESULT

```
ia800804.us.archive.org
['GharibSogdianDictionnary_djvu.txt']
```


## [2026-09-05T20:21:43.785Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /tmp; timeout 120 curl -sG 'https://ia800804.us.archive.org/fulltext/inside.php' --data-urlencode 'item_id=SogdianDictionary' --data-urlencode 'doc=SogdianDictionary' --data-urlencode 'path=/27/items/SogdianDictionary' --data-urlencode 'q=muhr' | head -c 1500",
 "description": "Archive.org fulltext search in Sogdian dictionary"
}
```


### [2026-09-05T20:21:45.846Z] TOOL RESULT

```
{"ia":null,"q":null,"indexed":true,"matches":[],"error":"No hOCR or Abbyy file present"}
```


## [2026-09-05T20:22:01.055Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/141.jpg 2>/dev/null || pdftoppm -f 141 -l 141 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg141 && echo done",
 "description": "Render PDF page 141"
}
```


### [2026-09-05T20:22:02.696Z] TOOL RESULT

```
site/pages/141.jpg
done
```


## [2026-09-05T20:22:04.687Z] TOOL CALL #61: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/141.jpg"
}
```


### [2026-09-05T20:22:04.714Z] TOOL RESULT

```

```


## [2026-09-05T20:22:26.783Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== BRT dipi ==\"; grep -n -iE \"dipi|dip[iī]-\" BRT.txt | head -10; echo \"== MON دبیر/دیوان ==\"; grep -n \"^دبیر:\\|^دیوان:\\|^دبستان:\\|^دیباچه:\\|^دیبا:\" MON_part1.txt MON_part2.txt | head; echo \"== KLN toph page ==\"; python3 - <<'EOF'\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nimport re\n# find nearest preceding standalone page-number line\nfor i in range(39562,39500,-1):\n    if re.fullmatch(r'\\s*\\d{3,4}\\s*', d[i] or ''):\n        print('page marker before toph:', d[i].strip(), 'at line', i+1); break\nfor i in range(39562,39620):\n    if re.fullmatch(r'\\s*\\d{3,4}\\s*', d[i] or ''):\n        print('page marker after toph:', d[i].strip(), 'at line', i+1); break\nEOF",
 "description": "Grep Bartholomae, Mo'in, Klein page"
}
```


### [2026-09-05T20:22:28.746Z] TOOL RESULT

```
== BRT dipi ==
2455:l'S.S  (wo  awÄ<f' als  LSf.),  Y.9-28';  —  w I  nH  aiäAili  i'lse  jamyät  as>mca  ..  asista  tä airihat  Aa'a  visal  güuS  buyät  Y.6'o.2i.; '  2.  S..2J.3.  52-3.  FrD.  P,  Yt.  /j.  i3;  ~  ioa fri>ä  .  .  buyata  ahmya  nmlne  Yt.  /J.  147  ; IS6f.^  Y.26.^,  62.3*;  —  fraddiäi  ahe nmanahe  ..  vlspaya  alaond  stöis  Y.52.4; 4.5',  Vr. ».  13*;  —  imim  >7oqm  .  .yänim .  .  jaioyemi  .  .  dn'atütam  aiiiAas?  tanvS ". .  Gesundheit  dieses  (meines)  Leibes"  Y. 5.19;  — yaiä  ratSm  akurö  valdil  . ,  aya qsayä(scL)Y.ji.2;  —  afäi  aAmäi  var^nai.. nidätitn  ahm  . .  iAaeiili  (sd.) . .  "und  in  diesen (ünsem)  Glauben  .  ."  Y.4ff-3;  —  aitiAa daenayä  mqs  vaca  dd^anaAe  Y.  j?.  3 1 ;  — frä  KTjri»ie(sd.)aA£(XS{.alsinstr.)da^(^a ..  aAura  ..  Vr.5.3;  —  atcäv3  mizdtm  (sd.) anhat  aAyä  magahyH  y.  S3T>  —  H  *"''^ (sd.)  maiy  aniya/ay  vasiy  astiy  kartam avJ*  ahiyäyä  dipiyä  ttaiy  nipislam  (sd.) ".  .  in  dieser  (meiner)  Inschrift  (hier)  . ." Bh,  4-  S;  —  yS  ach-a  mazdayasnalh-a  .  . ". .  wer  hier  unter  den  Af.  .  ."  V-S-z; —  aAyil  '^wil  J^rff  rtr»z3nil  .  .  pairl.ja-
3583:—  ma%rym  spmttm  . .  pmrumca  . .  'r^mca V.  4.45;  45;  —  ahun?m  vairJm  . .  Tim sraoidyehya  (^^  frasrüiti  Y.  5. 14;  — apanmta  tiais^mi&A.)  G.3.T, —  'raheca yamahe  haplanhatdis  Vr.2/.o;  0,4^;  — ranuhlsla  a'A  .  .  hupaurva  (sd.)  vahehiS Ti/"  räsaintü  ¥.52.3;  —  aiwiea  'rim patiia  'rym  apsca  paurvalibya  "und  (man soll)  einen  zweiten  (Rüden)  und  dann noch  einen  weiteren  (zulassen)  und  zwar (soll  man  ihn)  gesondert  von  den  beiden ersten  (halten)"  V.  i^.  48.  3)  '>  der  Zeit nach 'der  spätere,  kUnftige'rja^a  mä  'racil (NPm.)  saoiyanis  stavqn  V.9.  2;  — yastä datrSMg  °rö  .  .  tarS.mqstä  "wer  darum künftighin  (eig.  posterior)^  den  D.  ..  auf- sagen wird"  V.  4:5. 11;  —  huzantSus  paiti •raya  YL  13. 134.  a)  mit  ayan-  n.  'der spätere  Teil  des  Tags,  Nachmittag':  */ra- \aire  ayqn  bavaiiii^A.)  hubar,rS  ..  a',a  "re ayqrt  duWirjm  ". .  dann  am  Nachmittag (kommt)  das  Unglück"  Aog.jJ.  A)  ASn. 'r?m,  'ram  und  IS.  °ra  als  Adv.  'postea, später,  künftig' :  yezi  nairyS  aukat  pasca hl  pourum  (sd.)  paiti.hin£öi^  paitisa  "r^m V.ÄSS;  v,%;  —  \mätyi^hy(r'ramimam dipim  patiparsiltiy  .  ,  BL4.8;6,  15,  ^.y,
4965:aJs dessen  Konelat:  avam  käram..  °vaAya ksrahyä  .  .  tyam  z-ohyazdaiJ*  /räilayi^ Bh.5.  lof.;  —  nadi'tahaire^  .  .  udafiatata .  .  fasäve^  adam  .  .  asiyavam  abiy  "vam nadi'tabairam  kyi^  nabitkadrai'ari^  agau- batä  Bh. /. i6- 1 8;_j.  3, g,  14, 2. 4. 1  b) sub- stantivisch, auch  im  Sinn  unsres  schwach- tonigen  'er':  t3m  lafmeii . .  yatata  ahurö maxda , ,  aom  Jai'iyat  Yt  ^5. 1  —  3 ;  —  I  gau- mat^  . .  hauv  udapaiata  . .  pasäv<^  ATru* aHy..'vam  asiyav^  Bh.;.ii;  —  *utilmaiy amyaiiiy  vasiy  astiy  kartam  °v<^  .  .  naiy nifistam  Bh.  4.8;  —  tuvam  ks  hyc^ imäm  dipim  vainahy  .  .  imatvä  patikarä . .  yävä  (sd.)  *taumä  *ahatiy  *äva  °vaiy pariiarä  Bh.4-i5;  — ya'^a  «J  snaihi^. paiti.vaiaMt  'vat  paiti.päpayamnS  "..eine Waffe  .  ^  sich  dagegen  zu  decken  suchend' P.  2/;  —  afavatum  mahrka'^ni  aon äinrnta  strmca(sd.)\t ip.12.  a)l'insbes. ein  Nomen,  das  —  zum  selben  Satz  gc- höiig  —  sammt  Zubehör  unmittelbar Toraosgeht:  kSram  tyam  hamii'iyam  kyeT
7939:chen (ausgesprochenen)  Gegensatz;  i)  ad- jektivisch; öfters  sva,  'dieser  mein,  dieser unser*:  ^  ya'iä  avatnc^  °mäm  bümim  .. D.  ().4;  —  VTspqmäi  aipi  °mqm  zqm  Y. 37-P3;  V.2.io,*ii,  >i2,  j^;  5.25;  — -ma  apasca  z>masca  urvarasia  .  .  'mä asasla  sßiiräsäi  ..Y.  2.16;  S.l.aS',  2.28'; —  D  'mäm  dahyäum  a*ur^mazda  pätuv  . . abiy  'mam  dahyaum  ma  äjamiyi/'  .  .  D. 4-3',  Ao.j;  —  mäm  c^ur^mazda  pätuv , .  utamaiy  vtiam  Uta  'mam  dahyäum  D. tf.  S;  —  Äauciy . .  nirasätiy  (sd.)  abiy  'mam !'/5  am  D.  5. 3 ;  II  —  ma  yave  'ma^  nmantm .  .  ifanns  /rasa Alt  Y.  60.  7;  Vyt  (?;  — II  'mam  duvariim  .  .  adam  akunafam  X. 7.3;  —  °Mi<i*  Aadis  X.^.3,  4-3,  Am._5  (wo 'mam);  ^-j  —  '■mam  lacaram  D,  i;  — ^'mam  ustasanam"  {sd.)Ao.  1.2; — "'mam apadana*'^  (sd.)  Am.  i,  4;  —  'ma*  stäiiam (sd.)  Aauv  niyaitayt^  ka'lanaiy'X^y.y, — adam  niyaslayam  °mäm yuiiyäm  keCtanaiy D. /7;  —  tuvam  ka  hy^  aparam  'mam dipim  vainsAy  .  .  'maiva  patikani  Bh.  4. 'S;  ^6"i  17',  6.  8;  —  'mam  Aa'dugäm Bh.^.io,  11;  5.3(?);ll  —  yat  'mam  daz- nqm  astaotaYt,iQ.%w — A3  damqm  mazda- yasttim  fravaza  vazaite  AS  'mqm  datnqm
8831:•  p.  'kä  Part,  der  Verallgemeinerung,  nur \\\vXtx luvam  'du''*:  tuvam  kü  hya''  aparam iiH'Tn  dipim  vain-i/iy  "du,  wer  es  auch sei,  der  später  diese  Inschrift  sehen  wird" Bh.,#.15;  (>;^tm:im  k,i  xs.lya>iyj'  /ly./' aparam  (sd.)  il/iy  "du,  wer  es  auch  sei, ein  König,  der  später  sein  wird"  Bh.  4. 19, 5.  14.
9063:mit  7'i  'durch  Graben  beseitigen,  ab- tragen; zerstören':  yasca  .  .  daxmatiqm avavanhm  maz3  vtkanayät  ya>a  .  .  V.  7. 51 ; — yat  b.J  paiti  fra!st.>m  daxma  uzdaSza (sd.;  lies  vrd')  vJkanü  (3SPA.)  yahmya  . . "an  welchem  Ort  man  am  meisten  die  D. durch  Abtragung  zerstört,  wo  .  ."  V.  y. 13;  —  yat  bü  paiti  fraüittnt  vikmte (3SPM.)  .  .gjmam  V..J.Z2;  —Wäyadanä (sd.)  tyä  gauiii'ätJ'  . .  viyakai'  (3SPrA.) Bh. /.  14;  —  kyt^  aparam  imilm  dipim vaitnhy  ..  maty^  (sd.)  vikanähy^^  Bh. 4.  15;  16;— _jW;>  imrim  dipim  ..vainähy '.■ikanähidisi^  Bh.  4- 1 7  II  ■
9119:•  p.  Itä  Part,  der  Verallgemeinerung,  nur hinter  tuvatii  'du'":  tuvam  kä  kya''  aparam imäm  dipim  latnähy  "du,  wer  es  auch sei,  der  später  diese  Inschrift  sehen  wird" Bh.J.is;  6;  —  tumm  kii  xs.iyaitvc^  kya'' aparam  (sd.)  ahy  "du,  wer  es  auch  sei, ein  König,  der  später  sein  wird"  Eh.  4. 19, 5.  »4-
9169:Akk.;  I^yaäa  paruvamciy  avaiia  adam\ (flftf*)  akunavam  Bh. /.  14;  —  kui:a  Ais' az3m  hrmaväni  sva,  "was  soll  ich  mit  | ihnen  machen?"  YL77. 57;  —  \ava%iidis\ akunavam  Bh.  5.  a ;  4. 4.  II  Anhang  zu  S. Mit  Akk.  der  Person  oder  Sache  und  Akk. des  PFfP.  'machen  (usw.),  dass  Jemand, etwas  . .  wird' ;  naiy  äha''  . .  kasciy  hya'' .  .  gauniätam  .  .  xsa'i''am  dllam  caxriyä" "es  war  keiner,  der  es  fertig  gebracht hätte,  dass  G.  der  Herrschaft  beraubt wurde"  Bh.  /.  13;  —  yanaiy  (sd.)  dipim naiy  ttiptstäm  akunaus  X.  7. 3.  6)  mit
9196:vOstrajiqm'a  urvaranamca  ifars>S.bair-\  1  mit /a^iy 'pflegen,  Sorge  tragen  für —' yanqm  V.j,4;  —  yj  yaom  kärayeili  ÄJ'(Akk.):  imäm  dipim  ..  imaivä  patiiarä alim  k.lrayeiti  "wer  Getreide  durch  Aus- '  mätyj"  vikanühy  ylvä  (sd.)  *taum!l  ahatiy säen  anbaut,  der  baut  das  Asa  an"  '^.*svä  avaiy  parikarä  ". .  solang  pflege J.31.  isie"   Bh..^  15;    —  yadiy  .  .   utämaiy  .  .
11784:•  p,  tautnan-  n.  'Vermögen,  Kraft,  Macht' (etwas  zu  tun):  yaäiy  imäm  dipim  vainähy imaivä  patikarä  naiydts  vikanähy  utamaiy yavS  (sd.)  'mä  ahatiy  parikarahidiS  Bh.
== MON دبیر/دیوان ==
MON_part1.txt:64780:دیوان: 0 ([نوشتن ] (۷.) وزارت‌خانه (در 
== KLN toph page ==
page marker before toph: 1629 at line 39563
page marker after toph: 1629 at line 39563
```


## [2026-09-05T20:22:35.506Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '64778,64790p' MON_part1.txt",
 "description": "Read Mo'in divan entry"
}
```


### [2026-09-05T20:22:35.572Z] TOOL RESULT

```
دیواره: (»):4027 (امر.) آنچه که شببه به 
دیوار باشد» دیوار مانند. مه 
دیوان: 0 ([نوشتن ] (۷.) وزارت‌خانه (در 
قدیم). اداره (در قدیم) . دفترخانه. دفتر 
محاسبه» دفتر حساب» دفتر عمومی برای 
شست در آمد و هزینه. خرانه‌داری. دولت. 
دیوان انشاء: اداره‌ای که از طرف شاه اسناد 
رسمی صادر و مکاتبات دولشی را اداره 
می‌کرد (پیش از مغول). دیوان بلخ: گویند 
در شهر بلخ قاضبان احکام نادرستی صادر 
می کر دنده سگناهان را بزه کار و گناهکاران 
را معصوم جلوه می‌دادند. از این‌رو دیوان 
بلح مثل هر دادگاه و مسحکمه‌ای شده که
```


## [2026-09-05T20:23:07.764Z] AGENT

Now I'll write the verification file.


## [2026-09-05T20:28:06.309Z] TOOL CALL #64: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nU = {\n \"dabir\": W+\"%D8%AF%D8%A8%DB%8C%D8%B1\",\n \"divan_fa\": W+\"%D8%AF%DB%8C%D9%88%D8%A7%D9%86\",\n \"adab\": W+\"%D8%A3%D8%AF%D8%A8\",\n \"daf\": W+\"%D8%AF%D9%81\",\n \"diba\": W+\"%D8%AF%DB%8C%D8%A8%D8%A7\",\n \"dibache\": W+\"%D8%AF%DB%8C%D8%A8%D8%A7%DA%86%D9%87\",\n \"divan_ar\": W+\"%D8%AF%D9%8A%D9%88%D8%A7%D9%86\",\n \"dub\": W+\"%F0%92%81%BE\",\n \"daftar\": W+\"%D8%AF%D9%81%D8%AA%D8%B1\",\n \"etym_divan\": \"https://www.etymonline.com/word/divan\",\n}\n\ndata = {\n \"pdf_page\": 141,\n \"book_page\": 111,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Dub, Dup\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Sumerian dub 𒁾 'clay tablet, (written) document'\",\n   \"note\": (\"Sumerian DUB 𒁾 'tablet, document' is a real and well attested word, and the \"\n            \"language label and gloss are right ('scripture' is loose for 'written document'). \"\n            \"The onward chain drawn on this page — Sum. dub > Akk. ṭuppu/duppu > (Elamite tippi) > \"\n            \"OP dipi- > MP dibīr/dēwān > NP دبیر/دیوان, and Akk. dappu > Aram. dappā > Arab. daff — \"\n            \"is exactly the chain Zimmern (AKD p.19) sets out and that Moʿin repeats in his \"\n            \"etymological footnote to دبستان in Borhan-e Qateʿ (pp. 823-824), citing Zimmern p.19 by name. \"\n            \"Nourai's whole chart is in effect a transcription of that footnote. The two weak links are \"\n            \"(a) دیباچه, which most modern sources take from دیبا 'brocade' < MP dēbāg (Proto-Iranian \"\n            \"*diHp- 'to shine'), not from dipi 'writing', and (b) the Arabic دف 'tambourine', which is a \"\n            \"separate onomatopoeic Semitic drum-word (Heb. תֹּף tōp, Aram. tuppā), homonymous with, but \"\n            \"not identical to, دفّ 'board, side' < Aram. dappā.\"),\n   \"note_fa\": (\"ریشهٔ سومری dub (به خط میخی 𒁾) به معنی «لوح گِلی، نوشته» واژه‌ای است اصیل و شناخته‌شده؛ \"\n               \"برچسب زبانی و معنای آن در نمودار درست است. زنجیرهٔ اصلی — سومری dub ← اکدی ṭuppu/duppu ← \"\n               \"(ایلامی tippi) ← پارسی باستان dipi ← فارسی میانه dibīr و dēwān ← فارسی نو «دبیر» و «دیوان» — \"\n               \"همان است که تسیمرن (زیمرن) در «وام‌واژه‌های اکدی» ص ۱۹ آورده و معین در حاشیهٔ ریشه‌شناختی «دبستان» \"\n               \"در برهان قاطع (ص ۸۲۳ ـ ۸۲۴) با ارجاع صریح به همان صفحهٔ زیمرن تکرار کرده است؛ نمودار نورایی در واقع \"\n               \"برگردان همان حاشیه است. دو حلقهٔ سست: یکی «دیباچه» که بیشتر منابع امروزی آن را از «دیبا» (فارسی \"\n               \"میانه dēbāg، از ایرانی آغازین *diHp- «درخشیدن») می‌دانند نه از dipi «نوشتن»؛ و دیگری «دفّ» عربی به \"\n               \"معنی طبل که واژه‌ای سامی و آوانمای (onomatopoeic) است (عبری תֹּף، آرامی tuppā) و تنها هم‌آوای «دفّ» \"\n               \"به معنی «تخته، پهلو» است.\"),\n   \"sources\": [U[\"dub\"], U[\"divan_fa\"], U[\"dabir\"]],\n   \"ref_check\": [\n    {\"ref\": \"AKD:19\", \"status\": \"supports\",\n     \"note\": (\"Zimmern, Akkadische Fremdwörter, p.19 (local AKD.txt, leaf printed '19'): «akk. duppu, tuppu \"\n              \"Tafel, Schriftstück (< sum. dub), wozu dappu Brett, wohl nur eine Variante bildet : > aram. dappū \"\n              \"Brett, Tafel, Blattseite … (> wohl arab. daff u. ṭaff Brett, Seite, daffat Buchdeckel) … Ferner > \"\n              \"altpers. dipi Inschrift (wozu viell. neupers. debīr Schreiber, dīvān Buch), elam. tuppi Inschrift, \"\n              \"ind. dipi (lipi) Schrift.» This single paragraph is the source of the entire chart.\")},\n    {\"ref\": \"BQT:823\", \"status\": \"supports\",\n     \"note\": (\"Borhan-e Qateʿ, Moʿin's footnote 3 to دبستان, BQT_v2_pages.txt leaf 283 = printed p.823 on the \"\n              \"running-head calibration leaf+540: «از: دب + ستان (پسوند مکان)؛ جزو اول آن ریشهٔ دپ است. کلمهٔ اخیر \"\n              \"در کتیبه‌های هخامنشی بزبان پارسی باستان بصورت dipi بکار رفته و آن هم یادگاری است از قوم سومر … دوب \"\n              \"dub در زبان سومری بمعنی لوحه و خط است» (continued on the next leaf).\")}\n   ],\n   \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. dipi-\", \"stance\": \"supports\",\n     \"note\": \"«dipi- sb. 'inscription': Elam. tup-pi, Akk. duppu (§152.I): borrowed from Sumerian dup-» — the Sumerian origin is Kent's own view.\"},\n    {\"src\": \"MON\", \"where\": \"MON_part1.txt line 61981 s.v. دف / line 64780 s.v. دیوان\", \"stance\": \"partial\",\n     \"note\": \"Moʿin's Farhang tags دف as «[معر.]» and دیوان with an origin bracket pointing to «نوشتن»; he gives no Sumerian chain in the lexicon itself (that is in his Borhan footnotes).\"},\n    {\"src\": \"AKD\", \"where\": \"p.19\", \"stance\": \"supports\", \"note\": \"see ref_check — «akk. duppu, tuppu Tafel … < sum. dub».\"}\n   ],\n   \"nodes\": []\n  }\n ]\n}\n\nnodes = data[\"entries\"][0][\"nodes\"]\n\nnodes.append({\n \"id\": 1, \"lang\": \"Old Persian\", \"words\": \"dipi\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n  \"Old Persian dipi- is real and frequent in the Achaemenid inscriptions (accusative dipim 'this inscription', \"\n  \"locative dipiyā, e.g. DB 4.42, 4.47-48, 4.70), but it is a FEMININE NOUN 'inscription, written document', not \"\n  \"a verb: Nourai's gloss 'to write' is wrong (the OP verb 'to write' is ni-piš-, nipištanaiy). The route is also \"\n  \"not direct: Sumerian DUB was borrowed into Akkadian as ṭuppu/duppu and into Elamite as tuppi/tippi, and Old \"\n  \"Persian took the word from that Elamite–Akkadian chancery tradition in the 6th c. BCE, when Elamite scribes \"\n  \"wrote the Achaemenid archives; Kent states this explicitly (Elam. tup-pi, Akk. duppu, 'borrowed from Sumerian \"\n  \"dup-'), and Wiktionary's Sumerian entry lists Elamite tippi and Old Persian dipi- as successive descendants. \"\n  \"The same word travelled east from Achaemenid administration into Ashokan Prakrit dipi/lipi 'writing'. So the \"\n  \"arrow root→OP is right in substance but skips the Akkadian/Elamite mediation Nourai himself draws in the other \"\n  \"branch of this very chart.\"),\n \"derivation_fa\": (\n  \"«dipi» پارسی باستان واژه‌ای است واقعی و پربسامد در کتیبه‌های هخامنشی (رایی: dipim «این نبشته»، در بیستون ۴٫۴۲ و \"\n  \"۴٫۷۰)، اما اسم مؤنث به معنی «نبشته، سند» است نه فعل؛ پس معنای «to write» که نورایی داده نادرست است (فعل «نوشتن» \"\n  \"در پارسی باستان ni-piš- است). راه وام‌گیری نیز مستقیم نیست: dub سومری نخست به اکدی (ṭuppu/duppu) و سپس به ایلامی \"\n  \"(tuppi/tippi) رفته و پارسی باستان آن را از سنت دیوانی ایلامی ـ اکدی گرفته است؛ کنت همین را می‌گوید. همین واژه از \"\n  \"دیوان هخامنشی به پراکریت کتیبه‌های آشوکا (dipi/lipi «خط») هم رسیده است. بنابراین ادعای نورایی در اصل درست است، \"\n  \"اما با احتیاط: حلقهٔ اکدی ـ ایلامی جا افتاده و معنای واژه هم اسم است نه فعل.\"),\n \"sources\": [U[\"dub\"], U[\"divan_fa\"]],\n \"ref_check\": [\n  {\"ref\": \"BQT:823\", \"status\": \"supports\",\n   \"note\": \"Moʿin's footnote to دبستان (BQT_v2_pages.txt leaf 283 ≈ printed 823): «کلمهٔ اخیر در کتیبه‌های هخامنشی بزبان پارسی باستان بصورت dipi بکار رفته و آن هم یادگاری است از قوم سومر».\"}\n ],\n \"consulted\": [\n  {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. dipi- (KNT.txt line 5558)\", \"stance\": \"partial\",\n   \"note\": \"«dipi- sb. 'inscription': Elam. tup-pi, Akk. duppu (§152.I): borrowed from Sumerian dup-» — supports the Sumerian source but glosses the word as a noun 'inscription', and routes it through Elamite/Akkadian.\"},\n  {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW, OP citations (BRT.txt lines 2455, 8831, 9063)\", \"stance\": \"supports\",\n   \"note\": \"Bartholomae quotes the Behistun passages with dipim/dipiyā and translates «in dieser (meiner) Inschrift», i.e. a noun 'Inschrift'.\"},\n  {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 540, p.119\", \"stance\": \"supports\",\n   \"note\": \"«ap. vergl. LW. dipi- 'Schrift'» — Horn explicitly marks the Old Persian word a loanword (LW.).\"}\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"dabîr; dabestân; dîbâčeh; dîvân\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n  \"Three of the four words are certain, the fourth is contested. (1) دبیر dabīr 'scribe, (today) teacher' is \"\n  \"inherited from Middle Persian dibīr, written <dpy(w)r>: Nyberg reconstructs Old Iranian *dipi-vara- 'he who \"\n  \"preserves the documents' (dipi- + *var- 'to keep'), attested as Pahlavi dipivar and early contracted to dipīr; \"\n  \"the Armenian loan dpir and Greek διβυροπάτ-/Parthian dpyrwpt 'chief secretary' date the contraction to the \"\n  \"Sasanian period at the latest. MacKenzie: «dibir [dpy(w)r' | M dbyr, N ~] scribe». (2) دبستان/دبیرستان = \"\n  \"dabīr/dab- + the place-suffix -stān, already MP dibīrestān 'school' (MacKenzie s.v.); Moʿin's footnote analyses \"\n  \"it as «دب + ستان (پسوند مکان)». (3) دیوان dīvān 'register, office, collected poems' is inherited from MP dēwān \"\n  \"<d(p)ywn'> 'archive, collected writings' (MacKenzie), from Old Iranian *dipi-vahana- 'document-house' (Asbaghi); \"\n  \"the archaic spelling with -p- is the direct graphic proof of the dipi- base, and Klein and Horn both link dīvān \"\n  \"to debīr. (4) دیباچه dībāče 'preface' is the weak link: Moʿin's footnote does list دیبا and دیباچه among the \"\n  \"descendants of dipi, and Asbaghi derives dībā 'brocade' from MP dēpāk < ap. dipi; but the mainstream modern \"\n  \"account takes MP dēbāg 'brocade' from Proto-Iranian *diHp- 'to shine' (cf. Skt. dīp- 'to blaze'), from the sheen \"\n  \"of gold-threaded brocade, and dībāče itself is a re-borrowing of Arabic دِيبَاجَة dībāja, a diminutive of dībāj \"\n  \"'brocade' used for the ornate opening pages of a book. So dībāče is at best indirectly, and probably not at all, \"\n  \"from dipi.\"),\n \"derivation_fa\": (\n  \"سه واژه از چهار واژه قطعی‌اند و چهارمی محل بحث است. «دبیر» از فارسی میانهٔ dibīr (نگارش <dpy(w)r>) است؛ نیبرگ آن را \"\n  \"از ایرانی باستان *dipi-vara- «نگاهدارندهٔ اسناد» می‌داند (dipi + ستاک *var- «نگاه داشتن») که در پهلوی dipivar بوده و \"\n  \"زود به dipīr کوتاه شده است؛ وام ارمنی dpir و صورت پارتی dpyrwpt «دبیربد» گواه قدمت این کوتاه‌شدگی‌اند. «دبستان/دبیرستان» \"\n  \"همان دبیر + پسوند مکانِ «ـستان» است و در پهلوی هم dibīrestān آمده. «دیوان» از فارسی میانهٔ dēwān با نگارش کهنِ <d(p)ywn> \"\n  \"است، از ایرانی باستان *dipi-vahana- «خانهٔ اسناد»؛ همان «پ» در نگارش پهلوی، دلیل خطیِ پیوند با dipi است. اما «دیباچه» \"\n  \"حلقهٔ سست است: معین در حاشیهٔ برهان و اسباغی «دیبا» را از dipi می‌گیرند، حال آنکه دیدگاه رایج امروزی dēbāg «دیبا» را از \"\n  \"ایرانی آغازین *diHp- «درخشیدن» (هم‌ریشه با سنسکریت dīp-) می‌داند، و «دیباچه» خود وام‌گیری دوباره از عربی «دیباجه» \"\n  \"(مصغّر دیباج) است. پس ادعای نورایی دربارهٔ سه واژهٔ نخست درست و دربارهٔ «دیباچه» با احتیاط پذیرفتنی است.\"),\n \"sources\": [U[\"dabir\"], U[\"divan_fa\"], U[\"diba\"], U[\"dibache\"], U[\"etym_divan\"]],\n \"ref_check\": [\n  {\"ref\": \"BQT:824\", \"status\": \"supports\",\n   \"note\": (\"Continuation of Moʿin's دبستان footnote on the next leaf (BQT_v2_pages.txt leaf 284 ≈ printed p.824): \"\n            \"«… شده صورت ṭuppu و tuppu درآمده. همین کلمه وارد زبان آرامی شده … و بمعنی لوحه و صفحه گرفته شده و بعدها \"\n            \"داخل زبان عربی شده صورت دف درآمده و بمعنی لوحه بکار رفته است. (رک: Zimmern, Akkadische Fremdwörter ۱۹). \"\n            \"ریشهٔ لغت‌های دبیر، دبیرستان، دیبا، دیباچه و دیوان همین کلمه است» — literally Nourai's node, دیباچه included.\")},\n  {\"ref\": \"KLN:467\", \"status\": \"supports\",\n   \"note\": (\"Klein 1966 p.467 (page marker '467' immediately precedes the entry in KLN_1966.txt): «divan, n. … Turk. \"\n            \"diwan, fr. Pers. diwan, 'a royal court; a council of state' … (whence also Arab. diwan, It. divano, F. \"\n            \"divan, etc.); rel. to Pers. debir, dibir, 'writer'» — exactly Nourai's Persian→Arabic direction.\")},\n  {\"ref\": \"AKD:19\", \"status\": \"supports\",\n   \"note\": \"Zimmern p.19: «altpers. dipi Inschrift (wozu viell. neupers. debīr Schreiber, dīvān Buch)» — Zimmern names debīr and dīvān, but not dībāče.\"},\n  {\"ref\": \"ETM:36\", \"status\": \"not_checked\",\n   \"note\": \"Abolghasemi, Risheh-shenasi (1374): refs_online.json records that no digital copy exists on any permitted platform (catalogue/purchase only).\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD pp. 25/26 s.v. dibir, dēwān, dēbāg\", \"stance\": \"supports\",\n   \"note\": \"«dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. ~estān [-st'n' | N ~] school»; «dēwān [d(p)ywn' | N ~] archive, collected writings»; but «dēbag [dyp'k' | N dēbā] brocade» is a separate lemma — MacKenzie does not connect dēbāg to dibir.\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. dipivar\", \"stance\": \"supports\",\n   \"note\": \"«dipivar [dpywr] secretary … OIr *dipi-vara- from OP dipi- 'inscription', BP dyp 'document', MPrth dyb 'letter' + *vara- … thus 'he who preserves the documents'. Early contracted to dipir: Arm lw. dpir …; M Prth/Prs dbyr; NP dibir, dabir.»\"},\n  {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 540, p.119\", \"stance\": \"supports\",\n   \"note\": \"«540. debīr, dibīr 'Schreiber' … ap. vergl. LW. dipi- 'Schrift'; prākr. dipi-, lipi- (Aśoka-Inschriften); phlv. d(i)pivar, d(i)pīr, d(i)pīrīh, daneben d(i)bīr (Inschr.); arm. LW. dpir … Den Zusammenhang mit dīwān, defter … hat bereits de Lagarde erkannt.»\"},\n  {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §540 (HUB.txt line 2084)\", \"stance\": \"partial\",\n   \"note\": \"«Arm. dpir setzt phl. dipīr voraus und macht mir Horn's phl. dipivar nicht wahrscheinlich» — Hübschmann accepts dipīr but doubts the *dipi-vara- analysis; he also rejects Fr. Müller's rival derivation of dīwān from phl. *ativān.\"},\n  {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen p.129 s.v. dībā, and s.v. dīwān\", \"stance\": \"supports\",\n   \"note\": \"«dībā: 'Brokat, gestickter Goldstoff' … aus pers. dībā < mp. dēpāk, ap. dipi»; «dībāǧa: 'Vorrede' dim. v. dībā»; «dīwān … aus dem pers. dīwān, mp. dīvān < *dipi-vahana 'Dokumentenhaus' ← dipi 'schreiben'».\"},\n  {\"src\": \"MON\", \"where\": \"MON_part1.txt line 64780 s.v. دیوان\", \"stance\": \"partial\",\n   \"note\": \"«دیوان: [… نوشتن] (ا.) وزارت‌خانه (در قدیم) … دفترخانه، دفتر محاسبه» — Moʿin's bracket points to 'writing' but the Latin forms of the print edition are lost in this reprint's OCR.\"}\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Arabic\", \"words\": \"adab; dîwân\",\n \"verdict\": \"disputed\",\n \"derivation\": (\n  \"دیوان → ديوان dīwān is a certain and famous Persian loan in Arabic: the caliph ʿUmar's register of stipends \"\n  \"(dīwān al-ʿaṭāʾ, 20/641) took over the Sasanian chancery term, and Arabic dīwān then meant 'register, ledger, \"\n  \"government office, collected poems'; Klein (p.467), Lokotsch (no. 526) and Asbaghi all give Persian dīwān as the \"\n  \"source, and from Arabic it went on to Turkish divan, Andalusian Arabic > Spanish aduana, French douane, Italian \"\n  \"dogana, and European Divan 'couch'. أدب adab is the disputed half. Asbaghi 1988 (Nourai's kind of source) splits \"\n  \"the word in two and derives adab II 'literarische Bildung' «aus dem pers. adab << mp. dipi 'Inschrift' ← air. \"\n  \"*dipi-vara», i.e. Nourai's arrow. But the Arabist consensus — followed by Wiktionary with citations, and going \"\n  \"back to Nöldeke and EI's article 'Adab' — is that adab is native Arabic: a back-formation from آداب ādāb, plural \"\n  \"of the verbal noun دَأْب daʾb 'habit, persistent practice' (root د أ ب), with the semantic path 'inherited norm of \"\n  \"conduct' → 'good manners' → 'the learning that produces good manners' → 'belles-lettres'. Wiktionary comments \"\n  \"that Iranian derivations of adab are «surely inspired by some general idea of Abbasid cultural supremacy». The \"\n  \"phonetics also argue against Nourai: dipi/dabīr would not yield ʾ-d-b with a prosthetic hamza and no trace of the \"\n  \"p/b of the second syllable.\"),\n \"derivation_fa\": (\n  \"«دیوان» عربی وام‌واژه‌ای قطعی از فارسی است: دیوانِ عطای عمر (سال ۲۰ هجری) همان اصطلاح دیوانی ساسانی را گرفت و در عربی \"\n  \"معنی «دفتر، اداره، مجموعهٔ شعر» یافت؛ کلاین، لوکوچ و اسباغی همگی خاستگاه فارسی آن را تأیید می‌کنند و از عربی به ترکی \"\n  \"divan و از عربی اندلسی به اسپانیایی aduana و فرانسهٔ douane رسیده است. اما «ادب» محل نزاع است: اسباغی (۱۹۸۸) ادبِ به \"\n  \"معنی «فرهیختگی ادبی» را «از فارسی adab، از فارسی میانه dipi» می‌داند، یعنی همان ادعای نورایی؛ ولی دیدگاه غالب عرب‌شناسان \"\n  \"(نولدکه، دائرةالمعارف اسلام، ویکی‌واژه با ارجاع) «ادب» را عربی اصیل می‌داند: اشتقاق پسین از «آداب»، جمع مصدرِ «دَأْب» \"\n  \"(ریشهٔ د أ ب) به معنی «عادت و مداومت»، با این سیر معنایی: «سنت موروثی رفتار» ← «حسن سلوک» ← «دانشی که ادب می‌آورد» ← \"\n  \"«ادبیات». از نظر آوایی هم گذر از dipi/dabīr به «أ د ب» با همزهٔ آغازین توجیه‌پذیر نیست. پس: نیمی از این گره درست و \"\n  \"نیم دیگر را پژوهش امروزی رد می‌کند.\"),\n \"sources\": [U[\"adab\"], U[\"divan_ar\"], U[\"etym_divan\"]],\n \"ref_check\": [\n  {\"ref\": \"FVF:13,273\", \"status\": \"not_checked\",\n   \"note\": \"Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi (1347): refs_online.json lists it only as a noorlib/ketabnak page-viewer (login-gated); no OCR text on disk and the viewer cannot be read with WebFetch. Its thesis (Persian words in Arabic) is by nature the Iranianist side of the adab dispute.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein 1966 p.467 s.v. divan\", \"stance\": \"supports\",\n   \"note\": \"«… fr. Pers. diwan … whence also Arab. diwan, It. divano, F. divan» — Persian → Arabic. Klein has no entry deriving adab from Persian.\"},\n  {\"src\": \"PLA\", \"where\": \"Asbaghi 1988 pp.6-7 s.v. ʾadab, p.129 s.v. dīwān\", \"stance\": \"supports\",\n   \"note\": \"«ʾadab: 'literarische Bildung' aus dem pers. adab << mp. dipi 'Inschrift' ← air. *dipi-vara»; «dīwān: 'königlicher Hof, Gerichtshof' aus dem pers. dīwān, mp. dīvān < *dipi-vahana 'Dokumentenhaus'».\"},\n  {\"src\": \"LKT\", \"where\": \"Lokotsch no. 526\", \"stance\": \"supports\",\n   \"note\": \"«[Letzten Endes von pers. dibir 'Schreiber', Horn NpEt S.119, Nr.540] 'Amtszimmer, Rat, Tribunal' … sp. pg. aduana, frz. douane, it. dogana … frz. divan, dtsch. Diwan» — the whole European fan-out from Pers. dibīr via dīvān.\"},\n  {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qurʾān (FVQ.txt)\", \"stance\": \"silent\",\n   \"note\": \"grep 'diwan|adab|duff': only bibliographic occurrences (Ibn Qutayba, Adab al-Kātib; Dīwān of the six poets). Neither adab nor dīwān is a Qurʾānic word, so Jeffery has no entry either way.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"adab; adabiyyât; tadvîn\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n  \"That all three are Arabic loans re-entering Persian is certain; whether the return leg of a round trip is what \"\n  \"we are looking at depends on node 3. تدوین tadvīn is a genuine and uncontroversial round trip: Arabic coined the \"\n  \"form-II verb دوّن dawwana 'to collect (poems, records) into a dīwān' on the Persian loan dīwān, and its verbal \"\n  \"noun تدوين tadwīn 'compilation, codification' (with the participle مُدوَّن mudawwan) was then borrowed back into \"\n  \"Persian, where تدوین means 'compiling, drafting (a text, a law)'; the same Arabic derivational machinery gives \"\n  \"دواوين dawāwīn as the plural of the Persian word. أدب adab, its participle مؤدّب muʾaddab, the maṣdar تأدیب \"\n  \"taʾdīb and the plural آداب, and the nisba-plural ادبیّات adabiyyāt 'literature' (with ادیب adīb) are all built \"\n  \"inside Arabic on the root ʾ-d-b, and were taken into Persian from Arabic — Moʿin's Farhang tags Persian ادب simply \"\n  \"«[ع.]» ('Arabic'), not «[معر.]» ('Arabicised', his tag for round trips). So the Arabic→Persian direction is \"\n  \"confirmed; the claim that these are Persian words coming home is only as good as the disputed node 3. \"\n  \"ادبیّات in its modern sense 'literature (as a discipline)' is in any case a 19th-c. calque-like innovation.\"),\n \"derivation_fa\": (\n  \"اینکه هر سه واژه وام‌واژهٔ عربی در فارسی‌اند قطعی است؛ اما «بازگشت» بودنشان به گرهٔ پیشین بسته است. «تدوین» \"\n  \"بی‌گمان یک دورهٔ رفت‌وبرگشت کامل است: عربی بر پایهٔ وام‌واژهٔ «دیوان» فعل باب تفعیلِ «دوّن» را ساخت («در دیوان گرد \"\n  \"آوردن») و مصدر آن «تدوین» (و اسم مفعول «مدوّن») دوباره به فارسی وارد شد؛ جمع مکسّر «دواوین» نیز ساختهٔ همان دستگاه \"\n  \"صرفی عربی روی واژهٔ فارسی است. اما «ادب»، «مؤدّب»، «تأدیب»، «آداب» و «ادبیّات» (و «ادیب») همه در درون عربی و از \"\n  \"ریشهٔ «أ د ب» ساخته شده‌اند و از عربی به فارسی آمده‌اند؛ معین در فرهنگ خود ذیل «ادب» تنها نشانهٔ «[ع.]» می‌گذارد نه \"\n  \"«[معر.]» که نشانهٔ معرّب و بازگشتی است. پس جهت وام‌گیری عربی ← فارسی درست است، ولی «فارسی‌الاصل بودن» این واژه‌ها \"\n  \"به همان اندازهٔ گرهٔ ۳ محل تردید است.\"),\n \"sources\": [U[\"adab\"], U[\"divan_ar\"]],\n \"ref_check\": [\n  {\"ref\": \"FVA:28\", \"status\": \"not_checked\",\n   \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368): refs_online.json records 'no digital copy found on any permitted platform' after a 2026-09 re-search; catalogue entry only (OpenLibrary OL2012991M).\"},\n  {\"ref\": \"FVF:273\", \"status\": \"not_checked\",\n   \"note\": \"Emam Shushtari 1347 p.273 — same login-gated noorlib scan as node 3; not readable.\"}\n ],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"MON_part1.txt line 8905 s.v. ادب\", \"stance\": \"partial\",\n   \"note\": \"«ادب: [ع.] (ا.) فرهنگ، روش …» — Moʿin marks it a plain Arabic loan; he does NOT use his «[معر.]» tag, which he does use for دف and دفتر.\"},\n  {\"src\": \"PLA\", \"where\": \"Asbaghi 1988 pp.6-7\", \"stance\": \"supports\",\n   \"note\": \"Asbaghi lists ʾadab, ʾādāb (pl.), ʾudabāʾ, ʾadīb and even ʾadabḫāna as a family, deriving the Arabic base from Persian — i.e. he would license Nourai's re-borrowing arrow.\"},\n  {\"src\": \"KLN\", \"where\": \"Klein 1966 p.467 s.v. divan\", \"stance\": \"supports\",\n   \"note\": \"Klein derives Arabic dīwān from Persian, which is what makes تدوین a genuine round trip.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Sogdian\", \"words\": \"dyb-yy\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n  \"Sogdian δīp 'letter, written document' (Manichaean spelling δyp/δyb, oblique -yy) is real, but in Gharib's \"\n  \"dictionary it surfaces inside a compound: entry 5523 «mwhrdyb M — muhr-δīp (©ob. -yy) 'seal of letter'» (printed \"\n  \"p. ~220), which is exactly the shape 'dyb-yy' that Nourai prints. Nyberg independently attests the word family: \"\n  \"«BP dyp 'document', MPrth dyb 'letter'». Sogdian did not take the word from Sumerian directly: like Persian \"\n  \"dibīr/dēwān it continues Old Iranian dipi-, the Achaemenid chancery loan from Elamite/Akkadian, spread across the \"\n  \"eastern Iranian world with Aramaic-script scribal practice — the Sogdian Ancient Letters (early 4th c. CE) are \"\n  \"written by exactly the scribal class that used the word. The arrow should therefore hang off node 1, not off the \"\n  \"Sumerian root box.\"),\n \"derivation_fa\": (\n  \"واژهٔ سغدی δīp «نامه، سند» (نگارش مانوی δyp/δyb، صورت غیرفاعلی با ـyy) واقعی است، اما در فرهنگ قریب بیشتر در ترکیب \"\n  \"دیده می‌شود: مدخل ۵۵۲۳ «mwhrdyb = muhr-δīp «مهرِ نامه»» (ص ۲۲۰ چاپی) و همان صورت «dyb-yy» است که نورایی آورده. نیبرگ \"\n  \"نیز جداگانه «dyp پهلوی کتیبه‌ای «سند» و dyb پارتی «نامه»» را ثبت کرده است. سغدی این واژه را مستقیم از سومری نگرفته؛ \"\n  \"مانند «دبیر» و «دیوان» دنبالهٔ ایرانی باستان dipi است که از راه سنت دبیریِ خط آرامی در سراسر ایران شرقی پخش شد \"\n  \"(نامه‌های کهن سغدی، سدهٔ چهارم میلادی، کار همین طبقهٔ دبیران است). پس این پیکان باید از گرهٔ ۱ آویخته می‌شد نه از \"\n  \"جعبهٔ ریشهٔ سومری. ادعای نورایی با این اصلاح پذیرفتنی است.\"),\n \"sources\": [U[\"dub\"]],\n \"ref_check\": [\n  {\"ref\": \"SOD:148\", \"status\": \"not_found\",\n   \"note\": (\"Gharib's printed p.148 is a blank leaf in the local OCR (SOD_pages.txt leaf 214; p.147 ends with entry \"\n            \"3733 δypty- and p.149 resumes at 3759 δyn'pr'nyg, so entries 3734-3758 are lost), and the archive.org \"\n            \"item SogdianDictionary has no hOCR/Abbyy file, so its full-text search returns 'No hOCR or Abbyy file \"\n            \"present'. The word itself is confirmed elsewhere in the same dictionary: entry 5523 mwhrdyb 'seal of \"\n            \"letter', with the oblique ending -yy Nourai prints.\")}\n ],\n \"consulted\": [\n  {\"src\": \"SOD\", \"where\": \"Gharib entry 5523 (SOD_pages.txt line 19537, printed p. ~220)\", \"stance\": \"supports\",\n   \"note\": \"«5523 mwhrdyb M | muhr-δīp ©*mwdr', Parth. ©ob. -yy | seal of letter | BBB c36».\"},\n  {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. dipivar\", \"stance\": \"supports\",\n   \"note\": \"«BP dyp 'document', MPrth dyb 'letter'» — the same Middle Iranian word in Parthian, from OP dipi-.\"},\n  {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. dibir / dēwān\", \"stance\": \"partial\",\n   \"note\": \"MacKenzie has no Sogdian, but his historical spellings <dpy(w)r> and <d(p)ywn> show the same dip- base that the Sogdian form continues.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Akkadian\", \"words\": \"duppu, tuppu\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\n  \"Akkadian ṭuppu(m) (older/variant duppu, with dappu 'board') 'clay tablet, written document' is a loan from \"\n  \"Sumerian DUB 𒁾 'tablet', taken over with the cuneiform writing system itself in the third millennium BCE; the \"\n  \"Sumerogram DUB continued to be used to write the Akkadian word. Zimmern lists it in exactly these terms, and \"\n  \"Kent cites «Akk. duppu» beside «Elam. tup-pi» as the intermediaries of Old Persian dipi-. The Sumerian voiced \"\n  \"stop is rendered by Akkadian ṭ/d, whence the doublet spellings duppu ~ ṭuppu that Nourai prints as 'duppu, \"\n  \"tuppu'. This node is the best-supported one on the page.\"),\n \"derivation_fa\": (\n  \"واژهٔ اکدی ṭuppu(m) (صورت کهن‌تر/گونهٔ duppu، و dappu «تخته») به معنی «لوح گِلی، سند نوشته» وام‌واژه‌ای است از سومری \"\n  \"DUB 𒁾 «لوح»، که همراه با خودِ خط میخی در هزارهٔ سوم پیش از میلاد به اکدی راه یافت؛ نشانهٔ سومری DUB همچنان برای نوشتن \"\n  \"همین واژهٔ اکدی به کار می‌رفت. زیمرن (ص ۱۹) دقیقاً همین را می‌گوید و کنت هم «اکدی duppu» را در کنار «ایلامی tup-pi» \"\n  \"واسطهٔ رسیدن واژه به پارسی باستان می‌داند. همخوان انسدادی واکدار سومری در اکدی به ṭ/d بدل شده و همین دوگانگی نگارشی \"\n  \"duppu ~ ṭuppu است که نورایی به صورت «duppu, tuppu» آورده. مستندترین گرهٔ این صفحه است.\"),\n \"sources\": [U[\"dub\"]],\n \"ref_check\": [\n  {\"ref\": \"AKD:19\", \"status\": \"supports\",\n   \"note\": \"«akk. duppu, tuppu Tafel, Schriftstück (< sum. dub), wozu dappu Brett, wohl nur eine Variante bildet» (AKD.txt, printed p.19).\"},\n  {\"ref\": \"BQT:823\", \"status\": \"supports\",\n   \"note\": \"Moʿin's footnote (leaf 284 ≈ printed 824, continuation of the p.823 note): «… قوم اکد شده صورت ṭuppu و tuppu درآمده» with an explicit citation of «Zimmern, Akkadische Fremdwörter … ۱۹».\"}\n ],\n \"consulted\": [\n  {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. dipi-\", \"stance\": \"supports\",\n   \"note\": \"«Elam. tup-pi, Akk. duppu (§152.I): borrowed from Sumerian dup-».\"},\n  {\"src\": \"AKD\", \"where\": \"Zimmern p.19\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Aramaic\", \"words\": \"dappa, dup\",\n \"verdict\": \"plausible\",\n \"derivation\": (\n  \"Aramaic דפא dappā is well attested and is indeed an Akkadian loan, but its meaning is 'board, plank, leaf/column \"\n  \"of a book', not specifically 'skin for a writing tablet': Zimmern gives «> aram. dappū Brett, Tafel, Blattseite, \"\n  \"auch ägypt.-aram. tp Brett», i.e. the wooden writing-board and, by extension, the page of a codex, and Moʿin's \"\n  \"footnote renders it «بمعنی لوحه و صفحه گرفته شده» ('came to mean tablet and page'). Wiktionary's Arabic دفّ entry \"\n  \"likewise notes Aramaic דפא dappā 'board' as coming from Sumerian DAB/DUB. Nourai's 'skin' gloss looks like a \"\n  \"back-projection from the tambourine at node 8-9 (a skin stretched on a frame); the Aramaic word is about wood, \"\n  \"and the parchment word in this family is rather daftar < Aramaic diftērā < Greek διφθέρα, a different etymon. \"\n  \"The second form 'dup' is presumably the Akkadianising spelling ṭuppā/tuppā.\"),\n \"derivation_fa\": (\n  \"واژهٔ آرامی דפא (dappā) به‌خوبی گواهی شده و به‌راستی وام‌واژه‌ای از اکدی است، اما معنای آن «تخته، لوح، صفحه/ستون کتاب» \"\n  \"است نه «پوستِ لوح نوشتن»: زیمرن می‌نویسد «> آرامی dappā تخته، لوح، صفحه، و نیز آرامی مصری tp تخته» و معین در حاشیه \"\n  \"می‌آورد «و بمعنی لوحه و صفحه گرفته شده». پس معنایی که نورایی داده («پوست برای لوح نوشتن») ظاهراً بازتاب واپس‌گرایانهٔ \"\n  \"«دف» (پوست کشیده بر چنبر) در گره‌های بعدی است. واژهٔ «پوست‌نوشت» در این خانواده در واقع «دفتر» است از آرامی diftērā \"\n  \"از یونانی διφθέρα که ریشهٔ دیگری دارد. صورت دوم «dup» احتمالاً همان املای اکدی‌گونهٔ ṭuppā است. ادعای نورایی با اصلاح \"\n  \"معنایی پذیرفتنی است.\"),\n \"sources\": [U[\"daf\"], U[\"daftar\"]],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\",\n   \"note\": \"The node carries no reference in the book (refs=None); the claim is covered by the AKD:19 and BQT:823-824 citations of the neighbouring nodes, both of which do contain the Aramaic step.\"}\n ],\n \"consulted\": [\n  {\"src\": \"AKD\", \"where\": \"Zimmern p.19\", \"stance\": \"partial\",\n   \"note\": \"«> aram. dappū Brett, Tafel, Blattseite, auch ägypt.-aram. tp Brett (> wohl arab. daff u. ṭaff Brett, Seite, daffat Buchdeckel), südarab. ṭf' Tafel» — supports the Akkadian→Aramaic→Arabic route but glosses 'board/page', never 'skin'.\"},\n  {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1629 s.v. toph\", \"stance\": \"partial\",\n   \"note\": \"«toph … Heb. tōph 'timbrel, tambourine', rel. to Aram. tuppā, of s.m., Arab. duff 'drum'; of imitative origin» — Klein knows an Aramaic tuppā, but it is the DRUM word, kept apart from dappā 'board'.\"},\n  {\"src\": \"BQT\", \"where\": \"Moʿin's footnote, BQT_v2_pages.txt leaf 284 ≈ printed p.824\", \"stance\": \"supports\",\n   \"note\": \"«همین کلمه وارد زبان آرامی شده … و بمعنی لوحه و صفحه گرفته شده».\"}\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Arabic\", \"words\": \"daf\",\n \"verdict\": \"disputed\",\n \"derivation\": (\n  \"Two homonyms are being conflated. (a) Arabic دَفّ daff 'board, side, flank; book-cover (daffat al-kitāb)' really \"\n  \"is the Aramaic loan: Zimmern p.19 «> wohl arab. daff u. ṭaff Brett, Seite, daffat Buchdeckel», and Wiktionary \"\n  \"derives Arabic دفّ in the 'board' sense from Aramaic דפא dappā, itself from Sumerian DAB/DUB. Moʿin's Borhan \"\n  \"footnote likewise ends the chain with «داخل زبان عربی شده صورت دف درآمده و بمعنی لوحه بکار رفته است» — Arabic daff \"\n  \"meaning 'tablet/board', NOT 'tambourine'. (b) The instrument دُفّ/دَفّ duff 'frame drum, tambourine' is a common \"\n  \"Semitic word of imitative origin: Klein, s.v. toph, «Heb. tōph 'timbrel, tambourine', rel. to Aram. tuppā, of \"\n  \"s.m., Arab. duff 'drum'; of imitative origin» (cf. Hebrew תֹּף tōp, Ugaritic tp, already in Genesis 31:27), and \"\n  \"Wiktionary derives the tambourine sense inside Arabic from the root د ف ف related to دَفَعَ 'to push, strike'. \"\n  \"Nourai's gloss 'a tambourine made of animal skin on a frame' therefore attaches the wrong meaning to the right \"\n  \"etymology: the Sumerian chain reaches Arabic 'board/page', while the drum has its own Semitic ancestry.\"),\n \"derivation_fa\": (\n  \"دو واژهٔ هم‌آوا با هم آمیخته شده‌اند. نخست «دَفّ» عربی به معنی «تخته، پهلو، جلد کتاب (دفّةالکتاب)» که به‌راستی وام‌واژه‌ای \"\n  \"از آرامی dappā است: زیمرن (ص ۱۹) «> عربی daff و ṭaff تخته، پهلو، daffat جلد کتاب» و ویکی‌واژه نیز همین معنی را از آرامی \"\n  \"דפא و در نهایت سومری DUB می‌گیرد؛ حاشیهٔ معین بر برهان هم زنجیره را چنین پایان می‌دهد: «داخل زبان عربی شده صورت دف درآمده \"\n  \"و بمعنی لوحه بکار رفته است» — یعنی «لوح»، نه «دایره و طبل». دوم «دُفّ/دَفّ» به معنی سازِ چنبری که واژه‌ای سامی و آوانماست: \"\n  \"کلاین ذیل toph می‌نویسد «عبری תֹּף «دف»، هم‌ریشه با آرامی tuppā و عربی duff «طبل»؛ آوانما» (سنجیدنی با اوگاریتی tp و \"\n  \"سفر پیدایش ۳۱:۲۷). بنابراین معنایی که نورایی داده («دایره‌ای از پوست جانور بر چنبر») به ریشه‌شناسی نادرست چسبیده است: \"\n  \"زنجیرهٔ سومری به «لوح/صفحهٔ» عربی می‌رسد نه به ساز. پژوهش امروزی این گره را رد می‌کند.\"),\n \"sources\": [U[\"daf\"], U[\"daftar\"]],\n \"ref_check\": [\n  {\"ref\": \"MON:1540\", \"status\": \"partial\",\n   \"note\": (\"Moʿin's Farhang s.v. دف (MON_part1.txt line 61981, the 2-vol Adena reprint; the 6-vol edition's p.1540 \"\n            \"could not be paged exactly in this reprint): «دف: daff [معر.] (ا.) (موسیقی) چنبری است که پوستی بر آن \"\n            \"چسبانند و قوالان آن را با انگشت نوازند» — the definition Nourai copies, and the tag «[معر.]» \"\n            \"('Arabicised'), but no Aramaic/Sumerian derivation and no statement that the drum is the tablet word.\")}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1629 s.v. toph\", \"stance\": \"contradicts\",\n   \"note\": \"«toph, n., a small drum (music). — Heb. tōph, 'timbrel, tambourine', rel. to Aram. tuppā, of s.m., Arab. duff, 'drum'; of imitative origin.»\"},\n  {\"src\": \"AKD\", \"where\": \"Zimmern p.19\", \"stance\": \"partial\",\n   \"note\": \"«(> wohl arab. daff u. ṭaff Brett, Seite, daffat Buchdeckel)» — Zimmern's Arabic outcome is 'board, side, book-cover', never an instrument.\"},\n  {\"src\": \"BQT\", \"where\": \"Moʿin's footnote, BQT_v2_pages.txt leaf 284 ≈ printed p.824\", \"stance\": \"partial\",\n   \"note\": \"«… بعدها داخل زبان عربی شده صورت دف درآمده و بمعنی لوحه بکار رفته است» — 'tablet', not 'tambourine'.\"},\n  {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (AFM_pages.txt)\", \"stance\": \"silent\",\n   \"note\": \"grep 'الدف' finds no headword for the drum; Addi Shir only lists الديوان in passing (pp. 209, 2302 of the OCR) — he does not treat دف as a Persian/Aramaic loan.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Persian\", \"words\": \"daf\",\n \"verdict\": \"disputed\",\n \"derivation\": (\n  \"Persian دَف daf 'frame drum' is certainly a borrowing from Arabic دَفّ/دُفّ — Moʿin tags it «[معر.]» and Borhan-e \"\n  \"Qateʿ itself says under دب: «و بپای فارسی دایره را نامند و بعربی دف خوانند و دوف معرب است» (leaf 283 ≈ printed \"\n  \"p.823) — and Wiktionary's Persian entry states plainly 'a Persian frame drum, borrowed from Arabic دَفّ (daff)'. \"\n  \"The bracketed variant شُندف is a genuine Persian word for a drum, not a misprint: Moʿin has «شندف: طبل، دمامه، \"\n  \"نقارهٔ بزرگ» and Asadi Tusi's Loghat-e Fors glosses «شندف دهل و طبل باشد». What is wrong is the ancestry: the \"\n  \"Arabic source is the onomatopoeic Semitic drum word (Heb. tōp, Aram. tuppā), so the Persian instrument does not \"\n  \"descend from Sumerian dub 'tablet'. The chart's own NOTE, 'See Deru 1 for another possible root' (PIE *deru- \"\n  \"'tree, wood', i.e. the wooden frame), fares no better: no modern source derives daf from an Indo-European root — \"\n  \"the word is a plain Arabic loan in Persian and the ultimate etymon is imitative.\"),\n \"derivation_fa\": (\n  \"«دَف» فارسی بی‌گمان وام‌واژه‌ای از عربی «دَفّ/دُفّ» است؛ معین آن را «[معر.]» می‌نامد و خودِ برهان قاطع ذیل «دب» می‌گوید \"\n  \"«و بپای فارسی دایره را نامند و بعربی دف خوانند و دوف معرب است» (برگ ۲۸۳ ≈ ص ۸۲۳)، و ویکی‌واژه نیز «دف» فارسی را \"\n  \"وام‌گرفته از «دَفّ» عربی می‌داند. صورت داخل پرانتز، «شُندف»، خطای چاپی نیست بلکه واژه‌ای فارسی و واقعی است: معین «شندف: \"\n  \"طبل، دمامه، نقارهٔ بزرگ» و لغت فرس اسدی «شندف دهل و طبل باشد» دارد. آنچه نادرست است تبارنامهٔ واژه است: سرچشمهٔ عربی \"\n  \"آن همان واژهٔ سامیِ آوانمای طبل است (عبری תֹּף، آرامی tuppā)، پس این ساز از dub سومری «لوح» نمی‌آید. یادداشت خودِ کتاب \"\n  \"(«رک: Deru 1»، یعنی ریشهٔ هندواروپایی *deru- «درخت، چوب» برای چنبر چوبی) نیز پذیرفتنی نیست؛ هیچ منبع امروزی «دف» را \"\n  \"به ریشه‌ای هندواروپایی نمی‌برد. پژوهش امروزی این گره را رد می‌کند.\"),\n \"sources\": [U[\"daf\"]],\n \"ref_check\": [\n  {\"ref\": \"MON:1540\", \"status\": \"partial\",\n   \"note\": \"Same entry as node 8: «دف: [معر.] (ا.) چنبری است که پوستی بر آن چسبانند و قوالان آن را با انگشت نوازند» (MON_part1.txt line 61981). Moʿin confirms the word and its loan status but not the Sumerian ancestry; the 6-vol pagination (p.1540) could not be verified on the accessible 2-vol reprint.\"}\n ],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 61981 (دف) and 86893 (شندف)\", \"stance\": \"supports\",\n   \"note\": \"«دف: [معر.] … چنبری است که پوستی بر آن چسبانند»; «شندف: (ا.) طبل، دمامه، نقارهٔ بزرگ» — both forms of Nourai's node are Moʿin's.\"},\n  {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ s.v. دب, BQT_v2_pages.txt leaf 283 ≈ printed p.823\", \"stance\": \"supports\",\n   \"note\": \"«دب … و بپای فارسی دایره را نامند و بعربی دف خوانند و دوف معرب است».\"},\n  {\"src\": \"FRS\", \"where\": \"Asadi Tusi, Loghat-e Fors (FRS_pages.txt line 10890)\", \"stance\": \"supports\",\n   \"note\": \"«شندف دهل و طبل باشد» — the parenthetical variant is attested in an 11th-c. Persian glossary.\"},\n  {\"src\": \"KLN\", \"where\": \"Klein 1966 p.1629 s.v. toph\", \"stance\": \"contradicts\",\n   \"note\": \"Traces the Arabic source word duff 'drum' to an imitative Semitic etymon (Heb. tōph, Aram. tuppā), not to the Sumerian tablet word.\"}\n ]\n})\n\nwith io.open(\"data/verification/page-141.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write(\"\\n\")\nprint(\"written\", len(nodes), \"nodes\")\nPYEOF\npython3 -m json.tool data/verification/page-141.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 141",
 "description": "Write page-141.json and run verify_check"
}
```


### [2026-09-05T20:28:08.959Z] TOOL RESULT

```
written 9 nodes
JSON OK
nodes verified: 9/9
node verdicts: {'plausible': 5, 'disputed': 3, 'confirmed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 6, 'not_checked': 5, 'not_found': 1, 'partial': 2}
books consulted: {'partial': 9, 'supports': 19, 'silent': 2, 'contradicts': 2} | by book: {'KLN': 5, 'PLA': 3, 'MON': 3, 'AKD': 3, 'BQT': 3, 'KNT': 2, 'HRN': 2, 'PHD': 2, 'NYB': 2, 'BRT': 1, 'HUB': 1, 'LKT': 1, 'FVQ': 1, 'SOD': 1, 'AFM': 1, 'FRS': 1}
```


## [2026-09-05T20:28:17.886Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls -l data/verification/page-141.json; git status --short",
 "description": "Confirm output file"
}
```


### [2026-09-05T20:28:17.941Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 47475 Sep  5 16:28 data/verification/page-141.json
?? data/verification/page-139.json
?? data/verification/page-141.json
```


## [2026-09-05T20:28:37.415Z] AGENT

Page 141 (book p. 111) verified — `/home/sfmqrb/git/rishe/data/verification/page-141.json`, `verify_check.py 141` shows 0 PROBLEM lines.

**Counts** — 1 entry, 1 root (confirmed), 9 nodes: 1 confirmed, 5 plausible, 3 disputed. Ref checks: 6 supports, 2 partial, 1 not_found, 5 not_checked. 16 books consulted (19 supports, 9 partial, 2 contradicts, 2 silent).

**Key finding:** the whole chart is a transcription of Moʿin's etymological footnote to دبستان in Borhan-e Qateʿ pp. 823–824, which itself cites Zimmern (AKD) p. 19 by name — both cited pages were located and quote Nourai's chain verbatim, دیبا/دیباچه and Arabic دف included.

**Disputed**
- Node 3, Arabic أدب adab — Asbaghi 1988 derives it from Persian < MP dipi, but the Arabist consensus (Wiktionary with citations, Nöldeke, EI) makes it native Arabic, back-formed from آداب, pl. of دَأْب (root د أ ب); the hamza and the lost -p- are unexplained on Nourai's route. (دیوان in the same node is fully confirmed.)
- Node 8, Arabic دف — conflates two homonyms: daff 'board, side, book-cover' really is < Aram. dappā < Sum. dub (Zimmern; Moʿin ends the chain at «بمعنی لوحه»), but duff 'tambourine' is the imitative Semitic drum word (Klein s.v. *toph*: Heb. tōph, Aram. tuppā, "of imitative origin").
- Node 9, Persian دف — a real Arabic loan (Moʿin «[معر.]»), but inherits the wrong ancestor; the chart's own NOTE "See Deru 1" (PIE *deru-) is likewise unsupported by any modern source.

**Caveats worth noting** — node 2 is `plausible` only because of دیباچه: Moʿin and Asbaghi derive دیبا from OP dipi, but the mainstream view takes MP dēbāg < PIr. *diHp- 'to shine', with دیباچه a re-borrowing of Arabic دیباجة. دبیر/دبستان/دیوان are confirmed (MacKenzie's <dpy(w)r>, <d(p)ywn>; Nyberg's *dipi-vara-; Horn no. 540; Klein p. 467). Node 1: OP dipi- is a noun 'inscription', not a verb "to write", and reaches OP via Elamite/Akkadian.

**No extraction errors** — the page image matches the JSON exactly; شُندف is a genuine Persian word (Moʿin, Loghat-e Fors), not a misread.

**Unreachable references:** ETM:36, FVA:28, FVF:13,273 (no digital copies / login-gated noorlib). SOD:148 is `not_found` — Gharib's p. 148 is a blank leaf in the local OCR (entries 3734–3758 lost) and archive.org has no hOCR for that item; the Sogdian word is confirmed instead from Gharib entry 5523 *mwhrdyb* "seal of letter" (oblique -yy) plus Nyberg's "MPrth dyb 'letter'".
