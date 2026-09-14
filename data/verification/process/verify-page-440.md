# Verification process log — verify-page-440


## [2026-09-14T01:55:42.991Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 440 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-440.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-440.json. Write /home/sfmqrb/git/rishe/data/verification/page-440.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 440` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:55:43.939Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:55:44.722Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:55:44.739Z] TOOL RESULT

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


## [2026-09-14T01:55:45.225Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-440.txt"
}
```


### [2026-09-14T01:55:45.246Z] TOOL RESULT

```
1	=== PDF page 440 (book page 410) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Sekw : to follow  (refs POK:896)
4	#1 (parent #0) [Avestan] refs=ZAW:38,242; POK:896 | haša-kerta, aša-gerd : follower ☞Kwer ; haxay, haši : follower, companion, friend ; haxa-maniš : friendly mannered ☞Men 1
5	  #2 (parent #1) [Persian] refs=MON:1999; BQT:2316 | šâgerd «شاگرد» : student, "follower" ; Haxâmaneš «هخامنش» : "with friendly thoughts and manners"
6	#3 (parent #0) [Avestan] refs=POK:896 | hačâ : followed from ; hačâ-adairi : from under ☞En
7	  #4 (parent #3) [Pahlavi] refs=HRN:12,150 | aj : from ; azěr : from under, under
8	    #5 (parent #4) [Persian] refs=BQT:113,1051 | az «از» : from ; zîr «زیر» : under
9	#6 (parent #0) [Old Persian] refs=KNT:212 | hačâ : follow, from ; haxâ : friend ; haxâ-maniš : with friendly manners ☞Men 1
10	#7 (parent #0) [Latin] refs=AHD | signum : sign, mark ; sigillatus : a record
11	  #8 (parent #7) [Arabic] refs=AHD:1159 | siqillât : with little images ; sejell : a sealed record
12	    #9 (parent #8) [Persian] refs=AHD:1159; ARK:221 | saqarlât «سقرلات» : a type of cloth ; sejel «سجلّ» : a record
13	      #10 (parent #9) [Latin] refs=AHD:1159 | scarlatum : a purple cloth
14	        #11 (parent #10) [English] refs=None | scarlet
15	  #12 (parent #7) [English] refs=AHD | seal, sign, resign, assign
16	    #13 (parent #12) [French] refs=None | assignat : assigned bonds
17	      #14 (parent #13) [Russian] refs=DMO:220 | assignatsia : money bill
18	        #15 (parent #14) [Persian] refs=DMO:220; ARK:239 | eskenâs «اسکناس» : money bill
19	#16 (parent #0) [Latin] refs=AHD | socius : companion ; sequi : to follow ; secondus : coming next
20	  #17 (parent #16) [English] refs=AHD | society, association ; pursue, sequence, execute ; second
21	
```


## [2026-09-14T01:55:48.254Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-440.json | head -200",
 "description": "Read source JSON for page 440"
}
```


## [2026-09-14T01:55:48.953Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:55:49.433Z] TOOL RESULT

```
{
    "pdf_page": 440,
    "book_page": 410,
    "entries": [
        {
            "root": {
                "name": "Sekw",
                "lang": "Indo-European",
                "refs": "POK:896",
                "gloss": "to follow"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "ZAW:38,242; POK:896",
                    "words": [
                        {
                            "translit": "ha\u0161a-kerta, a\u0161a-gerd",
                            "gloss": "follower",
                            "script": null,
                            "see": [
                                "Kwer"
                            ]
                        },
                        {
                            "translit": "haxay, ha\u0161i",
                            "gloss": "follower, companion, friend",
                            "script": null
                        },
                        {
                            "translit": "haxa-mani\u0161",
                            "gloss": "friendly mannered",
                            "script": null,
                            "see": [
                                "Men 1"
                            ]
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
                    "refs": "MON:1999; BQT:2316",
                    "words": [
                        {
                            "translit": "\u0161\u00e2gerd",
                            "gloss": "student, \"follower\"",
                            "script": "\u0634\u0627\u06af\u0631\u062f"
                        },
                        {
                            "translit": "Hax\u00e2mane\u0161",
                            "gloss": "\"with friendly thoughts and manners\"",
                            "script": "\u0647\u062e\u0627\u0645\u0646\u0634"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:896",
                    "words": [
                        {
                            "translit": "ha\u010d\u00e2",
                            "gloss": "followed from",
                            "script": null
                        },
                        {
                            "translit": "ha\u010d\u00e2-adairi",
                            "gloss": "from under",
                            "script": null,
                            "see": [
                                "En"
                            ]
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "Pahlavi",
                    "refs": "HRN:12,150",
                    "words": [
                        {
                            "translit": "aj",
                            "gloss": "from",
                            "script": null
                        },
                        {
                            "translit": "az\u011br",
                            "gloss": "from under, under",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "Persian",
                    "refs": "BQT:113,1051",
                    "words": [
                        {
                            "translit": "az",
                            "gloss": "from",
                            "script": "\u0627\u0632"
                        },
                        {
                            "translit": "z\u00eer",
                            "gloss": "under",
                            "script": "\u0632\u06cc\u0631"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 0,
                    "lang": "Old Persian",
                    "refs": "KNT:212",
                    "words": [
                        {
                            "translit": "ha\u010d\u00e2",
                            "gloss": "follow, from",
                            "script": null
                        },
                        {
                            "translit": "hax\u00e2",
                            "gloss": "friend",
                            "script": null
                        },
                        {
                            "translit": "hax\u00e2-mani\u0161",
                            "gloss": "with friendly manners",
                            "script": null,
                            "see": [
                                "Men 1"
                            ]
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "signum",
                            "gloss": "sign, mark",
                            "script": null
                        },
                        {
                            "translit": "sigillatus",
                            "gloss": "a record",
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
                    "refs": "AHD:1159",
                    "words": [
                        {
                            "translit": "siqill\u00e2t",
                            "gloss": "with little images",
                            "script": null
                        },
                        {
                            "translit": "sejell",
                            "gloss": "a sealed record",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
```


### [2026-09-14T01:55:49.475Z] TOOL RESULT

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


## [2026-09-14T01:56:00.496Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-440.json | sed -n '200,400p'",
 "description": "Rest of source JSON"
}
```


### [2026-09-14T01:56:01.639Z] TOOL RESULT

```
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 8,
                    "lang": "Persian",
                    "refs": "AHD:1159; ARK:221",
                    "words": [
                        {
                            "translit": "saqarl\u00e2t",
                            "gloss": "a type of cloth",
                            "script": "\u0633\u0642\u0631\u0644\u0627\u062a"
                        },
                        {
                            "translit": "sejel",
                            "gloss": "a record",
                            "script": "\u0633\u062c\u0644\u0651"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": {
                        "text": "\u063a\u06cc\u0631 \u062d\u0631\u0641 \u0648 \u063a\u06cc\u0631 \u0627\u06cc\u0645\u0627 \u0648 \u0633\u062c\u0644\u0651 - \u0635\u062f \u0647\u0632\u0627\u0631\u0627\u0646 \u062a\u0631\u062c\u0645\u0627\u0646 \u062e\u06cc\u0632\u062f \u0632 \u062f\u0644",
                        "poet": "Molav\u00ee"
                    }
                },
                {
                    "id": 10,
                    "parent": 9,
                    "lang": "Latin",
                    "refs": "AHD:1159",
                    "words": [
                        {
                            "translit": "scarlatum",
                            "gloss": "a purple cloth",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 10,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "scarlet",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 12,
                    "parent": 7,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "seal, sign, resign, assign",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 13,
                    "parent": 12,
                    "lang": "French",
                    "refs": null,
                    "words": [
                        {
                            "translit": "assignat",
                            "gloss": "assigned bonds",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 14,
                    "parent": 13,
                    "lang": "Russian",
                    "refs": "DMO:220",
                    "words": [
                        {
                            "translit": "assignatsia",
                            "gloss": "money bill",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 15,
                    "parent": 14,
                    "lang": "Persian",
                    "refs": "DMO:220; ARK:239",
                    "words": [
                        {
                            "translit": "esken\u00e2s",
                            "gloss": "money bill",
                            "script": "\u0627\u0633\u06a9\u0646\u0627\u0633"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 16,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "socius",
                            "gloss": "companion",
                            "script": null
                        },
                        {
                            "translit": "sequi",
                            "gloss": "to follow",
                            "script": null
                        },
                        {
                            "translit": "secondus",
                            "gloss": "coming next",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 17,
                    "parent": 16,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "society, association",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "pursue, sequence, execute",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "second",
                            "gloss": null,
                            "script": null
                        }
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


## [2026-09-14T01:56:02.151Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['POK','ZAW','MON','BQT','HRN','KNT','AHD','ARK','DMO']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600]); print()\n\"",
 "description": "Look up refs metadata"
}
```


### [2026-09-14T01:56:03.313Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

ZAW {"title": "C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 1906", "edition_found": "1906 - Google Books record only", "kind": "google_books", "url": "https://books.google.com/books?id=agDP0HdEssEC (full view; PDF downloaded) ; also 8q0zAQAAMAAJ (full view) ; HathiTrust coo.31924026891675 (pdus)", "identifier": "agDP0HdEssEC", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt"], "p

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

ARK {"title": "M.H. Rokn-zadeh Adamiyyat, Arkan-e Sokhan, Sharq 1347/1968", "kind": "catalog", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}

DMO {"title": "Sa'id Nafisi, Dar Maktab-e Ostad, Zohreh 1344/1965", "kind": "website", "url": "https://www.ketabnak.com/book/55983 (283 pp. PDF, login)", "lookup_hint": "Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF page exists; not fetched."}
```


## [2026-09-14T01:56:08.850Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['POK']['page_offset'])\nprint(d['ZAW'].get('page_offset'))\nprint(d['BQT']['page_offset'])\nprint(d['KNT']['page_offset'])\nprint(d['MON'].get('page_offset'))\n\""
}
```


## [2026-09-14T01:56:09.735Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"sek[uʷ]\" POK_full.txt | head -40"
}
```


### [2026-09-14T01:56:10.053Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
ZAW_pages.txt: 306 leaves; printed = leaf(1-based) − 24 (leaf 60 = p.36; leaf 20 = p.X).
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
None
```


### [2026-09-14T01:56:10.111Z] TOOL RESULT

```
72926:Lithuanian seku, sekti, Latvian seku, se/r/"follow; feel, scent', Lithuanian at-sektas {see 
72982:Lithuanian seku, sekt/ "narrare' (= (£v)£n(jo, inseque), sek/mas'6as Erzahlen', sekmet ' 
78030:slanka, Latvian s/^o/ra (sekundarere-stem Old Prussian slanke, Litliuanian slanke), proto 
83453:also Latin sTbilo, -are "hiss, wliistie', 5/M^s "ziscliend; das Zisclien', sekundar sTfilo,
```


## [2026-09-14T01:56:12.953Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '72880,73010p' POK_full.txt"
}
```


### [2026-09-14T01:56:13.024Z] TOOL RESULT

```
"zugleich' (: Latvian secf?); Old Indie saca{m. Lok.) 'together with, by, angesiehts from', 

Avestan haca, ap. hacalort from, from - from' (Instr. eines *sek"o-s 'folgend'); zero grade 

Old Indie askra- ( *a-sk-ra-) ' combined ', as Avestan ask/t/t, ' association ' (full grade 

haciti- ' accompaniment '); 

because of Aryan A/? dubious: Old Indie sakha {sakhi-) ' fellow, comrade, friend', 
Avestan haxay- {hasi-) ds., ap. Haxamanis-^ 'Axai|j£vr|^'; 

gr. £TTO|jai ' follow ', Aor. £an6|jr|v (redupl., compare Old Indie sascati) and an£a9ai, 
a-n6\xzyoc„ £TTi-onou; due to eines *sok'^io-s (= Latin socius. Old Icelandic seggi): aoaoEw 
'help, stand by ' {*sm-sokzieid), aooor|Tnp 'Gehilfe'; participle *£nT6(; as base from aouv- 
£TTTC(-o9ai ouvaKoAouGnaai Hes.; 

maybe alb. {*sok'^ shokum. shoqe\. 'friend' 

ablaut, onaojv ' fellow ', ona^u) ' allow to follow ', 6na56c;, Ionian 6nr|56q ' Begleiter ' 
(*so(7"'a' das Folgen, Gefolgsehaft '); 

Latin sequor, -/"nachfolgen, begleiten, pursue ', participle secutus {afier solutus, 
volutus, for older *sectos= gr. *£nT6(;, Lithuanian 5/-5e/r/55 'aufgespiJrt, aufgefunden'); Tn- 
sequor' pursue' (: Old Indie a/7^-S5C-'nachgehen'); compare sector, -arf eager begleiten', 



sectaf. "Richtlinie, party, philosophische Schule'; 5ec^/7o'^s (participle Praes.) "tlie 
following, second '\sequester, -tra, -trum, newer -tris, -//'e'(*mitfolgend =) vermitteind, 
Mittelsperson' (from a n. es^stem -se/ri/cs derive ); secus{\N\Vc\ Akk.) "dense after, 
nebenbei, gemaft', solidified Norn. Sg. m. eines "se/r^f-s 'folgend' (compare o. Old Indie 
saca); to sec^s 'after, less good' (from 'folgend, zurijckstehend') trat ein jijngerer 
compounds sequius, soc/^s "teilnehmend, Gesellschafter, Teilnehmer, Bundesgenosse'; 

maybe alb. {*sek"'o-) shkoj^ go, follow', shko-ze^ beech, (*walking tree)' [-zealb. 
diminutive suffix] similar to alb. bredh^ fir-tree, spruce', bredh^ wander, (walking tree)', 
{*sok'^ shoku "friend, follower'. 

Old Irish sechithir{= Latin sequitui) "folgf, sechem'6as Folgen', sec/? (with Akk.) "vorbei 
an, about - out, namely', cymr. bret. /7e/0 'without' (compare Old Indie saca, Avestan haca, 
Latin secus); 

Old High German /?e'/>7se'^^5"pedisequa'. Old Saxon segg. Old English sec^. Old 
Icelandic se^^^'Gefolgsmann, journeyman, man' {*sok"ios)\ 

Lithuanian seku, sekti, Latvian seku, se/r/"follow; feel, scent', Lithuanian at-sektas {see 
above), sekmei. "Erfolg', Latvian (veraltet) secen, sec{xr\. Akk.) "vorbei, langshin', 
(perhaps from *sekenq, *seki= Old Indie saci). 

References: WP. II 476 f., WH. II 506, 518, 519 f., Trautmann 254 f. 
Page(s): 896-897 

Root / lemma: sek''-2 

Meaning: to see, show; to speak 

Note: identical with sek^-L 

Material: Gr. svsnoj, svvsnw (-vv- verbalized the metr. lengthening) 'sage an, erzahle' 

(Imp. £vv£n£, Impf. svvsns. Put. svi-annau) {*sk"'-e-), Aor. svi-ansTv, Imp. £vi-an£(;, svi- 

an£(;, 2. PI. sansTsfrom *£v-an£T£), aan£TO(; 'unsaglich; unsagbar groft, eternal, infinite ', 

np6a-£iiJiq npoaaY6p£uai(; Hes. (: Latin insectio), 9£an£aioq ' wonderful, divine' (originally 

"from the divinity geoffenbart'), from *-aTT£-TiO(;; Geghk;, Qza-n\oc, ' seer, Weissager' 

probably VerkiJrzung from Gsansaioc;; Gsani^u) "weissage'; aana^opai "greet' (a- from n 

"in'); aanaaiO(; " welcome, desirable, worth having, welcome, wanted, pleases ' (*/>ana- 

GioO; 

Latin Ihseque^sag an' (= gr. swehe), also Tnsece, cverschlepptfrom forms as: 
//75ec//o/7es"narrationes', //7sex//"dixerit'; inquam, inquis, -//"sage I, sagst du, he says ' 



(//7^i/a/77 Konjunktivform *en-sk"'am ' mocht' I say'; //7^i///originally themat. Aorist *en-sk"'e-t 
as £vi-an£Tv); 

Umbrian /7/'i/s//ri//'e/7/"pronuntiaverint', sukatu^6ec\a'CdXb, pronuntiato'; A" instead of p 
after forms with labialization of *k"'vor s, t, 

acymr. hepp, mcymr. heby{r), cymr. eb(e), ebr^ saqie' , mcymr. ^e-it*^ "speak", go-hebu 
"antworten', cymr. "entsprechen', mcymr. gwrtheb^ reaction ', cymr. " objection ', corn. 
^OAde/y'antworten'; mcymr. dihaereb^ proverb, saying ' {*de-ad-pro-sk"o-). Old Irish 
arose 6s. {*ad-pro-sk"'o-)\ Middle Irish /'osc'dithyrambische poem ' {*pro-sk"'o-)\ Old Irish 
in-coissig{*ind-com-sech-\xov(\ *sek"-) " identified ', /asc 'announcement' {*to-ad-sk"o-), 
ecosc "apparition' {*en-kom-sk"o-)\ mcymr. atteb, ncymr. 5/e/? "Antwort' {*at/-sek"'-), Old 
Irish a/fbescn. 'Antwort' {*ati-sku-om), con-secha ^ zuc\\Wg\! , cose' punishment ' = cymr. 
coS/Ods. {*kom-sk"o-m). Old Irish d/uscb/ 'weckt' {*di-uss-sechi). Old Irish insce' discourse 
' {*eni-sku-Ja), also Old Irish sce/n. ' narration ' {*sk"etlo-n, from which borrowed cymr. 
cbwed/ etc.); Middle Irish scotbt 'word'; 

Old High German sagen 'say' {*sok"e-), besides Germanic *sagid< *sajmd\n Old 
Saxon seggian, mnl. segghen. Old English secgan {ex\q\. say), Old Icelandic segja ds., 
abstract noun Old Icelandic Old High German S5^5 'declaration, narration ' (Modern High 
German Sage), Old English sagui. ds.; 

Lithuanian seku, sekt/ "narrare' (= (£v)£n(jo, inseque), sek/mas'6as Erzahlen', sekmet ' 
narration. Sage', sakau, sakyti'say', pasaka' Waxcheu' etc.; 

Old Church Slavic socitr indicate ', so/rb 'Anzeiger, Anklager', poln. osoka' accusation, 
slander' etc.; 

older meaning selc-see' and 'show' (see previously above Irish in-coissig, tasc, 
auch con-secha, cose as Latin animadvertere a\so ' reprove ') in: Old Irish rosem. 'eye, 
look' {*pro-sk"'o-)\ 

Gothic sa/h>an ' see' , Old Icelandic ^afrom sea, Old English seen. Old Saxon Old High 
German sehan. Modern High German sehen; Gothic s/unslace, eyesight'. Old Icelandic 
syn, sjont 'vision, sight, apparition'. Old English s/en. Old Saxon s/Z//? 'sight, vision, eye' 
from *se(g)wnr. Adj. Gothic anasiuns. Old English gesTene, Old Icelandic sj?/?/? 'visible, 
obvious, clear', sj?/7as/'shine, appear, seem' (= ' appear'); Old High German (gijsihV^e 
looking, face, sight'. Old English gesiht6s.; 

Maybe alb. syu, syn/' eye ' 



besides from lengthened grade *se(g)wni-: 0\6 High German selt-sani, Middle High 
German se//-5^/7e "seldom' se//sa/77 'strange ' (but Old English seldsTene^ rare ' from - 
*sa(g)wni-)\ 

Hittite sakuua-n. PI. "eyes', sakuua/'-'see'; Tocharian A sotre, B sotri'mark, token, sign' 
{*sek"'-tr-). 

From PIE this root passed to Altaic languages:
```


## [2026-09-14T01:56:20.063Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '72855,72885p' POK_full.txt; echo ====; grep -n \"signum\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T01:56:20.132Z] TOOL RESULT

```
Exit code 1

Yukaghir parallels: coyu ' shallow ', cogunn'e- 'be shallow (of a river)' 

Albanian cek^ touch', ceketB6\. " shallow ', cak^ border, line'. 

References: WP. II 473 f., Trautmann 256 f., Kuiper Indo Germanic Nasalpras. 185 f. 
Page(s): 894-895 

Root / lemma: selc-1 

Meaning: to follow 

Grammatical information: mostly medial 

Note: as Terminus the jargon spoken by hunters originally eins with sek''-2, s. Wissmann 

in: Das Institutf. deutsche language under Literatur 1954, 142. 

Material: Old Indie sacate^beq\e\\.e\, folgt', sacati, sfsakti, 3. PI. sascati{\ £on6|jr|v Aor.) 

ds., Avestan hacaite, hacaiti^s.. Old Indie sakman-, Avestan haxman-n. ' escort, 

companionship'; Old Indie sakam{m. Instr.) "in Gemeinschaft with, nebst'; Avestan hakal 

Adv. 'to same time' (solidified Nom. Sg. n. of participle, *sek"nt)\ Old Indie sac/A6v. 

"zugleich' (: Latvian secf?); Old Indie saca{m. Lok.) 'together with, by, angesiehts from', 

Avestan haca, ap. hacalort from, from - from' (Instr. eines *sek"o-s 'folgend'); zero grade 

Old Indie askra- ( *a-sk-ra-) ' combined ', as Avestan ask/t/t, ' association ' (full grade 
(eval):1: === not found
```


## [2026-09-14T01:56:20.718Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"sekw-\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-14T01:56:20.787Z] TOOL RESULT

```
914:sécula, sickle: SICKLE. 8. Suffixed variant form *sak-so- in Latin saxum, stone (< “broken-off piece”): SAXATILE; SAXICOLOUS, SAXIFRAGE. See also extended roots sked-, skei-, sker-', sker-4. [Pok. 2. sék- 895, sken-(d)- 929.] s@k-. Slack, calm: relax. Greek (h)éka, slowly, a little (> héss6n, inferior): ESSONITE. [Pok. 3. sék- 896.] sekw-1, To follow. 1. Latin sequi, to follow: SECT, SEGUE, SEGUIDILLA, SEQUACIOUS, SEQUEL, SEQUENCE, SUE, SUITOR; CONSEQUENT, ENSUE, EXECUTE, OBSEQUIOUS, PERSECUTE, PROSECUTE, (PURSUE), SUBSEQUENT. 2. Latin sequester, “follower,” mediator, depositary: SEQUESTER, SEQUESTRUM. 8. Suffixed (participial) form *sekv-ondo- in Latin secundus, following, coming next, second: SECOND2, SECONDO, SECUND, SECUNDINES. 4. Suffixed form *sekv-os, following, in Latin secus, along, alongside of: INTRINSIC. 5. Suffixed form *sekv-no- in Latin signum, identifying mark, sign (< “standard that one follows”): SEAL!, SEGNO, SIGN; AS- SIGN, CONSIGN, DESIGNATE, INSIGNIA, RESIGN. 6. Suf- fixed o-grade form *sok’-yo- in Latin socius, ally, companion (< “follower”): SOCIABLE, SOCIAL, SOCIETY, SOCIO-; ASSOCIATE, CONSOCIATE, DISSOCIATE. [Pok. 1. seky- 896.] sekw-2, To perceive, see. 1. Germanic *sehwan, to see, in Old English séon, to see: SEE}. 2. Germanic abstract noun *sih-tiz in Old English sihth, gesiht, vision, specta- cle: SIGHT. [Pok. 2. sek¥- 872.] sekw-3, To say, utter. 1. O-grade form *sokv- in: a. suf- fixed form *sokv-yo- in Germanic *sagjan in Old English secgan, to say: SAY; b. suffixed form *sok-d- in Ger- manic *sag6, a saying, in (i) Old English sagu, a saying, speech: sAw? (ii) Old Norse saga, a saying, narrative: saGA. 2. Suffixed zero-grade form *sk~-e-tlo-, narration, perhaps in North Germanic “skathla in Old Norse skdid, poet, “narrator,” perhaps akin to the probable Scandina- vian source of Middle English scolde, an abusive person: SCOLD, SKALD. [In Pok. 2. sek¥- 897.] sel-1, Human settlement. 1. O-grade form *sol- in Ger- manic *sal-, room, in Italian sala, hall, room: SALON, (SALOON). 2. Suffixed form *sel-o- in Latin solum, bot- tom, foundation, hence sole of the foot: SOLE!, SOLUM; ENTRESOL. [Pok. 1. sel- 898, 3. (swel-) 1046.] sel-2, Also sele-. Of good mood; to favor. 1. Germanic lengthened form *sél- in Old English ges#lig, happy (ge-, completely; see kom): SILLY. 2. Suffixed lengthened o-grade form *sdl-d- in Latin sdlari, to comfort, console: SOLACE; CONSOLE}. 3. Possibly suffixed form *sels-ro- in Greek hilaros (< *helaros), gay: HILARITY; EXHILARATE. [Pok. 6. sel- 900.] sel-3, To take, grasp. 1. Suffixed o-grade (causative) form *sol-eyo- in Germanic *saljan, to offer up, deliver, whence West and North Germanic “‘to sell,” in Old English sellan, to sell, betray: SELL. 2. Germanic *sal-, giving, sale, in: a. Old Norse sala, sale: SALE; b. Old Norse compound handsal, giving of the hand (in closing a bargain): HANDSEL. [Pok. 3. sel- 899.] sel-4, To jump. 1. Suffixed zero-grade form *sal-yo- in: a. Latin salire, to leap: SALACIOUS, SALIENT, SALLY, (SAUTE); ASSAIL, DESULTORY, DISSILIENT, EXULT, IN- SULT, RESILE, RESULT, SOMERSAULT; b. Greek halles- thai, to leap, jump: HALTER2. 2. Perhaps Latin salmé (borrowed from Gaulish), salmon (< “the leaping fish”): SALMON. [Pok. 4. sel- 899.] sel-es-. Swamp, marsh, sea. Greek helos, marsh: ELODEA. [Pok. selos- 901.] selk-. To pull, draw. 1. Perhaps Germanic *selhaz, seal (the animal), “that which drags its body along with difficulty” (but more likely an early Germanic borrowing from Finnic), in Old English seolh, seal: SEAL?. 2. Suf- fixed o-grade form *solk-o- in Latin sulcus, furrow, groove (< “result of drawing or plowing”): (SULCATE), sucus. [Pok. selk- 901.] selp-. Fat, butter. 1. Germanic *salb- in Old English sealf, healing ointment: SALVE}. 2. Germanic denomina-
1263:ASH? os- ASININE asinus ASK ais- ASPECT spek- ASPEN apsa ASPERSE (s)preg- ASPIRATE spirare Ass? ors- ASSAI? Sa- ASSAIL  sel-4 ASSAY ag- ASSEMBLE sem-! ASSENT sent- ASSERT ser-3 ASSESS sed-1 ASSET sa- ASSEVERATE weéro- assIDUOUS_ sed-1 ASSIGN sekw-1 ASSIMILATE sem-1 ASSIST sta- ASSOCIATE sekw-1 ASSOIL feu-1 ASSONANCE swen- ASSORT ser-3 ASSUAGE swad- ASSUASIVE swad- ASSUME em- ASSURE cira ASTASIA sta- ASTATINE  sta- ASTER  ster-3
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1461:ENNEAD newn ENNUI od-2 ENORMOUS gn6- ENOUGH kom, nek-2 ENSEMBLE sem-! ENSIFORM nsi- ENSTATITE sta- ENSUE sekw-1 ENSURE cira
1485:EXAMINE ag- EXAMPLE em- EXANTHEMA andh- EXARCH arkhein EXCALIBUR kal-3 EXCAVATE keue-2 EXCEED ked- EXCEL kel-6 EXCEPT kap- EXCERPT kerp- EXCISE? kae-id- EXCITE kei-3 EXCLAIM kela-2 EXCLUDE kleu-3 EXCORIATE sker-1 EXCREMENT krei- EXCRESCENCE ker-3 EXCURSION kers-2 EXECRATE Sak- EXECUTE sekw-1 EXEDRA sed-1 EXEGESIS sag- EXEMPLARY em- EXEMPLIFY em- EXEMPLUM em- EXEMPT em- EXERCISE arek- EXERGONIC werg- EXERGUE werg- EXERT ser-3 EXFOLIATE bhel-3 EXHAUST aus-2 EXHIBIT ghabh- EXHILARATE sel-2 EXHORT gher-5 EXHUME dhghem- EXIGENT ag-
1681:INQUIRE quaerere INSCRIBE skribh- INSECT sek- INSERT ser-3, s6-1 INSESSORIAL sed-1 INSIGNIA sekw-1 INSIST sta- INSOLATE sawel- INSOMNIA swep-! INSPECT spek- INSPIRE spirare INSTALL | stel- INSTALLMENT! | stel- INSTANT sta- INSTAURATION sta- INSTIGATE | steig- INSTINCT | steig- INSTITUTE sta- INSTRUCT  ster-2 INSULT sel-4 INSURE cura INTACT tag- INTEGER tag- INTEGUMENT (s)teg- INTELLIGENT leg-1 INTEND ten-
1683:INTRA- en INTRADOS dorsum, en INTRANSIGENT ag- INTREPID  trep-1 INTRINSIC en, sekw-1 INTRO- en INTRODUCE deuk-, en INTROIT el-1, en INTROMIT en, (s)meit(a)- INTRORSE en, wer-3 INTROSPECT en, spek- INTROVERT wer-3 INTRUDE treud- INTUITION teu- INTUMESCE teue- INTUSSUSCEPTION en, kap- INULIN wel-3 INUNCTION ongw- INUNDATE wed-! INURE op-! INVADE wadh-2 INVAGINATE wag- INVALID! = wal- INVALID2  wal- INVEIGH wegh- INVEIGLE okw- INVENT gWa- INVERT wer-3 INVEST wes-4 INVETERATE wet-2 INVOKE wekw- INVOLVE wel-3 INWARD wer-3 IODOPSIN  okw-
1952:OBEY au-5 OBFUSCATE dheu-1 OBITUARY el-1 OBJECT! yé- OBJURGATE ag-, yewes- OBLAST epi, wal- OBLATE! tele- OBLIGE leig-1 OBLITERATE deph- OBLIVION lel- OBLONG del-1 OBLOQUY tolkw- OBNOXIOUS nek-1 OBOE busk- OBSCURE (s)keu- OBSEQUIOUS sekw-1 OBSERVE ser-! oBsEss sed-1 OBSTACLE sta- OBSTETRIC sta- OBSTINATE sta- OBSTREPEROUS §strep- OBSTRUCT ster-2 OBTAIN ten- OBTECT (s)teg- OBTEST trei- OBTRUDE treud- OBTUND (s)teu- OBVERT wer-3 oBvious wegh- OBVOLUTE wel-3 OCARINA awi- OCCASION kad- occipuT kaput OCCLUDE kleu-3 occuLT kel-2 occupy kap- occur kers-2 OCELLUS okWw- OCHLOCRACY wegh- OCHLOPHOBIA wegh- OCTAD okto(u) OctTans okt6(u) OCTANT oktd(u) OCTAVE okt6d(u) OcTAvO okt6(u) OCTENNIAL at-
2081:PERQUISITE quaerere PERSE s(w)e- PERSECUTE sekw-1 PERSEVERE wéro- PERSIFLAGE swei-! PERSIST sta- PERSPECTIVE spek- PERSPIRE spirare PERSUADE swad- PERT wer-5 PERTAIN ten- PERTINACIOUS ten- PERTURB twer-1 PERVADE wadh-2 PERVERT wer-3 PERVIOUS wegh- PES ped-!
2136:PRO-2 per? PROBABLE per! PROBE pert PROBITY per! PROBLEM gWele-1 PROBOSCIS g¥6- PROCEED ked- PROCLAIM kele-2 PROcLITIC § klei- PROCLIVITY klei- PROCREATE ker-3 PROCTITIS prdkto- PROCTOLOGY prdkto- PROCTOR cura PROCTOSCOPE prdkto- PROCUMBENT keu-2 PROCURATOR cura PROCURE cura PROCYON kwon- PRODIGAL ag- PRODIGY ég- PRODROME der-1 PRODUCE deuk- PROFANE dhés- PROFESS bha-2 PROFESSOR reg-! PROFFER bher-1 PROFICIENT dhé-1 PROFILE gWhi- PROFIT dhé-1 PROFLIGATE bhiig- PROFOUND bhudh- PROFUSE gheu- PROGENITOR gene- PROGENY gene- PROGLOTTID glégh- PROGNOSIS gnd- PROGRAM gerbh- PROGRESS ghredh- PROHIBIT ghabh- PROJECT yée- PROLAN al-3 PROLAPSE leb-1 PROLATE tele- PROLEGOMENON leg-! PROLEPSIS (s)lag¥- PROLETARIAN al-3 PROLIFEROUS _al-3 PROLIFIC al-3 PROLIX wleik- PROLOCUTOR tolkw- PROLOGUE leg-1 PROLONG del-1 PROLUSION leid- PROMENADE men-2 PROMINENT men-2 PROMISCUOUS meik- PROMISE (s)meit(e)- PROMOTE meue- PROMPT em- PRONE per! PRONEPHROS _ negwh-ro- PRONOUN no-men- PRONOUNCE neu-! PROOF per! PROPAGATE pag- PROPEL pel-6 PROPEND (8)pen- PROPER pert PROPERTY per? PROPHET bha-2 PROPHYLACTIC phulax PROPINQUITY per? PROPIONIC ACID peie- PROPITIOUS pet- PROPOLIS pele-3 PROPORTION pere-2 PROPOSE apo- PROPRIOCEPTION per! PROPRIOCEPTOR per? PROPTOSIS pet- PROPYLAEUM pulé PROPYLON pulé PROROGUE reg-1 PROS- pert PROSCRIBE skribh- PROSE wer-3 PROSECUTE sekw-1 PROSELYTE leudh-1 PROSOMA teue- PROSOPOPEIA kWwel-2, per! PROSPECT spek- PROSPER spé-1 PROSTATE sta- PROSTHESIS dhé-1 PROSTITUTE sta- PROSTOMIUM ste-men-
2143:PURBLIND bhel-' PURCHASE per! PURE peue- PURFLE gWhi- PURGE peue- PURITAN peua- PURLOIN del-1 PURPORT per-2 PURSE bursa PURSLANE porko- PURSUE sekw-1 PURULENT pu-2 PUS pu-2
2180:REQUIEM kWeie-2 REQUIESCAT kWeia-2 REQUIRE quaerere REREDOS dorsum, re- RESCIND skei- RESCRIPT skribh- RESCUE kwét- RESEAU  era-2 RESECT sek- RESEMBLE sem-! RESENT sent- RESERVE ser-1 RESERVOIR ser-1 RESIDE sed-! RESIGN sekw-1 RESILE sel-4 RESIST sta- RESOLVE leu-1 RESORB srebh- RESOUND swen- RESPECT spek- RESPIRE spirare RESPITE spek- RESPLENDENT spel-2 RESPOND _spend- REST? sta- RESTITUTE sta- RESTIVE sta- RESTORE sta- RESTRICT  streig- RESULT sel-4 RESUME em- RESUSCITATE kei-3 RETAIN ten- RETALIATE telo- RETCH ker-2
2208:SAG sengw- SAGA sekw-3 SAGACIOUS sag- SAGE! sep-1 SAGE? sol- SAINFOIN dh@(i)-, sano- SAINT sak- SAKE! sag-
2221:SAY sekw-3
2225:SCHISM skei- SCHIST skei- SCHIZO-  skei- SCHIZONT es- SCHLEP |leij- SCHLIEREN sleu- SCHLOCK | slak- SCHMALTZ mel-1 SCHMEER (s)mer-3 SCHMUCK meug-2 SCHNAUZER snu- SCHNITZEL sneit- SCHNORRER sner- SCHNOZZLE snu- SCHOLAR segh- SCHOLASTIC segh- SCHOLIUM segh- SCHOOL! segh- SCHOOL? §skel-1 SCHUss skeud- SCIENCE skei- SCILICET skei- SCINTILLA skeei- SCINTILLATE skeei- SCIOLISM skei- SCION géi-1 SCIRE FACIAS dhé-1, skei- SCISSION  skei- SCISSORS kae-id- SCLERA skele- SCLERO- skele- SCLEROMA §skela- SCLEROSIS skela- SCLEROTIC skelo- SCLEROTIUM skela- SCLEROTIZATION skela- SCLEROUS skelo- SCOFF skeubh- SCOLD sekw-3 SCOLEX skel-3 SCOLIOSIS skel-3 SCONCE? dhé-1 SCONE keu-! SCOOP skep- Scop skeubh- -SCOPE spek- -SCOPY spek- SCORCH skerbh- SCORE sker-1 SCORIA_ sker-4 scoT skeud- SCOT AND LOT skeud- SCOTOMA  skot- SCOUR! cira SCOUR2 kéwero- SCOURGE reig-1 SCOUT! ous- scouT? skeud- SCRABBLE  sker-! SCRAG gWere-4 SCRAP!  sker-1 SCRAPE sker-1 SCRATCH grat- SCREAK ker-2 SCREAM ker-2 SCREECH ker-2 SCREED skreu- SCREEN sker-1 SCREW sker-! SCRIBBLE skribh- SCRIBE skribh- SCRIMP_ skerbh- SCRIPT skribh- SCRIPTORIUM skribh- ScRIPTURE  skribh- SCROBICULATE sker-1 SCROD skreu- SCROFULA  sker-1 SCROLL skreu- SCROTUM skreu- SCRUB!  sker-1 SCRUTINY skreu- SCUDO skei- SCUFF skeubh- SCUFFLE! skeubh- SCUFFLE? skeubh- SCULPTURE skel-1 SCUM (s)keu- SCUTCH kwét- SCUTTLE! skeud- SCUTUM  skei- SCYPHISTOMA skep-, ste-men- SCYPHOZOAN skep- SCYTHE sek- SEAL! sekw-1 SEAL? selk- SEAM syi- SEANCE sed-! SEAR! saus-
2230:sEccO seikw- SECEDE ked-, s(w)e- SECERN krel-, s(w)e- SECLUDE kleu-%, s(w)e- SECOND2 sekw.-1 SECONDO sekw-1 SECRET krel-, s(w)e- -SECT sek-, sekw-1 SECTILE sek- SECTION sek- SECTOR sek- SECUND sekw-1 SECUNDINES sekw-1 SECURE cilirra, s(w)e- SEDATE! sed-1 SEDENTARY sed-1 SEDERUNT sed-1 SEDGE sek- SEDILIA sed-1 SEDIMENT sed-1 SEDITION ei-1, s(w)e- SEDUCE deuk-, s(w)e- SEE] sekw.2
2236:SEETHE seut- SEGMENT sek- SEGNO  sekw-1 SEGREGATE ger-1, s(w)e- SEGUE sekw-1 SEGUIDILLA sekw-1 SEICENTO dekm, s(w)eks SEIGNIOR sen- SEISIN sag-
2248:SEPTUPLE pel-3, septm SEPULCHER sep-2 SEPULTURE sep-2 SEQUACIOUS sekw-i SEQUEL sekw-1 SEQUENCE sekw-1 SEQUESTER sekw-1
2249:SEQUESTRUM sekw-1 SERAC ser-2 SERE! saus- SERENE ksero- SERF servus SERGEANT servus SERIES ser-3 SERIF skribh- SERIOUS swer-5 SERMON ser-3 SEROTINOUS sé@-2 SERPENT serp-2 SERPIGO serp-2 SERRIED ser-3 SERTULARIAN ser-3 SERUM ser-2 SERVAL_ ker-! SERVE servus SERVICE servus SERVILE servus SERVITUDE servus SESQUI- kwe, sémi- SESQUIPEDALIAN ped-! SESSILE sed-1 SESSION sed-1 SESTERCE sémi-, trei- SESTET s(w)eks SESTINA s(w)eks SET! sed-1 SETTLE sed-1 SEVEN septm SEVER pere-! SEVERAL pere-1 SEVERE WEér0- SEW syu-
2257:SIGHT sekw-2 SIGN sekw-1 SIGNORY sen-1 SIKH kak-1 SILENT si-lo- SILL swel-3
2268:SITZMARK sed-1 SIX s(w)eks SKALD sekw-3 SKATOLE sker-4 SKEAN skei- SKEET skeud- SKELETON skele- SKEPTIC spek- SKI skei- SKIAGRAM skeei- SKIASCOPE skeei- SKIFF skipam SKIJORING geue- SKILL skel-1 SKIN sek- SKIPPER! skipam SKIRMISH sker-1 SKIRT sker-1 SKIVE skei- SKOAL skel-1 SKY (s)keu- SLAB? leb-1 SLACK! slég- SLAG slak- SLAM! leb-1 SLAP leb-1
2273:SNIFF snu- SNIP snu- SNIVEL snu- SNOOP snu- SNORE sner- SNORKEL sner- SNORT sner- SNOT snu- SNOUT snu- SNOW sneig’h- SNUB snu- SNUFF! snu- SNUFFLE snu- SNUG! kes-1 sO swo- SOAK seua-2 sOAP_ seib- SOAVE swad- SOBER s(w)e- SOCIABLE sekw-1 SOCIAL sekw-1 SOCIETY sekw-1 SOCIO- sekw-1 SOCKET sU- SODALITY s(w)e- SODDEN seut- SOIL! sed-1 som? si- SOIREE sé@-2 SOJOURN deiw- SOKE sag- sol’ sawel-
2323:sTuD2 sta- STUDENT (s)teu- sTUDY (s)teu- STULTIFY _ stel- sTUM stam- STUMBLE stam- STUMP stebh- STUN (s)tena- STUPA steu(@)- STUPE steu(9)- STUPEFY (s)teu- STUPENDOUS (s)teu- STUPID (s)teu- STURDY trozdo- STUTTER (s)teu- stTy2  steigh- STYLITE sta- STYLOBATE gWa-, sta- STYPTIC steu(@)- Styx (s)teu- SUASION swad- SUAVE swad- SUB- upo SUBALTERN al-1 SUBAUDITION au-5 SUBDUCTION deuk- SUBDUE deuk- SUBITO ei-! SUBJACENT yé- SUBJECT yé- SUBJOIN yeug- SUBJUGATE yeug- SUBLUNARY leuk- SUBMERGE mezg-! SUBMIT (s)meit(9)- SUBORDINATE ar- SUBORN ar- SUBPOENA kwei-1 SUBREPTION rép-1 SUBROGATE reg-1 SUBSCRIBE skribh- SUBSEQUENT sekw-1 SUBSIDE sed-1 SUBSIDY sed-1 sUBSIST sta- SUBSTANCE sta- SUBSTITUTE sta- SUBSTRATUM ster-2 SUBSTRUCTION | ster-2 SUBSUME em- SUBTEND ten- SUBTERFUGE bheug-', upo SUBTERRANEAN ters- SUBTLE teks- SUBTRACT tragh- SUBULATE syU- SUBVENTION gWa- SUBVERT wer-3 SUCCEED ked- succincT kenk-1 succor kers-2 succuBUS keu-2 SUCCULENT seud-2 SUCCUMB keu-2 SUCCUSSION kwét- SUCH swo-
2325:SUE sekw-1 SUFFER bher-1 SUFFICE dhé-1 SUFFICIENT dhé-1 SUFFIX dhig’- SUFFRAGAN bhreg- SUFFRAGE bhreg- SUFFUSE gheu- SUGGEST gerere SUICIDE s(w)e- SUINT sweid-2 SUITOR sekw-1 SULCATE selk- SULCUS selk- SULLEN s(w)e- SULTRY swel-2 SUM uper SUMMER! sem-2 SUMMIT uper
```


## [2026-09-14T01:56:46.331Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT haxay\"; grep -n \"haxay\\|haxa-\\|haxā\" BRT.txt | head -30\necho \"=== BRT hačā/haca\"; grep -n \"^hača\\|hača-\\|haca-\" BRT.txt | head -30\necho \"=== BRT adairi\"; grep -n \"adairi\\|aδairi\" BRT.txt | head -20"
}
```


### [2026-09-14T01:56:46.433Z] TOOL RESULT

```
=== BRT haxay
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2478:Stelle  der  kongruenten  Form  steht :  a)  das  i ;  —  iE  äbyö  frSrtt^  fr}r»m-ainti  asaonqm Neutr.  Sing.:  yüzim  .  .  aogS  data  .  .  x/a-  ..frtrvaBbyoYX.13.afi;  —  zugleich  zurück- '^nmcS  .  .  azimcll  ahyä  (statt  Du.)  ..'weisend:  asti'atjntö  ..  atihe  haxayü  frä- %wqm  mPtihi  ..vaSd>m{sA.)Y.2<).ia;  —  \yente  astvatjr?lahe  Yt.i'>.95;  —  dacnnm dva/sing  ..  qstqscä  .  .  yezT  ahyä^^  (statt'.,  atiihi  ..  kavaya  ..  daenayn  V./o.ig. Plur.) /ö/  mal  xsayehTY.44.\\i.; — duye  —  a)  mit  relativischem  Anschluss;  ama- navaiti  astanqm  (sd.)  .  .  däittm  ahmäicil  !'af6yö  acibyö  yazataHbvT'  yat  am»saeibyö harf^r?m  hrmi^ät  V.  74. 17.  b)  das  sp»^aAbyöYi.fj.^;  —  mmö  äbyö  döi'iräbyü
4650:äahtmm  gä'^anqm  sraohrät  pairistaytili  N.^'<>;  —  mmS  ahuräi  mazdai  mmö N.4^;45^*fH.2.i3; — yd  'nyehe  dahmahe  amisaiibys spintaHbyS mmS'nyagsqm  asao- bansma  *frast»r3nfe  ii.104;  lOi;  —  bsöalnqm  V.i^. 25:32;  —  »üi/  xsnSvayeiti  ahu- iia  hislahe  ..  'nyehe  dvan  (sd)  srayatül  r?m  mazdam  tUSit  °nye  (als  AP.)  amisO. V.j.zg;  N.6',7; —  hvSiits  vä  ySiitö  (i'3)  |  ¥1,70.139;'  '39;  —  hapta  hanti  *käva- yim  vä  'inim  *hais^aeTia  (sd.)  .  .  cayqn ,  iiayS  ratavS  .  .  aai  'nyahu  ralu/risü  N. N./;  — ]avada  'niyam  md^ifia/fi  . .  Bh.  102.  a)  mit  ciV'' :  saoiyanlqm  vfn'üra- 5.  4(?);  —  "nyqmca  suttm  ..  N.ff2(,?);  — jamm  Uta  "nyasHt  (als  APn.)  haxayS  Yt. ^rayS 'nya  (als  APm.)  maya  nihwirgsöU  /p.S9'*'.  NSm.  "/yJ,  ASm.'fiim,  ASn.
4828:mit  frS^''^  i)  'hervorgehen,  -Ireten': aiiihe  haxayB  fräyente  astva(.»r>take  Yt. ■'5-9SJ  — yü'ia  .,  hvanxsaet^m  tarasca harqtn..fraca  iii/i  aiwica  vazaite  ava^a  . . Yt  /0.118.  2)  'vorwärts,  weiter  gehen': fräyantö  tarö  pilüm  ..yim  cinvats  Vyt. 42.  a)  &oiysX  mA  ß-a^a: /rain /raysiii^ irUtim  uzbaröti  äpö  V.6.2T,  — /ra/a  fra- yaniu  n  maoö  (sA)  Y. /O.  14,  ig;  19;  — /rasa  /raya  (aSIA.)!'  vahisDm  a  ahüm binjayanti  (sd.)  ie  ..  V,  7.52;  —  vgl.  Inf. Jrayäi.  3)  'einhergehen'  iyio? paiti  mit Akk.):  yat  ÖS  paiii  ml  asava  frayaf^  .  . aismssastö  .  .  V.J.  i ;  —  äat  liama  yh paiti  frayat^^  tä paiii, .Yi.  lOjiJ).  4)  'be- gehen', mit  Akk.,  a)  einen  Weg:  kaf  tä pa>ä  (sd.)  Jrayqn^  pasvqm  vil  staorqm va  narqm  vä  Y.S.iy,  ii^23,  3.  15;  — likrava  paoirlm  aHa  pa%ä/rayanlu{s\.3Xl Sing.)  V.  Ä19.  b)  eine  Tat:  (aili  tä ^ao^aa  varsta  , .  fralta^''^  apati(a{&i.) anuzvars/a  . .  V.i^.i.
5662:•  j.  arätat-  f.  Name  derGöttin  {Yazala-)''' der  Geradheit,  Aufrichtigkeit"':  ys . .  tars manyete..  mi'irym..  larS  dätimca  rasnSmia •tät>m:a  fradat^at^qm  varidai^aiüam \X.io.  139;  —  raltiüm  rasiii?m..  °t3t>mca frädatgae^am  vandat^afkam  Y.  2.  7;  16. 6,  S.2.26,  Yt.J'j.ia,  Vr.7.2;  —  haxaya •tW/rädat^aikayä..\t.s].  16;^ — rasnaol raästahe  °t3lasca  frada^^ai>:ayh  var>dat.- gm'^ayh  Y.  /.  7.  —  a)  arstäts  (nämL  ayan) heisst  der  26.  Monatstag:  °W/J  /rädal.- gas'iayj  S.  J.  26;  vgl,2.26,  Y.16.6.
6925:i_fj  'mäi  gam  .  .  hSmJalat  at  höi  vSstrüi (sd.)  ..  Y.  47.35»;  —  'aeibyo  mal  as,i syazdat  yavqt  'mat  aurutiä  (sd.)  xra/strä Y.J4.9**; —  uzgpuniayeinti  zaslS  'mak^m ,  (GS.)  avaähe  yüsmäk>m  yasnahe  YL  13. 1 147;  —  s.  noch  unter  a,  a  a,  2)  vor I  einer  erläuternden  oder  ergänzenden  Bei- fügung; haxaya  •mäktm  saosyantqm  Yt. //.  17;  F.  7,  Vyt  J7; —  däyata  . .  mäva- yaca  zagere yaziinnai  'mäksmca  (statt  Dat) matdayasnanqm  fräyaztmnanqm  Y.  68.1 2; Vr. /2.  s;  —  haca  ahmät  nmätiift  "mä- kiiiua  mazdayasnanqm  "aus  dem  Haus hier  und  aus  (je)dem  von  uns,  der  M." Yt./_j.57;  —  s.  1.  a)  mit  relativischem .  Anschluss:  aom  narfm  .  .  yü  kasiSt?m  .  . \frSyatat  (sd.)  *°ma  (Akk.)  ^j-a"  atnisS sp?ntS  Yt  /.  24;  —  yUsmäk>m  yasmiica  . . \yqt  am^sanqm  .  .  'mäJhi/i  havaiiuhüua  ,  . ^yat  laesyatäam  Y.  14.  i,  Vr.  5.  i ;  Yt.  J.  i  f., I  FrVV.  I.  2 ;  -  's.  1 .  3)  sonst;  a)  D  im  Ap.
8195:vor  dem  ersten  Glied;  'ta  buyä  afrasaiiitil 'ta  äSu^.sravä  AacimnS  Y.  /;.  i ;  —  E  gau- mülJ'  .  .  adlru^  k^bajiyam  °tä  psrsam 'tä  mudam  'ta  aniyil  daAyav^^h.i.ii'i*; loJ*',  iii*>,  2.13*,  14';  — fras'a  upa.- Siiiidayäti  tni^rS . .  'ta  nmänjui  °ta  vXs?m 'ta  . .  Yt.  /o.  i89.  b)  beim  letzten  Glied zusammen  mit  a)  td,  ß)  /i^  (s.  auch  II  2  a) 'und  auch';  a)  barat  i^amiS  , .  baSsas>m 'ta  anumca  Vt/^.2.  ß)  yat  upanhacat taelyantqm  vprpiräjanfin  'ta  anySsat'"' haxayS  Yt.  /().  89;  87;  —  Aazar^nm Vij^wA  bavaiti  'ta  äsmmcit  frazaintm Yl  /<V.  5.  II)  zur  Verbindung  von  Sätzen; i)  bei  gleichem  Subjekt:  \  hauv  käram fraisayi^  ..  'tJsiJm  i  martiyam  maiistam aiunaus  Bh.j.^;  l.iS,  2.4,  13',  14',  16, 3.7,  II,  4-2,  16,  I70-I'.  D-4.3,  X.7.3; —  babirum  asiyavam  vasna  a'urtrmaz- dähJ'  °/(7**  babirum  agarbäyam  'tä  avam .  .  agarbJyam  "ich  zog  nach  Babylon und  nahm  nach  dem  Willen  AhM&. Babylon  ein  und  nahm  jenen  .  .  ge- fangen" Bh.2.1-,11  — ya'^a  az?m  banäa- ytni  .  .  fraiirasyätam  'ta  .  ,  vdaayeni  'ta .  .  upanayeni  YL5.18;  9^,  31*,  5.34,  82, ;;.2,  Y./0.4,  F.p»  FrB.  a)  Das  Sub- jekt ist  wiederholt:  'ta  drvh  asp>m  *viste\ 't.i  drva  .  .  yavanhim  *viste  Aog.  ^2;  —  | da'iäni  li  .  .  'ta  tl  az?m  afrlnäni  V,  22. 5.  a)    bei   verschiedenen   Subjekten:
8313:•  j.upayanä-f,  m\ldar/ya-  Adj.,  'die  lange Überlieferung",  d.  i.  'die  überliefeite  Lehre, die  Tradition'*':  vTspam^a  ma%nm  spunipm .  .  vJspimia  äät?m  vTdSyüm  .  .  vtspqmca darTjqm  'nqm  Y.  77.5;  2, 13;  —  darryaya 'nayäY.i.ij- —  haxaya  dar^yayä  'nayh Yt.  II.  1 7.
17433:(NP.)    vä    haxaya    vä   V.  4. 44;    ■ —    nsil
18478:•  j.  iiae9a.£it  Fait,  verstärktes  na^a: haxayS  .  .  ostvatjrHakc  .  .  humananks  .  . AttlaSta  n'  m^i!.ac/ät»ÄS  (sd.)  Yt  ig. 95.  a)  verstärktes  nsit'^:  ava  *vTsaäe *n'*i  ästryäle  P.57.
20509:•  j.  nii&ö.aog-  Adj.  'fälschlich  redend, falsche  Rede  führend':  haxayö . .  hu^ama Ait/yaohnäighs  na^a.cil  'Jsn/iS'^  alsqm ifa^aiiiya  AixvS  ". .  und  nicht  Itihren  sie irgend  falsche  Rede  mit  ihrer  (eigenen) Zunge"  YtJp.  95').  [S.  noch  "mi^rJ.- ao/aA:]
20883:razunm  (sd.)  yS  mqm  mairyö  .  .  paiti pantata  "laqueum  (insidiatoris)  qui  me insidiator  ,,  oppugnavit"  Yt5.  so^J*;  — yö  ktnnavät  (Sp.  447  o.)  yim  yataite MÜrfm  .  .  albists  hyat  Yt.  10.  iio;  — fra paurvö vätqm  vazailt yqm<,^-ai.) pa>ö siti  haomö  ". .  (ad  vias)  quas  vias  .  ." Yt.  Ä33;  —  üvistayaica  ..  huframirtta- ya?ca  ysi  htnti  haoma  sura  "..(vinorum) quae  sunt  vina  .  ."  Vr.  (?.  3;  —  udiyasca rasvas^a  gatris  yailqmta  .  .  masyika  . gairinqm  nilmqm  ddhar>  "et  U.  et  R.  mons et  (alii  monte.s)  quorura  .  .  montium  . ." Yt.  IQ.  6.  c)  yS  NSm.  und  ySi  NPm. stehen,  ohne  Beziehung  zu  einem  Wort  des Übergeordneten  Satzes,  d)  im  Vorder- satz im  Sinn  von  'wenn  wer,  wenn  einer, wenn  man':  yp  kainTti?m  upäiti  .  .pührqm- {sd.)i^  hl  daoäili  mä  .  .  agsa  ya  kaine . . tarO  daxslsm  paraylt  (Sp.  152  u.)  V, /5. 9;  —  y5  ffiirikam  U^ravaittm  . .  xsudrä avi  fraiiharisaiti  hat  aiiihe  asti  paititis (sd.)  V.jtV.67f.;  —  y5  hl  *3p?r»ti3mnai (Sp.  869  o.)  nsil  visäiti  *främrUite  kö  .  . ai>!rapaitinqm\ea^  ..  astryäti  N.  j_j;  — yö  aiuä  bansma^a  */ra stürmte.. aoäi  anye . .  *framravainti  . .  vispaZiqmcd  arwi.snm- vaiti  (sd.)  vispe  ratufryB  N.  6b;  —  y5i pa'^a  utbartnte  spanaüa  irista  naraiM  . . hat  tä  päka  (sd.)  frayqn  .  .  "wenn  man desWegs  hinausträgt  tote  Hunde,.,  sollen  .. V.Ä14;  —  *ySi  dim  */rahincin  *antari ätar>m:a  bar>smaca  anairyanqm  tat  dahyu- nqm  v»r>hrili  uzjasaiti  N.  6(Vj  —  mit  der 1.  Plur.  im  Sinn  von  'wenn  wir,  unsereins': ySi  timäni  hqmiarämahi  (sd.)  . .  alrsmca .  .  aaf  pascaäa  . .  sps  vä  tiä  vä  iri^yat huha  ts  v»i-)^qn  aSe  ySi  mazdayasna  V. 5.39.  b)  im  Nachsatz  im  Sinn  von  'dass einer':  aya  daoia  disyJ/(sA.)ylf..  aiwy'ir?- hqm  (sd.)  nSii  aiwyästi  V.  18. 9.  ß)  adjek- tivisch: yaEca  ß«  narS  . .  Jason  brä^ra vä  haxaya  vH  .  .  yezi  laäS-cinanhö  jasqn .  hqm  ioa  iaSitm  hqm.bäray>n  "quique  . .  vin venerint,  (iis)  ,  ."  V.  4. 44.  Anhang
21468:/raonHnta{5Ä)  äat . .  afvs zara'huitrS ..  Yt. 77. 19;  —  yäi,a  anye  'täahs  .  .  yazinti Yt  Ä  1 1 ;  —  haxaya  vXspaäam  'tanam YtJJ.17; — urvdha  'tanqm  bavahi ya%a.. A2.4;  —  ka%ra  vatfhuiys  'tazifyö  yat am?iälibyS  sptntaübyl}  Vr.  Ä  i;  p,  4;  — yaitustsmtm  'tanqm  .  .yatamaide  Y.  7/.  3');
25849:5. 1,  22. 1,  YL//.  17.  3  a)  Rur..  von den  künftigen,  am  Ende  der  Dinge  auf- tretenden Rettern,  die  die  Neugestaltung (fraiS-hnlay^  sd.)  der  Welt  bewirten: aoi  mqm  (nämL  haoimrn)  . .  staihi  yäha mä  aparaSl  'yantS  slavqn  ".  .  wie  mich die  künftigen  S.  preisen  werden"  Y.(J.  a; —  airyamaftfm  i/Tm  .  .  hm  *marSnti •yantS  FrW.^.  1;  —  s^armS  .  .  yal  upa- rthatat  'yantqm  vm%r3jamm  (s.  b)  Uta anyiscit  haxaySyai  A>rmavat  frasfm  ahatn
28905:•  j.  haxa-  n.  'Fusssohle':  äruxs  yä  nasui .  .  alairi  'x>m  mvSiryde  V.&69;  F.Jg; —  daiitum  {bez.  hsyum)  'xam    V,  ü.  70*.
28907:•  j-  (1  g-t  P)  haxay- :  Ariy-,  Aai'-^^,  m. i)  'Freund,  Genosse':  ^m  °xa  (NS.)  '1/ (DS.)  *baraiti  Y.  6'2.  8;  —  aa£  aosOe  'xa •sa  (IS.)  V.  18.  a6;  F.  24;  —  yaS:a  . .  mri Aamü.äaina  Jason  brn%ra  va  'xaya  (NP.) vä  V.  4.  44;  Vyt,  10;  —  vlsaitiva  asti mi^r5  atiian  'ia  (AD.)  suptiiiannga  (sd) Yt.  JO.  116;  —  Sxstim  kqm.vaintfm  .. 'xaya    (AD.)    sraosaAe    Yt  //.  16;     16',
30418:—  yum  'nS  kvacS  *hulyao^na  *hudaina H.2.ir,  12;  —  haxayS  . .  'natakB  hva- ioTihS  hu^aöiinäahö  huoa^na   Yt/^.  95;
30570:•  g.  huS.haxay-  Adj.  'gut  freund,  wohl- befreundet mit—'  (Instr.):  mazda  ahurS.. asä  'xa  Y._j2.  2;  —  tSm  vS  asä  mJhmatdl *'xäim  (AS.)"  "ihn  halten  wir  tür  gut  freund mit  eurem  As'a"  Y. 46.12.
30627:—  at  ~h'  vanASuI  vaAyS  (sd.)  na  aÜT.-  yünat  Aaca  .  .  'caahat  P.,?j;  —  yuin  .  . jamyät  yS  na  .  .  sUsit  Y.  43-  3-  [Y. '  "Ä?  H.  2.  11,  11;  —  haxayS  ..  'canhö  Yt 29.7:  lies  hvd.urulaäbys;  —   ^5^":   lies   z^.  95-
=== BRT hačā/haca
28820:•  j.,  g.  'hak-  V.  'sequi*.  Fracs.  1  Äai-, si;  2  haca-,  5  *his.hak-\  hisk-,  15  haxsa-, 16  (Des.)  hixia'^,  2  +  24  hacaya-,  30 (Her.)  häcaya:  —  PPfP.  'haxta-;  Inf. haxtSit.
=== BRT adairi
3256:•  j.  adairi  Praep.  'unter,  unterhalb';  i)  mit Akk.:    ao'  hax>m  nivöiryeite  V.  <¥.  69;  —
```


## [2026-09-14T01:56:47.362Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT haca\"; grep -n \"hacā\\|haca\\b\\|Haxāmaniš\\|Haxamanis\" KNT.txt | head -40"
}
```


### [2026-09-14T01:56:47.431Z] TOOL RESULT

```
=== KNT haca
1881:Derivative adjectives to compounds may be made by the addition of suffixes; Haxamanis-iya- ‘Achaemenian’ to Hazámanis-, Asagart-iya- ‘Sa- gartian’ to Asa-garia-.
2771:In DB 1.8 haca paruviyata, hyd amüxam tauma z5àyaBiyà aha, the probability is that rsdyaiyé 18 nom. pl. ‘kings’, in which case dha is plural, agreeing with its predicate; but if z$üya8iyü 18 taken аз nom. sg. adj. ‘royal’, aha is singular, agreeing with its subject taumd ‘family’.
3450:CMa = Cyrus, MunaHAB (PASARGADAR) А, 1 adam : Kürus : xSaya 2 уа : Haxamanisiya TRANSLATION or CMa: I am Cyrus the King, an Achaemenian.
3607:64 :08tiy : Dirayavaus : xšāyaðiya : pasáva : adam : nijàyam : haca :
3963:8 Cispi$ ; CispaiS : pita : Haximanis: 4 9 0atiy : Darayavaus : xšāyaðiya : avahya ^ ^^ 10 radiy : vayam : Haxamanisiyà : баһуй 11 mahy : hacá : paruviyata : àmàtà 12 : amahy ; haca : paruviyata : hyà 13 xam : taumá : xšāyaðiyā : dha : 6a 14 бу : Darayavaus : xSdyafiya : ҮНІ : ma 15. nà : taumiya : tyaiy : paruva
4039:DPb = Darius, PERSEPOLIS B. Dürayavaus : XŠ : vaaraka : Vistàspahy& : puça : Haxamanisiya
4203:1 adam : Dàrayavau 2 $:xSdyafiya 3 : vagraka : xSaya 4 буа : xšāyaði 5 yanim : xSdya 6 (ya : dahyünà 7 m : xSdyablya : '8 haruvahyáàya : 9 bümiyà : Vist 10 àspahy& : puça ll : Haxāmanišiya TRANSLATION OF DSb: Iam ... (= DPa 1-4), King in all the earth, ... (= DPe 4-5).
4322:9 риса : Haxamanisiya : 0ütiy : Da 4 rayavaus : XS : manā : АМ : АМһа : айаш: AMm : 5 ayadaiy : AMmaiy : upastàm : baratuv TRANSLATION OF DSk: $1. 1-3. Тат... (= DPa 1-5). §2. 3-5. Saith Darius the King: Ahuramazda is mine, I am Ahuramazda’s. I worshipped Ahura- mazda; may Ahuramazda bear me aid.
4404:9ш: katanaiy : haca : Piráva : nàma :
4406:10 iy : draya : tya : haeá : Рагва : aitiy : pasdva : iyam : yauviya : akaniya : 11 avafá : yaf : adam : niyastàyam : utd : nāva : àyatà : haca : Mudra 12 уй : tara : imam : yauviyim : abiy : Pársam : араба : yatà : mim : Ката : dha
4425:20 à : puça : Haxamanisiya TRANSLATION OF DE:
4430:2 üvnàm : Vistispahya : puça : Haxāmanišiya :
4481:XPc = XERXES, PERSEPOLIS C. 1 Бара : vazraka : Auramazda : hya : пойт : bümim : 2 ада : hya : avam : asmànam : ada : һуа : marti 3 yam : ada : һуа : Siyátim ; ada : martiyahyà 4 : һуа : Xšayāršām : XS8m : akunaus : aivam : pa 5 rūnām : XSm : aivam : pariinam : framátàram 6 :adam : XSayarsa : XS : vazraka : XŠ : XSanam : XS: 7 dahyünàm : paruv : zandndm : XS : аһуйуй : b 8 ümiyà : vazrakiya : düraiy : apiy : Darayava 9 haus : XShya : puça : Haxāmanišiya : 6atiy : X 10 šayāršā : XS : vazraka : vašnā : Aurahya Mazdaha : i 11 ma ; hadis : Dárayavaus : XS : akunaus : hya : manā : 12 pità : mim : Auramazda : pátuv : hada : baga 13 ibis : utd : tyamaty : kartam : uta : tyamaiy : 14 pica : Darayavahau’ : XShyá : камат : avaSely 15 : Auramazda : pátuv : hada : bagaibis
4607:57 iya :màm : Auramazda : patuv : haca : ga
4675:АЛ = ARTAXERXES I, INCERTO LOCO. Artaxfaci : XS : vazraka : XS : XSyinam P E DHyünàm : XéayarSahya : XShyà : puça : XSayarsahya : Dàrayavausahy& : XShyà : риса : Haxamanisiya : hya : imam : batugara : slyamam : vidiya : karta
4685:D'Sb = Darius IT, Sesa B. 1 айат: Dárayasaus : XS : vazraka : XŠ : XSyanam : XŠ : DHyünàm XŠ : а 2 hydyd : Вуй: Artazsagahyá : XShyá : puça : Haxamanisiya : 3 batiy : Dürayavaus : XS : ima : hadiš : Arlaxíacü : paranam : akunaus : 4 hya : mand : pilà : ima : hadis : pasava : vasnà : ÁMha : adam : akunavam Notes то D'Sb: Вга. WZKM 39.85-7, after the Akk., restored ? [apara]m ‘upper part’ = ‘part at the top of the slope’, and * [adaram] ‘lower part’ = ‘part lower on the hill’; but Hinz, ZDMG 91.251-2, restores [paranalm and [pasava], in temporal sense, which is preferable. *akunas in copy b. TRANSLATION OF D'Sb: $1. 1-2. ... (= DNa 8-12, with one omission), son of Artaxerxes the King, an Achaemenian. §2. 3-4. Saith Darius the King: This palace Artaxerxes previously built, who was my father; this palace, by the favor of Ahuramazda, I after- wards built (to completion).
4698:A’Sc = Artaxerxes II, Susa c. 0 Dérayavausahya : XShya : puça : 0 Dérayavausahya : V'Staspahya : puça 1 : Haxamanisiya : дану : Artaxsaga : 2 xSayabiya : vazraka : rSayafiya : х 9 šāyaðiyanām : xSdyafiya : dahyün 4 äm : xšāyaðiya : ahydya : bumiyd : 1 5 mam : hadis : uta : imam : usta 6 сапат : tya : afagainám : ta +++++4 ООА : Auramazdà :
5384:-ciy encl. particle, emphasizing or generaliz- ing, nsn. or asn. of с1-: Ау, -Git, Skt. eid, СК. т, Tat. quid, pIE *q*id (840, §84, $113, 5191.11, §201, 6998.11). In the following combinations: aciy (q.v.) ХРЇ 21. aniyaš-ciy nsn. DB 4.46; XPa 13; aniya&-c (452.1) XPh 41f; aniyai-ciy npm. XPf 29. avas-ccy nsn. DNb 55; asn. DNb 53f, 57; XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 5.9. Ка&-сїу nsm. DB 149, 53; DSe 37. @& ciy asn. DB 1.58. paruvam-ciy DB 1.63, 67, 69. yaciy (q.v.) DNb 35, 36, 57. haw-cty DPe 23f. hakaram-ciy DNb 34f. [haca-cily DSf 23: vakna-|cily XPg 7f, less likely than vaknalptly, see under apiy. |
```


## [2026-09-14T01:56:53.086Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==228' KNT.txt | head -60"
}
```


### [2026-09-14T01:56:54.162Z] TOOL RESULT

```
ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1); see OP mar-, and cf. Hz. АрІ 249-51. тапа пзш. XPh 48, 55. marlahyá gsm. РВ 5.20, 36.
EU: ET TORR ON |
INS SEE cals la pen X AN, ae ete. ЫЗ, Ses f. Av m ee Sm SN Ie e mne -
LEXICON 203
‘martiya- adj. as sb. ‘man’: -ize- extension of pIE *morios, Av. marata- ‘mortal, man’, NPers. márd, Skt. mária- (§31, $106, $122, 5242.11), ef. ~o- extension in Av. masya-, Skt. mártya- ($144.IV). See also wmartiya-, *Martiya-.
martiya nsm. DB 1.21, 36, 48, 74, 77; 2.8, 14, 79; 3.12, 22, 70, 78; 4.38, 65, 68; 5.5°, 7°; DNa 46; ОМ 16, 19, 21, 24; XPh 51. martiyà узш. "Ма 56. martiyam asm. DB 3.57; DNa 3; DNb 12, 22; DSe 3; DSf 2, 16f; DSs 2; DSt 3°; рле 2; DE 4f; XPa 2; XPb 4f; XPe 21; XPd 3f; XPf 3; XPh 3; XE 5; XV 4; A'Pa 3P; А°Не 3f; A?Pa 3f. martiyahyé gsm. DNa 4, 44; ОМ 3; DSe 4f; DSf
. 8; D8s 5^; DSt 4^; DZe 2f; DE 6; XPa 3; ХРЬ 6;
ХРе 3; XPd 4f; ХРі 4f; XPh 4; XE 7; XV 5; AlPa 5°; A?He 4f; martthya A3Pa 4f (852.VI; hardly phonetie, as taken by Morgenstierne, Ácta Or. 1.253). martiyá npm. DB 1.571; 4.80, 82; DSf 47, 49, 51, 52, 54. татітуй apm. DB 2.77; 3.48, 50, 74, 90, 91. татйуйтат gpm. DB 4.87. martiyaibiš ipm. DB 1.56f.
? Martiya- sb. ‘Martiya’, a Susian rebel: Elam. mar-tiia, АКК. mar-t-ta; same аз 'martiya-, specialized as man’s name (§168.Ib, $164.III; but ef. HK Iran. Eigenn. 13-4, Phil. 66.183-4, ApKI 1.54, 2.26). Martia nsm. DB 2.8; 4.15; DBf 1. Martiyam asm. DB 2.12f.
mard- vb. ‘crush’: Av. marad- ‘destroy’, Skt. mrd- ‘rub, crush’, Lt. mordet ‘bites’, pIE *merd- (Foy, KZ 35.48). See also Marduniya-.
vi- + mard- ‘destroy’: vimardatiy (830, $213) DSe 40f. wyamarda imf. (written viya : marda, $44; cf. also $52.IV, $228.II, and Lex. s.v. -di-) DB 5.11.
Marduniya- sb. 'Mardonius, father of Gobryas: Elam. mar-du-nu-ia, Gk. Марббио; per- haps deriv. to *marduna- ‘vintner’ (§144.IV, 8147. П, $153.1, $164.1V), ef. NPers mul ‘wine’, Skt. mydvikd- ‘grapevine’ (Bthl. AW 1151; otherwise Justi, INB 195), which possibly contains root mard- ‘crush (the grapes in the wine-making)’. Marduniyahya gsm. DB 4.84.
mav- vb. ‘send’: ef. Lt. moved Ч move’. [0т]- арай imf. mid. as pass. ($213, $235.II) DB 4.92 (dubious conj. of Kent, JAOS 62.269).
Mazdàh- adj. ‘wise’ (5156.1, $160.Ia): regu- larly compounded in Auramazdah- (q.v.); both
parts declined, but without an intervening word- divider, in Aurahya Mazdaha (8$185.IV) ХРе 10.
maskd- sb. ‘(inflated) skin’; NPers. mask, АКК. mas-ku-u ‘skin’, Aram. maškā: borrowed from Semitic ($99, $109, §117, §148.IV; see MB Gr. 5101). такаа lpf. (872) DB 1.86.
müha- sb. ‘month’: Skt. mása-, pIE *méso-; extension ($143.II) of pIE *més-, seen in Av. mah-, NPers. mah, Skt. mäs-, cf. also Lt. ménsis, Gk. шу, Gt. тепа, ОНС mano, Lith. ménuo, all mean- ing ‘moon’ or ‘month’. mdhyd gsm. DB 1.371, 42, 56, 89, 96; 2.26, 36, 41, 47, 56, 61f, 69, 98; 3.8, 18, 39, 46f, 08, 68, 88 (for *mahahyé, with con- traction of- ähah- to -ah-, with Gray, AJP 21.13-4; rather than the usual interpretation as ism. to stem mah-; $131, $165.n1, $185.IV).
miðah- sb. ($156.П) ‘evil’, the opposite of rüila-: Av. mibahya- ‘evil’, mi6aoxia- ‘falsely spoken’, Skt. mith- ‘to meet (as friend or antago- nist), engage in altercation’; cf. Hz. ApI 259-61, Kent Lg. 15.169-70, and hamigiya-. тиба asn. DNb 7, 9, 11.
Mié6ra- sb. ‘friend’; as deity, ‘Mithras’: El. т1-14-5а, Akk. mi-i-ri; Av. mibra-, NPers. mihr ‘sun’, Skt. mitrd- ‘friend’ (§9.VI, $33, §49c, $78, 5148.11). Cf. Vaumisa- and probably hamigzya-. Міга} nsm. АНЬ; Mitra (822) A’Sd 4, A?Ha 6; Ма А?а 5, А?Ра 25. Аз gen. ($818.П), M'tra A?Ha 5°, M‘éra A’Sa 4.
mub- vb., see maub-.
M udràya- adj. ‘Egyptian’; pl., al
```


## [2026-09-14T01:56:54.801Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"j\\.,\\s*g\\.\\s*haca\\|• *j\\. *haca\\|haca  *Praep\\|haca Praep\" BRT.txt | head\ngrep -n \"haca\" BRT.txt | sed -n '1,5p' | cut -c1-200"
}
```


### [2026-09-14T01:56:54.892Z] TOOL RESULT

```
29057:•  j.  hacant-  Adj.,  PPA.:  s.  ^hak-.
2452:—  paoiryö  gairis  kamMStat  .  .  paili  aya \zjmä  Aaraiti  6ari  Yt.  if/.i;  lo.gS,  tj.gy, I*V.<).IS,  V.5.4,  7-^54. '*Y./2.3;  —  raikö '  (sd.)  .  .  haca  ariAs  (als  Abi.))  z
2459:sSmaidf  Y.  jG.  I ;  —  ahmya  zaoi^re  imat  us  haca  aiihyS  nmänaiibyS  ..N. ^.-^^L-j^- barfsma  äyae  yäti  Y.  2-i;  aE,  Vr.2. iff.;  parö  ibisyanbyö..  a^^am  ibaisattuhatqmXx.
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■
2464:yat  baväma  aiwi.vanyn  dänavö  . .  ahmi gal'ie  piianähu  Yt.5.73;  —  ahmäi  J/ri- n?nti .  ./ravalayö  buyiil  ahmi  nmäne  giusia va^wa  ..  ". .  dem  . . ;  in  dessen  Hause  . 
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5;
```


## [2026-09-14T01:57:00.356Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==237' KNT.txt | grep -n \"LEXICON\\|hacā\\|haca\\|Haxāmaniš\\|Haxamanis\" | head -20"
}
```


### [2026-09-14T01:57:01.441Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:57:01.694Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"haca\" BRT.txt | awk -F: '{print $1}' | while read l; do sed -n \"${l}p\" BRT.txt | grep -o \"^.\\{0,120\\}\"; done | grep -i \"praep\\|Abl\" | head"
}
```


### [2026-09-14T01:57:06.481Z] TOOL RESULT

```
—  tiärTm..y!f  avaf,at  frafasüiie  xssi>nyat "his  (lies  hacaf)  'säy.V  (AblS.)'>  Vti'.as'i
vamm*jas»ittim^^  ahmya  nmariey. 13.22;  (.Aal'a  mit  AbL):  6a%a  alaum  apa.jasS — yh  (näml./z'aj'a.fflj'J)  *qfrSj
i)  '(den  Gürtel)  lösen  sva.  ablegen': yasca  . .  aiwyänhantvt  vä  aiwyäahayamnö aiwyatfhatum  vd  ds/ayamn^  "..d
{hai'a  mit  AbL):  astS.vi}>Stus  .  .  yakmat haca  nailis  bunjayät  .  .  mafyänqm  nsit afiirapatays ..  "Ä.  ..,  
-holen  aus  — '    {haca  mit  AbL):    m  kaca  äpisim    (Sp,  329  m.)    paräbar^    Bb.    i.
—  AblSm.,!!,:  vazrpm..yaAmat  /laca/ra- tpnsaili  ar»rS  mainyul  Yt  10.  97;  97J,  7  y. 87,  Aog.  5<¥;  —  hukair
'entlassen  aus  — '  (Aaca  mit  AbL):  aprm zatäAi  tum  . .  zrayanhai  haca  vourukasät ^'  5-  '  S  >  ' —  äp9m
```


## [2026-09-14T01:57:09.093Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"LEXICON 21[0-4]\" KNT.txt | head"
}
```


### [2026-09-14T01:57:09.148Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:57:10.228Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"hacá- \\|haca- prep\\|hacā- prep\\|‘from’\" KNT.txt | head -20"
}
```


### [2026-09-14T01:57:10.303Z] TOOL RESULT

```
900:*apo, OP prefix apa-, Skt. dpa, Gk. ёто ‘from’,
2731:A. With Ласӣ, to express the various ‘from’ E |
2870:‘after, behind me’ (DB 3.82). hacà ‘from’, with ablative of noun or pronoun, or
4912:а adv. as prefix and prep. ‘to’; Av. Skt. à, prep. with acc. and abl., ‘to, as far as’ (also with other uses and meanings); pIE *à if = Lt. à ‘from’ (Sturtevant, Lg. 15.145-54), or *0 if = Gk. ó- in ó-xeayós ‘(lying round about), ocean’.
```


## [2026-09-14T01:57:14.882Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Achaemenes\\|Haxamanis- \\|Haxāmaniš- \\|hacá prep\\|hacà prep\\|hacā prep\" KNT.txt | head -20\necho \"---- context near end lexicon h\"\ngrep -n \"haruva-\\|hadis- sb\\|hamaranam\" KNT.txt | head"
}
```


### [2026-09-14T01:57:14.954Z] TOOL RESULT

```
1262:a golden helmet’. тауйга- *door-knob', Skt. mayükha- ‘peg’. havd- ‘friend’ m Haad-mani§ ‘Achaemenes’, Skt.
1879:‘Having the mind of a friend, Achaemenes’ has a
3434:$1. 1-4. Ariaramnes, the Great King, King of Kings, King in Persia, son of Teispes the King, grandson of Achaemenes.
4818:Darius and the other Persian Kings who have left us cuneiform inscriptions composed in Old Persian, all belonged to the Achaemenian line, so called because they were descended from Achaemenes. Full information may be found in PW 1.200-204 s.v. Achaimenidai, and under the names of the individual persons? a complete gene-
4838:a, States that there had been eight kings in their family before him, and that he was the ninth in order. We must count them thus: 1 Achaemenes, 2 Teispes, 3 Cyrus, 4 Cambyses, 5 Cyrus the Great, 6 Cambyses, 7 Ariaramnes, 8 Arsames, 9 Darius. The last three belong to the younger line of Áriaramnes, while Nos. 3 to 6 belong to the line of Teispes' older son. Hystaspes father of Darius is not included in the count, because he nowhere receives the title of King, even when mentioned as father of Darius—whereas the other kings all give to their fathers the title King in statements of parentage.
4839:Herodotus 7.11, however, gives Darius’ line thus: Achaemenes, Teispes, Cambyses, Cyrus, Teispes, Ariaramnes, Arsames, Hystaspes, Darius: in which Darius is the ninth. But Darius surely knew his own genealogy better than did Hero- dotus. Herodotus either has a dittographie error made in copying from a list covering both branches, or erroneously looked upon Cambyses and Cyrus as ancestors of Darius and inserted Teispes the second time to make the list agree with the known fact that the father of Ariaramnes was named Teispes.
---- context near end lexicon h
607:II. For OP -атш- we find the following ex- amples: haruva-, once written fra-haravam; Skt. sárva-
1346:§107. PIE 1 became pAr. r, and therefore was indistinguishable from pIE r in the Aryan lan- guages, unless a cognate from another ТЕ branch can be adduced. pIE *selyo- ‘all’, OP haruva-, Av. haurva-, Skt.
1412:OP haruva- ‘all’, Skt. sárva-.
1694:Skt. sam-aranam, OP hamaranam; but with pre- fix, ufhamaranakara, with double writing of the initial, $ being the value after u, and A being the value when initial in the separate word. Perhaps also OP PatiSuvart§ for Рай- Swart, see Lex. s.v. Cf. Reichelt, Aw. Elmb. $103, for the same phenomenon in Avestan.
2240:pronominal antya-, haruva-, һата, $203; for the
2298:(1) Semi-pronominal adjectives: aniya- ‘other’, haruva- ‘all’, hama- ‘one and the same’.
2353:П. OP haruva- ‘all’ (Av. haurva-, Skt. sárva-) has nsm. haruva; asn. -haravam in adv. fraharavam (with irregular writing of -rv-, $26); Isf. haruva- hydyd, upon fem. stem haruvahyà- formed to gsm. *haruvahyd, Skt. sdrvasya (haruvahyaya is a defec- tive writing not indicating the length of the vowel), ef. Isf. ahyayà (8199).
2654:B. As predicate to a nominative subject: DB 1.1 adam Dérayavaus, 1.7 vayam Hazámanikiya даһуйатаћу, 2.27 avabasém hamaranam kartam.
2672:K. To express time when, as їп the adverbs paranam and paruvam ‘formerly’, and with the postposition pakiy: DB 1.20 xsapavd raucapativà ava akunavayata ‘either by night or by day, that was done’; DB 2.61f Güravaharahya mahya jiyam- nam patiy avat sam hamaranam kartam ‘on the last of the month Thuravahara, then by them the battle was fought’.
2949:(b) to express purpose, with verbs of motion: only in the phrase hamaranam сатіапату ‘to make battle’ (DB 1.93f, and 10 other oc- currences), depending upon @# ‘he went’, paraua (pl. ptc.) ‘they went forth’, јла ауа ‘he sent forth’.
```


## [2026-09-14T01:57:20.889Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"LEXICON\" KNT.txt | tail -20"
}
```


### [2026-09-14T01:57:20.950Z] TOOL RESULT

```
4971:LEXICON
5017:LEXICON
5062:LEXICON
5105:LEXICON
5153:LEXICON
5201:LEXICON
5246:LEXICON
5305:LEXICON
5351:LEXICON
5403:LEXICON
5448:LEXICON
5504:LEXICON
5546:LEXICON
5589:LEXICON
5636:LEXICON 195
5678:LEXICON
5712:LEXICON 199
5744:LEXICON
5783:LEXICON 203
5833:LEXICON | 205
```


## [2026-09-14T01:57:23.729Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5833,5900p' KNT.txt | grep -n \"hacā\\|hacà\\|hacá\\|Haxāmaniš\\|Haxamanis\\|haxā\\|havá\" | head -20\necho \"=== raw tail\"\nawk 'NR>5860 && NR<5920' KNT.txt | cut -c1-400 | head -60"
}
```


### [2026-09-14T01:57:24.854Z] TOOL RESULT

```
=== raw tail
rüsla- adj. ‘straight, right, true’, with nt. as Sb.; ріс. of ?^rad-: Av. réSta-, Turfan РЫ. тай ‘true’, Lt. réctus ‘straight’, pIE *rékto- (593, §93.- n1-2, $106, $122, 5126, $24211). Cf. arštā-. таӣз- iam asf. DNa 59. rdstam usn. DNb 11; asn. DNb 7.
‚ .. rlaryary, see vart-.
Labandna- (or Labnàna-) sb. ‘Lebanon’ (§6, §107), 2 mountain in Syria famous for its cedars. Labanéna nsm. DSf 31.
-vä encl. conj. ‘or’ (8133, $291.11); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See also Vidafarnah-. vainümiy lst sg. (4226.1) DNb 36, 36f, 39, 40. avaina imf. DB 2.76, 90; DNa 32. vainataiy mid. as pass. (8235.1) DNb 2; XPa 16
vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
```


## [2026-09-14T01:57:31.119Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nwc -l KNT.txt; awk 'NR>5930' KNT.txt | grep -n \"haca\\|Haxā\\|Haxa\\|haxā\" | cut -c1-300 | head -20"
}
```


### [2026-09-14T01:57:32.051Z] TOOL RESULT

```
5868 KNT.txt
```


## [2026-09-14T01:57:38.755Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ntail -3 KNT.txt | cut -c1-300\necho \"=== L1262\"; sed -n '1258,1264p' KNT.txt | cut -c1-800\necho \"=== L1875\"; sed -n '1875,1884p' KNT.txt | cut -c1-900\necho \"=== L2865\"; sed -n '2865,2875p' KNT.txt | cut -c1-900"
}
```


### [2026-09-14T01:57:38.856Z] TOOL RESULT

```
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
=== L1262
So also other instances of k and c in OP, though many of them are in words with very scanty etymological parallels, and others are obvious borrowings from other languages, such as mashd- ‘inflated skin’, Караша ‘Cappa- docia’, К@$а- ‘ethiopia’.
Where pAr. k stood before varying vowels, there may be variation in the products (as in the forms from root kar-), or one value may be generalized: OP rauca from nom.-acc. pIE *leugos, with c from oblique cases, where pIE had *leuges- (cf. Gk. yévos y&veos, Lt. genus generis).
$100. PAR. kh seems to appear in a few words, which have no far-reaching etymological con- nections: yaudd- ‘cap’, also in dgraxauda- ‘wearing the
pomted cap’, ef. Av. zaranya-ruoda- ‘wearing
a golden helmet’. тауйга- *door-knob', Skt. mayükha- ‘peg’. havd- ‘friend’ m Haad-mani§ ‘Achaemenes’, Skt.
nom. sdkha.
Also the place-name Rard, personal names Arra and Sku"ra, and the doubtful words Xarša- dasya and Hadaraya; see Lex. s.vv.
=== L1875
$168. OTHER Noun AND ADJECTIVE STEMS END- ING IN CONSONANTS are to be found listed among Root Nouns and Adjectives, $142.
5169. Noun AND Apsective COMPOUNDS IN ОР, apart from phrasal adverbs (§191.1V), may have as prior element an inseparable adverb as in a- zsata- ,"u-cüra-, dus-iydra-, ham-arana- (8268); or a prepositional adverb, as in apa-dàna-, pati-kara- (5268); or a noun or adjective stem! They have as second element a noun or adjective stem, which may receive an additional suffix.
Only compounds of stem + stem will be here discussed. Either stem may itself be a compound; either stem may already have one or more suffixes. The initial syllable of the first element, especially in adjectives, may show vriddhi or lengthening of the vowel, as in dáraniya-kara- ‘gold-worker’ to daranzya- ‘gold’; less often this appears in the sec- ond part, as in Baga-yadi- 'god-worshipping (month)’, where it is seen in both parts, and in asa-bàra- ‘horse-borne’, where it indicates passive meaning.
Compound adjectives with second elements of a specific gender assume the genders of their de- rived meaning and use, with change of form if necessary. Thus the masc. name Hazd-manis
‘Having the mind of a friend, Achaemenes’ has a
neuter stem as its second element, used without change in the masculine adjective as noun; the masc. adjective tigrarauda- ‘wearing a pointed cap’ has as second element the fem. zaudà- ‘cap’.
Derivative adjectives to compounds may be made by the addition of suffixes; Haxamanis-iya- ‘Achaemenian’ to Hazámanis-, Asagart-iya- ‘Sa- gartian’ to Asa-garia-.
Compounds of stem + stem, so far as they oc- .
cur in OP, may be divided into (1) Determinative Nouns and Adjectives, dependent and descrip- tive; (2) Possessive Adjectives, dependent and
! In Cica-tazma- the prior element is not the bare Stem, but the stem with an added nasal, attested in the transliterations into Elam., Akk., and Greek. This nasal ean hardly be the acc. ease-ending (as tentatively sug- gested by Bthl. AiW 587); it seems unexplainable except as a transfer from some other ера, in which & nasal in this position was justified (Schulze, KZ 33.216.n3; Richter, IF 9.208-4; Foy KZ 37.504-5). Cf. Gk. 'Aprga- Bápys (Hdt. 1.114-6, 9.122; Aesch. Pers. 29, 302, 971) = OP *Artam-bara ‘Aria-upholder’, where the prior ele- ment seems to be in the accusative (ef, Stonecipher, Graeco-Persian Names 27).
=== L2865
patiy (DB 2.76, 91; 3.52, 92), temporal ‘during’
with genitive and accusative in z$apa-và rauca- pati-vd (DB 1.20), with accusative in |pa]tiy a[va]mc ctam] bardam (DB 5.2f).
pasd ‘after’, with accusative of time in pasd tanüm
‘after himself’ and in the phrasal adverb pasáva
‘after that’; with genitive of place in pasd mand
‘after, behind me’ (DB 3.82). hacà ‘from’, with ablative of noun or pronoun, or
ablatival adverb; occasionally with nouns of lo-
cative or instrumental form (once with an an- acoluthie nominative phrase, DZec 9, and once with an accusative enclitic pronoun as invari- able, which it follows, DB 1.50). It governs place-names as the starting-point from which there is motion or action (DB 3.80) or exten- sion (DPh 5, 7) or separation (XPh 16); names of persons of whom fear is felt, from whom com- mands proceed (= agent), from whom rebellion takes place, from whom something is taken away (DB 1.61); adverbs of time as starting- point; names of persons and things and ab- stracts from which protection is to be given
(DPd 161, etc.).
$272. Tue Voices or THE Vers in OP include forms of the active, the middle, and the passive; but the meanings are not in all instances typical of the voice-forms.
8273. Tue Active Forms have the usual mean- ings of the active voice; but they are sometimes replaced, without difference of meaning, by middle forms (§274.b).
```


## [2026-09-14T01:57:54.533Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad 2>/dev/null || cd /tmp\ncurl -sL --max-time 120 \"https://archive.org/download/oldpers/oldpers_djvu.txt\" -o knt-440.txt; ls -la knt-440.txt; grep -n \"Haxamanis- \\|haca prep\\|hacā\\|Haxāmaniš\" knt-440.txt | head"
}
```


### [2026-09-14T01:57:57.837Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 944060 Sep 13 21:57 knt-440.txt
19752:ll : Haxāmanišiya 
20637:2 üvnàm : Vistispahya : puça : Haxāmanišiya : 
20812:9 haus : XShya : puça : Haxāmanišiya : 6atiy : X 
29549:haca prep. ‘from’: GAv. hacà, LAv. hacá, Skt.
```


## [2026-09-14T01:57:59.441Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /tmp; sed -n '29500,29600p' knt-440.txt"
}
```


### [2026-09-14T01:58:00.513Z] TOOL RESULT

```
Exit code 2
sed: can't read knt-440.txt: No such file or directory
```


## [2026-09-14T01:58:02.449Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; sed -n '29520,29600p' knt-440.txt"
}
```


### [2026-09-14T01:58:02.503Z] TOOL RESULT

```
cf. Hz. AMI 4.133, 8.31-4). Hazümanisiya пзш. 
AsH 4; CMa 2; CMb 2°; CMe^; DB 13; DBa 4; 
DPa 5; DPb; DPe 5; DPh 3; DNa 13; DSb 11; 
рва 2; DSe 12; DSf 7f; DSg 2; DSi 2°; DSj 2; 
рек 3; DSm 2; рву 3; DZb 6; DZc 6f; DE 20; 
DH 2; XPb 20f; ХРе 9; XPd 14; XPe 4; XPf 
14f; XPh 12; ХР]; XPk; X8e 2; XE 20; XV 
15f; A'Pa 16°; АЛ; D'Sb 2; A?8e 1; A’Sdb 2; A*Ha 
5; А?НЬ; A*Hc 15; A*Pa 20f; Wa 7f; Wb 8f; We 
Of; Wd 9. Hārämanišiya (653) XPa 10f. 
Натбтаті уа (822) DSa 2f; A?8da, dc 2. Haza- 
màán*&ya ($22, $51) А683.  Hazümanisiyà npm. 
DB 1.7; DBa 10. 


Ha"gmatàna- sb. ‘Ecbatana’, a royal resi- 
dence in Media: Elam. ag-ma-da-na, АКК. a-ga- 
ma-ta-nu, Gk. (Hdt) 'АуВатара, (Aesch., 
Aristoph.) "ExBarava, NPers. Hámádàn. Prob- 
ably deriv. of ha-gmata- (q.v., under gam-; §103.- 


OLD PERSIAN 


IV, $147.11): ‘City of Gatherings’. Hagmatànaty 
ism. DB 2.76, 77f. 


haca prep. ‘from’: GAv. hacà, LAv. hacá, Skt. 
sácã ‘with’ (on meanings, see Fay, JAOS 31.403- 
12): instr. sg. of thematic root-noun to pIE *seg*- 
‘follow’, Av. hacaile, Skt. sdcale, Gk. rerai, Lt. 
sequitur, Gr. satan ‘see’ (890). Syntax $271. 

(1) With abl.: DB 1.36, 40, 61; 2.64; 3.2, 26; 
4.37; DPd 11, 16, 17 bis; DPe 20; DNa 18, 46, 52; 
DSe 17, 38; DSf 31, 34, 35°, 35, 36, 38, 39, 41, 42, 
48, 44; DZe 7, 10, 11; XPh 16, 57; Аа 5^; A?Sda 
4 (hada de 4, §49b); A*Ha 6°. hacá-ma DB 1.19, 
28; 2.6, 12, 16, 98°; 3.27, 78, 81; 4.92; DPe 9; 
DNa 20; DSe 19°; XPh 18. 

(2) With loc. form as abl.: DPh 7; DSf 33, 44; 
DH 5. 

(3) With instr. form as abl.: DPh 5; DH 4. 

(4) With ablatival adverbs: Ласі avadasa DB 
1.37; 3.42, 80; DSe 47f°; ПЕ 47. hacà paruviyala 
DB 1.7, 8, 45; DBa 11, 12. [hacá-ci]y dūradaša 
DSf 23. 

(5) With preceding encl. pron. in acc.: -šim 
hacé DB 1.50 (Bang, ZDMG 43.534; Ву. BSLP 
31.2.64-5). 

(6) With anacoluthie naming-phrase in nom.: 
hacà Pirdva пата таша DZc 9. 


ha”j- vb. ‘hang’: Skt. safj- ‘fasten’, pres. 
зан. 
fra- + ha"j- ‘hang out’ for display (Foy, KZ 
35.39), namely the rebel’s skin, stuffed with straw 
(König, RuID 73-4; wrongly ‘imprison’, Sen 45): 
frahajam 1st sg. imf. ($213) DB 2.78. 


had- vb. ‘sit’: Av. had-, Skt. sad-, Lt. sedet, 
NEng. si. See also hadiš, and possibly 
Vistaspa-. 
ni- + šad- ($117), caus. ni-$adaya- (476.1, 
$122, 8123.2, $132.23, $215) ‘set down, establish’: 
niyasadayam (4226.11) 1st sg. imf. DNa 36. nisà- 
dayam (528.1, $140.11) XPh 34f (cf. Hz. AMI 
8.65, ApI 180-1). 


Һай prep. with instr. ‘with’: GAv. hada, 
LAv. haóa, Skt. sahá, pIE *sm-dhe (§11, $67, §76.-
```


## [2026-09-14T01:58:07.649Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; sed -n '29480,29522p' knt-440.txt; echo \"=== page marker\"; grep -n \"LEXICON\" knt-440.txt | awk -F: '$1>29300 && $1<29700' | head"
}
```


### [2026-09-14T01:58:08.628Z] TOOL RESULT

```
varga npm., DNa 25; DSe 24f^; XPh 26; аз nsm. 
(856.IIT), A?P 14. 


hauvam pron. ‘he’, nsm. DB 1.29: haw (q.v.) 
+ -am from adam, tuvam, etc. (§48, §137, §196). 
Cf. MB Gr. §158. 


hakaram adv. ‘once’ ($191.TIT, $9041): Av. 
hakarat ‘once’, Skt. sakft, cf. Gk. á-rat, Lt. sem-el; 
ha- (q.v.) + *hyt ‘time’ (cf. Lith. kaftas ‘time’), 
remade to -karam after kara- ‘maker’ (Hz. Apl 
181). Cf. also Ву. Gr. $323. hakaram-ciy DNb 
34f. 


hakarta- (§140.V) ptc. adj., nt. as sb., ‘co- 
operation’: ham- + karta- ‘done’, past. pte. pass. 
tokar-. — [halkartahya gsn. DNb 16 (Kent, JNES 
442-8; not karrpahyd or {ulkarrtahyd, with Hz. 
Apl 233-5; not [halkarrtahyd, with dittography 
of т, with Kent, Lg. 15.170). 


Hazämanıš- sb. ‘Achaemenes’ (§161.Ib), 
founder of the Achaemenian dynasty: Elam. ha- 
ak-qa-man-nu-i$, Akk. a-ha-ma-ni-iš-', ОК. 
"Ахат. From haxd-, LAv. пзш. haza, Skt. 
nsm. sákhā ‘friend’, + maniš-, with reduced grade 
of vowel in ultima (468.11, $124.4, §156.IV, 
$185.III, n1), otherwise identical with manah- 
(q.v.). See also HazümaniSiya. НалхйтамХ 
nsm. DB 1.6; DBa 8. Hazámanisahyá gsm. (§57, 
6185.11; ef. Hz. AMI 4.183, 8.31-4) AmH 3f. 


HaxdmaniSya- adj. as sb. ‘Achaemenian’: 
adj. to preceding ($144.IIT, $159, $185.n1; hardly 
-Sya- from -łya-, as suggested by MB Gr. $262, 
cf. Hz. AMI 4.133, 8.31-4). Hazümanisiya пзш. 
AsH 4; CMa 2; CMb 2°; CMe^; DB 13; DBa 4; 
DPa 5; DPb; DPe 5; DPh 3; DNa 13; DSb 11; 
=== page marker
29337:LEXICON 
29617:LEXICON 213
```


## [2026-09-14T01:58:15.046Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW\nawk 'BEGIN{RS=\"\\f\"} NR==62' ZAW_pages.txt | head -50"
}
```


## [2026-09-14T01:58:15.872Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW\nawk 'BEGIN{RS=\"\\f\"} NR==266' ZAW_pages.txt | head -50"
}
```


### [2026-09-14T01:58:16.178Z] TOOL RESULT

```
38                             Ch . Bartholomae,

 lebendig' 35, 48, 65, bavandag 'vollkommen', savgand 'Eid'
81, 312, pand 'Rat' 24, 52, 'abgand 'hingeworfen 81 ; 39, 77,
'andar innerhalb 16 u. ö., u. a. m., endlich die 3. Plur. parî-
stand 86, padîrand 86, ' êstand 1079, 'istâyand 69 ; s . S. 37
No. 3, unter 3.
       § 16. 2) vor rd :
                      C



      kêrd, qêrd gemacht 12 u. ö.¹), kêrdan machen' 85, 91,
kêrdag, qêrdag 'Tat' 862 u. ö., frašêgêrdîy, gêrdîg 49 ff.2) ; man
vergleiche zur Wurzelsilbe des bp. 11515 kartan, Paz. ‫وو‬         ‫وس‬
kardan, np. ‫ کردن‬kardan BARTHOLOMAE IF. 8. 253, SALEMANN
GIrPh. 1. 274 und zu deren Aussprache das entlehnte arm.
կերտ kert gemacht am Ende von Zusammensetzungen ; s.
HÜBSCHMANN AGr. 1. 168 ;
       yazdêgêrd ' Götterstadt' 75, SM.; vgl. dazu voNSTACKELBERG
Oss . Erzähl. 82, MUNCKASI Revue orient. 1904. 318, BARTHOLOMAE
AirWb . 448 ;
     hašâgêrd (MÜLLER gîrd) 'discipulus' 30, 32; vgl. zur Aus-
sprache die Pazandwiedergabe von bp. 119          oder ‫س دام‬
durch_
     ‫دسمو‬            sowie das entlehnte arm. muhtpır ašakert ; aber
im Np. wird ‫ شاگرد‬sagird gesprochen. In der Annahme, daß
dash der mpT. Wortformen etymologisch berechtigt ist, nicht
sekundär, setze ich uriran. * hašākarta- an, d. i. eigentlich der
mit der Wartung, dem Dienst des Priesterkollegen oder Priester-
kollegiums zu tun hat', eine Zusammensetzung aus *haxai- (jAw.
                                                                    von
unter einmal nach y, s. § 65, zweimal am Zeilenende, s. oben S. 26
den Handschriften im Dialekt sehe ich dabei allerdings ab -, sodann daß
neben -ênd auch -êênd vorkommt, s . nâzêênd neben nâzênd 69, hamnihêênd 19
    beide freilich am Zeilenende , s. oben S. 26 mit Note -, endlich daß in der
3. Sing. neben zahlreichen Formen auf -êd der Ausgang -ad nur in qûnad
11 , 12, kunad 100      hier am Zeilenende, s . S. 26 ; darum ist auch der Vokal
der ersten Silbe nicht geschrieben —, 'abrasad (?) 1081 , sowie in patâyad 33,
nimâyad 93, 1078    in beiden Fällen hinter y ; s. dazu § 65             belegt ist,
ē und nicht e zugewiesen werden muß .
            4. zîndag lebendig' 47, 55 u. ö., das aus zīvand (s . zîvandag 35 u. ö.)
zusammengezogen ist.
       1) kard oder qard ist überhaupt nicht bezeugt, daher MÜLLERS Er-
gänzung 21 Z. 5 nicht ganz richtig.          Statt padašqîrd 16 ist padišqêrd zu
schreiben, s . MÜLLER 110.
       2) Bd. S. 46 Z. 4 der WESTERGAARD SChen Ausgabe steht ‫لاسود ودامه‬
fraškirt.
```


### [2026-09-14T01:58:17.217Z] TOOL RESULT

```
242                         Ch . Bartholomae,

      ‫ دود‬hakirč oder die hakure sind mir nicht deutlich. Man
   verlangte hkyrj statt ḥkryj ; allein die Zeichen sind
   ganz deutlich auf dem Faksimile zu erkennen.

     Sp. 1744, Z. 33 und 43 ff. füge in den Noten zu jaw.
haxay- Freund' und zu ap. haxāmaniš- EN. hinzu : Vgl. mpT.
hašâgêrd, np. šāgird 'Schüler'.
         S. oben S. 38 f., 158 f. und 226. Man beachte das auch
      zu Sp. 238 m.

        Sp. 1754, Z. 41 f. füge in den Noten zum airan. Verbum
had- 'sitzen' hinzu : mpT. nišîyând 'sie werden sich setzen' M. 21 .
      Das Wort zeigt die selbe Präsensbildung wie das jAw.
   nišhidaiti oder auch wie das ai. níşīdati, indem es ar. * ni
      šīdānti fortsetzt ; s . a. O. No. 3.

        Sp. 1756, Z. 15 füge in den Noten zu ap. hadā zusammen
mit' hinzu : mpT. 'ad.
         Das mpT . Wort findet sich bei MÜLLER 16, 23, 352, 42,
   54, 66, 68, 83, 1082 an zum Teil undeutlichen Stellen. Not-
   wendig ist die Zusammenstellung mit dem ap. hadā nicht.
   Vielmehr spricht d eher für iran. t, und diesem Ansatz steht
      auch oss. äd nicht entgegen. Dann ließen sich mpT. 'ad,
   oss. äd mit griech. μετά verbinden; vgl. μέχρι und ἄχρι bei
   FICK BB. 5. 168, BRUGMANN GrGr.3 548.1)
        Sp. 1759, Z. 40 f. füge in den Noten zu jaw. hadō.zāta-
'leiblich' hinzu : arm. LW . harazat leiblicher Bruder'.

     Sp. 1765, Z. 13 ff. füge in Note 1 zum ap. Präsensstamm
hapariya- hinzu : Vgl. ferner JusTI IFAnz. 17. 106 mit meinen
Bemerkungen dazu, oben S. 104.
      Sp. 1771, Z. 21 ff. füge in den Noten zum gaw. Verbum
1hant- hinzu : Zu den gAw. Wörtern nišąsyā Y. 50. 2 und
hīšasat Y. 32. 15 S. SCHEFTELOWITZ ZDMG . 59. 693, 711 .
         Meine Übersetzung von Y. 32. 15 a ist nach ScH. sinnlos' .
   S. noch a. O. 714 Note .

       1) JSCHMIDTS Einwand dagegen, auf den PRELLWITZ WbGrSpr.2 292
verweist, Sonantentheorie 152, gilt mir nicht für stichhaltig .
```


## [2026-09-14T01:58:33.529Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 33 (p.12)\"; awk 'BEGIN{RS=\"\\f\"} NR==34' HRN.txt | head -40"
}
```


## [2026-09-14T01:58:34.295Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 171 (p.150)\"; awk 'BEGIN{RS=\"\\f\"} NR==172' HRN.txt | head -40"
}
```


### [2026-09-14T01:58:34.616Z] TOOL RESULT

```
=== HRN leaf 33 (p.12)
12 -
49. äniurzlden Verzeihen', ämarzis^ amurzlst (Qiss. Dan.).
aw. ä+i/'marz', ämarezen; iphlw, ümurzUan, ämurz(i)sn,
ämurzltär Verzeihen' ; ai. ä -j- [/'marj- Vegwischen .
Vergl. wa/. namurzg, sar. namüzg 'Rechen, Besen.
Im Awesta und Altindischen wird die Bedeutung
gnädig sein, verzeihen' durch das Wurzeldeterminativ
d aus der [/^merg- ^abwischen' gewonnen, vergl. aw.
merezdätä, meresdika-, ai. m^ddti (Bartholomae BB. 13,
87, während Brugmann, Indog. Forsch. I, 171 auch
an ai. mfsyate Vergisst*, lit. mifsztl Vergessen denkt).
50. iimö^ten lehren, lernen*, Praes. ämöz-em, amözis,
phlv. ämö/tan lehren', ämöc-am, amöc(i)sn^ ämöölmtan ;
lit. mokinü „wohl auch faktisch 'lehren*, eigentlich zum
können bringen" (Kurschat), moJdnus (refl.) 'ich lerne'.
Die Zusammenstellung stammt von Spiegel (Tradit.
Lit., 360) ; sie ist indess lautgesetzlich unmöglich, da
lit. (d. i. ö) arischem ä entspricht. Skr. ä + [/"muC'
heisst nur ^bekleiden*.
51. ätney(ten 'mischen , Praes. ämez-em, ämezis^ ümeze, ämey,
vergl. enduh-amey (Vis und Rämin, Seite 83 Vers 16).
phlv. ame/tan, ämeßt (Bund.) mischen*; aw. vergl.
hememyäsaite *sie mischen sich zusammen', minas *du
vereinst' (Bartholomae, Ar. Forsch. III, 61 Anm.;
II 170); skr. a-\- l^miks- f mischen*), vergl. ^miisä-
'Quark', neben ai. migrä- Vermischt*; vergl. gr. ulyw^u^
/List^ai etc.^).
52. an jener*.
Die heutige Aussprache ün findet sich schon in der
bukhärischen Psalmenübersetzung (Et he, Litbl. f. or.
Phil. I, 191).
päz. a7i bez. hän (Aussprache für die Ideogramme
■^T und auch nöD), phlv. in an-gün, an-c.
Zu aw. a«-a, an-agäo, an-äis; skr. an-aycC, Der
Übergang von der aw. skr. Bedeutung 'dieser zu jener'
ist derselbe, wie in ksl. onü^ lit. ans, lat. ollus {*onlus) ;
^) Np. äme/ten hat mit np. meßten (No. 1006) nichts zu thun, wie
Fr. Müller, WZKM. 5, 351 will.
```


### [2026-09-14T01:58:35.772Z] TOOL RESULT

```
=== HRN leaf 171 (p.150)
- 150 —
LW. zoh *Opfer ; ai. hoträ- *üpferhandlung, Opfergabe';
arm. vergl. jaimem Veihen, darbringen, opfern', jauni
TsXia(fo()og (H. No. 181).
676. zös 'zornig, grob*.
aw. zöismi' *unrein (nach Justi); arm. LW. (?) zös
*hässlich'.
Die Zusammenstellung ist sehr problematisch, wahr-
scheinlich sogar falsch; aw. zöisnu- ist unsicher
(v. Bradke, KZ. 28, 297 und danach Bartholomae
BB. XV, 11 Anm. 1 nehmen es zweifelnd als
glühend', während Geldner; KZ. 30, 524 es mit
zitternd' übersetzt — dazu s. aber Bartholomae,
Indog. Forssch. I, 191 Anm.).
677. zih 'Bogensehne*.
Käs. zeh, ze,
aw. jyd' 'Bogensehne; Sehne* (yt. 10, 70, Geldner,
KZ. 30, 514); ai. i^a-.
kurd. zih 'Bogensehne*; af/. za-l^ bei. j%y (177).
Urform von zih ist "^jtjaka-,
678. zehr 'Gift*, zehre 'Galle*.
phlv. zahr 'Gift* (Men.), arm. LW. zahr,
kurd. zahr, zäir, zur 'Gift' ; af/. bei. (297) LW. zahr,
np. zehre 'Galle' aus aw. *zartaka- ('gelb'), ^zad^raka-,
phlv. "^zahrak und identisch mit zehr 'Gift* nach
Nöldeke, Pers. Stud. I, 38, gegen Justi und
Hübschmann's sonst sehr ansprechende Erklärung
des letzteren aus aw. ^Jadra-, ai. Viatra- 'Mittel zum
Tödten* (Kurd. Spiranten, S. 21 bezw. ZDMG. 38, 424).
Und aw. zaras[ca (ZPGl.), das doch sicher 'Galle', gr.
X^^Vy ist?
679. :iiyän 'Schaden'.
aw. zyana- 'Schaden*; phlv. zi(y)an (talm. Nr"»T;
mand. Xi"»NT) ; skr. (Brähm.) jfydna- 'Bedrückung'.
LW. kurd. af/. ziyän; bei. ziyänl (307); oss. ziän,
d. ziän ; arm. zean,
680. zer 'unten, unterhalb*.
Käs. jir (Vullers jBr, Jerü), zer,
aw. haca + aöairi\ päz. az^r, vergl. phlv. er\tan 'mild',
```


## [2026-09-14T01:58:42.965Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"az 'von\\|az \\`von\\|az ‘von\\|hačā\\|haca-\\|'ab, von\\|az.*von'\" HRN.txt | head -20\necho \"=== search az entry\"\ngrep -n \"^[0-9]*\\. *az \" HRN.txt | head"
}
```


### [2026-09-14T01:58:44.084Z] TOOL RESULT

```
=== search az entry
```


## [2026-09-14T01:58:46.091Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==33' HRN.txt | head -45"
}
```


### [2026-09-14T01:58:47.268Z] TOOL RESULT

```
- 11 -
44. äleyten 'springen, ausschlagen (vom Pferde)*, Praes.
alezed^)^ alezende^ alezTden^),
got. laikan springen, hüpfen*, laiks Tanz'; lit. laujytl
*wild umherlaufen (von jungen Pferden, Rindern auf der
Strasse)*; air. löeg 'Kalb*, (bei Feist).
kurd. helezium 'ich tanze*, lizim 'ich spiele', Inf.
leiztin.
Die Etymologie stammt von Justi, Dict. kurde-
frangais.
45. ätnäj 'Pflugsterz'.
g. matk (Houtum-Schindler, ZDMG. 36, 70).
arm. mac (de Lagarde No. 1413, Htibschmann
No. 186).
Die Lautverhältnisse von äinaj und mätk passen
nicht zu einander (vgl. auch Bartholomae, Studien
II, 24).
46. ümäden 'zurecht machen, rüsten*, ämUden, Praes.
ämäy-em, ämüy-em,
ap. vergl. ämäta- erprobt*; aw. ämata-, ämayäont^^
sie sollen sich versuchen',
oss. t. amain 'erbauen' (176).
47. äniär 'Berechnung', ämäre,
aw. a + 2 l^mar- 'sich erinnern'; phlv. amär 1) 'Zahl'
2) 'zähle, rechne* (das Verbum ämartan ist nicht belegt) ;
skr. a + V^smaV" (nicht belegt).
48. ätneden 'kommen*, Praes. äy-em (s. No. 60).
ap. ä+ [/^gam-, äjannya 'er käme*; aw. ci+ [/'(/am-,
ägemat; phlv. nrntan, ämatan (PPGl.) ').
Mit Mahjalvokal (FJ.).
^) FR hat einen Beleg aus Siräj eddin:
(Metr. Xeftf)
tie/s^ cun ser^ gesf bestezed
tevsen-äsä beher süy älezed.
*) Beiläufig bemerkt, findet sich bure als Imperativ *komm* ausser
im Kurdischen (Houtum-Schindler) und bei Shukovski dialektisch
auch bei Bäbä Tähir *Uryän aus Rei (Huart, Journ. asiat, Si^me s^rie,
vol. VI, 519).
```


## [2026-09-14T01:58:51.410Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"azer\\|az\\^r\\|az&r\\|azêr\\|azer\" HRN.txt | head -10\necho \"===\"\ngrep -cn \"\" HRN.txt\ngrep -n \"\\baz\\b\" HRN.txt | head -20 | cut -c1-160"
}
```


### [2026-09-14T01:58:51.499Z] TOOL RESULT

```
1821:1466. bäzär 'Markt', bazargan, hazergän Kaufmann'.
5999:aw. haca + aöairi\ päz. az^r, vergl. phlv. er\tan 'mild',- 151 -
===
23314
643:.^^x^^ aw. äzäta- *frei, edel*; phlv. azät, arm. LW. azat,
646:20. äzär Xeid*, azärden^ azdris; äzerden^ äzerm^).
647:aw. a + [/'zar-j azärayeiMi sie peinigen' ; phlv. äzär,
1046:Käs. ezü^ azün, ajiyd, ajiyd, mit Ausfall des r, wie
1101:kurd. az, ze, z-; af/. ;'-; bei. a(f, as (1); wa/.,
1108:arm. azdahak beweist, dass im Mittelpersischen az-,
1112:aw. azi' 'Schlange'; phlv. az; ai. ähU; arm. ?i'^);
5999:aw. haca + aöairi\ päz. az^r, vergl. phlv. er\tan 'mild',- 151 -
11540:az 18.
15432:az 18.
19374:/azür 486.
```


## [2026-09-14T01:58:55.735Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1085,1115p' HRN.txt"
}
```


### [2026-09-14T01:58:55.788Z] TOOL RESULT

```
wohl nur verschrieben); ai. vergl. räjas-.
73. evff 'Castell, Citadelle'.
phlv. arkpatj nDp'?&* (Talmud) und weitere Formen
bei de Lagarde, Semitica I, 43; vergl. auch Nöldeke,
Tabari-Ubersetzung, 5, 111.
lat. arx, arceo, vergl. gr. doycew; arm. vergl. argel
'Hinderniss', argelum 'abwehren* (H. No. 38).
74. erm 'Arm' (nicht belegt, nur im BQ).
aw. aremö\suta' 'mit dem Arm geschleudert'; ai. irma-
'Arm, Vorderbug'; got. arms.
wa;^. yurm 'Vorderarm*; arm. armukn 'Ellbogen'
(H. No. 45).
eren *Elle' siehe ären (No. 14).
75. ez von, aus' etc., z% z-,
gel. ju köi {r= ez kujä),
ap. hacä; aw. haca; phlv. aj; ai. sdca,
kurd. az, ze, z-; af/. ;'-; bei. a(f, as (1); wa/.,
sar. z- etc.
1) Vgl. Bartholomae, BB. 10, 274.
*) Vergl. aber Bartholomae, Ar. Forsch. I, 119.
^) Bedeutungsübergang etwa: finster — höllisch ~ zornig.- 19 --
76. ezdehä 'Drache'.
aw. azis dahakö; phlv. aze dahäk, arm. LW. azdahak.
arm. azdahak beweist, dass im Mittelpersischen az-,
nicht a/- gesprochen wurde; in jüd.-pers. xmiX ist z
nur ausnahmsweise durch i bezeichnet, während es
sonst durch T ausgedrückt wird *).
aw. azi' 'Schlange'; phlv. az; ai. ähU; arm. ?i'^);
minj. yiz selbst ist sonst im Np. verloren gegangen.
77. esp, esb 'Pferd'.
ap. Aspa[cana-, uv]aspa- fschöne Pferde habend');
```


## [2026-09-14T01:59:04.451Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD az\"; grep -n \"^az \\|azēr\\|azer \\|\\[hcdr\\]\\|hačā\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB\"; grep -n \"azēr\\|azer\\b\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-14T01:59:04.529Z] TOOL RESULT

```
=== PHD az
PHD.txt:227:azbāy- [*2b*d-] invoke. ~išn: invocation. azd [zd | = M] known. Azdahag Pcydi’k' | M ?zdh?g, (N aždahā)] a legendary ‘dragon’ king, Dahāg. azdénidan, azdén- Pzdyn-ytn'] inform. azēr [%cdl | N zér] below, under. azg [22 | N аху) branch. aziš [hcf | М *cy$, 22у] from him, it; postposition (= az) from, ~-keh [-ks] inferior, subordinate. ~-meh [-ms] superior. āz-kāmaģ [?ck’mk'] greedy. ~ih: greediness. azmüdan, azmāy- ['zmwtn!,?zm'd- | N 2~] = uzmüdan. aznawar Pzrw/l | M ?zn] noble. azraw-, v. azruftan. azray- ['zr'd-] adorn. azruftan, azraw- [)zlwp-tn! | M *zrw-] go out, be extinguished. āzurdan [Pcwltn! | N ~] = āzārdan, āzwar [?*cwl | N ~] greedy. ~ih: greed.
PHD.txt:975:below ēr, azēr.
PHD_mackenzie.txt:1428:azer [hedll N zir] below, under.
PHD_mackenzie.txt:11438:abusih; iibusih             ~\o-              aber; azer                 ~t)t
=== NYB
```


## [2026-09-14T01:59:06.516Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD hašagird\"; grep -n \"hašāgird\\|hasagird\\|hašagird\\|hāšāgird\\|ašāgird\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -10\necho \"=== HUB sagird\"; grep -n \"šāgird\\|sagird\\|schagird\" HUB.txt HRN.txt | head -10"
}
```


### [2026-09-14T01:59:06.592Z] TOOL RESULT

```
=== PHD hašagird
PHD.txt:1631:disciple hašāgird, hāwišt.
PHD.txt:3288:pupil hašāgird, hāwišt; (of eye) syahag, tidag. pure abézag, agumég, āsnūd(ag),
PHD_mackenzie.txt:6418:disciple hasagird, hiiwist.             done, be'" kirih- ; be'" with pardaxtan
PHD_mackenzie.txt:7374:pupil hasagird, hawist; (of eye)               reap drlidan.
=== HUB sagird
HUB.txt:4535:arm. aSakert 'Schiller* — np. sagird; arm. dastakert *An-
HUB.txt:6723:arm. asaJcert = np. sagird; arm. -i^r^ gemacht' = np. -gird
```


## [2026-09-14T01:59:13.687Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"hašāgird \\[\" PHD.txt | head -3\ngrep -n \"hašāgird\" PHD.txt | head -5 | cut -c1-400\necho \"=== az entry\"; grep -n \"az \\[hc\\|az \\[hc |\" PHD.txt | head -3\ngrep -n \"^awurdan\\|ayār\\|az \\[\" PHD.txt | head -5 | cut -c1-300"
}
```


### [2026-09-14T01:59:13.782Z] TOOL RESULT

```
1631:disciple hašāgird, hāwišt.
3288:pupil hašāgird, hāwišt; (of eye) syahag, tidag. pure abézag, agumég, āsnūd(ag),
=== az entry
126:read ma... N та) not. delete mādayār ... mānīg ... add house-owner.
166:~ih: wonder. àb-dàn [^5d?n!] water-holder. abdast ['5dst!] hand-guard. abdom Pfdwm | М ?bdwm] last, final(ly). ~ih: finality, end. abd-sahist [pdshst'] wonderful. abē- [5»(y)- | M ?by-, N bé] without, Jess. ~-bar [-5/] fruitless. ---bé$ [-bys] unharmed. ~-bim [-bym] fearless. ~-bimih: fea
170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?
225:ayābāģ Dy'p()£!] acquisitive, receptive. ~ih: comprehension. ayād Pbyd?t' | M? yd, N yad] memory. ~ kardan; remember. ~gar LEI | N —gàr] memoir. āyaft Pdypt' | M ?ypt, N āyift] boon, favour, gift. ayāftan, ayüb- [5?5-tn! | M *3pt,*?b-, N yāftan, yab-] obtain, acquire, attain. ayār 
316:drón yaštan: consecrate the sacrificial bread. drēš [410] mark, branding; punishment. ~ag [-k!] *desolation. drēšīdan, dro$- [d/w$-ytn'] brand. drēūšom [dlwšwm] mark. droz-, v. druxtan. drózan [dlwen! | M, J drwzn] lying, liar. ^h: falsehood. drubušt [di(w)pwst'] fortress. ~ih: defe
```


## [2026-09-14T01:59:16.633Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -on \"hašāgird[^.]\\{0,80\\}\" PHD.txt | head\ngrep -on \"az \\[hc[^]]*\\][^.]\\{0,60\\}\" PHD.txt | head\ngrep -on \"hašāgird[^.]\\{0,80\\}\" PHD_mackenzie.txt | head\ngrep -on \"hasagird[^.]\\{0,80\\}\" PHD_mackenzie.txt | head"
}
```


### [2026-09-14T01:59:17.829Z] TOOL RESULT

```
1631:hašāgird, hāwišt
3288:hašāgird, hāwišt; (of eye) syahag, tidag
6418:hasagird, hiiwist
7374:hasagird, hawist; (of eye)               reap drlidan
```


## [2026-09-14T01:59:22.940Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -on \"hāwišt[^.]\\{0,100\\}\" PHD.txt | head\necho \"---\"; grep -n \"hamāg\\|hamē \\[\" PHD.txt | head -3 | cut -c1-100\necho \"=== search hs'klt\"; grep -n \"hš'klt\\|hs'klt\\|hsklt\" PHD.txt PHD_mackenzie.txt | head"
}
```


### [2026-09-14T01:59:24.101Z] TOOL RESULT

```
396:hāwišt [h’wst'] disciple, pupil
1631:hāwišt
1632:hāwištīh
3288:hāwišt; (of eye) syahag, tidag
---
1185:ceremonies, religious ~ khamāgdēn, radpassāg.
=== search hs'klt
```


## [2026-09-14T01:59:25.871Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '396p' PHD.txt | cut -c1-1500"
}
```


### [2026-09-14T01:59:25.922Z] TOOL RESULT

```
hannàm [%7m | = M] = handām. Harborz [Albwic | N Alburz] the mountain range surrounding the world. harg [hlg | cf. M bie, Аг. xarj, xaraj] duty, tribute; work, effort. *harrób- [hlwp- | M hrwb-] collect, gather. —išn(ih): collection, gathering. har(w) [KRA < A АР; hl | M been, N har] all, each, every. harwin [%/wyx! | M hrwyn] pl. al. harwisp [Ahlwsp! | M hrwsp] all. ~in [-yn'] pl. all. harzag [hick! | N harza] loose, free. has®r [Ps] = Av. háóra-] a measure of time (unequal hour, ze of day- light); a measure of length (— frasang, or 1 frasang, 1 mile). haspin [hspyn! | = M] rest, repose. hast, ~ih [AY T!, -yh] = tast, ~ih. hašāģird [kP klt! | M APgyrd, N šāgtrd] disciple, pupil. hast [h#! | = M, N ~] eight. ~ad [80 | N ~] eighty. ~dah [лаһ | N ~, higdah] eighteen. lhàwan [h?wn! | N +] a mortar. *hawan [/?zn! = Av. háwani-] the morning gdh. hāwand [/?wnd | M ÞPw(y)nd] like, similar. ^h: likeness, similarity. hāwišt [h’wst'] disciple, pupil. ~ih: disciplehood. haxt [h()At'] thigh, haunch, hip. hāxtan, hàz- [/7htn', h'e-] lead, guide, persuade, convert. ~išn: persuasion, conversion. hazār [1,000, hel | M h?r, N ~] thousand. ~ag LEI | N ~a] millennium. hazzān [?/h2’n'] tomb, ossuary. hên [Ayn! | M hyyn] army. ~ih: attack, aggression. hérbed [%y/pt! | N hérbud] teacher-priest. ~ih: priestly office. hērbedestān [hylptst’n'] priestly school. ~ih: priestly studies. hérig [hylyk' | N h/xéri] iris, wallflower. hézag [Ayck! | (M hyjg), N
```


## [2026-09-14T01:59:43.633Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==323' BQT_v1_pages.txt | head -30"
}
```


## [2026-09-14T01:59:44.344Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==508' BQT_v2_pages.txt | head -30"
}
```


### [2026-09-14T01:59:44.892Z] TOOL RESULT

```
ارمند
زلایتی‌است از کوهستان آنربابجان و مولدشیرین
مشهور آبجا بوده و ابریشم ارمنی منسوب بدانجا
است - و مخثف اگر من باشد در محاورات ؛
وبنعنی اول بکسر اول هم .کفتهاند .
از من « بروزن‌فرزند , مخففآرمیده
مند است یسی صاحب آرام و آرام گرنته .
از هنفه - بر وزن شرمنده » بمعنی
ارمنده.است که آرمیده و آرام گرفه باشث .
آزهنین « بر وزن مدجبین ۰ نام پس
لشطی بن‌بویان است - وبلفت رومی انار صحرابی
را گویند و بعربی رمان البری خوانند ؛ ویضی
درخت انار صحرایی را کفتداند ؛ و بضی گونند
قاف اول مکسور و ثانی حفتوح .
از هنيه » بکس اول » شهر ست‌معروف
کهآ تشکده درخش ۱ در آفجاست .گویند بانی
ارمنیه وشیراز ۴ و آتشکد؛درخش, رای‌مجوسی
۴ بوده که الحال براس‌البقل مشهور است؛ ودرهم
بغلی منسوب بیاوست .
ار مود بر وزن و معنی امرود است
و آن میوه‌ای باشد حمروف * .
اد هون ه بر وزن گردون ء زری‌باشد
که پیش از کار کردن بمزدور دهند وآنرابمبی
عربون و اربون خوانند ‏
(۱) چك : ژند ویاژند .
کرفن باشد ۵ .
ار هیا - بنتح اول یوذن انبیا. ام یکی
از پیغمبران بتیاسرالیل‌است ۷ -ونام ریفس
سو نام حترت‌علی علیه‌السلام نیز حست - و نام
بیت‌المقدس + و نام بلیان (۲) بن ملکان باشد»
```


### [2026-09-14T01:59:45.912Z] TOOL RESULT

```
  ‫زوترگ‬
                                                                                                               ‫ات‬   ‫ی و ه‬




 ‫و صندوق‬        ‫زورفین است که زرفین در خانه‬                                               ‫وصاحب قوت را گیفزته‌اند‪.‬‬
                                                    ‫باشد ‪.‬‬        ‫روع = بر وزن دوع ‪ ۰‬نهر و رودخانه‬
 ‫رولالی = بروزن دولابی ‪ ۰‬ام‌جاسوی‬                                                               ‫کون ‪:‬‬
                        ‫‪۱‬‬                  ‫اپوسلم بوده ‪.‬‬
                                                                  ‫خشاثاوتر‪.‬خشك‬       ‫دونوع میباشد‪:‬‬        ‫دوایی است‌وآن‬

‫باشد که بربای‬         ‫و آن‌آهنی‬   ‫زاولانه است؛‪:‬‬       ‫ممعي‬         ‫سای‬   ‫بر کے‬    ‫توان‬          ‫کر‬       ‫باس ‪۳‬‬      ‫‪ ۱‬زوفای‬


 ‫گنه کاران لهند و بر بای ستوران بیز کنند‬
                                                                  ‫‪1‬‬              ‫‪۸‬‬          ‫مکی میماند و به‌ترین دک‬
‫مجمد وییجینه را‬              ‫ی‬
                             ‫و‪-‬‬‫میند‬
                                  ‫ووگو‬‫وبتر کی بخا‬
                                     ‫لگىفزته‌آند ‪۰‬‬
 ‫زولزده = بازای نقطمدار برورن‌غول‬                                                          ‫شهرت دارد ‪ .‬گرم و خشاك‬

                                                                                            ‫است‌درسیم ؛ وتررا زوفای‬
                                             ‫گونند (‪.)۱‬‬                                    ‫که‬   ‫وآن چر کی‌است‬           ‫رطبه‬


‫زلوهین ‪ - ۴‬با لام » بروزن و معنی‬                                                            ‫برزبر دلب گوسفند ارمن‬
    ‫زورفین است که زرفین درصندوق زر باشد‪.‬‬                                 ‫زوفا‬               ‫جمم میشود‪ .‬وئوع دیگر‬
‫و هره‬     ‫حصه‬     ‫»‬    ‫چون‬    ‫بر وزن‬   ‫‪-‬‬     ‫رون‬                   ‫نیزدر اختبارات گفته‌اند ‪ .‬طبیمت آنکرم‌است‬
```


## [2026-09-14T01:59:55.411Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 324 325 326 327; do echo \"--- v1 leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v1_pages.txt | grep -o \"از[^ ]*\" | head -8; done"
}
```


### [2026-09-14T01:59:56.587Z] TOOL RESULT

```
--- v1 leaf 324
از
ازو
از
از
از
ازند
ازآن
از
--- v1 leaf 325
ازشصت
از
ازآن
از
از
از
از
ازس-تان
--- v1 leaf 326
از
از
از
از
از
از
از
از
--- v1 leaf 327
از
از
از
از
از
از
ازدست
از
```


## [2026-09-14T01:59:56.788Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 509 510 511 512 513; do echo \"--- v2 leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | tr -d '‏‫' | grep -o \"زیر[^ ]*\" | head -5; done"
}
```


### [2026-09-14T01:59:57.899Z] TOOL RESULT

```
--- v2 leaf 509
--- v2 leaf 510
--- v2 leaf 511
--- v2 leaf 512
--- v2 leaf 513
```


## [2026-09-14T02:00:06.658Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'BEGIN{RS=\"\\f\"} NR==399' BQT_v4_pages.txt | head -40"
}
```


### [2026-09-14T02:00:07.764Z] TOOL RESULT

```
[pdf page 399]
هجند رها
ههجند ۱ - بر وزن سند . برفت را | بروزن کشید. بلفت.زدد وپازند (۱) بمعتی بدهید
کویند وآن سبزیی‌است ماشد اسفناج کهدرآشها ِ باشد که امر بدادن امت .
کدند . هجیر ؟ » بر وزن فقیر »تام پر
هجنتم » بنح اول ولون بروزن مرهم» | قارون* بن‌کاوه است۹ که اورا سهراب وقت ی که
پزبان زند وپازند (۱) بممنی میدهم باشد که از | بایران میرفت در پای قامهٌ مفید در سبزوار در
دادن است ۴ . جنکه زند ه کرفت ۷ - و بنم اول » بهعنی‌خوب
هجید ۴ ج بنتح ارل و نستانی مجهول | وديك ولیکو وزیده وخلاسه بادد۴ .۸ 4

() چك : ژد وپاژند. () چك : ژد ویازند .

۰-۱ هجند سبزی‌آب است. وبرغت نیز گویند:» صحاح‌الفری «فرهنگه نظام» ور4+
صحاح‌الفری دغهٌ طاعتی ۰۰ ۴ - هزوارش‌دادن (پهلوی۰)42187 181)85(62)8(188
«هانه440۵ « پودکر ص۸۳ » امت که محققان 0۳۷8120تلا > 0000128(ع)7 خواند
«یب رکه ص۵۲ . رك : هجید .

۴ - رك : هجنم . ۴ -هجیر بنم اول * هس (و.م.) * خجیر(همم.) ۰

* - غلطاست بجای «فارن». ‎٩‏ - 1۴ز718 پر کودرز است . رك : فهرست‌ولف.

۷- دژی‌بود کش‌خواندبدی سپید بدان دز بد ایرانیان را امد

نگهبان در رزم دیده هجیر که بازورودل بودوبا کرژوتیی...

فردوسی طوسی «شاهنامةٌ بخ ج ۲ ص2۸ ور : 20*24۹ 0 85۸0-4۷۷:500 ‎٩‏
‏ورگ : ج ۵ص ۰۱۲۳۹

۸ - نوروز فرخ آمد ولغز آمد وهژین با طالع معادت و با ک وکب مثیر.

* منوچهری‌دامغانی ص۳۳

0 هچ رك4 : لفات متفرقهٌ پایان کناب .

ج هخاهش _ ۳1321829 در پارسی باستان می کب از دوجزه : هخی 851
(دوست : پار) ۳ متش 881810 از 138820 (حس باطنی » فهم وشمور ؛ اندیشیدن) و جمماً
بمعنی دوست منش است ؛ دریونانی ۸010267716865 . «بارتولمه ۱۷4۸ نام سردودمان سللهٌ
هخامنشی(ه.م.) وجد اعلای کورش ودارپوش امت .

و هخاهنشی - بنتح ارل ودوم وچبارم وکسر پنجم وششم » از : هخامنش (ه.م )ی
```


## [2026-09-14T02:00:16.256Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 323 324 325; do echo \"=== v1 leaf $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' BQT_v1_pages.txt | grep -n \"[A-Za-z]\" | head -12; done"
}
```


### [2026-09-14T02:00:17.420Z] TOOL RESULT

```
=== v1 leaf 323
=== v1 leaf 324
=== v1 leaf 325
```


## [2026-09-14T02:00:20.514Z] TOOL CALL #49: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:113 --image 2>&1 | tail -40"
}
```


### [2026-09-14T02:00:21.619Z] TOOL RESULT

```
no scan of BQT covers printed page 113 (see 'scans' in refs_online.json)
```


## [2026-09-14T02:00:23.892Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\""
}
```


### [2026-09-14T02:00:25.081Z] TOOL RESULT

```
[
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
]
```


## [2026-09-14T02:00:31.344Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"\" BQT_alt_v1.txt BQT_v1.txt BQT_dli_part1.txt BQT_v2.txt 2>/dev/null\necho \"=== haca\"; grep -n \"hačā\\|haca\\|hac[aā]\" BQT_alt_v1.txt BQT_v1.txt BQT_v2.txt BQT_v1_pages.txt BQT_v2_pages.txt 2>/dev/null | head"
}
```


### [2026-09-14T02:00:31.428Z] TOOL RESULT

```
BQT_dli_part1.txt:7
BQT_v2.txt:67022
BQT_alt_v1.txt:61533
BQT_v1.txt:66791
=== haca
```


## [2026-09-14T02:00:42.733Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\ncurl -sL --max-time 180 \"https://archive.org/download/borhan-ghate-v1/borhan-ghate-v1_djvu.txt\" -o bqt1-440.txt; wc -c bqt1-440.txt; grep -c \"[A-Za-z]\" bqt1-440.txt"
}
```


### [2026-09-14T02:00:47.157Z] TOOL RESULT

```
146 bqt1-440.txt
7
```


## [2026-09-14T02:00:54.851Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON shagerd\"; grep -n \"شاگرد\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5 | cut -c1-250\necho \"=== MON adena\"; grep -n \"شاگرد\" incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -5 | cut -c1-250\necho \"=== ARY latin index\"; grep -n -i \"sagird\\|shagerd\\|SEKW\\|sekw\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-14T02:00:55.033Z] TOOL RESULT

```
=== MON shagerd
MON_part2.txt:2206:امرد. (رجال؛ درایه) شاگرد؛ تلمیذ» ترست 
MON_part2.txt:2233:که خریدار به شاگرد دکان به عنوان انعام 
MON_part2.txt:2239:خانه شاگرد (در سرای بزرگان). پسر نابالغ 
MON_part2.txt:24545:مدرسه که در آن معلمان به شاگردان درس 
MON_part2.txt:27159:برجستگی سر زانو. کندهٌ شاگرد: (خاد.) 
=== MON adena
incoming/MON/MON_2vol_Adena_v2_djvu.txt:2206:امرد. (رجال؛ درایه) شاگرد؛ تلمیذ» ترست 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:2233:که خریدار به شاگرد دکان به عنوان انعام 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:2239:خانه شاگرد (در سرای بزرگان). پسر نابالغ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:24545:مدرسه که در آن معلمان به شاگردان درس 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:27159:برجستگی سر زانو. کندهٌ شاگرد: (خاد.) 
=== ARY latin index
```


## [2026-09-14T02:00:56.618Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN scarlet\"; grep -n \"scarlet\" KLN_1966.txt KLN_1971.txt | head -10 | cut -c1-200\necho \"=== KLN sigillat\"; grep -n \"sigillatus\\|siqillat\\|siqillāt\" KLN_1966.txt KLN_1971.txt LKT.txt DEV.txt PHN.txt | head -10 | cut -c1-250"
}
```


### [2026-09-14T02:00:56.723Z] TOOL RESULT

```
=== KLN scarlet
KLN_1971.txt:47043:‘tissue adorned with seals’. See scarlet. 
KLN_1971.txt:49798:cochineal, n., a scarlet dye. — Fr. F. cochenille , 
KLN_1971.txt:82452:cochineal; scarlet grain’, fr. L. grana , pi. of gra- 
KLN_1971.txt:82458:of plants; cochineal; scarlet grain’, and see 
KLN_1971.txt:214129:scarlatina, n., scarlet fever {med.) — Medical L., 
KLN_1971.txt:214130:Latinized fr. scarlet by the English physician 
KLN_1971.txt:214132:scarlet, n. — ME. scarlat, scarlet, fr. OF. escar- 
KLN_1971.txt:214141:Derivatives: scarlet, adj., scarlet-y, adj* 
KLN_1971.txt:221762:also the first element in scarlet and the second 
KLN_1971.txt:236067:saqirldt . See scarlet, 
=== KLN sigillat
KLN_1971.txt:214135:borrowed fr. Arab, siqillat, ‘tissue adorned with 
KLN_1971.txt:214136:seals’, which is a loan word fr. L. sigillatus, ‘seal- 
KLN_1971.txt:221720:sigillate, tr. v., to seal. — L. sigillatus, pp. of 
KLN_1966.txt:33972:also  It.  scarlatto);  from  Pers.  saqirldt,  itself borrowed  fr.  Arab,  siqillat,  ‘tissue  adorned  with seals’,  which  is  a  loan  word  fr.  L.  sigillatus,  ‘seal¬ ed’,  pp.  of  sigillare,  ‘to  seal’,  fr.
KLN_1966.txt:35163:sigillate,  adj.,  decorated  with  marks.  —  L.  sigilld- tus,  pp.  of  sigillare,  ‘to  mark  with  a  sign  or  seal’, fr.  sigillum.  See  prec.  word  and  adj.  suff.  -ate. sigillate,  tr.  v.,  to  seal.  —  L.  s
```


## [2026-09-14T02:00:59.765Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '214129,214145p' KLN_1971.txt\necho \"=== 47040\"; sed -n '47035,47050p' KLN_1971.txt\necho \"=== 221715\"; sed -n '221715,221730p' KLN_1971.txt"
}
```


### [2026-09-14T02:00:59.906Z] TOOL RESULT

```
scarlatina, n., scarlet fever {med.) — Medical L., 
Latinized fr. scarlet by the English physician 
Thomas Sydenham (1624-89). 
scarlet, n. — ME. scarlat, scarlet, fr. OF. escar- 
late (F. dear late) ; fr. ML. scarlatum (whence 
also It. scarlatto ); from Pers. sdqirlal, itself 
borrowed fr. Arab, siqillat, ‘tissue adorned with 
seals’, which is a loan word fr. L. sigillatus, ‘seal- 
ed’, pp. of sigillare, ‘to seal’, fr. sigillum (for 
*signolom), ‘seal’, dimin. of signum, ‘sign’. See 
sign and cp. suclat, ciclatoun. 

Derivatives: scarlet, adj., scarlet-y, adj* 
scaroid, adj., pertaining to the Scaridae ; n., a 
scaroid fish. — See Scarus and -old. 
scarp, n., a steep slope; an escarpment. — It. 
scarpa , whence also OF. escarpe. See escarp, n., 
=== 47040



circaEtus 



terial (obsol.) — OF. ciclaton , fr. Arab, siqilldf , 
‘tissue adorned with seals’. See scarlet. 

Ciconia, n., a genus of birds, the stork ( ornithol. ) 
— L. ciconia , ‘stork’; of uncertain origin. It is 
possibly, like cicada , ‘tree cricket’ (see Cicada), 
a loan word from a Mediterranean language. 

Cicuta, n., a genus of herbs of the carrot family 
=== 221715
seal, ‘stamp’. 

sigillate, adj., decorated with marks. — L. sigilla- 
tus, pp. of sigillare , ‘to mark with a sign or seal’, 
fr. sigillum. See prec. word and adj. suff. -ate. 
sigillate, tr. v., to seal. — L. sigillatus, pp. of 
sigillare. See prec. word and verbal suff. -ate. 
Sigismund, masc. PN. — G., a compound lit. 
meaning ‘protection through victory’. The first 
element is rel. to OHG. sigu , MHG. sic, sige , 
G. Sieg , MDu. seghe, Du. zege, ON. sigr, 
Swed. seger, Dan. seier, OE. sige, gesig, 
Goth, sigis , ‘victory’, and cogn. with OI. saha-, 
‘victory’, sahate, ‘overcomes, masters’, Gk. tyzw 
(fr. I.-E. base *segh-), ‘to have, hold’. See 
scheme and cp. words there referred to. The
```


## [2026-09-14T02:01:13.088Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN sign\"; grep -n \"^sign, n\\.\" KLN_1971.txt | head; \necho \"=== FVQ sijill\"; grep -n -i \"sijill\\|sigill\" FVQ.txt | head -10\necho \"=== LKT\"; grep -n -i \"siqillat\\|scarlat\\|sakirlat\\|saqirlat\" LKT.txt | head -10 | cut -c1-200"
}
```


### [2026-09-14T02:01:13.176Z] TOOL RESULT

```
=== KLN sign
221755:sign, n. — ME. signe, fr. OF. (= F.) signe, fr. L. 
=== FVQ sijill
10305:(Sijill). 
10309:The meaning of Sigill in this eschatological passage was unknown 
10323:Gk. criyiXXov ~ Lat. sigillum, used in Byzantine Greek for an Imperial 
=== LKT
4070:'Mit  Kermes  oder  Cochenille  rot  gefärbtes Kleid'  [aus  ar.  siklät  >  dtsch.  Siklat, 'schwerer  farbiger  Seidenstoö',  das  selbst aus  lat.  cyclas.  gr.  KUKXdi;  stammt], hieraus  
6482:escarlate  afz.  1794
7448:sapphirus  1830 saraballa  1849 Saraceni  1856  c sarrabarrae  1849 satanas  1867 satureia  1872 scarlatum  1794 Seraphim  1885 Äeres  1878 sericus  1878 seto  1878 sicera  1787  a siclus  1880 
8046:escarlata  1794
```


## [2026-09-14T02:01:13.795Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LEW signum\"; grep -n \"signum\" LEW_1910.txt LAT.txt | head -10 | cut -c1-200\necho \"=== socius\"; grep -n \"socius\" LEW_1910.txt LAT.txt | head -5 | cut -c1-200"
}
```


### [2026-09-14T02:01:13.887Z] TOOL RESULT

```
=== LEW signum
LAT.txt:6849:"signum". M.L.929.
LAT.txt:30257:Insignis: v.signum.
LAT.txt:31032:le pl. Jugulae, cf. Varr., L.L.7,50, iugula, signum quod Accius appellat
LAT.txt:36260:exercitus minima manus quae unum sequitur signum, Varr., 1 .L.5, 80 .
LAT.txt:39248:<signum> nulla lababat ex parte cum... subiectis uectibus conarentur
LAT.txt:41945:nota, -ae f.: — alias significat signum, ut in pecoribus, tabulis,
LAT.txt:45249:signum filii hominis in caelo. Les 1. romanea n'ont conservd que le
LAT.txt:58158:Pleiadum, Stat. S. 1, i, 95 > etc.; puis, par abus, a'eat ditdVun astre- xioi - signum
LAT.txt:58195:sigillum: v. signum.
LAT.txt:58208:signum, -In. (avec t notd dans les inscriptions, soit par i longa,
=== socius
LAT.txt:1707:i° aequalis (de aequus, comme socialis de socius): de meme taille, de
LAT.txt:12147:an ciuis comedis parui pendere, X socius, a peregrinus. Ainsi le ciuis
LAT.txt:12148:Romanus s'oppose au socius Latinus. Ancien (Loi des XII T.), usuel.
LAT.txt:37093:centre,et "moitie". Semble cree par Cic. sur le modele socius / societas ,
LAT.txt:58862:socius, -a, -um: qui accompagne; associe avec. Souvent substan¬
```


## [2026-09-14T02:01:16.637Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LAT signum\"; sed -n '58208,58250p' LAT.txt\necho \"=== LAT socius\"; sed -n '58862,58890p' LAT.txt"
}
```


### [2026-09-14T02:01:16.765Z] TOOL RESULT

```
=== LAT signum
signum, -In. (avec t notd dans les inscriptions, soit par i longa,
C 3 X VI 10934, ou par ei CIL I 3 49; nais les langues ronanes attestedtSignum - noa -
an i: it.segno, cf. Somner tdb. a , p.xax): signe, marque distinctive
(joint A nota) defini par Cic. : quod sub sensum aliquem cadit et
quiddam significat, Inu.1,30,40; jecoris, seruitutis signa , etc.;
"seing, sceau"; signal, et "cloche" (Greg.Tur.). De li divers enplois
speciam: x° dans la 1. militaire "enseigne(s) ", qui distinguent les
divisione d'une arnde (d'o b: signifer,' antesignani, subsignani )}
usitd surtout au pluriel, et qui figure dans un grand nombre d'ex¬
pressione techniques: signa sequi, seru&re, -deserere , etc.; a^ dans
la 1. des artistes "inage peinte ou sculptae", sens venu peut-etre
de l'habitude de distinguer' les enseignes, ou les proues des vais-
seaux de guerre par des figures brod^es ou sculptdes; 3 0 en astrononie:
signa dicuntur eadem et sidera. Signa quod aliquid significent, ut
Libra aequinoctium, Varr., L.L.7,14. Signum correspond i Otjp/x, crqueiov,
dont il a peut-etre empruntd quelques-uns des sens. - Ositd de tout
temps. Panroman, M.L.7908; celt.: irl.sen, sigen ; britt.swyn; et
gern;: v.angl .segn.
Ddriv 4 s et composds: sigillum n.: petite image, statuette; seing.
Sigillaria,-iuUi fetes des-inages; sigillarius, sigi llariSrius ;
sigillaricius} sigillO, sigillator} sigillatus (sur le sort de
sigillatus, v. O.Bloch sous dcarlate)} dissigillO (v.Thes., s.u.);
sigilliola n.pl.(Arn.), M. 1 .7903-4, celt.: iri. sila, siglithe "si¬
gillum,-Utus", britt. siel "sigillum", swinogl "signaculum"; signS,
-as: -re significat modo scribere, modo anulo signa imprimere,
modo pecora signis notare, P.F. 457,6} quelquefois employd pour
significB ou dSsignS. D 4 riv 6 s: signator,-tiS (Tert.), -tOrius (tardif);
signaculum (b.lat.), M.L.7905 et 7°94a *signate, 7906 *signicSre.
assignO: 1° assigner, t. du droit public, cf .Illuir agreis dandeis
adsignandeis} s»° sceller (^poq. imp< 5 r.); assignator,-tio.
consigno: marquer d'un sceau, confirmer par dcrit, britt. cyswygno}
designo (souvent confondu avec d-issigno) : ddsigner, marquer, M.l.
459^; dissigno (rare): 1 ° distinguer, glosd ordinO, distribuO} a° ronpre
le cacbet, ddtruire, violer; exsignO* noter tout au long; Insigno:
®YX a P(Gloss.), conservd dans les 1 . romanes av.ec le sens de
"enseigner", M.L. 4469} ob-signo: fermer par un seing, sceller;
persignO: tenir note de (rare, dpoq.imp.); praesigno: marquer d^a-
vance; resignO: briser le cach’er; ouvrir, violer'lesecret de ;
cf. aussi F.35a,4, resignare antiqui pro rescribere ponebant ut
adhuc subsignare dicimus pro subscribere} cf. P.F. 359,9 resignatum
aes dicitur militi, cum ob delictum aliquod iussu tribuni militum,
ne stipendium ei detur, in tabulas defertur} subsigno: transcrire
au bas. A ces verbes peuvent correspondre des ddrivds: cOnsig'nStio
=== LAT socius
socius, -a, -um: qui accompagne; associe avec. Souvent substan¬
tivi: socius, socia: compagnon, compagne, associe(e). Dans la 1 . du
droit public "allie", employe surtout au pl. socii. - Usite de tout
temps. M.L.O05G.
Derivis et composes: sociennus (Pl.Au.GS9, sans doute formation
populaire, cf . dossennus, leuenna, trasenna , avec suffixe etrusque,
cf. Porsenna Spurinna ?); societas: compagnie, societe, association,
alliance, M.L.Ooss; socialis: x° "concernant les allies"; 3° k l'epoq.
imper. "social, sociable», et "conjugal" ( 0 v.) f socidlitas (Plin.
le J.); s ocio, -as: associer, allier, d'ou sociat id, sociatrix (tar -
difs); sociabilis (epoq.imp.); sociofraudus (Pl.,Ps.3 63); adsocio
(lat.imper., Stace; syn. de adiungo), M.L.733; consocid (usuel et
class.), consociatio (joint par Cic. a conciliatio, connunitds ),
sur lesquels on a fait, a basse epoque, ad- et con-socius', dissocio,
-dtid,-alis,-dbilis (Hor.,calque de av e7tip,i,XTOS? ); insociabilis,
tnsocia l is (tous deux d*ipoque imperiale).
Les Latins n'ont jamais songe k etablir une parente entre sequorxi 15
sGd&s
et socius* Socius n*est pas "celui qui suit" «ais "celui qui va
avec", cf. Cic., Font.i7,39 uitae socia uirtus, mortis comes gloria.
Le germanique, ob la racine de sequor n'existe pas, au moinb au
sens de "suivre",' a aussi T.isl. seggr, v.angi, secg au seus de "homme,
guerrier". Ni le latin ni le germanique ne per«ettent de reconnaxtre
si ces mots ont un ancien ft to , un ancien h , ou un ancien kk. En indo-
iranien, il jr a un mot remarquable et sfirement ancien: vAd.sdfeftd
(acc.sg.sdfeASyam, dat. sg. safeAye), av. baxa (dat.sg .hasS, nom.pl. hdxayo)
"compagnon". Le rapprochement s'i«pose; il n’exclut pas celui avec
sequor , car -kh- peut alterner avec mais il indiquerait 1'exis-
tence d’un mot indo-europAen de caraCtbre "expressif", ^populaire"
```


## [2026-09-14T02:01:32.953Z] TOOL CALL #59: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T02:01:32.960Z] TOOL RESULT

```


```


## [2026-09-14T02:01:36.105Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/signum",
 "prompt": "Latin signum: give the full etymology section verbatim, including whether it is derived from PIE *sekʷ- 'to follow' or *sek- 'to cut', and any mention of de Vaan or uncertainty. Also any derived terms sigillum/sigillatus."
}
```


## [2026-09-14T02:01:37.659Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/scarlet",
 "prompt": "Give the full etymology of scarlet verbatim, including any mention of Persian saqirlat, Arabic siqillat, Latin sigillatus, Medieval Latin scarlatum, and any statement of uncertainty or alternative Germanic origin."
}
```


### [2026-09-14T02:01:40.585Z] TOOL RESULT

```
# Latin Signum Etymology

## Full Etymology Section

From Proto-Italic *segnom, from Proto-Indo-European *sek- ("to cut") or *sekʷ- ("to follow").

The entry indicates dual possible origins without resolving which is primary. De Vaan (2008) is cited as the etymological authority in the references section, specifically his *Etymological Dictionary of Latin and the other Italic Languages* (page 563).

## Derived Terms

The entry lists these derived terms from Latin signum:
- **sigillum** (seal, signet)
- insignis
- signāle
- signifex
- significō
- signō

Note: The entry does not include "sigillatus" in its derived terms list, though sigillum (from which sigillatus would derive) is mentioned as a separate derived term.
```


### [2026-09-14T02:01:42.987Z] TOOL RESULT

```
# Etymology of Scarlet

Based on the provided content, here is the full etymology:

The word **scarlet** comes from "mid-13c. (late 12c. as a surname), 'rich cloth' (often, but not necessarily, bright red), from a shortened form of Old French _escarlate_" and Medieval Latin _scarlatum_.

The document notes uncertainty about its ultimate origin: the term "often is said to be from a Middle Eastern source, but perhaps is rather from a Germanic source akin to Old High German _scarlachen_, _scharlachen_ (c. 1200), from _scar_ 'sheared' + _lachen_ 'cloth.'"

**Important note:** The web page provided does **not** mention Persian *saqirlat*, Arabic *siqillat*, or Latin *sigillatus*. It references only Old French, Medieval Latin, Italian, Spanish, and Old High German sources. The etymology presented here reflects no certainty about ultimate origin, offering only the Germanic alternative as a possibility rather than confirmation.
```


## [2026-09-14T02:01:51.292Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%A7%DA%AF%D8%B1%D8%AF",
 "prompt": "Persian شاگرد: give the etymology section verbatim — Middle Persian form, Old/Proto-Iranian reconstruction, any mention of *hačā-kr̥ta- or *haxā-kr̥ta-, Armenian աշակերտ, and cited sources (Hasandust, MacKenzie)."
}
```


## [2026-09-14T02:01:53.471Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B3%DA%A9%D9%86%D8%A7%D8%B3",
 "prompt": "Persian اسکناس: give the etymology verbatim — is it from Russian ассигнация (assignatsiya), from French assignat, from Latin assignare? Any dates or details."
}
```


### [2026-09-14T02:01:56.737Z] TOOL RESULT

```
# Etymology of اسکناس (eskenâs)

According to the Wiktionary entry, the Persian word اسکناس was "Borrowed from Russian ассигна́ция (assignácija), borrowed from Polish asygnacja, a learned borrowing from Latin assīgnātiō."

The entry does not mention French as an intermediate source. The documented chain is: Latin → Polish → Russian → Persian. No specific dates are provided for these borrowing events in the article.
```


### [2026-09-14T02:01:57.432Z] TOOL RESULT

```
# Etymology of Persian شاگرد

**Middle Persian Origin:**
The term derives from Middle Persian "hšʾklt'" (hašāgird), meaning "disciple, pupil."

**Proto-Iranian Reconstruction:**
From Proto-Iranian *hašā-kr̥táh-, composed of two elements:
- First component: *hu-šāk- from Proto-Indo-Iranian *Hsu- ("good") + Proto-Indo-European *sekʷ- ("to follow")
- Second component: Proto-Indo-Iranian *kr̥tás ("done, made")

**Related Forms:**
The word is cognate with Old Armenian "աշակերտ" (ašakert) and Aghwan "𐔰𐕐𐔰𐕙𐕄𐔴𐕜" (ašarḳeṭ), both Iranian borrowings.

**Cited Sources:**
- Keith Hitchins et al., "Georgia v. Linguistic Contacts with Iranian Languages," Encyclopedia Iranica (2001)
- V. S. Rastorgujeva and D. I. Edelʹman, Etymological Dictionary of Iranian Languages (2007)
- D. N. MacKenzie, A Concise Pahlavi Dictionary (1971)
```


## [2026-09-14T02:02:06.690Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%AC%D9%84",
 "prompt": "Arabic سجل (sijill): give the etymology verbatim — is it from Latin sigillum via Greek σιγίλλιον? Also the Persian سجل entry if present."
}
```


## [2026-09-14T02:02:09.259Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sek%CA%B7-",
 "prompt": "Proto-Indo-European *sekʷ- 'to follow': give the reconstruction, gloss, and the list of derived terms including Proto-Indo-Iranian, Avestan haca, Old Persian hacā, Latin sequor/socius/secundus/signum. Note if Pokorny 896 is cited."
}
```


### [2026-09-14T02:02:11.919Z] TOOL RESULT

```
# Etymology of سجل (sijill)

Based on the Wiktionary entry, here's the etymological path:

**Verbatim etymology from the source:**
"The noun is from Byzantine Greek _σιγίλλιον, σιγίλλον_ (sigíllion, sigíllon), from Latin _sigillum_ ('seal; sealed document')"

The word traveled through multiple languages: Latin → Byzantine Greek → Arabic. The Arabic term also appears in Classical Syriac as _ܣܝܓܝܠܝܘܢ_ and _ܣܓܠܐ_ (sagīlā, sīgīlīōn).

**Note on Persian:** The web page does not contain a separate Persian entry for سجل. While the page header indicates 10 language versions exist (including Persian), the actual content provided only covers Arabic, Moroccan Arabic, Ottoman Turkish, and South Levantine Arabic sections.
```


### [2026-09-14T02:02:14.304Z] TOOL RESULT

```
# Proto-Indo-European *sekʷ- Root

**Reconstruction:** *sekʷ- (imperfective)

**Gloss:** "to follow"

**Key Derived Terms:**
- Proto-Indo-Iranian: *sáčaH
- Avestan: 𐬵𐬀𐬑𐬙𐬀 (haxta)
- Old Persian: 𐏃𐎧𐎠𐎶𐎴𐎡𐏁 (haxamaniš)
- Latin: sequor, socius, secundus

**Citation:** Yes, Pokorny (1959) pages 896-897 is cited as the primary reference for this root's documentation in the *Indogermanisches etymologisches Wörterbuch*.

The page documents three distinct homonymic roots with the form *sekʷ-, meaning "follow," "see," and "say" respectively, each with separate etymological traditions and descendant forms across Indo-European language families.
```


## [2026-09-14T02:02:20.782Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B2",
 "prompt": "Persian از (az) 'from': give the etymology verbatim — Middle Persian ʾc (az), Old Persian hacā, Avestan haca, Proto-Iranian *hača, PIE *sekʷ-. List any cited sources."
}
```


## [2026-09-14T02:02:22.891Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%B1",
 "prompt": "Persian زیر (zir) 'under, below': give the etymology verbatim — Middle Persian azēr, Old Iranian *hačā adari / *hača-adari, Avestan aδairi. List cited sources."
}
```


### [2026-09-14T02:02:25.840Z] TOOL RESULT

```
# Etymology of Persian از (az)

Based on the Wiktionary entry, here is the etymological chain for the Persian preposition "از" (az), meaning "from":

**Direct lineage:**
- Middle Persian: 𐭬𐭮 (az)
- Old Persian: 𐏃𐎨𐎠 (hacā)
- Proto-Iranian: *háčā
- Proto-Indo-European: *sekʷ- ("to follow")

The entry notes that this preposition descended through multiple language stages, with the meaning evolving from the PIE root meaning "to follow" into the modern Persian sense of "from" or "of." 

Interestingly, the Wiktionary article identifies this as "the third most used word in Persian," according to *A Frequency Dictionary of Persian* by Miller and Aghajanian-Stewart (2009).

The word has also left its mark on related languages—it appears in Urdu, Hindi, Judeo-Persian, and Judeo-Tat as a loanword from Classical Persian.
```


### [2026-09-14T02:02:28.457Z] TOOL RESULT

```
# Etymology of Persian زیر (zir)

According to Wiktionary, the word زیر (zir, "under/below") derives from **Middle Persian azēr** ("underneath"), which traces back to **Old Persian *hacā-adari**.

The full etymological path breaks down as:
- **Old Persian components**: *hacā* ("from," itself from Proto-Iranian *háčaH) + *adari* ("under," from Proto-Iranian *(H)adárah)
- **Distant relative**: English "under"

The prepositional usage represents a contraction of older Persian phrases: **در زیر** (dar zēr-i, "in the underneath of") or **به زیر** (ba zēr-i, "at the underneath of"). These fuller forms remain dated in Iran but are more prevalent in eastern Persian-speaking regions.

**Cited scholarly sources** include works by Paul Horn (1893), Heinrich Hübschmann (1895, 1897), and the Etymological Dictionary of Iranian Languages by Rastorgujeva and Edelʹman (2000).
```


## [2026-09-14T02:02:36.581Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON eskenas\"; grep -n \"اسکناس\" MON_part1.txt MON_part2.txt 2>/dev/null | head -4 | cut -c1-300\necho \"=== MON saqerlat\"; grep -n \"سقرلا\\|سقلاط\" MON_part1.txt MON_part2.txt 2>/dev/null | head -6 | cut -c1-300\necho \"=== AFM/TAD/PLA siqillat\"; grep -n \"سقلاط\\|سقرلا\\|سجلاط\" AFM.txt TAD.txt incoming/PLA/PLA_pages.txt 2>/dev/null | head -8 | cut -c1-300"
}
```


### [2026-09-14T02:02:36.719Z] TOOL RESULT

```
=== MON eskenas
MON_part2.txt:80026:نوت: ۰0۱ [- نت ] (.) (عم.) اسکناس. 
MON_part1.txt:12921:اسکناس: عقجعمه (.) نوعی کاغذ بهادار 
MON_part1.txt:12924:نشر اسکناس: چاپ کردن و انتشار دادن 
MON_part1.txt:12925:اسکناس در میان مردم. 
=== MON saqerlat
MON_part2.txt:24808:را از سقرلات می‌ساختند. کلاه بوقی: کلاهی 
MON_part1.txt:34386:گرگ بغل‌زن: (کد.) سقرلاط دوز. #۳ 
MON_part1.txt:46835:سقرلات» لندره و مانند آن. جامه ازرق 
MON_part1.txt:78427:سقلاط - سقرلاط - سقرلات - سقلطون - 
MON_part1.txt:78428:سقلاطین | (.) نوعی پارچة ابریشمی زر 
=== AFM/TAD/PLA siqillat
```


## [2026-09-14T02:02:38.586Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT scarlet\"; grep -n \"SCARLET\\|scarlet\" SKT.txt | head -5 | cut -c1-300\necho \"=== FSD scarlet\"; grep -n \"siqillat\\|saqirlat\\|scarlatum\" FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt WEB_vol1.txt 2>/dev/null | head -8 | cut -c1-300"
}
```


### [2026-09-14T02:02:38.692Z] TOOL RESULT

```
=== SKT scarlet
3626:CochineaL  <Span.  -  L.  -  Gk.)  Sp< cochinilla^  cochineal  (made  from  iasM which  look  like  berries).  — L.  •»«'««, a  scarlet  colonr.  -  L.  c^fum,  a  Un also  kermes,  iuppo<;ed  to  Ik  a  benyt— C VMtitof.  a  berry,  cuchinnt.
7880:Ormil  (3).  fine  sand.  (F.-G.)     In  Spcn- F    O.  i.  7.  6;  Vii.  Bcllay.  «t.   u.- .>.  lit  bail  (K.^//).-G,^w, ;  allied  to  Grit, liu.  ^F.-L.)    M.  E.  grtin.^O.  F. »L.  granum,  a  grain,  com.     Cog- Twith  E.  Corn.     (VGAK.) entrain,   ingrain,   to  dye  of  a  fa
16601:■let  (F.  -  iVs.)  0.  F.  txarlatt, ,^pan.  €scarlaia,  Ital.  tcarhitto.) t^aijf,  ri^a/Jf,  lUf/ii/,  $c.i:kt Lg.  the  name  of  a  stuff,  which of  a  scarlet  colour.  ^  Hence fMM,  SwArlet  clolh,  whence  M.  E. iCIuucer).  The  Turkish  i$kerlat, merely  borrowed  from  Ital. 
23627:French  from  Persian:  check,  chcckci (chequer),  checkers  (chequers),  che^s  ex- chequer, jar  (a),  lemoo,  lime  (3),  ounce (2)  ?,  rook  {%\  scarlet.
=== FSD scarlet
FSD_vol4.txt:3410:<   LL  scarlatinas,  scarlet,  <   scarlatum  (<  Per  saqa-  roora  "t  ( <   n )
FSD_vol4.txt:3466:the  official  robes  Compare  sc  ablet  hat  (2)  A   judge, fox-hunter, orgolfer  forananalogousreason  5.  [Eng] A   small  June  moth  (Erastna  oslrina)  [<  OF  escar- late,  <   LL  scarlatum,  see  scarlatina  1 5car'Iet-sced",  X   skar'let-sld*,  2   scar'16t-sCd  ,   n
```


## [2026-09-14T02:02:46.643Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON eskenas\"; sed -n '12918,12926p' MON_part1.txt\necho \"=== MON saqlat\"; sed -n '78424,78436p' MON_part1.txt"
}
```


### [2026-09-14T02:02:46.731Z] TOOL RESULT

```
=== MON eskenas

اسکله: عاعتای رداف‌اه آمکعر. و متر] (ا.) 
بندرء لنگ رگاه» بارانداز کشتی‌ها. 
اسکناس: عقجعمه (.) نوعی کاغذ بهادار 
که بهای وی بر روی آن نوشته شده و برای 
خرید و فروش بکار می‌رود؛ پول کاغذی. 
نشر اسکناس: چاپ کردن و انتشار دادن 
اسکناس در میان مردم. 

=== MON saqlat
سسفقلاطون: (مهه)هتاقاه: [- معر. 


سقلاط - سقرلاط - سقرلات - سقلطون - 
سقلاطین | (.) نوعی پارچة ابریشمی زر 
دوزی شده که آن را در بغداد می‌بافتند و 
شهرت بسیار داشته. پارچه‌ای نفیس به رنگ 


سرخ يا کبود. 
ستلمه. (۵-)50(0۱۲0۵ [تر. - سقررمه - سغلمه
```


## [2026-09-14T02:03:04.205Z] TOOL CALL #71: Bash

```json
{
 "command": "ls site/pages/440.jpg 2>/dev/null; pdftoppm -f 440 -l 440 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg440 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg440.png"
}
```


### [2026-09-14T02:03:06.469Z] TOOL RESULT

```
site/pages/440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 75018 Sep 13 22:03 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg440.png
```


## [2026-09-14T02:03:08.587Z] TOOL CALL #72: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg440.png"
}
```


### [2026-09-14T02:03:09.422Z] TOOL RESULT

```

```


## [2026-09-14T02:03:09.416Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T02:03:28.533Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd2 sek\"; grep -n \"seq[uv]or\\|sek*u̯-\\|haxay\\|sakhi\\|sákhi\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -10 | cut -c1-250\necho \"=== IEC\"; grep -n \"sekʷ\\|seqṷ\\|sequor\" IEC.txt | head -6 | cut -c1-250\necho \"=== SYN follow\"; grep -n \"sequor\" SYN.txt | head -6 | cut -c1-250"
}
```


### [2026-09-14T02:03:28.631Z] TOOL RESULT

```
=== WLD Bd2 sek
30887:Wegen ar. kh sehr zweifelhaft ai. sdkJid [sakhi-) „Gefahrte, Genosse, 
30888:Freund“, av. haxay- (hasi-) ds., ap. Haxamanis- ..^Axaipevrjg^" \ Brugmann 
30901:Lat. sequor, -i „nachfolgen, begleiten, verfolgen“, Ptc. secutus nach so- 
30927:Air. sechur (= lat. sequor^, mir. sechim „folge“, sechem „das Polgen‘‘ (aber 
=== IEC
15233:sequð (1) “follow, accompany’. WP II, 476 Skt. sacami, v. “accompany, belong Io: Av. haca-, v. ‘follow, achieve’; Tokh. A säk-, v. ‘follow’; Myc. (h)eq-, Gk. hépomai, v. id.; Alb. cf. ndjek, aor: ndoqa, v. Cpureue fr. *endo-seq
=== SYN follow
26409:9. Goth. saithwan, ON sjd, OE séon, etc., general Gme. (with cpds. Du. aan- zien, NHG ansehen ‘look at’), with sbs. for ‘sight’, Goth. stuns, OE gesiht, syn, etc. : Ir. sech- in words for ‘point out’ and ‘sight’ (above, 8), IE
```


## [2026-09-14T02:03:30.128Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY\"; grep -n -i \"SEKW\\|SEQU\" incoming/ARY/ARY_latin_index_pages.txt | head -10 | cut -c1-200\necho \"=== ARY fa\"; grep -n \"شاگرد\\|اسکناس\" incoming/ARY/ARY_pages.txt | head -6 | cut -c1-200"
}
```


### [2026-09-14T02:03:30.217Z] TOOL RESULT

```
=== ARY
10216:INSEQUE LATIN) 3 SANSKRIT) np Suile
=== ARY fa
```


## [2026-09-14T02:03:38.492Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4055,4085p' LKT.txt"
}
```


### [2026-09-14T02:03:38.549Z] TOOL RESULT

```
1787.  Hebr.  säxar:
'Sich  berauschen';  hierzu  a)  lexar*  'ein aus  Obst  und  Honig  hergestelltes  be- rauschendes Getränk  bei  den  Hebräern'; hieraus  gr.  oiKepa,  lat.  sicera,  it.  sidro 'Obstwein',  cidro  'dass.',  rum.  p'ghir; frz.  cidre,  sp.  cidro  'Apfelwein';  dtsch. Cider,  ndl.  engl,  cider;
b)  iikkör  'betrunken';  hieraus  jüd.- dtsch.  schicker  'betrunken,  toll',  an- geschickert,  heschickert  'betrunken'  [Lenz Eindr  12].
1788.  Hebr.  säkar: 'Schminken',  dazu  pi'el  s7Z:J;er 'täuschen, lügen',  5eÄ-gr 'Lüge' ;  hieraus  jüd. -dtsch. Schakren  'Lügner',  dtsch.  Schäker 'Mensch,  der  Scherz  treibt',  Yh.  schäkern. [Kluge  383.  O.WEISE  inZfdWfV,255 (dagegen,  aber  wohl  zu  Unrecht).
1789.  Hebr.  säkas!
'Ekel  empHnden',  dazu  pi'el  sikkes  'ver-
unreinigen', hierzu  fem.  sikkeza,  nhbr. äiktsö  'die  Unreine',  ursprünglich  zur Bezeichnung  eines  christlichen  Mäd- chens, bes.  eines  Dienstmädchens:  jüd.- dtsch.  Schicksei.  Jetzt  wird  der  Aus- druck gerade  umgekehrt  als  landläufige Bezeichnung  eines  jüdischen  Mädchens benutzt.  [Ave-L  IV,  477.  Kluge  390. MWiD  47.
1790.  Ar.  sakf:
'Dach';  aus  sakf  fv's-sama'  'Dach  am Himmel'  wurde  mit  Imäla  [ä  >  e  ^  »] sp.  zaquizami  'Rumpelkammer,  kleine elende  Bude'.    [DE  365.    Eguilaz  526.
1791.  Ar.  säkija: 'Bewässerungsgraben,  -kanal';  hieraus mit  ar.  Art.  und  Imäla  [ä  >  e]  sp.  pg. acequia,  pg.  azequia;  kat.  cequia,  ciquia, siz.  saya,  sayuni  'Wassergraben,  Be- wässerungskanal'. [DE  34.  Eguilaz  24/25. ML  7594.
1792.  Ar.  sakika:
'Eine  Seite  des  Kopfes'  [vom  Vb.  sakka 'spalten'],  'einseitiges  Kopfweh';  hieraus sp.  jaqueca,  pg.  xaqueca,  enxaqueca 'dass.,  Migräne'.  [DE  217.  Eguilaz  512. ML  7673.
1793.  Ar.  sakima:
'Halfter' ;  hieraas  sp.  jäquima,  pg.  xd- quema  [Constancio  Dicc  974a]  'dass.'. [DE  353.    Eguilaz  512.
1794.  Pers.  säkirlät:
'Mit  Kermes  oder  Cochenille  rot  gefärbtes Kleid'  [aus  ar.  siklät  >  dtsch.  Siklat, 'schwerer  farbiger  Seidenstoö',  das  selbst aus  lat.  cyclas.  gr.  KUKXdi;  stammt], hieraus  mlat.  scarlatum  'Scharlach  als Stoß',  it.  scarlatto,  afrz.  escarlate,  nfrz. icarlate,  sp.  pg.  escarlata ;  engl,  scarlet, mhd.  scharlät,  ndl.  scharlaken  [mit  An- lehnung an  laken  'Tuch'],  dtsch.  Schar- lach; das  letztere  Wort  auch  zur  Be- zeichnung einer  Krankheit,  ebenso  frz. fihre  scarlatine,  russ.  skarlatina,  poln. szkarlatyna,  cech.  Sarlatina.  [Eguilaz 391.    ML  7661.    Gorjajew  322.
1795.  Ar.  sakk:
'Zweifel,  Schwierigkeit',  vulg.  mit  Art. es-sekk;  hieraus  sp.  (alt)  enjeco,  pg.  en- xeco  'Schwierigkeit,  Schaden,  Strafe'. [DE  261.    Eguilaz  390.    ML  7686.
1796.  Ar.  sakkä': 'Wasserträger',  ebenso  tk.  ['der  gegen Lohn  Wasser  transportiert'  im  Gegen- satze zum  sugu,  sngy  'der  auf  eigene Rechnung  mit  Wasser  hausieren  geht', vgl.  MO  XVII,  142,  Nr.  7];  hieraus  mit ar.  Art.  sp.  azacdn  'Wasserträger;  Ecken- steher' [Dicc  Gast  295bl,  pg.  oQacal 'Wasserträger  und  -Verkäufer';  rum. saca  'Wasserkarren,  -faß  der  Wasser-
143
[Ar.  sakkat.
träger',  sacagiu  'Wasserträger'].  [DE 221/222.  Eguilaz315.  Löbel  EITAP  79.
1797.  Ar.  sakkät:
'Althändler,  Trödler';  aus  sük  as- »akkätln  'Markt  der  Trödler'  wurde  sp. zacatin  'Plätzchen  oder  Straße,  wo  Tröd- ler wohnen',  'kleiner  Platz',  siz.  zügatu 'Delikatessenhandlung;  Ort  von  zweifel- haftem Rufe'.  [DE  356/358.  Eguilaz 517.    GrSVodSic  250.
1798.  Tk.  saklii:
[Vom  Stamme  jak,  sak  'recht,  wach; wach  sein,  beobachten,  hüten'  Vämbery TktEtWb  S.  1 1 1,  Nr.  122],  Infin.  saklamak 'verbergen,  bewahren,  schützen';  hieraus russ.  saklja  'Hütte  der  Bewohner  im Kaukasus'.
1799.  Ar.  sakr:
'Jagdfalke  Falco  sacer';  hieraus  mlat. sacer  [die  Form  dieses  Wortes  ist  viel- leicht in  Anlehnung  an  gr.  lepal  <^  iepö? gewählt  worden],  mgr.  odKpe,  kat.  sp. pg.  sacre,  frz.  sacre,  it.  sncro,  pg.  gafaro 'Falke';  dtsch.  Sackerfalk,  engl,  saker, sacre;  russ.  sokol,  klruss.  poln.  sokol, öech.  sokol,  serb.  soko,  bulg.  soA-o^  'Falke'. —  Die  Jagd  mit  Falken  erlebte  im  MA im  feudalen  Europa  eine  hohe  Blüte, schrieb  doch  FRIEDRICH  II.  sogar  ein Buch  de  arte  venandi  cum  avibus.  Von Deutschland  und  Byzanz  verbreitete  sich dieser  Sport  zunächst  in  das  östliche Europa  und  dann  bei  den  Völkern  Asiens, bes.  an  den  mittelasiatischen  Höfen  und bei  den  Nomaden  der  Steppe  und  den Beduinen  der  Wüste.  Bei  den  letzteren ist  sie  in  manchen  Gegenden  noch heutigen  Tages  eine  eifrig  betriebene Beschäftigung.  [DE  33S.  Eguilaz  488. Suohlati,  Die  dtsch.  Vogelnamen.  Straß- burg 1909.    S.  333/334.
1800.  Tk.  saksy:
'Blumentopf,  Porzellan vase'  [Kel6kian Kämüs  659a,  mit  Abbildung];  hieraus rum.  sacsie  'Blumentopf.
1801.  Tk.  sakyz:
```


## [2026-09-14T02:03:56.455Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%82%D9%84%D8%A7%D8%B7%D9%88%D9%86",
 "prompt": "Give the etymology of Arabic/Persian سقلاطون and any related سقلاط / سقرلاط: is it from Greek σιγιλλᾶτος / Latin sigillatus, or from Greek κυκλάς? Quote verbatim."
}
```


## [2026-09-14T02:03:58.077Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%82%D8%B1%D9%84%D8%A7%D8%B7",
 "prompt": "Persian/Arabic سقرلاط: give the etymology verbatim and the meaning. Is it linked to Arabic سقلاط / Latin sigillatus and to English scarlet?"
}
```


### [2026-09-14T02:04:00.298Z] TOOL RESULT

```
Based on the Wiktionary page provided, I cannot find any etymology information for سقلاطون. The page only states:

"**سِقِلّاطُون** [•] (siqillāṭūn) m: alternative form of _[سِقِلّاط](/wiki/%D8%B3%D9%82%D9%84%D8%A7%D8%B7#Arabic "سقلاط")_ (siqillāṭ)"

The content does not discuss whether the word derives from Greek σιγιλλᾶτος, Latin sigillatus, Greek κυκλάς, or any other source. To answer your question about etymological origins, I would need access to a different resource that provides historical linguistic information.
```


### [2026-09-14T02:04:01.752Z] TOOL RESULT

```
Based on the Wiktionary page provided, I can only offer limited information:

The entry shows **سِقِرْلَاط** (siqirlāṭ) is an Arabic masculine noun, described as "alternative form of سِقِلّاط (siqillāṭ)." However, the page contains no etymology section explaining its origins or connections to other languages.

The content does not address whether this word links to Latin *sigillatus* or English "scarlet," nor does it provide the detailed etymological information you're requesting. To answer your question about linguistic connections, you would need to consult a comprehensive etymological dictionary rather than this Wiktionary entry, which lacks such analysis.
```


## [2026-09-14T02:04:04.889Z] TOOL CALL #78: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%82%D9%84%D8%A7%D8%B7",
 "prompt": "Arabic سقلاط (siqillāṭ): give the etymology section verbatim and the definition. Does it come from Byzantine Greek σιγιλλᾶτος / Latin sigillatus?"
}
```


### [2026-09-14T02:04:09.970Z] TOOL RESULT

```
# Etymology of سقلاط (siqillāṭ)

**Etymology Section (Verbatim):**
"From Byzantine Greek σιγιλλᾶτος (sigillâtos), σιγιλλᾶτον (sigillâton), from Latin sigillātus (literally 'sealed'), the epithet of some kind of fabric, since sealings are most iconically of red colour."

**Definition:**
Scarlet cloth

**Answer to Your Question:**
Yes, the word does originate from those sources. It traces back through Byzantine Greek forms to the Latin root *sigillātus*, which literally means "sealed." The term was applied to a specific type of fabric, likely named for its characteristic red color associated with seal impressions.
```


## [2026-09-14T02:04:19.421Z] TOOL CALL #79: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/assignat",
 "prompt": "Give the etymology of assignat verbatim: French assignat, date, Latin assignatum, and what it meant (paper money of the French Revolution)."
}
```


## [2026-09-14T02:04:20.920Z] TOOL CALL #80: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sign",
 "prompt": "Give the etymology of sign (n.) verbatim, especially the Latin signum and its PIE derivation (is it from *sekw- 'to follow' or *sek- 'to cut'?), and any statement of uncertainty."
}
```


### [2026-09-14T02:04:22.174Z] TOOL RESULT

```
# Etymology of Assignat

**French Origin:** "French _assignat_"

**Latin Root:** "Latin _assignatus_, past participle of _assignare_/_adsignare_"

**Date:** 1790

**Meaning:** The term referred to "paper money of the French Revolution" that was "based on the security of confiscated Church lands" but "was over-issued and the value quickly deteriorated."
```


### [2026-09-14T02:04:26.465Z] TOOL RESULT

```
# Etymology of Sign (n.)

**Latin Origin:**
The word comes from Latin *signum* meaning "identifying mark, token, indication, symbol; proof; military standard, ensign; a signal, an omen."

**PIE Derivation — Competing Theories:**

The source presents two conflicting etymological accounts:

1. **Watkins' Theory:** *signum* derives from PIE *\*sekw-no-*, meaning "standard that one follows," from the root *\*sekw-* meaning "to follow."

2. **De Vaan's Theory:** *signum* comes from PIE *\*sekh-no-* meaning "cut," from PIE root *\*sek-* "to cut." De Vaan argues this represents "a semantic shift of *\*sek-no-* 'what is cut out', 'carved out' > 'sign'."

**Statement of Uncertainty:**

De Vaan acknowledges ambiguity by also proposing that Hebrew *sakkin* and Aramaic *sakkin* (both meaning "slaughtering-knife") and the PIE word "are probably borrowed from an unknown third source," leaving the ultimate origin unclear.

The page thus presents competing hypotheses without definitively resolving which etymology is correct.
```


## [2026-09-14T02:04:37.590Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/signum\" \\\n \"https://www.etymonline.com/word/scarlet\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D8%A7%DA%AF%D8%B1%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%DA%A9%D9%86%D8%A7%D8%B3\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D8%AC%D9%84\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sek%CA%B7-\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%B2\" \\\n \"https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%82%D9%84%D8%A7%D8%B7\" \\\n \"https://www.etymonline.com/word/assignat\" \\\n \"https://www.etymonline.com/word/sign\" \\\n \"https://archive.org/download/oldpers/oldpers_djvu.txt\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 440, root Sekw (to follow): verification of Nourai's chart\" 2>&1 | tail -1\ndone"
}
```


### [2026-09-14T02:04:44.833Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8b12a44986079e68.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1a47865c3a12fa5c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3ffce5baf57682b7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/59288a988faf62b6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8a5993b239816bcc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6e753b4f3424932d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c58668474154e1f6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7b2c819a2414c3c6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dfbc60d2b0eeaacc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/33d832d0b494140b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/82ae82c03e0befaf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/14b1d00a111388e7.txt
```


## [2026-09-14T02:04:49.478Z] TOOL CALL #82: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg440.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/440.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/440.png\nhead -40 /home/sfmqrb/git/rishe/data/verification/page-385.json 2>/dev/null | head -20"
}
```


### [2026-09-14T02:04:49.646Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 75018 Sep 13 22:04 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/440.png
{
  "pdf_page": 385,
  "book_page": 355,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-07",
  "entries": [
    {
      "entry": 0,
      "root": "Peg",
      "verdict": "plausible",
      "modern_form": "PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'",
      "note": "Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong together at all. Root is real and the language label is right; the gloss is a one-sided simplification.",
      "note_fa": "ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ «(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا «Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ریشه واقعی است و برچسب زبانی درست، اما معنای داده‌شده یک‌سویه و ساده‌سازانه است — ادعای نورایی با احتیاط پذیرفتنی است.",
      "sources": [
        "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7",
        "https://en.wiktionary.org/wiki/pectus"
      ],
      "ref_check": [
        {
          "ref": "POK:792",
```


## [2026-09-14T02:05:45.893Z] TOOL CALL #83: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B4%D8%A7%DA%AF%D8%B1%D8%AF/",
 "prompt": "Show the فرهنگ معین (Mo'in) entry for شاگرد verbatim, including any bracketed origin tag such as [په.] (Pahlavi) and the definitions."
}
```


### [2026-09-14T02:05:49.590Z] TOOL RESULT

```
# فرهنگ معین Entry for شاگرد

According to the Moein dictionary section on this page, the entry reads:

"(گِ ) (اِ. ) کسی که نزد دیگری علم و ادب یا هنر آموزد."

This translates to: someone who learns science, literature, or art from another person. The bracketed notations "(گِ)" and "(اِ.)" indicate grammatical markers, though the specific origin tag is not explicitly shown in this particular dictionary entry on the provided page.
```


## [2026-09-14T02:05:54.043Z] TOOL CALL #84: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%B4%D8%A7%DA%AF%D8%B1%D8%AF/\" --note \"pdf page 440, root Sekw: Mo'in entry for شاگرد (MON:1999 check)\" 2>&1 | tail -1"
}
```


### [2026-09-14T02:05:56.689Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5683e846961fabf0.txt
```


## [2026-09-14T02:13:02.843Z] TOOL CALL #85: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-440.py",
 "content": "# -*- coding: utf-8 -*-\nimport json\n\nW_SEKW = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sek%CA%B7-\"\nW_SIGNUM = \"https://en.wiktionary.org/wiki/signum\"\nW_SHAGERD = \"https://en.wiktionary.org/wiki/%D8%B4%D8%A7%DA%AF%D8%B1%D8%AF\"\nW_ESKENAS = \"https://en.wiktionary.org/wiki/%D8%A7%D8%B3%DA%A9%D9%86%D8%A7%D8%B3\"\nW_SIJILL = \"https://en.wiktionary.org/wiki/%D8%B3%D8%AC%D9%84\"\nW_AZ = \"https://en.wiktionary.org/wiki/%D8%A7%D8%B2\"\nW_ZIR = \"https://en.wiktionary.org/wiki/%D8%B2%DB%8C%D8%B1\"\nW_SIQ = \"https://en.wiktionary.org/wiki/%D8%B3%D9%82%D9%84%D8%A7%D8%B7\"\nE_SCARLET = \"https://www.etymonline.com/word/scarlet\"\nE_ASSIGNAT = \"https://www.etymonline.com/word/assignat\"\nE_SIGN = \"https://www.etymonline.com/word/sign\"\nKNT_TXT = \"https://archive.org/download/oldpers/oldpers_djvu.txt\"\nABADIS_SH = \"https://abadis.ir/fatofa/%D8%B4%D8%A7%DA%AF%D8%B1%D8%AF/\"\n\nnodes = []\n\nnodes.append({\n  \"id\": 1,\n  \"lang\": \"Avestan\",\n  \"words\": \"haša-kerta, aša-gerd; haxay, haši; haxa-maniš\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"Of the three items only haxay- is genuinely Avestan. Bartholomae, AirWb. col. 1744, lists \"\n    \"'j. (1 g. 1 p) haxay-: haxi-, haši-, m. 1) Freund, Genosse' (Y.62.8, V.4.44, Yt.10.116), beside the \"\n    \"verbal root 'hak- v. sequi' (AirWb. s.v., pres. haca-, ptc. haxta-), so 'friend, companion' = \"\n    \"'the one who accompanies'. — haša-kerta / aša-gerd is NOT an attested Avestan word: it is \"\n    \"Bartholomae's Old-Iranian reconstruction *hašākarta- (ZAW p.38), set up to explain Manichaean \"\n    \"Middle Persian hašāgērd 'discipulus' and NP šāgird, and analysed by him as *haxai- (jAw. haxay-) \"\n    \"+ karta- 'made', literally 'one who has to do with the service of the priestly colleague'; the \"\n    \"second form aša-gerd is in reality the Armenian loanword ašakert 'pupil' that Bartholomae cites \"\n    \"on the same page, so the box mixes an Old-Iranian reconstruction with an Armenian borrowing and \"\n    \"labels both 'Avestan'. — haxa-maniš likewise is Old Persian Haxāmaniš- (Kent p.212), not Avestan; \"\n    \"Nourai repeats it correctly as Old Persian in node 6. Finally the link of haxay-/Skt. sákhi- to \"\n    \"*sekʷ- is expressly doubted by the standard works: Pokorny 896 prints 'wegen des arischen kh \"\n    \"zweifelhaft: ai. sákhā (sakhi-), av. haxay- (haši-), ap. Haxāmaniš-', and Walde-Pokorny II 476 \"\n    \"has the same reservation ('sehr zweifelhaft'), because IE *kʷ should give Indo-Iranian č/k, not kh/x.\"\n  ),\n  \"derivation_fa\": (\n    \"از سه صورت این جعبه تنها haxay- اوستایی راستین است: بارتولمه در «فرهنگ ایرانی باستان» ستون ۱۷۴۴ آن را \"\n    \"haxay-/haši- «دوست، همراه» آورده و آن را به ستاک فعلی hak- «پیروی کردن» می‌پیوندد. صورت haša-kerta \"\n    \"واژه‌ای اوستایی نیست، بلکه بازسازی بارتولمه در ZAW ص۳۸ یعنی ایرانی باستان *hašākarta- است که برای \"\n    \"توضیح فارسی میانهٔ مانوی hašāgērd و فارسی نو «شاگرد» پیشنهاد شده و از *haxai- + karta- «ساخته، گماشته» \"\n    \"تشکیل می‌شود؛ و aša-gerd در حقیقت وام‌واژهٔ ارمنی ašakert «شاگرد» است، نه صورتی اوستایی. haxa-maniš نیز \"\n    \"پارسی باستان (Haxāmaniš-) است نه اوستایی. افزون بر این، پیوند haxay- با ریشهٔ *sekʷ- در پوکورنی (ص۸۹۶) \"\n    \"و والده-پوکورنی (ج۲ ص۴۷۶) «بسیار مشکوک» خوانده شده، زیرا kʷ هندواروپایی در هندوایرانی باید č/k بدهد نه kh/x. \"\n    \"پس ادعای نورایی در کلیت پذیرفتنی است ولی برچسب زبانی جعبه نادرست و پیوند ریشه‌شناختی مورد تردید است.\"\n  ),\n  \"sources\": [W_SEKW, W_SHAGERD],\n  \"ref_check\": [\n    {\"ref\": \"ZAW:38\", \"status\": \"supports\",\n     \"note\": \"ZAW_pages.txt leaf 62 (= printed p.38): 'hašâgêrd (MÜLLER gîrd) discipulus 30, 32 … aber im Np. wird شاگرد šagird gesprochen. … setze ich uriran. *hašākarta- an, d. i. eigentlich der mit der Wartung, dem Dienst des Priesterkollegen … zu tun hat, eine Zusammensetzung aus *haxai- (jAw. haxay-) …' — exactly Nourai's haša-kerta > šâgerd arrow, but as an Old-Iranian reconstruction, not an Avestan word; the same page cites 'das entlehnte arm. ašakert', which is Nourai's second form aša-gerd.\"},\n    {\"ref\": \"ZAW:242\", \"status\": \"supports\",\n     \"note\": \"ZAW_pages.txt leaf 266 (= printed p.242): 'Sp. 1744, Z. 33 und 43 ff. füge in den Noten zu jaw. haxay- Freund und zu ap. haxāmaniš- EN. hinzu: Vgl. mpT. hašâgêrd, np. šāgird Schüler.' — Bartholomae himself ties haxay-, Haxāmaniš- and šāgird together, which is precisely the content of this box.\"},\n    {\"ref\": \"POK:896\", \"status\": \"partial\",\n     \"note\": \"POK_full.txt (root sekʷ-1 'to follow', pp.896-897) has haxay- but only under the reservation 'because of Aryan kh dubious: Old Indic sakhā (sakhi-), Avestan haxay- (haši-), ap. Haxāmaniš-'. Pokorny does not list any *hašākarta-.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AirWb. col. 1744 s.v. haxay-; col. 1742 s.v. 1hak-\", \"stance\": \"supports\",\n     \"note\": \"BRT.txt: 'j. (1 g. 1 p) haxay-: haxi-, haši-, m. 1) Freund, Genosse' (Y.62.8; V.4.44; Yt.10.116) and 'j., g. 1hak- V. sequi. Praes. … haca- … PPfP. haxta-'. Confirms the word, the gloss and the root, but knows no Avestan *haša-karta-.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II 476 (WLD_Bd2_1927_dli_106624_djvu.txt l.30887)\", \"stance\": \"partial\",\n     \"note\": \"'Wegen ar. kh sehr zweifelhaft ai. sákhā (sakhi-) Gefährte, Genosse, Freund, av. haxay- (haši-) ds., ap. Haxamaniš- Ἀχαιμένης' — Walde-Pokorny accept the words as a group but rate their attachment to *sekʷ- as very doubtful.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. socius (LAT.txt l.58862 ff.)\", \"stance\": \"partial\",\n     \"note\": \"'En indo-iranien, il y a un mot remarquable et sûrement ancien: véd. sákhā …, av. haxa (dat. hašē, nom. pl. haxayō) compagnon. Le rapprochement s'impose; il n'exclut pas celui avec sequor, car -kh- peut alterner avec …' — same words, same hesitation about the aspirate.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p.43 s.v. hašāgird\", \"stance\": \"supports\",\n     \"note\": \"'hašāgird [hš\\\\'klt! | M hš\\\\'gyrd, N šāgird] disciple, pupil' — the Middle Persian link between Bartholomae's *hašākarta- and NP šāgird.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 2,\n  \"lang\": \"Persian\",\n  \"words\": \"šâgerd «شاگرد»; Haxâmaneš «هخامنش»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"شاگرد: Old Iranian *hašā-kr̥ta- (Bartholomae ZAW 38) > Manichaean Middle Persian hašāgērd, Book \"\n    \"Pahlavi hašāgird [hš'klt] 'disciple, pupil' (MacKenzie 43) > New Persian šāgird/šāgerd. The change is \"\n    \"the regular Middle-to-New-Persian loss of initial h- before a long vowel plus the collapse of the \"\n    \"pretonic syllable (hašāgird > (h)ašāgird > šāgird), the same treatment that gives the Armenian loan \"\n    \"ašakert (borrowed from a Parthian/Middle Persian form in the 5th c. CE, still with the a-) beside \"\n    \"Persian šāgird; -ird > -ard/-erd is the ordinary reflex of -kr̥ta- (cf. dastgerd, Bahmangerd). The \"\n    \"semantic line is 'made a companion/attendant (of a priest or master)' > 'apprentice, pupil'. — \"\n    \"هخامنش: Old Persian Haxāmaniš- (DB 1.6; genitive Haxāmanišahyā AmH 3f), literally 'having the mind \"\n    \"of a friend' = haxā- 'friend' + maniš 'mind, thinking' (Kent, Old Persian, p.212 and §169), Greek \"\n    \"Ἀχαιμένης, whence New Persian هخامنش and the dynastic adjective هخامنشی. The NP form is a learned \"\n    \"revival taken back from the inscriptions in the 19th-20th c., not a continuously transmitted word.\"\n  ),\n  \"derivation_fa\": (\n    \"«شاگرد» از فارسی میانهٔ هَشاگِرد hašāgird (در متون مانوی hašāgērd) «شاگرد، نوآموز» است (مکنزی ص۴۳)، \"\n    \"و آن از ایرانی باستان *hašā-kr̥ta- بازسازی‌شدهٔ بارتولمه. در گذار به فارسی نو «هـ» آغازین پیش از واکهٔ \"\n    \"بلند افتاده و هجای بی‌تکیهٔ نخست فروریخته است: hašāgird > (h)ašāgird > šāgird؛ همان صورت کهن‌تر است که \"\n    \"در ارمنی به شکل ašakert وام گرفته شده. پسوند -gerd بازماندهٔ -kr̥ta- «کرده، ساخته» است (سنجیدنی با \"\n    \"دستگرد، بهمن‌گرد). تحول معنایی: «همراه/خدمتکارِ آموزگار یا موبد» ← «نوآموز، شاگرد». — «هخامنش» از \"\n    \"پارسی باستان Haxāmaniš (کتیبهٔ بیستون ۱٫۶) مرکب از haxā «دوست» و maniš «منش، اندیشه»، یعنی «دوست‌منش»؛ \"\n    \"معین در حاشیهٔ برهان قاطع (ص۲۳۱۶) دقیقاً همین تحلیل را می‌آورد. ادعای نورایی درست است.\"\n  ),\n  \"sources\": [W_SHAGERD, ABADIS_SH],\n  \"ref_check\": [\n    {\"ref\": \"MON:1999\", \"status\": \"partial\",\n     \"note\": \"Mo'in's Farhang-e Farsi does carry شاگرد, but the copy available here (the 2-vol Adena reprint, MON_part1/part2 — different pagination, so p.1999 could not be printed) and the online Mo'in text at abadis.ir give only the definition '(گِ) (اِ.) کسی که نزد دیگری علم و ادب یا هنر آموزد', with no origin tag and no Pahlavi form. The headword and gloss match Nourai; the etymology could not be checked on the cited page.\"},\n    {\"ref\": \"BQT:2316\", \"status\": \"supports\",\n     \"note\": \"Borhan-e Qate' vol.4 (BQT_v4_pages.txt, pdf page 399 = printed 2316), Mo'in's footnote: «هخامنش Haxāmaniš در پارسی باستان مرکب از دو جزء: هخا haxā (دوست: یار) + منش maniš از manah (حس باطنی، فهم و شعور، اندیشیدن) و جمعاً بمعنی دوست‌منش است؛ در یونانی Ἀχαιμένης. بارتولمه AiW» — word for word Nourai's gloss 'with friendly thoughts and manners'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p.43 s.v. hašāgird\", \"stance\": \"supports\",\n     \"note\": \"'hašāgird [hš\\\\'klt! | M hš\\\\'gyrd, N šāgird] disciple, pupil' — MacKenzie himself equates the Pahlavi word with NP šāgird.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien / Armen. Grammatik, HUB.txt ll.4535, 6723\", \"stance\": \"supports\",\n     \"note\": \"'arm. ašakert Schüler — np. šāgird'; 'arm. ašakert = np. šāgird; arm. -kert gemacht = np. -gird' — Hübschmann confirms both the equation and the analysis of the second member as 'made'.\"},\n    {\"src\": \"MON\", \"where\": \"online Mo'in via abadis.ir s.v. شاگرد\", \"stance\": \"partial\",\n     \"note\": \"«(گِ) (اِ.) کسی که نزد دیگری علم و ادب یا هنر آموزد» — definition only, no etymology.\"},\n    {\"src\": \"BQT\", \"where\": \"vol.4 printed p.2316 s.v. هخامنش\", \"stance\": \"supports\",\n     \"note\": \"Mo'in's footnote quoted above; also «هخامنشی … از: هخامنش».\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 3,\n  \"lang\": \"Avestan\",\n  \"words\": \"hačâ; hačâ-adairi\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"Avestan haca 'from, away from, out of' is the instrumental singular of a thematic root-noun \"\n    \"*sekʷo-s 'following' to *sekʷ- (Pokorny 896: 'ai. sacā …, av. haca, ap. hacā von-her, von-aus \"\n    \"(Instr. eines *sekʷo-s folgend)'), so literally 'in the train of' > 'starting from'. It is a real, \"\n    \"very frequent Avestan preposition governing the ablative (Bartholomae passim: 'haca mit Abl.'). \"\n    \"— hačâ-adairi, however, is not a transmitted Avestan compound: aδairi is a separate Avestan \"\n    \"preposition 'unter, unterhalb' (Bartholomae s.v. 'j. adairi Praep. unter, unterhalb'), and the \"\n    \"collocation haca + aδairi is Horn's reconstruction (Grundriss no. 680, p.150) for the prehistory of \"\n    \"Pahlavi azēr / NP zēr, i.e. 'from below'. Wiktionary states the same prehistory in Old Persian \"\n    \"terms (*hacā-adari). The arrow is therefore right in substance but the form is a scholarly \"\n    \"reconstruction printed as if it were an attested Avestan word.\"\n  ),\n  \"derivation_fa\": (\n    \"haca اوستایی «از، از سوی» صورت بایی (instrumental) نام‌ستاکی *sekʷo-s «پیرو» از ریشهٔ *sekʷ- است \"\n    \"(پوکورنی ص۸۹۶) و حرف اضافه‌ای پرکاربرد با ازی (ablative) است. اما hačâ-adairi ترکیبی اوستایی و \"\n    \"گواهی‌شده نیست: aδairi خود حرف اضافهٔ مستقل اوستایی به معنی «زیر، فرودِ» است (بارتولمه، ذیل adairi) \"\n    \"و هم‌نشینی haca + aδairi بازسازی هرن (بند ۶۸۰، ص۱۵۰) برای پیشینهٔ فارسی میانهٔ azēr و «زیر» فارسی است. \"\n    \"بنابراین محتوای پیکان درست است ولی صورت، بازسازی پژوهشی است نه واژهٔ ضبط‌شده — با احتیاط پذیرفتنی است.\"\n  ),\n  \"sources\": [W_SEKW, W_ZIR],\n  \"ref_check\": [\n    {\"ref\": \"POK:896\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt, root sekʷ-1 pp.896-897: 'Old Indic sacā (m. Lok.) together with, by …, Avestan haca, ap. hacā von-her, von-aus (Instr. eines *sekʷo-s folgend)'. Exactly Nourai's 'hačâ: followed from'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AirWb. s.v. adairi (BRT.txt l.3256); s.v. haca (passim)\", \"stance\": \"supports\",\n     \"note\": \"'j. adairi Praep. unter, unterhalb; 1) mit Akk.: aoi haxəm nivōiryeite V.8.69'; and dozens of 'haca mit Abl.' citations. Both elements are real Avestan; no compound haca-aδairi is listed.\"},\n    {\"src\": \"HRN\", \"where\": \"Grundriss no. 680, p.150\", \"stance\": \"supports\",\n     \"note\": \"'zēr unten, unterhalb … aw. haca + aδairi; pāz. azēr, vergl. phlv. ēr' — the very reconstruction Nourai's box prints.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins, sekw-1 (AHD_watkins1985.txt)\", \"stance\": \"silent\",\n     \"note\": \"Watkins lists only the Latin descendants of sekw-1; no Iranian preposition.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 4,\n  \"lang\": \"Pahlavi\",\n  \"words\": \"aj; azěr\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Book Pahlavi ʾc, read az 'from' (Horn writes it 'aj' after the older transliteration of the \"\n    \"Aramaic-derived letter), continues Old Persian hacā / Avestan haca: initial h- was lost before the \"\n    \"stressed vowel and intervocalic -č- was voiced to -z- in the Middle Persian period, giving az; the \"\n    \"same word serves as the postposition aziš 'from it' (MacKenzie s.v. aziš '… postposition (= az) \"\n    \"from'). — azēr 'below, under' (MacKenzie: 'azēr [hcdl | N zēr] below, under'; the heterogram \"\n    \"spells the older haca-) is the univerbation of that az with the old adverb *adari (Av. aδairi), \"\n    \"i.e. *hačā-adari > *azadēr > azēr, with -d- lost and the vowels contracted; beside it Pahlavi has \"\n    \"the simplex ēr 'below' (MacKenzie: 'below ēr, azēr').\"\n  ),\n  \"derivation_fa\": (\n    \"«اَز» پهلوی (نوشتهٔ ʾc؛ هرن به شیوهٔ قدیم aj می‌نویسد) دنبالهٔ hacā پارسی باستان و haca اوستایی است: \"\n    \"«هـ» آغازین افتاده و «چ» میان‌واکه‌ای در فارسی میانه به «ز» بدل شده است (ابدال č > z). همین واژه در \"\n    \"صورت پس‌اضافهٔ aziš «از آن» نیز به کار می‌رود (مکنزی). azēr «زیر، فرودِ» از پیوستن همین az به قید کهن \"\n    \"*adari (اوستایی aδairi) پدید آمده است: *hačā-adari > *azadēr > azēr، با افتادن «د» و ادغام واکه‌ها؛ \"\n    \"در پهلوی صورت سادهٔ ēr «زیر» نیز هست. ادعای نورایی درست است.\"\n  ),\n  \"sources\": [W_AZ, W_ZIR],\n  \"ref_check\": [\n    {\"ref\": \"HRN:12\", \"status\": \"not_found\",\n     \"note\": \"HRN.txt leaf 34 (= printed p.12) contains nos. 49-52 (āmurzīdan, āmōxtan, āmēxtan, ān) — nothing about az. Horn's entry is no. 75 on p.18 (his own index lists 'az 18.'): 'ez von, aus etc., z, z-; ap. hacā; aw. haca; phlv. aj; ai. sácā; kurd. az, ze, z-'. Nourai's page number is wrong; his content is Horn's.\"},\n    {\"ref\": \"HRN:150\", \"status\": \"supports\",\n     \"note\": \"HRN.txt leaf 172 (= printed p.150), no. 680: 'zēr unten, unterhalb. Kās. jīr … zēr, aw. haca + aδairi; pāz. azēr, vergl. phlv. ēr' — Horn gives exactly the Pahlavi azēr and its Avestan source.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p.15 s.v. azēr, aziš; p.30 s.v. ēr\", \"stance\": \"supports\",\n     \"note\": \"'azēr [hcdl | N zēr] below, under'; 'aziš [hcš | M ʾcyš] from him, it; postposition (= az) from'; English-Pahlavi part: 'below ēr, azēr'.\"},\n    {\"src\": \"HRN\", \"where\": \"no. 75 p.18 and no. 680 p.150\", \"stance\": \"supports\",\n     \"note\": \"see ref_check; Horn is the source of both of Nourai's Pahlavi forms.\"},\n    {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (NYB_vol2_glossary.txt)\", \"stance\": \"silent\",\n     \"note\": \"grep for 'azēr'/'azer' in the glossary file returned nothing (the OCR of the glossary does not carry the diacritics); no independent confirmation from Nyberg.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 5,\n  \"lang\": \"Persian\",\n  \"words\": \"az «از»; zîr «زیر»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"«از» is Middle Persian az taken over unchanged into New Persian (and is, per the Miller/\"\n    \"Aghajanian-Stewart frequency dictionary, the third most frequent word of the language); the chain \"\n    \"is PIE *sekʷ- > Proto-Iranian *hácā > OP hacā / Av. haca > MP az > NP از. — «زیر» is MP azēr with \"\n    \"aphaeresis of the unstressed initial a- (azēr > zēr, later zīr with the regular New Persian raising \"\n    \"of majhūl ē to ī in the modern Iranian pronunciation), i.e. OIr. *hačā-adari > azēr > زیر 'under'. \"\n    \"Its prepositional use is a shortening of در زیرِ / به زیرِ 'in/at the underside of'. Wiktionary cites \"\n    \"Horn 1893 and Hübschmann 1895/97 and ESIJa (Rastorgueva-Edel'man) for exactly this chain.\"\n  ),\n  \"derivation_fa\": (\n    \"«از» همان az فارسی میانه است که بی‌تغییر به فارسی نو رسیده؛ زنجیره: هندواروپایی *sekʷ- ← ایرانی \"\n    \"آغازین *hácā ← پارسی باستان hacā / اوستایی haca ← فارسی میانه az ← فارسی نو «از». «زیر» از azēr \"\n    \"فارسی میانه است با افتادن «اَ»ی آغازین بی‌تکیه (azēr > zēr) و سپس تبدیل «ای» مجهول به «ای» معروف در \"\n    \"تلفظ امروز ایران (zēr > zīr). کاربرد حرف‌اضافه‌ای آن کوتاه‌شدهٔ «در زیرِ/به زیرِ» است. ویکی‌واژه برای همین \"\n    \"زنجیره به هرن (۱۸۹۳)، هوبشمان (۱۸۹۵) و فرهنگ ریشه‌شناختی زبان‌های ایرانی راستارگویوا-ادلمان ارجاع می‌دهد. \"\n    \"ادعای نورایی درست است.\"\n  ),\n  \"sources\": [W_AZ, W_ZIR],\n  \"ref_check\": [\n    {\"ref\": \"BQT:113\", \"status\": \"not_checked\",\n     \"note\": \"Borhan-e Qate' vols 1-2 exist here only as rough Persian-script OCR (BQT_v1_pages.txt); leaves 323-327, which cover the از region of vol.1, contain no Latin characters at all, so Mo'in's Latin-script etymological footnote cannot be recovered, and there is no local PDF of vols 1-2 to render as an image (tools/ref_page.py: 'no scan of BQT covers printed page 113'); archive.org borhan-ghate-v1 has no djvu.txt.\"},\n    {\"ref\": \"BQT:1051\", \"status\": \"not_checked\",\n     \"note\": \"Same problem for vol.2 (BQT_v2_pages.txt leaves ~508-513, the زو/زی region = printed ~1051): Persian-script OCR only, no Latin footnotes, no page scan available locally.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"no. 75 p.18; no. 680 p.150\", \"stance\": \"supports\",\n     \"note\": \"'ez von, aus etc. … ap. hacā; aw. haca; phlv. aj' and 'zēr unten, unterhalb … aw. haca + aδairi; pāz. azēr'.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p.15\", \"stance\": \"supports\",\n     \"note\": \"'azēr [hcdl | N zēr] below, under' — MacKenzie equates MP azēr with NP zēr.\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, online text (abadis/vajehyab)\", \"stance\": \"silent\",\n     \"note\": \"the online Mo'in text for از/زیر carries definitions only, without the print edition's origin tags.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 6,\n  \"lang\": \"Old Persian\",\n  \"words\": \"hačâ; haxâ; haxâ-maniš\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"All three are on Kent's Lexicon page 212, the page Nourai cites. hacā 'from' governs the ablative \"\n    \"(DB 1.36, 40, 61; DNa 18; XPh 16 etc.); Kent derives it as 'instr. sg. of thematic root-noun to \"\n    \"pIE *sekʷ- follow'. haxā- 'friend' is attested only inside the dynastic name: Haxāmaniš- \"\n    \"'Achaemenes' (DB 1.6, AmH 3f) = haxā- + maniš, 'having the mind of a friend', Elamite \"\n    \"ha-ak-qa-man-nu-iš, Akkadian a-ha-ma-ni-iš, Greek Ἀχαιμένης; the derived adjective Haxāmanišiya- \"\n    \"'Achaemenian' appears in almost every royal inscription. The reservation noted at node 1 applies to \"\n    \"haxā- alone: Skt. sákhā / Av. haxay- / OP haxā- show Indo-Iranian kh/x where *sekʷ- would predict \"\n    \"č/k, so Pokorny and Walde-Pokorny call the attachment doubtful; hacā itself is beyond dispute.\"\n  ),\n  \"derivation_fa\": (\n    \"هر سه صورت در همان صفحهٔ ۲۱۲ فرهنگ کنت آمده است: hacā «از» با ازی (DB 1.36 و …) که کنت آن را صورت \"\n    \"بایی نام‌ستاکی از ریشهٔ هندواروپایی *sekʷ- «پیروی کردن» می‌داند؛ haxā- «دوست» که تنها در نام \"\n    \"Haxāmaniš- «هخامنش» (بیستون ۱٫۶) دیده می‌شود، به معنی «دوست‌منش»، در ایلامی ha-ak-qa-man-nu-iš و \"\n    \"یونانی Ἀχαιμένης؛ و صفت Haxāmanišiya- «هخامنشی». تنها نکتهٔ محل تردید haxā- است: «خ» هندوایرانی در \"\n    \"برابر *kʷ هندواروپایی انتظار نمی‌رود و از همین رو پوکورنی و والده-پوکورنی این پیوند را مشکوک می‌شمارند. \"\n    \"در مجموع ادعای نورایی درست است.\"\n  ),\n  \"sources\": [KNT_TXT, W_SEKW],\n  \"ref_check\": [\n    {\"ref\": \"KNT:212\", \"status\": \"supports\",\n     \"note\": \"Kent, Old Persian, Lexicon p.212 (archive.org 'oldpers' djvu text, between the running heads 'LEXICON' and 'LEXICON 213'): 'Haxāmaniš- sb. Achaemenes …, founder of the Achaemenian dynasty … From haxā-, LAv. nsm. haxa, Skt. nsm. sákhā friend, + maniš …'; 'haca prep. from: GAv. hacā, LAv. hacā, Skt. sácā with …: instr. sg. of thematic root-noun to pIE *sekʷ- follow, Av. hacaite, Skt. sácate, Gk. hépetai, Lt. sequitur'. The local KNT.txt is truncated at 'vaz-' and does not reach the h-section, so this page was read from the archive.org text of the same edition; the same statements also stand in KNT §100 ('haxā- friend in Haxā-maniš Achaemenes, Skt. nom. sákhā') and §169 ('Haxā-maniš Having the mind of a friend, Achaemenes').\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AirWb. col. 1744 s.v. haxay-\", \"stance\": \"supports\",\n     \"note\": \"gives the Avestan counterpart haxay-/haši- 'Freund, Genosse' beside 'ap. Haxāmaniš-'.\"},\n    {\"src\": \"POK\", \"where\": \"IEW 896 (sekʷ-1)\", \"stance\": \"partial\",\n     \"note\": \"'Avestan haca, ap. hacā von-her' is confirmed; but 'because of Aryan kh dubious: … ap. Haxāmaniš-'.\"},\n    {\"src\": \"BQT\", \"where\": \"vol.4 printed p.2316, Mo'in's footnote on هخامنش\", \"stance\": \"supports\",\n     \"note\": \"«هخامنش Haxāmaniš در پارسی باستان مرکب از دو جزء: هخا haxā (دوست) + منش maniš … بمعنی دوست‌منش».\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 7,\n  \"lang\": \"Latin\",\n  \"words\": \"signum; sigillatus\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"Latin signum 'identifying mark, sign; military standard' is attached to *sekʷ- by Watkins (AHD \"\n    \"appendix, sekw-1 §5: 'Suffixed form *sekʷ-no- in Latin signum, identifying mark, sign (< standard \"\n    \"that one follows)'), and that is the authority Nourai cites. It is not, however, the only or the \"\n    \"current view: de Vaan (EDL 2008, 563) derives signum rather from *sek- 'to cut' (*sek-no- 'what is \"\n    \"cut out, carved' > 'sign'), and Wiktionary prints both possibilities side by side; Ernout-Meillet \"\n    \"list signum with its derivatives sigillum, sigillō, sigillatus but make no connection with sequor, \"\n    \"and Pokorny's sekʷ-1 (896) does not mention signum at all. — The second item is also mis-glossed: \"\n    \"sigillātus is not 'a record' but the perfect participle/adjective of sigillāre 'to seal, to mark \"\n    \"with little figures' (Ernout-Meillet: 'sigillum n.: petite image, statuette; seing … sigillatus \"\n    \"(sur le sort de sigillatus, v. O. Bloch sous écarlate)'), from sigillum, diminutive of signum.\"\n  ),\n  \"derivation_fa\": (\n    \"واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ AHD (ذیل sekw-1 بند ۵) signum لاتین را از صورت پسوندی \"\n    \"*sekʷ-no- «درفشی که از پی آن می‌روند» می‌گیرد و همین مأخذ استناد نورایی است؛ ولی این تنها رأی نیست: \"\n    \"دِ ڤان (۲۰۰۸، ص۵۶۳) آن را از ریشهٔ *sek- «بریدن» می‌داند (*sek-no- «آنچه بریده و کنده شده» ← «نشانه») و \"\n    \"ویکی‌واژه هر دو را کنار هم می‌آورد؛ ارنو-مِیه نیز signum و مشتقاتش sigillum و sigillatus را می‌آورد \"\n    \"ولی هیچ پیوندی با sequor نمی‌بیند و پوکورنی در ص۸۹۶ اصلاً نامی از signum نمی‌برد. افزون بر این، \"\n    \"معنای «a record» برای sigillatus نادرست است: این واژه صفت مفعولی sigillāre «مهر زدن، نگاره‌دار کردن» \"\n    \"است، نه نام. پس ادعای نورایی با احتیاط پذیرفتنی است.\"\n  ),\n  \"sources\": [W_SIGNUM, E_SIGN],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt s.v. sekw-1: '5. Suffixed form *sekʷ-no- in Latin signum, identifying mark, sign (< \\\"standard that one follows\\\"): SEAL1, SEGNO, SIGN; ASSIGN, CONSIGN, DESIGNATE, INSIGNIA, RESIGN. [Pok. 1. sekʷ- 896.]' — exactly the arrow Nourai draws.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. signum (LAT.txt l.58208 ff.)\", \"stance\": \"partial\",\n     \"note\": \"'signum, -ī n.: signe, marque distinctive … Dérivés et composés: sigillum n.: petite image, statuette; seing … sigillatus (sur le sort de sigillatus, v. O. Bloch sous écarlate); signō, -ās … assignō … resignō' — the whole family is there (including the Bloch cross-reference to écarlate, i.e. to node 10), but no derivation from sequor.\"},\n    {\"src\": \"POK\", \"where\": \"IEW 896-897, sekʷ-1\", \"stance\": \"silent\",\n     \"note\": \"Pokorny's Latin material is sequor, sector, secta, secundus, sequester, secus, socius — signum is not listed under this root.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. sigillate, sign\", \"stance\": \"supports\",\n     \"note\": \"'sigillate, adj., decorated with marks. — L. sigillātus, pp. of sigillāre, to mark with a sign or seal, fr. sigillum'; and s.v. scarlet 'L. sigillum (for *signolom), seal, dimin. of signum, sign. See sign.'\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 8,\n  \"lang\": \"Arabic\",\n  \"words\": \"siqillât; sejell\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Both Arabic words are Latin loans that reached Arabic through Byzantine Greek. سِقِلَّاط siqillāṭ \"\n    \"(also سِقِرْلَاط siqirlāṭ, سِقِلَّاطُون siqillāṭūn) 'scarlet cloth' is from Byzantine Greek σιγιλλᾶτος / \"\n    \"σιγιλλᾶτον, from Latin sigillātus 'sealed, stamped with little figures', the epithet of a fabric \"\n    \"(terra/textilia sigillata), the red colour being the colour of seal-wax — precisely Nourai's gloss \"\n    \"'with little images'. سِجِلّ sijill 'register, sealed document' (Qurʾān 21:104) is the same Latin \"\n    \"sigillum 'seal, sealed document' via Byzantine Greek σιγίλλιον, alongside Syriac sīgīlīōn / sagīlā; \"\n    \"Jeffery, Foreign Vocabulary of the Qurʾān, discusses the word under Sijill and notes 'Gk. σιγίλλον \"\n    \"~ Lat. sigillum, used in Byzantine Greek for an Imperial [rescript]'. A minority view (Lokotsch no. \"\n    \"1794) derives the cloth-word instead from Latin cyclas / Greek κυκλάς; the Greek σιγιλλᾶτος \"\n    \"derivation is the one adopted by Klein and current Wiktionary.\"\n  ),\n  \"derivation_fa\": (\n    \"هر دو واژهٔ عربی وام‌واژه‌هایی لاتین‌اند که از راه یونانی بیزانسی به عربی رسیده‌اند. «سِقِلّاط» (و گونه‌های \"\n    \"سِقِرْلاط و سِقِلّاطون) «پارچهٔ سرخ گران‌بها» از یونانی بیزانسی σιγιλλᾶτος و آن از لاتین sigillātus «مهرزده، \"\n    \"نگاره‌دار» است — همان معنایی که نورایی «with little images» می‌آورد؛ سرخی رنگ از رنگ موم مهر گرفته شده \"\n    \"است. «سِجِلّ» «دفتر، سند مهرشده» (قرآن، انبیاء ۱۰۴) از همان lat. sigillum از راه σιγίλλιον یونانی بیزانسی \"\n    \"و سریانی sīgīlīōn است؛ جفری در «واژگان دخیل در قرآن» همین را می‌گوید. رأی اقلیت (لوکوچ، شمارهٔ ۱۷۹۴) \"\n    \"سِقِلّاط را از cyclas لاتین/κυκλάς یونانی می‌داند، ولی کلاین و ویکی‌واژه همان sigillātus را می‌پذیرند. \"\n    \"ادعای نورایی درست است.\"\n  ),\n  \"sources\": [W_SIQ, W_SIJILL],\n  \"ref_check\": [\n    {\"ref\": \"AHD:1159\", \"status\": \"not_checked\",\n     \"note\": \"AHD:1159 is a page of the main body of the American Heritage Dictionary, New College Edition (the s.v. 'scarlet' entry); the local AHD file is only Watkins's Indo-European appendix (AHD_watkins1985.txt), which has no entry for scarlet or siqillat. The identical chain is however printed by Klein (see consulted).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. scarlet (KLN_1971.txt l.214132; KLN_1966.txt l.33972) and s.v. ciclatoun\", \"stance\": \"supports\",\n     \"note\": \"'scarlet, n. — ME. scarlat … fr. ML. scarlatum …; from Pers. sāqirlāt, itself borrowed fr. Arab. siqillāt, tissue adorned with seals, which is a loan word fr. L. sigillatus, sealed, pp. of sigillare, to seal, fr. sigillum (for *signolom), seal, dimin. of signum, sign.'; and 'ciclaton … fr. Arab. siqillāt, tissue adorned with seals. See scarlet.'\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery s.v. Sijill (FVQ.txt ll.10305-10323)\", \"stance\": \"supports\",\n     \"note\": \"'(Sijill) … The meaning of Sigill in this eschatological passage was unknown … Gk. σιγίλλον ~ Lat. sigillum, used in Byzantine Greek for an Imperial …'\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1794 (LKT.txt l.4070)\", \"stance\": \"partial\",\n     \"note\": \"'Pers. sāḳirlāt … [aus ar. siḳlāt > dtsch. Siklat, schwerer farbiger Seidenstoff, das selbst aus lat. cyclas, gr. κυκλάς stammt]' — Lokotsch has the same Arabic > Persian step but a different ultimate Latin source (cyclas, not sigillatus).\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 9,\n  \"lang\": \"Persian\",\n  \"words\": \"saqarlât «سقرلات»; sejel «سجلّ»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Both are Arabic loans in Persian, so a Latin word returns east and then travels west again. \"\n    \"سقرلات / سقرلاط / سقلاط / سقلاطون saqerlāt is the Arabic siqillāṭ ~ siqirlāṭ adopted into Persian for \"\n    \"the rich figured silk woven at Baghdad; Mo'in (Farhang-e Farsi s.v. سقلاطون) marks it معرّب and \"\n    \"defines it «نوعی پارچهٔ ابریشمی زردوزی‌شده که آن را در بغداد می‌بافتند و شهرت بسیار داشته؛ پارچه‌ای نفیس به \"\n    \"رنگ سرخ یا کبود», i.e. a fine cloth 'red or dark blue' — which is where Nourai's 'a type of cloth' \"\n    \"comes from and, incidentally, why the Medieval Latin borrowing could be glossed 'purple'. Klein \"\n    \"states the Persian step explicitly: 'from Pers. sāqirlāt, itself borrowed fr. Arab. siqillāt'. — \"\n    \"سجلّ sejel 'record, register' is Arabic sijill borrowed unchanged (with the Arabic tašdīd kept in \"\n    \"writing), used by Mowlavi in the verse Nourai quotes («غیر حرف و غیر ایما و سجلّ / صد هزاران ترجمان \"\n    \"خیزد ز دل»).\"\n  ),\n  \"derivation_fa\": (\n    \"هر دو واژه عربی‌اند که به فارسی وام داده شده‌اند؛ یعنی واژه‌ای لاتین از راه عربی به شرق آمده و سپس دوباره \"\n    \"به غرب بازگشته است. «سقرلات/سقرلاط/سقلاط/سقلاطون» همان siqillāṭ عربی است؛ معین در فرهنگ فارسی ذیل \"\n    \"«سقلاطون» آن را «معرّب» می‌خواند و چنین تعریف می‌کند: «نوعی پارچهٔ ابریشمی زردوزی‌شده که آن را در بغداد \"\n    \"می‌بافتند و شهرت بسیار داشته. پارچه‌ای نفیس به رنگ سرخ یا کبود» — همین معنا در جعبهٔ نورایی آمده است. \"\n    \"کلاین نیز گام فارسی را صریح می‌آورد: «from Pers. sāqirlāt, itself borrowed fr. Arab. siqillāt». \"\n    \"«سجلّ» نیز sijill عربی است که بی‌تغییر (با تشدید) وام گرفته شده و در بیت مولوی که نورایی نقل کرده به کار \"\n    \"رفته است. ادعای نورایی درست است.\"\n  ),\n  \"sources\": [W_SIQ, W_SIJILL, E_SCARLET],\n  \"ref_check\": [\n    {\"ref\": \"AHD:1159\", \"status\": \"not_checked\",\n     \"note\": \"page of the AHD New College Edition main body (s.v. scarlet); only Watkins's appendix is on disk here. Klein prints the same Arabic > Persian > Medieval Latin route.\"},\n    {\"ref\": \"ARK:221\", \"status\": \"not_checked\",\n     \"note\": \"ARK = Rokn-zadeh Adamiyyat, Arkān-e Sokhan (Sharq 1347/1968). refs_online.json: 'Not found … nothing digitised on any permitted platform'. No copy available.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. سقلاطون (MON_part1.txt ll.78424-78432)\", \"stance\": \"supports\",\n     \"note\": \"«سقلاطون: [- معر.] سقلاط - سقرلاط - سقرلات - سقلطون - سقلاطین (اِ.) نوعی پارچهٔ ابریشمی زردوزی شده که آن را در بغداد می‌بافتند و شهرت بسیار داشته. پارچه‌ای نفیس به رنگ سرخ یا کبود.» — Mo'in lists Nourai's exact spelling سقرلات as a variant and tags the word معرّب (arabicized).\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. scarlet\", \"stance\": \"supports\",\n     \"note\": \"'from Pers. sāqirlāt, itself borrowed fr. Arab. siqillāt' — the Arabic > Persian arrow.\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1794\", \"stance\": \"supports\",\n     \"note\": \"'Pers. sāḳirlāt: Mit Kermes oder Cochenille rot gefärbtes Kleid [aus ar. siḳlāt] … hieraus mlat. scarlatum' — Persian form and the Arabic source confirmed.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. scarlet; 'French from Persian' list\", \"stance\": \"supports\",\n     \"note\": \"Skeat classes scarlet as '(F.-Pers.)' and lists it among 'French from Persian: check … scarlet'.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 10,\n  \"lang\": \"Latin\",\n  \"words\": \"scarlatum\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"The word is Medieval, not classical, Latin — scarlatum 'a rich (usually but not necessarily red) \"\n    \"cloth', whence Italian scarlatto, Old French escarlate, Spanish/Portuguese escarlata. Most \"\n    \"etymological dictionaries take it straight from the Persian/Arabic cloth-name: Klein 'ML. scarlatum \"\n    \"(whence also It. scarlatto); from Pers. sāqirlāt'; Lokotsch no. 1794 'hieraus mlat. scarlatum \"\n    \"Scharlach als Stoff'; Funk & Wagnalls 'LL scarlatum (< Pers. saqa[rlāt])'; Skeat likewise. But the \"\n    \"step is not certain: Etymonline reports that the word 'often is said to be from a Middle Eastern \"\n    \"source, but perhaps is rather from a Germanic source akin to Old High German scarlachen, \"\n    \"scharlachen (c.1200), from scar \\\"sheared\\\" + lachen \\\"cloth\\\"'. Two further details of the box are \"\n    \"loose: the language should be Medieval Latin, and the gloss 'a purple cloth' renders Mo'in's \"\n    \"«سرخ یا کبود» rather than the usual sense 'rich cloth, scarlet'.\"\n  ),\n  \"derivation_fa\": (\n    \"scarlatum لاتینِ میانه (نه لاتین کلاسیک) است، به معنی پارچه‌ای گران‌بها و معمولاً سرخ، که ایتالیایی \"\n    \"scarlatto و فرانسهٔ کهن escarlate از آن آمده‌اند. بیشتر فرهنگ‌های ریشه‌شناختی آن را مستقیماً از واژهٔ \"\n    \"فارسی/عربی می‌گیرند (کلاین، لوکوچ شمارهٔ ۱۷۹۴، فانک و واگنالز، اسکیت). با این حال این گام قطعی نیست: \"\n    \"اتیمآنلاین یادآور می‌شود که «غالباً گفته‌اند خاستگاهش خاورمیانه‌ای است، ولی شاید از ریشه‌ای ژرمنی باشد، \"\n    \"همانند scarlachen آلمانی علیای کهن از scar «چیده‌شده» + lachen «پارچه»». دو نکتهٔ دیگر: برچسب زبان باید \"\n    \"«لاتین میانه» باشد، و معنای «پارچهٔ ارغوانی» دقیق نیست. پس: با احتیاط پذیرفتنی است.\"\n  ),\n  \"sources\": [E_SCARLET, W_SIQ],\n  \"ref_check\": [\n    {\"ref\": \"AHD:1159\", \"status\": \"not_checked\",\n     \"note\": \"the cited AHD page belongs to the main dictionary (s.v. scarlet), which is not in the local library (only Watkins's IE appendix). Klein, Lokotsch, Skeat and Funk & Wagnalls all print the same Medieval Latin step.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. scarlet\", \"stance\": \"supports\",\n     \"note\": \"'fr. ML. scarlatum (whence also It. scarlatto); from Pers. sāqirlāt'.\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1794\", \"stance\": \"supports\",\n     \"note\": \"'hieraus mlat. scarlatum Scharlach als Stoff, it. scarlatto, afrz. escarlate, nfrz. écarlate, sp. pg. escarlata; engl. scarlet, mhd. scharlāt, ndl. scharlaken'.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol.4 s.v. scarlatina/scarlet (FSD_vol4.txt ll.3410, 3466)\", \"stance\": \"supports\",\n     \"note\": \"'< LL scarlatinus, scarlet, < scarlatum (< Pers saqa[rlāt])' and 'scarlet … < OF escarlate, < LL scarlatum'.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. scarlet (SKT.txt l.16601)\", \"stance\": \"supports\",\n     \"note\": \"'Scarlet (F.-Pers.) O.F. escarlate, [Span. escarlata, Ital. scarlatto] … the name of a stuff, which [was often] of a scarlet colour … The Turkish iskerlat [is] merely borrowed from Ital.'\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 11,\n  \"lang\": \"English\",\n  \"words\": \"scarlet\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Middle English scarlat, scarlet (mid-13th c.; a surname already in the late 12th c.), aphetic from \"\n    \"Old French escarlate (Modern French écarlate), from Medieval Latin scarlatum. As in French, the \"\n    \"word first names the cloth and only later the colour; the modern colour sense is secondary. The \"\n    \"step Medieval Latin > Old French > Middle English is uncontroversial (Klein, Skeat, Etymonline \"\n    \"agree); only the ultimate origin of scarlatum (node 10) is debated.\"\n  ),\n  \"derivation_fa\": (\n    \"انگلیسی scarlet از انگلیسی میانهٔ scarlat (میانهٔ سدهٔ سیزدهم) و آن کوتاه‌شدهٔ escarlate در فرانسهٔ کهن \"\n    \"(امروزی: écarlate) از scarlatum لاتین میانه است. مانند فرانسه، واژه نخست نام پارچه بوده و معنای رنگ \"\n    \"دیرتر پدید آمده است. این حلقهٔ لاتین میانه ← فرانسهٔ کهن ← انگلیسی میانه مورد اختلاف نیست (کلاین، اسکیت، \"\n    \"اتیمآنلاین هم‌داستان‌اند)؛ تنها خاستگاه نهایی scarlatum محل بحث است. ادعای نورایی درست است.\"\n  ),\n  \"sources\": [E_SCARLET],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n     \"note\": \"Nourai gives no reference for this box; the parent box carries AHD:1159.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. scarlet\", \"stance\": \"supports\",\n     \"note\": \"'scarlet, n. — ME. scarlat, scarlet, fr. OF. escarlate (F. écarlate); fr. ML. scarlatum'.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. scarlet\", \"stance\": \"supports\",\n     \"note\": \"'(F.-Pers.) O.F. escarlate … the name of a stuff, which [was] of a scarlet colour. Hence … scarlet cloth, whence M.E. [scarlat] (Chaucer).'\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 12,\n  \"lang\": \"English\",\n  \"words\": \"seal, sign, resign, assign\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"All four are Latin-via-French descendants of signum, and Watkins groups exactly these under \"\n    \"sekw-1: seal1 < ME seel < OF seel < Latin sigillum (diminutive of signum); sign < ME signe < OF \"\n    \"signe < Latin signum; assign < OF assigner < Latin assignāre 'to mark out to someone' (ad- + \"\n    \"signāre); resign < OF resigner < Latin resignāre 'to unseal, cancel' (Ernout-Meillet: 'resignō: \"\n    \"briser le cachet; ouvrir, violer le secret de'). The 14th-century English semantic shift of resign \"\n    \"from 'cancel (a sealed document)' to 'give up an office' happened in Anglo-French chancery usage. \"\n    \"The verdict depends on node 7: if signum is de Vaan's *sek- 'cut' word, these English words belong \"\n    \"to a different root, but their descent from signum itself is certain.\"\n  ),\n  \"derivation_fa\": (\n    \"هر چهار واژه از signum لاتین و از راه فرانسه به انگلیسی رسیده‌اند و واتکینز دقیقاً همین‌ها را ذیل sekw-1 \"\n    \"می‌آورد: seal از انگلیسی میانهٔ seel از فرانسهٔ کهن seel از sigillum لاتین (مصغّر signum)؛ sign از signe \"\n    \"فرانسهٔ کهن از signum؛ assign از assigner فرانسهٔ کهن از assignāre (ad- + signāre)؛ resign از resignāre \"\n    \"«مهر را شکستن، باطل کردن» که در دیوان‌سالاری انگلیسی-فرانسوی سدهٔ چهاردهم به معنی «کناره‌گیری از منصب» \"\n    \"تحول یافت. تنها تردید همان تردید جعبهٔ لاتین است (ریشهٔ signum)، وگرنه این حلقه قطعی است. \"\n    \"ادعای نورایی درست است.\"\n  ),\n  \"sources\": [E_SIGN, W_SIGNUM],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt, sekw-1 §5: '… Latin signum, identifying mark, sign …: SEAL1, SEGNO, SIGN; ASSIGN, CONSIGN, DESIGNATE, INSIGNIA, RESIGN'; the AHD index in the same file confirms 'ASSIGN sekw-1', 'RESIGN sekw-1', 'SEAL1 sekw-1', 'SIGN sekw-1'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. sign, sigillate\", \"stance\": \"supports\",\n     \"note\": \"'sign, n. — ME. signe, fr. OF. (= F.) signe, fr. L. [signum]'; 'sigillate … L. sigillātus, pp. of sigillāre … fr. sigillum.'\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. signum, derivatives\", \"stance\": \"supports\",\n     \"note\": \"'assignō: 1° assigner, t. du droit public … 2° sceller; assignator, -tio … resignō: briser le cachet; ouvrir, violer le secret de' — the Latin bases of assign and resign.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 13,\n  \"lang\": \"French\",\n  \"words\": \"assignat\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\n    \"The French word is real and correctly glossed: assignat, the paper money issued from 1790 by the \"\n    \"Revolutionary assembly on the security of confiscated Church lands, 'assigned' to that security; \"\n    \"it is a direct learned formation on Latin assignātum / assignātus, past participle of assignāre. \"\n    \"What is wrong is the arrow: Nourai draws French assignat out of the English box (seal, sign, \"\n    \"resign, assign). English never mediated here — French took the word straight from Latin, as \"\n    \"English took assign straight from Old French; the two are siblings, not parent and child. The box \"\n    \"should hang from the Latin signum node.\"\n  ),\n  \"derivation_fa\": (\n    \"خودِ واژهٔ فرانسوی درست است: assignat نام اسکناسی است که مجلس انقلاب فرانسه از سال ۱۷۹۰ بر پشتوانهٔ \"\n    \"زمین‌های مصادره‌شدهٔ کلیسا منتشر کرد و ساختی عالمانه بر پایهٔ assignātum لاتین (اسم مفعول assignāre) است. \"\n    \"آنچه نادرست است جهت پیکان است: نورایی assignat فرانسوی را از جعبهٔ انگلیسی (assign و …) بیرون می‌کشد، \"\n    \"حال آنکه فرانسه این واژه را یکسره از لاتین گرفته و انگلیسی نیز assign را از فرانسهٔ کهن؛ این دو هم‌نیا \"\n    \"(خواهر) هستند نه پدر و فرزند. پژوهش امروزی این حلقه را رد می‌کند و جعبه باید زیر جعبهٔ لاتین signum \"\n    \"بنشیند.\"\n  ),\n  \"sources\": [E_ASSIGNAT],\n  \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n     \"note\": \"no reference is given for this box in the book.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein/Etymonline s.v. assignat\", \"stance\": \"partial\",\n     \"note\": \"Etymonline: 'assignat — 1790, paper money of the French Revolution, based on the security of confiscated Church lands … from French assignat, from Latin assignatus, pp. of assignare/adsignare' — the word and its Latin source are confirmed, the English parentage is not.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. signum, derivative assignō\", \"stance\": \"supports\",\n     \"note\": \"'assignō: 1° assigner, t. du droit public … assignator, -tiō' — the Latin base of French assignat.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 14,\n  \"lang\": \"Russian\",\n  \"words\": \"assignatsia\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\n    \"The Russian word ассигна́ция (assignácija) 'banknote' is genuine — it is the state paper money \"\n    \"introduced by Catherine II in 1769 and current until 1849 — but it does not come from French \"\n    \"assignat. Chronology alone excludes it: the Russian assignatsiya predates the French assignat of \"\n    \"1790 by two decades. The accepted derivation (Wiktionary, with the Persian اسکناس entry) is \"\n    \"Russian ассигнация < Polish asygnacja < Latin assignātiō 'an allotment, assignment' — a \"\n    \"Latin abstract noun in -ātiō, whereas French assignat continues the participle assignātum. Nourai \"\n    \"has the right family and the right end-point but the wrong intermediary.\"\n  ),\n  \"derivation_fa\": (\n    \"واژهٔ روسی ассигнация «اسکناس» واقعی است — پول کاغذی دولتی که کاترین دوم در ۱۷۶۹ منتشر کرد و تا ۱۸۴۹ \"\n    \"رایج بود — اما از assignat فرانسوی نیامده است. گاه‌شماری خود این را رد می‌کند: صورت روسی دو دهه پیش از \"\n    \"assignat فرانسوی (۱۷۹۰) پدید آمده. ریشه‌شناسی پذیرفته‌شده (ویکی‌واژه، ذیل «اسکناس») چنین است: روسی \"\n    \"ассигнация از لهستانی asygnacja و آن از assignātiō لاتین (اسم مصدر با پسوند -ātiō)، حال آنکه assignat \"\n    \"فرانسوی دنبالهٔ اسم مفعول assignātum است. خانواده و مقصد درست است، ولی واسطه نادرست: پژوهش امروزی این \"\n    \"حلقه را رد می‌کند.\"\n  ),\n  \"sources\": [W_ESKENAS, E_ASSIGNAT],\n  \"ref_check\": [\n    {\"ref\": \"DMO:220\", \"status\": \"not_checked\",\n     \"note\": \"DMO = Sa'id Nafisi, Dar Maktab-e Ostad (Zohreh 1344/1965). refs_online.json: no copy on archive.org; only a login-walled PDF at ketabnak.com, not fetched. The page could not be read.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Wiktionary s.v. اسکناس (etymology of the Russian source word)\", \"stance\": \"contradicts\",\n     \"note\": \"'Borrowed from Russian ассигна́ция (assignácija), borrowed from Polish asygnacja, a learned borrowing from Latin assīgnātiō' — Polish, not French, is the intermediary.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. signum, derivatives of assignō\", \"stance\": \"supports\",\n     \"note\": \"'assignator, -tiō' — Latin assignātiō, the base of the Polish and Russian forms, is a derivative of the same signum family, so the ultimate root link stands.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 15,\n  \"lang\": \"Persian\",\n  \"words\": \"eskenâs «اسکناس»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"اسکناس eskenās 'banknote' is a 19th-century borrowing of Russian ассигна́ция assignácija, taken \"\n    \"over through the Caucasus/Tabriz trade at the time when Russian paper roubles circulated in \"\n    \"northern Iran; Persian dropped the unstressed medial syllable and reshaped the ending, \"\n    \"assignácija > *asignās > اسکناس eskenās, with the prothetic/anaptyctic vowel that Persian regularly \"\n    \"inserts to break the initial cluster (cf. estekān < стакан, esteqbāl-type shapes). Mo'in's \"\n    \"Farhang-e Farsi defines it «نوعی کاغذ بهادار که بهای وی بر روی آن نوشته شده و برای خرید و فروش بکار \"\n    \"می‌رود؛ پول کاغذی», i.e. Nourai's 'money bill'. The root link holds through Latin assignātiō to \"\n    \"signum; only the intermediate steps drawn in nodes 13-14 are wrong.\"\n  ),\n  \"derivation_fa\": (\n    \"«اسکناس» وام‌واژه‌ای از روسی ассигнация (assignácija) است که در سدهٔ نوزدهم از راه داد و ستد قفقاز و \"\n    \"تبریز، هنگامی که روبل کاغذی روسیه در شمال ایران رواج داشت، به فارسی راه یافت. در فارسی هجای میانی \"\n    \"بی‌تکیه افتاده و پایانهٔ واژه بازساخته شده است: assignácija > *asignās > «اسکناس»، با واکهٔ آغازینِ \"\n    \"افزوده که فارسی برای شکستن خوشهٔ آغازین به کار می‌برد (مانند «استکان» از стакан). معین آن را چنین \"\n    \"تعریف می‌کند: «نوعی کاغذ بهادار که بهای وی بر روی آن نوشته شده و برای خرید و فروش بکار می‌رود؛ پول \"\n    \"کاغذی». پیوند ریشه‌ای تا assignātiō لاتین و signum برقرار است؛ تنها حلقه‌های میانیِ نمودار (فرانسه و \"\n    \"مسیر انگلیسی) نادرست‌اند. ادعای نورایی در این جعبه درست است.\"\n  ),\n  \"sources\": [W_ESKENAS],\n  \"ref_check\": [\n    {\"ref\": \"DMO:220\", \"status\": \"not_checked\",\n     \"note\": \"Nafisi, Dar Maktab-e Ostad p.220 — no accessible copy (see node 14).\"},\n    {\"ref\": \"ARK:239\", \"status\": \"not_checked\",\n     \"note\": \"Arkān-e Sokhan p.239 — the book is not digitised anywhere reachable (refs_online.json: 'Not found').\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. اسکناس (MON_part1.txt l.12921)\", \"stance\": \"supports\",\n     \"note\": \"«اسکناس: … (اِ.) نوعی کاغذ بهادار که بهای وی بر روی آن نوشته شده و برای خرید و فروش بکار می‌رود؛ پول کاغذی. نشر اسکناس: چاپ کردن و انتشار دادن اسکناس در میان مردم.» The Latin-script origin tag that Mo'in prints before the definition is destroyed in this OCR ('عقجعمه'), so only the sense could be checked.\"},\n    {\"src\": \"KLN\", \"where\": \"Wiktionary s.v. اسکناس\", \"stance\": \"supports\",\n     \"note\": \"'Borrowed from Russian ассигна́ция (assignácija)' — the Russian > Persian arrow, which is Nourai's.\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 16,\n  \"lang\": \"Latin\",\n  \"words\": \"socius; sequi; secondus\",\n  \"verdict\": \"transcription_suspect\",\n  \"derivation\": (\n    \"sequī 'to follow' is the direct Latin continuation of *sekʷ- (Pokorny 896: 'Latin sequor, -ī \"\n    \"nachfolgen, begleiten, verfolgen'), a deponent with participle secūtus for older *sectos. socius \"\n    \"'companion, ally' is Watkins's '*sokʷ-yo-, o-grade, ally, companion (< follower)'; Ernout-Meillet \"\n    \"give a caveat worth repeating — 'Les Latins n'ont jamais songé à établir une parenté entre sequor \"\n    \"et socius. Socius n'est pas celui qui suit mais celui qui va avec' — and connect it with Vedic \"\n    \"sákhā / Avestan haxa, i.e. with node 1/6, though the Indo-Iranian aspirate remains a problem. — The \"\n    \"third form is wrong as printed: Latin has secundus 'following, next, second' (participial \"\n    \"*sekʷ-ondo-, Watkins §3), never *secondus, which is an Italian/French-looking spelling. The scan \"\n    \"of p.410 shows that the BOOK prints 'secondus: coming next', so the JSON is a faithful extraction \"\n    \"and the error is Nourai's own misprint (or a contamination from Italian secondo).\"\n  ),\n  \"derivation_fa\": (\n    \"sequī «پیروی کردن» دنبالهٔ مستقیم ریشهٔ *sekʷ- در لاتین است (پوکورنی ص۸۹۶). socius «همراه، هم‌پیمان» \"\n    \"نزد واتکینز صورت o-درجهٔ *sokʷ-yo- «پیرو» است؛ ولی ارنو-مِیه هشدار می‌دهند که «رومیان هرگز میان sequor \"\n    \"و socius خویشاوندی نمی‌دیدند؛ socius «آن‌که از پی می‌رود» نیست بلکه «آن‌که همراه می‌رود» است» و آن را با \"\n    \"sákhā ودایی و haxa اوستایی می‌سنجند. صورت سوم چنان‌که چاپ شده نادرست است: لاتین secundus «پسین، دوم» \"\n    \"دارد (از *sekʷ-ondo-) نه *secondus که املایی ایتالیایی‌مآب است. تصویر صفحهٔ ۴۱۰ نشان می‌دهد که خودِ \"\n    \"کتاب «secondus» چاپ کرده است؛ پس این خطای چاپی کتاب است، نه خطای خوانش اسکن.\"\n  ),\n  \"error_in\": \"book\",\n  \"book_prints\": \"secondus\",\n  \"correct_form\": \"secundus\",\n  \"sources\": [W_SEKW, E_SIGN],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt, sekw-1: '1. Latin sequi, to follow: SECT, SEGUE … 3. Suffixed (participial) form *sekʷ-ondo- in Latin secundus, following, coming next, second: SECOND2 … 6. Suffixed o-grade form *sokʷ-yo- in Latin socius, ally, companion (< \\\"follower\\\"): SOCIABLE, SOCIAL, SOCIETY …'. Note that Watkins spells the word secundus, not secondus.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 896-897\", \"stance\": \"supports\",\n     \"note\": \"'Latin sequor, -ī nachfolgen, begleiten, verfolgen … secundus (participle Praes.) the following, second … socius teilnehmend, Gesellschafter, Teilnehmer, Bundesgenosse' — all three words under this root, with the correct spelling secundus.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. socius (LAT.txt l.58862 ff.)\", \"stance\": \"partial\",\n     \"note\": \"'Les Latins n'ont jamais songé à établir une parenté entre sequor et socius. Socius n'est pas celui qui suit mais celui qui va avec … En indo-iranien … véd. sákhā …, av. haxa compagnon. Le rapprochement s'impose' — the etymology is accepted but with reservations about the semantics and the aspirate.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II 476 f.\", \"stance\": \"supports\",\n     \"note\": \"'Lat. sequor, -ī nachfolgen, begleiten, verfolgen, Ptc. secutus …' (WLD_Bd2 l.30901), the reference Pokorny himself gives (WP. II 476 f.).\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. sequō (1) 'follow, accompany', WP II 476\", \"stance\": \"supports\",\n     \"note\": \"'sequō (1) follow, accompany. WP II, 476. Skt. sacāmi …; Av. haca-, v. follow, achieve; Tokh. A säk-; Gk. hépomai …'\"}\n  ]\n})\n\nnodes.append({\n  \"id\": 17,\n  \"lang\": \"English\",\n  \"words\": \"society, association; pursue, sequence, execute; second\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Each of these is a Romance-mediated descendant of the Latin words in node 16, and Watkins lists \"\n    \"them all under sekw-1: society and associate from socius (societās, associāre); pursue from Old \"\n    \"French poursuir < Vulgar Latin *prōsequere for prōsequī; sequence from Late Latin sequentia; \"\n    \"execute from Latin exsequī 'to follow out, carry out' through Old French executer; second from Old \"\n    \"French second < Latin secundus. The AHD word-index in the same file records 'SOCIETY sekw-1', \"\n    \"'ASSOCIATE sekw-1', 'PURSUE sekw-1', 'SEQUENCE sekw-1', 'EXECUTE sekw-1', 'SECOND2 sekw-1'.\"\n  ),\n  \"derivation_fa\": (\n    \"همهٔ این واژه‌ها از راه زبان‌های رومیایی از واژه‌های لاتین جعبهٔ پیشین آمده‌اند و واتکینز همه را ذیل \"\n    \"sekw-1 می‌آورد: society و association از socius (societās، associāre)؛ pursue از poursuir فرانسهٔ کهن \"\n    \"از *prōsequere عامیانه؛ sequence از sequentia لاتین متأخر؛ execute از exsequī «به پایان بردن» از راه \"\n    \"executer فرانسهٔ کهن؛ و second از second فرانسهٔ کهن از secundus. نمایهٔ واژگان AHD نیز همین را تأیید \"\n    \"می‌کند. ادعای نورایی درست است.\"\n  ),\n  \"sources\": [W_SEKW],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt, sekw-1 and its index: 'SECT, SEGUE, SEGUIDILLA, SEQUACIOUS, SEQUEL, SEQUENCE, SUE, SUITOR; CONSEQUENT, ENSUE, EXECUTE, OBSEQUIOUS, PERSECUTE, PROSECUTE, (PURSUE), SUBSEQUENT … SECOND2 … SOCIABLE, SOCIAL, SOCIETY, SOCIO-; ASSOCIATE, CONSOCIATE, DISSOCIATE'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.vv. society, pursue, execute, second\", \"stance\": \"supports\",\n     \"note\": \"Klein's entries derive these from Latin societās/socius, *prōsequere, exsequī and secundus respectively, i.e. from the same Latin box.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. socius\", \"stance\": \"supports\",\n     \"note\": \"'societās: compagnie, société, association, alliance … sociālis … adsociō (lat. impér.)' — the Latin bases of society and associate.\"}\n  ]\n})\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Sekw\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *sekʷ- 'to follow' (Pokorny 896-897 'sekʷ-1, to follow'; Watkins/AHD sekw-1)\",\n  \"note\": (\n    \"The root box is right in every particular: Pokorny's IEW pp.896-897 has 'Root/lemma: sekʷ-1, \"\n    \"Meaning: to follow' (with the note that as a hunters' term it was originally one with sekʷ-2 \"\n    \"'to see'), Walde-Pokorny II 476 f. is the same entry, and Watkins prints 'sekw-1, To follow. \"\n    \"[Pok. 1. sekʷ- 896.]'. Nourai's transliteration 'Sekw' and the label 'Indo-European' follow the \"\n    \"AHD appendix's conventions. Two cross-cutting points about the chart: (a) the Indo-Iranian \"\n    \"'friend' words (Av. haxay-, OP haxā-, Skt. sákhā) that carry nodes 1, 2 and 6 are attached to \"\n    \"this root only 'wegen des arischen kh sehr zweifelhaft' (Pokorny 896, Walde-Pokorny II 476) — \"\n    \"Nourai reproduces the attachment without the reservation; (b) Latin signum (node 7), on which the \"\n    \"whole scarlet/seal/eskenās branch hangs, belongs here only on Watkins's analysis (*sekʷ-no-), \"\n    \"while de Vaan 2008 derives it from *sek- 'to cut'. The page also contains one empty, unlabelled \"\n    \"box to the right of the Old Persian row, which the extraction correctly left out; and the printed \"\n    \"Latin form 'secondus' in the last box is a misprint for secundus.\"\n  ),\n  \"note_fa\": (\n    \"جعبهٔ ریشه در همهٔ جزئیات درست است: پوکورنی در «فرهنگ ریشه‌شناختی هندواروپایی» صص۸۹۶-۸۹۷ سرواژهٔ \"\n    \"«sekʷ-1، معنی: پیروی کردن» را دارد، والده-پوکورنی ج۲ ص۴۷۶ به بعد همان مدخل است، و واتکینز در پیوست \"\n    \"AHD «sekw-1, To follow» می‌نویسد. آوانگاری «Sekw» و برچسب «هندواروپایی» از شیوهٔ همان پیوست گرفته شده \"\n    \"است. دو نکتهٔ فراگیر دربارهٔ این نمودار: (الف) واژه‌های هندوایرانی به معنی «دوست» (haxay- اوستایی، haxā- \"\n    \"پارسی باستان، sákhā سنسکریت) که جعبه‌های ۱، ۲ و ۶ بر آن‌ها استوارند، تنها «به سبب خِ هندوایرانی بسیار \"\n    \"مشکوک» به این ریشه بسته شده‌اند (پوکورنی ص۸۹۶؛ والده-پوکورنی ج۲ ص۴۷۶) و نورایی این تردید را نیاورده \"\n    \"است؛ (ب) signum لاتین (جعبهٔ ۷) که کل شاخهٔ سقرلات/مهر/اسکناس بر آن آویخته است، تنها بر پایهٔ تحلیل \"\n    \"واتکینز (*sekʷ-no-) به این ریشه می‌پیوندد، حال آنکه دِ ڤان (۲۰۰۸) آن را از *sek- «بریدن» می‌گیرد. در \"\n    \"صفحهٔ چاپی یک جعبهٔ خالی و بی‌برچسب هم در کنار ردیف پارسی باستان هست که در استخراج به‌درستی نادیده گرفته \"\n    \"شده؛ و صورت «secondus» در جعبهٔ آخر غلط چاپی به‌جای secundus است.\"\n  ),\n  \"sources\": [W_SEKW, W_SIGNUM],\n  \"ref_check\": [\n    {\"ref\": \"POK:896\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt: 'Root / lemma: sekʷ-1 | Meaning: to follow | Grammatical information: mostly medial | Note: as Terminus [of] the jargon spoken by hunters originally eins with sekʷ-2 … References: WP. II 476 f., WH. II 506, 518, 519 f., Trautmann 254 f. | Page(s): 896-897'. Root, language and gloss all as Nourai gives them.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II 476 f. (WLD_Bd2_1927_dli_106624_djvu.txt ll.30887-30927)\", \"stance\": \"supports\",\n     \"note\": \"the same root entry, with 'Lat. sequor, -ī nachfolgen, begleiten, verfolgen', 'Air. sechur (= lat. sequor)', and the doubt about ai. sákhā / av. haxay-.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sekw-1\", \"stance\": \"supports\",\n     \"note\": \"'sekw-1, To follow. … [Pok. 1. sekʷ- 896.]' — Watkins's headword is exactly Nourai's 'Sekw'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. sequō (1) (IEC.txt l.15233)\", \"stance\": \"supports\",\n     \"note\": \"'sequō (1) follow, accompany. WP II, 476. Skt. sacāmi, v. accompany, belong to; Av. haca-, v. follow, achieve; Tokh. A säk-; Myc. (h)eq-, Gk. hépomai …'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck, Dictionary of Selected Synonyms\", \"stance\": \"silent\",\n     \"note\": \"Buck's chapter on 'follow' was searched (grep 'sequor' in SYN.txt); the hits belong to the sekʷ- 'see'/'say' discussion (§9 on Goth. saihwan), not to a separate treatment of 'follow' that adds anything to Pokorny.\"}\n  ],\n  \"nodes\": nodes\n}\n\ndoc = {\n  \"pdf_page\": 440,\n  \"book_page\": 410,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [entry]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-440.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\", len(nodes))\n"
}
```


### [2026-09-14T02:13:02.884Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-440.py (file state is current in your context — no need to Read it back)
```


## [2026-09-14T02:13:05.645Z] TOOL CALL #86: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-440.py && python3 -m json.tool data/verification/page-440.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 440"
}
```


### [2026-09-14T02:13:07.075Z] TOOL RESULT

```
ok 17
JSON OK
nodes verified: 17/17
node verdicts: {'plausible': 4, 'confirmed': 10, 'disputed': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 10, 'partial': 2, 'not_found': 1, 'not_checked': 11}
books consulted: {'supports': 37, 'partial': 8, 'silent': 4, 'contradicts': 1} | by book: {'KLN': 10, 'LAT': 7, 'PHD': 4, 'MON': 4, 'BRT': 3, 'HRN': 3, 'POK': 3, 'LKT': 3, 'SKT': 3, 'WLD': 2, 'BQT': 2, 'HUB': 1, 'AHD': 1, 'NYB': 1, 'FVQ': 1, 'FSD': 1, 'IEC': 1}
```


## [2026-09-14T02:13:15.008Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json,io\np='data/verification/page-440.json'\nd=json.load(open(p,encoding='utf-8'))\nnodes={n['id']:n for n in d['entries'][0]['nodes']}\nnodes[13]['consulted'][0]['src']='Etymonline'\nnodes[14]['consulted'][0]['src']='Wiktionary'\nnodes[15]['consulted'][1]['src']='Wiktionary'\njson.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)\nopen(p,'a',encoding='utf-8').write('\\n')\nEOF\npython3 tools/verify_check.py 440"
}
```


### [2026-09-14T02:13:16.477Z] TOOL RESULT

```
nodes verified: 17/17
node verdicts: {'plausible': 4, 'confirmed': 10, 'disputed': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 10, 'partial': 2, 'not_found': 1, 'not_checked': 11}
books consulted: {'supports': 37, 'partial': 8, 'silent': 4, 'contradicts': 1} | by book: {'LAT': 7, 'KLN': 7, 'PHD': 4, 'MON': 4, 'BRT': 3, 'HRN': 3, 'POK': 3, 'LKT': 3, 'SKT': 3, 'WLD': 2, 'BQT': 2, 'Wiktionary': 2, 'HUB': 1, 'AHD': 1, 'NYB': 1, 'FVQ': 1, 'FSD': 1, 'Etymonline': 1, 'IEC': 1}
```


## [2026-09-14T02:13:34.596Z] AGENT

Done. `data/verification/page-440.json` written; `verify_check.py 440` reports 0 PROBLEM lines (17/17 nodes).

**Page 440 (book p. 410) — root Sekw "to follow", 1 entry, 17 nodes**

Verdicts: root confirmed; nodes — confirmed 10, plausible 4, disputed 2, transcription_suspect 1.
Ref checks: supports 10, partial 2, not_found 1, not_checked 11 (ARK and DMO are undigitised; AHD:1159 is the New College main body, not the local Watkins appendix; BQT vols 1–2 exist here only as Latin-free Persian OCR with no page scan).

- **disputed — #13 French `assignat`**: real word (1790 Revolutionary paper money) but formed directly on Latin *assignātum*; it does not descend from the English box (seal/sign/assign) as drawn — siblings, not parent/child.
- **disputed — #14 Russian `assignatsia`**: Russian ассигнация (Catherine II, 1769) predates French *assignat* (1790); Wiktionary derives it from Polish *asygnacja* < Latin *assignātiō*. Wrong intermediary; the Persian end-point (#15 اسکناس) is still confirmed.
- **transcription_suspect — #16 Latin `secondus`**: Latin is *secundus*. Page scan (copied to `data/verification/sources/refs/ocr/BOOK/440.png`) shows the **book** prints "secondus"; extraction faithful → `error_in: "book"`.
- plausible flags worth noting: #1 mislabels Bartholomae's Old-Iranian reconstruction \*hašākarta- and the Armenian loan *ašakert* as "Avestan", and Pokorny 896 / Walde-Pokorny II 476 call the haxay-/sákhā link to \*sekʷ- "sehr zweifelhaft" — Nourai omits that reservation (#1, #6). #7 Latin *signum* is on \*sekʷ- only per Watkins; de Vaan prefers \*sek- "cut". #10 Medieval Latin *scarlatum* < Persian is the majority view (Klein, Lokotsch, Skeat, F&W) but Etymonline offers a Germanic alternative (*scarlachen*).
- Best finds: ZAW:38 and ZAW:242 check out verbatim (Bartholomae's \*hašākarta- → šāgird, cross-referenced to haxay-/Haxāmaniš-); KNT:212 checks out exactly (read from archive.org — local `KNT.txt` is truncated before the h-section); BQT:2316 = vol. 4 pdf p. 399 carries Mo'in's هخامنش footnote word-for-word.

**No extraction errors found** — the JSON matches the printed page everywhere, including the empty unlabelled box beside the Old Persian row, which was correctly not turned into a node. One citation of Nourai's is simply wrong: **HRN:12** (p. 12 has āmurzīdan/āmōxtan); his *az* material is Horn no. 75, p. 18.
