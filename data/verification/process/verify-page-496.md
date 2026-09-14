# Verification process log — verify-page-496


## [2026-09-14T03:08:54.246Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 496 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-496.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-496.json. Write /home/sfmqrb/git/rishe/data/verification/page-496.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 496` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:55.235Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:56.003Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:56.018Z] TOOL RESULT

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


## [2026-09-14T03:08:56.503Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-496.txt"
}
```


### [2026-09-14T03:08:56.523Z] TOOL RESULT

```
1	=== PDF page 496 (book page 466) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Tanŭr, Tannŭr : fire, oven  (refs FVQ:92-94)
4	#1 (parent #0) [Avestan] refs=FVQ:94; BQT:523 | tanŭra : oven
5	  #2 (parent #1) [Pahlavi] refs=FVQ:94 | tanŭr : oven | NOTE: Henning (MPP:88) gives "tnwr" as a Parthian form.
6	    #3 (parent #2) [Persian] refs=BQT:523 | tanŭr «تنور» : oven
7	  #4 (parent #1) [Sogdian] refs=SOD:388 | tn`wr : oven
8	#5 (parent #0) [Hebrew] refs=KLN:121 | tannŭr : oven
9	  #6 (parent #5) [Arabic] refs=TAD:18 | at-tannŭr : the oven used by alchemists
10	    #7 (parent #6) [French] refs=None | 
11	      #8 (parent #7) [English] refs=FSD:178; KLN:121 | athanor : a self feeding furnace
12	#9 (parent #0) [Arabic] refs=FVQ:92 | tannŭr : oven
13	#10 (parent #0) [Akkadian] refs=KLN:121; FVQ:94 | tinnŭra : oven
14	--- entry 1 ---
15	ROOT Tar -> redirect to Ter 3
16	--- entry 2 ---
17	ROOT Targumânu -> redirect to Ragâmu
18	--- entry 3 ---
19	ROOT Ta`rîf -> redirect to A`.r.f
20	--- entry 4 ---
21	ROOT [Greek] Tartaros : hell, a place of punishment  (refs KLN:1574)
22	#1 (parent #0) [Persian] refs=FSF:175 | dord «دُرد» : sediment in casks
23	#2 (parent #0) [Arabic] refs=TAD:27 | durdi : sediment, an acid salt in casks
24	  #3 (parent #2) [Latin] refs=KLN:1574; SKT:543 | tartarum : potassium bitartate, so called due to its burning effect | NOTE: FSD:2468 & SKT:543 derive it from Arabic "durdi: sediment"
25	    #4 (parent #3) [Arabic] refs=TAD:46 | tarteer : tartaric acid
26	      #5 (parent #4) [Persian] refs=MON:2221 | tartîr «طرطیر ، ترتیر» : tartaric acid
27	    #6 (parent #3) [French] refs=AHD:1317; DEV:218 | tartre : tartaric acid
28	      #7 (parent #6) [English] refs=AHD:1317; SKT:543; FSD:2468 | tartar : tartaric acid, a hard deposit on the teeth
29	--- entry 5 ---
30	ROOT Tât -> redirect to Âtos
31	
```


## [2026-09-14T03:08:59.563Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-496.json | head -200",
 "description": "Read source JSON for page 496"
}
```


### [2026-09-14T03:08:59.606Z] TOOL RESULT

```
{
  "pdf_page": 496,
  "book_page": 466,
  "entries": [
    {
      "root": {
        "name": "Tanŭr, Tannŭr",
        "lang": "Indo-European",
        "refs": "FVQ:92-94",
        "gloss": "fire, oven",
        "note": "ARB:84 claims it is an Iranian word. TAD:18 and FSD:178 derive it from root \"N.w.r:light, fire\". FVQ:92 claims it is a word from the pre-Indo-European and pre-Semitic tribes. See FWK for more details."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "FVQ:94; BQT:523",
          "words": [
            {"translit": "tanŭra", "gloss": "oven", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "FVQ:94",
          "words": [
            {"translit": "tanŭr", "gloss": "oven", "script": null}
          ],
          "note": "Henning (MPP:88) gives \"tnwr\" as a Parthian form.",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:523",
          "words": [
            {"translit": "tanŭr", "gloss": "oven", "script": "تنور"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:388",
          "words": [
            {"translit": "tn`wr", "gloss": "oven", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:121",
          "words": [
            {"translit": "tannŭr", "gloss": "oven", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Arabic",
          "refs": "TAD:18",
          "words": [
            {"translit": "at-tannŭr", "gloss": "the oven used by alchemists", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "FSD:178; KLN:121",
          "words": [
            {"translit": "athanor", "gloss": "a self feeding furnace", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Arabic",
          "refs": "FVQ:92",
          "words": [
            {"translit": "tannŭr", "gloss": "oven", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Akkadian",
          "refs": "KLN:121; FVQ:94",
          "words": [
            {"translit": "tinnŭra", "gloss": "oven", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Tar",
        "redirect": "Ter 3"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Targumânu",
        "redirect": "Ragâmu"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ta`rîf",
        "redirect": "A`.r.f"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Tartaros",
        "lang": "Greek",
        "refs": "KLN:1574",
        "gloss": "hell, a place of punishment",
        "note": "KLN indicates it is a word of imitative origin but DEV:218, SHP:351, SKT:543, and FSD:2468 all indicate that the Greek word is taken from the Arab/Persian word \"dord:sediment\""
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "FSF:175",
          "words": [
            {"translit": "dord", "gloss": "sediment in casks", "script": "دُرد"}
          ],
          "note": null,
          "quote": {
            "text": "از این آتشی جنگ بهر منست - همه نوش تو دُرد و زهر منست",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Arabic",
          "refs": "TAD:27",
          "words": [
            {"translit": "durdi", "gloss": "sediment, an acid salt in casks", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Latin",
          "refs": "KLN:1574; SKT:543",
          "words": [
            {"translit": "tartarum", "gloss": "potassium bitartate, so called due to its burning effect", "script": null}
          ],
          "note": "FSD:2468 & SKT:543 derive it from Arabic \"durdi: sediment\"",
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "TAD:46",
          "words": [
            {"translit": "tarteer", "gloss": "tartaric acid", "script": null}
          ],
          "note": null,
          "quote": null
        },
```


## [2026-09-14T03:09:02.772Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['FVQ','BQT','SOD','KLN','TAD','FSD','FSF','SKT','AHD','DEV','MON','POK','WLD','MPP','LKT','AFM','PLA','HRN','HUB','PHD','NYB','BRT','ARY','DOZ','LAM','PHN','AFA','WEB','IEC','SYN','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-14T03:09:03.860Z] TOOL RESULT

```
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://a
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushi
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
MPP {"title": "W. B. Henning, \"A List of Middle-Persian and Parthian Words\", Bulletin of the School of Oriental Studies IX (1937–39), pp. 79–92", "edition_found": "1958", "kind": "archive_djvu", "url": "https://archive.org/details/henning-1958-mitteliranisch", "identifier": "henning-1958-mitteliranisch", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/MPP.txt", "page_offset": "l
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git
LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt", "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verific
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
CHEUNG MISSING
```


## [2026-09-14T03:09:07.915Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-496.json'))\nprint(json.dumps(d['entries'][4]['nodes'][5:],ensure_ascii=False,indent=1))\nprint(json.dumps(d['entries'][5:],ensure_ascii=False,indent=1))\nprint(d.get('meta',''))\n\"; ls data/verification/ | tail -5; sed -n 1,60p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T03:09:09.084Z] TOOL RESULT

```
[
 {
  "id": 6,
  "parent": 3,
  "lang": "French",
  "refs": "AHD:1317; DEV:218",
  "words": [
   {
    "translit": "tartre",
    "gloss": "tartaric acid",
    "script": null
   }
  ],
  "note": null,
  "quote": null
 },
 {
  "id": 7,
  "parent": 6,
  "lang": "English",
  "refs": "AHD:1317; SKT:543; FSD:2468",
  "words": [
   {
    "translit": "tartar",
    "gloss": "tartaric acid, a hard deposit on the teeth",
    "script": null
   }
  ],
  "note": null,
  "quote": null
 }
]
[
 {
  "root": {
   "name": "Tât",
   "redirect": "Âtos"
  },
  "nodes": []
 }
]

page-97.json
page-98.json
page-99.json
process
sources
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
```


## [2026-09-14T03:09:11.861Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,120p /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T03:09:11.939Z] TOOL RESULT

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


## [2026-09-14T03:09:12.200Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 60,140p /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T03:09:12.252Z] TOOL RESULT

```
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
```


## [2026-09-14T03:09:28.421Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FVQ tannur ===\"; grep -n -i -E \"tannur|tannūr|tinūru|tinuru|tanūra\" FVQ_pages.txt | head -40\necho \"=== KLN tannur/athanor ===\"; grep -n -i -E \"athanor|tannur|tinnuru|tinuru\" KLN_1966.txt KLN_1971.txt | head -30\necho \"=== SOD tnwr ===\"; grep -n -i -E \"tn.wr|oven\" SOD_pages.txt | head -30"
}
```


### [2026-09-14T03:09:28.541Z] TOOL RESULT

```
=== FVQ tannur ===
3640:tical writings (PSm, 4473). It also occurs as tinuru in Akkadian, 2
3668:from an older form tannura.
10736:tinuru 94
=== KLN tannur/athanor ===
KLN_1971.txt:21959:to Akkad, tinnuru , ‘oven’. 
KLN_1966.txt:3811:athanor,  n.,  the  self  feeding  furnace  of  the  al¬ chemists.  —  F.,  fr.  Arab,  at-tanniir,  ‘the  oven’, fr.  at-,  assimilated  form  of  al-,  ‘the’,  and  tannfir ‘oven’,  borrowed  fr.  Heb.  tanndr,  which  is  rel. to  Akkad,  tinnuru,  ‘oven’.
=== SOD tnwr ===
3588:CII 1992 Sims-Williams, N. Corpus Inscriptionum                   Vostkovendenija, Moscow, 1980.
31445:     tamfar                                                        furnace, oven
31866:     (/cOthrust, (reinsert                                                 tynfty, VJ la; trans, pret. tnyWr-, C2
32387:      woven                                                         9947 wen-     C                 o^.J' ^j^/V^' <o-*i £j>
32486:                                                                              woven
32501:                                                                             woven
37417:         gold-woven                                                     ugly, hateful, hated
38371:generation      600, 4768, 10274      glowing fire 300                         gold- woven     11575
39018:     of you    6944, 9701, 9738              opposite shore       8125                   oven     9609
39925:                                        woven      9933, 9978, 9981
45560:                              not woven [+1]                     BSTi
```


## [2026-09-14T03:09:30.325Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT tartar ===\"; grep -n -i \"tartar\" SKT.txt | head -20\necho \"=== KLN tartar ===\"; grep -n -i -E \"tartar|durdi\" KLN_1966.txt | head -30\necho \"=== DEV tartre ===\"; grep -n -i -E \"tartre|durdi\" DEV.txt | head -20\necho \"=== AHD tartar ===\"; grep -n -i \"tartar\" AHD_watkins1985.txt | head"
}
```


### [2026-09-14T03:09:30.447Z] TOOL RESULT

```
=== SKT tartar ===
19214:—  Span,  tiritar,  to  shi^Tr,  shake  with Doubtless  from  a  lost  Latin  verb,  all Gk.  rapTtxpil*iV,  to  shake  vrith  cold Tartar  (3).
19215:Tartar  (i),  an  add  sail  in  casfa^  1 cretion  on  the  teeth.  ( F.  —  Low.  L.  -^^ A  term  due  to  the  alchemists ;  called  jn tre,  or  tartre,  in  Chaucer.  —  F.  tartn,  *  ii Cot.;  Low  L.  tartarmm.  —  Arab,  durd, i sediment  tartar  of  wine:  duriiy.  1 Cf.  Arab,  darad,  a  shedding  of  teeth; Devic  connects  with  tartar  on  the  lee
19216:Tartar  (a),  a  native  of  Tartary.  (1 A  per^'trse  spcllmg  of  Tatar,  owins popular  etymology  which  regarded  1 as  let  loose  out  of  Tartaruj  or  bd below).  From  Tdtar,  a  Tatar,  or  ii tant  of  Tatary  (as  it  should  be  spelt).
19217:Tartar  (.0,  TartarD*,  hell  (U  - '  The  gates  of  Tartar ; '  Tw.  Nt  II  *
19218:—  L.  Tartarus.  -  Gk.  Ttiprapoi,  Tai the  infemnJ   regions;    conceived, place  of  extreme  cold ;  cC  Gk- 10  shiver  with  cold.
22841:tacfu,  tail,  tang,  tap,  taper,  tare,  tart, tartar,  tassel,  tattoo,  tear.  teem,  templ^ temporal,  tend,  lender,  tense,  tent,  terrier^ the,  thee,  t/tere  {there),  thole,  thrumg thrush,  tick,  till,  tilt.  tip.  lire,  to-,  toasts  totl^ toll,  tool,  top,  tow,  trace,  trad,  Ira trepan,  trice,  tricJt,  trill,  trinket, trump,  tuck,  tuft,  turtle,  twig.
23695:Fremh  from  I-OW  Latin  from  Arabic'. camlet,  tartar  (1).
=== KLN tartar ===
14501:fecula,  n.,  starch.  —  L.  faecula,  ‘burnt  tartar, salt  of  tartar’,  dimin.  formed  fr  .faex,  gen.  fae- cis,  ‘dregs’.  See  feces.  For  the  ending  see  suff. -ule.
16107:Derivatives:  ghoul-ish,  adj.,  ghoul-ish-ly,  adv. ghurry,  n.,  clepsydra,  clock,  watch,  space  of  time, hour  {India).  —  Hind,  ghari,  fr.  OI.  ghafika, ‘water  jar,  pot’  (serving  as  a  water  clock),  fr. ghafah,  of  s.m.,  which  is  of  uncertain  origin, ghyll,  n.,  a  ravine.  —  AN.  Engl,  dialectal  var. of  gill,  ‘ravine’;  introduced  into  English  by  the English  poet  William  Wordsworth  (1770-1850). giant,  n.  —  ME.  geant,  fr.  OF.  geant  (F.  geant), fr.  earlier  jaiant,  fr.  VL.  *gagantem,  acc.  of *gagas,  assimilated  vr.  L.  gigas,  ‘a  giant’,  fr. Gk.  ytya q,  ‘a  giant’,  fr.  I’tyat;,  'any  of  the  sons of  the  Earth  and  Tartarus’,  which  is  prob.  a pre-Hellenic  word.  Cp.  gigantic.
26088:compounded  of  oStov,  gen.  oSovto;,  ‘tooth’, and  -oeiStj?,  ‘like’,  fr.  s!8o?,  ‘form,  shape’.  See odont-  and  -oid  and  cp.  dentoid. odontolith,  n.,  dental  tartar.  —  Compounded  of odonto-  and  Gk.  Xtffo?,  ‘stone’.  See  -lith. odontology,  n.,  the  study  of  the  teeth  ahd  their diseases.  —  Compounded  of  odonto-  and  Gk. -Xoyia,  fr.  -Xoyo;,  ‘one  who  speaks  (in  a  cer¬ tain  manner;  one  who  deals  (with  a  certain topic)’.  See  -logy.
26155:ogre,  n.,  1)  a  man-eating  giant;  a  hideous  or cruel  man.  —  F.,  first  used  by  Perrault  in  his fairy  stories,  1697;  in  English  it  appears  first (spelled  hogre )  in  a  translation  of  a  French version  of  the  Arabian  Nights;  fr.  Byzantine Ogur,  ‘Hungarian’.  The  sense  development  is due  to  a  confusion  of  the  Hungarians  with  the Huns  and  the  Tartars.  See  Wiener  in  Anglia, XXIII,  107,  and  Meyer-Liibke,  Romanisches etymologisches  Worterbuch,  p.  446,  No.  6048. Cp.  Ugrian.
38134:tanga,  n.,  also  tanka,  name  of  various  coins  in India  and  Turkestan.  —  Hind,  tanga,  lit. ‘weight’,  fr.  OI.  tahkah,  ‘stamped  coin;  a weight’,  which  is  prob.  connected  with  Tartar. tanka,  ‘a  silver  coin’,  ModPers.  tanga.  Arm. t'anka,  ‘a  small  coin’.
38244:Tartar,  n.  and  adj.  —  ML.  Tartarus,  fr.  Pers.  Ta¬ tar,  ult.  fr.  Tata,  name  of  the  Mongols,  who coming  from  the  Gobi  desert  invaded  Russia  in the  9th  cent.  The  first  r  in  Tartar  is  due  to  a  con¬ fusion  w'ith  L.  Tartarus,  ‘hell’ ;  see  Tartarus. tartar,  n.,  1)  potassium  bitartrate,  KHC4H4Os ( chem .);  2)  a  hard  deposit  on  the  teeth.  —  ME. tartre,  tartar,  fr.  OF.  tartre,  fr.  ML.  tartarum , fr.  Gk.  Tdpxapog  (see  Tartarus);  so  called  by Paracelsus  with  regard  to  the  burning  effect  of this  compound.
38245:Derivatives:  tartar-eous,  tartar-ic,  tartar-ish, adjs.,  tartar-ize,  tr.  v.,  tartar-iz-ation,  n.,  tortur¬ ous,  adj.
38246:Tartarean,  adj.,  pertaining  to  Tartarus.  —  Form¬ ed  fr.  Tartarus  with  suff.  -ean.
38247:Tartarus,  n.,  the  abyss  below  Hades;  place  of punishment;  Hades,  netherworld;  hell  (Greek mythol.)  —  L.,  fr.  Gk.  Taprapoc,  prob.  a  word of  imitative  origin,  suggestive  of  something frightful.  Cp.  tartar.
38248:tartlet,  n.,  a  small  tart.  —  Formed  fr.  tart,  n., with  dimin.  suff.  -let.  Cp.  F.  tartelette. tartrate,  n.,  salt  of  tartaric  acid  (chem.)  —  F., formed  with  chem.  suff.  -ate  fr.  tartre,  ‘tartar’.
38249:See  tartar.
38279:Tatar,  n.  —  See  Tartar.
39648:F.)  tortues ,  pi.  of  tortue ,  fr.  earlier  Proven?,  tor- tuga,  fr.  OProven?.  tartuga,  fr.  It.  tartaruga, which  derives  fr.  VL.  tartaruca,  lit.  ‘the  infernal animal’,  fr.  L.  Tartarus',  see  Tartarus.  The Proven?,  form  tortuga  is  due  to  the  influence  of L.  tortus,  ‘twisted’.  Folk  etymology  found  in  the name  of  the  animal  a  reference  to  its  twisted legs.  Cp.  turtle,  ‘tortoise’, tortricid,  adj.,  pertaining  to  the  Tortricidae.  —  See next  word.
=== DEV tartre ===
2201:Tartre.  Esp.  portug.  ital.  tartaro,  lat.  des  alchim.  tar- tarum;  de  l'arabe-persan  i;:»,  (^^;:>  dourd,  dourdi,  sédi- ment, dépôt,  lie  de  l'huile,  lie  du  vin,  tartre.  L'arabe  i>;i> darad  se  dit  aussi  du  tartre  ou  de  la  carie  des  dents; l'adjectif  i);:>^  adrad  s'applique  à  celui  qui  a  les  dents  ca- riées. Le  mot  nous  est  venu  par  les  alchimistes,  ce  qui explique  son  altération.  On  peut  en  voir  de  bien  plus  ex- traordinaires au  mot  Alchimie.  M.  Littré  cite  un  passage du  Glossaire  de  Simon  de  Gènes  où  il  est  dit:  «  Tartar, arabice  tartarum.  ??  jJ^jl»  iarùr,  qui  est  dans  Bocthor,  et ligure  aussi  dans  la  Fahr.  ling.  arah.  manque  dans  Freytag et  lUchardson.  Le  GazopliyL  Ung.  Pers.  écrit  -yy  larllr. jM.  Dozy  n'a  pas  noté  tartaro  dans  son  Glossarrc.
4410:Tarifa,  hisp.  vOy.  Tarif. Tariffa,  ital.  voy.  Tarif. Tap<;)^o5,  voy.  Boutargue. 'ïé.pi-/ov  ^  voy.  Boutargue. TapHoiatov ,  voy.  Carquois. Tarquais,  voy.  Carquois. Tartar,  voy.  Tartre. Tartaro,  hisp.  ital.  voy.  Tarhv. Tartarum,  b.  lat.  voy.  Tartre. Tartre. Tasse.
4690:■^jj  voy.  Tartre.
4767:^^3  voy.  Tartre.
4768:(^>>^i>  voy.  Tartre.
4933:iolb  vo\.  Patard. yÀh  voy.  Altaïr. ^-j-iLb  voy.  Tabaschir. J-^i^  voy.  Timbale. iCa^!^  voy.  JMatelas. ^^.jo  voy.  Tarbouch. i^pjc:  voy.  Estragon. ^^  voy.  Matelas. 'is^jo  voy.  Tare. ^jl^Jui.:^^  voy.  Taraxacuin. i^^j^  voy.  Estragon. i^^j^jo  voy.  Taraxacum. ■pioJû  voy.  Tartre. *UJ:>  voy.  Téréniabin. ^^  voy.  Matraca. JJo  voy.  Tasse. ,c«-ik>  voy.  Talisman, ^  voy.  Talc. \y^  voy.  Tambour. A«i)^  turc ,  voy.  Doliman.
=== AHD tartar ===
```


## [2026-09-14T03:09:46.285Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n 3610,3680p FVQ_pages.txt"
}
```


### [2026-09-14T03:09:46.335Z] TOOL RESULT

```
* i*
voc., explains it " It is said to be Arabic from jj> or ^t and that its
original form was j)j on the measure ^*^, then the ) was given
hamza because of the weight of the damma on it, and then the hamza
**
was suppressed and replaced by another J, so that it became jjZ* ."
This was not looked on with favour by the philologers, however, for
we read in TA, iii, 70, " As for the statements about j^ll* being from
*
jl or j y and that the O is an augment, it is all wrong, and Ibn
4 Usfur pointed this out clearly in his book Al-Mmnatti* as others have
done." This judgment of the philologers is vindicated by the fact
that J^*i is not a genuine Arabic form at all. 3
The Commentators differ among themselves as to the meaning
of the word, some taking it to mean the " surface of the earth ", or
" the highest part of the earth ", or " morning light ", or " oven "
(cf. Tab. on xi, 42). That the word does mean oven is evident from its
use in the old poetry, e.g. Hamasa, 792.
" Is it a loaf which a Nabataean woman bakes in her oven till the
crust rises,"
or a verse in Aghanl, iii, 1G, 1. 7. The Lexicons agree that this is the
original meaning, cf. JawharL sub voc., and LA, v, 162.
Fraenkel, Fremdw, 2G, suggested that the word came into Arabic
1 al-.lawullql is the source of na-Suyuti, Itq, 320 ; Mutaw, 46 : and nl-KhafajT, 52.
2 So al-Laith in LA, v, 163, and see the comment of Abu. Man.su r therein.
3 Roneevalles in Al-Machriq, xv, 049, and see LA, v, 16'i.94: FOREIGN VOCABULARY OF THE QUR^AN
from the Aram. 1 In the O.T. "HHH occurs frequently for furnace or
oven, i.e. the Gk. jcA/jSapo?, and the form in the Aram. Targums is
N*TI3FI, corresponding with the Syr. ]>cu2 of the Peshitta and ecclesias-
tical writings (PSm, 4473). It also occurs as tinuru in Akkadian, 2
a form which Dvorak takes to be a borrowing from the Heb. "11311?
but without much likelihood. 3 Closely connected with this is another
set of words, Aram. KjIDN ; Syr. ]joZl ; Eth. fc#? ; &r. J J>1,
with which group D. H. Miiller would associate the Akk. u-dun-tum.
With it again is to be connected yet another set of words Aram.
N33P ; Syr. ]nL smoke ; Eth. +*} = fopls vapour, and Mand. N3KD
furnace.
As the root *|3fl is not original in any Semitic language, we may
turn to the theory of Perisan origin suggested by the Muslim philologers.
Fraenkel, indeed, though he claims that the Ar. jj is a borrowing
from the Aram., yet thinks that the Aram, word itself is of Iranian
origin. 4 In Avestic we find the word JJ)AJJJ^ tanura (cf. Vendidad,
viii, 254), and in Phlv. it is Jqo meaning baking oven. 5 The word,
however, is no more Iranian than it is Semitic, and as Dvorak and
Hurgronje point out, the Iranian scholars treat it as a loan-word from
Semitic. 6 Now the word occurs also in Armenian, cf. p-nLftp oven,
and p-nLpuiuinLli a bakery, where Hiibschmann takes it as a borrow-
ing from Iranian, 7 and Lagarde as a borrowing from Semitic. 8
The truth would seem to be that it is a word belonging to the
1 The Muhlt, sub voc., says that some authorities considered it as of Hebrew or
Syriac origin, but he does not mention these, and as he explains it as duo to the
combination of ^ and jfc or ^y, one may suspect that ho is merely copying from
the old American translation of Gesenius' Hebrew Lexicon. Guidi, Delia Sede, 597,
noted its foreign origin.
2 Zimmern, Akkad. Fremdw, 32.
3 Zeitschrift fur Keilschriftforschung, i, 119 ff. D. H. Miiller, WZKM, i, 23, is
nearer the mark, however, in suggesting that l^fi is a borrowing from Mesopotamia
from an older form tannura.
4 Fremdw, 26, cf. also Noldeke, Sasaniden, 165.
6 West, Glossary, 121.
6 Dvorak, op. cit. ; Hurgronje, WZKM, i, 73. Cf. Bartholomae, A1W, 638;
Haug, Parsi*, 5 ; Justi, Handbttch der Zend-Sprache, 1864, p. 132 ; Spiegel, ZDMG,
ix, 191.
7 Arm. Gramm t i, 155.
8 Zur Urgeschichte der Armenier, 1854, p. 813, and Armenische Studien, 1877,
No. 863.FOREIGN VOCABULARY OF THE QUR^AN 95
pre-Semitic and pre-Indo-European population of the area which has
been taken over into both groups in its original form and with its original
meaning. 1 If this is so then there is no reason why the Arabs might
not have obtained the word from this primitive source, and not through
```


## [2026-09-14T03:09:49.241Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT tanur ===\"; grep -n -i -E \"tanūra|tanura|tanūr|tanur\" BRT.txt | head -20\necho \"=== PHD tnwr ===\"; grep -n -i -E \"tan(ū|u)r\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -20\necho \"=== HRN/HUB tanur ===\"; grep -n -i -E \"tanūr|tanur|Ofen\" HRN.txt | head -20; grep -n -i -E \"tanūr|tanur\" HUB.txt | head"
}
```


### [2026-09-14T03:09:49.365Z] TOOL RESULT

```
=== BRT tanur ===
11974:iterj»   j.  tanura-'*   n.  'Backofen':   ys  atrym
=== PHD tnwr ===
PHD.txt:4481:tanómandih tanbahr tund tundih tanīhā tandrustīh tandrust tandrust tanīg tanuk tanūr tantūhmag Tür Tiran tórag, Turk -tom
PHD_mackenzie.txt:7214:oven tanur.                               abarzen.
PHD_mackenzie.txt:8226:tanur
=== HRN/HUB tanur ===
2155:201. biriäten 'braten', vergl. bertjeriy btrezen 'Backofen',
4003:Geldner, Studien I, 50, will auch np. cär 'Ofen* von
4732:526. däS 'Ofen*.
```


## [2026-09-14T03:10:04.065Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT context ===\"; sed -n 11965,11985p BRT.txt\necho \"=== MPP tnwr ===\"; grep -n -i -E \"tnwr|tanur|oven\" MPP.txt | head -20\necho \"=== SOD 9609 ===\"; grep -n -E \"9609\" SOD_pages.txt | head -10\necho \"=== SOD tnwr ===\"; grep -n -iE \"tn.wr|tnwr\" SOD.txt SOD_pages.txt | head -20"
}
```


### [2026-09-14T03:10:04.169Z] TOOL RESULT

```
=== BRT context ===
Vgl.  Ai.  /,  wo  tanu.k>t!la.
•  j.  tanu.drug-  Adj.  'des  Leib  mit  der Dr.  verbunden,  der  mit  ihr  eins  geworden ist''>:  vUpe  drvants  'drujS{^V.) yS  adtrits.- ikalsß  (sd.)  V.  76.  18.
Pü. :  (jia)!än  anjar  lan  drui.  —  ')  Das  1.  GUed ist  wohl  als  Lok.  lu  nehmen,  S.  tanu.mi^ra:
•  j.  tanu.parfl^a-  Adj.  'des  Leib  ver- wirkt, dem  Gericht  verfallen  ist'*',  Bezeich- nung für  den,  der  ein  mit  200  upäzana (sd.)"*'  bedrohtes  Vergehen  begangen hat  und  (bis  zu  dessen  -Sühne)  eo  ipso exkommunizirt  ist :  vispe  anasavarw  yö -ä?  (NP-)'>  N.iÖ.-iZ;  —  dahmanqm  .. dafvayasnanqm  .  .  -)ianqm  atanu.p^rf- %anqm  V./ö.öz;  N.j*/;  —  datvayasium va  °^?m  vä  "einen  Ungläubigen  oder einen,  der  im  Kirchenbann  ist"  N.  roj;  — dazvayasnake  vü  '^aAe  v3  N.  11 ;  *P.  10;  — (kat)  nä  daivayamäi  vä  °äai  va  ''aihryäi (sd.)  ^casaite'ü.iy; —  kat  na  *dalvayasnäi vä  '^äi  vä  gSui  dhäitya  (sd.)  ästrydti N.  l8\  —  kat  nä  dafvayasnät  vä  '%äl  (vä) af^rapalSit  {sd.)  pairi  *aiwya»Aat  Ü.lö; —  yi  '^aAe  aparadiamnaAe  (sd.)  aja- yaunia  .  .  ya  Aaca  da!sayasnaeiiyS  .  . N.  54.  a)  bes.  im  Gegensatz  zu  dahma- (sd.):  ciial  al^qm  tipa.mqnay»n  .  ,  cvai dahmartqm  ifea/  °'^anqm  V.  72.  i;  i;  — "^"Jö"'  zaota  daAma  upa.sraotärS  (sd.) yezi  dim  °%9m  *vToarj  .  .  yezi  äat  äim n^il  '%3m  *viaar>  N.J5;  3!)';  —  daAmS zaota  '%a  upajraotärB  yai  dii '•'^H  (AP.)'* va^ia  . .  "der  Z.  ist  Gemeinder,  die  U. sind  im  Bann;  wenn  er  weiss,  dass  sie  im Bann  sind  .  ."  N.  ji?;  3K
*)  Vgl.  lanüm  piryiili,  f>irtlS.laaü;  pfteJani;
ob,Googlc
637
tanumazah-
'tav-
iterj»   j.  tanura-'*   n.  'Backofen':   ys  atrym
'tanu-mazah-  n.  'Grösse  des  Leibes':
V.Ä91.
LW.  aus  dem  s (M.),  np.  I..ir.
iraud-    mit    afa    I   n    und  aoa  I
•to  des  würdig'.    S.  noch  Haug  Zendphil.  34,  J^),  I  ^    o  *
Cdn.  KZ,  ?/.  579,  jo.   516,  sag,  Hbm.  AGr,  /.  "'
318  (vgl.  zu   !/<"--),    Saleuann  MAs.  p.  243-1),
Wbst   SBE,  j/,  62    "(by   a  Tanäpükar   sin)   a
person  becomes  an  outcast  and  woithr  ofdealh".
—  ••)  Nach  Sl.  /.  a  mit  300  StJr.
KompE.  —  'pirAia-  n.  'Verwirkung',  lum  V. ^•OT'.  —  PiLi  lanäpuhrSi,  erl.i  mark  ariän; ».•).  —  ')  Unthem.?  Ebenso  N.  .j*  2.  ^t. Wohl  -la  M  lesen.  —  ')  Hds.  "i.a.  —  S)  Laut- lich (ül)  von  aaäpuArai  beeinflusst.  —  i)  S. nnter  Iraorf.  No.  8.
=== MPP tnwr ===
1534:Nach dem bisher veröffentlichten Material, dessen letztliche Provenienz
=== SOD 9609 ===
31442:                                                              9609 tnNvr B                                «j/0ij
38322:for him     9368                          freeman       424, 2344                  furnace      1824, 9609
39018:     of you    6944, 9701, 9738              opposite shore       8125                   oven     9609
=== SOD tnwr ===
SOD.txt:45457:st.  tnwrt-  «»mwrt- 
SOD.txt:72867:tanur  ©<Av.  tanura\  MP  tnwr 
SOD.txt:73890:tynfty,  VJ  la;  trans,  pret.  tnyWr-,  C2 
SOD_pages.txt:19855:     strong ?, decisive ?, resembling ?,                                st. tnwrt- «»mwrt-
SOD_pages.txt:31443:9597 tmPr C                                          ^.*y          tanur ©<Av. tanura\ MP tnwr
SOD_pages.txt:31866:     (/cOthrust, (reinsert                                                 tynfty, VJ la; trans, pret. tnyWr-, C2
```


## [2026-09-14T03:10:05.710Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 tanur ===\"; grep -n \"تنور\" BQT_v1_pages.txt | head -20\necho \"=== MON tanur ===\"; grep -n \"تنور\" MON_part1.txt MON_part2.txt | head -10\necho \"=== ARY tanur ===\"; grep -n \"تنور\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-14T03:10:05.822Z] TOOL RESULT

```
=== BQT v1 tanur ===
18046:یدو ره بروزن‌تنوره » طعلمیرا گویند
19297:تنوری باش د که در آ نکماج و نان سنکك پزند ۰
19343:عموماً و سوراح تنور:را خصوصاً .
20598:پپن کرده باشند برای نان از تنور جدا کردن -
20602:بربان در تنور آویز ند .
20607:با سیخ کنده ای باشد که بدان بریان در تنور
28008:کون د که درآن خاریو تنور باشد ۳ وخانه‌ای‌را
28782:طبله‌ای که نان در آن گذارند- و تنور نان‌پزی‌را
29950:وطریق سافطان | ات که نان‌تنوری(۱) نیم‌پختهرا
29990:(۱) چش: تنور .
30329:تقو ده بر وزن تنور" بمعنیگل‌بادد
31351:[26۵ برآست که لفت عربی « تنور » ازآرامی بعاربت گرفته شده. در آرامی «تنورا» ودر
=== MON tanur ===
MON_part2.txt:18962:می‌گذارند و سر تنور را می‌بندند تا به 
MON_part2.txt:18963:حرارت و گرمی تنور خشکك شود و این 
MON_part2.txt:18984:تنوره» ند 
MON_part2.txt:18996:به یکك شبانه‌روز می‌گذارند» آنگاه در تنور 
MON_part2.txt:21069:نیز مواد سوخت را در تنور و کوره ریزند. 
MON_part2.txt:25473:تنور ريخته باشد و در میان آتش پخته شده 
MON_part2.txt:25800:دیوار تنور افتاده و در میان آتش بخته شده 
MON_part2.txt:25828:یک شبانروز میگذارند. آنگاه در تنور 
MON_part2.txt:26902:شده باشد. خمیر نانی که در تنور افتاده و در 
MON_part2.txt:33111:کوره‌ها یا ساختن تنور بکار می‌رود؛ گل 
=== ARY tanur ===
1422:۱ چم این واژه در ایرلندی کهن؛ تنور,
```


## [2026-09-14T03:10:17.718Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT page tag near 31351 ===\"; awk 'NR<=31360 && /\\[pdf page/ {l=NR\": \"$0} END{}' BQT_v1_pages.txt; grep -n \"\\[pdf page\" BQT_v1_pages.txt | awk -F: '$1<31360' | tail -3\necho \"--- context ---\"; sed -n 31320,31370p BQT_v1_pages.txt\necho \"=== SOD page tag ===\"; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<31450' | tail -3; sed -n 31430,31450p SOD_pages.txt"
}
```


### [2026-09-14T03:10:18.803Z] TOOL RESULT

```
=== BQT page tag near 31351 ===
--- context ---
تنومند ۴ ۳ بفتح اول ومیم و سکون
(۱) خم۳: با میم بروزن گلوبند .
۱ رکه : تنوزه ۰
انصاف ومالکیت),
-ه (یوند مدید آ ور ند اسماز ضل) .
اقا »از: بن ۳-ی (سبت).
اي ده
نون و دال ابجد (۱) +توانا و تدرست - وبلند
بالا - و عریض 7 وصلحب فوت - و فربه را
ات وشاد وخرم دارند تن را نیز کفته‌اند
که نن پرور باشد .
قنه ۴ « بنتح اول و الی» توت کیب
و جثه را کوند - و ننیده عنکبوت دا نیز
گفته اند 9 - و بعسی قبول و رشا هم هست
چه ننه شدن فبول کردن وراضی شدن باشد.
نا - معروف است که از مفرد بودن
باشد - و بمعنی اجسام نیز آعده است ۷ چه‌نن
بدهنی جیم‌است .
آفی۷ » بر وزن غنی » بمعنی‌جمالی
فئیان» - نتم اول و کر تالی
و تحتانی بالف کشیده و بنون زده » بمعنی
تنیدن* بر وزن رمیدن » معررف
۴ از : تن ۳ اومند (یود
۵ از: تن (تندن)
۷ -بپلوی
٩‏ -ازاوستا -5480 ؛بهلوی
«اسشق ۰۳۹۹ .
قه ازصفحهٌ ۰۲۳
ففه‌اللغه (۳۱۷) آنر! در زمر کلمات مشتراه فارسی و عربی آرد . درزبان | کدی 100111 آعده
(۰ 32 ,۳۲۵۵۵۵ ,۸۲2, 2۸1۳0026۳8) چون رش لغت‌مززبور درهيحجيك اززبانهای سامی
اصالی تیست. ممکن‌است متوجه فرطية لفوبان مسلمان راجم بابرانی بودن اسل لفت‌شد. فرانکل
[26۵ برآست که لفت عربی « تنور » ازآرامی بعاربت گرفته شده. در آرامی «تنورا» ودر
عری «نور» (بتشد ید دوم) فد فرردکل گوید لفت آرامی خورازمنعاً ابراتی‌است. دراوستا کلمةٌ
8 آمده ( رك : وندیداد , 1 ,۲۵4 ) , ودریهلوی صورت 2100 بمعنی احاق طت
(65),)21065311,121 ۷۷ ). با این حال لغتمز بورینظیمی رسد نه‌ابرانی‌باشدونه‌سامی؛ولیابران‌شناسان
آنرااز مأخشسامی دانستهاند. آنجه‌قویب بحتیفت بنظرمیرسد آنت که کلمة مزبور مثعلق است به
مت «ماقبل سامی»و «ماقبل ند وارویابی» مق ناحیه‌ای که بسدها لبرانیان وسامیان جای آنها را
کرقنند واين کلمهرا بپمان‌ممنی اسلی پذپرفتند . «جفری ٩۲‏ -۹0*.ححه اي سس
زوسن خاموش‌بودن - و فریب دادن‌هم
0
تنیده ۴ بر ون دسده ۰ سعتی
خاموش کردیده باشد -و معنی دیگر ممروفشت.
نیز ه - با زای هوزبروزن‌منیژه ؛بمعنی
سر 5
طرف وداعن باشد چنانکه اک رکویند « تنیزء
کوه» مراد ازآن دامن کوه‌باشد .
لنین فك » اشاره بمقد رای وذب
است که محل تقاطم فلك حامل قمی بأشد با
عابل <- و مجره را ثبر کون که کاهکشان
باشد(۱) ؟.
نو » پفتح اول و سکون ثالی » بمعنی
=== SOD page tag ===
     bodily, corporal                                              tan, tan ? ©suff.
     GMS 260, 1103                                                  emphatic particle
                                                                    TSP y2225,
                                                                         ou    9.84
9595 tmcyq C                                    LSJ^r(j^j^
     tamcik (tmcyk)                                           9608 tn>(kh) B                                ? }ytiJ^
                                                                   tanak ? ©Skt. dhatu
     hellish
                                                                   limit ?
         STii 5.39; GMS 1014; Farg. Len. 57.3
                                                                   BSTBL, Dhy. 200n p59; Benv. Notesii 230
9596 tmcyk       S «=> tmcyq
                                                              9609 tnNvr B                                «j/0ij
9597 tmPr C                                          ^.*y          tanur ©<Av. tanura\ MP tnwr
     body ? -^tmb'r, tn^r
     tamfar                                                        furnace, oven
                                                                   SCE 206
     STi 3.4; Sund. AoFi 229 n27
                                                              9610 tnb'r =» tnp>r
9598 tmp'r M, C                                    y
     body                                                     9611 tngy'n M                                  o^rjy
```


## [2026-09-14T03:10:30.291Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT tags ===\"; grep -n \"\\[pdf page\" BQT_v1_pages.txt | awk -F: '$1<31400' | tail -3\necho \"=== SOD tags ===\"; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<31445' | tail -3\necho \"=== KLN page markers near tartar ===\"; grep -n \"\\[pdf page\\|^ *[0-9]\\{3,4\\} *$\" KLN_1966.txt | awk -F: '$1<38250' | tail -4\necho \"=== KLN athanor page ===\"; grep -n \"\\[pdf page\\|^ *[0-9]\\{2,4\\} *$\" KLN_1966.txt | awk -F: '$1<3815' | tail -4"
}
```


### [2026-09-14T03:10:31.528Z] TOOL RESULT

```
=== BQT tags ===
=== SOD tags ===
=== KLN page markers near tartar ===
38025:1566
38061:1568
38062:1569
38180:1572
=== KLN athanor page ===
3689:116
3690:117
3787:120
3788:121
```


## [2026-09-14T03:10:49.292Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls | head -60; echo ---; ls incoming"
}
```


### [2026-09-14T03:10:49.381Z] TOOL RESULT

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


## [2026-09-14T03:10:50.770Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk -F: '$1<38244' <(grep -n \"^ *[0-9]\\{3,4\\} *$\" KLN_1966.txt) | tail -3\necho \"=== FSF dord ===\"; grep -n \"درد\\|دُرد\" FSF_pages.txt | head -20"
}
```


### [2026-09-14T03:10:51.794Z] TOOL RESULT

```
38061:1568
38062:1569
38180:1572
=== FSF dord ===
396:         ‫فرو ريخت آب از دو دیده به درد‪...‬‬    ‫(‪)۲-۲۴-۹۲۵‬‬
584:                               ‫دشم‬            ‫دیگر‪ :‬هلاک و درد و محنت‪ .‬نسخه دیگر‪:‬‬
1040:‫دلی کو نباشد به درد آژده‬                       ‫(‪)۵-۹۵۱۰-۷۹۲۱‬‬
1056:‫دلی پر ز درد و سری پر زگرد‬                     ‫گه خشم و سختی کنید آزمون‬
1228:                ‫همانا دلش دیو بفربفتست‬                      ‫ز بهر نیادل پر از دردکن‬
1534:        ‫کدایه از جهان پس از مرگ آن دنیا‪:‬‬            ‫مین ریت آز درد الوه رین‬
2032:         ‫بپیچ ای دل که ارزانی به دردی‬      ‫نام روز بیست و پنجم از هر ماه‬
2179:‫از درکار نیست‪ :‬بهکار نمی‌خورد‪ .‬به درد‬                                  ‫دو تن را بفرمود زورآزمای‬
2603:‫با داغ و درد‬         ‫ا‬                          ‫روز انجامش یعنی روز پسین؛ روز‬
2692:             ‫بزرگان ایران پر از داغو درد‬                                              ‫اندر آمدن‬
2958:         ‫برادر کزو بودتان دل به درد‬                        ‫نکته دیگر دربار؛ واه نوشه‪:‬‬
3015:‫یعنی دردسر و رنج و زحمتتان نزد شما به‬          ‫برادران رفته آنان را از انديشة جنگ‬
3728:                    ‫بدرد دل و مغزتان از نهیب‬
3821: ‫مجعول آن‪ ,‬مقالة دهخدا را در مقدمة‬                ‫دانایان گفته‌اند هر کهرا دردی باشد بهار‬
3989:                 ‫ادردبرهش‪:‬‬
4263:                                                                      ‫ددرد‬     ‫نیا‬
4338: ‫نباید گرفتن بدان هم شمار‬                         ‫به خنجر جای مهرش را بدرد‬
5301:          ‫به فرجام کار آیدت رنج و درد‬                              ‫رهایینده شدن شست‬
5508: ‫غم و درد فرزند برتر ز چیز‬                    ‫(‪)۱-۲۴۲-۵۷۵۱‬‬
5813:             ‫تو دانسته‌ای درد و تیمار من‬                        ‫زگوینده بپذیر به دين اوی‬
```


## [2026-09-14T03:11:03.890Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN next marker ===\"; grep -n \"^ *[0-9]\\{3,4\\} *$\" KLN_1966.txt | awk -F: '$1>38244 && $1<38400' | head -3\necho \"=== FSD athanor ===\"; grep -n -i \"athanor\" FSD_vol1.txt | head -5\necho \"=== FSD tartar ===\"; grep -n -i \"^tartar\\|tartar, n\\|tartre\" FSD_vol4.txt FSD_vol3.txt | head -10\necho \"=== incoming AHD ===\"; ls incoming/AHD\necho \"=== TAD ===\"; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['TAD'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-14T03:11:05.051Z] TOOL RESULT

```
=== KLN next marker ===
38298:1577
38330:1578
38331:1579
=== FSD athanor ===
27992:ath'e-nor,  1   ath'i-ner;  2   ath'e-nOr,  n.  Same  as  athanor.  fA*f*  nf  **~™«*h  ceh  «<=  t^w.
=== FSD tartar ===
FSD_vol4.txt:1052:sal  abslnthll,  an  Impure  potassium  carbonate obtained  from  the  ashes  of  wormwood  — sal  acetosella, the  acid  oxalate  of  potassium  —   sal  aeratus,  same  as  sao* eratus  —   sal  alembroth,  a   combination  of  mercuric  chlo- rld  and  ammonium  cblorld  salt  of  wlsdomt.— sal amarum,  magnesium  sulfate.  Epsom  salts  sal  cathar- tlcust  —   sal  ammoniac  {Mineral ),  a   white,  vitreous,  solu- ble ammonium  chlorld  (NH«C1),  crystallizing  in  the  Iso- metric system  —   sal  cullnarlus,  table  or  common  salt  — sal  Cyrenalcus,  same  as  sal  ammomac  —   sal  de  duobus, potassium  sulfate  sal  dupllcatust.— sal  dlurctlcus, potassium  acetate  — sal  enlxum,  hydrogen  potassium  sul- fate or  potassium  btsulfate  —   sal  gcramte,  rock  salt  —   sal Jovls,  stannic  chlorld  salt  of  tint,— sal  Martls,  Iron sulfate  copperas  green  vitriol  — sa!  rolcrocosmlcura, aramonlum-^odlutn  phosphate,  used  as  a   flux  In  blowpipe anily  sis  -   sal  rairablle,  sodium  sulfate  Glauber’s  saitt. —   sal  plumbl,  same  as  sugar  of  lead —   sal  prunella, same  as  prunella*  —   sal  SaturnI,  sugar  of  lead  —   sal sedativusy  boric  acid  sal  sedatlvus  Hombergllt.— sal sclgnette,  see  under  Seidlitz  powder  —   sal  soda,  sodium carbonate  washing-soda  —   sal  tartre,  potassium  carbonate, purified  pearlash  salt  of  tartart  —   sal  Tltrloll.  zinc  sul- fate —   sal  TOlatlie,  ammonium  carbonate  volatile  saitt. sal ,   1   sal  or  sel,  2   sal  or  sal  n   (E  Ind  )   A   very  large  tree {Shorea  robusta)  growing  m   India  It  yields  a   dark-brown, cross-grained  heart*wood,  that  Is  hard,  heavy,  strong,  and tough,  and  highly  prized  for  building  purposes  A   palo aromatic  oammar-Ilke  resin,  called  dammar  and  saLdam- xnar.  Is  obtained  from  the  tree,  and  the  Tussar  silkworm feeds  on  its  leaves  sal'*tree"t.
FSD_vol4.txt:30985:tar'tar*,  1   tor'tsr,  2   tar'tar,  n   1,  The  roughly  punfied cnist  of  argol  intermediate  between  crude  argol  and cream  of  tartar  See  cream  op  tartar,  under  cre  vm and  ABGOu  2.  A   yellowish  incrustation  that  forms  on the  teeth,  consisting  chiefly  of  calcium  phosphate  [< F   tartre  <   LI^  tartarun  <   Ar  dwd  dregs  j   —   tartar emetic,  a   white  crystalline  potassium  antlmonlous  tartrate (KSbOC^HiOO,  with  a   sweet  afterward  disagreeable  metal- lic taste  In  medicine,  chiefly  an  emetic  (poisonous  In  large doses)  and  In  calico-printing  and  *dj  elng  as  a   mordant  — ‘tar'tar-lsh,  a   [Rare  I   Same  as  tartarous*.  2 Tar'tar*,  a   &   n   Same  as  Tatar  the  usual  spellmg  in
FSD_vol4.txt:31040:tarttra— zln,  n   An  orangery  ellow  dyestuff  (CnHuNiOioSj  thlghi  a   tasse  [For  tasset  1 N3d  made  by  syntbe^  5   Icldini;  yellow  colors  oa  labrira  Tasm  ,   aibr  Tasmania tar'tra-rlnet  —   tar-trcric,  a   Derived  from  tartaric  Ta^ 'man  ^   tnq'mon  p   tvj'mnn  n   1   Abel  Jansroon add  Compare  TARTRALic-tartreltc  acid,  a   Jellowlsh  a   Dutch^SuSor  dJeover^  Tasmania
FSD_vol4.txt:31042:heattag  tartaric  acid  ^   ^   tartre- tMl  Ic,  peninsula  in  Pembroke  county ,   S   E   Tasmania
FSD_vol4.txt:31043:Same  as  tartrovimc  tartretbyllc  acid,  same  as  TTnc-ma'nl-a  l   tvz-mS'ni-a  2   tSs-mfi'nI-a,  a   An  Island TROVIMC  Amp  -   tar'tro-nate,  n   A   salt  of  tartronic  nf  in  the  S   Padfle
FSD_vol4.txt:47066:tartaric,  derlied  Irom  some  plant  a   term  lormerly  used  In  Vleorous  Ilvcle  nelKe  Tcn'e-tnust
=== incoming AHD ===
=== TAD ===
{
 "title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640",
 "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"
 ],
 "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair. Nourai's exact edition unknown; the Beirut reprint reproduces the 1932 pagination."
}
```


## [2026-09-14T03:11:06.366Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSF نوش تو ===\"; grep -n \"نوش تو\\|زهر منست\\|جنگ بهر منست\" FSF_pages.txt | head\necho \"=== FSF page tags sample ===\"; grep -n \"pdf page\" FSF_pages.txt | head -3\necho \"=== MON tartir ===\"; grep -n \"طرطیر\\|ترتیر\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head"
}
```


### [2026-09-14T03:11:06.500Z] TOOL RESULT

```
=== FSF نوش تو ===
11482:             ‫ازین آشتی جنگ بهر منست‬                             ‫خروشیدن کوس باکرنای‬
11483:‫همه نوش تدورد و زهر منست‬                             ‫همان زنگ زرین و هندی درای‬
=== FSF page tags sample ===
=== MON tartir ===
MON_part1.txt:1149:بی‌کربنات سود و اسید طرطیر کنند و مانند 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:1149:بی‌کربنات سود و اسید طرطیر کنند و مانند
```


## [2026-09-14T03:11:17.053Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSF context ===\"; sed -n 11460,11495p FSF_pages.txt\necho \"=== TAD tanur ===\"; grep -n \"تنور\" TAD_pages.txt | head\necho \"=== TAD durdi ===\"; grep -n \"دردي\\|درديّ\\|طرطير\\|ترتير\" TAD_pages.txt | head"
}
```


### [2026-09-14T03:11:17.160Z] TOOL RESULT

```
=== FSF context ===

                     ‫درج (بروزن برج ‪-‬تازی)‬                    ‫گواه به جای «زهر» در «زهرگونه»‬
‫قوطی‪ ,‬جعبه که در آن پیرایه‌های گرانبها و‬                    ‫زهر گونه‌ای رفت بر خوان سخن‪...‬‬
                 ‫جواهر گذارند‪ .‬پیرایه‌دان‪:‬‬           ‫‏)‪(YAY-AF-F‬‬
            ‫چنان بدکهقیصر بیان چندگاه‬                                                    ‫دراج‬
‫رسولی فرستاد نزدیک شاه‬                                                         ‫نوعی قرقاول‪:‬‬
        ‫ابانامه و مدیه و ببانتار‬                                   ‫لدهمیبلبلازشاخسرو‬
‫یکی درج و قفلی برو استوار‬                            ‫چو دراج زیر گلان با تذرو‬
‫(‪۸‬نوشیروان ‪)۵۵۵۳‬‬                                     ‫(‪)۳-۰۷۱-۱۹۵۲‬‬

                                     ‫درخشش‬                                               ‫درای‬
‫[اسم مصدر از درخشیدن ]‪ :‬درخشندگی‪:.‬‬                                          ‫‪-۱‬پتک آهنگری‪:‬‬

                          ‫تابندگی» فروغ‪:‬‬                       ‫از آنکچارمهنگران پشت پای‬
    ‫میان بزرگان درخشش مراست‬                          ‫بپوشند هنگام زخم درای‬
‫چو بخشایش وداد و بخشش مراست‬                          ‫(‪)۷۲۶۹۲۲‬‬
‫(‪۸‬هرمزد ‪)۶۳‬‬                                                   ‫همان کاوهآن بر سر نیزه کرد‬
                            ‫درد (با پیش اول)‬         ‫گرد‪.‬‬     ‫ارست‬
                                                                 ‫حبازا‬
                                                                     ‫رز‬‫بنگه‬
                                                                          ‫هما‬
          ‫ته‌نشینشراب و سرکهو مانندآن‪:‬‬                                       ‫‪-۲‬زنگ‪ .‬جرس‪:‬‬
             ‫ازین آشتی جنگ بهر منست‬                             ‫خروشیدن کوس باکرنای‬
‫همه نوش تدورد و زهر منست‬                             ‫همان زنگ زرین و هندی درای‬
‫‪۱۷۰۶۸۰6‬‬                                              ‫)‪(1-۷۴1-۸01‬‬
                                     ‫درزمان‬                    ‫ان‬
                                                                ‫ردواز‬
                                                                    ‫کایاآم‬
                                                                         ‫چو بانگ در‬
                    ‫بی‌درنگ» زود فوری‪:‬‬               ‫همی رفت پیش اندرون ساروان‬
‫چو بازور [نام افسونگر] در کوهشد در زمان‬              ‫(‪)۶-۲۹۱-۰۸۴‬‬
‫بسرامد یکی برف و باد دمال‬                                                  ‫(منوجهری» ‪:)۰۶۱‬‬
‫(‪)۴-۷۳۱۰-۹۲۳‬‬                                              ‫شاد باشید کهجشن مهرگان آمد‬
                        ‫(ویس» ‪:)۰۹۱-۳۱‬‬           ‫ای درای کاروان آمد‬  ‫وو‬‫آنگ‬
                                                                         ‫با‬
                                             ‫‪۳۳۰‬‬                                           ‫درست‬
=== TAD tanur ===
749:               ‫من‬    ‫منحوتث‬       ‫وهو‬    ‫المور‪ -‬في العيرانية ‪ 8‬ثور »‪ 6‬في الارامية « تنورا »‬
=== TAD durdi ===
1064:‫وونابى ‪ 8021:81‬وهو الراسب مانلزيت والراسب والسعيظ‬                                       ‫دردي‬
1770:                                                         ‫طرطير ع راجم دردي‬
```


## [2026-09-14T03:11:19.935Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON طرطير ===\"; grep -n \"طرطير\\|ترتير\\|طرطیر\" MON_part1.txt MON_part2.txt | head\necho \"=== ARY درد ===\"; grep -n \"دُرد\\|درد \" incoming/ARY/ARY_pages.txt | head -5\necho \"=== HRN dord ===\"; grep -n -i \"durd\\|dord\" HRN.txt HUB.txt | head -10\necho \"=== PHD durd ===\"; grep -n -iE \"\\bdurd|dwrd\" PHD.txt PHD_mackenzie.txt | head -10"
}
```


### [2026-09-14T03:11:20.068Z] TOOL RESULT

```
=== MON طرطير ===
MON_part1.txt:1149:بی‌کربنات سود و اسید طرطیر کنند و مانند 
=== ARY درد ===
2026:پروسی کهن (۷لفا55نا۲۸ صا0): 4 0110 را درد شا
2197:انگلیسی (۸/0//5ق): 20017 ,18788801 ایرلندی کهن (4لدلع! ضا0): زدرد ی نا
2631:۱ برنانی 078270): نشن درد فرهنگ معین : ۳۶
3238:نورس کهن (۸/08۶8 0ا0): درد ندرا پسگشت‌ها کر
3416:سوئدی (8(۳8015): ند راز ۱ 5 (807883) درد سا
=== HRN dord ===
HUB.txt:599:133. Np. . aurang (so , resp. jetzt durdng gesprochen,
HUB.txt:6094:(oben p. 61); durdy [daroy) Xiige' -= ap. drauga-; xuros
=== PHD durd ===
```


## [2026-09-14T03:11:35.433Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD tags ===\"; grep -n \"page\\|PAGE\\|\\[\" TAD_pages.txt | head -5\necho \"=== TAD ctx 745-755 ===\"; sed -n 740,760p TAD_pages.txt\necho \"=== TAD ctx 1060-1070 ===\"; sed -n 1058,1070p TAD_pages.txt\necho \"=== TAD ctx 1765-1775 ===\"; sed -n 1762,1775p TAD_pages.txt"
}
```


### [2026-09-14T03:11:35.523Z] TOOL RESULT

```
=== TAD tags ===
493:‫رظأقة حاارائية و قات أ ‪.‬وطالة وكتانتة وووقة وأم[ مناه ‪ 121‬اليا‬
2523: ‫بوناني تسطنةمعم‪ -‬أواتك معناه الف غرام وهو بساوي ؟الم‬        ‫كيلوغرام‬    ‫[ْ‬
2552:‫لعن و[لكوت فقالارشية ‪ 2‬لكن ‪ 6‬وف اليونانية ‪ 888101‬وى الارامية‬
2723:  ‫ميناء ‏ فىاثلاينوية [‪8‬مة وفى الارامية «مانا» معناه افللىغتين مرفاًومرسى‬
2879:               ‫عظام المت انما هو تعربب ‪2‬ماع[ء‪ 15:‬اليونانى الذي معناه جثة بأسة‬
=== TAD ctx 745-755 ===

‫ثق عن ( ليد » أي عامومنهالتلنود ‪١‬‏‬
                                 ‫اميف ‪ -‬عبرانيمعناهستعيلموهوممشت‬
                                                                         ‫أي كثاب سن المهود وتعليمهم‬

                                                                ‫‪ 5‬ل الف ‪--‬مترك عاميمعناه كسل ‪.‬ان‬
                                      ‫‪:‬‬      ‫‪0‬‬   ‫‪٠.‬‬            ‫‪4‬‬     ‫‪.‬‬                             ‫‪)2‬‏‬
                                   ‫ترك « تنجره » معناهقلارمنبحاس وغيره‬                        ‫س‬      ‫طنحرة‬
                                                                            ‫‪2‬‬                                  ‫سَّ‬
               ‫من‬    ‫منحوتث‬       ‫وهو‬    ‫المور‪ -‬في العيرانية ‪ 8‬ثور »‪ 6‬في الارامية « تنورا »‬




           ‫(‪ 16‬ذكر الفيروزبادي انها فارسية واهل مصر يتولون بفته' وهى عندهم نسيج‬
         ‫من القطن ابيش والصواب الهْت وهو نسيج رفع من القطن ابيش معرب يافته ‪:‬‬
             ‫بالفارسيه واما ماميه السوريين بالتفته' وهى عندهم نسي من الحرربنفأخوذ‪.‬نميو‪٠‬ال‏له اعل‬
               ‫ارقي‬      ‫ملك‬                ‫ل‬              ‫ع‬        ‫ا‬       ‫جر‬                ‫ل‬


                                                                                 ‫عه‬
=== TAD ctx 1060-1070 ===
‫للذة طعمه و اسمهذه الشجرة فى اللاثينية مهءذهوم ونالولوترصة معناه اللوز‬
                                           ‫‪-‬‬

                                                                   ‫الفارسي‬
                                            ‫الإ‬                                                  ‫آ‬

‫وونابى ‪ 8021:81‬وهو الراسب مانلزيت والراسب والسعيظ‬                                       ‫دردي‬


                                             ‫ل‬                                 ‫‪.‬‬

                                             ‫» معناه خ!‬      ‫ترى « درزي‬             ‫‪-‬‬   ‫درزي‬

=== TAD ctx 1765-1775 ===
           ‫طرخان ‪ --‬فارسي « ترخان‪ 6‬وهو زعم قوم معفى من الضراشب‬
 ‫«لااباءهدهةءل اللاتينى وهو نيات أصله فاىلونانية‬                  ‫يب‬‫عنر‪-‬‬
                                                                       ‫تخو‬
                                                                         ‫طر‬
                                                                             ‫ك‬‫ف‪11‬‬
                                                                                ‫لك ‪5‬‬
                                                                                   ‫لنا‬

                                                         ‫طرطير ع راجم دردي‬

‫طرنا وطامبا ‏ ايطالى ‪:255‬ه‪ 6‬قد بطل استعالها واعتاضوا ممها بلفظة‬
                                                                ‫عريمها مض‬         ‫ممم‬

                                ‫ايه باد وهاه‬                               ‫‪0‬‬
```


## [2026-09-14T03:11:59.326Z] TOOL CALL #23: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T03:11:59.331Z] TOOL RESULT

```


```


## [2026-09-14T03:12:01.902Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA durd ===\"; grep -n -iE \"durd|dord\" incoming/PLA/PLA_pages.txt | head -10\necho \"=== AFA durd/tannur ===\"; grep -n -iE \"durdi|Tannur|tannūr\" AFA.txt | head -10\necho \"=== LKT tartarum/tanur ===\"; grep -n -iE \"tartar|durd|tannur\" LKT.txt | head -10"
}
```


### [2026-09-14T03:12:01.985Z] TOOL RESULT

```
=== PLA durd ===
=== AFA durd/tannur ===
=== LKT tartarum/tanur ===
4204:(c)  Auf  das  ar.  Grundwort  sarki  geht auch  sicherlich  der  aus  byzantinischen Quellen  bekannte  Name  eines  zwischen Ägypten  und  Syrien  zeltenden  Beduinen- stammes lapaKfivoi  zurück;  hieraus  zur Bezeichnung  aller  islamischen  Völker des  Orients  lat.  Saraceni,  Adj.  saracenus 'sarazenisch',  it.  saracino  'Stechpuppe oder  hölzerner  Mann,  nach  dem  die Reiter  mit  der  Lanze  stießen',  saracenüo 'sarazenisch',  saracwiffre 'seil  warz  werden (Weintraube)',  hz.  sarrasin  'Buchweizen' [nach  de  Candolle  im  XV.  Jahrhundert aus  der  Tartarei  und  Rufsland  nach Mittel-  und  Westeuropa  eingeführt:  Poly- gonum  fagopyrum],  sarassine  'Gatter', Sarrazin  im  Argot  der  Pariser  Setzer 'Streikbrecher',  sp.  sarraccino  'Buch- weizen', überall  in  der  Bedeutung  'Sa-
4598:N.  pr.,  Name  einer  grolsen  Verzvveii^ung des  Türkenstammes;  hieraus  u.  a.  dtsch. Taterkorn  'Buchweizen',  Tatarennach- richt 'falsche,  voreilige  Nachricht,  Ente' (so  genannt,  weil  während  des  Krim- krieges ein  tatarischer  iVIeldereiter  vor- zeitig die  Nachricht  vom  Falle  Sewasto- pols nach  Konstantinopel  brachte] ;  cech. kh'üss.  tatarka  'Buchweizen,  Heidekorn'; rum.  tärtäcii^a  'dass.,  Walzenkürbis', tätar  'Tatare,  Tatarenpferd',  tätarcä 'Tatarenstute,  Pelzmantel';  frz.  tartare im  Schneiderargot  von  Paris  'Lehrling, zweiter  Geselle'.  [Roth  ViFr  43/44. MWiD  III.
6699:tartare  2045
7217:tannura  siz.  2019
```


## [2026-09-14T03:12:05.680Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^2019\\.\\|2019\\. \" LKT.txt | head; grep -n \"^2045\\.\\|2045\\. \" LKT.txt | head"
}
```


### [2026-09-14T03:12:05.840Z] TOOL RESULT

```
4545:2019.  Ar.  taunür:
4597:2045.  Tk.  Tatar:
```


## [2026-09-14T03:12:06.818Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tartar",
 "prompt": "Give the full etymology entries for \"tartar\" (the chemical/dental deposit), \"Tartarus\", and any mention of Arabic durd / Greek tartaron."
}
```


### [2026-09-14T03:12:12.547Z] TOOL RESULT

```
# Etymology of "Tartar" (Chemical/Dental Deposit)

**Tartar (noun)** — Late 14c. origin describing "bitartrate of potash, sediment of potassium tartarate" from wine fermentation. The term derives from Old French *tartre* and Medieval Latin *tartarum*, ultimately tracing to late Greek *tartaron*, meaning "tartar encrusting the sides of wine casks." The Greek word's exact origins remain uncertain, though a Semitic source has been proposed without definitive identification. The purified form became known as cream of tartar. By 1806, the term specifically referred to dental encrustation (calcium phosphate).

---

# Related Entry: "Tartarus"

The web content references Latin *Tartarus* meaning "hell," which influenced how Western European languages shaped the spelling of "Tartar" (the ethnic group). A 1270 letter from St. Louis illustrates this association: pushing adversaries "back into the Tartarus whence they are come."

---

# Regarding Arabic/Greek Terms

The content does not mention "Arabic durd" specifically. It only notes that while a Semitic origin for *tartaron* seems possible, the exact source remains unidentified and "Arabic is unlikely because of the early date of the word in Latin."
```


## [2026-09-14T03:12:19.950Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n 4545,4560p LKT.txt"
}
```


### [2026-09-14T03:12:19.994Z] TOOL RESULT

```
2019.  Ar.  taunür:
'Ofen,  und  zwar  beweglicher  Ofen'  [vgl. Assyr.  iitiüru,  Del  HWB  711b;  zur  Ent- stehung und  Geschichte  des  Wortes  vgl. Rudolf  Dvorak,  Ein  Beitrag  zur  Frage über  die  Fremdwörter  im  Koran.  Leip- ziger Diss.  München  1884];  hieraus  mit ar.  Art.  sp.  atanor  im  MA  'Ofen  der Alchemisten',  'Brunnenröhre',  frz.  atha- nor  'Alchemistenofen'.  Über  tk.  tandyr wurde  rum.  tandur  'Fußwärmer',  d.  h. ein  Tischchen,  unter  dem  ein  Gefäß  mit glühenden  Kohlen  aufgestellt  ist  [s.  man- gal  hier  Nr.  1392],  frz.  tandour  'dass.'. Unmittelbar  aus  dem  Ar.  wurde  siz. tanniira  'kleiner  Ofen,  Kohlenbecken'. Aus  dem  gleichlautenden  hehr.  Worte wurde  gaunerdtsch.  Tanner  'Ofen'.  [DE SlOy-il-ä.  Devic  DEt  216.  Lammens  Rem 5234.    Lammens  Fartik  917.
2020.  Ar.  tautana:
'Metallischer  Klang,  Gepränge',  ebenso tk.  tantana  'Pomp,  Parade';  hieraus rum.  dandana  'Gepolter,  Lärm,  schlechte Angelegenheit'.
2021.  Tk.  tapkur:
'Kleines  Lederkoppel,  das  die  Schabracke des  Pferdes  festhält'  [Kelekian  Kämüs 787  b:  iäiÄ;är];  hieraus  rum.  <«/'<wr 'dass.'.
2022.  Pers.  tär:
'Faden,  Gewebe'  [Horn  NpEt  S.  82, Nr.  369],  ebenso  tk.;  hieraus  rum.  tearä 'Zetteln'  (Weberausdruck).
2023.  Ar.  taraf:
'Seite,  Gegend',  ebenso  tk.;  hieraus  rum. taraf a  'Schar,  Bande'.
2024.  Ar.  taraha:
'Entfernen,  beseitigen',  dazu  subst.  Intin. tarh  'Abzug';  hieraus  it.  prov.  tara, frz.  tare,  sp.  pg.  <a>-a,  rum.  dar«;  dtsch. Tara,  engl,  tare;  russ.  tara  'Abzug  vom Bruttogewicht',  also  'Verpackungsge- wicht'. [Zur  Lautgestaltung  beachte man,  daß  das  ar.  tarh  fast  wie  farak gesprochen  wird;  Ableitung  von  fürah scheint  daher  zweifelhaft,  vgl.  RUSKÄ in  Isl  XII,  234-/235.]  Hierhin  gehört auch  it.  tarocco,  dtsch.  Tarock  'ein  Kar- tenspiel'. [DE  313.  Eguilaz  304.  ML 8568.    GrSVociSic  247.
2025.  Ar.  turahsakun:
'Wilde  Zichorie';  hieraus  la*.  taraxacum 'Löwenzahn,  Leontodon  laraxacum',  frz. taraxacon;  eng),  taraxacum.  [Devic  DEt 216/il7.    Lammens  Rem  235.
2Ui6.  Tk.  tarak: 'Kamm'  [vom  Stamme  tal,  tar  'groß, geräumig  >  erweitern,  ausstreuen',  c'ag. tarak  'Kamm',  eigentlich  'Zerstreuer', Vämbery  TktEtWb  S.  162,  Nr.  176  II]; hieraus  rum.  tarac,  arac  'Reben-  und Weinpfahr,  därac  'Wollkratze,  Krempel'.
2027.  Kas.-tat.  tarakau: 'Schabe';   hieraus  russ.  tarukan,  cech. tarakan  'dass.',    vielleicht  auch  poln. karuczan.     [Gorjajew  360.     Mikl  SiEt Wl)  347  a.
```


## [2026-09-14T03:12:22.196Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D9%86%D9%88%D8%B1",
 "prompt": "Give the etymology sections for the Persian and Arabic entries of تنور (tanur/tannūr): what origin is given (Akkadian, Aramaic, Semitic, Iranian?), and any mention of Middle Persian, Avestan tanūra, Sogdian."
}
```


### [2026-09-14T03:12:28.846Z] TOOL RESULT

```
# Etymology of تنور (tanur/tannūr)

## Arabic Entry

The Arabic noun تَنُّور (tannūr) is borrowed from Aramaic تַנּוּרַא (tannūrā), which derives from Middle Persian tanūr meaning "oven." The ultimate origin is traced to **Akkadian 𒋾𒂟 (tinūru)**.

## Persian Entry

The Persian تنور (tanūr, tannūr) comes directly from **Middle Persian** (tnwr /tanūr/, "oven"). The entry notes comparison with Sogdian (tnʾwr /tanūr/, "furnace, oven") and ultimately traces back to **Akkadian 𒋾𒂟 (tinūru)**.

## Key Differences

- **Arabic**: Shows the borrowing path through Aramaic as intermediary
- **Persian**: Presents direct inheritance from Middle Persian

Both entries converge on **Akkadian as the ancient source language**. Neither mentions Avestan tanūra.
```


## [2026-09-14T03:13:18.215Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MPP head ===\"; head -20 MPP.txt; wc -l MPP.txt\necho \"=== MPP tnwr search ===\"; grep -n -iE \"tnwr|tanur|Backofen\" MPP.txt | head\necho \"=== HENNING tnwr ===\"; grep -n -iE \"tnwr\" HENNING_selected_papers.txt | head"
}
```


### [2026-09-14T03:13:18.286Z] TOOL RESULT

```
=== MPP head ===
HANDBUCH DER ORIENTALISTIK
Herausgegeben von B. Spuler unter Mitarbeid von H. Franke, J. Gonda
H. Hammitzsch, H Kees und J. E. van Lohuizen-de Lee uw
ERSTE ABTEILUNG
DER NAHE UND DER MITTLERE OSTEN
HERAUSGEGEBEN VON B. SPULER UND H. KEES
VIERTER BAND
c
IRANISTIK
ERSTER ABSCHNITT
LINGUISTIK
MIT BEITRÄGEN VON
KARL HOFFMANN . W. B. HENNING
H. W. BAILEY • G. MORGENSTIERNE • W. LENTZ
E. J. BRILL
LEIDEN — KÖLN
1958HANDBUCH DER ORIENTALISTIK
HERAUSGEGEBEN VON BERTOLD SPULER
unter Mitarbeit von: H. Franke, J. Gonda,
H. Hammitzsch, H. Kees und E. J. van Lohuizen-de Leeuw
7737 MPP.txt
=== MPP tnwr search ===
=== HENNING tnwr ===
```


## [2026-09-14T03:13:20.629Z] TOOL CALL #30: Bash

```json
{
 "command": "pdftoppm -f 496 -l 496 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg496 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg496.png"
}
```


### [2026-09-14T03:13:22.331Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 78601 Sep 13 23:13 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg496.png
```


## [2026-09-14T03:13:25.592Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg496.png"
}
```


### [2026-09-14T03:13:26.107Z] TOOL RESULT

```

```


## [2026-09-14T03:13:26.104Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T03:13:42.580Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 496 -l 496 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg496hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg496hi.png'); print(im.size)\n# crop region of entry4 left spine: original 1700x2200 at 200dpi -> at 400dpi double\nim.crop((600,2400,1600,2900)).save('crop496-a.png')\n\""
}
```


### [2026-09-14T03:13:45.745Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-14T03:13:47.744Z] TOOL CALL #33: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop496-a.png"
}
```


### [2026-09-14T03:13:47.766Z] TOOL RESULT

```

```


## [2026-09-14T03:14:00.703Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN Hefe/Bodensatz ===\"; grep -n -iE \"Hefe|Bodensatz\" HRN.txt HUB.txt | head -10\necho \"=== CHEUNG drd ===\"; grep -n -iE \"\\*dard|durd\" CHEUNG.txt | head -5\necho \"=== PHD durdag ===\"; grep -n -E \"durd|dwlt|dregs|lees\" PHD_mackenzie.txt | head -10\necho \"=== MON درد entry ===\"; grep -n \"دُرد\\b\\|دردی (\" MON_part1.txt | head -5"
}
```


### [2026-09-14T03:14:00.812Z] TOOL RESULT

```
=== HRN Hefe/Bodensatz ===
HUB.txt:2300:aspres (Schefer, Chrest. pers., vgl. ZDMG. 44, 532),
HUB.txt:8812:'Hefenballen', zd. gunda-; gos 'Ohr ^= ap. gausa-; gun
HUB.txt:8894:*) Vgl. auoh maryas^ Schefer, Chrestom. II, 154, 15, 18; 159,
HRN.txt:952:Seljuqname, bei Sohefer 76, 7. (Ich verdanke dieses Citat Prof.
HRN.txt:6271:716. setei*veH, suturven^ esterven 'unfruchtbar' (Schefer,
HRN.txt:8129:936. gunde *Hefenballen (für ein BrotV.
HRN.txt:8330:'anno 1660) dagegen destemol (Schefer, S. 109).
HRN.txt:8915:1027. nirx, nerx "Preis, Wert' (z. B. Schefer, Chresto-
=== CHEUNG drd ===
24823:wdyr'nd; Partic.: pres. caus. MMP wyd’r’g, perf. pass. MMP *wdrd, BMP wtwit / widurd/, etc. 
=== PHD durdag ===
=== MON درد entry ===
```


## [2026-09-14T03:14:02.627Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%AF",
 "prompt": "Is there a Persian entry for درد read as \"dord\" meaning dregs/lees/sediment? Give its etymology (Middle Persian, Proto-Iranian forms). Also any Arabic entry درد / دردي \"dregs\" and its etymology."
}
```


### [2026-09-14T03:14:09.241Z] TOOL RESULT

```
# Persian "Dord" and Arabic Cognates

## Persian Entry for درد (dord)

Yes, the page documents a second Persian etymology for **درد** pronounced "dord," meaning **"dregs"** (sediment/lees).

**Etymology:** According to the article, it derives from "Proto-Iranian *dr̥ti-* ('manure, feces'), from Proto-Indo-European *dʰṛ-to-*, from Proto-Indo-European *dʰreyd-* ('to have diarrhea')."

## Arabic Cognate

The entry identifies an Arabic cognate: **دردي** (durdiyy), glossed as **"liquid sediment, lees, amurca"** (a byproduct of olive oil production). The text notes this as an "Iranian borrowing" into Aramaic and Arabic, suggesting the Arabic term derives from the same Proto-Iranian roots as the Persian word.

The page presents these as related through ancient borrowing patterns rather than independent developments, linking them to a shared Indo-European etymological foundation concerned with separation and refuse matter.
```


## [2026-09-14T03:14:19.205Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && curl -s \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%AF?action=raw\" -o drd496.wiki && python3 - <<'EOF'\nt=open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/drd496.wiki').read()\ni=t.find('==Persian==')\nprint(t[i:i+2500])\nEOF"
}
```


### [2026-09-14T03:14:20.412Z] TOOL RESULT

```
==Persian==

===Etymology 1===
From {{inh|fa|pal|dlt'|tr=dard|t=pain}}, from {{inh|fa|ira-pro|*dar-ta-|t=torn, burning, pain}},<ref>{{R:ira:ESIJa|vol=2|page=342}}</ref> from {{der|fa|ira-pro|*darH-|t=to have pain}}, from either {{der|fa|ine-pro|*der-|t=to tear, split}} or {{der|fa|ine-pro|*delh₁-|t=to split, suffer, be in pain}}, the latter which Cheung considers to be related to the former.<ref>{{R:ira:Cheung|page=61}}</ref><ref>{{R:fa:Nourai|page=89}}</ref> See also {{m|fa|دریدن|tr=daridan|t=to ravage, attack}}.

====Pronunciation====
{{fa-IPA|dard}}
<!-- {{audio|Fa-درد.ogg|Audio|lang=fa}} broken -->

====Noun====
{{fa-regional|درد|درد|дард}}
{{fa-noun|tr=dard}}

# [[pain]]
# [[ache]]
# [[affliction]]
# [[disease]]
# [[illness]]
# [[complaint]]

=====Derived terms=====
{{q|verbs}}
{{col2|fa
|درد کردن<tr:dard kardan>
|درد گرفتن<tr:dard gereftan>
}}
{{q|others}}
{{col2|fa
|اهل درد<tr:ahl-e dard>
|سردرد<tr:sar-dard>
|دردی<tr:dardi>
|دردناک<tr:dardnâk>
}}

=====Descendants=====
{{col-top|2|desc}}
* {{desc|jdt|dərd}}
* {{desc|az|dərd|bor=1}}
* {{desc|bn|দরদ|bor=1}}
* {{desc|gu|દર્દ|bor=1}}
* {{desc|inc-hnd|-|bor=1}}
*: {{desc|ur|درد|tr=dard}}
*: {{desc|hi|दर्द}}
* {{desc|kk|дерт|bor=on}}
* {{desc|kmr|derd|bor=on}}
* {{desc|bor=on|axm|դարդ|տարտ|դերդ|տէրտ}}
** {{desc|hy|դարդ|bor=1}}
* {{desctree|ota|درد|tr=dert|bor=on}}
** {{desc|sq|dert}}
** {{desc|el|ντέρτι}}
* {{desc|pa|-|bor=1}}
*: {{desc|pa|ਦਰਦ|sclang=1}}
*: {{desc|pa|دَرَد|sclang=1}}
* {{desc|zza|derd|bor=on}}
* {{desc|ug|دەرد|bor=1}}
* {{desc|uz|dard|bor=1}}
{{col-bottom}}

====References====
{{reflist}}

===Etymology 2===
From {{inh|fa|ira-pro|*dr̥ti-|t=manure, feces}}, from {{inh|fa|ine-pro||*dʰṛ-to-}}, from {{der|fa|ine-pro|*dʰreyd-|t=to have diarrhea}}, whence also {{cog|en|dirt}}, {{cog|non|dríta|t=to defecate}}, and {{cog|ru|дриста́ть|t=to shart}}. Possibly related to {{cog|ine-pro|*dʰerh₃-|t=to spring, leap}} (whence perhaps {{cog|sa|धारा|t=current, torrent}}).<ref>{{R:ira:ESIJa|vol=2|page=356}}</ref>

Compare the Iranian borrowings: {{cog|arc|[[דּוּרְדָּא]] / [[דֻּרְדָּא]]|tr=durdā|t=sediment; lees}}, in plural {{m|arc|[[דּוּרְדֵּי]] / [[דֻּרְדֵּי]]|tr=durdī}}; {{cog|ar|دُرْدِيّ|t=liquid sediment, lees, amurca}}.

====Alternative forms====
* {{alt|fa|دردی|tr=dordi}}

====Pronunciation====
{{fa-IPA|durd}}

====Noun====
{{fa-noun|tr=dord}}

# [[dregs]]

=====Descendants=====
* {{desc|axm|դիրտ|bor=1|alts=1}} {{see desc}}<ref>{{R:xcl:HAB|դիրտ|vol=I|page=670b}}</ref>
* {{desc|hy|դըռդի|bor=1}}
* {{desc
```


## [2026-09-14T03:14:21.560Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%A4%CE%AC%CF%81%CF%84%CE%B1%CF%81%CE%BF%CF%82",
 "prompt": "What etymology does Wiktionary give for Ancient Greek Τάρταρος (Tartaros)? Any mention of Pre-Greek, Beekes, reduplication, or Semitic?"
}
```


### [2026-09-14T03:14:27.016Z] TOOL RESULT

```
# Etymology of Τάρταρος According to Wiktionary

Based on the Wiktionary article, there is **no mention of Pre-Greek, Beekes, reduplication, or Semitic origins**.

The article presents two main etymological theories:

1. **Strabo's account**: According to the historical source, the word was believed to derive from the city of Ταρτησσός (Tartēssós), "with a slight change of letters," referencing a western location beyond the Pillars of Heracles.

2. **Klein's theory**: This scholar suggests the word is "prob[ably] word of imitative origin, suggestive of something frightful."

The etymology section contains no discussion of Indo-European sound patterns, Proto-Indo-European reconstruction, or any linguistic analysis beyond these two traditional explanations.
```


## [2026-09-14T03:15:00.745Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK tanur/Ofen ===\"; grep -n -icE \"tannur|tanur\" POK_full.txt | head -3\necho \"=== AHD watkins ===\"; grep -n -i \"oven\" AHD_watkins1985.txt | head -3\necho \"=== NYB tanur ===\"; grep -n -iE \"tanur|tnwl|tnwr\" NYB_vol2_glossary.txt | head -5\necho \"=== AFA 26 Ofen ===\"; grep -n -iE \"tannûr|Tannur|tannür|Backofen\" AFA.txt | head -5\necho \"=== AFM tanur ===\"; grep -n \"تنور\" AFM_pages.txt | head -5\necho \"=== DEV athanor ===\"; grep -n -i \"athanor\\|atanor\" DEV.txt PHN.txt LAM.txt | head -8\necho \"=== WEB athanor ===\"; grep -n -i \"athanor\" WEB.txt 2>/dev/null | head -3; ls | grep -i web"
}
```


### [2026-09-14T03:15:00.924Z] TOOL RESULT

```
=== POK tanur/Ofen ===
0
=== AHD watkins ===
310:aukv-, Cooking pot. 1. Germanic suffixed form *uhw-na- in *ufna- in Old English ofen, furnace, oven: OVEN. 2. Suffixed form *auk-sld- in Latin aulla, aula, olla, pot,
325:English bere, bere, berlic, barley: BARLEY; BARN. 2. Latin far (stem farr-), spelt, grain: FARINA, (FARINA- CEOUS), FARRAGINOUS, FARRAGO. [Pok. bhares- 111.] bhasko-. Band, bundle. 1. Latin fascis, bundle (as of rods, twigs, or straw), also crowd of people: FASCES, FASCICLE, FASCINE, FASCISM. 2. Latin fascia, band, fillet, bandage: FASCIA, FESS. 3. Probably Latin fascinum, fascinus, an amulet in the shape of a phallus, hence a bewitching: FASCINATE. [Pok. bhasko- 111.] bhau-. To strike. 1. Germanic *bautan in: a. Old English béatan, to beat: BEAT; b. German bosseln, to do odd jobs: BUSHEL?. 2. Germanic *bautilaz, hammer, in Old English bietel, hammer, mallet: BEETLE’. 3. Germanic “bitaz in Old English diminutive buttuc, end, strip of land: BUTTOCK. 4. Germanic *butt-, name for a flatfish, in Middle Dutch butte, flatfish: HALIBUT. 5. Germanic *buttan in Old French bo(u)ter, to strike, push (> French bouton, button): BOUTON, BUTT!, BUTTON, BUTTRESS; ABUT, REBUT, SACKBUT. 6. Variant form *bhit- in: a. Latin confiitdre, to check, suppress, restrain (com-, intensive prefix; see kom): CONFUTE; b. Latin refiitdre, to drive back, rebut (re-, back; see re-): REFUTE. [Pok. 1. bhau- 112.] bhé-. To warm. Contracted from *bheo. 1. Suffixed zero-grade form *bha-to- in Germanic *batham in Old English beth, a bath, and its denominative bathian, to bathe: BATH!, BATHE. 2. Suffixed zero-grade form *bha-g- in: a. Germanic *bakan in Old English bacan, to bake: BAKE; b. Germanic *bakkan in German backen, to bake: ZWIEBACK. [Pok. bhé- 113.] bhedh-. To dig. 1. Germanic *badjam, garden plot, also sleeping place, in Old English bed(d), bed: BED. 2. O-grade form *bhodh- in: a. Latin fodere, to dig: FOSSA, (FOSSE), FOSSIL, FOSSORIAL; b. perhaps Greek bothros, pit: BOTHRIUM. [Pok. 1. bhedh- 113.] bheg-. To break. Akin to bhreg-. Possibly in various Germanic forms. 1. Germanic nasalized form *bang- in: a. Old Norse banga, a hammering, akin to the probable Scandinavian source of English BANG!; b. Swedish dia- lectal bangla, to work inefficiently, akin to the possible Scandinavian source of English BUNGLE. 2. Possibly Germanic nasalized forms *bankiz and *bank6én-, bank of earth (possibly < “feature where the contour of the ground is broken,” escarpment, riverbank, possibly also associated with “manmade earthwork’’), later also bench, table, in: a. Old English benc, bench: BENCH; b. Old Danish banke, sandbank, akin to the Scandinavian source of BANK}; c. Old High German banc, bank, bench, moneychanger’s table (> Italian banca): BANK?, BANT- LING, BUNCO; BANKRUPT; d. Old French banc, bench: BANK, BANQUET; @. Provencal banca, bench: BAN- QUETTE. [Pok. bheg- 115.] bhegr-. To run away. 1. Germanic *bakjaz, a stream, in Old Norse bekkr, a stream: BECK?. 2. Greek phebesthai, to flee in terror, forming phobos, panic, flight, fear: -PHOBE, -PHOBIA. [Pok. bhegy- 116.] bhei-'. A bee. Germanic suffixed form *bidn- in Old English 6é0, a bee: BEE}. [Pok. bhei- 116.] bhei-2. To strike. 1. Germanic suffixed form *bili- in Old English bile, bird’s beak: BILL?. 2. Germanic suffixed form *bilja- in Old English bil), sharp weapon: BILL’. [Pok. bhei(a)- 117.] bheid-. To split; with Germanic derivatives referring to biting (hence also to eating and to hunting) and wood- working. 1. Germanic *bitan in Old English *bitan, to bite: BEETLE!, BITE. 2. Zero-grade form *bhid- in: a. Ger- manic *bitiz in Old English bite, a bite, sting: B1T?; b. Germanic *bitén- in Old English bita, a piece bitten off, morsel: BIT!; c. Suffixed form *bhid-ro- in Old English bit(tjer, ‘‘biting,’’ sharp, bitter: BITTER. 3. O-grade form *bhoid- in Germanic *baitjan in: a. Old Norse beita (verb), to hunt with dogs, and beita (noun), pasture, food: BAIT!; b. Old French beter, to harass with dogs: ABET. 4. Germanic *bait-, a boat (< “dugout
415:in: a. Old English twd, two (nominative feminine and neuter): Two; b. Old English fwégen, two (nominative and accusative masculine): TWAIN. 2. Germanic com- pound *twa-lif-, “two left (over from ten),” twelve (*-if-, left; see leik-), in Old English twelf, twelve, and twelfta, twelfth: TWELFTH, TWELVE. II. Adverbial form *dwis and combining form *dwi-. 1. Germanic *twi- in: a. Old English twi- (> Middle English twi-), two: TWIBIL, TWILIGHT; b. Old High German zwi- (> German zwie-), twice: ZWIEBACK, ZWITTERION. 2. Latin bis (combining form bi-), twice: BI-, BIS; BAROUCHE, BISCUIT. 3. Greek dis (combining form di-), twice: DI-!. 4. Germanic *twis in Middle English twisten, to twist: Twist. 5. Germanic *twiyes in Old English twige, twiga, twice: TWICE. 6. Ger- manic compound *twégentig, “twice ten” (*-tig, ten; see dekm), in Old English twéntig, twenty: TWENTY. 7. Ger- manic *twihna, double thread, twisted thread, in Old English twin, double thread: TWINE. 8. Germanic com- pounds “bi-twihna and *bi-twisk, “at the middle point of two” (*bi, at, by; see ambhi), in Old English betwéonum and betweohs, betwix, between: BETWEEN, BETWIXT, (TWIxT). 9. Germanic compound “twilic-, “two-threaded fabric” in Old English twilic, woven of double thread: TWILL. 10. Suffixed form *dwis-no- in: a. Germanic *twisnaz, double, in Old English twinn, getwinn, two by two, twin: TWIN; b. Latin bini, two by two, two each: BINAL, BINARY; COMBINE. 11. Suffixed form *dwi-ko- in Germanic *twig(g)a, a fork, in Old English twigge, a branch: Twic!. 12. Compound *dwi-plo-, twofold (*-plo-, -fold; see pel-3), in Greek diploos, diplous, twofold: DIPLO-, DIPLOE, DIPLOMA; ANADIPLOSIS. 13. Suffixed reduplicated form *dwi-du-mo- in Greek didumos, dou- ble, the testicles: (DIDYMIUM), DIDYMOUS; EPIDIDYMIS, TETRADYMITE. 14. Suffixed form *dwi-kha in Greek dikha, in two: DICHASIUM, DICHO-. III. Inflected form *duwo. 1. Latin duo, two: DEUCE}, DOZEN, DUAL, DUET, DUO-; DUODECIMAL, 2. Greek duo, dud, two: DUAD, DYAD; DODECAGON, HENDIADYS. IV. Variant form *du-. 1. Compound *du-plo-, twofold (*-plo-, -fold; see pel-%), in Latin duplus, double: DOUBLE, (DOUBLET), (DOU- BLOON), (DOUBLURE), DUPLE. 2. Compound *du-plek- (*-plek-, -fold; see plek-), twofold, in Latin duplex, double: DUPLEX, DUPLICATE, (DUPLICITY); CONDUPLI- CATE. 3. Suffixed form *du-bhw-io- in Latin dubius, doubtful (< “hesitating between two alternatives”), and dubitdre, to be in doubt: DOUBT, DUBIOUS; (REDOUBT- ABLE). [Pok. du6(u)- 228.]
=== NYB tanur ===
=== AFA 26 Ofen ===
1498:lies Wortes . .li »Backofen", das schon Sachau zum Mu*arr.
=== AFM tanur ===
=== DEV athanor ===
LAM.txt:1876:Athanor. Four des alchimistes, d% jy:i\ attannoâr , foyer,
LAM.txt:7005:j^ tannoûr (V. athanor et Prov. Arab. 14.) four, duquel
LAM.txt:8471:Athanor
DEV.txt:627:Athanor.  Four  des  alchimistes.  c^On  se  servait  de  ce mot,  il  n'y  a  pas  encore  longtemps,  dit  Bescherelle,  pour désigner  un  fourneau  construit  de  façon  qu'avec  le  même feu  on  pouvait  faire  plusieurs  opérations  différentes.  ?5  Esp. atanor,  qui  a  pris  un  sens  très-différent,  tuyau  de  fontaine.
DEV.txt:632:Acanor,  cité  par  Bescherelle,  est  une  altération  de  atha- nor;  on  sait  avec  quelle  facilité  les  sons  k  et  t  permutent dans  la  langue  du  peuple.  Dans  le  Lexicon  alchemiœ  de Martin  Ruland,  on  trouve  encore:  nthonor,  anthonor,  fur- nus,  atanor,  olla  perforata.
DEV.txt:2188:C'est  la  prononciation  turque  du  mot  arabe-persan  ^y^ /a/motlr. fourneau  portatif,four.(Voy.  Athanor.)  Le  réchaud ou  brasero  du  tandour  s'appelle  aujourd'hui,  à  Constanti- nople,  le  mangnl,  ce  qui  représente  le  ,3^1a;-«  manqfddjiq de  Meninski.
DEV.txt:2369:Acanor,  voy.  Athanor.
DEV.txt:2745:Anthonor,  voy.  Athanor.
=== WEB athanor ===
WEB_vol1.txt
```


## [2026-09-14T03:15:03.988Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 dord ===\"; grep -n \"درد \\|دردی\" BQT_v2_pages.txt | head -8\necho \"=== AFA durdi ===\"; grep -n -iE \"durd|Hefe\" AFA.txt | head -8\necho \"=== AFM دردي ===\"; grep -n \"دردي\" AFM_pages.txt | head -5\necho \"=== MON طرطیر full ===\"; grep -n \"طرطیر\\|طرطير\" incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -5\necho \"=== SKT Tartarus lines ===\"; sed -n 19210,19220p SKT.txt"
}
```


### [2026-09-14T03:15:04.114Z] TOOL RESULT

```
=== BQT v2 dord ===
597:‫ودردی پیاله را یز کفته‌اند و»بسکون میم هم‬                                                                         ‫لت ‪.‬‬
1130:                        ‫برمیآ بدودرد لمیکند؟ ‪-‬‬        ‫ببفتتححاول و کون ثالی‪ .‬جنگجوی‬     ‫=‬   ‫جح‬
1796:       ‫چومثك دردیده زنم‪.‬‬            ‫قدمت‬    ‫خاك‬       ‫جشه فشانی ای پسر د رکوم‬        ‫چون‬
2188:‫را از آن جلق‬         ‫هزار وهشتاد قسم کنند وهرقسمی‬             ‫ات که بعربی حماض جبلی‌خوانند‪ .‬درد مفاصل‬
2442:                     ‫اظر ‏ بدرد کشان احز س‬              ‫فغان کهارکس جماش شیخ شهرامروز‬
3606:   ‫دردیگی نوکه بگل‌اندودة باشند کرده س‬
8964: ‫‪ :‬در آدمی عشفی و دردی و خارخاری و قاضابی‬                          ‫‪۳۸۲‬‬         ‫» تعلیقات فيه مافه مصحح فروزان‌فر ص‬
9257:‫ولقره را تبز گفته‌اند "‪ ۳‬و کنابه از کلزار ولالهزار‬                               ‫درد ‪.‬‬    ‫از جسد وقاب آدمی(‪)۱‬‬
=== AFA durdi ===
5725:Weines war. »Wer yon Euch Wein und Hefe will und
5731:aus dem Lande des Weines und der Hefe («^icJI ^%t ^^
=== AFM دردي ===
1572:دردي
4615:درديس 5١‏
=== MON طرطیر full ===
=== SKT Tartarus lines ===
source  of  the  word,  though
been  affected  and  tixed  by  the  F.  tA
—  A.S.  /ergon,  to  vex.  provoke;  < allied  to  tira  (4):  see  Tear  (i).
Tart  (i),  acrid :  see  Tear  (0. Tart  (>),  a  small  pie ;  see  Torton Tartan,  a  woUcn  stuff.  (F.-Sj L.  7)  F.  tiretaine.  *  Hn-iie-wolsic,  or  1 therof,  worn  ordinarily  by  the  I peasants;*  Cot  — Span.  tirtloAOr  1 woollen  stuff;  <to  named  from  its  Aim
—  Span,  tiritar,  to  shi^Tr,  shake  with Doubtless  from  a  lost  Latin  verb,  all Gk.  rapTtxpil*iV,  to  shake  vrith  cold Tartar  (3).
Tartar  (i),  an  add  sail  in  casfa^  1 cretion  on  the  teeth.  ( F.  —  Low.  L.  -^^ A  term  due  to  the  alchemists ;  called  jn tre,  or  tartre,  in  Chaucer.  —  F.  tartn,  *  ii Cot.;  Low  L.  tartarmm.  —  Arab,  durd, i sediment  tartar  of  wine:  duriiy.  1 Cf.  Arab,  darad,  a  shedding  of  teeth; Devic  connects  with  tartar  on  the  lee
Tartar  (a),  a  native  of  Tartary.  (1 A  per^'trse  spcllmg  of  Tatar,  owins popular  etymology  which  regarded  1 as  let  loose  out  of  Tartaruj  or  bd below).  From  Tdtar,  a  Tatar,  or  ii tant  of  Tatary  (as  it  should  be  spelt).
Tartar  (.0,  TartarD*,  hell  (U  - '  The  gates  of  Tartar ; '  Tw.  Nt  II  *
—  L.  Tartarus.  -  Gk.  Ttiprapoi,  Tai the  infemnJ   regions;    conceived, place  of  extreme  cold ;  cC  Gk- 10  shiver  with  cold.
Taak ;  see  Tangent.
Tassel  (i),  a  bunch  of  silk,  ftc, ornament  (F.  —  L.)  M,  E.  tojtel^ tassei,  an  ornament,  clasp :  also  a  pi< square  staff  (cf.  Ital.  tastelh,  a  aqai collar  of  a  cloak).  —  L.  taxiUum^  1 taxillus,  a  small  die;  dimin.  of  M knuckle-bone,  a  die  made  of  a  kn bone.  Ttilus  »  tax-lui*,  as  shrwa  I dimin.  taxiUus,  and  means  a  bone  1 squared ;  cf,  Skt  taksh,  to  hew,  pr make.  (VTAK.)  f  The  appliottl a  tassel  is  curious ;  a  wood-cut  at  ] of  Guillim'ft  Display  of  Heraldry  ( shews  a  tassel  ornamented  with  stiioj dots:  these  strings  divide  it  into  sq each  of  whicb  (having  a  dot  hi  them resembles  an  Me  cit  a  dit.
```


## [2026-09-14T03:15:18.456Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFA ctx ===\"; sed -n 1493,1503p AFA.txt\necho \"=== AFM ctx ===\"; sed -n 1568,1578p AFM_pages.txt\necho \"=== MON ctx 1149 ===\"; sed -n 1145,1152p MON_part1.txt"
}
```


### [2026-09-14T03:15:18.573Z] TOOL RESULT

```
=== AFA ctx ===
dies schon in der Form ^^^^p in*s Aramilische gewandert ist.
Zur Wurzel ^i^ wie mir Prof. G. Hotimanu brietfich an-
deutete, möchte ich es nur sehr ungern ziehen. Es ist
yielleicht auch wieder persischer Herkunft. Schon die
Araber (Mu^arnib 111) kennen den fremden Ursprung
lies Wortes . .li »Backofen", das schon Sachau zum Mu*arr.
40 richtig mit Verraitteluug von *3-|13 jj^ü aus fumus
^:jpusi erklärt hat.
Wir kommen nun zu einigeu fnMiiden Xamt*n für >0e-
biluile." Sprenger hat (Leb. Muhammeds I. p. 108) .i^sAj
für ein von Muhammed überuommeues aramäisches Wort
=== AFM ctx ===
وهو مركب من در اي باب ومن بي اي اسفل ورجل ٌْ
: ( 07 5 93 النظر ملون 1 ܠܨ ܐܠܨܐ اللحم تعرويب 82 ومنة
التي طوراج ورادفه اليونالي. ا ف 00005
(درْدِي) الريك وقرفها يقن رامين في اسفله من الكدر تعريب 9 او
دردي
* (الدرد : ) الداهية والشيخ والعجوذ الفانية مركب من دَرْد اي ألم ومن
يس اي ردي
* (الدردار) شجر عظي له زهر اصفر وورق شائك وثر كقرون الدفلى ( 2
دَردَار ويقال له بالتركة «قره اغاج »٠وقال‏ في البرهان القاطع 3 يقال له بالعر 7 2
شجر البق لان البق يتكون فيه كثيرا
070053
=== MON ctx 1149 ===


آبچی 
مععد‌نی. اسی که در آن جوش بعنی 
بی‌کربنات سود و اسید طرطیر کنند و مانند 
گوارشی بياشامند. 

آبسجی: آ[20 [تر. آغاناجی - آباجی ]
```


## [2026-09-14T03:15:20.313Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/tartar",
 "prompt": "Give the English noun \"tartar\" (potassium bitartrate / dental deposit) etymology in full: Middle English, Old French tartre, Medieval Latin tartarum, Byzantine/Medieval Greek tartaron, and any statement about Arabic durd or Semitic origin."
}
```


### [2026-09-14T03:15:27.073Z] TOOL RESULT

```
# Etymology of "Tartar" (Potassium Bitartrate/Dental Deposit)

Based on the Wiktionary entry, here's the full etymological chain:

The English noun derives from **Old French** *tartre*, which came from **Medieval Latin** *tartarum*. This Latin term originated from **Byzantine Greek** *τάρταρον* (tártaron).

The etymology then traces to **Arabic** *دُرْدِيّ* (durdiyy), described as meaning "dreg." The Arabic term itself derives from **Persian** *درد* (dord, "dreg"), which came from **Proto-Iranian** *dr̥ti-* ("manure, feces"). This ultimately connects to **Proto-Indo-European** *dʰṛ-to-*, itself from PIE *dʰreyd-* ("to have diarrhea").

The entry notes the word is "a doublet of *dirt*," indicating a shared etymological root through different linguistic pathways. The source acknowledges some uncertainty, noting the Arabic etymon connection appears in historical texts like Pelagonius's *Ars veterinaria*, though textual accuracy remains questioned.
```


## [2026-09-14T03:15:53.773Z] TOOL CALL #42: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/tartar\" \"https://en.wiktionary.org/wiki/%D8%AA%D9%86%D9%88%D8%B1\" \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%AF\" \"https://en.wiktionary.org/wiki/%CE%A4%CE%AC%CF%81%CF%84%CE%B1%CF%81%CE%BF%CF%82\" \"https://en.wiktionary.org/wiki/tartar\"; do python3 tools/fetch_source.py \"$u\" --note \"page 496, roots Tanur/Tartaros: tannur and tartar etymologies\" 2>&1 | tail -2; done"
}
```


## [2026-09-14T03:15:55.245Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/athanor",
 "prompt": "Etymology of English \"athanor\": which languages mediate (French, Spanish atanor, Arabic al-tannūr, Aramaic, Akkadian)?"
}
```


### [2026-09-14T03:15:56.260Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1aa2a536c15f61d4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e5fc067593e2ec2d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ae639a8171010ce6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b625c94bc81b6840.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/80f6428b7b0d8798.txt
```


### [2026-09-14T03:16:01.389Z] TOOL RESULT

```
# Etymology of "Athanor": Language Mediation

Based on the Wiktionary entry, the direct etymological path is:

**Arabic → English**

The entry states the word comes from "Arabic _التَنُّور_ (at-tannūr, 'the baker's oven')." It notes that English "athanor" is "a doublet of _tandoor_."

However, the page **does not discuss** intermediate language mediation through French, Spanish, Aramaic, or Akkadian. While French and Spanish cognates exist (both have "athanor"/"atanor"), the entry provides no information about whether these languages served as historical mediators in the word's transmission to English, or whether they independently borrowed from the same Arabic source.

To answer your question about intermediary languages, you would need sources beyond this dictionary entry.
```


## [2026-09-14T03:16:49.284Z] TOOL CALL #44: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/athanor\" --note \"page 496, root Tanur: athanor etymology\" 2>&1 | tail -1; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg496.png data/verification/sources/refs/ocr/BOOK/496.png && ls -la data/verification/sources/refs/ocr/BOOK/496.png"
}
```


### [2026-09-14T03:16:50.547Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/aad7e4754c8874a1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 78601 Sep 13 23:16 data/verification/sources/refs/ocr/BOOK/496.png
```


## [2026-09-14T03:23:11.830Z] TOOL CALL #45: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build496.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_TANUR = \"https://en.wiktionary.org/wiki/%D8%AA%D9%86%D9%88%D8%B1\"\nW_DORD  = \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%AF\"\nW_TART  = \"https://en.wiktionary.org/wiki/tartar\"\nW_TARTAROS = \"https://en.wiktionary.org/wiki/%CE%A4%CE%AC%CF%81%CF%84%CE%B1%CF%81%CE%BF%CF%82\"\nW_ATH   = \"https://en.wiktionary.org/wiki/athanor\"\nETY_T   = \"https://www.etymonline.com/word/tartar\"\n\nentry0 = {\n \"entry\": 0,\n \"root\": \"Tanŭr, Tannŭr\",\n \"verdict\": \"disputed\",\n \"modern_form\": \"Akkadian tinūru 'oven' → an ancient Near-Eastern culture word (Aram. tannūrā, Heb. tannūr, Arab. tannūr; Av. tanūra-, MP tanūr, NP تنور). Not an Indo-European root.\",\n \"note\": \"The forms collected in the box are all real, but the language label 'Indo-European' is wrong: there is no PIE root *tanur- (Pokorny has nothing, and Watkins' appendix puts 'oven' under *aukʷ- 'cooking pot', unrelated). The oldest attestation is Akkadian tinūru 'oven' (cuneiform 𒋾𒂟, 2nd millennium BC); from Akkadian/Aramaic the word spread west (Heb. tannūr, Arab. tannūr) and east into Iranian (Av. tanūra-, which Bartholomae marks expressly as a Semitic loanword, MP tanūr, Sogd. tnʾwr, NP tanūr). Nourai's own note reproduces Jeffery's 1938 compromise ('a word belonging to the pre-Semitic and pre-Indo-European population of the area'), which is a defensible historical guess but not a licence to label the root Indo-European; Bartholomae, Fraenkel, Mo'in's footnote in Borhan-e Qate' and today's dictionaries all make the Iranian forms borrowings, i.e. the arrows into Avestan run the wrong way round for an IE root. The tree itself (Semitic branch + Iranian branch + Akkadian) is otherwise sound.\",\n \"note_fa\": \"واژهٔ «تنور» ریشهٔ هندواروپایی ندارد و برچسب «هندواروپایی» در کتاب نادرست است؛ پوکورنی چنین ریشه‌ای ندارد و واتکینز واژه‌های «تنور/اجاق» را زیر *aukʷ- «دیگ» می‌آورد که بی‌ربط است. کهن‌ترین گواه، اکدی tinūru «تنور» است که از آنجا به آرامی «تنورا»، عبری tannūr و عربی «تنّور» و نیز به ایرانی (اوستایی tanūra-، فارسی میانه tanūr، سغدی tnʾwr، فارسی نو «تنور») راه یافته است. بارتولومه در فرهنگ ایرانی باستان (ستون ۶۳۸) صورت اوستایی را صریحاً «وام‌واژه از سامی» می‌خواند و معین نیز در حاشیهٔ برهان قاطع (ص ۵۲۳) همین را می‌آورد. پس ادعای نورایی دربارهٔ وجود واژه در این زبان‌ها درست است، اما هندواروپایی‌دانستن ریشه را پژوهش امروزی رد می‌کند و آن را واژه‌ای فرهنگی و وام‌گرفته از خاور نزدیک باستان می‌داند.\",\n \"sources\": [W_TANUR, W_ATH],\n \"ref_check\": [\n   {\"ref\": \"FVQ:92-94\", \"status\": \"supports\", \"note\": \"Jeffery, Foreign Vocabulary, pp. 93-95 (FVQ_pages.txt ll. 3610-3690): 'In Avestic we find the word tanura (cf. Vendidad, viii, 254), and in Phlv. it is ... meaning baking oven'; 'It also occurs as tinuru in Akkadian'; and his conclusion, 'The truth would seem to be that it is a word belonging to the pre-Semitic and pre-Indo-European population of the area' — exactly Nourai's note. Jeffery does NOT call it Indo-European; he says 'The word, however, is no more Iranian than it is Semitic ... the Iranian scholars treat it as a loan-word from Semitic.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"grep -ic 'tannur|tanur' POK_full.txt = 0\", \"stance\": \"silent\", \"note\": \"Pokorny's IEW has no root or entry for tanūr/tannūr in any spelling; no IE reconstruction exists.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. aukʷ-\", \"stance\": \"contradicts\", \"note\": \"Watkins derives the IE words for 'oven' from 'aukʷ-, Cooking pot ... Old English ofen, furnace, oven: OVEN' — the IE family for 'oven' is quite separate from tanūr.\"},\n   {\"src\": \"BRT\", \"where\": \"col. 637/638 s.v. tanūra-\", \"stance\": \"partial\", \"note\": \"'tanūra- n. \\\"Backofen\\\" ... LW. aus dem s[emitischen], np. تنور' — the Avestan word exists, but Bartholomae marks it a Semitic loanword, not an inherited IE form.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/تنور\", \"stance\": \"contradicts\", \"note\": \"Persian tanūr 'from Middle Persian tnwr /tanūr/, compare Sogdian tnʾwr, ultimately from Akkadian 𒋾𒂟 (tinūru)'; Arabic tannūr 'borrowed from Aramaic tannūrā ... ultimately from Akkadian tinūru'. No Indo-European ancestry.\"}\n ],\n \"nodes\": []\n}\n\nn = entry0[\"nodes\"].append\nn({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"tanŭra\", \"verdict\": \"plausible\",\n \"derivation\": \"Avestan tanūra- n. 'baking oven' is genuinely attested (Vendidad 8.254, of the oven in which impure matter is burnt) and stands in Bartholomae's Altiranisches Wörterbuch col. 638. But it is not an inherited Iranian word: Bartholomae writes 'LW. aus dem sem.' ('loanword from Semitic') and links it directly to NP تنور. The source is the Akkadian/Aramaic culture word (Akk. tinūru, Aram. tannūrā) which reached Iran with the Mesopotamian bread-oven itself, probably already in the Achaemenid period; Avestan simply renders the foreign word with -ū- and an -a- stem ending. So as a node it is correct, but only as a loan from the Semitic word, not as a daughter of an Indo-European root.\",\n \"derivation_fa\": \"صورت اوستایی tanūra- «تنور، اجاق نان‌پزی» واقعاً گواهی شده است (وندیداد ۸، ۲۵۴) و بارتولومه آن را در ستون ۶۳۸ فرهنگ ایرانی باستان آورده است؛ اما همانجا می‌نویسد «وام‌واژه از سامی» و آن را با «تنور» فارسی نو پیوند می‌دهد. یعنی این واژه از اکدی tinūru / آرامی tannūrā همراه با خودِ تنورِ میان‌رودانی به ایران آمده و در اوستایی با ستاک -a پذیرفته شده است. بنابراین گرهِ اوستایی درست است، اما نه به عنوان فرزندِ یک ریشهٔ هندواروپایی، بلکه به عنوان وام‌واژه‌ای سامی.\",\n \"sources\": [W_TANUR],\n \"ref_check\": [\n   {\"ref\": \"FVQ:94\", \"status\": \"supports\", \"note\": \"Jeffery p. 94: 'In Avestic we find the word tanura (cf. Vendidad, viii, 254), and in Phlv. it is ... meaning baking oven' (FVQ_pages.txt l. 3654), with the footnote 'Cf. Bartholomae, AiW, 638'.\"},\n   {\"ref\": \"BQT:523\", \"status\": \"supports\", \"note\": \"Mo'in's etymological footnote (BQT_v1_pages.txt ll. 31345-31355, the note continuing از صفحهٔ ۵۲۳): 'دراوستا کلمهٔ tanūra آمده (رک: وندیداد ۸، ۲۵۴)، ودر پهلوی صورت tanūr بمعنی اجاق ...'\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 638, s.v. tanūra-\", \"stance\": \"supports\", \"note\": \"'tanūra- n. \\\"Backofen\\\" ... LW. aus dem s(em.), np. تنور' — the form and gloss are exactly Nourai's; the Semitic-loan label is his omission.\"},\n   {\"src\": \"SOD\", \"where\": \"no. 9609 (tnʾwr)\", \"stance\": \"supports\", \"note\": \"Gharib glosses Sogd. tnʾwr 'tanūr, furnace, oven' and marks it '©<Av. tanura, MP tnwr', i.e. she too works with an Avestan tanūra-.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/تنور\", \"stance\": \"silent\", \"note\": \"The Persian entry goes back only to Middle Persian tanūr and thence to Akkadian; the Avestan form is not mentioned, so the Avestan link is not part of the standard modern chain.\"}\n ]\n})\nn({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"tanŭr\", \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian tanūr (Book Pahlavi tnwl/tnwr) 'oven' is the regular continuation of the Old Iranian form of the borrowed word; MacKenzie's Concise Pahlavi Dictionary lists 'tanūr' between tanuk and tantūhmag. The word passes to New Persian unchanged (tanūr), since MP -ū- and final -r are stable. Nourai's added note that Henning (MPP:88) gives 'tnwr' as a Parthian form is plausible — the word is equally at home in Parthian, and Sogdian tnʾwr shows the same shape — but could not be checked here: the local MPP file is Henning's 1958 'Mitteliranisch' survey, not the 1937 BSOS word-list Nourai cites.\",\n \"derivation_fa\": \"فارسی میانهٔ tanūr (به خط پهلوی tnwl/tnwr) «تنور» دنبالهٔ منظمِ همان وام‌واژه است و مکنزی در فرهنگ کوچک پهلوی آن را ثبت کرده است. چون در فارسی میانه «او»ی کشیده و «ر» پایانی پایدارند، واژه بی‌دگرگونی به فارسی نو «تنور» رسیده است. یادداشت نورایی دربارهٔ صورت پارتی tnwr به نقل از هنینگ پذیرفتنی می‌نماید (سغدی tnʾwr نیز همین ساخت را دارد)، ولی نسخهٔ در دسترس از هنینگ، مقالهٔ ۱۹۵۸ «ایرانی میانه» است نه فهرست واژگان ۱۹۳۷، و از این رو راستی‌آزمایی نشد.\",\n \"sources\": [W_TANUR],\n \"ref_check\": [\n   {\"ref\": \"FVQ:94\", \"status\": \"supports\", \"note\": \"Jeffery p. 94: '... and in Phlv. it is [tnwl] meaning baking oven', footnote 5 'West, Glossary, 121' (FVQ_pages.txt l. 3654).\"},\n   {\"ref\": \"MPP:88\", \"status\": \"not_checked\", \"note\": \"Nourai's note cites Henning, 'A List of Middle-Persian and Parthian Words', BSOS IX, p. 88 for Parthian tnwr. The local MPP.txt is Henning's 1958 'Mitteliranisch' (Handbuch der Orientalistik) instead; grep -i 'tnwr|tanur' returns nothing there.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 81 / PHD.txt l. 4481 and PHD_mackenzie.txt l. 8226\", \"stance\": \"supports\", \"note\": \"'tanūr' is listed as a headword, and the English index has 'oven tanur'.\"},\n   {\"src\": \"NYB\", \"where\": \"grep 'tanur|tnwr' NYB_vol2_glossary.txt = 0\", \"stance\": \"silent\", \"note\": \"Nyberg's glossary (which covers only the texts of his Manual) has no entry for the word.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/تنور\", \"stance\": \"supports\", \"note\": \"'Persian تنور (tanūr) ... from Middle Persian tnwr /tanūr/, \\\"oven\\\"'.\"}\n ]\n})\nn({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"tanŭr «تنور»\", \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian تنور tanūr 'oven, clay bread-oven' continues Middle Persian tanūr without change; the same word gives Turkish/Urdu tandūr (whence English tandoor, a doublet of athanor). Mo'in's footnote to Borhan-e Qate' (p. 523) sets out precisely this history: the Arabic tannūr is borrowed from Aramaic tannūrā, Fraenkel thought the Aramaic word itself Iranian, the Avestan tanūra- and Pahlavi tanūr exist, and the word is 'neither Iranian nor Semitic' in ultimate origin (he is quoting Jeffery 92-95).\",\n \"derivation_fa\": \"«تنور» فارسی نو دنبالهٔ بی‌واسطهٔ tanūr فارسی میانه است و هیچ دگرگونی آوایی چشمگیری نیافته است؛ همین واژه از راه ترکی به صورت «تندیر/tandoor» به زبان‌های دیگر رفته است. معین در حاشیهٔ برهان قاطع (ص ۵۲۳) همین تاریخچه را می‌آورد: «لغت عربی تنور از آرامی به عاریت گرفته شده... در اوستا کلمهٔ tanūra آمده... و در پهلوی صورت tanūr به معنی اجاق». ادعای نورایی در این گره درست است.\",\n \"sources\": [W_TANUR],\n \"ref_check\": [\n   {\"ref\": \"BQT:523\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' with Mo'in's footnote (BQT_v1_pages.txt ll. 31344-31356): 'برآنست که لغت عربی «تنور» ازآرامی بعاریت گرفته شده. در آرامی «تنورا» و در عبری «تنور» ... فرانکل گوید لغت آرامی خود منشعباً ایرانی است. در اوستا کلمهٔ tanūra آمده (رک: وندیداد ۸، ۲۵۴) و در پهلوی صورت tanūr بمعنی اجاق ... با این حال لغت مزبور بنظر می‌رسد نه ایرانی باشد و نه سامی ... «جفری ۹۲-۹۵»'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol. 1 p. 523 + footnote continued on p. 524\", \"stance\": \"supports\", \"note\": \"See the quotation above; Mo'in's note is itself a summary of Jeffery and Fraenkel.\"},\n   {\"src\": \"HRN\", \"where\": \"grep 'tanur|tanūr' HRN.txt = 0\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no number for tanūr (he confines himself to inherited Iranian vocabulary; 'Ofen' appears only s.v. dāš no. 526).\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/تنور\", \"stance\": \"supports\", \"note\": \"Persian تنور from MP tanūr, 'ultimately from Akkadian tinūru'.\"}\n ]\n})\nn({\n \"id\": 4, \"lang\": \"Sogdian\", \"words\": \"tn`wr\", \"verdict\": \"confirmed\",\n \"derivation\": \"Buddhist Sogdian tnʾwr /tanūr/ 'furnace, oven' is entry 9609 of Gharib's Sogdian Dictionary, attested in the Sūtra of the Causes and Effects (SCE 206). Gharib herself derives it exactly as Nourai draws it, '< Av. tanūra, MP tnwr', i.e. the same Near-Eastern word taken over into Eastern Iranian, with ʾ marking the long ū. The Sogdian form shows no specifically Sogdian sound change, which is itself evidence of a loan rather than an inherited word.\",\n \"derivation_fa\": \"سغدی بودایی tnʾwr /tanūr/ «کوره، تنور» در فرهنگ سغدی قریب، مدخل ۹۶۰۹، آمده و گواه آن متن «علل و معلولات» (SCE 206) است. قریب خود همان مسیری را می‌آورد که نورایی رسم کرده است: «< اوستایی tanūra، فارسی میانه tnwr». نبودِ دگرگونی آوایی ویژهٔ سغدی در این صورت، خود نشانهٔ وام‌بودن واژه است. ادعای نورایی در این گره درست است.\",\n \"sources\": [W_TANUR],\n \"ref_check\": [\n   {\"ref\": \"SOD:388\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry no. 9609 (SOD_pages.txt l. 31442-31443): '9609 tnʾwr B ... tanur ©<Av. tanura, MP tnwr | furnace, oven | SCE 206'. Nourai's '388' is the printed page carrying that entry (the entry numbering runs to ~10,800, so 388 cannot be an entry number here).\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"no. 9609\", \"stance\": \"supports\", \"note\": \"See quotation above; gloss 'furnace, oven' matches Nourai's 'oven'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/تنور\", \"stance\": \"supports\", \"note\": \"'compare Sogdian tnʾwr /tanūr/, \\\"furnace, oven\\\"' cited under Persian تنور.\"}\n ]\n})\nn({\n \"id\": 5, \"lang\": \"Hebrew\", \"words\": \"tannŭr\", \"verdict\": \"confirmed\",\n \"derivation\": \"Biblical Hebrew תַּנּוּר tannūr 'oven, furnace' is frequent in the Old Testament (Gen. 15:17, Lev. 2:4, Hos. 7:4) and is rendered κλίβανος in the Septuagint. Klein (p. 121) states it is 'rel. to Akkad. tinnuru, \\\"oven\\\"'; modern Semitists (Zimmern, Akkadische Fremdwörter 32; CAD s.v. tinūru) treat Hebrew and Aramaic tannūrā alike as borrowings from Akkadian tinūru with the doubling of -n- characteristic of the West Semitic shape. Placing Hebrew directly under the culture-word 'root' is therefore right, though it is a sister of Aramaic rather than the fountainhead.\",\n \"derivation_fa\": \"عبری کتاب‌مقدسی תַּנּוּר (tannūr) «تنور، کوره» بارها در عهد عتیق آمده است (پیدایش ۱۵:۱۷، لاویان ۲:۴، هوشع ۷:۴) و در ترجمهٔ سبعینیه κλίβανος برگردانده شده است. کلاین (ص ۱۲۱) آن را «هم‌ریشه با اکدی tinnuru» می‌داند و سامی‌شناسان امروز (تسیمرن، فرهنگ آشوری شیکاگو) عبری tannūr و آرامی tannūrā را هر دو وام‌گرفته از اکدی tinūru می‌شمارند که در سامی غربی با مشدّدشدن «ن» پذیرفته شده است. پس گره درست است، هرچند عبری خواهرِ آرامی است نه سرچشمهٔ واژه.\",\n \"sources\": [W_TANUR],\n \"ref_check\": [\n   {\"ref\": \"KLN:121\", \"status\": \"supports\", \"note\": \"Klein 1966 p. 121 s.v. athanor: '... and tannūr, \\\"oven\\\", borrowed fr. Heb. tannūr, which is rel. to Akkad. tinnuru, \\\"oven\\\"' (KLN_1966.txt l. 3811, after the page marker 121 at l. 3788).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 121 s.v. athanor\", \"stance\": \"supports\", \"note\": \"See quotation; Klein makes Hebrew the immediate donor of the Arabic word, as Nourai's arrow does.\"},\n   {\"src\": \"FVQ\", \"where\": \"p. 94\", \"stance\": \"partial\", \"note\": \"Jeffery: 'In the O.T. תנור occurs frequently for furnace or oven, i.e. the Gk. κλίβανος, and the form in the Aram. Targums is תנורא, corresponding with the Syr. ... It also occurs as tinuru in Akkadian' — Hebrew is one member of the Semitic set, not its head.\"},\n   {\"src\": \"AFA\", \"where\": \"Fraenkel, Aram. Fremdwörter, p. 26 (AFA.txt ll. 1493-1500)\", \"stance\": \"partial\", \"note\": \"'Schon die Araber (Mu'arrab 111) kennen den fremden Ursprung dieses Wortes ... \\\"Backofen\\\", das schon Sachau zum Mu'arr. richtig mit Vermittelung von [Aram. תנורא] erklärt hat' — Fraenkel routes the Arabic word through Aramaic, not Hebrew.\"}\n ]\n})\nn({\n \"id\": 6, \"lang\": \"Arabic\", \"words\": \"at-tannŭr\", \"verdict\": \"plausible\",\n \"derivation\": \"Arabic التَّنُّور at-tannūr 'the oven' (al- + tannūr, with the assimilation of l to the 'sun letter' t) is the form that the medieval alchemists' vocabulary carried into Europe. The word itself, however, entered Arabic from Aramaic tannūrā, not from Hebrew: this is Fraenkel's conclusion (Aram. Fremdwörter 26, following Sachau on the Muʿarrab), Jeffery's (FVQ 93-94) and Wiktionary's ('borrowed from Aramaic tannūrā ... ultimately from Akkadian tinūru'). Klein's 'borrowed fr. Heb. tannūr', which Nourai follows, is the older and looser formulation. The alchemical sense 'self-feeding digesting furnace' is a specialisation of the ordinary 'bread oven' inside 8th-10th c. Arabic alchemy (Jābir, al-Rāzī).\",\n \"derivation_fa\": \"عربی «التَّنّور» (al- + تنّور، با همگونیِ لامِ تعریف پیش از «ت» که از حروف شمسی است) همان صورتی است که واژگان کیمیاگریِ سده‌های میانه به اروپا رساند. اما خودِ واژه از آرامی «تنورا» به عربی رفته است، نه از عبری: فرانکل (ص ۲۶)، جفری (ص ۹۳-۹۴) و ویکی‌واژه همین را می‌گویند و سرانجام آن را به اکدی tinūru بازمی‌گردانند. گفتهٔ کلاین که نورایی از او گرفته («وام‌گرفته از عبری») صورت‌بندیِ کهنه‌تر و سست‌تری است. معنای کیمیاییِ «کورهٔ خودسوز» نیز تخصیصِ معنایی همان «تنور نان‌پزی» در کیمیای عربی سده‌های دوم تا چهارم هجری است. پس ادعای نورایی با احتیاط پذیرفتنی است، با تصحیحِ واسطهٔ آرامی.\",\n \"sources\": [W_TANUR, W_ATH],\n \"ref_check\": [\n   {\"ref\": \"TAD:18\", \"status\": \"supports\", \"note\": \"Tobia al-Unaysi, Tafsīr al-alfāẓ al-dakhīla (TAD_pages.txt l. 749): 'التنور - في العبرانية «تنور»، في الارامية «تنورا» وهو منحوت من ...' — he lists tannūr among the loanwords in Arabic and names Hebrew and Aramaic, which is what Nourai's arrow and his root note ('TAD:18 ... derive it from root N.w.r') reflect.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AFA\", \"where\": \"Fraenkel p. 26\", \"stance\": \"partial\", \"note\": \"'Schon die Araber (Muʿarrab 111) kennen den fremden Ursprung dieses Wortes ... das schon Sachau zum Muʿarr. richtig mit Vermittelung von [Aramaic] erklärt hat'; he even allows 'Es ist vielleicht auch wieder persischer Herkunft'.\"},\n   {\"src\": \"FVQ\", \"where\": \"pp. 93-94\", \"stance\": \"partial\", \"note\": \"'Fraenkel, Fremdw, 26, suggested that the word came into Arabic from the Aram.' — Aramaic, not Hebrew.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 2019 'Ar. tannūr'\", \"stance\": \"supports\", \"note\": \"Lokotsch: 'Ar. tannūr: \\\"Ofen, und zwar beweglicher Ofen\\\" [vgl. Assyr. tinūru, Del HWB 711b] ... hieraus mit ar. Art. sp. atanor im MA \\\"Ofen der Alchemisten\\\", frz. athanor \\\"Alchemistenofen\\\"'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/تنور\", \"stance\": \"partial\", \"note\": \"Arabic تنّور 'borrowed from Aramaic tannūrā ... ultimately from Akkadian tinūru' — Hebrew is not the donor.\"}\n ]\n})\nn({\n \"id\": 7, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"plausible\",\n \"derivation\": \"Pass-through node: French athanor 'four des alchimistes', the furnace kept at a constant heat by a self-feeding hopper, attested in French alchemical writing from the late Middle Ages and still in Bescherelle's dictionary. It is the Arabic at-tannūr taken over with the article agglutinated, but the route was through Spain: Lokotsch (no. 2019) and Devic give Spanish atanor (medieval 'alchemists' furnace', later 'water pipe') as the intermediary, French athanor (also altered to acanor, anthonor, athonor in the alchemical lexica) following it. Nourai leaves the node wordless, so only the language step can be judged; it is right in substance, with Spanish deserving a place in the chain.\",\n \"derivation_fa\": \"این گره تهی است و تنها زبان را نشان می‌دهد: فرانسوی athanor «کورهٔ کیمیاگران»، همان کوره‌ای که با قیفِ خودخوراک گرمای یکنواخت نگاه می‌دارد. این واژه همان «التنّور» عربی است که با حرف تعریفِ چسبیده وام گرفته شده، اما راهِ آن اسپانیا بوده است: لوکوچ (شمارهٔ ۲۰۱۹) و دویک صورت اسپانیایی atanor را واسطه می‌دانند و صورت‌های دگرگونِ acanor، anthonor و athonor نیز در فرهنگ‌های کیمیایی دیده می‌شود. بنابراین گامِ زبانیِ نورایی درست است، اما جای اسپانیایی در زنجیره خالی مانده است.\",\n \"sources\": [W_ATH],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node; checked independently against Devic, Lammens and Lokotsch (below).\"}\n ],\n \"consulted\": [\n   {\"src\": \"DEV\", \"where\": \"p. 216 s.v. Athanor (DEV.txt l. 627)\", \"stance\": \"supports\", \"note\": \"'Athanor. Four des alchimistes ... Esp. atanor, qui a pris un sens très-différent, tuyau de fontaine' — and l. 632: 'Acanor ... est une altération de athanor ... on trouve encore: athonor, anthonor, furnus, atanor, olla perforata'.\"},\n   {\"src\": \"LAM\", \"where\": \"p. 52 s.v. Athanor (LAM.txt l. 1876)\", \"stance\": \"supports\", \"note\": \"'Athanor. Four des alchimistes, [ar.] attannoûr, foyer.'\"},\n   {\"src\": \"LKT\", \"where\": \"no. 2019\", \"stance\": \"supports\", \"note\": \"'hieraus mit ar. Art. sp. atanor im MA \\\"Ofen der Alchemisten\\\" ... frz. athanor \\\"Alchemistenofen\\\"' — Spanish mediating.\"}\n ]\n})\nn({\n \"id\": 8, \"lang\": \"English\", \"words\": \"athanor\", \"verdict\": \"confirmed\",\n \"derivation\": \"English athanor 'a self-feeding digesting furnace used by alchemists' is borrowed from French athanor (Chaucer's age onward in alchemical texts, and standard in 17th c. chemical writing); Klein p. 121 gives exactly this chain: 'F., fr. Arab. at-tannūr, \\\"the oven\\\", fr. at-, assimilated form of al-, \\\"the\\\", and tannūr, \\\"oven\\\"'. English thus keeps the Arabic article as part of the stem, like alcohol, alembic, alkali — the tell-tale sign of the alchemists' Arabic vocabulary. It is a doublet of tandoor, which reached English from the same word through Persian/Urdu.\",\n \"derivation_fa\": \"انگلیسی athanor «کورهٔ خودخوراکِ کیمیاگران» از فرانسوی athanor وام گرفته شده و کلاین (ص ۱۲۱) همین زنجیره را می‌آورد: «از فرانسوی، از عربی at-tannūr، از at- صورتِ همگون‌شدهٔ al- و tannūr». مانند alcohol و alembic و alkali، حرف تعریف عربی در این واژه بخشی از ستاک شده است ــ نشانهٔ آشکارِ واژگان کیمیای عربی. این واژه دوگانهٔ (doublet) واژهٔ tandoor است که از همین «تنور» ولی از راه فارسی و اردو به انگلیسی رسیده است. ادعای نورایی درست است.\",\n \"sources\": [W_ATH],\n \"ref_check\": [\n   {\"ref\": \"FSD:178\", \"status\": \"supports\", \"note\": \"Funk & Wagnalls vol. I (FSD_vol1.txt l. 27992) carries the headword 'athenor ... Same as athanor', i.e. the word is in F&W at the place Nourai cites (p. 178, letter A).\"},\n   {\"ref\": \"KLN:121\", \"status\": \"supports\", \"note\": \"Klein 1966 p. 121: 'athanor, n., the self feeding furnace of the alchemists. — F., fr. Arab. at-tannūr, \\\"the oven\\\" ...' (KLN_1966.txt l. 3811).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 121\", \"stance\": \"supports\", \"note\": \"See quotation above.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/athanor\", \"stance\": \"supports\", \"note\": \"'From Arabic التَنُّور (at-tannūr, \\\"the baker's oven\\\") ... Doublet of tandoor.'\"},\n   {\"src\": \"DEV\", \"where\": \"p. 216\", \"stance\": \"supports\", \"note\": \"French athanor is documented as the alchemists' furnace, the immediate source of the English word.\"}\n ]\n})\nn({\n \"id\": 9, \"lang\": \"Arabic\", \"words\": \"tannŭr\", \"verdict\": \"plausible\",\n \"derivation\": \"Arabic تَنُّور tannūr 'oven' is a Qur'anic word (XI:40 and XXIII:27, of the oven that 'boiled over' at the Flood) and is the entry Jeffery discusses on FVQ 92-95; old Arabic poetry (Ḥamāsa 792, 'a loaf which a Nabataean woman bakes in her oven') shows it in the plain sense. The Arab philologists themselves tried to derive it from nūr 'light, fire' with an augmented t-, which Jeffery and the Lisān reject ('taffūl is not a genuine Arabic form at all'). Drawing it straight from the culture-word is therefore right in substance, but the transmission ran through Aramaic tannūrā, so this node duplicates #6 rather than representing a second, independent borrowing.\",\n \"derivation_fa\": \"«تَنّور» عربی واژه‌ای قرآنی است (هود ۴۰ و مؤمنون ۲۷، دربارهٔ تنوری که به هنگام توفان «فار») و جفری در صفحات ۹۲ تا ۹۵ همان را بررسی می‌کند؛ شعر کهن عربی (حماسه ۷۹۲) نیز آن را در معنای ساده به کار برده است. لغویان عرب کوشیده‌اند آن را از «نور» با «ت» زائد بگیرند، اما جفری و لسان‌العرب این را رد می‌کنند («وزن تَفعول در عربی اصیل نیست»). پس پیوند این گره به واژهٔ فرهنگیِ کهن درست است، ولی راهِ ورود آن آرامی «تنورا» بوده و این گره در عمل همان گرهٔ شمارهٔ ۶ است، نه وام‌گیریِ جداگانه‌ای.\",\n \"sources\": [W_TANUR],\n \"ref_check\": [\n   {\"ref\": \"FVQ:92\", \"status\": \"supports\", \"note\": \"Jeffery's entry begins at p. 92 and the discussion quoted at pp. 93-94 (FVQ_pages.txt ll. 3610-3690) shows the Qur'anic word, its old-poetry attestations and the philologists' failed derivation from نور: 'This judgment of the philologers is vindicated by the fact that [taffūl] is not a genuine Arabic form at all.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"AFA\", \"where\": \"Fraenkel p. 26\", \"stance\": \"partial\", \"note\": \"Fraenkel derives the Arabic word from Aramaic (with Sachau), i.e. not directly from the primitive culture word.\"},\n   {\"src\": \"AFM\", \"where\": \"grep 'تنور' AFM_pages.txt = 0\", \"stance\": \"silent\", \"note\": \"Addi Shir does not list تنور among the Persian loanwords in Arabic — consistent with an Aramaic, not Persian, source.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/تنور\", \"stance\": \"partial\", \"note\": \"Arabic تنّور 'borrowed from Aramaic tannūrā ... ultimately from Akkadian tinūru'.\"}\n ]\n})\nn({\n \"id\": 10, \"lang\": \"Akkadian\", \"words\": \"tinnŭra\", \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The Akkadian word is real and is in fact the oldest member of the whole family — tinūru (logographic 𒋾𒂟, Old Babylonian onward), 'oven, kiln', the ancestor (directly or through Aramaic) of Hebrew tannūr, Aramaic tannūrā, Arabic tannūr and of the Iranian forms. But the shape printed here, 'tinnŭra', is not an Akkadian form: the nominative is tinūru (so CAD and Wiktionary), Klein writes 'tinnuru' and Jeffery 'tinuru'; the final -a belongs to the Aramaic emphatic state tannūrā and to the hypothetical 'older form tannura' that D. H. Müller posited and Jeffery quotes at p. 94 n. 3. The page image (pdf p. 496) shows the book itself printing 'tinnŭra', so the extraction is faithful and the odd form is Nourai's own conflation of the Akkadian with the Aramaic form.\",\n \"derivation_fa\": \"واژهٔ اکدی راست است و در حقیقت کهن‌ترین عضو این خانواده است: tinūru «تنور، کوره» (از بابلی کهن به بعد)، که نیای عبری tannūr، آرامی tannūrā، عربی تنّور و صورت‌های ایرانی است. اما شکلی که در کتاب آمده، «tinnŭra»، صورت اکدی نیست: حالت فاعلی tinūru است (فرهنگ آشوری شیکاگو و ویکی‌واژه)، کلاین «tinnuru» و جفری «tinuru» می‌نویسند؛ «ـا»ی پایانی از آنِ حالت مؤکدِ آرامی «تنورا» و صورت فرضیِ tannura (د. ه. مولر، به نقل جفری ص ۹۴ پانوشت ۳) است. تصویر صفحهٔ ۴۹۶ نشان می‌دهد که خودِ کتاب «tinnŭra» چاپ کرده است؛ پس خطا از خوانشِ اسکن نیست، بلکه آمیختنِ صورت اکدی و آرامی به دست نورایی است.\",\n \"error_in\": \"book\",\n \"book_prints\": \"tinnŭra\",\n \"correct_form\": \"tinūru\",\n \"sources\": [W_TANUR],\n \"ref_check\": [\n   {\"ref\": \"KLN:121\", \"status\": \"partial\", \"note\": \"Klein p. 121 has 'rel. to Akkad. tinnuru, \\\"oven\\\"' — double n but final -u, not -a.\"},\n   {\"ref\": \"FVQ:94\", \"status\": \"partial\", \"note\": \"Jeffery p. 94: 'It also occurs as tinuru in Akkadian' (footnote: Zimmern, Akkad. Fremdw, 32); the form with -a appears only in his n. 3, 'D. H. Müller ... suggesting that [Heb.] תנור is a borrowing from Mesopotamia from an older form tannura'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"p. 121\", \"stance\": \"partial\", \"note\": \"'Akkad. tinnuru' — supports the etymon but not the final -a.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 2019\", \"stance\": \"partial\", \"note\": \"Lokotsch cites 'Assyr. tinūru, Del[itzsch] HWB 711b' — Delitzsch's Assyrisches Handwörterbuch has tinūru.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/تنور\", \"stance\": \"partial\", \"note\": \"'ultimately from Akkadian 𒋾𒂟 (tinūru)' — the standard citation form.\"}\n ]\n})\n\nentry4 = {\n \"entry\": 4,\n \"root\": \"Tartaros\",\n \"verdict\": \"disputed\",\n \"modern_form\": \"Two different Greek words: Τάρταρος 'the underworld' (Pre-Greek, Beekes EDG 1455) and Byzantine Greek τάρταρον 'deposit crusting wine casks' (> ML tartarum), the latter probably from Arabic durdī < Persian dord.\",\n \"note\": \"The root box itself is a real Greek word with the right gloss — Τάρταρος, the abyss below Hades in Hesiod's Theogony — but it is the wrong root for this tree, and its own etymology is no longer explained as Klein explains it. (a) Modern scholarship (Beekes, Etymological Dictionary of Greek, s.v. Τάρταρος) treats the mythological word as a Pre-Greek substrate word of reduplicated shape; Wiktionary records only Strabo's guess (from Ταρτησσός) and Klein's 'word of imitative origin', both antiquarian. (b) The chemical word is a separate lexeme: Medieval/Byzantine Greek τάρταρον 'tartar of wine casks', which Wiktionary, Skeat, Devic and Funk & Wagnalls all derive from Arabic durdī 'dregs', itself from Persian dord; Etymonline is the dissenting modern voice ('a Semitic source has been proposed ... Arabic is unlikely because of the early date of the word in Latin'). (c) Nourai's arrows therefore run backwards at the top of the tree: Persian dord and Arabic durdī are not descendants of Greek Tartaros; dord is inherited Iranian (Proto-Iranian *dr̥ti-, PIE *dʰreyd- 'to have diarrhoea', a cognate of English dirt) and is the ultimate SOURCE of the European word, if the Arabic etymology is right at all. The lower half of the tree (Arabic/Latin > French tartre > English tartar, plus the modern Arabic/Persian back-loans) is sound. EXTRACTION NOTE: on the printed page the Latin box (#3) hangs from the root's own spine, not from the Arabic box; and the Ferdowsī hemistich is printed «از این آشتی جنگ بهر منست» (آشتی), while the JSON reads آتشی.\",\n \"note_fa\": \"جعبهٔ ریشه واژه‌ای یونانی و واقعی است ــ Τάρταρος، ژرفنای زیرِ هادس در «تئوگونی» هزیود ــ اما ریشهٔ درستِ این درخت نیست و ریشه‌شناسیِ خودش نیز امروز آن‌گونه که کلاین می‌گفت توضیح داده نمی‌شود: بیکس آن را واژه‌ای از بستر پیش‌یونانی می‌داند، نه «تقلید آوایی». افزون بر این، واژهٔ شیمیایی، لفظِ دیگری است: یونانیِ بیزانسی τάρταρον «دُردِ بسته بر جدار خمره»، که ویکی‌واژه، اسکیت، دویک و فانک‌واگنالز آن را از عربی «دُردی» و آن را از فارسی «دُرد» می‌گیرند (اتیمآنلاین مخالف است و می‌گوید کهن‌بودنِ صورتِ لاتینی با وام‌گیری از عربی نمی‌خواند). بنابراین جهت پیکان‌ها در بالای درخت وارونه است: «دُرد» فارسی از یونانی نیامده، بلکه واژه‌ای ایرانی و ارثی است (ایرانی آغازین *dr̥ti-، هندواروپایی *dʰreyd-، هم‌ریشه با dirt انگلیسی) و خودْ سرچشمهٔ واژهٔ اروپایی است. نیمهٔ پایینِ درخت (لاتین ← فرانسه ← انگلیسی و وام‌های بازگشتیِ عربی و فارسی) درست است.\",\n \"sources\": [W_TARTAROS, W_TART, ETY_T, W_DORD],\n \"ref_check\": [\n   {\"ref\": \"KLN:1574\", \"status\": \"supports\", \"note\": \"Klein 1966 p. 1574 (KLN_1966.txt ll. 38247-38248, between the page markers 1572 and 1577): 'Tartarus, n., the abyss below Hades ... L., fr. Gk. Τάρταρος, prob. a word of imitative origin, suggestive of something frightful. Cp. tartar.' Klein is quoted correctly by Nourai; but Klein derives the chemical word from Greek, not from Arabic.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"p. 543, entries 'Tartar (1)' and 'Tartar (3)'\", \"stance\": \"contradicts\", \"note\": \"Skeat keeps the two words apart: 'Tartar (1), an acid salt in casks ... A term due to the alchemists; called tartre in Chaucer. — F. tartre ... Low L. tartarum. — Arab. durd, sediment, tartar of wine: durdiy' vs 'Tartar (3), Tartarus, hell ... L. Tartarus. — Gk. Τάρταρος, the infernal regions; conceived as a place of extreme cold; cf. Gk. ταρταρίζειν, to shiver with cold.' So SKT:543 does NOT support making the mythological word the source of the chemical one.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/tartar\", \"stance\": \"contradicts\", \"note\": \"'from Medieval Latin tartarum, from late Greek tartaron \\\"tartar encrusting the sides of wine casks\\\" ... perhaps of Semitic origin, but Arabic is unlikely because of the early date of the word in Latin'; the mythological Tartarus is treated as a separate word.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/Τάρταρος\", \"stance\": \"partial\", \"note\": \"Gives only Strabo's derivation from Ταρτησσός and Klein's 'prob. word of imitative origin' — no support for a Semitic/Iranian origin of the mythological word.\"}\n ],\n \"nodes\": []\n}\n\nm = entry4[\"nodes\"].append\nm({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"dord «دُرد»\", \"verdict\": \"disputed\",\n \"derivation\": \"Persian دُرد dord 'lees, sediment in wine, vinegar or oil' is a genuine, well-attested word — Noushin's Shahnameh glossary has it with the very verse Nourai quotes — but it is not a descendant of Greek Tartaros. It is inherited Iranian: Proto-Iranian *dr̥ti- 'dung, refuse', from PIE *dʰṛ-to- < *dʰreyd- 'to have diarrhoea' (ESIJa II 356), which also gives English dirt and Old Norse dríta; the syllabic *r̥ yields Persian -or-/-ur-, whence dord, with the by-form دردی dordī. If anything the traffic goes the other way: Aramaic durdā and Arabic دُرْدِيّ durdiyy are listed by Wiktionary as Iranian borrowings, and it is through Arabic that the word reached Byzantine Greek τάρταρον and Latin tartarum. Extraction note: the JSON's Ferdowsī hemistich reads «از این آتشی جنگ بهر منست», but both the printed page and Noushin (FSF) have آشتی, 'out of this peace, war is my lot'.\",\n \"derivation_fa\": \"«دُرد» فارسی به معنی ته‌نشینِ شراب و سرکه و روغن واژه‌ای اصیل و پرگواه است ــ نوشین در «واژه‌نامک» همان بیتی را می‌آورد که نورایی نقل کرده ــ اما فرزندِ Τάρταρος یونانی نیست. این واژه ارثی و ایرانی است: از ایرانی آغازین *dr̥ti- «سرگین، پس‌مانده»، از هندواروپایی *dʰṛ-to- و ریشهٔ *dʰreyd- «اسهال داشتن» (فرهنگ ریشه‌شناختی زبان‌های ایرانی، ج۲ ص۳۵۶)، که dirt انگلیسی نیز از همان است؛ *r̥ هجایی در فارسی به -ur-/-or- بدل شده و «دُرد» و گونهٔ «دردی» را داده است. برعکسِ نمودار، آرامی durdā و عربی «دُردیّ» وام‌واژه‌های ایرانی‌اند و واژه از همین راه به یونانیِ بیزانسی τάρταρον و لاتینِ tartarum رسیده است. نکتهٔ خوانش: در استخراج، مصراع فردوسی «از این آتشی جنگ بهر منست» ثبت شده، حال آنکه چاپ کتاب و نوشین هر دو «از این آشتی جنگ بهر منست» دارند.\",\n \"sources\": [W_DORD, W_TART],\n \"ref_check\": [\n   {\"ref\": \"FSF:175\", \"status\": \"supports\", \"note\": \"Noushin, Vazhe-namak (FSF_pages.txt ll. 11477-11484): headword «درد (با پیش اول)» glossed «ته‌نشین شراب و سرکه و مانند آن», illustrated with «ازین آشتی جنگ بهر منست / همه نوش تو دُرد و زهر منست» — Nourai's word, gloss and quotation. The glossary gives no etymology, so it cannot support a Greek source.\"}\n ],\n \"consulted\": [\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/درد (Etymology 2)\", \"stance\": \"contradicts\", \"note\": \"'From Proto-Iranian *dr̥ti- (\\\"manure, feces\\\"), from PIE *dʰṛ-to-, from *dʰreyd- (\\\"to have diarrhea\\\"), whence also English dirt ... Compare the Iranian borrowings: Aramaic durdā ... Arabic دُرْدِيّ.'\"},\n   {\"src\": \"FSF\", \"where\": \"p. 175 s.v. درد\", \"stance\": \"supports\", \"note\": \"See the quotation above (word and Ferdowsī verse).\"},\n   {\"src\": \"HRN\", \"where\": \"grep 'durd|dord' HRN.txt = 0; HUB likewise\", \"stance\": \"silent\", \"note\": \"Neither Horn's Grundriss nor Hübschmann's Persische Studien has a number for dord.\"}\n ]\n})\nm({\n \"id\": 2, \"lang\": \"Arabic\", \"words\": \"durdi\", \"verdict\": \"disputed\",\n \"derivation\": \"Arabic دُرْدِيّ durdī 'lees, sediment (of oil or wine), amurca' is real and old, but it is a loan from Persian dord, not a descendant of Greek Tartaros. Addi Shir lists it among the Persian words Arabicised (AFM s.v. دردي, with تعريب), Wiktionary calls Arabic durdiyy and Aramaic durdā 'Iranian borrowings' of Persian dord, and Tobia al-Unaysi — Nourai's own TAD — puts durdī in his dictionary of foreign words in Arabic. Arabic gave the word the nisba ending -ī on the pattern of substance nouns. Nourai's arrow (Greek > Arabic) inverts the accepted direction and also crosses language families without a route.\",\n \"derivation_fa\": \"عربی «دُردیّ» به معنی ته‌نشینِ روغن و شراب واژه‌ای کهن و واقعی است، اما وام‌گرفته از فارسی «دُرد» است، نه فرزندِ Τάρταρος یونانی. ادّی شیر آن را در «الألفاظ الفارسیة المعرّبة» با نشانِ «تعریب» آورده، ویکی‌واژه عربی durdiyy و آرامی durdā را «وام‌واژه‌های ایرانی» می‌خواند، و طوبیا العنیسی (همان TAD که نورایی به آن ارجاع می‌دهد) نیز آن را در فرهنگ واژه‌های دخیل در عربی ثبت کرده است؛ پسوندِ نسبتِ «ـیّ» افزودهٔ عربی است. پس جهتِ پیکانِ نورایی وارونه است.\",\n \"sources\": [W_DORD, W_TART],\n \"ref_check\": [\n   {\"ref\": \"TAD:27\", \"status\": \"supports\", \"note\": \"Tobia al-Unaysi (TAD_pages.txt l. 1064): headword «دردي» glossed «وهو الراسب من الزيت ...» ('the sediment of oil'), listed as a dakhīl (foreign) word — which is Nourai's gloss 'sediment, an acid salt in casks'. TAD's inclusion of the word marks it as non-Arabic in origin, but says nothing about Greek.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AFM\", \"where\": \"Addi Shir s.v. (دُرْدِي) (AFM_pages.txt l. 1572)\", \"stance\": \"contradicts\", \"note\": \"'(درْدِي) ... ما يقع في اسفله من الكدر تعريب ...' — Addi Shir files durdī among Arabicised Persian words, i.e. Arabic < Persian, not < Greek.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/درد\", \"stance\": \"contradicts\", \"note\": \"Arabic دُرْدِيّ listed under 'the Iranian borrowings' from Persian dord.\"},\n   {\"src\": \"AFA\", \"where\": \"grep 'durd' AFA.txt = 0\", \"stance\": \"silent\", \"note\": \"Fraenkel does not treat durdī among the Aramaic loanwords in Arabic.\"}\n ]\n})\nm({\n \"id\": 3, \"lang\": \"Latin\", \"words\": \"tartarum\", \"verdict\": \"plausible\",\n \"derivation\": \"Medieval Latin tartarum 'potassium bitartrate, the crust deposited by wine in the cask' is certainly the source of the Romance and English words, and Nourai's chart follows the older etymology — Skeat, Devic, Funk & Wagnalls and today's Wiktionary all derive it ultimately from Arabic durdī (through Byzantine Greek τάρταρον, which Wiktionary makes the immediate Latin etymon). Two qualifications: (i) the immediate Latin etymon is the Byzantine Greek chemical word τάρταρον, not the mythological Τάρταρος, and Klein's story that it was 'so called by Paracelsus with regard to the burning effect' is anachronistic — Chaucer already has tartre c. 1390, over a century before Paracelsus, who only supplied the hellish rationalisation; (ii) Etymonline objects that 'Arabic is unlikely because of the early date of the word in Latin'. The node is therefore acceptable but not settled, and the chart's own NOTE (FSD:2468 & SKT:543 derive it from Arabic durdi) is a fair report of the split. EXTRACTION ERROR: on the printed page this Latin box branches from the root's spine, like the Persian and Arabic boxes; the JSON gives it parent #2 (Arabic).\",\n \"derivation_fa\": \"لاتینِ سده‌های میانه tartarum «دُردِ خمره، بی‌تارتراتِ پتاسیم» بی‌گمان سرچشمهٔ واژه‌های رومی و انگلیسی است و نمودارِ نورایی همان ریشه‌شناسی کهن‌تر را دنبال می‌کند: اسکیت، دویک، فانک‌واگنالز و ویکی‌واژهٔ امروزی همگی آن را در نهایت از عربی «دُردی» می‌گیرند، با واسطهٔ یونانیِ بیزانسی τάρταρον. دو نکته: نخست آنکه واسطهٔ بی‌میانجیِ لاتین همان واژهٔ شیمیاییِ بیزانسی است نه Τάρταρος اساطیری، و توضیح کلاین که «پاراسلسوس به سببِ اثرِ سوزانندگی چنین نامیدش» با تاریخ نمی‌خواند، زیرا چاسر نزدیک ۱۳۹۰م صورت tartre را به کار برده است، بیش از یک سده پیش از پاراسلسوس. دوم آنکه اتیمآنلاین وام‌گیری از عربی را به سببِ کهن‌بودنِ صورت لاتینی بعید می‌شمارد. پس این گره «با احتیاط پذیرفتنی» است.\",\n \"sources\": [W_TART, ETY_T],\n \"ref_check\": [\n   {\"ref\": \"KLN:1574\", \"status\": \"contradicts\", \"note\": \"Klein p. 1574 s.v. tartar: 'ME. tartre, tartar, fr. OF. tartre, fr. ML. tartarum, fr. Gk. Τάρταρος (see Tartarus); so called by Paracelsus with regard to the burning effect of this compound' — Klein derives the Latin word from Greek, NOT from Arabic durdī as Nourai's arrow does.\"},\n   {\"ref\": \"SKT:543\", \"status\": \"supports\", \"note\": \"Skeat p. 543: 'Tartar (1) ... F. tartre ... Low L. tartarum. — Arab. durd, sediment, tartar of wine: durdiy' — exactly the Arabic derivation, as Nourai's own NOTE says.\"}\n ],\n \"consulted\": [\n   {\"src\": \"FSD\", \"where\": \"vol. IV p. 2468 s.v. tartar (FSD_vol4.txt l. 30985)\", \"stance\": \"supports\", \"note\": \"'[< F tartre < LL tartarum < Ar durd, dregs]'.\"},\n   {\"src\": \"DEV\", \"where\": \"p. 218 s.v. Tartre (DEV.txt l. 2201)\", \"stance\": \"supports\", \"note\": \"'Tartre. Esp. portug. ital. tartaro, lat. des alchim. tartarum; de l'arabe-persan dourd, dourdi, sédiment, dépôt, lie de l'huile, lie du vin, tartre ... Le mot nous est venu par les alchimistes, ce qui explique son altération.'\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/tartar\", \"stance\": \"contradicts\", \"note\": \"'from late Greek tartaron \\\"tartar encrusting the sides of wine casks\\\" ... Arabic is unlikely because of the early date of the word in Latin.'\"},\n   {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/tartar\", \"stance\": \"supports\", \"note\": \"'From Old French tartre, from Medieval Latin tartarum, from Byzantine Greek τάρταρον, from Arabic دُرْدِيّ (durdiyy, \\\"dreg\\\"), from Persian درد (dord)' — Nourai's chain, with Byzantine Greek inserted.\"}\n ]\n})\nm({\n \"id\": 4, \"lang\": \"Arabic\", \"words\": \"tarteer\", \"verdict\": \"plausible\",\n \"derivation\": \"Modern Arabic طَرْطِير ṭarṭīr 'tartar, tartaric acid' is a 19th-20th c. chemical term taken back from the European (Latin/Italian/French) word, the Arabic script rendering the Romance t with emphatic ṭ as usual in scientific loans (cf. طرخون, طرطوفة). Tobia al-Unaysi lists it in his dictionary of foreign words and refers the reader to durdī — i.e. he recognises it as the same substance and, in effect, as the word that went out and came back. A genuine Arabic-internal derivation from the root ṭ-r-r is not available.\",\n \"derivation_fa\": \"«طَرطیر» در عربی نو اصطلاحی شیمیایی از سدهٔ نوزدهم و بیستم است که از صورتِ اروپایی (لاتینی/ایتالیایی/فرانسوی) بازپس گرفته شده و «ت» رومی در آن مانند دیگر وام‌واژه‌های علمی با «ط» نوشته شده است (قس طرخون، طرطوفه). طوبیا العنیسی آن را در فرهنگ واژه‌های دخیل آورده و خواننده را به «دردی» ارجاع می‌دهد، یعنی آن را همان مادّه و در واقع همان واژهٔ رفته‌وبازگشته می‌شناسد. اشتقاق درون‌عربی از ریشهٔ «ط‌ر‌ر» ممکن نیست. پس ادعای نورایی پذیرفتنی است.\",\n \"sources\": [W_TART],\n \"ref_check\": [\n   {\"ref\": \"TAD:46\", \"status\": \"supports\", \"note\": \"Tobia al-Unaysi (TAD_pages.txt l. 1770): «طرطير ... راجع دردي» — 'ṭarṭīr ... see durdī', i.e. the loanword is registered and tied to durdī, as Nourai's chart has it.\"}\n ],\n \"consulted\": [\n   {\"src\": \"TAD\", \"where\": \"s.v. طرطير\", \"stance\": \"supports\", \"note\": \"See quotation above.\"},\n   {\"src\": \"AFM\", \"where\": \"grep 'طرطير' AFM_pages.txt = 0\", \"stance\": \"silent\", \"note\": \"Addi Shir (1908) does not list ṭarṭīr — expected, since it is a European chemical term, not an old Persian loan.\"}\n ]\n})\nm({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"tartîr «طرطیر ، ترتیر»\", \"verdict\": \"plausible\",\n \"derivation\": \"Persian طرطیر / ترتیر ṭarṭīr 'tartar, tartaric acid' is the same modern chemical term, reaching Persian through Arabic-mediated scientific vocabulary in the Qajar period (the spelling with ط is the give-away of the Arabic route; the simplified ترتیر reflects the Persian pronunciation, since ط and ت are homophonous in Persian). Mo'in's dictionary uses the compound اسید طرطیر 'tartaric acid' in defining mineral waters, which shows the term established in Persian lexicography. So this is a Persian → Arabic → Europe → Arabic → Persian round trip of the original dord.\",\n \"derivation_fa\": \"«طرطیر / ترتیر» در فارسی همان اصطلاح شیمیاییِ نو است که در دورهٔ قاجار از راهِ واژگان علمیِ عربی به فارسی رسیده است؛ نگارش با «ط» نشانهٔ همین واسطهٔ عربی است و صورت سادهٔ «ترتیر» بازتابِ تلفظ فارسی است، چون «ط» و «ت» در فارسی هم‌آوایند. معین در تعریف آب معدنی ترکیبِ «اسید طرطیر» را به کار برده است که نشان می‌دهد این اصطلاح در فرهنگ‌نویسی فارسی جا افتاده است. بدین‌سان واژهٔ «دُرد» سفری رفت‌وبرگشتی داشته است: فارسی ← عربی ← اروپا ← عربی ← فارسی.\",\n \"sources\": [W_TART],\n \"ref_check\": [\n   {\"ref\": \"MON:2221\", \"status\": \"partial\", \"note\": \"Mo'in's page 2221 (vol. 2, letter ط) is not reachable in the local two-volume Adena reprint, which has its own pagination; but Mo'in's text does use the term: MON_part1.txt l. 1149 (s.v. آب معدنی) 'بی‌کربنات سود و اسید طرطیر کنند و مانند گوارشی بیاشامند'. The word is thus in Mo'in, as Nourai claims; the exact page could not be confirmed.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt l. 1149 (s.v. آب معدنی)\", \"stance\": \"supports\", \"note\": \"«اسید طرطیر» used in Mo'in's own definition — the Persian chemical term is attested.\"},\n   {\"src\": \"TAD\", \"where\": \"s.v. طرطير\", \"stance\": \"supports\", \"note\": \"The Arabic intermediary from which the Persian spelling with ط is taken.\"}\n ]\n})\nm({\n \"id\": 6, \"lang\": \"French\", \"words\": \"tartre\", \"verdict\": \"confirmed\",\n \"derivation\": \"French tartre 'tartar of wine, later dental calculus' is the regular Old French treatment of Medieval Latin tartarum: loss of the unstressed medial syllable and of the final -um gives tart(a)r- > tartre, with the usual French epenthetic -re for a final consonant group (cf. ML *cancrum > chancre). It is attested from the 14th c. in the language of the alchemists and apothecaries and is the direct source of English tartar; Devic's Dictionnaire étymologique des mots français d'origine orientale treats it at p. 218.\",\n \"derivation_fa\": \"فرانسوی tartre «دُردِ شراب» و سپس «جرمِ دندان» برآیندِ منظمِ tartarum لاتینِ میانه است: هجای میانیِ بی‌تکیه و پایانهٔ -um می‌افتد و خوشهٔ پایانی، مانندِ chancre از cancrum، با «ـre» تلفظ‌پذیر می‌شود. این واژه از سدهٔ چهاردهم میلادی در زبان کیمیاگران و داروسازان گواهی شده و سرچشمهٔ بی‌واسطهٔ tartar انگلیسی است؛ دویک در ص ۲۱۸ فرهنگ خود آن را آورده است. ادعای نورایی درست است.\",\n \"sources\": [ETY_T, W_TART],\n \"ref_check\": [\n   {\"ref\": \"AHD:1317\", \"status\": \"not_checked\", \"note\": \"The main lexicon of the 1975 American Heritage Dictionary is not available locally (only Watkins' IE appendix, which has no 'tartar'); p. 1317 would be the AHD entry for tartar.\"},\n   {\"ref\": \"DEV:218\", \"status\": \"supports\", \"note\": \"Devic p. 218 s.v. Tartre (DEV.txt l. 2201): 'Tartre. Esp. portug. ital. tartaro, lat. des alchim. tartarum; de l'arabe-persan dourd, dourdi ...' — the French word from ML tartarum.\"}\n ],\n \"consulted\": [\n   {\"src\": \"DEV\", \"where\": \"p. 218\", \"stance\": \"supports\", \"note\": \"See quotation above.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/tartar\", \"stance\": \"supports\", \"note\": \"'from Old French tartre, from Medieval Latin tartarum'.\"},\n   {\"src\": \"KLN\", \"where\": \"p. 1574 s.v. tartar\", \"stance\": \"supports\", \"note\": \"'ME. tartre, tartar, fr. OF. tartre, fr. ML. tartarum' — the French link is uncontested.\"}\n ]\n})\nm({\n \"id\": 7, \"lang\": \"English\", \"words\": \"tartar\", \"verdict\": \"confirmed\",\n \"derivation\": \"English tartar, first as tartre (Chaucer, Canon's Yeoman's Tale, c. 1390, among the alchemists' materials), is borrowed from Old French tartre; the modern spelling tartar is a Latinising respelling after ML tartarum and was helped by confusion with Tartar 'Tatar'. Sense 1 is the bitartrate of potash deposited by wine (whence cream of tartar, tartaric acid); the dental sense, 'a hard deposit on the teeth', is first recorded 1806 and is a transferred use of the same crust. Nourai's word, gloss and the French source are all correct.\",\n \"derivation_fa\": \"انگلیسی tartar نخست به صورت tartre نزد چاسر (نزدیک ۱۳۹۰م، در «حکایت خدمتکار کشیش کیمیاگر») در فهرست مواد کیمیاگران دیده می‌شود و وام‌گرفته از tartre فرانسوی است؛ املای امروزی با -ar بازنویسیِ لاتینی‌مآبانه بر پایهٔ tartarum است و آمیختگی با Tartar «تاتار» نیز در آن بی‌تأثیر نبوده است. معنای نخست همان بی‌تارتراتِ پتاسیمِ ته‌نشستهٔ شراب است (و از همین‌جا cream of tartar و اسید تارتاریک) و معنای «جرمِ دندان» از ۱۸۰۶م به بعد، کاربردی مجازی از همان پوسته است. واژه، معنا و خاستگاه فرانسویِ آن در نمودار درست است.\",\n \"sources\": [ETY_T, W_TART],\n \"ref_check\": [\n   {\"ref\": \"AHD:1317\", \"status\": \"not_checked\", \"note\": \"AHD's main lexicon is not available locally (only the Watkins IE appendix).\"},\n   {\"ref\": \"SKT:543\", \"status\": \"supports\", \"note\": \"Skeat p. 543: 'Tartar (1), an acid salt in casks ... A term due to the alchemists; called tartre in Chaucer. — F. tartre ... Low L. tartarum.'\"},\n   {\"ref\": \"FSD:2468\", \"status\": \"supports\", \"note\": \"Funk & Wagnalls vol. IV (FSD_vol4.txt l. 30985): 'tartar ... 1. The roughly purified crust of argol ... 2. A yellowish incrustation that forms on the teeth, consisting chiefly of calcium phosphate. [< F tartre < LL tartarum < Ar durd, dregs]' — Nourai's gloss verbatim.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"p. 543\", \"stance\": \"supports\", \"note\": \"See quotation above.\"},\n   {\"src\": \"FSD\", \"where\": \"vol. IV p. 2468\", \"stance\": \"supports\", \"note\": \"See quotation above.\"},\n   {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/tartar\", \"stance\": \"supports\", \"note\": \"'Late 14c., \\\"bitartrate of potash\\\" ... By 1806, the term specifically referred to dental encrustation.'\"}\n ]\n})\n\ndoc = {\n \"pdf_page\": 496,\n \"book_page\": 466,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [entry0, entry4]\n}\nopen(\"/home/sfmqrb/git/rishe/data/verification/page-496.json\",\"w\",encoding=\"utf-8\").write(json.dumps(doc, ensure_ascii=False, indent=2)+\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build496.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-496.json > /dev/null && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 496"
}
```


### [2026-09-14T03:23:13.220Z] TOOL RESULT

```
ok
nodes verified: 17/17
node verdicts: {'plausible': 7, 'confirmed': 7, 'transcription_suspect': 1, 'disputed': 2}
root verdicts: {'disputed': 2}
ref checks: {'supports': 17, 'not_checked': 4, 'partial': 3, 'contradicts': 1}
books consulted: {'supports': 29, 'silent': 7, 'partial': 10, 'contradicts': 4} | by book: {'Wiktionary': 11, 'KLN': 4, 'AFA': 4, 'DEV': 4, 'LKT': 3, 'AFM': 3, 'Etymonline': 3, 'SOD': 2, 'HRN': 2, 'FVQ': 2, 'FSD': 2, 'TAD': 2, 'BRT': 1, 'PHD': 1, 'NYB': 1, 'BQT': 1, 'LAM': 1, 'FSF': 1, 'MON': 1, 'SKT': 1}
```


## [2026-09-14T03:23:28.848Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-496.json` written, `verify_check.py 496` shows 17/17 nodes, 0 PROBLEM lines.

**Page 496 (book 466) — 2 real entries (4 redirects skipped)**
- Node verdicts: 7 confirmed, 7 plausible, 2 disputed, 1 transcription_suspect. Root verdicts: 2 disputed.
- Ref checks: 17 supports, 3 partial, 1 contradicts, 4 not_checked (MPP:88, AHD:1317 ×2, MON:2221 partial).

**Disputed / flagged**
- ROOT *Tanŭr, Tannŭr* — labelled "Indo-European"; no such PIE root (Pokorny silent, Watkins puts "oven" under *aukʷ-). It is a Near-Eastern culture word: Akkadian tinūru → Aram./Heb./Arab. and, as Bartholomae says expressly ("LW. aus dem sem.", AiW 638), a loan into Avestan. Tree itself sound.
- ROOT *Tartaros* — two different Greek words conflated: Τάρταρος "underworld" (Pre-Greek per Beekes; Klein's "imitative origin" is antiquarian) vs Byz. Gk. τάρταρον "cask deposit". Arrows also run backwards.
- #1 Persian dord «دُرد» — real word but inherited Iranian (*dr̥ti- < PIE *dʰreyd-, cognate of *dirt*), not from Greek; it is the source of the European word, not its descendant.
- #2 Arabic durdī — a loan from Persian dord (Addi Shir "تعریب"; Wiktionary), not from Greek.
- #10 Akkadian **tinnŭra** — transcription_suspect, `error_in: book`: the page (checked, PNG copied to `data/verification/sources/refs/ocr/BOOK/496.png`) does print "tinnŭra"; the Akkadian is tinūru (Klein "tinnuru", Jeffery "tinuru") — Nourai blended it with Aramaic tannūrā.

**Extraction errors for the owner to fix (`data/extracted/batch/page-496.json`)**
- Entry 4, node #3 (Latin *tartarum*): `parent` should be **0** (it branches off the root's spine on the printed page), not 2.
- Entry 4, node #1 quote: book prints «از این **آشتی** جنگ بهر منست» (matches Noushin FSF p.175); JSON has «آتشی».
