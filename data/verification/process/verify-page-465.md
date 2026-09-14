# Verification process log — verify-page-465


## [2026-09-14T02:27:45.116Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 465 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-465.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-465.json. Write /home/sfmqrb/git/rishe/data/verification/page-465.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 465` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:27:46.071Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:27:46.914Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:27:46.929Z] TOOL RESULT

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


## [2026-09-14T02:27:47.418Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-465.txt"
}
```


### [2026-09-14T02:27:47.443Z] TOOL RESULT

```
1	=== PDF page 465 (book page 435) ===
2	--- entry 0 ---
3	ROOT [Egyptian] Šôšen : lotus  (refs KLN:1548)
4	#1 (parent #0) [Arabic] refs=KLN:1548 | sausan : lily
5	  #2 (parent #1) [Pahlavi] refs=MON:1954 | sawsan, sŭsan : lily
6	    #3 (parent #2) [Persian] refs=MON:1954 | sŭsan «سوسن» : lily
7	#4 (parent #0) [Hebrew] refs=KLN:1548 | šôšannah : lily
8	  #5 (parent #4) [Greek] refs=KLN:1548 | sousanna
9	    #6 (parent #5) [Late Latin] refs=KLN:1548; AHD:1296 | sausanna
10	      #7 (parent #6) [English] refs=AHD:1296; KLN:1548 | Susan : a female name
11	#8 (parent #0) [Akkadian] refs=KLN:1548 | šĕšanu
12	#9 (parent #0) [Aramaic] refs=KLN:1548 | šušan
13	
```


## [2026-09-14T02:27:49.975Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-465.json",
 "description": "Read source JSON for page 465"
}
```


### [2026-09-14T02:27:50.019Z] TOOL RESULT

```
{
  "pdf_page": 465,
  "book_page": 435,
  "entries": [
    {
      "root": {
        "name": "Šôšen",
        "lang": "Egyptian",
        "refs": "KLN:1548",
        "gloss": "lotus"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:1548",
          "words": [
            {"translit": "sausan", "gloss": "lily", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "MON:1954",
          "words": [
            {"translit": "sawsan, sŭsan", "gloss": "lily", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:1954",
          "words": [
            {"translit": "sŭsan", "gloss": "lily", "script": "سوسن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "بسان سوسن اگر ده زبان شود حافظ - چو غنچه پیش تواش مُهر بر دهن باشد",
            "poet": "Hâfez"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:1548",
          "words": [
            {"translit": "šôšannah", "gloss": "lily", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Greek",
          "refs": "KLN:1548",
          "words": [
            {"translit": "sousanna", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Late Latin",
          "refs": "KLN:1548; AHD:1296",
          "words": [
            {"translit": "sausanna", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD:1296; KLN:1548",
          "words": [
            {"translit": "Susan", "gloss": "a female name", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Akkadian",
          "refs": "KLN:1548",
          "words": [
            {"translit": "šĕšanu", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Aramaic",
          "refs": "KLN:1548",
          "words": [
            {"translit": "šušan", "gloss": null, "script": null}
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


## [2026-09-14T02:27:52.531Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['KLN','AHD','MON','POK','FVQ','AFM','PLA','WLD','ARY','BQT','HRN','HUB','PHD','NYB','SKT','WEB','FSD','LKT','AFA','IEC','SYN']:\n    if k in d: print(k, json.dumps(d[k],ensure_ascii=False)[:400])\n\"",
 "description": "Check refs_online entries"
}
```


### [2026-09-14T02:27:53.946Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
```


## [2026-09-14T02:27:57.851Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['KLN','AHD','MON','FVQ','AFM','PLA','AFA','LKT','ARY']:\n    print('==',k)\n    print(json.dumps(d[k],ensure_ascii=False,indent=1))\n\" | head -150"
}
```


### [2026-09-14T02:27:59.188Z] TOOL RESULT

```
== KLN
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
== AHD
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
 "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.",
 "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
}
== MON
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
== FVQ
{
 "title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)",
 "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"
 ],
 "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)",
 "covers_etymology": true,
 "notes": "Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.",
 "cites": "page number of Jeffery, The Foreign Vocabulary of the Qurʾān (1938)"
}
== AFM
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
== PLA
{
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
== AFA
{
 "title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)",
 "edition_found": "1886",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/diearamischenfr00fraegoog",
 "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt",
 "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Arabic/Aramaic in script (not OCRed) with German glosses; grep the German meaning or transliteration.",
 "notes": "Built from djvu.xml."
}
== LKT
{
 "title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927",
 "edition_found": "1927",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/etymologische00lokoguat",
 "identifier": "etymologische00lokoguat",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt",
 "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.",
 "notes": "",
 "cites": "entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)"
}
== ARY
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
```


## [2026-09-14T02:28:02.776Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'shoshan\\|Susanna\\|^Susan' KLN_1966.txt | head -40"
}
```


### [2026-09-14T02:28:02.876Z] TOOL RESULT

```
35258:Simon  Pure,  the  right,  genuine  person.  —  Name of  a  Quaker  in  Susanna  Centlivre’s  play  A  Bold Stroke  for  a  Wife  (1717).  In  part  of  the  play Simon  Pure  is  impersonated  by  another  char¬ acter  (Colonel  Feignwell)  and  the  real  Simon Pure  is  dealt  with  as  an  impostor  and  is  believed only  after  he  has  proved  his  identity, simoniac,  n.,  one  who  practises  simony;  adj.,  per¬ taining  to  simony.  —  ML.  simoniacus,  fr.  simo- nia.  See  simony.
37621:Sus,  n.,  the  genus  of  swine  (zoo!.)  —  L.  sus, ‘swine’.  See  sow,  n.,  and  cp.  suilline. sus-,  form  of  sub-,  used  in  some  Latin  compounds in  which  the  second  element  begins  with  r,  p  or t.  —  L.,  prop,  a  contraction  of  subs-,  an  earlier form  of  sub-,  fr.  sub,  ‘under’.  See  sub-. Susannah,  Susanna,  fem.  PN.  —  L.  Susanna,  fr. Gk.  Souoiwa,  fr.  Heb.  shoshanna1',  shoshan, shushan,  ‘lily’;  cp.  Akkad,  sheshanu,  Aram. shushanta  (whence  Arm.  shushan ,  Arab,  saiisan, VArab.  susan),  ‘lily’.  All  these  words  derive  fr. Egypt.  s(sh)shn  (Coptic  shoshen),  ‘lotus'.  Cp. Gk.  oouaov,  ‘lily’,  which  is  a  Semitic  loan  word, susceptibility,  n.  —  ML.  susceptibilitas,  fr.  suscep- tibilis.  See  next  word  and  -ity.
```


## [2026-09-14T02:28:03.487Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'susan\\|shushan' KLN_1971.txt | head -40"
}
```


### [2026-09-14T02:28:03.550Z] TOOL RESULT

```
222232:of a Quaker in Susanna Centlivre’s play A Bold 
236447:Susan. 
237762:Susannah, Susanna, fem. PN. — L. Susanna , fr. 
237765:shushanta (whence Arm. shushan, Arab, sausan, 
237766:VArab. susan), ‘lily’. All these words derive fr.
```


## [2026-09-14T02:28:06.806Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=37621{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before:\",n}' KLN_1966.txt"
}
```


## [2026-09-14T02:28:07.507Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '236440,236455p;237755,237775p' KLN_1971.txt"
}
```


### [2026-09-14T02:28:07.874Z] TOOL RESULT

```
formfeeds before: 821
```


### [2026-09-14T02:28:07.940Z] TOOL RESULT

```
the soloist in tempo, etc. ( mus .) — F., ‘follow’, 
imper. pi. of suivre , ‘to follow’, which was re- 
fashioned fr. suit, metathesized form of siut , 
*sieut, fr. VL. *sequitus, pp. of sequere, ‘to 
follow’. See suit. 

sukey, n., tea kettle. — From Sukey, pet form of 
Susan. 

Sukkoth, Succoth, n., the Feast of Tabernacles 
(. Jewish Relig.) — Heb. sukkoth, pi. sukkd h , 
‘booth, tabernacle’, prop, ‘covert’, from sak- 
hakh, ‘he covered, screened’, 
sulcate, also sulcated, adj., marked with grooves, 
(bot.) — L. sulcatus , pp. of sulcare , ‘to furrow’, 
fr. sulcus, ‘furrow, trench’, which is cogn. with 

Sus, n., the genus of swine (zool) — L. sus, 
‘swine’. See sow, n., and cp. suilline. 
sus-, form of sub-, used in some Latin compounds 
in which the second element begins with s, p or 
t. — L., prop, a contraction of subs-, an earlier 
form of sub-, fr. sub, ‘under’. See sub-. 
Susannah, Susanna, fem. PN. — L. Susanna , fr. 
Gk. Sooofdtwa, fr. Heb. shdshanna H , shoshan, 
shushdn , ‘lily’; cp. Akkad, sheshanu , Aram. 
shushanta (whence Arm. shushan, Arab, sausan, 
VArab. susan), ‘lily’. All these words derive fr. 
Egypt. s(sh)shn (Coptic shoshen), ‘lotus’. Cp. 
Gk. croucrov, ‘lily’, which is a Semitic loan word, 
susceptibility, n. — ML. susceptibilitds, fr. suscep- 
tibilis. See next word and -ity. 
susceptible, adj. — ML. susceptibilis, fr. L. sus- 
ceptus, pp. of suscipere, ‘to take up, receive’, fr. 
sus- and capere (pp. cap t us), ‘to take’ (see cap- 
tive and -ible). Cp. intussusception. For the 
change of Latin d (in captus ) to & (in sus-ciptus)
```


## [2026-09-14T02:28:20.725Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i in (818,819,820,821,822):\n    p=pages[i]\n    print('--- leaf',i, repr(p[:120]))\n    print('   tail', repr(p[-120:]))\nEOF"
}
```


### [2026-09-14T02:28:21.889Z] TOOL RESULT

```
leaves 903
--- leaf 818 ',  OE.  seam,  ‘burden,  load  of  a beast  of  burden’.  Cp.  also  seam,  ‘measure’, sumpter.\nsummer  herring.  —  Tra'
   tail '  knowledge  is  superfi¬ cial,  superficial-ity,  n.,  superficial-ly,  adv.,  super- ficial-ness,  n.\nsuperficies,  n.'
--- leaf 819 ',  surface.  —  L.  superficies,  ‘top,  sur¬ face’,  fr.  super-  and  facies,  ‘face’.  See  face  and cp.  surface,  '
   tail ',  adj.,  and  cp.  plenum.  The irregular  form  of  the  OF.  verb  is  due  to  a  con¬ fusion  with  souploier,  sou'
--- leaf 820 'plier,  ‘to  beseech,  en¬ treat’  (fr.  L.  supplicdre;  see  supplicate). Derivatives:  supply,  n.,  suppliance  (q.v'
   tail 'mineering,  imperious’,  fr.  Herr, ‘master,  lord’.\nDerivatives:  surli-Iy,  adv.,  surli-ness ,  n. surmise,  tr.  and'
--- leaf 821 '  intr.  v.  —  ME.  surmisen,  fr.  MF. surmis,  surmise,  masc.  and  fem.  pp.  of  surmetre, ‘to  lay  to  one’s  ch'
   tail '  tenere,  ‘to  hold’.  See  tenable and  cp.  abstain  and  words  there  referred  to.  Cp. also  sostenuto,  souteneu'
--- leaf 822 'r, sustenance,  n.  —  ME.,  fr.  OF.  sustenance,  souste- nance  (F.  soutenance),  fr.  Late  L.  sustinentia, ‘endur'
   tail 'wart,  ON.  svartr,  Swed. svart,  Du.  zwart,  OHG.,  MHG.  swarz,  G. schwarz,  Goth,  swarts,  ‘dark-colored,  black’'
```


## [2026-09-14T02:28:35.148Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && grep -ho 'leaf [0-9]*[^\"]\\{0,80\\}' page-*.json 2>/dev/null | grep -i kln | head -20; echo ---; grep -l 'KLN:15' page-*.json | head"
}
```


## [2026-09-14T02:28:36.248Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (787,788,789,790):\n    print('--- leaf',i, repr(pages[i][:100]))\nEOF"
}
```


### [2026-09-14T02:28:36.563Z] TOOL RESULT

```
leaf 101/102 of KLN_1966.txt) 'Big Ben, name of the bell attached to the clock at Westmi
leaf containing pp.144-145 of KLN_1966.txt has \
leaf 444; KLN_1971.txt line 128053)
leaf running from 'elevation' to 'ellipse' in KLN_1966.txt, between the page markers 
leaf 570 of KLN_1966.txt = printed pp.1065-1066 (verified from the page numerals on leav
leaf 220 of KLN_1966.txt (leaf 221 carries the printed numerals 401–403, so leaf 220 = p
leaf 221 of KLN_1966.txt)
leaf 231 of KLN_1966.txt (the leaf carries the printed numerals 420, 421, so the entry b
leaf 36; KLN_1971.txt line 10681)
leaf 360 = p.665; KLN_1971.txt line 104081)
leaf 392 of KLN_1966.txt) 'Avestic zaya(n)-, zyā (gen. zimō), \
leaf 392; text quoted from KLN_1971.txt line 113469)
leaf 270 ≈ p.516; Hagar/hegira = leaves 374/385 ≈ pp.724/746) while KLN:3 is exact — the
leaf carrying printed pp. 847-848 (KLN_1966.txt line 20716, leaf 456, whose page numb
leaf 202 of KLN_1966.txt, the numeral '364' printed in the column): 'cogn. with OIr. bo,
leaf 571, which carries the running numbers 1067/1068 — so KLN:1068 is the right page): 
leaf 126 of KLN_1966 = printed pp. 218-219 (Nourai's '216' is 2-3 pages off). It reads: 
leaf 126 of KLN_1966 = printed pp. 218-219 (Nourai's page number is 2-3 low): 'fr. F. ca
leaf carrying printed pp.238-239 (KLN_1966.txt line 6504, between the page markers '2
leaf 174; p = 2·leaf − 34 ≈ 313, calibrated on 'cherub' = KLN:164 at leaf 99 and 'caftan
---
page-104.json
page-117.json
page-120.json
page-273.json
page-247.json
page-399.json
page-379.json
page-404.json
page-442.json
page-414.json
```


### [2026-09-14T02:28:38.020Z] TOOL RESULT

```
--- leaf 787 ',  n.  pi.,  a  long  gaiter.  —  Compound¬ ed  of  spatter  and  dash.  Cp.  spat,  ‘short  gaiter’'
--- leaf 788 '. name  of  the  campanula.  See  speculum  and  -ia.\nspeculate,  intr.  v.,  to  think,  conjecture'
--- leaf 789 'ModL.,  compounded of  spermato-  and  Gk.  ^o)ov,  ‘animal’.  See  zoo-, spermine,  also  spermin, '
--- leaf 790 'ument  for  meas¬ uring  blood  pressure  in  the  arteries.  —  Com¬ pounded  of  sphygmo-  and  ma'
```


## [2026-09-14T02:28:48.262Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(814,828):\n    nums=re.findall(r'\\b1[45]\\d\\d\\b', pages[i])\n    print(i, nums[:8])\nEOF"
}
```


### [2026-09-14T02:28:49.486Z] TOOL RESULT

```
814 ['1534']
815 ['1536', '1537']
816 ['1538']
817 ['1541']
818 ['1542', '1543']
819 ['1544', '1545', '1527']
820 []
821 ['1548', '1549']
822 ['1510', '1551']
823 ['1552', '1553', '1552']
824 ['1554', '1555']
825 ['1493', '1541', '1556']
826 []
827 ['1530']
```


## [2026-09-14T02:29:15.261Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in AFA.txt LKT.txt HRN.txt HUB.txt PHD.txt NYB.txt SKT.txt IEC.txt FVQ_pages.txt; do echo \"=== $f\"; grep -n -i 'sausan\\|sawsan\\|susan\\|sōsan\\|shushan\\|sōšan\\|Lilie\\|sosan' $f 2>/dev/null | head -12; done"
}
```


## [2026-09-14T02:29:15.904Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo ---; ls incoming 2>/dev/null"
}
```


### [2026-09-14T02:29:16.400Z] TOOL RESULT

```
=== AFA.txt
5203:yj^\m »Lilie*' geht wohl zunTichst auf aram. )l ^ <^ ^ , nicht
=== LKT.txt
4421:'Lilie'  [teils  bläulich  oder  dunkelviolett, teils  weiß ;  s.  FLEISCHER  u.  DOZY  in BSAW'  XX,  305;  wie  hehr,  sösan  wahr- scheinlich aus  äg.  s-ss-n  entlehnt  ZDMG XLVI,  117],  Einheitsnomeii  snsäna  ;  hier- aus mit  ar.  Art.  und  Imäla  /«  ^  e/  sp. azucena,  pg.  agiccena  'weiße  Lilie',  Ab- leitung it.  susino  'Lilienparfüm'.  [DE 228.    Eguilaz  325.    ML  8480.
=== HRN.txt
=== HUB.txt
=== PHD.txt
=== NYB.txt
=== SKT.txt
7050:F.  Jwmmkiu,  privileged   lilierly.  —
=== IEC.txt
=== FVQ_pages.txt
```


### [2026-09-14T02:29:16.456Z] TOOL RESULT

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
KNT_full.txt
KNT.txt
LAM.txt
LAT.txt
LEW_1910.txt
LKT.txt
LST.txt
MON_part1.txt
MON_part2.txt
MPP.txt
---
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


## [2026-09-14T02:29:22.816Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFA ctx\"; sed -n '5195,5215p' AFA.txt; echo; echo \"=== AFA leaf\"; awk 'NR<=5203{n+=gsub(/\\f/,\"\")} END{print n}' AFA.txt; echo \"=== LKT ctx\"; sed -n '4412,4428p' LKT.txt; echo \"=== LKT leaf\"; awk 'NR<=4421{n+=gsub(/\\f/,\"\")} END{print n}' LKT.txt"
}
```


### [2026-09-14T02:29:24.187Z] TOOL RESULT

```
=== AFA ctx
bezeichnet; es ist gewiss mit Umstellung entlehnt aus]??}!^
Kmn;r Low 283 ff.
IUS
jp^ »Rübe** geht zunächst auf KpVo U^ Low 273
zurück, das Low nach dem Vorgänge von Mahn auf ^i-
xsXof siciliach zurückfährt (Vgl Dozy a. t.) — Über
m f
OU-- = pO^D vgl. Gl. geogr. 264.
yj^\m »Lilie*' geht wohl zunTichst auf aram. )l ^ <^ ^ , nicht
auf das Persische zurück — Jüud ist entlehnt aus U^^
X*inV = aatureja Low 325. Einschub eines ^Ain ist
auch sonst zu constatieren ; z. B. überliefert Jäküt L 621, 7
als Volksaussprache fübc sT) (mit yolksetymologischer An-
lehnung) fi .V und ebenso lO^vJu für ^^L Jaküt l. 672, 2.
Die Wurzel JJuo scheint nämlich echt arabisch Ja^üt ü.
204, 5. [^nns Rga. der Gaönim Berlin 42, 6 p^lp 'yos^
iny V]. — oLoA^ > Weide" ist entlehnt aus HfivaS Low 301.
Daselbst ist für die Synonymik Sabb. 36* 8 nachzutragen.
{jiSmßji ist entlehnt aus pD*lS Low 148.
^^ »Portulak'* (woneben nach Gauh. auch ^^jJ^ vor-
kommen soll; dies ist aber wohl Fehler für ^^yx^pJ^) i>t

=== AFA leaf
173
=== LKT ctx
1955.  Ar.  snrta: 'Polizeimann';  hieraus  siz.  scmia,  (alt) zurta 'Nachtwächter, Nachtwache;  nächt- licher Gesang'.    [ZfromPh  XXXV,  440. GrSVociSic  245.    ML  7717.
1956.  Tk.  sürii^ü:
Auch  sürigi  'Postillon,  Stallknecht' (Kelekian  Kämüs  699b];  hieraus  rum.
155
[Ar.  sQs.
surugiü  'dass.,  Postknechf,  Ableitung surugiesc,  surugieste.
1957.  Ar.  süs:°
'Süßholz,  Glycyrrhiza'  [Dozy  Suppl  II, 119a;  aus  aram.  süM  <  ass.  süsti, ZAkkFW  .öS];  hierzu  a)  'urük  süs  [Plr. von  'irk  'Wurzel']  'Wurzeln  der  Süs- pflanze';  hieraus  sp.  orozuz,  alcazuz, pg.  alcoQHZ  'Süßholz' ;  b)  rnhb  as-süs [s.  hier  Nr.  1726]  'Fruchtsaft  des  Sas'; hieraus  sp.  rabazuz  'Mus  aus  Süßholz'. [DE  3^25/326.  327.    Eguilaz  4()7.  476.
1958.  Ar.  süsäii:
'Lilie'  [teils  bläulich  oder  dunkelviolett, teils  weiß ;  s.  FLEISCHER  u.  DOZY  in BSAW'  XX,  305;  wie  hehr,  sösan  wahr- scheinlich aus  äg.  s-ss-n  entlehnt  ZDMG XLVI,  117],  Einheitsnomeii  snsäna  ;  hier- aus mit  ar.  Art.  und  Imäla  /«  ^  e/  sp. azucena,  pg.  agiccena  'weiße  Lilie',  Ab- leitung it.  susino  'Lilienparfüm'.  [DE 228.    Eguilaz  325.    ML  8480.
1959.  Ar.  siiwär:
'Hausrat',  insbesondere  mwäv  al-'arün 'Brautausstattung';  hieraus  mit  ar.  Art. sp.  ajuar,  ajovar,  kat.  aixovar,  aljurar, pg.  enxoval  'Mitgift'.  [DE  221.  Eguilaz 79/80.    ML  7714a.
1960.  Tk.  sykmak:
'Diücken,  quälen'  [vom  Stamme  sok, sik  'eng,  dicht,  drücken'  Vämbery  Tkt EtWb  S.  152,  Nr.  164];  vom  Stamme f'-jk  wurde  rum.  säcäi,  s'icäi  'kritteln, nörgeln,  quälen'.  Das  tk.  Kausativ  lautet sylcdyrmak,  Imper.  s!/fcrf//»-;  hieraus  rum. sictir  'zum  Teufel  mit  dir',  ein  Fluch, dazu  das  Vb.  sictiri  'zum  Teufel  jagen'. —  [Der  osmanische  Fluch  k.  e.  ist  ana- syny  sykaji/m  'cum  matre  eius  coibo' oder  in  ähnlicher  Form,  z.  B.  NO  III, ^1 ;  er  ist  wie  bei  den  Türken  so  auch bei  den  Völkern  des  südöstlichen  Eu- ropas trotz  seiner  Obszönität  zur  bana- len Redensart  in  allen  Lagen  des  täg- lichen Lebens  geworden.]
1961.  Tk.  syra:
'Reihe,  Glied'  [aus  gr.  ffeipctj ;  hieraus rum.  fir  'dass.',  ^irä  'Wirbelsäule'.
1962.  Tk.  syriiia:
=== LKT leaf
183
```


## [2026-09-14T02:29:33.945Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt BQT_v1_pages.txt BQT_v2_pages.txt AFM_pages.txt DOZ.txt DEV.txt PHN.txt LAM.txt; do echo \"=== $f\"; grep -n 'سوسن' $f 2>/dev/null | head -6; done; echo \"=== ARY\"; grep -n 'سوسن' incoming/ARY/ARY_pages.txt | head -6; echo \"=== PLA\"; grep -n -i 'sausan\\|sawsan\\|susan\\|Lilie' incoming/PLA/PLA_pages.txt | head -10"
}
```


### [2026-09-14T02:29:35.475Z] TOOL RESULT

```
=== MON_part1.txt
10734:سوسنی‌ها از دستة مارچوبه‌ها که ریشه‌اش 
33882:سوسنی‌ها جزو تک لیه‌های جام و کاسه 
33920:زیبا از تیرة سوسنی‌ها جزو تککلیه‌بی‌های 
35584:(امر.) ( گیا.) سوسن. (گیا.) کل نبلوفر. (گیا.) 
40267:سوسنی‌ها جزو دستةٌ گل سوسن که گیاهی 
71659:رستی. ( کباء) سوسن. رسق ررد. ( کباء.) 
=== MON_part2.txt
20729:از تیرةُ سوسنی‌ها که گیاهی زیبا و پایا و 
33463:خیار: (گیا.) گیاهی است از تیرةُ سوسنی‌ها با 
33613:سوسنی‌ها که اصش از ایران است و 
33674:تیرة سوسنی‌ها و از دسته مارچوبه‌ها که اصل 
34302:و قاعده آور مصرف می‌شود؛ سوسن سر ح» 
34303:دورخولی؛ درحونی» گلادیول» سوسن 
=== BQT_v1_pages.txt
7502:فارخش ساختم و خلاصش کردم - و سوسن سفید
7507:حرختی را نیز که میوه ندهد ؛ و همانا که سوسن
7551:آزاده ؟ پر وژن آملده . سوسن
15537:توا فلك آفتاب را یز کویند؟ . - وناییکی را کوبند وفام یخ‌سوسن ۴ آسمان کون هم‌هست
18267:بر توسوسن سین اول مک ور
27632:کلی است‌از جنس سوسن و آنرا سوسن آسمان
=== BQT_v2_pages.txt
2222:                                                               ‫و درختآنرا سوسن گویند ‪ .‬قوت باه دهد ومنی‬
14753:                                 ‫آبادان ‪ -‬رامپرمز ‪ -‬سوسنگرد ‪ -‬دشت میشان ‪ .‬رك ‪ :‬جفر‬
17066:‫کلی است ازجنی سوسن وآ نرابعربی‌اصل‌اللوف‬
19802:                                                                                                           ‫محبوس؛ نوعی‌ازسوسن‬
21054: ‫بواو رسده ‪.‬کل رعا را گوشد جه بکروی آن‬                               ‫بواورسیده ولام بتحتانی کشیده » نوعی از سوسن‬
21862: ‫هکه سوسن‌دود‬
=== AFM_pages.txt
=== DOZ.txt
=== DEV.txt
=== PHN.txt
=== LAM.txt
=== ARY
=== PLA
312:susan        und    süsän
8358:3»,        - zambag:                       "Lilie,          Sambac'"          pers.        ı mand.                sinba,        syr.-ey3            (P-    5%   )
9585:Gu--        süsan:           "Liliet                   pers.          0%»        susan         m.             mp»    sösar    7, lat,         süsianus,
9590:Salat ausw - süsan asimänfüni:                                                 pers.          s. susan 1°.
13531:       "eine        Turban             tragende             Lilie"           s.     süsan.
14303:ou               - maisüsan:                          "eine       Art        Sirup"            —T pers..g           mai    +,        Susan       q.    V.     10,
14886:BI          - nilüfar:                "Wasserlilie"
14888:       pal     '"Wasserlilie",                      wahrscheinlich                 aus      pers.    )&    nil     "blau"    + .„ par
```


## [2026-09-14T02:29:41.425Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9575,9605p' incoming/PLA/PLA_pages.txt; echo \"=== leaf(1-based)\"; awk 'NR<=9585{n+=gsub(/\\f/,\"\")} END{print n+1}' incoming/PLA/PLA_pages.txt"
}
```


### [2026-09-14T02:29:42.484Z] TOOL RESULT

```
pls» - surädig:                            "Palast,             Haus" mp.»                          sräd       °.


ol,» - susän                 = süsan             q.    V.


Oye-       süs:       "Susa'            —       MP.yo           sus        ap.            gusa      6,


Gu--        süsan:           "Liliet                   pers.          0%»        susan         m.             mp»    sösar    7, lat,         süsianus,
       griech.           sousianos                   aus     susa,          einer         antiken         Stadt       Persiens       8, SYr.O8 ,
       hebr.          a        9 .


Salat ausw - süsan asimänfüni:                                                 pers.          s. susan 1°.

u           _    süsanbar:                 "Mentha           aquatica,               Wasserminze;                sismbrium,         wilde      Thyme,
       Thymian!"             pers.           Kat.) DEI VERREN sisambar                          11       mand.       susambar,       syr,.     main     12


Op -        aug:       "Markt;               Richtung"               mp.             sog       13     syr.      vun,      mand.     suga >»



1.    al-Munfid              s.      v.
2. Hosrow             OQobadan             n.    Chista          Bd.        9 s.         v.
3.    Muhit       s.     v.,         al-MuCarrab                 s.       v.
4.    Mackenzie              Ss.     Vv.
5.    Nyberg          Bd.      II       s.      v.
6.    ebda.
=== leaf(1-based)
184
```


## [2026-09-14T02:29:50.618Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=NYB=\"; grep -n -i 'sōsan\\|sosan\\|swsn\\|lily' NYB.txt | head -20; echo \"=PHD=\"; grep -n -i 'sosan\\|sōsan\\|swsn\\|lily' PHD.txt | head -20"
}
```


### [2026-09-14T02:29:50.692Z] TOOL RESULT

```
=NYB=
=PHD=
514:nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, water-lily. nimüdan, nimāy- [nmwtn', nmd- | M nmwdn, nm’y-, N ~] show, guide. nirfs- [nlps-] wane, decrease. ~išn: decrease, diminution. nirmad [nylmt'] profit, interest. ~ӧтапа [-’wmnd] profitable. P nisag [nys’k' | P nys’g] bright, splendid. niš- [nyi- | M nyyš-ydn, J ~] see, observe. nišān-, v. nišāstan. nīšān [ny$*x! | = M, N nisàn] sign, mark, banner. nišast [nsst! | N ~] association. nišastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit. nišāstan, nišān- [Y TY BWN.stn!, 2n-; nP?stn!, nP?n- | M nf?st, (nP5y-), N ~] set, seat, plant, found. nišāyišn [n£ din! | M n$?y-, v. niSástan] foundation. nišēb [niyp | N ~] declivity; astr. dejection. ~ig [-yk'] declining. nišēm (nidm | M nšym, N ~an] seat, perch. ~ag [-k'] residence, abode. niSin-, v. niSastan. niwāģ [nw k! | M ng, N nawa] music, song, melody. *niwé [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
2633:lily sēsan.
4279:water-lily nīlēpal.
```


## [2026-09-14T02:29:51.213Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9605,9625p' incoming/PLA/PLA_pages.txt"
}
```


### [2026-09-14T02:29:51.268Z] TOOL RESULT

```
6.    ebda.
7.    Mackenzie              s.      v.,        Unvala          s.    v.,        Bq.      S.    1188.
8.    Genaust          Ss.    v.
9.    Ellenbogen               s.       v.,      Brockelmann                   s,    v.
10.    Löw       s.    v.
11.    Löw       s.    v.,         Mackenzie               s.    v.,        Bundahi$fn           s.      v.
12.    Macuch          s.     v.
13.    Mackenzie               s.       v.,      Nyberg          Bd.        II      s.    v.
14.    Macuch          s.     v.,          Brockelmann                 s.      v.
sib                                                                      170                                              simasanfarf


De za -    sib:         "Apfel"             pers.     Ic          MP.»            SEb    2,


arme       —   sibaway:                der     berühmte           Grammatiker                 iranischer       Herkunft          pers.
          u»            Sib-büy-ye,                 wörtlich           "der        nach       Apfel     Duftende".


er        sin:      "Bratspieß"                    pers.
```


## [2026-09-14T02:30:00.390Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'سوسن' MON_part2.txt | head -40"
}
```


### [2026-09-14T02:30:00.455Z] TOOL RESULT

```
20729:از تیرةُ سوسنی‌ها که گیاهی زیبا و پایا و 
33463:خیار: (گیا.) گیاهی است از تیرةُ سوسنی‌ها با 
33613:سوسنی‌ها که اصش از ایران است و 
33674:تیرة سوسنی‌ها و از دسته مارچوبه‌ها که اصل 
34302:و قاعده آور مصرف می‌شود؛ سوسن سر ح» 
34303:دورخولی؛ درحونی» گلادیول» سوسن 
34306:سوسن صحرایی» اریدبرید. کسیقون. 
35493:(ص.) اصم. گنک دهزبان: (کد.) گل سوسن 
35496:سوسن سفید است. 
42184:سوسنی‌ها و از دستةٌ مارجوبه‌ها که گیاهی 
69191:است علفی و پایا از تیرهُ سوسنی‌ها و از دستة 
69724:ابن شراب «می بخته» است. می سوسن:- 
69725:شربت سوسن. می شعری‌فش: شراب 
77223:نعنای فلفلی: ( گیا.) سوسنبر. نعناعی وحشی:
```


## [2026-09-14T02:30:06.252Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'سوسن' MON_part1.txt | head -40; echo \"=== ctx 10730\"; sed -n '10725,10745p' MON_part1.txt"
}
```


### [2026-09-14T02:30:06.338Z] TOOL RESULT

```
10734:سوسنی‌ها از دستة مارچوبه‌ها که ریشه‌اش 
33882:سوسنی‌ها جزو تک لیه‌های جام و کاسه 
33920:زیبا از تیرة سوسنی‌ها جزو تککلیه‌بی‌های 
35584:(امر.) ( گیا.) سوسن. (گیا.) کل نبلوفر. (گیا.) 
40267:سوسنی‌ها جزو دستةٌ گل سوسن که گیاهی 
71659:رستی. ( کباء) سوسن. رسق ررد. ( کباء.) 
77729:تبر ۵ سوسنی‌ها که دارای گل‌های زینتی است 
79843:(گیا.) گیاهی است از تیرةٌ سوسنی‌ها جزو 
81246:سوسن: 5۱527 [م عر.] (.) (گیا.) گیاهی 
81247:است از تیرة سوسنی‌ها که جزو گیاهان 
81255:فیلگوش» پیلغوش؛ زنبق رشتی. سوسن 
81256:الوان: (گیا.) گونه‌ای سوسن که دارای 
81258:گونه سوسن از ژاین است» سوسن 
81259:خوش‌اندام. سوسن بری: (گی.) گونه‌ای 
81266:وی بسیر طبوع است. این گونه سوسن در 
81268:سوسن چینی: (گیا.) گ وهای سوسن که 
81270:لاجوردی است. اصل این کونه سوسن از 
81271:هیمالیا می‌باشد؛ سوسن ختایی» سوسن 
81272:لا.جوردی» ابماروقالس» سوسن کبود» 
81273:سوسن زرد: (گیاء) یکی از گونه‌های سوسن 
81274:زنبق» سوسن ژاپنی. سوسن سفید: ( کیاء.) 
81275:سوسنی که دارای گل‌های سفید است. ایبن 
81277:بیشتر پرورش می‌دهند» سوسن آزاد؛ سوسن 
81278:انیض» سوسن ده‌زیان» سوسن کل دراز. 
82186:سوسنی‌ها که علفی و پیازدار و شامل 
88786:سوسنی‌ها جزو دسته تک لیه‌بی‌ها که دارای 
=== ctx 10730
کاری. 

ازمان: 2210 [ع.] (مص‌ل.) کهنه شدن» 
دیرنه گشتنر 

از محر د م گر یز ال «22-00۵۲0000-807]22 
۳۱۳ ی انزواطلب» منزوی» 
کسی که با مردم نمی آمیزد و حشر و نشر 
از ملک: »دادهعه (.) (گیا.) گیاهی از تيرة 
سوسنی‌ها از دستة مارچوبه‌ها که ریشه‌اش 
خاصیت دارویی دارد. چون به گیاهان مجاور 
می‌بیجد ظاهراً با پیچک‌ها اشتباه می‌شود. 
ساقه‌اش خاردار است» بالگا. 

از تسده (6-)22016112 [ع. ۰ (.) 3 
ز مان زمان‌ها» روزگارها 

از میان برداشتن 
(مص ع.) منهدم کردن» تشتتا گر دانمد 0 
تمام کردن» به بایان آوردن.
```


## [2026-09-14T02:30:18.069Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '81240,81282p' MON_part1.txt"
}
```


### [2026-09-14T02:30:18.130Z] TOOL RESULT

```
مرادف با سوسمار آبی با یه ح بکار رفته 
است ولی باید دانست که نهنگ معمولاً 
مرادف با پستانداران عظیم ماهی شکل 
دریایی است که بنام بالن يا کاشالوت نامیده 
می‌شوند. 

سوسن: 5۱527 [م عر.] (.) (گیا.) گیاهی 
است از تیرة سوسنی‌ها که جزو گیاهان 
تکث یه بی جام و کاسه نگین است. گلی 
است فصلی و دارای گل‌های زیبا و درشت 
به رنگ‌های مختلف. اصل این گیاه از ارو با 
و ژاين و آمریکای شمالی و هبمالیا است. 
جهت ازدیاد این گُیاه یو در پاییز 
پیازهای فرعی را از پباز اصلی جدا می‌کنند و 
در بهار مسجدداً سی‌کارند؛ پیلگوش؛ 
فیلگوش» پیلغوش؛ زنبق رشتی. سوسن 
الوان: (گیا.) گونه‌ای سوسن که دارای 
گل‌های درشت و رنگارنگ است. اصل این 
گونه سوسن از ژاین است» سوسن 
خوش‌اندام. سوسن بری: (گی.) گونه‌ای 


۳ ۰ سس ۰ 
سوسوردن ت فاررسی معین ۸۷ 


وی بسیر طبوع است. این گونه سوسن در 
اردسهشت 9 تا و گل‌های آن 
سوسن چینی: (گیا.) گ وهای سوسن که 
دارای ساقه‌های سیر و نك و گل‌های 
لاجوردی است. اصل این کونه سوسن از 
هیمالیا می‌باشد؛ سوسن ختایی» سوسن 
لا.جوردی» ابماروقالس» سوسن کبود» 
سوسن زرد: (گیاء) یکی از گونه‌های سوسن 
زنبق» سوسن ژاپنی. سوسن سفید: ( کیاء.) 
سوسنی که دارای گل‌های سفید است. ایبن 
گونه را به مناسبت زیسایی خاصی که دارد 
بیشتر پرورش می‌دهند» سوسن آزاد؛ سوسن 
انیض» سوسن ده‌زیان» سوسن کل دراز. 
۳" وجه تسم ده‌زیان بدان جهت است 
که کاس رگک‌ها نیز همانند گل‌ب رگ‌ها سفید و 
مشاه آنهایند و با توجه به اينکه تعداد هر 
یکت ۵ عدد است بدین تام موم سده۵.
```


## [2026-09-14T02:30:20.365Z] TOOL CALL #24: Bash

```json
{
 "command": "pdftoppm -f 465 -l 465 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg465 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg465.png"
}
```


### [2026-09-14T02:30:22.396Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 50604 Sep 13 22:30 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg465.png
```


## [2026-09-14T02:30:27.975Z] TOOL CALL #25: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg465.png"
}
```


### [2026-09-14T02:30:28.773Z] TOOL RESULT

```

```


## [2026-09-14T02:30:28.757Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T02:30:50.322Z] TOOL CALL #26: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T02:30:50.331Z] TOOL RESULT

```


```


## [2026-09-14T02:30:53.876Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%B3%D9%86",
 "prompt": "Give the full etymology sections for the Persian, Arabic, and any other language entries of سوسن (lily): source language, Middle Persian form, Aramaic/Akkadian/Egyptian antecedents, and cited authorities."
}
```


## [2026-09-14T02:30:54.996Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Susan",
 "prompt": "Full etymology of the English given name Susan: Latin Susanna, Greek Sousanna, Hebrew Shoshannah, Egyptian source."
}
```


### [2026-09-14T02:31:00.509Z] TOOL RESULT

```
# Etymology of سوسن (Lily)

## Arabic

The Arabic entry traces the word's origins through multiple ancient languages. According to the source: "From Middle Persian (swsn' /⁠sōsan⁠/), from Ancient Greek σοῦσον (soûson), ultimately from Egyptian zšn." The entry notes this is a "doublet of سُوزَان (sūzān)."

## Persian

The Persian section provides comparable etymological information: "From Middle Persian (swsn' /⁠sōsan⁠/), from Ancient Greek σοῦσον (soûson), ultimately from Egyptian zšn." It additionally compares related forms across multiple ancient languages including "Old Armenian շուշան (šušan), Old Georgian შროშანი (šrošani), Biblical Hebrew שׁוֹשָׁן (šōšān), and Aramaic שַׁוֹשַׁנְתָּא (šōšantā)."

## Cited Authorities

The Arabic section references historical lexicographical works by Freytag (1833), Edward William Lane (1863-1893), Hans Wehr with Lorenz Kropfitsch (1985), and Heinrich Zimmern (1915), who documented Akkadian loan word evidence.
```


### [2026-09-14T02:31:01.936Z] TOOL RESULT

```
# Susan - Etymology and Meanings

**Primary Definition:**
Susan is a female given name derived from Hebrew, meaning "lily." The name traces back through multiple languages: Biblical Hebrew *šōšannā*, Greek Sousanna, and ultimately Egyptian origins.

**Etymology Path:**
According to the Wiktionary entry, the name comes from "the biblical Susanna, from Biblical Hebrew שׁוֹשַׁנָּה (šōšannā, 'lily'), ultimately from Egyptian" sources. The name has been "in continuous use since the Middle Ages, with the latest popularity peak in the mid-twentieth century."

**Secondary Meanings:**
Beyond the given name, "Susan" also functions as a historical adjective and noun referring to "the ancient city of Susa," though this usage is marked as archaic.

**Notable Variants:**
The name has numerous English variants including Susanna, Susannah, Suzanne, and diminutives like Sue, Susie, and Suzy. It appears across 20+ languages with localized versions such as Czech Zuzana, French Suzanne, and Spanish Susana.

**Cultural Reference:**
The name appears in Shakespeare's *Romeo and Juliet* and maintains prominence in contemporary usage, including in recent 2025 news references.
```


## [2026-09-14T02:31:07.774Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%83%CE%BF%E1%BF%A6%CF%83%CE%BF%CE%BD",
 "prompt": "Etymology of Ancient Greek σοῦσον 'lily': source language (Semitic? Egyptian?), descendants, and cited authorities (Beekes etc.)."
}
```


## [2026-09-14T02:31:09.425Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%A9%D7%95%D7%A9%D7%9F",
 "prompt": "Etymology of Hebrew שושן / שושנה 'lily': Egyptian origin, Akkadian and Aramaic cognates, descendants (Greek Sousanna)."
}
```


### [2026-09-14T02:31:13.565Z] TOOL RESULT

```
# Etymology of σοῦσον (Lily)

## Source Language

The Ancient Greek word σoῦσον derives from **Egyptian origin**. The entry notes it was "Borrowed from Egyptian _zšn_." Related cognates appear in Biblical Hebrew (_šōšannā_, "lily") and Coptic (_šōšen_).

## Descendants

The term dispersed widely through Persian and Arabic, generating descendants across multiple language families:

- **Persian**: سوسَن (sōsan)
- **Arabic**: سَوْسَن (sawsan)
- **Romance languages** (via Andalusian Arabic): Spanish _azucena_, Portuguese _açucena_, Galician _azucena_, Catalan variants
- **Asian languages**: Tagalog and Cebuano _asusena_
- **Azerbaijani**: süsən

## Cited Authorities

The entry references major lexicographic works:
- Liddell & Scott's _A Greek–English Lexicon_ (1940)
- Bailly's _Le Grand Bailly: Dictionnaire grec-français_ (1935)
- Beekes' _Etymological Dictionary of Greek_ (2010)
```


### [2026-09-14T02:31:16.161Z] TOOL RESULT

```
# שושן (Shushan/Susán)

This Hebrew word has two distinct etymologies:

## Etymology 1: Lily (the flower)

**Meaning:** "lily"

**Origin:** Derived from Egyptian *zšn*. The word appears across related languages, including Ancient Greek *σοῦσον* (soûson) and Coptic *ϣⲱϣⲉⲛ* (šōšen), all referring to the same flower.

**Pronunciation:** 
- Tiberian Hebrew: /ʃoːˈʃɔːn/
- Modern Israeli: /ʃoˈʃan/

## Etymology 2: Susa (the ancient city)

**Meaning:** Susa or Shushan, the ancient capital of Elam in modern-day Iran

**Origin:** Ultimately from Elamite *šušen*, with cognates in Old Persian and Ancient Greek *Σοῦσα* (Soûsa).

**Pronunciation:**
- Tiberian Hebrew: /ʃuːˈʃɔːn/
- Modern Israeli: /ʃuˈʃan/

The word appears in biblical texts, notably in the Book of Esther, referencing the royal residence of King Ahasuerus.
```


## [2026-09-14T02:31:24.592Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Susan",
 "prompt": "Etymology of Susan/Susanna: Latin, Greek, Hebrew shoshannah, Egyptian sshn lotus; any mention of Akkadian or Persian."
}
```


## [2026-09-14T02:31:25.237Z] TOOL CALL #32: WebSearch

```json
{
 "query": "Akkadian šūšanu \"lily\" Egyptian sšn loanword Zimmern šušanu"
}
```


### [2026-09-14T02:31:29.346Z] TOOL RESULT

```
# Etymology of Susan

Based on the online etymology dictionary, the name Susan has the following origins:

**Direct lineage:** The name derives from French *Susanne*, which came from Late Latin *Susanna*.

**Earlier roots:** *Susanna* itself traces back through Greek *Sousanna* to Hebrew *Shoshannah*, which literally means **"a lily."**

**Historical significance:** Susan was notably popular in the United States, ranking among the top 10 girls' names from 1945-1968, with its peak popularity at #2 between 1957-1960.

**Related forms:** Common variants and shortened versions include Sue, Suzie, and Sukey, with Sue being described as "a shortened or familiar form of Susan."

The page notes that this Hebrew word for lily was also borrowed into Greek in its literal sense as *souson*. The biblical reference mentions that Susanna was "one of the women that attended Jesus in his journeys."
```


### [2026-09-14T02:31:31.878Z] TOOL RESULT

```
Web search results for query: "Akkadian šūšanu "lily" Egyptian sšn loanword Zimmern šušanu"

Links: [{"title":"Akkadian Loanwords in Biblical Hebrew - Paul V. Mankowski - Google Books","url":"https://books.google.com/books/about/Akkadian_Loanwords_in_Biblical_Hebrew.html?id=rt6mDwAAQBAJ"},{"title":"Balashon - Hebrew Language Detective: shoshana","url":"https://www.balashon.com/2009/03/shoshana.html"},{"title":"iii Papers on Semitic and Afroasiatic Linguistics in Honor of Gene B. Gragg","url":"https://starlingdb.org/Texts/akkegypt.pdf"},{"title":"שׁוֹשַׁנָּה — Lily / Rose | Elon Gilad","url":"https://www.elongilad.com/en/etymology/%D7%A9%D7%95%D7%A9%D7%A0%D7%94"},{"title":"(PDF) Akkadian Loanwords in Sumerian Revised","url":"https://www.academia.edu/7291409/Akkadian_Loanwords_in_Sumerian_Revised"},{"title":"On Sumerian Loanwords in Akkadian. Part I","url":"https://www.researchgate.net/publication/330696042_On_Sumerian_Loanwords_in_Akkadian_Part_I"},{"title":"Aula Orientalis 23 (2005) 191-198 191 Loanwords in Semitic","url":"https://www.ub.edu/ipoa/wp-content/uploads/2021/09/200512AuOr12Watson.pdf"}]

Based on the search results, I found relevant information about this linguistic topic:

Several scholars derive these words from Egyptian sshshn and sshn, Coptic shoshen (meaning big flower; lotus). The Akkadian cognate is sheshanu (meaning lily).

The word Shoshana traces its roots back to Ancient Egyptian sšn (seshen), which referred to the water lily or lotus. This represents a loanword relationship between Egyptian and Akkadian, with the word also appearing in related Semitic languages.

The search results reference scholarly discussions of this etymology, including work by various linguists studying loanwords between Akkadian and Egyptian, though specific citation of Zimmern's work appears in bibliographic references rather than detailed discussion in these particular search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T02:31:39.186Z] TOOL CALL #33: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1188 --image 2>&1 | tail -40"
}
```


### [2026-09-14T02:31:40.293Z] TOOL RESULT

```
no scan of BQT covers printed page 1188 (see 'scans' in refs_online.json)
```


## [2026-09-14T02:31:43.940Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n 'pdf page' BQT_v2_pages.txt | head -3; echo ---; python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'سوسن' in p:\n        print('leaf',i, p[:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T02:31:45.126Z] TOOL RESULT

```
---
leaves 684
leaf 40   ‫اس‬      ‫‪۲‬‬                                                               
leaf 251   ‫خوزی‬                                                                        
leaf 290 ‫سوم برس‬                                                                       
leaf 334         ‫مت‬   ‫هد کنابه از عشتاق و مهجور‬               ‫دون‬                  
leaf 355       ‫دز رو‬                                                                   
leaf 369    ‫دور‬                                                                        
leaf 387    ‫راست‬                                                                       
leaf 389                                                                                 
leaf 559                                                                                 
leaf 599                                                                                 
leaf 634       ‫و‪۷‬‬                                                                    
leaf 652     ‫اس‬                            ‫‪۱‬‬                                       
leaf 668 ‫ودرین روز گوشت وسیر برادر پیازخورندو گویند‬               ‫رگاعی ئىز هت که سوست
```


## [2026-09-14T02:31:54.138Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i in range(655,684):\n    p=pages[i]\n    if 'سوس' in p or 'سوز' in p:\n        idx=p.find('سوس')\n        print('--- leaf',i)\n        print(p[max(0,idx-300):idx+600])\nEOF"
}
```


### [2026-09-14T02:31:55.367Z] TOOL RESULT

```
--- leaf 656
 ‫کردیده ‪ ,‬وآن نام بتی بود ومعنی ترکیبی آن‬                        ‫سو منات ‪ = ۹‬هم اول وفتح میم‌ولون‬
‫سوم نات است بعنی صنمی است امول قمر» چه‬                           ‫بالف کشیده بروزن مهمالات‪:‬خانه‌ای بودم‌درملك‬
      ‫سوم بپندی قمررا گوبند ونات تءظیم‌است‬                        ‫گجرات‪ .‬کونند سلطان محمود غبزنروایاخراب‬
 ‫سومندر ‪ = ۲‬با دال ابجد بر وزن‬                                   ‫کرد ومنات راکه از بتهای مشپور است در آن‬
 ‫سوزنگر » بمعنی سمندراست» وآن‌جانوری باشد‬                        ‫‪ .‬و بعضی گوبند که‌فریش‬    ‫بتخانه مشیبکودست‬
                                        
--- leaf 657
‬                     ‫‪۶‬‬       ‫)‪ (۱‬در چك چا‬

                                                                                         ‫تصحیح شده ‪.‬رك ‪ :‬ح‪. ۳‬‬


       ‫بزرگ‬‫‪.‬قرب ایست‬       ‫سوج‬      ‫‪.‬مودو‬    ‫اظ‬    ‫‪۳‬‬       ‫(«‪.‬م‪).‬‬    ‫سان‬   ‫‪= ۲‬‬           ‫‪.‎ ٩‬یوسوس‪:‬كر‬
  ‫معج‌الباد ان ‪.‬‬
  ‫از‬



                    ‫‪٩۱‬‏‬   ‫معر وف بفقیه سواسی‌بدان ‪٥‬وت‬          ‫أ حم بر !می‌الاسم‪ ۳ .‬وی‬                    ‫‪۰‬اف‬        ‫تواحیذف‬




   ‫«منوجپری دامفانی ‪۴۲۱‬؟‪.‬‬
                                                  ‫بگشاده‬   ‫‪ - ۴‬برمرش ( الل)ر يکيغالیهدای‬
                                     ‫دنار‪.‬‬    ‫و | گنده در آن غا[ہه دان سواش‬

               ‫رك؛ سو ست ‪/‬‬    ‫‪= ۷‬‬            ‫‪ - ٩‬رك‪ :‬سوزن‪. ‎‬‬                         ‫رك ‪ :‬سوهان‪. ‎‬‬               ‫*‬

           ‫‪۰‬‬    ‫سد کسی («‪.‬ء‪‎).‬‬   ‫=‬    ‫«سد کته‬   
--- leaf 660
                                            ‫باشد ‪.‬‬      ‫سه ستبل ؟ = بنتح سین بی قطه (‪)۷‬‬
  ‫کماف فسارکسیونولام؛‬
                    ‫سه گل ‪ -‬ن‬                               ‫و سکون لون و بای ابجد (‪ )۳‬مضموم‌بلام زده‪,‬‬
 ‫نام درختی است که‌میوءآن چون پخته شودسرخ‬                   ‫بمعنی سوستبر است » و آن سبزیی باشد میان‬
 ‫گردد و بغابت قابض باشد وآنرا بفارسی‌توت‌سه‬                 ‫پودنه و عناع زبرا که چون بودنه رادست نتان‬
 ‫کل و بعربی توث العلیق خوانند چه درخت‬                        ‫که ور شوو و افا یسار نر گونتهه‬
‫آلرا عربان علیق گوبند » وتوث وحشی لیزهمان‬                   ‫سه شاخ ‪ -‬با شن قرعت (‪ )4‬بالف‬
                                 ‫اع ‪: ۷‬‬                         ‫کشنده وبخای نقطه‌دار (ه) زده » بمعنی‌سهروح‬
‫سه "نید ان ‪ -‬عبارت از قلمهةٌ سنگوان‬                         ‫اهبه از موالید ثلائه باثد وآن حیوان‬‫اکستن ک‬
 ‫است که در شبراز بپیدان مشهور است وآن سه‬
--- leaf 668
‫ودرین روز گوشت وسیر برادر پیازخورندو گویند‬               ‫رگاعی ئىز هت که سوسته در آبرای استاده‬

‫که خوردن‌آن ايمن بودن ازمس جن است‌وجن‬                                   ‫حیض را‬        ‫روبد و خوردش‬
                              ‫کگرفته را آ‬
 ‫انز‌دهند‪ .‬یك است درین روزفرزند‬                                         ‫بگهاید وبول را برائد و آلرا‬
               ‫دادن وسثه وصنمت آموختن ‪۰‬‬         ‫شک‬

‫و کتابه‬          ‫‪۴‬‬   ‫معروفت‬     ‫=‬   ‫سیر شدن‬                                                      ‫خوانند ‪.‬‬
‫از‬     ‫كاھ‬      ‫‪2‬‬    ‫است‬    ‫از هر جر‬   ‫شدن‬     ‫از اد‬
                                                                        
--- leaf 669
                                                        ‫‪a‬‬               ‫‪ ٩‬بنقل از هاینریش»‪‎.‬‬
   ‫قس ‪( 055‬اسب ) در ‪ ۳‬اکدی و آشوری که در‬                            ‫‪6‬‬           ‫‪ :‬سیج ‪.‬‬   ‫قی‬   ‫‪-‬‬    ‫‪۴‬‬


       ‫آرامی ‪ 272505‬شده و صورت هزوارش وارد پهلوی گردیده ( رك‪ :‬سوسبار ) « فاب‪۱‬ص‪:۲۳۲‬‬
                                              ‫تنگ گردد چون دل عاشق جهان بر دشمنت‬
            ‫روز هیجا کچوین‌برسیس بکران تنگه تیکه‪.‬‬
   ‫عبدالرزاق اصفهالی‪« .‬فرهنگك نفام»‪.‬‬
              ‫‪۱‬‬             ‫‪ ۲6515‬د لك ‪ ۲‬ص ‪۰ ۰۱۳‬‬             ‫‪= ۷‬‬                  ‫ق‬            ‫ر‬


        ‫‪nabsie=s 4‬‏ ‪ ° sohciloD‬لك ص‪. ۰۱۳‬‬                  ‫‪ ۸‬رل ‪ :‬ساسالوس ‪.‬‬
   ‫‪ #‬سیزده ‪ -‬بکر اول وفتح چپادم ‪ ,‬اوستا ‪ ( )25201۳0‬سیزده) ؛ بهلوی|‪, 206]5‬‬
   ‫‪ .‬افقانی‬          ‫بازند ‪ 0602۵5‬و ‪ 120012۵5‬؛ هندی باستان ‪asad‬‏ ‪ > öy4rt‬کردی ع ‪0‬‬

--- leaf 670
     ‫سیسنبر ون = با رای (‪ )۱‬بواورسیده‬
                                              ‫دار‬       ‫ره‬   ‫(‪ )۲‬چك ‪- :‬‬              ‫(‪ )۱‬چك ‪ :‬بارا ‪.‬‬

      ‫‪ - ۴‬رك‪ :‬سیتروءسیك‪,‬وقس‪:‬سوی‪.‬‬                   ‫(«‪.‬م‪٣ ).‬‏ تن (بوند مصدری ) ‪۰‬‬            ‫= از ‪ :‬سسس‬

  ‫‪.‬‬   ‫سوس‬     ‫‪ 4‬سیسرو؛وقس‪:‬‬    ‫‪ :‬سى سرك‬   ‫رك‬   ‫=‬     ‫‪۴‬‬        ‫وفس‪-:‬وس‪.‬‬       ‫بسك‬   ‫رك ‪ :‬مسر ‪۰ 4‬‬          ‫‪۴‬‬

  ‫(لاتینی) «لك ‪۲‬س ‪ < »۹۰۳‬فرهنگه‬                     ‫‪my‬‬
                                                     ‫‪ıibs‬‬
                                                        ‫=نان ‪mu = 80170000515‬‏‬
                                                                             ‫‪ ۵‬و‬
  ‫» اصاب‬       ‫طمری ‪mesreS‬‏‬      ‫لانبای ‪ -‬انگلیسی ‪ .‬مرچنت » پپلوی ‪ « ۲200۳155‬اونوالا ‪۰ ۷4۳۰‬‬
                                                           
--- leaf 676
    ‫ه‬
    ‫ا‪۲ ۷‬‬

               ‫از آب صاف و شراب صافی باشد‪.‬‬        ‫سیم گاورس دار د کنا بهاز‬
‫سیهناة ‪ - ۴‬بادونبروزن زیر باد »‬                    ‫ماه با ستارکان باشد‪,‬چه ستاره را بگاوری‌تشبیه‬
‫بمعنی سوزه باشد همجو سورتالحمد و سور قل‬
                                                   ‫بختح کاف » استاد فتول‬
‫سی مهرخ ماه صیام ‪ -‬کنابهاز‬                         ‫کش را کوینداعم از آنکه مفتول طلاو قرموآ هن‬

                   ‫سی‌روز (‪ )۱‬ماه رمان است‬         ‫وامثال آن بکشد ‪ -‬وکنایه ازمردم جراروچیزی‬
 ‫هس‌ینبروزن‬
          ‫سیمه سبایر‌*ش‪-‬لبا‬                        ‫گیرن
--- leaf 678
است که دررآوبید و بجای سوخته‬                     ‫سینی = بروزن چینی ‪ ۰‬خوالی باشد که‬
                                 ‫‪ 3‬آتشگیره بکار بنرك‪.‬‬    ‫و برنج سازند ‪-.۷‬‬             ‫مهس‬
                                                                                      ‫و‬ ‫آنرا ازطلا و نقر‬
‫سوس = منم اول بر وزن خروس ‪۰‬‬
‫نام درختی است ؛ و بعضی کوبند نام کیاهی‬
                                             ‫است ‪4 .‬‬
‫سیو بست ‪ = ۴‬بنتح اول بروزن شش‬
 ‫گاآه نبودن است »‬
                ‫بیست » بمعنی نا | گاهی و‬

 ‫سیه ‪ = ۳‬بكر اول بروزن نگه‪.‬مخنف‬
 ‫لافاحم حبشی وحندی‬   ‫غت ط‬
                        ‫سیاه است ‪ -‬وومس‬
‫نوکی را یز گویند ‪ -‬و نامخط چهارم است از‬
 ‫جملاهفت خط جام جآمنورا خطازرق نخیوزالند‬
‫و‪-‬پمعنی نس و شوم هم هت ‪ -‬و نام اسب‬
 ‫کتامی‌انت‬   ‫عه ونام‬    ‫زوه‬
                          ‫اسفند بار است وآن ستاه ن‬

                             ‫از مصنفات زردشت
```


## [2026-09-14T02:32:22.969Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D9%88%D8%B3%D9%86/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for سوسن, including any bracketed origin tag such as [معر.] or [په.], and any Dehkhoda etymological note about the origin of the word."
}
```


## [2026-09-14T02:32:24.904Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.balashon.com/2009/03/shoshana.html",
 "prompt": "Summarize the etymology of shoshana/shushan: Egyptian sšn, Akkadian sheshanu, Aramaic, Arabic sawsan, Persian susan, Greek souson; which authorities are cited (Klein, Kaddari, etc.)."
}
```


### [2026-09-14T02:32:28.399Z] TOOL RESULT

```
# فرهنگ معین Entry for سوسن

According to the فرهنگ معین dictionary section, the entry reads:

**(سَ) [معر.] (اِ.)** "گلی است بابرگ های دراز و باریک و گل های خوشبو به رنگ های مختلف"

This translates to: a flower characterized by long, narrow leaves and fragrant blossoms in various colors.

The bracketed tag **[معر.]** indicates the word has an **Arabic origin** (معرّب = arabicized/borrowed into Persian).

Notably, the Dehkhoda etymological notes provide additional historical context, mentioning that سوسن originates from Middle Persian *sōsan* or *sōsanag*, and that related forms appear in Greek (Souson), Hebrew (Shoshan), and Arabic (سوسن), all derived from this Persian root.
```


### [2026-09-14T02:32:31.785Z] TOOL RESULT

```
# Etymology of Shoshana/Shushan

According to Klein's etymological dictionary, the word traces back through multiple ancient languages. The entry notes connections to "Aramaic שושנתא (whence Ugaritic twt, Arabic sausan, Vulgar Arabic susan), Akkadian sheshanu (=lily), Syriac shishno (=butomus flowers)."

## Ancient Sources

Several scholars propose Egyptian origins, deriving the word "from Egyptian sshshn and sshn, Coptic shoshen (=big flower; lotus)." Alternative theories suggest descent from Akkadian roots meaning "six-sided" or "sixth."

## Key Authorities Cited

**Klein** provides the most comprehensive etymological treatment, listing two separate entries for the term's various meanings.

**Kaddari** identifies the flower specifically as *lilium candidum*, referencing it as "the shoshan hatzachor" appearing on historical currency.

**Steinberg** identifies both shoshan and shoshana as lily varieties.

**Ibn Ezra** connects the word to *shesh* (six), noting the flower characteristically has "six [_shesh_] petals, within which are six long filaments."

The evidence suggests an ancient Near Eastern origin that spread across multiple language families through trade and cultural contact.
```


## [2026-09-14T02:32:59.311Z] TOOL CALL #38: WebSearch

```json
{
 "query": "Akkadian \"šūšanu\" OR \"šušanu\" lily CAD Chicago Assyrian Dictionary Egyptian loanword"
}
```


### [2026-09-14T02:33:06.569Z] TOOL RESULT

```
Web search results for query: "Akkadian "šūšanu" OR "šušanu" lily CAD Chicago Assyrian Dictionary Egyptian loanword"

Links: [{"title":"The Assyrian Dictionary of the Oriental Institute of the University of Chicago (CAD)","url":"http://www.aina.org/cad.html"},{"title":"The Assyrian Dictionary of the Oriental Institute of the University of Chicago (CAD) | Institute for the Study of Ancient Cultures","url":"https://isac.uchicago.edu/research/publications/chicago-assyrian-dictionary"},{"title":"Chicago Assyrian Dictionary","url":"https://en.wikipedia.org/wiki/Chicago_Assyrian_Dictionary"},{"title":"THE ASSYRIAN DICTIONARY OF THE ORIENTAL INSTITUTE OF THE UNIVERSITY OF CHICAGO","url":"https://isac.uchicago.edu/sites/default/files/uploads/shared/docs/cad_z.pdf"},{"title":"The Chicago Assyrian Dictionary (CAD)","url":"https://www.atour.com/library/cad/"},{"title":"Dictionaries and Lexica 📖 — eAkkadian","url":"https://digitalpasts.github.io/eAkkadian/bibliography/dictionaries.html"},{"title":"The Assyrian Dictionary of the Oriental Institute of the University of Chicago (CAD) : Oriental institute of Chicago : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/Assyrian_cad"},{"title":"THE ASSY RIAN DICTIONARY OF THE ORIENTAL INSTITUTE OF THE UNIVERSITY OF CHICAGO","url":"https://isac.uchicago.edu/sites/default/files/uploads/shared/docs/cad_r.pdf"},{"title":"iii Papers on Semitic and Afroasiatic Linguistics in Honor of Gene B. Gragg","url":"https://starlingdb.org/Texts/akkegypt.pdf"}]

I've searched for information on the Akkadian terms "šūšanu" or "šušanu" (lily) in the Chicago Assyrian Dictionary with a focus on Egyptian loanword connections. The search results provide general information about the Chicago Assyrian Dictionary (CAD) itself and note that there are Egyptian-Akkadian lexical borrowings, but don't contain specific information about the entry for šūšanu/šušanu or its etymological status as an Egyptian loanword.

The Assyrian Dictionary of the Oriental Institute of the University of Chicago (CAD) is the dictionary of Akkadian (Assyrian), compiled over a 90 year period by scholars at the Oriental Institute of the University of Chicago. This is a dictionary of 21 volumes (1956-2010) that presents Akkadian words in context with references to the cuneiform texts.

The search results confirm that Egyptian-Semitic inter-borrowings include several isolated Egyptian loans in Ugaritic, Aramaic, Arabic, Neo-Babylonian and Neo-Assyrian, suggesting that Egyptian loanwords in Akkadian are documented. However, the specific entry for šūšanu/šušanu and its classification as an Egyptian loanword would require consulting the CAD directly or accessing scholarly literature specifically focused on that term.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T02:33:14.781Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in ARB_mo3rb.txt ARB_abdulraheem.txt AFM.txt AFM_alt.txt FVQ.txt AKD.txt AHM.txt; do echo \"=== $f\"; grep -n 'سوسن\\|السوسن' $f 2>/dev/null | head -5; done; echo; ls | sed -n '60,200p'"
}
```


### [2026-09-14T02:33:15.983Z] TOOL RESULT

```
=== ARB_mo3rb.txt
=== ARB_abdulraheem.txt
=== AFM.txt
=== AFM_alt.txt
5876:سوسن ٠ ٠ ٠‏ 
=== FVQ.txt
=== AKD.txt
=== AHM.txt

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
SKT_dli_revised.txt
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
```


## [2026-09-14T02:33:20.602Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=AFM_alt=\"; sed -n '5860,5890p' AFM_alt.txt; echo \"=NYB2=\"; grep -n -i 'swsn\\|sōsan\\|sosan\\|lily' NYB_vol2_glossary.txt | head -10; echo \"=UNV=\"; grep -n -i 'swsn\\|sosan\\|sōsan\\|lily' UNV.txt | head -10"
}
```


### [2026-09-14T02:33:20.693Z] TOOL RESULT

```
=AFM_alt=

ا 


۱4 — 

ا غة في المائدة بالعر نة اما فرنكل فقال ان المادة تعريب الحشي mûed‏ 
( ا :۸۳( 

( اليزاب ) بالياء والميزاب بهمزة ساكنة القناة بحري فما اء والقى ويال 
عرز اب وصفها ابن السكمت والفراء وابو حاتم ۰ وی ات اء ل :9 
ا تقد الراء المهلة وتاخبرها ونقله الايث وجاعة ( اقرب 
اموارد ٠)‏ قات ان ازاب م رک من مز اي بول ومن آب اي ماء وساب الأسمبة 
ظاهر ( راجع ایضاً فرنکل ص :۲۹) 

RR‏ | اتب رسن ربا کن مي اي شراب اومن المويي 
سوسن ٠ ٠ ٠‏ 

( اليل ) الول الذي پککل به فارستة ممل ٠‏ وقال فرنکل ( ص )۲١۱‏ ا 
ف ع المونافي i‏ ارسي ت ا ماخوذا ع ن المونافي ا le‏ 
دور بالاراة ا ا للمسافة فهو تعريب اروی Cla 4_i, mille‏ 
بالارامىة 

3 (1 لتا ۰ عى ار ازجاح عر ت 1 نارسي مستا ور به الفرنسي e‏ 
والايطاليافي Lely smalto‏ سی ااسین AE.‏ ¿ الارای rtd‏ والارایی 
تسه مأخوذ من اليوتاني أبس( 

( المنويزج) نات له ورق سمه بورق اككرم الاري تعر لب مو یز 


باب النون 
=NYB2=
=UNV=
```


## [2026-09-14T02:33:34.436Z] TOOL CALL #41: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg465.png data/verification/sources/refs/ocr/BOOK/465.png && echo copied\nfor u in \\\n 'https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%B3%D9%86' \\\n 'https://en.wiktionary.org/wiki/Susan' \\\n 'https://en.wiktionary.org/wiki/%CF%83%CE%BF%E1%BF%A6%CF%83%CE%BF%CE%BD' \\\n 'https://en.wiktionary.org/wiki/%D7%A9%D7%95%D7%A9%D7%9F' \\\n 'https://www.etymonline.com/word/Susan' \\\n 'https://abadis.ir/fatofa/%D8%B3%D9%88%D8%B3%D9%86/' \\\n 'https://www.balashon.com/2009/03/shoshana.html' ; do\n timeout 120 python3 /home/sfmqrb/git/rishe/tools/fetch_source.py \"$u\" --note 'page 465, root Šôšen (lily/lotus): Egyptian>Semitic/Iranian chain, Susan' 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T02:33:41.019Z] TOOL RESULT

```
copied
/home/sfmqrb/git/rishe/data/verification/sources/web/14fbe49972014ea4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a887b772692f4a2a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e0702e3a26c9f450.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/199ff4b615e8cd15.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4720f5b2c222f976.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1f437a3a6f9b06a9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/95a0907081ef2c83.txt
```


## [2026-09-14T02:33:43.402Z] TOOL CALL #42: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T02:33:43.454Z] TOOL RESULT

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


## [2026-09-14T02:33:59.324Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i 'sosan\\|s.san' PHD_pages.txt | head -5; echo \"--- leaf calc\"; python3 - <<'EOF'\nt=open('PHD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'sosan' in p.lower() or 'lily' in p.lower():\n        print(i, p[:60].replace('\\n',' '))\nEOF\necho \"=FSD=\"; grep -n 'Susanna\\|Susan,' FSD_vol4.txt FSD_vol3.txt 2>/dev/null | head -6"
}
```


### [2026-09-14T02:34:00.453Z] TOOL RESULT

```
60:this'Sasanian' transcription for his journeying further. To have
102:third century of our era, the period of the rise of the Sasanian
1683:Burzenmihr [bwlcynmtr ] the third major Fire of Sasanian Eran, that
2278:Farrobll~ [plwb(')g] the first major Fire of Sasanian Eran, that of priests
2634:Gu§nasp [gwln(')sp]      the second major Fire of Sasanian Eran, that of
--- leaf calc
leaves 260
81 nihuftan                          60                        
96 se-pay                            75                        
143  122                ENGLISH-PAHLAVI INDEX  likeable passandi
160                    ENGLISH-PAHLAVI INDEX                    
236                                  !lAlILAVI KEY              
=FSD=
FSD_vol4.txt:32038:Tem'plcs  n   1   Frederick  (»Viol821-n/sl902),  an  English divine,  born  In  Santa  Maura,  Ionian  Islands  Archbishop  of Canterbury  crowned  Edward  VII  king  2   Sir  William (162S-Vt1689)  .   an  English  statesman,  diplomat,  and  writer, Miscellanea  3.  A   city  In  Bell  county,  Tex  ,   In  an  agricul- tural region  —   Char!ott3Teraple,anovelby  SusannaRow- son.relatlngthet-aglcstoryof  Charlotte  Stanley,  who  In  1774 fled  from  England  to  New  "i  ork  In  the  company  of  Colonel Montresor.w  ho  abandoned  her  She  died  at  the  age  of  19and was  burled  in  the  grav  ey  ard  of  Trinity  Church  the  Inscrip- tion on  her  tombstone  was  changed  from  Stanley  to  Temple In  1846  The  novel  was  published  in  1790 Tcra'ple  Bar.  A   historic  site  In  London,  at  the  junction of  Fleet  street  and  the  Strand,  near  the  Temple,  which marks  the  boundary  between  the  city  proper  and  \^es^- mlnster,  and  where  the  Lord  Mayor  presents  the  sovereign entering  In  state  with  the  sw  ord  of  the  city  V   irlous  struc* tures  have  marked  the  site  the  most  familiar  of  which  was the  stone  gateway,  designed  by  Sir  Christopher  Wren, erected  In  1672,  to  take  the  place  of  all  earlier  gatevTays  de- stroy cd  by  the  fire  of  1666,  upon  which  the  beads  of  exe> cuted  traitors  vrere  exposed  It  was  removed  In  1878  and reereeted  at  Waltham  Cross  In  1888 tem'plct,  1   tem'plet,  2   tSm'pISt,  tf  To  shape  or  mark the  position  of  with  a   templet tcin'plcti»  n   1.  A   pattern,  usually  fiat  and  of  wood or  metal,  adapted  to  the  purpose  of  shaping  some- thing, especially  In  profile  (1)  A   perforated  strip  serving as  a   guide  in  laying  out  riveted  work,  as  boilers  (2)  A gage  for  shaping  pottery  (3)  A   pattern  to  aid  In  turning balusters,  etc ,   to  a   uniform  size  (4)  Shtp^buildiny  A. board  cut  to  show  the  proper  curv  e   of  timbers  or  framing
FSD_vol4.txt:108687:Feast  »day  of  St.  Tlburtins,  martyr.  St.  C^at^vHle,  Pa ChroraatlDs:  St.  Susanna,  martyr.  St.  ««'
```


## [2026-09-14T02:39:17.346Z] TOOL CALL #44: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-465.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_SUSAN_FA = \"https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%B3%D9%86\"\nW_SUSAN_EN = \"https://en.wiktionary.org/wiki/Susan\"\nW_SOUSON  = \"https://en.wiktionary.org/wiki/%CF%83%CE%BF%E1%BF%A6%CF%83%CE%BF%CE%BD\"\nW_SHUSHAN = \"https://en.wiktionary.org/wiki/%D7%A9%D7%95%D7%A9%D7%9F\"\nETY       = \"https://www.etymonline.com/word/Susan\"\nABADIS    = \"https://abadis.ir/fatofa/%D8%B3%D9%88%D8%B3%D9%86/\"\nBALASHON  = \"https://www.balashon.com/2009/03/shoshana.html\"\n\nKLN_NOTE = (\"KLN_1966.txt leaf 821 (the leaf carries the printed numerals 1548/1549), s.v. \"\n            \"'Susannah, Susanna, fem. PN. — L. Susanna, fr. Gk. Sousanna, fr. Heb. shoshannah, shoshan, \"\n            \"shushan, ‘lily’; cp. Akkad. sheshanu, Aram. shushanta (whence Arm. shushan, Arab. sausan, \"\n            \"VArab. susan), ‘lily’. All these words derive fr. Egypt. s(sh)shn (Coptic shoshen), ‘lotus’. \"\n            \"Cp. Gk. souson, ‘lily’, which is a Semitic loan word.' (grep -n -i 'susan' KLN_1966.txt)\")\n\nLKT_NOTE = (\"LKT.txt leaf 183 = printed p.157, entry no. 1958: 'Ar. sūsān: ‘Lilie’ … wie hebr. sōsan \"\n            \"wahrscheinlich aus äg. s-ss-n entlehnt (ZDMG XLVI, 117), Einheitsnomen susana; hieraus mit ar. Art. \"\n            \"und Imala sp. azucena, pg. açucena ‘weiße Lilie’'.\")\n\nAFA_NOTE = (\"AFA.txt leaf 173 = printed p.143 (Fraenkel, Die aramäischen Fremdwörter im Arabischen): \"\n            \"'سوسن »Lilie« geht wohl zunächst auf aram. … zurück, nicht auf das Persische zurück' — \"\n            \"Arabic sawsan is taken from Aramaic (and Fraenkel explicitly denies a Persian source).\")\n\nPLA_NOTE = (\"incoming/PLA/PLA_pages.txt leaf 184 = printed p.169 (Asbaghi, Persische Lehnwörter im Arabischen): \"\n            \"'sūsan: ‚Lilie‘ — pers. سوسن susan, mp. sōsan (n.7 = Mackenzie s.v., Unvala s.v., Bq. S. 1188), \"\n            \"lat. sūsianus, griech. sousianos aus Susa …, syr. …, hebr. …' — Asbaghi files Arabic sūsan as a \"\n            \"loan FROM Persian/Middle Persian, i.e. the opposite of Nourai's Arabic→Pahlavi arrow.\")\n\nPHD_NOTE = (\"PHD_pages.txt leaf 96 (printed p.75, running head 'se-pay 75'): 'sōsan [swsnʼ | N ~] lily'; the \"\n            \"English–Pahlavi index (PHD.txt line 2633) has 'lily sōsan'. MP sōsan is thus a genuine Sasanian-era \"\n            \"Pahlavi word, written swsnʼ.\")\n\nMON_NOTE = (\"Mo'in's six-volume Farhang (the edition Nourai cites) is not online; checked the two-volume Adena \"\n            \"abridgement MON_part1.txt line 81246: 'سوسن: [معر.] (اِ.) (گیا.) گیاهی است از تیرة سوسنی‌ها …' and \"\n            \"abadis.ir (فرهنگ معین): '(سَ) [معر.] (اِ.) گلی است با برگ‌های دراز و باریک …'. Mo'in tags the word \"\n            \"[معر.] = muʿarrab (Arabicised), which is what Nourai turned into an Arabic→Pahlavi arrow; Mo'in gives \"\n            \"no Pahlavi form there, and Dehkhoda on the same abadis page records Pahlavi sōsan/sōsanag.\")\n\nAHD_NC = {\"ref\": \"AHD:1296\", \"status\": \"not_checked\",\n          \"note\": \"AHD p.1296 is a page of the main A–Z body of the 1975/76 New College Edition, which is \"\n                  \"lending-only on archive.org; the local proxy (AHD_watkins1985.txt) is only the Indo-European \"\n                  \"roots appendix and this word is not Indo-European, so nothing there to check.\"}\n\nentries = [{\n  \"entry\": 0,\n  \"root\": \"Šôšen\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"Egyptian zšn / sšn ‘lotus, water-lily’ (Coptic щ… ϣⲛϣⲥη šōšen)\",\n  \"note\": (\"The ultimate etymon is right: Egyptian zšn (sšn) ‘lotus, water-lily’ is the accepted source of \"\n           \"Hebrew šōšan(nā), Greek σοῦσον, Aramaic šōšantā, Arabic sawsan and Persian سوسن. But the form Nourai \"\n           \"prints as the root, Šôšen, is the COPTIC reflex (ϣωϣεν šōšen), not the hieroglyphic Egyptian form; \"\n           \"Klein, whom he cites, prints 'Egypt. s(sh)shn (Coptic shoshen)' and Nourai has promoted the \"\n           \"parenthesis to the headword. Since Coptic is the last stage of Egyptian the language label is not \"\n           \"false, but the chart implies a 2nd-millennium-BCE donor form that in fact is attested only in the \"\n           \"1st millennium CE — hence 'plausible' rather than 'confirmed'. The internal shape of the chart is \"\n           \"also looser than the sources: Hebrew, Aramaic and Akkadian are drawn as four independent branches \"\n           \"off Egyptian, whereas Klein, Fraenkel and Wiktionary route Arabic (and the Iranian forms) through \"\n           \"Aramaic/Greek.\"),\n  \"note_fa\": (\"ریشهٔ نهایی درست است: واژهٔ مصری باستان zšn/sšn «نیلوفر آبی، لوتوس» خاستگاه عبری šōšān، \"\n              \"آرامی šōšantā، یونانی souson، عربی سَوْسَن و فارسی «سوسن» شمرده می‌شود. اما صورتی که نورایی \"\n              \"در جعبهٔ ریشه آورده (Šôšen) درست صورت قبطی (قبطی: šōšen) است نه مصری هیروگلیفی؛ کلاین در ص ۱۵۴۸ \"\n              \"می‌نویسد «مصری s(sh)shn (قبطی shoshen)» و نورایی همان پرانتز را سرمدخل کرده است. افزون بر این، چهار شاخهٔ \"\n              \"عبری، آرامی، اکدی و عربی در نمودار مستقل از یکدیگر رسم شده‌اند، حال آنکه فرنکل و کلاین و ویکی‌واژه \"\n              \"عربی را از راه آرامی (یا ایرانی میانه) می‌دانند. به اختصار: ادعای نورایی در کلیات با احتیاط پذیرفتنی است.\"),\n  \"sources\": [W_SOUSON, W_SHUSHAN, W_SUSAN_FA, BALASHON],\n  \"ref_check\": [{\"ref\": \"KLN:1548\", \"status\": \"supports\", \"note\": KLN_NOTE}],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"leaf 821 = printed pp.1548–1549, s.v. Susannah\", \"stance\": \"supports\", \"note\": KLN_NOTE},\n    {\"src\": \"LKT\", \"where\": \"entry no. 1958, leaf 183 = p.157\", \"stance\": \"supports\", \"note\": LKT_NOTE},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt (IE roots appendix)\", \"stance\": \"silent\",\n     \"note\": \"grep of the local Watkins 1985 text finds no root for this word, as expected: šōšen/šūšan is Afro-Asiatic, not Indo-European.\"}\n  ],\n  \"nodes\": []\n}]\n\nN = entries[0][\"nodes\"]\n\nN.append({\n  \"id\": 1, \"lang\": \"Arabic\", \"words\": \"sausan\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"Arabic سَوْسَن sawsan (colloquial sūsan) ‘lily, iris’ is certainly a loanword and its ultimate \"\n                 \"source is the Egyptian word, so Nourai's arrow is right at the far end; the immediate donor, \"\n                 \"however, is not Egyptian. Fraenkel (p.143) derives it from Aramaic šōšantā and expressly rejects a \"\n                 \"Persian source; Klein likewise puts it under 'Aram. shushanta (whence … Arab. sausan, VArab. \"\n                 \"susan)'. Wiktionary and Asbaghi instead take Arabic sawsan from Middle Persian sōsan (itself from \"\n                 \"Greek σοῦσον). Lokotsch (no.1958) is the one source that agrees with Nourai's short-circuit: \"\n                 \"'Ar. sūsān … like Hebrew šōsan probably borrowed from Egyptian s-ss-n'. Phonetically the Arabic \"\n                 \"form shows the regular Semitic shape šōšan > sawsan with s for š and the diphthong aw of the \"\n                 \"faʿlal pattern; from it come Andalusi Arabic as-sūsana > Spanish azucena, Portuguese açucena.\"),\n  \"derivation_fa\": (\"عربی «سَوْسَن» (عامیانه sūsan) بی‌گمان وام‌واژه است و سرچشمهٔ دوردست آن همان واژهٔ مصری است؛ \"\n                    \"اما وام‌دهندهٔ مستقیم مصری نیست. فرنکل (ص ۱۴۳) آن را از آرامی šōšantā می‌گیرد و صریحاً منشأ فارسی را رد \"\n                    \"می‌کند؛ ویکی‌واژه و اصبغی برعکس، عربی را وام‌گرفته از فارسی میانهٔ sōsan می‌دانند. فقط لوکوچ (شمارهٔ ۱۹۵۸) \"\n                    \"همانند نورایی مستقیم از مصری می‌گیرد. پس ادعای نورایی در ریشهٔ دور درست و در حلقهٔ نزدیک ناقص است؛ \"\n                    \"از همین صورت عربی اندلسی as-sūsana اسپانیایی azucena پدید آمده است.\"),\n  \"sources\": [W_SUSAN_FA, BALASHON],\n  \"ref_check\": [{\"ref\": \"KLN:1548\", \"status\": \"partial\",\n                 \"note\": \"Klein has Arab. sausan / Vulgar Arab. susan on p.1548, but places it under Aramaic \"\n                         \"shushanta, not directly under Egyptian: '… cp. Akkad. sheshanu, Aram. shushanta \"\n                         \"(whence Arm. shushan, Arab. sausan, VArab. susan)'. So the page supports the word and \"\n                         \"the ultimate Egyptian origin but not the direct Egyptian→Arabic arrow.\"}],\n  \"consulted\": [\n    {\"src\": \"AFA\", \"where\": \"Fraenkel, p.143 (AFA.txt leaf 173)\", \"stance\": \"partial\", \"note\": AFA_NOTE},\n    {\"src\": \"LKT\", \"where\": \"no. 1958 = p.157\", \"stance\": \"supports\", \"note\": LKT_NOTE},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi p.169 (leaf 184)\", \"stance\": \"contradicts\", \"note\": PLA_NOTE},\n    {\"src\": \"AFM\", \"where\": \"AFM_pages.txt / AFM_alt.txt\", \"stance\": \"silent\",\n     \"note\": \"grep 'سوسن' in AFM_pages.txt returns nothing; AFM_alt.txt line 5876 has a bare 'سوسن · · ·' in a \"\n             \"running index whose surrounding Arabic OCR is unreadable, so Addi Shir could not be used.\"},\n    {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt\", \"stance\": \"silent\",\n     \"note\": \"not a Qur'anic word; grep for 'sausan/sawsan/susan' in Jeffery returns nothing.\"}\n  ]\n})\n\nN.append({\n  \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"sawsan, sŭsan\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\"Middle Persian sōsan ‘lily’ is genuine — MacKenzie p.75 has 'sōsan [swsnʼ | N ~] lily' — but it \"\n                 \"cannot come from Arabic: it is Sasanian Book Pahlavi, written swsnʼ, centuries older than any \"\n                 \"Arabic influence on Persian, and the direction of borrowing in the sources is the reverse. \"\n                 \"Asbaghi (p.169) lists Arabic sūsan as a PERSIAN loanword and cites MP sōsan (after MacKenzie, \"\n                 \"Unvala and Borhan-e Qateʿ p.1188) as its etymon; Wiktionary derives both Persian سوسن and Arabic \"\n                 \"سوسن from MP swsnʼ /sōsan/, itself borrowed from Ancient Greek σοῦσον (a Semitic–Egyptian \"\n                 \"Wanderwort), most likely in the Parthian/early Sasanian period along the same route as other \"\n                 \"Greek plant names. The first of Nourai's two forms, 'sawsan', is in fact the Arabic shape \"\n                 \"(faʿlal with aw) and is not a Pahlavi form at all; only sŭsan = sōsan is. Nourai has evidently \"\n                 \"read Mo'in's tag [معر.] '(Arabicised)' on Persian سوسن as licence for an Arabic→Pahlavi arrow.\"),\n  \"derivation_fa\": (\"فارسی میانهٔ sōsan (به خط پهلوی swsnʼ) در فرهنگ مکنزی ص ۷۵ به معنی «سوسن» آمده و واژه‌ای \"\n                    \"اصیل دورهٔ ساسانی است؛ بنابراین برگرفتن آن از عربی از نظر تاریخی ناممکن است و جهت وام‌گیری وارونه \"\n                    \"است: اصبغی (ص ۱۶۹) سوسن عربی را در شمار وام‌واژه‌های فارسی می‌آورد و ویکی‌واژه نیز فارسی نو و عربی را \"\n                    \"هر دو از پهلوی sōsan می‌داند، و آن را وام‌گرفته از یونانی souson. نکتهٔ دیگر آنکه صورت «sawsan» اصلاً \"\n                    \"صورت عربی (بر وزن فَعْلَل) است نه پهلوی. پژوهش امروزی این پیکان را رد می‌کند.\"),\n  \"sources\": [W_SUSAN_FA, ABADIS],\n  \"ref_check\": [{\"ref\": \"MON:1954\", \"status\": \"partial\", \"note\": MON_NOTE}],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p.75 (PHD_pages.txt leaf 96)\", \"stance\": \"partial\", \"note\": PHD_NOTE},\n    {\"src\": \"NYB\", \"where\": \"NYB.txt / NYB_vol2_glossary.txt\", \"stance\": \"silent\",\n     \"note\": \"grep -i 'swsn|sosan|sōsan|lily' in both Nyberg files returns nothing; the OCR of the glossary \"\n             \"volume does not yield the entry, although Asbaghi p.169 n.7 cites 'Nyberg Bd. II s.v.' for MP sōsan.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi p.169\", \"stance\": \"contradicts\", \"note\": PLA_NOTE},\n    {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt, leaves 656–657 (the سو- range, around printed p.1188)\", \"stance\": \"silent\",\n     \"note\": \"The scanned OCR of Borhan vol. 2 in the سوسن range is too degraded to isolate the headword \"\n             \"(only fragments such as 'سومنات', 'سومندر' are legible) and no page image of vols 1–2 is available \"\n             \"to ref_page.py ('no scan of BQT covers printed page 1188'); Asbaghi p.169 n.7 reports Borhan \"\n             \"p.1188 as giving MP sōsan.\"}\n  ]\n})\n\nN.append({\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"sŭsan\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"New Persian سوسن susan ‘lily, iris’ continues Middle Persian sōsan without change beyond the \"\n                 \"regular MP ō > NP ū/u of the first syllable (MacKenzie marks the New Persian reflex simply as \"\n                 \"'N ~'), so the Pahlavi→Persian arrow itself is correct even though the Arabic→Pahlavi arrow \"\n                 \"above it is not. The word is well attested in classical poetry — Hāfez's line quoted in the box, \"\n                 \"'بسان سوسن اگر ده زبان شود حافظ', plays on the epithet سوسن ده‌زبان 'the ten-tongued lily'. \"\n                 \"Mo'in's own entry, which Nourai cites, tags the word [معر.] (Arabicised) rather than [په.], \"\n                 \"while Dehkhoda records Pahlavi sōsan/sōsanag; the modern consensus (Wiktionary, Asbaghi) is the \"\n                 \"inherited Middle Persian line, with Arabic sawsan as the borrower, not the lender.\"),\n  \"derivation_fa\": (\"«سوسن» فارسی نو دنبالهٔ مستقیم فارسی میانهٔ sōsan است؛ تنها دگرگونی آوایی، تبدیل معمول ō ی پهلوی به u \"\n                    \"در فارسی دری است؛ مکنزی صورت فارسی نو را با علامت «N ~» همان sōsan می‌آورد. بیت حافظ در جعبه به لقب \"\n                    \"«سوسن ده‌زبان» اشاره دارد. معین خود این واژه را [معر.] نشان کرده و دهخدا صورت پهلوی sōsan/sōsanag را \"\n                    \"می‌آورد؛ این حلقهٔ پهلوی ← فارسی درست است.\"),\n  \"sources\": [W_SUSAN_FA, ABADIS],\n  \"ref_check\": [{\"ref\": \"MON:1954\", \"status\": \"supports\", \"note\": MON_NOTE}],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"فرهنگ معین s.v. سوسن (abadis.ir; 2-vol Adena abridgement MON_part1.txt line 81246)\",\n     \"stance\": \"partial\", \"note\": MON_NOTE},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p.75\", \"stance\": \"supports\", \"note\": PHD_NOTE},\n    {\"src\": \"HRN\", \"where\": \"HRN.txt (Horn, Grundriss)\", \"stance\": \"silent\",\n     \"note\": \"grep -i 'sausan|sawsan|susan|sosan' in HRN.txt returns nothing; Horn has no article on سوسن.\"},\n    {\"src\": \"HUB\", \"where\": \"HUB.txt (Hübschmann, Persische Studien)\", \"stance\": \"silent\",\n     \"note\": \"same grep returns nothing; Hübschmann does not treat the word.\"},\n    {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n     \"note\": \"grep 'سوسن' finds no headword — expected, since Aryanpur's dictionary covers only Indo-European roots.\"}\n  ]\n})\n\nN.append({\n  \"id\": 4, \"lang\": \"Hebrew\", \"words\": \"šôšannah\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Biblical Hebrew שׁוֹשַׁנָּה šōšannā (absolute שׁוֹשָׁן šōšān) ‘lily’ (Song of Songs 2:1, 1 Kings 7:19 of the \"\n                 \"lily-work on the capitals of Jachin and Boaz) is the standard Semitic reflex of Egyptian zšn, \"\n                 \"with the Egyptian s rendered by š and the feminine ending -ā added (šōšan + -nā with reduplication \"\n                 \"of the n). Wiktionary and Klein both give the Egyptian source directly; the competing native \"\n                 \"derivation from šēš ‘six’ (Ibn Ezra, because the flower has six petals) is a medieval folk \"\n                 \"etymology and is not accepted today.\"),\n  \"derivation_fa\": (\"عبری کتاب مقدس šōšannā (صورت مطلق šōšān) «سوسن» — در غزل غزل‌ها ۲:۱ و در وصف سرستون‌های \"\n                    \"هیکل سلیمان — بازتاب معمول سامی واژهٔ مصری zšn است: s مصری به š بدل شده و پسوند مؤنث -ā افزوده شده است. \"\n                    \"ریشه‌شناسی عامیانهٔ قدیمی (پیوند با šēš «شش» به سبب شش گلبرگ) پذیرفتنی نیست. ادعای نورایی درست است.\"),\n  \"sources\": [W_SHUSHAN, BALASHON],\n  \"ref_check\": [{\"ref\": \"KLN:1548\", \"status\": \"supports\",\n                 \"note\": \"Klein p.1548: 'fr. Heb. shoshannah, shoshan, shushan, ‘lily’ … All these words derive \"\n                         \"fr. Egypt. s(sh)shn (Coptic shoshen), ‘lotus’.' — exactly Nourai's arrow.\"}],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"leaf 821 = p.1548 s.v. Susannah\", \"stance\": \"supports\", \"note\": KLN_NOTE},\n    {\"src\": \"LKT\", \"where\": \"no. 1958 = p.157\", \"stance\": \"supports\",\n     \"note\": \"'wie hebr. sōsan wahrscheinlich aus äg. s-ss-n entlehnt (ZDMG XLVI, 117)' — Lokotsch derives the \"\n             \"Hebrew word from Egyptian just as Nourai does.\"},\n    {\"src\": \"AFA\", \"where\": \"Fraenkel p.143\", \"stance\": \"partial\", \"note\": AFA_NOTE}\n  ]\n})\n\nN.append({\n  \"id\": 5, \"lang\": \"Greek\", \"words\": \"sousanna\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Greek Σουσάννα Sousánna is the Septuagint/New Testament transcription of Hebrew šōšannā as a \"\n                 \"woman's name: it is the heroine of the deuterocanonical Susanna (Daniel 13, Theodotion/LXX) and \"\n                 \"one of the women who followed Jesus in Luke 8:3. Greek ou renders the Hebrew long ō/ū and the \"\n                 \"geminate -nn- is kept; the final -a is the Greek feminine ending substituting for the Hebrew -ā. \"\n                 \"The common noun σοῦσον 'lily' (Hippocrates, Theophrastus) is a separate, earlier borrowing of the \"\n                 \"same Egyptian word, as Klein and Beekes (2010) note.\"),\n  \"derivation_fa\": (\"یونانی Σουσάννα آوانویسی نام عبری šōšannā در ترجمهٔ سبعینیه و عهد جدید است (داستان سوسن در \"\n                    \"باب ۱۳ دانیال؛ لوقا ۸:۳). در این وام‌گیری ou یونانی برابر ō/ū عبری است و پایانهٔ -a نشانهٔ مؤنث \"\n                    \"یونانی است. نام عام σοῦσον «سوسن» وام‌گیری جداگانه و کهن‌تری از همان واژهٔ مصری است. \"\n                    \"ادعای نورایی درست است.\"),\n  \"sources\": [W_SUSAN_EN, W_SOUSON, ETY],\n  \"ref_check\": [{\"ref\": \"KLN:1548\", \"status\": \"supports\",\n                 \"note\": \"Klein p.1548: 'L. Susanna, fr. Gk. Sousanna, fr. Heb. shoshannah' — the Hebrew→Greek \"\n                         \"step is exactly as drawn.\"}],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"leaf 821 = p.1548\", \"stance\": \"supports\", \"note\": KLN_NOTE},\n    {\"src\": \"WLD\", \"where\": \"WLD_band3.txt (Walde-Pokorny register)\", \"stance\": \"silent\",\n     \"note\": \"no entry, as expected: σοῦσον is a Semitic/Egyptian loan, not inherited Indo-European; Beekes \"\n             \"(cited on the Wiktionary page for σοῦσον) says the same.\"}\n  ]\n})\n\nN.append({\n  \"id\": 6, \"lang\": \"Late Latin\", \"words\": \"sausanna\",\n  \"verdict\": \"transcription_suspect\",\n  \"error_in\": \"book\",\n  \"book_prints\": \"sausanna\",\n  \"correct_form\": \"Susanna\",\n  \"derivation\": (\"The Late Latin form is Susanna — the name of the Vulgate's Susanna (Dan. 13) and of the Roman \"\n                 \"martyr St Susanna — taken over unchanged from Greek Σουσάννα with ou > u. The book prints \"\n                 \"'sausanna', which is not an attested Latin form; it looks like a contamination from the Arabic \"\n                 \"'sausan' printed two boxes above. Klein, the reference cited on this very box, has 'L. Susanna', \"\n                 \"and so do Etymonline and Wiktionary. The page image (data/verification/sources/refs/ocr/BOOK/465.png) \"\n                 \"shows 'sausanna' in the Late Latin box, so the extraction is faithful and the error is Nourai's.\"),\n  \"derivation_fa\": (\"صورت درست لاتینی متأخر Susanna است (نام سوسن در وولگاتا و نام قدیسهٔ رومی)، که بی‌تغییر از \"\n                    \"یونانی Σουσάννα گرفته شده است. آنچه در کتاب چاپ شده («sausanna») صورتی لاتینی نیست و ظاهراً از \"\n                    \"روی «sausan» عربی دو جعبه بالاتر به این خانه راه یافته است؛ کلاین در همان صفحهٔ ۱۵۴۸ «L. Susanna» دارد. \"\n                    \"تصویر صفحه نشان می‌دهد خوانش اسکن درست بوده و خطا از خود کتاب است (خطای چاپی کتاب).\"),\n  \"sources\": [W_SUSAN_EN, ETY],\n  \"ref_check\": [\n    {\"ref\": \"KLN:1548\", \"status\": \"contradicts\",\n     \"note\": \"Klein p.1548 prints 'L. Susanna', not 'sausanna'; the cited page therefore contradicts the form in \"\n             \"the box (though it supports the Greek→Latin step itself).\"},\n    AHD_NC\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"leaf 821 = p.1548\", \"stance\": \"partial\", \"note\": KLN_NOTE},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt (Skeat, Concise)\", \"stance\": \"silent\",\n     \"note\": \"grep 'Susan' returns only an unrelated OCR artefact ('lilierly'); Skeat's concise dictionary has no \"\n             \"article on the personal name.\"},\n    {\"src\": \"FSD\", \"where\": \"FSD_vol4.txt\", \"stance\": \"silent\",\n     \"note\": \"Funk & Wagnalls has 'Susanna Rowson' and 'St. Susanna' in the biographical/calendar matter only, no \"\n             \"etymological article; nothing on a form 'sausanna'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 7, \"lang\": \"English\", \"words\": \"Susan\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"English Susan is the short form of Susanna(h), current since the Middle Ages; Etymonline routes it \"\n                 \"'from French Susanne, from Late Latin Susanna, from Greek Sousanna, from Hebrew Shoshannah, \"\n                 \"literally ‘a lily’', so the immediate donor is Old French rather than Latin directly — the one \"\n                 \"simplification in Nourai's box. The loss of the final syllable is the usual English hypocoristic \"\n                 \"shortening (cp. Sue, Sukey, Suzy). The name peaked in the United States in 1957–1960 at no. 2.\"),\n  \"derivation_fa\": (\"«Susan» انگلیسی کوتاه‌شدهٔ Susanna است و از سده‌های میانه رایج بوده است؛ اتیمانلاین مسیر را \"\n                    \"فرانسهٔ کهن Susanne ← لاتینی متأخر Susanna ← یونانی Sousanna ← عبری šōšannā می‌داند؛ \"\n                    \"نورایی حلقهٔ فرانسه را حذف کرده ولی زنجیره درست است. کوتاه‌شدن هجای پایانی همان روند معمول \"\n                    \"نام‌کوتاه‌سازی انگلیسی است (Sue، Sukey).\"),\n  \"sources\": [ETY, W_SUSAN_EN],\n  \"ref_check\": [\n    {\"ref\": \"KLN:1548\", \"status\": \"supports\",\n     \"note\": \"Klein p.1548 s.v. 'Susannah, Susanna, fem. PN.' gives the whole Latin–Greek–Hebrew chain for the \"\n             \"English name; Klein's separate entry 'sukey, n., tea kettle. — From Sukey, pet form of Susan' \"\n             \"(KLN_1971.txt line 236447) shows he treats Susan as the English short form.\"},\n    AHD_NC\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"leaf 821 = p.1548\", \"stance\": \"supports\", \"note\": KLN_NOTE},\n    {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt (Webster's New Twentieth Century, vol. 1 A–?)\", \"stance\": \"silent\",\n     \"note\": \"only volume 1 of Webster's is available locally, so the letter S could not be checked.\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt\", \"stance\": \"silent\", \"note\": \"Skeat has no entry for the personal name.\"}\n  ]\n})\n\nN.append({\n  \"id\": 8, \"lang\": \"Akkadian\", \"words\": \"šĕšanu\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"The form is Klein's: 'cp. Akkad. sheshanu' (p.1548), i.e. šeššānu/šūšānu ‘lily’, a Late-Babylonian \"\n                 \"word generally taken (after Zimmern, Akkadische Fremdwörter, 1915) as one of the isolated \"\n                 \"Egyptian loans in Neo-Assyrian/Neo-Babylonian, borrowed with the Egyptian s rendered š and an \"\n                 \"Akkadian nominative -u added. So Nourai's Egyptian→Akkadian arrow reproduces Klein faithfully and \"\n                 \"is compatible with the standard view. It is marked plausible rather than confirmed because the \"\n                 \"Chicago Assyrian Dictionary could not be consulted (no open copy of the Š volumes was reachable) \"\n                 \"and the vocalisation šĕšanu with a short e is Klein's transcription, not a normalised Assyriological \"\n                 \"citation form; Wiktionary's Arabic entry cites Zimmern for the Akkadian evidence but gives no headword.\"),\n  \"derivation_fa\": (\"صورت اکدیٔ یادشده همان است که کلاین در ص ۱۵۴۸ می‌آورد («Akkad. sheshanu»)؛ به تعبیر رایج، \"\n                    \"زیمرن (۱۹۱۵) آن را از وام‌واژه‌های مصری در اکدی متأخر می‌شمارد: s مصری به š بدل شده و پایانهٔ \"\n                    \"نشانهٔ فاعلی -u اکدی افزوده شده است. چون فرهنگ آشوری شیکاگو (CAD) در دسترس نبود، این حلقه با \"\n                    \"احتیاط پذیرفتنی است.\"),\n  \"sources\": [BALASHON, W_SUSAN_FA],\n  \"ref_check\": [{\"ref\": \"KLN:1548\", \"status\": \"supports\",\n                 \"note\": \"Klein p.1548: 'cp. Akkad. sheshanu … All these words derive fr. Egypt. s(sh)shn' — the \"\n                         \"form and the Egyptian source are both Klein's.\"}],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"leaf 821 = p.1548\", \"stance\": \"supports\", \"note\": KLN_NOTE},\n    {\"src\": \"LKT\", \"where\": \"no. 1957 (Ar. sūs) and no. 1958, p.157\", \"stance\": \"partial\",\n     \"note\": \"Lokotsch cites Assyrian only for the homonym sūs 'liquorice' ('aus aram. sūšā < ass. sūsu, \"\n             \"ZAkkFW 58'); for the lily (no. 1958) he names only Hebrew and Egyptian, so the Akkadian lily word \"\n             \"is not corroborated there.\"},\n    {\"src\": \"AFA\", \"where\": \"Fraenkel p.143\", \"stance\": \"silent\",\n     \"note\": \"Fraenkel discusses only the Aramaic source of Arabic sawsan and does not mention Akkadian.\"}\n  ]\n})\n\nN.append({\n  \"id\": 9, \"lang\": \"Aramaic\", \"words\": \"šušan\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"Aramaic/Syriac for the lily is šōšantā / šūšantā (שׁוֹשַׁנְתָּא, Syriac ܔܘܫܢܬܐ), with the \"\n                 \"-tā of the emphatic feminine singulative; Klein's page, which Nourai cites, prints exactly \"\n                 \"'Aram. shushanta'. The bare 'šušan' of the chart is the underlying stem rather than an attested \"\n                 \"Aramaic citation form (Hebrew šūšan is the form with that shape). The Egyptian origin and the \"\n                 \"position of Aramaic in the chain are right — indeed Fraenkel (p.143) and Klein make Aramaic the \"\n                 \"donor of Arabic sawsan, a step Nourai's chart omits — so the node is plausible rather than \"\n                 \"confirmed, the quibble being the form, not the etymology.\"),\n  \"derivation_fa\": (\"صورت رایج آرامی/سریانی šōšantā (با پسوند مؤنث معرفهٔ -tā) است و خود کلاین در ص ۱۵۴۸ \"\n                    \"همین «shushanta» را می‌آورد؛ صورت بدون پسوند که نورایی آورده ستاک است نه صورت مضبوط آرامی. \"\n                    \"از سوی دیگر، فرنکل و کلاین همین صورت آرامی را وام‌دهندهٔ «سوسن» عربی می‌دانند، حلقه‌ای که در \"\n                    \"نمودار نیامده است. ادعای نورایی با احتیاط پذیرفتنی است.\"),\n  \"sources\": [W_SUSAN_FA, BALASHON],\n  \"ref_check\": [{\"ref\": \"KLN:1548\", \"status\": \"partial\",\n                 \"note\": \"Klein p.1548 has 'Aram. shushanta', not 'shushan'; the etymology (Egyptian source) is \"\n                         \"as Nourai draws it, the form is not.\"}],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"leaf 821 = p.1548\", \"stance\": \"partial\", \"note\": KLN_NOTE},\n    {\"src\": \"AFA\", \"where\": \"Fraenkel p.143 (AFA.txt leaf 173)\", \"stance\": \"supports\", \"note\": AFA_NOTE},\n    {\"src\": \"LKT\", \"where\": \"no. 1958, p.157\", \"stance\": \"silent\",\n     \"note\": \"Lokotsch names only Hebrew and Egyptian for the lily word; no Aramaic form given.\"}\n  ]\n})\n\nout = {\n  \"pdf_page\": 465,\n  \"book_page\": 435,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": entries\n}\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-465.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-465.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-465.json > /dev/null && echo \"valid json\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 465"
}
```


### [2026-09-14T02:39:18.798Z] TOOL RESULT

```
written
valid json
nodes verified: 9/9
node verdicts: {'plausible': 3, 'disputed': 1, 'confirmed': 4, 'transcription_suspect': 1}
root verdicts: {'plausible': 1}
ref checks: {'partial': 3, 'supports': 5, 'contradicts': 1, 'not_checked': 2}
books consulted: {'partial': 7, 'supports': 8, 'contradicts': 2, 'silent': 14} | by book: {'KLN': 6, 'AFA': 4, 'LKT': 4, 'PLA': 2, 'PHD': 2, 'SKT': 2, 'AFM': 1, 'FVQ': 1, 'NYB': 1, 'BQT': 1, 'MON': 1, 'HRN': 1, 'HUB': 1, 'ARY': 1, 'WLD': 1, 'FSD': 1, 'WEB': 1}
```


## [2026-09-14T02:39:26.891Z] TOOL CALL #45: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-465.json'\nd=json.load(open(p,encoding='utf-8'))\nd['entries'][0]['modern_form']=\"Egyptian zšn / sšn 'lotus, water-lily' (Coptic ϣⲱϣⲉⲛ šōšen)\"\ne=d['entries'][0]\nfor n in e['nodes']:\n    n['derivation_fa']=n['derivation_fa'].replace('ܔܘܫܢܬܐ','ܫܘܫܢܬܐ')\n    n['derivation']=n['derivation'].replace('ܔܘܫܢܬܐ','ܫܘܫܢܬܐ')\nio.open(p,'w',encoding='utf-8').write(json.dumps(d,ensure_ascii=False,indent=2)+'\\n')\nprint(d['entries'][0]['modern_form'])\nEOF\npython3 tools/verify_check.py 465"
}
```


### [2026-09-14T02:39:28.399Z] TOOL RESULT

```
Egyptian zšn / sšn 'lotus, water-lily' (Coptic ϣⲱϣⲉⲛ šōšen)
nodes verified: 9/9
node verdicts: {'plausible': 3, 'disputed': 1, 'confirmed': 4, 'transcription_suspect': 1}
root verdicts: {'plausible': 1}
ref checks: {'partial': 3, 'supports': 5, 'contradicts': 1, 'not_checked': 2}
books consulted: {'partial': 7, 'supports': 8, 'contradicts': 2, 'silent': 14} | by book: {'KLN': 6, 'AFA': 4, 'LKT': 4, 'PLA': 2, 'PHD': 2, 'SKT': 2, 'AFM': 1, 'FVQ': 1, 'NYB': 1, 'BQT': 1, 'MON': 1, 'HRN': 1, 'HUB': 1, 'ARY': 1, 'WLD': 1, 'FSD': 1, 'WEB': 1}
```


## [2026-09-14T02:39:42.225Z] AGENT

Page 465 (book p. 435) verified — 1 entry, 9 nodes, `verify_check.py 465` shows 0 PROBLEM lines.

Verdicts: root plausible; nodes 4 confirmed, 3 plausible, 1 disputed, 1 transcription_suspect.

- **disputed — #2 Pahlavi `sawsan, sŭsan` ← Arabic**: MP sōsan is genuine Sasanian Pahlavi (MacKenzie p.75 `sōsan [swsn' | N ~] lily`), so it cannot descend from Arabic. Asbaghi p.169 files Arabic sūsan as a *Persian* loanword citing MP sōsan; Wiktionary derives both NP and Arabic from MP sōsan ← Greek σοῦσον. Nourai appears to have turned Mo'in's tag [معر.] into an Arabic→Pahlavi arrow. Also "sawsan" is the Arabic shape, not a Pahlavi form.
- **transcription_suspect — #6 Late Latin `sausanna`**: correct form is Latin *Susanna*; Klein (the cited page 1548) prints "L. Susanna". `error_in: book` — the page image confirms the book itself prints "sausanna" (probably contaminated by Arabic "sausan" two boxes above). Page PNG copied to `data/verification/sources/refs/ocr/BOOK/465.png`.
- Plausible: root (Nourai's "Šôšen" is the *Coptic* reflex promoted to an Egyptian headword; real Egyptian etymon zšn/sšn); #1 Arabic (ultimate Egyptian source right, but Fraenkel p.143 and Klein route it via Aramaic, and Fraenkel explicitly denies a Persian source); #8 Akkadian (Klein's "sheshanu"; CAD not reachable); #9 Aramaic (Klein prints *shushanta*, not bare "šušan").

Ref checks: KLN:1548 verified exactly (KLN_1966.txt leaf 821 carries the printed numerals 1548/1549, s.v. "Susannah, Susanna") — supports the Hebrew/Greek/English chain, contradicts the Late Latin form, only partial for Arabic/Aramaic. MON:1954 not checkable directly (6-vol Mo'in not online); substituted abadis.ir Mo'in entry + 2-vol abridgement. AHD:1296 not_checked (main-body page of the 1976 New College Edition, lending-only; the word is non-IE so the local Watkins appendix is irrelevant).

No extraction errors: the JSON matches the printed page exactly. 7 web pages archived via fetch_source.py.
