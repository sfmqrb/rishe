# Verification process log — verify-page-421


## [2026-09-14T01:21:30.247Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 421 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-421.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-421.json. Write /home/sfmqrb/git/rishe/data/verification/page-421.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 421` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:21:31.333Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:21:32.230Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:21:32.244Z] TOOL RESULT

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
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	```json
231	{
232	  "pdf_page": 126,
233	  "book_page": 96,
234	  "verified_by": "claude-opus-5",
235	  "verified_on": "2026-09-05",
236	  "entries": [
237	    {
238	      "entry": 0,
239	      "root": "Dheigh, Dhigha",
240	      "verdict": "confirmed",
241	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
242	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
243	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
244	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
245	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
246	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
247	      "nodes": [
248	        {
249	          "id": 6,
250	          "lang": "Avestan",
251	          "words": "pairi-daeza",
252	          "verdict": "confirmed",
253	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
254	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
255	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
256	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
257	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
258	        }
259	      ]
260	    }
261	  ]
262	}
263	```
264	
265	Rules:
266	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
267	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
268	- `words` = the transliterations of the node joined by "; " (copy from the chart).
269	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
270	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
271	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
272	- If a node lists several words, cover each word; if they differ in verdict, use the worst
273	  verdict for the node and explain per word in `derivation`.
274	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
275	  scholarship takes.
276	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
277	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
278	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
279	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-09-14T01:21:32.731Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-421.txt"
}
```


### [2026-09-14T01:21:32.760Z] TOOL RESULT

```
1	=== PDF page 421 (book page 391) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Rěp : to crawl  (refs POK:865)
4	#1 (parent #0) [Avestan] refs=HUB:67; HRN:137 | rap : to go
5	  #2 (parent #1) [Persian] refs=BQT:955 | raftan «رفتن» : to go | extra: رفتار ، روا ، روان ۱ ، روش ، روند
6	#3 (parent #0) [Arabic] refs=AFM:74 | ravâj : circulation
7	  #4 (parent #3) [Persian] refs=HRN:137 | ravâj «رواج ( ترویج ، رائج ، رایج )»
8	#5 (parent #0) [Latin] refs=AHD; POK:865 | repere : to creep
9	  #6 (parent #5) [English] refs=None | reptile
10	
```


## [2026-09-14T01:21:35.488Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-421.json",
 "description": "Read source JSON for page 421"
}
```


### [2026-09-14T01:21:35.529Z] TOOL RESULT

```
{
  "pdf_page": 421,
  "book_page": 391,
  "entries": [
    {
      "root": {
        "name": "Rěp",
        "lang": "Indo-European",
        "refs": "POK:865",
        "gloss": "to crawl"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HUB:67; HRN:137",
          "words": [
            {
              "translit": "rap",
              "gloss": "to go",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:955",
          "words": [
            {
              "translit": "raftan",
              "gloss": "to go",
              "script": "رفتن"
            }
          ],
          "script_extra": "رفتار ، روا ، روان ۱ ، روش ، روند",
          "note": null,
          "quote": {
            "text": "همان جویبار است و آب روان ۱ ـ که از دیدنش تازه گردد روان ۲",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Arabic",
          "refs": "AFM:74",
          "words": [
            {
              "translit": "ravâj",
              "gloss": "circulation",
              "script": null
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "HRN:137",
          "words": [
            {
              "translit": "ravâj",
              "gloss": null,
              "script": "رواج ( ترویج ، رائج ، رایج )"
            }
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; POK:865",
          "words": [
            {
              "translit": "repere",
              "gloss": "to creep",
              "script": null
            }
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
            {
              "translit": "reptile",
              "gloss": null,
              "script": null
            }
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T01:21:37.480Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','HUB','HRN','BQT','AFM','AHD','WLD','IEC','SYN','BRT','PHD','NYB','CHEUNG','MON','ARY','KLN','SKT','FSD','WEB','PLA','FVQ','LKT']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-14T01:21:38.718Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
CHEUNG null
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
```


## [2026-09-14T01:21:48.382Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80; echo ---; ls ocr 2>/dev/null | head"
}
```


### [2026-09-14T01:21:48.485Z] TOOL RESULT

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
FFD
HRN
IRN
PLA
SNS
SOD
```


## [2026-09-14T01:21:48.958Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,200p' /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T01:21:49.018Z] TOOL RESULT

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
```


## [2026-09-14T01:21:51.646Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rep-\" POK_full.txt | grep -i -n \"kriechen\\|schleichen\" | head -20; echo \"=== search rēp\"; grep -n \"rēp-\\|rep-\\b\" POK_full.txt | head -40"
}
```


### [2026-09-14T01:21:51.735Z] TOOL RESULT

```
=== search rēp
48390:Root / lemma: krep-1, kfp- 
48398:Root / lemma: krep-1, kfp- : body derived from -p- suffix of Root / lemma: (s)ker-4, (s)kera- 
48421:Root / lemma: krep-1, kfp- : body derived from -p- suffix of Root / lemma: (s)ker-4, (s)kere- 
48451:Root / lemma: krep-2 
48747:Root / lemma: krep-1 
48762:Root / lemma: krep-2 
57732:ncymr. modryb^ mother's sister', acymr. modrep-edP\., abret. motrep, nbret. moereb6s. 
69022:sign', eres{*prep-s-), mostly PI. eresk'^iace, Miene, sight, Vorderseite', eresem 'ze'\ge 
71096:Root / lemma: rep-1 {rep-?) 
71110:Root / lemma: rep-2, rap- 
87343:Root / lemma: trep-1 
87381:Root / lemma: trep-2 
87404:Root / lemma: trep-3, treb-
```


## [2026-09-14T01:21:52.544Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"repere\" POK_full.txt AHD_watkins1985.txt LEW_1910.txt LAT.txt | head -30"
}
```


### [2026-09-14T01:21:52.674Z] TOOL RESULT

```
AHD_watkins1985.txt:1032:strep-. To make a noise. Imitative root. Latin strepere, to make noise: OBSTREPEROUS. [Pok. (s)trep- 1037.]
LAT.txt:28511:obbri-, orri-, d'aprbs obrepere?)} horrisonus (po^t.); abhorrei:
LAT.txt:42698:un point de repere, non une direction. L'ombrien n'a que o(p)s- dans
LAT.txt:59412:uel stridere clarius quam mures uel strepere magis.
```


## [2026-09-14T01:21:55.937Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '71090,71140p' POK_full.txt"
}
```


### [2026-09-14T01:21:55.993Z] TOOL RESULT

```
Meaning: ' cry, shout, holler 
See also: s. re/-3. 
Page(s): 853 



Root / lemma: rep-1 {rep-?) 

Meaning: to crawl, sneak 

Material: Latin repo, -ere' grovel, truckle, creep, slink'; Old High German rebo, reba, repa. 

Middle High German /■©it'e'Schlingschoftling'; ablaut. Middle Low German wTn-rave' vine '; 

Lithuanian replioti' grovel, truckle, creep ', ablaut, roplotif^s., Latvian rapat, rapt6s.. Old 
Prussian rTpaitHo\Qe\!\ barely in addition wruss. rapuxa, poln. ropucha' toad '. 

References: WP. II 370, WH. II 430, Trautmann 246, Kluge-Goetzeie 604. 
Page(s): 865 

Root / lemma: rep-2, rap- 
Meaning: pole; beam 

Material: Old High German /-a i/o 'rafter'. Old Icelandic rafr, raefrm., rafu. 'Sparrendach'; 
Old Icelandic raptrm. 'stick, rafter' (vandal. PN Raptus), Old English r3efter6s.. Middle 
Low German rafter, racMer'smaW balk, beam, lath'; Lithuanian re/?///?// "uplift, set up, 
hinstellen'; Old Church Slavic repbjb, repijb "picket, pole', reptje' TpipoAo(; '. 
References: WP. II 370. 
Page(s): 866 

Root / lemma: res-, ros- 

Meaning: " flow ' 

See also: see above S. 336 f. {ere-s-2). 

Page(s): 866 

Root / lemma: ret- rot- ret- 
Meaning: pole; trunk 



Material: Old High German ruota, Old Icelandic roda 'rod, shaft, pole', Old Saxon roda 
"(picket, pole)kreuz'. Old English rdd6s. and Church Slavic ratiste, ratoviste 
"Lanzenschaff; perhaps in addition Latin retae'irom dem bank, border, shore of river 
protruding tree ', retare'6ev\ river from solchen clean' and AaZ/sTloft'. 
References: WP. II 368, WH. II 420, 431. 
Page(s): 866 

Root / lemma: roi-no-
```


## [2026-09-14T01:22:02.086Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f,off in [('HRN.txt',21),('HUB.txt',10)]:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    print('###',f,'npages',len(pages))\nEOF"
}
```


## [2026-09-14T01:22:02.733Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"raftan\\|raft\\b\\|rav\\b\" HRN.txt | head -30"
}
```


### [2026-09-14T01:22:03.439Z] TOOL RESULT

```
### HRN.txt npages 412
### HUB.txt npages 300
```


### [2026-09-14T01:22:03.506Z] TOOL RESULT

```
645:kurd. aza *brav, tapfer* (Houtum-Schindler).
1721:sich aus der ursprünglichen Bedeutung 'seine Kraft,
1741:*) Ein aw. üö^«- *Kraft' (Justi) giebt es nicht, vergl. Geldner ,
2247:Meinung nach fälschlich zu skr. {/'rav-, lav-),
2698:Pehlevi aufgegeben worden; np. pärav alte Frau' ist
2770:seine Kraft hält sich nicht länger als ein Jahr (187
2836:patiraftan (Bund., sonst stets inJltJ^pD), päz. padlraftan
2966:bedeutet überhaupt nicht 'enthaltsam', sondern ursprünglich nur *brav*
3552:tuxs(l)sn, tu^sUan; ai. tväksas^ 'Thatkraft'.
3618:(y. 11 (17)), taraftagl, taraft (ZPGL); ai. (mit anderer
5950:674*»^'* {\)»ör 'Kraft, Gewalt' (reimt auf hör, Sahn. I, 202
5952:aw. zävar- 'Macht, Kraft*; phlv. zör, zörlh, arm.
6412:srayltan^ sräy(i)su^ srüt 'Gesang; ai. l/'grav-^ Caus.
6414:wa/. sirav-am^ sar. nasrav-am 'recitiren*.
7162:aw. *fravärana-^ vergl. fravüra- (?) ; phlv. fravär
7188:ai. pravät- abschüssige Bahn', pracdtä 'beigab, ab-
7884:gerewnäiti; phlv. graftan; ai. l^grabh^, gfbhndti,
7905:ap. aw. l/'var- glauben ; phlv. varav(i)stan, mirav{i)sn
9204:1064. nirö {*n^rö) 'Kraft, Macht'.
9798:s. V. berpernsän) aus phlv. varav(i)m und urmek —
9994:aw. ägerepta-; phlv. ägraft, päz. agereft.
10439:83. fraraftan vorwärts, herzugehen , immer mit frad
10443:Lesung fravämUan (Spiegel, Glossar) ebenso wie die
10449:about, to wander*, fraravä zavum *to take a walk' bei Jus ti, Bund., 197.
10467:und ähnliches (vergl. auch AV. yravä/tanö") wieder-
10468:giebt. Fr. Müller, der in der Lesung fraraftan mit
10470:Verbum fraraftan lesen (WZKM. 5, 350); ich habe
10558:97. yrav (geschrieben yrüb), vd. 9 (41) (42); vielleicht
10561:437 übersetzt strongly* und nimmt also phlv. grav
10706:127. fiisrav 'berühmt, erlaucht', x^isravih.
```


## [2026-09-14T01:22:07.844Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==158' HRN.txt | head -60"
}
```


### [2026-09-14T01:22:09.133Z] TOOL RESULT

```
— 136 -
609. reje^ reze *Reihe\
aw. razista- ^geradester ; ai. räjistha- (Nöldeke,
mündliche Mitteilung). Jüd.-pers. T]T\ dagegen dürfte
zu aw. rasman- 'Schlachtreihe', ai. ragmän-^ racmi'^
ragi- gehören.
Geldner hatte KZ. 24, 387 Note 2 aw. razura-
'Geleis' (yt. 5, 50) vergleichen wollen.
np. rede 'Richtung, Linie, Reihe' (Öähn. I, 367
Vers 823) scheint dagegen zu aw. ereta-, areta-y ai.
ftd' 'richtig, vollkommen' zu gehören (ursprünglich
'etwas Rechtes, Gerades).'
610. ru%8 {rexs) 'Glanz, Licht', ru/^Tden [rexsiden).
aw. vergl. rao/snc^ 'glänzend, leuchtend, strahlend' ;
ai. ruksd' 'glänzend'.
oss. d. ro/s^ t. rü/s 'Licht, leuchtend', rü/say (214);
ya;'n. ru/sinie.
Gehört np. ru/ 'Wange' auch zu derselben Wurzel?
611. red 'weise, tapfer' (z. B. Sahn. I, 149 Vers 365; Vis
und Rämin S. 13, V. 5 v. u.).
aw. ratU' 'Herr'; phlv. rat, -rat^),
612. rezm 'Schlacht, Kampf.
aw. vergl. areza- 'Schlacht'; arm. LW. paterazm
'Kampf, auch razm.
An Ableitung von aw. rasman- 'Schlachtreihe' zu
denken {s könnte statt z vor m stehen), verbietet die
Bedeutungsverschiedenheit (s. No. 609).
613. rest]äy(^e^ 'Auferstehung der Todten'^).
aw. irista- 'todt'; phlv. rist^ ristä/ez (paz. ristaxez),
614. rasten 'wachsen, Praes. röy-em, röylden, röyäniden,
rösta (arab. syr. LW. rustOq), pNDDn, Is. 42, 11.
aw. |/>c/orf-, raoöahe 'wachsen'; phlv. rustan (bezw.
rödastan , aber nicht wahrscheinlich), röyend bezw.
rödent (3. Plur.), rostäk [rödastak, Salemann, Eine
*) Vergl. Nöldeke, Tabarl-Obersetzung, 447.
*) Kaum gehört hierher röz-l *ir,9 'Todestag' (Pertsch, Die
persischen Handschriften der herzogl. Bibl. zu Gotha, S. 115, 116),
vergl- de t^agarde, Ges. Abb» 3?,
```


## [2026-09-14T01:22:11.880Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==159' HRN.txt"
}
```


### [2026-09-14T01:22:12.965Z] TOOL RESULT

```
- 137 —
Pärsenhandschrift 68, 10), röd(i)sn bezw. röy(i)sn; ai.
rödli' rodliati (KröA-, röltati).
bei. rtiday, n. ruday (319).
Zur i/^rödfi- vergl. Bartliolomae, ZDMG. 44, 553
No. 332.
615. resen 'Strick'.
ai. ragandr 'Strick, Riemen, Zügel, Gurt'; arm. LW.
apa\rasan zügellos*, erasan, erasanak 'Zügel' (Hübsch-
mann, No. 96).
arab. hebr. LW. rasan, bezw. JD^.
616. restden 'ankommen, erreichen', Praes. res-em^
resänTden,
g. rasadmün.
ap. i/^ras' 'kommen, gelangen', arusam^); phlv.
rasltan, ras(i)§n (AV.), rasmitan,
LW. afy. rasedal; bei. rasa(/ (313).
617. risten 'spinnen, Praes. res-efn, riste, resulen, resmän,
rismän, vergl. ebresum (No. 65).
g. risbün *Zwirn .
ai. i/^reg-, rigäte 'rupfen, abreissen.
bei. resag^ n. resay 'spinnen, flechten' (318), üresarj
'spinnen' (40) ; oss. alunjssin, d. alwiessun (bei Geiger).
resk s. eresk (No. 71).
618. risk 'Lauseei, Nisse' (AM. 141 Zeile 11, 191 Zeile 7).
ai. liksd' 'Ei einer Laus, Nisse' (Nöldeke bei
Hübschmann, Oss. Etym., S. 46).
kurd. LW. risk ; af/. riya ; bei. LW. rask, risk 'Läuse'
(217); oss. t. llsk, d. liskä 'Nisse' (170).
619. reften 'gehen, weggehen', Praes. rew-em, reftar, retvä
(arab. LW. rawäj), rewän, rewäne, retvis'^),
aw. y^rap' 'gehen' in rap<ö-.(?)3); phlv. raftafi, rapet^
rawad (3. Sing., geschr. ra/d)^ rawäk, räwäkth^
Aw. rasaintl' (y. 52, 1, 3) gehört nicht hierher nach liartho-
lomae, Indog. Forsch. II, 264.
*) BeilAufig bemerkt, ist die Aussprache rös in dem bei Vullers
aus Bh. 8. V. citirten öahnämeverse falscl^; derselbe steht I, 8 Vers 131.
') Yd. 13, 45. Aber ganz annoher.
```


## [2026-09-14T01:22:20.180Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 76 77 78; do echo \"=== leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' HUB.txt | head -50; done"
}
```


### [2026-09-14T01:22:21.332Z] TOOL RESULT

```
=== leaf 76
— 65 -
aus der dih wurde, wie -kert, -gerd (in Namen) zu gird
u. s. w. geworden ist, oder geht np. dih = dlh, dsh,
das haufig vorkommt, auf mp. dsh zuriick?
589. Bei Rosen, Np. Sprachfiihrer p. 26, 39: ddhdnd*Qe-
bissstiick des Ziigels ; afgh. LW. dahana fem. *the bit
of a bridle', kal dehand, dahnd etc.
593. Ich stelle -des, -dis *ahnlich' zu gr. Jaxv/t/'zeige', dsixrjXov
*Ebenbild', skr. dig 'zeigen', subst. dig *Hinweis, Art and
Weise', zd. dis Veisen', osset. dwd%8}n zeigen u. &. w.
Also doeh -dEs = zd. ^da^a-, auch wenn dies nicht
rait daesa- yt. 13, 104 (*Traumbild'?) identisch ist.
594. Wenn dBz, deza *Kochtopf zu got. deigan *kneten, aus
Thon formen* (Wzl. dhig%) gehOrt, ist es verwandt mit
Nr. 563 diz, dSz *Burg', s. oben. Ob auch deg *Koch-
topf dazu gehort, ist fraglich, da 1) idg. dhig^h durch
skr. dBgdhiy digdha- nicht gesichert ist (vgL Brug-
mann, Grundriss I, p. 344) und 2) idg. dhoi^ho- im
Neup. zu *d^y werden miisste. Np. d^ (afgh. LW.
dEg *Kesser) setzt ap. ^daika- voraus. Phi. dSg 'Kesser
(Gl. and Ind. 288) kann eine junge Form sein. Zu d.
Tiegel u. s. w. vgl. Kluge, Wb. 5. Aufl. s. v.
595. Piige hinzu : paz. dddlgar ^secondly, other' Shk. 240,
Min. Gl. 53, did 'second' Shk. 241, Min. Gl. 61, dadum
'second' Shk. 240. Dieses paz. did ist direct = ap.
duvitiya- *der zweite . Vgl. WZKM. 5, 262.
596. Die kurdische Form lautet dem *Gesicht' bei Socin,
kurd. Sammlungen II, p. 307 ; afgh. lies ISmq.
599. Besser *daidavara- (Fe&tungBmsiuer*)^) Sils *daigavara-
anzusetzen, vgl. oben Nr. 594 und 563. Anders Fr.
Mil Her, WZKM. 8, 95 {^daya-vara- *Scheidemauer).
Falls dtvar (mit i) die urspriingliche Form ist (vgl.
afgh. LW. dlval *a wall'), ware dUvdr iiber *diyvar =
*did-vclr auf ap. *dida-vara- zuriickzufiihren. Alles
unsicher. Nebenform dwal JRAS. 1893, 463.
600. NSldeke macht mich darauf aufmerksam, dass im
ersten Verse von Vis u Ramin ra Dativpartikel (und
niar an Nominativ) ist.
>) Vgl. bara I diz *Mauer der Festung' Fird. I, 452, 325.
HUbsohmann, Peraisohe Studien. 5
=== leaf 77
i — 66 —
601. Zu rdd 'freigebig = phi. rat (vgl. paz. rad% liberality'
Shk. 264) geh5rt arm. LW. arat *reichlich, freigebig,
giitig.
607. Geht rah *Weg' = paz. rah = arm. rah (bei Faiistus
V. Byz.) auf ap. *r5^a- (Horn vergleicht skr. rathya-
Tahrstrasse' von ratha- = zd. ra^a-*Wagen') zuriick, so
kann das Wort im Pehlevi, wo ras geschrieben wird,
in alter Zeit docli nur *r5^, jiinger rah gelautet haben.
Ich glaube dann nicht an ras als neupersische Neben-
form. Bei aspras 'Stadium* liegt die Deutung als Pferde-
weg' allerdings nahe, aber warum heisst es nicht *asprah
anstatt np. aspras, aspraz^ aspres, asprlz (Vullers),
aspres (Schefer, Chrest. pers., vgl. ZDMG. 44, 532),
phi. aspras, aspres (Pahl. Diet. Ill, p. 541), arm. LW.
asparez, aspar^ (g^n. asparisi)? Np. rastan gehort
nicht hierher, da es kein Denominativum sein kann.
608. Np. ruhdyad raubt' aus *rupayati ist wohl von robad
*fegt' aus *raupati zu trennen.
609. Np. raja, raSa *Reihe' scheint mir ein phi. *racak oder
"^rajfaky dagegen np. rada 'Richtung, Linie, Reihe* ein
phi.* ratak vorauszusetzen. Mit rajfa = '^racak Hesse
sich skr. raSana- 'Ordnung, Anordnung vergleichen. Fiir
skr. rdji- *Richtung, Linie' wiirde ich np. "^raz-a er-
warten. Vullers fiihrt ein np. raja {raSa, raza) 'funis
vestibus imponendis inserviens' auf, das = skr. rdjju-
'Strick, Seir sein kSnnte. Vgl. phi. araSak = arajak
'frei von Fesseln' Bdh. 61. 59?
610. Np.rwa? Wange gehSrt nicht hierher.
611. Np. rod weise, tapfer' stimmt in der Bedeutung nicht
zu zd. ratU' 'geistliches Oberhaupt, Herr' = paz. ra3
'master' Shk. 264 = np. rad (rad) 'Oberhaupt eines
Kreises' (Tab. 447). Nach NSldeke ist aber rad bei
F i r d u s i = 'Herr oder 'Held'. Vgl. z. B. Fi r d. 1, 130, 28.
612. Np. razm 'Schlacht' ist = ap. "^razma = zd. rasma
'Schlachtreihe (von Wzl. raz = idg. reg^, vgl. skr.
raju *Reihe'). Der Ubergang von 'Schlachtreihe' zu
'Schlacht' ist, meine ich, begreiflich und iiberdies be-
legbar, vgl. z. B. arm. iakat *Stim, Front, Heerresfront,
=== leaf 78
- 67 -
Schlachtreibe, Schlacht'. Fiir idg. g^m, g^hm erscheint
regelrecht zd. sm = ap. zm, Zu arm. razm und pate'
razm vgl. phi. razm u patrazm Yatk. i. Zar. p. 66.
616. Np. rasad = ap. rasatiy zu skr. rdchdti. Uber die
Bildung vgl. Bartholomae, Idg. Forsch. II, 264.
Die Etymologie gait schon lange vor WZKM. 6, 187,
vgl. z. B. Bartholomae, Handbuch p. 120.
617. Osset. alwtstn^ dltolstn spinnen* findet sich bei Sjogren
p. 351 und Bischof Joseph p. 441 (s. v. prjasfi). Es
stimmt zu bal. brBsag. Aus dem Afgh. geh5rt hierher
vrHql^ rHql spinnen'.
618. Np. riSk *Nisse' = afgh. riSa fem. ^Nisse* ( = iran.
*riska^ Geiger, Etym. p. 46 gegenilber skr. likSOr),
619. Zu lat. rSpo oder serpo? Im Phi. wird Qbrigens fQr
np. ravd = paz. rawd etc. geschrieben ruhcik d. i.
ravak, das auf einen Praesensstamm rav-, ap. rab-,
nicht rap- weist. Das angefiihrte np. rdm scheint nach
Bedeutung und Etym. sehr unsicher. Etwa identisch
mit ram *froh*?
622. Np. randfdan liobeln, glatten, schaben wohl denom.
von rand, randa *Hobel, Schabemesser = afgh. LW.
randa 'Hobel'. Die nasallose Form liegt vor in skr.
rod *kratzen, ritzen, hacken, nagen', bal. radag *to tear
up the ground', pt. pf. rasfa, lat. rado 'scharren, schaben,
kratzen, glatten, rasieren*, rallum *Pflugreute', rast-
rum 'Hacke, Karst*.
627. Dazu arm. LW. rot Tluss'.
628*»*"(p. 258). Zu jtid. pers. rudan ausraufen' gehOrt bal.
runay *Korn schneiden, ernten', pt. pf. ru&a, skr. lu,
lufiati schneiden , waxi rut, sar. rUt *J§,tung des Un-
krautes* (Geiger, Etym. des Bal. Nr. 321).
629. Np. rozl *das t^gliche Brot' ist direct = phi. rddTk
= arm. LW. fodik 'der tS-gliche Unterhalt, Lebens-
mittel'.
631. Die armenischen Formen haben kurzes o. Als modeme
Aussprache von roSan giebt Rosen, Np. Sprachf.
p. 61 rouS&n *heir wie von Nr. 632 rauy&n 'zerlassene
Butter' an.
6*
```


## [2026-09-14T01:22:29.965Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"raftan\" CHEUNG.txt | head -20; echo \"=== rab\"; grep -n \"^\\*\\?rab\\b\\|\\*rab \\|rab- \" CHEUNG.txt | head -20"
}
```


### [2026-09-14T01:22:30.034Z] TOOL RESULT

```
12596:*NWIR: NP raftan/rav-, Bal. rapt (supplet. Sut) / ra(w)- ‘to go’, Kurd. (Kurm.) roy- ‘to 
41357:raftan/rav-, 184 
=== rab
8591:*AVESTAN: grab- (garab-) ‘to grab, seize, take’ || (+ *a-) ‘to grab (to)’ || (+ *uz-) "to 
8608:*OLD PERSIAN: grab- ‘to seize (as possesion), seize (as prisoner)’ — Kent: 183b 
33445:grab- (gorob-), 119
```


## [2026-09-14T01:22:30.968Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rap\\b\\|rapta\\|rapaiti\" BRT.txt | head -30"
}
```


### [2026-09-14T01:22:31.074Z] TOOL RESULT

```
2618:WZKM.  /j.  118.  Ung":    antJry  'ry.i  (AD.)  ,u:irapaiti  isd-i
2620:Yt.iO.ii6;   —    af^rapaitinam  "'^rya/iam]
2767:(sd.) N.52 ; 53{yio*up5is»mne)  ■".  4) 'Jem. besuchen,  sich  einfinden  bei  — ';  upä  tu  (sd.) nö  ioa  yti  asaonqm  nwsu*i>:^ntö{iVlk)"^ /ravasayd  Ylij.  146.  a)  insbes.  'einen Lehrer  besuchen,  zu  ihm  in  die  Schule gehen':  ivat  nj  *ai^rapaitint  (sd.)  upöi- sät"^  N. /j;  —  ..  *ainim  ai%rapailim (sd.)  upsissi/^'''  a'ia  "i^ritTtn  upsisöil  ai- va'ha  ioirim  upäisi}it"1^.ii.  5>'erfahren, '  erleben' :  upa  aBqm  xiapamm  üvavat  sätüis urva  *  Haiti  yaia  .,  H,  2.a.
3372:ainim  ag^rapaitiot  (sd.)  üpshöit  '>a  >. Um  aivdi:a  tüirim  T^.ii; — yujyastis  haca *nmanat    "'ha    \daniuil]     visal     Aa'ir»m *zaiUao]  *'%a  •>   *daMaot  N.  8;  ioS\  Yt. JT.3; —  dvaiibya  Aaca  mnbya  dva  nara
3447:7.  b)  beim  Imp.:  dJidt  at  ruras  .  . aimil.ra/mauis {s^)  Y.40.S;  —  äAü  at paiti  adähü  .  .  mazdqmcä  büiricä  ksnniä ..  Äru/nt^f  (sd.)  Y.40.1.  U)  sonst  (?)=>: ifm  atm  *apl  ae'i-rapaitim  upayat  N,/2 —  ailahmi  paiti  at^  as^ante  YL  i(). 46.  Wertlos:  Vd.<¥,"^/J.  S.  noch  atca, atcit,  at  va,  at  zT.  [P.  27:  lies  aoaoy^ ainaL]
3528:AvyayibAävaVorap. ;    Dbr.   VglS.   I.    614.    — ^paiH-buslay-  f.,  lum  V,  baad- ;   ai.  TgU  baddhay- f.;  S  53  II-  7-  —  P"'=  P^  animäyiinih. j.  apailir>la  F.  jh;  lies  apaili^rfla.
3554:an  Gerechtigkeit,  von  AHM.:  ahurvm  Durch H.pIoL  «us  -M-"«"'''"'"''-.  Superl.  aus mazdqm  ..yS  aÜahe  'mS  Y.57.4;  I.\;  — |  'apayanta- Aiy,  V¥¥.  iam\. yam-;  yant{a-  ist fravaslm  avqm  yqtn  shurahe  mazdä  ,  ,  |  Komp.-Form  zn  ü.  yämi^aväi,  IF.  /,  70. asäi°mqmca'V.26.2.  2) 'der  tüchtigste,  •  j.  apayav-  'der  es  (einem  Geräusch wirksamste"*;  'maya  fiaiti  vacastaitü  "^loxtmA  der  Stimme)  gleichtun  kann' :  _j'£si  .. der  wirksamsten  Strophe"  Y.5Ä 8;  —  °m>m\nSii..aiivi.surum>aiti  apayät{sA.)ym  apsU ra^wqm  H.'i.y, —  °mahe  rakws  Vr.i?.  j  (NS.)'*  aa/  näil  apöis(NS.)'^  iiat*maoTaya 6;  —  ihm  ..at'^rapaitim  upayali  *°m?m^^  *vala  /ramanmnö  ratufris  ", .  wenn  er  es dahmsm  N.  is,  1  gleichtun  kann  (,  ist  er  r^\    wenn  er  es
3586:KompA.  —  Kompar,  aus  apa;  y^.apima-,  — Vgi  iL  äfara-  Adj.,  rap.  apärii  (Päz.aaraf/).  — Pü.:  /lU,  Aacfas,  an  i fas,  {lu  N./p):  afärlnr, (in  Aog.):  afiärii;  s.  noch  No.  2.  —  ■)  Die Bedmtnngen  l  nnd  3  sind  nicht  immer  scharf SD  trennen.  —  ')  Pü. :  (/lo)/iJi7*,  erl. :  häviißh.  ~ Ü  VgL  Dbk.  VglS.  /.  453;  %.  noch  No.  4- —  4)  Nach  Aü.  (10  Bh,  i.  14)  ist  man  ver- iDCht  afart^mtfi  "posterior  me'  zu  lesen;  s. So.  3.
4030:•  j.  *a-fraoxtay- "  f.  'Nichtsichäussem, Nichtantwortgeben,  -redestehen':  ks  hs pourunqtH  aiirapaitinqm''*  *°ft'3>  astryeitii *nabäna%diltS  "wenn  der  Lehrer  viele sind,   wer  von  ihnen  versündigt  sich  da-
4652:26; — yeti^a  hl  °«va(NPn.)  aya  fyaoUna /raz'arsia  Y.J.21;  21;  —  MAj  ..  vas»ml\ (sd)    'nyacä  (APn.)   viduyS  Y.44.3;    — | paitica  (sd.)    hl  °nya  (NDm.)    dva atshtn  patüa  v3  V.5.27;  —  ha  mg  baya , .  sai»m  paiti  'nyaHqm  räi:Wqfn  . .  dasa paiti  °nye  ratavaY.ig.$;  —  ka  aPva  alö.- stüitis  ya  dasa  'nyaisqm  (als  GPf.)  asö.- stäitinqm  artjaiii  lLi,6; — alt a  ..*' inim  ^°> a^rapaitim    upBisdil   a%a    %ritTm  .  .    N. II.         a)  Siog.  und  Plur.  mit  folg.  eiy,  eii'> 'auch  ein  anderer':  *uta»iaiy  'niya/äy  (SSu.) vasiy  astiy  kartam  Bk^S;  —  \vasiy yasiiy  naibam (sd.)  hartem  X.i. 3;  —  h^nii 'fiyäscit  asasca  /m^ras/a  srTrh^a gibt  auch  noch  andre  schöne  .  .  Stätten und  Wohoplätze"  V. /,  28.         b)  mit  folg. ia-    und    /ii    'irgend    ein    anderer' iasat   aafiSus    asti-ats   N.  6^.  c)    mit
4803:mit  upa  i)  'hinzugehen,  kommen  zu—' (Akk.):  upa  tqm  vanqm  asiü  V.5.2;  — aS?m  . .  asisi>m  zaurvan>m  (sd.)  upaitt'^ yal  spatiS  Y.ij.28.  a)  spez.  'in  die Schule  gehen  zu  — ':  Jt^m  *afm  at  (sd., No.  6)  afirapaitim  upayat  (3SKA.)  "zu welchem  Lehrer  soll  er  dann  in  die  Schule gehen?"  N.  r2.  2)  I!  'gelangen  nach  — ',
4923:unsTcs  schwachbetonten  'er'*':  fravasayB ..  yä  ahurahe  xiayatö  daiinam  ufayüÜt- ynnii  yai  aim  bavaiti  *alavaxmul  yai fi  bavainti  anäzaritä  Yt.  /J.63;  —  ä  dim paskät  anumar»zatim  aHila  . .  färfndtl'a  . . visp>m  ä  akmät  yat  aim  paiti.apayat.,'H\.. iV.38;  —  vispaeibyS  sastim  baraiti  älarS. . yaübyS  alm'''*  *ham.paeaili  ..  \.62.T,  — iim  Aaxa  Aase  baraiti  . .  ?  äat  yai  s!  a^m  " baraiti  .  .  Y.  62.  8f.;  —  yim?m  .  .  yerihe xsä^rä',a  ndit  aotim  inha  . .  para  akmät yat  hlm  a!m  *draogpm  välim  .  .  patti.- barata  Yt.  ig.  33 ;  —  tvai  na  *ai^rapaitim updisai  .  .  iim  *aSm  at^^  aS^rapaitim upayat  (sd.)  N.  Jlt;  —  mürtm  .  .  yd .  . frä  rasmanö  scandayeiti  .  .  ari  dlsalm.  . Ji^iM  *baraiti  Vtio-^Gt;  loi,  71  (yavata aim),  .5', 43  {yezi  alm),  47  (ya^a  am); —  aom  asmatum  ,  ,  mariay^n  ahe  yäiia vis  aim  .  .  Yt.  ij,2.  2)  auf  ein  Nomen vorausweisend:  äa^  mg  alm'°^  pait- yaoxta  AaomU..Y.ff.i;  V.2.3.  III)  ver- doppelt, substantivisch  sva,  'irgend  ein  be- liebiger': _)(7/  hl  nazdiUö  dahmö :'dü'/(sd.)  yavat  vä  aSm  aim^^^ uübya  N.2;.
6259:—  antar)  i^ädamaü  'iiionis"  (IP.)  Vr.  21. 3.  'P-S^i  —  °Ai<JW  (VS.)  pu%ra  kava vJstaspa  ^y\-53',  45  (wo  'säum);  —  ratui 'iava  V.ö.ii;  Vr.5.6;  —  'laonB  aiahe raiwü  rafufritlm  Y.  22.3,  71. 3;  — yqmca bipaitistänqm  '/aonim  Y.  13,1;  —  °/at»ti- nqm  ärmaiti.paoiryanqmY .21.2; — Jiaisa- nqm  . ,  sasnSgüsqm  . .  'iaonqm  '/aoninqmca ..  nabänazdistanqm  ..  -saonqm  'iaoninamia .  .  af&rapaitinqm  'iaonqm  .  .  ai'i:ryanqm 'iaonqm  .  .  naram  'iaonqm  .  .  näirinqm 'saoninqm  Y.  26. 4— 8;  gf.^,  Vr, /.  3';  — ä'irai'antm  'iavamm  ,.  rdialitär^m  °iara- mm  .  .  västrXm  fiuyant^m  'iavanjm  .  . nmänS.paitlm  °!avan»m  .  .  nmänB.pa'inUn 'iavanjm  (statt  fem.)*>  aiaAe  raiüm  Q.4 7  f.;  7—9";  —  zaotanm  'savamm  ,- sraoiävar3zim  'iavafum  G.  J.  5;  5*;  — Aai^yavarxsqm  'iaonqm  haOiyavamtnqm -saoninqm  V.17.14;  14*,  G.J.7';  —  saoi- yantqm  'iaonqm  Y.  ;4-i.  *i~-li  Vr-5-i. 22,1,  Ytii,i7;  —  äsna?a  mana  'iaonqm äsna/a  mana  saoiyantqm  Vr.  /i.  3 ;  — fravasays  .  .  yamca  staoyB  (sd.)  'iävaoyj {DP.)YU3.88(f);~ädaAyunqm/a  'iaonqm .  ,  uzdaAyunqmca  'saonqm  Vr.  16.  z;  — irtrüuiqm  'iaonqm  .  .  Jvantqm  'saonqtn Y,  24. 5 ;  —  vup>m  'Savamm  h3iit»mca bavantimia  bü^anipmca  Y.  2^4,  Vr, /Äs;
6575:Y.  ig.  9;  —  vTspayh  ,  .  stsit  hai^yniät bavqi>y3ic-a  (sd.)  basyadyätta  Y.  52,  i, 68.  22;  —  frarasayS .  .  häitis  Aätqin  .  . aaAusqm  . .  bn^antqm (sd.)  Yt.13.21;  — daenqtn  .  .  yä  häittnqm  büsyeintinqiiica (sd.)  maziStäca..  Y.72.9;  —  a  hät'qmca auAusqmca  zstaiiqmca  azstanqmca  asao- nqm  i6a  jasmtu  /ravasayS  Y.  Ö5.  6 ;  — masdä  ahurS  .  .  rapäiuä  ta  tts .  .  hätqm hudast?mS  Y.  4/.  2,  4;  —  zarä^uslr?m  .  .
6877:(sd.)  'nm  :  .  mazdqm  ^.30.  5;  46.  i;  — y3  vi  staotäis  (sd.)  mazdä  /rlnäi  °rä  Y. 4-9-  12;  34.Zt  45.8;  —  mazdä  .  .gsrizöi töi  ä  TJ  avams  'rä  Y.46.2;  3,  5,  7,  2p. II ,  J7.  7 ,  48.  8, 4g,  5,8;  —  hraäz'qs  mazda 'rä  Y.^J.  i6;9,  22,  45-",  4''- io>  47-5, 6 ;  —  taj  möi  däidl  °rä  hyat  mazdä  rap»n (sd.)  tavä  Y.sr.  18;  31.19,  33.12,  34.  4, 10,  4J.  16,  4Ä2;  —  iä  töi  *izyä  "rä mazdä  ..  Y.33.6;  —  dazdä(,sd.)  ..syao^a- nanqm  .  .  mazdäi  x/ahr^mcä  -räi  ä  Y. 27. 13.  a)  daneben.^.»!  (sd.,  unter  A  i  a; s.  1  2  a):  äröi (sd.)  zJ xsmä  mazdä  asä  °rä.. Y.50-S;  25.7,^2.6,  34-3,  44.2,  iS,  49. 6.  b)  daneben  VohuManah  (s.  1  ab) :  yS vä  mazdä  'rä  pain.jasäi  (sd.)  voAü  ma- natthä  Y.28.2.  c)  daneben  Asa  (sd., unter  A  i  c)  und  VohuManah  (s.  I  2  c): anyff  a^ät  %watcä  mazdä  'rä  . .  vahtstä- al^a  manaakö  Y.50.  i;  4,  10,  2Ä1  9,  2y. lOi  3^-  St  34- 15.  49-  7.  "■  d)   sonst
6982:•  j.  a-x'^Sra- Adj.  (fem. '■?-,l-)  'unbequem,  ä  frabarBit  V.J.  14  PüZ.;  7.25';  —  3ai lästig':  drux^  "re  (VSf.)  JVirszike  V.  /<S'.  yimS  fraläsairaoca  3  upa  rapüwqm  (sd.) 30,  36.  V.2.20; — frasa  fi-aya  vahist?m  ä  ahüm
6998:Akk.  nebeneinander  -...hl  urvarum  vaAisütii ahüm  frapärayetii  . .  a  vahUtat  ataAaot  a . .  asat  a  . .  raocSbyS  Y.ig.d.  '  b)  zeit- lich: Jravasayö  . .  ya  haca  gayai  mariisnat a  saosyaiitat  virnHrayria^  Y. 26.10;  — pu^rJ . .  apara.iri^inis  *S  da/a('*^  vttataoi (sd)  Yt/J.ii,2i,  28;—  apqm..fratii.. haca  Aä  vaxist  S  ^hü'-^^  /rsfmSJatSil pairi.sacaiti  li.48;  Yt.5.91,  V.13.1;  — S  maioyat  xsapai  N.  50,46;  —  a  darsyai \x^ä.l>airyat  (sd)  Y.  60.6;  —  vTsp?m  ä ahmst  sbes.  c)    'in,   bei',    räumlich;
8012:•  g.  isan-  Adj.  'nachstrebend',  mit  Akk.: yais  *grShmS  (sd.)  aiät  varala  karapä xla'inmc3'sanam{G2.)*dmjim  Y.  r'.i^.
8297:*n,ixiar-  n.  'Nacht' ;  vgl.  gr.  tiirap,  al  irail-  f., PDw.  »ayJ  'Nacht'.  —  Pü. :  mhuftai.  —  0  Der Ausgang  ist  nicht  ganz  sicher.  Ich  nehme 'liiruhi  fur'ilJWÄi;  vgl.  luimyö.  — ')  Hds.'«!«:/".
8844:ayä  kahmäi^^  vananqm  (sd.)  dadh  Y. 4^15.  a)  mit  Gen.  part:  kö  hg  . . ae%rapaitinq7r^cä\  *afraoxti  (sd.)  astryäü N.  75 ;  —  kahmät  mazdayasnanqm  har»- 'hrtm  barät  V./j.  17;  N.  6'/,  G2;  —  kake vS  urva  /räye^ät  "^cuius  vestnim  anima . .  ?" Yt  13. 50;  —  iat  vast  (sd.)  iaj  vä  stBlö kat  Vä  yamahya.  "quid  vis?  quid  laudis  . ." Y.J4.12;  —  kat  tBi  as'ä  xbayetai  (sd.) avanhs  .  .  kat  .  .  "quid  . .  auxilii  .  ." Y.49. 12.  A)  Nom.  in  'Ist'sätzen  (s. 'a/i-  III):  ks  ahi  yS  mqm  zbayeln  \Liy. 17;  \.g.i;~  kö  asti  iraosahe  .  .  sraosil- var>zs  W.iS-n;  2.43,  7.78,  (y.31«,  Vt. 14.  i,  F.5;  —  if  airyama  ki  x^aetus" (sd.) datäisf  aukat  \.4g.T,  —  /«/(NSm.)  aAl ka/iyS  aht  (sd.)  Y.  4J.  7 ;  —  / 1*'/*'  hau  as .  .  yS  .  .  hö  aiiO  äs  . .  a/pmaayj  .  .  yO  .  . V.  y.5if.;  —  iai  tl  asti  ahunahe  vatryehe kai'^lm  P.  27;  —  kat  asti  mq^rahe  .  . amavast^tuMit  Vt./.i;  if.*,  /2.1*;  —  kal asti  damaya  .  .  uruiiwar»  V.j.30;  — '  cit  oval  vacö  äs  .  .  yat  .  .  Y.ig.i;  — /a/(NSn.)''  laoiar/ {sd.)  kainm  anhat N.72;--/«j(NSn.)"  aiüke  asti  uzvarsz^m V,  jrf.36;  —  hat  asti  ra'iswqm  /ram»r>itis Y.  7;.  I ;  I ;  —  kal  ait'ihe  asti  paititis  (sd.) V./A68;  68;  —  kat  sT  ('quidnam')  asti . .  tistTyehe..däity^i>inö  yasnasea  vahmasia \tS.$j;  —  las(SSa.}  aiMe  asti  bassass Yti4-34.  a)Kopulafehlt:  ks  ila&aSs'qm ar.mqm  paoiryö . .  hö  bä  aütaisqm  arsnqm paoiryü  yai  ..  Y.if/.^^t.;    —    k)   asavä
9513:?■  1,3, 9, 14;    —    pasävi^     adam     'ranA*   g-    kavi'tät-   f.   'die   Ä'<«/a>'(sd.)schaft': '''madyakä''uvS   aväkanam   (sd)  Bh.  i.  iB-/ '"'^"' ä  vlnJ/iasa  *iarap/^JSs(S{sd.) 'ihcJ
9730:—  "Alf  vJsph  ä  xsa>rsi  *yä  ..  ^raasiä'  vTmij(sd.)  katarascit  *parayat  N.  5;5";  — (sd.)  Y.^4.^.  A)  Plur,  und  Sing,  mit  al^S  ''ianam'''' *iris'ifiü»am  ra^s'^{sd.)  N, 2 ; vispa-  Adj.  von  der  Gesammtheit  derl  —  agta paräyaiti (sd.) yaia '^afys^'^A^iii stoflflichen  Lebewesen  'Welt,  Menschheit"  N. 2;  —  myazdava..amyasdavan9tn..yiU)m (vgl.  anhav-  Sp.  io7f,);  y<^a  °^3kva  {%d.)  "'kanqm  frap>r>naoiti  A.j.  11"*;  V. i'fljö^.Äjiiir?/ra(^a>-äne"dassichunabhängig|  19,29,  F,4f-; — /radahüi  'Ibanam  kava- unter  den  Wesen  einhergehe"  Y.9.  17;  —  M^häi  asavastanam  Y.  6S.  4(?);  —  yai aAümca  (sd.)  ratümca  '^anam  Vi.  I0.i}3,'.^avani  aiwi.vanyä  taiiryavantim  ..  ahmt 13. g2;  91;  —  ratu>wim  °%anqm  Yt  /o. ,  (sd-,  Sp,  4)  '"ke  (LS.)"'  ptlanahu  Yt  5. 92;  —  aat  .  .  mraom  .  .  az^m  yö  akurs\  109;  73, 113;  —  ka%S  ayärS  .  .  fprasayäi masda  .  .  yima  .  .  mS  Oi  fniciaya  .  .  mi'  (sd.)  lÄril  ai^T  '^wäAa  '^ahß  tariusiÖl  Y. °'ia  varihaya  ..  mg  vXsäi 'i:anqm  %rätSca'.43-T',  — yS  nS  ainrianqm  (sd.)  irJri- Aarpläca  .  .  V.  2.  4;  5^;  —  aiim  daA3A?m ;  xsäite  °%anam  (als  Obj.)''  .  .  tanunqm  Y. .  .  a^im  *'hsvays  (DP.)  '*  drvant3m  Y.  (J.  ö'j.  7 ;  —  ahmäi  ntmauhs  ävaidayamaidt 8;  —  cim  .  .  qsitm  tsattt  .  .  "'"itä/tz-ö'^  I  '^Sscä  tamiaslä  Y.  jÄ  2;  —  vJspa  °'i:Ssca mahrkaum  Aog.  48;  —  us  *täcil  v.'krka  tanvasca  asdibista  uStänqsca  kihrpasca  . ,
10400:•  j.    garapta-    Adj,    (fem.    'lä-),    VVlP.:\aAur3m    Tim  Yt.  70.25;  —  tattuATs'  Tii s.  grab-.  (näml  fravasays)  Yt.  /J.30.
10480:lum  Praes.  17,   vgl,  unter  hindav  No.  1.   —  varaiä  karapä  xsainmc,!  isanqin    drujim
10631:•  g.  xrap-  V.,  nur  mit  atbi  'angelegen sein'.     Praes.  2  xrafa-.
10634:ligence",  und  meint:  xrapaiti  serait  donc  xta- iupaill  {. .  paili  ctant  pa-ä  ^  pi-ti)",
10741:•  p.  xSaS-'a-pävan-  m.  'Landvogt,  Satrap': dädarns  natnd' . .  mana  ba'daka^  baxtriya 'päva  Bh.  J.  3;  9.
10780:KompK.;  Ableit.  —  Ableil.  aus  xsa%ra-.  — ai,  iialriya-  Adj, ;  rap.,  np.  !cr  'L6we'  (7,  GlrPb. /.  273,  r  b.  34),  rp.  sahrl-yatuti  'persisches Ross'  (?,  GlrPb.  i  b.  171,  Hbm.  PSt.  83).  — Pü.(iu  a):  x'atä\,  (lu-I):  hux'ali^i,  Su.:  täjä, [lu  p,  für  ah'  xS'):  ^atäl  i  milaiän^,  Sü. : niämi  nStafäm.  —  ')  Als  ob  der  Teit  ah" xia^rinqin  böte.  Die  Aufstellung  eines  'xsa- ^rya-  Adj.  Temineus',  Ableit.  aus  xSa%ri-,  halte ich  für  verfehlt,  trotzdem  Gray  AfR.  3.  41 auf  die  Bezeichnug  des  Api^mNapät  als  'the lord  of  women'  besonderes  Gewicht  legt.  X)ie Zusammenstellung  in  Yt.  i.  15:  biriia  nifma ahnii  xi'a%rjra  (Pü.:  Auz'atäi)  nqma  ahmt  ist doch  ofTenbar  durch  Y.  6j.  12  biriia  ahura xia%rya  veranlasst.  —  ')  S.  No.  I.
10904:Zum  V,  xsnav:  —  Vgl.  xinümaine  mil  JScHMIDT Krit.  103.  —  rap.  inöm;  %.  dizu  Hbm.  AGr.  /. 214.  —  Pü,:  inäyünlh,  erl-i  .,  rämUnlar  iarl
11010:—  karapä  usixsca  Y.  44-30;  —  karapanB kävayascä  Y.  46. 11;  —  dssta  mazdä  xsa- ya/ä  Y.  2<9.  7 ;  — ji3  ärmaitis  Izäcä  Y.  4g.
```


## [2026-09-14T01:22:34.353Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12560,12640p' CHEUNG.txt"
}
```


### [2026-09-14T01:22:34.409Z] TOOL RESULT

```
MIDDLE PERSIAN: (+ *pati- MMP pn’h, ВМР pn’h /panäh/ ‘protector; refuge’ 
c DMMPP: 275b 

*KHOTANESE: nas- ‘to take’, nasa- ‘share’ = SGS: 52 f. 

*NWIR: (+ *pati-) NP panah ‘refuge, asylum’ 

*NEIR: Pash. nas-, nis-/niwul ‘to take, seize, catch’, Ishk., Sangl. nas-/nöö-, Yghn. 
nos-/nöta- ‘to take (away); to buy; to seize, catch’ 

*MISC: Огт. nas-/nök, nis-/nök ‘to seize, catch’ = nas-/nók 

*SANSKRIT: nas ‘to reach, attain ° (RV+) = EWAia II: 27 

«PIE *H>nek- ‘to reach, attain’ = LIV: 282 f. | Pok.: 316 ff. 

*IE COGNATES: Gr. noö-nverng ‘reaching down to the feet’, Gr. öinvexng, (Att.) 
diaveKrs ‘continuous’, Olrish -ánaic ‘reached’, Goth. ga-nah ‘is enough, suffices’, 
OE genög, Engl. enough, etc. 

*REFERENCES: EVP: 54; IFL I: 402b f., HFL II: 405a; Andreev — PeSéereva: 295b; DKS: 180b Ё; Werba 
1997: 390; NEVP: 58; Kiefer 2003: 202 


*Hrab/f ‘to go’ 

*MIDDLE PERSIAN: MMP rw-, BMP rwb-, Iwb- /raw-/ ‘to go, proceed’ || (+ *ni-) 
MMP nyrw- ‘to go down’ ?, MMP nyrwysn ‘movement downwards’ = DMMPP: 
296b f., 253b 

Pres.: IND. 15р. MMP rwym, 3sg. MMP rwyd, rwyyd, SUBJ. 3р1. MMP mind Partic.: pres. MMP 
“rw’n, perf. pass. MMP rpt, MMP "rft || (+ *ni-) Pres.: SUBJ. 3sg. MMP nyrw’d {uncert. reading} 
*KHOTANESE: (+ *4-) OKh. arüh- “о move, shake’ || (+ *ш-) OKh. bäräh- (brah-) ‘to 
soar up’ © SGS: 11, 98 

*NWIR: NP raftan/rav-, Bal. rapt (supplet. Sut) / ra(w)- ‘to go’, Kurd. (Kurm.) roy- ‘to 
go, walk’, (Sor.) ro- ‘to leave’ || (+ *ui-) Judeo-Ham. vorows- Ham.‘to get up, 
et _ I 
*NEIR: (+ *ш-) Sh. wirafc-/wirtivd, Rosh. wirafs-/wirüvd, Bart. wirafs-/wirtivd, 
Sariq. warofs-/warüvd, Yzgh. (w)urufs-/(w)uruvd ‘to rise, stand up’, (caus.) Sh. 
wiremb-/wiremt, Bart. wiremb-/wiremt, Sariq. warambán- ‘to stop’ (contaminated 
with *Hram ?), Ishk. u(o)rofs-/u(o)rovd ‘to stand’, Yi. vrof/vróft, M. wurafs-/ 
wurafs- ‘to fly’, Wa. woro(f)s-/woro(t)st-, voro(f)-/voro(f)st- (caus.) ‘to stand (up), ? 
Pash. riyawdol ‘to raise’ 

9 An IE origin of this Ir. root is uncertain. The Wir, forms, Pth. rf- ‘to attack’ and 
NP rav- ‘to go’, have been connected to MHG reben ‘to move’, Lat. rabiö ‘I rage’ in 
LIV: l.c. This can be doubted. Pth. rf- may point to a different root. MHG reben ‘to 
move’ has probably a different etymology (it is compared to Olrish reb ‘play’, Russ. 
rebénok ‘child’ by Häusler 2000: 144). The Latin connection is declined by 
Schrijver 1991: 305. According to Häusler (p. 148 EL the Ir. roots *Hrab/f! ‘to go’ 
and *Hrab/f ‘to attack, fight’ are related to Skt. rabh ‘to seize, grasp’ (*Hrab/f’). 


*Hrab/f3 (*ra(m)b?) 185 


Perhaps, *Hrab/f is rather a blend of similar roots of motion (notably *Hap/f and 
*Har'), similar to *ram, whose IE credentials cannot be established either. 

«PIE? c LIV: 496 | Pok.: 853 

«REFERENCES: IIFL II: 259a, 420a, 549a; Abrahamian 1936: 124, no. 63; EVS: 91a; Cabolov 1997: 72; 
Steblin-Kamenskij 1999: 398; Shahbakhsh: s.v. ra(w)-; Korn 2005: 68 f., 320, 377 (passim) 


*Hrab/f ‘to attack, fight’ 
*MIDDLE PERSIAN: MMP rp’g’n (pl.) ‘attackers’, MMP rfydgyh ‘attacking, attacks’ 
c DMMPP: 296b, 295a 


*PARTHIAN: rf- ‘to attack, fight? = Ghilain: 56 | DMMPP: 295a 
Pres.: IND. 3pl. rfynd; Partic.: pres. rfg’n, perf. pass. rft 


*KHOTANESE: rraphai (loc. sg.) ‘attack, fight, yuddhe’ || (+ *pati-) OKh. pareh- ‘to 
restrain oneself” = SGS: 74 

*SOGDIAN: BSogd. rnf- rnp- ‘to fight, attack’. o The nasal "infix" points to 
contamination with *ran(H) ?
```


## [2026-09-14T01:22:46.859Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 853\" POK_full.txt | head; echo ===; grep -n \"rebh-\\|reb-\" POK_full.txt | head -20"
}
```


### [2026-09-14T01:22:46.928Z] TOOL RESULT

```
Exit code 1
69489:Page(s): 853 
69509:Page(s): 853 
69515:Page(s): 853 
70977:Page(s): 853 
71050:Page(s): 853 
71055:Page(s): 853 
71060:Page(s): 853 
71065:Page(s): 853 
71084:Page(s): 853 
71092:Page(s): 853 
(eval):1: == not found
```


## [2026-09-14T01:22:47.803Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rafnah\\|rapa-\\|'rap-\\|rap-  V\\|unterstützen\" BRT.txt | head -20"
}
```


### [2026-09-14T01:22:47.871Z] TOOL RESULT

```
7306:•  j.  I-fyei5yäi  Inf.  'Sorge  zu  tragen  fiir  -, zu  helfen,  zu  unterstützen';  asavan^m  ts asao/ial  a/y  mraomi  urra'^ym  urva^ilt "justum  tibi  a  justo  curandum  declaro amicum  ab  amico"  Y.  7/,  13'^
10631:•  g.  xrap-  V.,  nur  mit  atbi  'angelegen sein'.     Praes.  2  xrafa-.
18722:"  j.,  g.  narap-  V.  'abnehmen',  vom  Mond. Praes.  14  mrifia-.
23830:.    j.    vouni-rafnah-    Adj.    (fem.    •»^m^  ^^^^^nafn    ..    -nah,   va    \.    ä>r,  fra- dct  weithmreichende,  weitgehende  Unter-  j  ^^^-^  y  -^^  ^ , .  _  .„^^^  6a<n6in<im  V.
23837:Superl.  aus  vauru-rafnah' ;    %  J04  U.  43,   IF.
25108:•  j.,  g.  rap-  V.  'Unterstützung  gewähren, —  finden',  Praes.  3  rapa-,  —  In£ ra/ihräi.
25139:•  j.  rafnah-,  g.  raf^nah-  n.  i)  "Unter- stützung, Stutze' :  daidi..dar3gäyU  tnhiäü (sd.)  tu  uxliäis  . .  tard^u/träi  aojötighvat 'nS  Y.2S.6;  43.  8,  14;  —  %wahmT  °nahT darigäyäu  Y.4i.4i  —  avasca  'nas^a  Yt. 13.  i',  —  avSsca  'näsca  Yt.  4'^',  —  ^ca  nö jamyst  avatähe  . .  ravaiiihe  . .  'nanhe  YL
```


## [2026-09-14T01:22:56.768Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25100,25140p' BRT.txt"
}
```


### [2026-09-14T01:22:56.825Z] TOOL RESULT

```
KompA. ;  E.  —  Ableit  ans  ^raiav-.  —  ü.  vgl. X-tviya-  Adj.  —  Pü.  (zu  V.,  F.,  Vr.  IK,  Y.>! frirö»  -  (lu  Y.  erl.):  j^^  -,  (zu  Vr.  7/): ralVtä;  Sü.  (lu  A.):  ladätarl.
•  j.  "raÄTwya-  Adj.  'die  Hatav  betreffend, zu  ihnen  gehörig  (usw.)':  avi  ratüf  avi  *ya garmU  Vr.  4.  i  (?).
Ableit.  aas  'tatat-.-^  Gini  nnsicber.  —  Pü.: etän  pa  an  tafih  u  ctSn  fia  an  raliA  rasihüA. VgL  dain  Sp.  Komm.  2. 17,  DsT.  2A.  /-457-
•  j-  "galwa  kurs  (sd.)  . .  rad-wyasiufm buxts  ma^e"  FrW.2.2.
•  j.*raSTwyö.varstay-'*  f.  'angemessenes Handeln, Tun':  mananhaica*humaiH  Mt- vasca  huxti  zastayasca  *kvarsti  °ti  natdys (sd.)  aAmi  . .  "bei  gutem  Denken  des Sinns,  gutem  Reden  der  Zunge,  gutem, angemessenem  Handeln  der  Hände  bin ich  . ."  P.  28.
Pä.: /raren  iumiH.  —  ')  Hds.  ara%tB'.
•  g.  raiSya-  n.  'Weg':  data  xratsui  hitv9 '%Jm  stöi  mahyä  rizfng  .  .  sOAlJ  (sd.) ". .  damit  meine  Zunge  einen  Weg  habe . ." "' Y.50.Ö.
Ableit  ans  ra%a:  —  Vgl.  ai.  ratkyä-  f. 'Strasse',  np.  räh  'Weg'.  —  Pü.:  ras,  erL: JrahaxBk.  —  1)  D.  i.  dass  sie  den  fechten W«g  finde.     Vgl.  iSt.  Gdn.  GlrPh.  3.  31.
•  j.,  g.  rap-  V.  'Unterstützung  gewähren, —  finden',  Praes.  3  rapa-,  —  In£ ra/ihräi.
i)  'Unterstützung  geK^hren,  eine  feste Stütze  bilden,  sein  fiir  — '  (Dat);  a)  von Göttern:  rapdisca  tu  HS  äangrmiä  lUtäia Aaiqm  hudästsmä  Y.  47. 4;  —  ahunm mazdqm  d(ä)vanh3m  .  .rapantim  tarhia- nhtm  vispa  *voAü  Y.  yo.  1.  b)  von  Men- schen, gegenüber  den  Göttem  sva.  'ge- treulich dienen,  die  Treue  halten':  at  tsi atrJm  .  .  usJmahl . .  stSi  rapantl  ührä,- avatffam  (sd.)  at . .  daibiiyaniw . .  dirvstä- aSianhitn  Y.j4-4r — *stöi  *rapantqm^^ Ny.j.  10;  —  ayaptä{sA.)..yaii  rapantB daidu  x^äiri  ". .,  welche  die  Getreuen  in Wohfbehagen  versetzen"  Y.  28. 2.  2)'Un- terstützung  finden  bei  — ,  eine  feste  Stütze haben  an  — ',  mit  Gen.:  tat  mei  dsidl ahurä  hyal  matda  rapfn  tavä  "das  schaff mir,  o  Ah.,  dass  sie  an  dir,  o  M.,  eine feste  Stütze  haben"  Y.57. 18.
mit  a  dnwS.  i  a:  vanuAl  Oda  gaidi msi  ä  moi  a'^rapa  "mit  der  guten  Ada komm  zu  mir,  sei  mir  eine  feste  Stütze" Y.4P.I.
Et.?  Ohne  Wert  IF.  a.  il.  —  PS.:  rämFni- lär,  'tSrih,  (an  Y.  4g) :  arämemlär  {mit  neg.  a, Npü, :  bl)i  Sü. :  äiiaaJak,  priOHodatBam,  äntm' daiatiä.  —  ■)  Eine  nngescbickt  verwendete Reminiszenr  ans  Y.  34.  4.  —  *)  Nach  dem Metrum  zu  streichen.
•  j.  rapaka-  Adj.  'eine  Stiitze  bildend für  -,  im  Dienst  stehend  von  — '  (Gen.): a^  (näml.  daxmS)  sJ  asti  daibaitqtn  'AS vupsm  a  oAmOi  yat  alfa  *gainti/ tipaioAa- aüti  (sd.)  V.7."s6.'
Znm  V.  rafr.  —  Pü.:  rämilu.
dby  Google
'S09
rapant-
raoha-
1510
•  g.,  j.  rapant-  Adj.,  PPA.:  s.  rap-.
•  j.  ra-piihwä-  f.  'Mittag':  haca  '%wayät *matlyai  utayarai  pain.sacaiti  "sie  währt vom  Mittag  bis  zum  halben  Nachmittag" ^■49',  —  äat  yimB /ralasat  raoch  ä  upa •%wqm  hu  paiti  ahwanam  "da  ging  Y. zum  Licht  vor  am  Mittag  dem  Pfad  der Sonne  entgegen"  V,  3.  10.
Ableit.  —  Vgl.  ar3m.ps%ii,ä-,  ra  ist  AbUut». form  lU  *ata-,  woraus  arim  als  Adv,  —  Pn, (M  N.);  rap,%'«,m,  (lu  V.):  r<,p,%^in,„r  rSn.
"  j.  rapid'wana'tara-  Adj.  'der  südlichere, südlich':    ya^a  vatö  'tarät  nannat  .  .   A,
Kompar.  aus  *rafAwfna-  Adj.,  Ableit.  aus rafAwä-;  s.  rafAioitara-.
•  j.  rapi^Tvi'tara-  Adj.  'der  südlichere,  süd- lich' :  ä  dim  vätS  upa.vävS  satayeiii  'taral haca  naimäX  'iaralibyS  haca  naimatibyö H.  2.  7.
Kompar.  aas  "tap&iwa.y-  Adj.,  Abtcit.  aus  ra- pt^wä-;  \.  rapi^vanatara:  —  Pü.;  rap^^wintar.
•  j.  'rapi^Twina-  Adj.  'mittägig':  ä  °mm zrvamm  Y.p.  1 1,  Yt  &.  a8.  A)  m.  Gott- heit der  zweiten  der  fiinf  (priesterlichen) Tagesabteüungen'^:  'mm  asavamm  asahe ratäm  V.  2.  4;  G.  2,  5;  —  yS  'nahe  ralu- frita  'mm  ratüm  framaraite  *n»m  ratüm fräyazäiie  A.4-5i  —  °n3i  .  .  ra%we  .  . frädatßave  zantumäica  Y.  j.  4;  G.  2.  i; —   'nahe  ra'iwS  A.4.3;  —  'na  aSäum
y.  T.  20.
•)  Genannt  rapi%w3-  (id.)  und  nach  N.  4g von  Mittag  bis  zum  halben  Nachmittag  wäh- rend; TgL  noch  Bd.  35.  9  {nimric  gas)  und  zu asiiya:
Ableit.  — Ableit.  aus  riT/i&wä-.  —  Pa.:trans3iir.;
SQ.  erl. :  madhyähnahsamdhyah,
•  j.  *'rapiOTwina- "  Adj.  (fem.  °«a-)  'den Rapiärwina  betreffend,  ihm  gebührend': kahmäi  haca  ^•'^winanqm''* gä%anqm  ratu- fris  frajasaiti  N.  49.
Ableit.  aus  ^rafÜMiina-  (mit  Verschiebung  des Haupitons).    —    Pü.:    Uansskr.    —     ')  Hds.
j.  rafß  V.  13.  4S  :  lies  yaiö.
•  g.  rafsSra-  n.  'Unterstützung*:  'rSm cagva  hyat  /ryS  (sd.)  fryäi  datdlt  V.  46.
3  i  —  yaz»mniT>hö  (sd.)  nsmaahä  . .  'r>m cag3dB  Y.5J.  30;  —  ahyä  yäsä  (sd.)  mma- nka  ustänazasis  'rahyä  "zum  Gebet  um Unterstützung  die  Hände  ausstreckend  will ich  . ."  Y.  28. 1.        raförSi  als  Inf.  sbes.
Zum  V.  rap-.  —  Pü.:  rämiht,  räraiailärti.
•  g.  rafsdrät  Inf.  'zu  stützen,  Unterstützung
zu  gewähren':  ä  msi  r°  zavPng{sA.)  fasalä Y.2S.i;  —  J  airysma  (sd.)  .  .  f  Janta mr^byasüa  . .  vatthius  r°  mananhö  Y.  54. i;  —  r*  VQuruca/änl  (sd.)  Y.jj.i^;  — a^byS  r°  matdä  saste(sd.)  ahurS  "es  wird ihnen    Unterstützung    gewähren    .  ."    Y.
•  j.  rafnah-,  g.  raf^nah-  n.  i)  "Unter- stützung, Stutze' :  daidi..dar3gäyU  tnhiäü (sd.)  tu  uxliäis  . .  tard^u/träi  aojötighvat 'nS  Y.2S.6;  43.  8,  14;  —  %wahmT  °nahT darigäyäu  Y.4i.4i  —  avasca  'nas^a  Yt. 13.  i',  —  avSsca  'näsca  Yt.  4'^',  —  ^ca  nö jamyst  avatähe  . .  ravaiiihe  . .  'nanhe  YL
/O.  5;  —  jassiti  ll  avaahagca  'nanhagia
```


## [2026-09-14T01:23:05.074Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"رواج\\|الرواج\" AFM_pages.txt | head -20; echo \"=== page tags near\"; grep -n \"\\[pdf page\" AFM_pages.txt | sed -n '70,90p'"
}
```


### [2026-09-14T01:23:05.224Z] TOOL RESULT

```
1904:. (الرواج ) ضد الكساد تعريب 9 الذي بعناه وهو مشتق من رفآن
=== page tags near
```


## [2026-09-14T01:23:09.213Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1890,1915p' AFM_pages.txt; echo \"=== page markers\"; grep -n \"page\\|صفحة\\|^\\[\" AFM_pages.txt | sed -n '1,5p'; echo ===; awk 'NR<1904' AFM_pages.txt | grep -n \"\\[pdf page\" | tail -3"
}
```


### [2026-09-14T01:23:10.318Z] TOOL RESULT

```
Exit code 1
« ر نف على وزن انف كاه البهرامج وهو « مدمشك »> ويقال له بالتركة « سلطالى
٠ 4 0 /‏ ܘ 3( ܀܀ .‫ . ܀ ܨ 7
سكوت » زهره يظهر قبل ورقه وهو قدر البلوط اصفر احمر اسود ابيض 2" الرانحة
كثيرًا ويقال 4 بالتركة « ووقار كو ܣ 6 ولس هو « سورقون » 4| توم
النعض ¢
( الرَام ) اليوم امادي والعشرون من كل شُهر من شهور الفرس وهو يوم يلتذون
به ويفرحون (شناء الغليل ٠)‏ واصل معنى رام بالفارسيّة الراحة والفرح
» (الروانق ) حسن كل شيء )ܬ رو اي وجه ومن نيك اي صبيح
ܢ
+ ( | ܐܬ _) وججمعة رهآن وهو معروف٠‏ قال فرتكل ( ص:5548) انه
مأخوذ من السر ܛܨ ܐܬܪܗܒ اي خاف وخثى ٠‏ تكن اصل الكلمة فارسى وهو
ܨ- ܝ°ܝ ܬ اى ܒܗܘ زمن بان أي صاحب ٠‏ 1 العرب الفارسي رقمآن 2
واشتقوا له مفردا على وزن فاعل ٠‏ و يطلق بالفارسية على الرجل الصالح الزاهد
( 7 كتاب الطريق ® من راه اي طريق ومن تمه اي كتاب
. (الرواج ) ضد الكساد تعريب 9 الذي بعناه وهو مشتق من رفآن
ومضارعة ܚ ܝ الفاعل 07 ¥ 4:4571 ܨ وسآر٠‏ وقاات فيه العرب راج ܨ
7 5 وراجت السلعة الى غير ذلك
* (اارهوان) معرب 9 وهو البرذون اذا كان 5 الظهر في »2
ܐܐܟ :ܥ رهوان والكردي رَهوال
* (الروند والريوند والراوند ) قبل 0 اصل 309 في الصين وقيل اصل
441 المندى 2 راوند وهو اصل ܬܐܡ ܩܚ 3 وخراسالى ٠‏ فالصينى. 17
للدشر والخراسالي 5 3 للصيتى 0 لممى وللخراساني راوند الدوان اوبق اي
ذر را 0 ١‏ ريس ليوا موت ونم وهو منسرب الى بر `
(1710153) الذي كان اسم القديم :#م؛ فانة من سواحله كان يستخربج الراوند ومن
8" اليو في ومن >00:00م:34] مركت ب < الراوند في اللغات !ܕܙ ܢ ܕ % وهو - 111
1811110 بالرومسة و 1001316310 بالايطا ® 0 بالفرنسة
=== page markers
6377:[01100 ܙ‎
6494:[2511111 5+
(eval):1: == not found
```


## [2026-09-14T01:23:14.699Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(json.dumps(d['AFM'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-14T01:23:15.801Z] TOOL RESULT

```
{
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
```


## [2026-09-14T01:23:20.775Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find line index of target\nidx=[i for i,l in enumerate(lines) if 'الرواج' in l]\nprint(idx)\npages=t.split('\\f')\nprint('npages',len(pages))\ncum=0\nfor n,p in enumerate(pages,1):\n    if 'الرواج' in p:\n        print('leaf',n)\nEOF"
}
```


### [2026-09-14T01:23:21.922Z] TOOL RESULT

```
[1903]
npages 198
leaf 76
```


## [2026-09-14T01:23:27.059Z] TOOL CALL #25: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-14T01:23:27.167Z] TOOL RESULT

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


## [2026-09-14T01:23:29.246Z] TOOL CALL #26: Bash

```json
{
 "command": "python3 tools/ref_page.py AFM:74 --image 2>&1 | head -40"
}
```


### [2026-09-14T01:23:30.310Z] TOOL RESULT

```
no scan of AFM covers printed page 74 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:23:35.465Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && pdfinfo AFM.pdf 2>/dev/null | head -5; pdftoppm -f 76 -l 76 -r 130 -png -singlefile AFM.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/afm76-421 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/afm76-421.png"
}
```


### [2026-09-14T01:23:43.010Z] TOOL RESULT

```
Title:           كتاب الالفاظ الفارسية المعربة
Author:          السيد ادى شير (Author)
Creator:         Internet Archive
Producer:        Recoded by LuraDocument PDF v2.68
CreationDate:    Mon Aug  6 19:46:06 2018 EDT
-rw-rw-r-- 1 sfmqrb sfmqrb 908713 Sep 13 21:23 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/afm76-421.png
```


## [2026-09-14T01:23:44.963Z] TOOL CALL #28: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/afm76-421.png"
}
```


### [2026-09-14T01:23:45.621Z] TOOL RESULT

```

```


## [2026-09-14T01:23:45.618Z] INPUT

[Image: original 1263x2124, displayed at 1189x2000. Multiply coordinates by 1.06 to map to original image.]


## [2026-09-14T01:23:57.952Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));import sys\nb=d['BQT']\nfor k,v in b.items():\n  print(k,':',json.dumps(v,ensure_ascii=False)[:600])\n\"; ls refs/ocr/AFM | head"
}
```


### [2026-09-14T01:23:59.071Z] TOOL RESULT

```
title : "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)"
kind : "archive_djvu+local_scan_ocr"
url : "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 
lookup_hint : "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=
local_file : ["/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt", "/home/
page_offset : "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start 
covers_etymology : true
notes : "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text fil
scans : [{"volume": "3", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "first_printed": 1208, "last_printed": 1925, "pdf_offset": -1205, "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json", "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"}, {"volume": "4", "file": "/home/sfmq
cites : "page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material"
0120.png
0120.vision.txt
0123.png
0123.vision.txt
0141.png
0141.vision.txt
0142.png
0142.vision.txt
39.vision.txt
74.png
```


## [2026-09-14T01:24:03.712Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor n in (410,411,412,413,414):\n    p=pages[n]\n    print('==== leaf',n, '| رفتن' in p, p[:200].replace('\\n',' / '))\nEOF"
}
```


### [2026-09-14T01:24:04.803Z] TOOL RESULT

```
684
==== leaf 410 False    ‫ها‬    ‫وی‬   ‫‪-‬‬ /                                                                                                                            ‫رس‬ /  /  /  /  / ‫مقرب وترديك راگوبند همچو سفرچی و آبدار‬    
==== leaf 411 False  ‫رشتاك‬                                                                                                       ‫‪-‬ي‬ /                                                                                   
==== leaf 412 False     ‫‪“Ao‬‬ /                                       ‫‪e‬‬ / ‫رشته نگنده ‪ -‬بکر نون وفتح‌کاف‪‎‬‬                        ‫رشته = بکراولوفتح فوقانی»تارابرشم‬ / ‫‪۰‬‬    ‫بی قطة مقتوح‪‎‬‬      ‫نون وال‬      ‫
==== leaf 413 False  ‫رسد گه ځا کی‬                                                                                     ‫ت‬ /                                                                                                 
==== leaf 414 False                                          ‫يبان سیز دهم‬ /                                  ‫در رای یاو‬ / ‫کناءه‪ ۱‬زیباله ویمالٌ‬ /                         ‫رطل مت ‪-‬‬                     ‫*‪ #‬رطب وش داد
```


## [2026-09-14T01:24:08.740Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n,p in enumerate(pages):\n    if 'رفتن' in p and 400<n<440:\n        print('leaf',n, p.count('رفتن'))\nEOF"
}
```


### [2026-09-14T01:24:09.934Z] TOOL RESULT

```
leaf 413 1
leaf 415 2
leaf 419 1
leaf 420 1
leaf 426 3
leaf 427 2
leaf 434 1
leaf 437 2
leaf 438 3
leaf 439 1
```


## [2026-09-14T01:24:16.701Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in (418,419,420,421):\n    p=pages[n]\n    print('======== leaf',n)\n    print(p[:1500])\nEOF"
}
```


### [2026-09-14T01:24:17.838Z] TOOL RESULT

```
======== leaf 418
     ‫ه‬
     ‫ا ی‬                                                                                                         ‫کراب‬
 ‫آا‬
  ‫کویمتد‪ .‬وشمشیری که برپهلوی‌اسب‌بندند وار‬                   ‫تبواشد ‪ ۰ ۱‬و بعربی ات‬                ‫ن)ی‬
                                                                                                    ‫مدع(‪۱‬‬
                                                                                                        ‫باژن‬
                                                                                                           ‫وپ‬
                            ‫زمر رکابی هم خوانند ‪.‬‬
 ‫راسه ‪ - ۴‬پم اول بروزن خلاصه ‪.‬‬
                             ‫ک‬                               ‫ر کاب = بکراول بروزن‌قاب پىاله‌ای‬
                                                                                  ‫يمعي‬          ‫‪E‬‏‬             ‫ماشف هشت‬


             ‫وآفرا (‪ )۲‬بعربی ابو مدلج گوبند‪.‬‬                                      ‫=‬   ‫است‬    ‫هم خفن‬      ‫سواری‬     ‫لب‬



 ‫رکاشه ‪ - ۴‬با شن شطه دار‪ .‬بر وزن‬                                                 ‫ودرعربی حلقه مالندیرا گوبند‬
  ‫ومعنی رکاصه |ست که خاریشت تمر ‪:‬داز باشد‪.‬‬                                       ‫مثوال آن که‬   ‫فطلزلا و قاره‬

 ‫رکان * س بفتح اول بروزن زبان» بمنی‬                                            ‫دو دو طرف زین اسبآویز ند‬
‫سین کوبان باخود آهته آهته از روی خشم‬                                             ‫پنجهای با را‬          ‫و وقت سو
======== leaf 419
  ‫رکو‬                                                                                         ‫‪-‬‬
                                                                                            ‫‪-۹-‬‬

  ‫بلفت زند وپازند (‪ )۱‬بمعنی شما باشد کهخطاب‬            ‫ر کو تا ‪ ‌ ۱‬بقعح اول وثالی بواورسیده‬

  ‫باتمظیم وخطاب‌باجمم است» وبسربی اگنتومیند‪.‬‬           ‫وفوقانی بالفکشیده» بزبان زندوپازند(‪ )۱‬بمعنی‬
 ‫ر کیدن ؟ ‪ ۰‬بروزن مکیدن‪ ,‬بعنی‌خود‬                                        ‫هوش باشد ‪۰‬‬    ‫هشار وصاحب‬


          ‫بخود سخن کفتن از روی قپر و نشب ‪.‬‬             ‫ر کو م ‪ ۲‬د بفتح اول بروزن سوم »‬

                                        ‫يان هیحدهم‬
                 ‫یوت‬
                   ‫اغت‬
                     ‫نه ل‬
                        ‫کسیزد‬
                            ‫دررای بنیقطه بکااف فارسی مشتمل بر‬
 ‫جان۔ بکرثائی» کنابه‌ازشربان‬        ‫رگ‬

                          ‫وحبل‌الورید باشد ‪. ۸‬‬
 ‫رکه‬    ‫بمعنتی‬    ‫خو ابا نیدن ‪-‬‬     ‫رگ‬
                                                          ‫ب‬
                                                          ‫ساصل‬‫ونی‬
                                                                ‫وقهر سخن کفتن باشد ® ‪ -‬ویمع‬
                                                                                ‫هم‌آمده احت )‪۳ (1‬‬
 ‫بازگرفتن امت کنهابه ازکاهلی و ستی کردن‬
                                  ‫درکاری باشد ‪.‬‬

‫سبترین‪ -‬کنابه از‬
               ‫رگ دخراتن‬                                        
======== leaf 420
 ‫=‬                                                                                                    ‫کرول‬
‫وچادرىك‬   ‫‪-‬‬   ‫رکوه است که کهنه ولتۀمىتممل ‏‬
                                                         ‫ر گول » بنم اول و باالك مجهول‬
                                                         ‫بروزن سلوك؛ بمعنی ر کواست که کربای وجامه‬
‫ر یك ‪ = ۲‬بروزن رمید‪ .‬ماضی رگیدن‬                                           ‫ولنة کهنة ازهمرفته باشد ‪.‬‬
                                                        ‫زرگوه = بکر اول و سکون ثالی‬
                     ‫زد ‪.‬‬    ‫خود سخن گفت وحرف‬           ‫و پور های هوز (‪ ۰ )۱‬بمعنی ر کوست کهلته‬
   ‫»ی‬
    ‫عنن‬
      ‫ممید‬
         ‫بن ر‬
            ‫ر گیدن ‪ - ۴‬بر وز‬                              ‫لكخت‬
                                                             ‫کپنه و کر بای آزهم رفته باشد‪ -‬وچادر ي‬
‫با خود سخن‬    ‫عبت‬    ‫از روی قهر و‬       ‫آهته‌اهته‬                                            ‫‪.‬‬   ‫را یز گوبند‬


                                       ‫کفتن باشد ‪.‬‬       ‫برورن وحمنتی‬      ‫بابای حطی؛‬   ‫‪a‬‏‬   ‫گوی‬      ‫ر‬




                                            ‫بیان نور دهم‬
                     ‫در رای بی نقطه با میم مشتمل بر بانزده لغت‬
     ‫شت‬   ‫ود ‪-‬‬‫ومیکباش‬‫و بضم اول » موی زهار آد‬            ‫رم د بفتح اول و سکون ای » بمعنی‬
 ‫درون دهاترا یز گفته‌اند‪ .‬ونام دشتی وبیابالی‌هم‬         ‫ومعنی رمه و کل‬‫رمیدن و فرت باشد ‪ - ۴‬ب‬
 ‫و در عربی باتشدید ثالی (‪ )4‬مرمت‬          ‫‪- ۷‬
======== leaf 421
 ‫رمکان‬                                                                                               ‫هت‬
                                                                                                      ‫‪-‬‬

‫روش» بممنی‌تبدیل‌است که ازبدلکردن‌باشد ‪- ۴‬‬              ‫رمارم = بفتح اول ورای قرشت بروزن‬
              ‫‪۰‬‬   ‫وبممنی رمیدن هم آمده است ©‬            ‫«مادم » بمعنی مقابل _وکونا کون ‪٩‬‏ پریوسته‬
‫رمظان ‪ ۱‬با فای شقطه دار بروزن‬                                           ‫ومتعافب وپی دربی باشد ‪. ۴‬‬
‫شیطان * نام یکی از احاب دين مجوی بوده‬                   ‫رماس » بفتح اول بر وزن تمای »‬
    ‫وباعتقاد او لور مختار است وظلمت موجب ‪.‬‬              ‫دوای‬   ‫مصطکی را گوند ‪ ۰‬و ان صمغی است‬

‫بر وزن سك ‪ ,‬بمعئی رمه‬            ‫رمك ‪۲‬‬                  ‫وآنرا رماست هم میگوبند بافوقالی درآخر(‪.)۱‬‬
‫و ابلشی اسب غویره‬          ‫فهند‬
                              ‫سکل‬
                                ‫کتوکه‬
                                    ‫اس‬                  ‫بقتح‌اول وزای‌فارسی بر وزن‬             ‫رهز ك‬
                                           ‫باشد ‪.‬‬
                                                        ‫باشد تامعنوی‪ -‬وبممنی گناه کردن وازجابی(‪-)۲‬‬
‫رمگاه = بفتح اول و ئالی‌وکاف فارسی‬
‫بالفکشیده ‏ بلفت زند وپازند(‪)۳‬اس مادیایرا‬               ‫فروافکندن وافتادن‌هم هست ؛ وباین ععنی بجای‬
                                                                    ‫‪:‬ی‬    ‫ثالی لون حم بنظر آ مده ات‬    ‫حرف‬
```


## [2026-09-14T01:24:26.270Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in (415,416,417):\n    print('======== leaf',n)\n    print(pages[n][:1800])\nEOF"
}
```


### [2026-09-14T01:24:27.388Z] TOOL RESULT

```
======== leaf 415
                                             ‫بیان پانزدهم‬
                      ‫شش لغت‬          ‫بر‬   ‫رای بی نقطه بافا مشتمل‬                ‫در‬


  ‫ر فو شه = بانشقیطنه‌داربروزن صوچهه‬                  ‫رق ‪ = ۲‬بروزن صف » سکوب ی که بز‬
 ‫بازی ومخر کی وظرافت باشد‪ .‬وبمعنی‌بی‌بردن‬                 ‫د‬‫شیی‬ ‫اک‬‫بآمد‬
                                                                    ‫درخانها بجهت شتن سازند‪ -‬وبر‬
   ‫نناوه‬
       ‫کبا‬
         ‫هم هست ‪ -‬و عس‬           ‫‪-‬یدن‬
                                    ‫وافبتنرچ‬
                                           ‫وی‬           ‫از دبوار درون خانها بقدر چهار انگشت ببیاشتی‬
                                 ‫را نیز گفته‌اند ‪#.‬‬     ‫که از برای زمنت خانه چیز هابرآن گذارند ‪.‬‬
                                                       ‫عربی نز آن برآمد کی را رف میگ نهد‬                   ‫ور‬
                                                                                                            ‫د‬
 ‫و ثالی ‪ ۰‬بروین را‬   ‫اول‬   ‫یتح‬    ‫ر وه ‪= ۴‬‬

‫کون دکه آن شش سار کوچك باشد که در‬                      ‫=فتح اول بروزن زبان * شفیم‬
                                                                                ‫رفان ب‬
         ‫‪.‬‬   ‫نباند‬
                 ‫ویاثر‬
                     ‫خعرب‬
                        ‫کوهان ثور است وب‬                                          ‫وشفاعت کننده باشد ‪¥.‬‬

‫رفیده د بفتح اول بروزن رسده ‪ ,‬لته‬                       ‫رفو ‪ - ۴‬بفتح اول و ثالی بواو مجهول‬

‫و کهنٌچند باشد که بره‌ثال کردبالشی درهمدوز ند‬           ‫رسیده » پیوند شال وجامةٌ پاره وسوراخ دارباشد‬
  ‫وخمیران‌را بربالای آن کترانیده برتنوربندند‪.‬‬                                    ‫بنوعیکه مملوم شود (‪)۱‬‬




                                                      ‫معلوم نشود ‪.‬‬        ‫‪-‬
======== leaf 416
                                  ‫بیان شانز دهم‬
                ‫ت‬
                ‫ات و‬
                   ‫نه لغ‬   ‫دررای بی نقطه باقاف مشتمل بر چ‬
                       ‫کهارد‬
  ‫اشرات کردنوازبهلوبیهلو غلطیدن باشد‪.‬‬            ‫رق س بکسراول وسکون ثالی » پوست‬
‫پااول مفتوح وسکون‌نالی وعین‬    ‫ر قعا‬            ‫لاك بشت دربایی باشد (‪ )۱‬و بعضی گوبند پوست‬
‫بینقطه بالف کشیده ‏ بممنی سرخس و کیلدارو‬         ‫لباكشت (‪ )۲‬وبسنی دیگر گفته‌اند نام لاك پنت‬
‫اشد ‪ ۰9 ۴‬آن چوبکی أست دوایی که دکرنار‬          ‫ی(‪٩ )۳‬‏ » وباین ممتی بفتح اول حم‬
                                                                              ‫اعسرتبدر‬
       ‫دربای خزر یایند ک‪.‬وبند عربی است ‪.‬‬                                          ‫آمده است ‪.‬‬

 ‫ر قعه ‪ -‬بفتح اول و ثالث " هکریاهی‬              ‫رقاراق ‪ - ۲‬بنتم اول و ثالی و رای‬
‫راگونند که جبر شکستن کند همجو خامااقعطلی‬        ‫وبای‬   ‫بی قطه يالف نشنه وشاف زده‪ .‬صداویدست‬

‫والجبار وبنتومه ومانند آن هموما‪ -‬وبمعضی رقعا‬                                      ‫ستوران باشد ‪.‬‬
‫است که سرخس و کیلدارو باشد خصوصاً » وان‬
‫پیخی است سرخ رنگه ‪ .‬اکر آسرا بکوبنه‬
                                                ‫وسکور سن بیاقطه ‪۰.‬ملخت عوتالی جفت | فرید را‬
 ‫وبك مثقال ازآن با دو بیهةٌ لیمبرشت بخورند‬
 ‫آزاربرا که ببب‌افتادن بابرداشتن چبزی مکی‬        ‫کومند که لوعی ازسورنجان است وبعضی گوبند‬
                                                                  ‫خصةالشملب است ‪ .‬اف اعلم ‪.‬‬
 ‫بهمرسده باشد نافع است‪٩‬‏ ‪ -‬وم اول درعربی‬
                         ‫اعند‪..‬‬
                              ‫بینه ویاره زگو‬      ‫از راحت‬     ‫کنابه‬    ‫پهلو ‪-‬‬      ‫رقص‬


   ‫شت‪.‬‬ ‫‪ :‬و‪-‬بعضی ‪ ...‬لأ‬
     ‫ماك‬                   ‫(‪ )۲‬جك ‪ -۲ :‬صحرائی‌است ؛چش‬                 ‫چس ‪ :‬ات‬     ‫‪)۷‬‬

                       
======== leaf 417
 ‫رك‬                                                                                         ‫‪۷‬و ‪4‬‬

 ‫ومعی‬
    ‫پیام ابزد وییام نآیفوریدون مینوبسند‪ .‬ج‬         ‫رقعة بست نیلگون = کنابه از‬
 ‫اورانوح میدانند وعربان سلام عقلیى‌اولحمالمین‬      ‫زمین است > و بای سین بی‌اقطه شین نقطمدار‬
‫مینوسند » و بزعم اهل هند روز اينجم اسفتدار‬         ‫حم بنظر آهده است که رفعة پشت لیلگون‬
‫ماه‌باشد که‌درحة پنجم‌حوت‌است» ودرین روزرقمة‬                                                 ‫باشف ‪.‬‬

‫کژد‌مینوسند بسیبآدکه میگوبند درجةً پنجم‬            ‫از‬     ‫به‬
                                                           ‫نونا ‪-‬‬
                                                                ‫کلگ‬
                                                                  ‫رعة بلند نی‬
                                                                            ‫ق‬
                  ‫دازد ‪۰‬‬   ‫صورت حشرات‬    ‫حوت‬
                                                                                     ‫آسمان است ‪.‬‬

‫رقون = پروزن زیون» بمعنی حناباشد‬                        ‫)ت‬
                                                         ‫(ي‬‫رقعةٌ‬          ‫‪-‬ى‬
                                                                           ‫من‬‫برا‬
                                                                               ‫رقعة غی‬
‫آون‌بر گی‌است که‌بکوبند وبردست‌وپاییندسد(‪)۱‬؛‬                          ‫یلگرن باشد که زمین است ‪.‬‬
                    ‫رضم اول حم هده أاست ‪.‬‬                                  ‫‪۰‬‬
                                                   ‫‪-‬ونمنان کهآ شس‬
                                                                ‫رقعه کژ دم ‪ ۱‬ک‬
‫رقیبان راز ‪ -‬کنابه از مارفان‬                        ‫برستان باشند درروز اول ازینجروزآخر اسفندار‬
‫و اسحاب مشاهده و نگه
```


## [2026-09-14T01:24:39.732Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"raftan\\|raftán\\|rawāk\\|ravāk\\|rawak\" BQT_v2_pages.txt BQT_v2.txt | head -20"
}
```


### [2026-09-14T01:24:39.916Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:24:45.323Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/BQT/ 2>/dev/null; ls -la *.pdf 2>/dev/null | head; ls ocr/BQT | head -40"
}
```


### [2026-09-14T01:24:45.394Z] TOOL RESULT

```
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb 14780832 Sep  4 14:01 AFM.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  4 14:06 PHD_mackenzie.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  4 14:03 PHD.pdf
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1074.vision.txt
1092.jpg
1092.vision.txt
1187.png
1187.vision.txt
1219.png
1219.txt
1219.vision.txt
1223.png
1223.txt
1225.png
1225.txt
1225.vision.txt
1226.png
1226.txt
1237.png
1237.txt
1237.vision.txt
1261.png
1261.txt
1266.png
1266.txt
1266.vision.txt
1267.png
1267.txt
1267.vision.txt
1272.png
1272.txt
1275.png
1275.txt
1279.png
1279.txt
1280.png
1280.txt
1280.vision.txt
```


## [2026-09-14T01:24:54.082Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in range(400,432):\n    p=pages[n]\n    nums=re.findall(r'[۰-۹]{2,4}',p)\n    print(n, nums[:8])\nEOF"
}
```


### [2026-09-14T01:24:55.207Z] TOOL RESULT

```
400 ['۱۹۲', '۷۱۰']
401 ['۱۷', '۹۱۵', '۸۱۵', '۵۲', '۸۱۵', '۲۸', '۹۱', '۶۱']
402 ['۰۷', '۷۲۳۱', '۸۱', '۱۸', '۷۱۸', '۷۲۱', '۶۱۳', '۷۸۲']
403 ['۳۲', '۲۱', '۷۸', '۱۱', '۵۲', '۱۱۷۰']
404 ['۵۲', '۵۰۱', '۹۰', '۷۷', '۱۳۲', '۸۱', '۸۳۲', '۸۲۱']
405 ['۸۲۱', '۱۵۳', '۲۱۱', '۵۸۹۷']
406 ['۶۷۱', '۸۹', '۱۹۳']
407 ['۱۷']
408 ['۴۰', '۲۰', '۳۱۱', '۳۳۳', '۹۳۱', '۱۲', '۵۳۹۱', '۳۱']
409 ['۵۸', '۴۲', '۵۲', '۵۲', '۵۰۵۱', '۳۹۱', '۵۲', '۷۲']
410 ['۵۰۱', '۷۳', '۶۱', '۹۳', '۵۱', '۳۸۱', '۹۱', '۳۹۱']
411 ['۳۱', '۴۱۰', '۰۲', '۳۱', '۱۲۲', '۹۶', '۰۰۰۶', '۲۱']
412 ['۱۷', '۷۳۱', '۷۲', '۸۳۱', '۸۱', '۵۲']
413 ['۷۲', '۳۷۰']
414 ['۷۸', '۲۷', '۸۷۱']
415 ['۹۳', '۲۲', '۰۹۱', '۵۳', '۵۱', '۲۷', '۵۲', '۸۷۰']
416 ['۵۲', '۹۷۱۰', '۹۹', '۹۷۱', '۹۷', '۰۸۱']
417 ['۹۵۲', '۹۲۲', '۶۹۲', '۶۱۲']
418 ['۹۰', '۲۲', '۳۷', '۲۱', '۹۳۳', '۳۱۱', '۱۸۹']
419 ['۹۰۱', '۵۲۷', '۲۵۲۷', '۰۱', '۹۱۲', '۸۹۲', '۲۲۱', '۲۷']
420 ['۳۷', '۳۵۲', '۳۵۲', '۹۰', '۰۲']
421 ['۳۵۲', '۵۰', '۱۷', '۵۱۲', '۰۱', '۵۲', '۳۵۲']
422 ['۹۱۲۰', '۷۰', '۰۲']
423 ['۱۰', '۴۱', '۵۲', '۹۵۲', '۱۹۱', '۷۲', '۳۴', '۸۳']
424 ['۶۱', '۱۱', '۲۲', '۲۲', '۱۹۱', '۳۲', '۵۲', '۵۲۱']
425 ['۲۱', '۳۱', '۵۱', '۷۱', '۴۰', '۱۲', '۰۲', '۲۲']
426 ['۹۳۱']
427 ['۹۱۱', '۹۸۱', '۵۲', '۰۵', '۱۳۱۰', '۲۵۷', '۲۵۷۷', '۷۳']
428 ['۷۹۰', '۰۶', '۲۷', '۵۲', '۷۷', '۲۰', '۲۰', '۹۲']
429 ['۷۱۰', '۸۹۱', '۰۹', '۵۲', '۷۲', '۹۳۰', '۵۸۵۲', '۷۲']
430 ['۵۲', '۸۵۳', '۹۱', '۷۷', '۱۲', '۵۲', '۵۲', '۸۷']
431 ['۷۱', '۹۸', '۹۱', '۵۲', '۷۲', '۵۲۷', '۵۲', '۵۲']
```


## [2026-09-14T01:25:11.023Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n in (413,415):\n    for line in pages[n].split('\\n'):\n        if 'رفتن' in line: print(n,'|',line.strip())\nEOF"
}
```


### [2026-09-14T01:25:12.161Z] TOOL RESULT

```
413 | ‫کوبند راتینج باینهنی عربی است » و بعضی‬                    ‫بعروسی ومهمانی رفتن باشد ‪ -‬وفرو بردن‬
415 | ‫‪ #‬وفتار ‪ -‬بفتح اول‪ ,‬حاصل مصدر رفتن (ه‪ .‬م‪ ).‬روش» سیر » ح ركت ‪ -‬سلوك طرز‬
415 | ‫ریعة ‪( 08۲ -‬رفتن) (‪ )0‬فی‪ :‬لانینی ‪ . ۵۳6۳‬لیتوابی ‪ , 14۵۱1۳6۲‬لتویی ‪( ۷06۲‬خزبدن )‪.‬‬
```


## [2026-09-14T01:25:22.248Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[415])\nEOF"
}
```


### [2026-09-14T01:25:23.356Z] TOOL RESULT

```
                                             ‫بیان پانزدهم‬
                      ‫شش لغت‬          ‫بر‬   ‫رای بی نقطه بافا مشتمل‬                ‫در‬


  ‫ر فو شه = بانشقیطنه‌داربروزن صوچهه‬                  ‫رق ‪ = ۲‬بروزن صف » سکوب ی که بز‬
 ‫بازی ومخر کی وظرافت باشد‪ .‬وبمعنی‌بی‌بردن‬                 ‫د‬‫شیی‬ ‫اک‬‫بآمد‬
                                                                    ‫درخانها بجهت شتن سازند‪ -‬وبر‬
   ‫نناوه‬
       ‫کبا‬
         ‫هم هست ‪ -‬و عس‬           ‫‪-‬یدن‬
                                    ‫وافبتنرچ‬
                                           ‫وی‬           ‫از دبوار درون خانها بقدر چهار انگشت ببیاشتی‬
                                 ‫را نیز گفته‌اند ‪#.‬‬     ‫که از برای زمنت خانه چیز هابرآن گذارند ‪.‬‬
                                                       ‫عربی نز آن برآمد کی را رف میگ نهد‬                   ‫ور‬
                                                                                                            ‫د‬
 ‫و ثالی ‪ ۰‬بروین را‬   ‫اول‬   ‫یتح‬    ‫ر وه ‪= ۴‬‬

‫کون دکه آن شش سار کوچك باشد که در‬                      ‫=فتح اول بروزن زبان * شفیم‬
                                                                                ‫رفان ب‬
         ‫‪.‬‬   ‫نباند‬
                 ‫ویاثر‬
                     ‫خعرب‬
                        ‫کوهان ثور است وب‬                                          ‫وشفاعت کننده باشد ‪¥.‬‬

‫رفیده د بفتح اول بروزن رسده ‪ ,‬لته‬                       ‫رفو ‪ - ۴‬بفتح اول و ثالی بواو مجهول‬

‫و کهنٌچند باشد که بره‌ثال کردبالشی درهمدوز ند‬           ‫رسیده » پیوند شال وجامةٌ پاره وسوراخ دارباشد‬
  ‫وخمیران‌را بربالای آن کترانیده برتنوربندند‪.‬‬                                    ‫بنوعیکه مملوم شود (‪)۱‬‬




                                                      ‫معلوم نشود ‪.‬‬        ‫‪-‬که‬
                                                                            ‫ع‪:‬ی‬
                                                                              ‫و‪۱‬‬‫ب)نخم‬
                                                                                    ‫(‪۱‬‬
   ‫‪ - ۱‬تهرانی وکیاکی ]‪( 2۲‬طافچهُ اطاق تزدبك بقف)‪ .‬معرب آن هم رف ( بفتح اول‬
                                                            ‫‪:‬‬   ‫‪۹۳6‬‬       ‫‪۱‬ص‬     ‫وتشدىف دوم ( رك‪ :‬دری‬


              ‫اررو ‏‬
                   ‫مخبا‬
                      ‫و با‬
                         ‫ارش‬
                           ‫بفسی‬
                              ‫بت‬                          ‫کند مشحون همه طاق و رف آن‬
   ‫‪۶‬سعود سعد لاهوری ‪٤۲۲‬‏ > ‪.‬‬
                           ‫م‬
   ‫معرب آن » رفو (یفتح‌اول وسکون دوم) قس ‪ :‬بونانی ‪ 0704163۲‬خ(یاطی کرد »‬                       ‫‪۴‬‬
                                                         ‫‪ :‬رمه ‪.‬‬     ‫رك‬    ‫‪۴‬‬          ‫‪۸‬‬   ‫( انفی»‬     ‫دوخت‬

  ‫‪ #‬وفتار ‪ -‬بفتح اول‪ ,‬حاصل مصدر رفتن (ه‪ .‬م‪ ).‬روش» سیر » ح ركت ‪ -‬سلوك طرز‬

                                                                               ‫عمل شیوه ‪.‬‬           ‫حر کت_طرز‬
   ‫‪ #‬رفتی ‪ -‬بفتح‌اول و سوم » چهلوی ‪ 02627‬از ربشة ‪ « ۷2۲‬نیبر کے ‪۰ ۰۹۱‬او“ستا‬
   ‫ریعة ‪( 08۲ -‬رفتن) (‪ )0‬فی‪ :‬لانینی ‪ . ۵۳6۳‬لیتوابی ‪ , 14۵۱1۳6۲‬لتویی ‪( ۷06۲‬خزبدن )‪.‬‬
   ‫کردی ‪ ,01۲۷6۲ ۰‬بلوچی ع ‪ 82۷70۲ , 22۵۲‬و ‪ .827۳2۲‬وخی ‪ ۸۷۰ 7125]6۲‬سربکلی‬
   ‫تفییر جا ومکان دادن» رحلت‬          ‫ن‪:‬‬
                                       ‫ردکت‬
                                          ‫کا؛ح‬
                                             ‫د«اسشق ‪ ۹6‬ورك‪ :‬هوبشمان اس‬                            ‫‪0‬‬
                                                                      ‫کردن » سر کردن » کنر کردن ‪.‬‬

                                   ‫یدن ‪.‬‬
                                       ‫ونب»‬
                                          ‫»ك‪ :‬رروفت‬
                                                  ‫‪#‬فتی ‪ -‬شم اول وفتح دوم ر‬
                                                                         ‫ر‬
     ‫بقده درصفحة ‪1‬‬
```


## [2026-09-14T01:25:50.693Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '71030,71096p' POK_full.txt"
}
```


### [2026-09-14T01:25:50.746Z] TOOL RESULT

```
Machte, gods'. Old Saxon ragino giscapu^Besc\\\usse the gottlichen Machte', Old High 
German regin- in proper name; Old Church Slavic rok-b m. " certain time, purpose ', rekg, 
rest/'say', rakngti, rac/t/'want, desire, will' etc.; Tocharian A rake, B rek/, PI. rekauna 
"word'; 



with e/Gothic ga-rehsnsi. " decision, ruling, determination '; Old Church Slavic recbi. " 
a formal complaint, indictment, accusation, prosecution '; 

quite doubtful sameness with Old Icelandic rann. " robbery ' {*rahna-), r^na' rob' 
{*rahnjan). Old High German bi-rahanen' capture, entrap '; primary meaning would be ' 
robbing - assassination '? 

References: WP. II 362, Trautmann 243. 
Page(s): 863 

Root / lemma: re-1, as- extended re-d^-etc. 
Meaning: " calculate, count ', ' make ready, consider ' 
See also: see above S. 59 f. (ar-). 
Page(s): 853 

Root/ lemma: /©-^extended re-d!^- 
Meaning: " disjoint, separate ' 
See also: see above S. 332 f. (e/--). 
Page(s): 853 

Root / lemma: re-3 
Meaning: ' oar, row, paddle ' 
See also: see above S. 338 {era^. 
Page(s): 853 

Root / lemma: re-4 
Meaning: ' lie, rest, repose ' 
See also: see above S. 338 f. (e/p-) 
Page(s): 853 

Root / lemma: re-5 

Meaning: dark 

Material: Old Indie rama-^ swart, black'; n. " darkness, night'; ramTi. 'night'; Middle High 

German ram, romm. "smut, smut'; nisi. rama-/egr'6\(iY, filthy'; Old High German ramac. 

Middle High German ramec, ramig^6\r{y, filthy, sooty ', Old English romig^ sooty ', Modern 

English room "scurf on the head, dandruff'; 

Old Indie /"a//"/"" night' better to Latin /ateoetc, above S. 651 nachzutragen. 



With -£/{?-formants: Latin ravus'gray, gray-yellow '. 
Page(s): 853 



Root / lemma: re-6 
Meaning: to cry 
Meaning: ' cry, shout, holler 
See also: s. re/-3. 
Page(s): 853 



Root / lemma: rep-1 {rep-?)
```


## [2026-09-14T01:25:52.617Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AHD rep\"; grep -n -i \"^rep-\\|rep-\\. To\\|reptile\" AHD_watkins1985.txt | head -10; echo \"== KLN reptile\"; grep -n \"reptile\" KLN_1966.txt | head -10; echo \"== SKT\"; grep -n \"reptile\\|rep-tile\" SKT.txt | head -5"
}
```


### [2026-09-14T01:25:52.717Z] TOOL RESULT

```
== AHD rep
872:+ esse, to be; see es-): POSSIBLE, POTENT; (IMPOTENT), PREPOTENT. 3. Form *pot- in: a. compound *ghos-pot-, “suest-master,” host (see ghos-ti-); b. compound *dems-pot-, “house-master,” ruler (see deme-'). 4. Old Persian pati-, master: PADISHAH. [Pok. poti-s 842.] [prak-. To make, do. Greek root. Greek prassein (Attic prattein), to effect, do: PRACTICAL, (PRACTICE), PRAG- MATIC, PRAXIS. [In Pok. 1. per 811.]] prek-. To ask, entreat. 1. Basic form *prek- in Latin *prex, prayer (attested only in the plural precés), with denominative precdri, to entreat, pray: PRAY, PRAYER?, PRECARIOUS; DEPRECATE, IMPRECATE. 2. Suffixed zero-grade form *prk-sk- becoming *pork-sk-, contracted into *posk- in suffixed form *posk-to-, contracted into *posto-, which appears in Latin postuldre, to ask, re- quest: POSTULATE; EXPOSTULATE. [Pok. 4. perk- 821.] prep-. To appear. Suffixed zero-grade form *prp-yo- in Germanic *furbjan, to cause to have a (good) appearance, polish, in Old French fo(u)rbir, to polish, burnish: FuR- BISH. [Pok. prep- 845.] preu-. To hop. 1. Zero-grade form *pru- in Germanic *fru- in Old English frogga (with obscure expressive suffix -gga), frog: FROG. 2. Extended o-grade form *prowo- in Germanic *frawaz in: a. Middle Dutch uro, “leaping with joy,” happy: FROLIC; b. Old High German fré, happy, in frewida, joy (> German Freude): scHa- DENFREUDE. [Pok. preu- 845.] preus-. To freeze, burn. 1. Germanic *freusan, to freeze, in Old English fréosan, to freeze: FREEZE. 2. Suffixed zero-grade form *prus-to- in Germanic *frustaz, frost, in Old English forst, frost, frost: FROST. 3. Suffixed form *preus-i- in Latin *preusis, *preuris, act of burning, whence denominative pririre, to burn, itch, yearn for: PRURIENT, PRURIGO, PRURITUS. 4. Suffixed zero-grade form *prus-ina in Latin pruina, hoarfrost: PRUINOSE. [Pok. preus- 846.] pri-. To love. Contracted from *pria-. 1. Suffixed form *priy-o- in Germanic “frijaz, beloved, belonging to the loved ones, not in bondage, free, in: a. Old English fréo, free; FREE; b. Dutch vrij, free: FILIBUSTER. 2. Suffixed (participial) form “priy-ont-, loving, in Germanic ‘“fri- Jjand-, lover, friend, in Old English friond, fréond, friend: FRIEND. 3. Suffixed shortened form *pri-tu- in Germanic *frithuz, peace, in: a. Old High German fridu, peace: SIEGFRIED; b. Old French esfreer, to disturb: AFFRAY; c. Germanic *frij-, peace, safety, in compound *berg-frij-, “high place of safety” (see bhergh-?). 4. Suffixed femi- nine form *priy-G, beloved, in Germanic *frijj6, beloved, wife, in: a. Old Norse Frigg, goddess of the heavens, wife of Odin: Fricc; b. Germanic compound “*frije-dagaz, “day of Frigg” (translation of Latin Veneris diés, “Ve- nus’s day”), in Old English frigedeg, Friday: FRIDAY. [Pok. prdi- 844.] prokto-. Anus. Greek prokios, anus: PROCTITIS, PROCTOL- OGY, PROCTOSCOPE. [Pok. prdkto- 846.] pster-. Also ster-. To sneeze. Imitative root. 1. Suffixed form *ster-nu- in Latin sternuere, to sneeze: STERNUTATION. 2. Suffixed form *ster-t- in Latin ster- tere, to snore: STERTOR. [Pok. pster- 846.] pu-'. Also phu-. To blow, swell. Imitative root. 1. Ex- tended form *pus- in Latin pustula, a bubble, blister: PUSTULE. 2. Perhaps extended form “pit-, penis, in Latin praepiitium, foreskin (prae-, before, in front; see per’): PREPUCE. 3. Variant form *phi- in Greek phusa (> phusan, to blow), bellows, bladder: EMPHYSEMA, PHYSO- STIGMINE, PHYSOSTOMOUS. [Pok. 1. pu- 847.] pu-2, To rot, decay. 1. Suffixed form *pi-lo- in Germanic *filaz, rotten, filthy, in: a. Old English fi, unclean, rotten: FOUL; b. Old Norse fill, foul, akin to the Scandi- Navian source of FULMAR; ¢. Germanic abstract noun *filithd in Old English fylth, foulness: FILTH; d. Ger- manic denominative *filjan, to soil, dirty, in Old English fylan, to sully: FILE’; DEFILE!. 2. Extended form *pug- in Germanic *fuk- in Icelandic fiki, rotten sea grass, and
895:ryfe, abundant: RIFE. 3. Suffixed form *reip-d- in Latin ripa, bank (< “that which is cut out by a river”): RIPARIAN, RIVAGE, RIVER; ARRIVE. IV. Extended form *reib- in Germanic *rip-. 1. Germanic *ripja- in Old English ripe, ripe, ready for reaping: RIPE. 2. Germanic *ripan in Old English ripan, to reap: REAP. 3. Middle Low German repelen, to remove seeds, akin to the source of Middle English ripelen, to remove seeds: RIPPLE? [Pok. 1. rei- 857.] rei-2. Striped in various colors, flecked. Suffixed o-grade form *roi-ko- in Germanic *raihaz in Old English rd, raha, deer: ROE*. [Pok. 2. rei- 859.] rei-3, To flow, run. 1. Suffixed zero-grade form *7i-nu- in: a. Germanic *ri-nw-an, whence *rinnan, to run, in Old English rinnan, to run, and Old Norse rinna, to run: RUN, RUNNEL; b. secondary Germanic derivative *runiz in Old English ryne, a running: EMBER DAY. 2. Suffixed zero-grade form *ri-l- in Germanic *ril- in Dutch ril and Low German rille, running stream: RILL. 3. Suffixed form *rei-wo- in Latin rivus, stream: RIVAL, RIVULET; DERIVE. [Pok. 3. er- 326.] reidh-. To ride. I. Basic form *reidh-. 1. Germanic *ridan in: a. Old English ridan, to ride: RIDE; b. Middle Dutch riden, to ride (> ridder, rider, knight): RITTER. 2. Celtic *vo-réd- in Latin verédus, post horse (*vo-, under; see upo): PALFREY. II. O-grade form *roidh-. 1. Germanic *raid- in: a. Old English rdd, a riding, road: RAID, ROAD; b. possibly Middle High German reidel, rod between upright stakes (< “wooden horse”): RADDLE!. 2. Prob- ably Germanic *raid-ja- in Old English réde, geréde, ready (< “prepared for a journey’): READY. 3. Germanic *raidjan in Vulgar Latin *arrédare, to arrange: ARRAY. [Pok. reidh- 861.] reig-'. To bind. 1. Germanic *rigg- (the -gg- is anoma- lous) in Norwegian rigga, to bind, akin to the Scandina- vian source of Middle English riggen, to rig: RIG. 2. Zero-grade form *rig- in Latin corrigia (probably borrowed from Gaulish), thong, shoelace (cor-, from com-, together; see kom): SCOURGE. [Pok. reig- 861.] reig-2. To reach, stretch out. 1. O-grade form “roig- in Germanic *raikjan in Old English récan, to stretch out, reach: REACH. 2. Possibly suffixed (stative) zero-grade form “rig-é- in Latin rigére, to be stiff (? < “be stretched out”): RIGID, RIGOR. [Pok. (reig-) 862.] rendh-. To tear up. 1. Germanic *randjan in Old English rendan, to tear: REND. 2. Germanic *rind- in Old English rinde), rind (< “thing torn off”): RIND. [Pok. rendh- 865.] rep-. To snatch. Suffixed zero-grade form *rap-yo- in Latin rapere, to seize: RAPACIOUS, RAPE!, RAPID, RAPT, RAVEN?, RAVIN, RAVISH; EREPSIN, SURREPTITIOUS. [Pok. rep- 865.] rép-'. To creep, slink. Latin répere, to creep: REPENT?, REPTILE; SUBREPTION. [Pok. 1. rép- 865.] rép-2, Stake, beam. Suffixed variant form *rap-tro- in Germanic *raf-tra- in: a. Old English refter, rafter: RAFTER; b. Old Norse raptr, beam: RAFT!. [Pok. 2. rép- 866.] ret-. To run, roll. 1. Prefixed form *to-vo-ret-, “a running up to” (to-, to; vo, under, up, up from under; see upo), in Old Irish toir, pursuit: Tory. 2. Suffixed o-grade form *rot-d- in Latin rota, wheel: RODEO, ROLL, ROTA, RO- TARY, ROTATE, ROTUND, (ROTUNDA), ROULETTE, ROUND!, ROWEL; BAROUCHE, CONTROL, PRUNE?, ROTIFORM, ROTO- GRAVURE. [Pok. ret(h)- 866.] rét-. Post. O-grade form *rdt- in Germanic *réd- in Old English réd, rod, cross: ROOD. [Pok. rét+ 866.] reu-'. To bellow. 1. Extended form *reud- in Germanic *rauton in Old Norse rauta, to roar (akin to the Scandi- navian source of ROTE?): ROUT’. 2. Suffixed extended form *reum-os- in Latin riimor, rumor, “common talk”: RUMOR. 3. Extended form *reug- in Latin rigire, to roar: RIOT, RUT’. 4. Variant *rau-ko- in Latin raucus, hoarse: RAUCOUS. [Pok. 1. reu- 867.]
1032:strep-. To make a noise. Imitative root. Latin strepere, to make noise: OBSTREPEROUS. [Pok. (s)trep- 1037.]
2178:REIGN reg-! REIMBURSE bursa REINDEER dheu-1, ker-1 REINFORCE bhergh-2 REITERATE i- REJECT yé- REJOICE gau- REJUVENATE yeu- RELAPSE leb-! RELATE tele- RELAX slég- RELAY slég- RELEGATE leg-1 RELENT lento- RELIEVE leg¥h- RELINQUISH leikw- RELUCENT leuk- RELUCT leug-! RELY leig-1 REMAIN men-3 REMAND man-2 REMARK merg- REMEDY med- REMEMBER (s)mer-! REMEX ere-! REMINISCENT men-! REMIT (s)meit(a)- REMORA mere- REMORSE mer-2 REMOTE meue- REMOVE meue- REMUDA mei-1 REMUNERATE mei-! RENAISSANCE gene- REND rendh- RENDER do- _ RENDEZVOUS wOS RENEGADE ne RENEGE ne RENITENT kneigh- RENOUNCE neu-! RENOVATE newo- RENOWN no-men- RENT! do- REPAIR! pere-1 REPAND pete- REPARTEE pere-2 REPAST pa- REPEAT pet- REPEL pel-6 REPENT2 rép-1 REPERTORY pere-! REPINE kWei-1 REPLENISH pele-! REPLETE pele-1 REPLEVIN plegan REPLICATE plek- REPORT per-2 REPOSE! paus- REPOSIT apo- REPREHEND ghend- REPRESENT e@S- REPRESS per-5 REPRIMAND per-5 REPRISAL ghend- REPRISE ghend- REPROACH pert REPROVE per? REPTILE rép-1 REPUBLIC ré- REPUDIATE (s)peud- REPUGN peuk- REPUTE peu-
== KLN reptile
1839:Aetosaurus,  n.,  a  genus  of  reptiles  of  the  Triassic period  (paleontol.)  —  ModL.,  compounded  of aeto-  and  Gk.  oxupoq,  ‘lizard’.  See  sauro-. af-,  assimilated  form  of  ad-  before/, afar,  adv.  —  Formed  fr.  a-,  ‘on’,  and  far. afeard,  afeared,  adj.,  afraid  (archaic).  —  ME. afered,  fr.  OE.  aftered,  pp.  of  dfreran,  ‘to  frighten, terrify’,  formed  from  intensive  pref.  a-  and  fxran, ‘to  terrify’.  See  fear,  v.  and  n. affability,  n.  —  F.  affabilite,  fr.  L.  affdhiiitdtem, acc.  of  affabilitas,  ‘courtesy,  kindness,  affability’, fr.  affdbiiis.  See  affable  and  -ity. affable,  adj.,  easy  to  speak  to;  courteous.  —  F., fr.  L.  affabilis,  ‘kind,  friendly,  affable’,  lit.  ‘he who  can  be  (easily)  spoken  to’,  fr.  affari,  ‘to speak  to’,  fr.  ad-  and  fan,  ‘to  speak’.  See  fable and  cp.  esp.  ineffable.
2246:of  mammals,  birds  and  reptiles  ( anat .)  —  ModL., fr.  Gk.  SXXavTOEtSY)?,  ‘sausage-shaped’.  See  prec. word.
2502:the  first  element  in  abdest,  abkari,  Apsaras  and the  second  element  in  doab  and  in  Messapian. For  the  ending  of  amnic  see  suff.  -ic. amnion,  n.,  the  membrane  enclosing  the  embryos of  mammals,  birds  and  reptiles.  —  Gk.  dpvlov,
7327:Chelone,  n.,  a  genus  of  plants  of  the  figwort family  (bot.)  —  ModL.,  fr.  Gk.  /eXcovt),  ‘tor¬ toise’  (see  prec.  word);  so  called  because  the corolla  resembles  the  head  of  a  tortoise. Chelonia,  n.,  an  order  of  reptiles,  the  tortoise  or turtle  (zool.)  —  ModL.,  fr.  Gk.  ycXcovr,,  ‘tor¬ toise’.  Sec  chelone,  ‘siege  performed  with shields’,  and  -ia.
13038:-en,  suff.  forming  verbs  from  adjectives  and nouns,  as  deepen,  darken;  lengthen,  strengthen. —  ME.  -en,  -ien,  fr.  OE.  -titan. enable,  tr.  v.  — •  Formed  fr.  1st  en-  and  able. Derivatives:  enabl-er,  n.,  enabl-ing,  adj. enact,  tr.  v.,  to  make  into  an  act.  —  Formed  fr. 1st  en-  and  act.  Derivatives:  enact-ion,  n.,  enact- ive,  adj.,  enact-ment,  n.,  enact-or,  n. Enaliosauria,  n.  pi.,  a  group  of  extinct  gigantic marine  reptiles  (paleontol.)  —  ModL.,  lit. ‘marine  lizards’,  compounded  of  Gk.  btulio;, ‘of  the  sea’,  and  aaupos,  ‘lizard’.  The  first  ele¬ ment  is  formed  fr.  ev  (see  2nd  -en)  and  81;, gen.  0X61;  (fern.),  ‘sea’.  See  halieutic.  For  the second  element  see  sauro-. enam,  n.,  land  exempt  from  rent  or  with  favor¬ able  rent  (Hindu  law).  —  Hind,  in' dm,  bor¬ rowed,  through  the  medium  of  Persian,  fr. Arab,  in' dm,  ‘benefit,  favor’,  inf.  of  an'ama,  ‘he granted  a  favor,  favored’,  IV  (i.e.  causative) form  of  na'ima,  ‘was  easy  or  pleasant’,  which  is rel.  to  Heb.  na'dm,  ‘was  pleasant  or  lovely’, na'fm,  ‘pleasant,  lovely’.  Cp.  the  Hebrew  PN.s Na‘dmdk,  Na'amdn,  No'dmt,  which  all  derive from  the  stem  of  the  verb  na'em,  and  see Naaman,  Naomi.
15896:gehenna,  n.,  hell.  —  Eccles.  L.,  fr.  Gk.  fiewot, fr.  Heb.  Ge  HinnSm,  ‘the  Valley  of  Hinnom’, shortened  fr.  Ge  Ben- Hinnom,  ‘the  Valley  of  the Son  of  Hinnom’,  a  valley  SW.  and  S.  of  Jeru¬ salem,  where  children  were  sacrificed  to  Moloch, gehlenite,  n.,  a  calcium  aluminum  silicate, Ca3Al2SiiO10  (mineral.)  —  Named  by  the  Ger¬ man  chemist  Johann  Nepomuk  Fuchs  (1774- 1856)  after  his  colleague  A.  F.  Gehlen  (1775- 1815).  For  the  ending  see  subst.  suff.  -ite. geikelite,  n.,  magnesium  titanate  (mineral.)  — Named  after  Sir  Archibald  Geikie,  director  of the  Geological  Survey  of  Great  Britain  (1835- 1924).  For  the  ending  see  combining  form  -life, geikia,  n.,  a  toothless  reptile  from  the  New  Red Sandstone  of  Scotland  (paleontol.)  —  ModL., named  after  Sir  Archibald  Geikie.  See  prec. word.
17008:Hadromerina,  n.,  a  group  of  sponges  (zoo/.)  — ModL.,  compounded  of  hadro-,  Gk.  pipo?, ‘part’  (see  ist  mero-),  and  suff.  -ina. hadrosaur,  n.,  any  reptile  of  the  genus  Hadro- saurus.  —  See  next  word.
17009:Hadrosaurus,  n.,  a  genus  of  extinct  dinosaurian reptiles  ( pa/eontol .)  —  ModL.,  compounded  of hadro-  and  Gk.  araupot;,  ‘lizard’.  See  sauro-. haecceity,  n.,  thisness;  individuality  (scholastic philos.)  —  ML.  haecceitas,  fr.  L.  haecce  (res), ‘this  (thing)’,  with  better  spelling  haece,  fern, of  hlce  (hicce),  intensive  form  of  hie  (fern,  haec, neut.  hoc),  ‘this’.  See  hodiernal  and  cp.  encore, langue  d’oe.  For  the  ending  see  suff.  -ity. haem-.  —  See  hem-.
17656:heronsew,  n.,  heron.  —  ME.  heronsewe,  fr.  OF. heroncel,  heronceau,  ‘a  young  heron’,  dimin. of  heron.  See  prec.  word, herpes,  n.,  an  inflammatory  disease  of  the  skin {med.)  —  Gk.  Ipro;?,  ‘shingles’,  lit.  ‘that  which creeps’,  fr.  gpjretv,  ‘to  creep’  (whence  also  kpnt- x6v,  ‘creeping  animal,  reptile’);  cogn.  with  L. serpere,  ‘to  creep’.  See  serpent  and  cp.  reptile, herpetic,  adj.,  pertaining  to  herpes  {med)  — Formed  fr.  Gk.  epm)?,  gen.  epTvt]xoq,  ‘shingles’, with  suff.  -ic.  See  prec.  word, herpetiform,  adj.,  resembling  herpes  {med.)  — A  hybrid  coined  fr.  Gk.  2pir r\q,  gen.  gp7tr]To;, ‘shingles’,  and  L.  forma,  ‘form,  shape’.  See herpes  and  form,  n.
17657:herpetiform,  adj.,  like  a  reptile.  —  A  hybrid coined  fr.  Gk.  kpmxiv,  ‘creeping  animal,  rep¬ tile’,  and  L  .forma,  ‘form,  shape’.  See  prec.  word, herpetology,  the  study  of  reptiles.  —  Compound¬ ed  of  Gk.  4p7teTi5v,  ‘creeping  animal,  reptile  , and  -koyti,  fr.  -X6yo<;,  ‘one  who  speaks  (in  a certain  form);  one  who  deals  (with  a  certain topic)’.  See  herpes  and  -logy.
== SKT
10531:Iiiaard,  a  fboz-footed  reptile.  (F.  —  L.) M.  E.  Usanie.  «  F.  UsarJ,  itsard.  •-  L.  Zo- (W^;^  a  liaard.
16398:Salamander,  a  reptile.  (F.-L.-Gk.) F.  salamandrt.  —  L.  salamandra.  —  Gk. txtxXsx^nvhpa,  a  kind  of  lizard.  Of  Eastern origin;  cf.  Pen.  tamatuiar,  a  Balanuin- der.
```


## [2026-09-14T01:26:00.308Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"repent,\\|reptile,\\|rëpere\\|repere\" KLN_1966.txt | head -10"
}
```


### [2026-09-14T01:26:00.375Z] TOOL RESULT

```
17656:heronsew,  n.,  heron.  —  ME.  heronsewe,  fr.  OF. heroncel,  heronceau,  ‘a  young  heron’,  dimin. of  heron.  See  prec.  word, herpes,  n.,  an  inflammatory  disease  of  the  skin {med.)  —  Gk.  Ipro;?,  ‘shingles’,  lit.  ‘that  which creeps’,  fr.  gpjretv,  ‘to  creep’  (whence  also  kpnt- x6v,  ‘creeping  animal,  reptile’);  cogn.  with  L. serpere,  ‘to  creep’.  See  serpent  and  cp.  reptile, herpetic,  adj.,  pertaining  to  herpes  {med)  — Formed  fr.  Gk.  epm)?,  gen.  epTvt]xoq,  ‘shingles’, with  suff.  -ic.  See  prec.  word, herpetiform,  adj.,  resembling  herpes  {med.)  — A  hybrid  coined  fr.  Gk.  2pir r\q,  gen.  gp7tr]To;, ‘shingles’,  and  L.  forma,  ‘form,  shape’.  See herpes  and  form,  n.
24906:Nahum,  1)  masc.  PN. ;  2)  in  the  Bible,  the  seventh in  the  order  of  the  Twelve  Prophets;  he  lived  in the  7th  cent.  B.C.E.  and  predicted  the  downfall of  Niniveh  (which  took  place  in  612).  —  Heb. Nahum,  lit.  ‘rich  in  comfort,  comforter’,  from the  stem  n-b-m,  ‘to  be  sorry,  repent,  con¬ sole  oneself’,  whence  nibdm,  ‘he  comforted.
25949:obstreperous,  adj.,  noisy,  clamorous,  turbulent, unruly.  — -  L.  obstreperus ,  ‘clamorous’,  fr.  ob- strepere,  ‘to  cry  out  against’,  fr.  ob-  and  strepere, ‘to  make  a  noise,  rattle,  roar’,  which  is  of imitative  origin.  Cp.  L.  stertare ,  'to  snore’,  and ON.  prapt,  ‘chattering,  garrulity’,  Icel.  prefa, ‘to  quarrel’,  OE.  pneft,  ‘quarrel’,  which  all  are imitative;  see  stertorous  and  cp.  strepitous.  For E.  -ous,  as  equivalent  to  L.  -us,  see  -ous.
32366:Derivatives:  repellent,  n.,  repellent-ly,  adv. repent,  intr.  v.,  to  feel  penitence;  tr.  v.,  to  be  sorry for.  —  ME.  repenten,  fr.  OF.  (=  F.)  (se)  repentir, fr.  (se)  pentir,  fr.  VL.  *penitire,  corresponding  to L.  paenitere,  ‘to  cause  to  repent’.  See  penitent, repent,  adj.,  creeping,  trailing  (said  of  plants).  — L.  repens,  gen.  -entis,  pres.  part,  of  repere,  ‘to creep,  crawl’.  See  reptile  and  -ent  and  cp.  rep- tant.
32367:repentance,  n.  —  ME.  repentaunce,  fr.  MF. repentance,  fr.  OF.,  fr.  repentant,  pres.  part,  of (se)  repentir.  See  repent,  v.,  and  -ce. repentant,  adj.  —  F.,  pres.  part,  of  (se)  repentir. See  repent,  v.,  and  -ant.
32425:Derivatives:  reprov-er,  n.,  reprov-ing-ly,  adv. reps,  n.  —  A  var.  of  1st  rep. reptant,  adj.,  creeping.  —  L.  reptans,  gen.  -antis, pres.  part,  of  reptare,  freq.  of  repere,  ‘to  creep’. See  next  word  and  -ant.
32426:reptile,  n.  and  adj.  —  ME.  reptil,  from  the  Late L.  noun  reptile,  prop.  neut.  of  the  adj.  reptilis, ‘creeping’,  fr.  L.  rept-(um),  pp.  stem  of  repere, ‘to  creep’,  which  is  cogn.  with  Lith.  replidju, replioti,  ‘to  creep’,  Lett,  rapt,  of  s.m.  L.  repere is  prob.  not  related  to  serpere,  ‘to  creep’.  For the  ending  see  suff.  -ile.  Cp.  repent,  adj. Derivatives:  reptil 'an,  adj.  and  n.,  reptili-ary, adj.,  reptil-ism,  n.,  reptil-ity,  n.
32428:(zool.)  —  L.,  pi.  of  reptile,  ‘a  reptile’.  See  reptile and  2nd  -ia.
34702:prop.  pres.  part,  of  serpere,  ‘to  creep’,  hence  lit. meaning  ‘a  creeping  thing’.  L.  serpere  is  cogn. with  OI.  sarpati,  ‘creeps',  sarpah,  ‘serpent’,  Gk. IpTcetv,  ‘to  creep’,  spneTiv,  ‘serpent’.  Alb. gdrper,  ‘serpent’.  Cp.  herpes,  serpigo,  Serpula. For  the  ending  see  suff.  -ent.  L.  serpere  is  prob. not  rel.  to  repere,  ‘to  creep’  (see  reptile). Derivatives:  serpent-ile,  adj.,  serpent-ize,  tr.  and intr.  v.,  serpent-ly,  adv.
36999:Derivatives :  strenuous-ly,  adv. ,  slrenuous-ness,  n. Strephon,  n.,  a  lover,  swain.  —  Fr.  Strephon,  the shepherd  lover  in  Sir  Philip  Sydney’s  Arcadia. strepitoso,  adj.,  noisy  (musical  direction).  —  It., formed  fr.  L.  strepitus,  ‘noise’.  See  next  word, strepitous,  adj.,  noisy.  —  Formed  with  suff.  -ous (as  if  fr.  ModL.  *strepitosus),  fr.  L.  strepitus, ‘noise’,  fr.  strepere,  ‘to  make  a  noise,  rattle, roar’,  which  is  of  imitative  origin.  Cp.  L.  sterta- re,  ‘to  snore’,  and  see  stertorous.  Cp.  also  ON. prapt,  ‘chattering,  garrulity’,  Icel.  prefa,  ‘to quarrel’,  OE.  praeft,  ‘quarrel’,  which  are  also imitative;  see  obstreperous, strepto-,  before  a  vowel  strept-,  combining  form meaning  ‘twisted’,  as  in  Streptococcus.  —  Gk. axpcTtxo-,  axpsTtx-,  fr.  axpeTrxAc,  ‘easy  to bend,  pliant',  verbal  adj.  of  oxp£cpew,  ‘to  turn, twist',  axpotpf],  ‘a  turning,  twisting-,  axpiScpop, ‘twisted  band'.  See  strophe  and  cp.  words  there referred  to.
```


## [2026-09-14T01:26:07.623Z] TOOL CALL #42: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B1%D9%81%D8%AA%D9%86' --note 'page 421, root Rep, NP raftan etymology' 2>&1 | tail -20"
}
```


### [2026-09-14T01:26:08.781Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0b39be7b8983e00c.txt
```


## [2026-09-14T01:26:10.984Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -A30 \"Persian\" 0b39be7b8983e00c.txt | head -70"
}
```


### [2026-09-14T01:26:11.058Z] TOOL RESULT

```
57: Persian 
58-
59: Toggle Persian subsection 
60-
61- 1.1 
62- Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Verb 
69-
70- 1.1.2.1 
71- Conjugation 
72-
73- 1.1.2.2 
74- Derived terms 
75-
76- 1.1.2.3 
77- Related terms 
78-
79- 1.1.2.4 
80- Descendants 
81-
82- 1.1.3 
83- References 
84-
85- 1.2 
86- Etymology 2 
87-
88- 1.2.1 
89- Pronunciation 
--
185: Persian
186- [ edit ] 
187-
188- Etymology 1
189- [ edit ] 
190-
191: From Middle Persian [script needed] ( SGYTWN-tn' /⁠raftan⁠/ , “ to move, proceed ” ) , from Proto-Iranian *Hrab- / *Hraf- ( “ to go ” ) , of uncertain origin.
192-
193- Perhaps from Proto-Indo-European *h₁reh₁p- ( “ to move, crawl ” ) , in which case compare English reptile , Latin rēpō ( “ to creep ” ) , Latvian rãpât , râpt , Middle High German reben ( “ to move, steer ” ) , rebe ( “ offshoot, bud ” ) . [ 1 ] Edelman reconstructs the Proto-Indo-European root as *rebʰ- ( “ to move, hurry ” ) instead, and cites the Germanic cognates listed above, as well as Old Irish rebrad ( “ children's game ” ) . [ 2 ] 
194-
195- Alternatively, per Cheung, perhaps a blend of Proto-Iranian *Hap/f- ( “ to reach, attain ” ) and *Har- ( “ to go towards, reach ” ) , the former from Proto-Indo-European *h₁ep- ( “ to take, seize ” ) and cognate with Latin apīscor ( “ to try to seize ” ) , the latter from Proto-Indo-European *h₁er- ( “ to go to, reach ” ) and cognate with Ancient Greek ἔρχομαι ( érkhomai , “ to go, come ” ) . [ 3 ] 
196-
197- Pronunciation
198- [ edit ] 
199-
200: ( Classical Persian ) IPA ( key ) : /raf.ˈtan/ 
201-
202- ( Dari, formal ) IPA ( key ) : [räf.t̪ʰán] 
203-
204- ( Dari, formal ) IPA ( key ) : [räf.t̪ʰán] 
205- ( Kabuli ) IPA ( key ) : [räf.t̪ʰán] 
206-
207- ( Hazaragi ) IPA ( key ) : [räf.t̪ʰán] 
208-
209- ( Iran, formal ) IPA ( key ) : [ɹæf.t̪ʰǽn] 
210-
211- ( Tajik, formal ) IPA ( key ) : [ɾäf.t̪ʰán] 
212-
213- Rhymes: -an 
214-
215- Readings
216-
217- Classical reading ? 
218-
219- raftan
220-
```


## [2026-09-14T01:26:19.101Z] TOOL CALL #44: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%A7%D8%AC' --note 'page 421, Arabic/Persian rawaj' ; python3 tools/fetch_source.py 'https://www.etymonline.com/word/reptile' --note 'page 421, English reptile from Latin repere'"
}
```


### [2026-09-14T01:26:21.420Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3efa1fa468d19105.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e9290e2c7d85e970.txt
```


## [2026-09-14T01:26:24.659Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== RAWAJ ===\"; grep -n -i \"Etymology\\|Arabic\\|Persian\\|root\\|ر و ج\" 3efa1fa468d19105.txt | sed -n '1,60p'; echo; echo \"=== REPTILE ===\"; sed -n '1,80p' e9290e2c7d85e970.txt | grep -n -i \"reptile\\|repere\\|creep\" | head -20"
}
```


### [2026-09-14T01:26:24.747Z] TOOL RESULT

```
=== RAWAJ ===
57: Arabic 
59: Toggle Arabic subsection 
62: Etymology 
77: Persian 
79: Toggle Persian subsection 
82: Etymology 
166: Arabic
169: Root 
171: ر و ج ( r w j ) 
175: Etymology
178: Borrowed from Middle Persian lwʾk' ( /⁠ravāg⁠/ , “ going ” ) .
476: Persian
481: Etymology
484: Etymology tree
486: Middle Persian lwʾk' ( /⁠ravāg⁠/ ) bor. 
487: Arabic رَوَاج ( rawāj ) bor. 
488: Persian رواج 
490: Reborrowed from Arabic رَوَاج ( rawāj ) , from Middle Persian [script needed] ( lwʾk' /⁠ravāg⁠/ , “ going ” ) . Doublet of روا ( rawâ ) . 
495: ( Classical Persian ) IPA ( key ) : /ra.ˈwaːd͡ʒ/ 
570: Dehkhoda, Ali-Akbar ( 1931– ), “ رواج ”, in Dehkhoda Dictionary Institute , editors, Dehkhoda Dictionary (in Persian), Tehran: University of Tehran Press . 
574: Categories : Arabic terms belonging to the root ر و ج 
575: Arabic terms derived from Middle Persian 
576: Arabic terms borrowed from Middle Persian 
577: Arabic lemmas 
578: Arabic nouns 
579: Arabic masculine nouns 
580: Arabic verbal nouns 
581: Arabic nouns with basic triptote singular 
582: Arabic adjectives 
583: Arabic rare terms 
584: Arabic adjectives with basic triptote singular 
585: Arabic adjectives with triptote singular in -a 
586: Arabic adjectives with sound masculine plural 
587: Arabic adjectives with sound feminine plural 
588: Persian terms borrowed from Arabic 
589: Persian terms derived from the Arabic root ر و ج 
590: Persian terms derived from Middle Persian 
591: Persian terms derived from Arabic 
592: Persian doublets 
593: Persian terms with IPA pronunciation 
594: Rhymes:Persian/aːd͡ʒ 
595: Rhymes:Persian/aːd͡ʒ/2 syllables 
596: Persian lemmas 
597: Persian nouns 
598: Persian terms with quotations 
600: Hidden categories: Arabic entries referencing missing etymons 
602: Arabic entries with etymon 
603: Arabic entries with etymology texts 
609: Foreign words of the day in Persian 
611: Foreign words of the day in Persian/2021 
612: Persian entries with etymon 
613: Pages with etymology trees 
614: Persian entries with etymology trees 
615: Requests for native script for Middle Persian terms 
616: Requests for transliteration of Persian quotations 
617: Requests for translations of Persian quotations 

=== REPTILE ===
1:URL: https://www.etymonline.com/word/reptile
4:TITLE: Reptile - Etymology, Origin & Meaning
6:Reptile - Etymology, Origin & Meaning 
21: Origin and history of reptile 
23: reptile (n.) 
25: late 14c., "creeping or crawling animal; one that goes on its belly on the ground on small, short legs," from Old French reptile (early 14c.) and directly from Late Latin reptile , noun use of neuter of reptilis (adj.) "creping, crawling," from rept- , past-participle stem of repere "to crawl, creep." This is reconstructed to be from PIE root *rep- "to creep, crawl" (source also of Lithuanian rėplioti "to creep").
27: Used of persons of abject, groveling, or mean character from 1749. As an adjective, c. 1600, "creeping or crawling," hence, of persons, "low, mean" (1650s). Also sometimes used 18c. of creeping plants.
29: The precise scientific sense of the noun began to develop mid-18c., but the word also was used at first of animals now known as amphibians , including toads, frogs, salamanders. The separation of Reptilia (1835 as a distinct class) and Amphibia took place early 19c.; popular use lagged, and reptile still was used late 18c. with sense "An animal that creeps upon many feet" [Johnson, who calls the scorpion a reptile], sometimes excluding serpents. The Old English word for "reptile" was slincend , related to slink .
31: And the terrestrial animals may be divided into quadrupeds or beasts, reptiles, which have many feet, and serpents, which have no feet at all. [Locke, "Elements of Natural Philosophy," 1689]
39: Will tread aside, and let the reptile live.
44: Entries linking to reptile 
48: Middle English slinken , from Old English slincan "to creep, crawl" (of reptiles), from Proto-Germanic *slinkan (source also of Old High German slihhan , German schleichen "slink, crawl, sneak, move slowly," Swedish slinka "to glide," Dutch slinken "to shrink, shrivel"), related to the source of sling (v.)).
54: "a creeping in," 1590s, from Late Latin irreptionem (nominative irreptio ), noun of action from past-participle stem of Latin irrepere , from assimilated form of in- "in" (see in- (2)) + repere "to creep" (see reptile ).
67: "the obtaining or trying to obtain something by craft or deception," 1610s, from Latin obreptionem (nominative obreptio)  "a creeping or stealing on," noun of action from past-participle stem of obrepere "to creep on, creep up to," from ob "on, to" (see ob-) + repere "to cre
71: extinct gigantic long-necked marine reptile, 1825, from Modern Latin Pleisiosaurus (1821), coined by English paleontologist...It was one of the earliest "antediluvian" reptile fossils discovered in the scientific age and was so called for being more...
75: scale-like, covered with scales," 1540s, from Latin squamosus "covered with scales, scaly," from squama "scale" of a fish or reptile...
79: "reptile of the order Sauria," 1817, from Modern Latin Sauria "the order of reptiles" (Brongniart, 1799), from Greek sauros...
```


## [2026-09-14T01:26:39.313Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD\"; grep -n \"raftan\\|rawāg\\|rawag\\|raw-\" PHD.txt PHD_mackenzie.txt | head -20; echo \"== NYB\"; grep -n \"raftan\\|rawāk\\|ravāk\\|lwʾk\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-14T01:26:39.403Z] TOOL RESULT

```
== PHD
PHD.txt:164:abarmān [5/mn'] in charge. abarmānd ['pín?nd] inheritance, privilege. abarmānīģ [%n?nyk!] noble. abar-menišn Pf/myn$n'!] proud, haughty. abarón Pf*/xwn! | N wárün] contrary, wrong, sinful. ~ih: sin. abar-6z PóPeoc] stronger. ~ih: mastery. abar-tan [Pltn'] arrogant. ~th: arrogance. abarwēz Pfltvyc | (M *bruyj, N parwéz)] triumphant, victorious. ~ih: triumph, victory. abarzén, v. zmašk, abaxs [hš] repentant; regret. ~ЛЬ : repentance. abaxšāwand [5hP^wnd] regretful. abaxšāyīdan, abaxšāy- [5APd-ytn! | М ?bxPy-, N baxšūdan, baxšāy-) forgive, have mercy on. ~išn: mercy, forgiveness. ~i&nig : forgiving, merciful. labāxtar [*5?*4tl | M 7b’xtr] planet. žabāxtar [PP’htl | (N bāxtar ‘west’)] north. abaydag Pyrťk', v. paydag | M ?byd?g] invisible. ~th: invisibility. abày- : abayéd ['yt' | M Maud, N bāyad] it is necessary, fitting; must (+ infinitive). ~ist Pf?dst' | N bāyist] it was necessary. ~istan [?P?dstn!] be necessary, fitting; desire, want. ~išn: necessity. ~išnīg : necessary, fitting, seemly. abāz [L AWHL < A lI2(w)hr;?Pc | М Рс, N baz, wa] back, again, re-. ~ айдап б: attribute, ascribe to. 7 appoint t= ~ dāštan: withhold, restrain, prevent. ~ ēstādan az: abandon, desist from. — kardan: open. — kardan az: disengage from, wean. ~ mándan: remain behind. ~ pádan: remain, stay. — raftan : issue, go forth. ~ waštan O: turn into, become. ~ wirāstan: rearrange. abāzsār [LAWHLs'I] rebellious. ~ih: rebellion. āb-čihrag [$ cyhlk'] holding the seed, essence of water. abd [>24 | М "Gd J ?bd-] wonderful. ~ sahistan: seem wonderful (to) > marvel.
PHD.txt:227:azbāy- [*2b*d-] invoke. ~išn: invocation. azd [zd | = M] known. Azdahag Pcydi’k' | M ?zdh?g, (N aždahā)] a legendary ‘dragon’ king, Dahāg. azdénidan, azdén- Pzdyn-ytn'] inform. azēr [%cdl | N zér] below, under. azg [22 | N аху) branch. aziš [hcf | М *cy$, 22у] from him, it; postposition (= az) from, ~-keh [-ks] inferior, subordinate. ~-meh [-ms] superior. āz-kāmaģ [?ck’mk'] greedy. ~ih: greediness. azmüdan, azmāy- ['zmwtn!,?zm'd- | N 2~] = uzmüdan. aznawar Pzrw/l | M ?zn] noble. azraw-, v. azruftan. azray- ['zr'd-] adorn. azruftan, azraw- [)zlwp-tn! | M *zrw-] go out, be extinguished. āzurdan [Pcwltn! | N ~] = āzārdan, āzwar [?*cwl | N ~] greedy. ~ih: greed.
PHD.txt:316:drón yaštan: consecrate the sacrificial bread. drēš [410] mark, branding; punishment. ~ag [-k!] *desolation. drēšīdan, dro$- [d/w$-ytn'] brand. drēūšom [dlwšwm] mark. droz-, v. druxtan. drózan [dlwen! | M, J drwzn] lying, liar. ^h: falsehood. drubušt [di(w)pwst'] fortress. ~ih: defence, fortification. drüdan, *drün- (HCDLWN-tn! < A У hsd | M ача, (dwr-), N durüdan, diraw-] reap, mow. drust [drw(y)st' | (M dryst), N durust] right; well, healthy. —Ih: righteous; health. drustabed [drwystpt'] chief physician. društ [dlwšt' | N durust] harsh, rough, severe. ~ih: harshness, severity. ~-Awaz, ~-éwaz [-p'c, ~yw’c] harsh-spoken. druwand [dlwnd | M drwnd] evil, sinful, unrighteous. ~īh: sin, unrighteousness. druxtan, dróz- [dlwhtn', dlwc- | M drwxt, drwz-] lie, deceive. druz [dlwe | (P drwj)] demon. айа [dwt! | M dwd, N ~] smoke. düdag [dwtk! | N —a] family. dudigar [dtykl | M dwdygr, N digar] second. duj-, = duš-. ~-daft [dwsdpt'] ill-breathing, short of breath. ~-dānāg [dwšd”7?k!] ignorant. ~-dén [dwšdyn' | M dwjdyn-] of evil religion. «=dēys*rīh [dwsdwyslyh] the evil eye. ~-gand (dtwsgnd | P dwjgnd] stinking. ~-gandih: stench. dum(b) [dwm(b') | N ~] tail. ~dmand [-'wmnd) tailed. ааг [LH YK'! < А rhyq; dul | M dur, N ~] far, distant, remote. durgar [dwlgl | N ~] carpenter. dusraw [dwslwb!] notorious, dishonoured. ^Ah : notoriety, dishonour. duš- [dws- | = M] ill-, evil-. ~īh: evil, wickedness. ~-абаһ [dw??^ Es] foolish, stupid, ignorant. ~-абаһіһ : foolishness, stupidity. ~-arz [2 ic] worthless. 7--Ca&m [-cém] envious. —-Ca$mih: envy. ~-tihr [-cyhl | M dwfcyhr] ugly, hideous.
PHD.txt:555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
PHD.txt:557:ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
PHD.txt:680:žzēn [zyn! | N zin] saddle. zēn-abzār [zyn'pe!l | N zinafzár] horse-armour. zēnāwand [zy>zond] alert, vigilant. zēndān [zynd?n! | = M, N zindān] prison. «bān [-p?*x! | N -ban] jailer. ~ig [-yk! | N -i] prisoner. zënënidan, zënën- [zynyn-ytn!] look after, preserve. zēnhār [zyn)?] | N zinhàr] protection. zénig [zynyk!] armed. *zibāl [zb | N zībāl] swift (horse, etc.). zih [zyh | N zih] bow-string. zindag [zy(w)ndk! | M zyndg, N zinda] alive, living. ~th: life. zindakkar [zywndkkl | M zyndkr] vivifier, reviver. zinénidan, zinén- [zynyn-ytn'] damage, harm. zirak [zylk' | M zyr, N ~] wise, clever. zistan, v. ziwistan. zišt [zyst! | = P, N ~] hateful, ugly. ziwénidan, ziwén- [zywyn-ytn! | M zywyn-] vivify, revive. zi(wi)stan, zi(w)- [zyz-stn! | M zywystn, zyw-, N zistan] live. zi(w)išn [zywšn! | M zyysn] life; livelihood. ~ih: life, living. --6mand [-”xmnd] living, alive. ziyānaģ [zyd?nk'] young woman. zīyišn, v. zī(w)išn. zofāy [zwp'd | M zwp’y] deep; depth. *~ih: depth. ` zofr [zwpl | M zwwpr, J zwrf, (N žarf)) deep. —šy [2d] depth. ~-payag [-p'dyk'] deep. zóhr [zwhl | M zwhr] libation, offering. zor [z())wl | M zwr, N ~] power, strength. Bay ge J ~ig, ~dmand [-yk!, -wmnd | M -mnd, N —mand] powerful, strong. d z^ 201 [zwt! = Av. zaotar-] first officiating priest. ~ih: office of 201. Zraw-, v. zruftan. !zréh [zlyh | P zryh] sea, lake. *zréh [ziyh | N zirih] armour. zruftan, zraw- [zlwp-tn'] = azruftan. zūd [zwt! | M zwd, N ~] quick(ly). ^h : speed. zür [zwl | M z*wr] false, deceitful.
PHD.txt:1467:currency rawagih.
PHD.txt:1468:current rawag.
PHD.txt:2112:go franaftan, raftan, Sudan; cause to ~ rawénidan.
PHD.txt:2113:go forth abàz raftan.
PHD.txt:2380:immobile arawāg, awazišnīg.
PHD.txt:2493:issue abāz raftan. item tag. itinerant wiyābānīg.
PHD.txt:2854:motion jumbāgīh, Jumbisn, rawišn; set in — rawagenidan.
PHD.txt:2864:move ēwarzīdan, jumbidan, raftan, wazidan, wihēz-; — quickly šēb-; cause to — jumbēnīdan, wāzīdan.
PHD.txt:3229:proceed franaftan, raftan.
PHD.txt:3249:propagate franāftan, rawāgēnīdan.
PHD.txt:3874:successful kamag-hanjam / -widār, kāmrawāg.
PHD.txt:4803:rawen-! rawenidan! rawiánt raftan! saxtag sabz
PHD.txt:4939:1% rēš rēšīdan rēšag rēšk��n rēškēnīh ristag ridan rédak raw- ruwanig ruwan rawagih rawágén- rawagénidan rawag rawišnīh rawišn rang 1-3r6y
PHD.txt:5052:kimaghanjamih "age ” 425 kāmagxwadāy ^A pr 563 kāmgār > 56 8 1-2kāmag ($e 3 kāmagwidār ` 156 3 kāmrawāg 1 ө» e 4 kāmistan uerg s kastar `, Let 4 kástan 101635 4 kāč Q» 5 kābēn wars kāpūr N vays kādag Y4ve» 5 wast 25 A wasxwüstag 1341223920 эу "kay 24 drat “ys drodádwarih! >) мео 5 у kch SIE kahist 1825-65 4
== NYB
505:lapar [’pl; MDM, v. 2apar] adj. situated above, lying above: évak ~, apäk dit, v.s.v. žapāk (2); — heavenly, often in compounds: apar-apükeh etc., v. below; comp. ~-tar [’pltl] higher 5426, 581°, highest 1097; sup. ~-tom highest 415. 102°; v. also apartaréh; — adv. empha- sizing an adj.: highly, extremely: apar- aržānīk, v. aržānīk. — Av. (393) upara-, adv. upara (instr.), uparam; MPrth ’br adj. and adv. (MHC), comp. ’brdr, sup. ’brdwm; Ps. ?pldl; Paz. awartar, awardar (SGV); NP bar ‘height, top, summit’, bartar ‘higher’. ?apar [MDM, erroneous reading of OAram QDM] 1. adv. above: (3 päs) i-m guft ~ of which I spoke above 65°; či nümak" cé hac ~ nipišt" éstat the inscription that had been written here above P2:3, cf hacapar; — prev. over, on, upon, up, or simply expressing the initiation of the action, with varying vbs., cf esp. (@)ma- tan, burtan, grätan, raftan, rasitan ; follow- ed by enclitics: apar-p-im ravišn I must needs ascend 4076, v.s.v. -p(i); — refer- ring back to an encl. pron.: api-š Vidrafš . ~ mšast and V. got on it (the horse) 25W5; cē-t avdom margéh ~ raset for at the end Death will come upon thee 726-7; (martömän) tāi-šān āmēcišn ~ nē barend as long as one does not impart instruction to them 801. — 2. prep. a) local: over, on, on to, down on: Krisäsp ~ én damik raset K. is roaming all over this earth 3318; ~ giyāk on the spot 3", 102; ~ ki Zartuxst bé dahém where we shall deposit Z. 3957; ~ pad ēstāt rose to his feet 1821; asp ... — rahy vartét harness the horse! 5418-14; srišk ~ srišk drop after drop 214
975:Religion 1097-8; hac kunišn 4 im bē out of the activity of this man 5212; — c) late, for pat, as NP bi-: bē ravākēh bavet 37? (gl.); 4717 (gl.); 502° (editorial summary). - 4. adversative conj. but: a) after a negative sentence or a negative part of the sentence: andar déh ne, be pat kustak-é € deh vitart 61%; nē ozančt, bé apäc 6 Käyös Sut 4527, ete.; ne ēvāc ... bé not only...
1520:framän [plm'n'] order, command 12). 11310 ete.; ~ būt hac... + inf. it was ordained, decreed by ... that 3611-13; ~ dätan to issue orders, to order 191 ete. passim; ~ patigraftan to comply with an order 38!; — be spoxtan to disregard, disobey an order 3? (cf 12"); v. also
3031:received it (the earthly riches) from O, in order to distribute it 7914-15, — 6. Ohur- mazd ... hakarc anākēh nē patīrēt O. is never subject to Evil 772 (cf. Arab la yaqbalu); 794-5. — From pati + Av. OP grab-, v. griftan; MPrth pdgryfin pdgyrw-; MPrs pdyryfin pdyr-, v. Verbum 205, Ghilain 89; Paz. padiraftan padir-, NP pačiruftan pačir-.
3196:raftan
3200:raftan [SGYTN-tn'; Iptn'] rav- [SGYTN-; lwb-, cf ravišn; lw-], imp. rav [SGYTN] 38° etc., ravé [SGYTN-yd] 44!; pres. 3d p. pl. SGYTN-nd = ravénd, e. g. 87°, but lwnd = ravand 20%: to go, to walk, to proceed, passim; with prep.: apak kurti- kānšu pānān raft he lived among the slave shepherds 19-10 (cf s.v. kurtīk); apak
3201:. raftan to keep company with, to communicate with 702-8; — apar én zamik ravét he moves on this earth 3333; apar zanišn raft hend they went to slay (him) 4515-16. — hac from 62. 569.809; — 6 to 3726, 385-9 etc. passim ; — pat gehän *hamāi raft hom I roamed the world all about 318-9 (kame would not suit the context; cf 952° s, v. hamäk); — with prev.: andar ~ : ka srav ... 0$ (prep.) mart (+...) andar rajt ēstāt when the report had reached that man (who ...) 4424-26; došar"% ... andar 6 [KN] ravét will move, roam freely in Hell 347-8; — apar ~ : 6 õi ket apar raft hénd they went off to the sooth- sayer 379; 3811-15, 415, ete. — be ~ : fra- tom 6 änöd apar raft, avdom be raft (he was the first to step in there) and the last to step out 496-?-20; 5714-15; pas patvand hac oisan be raft then offspring proceeded from them 941°; very often bē only indicates the aspect: ētēn sart bē raft i-š ... went ahead so vehemently that 3315; bē rav! 6019; adak ēišān bē raft hend 5712; — frac ~ : frac raft Pourusäsp
3204:raftan- raft hac ... han-tãi 6 the Haoma moved from ... to... 415; 50H v.s. v. hast;
3205:frāc ravēt (imp.) apar 6 màn + Vistasp go ye immediately forth to the house of V. 587; — peš ~ : pēš raft peš hac got ahead of 493-18, — SW only (NW rfin rf- is an- other vb.) MPrs rpin rw-: Paz. NP raftan rav-.
3206:*raftenitan [SGY TN-tynytn'] "to form flocks: hàn 1 zivandak góspand frahist 6 ham *rafténit *has brought flocks of living cattle together in the greatest number 3819-3, — If correctly handed down, it may be explained as a den. of *raft ‘drove, flock’, from raftan.
3279:raväk [lwb’k'] running, going on, current: ~ kartan to put into circulation, to dis- : seminate. 8015, 1072, — From raftan (g. v.); Paz. ravā, Skr. v. pravartamāna (Mx), pravrtta (SGV); NP ravä ‘current (coin), lawful, admissible’; Arab. lw. ravāj < raväg ‘current (money), vendible (goods); use, custom’.
3280:ravākēh progress: hamäk xučškčirčh hac im bē (for pat) ~ bavēt the whole moral law will proceed from, originate with him 379-10 (gl.).
3284:raväk-kämakeh [~ k'mkyh] prevailing dominance 105!2, — Abstr. of ravāk-kāmak ‘he whose will is (everywhere) valid’.
3285:ravčnitan [SGYTN-ynytn'] to let go, to let loose, to convey, to drive: hàn ānēd amahraspandān frac ravénit hac hàn + anagr rošneh he was brought there by the Amahraspands from the Endless Light 3921-22, 5 ūtšān urvar apar ravčnit Pouru- šāsp 6 gav P. sent out six cows (to pas- ture) on these plants 41297; api-§ hàn gäv apäc ravenit Pourusäsp and P. took them home 425; gāvān i vas pat han vitarg ravenitan to drive a great many cows through this passage 4825-26; 3000 sal nč ravenit was not allowed to budge 9518-19 — Caus. of raftan.
3846:ul [L^L?] adv. up, used as prev. l. in a purely local sense together with āmatan, estätan, handäztan, hangézénitan, hixtan, kašitan, nikeritan, östätan, patitan, raftan, šutan, vaxšitan, vàzenitan, v. these vbs.; — 2. in a more abstract sense denoting, the start of an action: ul šust he set about washing 417; ul. nipast hénd they lay down 4369-11; ul zātan to be born 44?3.? the literal translation of Av. (1658) us zāy-. — < Olr *róva- (Skr ürdhva- < *fdhua-). Av. (350) aradwa- ‘turned upwards’; MPrs 'wl (S); Paz. (awal, probably a misreading of "wi (but cf J-Prs. wr!).
4496:zančh [NYSH-yh] marriage: pat ~ x“astan to ask in marriage 1165-9 ete.; pat ~ patigraftan to wed, to take in marriage 161; pat ~ matan to get married 382, ete.
6115:rnz, rnzwr: ranj rptn, rw- raftan rsydn: rasitan rxtrnz: raxtan rw’n: ruvän rweyn-: rocēnītārēh rwd: röt
6767:pa: pat padafrah: patifras pādāišn, pādāš(a)n: pātdāšin pādan, pāy-: pātan pādēz: pātēz padīra: patīrak padīraftan: patigriftan pādišāh: pātixšāi padix"i: patēxvēh pad-kēs: pātkust
6774:raftan, rav-:
7358:ravā: ravāk
```


## [2026-09-14T01:26:49.587Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PLA\"; grep -n \"rawāğ\\|rawāǧ\\|rawāj\\|rawag\\|ravāg\" incoming/PLA/PLA_pages.txt | head -20",
 "description": "Grep Asbaghi for rawaj"
}
```


### [2026-09-14T01:26:49.655Z] TOOL RESULT

```
== PLA
7836:gi» -         rawag:       "fließend,                beweglich"           pers, << mp.        ZI» rawag     "fließend"       v.
```


## [2026-09-14T01:26:50.479Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== ARY\"; grep -n \"رفتن\\|روا \" incoming/ARY/ARY_pages.txt | head -20"
}
```


### [2026-09-14T01:26:50.545Z] TOOL RESULT

```
== ARY
52:تبایل ترکك زبان (از حدود سده‌ی پنج میلادی به بعد) موجب از میان رفتن آن زبانهای محلی گردیده
309:کوچگران وقتی به گیاه یا جانور تازه‌ای برمی‌خورند يا نام محلی را می‌پذپرفتند» یا نام جدیدی را
647:ایران راگرفتند ولی آثار و بقایای زبان هندی در بین‌النهرین بجا ماند.
771:مرکز آسیای صغیر پیش رفتند. در اثر ورود اقوام هند و اروپایی دیگر؛ کم کم گستره‌ی مردم سلت :
985:کین‌تر همین کار را می‌کردند. مثلاً در داستان جنگ تروا آمده است که آقاممنون
987:حرکت ناوگان یسونان بسوی تروا بفرستند. دو مورخ کهن» لیوی (17۷9) و پلوتارکكه
1029:می‌گرفتند. در حماسه‌ی ابلیاد (1۸0ن11) اثر هومر آمده است که پریام (/۳۸1۸3) شاه تروا دو زن
1058:پردندکه نه تنها در بسیاری از امور مورد مشورت شاه قرار می‌گرفتند بلکه گهگاه نیز در برکنار سازی
1073:با آسیاب دستی) بودند. وقتی یونانیان شهر تروا راگشودند» زنان خانواده سلطتتی (مثلاًاندروما کك
1097:تروا ادامه داد تاکشته شد. او هم مانند دیگر قهرمانان هند و اروپایی در پی نام نیک بود نه سرای
2481:و فرار گرفتن" و دبگری 818۳ (۱۰۱۹) به معنی "ایستاندن" و ار دادن", 8
2788:برخی از روستاهای مازندران و گیلان به کار می‌رود. شاید علت از مان رفتن این واژه در دیگر نواحی فلات ایران
2808:۲ واژه‌های لاتین 13۷0-0771۸88 (به چم "لاس" و آپوشاکه) و 8807۷1۸8 (به چم "پرست منار و یروا هن
3523:۱ این واژه در اکثر زبان‌های هند و اروپائی دو چم دارد: بردن؛ گرفتن.
6572:۲ چم اين واژه در زبان‌های ژرمنی کهن "گرفتن" برده ولی در زبان‌های ژرمی نوین چم آن اپا زور بلند کردن*
6574:۳ چم این واژه در زبان‌های لاتین و -لنی؛ اسیر گرفتن.
8589:ی یک ص ا روا ی
9061:۸ رفتن
9069:مرحوم معین در پانوشت برهان فاطع: (و به پیروی از آنیبرگ" و "هوبشمان") واژه‌ی رفتن را از واجریشه‌ی هند و
10483:آلمانی کهن (058(4۸۸ 0۲ انز ضا۵): 8 (لتهت) روا اد
```


## [2026-09-14T01:26:56.433Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7830,7845p' incoming/PLA/PLA_pages.txt; echo \"==== ARY\"; sed -n '9050,9090p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-14T01:26:56.522Z] TOOL RESULT

```
Fi            - rahnamaf = rahnämaf a. v.

0,2,- rahwa = rahwäß q. v.

gi» -         rawag:       "fließend,                beweglich"           pers, << mp.        ZI» rawag     "fließend"       v.
         Verb        raftan          "gehen".


sb           - rawädig:          Pl.       v.    gb» raudag           q.    v.

ob, -          rawäzin:          Pl.       v.ch,,       rauzan.


BF             - rawäsir:              Pl.      v.    risär a. v.
==== ARY
انگلیسی (تلدالاه/52): نان 778 :00/5
نروژی (/(0/087/8014: 8۷86/5 ,8186 و59 547
۳ ملندی (:070): 7 886 ند زرط بل 07ات۸
ااسلاری کهن (۲7۵ 54 نات صها: برهان قاطع : ۹۹۴
ار 1020۸ لفت‌نامه دهغدا: ۱۳۵
یادداشت:
چم این واژه در زبان‌های ژرمنی؛ نی.
چم این واژه در زبان‌های لیتوانی و لتونی؛ سبد(ساخته شده از نی)؛ یافتن,
چم این واژه در زبان‌های سانسکریت و لاتین: طناب (ساخته شده از ساقه‌ی گیاه).
چم این واژه در زبان اسلاوی کهن: ریشه.
[pdf page 307]
۸ رفتن
اوستایی (/487۸۷): 2۸ ۹ 0 ۳
پهلوی (۷1الل۳۸): ۸7 ,8۸ ایرلندی میانه (52ل1# 041002: دی
اوستی (055871]6): ۹
کردی (0782154)): لدانید؛ پسگشت‌ها دراد نیا
بلرچی (اله‌تاملهظ): ۸0:6 ۳
آلمانی میانه (052(/۸(7 ۲1۵۶ 0/1008 : برهان قاطع : ۹۵
بادداشت:
مرحوم معین در پانوشت برهان فاطع: (و به پیروی از آنیبرگ" و "هوبشمان") واژه‌ی رفتن را از واجریشه‌ی هند و
اروپایی 33۳۰ می‌داند و آن را با واژه‌ی لاتین 3380 همريشه می‌پندارد (برهان قاطم: ۹۵۵).
اوستی (0558716): ۲۸۸ روسی (۷ل#1(851): 10 ِ
تخاری 8(8 ۸ 7۸ل708): ی لترنی (تی) (۸4ا 7 با): تازناهط
سانسکربت (5۸۷5/7): ابرلندی کهن (57ل18 00): ۸07 ۱
۸ ,الما ,۸02۸3 ولزی (3کا75): ۱۱:۳۱ ۱
ایسلندی‌کهن (/۸ یک ام
3 3006 پسگشت‌ها 25
نروژی (07:7۷50[14(۷/): ۸ 2040452220 1/۸004
اسلاوی کهن (12اشا5 نابز صا0): برهان قاطع + ۹۳۰۹ ۱
10 لغت‌نامه دهخدا: ۲۱ و ۱۲۲۲۸
پادداشت: ۰
چم این واژه در سانسکریت: موی بدن انسان و حیوان,
چم این واژه در تخاری 8 و لتونی و اسلاوی کهن: کندن.
چم اين واژه در ایرلندی کهن: پال اسب.
چم این واژه در روسی و نروژی و ایسلندی کهن: موی نرم؛ پشم نرم.
۴۹۰
[pdf page 308]
۱ رنگ / ۳۰۹
پهلری (1لاتله): زا بونانی 075680): 0
کردی (۴157/): ,8۸3۸6 5
بلرچی (اللتابلم8): زان
```


## [2026-09-14T01:27:08.878Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LEW repo\"; grep -n \"repo,\\|rēpo\\|repere\" LEW_1910.txt | head -10; echo \"== LAT repo\"; grep -n \"repo\\b\\|rëpo\" LAT.txt | head -10; echo \"== IEC\"; grep -n \"rēpō\\|repo \" IEC.txt | head -10; echo \"== WLD\"; grep -n \"replioti\\|rēp-\" incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-14T01:27:08.982Z] TOOL RESULT

```
== LEW repo
14218:éase I 176 éajo II 396, 406 éeznoti I 194, 263 éelesone (r.-ksl.) LT9T. éelo I 197, 551 éeta (s.-ksl.) I 182 éestite II 494 éesto II 494 éetyre, cetvero lI 401 éeso, Cesate I 173 éime IT 406 Cisti, Gitati IT 494 Cisto II 494 éléne IT 492 érove I 318, II 760 éudo I 186 cujo, Cutt I 186 cromens II 760 crepo, crétt I 172 érostve (r.-ksl.) 1285 Cretu, Crésti (r.-ksl.) I 198 érévo I 274, 278 Grévoejo I 274 éréda I 289 éréme (ksl.) I 274 érépe Tl 172, IT 491, 676 Crése, Crésb (ksl.) 9 -Cono, -Cett II 423 Corstve (r.-ksl.) I 285 éeto II 410 éedo II 423 Selke II 521 Sesto IT 529 -Sivati II 631 sive (r.-ksl.) IZ 631 Silo II 620, 631 Sija IE 546 Sijo, siti IT 631 sup IT 486 Sure (s.-ksl.) IZ 631 Suro, Surin IT,551 Sevens, Sovo ITi 631 Soves (r.-ksl.) IT 631 Sodo 1193 ju(ze) I 668 june I 736
== LAT repo
1267:incendebant. Alii dicunt arculam esse turariam, scilicet ubi tus repo¬
1970:got. aiw (dans ni..,, aiw "ouSercore", suns-aiw "euQeoK", etc.) peut repo-
4947:pennum uocant; A rapprocher peut-fctre de arepo, CIL HI 909. - M.L.634.
12219:inclamo: crier aprbs, crier sur, crier contre (cf. increpo) ; proclino:
13966:frequenta ailleurs, y sont rares: v. crepo et surtout crocio.
14499:crepo
14526:prochement du k 1 1 ^tymologie populaire avec crepo, c£ Isid., Or. 19,34,3,
14538:crepo, -as, -ul, -Itum, -are: craquer, claquer, petiller, peter
14546:se plaindre bruyaament", cf. increpo. - Anci en, usuel. Panroaan, M.L.
14563:percrepo (percrepis dans Varr. Men.134, coaae tonimus , id., ibid.133
== IEC
== WLD
24452:     Lat. repo^ -ere „kriechen, schleichen^,                lit,    replioti     „kriechen“,       lett.   rapt
```


## [2026-09-14T01:27:10.812Z] TOOL CALL #51: Bash

```json
{
 "command": "pdftoppm -f 421 -l 421 -r 170 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg421 && echo ok"
}
```


### [2026-09-14T01:27:12.188Z] TOOL RESULT

```
ok
```


## [2026-09-14T01:27:18.280Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\ni=t.find('replioti')\nprint(t[i-1500:i+400])\nEOF"
}
```


### [2026-09-14T01:27:19.361Z] TOOL RESULT

```
espian ds., ags. refsan^ rcepsan „tadeln“, woneben "^rafjan in mhd. reffen                                   =
refsen^ vgl. mit Dehnstufe ags. ger'^f n, (ft)            =
                                               geresp „Anklage, Tadel“ (s. Fick
1^118^ 527, 111^ 337; verschiedenen Ursprungs                              ist   ags. ripsan „tadeln‘^,
s. Falk-Torp u. revse und r^ffel)

  anord. rafr „Streifen Heilbuttenfleisch“, refill ,Streifen, Stuck eines Ge-
                                                                       5


webes'* („abgerissenes“), ndl. rafel „Faser, ausgezupfter Faden^^, rafelen
,^usfasern‘^ (Fick 111^337, Falk-Torp u. revle II; ahnliche Worte mit ^-Vok.,
wie    ndl. rijvelen           „ausfasern“,   ags. ardfian         „loswickeln‘‘      s.   u.   *m-,       relp-
„ritzen“); zweifelhafter anord. rafr „Bernstein“ (Bezzenberger                                  GGA. 1898,
555, Falk-Torp u. rav I) und ags. rof „tuchtig“ (*an sich rei6end‘‘ ? Uhlen-
beck PBrB. 26, 570, Fick III ^ 338);
   alit. ap-repti {-repti; s. zur Wortform v. d. Osten-Sacken IF. 33, 251)

„fassen, ergreifen, begreifen*^, ne aprepiami „unbegreifliche'^ lit. reples (apr.
raples) „Zange“, aprepnas „vollkommen“ (Bezzenberger BB. 3, 73 Anm.),
wohl auch (ap)r6piu, ropti „mit einer Arbeit fertig werden“ (*sie in alien
Teilen umfassen, bewaltigen“; v. d. Osten-Sacken aaO.).


1.   rep- {repf) „kriechen, schleichen^.
     Lat. repo^ -ere „kriechen, schleichen^,                lit,    replioti     „kriechen“,       lett.   rapt
ds.,   lit.   replomis instr. pi. adv. „kriechend, auf alien vieren.“                           Gehort apr.
ripaiii „folget“, serrlpimai „erfahren^‘ hierher?(s. E. Lewy IF. 32, 163).

     Unsicher     der Zusammenbang mit ahd. reho, reha, repa, mhd. rehe
                  ist
„Schlingsch6fiLing‘^ (Fick III ^ 338, Falk-Torp 894 (revling) s. unter ^iier-^
```


## [2026-09-14T01:27:24.539Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('replioti')\nseg=t[:i]\nimport re\ntags=re.findall(r'\\[pdf page (\\d+)\\]',seg)\nprint('last tag',tags[-3:] if tags else None)\nEOF"
}
```


### [2026-09-14T01:27:25.705Z] TOOL RESULT

```
last tag None
```


## [2026-09-14T01:27:28.728Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor n,p in enumerate(pages):\n    if 'replioti' in p:\n        print('leaf',n,'of',len(pages))\n        print(repr(p[:200]))\nEOF"
}
```


### [2026-09-14T01:27:29.882Z] TOOL RESULT

```
leaf 374 of 725
'                    ;                           ;                                                               ;\n\n\n\n\n370                                            rep-   — rebh-\nes nicht notig      '
```


## [2026-09-14T01:27:41.603Z] TOOL CALL #55: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg421.png"
}
```


### [2026-09-14T01:27:41.632Z] TOOL RESULT

```

```


## [2026-09-14T01:27:56.926Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"رواج\" MON_part1.txt MON_part2.txt 2>/dev/null; grep -n \"رواج\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5"
}
```


### [2026-09-14T01:27:57.018Z] TOOL RESULT

```
MON_part2.txt:30
MON_part1.txt:24
MON_part2.txt:8376:فلزی که در عراق (عرب) رواج دارد. هر 
MON_part2.txt:18202:بی‌رونق؛ مق. رواء رواج. کالای (متاع) 
MON_part2.txt:20690:توسط آنان در ایران رواج یافت. 
MON_part2.txt:22085:وارد شد و رواج بافت (الماثر و الاثار 
MON_part2.txt:22944:کسشحاد: ۵قفا (ع.] (مصل.) از رواج و
```


## [2026-09-14T01:27:59.339Z] TOOL CALL #57: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg421.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/421.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/421.png"
}
```


### [2026-09-14T01:27:59.418Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 31408 Sep 13 21:27 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/421.png
```


## [2026-09-14T01:28:03.167Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"رَواج\\|رواج \\[\\|رواج(\\|روا (\\|رَوا\" MON_part1.txt MON_part2.txt | head -12; echo \"---\"; grep -n -B2 -A2 \"رواج\" MON_part2.txt | sed -n '1,40p'"
}
```


### [2026-09-14T01:28:03.265Z] TOOL RESULT

```
---
8374-اکنون هم بشر در همان دوره است. 
8375-فلس: داد [ع.] (.) بول سیاه؛ بشیز . سکه‌ای 
8376:فلزی که در عراق (عرب) رواج دارد. هر 
8377-یک از بولک‌های خرد یر | 
8378-افلس. فلوس. مقباسی است معادل 
--
18200-زبان. انحراف» منحرف شدن» کجی» کژی. 
18201-کاسد: 4 (ع.] (ص.) ناروا» نارایج» 
18202:بی‌رونق؛ مق. رواء رواج. کالای (متاع) 
18203-کاسد: متاعی که از آن استقبال نکنند؛ کالای 
18204-ناروان. 
--
20688-- معر. قتاله] (.) شمشیری است کوتاه با تيغة 
20689-بهن که هندوان آن را بکار می‌بردند و 
20690:توسط آنان در ایران رواج یافت. 
20691-
20692-
--
22083-مشکك. کرفس فرنکی: (کیا.) نوعی کرفس 
22084-که در زمان ناصرالدین شاه از اروبا به ایران 
22085:وارد شد و رواج بافت (الماثر و الاثار 
22086-۰)کرفس کوهی: (گیا.) گونه‌ای کرفس 
22087-که در دامن تبه‌ها و نواحی کوهستانی 
--
22942-کساء: هه (ع. ف. کسا] ( ۰) گلیم که 1 
22943-را پوشند؛ عباء؛ ج. اکسیه (غم.) 
22944:کسشحاد: ۵قفا (ع.] (مصل.) از رواج و 
22945-رونق افتادن ( کالا). (اسص.) بی‌رونقی» 
22946:نارواجی (کللا). (ص.) اف. - کاسد] 
22947:بی‌خر یدار؛ بی‌مشتری. بی‌رونق» بی‌رواج. 
22948-کت ات (تد. -۱252121066 (ع. کسالة] 
22949-(مصل.) بیمار بودن؛ 0 داشتن. 
--
31726-گداخته را به پوست خود حس نکرده بی 
31727-حرکت می‌ماند (د کت سیاسی. مبانی فلسفه. 
31728:۲ ص اک ۱77 بازار: رواج؛ رونق. 
31729-گرمی خونابه: (کد.) بسیاری و شتاب در 
31730-گریه. گرمی طبیعی: حرارت طبیعی؛ 
--
33253-همیشه بهار و زینتی است. ضح.- دو قسم گل
```


## [2026-09-14T01:28:44.586Z] TOOL CALL #59: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/AFM/74.vision.txt <<'EOF'\nAddi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba, Beirut 1908, printed p. ٧٤ (= 74; pdf leaf 76 of AFM.pdf).\nRead from the page image by a vision model (page 421 verification, root Rěp).\n\nHeadword relied on:\n\n* ( الرَوَاج ) ضدّ الكساد تعريب رَوَایی الذي بمعناهُ وهو مشتقّ من رفتن ومضارعهُ رَوْ واسم\nالفاعل منهُ رَوَا ومعناهُ مشى وسارَ. وقالت فيه العرب راجَ الأمرُ رَوْجاً ورَوَاجاً وراجت\nالسلعة الى غير ذلك\n\n(Neighbouring entries on the same page, for locating it: الرَنْف والرَنَف ، الرَام ،\nالرَوْنَق ، الراهب ، الرَهْنامَج ، الرَوَاج ، الرَهْوان ، الرَوَند والرِيوَند والراوند.)\n\nSense: \"al-rawāj, the opposite of stagnation (kasād), is an Arabicization of Persian\nravāyi of the same meaning; it is derived from raftan, whose present stem is raw and\nwhose agent noun is ravā, meaning 'went, travelled'. The Arabs then said rāja l-amru\nrawjan wa-rawājan, and rājat al-silʿa (the goods sold well).\"\nEOF\necho written"
}
```


### [2026-09-14T01:28:44.649Z] TOOL RESULT

```
written
```


## [2026-09-14T01:28:47.050Z] TOOL CALL #60: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T01:28:47.096Z] TOOL RESULT

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


## [2026-09-14T01:32:37.775Z] TOOL CALL #61: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-421.json",
 "content": "{\n  \"pdf_page\": 421,\n  \"book_page\": 391,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Rěp\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *rēp- 'to creep, crawl, slink' (Pokorny 1. rēp- (rep-?), IEW 865; Walde-Pokorny II 370; Watkins rēp-¹)\",\n      \"note\": \"The root box is right on all three counts. Pokorny IEW p. 865 has 'Root/lemma: rep-1 (rēp-?), Meaning: to crawl, sneak', with Lat. repō, -ere, Lith. replióti, Latv. rāpât/rāptiês, OPruss. rīpaiti; Walde-Pokorny II 370 has the same article ('1. rēp- (rep-?) „kriechen, schleichen“'), and Watkins/AHD gives 'rēp-¹. To creep, slink. Latin rēpere … REPTILE. [Pok. 1. rēp- 865.]'. Nourai's 'Rěp' is his rendering of the long vowel of rēp- (the printed page shows Rěp with a breve; it is a typographic habit of the book, not a different root). Two cautions the chart does not show: (a) the root is thinly attested — Italic plus Baltic only — and LIV does not set up a separate *rēp-, Wiktionary reconstructing it as *h₁reh₁p- 'to move, crawl'; (b) it must be kept apart from the homophonous *rep- 'to snatch' (Lat. rapiō, Pok. 865 too), which is where Watkins puts rapere. The Iranian branch drawn under it (Av. rap-, NP raftan) is the doubtful part of this chart, not the root itself. NOTE on the drawing: on the printed page the arrow into the Arabic box leaves the bottom-left corner of the PERSIAN raftan box, not the root spine (the root's two arrows run down the left margin to Avestan and to Latin); the JSON records Arabic #3 with parent #0, which is an extraction error — see node #3.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *rēp- «خزیدن، آهسته رفتن» در پوکورنی (IEW ص ۸۶۵، «rep-1 (rēp-?) kriechen, schleichen») و والده‑پوکورنی (ج ۲ ص ۳۷۰) و واتکینز (AHD: rēp-¹ «to creep, slink») آمده است و برچسب زبانی و معنای آن در نمودار نورایی درست است؛ نگارش «Rěp» تنها شیوهٔ نشان دادن مصوت بلند ē در این کتاب است. دو نکتهٔ احتیاط: نخست آنکه گواه این ریشه تنها لاتینی و زبان‌های بالتیک است و در LIV اصلاً ریشهٔ جداگانه‌ای به این نام نیامده (ویکی‌واژه آن را *h₁reh₁p- بازسازی می‌کند)؛ دوم آنکه باید آن را از ریشهٔ هم‌آوای *rep- «ربودن» (لاتینی rapere) جدا داشت. بنابراین ادعای نورایی دربارهٔ خودِ ریشه درست است و مشکل در شاخهٔ ایرانی زیر آن است. یادآوری: در صفحهٔ چاپی، پیکان جعبهٔ عربی از گوشهٔ پایینِ جعبهٔ فارسی «رفتن» بیرون می‌آید نه از خود ریشه؛ در JSON به اشتباه parent=0 ثبت شده است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B1%D9%81%D8%AA%D9%86\",\n        \"https://www.etymonline.com/word/reptile\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:865\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt (grep 'Page(s): 865'): 'Root / lemma: rep-1 (rēp-?) — Meaning: to crawl, sneak — Material: Latin repo, -ere \\\"grovel, truckle, creep, slink\\\"; … Lithuanian replioti \\\"creep\\\", Latvian rāpat, rāptiês, Old Prussian rīpaiti … References: WP. II 370, WH. II 430 … Page(s): 865'. Exactly Nourai's root, language and gloss.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. II p. 370 (WLD_Bd2_pages.txt, \\\\f-leaf 374, running head 'rep- — rebh-')\",\n          \"stance\": \"supports\",\n          \"note\": \"'1. rēp- (rep-?) „kriechen, schleichen“. Lat. repo, -ere „kriechen, schleichen“, lit. replioti „kriechen“, lett. rāpt ds., lit. replomis instr. pl. adv. „kriechend, auf allen vieren.“' — the article Pokorny 865 refers back to.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"AHD_watkins1985.txt line 895\",\n          \"stance\": \"supports\",\n          \"note\": \"'rēp-¹. To creep, slink. Latin rēpere, to creep: REPENT², REPTILE; SUBREPTION. [Pok. 1. rēp- 865.]' — and, separately, 'rep-. To snatch. … Latin rapere' (the homonym that must not be confused with it).\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"IEC.txt, grep 'rēpō' / 'repo '\",\n          \"stance\": \"silent\",\n          \"note\": \"Mann's Indo-European Comparative Dictionary gives no hit for a lemma rēpō / rēp- in the local OCR; he does not treat this thinly attested root.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"rap\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"There is no Avestan verb rap- 'to go'. Bartholomae, Altiranisches Wörterbuch col. 1508 knows only 'j., g. rap- V. \\\"Unterstützung gewähren, — finden\\\", Praes. 3 rapa-, Inf. rafəδrāi' ('to grant / find support'), with the derivatives rafnah- 'support', rafəδra- 'support' and the verdict 'Et.?' — the etymology is unknown to him and he does not connect it with Lat. rēpō. The single passage that ever suggested a meaning 'go', Vidēvdād 13.45, Bartholomae strikes out at col. 1509: 'j. rafϑ V. 13.45: lies yaϑō' (read yaϑō). Horn, Grundriss no. 619 (p. 137), Nourai's own source, only writes 'aw. √rap- \\\"gehen\\\" in raptō-(?)' with a question mark and the footnote 'Vd. 13,45. Aber ganz unsicher'; Hübschmann, Persische Studien p. 67 (ad no. 619), Nourai's other source, then rejects it: Pahlavi lwbʾk = ravāk 'points to a present stem rav-, OP rab-, not rap-'. Cheung, Etymological Dictionary of the Iranian Verb (2007) 184 f. accordingly reconstructs Proto-Iranian *Hrab/f 'to go' with Middle Persian raw-/raft, Parthian rf-, Khotanese ā-rūh-, and lists NO Avestan reflex at all. So the Avestan box is a ghost: the form rap- exists in Avestan but means 'to support', and the Iranian etymon of raftan is *Hrab- / *Hraf-, with b/f, not p. (Because *rap- and *rab- would fall together in Middle Persian raft/raw-, the error is invisible from the Persian side, which is why Horn's guess survived into Mo'in's footnote and into Nourai.)\",\n          \"derivation_fa\": \"در اوستایی فعلی به معنای «رفتن» با ستاک rap- وجود ندارد. بارتولومه در فرهنگ ایرانی باستان (ستون ۱۵۰۸) تنها «rap- : پشتیبانی کردن، پشتیبانی یافتن» (ستاک حال rapa-، مصدر rafəδrāi) را می‌آورد با مشتقات rafnah- و rafəδra- «پشتیبانی»، و دربارهٔ ریشه‌شناسی‌اش می‌نویسد «Et.?»؛ افزون بر این، همان بندِ وندیداد ۱۳٫۴۵ را که تنها گواهِ معنای «رفتن» پنداشته می‌شد، در ستون ۱۵۰۹ تصحیح می‌کند: «rafϑ در وندیداد ۱۳٫۴۵ را yaϑō بخوانید». هرن نیز در بند ۶۱۹ (ص ۱۳۷) همین صورت را با علامت پرسش و با پانوشت «کاملاً نامطمئن» آورده، و هوبشمان در پژوهش‌های فارسی ص ۶۷ آن را رد می‌کند و می‌گوید صورت پهلوی lwbʾk = ravāk بر ستاک حالِ rav- و پارسی باستان rab- دلالت دارد نه rap-. چونگ (۲۰۰۷، ص ۱۸۴) نیز ریشهٔ ایرانی را *Hrab/f «رفتن» بازسازی می‌کند و هیچ شاهد اوستایی برای آن نمی‌آورد. پس این جعبه نادرست است: ادعای نورایی (به پیروی از هرن و حاشیهٔ معین بر برهان قاطع) را پژوهش امروزی رد می‌کند. چون *p و *b میان‌واکه‌ای هر دو در فارسی میانه به یک صورت می‌رسند، این خطا از سمت فارسی دیده نمی‌شود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D9%81%D8%AA%D9%86\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HUB:67\",\n              \"status\": \"contradicts\",\n              \"note\": \"Hübschmann, Persische Studien p. 67 (HUB.txt, \\\\f-leaf 78 = printed 67), note to Horn 619: 'Zu lat. rēpo oder serpo? Im Phl. wird übrigens für np. ravā = paz. rawā etc. geschrieben ruhāk d. i. ravak, das auf einen Präsensstamm rav-, ap. rab-, nicht rap- weist.' — Hübschmann does toy with Lat. rēpō, but explicitly denies the stem rap- that Nourai puts in the Avestan box.\"\n            },\n            {\n              \"ref\": \"HRN:137\",\n              \"status\": \"partial\",\n              \"note\": \"Horn, Grundriss no. 619 (HRN.txt, \\\\f-leaf 159 = printed 137): 'reften \\\"gehen, weggehen\\\" … aw. √rap- \\\"gehen\\\" in raptō-.(?)³)' with footnote 3 'Vd. 13, 45. Aber ganz unsicher.' — the source of Nourai's Avestan box, but Horn himself marks it twice as uncertain.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Altiranisches Wörterbuch coll. 1508-1509 (BRT.txt lines 25108 ff.)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'• j., g. rap- V. \\\"Unterstützung gewähren, — finden\\\", Praes. 3 rapa-, — Inf. rafəδrāi' … 'Et.?'; and 'j. rafϑ V. 13. 45: lies yaϑō.' No Avestan rap- 'to go' exists; the one alleged attestation is emended away.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Etymological Dictionary of the Iranian Verb, s.v. *Hrab/f¹ 'to go', pp. 184-185\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'*Hrab/f ʻto goʼ — MIDDLE PERSIAN: MMP rw-, BMP rwb-, lwb- /raw-/ … NWIR: NP raftan/rav-, Bal. rapt/ra(w)-' — no Avestan entry; 'An IE origin of this Ir. root is uncertain… Perhaps, *Hrab/f is rather a blend of similar roots of motion (notably *Hap/f and *Har), whose IE credentials cannot be established either. PIE? cf. LIV: 496 | Pok.: 853' (not Pok. 865).\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, Concise Pahlavi Dictionary p. 70 s.v. raftan (PHD.txt line 555)\",\n              \"stance\": \"partial\",\n              \"note\": \"'raftan, raw- [SGYTWN-tn' < A √sgʼ; lwb- | M rptn, rw-, N ~] go, move, proceed' — the Middle Persian verb has the b/w present stem Hübschmann pointed to, which is incompatible with an Avestan *rap-.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"raftan «رفتن»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP رفتن raftan / rav- 'to go' continues Middle Persian raftan, raw- (Book Pahlavi ideogram SGYTWN-tn', phonetic lptn'; Manichaean MP rptn, rw-) — MacKenzie, CPD 70; Nyberg, Manual II 170 s.v. raftan 'to go, to walk, to proceed … MPrs rptn rw-; Paz., NP raftan rav-'. The whole family Nourai lists is built on the two stems: past raft- gives رفتار raftār 'gait, conduct' (MP raftār 'goer', PHD 70) and رفتن; the present stem raw- gives روا ravā 'current, admissible' (MP rawāg 'current', PHD 70, Nyberg s.v. ravāk), روش raviš 'way, manner' (MP rawišn 'going, motion; behaviour'), روان ravān¹ 'flowing, running' (pres. part.; Ferdowsi's line in the box puns on it against روان² 'soul' < MP ruwān), and the modern رَوَند ravand 'course, trend'. All of that is solid. What is only plausible is the arrow itself: the Iranian etymon is Proto-Iranian *Hrab-/*Hraf- (Cheung 2007:184), and its Indo-European affiliation is an open question — Wiktionary lists the derivation from PIE *h₁reh₁p- 'to move, crawl' (= Pokorny's rēp-, whence Lat. rēpō, Latv. rāpât, Engl. reptile) as the first of three options, Edelman prefers *rebʰ- 'to move, hurry', and Cheung doubts any IE origin and would rather see a blend of *Hap/f- and *Har-. Mo'in's footnote in Borhan-e Qateʿ p. 955 takes exactly Nourai's line, so the chart reproduces a respectable 19th-20th-c. Iranian-philology position, not a modern consensus.\",\n          \"derivation_fa\": \"«رفتن / رو-» از فارسی میانهٔ raftan, raw- (پهلوی کتابی با هزوارش SGYTWN-tn' و صورت آوایی lptn'، پهلوی مانوی rptn, rw-) است؛ مکنزی (فرهنگ کوچک پهلوی ص ۷۰) و نیبرگ (راهنمای پهلوی، ج ۲) هر دو همین را می‌آورند. همهٔ واژه‌های کنار جعبه بر همین دو ستاک ساخته شده‌اند: از ستاک گذشتهٔ raft-: «رفتار» (فارسی میانه raftār)؛ و از ستاک حالِ raw-: «روا» (فارسی میانه rawāg «رایج»)، «روش» (rawišn «رفتن، حرکت؛ سلوک»)، «روان ۱» (اسم فاعل، که در بیت فردوسی با «روان ۲» به معنی جان ــ از فارسی میانهٔ ruwān ــ جناس شده) و «روند». تا اینجا ادعا درست است. آنچه با احتیاط پذیرفتنی است خودِ پیکان است: نیای ایرانیِ این فعل *Hrab-/*Hraf- است (چونگ ۱۳۸۶: ۱۸۴) و پیوند آن با هندواروپایی قطعی نیست؛ ویکی‌واژه پیوند با *h₁reh₁p- (همان rēp- پوکورنی، خاستگاه لاتینی rēpō و انگلیسی reptile) را نخستین گزینه می‌شمارد، ادلمان *rebʰ- را ترجیح می‌دهد و چونگ در هرگونه خاستگاه هندواروپایی تردید می‌کند. مرحوم معین نیز در حاشیهٔ برهان قاطع (ص ۹۵۵) همین نظر نورایی را آورده است؛ پس این نمودار دیدگاهی کهن و آبرومند را بازمی‌تاباند، نه اجماع امروزی را.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D9%81%D8%AA%D9%86\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:955\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qateʿ ed. Moʿin, p. 955 = BQT_v2_pages.txt \\\\f-leaf 415 (offset confirmed twice: the leaf carries the بیان پانزدهم section 'در رای بی نقطه با فا', and Aryanpur's رفتن entry cites 'برهان قاطع: ۹۵۵' for the very same footnote). Moʿin's addenda on that page read: '# رفتار - بفتح اول، حاصل مصدر رفتن (ه.م) روش، سیر، حرکت - سلوک، طرز عمل، شیوه' and '# رفتن - بفتح اول و سوم، پهلوی raftan از ریشهٔ rap … اوستا rap- (رفتن) … قس: لاتینی repere، لیتوانی replioti، لتویی rāpot (خزیدن)، کردی …، بلوچی raptin / rawtin …، وخی …، رک: هوبشمان' (OCR garbles the Latin letters as '… چهلوی 02627 از ربشة ۷2۲ … او“ستا ریعة - 08۲ (رفتن) … فی: لانینی ۵۳6۳. لیتوابی 14۵۱1۳6۲، لتویی ۷06۲ (خزبدن)'). This is precisely Nourai's chart — Av. rap-, NP raftan, Lat. repere — so the reference supports him, though it is itself dependent on Horn/Hübschmann.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD p. 70 (PHD.txt lines 555, 557)\",\n              \"stance\": \"supports\",\n              \"note\": \"'raftan, raw- … go, move, proceed'; 'raftār [lptʼl | N ~] goer'; 'rawāg [lwʼk' | N rawā] current. ~īh: currency'; 'rawišn [lwbšn', SGYTWNšn' | N rawiš] going, motion. ~īh: behaviour' — every Persian word in the box has its Middle Persian ancestor here.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.vv. raftan, ravāk (NYB_vol2_glossary.txt lines 3200, 3279)\",\n              \"stance\": \"supports\",\n              \"note\": \"'raftan [SGYTN-tn'; lptn'] rav- [SGYTN-; lwb-] … to go, to walk, to proceed, passim … MPrs rptn rw-; Paz., NP raftan rav-.' and 'ravāk [lwbʼk'] running, going on, current … From raftan; Paz. ravā … NP ravā.'\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 619, p. 137 (HRN.txt \\\\f-leaf 159)\",\n              \"stance\": \"supports\",\n              \"note\": \"'619. reften \\\"gehen, weggehen\\\", Praes. rew-em, reftar, rewā (arab. LW. rawāj), rewān, rewāne, rewiš … phlv. raftan, rapet, rawad (3. Sing., geschr. rafd), rawāk, rawākīh' — Horn's list is verbatim Nourai's row of Persian derivatives.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e riše-hā-ye hend-o-orupāyi, printed p. 308 (ARY_pages.txt, [pdf page 307], headword رفتن)\",\n              \"stance\": \"partial\",\n              \"note\": \"'مرحوم معین در پانوشت برهان قاطع (و به پیروی از «نیبرگ» و «هوبشمان») واژه‌ی رفتن را از واج‌ریشه‌ی هند و اروپایی rap می‌داند و آن را با واژه‌ی لاتین rāpō هم‌ریشه می‌پندارد (برهان قاطع: ۹۵۵)' — Aryanpur reports the Avestan rap- / Latin comparison as Moʿin's opinion (a report, not an independent confirmation), and his citation fixes BQT p. 955 as the رفتن page.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *Hrab/f¹ 'to go', pp. 184-185\",\n              \"stance\": \"partial\",\n              \"note\": \"gives the Persian chain (MP raw-, NP raftan/rav-) but files it under PIr *Hrab/f with 'PIE?' and 'Pok.: 853', not Pok. 865, and doubts the Latin comparison ('The Latin connection is declined by Schrijver 1991: 305').\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"ravâj\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic رَوَاج rawāj 'circulation, currency, ready sale' is a borrowing of Middle Persian rawāg (Book Pahlavi lwʼk') 'going, current, in circulation' — the present-stem noun of raftan/raw- that survives as NP روا ravā 'current, admissible'. Nyberg, Manual II s.v. ravāk says so in as many words: 'ravāk [lwbʼk'] running, going on, current … From raftan … NP ravā \\\"current (coin), lawful\\\"; Arab. lw. ravāj < ravāg \\\"current (money), vendible (goods); use, custom\\\"'; Asbaghi, Persische Lehnwörter im Arabischen s.v. rawāğ: '\\\"fließend, beweglich\\\", pers. << mp. rawāg \\\"fließend\\\", v. Verb raftan \\\"gehen\\\"'; Wiktionary: 'Borrowed from Middle Persian lwʼk' (/ravāg/, \\\"going\\\")'. Iranian -g was rendered by Arabic ج (ǧ/j), the regular substitution in Sasanian-era loans; Arabic then treated the loan as a verbal noun of a hollow root ر-و-ج and back-formed the verb rāja / yarūju 'to be current, sell well' with the participle رائج rāʾij and the form-II verbal noun ترویج tarwīj 'putting into circulation'. Two things to note about the drawing: (a) on the printed page the arrow into this box comes out of the PERSIAN raftan box, not out of the root — and that is the correct route, since Arabic borrowed the Iranian word, not the IE root (the JSON's parent #0 is an extraction error); (b) Nourai's own reference, Addi Shir p. 74, derives it from the Persian noun rather than the MP participle, which comes to the same thing.\",\n          \"derivation_fa\": \"«رَواج» عربی وام‌واژه‌ای است از فارسی میانهٔ rawāg (پهلوی کتابی lwʼk') «روان، رایج، در گردش» ــ همان اسمِ ساخته‌شده از ستاک حالِ raftan/raw- که در فارسی نو «روا» شده است. نیبرگ (ج ۲، ذیل ravāk) صریح می‌گوید: «Arab. lw. ravāj < ravāg»؛ آسبقی در «وام‌واژه‌های فارسی در عربی» ذیل rawāğ می‌نویسد «pers. << mp. rawāg، از فعل raftan»؛ ویکی‌واژه نیز آن را وام‌گیری از lwʼk'/ravāg می‌داند. گ ایرانی در معرّب‌سازی به «ج» بدل شده است (ابدال معمولِ وام‌واژه‌های دورهٔ ساسانی)، و سپس عرب‌ها آن را مصدرِ ریشه‌ای اجوف «ر-و-ج» انگاشتند و از آن فعل «راجَ یَروجُ»، اسم فاعل «رائج» و مصدر باب تفعیل «ترویج» را برساختند. ادعای نورایی درست است؛ تنها باید توجه داشت که در صفحهٔ چاپی پیکان این جعبه از جعبهٔ فارسی «رفتن» می‌آید نه از خود ریشه (ثبت parent=0 در JSON خطای خوانش است) و همین هم درست است، زیرا عربی واژهٔ ایرانی را وام گرفته نه ریشهٔ هندواروپایی را.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%A7%D8%AC\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AFM:74\",\n              \"status\": \"supports\",\n              \"note\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba p. ٧٤ (= 74; verified on the page image, AFM.pdf leaf 76, running number ٧٤; transcription saved to data/verification/sources/refs/ocr/AFM/74.vision.txt): '( الرَوَاج ) ضدّ الكساد تعريب رَوَایی الذي بمعناهُ وهو مشتقّ من رفتن ومضارعهُ رَوْ واسم الفاعل منهُ رَوَا ومعناهُ مشى وسارَ. وقالت فيه العرب راجَ الأمرُ رَوْجاً ورَوَاجاً وراجت السلعة' — 'al-rawāj, the opposite of stagnation, is an arabization of Persian ravāyi of the same meaning, derived from raftan, present stem raw, agent noun ravā \\\"went, travelled\\\"; the Arabs then said rāja l-amru rawjan wa-rawājan.' Exactly Nourai's claim, including the back-formed Arabic verb.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. ravāk (NYB_vol2_glossary.txt line 3279)\",\n              \"stance\": \"supports\",\n              \"note\": \"'ravāk [lwbʼk'] running, going on, current: ~ kartan to put into circulation, to disseminate … From raftan (q.v.); Paz. ravā … NP ravā \\\"current (coin), lawful, admissible\\\"; Arab. lw. ravāj < ravāg \\\"current (money), vendible (goods); use, custom\\\".'\"\n            },\n            {\n              \"src\": \"PLA\",\n              \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen, s.v. رواج rawāğ (PLA_pages.txt line 7836)\",\n              \"stance\": \"supports\",\n              \"note\": \"'rawāg: \\\"fließend, beweglich\\\" pers. << mp. rawāg \\\"fließend\\\", v. Verb raftan \\\"gehen\\\".'\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 619, p. 137\",\n              \"stance\": \"supports\",\n              \"note\": \"lists among the derivatives of reften: 'rewā (arab. LW. rawāj)' — i.e. Arabic rawāj is a loan from Persian ravā.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD p. 70 s.v. rawāg\",\n              \"stance\": \"supports\",\n              \"note\": \"'rawāg [lwʼk' | N rawā] current. ~īh: currency' — the Middle Persian source form with exactly the sense 'current/circulation' that Arabic rawāj has.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, Comprehensive Etymological Dictionary (KLN_1966.txt, grep rawaj/rawāj)\",\n              \"stance\": \"silent\",\n              \"note\": \"Klein has no entry for this Arabic word (it never entered English), so the Semitic-side reference recommended by the matrix contributes nothing here; AFM, PLA and NYB cover the loan instead.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"ravâj «رواج ( ترویج ، رائج ، رایج )»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP رواج ravāj 'currency, vogue, circulation' is the Arabic rawāj taken back into Persian — a classic Persian → Arabic → Persian round trip, and therefore a doublet of the inherited روا ravā (< MP rawāg). Wiktionary states it exactly so: 'Reborrowed from Arabic رَوَاج (rawāj), from Middle Persian lwʼk' (/ravāg/, \\\"going\\\"). Doublet of روا (rawâ)'. The three words Nourai puts in parentheses are the Arabic derivatives that came back with it: ترویج tarwīj (form II maṣdar, 'promotion, putting into circulation'), رائج rāʾij (active participle of rāja) and its Persian-spelt variant رایج rāyij 'current, prevalent' — the hamza of رائج being regularly written as ی in Persian orthography. The Persian words are in daily use (rawāj dādan 'to promote', rāyij 'current'), so the box is correct; Nourai's reference HRN:137 supports the first half of the trip (Persian → Arabic) and Wiktionary/Dehkhoda the return.\",\n          \"derivation_fa\": \"«رواج» فارسیِ امروز، معرّبِ همان واژه است که دوباره به فارسی بازگشته؛ یعنی نمونه‌ای روشن از وام‌واژهٔ دورگرد (فارسی ← عربی ← فارسی) و از این رو دوگانهٔ «روا» (از فارسی میانه rawāg). ویکی‌واژه می‌نویسد: «از عربی رَواج، از فارسی میانهٔ ravāg؛ دوگانهٔ روا». سه واژهٔ داخل کمانک نیز مشتقات عربی‌اند که همراه آن به فارسی آمده‌اند: «ترویج» (مصدر باب تفعیل)، «رائج» (اسم فاعلِ راجَ) و صورت فارسی‌نویسِ آن «رایج» ــ چون همزهٔ «رائج» در املای فارسی به «ی» بدل می‌شود. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%A7%D8%AC\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:137\",\n              \"status\": \"supports\",\n              \"note\": \"Horn, Grundriss no. 619 (HRN.txt \\\\f-leaf 159 = printed p. 137): 'reften … Praes. rew-em, reftar, rewā (arab. LW. rawāj), rewān …' — Horn documents the Persian→Arabic step that makes the Persian رواج a re-borrowing; he does not spell out the return trip, but that is what 'arab. LW.' beside a Persian word means in his notation.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Moʿin, Farhang-e Fārsi (MON_part1/2.txt, grep رواج)\",\n              \"stance\": \"partial\",\n              \"note\": \"the local OCR of Moʿin has no full headword article رواج (the ر section is incomplete in these two files), but the word appears throughout marked as Arabic, e.g. s.v. کاسد: '[ع.] (ص.) ناروا، نارایج، بی‌رونق؛ مق. رواء رواج' — Moʿin treats رواج/رایج as the Arabic pair opposite to کاسد, i.e. as Arabic-derived Persian vocabulary.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual II s.v. ravāk\",\n              \"stance\": \"supports\",\n              \"note\": \"'Arab. lw. ravāj < ravāg' — the Arabic word whose Persian re-borrowing this node records.\"\n            },\n            {\n              \"src\": \"AFM\",\n              \"where\": \"Addi Shir p. 74\",\n              \"stance\": \"supports\",\n              \"note\": \"'وقالت فيه العرب راجَ الأمرُ رَوْجاً ورَوَاجاً' — the Arabic verb and maṣdar from which Persian رواج، ترویج، رایج were re-imported.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"repere\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin rēpō, rēpere 'to creep, crawl' is the principal Italic reflex of the root and the basis for Pokorny's article: IEW 865 lists 'Latin repo, -ere \\\"grovel, truckle, creep, slink\\\"' first, beside Lith. replióti and Latv. rāptiês; Watkins/AHD has 'rēp-¹ … Latin rēpere, to creep'. The verb is thematic with no suffix (*rēp-e/o-), its participle stem rept- giving reptāre 'to crawl about' and the adjective rēpēns 'creeping'. Klein adds the standard caveat that L. rēpere 'is prob. not related to serpere \\\"to creep\\\"', i.e. the two Latin creep-verbs are separate roots — Nourai does not confuse them. Both of Nourai's references (AHD and POK:865) are the modern standard for this link, so the node is confirmed.\",\n          \"derivation_fa\": \"لاتینی rēpō / rēpere «خزیدن» بازتاب اصلی این ریشه در شاخهٔ ایتالیک است و در واقع پایهٔ مدخل پوکورنی: در IEW ص ۸۶۵ نخستین گواه همین «Latin repo, -ere kriechen, schleichen» است، در کنار لیتوانیایی replioti و لتونیایی rāptiês؛ واتکینز نیز ذیل rēp-¹ همین را می‌آورد. فعل، ستاک حالِ بی‌پسوند (*rēp-e/o-) دارد و از ستاک اسم مفعولی rept- واژه‌های reptāre و rēpēns «خزنده» ساخته شده است. کلاین یادآور می‌شود که rēpere را نباید با serpere «خزیدن» یکی گرفت؛ نورایی نیز این دو را درنیامیخته است. هر دو مرجع خودِ نورایی (AHD و POK:865) در این مورد همان معیار امروزی‌اند، پس ادعا درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/reptile\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 895): 'rēp-¹. To creep, slink. Latin rēpere, to creep: REPENT², REPTILE; SUBREPTION. [Pok. 1. rēp- 865.]' — root, Latin verb and gloss as drawn.\"\n            },\n            {\n              \"ref\": \"POK:865\",\n              \"status\": \"supports\",\n              \"note\": \"Pokorny IEW 865 s.v. rep-1 (rēp-?): 'Material: Latin repo, -ere \\\"grovel, truckle, creep, slink\\\"' — the Latin verb is the head of the article.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny II 370\",\n              \"stance\": \"supports\",\n              \"note\": \"'1. rēp- (rep-?) „kriechen, schleichen“. Lat. repo, -ere „kriechen, schleichen“, lit. replioti „kriechen“, lett. rāpt ds.'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, CEDEL s.vv. reptile, serpent (KLN_1966.txt lines 32426, 34702)\",\n              \"stance\": \"supports\",\n              \"note\": \"'… fr. L. rept-(um), pp. stem of repere, \\\"to creep\\\", which is cogn. with Lith. replióju, replióti, \\\"to creep\\\", Lett. rāpt, of s.m. L. repere is prob. not related to serpere, \\\"to creep\\\".'\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"reptile\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English reptile is first recorded late 14c. in the sense 'creeping or crawling animal', from Old French reptile (early 14c.) and directly from Late Latin reptile, the neuter of the adjective reptilis 'creeping', built on rept-, the past-participle stem of rēpere (Etymonline; Klein, CEDEL s.v. reptile: 'ME. reptil, from the Late L. noun reptile, prop. neut. of the adj. reptilis, \\\"creeping\\\", fr. L. rept-(um), pp. stem of repere'). Late Latin reptilia was the Vulgate's word for the 'creeping things' of Genesis, which is how the word reached the vernaculars. The narrow zoological sense is 18th-c.; the class Reptilia was separated from Amphibia only in the early 19th c. (1835), so the animals Nourai's readers think of are a late specialisation of 'crawler'. The box carries no reference of its own, but AHD/Watkins explicitly lists REPTILE under rēp-¹, which is the parent box's citation.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی reptile نخستین بار در اواخر سدهٔ چهاردهم میلادی به معنای «جانور خزنده» ثبت شده، از فرانسهٔ کهن reptile و مستقیماً از لاتینی متأخر reptile، که صورت خنثای صفت reptilis «خزنده» است و بر ستاک اسم مفعولیِ rept- از فعل rēpere ساخته شده (اتیمانلاین؛ کلاین ذیل reptile). صورت جمع reptilia در ترجمهٔ لاتینی کتاب مقدس برابرِ «خزندگان» سفر پیدایش به کار رفت و از همان راه به زبان‌های اروپایی رسید. معنای جانورشناختیِ امروزی تازه است: ردهٔ Reptilia در ۱۸۳۵ از دوزیستان جدا شد. این جعبه در کتاب ارجاعی ندارد، ولی واتکینز خودِ REPTILE را ذیل rēp-¹ آورده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/reptile\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives no reference for this box; the parent box's AHD citation covers it ('rēp-¹ … Latin rēpere, to creep: REPENT², REPTILE'), so nothing is left unsupported.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, CEDEL s.v. reptile (KLN_1966.txt line 32426)\",\n              \"stance\": \"supports\",\n              \"note\": \"'reptile, n. and adj. — ME. reptil, from the Late L. noun reptile, prop. neut. of the adj. reptilis, \\\"creeping\\\", fr. L. rept-(um), pp. stem of repere, \\\"to creep\\\" …'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, s.v. rēp-¹ and index entry 'REPTILE rēp-1'\",\n              \"stance\": \"supports\",\n              \"note\": \"'rēp-¹. To creep, slink. Latin rēpere, to creep: REPENT², REPTILE; SUBREPTION.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etymological Dictionary (SKT.txt, grep 'reptile')\",\n              \"stance\": \"silent\",\n              \"note\": \"Skeat's concise edition has no headword reptile (it appears only in passing under lizard, salamander), so it adds nothing here.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-14T01:32:37.811Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-421.json (file state is current in your context — no need to Read it back)
```


## [2026-09-14T01:32:40.497Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-421.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 421"
}
```


### [2026-09-14T01:32:41.714Z] TOOL RESULT

```
JSON OK
nodes verified: 6/6
node verdicts: {'disputed': 1, 'plausible': 1, 'confirmed': 4}
root verdicts: {'confirmed': 1}
ref checks: {'contradicts': 1, 'partial': 1, 'supports': 5, 'not_checked': 1}
books consulted: {'contradicts': 2, 'partial': 4, 'supports': 13, 'silent': 2} | by book: {'PHD': 3, 'NYB': 3, 'KLN': 3, 'CHEUNG': 2, 'HRN': 2, 'BRT': 1, 'ARY': 1, 'PLA': 1, 'MON': 1, 'AFM': 1, 'WLD': 1, 'AHD': 1, 'SKT': 1}
```


## [2026-09-14T01:32:59.643Z] AGENT

Page 421 (book p. 391) verified — one entry, root **Rěp** "to crawl", 6 nodes. 0 PROBLEM lines from `verify_check.py`.

**Verdicts:** root confirmed; nodes 4 confirmed, 1 plausible, 1 disputed.

- **disputed — #1 Avestan `rap` "to go"**: no such Avestan verb. Bartholomae AirWb col. 1508 has only `rap-` "Unterstützung gewähren" (with "Et.?"), and at col. 1509 emends the sole alleged "go" attestation away: "j. rafϑ V. 13.45: lies yaϑō". Horn 137 (Nourai's own ref) writes it with "(?)" and the footnote "ganz unsicher"; Hübschmann p. 67 (his other ref) explicitly rejects the stem, since Pahlavi *lwbʾk* = ravāk points to `rav-`/OP `rab-`, not `rap-`. Cheung 2007:184 reconstructs PIr *\*Hrab/f* with no Avestan reflex.
- **plausible — #2 Persian رفتن**: word and MP chain (raftan, raw-) fully confirmed (MacKenzie, Nyberg), and all five extras (رفتار، روا، روان۱، روش، روند) check out; only the IE affiliation is open (Wiktionary lists *\*h₁reh₁p-* first, Edelman *\*rebʰ-*, Cheung doubts any IE origin).
- Nice finds: Addi Shir **AFM:74** verified on the page image (printed ٧٤) and says exactly what Nourai claims — الرواج "تعریب روایی … مشتق من رفتن"; **BQT:955** located and confirmed (vol-2 leaf 415; Mo'in's footnote gives پهلوی raftan, اوستا rap-, قس لاتینی repere، لیتوانی replioti، لتویی rāpot — Aryanpur p. 308 independently cites "برهان قاطع: ۹۵۵" for that same footnote). Nyberg (s.v. ravāk: "Arab. lw. ravāj < ravāg") and Asbaghi confirm the Persian→Arabic→Persian round trip.

**Extraction error for the owner to fix:** node **#3 (Arabic ravâj) has `parent: 0`, but the printed page draws its arrow out of the bottom-left of the Persian *raftan* box** (the root's two arrows run down the left margin to Avestan and Latin only). Parent should be **2**. This also happens to be the etymologically correct route (Arabic borrowed MP rawāg, not the PIE root).

Artifacts written: `data/verification/page-421.json`; `data/verification/sources/refs/ocr/AFM/74.vision.txt` (transcribed Addi Shir entry); `data/verification/sources/refs/ocr/BOOK/421.png` (page image relied on for the arrow check); 3 web pages archived via `fetch_source.py`.
