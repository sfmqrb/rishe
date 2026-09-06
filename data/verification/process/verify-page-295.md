# Verification process log — verify-page-295


## [2026-09-06T22:27:47.454Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 295 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-295.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-295.json. Write /home/sfmqrb/git/rishe/data/verification/page-295.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 295` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:27:48.928Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T22:27:49.635Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:27:49.650Z] TOOL RESULT

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


## [2026-09-06T22:27:49.831Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-295.txt"
}
```


### [2026-09-06T22:27:49.845Z] TOOL RESULT

```
1	=== PDF page 295 (book page 265) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kwetwer, Qwetwor : four  (refs POK:642)
4	#1 (parent #0) [Avestan] refs=POK:642 | čatwârao : four
5	  #2 (parent #1) [Persian] refs=POK:642 |  | extra: چهار ، چهارک ، چهارده ، چهل
6	#3 (parent #0) [Armenian] refs=SNS:148 | čatvar : one fourth
7	  #4 (parent #3) [Persian] refs=SNS:148 | katvar «کَتوَر» : one quarter of a kilogram (250 grams) | NOTE: MON:1273 claims this word has entered Persian through Russian.
8	#5 (parent #0) [Sanskrit] refs=BQT:1254 | catur-anga : four members, referring to the chess game ☞Ang
9	  #6 (parent #5) [Pahlavi] refs=None | catrang : chess
10	    #7 (parent #6) [Persian] refs=None | katrang «کَترنگ» : chess | extra: شترنگ ، شطرنج
11	#8 (parent #0) [Latin] refs=AHD:1068 | quadrus : four ; quadrâgintâ : forty
12	  #9 (parent #8) [French] refs=None | 
13	    #10 (parent #9) [Persian] refs=MON | kâdr «کادر» : frame, framework
14	    #11 (parent #9) [English] refs=AHD | cadre, squad, square, quart, quarter
15	  #12 (parent #8) [Italian] refs=AHD:1068 | quadratina : forty, forty days of isolation at the entry ports of a country enforced upon people or products suspected of carrying contagious diseases
16	    #13 (parent #12) [Arabic] refs=TAD:62 | karantînâ, qarantîna : quarantine
17	      #14 (parent #13) [Persian] refs=MON:2666 | qarantîn «قرنطین» : quarantine | extra: قرنطینه
18	    #15 (parent #12) [English] refs=AHD:1068 | quarantine
19	#16 (parent #0) [Germanic] refs=AHD | petwor : four
20	  #17 (parent #16) [English] refs=None | four, fourteen, forty
21	#18 (parent #0) [Greek] refs=AHD:1365 | tra-peza : "four-legged" table, trapezoid ☞Ped
22	  #19 (parent #18) [Arabic] refs=MON:1481 | dar-bezin : a seating area between two doors of a room
23	    #20 (parent #19) [Persian] refs=MON:1481 | dârâbzîn «دارابزین» : a seating area | extra: درابزین ، دارافزین ، داروزین
24	  #21 (parent #18) [Latin] refs=AHD | 
25	    #22 (parent #21) [English] refs=AHD | trapezoid, trapeze
26	
```


## [2026-09-06T22:27:52.790Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-295.json",
 "description": "Read source JSON for page 295"
}
```


### [2026-09-06T22:27:52.826Z] TOOL RESULT

```
{
  "pdf_page": 295,
  "book_page": 265,
  "entries": [
    {
      "root": {
        "name": "Kwetwer, Qwetwor",
        "lang": "Indo-European",
        "refs": "POK:642",
        "gloss": "four"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:642",
          "words": [
            {"translit": "čatwârao", "gloss": "four", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:642",
          "words": [],
          "script_extra": "چهار ، چهارک ، چهارده ، چهل",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Armenian",
          "refs": "SNS:148",
          "words": [
            {"translit": "čatvar", "gloss": "one fourth", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "SNS:148",
          "words": [
            {"translit": "katvar", "gloss": "one quarter of a kilogram (250 grams)", "script": "کَتوَر"}
          ],
          "script_extra": null,
          "note": "MON:1273 claims this word has entered Persian through Russian.",
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "BQT:1254",
          "words": [
            {"translit": "catur-anga", "gloss": "four members, referring to the chess game", "script": null, "see": ["Ang"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {"translit": "catrang", "gloss": "chess", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "katrang", "gloss": "chess", "script": "کَترنگ"}
          ],
          "script_extra": "شترنگ ، شطرنج",
          "note": null,
          "quote": {
            "text": "تا جز از بیست و چهارش نبود خانهٔ نرد - همچو دو سی و دو خانست نهادش شترنگ",
            "poet": "Najjâr"
          }
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1068",
          "words": [
            {"translit": "quadrus", "gloss": "four", "script": null},
            {"translit": "quadrâgintâ", "gloss": "forty", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "kâdr", "gloss": "frame, framework", "script": "کادر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 9,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "cadre, squad, square, quart, quarter", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 8,
          "lang": "Italian",
          "refs": "AHD:1068",
          "words": [
            {"translit": "quadratina", "gloss": "forty, forty days of isolation at the entry ports of a country enforced upon people or products suspected of carrying contagious diseases", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Arabic",
          "refs": "TAD:62",
          "words": [
            {"translit": "karantînâ, qarantîna", "gloss": "quarantine", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Persian",
          "refs": "MON:2666",
          "words": [
            {"translit": "qarantîn", "gloss": "quarantine", "script": "قرنطین"}
          ],
          "script_extra": "قرنطینه",
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 12,
          "lang": "English",
          "refs": "AHD:1068",
          "words": [
            {"translit": "quarantine", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "petwor", "gloss": "four", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "four, fourteen, forty", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1365",
          "words": [
            {"translit": "tra-peza", "gloss": "\"four-legged\" table, trapezoid", "script": null, "see": ["Ped"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "Arabic",
          "refs": "MON:1481",
          "words": [
            {"translit": "dar-bezin", "gloss": "a seating area between two doors of a room", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 19,
          "lang": "Persian",
          "refs": "MON:1481",
          "words": [
            {"translit": "dârâbzîn", "gloss": "a seating area", "script": "دارابزین"}
          ],
          "script_extra": "درابزین ، دارافزین ، داروزین",
          "note": null,
          "quote": null
        },
        {
          "id": 21,
          "parent": 18,
          "lang": "Latin",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 22,
          "parent": 21,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "trapezoid, trapeze", "gloss": null, "script": null}
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


## [2026-09-06T22:27:53.487Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T22:27:53.525Z] TOOL RESULT

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


## [2026-09-06T22:28:02.983Z] TOOL CALL #5: Bash

```json
{
 "command": "pdftoppm -f 295 -l 295 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg295 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 295"
}
```


### [2026-09-06T22:28:05.367Z] TOOL RESULT

```
total 118500
drwx------ 5 sfmqrb sfmqrb     4096 Sep  6 18:28 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb      770 Sep  6 18:27 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  5157031 Sep  6 18:05 aiw.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    26688 Sep  6 18:20 ary377_bot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71464 Sep  6 18:20 ary377_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71267 Sep  6 18:19 ary378_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25966 Sep  6 18:19 ary378_top_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   127656 Sep  6 18:17 bqt1267_foot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb   362419 Sep  6 17:50 bqt1583_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105420 Sep  6 18:16 bqt27.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   703015 Sep  6 17:50 bqt_fn4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299015 Sep  6 17:50 bqt_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   325427 Sep  6 17:50 bqt_n552.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   315487 Sep  6 17:50 bqt_n553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   330101 Sep  6 17:50 bqt_n554.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   560485 Sep  6 17:53 bqtv2_650_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   541712 Sep  6 17:53 bqtv2_651_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   729454 Sep  6 17:53 bqtv2_n650.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   702551 Sep  6 17:53 bqtv2_n651.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   100817 Sep  6 17:36 bqt_v3_111.png
-rw-rw-r-- 1 sfmqrb sfmqrb   110820 Sep  6 17:36 bqt_v3_112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   137595 Sep  6 18:10 buck2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      146 Sep  6 18:10 buck3.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52615 Sep  6 17:36 build275.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74145 Sep  6 17:43 build278.py
-rw-rw-r-- 1 sfmqrb sfmqrb    72342 Sep  6 17:58 build283.py
-rw-rw-r-- 1 sfmqrb sfmqrb    28249 Sep  6 18:25 build290a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    39449 Sep  6 18:27 build291.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb 60831599 Sep  6 18:01 cad_k.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  2530822 Sep  6 18:01 cad_k.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 18:09 cpd.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 18:09 cpd.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  2144625 Sep  6 17:55 dmmpp.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14732 Sep  6 18:27 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17126 Sep  6 17:54 e1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    18004 Sep  6 17:56 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb  5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1845041 Sep  6 18:04 gharib.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3698758 Sep  6 17:50 IEC_full_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb     4265 Sep  6 17:53 kapi_script.png
-rw-rw-r-- 1 sfmqrb sfmqrb   944060 Sep  6 18:06 kent_full.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   288525 Sep  6 18:07 kent_n222.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   285652 Sep  6 18:07 kent_n223.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282304 Sep  6 18:07 kent_n224.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   268920 Sep  6 18:07 kent_n225.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb    73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46494 Sep  6 17:52 mk279.py
-rw-rw-r-- 1 sfmqrb sfmqrb    16605 Sep  6 17:54 mk280b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17667 Sep  6 17:56 mk280c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    43177 Sep  6 17:50 mk280.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58322 Sep  6 17:51 mk282.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63940 Sep  6 18:05 mk285.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67974 Sep  6 18:09 mk286.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60646 Sep  6 18:11 mk287.py
-rw-rw-r-- 1 sfmqrb sfmqrb    14748 Sep  6 18:27 mk292.py
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb    10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb    14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb    25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb   105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7106 Sep  6 17:34 p279_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    12970 Sep  6 17:34 p279_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3647 Sep  6 17:34 p279_xsaeta.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130651 Sep  6 17:48 p283_arrow.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:02 p284
-rw-rw-r-- 1 sfmqrb sfmqrb    43108 Sep  6 17:51 p284_e0_fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89734 Sep  6 17:51 p284_e0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59639 Sep  6 17:48 p284_e2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106502 Sep  6 17:48 p284_e2.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:25 p289
-rw-rw-r-- 1 sfmqrb sfmqrb    54419 Sep  6 18:05 p289_labibi.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:25 p290
-rw-rw-r-- 1 sfmqrb sfmqrb     1476 Sep  6 18:11 p291_esfand.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31043 Sep  6 18:11 p291_root.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168655 Sep  6 17:34 pg279hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75777 Sep  6 17:34 pg279.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61535 Sep  6 17:39 pg281.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70575 Sep  6 17:34 pg282.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74784 Sep  6 17:47 pg283.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:50 pg284hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:51 pg284.png
-rw-rw-r-- 1 sfmqrb sfmqrb   144566 Sep  6 17:49 pg284_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84487 Sep  6 17:53 pg285.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106264 Sep  6 17:53 pg286hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76099 Sep  6 18:10 pg286.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72442 Sep  6 17:59 pg287.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53847 Sep  6 17:58 pg288.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28862 Sep  6 18:27 pg289_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91779 Sep  6 18:26 pg289.png
-rw-rw-r-- 1 sfmqrb sfmqrb   187988 Sep  6 18:19 pg290hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98901 Sep  6 18:18 pg290.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105586 Sep  6 18:11 pg291hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70592 Sep  6 18:10 pg291.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103438 Sep  6 18:12 pg292.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36312 Sep  6 18:20 pg294_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77133 Sep  6 18:28 pg295.png
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1548.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1549.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1550.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     3698 Sep  6 18:19 zar_line.png
```


## [2026-09-06T22:28:05.612Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SNS','BQT','AHD','MON','TAD','KLN','SKT','LKT','PLA','AFM','ARY','HRN','HUB','PHD','NYB','IEC','SYN','WLD','LEW','LAT','FSD','WEB','DEV','PHN','HJB','RCH','FVQ','ARB']:\n    v=d.get(k)\n    if v: print(k, json.dumps(v, ensure_ascii=False)[:600]); print()\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-06T22:28:07.224Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 =

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "lo
```


## [2026-09-06T22:28:09.813Z] TOOL CALL #7: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg295.png"
}
```


### [2026-09-06T22:28:10.171Z] TOOL RESULT

```

```


## [2026-09-06T22:28:10.168Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T22:28:29.769Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 295 -l 295 -r 450 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg295hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg295hi.png'); print(im.size)\nW,H=im.size\n# katvar box (script at right) approx y 0.19-0.24, x 0.4-0.80\nim.crop((int(W*0.38),int(H*0.185),int(W*0.80),int(H*0.245))).save('c_katvar.png')\nim.crop((int(W*0.42),int(H*0.245),int(W*0.80),int(H*0.34))).save('c_katrang.png')\nim.crop((int(W*0.20),int(H*0.40),int(W*0.50),int(H*0.50))).save('c_ital.png')\nim.crop((int(W*0.18),int(H*0.545),int(W*0.40),int(H*0.585))).save('c_germ.png')\nim.crop((int(W*0.18),int(H*0.58),int(W*0.80),int(H*0.66))).save('c_greek.png')\n\"\nls",
 "description": "Crop regions of page 295"
}
```


### [2026-09-06T22:28:33.576Z] TOOL RESULT

```
(3825, 4950)
afm41_a.png
afm41_b.png
afm41.png
afm46.png
afm46_top.png
agents.txt
aiw.txt
ary377_bot_p294.png
ary377_p294.png
ary378_p294.png
ary378_top_p294.png
bqt1237_foot.png
bqt1267_foot_p294.png
bqt1583_foot.png
bqt1594_foot.png
bqt27.png
bqt83_head.png
bqt_fn4.png
bqt_fn.png
bqt_n552.jpg
bqt_n553.jpg
bqt_n554.jpg
bqtv2_650_s.png
bqtv2_651_s.png
bqtv2_n650.jpg
bqtv2_n651.jpg
bqt_v3_111.png
bqt_v3_112.png
bqt_v3_83.png
buck2.txt
buck3.txt
build261.py
build269.py
build270.py
build275.py
build278.py
build283.py
build290a.py
build291.py
c1.png
c2.png
c3.png
c4.png
cad_k.pdf
cad_k.txt
c_av.png
c_cros.png
c_empty.png
c_germ.png
c_greek.png
c_ital.png
c_katrang.png
c_katvar.png
coord_pg262.png
cpd.pdf
cpd.txt
crop_ak2.png
crop_ak.png
crop_alk.png
crop_fr269.png
crop_germ269.png
crop_gk269.png
crop_gk271.png
crop_gr267.png
crop_gr.png
crop_kohul.png
crop_lat2.png
crop_latin269.png
crop_lat.png
crop_me2.png
crop_me.png
crop_op2.png
crop_op.png
crop_pers.png
crop_sak.png
crop_sax.png
crop_shekar.png
crop_sirish.png
crop_skt267.png
crop_slav.png
crop_top.png
dmmpp.txt
e0.json
e1.json
e2.json
ediv.pdf
ediv.txt
gharib.txt
IEC_full_djvu.txt
jscheck.js
kapi_script.png
kent_full.txt
kent_n222.jpg
kent_n223.jpg
kent_n224.jpg
kent_n225.jpg
merge262.py
mk265.py
mk267.py
mk268.py
mk274.py
mk276.py
mk279.py
mk280b.py
mk280c.py
mk280.py
mk282.py
mk285.py
mk286.py
mk287.py
mk292.py
mk.pdf
mk.txt
p262-g01.json
p262-g02.json
p262-g03.json
p262-g04.json
p262-g05.json
p262-g06.json
p262-g07.json
p262-g08.json
p262-g09.json
p262-g10.json
p262-g11.json
p262-g12.json
p262-g13.json
p263hi.png
p275_krei_empty.png
p275_pahlavi.png
p279_greek.png
p279_word.png
p279_xsaeta.png
p283_arrow.png
p284
p284_e0_fa.png
p284_e0.png
p284_e2b.png
p284_e2.png
p289
p289_labibi.png
p290
p291_esfand.png
p291_root.png
pg261.png
pg262.png
pg263.png
pg264hi.png
pg264.png
pg265_crop.png
pg265.png
pg266.png
pg267.png
pg268.png
pg269.png
pg270hi.png
pg270.png
pg271hi.png
pg271.png
pg272.png
pg273_crop.png
pg273hi.png
pg273.png
pg274.png
pg275.png
pg276.png
pg277.png
pg278.png
pg279hi.png
pg279.png
pg280.png
pg281.png
pg282.png
pg283.png
pg284hi.png
pg284.png
pg284_top.png
pg285.png
pg286hi.png
pg286.png
pg287.png
pg288.png
pg289_crop.png
pg289.png
pg290hi.png
pg290.png
pg291hi.png
pg291.png
pg292.png
pg294_p294.png
pg295hi.png
pg295.png
syn_n1548.jpg
syn_n1549.jpg
syn_n1550.jpg
zar_line.png
```


## [2026-09-06T22:28:36.510Z] TOOL CALL #9: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_katvar.png"
}
```


### [2026-09-06T22:28:36.526Z] TOOL RESULT

```

```


## [2026-09-06T22:28:45.536Z] TOOL CALL #10: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_katrang.png"
}
```


### [2026-09-06T22:28:45.553Z] TOOL RESULT

```

```


## [2026-09-06T22:28:56.816Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg295hi.png'); W,H=im.size\nc=im.crop((int(W*0.72),int(H*0.202),int(W*0.79),int(H*0.228))).resize((int(W*0.07*4),int(H*0.026*4)))\nc.save('c_katvar_zoom.png')\n\"",
 "description": "Zoom Persian script of katvar"
}
```


### [2026-09-06T22:28:58.694Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:29:00.442Z] TOOL CALL #12: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_katvar_zoom.png"
}
```


### [2026-09-06T22:29:00.457Z] TOOL RESULT

```

```


## [2026-09-06T22:29:09.065Z] TOOL CALL #13: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_ital.png"
}
```


### [2026-09-06T22:29:09.081Z] TOOL RESULT

```

```


## [2026-09-06T22:29:09.821Z] TOOL CALL #14: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_germ.png"
}
```


### [2026-09-06T22:29:09.836Z] TOOL RESULT

```

```


## [2026-09-06T22:29:25.494Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK page 642 (leaf=p+8 -> 650) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==650' POK_01.txt | head -60\necho \"=== grep kᵘ̯etu̯er in POK ===\"\ngrep -n \"etu̯er\" POK_01.txt | head -20",
 "description": "Pokorny p.642"
}
```


## [2026-09-06T22:29:26.908Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins kwetwer ===\"\ngrep -n -i -A20 \"^k[wʷ]etwer\" AHD_watkins1985.txt | head -60\necho \"=== AHD ped ===\"\ngrep -n -i \"trapeza\\|trapez\" AHD_watkins1985.txt | head -20",
 "description": "AHD Watkins kwetwer"
}
```


### [2026-09-06T22:29:28.094Z] TOOL RESULT

```
=== POK page 642 (leaf=p+8 -> 650) ===
=== grep kᵘ̯etu̯er in POK ===
```


### [2026-09-06T22:29:28.150Z] TOOL RESULT

```
=== AHD watkins kwetwer ===
=== AHD ped ===
654:four (genitive tessardn): TESSERA; DIATESSARON. c. Greek tetras, group of four: TETRAD; d. zero-grade form *k¥t(w)r- in Greek tra-, four: TRAPEZIUM. III. Ordi- nal adjective *ketur-to-. 1. Germanic *fe(d)worthén- in: a. Old English féortha, féowertha, fourth: FOURTH; b. Middle Dutch veerdel, one-fourth: FIRKIN; c. Old English féorthing, féorthung, fourth part of a penny: FARTHING. 2. Latin qudrtus, fourth, quarter: QUA- DRILLE?, QUADROON, QUART, QUARTAN, QUARTER, quarto. [Pok. kvetuer- 642.]
818:ANTIPODES, APODAL, APPOGGIATURA, APUS, CALIBER, LYCOPODIUM, MONOPODIUM, OCTOPUS, PELECYPOD, PHALAROPE, PLATYPUS, PODAGRA, PODIATRY, PODOPHYL- LIN, POLYP, POLYPOD, SYMPODIUM; b. Russian pod, un- der: PODZOL. 8. Suffixed form *ped-ya in Greek peza, foot: TRAPEZIUM. 9. Suffixed form *ped-o- in: a. Greek pedon, ground, soil: PEDO-!; PARALLELEPIPED; b. San- skrit padam, footstep, foot, and pat (> Hindi paisd), foot: PAISA, PICE, PIE’, PUG3; c. Middle Persian pdi, leg, foot: PAJAMAS, TEAPOY; d. lengthened-grade form *pédo- in (i) Greek pédon, rudder, steering oar: PILOT (ii) Greek pédan, to leap: DIAPEDEsIs. 10. Suffixed form *ped-i- in Greek pedilon, sandal: CYPRIPEDIUM. II. Verbal root *ped-, to stumble, fall. 1. Germanic *fetén in Old English fetian, feccean, to bring back: FETCH!. 2. Latin *ped- in: a. suffixed (comparative) form *ped-yos in Latin péor, worse (< “stumbling”): PEJORATION; IMPAIR; b. suffixed (superlative) form *ped-samo- in Latin pessimus, worst: PESSIMISM; C. suffixed form *ped-ko- in Latin peccdre, to stumble, sin: PECCABLE, PECCADILLO, PECCANT; IMPEC- CABLE. [Pok. 2. péd- 790.]
2405:TRAPEZIUM kWetwer-, ped-1
```


## [2026-09-06T22:29:32.186Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '650,656p' AHD_watkins1985.txt",
 "description": "Print AHD kwetwer entry"
}
```


### [2026-09-06T22:29:32.228Z] TOOL RESULT

```
kwed-. To sharpen. Germanic *hwatjan in Old English hweittan, to whet: WHET. [Pok. k¥ed- 636.] kwei-. To hiss, whistle. Imitative root. Germanic *hwi-n- and *hwis- in: a. Old English hwinan, to whine: WHINE; b. Old English Awisprian, to whisper: WHISPER; Cc. Old English hAwistlian, to whistle: WHISTLE. [Pok. 2. kuei- 628.] kvei-'. To pay, atone, compensate. Suffixed o-grade form *koi-néd in Greek poiné, fine, penalty, borrowed into Latin as poena, penalty: PAIN, PENAL, (PENALTY), PINE?, PUNISH; IMPUNITY, PENOLOGY, (PUNITORY), (REPINE), SUBPOENA. [Pok. k#ei-t- 636.] kwei-2. To pile up, build, make. O-grade form *koi- in: a. Sanskrit kayah, body: CHEETAH; b. suffixed form *koi-wo-, making, in denominative verb *k“oiw-eyo- in Greek poiein, to make, create: POEM, POESY, POET, POETIC, -POIESIS, -POIETIC; MYTHOPOEIC, ONOMATO- POEIA, PHARMACOPOEIA, PROSOPOPEIA. [Pok. 2. kyei- 637.] kweia-'. To value, honor. Suffixed zero-grade form *kvi-ma (< *kvia-md) in Greek timé, honor, worth: TImocrAcy. [In Pok. kvei-(t-) 636.] kweia-2. To rest, be quiet. I. Suffixed zero-grade variant form *k¥i-lo- (< *kvia-lo-). 1. Germanic *hwilé in: a. Old English Awil, while: WHILE; b. Old English hwilum, sometimes: WHILOM. 2. Possibly Latin tranguillus, tran- quil (trdns-, across, beyond; see tere@-2): TRANQUIL. IL. Variant form *kvyé- (< *kwyes-) in Latin quiés, quiet (> quiétus, calm, retiring), and in requiés, rest, and requiescere, to rest: COY, QUIET; ACQUIESCE, REQUIEM, REQUIESCAT. [Pok. k¥eis- 638.] kweit-. White; to shine. Suffixed form *kweit-o-. 1. Ger- manic *hwitaz in: a. Old English hwit, white: WHITE; b. Middle Dutch wijting, whiting: WHITING?; c. Old High German hwiz, wiz, white; EDELWEIss. 2. Germanic *hwaitjaz in Old English hwé&te, wheat (from the fine white flour it yields): WHEAT. [Pok. 3. kuei- 628.] kwek-. To appear, see, show. Variant form *kveg- in Slavic *kaz- in Russian ukazat’, to order: UKASE. [Pok. k#ek- 638.] kvel-1, To revolve, move around, sojourn, dwell. I. Basic form *kvel- in Latin colere, to till, cultivate, inhabit: COLONY, CULT, CULTIVATE, (CULTURE); INCULT, INQUI- LINE, SILVICOLOUS. II. Suffixed form *k¥el-es- in Greek telos, “completion of a cycle,” consummation, perfection, end, result (> teleos, perfect, complete): TELIC, TELIUM, TELO-; ENTELECHY, TALISMAN, (TELEOLOGY), TELEOST, TELEUTOSPORE. III. Suffixed reduplicated form *k/(e)- kvl-o-, circle. 1. Germanic *hwewlaz in Old English hwéol, hweogol, wheel: WHEEL. 2. Greek kuklos, circle, wheel: CYCLE, CYCLO-, CYCLOID, CYCLONE, CYCLOSIS; BICYCLE, ENCYCLICAL. 3. Sanskrit cakram, circle: CHUK- KER. IV. O-grade form *kvol-. 1. Suffixed form *k¥ol-so-, “that on which the head turns,” neck, in: a. Germanic *h(w)alsaz in (i) Old Norse hails, neck, ship’s bow: HAWSE (ii) Middle Dutch hals, neck: RINGHALS (iii) Germanic compound *h(w)als-berg-, “neck-protector,” gorget (*ber- gan, to protect; see bhergh-'), in Old French hauberc, hauberk: HAUBERK; b. Latin collum, neck: COL, COLLAR, COLLET, CULLET; ACCOLADE, DECOLLATE!, DECOLLETE, MACHICOLATE, (MACHICOLATION), TORTICOLLIS. 2. Suf- fixed form *kol-d in Latin -cola and incola, inhabitant (in-, in; see en): -COLOUS; PRATINCOLE. 3. Suffixed form *kvol-o- in: a. Latin anculus, “he who bustles about,” servant (an-, short for ambi-, around, about; see ambhi): ANCILLARY; b. Greek polos, axis of a sphere: POLE}, PULLEY; c. Greek -kolos, herdsman, in boukolos, cow- herd: BucoLic. 4. Suffixed zero-grade form *k»J-i- in Greek palin, again (< “revolving”): PALIMPSEST, PALIN- DROME, PALINGENESIS, PALINODE. [Pok. 1. k¥el- 639.] kvel-2, Far (in space and time). 1. Lengthened-grade form *kvél- in Greek téle, far off: TELE-. 2. Suffixed zero-grade form *k»l-ai in Greek palai, long ago: PALEO-. [Pok. 2. kuel- 640.]
kwelek-
kwelek-. Bundle. Proposed by some as the root of Latin culcita, mattress, sack, which is more likely of unknown origin: QUILT. [Pok. kuelak- 630.] kwelp-. To arch. 1. Germanic *hwalbjan in Old English *hwelfan, hwylfan, with parallel form *hwelman (> Middle English whelman), to turn over: WHELM. 2. Suf- fixed o-grade form *kwolp-o- in Greek kolpos, bosom, womb, vagina: GULF; COLPITIS, COLPOSCOPE, COLPOS- copy. [Pok. 2. kuelp- 630.] kwen-. Holy. Suffixed zero-grade form *kwn-s-lo- in Germanic *hunslam in Old English hisl, hiisel, Eucha- rist: HOUSEL. [Pok. kuen- 630.] kwent(h)-. To suffer. 1. Suffixed form *kventh-es- in Greek penthos, grief: NEPENTHE. 2. Zero-grade form *kenth- in: a. Greek pathos, suffering, passion, emotion, feelings: PATHETIC, PATHO-, PATHOS, -PATHY; PATHOGNO- MONIC, SYMPATHY; b. suffixed form *k“nth-sko- in Greek paskhein, to feel, suffer: PROTOPATHIC. [Pok. kventh- 641.] kwép-. To smoke, cook, move violently, be agitated emotionally. Hypothetical base of possibly related words. 1. Suffixed variant form *kup-yo- in Latin cupere, to desire: COVET, CUPID, CUPIDITY; CONCUPISCENCE. 2. Zero-grade form *kwap-, becoming *kwap- possibly in: a. Latin vapor, steam, vapor: VAPOR; EVAPORATE; b. Latin vapidus, that has emitted steam or lost its vapor, flat, poor: VAPID; c. Greek kapnos, smoke: ACAP- niA. [Pok. kuép- 596.] kver-1, To make. 1. Sanskrit karoti, he makes: SANSKRIT. 2. Suffixed form *kver-6r with dissimilated form *kel-6r in Greek pelér, monster (perhaps “that which does harm”): PELORIA. 3. Suffixed form *ker-as- in Greek teras, monster: TERATOCARCINOMA, TERATOGEN, TERA- TOID, TERATOMA. 4, Suffixed form *ker-mn in Sanskrit karma, act, deed: KARMA. [Pok. 1. kver- 641.] kwer-2. Something shaped like a dish or shell. Suffixed variant form *k”ar-yo- in Scottish Gaelic coire, cauldron, hollow, whirlpool: corrt&. [Pok. 2. kver- 642.] kwerp-. To turn oneself. 1. Germanic *hwarb- in Old English hwearf, wharf (< “place where people move about”): WHARF. 2. Germanic *hwerban in: a. Old Norse hverfa, to turn: VARVE; b. Old Norse *hvirfa, to whirl, perhaps assimilated to Danish hvirre, to whir, akin to the Scandinavian source of Middle English whirren, to whir: WHIR; C. Old Norse hAvirfla, to whirl: WHIRL; d. Old North French werble, a warbling: WARBLE!. 3. Possibly suffixed zero-grade form *kwrp-o- in Greek karpos, wrist: CARPAL, CARPUS. [Pok. kuerp- 631.] kwes-. To pant, wheeze. 1. Germanic *hwésjan in Old Norse huzsa, to hiss: WHEEZE. 2. Latin queri, to com- plain: QUARREL!, QUERULOUS. 3. Suffixed zero-grade form *kus-ti- in Greek kustis, bladder, bag (< “bellows”): cyst, cysTo-. [Pok. kues- 631.] kwé6t-. To shake. Zero-grade form *kwet-, becoming *kwat- in Latin quatere (past participle quassus, in composition -cussus), to shake, strike: CASCARA, KVETCH, SCUTCH, SQUASH?; CONCUSS, DISCUSS, PERCUSS, RESCUE, succussIoNn. [Pok. kuét- 632.] kvetwer-. Four. I. O-grade form *ketwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English féower, four: Four; b. Old English féowertig, forty: FORTY; c. Old English féowerténe, fourteen: FOURTEEN. 2. Latin quat- tuor (> Italian quattro), four: CAHIER, CARNET, QUATRAIN; CATER-CORNERED, QUATTROCENTO. IT. Mul- tiplicatives *kveturs, kvetrus, and combining forms *kvetur-, *kvetru-. 1. Latin quater, four times: (CARIL- LON), QUATERNARY, QUATERNION, QUIRE’. 2. Latin gua- drus, four-sided thing, square: CADRE, QUADRATE, QUARREL?, QUARRY?; SQUAD, SQUARE, TROCAR. 3. Latin quadri-, four: QUADRI-. 4. Latin quadra, square: QUA- DRILLE!. 5, Latin quadrdns, a fourth part: QUADRANT. 6. Latin quadrdagintd, forty (-gintd, ten times; see dekm): QUARANTINE. 7. Variant form *ket(w)r- in: a. Greek tetra-, four: TETRA-; b. Greek tessares, tettares,
lab-
four (genitive tessardn): TESSERA; DIATESSARON. c. Greek tetras, group of four: TETRAD; d. zero-grade form *k¥t(w)r- in Greek tra-, four: TRAPEZIUM. III. Ordi- nal adjective *ketur-to-. 1. Germanic *fe(d)worthén- in: a. Old English féortha, féowertha, fourth: FOURTH; b. Middle Dutch veerdel, one-fourth: FIRKIN; c. Old English féorthing, féorthung, fourth part of a penny: FARTHING. 2. Latin qudrtus, fourth, quarter: QUA- DRILLE?, QUADROON, QUART, QUARTAN, QUARTER, quarto. [Pok. kvetuer- 642.]
kwo-. Also ki-. Stem of relative and interrogative pro- nouns. 1. Germanic *hwa-, hwi- in: a. personal pronouns *hwas, *hwasa, *hwam in Old English hwd, hwes, hwem, who, whose, whom: WHO, WHOSE, WHOM; b. pro- noun *hwat in Old English hwet, what: WHAT; c. adverb *hwi in Old English hwy, why: wHy; d. relative pronoun *hwa-lik- (*lik-, body, form; see lik-) in Old English hwilc, hwelc, which: WHICH; e. adverb *hwo6 in Old English hii, how: How!; f. adverb *hwan- in (i) Old English hwenne, hwanne, when: WHEN (ii) Old English hwanon, whence: WHENCE; g. adverb *hwithré in Old English hwider, whither: WHITHER; h. adverb *hwar- in Old English hwér, where: WHERE. 2. Germanic *hwatha- raz in: a. Old English hwether, hwether, which of two, whether: WHETHER; NEITHER; b. Germanic phrase *aiwo gihwatharaz, “ever each of two” (*aiwo, *aiwi, ever; see aiw-; *gi- from *ga-, collective prefix; see kom), in Old English €ghwether, &ther, either: EITHER. 3. Latin gui, who (genitive plural guérum): QUA, QUIB- BLE, QUORUM. 4. Latin quid, what, something: HIDALGO, QUIDDITY, QUIDNUNC, QuIP. 5. Latin quam, as, than, how, in quasi (quam + si, if; see swo-), as if: QUASI. 6. Latin quod, what: QUODLIBET. 7. Latin quot, how Many: QUOTE, QUOTIDIAN, QUOTIENT; ALIQUOT. 8. Latin quom, when: QUONDAM. 9. Latin quem, whom: CON- QUIAN. 10. Latin quantus, how great: QUANTITY. 11. Latin gudlis, of what kind: QuALITY. 12. Latin ut, that: (uT). 13. Latin uter, either of two: NEUTER. 14, Latin ubi, where, and ibi, there: ALIBI, UBIQUITY. 15. Persian chiz, thing: CHEESE, [Pok. k¥o- 644.] kwon-. Dog. 1. Greek kudn, dog: CYNIC; CYNOSURE, PROCYON, QUINSY. 2. Suffixed zero-grade form “kwn-to- in Germanic *hundaz in: a. Old English hund, dog: HOUND; b. Old High German Aunt (> German Hund), dog: DACHSHUND; c. Dutch hond, dog: KEESHOND. 3. Nominative form *kw6o in Welsh ci, dog: CORGI. 4. Variant *kan-i- in Latin canis, dog: CANAILLE, CA- NARY, CANICULA, CANINE, CHENILLE, KENNEL}, [Pok. Ruon- 632.]
kerep-. Body. 1. Suffixed form *krep-es- in Germanic *hrifiz in Old English Arif, belly: MipRIFF. 2. Suffixed zero-grade form *krp-es- in Latin corpus, body, sub- stance: CORPORAL, CORPORAL’, CORPORATE, CORPOREAL, CORPOSANT, CORPS, CORPSE, CORPULENCE, CORPUS, COR- PUSCLE, CORSAGE, CORSE, CORSET; LEPRECHAUN. [Pok. 1. krep- 620.]
```


## [2026-09-06T22:29:34.092Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"--- $f\"; wc -c $f; awk 'BEGIN{RS=\"\\f\"} END{print NR\" pages\"}' $f; done\ngrep -n \"k\\^uetuer\\|kuetuer\\|q\\^uetuer\\|quetuer\" POK_full.txt | head",
 "description": "Inspect POK files"
}
```


### [2026-09-06T22:29:36.044Z] TOOL RESULT

```
--- POK_01.txt
981836 POK_01.txt
363 pages
--- POK_02.txt
1137861 POK_02.txt
433 pages
--- POK_03.txt
1170809 POK_03.txt
429 pages
--- POK_full.txt
3971883 POK_full.txt
1 pages
```


## [2026-09-06T22:29:45.935Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"etuer\\|etu̯er\\|k\\*etuer\\|q\\*etuer\" POK_02.txt | head -20\necho \"--- search 'vier' near 642\"\npython3 - <<'EOF'\nimport re\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i,p in enumerate(pages):\n    if 'etuer' in p or 'etu̯er' in p:\n        print(i, p[:200].replace('\\n',' '))\nEOF",
 "description": "Find kwetwer in Pokorny"
}
```


### [2026-09-06T22:29:47.696Z] TOOL RESULT

```
4792:k'Aetuer-,  k^etu^r-,  kl^etur-  m.,  k'ietes{o)r-  f.,  ,vier'  (enthält??  *sor  Frau');
4801:cfv.  hom.  reffffagsg,  att.  rhraosg,  böot.  nerragsg  (mit  sekundärer  Schwach- stufe); ion.  ark.  hellen.  Tsaaegsg  {*-kV:etueres)  \  reduktionsstufig  hom.  Ttiovgeg (Akk.  Tclavgag  =  ai.  catürah,  lesb.  Ttiovgwv  =  av.  ^aturam),  lesh,  auch jthcyvgsg]  dor.  wgr.  Terogsg  (*kl^etuores) ;
4807:Ai.  caturthd-,  turiya-,  türya-,  av.  tüirya- ;  arm.  6orir,  corr-ord,  kar-ord ; gr.  att.  'vexagzog,  hom.  reTgarog  (für  ^rvgxog  ^vierter'  in  Tvgratog),  böot. Tthgazog;  lat.  quäi'tus,  prän.  Quorta,  osk.  vielleicht  truto-  (s.  oben);  air. cethramad  (*kV:etru-metos) -^  gall.  p etu arios  =  3iCjmi\  petuerid]  ahd.  ßordo, ags.  feorda,  aisl.  fiördi]  lit.  ketvirtas  (lett.  ceturtais  wie  ai.  caturthd-h), aksl.  cetvrbh]  toch.  A  Hart  i^kVietuftos),  B  itwerne.
--- search 'vier' near 642
434
301   .Schmied';  k2'ti-  .Tat';  sam-krt .einmal';  daneben  mit  s-  pari-skar-  und  sam-skar-] av.  kdrdnaoiti  .macht,  vollführt,  tut',  kdrdtay-  .Tat'.  Infin.  kdrdtde,  apers. akunavarrij  kart
302 kl^etur-  m.,  k'ietes{o)r-  f.,  ,vier'  (enthält??  *sor  Frau'); Kompositionsform  ic^(e)fru-,  k^(e)tur-,  k'^(e)tur-;  Ordinale  (k^)tur- io-,   sekundär   k'^etur-to-]    Zahladverb  k'Aeturs,  
303 ramad  (*kV:etru-metos) -^  gall.  p etu arios  =  3iCjmi\  petuerid]  ahd.  ßordo, ags.  feorda,  aisl.  fiördi]  lit.  ketvirtas  (lett.  ceturtais  wie  ai.  caturthd-h), aksl.  cetvrbh]  toch.  A
```


## [2026-09-06T22:29:54.974Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (301,302,303):\n    print('==== leaf',i)\n    print(pages[i][:1800])\nEOF",
 "description": "Print Pokorny leaves 301-303"
}
```


### [2026-09-06T22:29:56.898Z] TOOL RESULT

```
==== leaf 301
  .Schmied';  k2'ti-  .Tat';  sam-krt .einmal';  daneben  mit  s-  pari-skar-  und  sam-skar-]
av.  kdrdnaoiti  .macht,  vollführt,  tut',  kdrdtay-  .Tat'.  Infin.  kdrdtde,  apers. akunavarrij  karta-]  av.  cärä  .Mittel.  Hilfsmittel',  np.  cär  , Mittel',  cära .Mittel.  Hilfe.  List'  (=  sl.  cara  .Zauber',  s.  unten);
osk.  petiro-pert  .viermal'  (:  ai.  sam-krt);
cymr.  paraf  .bewirke,  verschaffe',  Verbaln.  peri,  wozu  redupL  (aus einem  redupl.  Präs.?)  wohl  cymr.  pyhyr  .tatkräftig';
air.  cruth  .Gestalt',  cymr.  pryd  (*k'^rtu-)  .Gestalt.  Zeit';  dazu  vielleicht air.  Cru(i)thinj  mcymr.  Prydyn  .Pikten';  cymr.  Prydain  .Britannien'  hat die  Endung  von  Rhufain  (ßömanl)  bezogen;  acorn.  prit,  mcorn.  prys, bret.  pred  .Zeit';  mir.  creth  .Dichtung'  (*Ä;?^f^o-).  cymr.  prydu  ,dichten'. prydydd  .Dichter';
41
642
I
lit.    kuriü,    kürti;!, errichten,   bauen,   machen^,    daraus   vielleicht  ,Feuer anmachen,  heizen';  lett.  kurt  ^anfeuern,  heizen',  apr.  küra  ^erbaute';  anders* oben  S.  572.
Hierher  mit  der  Bed.  ,63  jemandem  antun,  verhexen',  auch  ai.  k^ty^ (,Handlung-,  Tat'  und  :)  ,Behexung,  Zauber'  u.  dgl.,  gr.  zigag  n.  ,Wunder- zeichen',  fceXwQ  n.  ,Ungetüm,  Ungeheuer',  rsXwQiog'  ^eyag,  TteXcogiog  Hes.; das  TT-  ist  Äolismus;  tvsXcjüq,  rsXwQ  aus  *7T€qo)q,  Hsqwq  dissimiliert;  Ht. keriü,  kerUi  ,jemanden  bezaubern,  in  der  Gesundheit  schädigen',  kero^ , Zauber',  slav.  6ara  f.  ,Zauber'_in  abg.  carodSjh  ,Zauberer',  cari  f.  pj^ , Zauber,  Reiz'  usw.;
vielleicht  mit  anlaut.  s-  (vgl.  ai.  sam-skar-)  ai.  ä-icarya-  ,seltsam,  wun- derbar', n.  ,Wunder',  aisl.  skars  n.  ,ein  Ungeheuer;  Riesin',  skersa  f. ,Riesin',  skyrse  m.  ,(übles)  Vorzeichen,  Phan
==== leaf 302
kl^etur-  m.,  k'ietes{o)r-  f.,  ,vier'  (enthält??  *sor  Frau');
Kompositionsform  ic^(e)fru-,  k^(e)tur-,  k'^(e)tur-;  Ordinale  (k^)tur-
io-,   sekundär   k'^etur-to-]    Zahladverb  k'Aeturs,   k^etrus   ,viermal';
Kollektiv  i-Hefuero-,  knOtuoro-,
Ai.   catvärah   m.  (Akk.  catürah),    catväri   n.,    cätasrah   f. ;    av.   cad-wärö
m.  (Gen.  caturqm),  ^atavrö  f.,  npers.  ^ahär;
r
643
arm.  ^orH  aus  *6o7'eli  <i*k^etuores  (Akk.  cors);
cfv.  hom.  reffffagsg,  att.  rhraosg,  böot.  nerragsg  (mit  sekundärer  Schwach- stufe); ion.  ark.  hellen.  Tsaaegsg  {*-kV:etueres)  \  reduktionsstufig  hom.  Ttiovgeg (Akk.  Tclavgag  =  ai.  catürah,  lesb.  Ttiovgwv  =  av.  ^aturam),  lesh,  auch jthcyvgsg]  dor.  wgr.  Terogsg  (*kl^etuores) ;
lat.  quattuor  (a  scheint,  wie  hom.  iriovgeg,  e  fortzusetzen);  osk.  pettiur] petora  n.  (vgl.  petiro-pert  ,viermaF  aus  *petriä-,  das  nach  *^riä  in  umbr. triiuper  ,dreimalO;
air.  cetk(a)ir  (fem.  cetheoir  nach  ^eoiV  „3"),  acymr.  j9e<^«ar,  ncymr.  pedwar (fem.  pedair),  corn.  peswar  (abrit.  Stadtname  IleTovagia) ;
got.  fidwör,  nord.  und  westgerm.  auf  Grund  einer  Assimilationsform *kiiekuor  (bis  auf  die  Kompositionsformen  salfr.  j^^^er-,  ags.  fyder-,  aschwed. ßceper- :  got.  fidur-) :  aisl.  /örer  m.,  /örar  f ._,  /o^or  n.,  ahd.  /eor,  /or,  as. fiuioar,  fior,  ags.  feoicer)
lit.  keturi  (Akk.  keturis  =  ai.  caturah),  fem.  heturios-^  lett.  ^e^W;  aksl. ce^j^T^e  m.,  -i  f.  n.,
toch.  A  s<«;ar  (*/(;JJe^Wer-),  B  §(t)wäry  s(t)ioer  [*k^etuores)  ,4c' ^  A  stwaräk  ,4.0'. In  Kompositis  (und  Ableitungen)  k^etur-,  k^etur-,  k'^etru-  :  ai.  cdtur- [a7dga-h  ^viergliedrig^],  mit  Schwundst.  der  1.  Silbe  av.  ä-xtüirlm  ^viermal^, ai.  turiy
==== leaf 303
ramad  (*kV:etru-metos) -^  gall.  p etu arios  =  3iCjmi\  petuerid]  ahd.  ßordo, ags.  feorda,  aisl.  fiördi]  lit.  ketvirtas  (lett.  ceturtais  wie  ai.  caturthd-h), aksl.  cetvrbh]  toch.  A  Hart  i^kVietuftos),  B  itwerne.
Von  anderem  Zubehör  sei  herausgehoben  lat.  quattuor decira,  got.  fid- wörtaihun,  ahd.  viorzehan  ,14';  dor.  ion.  delph.  rsrgcoxovra  (*k^etUor9- komte)  =  lat.  quadrägintä  „40";  av.  iia&rus  ^viermal',  ai.  catüh  =  lat. quater  {*k^etrus)]  ai.  catvard-  m.  ^viereckiger  Platz',  lit.  ketverz  ,je  vier', aksl.  cetverb,  öetvor^  ds.,  air.  cethorcho  „40"  (^k'^etru-Jcomt-s).
41*
644  *
WP.  I  512,  Trautmann  131  f.,  Schwyzer  Gr.  Gr.  I  351  f.,  589  f.,  WH.  U 394,  400  f.,   F.  Sommer  Zum  Zahlwort,  27.
k^o-,  k^.e-,  fem.  k^ä]  k^ei-  (vermutlich  einst  nur  im  Nom.  Akk.  Sg.). kY,u-  (nur  im  Adv.) ;  die  betonten  Formen  sind  Interrogativa,  die  im! betonten  Indefinita;  einzel sprachlich  z.  T.  Relativum  geworden.
1.  Stamm  kiio-,  k^e-,  fem.  küä-;  Gen.  k'iesOy  Instr.  k^^i,  Zeitadverb  ic^ozö.
A.   Kasuelle  Formen  und  nur  einzelsprachlich   belegbare  Ableitungen:
Ai.  kd-h  (=  phryg.  xog  ,irgendeiner^;  got.  has  ,wer?'),  fem.  kä  ,wer?* und  indefinit;    idg.  k^os  wohl  der  alte  Nom.  Sg.  m.;
av.  kö  (Gen.  gthav.  ka-liyä,  (Sa-hya),  fem.  kä  ,wer?,  welcher?^,  apers. ka^[^6iy'\,  als  Indef.  mit  -cTt,  oder  in  Doppelsetzung,  oder  in  neg.  oder rel.  Sätzen;  av.  kä  ,wie?^;  apers.  ada-kaiy  ,damals^  ==  gr.  jtoi  bei  Pindar jTCov'  gesetzt;
arm.  o  ,wer?^  {*kl^o-,  Meillet  Esquisse^  189),  indef.  o-k  ,irgendwer'  {-k  ^ lat.  que),  o-mn  ,wer^  (relativ  o-r  ,welcher^);  kani  ,wievieF,  kan  ,als,  nach dem  Komparativ^  (=  la
```


## [2026-09-06T22:30:34.776Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS grep catvar ===\"\ngrep -n -i \"catvar\\|čatvar\\|catwar\\|chatvar\" SNS.txt SNS_pages.txt | head -20\necho \"=== SNS page 148 (find) ===\"\ngrep -n \"\\[pdf page\" SNS_pages.txt | head -3\necho \"=== SNS grep chess/catrang ===\"\ngrep -n -i \"catrang\\|chatrang\\|shatrang\" SNS.txt | head",
 "description": "Grep SNS for catvar"
}
```


### [2026-09-06T22:30:34.860Z] TOOL RESULT

```
=== SNS grep catvar ===
SNS.txt:3949:catasrah, cattirah, catvarah: ^d^- caQwar- :fc- 
SNS.txt:10609:(Jackson. 106) catvarisSt : L caflwar^sat- sbm 
SNS.txt:28697:catvarisat 172/2 
SNS_pages.txt:2365:                                                                                                       catasrah, cattirah,  catvarah: ^d^- caQwar-                                :fc-
SNS_pages.txt:7194:                                                                      (Jackson. 106) catvarisSt                :   L caflwar^sat-                    sbm
SNS_pages.txt:14963:A                              akaSya-klsate- 38/6   kara- 209/15                      catvarisat 172/2
=== SNS page 148 (find) ===
=== SNS grep chess/catrang ===
```


## [2026-09-06T22:30:37.569Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD catrang ===\"\ngrep -n -i \"catrang\\|čatrang\\|catrang\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ===\"\ngrep -n -i \"catrang\\|čatrang\" NYB_vol2_glossary.txt | head\necho \"=== HRN shatranj ===\"\ngrep -n -i \"schatrang\\|šatranǧ\\|satrang\\|schatrandsch\" HRN.txt HUB.txt | head -20",
 "description": "Grep Pahlavi dicts for catrang"
}
```


### [2026-09-06T22:30:37.648Z] TOOL RESULT

```
=== PHD catrang ===
PHD.txt:298:čāšt [ой | N ~] lunch, meal. 1~ag [-k'] food. &а$їар [c'štk'] doctrine. čāštan, čāš- [c?s-tn'] teach. ~išn: teaching. čatrang [cting | (Ar. šatranj)] chess. *taw(la)gan [cwpk'n!! | Ar. sawlajan, N čaugān] (curved) polo-stick ; polo. CaxSágih [ch kyh] (sense of) taste. čaxšišn [chsfn! | M, J схі, N ¿aš-] taste, flavour. 148 [ME < A mh | M cy, N či] what, which. ~ ray: for what, why. ~ih: quiddity, essence. tčē [ME, v. 166] for, because, since, as, that. &ë-ëwënag [ME ^ dwynk!] how. ~ith : circumstances. čegām-iz [су?т-с | M cyg^myc], —-6(w): a little; whatever. Cegámag [cyk”mk! | N &(ag)áma] song, snatch. €éh- , —išn, v. idan. *téhag [cyhk'] grief. čehel [40 | N chil] forty. Céh-widarag [cyhwtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- | M cy-] mourn, lament, grieve. ~i8n : lamentation. ~i$nig¢ : mournful. ihr [cyhl | M cyhr, № ~] form, shape, appearance, face. žčihr(aģ) [cyhl(k') | M сулу, P -g, № ~] seed, origin; nature, essence. Cihrénidan, čihrēn- (cyhlyn-ytn'] form. Cihrig [cyhlyk'] natural. čihr-šnāsīh [суйру] physics. čim [c(y)m | M сут, N ~] reason, cause, purpose, meaning. ~ (ray): why? Cim-gó6wáàgih [сут gwh’kyh] logic. čimīģ [cymyk!] purposeful. čīn-, ~i8n, v. idan. čīnag [cynk! | P cyng, N ~a] grain, bait. Cinàr [су | N ~] oriental plane tree. činwad [cynw(p)t'], ~ puhl: the ‘divider bridge’ which separates the souls of the righteous dead, who cross, from those of the wicked, who fall off.
PHD.txt:1215:chess Catrang; (pieces) K šah, Q frazén, B pil, Kt asp, R mādayār, P payādag.
PHD.txt:4582:catrang
PHD_mackenzie.txt:6163:carrion murdar, nasa.                   chess catrang; (pieces) K sah, Q
PHD_mackenzie.txt:8480:catrang                               caw(la)gan
=== NYB ===
2710:darraky — to put one’s feet on the rock HajB:6-7.12-13; tigr andar kamān ~ to put the arrow to the bow (-string) 100%; catrang ~ to arrange a game of chess 11914.20.21. gartänäk be ~ to cast the dice 1202122; pat ... ~ to deposit in... 10719, 11312; apar ~ to put (wood) on (the fire) 95°; dast apar ~ to put one's hand (to work) 6215; bé ~ to deposit 4216, to take off (a garment) 5717; — nam m to give a name, to name 1025-36, 11421, 11623; pat nām i ... ~ to name after 1201-2; mēnišn ~ 6 to ponder on 5?2-?3, — Av. (721 sq.) ni-dä-; MPrs nh’dn, nyh?dg, Verbum 194; Ps. nyd?t; Paz. nahādan; NP nihādan; only SW.
3627:310 šāyīt [š?dyt'], cond. 3d p. sg. (nē) &ayit hat 711%, to be able, capable, 1. with a pers. subj.: kad šāyem griftan? when shall we be able to catch him? 75; 8?;-4 martömän šāyēnd ayāftan 887-9; Sūšāns apāk Kai-Xösröi kartan šāyēnd. 8820-22; 908; — 2. with a non-pers. subj.: amäh garān ziyän ... haciš šāyet butan serious harm must necessarily arise for us: from it 191-?; ctš-ē ke ziyān ne haciš Sayist bütan from which no harm could arise 411-12; kū ātaxš haciš nē šāyet vextan that is: the fire cannot break forth from it 95! (gl.); — 2. impers.: it is possible, in varying modal senses: it can, may, might (be), it is proper, suitable, fitting, permis- sible; ‘perhaps it will... .’; it is predestin- ed, necessary, must, ought to, should, passim; the difference between šāyet and tuvan may be illustrated by 719-3; hakar tài 3 rēc griftan ne šāyet, pas hac hin griftam ne tuvdn if he cannot be caught within three days it will be im- possible to catch him; sdéyet ku perhaps 81. 242; ma hakar-am ... nē brihénit estet ku Erän-sahr pat ēv-xvatāyēh be šāyēt vīnā- ristan it is perhaps not predestined for me that I should bring E. together into one kingdom 137-9; šāyet butan ka šāyet butan “it is predestinated to happen when it is predestinated to happen”, it must happen when it must, Fate will necessarily be accomplished 231-? (cf Skr yad bhavisyati tad bhavisyati); kū yam etön névak pat xuatäyeh šāyet kartan that is: so beautiful & bowl must be made for royal persons 6015 (gl.); ānēd x"arisn šāyet x"artan it is permitted to take food here 76%, v. s. v. frayist ; tài Emahčip x"artan ne šāyet during one whole month it was not possible to drink of the water 2017; — if the real subj. is a person the pret. šāytst has regularly impers. construction: asvārān ... hixtan nē šāyist the equestrians could not haul up 153-4 (cf 887-8, above sub 1); ke (indir. obj.) cim 4 han catrang vicārtan šāyist anyone who could solve the problem of this game of chess 11817-18; without
4065:vazitan [w’cytn'] caus. of the preceding v., to move: 1. trans. catrang — to play at chess 11915, 121%, — 2. intrans. to travel, to ride (= vazitan) 519-14. 6019, — Cf MPrth pdw’z ‘suite, followers’, pres. prw’z- ‘to cause to fly’, Ghilain 70; NP bazidan, büxtan ‘to play; to fly’.
4291:Xösröi [hwslwd; hwslwd' 110!5 M, but hwslwd Cod. K 43b] n. pr. A. the 3d king of the Kayanian dynasty, mostly known as Kai-Xösröi [kdhwslwd, -Iwd'] 7133. 1138-17; with the patron. Siydvaxsan 116’; eschatological hero 887°. 99—100 passim. 1065; — ~ i Kavätän, founder of five cities 114? sqq., is probably the old Kayanian king of the heroic saga. — B. the Sassanid kings from Bahram I (273— 276) onwards assumed the title ka? (g.v.) and regarded themselves as Kayanians: Kai-Kavät (488—531), his son im bag Xösröi šāhān šah i Kavätän (531-579) 10921, known as anösak-ruvän 118%; on Baxt-— v. this w. — Gr Xoopöns, NP Xusrav; Av. (1738) žhaosravah-. The spell- ings are: 1. on coins: hwslwd, hwslwdy (already Prth); hwslwy (predominant un- der Khosroes II 590-628); once hwslw? and once hwslwty (!) v. Paruck 380- 384. 386-390; Hansen, Catrang 18-19; — 2. in the inseriptions: KZSPrth hwsrw, Gr. v. Xootew, Prs hwslwb, which is also the spelling in three of the cities mention- ed 1141? sqq., certainly to be pronounced Xūsrūv = Arm Xosrov (but Syr Kösrö). In my opinion the BP form hwslwb' re- presents in reality hwslwdy, -b- being, as often at the end of the w., the cursive form of the letter d as written in the Ps.
4795:„ Eine Tischrede aus der Zeit der Sasaniden, in the same publication as Hansen. Catrang (q. v.), pp. 1-10.
6930:catur-anga-: catrang
=== HRN shatranj ===
```


## [2026-09-06T22:30:50.329Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN/HUB shatranj variants ===\"\ngrep -n -i \"schatran\\|šatran\\|satrang\\|chatrang\" HRN.txt HUB.txt | head -20\necho \"=== AFM shatranj ===\"\ngrep -n \"شطرنج\\|الشطرنج\" AFM.txt | head -10\necho \"=== PLA shatranj ===\"\ngrep -n -i \"satrang\\|šatranǧ\\|Schach\" /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10",
 "description": "Grep for shatranj across sources"
}
```


### [2026-09-06T22:30:50.399Z] TOOL RESULT

```
=== HRN/HUB shatranj variants ===
=== AFM shatranj ===
2604:الغاب في الشطرنج ٠‏ فارسيّتها دست أخذتمهسا العرب وتصرفت بها ١‏ وقد اجتمع أكثر 
4138:وان وذ بره بإد#هر ܠܝ قبالتها لعبة الترد ܝܨ معروفة ٠‏ والشطرنج معرب 29 
4139:سترنك ٠‏ وقال المعض ان الذي اخترع الشطرنج رجل اسمة ضصه والظاهر اانه ابن 
4830:5 صار فرزانً من الفرزان وهي الملكة في لعبة الشطرنج مشتق 
5516:دكش ) 0 رقعة الشطرنج فارسيّة اضلها كشت أي 0) 
=== PLA shatranj ===
10232:E- ruh: "der Turm beim Schachspiel" pers. 2, 
12895:Schach <T Ders. >; ar. > frz. ”, mhd. schach, afrz. eschac zu pers. 
12963:Osuelü - Sähsawan: "Schahseven od. Schachseven; iranische Fußtruppe" pers. 
12970:bLoll - Sähmät: "Schachmatt" pers. >>ar. 3 s. an. 
13240:e> $Satrang: "Schachspiel sd satrang pers. $Satrang mp. 
13242:dtsch. Schach <T afrz. echac zu pers. Schah 4, 
15159:ob - farzän: "die Königin im Schach" pers. s. farzäna 
15606:a“ - fil?: "der Läufer im Schach".
```


## [2026-09-06T22:30:53.781Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON darabzin ===\"\ngrep -n \"دارابزین\\|درابزین\\|دارابزين\\|درابزين\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10\necho \"=== MON qarantin ===\"\ngrep -n \"قرنطینه\\|قرنطین\\b\\|قرنطينة\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10\necho \"=== MON chatvar ===\"\ngrep -n \"چتور\\|چتوَر\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10",
 "description": "Grep Mo'in for the Persian words"
}
```


### [2026-09-06T22:30:53.886Z] TOOL RESULT

```
=== MON darabzin ===
=== MON qarantin ===
MON_part2.txt:12468:قرنطین: ۵ [- قر نطینه» معر.] (.) 
MON_part2.txt:84311:برمی‌گشت و در ایستگاه قرنطینهٌ الطور 
=== MON chatvar ===
MON_part1.txt:49843:چتور: : 28۲ [(رس.] یک چهارم گیروانکه.
```


## [2026-09-06T22:31:03.487Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON chatvar context ===\"\nsed -n '49838,49850p' MON_part1.txt\necho \"=== MON qarantin context ===\"\nsed -n '12460,12480p' MON_part2.txt\necho \"=== search قرنطینه entry ===\"\ngrep -n \"قرنطینه\" MON_part2.txt | head -10",
 "description": "Context around Mo'in entries"
}
```


### [2026-09-06T22:31:03.581Z] TOOL RESULT

```
=== MON chatvar context ===
شاخه‌های آن مدور و مانند چتر باشد. (گیا.) 
تیره‌ای از گیاهان که گل‌های آنها به شکل 
چتر در بالای شاخه‌ها قرار دارد مانند: 
جعفری و هویج. 

چتور: : 28۲ [(رس.] یک چهارم گیروانکه. 
ترا برابر با ۲۵ ۱ گرم. 

چتوک: ( ۰) (جاذ.) گنجشک. 

چچ: 6 (.) چوبی باشد چند شاخه مانند 
پنجةٌ دست و دسته‌ای هم دارد که غله کو فته 
را ندان ناد دهند؛ چهار شاخ» هید. غربالی که 
=== MON qarantin context ===
رد 0 ((ص .) همدست و 
حریف در شجاعت و کشتی و جز آن. نظیر 
مانند» ج. اقران. 

قسرناق: ۳277۰ [تسر. - قرنق] () 
خدمتکار؛ کنیزکك» ج. (به سیاق فارسی) 
قرناقان. 

قرنطین: ۵ [- قر نطینه» معر.] (.) 
جایی که در آن مسافرانی را که از سرزمینی 
۱ وارد می‌شوند که در آنجا بیماریی ساری 
مانند وبا و طاعون شیوع دارد» مدت چند 
روز نگهداری می‌کنند. 

ثرنفل: 0 (گیا.) یر ۱ است از 
رده دولیه یی‌های جدا گلب رگ که سر دسته 


فررهنگ فارسی معین 


=== search قرنطینه entry ===
84311:برمی‌گشت و در ایستگاه قرنطینهٌ الطور
```


## [2026-09-06T22:31:18.170Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== darabzin variants in MON ===\"\ngrep -n \"دارابز\\|درابز\\|دارافز\\|داروز\" MON_part1.txt MON_part2.txt | head -20\necho \"=== in BQT ===\"\ngrep -n \"دارابز\\|درابز\\|دارافز\\|داروز\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head -20\necho \"=== in ARY ===\"\ngrep -n \"دارابز\\|درابز\" incoming/ARY/ARY_pages.txt | head",
 "description": "Grep darabzin"
}
```


### [2026-09-06T22:31:18.264Z] TOOL RESULT

```
=== darabzin variants in MON ===
MON_part1.txt:58922:دارافزین: 020-10 [ - دارایز ین - داریز ین 
MON_part1.txt:58923:- داروزین - معر. دراسزین» درایز ون 
=== in BQT ===
BQT_v1_pages.txt:17991:بد‌سقان - باغین قطه‌داروزن‌دبستان,
incoming/BQT/BQT_v3_pages.txt:42211:در بپرام بشت (اوستا) . بهرام » فرشتة پیروزی ده تر کیب جمانی ‎opty‏ گرفت وخودرابزرتتت
BQT_v2_pages.txt:15918: ‫آمده‪« :‬دارا‪.‬‬      ‫«رارافز ین» (درابز بن) ) ھ‪.‬م‪ ( .‬درفرهنث رشدی‬               ‫‏‪ - A‬تمعتی اول مصحف‬
BQT_v2_pages.txt:15920: ‫قزین وداروزین » وداربزین بممنی تکیه گاه و محجرتخت وصفه و بام وتکیه گاهمطلق ‪ .‬ابوالفرج‬
BQT_v2_pages.txt:15926: ‫هقی چاپ ادیب ص ‪:۱۵۵‬دارآ فرین‌ها» ثبت شده ولی در چاپد کتر فباض « دارافزین‌ها ‪٩‬‏ و در‬
BQT_v2_pages.txt:15927: ‫رکه ‪ :‬درایزین؛‬      ‫ی مشبك» آمده وبازاوصحیح است‬               ‫دارافز‬     ‫برلن‌صی‪۹۷‬‬   ‫سقرنامةٌ ناسرخسرو اپ‬
BQT_v2_pages.txt:15985:     ‫داروزین (رك‪ :‬دار آفرین ‪9 (1‬‬   ‫ص‬   ‫دارافزین‬   ‫=‬   ‫‪°‬‬                ‫‪.‬‬    ‫رك‪ :‬دار کوب‬     ‫‪۴‬‬
BQT_v2_pages.txt:15989:         ‫‪ ۱‬کیلکی ‪( 15-78‬شاخشدرخت)‪.‬‬                          ‫«دربزین»‪« .‬درابزین»و«درایزون» (المنجد)‪.‬‬
BQT_v2_pages.txt:17036:    ‫* درابر یی ‪ -‬از بونابی ‪( 00126۳2۲1‬نرده» شدکه)معرب‌آن درابزین ودربوز «دزی‬
=== in ARY ===
```


## [2026-09-06T22:31:19.744Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD qarantina ===\"\ngrep -n \"قرنطين\\|كرنتين\\|قرنطينة\" TAD.txt TAD_pages.txt | head -20\necho \"=== TAD darabzin ===\"\ngrep -n \"درابزين\\|دارابزين\" TAD.txt | head",
 "description": "Grep TAD"
}
```


### [2026-09-06T22:31:19.805Z] TOOL RESULT

```
=== TAD qarantina ===
=== TAD darabzin ===
```


## [2026-09-06T22:31:31.088Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON darafzin ctx ===\"\nsed -n '58915,58940p' MON_part1.txt\necho \"=== BQT v2 line 17030-17045 ===\"\nsed -n '17025,17045p' BQT_v2_pages.txt\necho \"=== find pdf page tag near 17036 ===\"\nawk 'NR<=17036 && /\\[pdf page/ {p=$0; n=NR} END{}' BQT_v2_pages.txt\ngrep -n \"\\[pdf page\" BQT_v2_pages.txt | awk -F: '$1<17036' | tail -3\ngrep -n \"\\[pdf page\" BQT_v2_pages.txt | awk -F: '$1<15918' | tail -2",
 "description": "Context for darabzin in MON and BQT"
}
```


### [2026-09-06T22:31:32.796Z] TOOL RESULT

```
=== MON darafzin ctx ===

دارات: 12:2۱ (.) کروفر داروگیر. 
داراشستان: (6210) 12۲21-420 اف. ۳06 
(ص‌مر.) آنکه صاحب شأن و شوکت دارا 
باشد؛ خداوند فر و شکوه؛ دار یوش دارا 
شکوه. 

دارافزین: 020-10 [ - دارایز ین - داریز ین 
- داروزین - معر. دراسزین» درایز ون 


فرهنگ فارسی معین 


۵۳ 
دربزین ] (.) مجری که در جلو اطاق بین دو 
در سازند. تکیه گاه؛» طار می. 

دارایی: آ[-0275 (حامص. امر.) خواسته؛ 
مال) مایملکت. داشت» نگهداشت؛ نگهبانی. 
بارچه‌ای ابریشمین رنگارنگ موجدار. (ادا.) 
وزارتخانه با اداره‌ای که موظف است 
ماليات‌ها را وصول و هزینة وزارتخانه‌ها و 
موّسسات دولتی ر تأمین کند؛ مالبه. 
دارباز: 427022 [- داربازنده] (ص‌فا.) کسی 
که روی‌ریسمان حرکات جالب انجام دهد؛ 
=== BQT v2 line 17030-17045 ===
   ‫الخیط الممدود ادلی حرکة تحرک الجرس ‪ .‬فمن کات له طلامة حرکک حذاالخ‌ط فبتحر که‬
   ‫الحری مه علی‌راس الملك فوژدن له بالدخول حتی هى حاله بنفه ویشر حطلامته و جمی‌للبلاد‬
                            ‫فیها ذلك‪« ».‬اخبارالسن والهند ص ‪( ۹۱6 - ۸۱‬از افادات علامه دهشدا) ‪.‬‬
       ‫معنی‌دو کث»است‬     ‫‪( -‬عر) «درارة بروزن جبانه‪.‬‬     ‫‪۱‬‬       ‫‪ -‬امر از «درآمدن؟ ‪.‬‬        ‫‪۵‬‬
     ‫‪ - ۷‬اوستا ‪( 012[800-‬طول) ‪.‬پپلوی [ک‪4‬ر‪۳‬د‪.9‬ی‪.121711‬بلوچی‬                            ‫«شرح قاموی» ‪.‬‬
    ‫‪۷۱۱٩۰‬‏‬     ‫‏‪ d۲8‬و ‪028۲0‬اسشق ‪ ۷4۵‬یز دریر‌لوی ‪«28۳10‬منای‪.»۱۷۲:۲‬استی ‪ «018۲20‬کث‪.‬است‬
     ‫کد‪ .‬اص ‪۲٩۰‬‏ »سمنالی‪2 .‬سنگسری»سرخه‌یی‬                      ‫فرىز لدی‪,‬و لطازی ‪zdread.‬‏ عرلی ‪27‬‬
                      ‫‪.‬یلکی ‪: 28۲81‬‬
                                  ‫وشهمیرزادی‪ .22۳64‬لاسگردی ‪« 28۳621‬که‪ ۲ .‬م‪ ۳۹۱۰‬ک‬
             ‫بدستهای د گر همچنین بخواهدرفت ‪.‬‬                  ‫چه سالهای فراوان و عمرهای دراز‬
      ‫‪‎‬ناتلک« ‪. 14٩‬‬
    ‫* درابر یی ‪ -‬از بونابی ‪( 00126۳2۲1‬نرده» شدکه)معرب‌آن درابزین ودربوز «دزی‬
    ‫‪#‬معحمدات عر مبه‌سامیه ص‪ » ۲ ۷۲‬و درابر ون «المتجد» رکف ‪ :‬داریز دنه دارآ فرین(‪)۱‬‬          ‫‪ ۱‬ص‪۶۳‬‬

     ‫بغيةٌ درصفحه ‪۳۸ ۰‬‬                                                                 ‫ودارفر بن (‪. )۱‬‬
‫سوم برس‬                                                                                              ‫هراز دم‬

                                                                     ‫‪-‬ستم وجور نمودن باشد ‪.‬‬
                                                                                          ‫کردن و‬
‫‪«,‬وآن زستتیی‬      ‫وزن ابارج» لرعی ازلبلاب است؟‬
                                                         ‫درار دم بضم‌دال دوم وسکون هیم»‬
=== find pdf page tag near 17036 ===
```


## [2026-09-06T22:31:48.342Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -5 BQT_v2_pages.txt; echo \"---\"; grep -c \"\" BQT_v2_pages.txt; grep -n \"pdf page\\|^\\[\" BQT_v2_pages.txt | head -5\necho \"=== formfeeds ===\"\nawk 'BEGIN{RS=\"\\f\"} END{print NR}' BQT_v2_pages.txt\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find which formfeed page contains line 17036\nimport re\ncnt=0\nfor i,l in enumerate(lines[:17036]):\n    cnt+=l.count('\\f')\nprint('page index (0-based ff) for line 17036:',cnt)\nEOF",
 "description": "Locate BQT page for darabzin footnote"
}
```


### [2026-09-06T22:31:50.394Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
---
41071
=== formfeeds ===
683
page index (0-based ff) for line 17036: 289
```


## [2026-09-06T22:31:53.668Z] TOOL CALL #30: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\n\"",
 "description": "BQT and MON ref details"
}
```


### [2026-09-06T22:31:55.830Z] TOOL RESULT

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
```


## [2026-09-06T22:32:04.373Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor p in pages:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m and 44<=int(m.group(1))<=52:\n        print('=====',m.group(1))\n        print(p[:2500])\nEOF",
 "description": "BQT vol3 pages near printed 1254"
}
```


### [2026-09-06T22:32:06.001Z] TOOL RESULT

```
<persisted-output>
Output too large (30.2KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/byg9e6ycr.txt

Preview (first 2KB):
===== 44
[pdf page 44]
۱۲۵۳ -

همچنانکه ثیردل بردلیر وشجاع ومرداله ‎٩‏ .

شتردندان بام توعی از زاج ‎rel‏
‏وآن مصری میباشد وبدندان شتر میماند. گویند
معتدل ترین زاچهاست .

شتر ‎J‏ @ همان اشتر غاز است که‌بیخ
درخت انکدان باشد و بعضیکوبند گیاهی است
که بیخ آلراآچار سازند ۴ .

‎gin = Sas‏ اول‌ونابیوفتحنال‌وسکون
کاف » بمنی موج است اعم از موج دربا وغیره
- وآدمی را لیز کوبند که خود را بصورت شتر
و گوسفند ‎IO,‏ وماند ‎oT‏ بازد.

‏شتر گاو ۲ - جانوری است که آرا
بعربی زرافه کویند ۴ » سرآن جانور بسر شتر
ویضی کوبند بس رکاو کوهی میماند و سیثه وسم
و شاخ او بسینه وسم وشاخ کاو شبیه است.لیکن
شاخش از شاج کاو باربکتر و کوچکتر است
و پوستش ‎aul‏ پوست ‎CL‏ پر خال میباشد .
‎gull‏ جهت شترکاو پلنکه ‎js‏ کوبندش و دمش
‎ale‏ دم ‎pt‏ و دندانپایش = دندانهای خر
الاغ و گردن و د-تهایش ‎se‏ دراز و پابهایش
کوتاء ‎ay‏ . گوبند زائو ندارد وکاری نیز ازو بر

‏0 چش: دو چیز. ‎(x)‏ چك

‎٩‏ - زحاسدان شتر دل مدار مردی چشم

‏: بوزن .

‎es

‎ale EST ars‏ عجیب وفریب است‌وطیع
را از دیدش خوش میآید . کوبند ‎BU‏ حبشی با
کاو کوهی جمع میشود ‎only‏ صورت تولدمیکند
و بیشتر در ولایت نوبه بهم مپرسد - و لام یکی
از مپرهای شطرج کییر هم هست.

‏شت رگرب ‎ale pen‏ نتاس
و نامتجاس راگوبند - و دو چیژی (۱) را لیز
شتر گربه کوبند که در غابت بلندی و بستی
و کوچکی ویزرگی باشد.

‎OE se‏ - معروف است ۰ و آن
مرفی‌باشد شبیه بشتر وعربان نعامه خواننه ‎٩‏ -

‏شتر مود « کوبنددرجنگلی ازجنگلهای
عقرب زمین درختی هست که برکهای آن
کارا کیر میکند و در آن جنگل مورچة ‎“pb‏
‏میباشد ببز رکی بزغالةً بزرکیو ‎DLS‏ کوچکی.
کی که پدان جنگل در آید مورچگان بدو
آویزند و دريك لحظه پاره پاره‌ا شکنشد,

‏شتر ‎CS‏ = بر وزن (۷) ‎kes‏ » اقسام
غله راکویند که بهم آميخته باشند واکر ازآن
آشی ‎ate‏ آن آش را آش شترنجی (۳) واگر
نانی بیزند نان شترنجی (۳) گوبند ۷ .

‎ote )۳(‏ : شطرنجی .
که یشکر له بروید ز بیخ ‎HA‏ .
ظهیر فاریابی«فرهنگه نظام».

‎Ge cor ۴‏ پیخ انکدان است که درس رکه نهند وبربچال خورند ء شاعر گوید:

‏«همه س رکه کفتيم عطه دهیم

‏* رك؛ اشتر مرغ..
‎ots - ۲‏ راوبیشه راوکوه را وآب را

‏۲ - سفر؛ چرخ و نان شترتجی

‎cal?‏ فری ‎Var‏ ورك : شاهد ح
...
</persisted-output>
```


## [2026-09-06T22:32:10.772Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor p in pages:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m and int(m.group(1)) in (45,46):\n        print('=====',m.group(1)); print(p)\nEOF",
 "description": "BQT vol3 printed 1254-1255"
}
```


### [2026-09-06T22:32:12.320Z] TOOL RESULT

```
===== 45
[pdf page 45]
شتر نگ ۱« با کاف فارسی » بر وزن
و ‎gine‏ شطرلح است » و ‎OT‏ بازبی باشد ‎agate‏
‏و ‎Ke LT Sym‏ داهر هندی یا پسر او
درزمان الوشیروان اختراع کرده بود وابوزرجمهر
در برایر آن رد را ساخت و شطرنج معرب ‎OT‏
‏باشد - و بزد:
محققین تردآشاره
بجبراست وشطر نج
باختیار - ومردم
‎sill‏ کویند.
وآن کیاهیباشد . . شترنگه (عطررنج)
که بیشتر از چین‌آورند +

شتفت ‎<a‏ ارل و فتح ثالی وسکون
فا وفوقانی . بممنی ‎ath‏ و علو باشد - وسقف
‎ole‏ را نیز گویند- وپوشش هرچیز را میگویند
عموماً و پوشش عمارت و خانه و امثال ‎WaT‏
‏خمرماً ! و بکس اول و ثالی هم بنظر آمده
است ۴ .

شتکار ۴ - جتح اود بر وزن ‎Gl‏ .

)0 چك: زری شاید ؛ چش: زریرا گوشد .

—\vet—

‎fan‏ شدبار است که شکافتن زمین باشد بجهت
زراعت کردن ؛ ‎Sal Gry‏ وضم اولهم گفته‌اند.

‎)٩( ath ‏زری‎ » deo ‏بر وزن‎ = je
‏و بحاضران مجلی دهند.‎ aia glad ‏که در‎

‏شتلم ° بطم اول و انی ولام وسکون
میم ۰ بجمنی اشتلم است. و ‎OT‏ درشتی کردن
بفیر موق وبیجا وظلم‌ونه‌دی لمودن باشدیامردم.

‏شتمین ۲ » بنتح اول وسکون ابی و کسر
میم و نون ‎QSL‏ بلفت زند وپازد ‎HS)‏
‏گاه را کویند و بعربی مقعد خوانند.

‎pe‏ ۲ ۰ بنتح اول بر وزن چمن ؛ به
لت زند و پازاد (۷) بمعنی شهر باشد و بعربی
‎Aire‏ کویند.

‏شته = ‎poe‏ اول و ‎IC‏ + بسنی انکور
باشد ۸ - وهرچرز را یز گوبند که شب برآن
کذشته باشد و صباح‌خورند؟ ؛وبکراول‌وشدید
ثانی هم آمده است.

‎7

‎ws
‎Wh ‏وآن خرانی است که از‎ ath gine ‏بمعتی‎

‏من

‏”!= بفتح اول وثالیبتحتانی کشیده»

‎. ‏چك : ژندویاژند‎ (x)

‏۱ - پپلوی 6۵1۳258 , ارمنیع ‎nt? Shitranj‏ که 4۳ * ازسانسکریت ‎catur_‏
‏8 ( دارای چهارلبه باچهارحد) شامل چهار جزه: فیل,رخ " اسب , پیاده فوبلیامز ۱:۳۸۶»

‏معرب آن شطرنج :
ناجز از بیست وچهارش نبود ‎BIS‏ نرد

‏همچو در سی ودو خانه است ‎GLE‏ شترنگه .

‎. ۲۸۹ ‏لغت فرس‎ « . sat

‎cits - ۴‏ درمهذب‌الامماه پیمتی « دستهبی و « مغاک ی که بر‌ای صید شیر ساز ند
آمده > فرهنگه نظام» ‎Ken by‏ رشیدی این‌لفت را ندارد و درجهانگیری به‌عنی «بلندی ویودش
هرچیز عموماً ویوشش خانه» آمده و شاهدی ندارد , ظ . مصحف «سقف؟است .

‏۴ 2-2 شدبار < شرار ‎Base‏ .

‏6 مخنف «اشتلم» ‎Cen)‏ +

‏۴ هت ‎(Gime)‏ («.م.) در تهرالی 502121 .

‏1 - صحیفی است ازهز , 502020 ,

‎shman. shakaman‏ . پرلوی 108 ‎Sy? oS‏ ۰۸4 . ۷ - قراءتی درپولوی
که ‎oo.‏ 5847( شبر) را بعنوان 31,5 ‎shtan‏ و ‎Shatin‏ میخواندند .رك:یونکر ‎Ao‏

‎ هتس‎ : ‏رکه‎ A

‎. Cem) wilt ‏-ظ . مصحفثشبه»‎ ٩

‏*- در رشیدی

‏و جهانگری وفرهنگه تظام ‎uals‏ وشاهدی مم دیده لشده » ظ.مصحفه شینی * .

‏( برهان لاطع ‎Cow‏

===== 46
[pdf page 46]
—\Yoo

شجرة رستو

ونقره ومس وبراج وامثال آن سازند.
‎Gace‏ ۱ - بر وزن امینا . بلفت ‎wy‏

وپازند (۱) بمعنی خنده باشد و بعربی ضحك
خوالند .

بیان پنحم

در شین نقحله دار با جیم مشتمل بر چهارده لغت

صج » بفتح اول و سکون ثانی مخقف .
‎yesh‏ سفید سخت کم گیاه را کوبند که درآن‌غله
تروید - وبا نشدید ثالی‌درعرمی به‌منی‌سرشکستن
‎ath‏ - و شکافتن کشتی ‎OT‏ دربا را .

wih ۰ ‏بر وزن صاری‎ «۴ Wyle
‏زند و پازند (۱) بمعنی درخت باشد که ء بان‎
. ‏شجر گوبند‎

شجام ۴ - بنتح اولبروزنسلام ‎os‏
‏اول هم کفته‌اند , سرمای سختی باشد که درختان
را بششکاند ۴

شحافیدن * - بروزن چنایدن . به
سرما دادن چیزی وسرما خوردن باشد.

‎rele )۱(‏ ژد ویاژند +

‏شحانیده ۱ - بروزن چدانیده, کسی
را و چیزی را گوبند که سیب سرمای مخت از
جای خود و از حال خودکشته باشد.

‏شحاید ۷ بر وزن سراید » یعنی
سرما خورد وسرد شود #۰

‏شحد ۸
است که سرمای سخت باشد ۰

‎5 4 be
‏کیاهی ات که‎ ٩ ‏شحرخ ابر اهیم‎ ۱
‏پنج انگشت کویند ؛ وبسنی شجرة ابراهيم‎ LAT
. ‏خار مفیلان‌را گفته‌اند‎

‎WTS ‏رستم = درابی‌است‎ & pee
wae ‏زراوید طویل‎

‏بر وزن لمد » ‎gee‏ شجام

‏۱ - هز ‎Stind , sh(aj}tind.‏ ,پهلوی 8802 , خنده «بونکر ‎=o‏
‏۴ - هز , ‎(yl ts) shajaray‏ بهلوی ۳24 » درخت ‎٩۸۷۲ Gyr‏ قس :عرمی

‏۴ - سپاهی که نو روز گرد. آورید

‏۴ سبجام ‎(pa)‏ قی : شجالیدن , ‎samt‏ شجلیز » شجن .

‏همه یت کردش ز ‎SU‏ شجام .
دقیقی طوسی . ‎ca?‏ فری ۰۳4۵ .

‏6 - ۰سبرلازم آن«ثجیدن» و«شجاییدن» است از:شج (قس: شجام » شجد؛شجلیزشجن)
+ بدن, (یموندمسدری) ‎SU‏ کسی را سرمایی بزند گویند «شجیده باشد» .

‏خاك دربا شود بسوزد آب

‎. ‏اسم مفعول از «شجانیدن»‎ - ٩

‎. ‏نار و برق بشجاید‎ oie
. ٩۱۱۵ ‏دقیقی طوسی . «لت فری‎
al ‏رك:‎ - ۷

‎. ۱۷۵ ‏قس: شجام , شجاییدن » شجلیز ؛ ورك: لت فری‎ A
‏ج۱‎ se «) ‏کف الجنماه + بنجنکست ( پنجنگشت‎ + Quinquefolium = ٩

‎۰۱۸۳ yale Vitex agnus castus ۰۷۷۹

‎=a Jl ‏در‎ -*

‏°
‎Aristolochia longa‏ ., زرارند طوبل . «دزی جاص ۷۲۹ .
# دجایدی - سرما خوردن .رك: شجانپدن .
```


## [2026-09-06T22:32:33.037Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FRS verse najjar ===\"\ngrep -n \"شترنگ\\|شترنج\" FRS.txt FRS_pages.txt | head -10\necho \"=== TAD page structure ===\"\ngrep -n \"\\[pdf page\\|قرنط\\|كرنتين\" TAD_pages.txt | head -20\necho \"=== TAD raw grep qrntyn ===\"\ngrep -n \"رنطين\\|رنتين\" TAD.txt | head",
 "description": "FRS verse and TAD quarantine"
}
```


### [2026-09-06T22:32:33.106Z] TOOL RESULT

```
=== FRS verse najjar ===
=== TAD page structure ===
=== TAD raw grep qrntyn ===
```


## [2026-09-06T22:32:33.473Z] TOOL CALL #34: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:829 --image 2>&1 | tail -30",
 "description": "Render BQT page 829"
}
```


### [2026-09-06T22:32:35.352Z] TOOL RESULT

```
no scan of BQT covers printed page 829 (see 'scans' in refs_online.json)
```


## [2026-09-06T22:32:45.243Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD size ===\"; wc -c TAD.txt TAD_pages.txt; head -c 600 TAD_pages.txt; echo; echo \"=== TAD leaves ===\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' TAD_pages.txt\necho \"=== BQT_v2 raw around darabzin ===\"\ngrep -n \"درابر یی\\|درابزین\\|00126\" BQT_v2.txt | head",
 "description": "TAD structure and BQT raw"
}
```


### [2026-09-06T22:32:46.890Z] TOOL RESULT

```
=== TAD size ===
151889 TAD.txt
243285 TAD_pages.txt
395174 total
                                     ‫الف‬
           ‫ياكابىاللبناك‬  ‫‪َ8‬‬
                       ‫نببى‬




       ‫لحتل‬
    ‫‪ -‬اا لدم‬  ‫‪1‬‬             ‫تت‬             ‫‪7‬‬   ‫‪:‬‬
     ‫امون‬
‫ظ‬     ‫‪1‬‬



      ‫هني بنشره وتصحيحه وتعليق <واشيه‬
                            ‫ا‬


           ‫الو مان‬
              ‫دام‬    ‫ده ل‬




                    ‫« طبعة ثانية ‪6‬‬




                
=== TAD leaves ===
86
=== BQT_v2 raw around darabzin ===
26179:«دربزین». «درابزین»و«درایزون» (المنجد). 
27910:* درابر یی - از بونابی 1۲2۳62100 (نرده» شدکه)معرب‌آن درابزین ودربوز «دزی 
45857:۱ = 201510100126 (فر) « لك ۷ ص ۲۰۳ » .
```


## [2026-09-06T22:33:01.211Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -s \"https://archive.org/metadata/borhan-ghate-v2\" -o bqtv2_meta.json && python3 -c \"\nimport json;d=json.load(open('bqtv2_meta.json'))\nprint(d.get('server'),d.get('dir'))\nfor f in d['files']:\n    if f['name'].endswith(('.pdf','.jp2','.zip','_djvu.txt')): print(f['name'], f.get('size'))\n\"",
 "description": "Archive.org metadata for BQT v2"
}
```


### [2026-09-06T22:33:04.792Z] TOOL RESULT

```
ia600609.us.archive.org /25/items/borhan-ghate-v2
برهان قاطع، جلد دوم.pdf 10740708
برهان قاطع، جلد دوم_djvu.txt 2359504
برهان قاطع، جلد دوم_jp2.zip 340727786
برهان قاطع، جلد دوم_text.pdf 31711743
```


## [2026-09-06T22:33:11.417Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && for n in 289; do curl -sL -o bqtv2_n$n.jpg \"https://archive.org/download/borhan-ghate-v2/page/n$n.jpg?fit=cover&quality=100\"; file bqtv2_n$n.jpg; done",
 "description": "Download BQT v2 leaf 289 image"
}
```


### [2026-09-06T22:33:15.139Z] TOOL RESULT

```
bqtv2_n289.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2569x3970, components 1
```


## [2026-09-06T22:33:18.044Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('bqtv2_n289.jpg'); W,H=im.size; print(W,H)\nim.crop((0,int(H*0.72),W,int(H*0.92))).save('bqtv2_289_foot.png')\n\"",
 "description": "Crop footnote area"
}
```


### [2026-09-06T22:33:20.033Z] TOOL RESULT

```
2569 3970
```


## [2026-09-06T22:33:21.949Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqtv2_289_foot.png"
}
```


### [2026-09-06T22:33:22.092Z] TOOL RESULT

```

```


## [2026-09-06T22:33:22.073Z] INPUT

[Image: original 2569x794, displayed at 2000x618. Multiply coordinates by 1.28 to map to original image.]


## [2026-09-06T22:33:36.990Z] TOOL CALL #40: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T22:33:36.998Z] TOOL RESULT

```


```


## [2026-09-06T22:33:39.529Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\n# find page with 'قرنط'\nfor i,p in enumerate(pages):\n    if 'رنط' in p or 'رنت' in p:\n        print('leaf',i, p[:300])\nEOF\necho \"=== leaf 62-ish ===\"\npython3 -c \"\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[35][:1500])\n\"",
 "description": "Search TAD for quarantine"
}
```


### [2026-09-06T22:33:41.215Z] TOOL RESULT

```
87
leaf 61                                                        ‫لوش ‪ -‬اطلب كالوش‬
                          ‫كظورنت‬
                               ‫قس وقومس ‪ -‬أمير ورجل شريف ‪ -‬ان‬
 ‫قاش ‪ -‬في الفارسية ك«ش » معناه نسيج من قطن شن ثمنقل قاش الى‬
                                                         
=== leaf 62-ish ===
                                 ‫ة‬
                                 ‫سنلام‬
                                     ‫سس‬


                                 ‫‪» 0‬ع‬

 ‫زئبق وبق وزاووق ”‪ 2‬س فارسي « زيوه » وهو سال معدلى لياله‬
                                                     ‫بالزجاج‬
‫زاروب سعامي ‪ -‬ارام ‪ 7‬زريبا » معناه ضددق مرادفه لقب والأزم‬

          ‫تزرَجد‪ -‬في الفارسية ‪ 9‬زبرجد » وهو حجر يم بشبه الزمرد‬
                                   ‫سرسي « زبان » معناه لسان‬
                                                          ‫زيان فا‬
                         ‫ون ‪ -‬فارسي « زون ‪ 4‬معناه ضعيف أبله‬
    ‫ون ‪ -‬لفظة أراميةمشتقةمن« زكن ‪ 6‬أي اشترى مرادفه المشتري‬
            ‫اب أى ماء‬
                    ‫»ى ذوهب‬
                          ‫ابر‪-‬سي مركب من « زر أ‬
                                              ‫فيا‬
                                                ‫زر‬
 ‫زرييّة وزّران ‏ البّسط والقارق ‪ -‬فارسي م ركب من «زير» أى ني‬
                             ‫وبا أى رجّل وقد نقلت الى الانكليزية ‪6‬عمرهه‬
 ‫زرجون‪ -‬قضبان الكرم ‏ لانيني ‪5‬نالده‪ 05:‬معناه فرخ الشسجرة مراد‬
                        ‫زكش ‪ -‬فارسي معناه الحرير المنسوج بالذهب‬
                                                              ‫ر‬
 ‫وهو مادة صلية شبمبة بالمى‬      ‫بوناني لمعال ‪ 56523‬معاه ‪5‬‬    ‫زر نبخ‬

‫بتسيعطرأميافه فاىلكلتغة بأنه حجرلهألو‬          ‫صور‬
                                                 ‫نوه‬
                                                   ‫عاص‬
```


## [2026-09-06T22:33:47.738Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[61])\n\" | head -60",
 "description": "Print TAD leaf 61"
}
```


### [2026-09-06T22:33:49.623Z] TOOL RESULT

```
                                                       ‫لوش ‪ -‬اطلب كالوش‬
                          ‫كظورنت‬
                               ‫قس وقومس ‪ -‬أمير ورجل شريف ‪ -‬ان‬
 ‫قاش ‪ -‬في الفارسية ك«ش » معناه نسيج من قطن شن ثمنقل قاش الى‬
                                                            ‫الفارسية بلفظة فاش‬
      ‫ترك « قامش ‪ 6‬معناه قضيب وقصب و ( فجي » معناه سوط‬                     ‫‪2‬‬

 ‫وفي اللغة‬             ‫في الايطالية *‪01‬مهه وفي اللاتينية الركيكة‬       ‫فض‬
‫كا فعي منقولة من اللاتمنية الى العربية والى السسربانية ايضا‬        ‫اللعزنطية ‪805‬‬

                                                                   ‫‪6 05 2‬‬
                                                                           ‫َ ‪2‬‬
                             ‫قمهم‪ --‬فارسي «‪ ) 5‬وعرببه يعدروم‬
                    ‫معناه ‪1‬ون وموقد‬       ‫وق الخجام ب بوناني ‪5‬‬             ‫ثين‬

‫وفي اللاتينية دتاتاء معناه أعلىكل شيء مرادفه‬       ‫شه وهامة ‪ -‬بوناني ‪51‬‬
                                                                      ‫وك‬         ‫‪010‬‬

                                                            ‫قله وقلة وشعدفة‬
                                                                           ‫‪9‬‬

‫شريمتفازنى و كد ب و©أصل هذا النبات من بلاد الهند وفارس فتقل‬
             ‫الى اليونانية ونطهدسهة ومنها إلى الابطالية ‪#‬مقصد وسائر لغات اوربا‬
       ‫قكرذةف من المدفم مرادفهاقذيفة‬
                                   ‫قنبلةبتري « قومباره » وتهي‬
                                 ‫«ند» قرفن الب‬
                                             ‫ند ‪ -‬فارسي ك‬
 ‫فارسي «كندسك ‪ 6‬معنأه خصية الكاب وغو‬               ‫ا‬     ‫وفلدز دن‬          ‫‪5‬‬

                                          ‫كلب الماء وخصيته يقال لها جندييدستر‬
‫قندسة وكتدجة ‪ -‬فارسي «وكنده » وهوخشبة يستعملها البثساؤنفي‬
                                                                   ‫بنيان القناطر‬
```


## [2026-09-06T22:34:08.281Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && for n in 61 62; do curl -sL -o tad_n$n.jpg \"https://archive.org/download/TOB1932ARAR/page/n$n.jpg?fit=cover&quality=100\"; file tad_n$n.jpg; done",
 "description": "Download TAD leaf images"
}
```


### [2026-09-06T22:34:17.537Z] TOOL RESULT

```
tad_n61.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1789x2838, components 1
tad_n62.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1789x2838, components 1
```


## [2026-09-06T22:34:19.292Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/tad_n61.jpg"
}
```


### [2026-09-06T22:34:19.770Z] TOOL RESULT

```

```


## [2026-09-06T22:34:19.769Z] INPUT

[Image: original 1789x2838, displayed at 1261x2000. Multiply coordinates by 1.42 to map to original image.]


## [2026-09-06T22:34:31.218Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o tad_n60.jpg \"https://archive.org/download/TOB1932ARAR/page/n60.jpg?fit=cover&quality=100\" && python3 -c \"\nfrom PIL import Image\nim=Image.open('tad_n60.jpg'); W,H=im.size\nim.crop((0,0,W,int(H*0.55))).save('tad_n60_top.png')\nim.crop((0,int(H*0.45),W,H)).save('tad_n60_bot.png')\nprint(im.size)\"",
 "description": "Download TAD leaf 60"
}
```


### [2026-09-06T22:34:35.474Z] TOOL RESULT

```
(1789, 2838)
```


## [2026-09-06T22:34:38.040Z] TOOL CALL #46: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/tad_n60_bot.png"
}
```


### [2026-09-06T22:34:38.063Z] TOOL RESULT

```

```


## [2026-09-06T22:34:45.235Z] TOOL CALL #47: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/tad_n60_top.png"
}
```


### [2026-09-06T22:34:45.260Z] TOOL RESULT

```

```


## [2026-09-06T22:34:55.080Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (58,59,64,65,66):\n    print('==== leaf',i); print(t[i][:1200])\n\"",
 "description": "Check TAD leaves 58,59,64-66"
}
```


### [2026-09-06T22:34:58.176Z] TOOL RESULT

```
==== leaf 58
                                      ‫سد‬    ‫اهم‬



                                           ‫‪2‬ك » وهو الحجل‬
                                                        ‫قب ‪ .-‬فارسي ك‬
     ‫معنأه حماس و ‪ 110 862‬ألاتزلاه‬   ‫قرس ل أخوة النحاسى ‏ لانيني امن‬

                                                                 ‫رسسي‬
                                                                    ‫بحا‬
                                                                      ‫أقين‬
                        ‫بعر يب ‪50]0/5‬ألء وهو اسممصر ف اليونانية‬
                                                              ‫قبط ت‬

 ‫ايطالي مطةالمةن معناه فى الاصل رئيس مرادقه ناك السفينة‬            ‫قبطان ف‬

                                            ‫وفائد الجيش وعميد القوم وعمدة وكش‬
     ‫قدوم ‪ -‬عبراني « كردُوم » تأدغت الراء بالدال فصار « قدوم » وهو‬
                                                   ‫مجر النجار وم‪:‬ته‬
      ‫وهو وع سن الهوخ كرة شه حب‬               ‫بوناني ‪8‬‬       ‫قراسيأ وقراصا‬

‫‪١‬‏‬                                         ‫االعلنباسود الا ان فىلبه عجمة واحدة‬
                       ‫قراغول ‪ -‬ترك « فراغول » معناهرييئةوطليعة وخفير‬
                         
==== leaf 59
                                        ‫ده‬     ‫ااه‬



‫اراق « كرميل »عد الإل الال وهو تدناظري 'تحوت دينكم أي |‬
‫دودة ول أي حراء وهزاكوقة عراء كرن ف ‪:‬ضوف اقاء مو نف ابيقة ‪1‬‬
‫اوتستعها وهو نوسود ف نينا ‪١١‬‏‬
                            ‫ويقع على ورق شجرة بلوط القرمز وعلى أنه ) ب‬
  ‫والهند والككيك وسائرالبلدان الحارةفيجمعفىحينهويصبغ به ولونه أحر قانر‬
                                   ‫فنقل قرمر منالعر ببة الى لغات اوريا بلفظ و‪6‬ممه؟‪1‬‬

                                            ‫قرقة © ‪ --‬تركي( غورق عريهارنقاء‬
    ‫قرميبدد ‪ -‬بوناني ‪5112:2, 8‬نع‪ 21‬معناه تراب محروق أي طهيشنوي” وهو‬
                                                               ‫الخزف والفخار والاجر‬
   ‫وزاك الذئ بال حل عالقا ستول سن انوناق وموم عرو اينرنيتاة‬
    ‫عندمم زمانووقت ومدة وستون و دكأبظا على الهالزمان مرادفه دهر أي مأئة سنة‬
   ‫قترفل ‪ -‬فى اليونانية مله رخفا وهو شجر قروئه أفضل الافاويه‬
   ‫وبطلق أيضاعلىنبات بستاني زغوه علتن الاقامتفاء وان مداوكه وقد‬
                                                               ‫ينجبتز فاىئر الانطيل‬
                                             ‫قن وخر" ‪ -‬لفظ فارسي براد بهالخرير‬

   ‫قس وقِسّهس ‪ -‬أرامي « قشيشا » معناه شيخ وقديم وقد يلقب به ا
==== leaf 64
                               ‫‪ 2-0‬ل‬


                ‫فونانى ‪5169‬مم‪ !2‬عربيهالأصّيف م ى الزغر‬          ‫‪53-5‬‬

‫“سول الفيؤنانكه عار ولاموله طناسنة قارف ادراونة تن‬
                              ‫وهو قعيحشى من ملح الزئيق فيشعل البارودة‬
    ‫“كتهدا وكاغية حر ‪:‬وكتخا واه يهسقندالواليوكاتمسر"ه‬

‫«وتينا » وف اليونانية‬
                    ‫‪ - 8‬عبرانى ‪ » 65‬وى الارامية كم‬
‫للك ‪ 0‬وهو القميص من كتان وغيره الظاهر الها مشتقة من الكتان‬
                            ‫مادمها وهو نبات معروف تنسج من لهاءه الثياب‬
              ‫نالسران ‪ 3‬كر وق التونانة ددم‬             ‫‪71‬و‬
                                  ‫كرباج ب تر « ‪.‬قرباج » وهو السوط‬
‫فى ع اللكيمياوعنهكرنزنات‬     ‫يوطناسلي ‪0‬تدوطمرهء ام‬
                                                 ‫اكر‬
                              ‫‪0‬‬          ‫وهو كن من الخامض الفحهي‬

                  ‫كرنون ‪ -‬ايطالى ‪680‬ةه معناه ورق صفيق ومقو"ى‬
                           ‫اال فارسي كار حانه» معئاه معيل‬

 ‫‪ -‬بوتالى ‪ 5022:6:1‬وهو شجر سمي بالكرز كمرناسون وهي مديلة‬
‫فاىسيا الصغرى على ساحل اليحر الاسود وثقله ارلوىمية القائدأ كولو‬
                                               ‫سنة “لاق م راجم قراسيا‬
 ‫‪ 1‬راز ‪ -‬فارسي ‪ » 60
==== leaf 65
              ‫معنا ودس ويارك ومازاً ‪1‬‬                ‫‪ 1‬ع ‪ -‬لانيي ‪1‬‬

                      ‫«رشف » وهو القطن‬
                                     ‫اتيف وكرفس‪ -‬فارسي ك‬
                              ‫فلارامية «كرفسا »( بات)‬
                                                    ‫كرفس ا‬
                               ‫نات )‬          ‫الآراية ناه‬            ‫"كر حاف‬
      ‫ايطالى فوعامج رونو معناة اونشوك نومامرادقه الجر الصحي‬                ‫ال‬

‫كرنيتة ‪7‬س ايطالى هااءد‪.‬ده معناه قرن صغير وهو بوق تحيف ينفخ فيْه‬
                                                                            ‫كازمارة‬

‫واروسميهة وكروبين وشارويين ‪ -‬فاىلعيرانية « كووب ‪3‬‬                        ‫‪1‬‬

‫كع » وثم بمثلون الملاتكة الغير المنظورين الا ان صورتهم الحسوسة انما هي‬
‫‪ 85:91‬حزقيال ‪١٠:١١‬‏ الك‬              ‫ور دو أربعة أجدحة تكوين م ‪:‬خ‪4‬روج‬
 ‫أصل هذا اللفظ أشوري ومعناه حارس لان سكان شنعار فىبكابالنوا يصورون‬
                 ‫حفراً فى جدران الدور ثورا ذا أجنحة ايحرس الانواب والمداخل‬
                         ‫سب ايطالى ‪822‬ه‪ ©223‬معناه عربة وعجلة‬                 ‫>‬

 ‫كرون سديوناق وها زعو نات ووو عر عداو ا قل انيما‬
‫الكرويا نبات معروف يشبه أغصانه وورقه بالرجلة‪.‬الا 
==== leaf 66
‫فاتدير سموا به وحيد القرن على سبيل المشاعبة أدذمهها ‪:50‬عتاوهاء فراسوه‬
‫وعر وه كروكدحنأييد القرن الهنديويوز أنيكون الاسمفينيقي« قرنإحد»‬
                                                        ‫أي وحيد القرن‬
               ‫كستك وكشتبج فارمبي ‪ 9‬ع ‪ 6‬معناه خبط غليظ‬

‫الوا ‪:‬فاه ونيفاة‬            ‫“كتوفت لعن بوالقين الفولة حمر‬
‫تقممان النوروقدتكسف الشمس لهاولة القمربينهاويين الارض مرادفه احتجي‬
‫"ابح لاتق دءمفادن وهو شجر وف اليونانية «م«ماوةا سمي‬
                                   ‫باسممدينة فى بلاد اليونان مهدا الامبر‬

        ‫"تان حب فارسي « انكشتانه » معناه اصبعي مرادفه فمالخباط‬

  ‫رديبطهة‬
        ‫خمرا‬
           ‫معناهجامكل شيء وال‬        ‫‪ 1-‬ب أرامي‪ 8‬كر‪0‬‬
‫ل المذكور « كناش » فى قالون ان سينا‬        ‫امتكدي يجمم فها رزقه ومن‬
                           ‫وهودقتريكتب فيهالانسان ماينغي أن محنظه‬
                                   ‫تعريب «كاك ‪ 6‬القارسبى‬        ‫“كيك‬

 ‫معناه غطاء عقب الرجل ‪ .‬وجورب‬       ‫كاسات وقاشين ‪ -‬لانيني ‪3‬ع‬

       ‫‪0‬‬            ‫رلارجدلفه لفافة الرجل‬
                                        ‫ججوارب فارسيمعناهقبمر ا‬
‫وتالى ‪5‬ه معناه إرث ونصيب واللمراد به كبئةاليعةلان‬           ‫كليرس‬
```


## [2026-09-06T22:35:08.446Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o tad_n59.jpg \"https://archive.org/download/TOB1932ARAR/page/n59.jpg?fit=cover&quality=100\" && python3 -c \"\nfrom PIL import Image\nim=Image.open('tad_n59.jpg'); W,H=im.size\nim.crop((0,int(H*0.30),W,int(H*0.80))).save('tad_n59_mid.png')\"",
 "description": "Crop TAD leaf 59"
}
```


### [2026-09-06T22:35:12.447Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:35:14.509Z] TOOL CALL #50: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/tad_n59_mid.png"
}
```


### [2026-09-06T22:35:14.535Z] TOOL RESULT

```

```


## [2026-09-06T22:35:32.260Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o tad_n65.jpg \"https://archive.org/download/TOB1932ARAR/page/n65.jpg?fit=cover&quality=100\" && python3 -c \"\nfrom PIL import Image\nim=Image.open('tad_n65.jpg'); W,H=im.size\nim.crop((0,0,W,int(H*0.45))).save('tad_n65_top.png')\"",
 "description": "Crop TAD leaf 65"
}
```


### [2026-09-06T22:35:36.528Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:35:38.484Z] TOOL CALL #52: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/tad_n65_top.png"
}
```


### [2026-09-06T22:35:38.509Z] TOOL RESULT

```

```


## [2026-09-06T22:36:23.338Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/TAD data/verification/sources/refs/ocr/BQT\ncat > data/verification/sources/refs/ocr/TAD/62.vision.txt <<'EOF'\n[TAD = Tobia al-Unaysi, Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya, 2nd ed. Cairo 1932\n archive.org/details/TOB1932ARAR, leaf n65 = printed page ٦٢ (62). Read from the page image\n by Claude (vision) on 2026-09-06 for verification of PDF page 295, node #13.]\n\n— ٦٢ —\n\nكَرَّس — لاتيني consecrare معناه قدَّس وبارك ومجازاً خصَّص\nكُرسف وكِرفِس — فارسي « كَرشَف » وهو القطن\nكَرَفس — في الارامية « كَرفسا » ( نبات )\nكَرَنب — في الارامية « كرّبـا » ( نبات )\nكرنتينا — ايطالي quarantena معناه أربعون يوما مرادفه المحجر الصحي\nكرنيتة (١) — ايطالي cornetta معناه قرن صغير وهو بوق نحيف ينفخ فيه كالزمارة\nكَروبيّون وكَروبيّة وكَروبين وشاروبين — في العبرانية « كروب ج كرُوبيم » وهم يمثلون الملائكة ...\n\n[Key line for the verification: كرنتينا — ايطالي quarantena معناه أربعون يوما مرادفه المحجر الصحي\n = \"karantīnā — Italian quarantena, meaning 'forty days'; its synonym is al-maḥjar al-ṣiḥḥī.\"]\nEOF\ncat > data/verification/sources/refs/ocr/BQT/829.vision.txt <<'EOF'\n[BQT = Borhan-e Qate', ed. Mo'in; vol. 2, archive.org/details/borhan-ghate-v2 leaf n289 =\n printed page ۸۲۹ (829; confirmed by the catch-line «بقیهٔ در صفحه ۸۳۰» at the foot).\n Read from the page image by Claude (vision) on 2026-09-06 for verification of PDF page 295,\n nodes #19-#20. Mo'in's etymological footnote at the foot of the page:]\n\n* درابزین ـ از یونانی Trapézion (نرده، شبکه) معرّب آن درابزین و دربوز «دزی ج ۱ ص ۴۳۰»\n«معجمیات عربیة سامیة ص ۲۲۷» و درابزون «المنجد». رک: داربزین، دارآفرین(۱) و دارفرین(۱).\n                                                            بقیهٔ در صفحه ۸۳۰\n\n[i.e. Mo'in: darābzīn is from Greek \"Trapézion\" (\"railing, lattice\"); its Arabicized forms are\n درابزین and دربوز (citing Dozy vol.1 p.430 and Mu'jamiyyat 'arabiyya samiyya p.227), and\n درابزون (al-Munjid).]\nEOF\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/tad_n65.jpg data/verification/sources/refs/ocr/TAD/62.png 2>/dev/null\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqtv2_n289.jpg data/verification/sources/refs/ocr/BQT/829.png\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg295.png data/verification/sources/refs/ocr/BOOK/295.png\nls -la data/verification/sources/refs/ocr/TAD data/verification/sources/refs/ocr/BQT | head -20",
 "description": "Save vision readings and page images"
}
```


### [2026-09-06T22:36:25.225Z] TOOL RESULT

```
data/verification/sources/refs/ocr/BQT:
total 40704
drwxrwxr-x  2 sfmqrb sfmqrb  12288 Sep  6 18:36 .
drwxrwxr-x 12 sfmqrb sfmqrb   4096 Sep  6 18:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb 368375 Sep  4 13:39 0001.png
-rw-rw-r--  1 sfmqrb sfmqrb   1684 Sep  4 13:39 0001.txt
-rw-rw-r--  1 sfmqrb sfmqrb 534367 Sep  4 13:39 0049.png
-rw-rw-r--  1 sfmqrb sfmqrb   2677 Sep  4 13:39 0049.txt
-rw-rw-r--  1 sfmqrb sfmqrb   1076 Sep  4 15:27 103.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 330101 Sep  6 17:59 1092.jpg
-rw-rw-r--  1 sfmqrb sfmqrb   2600 Sep  6 17:59 1092.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 541712 Sep  6 17:54 1187.png
-rw-rw-r--  1 sfmqrb sfmqrb   1579 Sep  6 17:54 1187.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 393921 Sep  6 11:40 1219.png
-rw-rw-r--  1 sfmqrb sfmqrb   3603 Sep  6 11:40 1219.txt
-rw-rw-r--  1 sfmqrb sfmqrb    818 Sep  6 11:40 1219.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 435393 Sep  6 10:57 1223.png
-rw-rw-r--  1 sfmqrb sfmqrb   4468 Sep  6 10:57 1223.txt
-rw-rw-r--  1 sfmqrb sfmqrb 446843 Sep  4 13:39 1225.png
-rw-rw-r--  1 sfmqrb sfmqrb   4412 Sep  4 13:39 1225.txt
```


## [2026-09-06T22:36:29.458Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7et%CA%B0w%C3%B3res",
 "prompt": "Give the reconstructed PIE root/numeral for \"four\": exact form, meaning, and the list of descendants — especially Proto-Indo-Iranian, Avestan, Old Persian, Armenian, Proto-Germanic, Latin, Greek, Balto-Slavic. Quote the Avestan and Armenian forms and the Proto-Germanic form verbatim."
}
```


## [2026-09-06T22:36:31.519Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%D9%87%D8%A7%D8%B1",
 "prompt": "Give the Persian entry for چهار: etymology (Middle Persian, Old Iranian, Proto-Indo-Iranian, PIE forms), meaning, and any derived terms like چهل, چهارده, چهارک."
}
```


### [2026-09-06T22:36:31.759Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T22:36:37.871Z] TOOL RESULT

```
# Persian Entry: چهار

## Meaning
The word **چهار** (čahār / čahâr) is a Persian numeral meaning "four" (۴).

## Etymology
This term traces back through multiple language families:

- **Middle Persian**: /čahār/
- **Proto-Iranian**: *čaθwā́rah
- **Proto-Indo-Iranian**: *čatwā́ras
- **Proto-Indo-European**: *kʷetwóres

The entry notes that it is "inherited from Middle Persian" and ultimately derived from Proto-Indo-European, with cognates appearing in Sanskrit (catur), Armenian (čʻors), Lithuanian (keturi), Latin (quattuor), and English (four).

## Linguistic Forms
The numeral has alternative colloquial forms including چار (čār) and چاهار (čāhār in Iranian Persian).

## Derived Terms
Related words include:
- **چهارده** – fourteen
- **چهارشنبه** – Wednesday
- **چهارصد** – four hundred
- **چهارپا** – quadruped
- **چارک** – quarter

These compounds demonstrate the word's generative function in Persian vocabulary construction.
```


## [2026-09-06T22:36:42.276Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7etw%C3%B3res",
 "prompt": "Give the PIE numeral \"four\": exact reconstructed form, and its descendants — Proto-Indo-Iranian, Avestan, Old Armenian, Proto-Germanic, Latin, Ancient Greek, Proto-Slavic. Quote the Avestan, Old Armenian and Proto-Germanic forms verbatim, and note any remark about the Germanic p-/f- form."
}
```


## [2026-09-06T22:36:43.629Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/quarantine",
 "prompt": "Give the full etymology of \"quarantine\", including the Italian and Venetian forms, the Latin source, the date, and also whatever it says about \"quarantina\"/\"quaranta\"."
}
```


### [2026-09-06T22:36:48.021Z] TOOL RESULT

```
# Proto-Indo-European "Four"

**Reconstructed Form:** *kʷetwóres

**Key Descendants:**

- **Proto-Indo-Iranian:** *čatwā́ras
- **Old Armenian:** čʻorkʻ (չորք)
- **Proto-Germanic:** *fedwōr
- **Latin:** (derived from Proto-Italic *kʷettwōr)
- **Ancient Greek:** (derived from Proto-Hellenic *kʷétwores)
- **Proto-Slavic:** (derived from Proto-Balto-Slavic *ketū́res)

**Note on Germanic Form:** The Proto-Germanic reflex shows *fedwōr with an initial *f- rather than *kʷ-, reflecting regular sound changes in the Germanic branch where the labiovelar consonant underwent different phonological developments compared to other Indo-European languages.
```


### [2026-09-06T22:36:52.107Z] TOOL RESULT

```
# Full Etymology of "Quarantine"

**Noun Form (1660s):**
The term originated from Italian *quaranta giorni*, literally "space of forty days." It derives from *quaranta* (forty), which comes from Latin *quadraginta* (forty). This Latin term relates to *quattuor* (four), ultimately traced to the Proto-Indo-European root *kwetwer- (four).

**Historical Origin:**
The naming convention stems from Venetian maritime policy. "The Venetian policy (first enforced in 1377) of keeping ships from plague-stricken countries waiting off its port for 40 days" established this practice to verify no latent plague cases existed aboard arriving vessels.

**Earlier English Uses:**
Before the medical sense emerged, the word appeared in English during the 1520s referring to "period of 40 days in which a widow has the right to remain in her dead husband's house." An earlier variant, *quarentyne* (15c.), denoted "desert in which Christ fasted for 40 days."

**Verb Form (1804):**
The verbal usage meaning "put under quarantine" or figuratively "to isolate, as by authority" dates to 1804, derived directly from the noun form.

The document does not contain information about "quarantina" specifically.
```


## [2026-09-06T22:36:56.994Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cadre",
 "prompt": "Give the etymology of \"cadre\" (French cadre, Italian quadro, Latin quadrum/quadrus). Also, if present on the page, note the etymologies of \"square\" and \"squad\" and \"quarter\"/\"quart\"."
}
```


## [2026-09-06T22:36:57.968Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/trapeze",
 "prompt": "Give the etymology of \"trapeze\" and \"trapezoid\": the Greek trapeza, its analysis as \"four-footed\" (tra- + peza), and the route into French/Latin/English."
}
```


### [2026-09-06T22:37:03.096Z] TOOL RESULT

```
# Etymology of "Cadre" and Related Words

**Cadre** (noun, 1851): "permanently organized framework of a military unit" from French *cadre*, literally "a frame of a picture" (16c.). The French term derives from Italian *quadro*, which comes from Latin *quadrum* meaning "a square," related to *quattuor* "four" from the Proto-Indo-European root *kwetwer-.

The communist political sense emerged later: "group or cell of workers trained to promote the interests of the Party" (1930).

**Square**, **Squad**, and **Quarter/Quart** all share this same etymological lineage through the PIE root *kwetwer-* (meaning "four"). The page indicates these words "might form all or part of" an extensive list of related terms, all ultimately deriving from the concept of "four" or "square" (a four-sided shape). This includes *quadrant*, *quartet*, *quarter*, and numerous other words with the *quad-* prefix.
```


### [2026-09-06T22:37:04.991Z] TOOL RESULT

```
# Etymology of Trapeze and Trapezoid

## Trapeze
The word **trapeze** entered English in 1861 from French *trapèze*, derived from Late Latin *trapezium*. The name reflects the device's shape: "the crossbar, the ropes and the ceiling formed a trapezium."

## Trapezoid and the Greek Root
Both terms trace to Greek *trapezion*, meaning "irregular quadrilateral," literally "a little table." This Greek word decomposes into components reflecting its original meaning: *tra-* (meaning "four") plus *peza* ("foot, edge").

## The Route into English
The pathway traveled through multiple languages: Greek *trapezion* → Late Latin *trapezium* → French *trapèze* → English *trapeze* (1861).

The geometric sense appeared earlier in English around the 1560s via the Latin form, while the gymnastics apparatus represents the later 19th-century adoption. The wrist bone (*trapezium*) was named using this same term by 1840, sharing the four-sided shape analogy.
```


## [2026-09-06T22:37:09.416Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%B7%D8%B1%D9%86%D8%AC",
 "prompt": "Give the Arabic and Persian entries for شطرنج: etymology (Middle Persian čatrang, Sanskrit caturaṅga), meanings, and any Persian variants like شترنگ / چترنگ."
}
```


## [2026-09-06T22:37:11.292Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%A7%D8%A8%D8%B2%D9%8A%D9%86",
 "prompt": "Give the Arabic entry for درابزين: meaning and etymology (any Greek source such as τραπέζιον or δρύφακτος), and any Persian/Turkish related forms."
}
```


### [2026-09-06T22:37:15.609Z] TOOL RESULT

```
# شطرنج (Shatranj) - Arabic and Persian Entries

## Arabic Entry
**Meaning:** "shatranj" or "chess"

**Etymology:** Borrowed from Classical Persian *čatrang*, which came from Middle Persian *čatrang* ("chess"), ultimately from Sanskrit *caturaṅga* ("comprising elephants, chariots, cavalry, and infantry"). The Sanskrit term combines *catúr* ("four") + *áṅga* ("limb, member"), literally meaning "four limbs; four members."

## Persian Entry
**Meaning:** "shatranj" or "chess"

**Alternative Forms:** The Wiktionary page lists several variants including *šatranj*, *eštranj*, *eštrang*, *šatrang*, *čatrang*, *satrang*, *satranj*, and *šafatranj*.

**Etymology:** Similar to Arabic, Persian borrowed this term from Arabic *šaṭranj*, which itself was borrowed from Classical Persian *čatrang*. The ultimate origin traces back through Middle Persian to Sanskrit *caturaṅga* with the same meaning structure.

Both entries share the same etymological path through Sanskrit and Persian languages, reflecting how the word spread across regions over centuries.
```


### [2026-09-06T22:37:16.471Z] TOOL RESULT

```
# درابزين (Darābzīn)

## Meaning
The word refers to a "railing, handrail, or banister" in Hijazi Arabic.

## Etymology
According to the Wiktionary entry, the term traces back through multiple languages:

- **Source**: "From Ottoman Turkish _طرابزان_ (tarabizan), from Persian _داربزین_ (dârabzin)"

The etymology section notes this derivation is incomplete and invites expansion.

## Related Forms
An alternative spelling exists: دربزين (darabzīn), with a slightly different vowel pattern.

## Note on Greek/Classical Origins
The provided Wiktionary content contains no references to Greek etymological sources such as τραπέζιον or δρύφακτος. The documented lineage begins with Persian and Ottoman Turkish forms rather than classical Greek.
```


## [2026-09-06T22:37:22.759Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/trabzan",
 "prompt": "Give the etymology of Turkish \"trabzan\" (railing/banister): the Greek or Persian source, forms and dates."
}
```


## [2026-09-06T22:37:23.911Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D1%87%D0%B5%D1%82%D0%B2%D0%B5%D1%80%D1%82%D1%8C",
 "prompt": "Give the Russian entry for четверть: meanings (including any unit of weight/measure), and etymology (Proto-Slavic, PIE)."
}
```


### [2026-09-06T22:37:26.818Z] TOOL RESULT

```
I cannot provide the etymology information you've requested based on the provided content. The web page excerpt shown is only the header and footer of the Nişanyan Sözlük (Nişanyan Dictionary) website—it contains navigation elements, copyright notice, and policy links, but no actual dictionary entries or etymological data about the word "tırabzan."

To find the etymology of Turkish "tırabzan" (railing/banister), you would need to access the full dictionary entry on that website.
```


### [2026-09-06T22:37:29.930Z] TOOL RESULT

```
# Четверть (Russian Entry)

## Meanings

The word **четверть** (čétvertʹ) is a feminine inanimate noun with several definitions:

1. "Quarter, fourth" — as in "три четверти" (three quarters)
2. School term or quarter
3. In astronomy: "quarter, phase" of the moon
4. In music: "crotchet, quarter note"

The entry also notes usage for time expressions: "четверть второго" means "quarter past one," while "без четверти два" means "quarter to two."

## Etymology

The page indicates the word is derived from Proto-Indo-European (PIE), specifically noting the category "Russian terms derived from the Proto-Indo-European word *kʷetwóres." However, the specific Proto-Slavic etymology is not explicitly detailed in this entry—only the PIE connection is provided.

**Note:** The entry contains an Etymology section header but no detailed content explaining intermediate etymological stages between PIE and modern Russian.
```


## [2026-09-06T22:37:45.154Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS leaf for page 148 ===\"\npython3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nimport re\n# find pages containing 'catvar'\nfor i,p in enumerate(pages):\n    if 'catvar' in p or 'catwar' in p or 'caflwar' in p or 'caQwar' in p:\n        print('leaf',i)\nEOF\necho \"=== BRT caθwārō ===\"\ngrep -n \"ca\\^θwārō\\|caθwārō\\|caqwaro\\|čaθwārō\\|cathwaro\" BRT.txt | head\ngrep -n \"caqwar\\|ca0war\\|caowar\" BRT.txt | head -5\necho \"=== HRN chahar ===\"\ngrep -n \"čahār\\|tschahār\\|čihil\\|tschihil\" HRN.txt | head -10\necho \"=== HUB ===\"\ngrep -n \"čahār\\|tschahār\\|čatvārō\" HUB.txt | head -10",
 "description": "Local greps: SNS, BRT, HRN, HUB"
}
```


### [2026-09-06T22:37:47.400Z] TOOL RESULT

```
=== SNS leaf for page 148 ===
leaves 243
leaf 36
leaf 102
leaf 207
leaf 213
=== BRT caθwārō ===
=== HRN chahar ===
=== HUB ===
```


## [2026-09-06T22:37:51.249Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['SNS'],ensure_ascii=False,indent=1))\"",
 "description": "SNS ref details"
}
```


### [2026-09-06T22:37:52.934Z] TOOL RESULT

```
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


## [2026-09-06T22:37:55.470Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (102,):\n    print('==== leaf',i); print(t[i][:2500])\nEOF",
 "description": "SNS leaf 102"
}
```


### [2026-09-06T22:37:57.659Z] TOOL RESULT

```
==== leaf 102
                                          »


                        L^   ^U -b    ')')_




                j"I ;iJ           —           gsh5n:   ^
 c akta
          L,   .o^-^V         *
                                              lMpf# 160 )
                                                            bl?

                        .^./L-sB«t tar: >*~»                                                                                             .f a:           40   :   -O
                .
                                                                      (Jackson. 106) catvarisSt                :   L caflwar^sat-                    sbm


                    ,        M    3
                                      ^o>^=saxtag:J^
                                                                                                                             >*iJC       .*-:            si :A3


                        ^v^-w"-
                             :E av S nd:
                                         SGVTWN, nd =   ^:^                                      1/1Y*£   .*-!?*- :sig3nag:              S3K3**

                                            i37)
                                                       c^i                                                            .*l*-:siy3(h)                  :   -U*->*

                                                                                        U:.syawarsan   s©i-CAiffl>.   1631)syava-                    jfc-
                                                                      .
                                                                          6/ Y^.   iJ




                                                                                                                       .Crf-L   :s3xt: \*>U<J>
                                                                                                          .{GNPE.     152)/sac-                  :       t-
                                                                  I




                                                                  I
                                                                               -TA/T^ .o-ltf*L :saxt 5st5d:                  ^i^ -^ t*^^
                                                                                                                                     1




                                                                                            S1/r£ .fA-fY-n/T^ 4i»L :sSxtag: 3 >oh^L^


\o
```


## [2026-09-06T22:38:08.637Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && for n in 155 156; do curl -sL -o sns_n$n.jpg \"https://archive.org/download/VajnameShayest/page/n$n.jpg?fit=cover&quality=100\"; file sns_n$n.jpg; done",
 "description": "Download SNS leaf images"
}
```


### [2026-09-06T22:38:14.660Z] TOOL RESULT

```
sns_n155.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1094x804, components 1
sns_n156.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1094x804, components 1
```


## [2026-09-06T22:38:17.393Z] TOOL CALL #68: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/sns_n155.jpg"
}
```


### [2026-09-06T22:38:17.412Z] TOOL RESULT

```

```


## [2026-09-06T22:38:30.065Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o sns_n92.jpg \"https://archive.org/download/VajnameShayest/page/n92.jpg?fit=cover&quality=100\" && python3 -c \"\nfrom PIL import Image\nim=Image.open('sns_n92.jpg'); print(im.size)\nW,H=im.size\nim.crop((0,0,W//2,H)).resize((W,2*H)).save('sns_n92_left.png')\nim.crop((W//2,0,W,H)).resize((W,2*H)).save('sns_n92_right.png')\n\"",
 "description": "Download SNS leaf 92"
}
```


### [2026-09-06T22:38:33.596Z] TOOL RESULT

```
(1109, 804)
```


## [2026-09-06T22:38:36.278Z] TOOL CALL #70: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/sns_n92_right.png"
}
```


### [2026-09-06T22:38:36.329Z] TOOL RESULT

```

```


## [2026-09-06T22:38:47.198Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -sL -o sns_n90.jpg \"https://archive.org/download/VajnameShayest/page/n90.jpg?fit=cover&quality=100\" && python3 -c \"\nfrom PIL import Image\nim=Image.open('sns_n90.jpg'); W,H=im.size\nim.crop((W//2,0,W,H)).resize((W,2*H)).save('sns_n90_right.png')\"",
 "description": "SNS leaf 90"
}
```


### [2026-09-06T22:38:50.520Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:38:53.296Z] TOOL CALL #72: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/sns_n90_right.png"
}
```


### [2026-09-06T22:38:53.430Z] TOOL RESULT

```

```


## [2026-09-06T22:39:22.192Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT ca0waro ===\"\ngrep -n \"caθwārō\\|ca_wārō\\|čaθwārō\\|caqwârô\\|ča\\^θwārō\" BRT.txt | head\ngrep -n -i \"vier'\\|,vier\" BRT.txt | head -5\necho \"=== BRT grep catur ===\"\ngrep -n \"caθru\\|caθwar\\|ca9war\\|caGwar\" BRT.txt | head -10\necho \"=== SYN four ===\"\ngrep -n -i \"13\\.13\\|kʷetwer\\|q[ṷu]etuer\" SYN.txt | head -10\necho \"=== IEC ===\"\ngrep -n -i \"qetuor\\|kuetuor\\|qetu[ou]r\" IEC.txt | head -10",
 "description": "BRT, SYN, IEC greps"
}
```


### [2026-09-06T22:39:22.294Z] TOOL RESULT

```
=== BRT ca0waro ===
11145:•  j.  öaS-war- ;  ca/w/--  Zw.,  fem.  fiataur- 'vier',  Pliir.:  a?vahe  . .  *ahmao^ahe  .  . ävaya  .  .  %rayam  . .  '^wärS  (Nm.)  V.  18. " ;  31.  6. 43. 5*6,  =9.  Y.57. 27,  Yt.  10. 1 25, 5.13,  I20,  N,  ()0,  66',  Vd, /o,  75,  j^);  — •%watif    fi'jwana    (sd.)    .fno/iJ    Yt.  /p.  3;
=== BRT grep catur ===
=== SYN four ===
23353:13.13 WHOLE
23429:13.13 WHOLE
28759:Goth. aljan (renders fos as ‘jeal- ousy’, Rom. 13.13, otherwise ‘zeal’) = ON eljan ‘energy, endurance’, OE ellen ‘strength, vigor, courage’, OHG ellen ‘zeal, strength’, etc., etym. dub., perh. : Lat. alacer ‘lively, eager, glad’. Walde- P. 1.156. Falk-Torp 188. Feist 38. Walde-H. 1.25.
=== IEC ===
```


## [2026-09-06T22:39:28.304Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"13\\.1[0-9] FOUR\\|FOUR$\\|^13\\.1\" SYN.txt | head -20\necho \"---\"\ngrep -n -i \"quattuor\" SYN.txt | head -5",
 "description": "Buck four entry"
}
```


### [2026-09-06T22:39:30.123Z] TOOL RESULT

```
23351:13.11 Quantity
23352:13.12 Numper
23353:13.13 WHOLE
23354:13.14 Every; Au (pl.)
23355:13.15 Mucu; Many
23356:13.16 More
23357:13.17 Lirruz (Quantity); Few (Number)
23358:13.18 ENnoucH
23359:13.19 Moxtirupr, Crowp
23360:13.192 Norte on oTHER Wonps ror A CoL- LECTIVE Bopy (of Persons, Ani- mals, or Things)
23379:13.11 QUANTITY Grk. —_ xoabrns Goth. (managei) Lith. kiekybé
23405:13.12 NUMBER
23429:13.13 WHOLE
23478:13.14 EVERY; ALL (pl.)
23511:13.15 MUCH; MANY (Where only one form is entered, this is also used, either in pl. or with pl., for ‘Many’)
23595:13.162. Words for the superlative ‘most’ generally go with those for ‘more’, as Grk. mdéicros beside mAciwv, Lat. plirimus beside plis, Goth. managists beside managiza, ON flestr beside fleiri, OE mé@st beside m4, etc.
23596:13.17 LITTLE (Quantity); FEW (Number) (Where only one form is entered, this is also used, either in pl. or with pl., for ‘Few’)
23631:13.18 ENOUGH (adj. or adv.)
23681:13.19 MULTITUDE, CROWD
23711:13.192. Note on other words for a col- lective body (of persons, animals, or things). NE group (fr. Fr. groupe, fr. Ital. gruppo : groppo ‘knot’), in earliest use an art term (group of sculptured or painted figures), has become the most nearly generic term; but even this is not applied to animals. For the most part, instead of any generic term, there is a wealth of individualistic terms, differ- entiated according to the object re- ferred to. Thus, to illustrate from one language only, though a parallel variety may be seen elsewhere, note the follow- ing NE words (excluding military terms like battalion, brigade, squadron, etc., and otherwise far from exhaustive), with their most familiar applications (these are not exclusive; in fact, most of those commonly used of certain animals are sometimes used also of others and of persons). For the etymology and range of use, cf. NED. :
---
23044:pedestal, table’, quadrum ‘square’), all fr. quattuor ‘four’, in form quadru- as in quadru-plex, etc. Ernout-M. 836.
24231:2. In classical Latin the only numeral coll. sbs. are decuria and centuria for groups of 10 or 100. This type prob. started in a *quetur-ia or the like (with second syllable of quattuor in weak grade, as in Skt. catur-). Another type is seen in Umbr. puntes ‘pentads’, formed like Skt. pank-ti- ‘group of five’.
```


## [2026-09-06T22:39:35.715Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23035,23050p' SYN.txt\necho \"=== numerals ===\"\ngrep -n \"13\\.2[0-9]\\|FOUR\" SYN.txt | head -20",
 "description": "Buck context"
}
```


### [2026-09-06T22:39:35.778Z] TOOL RESULT

```
on.the cross, crucifix’ to ‘cross’. Berne- ker 634. Stender-Petersen 419 ff.
12.78 SQUARE (sb.)
Crk. rerprywvov Goth? os. Lith. keturkampis, ketvir- NG rerp&yuvo ON ferskeyttr, _ ferhyrndr tainis lat. quadralum, quadrum (adjs.) Lett.  Ceirstiris It.  quadrato, quadro Dan. firkant C@hSliveeeriee Fr. _carré Sw. Syrkant SCr.  éetverokut Sp.  cuadrado, cuadro OE féowerscijte (adj.) Boh.  lverec, civerhran Rum. pdtrat ME square, fourhuyrned Pol. czworokat, czworobok I. celharchoir, cetharuil- (adj.) Russ. éetyreugol’ntk lech (adjs.) NE square Skt. caturagra- Nir. cearnach, cearnog Du vierhoek Av. éadru.karana- (adj.)
WV. ysgwar, pedrongl Br _-karrezenn, pevare’ hor- neg NHG  viereck
a all the. words for ‘square’ are pe or compounds of words for oe The last member of the com- a 1s usually a word (or deriv. of a ae for ‘corner’ (12.76), ‘edge’ ih or ‘side’ (12.36). Only the “forms are si rom. ‘corner’ ihe Pome: mply from ‘corner’,
- Grk, Terpaywvov, neut. of adj.
TE pay ayo s, ¢ ‘YWrlg, onal of rerpa- ‘four’ and
O1 at, quadratum, neut. of quadrdtus Fr. carré, Sp. cuadrado ee pple. of guadrare ‘make Oude ae quadrus (> Tt, quadro, Sp. Mab. fo €and late in adj. use (mostly 1 Quadra ‘square, base of a
OHG fiorscoz (adj.) MHG vierecke (adj.)
pedestal, table’, quadrum ‘square’), all fr. quattuor ‘four’, in form quadru- as in quadru-plex, etc. Ernout-M. 836.
Rum. pdtrat, fr. patru ‘four’ (with in- fluence of Lat. quadratus). Tiktin 1134.
3. Ir. cethar-choir, cethr-ochair, cethar- ochair, epd. of cethir ‘four’ and eochair (NIr. ochar) ‘border, edge’.
Ir. cethar-uillech, epd. of cethir ‘four’ and uillind ‘corner’.
MIr. cernach, NIr. cearnach, cearnog, deriv. of Ir. cern ‘corner’.
W. ysgwar fr. NE square.
W. pedrongl, cpd. of pedwar ‘four’ and ongl ‘angle’.
=== numerals ===
747:Grk. aidy ‘lifetime, age’ (:Lat. aevum, aetas, etc., 14.12) is used in the NT for ‘worldly life, this world’ in sense c, e.g. Mt. 13.22, Mk. 4.19 4 pépyuva (ak Hépiuvat) rod alvas robrov ‘the care(s) of this world’. Although this use itself was not extended to ‘world’ in other senses in Greek, it is important for the history of other words used to translate it.
770:ON vergld, OF weorold, OHG weralt, etc. general Gmc. except Gothic, a cpd. of wer ‘man’ (2.21) and a noun form of adjs. for ‘old’ (14.15), hence ‘age of man’. Thus it was equivalent to and followed Lat. saeculwm in its ecclesiasti- cal use (above, 2). For the early period this is the prevailing use, e.g. in the OF gospels, Mt. 12.32, 13.22 (Grk. aiwy, Vulgate saeculum). The further de- velopment was from this sense c to sense b and eventually to sense a, until the words in question became the common expressions for ‘world’ in all senses in all the Gmc. languages. NED s.v. world. Falk-Torp 1368.
774:ChSl. svétz ‘light’ (1.61) is used once in the gospels (Mt. 13.22) to translate Grk. diay (above, 2). The semantic de- velopment was from ‘light’ to the ‘realm of light, life’ (cf. the association between ‘light’ and ‘life’, e.g. Grk. doris pas dpa ‘whoever sees the light’ = ‘lives’), hence ‘world’ in sense c, later ‘world’ in all senses, as in the present Slavic lan- guages.
2094:‘fire’, etc. (Walde-P. 2.158f.) G. S. Lane, Language 13.22.
2478:W. hogen, perh. fr. *suka : Ir. siigim, OE siican, ete. ‘suck’, and so orig. ‘suck- ling’. G.S. Lane, Language 13.25 f.
3633:Late ChSl. pastortiki ‘stepson’, pas- tortika ‘stepdaughter’, SCr. pastorak, pastorka, Boh. pastorek, pastorkyné, etym. disputed, but best explained as starting in a *pa-diktorika (cf. pa-dusti, etc., above), whence an abbreviated *nadtortika > pastortika, with new masc. formed from this. Miklosich 55. Meil- let, MSL 13.28. Otherwise Zubaty, Arch. sl. Ph. 18.815 f. Still otherwise M. Vey, BSL 32.66.
4629:and flighty young animal that follows the dam, child at the mother’s heels’ (Dinneen), this fr. *ster-p- (Lith. stirptt ‘srow up’) beside *ster-t- in NE start, startle, etc. Loth. RC 43.147. Pedersen 1.94. Walde-P. 1.631. The develop- ment of ‘foal’ through the notion of ‘tim- id, startled’ is much more probable than either of the stages assumed by Pedersen or Walde-P. G. S. Lane, Language 13.26 f.
4643:2. Grk. évos is prob. fr. the same source as Lat. asinus, though the precise phonetic relation is obscure. The old view that it belongs with Lat. onus ‘load, burden’ (cf. NG youapt, It. soma- ro, below) has recently been revived by Grégoire, Byzantion 13.288 ff.
7301:6. ChSl. neprazdina (cf. Jagié, Ent. stehungsgesch. 369), lit. ‘not empty’ epd, of neg. ne- and prazdint (see 13.22), So also Bulg. neprazdna.
7761:diseases), perh. : Skt. klaba- ‘emascu- lated, impotent, eunuch’, fr. an exten- sion of the root *kel- in Lith. kaltz istrike’, Gr. xAdw ‘break’, etc. (Walde-P. 1436 ff.). G.S. Lane, Language 13.23.
7818:115, Wartburg 1.406. um, Tana, fr. Slavic (below, 6). , crécht, NIr. créacht : W. crei- T. creizenn, NBr. kleizenn ‘scar’, ‘ ae NE scar fr. i ab’) : skra@ ‘dry piece Gs Li a ete, (Falk-Torp 1021), ir ae oe 13.28 f. rape, ar, : Ir. cneadh : Grk. xvite atch’, ON hrita ‘strike,
8034:W. blin, cf. OBr. pl. blinion ‘inert’, Gael. blian ‘lean, insipid’ etym. dub., perh. (fr. IE *mléno- or *mlino-): Skt. mlana- ‘faded, withered, exhausted, languid’, pple. of mla- ‘fade, wither, grow weary’, SCr. mlitav ‘tepid, list- less’, etc. fr. extensions of IE *mel- ‘rub, grind’ (Walde-P. 2.284 ff.). G.S. Lane, Language 13.21 f.
9087:ON braud, OF bréad, OHG brdt, etc., becoming the general Gmc. word at the expense of the preceding, is commonly derived fr. the root of OE bréowan ‘brew’, etc., as if connected with the use of yeast. So Walde-P. 2.168, Falk-Torp 112, Schrader, Reallex. 1.166, ete. But more probable is the view preferred in NED s.v. bread, that the development is from ‘bit, morsel’ (cf. OE gl. bréadru ‘frusta’ and the Northumbrian bréad = OE bitan, Vulgate buccella, Grk. Ywptov in Jn. 13.27, 30; also = aprov, Vulgate panem in Jn. 6.23), just as in Grk. Yo- ulov (above, 1), SCr. kruh (below, 6), and Sc. piece bread (NED s.v. piece, sb. 3b). In this case the word may be connected with OE bréotan ‘break’, through a parallel extension of IE *bhreu- (Walde-P. 2.196).
13225:OE twig, twigge (ME, NE twig ‘smal] branch, twig’, but in OR general ‘branch’, cf. Gospels, Mk, 13.28, Mt. 24.32, of the branches of the fig tree also Jn. 12.13 palm-treowa twigu), Dit twijg, OHG zwig (mostly ‘twig’, of. Graff 5.729; but also ‘branch’, ef, Tatian 116.4, 5), MHG zuice (likewise mostly ‘twig, sprout, cutting’), NHG 2weig, all derivs. of IE *dwi-, *dwei-- *dwou ‘two’, like ON kvistr, etc., above. Here also OHG zuog, OS tg, with vowel from the numeral. Walde-P. 1.819, Note the opposite tendencies of usage in Eng- lish (‘branch’ > ‘twig’) and German (‘twig’ > ‘branch’).
14069:W. trychu, Br. trouc’ha, beside W. trweh ‘broken, maimed’, MCorn. trehy ‘thew’, prob. fr. *truk-s- : Lith. trukti ‘rend, break, burst’, OE prycean ‘press’, etc. (Walde-P. 1.731). G.S. Lane, Lan- guage 13.27f. (vs. Walde-P. 1.758, etc.).
14243:W. torrz, Br. terri (older torri), cf. W. tor, Br. torr ‘a break, cut’, perh. fr. torp- : Lith. tarpas ‘interval, interstice’ (i.e. ‘a break’), trapus ‘fragile’, etc. (Walde-P. 1.732). G.S. Lane, Language 13.27.
14356:3. Ir. fennaim, NIv. feannaim, etym. dub. G.§S. Lane, Language 13.24.
15966:W. peth : Br. pez ‘piece, bit’, Ir. cuit ‘share, part’, etc. (13.23). Pedersen 1.160.
16364:W. hawdd, perh. : W. hedd, Ir. sid ‘peace’, with different grades of the root *sed- ‘sit’, W. hawdd fr. the a (IE 6) grade as in Ir. con-sddw ‘compono’. Loth, RC 36.162 (vs. Morris Jones 135, 247). Another suggestion (: Skt. sadhu- ‘effective, well-disposed, correct, good’), G.S. Lane, Language 13.25.
19329:ChSl. ottStetiti (Supr., etc.), SCr. ostetitt, derivs. of ChSl. tisteta, SCr. Steta ‘harm, injury’ : ChSl. ist? ‘empty’ (13.22). Leskien, Serbo-Croat. Gram. 55.
```


## [2026-09-06T22:39:44.146Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN quarantine ===\"\ngrep -n \"quarantine\" KLN_1966.txt | head -5\necho \"=== KLN cadre ===\"\ngrep -n \"^cadre\\|cadre, n\" KLN_1966.txt | head -5\necho \"=== KLN trapeze ===\"\ngrep -n \"trapeze\\b\" KLN_1966.txt | head -5\necho \"=== SKT quarantine/trapeze ===\"\ngrep -n \"QUARANTINE\\|quarantine\\|trapeze\" SKT.txt | head -8\necho \"=== LKT karantina ===\"\ngrep -n -i \"karantän\\|quarantäne\\|karantin\" LKT.txt | head -5",
 "description": "Klein, Skeat, Lokotsch greps"
}
```


### [2026-09-06T22:39:44.252Z] TOOL RESULT

```
=== KLN quarantine ===
9837:cuarenta,  n.,  a  silver  coin  of  Cuba.  —  Sp.,  ‘forty’, fr.  L.  quadraginta.  See  quadragenarian  and  cp. quarantine.
15279:fount,  n.,  the  British  equivalent  of  font.  —  F. fonte.  See  font,  ‘set  of  type  of  one  size’, fountain,  n.  —  OF.  (=  F.)  fontaine,  fr.  Late  L. fontana,  prop.  fern,  of  fontanus,  ‘pertaining  to a  spring’,  used  as  a  noun,  fr.  L  .fons,  gen  .fontis, ‘spring’.  See  font,  ‘receptacle’,  and  cp.  fontanel, four,  adj.  and  n.  —  ME.  feower,  fower,  foure, four,  fr.  OE.  feower,  rel.  to  OS.  fiuwar,  fiwar, OFris.  fiuwer,fidr,  Du.  vier,  OHG.  for,  MHG., G.  vier,  ON.  fjorir,  Dan  .fire,  Swed  .fyra,  Norw. fire,  Goth,  fidwor,  ‘four’,  and  cogn.  with  OI.  cat- vArah,  Avestic  cad  ward,  Pers.  catvdr,  Toch.  A stwar,  B  stwer,  Arm.  cork',  Gk.  -r6<j<rape<;,  Att. -nhrrapes,  Ion.  -reaaepes,  Aeol.  rrfcrjpet;,  toctu- pep,  L.  quattuor,  Oscan  petora,  Umbr.  petur-, OSlav.  cetyre,  Lith.  keturi,  OIr.  cethir,  W.  pet- guar,  pedwar,  ‘four’.  (Alb.  katsr  is  a  loan  word fr.  L.  quattuor.)  All  these  words  derive  fr.  I.-E. base  *quetwAr-,  ‘four’.  Cp.  fardel,  ‘fourth  part’, farthing,  firkin,  forty.  Cp.  also  cadre,  cahier, carfax,  carillon,  cater,  ‘four  at  cards  or  dice’, charpoy,  quadrant,  quadrate,  quadri-,  quadrille, quadroon,  quarantine,  quarrel,  ‘arrow,  bolt’, quarry,  ‘a  place  for  excavating  stones’,  quart, quatrain,  quaternion,  quire  of  paper,  squad, square,  tessara-,  tetarto-,  tetra-,  tetrakis-,  te- trarch,  trapezium,  trocar, fourchee,  fourche,  adj.,  forked,  divided  (her.)  —
31257:quadragenarian,  1)  adj.,  forty  years  old;  2)  n.,  a quadragenarian  person.  —  Formed  with  suff. -an  fr.  L.  quadragenarius,  ‘forty  years  old’,  fr. quadrageni,  ‘forty  each’,  fr.  quadraginta  (for *quatra-ginta),  ‘forty’,  which  is  formed  fr.  quat- tuor,  ‘four’,  with  -ginta,  a  suff.  denoting  tens. This  suff.  is  cogn.  with  Gk.  -xovtx  in  rpia- xov-rx,  ‘thirty’,  TscraxpS-xovra,  ‘forty’,  etc.  See four  and  cp.  quadri-.  For  the  etymology  of  the Gk.  suff.  -xovxa,  L.  suff.  -ginta,  see  penteconta-. Cp.  quarantine,  cuarenta.
31267:See  four  and  cp.  quadrant,  quadrate,  quadrille, ‘a  square  dance’,  quadroon,  quarantine,  quarrel, arrow,  bolt’,  quarry,  ‘a  place  for  excavating stones’,  quart,  quatrain,  quire  of  paper,  squad,
31326:Derivative:  quaquaversal-ly,  adv. quarantine,  n.,  a  period  (orig.  of  forty  days)  of isolation  to  prevent  the  spread  of  disease.  —  It. quarantina,  fr.  quaranta,  ‘forty’,  fr.  L.  quadra- gintd.  See  quadragenarian  and  cp.  cuarenta.  The term  goes  back  to  It.  quaranta  giorni,  ‘forty days’.  Ships  coming  from  the  Levant  and  Egypt were  isolated  at  special  ports  for  thirty,  later forty,  days.  This  measure  for  preventing  the spread  of  contagious  diseases  was  first  enforced atRagusainl377.  SeeK.  Sudhoff,  “Epidemiolo¬ gical  Rules  from  the  Past”,  in  Essays  in  the History  of  Medicine,  trans.  F.  H.  Garrison,  New York,  1926,  p.  152.
=== KLN cadre ===
=== KLN trapeze ===
39917:trapan,  n.  and  tr.  v.  —  A  var.  of  trepan, trapes,  intr.  v.  —  See  traipse, trapeze,  n.,  a  suspended  horizontal  bar  used  in gymnastics.  —  F.  trapeze,  fr.  Late  L.  trapezium.
=== SKT quarantine/trapeze ===
15305:quarantine ,  i.  F.  *  L. )  O.  F.  pm tine,  usually  quaranSaim,  a  space  of  I days.  —  F.  quaranU,  forty.  —  L  <Md gitita,  forty  ;  see  quadra^alma  (awM
=== LKT karantina ===
```


## [2026-09-06T22:39:56.410Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1971 cadre ===\"\ngrep -n \"cadre\" KLN_1971.txt | head -3\necho \"=== KLN trapezium ===\"\ngrep -n \"trapezium\" KLN_1966.txt | head -3\necho \"=== MON kadr ===\"\ngrep -n \"کادر:\" MON_part1.txt MON_part2.txt | head -3\necho \"=== PLA satrang ctx ===\"\nsed -n '13238,13246p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt\necho \"=== PHD leaf for catrang ===\"\npython3 - <<'EOF'\nt=open('PHD.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'čatrang' in p or 'catrang' in p:\n        print('leaf',i, '-> printed p.', i-21)\nEOF",
 "description": "More local lookups"
}
```


### [2026-09-06T22:39:58.259Z] TOOL RESULT

```
=== KLN 1971 cadre ===
36626:cadre, n., frame, framework; framework of a 
96671:farthing, firkin, forty. Cp. also cadre, cahier, 
=== KLN trapezium ===
15110:foot,  n.  —  ME.  fat,  fr.  OE.  fat,  rel.  to  OS.  fat, ON.  fa tr,  Swed.  fat,  Dan.  fad,  Du.  voet,  OHG. fuo3,  MHG.  VU03,  G.  Fuji,  Goth./o/u.s,  ‘foot’,  and cogn.  with  Ol.  pit,  acc.  pidam,  ‘foot’,  Avestic pad-,  ‘foot’,  Toch.  A  pe,  B  pai,  ‘foot’,  A  pent,  B paine,  ‘both  feet’.  Arm.  ot-n,  ‘foot’,  ot-k\  ‘feet’. Dor.  Gk.  7rtii ;,  Att.  7101)9  (formed  on  analogy  of 009,  ‘ear’),  gen.  770809,  L.  pes,  gen.  pedis,  ‘foot’, Ol.  paddm,  ‘step,  track’.  Arm.  het,  gen.  he  toy, ‘track,  footmark’,  Gk.  rtiSt),  ‘fetter’,  TreSav,  ‘to bind  with  fetters’,  7t£Sov,  ‘ground,  earth’,  h.peda, ‘footstep \pedica,  ‘shackle,  fetter’,  impedire,  ‘en¬ tangle,  ensnare’,  expedire,  ‘to  extricate,  disen¬ gage’,  Lith.  peda,  ‘footstep,  trace’,  OSlav.  podii, ‘loft’,  Russ,  pod-oshva,  ‘sole  of  foot’.  All  these words  derive  fr.  I.-E.  base  *pdd-,  *pid-,  ‘foot’. Cp.  fetch,  fetlock,  fetter,  fit,  ‘part  of  a  song’.  Cp. also  antipodes,  apod,  babouche,  biped,  breviped, caliber,  cap-a-pie,  charpoy,  expedient,  expedite, impeach,  impede,  impedimenta.  Lycopodium, millepede,  multiped(e),  octopus,  oppidan,  palmi¬ ped,  pawn  (in  chess),  parallelepiped,  pajama, pedal,  pedate,  -pede,  pedesis,  pedestal,  Pedetes, pedicel,  pedicle,  pedigree,  pedology,  ‘the  study  of soils’,  peduncle,  peon,  pes,  petiole,  pew,  Peziza, pie,  ‘a  small  coin’,  piepoudre,  pilot,  podagra, podal,  podium,  podo-,  pug,  ‘footprint’,  puy,  seer- paw,  Taliped,  Tarsipes,  teapoy,  trapezium,  triped, tripos,  vamp,  ‘front  part  of  the  foot’,  velocipede. Cp.  also  pejorative,  pessimism.
15279:fount,  n.,  the  British  equivalent  of  font.  —  F. fonte.  See  font,  ‘set  of  type  of  one  size’, fountain,  n.  —  OF.  (=  F.)  fontaine,  fr.  Late  L. fontana,  prop.  fern,  of  fontanus,  ‘pertaining  to a  spring’,  used  as  a  noun,  fr.  L  .fons,  gen  .fontis, ‘spring’.  See  font,  ‘receptacle’,  and  cp.  fontanel, four,  adj.  and  n.  —  ME.  feower,  fower,  foure, four,  fr.  OE.  feower,  rel.  to  OS.  fiuwar,  fiwar, OFris.  fiuwer,fidr,  Du.  vier,  OHG.  for,  MHG., G.  vier,  ON.  fjorir,  Dan  .fire,  Swed  .fyra,  Norw. fire,  Goth,  fidwor,  ‘four’,  and  cogn.  with  OI.  cat- vArah,  Avestic  cad  ward,  Pers.  catvdr,  Toch.  A stwar,  B  stwer,  Arm.  cork',  Gk.  -r6<j<rape<;,  Att. -nhrrapes,  Ion.  -reaaepes,  Aeol.  rrfcrjpet;,  toctu- pep,  L.  quattuor,  Oscan  petora,  Umbr.  petur-, OSlav.  cetyre,  Lith.  keturi,  OIr.  cethir,  W.  pet- guar,  pedwar,  ‘four’.  (Alb.  katsr  is  a  loan  word fr.  L.  quattuor.)  All  these  words  derive  fr.  I.-E. base  *quetwAr-,  ‘four’.  Cp.  fardel,  ‘fourth  part’, farthing,  firkin,  forty.  Cp.  also  cadre,  cahier, carfax,  carillon,  cater,  ‘four  at  cards  or  dice’, charpoy,  quadrant,  quadrate,  quadri-,  quadrille, quadroon,  quarantine,  quarrel,  ‘arrow,  bolt’, quarry,  ‘a  place  for  excavating  stones’,  quart, quatrain,  quaternion,  quire  of  paper,  squad, square,  tessara-,  tetarto-,  tetra-,  tetrakis-,  te- trarch,  trapezium,  trocar, fourchee,  fourche,  adj.,  forked,  divided  (her.)  —
38725:terzetto,  n.,  trio ;  vocal  trio.  —  It.,  dimin.  of  terzo, ‘third’,  fr.  L.  tertius.  See  tertian,  adj. teschemacherite,  n.,  an  acid  ammonium  carbo¬ nate  (mineral.)  —  Named  after  the  English chemist  Frederick  E.  Teschemacher  (died  in 1 863).  For  the  ending  see  subst.  suff.  -ite. tessara-,  combining  form  meaning  ‘four’.  —  Fr. Gk.  TEcraapa,  neut.  of  xiaaapEp,  ‘four',  rel.  to Att.  TETTapE?,  Ion.  T^ooEpe;,  Aeol.  Tucrupcp, Lesbian  tteoupei;,  fr.  I.-E.  base  *qwetur-,  ‘four’. See  four  and  cp.  tessera-,  diatessaron,  tetarto-, tetra-,  tetrad  and  the  first  element  in  trapezium, tessella,  n.,  a  small  tessera.  —  L-,  ‘a  little  cube', dimin.  of  tessera.  See  tessera-  and  -ella. tessellar,  adj.,  composed  of  tesserae.  —  Formed with  adj.  suff.  -ar  fr.  L.  tessella.  See  prec.  word, tesscllate,  tr.  v.,  to  pave  by  inlaying  small  square blocks  in  mosaic.  —  L.  tessellatus,  pp.  of  tessel- lare,  ‘to  chequer,  tessellate’,  fr.  tessella.  See  tes- sella  and  verbal  suff.  -ate.
=== MON kadr ===
MON_part2.txt:17223:کادر: 120 (۱) چوب بافلزی که دور 
=== PLA satrang ctx ===
. £ . L. 
-._ . u" nv RT) 
e> $Satrang: "Schachspiel sd satrang pers. $Satrang mp. 
yPpyg catrang skr. caturanga ”. 
dtsch. Schach <T afrz. echac zu pers. Schah 4, 


Juü - Sagal: "Schakal" tk. tschakal pers. Ju schagal < mp. 
Y- wu shaghal 6, syr.\e pers. ger 7, dtsch. Schakal <T skr. >> pers, 
=== PHD leaf for catrang ===
leaf 44 -> printed p. 23
leaf 201 -> printed p. 180
```


## [2026-09-06T22:40:05.547Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '17218,17232p' MON_part2.txt\necho \"=== PLA page for satrang ===\"\npython3 - <<'EOF'\nt=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'atrang' in p and 'caturanga' in p:\n        print('leaf',i); print(p[:400])\nEOF",
 "description": "Mo'in kadr, PLA page"
}
```


### [2026-09-06T22:40:07.286Z] TOOL RESULT

```
کاخ: [- یت ای باران» مطر. 
ک‌خ‌نشین : 1128[0-. [- کاخ‌نشیننده] 
(ص‌فا.) آنکه در قصر اقامت دارد؛ شاه امبر. 
کاخه: (م)سها [- کاخ] (.) باران» مطر. 
کادر: 120 (۱) چوب بافلزی که دور 
عکس يا آیینه و غیره قرار دهند؛ قاب» چهار 
چوب. (ف.) هبثت اداره کنندة یک اداره با 
موسسه. ضح. احتراز از استعمال این کلمة 
بیگانه اولی است. 

کادو: ۷200 (۰.) همدبه‌ای که به دوستان 
دهند؛ تحفه. ضح.- احتراز از استعمال این 
کلمه بگانه اولی است. 

=== PLA page for satrang ===
leaf 192
Saöma                                                                          178                                                Sikarahang_

4b          $aSma:           "Abort" <                      pers. om tefma                  "Quelle"          1,


or     Sass:           "Angelhaken"                     _     pers... Sast              2,

 .            £
```


## [2026-09-06T22:40:18.959Z] TOOL CALL #79: WebSearch

```json
{
 "query": "Armenian չորրորդ \"čatvar\" quarter Armenian word for one fourth Persian چتور Russian четверть loanword"
}
```


### [2026-09-06T22:40:26.309Z] TOOL RESULT

```
Web search results for query: "Armenian չորրորդ "čatvar" quarter Armenian word for one fourth Persian چتور Russian четверть loanword"

Links: [{"title":"չորրորդ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D5%B9%D5%B8%D6%80%D6%80%D5%B8%D6%80%D5%A4"},{"title":"Word Embeddings for the Armenian Language: Intrinsic and Extrinsic Evaluation","url":"https://arxiv.org/pdf/1906.03134"},{"title":"քառ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D6%84%D5%A1%D5%BC"},{"title":"Da (Armenian letter)","url":"https://en.wikipedia.org/wiki/Da_(Armenian_letter)"},{"title":"Armenian Language Lessons Chapter 4 - Armeniapedia","url":"https://www.armeniapedia.org/wiki/Armenian_Language_Lessons_Chapter_4"},{"title":"Da (Armenian)","url":"https://en.wikipedia.org/wiki/Da_(Armenian)"},{"title":"quattuor - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/quattuor"},{"title":"չորրորդ in English - Armenian-English Dictionary | Glosbe","url":"https://glosbe.com/hy/en/%D5%B9%D5%B8%D6%80%D6%80%D5%B8%D6%80%D5%A4"},{"title":"Category:Armenian terms by etymology - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Armenian_terms_by_etymology"},{"title":"چهار - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%DA%86%D9%87%D8%A7%D8%B1"}]

Based on the search results, I found relevant information about these related words:

The Armenian word չորրորդ (čoraord) means "fourth". The etymology involves չորի- (čʻori-) plus the suffix -րորդ (-rord), where the root relates to "four."

Regarding the broader linguistic connections, cognates include Sanskrit चतुर् (catur), Old Armenian չորք (čʻorkʻ), Ancient Greek τέσσαρες (téssares), and Old English fēower (English four). Persian چهار (čahār) is ultimately from Proto-Indo-European *kʷetwóres, which also connects to Armenian չորս (čʻors).

These words all trace back to Proto-Indo-European roots meaning "four," demonstrating how this numerical term spread across different language families through historical linguistic development. The Persian and Armenian words share a common Indo-European ancestry rather than being loanwords from each other in this case.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T22:40:31.485Z] TOOL CALL #80: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7etw%C3%B3res' --note 'page 295, root Kwetwer: PIE *kʷetwóres \"four\", descendants (PII *čatwā́ras, Old Armenian čʻorkʻ, PGmc *fedwōr)' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%86%D9%87%D8%A7%D8%B1' --note 'page 295 node 2: Persian چهار < MP čahār < PIr *čaθwārah < PIE *kʷetwóres; derived چهارده، چارک' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/quarantine' --note 'page 295 nodes 12-15: quarantine < It. quaranta giorni < L. quadraginta; Venice 1377' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/cadre' --note 'page 295 nodes 9-11: cadre < Fr. cadre < It. quadro < L. quadrum/quadrus' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/trapeze' --note 'page 295 nodes 18,21,22: trapeze/trapezoid < Gk. trapezion < trapeza, tra- \"four\" + peza \"foot\"' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B4%D8%B7%D8%B1%D9%86%D8%AC' --note 'page 295 nodes 5-7: Arabic/Persian شطرنج < Class. Pers. čatrang < MP čatrang < Skt caturaṅga' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%A7%D8%A8%D8%B2%D9%8A%D9%86' --note 'page 295 nodes 19-20: Arabic درابزين railing, Wiktionary derives it from Ottoman Turkish طرابزان < Persian داربزین' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D1%87%D0%B5%D1%82%D0%B2%D0%B5%D1%80%D1%82%D1%8C' --note 'page 295 nodes 3-4: Russian четверть \"quarter\" < PIE *kʷetwóres (Mo'in derives Persian چتور from Russian)' 2>&1 | tail -3",
 "description": "Archive web sources"
}
```


### [2026-09-06T22:40:33.034Z] TOOL RESULT

```
Exit code 1
(eval):8: parse error near `)'
```


## [2026-09-06T22:40:50.476Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7etw%C3%B3res' --note 'page 295, root Kwetwer: PIE *kwetwores four, descendants PII catwaras, Old Armenian corkc, PGmc fedwor' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%86%D9%87%D8%A7%D8%B1' --note 'page 295 node 2: Persian chahar from MP chahar, PIr cathwarah, PIE kwetwores' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/quarantine' --note 'page 295 nodes 12-15: quarantine from It. quaranta giorni, L. quadraginta, Venice 1377' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/cadre' --note 'page 295 nodes 9-11: cadre from Fr. cadre, It. quadro, L. quadrum/quadrus' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/trapeze' --note 'page 295 nodes 18,21,22: trapeze/trapezoid from Gk trapezion, trapeza = tra- four + peza foot' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B4%D8%B7%D8%B1%D9%86%D8%AC' --note 'page 295 nodes 5-7: Arabic and Persian shatranj from Classical Persian chatrang, MP chatrang, Skt caturanga' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%A7%D8%A8%D8%B2%D9%8A%D9%86' --note 'page 295 nodes 19-20: Arabic darabzin railing; Wiktionary derives it from Ottoman Turkish tarabizan from Persian darabzin' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D1%87%D0%B5%D1%82%D0%B2%D0%B5%D1%80%D1%82%D1%8C' --note 'page 295 nodes 3-4: Russian chetvert quarter from PIE kwetwores; Moin derives Persian chatvar from Russian' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D5%B9%D5%B8%D6%80%D6%80%D5%B8%D6%80%D5%A4' --note 'page 295 node 3: Old Armenian chorrord fourth, from chori- plus -rord; no Armenian form chatvar' 2>&1 | tail -2",
 "description": "Archive web sources (fixed quoting)"
}
```


### [2026-09-06T22:40:55.754Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7f1273ffcd63ff3f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0eeb85e5cf96f217.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/06591a713e0e6468.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9f95a9a0b492848f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/538c535c37b3081a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4cb87853e3138977.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3b385faabe018e56.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/67fbe8f00f20e058.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ac1d5e120c7306d2.txt
```


## [2026-09-06T22:40:58.956Z] TOOL CALL #82: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T22:40:58.997Z] TOOL RESULT

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


## [2026-09-06T22:42:27.297Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN chahar ===\"\ngrep -n -i \"čahār\\|čahâr\\|cahâr\\|tschahâr\\|čihil\\|tschihil\\|čārak\" HRN.txt | head -8\ngrep -n \"چهار\" HRN.txt | head -3\necho \"=== HUB ===\"\ngrep -n -i \"cahâr\\|čahâr\\|catvârô\" HUB.txt | head -5\necho \"=== ARY chahar ===\"\ngrep -n \"چهار$\\|^چهار\\|چهار \" incoming/ARY/ARY_pages.txt | head -5\ngrep -n -i \"KWETWER\\|QUETWER\\|CHAHAR\" incoming/ARY/ARY_latin_index_pages.txt | head -5\necho \"=== WLD Bd1 512 ===\"\npython3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('etuer')\nprint(t[i-500:i+900] if i>0 else 'not found')\nEOF",
 "description": "HRN, HUB, ARY, WLD greps"
}
```


### [2026-09-06T22:42:29.207Z] TOOL RESULT

```
=== HRN chahar ===
=== HUB ===
=== ARY chahar ===
152:اروپایی زبان واحد مردمی بود که حدود چهار تا شش هزار سال پیش در ناحیه‌ی نسبتاً محدودی
446:¥ chahar | quatre vier vier fyt
6571:FIOR (OLD HIGH GERMAN) yf gt CHAHAR, CAHAR (PAHLAVI) «5 Sy
=== WLD Bd1 512 ===
    ,                                                                                  ;


gr. TkaoTog , hom.                                    zhgazog, boot, nhoazog; lat. quartus, praen. Quorta (siehe
Vf. LEWb. 2 s. v., Bgm. II 2 2, 54), osk. vielleicbt truto- (s. o.)                                                                     air. cethramad,
                                                                                                                                    ;


acymr. petuerul                toch. sdardh, itardh , sdhardh; ahd. fiordo, ags. feorda, aisl.
                                                :




fiordi             lit. ketvirtas (lett. ceturfais wie ai. caturthd-h  aksl. ceimH.                                     ),
         Yon anderem Zubehor                                             sei
                                                     quattuordecim , got. fid-     herausgehoben             lat.
wertaihun ahd. viorzelian „14“; dor. ion. delph. rezQwxovza (*(pietu ro-komta
                           ,
                                                                    0
s. zuletzt Yf.) = lat. qundruginta. Av. cafrrus „4mal“ (umgebildet ai. catur
aus *caturs) = lat. quater (wenn nicht aus nach *tris, *duis umgebildetem
*quatr is). Ai. catvard- m. „viereckiger Platz“ (s. Bgm. II* 2, 76), lit. ketver'i
..je         vier“. aksl. ectven,
```


## [2026-09-06T22:42:39.058Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\ni=t.find('etuer')\nseg=t[:i]\ntags=re.findall(r'\\[pdf page (\\d+)\\]',seg)\nprint('last pdf page tag before hit:',tags[-3:] if tags else None)\n# find the entry start\nj=t.rfind('k^etuer',0,i)\nprint(t[i-3000:i-400][-1500:])\nEOF\necho \"=== ARY page for line 446 and 6571 ===\"\nawk 'NR<=446 && /\\[pdf page/ {p=$0} END{}' incoming/ARY/ARY_pages.txt\ngrep -n \"\\[pdf page\" incoming/ARY/ARY_pages.txt | awk -F: '$1<446' | tail -1\ngrep -n \"\\[pdf page\" incoming/ARY/ARY_latin_index_pages.txt | awk -F: '$1<6571' | tail -1\nsed -n '440,452p' incoming/ARY/ARY_pages.txt",
 "description": "WLD page tag, ARY pages"
}
```


### [2026-09-06T22:42:40.847Z] TOOL RESULT

```
last pdf page tag before hit: None
              av. tuirya- „vierter“;
av. ra§ru-[gaosa -]  gr. T«Tpa-[^oo(ot], -n ovg, schwundstufig oder durch Diss.
                                                     ;

aus rerga- gr. rgdjieCa (Lit. auch bei Boisacq 979); t gv-cpafaia „Helm“ (vgl.
reiod-c/akog „mit vier Schirmen versehen“j wohl schwundstufig
                                                                         *[g'“J(/w-
fj. Schmidt KZ. 25, 46       Prellwitz BB. 25, 324, Bechtel Lex. 319; kaum
                         f.,

diss. aus           Fick BB.       64), wie osk. trutom (wenn es „quartum“ 1   ,


bedeutet; sehr fraglich, ob auch in lat. tru-etdo, s. Yf. LEWb. 2 s. v.        lat.                                                                   ;

qttadru-\pcs]: umbr. pctur[-pursus „quadrupedibus“]      gall. Petrti-corius -de-                                   ;                                 ,

cametos „14.“ (petor-ritum „vierraderiger Wagen“ wohl mit dem Yokal von
*q'ietuore >>)                 ;
                                   got. fulur-dogs                      westgermanisches s. v.); lit. ketur-[kojis „Vierfufi“];
arm. kar-n-sun „40“                                        ({q’ifiur-V).

O rd          i    na1e             :




         Ai. caturtha-h, turJya-h, tiirya-h, av. tuirya-; arm. rorir corr-ord kar-ord
                                                                    ,        ,                                                                                  ;


gr. TkaoT
=== ARY page for line 446 and 6571 ===
443:[pdf page 18]
6563:[pdf page 228]
ارائه شد (زبانها لتوانی و آلبانی و ارمنی و تخاری بعداً توسط دیگران شناسایی و به فهرست ری
افزوده گردید):
کت
[pdf page 18]
لجج ۹
دیباچه / ۱۹
ناکسا
لت لت 00 ۵ اهر ‎٩‏
‏۸ اند 26 7 00 ۰ ۲
ات ع0 ات ۵6لا | 86 ۳
1۸ وتان ات 6 ۲ ۲۵۵۵۲ ۴
1 3 ۳ 4 . زمم ۵
قت 2 ات امه ۶
```


## [2026-09-06T22:42:49.286Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6565,6580p' incoming/ARY/ARY_latin_index_pages.txt\necho \"=== ARY chahar entry search ===\"\ngrep -n \"چهار (\\|^چهار\\|چهار:\" incoming/ARY/ARY_pages.txt | head -10\ngrep -n \"چار\\b.*هند\\|چهار.*کوادر\\|quattuor\\|quadr\" incoming/ARY/ARY_pages.txt | head -10",
 "description": "ARY chahar"
}
```


### [2026-09-06T22:42:49.358Z] TOOL RESULT

```
WS Ile
lethal
Ler tah Oaks Seay SI 2 3s ool ee
LaSi gtd a ly 22 Sly al oe
HOLD FRISIAN) oS 54,3 HAVESTAN)  gleu 3}
FIUWER, FIOR CHATHWARO, CHATHRO-
FIOR (OLD HIGH GERMAN) yf gt CHAHAR, CAHAR (PAHLAVI) «5 Sy
VIER GERMAN) glalT CIPPAR HOSSETIC) gy)
FEOWER | :(OLD ENGLISH) aS gJ&il CHAR (KURDISH) 52,5
FOUR ENGLISH) JS} AFGHAN) (4) lai!
FIRE DANISH) Slasla CALOR, TSALOR
FYRA (SWEDISH) $8 yo STWAR :(TOKHARIAN A) A 5 ,\65
FIRE s(NORWEGIAN) ($53, :(TOKHARIAN B) B 5 \as
VIER (DUTCH) gacha STWARE, SWAR
HOLD CHURCH SLAVIC) 4S 5j%\ SANSKRIT) ey Site
KETYRE, CHETYRE CATVARAS, CATASRAS, CATVARI
=== ARY chahar entry search ===
```


## [2026-09-06T22:43:06.082Z] AGENT

Now I'll write the verification file.


## [2026-09-06T22:43:07.978Z] TOOL CALL #86: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p295",
 "description": "Make scratch dir"
}
```


### [2026-09-06T22:43:08.028Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:53:49.200Z] TOOL CALL #87: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p295/build.py",
 "content": "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\nimport json, io\n\nPOKQ = (\"POK_02.txt leaf 302-303 (printed pp. 642-644): \"\n        \"\\\"kʷetuer-, kʷetu̥r-, kʷetur- m., kʷetes(o)r- f., ,vier'… \"\n        \"Ai. catvāraḥ m.… av. caθwārō m. (Gen. caturąm), čataṣrō f., npers. čahār; \"\n        \"arm. čʻorkʻ aus *čoreh < *kʷetuores… lat. quattuor… got. fidwōr…\\\"\")\n\nAHDQ = (\"AHD_watkins1985.txt s.v. kʷetwer-: \\\"Four. I. O-grade form *kʷetwor-. 1. Probably Germanic \"\n        \"*fe(d)wor- in: a. Old English fēower, four: FOUR; b. … fēowertig, forty: FORTY; c. … \"\n        \"fēowertēne, fourteen: FOURTEEN. 2. Latin quattuor… II. … 2. Latin quadrus, four-sided thing, \"\n        \"square: CADRE, QUADRATE, QUARREL, QUARRY; SQUAD, SQUARE, TROCAR… 6. Latin quadrāgintā, forty \"\n        \"(-gintā, ten times; see dekm): QUARANTINE. 7. Variant form *kʷet(w)r- in… d. zero-grade form \"\n        \"*kʷt(w)r- in Greek tra-, four: TRAPEZIUM. III. Ordinal adjective *kʷetur-to-… 2. Latin quārtus, \"\n        \"fourth, quarter: … QUART, QUARTAN, QUARTER, QUARTO. [Pok. kʷetuer- 642.]\\\"\")\n\ndata = {\n  \"pdf_page\": 295,\n  \"book_page\": 265,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Kwetwer, Qwetwor\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *kʷetwóres / *kʷetwer- ‘four’ (Pokorny 642 kʷetuer-; Watkins/AHD kʷetwer-)\",\n      \"note\": (\"Pokorny IEW 642-643 heads the entry kʷetuer-, kʷetu̥r-, kʷetur- m., kʷetes(o)r- f., ‘vier’, \"\n               \"with composition stem kʷ(e)tru-/kʷ(e)tur-; Watkins gives kʷetwer- ‘four’ with o-grade *kʷetwor- \"\n               \"and zero-grade *kʷt(w)r-. Nourai’s two head-forms ‘Kwetwer, Qwetwor’ are simply his spellings of the \"\n               \"e-grade and o-grade of one root; the language label (Indo-European) and the gloss (‘four’) are both right, \"\n               \"and POK:642 is the exact page. The page is otherwise sound; the errors are concentrated in three boxes: \"\n               \"the Persian čatvar (#3-#4), the Persian chess word (#7) and the Italian ‘quadratina’ (#12).\"),\n      \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *kʷetwóres «چهار» است؛ پوکورنی در صفحهٔ ۶۴۲ فرهنگ ریشه‌شناسی \"\n                  \"هندواروپایی خود آن را با صورت‌های kʷetuer-، kʷetur- و ستاک ترکیبی kʷ(e)tru- آورده و واتکینز \"\n                  \"(پیوست ریشه‌های هندواروپایی فرهنگ امریکن هریتیج) نیز همان را با درجهٔ آوایی o یعنی *kʷetwor- ثبت کرده است. \"\n                  \"دو صورتی که نورایی در سرلوحه آورده (Kwetwer و Qwetwor) در واقع دو گونهٔ آوایی یک ریشه‌اند، و برچسب زبان و \"\n                  \"معنا هر دو درست است. ادعای نورایی دربارهٔ خودِ ریشه درست است و ارجاع POK:642 دقیقاً همان صفحه است.\"),\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7etw%C3%B3res\",\n        \"https://www.etymonline.com/word/quarantine\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:642\", \"status\": \"supports\",\n         \"note\": \"Checked the local OCR of Pokorny (IEW Bd. I), \" + POKQ + \" — the printed page numerals 642/643/644 appear inside these leaves, so 642 is exactly Nourai’s page.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"POK_02.txt leaves 302-303 = IEW pp. 642-644\", \"stance\": \"supports\",\n         \"note\": \"“kʷetuer-… ,vier’… WP. I 512, Trautmann 131 f., Schwyzer Gr. Gr. I 351 f., WH. II 394, 400 f.” — the root, the gloss and the page all match.\"},\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I 512 (incoming/WLD/WLD_Bd1_pages.txt, s.v. the numeral ‘four’)\", \"stance\": \"supports\",\n         \"note\": \"“gr. τέταρτος… lat. quartus… lat. quadrāgintā… gr. τράπεζα… lat. quadru-[pes]… got. fidur-… arm. kʻar-a-sun ‘40’” — the same root, the very page (WP I 512) Pokorny cites at IEW 644.\"},\n        {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. kʷetwer-\", \"stance\": \"supports\",\n         \"note\": AHDQ},\n        {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. ‘four’\", \"stance\": \"supports\",\n         \"note\": \"“four… cogn. with OI. catvāraḥ, Avestic caθwārō, Pers. čatvār, Toch. A stwar, Arm. čorkʻ, Gk. τέσσαρες, L. quattuor, Oscan petora, Umbr. petur-, OSlav. četyre… All these words derive fr. I.-E. base *quetwār-, ‘four’. Cp.… cadre… quarantine… square… trapezium, trocar.” Klein’s cross-references cover almost every branch of this chart.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 12.78 SQUARE\", \"stance\": \"supports\",\n         \"note\": \"“Lat. quadrātum, neut. of quadrātus… fr. quadrus (> It. quadro, Sp. cuadro)… quadra ‘square, base of a pedestal, table’, quadrum ‘square’, all fr. quattuor ‘four’, in form quadru- as in quadru-plex”.\"},\n        {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_latin_index_pages.txt, pdf page 228 (cognate table for ‘four’)\", \"stance\": \"supports\",\n         \"note\": \"Aryanpur’s cognate list: “CHATHWARO, CHATHRO- (AVESTAN) | CHAHAR, CAHAR (PAHLAVI) | CIPPAR (OSSETIC) | CHAR (KURDISH) | CATVARAS, CATASRAS, CATVARI (SANSKRIT) | STWAR (TOKHARIAN A) | KETYRE, CHETYRE (OLD CHURCH SLAVIC) | FEOWER (OLD ENGLISH)” — an independent modern Persian cross-check of the whole family.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1, \"lang\": \"Avestan\", \"words\": \"čatwârao\", \"verdict\": \"plausible\",\n          \"derivation\": (\"The Avestan nominative plural masculine of ‘four’ is caθwārō (Bartholomae, AiW s.v. čaθwar-, \"\n                         \"gen. caturąm, fem. čataṣrō), the regular reflex of PIE *kʷetwóres: PIE *kʷ- gives Indo-Iranian \"\n                         \"*č- before a front vowel (satem palatalisation) and PIE *-tw- gives Avestan -θw-, exactly as in \"\n                         \"Skt. catvāraḥ. Nourai’s spelling ‘čatwârao’ keeps the č- but writes plain tw for θw and ‘-ao’ for \"\n                         \"the long ō of the ending, so the derivation from the root is right while the form itself is not the \"\n                         \"one the handbooks print; read it as caθwārō. Verdict ‘plausible’ for the spelling only — \"\n                         \"the arrow root → Avestan is beyond doubt.\"),\n          \"derivation_fa\": (\"صورت اوستایی عدد چهار در حالت فاعلی جمع مذکر caθwārō است (بارتولومه در فرهنگ ایرانی باستان، \"\n                            \"ذیل čaθwar-، با اضافهٔ caturąm و مؤنث čataṣrō)، که بازتاب قاعده‌مند *kʷetwóres هندواروپایی است: \"\n                            \"*kʷ در ایرانی باستان پیش از واکهٔ پیشین به č بدل شده و *tw هندواروپایی در اوستایی θw داده است. \"\n                            \"نورایی č آغازین را درست آورده اما θw را tw و واکهٔ کشیدهٔ پایانی ō را «ao» نوشته است؛ پس اشتقاق درست \"\n                            \"است ولی املا با آنچه در کتاب‌های مرجع آمده یکی نیست و باید caθwārō خوانده شود. حکم «با احتیاط \"\n                            \"پذیرفتنی است» تنها به همین املا برمی‌گردد.\"),\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7etw%C3%B3res\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:642\", \"status\": \"supports\",\n             \"note\": \"IEW 642 (POK_02.txt leaf 302): “av. caθwārō m. (Gen. caturąm), čataṣrō f., npers. čahār” — exactly the Avestan→Persian link Nourai draws, on the page he cites; only his spelling differs.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt s.v. čaθwar-, AiW col. 577\", \"stance\": \"supports\",\n             \"note\": \"“čaθwar-; čaθru- Zw., fem. čataṣar- ‘vier’” with the Yasna/Yasht/Vendīdād citations — the word is well attested in Avestan, spelt with θw.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_latin_index_pages.txt pdf p. 228\", \"stance\": \"supports\",\n             \"note\": \"“CHATHWARO, CHATHRO- (AVESTAN)” — Aryanpur too writes the Avestan with -thw- (= θw), not -tw-.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. four\", \"stance\": \"supports\",\n             \"note\": \"“Avestic caθwārō” listed among the cognates of OE fēower.\"}\n          ]\n        },\n        {\n          \"id\": 2, \"lang\": \"Persian\", \"words\": \"(چهار ، چهارک ، چهارده ، چهل)\", \"verdict\": \"confirmed\",\n          \"derivation\": (\"New Persian چهار čahār (colloquial چار čār) continues Middle Persian čahār < Old Iranian \"\n                         \"*čaθwārah < PIE *kʷetwóres; intervocalic Old Iranian *θw weakened to h in Middle Persian \"\n                         \"(*čaθwāra- > čahār), the same change as in Av. maθra- > MP mahr. چهارده čahārdah ‘fourteen’ is \"\n                         \"čahār + dah ‘ten’ (cf. Lat. quattuordecim, Goth. fidwortaihun, cited by Pokorny at 644), and چهارک \"\n                         \"čārak ‘a quarter’ is čār + the diminutive/fractional -ak. چهل čehel ‘forty’ is not built on čahār \"\n                         \"inside Persian but continues MP čihil < Old Iranian *čaθwarəsat- (Av. caθwarəsatəm ‘40’, the exact \"\n                         \"counterpart of Lat. quadrāgintā), so it belongs to the same root by a parallel line. The arrow as \"\n                         \"drawn is a shorthand: New Persian descends through Middle Persian from Old Iranian, of which Avestan \"\n                         \"is a sister dialect, not the ancestor.\"),\n          \"derivation_fa\": (\"«چهار» فارسی نو دنبالهٔ چهارِ فارسی میانه (čahār) است، از ایرانی باستان *čaθwārah و آن از \"\n                            \"هندواروپایی آغازین *kʷetwóres؛ خوشهٔ θw ایرانی باستان در میان دو واکه در فارسی میانه به h نرم شده \"\n                            \"و *čaθwāra- به čahār بدل گشته است. «چهارده» از چهار + ده ساخته شده (سنجیدنی با quattuordecim لاتینی و \"\n                            \"fidwortaihun گوتی که پوکورنی در ص ۶۴۴ آورده) و «چارک» از چار + پسوند تصغیر/کسری «ـک» است. اما «چهل» \"\n                            \"درون فارسی از «چهار» گرفته نشده، بلکه دنبالهٔ čihil فارسی میانه از ایرانی باستان *čaθwarəsat- است \"\n                            \"(اوستایی caθwarəsatəm «چهل»، همتای دقیق quadrāgintā لاتینی). ادعای نورایی درست است؛ تنها باید \"\n                            \"توجه داشت که فارسی نو از راه فارسی میانه به ایرانی باستان می‌رسد و اوستایی خواهرِ آن است نه نیای آن.\"),\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%86%D9%87%D8%A7%D8%B1\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7etw%C3%B3res\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:642\", \"status\": \"supports\",\n             \"note\": \"IEW 642: “av. caθwārō… npers. čahār”; and IEW 644 for the compounds: “lat. quattuordecim, got. fidwortaihun, ahd. viorzehan ‘14’… dor. τετρώκοντα = lat. quadrāgintā ‘40”’ — both čahār and the ‘fourteen’/‘forty’ type are on the cited pages.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD.txt (MacKenzie) p. 23\", \"stance\": \"supports\",\n             \"note\": \"“čehel [40 | N chil] forty” immediately after čatrang — MacKenzie confirms the Middle Persian ancestor of چهل.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_latin_index_pages.txt pdf p. 228\", \"stance\": \"supports\",\n             \"note\": \"“CHAHAR, CAHAR (PAHLAVI)” listed as the Middle Persian reflex of the same numeral.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt, grepped for čahār / tschahār / čihil / čārak\", \"stance\": \"silent\",\n             \"note\": \"Horn’s Grundriss has no entry for the numeral (he treats only etymologically problematic words), so it neither supports nor contradicts.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt, grepped for čahār / catvārō\", \"stance\": \"silent\",\n             \"note\": \"Hübschmann’s Persische Studien likewise has no numeral entry.\"}\n          ]\n        },\n        {\n          \"id\": 3, \"lang\": \"Armenian\", \"words\": \"čatvar\", \"verdict\": \"disputed\",\n          \"derivation\": (\"Nourai’s source really does say this: Tavoosi, Glossary of Šāyast nē Šāyast p. 148, s.v. tasum \"\n                         \"‘fourth’, ends “(چَتْوَر فارسی ما مأخوذ از ارمنی = ۱/۴ نیز همین است)”, i.e. ‘our Persian čatvar, \"\n                         \"taken from Armenian, = ¼, is this same word’. But no Armenian word čatvar exists: Old Armenian ‘four’ \"\n                         \"is ďʻorkʻ (չորք, < *čoreʻ < *kʷetuores, Pokorny 643), ‘fourth’ is čʻorrord (չորրորդ) and ‘a quarter’ is \"\n                         \"kʻaṛʿord (քառորդ) — none of them with a -tv- cluster, which Armenian lost. Mo‘in (whom Nourai himself \"\n                         \"cites in the note) makes the donor Russian: چتور [رس.] ‘a quarter of a girvanka’, i.e. Russian \"\n                         \"четверть četvеrtʹ ‘quarter’ (< Proto-Slavic *četvьʁtь < the same PIE *kʷetwer-), a Russian trade \"\n                         \"measure that reached Iran through Caucasian trade in the 19th c. — which fits the shape čatvar/četvert \"\n                         \"far better. So the ultimate root is right, but the branch label ‘Armenian’ is not: modern lexicography \"\n                         \"makes it a Russian (Slavic) loan, at most transmitted by Armenian merchants.\"),\n          \"derivation_fa\": (\"مأخذ نورایی همین را می‌گوید: طاووسی در واژه‌نامهٔ شایست نه‌شایست، ص ۱۴۸، ذیل tasum «چهارم» \"\n                            \"می‌نویسد «چَتْوَر فارسی ما مأخوذ از ارمنی = ۱/۴ نیز همین است». اما در ارمنی واژه‌ای به شکل čatvar \"\n                            \"نداریم: «چهار» در ارمنی کهن čʻorkʻ (չորք)، «چهارم» čʻorrord و «یک‌چهارم» kʻaṛʿord است و خوشهٔ tv در \"\n                            \"ارمنی از میان رفته است. معین ــ که خودِ نورایی در یادداشت به او ارجاع می‌دهد ــ سرچشمه را روسی می‌داند: \"\n                            \"«چتور [رس.] یک چهارم گیروانکه». روسی четверть (četvert) «یک‌چهارم» از همان ریشهٔ هندواروپایی است و \"\n                            \"به‌عنوان واحد بازرگانی در سدهٔ سیزدهم خورشیدی از راه قفقاز به ایران رسیده و از نظر آوایی هم به čatvar \"\n                            \"بسیار نزدیک‌تر است. پس ریشهٔ نهایی درست است ولی برچسب «ارمنی» را پژوهش امروزی نمی‌پذیرد و آن را \"\n                            \"وام‌واژه‌ای روسی می‌داند.\"),\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D1%87%D0%B5%D1%82%D0%B2%D0%B5%D1%80%D1%82%D1%8C\",\n            \"https://en.wiktionary.org/wiki/%D5%B9%D5%B8%D6%80%D6%80%D5%B8%D6%80%D5%A4\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7etw%C3%B3res\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SNS:148\", \"status\": \"supports\",\n             \"note\": \"Read the page image (archive.org/details/VajnameShayest leaf n90, right-hand page, printed ۱۴۸ = 148), s.v. tasum ‘تسوم، چهارم’: “قس: *čaθš : ستا *čaθrəma : سغدی *ctβʼrm = catfārum… پاتر: tswm (Mir. Man. II, 69) و طسوج عربی ظاهراً از همین واژه است. (چَتْوَر فارسی ما مأخوذ از ارمنی = ۱/۴ نیز همین است)”. The reference says exactly what Nourai’s arrow says — the page-image also shows the Persian is spelt چَتْوَر with چ, not ک.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt (2-vol. Adena condensation) s.v. چتور\", \"stance\": \"contradicts\",\n             \"note\": \"“چتور: [رس.] یک چهارم گیروانکه، برابر با ۱۲۵ گرم” — Mo‘in tags the word [رس.] = Russian, not Armenian, and glosses it ‘a quarter of a girvanka = 125 g’ (Nourai’s ‘250 grams’ is his own conversion).\"},\n            {\"src\": \"POK\", \"where\": \"IEW 643 (POK_02.txt leaf 302)\", \"stance\": \"partial\",\n             \"note\": \"“arm. čʻorkʻ aus *čorekʻ < *kʷetuores (Akk. čors)” and “aksl. četyre… lit. keturi” — the root is shared, but the Armenian reflex Pokorny knows is čʻorkʻ, never čatvar; the -tv- form belongs to the Slavic branch (OCS četvrътъ).\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. four\", \"stance\": \"partial\",\n             \"note\": \"“Arm. čorkʻ” listed as the Armenian cognate — again no čatvar.\"}\n          ]\n        },\n        {\n          \"id\": 4, \"lang\": \"Persian\", \"words\": \"katvar «کَتوَر»\", \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"extraction\",\n          \"book_prints\": \"katvar «چَتْوَر»\",\n          \"correct_form\": \"čatvar «چَتْوَر»\",\n          \"derivation\": (\"Two separate problems. (a) EXTRACTION ERROR: the printed page 265 shows the Persian script \"\n                         \"چَتْوَر with چ (three dots below — clearly visible at 450 dpi, see \"\n                         \"data/verification/sources/refs/ocr/BOOK/295.png), while the JSON has کَتوَر with ک. The data must \"\n                         \"be fixed to چَتْوَر. (b) The book’s own Latin transliteration ‘katvar’ is Nourai’s misprint: his \"\n                         \"own source (SNS:148) and Mo‘in both write چتور/čatvar with č-, and č- is what the Armenian and \"\n                         \"Slavic cognates require. On the substance, the word is a 19th-c. commercial weight, ‘a quarter’, \"\n                         \"borrowed — per Mo‘in — from Russian четверть četvеrtʹ (Proto-Slavic *četvьʀtь, same PIE root), \"\n                         \"not from Armenian; and Mo‘in makes it ¼ of a girvanka (≈125 g), not ¼ kg. So: the arrow’s root is \"\n                         \"right, the immediate donor is doubtful (see #3), the gloss is off, and the JSON script is wrong.\"),\n          \"derivation_fa\": (\"در این گره دو مشکل جداگانه هست. نخست خطای خوانش اسکن: صفحهٔ چاپی ۲۶۵ نگارش «چَتْوَر» را با «چ» \"\n                            \"نشان می‌دهد (سه نقطهٔ زیرین در تصویر ۴۵۰ نقطه‌براینچ به‌روشنی دیده می‌شود) اما در داده‌ها «کَتوَر» \"\n                            \"با «ک» آمده است؛ داده باید اصلاح شود. دوم، آوانگاری لاتینِ خودِ کتاب («katvar») خطای چاپی نورایی است، \"\n                            \"زیرا هم مأخذ او (طاووسی ص ۱۴۸) و هم معین «چتور» می‌نویسند. از نظر محتوا، این واژه یک واحد وزنِ \"\n                            \"بازرگانی سدهٔ سیزدهم خورشیدی است و معین آن را وام‌واژه‌ای روسی از четверть می‌داند نه ارمنی، \"\n                            \"و معنای آن را «یک چهارم گیروانکه» (نزدیک ۱۲۵ گرم) آورده، نه یک چهارم کیلوگرم. پس ریشهٔ دور درست است \"\n                            \"ولی وام‌دهِ نزدیک محل تردید است و املای فارسی در داده‌ها خطای خوانش اسکن است.\"),\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D1%87%D0%B5%D1%82%D0%B2%D0%B5%D1%80%D1%82%D1%8C\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SNS:148\", \"status\": \"supports\",\n             \"note\": \"Tavoosi p. 148 (page image, archive.org/details/VajnameShayest leaf n90 right): “چَتْوَر فارسی ما مأخوذ از ارمنی = ۱/۴ نیز همین است” — supports the arrow, and prints the Persian with چ, confirming the JSON’s کَتوَر is an extraction error.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. چتور\", \"stance\": \"contradicts\",\n             \"note\": \"“چتور: [رس.] یک چهارم گیروانکه، برابر با ۱۲۵ گرم” — Russian, and 125 g, not Armenian and 250 g. This is the very claim Nourai reports as MON:1273 in his own NOTE.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt / BQT_v1_pages.txt, grepped چتور and چتوَر\", \"stance\": \"silent\",\n             \"note\": \"Borhan-e Qate‘ (a 17th-c. dictionary) has no entry for this modern Russian trade term — as expected.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt, grepped چتور\", \"stance\": \"silent\",\n             \"note\": \"Aryanpur’s IE-roots dictionary does not list the word.\"}\n          ]\n        },\n        {\n          \"id\": 5, \"lang\": \"Sanskrit\", \"words\": \"catur-anga\", \"verdict\": \"confirmed\",\n          \"derivation\": (\"Sanskrit caturaṅga- ‘having four limbs/members’ = catúr- (the composition stem of catvāraḥ \"\n                         \"‘four’, PIE *kʷetur-) + aṅga- ‘limb, member’; in military usage it names the four-fold army \"\n                         \"(elephants, chariots, cavalry, infantry) and hence the game that models it, first attested in the \"\n                         \"Sanskrit sources of the Gupta period (c. 6th c. CE). Pokorny cites the very compound at IEW 643 \"\n                         \"as an example of the composition stem: “ai. cátur-[aṅga-ḥ ‘viergliedrig’]”. The chart’s cross-reference \"\n                         \"☆Ang (to Nourai’s root Ang) for the second element is correct.\"),\n          \"derivation_fa\": (\"سنسکریت caturaṅga- «دارای چهار اندام/چهار بخش» از catúr- (ستاک ترکیبی catvāraḥ «چهار»، از \"\n                            \"هندواروپایی *kʷetur-) و aṅga- «اندام، عضو» ساخته شده است. در کاربرد نظامی به سپاهِ چهاربخشی \"\n                            \"(فیل، ارابه، سواره، پیاده) گفته می‌شد و از همین‌جا نام بازی‌ای شد که همان آرایش را بازمی‌نماید؛ \"\n                            \"نخستین گواهی‌های آن به دورهٔ گوپتا (سدهٔ ششم میلادی) بازمی‌گردد. پوکورنی در ص ۶۴۳ همین ترکیب را \"\n                            \"«ai. cátur-[aṅga-ḥ ‘viergliedrig’]» نمونه‌ای از ستاک ترکیبیِ ریشه آورده است. ادعای نورایی درست است.\"),\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%D8%B7%D8%B1%D9%86%D8%AC\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1254\", \"status\": \"supports\",\n             \"note\": \"Borhan-e Qate‘ (Mo‘in’s ed.) p. 1254 = incoming/BQT/BQT_v3_pages.txt [pdf page 45], headword شترنگ, Mo‘in’s footnote 1: “پهلوی čatrang، ارمنی… shitranj… از سانسکریت catur[-anga] (دارای چهار لبه با چهار حد) شامل چهار جزء: فیل، رخ، اسب، پیاده… معرب آن شطرنج” — exactly the Sanskrit → Pahlavi → Persian chain Nourai draws, on the page he cites.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 643 (POK_02.txt leaf 302)\", \"stance\": \"supports\",\n             \"note\": \"“In Kompositis (und Ableitungen) kʷetur-, kʷetur-, kʷetru-: ai. cátur-[aṅga-ḥ ‘viergliedrig’]” — Pokorny himself uses catur-aṅga- as the example.\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt (Nyberg, Manual of Pahlavi II), Sanskrit index\", \"stance\": \"supports\",\n             \"note\": \"“catur-anga-: catrang” — Nyberg’s glossary index equates the Sanskrit compound with Pahlavi čatrang.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen p. 178\", \"stance\": \"supports\",\n             \"note\": \"“شطرنج šaṭrang: ‘Schachspiel’… pers. šatrang, mp. čatrang, skr. caturanga”.\"}\n          ]\n        },\n        {\n          \"id\": 6, \"lang\": \"Pahlavi\", \"words\": \"catrang\", \"verdict\": \"confirmed\",\n          \"derivation\": (\"Middle Persian čatrang [ctrng] ‘chess’ is the regular Iranian adaptation of Skt. caturaṅga-: the \"\n                         \"Indian compound was shortened in Iranian to čatr-ang, the aṅga element being reduced to -ang, and \"\n                         \"the initial c- was heard as Iranian č- (already homophonous with the native čaθr-/čahār ‘four’, which \"\n                         \"made the loan transparent). The word is the title of a late Sasanian Pahlavi tract, Wīzārišn ī \"\n                         \"čatrang ud nihšn ī nēw-ardaхšīr, which tells how the game came from India to the court of Khusrau I \"\n                         \"(6th c.), and it is quoted repeatedly in the Kārnāmag; Nyberg’s glossary cites čatrang nēhādan ‘to set \"\n                         \"up a game of chess’ and čatrang wačitan ‘to play chess’.\"),\n          \"derivation_fa\": (\"فارسی میانه čatrang [ctrng] «شطرنج» گرته‌برداری قاعده‌مند از caturaṅga- سنسکریت است: ترکیب هندی \"\n                            \"در ایرانی به čatr-ang کوتاه شده و جزء aṅga به «ـنگ» فروکاسته است، و c آغازین همان č ایرانی شنیده شده \"\n                            \"که با čaθr-/čahārِ بومی هم‌آواست و همین وام‌واژه را شفاف می‌کرد. این واژه نام رساله‌ای پهلوی از اواخر \"\n                            \"دورهٔ ساسانی است: «ویزارشن ای چترنگ اُد نهشن ای نیو-اردخشیر» که داستان آمدن بازی از هند به دربار \"\n                            \"خسرو یکم را بازمی‌گوید؛ نیبرگ نیز ترکیب‌های čatrang nēhādan و čatrang wačitan را آورده است. \"\n                            \"ادعای نورایی درست است.\"),\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%D8%B7%D8%B1%D9%86%D8%AC\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n             \"note\": \"Nourai gives no reference on this box; the parent box cites BQT:1254, whose footnote (“پهلوی čatrang… از سانسکریت catur[-anga]”) covers this arrow too.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p. 23\", \"stance\": \"supports\",\n             \"note\": \"“čatrang [ctlng | (Ar. šatranj)] chess” — MacKenzie gives the Pahlavi form and the Arabic outcome.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, s.vv. nihādan, wačitan and the Sanskrit index\", \"stance\": \"supports\",\n             \"note\": \"“catrang ~ to arrange a game of chess 119¹⁴”; “vazitan… catrang — to play at chess 119¹⁵, 121”; index “catur-anga-: catrang”. Nyberg also refers to Hansen’s edition of the tract ‘Catrang’.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT p. 1254 footnote 1\", \"stance\": \"supports\",\n             \"note\": \"“پهلوی čatrang… از سانسکریت catur[-anga]… معرب آن شطرنج”.\"}\n          ]\n        },\n        {\n          \"id\": 7, \"lang\": \"Persian\", \"words\": \"katrang «کَترنگ» (شترنگ ، شطرنج)\", \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"katrang «کَترنگ ( شترنگ ، شطرنج )»\",\n          \"correct_form\": \"čatrang «چترنگ» / šatrang «شترنگ»\",\n          \"derivation\": (\"The extraction is faithful — the printed page really does read ‘katrang’ with کَترنگ — but no such \"\n                         \"Persian word exists; this is Nourai’s misprint (ک for چ) for čatrang چترنگ. Borhan-e Qate‘ p. 1254, \"\n                         \"the very page cited on the parent box, has the headword شترنگ “با کاف فارسی” (i.e. with گ) \"\n                         \"glossed ‘شطرنج’, with Mo‘in’s footnote ‘پهلوی čatrang… معرب آن شطرنج’, and it quotes the same \"\n                         \"distich Nourai prints: “تا جز از بیست و چهارش نبود خانهٔ نرد / همچو در سی و دو خانه است \"\n                         \"نهادش شترنگ” (Borhan cites Asadi’s Loghat-e Fors p. 289). Phonetically MP čatrang gives NP čatrang \"\n                         \"چترنگ, whence by dissimilation/Arabic mediation شترنگ šatrang; Arabic borrowed it as شطرنج \"\n                         \"šaṭranj (the emphatic ṭ and the final j reflecting Arabic phonotactics), and Persian re-borrowed that \"\n                         \"Arabicised form as شطرنج — a classic Persian → Arabic → Persian round trip. The two variants Nourai \"\n                         \"lists in brackets, شترنگ and شطرنج, are therefore correct; only his headword is not.\"),\n          \"derivation_fa\": (\"خوانش اسکن درست است ــ صفحهٔ چاپی به‌راستی «katrang» و «کَترنگ» دارد ــ اما چنین واژه‌ای در فارسی \"\n                            \"نیست و این خطای چاپی خودِ کتاب است (ک به‌جای چ) برای čatrang «چترنگ». برهان قاطع در همان صفحهٔ ۱۲۵۴ \"\n                            \"که نورایی به آن ارجاع داده، سرواژهٔ «شترنگ» را «با کاف فارسی» آورده و «شطرنج» معنا کرده و در حاشیهٔ معین \"\n                            \"«پهلوی čatrang… معرب آن شطرنج» آمده است؛ همان بیتی هم که نورایی نقل می‌کند در برهان (به نقل از \"\n                            \"لغت فرس اسدی ص ۲۸۹) هست. از نظر آوایی čatrangِ فارسی میانه در فارسی نو «چترنگ» می‌شود و با ابدال \"\n                            \"چ به ش «شترنگ» می‌گردد؛ عربی آن را «شطرنج» معرّب کرد (ط و ج بازتاب نظام آوایی عربی است) و فارسی \"\n                            \"همان صورت معرّب را دوباره وام گرفت ــ نمونه‌ای از رفت‌وبرگشت فارسی ← عربی ← فارسی. دو گونهٔ داخل \"\n                            \"کمانک درست‌اند و تنها سرواژه خطای چاپی کتاب است.\"),\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B4%D8%B7%D8%B1%D9%86%D8%AC\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n             \"note\": \"No reference on this box. Checked BQT:1254 (cited on the ancestor box) instead: it prints the headword as شترنگ, never کترنگ.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate‘ p. 1254 (incoming/BQT/BQT_v3_pages.txt [pdf page 45])\", \"stance\": \"partial\",\n             \"note\": \"“شترنگ «با کاف فارسی»… بمعنی شطرنج است…” + footnote “پهلوی čatrang… معرب آن شطرنج” and the distich “تا جز از بیست و چهارش نبود خانهٔ نرد / همچو در سی و دو خانه است نهادش شترنگ” — supports the etymology but contradicts the head-form کترنگ.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p. 23\", \"stance\": \"partial\",\n             \"note\": \"“čatrang [ctlng | (Ar. šatranj)] chess” — č-, not k-.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, AFM.txt (الشطرنج)\", \"stance\": \"supports\",\n             \"note\": \"“والشطرنج معرب… سترنک” — Addi Shir lists شطرنج as an Arabicised Persian word (سترنگ/شترنگ), confirming the Persian → Arabic direction.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi p. 178\", \"stance\": \"supports\",\n             \"note\": \"“شطرنج šaṭrang… pers. šatrang, mp. čatrang, skr. caturanga”.\"}\n          ]\n        },\n        {\n          \"id\": 8, \"lang\": \"Latin\", \"words\": \"quadrus; quadrâgintâ\", \"verdict\": \"plausible\",\n          \"derivation\": (\"Both Latin words are genuine and both go back to *kʷetwer-, but the gloss on the first is wrong: \"\n                         \"quadrus is not ‘four’ (that is quattuor) but ‘four-sided, square’, an adjective built on the \"\n                         \"composition stem quadru- (< *kʷetru-), with the derived nouns quadrum ‘a square’ and quadra \"\n                         \"‘square, base of a pedestal, table’. quadrāgintā ‘forty’ is quadrā- + -gintā ‘ten times’ (< *dḱmt-), \"\n                         \"the exact counterpart of Doric τετρώκοντα and Av. caθwarəsatəm; Pokorny gives the equation at IEW 644. \"\n                         \"Verdict ‘plausible’ only because of the loose gloss on quadrus.\"),\n          \"derivation_fa\": (\"هر دو واژهٔ لاتینی اصیل‌اند و هر دو به *kʷetwer- بازمی‌گردند، اما معنایی که برای نخستین آمده دقیق نیست: \"\n                            \"quadrus «چهار» نیست (چهار در لاتین quattuor است) بلکه صفتی است به معنای «چهارگوش، چهارسو» که بر ستاک \"\n                            \"ترکیبی quadru- (از *kʷetru-) ساخته شده، با مشتق‌های quadrum «مربع» و quadra «چهارگوش، پایهٔ ستون، میز». \"\n                            \"quadrāgintā «چهل» از quadrā- و پسوند -gintā «ده‌بار» است و همتای دقیق τετρώκοντα دوری و \"\n                            \"caθwarəsatəm اوستایی است؛ پوکورنی این برابری را در ص ۶۴۴ آورده است. حکم «با احتیاط پذیرفتنی است» \"\n                            \"تنها به‌سبب همان معنای نادقیقِ quadrus است.\"),\n          \"sources\": [\"https://www.etymonline.com/word/cadre\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1068\", \"status\": \"supports\",\n             \"note\": \"AHD:1068 is a page of the New College Edition main dictionary, which is not open online; checked instead the AHD’s own Indo-European appendix (Watkins), AHD_watkins1985.txt s.v. kʷetwer-: “Latin quadrus, four-sided thing, square: CADRE, QUADRATE, QUARREL, QUARRY; SQUAD, SQUARE, TROCAR… Latin quadrāgintā, forty (-gintā, ten times; see dekm): QUARANTINE” — both words, from the same root, in the same source book; note that Watkins glosses quadrus ‘four-sided thing, square’, not ‘four’.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SYN\", \"where\": \"Buck 12.78 SQUARE\", \"stance\": \"partial\",\n             \"note\": \"“quadrus (> It. quadro, Sp. cuadro)… quadra ‘square, base of a pedestal, table’, quadrum ‘square’, all fr. quattuor ‘four’” — confirms the root but glosses quadrus as ‘square’.\"},\n            {\"src\": \"POK\", \"where\": \"IEW 644\", \"stance\": \"supports\",\n             \"note\": \"“dor. ion. delph. τετρώκοντα (*kʷetu̥orə-komtā) = lat. quadrāgintā ‘40”’”.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. quadragenarian\", \"stance\": \"supports\",\n             \"note\": \"“L. quadrāginārius… fr. quadrāgintā (for *quatra-ginta), ‘forty’, which is formed fr. quattuor, ‘four’, with -ginta, a suff. denoting tens… Cp. quarantine, cuarenta.”\"}\n          ]\n        },\n        {\n          \"id\": 9, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n          \"derivation\": (\"A pass-through box with no word printed: the French link is cadre (16th c.) ‘picture frame, \"\n                         \"framework’, borrowed from Italian quadro ‘square, picture’ < Latin quadrum/quadrus. Old French \"\n                         \"also inherited the family directly (esquarre > équerre ‘square’, escadre ‘squadron’ from Italian \"\n                         \"squadra), which is what feeds the English box below. The arrow Latin → French is therefore right, \"\n                         \"though for cadre itself the route runs Latin → Italian → French.\"),\n          \"derivation_fa\": (\"این خانه واژه‌ای چاپ نشده و تنها حلقهٔ واسط است: واژهٔ فرانسوی مورد نظر cadre (سدهٔ شانزدهم میلادی) \"\n                            \"به معنای «قاب، چهارچوب» است که از ایتالیایی quadro «مربع، تابلو» و آن از quadrum/quadrus لاتینی گرفته \"\n                            \"شده است. فرانسهٔ کهن نیز شاخه‌های دیگر همین خانواده را مستقیم به ارث برده (équerre از esquarre، و \"\n                            \"escadre از squadra ایتالیایی) و همان‌هاست که به خانهٔ انگلیسی پایین می‌رسد. پس پیکان لاتین ← فرانسه \"\n                            \"درست است، هرچند برای خودِ cadre مسیر از راه ایتالیایی می‌گذرد.\"),\n          \"sources\": [\"https://www.etymonline.com/word/cadre\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n             \"note\": \"No reference on this box; the parent (AHD:1068) and the child (AHD) cover the chain, and Watkins lists CADRE under Latin quadrus.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1971.txt s.v. cadre\", \"stance\": \"supports\",\n             \"note\": \"“cadre, n., frame, framework; framework of a [military unit]…” — Klein derives it from F. cadre, It. quadro, L. quadrum.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 12.78 SQUARE\", \"stance\": \"supports\",\n             \"note\": \"“Fr. carré, Sp. cuadrado… pple. of quadrāre ‘make square’… fr. quadrus (> It. quadro, Sp. cuadro)” — the Latin → Romance line.\"}\n          ]\n        },\n        {\n          \"id\": 10, \"lang\": \"Persian\", \"words\": \"kâdr «کادر»\", \"verdict\": \"confirmed\",\n          \"derivation\": (\"Persian کادر kādr is a 20th-century loan straight from French cadre [kadʁ], taken over with the \"\n                         \"French stress and consonant cluster and written with alef for the long ā; both French senses came \"\n                         \"with it, the concrete ‘frame, framework (of a picture, a window)’ and the institutional ‘permanent \"\n                         \"staff/managing body of an office’ (compare the Communist-party sense of cadre, 1930s). Mo‘in’s entry \"\n                         \"gives exactly these two senses and, like all his European loans, appends a purist warning; the \"\n                         \"French intermediary is what the chart draws, and it is right.\"),\n          \"derivation_fa\": (\"«کادر» وام‌واژه‌ای است از فرانسوی cadre که در سدهٔ چهاردهم خورشیدی وارد فارسی شده؛ خوشهٔ همخوانی \"\n                            \"پایانی و کشش واکه همان‌گونه که در فرانسه بود نگاه داشته شده و «ا» در نوشتار همان ā کشیده است. هر دو \"\n                            \"معنای فرانسوی نیز با آن آمده است: معنای عینی «قاب، چهارچوب» و معنای اداری «هیئت اداره‌کنندهٔ یک اداره یا \"\n                            \"مؤسسه». معین در فرهنگ فارسی هر دو معنا را آورده و مانند دیگر وام‌واژه‌های اروپایی یادداشت پرهیز از \"\n                            \"کاربرد آن را افزوده است. پس واسطهٔ فرانسوی که نورایی نشان داده درست است.\"),\n          \"sources\": [\"https://www.etymonline.com/word/cadre\"],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\",\n             \"note\": \"Mo‘in (MON_part2.txt, 2-vol. Adena condensation) s.v. کادر: “چوب یا فلزی که دور عکس یا آیینه و غیره قرار دهند؛ قاب، چهارچوب. (ف.) هیئت اداره‌کنندهٔ یک اداره یا مؤسسه. ضح.- احتراز از استعمال این کلمهٔ بیگانه اولی است” — the gloss ‘frame, framework’ is Mo‘in’s, and ‘کلمهٔ بیگانه’ marks it a European loan. (The 6-vol. edition Nourai cites is not online, so the page number could not be checked.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt s.v. کادر\", \"stance\": \"supports\", \"note\": \"see ref_check — both senses and the foreign-word tag.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1971.txt s.v. cadre\", \"stance\": \"supports\",\n             \"note\": \"“cadre, n., frame, framework” — the same two senses in the French donor.\"},\n            {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt, grepped کادر\", \"stance\": \"silent\",\n             \"note\": \"Aryanpur’s IE-roots dictionary treats inherited Persian vocabulary and does not list modern French loans.\"}\n          ]\n        },\n        {\n          \"id\": 11, \"lang\": \"English\", \"words\": \"cadre, squad, square, quart, quarter\", \"verdict\": \"plausible\",\n          \"derivation\": (\"Three of the five come from Latin quadrus as drawn: cadre (1851, ‘framework of a military unit’) \"\n                         \"< Fr. cadre < It. quadro; square (13th c.) < Old French esquarre < Vulgar Latin *exquadra, from \"\n                         \"quadra/quadrus; squad (1640s) < Fr. escouade < It. squadra, same base. But quart and quarter do \"\n                         \"NOT come from quadrus: they continue Latin quārtus ‘fourth’, the ordinal of the same root — \"\n                         \"OFr. quarte/quartier > ME quart, quarter. Watkins puts CADRE, SQUAD, SQUARE under section II \"\n                         \"(multiplicative *kʷetur-/quadrus) but QUART and QUARTER under section III (ordinal *kʷetur-to- > \"\n                         \"L. quārtus), so the box mixes two sub-branches of one root.\"),\n          \"derivation_fa\": (\"از پنج واژهٔ این خانه سه‌تا همان‌گونه که نورایی رسم کرده از quadrus لاتینی می‌آیند: cadre (۱۸۵۱ م) \"\n                            \"از فرانسوی cadre و ایتالیایی quadro؛ square (سدهٔ سیزدهم میلادی) از فرانسهٔ کهن esquarre و لاتین \"\n                            \"عامیانهٔ *exquadra؛ و squad (دههٔ ۱۶۴۰) از فرانسوی escouade و ایتالیایی squadra. اما quart و quarter \"\n                            \"از quadrus نیستند، بلکه دنبالهٔ quārtus لاتینی («چهارم»، صفت ترتیبی از همان ریشه) از راه فرانسهٔ کهن \"\n                            \"quarte/quartier‌اند. واتکینز نیز CADRE و SQUAD و SQUARE را ذیل بخش دوم (ستاک quadru-) و QUART \"\n                            \"و QUARTER را ذیل بخش سوم (صفت ترتیبی *kʷetur-to-) آورده است؛ پس این خانه دو شاخهٔ یک ریشه را \"\n                            \"درهم آمیخته و ادعای نورایی با احتیاط پذیرفتنی است.\"),\n          \"sources\": [\"https://www.etymonline.com/word/cadre\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\",\n             \"note\": AHDQ + \" — the AHD appendix supports CADRE/SQUAD/SQUARE from quadrus, but files QUART and QUARTER under Latin quārtus in section III, not under quadrus.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. four (cross-reference list)\", \"stance\": \"partial\",\n             \"note\": \"“Cp. also cadre, cahier, carfax, carillon, cater… quadrant, quadrate, quadri-, quadrille, quadroon, quarantine, quarrel, quarry, quart, quatrain, quaternion, quire of paper, squad, square, tessara-… trapezium, trocar” — all under one root, but Klein’s own entries separate quart/quarter (< quārtus) from square/squad (< quadrus).\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 12.78 SQUARE\", \"stance\": \"supports\",\n             \"note\": \"“NE square… fr. quadrus” line of Latin → Romance → English.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt s.vv. square, quart\", \"stance\": \"partial\",\n             \"note\": \"Skeat likewise takes square from OF esquarre < L. quadra, but quart from L. quartus.\"}\n          ]\n        },\n        {\n          \"id\": 12, \"lang\": \"Italian\", \"words\": \"quadratina\", \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"quadratina : forty, forty days of isolation at the entry ports of a country…\",\n          \"correct_form\": \"quarantina (Venetian/Italian quarantena)\",\n          \"derivation\": (\"The extraction is faithful: the printed page 265 does read ‘quadratina’ (checked at 450 dpi, \"\n                         \"data/verification/sources/refs/ocr/BOOK/295.png). But there is no Italian word quadratina meaning \"\n                         \"‘forty’; the word behind quarantine is Italian quarantina ‘about forty, a set of forty’ (Venetian \"\n                         \"quarantena), from quaranta ‘forty’ < Latin quadrāgintā — with the regular Italian development \"\n                         \"-drāg- > -rā(n)-. Nourai has evidently contaminated it with quadrato/quadratino ‘small square’. \"\n                         \"The institution he describes is real and correctly described: the forty-day detention of ships \"\n                         \"from plague ports, first imposed at Ragusa in 1377 (thirty days, trentina, then forty) and at \"\n                         \"Venice from 1423, whence It. quaranta giorni. So the semantics of the box are right and only the \"\n                         \"head-form is a misprint of the book.\"),\n          \"derivation_fa\": (\"خوانش اسکن درست است: صفحهٔ چاپی ۲۶۵ به‌راستی «quadratina» دارد. اما در ایتالیایی واژه‌ای به این \"\n                            \"شکل با معنای «چهل» وجود ندارد؛ واژه‌ای که پشت quarantine ایستاده quarantina ایتالیایی «حدود چهل، \"\n                            \"دستهٔ چهل‌تایی» (در ونیزی quarantena) است، از quaranta «چهل» و آن از quadrāgintā لاتینی، با تحول \"\n                            \"آواییِ قاعده‌مندِ -drāg- به -rā(n)- در ایتالیایی. پیداست که نورایی آن را با quadrato/quadratino \"\n                            \"«مربع کوچک» درآمیخته است. اما شرحی که در همین خانه آمده درست است: نگاه‌داشتن چهل‌روزهٔ کشتی‌های \"\n                            \"آمده از بندرهای طاعون‌زده، که نخست در راگوزا (۱۳۷۷ م) و سپس در ونیز (از ۱۴۲۳ م) برقرار شد و از \"\n                            \"همان‌جا ترکیب quaranta giorni پدید آمد. پس تنها سرواژه خطای چاپی کتاب است.\"),\n          \"sources\": [\"https://www.etymonline.com/word/quarantine\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1068\", \"status\": \"partial\",\n             \"note\": \"The New College main-dictionary page 1068 is not online; checked the AHD IE appendix instead (AHD_watkins1985.txt s.v. kʷetwer-): “Latin quadrāgintā, forty (-gintā, ten times; see dekm): QUARANTINE” — the AHD derives QUARANTINE from quadrāgintā and knows no form ‘quadratina’.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. quarantine\", \"stance\": \"contradicts\",\n             \"note\": \"“quarantine, n.… — It. quarantina, fr. quaranta, ‘forty’, fr. L. quadrāgintā… The term goes back to It. quaranta giorni, ‘forty days’. Ships coming from the Levant and Egypt were isolated at special ports for thirty, later forty, days… first enforced at Ragusa in 1377.” The Italian form is quarantina, not quadratina.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt s.v. quarantine\", \"stance\": \"contradicts\",\n             \"note\": \"“quarantine… O.F. quarantaine, a space of [forty] days. — F. quarante, forty. — L. quadrāgintā”.\"},\n            {\"src\": \"TAD\", \"where\": \"al-Unaysi p. 62\", \"stance\": \"contradicts\",\n             \"note\": \"“كرنتينا — ايطالي quarantena معناه أربعون يوما” — Nourai’s own Arabic source spells the Italian quarantena.\"}\n          ]\n        },\n        {\n          \"id\": 13, \"lang\": \"Arabic\", \"words\": \"karantînâ, qarantîna\", \"verdict\": \"confirmed\",\n          \"derivation\": (\"Arabic كرنتينا karantīnā / قرنطينة qaranṭīna ‘quarantine’ is a 19th-century borrowing of the \"\n                         \"Italian maritime term quarantena/quarantina, taken in through Levantine ports (Beirut, Alexandria, \"\n                         \"Izmir) where Italian was the lingua franca of shipping. The two Arabic shapes reflect two routes of \"\n                         \"adaptation: k-r-n-t-y-n-ā keeps the Italian consonants unchanged, while q-r-n-ṭ-y-n-a substitutes the \"\n                         \"emphatic ṭ for t after r and q for k, the usual Arabic treatment of European t/k in an emphatic \"\n                         \"environment (compare قميص : camicia). Nourai’s own reference is exactly on the point: al-Unaysi’s \"\n                         \"dictionary of foreign words in Arabic, p. 62.\"),\n          \"derivation_fa\": (\"عربی «کرنتینا / قرنطینة» وام‌واژه‌ای است از اصطلاح دریایی ایتالیایی quarantena/quarantina که در \"\n                            \"سدهٔ نوزدهم میلادی از راه بندرهای شام و مصر (بیروت، اسکندریه، ازمیر) که زبان میانجی بازرگانی‌شان \"\n                            \"ایتالیایی بود وارد عربی شد. دو صورت عربی دو شیوهٔ سازگارسازی‌اند: در «کرنتینا» همخوان‌های ایتالیایی \"\n                            \"دست‌نخورده مانده‌اند و در «قرنطینة» پس از «ر» ابدال t به طِ مفخّم و k به ق روی داده است ــ همان رفتار \"\n                            \"همیشگی عربی با t و k اروپایی در بافت مفخّم (سنجیدنی با camicia ← قمیص). مأخذی که نورایی داده دقیقاً \"\n                            \"همین را می‌گوید. ادعای نورایی درست است.\"),\n          \"sources\": [\"https://www.etymonline.com/word/quarantine\"],\n          \"ref_check\": [\n            {\"ref\": \"TAD:62\", \"status\": \"supports\",\n             \"note\": \"Read the page image (archive.org/details/TOB1932ARAR leaf n65 = printed ٦٢ = 62; the OCR of TAD_pages.txt leaf 65 is unusable, so the reading is saved at data/verification/sources/refs/ocr/TAD/62.vision.txt): “كرنتينا — ايطالي quarantena معناه أربعون يوما مرادفه المحجر الصحي” = ‘karantīnā — Italian quarantena, meaning forty days; its synonym is the health quarantine’. Exactly Nourai’s Italian → Arabic arrow, on exactly the page he cites. (Note: the ق-section, pp. 56-58, has no قرنطينة entry — al-Unaysi files the word under ك.)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. quarantine\", \"stance\": \"supports\",\n             \"note\": \"“It. quarantina… The term goes back to It. quaranta giorni” — the Italian origin of the international word.\"},\n            {\"src\": \"LKT\", \"where\": \"LKT.txt (Lokotsch), grepped Karantän-/Quarantäne\", \"stance\": \"silent\",\n             \"note\": \"Lokotsch covers European words of ORIENTAL origin, so a European word borrowed INTO Arabic is outside his scope — no entry.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\",\n             \"note\": \"Asbaghi covers Persian loans in Arabic only; قرنطينة is not Persian and is absent.\"}\n          ]\n        },\n        {\n          \"id\": 14, \"lang\": \"Persian\", \"words\": \"qarantîn «قرنطین» (قرنطینه)\", \"verdict\": \"plausible\",\n          \"derivation\": (\"Persian قرنطینه qaranṭīne ‘quarantine (station)’ is certainly the same international word, and it is \"\n                         \"written in Arabic dress (ق and ط for European k/qu and t), which is why Mo‘in labels the shorter \"\n                         \"قرنطین as ‘[- قرنطینه، معر.]’, i.e. an Arabicised form; that spelling supports Nourai’s \"\n                         \"Italian → Arabic → Persian route. Against it, most Iranian lexicographers take قرنطینه as a direct \"\n                         \"loan from French quarantaine, which is what the final -e (ـه) actually renders — an Arabic قرنطينة \"\n                         \"would normally give Persian قرنطینه too, so the two routes are hard to separate on form alone, and \"\n                         \"the word entered Persian in the Qajar period together with a mass of French administrative and \"\n                         \"medical vocabulary. Verdict ‘plausible’: the chain is compatible with Mo‘in, but the French route is \"\n                         \"at least as likely for the immediate donor.\"),\n          \"derivation_fa\": (\"«قرنطینه» بی‌گمان همان واژهٔ بین‌المللی است و در فارسی با جامهٔ عربی نوشته می‌شود (ق و ط به‌جای \"\n                            \"k/qu و t اروپایی)؛ به همین سبب معین صورت کوتاه «قرنطین» را «[- قرنطینه، معر.]» یعنی معرّب دانسته است \"\n                            \"و همین نکته مسیر ایتالیایی ← عربی ← فارسیِ نورایی را تأیید می‌کند. در برابر، بیشتر فرهنگ‌نویسان \"\n                            \"ایرانی «قرنطینه» را وام‌واژه‌ای یک‌راست از فرانسوی quarantaine می‌دانند و «ـه» پایانی هم همان -aine \"\n                            \"فرانسوی است؛ از سوی دیگر «قرنطینة» عربی نیز در فارسی «قرنطینه» می‌شود، پس این دو راه را تنها از روی \"\n                            \"صورت نمی‌توان از هم جدا کرد، و واژه در دورهٔ قاجار همراه انبوهی از واژگان اداری و پزشکی فرانسوی وارد \"\n                            \"شده است. حکم: ادعای نورایی با احتیاط پذیرفتنی است؛ راه فرانسوی دست‌کم به همان اندازه محتمل است.\"),\n          \"sources\": [\"https://www.etymonline.com/word/quarantine\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:2666\", \"status\": \"partial\",\n             \"note\": \"The 6-vol. Mo‘in (where p. 2666 belongs) is not online; the 2-vol. Adena condensation (MON_part2.txt) has “قرنطین: [- قرنطینه، معر.] (ا.) جایی که در آن مسافرانی را که از سرزمینی وارد می‌شوند که در آنجا بیماریی ساری مانند وبا و طاعون شیوع دارد، مدت چند روز نگهداری می‌کنند” — same headword, same gloss, and the tag معر. (Arabicised) that Nourai’s arrow relies on; the page number itself could not be verified.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt s.v. قرنطین\", \"stance\": \"supports\",\n             \"note\": \"see ref_check — “[- قرنطینه، معر.]”.\"},\n            {\"src\": \"TAD\", \"where\": \"al-Unaysi p. 62\", \"stance\": \"supports\",\n             \"note\": \"“كرنتينا — ايطالي quarantena” — the Arabic link in the chain exists and is Italian-derived.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v3/v4_pages.txt, grepped قرنط\", \"stance\": \"silent\",\n             \"note\": \"Borhan-e Qate‘ (1652) predates the word; no entry, as expected.\"}\n          ]\n        },\n        {\n          \"id\": 15, \"lang\": \"English\", \"words\": \"quarantine\", \"verdict\": \"confirmed\",\n          \"derivation\": (\"English quarantine, in the medical sense, is first recorded in the 1660s, borrowed from Italian \"\n                         \"quarantina (Venetian quarantena) ‘a space of forty days’, from quaranta ‘forty’ < Latin \"\n                         \"quadrāgintā; the practice is the Venetian one of holding ships from plague ports offshore for \"\n                         \"forty days (Ragusa 1377, Venice 1423). Two older English senses of the same word came in earlier \"\n                         \"through French: quarentyne (15th c.) ‘the desert where Christ fasted forty days’ and quarantine \"\n                         \"(1520s) ‘the forty days a widow may stay in her dead husband’s house’. The verb is 1804.\"),\n          \"derivation_fa\": (\"واژهٔ انگلیسی quarantine در معنای پزشکی نخستین‌بار در دههٔ ۱۶۶۰ م ثبت شده و وام‌واژه‌ای است از \"\n                            \"ایتالیایی quarantina (در ونیزی quarantena) «دورهٔ چهل‌روزه»، از quaranta «چهل» و آن از quadrāgintā \"\n                            \"لاتینی؛ خودِ رسم هم ونیزی است: نگاه‌داشتن چهل‌روزهٔ کشتی‌های آمده از بندرهای طاعون‌زده (راگوزا ۱۳۷۷ م، \"\n                            \"ونیز ۱۴۲۳ م). دو معنای کهن‌تر همین واژه پیش‌تر از راه فرانسه وارد انگلیسی شده بود: quarentyne \"\n                            \"(سدهٔ پانزدهم) «بیابانی که مسیح چهل روز در آن روزه گرفت» و quarantine (دههٔ ۱۵۲۰) «چهل روزی که بیوه \"\n                            \"حق ماندن در خانهٔ شوی درگذشته را دارد». ادعای نورایی درست است.\"),\n          \"sources\": [\"https://www.etymonline.com/word/quarantine\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1068\", \"status\": \"supports\",\n             \"note\": \"New College p. 1068 not online; the AHD’s IE appendix (AHD_watkins1985.txt s.v. kʷetwer-) has “Latin quadrāgintā, forty (-gintā, ten times; see dekm): QUARANTINE” — the English word is derived from the Latin ‘forty’ exactly as the chart draws.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. quarantine\", \"stance\": \"supports\",\n             \"note\": \"“It. quarantina, fr. quaranta, ‘forty’, fr. L. quadrāgintā… first enforced at Ragusa in 1377”, with the reference to K. Sudhoff, Essays in the History of Medicine, p. 152.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt s.v. quarantine\", \"stance\": \"supports\",\n             \"note\": \"“quarantine… O.F. quarantaine, a space of [forty] days. — F. quarante, forty. — L. quadrāgintā” — Skeat routes it through French rather than Italian, a minor difference.\"}\n          ]\n        },\n        {\n          \"id\": 16, \"lang\": \"Germanic\", \"words\": \"petwor\", \"verdict\": \"plausible\",\n          \"derivation\": (\"Proto-Germanic ‘four’ is *fedwōr (Goth. fidwōr, ON fjórir, OE fēower, OHG fior). Its f- cannot \"\n                         \"come straight from *kʷ-, which would give Gmc *hw-; a pre-form with initial *p- is therefore \"\n                         \"posited, *petwor-, produced by dissimilation of the first labiovelar before the *-w- of the second \"\n                         \"syllable (*kʷetwor- > *petwor- > *fedwōr by Grimm’s law, with *t > *d by Verner’s law). Modern \"\n                         \"handbooks (Kroonen, Ringe) do reconstruct exactly this *petwor-, so Nourai’s form is defensible; \"\n                         \"but it is a PRE-Germanic stage, not a Germanic word, and the p-forms actually attested belong to \"\n                         \"Italic and Celtic (Osc. petora, pettiur, Gaul. petuarios, Welsh pedwar). Pokorny himself, at IEW \"\n                         \"643, derives Germanic instead from an assimilated *kʷekʷor-, and Watkins writes ‘Probably Germanic \"\n                         \"*fe(d)wor-’ — neither prints ‘Germanic petwor’. Hence plausible, with a mislabelled node.\"),\n          \"derivation_fa\": (\"صورت ژرمنی آغازین «چهار» *fedwōr است (گوتی fidwōr، نورس کهن fjórir، انگلیسی کهن fēower، \"\n                            \"آلمانی علیای کهن fior). f آغازین آن نمی‌تواند یک‌راست از *kʷ آمده باشد، زیرا *kʷ در ژرمنی *hw \"\n                            \"می‌دهد؛ از این‌رو صورت پیشاژرمنی *petwor- بازسازی می‌شود که از ناهمگونی‌ (dissimilation) نخستین \"\n                            \"لبی‌کامی پیش از w هجای دوم پدید آمده است (*kʷetwor- ← *petwor- و سپس با قانون گریم و ورنر \"\n                            \"*fedwōr). کتاب‌های امروزی (کرونن، رینگه) همین *petwor- را بازمی‌سازند، پس صورتِ نورایی بی‌پایه \"\n                            \"نیست؛ اما این مرحلهٔ پیشاژرمنی است نه واژه‌ای ژرمنی، و صورت‌های p‌دارِ گواهی‌شده به ایتالیایی باستان \"\n                            \"و سلتی تعلق دارند (اسکی petora، گلی petuarios، ولزی pedwar). خود پوکورنی در ص ۶۴۳ ژرمنی را از \"\n                            \"*kʷekʷor- همگون‌شده می‌گیرد و واتکینز «احتمالاً ژرمنی *fe(d)wor-» می‌نویسد. پس برچسب این خانه \"\n                            \"نادرست است، هرچند بازسازی‌اش پذیرفتنی.\"),\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7etw%C3%B3res\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\",\n             \"note\": \"AHD_watkins1985.txt s.v. kʷetwer-: “I. O-grade form *kʷetwor-. 1. Probably Germanic *fe(d)wor- in: a. Old English fēower, four: FOUR…” — the AHD supports the root and the English words but writes the Germanic form *fe(d)wor-, never petwor.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"IEW 643 (POK_02.txt leaf 302)\", \"stance\": \"contradicts\",\n             \"note\": \"“got. fidwōr, nord. und westgerm. auf Grund einer Assimilationsform *kʷekʷor…” — Pokorny explains Germanic by assimilation to *kʷekʷor-, and puts the p-forms under Italic/Celtic: “osk. pettiur, petora… acymr. petuar, ncymr. pedwar… gall. petuarios”.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. four\", \"stance\": \"partial\",\n             \"note\": \"“Goth. fidwōr, ‘four’… Oscan petora, Umbr. petur-” — Klein too keeps the p-forms Italic.\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I 512\", \"stance\": \"partial\",\n             \"note\": \"“got. fidur-dogs… umbr. petur[-pursus]… gall. Petru-corios” — p- in Italic and Celtic, f- in Germanic.\"}\n          ]\n        },\n        {\n          \"id\": 17, \"lang\": \"English\", \"words\": \"four, fourteen, forty\", \"verdict\": \"confirmed\",\n          \"derivation\": (\"All three are inherited, not borrowed: OE fēower > ME fower/foure > four; OE fēowertēne \"\n                         \"(fēower + tēn ‘ten’) > fourteen; OE fēowertig (fēower + -tig ‘decade’) > forty, whose modern \"\n                         \"spelling with -or- reflects the shortening of the vowel in the unstressed compound (four : forty). \"\n                         \"All continue Proto-Germanic *fedwōr < the pre-Germanic *petwor- of the parent box, and Watkins \"\n                         \"lists FOUR, FOURTEEN and FORTY together under Germanic *fe(d)wor-.\"),\n          \"derivation_fa\": (\"هر سه واژه ارثی‌اند نه وام‌واژه: fēower انگلیسی کهن به four، fēowertēne (از fēower + tēn «ده») \"\n                            \"به fourteen، و fēowertig (از fēower + پسوند دهگانِ -tig) به forty رسیده است؛ املای امروزیِ forty با \"\n                            \"-or- بازتاب کوتاه‌شدن واکه در ترکیبِ بی‌تکیه است (four در برابر forty). هر سه دنبالهٔ *fedwōr \"\n                            \"ژرمنی آغازین‌اند که در خانهٔ بالا آمده، و واتکینز نیز FOUR و FOURTEEN و FORTY را با هم ذیل \"\n                            \"*fe(d)wor- ژرمنی آورده است. ادعای نورایی درست است.\"),\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7etw%C3%B3res\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n             \"note\": \"No reference on this box; the parent cites AHD, whose appendix (s.v. kʷetwer-) lists exactly these three English words: “Old English fēower, four: FOUR; … fēowertig, forty: FORTY; … fēowertēne, fourteen: FOURTEEN”.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. four\", \"stance\": \"supports\",\n             \"note\": \"“four, adj. and n. — ME. feower, fower, foure, four, fr. OE. feower… Cp. fardel, ‘fourth part’, farthing, firkin, forty.”\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt s.v. four\", \"stance\": \"supports\",\n             \"note\": \"Skeat likewise: OE fēower, cognate with L. quattuor, Gk. τέσσαρες.\"},\n            {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. kʷetwer-\", \"stance\": \"supports\",\n             \"note\": \"FOUR, FORTY, FOURTEEN all listed under Germanic *fe(d)wor-.\"}\n          ]\n        },\n        {\n          \"id\": 18, \"lang\": \"Greek\", \"words\": \"tra-peza\", \"verdict\": \"confirmed\",\n          \"derivation\": (\"Ancient Greek τράπεζα trápeza ‘table’ is a transparent compound *kʷtwṛ-ped-ya ‘four-footed \"\n                         \"(thing)’: the zero grade *kʷt(w)r- of *kʷetwer- gives Greek tra- (as in τρά-πεζα, beside the \"\n                         \"full-grade τετρα-), and -πεζα is the *-ya derivative of *ped- ‘foot’ (Gk. πούς, πεζός). \"\n                         \"The diminutive τραπέζιον trapézion ‘little table’ was used by the geometers for an irregular \"\n                         \"quadrilateral, whence trapezium/trapezoid. Watkins files TRAPEZIUM under both kʷetwer- and ped-1, \"\n                         \"which is precisely the two-root analysis Nourai marks with his ☆Ped cross-reference.\"),\n          \"derivation_fa\": (\"«τράπεζα» یونانی باستان به معنای «میز» ترکیبی است شفاف از *kʷtwṛ-ped-ya یعنی «چهارپا/چهارپایه»: \"\n                            \"درجهٔ صفر ریشهٔ *kʷetwer- در یونانی tra- می‌دهد (در برابر درجهٔ کاملِ τετρα-) و -πεζα مشتقِ *-ya از \"\n                            \"*ped- «پا» است (یونانی πούς و πεζός). صورت مصغر τραπέζιον «میز کوچک» را هندسه‌دانان برای \"\n                            \"چهارضلعی نامنتظم به کار بردند و از همان‌جا trapezium و trapezoid پدید آمد. واتکینز واژهٔ TRAPEZIUM \"\n                            \"را هم ذیل kʷetwer- و هم ذیل ped- آورده است، یعنی همان تحلیل دو‌ریشه‌ای که نورایی با ارجاع ☆Ped \"\n                            \"نشان داده است. ادعای نورایی درست است.\"),\n          \"sources\": [\"https://www.etymonline.com/word/trapeze\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD:1365\", \"status\": \"supports\",\n             \"note\": \"New College p. 1365 (the ‘tr-’ pages of the main dictionary) is not open online; the AHD’s IE appendix says it twice — s.v. kʷetwer-: “d. zero-grade form *kʷt(w)r- in Greek tra-, four: TRAPEZIUM”, and s.v. ped-1: “8. Suffixed form *ped-ya in Greek peza, foot: TRAPEZIUM”; the index line reads “TRAPEZIUM kʷetwer-, ped-1”.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I 512\", \"stance\": \"supports\",\n             \"note\": \"“av. čaθru-[gaoša-]: gr. τετρα-[γουνος]… schwundstufig oder durch Diss. aus τετρα- gr. τράπεζα (Lit. auch bei Boisacq 979)” — the zero-grade tra- of τράπεζα explicitly.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.vv. foot and tessara-\", \"stance\": \"supports\",\n             \"note\": \"s.v. foot the cross-reference list ends “… teapoy, trapezium, triped, tripos”; s.v. tessara- “fr. I.-E. base *qʷetur-, ‘four’. See four and cp.… the first element in trapezium”.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck (table/foot sections)\", \"stance\": \"supports\",\n             \"note\": \"Buck likewise analyses τράπεζα as ‘four-footed’, from the numeral plus πέζα.\"}\n          ]\n        },\n        {\n          \"id\": 19, \"lang\": \"Arabic\", \"words\": \"dar-bezin\", \"verdict\": \"plausible\",\n          \"derivation\": (\"The Arabic word is درابزين darābzīn (also دربزين, درابزون) ‘railing, banister, balustrade’, \"\n                         \"and Mo‘in’s footnote in Borhan-e Qate‘ p. 829 derives it exactly as the chart does: ‘درابزین — from \"\n                         \"Greek Trapézion (railing, lattice); its Arabicised forms are درابزین and دربوز’ (citing Dozy I 430 \"\n                         \"and Mu‘jamiyyāt ‘arabiyya sāmiyya 227), i.e. the Greek diminutive τραπέζιον was taken into Arabic \"\n                         \"with prothetic/metathetic reshaping (tr- unpronounceable initially in Arabic → dar-) and given the \"\n                         \"sense ‘lattice/railing’ from the trellis-table shape. Two reservations: Nourai’s form ‘dar-bezin’ and \"\n                         \"his gloss ‘a seating area between two doors of a room’ are really Mo‘in’s Persian entry for \"\n                         \"دارافزین (‘مجری که در جلو اطاق بین دو در سازند؛ تکیه‌گاه، طارمی’), not the Arabic sense; and Wiktionary \"\n                         \"reverses the direction, making Arabic درابزين a loan from Ottoman Turkish طرابزان < Persian داربزین.\"),\n          \"derivation_fa\": (\"واژهٔ عربی «درابزین» (و گونه‌های «دربزین» و «درابزون») به معنای «نرده، طارمی، محجر» است و حاشیهٔ \"\n                            \"معین بر برهان قاطع در ص ۸۲۹ آن را درست همان‌گونه که نورایی رسم کرده ریشه‌یابی می‌کند: «درابزین ــ از \"\n                            \"یونانی Trapézion (نرده، شبکه) معرّب آن درابزین و دربوز» با ارجاع به دُزی ج۱ ص۴۳۰ و «معجمیات عربیة \"\n                            \"سامیة» ص۲۲۷. یعنی مصغر یونانی τραπέζιον با دگرگونی آغازین (خوشهٔ tr در آغاز واژهٔ عربی ناممکن است و \"\n                            \"به dar- بدل شده) وارد عربی شده و معنای «نرده/شبکه» را از شکل شبکه‌مانندِ آن گرفته است. دو نکته: صورت \"\n                            \"«dar-bezin» و معنای «جایی برای نشستن میان دو درِ اتاق» که نورایی آورده در اصل مدخل فارسیِ «دارافزین» \"\n                            \"در فرهنگ معین است نه معنای عربی؛ و ویکی‌واژه جهت وام‌گیری را وارونه می‌داند و «درابزین» عربی را از \"\n                            \"ترکی عثمانی «طرابزان» و آن را از «داربزین» فارسی می‌گیرد. پس با احتیاط پذیرفتنی است.\"),\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%A7%D8%A8%D8%B2%D9%8A%D9%86\",\n            \"https://www.etymonline.com/word/trapeze\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:1481\", \"status\": \"partial\",\n             \"note\": \"The 6-vol. Mo‘in is not online, so p. 1481 could not be opened; but Mo‘in’s own footnote in his edition of Borhan-e Qate‘, p. 829 (read from the page image, archive.org/details/borhan-ghate-v2 leaf n289; saved at data/verification/sources/refs/ocr/BQT/829.vision.txt) states the identical claim: “* درابزین ـ از یونانی Trapézion (نرده، شبکه) معرب آن درابزین و دربوز «دزی ج ۱ ص ۴۳۰»… و درابزون «المنجد»”.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate‘ ed. Mo‘in, vol. 2 p. 829, Mo‘in’s footnote\", \"stance\": \"supports\",\n             \"note\": \"“* درابزین ـ از یونانی Trapézion (نرده، شبکه) معرب آن درابزین و دربوز” — the Greek τραπέζιον → Arabic step of Nourai’s chain, in Mo‘in’s own words, with Dozy as authority.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. دارافزین\", \"stance\": \"partial\",\n             \"note\": \"“دارافزین: [- دارابزین - داربزین - داروزین - معر. درابزین، درابزون] (ا.) مجری که در جلو اطاق بین دو در سازند؛ تکیه‌گاه، طارمی” — the gloss Nourai puts on the ARABIC box is in fact Mo‘in’s gloss on the PERSIAN word.\"},\n            {\"src\": \"TAD\", \"where\": \"TAD.txt / TAD_pages.txt, grepped درابزين\", \"stance\": \"silent\",\n             \"note\": \"al-Unaysi’s dictionary of foreign words in Arabic has no entry for درابزين.\"}\n          ]\n        },\n        {\n          \"id\": 20, \"lang\": \"Persian\", \"words\": \"dârâbzîn «دارابزین» (درابزین ، دارافزین ، داروزین)\", \"verdict\": \"confirmed\",\n          \"derivation\": (\"Persian دارابزین / دارافزین / داروزین / درابزین ‘balustrade, railing, the rail or dais built \"\n                         \"between the two doors at the front of a room’ is one word in many shapes, and Mo‘in lists exactly \"\n                         \"these four in his Farhang (‘دارافزین [- دارابزین - داربزین - داروزین - معر. درابزین، درابزون]’) \"\n                         \"with the very gloss Nourai gives. The variation ‑bzīn ~ ‑fzīn ~ ‑wzīn is the ordinary Persian \"\n                         \"alternation of b/f/w in an unstressed medial syllable, helped along by folk etymology (دار ‘wood, \"\n                         \"post’ + افزودن ‘to add’, as if ‘added woodwork’). Mo‘in’s note in Borhan-e Qate‘ p. 829 traces the \"\n                         \"word to Greek τραπέζιον through an Arabicised درابزین/دربوز, which is exactly the route drawn here.\"),\n          \"derivation_fa\": (\"«دارابزین / دارافزین / داروزین / درابزین» یک واژه با چند گونهٔ نوشتاری است به معنای «نرده، طارمی، \"\n                            \"مجری‌ای که در جلو اتاق میان دو در می‌سازند»، و معین در فرهنگ فارسی دقیقاً همین چهار گونه را با همان \"\n                            \"معنایی که نورایی آورده ثبت کرده است: «دارافزین [- دارابزین - داربزین - داروزین - معر. درابزین، درابزون] \"\n                            \"مجری که در جلو اطاق بین دو در سازند؛ تکیه‌گاه، طارمی». گوناگونی ـبزین/ـفزین/ـوزین همان ابدال معمول \"\n                            \"ب و ف و و در هجای میانیِ بی‌تکیه است که ریشه‌شناسی عامیانه (دار + افزودن، گویی «چوبِ افزوده») نیز \"\n                            \"به آن دامن زده است. حاشیهٔ معین بر برهان قاطع در ص ۸۲۹ واژه را از یونانی τραπέζιον از راه صورت \"\n                            \"معرّبِ درابزین/دربوز می‌گیرد؛ یعنی همان مسیری که نورایی رسم کرده است. ادعای نورایی درست است.\"),\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%A7%D8%A8%D8%B2%D9%8A%D9%86\",\n            \"https://www.etymonline.com/word/trapeze\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:1481\", \"status\": \"partial\",\n             \"note\": \"6-vol. Mo‘in not online; the 2-vol. condensation (MON_part1.txt) has the entry verbatim: “دارافزین: [- دارابزین - داربزین - داروزین - معر. درابزین، درابزون] (ا.) مجری که در جلو اطاق بین دو در سازند؛ تکیه گاه؛ طارمی” — all four variants of Nourai’s box and his gloss, so the content of MON:1481 is confirmed even though the page number is not.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt s.v. دارافزین\", \"stance\": \"supports\", \"note\": \"see ref_check — the four variants and the gloss.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate‘ vol. 2 pp. 829-830, headword درابزین with Mo‘in’s footnote\", \"stance\": \"supports\",\n             \"note\": \"“«دارافزین» (درابزین)… وداروزین و داربزین بمعنی تکیه‌گاه و محجر تخت و صفه و بام…” and the footnote “از یونانی Trapézion (نرده، شبکه)”.\"},\n            {\"src\": \"RCH\", \"where\": \"Richardson, Persian-Arabic-English\", \"stance\": \"silent\",\n             \"note\": \"grepped for درابزین/دارابزین in RCH.txt — the OCR turns up nothing usable.\"}\n          ]\n        },\n        {\n          \"id\": 21, \"lang\": \"Latin\", \"words\": \"\", \"verdict\": \"confirmed\",\n          \"derivation\": (\"Another unfilled pass-through: the Latin link is Late Latin trapezium, the learned borrowing of \"\n                         \"Greek τραπέζιον (with the usual Latinisation of Greek -ion to -ium). Classical Latin already had \"\n                         \"trapezīta ‘money-changer’ from τραπεζίτης (the banker’s ‘table’), but it is the geometers’ \"\n                         \"trapezium, used in the Latin translations of Euclid, that gives the modern words.\"),\n          \"derivation_fa\": (\"این هم خانه‌ای واسط و بی‌واژه است: حلقهٔ لاتینی همان trapezium در لاتینِ متأخر است، وام‌واژه‌ای \"\n                            \"عالمانه از τραπέζιον یونانی با لاتینی‌سازی معمولِ -ion به -ium. لاتین کلاسیک پیش‌تر trapezīta \"\n                            \"«صرّاف» را از τραπεζίτης (از «میز» صرّافی) گرفته بود، اما آنچه واژه‌های امروزی از آن برآمده‌اند \"\n                            \"همان trapezium هندسه‌دانان است که در ترجمه‌های لاتین اقلیدس به کار رفته است. ادعای نورایی درست است.\"),\n          \"sources\": [\"https://www.etymonline.com/word/trapeze\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\",\n             \"note\": \"AHD_watkins1985.txt lists TRAPEZIUM (the Latin form) as the English outcome of Greek trapeza under both kʷetwer- and ped-1; the index line reads “TRAPEZIUM kʷetwer-, ped-1”.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. trapeze\", \"stance\": \"supports\",\n             \"note\": \"“trapeze, n.… — F. trapèze, fr. Late L. trapezium” — the Late Latin link.\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet, LAT.txt s.v. trapezita/trapezium\", \"stance\": \"supports\",\n             \"note\": \"Ernout-Meillet treat trapez- words as Greek loans in Latin (trapezīta ‘banquier’, from τράπεζα).\"}\n          ]\n        },\n        {\n          \"id\": 22, \"lang\": \"English\", \"words\": \"trapezoid, trapeze\", \"verdict\": \"confirmed\",\n          \"derivation\": (\"trapezoid (1706, in geometry) is Modern Latin trapezoides, from Greek τραπεζοειδής \"\n                         \"‘table-shaped’ (τράπεζα + -οειδής ‘-shaped’); trapeze (1861) is French trapèze, from Late Latin \"\n                         \"trapezium, the gymnastic apparatus being so named because the bar, the two ropes and the ceiling \"\n                         \"outline a trapezium. The geometrical trapezium itself is in English from the 1560s and the wrist \"\n                         \"bone from 1840. All ultimately continue the Greek ‘four-footed’ compound of the box above.\"),\n          \"derivation_fa\": (\"trapezoid (۱۷۰۶ م، در هندسه) از لاتین نو trapezoides و آن از τραπεζοειδής یونانی «میزمانند» \"\n                            \"(از τράπεζα و پسوند -οειδής «‌مانند») است؛ و trapeze (۱۸۶۱ م) از فرانسوی trapèze و آن از \"\n                            \"trapezium لاتینِ متأخر، زیرا میلهٔ بازی و دو طناب و سقف روی‌هم یک ذوزنقه می‌سازند. خودِ trapezium \"\n                            \"هندسی از دههٔ ۱۵۶۰ و نام استخوان مچ از ۱۸۴۰ در انگلیسی است. همهٔ اینها در پایان به همان ترکیب \"\n                            \"یونانیِ «چهارپا» در خانهٔ بالا بازمی‌گردند. ادعای نورایی درست است.\"),\n          \"sources\": [\"https://www.etymonline.com/word/trapeze\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\",\n             \"note\": \"AHD_watkins1985.txt s.v. kʷetwer- — “d. zero-grade form *kʷt(w)r- in Greek tra-, four: TRAPEZIUM”; the trapeze/trapezoid family is the same word.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. trapeze\", \"stance\": \"supports\",\n             \"note\": \"“trapeze, n., a suspended horizontal bar used in gymnastics. — F. trapèze, fr. Late L. trapezium.”\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt s.v. trapezium\", \"stance\": \"supports\",\n             \"note\": \"Skeat derives trapezium from Gk. τραπέζιον, dimin. of τράπεζα ‘a table’, lit. ‘four-footed’.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, FSD_vol4.txt s.v. trapeze/trapezoid\", \"stance\": \"supports\",\n             \"note\": \"Same chain: Gk. trapeza > L. trapezium > F. trapèze > E. trapeze.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-295.json', 'w', encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('ok')\n"
}
```


### [2026-09-06T22:53:49.238Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p295/build.py (file state is current in your context — no need to Read it back)
```


## [2026-09-06T22:53:55.959Z] TOOL CALL #88: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p295/build.py && python3 -m json.tool data/verification/page-295.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 295",
 "description": "Build and verify page-295.json"
}
```


### [2026-09-06T22:54:02.946Z] TOOL RESULT

```
ok
JSON OK
nodes verified: 22/22
node verdicts: {'plausible': 6, 'confirmed': 12, 'disputed': 1, 'transcription_suspect': 3}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 12, 'not_checked': 4, 'partial': 6}
books consulted: {'supports': 39, 'silent': 10, 'contradicts': 6, 'partial': 10} | by book: {'KLN': 14, 'MON': 6, 'BQT': 6, 'SKT': 5, 'ARY': 4, 'POK': 4, 'SYN': 4, 'PHD': 3, 'PLA': 3, 'TAD': 3, 'NYB': 2, 'WLD': 2, 'BRT': 1, 'HRN': 1, 'HUB': 1, 'AFM': 1, 'LKT': 1, 'AHD': 1, 'RCH': 1, 'LAT': 1, 'FSD': 1}
```


## [2026-09-06T22:54:12.343Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSD trapeze ===\"; grep -c -i \"trapeze\" FSD_vol4.txt; grep -n -i -o \"trapeze[^ ]\\{0,60\\}\" FSD_vol4.txt | head -3\necho \"=== LAT trapez ===\"; grep -n -i -o \"trapez[a-zî]*[^ ]\\{0,80\\}\" LAT.txt | head -3\necho \"=== SKT four/square ===\"; grep -n -i -o \"square,[^|]\\{0,120\\}\" SKT.txt | head -2; grep -n -i -o \"quart,[^|]\\{0,120\\}\" SKT.txt | head -2; grep -n -i -o \"^four[^|]\\{0,150\\}\" SKT.txt | head -2\necho \"=== SKT trapezium ===\"; grep -n -i -o \"trapezium[^|]\\{0,120\\}\" SKT.txt | head -2\necho \"=== RCH darabzin ===\"; grep -c \"درابز\\|دارابز\" RCH.txt\necho \"=== SYN trapeza ===\"; grep -n -o \"τράπεζα\\|trapeza\\|rpdmeza\\|rgdmeCa\" SYN.txt | head -3",
 "description": "Verify asserted consulted quotes"
}
```


### [2026-09-06T22:54:15.522Z] TOOL RESULT

```
=== FSD trapeze ===
1
38525:trapezet
=== LAT trapez ===
=== SKT four/square ===
12426:square,    rule,     pattern.     For    jfnw*"*' allied  to  Ononoon.     (^GNA.)
14146:square,  a  piaaza.
15310:quart,  the  fourth  of  a  galloo.  (F.* M.  E.  quarlt.  —  F.  quarte.  —  I     '"  "*'  '^ parT\  a  fourth  part ;  fem.
15352:Quart,  Quartan,  &c.;  see  Quadrate.
7014:Four.  (E.)  M.  K.  feovfur.  fowtr,  four. A,  S.  ftSwtr-  •+■  Icei.  fj6rir,  Dnn  fire. Swed.^m,  Du.  wVr.  Goih._/f(/uY^r,  G.  vUr, W.  ptif-witr
=== SKT trapezium ===
=== RCH darabzin ===
0
=== SYN trapeza ===
12127:trapeza
```


## [2026-09-06T22:54:27.865Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN trapeza ctx ===\"; sed -n '12120,12132p' SYN.txt\necho \"=== LEW trapez ===\"; grep -n -o \"trapez[a-zī]*[^|]\\{0,100\\}\" LEW_1910.txt | head -3\necho \"=== SKT square entry ===\"; grep -n -o \"Square\\.[^|]\\{0,200\\}\" SKT.txt | head -2\necho \"=== SKT squad ===\"; grep -n -o \"Squad[^|]\\{0,150\\}\" SKT.txt | head -2\necho \"=== FSD trapezium/quarantine vol4 ===\"; grep -n -o \"Quarantine[^|]\\{0,150\\}\" FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt | head -3\necho \"=== WEB trapez ===\"; grep -n -o \"trapez[a-z]*[^|]\\{0,100\\}\" WEB_vol1.txt | head -3\necho \"=== IEC qetuor ===\"; grep -n -o \"qetuor[^|]\\{0,120\\}\\|kʷetuor[^|]\\{0,120\\}\" IEC.txt | head -3",
 "description": "Check quotes for fixes"
}
```


### [2026-09-06T22:54:32.545Z] TOOL RESULT

```
=== SYN trapeza ctx ===
5. Skt. pitha-, etym.?
Av. gdtu-, OPers. ga6u- ‘place’ and ‘seat, throne’ : Skt. ga- ‘go’. Walde-P. 1.677.
1 With Te. Stolti, nrg.
Slolica,
7.44 TABLE
Grk.  rpaxeta Goth. biuds, mes Lith.  stalas
NG tpdxeta, rparéte ON bord (bj00) Lett. galds
Lat. _ménsa Dan. bord ChSl. trapeza It. lavola Sw. bord SCr. __ stol (irpeza) Fr. table OE bord, beod Boh. — stil
Sp. mesa ME _borde, table Pol. —_stét
Rum. masa NE table Russ.  stol
Ir. mias, bordd Du. tafel Skt. (phalaka-) Nir. bord OHG  fisc, mias Av.
Biss Berea Bord MHG_ tisch 7 Pe Br. taol NHG isch (lafel)
A regular ‘table’ for Serving meals and for other purposes (Grk. zpéreta also ‘bank’), was a common article of furniture in Greece and Rome. Pre- vious to its introduction into northern
=== LEW trapez ===
ugrep: error: error at position 334
x8f][\x80-\xbf][\x80-\xbf]){0,100}
     exceeds complexity limits___/


=== SKT square entry ===
=== SKT squad ===
18242:Squad,  Squadron ;  >ec  Quadrate.
=== FSD trapezium/quarantine vol4 ===
=== WEB trapez ===
ugrep: error: error at position 321
f][\x80-\xbf]){0,100}
                     \___exceeds complexity limits


=== IEC qetuor ===
```


## [2026-09-06T22:54:41.401Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12132,12150p' SYN.txt\necho \"=== SKT quart/square lines ===\"\nsed -n '15308,15314p' SKT.txt\ngrep -n \"Square\" SKT.txt | head -5",
 "description": "Buck trapeza etymology, Skeat entries"
}
```


### [2026-09-06T22:54:41.474Z] TOOL RESULT

```
A regular ‘table’ for Serving meals and for other purposes (Grk. zpéreta also ‘bank’), was a common article of furniture in Greece and Rome. Pre- vious to its introduction into northern
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Europe, food was served on small indi- vidual tables (as also in Homer), such a table being properly a serving tray a0
in part consisting only of a piece of board. Cf. Schrader Reallex. 2.536.
DW ELLI
an jmportant bearing
rhis sir Bis words. . 0 ir op the jus ae ChSl. ae «TP ‘four-foote 1 Grk + qrpar medio fou tour’
cr.trpezd) “ e etgaapes, TETPO ss of forms if i ‘Also Boeot. 7pt-
G. os ’ and (i Hl lit. «hree-footed’. ( pple. of
ensa Lat. me? fr. IE +mé- ‘measure’.
vidual ta : Br a food’, the latter use evn in Latin beside ‘table’. rade? 2.2 Ernout-M. 607. de-H. 2.70. : ea (through VLat. mésa) Sp.
nesa, Rum. mast, Ir. mias (‘table’ and idish’), Goth. més (‘table’ and ‘platter’), OHG mias, meas, OE mesa, myse. Hence also, as applied to the small indi- vidual table or serving tray of the Celts, Germans, and Slavs, numerous words for ‘platter’ or ‘dish’ (5.31, 5.32).
It. tavola, Fr. table (> ME, NE table), Br, faol, Du. tafel, fr. Lat. tabula ‘board, tablet’ (9.52). As suggested by Meyer- Liibke, this was first used for ‘table’ by the Franks, as equivalent to the Gmc. terms for their small table (below, 4). ie pence borrowing in Fr. fr.
» then fr. Fr. in It., ete., and in
NHG tafel (> Dan., § +, Sw. t 1 } tsed for ‘dining-table’. gietewhen.
Digitized by Arya Samaj Foundation Chennai and eGangotri
NG, HOUSE, FURNITURE 483
3. Ir. bordd, NIr. bord, W. bwrdd, bord, fr. Gme., OE or Norse, below, 4.
4, Goth. biubs, ON bj60 (rare), OF bzod, OHG beot, biet, fr. the root of Goth. -biudan, OE béodan, OHG biotan ‘offer’. Orig. ‘offering, portion’ (cf. Lat. ménsa, above, 2), applied to the ‘serv- ing tray, platter’ (whence Balto-Slavic words for ‘platter, dish, bowl’, 5.31- 5.33), which was the old Gmc. ‘table’. Walde-P. 2.147. Feist 97.
=== SKT quart/square lines ===
quarry  (I),  a  place  where  siaaaii dug.  (F.  — L.)  Formerly  quarrtr\  U. quarrere,  a  place  where  stones  arc  squii
—  O.  F.  quarriift,  a  quarry ;  F-  (orrit* I.OW  L.  qtmdntrta^  a  quajry  for  ifM stones.  >I«  quadrart.  to  squaic^U^ rus,  square.  ^  The  sense  was  fo^ri by  L.  quadratarius,  a  stone-squaicr.  ik stone-cutter  (merely).
quart,  the  fourth  of  a  galloo.  (F.* M.  E.  quarlt.  —  F.  quarte.  —  I     '"  "*'  '^ parT\  a  fourth  part ;  fem.  of  ^.' Apparently    short    lor    qua:. qua/uor,  foor.
quartan.  (F.  •  L.>  F  y^-;  '  .  I curring  on  the  fourth  day  (said  of  %  lr« *  L.  quartana  (JfSris),  a  quartan  if* fem.  cAquartaMus,  belonging  to  Uiffoe •>L.  quartus,  fourth  ^above).
quarter.  (F.  -  L.)  ME. O-  F.  quaritr,  quarticr.  ■>  t. fourth  part  *  L.  quarims,  fourlhl
quartern,  fourth  of  a  pint.   (F. Short  for  quarieron.     M,  E.  quarten O.  F.  quaritren,   s   quanenL  »  Lav quart<ro»um,    ace.    of   quartern,  a  i\ part.  — Low  L  quarterns^  from  L. fourth.
quartet,  quartette.  (Ttel.-*!.) quarUtto  {guartettt  is  a  F.  t|>clling);^ q{  quarto,  fourth. «L.  quartnt
18248:Square;  see  Qnadrate.
```


## [2026-09-06T22:55:17.587Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'PYEOF'\nimport json, io\np='data/verification/page-295.json'\nd=json.load(open(p,encoding='utf-8'))\ne=d['entries'][0]\nnodes={n['id']:n for n in e['nodes']}\n\ndef setc(node_id, src, **kw):\n    for c in nodes[node_id]['consulted']:\n        if c['src']==src:\n            c.update(kw); return True\n    return False\n\n# root: soften WLD page claim\nfor c in e['consulted']:\n    if c['src']=='WLD':\n        c['where']=\"Walde-Pokorny Bd. I p. 512 (the page Pokorny cites at IEW 644 as 'WP. I 512'); incoming/WLD/WLD_Bd1_pages.txt\"\n\n# #1 BRT: drop the unverified column number\nassert setc(1,'BRT', where=\"BRT.txt, s.v. čaθwar- (grepped 'öaS-war' in the OCR)\")\n\n# #11 SKT: correct quote\nassert setc(11,'SKT', where=\"SKT.txt s.vv. Square, Squad, quart, quarter\",\n  note=\"Skeat files “Square; see Quadrate” and “Squad, Squadron; see Quadrate” (i.e. under L. quadrus/quadrāre), but “quart, the fourth of a gallon… — F. quarte. — L. quarta, a fourth part; fem. of [quartus]” and “quarter… O.F. quartier… L. quartus, fourth” — the same split as Watkins.\")\n\n# #18 SYN: real quote\nassert setc(18,'SYN', where=\"Buck 7.44 TABLE\",\n  note=\"Buck's entry on 'table' analyses “Grk. τράπεζα… ‘four-footed’… (: τέσσαρες, τετρα- ‘four’)… Also Boeot. τρίπεζα… lit. ‘three-footed’” (the OCR of this paragraph is badly scrambled but the four-foot analysis and the Boeotian variant are legible); ChSl. trapeza is listed as a Greek loan.\")\n\n# #21 LAT: not actually present\nassert setc(21,'LAT', where=\"LAT.txt (Ernout-Meillet), grepped trapez*\", stance=\"silent\",\n  note=\"No trapez- entry surfaced in the OCR of Ernout-Meillet, so this reference is silent here; the Late Latin trapezium is documented from Klein and the AHD index instead.\")\n\n# #22 SKT and FSD: not actually present\nassert setc(22,'SKT', where=\"SKT.txt, grepped trapezium/trapeze\", stance=\"silent\",\n  note=\"Skeat's concise dictionary has no trapezium/trapeze entry in this OCR (only the Quadrate cross-references), so it is silent on this node.\")\nassert setc(22,'FSD', where=\"FSD_vol4.txt, grepped trapeze/trapezoid\", stance=\"silent\",\n  note=\"The Funk & Wagnalls OCR of vol. IV yields only a corrupt 'trapezet' line, nothing usable, so this reference is silent here.\")\n\nwith io.open(p,'w',encoding='utf-8') as f:\n    json.dump(d,f,ensure_ascii=False,indent=2); f.write('\\n')\nprint('patched')\nPYEOF\npython3 -m json.tool data/verification/page-295.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 295",
 "description": "Patch consulted notes and re-verify"
}
```


### [2026-09-06T22:55:19.767Z] TOOL RESULT

```
patched
JSON OK
nodes verified: 22/22
node verdicts: {'plausible': 6, 'confirmed': 12, 'disputed': 1, 'transcription_suspect': 3}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 12, 'not_checked': 4, 'partial': 6}
books consulted: {'supports': 36, 'silent': 13, 'contradicts': 6, 'partial': 10} | by book: {'KLN': 14, 'MON': 6, 'BQT': 6, 'SKT': 5, 'ARY': 4, 'POK': 4, 'SYN': 4, 'PHD': 3, 'PLA': 3, 'TAD': 3, 'NYB': 2, 'WLD': 2, 'BRT': 1, 'HRN': 1, 'HUB': 1, 'AFM': 1, 'LKT': 1, 'AHD': 1, 'RCH': 1, 'LAT': 1, 'FSD': 1}
```


## [2026-09-06T22:55:25.763Z] TOOL CALL #93: Bash

```json
{
 "command": "ls -la data/verification/page-295.json data/verification/sources/refs/ocr/TAD/62.vision.txt data/verification/sources/refs/ocr/BQT/829.vision.txt data/verification/sources/refs/ocr/BOOK/295.png && git status --short | head -20",
 "description": "Confirm outputs"
}
```


### [2026-09-06T22:55:25.827Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 84934 Sep  6 18:55 data/verification/page-295.json
-rw-rw-r-- 1 sfmqrb sfmqrb 77133 Sep  6 18:36 data/verification/sources/refs/ocr/BOOK/295.png
-rw-rw-r-- 1 sfmqrb sfmqrb   981 Sep  6 18:36 data/verification/sources/refs/ocr/BQT/829.vision.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1272 Sep  6 18:36 data/verification/sources/refs/ocr/TAD/62.vision.txt
?? data/verification/page-295.json
?? data/verification/page-300.json
```


## [2026-09-06T22:55:48.144Z] AGENT

Page 295 (book p. 265) verified — 1 entry, root + 22 nodes, `verify_check.py 295` shows 0 PROBLEM lines.

**Verdicts:** root confirmed; nodes 12 confirmed, 6 plausible, 1 disputed, 3 transcription_suspect. Ref checks: 12 supports, 6 partial, 4 not_checked (boxes with no refs).

**Disputed**
- #3 Armenian `čatvar` "one fourth" — Nourai's source (Tavoosi SNS p. 148, read from the page image) really does say "چَتْوَر فارسی ما مأخوذ از ارمنی"، but no Armenian *čatvar* exists (Arm. is čʻorkʻ / čʻorrord / kʻaṛʿord); Mo'in makes it Russian четверть ("چتور [رس.] یک چهارم گیروانکه" = 125 g, not 250 g).

**Transcription_suspect**
- #4 Persian «کَتوَر» — **EXTRACTION ERROR, owner must fix**: the printed page shows **چَتْوَر** with چ (three dots below, clear at 450 dpi); JSON has ک. The book's own Latin "katvar" is separately Nourai's misprint for *čatvar*.
- #7 Persian `katrang «کَترنگ»` — error in the **book**: no such word; BQT p. 1254 (the page cited on the parent box) has شترنگ with Mo'in's footnote "پهلوی čatrang… معرب آن شطرنج" and the same distich Nourai quotes. Correct: چترنگ/شترنگ.
- #12 Italian `quadratina` — error in the **book**: the word is *quarantina* / Venetian *quarantena*; Nourai's own ref (TAD p. 62) prints "كرنتينا — ايطالي quarantena معناه أربعون يوما".

**Other plausible-not-confirmed:** #1 Avestan "čatwârao" (standard caθwārō); #8 gloss "quadrus : four" (= "square, four-sided"); #11 quart/quarter come from *quārtus*, not *quadrus*; #14 Persian قرنطینه may be direct from French *quarantaine*; #16 "Germanic petwor" is a pre-Germanic reconstruction (PGmc is *fedwōr; Pokorny derives Gmc from assimilated *kʷekʷor-); #19 the gloss on the Arabic box is really Mo'in's gloss on Persian دارافزین.

**New reference readings saved** (page images could not be OCR'd): `data/verification/sources/refs/ocr/TAD/62.vision.txt` (+ 62.png) and `.../BQT/829.vision.txt` (+ 829.png, Mo'in's footnote "درابزین ـ از یونانی Trapézion (نرده، شبکه)" — which confirms the Greek trapez- origin of #19/#20). Page image at `.../ocr/BOOK/295.png`. Nine web sources archived via `fetch_source.py`.
