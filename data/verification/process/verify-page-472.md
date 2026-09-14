# Verification process log — verify-page-472


## [2026-09-14T02:28:04.583Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 472 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-472.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-472.json. Write /home/sfmqrb/git/rishe/data/verification/page-472.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 472` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:28:05.539Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:28:06.246Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:28:06.260Z] TOOL RESULT

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


## [2026-09-14T02:28:06.756Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-472.txt"
}
```


### [2026-09-14T02:28:06.779Z] TOOL RESULT

```
1	=== PDF page 472 (book page 442) ===
2	--- entry 0 ---
3	ROOT [Arabic] Š.r.b : to drink  (refs FVA:208)
4	#1 (parent #0) [Arabic] refs=FVA:208 | šarâb : a drink
5	  #2 (parent #1) [Persian] refs=MON; FVA:208 | šarâb «شراب» : wine ; šarbat «شربت» : sherbet | extra: مشروب ، شُرب
6	    #3 (parent #2) [Turkish] refs=None | 
7	      #4 (parent #3) [English] refs=KLN:1434 | sherbet
8	#5 (parent #0) [Latin] refs=KLN:1450 | siripus : a drink
9	  #6 (parent #5) [French] refs=None | 
10	    #7 (parent #6) [English] refs=None | syrup
11	--- entry 1 ---
12	ROOT Srěm -> redirect to Ser 1
13	--- entry 2 ---
14	ROOT [Indo-European] Srěno : thigh, hip  (refs POK:1002)
15	#1 (parent #0) [Avestan] refs=POK:1002 | râna 2 : thigh
16	  #2 (parent #1) [Persian] refs=BQT:932; HRN:135 | rân «ران» : thigh
17	  #3 (parent #1) [Sogdian] refs=SOD:339 | r`n` : belt
18	--- entry 3 ---
19	ROOT [Indo-European] Sresk : to drip  (refs POK:1002)
20	#1 (parent #0) [Avestan] refs=POK:1002 | srask : tear drop
21	  #2 (parent #1) [Pahlavi] refs=BQT:1124; SNS:183 | srešk : drop
22	    #3 (parent #2) [Persian] refs=POK:1002; BQT:1124 | serešk «سرشک» : tear drop
23	--- entry 4 ---
24	ROOT Sreu -> redirect to Ser 1
25	
```


## [2026-09-14T02:28:09.833Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-472.json | head -200",
 "description": "Read source JSON for page 472"
}
```


## [2026-09-14T02:28:10.519Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T02:28:10.868Z] TOOL RESULT

```
{
    "pdf_page": 472,
    "book_page": 442,
    "entries": [
        {
            "root": {
                "name": "\u0160.r.b",
                "lang": "Arabic",
                "refs": "FVA:208",
                "gloss": "to drink"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Arabic",
                    "refs": "FVA:208",
                    "words": [
                        {
                            "translit": "\u0161ar\u00e2b",
                            "gloss": "a drink",
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
                    "refs": "MON; FVA:208",
                    "words": [
                        {
                            "translit": "\u0161ar\u00e2b",
                            "gloss": "wine",
                            "script": "\u0634\u0631\u0627\u0628"
                        },
                        {
                            "translit": "\u0161arbat",
                            "gloss": "sherbet",
                            "script": "\u0634\u0631\u0628\u062a"
                        }
                    ],
                    "script_extra": "\u0645\u0634\u0631\u0648\u0628 \u060c \u0634\u064f\u0631\u0628",
                    "note": null,
                    "quote": {
                        "text": "\u0633\u0627\u0642\u06cc \u0627\u0631 \u0628\u0627\u062f\u0647 \u0627\u0632 \u0627\u06cc\u0646 \u062f\u0633\u062a \u0628\u062c\u0627\u0645 \u0627\u0646\u062f\u0627\u0632\u062f - \u0639\u0627\u0631\u0641\u0627\u0646 \u0631\u0627 \u0647\u0645\u0647 \u062f\u0631 \u0634\u064f\u0631\u0628 \u0645\u062f\u0627\u0645 \u0627\u0646\u062f\u0627\u0632\u062f",
                        "poet": "H\u00e2fez"
                    }
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Turkish",
                    "refs": null,
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "English",
                    "refs": "KLN:1434",
                    "words": [
                        {
                            "translit": "sherbet",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "KLN:1450",
                    "words": [
                        {
                            "translit": "siripus",
                            "gloss": "a drink",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 5,
                    "lang": "French",
                    "refs": null,
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "syrup",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Sr\u011bm",
                "redirect": "Ser 1"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Sr\u011bno",
                "lang": "Indo-European",
                "refs": "POK:1002",
                "gloss": "thigh, hip"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:1002",
                    "words": [
                        {
                            "translit": "r\u00e2na 2",
                            "gloss": "thigh",
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
                    "refs": "BQT:932; HRN:135",
                    "words": [
                        {
                            "translit": "r\u00e2n",
                            "gloss": "thigh",
                            "script": "\u0631\u0627\u0646"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 1,
                    "lang": "Sogdian",
                    "refs": "SOD:339",
                    "words": [
                        {
                            "translit": "r`n`",
                            "gloss": "belt",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Sresk",
                "lang": "Indo-European",
                "refs": "POK:1002",
                "gloss": "to drip"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:1002",
```


### [2026-09-14T02:28:10.906Z] TOOL RESULT

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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
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


## [2026-09-14T02:28:18.991Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-472.json'))\nprint(json.dumps(d['entries'][3],ensure_ascii=False,indent=1))\nprint(json.dumps(d['entries'][4] if len(d['entries'])>4 else None,ensure_ascii=False,indent=1))\n\"",
 "description": "Read entries 3 and 4"
}
```


### [2026-09-14T02:28:20.107Z] TOOL RESULT

```
{
 "root": {
  "name": "Sresk",
  "lang": "Indo-European",
  "refs": "POK:1002",
  "gloss": "to drip"
 },
 "nodes": [
  {
   "id": 1,
   "parent": 0,
   "lang": "Avestan",
   "refs": "POK:1002",
   "words": [
    {
     "translit": "srask",
     "gloss": "tear drop",
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
   "lang": "Pahlavi",
   "refs": "BQT:1124; SNS:183",
   "words": [
    {
     "translit": "srešk",
     "gloss": "drop",
     "script": null
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  },
  {
   "id": 3,
   "parent": 2,
   "lang": "Persian",
   "refs": "POK:1002; BQT:1124",
   "words": [
    {
     "translit": "serešk",
     "gloss": "tear drop",
     "script": "سرشک"
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": {
    "text": "دور از رخ تو دمبدم از گوشهٔ چشمم - سیلاب سرشک آمد و طوفان بلا رفت",
    "poet": "Hâfez"
   }
  }
 ]
}
{
 "root": {
  "name": "Sreu",
  "redirect": "Ser 1"
 },
 "nodes": []
}
```


## [2026-09-14T02:28:20.795Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['FVA','FVQ','POK','KLN','MON','BQT','HRN','SOD','SNS']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]); print()\n\"",
 "description": "Check refs_online entries"
}
```


### [2026-09-14T02:28:21.917Z] TOOL RESULT

```
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt
```


## [2026-09-14T02:28:28.102Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"sresk\\|srē̆n\\|sreno\\|srasča\\|sraska\" POK_full.txt POK_01.txt POK_02.txt POK_03.txt | head -40",
 "description": "Grep Pokorny for sresk and sreno"
}
```


### [2026-09-14T02:28:28.163Z] TOOL RESULT

```
POK_03.txt:2619:WP.  II  602  f.,  705;  vgl.  auch  sresk-  ,tropfen'?
POK_03.txt:3324:sreno-,  -ä  Körperteilbenennung,  etwa  ,Oberschenkel,  Lenden'.
POK_03.txt:3326:sresk'  ,tropfen'V
POK_03.txt:3327:Av.  srask-  (srasca-)  ,triefen,  abtriefen  von ;  triefregnen',  sraska-  m.  (i sirisk)    ,Träne,  Weinen',    mp.    srixt   ,dropped',    arm.    srskel   {^srSsh- srösk-)  , besprengen' ;  Entlehnung  des  arm.  Wortes  aus  dem  Arischen die  Vorbedingung    für    die   Verbindung    von   av.    srask-,    arm.   srskti *klkk-skö-    mit   lit.    släkas    ,Tropfen',    §laketi    ,tröpfeln',    §lUti  ,spriti6S*i (s.  oben  S.  607  hleu-  ,spülen').  *  ■-
POK_full.txt:77845:See also: compare also sresk- "drip'? 
POK_full.txt:80836:Root / lemma: sresk- 
POK_full.txt:80839:Material: Avestan srask- {srasca-) "triefen, abtriefen from; triefregnen', sraska-m. (np. 
POK_full.txt:80840:sirisk) "tears, Weinen', mp. s/va-/ "dropped', Armenian srskel {* sresk- or srosk-) "sprinkle'; 
POK_full.txt:80924:Root / lemma: sreno- -a
```


## [2026-09-14T02:28:29.115Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1002\" POK_full.txt | head -20; echo ---; grep -c \"\" POK_full.txt",
 "description": "Check POK_full structure"
}
```


### [2026-09-14T02:28:29.212Z] TOOL RESULT

```
80804:Page(s): 1001-1002 
---
93771
```


## [2026-09-14T02:28:31.451Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '80830,80960p' POK_full.txt",
 "description": "Read Pokorny sresk- and sreno- entries"
}
```


### [2026-09-14T02:28:31.511Z] TOOL RESULT

```
"nostril, nose' out of it borrowed or under Indo Germanic *srungh-\N\Vc\ it common origin 
sei, is doubtful. 

References: WP. II 705. 
Page(s): 1 002 

Root / lemma: sresk- 
Meaning: to drizzle 

Material: Avestan srask- {srasca-) "triefen, abtriefen from; triefregnen', sraska-m. (np. 
sirisk) "tears, Weinen', mp. s/va-/ "dropped', Armenian srskel {* sresk- or srosk-) "sprinkle'; 
borrowing of Armenian words from dem Aryan would be die Vorbedingung for die 
connection from Avestan srask-, Armenian srskel as *k/ek-skd- \N'\t\r\ Lithuanian slakas 
"drip', s/aket/^dnp, trickle', s/eM "spray' (see above S. 607 k/eu-^ rinse '). 
References: WP. II 602 f., 705. 
Page(s): 1 002 

Root / lemma: sreup- 

Meaning: scabby, dirt 

Material: Gr. purroc; m. "smut, Unreinlichkeit', purrou), punaivw "sully', punapoq "dirty, 

filthy', punau) "bin dirty, filthy', puno(; n. "wheys', punraj "clean', Med. "wash myself, 

schneuze myself; proto Slavic. *strup-b (from *sreupos or *sroupos) "wound' (Old Church 

Slavic; actually "*scurf, scab auf the wound'), " poison, pus' (slov.), "scurf, scab' (New 

Bulgarian russ.), "skin rash by children' (Serbo-Croatian), " crust, scab, eschar ' (poln. 

Czech); ablaut. Church Slavic strbp-bth "roughness, hardness '. 

References: WP. II 703, Vasmer 3, 32. 

Page(s): 1 004 

Root / lemma: sreu- 

Meaning: to flow 

Material: Old Indie sravati^ flows ' (= gr. psw), srava-m. "das Flieften' (= gr. pooc;. Old 

Church Slavic o-sfrovb), g/r/srava ^Bergstrom' (= gr. por), Lithuanian srava), sm/^- flowing, 



geflossen' (= gr. puT6(; = fern. Lithuanian srutsr, zero grade Latvian strauts), srutf-i. "way, 
das Flieften' (= gr. puai(;, perhaps Armenianan/), sravat- f. 'river' (= gr. -pEFsT-nO. O'd 
Indie srotahu.. Old pers. rautah-v\., npers. rdd^nvef; causative s/'si/aya//" makes flow', 
srava-vn. " effluence '; 

Avestan (ravan-), Gen. PI. raon^m'the FliJsse', urvant- {sru-vant-) " flowing '; from 
einemo(/7)-present from (: gr. pu9-pi6(;?): Avestan raodaiti^ flows ', rao5ah-v\. "river', urud\. 
" river flow, bed' (Old Indie visruh-i. "stream' or likewise?); 

Armenian aroganem, oroganem^ wet ' {*srou-), compare Old Lithuanian srav/nu^make 
bluten'), probably also an/ "canal' {*srut/s or *sruios)\ 

gr. p£U) "flow' (Put. p£uoo|jai, Aor. Epidaur. s^sppua, Kalymna £[Y]-pug Konj. from 
*sruua-\ compare Lithuanian pasruvo "floft' from -at, usually *sreue- in sppunv, Lithuanian 
sravetr, to this beiden heavy base Old Indie Inf. sravitav§)\ p6o(; (Cypriot p6Fo(;), Attic pou(; 
m. "current, flood', nspi-ppooc; "rings umflossen' (also aijjo-pooq for expressed aijjoppoc;), 
pon (korkyr. Dat. PI. p/7oFaTaiv) "das Stromen, stream' (= Lithuanian srava), puT6(; " 
flowing, stromend', nspippuTOc; "rings umflossen' (= Old \r\d'\c par/sruta-), puaic;f. "das 
Stromen', pua(;, -a5o(; "rinnend', pu5r|v, hom. pu56vAdv. "in Uberfluft'; psupa n. "Stromen, 
river; surge '; aKaAa-ppEirri^ "gentle flowing ', pa9u-pp£iTr|c; "deep flowing ', Eu-ppeirri^ "rich 
flowing ', (*-pp£F£Tr|c;, compare Old Indie sravat-), as Ionian pssGpov, Attic psTGpov n. " 
river flow, riverbed ' from themat. *sreue- derive ; pu0fj6(;, Ionian pua|j6(; ("the wash of the 
waves of Meeres compared) regelmaftige Bewegung, rhythm '; thrak. iTpuiJOov river name, 
iTpupn town name; 

Old Irish sruaimmu. "river', abret. strum^ copia (lactis) ' (= gr. psuija, if not ablaut 
equally with Germanic *strauma-)\ but Old Irish sruth "river', cymr. ffrwde\.c., from *spru-tu- 
; compare Pokorny Celtica 3, 308 f.; 

Old High German stroum. Old English stream. Old Icelandic s//'5^/r7/'"stream' (: Latvian 
straume, poln. strumien); 

Lithuanian sraviu, sravet/{o\6 sravu) " mild flow, seep, drip', sraujas ^rasch flowing ', 
srava^6as Flieften, Menstruieren', srove, Latvian strave, straume 'stream', strauts 
"Regenbach, Stromschnelle', Lithuanian sruta 'Jauche'; Old Church Slavic struja 'currer\t', 
ostrovb "\s\ar\6' ("das Umflossene'), poln. 5/At//77/e/7 "stream, brook'; 

Indo Germanic sreu- is extension from ser- "flow'. 

References: WP. II 702 f., Trautmann 279 f.; Vasmer 2, 287; 3, 32. 



Page(s): 1 003 



Root / lemma: sreno- -a 

Meaning: body part (hip?) 

Material: Avestan rana- m. "the outer Teil of Oberschenkels, thigh', mp. np. ran^ thigh '; 

Lithuanian strenos^6\e loins, the cross'. 

References: WP. II 705. 

Page(s): 1 002 

Root / lemma: sng-, sngos- 

Meaning: cold, frost 

Material: Gr. pTyoc; n. "frost', pTvEU), Perf. m. present-meaning sppTva " freeze, shudder, 

erschauern'; plYcbcjo "friere'; 

Latin fngus, -or/'sn. (= gr. pTyoc;) "coldness, frost', fnged, -ere'co\d sein, freeze, gefroren 
sein', fng/dus ^co\d'. 

References: WP. II 705 f.; after WH. I 547, II 434, zero grade from *{s)re/g-, to Latin riged' 
rigid', r/gor^ solidification (vor coldness)', Lithuanian re/zt/s ' s\c\r\ strecken' (different above 
S. 855, 862.) 
Page(s): 1 004 

Root / lemma: sromo- 

Meaning: lame 

Note: only altindisch and slavisch 

Material: Old Indie 5/'a/77a-"lame', srama-m. "Lahmheif; Old Church Slavic (etc.) chromb 

"lame'.
```


## [2026-09-14T02:28:32.451Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3320,3345p' POK_03.txt",
 "description": "Read POK_03 around sreno"
}
```


### [2026-09-14T02:28:32.535Z] TOOL RESULT

```
WP.  II  702,  Frisk  Gr.  Wb.  103.
srenk-  ^schnarchen'.  ^
Gr.  Qsyyio},  Qsyx^  , schnarche;  schnaube';  Qsyiiog  n.,  ^ey^tg  f.  ,Schnarch<?5 QÖyycog,  ^oyf.iög  ds. ;  air.  srennim  , schnarche'  (*srenk-nä-mi)'j  mir.  srSimm ^Schnarchen'  (*srenk-smn),  auch  srHmm  durch  Einfluß  von  srennim'^
einer  ähnlichen  Schallnachahmung  entspringt  wohl  gr.  ^vyxog  , Schwein rüssel,  Schnauze,  Schnabel' ;  ob  arm.  *rungn,  PI.  rngun-k,  rdngun-li  ,N«j|t löcher,  Nase'  daraus  entlehnt  oder  unter  idg.  *srungh-  damit  urverwftr^ sei,  ist  fraglich. WP.  II  705.
sreno-,  -ä  Körperteilbenennung,  etwa  ,Oberschenkel,  Lenden'.
Av.  räna-  m.  ,der  äußere  Teil   des   Oberschenkels,   OberschenkelVp»] np.  rän  , Schenkel';  lit.  strHos  ,die  Lenden,  das  Kreuz'. WP.  n  70Ö.
sresk'  ,tropfen'V
Av.  srask-  (srasca-)  ,triefen,  abtriefen  von ;  triefregnen',  sraska-  m.  (i sirisk)    ,Träne,  Weinen',    mp.    srixt   ,dropped',    arm.    srskel   {^srSsh- srösk-)  , besprengen' ;  Entlehnung  des  arm.  Wortes  aus  dem  Arischen die  Vorbedingung    für    die   Verbindung    von   av.    srask-,    arm.   srskti *klkk-skö-    mit   lit.    släkas    ,Tropfen',    §laketi    ,tröpfeln',    §lUti  ,spriti6S*i (s.  oben  S.  607  hleu-  ,spülen').  *  ■-
WP.  II  602  f.,  705.  4.
1003
gfeti'  ;fließen^;  sreu-et-,  sreu-men-,  sreu-to-s  ,Fl\iß',  srouä,  srouo-, sru-ti-  ,das  Fließen^^  sru-to-  ,fließend,  geflossen'^,  peri-sru-to-  ,rino-s umflossen^
Ai.  srdvati  .fließt^  (=  gr.  qeo}),  srava-  m.  ,das  Fließen'  (==  gr.  göog, aksl.  o-strov^),  giri-sravä  ,Bergstrom'  (=  gr.  qotj,  lit.  sravä),  srutd-  ,fließend, o-eflossen^  (=  gr.  qvxog  =  fem.  lit.  srutä]  hochstufig  lett.  strauts),  sruti- l  ,Weg,  das  Fließen'  (=  gr.  qvGig,  vielleicht  arm.  afu\  sravdt-  f.  ,Fluß' (=  gr.  -QsJ^sr-r]g\  ai.  srötah  n.,  apers.  rautah-  n.,  npers.  röd  ,Fluß*;  Kausat. srävdyati  ,macht  fließen',  sräva-  m.  , Ausfluß';
av.  (ravan-),  Gen.  PI.  raonqm  ,der  Flüsse',  urvant-{sru-vant-)  ^fließend' ; von  einem  (^(Ä)-Präs.  aus  (:  gr.  Qvd-fiög?):  av.  raodaiti  ,fließt',  raodah-  n. ^FlußS  urüd  f.  .Flußlauf,  Bett'  (ai.  visrüh-  f.  .Strom'  oder  dgl.?);
arm.  aroganem,  ofoganem  .benetze'  {*srou-),  vgl.  alit.  srävinu  .mache bluten'),  wohl  auch  aru  , Kanal*  (*s7^utis  oder  *sru{os);
gr.  Q€ü)  jfließe'  (Fut.  qevaoiiai,  Aor.  Epidaur.  i^sQQvß^  Kalymna  i[yyQvä Konj.  aus  ^^sruuä-]  vgl.  lit.  pasriivo  .floß'  aus  -ät]  gewöhnlich  *sreue-  in  äQQvrjv, lit.  sraveti]  zu  einer  dieser  beiden  schweren  Basen  ai.  Inf.  srdvitave)] QÖog  (kypr-  QO-Fog),  att.  godg  m.  .Strömung.  Flut'.  Ttegl-ggoog  .rings  um- flossen^ (auch  hp6-QOog  für  überliefertes  HipOQQog),  gorj  (korkyr.  Dat.  PI. QliOrPaXaiv)  .das  Strömen.  Strom'  (=  lit.  srava)^  Qvrög  ,fließend.  strömend', fcegiQQVTog  .rings  umflossen'  (==  ai.  pari-sruta-),  qvaig  f.  .das  Strömen', qvdg,  -döog  .rinnend',  ^vdrjv^  hom.  qvööv  Adv.  .im  Überfluß';  Qsv(.ia  n. .Strömen.  Fluß;  Wallen';  dy,ala-QQSLTr]g  .sanft  fließend',  ßad^v-QQelxiqg  .tief fließend',  iv-QQelzrjg  .reichlich  fließend'.  (*-QQeJ^eT7jg,  vgl.  ai.  sravat-),  wie ion.  QSsd^QOVj  att.  QsZd-QOv  n.  , Flußlauf.  Flußbett'  von  themat.  ^sreue-  aus- gegangen; Qvd^^ög,  ion.  Qvaf.i6g  (,dem  Wellenschlag  des  Meeres  verglichene) regelmäßige  Bewegung.  Rhythmus';  thrak.  ^tgt^Kjov  Flußname,  ^tq^j^t] Stadtname;
air.  sruaimm  n.  ,Fluß^,  abret.  strum  ,copia  (lactis)'  (=  gr.  gsvi-ittf  wenn nicht  ablautgleich  mit  germ.  *strauma-) ;  aber  air.  sruth  .Fluß',  cymr.  ffrwd usw.,  aus  *spru-tu-',  vgl.  Pokorny  Celtica  3,  308 f.;
ahd.  strourrij  ags.  stream,  aisl.  straumr  , Strom'  (:  lett.  straume,  poln. strumien) ;
lit.  sraviüj  sraveti  (alt  sravü)  , gelinde  fließen,  sickern',  sraüjas  .rasch fließend',  sravä  ,das  Fließen.  Menstruieren',  srove^  lett.  sträve,  sträume , Strom',  s^raw ^6- .Regenbach,  Stromschnelle',  lit.  srutä  .Jauche';  aksl.  struja ,Strömung'.  ostrov^  .Insel'  (,das  Umflossene'),  poln.  strumien  ,Bach';
idg.  sreu-  ist  Erweiterung  von  ser-  , fließen'.
WP.  II  702 f..  Trautmann  279 f.;  Vasmer  2,  287;  3,  32.
1004
sreup-  jSchorfiger  Schmutz  am  Körpe^^  t»^«
Gr.  (ßVTtog  m.  ^Schmutz,  UnreinlichkeitS  Qvrröayj  Qv^raivo)  ,befl^y ^vnaQÖg  ^schmutzig',  Qvrtdcj  ,bin  schmutzig',  ^vn;og  n.  ,Molken»,  f^^ ,reinigeS  Med.  ^wasche  mich,  schneuze  mich*;  urslav.  ''strup^  {&\xB*srtup^ oder  *sroupos)  ,Wunde^  (aksl.;  eig.  ,*Schorf  auf  der  Wunde^,  ,Gift,  fi^^ (slov.),  ,SchorP  (nbulg.  russ.),  ^Ausschlag  bei  Kindern^  (skr.),  ,Q^^ Kruste'  (pohi.  dech.);  ablaut.  ksl.  str^'p^t^  ,Rauheit,  Härte'. WP.  II  703,  Vasmer  3,  32.
srig-,  srigos-  ,Kälte,  Frost*.
Gr.  Qlyog  n.  ,Frost',  Qiyia),  Perf.  m.  Präs. -Bedeutung  eggiya  ,frierett, schaudern,  erschauern';  Qlyü)w  ^friere';
lat.  frigus,  -oris  n.  (=  gr.  Qlyog)  ,Kälte,  Frost',  frtgeö,  -ere  ,kaltlieii^ frieren,  gefroren  sein',  frlgidus  ,kalt'.  f;^
```


## [2026-09-14T02:28:46.210Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 sreno/sresk ===\"; grep -n -i \"strėnos\\|strenos\\|sresk\\|sraska\\|srask\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -20; echo \"=== BRT rana ===\"; grep -n \"rāna-\\|rana-  \\|sraska\\|srask-\" BRT.txt | head -30",
 "description": "Grep WLD and Bartholomae"
}
```


### [2026-09-14T02:28:46.281Z] TOOL RESULT

```
=== WLD Bd2 sreno/sresk ===
41150:Mit Guttural e rw. : s. streig- „steif”; ob dazu lit. strenos „Kreuz (am 
45850:np. ran „Schenker‘; lit. strenos „die Lenden, das B[reuz‘‘. Fick 339 zw.; 
45888:Av. srask- {srasca-) „triefen, abtriefen von; triefregnen“, sraska- m. (np. 
45893:srask-^ arm. srskel als Hcleq-sqo- mit lit. slakas „Tropfen“, slaketi „tr6pfeln‘^, 
=== BRT rana ===
3880:•  J.  ainrLvarana-  m.  'Bedeckung,  Beklei- dung': up^mii  [aite]  statri^ta),  anlama  °na also  druxs  yä  nasus  fräsnaoili  "zu  oberst das  Lager,  das  äusserste  Kleidungsstück erreicht  .  ."  V.j.ioC?)'*.
5330:KompE.  —  Zum  V.  'ar-.  —  ai.  arana-  n.
5384:Et.?  Ob  zu  ai.  ärana-  Adj.  'fem,  fremd'?  — Pü.:  aramut  'nicht  in  Herden  lebend',  Npü. : saßd  ia  tan.
5859:•  j.  asparana-  m.  Name  einer  Münze*>: °nS  F.  7;  —  duye  AazaaraAe  'nam  nidmat Vd.  6.
6900:•  j.  ahurana-  m.  Name  eines  Bergs  oder Gebirgs:  ahmat  haca  garayS  fraoxSyqn  .. 'nasca  Yt.  ly.  {.
7191:•  ].  atM.Öarana-  n.  'Feuergerat,  zur  In-  '  ^'  ^  ,  ,  ^  ,  ,.  ,.  „,  ,-' standhaltung  des  Feuers  dienendes  Gerät':  .^°|- „  ^)  ^nter  den  Namen,  d,e  fiir  den '«  (AP.)  pairisMnäna  V.  14. 7-                   ""^^'"^^  ergossenen  Samen  vorgeschrieben
7251:zu  *  myaso-ä. Sarana-  und  ♦i^nira-.  —  '«  In  |  Nachsatz  r  cim  Aoxa  . .  ^baraiU  .Ja'  ym Pü.  scheint  *aoM*tD  entsprechen, —  w)  Wennjj'^  glm  baraifi  agsttum  ..  ä  kl  pascalta nicht  -  mp.  äk;  s.  »u  J™.  -  •')  Geschr.  f^^atti  aiar/  .  .  ".  .  wenn  er  ihm  drauf Brennholz  bringt,  alsdann  segnet  ihn  Ä." Y.62.8f.  I  A)  'seit  dem':  äal  (s.i)  ^aiä •  j.,  g,'>  aat  Adv,,  meist  an  der  Spitze  ..  varrfa  viiar^n . .  a-  ahva  paurvatähi-a des  Satzes  stehend'*;  1)  zum  Ausdruck  ,.  vTraö^ahe  Y.io.iii.;  — frä  il  mazdä zeitlicher  Folge 'darauf,  dann,  alsdann,  da' :  i  Mm/  ,.  atmyatahajam  ..  ä°  aiiike  ahi pfnsal  zard^ultrS  ahumn  mazdqm  .  ,  3° .  aiwyäslö  V.p.  26,  2)   zur  Anknüpfung
7721:•  j.  «rszifyö.parana-  Adj.  'mit  Adler- fedem  besetzt":  isavasca  'na  V.  77.9;  Yt. /0.39,   lOI.
9242:•  j.  'karana-  m.  'Ende';  i)  räumlich:  "des  gläubigen  H.,  (aus  der  Familie)  der 'Grenze,  Rand;  Ufer;  Flügel  (des  Heeres)';  A'."  YL/j.ia?.
9256:.  j.  »karana-  n.  ein  Kleidungsstück  mite- '  f '■^'''«■'  "^  ^^^^t""  =  k>nnv-'\  12b lererGrösse, 'Hose'');  v«.«.r?y^.^«..««^,,r'f''-'«-'':  9+^4  -f^^«va-,  n  k.r.>ya-i\ "eine  Hose,  die  die  beiden  Schenkel  be-'~  \^[^-°'''.^f"^'-     .  ,    .    -,      .
9332:•  j.    'karana-  m.    Ohr',   uzw.  rfnÄ^ischer       haben;  vgl.  Yt.  ,0.  125.-»)  Anders  freilich Wesen":    lai  drvalö   drvatyiisca    asi    usi ■     Dk.  /.  4.  44  (SBE.  47.  59). 'na{Kp.)gava*dvari>mzafar»..pairi.-\^    .     ^^^3-    V.    'ausschütten'.    Praes.    2 urvalit^m  (sd.)  Yt.//.2.  ,_(.^„^._  _  pp^p^  ^^„y^._
9771:_^  _     •  j.  gao'karana-  m.  Name  eines  raythi-
10254:j.«   (näml.  aridvt,    mpunqm   hlmSimm' ,  ■    „„„s.starana-   m.   ein   bei    der Mää,  ••<™,.>^...v4,M,«  Y.65.=;-Arp^i„»        gebrauchtes    Gerät:    ymiäMi
11172:•  ).  £adTu.karana-  Adj,  mit  vier  Ecken, Kanten':  gaosävara  "«a  Yt.  j.  127,  /7.10,
12873:•  j.  dar«na-,  darana-  n.  i)  'Befestigung'
12923:•  j.  darflj'ö.haxaSrajrana-  Adj.  -  ?  -: pouru.ipaxM  dural  pihana  (sd.)  :i^a%ra- vana  'na  Yt.p.  i.
13482:•  j.  däuru.-upa.darana-  d.  'aus  Holz (-Stangen  od.  dgl.)  aufgerichtete  Hütte">: yat  'tu  vä  *tumats.aiwi.varane  vä  spS  nS vä  iri>yai  V.  cV.  1.
13700:•  j.  dürae-karana-  Adj.  'des  Enden  in der  Feme  liegen,  fembegrenzt":  asmati>m
13896:•  g.  duz-varana-  Adi.   'der  den  Miss-         .   .,   _.-  '.,         *        . glauben  hat,  misselaubiB':  'nats  vagsS  r,lsti  ,  ,  ..■,.,
13999:AvyaylbhStaVomp.  —   'larana-   n.   'ÜI)erganE  ,  g,  adrujyant-.  [Vgl.   noch  drujaiti.']
14949:•  j.  paiti.darana-  n.  'Ort  des  Verweilens, Aufenthaltsort':  /m  imqm  damqm  .  .  fra- pinaoiti  satim  * paitiltananqm  (sd.)  haxaa- nm  °ranqm  (GP.)  V._j.  31.
15412:ASn.  aus  'parana-  Adj.  'vormalig';  s.  'para, parö.  —  ai.  vgl.  puräriä-  Adj.
15644:•  j,  pairiä.hanana-  Adj.  —  ?  — ,  von  stn.- carana-  (sd.):  airi^carana  'na  'V.]4.'j.
15704:•  j.  parana-  n.  1)  'Feder":  mirrjahe  .  . vHrmßnaAe  (sd)    'tarn   ayasaisa   .  .  ana
16127:rä.:pur  atäs  i  kar  i  däiasiän.  l  •  j.  'parana-  m.,  n.  i)  'Feder':  cataurS
16201:•  '].  pflSö-parana-  Adj.  'des  Federn  weit
17764:•  j.  frayarana-  Adj.  'vormittägig":  *'ne''^ vS  usayärine  (sd.)  vä  *ayqn  N.p.
17913:frasparana-  1 00a
17931:•  j.  fra-8parana-  Adj.  'mit  den  Füssen ausschlagend':  usirahe..  'noAe  \tl4-ii.
17932:Zum  V.  ifar-.  —  ai.  vgl.  sphirana-  lu  —  Npü. : bi  sifarad,  erl.:  ftu'  ml  kunad.
```


## [2026-09-14T02:28:48.517Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ===\"; grep -n -i \"sre[sš]k\\|srišk\\|sirišk\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n -i \"sre[sš]k\\|srixt\" NYB_vol2_glossary.txt | head -20; echo \"=== CHEUNG ===\"; grep -n -i \"sraska\\|sresk\\|srask\" CHEUNG.txt | head -20",
 "description": "Grep MacKenzie, Nyberg, Cheung"
}
```


### [2026-09-14T02:28:48.654Z] TOOL RESULT

```
=== PHD ===
PHD.txt:568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
PHD.txt:1699:drop passing, paššinjag, srešk.
PHD.txt:3944:tear (n.) ars, sreški%v?
PHD.txt:4782:gáy- gādanī wattart wattarīh! srawēn- srawēnīdan srūwēn ` sarw, sraw, srü srūwar sarw bar-! burdan! srub srubén Srūš srūšīg srūd srūdan sarmāg srub srešk srištan sardīh sard, srat
PHD.txt:4791:srešk
PHD_mackenzie.txt:7764:tear (n.) ars, sreSkt,L~~                    siderati011.
=== NYB ===
=== CHEUNG ===
```


## [2026-09-14T02:28:54.351Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '45840,45900p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt",
 "description": "Read Walde-Pokorny II 705 context"
}
```


### [2026-09-14T02:28:54.404Z] TOOL RESULT

```
sreno-, -a — srlg- 


705 


sreno-, -a Korperteilbenennung, etwa „Oberschenkel, Lenden" 

Av, Tana- m. „der auBere Teil des Oberschenkels, Oberschenkel^, mp. 
np. ran „Schenker‘; lit. strenos „die Lenden, das B[reuz‘‘. Fick 339 zw.; 
sehr wahrscheinliche Verkniipfung. 

srenk- „8chnarcbeii“. 

Grr. Qeyxoy^ ,,schnarche; schiiaube“; air. srennim „schnarche'^ 

(^srenk-na-mi^; ob nasallos dazu air. sron „Nase“, cymr. ffroen^ mbret. 
froan^ nbret. /rem „Kasenloch'‘ als Cymr. yfr deutet aberauf.5^- 

hin (Pokomy brief lich). Pick II ^ 318, Pedersen KG. I 82. 

Finer ahnlichen Schallnachahmung entspringt wohl gr. ovyyog „Schweins- 
riissel, Schnauze, Schnabel^; ob arm. *mngn^ pi. rngun-k, Hngun-k „Nasen- 
locher, Nase'^ daraus entlehnt oder unter idg. ^srungJi- damit urverwandt 
sei, ist fraglich ; s. Curtins 504, Medermann e und ^28, Zupitza KZ. 36, 59, 
Hiibschmann Arm. Gr, 1 486 f., Boisacq 838, 845 ; Qvyyog nicht naeh Froehde 
KZ. 22, 267 zu oqvooco „grabe“ (s. reu-, reiih- „aufreifien“), obwobl „Schweins- 
ru8sel“ die eigentliche Bedeutung des Wortes ist, auch kaum im Vokal 
von diesem beeinfluBt. 

srens- oder srems- „zerfallen, zerstieben; Franse“? 

Ai. sranisat% ^ate zerfallt, vergeht“, ptc. srastd-li ; 

lat. fimbria „Franse, Troddek* (sei diss. aus "^frimbria — wie anders 
roman, ^frimbial — , alter ’^srensria; andere Deutungsversuche s. bei Yf. 

LEWb.2 8. V.); 

Slovak, strdsno „Webergerei6, Trumm, Zettelgarn, Fransen" (sei ursl. 
stresno aus ^srens-no-)^ eech. mit diss. Schwunde des anl. s- tfdsnej ifisne ds, 
Petersson LUA. 1916, 45f.; ganz fragwiirdige Yerbindung; fur das cech. 
(und daher auch das slovak.) Wort ist wohl Yerbindung mit cech. tfasu, 
tfdsti, tnsti „schutteln'^ (abg. tresQy iresti „erschuttem'‘) wahrscheinlicher. 

sresq- „tropfen“. 

Av. srask- {srasca-) „triefen, abtriefen von; triefregnen“, sraska- m. (np. 
sirisk) „Trane, Weinen“, mp. srixt „dropped“, arm. srdkel {*sresq^ oder 
srosq-) „be9prengen“. S. Bartholomae Airan. Wb. 1 644 f. m. Lit, Entlehnung 
des arm. Wortes aus dem arischen bekampft Hiibschmann I A. 10, 28; sie 
ware die Yorbedingung fiir Picks I^ 208 ansprechende Yerbindung von av. 
srask-^ arm. srskel als Hcleq-sqo- mit lit. slakas „Tropfen“, slaketi „tr6pfeln‘^, 
sUkti „spritzen“ (s. u. kleu- „spulen“). 

srig- „Kalte, Frost“. 

Gr. Qiyog n. jjFrost'^, pf/eco, Pf. m. Praes.-Bedeutung eogiya „frieren, vor 
Kalte schaudern, dann schaudern uberhaupt“;
```


## [2026-09-14T02:28:56.473Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"srasca\\|sraska\\|srask\" BRT.txt | head -20; echo \"=== rana ===\"; grep -n \"^.\\{0,12\\}j\\.  *.\\?rana-  *m\\.\" BRT.txt | head; echo \"=== alt ===\"; grep -n \"Oberschenkels\" BRT.txt | head",
 "description": "Grep Bartholomae for srask and rana"
}
```


### [2026-09-14T02:28:57.666Z] TOOL RESULT

```
14148:•  j,  driwika-  n.  'Stöhnen,  Heulen':  pait- yar^nt  (näml.  fiaraivahe)  fräkinntat  aurS mainyul. . ^sraskpmia  'käca (AP.) "..Weinen und  Stöhnen"'>  V.;.8.
27390:•  j.  srask-  V.  'triefen'.  Praes.  2  srasca-, 30  (Kaus.)  iraseaya-.
27396:'''sraska-
27404:•  '].  srasCant-''  Adj,  (fem.  °nff-y\  PPA,: s.  srask:
=== rana ===
=== alt ===
28919:•  j.,  g.  haxt-**  n.  'der  innere  Teil  dea| Oberschenkels':  jieii^a  aps  .  .  'H  (AD.) paULjasaiti  V.ÄS9;  58,  p.ai';  —  */«'' F. Jg.  a)  to«ü»  'tayä  (GS.) 3*  sva.  'in Mark  und  Bein,  in  Fleisch  und  Blut': yavtst  aiul  (sd.)  *zrazciists  bSndi  'tayä "^■53- 7-
```


## [2026-09-14T02:29:04.234Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27385,27410p' BRT.txt; echo \"=== rana search ===\"; grep -n \"rana-  m\\.\\|räna-\\|rāna-\\|'rana\" BRT.txt | head -20",
 "description": "Read Bartholomae srask entries"
}
```


### [2026-09-14T02:29:04.321Z] TOOL RESULT

```
ianä.  —    3)   Die  Dreiheit  '      '      "
und  IUI-  bildet,  wie  yasna-,  ■Doiah-  nnd  iyait. \anar  in  Y.  34.  I ,  nur  eine  Variante  der bekannten  Dieiheit  manah-,  va!ak-,  fyaiAana: irat/aA-  vertritt  va^aA-.  —  4)  Nach  der  n-Dekl. —  S)  Pü.!  aarnb  statt  dd  ra  b  =  irav.  — 6)  Hds.  irävaoitm  und  irauaalum  (T);  Pfi. : srav,  erL ;  afasläi ;  s.  No.  7.  —  7)  PS. :  rrav, erl.:  apasläk  u  tand;  5.  No.  6,  —  8)  Pö.: nänükih,  Sü. :  ktrti^.  — ■  9)  Them.
j.  sroiiS  V.  tg.  42 :  s.  onter  irä-.
I-  •
Ä  Vd,  .
•  j.  srask-  V.  'triefen'.  Praes.  2  srasca-, 30  (Kaus.)  iraseaya-.
i)  'triefen,  abtriefen  von  -'  (Gen.  statt AbI.),vonfcttenSpeisen:a»^«iF(Sp.357f.) srasfintls  :^an^ä'V.3.2<}.  aa)  trief- regnen sva.  triefenden  Regen  fallen  lassen, veranlassen',  persänl.:  tnlsti  zl  ml  kim  .. var?ntal{si.)^a  sna^intal'a  srasctttta^a (3PPM.,  näml.  arsäna)  *fyankuntaica  Yt 5.  lao;  —  haca  xsafnB  varmtya  .  ,  sra- scirttyä  "in  einer  Nacht,  die  (sva.  in  der es)  . .  triefregnet"  Yt  16.  10'*.  b)  'als Triefregcn  (zur  Erde)  fallen':  cvat  aBanhä apSyaf  snaiSinfyai(sd.)äi  srascintyaica" "wie  viel  von  dem  Schnee  und  Regen- wasser . ."  V.  6. 36.
mit  *ava  'abtriefen':  vUpanam  ^sl  *ava.- iras^intam^  .  .  äaRia  *raluiite  (sd.) N.ö"Ä       ■
mit  vJ  Kaus.  'auf  allen  Seiten  beträufeln, besprengen' :  hakir^l  apd  vXtraslayat  "ein-
dby  Google
1045
'''sraska-
srira-
1646
mal  solleo  sie  (die  Brennhölzer)  mit  Wasser
besprengen"  V.  7. 19.
Vgl.  arm.  srsMi)  'besprengen',  mp. ■diopped',  PPfP.  (SBE.  j/.  191,  vgl.  Bthl. WklPbU.  /epS.  io6o)i  s.  noch  in  srasta-.  — Pü.  (lu  V.  6):  latark  'Hagel*,  (in  N.):  1^ mtat(}).  (m  V.7):  äiinßnd,  {lU  V.  j):  ddtk. —  >)  S,  10  V.  *.  4,  Sp.  1616  o.  —  •)  yäi- Dat  slatl  Gen.  —  J)  Ilds.  lyu  asratantim.  — 4)  Aue  idg.  'sreti'  oder  *stSsi',  mit  Dehn- vokal;  üchlarm.;  s.  IFAnz.  ro.  l8.
''  m.  'Träne, Weinen':  aal  ahe (näml.  haraevahe)  paityar^m  fräk^rmtal anr3  mainyus..  *'k?m^a  ifria'ii3(sd.ya  V. 7.8.
Zum  V.  irasi-.  —  np.  sirisi  'Tropfen,  Träne'. —  Pu.!  irc'a  (in  Avf.-Buchst.).   —    ■)  NA.  sa-
•  '].  srasCant-''  Adj,  (fem.  °nff-y\  PPA,: s.  srask:
KompE.  —  ')  Nur  'Hitl-,  %  298.  4.
•  j.  sräy-:j-rr-  £  'Schönheit':  hkrpa  ava- vatqm  iraya'^  (IS.)  ya%a  dxhayafam  tao^S (sd.)  Yt./7.ii; — kihrpa  avavais  *sraya'"'' (IS.)  ya^a  dämqn  sraiStäil  "am  Körper von  der  Schönheit  eines  solchen  wie  die schönsten  Geschöpfe  (sind)"  H.  2. 9.
ai.  iti-  f.  (:  Sriya).  —    ■)  Statt  *sriya  geschr.;
S  410.  —  ')  So  M  6  and  lu  Vyt.  56.    Ausg. ■yi.
j.  sräyeüi  N.  J/:  lies  srävayeiH.
j.  srävaiiktm  N.  32:  lies  travaithi.
=== rana search ===
3880:•  J.  ainrLvarana-  m.  'Bedeckung,  Beklei- dung': up^mii  [aite]  statri^ta),  anlama  °na also  druxs  yä  nasus  fräsnaoili  "zu  oberst das  Lager,  das  äusserste  Kleidungsstück erreicht  .  ."  V.j.ioC?)'*.
5859:•  j.  asparana-  m.  Name  einer  Münze*>: °nS  F.  7;  —  duye  AazaaraAe  'nam  nidmat Vd.  6.
6165:•  j.  aSa-ä^ra-,  aäö.ÜdTa-'*  Adj.  'der seinen  Ursprung  im  Asa  hat':  vispanam vohunqm  vispanam  'ranam  H.  1. 1 ;  —  vis- palsu  var»hufu  vUpagsuca  -ra^iu  YL  1/.3'*; P.  27'';  -^  äps  ..  urvara  .  .  vitpa  voka 'ra  y.8.^.  a)  vlspa  *voAli  maxdaoäla 'ra  Y.ig.2,  22.3,  YL5.89,  y.88,  H.i.3, 16,  V.ii.i,  2,  10,  Vd.4;  —  i7^»t(  ..  vispa *voAa  mazdatiäta  'ra  Yti.  7.
6900:•  j.  ahurana-  m.  Name  eines  Bergs  oder Gebirgs:  ahmat  haca  garayS  fraoxSyqn  .. 'nasca  Yt.  ly.  {.
8077:vTsp^m  ahäm  .  .  °zay%    vafnJI   döi^räbyü  '  a)  kar^säspim  yat  äs   'ranarn  aojislS  Yt.
8467:•  j.,  g.  urvarä-  f.  Tflanze',  meist  Plur.; Sing,  äwich  koll.'*;  oft  göttlich  verehrt; I )  im  AUgemeben,  hauptsächlich  von  den Nutz-  und  NährpSanzen:  eaiti  hsnti  'ranqm sar»fia  "wie  viel  Arten**  von  Pflanzen giebt  es?"  V.5.19  PitZ.;  —  a^ra  »;? raoomti  vUpk  vispSjarvoö  V,5.  19;  — yerihe  paiti  pourujar^a  s»mSoa  usuxlyeinii •rä  Yt  /j,  10;  —  avqm  vanqm  .  .  yä visps.bis(_sd.)  nqma  yqm  upairi  vjspanqm •ranqm  iacxma  nilayal  YL  /2. 1 7 ;  —  vis- paaqm  'ranqm  taoxma  .  .  ysi  hmti bartzisia^a  hubaotaitsmaca  V.  2.  28; 'ranam  (als  Subi.)  zairi^aonanam  tarp- matm  paiti  amäca  *usuxsyänti  Yt7.4'';
8470:-*  'ranam  sBra  vaxfyente  (sd.)  vaxsa Yt.A4a;  —  'ranqm  (statt  Akk.  des  Ziels) urukmyanqm  ava.jasä/ii  V .  /q,  18;  Vyt.22; kö  p»rfi^we  (sd.)  aitihh  sjmS  *upa.- 'i:war>5li    'ranqm    (als   Obj.)    V.  p.  z;    —
8471:'  'um  "ranqm  uzuxfyenlinam  srlranqm zairi^aoiianqm  vaxsA  (sd.)  apayasaite  V. /Ä63;  Yt. /Ä6;  —  at  aRyäi  (näml.  dem Rind)  mazdä.  'rä  vaxiaj  (sd.)  Y.4S.6;  — avi  racynyq/H  varauhmt  azuitlmca  'ranam Yt.  ^2.3;  —  nima  'vaire  (VS.)  varMhi masdaöäte  asaone'V.  ig.ii;  Vyt.22,  N.7/, f)7.  a)  Plut.,  im  Gegens.  zu  alxa-  Plur., 'pflanzenbewachsener Boden';  ahond  una 'rlhuca  paiti  *baooisca  vTdtnanmnS  saoa- yäti  . .  ärvatS  urva  *aexahuea  (sd.) . .  "der Seele  des  Gläubigen  ist  es  so,  als  ob  sie auf  Wiesengiund  (stehe)  und  Wohlgerüche empfinde,  .."H.  2. 7— 25.  b)  sva, 'Baum', a)  im  Gegens.  zu  var^ä-.  pairi  van>'>iJ- byasca  'räbyas^a  atsmaiibyS  (sd.)  V.  16. s.  ß)  sonst:  v3r»ynahe  . .  yS  .  .  sainif marisat  'ranqm  ". .  der ..  im  Flug  der  Bäume Wipfel  streift'"  Yt./.4.2i''.  c)  'Pflanzen- Stengel,  Reis':  yavat  akmUi  paitinqm •ranqm  aetavat . .  "so  viel  es  ihm  einzelne Reiser  gibt,  (als  ob)  er  so  viel  .  ."  V.  iV. 86,  a)  bes.    der   zum  Barisman    ge-
8478:—  mä  .  .  kaine  .  .  tarS  daxslim  pärayat (sd.)  tarö  ap?mca  (sd.)  'ramea  V./5.9; 10;  —  avi  tu  dim  disyata  (sd)  yä  apasca 'r-hca  zao>nhca  Y. A3,  a)  Du.  in Verbindung  mit  sp-  Du.;  yat  iurmaot a»haosimne  äpa  (Sh-erz.)  °vaire  Y.  9.  4; usw.  2)  mit  einer  einschränkenden Bestimmung :  aisma  .  .  yat  vä  aitaaham  . . 'ranam  yat  ätn.ciiranam  V.  ^75;  — altayh  °raya  aian^ar?}  V . S.-j ^-y  —  upa .  .  nmärum  baoiayaH  un-äsnayä  fä  .  . kamcit  v<l  hubaoi'At^manqm  °ranam  \.S. 2 ;  —  aoa  az»m  yS  ahurö  masda  °rä  bal- iasy'i  uzbamn  ".  .  die  Heilkräuter  . ."  V. JO.4;  —  ynän^m  vä  .  .  kamcit  vä  vlta- afianam(sd.)°ranainY.ij.i4; — yavanqmca vtlstranqm^a  'ranqm'a  :far?i5.bairyartqm (sd.)V.J.4;  —  'raaqm  s^awrlranqi'i  (sä.) Yt/>5S;  Vr.2/.i;  —  'rShu  paiti  barss- manyäku  Y.  2.11,  "Y't /0.14s;  —  imqmcä 'rqm  bansmanim  Y.  22.3,  a)  durch Namensnennung:  aetayh  *rayh  ya  i-aoÜ ha'jana^aia  V.  14.  4;  V.J.  3,  22.  i,  62.  9
9242:•  j.  'karana-  m.  'Ende';  i)  räumlich:  "des  gläubigen  H.,  (aus  der  Familie)  der 'Grenze,  Rand;  Ufer;  Flügel  (des  Heeres)';  A'."  YL/j.ia?.
9332:•  j.    'karana-  m.    Ohr',   uzw.  rfnÄ^ischer       haben;  vgl.  Yt.  ,0.  125.-»)  Anders  freilich Wesen":    lai  drvalö   drvatyiisca    asi    usi ■     Dk.  /.  4.  44  (SBE.  47.  59). 'na{Kp.)gava*dvari>mzafar»..pairi.-\^    .     ^^^3-    V.    'ausschütten'.    Praes.    2 urvalit^m  (sd.)  Yt.//.2.  ,_(.^„^._  _  pp^p^  ^^„y^._
9771:_^  _     •  j.  gao'karana-  m.  Name  eines  raythi-
11229:•  j.  äaräna-  n.  '(Ackerfeld,)  Feld,  Gefild': haoma  .  .  staomi  stmS  yd^a  raohahe  .  . •fipm  "ich  preise  der  Erde  . .  Gefild"  Y. /o.4'>.
11547:•  j.  Jafra-  Adj.  (fem,  °/-ä-)  'tief:  var5is .  .  'rahe  Yt.5.49;  ■y.46;  —  'ra  varayS Yt /O.  14;  F. /5J  —  bune  'ranam  vair- yanam  Yt  15.51,  V.  75.42 ;  —  ranAaya .  .  'raya  hasarirS.vlraya  Yt.  i^.  29;  — frayanä  (sd.)  , .  °ra  Yl/0.  112;  —  dsnui ..  'ra  (NSf.)  Aog.  77  (?)■).
12336:aiwi.vanyh  dsnavB  'ra  ■vySxanaYx.-^.'jy, -  yBz)m  taaa  taurvayaia  Virihrtm  dStm- IM  'ranam  Yt.y.  38;  38. AbleiL  —  VgL  Vüra-  EN.  — -  kurd.  lir  'wüd, unbändig';  WklPh.  iSyS.  1307;  ander*  IF.  10, 1  No.  Unsicher.  —  Fü.:  lär,  (»u  V,  13  erL): vbiäskär;  SQ.i  htrti/iaAi  s.  noch  No.  3.  — ')  Mit  u  nur  Yt  //.  55,  $6.  —  *)  Stammt aus  y.  46.  13,  mit  Umtetitmg  ins  jAw.  Pü.: /aAär  dna,  vgl.  unter  *ni>ttdäidyäi*),
12658:dadräna-
12664:•  j.  dadräna-,  daJSräna-  Adj.,  PFfM.: s.  idar-.
15214:•  j.  pawräna-  n.  'Bergabhang,  Halde': äat .  .^wä  . .  murr/a  .  .  vibann  .  .  *aoi '„a  Y.  10.  II.
15876:•  j.  'pasu.vastra-  n.  TCleid  aus  Tier-, /spez.i  Schaffell':  carimanam  'ranamca N.  >8;  8v,  —  'rahe  F.^b.
16127:rä.:pur  atäs  i  kar  i  däiasiän.  l  •  j.  'parana-  m.,  n.  i)  'Feder':  cataurS
```


## [2026-09-14T02:29:11.215Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Oberschenkel\" BRT.txt | head -20",
 "description": "Grep Bartholomae for Oberschenkel"
}
```


### [2026-09-14T02:29:11.286Z] TOOL RESULT

```
25363:schenlcels'';  Oberschenkel  (überhaupt)': doHnim  (hz.Aliyum)  'tum  V,&59-6i',  g. 21  f.';  —  an/ar?  ähittm  'tarn*'  V.lß.  16;
28919:•  j.,  g.  haxt-**  n.  'der  innere  Teil  dea| Oberschenkels':  jieii^a  aps  .  .  'H  (AD.) paULjasaiti  V.ÄS9;  58,  p.ai';  —  */«'' F. Jg.  a)  to«ü»  'tayä  (GS.) 3*  sva.  'in Mark  und  Bein,  in  Fleisch  und  Blut': yavtst  aiul  (sd.)  *zrazciists  bSndi  'tayä "^■53- 7-
30216:Oberschenkel';  ahd.  dioA,  ne.  Ihig;  vgl.  DST.
```


## [2026-09-14T02:29:13.677Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25355,25375p' BRT.txt; echo \"=== 30210 ===\"; sed -n '30208,30222p' BRT.txt",
 "description": "Read Bartholomae rana entry"
}
```


### [2026-09-14T02:29:13.751Z] TOOL RESULT

```
dby  Google
I5»3
rä9inan-
rämanivant-
1S»4
•  j.  rädman-  Adj. mit  —  (Gen.),  Anhänger':  yS yasnS  aojanS  aiahe  'ma  (NS.)  jlslayamnd ya^wa  gai'hä  asahe  tmrrjinte  "wer  .  . sich  einen  M.  nennend,  sich  Tür  einen Anhänger  des  A.  ausgebend  mit  Zauber die  Well  des  A.  zerstört"  Y.  Ä  3.
Zum  V.  riii-.  —  Vgl.  rä%>ma-  (und  iB.  iX.  dar- man-  neben  darma-).  —  Pü.:  iaht.
•  j,  rSna-  m.  'der  äussere  Teil  des  Ober-
schenlcels'';  Oberschenkel  (überhaupt)': doHnim  (hz.Aliyum)  'tum  V,&59-6i',  g. 21  f.';  —  an/ar?  ähittm  'tarn*'  V.lß.  16;
—  -««(ND.)  F. Jg.
KompA.  —  Nach  FicK  VglWb.*  /.  339  aus *srän'.  —  mp.  (Pü.),  np.  räti  'Schenkel'.  — ')  Im  Ge^ensalt  tu  kaxl'.  —  •)  Man  TMlangte Du.
•  g.  'rana-,  runa-"  m.  'Streiter,  Kämpfer', nur  Du.",  von  den  mit  einander  im  Streit liegenden  Religionsparteicn^':  yam  x^nü- Um  (sd.)  'neibya  da  %ws  ^rä  tuxrä masdi  ayanhs  xfuita  (sd.)  "was  du  als Belohnung  den  beiden  Parteien  durch dein  rotes  Feuer,  o  M.,  durch  das  ge- schmolzene Metall  bereiten  wirst"  Y.ji.  9;
—  yqm  dh  mainyU  ä^ra/3  asalä  cSis 'nSibyS  xsnütim  (sd.)  "was  du  als  Belohnung durch  den  (heiligen)  Geist  und  das  Feuer bereiten  wirst  —  und  durch  Ala  gelehrt hast  —  den  beiden  Parteien"  Y.j/,  3;  — t3  da  sptntä  mainyU  .  .  ährä  vanhäu vidaiffm  (,sä.)  'nöibyä  Y.4'^.6;  —  ä'i^ra suxrit  . .  vanhäu  vidati  (sd.)  °nay3  Y. 31. 19;  — ya  (näml.  aÄ/)  vT  aUs  'ndibya'i savHi  (sd.)  vJdäyäi  Y.43.  ra.
Zum  V.  'ar-.  Tgl.  rhta-  (•-  ai.  räna-)*).  — Pü.!  foUatlätäit  (SQ.!  praiivjdaij-ta^  oder ähnlich),  dazu  (autsei  Y.  43)  die  ErL:  iuxlu Frixtt)  (Sü.:  iuddham  aiuddkamta)  ficiläi  kirnit 'den  geretteten  und  den  preisgegebenen  macht er  ofTenkundig'.  —  •)  %2g4.  3;  nur  in  rqnayi. —  ')  Zu  y.  43-  la,  w*  NA,  'äye,  t.  BB.  I4- 15,  KZ. J0.3J0.  — 3)  Zaletit hierüber  JusTlPrJ. (SJ.  *39;  E.  auch  zu  tjsa:  —  4)  räna- :  ttna- : ar-  y.^dtmäna-:  d>inana-:gi.iin-a;  a.  noch IF.  7,  6?  No.  —  9  Bthl.  IF.  12.  na.
•j.  r»na-pä(y)-  m.  'BeinschÜUer,  -schiene'; yaisqm  zayanam  rd&sisti  .  ,  dvadasll  'J>ö
(ND.)"   ".  .   ein   Paar   Beinschienen"   V.
I4-9-
Pü. :  Tänpän,  erl.:  sfarfak  'kleines  Schild',  s. West  ZDMG.  43.  49,  Jn.  Her.  119  und unter  'iarana-  No,  2.  —  ")  S  4^4  Ntr.
•  g.  ränyö.sk9r3ta/-  Adj.  'GlUck,  das Glück   schaffend,   bringend',    vom  Rind:
yf  ahmai  gqm  *'r»Ulm  hSm.talat  "der  für uns  das  Glück  bringende  Rind  geschaffen hat"  Y.47.3;  —  kdha  mazdä  *°r;inm gqm  iiasöit  "ob  wohl  der,  o  M.,  des GlUck  bringenden  Rinds  Besitz  erlangen wird  . ."  Y.  50.  3;  —  küäbys  asTm  *'rfitlm gqm  tass  "wer  sind  die,  für  die  du  das Glück  bringende  trächtige  Rind  geschaffen hast?"  Y.44.6.
Komp.:  *rärt)'a4-(Konipar.  zum  ai.  V.  ranyati^ lum  S  %.%  304 II. 43l+*'ij«/a/-, eig. 'das Be- haglichere, Angenehmere  bewirkend';  ai.  vgL ranak^l'  Adj.  —  Pn.:  räßh  Aarlär.
=== 30210 ===
s  Wesen    des
luf  Hutös  -  in   Sü.  merkwürdiger  Weise  mahai
punyam\  -  beziehen;  MiLLS  G. 381  spricht  von
•■Hülötk'    als   'the  bride's  molher,   as  arranging
the  ceremonial';  aber  die  Braut  in  Y.  jj  ist  doch
Pourucislä,  die  jüngste  Tochter  Zara%uilras\
Eig.   'mit  schönem  Dickbein'  (vgl.  iBed.  ai.
vämoruh,  gr.  «aXJjiiiTO,-);  *laoia-  m.  "Dickbein,
Oberschenkel';  ahd.  dioA,  ne.  Ihig;  vgl.  DST.
MSI_5.  9").   —  mp.  hutös  [iB.  Dk,  7.  4.  86,
Y.5i.  sPüErl.i   s.  noch  •)].  —  >)  Was  JUSTl
ZDMG.  4g.  ÖS4  dagegen  vorbringt,   ist  nicht
stichhaltig.
•  j.  "hutay-"  f.  'Auspressung,  Kelterung", des    ffaoma;    kävanaHbya  (sd.)    .  .    '*ya-
dby  Google
```


## [2026-09-14T02:29:21.732Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==157' HRN.txt | head -60",
 "description": "Print Horn leaf 157 (printed p.135)"
}
```


### [2026-09-14T02:29:22.769Z] TOOL RESULT

```
— 135 —
*Ruhe'; phlv. hu]ram, ram(i)sn, rämmltan; ai. rdmU'
*Lust'.
oss. üromjn 'zurückhalten, hemmen, beruhigen' (263).
605. ran 'Schenkel'.
aw. räna- 'Schenkel'; phlv. ran^ ränpün, arm. LW.
eran, meist pl. eranK (Hübschmann, No. 96).
kurd. bei. (221) LW. ran; af/. vrün.
606. ränden 'treiben, stossen*, ranis,
Contrahirt aus rawdmden^ Causativ von reßen
(No. 619), vergl. Kä»än: Z(efre), beräw, heräivött^
heräft s. v. ränden,
Phlv. rayinTtan, räyma, räyln(i)sn, räymitärih (Men.),
jüd.-pers. pJN^NI (Is. 63, 17) sind nicht klar.
607. rah^ ras ^), reh *Weg ; espyes.
skr. vergl. rathyd- Xandstrasse' (spät) 2); phlv. reis,
aspjräs; af/. lär^),
LW. kurd. rl; bei. ra, n. rah (219); af/. räh;
arm. rah.
Gehört hierher auch np. reste^i (phlv. rastan, Men.),
Praes. reh-em^ rehlden u. s. w. 'befreit werden, ent-
kommen', wörtl. 'sich auf den Weg machen'?**)
608. rubüden 'wegnehmen, rauben', Praes. rubay-em,
riibäyende ; ruften 'fegen , gäten', Praes. röb-em,
ai. V^löp' (älter röp-) 'zerbrechen, packen, plündern,
rauben''^); phlv. röp 'Raub' (AV.-GL), kah]rupäl 'Bern-
stein (Säy. näsay. II, 115); got. biyaubön 'berauben'.
bei. röpcifj 'fegen, kehren' (329).
ö hat noch Kää. Z. böröw (Impt.), börowön (Aor.),
rowon (Praes.).
np. rubäyem geht auf älteres *rupäyati zurück.
^) BQ. Rückert bei do Lagarde, Ges. Abh. 51, Note l.
^) Aw. hizvö raiHm (y. 50, 6) beisst iiacb Bartholomae,
KZ. 28, 34 *Lenker der Zunge*, siehe aber Geldncr, KZ 28, 259.
') Aus *ral (Trunipp, Graramar of the Tastö § 7); //är,
Darmesteter, Ch. pop., p. CLXXV, Note 2.
*) AM. 183 Zeile 1 hat aUerdings biriheS,
^) Aw. urüpay^intl (y. 43, lÜJ muss als unsicher bei Seite ge-r
lasäcn werden.
```


## [2026-09-14T02:29:23.275Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sirišk\\|sirisk\\|siriSk\\|siri.k\" HUB.txt HRN.txt | head -20",
 "description": "Grep Horn/Hübschmann for sirisk"
}
```


### [2026-09-14T02:29:23.325Z] TOOL RESULT

```
HUB.txt:6073:zd. sris 'haften*; sirisk 'Tropfen', paz. srisk, zd. srasc 'be-
HUB.txt:7572:mischen*, skr. griS (siehe oben p. 75) ; sirisk *Tropfen = zd.
HUB.txt:7820:idg. ''^skepti') ; sikdr * Jagd', siehe oben p. 80 ; sirisk *Tropfen'
HUB.txt:8489:'Nisse', osset. lisk, skr. liksa-; sirisk *Tropfen' = zd. sraska-;
```


## [2026-09-14T02:29:30.004Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6068,6078p' HUB.txt; echo ===; sed -n '8485,8492p' HUB.txt; echo \"=== HUB ran ===\"; grep -n \"rān 'Schenkel'\\|ran 'Schenkel'\\|Schenkel\" HUB.txt | head",
 "description": "Read Hübschmann contexts"
}
```


### [2026-09-14T02:29:30.071Z] TOOL RESULT

```
Exit code 1
xratU' ; xirdmldan schreiten*, skr. kram; firistCLdan schicken ,
firista *Bote' = ^rz. frMa Shk. 245; firEsta *Bote, Engel' =
arm. hrestak; firod (fiirDd) *hinunter' = paz. fro^; fireftan
'betriigen H. 829; Jirih \iel, mehr H. 826; siristan mischen,
skr. gris Verbinden*, crt *mischen , sires 'Leiin' (afgh. sare$)^
zd. sris 'haften*; sirisk 'Tropfen', paz. srisk, zd. srasc 'be-
sprengen ; sipah *Heer' (jiid. pers. supdh H. 699) = zd, spada-;
siparam ubergebe* (inf. supurdan), Wrzl. spar; sipar 'Schild*—
paz. spar; sipihr 'Hininier = skr. gvifrd-; siped weiss' = zd.
spaeta- ; sitara 'Stern' = zd. star- ; siparl Vollendet*, paz. spur
'perfect*, arm. spar 'Ende', -sitdn {-istan) *Ort' = ap. stana-;
(eval):1: == not found
```


## [2026-09-14T02:29:31.128Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"r'n'\\|r\\`n\\`\\|belt\" SOD_pages.txt | head -30",
 "description": "Grep Gharib Sogdian dictionary"
}
```


### [2026-09-14T02:29:32.346Z] TOOL RESULT

```
11847: 2829 przzw'n'y pr'n'y B           ^v^o^'j^o^)-^              2842 bstry C                                  (>-*)•>-
23724:                                                                      paranay (pr*nJy-, pr'n'y-) ©<*para-a-naya-
23731:        pr>k>nty> Frag. Len. 34.3, S W, xwast, 1991, 324        6979 pr'n'k    B                          f^»>^<<«
23742:     parakan (pr'gn-) ©<para-kan                                     parane ©pi. -r ^pr'n'k
23751:       paranay ^pr'n'y-
28011:                                                                         belt
28019:                                                                         belt
37731:(to)be carried 7, 3021                (to)bc fixed    1080                    belt 8435, 8436
```


## [2026-09-14T02:29:36.485Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"8435\\|8436\" SOD_pages.txt | head -10; echo \"=== ctx ===\"; sed -n '28000,28030p' SOD_pages.txt",
 "description": "Find SOD belt entries"
}
```


### [2026-09-14T02:29:36.564Z] TOOL RESULT

```
28008:     SCE 135; TSP 2.810; Hen. BSOAS 12, 307.36;                     8435 rW C                                            ju^T
28016:                                                                    8436 iVkh B
37731:(to)be carried 7, 3021                (to)bc fixed    1080                    belt 8435, 8436
=== ctx ===
      GNJ£ 1078; BSTi 221
                                                                           np28
8420 r»f q'w     C -* r'f k>w                                       8434 rtarwc M, S        {fij :^j^S)j3^\j «.U ^ j c~-t j3J
8421 r'fqyn      M => r'pkyn                                             ram-roc
8422 r»Y B, M, C                                                         twenty-first day of the month
                                 (f_ 'j •l_/^J*"-,)'^:>*~* **xl>.        Hen. JRAS 1945, 151.8; MDii, Nov. 6.13 p!86;
     ray (r'yh) ©ob. -y(hk pi. -t =>cyz r'yh
     plain, desert                                                         MDiii p65.1, 44.3, 31.3
     SCE 135; TSP 2.810; Hen. BSOAS 12, 307.36;                     8435 rW C                                            ju^T
       GMS 1205, 1661; STi 3321; Hen. LW 95; MDii                        rana     ©<*Av. rana\ Khot. rana\ Oss. ron
         B8-10 p47; Gersh. Melanges. p!95ff.                               ^n'kh
                                                                         belt
8423 r»Yh      B, S =* r>y
                                                                         BSTi 278; Gersh. JRAS 1946, 180; Bailey. AO
8424 r'YyCh) B                              >Sjj»<jM**^j                    1966, 34
     raye ©Khwar. ryYy                                                                                             XjjS
                                                                    8436 iVkh B
     wild, deserted
     SCE 39, 300                                                         ranak ^rW
                                                                         belt
8425 r>k M                                      J 'j
     rak ©<*rahaka\ Av. rar]ha\ Parth. rahg; MP rag                      VJ 41\ 984, 1167; Benv. "jewel"
       ©ob. pi. -tyy                                                8437 r'8 C
     vein                                                                ra8 (r>55(h)) ©ob. -y =^r>5(h)
      GMS 399; Hen. JRAS 1942, 232 n 6; BSOAS 12,                        road
        312.123; 11, 71.14; Sogdica. 56, 37                              GMS 222; STi 19.11, 31.9, 15, 36.14; BSTi 176; C2
8426 rWnd        M                                         <ll^>           gloss. p224; ry0y, 11V28, 12V17, 94R9, 10; r0 ?
                                                                           STi 17.1; Sund. AoFviii 1981 p217, AoFi 1974,
      ramand      (r*mn(d)t, rWnt) ^rWnty
      always                                                               9R1, 4V1; r><5, STSC 131.3
      GMS 434 n 2; KG 417, 421, 633; MSP bl28;                      8438 r't- B                {jj^ijz^j)^^/ t^J^
```


## [2026-09-14T02:29:43.668Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=28016 && /\\[pdf page/ {n=NR\": \"$0} END{print n}' SOD_pages.txt; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<28020' | tail -3",
 "description": "Find pdf page tag for SOD entry 8435"
}
```


### [2026-09-14T02:29:44.771Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:29:48.563Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" SOD_pages.txt | head -3; echo ---; python3 - <<'EOF'\nimport re\ntxt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# find form feeds\nidx=0\ncnt=0\nfor i,l in enumerate(lines):\n    if '\\f' in l:\n        cnt+=1\n        if i>28016:\n            print('leaf index at line',i,'count',cnt); break\nEOF",
 "description": "Locate SOD leaf for entry 8435"
}
```


### [2026-09-14T02:29:49.806Z] TOOL RESULT

```
---
leaf index at line 28038 count 405
```


## [2026-09-14T02:29:56.627Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sre[sš]k\\|sre.k\" SNS_pages.txt | head -20; echo \"=== SNS 183 ===\"; grep -n \"183\" SNS_pages.txt | head -5",
 "description": "Grep SNS for sresk"
}
```


### [2026-09-14T02:29:56.699Z] TOOL RESULT

```
=== SNS 183 ===
1637:                                                                                                                                                <   >^ t*;^ Hymn Cycles, 183)
3196:          (Man. Stud. 91)          xwb: jit (AtM).                        1833)hv-apah-: L.
3631:                              .<\/\o^UiVi. 1834) humayfl-
3648: .'^       Uitffc.   1832)sumatS-          :    ^     i5-^    hu-mata-                 :
3682:                        -If/IT^Mitffc- 1832)humatanam      1-                           i
```


## [2026-09-14T02:29:58.462Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v2 سرشک ===\"; grep -n \"سرشک\" BQT_v2_pages.txt | head -10; echo \"=== BQT v2 ران ===\"; grep -n \"^ران\\|(ران)\\|ران :\" BQT_v2_pages.txt | head -10",
 "description": "Grep Borhan-e Qate vol2"
}
```


### [2026-09-14T02:29:58.559Z] TOOL RESULT

```
=== BQT v2 سرشک ===
35264:            ‫وآن سرشکش برنگه تازسرشك»‪.‬‬                       ‫نگائته برشك‬            ‫ردخیزده‬
35266:                             ‫‪ -‬رك‪:‬سرشکوان ‪.‬‬  ‫‪ -‬رك س‪:‬رشکون ‪.‬‬
35272:‫است وآنرادای ترکی نیز خواند؛ ویکسر لول‬                    ‫باشد که‌در‬     ‫وآن برده‌ای‬       ‫اة‬    ‫سرشکوان‬        ‫نمی‬
=== BQT v2 ران ===
```


## [2026-09-14T02:30:03.272Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" BQT_v2_pages.txt | awk -F: '$1<35264' | tail -2; echo \"=== head of file ===\"; head -5 BQT_v2_pages.txt",
 "description": "Locate BQT v2 pdf page for سرشک"
}
```


### [2026-09-14T02:30:04.435Z] TOOL RESULT

```
=== head of file ===
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
```


## [2026-09-14T02:30:04.635Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sre\\|srê\\|sreshk\\|sri.k\" SNS.txt | head -20",
 "description": "Grep SNS.txt for sresk"
}
```


### [2026-09-14T02:30:04.688Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:30:08.138Z] TOOL CALL #29: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps(d,ensure_ascii=False,indent=1))\n\"",
 "description": "Read BQT ref details"
}
```


### [2026-09-14T02:30:09.291Z] TOOL RESULT

```
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
```


## [2026-09-14T02:30:13.446Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 583 584 585; do echo \"###### leaf $L (printed ~$((L+540)))\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -30; done",
 "description": "Print BQT v2 leaves near printed 1124"
}
```


### [2026-09-14T02:30:14.457Z] TOOL RESULT

```
###### leaf 583 (printed ~1123)
  ‫سرد ب‬                                                                                              ‫==‬

                        ‫کردن «م آهده است‪.‬‬                                                    ‫حمیرا کویند ‪۲ . ۱‬‬


‫د کنابه از کسی‌است که از‬     ‫سر خوش‬                      ‫و سکون را‬          ‫میم‬    ‫ه بفتح‬    ‫هرت‬      ‫سرح‬


‫شراب و سامان و اسباب و حسن» خوب و خوش‬                     ‫و آنرستنمی‌باشد‬         ‫‪ 3‬دال بی‌لقطه ‪a‬‏ نازك دناست‬

                                      ‫حال باشد ‪.‬‬          ‫که برکش ببر گهبتان افروزماند وساق آن‌سرخ‬

 ‫سر خه ‪ -‬بضماول وفتح‌خای نقطه‌رار(‪,)۲‬‬                                                    ‫‌‬   ‫خوشآ بنده بود ‪۴‬‬        ‫و‬



 ‫نام پسرافراسیاب‌است که فرامرز اورا زنده کرفت‬           ‫= بازای قطه دار (‪ )۱‬؛بر‬              ‫هرر‬      ‫سرح‬


‫وستم بکین سیاوشش بکشت ‪ -‬وام موضمی هم‬
                                   ‫ر‬                      ‫رستنیی‌باشدشبیه‬        ‫وزن و ععنی سرخ مرد است که‬
 ‫هست امزضافات سمنان ‪ -‬و نامنوعی اکزبوتر‬                                                             ‫بستان افروز ‪.‬‬


‫سرخیزه و سرخیژه * = بنم‌اول‬                               ‫ثالی و واو » بممنی سرخجه باشد ‪. ۴‬و آن‬
 ‫فارسی در‬  ‫و فتح زای هوز در لفت اول و زای‬                ‫اطفال را در بدن بهم‬             ‫تر‬
                                                                                          ‫بتشکه‬
                                                                                              ‫اس‬              ‫جوششی‬
‫لفت دوم ‪ ۰‬بممثی سرخجه است که نوعی از‬                                                                      ‫‪.‬‬    ‫رسف‬

###### leaf 584 (printed ~1124)
 ‫‪“NYY‬‬                                                                                                      ‫مردابه‬
            ‫و زودآورند و زود سازند ‪ ۴‬و‬
‫‪ -‬آنچه در دست‬                                            ‫سردا به‪ = ۱‬بفتح بای ابجد » بمعنی‬
‫بود وچوی که‬          ‫بوده باشد ‪ -‬وآ نجه برصر دست‬        ‫سرداب است که خالهٌ زیر زمینی باشد ‪ -‬و خانهةٌ‬
                         ‫قلندران بر دست گیر ند ‪۰‬‬
                                                          ‫ندا‪-‬م آبشاری‬    ‫ووبن‬
                                                                             ‫تابستانی بسیار سرد را نیز ک‬
                                                        ‫است درآب گرم قزوین ‪ -‬و نام جزیره‌است از‬
‫گرم شدن باشد ‪ -‬و کنابه از مردن ‪ -‬و ازکاری‬                                       ‫جزابر اندلی ‪#.‬‬
       ‫واسوختن و ملال بپمررسالیدن هم‌هست‪.‬‬                ‫»ابه‌ازمردم غیر ضیح‬
                                                                           ‫سرد لبان کن‬
‫وی؟ ه کنابه از کتدطبع ‪-‬‬        ‫سگرد‬                     ‫و کند طبع و کسیکه بمخنان راست مردم را‬
 ‫درشت‬     ‫و‬   ‫سخت‬    ‫دسخنان‬   ‫کسی که مردم را‬       ‫و‬
                                                           ‫یند ‪.‬‬
                                                               ‫وهم‬
                                                                 ‫ینگرا‬
                                                                     ‫مزو‬
                                                                       ‫برفجاند ‪ -‬و مردم نامو‬
 ‫واست برنجاند ‪ -‬و کنابه از مردم نماوزون‬‫ر‬                ‫سر در گلیم‪ -‬بکر کاف فارسی ‪ .‬نام‬
                                 ‫هم هت ‪.‬‬                 ‫درجاها‬       ‫عی‬
                                                                       ‫مکه‬
                                                                         ‫جشد‬
                                                                           ‫بازبی است » وآن چنان با‬
 ‫» سكرردة‬           ‫ه بفتح ثالك‬     ‫سدرور‬
                                                           ‫شخص‬
                                                             ‫بخوابند و چیزی برسر خود کشند و‬
                                                        ‫میدیده باشد » بامزدآن آن شخص سر درکنار‬
‫که بدان‬       ‫= بروزن ارده » قدح‬     ‫سر ‪3‬ه‬               ‫شخص دیگر نهدو آنهاییکه خوابید» بودندجاها‬
                                                        ‫را تفییر دهند و سر در کلم با لحاف کشند» بعد‬
‫شراب‌خورند ‪ -‬و سر کرده وپیشوای میخوار کان‬
###### leaf 585 (printed ~1125)
                                                                                                                         ‫‪٩۷۷۴‬‬

‫و زلد گی و تری‬                ‫و زای هوز ‪ ,‬کنابه از حات‬                                                       ‫وقصود است‪.‬‬
                                                                                                                      ‫از مدعا م‬
 ‫وناز کی عیش ‪ -‬وجوان صاحب دولت وکامکار ‪-‬‬
                                                                              ‫و معامله‬         ‫از سراسیمه شدن و ترك دادن م‬
                                                ‫‪۰‬‬   ‫باشد‬      ‫ویادشاه‬




 ‫سر سری = بر وزن مرمری ‪ ۰‬مردم‬                                                                                     ‫و مردن باشد ‪١‬‏‬
 ‫فرومایه راگوبند ‪ -‬و ست گرفتن‌کارها ورعایت‬
 ‫آا را بواجبی نکردن ‪ -‬وکار آسان‌باشد‬
                                   ‫حقوق ه‬                                                      ‫کار و مپم و مقصود ومدعا باشد ‪. ۳‬‬
‫بی فکر‬       ‫سڪخن‬      ‫و‬    ‫کنابه از کار پی تامل ‪-‬‬               ‫و‬   ‫_‬
                                                                             ‫سرر = بفتح اول و ثالی و سکون زای‬
‫الفهم‪ -‬واسب‌سربع السیر‬               ‫ربیهوده‌رخام ‪ 6‬وسر‬
                                                                             ‫انند که بنابان بدان کچ‬
                                                                                                  ‫شلددار (‪ » )۱‬ماله گرو‬
                                                         ‫‪.‬‬    ‫هم هت‬
                                                                             ‫هم‬   ‫نانی‬         ‫کون‬   ‫و‬     ‫مالد‬    ‫دبوار‬   ‫بر‬    ‫احكث‬       ‫و‬

‫نکر انی کنانه ازسوراخج‬                ‫سر سفر ‪= ۵‬‬
                                                                                                                           ‫گفته اند ‪.‬‬
                                                    ‫مقعد باشد ‪.‬‬
                                                                             ‫سر ژدن‪ -‬بر وزن کر کدن ‪ ۰‬بمعنی‬
‫سرسنه ‪ - ۷‬بکر اول و انی وسکون‬                                                 ‫سرزنش باشد ‪ -‬و بمعنی گردن زدن هم هست‪-‬‬
                                                                             ‫و بی رخصت واجازت وبی‌خبر و بك نگاه‌بشانه‬
                       ‫وبفتح اول هم بنظر آمده است‪.‬‬                                               ‫و مجلسی درآمدترا نیز گوبند ‪.‬‬
```


## [2026-09-14T02:30:21.377Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nlines=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\ncnt=0\nfor i,l in enumerate(lines,1):\n    if '\\f' in l:\n        cnt+=1\n    if i==35264:\n        print('leaf(0-based blocks before line):',cnt, '-> printed approx', cnt+540, cnt+541)\n        break\nEOF",
 "description": "Compute leaf for سرشک line"
}
```


### [2026-09-14T02:30:22.494Z] TOOL RESULT

```
leaf(0-based blocks before line): 584 -> printed approx 1124 1125
```


## [2026-09-14T02:30:27.701Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==586' BQT_v2_pages.txt | sed -n '1,80p'",
 "description": "Print BQT v2 block 586"
}
```


### [2026-09-14T02:30:28.830Z] TOOL RESULT

```
                                                                                                                         ‫‪٩۷۷۴‬‬

‫و زلد گی و تری‬                ‫و زای هوز ‪ ,‬کنابه از حات‬                                                       ‫وقصود است‪.‬‬
                                                                                                                      ‫از مدعا م‬
 ‫وناز کی عیش ‪ -‬وجوان صاحب دولت وکامکار ‪-‬‬
                                                                              ‫و معامله‬         ‫از سراسیمه شدن و ترك دادن م‬
                                                ‫‪۰‬‬   ‫باشد‬      ‫ویادشاه‬




 ‫سر سری = بر وزن مرمری ‪ ۰‬مردم‬                                                                                     ‫و مردن باشد ‪١‬‏‬
 ‫فرومایه راگوبند ‪ -‬و ست گرفتن‌کارها ورعایت‬
 ‫آا را بواجبی نکردن ‪ -‬وکار آسان‌باشد‬
                                   ‫حقوق ه‬                                                      ‫کار و مپم و مقصود ومدعا باشد ‪. ۳‬‬
‫بی فکر‬       ‫سڪخن‬      ‫و‬    ‫کنابه از کار پی تامل ‪-‬‬               ‫و‬   ‫_‬
                                                                             ‫سرر = بفتح اول و ثالی و سکون زای‬
‫الفهم‪ -‬واسب‌سربع السیر‬               ‫ربیهوده‌رخام ‪ 6‬وسر‬
                                                                             ‫انند که بنابان بدان کچ‬
                                                                                                  ‫شلددار (‪ » )۱‬ماله گرو‬
                                                         ‫‪.‬‬    ‫هم هت‬
                                                                             ‫هم‬   ‫نانی‬         ‫کون‬   ‫و‬     ‫مالد‬    ‫دبوار‬   ‫بر‬    ‫احكث‬       ‫و‬

‫نکر انی کنانه ازسوراخج‬                ‫سر سفر ‪= ۵‬‬
                                                                                                                           ‫گفته اند ‪.‬‬
                                                    ‫مقعد باشد ‪.‬‬
                                                                             ‫سر ژدن‪ -‬بر وزن کر کدن ‪ ۰‬بمعنی‬
‫سرسنه ‪ - ۷‬بکر اول و انی وسکون‬                                                 ‫سرزنش باشد ‪ -‬و بمعنی گردن زدن هم هست‪-‬‬
                                                                             ‫و بی رخصت واجازت وبی‌خبر و بك نگاه‌بشانه‬
                       ‫وبفتح اول هم بنظر آمده است‪.‬‬                                               ‫و مجلسی درآمدترا نیز گوبند ‪.‬‬
 ‫سرش د بکر اول وفتح ثانی وسکون‬
 ‫‪۰‬‬              ‫‪e‬‬                                   ‫‪‎‬ب‬

                                                                              ‫سرز لف = بکسر ثالی‌وضم‌ثالت‌وسکون‬
 ‫است‪.‬وآن مقنعه‬             ‫‪7‬‬    ‫سه‬    ‫شن قطه‌دار ز مخف‬                       ‫کرشمه‬       ‫لام و فا» کنانه از ناز وغمزه و عشوه و‬

‫و روپاکی باشد سه گز» چهرش‌بمه‌نی کزهمآ مده‬                                                                               ‫و عتاب باشد‪.‬‬
                                                                              ‫وه ‪7‬رن = بروزن ارزن » ‪:‬معنی‌سر کش‬
 ‫و آن آردی است که کفشگران و صحافان‬
                                                                                                   ‫باشد‬    ‫ودافرمان‬   ‫دده‬            ‫و عنان‬
 ‫وامثالایشان‌کار فرمابند ‪ - ۷‬وبلغت زلدویازند(‪)۷‬‬
‫بمعنی بد و زبون است که درمقابل ليك ولیکو‬                                          ‫ست‬
                                                                                   ‫یام‬
                                                                                     ‫هل‬‫اره»‬
                                                                                          ‫یزنجی‬
                                                                                              ‫کزن‌‬
                                                                                                 ‫سر ر لره » برو‬
                                 ‫باشدھ ‪.‬‬                                                                                       ‫خوشبوی ‪.‬‬
‫سر شاخ « بفتح اول و کرئالی و الث‬                                              ‫سرساد س با سین بی‌نقطه بروزن‌بفداد‪.‬‬
                                                                              ‫کاھی انت که نآرا شمانگتت کویند ‪ ۴‬ویترین‬
‫را‬    ‫‪ ۰‬بلندی‬       ‫دار رده‬    ‫شلد‬   ‫بشای‬   ‫و‬       ‫بالف کشیده‬


 ‫کوبند که بردو جاب‌پیشانی میباشد ‪ -‬وسکون‬
 ‫الی "چجوبی باشد دراز که بام خانه رابدان فوشند‬                                ‫چخماخ ‪ ۰‬ابرشم‬               ‫سرساخ ‪ -‬بورزن‬
                    ‫وسرهای آن از عمارت سرون باشد‪.‬‬                                                           ‫باريكك همواز راکوبند‪.‬‬

     ‫»معنی‬
         ‫سر شاد ‪ ۰ ۰‬بر وزن خروار ب‬                                            ‫سر سیژ‪= ۴‬بفتح الت و سکون‌بای ابجد‬
                                                ‫(‪ )۲‬چك ‪ :‬ژند ویاژند ‪.‬‬                           ‫(‪ )۱‬چك ‪ :‬وسکون زا‬
      ‫قی ‪ :‬سر رشته از دست رفتن ‪.‬‬                         ‫‪۴‬‬               ‫‪ - 8‬رك ‪ :‬سررسن بافتن » سر رشته یافتن ‪.‬‬
      ‫‪ - ۴‬رك‪:‬سرت سب باد‪.‬‬               ‫ورك ‪:‬پنج انگت‪.‬‬                    ‫‪۲‬‬    ‫بنجنگشت «لكث ص‬              ‫‪(6(6)1۷‬فر) =‬     ‫=‬     ‫‪۳‬‬

                ‫بابانیان سر سری ‪.‬‬            ‫سخن چون‬                              ‫نگت از سرداد ودين بروری‬                  ‫‪6‬‬
      ‫کنجینه ‪ » ۷۸‬خ‬        ‫نظامی کنجوی‪«.‬‬

      ‫‪#‬سروشنه؟و «اسروشنه»(ه‪.‬م‪).‬‬                 ‫‪ - ۹‬در حدود المالم ومعجم البلدان لیامده ‪.‬طاهراً مصحف‬
      ‫شاو (هم‪. ‎).‬‬         ‫از ‪ :‬مر‬     ‫‪- ٩‬‬           ‫‪.‬‬       ‫رك ‪ :‬سلش»سلیش‬          ‫‪۵۸‬‬     ‫‪2‬‬     ‫موش‬       ‫تو‬                    ‫‪۰‬‬    ‫است‬
```


## [2026-09-14T02:30:35.142Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==587' BQT_v2_pages.txt | sed -n '1,90p'",
 "description": "Print BQT v2 block 587"
}
```


### [2026-09-14T02:30:36.193Z] TOOL RESULT

```
   ‫)‪۷۱‬ات‬

‫که بجمد و جهنده باشد ‪ -‬و نام درختی است‌در‬           ‫بمعنی ربختن باشد ‪-‬ویمعنی‬         ‫ر‬
                                                                                     ‫شتاچه‬
                                                                                         ‫لبریز اس‬
   ‫آردثور‬
        ‫بلخکه کلهای سفید مابل بسرخی دا‬
‫و کی گونند کل ان‬          ‫آزاد درخت ءیگوند‬
                                                    ‫سر شب = بروزن هرشب ؛ بمعنی‌شاهین‬
                       ‫درخت سر شك نام دارد ©‬
                                                                    ‫باشد وآن جالوربست شکاری ‪.‬‬
 ‫سر شك ‪ ۲‬تش ه کنابه از فطرحامی‬                      ‫بکر اول و انی بر وزن‬            ‫سر شت ‪۲‬‬
          ‫می‌چکد‪.‬‬    ‫است که از هیزم تر اش‬           ‫بهشت ‪ ,‬خلقت و طیئت و هاب طبع و طبیمت ‪۴‬‬
 ‫ترشی‬   ‫کنابه از‬    ‫انگیین =‬     ‫‪2‬‬                   ‫غطشوته‬
                                                          ‫وخوی آدمی راگویند ‪ -‬وبمعنی مآخلو‬
                                                                ‫و ماضیآغشته کردن هم حست‪* .‬‬
 ‫رسکه‬
    ‫چواشنیی است که مرکب ازآب وعسل و‬
               ‫باشد ‪ -‬و دوشاب را نبزگفته‌اند‪.‬‬      ‫ثالث بروزن فرقف ‪ .‬نام‬           ‫ح‬
                                                                                   ‫ففت=‬
                                                                                      ‫رش‬‫سب‬
‫سرشك شور ‪ -‬بکسکان‪ .‬کناب‬                            ‫غله‌ایت شبیه بخردل که روغن تلخ از آن کبرند‬
                                                                     ‫میباشد‪.‬‬        ‫سدروخ‬
                                                                                        ‫وکل او زر‬
                       ‫اازشك غمزدکان باشد‪.‬‬
                                                    ‫زرشث‬      ‫عننوی‬
                                                                  ‫موز‬
                                                                    ‫سر شك = بر‬
 ‫سشرکوان ‪ - ۱‬بکر اول ثوالی‬
‫وابع و واو بکالشفیده و بنونِ‬
                           ‫وکون ثالث ر‬
                                     ‫س‬
                                                      ‫یرس‬
                                                        ‫ارمیرالب‬
                                                               ‫بهبع‬
                                                                  ‫باشد‪ , .‬وآن لباتی‌است «عروف ک‬
                                                     ‫گوبند ‪ .‬و فانق آشپا کنند ؛ و بعضی ررخت‬
‫ه‌ای را کویند که درشب زفاف پیش‬
                             ‫زپدرهد»‬
                                                    ‫و بوتهٌ زرشك را سرشك میگوبند ‪ - ۴‬و مطلق‬
         ‫عروی بیاویززند ونآرا بعربی کله گویند‪.‬‬
                                                    ‫قطره را گویند عموماً و قطر۾ء باران و اشك‌چشم‬
 ‫سر شکون ‪ -‬بفتح واو و سکون نون»‬                     ‫را خصوصا ؟ ‪ -‬و بمعتی شراره و خرو آمشی‌بود‬
    ‫‪ ۱‬فی ‪ :‬اففالی ‪( 1151715) , 1‬طبیمت‪ ,‬مزاج)‪ ( 0156۳25 ,‬سریش‪,‬چسب‪.‬‬
   ‫چبن دگی) = ‪.60۳56125 , 7 . 58125‬ءعنی که تزددك است به ‪ ( 051۲۲ ۱ :‬بستن»‬
   ‫متحد کردن » متصل کردن) قی ‪ :‬ساف کریت ‪îrç‬‏ (آمیختن › مخلوط کودن) ‪.‬فارسی ‪ :‬سرشتن‪.‬‬
   ‫( ‪ ,‬فارسی ‪ :‬سرش‬      ‫)‪.‬اوستا ‪hsirs‬‏ (چبدن‬      ‫«( مالکرت ‪hsilç‬‏ ( آویزان بودن ۽ چبیدن‬
  ‫‪ 9۱‬گرچه سرشت رو ز گار برآن جماه آمد که‬             ‫‪۳‬‬         ‫ورك ‪ :‬سرشتن *‬        ‫«‪+‬هوشمان ‪۲۳۷‬‬
        ‫‪ = ۴‬زرشك («م‪. ).‬‬            ‫هیج فرزلد پند پدر خویش را د«رقنباندبد‪.‬و»سنامه ص ‪. ۱‬‬
   ‫ورك‪ :‬هویشمان ‪۳۳۷۰‬‬      ‫‪- ۴‬اوستا _ ‪(86158]5‬نگ رکه) ‪ ۶‬بارتولمه ‪« ۵۸۹۱‬اسشق ‪۳۳۷‬‬
                                                ‫سرشك فارسی شابد از پارتی ‪( 5۲5‬قطره) باشد ‪:‬‬
            ‫‪Henning, A list of Middle ۳6۲5۱۵9... BSOS, 126,1,‬‬                           ‫‪۰‬‬
   ‫درپهلوی )‪ ( 181۲5‬قطره ) « تیبرکه ‪ « . » ۹۰۲‬زرشك و سرشك » انبرباریس بود »‬
   ‫‪«- ۵‬سرشك‪ .‬قطرء آب چشم بود » وبکی کلی بود که پاره‌ای بسرخی‬                        ‫«لفت فری‪.*۹۰۳‬‬
   ‫زد ‪«,‬دیگر درخت کل رائیز کوبند وآزاد درخت‌بیزش کوبند ‪ .‬دبگر قطرة باران وقطر‪ :‬هرچیز‬
                                                                  ‫بود ‪ .‬عنصری (بلخی) کوبد ‪:‬‬
            ‫وآن سرشکش برنگه تازسرشك»‪.‬‬                       ‫نگائته برشك‬            ‫ردخیزده‬
   ‫« لفت فری ‪٩۲‬‏ © ‪.‬‬                                                           ‫‪۱‬‬
                             ‫‪ -‬رك‪:‬سرشکوان ‪.‬‬  ‫‪ -‬رك س‪:‬رشکون ‪.‬‬
  ‫کن اول و دوم ِ ِِِ ب>هلوی ‪[ 881215۳5‬رك‪ :‬سرشت ]ه‬ ‫کک ‪-‬‬
        ‫سر دکلنی ‪ma-xrix‬‏ ( آمیختن‪ .‬مخلوط کردن) «اسدق‪ -‬هویشمان ‪ ۲۷۷‬؛مخلوط کردنا‬
                                                         ‫ساختن ‪ -‬خمیر کردن ‪ -‬معجون ساختن ‪.‬‬
```


## [2026-09-14T02:30:51.189Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for B in 393 394; do echo \"##### block $B (printed ~$((B+539)))\"; awk -v n=$B 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | sed -n '1,80p'; done",
 "description": "Print BQT v2 blocks near printed 932"
}
```


### [2026-09-14T02:30:52.234Z] TOOL RESULT

```
##### block 393 (printed ~932)
 ‫~‪“r‬‬                                                                                                                       ‫رامشگر‬
 ‫رامیتن ‏ د با ثالث بتحتالی مجهول‬                                                                          ‫ا‬
                                                                           ‫رمشگر ه باکاف‌فارسی‌برو‪ :‬نیداشور‪,‬‬
 ‫رسیده وفوقانی مفتوح بنون زده » نام قصبه‌ایست‬                              ‫مطرب و خنیا کر راکوبند که خواننده وسازنده‬
‫از ولایت بخارا‪.‬و خواجه على رامیتنی که از‬                                                                                     ‫باشد ‪.‬‬
‫کمل اولیاست وبحضرت عزبزان اشتهار دارد از‬                                 ‫بکرثالث ورابع وسکلون‬             ‫رامشی؟ ‌‬
                                                ‫آلجاست ‪.‬‬                   ‫که ساز نده وخواننده‬      ‫تحتالی؛ بمعنی راه‌شگراست‬


‫رامین = بائالث بتحتانی رسیده وینون‬                                                                                           ‫باشد ‪.‬‬
‫زده ‪ ۰‬نام عاشق وس است و قصه وبس وراهین‬                                     ‫رامك = بفاح‌الت و‪‌-‬کون‌کاف؛ مصغر‬
‫مشهور انت ‪ - ۷‬و نام چنگه نوازی هم بوده‬
                                                                               ‫از زاج یاه ومازو وپوست انار وصمغ د‬
                                                                           ‫ووشاب‬
                                                                                    ‫ان دفع اسپال کند ‪۰‬‬        ‫انگوری که خوردن‬
‫رامینه ‪ = ۸‬بامیمبروزن خاگینه ‪.‬‬
                      ‫رامین است که عاشق وبس باشد‪.‬‬                          ‫رامور = با زای نقطه دار(‪ )۱‬بر ورن‬

 ‫ران = بر وزن جان ‪ .‬معروف است‬                                                   ‫ناموس » کشتی‌بان وناخدا گروایند ‪.‬‬
‫گویند ‪٩‬‏ ‪ -‬ودرخت الگوزه را یز‬
                            ‫ذخ‬‫و عربی ف‬                                 ‫رام هرهز » بسکون الك وضم ها‬
 ‫گونکہ وبوا گی سے نة انت کات‬                                               ‫ورای بی‌نقطة ساکن ومیم مضموم بزای نقطه‌دار‬
                                                        ‫باشد ‪.‬‬          ‫زده * نام شهری است از اهواز و آنرا در قدیم‬
‫رانا د بروزن داناء بلغت بونایی انار‬
                          ‫باشد که بعربی رمان خوانند ‪.‬‬                      ‫داهی؟ = بروزن‌جامی‪ ,‬امشخصی است‬
 ‫ران افشردن‪ -‬کنابه از نیز کردن‬                                             ‫که واضع چنک بوده وآن سازی است مشهور‪.‬‬
‫و برانگیختن ‪ka‬‏ عموماًء وبرانگیختن اسب را‬                                  ‫رامیار = بباای حطی (‪ )۲‬بر وزن‬
                                           ‫گونشد خصوصا ‪.‬‬                            ‫کامگار » شکباونسوفند چرانرا گوبند ‪۰‬‬
                                                          ‫(‪ )۲‬چك ‪ :‬با با‪.‬‬                        ‫(‪ )۱‬چك ‪ :‬بازا ‪.‬‬

                                                                      ‫‪ - ۱‬از ‪ :‬رامش ‪ +‬کر (یوند شغل) ‪:‬‬

                   ‫که رامش نود نزد رامشگران‪.‬‬                                        ‫ز رامشگران رامشی کن طلب‬
  ‫‪.‬‬     ‫‪۲‬‬       ‫دامغانی‬    ‫منوچهری‬     ‫‪2‬‬


  ‫>‬    ‫‪۸‬‬        ‫المالم ‪۳‬‬   ‫» حجدود‬    ‫رام اورمزد‬          ‫‪۳‬‬
                                                                               ‫(نت) ‪۰‬‬         ‫از ‪ :‬رامش ‪+‬ی‬             ‫‪۴‬‬
      ‫‪.‬و لف مجمل التواریخ و القصص (ص‪)٩۲‬‏ دکررنشهرهای‌بنا کرد اردشیر بابکان گوید‪ « :‬رامهرمز‬
            ‫‪۱‬‬                        ‫ار«شیر[ و ] آن رامز است ‪ ».‬و اکنون مردم محل ‪ 2601031‬گوبند ‪.‬‬
            ‫نود وچهار‪.‬‬      ‫‪ .‬رك ‪ :‬مقدمه‌ص‬     ‫درسر حد توران نوده‬               ‫«سمتگان»‬       ‫‪۴‬‏ "‪ E‬بتر بح شاهنامه‬

  ‫رامیئن ‪ ۲‬قربه‌ای به‌شاراً *معجم البلدان‪5 ‎‬‬                     ‫سه‬    ‫‪٩‬‬              ‫‪.‬‬   ‫رام رامی»ء رامتن‪‎‬‬    ‫رك‪:‬‬     ‫‪e‬‬


                                       ‫‪۰‬‬   ‫رامشن‪‎‬‬   ‫‪.‬‬   ‫راعی‬     ‫>‬    ‫‪ :‬رام‬    ‫ره‬    ‫‪۸‬‬             ‫‪ :‬رام ی‪‎‬‬   ‫رك‬   ‫‪.‬‬   ‫‪۷‬‬


   ‫‏‪ - ٩‬اوسا ‪ ( 80۵۲ -‬ران ) * پهلوی ‪ . 0۲‬ارمنی ع ‪ 03۲6۰‬کردی و بلوچی ع‬
  ‫تپرالی ‪nûr‬‏ ‪ .‬گیلکی‬                ‫افغانی ‪nÛrv‬‏ » اسشق ‪٥0‬‏ ‪ ,‬طبری ‪nûr‬‏ «صاب طبری ‪۷۹۳۰‬‬                                      ‫‪02‬‬

      ‫‪ °‬لاتینی ‪( 0۳110202۳26‬وکمةٌ ‪ 01101201‬در آن مستتر است ) یعنی سیب‬                                                       ‫‪. ۳‬‬
                                                                              ‫‪. €‬‬   ‫بزرگه ‪edanerg :‬‏‬           ‫دار «لاروس‬     ‫داله‬

##### block 394 (printed ~933)
  ‫رارز‬                                                                                            ‫‪- ۳۳‬‬

     ‫هم بنظرآمده است که بروزن فلولا باشد ‪.‬‬                 ‫رانج! = بفتح لون وسکون جيم » به‬
‫راوش؟ ه بفتح الكت بروزن آش ‪.‬‬                               ‫آتبکرها جوزهندی کونند‪* .‬‬
                                                                                  ‫رنیکنیال اس‬
                                                                                            ‫مع‬
                      ‫کوکب مشتری رگاوند ‪۰‬‬
                                                          ‫رانش؟ ب=روزن داش» بمعتی راندن‬
‫ولطیف‬    ‫ناوك ‪ ۰‬صاف‬    ‫‪:‬ر وزن‬    ‫=‬   ‫راوك‬                  ‫ودور کردن باشد وترجمة سلب در مقابل ایجاب‬
  ‫ویالودة هرچیز باشد ‪ ,‬ومعرب آن راوق است ‪.‬‬                                                ‫هم هت ‪.‬‬

‫راوماده = بکر الكت بر وزن کاو‬
                                                           ‫طاهر‬    ‫وعت‬     ‫وراه رفتن وفرودآمدن از مر کب‬

                  ‫تالت هم بنظر ا مده است ‪۰‬‬       ‫رضم‬                     ‫کردن ‪ -‬وبرهنه شدن باشد ‪.‬‬
                                                           ‫رانين » با نون بتحتانی ريده و نون‬
‫راو نك د بنتح‌نالك وسکون دون ودال‬
‫ایجد » رسمالی باشد که خوشهای انگور برآن‬                    ‫دیگر زده » بمعنی شلوار باشد و بعربی رانان‬
                                                             ‫رائیز گفته‌اند که ازز وة‬       ‫وزرهی‬      ‫گوشد‬
‫آویزند وجامه وفوطه و ازار ولنگی وامتال آن‬
                                                                                         ‫رالها را پپوشاند ‪. ۴‬‬
‫بر بالای آن انداز ند ‪ - 1‬وتام جابی‌است از توایع‬

 ‫قزوین ‪ ۷‬و راوندی منوب بلاجاست ‪ -‬وریوند‬                   ‫راو حه = بر وزن لاوچه » بوعی از‬
‫را نیز بندوآن دوابی است مشهورومعروف ‪.۸‬‬                                                          ‫انگور باشد ‪.‬‬
‫کوبندربوندبیخ‌ربوای‌است وآن‌چینی وخراسالی‬                  ‫راود = بفتح واو بروزن آمد ؛ زمین‬
 ‫میباشد‪ .‬چینی رابجهت‌مردمان وخراسالی رابرای‬                 ‫ویلند وشته يشته پرآب وعلف را كو‬               ‫بت‬

‫دران و ‪-‬خبپازبانان‪ :‬دنکن انتمنان‪ .‬کته ‪:‬‬                            ‫‪۰‬‬   ‫را هم گفتهارد‬   ‫وت رگی آب‬     ‫تاصافی‬   ‫و‬


‫‪ ۶۱‬ر یو ند لحمی‬   ‫و چىئى‬   ‫راوند الدواب‬   ‫خراسائفرا‬
                                                           ‫راودا ‪ = ۴‬بسکون‌نالت ورای بی‌نقطه‬
                                           ‫کویند ‪.‬‬         ‫بالف کشیده بروزن چاربا ‪ ۰‬خاریشت را گونند ‪۰‬‬

‫دراو یز = بوااو بر وزن فالیز ‪ ۰‬علف‬                         ‫وآن جالوربست ممروف ؛ و بفتح اول و ثالی‬

   ‫از ‪ :‬ران (راندن) ‪+‬ش‬           ‫‪۴‬‬             ‫‪( 0606 = ١‬فر) ‪ ,‬تارجیل « لك‪ ۲‬ص‪۱۹۷ ‎‬‬
 ‫‪ « - ۴‬چون رود کی بدین بیت رسید» امیرچنان منفعل کشت‬                                    ‫( پوند اسم مصدر) ‪.‬‬

  ‫سخارا نهاد چنانکه رائن‬        ‫فوشی وزو وروی‬          ‫که از تحت فرود آمدویی دوزه بای در رکاب گت‬


  ‫‪ ۴‬ره‪ :‬ژرژه ‪.‬ژوژ‪.‬‬                   ‫وموزه تا دو فرسنك‌در یی اهیر بردند به برونه » « چپارمقاله ‪۳۳‬‬
                                 ‫‪.‬‬   ‫ح‬   ‫‪۵۵۳‬‬     ‫چك ص‬    ‫) ورك ‪:‬‬   ‫» ( ه‪.‬م‪.‬‬   ‫« زاوش‬   ‫ممحف‬


 ‫‪ - ۲‬شهر کی زدیك کاشان‬                    ‫‪. ).‬‬   ‫(ه ‪.‬م‬    ‫آوند »‬   ‫وصرفی در «‬     ‫ظ‪ ,‬صحیف‬        ‫‪۱‬‬

   ‫واصفهان‪ .‬حمزه (اصفهانی) گوبد ‪ :‬اصل‌آن «راهاوند» بمعنی (خیر مضاعف) است «معجم‌البلدان»‪.‬‬
                             ‫«دزیح س ‪1٩4۰۰‬‏‬              ‫‪( 6۵۲2۵0۱۲ = ۸‬فر) «لك‪ ۲‬ص‪۵۱‬‬
   ‫* رالدن ‪ -‬بفتح چهارم ‪ ۰‬محشاف فرواندن» منمدی «رفتن ‪ «€‬فیس ‪ ۱‬کاشالی ‪ 7‬زفره ی‬

  ‫‏‪ . bérãbt . bérãwên . bérãw‬بهلوی ‪natînîydr‬‏ ‪ nhs)i(niyãT« . ۵81۷۵۲ ۰‬روشن‬

    ‫ست‪ * .‬اسشق‪ :»۰۱‬کخرادرنج»ببرون کرد ‪-‬ن دکقردعنه اغراجبلدکردن‪ ,‬مرکدورددن۔‬
 ‫‪ ۰‬اعتغال داشتن ‪;0D‬‏ هیچ حال ننده بدرگاه تباید وشفل وزارت براند که‬                 ‫ورزسن‬    ‫آوردن ك‬   ‫اسهال‬


                                     ‫استضفاف چنن قوم کشیدن دشوار است » « تاریخ بیهقی ‪٩۵۱‬‏ * ‪.‬‬
```


## [2026-09-14T02:31:11.722Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"sherbet[^.]\\{0,400\\}\" KLN_1966.txt | head -5; echo \"=== syrup ===\"; grep -n -o \"syrup[^.]\\{0,500\\}\" KLN_1966.txt | head -8",
 "description": "Grep Klein for sherbet and syrup"
}
```


### [2026-09-14T02:31:13.431Z] TOOL RESULT

```
34962:sherbet,  n
34962:sherbet,  fr
35085:sherbet
35355:sherbet  and  cp
35953:sherbet
=== syrup ===
35355:syrup,  n
35355:syrupus,  fr
35356:syrup-y,  adj
37932:syrup,  n
37933:syrup,  tr
37933:syrup-y,  adj
```


## [2026-09-14T02:31:16.127Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '34960,34966p' KLN_1966.txt; echo \"=== syrup ===\"; sed -n '35350,35360p' KLN_1966.txt; echo \"=== 35080 ===\"; sed -n '35082,35090p' KLN_1966.txt",
 "description": "Read Klein sherbet and syrup entries"
}
```


### [2026-09-14T02:31:16.248Z] TOOL RESULT

```
Derivatives:  shepherd,  tr.  v.,  shepherd-ess,  n. Shepherdia,  n.,  a  genus  of  plants  (hot.)  —  ModL., named  after  John  Shepherd,  curator  of  the  Bo¬ tanic  Garden  in  Liverpool  (1764-1836).  For  the ending  see  1st  suff.  -ia.
Sherardia,  n.,  a  genus  of  plants,  the  field  madder ( bot .)  —  ModL.,  named  after  the  English  bot¬ anist  William  Sherard  (1659-1728).  For  the ending  see  suff.  -ia.
Sheraton,  adj.  —  Made  in  the  style  of  the  cabinet¬ maker  Thomas  Sheraton  (1751-1806). sherbet,  n.,  a  drink  made  of  diluted  fruit  juice and  sugar.  —  Turk.,  Pers.  sherbet,  fr.  Arab. shurbu",  ‘one  drink’,  fr.  sharab,  ‘drink,  beverage’, fr.  shariba,  ‘he  drank’,  which  is  rel.  to  Mishnaic
Heb.  sdraph ,  ‘he  absorbed,  sipped,  sucked’.  Cp. sirup,  shrub,  ‘a  drink’,  sorbet  and  the  second word  in  loll  shraub.
sherd,  n.,  a  fragment.  —  A  var.  of  shard, shereef,  sherif,  n.,  1)  a  descendant  of  Mohammed through  his  daughter  Fatima;  2)  the  governor of  Mecca.  —  Arab,  sharif  (in  vulgar  pronuncia¬ tion  sherif),  ‘noble’,  fr.  sharafa,  ‘he  was  exalted, was  noble’.  Cp.  ashrafi,  tashrif,  xerafim. Derivative:  shereef-ian,  sherif-ian,  adj. sheriff,  n.  —  ME.  shereve,  fr.  OE.  scir-gerefa, ‘president  of  a  shire’,  which  is  compounded  of scir,  ‘shire’,  and  gerefa,  ‘officer,  governor’.  See shire  and  reeve,  ‘official’.
Derivatives:  sheriff-ess,  n.,  sheriff-dom,  n., sheriff-ry,  n.
sherry,  n.  —  Back  formation  fr.  earlier  sherries (which  was  mistaken  for  a  plural),  fr.  Xeres  (pro¬ nounced  sheris),  now  spelled  Jerez  (de  la  Fron- tera),  a  town  near  Cadiz,  Spain,  fr.  L.  ( oppidum ) Caesaris,  ‘(the  town)  of  Caesar’.  Hence  sherry prop,  means  ‘wine  of  Jerez’.  For  similar  back formations  cp.  pea  and  words  there  referred  to. shew,  v.  —  A  var.  spelling  of  show, shewbread,  n.  (Jewish  Religion).  —  Coined  by Tyndale  on  analogy  of  G.  Schaubrot,  which  it¬ self  was  coined  by  Luther  as  a  loan  translation of  Heb.  lehern  ( hap-)panim ,  lit.  ‘the  bread  of  the Divine  presence’,  fr.  lehem,  ‘bread’,  and  panim, ‘face;  presence’.  See  Ex.  25  :  30.
=== syrup ===
Sirius,  n.,  the  Dog  Star.  —  L.,  fr.  Gk.  Ssipto;, lit.  ‘hot,  scorching’.  See  siriasis.
sirloin,  n.,  the  loin  of  beef,  or  a  part  of  it.  —  A var.  spelling  of  surloin,  lit.  ‘the  upper  part  of  the loin’,  fr.  OF.  surlogne,  surlonge  (F.  surlonge), from  sur,  ‘above’,  and  logne,  longe  (F.  longe), ‘loin’.  See  sur-  and  loin.
Derivative:  sirloin-y,  adj.
sirocco,  n.,  a  hot  wind  blowing  from  the  Lybian deserts.  —  It.  sirocco,  scirocco,  dissimilated  fr. VArab.  shoruq,  'the  east  wind’,  fr.  Arab,  sharqi, ‘eastern;  east  wind’,  fr.  shdraqa,  ‘he  cleft,  dis¬ sected;  rose’  (said  of  the  sun).  Cp.  Saracen, sarcenet,  sarsen,
sirrah,  n.,  a  term  of  address  used  to  men  or  boys, expressing  anger  or  contempt  (obsol.)  —  Alter, of  sir.
sirup,  syrup,  n.  —  ME.  sirop,  sirup,  fr.  OF.  (=  F.) sirup,  fr.  ML.  sirupus,  syrupus,  fr.  Arab,  sharab, ‘drink,  beverage’,  from  the  stem  of  shariba,  ‘he drank’,  whence  also  Sp.  jarabe,  jarope,  and OProven?.  eissarop.  It.  sciroppo  is  also  borrowed fr.  ML.  sirupus.  See  sherbet  and  cp.  shrub,  ‘a drink’,  sorbet,  and  the  second  word  in  loll shraub.
Derivative:  sirup-y,  syrup-y,  adj.
sirvente,  n.,  a  kind  of  medieval  Provencal  song. —  F.,  fr.  Provenc-  sirventes(c),  ‘a  kind  of  song’, prop,  ‘a  song  referring  to  service’,  fr.  sirven, ‘serving’,  pres.  part,  of  servir,  fr.  L.  service,  ‘to serve’.  See  serve.
sis,  n.,  a  girl  ( colloq .)  —  Abbreviation  of  sister. Cp.  sissy.
-sis,  suff.  in  nouns  of  Greek  origin  denoting  ac¬ tion,  process,  state,  condition.  —  Gk.  -015,  iden¬ tical  in  meaning  with  L.  -entia  (whence  E.  -ence) and  with  E.  -ing.  Cp.  -asis,  -esis,  -osis.
sisal  grass,  sisal  hemp.  —  Named  after  Sisal,  a seaport  in  Yucatan.
=== 35080 ===
of  shrove ,  a  noun  which  is  related  to  shrive  (past tense  shrove ),  and  of  tide.
Shrove  Tuesday,  n.  - —  See  Shrovetide;  so  called from  the  custom  of  confessing  sins  before  Ash Wednesday.
shrub,  n.,  a  low  woody  plant.  —  ME.  schrubbe, schrub,  shrub ,  fr.  OE.  scrybb,  ‘underwood’,  rel. to  dial.  Dan.  skrub,  ‘brushwood’,  Norw.  skrubba, ‘a  dwarf  cornel  tree’.  Cp.  scrub,  ‘a  stunted  tree’. Derivatives:  shrubb-ery,  n.,  shrubb-y,  adj., shrubb-i-ness,  n.
shrub,  n.,  a  drink.  —  Arab,  shurb,  ‘a  drink’,  form¬ ed  from  the  base  of  shariba,  ‘he  drank’.  See sherbet.
shrug,  tr.  and  intr.  v.  —  ME.  schruggen,  of  uncer¬ tain  origin.  Cp.  Dan.  skrugge,  ‘to  stoop, crouch’.
Derivative:  shrug,  n.
shrunk,  pp.  of  shrink.  —  ME.  shrunke,  shrunken, fr.  OE.  gescruncen,  pp.  of  scrincan.  See  shrink, shrunken,  adj.  —  Old  pp.  of  shrink.  See  prec. word.
shruti,  n.  —  See  sruti.
shuck,  n.,  husk,  shell.  —  Of  uncertain  origin. Derivative:  shuck,  tr.  v.
```


## [2026-09-14T02:31:26.459Z] TOOL CALL #37: Bash

```json
{
 "command": "ls site/pages/472.jpg 2>/dev/null; pdftoppm -f 472 -l 472 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg472 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg472.png",
 "description": "Render PDF page 472"
}
```


### [2026-09-14T02:31:28.112Z] TOOL RESULT

```
site/pages/472.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 60397 Sep 13 22:31 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg472.png
```


## [2026-09-14T02:31:29.923Z] TOOL CALL #38: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg472.png"
}
```


### [2026-09-14T02:31:30.435Z] TOOL RESULT

```

```


## [2026-09-14T02:31:30.422Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:31:48.345Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 472 -l 472 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg472hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg472hi.png')\nprint(im.size)\n# region around root/arabic/latin left column: original 1700x2200 at 200dpi -> 400dpi is 3400x4400\nim.crop((650,350,1400,1300)).save('pg472-crop.png')\n\"",
 "description": "Crop left column of page 472"
}
```


### [2026-09-14T02:31:51.439Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-14T02:31:53.553Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg472-crop.png"
}
```


### [2026-09-14T02:31:53.577Z] TOOL RESULT

```

```


## [2026-09-14T02:32:08.994Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT scherbet/sirup ===\"; grep -n -i \"scherbet\\|sirup\\|sorbet\" LKT.txt | head -20; echo \"=== DEV/PHN sirop ===\"; grep -n -i \"sirop\\|sorbet\" DEV.txt PHN.txt | head -20",
 "description": "Grep Lokotsch, Devic, Pihan"
}
```


### [2026-09-14T02:32:09.068Z] TOOL RESULT

```
=== LKT scherbet/sirup ===
732:2'i7.  Ar.  barbäris: [Entstanden  aus  nnnr  hüris  über  ambar bäris,  vgl.  FLEISCHER  in  BSGW  phil. bist.  Kl.  1881,  XXXill,  9]  'eine  Pflanze Berberis  vulgaris',  deren  Beeren  zu  Mar- mel.ide,  Sirup  oder  Eis  verarbeitet  wer- den; die  Apotheker  benutzen  ihre  Wur- zalrinde;  zuerst  wurde  die  Pflanze  von den  Arabern  verwertet.  Frz.  berberis, engl,  barberry  [aber  berberine  'die  dar- aus gewonnene  Substanz  zum  Gelb- färben'], dtsch.  Berberize,  Berberstaude, Berberisbeere.  Russ.  barbaris  'Sauer- dorn'.
1808:742.  Pers.  guläb: 'Rosenwasser'  [aus  pers.  gul  'Rose',  s. hier  Nr.  740,  und  ab  'Wasser',  s.  hier Nr.  5],  ebenso  ar.  guläb,  vulg.  guleb; hieraus  m\2L\..  jidapium  'eine  Art  Sirup, Kühltrank',  li.giulebbe,  giulebbo,giuleppo,
3353:'Zucker'  [nach  DE  164];  hieraus  sp.  kat. almibar  'Sirup',  almibarar  'mit  Zucker- seim überziehen,  süße  Worte  geben', almibarado  'süßtuender  Mensch'.  — [Eguilaz  222  hat  als  Grundwort  miba.'
4167:'Trank'  [Vb.  sariba  'trinken'],  hieraus mlat.  siröpus,  sirüpus,  it.  sciroppo,  si- roppo,  frz.  sirop,  syrop,  prov.  isarop, kat.  aixarop,  sp.  jnrope,  pg.  xarope, enxarope,  rum.  sirop,  sirup;  ndl.  siroop, stroop  [in  Südhmburg  dial.  sroep,  vgL GRM  V,  171],  dtsch.  Sirup,  engl,  syrop, syrup;  russ.  sirop,  serb.  sirup,  äech. syrup,  poln.  syrop.  —  Aus  der  gleich- bedeutenden ar.  Form  surba,  sarba wurde  zur  Bezeichnung  eines  kühlenden Trankes  über  tk.  serbet  'Kühltrank'  it. sorbetto  'süßes  Fruchteis'  [mit  Einwir- kung von  it.  sorbire  'schlürfen'],  frz. Sorbet,  sp.  sorbete,  pg,  sorvete,  rum.  ger- bet 'dicker  Obstsaft';  ndl.  sorbet,  engl. sherbet,  shrub,  dtsch.  Sorbet,  Scherbet 'ein  aus  Wasser,  zerstoßenen  Rosinen, Zucker,  Zitronensaft,  Ambra  und  ähn- lichen Zutaten  gemischter  Kühltrank'. [DE  218  und  417.  Eguilaz  495  und  513. ML  7675  und  7711.
7200:somaro  1883 '  sommaco  1946 !  sorbetto  1838 I  sor^o  551 I  spinace  126 !  sia^cMO  2017 j  stambecco  1740
7448:sapphirus  1830 saraballa  1849 Saraceni  1856  c sarrabarrae  1849 satanas  1867 satureia  1872 scarlatum  1794 Seraphim  1885 Äeres  1878 sericus  1878 seto  1878 sicera  1787  a siclus  1880 Signum  1896 s/nws  641  b Sir  opus  1838 sirupus  1838 soccus  1782 stagnum  2017 stibium  918 syrma  1820
8789:sirup  1838
9711:Sirup  X.OOO
=== DEV/PHN sirop ===
PHN.txt:7864:fait une pâte et un sirop employés avec succès contre les ma-
PHN.txt:9200:SIROP, s. m. (a.)
PHN.txt:9209:quent usage en été pour se rafraîchir. — Voyez Sorbet.
PHN.txt:9280:SORBET, s. m. (a.)
PHN.txt:9286:d'œtl, que sorbet dérive du substantif latin sorbitio, qui se rat-
PHN.txt:9289:— Comparez aussi l'italien sorbetto et l'anglais slierbet.
PHN.txt:10875:Sirop, s. m. (a.) 336
DEV.txt:1259:Dans  la  terminologie  pharmaceutique,  éhxir  a  subi  une déviation  de  sens  analogue  à  celle  d'alcool;  le  mot  ne  se dit  plus  aujourd'hui  que  de  liqueurs  résultant  d'un  mé- lange de  certains  sirops  avec  des  alcoolats.
DEV.txt:1593:Kaïmac.  Sorte  de  sorbet  turc.  Le  mot  turc  (^i  ou  (^}:i qdimnq  signifie  proprement  crème  du  lait.
DEV.txt:2018:robe.  De  l'arabe  <!>;  robb,  sirop  ou  gelée  de  fruits.  Ce terme  paraît  être  d'origine  persane,  rob  par  un  seul  h;  les Arabes  auraient  doublé  cette  lettre  pour  donner  au  mot la  forme  trilitère  ordinaire  aux  mots  de  leur  langue.
DEV.txt:2125:Sirop.  \  ieu\  français  essyrot  (xiif  siècle),  ijsserop  (xv" siècle),  provenir',  elssarop,  issarop,  yssarop ,  esp.  xarahe , nxarnbe,  axarave,  axnrope,  jarah,  jarope,  portug.  xaropc (^surrapa,  zurappa,  vin  qui  a  perdu  sa  force ^),  ital.  siroppo, mvoppo,  sciloppo,  bas  lat.  syrupus,  siruppus,  sciruppus.  De l'arabe  vlr^  charâh ,  boisson,  vin,  café,  venant  du  verbe LjJi*  charih,  boire.  On  voit  qu'un  grand  nombre  des  formes citées  ont  conservé  l'article  [ach-charâh);  plusieurs  ont  pu t'tre  faites  sur  cj^^àJI  ach-charoûb ,  boisson.
DEV.txt:2126:te  mot  arabe  cliarâh  a  aussi  signifié  sirop ,  comme  on peut  le  voir  par  les  dérivés  j,îyi  charâhi,  «  syruporum  ven- ditor»,  jL?iyi  charâbâll^,  cr qui  syrupos  conficit  aut  ven- dit. ??  (Freytag.)  Voy.  aussi  Dozy,  Gloss.  p.  218.
DEV.txt:2874:Axarabe ,  esp.  voy.  Sirop.
DEV.txt:2875:Axarave,  esp.  voy.  Sirop.
DEV.txt:2876:Axarope,  esp.  voy.  Sirop.
DEV.txt:3398:Eissarop ,  ;;roi'.  vov.  Sirop.
DEV.txt:3439:EssMot,  voy.  Sirop.
DEV.txt:3673:Issarot,  pi^ov.  voy.  Sirop.
DEV.txt:3687:Jarab ,  esp.  voy.  Sirop.
DEV.txt:3691:Jarope,  esp.  voy.  Sirop.
```


## [2026-09-14T02:32:11.000Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT syrup/sherbet ===\"; grep -n -o \"SYRUP[^.]\\{0,300\\}\\|SHERBET[^.]\\{0,300\\}\" SKT.txt | head; echo \"=== FVQ sharab ===\"; grep -n -i \"sharab\\|šarāb\\|shurb\" FVQ_pages.txt | head",
 "description": "Grep Skeat and Jeffery"
}
```


### [2026-09-14T02:32:12.063Z] TOOL RESULT

```
=== SKT syrup/sherbet ===
=== FVQ sharab ===
```


## [2026-09-14T02:32:22.631Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -i \"syrup, sirup[^.]\\{0,300\\}\\|sirup, syrup[^.]\\{0,300\\}\\|sherbet[^.]\\{0,300\\}\" SKT.txt | head -6; echo \"=== WEB ===\"; grep -n -o -i \"sherbet[^.]\\{0,250\\}\" WEB_vol1.txt | head -4",
 "description": "Grep Skeat and Webster"
}
```


### [2026-09-14T02:32:23.957Z] TOOL RESULT

```
17101:Sherbet,  a  drink
17101:sherbet,  syrup
17217:Sherbet
17332:Sherbet
23690:sherbet,  shmb  i^i\ oh,  loraiacura,  vUiet  (^iner)
=== WEB ===
77889:sherbet
78622:sherbet glass, etc
```


## [2026-09-14T02:32:24.295Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON شربت ===\"; grep -n \"شربت\" MON_part1.txt MON_part2.txt | head -6; echo \"=== MON شراب ===\"; grep -n \"شراب\" MON_part1.txt MON_part2.txt | head -6",
 "description": "Grep Mo'in for sharab/sharbat"
}
```


### [2026-09-14T02:32:24.390Z] TOOL RESULT

```
=== MON شربت ===
MON_part2.txt:7980:شربتی شکل يا مربا ماتندی که از جوشاندن 
MON_part2.txt:11790:مدور خلط آور بصورت شربت يا دم کرده 
MON_part2.txt:34165:نوعی شیرینی که در درون آن شربتی معطر 
MON_part2.txt:34220:تخم مرع پزند و در شربت قند و نبات ریزه 
MON_part2.txt:34419:حلوا. طرز تهیه: شربت قند را قوام آورده و 
MON_part2.txt:34879:شربت‌های بیماران مبتلا به مرضص قند 
=== MON شراب ===
MON_part2.txt:193:غارج: ۲6 | - غاره| (.) شرابی که به وقت 
MON_part2.txt:646:غسبوق: 7( ] (مسصل.) شراب 
MON_part2.txt:1734:دوزخیان جریان یابد. شراب دوزخیان. 
MON_part2.txt:1818:شراب. غل و غش: آميزش چیزی کم قیمت 
MON_part2.txt:2460:بلبل. حکایت صوت جوشیدن آب و شراب 
MON_part2.txt:2834:اصطلاحات؛ لغ.) بادةٌ غمگسار: شرابی که
```


## [2026-09-14T02:32:29.421Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17098,17104p' SKT.txt; echo \"=== 17215 ===\"; sed -n '17215,17220p' SKT.txt; echo \"=== WEB 77889 ===\"; sed -n '77885,77895p' WEB_vol1.txt",
 "description": "Read Skeat and Webster sherbet"
}
```


### [2026-09-14T02:32:29.526Z] TOOL RESULT

```
[LLING.
allied  to  sAt//.  Florio  tmi-ilates  O.  1 xtralart  bv  *  to  shelve  or  go  aside,  ask awry.'  The  v  stands  for  a  guttural.  — I skelgja-sk  (where  -ik^'siJi,  oneselO.  to  cc askew. -Icel.  tkdlgr,  wry,  oblique,  (.be slouing).     See  Bhallov,
Snepherd ;  sec  Sheep.
Sherbet,  a  drink.  (Arab.)  Arab,  si a   drink,  draught,  sherbet,  syrup.— At rout  shartba,  he  drank.
shrub  (a),  a  drink,  chiefly  made  v rum.  (Atab.)     Arab.  skir6,  shurd,  a  dri
—  Arab.  root,  skariba  (above). ayrup,  sirup.  (F.— Span— Arab.)
iytitp.  —  Span,  xaropt,  a.  drink.  —  At skardb,  shurdb,  wine,  beverage,  syruj] Arab,  root  skariba  (above).
=== 17215 ===
SHRUB.
brig,  to  nib  with  r  brojidi  of  a m  A.  S.  /<•«*,  a  shrub.  Cf.  E. the  shnib  so  called;  Lowl n^r,  *o  liandful  of  heath  tied
Blether  lor  cleaning  culinary amieson.  Der.  senw-j^,  mean, y.  stunted. 0  ;  sec  Sherbet. (Scand.)  The  old  cense  Is  to nk  up— Dan,  sknt^f,  skruAMi, hftA.  dial.  ikrtikJea,  ikrui^,  to lelf  together,  allied  to  tkrinka, See  Shrink.
:  (O.  Low  G. )  M.  E.  schoderm, A  frequenlatire  x-erb.  —  O.  Sax. lo  ifaake ;  O.  Du.  schuddet^  to ible. _«e«  Shore. [E.)  M.  E.  skunitn^  shonien. It,  to  shun,  avoid ;  orig.  sen»e, hasten.  Cf.  Icel.  skunJa, tkyntia  iig^   Dan.  tkyndt,
Rvny,  speed. r.  (E.)  F'ropcrly  scocrtrr,  but 1/  derived  from  Dutch,  which  is the  Du.  sehoorur  being  of  E. t  called  a  scoontr  in  17I5, t  schooner  was  so  named  in MasMchuselts,  from  the  remark /ix.'I.e.  glides  swiftly.  This Clydcsdsue  Kon  or  sc0on,  to (Uy*  applied  to  stones  with  which ducks  and  drakes  *  in  the  water. ,  to  ahun,  orig.  to  speed,
(Scand.)  Pror.  E.  tkunt,  to M.  E.  shuHten,  to  stnrt  aside. ien  *.  •  Icel.  skunda,  to  s;  leed  ;
=== WEB 77889 ===
bon dioxide is freezable. 3
froze, pt.; frozen, pp.; freezing, ppr.
eze, vi.; Z fre ” freesen, fresen, from AS. freosan, to
es be ene into ice; to be hardened or idified by cold. t Soon a covered or clogged with ice. 3. to be or become very cold. — | í 4. to become fixed or attached by freezing; as, the automobile tires froze to the ground. 5. to die or be damaged by exposure to cold. : pa 6. to become motionless or stiff. F 7. to be chilled or made momentarily rigid by a strong, sudden emotion; as, his face froze with terror. A 8. to become formal, haughty, or unfriendly to freeze over; to become covered with ice. to freeze up; figuratively, to assume a frigid and forbidding attitude. [Colloq.]} freeze, v.t. 1. to cause to form into ice; to harden or solidify by cold. 2. to cover or clog with ice. 3. to make very cold; to chill. 4. to preserve (food) by rapid refrigera- tion. 5. to make fixed or attached by freezing. 6. to kill or damage by exposure to cold. 7. to make or keep motionless or stiff. _ 8. to frighten or discourage by cool behav- ior, unfriendliness, etc. 9. to make formal, haughty, or unfriendly. 10. to fix (prices, employment, an em- ployee, etc.) at a given level or place by au- thoritative regulation. [Colloq.] to freeze in; to entangle or envelop in ice; as, the ship was frozen in for the winter. to freeze one’s blood; to terrify or horrify. fo ae (on) to; to cling to; hold fast to. [Colloq.] to freeze out; to keep out or force out by a cold manner, competition, etc. (Colloq.] lo freeze over; to cover with ice. freeze, n. 1. a freezing or being frozen. freases penodi of a freezing weather. f C, n. frieze. [Obs.] reez'čr, n. 1. a person or device that freezes;
especially, a machine for making i and sherbet. ea
fre a deep freezer. ez'in: a. ve: e 5 Sheen Ty cold; as, a freezing atmos-
freez’in N n. . ozen the process or state of becoming
freez/ing ly, adv. a coldly.
substan Cure, misste of two or more
1 j of salt and snow i -
£ pees intense cold. Dom o meh o
```


## [2026-09-14T02:32:41.332Z] TOOL CALL #46: Bash

```json
{
 "command": "python3 tools/fetch_source.py --help 2>&1 | head -30",
 "description": "Check fetch_source usage"
}
```


### [2026-09-14T02:32:42.663Z] TOOL RESULT

```
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
```


## [2026-09-14T02:32:46.774Z] TOOL CALL #47: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/sherbet\" \"https://www.etymonline.com/word/syrup\" \"https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%B4%DA%A9\" \"https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D9%86\"; do python3 tools/fetch_source.py \"$u\" --note \"page 472 verification\" 2>&1 | tail -1; done",
 "description": "Archive web sources batch 1"
}
```


### [2026-09-14T02:32:51.398Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/705d689d1e133e0a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d171550d2f1447fa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b83ace3dea6b9165.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3a5d0f6d8b7ddc76.txt
```


## [2026-09-14T02:32:54.173Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== sherbet ===\"; grep -n -A18 -i \"^Etymology\" 705d689d1e133e0a.txt | head -40",
 "description": "Read wiktionary sherbet"
}
```


### [2026-09-14T02:32:54.239Z] TOOL RESULT

```
=== sherbet ===
```


## [2026-09-14T02:32:56.104Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== syrup etymonline ===\"; grep -n -i -m1 -A12 \"syrup(n\" d171550d2f1447fa.txt | head -25; echo; grep -n -i -m2 -B2 -A10 \"sharab\\|Arabic\" d171550d2f1447fa.txt | head -40",
 "description": "Read etymonline syrup"
}
```


### [2026-09-14T02:32:56.175Z] TOOL RESULT

```
=== syrup etymonline ===

23- syrup (n.) 
24-
25: late 14c., sirup , "thick, sweet liquid," from Old French sirop "sugared drink" (13c.), and perhaps from Italian siroppo , both from Arabic sharab "beverage, wine," literally "something drunk," from verb shariba "he drank" (compare sherbet ). Spanish jarabe , jarope , Old Provençal eissarop are from Arabic; Italian sciroppo is via Medieval Latin sirupus . In English, formerly also sirup , sirop .
26- also from late 14c. 
27-
28- Entries linking to syrup 
29-
30- sherbet (n.) 
31-
32: 1580s as sorbet ; other early spellings include zerbet, cherbet ; the form sherbert is attested by 1670s. Originally a cooling drink of the East, made from diluted fruit juice and sugar and chilled with fresh snow when possible. The word is from Turkish serbet , from Persian sharbat , from Arabic sharba(t) "a drink," from shariba "he drank." A doublet of syrup , and compare sorbet .
33-
34- In 16c-18c. in reference to a drink, sometimes served with ice. By 1723 it could also be a prepared syrup that was added to punch or other drinks. The frozen dessert appears to be an Italian invention, attested in English 1760 as sorbetto , offering sherbet in the definition.
35-
36- Milk sherbet , with dairy added, is by 1827. French spelling sorbet readopted in English by 1828, originally always with full French name ( sorbet au cafe, sorbet a la pistache, etc.) in recipes that could be indistinguishable from ice cream.
37-
38- In later 19c. the French sorbet (in this era, in English cookbooks) necessarily contained alcohol, and was thus differentiated from sherbet. In early 20c. sherbet was distinguished from ices by including egg whites or other stabilizers; around the 1940s the addition of dairy became the designator (an article in Confectionary and Ice Cream World dated July 18, 1947, discusses new state laws requiring milk solids be included in sherbet.) Sorbet lost the alcohol connection after American prohibition, and came to designate a dessert of sweetened fruit juice or pulp without added dairy.
39-
40- In chiefly British use, sherbet also refers to a kind of powder that is stirred into water to make a fizzy drink, by 1850.
41-
42- sirop (n.)
```


## [2026-09-14T02:33:02.733Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== سرشک ===\"; head -60 b83ace3dea6b9165.txt; echo; echo \"=== ران ===\"; grep -n -i -B3 -A12 \"Persian\" 3a5d0f6d8b7ddc76.txt | head -60",
 "description": "Read wiktionary sereshk and ran"
}
```


### [2026-09-14T02:33:02.796Z] TOOL RESULT

```
=== سرشک ===
URL: https://en.wiktionary.org/wiki/%D8%B3%D8%B1%D8%B4%DA%A9
FETCHED: 2026-09-14T02:32:49Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
=== ران ===
79- Noun 
80-
81- 3 
82: Persian 
83-
84: Toggle Persian subsection 
85-
86- 3.1 
87- Alternative forms 
88-
89- 3.2 
90- Pronunciation 
91-
92- 3.3 
93- Etymology 1 
94-
95- 3.3.1 
96- Noun 
--
723-
724- ( anatomy ) thigh 
725-
726: Persian
727- [ edit ] 
728-
729: Persian Wikipedia has an article on: ران 
730-
731- Wikipedia fa 
732-
733- Alternative forms
734- [ edit ] 
735-
736- رون ( run ) ( colloquial Iranian ) 
737-
738- Pronunciation
739- [ edit ] 
740-
741: ( Classical Persian ) IPA ( key ) : /ˈraːn/ 
742-
743- ( Dari, formal ) IPA ( key ) : [rɑːn] 
744-
745- ( Dari, formal ) IPA ( key ) : [rɑːn] 
746- ( Kabuli ) IPA ( key ) : [rɑːn] 
747-
748- ( Hazaragi ) IPA ( key ) : [rɔːn] 
749-
750- ( Iran, formal ) IPA ( key ) : [ɹɒːn] 
751-
752- ( Iran, formal ) IPA ( key ) : [ɹɒːn] 
753- ( Tehrani ) IPA ( key ) : [ɹuːn] 
--
777- Etymology 1
778- [ edit ] 
779-
780: Inherited from Middle Persian [script needed] ( lʾn' /⁠rān⁠/ , “ thigh ” ) , from Proto-Iranian *hrā́nah , from Proto-Indo-Iranian *srā́nas , from Proto-Indo-European *srḗn-s .
781-
782- Noun
783- [ edit ] 
784-
785- Dari
```


## [2026-09-14T02:33:17.540Z] TOOL CALL #51: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D8%B4%D8%B1%D8%A8%D8%AA\" \"https://en.wiktionary.org/wiki/%D8%B4%D8%B1%D8%A7%D8%A8\" \"https://www.nisanyansozluk.com/kelime/serbet\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/hr%C4%81nah\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 472 verification\" 2>&1 | tail -1; done",
 "description": "Archive web sources batch 2"
}
```


### [2026-09-14T02:33:25.347Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D8%B4%D8%B1%D8%A8%D8%AA
/home/sfmqrb/git/rishe/data/verification/sources/web/9991105bd84fd615.txt
### https://en.wiktionary.org/wiki/%D8%B4%D8%B1%D8%A7%D8%A8
/home/sfmqrb/git/rishe/data/verification/sources/web/644cb1733249b6e2.txt
### https://www.nisanyansozluk.com/kelime/serbet
/home/sfmqrb/git/rishe/data/verification/sources/web/834e80fcb6fdd533.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/hr%C4%81nah
/home/sfmqrb/git/rishe/data/verification/sources/web/e43bd23aee9cb744.txt
```


## [2026-09-14T02:33:28.303Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 9991105bd84fd615 644cb1733249b6e2 834e80fcb6fdd533 e43bd23aee9cb744; do echo \"##### $f\"; head -5 $f.txt; grep -n -i \"borrowed from\\|Inherited from\\|From Arabic\\|Etymology\" $f.txt | head -10; done",
 "description": "Inspect fetched pages"
}
```


### [2026-09-14T02:33:29.370Z] TOOL RESULT

```
##### 9991105bd84fd615
URL: https://en.wiktionary.org/wiki/%D8%B4%D8%B1%D8%A8%D8%AA
FETCHED: 2026-09-14T02:33:19Z
STATUS: 200
TITLE: شربت - Wiktionary, the free dictionary

70: Etymology 
87: Etymology 
107: Etymology 
219: Etymology
222: From Ottoman Turkish شربت ( şerbet ) or Persian شربت ( šarbat ) , from Arabic شَرْبَة ( šarba ) .
245: Etymology
248: Etymology tree
255: Borrowed from Classical Persian شَرْبَت ( šarbat ) , borrowed from Arabic شَرْبَة ( šarba ) , from شَرِبَ ( šariba ) .
328: Etymology
331: Etymology tree
##### 644cb1733249b6e2
URL: https://en.wiktionary.org/wiki/%D8%B4%D8%B1%D8%A7%D8%A8
FETCHED: 2026-09-14T02:33:24Z
STATUS: 200
TITLE: شراب - Wiktionary, the free dictionary

62: Etymology 1 
77: Etymology 2 
89: Etymology 3 
109: Etymology 
126: Etymology 1 
135: Etymology 2 
149: Etymology 1 
158: Etymology 2 
175: Etymology 
192: Etymology 
##### 834e80fcb6fdd533
URL: https://www.nisanyansozluk.com/kelime/serbet
FETCHED: 2026-09-14T02:33:24Z
STATUS: 200
TITLE: Kelime bulunamadı - Nişanyan Sözlük

##### e43bd23aee9cb744
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/hr%C4%81nah
FETCHED: 2026-09-14T02:33:25Z
STATUS: -1
TITLE:
```


## [2026-09-14T02:33:34.699Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### sharbat Persian section\"; sed -n '100,135p' 9991105bd84fd615.txt; echo; echo \"### sharab Persian\"; grep -n -A6 \"^Persian$\\| Persian$\" 644cb1733249b6e2.txt | sed -n '1,60p'",
 "description": "Read Persian sections"
}
```


### [2026-09-14T02:33:36.186Z] TOOL RESULT

```
### sharbat Persian section

 4 
 Persian 

 Toggle Persian subsection 

 4.1 
 Etymology 

 4.2 
 Pronunciation 

 4.3 
 Noun 

 4.3.1 
 Derived terms 

 4.3.2 
 Descendants 

 Toggle the table of contents 

 شربت 

 12 languages 

 العربية 
 فارسی 
 Suomi 
 Bahasa Indonesia 
 Kurdî 
 Malagasy 
 پنجابی 
 پښتو 
 Русский 

### sharab Persian
1665: Persian
1666- [ edit ] 
1667-
1668- Persian Wikipedia has an article on: شراب 
1669-
1670- Wikipedia fa 
1671-
--
1720: Iranian Persian
1721-
1722- Tajik
1723-
1724- шароб 
1725-
1726- شراب • ( šarāb / šarâb ) ( Tajik spelling шароб )
```


## [2026-09-14T02:33:39.368Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1670,1700p' 644cb1733249b6e2.txt; echo \"=== sharbat persian etym ===\"; awk 'NR>400 && /Persian/,0' 9991105bd84fd615.txt | grep -n -i -m4 -A4 \"Borrowed from Arabic\\|from Arabic\" | head -20",
 "description": "Read Persian etymologies"
}
```


### [2026-09-14T02:33:40.454Z] TOOL RESULT

```
 Wikipedia fa 

 Etymology
 [ edit ] 

 Borrowed from Arabic شَرَاب ( šarāb ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʃa.ˈraːb/ 

 ( Dari, formal ) IPA ( key ) : [ʃä.ɾɑ́ːb] 

 ( Dari, formal ) IPA ( key ) : [ʃä.ɾɑ́ːb] 
 ( Kabuli ) IPA ( key ) : [ʃä.ɾɑ́ːb] 

 ( Hazaragi ) IPA ( key ) : [ʃä.ɾɔ́ːb̥] 

 ( Iran, formal ) IPA ( key ) : [ʃæ.ɹɒ́ːb̥] 

 ( Tajik, formal ) IPA ( key ) : [ʃä.ɾɔ́b] 

 Rhymes: -aːb 

 Readings

 Classical reading ? 

 šarāb

=== sharbat persian etym ===
3: Gulf Arabic terms derived from Arabic 
4- Gulf Arabic terms with IPA pronunciation 
5- Gulf Arabic lemmas 
6- Gulf Arabic nouns 
7- Ottoman Turkish terms derived from Classical Persian 
8: Ottoman Turkish terms derived from Arabic 
9- Ottoman Turkish terms derived from the Arabic root ش ر ب 
10- Ottoman Turkish terms borrowed from Classical Persian 
11- Ottoman Turkish lemmas 
12- Ottoman Turkish nouns 
--
14: Persian terms borrowed from Arabic 
15- Persian terms derived from the Arabic root ش ر ب 
16: Persian terms derived from Arabic 
17- Persian terms with IPA pronunciation 
18- Rhymes:Persian/at 
19- Rhymes:Persian/at/2 syllables 
20- Persian terms with audio pronunciation
```


## [2026-09-14T02:33:50.121Z] TOOL CALL #55: Bash

```json
{
 "command": "for u in \"https://www.nisanyansozluk.com/kelime/%C5%9Ferbet\" \"https://en.wiktionary.org/wiki/sirisk\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 472 verification\" 2>&1 | tail -1; done; echo; cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in $(ls -t *.txt | head -2); do echo \"##### $f\"; head -40 $f; done",
 "description": "Fetch Nisanyan serbet"
}
```


### [2026-09-14T02:33:52.176Z] TOOL RESULT

```
### https://www.nisanyansozluk.com/kelime/%C5%9Ferbet
/home/sfmqrb/git/rishe/data/verification/sources/web/31234b121c68e295.txt
### https://en.wiktionary.org/wiki/sirisk
/home/sfmqrb/git/rishe/data/verification/sources/web/2e9d3c6bd71a38ee.txt

##### 2e9d3c6bd71a38ee.txt
URL: https://en.wiktionary.org/wiki/sirisk
FETCHED: 2026-09-14T02:33:52Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found##### 31234b121c68e295.txt
URL: https://www.nisanyansozluk.com/kelime/%C5%9Ferbet
FETCHED: 2026-09-14T02:33:51Z
STATUS: 200
TITLE: şerbet - Nişanyan Sözlük

şerbet - Nişanyan Sözlük 

 Nişanyan Sözlük 

 ç ğ ı ö ş ü 
 ileri arama

 Bu sözlük nedir? Kullanım Şartları ·
 Gizlilik Politikası 

 © Sevan Nişanyan 2002-2026
 Alıntılarda kaynak gösterilmesi rica olunur.
```


## [2026-09-14T02:33:58.974Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ===\"; grep -n -i \"sresk\\|sreno\\|srēnos\\|srāna\" IEC.txt | head -10; echo \"=== SYN thigh ===\"; grep -n -i \"4.36\\|thigh\" SYN.txt | head -10; echo \"=== AHD watkins ===\"; grep -n -i \"sreu\\|sresk\\|sreno\" AHD_watkins1985.txt | head -10",
 "description": "Grep Mann, Buck, Watkins"
}
```


### [2026-09-14T02:33:59.084Z] TOOL RESULT

```
=== IEC ===
=== SYN thigh ===
5350:Goth. mimz (once, here ‘meat’; also mammo prob. related); Lith. mésa, Lett. miesa, OPruss. mensa; ChSl. meso, etc., general Slavic: Skt. marisa-, mas-; Arm. mis; Alb. mish; Toch. B misa (pl. tan- tum); with other meanings, Grk. punpds ‘thigh’, Lat. membrum ‘part of the body’, Ir. mir ‘portion, morsel’, etc.
5771:be teeth, on ‘fork’, tour OS ’ t of the Jaw in jaw Pol ‘angle�� to tha Bee ae m verbs for ‘chew’ Or wae he modern Polish) seems to have dasa slang term forthe: ‘chauter starte - Several are obscure in their d ection. i a ait words for ew, aHal ‘chin’. Orig. sense Jaw and ultimate connection with ae word for ‘knee’, 1B *genu- (neut.), Gri. yoru, Lat. geni, etc. (4.36), through some com- mon notion like ‘angle’, is probable. Walde-P. 1.587. Ernout-M. 414. -H, 1.589 f. on ‘jaw’ (so always in Hom.) and ‘cheek’, -yéverov ‘chin’ (and ‘beard’) ; Lat. gena ‘cheek’ (mostly in pl.; stem genu- in genutni dentés ‘back teeth’); W. gen ‘jaw, chin’ (Ir. gin, W. geneu, Br. genou ‘mouth’); Goth. kinnus, ON kinn, Dan., Sw. kind ‘cheek’, OE cin, OHG kinni, etc. (all WGmce. words) ‘chin’ (but in early period traces of use for ‘jaw’, as OHG chinne ‘jaws’ Notker, Ps. 31.9, OHG chinnibacho ‘jaw’, OE cinban ‘jaw- bone’); Skt. hanu- ‘jaw’ (h for 7 second- ary), Av. zanu- ‘jaw’ or ‘chin’ (in epd., Barth, 1689) , NPers. zanaz ‘chin’; Toch. Ber oa (dual, SSS, 3, ftn.). Gre ae ae extension *Gon(e)dh-, Ba ease pn ; zandas ‘jaw’, al Mihl.-Endz, 4.759) edi pail # Ok rn al yom vor) istot, =i + Boisacq 862. GROpeRT se ce nr HdBos,. vers NG Hacé\)\a, of frequency.
5940:; Lett. gumba ‘{umor’, sa pera 568. Brickner 138 ff. (Ber- a ae akes two separate groups.) ,; Chsl. rit ‘peak’, SCr. rt a Boh. ret ‘Jip’, etc., these Lee oe. ‘projection’ (whence a th’ or ‘Lip’ through ‘snout’ of ‘ante ae Lat. ort? ‘rise’, Okt. T$va~- ‘thigh’, we S. Lane, AJPh. 54.64.
6199:6. Skt. aviguli-, Av. angusta- (as ‘finger’ only in epds., otherwise ‘toe’ = Skt. avigustha- ‘thumb, big toe’) : Skt, anga- ‘limb’, OHG ancha ‘nape of the neck, thigh’, NE ankle, etc., all prob. as ‘crooked’ : Lat. angulus ‘corner’, etc, Walde-P. 1.61. Walde-H. 1.48 f.
6250:3. Ir. coss (also ‘foot’), NIr. cos : Lat. coxa ‘hip’ (in VLat. replaces femur ‘thigh’, hence Fr. cutsse, etc., REW 2292; > W. coes ‘leg’), Skt. kaksa-, Av. kaSa- ‘armpit’, OHG hahsa ‘bend of the knee’, with varied specializations fr. a common notion of ‘joint, articulation of the limbs’; Walde-P. 1.456f. Ernout-M. 226. Walde-H. 1.283. Pedersen 1.34, 78.
6251:Br., Corn. gar = W. gar ‘thigh, ham’, Ir. gairri ‘calves’ of the leg (cf. Fr. jarret ‘hock’ fr. Gallic *garr-), etym. obscure. Henry 129. Connection with Lett. gurnt ‘groins, hips’ (as Bezzenberger in Stokes 107) apparently untenable (cf. Walde-P. 1.557, Miihl.-Endz. 1.684).
6257:OE sceanca (but esp. the leg below the knee, ‘the shank’, gl. Lat. crus) = Dan. skank ‘shank’, Sw. skank ‘thigh- or shinbone’, MLG schenke ‘thigh’ (dim, MHG, NHG schenkel, etc. ‘thigh’), perh. fr. the notion of ‘crooked’ (cf. Grk, oxédos : axodtds, above, 1): OHG hin. kan, NHG hinken, Skt. khafij- ‘limp’, kanga- ‘lame’. Walde-P. 2.564. Falk. Torp 984 f.
9064:ChS]. veéerja, SCr. vegera, Boh, vedere ‘supper’ (Pol. wreczerza, Russ, vederja now mostly of the Lord’s Supper), fr, ChSl. vecerii, etc. ‘evening’ (14.36),
9304:A word denoting a certain part of any animal may be used specifically for the meat of that part of a particular animal, So words for ‘ham’ mainly that of swine, as NE ham, once ‘hollow back of the knee’, ‘back of the thigh, buttock’ (ef. NED s.v.), NHG schinken (: schenkel ‘thigh’), Fr. jambon (: jambe ‘leg’), Russ. okorok (: SCr. krak ‘thigh’), etc. Cf. also NE bacon (: back), NHG speck ‘bacon’ (: OE spic ‘fat, fat meat or ba- con’, etc.).
10675:NE trousers, earlier trouses, pl. of trouse, this fr. Ir. or Gael. triubhas (pro- nounced as NIr. trits, Sc. trews), this prob. fr. OFr. trebus, MLat. tubricus a sort of ‘leggings’ (Isid. 22.30), this again fr. a Gme. form like OHG deohproh, cpd. of words for ‘thigh’ and ‘breeches’. NED s.v. REW 8967, Jaberg, op. cit. 159,
=== AHD watkins ===
897:reu-2, Also reue-. To smash, knock down, tear out, dig up, uproot. 1. Suffixed o-grade form *rous-o- in Ger- manic *rawwa- in: a. Old Norse régg, réggr, woven tuft of wool: RAG}; b. Norwegian rugga, rogga, coarse cover- let, akin to the Scandinavian source of RUG. 2. Basic form *reu- in Latin ruere, to collapse, cause to collapse: RABBLE, RUIN. [Pok. 2. reu- 868.] reudh-', Red, ruddy. I. O-grade form *roudh-. 1. Ger- manic “raudaz in: a. Old English réad, red: RED; b. Old Norse rauthr, red (> reythr, rorqual): RORQUAL. 2. Ger- manic *raudnia- in Old Norse reynir, mountain ash, rowan (from its red berries), akin to the source of ROWAN. 3. Latin rijfus (of dialectal Italic origin), reddish: RUFES- CENT, RUFOUS. 4. Latin rdbus, red, in robigd, ribigo, rust: RUBIGINOUS. 5. Latin rdbur, rdbus, red oak, hard- ness, and rdbustus, strong: ROBLE, ROBORANT, ROBUST; CORROBORATE, RAMBUNCTIOUS. II. Zero-grade form *rudh-. 1. Form *rudh-d- in Germanic *rud6 in: a. Old English rudu, red color: RUDDLE, RUDDY; b. Old English rudduc, robin: RUDDOCK. 2. Suffixed form *rudh-sto- in Germanic *riist- in Old English rdst, rust: RusT. 3. Latin rubeus, red: ROUGE, RUBEOLA, RUBY; RUBEFACIENT 4. Latin rubicundus, red, ruddy: RUBICUND. 5. Latin rubidus, red: RUBIDIUM. 6. Suffixed (stative) form *rudh-é- in Latin rubére, to be red: RUBESCENT; ERUBES- CENCE. 7. Suffixed form *rudh-ro- in: a. Latin ruber, red: RUBELLA, RUBRIC; BILIRUBIN; b. Latin rutilus, reddish: RUTILANT; Cc. Greek eruthros, red (with pro- thetic vowel, from oldest root form *sreudh-): ERY- THEMA, ERYTHRO-; d. possibly remade Greek erusi-, red, reddening: ERYSIPELAS. 8. Suffixed form *rudh-to- in Latin russus, red: RISSOLE, ROUX, RUSSET. [Pok. reudh- 872.] reudh-2, To clear land. 1. Suffixed zero-grade form *rudh-yo- in Germanic *rudjan in Old Norse rydhja, to clear land: RID. 2. Possibly Germanic expressive variant *rudd- stick, club, in Old English rodd, stick: Rop. [In Pok. 2. reu- 868.] reue-. To open; space. 1. Suffixed variant form *ri-mo- (< *rua-mo-) in Germanic *riimaz in: a. Old English rim, space: ROOM; b. Old French run, ship’s hold, space: RUMMAGE. 2. Suffixed form *reu(g)-es- in Latin ris, “open land,” the country: RURAL, RUSTIC. [Pok. reuo-, ri- 874.] reug-. To vomit, belch, smoke, cloud. 1. Germanic *reu- kan in Old English réocan, to smoke, reek: REEK. 2. Suf- fixed zero-grade form *rug-to- in Latin ructdre, to belch: ERUCT. [Pok. 4. reu- 871.] reugh-men-. Cream. O-grade form *roughmen- in Ger- manic *rau(g)ma- in Middle Low German rém(e), cream: RAMEKIN. [Pok. reugh-m(e)n- 873.] reup-. Also reub-. To snatch. I. Basic form *reub- in Germanic *rupja in Flemish rippen, to rip: RIP!. II. O-grade form *roup-. 1. Germanic *raufjan in: a. Old English réafian, to plunder: REAVE!; b. Old English beréafian, to take away (be-, bi-, intensive prefix; see ambhi): BEREAVE. 2. Germanic *raubén, to rob, in: a. Middle Dutch and Middle Low German réven, to rob: ROVER; b. Old French rober, to rob: ROB; c. Italian rubare, to rob: RUBATO. 3. Germanic *raubd, booty, in Old French robe, robe (> “clothes taken as booty”): ROBE. 4. Suffixed form *roup-tro- in Sanskrit loptram, booty, from lumpati, he breaks, removes: LOOT. III. Zero-grade form *rup-. 1. Latin dsirpdre (< *isu- rup-; isus, use, usage, from iti, to use), originally “to interrupt the orderly aquisition of something by the act of using,” whence to take into use, usurp: USURP. 2. Na- salized form *ru-m-p- in Latin rumpere, to break (> riipés, rock): ROUT!, RUPTURE; ABRUPT, BANKRUPT, CORRUPT, DISRUPT, ERUPT, INTERRUPT, IRRUPT, RUPICO- Lous. [Pok. 2. reu- 868.] rezg-. To plait, weave, wind. Germanic *ruski- in Old English risc, rysc, rush: RUSH?. [Pok. rezg- 874.] [risan. To rise. Germanic word. 1. Germanic *risan in:
995:spit!. 2. Germanic *speiw- in Old English spiwan, spio- wan, to spew: SPEW. 3. Germanic *spait- in Old English spatl, spittle: sPITTLE. 4. Germanic *spiit- in: a. Middle English spouten, to spout forth: spout; b. Dutch sputte- ren, to sputter, akin to the probable Low German source of SPUTTER. 5. Zero-grade form *spu- in Latin spuere, to spit: SPUTUM; CUSPIDOR. 6. Zero-grade form *(s)pyu- in Greek ptuein, to spit: HEMOPTYSIS, PTYALIN. [Pok. (s)p(hjieu- 999.] srebh-. To suck, absorb. Zero-grade form *srbh- in: a. Germanic *surp- in altered form in Dutch slurpen, to slurp, lap: SLURP; b. suffixed form *srbh-é- in Latin sorbére, to suck: ABSORB, ADSORB, RESORB. [Pok. srebh- 1001.] srenk-. To snore. O-grade form *sronk- in: a. Greek rhonkos, rhonkhos, a snoring: RHONCHUS; b. Greek rhunkhos, snout, bill, beak: RHYNCHOCEPHALIAN. [Pok. srenk- 1002.] sreu-. To flow. 1. Suffixed o-grade form *srou-mo- in Germanic *straumaz, stream, in: a. Old English stréam, stream: STREAM; b. Dutch stroom, stream: MAELSTROM. 2. Basic form *sreu- in: a. Greek rhein, to flow: RHEO-, -RRHEA; CATARRH, DIARRHEA, HEMORRHOID, RHYOLITE; b. suffixed form *sreu-mn in Greek rheuma, stream, humor of the body: RHEUM. 3. Suffixed zero-grade form *sru-dhmo- in Greek rhuthmos, measure, recurring mo- tion, rhythm: RHYME, RHYTHM. [Pok. sreu- 1003.]
1336:CASE2 kap- CASHIER kes-2 CASTE kes-? CASTIGATE kes-2 CASTLE kes-2 CASTRATE kes-2 CATA- kat-1 CATABOLISM gWele-1 CATACHRESIS gher-5 CATACLYSM kleu-2 CATALECTIC slég- CATALEPSY (s)lag¥- CATALOGUE leg-1 CATALYSIS leu-1 CATAMENIA mé-2 CATAPLEXY plak-2 CATAPULT pél- CATARRH sreu- CATASTASIS sta- CATASTROPHE streb(h)- CATCH kap- CATCHPOLE pau- CATECHIZE (s)wagh- CATEGORY ger-1 CATER-CORNERED kWetwer- CATERPILLAR pilo- CATHEDRA sed-1 CATHEPSIN kat-1 CATHETER yé- CATHODE sed-2 CATHOLIC sol- CATION ei-1 CATOPTRIC okw- CATTLE kaput CAUDILLO kaput CAUDLE kele-1 CAULESCENT kaul- CAULICLE kaul- CAULIFLOWER _bhel-3, kaul- CAULINE kaul- CAUSTIC kéu- CAUTERY kéu- CAUTION keue-1 CAVE keue-2 CAVEAT keue-1 CAVERN keue-2 CAVETTO keue-2 CAVIL  kel-8
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
1595:HEM! kem-2 HEMATOCRIT krei- HEMERALOPIA amer- HEMI- sémi- HEMISTICH  steigh- HEMOPTYSIS spyeuU- HEMORRHOID sreu- HEMP kannabis
1791:MADAM deme-! MADAME deme-1 MADDER! modhro- MADEMOISELLE deme-1 MADONNA deme-1 MADREPORE miater- MADURO ma-1 MAELSTROM mele-, sreu- MAENAD men-! MAESTOSO meg- MAESTRO meg-
2181:RETE era-2 RETIARY era-2 RETICENT tak-1 RETICLE era-2 RETICULE ere-2 RETIFORM ere-2 RETINA era-2 RETINACULUM  ten- RETORT! terkw- RETRACT tragh- RETRAL re- RETRIEVE trep-2 RETRO- re- RETROACTIVE ag- RETROCEDE ked- RETROGRADE ghredh- RETROGRESS ghredh- RETRORSE wer-3 RETROSPECT spek- RETURN tera-1 RETUSE (s)teu- REVEAL weg-1 REVEILLE weg-2 REVEL duellum REVENANT gWa- REVENGE deik- REVENUE gWa- REVERBERATE wer-3 REVERE! wer-4 REVERT wer-3 REVEST wes-4 REVIEW weid- REVIVE gWei- REVOKE wekw- REVOLVE wel-3 REVULSION wel-4 REWARD wer-4 RHABDOMANCY wer-3 RHABDOVIRUS wer-3 RHAPSODY wed-2, wer-3 RHEO- sreu- RHETOR wer-6 RHEUM sreu- RHINOCEROS ker-1 RHIZO- wrad- RHIZOBIUM gWei- RHIZOME wrad- RHODIUM wrod- RHODO- wrod- RHODOCHROSITE ghréu- RHODODENDRON deru RHODOPSIN OkW- RHOMBUS_ wer-3 RHONCHUS  srenk- RHYME sreu- RHYNCHOCEPHALIAN srenk- RHYOLITE sreu- RHYTHM = sreu-
2200:ROW? era-1 ROWAN reudh-! ROWEL ret- ROWEN wel-2 ROYAL reg-! -RRHAGIA wrég- -RRHEA sreu- RUBATO reup- RUBEFACIENT dhé-1, reudh-1
2319:STOVE! staup- sTow sta- STRABISMUS streb(h)- STRABOTOMY streb(h)- STRAIN! | streig- STRAIN?  ster-2 STRAIT  streig- STRANGE eghs STRANGLE strenk- STRANGLEs  strenk- STRANGULATE _ strenk- STRANGURY strenk- STRATAGEM ag-, ster-2 STRATH ster-2 STRATOCRACY  ster-2 STRATUS  ster-2 STRAW ster-2 STREAK streig- STREAM sreu- STREET  ster-2 STRENGTH  strenk- STREPTO-  streb(h)- STREPTOMYCES meug-2 STREPTOMYCIN meug-2 STREPTOTHRICIN  thrix STREUSEL ster-2 STREW ster-2
```


## [2026-09-14T02:34:00.949Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index ===\"; grep -n -i \"SRENO\\|SRESK\\|RAN \\|SERESHK\" incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"=== ARY fa ===\"; grep -n \"سرشک\\|ران(\" incoming/ARY/ARY_pages.txt | head -10",
 "description": "Grep Aryanpur"
}
```


### [2026-09-14T02:34:01.025Z] TOOL RESULT

```
=== ARY latin index ===
1089:BIS ge tle Np MB ly J Saran LS a jpn Sa po 9 SEL aL galy |
1148:Ie Sule D4 Gr FAT IN) eran ly ay 08 heel Lal jy (Ke ol wo
1526:ARYEN (FRENCH) <1 ERA, ERANAG,ERAN (PAHLAVI) 5 sly,
1547:o8Y (AREIA) fp ERAN 5 hey AIRYA Sly pel eel Oy cent jt ae “ola!” edly -t
2485:STIERAN HOSTUBAR (PAHLAVI) «5.34
2936:GAYR ARMENIAN) gs, VARAN, WARAN (PAHLAVI) 5 hay,
2937:OURON GREEK) gl» BARIN, BARAN (KURDISH) 52,5
2938:URINA LATIN) o3Y BARAN 4AFGHANI) (4) sbi!
3432:DELAMARRE: oo BAIRAN (GOTHIC) 3,
3441:. BERAN (OLD ENGLISH) oy 16:
=== ARY fa ===
2552:ا ۲ ۲ اشکه ارس» سرشک
10519:۵۶ ) سرشک (به چم "شک چشم » "قطره"
```


## [2026-09-14T02:34:06.670Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10510,10530p' incoming/ARY/ARY_pages.txt; echo \"=== pdf page tag ===\"; awk 'NR<=10519 && /\\[pdf page/{p=$0} END{print p}' incoming/ARY/ARY_pages.txt",
 "description": "Read Aryanpur sereshk entry"
}
```


### [2026-09-14T02:34:07.725Z] TOOL RESULT

```
اپ پارسی پاستان (28851/00 0ا۰:)0 -133۸060 یا
: پهلری نمی 5۸80۸ ,85۸7۸5 آلمانی (/080تا0): لد رای انا
سانسکریت (5۸/۷5877): 5230۸85 انگلیسی کهن (#لقلا20/0 ۰:۵۵ 118080
یرنانی 086870): : انگلیسی (3/7ل8001): زان ان
8 ,1017115 دانمارکی (/0۸۸/13): 10
گرتبک (ع007171): 1۸10۸ سرئدی (5750157): 102
ایسلندی کهن (/(500010۸71۸ صا0): نروژی (07780140/): 102
11707307 هلدی (17ع07)+ از (41 ان ۱:۱
[pdf page 355]
۵۶ ) سرشک (به چم "شک چشم » "قطره"
اسلاوی کهن (ع۲1ها5 4ل#لاتت صا0): پسگشت‌ها شمیت دی
0۸ 9 ۶00200
لهستانی (8.ا۳0): 700۸ ای اس : +87
بلغاری‌کهن (/(من۶ ناه صهام: 05230۸ سس ها
لیتوانی (۵0۷ا(فلا77/ا): ۱ ادها 4 (507) ,1320 (130) رت
پروسی کهن (/(4ا۶5تا۶۸ ۰:۵۵ 150۸۲ 7 (11830) :005
ایرلندی کهن 183324 صا۵): رززد نا 9 (07880 ۰ 7
ولزی (7(کل#5): رزوی رده فرهنگ معین : ۱۸۸۵
برهان قاطع : ۱۱۳۲
بادداشت:
چم اين واژه در زبان برنانی: توده» انباشته» تل
=== pdf page tag ===
[pdf page 355]
```


## [2026-09-14T02:34:14.914Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk '/\\[pdf page 355\\]/,/\\[pdf page 356\\]/' incoming/ARY/ARY_pages.txt | head -60",
 "description": "Print ARY pdf page 355"
}
```


### [2026-09-14T02:34:15.964Z] TOOL RESULT

```
[pdf page 355]
۵۶ ) سرشک (به چم "شک چشم » "قطره"
اسلاوی کهن (ع۲1ها5 4ل#لاتت صا0): پسگشت‌ها شمیت دی
0۸ 9 ۶00200
لهستانی (8.ا۳0): 700۸ ای اس : +87
بلغاری‌کهن (/(من۶ ناه صهام: 05230۸ سس ها
لیتوانی (۵0۷ا(فلا77/ا): ۱ ادها 4 (507) ,1320 (130) رت
پروسی کهن (/(4ا۶5تا۶۸ ۰:۵۵ 150۸۲ 7 (11830) :005
ایرلندی کهن 183324 صا۵): رززد نا 9 (07880 ۰ 7
ولزی (7(کل#5): رزوی رده فرهنگ معین : ۱۸۸۵
برهان قاطع : ۱۱۳۲
بادداشت:
چم اين واژه در زبان برنانی: توده» انباشته» تل
چم اين واژه ذر زبان ابرلندی کهن و ولزی: گروه» گروه سربازان.
چم این واژه در ازبان‌های ژرمنی: گله» دسته‌ی گوسپند یاگاو» گروه.
اوستایی (4/887): ه6
پهلری (41ا(م۳۸): پسگشت‌ها اند ردان ]
,53731 ,575736 ۳
کردی (15]7ص0): ان ان ل2 الق از
آرمنی (4/48/1497): 5 6 (78۸8) بلنذ (00۵7)
لیتوانی ((۸ا ما2 لام 297 هم
51 ,کفکلق ات5 برهان قاطع + 1۱۳۴
یادهاشت:
چم اين واژه در اوستایی: تگرگك.
آوستابی (۸۷857۸2): هیک 07 5۸601 ,85۸360
پهلری (۲1ماتنهه): اففانی (پشتر) (ابلفتا0 ۳ ۰ هعلاه
: ۲
[pdf page 356]
```


## [2026-09-14T02:34:23.544Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ران (به چم\\|ران(به چم\\|«ران»\" incoming/ARY/ARY_pages.txt | head; echo \"=== try latin index RANA ===\"; grep -n -i \"RANA (AVESTAN\\|RAN (PAHLAVI\\|RAN (PERSIAN\" incoming/ARY/ARY_latin_index_pages.txt | head",
 "description": "Grep Aryanpur for ran"
}
```


### [2026-09-14T02:34:23.612Z] TOOL RESULT

```
4628:پدر و مادر پدران (به چم / ۱۵۹
=== try latin index RANA ===
1526:ARYEN (FRENCH) <1 ERA, ERANAG,ERAN (PAHLAVI) 5 sly,
2936:GAYR ARMENIAN) gs, VARAN, WARAN (PAHLAVI) 5 hay,
```


## [2026-09-14T02:34:29.072Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sri[sš]k\\|srišk\\|srisk\\|sresk\" NYB_vol2_glossary.txt NYB_vol1.txt | head; echo \"=== rān ===\"; grep -n \"rān \\|rān,\\|l'n'\" NYB_vol2_glossary.txt | head -5",
 "description": "Grep Nyberg"
}
```


### [2026-09-14T02:34:29.144Z] TOOL RESULT

```
NYB_vol2_glossary.txt:505:lapar [’pl; MDM, v. 2apar] adj. situated above, lying above: évak ~, apäk dit, v.s.v. žapāk (2); — heavenly, often in compounds: apar-apükeh etc., v. below; comp. ~-tar [’pltl] higher 5426, 581°, highest 1097; sup. ~-tom highest 415. 102°; v. also apartaréh; — adv. empha- sizing an adj.: highly, extremely: apar- aržānīk, v. aržānīk. — Av. (393) upara-, adv. upara (instr.), uparam; MPrth ’br adj. and adv. (MHC), comp. ’brdr, sup. ’brdwm; Ps. ?pldl; Paz. awartar, awardar (SGV); NP bar ‘height, top, summit’, bartar ‘higher’. ?apar [MDM, erroneous reading of OAram QDM] 1. adv. above: (3 päs) i-m guft ~ of which I spoke above 65°; či nümak" cé hac ~ nipišt" éstat the inscription that had been written here above P2:3, cf hacapar; — prev. over, on, upon, up, or simply expressing the initiation of the action, with varying vbs., cf esp. (@)ma- tan, burtan, grätan, raftan, rasitan ; follow- ed by enclitics: apar-p-im ravišn I must needs ascend 4076, v.s.v. -p(i); — refer- ring back to an encl. pron.: api-š Vidrafš . ~ mšast and V. got on it (the horse) 25W5; cē-t avdom margéh ~ raset for at the end Death will come upon thee 726-7; (martömän) tāi-šān āmēcišn ~ nē barend as long as one does not impart instruction to them 801. — 2. prep. a) local: over, on, on to, down on: Krisäsp ~ én damik raset K. is roaming all over this earth 3318; ~ giyāk on the spot 3", 102; ~ ki Zartuxst bé dahém where we shall deposit Z. 3957; ~ pad ēstāt rose to his feet 1821; asp ... — rahy vartét harness the horse! 5418-14; srišk ~ srišk drop after drop 214
NYB_vol2_glossary.txt:2783:4321, 4874, 4912.25, 548.10, 10917; srišk srišk drop by drop incessantly 412°,
NYB_vol2_glossary.txt:3510:srišk [slyšk'; slšk'] drop 211. 412°, 8920, — Av. (1645) sraska- 'tear'; MPrth srsk (List 87); NP sirisk.
NYB_vol2_glossary.txt:5354:sraska-: srišk
NYB_vol2_glossary.txt:7404:sirišk: srišk
=== rān ===
473:ap [MY”; ’p' 607. 787. 862.6, 878-11] water 1416-26 and passim; pl. cas. obl. āpān Dp?n'] 1095. — Av. (325 sqq.) āp-, OP āpt-; MPrthPrs ’b; Paz. āw, àv; NP ab. - V. dp-cthrak, āp-sārān, āpīk.
554:apäyistan ['p'dstn'], apāyītan [’p’dytn'] apäy-, 3d p. sg. apāyēt [’p’dt', ^p'dyt'], 3d p. pl. apäyend ['p'dynd], pret. 3d p. sg. apāyist 1. to please a p. (pat) 83%; cigon mēnēyān apäyist as it had pleased (was predestinated by) the heavenly gods 405, v. below. — 2. impers. it is desirable: -m apāyēt 6 han ciš I desire, try to obtain, this 562%, — 3. to be needed 1211-2 also pat. kär. apāyet 14%. 375, andar apāyēnd 105%. — 4. to be proper, seemly 4015 (bē ~). — 5. impers. apäyet auxiliary vb.: must, ought to, shall, should, has to, is bound to, ete. with the p. as indir. obj. (virtual dat.), a) governing an inf., which is as a rule placed after: u api-t xvatāyēh i Ērān šahr vas sal apäyet kartan and thou shalt exercise dominion over Iran for many years 629-31; 918-19, ]014 ete.; in this case preverbs to the inf. are drawn to apäyet; bé — pursitan 1319; ba ~ hištan 1313; kār-ē i apar nē ~ kartan 104%; apārīk 6 [KN] ~ xtartan 94??; less often the inf. is placed before: ēzatan nē ~ 1017-19; pit u mat frazand i xueš rād En and kär u kirpak ... bē üámóxtan ~ the parents shall teach 6522-23; 6519-20; 9113; the inf. sometimes has to be supplied: -
607:äp-särän ['ps'l'n'] rainy: pat ~ rēc 7128, Paz. pa äwsärq rož.
650:Artaxšērān [’lthsdl’n'] 1413. 1512-17, Arta- šērān [*ltšdl*n'] 114-116, patron.
763:ütur ['twr'; inser. ’twry] fire, referring to the old Iranian fire cult: ~ yazét god Ātur 25?; ~ farröbäg, gušnasp u burzen mihr the names of the three sacred fires connected with the three classes of the old Iranian society 118, explained 27-9; ~ farröbäg, i -bag 974. 9511; ~ gusnasp 955; ~burzén mihr 95%; ~-dn šāh the head of the sacred fires 1222-23, 131; — sal 58, āturv i Artaxšahr säl 40, āturv Šahpuhr i āturān šāh sal 24 SPrs:1-3 = sar 58, ātarē Artaxéahr sar 40, ātarē Šāhēpuhr ātarūn xšāh sār 24 SPrth:1-3: ‘... of the year 58 (viz.) the year 40 (of =) after the (enthronement) fire of Artax- Sahr, the year 24 (of =) after the (en- thronement) fire of Sahpuhr, the head of the fires’, which means the year 266 A.D., v. Christensen apud Ghirshman, Rev. des arts asiatiques X, 1936, 127—128 (the year 40 reckoned from the coronation of A. in the year 226, the year 24 reckoned from the coronation of S. in the year 242, and the year 58 reckoned from what must have been the epochal year of Sassanid time-reckoning, viz. 208 A. D.). — [~ the name of the 9th day of the month, also of the 9th month of the year; dade (q.v.) pat — the name of the 8th day of the month: FrP 28.] — Av. v.s. v. ätaxs; Prth ätarö (g. v.); MPrthPrs ’dwr; Paz. ädur; NP āčar, ādar. As to the three sacred fires v. Christensen, Sass. 164— 167; cf also de Menasee, Feux (1964); Mary Boyce, BSOAS XXXI, 1968, 52- 68, 270-289.
```


## [2026-09-14T02:34:37.133Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"srisk\\|srišk\\|sresk\\|srešk\\|slyšk\\|sl(y)šk\" SNS_pages.txt SNS.txt | head; echo \"=== page 183 area ===\"; grep -n \"\\[pdf page\" SNS_pages.txt | head -3",
 "description": "Grep SNS for sresk"
}
```


### [2026-09-14T02:34:37.221Z] TOOL RESULT

```
=== page 183 area ===
```


## [2026-09-14T02:34:40.857Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('npages',len(pages))\n\" ; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))['SNS'];print(json.dumps(d,ensure_ascii=False,indent=1))\"",
 "description": "Check SNS structure"
}
```


### [2026-09-14T02:34:42.269Z] TOOL RESULT

```
npages 243
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


## [2026-09-14T02:34:46.788Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==184' SNS_pages.txt | head -25",
 "description": "Print SNS leaf 184"
}
```


### [2026-09-14T02:34:47.843Z] TOOL RESULT

```
                                                                                                                                 Lxi^--UA.L*3l3                                                     YYY
                              i   .'- \   '"--^l- «*L «3^
XX
                                                                                                          .fr/Y^ .cJj*«.ii. stad:.                                   --,t:        vm*^»v
                                                                                                 jjjAu-^   -   a-j*5. AiiL- :stanend:                                ,nd:          *t*-***
                                          (Mir. Man. II, 50>dwswx
f/n^ ^-Y-A/A^-Y/^
                                                                              :
.

                                                          •a/iy^    n/ir^ -ya
                                                                                                                                                                                     ^\^_> «*-»»*
                                                                                             rf/Y^-o^/'O^ *- :st3nisn: yNSBWN, In:
                                                                                                                   1




    (Mir. Man. III/54)dyjw'r               :     ^V   (
                                                            -«i^**
                                                                                                                                                                                                     J«
                                                                                             >"»«-*»* lsU*)        .Aiib- :st3n5h:                      yNSBVTN, yh:                  )fc*«J->
```


## [2026-09-14T02:34:53.278Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 182 183; do echo \"### leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' SNS_pages.txt | grep -o \"sr[a-zöē̆ïš0-9]*\\|:s[a-z]*:\" | head -20; done",
 "description": "Scan SNS leaves 182-183"
}
```


### [2026-09-14T02:34:54.306Z] TOOL RESULT

```
### leaf 182
### leaf 183
srav
sravah
srab
:stadan:
```


## [2026-09-14T02:35:00.737Z] TOOL CALL #66: Bash

```json
{
 "command": "timeout 180 python3 tools/ref_page.py SNS:183 --image 2>&1 | tail -20",
 "description": "Try rendering SNS page 183"
}
```


### [2026-09-14T02:35:01.850Z] TOOL RESULT

```
no scan of SNS covers printed page 183 (see 'scans' in refs_online.json)
```


## [2026-09-14T02:35:11.080Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"شراب\" FVQ_pages.txt 2>/dev/null; grep -n -i \"sharab\\|sharba\" FVQ_pages.txt AFM_pages.txt incoming/PLA/PLA_pages.txt 2>/dev/null | head -5; echo \"(done)\"",
 "description": "Grep Jeffery, Addi Shir, Asbaghi"
}
```


### [2026-09-14T02:35:11.148Z] TOOL RESULT

```
0
(done)
```


## [2026-09-14T02:35:13.672Z] TOOL CALL #68: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D8%B4%D8%B1%D8%A8%D8%AA/\" \"https://abadis.ir/fatofa/%D8%B3%D8%B1%D8%B4%DA%A9/\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 472, Mo'in entry\" 2>&1 | tail -1; done",
 "description": "Fetch abadis for Moin entries"
}
```


### [2026-09-14T02:35:18.038Z] TOOL RESULT

```
### https://abadis.ir/fatofa/%D8%B4%D8%B1%D8%A8%D8%AA/
/home/sfmqrb/git/rishe/data/verification/sources/web/44de4742a7ac432b.txt
### https://abadis.ir/fatofa/%D8%B3%D8%B1%D8%B4%DA%A9/
/home/sfmqrb/git/rishe/data/verification/sources/web/0ced8de0feff459d.txt
```


## [2026-09-14T02:35:21.550Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 44de4742a7ac432b 0ced8de0feff459d; do echo \"##### $f\"; head -4 $f.txt; grep -n -m3 -A6 \"فرهنگ معین\\|معین\" $f.txt | head -25; done",
 "description": "Read abadis Moin entries"
}
```


### [2026-09-14T02:35:22.664Z] TOOL RESULT

```
##### 44de4742a7ac432b
URL: https://abadis.ir/fatofa/%D8%B4%D8%B1%D8%A8%D8%AA/
FETCHED: 2026-09-14T02:35:16Z
STATUS: 200
TITLE: شربت - معنی در دیکشنری آبادیس
54: فرهنگ معین
55-
56- (شَ بَ ) [ ع . شربة ] (اِ. ) در فارسی : ۱ - نوشیدنی . ۲ - آب آمیخته با شکر یا عصارة میوه . 
57-
58- فرهنگ عمید
59-
60- ۱. مقداری از آشامیدنی که به یک بار آشامیده شود.
--
208: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
209-
210- لینک ها 
211-
212- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
213-
214- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
##### 0ced8de0feff459d
URL: https://abadis.ir/fatofa/%D8%B3%D8%B1%D8%B4%DA%A9/
FETCHED: 2026-09-14T02:35:18Z
STATUS: 200
TITLE: سرشک - معنی در دیکشنری آبادیس
18: سرشک. [ س ِ رِ ] ( اِ ) اوستا «سرسکا» ( تگرگ ). سرشک فارسی شاید از پارتی «سرسک » ( قطره ) باشد. در پهلوی «سریشک » ( قطره ). «زرشک و سرشک ، انبرباریس بود». ( لغت فرس ص 306 ). ( حاشیه برهان قاطع چ معین ). اشک چشم. ( برهان ) ( آنندراج ). آب چشم که آن را اشک نیز گویند. ( غیاث ) : 
19-ای آنکه غمگنی و سزاواری 
20-و اندر نهان سرشک همی باری. رودکی.
21-سرشک دیده به رخسار تو فروبارد
22-هر آنگهی که بر آماجگاه او گذری. عماره مروزی.
23-ببارید پیران ز مژگان سرشک 
24-تن پیلسم درگذشت از پزشک. فردوسی.
--
62: فرهنگ معین
63-
64- (س رِ ) (اِ. ) قطرة اشک . 
65-
66- فرهنگ عمید
67-
68- ۱. قطرۀ آب چشم که هنگام گریستن فرو چکد، اشک، قطره.
--
106:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
107-• غلط ننویسیم، ابوالحسن نجفی، مرکز نشر دانشگاهی، تهران، ۱۳۸۶
108-• فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
109-
110- م. سرشک تخلص آقای محمدرضا شفیعی کدکنی هستش
111-
112- توی متن شعر بهار دلنشین هم بود، بگین مصراعشو بی زحمت. . .
```


## [2026-09-14T02:35:31.033Z] TOOL CALL #70: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check script"
}
```


### [2026-09-14T02:35:31.082Z] TOOL RESULT

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


## [2026-09-14T02:35:37.333Z] TOOL CALL #71: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg472.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/472.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/472.png",
 "description": "Copy page image for audit"
}
```


### [2026-09-14T02:35:37.411Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 60397 Sep 13 22:35 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/472.png
```


## [2026-09-14T02:36:15.806Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -4 705d689d1e133e0a.txt",
 "description": "Check sherbet fetch status"
}
```


### [2026-09-14T02:36:15.853Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/sherbet
FETCHED: 2026-09-14T02:32:48Z
STATUS: 200
TITLE: sherbet - Wiktionary, the free dictionary
```


## [2026-09-14T02:36:18.498Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i -m2 -A3 \"Ottoman Turkish\\|Turkish شربت\\|şerbet\" 705d689d1e133e0a.txt | head -20",
 "description": "Read wiktionary sherbet etymology"
}
```


### [2026-09-14T02:36:18.561Z] TOOL RESULT

```
203: Ottoman Turkish شربت ( şerbet ) bor. 
204- English sherbet 
205-
206: Borrowed from Ottoman Turkish شربت ( şerbet ) , borrowed from Classical Persian شَرْبَت ( šarbat ) , borrowed from Arabic شَرْبَة ( šarba ) , from شَرِبَ ( šariba ) .
207-
208- Doublet of sorbet and sharbat , related to syrup .
209-
```


## [2026-09-14T02:42:24.471Z] TOOL CALL #74: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-472.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_SHERBET = \"https://en.wiktionary.org/wiki/sherbet\"\nW_SHARBAT = \"https://en.wiktionary.org/wiki/%D8%B4%D8%B1%D8%A8%D8%AA\"\nW_SHARAB  = \"https://en.wiktionary.org/wiki/%D8%B4%D8%B1%D8%A7%D8%A8\"\nE_SYRUP   = \"https://www.etymonline.com/word/syrup\"\nW_RAN     = \"https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D9%86\"\nA_SHARBAT = \"https://abadis.ir/fatofa/%D8%B4%D8%B1%D8%A8%D8%AA/\"\nA_SERESHK = \"https://abadis.ir/fatofa/%D8%B3%D8%B1%D8%B4%DA%A9/\"\n\nFVA_NC = {\"ref\": \"FVA:208\", \"status\": \"not_checked\",\n          \"note\": \"FVA = S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368/1989); refs_online.json records that no digital copy exists on any permitted platform, so p.208 could not be read.\"}\n\ndoc = {\n \"pdf_page\": 472,\n \"book_page\": 442,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": []\n}\n\n# ---------------------------------------------------------------- entry 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Š.r.b\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Arabic root ش ر ب š-r-b, verb شَرِبَ šariba 'he drank'\",\n \"note\": (\"The root box is right: Arabic ش ر ب, base verb شَرِبَ šariba 'to drink', with the \"\n          \"nouns شَراب šarāb 'beverage, wine', شُرْب šurb 'drinking' and شَرْبة šarba 'a single draught'. \"\n          \"Every Western authority consulted (Klein s.v. sherbet/sirup, Skeat, Lokotsch no. 1838, \"\n          \"Devic s.v. Sirop, Etymonline) starts the sherbet/syrup/sorbet/shrub family from exactly this verb. \"\n          \"Nourai's only citation, FVA:208, is a book with no digital copy, so it could not be checked. \"\n          \"TWO CAVEATS ON THIS CHART: (a) the Latin box prints 'siripus', which is not a Latin form \"\n          \"(Medieval Latin is sirupus / syrupus / siropus) — see node #5; (b) the printed chart draws the \"\n          \"arrow into the Latin box from the Arabic šarâb box (node #1), not from the root box: the JSON's \"\n          \"\\\"parent\\\": 0 on node #5 is an extraction error (see the page image in \"\n          \"data/verification/sources/refs/ocr/BOOK/472.png).\"),\n \"note_fa\": (\"ریشهٔ سه‌حرفی عربی «ش ر ب» با فعل شَرِبَ «نوشید» و اسم‌های شَراب، شُرْب و شَرْبة. \"\n             \"همهٔ فرهنگ‌های ریشه‌شناسی غربی (کلاین، اسکیت، لوکوچ ش۱۸۳۸، دویک، اتیمانلاین) خانوادهٔ \"\n             \"sherbet / syrup / sorbet را از همین فعل می‌گیرند؛ پس جعبهٔ ریشه درست است. مأخذ خودِ نورایی \"\n             \"(FVA:208) نسخهٔ دیجیتال ندارد و بررسی‌پذیر نبود. دو نکته: صورت لاتینی «siripus» در کتاب \"\n             \"غلط چاپی است (درستش sirupus/syrupus) و پیکانِ جعبهٔ لاتین در صفحهٔ چاپی از جعبهٔ عربیِ \"\n             \"šarâb می‌آید نه از خود ریشه — که خطای استخراج داده است.\"),\n \"sources\": [W_SHERBET, E_SYRUP],\n \"ref_check\": [FVA_NC],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1434 s.v. sherbet\", \"stance\": \"supports\",\n    \"note\": \"'sherbet, n., a drink made of diluted fruit juice and sugar. — Turk., Pers. sherbet, fr. Arab. shurbaⁿ, ‘one drink’, fr. sharab, ‘drink, beverage’, fr. shariba, ‘he drank’' (KLN_1966.txt line 34962).\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1838\", \"stance\": \"supports\",\n    \"note\": \"Lokotsch: 'Ar. šarāb ‘Trank’ [Vb. šariba ‘trinken’], hieraus mlat. sirōpus, sirūpus, it. sciroppo, frz. sirop … engl. syrop, syrup; … Aus der gleichbedeutenden ar. Form šurba, šarba wurde … über tk. šerbet it. sorbetto … engl. sherbet, shrub' (LKT.txt line 4167).\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. Sherbet / syrup\", \"stance\": \"supports\",\n    \"note\": \"Skeat: 'Sherbet, a drink. (Arab.) Arab. sharbat, a drink, draught, sherbet, syrup. — Arab. root shariba, he drank'; and 'syrup, sirup … Arab. sharab, shurab, wine, beverage, syrup. — Arab. root shariba' (SKT.txt line 17101).\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Arabic\", \"words\": \"šarâb\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Arabic شَراب šarāb is the ordinary noun of the base verb شَرِبَ šariba 'he drank' \"\n   \"(form-I fa'āl noun of the root ش ر ب), meaning 'drink, beverage' and, in poetry and in later usage, 'wine'. \"\n   \"It is a native Arabic formation, already Qur'anic (e.g. Q 16:69 fīhi šifāʾun lin-nās, of honey as a šarāb), \"\n   \"and it is the etymon from which every European member of this family is drawn. Klein and Skeat both give \"\n   \"the same one-step derivation šariba → šarāb; Lokotsch no. 1838 heads his article 'Ar. šarāb «Trank» [Vb. šariba «trinken»]'. \"\n   \"Jeffery's Foreign Vocabulary of the Qur'an does not list it, which is itself confirmation: it is not a loanword in Arabic.\"),\n \"derivation_fa\": (\"«شَراب» اسمِ فعلِ شَرِبَ از ریشهٔ عربیِ «ش ر ب» است (وزن فَعال) به معنی «نوشیدنی» و در کاربرد \"\n   \"متأخر و شعری «می». واژه عربیِ اصیل است؛ جفری آن را در «واژگان دخیل در قرآن» نیاورده و همین نشان می‌دهد که \"\n   \"وام‌واژه نیست. کلاین و اسکیت هر دو همین اشتقاق یک‌مرحله‌ای šariba ← šarāb را می‌دهند و لوکوچ (ش۱۸۳۸) نیز مقالهٔ \"\n   \"خود را با همین صورت آغاز می‌کند. ادعای نورایی درست است.\"),\n \"sources\": [W_SHARAB],\n \"ref_check\": [FVA_NC],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1434 s.v. sherbet; p. 1450 s.v. sirup\", \"stance\": \"supports\",\n    \"note\": \"'… fr. sharab, ‘drink, beverage’, fr. shariba, ‘he drank’' (KLN_1966.txt line 34962); 'fr. Arab. sharab, ‘drink, beverage’, from the stem of shariba' (line 35355).\"},\n   {\"src\": \"FVQ\", \"where\": \"grep 'شراب' / 'sharab' in FVQ_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"No entry: Jeffery does not treat شراب as a foreign word in the Qur'an, i.e. it is native Arabic.\"},\n   {\"src\": \"DEV\", \"where\": \"s.v. Sirop\", \"stance\": \"supports\",\n    \"note\": \"Devic: 'De l’arabe شراب charâb, boisson, vin, café, venant du verbe شرب charib, boire' (DEV.txt line 2125).\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"šarâb «شراب»; šarbat «شربت»\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Both words are Arabic loans in New Persian, taken over after the Islamic conquest and fully \"\n   \"naturalised by the 4th/10th century (Hāfez's line quoted in the box turns on šurb). شراب šarāb is a direct \"\n   \"borrowing of Arabic šarāb, with the meaning narrowed in Persian usage to 'wine' — Wiktionary: 'Borrowed from \"\n   \"Arabic شَرَاب (šarāb)'. The box's extra forms مشروب mašrūb (Ar. passive participle 'drunk' → 'beverage') and \"\n   \"شُرب šurb (Ar. verbal noun 'drinking') are likewise straight Arabic borrowings from the same root. \"\n   \"The one imprecision is شربت šarbat: its Arabic source is not šarāb but the nomen unitatis شَرْبة šarba(t) \"\n   \"'one draught' (فَعْلة of the same root), Persian keeping the tāʾ marbūṭa as -at; Mo'in's dictionary tags it \"\n   \"exactly '[ع. شربة]' ('(شَ بَ) [ع. شربة] (اِ.) در فارسی: ۱- نوشیدنی'). So the node is right about language and \"\n   \"direction but draws šarbat from the sister noun šarāb instead of from šarba — hence 'plausible' rather than 'confirmed'.\"),\n \"derivation_fa\": (\"هر دو واژه معرّب نیستند بلکه وام‌واژهٔ عربی در فارسی نو‌اند: «شراب» گرتهٔ مستقیم عربی شَراب است \"\n   \"که در فارسی معنایش به «می» تخصیص یافته، و «مشروب» (اسم مفعول) و «شُرب» (مصدر) نیز از همان ریشه به فارسی آمده‌اند. \"\n   \"تنها نکتهٔ نادرست این است که مأخذ «شربت» در عربی شَراب نیست، بلکه شَرْبة (اسم مرّه بر وزن فَعْلة) است که تاء \"\n   \"مربوطهٔ آن در فارسی به «ت» بدل شده؛ معین هم در ذیل «شربت» می‌نویسد «[ع. شربة]». پس ادعای نورایی در کلیت درست \"\n   \"است ولی پیکانِ «شربت» باید از شَرْبة کشیده می‌شد نه از شَراب — با احتیاط پذیرفتنی است.\"),\n \"sources\": [W_SHARAB, W_SHARBAT, A_SHARBAT],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"supports\",\n    \"note\": \"Mo'in's Farhang-e Farsi s.v. شربت (read via abadis.ir, section فرهنگ معین): '(شَ بَ ) [ ع . شربة ] (اِ. ) در فارسی : ۱ - نوشیدنی . ۲ - آب آمیخته با شکر یا عصارة میوه' — Arabic origin confirmed, but from شربة, not شراب.\"},\n   FVA_NC\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. شربت (vajehyab/abadis text of Farhang-e Farsi)\", \"stance\": \"partial\",\n    \"note\": \"'[ ع . شربة ]' — Mo'in derives Persian شربت from Arabic شربة, not from شراب.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1434 s.v. sherbet\", \"stance\": \"supports\",\n    \"note\": \"Klein has the same chain through Persian: 'Turk., Pers. sherbet, fr. Arab. shurbaⁿ, ‘one drink’' — i.e. the Persian word comes from the Arabic unit-noun.\"},\n   {\"src\": \"PLA\", \"where\": \"grep 'sharab'/'sharba' in PLA_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"Asbaghi (Persian loanwords IN Arabic) has nothing here, as expected: the traffic is the other way round.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Turkish\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"A pass-through box with no word printed: the intended form is Ottoman Turkish شربت şerbet \"\n   \"(modern Turkish şerbet) 'a sweet cold fruit drink'. Wiktionary classifies it under 'Ottoman Turkish terms \"\n   \"borrowed from Classical Persian' and derives it from Classical Persian شَرْبَت šarbat, itself from Arabic شَرْبَة \"\n   \"šarba — exactly the Persian → Turkish arrow drawn here. The Turkish form kept the Persian -at as -et by \"\n   \"front-vowel harmony (šarbat → şerbet), and it is the Ottoman drink, not the Persian or Arabic one, that \"\n   \"Europeans met and named in the 16th–17th centuries.\"),\n \"derivation_fa\": (\"این جعبه تهی است و واژهٔ مقصود ترکی عثمانی «شربت» şerbet است. ویکی‌واژه آن را وام‌واژه از \"\n   \"فارسیِ کلاسیک شَرْبَت می‌داند (و آن از عربی شَرْبة)؛ یعنی همان پیکانِ فارسی ← ترکی که نورایی کشیده است. \"\n   \"تغییر آوایی روشن است: هماهنگی واکه‌ای ترکی، šarbat را به şerbet بدل کرده. ادعای نورایی درست است.\"),\n \"sources\": [W_SHERBET, W_SHARBAT],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box.\"}],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no. 1838\", \"stance\": \"supports\",\n    \"note\": \"'… wurde zur Bezeichnung eines kühlenden Trankes über tk. šerbet ‘Kühltrank’ it. sorbetto … engl. sherbet, shrub, dtsch. Sorbet, Scherbet' (LKT.txt line 4167).\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1434 s.v. sherbet\", \"stance\": \"supports\",\n    \"note\": \"'Turk., Pers. sherbet, fr. Arab. shurbaⁿ' — Turkish is the immediate donor to English, Persian the donor to Turkish.\"},\n   {\"src\": \"PHN\", \"where\": \"s.v. SORBET\", \"stance\": \"partial\",\n    \"note\": \"Pihan discusses the Turkish word behind sorbet and warns against the folk-etymological link with Latin sorbitio, 'que sorbet dérive du substantif latin sorbitio' being only an appearance (PHN.txt line 9286).\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"sherbet\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English sherbet is first recorded in the 1580s (early spellings zerbet, cherbet, sorbet; \"\n   \"the intrusive-r form sherbert from the 1670s), brought back by travellers to the Ottoman lands as the name \"\n   \"of a cooled drink of diluted fruit juice and sugar. Etymonline: 'from Turkish serbet, from Persian sharbat, \"\n   \"from Arabic sharba(t) \\\"a drink,\\\" from shariba \\\"he drank\\\"'; Wiktionary gives the identical chain and notes \"\n   \"that sherbet is a doublet of sorbet (the same Turkish word via Italian sorbetto and French) and related to syrup. \"\n   \"Klein p.1434, the page Nourai cites, gives Turk. ← Pers. ← Arab. and cross-refers to sirup, shrub and sorbet — \"\n   \"precisely this chart's two branches.\"),\n \"derivation_fa\": (\"انگلیسی sherbet نخستین بار در دههٔ ۱۵۸۰ ثبت شده (به صورت‌های zerbet و cherbet) و از راه \"\n   \"سفرنامه‌نویسان از قلمرو عثمانی به اروپا رفته است: ترکی şerbet ← فارسی شربت ← عربی شَرْبة ← شَرِبَ. \"\n   \"اتیمانلاین و ویکی‌واژه هر دو همین زنجیره را می‌دهند و sherbet را دوگانهٔ (doublet) sorbet و هم‌ریشهٔ syrup می‌شمارند. \"\n   \"کلاین در همان صفحهٔ ۱۴۳۴ که نورایی ارجاع داده همین را نوشته است. ادعای نورایی درست است.\"),\n \"sources\": [W_SHERBET, E_SYRUP],\n \"ref_check\": [\n   {\"ref\": \"KLN:1434\", \"status\": \"supports\",\n    \"note\": \"Klein 1966 p.1434: 'sherbet, n., a drink made of diluted fruit juice and sugar. — Turk., Pers. sherbet, fr. Arab. shurbaⁿ, ‘one drink’, fr. sharab, ‘drink, beverage’, fr. shariba, ‘he drank’ … Cp. sirup, shrub, ‘a drink’, sorbet' (KLN_1966.txt line 34962, in the s-h-e-r run of headwords).\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"s.v. Sherbet\", \"stance\": \"partial\",\n    \"note\": \"'Sherbet, a drink. (Arab.) Arab. sharbat, a drink, draught, sherbet, syrup. — Arab. root shariba' (SKT.txt line 17101) — same origin, but Skeat skips the Turkish and Persian stages.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1838\", \"stance\": \"supports\",\n    \"note\": \"'… über tk. šerbet … engl. sherbet, shrub' (LKT.txt line 4167).\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Latin\", \"words\": \"siripus\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"siripus\",\n \"correct_form\": \"sirupus / syrupus (also siropus), Medieval Latin\",\n \"derivation\": (\"The word is real and the derivation is right, but the form printed is not. There is no Latin \"\n   \"*siripus: the pharmacists' Medieval Latin word, taken from Arabic شراب šarāb 'beverage' in the Salerno/Toledo \"\n   \"translations of Arabic medicine (11th–13th c.), is sirupus, syrupus, siropus. Klein p.1450, the page Nourai \"\n   \"cites, prints 'ML. sirupus, syrupus'; Lokotsch no. 1838 'mlat. sirōpus, sirūpus'; Devic s.v. Sirop 'bas lat. \"\n   \"syrupus, siruppus, sciruppus'. Arabic -ā- was rendered by the Latin -u- of the second syllable through the \"\n   \"Spanish/Italian intermediaries (Sp. jarabe/jarope, It. sciroppo). I checked the printed page (PDF p.472, book \"\n   \"p.442, image saved as data/verification/sources/refs/ocr/BOOK/472.png): the box really does read 'siripus : a \"\n   \"drink', so the extraction is faithful and the misprint is Nourai's. The label 'Latin' should also be 'Medieval \"\n   \"Latin' — the word is unknown to classical Latin. SEPARATE POINT: on the printed page the arrow into this box \"\n   \"comes down from the Arabic šarâb box (node #1), not from the root box; the JSON's \\\"parent\\\": 0 is an \"\n   \"extraction error, and the derivation described here is Arabic šarāb → ML sirupus, which is also Klein's route.\"),\n \"derivation_fa\": (\"اشتقاق درست است ولی صورتِ چاپ‌شده نادرست: در لاتینی صورتی به شکل *siripus وجود ندارد. واژهٔ \"\n   \"لاتینیِ میانه (لاتینِ پزشکان) که از عربی «شراب» در ترجمه‌های طب عربی در سالرنو و طلیطله (سده‌های ۱۱ تا ۱۳ م.) \"\n   \"گرفته شده sirupus / syrupus / siropus است؛ کلاین در همان ص۱۴۵۰ «ML. sirupus, syrupus» و لوکوچ «mlat. sirōpus, \"\n   \"sirūpus» و دویک «bas lat. syrupus, siruppus» می‌نویسند. صفحهٔ چاپیِ کتاب را دیدم (تصویر در \"\n   \"data/verification/sources/refs/ocr/BOOK/472.png): در خودِ کتاب «siripus» چاپ شده، پس خطا از نورایی است نه از \"\n   \"خوانشِ اسکن. برچسب «Latin» هم باید «لاتینی میانه» می‌بود. افزون بر این، در صفحهٔ چاپی پیکان این جعبه از جعبهٔ \"\n   \"عربیِ šarâb می‌آید نه از خود ریشه؛ «parent: 0» در داده خطای استخراج است.\"),\n \"sources\": [E_SYRUP],\n \"ref_check\": [\n   {\"ref\": \"KLN:1450\", \"status\": \"partial\",\n    \"note\": \"Klein 1966 p.1450: 'sirup, syrup, n. — ME. sirop, sirup, fr. OF. (= F.) sirup, fr. ML. sirupus, syrupus, fr. Arab. sharab, ‘drink, beverage’, from the stem of shariba, ‘he drank’' (KLN_1966.txt line 35355). Supports the Arabic → Medieval Latin → French → English chain, but prints sirupus/syrupus — not Nourai's 'siripus'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no. 1838\", \"stance\": \"partial\",\n    \"note\": \"'hieraus mlat. sirōpus, sirūpus, it. sciroppo, siroppo, frz. sirop, syrop … engl. syrop, syrup' (LKT.txt line 4167) — no *siripus.\"},\n   {\"src\": \"DEV\", \"where\": \"s.v. Sirop\", \"stance\": \"partial\",\n    \"note\": \"'ital. siroppo, sciroppo, bas lat. syrupus, siruppus, sciruppus. De l’arabe شراب charâb' (DEV.txt line 2125) — again no form with -i- in the second syllable.\"},\n   {\"src\": \"PHN\", \"where\": \"s.v. SIROP\", \"stance\": \"supports\",\n    \"note\": \"Pihan has a full article SIROP, s. m. (a.) among the French words from Arabic (PHN.txt line 9200; index 'Sirop, s. m. (a.) 336').\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Empty pass-through box: the form meant is Old French sirop (13th c.), continued unchanged as \"\n   \"modern French sirop. Etymonline derives English syrup 'from Old French sirop \\\"sugared drink\\\" (13c.), and \"\n   \"perhaps from Italian siroppo, both from Arabic sharab'; Klein routes the French word through ML sirupus. \"\n   \"The final -us of the Latin was dropped in the normal Gallo-Romance way and the word entered French as a \"\n   \"medical/apothecary term, which is how it then reached English.\"),\n \"derivation_fa\": (\"این جعبه تهی است و صورتِ مقصود فرانسویِ کهن sirop (سدهٔ ۱۳ م.) است که بی‌تغییر به فرانسویِ \"\n   \"امروز رسیده. پایانهٔ -us لاتینی طبق قاعدهٔ گالو-رومی افتاده و واژه به عنوان اصطلاحی دارویی وارد فرانسه و از \"\n   \"آنجا وارد انگلیسی شده است. اتیمانلاین و کلاین هر دو همین را می‌گویند؛ ادعای نورایی درست است.\"),\n \"sources\": [E_SYRUP],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box; the chain is covered by KLN:1450 on the parent box.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1450 s.v. sirup\", \"stance\": \"supports\",\n    \"note\": \"'ME. sirop, sirup, fr. OF. (= F.) sirup, fr. ML. sirupus, syrupus' (KLN_1966.txt line 35355).\"},\n   {\"src\": \"DEV\", \"where\": \"s.v. Sirop\", \"stance\": \"supports\",\n    \"note\": \"Devic lists the French history: 'Vieux français essyrot (xiiiᵉ siècle), ysserop (xvᵉ siècle)' beside Prov. eissarop and Sp. jarabe (DEV.txt line 2125).\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 7, \"lang\": \"English\", \"words\": \"syrup\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"English syrup is attested from the late 14th century, spelt sirup/sirop, in medical writing \"\n   \"('thick, sweet liquid'), borrowed from Old French sirop; the y- spelling follows the Medieval Latin syrupus. \"\n   \"Etymonline and Klein agree, and both note that syrup and sherbet are doublets — the same Arabic root reaching \"\n   \"English twice, once through the Latin-Romance pharmacy tradition and once through Ottoman Turkish. \"\n   \"Skeat routes it through Spanish xarope instead of Latin, which is a variant but not an objection: all agree \"\n   \"the source is Arabic šarāb.\"),\n \"derivation_fa\": (\"انگلیسی syrup از اواخر سدهٔ ۱۴ م. به صورت sirup/sirop در متون پزشکی دیده می‌شود و از فرانسویِ \"\n   \"کهن sirop وام گرفته شده؛ املای y از لاتینیِ میانهٔ syrupus آمده است. syrup و sherbet دوگانه‌اند: یک ریشهٔ عربی \"\n   \"که دو بار به انگلیسی رسیده، یک‌بار از راه داروشناسیِ لاتینی-رومی و یک‌بار از راه ترکی عثمانی. اسکیت مسیر را از \"\n   \"اسپانیایی xarope می‌گیرد که تفاوتی جزئی است. ادعای نورایی درست است.\"),\n \"sources\": [E_SYRUP],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on this box; KLN:1450 on node #5 covers the whole chain.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 1450 s.v. sirup, syrup\", \"stance\": \"supports\",\n    \"note\": \"'ME. sirop, sirup, fr. OF. (= F.) sirup, fr. ML. sirupus, syrupus, fr. Arab. sharab … See sherbet' (KLN_1966.txt line 35355).\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. syrup, sirup\", \"stance\": \"partial\",\n    \"note\": \"'syrup, sirup. (F.—Span.—Arab.) … Span. xarope, a drink. — Arab. sharab, shurab, wine, beverage, syrup' (SKT.txt line 17101) — Spanish rather than Latin as the intermediary.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1838\", \"stance\": \"supports\",\n    \"note\": \"'… dtsch. Sirup, engl. syrop, syrup' (LKT.txt line 4167).\"}\n ]\n})\n\ndoc[\"entries\"].append(e0)\n\n# ---------------------------------------------------------------- entry 2\ne2 = {\n \"entry\": 2,\n \"root\": \"Srěno\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *srēn-/*sreno- 's-, -ā 'hip, loin, (outer) thigh' (Wiktionary: *srḗn-s)\",\n \"note\": (\"Pokorny p.1002 has exactly this lemma: 'sreno-, -ā Körperteilbenennung, etwa ‚Oberschenkel, \"\n          \"Lenden’', with Av. rāna- m., mp./np. rān and Lith. strėnos 'die Lenden, das Kreuz'. The language label \"\n          \"(Indo-European) and the gloss ('thigh, hip') are both right; Nourai's page number is right. It is worth \"\n          \"recording that the root is a narrow Irano-Baltic isogloss — Walde-Pokorny II 705 says 'Fick 339 zw.; \"\n          \"sehr wahrscheinliche Verknüpfung' ('doubtful per Fick; a very probable connection'), and Watkins/AHD \"\n          \"omits it altogether because it has no English reflex. Wiktionary reconstructs *srḗn-s > PII *srá̄nas > \"\n          \"Proto-Iranian *hrā́nah.\"),\n \"note_fa\": (\"پوکورنی در ص۱۰۰۲ همین ریشه را می‌آورد: «sreno-, -ā نام اندامی از تن، تقریباً ران و کمرگاه»، با \"\n             \"شواهدِ اوستایی rāna-، فارسیِ میانه و نوِ rān، و لیتوانیایی strėnos «کمرگاه». برچسبِ زبانی (هندواروپایی) \"\n             \"و معنای «ران، سرین» درست است و شمارهٔ صفحه هم درست. تنها باید افزود که این ریشه ایزوگلاسی تنگ میان \"\n             \"ایرانی و بالتی است: والده-پوکورنی (ج۲ ص۷۰۵) آن را «پیوندی بسیار محتمل» می‌خواند و واتکینز در پیوستِ \"\n             \"AHD اصلاً آن را نیاورده چون بازتابی در انگلیسی ندارد. ویکی‌واژه *srḗn-s را بازسازی می‌کند. \"\n             \"ادعای نورایی درست است.\"),\n \"sources\": [W_RAN],\n \"ref_check\": [\n   {\"ref\": \"POK:1002\", \"status\": \"supports\",\n    \"note\": \"Pokorny IEW p.1002: 'sreno-, -ä Körperteilbenennung, etwa ‚Oberschenkel, Lenden‘. Av. räna- m. ‚der äußere Teil des Oberschenkels, Oberschenkel‘, np. rän ‚Schenkel‘; lit. strėnos ‚die Lenden, das Kreuz‘. WP. II 705.' (POK_03.txt line 3324; POK_full.txt line 80924 gives the same lemma with 'Page(s): 1002').\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 705\", \"stance\": \"supports\",\n    \"note\": \"'sreno-, -ā Körperteilbenennung, etwa „Oberschenkel, Lenden“ — Av. rāna- m. … mp. np. rān „Schenkel“; lit. strėnos … Fick 339 zw.; sehr wahrscheinliche Verknüpfung' (WLD_Bd2 djvu line 45845).\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 appendix, s-r- run\", \"stance\": \"silent\",\n    \"note\": \"grep 'sreno' in AHD_watkins1985.txt: nothing — the appendix has only srebh-, srenk- and sreu-, since *sreno- left no English descendant.\"},\n   {\"src\": \"IEC\", \"where\": \"grep 'sreno'/'srēno' in IEC.txt\", \"stance\": \"silent\",\n    \"note\": \"Mann has no lemma for this root in the searchable text.\"}\n ],\n \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"râna 2\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Young Avestan rāna- m. 'the outer part of the thigh; the thigh (in general)', attested in the \"\n   \"Vidēvdād (V.8.59–61, V.18.16, opposed to haxt- 'the inner part of the thigh'). Bartholomae, Altiranisches \"\n   \"Wörterbuch col. 1513: 'j. rāna- m. «der äussere Teil des Oberschenkels; Oberschenkel (überhaupt)» … Nach Fick \"\n   \"VglWb.⁴ I 339 aus *srān-. — mp. (Pü.), np. rān «Schenkel»'. The '2' in Nourai's 'râna 2' is a homonym number: \"\n   \"Bartholomae has a second, Gathic ʾrana-/runa- 'combatant, contending party' (to the verb ar-), unrelated. \"\n   \"Phonetically the Avestan form shows the regular Iranian treatment of initial *sr-: PIE *srē-n- > PII *srā́na- > \"\n   \"Proto-Iranian *hrā́nah- > Av. rāna- (the *s- becomes h- before r and is then lost).\"),\n \"derivation_fa\": (\"اوستاییِ متأخر rāna- «بخش بیرونی ران؛ ران» که در وندیداد (فرگرد ۸ و ۱۸) در برابر haxt- «بخش \"\n   \"درونی ران» به کار رفته است. بارتولمه در «فرهنگ ایرانی باستان» ستون ۱۵۱۳ می‌نویسد: «j. rāna- m. der äussere \"\n   \"Teil des Oberschenkels … nach Fick aus *srān-. — mp., np. rān». عددِ ۲ در «râna 2» شمارهٔ هم‌نام است؛ بارتولمه \"\n   \"rana-/runa- گاهانی به معنی «رزمنده، طرف نزاع» را جدا آورده که بی‌ربط است. از نظر آوایی، *sr- آغازیِ \"\n   \"هندواروپایی در ایرانی باستان به *hr- بدل شده و سپس h افتاده است: *srē-n- ← *srā́na- ← *hrā́nah- ← rāna-. \"\n   \"ادعای نورایی درست است.\"),\n \"sources\": [W_RAN],\n \"ref_check\": [\n   {\"ref\": \"POK:1002\", \"status\": \"supports\",\n    \"note\": \"Pokorny p.1002 s.v. sreno-: 'Av. räna- m. ‚der äußere Teil des Oberschenkels, Oberschenkel‘' (POK_03.txt line 3325).\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 1513 s.v. rāna-\", \"stance\": \"supports\",\n    \"note\": \"'• j. rāna- m. ‘der äussere Teil des Oberschenkels’; Oberschenkel (überhaupt)’ … Nach Fick VglWb.⁴ I 339 aus *srān-. — mp. (Pü.), np. rān ‘Schenkel’' (BRT.txt line 25363).\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 705\", \"stance\": \"supports\",\n    \"note\": \"'Av. rāna- m. „der äußere Teil des Oberschenkels, Oberschenkel“' (WLD_Bd2 djvu line 45850).\"},\n   {\"src\": \"KNT\", \"where\": \"grep 'rana' in KNT_full.txt (Old Persian lexicon)\", \"stance\": \"silent\",\n    \"note\": \"No Old Persian cognate is attested; Kent has no entry, as expected for a body-part word absent from the inscriptions.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"rân «ران»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"New Persian ران rān 'thigh' is the direct continuant of Middle Persian rān (Pahlavi <lʾn'>), \"\n   \"itself from Old Iranian *hrāna- — so the true line is OIr. *hrāna- > MP rān > NP rān, with Avestan rāna- a \"\n   \"sister form rather than the literal ancestor; Nourai's Avestan → Persian arrow is his usual shorthand for that. \"\n   \"Horn, Grundriss no. 605 (p.135, the page cited) sets it out: 'rān «Schenkel». aw. rāna- «Schenkel»; phlv. rān, \"\n   \"rānpān, arm. LW. eran'. Mo'in's footnote in Borhan-e Qate' p.932 gives the same list (Av. rāna-, Pahl. rān, \"\n   \"Arm. eran, Kurd./Baluchi rān, Pashto wrūn, Mazandarani/Tabari rūn) and cites 'اشتقاق ۶۰۵' = Horn no. 605. \"\n   \"Wiktionary: 'Inherited from Middle Persian rān «thigh», from Proto-Iranian *hrā́nah, from Proto-Indo-Iranian \"\n   \"*srā́nas, from Proto-Indo-European *srḗn-s'. The long ā is unchanged; the colloquial Tehrani رون rūn shows the \"\n   \"later raising of ā before a nasal.\"),\n \"derivation_fa\": (\"«ران» در فارسی نو دنبالهٔ مستقیم فارسیِ میانهٔ rān (پهلوی ‹lʾn›) است و آن از ایرانیِ باستان \"\n   \"*hrāna-؛ پس مسیرِ راستین ایرانی باستان ← فارسی میانه ← فارسی نو است و اوستاییِ rāna- خواهرِ آن است نه نیایش، \"\n   \"هرچند نورایی طبق شیوهٔ همیشگی‌اش پیکان را از اوستایی کشیده است. هرن در «بنیاد ریشه‌شناسی فارسی نو» شمارهٔ ۶۰۵ \"\n   \"(همان ص۱۳۵ که نورایی ارجاع داده) می‌نویسد: «rān «ران». اوستایی rāna-؛ پهلوی rān، ارمنی (وام‌واژه) eran». \"\n   \"معین نیز در حاشیهٔ برهان قاطع ص۹۳۲ همین‌ها را می‌آورد و به «اشتقاق ۶۰۵» یعنی شمارهٔ هرن ارجاع می‌دهد. \"\n   \"آ کشیده بی‌تغییر مانده و «رون» گفتاری تهرانی از برافراشتنِ متأخرِ آ پیش از خیشوم است. ادعای نورایی درست است.\"),\n \"sources\": [W_RAN],\n \"ref_check\": [\n   {\"ref\": \"HRN:135\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss p.135 no. 605 (HRN.txt leaf 157 = printed p.135): '605. rān ‘Schenkel’. aw. rāna- ‘Schenkel’; phlv. rān, rānpān, arm. LW. eran, meist pl. eranḳ (Hübschmann, No. 96). kurd. bel. LW. rān; afġ. vrūn.'\"},\n   {\"ref\": \"BQT:932\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' ed. Mo'in, printed p.~932 (BQT_v2_pages.txt \\\\f-block 393): headword 'ران = بر وزن جان . معروف است و عربی فخذ گویند', with Mo'in's footnote 9: 'اوستا rāna- (ران) ، پهلوی rān ، ارمنی eran ، کردی و بلوچی rān ، افغانی wrūn ، اشتقاق ۶۰۵ ، طبری rūn' — 'اشتقاق ۶۰۵' is a reference to Horn no. 605.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 605, p.135\", \"stance\": \"supports\",\n    \"note\": \"See ref_check; Horn explicitly gives the Pahlavi stage phlv. rān between Avestan and New Persian.\"},\n   {\"src\": \"PHD\", \"where\": \"grep 'rān' in PHD.txt\", \"stance\": \"partial\",\n    \"note\": \"MacKenzie's Concise Pahlavi Dictionary is not searchable for this short word in the OCR, but Horn, Mo'in and Nyberg's transcriptions all give MP rān; Wiktionary cites MP lʾ nʹ /rān/.\"},\n   {\"src\": \"ARY\", \"where\": \"grep 'ران' / 'RANA' in ARY_pages.txt and ARY_latin_index_pages.txt\", \"stance\": \"silent\",\n    \"note\": \"No entry located in the OCR of Aryanpur's IE-roots dictionary.\"},\n   {\"src\": \"BQT\", \"where\": \"p. ~932, Mo'in's footnote 9\", \"stance\": \"supports\",\n    \"note\": \"See ref_check.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Sogdian\", \"words\": \"r`n`\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Sogdian r'n' (Christian script) /rān/ 'belt', with the derivative r'n'kh ranak 'belt'. \"\n   \"Gharib's Sogdian Dictionary entry 8435 (printed p.339, the page Nourai cites) reads: \\\"r'n' C — rāna \"\n   \"©<*Av. rāna-; Khot. rāna-; Oss. ron — belt\\\", with references to Gershevitch JRAS 1946, 180 and Bailey AO 1966, 34. \"\n   \"The word is thus the same Old Iranian *hrāna- 'thigh, loin', the sense having moved from the body part to \"\n   \"what girds it: 'loins' → 'what goes round the loins' → 'belt'. Ossetic ron 'belt' shows the identical shift, \"\n   \"which is the strongest argument that the Sogdian sense is old and not a chance homonym. The arrow should \"\n   \"strictly start from Old Iranian rather than from Avestan itself, but Gharib's own entry writes '<*Av. rāna-', \"\n   \"so Nourai is following his source exactly.\"),\n \"derivation_fa\": (\"سغدیِ r'n' (به خط مسیحی) /rān/ «کمربند» و مشتق آن r'n'kh «کمربند». قریب در «فرهنگ سغدی» \"\n   \"مدخل ۸۴۳۵ (همان ص۳۳۹ که نورایی ارجاع داده) می‌نویسد: «r'n' rāna < اوستایی rāna-؛ ختنی rāna-؛ آسی ron — belt». \"\n   \"پس همان *hrāna- ایرانی باستان است و تحول معنایی از اندام به آنچه بر آن اندام بسته می‌شود رخ داده: \"\n   \"«ران/کمرگاه» ← «آنچه بر کمرگاه می‌بندند» ← «کمربند». آسیِ ron «کمربند» همین دگرگونی را نشان می‌دهد و \"\n   \"بهترین گواه است که این معنا کهن است. ادعای نورایی درست است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:339\", \"status\": \"supports\",\n    \"note\": \"Gharib, Sogdian Dictionary, entry 8435 on printed p.339 (SOD_pages.txt, \\\\f-block 405; printed ≈ leaf − 66): \\\"8435 r'n' C / rāna ©<*Av. rāna-; Khot. rāna-; Oss. ron / r'n'kh / belt / BSTi 278; Gersh. JRAS 1946, 180; Bailey, AO 1966, 34\\\"; entry 8436 \\\"r'n'kh B / ranak ⇒ r'n' / belt\\\". The cited page number is exactly right.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"entries 8435–8436, printed p.339\", \"stance\": \"supports\", \"note\": \"See ref_check.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Khotanese; cited at second hand through Gharib\", \"stance\": \"supports\",\n    \"note\": \"Gharib's entry cites Khotanese rāna- and Bailey, Asia Major/AO 1966, 34 for the same equation.\"},\n   {\"src\": \"BRT\", \"where\": \"col. 1513 s.v. rāna-\", \"stance\": \"supports\",\n    \"note\": \"Bartholomae's *srān- base underlies the Sogdian form too; he lists the Middle and New Persian continuants.\"}\n ]\n})\n\ndoc[\"entries\"].append(e2)\n\n# ---------------------------------------------------------------- entry 3\ne3 = {\n \"entry\": 3,\n \"root\": \"Sresk\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *sresk- 'to drip, trickle' (Pokorny prints the lemma with a query mark)\",\n \"note\": (\"Pokorny p.1002 has 'sresk- ‚tropfen’?' — a lemma of exactly this shape and meaning at exactly the \"\n          \"cited page, so root, language label, gloss and page are all correct. Pokorny's own question mark, and \"\n          \"Walde-Pokorny II 602f./705, record that the reconstruction rests on a narrow base: Avestan srask-, \"\n          \"Armenian srskel 'to sprinkle' (which Hübschmann held to be an Iranian loan) and, only if the Armenian \"\n          \"word is a loan, Lithuanian šlakas 'drop', šlakėti 'to trickle' from *ḱlek-skō-. Watkins/AHD omits it \"\n          \"(no English reflex). So 'confirmed' for what the chart claims, with the caveat that this is one of \"\n          \"Pokorny's weaker roots.\"),\n \"note_fa\": (\"پوکورنی در ص۱۰۰۲ مدخل «sresk- «چکیدن»؟» را دارد؛ پس ریشه، برچسبِ زبانی، معنا و شمارهٔ صفحه \"\n             \"همه درست است. علامت پرسشِ خودِ پوکورنی و یادداشت والده-پوکورنی (ج۲ ص۶۰۲ و ۷۰۵) نشان می‌دهد که \"\n             \"بنیادِ این بازسازی تنگ است: اوستایی srask-، ارمنی srskel «افشاندن» (که هوبشمان آن را وام‌واژهٔ \"\n             \"ایرانی می‌دانست) و — تنها اگر واژهٔ ارمنی وام باشد — لیتوانیایی šlakas «قطره». واتکینز در پیوستِ \"\n             \"AHD آن را نیاورده چون بازتاب انگلیسی ندارد. ادعای نورایی درست است، با این احتیاط که این از \"\n             \"ریشه‌های سست‌بنیادِ پوکورنی است.\"),\n \"sources\": [A_SERESHK],\n \"ref_check\": [\n   {\"ref\": \"POK:1002\", \"status\": \"supports\",\n    \"note\": \"Pokorny IEW p.1002: 'sresk- ‚tropfen‘? Av. srask- (srasca-) ‚triefen, abtriefen von; triefregnen‘, sraska- m. (np. sirisk) ‚Träne, Weinen‘, mp. srixt ‚dropped‘, arm. srskel … WP. II 602 f., 705.' (POK_03.txt line 3326; POK_full.txt line 80836 'Root / lemma: sresk-, Meaning: to drizzle, Page(s): 1002').\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 705 (with II 602f.)\", \"stance\": \"supports\",\n    \"note\": \"'sresq- „tropfen“. Av. srask- (srasca-) … sraska- m. (np. sirisk) „Träne, Weinen“, mp. srixt „dropped“, arm. srᵏkel … S. Bartholomae Airan. Wb. 1644f. … Entlehnung des arm. Wortes aus dem arischen bekämpft Hübschmann IA. 10, 28' (WLD_Bd2 djvu line 45888).\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 appendix\", \"stance\": \"silent\",\n    \"note\": \"grep 'sresk' in AHD_watkins1985.txt: nothing — only srebh-, srenk-, sreu- appear, none of them this root.\"},\n   {\"src\": \"IEC\", \"where\": \"grep 'sresk' in IEC.txt\", \"stance\": \"silent\", \"note\": \"Mann has no such lemma in the searchable text.\"}\n ],\n \"nodes\": []\n}\n\ne3[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"srask\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The Avestan material is real, but the form and the gloss in the box belong to two different words. \"\n   \"Bartholomae, Altiranisches Wörterbuch col. 1645, has 'j. srask- V. «triefen». Praes. srasca-' — a VERB \"\n   \"'to drip, to trickle down from, to rain in streams' (Vd. 3.29, 6.36, Yt. 5.120, 16.10) — and separately the \"\n   \"noun '*sraska- m. «Träne, Weinen»' (Vd. 7.8, in the phrase ... «Weinen und Stöhnen»), to which he adds \"\n   \"'Zum V. srask-. — np. sirisk «Tropfen, Träne»'. Nourai prints the verb stem srask- but glosses it 'tear drop', \"\n   \"which is the sense of the derived noun sraska-; and it is sraska-, not srask-, that is the etymon of the \"\n   \"Pahlavi and Persian words in the boxes below. The root-to-node arrow is otherwise exactly Pokorny's. \"\n   \"Hence 'plausible': the derivation is right, the citation form is one derivational step off.\"),\n \"derivation_fa\": (\"مادّهٔ اوستایی درست است ولی صورت و معنای جعبه به دو واژهٔ جداگانه تعلق دارد. بارتولمه در ستون \"\n   \"۱۶۴۵ می‌آورد: «j. srask- فعل «چکیدن»، ستاکِ حال srasca-» — فعلی به معنی «چکیدن، فروچکیدن، باران تند باریدن» \"\n   \"(وندیداد ۳٫۲۹ و ۶٫۳۶، یشت ۵٫۱۲۰) — و جداگانه اسمِ «*sraska- m. «اشک، گریه»» (وندیداد ۷٫۸) که ذیل آن نوشته \"\n   \"«از فعل srask-؛ فارسی نو sirisk «قطره، اشک»». نورایی ستاکِ فعلی srask- را نوشته اما معنای اسمِ مشتق sraska- \"\n   \"را به آن داده است؛ و نیایِ صورت‌های پهلوی و فارسیِ زیر همان sraska- است نه srask-. بنابراین اشتقاق درست است \"\n   \"ولی صورتِ ذکرشده یک پله جابه‌جا است: با احتیاط پذیرفتنی است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:1002\", \"status\": \"partial\",\n    \"note\": \"Pokorny p.1002 supports the root → Avestan arrow but distinguishes the two forms: 'Av. srask- (srasca-) ‚triefen …‘, sraska- m. (np. sirisk) ‚Träne, Weinen‘' — the verb means 'to drip', the noun means 'tear'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"cols. 1645–1646 s.v. srask-, *sraska-\", \"stance\": \"partial\",\n    \"note\": \"'• j. srask- V. ‘triefen’. Praes. srasca-, (Kaus.) srascaya- …' and '*sraska- m. ‘Träne, Weinen’ … Zum V. srask-. — np. sirisk ‘Tropfen, Träne’' (BRT.txt lines 27390, 27396). Verb and noun are separate entries.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 705\", \"stance\": \"partial\",\n    \"note\": \"Same distinction: 'Av. srask- (srasca-) „triefen…“, sraska- m. (np. sirisk) „Träne, Weinen“'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"grep 'srask'/'sresk' in CHEUNG.txt\", \"stance\": \"silent\",\n    \"note\": \"Cheung's Etymological Dictionary of the Iranian Verb has no hit for this verb in the local text.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"srešk\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Middle Persian srešk (written <sl(y)šk'>, Psalter <srsk>) 'drop, tear' is the regular continuant \"\n   \"of Old Iranian *sraska- (Av. sraska- 'tear'): the cluster sr- is kept in Middle Persian, and the Old Iranian \"\n   \"-a- of the first syllable is reduced while the suffix vowel is fronted to give -ešk/-išk. MacKenzie, A Concise \"\n   \"Pahlavi Dictionary, s.v.: 'srešk [sl(y)šk | (P srsk), N sirišk] drop, tear'. Nyberg, Manual of Pahlavi II, \"\n   \"reads the same word as srišk: 'srišk [slyškʹ; slškʹ] drop … — Av. (1645) sraska- ‘tear’; MPrth srsk (List 87); \"\n   \"NP sirišk', and quotes the idiom srišk ≈ srišk 'drop after drop' (Kārnāmag 21⁴). The two readings are the \"\n   \"same consonantal skeleton; the chart's srešk is MacKenzie's.\"),\n \"derivation_fa\": (\"فارسیِ میانهٔ srešk (به خط پهلوی ‹sl(y)šk›، در زبور ‹srsk›) «قطره، اشک» دنبالهٔ قاعده‌مندِ \"\n   \"ایرانی باستان *sraska- (اوستایی sraska- «اشک») است: خوشهٔ آغازیِ sr- در فارسی میانه نگه داشته شده و واکهٔ \"\n   \"پسوند به e/i بدل شده است. مکنزی در «فرهنگ کوچک پهلوی» می‌نویسد: «srešk [sl(y)šk | زبور srsk، فارسی نو sirišk] \"\n   \"قطره، اشک». نیبرگ همان واژه را srišk می‌خواند و می‌افزاید «اوستایی (۱۶۴۵) sraska- ‹اشک›؛ پارتیِ مانوی srsk؛ \"\n   \"فارسی نو sirišk» و اصطلاح «srišk pad srišk» یعنی «قطره‌قطره» را از کارنامه نقل می‌کند. هر دو خوانش از یک \"\n   \"اسکلتِ همخوانی‌اند. ادعای نورایی درست است.\"),\n \"sources\": [A_SERESHK],\n \"ref_check\": [\n   {\"ref\": \"BQT:1124\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' ed. Mo'in, the سرشک page (BQT_v2_pages.txt \\\\f-block 587, printed ≈ 1125/1126 by the leaf+540 offset, i.e. within a page or two of Nourai's 1124): Mo'in's footnote 4 reads 'اوستا sraska- … بارتولمه ۱۶۴۵ ، اشتقاق هویشمان ۲۳۷ ، سرشک فارسی شاید از پارتی srsk (قطره) باشد: Henning, A list of Middle Persian… BSOS … در پهلوی (srišk) (قطره) ، نیبرگ ۲۰۹'. The same footnote is reproduced by Dehkhoda (abadis.ir s.v. سرشک, 'حاشیه برهان قاطع چ معین').\"},\n   {\"ref\": \"SNS:183\", \"status\": \"partial\",\n    \"note\": \"Tavoosi's Shayast ne Shayast glossary: the OCR (SNS_pages.txt) is too poor for Persian, but \\\\f-block 183 is exactly the s-r run — grep of that block yields 'srav', 'sravah', 'srab' and ':stadan:' — so the cited page is the right place for srešk; the entry itself could not be read, and no page scan of SNS is available to tools/ref_page.py.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. srešk\", \"stance\": \"supports\",\n    \"note\": \"'srešk [sl(y)šk | (P srsk), N sirišk] drop, tear' (PHD.txt line 568, in the spa–srēd run); the English index has 'tear (n.) ars, srešk' (line 3944).\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (Glossary) s.v. srišk\", \"stance\": \"supports\",\n    \"note\": \"'srišk [slyškʹ; slškʹ] drop 211. 412°, 89²⁰. — Av. (1645) sraska- ‘tear’; MPrth srsk (List 87); NP sirišk' (NYB_vol2_glossary.txt line 3510); also 'srišk ~ srišk drop after drop 21⁴' (line 505).\"},\n   {\"src\": \"BQT\", \"where\": \"Mo'in's footnote to سرشک\", \"stance\": \"supports\", \"note\": \"See ref_check — Mo'in gives Pahlavi srišk with Nyberg 209 as his authority.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"serešk «سرشک»\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"New Persian سرشک serešk / sirišk 'tear, drop (of water)', in the poets from Rudaki and Ferdowsi \"\n   \"on (Dehkhoda quotes Rūdakī 'و اندر نهان سرشک همی باری' and Ferdowsi 'ببارید پیران ز مژگان \"\n   \"سرشک'), continues Middle Persian srešk/srišk with the regular New Persian resolution of the initial cluster \"\n   \"sr- by an anaptyctic vowel (srišk > sirišk, whence the modern pronunciation serešk). Pokorny cites exactly this \"\n   \"word in the root article ('sraska- m. (np. sirisk)'), as do Bartholomae col. 1646 ('np. sirisk ‘Tropfen, Träne’') \"\n   \"and Hübschmann, Persische Studien p.237 ('sirisk ‘Tropfen’ = zd. sraska-'). One nuance Nourai's straight arrow \"\n   \"hides: Mo'in, following Henning's List of Middle Persian Papyri, suggests the Persian word may be a borrowing \"\n   \"from Parthian srsk rather than an inheritance through Middle Persian — 'سرشک فارسی شاید از پارتی «srsk» \"\n   \"(قطره) باشد'. Either way the ultimate source is the same OIr. *sraska-.\"),\n \"derivation_fa\": (\"«سرشک» در فارسی نو به معنی «اشک، قطره» از رودکی و فردوسی به بعد گواه دارد (دهخدا از رودکی \"\n   \"«و اندر نهان سرشک همی باری» و از فردوسی «ببارید پیران ز مژگان سرشک» می‌آورد) و دنبالهٔ فارسیِ میانهٔ srešk/srišk \"\n   \"است؛ خوشهٔ آغازیِ sr- در فارسی نو با واکهٔ میانجی شکسته شده (srišk ← sirišk ← سرشک). پوکورنی در همان مقالهٔ \"\n   \"ریشه «np. sirisk» را آورده، بارتولمه (ستون ۱۶۴۶) «np. sirisk ‹قطره، اشک›» و هوبشمان در «پژوهش‌های فارسی» \"\n   \"ص۲۳۷ «sirisk ‹قطره› = اوستایی sraska-». یک نکتهٔ ظریف که پیکانِ مستقیمِ نورایی می‌پوشاند: معین به پیروی از \"\n   \"هنینگ احتمال می‌دهد «سرشک فارسی شاید از پارتی srsk (قطره) باشد» یعنی وام‌واژه از پارتی باشد نه میراثِ \"\n   \"مستقیمِ فارسی میانه. در هر دو حال خاستگاهِ نهایی همان *sraska- ایرانی باستان است. ادعای نورایی درست است.\"),\n \"sources\": [A_SERESHK],\n \"ref_check\": [\n   {\"ref\": \"POK:1002\", \"status\": \"supports\",\n    \"note\": \"Pokorny p.1002 cites the New Persian word inside the root article: 'sraska- m. (np. sirisk) ‚Träne, Weinen‘' (POK_03.txt line 3327).\"},\n   {\"ref\": \"BQT:1124\", \"status\": \"supports\",\n    \"note\": \"Mo'in's footnote to سرشک in Borhan-e Qate' (BQT_v2_pages.txt \\\\f-block 587) traces سرشک to Av. sraska- via Pahlavi srišk, citing Bartholomae 1645, Hübschmann 237, Nyberg 209 and Henning; Dehkhoda reproduces it verbatim: 'اوستا «سرسکا» (تگرگ). سرشک فارسی شاید از پارتی «سرسک» (قطره) باشد. در پهلوی «سریشک» (قطره). … (حاشیه برهان قاطع چ معین)'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Persische Studien p.237 (and pp. 75, 80 cross-refs)\", \"stance\": \"supports\",\n    \"note\": \"'sirisk ‘Tropfen’, paz. srisk, zd. srasc ‘besprengen’' (HUB.txt line 6073) and 'sirisk ‘Tropfen’ = zd. sraska-' (line 8489) — the page Mo'in cites as 'هویشمان ۲۳۷'.\"},\n   {\"src\": \"BRT\", \"where\": \"col. 1646 s.v. *sraska-\", \"stance\": \"supports\",\n    \"note\": \"'Zum V. srask-. — np. sirisk ‘Tropfen, Träne’' (BRT.txt line 27396).\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, IE-roots dictionary, pdf p.355 s.v. سرشک\", \"stance\": \"supports\",\n    \"note\": \"Entry 'سرشک (به چم اشک چشم ، قطره)' with Avestan and Pahlavi forms (OCR: 'srešk, srišk'), Lithuanian šlakas/šlakėti, and a cross-reference 'برهان قاطع ۱۱۳۴'; note 'چم این واژه در اوستایی: تگرگ' matches Bartholomae's Pahlavi gloss tatark 'Hagel' (ARY_pages.txt, [pdf page 355]).\"},\n   {\"src\": \"HRN\", \"where\": \"grep 'sirisk' in HRN.txt\", \"stance\": \"silent\",\n    \"note\": \"Horn's Grundriss has no numbered article for this word in the searchable text.\"}\n ]\n})\n\ndoc[\"entries\"].append(e3)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-472.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-472.py",
 "description": "Write verification JSON for page 472"
}
```


### [2026-09-14T02:42:25.720Z] TOOL RESULT

```
written
```


## [2026-09-14T02:42:28.094Z] TOOL CALL #75: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-472.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 472",
 "description": "Validate and run verify_check"
}
```


### [2026-09-14T02:42:29.241Z] TOOL RESULT

```
JSON OK
nodes verified: 13/13
node verdicts: {'confirmed': 10, 'plausible': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 3}
ref checks: {'not_checked': 5, 'supports': 9, 'partial': 3}
books consulted: {'supports': 24, 'silent': 6, 'partial': 9} | by book: {'KLN': 5, 'LKT': 4, 'BRT': 4, 'DEV': 3, 'PHN': 2, 'SKT': 2, 'WLD': 2, 'HRN': 2, 'PHD': 2, 'ARY': 2, 'BQT': 2, 'FVQ': 1, 'MON': 1, 'PLA': 1, 'KNT': 1, 'SOD': 1, 'ISS_alt_DKS': 1, 'CHEUNG': 1, 'NYB': 1, 'HUB': 1}
```


## [2026-09-14T02:42:45.410Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-472.json` written; `verify_check.py 472` reports 13/13 nodes, 0 PROBLEM lines.

**Page 472 (book p. 442) — 3 non-redirect entries, 13 nodes**
- Root verdicts: 3 confirmed (Š.r.b, Srěno, Sresk)
- Node verdicts: 10 confirmed, 2 plausible, 1 transcription_suspect
- ref_check: 9 supports, 3 partial, 5 not_checked · consulted: 24 supports, 9 partial, 6 silent

**transcription_suspect**
- Š.r.b #5 [Latin] `siripus` — no such Latin form; Medieval Latin is *sirupus/syrupus/siropus* (Klein p.1450, Lokotsch 1838, Devic). `error_in: "book"` — the printed page really reads "siripus" (image saved to `data/verification/sources/refs/ocr/BOOK/472.png`). The label should also be "Medieval Latin".

**plausible**
- Š.r.b #2 [Persian] — šarāb ← Ar. šarāb is right, but šarbat's Arabic source is شَرْبة *šarba* (nomen unitatis), not šarāb; Mo'in tags it "[ع. شربة]".
- Sresk #1 [Avestan] `srask : tear drop` — srask- is the verb 'to drip' (Bartholomae col. 1645); the noun meaning 'tear' is *sraska-*, which is also the actual etymon of Pahl. srešk / NP سرشک.

**Extraction error the owner must fix**
- `page-472.json`, entry 0, node #5 (Latin): `"parent": 0` is wrong. On the printed page the arrow into the Latin box descends from the Arabic *šarâb* box, i.e. **parent should be 1**. (Verified on the 400 dpi render; Klein's chain Ar. šarāb → ML sirupus agrees.)

**Notes on Nourai's refs:** FVA:208 unverifiable (no digital copy of Nahvi anywhere). KLN:1434, KLN:1450, POK:1002 (×4), HRN:135, BQT:932, SOD:339, BQT:1124 all checked and correct — SOD:339 hits Gharib's entry 8435 exactly ("r'n' rāna <*Av. rāna-, Khot. rāna-, Oss. ron — belt"); BQT:932 carries Mo'in's footnote citing Horn no. 605. SNS:183 marked partial: the OCR is unreadable but leaf 183 is demonstrably the s-r run, and no SNS page scan exists for `ref_page.py`.
